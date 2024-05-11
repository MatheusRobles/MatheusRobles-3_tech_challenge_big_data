# 🦾 Tech Challenge - Big Data

Este é um projeto acadêmico do curso de [Pós-Graduação da FIAP em Data Analytics](https://postech.fiap.com.br/curso/data-analytics/), por isso, esta análise ficará restrita à população brasileira, utilizando os dados do [PNAD-COVID-19, produzidos pelo IBGE](https://covid19.ibge.gov.br/pnad-covid/).
    
Selecionamos 20 perguntas do questionário aplicado pelo IBGE, durante a elaboração do estudo. Esses dados foram todos retirados da base de dados disponível do site do PNAD-COVID e, para a análise apresentada nesta aplicação, consideramos três meses (maio, junho e julho) de 2020.


## ⚙️ Estrutura do Projeto

Descreva aqui a estrutura do seu projeto. Por exemplo:

- `imgs/`: Contém imagens utilizadas para elaboração da aplicação.
- `notebooks/`: Contém notebooks com análise exploratória e gráficos plotados
- `pages/`: Contém páginas dependentes da Home.
- `function/`: Contém as funções de tratamento dos dados e geração de graficos.
- `data/`: Contém os dataframes tratados.


## 🚀 Como Executar

Este projeto foi desenvolvido para ser uma aplicação streamlit. A base de dados [(`base_tratada_pnad.csv`), está disponível em uma pasta pública do drive](https://drive.google.com/file/d/1UsilAr5m7NT6SKCP1D9QtmtXQYkhx7tX/view?usp=sharing). Ao copiar este projeto, para rodar o streamlit, baixe a base localmente, atualize o _path_ dos arquivos nos _notebooks_ e rode o _script_, conforme passos a seguir:


1. Instale o Streamlit usando pip, que é o gerenciador de pacotes do Python. Você pode fazer isso executando o seguinte comando no terminal:

`pip install streamlit`

2. Navegue até o diretório do seu projeto Streamlit usando o comando cd. Por exemplo, se o seu projeto estiver no diretório my_project, você pode usar o seguinte comando:

`cd my_project`

3. Execute o seu aplicativo Streamlit. Se o seu aplicativo Streamlit estiver em um arquivo chamado app.py, você pode usar o seguinte comando:

`streamlit run Home.py`

5. O Streamlit irá iniciar um servidor local e fornecerá um URL que você pode abrir em seu navegador para visualizar o aplicativo.

# 🦾 O Desafio

O Tech Challenge é um desafio técnico, feito em grupo que, todo final de módulo é apresentado para que os alunos apliquem os conhecimentos adquiridos no decorrer das aulas.

## 👊 O problema

Do ponto de vista de "um grande hospital", entender como foi o comportamento da população no período da COVID-19 e quais indicadores seriam importante para o planejamento, caso haja um novo surto da doença.

Para a realização desta análise, será utilizado o estudo do PNAD-COVID19 do IBGE, como base para busca da resposta do problema proposto.

## 🎲 Dados triviais

O desafio deixa o grupo livre para definir quais são os dados que serão utilizados na análise, contudo, três dados são triviais:

- Característica clínicas dos sintomas;
- Características da população;
- Características econônimcas da sociedade.

### Dados selecionados

#### Dados básicos
Dados básicos sobre respondentes, utilizado para contexto, segmentação e identificação da população pesquisada.

- **Código da Variável**: UF
    **Descrição da Variável** Unidade da Federação

- **Código da Variável**: CAPITAL
    **Descrição da variável**: Capital do Estado

- **Código da Variável**: RM_RIDE
    **Descrição da variável**: Região Metropolitana Adminstrativa Integrada de Desenvolvimento

- **Código da Variável**: V1012
    **Descrição da variável**: Semana no mês - 1 a 4 (indicando qual semana em do mês em que a pesquisa foi tomada)

- **Código da Variável**: V1013
    **Descrição da variável**: Mês da pesquisa - 1 a 12 (indicando em qual mês do ano a pesquisa foi tomada)

- **Código da Variável**: V1022
    **Descrição da Variável**: Situação do domicílio - 1 | Urbanda; 2 | Rural

- **Código da Variável**: V1023
    **Descrição da Variável**: Tipo de área  
        
        1- Capital; 
        2 - Resto da RM (Região Metropolitana, excluindo a capital);
        3 - Resto da RIDE (Região Integrada de Desenvolvimento Econômico, excluindo a capital); 
        4 - Resto da UF  (Unidade da Federação, excluindo a região metropolitana e a RIDE)

- **Código da Variável**: A002
    **Descrição da Variável**: 000 a 130 (idade em anos)

- **Código da Variável**: A003
    **Descrição da Variável**: Sexo (gênero)
        1 - Homem; 
        2 - Mulher

- **Código da Variável**: A004
    **Descrição da Variável**: Cor ou raça
        1 -  Branca; 
        2 -  Preta; 
        3 -  Amarela; 
        4 -  Parda; 
        5 -  Indígena; 
        9 -  Ignorado

- **Código da Variável**: A005
    **Descrição da Variável**: Escolaridade 1 - Sem instrução; 
        2 - Fundamental incompleto; 
        3 - Fundamental completa; 
        4 - Médio Incompleto; 
        5 - Médio completo; 
        6 - Superio incompleto; 
        7 - Superior completo; 
        8 - Pós-graduação, mestrado ou doutorado

#### Dados de análise

- 1. **Código da Variável**: B011
    **Descrição da Variável**: Na semana passada teve febre?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 2. **Código da Variável**: B012
    **Descrição da Variável**: Na semana passada teve tosse?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 3. **Código da Variável**: B013
    **Descrição da Variável**: Na semana passada teve dor de garganta?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado 

- 4. **Código da Variável**: B014
    **Descrição da Variável**: Na semana passada teve dificuldade para respirar?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 5. **Código da Variável**: B015
    **Descrição da Variável**: Na semana passada teve dor de cabeça?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 6. **Código da Variável**: B016
    **Descrição da Variável**: Na semana passada teve dor no peito?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 7. **Código da Variável**: B017
    **Descrição da Variável**: Na semana passada teve náusea?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 8. **Código da Variável**: B018
    **Descrição da Variável**: Na semana passada teve nariz entupido ou escorrendo?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 9. **Código da Variável**: B019
    **Descrição da Variável**: Na semana passada teve fadiga?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 10. **Código da Variável**: B00110
    **Descrição da Variável**: Na semana passada teve dor nos olhos?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 11. **Código da Variável**: B00111
    **Descrição da Variável**: Na semana passada teve perda de cheiro ou sabor?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 12. **Código da Variável**: B00112
    **Descrição da Variável**: Na semana passada teve dor muscular?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 13. **Código da Variável**: B00113 - maio sem / junho sem / julho tem
    **Descrição da Variável**: Na semana passada teve diarréia?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 14. **Código da Variável**: B002
    **Descrição da Variável**: Por causa disso, foi a algum estabelecimento de saúde?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado
            Não Aplicável

- 15. **Código da Variável**: B006
    **Descrição da Variável**: Durante a internação, foi sedados, entubado e colocado em respiração artificial com ventilador?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado
            Não Aplicável

- 16. **Código da Variável**: B007
    **Descrição da Variável**: Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público?
        1 - Sim;
        2 - Não;
        3 - Não sabe;
        9 - Ignorado

- 17. **Código da Variável**: B009B - maio sem / junho sem / julho tem
    **Descrição da Variável**: Qual o resultado (SWAB)?
        1. Positivo
        2. Negativo
        3. Inconclusivo
        4. Ainda não recebeu o resultado
        9. Ignorado
           Não aplicável

Esta pergunta é sequência da pergunta B009A (Fez o exame coletado com cotonete na boca e / ou nariz (SWAB)?).

- 18. **Código da Variável**: B011 - MAIO SEM / junho sem / julho tem
    **Descrição da Variável**: Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr(a) restringiu o contato com as pessoas?
        1. Não fez restrição, levou vida normal como antes da pandemia
        2. Reduziu o contato com as pessoas, mas continuou saindo de casa para trabalho ou atividades não essenciais e/ou recebendo visitas
        3. Ficou em casa e só saiu em caso de necessidade básica
        4. Ficou rigorosamente em casa
        9. Ignorado

- 19. **Código da Variável**: C013
    **Descrição da Variável**: Na semana passada, o(a) Sr(a) estava em trabalho remoto (_home office_ ou teletrabalho)?
        1. Sim
        2. Não
           Não aplicável

- 20. **Código da Variável**: D0051 D1
    **Descrição da Variável**: Auxílios emergenciais relacionados ao Coronavírus
        1. Sim
        2. Não

## 🎯 Objetivo

Ao utilizar a base do [PNAD-COVID-19 do IBGE](https://covid19.ibge.gov.br/pnad-covid/), será criada uma nova base para análise, considerando as seguintes características:

- Utilização de no máximo 20 questionamentos realizados na pesquisa;
- Utilizar 3 meses para construção da solução;
- Caracterização dos sintomas clínicos da população;
- Comportamento da população na época da COVID-19;
- Características econômicas da Sociedade;

À partir disso, desenvolver uma breve análise sobre o processo de organização do banco, as perguntas selecionadas para a resposta do problema e quais seriam as principais ações que o hospital deverá tomar em caso de um novo surto de COVID-19.

## 🕹️ Organização do Banco de Dados

Utilizando o Google Big Query, foi feito o _download_ das bases do PNAD-COVID dos meses de maio, junho e julho de 2020. Depois disso, foi feito um tratamento nas planilhas, de modo que todas ficassem com a mesma quantidade de coluna e com os seus tipos de dados padronizados.