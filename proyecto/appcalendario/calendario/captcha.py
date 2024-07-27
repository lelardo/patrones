# captcha.py
import io
from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile
from django.conf import settings
import random
import string


def generate_captcha_image():
    # Genera un texto aleatorio para el CAPTCHA
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    # Crear una imagen en blanco
    width, height = 150, 50
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # Cargar una fuente
    font = ImageFont.load_default()

    # Dibujar el texto en la imagen
    text_width, text_height = draw.textsize(captcha_text, font=font)
    draw.text(((width - text_width) / 2, (height - text_height) / 2), captcha_text, fill='black', font=font)

    # Agregar ruido (opcional)
    for _ in range(100):
        draw.point((random.randint(0, width), random.randint(0, height)), fill='gray')

    # Guardar la imagen en un buffer
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    image_content = buffer.getvalue()

    # Guardar la imagen en el sistema de archivos
    image_file_name = 'captcha.png'
    image_file = ContentFile(image_content, image_file_name)
    image_path = f'{settings.MEDIA_ROOT}/{image_file_name}'

    with open(image_path, 'wb') as f:
        f.write(image_content)

    image_url = f'{settings.MEDIA_URL}{image_file_name}'

    return image_url, captcha_text
