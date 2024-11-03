import pandas as pd

def preparaDataSet():
    # Caminhos dos arquivos carregados
    sh_data_path = 'Dataset/HemisferioSul.csv'
    nh_data_path = 'Dataset/HemisferioNorte.csv'

    # Carregar os arquivos, começando do segundo cabeçalho para limpar os dados
    sh_data_corrected = pd.read_csv(sh_data_path)
    nh_data_corrected = pd.read_csv(nh_data_path)

    # Drop das colunas indesejadas (J-D, D-N, DJF, MAM, JJA, SON)
    columns_to_drop = ['J-D', 'D-N', 'DJF', 'MAM', 'JJA', 'SON']
    sh_data_corrected = sh_data_corrected.drop(columns=columns_to_drop)
    nh_data_corrected = nh_data_corrected.drop(columns=columns_to_drop)

    # Aplicar o melt para transformar os meses em linhas
    melted_corrected_data_nh = pd.melt(
        nh_data_corrected, 
        id_vars=['Year'], 
        var_name='Month', 
        value_name='NorthHemisphere'
    )

    melted_corrected_data_sh = pd.melt(
        sh_data_corrected, 
        id_vars=['Year'], 
        var_name='Month', 
        value_name='SouthHemisphere'
    )

    # Mesclar os dois datasets com base na coluna 'Year' e 'Month'
    merged_data_corrected = pd.merge(
        melted_corrected_data_nh[['Year', 'Month', 'NorthHemisphere']],
        melted_corrected_data_sh[['Year', 'Month', 'SouthHemisphere']],
        on=['Year', 'Month']
    )

    # Remover linhas com valores em branco nas colunas 'NorthHemisphere' ou 'SouthHemisphere'
    merged_data_corrected = merged_data_corrected.dropna(subset=['NorthHemisphere', 'SouthHemisphere'])

    # Gerar o arquivo CSV a partir do dataset resultante
    merged_data_corrected.to_csv('Dataset/merged_hemispheres.csv', index=False)
    print("CSV gerado com sucesso!")

    # Exibir a tabela final
    print(merged_data_corrected)

preparaDataSet()

