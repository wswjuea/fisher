
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], threaded=True)
    # threaded=True开启单进程多线程模式,在本地调试可用,部署在服务器上,已存在web服务器,不会使用flaskweb服务器
