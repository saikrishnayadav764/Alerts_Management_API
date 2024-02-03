import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    # Gmail credentials
    gmail_username = 'bunnybune47@gmail.com'
    gmail_password = 'fazyhizswqhfntyl'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = gmail_username
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(gmail_username, gmail_password)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


    
def get_current_price(crypto_symbol, data):
    output_file_path="crypto_data.txt"
    with open(output_file_path, "w") as file:
        file.write(str(data))
    current_price = data[crypto_symbol]["USD"]
    return int(round(current_price))

def notify_user(user_id, target_price, current_price):
    from .models import User
    # Fetching the user's email from the database based on user_id
    user = User.find_by_username(user_id)
    if user:
        user_email = user['email']
        subject = "Price Alert Triggered"
        body = f"Your price alert for {target_price} has been triggered. Current price: {current_price} dollar"

        # Sending email notification
        send_email(user_email, subject, body)

