from models.alert import Alert

alert = Alert("e5f7406361974b6486a27d50c7fb7172", 1000)
alert.save_to_mongo()

# from models.item import Item
#
#
# URL = "https://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-cellular-64gb/p3834601"
# TAG_NAME = "span"
# QUERY = {"class":"price__current"}
#
# ipad = Item(URL, TAG_NAME, QUERY)
# ipad.save_to_mongo()
#
# items_loaded = Item.all()
# print(items_loaded)
# print(items_loaded[0].load_price())
