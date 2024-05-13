from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from os.path import exists
import secrets

secret = secrets.token_urlsafe(32)

db_file = "values.db"
# Configure CS50 Library to use SQLite database
if not exists(db_file):
	open(db_file, 'a')
db = SQL('sqlite:///values.db')

# Configure application
app = Flask(__name__)
app.secret_key = secret

@app.route('/')
def home():
	# Home page
	return render_template('home.html')


@app.route('/calculate', methods=['POST'])
def calculate():
	a = request.form.get('a')
	b = request.form.get('b')
	c = request.form.get('c')

	if not a or not b or not c:
		flash("Input values for a, b & c")
		return redirect('/')
	else:
		a = float(a)
		b = float(b)
		c = float(c)

	s = (a + b + c) / 2
	s = round(s, 3)

	x = round(s - a, 3)
	y = round(s - b, 3)
	z = round(s - c, 3)


	if x < 0 or y < 0 or z < 0:
		flash("Invalid triangle")
		return redirect("/")

	area = (s * x * y * z) ** 0.5
	area = round(area, 3)

	db.execute("CREATE TABLE IF NOT EXISTS triangle (triangle_no INTEGER PRIMARY KEY, a INTEGER, b INTEGER, c INTEGER, s INTEGER, 's - a' INTEGER, 's - b' INTEGER, 's - c' INTEGER, area REAL)")
	db.execute("INSERT INTO triangle (a, b, c, s, 's - a', 's - b', 's - c', area) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", a, b, c, s, x, y, z, area)

	return redirect('/results')


@app.route('/results', methods=['GET', 'POST'])
def results():
	if request.method == 'GET':
		try:
			results = db.execute("SELECT * FROM triangle")
			if not results:
				flash("No results to show")
				return redirect('/')
			return render_template('results.html', results=results)
		except:
			flash("No results to show")
			return redirect('/')
	if request.method == 'POST':
		triangle_no = int(request.form.get('triangle_no'))
		db.execute("DELETE FROM triangle WHERE triangle_no = ?", triangle_no)
		return redirect('/results')
