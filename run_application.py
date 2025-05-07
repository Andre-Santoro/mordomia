import subprocess
import os

# Caminho até o arquivo main.py (ajuste se estiver em outra pasta)
caminho_arquivo = os.path.join(os.getcwd(), "main.py")

# Comando para rodar o Streamlit
subprocess.run(["streamlit", "run", caminho_arquivo])