from PIL import Image

# Function to convert XCF to TIFF

def convert_xcf_to_tiff(xcf_path, tiff_path):
    with Image.open(xcf_path) as img:
        img.save(tiff_path, "TIFF")

# Function to convert TIFF to WebP

def convert_tiff_to_webp(tiff_path, webp_path):
    with Image.open(tiff_path) as img:
        img.save(webp_path, "WEBP")

# Example usage
# convert_xcf_to_tiff('path/to/image.xcf', 'path/to/image.tiff')
# convert_tiff_to_webp('path/to/image.tiff', 'path/to/image.webp')
