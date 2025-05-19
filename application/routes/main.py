from flask import Blueprint, render_template, request
from application.logger import logger

router = Blueprint("main", __name__)

@router.route("/")
def main_page_handler():
    logger.info("main page requested")
    return render_template("index.html")