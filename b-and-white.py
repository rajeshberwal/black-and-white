from PIL import Image

def b_and_w(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)

    bw_image = color_image.convert('L')

    bw_image.save(output_image_path)

b_and_w('codes.jpg', 'bw_codes.jpg')