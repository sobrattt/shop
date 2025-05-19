from application import app
from threading import Thread
from application.parser.extractors import run_parser



thread = Thread(target=run_parser, daemon=True)

thread.start()
app.run()
