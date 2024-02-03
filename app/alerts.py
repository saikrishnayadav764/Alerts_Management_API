from flask import Blueprint, jsonify, request
from .models import Alert
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import cache 


alerts_bp = Blueprint('alerts', __name__, url_prefix='/alerts')



# Get request to get all alerts
@alerts_bp.route('/', methods=['GET'])
@jwt_required()
@cache.cached(timeout=300)
def get_alerts():
    user_id = get_jwt_identity()
    status_filter = request.args.get('status', None)
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    query = {'user_id': user_id}
    if status_filter:
        query['status'] = status_filter

    alerts = Alert.collection.find(query).skip((page - 1) * per_page).limit(per_page)
    alerts_list = [{'alert_id': alert['alert_id'], 'crypto_symbol': alert['crypto_symbol'], 'target_price': alert['target_price'], 'status': alert['status']} for alert in alerts]
    return jsonify(alerts_list), 200

# Delete request to delete particular alert
@alerts_bp.route('/<alert_id>', methods=['DELETE'])
@jwt_required()
def delete_alert(alert_id):
    user_id = get_jwt_identity()
    alert = Alert.find_by_alert_id_and_user(alert_id, user_id)

    if alert:
        Alert.delete(alert_id)
        return jsonify({"message": "Alert deleted successfully"}), 200
    else:
        return jsonify({"message": "Alert not found"}), 404
