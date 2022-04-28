from flask import Blueprint,render_template,g

bp = Blueprint("qa",__name__,url_prefix="/")

@bp.route("/")
def index():
    #questions = QuestionModel.query.order_by(db.text("-create_time")).all()
    return render_template("index.html")