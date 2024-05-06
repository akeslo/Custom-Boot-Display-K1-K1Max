from PIL import Image
import os

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return height, width

def convert_gif_to_images(gif_path, output_folder):
    with Image.open(gif_path) as gif:
        width, height = gif.size
        
        os.makedirs(output_folder, exist_ok=True)
        
        frame_num = 1
        while True:
            try:
                gif.seek(frame_num)
            except EOFError:
                break
            
            frame = gif.convert('RGB')
            
            if width > height:
                frame = frame.rotate(270, expand=True)
            
            frame = frame.resize((480, 800))
            
            frame_path = os.path.join(output_folder, f"frame_{frame_num:03d}.jpg")
            frame.save(frame_path, "JPEG")
            
            frame_height, frame_width = get_image_dimensions(frame_path)
            print(f"Frame {frame_num} Created - Dimensions - Height: {frame_height}, Width: {frame_width}")
            
            frame_num += 1

gif_path = "GifPathHere"
output_folder = "ImageOutputHere"
convert_gif_to_images(gif_path, output_folder)
