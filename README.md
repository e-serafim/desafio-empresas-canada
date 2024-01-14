# Desafio de ciência de dados - Empresas Canada

## Contexto

Base disponibilizada: Desafio_ciencia_de_dados.xlsm
A Base de dados fornecida representa um conjunto de empresas do Canadá com a respectiva descrição de seus produtos, dados econômicos e localização.
Assim, podemos caracterizar cada variável:
- *name:* Nome da empresa;
- *description:* Descrição do produto da empresa;
- *employees:* Número de empregados da empresa;
- *total_funding:* Total de investimento já recebido pela empresa;
- *city:* Cidade;
- *subcountry:* Estado;
- *lat:* Latitude da cidade;
- *lng:* Longitude da cidade.

## Problema
Deseja-se prospectar empresas que possuam soluções em **tratamento de água** , principalmente,  elativas à : **solutions on waste and water, Improve water quality and water efficiency use, water contamination, water for human consumption, water resources**.

### EXERCÍCIO 1 
<b>Aplique um algoritmo de ML (ou um conjunto deles) capaz de selecionar as principais empresas indicadas para desenvolver a solução de acordo com seu alinhamento com o tema (Justifique a escolha do algoritmo).</b>
R: Utilizando um algoritmo de identificação de tópicos podemos separar as empresas que se assemelham pela descrição, assim resolvi utilizar um BERTopic onde os textos são transformados em embeddings e depois são agrupados por semelhança. Extraindo as principais palavras dos tópicos, podemos buscar as que mais se assemelham ao tema que queremos. Nessa execução do algoritmo dos mais de 400 tópicos identificados, apenas 3 possuem a palavra “water” como uma das principais palavras. Desses 3 entendo que 2 fazem sentido para nosso escopo, sendo as palavras principais desses tópicos [water, wastewater, membrane, treatment, wastewater treatment] e [water, esplash, contaminants, detect, fred] com 40 e 8 empresas respectivamente.

### EXERCÍCIO 2
<b>EXERCÍCIO 2 - Faça uma análise exploratória dos resultados acrescentando as demais variáveis contidas no dataset. Quais insights você pode obter a partir desses dados? Quais são as principais cidades (pólos de desenvolvimento) para essa solução? </b>
R: Analisando os locais das empresas no escopo temos que a maior parte delas estão em Ontario e Alberta. Olhando mais detalhadamente nas cidades, podemos ver que a maioria das empresas em Ontario são localizadas em Toronto e que todas as empresas no subcountry Alberta são localizadas na cidade de Calgary. Podemos também extrair algumas informações de empregados das empresas para ter mais informação sobre os tamanhos dessas empresas. Tamanho não necessariamente quer dizer qualidade nos produtos e soluções mas geralmente costumam ter uma correlação positiva. Focando nas cidades citadas anteriormente, temos que Toronto tem 7 empresas com 10 funcionários ou mais enquanto Calgary tem apenas 2 empresas, além disso Toronto tem 2 empresas com 50 funcionários ou mais enquanto Calgary não tem nenhuma.
Entrando no mérito de funding, 3 cidades tem empresas com o funding relevante que também pode indicar maior qualidade nos produtos e soluções, essas são Toronto, Vancouver e Calgary, com 3, 3 e 1 empresa respectivamente.
Assim, os principais polos de desenvolvimento estão localizados em Toronto, Vancouver e Calgary. Mas Toronto aparenta ter empresas mais solidas pelas informações contidas na base.

## Utilizando o Dockerfile

1) Para gerar a imagem python utilize o código abaixo:
```docker build -t imagem_desafio .```

2) Para iniciar o container com o jupyter notebook:
```docker run -p 8888:8888 --name container_desafio imagem_desafio```

3) Para acessar o jupyter pegue o token do terminal e acesse:
```http://127.0.0.1:8888/?token=<token_do_terminal>```

4) Por fim, será possível utilizar o mesmo notebook mas lembresse que os tópicos podem variar a cada execução. Caso tenha algum problema com os stopwords da lib nltk, é possível fazer o download dentro do próprio notebook com ```nltk.download()```