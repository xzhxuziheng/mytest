# 文件使用说明
    1、用例yaml文件
        1）传参方式为列表字典
        2）在接口自动化中必含num、name、url、method、data、asserts、depends
        num为用例编号
        method值为get、post、put、patch、delete
        若depends为n，则无后续key
        若depends为y，则后续key必含depends_site、depends_type、depends_key、depends_value
        depends_site：依赖字段添加位置，url、body
                      注：get、delete请求不填value
        depends_type：依赖字段添加类型（str、list）
                      依赖中key-value中value类型为str，则depends_type值为str
                      依赖中key-value中value类型为list，则depends_type值为list
        depends_key：需要添加的key值
        depends_value：格式为1-2.data.list.0.merchantNo，
                       1-2代表用例编号为1-2的接口返回的所有数据，
                       data代表取接口返回参数中的data值，
                       后面以此类推
        所有的key对应的value可以为空
    2、dependCase.yaml文件为全局依赖
    3、mysql.yaml为用例执行前的sql操作
    4、response.yaml保存所有接口返回参数
 