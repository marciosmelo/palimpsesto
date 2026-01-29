import json
import os

JSON_FILE = 'data/decks_master.json'
DECKS_MAP = {
    'deck_vozes_atuacao': 'deck1',
    'deck_cicatrizes_ideologicas': 'deck2',
    'deck_tecido_mundo': 'deck3',
    'deck_rupturas_percurso': 'deck4'
}

def update_images():
    if not os.path.exists(JSON_FILE):
        print("❌ Erro: Execute o merge_decks.py primeiro.")
        return

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key, folder in DECKS_MAP.items():
        if key in data and isinstance(data[key], list):
            for carta in data[key]:
                if isinstance(carta, dict):
                    # Padroniza o ID para minúsculo para bater com o nome do arquivo .webp
                    card_id = carta.get('id', '').lower()
                    if card_id:
                        caminho_img = f"assets/images/{folder}/{card_id}.webp"
                        carta['image'] = caminho_img
                        carta['id'] = card_id

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"🖼️ Caminhos de imagem atualizados em {JSON_FILE}")

if __name__ == "__main__":
    update_images()