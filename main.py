import sqlite3
import requests

from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, make_response, redirect, url_for


app = Flask(__name__)

@app.route('/')
def main():
	
	return render_template('index.html')

@app.route('/news')
def news():
	
	url = 'https://russian.rt.com/tag/ekologiya'
	res = requests.get(url)
	soup = BeautifulSoup(res.content, 'html.parser')
	data = soup.find('a', class_='link link_color').text
	body = soup.find('div', class_='card__summary card__summary_all-new_cover').text
	#news = [{"header":"Fake news: Trump died", "body":"Sorry, world."}, {"header":"Fake news: Trump now alive", "body":"Sorry, world again."}]
	news = [{"header": data, "body": body}]
	return render_template('news.html', news=news)

@app.route('/sovety')
def sovety():

	return render_template('sovety.html')
if __name__ == '__main__':
	app.run(port=1000, host='0.0.0.0', debug=True)