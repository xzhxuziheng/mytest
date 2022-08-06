# 文件使用说明
    1、用例yaml文件
        1）传参方式为列表字典
        2）在接口自动化中必含num、name、execute、token_source、url、method、data、asserts、depends
        num为用例编号
        execute用例是否执行（y为执行，n为不执行）
        token_source token来源
                     admin：web平台端
                     operator：web运营商端
                     merchant_app：商户端app
                     factory_wx_mini：厂测微信小程序
                     user_wx_mini：用户端微信小程序
        method值为get、post、put、patch、delete
        若depends为n，则无后续key
        若depends为y，则后续key必含depends_site、depends_type、depends_key、depends_value
        depends_site：依赖字段添加位置，url、body、url_and_body
                      注：get、delete请求不填value
        depends_type：依赖字段添加类型（str、list）
                      依赖中key-value中value类型为str，则depends_type值为str
                      依赖中key-value中value类型为list，则depends_type值为list
        depends_key：需要添加的key值
        depends_value：格式为1-2.data.list.0.merchantNo，
                       1-2代表用例编号为1-2的接口返回的所有数据，
                       data代表取接口返回参数中的data值，
                       后面以此类推
        若depends_site: url_and_body
                       则需添加后续参数
                       depends_url_key
                       depends_url_value
                       depends_body_key
                       depends_body_value
        所有的key对应的value可以为空
    2、dependCase.yaml文件为全局依赖
    3、mysql.yaml为用例执行前的sql操作
    4、response.yaml保存所有接口返回参数
    5、baseconfig.yaml为全局配置
        1）域名配置
        2）header配置
        3）日志等级配置
        4）项目接口自动化执行yaml文件配置
        5）数据库配置
        6）redis配置
 