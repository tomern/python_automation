import cloudinary
import cloudinary.uploader
import cloudinary.api
import json


def upload_cloudinary(full_path):
    with open('C:/Users/tomern23/PycharmProjects/PytestProject/configuration_folder/config.json') as json_data:
        data = json.load(json_data)

    cloudinary.config(
        cloud_name=data["cloudinary"]["cloud_name"],
        api_key=data["cloudinary"]["api_key"],
        api_secret=data["cloudinary"]["api_secret"]
    )

    res = cloudinary.uploader.upload_image(full_path, use_filename=True, unique_filename=False)
    return res.url
