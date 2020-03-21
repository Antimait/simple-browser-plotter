import antimait
from antimait.plotting import Plotter, format_filename
import pathlib
import flask

import logging
logging.basicConfig(level=logging.INFO)

img_path = str(pathlib.Path("static", "plots").absolute())

app = flask.Flask(__name__)
gw = antimait.Gateway()


def on_connect(interface: antimait.CommInterface, description: str) -> None:
    plotter = Plotter(interface.ifc_id, img_dir=img_path)
    plotter.plot()
    interface.attach(plotter)


gw.on_connect = on_connect
gw.listen()


@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/plots")
def plots():
    img_list = ["{}.png".format(format_filename(interface.ifc_id)) for interface in gw.interfaces]
    return {"plots": img_list}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
