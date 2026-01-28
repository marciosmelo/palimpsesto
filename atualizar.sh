#!/bin/bash

echo "--- Iniciando Processamento do Motor de Tramas ---"

# Roda o Merge
python3 merge_decks.py

# Verifica se o merge deu certo antes de continuar
if [ $? -eq 0 ]; then
    # Roda o Update das Imagens
    python3 update_json.py
    echo "--- Tudo pronto! Atualize o navegador. ---"
else
    echo "--- Erro no Merge. Processo interrompido. ---"
fi