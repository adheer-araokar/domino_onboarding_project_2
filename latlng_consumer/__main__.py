#!/usr/bin/env python3

import socket
import sys
from controller.car_controller import api_v1
from data_plotter.plotter import plot_from
from latlng_consumer.consumer import consume
from flask import Flask

import threading


app = Flask(__name__)
data_sink = []


@app.route("/")
def home():
    return plot_from(data_sink)


def main():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    port = sys.argv[1]
    name = str(host_ip) + ":" + str(port)
    t = threading.Thread(target=consume, kwargs={"sink": data_sink, "name": name})
    t.start()

    app.register_blueprint(api_v1)
    app.run(debug=True, port=port)


if __name__ == '__main__':
    main()
