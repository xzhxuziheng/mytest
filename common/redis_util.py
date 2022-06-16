import redis
from common import yaml_util
import requests


yaml_data = yaml_util.read_yaml('/baseconfig.yaml')
host = yaml_data['redis_host']
port = yaml_data['redis_port']
db = yaml_data['redis_db']
password = yaml_data['redis_password']


def get_redis_data(redis_key):
    # 实现一个连接池
    pool = redis.ConnectionPool(
        host=host,
        port=port,
        db=db,
        password=password,
        decode_responses=True
    )
    conn = redis.Redis(connection_pool=pool)
    data = conn.get(redis_key)
    return data


if __name__ == '__main__':
    redisKey = 'user:cache:login:1525_1'
    print(get_redis_data(redisKey))
    header = {
        'token': get_redis_data(redisKey),
        'source_type': '1',
        'content-type': 'application/json'
    }
    url = 'https://test.bike.ledear.cn/api/order/user/ride/list?page=1'
    res = requests.get(url=url, headers=header)
    print(res.json())
