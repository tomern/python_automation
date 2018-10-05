import cloudinary
import cloudinary.uploader
import cloudinary.api


def upload_cloudinary(full_path, cfg):
    cloudinary.config(
        cloud_name=cfg.cloudinary['cloud_name'],
        api_key=cfg.cloudinary['api_key'],
        api_secret=cfg.cloudinary['api_secret']
    )

    res = cloudinary.uploader.upload_image(full_path, use_filename=True, unique_filename=False)
    return res.url
