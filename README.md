# Prevendo o tipo de usuário de acordo com seus padrões de carregamento de carro elétrico


<div align="center" style="max-width:68rem;">
<table>
  <tr>
    <td align="center">
        <a href="https://github.com/gianvr"><img src="https://avatars.githubusercontent.com/gianvr" alt="Giancarlo Ruggiero" width="100" style="border-radius: 50%;" /><br />
        <sub><b>Giancarlo Ruggiero</b></sub></a><br />
        Developer
    </td>
    <td align="center">
        <a href="https://github.com/Peng1104"><img src="https://avatars.githubusercontent.com/Peng1104" alt="Lucas Hix" width="100" style="border-radius: 50%;" /><br />
        <sub><b>Lucas Hix</b></sub></a><br />
        Developer
    </td>
  </tr>
</table>
</div>

## Dependências

Para instalar as dependências necessárias, execute o comando abaixo:

```bash
pip install -r requirements.txt
```


## Objetivo

O objetivo deste projeto tem como prever o tipo de usuário de acordo com seus padrões de carregamento de carro elétrico. Os tipos são:

- Long-distance traveler
- Casual driver

As variáveis utilizadas para a previsão são:

- Vehicle Model
- Charging Station Location
- Time of Day
- Day of Week
- Charger Type
- Battery Capacity
- Charging Cost
- Charging Duration
- Charging Rate
- Distance Driven
- Energy Consumed
- State of Charge End
- State of Charge Start
- Temperature
- Vehicle Age

## Dataset

> [!TIP]
> A análise exploratória do dataset pode ser encontrada no arquivo `notebooks/exploratory_analysis.ipynb`.

O dataset utilizado foi obtido no [Electric Vehicle Charging Patterns](https://www.kaggle.com/datasets/valakhorasani/electric-vehicle-charging-patterns). 

Além das classes de usuários citadas acima, o dataset original possui a classe `commuter` que foi removida para simplificação do projeto. Algumas variáveis, sendo elas: `Charging Start Time`, `Charging End Time`, `User ID`, `Charging Station ID` foram removidas por não serem relevantes ou serem redundantes.

## Treinamento

> [!TIP]
> O treinamento do modelo pode ser encontrado no arquivo `notebooks/training.ipynb`.

O modelo utilizado foi o `RandomForestClassifier`. Inicialmente foi utilizado o `GridSearchCV` para encontrar os melhores hiperparâmetros para o modelo, entretanto, devido a sua baixa acurácia, foi utilizado o `SequentialFeatureSelector` para selecionar as melhores features para o modelo, com os hiperparâmetros obtidos no `GridSearchCV`.

## Avaliação

A acurácia do modelo foi de `0.79`. Mais detalhes sobre a avaliação do modelo podem ser encontrados no arquivo `notebooks/training.ipynb`.


## API

Para executar a API, execute o comando abaixo:

- Produção

```bash
fastapi run app/main.py
```

- Desenvolvimento

```bash
fastapi dev app/main.py
```

Após a execução acesse a documentação da API em `http://127.0.0.1:8000/docs`.


## Autores

- Giancarlo Vanoni Ruggiero
- Lucas Hix