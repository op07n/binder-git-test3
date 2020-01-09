from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    Popen(["streamlit", "run", "mushroom_challenge/mushroom_app.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"],env=dict(os.environ, PYTHONPATH="${PYTHONPATH}:mushroom_challenge/"))
