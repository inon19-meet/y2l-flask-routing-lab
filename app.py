from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/shop')
def shop():
	oranges = ["orange", "blue orange", "orange with smiley"]
	return render_template(
		"shop.html",
		oranges=oranges,
		no_oranges=False)


if __name__ == '__main__':
   app.run(debug = True)