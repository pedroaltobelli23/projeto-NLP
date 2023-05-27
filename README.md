# projeto-NLP
Projeto NLP

Avaliação Final – NLP
Objetivo: elaborar, desenvolver, avaliar e entregar um produto de dados baseado em IA e NLP.

Parte 1: definir produto e buscar base de dados

1 - Defina um produto de IA/NLP baseado em dados (não pode ser um chatbot).
    
    a) Qual é o problema que esse produto resolve?

        Definir as tags de um video do youtube a partir de sua legenda completa
    
    b) Qual é o público a que o produto atende?

        Pessoas que querem postar videos no youtube

    c) Como esse produto se relaciona a machine learning?
        NLP


2 - Escolha uma base de dados (maior que a memória do seu computador – se precisar, faça webscrapping ou use APIs!)
	
    a) Baixe a base de dados
	
    b) Organize os dados de forma que possam ser lidos em minibatches pela API do Keras
	
    c) Defina qual (ou quais) métrica(s) poderiam ser usadas na sua base de dados para avaliar se IA e NLP são soluções viáveis para a realização do seu produto?


Parte 2: experimentar estratégias de machine learning

1 - Escolha algumas estratégias de machine learning para testar, incluindo, no mínimo:
	
    a) Uma abordagem tradicional “baseline” (por exemplo, as disponíveis no sklearn)
	
    b) Uma abordagem com Deep Learning treinada integralmente in-house
	
    c) Uma abordagem com Deep Learning que usa redes pré-treinadas para alimentar uma rede neural treinada in-house
	
    d) Uma abordagem com Deep Learning que usa integralmente uma rede pré-treinada, com o mínimo de pós-processamento (não precisa ser a mesma rede do ítem (c) )

2 - Compare o desempenho de cada uma das estratégias escolhidas. Para isso:
	
    a) Treine cada uma das redes in-house várias vezes, e encontre um intervalo de confiança de 95% para o desempenho.
	
    b) Compare o desempenho das quatro abordagens que você testou. Reporte o desempenho em um gráfico de barras com intervalos de confiança.
	
    c) Encontre casos típicos de erro para cada um dos sistemas treinados.
	
    d) Salve os modelos treinados

Parte 3: Avalie o custo computacional de inferência dos sistemas
	
    a) Avalie o tempo que cada um dos sistemas demora para responder a uma chamada de inferência (predict).
	
    b) Compare o tamanho dos modelos e a memória RAM usada por cada um deles ao ser carregado para a memória.
	
    c) Levando em consideração as possibilidades de usar VMs gratuitas na Oracle, ou pagas na AWS, decida qual dos modelos é mais adequado para a sua aplicação.

Parte 4: Faça o deploy do sistema para uma API e uma demo
	
    a) Suba um pequeno servidor usando FastAPI, Django ou a tecnologia a sua escolha. Através de uma API REST, o usuário deve ser capaz de enviar dados ao sistema e receber uma resposta.
	
    b) Faça uma página HTML/Javascript que permita acessar facilmente uma demonstração da API através da web.