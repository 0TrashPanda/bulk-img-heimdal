image_links = ["https://i.imgur.com/zeMo5QC.jpg","https://i.imgur.com/rj2PFuz.jpg","https://imgur.com/0H49Lha","https://imgur.com/68rbu8h","https://imgur.com/AY4PTD6","https://imgur.com/0XXmVhg"]

for image_link in image_links:
    new_image_link = image_link.replace("https://imgur.com/", "https://i.imgur.com/")
    if new_image_link != image_link:
        new_image_link += ".jpg"
    
    # Split the string by periods
    split_link = new_image_link.rsplit('.', maxsplit=1)
    thumbnail_link = split_link[0] + 'm.' + split_link[1]

        
    print(image_link)

"""

https://i.imgur.com/zeMo5QC.jpg
https://i.imgur.com/rj2PFuz.jpg
https://imgur.com/0H49Lha
https://imgur.com/68rbu8h
https://imgur.com/AY4PTD6
https://imgur.com/0XXmVhg

"""