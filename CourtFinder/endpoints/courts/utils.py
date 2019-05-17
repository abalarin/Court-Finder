import os
import datetime

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


def get_images(id):
    # Create a path with the ID & the root of our App
    target = os.path.join(Config.APP_ROOT, 'static/images/courts/' + id)

    # If path exsists we have images! Return them all
    if os.path.isdir(target):
        return os.listdir(target)

    return False

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
