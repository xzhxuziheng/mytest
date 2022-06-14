import pymysql
from common import yaml_util


yaml_data = yaml_util.read_yaml('/baseconfig.yaml')
host = yaml_data['host']
port = yaml_data['port']
user = yaml_data['user']
password = yaml_data['password']
db = yaml_data['db']
charset = yaml_data['charset']


# 连接MySQL数据库
def connect_mysql():
    try:
        db_mysql = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db,
            charset=charset
        )
        return db_mysql
    except Exception:
        raise Exception("数据库连接失败")


if __name__ == '__main__':
    db_mysql = connect_mysql()
    cur = db_mysql.cursor()
    sql = 'select * from bike_model'
    select_result = cur.execute(sql)
    data = cur.fetchall()
    print(len(list(data)))
    print(list(data))
    print(data)