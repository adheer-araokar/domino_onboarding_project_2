# #!/usr/bin/env python3
#
# import sys
# from time import sleep
#
# from controller.car_controller import api_v1
# from data_plotter.plotter import plot_from
# from latlng_consumer.consumer import consume
# from latlng_producer.producer import produce
# from flask import Flask
#
# import threading
#
#
# app = Flask(__name__)
# data_sink = []
#
#
# @app.route("/")
# def home():
#     return plot_from(data_sink)
#
#
# def main():
#     args = sys.argv[1]
#
#     if args == 'p':
#         # t1 = threading.Thread(target=produce())
#         # t1.start()
#         # t1.join()
#         for i in range(10):
#             t = threading.Thread(target=produce)
#             t.start()
#             sleep(1)
#     else:
#
#         port = sys.argv[2]
#
#         name = 't1'
#         t = threading.Thread(name=name, target=consume, kwargs={"sink": data_sink})
#         t.start()
#
#         app.register_blueprint(api_v1)
#         app.run(debug=True, port=port)
#
#
# if __name__ == '__main__':
#     main()
