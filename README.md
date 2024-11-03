# Conjunto de Dados de Anomalias Climáticas

Este conjunto de dados foi criado com base nos dados de anomalias climáticas dos hemisférios Norte e Sul. Os dados foram coletados e processados pela NASA e estão disponíveis no site [NASA GISTEMP](https://data.giss.nasa.gov/gistemp/).

## Descrição do Conjunto de Dados

O conjunto de dados fornece registros mensais das anomalias climáticas para os hemisférios Norte e Sul. Essas anomalias representam desvios das temperaturas médias globais durante o período de 1951 a 1980, que é utilizado como linha de base. O conjunto de dados está estruturado para facilitar a análise de séries temporais e previsões.

### Fonte dos Dados

Os dados utilizados neste projeto vêm do Instituto Goddard de Estudos Espaciais (GISS) da NASA e fazem parte do conjunto de dados GISTEMP v4. Os dados originais podem ser acessados em:

- [NASA GISTEMP: Série Temporal de Temperaturas Globais](https://data.giss.nasa.gov/gistemp/)

### Variáveis

- **Year**: O ano em que os dados foram registrados.
- **Month**: O mês em que os dados foram registrados.
- **NorthHemisphere**: Anomalias de temperatura (em graus Celsius) para o Hemisfério Norte.
- **SouthHemisphere**: Anomalias de temperatura (em graus Celsius) para o Hemisfério Sul.

### Previsões Usando Prophet

Utilizamos o modelo **Prophet** para realizar previsões de anomalias climáticas, com foco nas anomalias do Hemisfério Sul, usando as anomalias do Hemisfério Norte como variável exógena.

#### Exemplo de Previsão para 300 Steps

A imagem a seguir ilustra um exemplo de previsão de 300 meses à frente usando o Prophet:

![Exemplo de Previsão](path_para_imagem)

### Resultados do Treinamento de 300 Steps

Os resultados para a previsão de 300 meses à frente foram:

- **RMSE**: 0.1425
- **MAE**: 0.1099
- **MAPE**: 28.00%

Esses valores indicam a precisão do modelo na previsão das anomalias de temperatura do Hemisfério Sul com base no Hemisfério Norte como variável exógena.

### Como Utilizar o Conjunto de Dados

1. Clone este repositório:
   ```bash
   git clone https://github.com/brunodenardo/SerieTemporal.git
