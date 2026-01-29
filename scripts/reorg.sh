#!/bin/bash

# 1. Criar estrutura de segurança
mkdir -p assets/images/pool_temporario
mkdir -p assets/images/deck{1,2,3,4}

echo "--- Iniciando redistribuição das 104 lâminas ---"

# 2. Mover tudo para um "pool" neutro para evitar colisões de nomes
mv assets/images/deck1/*.webp assets/images/pool_temporario/ 2>/dev/null
mv assets/images/deck2/*.webp assets/images/pool_temporario/ 2>/dev/null
mv assets/images/deck3/*.webp assets/images/pool_temporario/ 2>/dev/null
mv assets/images/deck4/*.webp assets/images/pool_temporario/ 2>/dev/null

# 3. DISTRIBUIÇÃO: DECK 1 - VOZES (Orgânico/Humanoides/Faces)
# Priorizando IDs que originalmente sugeriam formas vivas ou de atuação
mv assets/images/pool_temporario/v01.webp assets/images/deck1/v01.webp
mv assets/images/pool_temporario/v02.webp assets/images/deck1/v02.webp
mv assets/images/pool_temporario/v03.webp assets/images/deck1/v03.webp
mv assets/images/pool_temporario/v04.webp assets/images/deck1/v04.webp
mv assets/images/pool_temporario/v06.webp assets/images/deck1/v05.webp
mv assets/images/pool_temporario/v07.webp assets/images/deck1/v06.webp
mv assets/images/pool_temporario/v08.webp assets/images/deck1/v07.webp
mv assets/images/pool_temporario/v09.webp assets/images/deck1/v08.webp
mv assets/images/pool_temporario/v12.webp assets/images/deck1/v09.webp
mv assets/images/pool_temporario/v15.webp assets/images/deck1/v10.webp
mv assets/images/pool_temporario/v17.webp assets/images/deck1/v11.webp
mv assets/images/pool_temporario/v21.webp assets/images/deck1/v12.webp
mv assets/images/pool_temporario/v22.webp assets/images/deck1/v13.webp
mv assets/images/pool_temporario/v24.webp assets/images/deck1/v14.webp
mv assets/images/pool_temporario/t03.webp assets/images/deck1/v15.webp
mv assets/images/pool_temporario/t06.webp assets/images/deck1/v16.webp
mv assets/images/pool_temporario/t07.webp assets/images/deck1/v17.webp
mv assets/images/pool_temporario/t24.webp assets/images/deck1/v18.webp
mv assets/images/pool_temporario/t25.webp assets/images/deck1/v19.webp
mv assets/images/pool_temporario/g01.webp assets/images/deck1/v20.webp
mv assets/images/pool_temporario/g06.webp assets/images/deck1/v21.webp
mv assets/images/pool_temporario/g11.webp assets/images/deck1/v22.webp
mv assets/images/pool_temporario/r01.webp assets/images/deck1/v23.webp
mv assets/images/pool_temporario/r09.webp assets/images/deck1/v24.webp
mv assets/images/pool_temporario/r10.webp assets/images/deck1/v25.webp
mv assets/images/pool_temporario/r22.webp assets/images/deck1/v26.webp

# 4. DISTRIBUIÇÃO: DECK 3 - TECIDO DO MUNDO (Estruturas/Máquinas/Urbano)
# Focando em linhas retas, arquitetura e lógica de sistema
mv assets/images/pool_temporario/t01.webp assets/images/deck3/t01.webp
mv assets/images/pool_temporario/t02.webp assets/images/deck3/t02.webp
mv assets/images/pool_temporario/t04.webp assets/images/deck3/t03.webp
mv assets/images/pool_temporario/t05.webp assets/images/deck3/t04.webp
mv assets/images/pool_temporario/t08.webp assets/images/deck3/t05.webp
mv assets/images/pool_temporario/t09.webp assets/images/deck3/t06.webp
mv assets/images/pool_temporario/t10.webp assets/images/deck3/t07.webp
mv assets/images/pool_temporario/t11.webp assets/images/deck3/t08.webp
mv assets/images/pool_temporario/t12.webp assets/images/deck3/t09.webp
mv assets/images/pool_temporario/t13.webp assets/images/deck3/t10.webp
mv assets/images/pool_temporario/t14.webp assets/images/deck3/t11.webp
mv assets/images/pool_temporario/t16.webp assets/images/deck3/t12.webp
mv assets/images/pool_temporario/t17.webp assets/images/deck3/t13.webp
mv assets/images/pool_temporario/t19.webp assets/images/deck3/t14.webp
mv assets/images/pool_temporario/t20.webp assets/images/deck3/t15.webp
mv assets/images/pool_temporario/t23.webp assets/images/deck3/t16.webp
mv assets/images/pool_temporario/v05.webp assets/images/deck3/t17.webp
mv assets/images/pool_temporario/v11.webp assets/images/deck3/t18.webp
mv assets/images/pool_temporario/v13.webp assets/images/deck3/t19.webp
mv assets/images/pool_temporario/v18.webp assets/images/deck3/t20.webp
mv assets/images/pool_temporario/v25.webp assets/images/deck3/t21.webp
mv assets/images/pool_temporario/g04.webp assets/images/deck3/t22.webp
mv assets/images/pool_temporario/g19.webp assets/images/deck3/t23.webp
mv assets/images/pool_temporario/r03.webp assets/images/deck3/t24.webp
mv assets/images/pool_temporario/r07.webp assets/images/deck3/t25.webp
mv assets/images/pool_temporario/r16.webp assets/images/deck3/t26.webp

# 5. DISTRIBUIÇÃO: DECK 4 - RUPTURAS (Caos/Manchas/Abstrato)
# Priorizando a "sujeira" do nanquim e explosões visuais
mv assets/images/pool_temporario/r02.webp assets/images/deck4/r01.webp
mv assets/images/pool_temporario/r04.webp assets/images/deck4/r02.webp
mv assets/images/pool_temporario/r05.webp assets/images/deck4/r03.webp
mv assets/images/pool_temporario/r06.webp assets/images/deck4/r04.webp
mv assets/images/pool_temporario/r08.webp assets/images/deck4/r05.webp
mv assets/images/pool_temporario/r11.webp assets/images/deck4/r06.webp
mv assets/images/pool_temporario/r12.webp assets/images/deck4/r07.webp
mv assets/images/pool_temporario/r13.webp assets/images/deck4/r08.webp
mv assets/images/pool_temporario/r15.webp assets/images/deck4/r09.webp
mv assets/images/pool_temporario/r18.webp assets/images/deck4/r10.webp
mv assets/images/pool_temporario/r19.webp assets/images/deck4/r11.webp
mv assets/images/pool_temporario/r20.webp assets/images/deck4/r12.webp
mv assets/images/pool_temporario/r21.webp assets/images/deck4/r13.webp
mv assets/images/pool_temporario/r23.webp assets/images/deck4/r14.webp
mv assets/images/pool_temporario/r24.webp assets/images/deck4/r15.webp
mv assets/images/pool_temporario/r25.webp assets/images/deck4/r16.webp
mv assets/images/pool_temporario/v14.webp assets/images/deck4/r17.webp
mv assets/images/pool_temporario/v16.webp assets/images/deck4/r18.webp
mv assets/images/pool_temporario/v26.webp assets/images/deck4/r19.webp
mv assets/images/pool_temporario/t21.webp assets/images/deck4/r20.webp
mv assets/images/pool_temporario/t22.webp assets/images/deck4/r21.webp
mv assets/images/pool_temporario/g07.webp assets/images/deck4/r22.webp
mv assets/images/pool_temporario/g14.webp assets/images/deck4/r23.webp
mv assets/images/pool_temporario/g24.webp assets/images/deck4/r24.webp
mv assets/images/pool_temporario/r26.webp assets/images/deck4/r25.webp
mv assets/images/pool_temporario/t15.webp assets/images/deck4/r26.webp

# 6. DISTRIBUIÇÃO: DECK 2 - CICATRIZES (Peso/Simbólico/Ideológico)
# O que restou preenche o deck de conceitos e cicatrizes
mv assets/images/pool_temporario/*.webp assets/images/deck2/ 2>/dev/null
# Renomear os restantes para seguir o padrão g01-g26
cd assets/images/deck2/
count=1
for f in *.webp; do
    printf -v newname "g%02d.webp" $count
    mv "$f" "$newname"
    let count++
done
cd ../../../

# 7. Limpeza
rm -rf assets/images/pool_temporario

echo "--- Reorganização concluída com sucesso! ---"
echo "Agora execute: ./atualizar.sh para atualizar os caminhos no JSON."