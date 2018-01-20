from flask import *
import api

app = Flask(__name__)

LANDING_PAGE = "/"
BASE_URL = "/api"
HOST = "0.0.0.0"
PORT = 65010

@app.route(LANDING_PAGE)
def home():
	h = "http://"+HOST
	if PORT!=80:
		h = "{}:{!s}".format(h,PORT)
	return """<html>
<head>
<title>Prequel API - It's Alive!</title>
</head>
<body>
<h1>Prequel API is indeed running right now!</h1>
<h3>To use:</h3>
<p>To get the latest update, go to <a href="{host}{baseurl}/latest">{host}{baseurl}/latest</a>.</p>
<p>To get the latest 5 updates, go to <a href="{host}{baseurl}/latest/5">{host}{baseurl}/latest/5</a>. (Customizable!)</p>
<p>To get the update from a specific date, go to "{host}{baseurl}/from/{{year}}/{{month}}/{{day}}".
</body>
</html>""".format(host=h,baseurl=BASE_URL)

app.register_blueprint(api.api,url_prefix=BASE_URL)

if __name__=="__main__":
	app.run(HOST,PORT)
