import time
import requests
from bs4 import BeautifulSoup
from application.logger import logger
from application.database.functions import add_item_info
from sqlalchemy.exc import IntegrityError
from application.database import session
from application.config import PARSING_INTERVAL
from application.utils import update_last_extraction_time, get_last_extraction_time
from datetime import datetime, timedelta

def extract_category_links(page_link):
    response = requests.get(page_link)
    if response.status_code == 200:
        logger.info(f"Got a response from: {page_link}")
    else:
        logger.error(f"failed to get a response from {page_link}")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    section = bs.find("section", {"class": "kueLqa"})
    links = section.find_all("a")
    logger.info("extracting links...")
    category_links = []
    for link in links:
        category_link = link.get("href")
        category_link = "https://www.c-and-a.com/" + category_link
        category_links.append(category_link)
    logger.info(f"Found {len(category_links)} category links")
    return category_links

def extract_item_links(category_link):
    response = requests.get(category_link)
    if response.status_code == 200:
        logger.info(f"Got a response from: {category_link}")
    else:
        logger.error(f"failed to get a response from {category_link}")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    items = bs.find_all("div", {"role": "listitem"})
    logger.info("extracting item links...")
    item_links = []
    for item in items:
        item_link = item.find("a").get("href")
        item_link = "https://www.c-and-a.com/" + item_link
        item_links.append(item_link)
    logger.info(f"Found {len(item_links)} item links")
    return item_links

def extract_item_info(item_link, shop_name):
    response = requests.get(item_link)
    if response.status_code == 200:
        logger.info(f"Got a response from: {item_link}")
    else:
        logger.error(f"failed to get a response from {item_link}")
        return
    bs = BeautifulSoup(response.text, "html.parser")
    name = bs.find("h1", {"data-qa": "ProductName"})
    if name is None:
        name = "None"
    else:
        name = name.text
    price = bs.find("div", {"data-qa": "Headline"})
    if price is None:
        price = "None"
    else:
        price = price.text
    image_element = bs.find("div", {"data-qa": "ProductImage"})
    image_links = image_element.find_all("img")
    logger.info("extracting item images...")
    images = []
    for image_link in image_links:
        link = image_link.get("src")
        images.append(link)
    logger.info(f"item name: {name}, item price: {price}, item images: {images}")
    return {"item_name": name, "item_price": price, "item_images": images, "item_link": item_link, "shop_name": shop_name}


def run_parser():
    while True:
        last_time = get_last_extraction_time()
        if last_time is None or datetime.now() - last_time > timedelta(days=1):
            men_page = "https://www.c-and-a.com/eu/ro/shop/barbati"
            women_page = "https://www.c-and-a.com/eu/ro/shop/femei"
            kids_page = "https://www.c-and-a.com/eu/ro/shop/copii"
            category_links_men = extract_category_links(men_page)
            category_links_women = extract_category_links(women_page)
            category_links_kids = extract_category_links(kids_page)
            for category_link in category_links_men:
                item_links = extract_item_links(category_link)
                for item_link in item_links:
                    item_info = extract_item_info(item_link, "C&A")
                    try:
                        add_item_info(item_info)
                    except IntegrityError:
                        logger.error("item already im base!")
                        session.rollback()

            for category_link in category_links_women:
                item_links = extract_item_links(category_link)
                for item_link in item_links:
                    item_info = extract_item_info(item_link, "C&A")
                    try:
                        add_item_info(item_info)
                    except IntegrityError:
                        logger.error("item already im base!")
                        session.rollback()

            for category_link in category_links_kids:
                item_links = extract_item_links(category_link)
                for item_link in item_links:
                    item_info = extract_item_info(item_link, "C&A")
                    try:
                        add_item_info(item_info)
                    except IntegrityError:
                        logger.error("item already im base!")
                        session.rollback()


        update_last_extraction_time()
        time.sleep(PARSING_INTERVAL)



