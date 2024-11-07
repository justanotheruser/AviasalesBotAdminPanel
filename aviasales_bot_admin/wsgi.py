from aviasales_bot_admin.main import app
from a2wsgi import ASGIMiddleware

application = ASGIMiddleware(app)