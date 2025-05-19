from flask import Blueprint, render_template, request, redirect
from flask import session as flask_session
from application.logger import logger
from application.database.models import Account
from application.database import session
from sqlalchemy.exc import IntegrityError





router = Blueprint("auth", __name__, url_prefix="/auth")

@router.route("/login")
def login_page_handler():
    logger.info("login page requested")
    return render_template("login.html")

@router.route("/registration")
def registration_page_handler():
    logger.info("registration page requested")
    return render_template("registration.html")


@router.route("/registration", methods=["POST"])
def registration_submit_handler():
    data = request.form
    logger.info(f"Registration handler data {data}")
    username = data.get("username")
    password = data.get("password")
    account = Account(username=username, password=password)
    try:
        session.add(account)
        session.commit()
        logger.info(f"User created with ID={account.id}")
    except IntegrityError:
        session.reset()
        return render_template("error.html", message="User already exists!")
    return redirect("/auth/login")


@router.route("/login", methods=["POST"])
def login_submit_handler():
    data = request.form
    logger.info(f"login handler data {data}")
    username = data.get("username")
    password = data.get("password")
    # account = Account(username=username, password=password)
    if not username or not password:
        logger.info(f"Missing logging fields")
        return render_template("error.html", message="All fields are required!")

    # try:
    else:
        account_data = session.query(Account).filter_by(username=username).first()
        if account_data is None:
            return render_template("error.html", message="Invalid username or password")

        elif password == account_data.password:
            logger.info(f"User logged successfully id={username}")
            flask_session["user_id"] = account_data.id
            return redirect("/shop")
        else:
            logger.info(f"Failed login attempt username={username}")
            return render_template("error.html", message="Invalid username or password")












