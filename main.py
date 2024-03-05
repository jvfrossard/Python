#versão usando polars
import polars as pl

conversas = pl.read_csv("relatorio-sample.csv",ignore_errors=True,separator=';')
conversas = conversas.with_columns(pl.col("Data da mensagem").str.slice(0,10)).drop_nulls()

result = (
    conversas.group_by("Data da mensagem")
    .agg(pl.col("Identificador").n_unique().alias("quantidade de identificadores"))
    .sort("Data da mensagem")
)

print(result["quantidade de identificadores"].sum())

#versão usando pandas
import pandas as pd

conversas = pd.read_csv("relatorio-sample.csv",sep=';')
conversas["Data da mensagem"] = conversas["Data da mensagem"].str.slice(0, 10)

result = (
    conversas.groupby("Data da mensagem")
    .agg({"Identificador": "nunique"})
    .rename(columns={"Identificador": "quantidade de identificadores"})
    .sort_values("Data da mensagem")
)

total_identificadores = result["quantidade de identificadores"].sum()

print(total_identificadores)