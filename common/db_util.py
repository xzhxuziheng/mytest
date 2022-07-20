import pymysql
from common import yaml_util


yaml_data = yaml_util.read_yaml('/baseconfig.yaml')
host = yaml_data['mysql_host']
port = yaml_data['mysql_port']
user = yaml_data['mysql_user']
password = str(yaml_data['mysql_password'])
db = yaml_data['mysql_db']
charset = yaml_data['mysql_charset']


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


def handle_mysql(sql):
    conn = connect_mysql()
    cur = conn.cursor()
    for sql_data in sql:
        cur.execute(sql_data)
        try:
            conn.commit()
        except:
            conn.rollback()
    conn.close()


if __name__ == '__main__':
    # s = [
    #     'select * from app001_publisher',
    #     'insert into app001_publisher (`name`, `address`) values ("hhh", "a")'
    # ]
    # s = [
    #     'delete from merchant where name = "API-test1"'
    # ]
    # handle_mysql(s)
    s = yaml_util.read_yaml('/all_testcase/case/mysql.yaml')['delete']
    handle_mysql(s)
