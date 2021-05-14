from app.httpServer import App
from dotenv import load_dotenv

load_dotenv('.env')
app = App()
app.run()
