import subprocess
from src.bot import IELTSBot

def start_ollama():
    try:
        subprocess.run(["ollama", "run", "llama3.1"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to start Ollama. Make sure it's installed and the llama2 model is available.")
        exit(1)

if __name__ == "__main__":
    start_ollama()
    bot = IELTSBot()
    bot.start()