from . import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import requests
from .email_notifier import send_email, notify_user, get_current_price

class User:
    collection = mongo.db.users

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def save(self):
        self.collection.insert_one({
            'username': self.username,
            'password': self.password,
            'email': self.email
        })

    @staticmethod
    def find_by_username(username):
        return User.collection.find_one({'username': username}, {'_id': 0})

class Alert:
    collection = mongo.db.alerts

    def __init__(self, alert_id, user_id, target_price, crypto_symbol, status):
        self.user_id = user_id
        self.target_price = target_price
        self.status = status
        self.created_at = datetime.utcnow()
        self.crypto_symbol = crypto_symbol
        self.alert_id = alert_id

    def save(self):
        self.collection.insert_one({
            'alert_id': self.alert_id,
            'user_id': self.user_id,
            'target_price': self.target_price,
            'crypto_symbol': self.crypto_symbol,
            'status': self.status,
            'created_at': self.created_at
        })

    def update(self, new_status):
        Alert.collection.update_one({'alert_id': self.alert_id}, {'$set': {'status': new_status}})

    @staticmethod
    def find_by_id_and_user(alert_id, user_id):
        return Alert.collection.find_one({'_id': alert_id, 'user_id': user_id})
    
    @staticmethod
    def find_by_alert_id_and_user(alert_id, user_id):
        return Alert.collection.find_one({'alert_id': alert_id, 'user_id': user_id})

    @staticmethod
    def delete(alert_id):
        Alert.collection.delete_one({'alert_id': alert_id})

    @staticmethod
    def check_and_notify_triggered_alerts():
        triggered_alerts = []
        
        # Fetching alerts from the database
        alerts = list(Alert.collection.find({'status': 'created'}))
        API_KEY = 'a84341ca60b24f5f3107af219b1b52acd53cac0defbdf2527cd42d1442099f1b'
        url = f'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,USDC,XRP,USDT,SUI,ICP,BNB,ADA,FIL&tsyms=USD&api_key={API_KEY}'
        response = requests.get(url)
        data = response.json()

        for alert in alerts:
            current_price = get_current_price(alert['crypto_symbol'], data) 
            if int(current_price) == int(alert['target_price']):
                dm = { 'alert_id': alert['alert_id'], 'target_price': alert['target_price'],'crypto_symbol': alert['crypto_symbol']}
                triggered_alerts.append(dm)
                
                alert_instance = Alert(alert['alert_id'], alert['user_id'],  alert['target_price'], alert['crypto_symbol'], 'triggered')
                alert_instance.update('triggered')
   

                # Notifying user via email
                notify_user(alert['user_id'], alert['crypto_symbol'], current_price)

        return triggered_alerts