from app import app

# Adaptador para Vercel
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)