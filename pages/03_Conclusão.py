import streamlit as st
import pandas as pd
from PIL import Image

# configura características da página
st.set_page_config(page_title='Cpnclusão', page_icon='https://th.bing.com/th?id=ODLS.b7e13985-946a-47c6-8d8e-a4d10d1e8063&w=32&h=32&qlt=90&pcl=fffffa&o=6&pid=1.2', initial_sidebar_state='expanded')

# seta header image da página
page03_header_image = Image.open('imgs\header_principal.jpg')
st.image(page03_header_image, caption='Image credit: Fusion Medical Animation at Unsplash')

st.title('Conclusão')
st.markdown('''         
                [A disseminação de desinformação e notícias falsas durante toda a pandemia contribuiu para o medo e a sobrecarga do sistema de saúde, além de minar a confiança na ciência](https://www.jornalopcao.com.br/reportagens/o-impacto-da-epidemia-das-fake-news-no-combate-a-covid-19-e-os-desafios-da-ciencia-329354/). Os sistemas de saúde, estados e prefeituras precisam estar atentos a crises como a da COVID-19, ressaltando a importância da ciência para orientar a operacionalização do enfrentamento dessas situações. 
                
                Algumas medidas precisam ser lembradas: 

                - **Triagem Eficiente em Hospitais**: É fundamental que os hospitais tenham triagem eficaz para separar os casos graves dos não graves.

                - **Investimento em Hospitais de Campanha**: A criação de hospitais de campanha pode ajudar a lidar com o aumento da demanda durante crises.

                - **Atenção a Outras Doenças**: Além da COVID-19, é essencial que as unidades de saúde continuem a tratar outras doenças para evitar negligência.

                - **Informações Baseadas em Evidências**: O acesso regular a informações embasadas e confiáveis é crucial para tomar decisões informadas.

            
                O vírus responsável pela pandemia de COVID-19 é altamente mutável, e já existem várias variantes em todo o mundo. Uma dessas variantes ou até mesmo um novo vírus pode ser responsável por um futuro surto global. A análise do PNAD 2020 revelou insights valiosos sobre o impacto da COVID-19 no Brasil, fornecendo uma base sólida para estratégias de intervenção mais direcionadas.

                Olhando para o futuro, esses resultados sugerem a necessidade contínua de abordagens interdisciplinares e adaptações metodológicas. A implementação de políticas públicas mais eficazes e equitativas requer uma compreensão mais profunda das nuances da disseminação do vírus.

                ## Ações Recomendadas:
                
                - **Campanhas de Conscientização**: Direcionar campanhas educativas para aumentar a adesão às medidas preventivas, especialmente entre a população economicamente ativa.
                - **Parcerias com Planos de Saúde / Hospitais Particulares**: Estabelecer parcerias estratégicas com provedores de planos de saúde para garantir tratamento oportuno.
                - **Monitoramento Contínuo**: Utilizar dados em tempo real para acompanhar o comportamento dos pacientes em relação à evolução da doença e adaptar estratégias conforme necessário.
            
                ---
            ''')