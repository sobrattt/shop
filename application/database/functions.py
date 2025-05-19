from application.database import session
from application.database.models import Image, Item
from application.logger import logger


def add_item_info(item_info):
    item_name, item_price, item_link, item_images, shop_name = (
        item_info["item_name"],
        item_info["item_price"],
        item_info["item_link"],
        item_info["item_images"],
        item_info["shop_name"]
    )
    item_1 = Item(
        item_name=item_name,
        item_price=item_price,
        item_link=item_link,
        shop_name=shop_name
    )
    session.add(item_1)
    session.commit()
    logger.info(f"item {item_1.id} saved in DB")
    for image in item_images:
        image_1 = Image(item_image=image, item_id=item_1.id)
        session.add(image_1)
        logger.info("image saved im DB")
    session.commit()
    logger.info(f"{item_1.id} successfully saved")
    return item_1