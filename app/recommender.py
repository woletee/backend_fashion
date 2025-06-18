# You can replace these links with real product images and shops
item_catalog = {
    "t-shirt": {
        "suggest_link": "https://www2.hm.com/en_us/productpage.1213796004.html",
        "image_url": "https://lp2.hm.com/hmgoepprod?set=source[/9b/c2/9bc28bb94a4090cc6f390276d85b3d5b9b7099d2.jpg],type[LOOKBOOK],res[z],hmver[2]"
    },
    "jeans": {
        "suggest_link": "https://www2.hm.com/en_us/productpage.1024257001.html",
        "image_url": "https://lp2.hm.com/hmgoepprod?set=source[/38/87/3887f697bba184c91a219bbd83b0c7ed073b4ab5.jpg],type[LOOKBOOK],res[z],hmver[2]"
    },
    "jacket": {
        "suggest_link": "https://www2.hm.com/en_us/productpage.1209929002.html",
        "image_url": "https://lp2.hm.com/hmgoepprod?set=source[/71/ae/71ae7f4d8a1b237e0f167b2abfbc8bb17202ef7f.jpg],type[LOOKBOOK],res[z],hmver[1]"
    },
    "sneakers": {
        "suggest_link": "https://www.nike.com/t/air-force-1-07-mens-shoes-KyTwDP",
        "image_url": "https://static.nike.com/a/images/t_default/0c3bc655-13d5-48df-9a44-d95a13e5a51d/air-force-1-07-mens-shoes-KyTwDP.png"
    },
    "shirt": {
        "suggest_link": "https://www2.hm.com/en_us/productpage.1217445002.html",
        "image_url": "https://lp2.hm.com/hmgoepprod?set=source[/c8/e6/c8e650b05b7b2b2aab7f6e5f40f8e3a47e6dcba5.jpg],type[LOOKBOOK],res[z],hmver[1]"
    },
    "skirt": {
        "suggest_link": "https://www2.hm.com/en_us/productpage.1214733001.html",
        "image_url": "https://lp2.hm.com/hmgoepprod?set=source[/44/d3/44d3e8a80ed21f4efb3e9cfb8a4b6452d84fe5c3.jpg],type[LOOKBOOK],res[z],hmver[1]"
    }
}


def get_recommendations_with_images(detected_items: list):
    detected_set = set(detected_items)
    missing = [item for item in item_catalog if item not in detected_set]

    return [
        {
            "missing_item": item,
            "suggest_link": item_catalog[item]["suggest_link"],
            "image_url": item_catalog[item]["image_url"]
        }
        for item in missing
    ]
