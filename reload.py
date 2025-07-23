import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Archivo principal del bot
ARCHIVO_BOT = "app.py"

# Proceso del bot
proceso_bot = None

# Manejador de eventos para watchdog
class BotHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global proceso_bot
        # Verificar si el archivo modificado es un archivo Python
        if event.src_path.endswith(".py"):
            print(f"Cambios detectados en {event.src_path}. Reiniciando el bot...")
            if proceso_bot:
                proceso_bot.terminate()  # Detener el bot actual
            proceso_bot = subprocess.Popen(["python", ARCHIVO_BOT])  # Reiniciar el bot

# Función principal
def main():
    global proceso_bot
    evento_handler = BotHandler()
    observador = Observer()
    observador.schedule(evento_handler, path=".", recursive=True)  # Monitorear todos los archivos
    observador.start()

    # Iniciar el bot por primera vez
    proceso_bot = subprocess.Popen(["python", ARCHIVO_BOT])

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observador.stop()
        if proceso_bot:
            proceso_bot.terminate()
    observador.join()

if __name__ == "__main__":
    main()