import os

# Application配置参数
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "debug":True,
    "cookie_secret":"CvvrEAo4RDS6b78NO+R+00PJcRE7Y0UXqjUj8vVOCRo=",
    "xsrf_cookies":True,
}


# mysql参数设置
mysql_options = dict(
    host="127.0.0.1",
    port=3306,
    db="ihome",
    user="root",
    passwd="admin",
    charset="utf8",
)


# redis参数设置
redis_options = dict(
    host="127.0.0.1",
    port=6379
)

# log日志参数设置
log_file = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"