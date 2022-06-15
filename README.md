# mytest
1、用例yaml文件
  1）传参方式为列表字典
  2）在接口自动化中必含name、url、method、data、asserts、depends
  若depends为n，则无后续key
  若depends为y，则后续key必含depends_site、depends_key、depends_value
  depends_site：依赖字段添加位置，url、body
  depends_key：需要添加的key值
  depends_value：格式为1.data.list.0.merchantNo，1代表第二个接口返回的所有数据，data代表取第二个接口返回参数中的data值，后面以此类推
2、dependCase.yaml文件为全局依赖
3、mysql.yaml为用例执行前的sql操作
4、response.yaml保存所有接口返回参数
