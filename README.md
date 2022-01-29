# Multi-Classification_Election


## Sobre o algoritmo
* Nesse projeto foi feito um modelo de multi-classificação dos candidatos a vereadores de Campos dos Goytacazes se será eleito, não eleito ou suplente.
Basicamente o modelo vai receber um grande grupo de dados com características do candidato e o algoritmo irá determinar o resultado. O grande desafio foi justamente fazer o modelo ter 3 saídas diferente dos modelos de classificação que tem 0 ou 1 como saída, que foi uma nova experiência.


* A explicação detalhada linha por linha você encontra aqui (https://github.com/PFCalanca/Multi-Classification_Election/blob/master/Eleicao_Classification_with_Keras.ipynb)



## Tecnologias  

Tecnologias usadas no projeto.

* Python
* Pandas
* Numpy
* Keras
* Tensorflow
* Streamlit


## Observação 
* Caso tente replicar esse projeto mude o diretório para as pastas onde está o dataset deixada no git (
Multi-Classification_Election/Datasets/nome_dataset.csv ).
 ![Posts](https://github.com/PFCalanca/Multi-Classification_Election/blob/master/readme/datasetsalert.png)
  
## Sobre o modelo: 
![Post show](https://github.com/PFCalanca/Multi-Classification_Election/blob/master/readme/modelop.png)

* O modelo foi feito com 3 camadas densas, aqui precisamos ter muito cuidado, pois numeros de camadas não significa uma acurácia maior, então temos que ter a noção para não ultrapassar nem faltar.
  
## Acurácia: 
![Post show](https://github.com/PFCalanca/Multi-Classification_Election/blob/master/readme/acuracia.png)

* Nesse modelo tive uma acurácia de 94% que não é tão ruim ja que utilizamos poucos dados.
  
## Testes: 
  * Se não tivesse aplicado a SMOTE() eu teria uma acurácia alta, mas ao aplicar esses testes teríamos um gráfico bem desalinhado com a realidade, com a visualização temos uma segurança maior sobre a acurácia do modelo.
 <center>
  
  ![Post show](https://github.com/PFCalanca/Multi-Classification_Election/blob/master/readme/modeteste1.png) 
  
  ![Post show](https://github.com/PFCalanca/Multi-Classification_Election/blob/master/readme/acuraciateste.png)
 
  * Uma outra maneira de comprovar que o modelo funciona é o teste de precisão, que sem o balanceamento usando SMOTE() daria 0.
  
  ![Post show](https://github.com/PFCalanca/Multi-Classification_Election/blob/master/readme/vantagemsmote.png) 
</center>


## Links
  - Repository: https://github.com/PFCalanca
    - Caso você encontre algum erro ou tenha alguma observação, entre em contato.


  ## Autor

  * **Paulo de Freitas Calanca** 

  Please follow github and join us!
  Thanks to visiting me and good coding!
