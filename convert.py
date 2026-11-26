import os
import shutil
from PIL import Image

src_folder = os.path.join("assets", "icons")
dst_folder = os.path.join("assets", "dark-icons")

target_files = [
    "eslint.png",
    "jsconfig.png",
    "nextjs.png",
    "postcss.png",
    "rspack.png",
    "tsconfig.png",
]

os.makedirs(dst_folder, exist_ok=True)

for filename in target_files:
    src_path = os.path.join(src_folder, filename)
    dst_path = os.path.join(dst_folder, filename)

    if not os.path.exists(src_path):
        print(f"Arquivo não encontrado: {src_path}")
        continue

    try:
        shutil.copy2(src_path, dst_path)
        img = Image.open(dst_path).convert("RGBA")
        pixels = img.load()
        width, height = img.size

        bg_color = pixels[0, 0]
        tolerance = 20 if filename == "nextjs.png" else 45

        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]

                is_background = (
                    abs(r - bg_color[0]) < tolerance
                    and abs(g - bg_color[1]) < tolerance
                    and abs(b - bg_color[2]) < tolerance
                )

                if is_background:
                    pixels[x, y] = (0, 0, 0, 255)
                elif filename == "nextjs.png":
                    pixels[x, y] = (255, 255, 255, 255)

        img.convert("RGB").save(dst_path)
        print(f"{filename} -> Fundo preto aplicado com sucesso")
    except Exception as e:
        print(f"Erro ao processar {filename}: {e}")

print("\nConversão concluída em 'assets/dark-icons'.")