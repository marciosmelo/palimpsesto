import json
import os

# Caminhos dos arquivos de origem e destino
FILES = {
    'deck_vozes_atuacao': 'data/deck01.json',
    'deck_cicatrizes_ideologicas': 'data/deck02.json',
    'deck_tecido_mundo': 'data/deck03.json',
    'deck_rupturas_percurso': 'data/deck04.json'
}
MASTER_FILE = 'data/decks_master.json'

def merge():
    master_data = {}
    
    for key, path in FILES.items():
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                conteudo = json.load(f)
                # Pega apenas a lista de cartas, ignorando a chave de embalagem
                if isinstance(conteudo, dict) and key in conteudo:
                    master_data[key] = conteudo[key]
                else:
                    master_data[key] = conteudo
            print(f"✅ {path} mesclado com sucesso.")
        else:
            print(f"⚠️ Aviso: {path} não encontrado.")
            master_data[key] = []

    # Garante que a pasta data existe
    os.makedirs(os.path.dirname(MASTER_FILE), exist_ok=True)

    with open(MASTER_FILE, 'w', encoding='utf-8') as f:
        json.dump(master_data, f, indent=4, ensure_ascii=False)
    print(f"\n✨ {MASTER_FILE} reconstruído com estrutura plana.")

if __name__ == "__main__":
    merge()