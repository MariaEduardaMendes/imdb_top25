def scraping(url, qtd_filmes):
    """Função geral para o Web Scraping."""
    #EX 1 Scraping Básico do IMDb Top 25

    import urllib.request
    from bs4 import BeautifulSoup

    url = "https://www.imdb.com/chart/top/"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    titulos = []
    find_titulos = soup.find_all("h3", class_="ipc-title__text")
    for titulo in find_titulos:
        titulos.append(titulo.text)

    titulos.remove(titulos[-1])

    print("Top 10 Filmes no IMDB:")
    for titulo in titulos[:10]:
        print(titulo)

    #EX 2 Título, ano e nota dos filmes

    anos = []
    find_anos = soup.find_all("span", class_="sc-b4f120f6-7 hoOxkw cli-title-metadata-item")
    for ano in find_anos:
        if len((ano.text).strip()) != 4: #a mesma classe trazia classificação etária e duração 
            continue
        anos.append(ano.text)

    notas = []
    find_notas = soup.find_all("span", class_="ipc-rating-star--rating")
    for nota in find_notas:
        notas.append(nota.text)

    limite = min(len(titulos), len(anos), len(notas), qtd_filmes)

    dicionarios_filmes = []
    for i in range(limite):
        dicionario = {
            "título": titulos[i],
            "ano de lançamento": anos[i],
            "nota": notas[i]
        }
        dicionarios_filmes.append(dicionario)

    print("Top 5 detalhado:")
    for filme in dicionarios_filmes[:5]:
        print(f"- {filme["título"]} ({filme["ano de lançamento"]}) - Nota: {filme["nota"]}")

    #EX 5 Lista de objetos a partir do scraping

    from classes import Movie, Series

    catalog = []
    for i in range(len(dicionarios_filmes)):
        filme = Movie(titulos[i], anos[i], notas[i])
        catalog.append(filme)

    serie1 = Series("Friends", "1994", 10, 236)
    serie2 = Series("Grey's Anatomy", "2005", 21, 433)
    catalog.append(serie1)
    catalog.append(serie2)

    print("\nTodos os itens do catálogo:")
    for item in catalog:
        print(item)
    
    return catalog