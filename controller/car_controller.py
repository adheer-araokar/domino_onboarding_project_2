import connexion

from flask import Blueprint, Response

from db.db import get_car_data_for_key

api_v1 = Blueprint('api', 'api', url_prefix='/api/v1')


@api_v1.route('/get_car_data', methods=['POST'])
def get_car_data(body=None):

    if connexion.request.is_json:
        try:
            body = connexion.request.get_json()
        except Exception as e:
            return Response(str(e), status=400)
        return get_car_data_internal(body)

    return Response("Invalid Data! Data is not JSON!", status=400)


def get_car_data_internal(body):

    try:
        key = body["car_name"]
        return Response(response=get_car_data_for_key(key), status=200, mimetype="application/json")
    except Exception as e:
        return Response(str(e), status=400)
