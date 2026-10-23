import os
import shutil
from PIL import Image

# Caminhos das pastas
src_folder = os.path.join('assets', 'icons')
dst_folder = os.path.join('assets', 'dark-icons')

if os.path.exists(dst_folder):
    shutil.rmtree(dst_folder)
shutil.copytree(src_folder, dst_folder)
print("Pasta 'dark-icons' criada com sucesso. Convertendo imagens...")

for filename in os.listdir(dst_folder):
    if filename.endswith('.png'):
        filepath = os.path.join(dst_folder, filename)
        
        try:
            img = Image.open(filepath).convert("RGBA")
            pixels = img.load()
            width, height = img.size

            bg_color = pixels[0, 0]
            tolerance = 45 

            for x in range(width):
                for y in range(height):
                    r, g, b, a = pixels[x, y]
        
                    if (abs(r - bg_color[0]) < tolerance and
                        abs(g - bg_color[1]) < tolerance and
                        abs(b - bg_color[2]) < tolerance):
                        pixels[x, y] = (0, 0, 0, 255)

            img.convert("RGB").save(filepath)
            print(f"{filename} -> Fundo preto aplicado")
        except Exception as e:
            print(f"Erro ao processar {filename}: {e}")

print("\nTodas as imagens de 'assets/dark-icons' estão com fundo preto.")