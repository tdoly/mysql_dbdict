##msyql数据库数据字典导出

* 在client.py中配置数据库链接，及要忽略的库
* 运行export_excel.py

##依赖包

* MySQLdb
* xlrd
* xlwt
* xlutils

##依赖包安装

ubuntu为例
```terminal
sudo apt-get install python-mysqldb

pip install xlrd

pip install xlwt

pip install xlutils

```

##2014.2.23更新日志

* 使用了zerorpc
* 使用了tornado

```terminal

pip install zerorpc
pip install tornado

```
![demo image](/static/images/demo.png "the demo image")
