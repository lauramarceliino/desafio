# Processamento e Análise de Dados de Comércio Exterior

Este repositório contém os scripts utilizados para processar, limpar e armazenar dados de importação e exportação referentes aos anos de 2020 e 2021. O objetivo final é fornecer um banco de dados otimizado para a criação de um dashboard interativo no Power BI.

---

## O Que Foi Feito?

Para preparar os dados, segui uma série de passos documentados em scripts Python:

1.  **Verificação da Qualidade dos Dados:** Inicialmente, realizei uma verificação preliminar dos dados brutos (`passo1-verificar_qualidade_raw.py`) para identificar possíveis problemas e inconsistências antes do processamento.
2.  **Adição de Descrição dos Produtos:** Utilizando um arquivo `NCM.csv`, adicionei uma coluna com a descrição detalhada dos produtos aos dados brutos (`passo2-adicionar_descricao.py`). Isso enriquece a análise, tornando os produtos mais fáceis de identificar.
3.  **Limpeza e Unificação de Dados:** Realizei a limpeza e a união dos arquivos de importação e exportação. Os dados foram centralizados em uma única estrutura, mas mantendo a distinção entre importação e exportação para facilitar a análise posterior (`passo3-limpeza_uniao.py`).
4.  **Criação e Armazenamento no Banco de Dados:** Os dados processados foram armazenados em um banco de dados SQLite (`passo4-criar_db.py`). O arquivo resultante, **`dados_comercio_exterior1.db`**, centraliza todas as informações em um formato otimizado para conexão com ferramentas de Business Intelligence.

---

## Como Replicar o Processo

Para recriar demais arquivos `.csv` processados, é necessário rodar os scripts na ordem em que foram apresentados. No entanto, para obter os dados de forma rápida e conectá-los diretamente ao Power BI, você pode utilizar o arquivo `.db` já fornecido ou os dois arquivos `EXP_dados_unificados.csv` e `IMP_dados_unificados.csv`.

### Requisitos

Para rodar este projeto e se conectar ao banco de dados, você precisará dos seguintes requisitos:

* **Python:** Os scripts foram desenvolvidos em Python.
* **Power BI:** A ferramenta foi utilizada para criar o dashboard de visualização. Para visualizar o dashboard, é **obrigatório ter o Power BI instalado** em sua máquina.
* **SQLite:** O banco de dados foi criado com SQLite.
* **Conector ODBC:** Para conectar o banco de dados SQLite ao Power BI, é necessário ter um conector ODBC instalado e configurado em sua máquina.

---

## Dashboard de Análise

O arquivo do dashboard (`.pbix`) desenvolvido no Power BI se encontra dentro do projeto. Para visualizá-lo, basta abrir o arquivo no Power BI Desktop.

O dashboard foi projetado para responder às seguintes perguntas:

* Quais são os **top 3 produtos mais exportados por estado** nos anos de 2020 e 2021?
* Quais são os **top 3 produtos mais importados por estado** nos anos de 2020 e 2021?
* Quais são os **top 3 produtos exportados em cada mês de 2021 por estado**?
```
