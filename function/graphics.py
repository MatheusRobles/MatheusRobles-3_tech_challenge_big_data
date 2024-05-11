import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot_bar(df, x, dict_map={}, title=None, top_n=None):
    # Calcula as contagens e porcentagens
    counts = df[x].value_counts(normalize=True) * 100

    # Seleciona as top_n categorias mais comuns, se especificado
    if top_n is not None:
        counts = counts.head(top_n)

    # Aplica o mapeamento, se fornecido
    if dict_map:
        counts.index = counts.index.map(dict_map)

    # Cria o DataFrame para plotagem
    data = pd.DataFrame({'x': counts.index, 'percent': counts.values})

    # Plotagem com Plotly
    fig = px.bar(data, x='x', y='percent', text='percent', color='x', labels={'x': x, 'percent': 'Porcentagem'})
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(title=title if title else f'Porcentagem de {x}', xaxis_title=None, yaxis_title='Porcentagem')
    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)



def plot_bar_sintomas(df, sintomas, title=None):
    # Criar listas vazias para armazenar os resultados
    sintoma_list = []
    percent_sim_list = []

    # Para cada sintoma
    for sintoma in sintomas:
        # Contar o número de casos 'Sim' para o sintoma atual
        num_sim = (df[sintoma] == 'Sim').sum()

        # Calcular a porcentagem de casos 'Sim' para o sintoma atual
        percent_sim = (num_sim / len(df)) * 100

        # Adicionar os resultados às listas
        sintoma_list.append(sintoma.replace('SE_TEVE_', ''))
        percent_sim_list.append(percent_sim)

    # Criar um DataFrame com os resultados
    data = pd.DataFrame({'Sintoma': sintoma_list, 'Porcentagem': percent_sim_list})

    # Plotagem com Plotly
    fig = px.bar(data, x='Sintoma', y='Porcentagem', text='Porcentagem', labels={'Sintoma': 'Sintoma', 'Porcentagem': 'Porcentagem'})
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(title=title if title else 'Porcentagem de casos positivos para cada sintoma')
    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)


import pandas as pd
import plotly.express as px

def plot_mult_bar(df, column, sintomas, title=None):
    data = {'Sintoma': [], column: [], 'Porcentagem': []}

    for sintoma in sintomas:
        for category_value in df[column].unique():
            total = len(df[df[column] == category_value])
            total_sim = len(df[(df[sintoma] == 'Sim') & (df[column] == category_value)])
            percent_sim = (total_sim / total) * 100 if total > 0 else 0
            data['Sintoma'].append(sintoma.replace('SE_TEVE_', ''))
            data[column].append(category_value)
            data['Porcentagem'].append(percent_sim)

    df_plot = pd.DataFrame(data)

    fig = px.bar(df_plot, x='Sintoma', y='Porcentagem', color=column, barmode='group',
                 text='Porcentagem', labels={'Sintoma': 'Sintoma', 'Porcentagem': 'Porcentagem'},
                 title=title if title else f'Porcentagem de casos positivos para cada sintoma separados por {column}')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)


def plot_testados(df, title=None):
    # Mapeamento dos valores da coluna "x" para 'Testado' e 'Não Testado'
    mapping = {
        'Não aplicável': 'Não Testado',
        'Negativo': 'Testado',
        'Positivo': 'Testado',
        'Ainda não recebeu o resultado': 'Testado',
        'Inconclusivo': 'Testado'
    }

    # Criando uma nova coluna com os valores mapeados
    df['RESULTADO_MAPEADO'] = df['QUAL_RESULTADO'].map(mapping)
    # Calcula as contagens e porcentagens
    counts = df['RESULTADO_MAPEADO'].value_counts(normalize=True) * 100

    # Cria o DataFrame para plotagem
    data = pd.DataFrame({'x': counts.index, 'percent': counts.values})

    # Plotagem com Plotly
    fig = px.bar(data, x='x', y='percent', text='percent', color='x', 
                 labels={'x': 'Resultado do Teste', 'percent': 'Porcentagem (%)'},
                 title=title if title else f'Porcentagem de Resultados do Teste',
                 barmode='group')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)

def plot_qual_resultado_regiao_percentual(df, title=None):
    # Filtrando o DataFrame para excluir a categoria "Não aplicável"
    df_filtered = df[df['QUAL_RESULTADO'] != 'Não aplicável']

    # Contagem total de casos por região
    df_total_regiao = df_filtered.groupby('REGIAO').size().reset_index(name='total_regiao')

    # Contagem dos casos por resultado do teste e região
    df_counts = df_filtered.groupby(['QUAL_RESULTADO', 'REGIAO']).size().reset_index(name='count')

    # Mesclando as contagens com a contagem total por região para calcular percentuais
    df_counts = pd.merge(df_counts, df_total_regiao, on='REGIAO')

    # Calculando percentuais
    df_counts['percent'] = (df_counts['count'] / df_counts['total_regiao']) * 100

    # Plot do gráfico de barras
    fig = px.bar(df_counts, x='QUAL_RESULTADO', y='percent', color='REGIAO', barmode='group',
                 labels={'QUAL_RESULTADO': 'Resultado do Teste', 'percent': 'Porcentagem (%)'},
                 title=title if title else 'Porcentagem de Casos por Resultado do Teste e Região')

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)


def plot_heatmap(df_cluster):
    # Calcular as médias das características para cada cluster
    cluster_means = df_cluster.groupby('Cluster').mean().round(2)

    # Transpor os dados para que as características sejam as linhas e os clusters sejam as colunas
    cluster_means_transposed = cluster_means.T

    # Criar o heatmap interativo com o Plotly
    heatmap_data = go.Heatmap(z=cluster_means_transposed.values,
                              x=cluster_means_transposed.columns,
                              y=cluster_means_transposed.index,
                              colorscale='Viridis')

    layout = go.Layout(title='Correlação das características com os clusters',
                       xaxis=dict(title='Cluster'),
                       yaxis=dict(title='Característica'),
                       width=1000,  # Ajuste a largura conforme necessário
                       height=1400)  # Ajuste a altura conforme necessário)

    fig = go.Figure(data=[heatmap_data], layout=layout)
    # Exibir o heatmap
    st.plotly_chart(fig)