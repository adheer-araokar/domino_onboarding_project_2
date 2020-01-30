#!/usr/bin/env python3

import sys
from controller.car_controller import api_v1
from data_plotter.plotter import plot_from
from db.db import setup_schema
from latlng_consumer.consumer import consume
from flask import Flask

import threading


app = Flask(__name__)


@app.route("/get_car_data/<car_name>", methods=['GET'])
def home(car_name):
    return plot_from(car_name)


def main():

    port = sys.argv[1]

    t = threading.Thread(target=consume)
    t.start()

    app.register_blueprint(api_v1)
    app.run(debug=True, port=port)
    setup_schema()


if __name__ == '__main__':
    main()
