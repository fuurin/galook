from src.app import create_app
import os

app = create_app()

if __name__ == '__main__':
    if os.environ["SSL_DIR"]:
        ssl_dir = os.environ["SSL_DIR"]
        ssl_context = (f"{ssl_dir}/fullchain.pem", f'{ssl_dir}/privkey.pem')
        app.run(host='0.0.0.0', port=443, ssl_context=ssl_context, threaded=True, debug=False)
    else:
        app.run(debug=True)