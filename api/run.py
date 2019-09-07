from src.app import app
import os

if __name__ == '__main__':
    if os.environ["SSL_DIR"]:
        ssl_dir = os.environ["SSL_DIR"]
        ssl_context = (f"{ssl_dir}/server.crt", f'{ssl_dir}/server.key')
        app.run(host='0.0.0.0', port=334, ssl_context=ssl_context, threaded=True, debug=False)
    else:
        app.run(debug=True)