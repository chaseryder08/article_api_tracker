from flask import Flask
from routes.article_routes import article_bp
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///articles.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(article_bp, url_prefix="/articles")

if __name__ == "__main__":
    app.run(debug=True)
