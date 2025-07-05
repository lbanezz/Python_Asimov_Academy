import os
from streamlit.web import cli as stcli

os.argv = ["streamlit", "run", "app.py"]
os.system("streamlit run app.py")
