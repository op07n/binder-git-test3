from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    PYTHONPATH="${PYTHONPATH}:/my/other/path2"
    Popen(["PYTHONPATH='${PYTHONPATH}:mushroom_challenge/' streamlit", "run", "mushroom_challenge/mushroom_app.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
