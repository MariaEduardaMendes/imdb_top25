import scraping
import banco_de_dados
import analise_de_dados
import json

def main():
    """Sequência e comando de execução."""

    try:
        with open("Maria_Mendes_DR4_AT/config.json", "r") as f:
            config = json.load(f)
            url = config["url_imdb"]
            n_filmes = config["n_filmes"]
            print(f"Configuração carregada: Ler {n_filmes} filmes do IMDb.")
    except FileNotFoundError:
        print("Aviso: config.json não encontrado. Usando valores padrão.")
        url = "https://www.imdb.com/chart/top/"
        n_filmes = 250

    print("\n--- 1. Iniciando Scraping ---")
    meu_catalogo = scraping.scraping(url, n_filmes)
    
    print("\n--- 2. Atualizando Banco de Dados ---")
    df_filmes, df_series = banco_de_dados.banco_de_dados(meu_catalogo)
    
    print("\n--- 3. Realizando Análise de Dados ---")
    analise_de_dados.analise_de_dados(df_filmes, df_series)

if __name__ == "__main__":
    main()