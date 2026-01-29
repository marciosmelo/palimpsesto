import os
from PIL import Image, ImageDraw, ImageFont

# Configurações
BASE_DIR = 'assets/images'
TEXTO = "© Marcio Melo | Motor de Tramas"
OPACIDADE_TEXTO = 180  # De 0 a 255 (Aumentado para ser visível)
TAMANHO_FONTE = 22     # Aumentado para dar leitura

def aplicar_assinatura():
    # Tenta carregar uma fonte, se não conseguir usa a padrão
    font = None
    try:
        # Tenta fontes comuns de sistema (ajuste o caminho se necessário no Windows/Mac)
        font_paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
            "C:\\Windows\\Fonts\\arialbd.ttf",
            "/Library/Fonts/Arial Bold.ttf"
        ]
        for path in font_paths:
            if os.path.exists(path):
                font = ImageFont.truetype(path, TAMANHO_FONTE)
                break
    except:
        pass
    
    if font is None:
        font = ImageFont.load_default()
        print("⚠️ Usando fonte padrão (pode ficar pequena).")

    for pasta in ['deck1', 'deck2', 'deck3', 'deck4']:
        caminho_pasta = os.path.join(BASE_DIR, pasta)
        if not os.path.exists(caminho_pasta):
            continue

        print(f"Assinando artes em {pasta}...")
        
        for arquivo in os.listdir(caminho_pasta):
            if arquivo.endswith('.webp'):
                caminho_img = os.path.join(caminho_pasta, arquivo)
                
                # Abrir imagem e converter para RGBA
                img = Image.open(caminho_img).convert("RGBA")
                txt_layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
                d = ImageDraw.Draw(txt_layer)

                # Calcular posição (Canto inferior direito com margem)
                # Usando bbox para medir o texto corretamente
                bbox = d.textbbox((0, 0), TEXTO, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                
                x = img.size[0] - text_width - 20
                y = img.size[1] - text_height - 25

                # 1. DESENHAR A SOMBRA (Preta, para dar contraste no branco)
                for adj in range(-1, 2):
                    for bdy in range(-1, 2):
                        d.text((x+adj, y+bdy), TEXTO, fill=(0, 0, 0, 150), font=font)

                # 2. DESENHAR O TEXTO PRINCIPAL (Branco)
                d.text((x, y), TEXTO, fill=(255, 255, 255, OPACIDADE_TEXTO), font=font)

                # Combinar e salvar
                combined = Image.alpha_composite(img, txt_layer)
                combined.convert("RGB").save(caminho_img, "WEBP", quality=95)

    print("\n✅ Processo concluído! Agora a assinatura deve estar visível em qualquer fundo.")

if __name__ == "__main__":
    aplicar_assinatura()