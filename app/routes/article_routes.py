from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Article, db  # Adjust this import path based on your structure

article_bp = Blueprint('articles', __name__)

@article_bp.route("/", methods=["GET"])
def list_articles():
    articles = Article.query.all()
    result = []
    for a in articles:
        result.append({
            "id": a.id,
            "title": a.title,
            "ticket_number": a.ticket_number,
            "created_by": a.created_by,
            "created_date": a.created_date.isoformat(),
            "published_date": a.published_date.isoformat() if a.published_date else None,
            "stage": a.stage,
            "days_to_publish": a.days_to_publish,
            "delay_reason": a.delay_reason
        })
    return jsonify(result)

@article_bp.route("/", methods=["POST"])
def create_article():
    data = request.get_json()
    article = Article(
        title=data["title"],
        ticket_number=data["ticket_number"],
        created_by=data["created_by"],
        created_date=datetime.utcnow(),
        stage="Draft"
    )
    db.session.add(article)
    db.session.commit()
    return jsonify({"message": "Article created", "id": article.id}), 201

@article_bp.route("/<int:article_id>/publish", methods=["PUT"])
def publish_article(article_id):
    article = Article.query.get(article_id)
    if not article:
        return jsonify({"error": "Article not found"}), 404

    if article.published_date:
        return jsonify({"message": "Article already published"}), 400

    published_date = datetime.utcnow()
    article.published_date = published_date
    article.stage = "Approved/Published"

    days_to_publish = (published_date - article.created_date).days
    article.days_to_publish = days_to_publish

    if days_to_publish > 2:
        article.delay_reason = request.json.get("delay_reason", "No reason provided")

    db.session.commit()

    return jsonify({
        "message": "Article published",
        "days_to_publish": days_to_publish,
        "delayed": days_to_publish > 2
    })
