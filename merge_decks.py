import json
import os

def build_palimpsesto():
    data_dir = './data'
    master_data = {}

    # Lista todos os JSONs, ignorando o arquivo mestre para não duplicar
    arquivos = [f for f in os.listdir(data_dir) if f.endswith('.json') and f != 'decks_master.json']

    for nome_arquivo in arquivos:
        caminho = os.path.join(data_dir, nome_arquivo)
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = json.load(f)
            master_data.update(conteudo)

    # Salva o resultado final
    output_path = os.path.join(data_dir, 'decks_master.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(master_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Sucesso! {len(arquivos)} decks unidos em: {output_path}")

if __name__ == "__main__":
    build_palimpsesto()