import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
# 导入配置文件
import config
import pymysql
import redis

from tornado.options import define, options
# 导入urls路由文件
import urls
# 设置服务器端口号
define("port", default=8000, type=int)


class Application(tornado.web.Application):
    """"""
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        # 创建一个全局mysql连接实例供handler使用，并从config配置文件导入mysql配置参数
        self.db = pymysql.connect(**config.mysql_options)
        # 创建一个全局redis连接实例供handler使用，并从config配置文件导入redis配置参数
        self.redis = redis.StrictRedis(**config.redis_options)


def main():
    # 设置log日志等级
    options.logging = config.log_level
    # 设置log日志保存路径
    options.log_file_prefix = config.log_file
    tornado.options.parse_command_line()
    app = Application(
            # 从urls导入handlers信息，从config配置文件导入settings信息
            urls.handlers, **config.settings
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()