from flask import Flask, jsonify, request
import csv

all_articles = []
with open("articles.csv", encoding = 'utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)
@app.route("/get-article")
def get_article():
    article_data = {
        "url": all_articles[0][11],
        "title": all_articles[0][12],
        "text": all_articles[0][13],
        "lang": all_articles[0][14],
        "total_events": all_articles[0][15]
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article",methods = ["POST"])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unliked-article",methods = ["POST"])
def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201
