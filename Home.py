import streamlit as st
from PIL import Image

# configura características da página
st.set_page_config(page_title="Home", page_icon="https://th.bing.com/th?id=ODLS.b7e13985-946a-47c6-8d8e-a4d10d1e8063&w=32&h=32&qlt=90&pcl=fffffa&o=6&pid=1.2", layout="centered", initial_sidebar_state="expanded")


# seta header image da página
home_header_image = Image.open('imgs/header_principal.png')
st.image(home_header_image, caption='Image credit: Fusion Medical Animation at Unsplash')

# texto da homepage
st.markdown('''
    # COVID-19: nosso comportamento em uma crise global
            
    A Pandemia do COVID-19 é, sem dúvidas, um marco na história recente. Além de ser um acontecimento que mobilizou a humanidade, fomos testemunhas da luta de profissionais da saúde na linha de frente, cientistas, pesquisadores e toda a Comunidade Científica que se uniu para combater um adversário que, segundo a revista Nature, [poderia ter infectado 90% da população global e matado 40.6 milhões de pessoas](https://www.nature.com/articles/d41586-020-00966-w).
    
    Se se um lado testemunhávamos a união da comunidade científica numa corrida épica para busca da cura ou mitigação de uma doença potencialmente fatal para uma fatia considerável do globo, do outro lado, assistimos a crise ser politizada e transformada em arma para defesa de discursos ou ideias que, muitas vezes, não encontravam embasamento científico.
    
    Como ponte para ligar esses dois lados, havia a cobertura em tempo real da crise. Notícias que chegavam a todo momento, com números atualizados, teorias, hipóteses e uma coleção interminável de especialistas que pouco faziam para, de fato, ajudar a população que seguia - em sua grande maioria - às orientações da OMS e aguardava ansiosamente o desdobrar positivo de toda essa história.
    
    No meio de todas essas narrativas duvidosas, sempre foi muito difícil entender - de fato - como a Pandemia do Coronavirus afetou nossas vidas. Mais do que análises com opiniões de "especialistas", nunca ficou claro como, de fato, essa crise mudou a nossa economia; o comportamento da população durante a batalha para controle da disseminação da doenca; quais eram - de fato - os sintomas comuns?; qual foi a população mais atingida?; havia algum padrão possível de ser identificado para auxílio nesta luta?
    
    Essas e outras perguntas, respondidas de forma direta e com base em dados, naquele momento, poderiam ter sido preciosas para que pudéssemos ser capazes de criar melhores planos de ação para lidar com uma crise que escalou a nível global.
            
    ## Escopo da análise
    
    Este é um projeto acadêmico do curso de [Pós-Graduação da FIAP em Data Analytics](https://postech.fiap.com.br/curso/data-analytics/), por isso, esta análise ficará restrita à população brasileira, utilizando os dados do [PNAD-COVID-19, produzidos pelo IBGE](https://covid19.ibge.gov.br/pnad-covid/).
    
    Selecionamos 20 perguntas do questionário aplicado pelo IBGE, durante a elaboração do estudo. Esses dados foram todos retirados da base de dados disponível do site do PNAD-COVID e, para a análise apresentada nesta aplicação, consideramos três meses (maio, junho e julho) de 2020.
           
    ---
''')
