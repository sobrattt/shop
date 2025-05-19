from click.core import augment_usage_errors
from flask import Blueprint, render_template, redirect, request
from application.logger import logger
from application.database import session
from application.database.models import Item
from flask import session as flask_session

router = Blueprint("shop", __name__, url_prefix="/shop")

@router.route("/")
def shop_page_handler():
    user_id = flask_session.get("user_id")
    if user_id is None:
        return redirect("/auth/login")
    page_number = request.args.get("page")
    query = request.args.get("query")
    if not query or query == "None":
        all_items = session.query(Item).count()
        max_page = all_items / 20
        if not page_number or int(page_number) <= 0 or int(page_number) > max_page + 1:
            page_number = 1
        items = session.query(Item).limit(20).offset((int(page_number) - 1) * 20)

    else:
        all_items = session.query(Item).where(Item.item_name.like(f"%{query}%")).count()
        max_page = all_items / 20
        if not page_number or int(page_number) <= 0 or int(page_number) > max_page + 1:
            page_number = 1
        items = session.query(Item).where(Item.item_name.like(f"%{query}%")).limit(20).offset((int(page_number) - 1) *20)


    return render_template("shop.html", items=items, page_number=int(page_number), query=query)


@router.route("/search")
def search_page_handler():
    return render_template("search.html")






