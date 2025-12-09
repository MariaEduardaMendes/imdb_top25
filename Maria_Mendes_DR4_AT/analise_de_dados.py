def analise_de_dados(df_movies, df_series):
    """Funçao geral para a análise de dados."""

    #EX 8 Análise e exportação de filmes e séries

    df_movies = df_movies.sort_values(by='rating', ascending=False)
    df_movies_filtrado = df_movies[df_movies['rating'] > 9.0]
    print(df_movies_filtrado.head())

    try:
        df_movies_filtrado.to_csv("Maria_Mendes_DR4_AT/data/movies.csv", index=False)
        df_series.to_csv("Maria_Mendes_DR4_AT/data/series.csv", index=False)

        df_movies_filtrado.to_json("Maria_Mendes_DR4_AT/data/movies.json", orient="records", indent=4)
        df_series.to_json("Maria_Mendes_DR4_AT/data/series.json", orient="records", indent=4)
    except PermissionError:
        print("Erro de permissão.")
    except OSError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro: {e}")

    #EX 9 Classificação textual das notas

    def avaliar_nota(nota):

        """Função que recebe uma nota e retorna uma categoria textual."""

        if nota >= 9.0:
            return "Obra-prima"
        elif nota >= 8.0:
            return "Excelente"
        elif nota >= 7.0:
            return "Bom"
        else:
            return "Mediano"
        
    df_movies['categoria'] = df_movies["rating"].apply(avaliar_nota)
    colunas = ["title", "rating", "categoria"]

    print(df_movies[colunas].head(10))

    #EX 10 Resumo de filmes por categoria

    resumo = df_movies.pivot_table(
        index="year", 
        columns="categoria", 
        values="title", 
        aggfunc="count",
        fill_value=0
    )

    resumo = resumo.sort_index(ascending=False)

    print(resumo)