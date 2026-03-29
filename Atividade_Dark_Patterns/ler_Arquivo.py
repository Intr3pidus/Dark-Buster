import pandas as pd

def ler_arquivo_xlsx(nome_arquivo):
    try:
        # Lê o arquivo Excel e transforma em DataFrame
        df = pd.read_excel(nome_arquivo, engine = 'openpyxl')
        
        # Se você quiser que ele retorne uma lista de dicionários (igual ao JSON)
        return df.to_dict(orient = 'records')
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o Excel: {e}")
        return []