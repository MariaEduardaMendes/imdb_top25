def banco_de_dados(catalog):
    """Função geral para o banco de dados."""
    from sqlalchemy import create_engine, Column, Integer, String, Float
    from sqlalchemy.orm import declarative_base, sessionmaker
    from classes import Movie as POOMovie, Series as POOSeries

    #EX 6 Banco de dados imdb.db com SQLAlchemy

    engine = create_engine("sqlite:///Maria_Mendes_DR4_AT/data/imdb.db", echo=False)
    Base = declarative_base()

    class Movie(Base):
        __tablename__ = "movies"
        id = Column(Integer, primary_key=True)
        title = Column(String, nullable=False)
        year = Column(Integer, nullable=False)
        rating = Column(Float, nullable=False)

    class Series(Base):
        __tablename__ = "series"
        id = Column(Integer, primary_key=True)
        title = Column(String, nullable=False)
        year = Column(Integer, nullable=False)
        seasons = Column(Integer, nullable=False)
        episodes = Column(Integer, nullable=False)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for item in catalog:
        try:
            entry = None
            if isinstance(item, POOMovie):
                existe = session.query(Movie).filter_by(title=item.title).first()

                if existe:
                    raise ValueError(f"Filme '{item.title}' já consta no banco.")

                entry = Movie(
                    title = item.title,
                    year = int(item.year),
                    rating = float(item.rating)
                )

            elif isinstance(item, POOSeries):
                existe = session.query(Series).filter_by(title=item.title).first()

                if existe:
                    raise ValueError(f"Série '{item.title}' já consta no banco.")
                entry = Series(
                    title = item.title,
                    year = int(item.year),
                    seasons = int(item.seasons),
                    episodes = int(item.episodes)
                )

        except ValueError as e:
            print(f"Duplicado: {e}")
        except Exception as e:
            session.rollback()
            print(f"Erro: {e}")
        else:
            if entry is not None:
                session.add(entry)
                session.commit()

    #EX 7 Lendo os dados do banco com Pandas

    import pandas as pd

    try:
        df_movies = pd.read_sql_table('movies', con=engine)
        df_series = pd.read_sql_table('series', con=engine)

        print(df_movies.head())
        print(df_series.head())

        return df_movies, df_series

    except ValueError as e:
        print(f"Erro: {e}")
        return None, None

    except Exception as e:
        print(f"Erro: {e}")
        return None, None