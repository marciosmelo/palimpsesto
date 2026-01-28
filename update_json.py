import json
import os

# Configurações de caminhos
JSON_FILE = 'data/decks_master.json'
BASE_IMAGE_PATH = 'assets/images'
DECKS = {
    'deck_vozes_atuacao': 'v',
    'deck_cicatrizes_ideologicas': 'g',
    'deck_tecido_mundo': 't',
    'deck_rupturas_percurso': 'r'
}

def atualizar_decks():
    # Cria a pasta data se não existir
    os.makedirs(os.path.dirname(JSON_FILE), exist_ok=True)

    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                data = {}
    else:
        data = {}

    for deck_key, prefix in DECKS.items():
        if deck_key not in data:
            data[deck_key] = []

        # Mapeamento de pastas físicas (deck1, deck2...)
        folder_map = {
            'v': 'deck1', 'g': 'deck2', 't': 'deck3', 'r': 'deck4'
        }
        deck_folder = folder_map[prefix]

        for i in range(1, 27):
            card_id = f"{prefix}{i:02d}"
            image_filename = f"{card_id}.webp"
            relative_path = f"assets/images/{deck_folder}/{image_filename}"
            
            # Procura a carta no JSON (ignora case para bater 'V01' com 'v01')
            card_entry = next((item for item in data[deck_key] if item.get('id').lower() == card_id.lower()), None)

            if card_entry:
                card_entry['image'] = relative_path
                # Padroniza o ID para minúsculo para consistência
                card_entry['id'] = card_id.lower()
            else:
                # Só cria se realmente não existir nada com esse ID
                data[deck_key].append({
                    "id": card_id.lower(),
                    "titulo": f"Arquétipo {card_id}",
                    "image": relative_path,
                    "arquetipo_vinculado": "Definir",
                    "descricao": "Texto pendente...",
                    "instrucao_narrativa": "Instrução pendente..."
                })

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"✅ JSON atualizado em {JSON_FILE}")

if __name__ == "__main__":
    atualizar_decks()