import cloudinary
import cloudinary.uploader
import cloudinary.api


def upload_cloudinary(full_path):
    cloudinary.config(
        cloud_name="doomw8apy",
        api_key="455829723853644",
        api_secret="bAw3EPy5A85ZE693hjAHGj8I7kM"
    )

    # res = cloudinary.uploader.upload_image(file=full_path, options={'use_filename': True, 'unique_filename': True})
    res = cloudinary.uploader.upload_image(file=full_path)
    return res.url
