import subprocess
import os

caminho_arquivo = os.path.join(os.getcwd(), "app.py")

subprocess.run(["streamlit", "run", caminho_arquivo])