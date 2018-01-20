from flask import *
import feedparser,time,re

#feed = feedparser.parse("https://prequeladventure.com/feed/")

def get_update(date=None,amount=-1):
	feed = feedparser.parse("http://www.prequeladventure.com/feed/")
	entries = feed['entries']
	if not date:
		if amount==-1:
			return entries[0]
		else:
			return entries[0:amount]
	else:
		for entry in entries:
			n = entry.published_parsed
			if date.tm_year==n.tm_year and date.tm_mon==n.tm_mon and date.tm_mday==n.tm_mday:
				return entry
		return None

def parse_update(u):
	ret = dict()
	ret["title"]=u.title
	ret["link"]=u.link
	ret["summary"]=re.sub(r"</?[^>]+>","",u.summary.replace("&#8217;","'")).replace(" [","").replace("]","")
	ret["published"]=time.strftime("%Y-%m-%d",u.published_parsed)
	return ret

api = Blueprint("api",__name__)

@api.route("/latest")
def latest():
	update = get_update(None)
	if not update:
		return abort(500)
	return json.dumps(parse_update(update))

@api.route("/latest/<amount>")
def latest_amount(amount):
	try:
		updates = get_update(None,int(amount))
		updates = [parse_update(y) for y in updates]
		return json.dumps(updates)
	except ValueError:
		return abort(400)

@api.route("/from/<year>/<month>/<day>")
def from_date(year,month,day):
	update = get_update(time.strptime("{!s} {!s} {!s}".format(year,month,day),"%Y %m %d"))
	if not update:
		return abort(500)
	return json.dumps(parse_update(update))
