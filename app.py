import os
import shutil
import csv
import sys
import os
import sqlite3
""" from flask_sqlalchemy import SQLAlchemy """
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
port = int(os.getenv("PORT", 5000))

bootstrap = Bootstrap(app)


	 

conn = sqlite3.connect('people.db', check_same_thread=False)
print("Opened database successfully")

# Configurations
app.config['SECRET_KEY'] = 'blah blah blah blah'



# ROUTES!
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html', result={})

@app.route('/help')
def help():
	text_list = []
	# Python Version
	text_list.append({
		'label':'Python Version',
		'value':str(sys.version)})
	# os.path.abspath(os.path.dirname(__file__))
	text_list.append({
		'label':'os.path.abspath(os.path.dirname(__file__))',
		'value':str(os.path.abspath(os.path.dirname(__file__)))
		})
	# OS Current Working Directory
	text_list.append({
		'label':'OS CWD',
		'value':str(os.getcwd())})
	# OS CWD Contents
	label = 'OS CWD Contents'
	value = ''
	text_list.append({
		'label':label,
		'value':value})
	return render_template('help.html',text_list=text_list,title='help')


@app.route('/list_files', methods=["GET"])
def list_files():
	files_dict = {}
	files_list = os.listdir('./static/pics/')
	for file in files_list:
		file_name = './static/pics/' + file
		files_dict[file] = os.stat(file_name).st_size
	return render_template('list_files.html', result=files_dict)

@app.route('/show_pic', methods=["GET"])
def show_pic():
	ret = []
	return render_template('show_pic.html', result=ret)


# search by name function
@app.route('/show_pic', methods=["POST"])
def show_pic_name():
	picture_mem = request.form["picture_mem"]
	cur = conn.cursor()
	cur.execute('SELECT * FROM people where Pictures = (?) ', (picture_mem, ))
	result = cur.fetchall()
	print(result)
	return render_template('show_pic.html', result=result)

@app.route('/show_pic_id', methods=["GET"])
def show_picid():
	ret = []
	return render_template('show_pic_id.html', result=ret)


# search by name function
@app.route('/show_pic_id', methods=["POST"])
def show_pic_id():
	id_mem = request.form["id_mem"]
	cur = conn.cursor()
	cur.execute('SELECT * FROM people where ID = (?) ', ( id_mem, ))
	result = cur.fetchall()
	print(result)
	return render_template('show_pic_id.html', result=result)

@app.route('/search_sal', methods=["GET"])
def search_room():
	ret = []
	return render_template('salary_search.html', result=ret)


# search by name function
@app.route('/search_sal', methods=["POST"])
def search_by_room():
	sal_st = request.form["sal_start"]
	sal_end = request.form["sal_end"]
	if sal_st == '' and sal_end == '':
		sal_st = 0
		sal_end = 0
	if sal_st == '':
		sal_st = 0
	if sal_end == '':
		sal_end = 0
	cur = conn.cursor()
	cur.execute('SELECT * FROM people WHERE Year between (?) and (?) ', (sal_st, sal_end, ))
	result = cur.fetchall()
	return render_template('salary_search.html', result=result)

@app.route('/search_name', methods=["GET"])
def search_name():
	ret = []
	return render_template('name_search.html', result=ret)


# search by name function
@app.route('/search_name', methods=["POST"])
def search_by_name():
	name = request.form["name"]
	cur = conn.cursor()
	cur.execute('SELECT * FROM people WHERE Person = (?)', (name, ))
	result = cur.fetchall()
	return render_template('name_search.html', result=result)	


@app.route('/insert', methods=["GET"])
def insert_by_room():
	cur = conn.cursor()
	cur.execute('SELECT * FROM  people')
	result = cur.fetchall()
	return render_template('insert.html', result=result)


@app.route('/insert', methods=["POST"])
def insert():
	if request.method == 'POST':
		name = request.form['name']
		salary = request.form['salary']
		room = request.form['room']
		telnum = request.form['telnum']
		picture = request.form['picture']
		keywords = request.form['keywords']
	cur = conn.cursor()
	cur.execute('INSERT INTO people VALUES(?,?,?,?,?,?)', (name, salary, room, telnum, picture, keywords))
	conn.commit()
	return redirect(url_for("just_hello1"))

	
@app.route('/update', methods=["GET"])
def update_by_room():
	cur = conn.cursor()
	cur.execute('SELECT * FROM people where Person is Not Null')
	result = cur.fetchall()
	return render_template('update.html', result=result)


@app.route('/update', methods=["POST"])
def update():
	name = request.form.get('opt')
	caption = request.form["caption"]
	cur = conn.cursor()
	if  caption != '':
		cur.execute('UPDATE people SET Description = (?) WHERE Person = (?)', (caption, name,))
	conn.commit()
	return redirect(url_for("just_hello"))	


@app.route('/delete', methods=["GET"])
def delete_by_name():
	ret = []
	cur = conn.cursor()
	cur.execute('SELECT * FROM people where Person is Not Null')
	result = cur.fetchall()
	return render_template('delete.html', result=result)	

@app.route('/delete', methods=["POST"])
def delete():
	name = request.form.get('opt')
	cur = conn.cursor()
	if name != '':
		cur.execute('DELETE FROM people WHERE Person = (?)', ( name, ))
	conn.commit()
	return redirect(url_for("just_hello2"))	

app.config["UPLOADS"] = "static\pics"

@app.route('/upload', methods = ["GET","POST"])	
def upload():
	if request.method == "POST":


		if request.files:

			image = request.files["image"]

			image.save(os.path.join(app.config["UPLOADS"], "nigel.jpg"))

			print(image)

			return redirect(request.url)



	return render_template('upload.html')




	
@app.route('/list', methods=[ "GET"])
def just_hello():
	cur = conn.cursor()
	sql = "SELECT * FROM people where Person is Not Null;"
	cur.execute(sql)
	result = cur.fetchall()
	return render_template('update.html', result=result)

@app.route('/list1', methods=["GET"])
def just_hello1():
	cur = conn.cursor()
	sql = "SELECT * FROM people where Person is Not Null;"
	cur.execute(sql)
	result = cur.fetchall()
	return render_template('insert.html', result=result)


@app.route('/list2', methods=["GET"])
def just_hello2():
	cur = conn.cursor()
	sql = "SELECT * FROM people where Person is Not Null;"
	cur.execute(sql)
	result = cur.fetchall()
	return render_template('delete.html', result=result)




@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)