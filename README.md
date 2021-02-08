# Planilha_resistencia_aterramento

Cálculo dos parâmetros de malhas de aterramento conforme o exemplo do livro

- MAMEDE FILHO, J. Instalações Elétricas Industriais – LTC – 9a ed., 2017

- ABNT NBR 7117-1

## Observações importantes

** Qualquer análise de resistência de aterramento deve ser feita por profissional qualificado, habilitado e capacitado. Sob pena das aplicações das sanções previstas na legislação. **

## Arquivos

Aterramento_malha - Utiliza o método mostrado no livro do Mamede

Cálculo das resistências - Utiliza o método da ABNT NBR 7117-1


### Resistividade

Tabela de cálculo da resistividade do solo a partir das medições de sondagem geolétrica.

Valores com desvio padrão maior que 50% são descartados do cálculo.

### Modelo Geolétrico

- Modelagem das camadas do solo, resistividade e altura da primeira camada.

- Rô1 é encontrado projetando a curva da resistividade até o eixo das ordenadas .(eixo Y).

- Rô2 é encontrado projetando a curva da resistividade até o infinito, cujo valor coincide com o eixo das ordenadas (eixo Y).

- O valor de H1 é encontrado multiplicando o fator M0 por Rô1 e projetando o seu valor no gráfico.

### Memória

- Modelagem da resistência de aterramento conforme o exemplo do livro mencionado anteriormente.

### Auxiliar

- Tabela auxiliar de cálculo.

### Aterranto_hastes.py

- Cálculo numérico da resistência de aterramento de um conjunto de haste configurável.

- O script pode ser facilmente executado em compiladores de python online.