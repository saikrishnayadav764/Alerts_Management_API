from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Alert
import uuid
alert_id = str(uuid.uuid4())

from bson import ObjectId

bp = Blueprint('main', __name__)

# Create an alert
@bp.route('/alerts/create', methods=['POST'])
@jwt_required()
def create_alert():
    user_id = get_jwt_identity()
    data = request.get_json()
    alert_id = str(uuid.uuid4())
    alert = Alert(alert_id=alert_id, user_id=user_id, target_price=data['target_price'], crypto_symbol=data['crypto_symbol'], status="created")
    alert.save()

    return jsonify({"message": "Alert created successfully"}), 201

# Delete an alert
@bp.route('/alerts/delete/<alert_id>', methods=['DELETE'])
@jwt_required()
def delete_alert(alert_id):
    user_id = get_jwt_identity()
    alert = Alert.find_by_id_and_user(alert_id, user_id)

    if alert:
        alert.delete()
        return jsonify({"message": "Alert deleted successfully"}), 200
    else:
        return jsonify({"message": "Alert not found"}), 404

# Fetch all alerts
@bp.route('/alerts', methods=['GET'])
@jwt_required()
def get_alerts():
    user_id = get_jwt_identity()
    status_filter = request.args.get('status', 'created')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    query = {'user_id': user_id}
    if status_filter:
        query['status'] = status_filter

    alerts = Alert.collection.find(query).skip((page - 1) * per_page).limit(per_page)
    alerts_list = [{'alert_id': alert['alert_id'], 'crypto_symbol': alert['crypto_symbol'], 'target_price': alert['target_price'], 'status': alert['status']} for alert in alerts]

    return jsonify(alerts_list), 200



# Background task to check and notify triggered alerts
@bp.route('/alerts/check', methods=['GET'])
@jwt_required()
def check_alerts():
    triggered_alerts = Alert.check_and_notify_triggered_alerts()
    return jsonify({"triggered_alerts": triggered_alerts}), 200

