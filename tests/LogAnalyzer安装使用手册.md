<table><tr><td>编号</td><td></td></tr><tr><td>密级</td><td></td></tr></table>

# LogAnalyzer 安装使用手册

——VER 1.0

红帽全球专业服务

文档说明  

<table><tr><td colspan="2">文档名称</td><td colspan="3">LogAnalyzer 安装使用手册</td></tr><tr><td colspan="2">内容描述</td><td colspan="3"></td></tr><tr><td colspan="5">修订历史</td></tr><tr><td>日期</td><td>版本</td><td>修订者</td><td>修订说明</td><td>评审人员</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>

# 目 录

1. 下载 LOGANALYZER..  
2. 安装必要的软件包..   
3. 设置 RSYSLOG MYSQL...   
4. 安装 LOGANALYZER..  
5. 报表功能..

# LogAnalyzer 安装使用手册

# 1. 下载 LogAnalyzer

wget http://download.adiscon.com/loganalyzer/loganalyzer-4.1.5.tar.gz

# 2. 安装必要的软件包

[root@test ~]# yum install httpd

[root@test ~]# yum install php*

# 3. 设置 rsyslog mysql

RHEL6 主机做如下设置.

[root@test ~]# setenforce 0

[root@test ~]# service iptables stop

[root@test ~]# service httpd start

[root@test ~]# yum -y install mysql-server rsyslog-mysql mysql

[root@test ~]# service mysqld restart

[root@test ~]# chkconfig mysqld on

[root@test ~]# cd /usr/share/doc/rsyslog-mysql-5.8.10/

[root@test rsyslog-mysql-5.8.10]# mysql <createDB.sql

[root@test rsyslog-mysql-5.8.10]#

[root@test rsyslog-mysql-5.8.10]# mysql

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 3

Server version: 5.1.73 Source distribution

Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its affiliates. Other names may be trademarks of their respective owners.

Type 'help;' or '\h' for help. Type $" \backslash \mathsf { C } ^ { \prime }$ to clear the current input statement.

```txt
mysql> show databases;  
+--------+  
| Database |  
+--------+  
| information_schema |  
| Syslog |  
| mysql |  
| test |  
+--------+  
4 rows in set (0.00 sec) 
```

```txt
mysql> use Syslog;  
Reading table information for completion of table and column names  
You can turn off this feature to get a quicker startup with -A 
```

```txt
Database changed  
mysql> grant all on Syslog.* to 'syslogroot'@'192.168.122.56' identified by 'syslogpass';  
Query OK, 0 rows affected (0.00 sec) 
```

```txt
mysql> flush privileges;  
Query OK, 0 rows affected (0.00 sec) 
```

# rsyslog 做如下设置

```txt
修改/etc/ryslog.conf, 打开如下选项.
$ModLoad imuxsock
$ModLoad imklog
$ModLoad imudp #加载 udp 的模块
$UDPServerRun 514 #允许接收 udp 514 的端口传来的日志
$ModLoad imtcp #加载 tcp 的模块
$InputTCPServerRun 514 #允许接收 tcp 514 的端口传来的日志
$ModLoad ommmysql #加载 mysql 的模块
...
*.:*:ommmysql:192.168.122.56,Syslog,syslogroot,syslogpass #将日志写入
```

mysql

# 4. 安装 LogAnalyzer

 解压 LogAnalyzer 安装包, 拷贝 src 文件夹至 http 文件夹, 并配置安装程序

```txt
[root@test ~]# cd loganalyzer-4.1.5  
[root@test loganalyzer-4.1.5]# ls  
ChangeLog contrib COPYING doc INSTALL src  
[root@test loganalyzer-4.1.5]# cp -ap src/* /var/www/html/log/  
[root@test loganalyzer-4.1.5]# cp contrib/* /var/www/html/log/  
[root@test loganalyzer-4.1.5]# cd /var/www/html/log/  
[root@test log]# chmod +x configure.sh  
[root@test log]# ./configure.sh 
```

浏览器打开安装界面

![](images/43ddffd32ee69f83ad49f506036e8d4810086a1142caaef326db1c3312525097.jpg)

![](images/4317b4078ae4794ee4624d0b6cb67ce0b5a69bc9f7b127d4dc4ac237af9b93e3.jpg)

192.168.122.56/log/

![](images/4ebbccad061fa7dac792b511a3f1f8b5c92480784f7572164ac85a00d473683a.jpg)

创建数据库

```perl
mysql> create database loganalyzer;  
mysql> grant all on loganalyzer.* to lyzeruser@'192.168.122.56' identified by 'lyzeruser';  
mysql> flush privileges; 
```

设置连接

# Step 3 - Basic Configuration

In this step, you configure the basic configurations for LogAnalyzer.

![](images/23ce821056b3c35e79f574da3b23d8c770d415a552393381e49d3e355d7ead6d.jpg)

InstallProgress:

Next

# 创建管理员账号与密码admin/admin

# Step 6 - Creating the Main Useraccount

You are now about to create the initial LogAnalyzer User Account.

This willbethefirstadministrativeuserwhichwillbeneededtologinintoLogAnalyzerandaccesstheAdminCenter!

![](images/97ceb794af02857c085966b774cd246b9f4c424f8c736d7e428448adee45740e.jpg)

Install Progress:

Next

# 设置数据源

![](images/5df261cacd82673564dce109ac650d7a9ff4af21ba78d223e192941117fca911.jpg)

# 监控主界面如下

![](images/0f3cc00b9627fe6b18eadd4e856042a99d1aae3ed8d97ec4395560c2b40630b3.jpg)

# 5. 报表功能

配置报表, 用 admin 登录，进入’Admin Center’ ‘Report Module’.

![](images/a97beedd58375467d6ca7d5f1cc7e609d8c0b2835251cf11e5eed2be4fb53e79.jpg)

配置 syslogsummary.

ReportModules

![](images/871489783e907c65a53aba184868fb64dd48814e8895a382f2aa9eb6afc25e0a.jpg)

# 生成html 报表

![](images/e57481564525e9aa821e9d0242e100370dc8985e9aea0cee840fc3dd7b6c5ee3.jpg)

![](images/1ec1f9044f214a3d594731774d9bbc820676765d2353f3b5119d8f09913af9fe.jpg)

![](images/d7a8b88ef69f5c0a429a644cb6d2507447964b8989cc83f24f3cbf50d9036f78.jpg)

rhel6-repo

Syslogmessagesconsolidated per Host

![](images/9608a52dd3335513b3b04f507a784c2ac54d0e6db935268064bea671fe42ed47.jpg)

# 生成pdf 报表

![](images/5b4b714bbc7a5fc393217d8ab3e058fc3fa29fc6337a2d87e5cc637f11447244.jpg)