import json
import os

def build_palimpsesto():
    data_dir = './data'
    master_data = {}
    output_filename = 'decks_master.json'
    backup_filename = 'decks_master_backup.json'

    # Caminhos completos para os arquivos
    output_path = os.path.join(data_dir, output_filename)
    backup_path = os.path.join(data_dir, backup_filename)

    # Lista todos os JSONs, ignorando o arquivo mestre e o de backup
    arquivos = [f for f in os.listdir(data_dir) if f.endswith('.json') and f not in [output_filename, backup_filename]]

    for nome_arquivo in arquivos:
        caminho = os.path.join(data_dir, nome_arquivo)
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = json.load(f)
            master_data.update(conteudo)

    # --- Lógica de Backup ---
    # Verifica se o arquivo mestre já existe
    if os.path.exists(output_path):
        # Se um backup antigo já existe, ele será sobrescrito pela renomeação.
        # Para evitar erros no Windows, removemos o backup antigo explicitamente.
        if os.path.exists(backup_path):
            os.remove(backup_path)
            print(f"🗑️ Backup antigo removido: {backup_path}")
            
        # Renomeia o arquivo mestre atual para o nome de backup
        os.rename(output_path, backup_path)
        print(f"↪️ Backup do arquivo mestre anterior salvo como: {backup_path}")


    # Salva o resultado final
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(master_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Sucesso! {len(arquivos)} decks unidos em: {output_path}")

if __name__ == "__main__":
    build_palimpsesto()