import psycopg2 as pg
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

def conectar_banco(visualizacao_youtube, inscricao_youtube, visualizacao_youtube_28dias, visualizacao_youtube_48horas, seguidores_linkedin, impressoes_28dias, impressores_90dias):
    try:
        conexao = pg.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO dados_redes_sociais (
                visualizacao_youtube,
                inscricao_youtube,
                visualizacao_youtube_28dias,
                visualizacao_youtube_48horas,
                seguidores_linkedin,
                impressoes_28dias,
                impressores_90dias
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                visualizacao_youtube,
                inscricao_youtube,
                visualizacao_youtube_28dias,
                visualizacao_youtube_48horas,
                seguidores_linkedin,
                impressoes_28dias,
                impressores_90dias
            ))
        
        conexao.commit()
        st.success("Dados Salvos Com Sucesso!!!!")
        cursor.close()
        conexao.close()


    except Exception as e:
        st.error(f'Error ao se conectar com o banco {e}')
        cursor.close()
        conexao.close()

        
if __name__ == '__main__':
    print(conectar_banco())