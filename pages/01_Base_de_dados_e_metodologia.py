import streamlit as st
import pandas as pd
from PIL import Image

# configura características da página
st.set_page_config(page_title='Dados Selecionas & Metodologia', page_icon='https://th.bing.com/th?id=ODLS.b7e13985-946a-47c6-8d8e-a4d10d1e8063&w=32&h=32&qlt=90&pcl=fffffa&o=6&pid=1.2', initial_sidebar_state='expanded')

# seta header image da página
page01_header_image = Image.open('imgs/header_principal.png')
st.image(page01_header_image, caption='Image credit: Fusion Medical Animation at Unsplash')

# cria tabs de conteúdo da página
tab1, tab2, tab3 = st.tabs(['Sobre o PNAD-COVID', 'Base de dados', 'Objetivos'])

# tab 1 - Sobre o PNAD-COVID
with tab1:
    st.markdown('''
        # Sobre o PNAD-COVID
        
        O PNAD-COVID-19 do IBGE, foi implementado em plena Pandemia, com o objetivo de levantar informações sobre os sintomas referidos da síndrome gripal, além de ser utilizada como ferramenta para monitoramento e avaliação dos impactos da crise no mercado de trabalho brasileiro. Além de informações sobre a saúde, esta pesquisa também elucida aspectos socieconômicos e demográficos da crise. Desta forma, é possível entender nuances e buscar alternativas para planejamento e recuperação dessa e de outras possíveis Pandemias que possam, eventualmente, assolar o país.
                
        O PNAD-COVID-19 foi o primeiro estudo divulgado com o selo de Estatística Experimental, ou seja, uma análise que ainda está sob avaliação por não ter atingido um grau completo de maturidade em termos de harmonização, cobertura e metodologia.
        
        ## Relevância do PNAD-COVID
        
        Em um mundo dominado pela polarização política durante a maior crise sanitária da história recente, um estudo com a proposta do PNAD-COVID-19 tras ponderamento lógico, embasamento científico e análise crítica em relação às ações tomadas pelos órgãos responsáveis pela gestão da crise, também dominados pelos discursos "políticos-polizadores".
        
        Tivéssemos tido maturidade durante a crise, focando nossa atenção e esforços em frentes e iniciativas como a do PNAD-COVID-19, talvez, a perda de tempo e vidas pudesse ter sido menor. É provável que tivéssemos testemunhado a um número menor de perda de vidas e, quem sabe, uma consequência social e econômia menos severa.
        
        Em tempos em que a sociedade (a nível global) baseia formação de opinião e decisões importantes em algorítimos de redes sociais, encontrar iniciativas como esta, evidencia a importância do estudo aprofundado de todos os tópicos que envolvam o bem-estar de uma população. Quem sabe assim, seja possível começar a trazer atenção e foco para a importância da **decisão informada** e do **pensamento crítico** que, se dúvidas, exigem um pouco mais de atenção e esforço para responder a uma pergunta, do que 15 segundos de um vídeo.
        
        ---
    ''')

# tab 2 - Base de Dados
with tab2:
    st.markdown('''

        # Base de Dados selecionada
        
        Por ser um estudo experimental de um projeto acadêmico de Pós-graduação que tem como objetivo exclusivo, colocar em prática conhecimentos técnicos adquiridos durante o desenvolvimento do módulo, o escopo do que pode ser explorado nas bases de dados foi limitada. De acordo com as instruções do desafio proposta, poderíamos limitar a elaboração da nossa base de dados a 20 perguntas do questionário aplicado pelo IBGE. Além disso, limitamos a nossa base aos meses de maio, junho e julho de 2020, todos disponibilizados no site do [PNAD-COVID-19](https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=downloads&utm_source=covid19&utm_medium=hotsite&utm_campaign=covid_19). Contudo, além dos dados de questionários (20 perguntas), selecionamos como extra, algumas informações que iremos chamar de **Dados Demográficos**, contendo informações básicas da população pesquisada.

        ## Análise de frentes únicas
        
        Com a estruturação da base de dados como mencionamos anteriormente, será possível abordar três frentes diferentes na análise: **Sintomas Clínicos**, **Perfil Populaciona** e **Impactos Econômicos**.
        
        ### Dados Demográficos
        
        Dicionário que mostra os campos de informações básicas da população pesquisada.
    ''')

    # desenha tabela com dados demográficos
    st.markdown('''
                            | Código | Descrição |
                            | ------ | --------- |
                            | UF | Unidade da Federação |
                            | CAPITAL | Capital |
                            | RM_RIDE | Região Metropolitana e Região Administrativa Integrada de Desenvolvimento |
                            | V1012 | Semana no mês |
                            | V1013 | Mês da pesquisa |
                            | V1022 | Situação do domicílio |
                            | V1023 | Tipo de área |
                            | A002 | Idade do morador |
                            | A003 | Sexo |
                            | A004 | Cor ou raça |
                            | A005 | Escolaridade |
                ''')



    st.markdown('''
    
        ### Dados Clínicos, Econômicos e Comportamentais
    
        Dicionário que mostra os campos de informações sobre sintomas clínicos e de comportamento, coletados durante a Pandemia.
    ''')

    # desenha tabela com dados comportamentais, econômicos e clínicos
    st.markdown('''
                  | Pergunta | Código | Descrição |
                  | -------- | ------ | --------- |
                  | 1 | B0011 | Na semana passada teve febre? |
                  | 2 | B0012 | Na semana passada teve tosse? |
                  | 3 | B0013 | Na semana passada teve dor de garganta? |
                  | 4 | B0014 | Na semana passada teve dificuldade para respirar? |
                  | 5 | B0015 | Na semana passada teve dor de cabeça? |
                  | 6 | B0016 | Na semana passada teve dor no peito? |
                  | 7 | B0017 | Na semana passada teve náusea? |
                  | 8 | B0018 | Na semana passada teve nariz entupido ou escorrendo? |
                  | 9 | B0019 | Na semana passada teve fadiga? |
                  | 10 | B00110 | Na semana passada teve dor nos olhos? |
                  | 11 | B00111 | Na semana passada teve perda de cheiro ou sabor? |
                  | 12 | B00112 | Na semana passada teve dor muscular? |
                  | 13 | B00113 | Na semana passada teve diarreia? |
                  | 14 | B002 | Por causa disso, foi a algum estabelecimento de saúde? |
                  | 15 | B006 | Durante a internação, foi sedado, entubado e colocado em respiração artificial com ventilador |
                  | 16 | B007 | Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público |
                  | 17 | B009B | Qual o resultado? (SWAB) |
                  | 18 | B011 | Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr(a) restringiu o contato com as pessoas? |
                  | 19 | C013 | Na semana passada, o(a) Sr(a) estava em trabalho remoto (home office ou teletrabalho)? |
                  | 20 | D0051 | Auxílios emergenciais relacionados ao coronavirus |
                
                ---
                ''')

# tab 3 - Objetivos
with tab3:
    st.markdown('''
        
        # Objetivo da análise
                
        Ao utilizar a base do [PNAD-COVID-19 do IBGE](https://covid19.ibge.gov.br/pnad-covid/), será criada uma nova base para análise, considerando as seguintes características:

        - Utilização de no máximo 20 questionamentos realizados na pesquisa;
        - Utilizar 3 meses para construção da solução;
        - Caracterização dos sintomas clínicos da população;
        - Comportamento da população na época da COVID-19;
        - Características econômicas da Sociedade;

        À partir disso, **o objetivo é desenvolver uma breve análise sobre o processo de organização do banco**, as perguntas selecionadas para a resposta do problema e quais seriam as principais ações que um hospital deveria tomar em caso de um novo surto de COVID-19.
    ''')
