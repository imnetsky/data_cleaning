# 南方基金

# yum 源搭建与补丁更新手册

![](images/fe654e54794eee79470556e6027ddfc927aae7cb0fba93f251dd8c414bddcd54.jpg)


redhat. 


文档版本信息


<table><tr><td>版本</td><td>作者</td><td>时间</td><td>备注</td></tr><tr><td>V1.0A01</td><td>冯宝兴</td><td>2019-10-25</td><td>创建文档</td></tr><tr><td>V1.0A02</td><td>邬灏</td><td>2021-12-06</td><td>修改配置</td></tr></table>

# 目 录

南方基金.. 

yum源搭建与补丁更新手册. 

# 环境简介... 3

# 二、 仓库下载.. 3

2.1． 注册到红帽官网. 3 

2.2． 订阅相关仓库.. 3 

# 三、 同步仓库到yum服务器.. /

# 四、 yum 服务器搭建 rsync 服务. /

# 五、 搭建 httpd 服务.. 5

5.1．安装 httpd 软件包.. 

5.2．设置开机启动.. 5 

5.3．添加软连接. 5 

5.4．启动 httpd... [ 

# 六、 安装 ansible.. 5

# 七、 纳管客户端服务器.

# 八、 批量配置 yum 源..

# 九、 检查勘误情况..

# 十、 批量升级补丁..

# 十一、 附录.. 8

附录一：playbook 案例库地址. .8 

附录二：目前可用yum源.. . 8 

附录三：ansible 的 playbook 结构. .8 

# 一、 环境简介

通过rhel6、rhel7各一台下载机接入到互联网，定时从红帽官网下载对应的补丁安装 包，再导出RPM源到指定目录，通过同步到YUM源（生产/测试/开发都可访问）服务 器，通过ansible剧本推送补丁。 

由于每个网络区域都是隔离的，为了减少网络链路开通，在每个网络区域设置一台代 理服务器。只需开通ansible到代理服务器的网络，ansible即可通过代理服务器管理该 网络区域的所有服务器。 


架构图如下：


![](images/03c849ac18d1e01a674b49a6eed7ef22914039ea2d3ebf90cc23faa8992fa559.jpg)


# 二、 仓库下载

# 2.1． 注册到红帽官网

登录下载机，进行注册。 

```txt
注册到官网  
# subscription-manager register  
正在注册到：subscription.rhsm.redhat.com:443/subscription  
用户名：  
密码：  
# 查看订阅状态  
# subscription-manager status 
```

# 2.2． 订阅相关仓库

根据需要，订阅对应的仓库，如无特别需求，可使用自动附加订阅。 

```txt
自动附加订阅  
# subscription-manager attach -auto  
# 查看订阅库  
# subscription-manager repos 
```

```powershell
查看开启的订阅仓库  
# subscription-manager repos -list-enabled  
# 开启仓库订阅（开启多个仓库，需要反复执行多次命令或使用*/？通配符）  
# subscription-manager repos --enable=rhel-7-server-rpms 
```

# 2.3． 下载仓库

在下载机中，使用 reposync 命令把官网仓库同步到本地。 

```txt
同步时间根据仓库的大小和带宽而异，本次rhel-7-server-rpms大概51G，20小时左右# reposync -m -g --plugins --download_path=/data/localrepo -r rhel-7-server-rpms 
```

同步仓库的脚本已经设置了定时任务，每月第一周周日凌晨1点会执行。 

脚本位置：/data/reposync-script.sh 

注：建议同步如下官方仓库 

```txt
rhel-7-server-rpms  
rhel-7-server-extras-rpms  
rhel-7-server optional-rpms  
rhel-server-rhscl-7-rpms  
rhel-7-server-ansible-2-rpms 
```

# 三、 同步仓库到 yum 服务器

通过下载机同步的仓库，需要集中同步到 yum服务器，才能提供给各环境的 redhat服 务器使用。 

在下载机中，root用户中设置crontab定时任务，设置每月第一周周日凌晨1点会执行。 

```shell
crontab -l
0 1 1-7 * 0 [ "$(date+%a)"=="Sun" ] && cd /data && nohup sh reposync-script.sh & 
```

# 四、 yum服务器搭建rsync服务

4.1．安装 rsync 软件包； 

```batch
yum install rsync -y 
```

4.2．配置/etc/rsyncd.conf 

```ini
log file = /var/log/rsync.log  
pidfile = /var/run/rsync.pid  
lock file = /var/run/rsync.lock  
motd file = /etc/rsyncd.motd  
port = 873  
[7Server]  
path = /data/localrepo/7Server/  
comment = rhel7 yum repository  
uid = root  
gid = root 
```

```ini
use chroot = no  
write only = true  
read only = false  
list = no  
max connections = 10  
timeout = 600  
host allow = 10.71.1.134  
[6Server]  
path = /data/localrepo/6Server/  
comment = rhel6 yum repository  
uid = root  
gid = root  
use chroot = no  
write only = true  
read only = false  
list = no  
max connections = 10  
timeout = 600  
host allow = 10.71.1.133 
```

# 4.3．设置开机启动

systemctl enabled rsyncd 

# 4.4．启动 rsyncd

systemctl start rsyncd 

# 五、 搭建 httpd 服务

# 5.1．安装 httpd 软件包

```txt
如未安装，先安装httpd yum install httpd mod_SSL -y 
```

# 5.2．设置开机启动

systemctl enabled httpd 

# 5.3．添加软连接

```txt
分别做软连接到/var/www/html/下  
# In -s /data/localrepo/7Sserver 7Server  
# In -s /data/localrepo/6Sserver 6Server 
```

# 5.4．启动 httpd

# systemctl start httpd 

# 六、 安装 ansible

6.1．上传 ansible-tower-setup-bundle-3.5.3-1.el7.tar.gz 到 ansible 服务器； 

6.2．解压压缩包； 

```txt
tar -xzfansible-tower-setup-bundle-3.5.3-1.el7.tar.gz 
```

6.3．进入目录 

```txt
cdansible-tower-setup-bundle-3.5.3-1.el7/bundle/repos/ansible-tower-dependencies/ 
```

6.4．安装 ansible 

```txt
yum localinstallansible 
```

6.5．配置/etc/ansible.cfg 

```txt
Vim /etc/ansible.cfg 
```

```txt
去掉此行注释，ansible连接时会忽略首次连接的提示 
```

```txt
host_keychecking = False 
```

# 6.6. 启动防火墙

```txt
#开机启动防火墙 
```

```txt
Systemctl enabled firewalld 
```

```txt
#启动防火墙 
```

```txt
Systemctl start firewalld 
```

# 6.7．配置防火墙规则

```txt
指定堡垒机可以访问ansible服务器 
```

```txt
Firewall-cmd -add-rich-rule="rule family=ipv4 source address=10.71.9.120 port port=22 protocol=tcp accept" - permanent 
```

```txt
Firewall-cmd -add-rich-rule="rule family=ipv4 source address=10.71.9.121 port port=22 protocol=tcp accept" -- permanent 
```

```txt
Firewall-cmd -add-rich-rule="rule family=ipv4 source address=10.71.9.122 port port=22 protocol=tcp accept" -- permanent 
```

```batch
Firewall-cmd -remove-service=ssh -permanent 
```

```txt
配置ansible可以访问指定代理机22端口 
```

```batch
Firewall-cmd -permanent -direct -add-rule ipv4 filter OUTPUT 0 -p tcp -d 10.70.13.243 -dport 22 -j ACCEPT .... 
```

```txt
Firewall-cmd -permanent -direct -add-rule ipv4 filter OUTPUT 0 -p tcp -dport 22 -j DROP #这个要最后执行 
```

注意： 

设置防火墙的规则要注意顺序，不然规则生效顺序会不同。 

# 七、 纳管客户端服务器

由于ansible服务器与客户端网络不能直连，需要通过代理，所以需要先设置 ansible 到代理服务器的互信。 

7.1．生成密钥对 

```txt
生成密钥对 
```

```txt
ssh-keygen 
```

7.2．设置与代理机互信 

```txt
ssh-copy-id patrol@10.71.20.243 
```

7.3．设置主机清单 

```txt
#把需要纳管的服务器添加到主机清单中  
#test client  
[test-group]  
10.71.23.152  
10.71.21.54  
[all:vars]  
#该行参数指定代理服务器  
ansible_ssh_common_args=-o ProxyCommand="ssh -W %h:%p -q patrol@10.71.20.243" 
```

# 7.4．批量互信纳管

批量互信纳管 playbook 代码如下，保存为 set-authorized.yml： 

```yaml
---   
- hosts: all   
gather_facts: false   
remote_user: patrol   
tasks:   
- name: set authorized key taken from file   
authorized_key:   
user: patrol   
state: present   
key:"{\{lookup('file','/root/.ssh/id_rsa.pub')\}" 
```

在 ansible 服务器中执行 playbook，如下： 

```txt
#ansible-playbook -i two-inventory set-authorized.yml -k
#第一次执行需要提供patrol密码 
```

# 八、 批量配置 yum 源

8.1．登录 ansible 服务器； 

8.2．执行配置 yum 源 playbook； 

```txt
为客户端配置yum源  
ansible-playbook -i two-inventory yum-config.yml 
```

执行结果： 

![](images/7e6ad727b0b9be9b728eb1f41a58547228faec87548ab882bc97c4a2c9562936.jpg)


附言：由于本环境两台机已经执行过，所以都是绿色，即没有对客户机修改。 

# 九、 检查勘误情况

9.1．登录 ansible 服务器； 

9.2．根据需要检查的补丁编号，设置 CVENUM、ADVISORYNUM 变量； 

9.3．检查系统补丁的 playbook 有四个标签，分别是： 

默认只检查服务器的 updateinfo 信息概括； 

alladvisory：列出服务器中所有 advisory 的列表，默认不执行； 

allcve：列出服务器中所有 cve 的列别，默认不执行； 

advisory：检查指定 advisory 是否存在于服务器中，默认不执行； 

cve：检查指定 cve 是否存在于服务器中，默认不执行； 

# 9.4．执行 playbook

```shell
使用-e指定需要检查的cve号和advisory号  
#ansible-playbook -i two-inventory yum-check.yml -e "CVENUM=CVE-2018-14526" -e "ADVISORYNUM=RHBA-2018:1903"  
#使用一tags指定需要执行的标签，即升级行为  
#ansible-playbook -i two-inventory yum-patch.yml --tags allcve 
```

# 十、 批量升级补丁

10.1．登录 ansible 服务器； 

10.2．根据需要升级的补丁编号，设置 CVENUM、ADVISORYNUM 变量； 

10.3．升级补丁的playbook有五个标签，分别是： 

min-sec-update：升级具有安全勘误表的包(升级到最后一个安全勘误表包)，默认不执 行 

min-update：仅更新到修复影响系统的版本，默认不执行 

all-update：更新到可用最新版本，默认不执行 

cve-update：更新指定CVE号的版本，默认执行 

advisory-update：更新指定 RHSA 号的版本，默认执行 

10.4．执行 playbook 

# 使用-e 指定需要打补丁的 cve 号和 advisory 号 

#ansible-playbook -i two-inventory yum-patch.yml -e "CVENUM=CVE-2018-14526" -e "ADVISORYNUM=RHBA-2018:1903" 

# 使用—tags 指定需要执行的标签，即升级行为 

# ansible-playbook -i two-inventory yum-patch.yml --tags min-sec-update 

# 十一、 附录

附录一：playbook 案例库地址 

https://galaxy.ansible.com/ 

附录二：目前可用 yum 源 

其中 10.255.197.10 是 yum 源服务器，需要在 hosts 中配置： 

https:// 10.255.197.10/7Server/rhel-7-server-rpms 

https:// 10.255.197.10/6Server/rhel-6-server-rpms 

附录三：ansible 的 playbook 结构 

/root/yum-patch/ 

![](images/853f6028fdacdcce11e60127d17b2c0723f9b290fab3bd95d601eef456872203.jpg)


│ ── yum-config ├ #配置yum源的角色目录 

│ │ ── tasks├ #tasks 目录 

![](images/ec63ac8c968040f12b04bc069ff7a844aba39c256c010d538d5f26f85aac6275.jpg)


│ └── yum-patch #打补丁的角色目录 

![](images/0639a00da8c7111ed4ea5b3146577830b123b9becba2ca8b68f309753e86a223.jpg)


![](images/66178ebd359adfe176775f4e4d342c8eccaa1af80e8e5b887e2154f4f402448c.jpg)


├── set-authorized.yml #设置互信的 playbook 脚本 

├── two-inventory #主机清单 

├── yum-check.yml #调用勘误检查角色的 playbook 

├── yum-config.yml #调用配置 yuan 源角色的 playbook 

└── yum-patch.yml #调用为系统打补丁角色的playbook 