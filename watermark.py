import os
from PIL import Image, ImageDraw, ImageFont

# Configurações
BASE_DIR = 'assets/images'
TEXTO = "© Marcio Melo | Motor de Tramas"
OPACIDADE = 80  # De 0 a 255 (80 é bem subtil)

def aplicar_assinatura():
    # Tenta carregar uma fonte do sistema, se não conseguir usa a padrão
    try:
        # No Linux/Fedora, as fontes costumam estar aqui
        font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 16)
    except:
        font = ImageFont.load_default()

    for pasta in ['deck1', 'deck2', 'deck3', 'deck4']:
        caminho_pasta = os.path.join(BASE_DIR, pasta)
        if not os.path.exists(caminho_pasta):
            continue

        print(f"Processando {pasta}...")
        
        for arquivo in os.listdir(caminho_pasta):
            if arquivo.endswith('.webp'):
                caminho_img = os.path.join(caminho_pasta, arquivo)
                
                # Abrir imagem e converter para RGBA para permitir transparência
                img = Image.open(caminho_img).convert("RGBA")
                txt = Image.new('RGBA', img.size, (255, 255, 255, 0))
                d = ImageDraw.Draw(txt)

                # Calcular posição (Canto inferior direito)
                largura_total, altura_total = img.size
                # Posição aproximada 10px de margem
                posicao = (largura_total - 220, altura_total - 30)

                # Desenha o texto com a opacidade definida
                d.text(posicao, TEXTO, fill=(255, 255, 255, OPACIDADE), font=font)

                # Combinar e salvar de volta como WebP
                combined = Image.alpha_composite(img, txt)
                combined.convert("RGB").save(caminho_img, "WEBP", quality=90)

    print("✅ Todas as 104 imagens foram assinadas.")

if __name__ == "__main__":
    aplicar_assinatura()