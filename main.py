from PIL import Image

def resize_image_to_16x16(image_path, output_path):
    # Open the image
    with Image.open(image_path) as img:
        # Resize the image to 16x16 pixels
        resized_img = img.resize((16, 16), Image.ANTIALIAS)

        # Save the resized image
        resized_img.save(output_path)

    print(f"Image resized to 16x16 and saved as {output_path}")

# Example usage
resize_image_to_16x16("path_to_your_image.jpg", "output_image.jpg")
