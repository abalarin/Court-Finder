import os
import datetime
from flask import jsonify

from CourtFinder import client
from CourtFinder.models.courts import Court
from CourtFinder.config import Config


def upload_images(images, id):

    # Create a target path using listing ID
    target = os.path.join(Config.APP_ROOT, 'static/images/courts/' + str(id))

    # If target director exsist then this is just an update, no need to create new dir
    if not os.path.isdir(target):
        os.mkdir(target)

    # Loop through all images and upload
    for image in images:
        filename = image.filename
        destination = "/".join([target, filename])
        image.save(destination)

# Validate the unique ID of our new listing to prevent collisions
def id_validator(uid):
    # Query for any listing where id matches uid
    result = Court.query.filter_by(uid=str(uid)).first()

    # If the ID exsists try again with new ID
    if result is not None:
        id_validator(uuid.uuid4())

    return uid


def date_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def list_courts():
    return client.list_objects(Bucket='courtfinder', Prefix='courts/', Delimiter='/')


def get_URL(file_name):
    return client.generate_presigned_post(Bucket='courtfinder', Key=file_name)


def get_images(court):
    try:
        prefix = 'courts/' + str(court) + '/'
        result = client.list_objects(Bucket='courtfinder', Prefix=prefix, Delimiter='/')

        image_urls = []
        skipthedir = 0  # becuase the directory itself is also retrived we want to skip it
        for object in result.get('Contents'):
            if skipthedir > 0:
                url = get_URL(object.get('Key'))
                image_urls.append(url.get('url') + '/' + url.get('fields')['key'])
            else:
                skipthedir += 1

        return image_urls

    except Exception as e:
        print(e)
        return jsonify({"error": "There was a problem with the data you provided."})
