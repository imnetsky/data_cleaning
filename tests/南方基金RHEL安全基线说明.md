# 南方基金

2019 版

# 文档属性

<table><tr><td colspan="6">修订历史 2021年12月</td></tr><tr><td>编号</td><td>日期</td><td>修订描述</td><td>版本</td><td>作者</td><td>审核</td></tr><tr><td>1</td><td>2019-11-04</td><td>根据最新情况修订</td><td>V1.0</td><td>冯宝兴</td><td></td></tr><tr><td>2</td><td>2021-12-07</td><td>根据最新情况修订</td><td>V1.1</td><td>郭灏</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# 目录

1 文档说明..

1.1 文档简介..   
1.2 适用对象..   
1.3 生效范围..

2 系统安装.. 8

2.1 版本选择.. . 8  
2.2 安装参数.. . 8  
2.3 手动安装.. .10   
2.4 自动安装.. .10   
2.5 虚拟机安装.. . 15   
2.6 修改初始密码.. . 15   
2.7 配置 YUM 源.. .15

2.7.1 配置YUM源文件. .15  
2.7.2 检查 YUM 源是否可用. .16  
2.7.3 配置本地YUM源.. . 17   
2.8 安装常用软件.. . 18

3 网络配置.. . 19

3.1 主机名配置. . 19   
3.1.1 主机名命名规范.. .19  
3.1.2 修改主机名.. .19   
3.1.3 主机文件编写规范.. . 20  
3.2 网卡配置. .20   
3.2.1 物理机配置.. .21   
3.2.2 虚拟机配置.. .22   
3.2.3 路由配置. .23   
3.2.4 内核配置. .23

4 存储配置. . 26

4.1 本地磁盘管理. . 26  
4.2 卷组规范.. .27   
4.3 文件系统格式.. . 27  
4.4 多路径软件.. . 27  
4.5 NFS挂载选项规范. .30

5 服务配置： . 31

# 6 安全加固.. . 34

5.1 NTP 服务.. . 31  
6.1 服务的配置. . 34  
6.2 SELINUX 服务.. 35  
6.3 设置服务器登录公告板. .35  
6.4 命令时间戳记录与命令行提示符.. .36  
6.5 ulimit 设置.. .38   
6.6 文件系统挂载选择设置. .39  
6.7 系统敏感文件权限设置. .39  
6.8 日志审计策略配置. .39  
6.9 kdump 配置.. . 42  
6.10 系统内核参数配置. ..43   
6.11 crontab 配置. . 44  
6.12 物理安全设置.. . 44  
6.13 口令策略设置.. . 45   
6.14 UID 0 用户设置.. .46  
6.15 系统登录安全设置. .47

6.16 系统全局 PROFILE 安全设置. .47  
6.17 网络客户端 IP 建议.. .48  
6.18 CRON 授权规定（建议） . 48   
6.19 删除 rhost 相关高风险文件.. .48  
6.20 SSHD 配置.. .48  
6.21 SFTP 服务加固策略. .50  
6.22 系统日志转发策略. .51   
6.23 账户安全... .54  
6.24 补丁安装规范. . 55

# 7 通用操作.. . 57

7.1 日常巡检.. .57

7.1.1 内存管理. .57  
7.1.2 CPU 使用率.. . 59  
7.1.3 磁盘管理. .61  
7.1.4 系统负载. . 63  
7.1.5 网络.. .. 64  
7.1.6 系统运行时间.. .. 66

7.2 逻辑卷管理. . 67

7.2.1 基本术语.. ..67  
7.2.2 命令描述.. ..68  
7.2.3 配置 LVM.. . 69   
7.2.4 创建分区.. ..69  
7.2.5 创建 PV... . 70  
7.2.6 创建 VG.. . 70  
7.2.7 扩展 VG... . 70  
7.2.8 创建 LV... . 71  
7.2.9 扩展 LV... . 71  
7.2.10 创建文件系统.. .71  
7.2.11 扩展文件系统.. . 72

7.3 系统服务配置. 72

7.3.1 rsync... . 72   
7.3.2 NFS... . 88   
7.3.3 autofs.. . 92   
7.3.4 logrotate.. ..95   
7.3.5 vsftp... . 112   
7.3.6 SAMBA... . 130

7.3.7 VNC.. .. 161   
7.3.8 sftp... .. 172

# 1 文档说明

# 1.1 文档简介

本规范为 Red Hat Enterprise Linux(RHEL)操作系统的管理规范，包括系统安装标准、服务配置标准、安全加固标准、存储管理和日常巡检。

# 1.2 适用对象

本文档适用于全行 Linux 服务器系统管理员。

# 1.3 生效范围

自本版规范正式下发之日起，新安装的 Red Hat Enterprise Linux(RHEL)服务器必须遵照配置执行。

除明确注明“新安装操作系统”的配置项外，已安装的Linux服务器,应按照本版规范进行配置调整。

配置项中，包含“必须”的，必须遵照执行；包含“应/不应”的，除特殊原因外需遵照执行；包含“建议”的，可根据实际情况执行，不做强制要求。

由于特殊原因而无法遵照执行的，应该及时报备。

# 2.1 版本选择

根据应用的要求，并结合硬件类型，选择适当的操作系统版本。

至本规范最后更新时，新安装操作系统允许使用的版本如下：

1) RedHat Enterprise Linux Server 6.10   
2) RedHat Enterprise Linux Server 7.9

如无特殊要求，建议使用 RedHat Enterprise Linux Server 6.10 与 RedHat EnterpriseLinux Server 7.9。为便于管理，不建议安装 SUSE 等其他厂商的 Linux 操作系统，若由于特殊要求，必须安装其他厂商的 Linux 操作系统，应及时报备，审批通过后方可安装，且应按照本配置规范要求进行配置。

# 2.2 安装参数

本章节主要描述安装过程中的各项参数设置，该要求同时适用于手工安装和kickstart自动安装。

引导系统提示：选择“Installation”，正常安装系统

语言选择: 选择 EngLish

键盘布局：选择 U.S. English

设置系统主机名：请参考章节3.1中的“主机命名规范”进行系统主机名的设置

时区选择:统一选择“Asia/Shanghai”，系统时钟使用 UTC 时间

root账户密码：密码复杂性配置要求，请参考章节6.13中的“口令策略设置”

分区划分：请参考章节4.1中的“本地磁盘管理”

文件系统：rhel6 使用 EXT4，rhel7 使用 XFS

软件包选择： 操作系统安装的初始软件包选择建议如下

<table><tr><td>软件包名称</td><td>必须/可选</td><td>软件包说明</td></tr><tr><td>RHEL6: Base</td><td>必须</td><td>操作系统基础包</td></tr><tr><td>RHEL7: Minimal</td><td></td><td></td></tr><tr><td>Compatibility libraries(组)</td><td>可选</td><td>操作系统兼容性库包，提供对老版本软件的支持</td></tr><tr><td>Hardware monitoring utilities(组)</td><td>可选</td><td>硬件监控工具，提升系统定位能力</td></tr><tr><td>Large Systems Performance(组)</td><td>可选</td><td>大型系统工具集包，提供cgroup等管理工具</td></tr><tr><td>Legacy UNIX compatibility(组)</td><td>可选</td><td>UNIX兼容性包（RHEL6）</td></tr><tr><td>Performance Tools(组)</td><td>可选</td><td>性能定位和监控工具，及时了解系统瓶颈</td></tr><tr><td>nc（RHEL6）</td><td>必须</td><td>网络工具</td></tr><tr><td>nmap-ncat (RHEL7)</td><td>必须</td><td>Nc替代工具包</td></tr><tr><td>telnet</td><td>必须</td><td>telnet客户端，环境维护管理员使用（建议）</td></tr><tr><td>bash-completion (RHEL7)</td><td>必须</td><td>Tab键自动补全</td></tr><tr><td>vim-enhanced</td><td>必须</td><td>Vim编辑工具</td></tr><tr><td>chrony (RHEL7)</td><td>必须</td><td>时间同步服务</td></tr><tr><td>ntpdate</td><td>必须</td><td>时间同步工具</td></tr><tr><td>yum-plugin-security (RHEL6)</td><td>必须</td><td>Yum插件</td></tr></table>

备注：软件包安装建议采用上述的最小安装方式，gcc/make等开发编译工具如非特殊需要，不应在生产系统中安装。若因生产需要，需要安装额外组件，请按第6.23章“补丁安装规范”中说明，从规定的yum源服务器获取，不得通过其他途径安装。

# 物理机分区划分规范：

除/boot 分区不能采用 LVM 外，其他所有分区都应采用 LVM 管理磁盘，另外应用程序如果使用 LVM 来管理,需要创建单独的 VG,文件系统可按照下表来设置逻辑卷名称及相应空间(这里列出的为最低空间要求)：

<table><tr><td>Mount Point</td><td>LV命名</td><td>最低配置(GB)</td><td>备注</td></tr><tr><td>/boot</td><td></td><td>1024M</td><td>必须是分区</td></tr><tr><td>/</td><td>/dev/mapper/rootvg-lv_root</td><td>300G</td><td></td></tr><tr><td>swap</td><td>/dev/mapper/rootvg-lv_swap</td><td>16G</td><td></td></tr></table>

注：上述分区方案只用了RAID1操作系统硬盘，对于数据磁盘，需要根据应用情况进行规划。

对于内存大于 50G 的机器，/dev/mapper/rootvg-lv_root 需要在业务上线前手工触发

kernel panic 来检测大小是否适用。

# 虚拟机分区划分规范：

除/boot 分区不能采用 LVM 外，其他所有分区都应采用 LVM 管理磁盘，文件系统可按照下表来设置逻辑卷名称及相应空间(这里列出的为最低空间要求)：

<table><tr><td>Mount Point</td><td>LV命名</td><td>最低配置(GB)</td><td>备注</td></tr><tr><td>/boot</td><td></td><td>1024M</td><td>必须是分区</td></tr><tr><td>/</td><td>/dev/mapper/Rootvg-lv_root</td><td>90G</td><td></td></tr><tr><td>swap</td><td>/dev/mapper/Rootvg-lv_swap</td><td>8G/16G</td><td></td></tr></table>

# swap 的大小按照如下规则：

内存小于等于 2G，swap 为内存的 3 倍  
内存大于 2G，小于等于 8G，swap 为内存的 2 倍  
内存大于 8G，swap 大小为 16G（MAX）

如果有应用对于 swap 又特殊要求，按照应用的要求划分。

# 2.3 手动安装

根据上述安装参数，手动安装系统。

# 2.4 自动安装

kickstart 可引导完成自动安装

1）将包含自动安装 kickstart 脚本的 ISO 光盘文件（bak_rhel-server-  
6.10_x86_64_auto.iso）上传至可以使用远程管理口连接服务器的 PC 机上。  
2）使用远程管理口连接至服务器，打开控制台，通过控制台将本地 ISO 光盘文件

（bak_rhel-server-6.10_x86_64_auto.iso）挂载至服务器，重启服务器。

3）重启服务器时进入BIOS将首选启动项设置为CD-ROM，然后再重启服务器，若服务器是一台裸机，此步骤可省略。  
4）重启服务器后，会自动加载ISO光盘文件，进入引导界面，在规定时间内此界面若无操作将自动使用默认菜单引导，下图默认菜单为第一项“Install or upgrade an existingsystem”。

Welcome to Red Hat Enterprise Linux6.4!

Install or upgrade an existing system

Install system with basic uideo driuer

Rescue installed system

Boot from local drive

Memory test

Press [Tab] to edit options

Automatic boot in 3 seconds...

# RED HAT

# ENTERPRISE LINUX 6

![](images/9f828f2abdc062da5bebde1ba7e77e2d3d1d32e2a90e26835fe4cb531cbe3251.jpg)

Copyright 2oo3-2o1o Red Hat, Inc.and others.All rights reserved.

5）使用↑↓键可以选择菜单，在选中的菜单上按Tab键可以查看此菜单的引导参数，下图为

第一项菜单的引导参数，其中 ks=cdrom:/isolinux/ks.cfg 指定的是 kickstart 自动安装脚本的

路径。

Welcome to Red Hat Enterprise Linux6.4!

Install or upgrade an existing system Install systemwith basicuideo driver Rescue installed system Boot from local drive Memory test

>umlinuz ks=cdrom:/isolinux/ks.cfg initrd=initrd.img_

# RED HAT ENTERPRISE LINUX 6

Copyright@ 2oo3-2o1o Red Hat Inc.and others.All rights reserved.

![](images/933c46febc311c5bbc99dd2445a59e9bca2aa5688e11dba5eb1f8820d6038f2f.jpg)

6）按 Esc 键返回菜单选择界面，选择第一项“Install or upgrade an existing system”，按

回车键，进入自动安装界面。

Welcome to Red Hat Enterprise Linux6.4!

Install or upgrade an existing system

Install system with basic uideo driuer

Rescue installed system

Boot from local drive

Memory test

Press [Tab] to edit options

# RED HAT?

# ENTERPRISE LINUX 6

![](images/d04a1f10d7bb215820f80106f0e4594f95e3f22e0cb7876bdf110b2d375780da.jpg)

Copyright 2oo3-2o1o Red Hat, Inc.and others.All rights reserved.

7）自动安装界面，进入此界面之前无需任何的人工操作。

![](images/9bbe806639417a5b5cf26fb80123e982b92769f674482ce274cede703cb36963.jpg)

8）安装完成后，系统将自动重启，并进入登陆界面，如下图：

![](images/acb57ca94ad47a0ea6049413f20eebce6bc4f2627f818073879faaebee4fab4c.jpg)

# 2.5 虚拟机安装

虚拟机若无特殊要求，请VMware管理员使用模板克隆，如有特殊要求，请参照手工安

装步骤，根据需要修改相应的参数设置。

# 2.6 修改初始密码

使用kickstart自动安装和虚拟机模板克隆的新系统，root用户都有一个初始密码，为了

保证系统的安全性，建议系统管理员及时修改 root 用户密码。密码复杂度请参考口令复杂度

规定。

修改超级用户密码

```txt
#passwd root Changing password for user root. New password: Retype new password: passwd: all authentication tokens updated successfully. 
```

修改普通用户密码

```txt
#passwd user Changing password for user user. New password: Retype new password: passwd: all authentication tokens updated successfully. 
```

# 2.7 配置 YUM 源

目前 RedHat 的 YUM 源服务器地址均为 10.255.197.10，所有的 Linux 服务器都应从该

YUM 源服务器中下载安装软件及补丁程序。

# 2.7.1 配置 YUM 源文件

下载YUM配置文件之前，请确定网络配置成功，并且能够正常访问YUM服务器的80端

口，操作方法如下：

在/etc/yum.repos.d/目录下创建 repo 文件 rhel-6-server-rpms.repo

YUM 配置文件内容

[root@test ~]# cat /etc/yum.repos.d/rhel-6-server-rpms.repo

[rhel-6-server-rpms]

#YUM 源 ID

name $=$ rhel-6-server-rpms

#YUM源名称

baseurl=http://10.255.197.10/6Server/ rhel-6-server-rpms #YUM 源地址

enabled=1

#YUM源开关，1为开

gpgcheck=0

#gpgkey 检查开关，1 为开

# 2.7.2 检查 YUM 源是否可用

[root@test ~]# yum clean all

#清除缓存

Loaded plugins: product-id, security, subscription-manager

This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.

Cleaning repos:

Cleaning up Everything

[root@test ~]# yum repolist

#列出YUM源

Loaded plugins: product-id, security, subscription-manager

This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.

rhel-6-server-rpms

| 3.9 kB 00:00

rhel-6-server-rpms /primary_db

| 3.1 MB 00:00

repo id

repo name

status

rhel-6-server-rpms

rhel-6-server-rpms

3,648

repolist: 3,648

可以看到当前一共有一个可用的 YUM 源：rhel-6-server-rpms，每个 YUM 源的 status 下都有一些数字，该数字表示对应YUM源中的软件包的数量，最后一行为所有YUM源包含的软件包的总数。

# 2.7.3 配置本地 YUM 源

如果网络不可用，或者需要从 ISO 镜像安装软件，可以配置本地 YUM 源

```shell
# mount -o loop /dev/sr0 /mnt
# cat /etc/yum.repos.d/dvd(repo
[rhel-dvd]
name=rhel_dvd
baseurl=file:///mnt
enabled=1
gpgcheck=0
# yum repolist
Loaded plugins: product-id, security, subscription-manager
This system is not registered to Red Hat Subscription Management. You can
use subscription-manager to register.
rhel-dvd | 3.9 kB 00:00
...
rhel-dvd/primary_db | 3.1 MB 00:00
...
repo id repo name
status 
```

```txt
rhel-dvd rhel_dvd 3,690 repolist:3,690 
```

# 2.8 安装常用软件

若系统是使用Kickstart自动安装或者是使用虚拟机模板创建的，默认已经安装了常用的

客户端软件，此步骤可跳过，若系统是手工安装，则需要继续手工安装常用客户端软件。安

装前确认网络和 YUM 源已经配置成功。

# 安装方法如下：

```txt
# 以rhel7.6为例，如下：  
# yum install -y telnet nmap-ncat bash-completion vim-enhanced chrony ntpdate  
# rpm -q telnet nmap-ncat bash-completion vim-enhanced chrony ntpdate  
package telnet is not installed  
package nc is not installed  
package bash-completion is not installed  
vim-enhanced-7.4.629-5.el6.x86_64  
package chrony is not installed  
ntpdate-4.2.6p5-10.el6.x86_64 
```

默认情况下，在配置网络IP地址时，禁用IPV6功能。若业务环境需要开启IPV6功能，再根据具体业务的使用情况启用IPV6功能。

# 3.1 主机名配置

# 3.1.1 主机名命名规范

设置主机名时应遵循下述规则：

主机名只能包含小写英文字母、数字和连字符(-)，最长不得超过64个半角字符，最短建议不少于5个半角字符；  
对于一般服务器，主机名构成为：所属系统{2-4}功能{2-6}[-(连字符)]序号{2-4}[v]物理位置{2}。

“所属系统”为该服务器所属系统的英文名称缩写，长度为2-4位的英文字母或数字，缩写应登记备案，例如，tp(手机平台)、wp(网上应用)、dw（数据仓库）等等；

“功能”为该服务器的功能描述，长度为 2-6 为的英文字母或数字，例如，app(应用服务器)、web（web 服务器）、db（数据库服务器）等等；

在总长度不超过 15 个半角字符的前提下，可采用连字符分隔增加易读性；

“序号”为相同系统和功能的计算机标识，长度为2-4位的字母或数字，例如，1N、F2等等；

在满足总长度不超过 15 个半角字符的前提下，可用字母 v 标识虚拟机；

“物理位置”为该服务器所在地址位置标识，长度为 2 位的英文字母或数字，如sz、sh、bj 分别标识深圳、上海、北京。

# 3.1.2修改主机名

RHEL6 编辑文件/etc/sysconfig/network，修改 HOSTNAME 字段值，重启生效。

```shell
# cat /etc/sysconfig/network
NETWORKING=yes
HOSTNAME=rhel64
# hostname rhel64 
```

RHEL7命令行修改直接生效，不需要重启。

```txt
# hostnamectl set-hostname rhel74
# hostname
rhel74 
```

# 3.1.3主机文件编写规范

在/etc/hosts原文件的基础上新增主机条目(切记不可修改localhost条目)，格式为：

```txt
<IP><全主机名><别名>
```

例如：

```batch
echo " x.x.x.x test.example.com test" >> /etc/hosts 
```

# 3.2 网卡配置

# DNS信息：

外网环境:

深圳: DNS1 : 10.71.8.1

DNS2 : 10.71.8.2

内网环境:

深圳: DNS1 : 10.81.4.1

DNS2 : 10.81.4.2

物理机网络设置 物理机网卡必须采用 bond 配置（建议主备模式），

# 3.2.1 物理机配置

/etc/sysconfig/network-scripts/ifcfg-bond0 文件配置：

DEVICE $\equiv$ bond0   
TYPE $\equiv$ Ethernet   
NAME $\equiv$ bond0   
DNS1=a.a.a.a   
DNS2 $\equiv$ b.b.b.b   
ONBOOT $\equiv$ yes   
BOOTPROTO $\equiv$ static   
NM-controlledLED $\equiv$ no   
IPADDR $= x.x.x.x$ NETMASK $\equiv$ y.y.y.y   
GATEWAY $\equiv$ z.z.z.z   
BONDING_OPTIONS $\equiv$ "mode $\equiv$ 1 mimmon $= 100$ " (primary $\equiv$ ethX可选，根据需要添加，但需要跟updelay $= 120000$ 一起使用)

/etc/sysconfig/network-scripts/ifcfg-eth0 文件配置：

```python
DEVICE=eth0  
TYPE=Ethernet  
NAME=eth0  
USERCTL=no 
```

NM_CONTROLLED $\equiv$ no   
IPV6INIT $\equiv$ no   
ONBOOT $\equiv$ yes   
BOOTPROTO $\equiv$ none   
MASTER $\equiv$ bondO   
SLAVE $\equiv$ yes

/etc/sysconfig/network-scripts/ifcfg-eth1 文件配置：

```txt
DEVICE=eth1  
TYPE=Ethernet  
NAME=eth1  
USERCTL=no  
NM_CONTROLLED=no  
IPV6INIT=no  
ONBOOT=yes  
BOOTPROTO=none  
MASTER=bond0  
SLAVE=yes 
```

编辑/etc/modprobe.d/bonding.conf(系统默认不存此文件，需要手工建)，增加下面一行：

```txt
alias bond0 bonding 
```

# 3.2.2 虚拟机配置

/etc/sysconfig/network-scripts/ifcfg-eth0 文件配置：

```txt
DEVICE=eth0  
TYPE=Ethernet  
NAME=eth0  
DNS1=a.a.a.a  
DNS2=b.b.b.b 
```

```txt
USERCTL=no  
NM_CONTROLLED=no  
IPV6INIT=no  
ONBOOT=yes  
BOOTPROTO=static  
IPADDR=x.x.x.x  
NETMASK=y.y.y.y  
GATEWAY=z.z.z.z 
```

注：上述配置示例中，DNS、IP地址、子网掩码和网关及DOMAIN均用a.a.a.a和b.b.b.b、x.x.x.x、y.y.y.y 和 z.z.z.z 及 XXX.xxx.cn 表示，实际配置中应修改为真实的配置值。

# 使用nmcli配置

```txt
nmcli connection modify <interface-name> connection.autoconnect yes nmcli connection modify <interface-name> ipv4.method manual ipv4_addresses </prefix> ipv4.gateway <GW-address> #例如配置ens33接口： nmcli connection modify ens33 connection.autoconnect yes nmcli connection modify ens33 ipv4.method manual ipv4_addresses "172.16.142.103/24" ipv4.gateway "172.16.142.2" ipv4.dns "172.16.142.2" 
```

# 3.2.3 路由配置

若操作系统同时有业务流量和其他流量如备份流量等，应增加相应网卡并配置路由，以将其他流量同业务流量分离。新增网卡的配置方法见上述物理机或虚拟机的网络配置，但网关不应设置。路由配置的方法如下所示：

 打开/etc/sysconfig/static-routes 文件，若该文件不存在则手工新建一个；  
在static-routes文件中增加所需要配置的路由，配置示例如下所示：

```txt
any net 10.0.18.0/24 gw 10.0.18.253 
```

重启网络服务，然后执行route –n|grep UG，查看是否新增路由的记录。

注: 上述路由表示本机到 10.0.18 网段的路由都经由 10.0.18.253 这个网关发送。

# 3.2.4 内核配置

注：以下设置选项在/etc/sysctl.conf 中修改，执行: sysctl -p 生效。

<table><tr><td>编号</td><td>设置值</td><td>说明</td></tr><tr><td>1</td><td>netipv4.conf.all.arpbao = 0
netipv4.conf.default.arpbao = 0</td><td>不允许ignore arp(只有LVS时才需要此选项)</td></tr><tr><td>2</td><td>netipv4.conf.all.arp_filter = 0
netipv4.conf.default.arp_filter = 0</td><td>不允许ignore arp filter(只有LVS时才需要此选项)</td></tr><tr><td>3</td><td>netipv4.conf.all.rp_filter = 0</td><td>不开启rp_filter(防止ip欺骗)</td></tr><tr><td>4</td><td>netipv4.conf.all.log_martians = 0
netipv4.conf.default.log_martians = 0</td><td>不记录探测包,源路由包,重定向包</td></tr><tr><td>5</td><td>netipv4.conf.all.promotealsecondari es = 1</td><td>禁止删除primary ip,当secondary ip地址与primary ip地址属于同一个网段时,删除primary ip地址时也会删除secondary ip地址</td></tr><tr><td>6</td><td>netipv4.ip_no_pmtu_disc = 1</td><td>禁用ip path mtu discover</td></tr><tr><td>7</td><td>netipv4.conf.all.forwarding = 0
netipv4.conf.default.forwarding = 0</td><td>禁用ip转发</td></tr><tr><td>8</td><td>netipv4.icmpTONgrecycle_broadcasts = 1</td><td>禁止响应目的地为广播地址类型为echo的icmp包。</td></tr><tr><td>9</td><td>netipv4.conf.all.accept_source rout e = 0
netipv4.conf.default.accept_source</td><td>禁用源地址路由</td></tr><tr><td></td><td>_route = 0</td><td></td></tr><tr><td rowspan="2">10</td><td>net. ipv4.conf.all.accept Redirects = 0</td><td rowspan="2">拒绝路由重定向包</td></tr><tr><td>net. ipv4.conf.default.acceptredirects = 0</td></tr><tr><td>11</td><td>net. ipv4.conf.allsecureRedirects = 0</td><td>也不允许网关发送的路由重定向包</td></tr><tr><td>12</td><td>net. ipv4.tcp_timestamps = 1</td><td>开启 tcp 时间戳选项</td></tr><tr><td>13</td><td>net. ipv4.icmpignore_bogus_error_reponses = 1</td><td>某些路由器忽略 RFC1122 规定的包，发送假的错误消息给源主机，导致源主机记录大量错误信息到日志中</td></tr><tr><td rowspan="2">14</td><td>net. ipv4.conf.allproxy ARP = 0</td><td rowspan="2">关闭 arp代理</td></tr><tr><td>net. ipv4.conf.default proxies ARP = 0</td></tr><tr><td rowspan="2">15</td><td>net.core.somaxconn = 65535</td><td>最大的 syn 包队列设置，加大 tcp 会话等待数</td></tr><tr><td>net. ipv4.tcp_max_syn_backlog = 838860</td><td>对于需要支撑高并发的业务服务器，可以根据压力测试情况，将该值增大。</td></tr><tr><td>16</td><td>net. ipv4.tcp_syncookies = 1</td><td>防止客户端使用 syn 包打开半链接进行拒绝攻击，</td></tr><tr><td>17</td><td>net. ipv4.tcp_fin_timeout = 60</td><td>本端关闭的链接从 FIN_WAIT_2 到TIME_WAIT 状态设置为 60</td></tr><tr><td>18</td><td>net. ipv4.ip_forward = 0</td><td>禁止 IP 转发</td></tr><tr><td>19</td><td>net. ipv4.conf.all.send Redirects = 0</td><td>禁止发送重定向报文</td></tr><tr><td rowspan="3">20</td><td>net. ipv4.tcp_keepalive_time = 300</td><td rowspan="3">TCP keepalive 设置</td></tr><tr><td>net. ipv4.tcp_keepalive_probes = 5</td></tr><tr><td>net. ipv4.tcp_keepalive_intvl = 6</td></tr></table>

# 存储配置

# 4.1 本地磁盘管理

# 磁盘配置要求：

在物理服务器上安装操作系统时，操作系统所在磁盘必须配置为RAID1的硬件磁盘阵列

# 物理机分区划分规范：

除/boot 分区不能采用 LVM 外，其他所有分区都应采用 LVM 管理磁盘，另外应用程序如果使用 LVM 来管理,需要创建单独的 VG。LVM 管理请参考 7.2“逻辑卷管理”。

文件系统可按照下表来设置逻辑卷名称及相应空间(这里列出的为最低空间要求)：

<table><tr><td>Mount Point</td><td>LV命名</td><td>最低配置(GB)</td><td>备注</td></tr><tr><td>/boot</td><td></td><td>500M</td><td>必须是分区</td></tr><tr><td>/</td><td>/dev/mapper/rootvg-lv_root</td><td>300G</td><td></td></tr><tr><td>swap</td><td>/dev/mapper/rootvg-lv_swap</td><td>16G</td><td></td></tr></table>

注：上述分区方案只用了RAID1操作系统硬盘，对于数据磁盘，需要根据应用情况进行规划。

对于内存大于 50G 的机器，/dev/mapper/Rootvg-lv_root 需要在业务上线前手工触发kernel panic 来检测大小是否适用。

# 虚拟机分区划分规范：

除/boot 分区不能采用 LVM 外，其他所有分区都应采用 LVM 管理磁盘，另外应用程序如果使用 LVM 来管理,需要创建单独的 VG。。LVM 管理请参考 7.2“逻辑卷管理”。

文件系统可按照下表来设置逻辑卷名称及相应空间(这里列出的为最低空间要求)：

<table><tr><td>Mount</td><td>LV 命名</td><td>最低配置(GB)</td><td>备注</td></tr><tr><td>Point</td><td></td><td></td><td></td></tr><tr><td>/boot</td><td></td><td>500M</td><td>必须是分区</td></tr><tr><td>/</td><td>/dev/mapper/rootvg-lv_root</td><td>90G</td><td></td></tr><tr><td>swap</td><td>/dev/mapper/rootvg-lv_swap</td><td>8G/16G</td><td></td></tr></table>

swap 的大小按照如下规则：

内存小于等于 2G，swap 为内存的 3 倍  
内存大于 2G，小于等于 8G，swap 为内存的 2 倍  
内存大于 8G，swap 最大为 16G（MAX）  
如果有应用对于 swap 又特殊要求，按照应用的要求划分。

# 4.2 卷组规范

#  逻辑卷（LV）命名规范

用于操作系统的逻辑卷命名采用入下表所示方案：

<table><tr><td>逻辑卷用途</td><td>命名方法</td><td>举例</td></tr><tr><td>用于文件系统</td><td>lv _ 挂载点名称</td><td>Lv_root</td></tr><tr><td>用于保留交换区的文件系统</td><td>lv _ 挂载点名称</td><td>Lv_swap</td></tr></table>

注意：划分的逻辑卷必须有特定的用途，严禁系统中存在未使用的逻辑卷。

# 4.3 文件系统格式

RHEL6默认文件系统格式建议为ext4，对于特殊情况可以选择其他文件系统（比如磁盘大小超过16T，可以使用xfs文件系统），RHEL7默认文件系统格式为xfs.

# 4.4 多路径软件

在物理系统使用共享存储的情形下，应该配置多路径软件，虚拟机系统无需配置。

1. 建议优先使用存储厂商提供的多路径软件，安装配置按照存储厂商提供的安装说明进行配

置即可。

2. 若存储厂商不提供多路径软件，则应安装系统自带的多路径软件，开启方法如下：

 在 RedHat Enterprise Linux Server 6 上:

```txt
service multipathd start #chkconfig multipathd on 
```

 在 RedHat Enterprise Linux Server7 上:

```txt
systemctl start multipathd.service #systemctl enable multipathd.service 
```

3. /etc/multipath.conf为多路径配置文件，建议优先使用存储厂商提供的多路径配置文件，如果存储厂商没有提供，那么可以由操作系统命令”/sbin/mpathconf –enable”探测存储信息后自动生成。除非特殊需求，不应修改。

对于 polling_interval，我们使用如下计算公式：

```python
polling_interval = 10 (default when Lun is less than a NUMBER[50])
    polling_interval = 60 (Number[50] ~ 3*NUMBER[50])
    polling_interval = 120 (10*Number[50])
    polling_interval = 300 (30*Number[50]) 
```

配置范例说明如下：

defaults { (全局配置设定)

```txt
udev_dir /dev  
polling_interval 10 （路径探测轮询间隔时间）  
path_grouping_policy multibus (路径组合策略方式)  
getuid_callout "/lib/udev/scsi_id-whitelisted-device=/dev/%n" （唯一路径检测方式）  
prio alua （路径优先级检测方式）  
pathchecker readsector0 （路径状态检查方式）  
rr_min_io 100 （设备状态检查最小读
```

```txt
max_fds 8192 (multipathd程序最大打开文件句柄数)  
rr_weight priorities (路径优先级权重计算方式)  
failback immediate (切换策略)  
no_path_retry fail (路径检查失效后处理策略)  
user Friendly names yes (命名方式是否启用/dev/mapper/mpathN)  
}  
multipaths { (给特定的wwid设备设置其他策略)  
multipath {  
    wwid xxx  
    alias YOUR_DEVICE_NAME  
    path_checker xxx  
    path_selector xxx  
    failback xxx  
}  
}  
devices { (给特定vendor/product设备设置其他策略)  
device {  
    vendor xxx  
    product xxx  
    path_checker xxx  
    path_selector xxx  
    failback xxx  
} 
```

# 4.5 NFS 挂载选项规范

# 1. hard 和 soft 选项

虽然 soft 选项能很快检测到NFS不能访问，但是soft选项容易导致正在写的数据被损坏，所以对于以rw挂载的NFS，应该使用默认的hard选项。对于使用NFS作为心跳盘的OracleRAC环境，对于NFS的可用性需要快速判断，因为心跳盘不会涉及到数据损坏，所以需要配置为soft选项。

# 2. bg 选项

如果客户端再重启的时候遇到网络故障或者NFS Server端无法访问，可能会导致系统hang住，解决这个问题的方法是，使用bg选项将NFS的开机自动挂载放在后台进行，默认是fg前台进行挂载。

对于以 rw 挂载的 NFS，开机自动挂载及挂载选项设置示例如下：

```txt
<NFS Server>/vol /data nfs defaults,bg 0 0 
```

对于使用NFS作为心跳盘的Oracle RAC环境，开机自动挂载及挂载选项设置示例如下：

```txt
<NFS Server>/vol /votedisk nfs  
defaults, rw, bg, soft, nointr, rsize=32768, wsize=32768, tcp, noac, vers=3, timeo=600, actimeo=0  
0 0 
```

# 5 服务配置：

Ntp 服务器信息：

IP：10.71.8.230

IP：10.72.8.230

IP：10.81.0.230

IP：10.82.4.230

时钟同步建议采用如下规范：

VMware虚拟机中，须取消VMware Tools配置项中的“在虚拟机和ESXServer 操作系统之间进行时间同步”。  
操作系统应开启时间同步服务，以进行时间同步，配置方法如下：

 在 RedHat Enterprise Linux Server 6 上:

(1) 添加时钟同步服务器，在/etc/ntp.conf文件中增加如下配置：

总部系统添加如下地址：

server 10.0.170.124 prefer

(2) 启动 ntp 服务：

# service ntpd restart

(3) 添加ntp服务到系统启动进程：

# chkconfig ntpd on

 在 RedHat Enterprise Linux Server 7 上:

1）添加时钟同步服务器，在/etc/chrony.conf 文件中增加如下配置：

总部系统添加如下地址：

server 10.0.170.124 prefer

2）启动 chronyd 服务：

# systemctl start chronyd.service

(4) 添加 chronyd 服务到系统启动进程：

# systemctl enable chronyd.service

时间同步最大阀值应设置为500秒，服务器与时间服务器的时间误差超过500秒时应停止同步，在 RedHat Enterprise Linux Server 6 上 ntpd 服务将自动退出，在RedHat Enterprise Linux Server 7 上 chronyd 服务将忽略跳过，配置方法如下:

 在 RedHat Enterprise Linux Server 6 上：

在配置文件/etc/ntp.conf首行添加如下内容：

tinker panic 500

 在 RedHat Enterprise Linux Server 7 上：

在配置文件/etc/chrony.conf 中添加如下内容：

maxchange 500 0 -1

时钟同步模式须采用微调模式，并禁止时间服务在服务启动或者重启时自动同步

时间，配置方法如下：

 在 RedHat Enterprise Linux Server 6 上：

在配置文件/etc/sysconfig/ntpd 中的 OPTIONS 中添加 -x 选项，删除 -g 选项：

OPTIONS $=$ " -x -u ntp:ntp -p /var/run/ntpd.pid"

 在 RedHat Enterprise Linux Server 7 上：

RHEL7 上 chrony 默认已经开启微调模式，默认值是 83333.333 ppm (onetwelfth)，即每秒同步 1/12 秒，在RHEL6上微调模式同步1秒需要2000秒的时间，即每秒同步 0.5ms，需保证所有 RHEL 版本时间服务的微调模式一致，在 RHEL7 上需将微调模式的频率修改为 500 ppm，即 1/2000 秒，配置如下：

注释或者删除配置文件/etc/chrony.conf 中的如下内容：

RHEL7.2 为:

```txt
makestep 10 3 
```

RHEL7.6 为:

```txt
makestep 1.0 3 
```

在配置文件/etc/chrony.conf 中添加如下内容：

```txt
maxslewrate 500 
```

以上所有修改之后，需要重新启动 ntpd 或者 chronyd 服务器，操作如下：

 在 RedHat Enterprise Linux Server 6 上:

```txt
service ntpd restart 
```

 在 RedHat Enterprise Linux Server 7 上:

```txt
systemctl restart chronyd.service 
```

服务器第一次与时间服务器进行时间同步需采用手动同步的方式，在同步之前需要检查与时间服务器的误差范围，若误差范围较大（超过预设500s）,需要评估时间调整后对操作系统和业务的影响，检查方法如下：

```txt
ntpdate -q <NTP Server IP地址> 
```

手动同步方法如下：

```txt
ntpdate <NTP Server IP地址>
```

注：手动同步时间时需要先停止时间服务，同步完成后才开启时间服务。

# 6.1 服务的配置

为提高系统的稳定性，减少系统网络配置上的安全漏洞，如非特殊需要，建议关闭以下系统服务：

<table><tr><td>服务名称</td><td>服务描述</td></tr><tr><td>cups</td><td>打印服务</td></tr><tr><td>postfix</td><td>邮件服务</td></tr><tr><td>pcscd</td><td>smart卡登录服务</td></tr><tr><td>smartd</td><td>磁盘监控服务，对于做过RAID的磁盘无效</td></tr><tr><td>sound</td><td>声卡服务</td></tr><tr><td>target</td><td>iscsi target服务</td></tr><tr><td>smb</td><td>与windows互访问的文件服务</td></tr><tr><td>acpid</td><td>acpi高级电源管理服务</td></tr><tr><td>iptables</td><td>ipv4防火墙服务</td></tr><tr><td>ip6tables</td><td>ipv6防火墙服务</td></tr><tr><td>firewalld</td><td>防火墙服务（RHEL7上才有的）</td></tr></table>

备注：上述网络服务可通过下列命令停止并关闭：

 在 RedHat Enterprise Linux Server 6 上:

```txt
# service <servicename> stop
# chkconfig <servicename> off
例如：
# service postfix stop
#chkconfig postfix off 
```

 在 RedHat Enterprise Linux Server 7 上:

```txt
# systemd停止 <servicename>
# systemd disable <servicename>
例如：
# systemd stop postfix.service
# systemd disable postfix.service 
```

# 6.2 SELINUX 服务

为了更方便的管理系统及应用程序服务，如非特殊需要，建议关闭系统的SELinux服务，操作步骤如下：

```txt
#getenforce #检查当前SELinux状态，若为Enforcing或   
Permissive则需修改   
#sed-i's/\SELINUX= \).*/\1disabled/g'/etc/selinux/config   
#修改配置文件   
# reboot #重启系统，若当前场景不适合重启系统，可执行以下步骤   
#setenforce 0 #临时关闭
```

# 6.3 设置服务器登录公告板

配置用户登录警告，如下：

```batch
echo "   
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   
\*   
\* 
```

\* \* I M P O R T A N T N O T I C E   
\* \*   
\* NFJJ's internal systems must only be used for conducting NFJJ's   
\* \* business or for purposes authorized by NFJJ management.   
\* \* UNAUTHORIZED ACCESS IS PROHIBITED   
\* \*   
\* Please change your password every 90 days. The password rule is : $12^{*}$ \*characters at least,including capital letter、small letter、number and\* \* special character.   
\* \*   
\* \*   
\*   
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

# 6.4 命令时间戳记录与命令行提示符

为安全审计需要，应在记录用户系统操作命令的同时记录命令的时间戳，在/etc/bashrc 文件中增加如下行：

export HISTTIMEFORMAT $\equiv$ "F % T

另外，还需要在命令行提示符中显示时间戳，在/etc/profile.d 目录中添加 ps1.sh 脚本（不建议直接修改/etc/bashrc文件），内容如下（脚本内容可从/etc/bashrc文件中复制）：

```shell
#!/bin/bash
# are we an interactive shell?
if [ "$PS1" ]; then
if [ -z "$PROMPT_COMMAND" ]; then
case $TERM in
xterm*) 
if [ -e /etc/sysconfig/bash-prompt-xterm ]; then
PROMPT_COMMAND=/etc/sysconfig/bash-prompt-xterm
else
PROMPT_COMMAND='printf "\033]0;%s%@%s:%s\007" "${USER}" "${HOSTNAME%*.}" "${PWD/#$HOME/~}''
fi
;; 
screen)
if [ -e /etc/sysconfig/bash-prompt-screen ]; then
PROMPT_COMMAND=/etc/sysconfig/bash-prompt-screen
else 
```

```shell
PROMPT_COMMAND='printf "\033]0;%s%@%s:%s\033\" "$  
{USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/~}''  
fi  
;  
*)  
[ -e /etc/sysconfig/bash-prompt-default ] &&  
PROMPT_COMMAND=/etc/sysconfig/bash-prompt-default  
;  
esac  
fi  
# Turn on check winsize  
shopt -s check winsize  
[ "$PS1" = "\\s-\v\W" ] && PS1="[\u@\h \W]<$(date+'%ym%d') \t>\\\( "  
fi 
```

# 6.5 ULIMIT 设置

不恰当的limit设置会导致系统或者应用程序运行出现错误，应对/etc/security/limits.conf配置文件中的参数进行设置，在 RHEL6 中将/etc/security/limits.d/90-nproc.conf(RHEL7 为/etc/security/limits.d/20-nproc.conf)配置文件中的以下行注释：

#*

soft

nproc

1024

配置文件/etc/security/limits.conf 中主要参数的说明及配置值如下所示：

应用程序 core 大小设置，为防止大量的 core 文件占用系统，建议应用程序 core 大小限制为100M以下，在配置文件中增加如下两行：

```txt
* soft core 102400
* hard core 102400 
```

对于需要打开调试搜集应用程序core 文件，可以根据应用内存使用情况设置合适大小或者无限制，例如 test 设置为 unlimited：

```txt
test soft core unlimited test hard core unlimited 
```

单个程序打开的最大文件句柄数，不应设置过小，建议设置为 8192:

```txt
* soft nofile 8192
* hard nofile 8192 
```

对于需要较多的文件句柄数的应用，例如Web服务器，可以根据应用需要设置合适的值，但需要指定应用用户，例如：

```txt
test soft nofile 65535  
test hard nofile 65535 
```

单个程序创建的最大线程数，一般建议设置为 8192：

```txt
* soft nproc 8192
* hard nproc 8192 
```

对于需要较多线程数的应用，例如Web服务器，可以根据应用需要设置合适的值，但需要指定应用用户，例如：

```txt
test soft nproc 65535  
test hard nproc 65535 
```

其他ulimit参数除非有特需要求，不应修改，例如: data/stack程序数据段和堆栈段大小，rss程序驻留在系统中占有内存最大值，memlock/locks内存锁大小和文件锁个数。

# 6.6 文件系统挂载选择设置

修改文件系统默认选项，提升文件系统稳定性和安全性。安装后应做如下修改：

对/tmp 和/var 分区增加 nodev，nosuid 选项  
对/home 分区增加 nosuid 选项

例如，针对/var 分区的配置，可编辑/etc/fstab, 然后进行如下修改：

```txt
/dev/vg/lv_var /var ext4 defaults,nosuid 0 0 
```

# 6.7 系统敏感文件权限设置

针对系统文件，配置最小可用的文件权限。部分修改如下：

```txt
# chmod 400 /etc/crontab
# chmod 400 /etc/securety
# chmod 600 /boot/grub/grub.conf
# chmod 600 /boot/grub2/grub.cfg (仅针对RHEL7)
# chmod 600 /boot/efi/EFI/redhat/grub.cfg (仅针对使用UEFI模式)
# chmod 600 /etc/inittab
# chmod 600 /etc/login.defs
```

# 6.8 日志审计策略配置

1. 系统缺省已经开启 syslog/rsyslog 服务，禁止关闭。系统 syslog/rsyslog 服务会将所有系统日志自动记录到/var/log/messages文件中，系统日志永久保留。

2. 开启audit审计功能，可以监控指定用户或目录，缺省会监控root的所有登录和操作。

添加规则到 /etc/audit/audit.rules(RHEL7 为/etc/audit/rules.d/audit.rules) 文件中，实现监控所有用户的登录行为，包含用户所有操作，以及shell脚本中的命令

```batch
-a exit,always -F arch=b64 -S execve -k exec  
-a exit,always -F arch=b32 -S execve -k exec 
```

添加后 RHEL6、7 都需要通过执行“service auditd restart”使配置生效，然后便可用ausearch -k exec 来列出用户操作的记录。

添加规则到 /etc/audit/audit.rules(RHEL7 为/etc/audit/rules.d/audit.rules) 文件中，实现对重点配置文件的监控（根据实际应用额外添加文件列表）

```shell
-w /etc/crontab -p wa -k crontab  
-w /etc/hosts -p wa -k hosts  
-w /etc/hosts.allow -p wa -k hosts-allow  
-w /etc/hosts.deny -p wa -k hosts-deny 
```

```batch
-w /etc/fstab -p wa -k fstab
-w /etc/passwd -p wa -kpasswd
-w /etc/shadow -p wa -k shadow
-w /etc/group -p wa -k group
-w /etc/gshadow -p wa -k gshadow
-w /etc/ntp.conf -p wa -k ntp (RHEL7为-w /etc/chrony.conf -p wa -k ntp)
-w /etc/sysctl.conf -p wa -k sysctl
-w /etc/security/limits.conf -p wa -k limits
-w /boot/grub/grub.conf -p wa -k grub (RHEL7为-w /boot/grub2/grub.cfg -p wa -k grub)
-w /etc/ssh/sshd_config -p wa -k sshd
-w /etc/ssh/ssh_config -p wa -k ssh
-w /etc/udev/rules.d/ -p wa -k udev
-w /etc/profile -p wa -k profile
-w /etc/kdump.conf -p wa -k kdump
-w /etc/lvm/lvm.conf -p wa -k lvm
-w /etc/login.defs -p wa -k login-defs
-w /etc/rsyslog.conf -p wa -k rsyslog
-w /etc/sysconfig/i18n -p wa -k i18n (RHEL7为-w /etc/locale.conf -p wa -k i18n)
-w /etc/sysconfig/network -p wa -k network
-w /etc/multipath.conf -p wa -k multipath
-w /etchostname -p wa -k hostname (仅RHEL7) 
```

添加后使用 ausearch -k <key>来列出对应文件的修改记录，如 ausearch -kmultipath。

3. 配置 audit 日志，audit 日志文件自动保存在/var/log/audit/目录中。

每个log文件超过50M时进行轮换，保持最后4个log，可以通过/etc/audit/auditd.conf进行配置，修改如下选项：

```txt
num_logs = 4 #个数  
max_log_file = 50 #大小(MB)
```

 默认情况下，审计日志为每20条flush一次，为了防止由于大量后台脚本运行产生的审计日志在频繁flush到磁盘，导致磁盘使用率过高（特别是没有cache直接落盘的RAID卡），所以需要修改 flush 模式为 NONE。可以通过编辑 audit 配置文件/etc/audit/auditd.conf 进行配置，修改如下选项：

flush $\equiv$ NONE

4. 启动 audit 和 syslog/rsyslog 服务

启动审计服务：

 在 RedHat Enterprise Linux Server 6 上:

```txt
service auditid start #若更改了配置文件则使用restart替换start#chkconfig auditid on
```

 在 RedHat Enterprise Linux Server 7 上:

```txt
service auditid.service restart #若更改了配置文件则使用restart替换start#systemctl enable auditid.service
```

# 6.9 KDUMP 配置

系统应开启kdump服务，以便在服务器系统崩溃时能够加载捕获内核，将系统内核崩溃前的内存镜像保存并进行转储，以定位内核崩溃的原因并改进。

默认kdump保存路径为/var/crash，如非特殊不可修改。

配置 kdump 服务需要提前在 grub 内核引导项中(RHEL6 的配置文件位于/boot/grub/

grub.conf，默认值为 auto，RHEL7 的配置文件位于/boot/grub2/grub.cfg，默认值为 auto)设置crashkernel=xxM 参数，xx 值通过下表来计算:

<table><tr><td>内存大小</td><td>Crashkernel值</td></tr><tr><td>&lt;2GB</td><td>128MB</td></tr><tr><td>2GB-6GB</td><td>256MB</td></tr><tr><td>6GB-8GB</td><td>512MB</td></tr><tr><td>&gt;8GB</td><td>768MB</td></tr></table>

配置完 crashkernel 后需要重启系统才可生效，然后开启 kdump 服务的命令如下：

 在 RedHat Enterprise Linux Server 6 上:

```txt
servicekdump start #chkconfigkdump on 
```

 在 RedHat Enterprise Linux Server 7 上:

```txt
systemctl start kdump.service #systemctl enable kdump.service 
```

配置完 kdump 服务后，需要使用以下的命令来触发 kernel panic 检测 kdump 服务是否配置正确：

echo c $>$ /proc/sysrq-trigger #该命令会导致系统 crash，切莫在生产环境使用！！

若 kdump 提示 out-of-memory 错误，可根据情况增大 crashkernel 的值。

# 6.10系统内核参数配置

注：以下设置选项在/etc/sysctl.conf 中修改，执行: sysctl -p 生效。  

<table><tr><td>编号</td><td>默认值（如非特殊需要，不应修改）</td><td>说明</td></tr><tr><td>1</td><td>vm.min_free_kbytes = 16384</td><td>最小内存水平线，free内存低于此值，系统会强制回收内存。建议最大设置不要超过：64000 KB。应使用默认值。最小值：128K，最大值：65536K</td></tr><tr><td>2</td><td>vm.vfs_cache_pressure = 100</td><td>vfs层cache保留倾向，&gt;100表示系统尝试多回收vfs cache，&lt;100表示系统尽量多保留vfs</td></tr><tr><td></td><td></td><td>cache。</td></tr><tr><td>3</td><td>vm.dirty_ratio = 40</td><td>Page cache达到40% total memory(含 swap)时,系统尝试将cache回写到磁盘,回收内存。</td></tr><tr><td>4</td><td>vm.page-cluster = 3</td><td>每次写入swap的最小页面数,默认是2的3次方=8个页面。</td></tr><tr><td>5</td><td>(需要根据内存大小使用计算公式来计算,例如8G内存:)
fs.file-max = 838860</td><td>kernel允许的最大文件句柄数。系统启动时根据内存自动调节,打开一个文件大概需要1k,总数不应超过系统内存的10%:计算公式为:
Max(N, NR_FILE)
N=(mempages * 4)/10
NR_FILE=4096
例如内存为8G的设置为
(8*1024*1024/4)*4/10=838860</td></tr><tr><td>6</td><td>kernel.shmmax</td><td>共享内存的最大值,系统启动时根据内存自动调节,如非特殊需要,不应修改。此值最大设置为物理内存的90%。</td></tr><tr><td>7</td><td>kernel.shmmni = 4096</td><td>共享内存的最小值,系统默认值为4096,如非特殊需要,不应修改。</td></tr><tr><td>8</td><td>kernel.core Uses pid = 0 (默认为1)
kernel.core_pattern = corefile/core-%e</td><td>应用程序core文件的命名设置,为防止应用程序生成大量core文件占用系统空间,应用程序core文件应设置为仅生成一个。其中core_pattern的路径可修改为其他路径。默认路径为应用用户家目录,且没有完全开启,如需完全开启,只需在应用用户家目录下创建corefile目录即可(但需注意home目录空间比应用程序所用内存要大)。</td></tr><tr><td>9</td><td>kernel.sysrq = 1</td><td>系统hung住时,可以使用Alt+Sysrq+c来收集vmcore</td></tr><tr><td>10</td><td>vm.swappiness = 0</td><td>swappiness参数值可设置范围在0到100之间。低参数值会让内核尽量少用交换,更高参数值会使内核更多的去使用交换空间。
当内存大于256G时,设置为0,优先使用物理内</td></tr><tr><td></td><td></td><td>存。</td></tr></table>

# 6.11CRONTAB 配置

默认cron任务的输出会以邮件的方式发送给管理员，由于系统默认已经关闭邮件服务，所以邮件会发送失败，最后会被扔在/var/spool/postfix/maildrop 目录下，最后的结果是导致/var 目录使用率逐渐增大，当inode使用率到达 $100 \%$ 时，会导致写入失败。

正规的crontab写法需要将cron作业的输出重定向到指定的输出文件中，为了防止cron作业写法不正规导致不必要的问题，我们可以修改crond配置文件，关闭邮件发送，编辑文件/etc/sysconfig/crond，修改如下选项：

```makefile
# cat /etc/sysconfig/crond
# Settings for the CRON daemon.
# CRONDARGS= : any extra command-line startup arguments for crond
CRONDARGS=-m off" 
```

# 6.12物理安全设置

1. 应禁止使用 usb 存储设备，防止物理 usb 设备引入木马文件。

```batch
echo "install usb-storage /bin/true" >> /etc/modprobe.d/usb-storage.conf 
```

2. 必须禁止 Control+Alt+Delete 直接重启服务器:

 在 RedHat Enterprise Linux Server 6 上:

```txt
sed -i 's/^\start on control-alt-delete/#start on control-alt-delete/g' /etc/init/control-alt-delete.conf 
```

 在 RedHat Enterprise Linux Server 7 上:

```txt
systemctl mask ctrl-alt-del.target 
```

# 6.13*口令策略设置

# 口令复杂度规定

# 密码复杂性配置应满足如下要求

密码长度至少为 12 位，且含有如下字符类型中的四种：

 英语大写字母 A, B, C, … Z  
 英语小写字母 a, b, c, … z  
 西方阿拉伯数字 0, 1, 2, … 9  
 非字母数字字符，如标点符号， $@$ , #, $, %, &, *等

密码历史为5次，是指修改口令时禁止使用最近5次已使用过的密码口令（己使用过的口令会被保存在 /etc/security/opasswd 下面）。

 在 RedHat Enterprise Linux Server 6 上:

```javascript
sed -i '/^password[[:space:]]\{1,\}requisite[[:space:]]\{1,\}pam Cracklib.so/a\password required pam_pwhistory.so use_authtok remember=5 enforce_for_root'/etc/pam.d/system-auth-ac 
```

 在 RedHat Enterprise Linux Server 7 上:

```shell
sed -i '/^password[[:space:]]\{1,\}requireit[[:space:]]\{1,\}pam_pwquality.so/a\password required pam_pwhistory.so use_authtok remember=5 enforce_for_root'/etc/pam.d/system-auth-ac 
```

# 口令有效期规定

root用户应满足如下用户口令策略，对于其他用户，如无特殊要求，建议采用。修改/etc/login.defs文件，修改如下参数的值：

PASS_MAX_DAYS90（最长期限 90 天）  
 PASS_MIN_DAYS 0 （最短期限0天）  
 PASS_MIN_LEN 12 （最少 12 个字符）  
 PASS_WARN_AGE 14 （提前 14 天提示密码修改）

# 设置：

 在 RedHat Enterprise Linux Server 6 上:

sed -i "s/^ $\backslash$ (password[[:space:]]*requisite[[:space:]]*pam Cracklib.so).\*.*\1 try_first_pass retry=5 minlen=12 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=-1 enforce_for_root/g" /etc/pam.d/system-auth-ac

 在 RedHat Enterprise Linux Server 7 上:

```txt
sed -i "s/^\(\backslash\) (password[[:space:]]*requisite[[:space:]]*pam_pwquality.so\).*\(\backslash 1\) try_first_pass local_users_only retry \(= 5\) minlen \(= 12\) dcredit \(= -1\) ucredit \(= -1\) ocredit \(= -1\) lcredit \(= -1\) enforce_for_root authtok_type \(= /g\) "/etc/pam.d/system-auth-ac 
```

超级用户口令最长有效期为90，具有配置、修改权限用户的口令最长有效期可为90天。

添加完用户后，执行以下命令：

# 超级用户

```txt
chage -M 90 username 
```

# 具有配置、修改权限用户

```markdown
# chage -M 90 username 
```

# 6.14UID 0 用户设置

系统应禁止除 root 用户之外 UID 为 0 的用户。

系统中每一个用户都被分配一个用户ID号，ID 号为0 是为root 保留的，UID 号1-499 是为系统其它预定义的帐号保留的，UID为0拥有系统的最高特权，为了系统安全，应保证只有root用户的UID为0。

检查方法：

```txt
awk -F: ($3 == 0) { print $1}'/etc/passwd 
```

返回值包括“root”以外的条目，则应修正。

# 6.15*系统登录安全设置

针对系统登录进行加固，提升系统安全性。具体修改如下：

记录不存在用户的登录信息，避免用户误输入导致密码泄露

```batch
echo "LOG_UNKFAIL_ENAB yes" >> /etc/login.defs 
```

配置用户密码尝试次数为 5 次，避免暴力破解

```shell
echo "LOGIN_RETRIES 5" >> /etc/login.defs 
```

记录用户上次登录时间，用户登录时给予提示

```batch
echo "LASTLOG_ENAB yes" >> /etc/login.defs 
```

# 6.16系统全局 PROFILE 安全设置

配置系统超时自动退出，建议配置成600秒

```shell
echo "export TMOUT=600" >> /etc/profile 
```

配置命令历史记录条数为5000

```shell
echo "export HISTFILESIZE=5000" >> /etc/profile 
```

连续5次输错密码禁用一段时间，建议配置成300秒

在 RedHat Enterprise Linux Server 6 和 7 上:

sed -i '/auth[[:space:]]*required[[:space:]]*pam_env.so/a\auth required pam_tally2.so onerr $\equiv$ fail deny $= 5$ unlock_time $= 300$ evendeny_root root_unlock_time $= 300$ /etc/pam.d/system-auth-ac # sed -i '/account[[:space:]]*required[[:space:]]*pam_unix.so/i\account required pam_tally2.so'/etc/pam.d/system-auth-ac #sed-i'/auth[[:space:]]*required[[:space:]]*pam_env.so/a\auth required pam_tally2.so onerr $\equiv$ fail deny $= 5$ unlock_time $= 300$ evendeny_root root_unlock_time $= 300$ /etc/pam.d/password-auth-ac #sed-i'/account[[:space:]]*required[[:space:]]*pam_unix.so/i\account required pam_tally2.so'/etc/pam.d/password-auth-ac

 根据安全审计要求，所有允许登录操作系统的用户的umask值须设置为077。

# 6.17网络客户端 IP 建议

为进一步提高安全性，远程登录协议中，尽量做到对ssh, telnet, ftp等网络服务客户端的IP地址进行限制，能使用特定的中转机客户端IP发起登录连接最好。

# 6.18CRON 授权规定（建议）

除 root 和特定运行维护的账号拥有 CRON 权限外，其他账号不应具有该权限。

配置方法：将允许拥有CRON权限的账号加入到/etc/cron.allow(系统默认不存在，需要手工建此文件)配置文件中。

# 6.19删除 RHOST 相关高风险文件

rcp，rsh，rlogin 等远程拷贝和登录命令会使用 rshost 相关文件，这些命令存在较高风险，应禁止使用，并在实际使用中用scp, ssh等命令替代。其相关配置文件应该删除。

删除命令如下：

```txt
rm /root/.rhosts /root/.shosts /etc/hosts.equiv /etc/shosts.equiv 
```

# 6.20SSHD 配置

为保证sshd服务的安全性，应在/etc/ssh/sshd_config配置文件中放开如下配置的注释并做相应的修改：

强制使用22号端口

Port 22

记录所有信息，包括info信息

LogLevel INFO

最大重试次数从 5 次(RHEL7 中的默认值为 6)

MaxAuthTries 5

允许密码认证

PasswordAuthentication yes

禁止 root 远程登录

PermitRootLogin no

在使用 RhostsRSAAuthentication 或者 HostbasedAuthentication 两种认证方式时，应禁止使用 .rhosts 和 .shosts 两个文件

RhostsRSAAuthentication no(RHEL7.4 中没有此值)

当使用密码认证时，不允许设置空密码

PermitEmptyPasswords no

在用户登录前，是否检查用户文件和目录的属主和权限

StrictModes yes

在使用 RhostsRSAAuthentication 或者 HostbasedAuthentication 两种认证方式时，忽略~/.ssh/known_hosts 文件

IgnoreUserKnownHosts yes

使用版本为2的ssh协议

Protocol 2(RHEL7.4 中没有此值)

不允许基于 GSSAPI 的用户认证

```txt
GSSAPIAuthentication no 
```

用户退出登录后不自动销毁用户凭证缓存

```txt
GSSAPICleanupCredentials no 
```

不使用 dns 反向解析

```txt
UseDNS no 
```

# 6.21 SFTP 服务加固策略

Linux服务器在缺省情况下开启了sftp服务，因此，需要对sftp服务做安全加固，默认情况下限制普通用户使用sftp服务。同时，配置sftp服务的日志记录功能。

1. 执行以下命令，创建 sftp 服务日志目录及文件。

```shell
mkdir -p /var/log/sftp   
#touch-f/var/log/sftp/sftp.log 
```

2. 执行以下命令，配置 sftp 服务的日志记录级别。

```txt
vi /etc/rsyslog.conf  
添加以下sftp服务日志记录级别配置：  
authpriv.info /var/log/sftp/sftp.log  
修改完成后，按ESC键退出编辑模式，输入:wq报错退出。
```

3. 执行以下命令，配置 sftp 服务日志转储。

```txt
vi /etc/logrotate.d/syslog  
在/var/log/messages 此行下添加：  
/var/log/sftp/sftp.log  
修改完成后，按 ESC 键退出编辑模式，输入:wq 报错退出。
```

4. 执行以下命令，配置 sftp 服务启动模式。

```txt
# vi /etc/ssh/sshd_config
将:
Subsystem sftp /usr/libexec/openssh/sftp-server
修改为:
Subsystem sftp /usr/libexec/openssh/sftp-server -f AUTHPRIV -l INFO
修改完成后，按 ESC 键退出编辑模式，输入:wq 报错退出。
```

5. 执行以下命令，创建 sftp 用户组。

```batch
groupadd -g 768 sftpgrp
```

6. 执行以下命令，加固 sftp 服务。

```txt
chown root:sftpgrp /usr/libexec/openssh/sftp-server
# chmod 750 /usr/libexec/openssh/sftp-server
```

# 6.22 系统日志转发策略（建议）

按要求，Linux服务器的audit日志需要做转储，上传到SOC服务器做日志审计分析。为将audit日志上传到SOC服务器，需要做如下配置。

1. 编辑/etc/audisp/plugins.d/syslog.conf 配置文件，打开日志转发功能，修改如下选项：

```hcl
active = yes  
args = LOG_LOCAL2 
```

2. 另外还需在 syslog/rsyslog 的配置文件中进行转发配置。目前 SOC 系统的 IP 和端口号分别如下：

办公网：xxx.xxx.xxx.xxx port

配置方法如下：

RHEL6 版本的操作系统，在/etc/rsyslog.conf 文件中作如下配置：

修改如下内容：

```javascript
*.info;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full;mail.full 
```

# 添加如下内容：

```powershell
$SystemLogRateLimitInterval 0
$SystemLogRateLimitBurst 0
$IMUXSockRateLimitBurst 0
$IMUXSockRateLimitInterval 0
$IMUXSockRateLimitSeverity 7
auth, authpriv, cron.info @10.1.250.71:514 
```

在/etc/rsyslog.d/目录添加 audit_filter.conf 文件，并在文件中添加如下内容：

```txt
:msg, ereregex, "(bin|sbin|sa)\/(ping|top|mpstat|iostat|iotop|vmstat|sar|sadc|sh)\"\~   
:msg, ereregex, "(sbin|udev)\/(fstab-import|udisks-part-id|path_id|edd_id|scsi_id)\"\~   
:msg, ereregex, "(bin|sbin)\/(tr|sort|wc|cut|awk|gawk|grep|fgrep|egrep|sed|head|tail|tailf)\"\~   
:msg, ereregex, "(bin|sbin)\/(sleep|ls|expr|nohup|date|cat|du|dirname|tar|gzip|df|sg persist|ip)\"\~   
:msg, ereregex, "(bin|sbin)\/(basename|hostname|readlink|bc|touch|dmesg)\"\~   
:msg, ereregex, "(bin|sbin)\/(consoles type|blkid|lsblk)\"\~   
:msg, ereregex, "\\"(ping|top|mpstat|iostat|iotop|vmstat|sar|sadc|sh)\"\~   
:msg, ereregex, "\\"(fstab-import|udisks-part-id|path_id|edd_id|scsi_id)\"\~   
:msg, ereregex, "\\"(tr|sort|wc|cut|awk|gawk|grep|fgrep|egrep|sed|head|tail|tailf)\"\~   
:msg, ereregex, "\\"(sleep|ls|expr|nohup|date|cat|du|dirname|tar|gzip|df|sg persist|ip)\"\~   
:msg, ereregex, "\\"(basename|hostname|readlink|bc|touch|dmesg)\"\~   
:msg, ereregex, "\\"(consoles type|blkid|lsblk)\"\~   
:msg, ereregex, "\(type=PATH)\" \~   
:msg, ereregex, "\(key=\\"exec\"'|type=EXECVE)" @10.1.250.71:514   
:msg, ereregex, "\(type=(PATH|SYSCALL|EOE)" \~   
:msg, ereregex, "\(cwd=\\"/home\omm"\~   
:msg, ereregex, "\(cwd=\\"/opt\huawei\Bigdata\nodeagent"\~ 
```

```batch
:msg, ereregex, "cwd=\\"Vopt\Vlinuxmon\Vtsagent" ~  
:msg, ereregex, "cwd=\\"Vopt\Vhuawei\VBigdata\VFusionInsight.*\\\\kerberos\Vscripts" ~ 
```

RHEL7 版本的操作系统，在/etc/rsyslog.conf 文件中作如下配置：

修改如下内容：

```txt
*.info;mail.full;mail.full2.full 
```

添加如下内容：

```powershell
$imjournalRatelimitInterval 0
$imjournalRatelimitBurst 0
auth, authpriv, cron.info @10.1.250.71:514 
```

在/etc/systemd/journald.conf 文件中添加如下内容：

```txt
RateLimitInterval=0  
RateLimitBurst=0 
```

在/etc/rsyslog.d/目录添加 audit_filter.conf 文件，并在文件中添加如下内容：

```javascript
:msg, ereregex, "(bin|sbin|sa)\\/(ping|top|mpstat|iostat|iotop|vmstat|sar|sadc|sh)\\"~   
:msg, ereregex, " (sbin|udev)\\/(fstab-import|udisks-part-id|path_id|edd_id|scsi_id)\\"~   
:msg, ereregex, " (bin|sbin)\\/(tr|sort|wc|cut|awk|gawk|grep|fgrep|egrep|sed|head|tail|tailf)\\"~   
:msg, ereregex, " (bin|sbin)\\/(sleep|ls|expr|nohup|date|cat|du|dirname|tar|gzip|df|sgpersistip)\\"~   
:msg, ereregex, " (bin|sbin)\\/(basename|hostname|readlink|bc|touch|dmesg)\\"~   
:msg, ereregex, " (bin|sbin)\\/(console type|blkid|lsblk)\\"~   
:msg, ereregex, "\\"(ping|top|mpstat|iostat|iotop|vmstat|sar|sadc|sh)\\"~   
:msg, ereregex, "\\"(fstab-import|udisks-part-id|path_id|edd_id|scsi_id)\\"~   
:msg, ereregex, "\\"(tr|sort|wc|cut|awk|gawk|grep|fgrep|egrep|sed|head|tail|tailf)\\"~   
:msg, ereregex, "\\"(sleep|ls|expr|nohup|date|cat|du|dirname|tar|gzip|df|sgpersistip)\\"~   
:msg, ereregex, "\\"(basename|hostname|readlink|bc|touch|dmesg)\\"~   
:msg, ereregex, "\\"(console type|blkid|lsblk)\\"~ 
```

```batch
:msg, ereregex, "(type=PATH)" ~  
:msg, ereregex, "(key=\\"exec\"|type=EXECVE)" @10.1.250.71:514  
:msg, ereregex, "type=(PATH|SYSCALL|EOE)" ~  
:msg, ereregex, "cwd=\\"home\omm" ~  
:msg, ereregex, "cwd=\\"Vopt\Vhuawei\VBigdata\Vnodeagent" ~  
:msg, ereregex, "cwd=\\"Vopt\Vlinuxmon\Vtsagent" ~  
:msg, ereregex, "cwd=\\"Vopt\Vhuawei\VBigdata\VFusionInsight.*\\\\kerberos\scripts" ~ 
```

# 3. 启动 audit 和 syslog/rsyslog 服务

启动审计服务：

 在 RedHat Enterprise Linux Server 6 上:

```txt
service auditid start #若更改了配置文件则使用restart 替换 start #chkconfig auditid on
```

 在 RedHat Enterprise Linux Server 7 上:

```txt
service auditid.service restart #若更改了配置文件则使用restart替换start #systemctl enable auditid.service 
```

启动日志服务服务：

 在 RedHat Enterprise Linux Server 6 上:

```txt
service rsyslog start #若更改了配置文件则使用restart替换start#chkconfig rsyslog on
```

 在 RedHat Enterprise Linux Server 7 上:

```txt
systemctl start rsyslog.service #若更改了配置文件则使用restart 替换 start  
#systemctl enable rsyslog.service  
#systemctl start systemd-journald.service #若更改了配置文件则使用restart 替换 start 
```

# 6.23 账户安全

1. 根据应用的要求，增加应用账户，比如下面示例：

<table><tr><td>应用平台用
户</td><td>用户
ID</td><td>组名</td><td>组ID</td><td>备注</td><td>家目录</td><td>shell</td></tr><tr><td>sysread</td><td></td><td>sysread</td><td></td><td>密码不过期</td><td>/home/
sysread</td><td>/bin/bash</td></tr><tr><td>shucl</td><td></td><td>nfadmin</td><td></td><td></td><td>/home/shucl</td><td>/bin/bash</td></tr><tr><td>zhouss</td><td></td><td>nfadmin</td><td></td><td></td><td>/home/zhouss</td><td>/bin/bash</td></tr><tr><td>patrol</td><td></td><td>nfadmin</td><td></td><td>密码不过期</td><td>/home/patrol</td><td>/bin/bash</td></tr><tr><td></td><td></td><td>nfadmin</td><td></td><td>sudo all
Noppasswd</td><td></td><td></td></tr></table>

2. 系统默认的用户账户不建议进行删除。系统默认的用户账户被系统用于进行对各种系统自有进程的控制操作中，误删除将有可能导致一些受影响的系统进程出现启动，运行或关闭过程中的异常。系统默认的用户账户已经经过系统建议的安全设置配置，在无人为修改的前提下能够保证系统主机的安全访问控制。  
3. 除root用户外，系统其他的默认用户的登录shell均为非交互式登录shell，不应修改系统默认账户的登录shell的属性。  
4. 在系统集成和应用规划时，对账户的管理必须达到如下要求：

系统不存在无用的账号；  
所有系统的账号均可更改；  
. 一般情况不允许将各类账号/口令的明文存储在文件中，除非受到技术限制（如只能通过文件存放明文）；  
必须对密码限制，包括时效限制(口令每90天修改一次)、复杂程度限制(长度最少8位)、

非空限制、重复使用次数限制(不得使用5次之内重复的密码)。详见第6.13节。

5. 如非特殊需要，应用管理员需要以应用账号登陆，需要使用特权指令时，使用sudo权限。使用以下方法来配置sudo权限：

```txt
# visudo 
```

例如：赋予oracle用户使用fdisk命令的权限，在visudo命令打开的配置文件最后添加：

#创建 alias PRIVUSERS 然后添加 sudo 用户 oracle，这样可以使多个用户有相同的权限

User_Alias PRIVUSERS $=$ oracle

#创建 alias PRIVSERVICES 这样便于以后可以添加多个命令

Cmnd_Alias PRIVSERVICES $=$ /sbin/fdisk

#指定之前创建的alias给指定的用户/用户组

PRIVUSERS ALL $=$ (ALL) PRIVSERVICES

sudo 使用方法:

以 oracle 用户在运行命令前加 sudo，然后输入 oracle 用户的密码（非 root 密码）

```txt
oracle\$ sudo /sbin/fdisk -l 
```

# 6.24 补丁安装规范

1. 所有的 Linux 服务器应向配置红帽 yum 源补丁仓库；  
2. 对于新部署的Linux服务器，推荐更新到最新的补丁版本，以保证系统的安全稳定运行；  
3. 对于已经稳定运行的环境，各种类型的补丁更新应达到以下要求：

对于致命级别的安全漏洞补丁，应立即更新；  
对于bug修复类补丁，若涉及到的模块满足bug触发条件，应及时更新，其他情况则建议1个月内进行更新；  
对于功能增强型补丁，建议每6个月更新一次，间隔时间不宜过长或过短；

4. 若补丁是内核补丁，安装时应保留原内核内容，避免出现安装失败后无法进入系统的情况；若是其他补丁，则建议安装时替换原内容。

对于升级过内核的机器，要确保下一次启动将使用新内核启动，默认情况下，新安装的内核会排在第一位，且默认启动使用的内核为第一个内核，该设置在/boot/grub/grub.conf文件中（RHEL7使用grub2-set-default命令设置），如无特殊需求，不应修改。

5. 若由于应用需求要立即安装相关补丁，建议首先搭建测试环境，在测试环境中进行更新测试，

测试通过后再在生产环境更新；

# 7.1 日常巡检

# 7.1.1 内存管理

# 1) 如何查看系统内存状态

使用 free 命令列出当前内存使用状况

```txt
$ free
total used free shared buffers cached
Mem: 4040360 4012200 28160 0 176628 3571348
-/+ buffers/cache: 264224 3776136
Swap: 4200956 0 4200956 
```

使用vmstat查看swap列看是否在频繁使用swap分区

```txt
vmstat 15   
procs memory--- --swap-- ---io--- --system--- --cpu----   
r b swpd free buff cache si so bi bo in cs us sy id wa st   
0 0 0 1749492 9632 60716 0 0 76 2 45 47 0 1 98 0 0   
0 0 0 1749492 9632 60736 0 0 0 0 32 28 0 0 100 0 0 
```

# 2) 正常情况

```txt
used free  
-/+ buffers/cache: 264224 3776136 
```

当-/+ buffers/cache 这行 free 列的值大于总内存的 $20 \%$ ，并且si加上so无大量I/O操作（少于 1000）

# 3) 报警

当 $- / +$ buffers/cache 这行 free 列的值小于总内存的 $20 \%$ ，但 Swap 这行的 used 列小于总swap 的 $30 \%$ ，并且 si 加上 so 无大量 I/O 操作（少于 3000）。

# 4) 紧急情况

当 $- / +$ buffers/cache 这行 free 列的值小于总内存的 $10 \%$ ，或者Swap这行的used列大于总swap 的 $30 \%$ ，或者 si 加上 so 有大量 I/O 操作（大于 3000）。

# 5) 内存过少处理办法

执行 top 命令，然后按'shift $\cdot \mathsf { m }$ 按照内存使用率排列来找出占用内存过多的应用：

```csv
$ top
top -07:35:42 up 14 min, 2 users, load average: 0.00, 0.00, 0.00
Tasks: 78 total, 1 running, 77 sleeping, 0 stopped, 0 zombie
Cpu(s): 0.0%us, 1.4%sy, 0.0%ni, 98.6%id, 0.0%wa, 0.0%hi, 0.0%si, 0.0%st
Mem: 1922428k total, 172572k used, 1749856k free, 9212k buffers
Swap: 4128764k total, 0k used, 4128764k free, 60716k cached
PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND 
```

```txt
1293 root 20 0 96328 4432 3456 S 0.0 0.2 0:00.35 sshd  
1228 postfix 20 0 81592 3844 2928 S 0.0 0.2 0:00.02 qmgr  
1217 root 20 0 81328 3816 2872 S 0.0 0.2 0:00.04 master  
1227 postfix 20 0 81408 3808 2892 S 0.0 0.2 0:00.20 pickup  
1268 root 18 -2 12392 2620 548 S 0.0 0.1 0:00.00 udevd  
1269 root 18 -2 12392 2616 544 S 0.0 0.1 0:00.01 udevd 
```

# 7.1.2 CPU 使用率

# 1) 如何查看系统CPU使用情况

执行 top 命令，然后按'shift $\cdot + \mathsf { p ^ { \prime } }$ 按照 CPU 使用率排列来查看应用 CPU 使用率：

```csv
$ top
top -07:47:33 up 26 min, 2 users, load average: 0.00, 0.00, 0.00
Tasks: 78 total, 1 running, 77 sleeping, 0 stopped, 0 zombie
Cpu(s): 1.8%us, 0.0%sy, 0.0%ni, 98.2%id, 0.0%wa, 0.0%hi, 0.0%si, 0.0%st
Mem: 1922428k total, 173068k used, 1749360k free, 9632k buffers
Swap: 4128764k total, 0k used, 4128764k free, 60744k cached
PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
7 root 20 0 0 0 0 S 1.8 0.0 0:01.11 events/0
1326 root 20 0 15012 1244 972 R 1.8 0.1 0:00.01 top
1 root 20 0 19232 1508 1216 S 0.0 0.1 0:00.67 init
2 root 20 0 0 0 0 S 0.0 0.0 0:00.00 kthreadadd
3 root RT 0 0 0 0 S 0.0 0.0 0:00.00 migration/0 
```

执行 mpstat 命令，查看是否 kernel 或者 I/O 占用了 CPU 时间：

```batch
# mpstat 15 Linux 2.6.32-504.el6.x86_64 (host.example.com) 04/09/2015 _x86_64_ (4 CPU) 07:59:15 AM CPU %usr %nice %sys %iowait %irq %soft %steal %guest %idle 07:59:16 AM all 0.00 0.00 0.00 0.00 0.00 0.00 0.00 100.00 07:59:17 AM all 0.00 0.00 0.00 0.25 0.00 0.00 0.00 99.75 07:59:18 AM all 0.00 0.00 0.00 0.00 0.25 0.00 0.00 99.75 
```

# 2) 正常情况

```txt
Cpu(s): 1.8%us, 0.0%sy, 0.0%ni, 98.2%id, 0.0%wa, 0.0%hi, 0.0%si, 0.0%st  
PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND  
7 root 20 0 0 0 0 S 1.8 0.0 0:01.11 events/0 
```

当 top 输出里 Cpu(s)行的%id 大于 $70 \%$ ，且 mpstat 的%sys 和%iowait 低于 $30 \%$ ，另外无进程长

时间占用 $100 \%$ ，则系统运行正常。

# 3) 报警

当 top 输出里 Cpu(s)行的%id 大于 $30 \%$ 小于 70%时，需对问题进行调查。

# 4) 紧急情况

当 top 输出里 Cpu(s)行的%id 小于 30%时，需立即处理。

# 5) CPU使用率高处理办法

如果 mpstat 的%us 较高，需检查应用。  
如果 mpstat 的%sys、%iowait 较高，需进行内核以及磁盘读写问题排查。

# 7.1.3 磁盘管理

使用df命令查看磁盘空间以及inode使用情况

# 查看磁盘空间

```txt
$ df -Th
Filesystem Type Size Used Avail Use% Mounted on
/dev/mapper/Rootvg-lv_root
ext4 50G 1.8G 45G 4% /
tmpfs tmpfs 939M 0 939M 0% /dev/shm
/dev/sda1 ext4 477M 33M 420M 8%/boot
/dev/mapper/Rootvg-lv_home
ext4 26G 45M 24G 1% /home 
```

# 查看 inode 使用情况

```txt
$ df -Ti
Filesystem Type Inodes IUsed IFree IUse% Mounted on
/dev/mapper/Rootvg-lv_root
ext4 3276800 79083 3197717 3% /
tmpfs tmpfs 240252 1 240251 1% /dev/shm
/dev/sda1 ext4 128016 42 127974 1% /boot
/dev/mapper/Rootvg-lv_home
ext4 1676080 57 1676023 1% /home 
```

# 1) 正常情况

磁盘空间和 inode 使用率都低于 $70 \text{‰}$ 。并且 dmesg 无文件系统报错。例如 ext4 error。

# 2) 报警

磁盘空间或 inode 使用率高于 $70 \%$ 低于 $90 \text{‰}$

dmesg存在文件系统报警。

# 3) 紧急情况

磁盘空间或inode使用率高于 $90 \text{‰}$ 。文件系统变只读无法进行写操作。

# 4) 磁盘问题处理办法

# 磁盘剩余空间少

使用du -sh命令对文件系统所有目录文件大小进行统计，并一级一级目录查找到占用大量

磁盘空间的文件，例如：

```txt
# df -h /home/   
Filesystem Size Used Avail Use% Mounted on   
/dev/mapper/Rootvg-lv_home 26G 4.2G 20G 18%/home   
# cd /home/   
# du -sh \*   
16K ftpadmin   
16K lost+found   
24K test   
4.1G user   
24K user1   
# cd user   
# du -sh\*   
4.1G shares   
4.0K tmp 
```

# inode 使用率高

删除或迁移不必要的文件。

# 文件系统只读

1. 备份数据  
2. 根据文件系统报错决定下一部操作  
3. 如果情况紧急，另外有完整备份可以卸载该文件系统，然后使用e2fsck进行文件系统检

查：

```txt
e2fsck<设备名> 
```

4. 如果修复失败，可以重建文件系统，并恢复备份数据。

# 7.1.4 系统负载

使用uptime命令查看系统当前负载，load average后的第一列反应的是过去1分钟、5分钟和

15分钟的负载。

```txt
uptime 
```

```txt
08:23:25 up 32 min, 1 user, load average: 0.00, 0.09, 0.07 
```

1) 正常情况

load average 三列的值小于 CPU 个数。

```batch
grep processor /proc/cpuinfo |wc -l 
```

2) 报警

load average 三列的值大于 CPU 个数但小于 CPU 个数的两倍。

3) 紧急情况

load average 三列的值大于 CPU 个数的两倍。

4) 负载过大处理办法

检查CPU使用率，并参照其处理方法操作。

# 7.1.5 网络

使用 ifconfig 命令查看是否存在丢包

```txt
ifconfig   
bond0 Link encaps:Ethernet HWaddr 08:00:27:85:FB:BE inlet addr:192.168.56.102 Bcast:192.168.56.255 Mask:255.255.255.0 inlet6 addr:fe80::a00:27ff:fe85:fbbe/64 Scope:Link UP BROADCAST RUNNING MASTER MULTICAST MTU:1500 Metric:1 RX packets:1940 errors:0 dropped:0 overruns:0 frame:0 TX packets:1169 errors:0 dropped:0 overruns:0 carrier:0 
```

collisions:0 txqueuelen:0

RX bytes:189594 (185.1 KiB) TX bytes:152740 (149.1 KiB)

# 使用 ping 命令检查网络

# ping -c3 192.168.56.1

PING 192.168.56.1 (192.168.56.1) 56(84) bytes of data.

64 bytes from 192.168.56.1: icmp_seq $^ { = 1 }$ tt $\yen 128$ time $= 0 . 3 1 9$ ms

64 bytes from 192.168.56.1: icmp_seq $^ { = 2 }$ tt $\yen 128$ time=0.282 ms

64 bytes from 192.168.56.1: icmp_seq $^ { = 3 }$ tt $\yen 128$ time=0.296 ms

--- 192.168.56.1 ping statistics ---

3 packets transmitted, 3 received, $0 \%$ packet loss, time 2000ms

rtt min/avg/max/mdev = 0.282/0.299/0.319/0.015 ms

# 使用ethtool查看物理连接

# ethtool eth0

Settings for eth0:

Supported ports: [ TP ]

Supported link modes: 10baseT/Half 10baseT/Full

100baseT/Half 100baseT/Full

1000baseT/Full

Supported pause frame use: No

Supports auto-negotiation: Yes

Advertised link modes: 10baseT/Half 10baseT/Full

<table><tr><td>100baseT/Half 100baseT/Full</td></tr><tr><td>1000baseT/Full</td></tr><tr><td>Advertised pause frame use: No</td></tr><tr><td>Advertised auto-negotiation: Yes</td></tr><tr><td>Speed: 1000Mb/s</td></tr><tr><td>Duplex: Full</td></tr><tr><td>Port: Twisted Pair</td></tr><tr><td>PHYAD: 0</td></tr><tr><td>Transceiver: internal</td></tr><tr><td>Auto-negotiation: on</td></tr><tr><td>MDI-X: off (auto)</td></tr><tr><td>Supports Wake-on: umbg</td></tr><tr><td>Wake-on: d</td></tr><tr><td>Current message level: 0x00000007 (7)</td></tr><tr><td>drv probe link</td></tr><tr><td>Link detected: yes</td></tr></table>

# 1) 正常情况

ifconfig 的 erros，dropped，overruns 和 frame 都是 0。  
ping 无丢包和延时。  
ethtool 显示 Link detected: yes 以及 Advertised link modes 为正确的千兆或者百兆

# 2) 报警

ifconfig 的 erros，dropped，overruns 和 frame 有 1000 以下的报错。  
ping有低延时或者少量丢包。  
ethtool 显示 Link detected: yes 但 Advertised link modes 非正确的千兆或者百兆

# 3) 紧急情况

ifconfig 的 erros，dropped，overruns 和 frame 大于 1000 的报错。  
ping 延时高以及大量丢包。  
ethtool 显示 Link detected: no

# 4) 网络问题处理方法

ethtool 显示不对，先检查好物理网络  
使用 ping 去测试其他网段和其他机器，排除是否网络问题  
如果 ifconfig 有 error 检查网络、网卡和网卡驱动。

# 7.1.6 系统运行时间

使用 uptime 命令查看系统运行时间

# uptime

08:23:25 up 32 min, 1 user, load average: 0.00, 0.09, 0.07

 如果系统无故重启，但没有频繁重启，收集系统日志于工作时间并联系红帽工程师。

如果系统频繁重启，按照以下步骤排错：

 查看是否由 kernel panic 引起，可以看 console 或者查看/var/crash 下是否有 vmcore  
 如果是 Oracle RAC 集群，检查是否 Oracle RAC 重启了机器  
 检查硬件日志

# 7.2 逻辑卷管理

LVM（Logical Volume Manager）逻辑卷管理是 Linux 环境下对磁盘分区进行管理的一种机制，LVM 是建立在硬盘和分区之上的一个逻辑层，来提高磁盘分区管理的灵活性。通过LVM 系统管理员可以轻松管理磁盘分区。

# 7.2.1 基本术语

1) 物理存储介质（PhysicalStorageMedia）

指系统的物理存储设备：磁盘，如：/dev/hda、/dev/sda等，是存储系统最底层的存储单元。

2) 物理卷（Physical Volume，PV）

指磁盘分区或从逻辑上与磁盘分区具有同样功能的设备（如RAID），是LVM的基本存储逻辑块，但和基本的物理存储介质（如分区、磁盘等）比较，却包含有与LVM相关的管理参数。

3) 卷组（Volume Group，VG）

类似于非LVM系统中的物理磁盘，其由一个或多个物理卷PV组成。可以在卷组上创建一个或多个 LV（逻辑卷）。

4) 逻辑卷（Logical Volume，LV）

类似于非LVM系统中的磁盘分区，逻辑卷建立在卷组VG之上。在逻辑卷LV之上可以建立文件系统（比如/home或者/usr等）。

5) 物理块（Physical Extent，PE）

每一个物理卷PV被划分为称为PE（Physical Extents）的基本单元，具有唯一编号的PE是可以被LVM寻址的最小单元。PE的大小是可配置的，默认为4MB。所以物理卷（PV）由大小等同的基本单元PE组成。

6) 逻辑块（Logical Extent，LE）

逻辑卷LV也被划分为可被寻址的基本单位，称为LE。在同一个卷组中，LE的大小和PE是相同的，并且一一对应。

简单来说：一个或多个 PV 组成 VG，VG 可以划分为一个或多个 LV。

# 7.2.2 命令描述

命令及参数说明

<table><tr><td>命令</td><td>命令及参数描述</td></tr><tr><td>pvcreate</td><td>用于创建物理卷。</td></tr><tr><td>vgcreate</td><td>用于创建逻辑卷组。</td></tr><tr><td>lvcreate</td><td>用于创建逻辑卷。</td></tr><tr><td>vgextend</td><td>用于扩展逻辑卷组。</td></tr><tr><td>lvextend</td><td>用于扩展逻辑卷。</td></tr><tr><td>resize2fs</td><td>用于扩展ext3或者ext4类型的文件系统。</td></tr><tr><td>xfsgrowfs</td><td>用于扩展xfs类型的文件系统。</td></tr><tr><td>mkfs.ext4</td><td>用于将逻辑卷或者分区格式化为ext4类型文件系统</td></tr><tr><td>mkfs.xfs</td><td>用于将逻辑卷或者分区格式化为xfs类型文件系统</td></tr><tr><td>pvdisplay</td><td>显示物理卷PV信息</td></tr><tr><td>vgdisplay</td><td>显示卷组VG信息</td></tr><tr><td>lvdisplay</td><td>显示逻辑卷LV信息</td></tr><tr><td>lvreduce</td><td>减小逻辑卷</td></tr><tr><td>vgreduce</td><td>减小卷组</td></tr><tr><td>pvmove</td><td>移动物理卷上的数据至其他物理卷上</td></tr><tr><td>pvremove</td><td>移除物理卷</td></tr><tr><td>e2fsck</td><td>检查文件系统</td></tr></table>

# 7.2.3 配置 LVM

使用普通分区配置LVM，首先要将普通分区转换为lvm的分区形式，再将普通分区创建为物理卷，再将物理卷创建为逻辑卷组，最后使用逻辑卷组创建逻辑卷。

以磁盘/dev/sdc为例进行说明，在实际使用过程中，请使用实际设备名称代替/dev/sdc。

磁盘/dev/sdc 大小为 100GB。

# 7.2.4 创建分区

1 使用root用户登录服务器。  
2 执行以下命令，创建磁盘 label。

```batch
parted -s /dev/sdc mklabel msdos 
```

3 执行以下命令，查看磁盘分区信息，获取新建分区的起始位置。

```txt
parted/dev/sdc print 
```

4 执行以下命令，创建分区。

```txt
parted -s --align cylinder <设备名称> mkpart primary <文件系统类型> <起始位置> <结束位置>
```

例如：设备名称为/dev/sdc，新建分区的起始位置为512B，将磁盘的空间全部分配给新建的分区，因此，新建分区的结束位置为107GB，使用的文件系统类型为ext4。

```txt
parted -s --align cylinder /dev/sdc mkpart primary ext4 512B 107GB 
```

5 执行以下命令，使用新建的分区生效。

```txt
partx/dev/sdc
```

6 执行以下命令，查看新建的分区。

```txt
parted/dev/sdc print 
```

磁盘/dev/sdc 只有一个分区，因此，新建分区的编号为 1。

7 执行以下命令，设置新建分区为 LVM 类型。

```txt
parted/dev/sdc set 1 lvm on 
```

在实际使用过程中，请使用实际设备名称代替/dev/sdc 和分区编号 1。

8 执行以下命令，使设置生效。

```batch
partx -a /dev/sdc 
```

9 执行以下命令，查看新建分区的设置，如下图所示，分区为 LVM 类型。

```txt
parted/dev/sdc print 
```

# 7.2.5 创建 PV

以分区/dev/sdc1 为例进行说明。实际使用过程中，请使用实际分区代替/dev/sdc1。

1 执行以下命令，将磁盘分区创建为物理卷PV。

```txt
# pvcreate /dev/sdc1 
```

# 7.2.6 创建 VG

以物理卷/dev/sdc1，创建的卷组名是Rootvg为例进行说明。实际使用过程中，请使用实际分区代替/dev/sdc1。

1 执行以下命令，创建 VG。

```txt
vgcreate Rootvg /dev/sdc1 
```

# 7.2.7 扩展 VG

以物理卷/dev/sdc1，需要扩展的卷组名是Rootvg为例进行说明。实际使用过程中，请使用实际分区代替/dev/sdc1。

1 执行以下命令，创建VG。

```txt
vgextend Rootvg /dev/sdc1 
```

# 7.2.8 创建 LV

以卷组名是Rootvg，lv的名称是lv_data为例进行说明。实际使用过程中，请使用实际卷组名称和逻辑卷名称代替 Rootvg 和 lv_data。

1 执行以下命令，创建 LV。

```batch
lvcreate -L +100M -n lv_data Rootvg 
```

至此，LVM的配置过程已全部完成。若要使用逻辑卷，需要将其格式化为文件系统，请参考章节 Error: Reference source not found "Error: Reference source not found"。

# 7.2.9 扩展 LV

以卷组名是 Rootvg，lv 的名称是 lv_data，lv 扩展 1GB 为例进行说明。实际使用过程中，请使用实际卷组名称和逻辑卷名称代替 Rootvg 和 lv_data。

1 执行以下命令，扩展LV。

```batch
lvextend -L +1G /dev/Rootvg/lv_data 
```

至此，lv的扩展操作已经完成。因逻辑卷 lv_data已经被格式化为文件系统来使用，因此，还需要扩展文件系统，才能正常使用扩展的逻辑卷的空间，请参考章节 Error: Referencesource not found "Error: Reference source not found"。

# 7.2.10创建文件系统

以卷组名是Rootvg，lv的名称是lv_data，挂载点是/data，文件系统类型是ext4为例进行说明。实际使用过程中，请使用实际卷组名称、逻辑卷名称、挂载点、文件系统类型代替 Rootvg、lv_data、/data、ext4。

1 执行以下命令，格式化 lv 为文件系统。

```txt
mkfs.ext4 /dev/Rootvg/lv_data 
```

2 执行以下命令，创建挂载点。

```markdown
# mkdir /data 
```

3 执行以下命令，挂载逻辑卷。

```txt
# mount -o rw,acl /dev/mapper/Rootvg-lv_data /data 
```

4 执行以下命令，修改/etc/fstab文件，使新建的文件系统随开机启动。

# 7.2.11扩展文件系统

以卷组名是 Rootvg，lv 的名称是 lv_data，文件系统类型是 ext4 为例进行说明。实际使用过程中，请使用实际卷组名称、逻辑卷名称代替 Rootvg、lv_data。

1 执行以下命令，修改/etc/fstab 文件，使新建的文件系统随开机启动。

```txt
# resize2fs /dev/Rootvg/lv_data 
```

![](images/7992d09f32de3569ff61b567a0c20241a0c1f5e693fccad22d930a0d071a0a67.jpg)

说明

若为 xfs 类型文件系统，须使用命令 xfs_growfs 对文件系统进行扩展。  
xfs 类型文件系统，只能扩展，不能缩小。

# 7.3 系统服务配置

# 7.3.1 rsync

1) 概述

rsync（Remote Sync）是类 Unix 系统下的数据镜像备份工具。一款快速增量备份工具，远程同步支持本地复制，或者与其他 SSH，rsync 主机同步。

2) 特点

可以镜像保存整个目录树和文件系统。

可以很容易做到保持原来文件的权限、时间、软硬链接等等。

无须特殊权限即可安装。

快速：第一次同步时 rsync 会复制全部内容，但在下一次只传输修改过的文件。rsync 在传输数据的过程中可以实行压缩及解压缩操作，因此可以使用更少的带宽。

安全：可以使用scp、ssh等方式来传输文件，当然也可以通过直接的socket连接。

支持匿名传输，以方便进行网站镜象。

# 3) 命令说明

表 1 命令选项说明  

<table><tr><td>选项</td><td>说明</td></tr><tr><td>-a</td><td>归档模式,相当于-rlptgoD</td></tr><tr><td>-r</td><td>递归,对子目录以递归模式处理</td></tr><tr><td>-l</td><td>拷贝链接文件</td></tr><tr><td>-p</td><td>保留文件权限</td></tr><tr><td>-t</td><td>保留文件时间</td></tr><tr><td>-g</td><td>保留文件拥有组</td></tr><tr><td>-o</td><td>保留文件拥有者</td></tr><tr><td>-D</td><td>拷贝块设备文件</td></tr><tr><td>-z</td><td>传输时压缩</td></tr><tr><td>-P</td><td>传输进度</td></tr><tr><td>-v</td><td>详细模式输出</td></tr><tr><td>-q</td><td>精简模式输出</td></tr></table>

表 2 配置文件参数说明  

<table><tr><td>-c</td><td>强制对文件传输进行效验</td></tr><tr><td>-b</td><td>创建备份，对已经存在的同名文件名，将老文件重命名为filename~，可以使用--suffix 选项来指定不同的备份文件前缀</td></tr><tr><td>--backup-dir</td><td>将备份文件存放在目录</td></tr><tr><td>-u</td><td>仅更新，跳过所有已经存在 DEST，且文件时间要晚于要备份的文件</td></tr><tr><td>-L</td><td>像对待常规文件一样处理软连接</td></tr><tr><td>-H</td><td>保留硬链接</td></tr><tr><td>-A</td><td>保留acl 权限</td></tr><tr><td>-W</td><td>不做增量检查，直接做全备</td></tr><tr><td>-e</td><td>指定使用 rsh, ssh 方式进行数据同步</td></tr><tr><td>--list-only</td><td>列出服务器上提供的同步内容</td></tr><tr><td>--delete</td><td>删除那些 DEST 中 SRC 没有的文件</td></tr><tr><td>--progress</td><td>显示备份过程，百分比</td></tr><tr><td>--password-file</td><td>指定密码文件，在使用 crontab 自动同步时比较有用</td></tr><tr><td>--existing</td><td>仅同步 DEST 中已经存在的文件，不同步 SRC 中的新文件</td></tr><tr><td>全局参数</td><td>说明</td></tr><tr><td>motd file</td><td>定义服务器信息，需自己编辑，默认没有，也可不配置</td></tr><tr><td>pid file</td><td>PID文件，默认没有，一般指定为：/var/run/rsyncd.pid</td></tr><tr><td>port</td><td>端口，默认指定为873</td></tr><tr><td>address</td><td>指定服务器IP地址</td></tr><tr><td>模块参数</td><td>说明</td></tr><tr><td>comment</td><td>描述信息，自定义</td></tr><tr><td>path</td><td>需要同步的目录路径</td></tr><tr><td>use chroot</td><td>如果为yes，rsync进程将chroot到文件系统中的目录中，好处是保护系统被安装漏洞侵袭的可能。缺点是需要超级用户权限。另外对符号链接文件，将会排除在外。</td></tr><tr><td>max connetions</td><td>允许客户端最大链接数，0表示无限制</td></tr><tr><td>log file</td><td>日志文件，一般设定为：/var/log/rsync.log</td></tr><tr><td>lock file</td><td>锁文件，用来记录最大连接数，默认是/var/run/rsyncd.lock</td></tr><tr><td>read only</td><td>只读，默认为yes，表示不让客户端上传文件到服务器</td></tr><tr><td>write only</td><td>只写，默认为no，表示客户端可以下载文件，yes表示不能下载</td></tr><tr><td>list</td><td>列出服务器上提供同步的数据目录，默认为yes</td></tr><tr><td></td><td></td></tr><tr><td>uid</td><td>服务器传输文件时使用哪个用户执行，默认是 nobody，如果遇到权限文件，可能需要 root 用户</td></tr><tr><td>gid</td><td>服务器传输文件时使用哪个用户组执行，默认是 nobody</td></tr><tr><td>exclude</td><td>排除不需要同步的目录或文件，多个用空格隔开</td></tr><tr><td>auth users</td><td>认证用户，必须是服务器上存在的用户</td></tr><tr><td>secrets file</td><td>指定密码文件路径</td></tr><tr><td>strict modes</td><td>是否检查密码文件权限，拥有组和其他人必须为 0</td></tr><tr><td>hosts allow</td><td>允许哪些地址可以同步，可以是 IP 或网段，多个用空格隔开</td></tr><tr><td>hosts deny</td><td>拒绝哪些地址的同步，可以是 IP 或网段，多个用空格隔开</td></tr><tr><td>ignore errors</td><td>忽略 IO 错误</td></tr><tr><td>log format</td><td>日志格式</td></tr><tr><td>timeout</td><td>超时时间</td></tr></table>

# 4) 安装 rsync

rsync 安装很简单，不管是同步端机器还是被同步端机器，都只需安装 rsync 包既可，如果配置了 yum 源，可直接使用 yum 安装，命令如下：

# yum -y install rsync

# 5) 启动 rsync

启动 rsync 的方法很简单，有以下两种方法，推荐使用第二种方法：

方法一：--daemon 参数方式，是让 rsync 以服务器模式运行，命令如下：

启动

```shell
#/usr/bin/rsync --daemon --config=/etc/rsyncd.conf
```

查看端口

```txt
netstat -tulnp | grep rsync 
```

```batch
tcp 0 0 0.0.0.0:873 0.0.0.0:* LISTEN 27064/rsync 
```

```batch
tcp 0 0::873 :LISTEN 27064/rsync 
```

注释：--config 用于指定 rsyncd.conf 的位置，如果默认在/etc 目录下默认可以不用指

定

方法二：xinetd 监管，只需将/etc/xinetd.d/rsync 文件中的 disable $=$ yes 改为 no 即可，如

下：

# default: off

# description: The rsync server is a good addition to an ftp server, as it \

# allows crc checksumming etc.

service rsync

{

disable $=$ no #将 yes 改为 no

flags = IPv6

socket_type $=$ stream

wait = no

```hcl
user = root  
server = /usr/bin/rsync  
server_args = --daemon  
log_on_failure += USERID 
```

然后启动 xinetd 服务

```txt
service xinetd start Starting xinetd:[ OK ] 
```

查看端口，会发现 rsync 并没有监听，但是 xinetd 监听了 873 端口

```txt
netstat -tulnp | grep rsync   
# netstat -tulnp | grep 873   
tcp 0 0::873 :LISTEN 28245/xinetd 
```

修改/etc/xinetd.d/rsync 主要是要打开 rsync 这个 daemon, 一旦有 rsync client 要连接时,

xinetd 会把它转移给 rsyncd(port 873)

6) rsync 工作模式

rsync有三种不同的工作模式：

1、本地

语法：

rsync [OPTION]... SRC [SRC]... DEST

注释：从本地目录复制到本地目录，前面为源目录，后面为目标目录

# 2、远程 shell

语法：

rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST

注释：上传，从本地目录同步至远程目录

rsync [OPTION]... [USER@]HOST:SRC [DEST]

注释：下载，从远程目录同步至本地目录

# 3、rsync 进程

语法：

rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST

rsync [OPTION]... SRC [SRC]... rsync://[USER@]HOST[:PORT]/DEST

注释：上传，从本地目录同步至远程目录，两种写法效果一样

rsync [OPTION]... [USER@]HOST::SRC [DEST]

rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]

注释：下载，从远程目录同步至本地目录，两种写法效果一样

# 7) 配置 rsync

rsync 的主配置文件为/etc/rsyncd.conf，该文件默认不存在，需手动创建。主配置文件中包含全局配置和若干个模块配置，一个目录对应一个模块配置。下面将讲述 rsync 使用自身 socket 和 ssh 协议传输文件的方法。

# 环境介绍：

主机名：test IP：172.168.0.10 （服务器）

主机名：remote IP：172.168.0.11 （备份端）

# 7.1) 使用 SSH 协议传输

使用 SSH 协议传输，rsync 不需要做任何配置，只需要备份端能 ssh 到服务器既可。下面将讲述将服务器上的/etc目录同步至备份端的/data目录

# 操作步骤：

# 7.1.1在备份端创建/data目录，命令如下：

```txt
[root@remote ~]# mkdir /data 
```

# 7.1.2同步数据，在备份端操作，命令如下：

```ini
[root@remote ~]# rsync -aze ssh root@172.168.0.10:/etc/data  
The authenticity of host '172.168.0.10 (172.168.0.10)' can't be established.  
RSA key fingerprint is b1:1c:7f:ae:d8:8d:05:e4:80:a0:35:5e:62:49:1b:c2.  
Are you sure you want to continue connecting (yes/no)?yes #输入 yes  
Warning: Permanently added '172.168.0.10' (RSA) to the list of known hosts.  
root@172.168.0.10's password: #输入服务器端 root 的密码  
[root@remote ~]# 
```

# 7.1.3检查数据是否被同步，如下：

```txt
[root@remote ~]# ls /data/  
etc  
[root@remote ~]# du -sh /data/etc/ 
```

7.1.4可以看到服务器上的/etc目录已经被同步过来，但是每次同步的时候都需要输入密码，

下面将配置 ssh 免密码传输。

7.1.5 在备份端生成一对 ssh 密钥，将公钥提供给服务器，命令如下：

生成密钥对

```txt
[root@remote ~]# ssh-keygen 
```

```txt
Generating public/private rsa key pair. 
```

```txt
Enter file in which to save the key (/root/.ssh/id_rsa): #回车 
```

```txt
Enter passphrase (empty for no passphrase): #回车 
```

```txt
Enter same passphrase again: #回车 
```

```txt
Your identification has been saved in /root/.ssh/id_rsa. 
```

```txt
Your public key has been saved in /root/.ssh/id_rsa.pub. 
```

```txt
The key fingerprint is: 
```

```txt
54:c2:5e:c0:48:04:ba:9c:46:dc:12:f1:8c:c8:68:69 root@remote 
```

```txt
The key's randomart image is: 
```

```markdown
+-[ RSA 2048]----+
```

```txt
0..+0+0.. 
```

```txt
oo.B .oo. 
```

$\left|oE^{\star} + \dots \right|$

```txt
00+ 
```

$\begin{array}{rlr}{\sf I} & = & {\sf S}\end{array}$

```txt
1. 
```

```txt
1 
```

```txt
1 1   
1 1   
+ 
```

将公钥提供给服务器

```txt
[root@remote ~]# ssh-copy-id -i /root/.ssh/id_rsa.pub 172.168.0.10 
```

```txt
root@172.168.0.10's password: 
```

```txt
输入服务器 root 密码
```

```txt
Now try logging into the machine, with "ssh '172.168.0.10"', and check in: 
```

```txt
.ssh/authorized_keys 
```

```txt
to make sure we haven't added extra keys that you weren't expecting. 
```

```txt
测试 
```

```txt
[root@remote ~]# ssh 172.168.0.10 
```

```txt
Last login: Wed Apr 8 16:28:56 2015 from 172.168.0.1 
```

```txt
[root@test ~]# 
```

```txt
成功登陆
```

7.1.6测试数据同步是否需要输入密码，先删除之前同步的数据，如下：

```txt
[root@remote ~]# rm -rf /data/* 
```

```txt
[root@remote ~]# rsync -ae ssh root@172.168.0.10:/etc /data 
```

```txt
[root@remote ~]# du -sh /data/* 
```

```txt
44M /data/etc 
```

同步成功，整个过程也没有提示输密码

7.2) 使用 rsync 自身 socket 传输

操作步骤：

7.2.1 生成配置文件/etc/rsyncd.conf，在服务器端操作，如下：

```txt
[root@test ~]# touch /etc/rsyncd.conf 
```

7.2.2 配置/etc/rsyncd.conf，如下：

```txt
Global Parameters #全局配置 
```

```txt
pid file = /var/run/rsyncd.pid #指定PID文件
```

```txt
port = 873 #指定端口
```

```txt
Module Parameters #模块配置 
```

```txt
[server_etc] #模块名称
```

path $=$ /etc #需要同步的目录的路径

```txt
list = yes #允许列出数据 
```

```txt
use chroot = no #不适用chroot 
```

```txt
uid = root #传输时使用 root 用户执行
```

```txt
gid = root #传输时使用 root 用户组执行
```

```txt
ignore errors #忽略IO错误 
```

```txt
log file = /var/log/rsync.log #指定日志文件
```

```txt
lock file = /var/run/rsync.lock #指定锁文件
```

```txt
max connections = 5 #最大连接数为5  
hosts allow = 172.168.0.11 #允许172.168.0.11同步  
hosts deny = * #拒绝所有 
```

7.2.3 启动 rsync 服务，命令如下：

```txt
[root@test ~]# rsync --daemon  
[root@test ~]# netstat -tulnp | grep rsync  
tcp 0 0 0.0.0.0:873 0.0.0.0:* LISTEN 6014/rsync  
tcp 0 0 :::873 :::* LISTEN 6014/rsync  
可以看到 rsync 已经监听 TCP 873 端口
```

7.2.4 在备份端查看服务器上有哪些数据能够被同步，如下：

```txt
[root@remote ~]# rsync --list-only 172.168.0.10:  
server_etc  
如果服务器端配置文件中 list = no，这里将看不到内容
```

还可以查看 server_etc 中有哪些数据，如下：

```txt
[root@remote ~]# rsync --list-only 172.168.0.10::server_etc  
drwxr-xr-x 12288 2015/04/08 22:50:55 .  
-rw----- 0 2013/08/01 17:49:13 .pwd.lock  
-rw-r--r-- 0 2013/08/07 22:12:29 .services.lock  
-rw-r--r-- 4439 2012/04/17 21:03:48 DIR COLORS  
-rw-r--r-- 5139 2012/04/17 21:03:48 DIR COLORS.256color
```

```txt
-rw-r--r-- 4113 2012/04/17 21:03:48 DIR COLORS.lightbgcolor  
-rw-r--r-- 45 2012/08/25 04:55:29 Trolltech.conf  
以下省略
```

7.2.5通过备份端来同步服务器端/etc目录至/data目录，命令如下：

```txt
需要在/data目录后面接一个目录，否则同步过来的文件将全部在/data目录下，若指定的目录不存在，rsync会自动创建。  
[root@remote ~]# rm -rf /data/*  
[root@remote ~]# rsync -az 172.168.0.10::server_etc /data/etc  
[root@remote ~]# du -sh *  
44M etc  
如果需要看到输出详细信息，可以加上-v选项，在命令的最后加上输出重定向，将结果保存到文件，如下：  
[root@remote ~]# rm -rf /data/*  
[root@remote ~]# rsync -avz 172.168.0.10::server_etc /data/etc &>  
/tmp/rsync.log
```

7.2.6 在这种情况下，没有提示输密码等操作，那就太不安全，任何能登陆到 172.168.0.10 上

的人都可以同步数据了，下面将讲述如何使用密码来控制同步。

7.2.7修改服务器端配置文件如下：

```txt
Global Parameters  
pid file = /var/run/rsyncd.pid  
port = 873 
```

Module Parameters   
[server_etc]   
path $=$ /etc   
list $=$ yes   
use chroot $=$ no   
uid $=$ root   
gid $=$ root   
ignore errors   
log file $=$ /var/log/rsync.log   
lock file $=$ /var/run/rsync.lock   
max connections $= 5$ hosts allow $= 172.168.0.11$ hosts deny $=$ \*   
secrets file $=$ /etc/rsyncd/secrets #指定密码文件   
strict modes $=$ yes #检查密码文件权限   
auth users $=$ root #指定认证用户为root

# 7.2.8 在服务器端创建密码文件，必须与配置文件中指定的相对应，如下：

```txt
[root@test ~]# echo "root:abc123" > /etc/rsyncd Secrets  
[root@test ~]# chmod 600 /etc/rsyncd secrets  
[root@test ~]# II /etc/rsyncd secrets  
-rw----- 1 root root 12 Apr 8 23:13 /etc/rsyncd secrets  
密码文件的格式是“用户名：密码”，一行对应一个，这里的用户必须是操作系统中已经存在的用户，密码与登陆操作系统的密码不相同，但是长度不能超过8个字符
```

# 7.2.9 使用账号密码来同步，如下：

[root@remote ~]# rm -rf /data/*

[root@remote ~]# rsync -az root@172.168.0.10::server_etc /data/etc

Password: #输入密码 abc123，即服务器/etc/rsyncd.secrets 中保存的密码

[root@remote ~]# du -sh /data/*

44M /data/etc

# 7.2.10 每次输入密码也很麻烦，特别是在配置计划任务的时候，rsync 有一个选项：--

password-file，这个参数是用来指定密码文件的，客户端密码文件保存的只有密码，没

有用户名，所以与服务器端密码文件/etc/rsyncd.secrets 不同，客户端密码文件保存的

就是服务端/etc/rsyncd.secrets 文件中某个用户的密码，当客户端同步服务端数据时，

指定--password-file 选项读取密码，而不用手动去输入，所以客户端每个密码文件中只

能有一个密码，不同的用户需要创建不同的密码文件，相同密码的用户可以使用一个密码

文件验证。如下：

在客户端创建密码文件/root/rsyncd.secrets，密码为 abc123，修改文件权限为

600，其他人无权限访问该文件

[root@remote ~]# echo "abc123" $>$ /root/rsyncd.secrets

[root@remote ~]# chmod 600 /root/rsyncd.secrets

# 7.2.11指定密码文件来同步数据

```txt
[root@remote ~]# rm -rf /data/* 
```

```txt
[root@remote ~]# rsync -az --password-file=/root/rsyncd.secrets 
```

```txt
root@172.168.0.10::server_etc /data/etc 
```

```txt
[root@remote ~]# du -sh /data/* 
```

```txt
44M /data/etc 
```

在此过程中，rsync 自动读取了/root/rsyncd.secrets 文件中的密码，然后通过验证

注释：服务器端/etc/rsyncd.secrets 和备份端/root/rsyncd.secrets 两个文件中的密码都和本

地用户登陆操作系统的密码无关，所以一般不用担心，为了更安全，可以把这两个文件设置

为隐藏文件。

# 8) 扩展

# 更改 Rsync 端口

1 由于 xinetd 服务运行时会忽略/etc/rsyncd.conf 文件中 port 参数，所以更

改/etc/rsyncd.conf 文件中的 port 是无效的，所以需要更改/etc/services 文件，如下：

# 更改

```batch
[root@test ~]#sed -i '/^rsync/s/873/8730/g' /etc/services 
```

```txt
sync 8730/tcp 
```

```txt
rsync 
```

```txt
sync 8730/udp 
```

```txt
rsync 
```

# 查看

```tcl
[root@test ~]#grep ^rsync /etc/services  
rsync 8730/tcp # rsync  
rsync 8730/tcp # rsync 
```

# 2 重新启动 xinetd 服务

```txt
[root@test ~]# service xinetd restart  
Stopping xinetd: [OK]  
Starting xinetd: [OK]  
[root@test ~]# netstat -tulnp | grep 8730  
tcp 0 0::8730 :::* LISTEN 42512/xinetd 
```

# 3 连接，客户端连接时需要用 --port 指定端口

```txt
不指定端口，连接拒绝  
[root@test ~]#rsync --list-only root@172.168.0.10::  
rsync: failed to connect to 172.168.0.10: Connection refused (111)  
rsync error: error in socket IO (code 10) at clientserver.c(124) [receiver=3.0.6]  
指定端口8730，连接成功  
[root@test ~]# rsync --list-only --port=8730 root@172.168.0.10::  
+++++**********  
Welcome to use the rsync services!  
+++++**********  
server_etc 
```

# 7.3.2 NFS

# 1) 概述

NFS（Network File System）即网络文件系统，它允许网络中的计算机之间通过 TCP/IP网络共享资源。在 NFS 的应用中，本地 NFS 的客户端应用可以透明地读写位于远端 NFS服务器上的文件，就像访问本地文件一样。

# 2) 特点

1. 节省本地存储空间，将常用的数据存放在一台NFS服务器上且可以通过网络访问，那么本地终端将可以减少自身存储空间的使用。  
2. 用户不需要在网络中的每个机器上都建有 Home 目录，Home 目录可以放在 NFS 服务器上且可以在网络上被访问使用。  
3. 一些存储设备如软驱、CDROM 和 Zip（一种高储存密度的磁盘驱动器与磁盘）等都可以在网络上被别的机器使用。这可以减少整个网络上可移动介质设备的数量。

# 3) RPC（Remote Procedure Call）

# 4) 命令及参数

表一 命令选项说明  

<table><tr><td>选项</td><td>说明</td></tr></table>

表二配置文件参数说明  

<table><tr><td>-a</td><td>全部挂载或卸载</td></tr><tr><td>-r</td><td>更新配置，重新读取/etc/exports</td></tr><tr><td>-u</td><td>卸载指定目录</td></tr><tr><td>-v</td><td>显示详细信息</td></tr></table>

<table><tr><td>参数</td><td>说明</td></tr><tr><td>ro</td><td>只读,最终还要看共享目录是否有读权限</td></tr><tr><td>rw</td><td>读写,最终还要看共享目录是否有读写权限</td></tr><tr><td>sync</td><td>数据同步写入硬盘</td></tr><tr><td>async</td><td>数据暂存于内存中,而非直接写入硬盘</td></tr><tr><td>secure</td><td>NFS 通过 1024 以下的安全 TCP/IP 端口发送(默认)</td></tr><tr><td>insecure</td><td>NFS 通过 1024 以上的 TCP/IP 端口发送</td></tr><tr><td>wdelay</td><td>多个用户对共享目录进行写操作时,则按组写入数据(默认)</td></tr><tr><td>no_wdelay</td><td>多个用户对共享目录进行写操作时,则立即写入数据</td></tr><tr><td>hide</td><td>不共享其子目录</td></tr><tr><td>no Hide</td><td>共享其子目录</td></tr><tr><td>subtree_check</td><td>强制 NFS 检查父目录的权限</td></tr><tr><td>no_subtree_check</td><td>不检查父目录权限（默认）</td></tr><tr><td>all_squash</td><td>任何访问者，都映射成匿名用户</td></tr><tr><td>root_squash</td><td>root用户访问，映射成匿名用户（默认）</td></tr><tr><td>no_root_squash</td><td>root用户访问，不映射成匿名用户</td></tr><tr><td>anonuid/anongid</td><td>指定匿名用户访问时的UID和GID，但是必须是/etc/passwd中已经存在的</td></tr></table>

# 5) 安装

安装 NFS 需要安装 RPC 主程序 rpcbind 和 NFS 主程序 nfs-utils，这两个程序一般在安装系统时都已经安装了，如果没有，使用一下命令安装即可：

```txt
yum -y install rpcbind nfs-utils 
```

# 6) 配置

# 6.1 配置文件

NFS 的配置文件为/etc/exports，这个文件默认是空的，格式如下：

<共享目录> 客户端 1(选项) [客户端 2(选项) ...]

共享目录：NFS共享给客户机的目录，必须是绝对路径。

客户端：网络中可以访问此目录的主机。多个客户端以空格分隔。主机可以用IP、网段、主机名、域名，主机名支持通配符。

选项：设置共享目录的访问权限、用户映射等，多个选项以逗号分隔。

# 6.2 配置示例

环境介绍：

主机名：test IP：172.168.0.10 （服务端）

主机名：remote IP：172.168.0.11 （客户端）

操作步骤：

# 6.2.1 在服务端创建共享目录，并赋予读写权限，如下：

[root@test ~]# mkdir /data

[root@test ~]# mkdir /home/data

[root@test ~]# chmod 777 /data

[root@test ~]# chmod 777 /home/data

如果不赋予目录读写权限，就算配置文件里给了读写权限，客户端也无法读写，

除非使用 root 用户访问共享目录，并且设定了 no_root_squash 参数

# 6.2.2 配置共享，修改/etc/exports 文件，内容如下：

/data 172.168.0.11(rw,no_root_squash)

/home/data 172.168.0.11(rw) 172.168.0.12(ro)

一行一个配置，共享目录与主机中间有空格，主机与参数之间没有空格，多个主

机之间用空格隔开，上面的配置表示将/data目录共享给172.168.0.11，对共享目

录具有读写权限，并且不将 root 用户映射成匿名用户，将/home/data 目录共享

给 172.168.0.11 和 172.168.0.12，172.168.0.11 具有读写权限，172.168.0.12 具有

只读权限

# 6.2.3 启动服务，先启动rpcbind，在启动nfs，如下：

[root@test ~]# service rpcbind start

[root@test ~]# service nfs start

如果需要开机启动，还需执行一下操作：

[root@test ~]# chkconfig rpcbind on

[root@test ~]# chkconfig nfs on

rpcbind默认已经是开启的，一般不需要对他操作

# 6.2.4 服务端查看，命令如下：

```txt
[root@test ~]# exportfs -v  
/data 172.168.0.11(rw,wdelay,no_root_squash,no_subtree_check)  
/home/data 172.168.0.11(rw,wdelay,root_squash,no_subtree_check)  
/home/data 172.168.0.12(ro,wdelay,root_squash,no_subtree_check) 
```

其中 wdelay，root_squash,no_subtree_check 都是默认选项

# 6.2.5 客户端查看，命令如下：

```txt
[root@remote ~]## showmount -e 172.168.0.10 Export list for 172.168.0.10: /home/data 172.168.0.12,172.168.0.11 /data 172.168.0.11 
```

客户端只能看到服务端将哪些目录共享给了哪些主机

# 6.2.6 客户端挂载，命令如下：

```txt
[root@remote ~]# mount -t nfs 172.168.0.10:/data /mnt  
[root@remote ~]# mount -t nfs 172.168.0.10:/home/data /media  
[root@remote ~]# df -h  
Filesystem Size Used Avail Use% Mounted on  
/dev/sda2 20G 3.7G 16G 20% /  
tmpfs 1000M 228K 1000M 1% /dev/shm  
/dev/sda1 194M 34M 151M 19% /boot  
172.168.0.10:/disk 15G 4.8G 9.3G 34% /mnt  
172.168.0.10:/home/data 504M 54M 425M 12% /media 
```

挂载 NFS 文件系统时，需用-tnfs 指定文件系统类型

# 6.2.7 客户端测试，命令如下：

分别在两个目录创建一个文件，写入一些内容

# 6.2.8 服务端检查，如下：

```txt
/data目录中看到的文件内容与客户端写入的一样，文件的拥有者和拥有组都为 root  
[root@test ~]# cat /data/a.txt  
"hello world"  
[root@test ~]# II /disk/a.txt  
-rw-r--r-- 1 root root 18 Apr 9 17:02 /disk/a.txt
```

/home/data目录中看到的文件内容与客户端写入的一样，但是文件的拥有者和拥

有组都为 nfsnobody

```batch
[root@test ~]# cat /home/data/a.txt  
"hello world"  
[root@test ~]# II /home/data/a.txt  
-rw-r--r-- 1 nfsnobody nfsnobody 18 Apr 9 17:22 /home/data/a.txt 
```

因为/data 目录设置了 no_root_squash，所以不会将 root 用户映射成匿名用户

# 6.2.9 客户端设置开机自动挂载，如下：

方法一：将手动挂载命令加入开机脚本

```txt
[root@remote ~]#echo "mount -t nfs 172.168.0.10:/data /mnt" >> /etc/rc.local 
```

方法二：添加至/etc/fstab中实现自动挂载

```txt
[root@remote ~]# echo 172.168.0.10:/data /mnt nfs defaults 0 0>> /etc/fstab  
[root@remote ~]# chkconfig netfs on 
```

网络文件系统由netfs服务来挂载，所以必须保证netfs为开机启动

# 7.3.3 autofs

# 1) 概述

Autofs 可以实现客户端对 NFS 共享目录根据需要自动挂载，当用户停止访问后，在规定时间内实现自动卸载，从而减少对 NFS 服务端的连接数。

# 2) 特点

Autofs 与 Mount/Umount 的不同之处在于，它是一种看守程序。如果它检测到用户正试图访问一个尚未挂接的文件系统，它就会自动检测该文件系统，如果存在，那么 Autofs会自动将其挂接。另一方面，如果它检测到某个已挂接的文件系统在一段时间内没有被使用，那么 Autofs 会自动将其卸载。因此一旦运行了 Autofs 后，用户就不再需要手动完成文件系统的挂接和卸载。

# 3) 安装

安装非常简单，命令如下：

```txt
yum -y install autos 
```

# 4) 启动

启动方法也很简单，命令如下：

```txt
service autofs start 
```

```txt
#chkconfig autofs on 
```

```txt
注：在RHEL6.0中不能使用service autofs restart来重启autofs服务，必须先
```

stop，在 start

# 5) 配置

Autofs 使用的是双层配置，第一层配置文件为：/etc/auto.master，该文件指定了自动挂载目录和第二层配置文件名称；第二层配置文件为/etc/auto.master 中指定的名称，该文件指定了要挂载的挂载点、挂载选项和 NFS 服务端的共享目录。

# 操作步骤：

在第二章的基础上实现 172.168.0.10:/home/data 自动挂载至 172.168.0.11 的/media目录上。

1) 编辑第一层配置文件/etc/auto.master，设置挂载目录及第二层配置文件，如下：

```txt
[root@remote ~]# echo "/media /etc/auto.nfs --timeout=120" >> /etc/auto/master  
指定第二层配置文件名为：/etc/auto.nfs，--timeout=120表示120秒内没有用户访问就自动卸载
```

2) 编辑第二层配置文件/etc/auto.nfs，设置挂载点，选项及NFS共享目录，如下：

```txt
[root@remote ~]# echo "data 172.168.0.10:/home/data" >> /etc/auto.nfs  
data是挂载点，当用户访问时，会自动在/media目录下生成，当自动卸载时，改目录会自动消失
```

3) 重启客户端autofs服务，如下：

[root@remote ~]# service autofs restart

Stopping automount: [ OK ]

Starting automount: [ OK ]

# 4) 测试，如下：

先查看本地挂载的文件系统，/media 目录上没有挂载任何文件系统

[root@remote ~]# df -h

Filesystem Size Used Avail Use% Mounted on

/dev/sda2 20G 3.7G 16G 20% /

tmpfs 1000M 228K 1000M 1% /dev/shm

/dev/sda1 194M 34M 151M 19% /boot

172.168.0.10:/disk 15G 4.8G 9.3G 34% /mnt

当进入到/media 目录时，使用 ls 命令看不到任何文件或目录，但是使用 cd 命令却可

以进入 data 目录

[root@remote ~]# cd /media/

[root@remote media]# ls

[root@remote media]# cd data

在次查看本地文件系统，发现/media 目录自动挂载了 172.168.0.10:/home/data，说

明自动挂载配置成功

[root@remote data]# df -h

Filesystem Size Used Avail Use% Mounted on

/dev/sda2 20G 3.7G 16G 20% /

tmpfs 1000M 228K 1000M 1% /dev/shm

/dev/sda1 194M 34M 151M 19% /boot

# 7.3.4 logrotate

# 1) 概述

Logrotate 是作为 linux 系统日志的管理工具存在。它可以轮换，压缩，邮件系统日志文件。并能实现将日志转储到其他目录（同一文件系统和不同文件系统）和远程目录。

# 2) 命令说明

表1 命令及选项说明  
表2 配置文件参数及说明  

<table><tr><td>选项</td><td>说明</td></tr><tr><td>-d</td><td>debug模式，隐含-v，不会对日志文件做实际操</td></tr><tr><td>-f</td><td>--force，强制轮转日志</td></tr><tr><td>-v</td><td>在轮换日志时显示详细信息</td></tr><tr><td>-s</td><td>使用指定的状态文件</td></tr></table>

<table><tr><td>参数</td><td>说明</td></tr><tr><td>daily</td><td>指定转储周期为每天</td></tr><tr><td>weekly</td><td>指定转储周期为每周</td></tr><tr><td>monthly</td><td>指定转储周期为每月</td></tr><tr><td>size</td><td>当日志文件达到指定大小时才转储，缺省单位是字节，可以设定k(小写)或者M(大写)</td></tr><tr><td>rotate</td><td>指定日志文件删除之前转储的次数，0指没有备份，5指保留5个备份</td></tr><tr><td>compress</td><td>通过gzip压缩转储后的日志</td></tr><tr><td>nocompress</td><td>不压缩转储后的日志</td></tr><tr><td>dateext</td><td>在转储后的日志文件后面加上日期做后缀</td></tr><tr><td>dateformat</td><td>指定日期格式，默认是-%Y%m%d，最多也只能加上秒，如：-%Y%m%d%s</td></tr><tr><td>copytruncate</td><td>用于还在打开中的日志文件，把当前日志备份并截断</td></tr><tr><td>nocopytruncate</td><td>备份日志文件不截断</td></tr><tr><td>nocreate</td><td>不建立新的日志文件</td></tr><tr><td>delaycompress</td><td>与compress一起使用时，转储的日志到下一次转储时才压缩</td></tr><tr><td>nodelaycompress</td><td>覆盖delaycompress，转储完成时就压缩</td></tr><tr><td>ifempty</td><td>即使是空文件也转储，缺省选项</td></tr><tr><td>notifempty</td><td>空文件不转储</td></tr><tr><td>olddir dir</td><td>转储后的日志文件放入指定的目录，必须和当前日志文件在同一个文件系统</td></tr><tr><td>noolddir</td><td>转储后的日志文件和当前日志文件放在同一目录</td></tr><tr><td>include</td><td>用于读取其他配置文件，可以指定文件，也可以指定目录</td></tr><tr><td>create</td><td>自动建立新的日志文件，新的日志文件具有和原来的文件一样权限</td></tr><tr><td>prerotate/ endscript</td><td>在转储以前需要执行的的命令可以放入这个对，这两个关键字必须独立成行</td></tr><tr><td>postrotate/ endscript</td><td>在转储以后需要执行的的命令可以放入这个对，这两个关键字必须独立成行</td></tr><tr><td>firstaction/ endscript</td><td>在转储所有匹配通配符的日志之前执行的命令，在 prerotate 之前执行，这两个关键字必须独立成行</td></tr><tr><td>lastaction/ endscript</td><td>在转储所有匹配通配符的日志之后执行的命令，在 postrotate 之后执行（并且至少有一个日志被转储才会执行），这两个关键字必须独立成行</td></tr></table>

# 3) 配置 logrotate

logrotate 缺省配置文件是 /etc/logrotate.conf，配置文件中通过使用 include 选项读取其他配置文件，默认指定的是 /etc/logrotate.d/，该目录下配置文件的参数会覆盖缺省参数。以下将讲述 logrotate 的配置步骤，实现将日志转储，以及转储到其他目录（同一文件系统和不同文件系统）和远程目录，这里使用 testlog 作为示例。

# 4) 日志转储（转储至当前日志目录）

# 操作步骤

1) 在/etc/logrotate.d/ 目录下生成子配置文件，执行以下命令：

```shell
echo "/var/log/testlog  
> {  
> size 100k  
> rotate 4  
> compress  
> copytruncate  
> dateext  
> dateformat -%Y%m%d%s  
>}" />etc/logrotate.d/testlog 
```

2) 查看子配置文件

```tcl
# cat /etc/logrotate.d/testlog
/var/log/testlog 指定日志路径
{
size 100k 设定日志大小达到100K就转储
rotate 4 保留4个备份
compress 转储后使用gzip压缩
copytruncate 备份日志并截断
dateext 在转储后的日志加上日期做后缀
dateformat-%Y%m%d%s 指定日期的格式
}
```

3) 复制一个大于100k的文件到/var/log/目录下并改名为testlog，命令如下：

# 复制文件

```txt
cp /var/log/messages /var/log/testlog 
```

# 查看文件大小

```shell
II -h /var/log/testlog* 
```

```txt
-rw----- 1 root root 609K Apr 2 12:10 /var/log/testlog 
```

4) 测试，手动运行 logrotate 命令，命令如下：

```shell
logrotate -v /etc/logrotate.d/testlog 
```

```txt
reading config file /etc/logrotate.d/testlog 
```

```txt
reading config info for /var/log/testlog 
```

```txt
Handling 1 logs 
```

```txt
rotating pattern:/var/log/testlog 
```

```txt
102400 bytes (4 rotations) 
```

```txt
empty log files are rotated, old logs are removed 
```

```txt
considering log /var/log/testlog 
```

```txt
log needs rotating 
```

```txt
rotating log /var/log/testlog, log->rotateCount is 4 
```

```txt
Converted '-%Y%m%d%s' -> '-%Y%m%d%s'
```

```txt
dateext suffix '-201504021427948126' 
```

```txt
glob pattern '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9] 
```

```json
[0-9][0-9] 
```

```txt
glob finding old rotated logs failed 
```

```txt
copying /var/log/testlog to /var/log/testlog-201504021427948126 
```

```txt
truncating /var/log/testlog 
```

```txt
compressing log with: /bin/gzip 
```

注释：-v选项可以查看logrotate命令运行的详细信息，通过以上的输出，可以很清楚的看出

logrotate 的运行过程。

5) 检查，查看日志是否被转储，命令如下：

```txt
Il-h/var/log/testlog\*   
-rw-----1 root root 0 Apr 2 12:15 /var/log/testlog   
-rw-----1 root root 39K Apr 2 12:15 /var/log/testlog-201504021427948126.gz   
注释：可以看到原来的日志文件testlog已经被转储为testlog-201504021427948126.gz, 并且被压缩，testlog大小已经为0字节
```

# 5) 日志转储（转储至同一文件系统下的不同目录）

# 操作步骤

1) 查看文件系统，命令如下：

```txt
df-h  
Filesystem Size Used Avail Use% Mounted on  
/dev/mapper/lv-root 15G 4.8G 9.4G 34% /tmpfs 935M 76K 935M 1% /dev/shm  
/dev/sda1 194M 29M 156M 16% /boot  
/dev/mapper/lv-home 504M 17M 462M 4% /home  
注释：可以看到/var目录没有单独分出，所以在根分区上 
```

2) 创建储存日志的目录，与/var目录在同一文件系统，命令如下：

```txt
mkdir/var/logbak 
```

```shell
# II /var/log* -d  
drwxr-xr-x. 15 root root 4096 Apr 2 12:15 /var/log  
drwxr-xr-x 2 root root 4096 Apr 2 12:27 /var/logbak 
```

3) 修改配置文件，设置转储目录为/var/logbak，更改内容如下：

```txt
# cat /etc/logrotate.d/testlog
/var/log/testlog
{
size 100k
rotate 4
olddir /var/logbak #增加 olddir 参数，指定转储目录为/var/logbak
compress
copytruncate
dateext
dateformat-%Y%m%d%
} 
```

4) 重新生成一个大于100k的testlog文件，并删除之前转储的日志，命令如下：

```shell
# cat /var/log/messages > /var/log/testlog
# rm -f /var/log/testlog-* 
```

5) 测试，手动运行 logrotate 命令，命令如下：

```txt
# logrotate -v /etc/logrotate.d/testlog  
reading config file /etc/logrotate.d/testlog  
reading config info for /var/log/testlog 
```

```txt
olddir is now /var/logbak #可以看到，现在 olddir 是/var/logbak  
Handling 1 logs  
rotating pattern: /var/log/testlog  
102400 bytes (4 rotations)  
olddir is /var/logbak, empty log files are rotated, old logs are removed  
considering log /var/log/testlog  
log needs rotating  
rotating log /var/log/testlog, log->rotateCount is 4  
Converted '-%Y%m%d%s' -> '-%Y%m%d%s'  
dateext suffix '-201504021427949413'  
glob pattern '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9] [0-9][0-9]'  
glob finding old rotated logs failed  
copying /var/log/testlog to /var/logbak/testlog-201504021427949413 #可以看到日志  
已经 copy 到 /var/logbak 目录  
truncating /var/log/testlog  
compressing log with: /bin/gzip 
```

6) 检查，分别检查 testlog 日志当前目录与/var/logbak 目录，命令如下：

```txt
#II-h/var/log/testlog\*   
-rw-----1 root root 0 Apr 2 12:36 /var/log/testlog   
#II-h/var/logbak/\*   
-rw-----1 root root 65K Apr 2 12:36 testlog-201504021427949413.gz   
注释：可以看到testlog已经被转储至/var/logbak目录下 
```

6) 日志转储（转储至不同文件系统下的目录）

# 操作步骤

# 1) 查看文件系统

```markdown
# df -h  
Filesystem Size Used Avail Use% Mounted on  
/dev/mapper/lv-root 15G 4.8G 9.4G 34% /  
tmpfs 935M 76K 935M 1% /dev/shm  
/dev/sda1 194M 29M 156M 16% /boot  
/dev/mapper/lv-home 504M 17M 462M 4% /home 
```

注释：可以看到/home目录是一个单独分区

2) 设置/home 目录为日志存储目录，修改配置文件如下：

```tcl
/var/log/testlog   
{   
size 100k   
rotate 4   
olddir /home #修改olddir为/home   
compress   
copytruncate   
dateext   
format -%Y%m%d%s   
} 
```

3) 测试，重新生成一个大于 100K 的 testlog 文件，手动运行 logrotate 命令，命令如下：

```batch
cat /var/log/messages > /var/log/testlog 
```

```txt
- II -h /var/log/testlog*
-rw----- 1 root root 1.2M Apr 2 12:49 /var/log/testlog
# logrotate -v /etc/logrotate.d/testlog
reading config file /etc/logrotate.d/testlog
reading config info for /var/log/testlog
olddir is now /home #当前 olddir 目录为/home
error: /etc/logrotate.d/testlog:9 olddir /home and log file /var/log/testlog are on different devices #报错
removing last 1 log config
注释：通过错误提示可以看到，/home 与 /var/log/testlog 分别在不同的设备上，所以不能使用 olddir 来实现转储至不同文件系统 
```

4) 修改配置文件如下：

```txt
/var/log/testlog  
{  
size 100k  
rotate 1 #修改保留备份数量为1份  
#olddir /home #注释掉 olddir 参数（也可删除此行）  
compress  
copytruncate  
dateext  
dateformat -%Y%m%d%s  
lastaction  
/bin/cp /var/log/testlog-* /home/ #使用lastaction脚本将转储后的日志复制
```

```txt
到/home目录  
endscript
```

5) 测试，手动运行 logrotate 命令，命令如下：

```txt
# logrotate -v /etc/logrotate.d/testlog  
reading config file /etc/logrotate.d/testlog  
reading config info for /var/log/testlog  
Handling 1 logs  
rotating pattern: /var/log/testlog  
102400 bytes (1 rotations)  
empty log files are rotated, old logs are removed  
considering log /var/log/testlog  
log needs rotating  
rotating log /var/log/testlog, log->rotateCount is 1  
Converted '-%Y%m%d%s' -> '-%Y%m%d%s'  
dateext suffix '-201504021427950617'  
glob pattern '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9] [0-9][0-9]'  
glob finding old rotated logs failed  
copying /var/log/testlog to /var/log/testlog-201504021427950617  
truncating /var/log/testlog  
compressing log with: /bin/gzip  
running last action script #日志在压缩后，运行了lastaction脚本 
```

6) 检查，分别查看/var/log/目录和/home目录，命令如下：

```shell
II -h /var/log/testlog* 
```

```txt
-rw-----1 root root 0 Apr 2 12:56 /var/log/testlog  
-rw-----1 root root 65K Apr 2 12:56 /var/log/testlog-201504021427950617.gz  
#II -h /home/*  
-rw-----1 root root 65K Apr 2 12:56 /home/testlog-201504021427950617.gz  
注释：可以看到 testlog 日志已经被转储至当前目录，并且被复制到/home 目录
```

7) 再次生成一个大于 100K 的 testlog 文件，并手动运行 logrotate 命令，显示如下：

```txt
# cat /var/log/messages > /var/log/testlog
# II -h /var/log/testlog*
-rw----- 1 root root 1.3M Apr 2 13:05 /var/log/testlog
-rw----- 1 root root 65K Apr 2 12:56 /var/log/testlog-201504021427950617.gz
# logrotate -v /etc/logrotate.d/testlog
reading config file /etc/logrotate.d/testlog
reading config info for /var/log/testlog
Handling 1 logs
rotating pattern: /var/log/testlog
102400 bytes (1 rotations)
empty log files are rotated, old logs are removed
considering log /var/log/testlog
log needs rotating
rotating log /var/log/testlog, log->rotateCount is 1
Converted '-%Y%m%d%s' -> '-%Y%m%d%s'
dateext suffix '-201504021427951176'
glob pattern '-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9] [0-9] [0-9]'
copying /var/log/testlog to /var/log/testlog-201504021427951176
truncating /var/log/testlog 
```

```txt
compressing log with:/bin/gzip   
removing old log /var/log/testlog-201504021427950617.gz #移除了旧的文件   
running last action script 
```

8) 检查，分别查看/var/log/目录和/home 目录，命令如下：

```txt
#II-h/var/log/testlog\*   
-rw-----1 root root 0 Apr 2 13:06 /var/log/testlog   
-rw-----1 root root 66K Apr 2 13:06 /var/log/testlog-201504021427951176.gz   
#II-h/home/\*   
-rw-----1 root root 65K Apr 2 12:56 /home/testlog-201504021427950617.gz   
-rw-----1 root root 66K Apr 2 13:06 /home/testlog-201504021427951176.gz   
注释：可以看到/home目录下有两个日志文件，而/var/log/目录下只有一个最新的日志文   
件，所以/var/log/目录下始终只会保留一个备份
```

# 7) 日志转储（转储至远程目录）

如果远程目录使用了 NFS 共享，可以将远程目录挂载至本地，使用第 3 种方法（日志转储至不同文件系统下的目录）来实现，如果没有使用 NFS 共享，可以使用 scp 来实现。

# 操作步骤

1) 环境介绍：客户端 IP 地址为 172.168.0.10，远程端地址为：172.168.0.11，分别在两台

机器上执行以下命令查看：

```txt
[root@test ~]# ifconfig eth0 | grep "inet addr" | awk '{print $2}' | awk -F: '{print $2}' 
```

172.168.0.10

[root@remote ~]# ifconfig eth0 | grep "inet addr" | awk '{print $\$ 23$ | awk -F: '{print $2}'

172.168.0.11

2) 配置ssh免密钥登陆，在客户端上操作，命令如下：

[root@test ~]# ssh-keygen

Generating public/private rsa key pair.

Enter file in which to save the key (/root/.ssh/id_rsa): #回车

Enter passphrase (empty for no passphrase): #回车

Enter same passphrase again:

Your identification has been saved in /root/.ssh/id_rsa.

Your public key has been saved in /root/.ssh/id_rsa.pub.

The key fingerprint is:

ba:b4:4b:ef:27:81:ec:11:ef:4a:4b:8d:15:7b:e9:45 root@test

The key's randomart image is:

+--[ RSA 2048]----+

```txt
| | |
| --- | --- |
| | | |
| | . E | |
| | . o o | |
| | .+S o . | |
| | +=00 . | |
| | .Bo... | |
| | =.=0 . | |
| | *+00 | |
| +--------+ 
```

[root@test ~]# ssh-copy-id -i /root/.ssh/id_rsa.pub 172.168.0.11

The authenticity of host '172.168.0.11 (172.168.0.11)' can't be established.

RSA key fingerprint is 40:8c:d1:8b:ed:bf:e3:64:ca:ae:17:c6:11:7d:38:8f.

Are you sure you want to continue connecting (yes/no)? yes #输入 yes

Warning: Permanently added '172.168.0.11' (RSA) to the list of known hosts.

root@172.168.0.11's password:

#输出 172.168.0.11 的 root 密码

Now try logging into the machine, with "ssh '172.168.0.11'", and check in:

.ssh/authorized_keys

to make sure we haven't added extra keys that you weren't expecting.

3) 测试，使用 ssh 登陆远程端 172.168.0.11，看是否需要输密码，命令如下：

[root@test ~]# ssh 172.168.0.11

Last login: Thu Mar 26 09:38:42 2015 from 172.168.0.1

[root@remote ~]#

#成功免密钥登陆

4) 在远程端建立储存日志的目录/data，命令如下：

[root@remote ~]# mkdir /data

5) 修改 logrotate 子配置文件/etc/logrotate.d/testlog 内容如下：

/var/log/testlog

size 100k

rotate 1

#olddir /home

compress

copytruncate

dateext

dateformat -%Y%m%d%s

lastaction

/usr/bin/scp /var/log/testlog-* 172.168.0.11:/data

#修改 lastaction 脚本，将

转储后的日志复制至远程目录

```txt
endscript } 
```

6) 生成一个大于 100K 的 testlog 文件，并删除之前 testlog 转储过的日志文件，命令如下：

```txt
[root@test ~]# cat /var/log/messages > /var/log/testlog  
[root@test ~]# rm -rf /var/log/testlog-*  
[root@test ~]# II -h /var/log/testlog*  
-rw----- 1 root root 1.3M Apr 2 13:39 /var/log/testlog 
```

7) 测试，手动运行 logrotate 命令，显示如下：

```txt
[root@test ~]# logrotate -v /etc/logrotate.d/testlog   
reading config file /etc/logrotate.d/testlog   
reading config info for /var/log/testlog   
Handling 1 logs   
rotating pattern:/var/log/testlog   
102400 bytes (1 rotations)   
empty log files are rotated, old logs are removed   
considering log /var/log/testlog   
log needs rotating   
rotating log /var/log/testlog, log->rotateCount is 1   
Converted '-%Y%m%d%s' -> '-%Y%m%d%s'   
dateext suffix '-201504021427953276'   
glob pattern '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'   
glob finding old rotated logs failed   
copying /var/log/testlog to /var/log/testlog-201504021427953276   
truncating /var/log/testlog   
compressing log with:/bin/gzip   
running last action script 
```

8) 检查，分别查看/var/log/目录，和远程端 172.168.0.11 下的/data 目录，命令如下：

```txt
[root@test ~]# II -h /var/log/testlog*  
-rw----- 1 root root 0 Apr 2 13:41 /var/log/testlog  
-rw----- 1 root root 67K Apr 2 13:41 /var/log/testlog-201504021427953276.gz  
[root@test ~]# ssh 172.168.0.11 "Is -lh /data/"  
-rw-----+ 1 root admin 67K Mar 26 11:12 /data/testlog-201504021427953276.gz 
```

注释：可以看到，testlog 日志被转储至当前目录，然后被复制至远程目录/data 下。因为设置了 rotate 1，所以在/var/log 目录下只会保留一个备份。

# 8) 扩展

如果转储后的日志是放在不同的文件系统或者是远程目录，日志同一目录下可以通过设置rotate 1 来确保始终只保留一份备份，而其他文件系统和远程目录可以通过设置firstaction 脚本或者 crontab 来实现保留几份备份。以下示例仅供参考：

# 方法一：

使用firstaction脚本实现保留最近5天的备份，修改配置文件如下：

```txt
/var/log/testlog  
{  
size 100k  
rotate 1  
#olddir /home  
compress 
```

copytruncate   
dateext   
dateformat $-\% \% \text{m}\% \text{d}\% \text{s}$ firstaction   
/usr/bin/find/home-name testlog-\*-mtime $+5$ -exec rm{}; #使用find查找出5天以前的日志，然后删除   
endscript   
lastaction   
/bin/cp/var/log/testlog-\*/home/   
endscript   
}

# 方法二：

使用crontab来实现保留最近5天的备份，创建脚本，命令如下：

```shell
# vim /root/logrotate.sh
输入以下内容：
#!/bin/bash
/usr/bin/find/home-name testlog-* -mtime +5 -exec rm {} \
赋予脚本执行权限：
# chmod u+x /root/logrotate.sh 
```

创建计划任务，命令如下：

```txt
crontab -e输入以下内容：
```

# 7.3.5 vsftp

# 1) 概述

FTP（File Transfer Protocol）即文件传输协议，用于 Internet 上的控制文件的双向传输。

同时，它也是一个应用程序。基于不同的操作系统有不同的FTP应用程序，而所有这些

应用程序都遵守同一种协议以传输文件。在 FTP 的使用当中，用户经常遇到两个概念：

下载（Download）和上传（Upload）。下载文件就是从远程主机拷贝文件至自己的计

算机上；上传文件就是将文件从自己的计算机中拷贝至远程主机上。用Internet语言来

说，用户可通过客户机程序向（从）远程主机上传（下载）文件，由于使用的是明码传输

方式，为了更安全的使用 FTP，也就有了后来的 VSFTP（Very Secure FTP）。

# 2) 特点

它是一个安全、高速、稳定的 FTP 服务器

它可以做基于多个IP的虚拟FTP主机服务器

匿名服务设置十分方便

匿名FTP的根目录不需要任何特殊的目录结构，或系统程序或其它的系统文件

不执行任何外部程序，从而减少了安全隐患

支持虚拟用户，并且每个虚拟用户可以具有独立的属性配置

可以设置从 inetd 中启动，或者独立的 FTP 服务器两种运行方式

支持两种认证方式（PAP 或 xinetd/ tcp_wrappers）

支持带宽限制

# 3) 配置参数

<table><tr><td>参数</td><td>说明</td></tr><tr><td>local_enable</td><td>是否开启实体用户模式，默认是NO，设为YES时，/etc/passwd中的用户才能以实体用户的方式登陆</td></tr><tr><td>local_max_rate</td><td>限制实体用户的传输速度，单位是字节，默认是0，表示不限速</td></tr><tr><td>write_enable</td><td>是否允许用户上传数据，默认是NO</td></tr><tr><td>local.umask</td><td>用户上传文件的权限，默认是077</td></tr><tr><td>pasv_enable</td><td>支持数据流的被动式连接模式(passive mode)，默认为YES</td></tr><tr><td>anonymous_enable</td><td>是否允许匿名访问，默认是YES</td></tr><tr><td>anon_world_readable_o nly</td><td>允许匿名用户具有下载可读档案的权限，默认是YES，需 anonymous_enable=YES 才会生效，</td></tr><tr><td>anon_upload_enable</td><td>是否允许匿名用户上传数据，默认是NO，如果设为 YES，需anonymous_enable=YES 和 anon_other_write_enable=YES 才会生效</td></tr><tr><td>anon_mkdir_write_enab le</td><td>是否允许匿名用户具有创建目录的权限，默认是NO，如 果设为YES，需anonymous_enable=YES 和 anon_other_write_enable=YES 才会生效</td></tr><tr><td>anon_other_write_enabl e</td><td>是否允许匿名用户具有除写入之外的权限，包括删除与改 写服务器上的档案及档名等权限，默认是NO，如果设为 YES，需anonymous_enable=YES 才会生效</td></tr><tr><td>no_anon_password</td><td>是否检查匿名用户的密码，默认是NO</td></tr><tr><td>anon_max_rate</td><td>限制匿名用户传输速度，单位是字节，默认是0，表示不 限速</td></tr><tr><td>anon.umask</td><td>匿名用户上传文件的权限，默认是077，</td></tr><tr><td>guest_enable</td><td>是否开启访客模式，默认是NO，如果设为YES，任何实 体账号均被假设成 guest</td></tr><tr><td>guest_username</td><td>指定访客的身份，默认是ftp，需guest_enable=YES才会生效</td></tr><tr><td>listen</td><td>以standalone的方式来启动，默认是NO</td></tr><tr><td>listen_port</td><td>FTP监听端口，默认是21</td></tr><tr><td>connect_from_port_20</td><td>是否通过20端口连接，默认是YES</td></tr><tr><td>ftp_data_port</td><td>数据传输端口，默认是20，需connect_from_port_20=YES才会生效</td></tr><tr><td>chroot_local_user</td><td>是否将用户限制在自己的家目录，默认是NO，如果设为YES，表示用户就会被chroot，该设置还与chroot_list_enable，chroot_list_file两个参数有关</td></tr><tr><td>chroot_list_enable</td><td>是否启用chroot列表功能，默认是NO</td></tr><tr><td>chroot_list_file</td><td>指定chroot_list文件路径，默认是/etc/vsftpd/chroot_list，当chroot_list_enable=YES时，该参数才会生效</td></tr><tr><td>userlist_enable</td><td>启用用户列表，默认是NO</td></tr><tr><td>userlist_deny</td><td>拒绝用户列表中的用户，默认是YES</td></tr><tr><td>userlist_file</td><td>默认是/etc/vsftpd/user_list</td></tr><tr><td>tcpWrappers</td><td>是否支持tcpWrappers，默认是NO</td></tr><tr><td>xferlog_ecanle</td><td>是否记录上传与下载文件的记录，默认是NO</td></tr><tr><td>xferlog_file</td><td>记录上传与下载记录的文件，默认是/var/log/xferlog，
需xferlog_ecanle=YES才会生效</td></tr></table>

# 4) 安装

服务端的 RPM 包为 vsftpd

客户端的 RPM 包为 ftp，lftp（选择其中之一即可）

安装方法如下：

安装服务端

# yum -y install vsftpd

安装客户端

# yum -y install ftp lftp #安装一个即可，也可以两个都安装

# 5) 配置

vsftp 的主配置文件为：/etc/vsftpd/vsftpd.conf，该配置文件的设定是以 bash 变量设定

相同的方式来处理的，也就是“option=value”来设定的，需要注意的是，等号两边不能

有空格，#开头的都为注释行。如果涉及到用户访问权限等问题，还需要配置/etc/

vsftpd/ftpusers，/etc/vsftpd/user_list，/etc/vsftpd/chroot_list 等文件，除了主配置

文件外，还可以给特定用户设定个人配置文件。

注：对于用户能否上传，修改，删除文件，除了需要在配置文件中定义外，还需要注意服务端目录的权限问题。

# 环境介绍：

主机名：server IP：172.168.0.10 （服务器）

主机名：client IP：172.168.0.11 （备份端）

# 5.1) 配置 FTP 实现匿名用户上传及下载

# 操作步骤：

5.1.1配置ftp，允许匿名访问，默认情况下，vsftp的配置文件已经开启了匿名用户的访问权

限，ftp 匿名用户的目录在/var/ftp，如下：

```txt
[root@server ~]# grep -v ^# /etc/vsftpd/vsftpd.conf | grep -v ^$ 
```

```txt
anonymous_enable=YES #允许匿名访问 
```

```txt
local_enable=YES 
```

```ini
write_enable=YES 
```

```txt
local_unmask=022 
```

```txt
dirmessage_enable=YES 
```

```txt
xferlog_enable=YES 
```

```txt
connect_from_port_20=YES 
```

xferlog_std_format $\equiv$ YES   
listen $\equiv$ YES   
pam.service_name $\equiv$ vsftpd   
userlist_enable $\equiv$ YES   
tcp��pers $\equiv$ YES   
在匿名用户目录下放一些文件   
[root@server\~]# echo "hello world"> /var/ftp/a.txt   
启动vsftp   
#service vsftpd start   
Starting vsftpd for vsftpd: [ OK ]

# 5.1.2客户端匿名访问及下载，如下：

[root@client ~]# ftp 172.168.0.10 #使用 ftp 客户端匿名访问 172.168.0.10

Connected to 172.168.0.10 (172.168.0.10).

220 (vsFTPd 2.2.2)

Name (172.168.0.10:root): anonymous #使用 anonymous 用户访问

331 Please specify the password.

Password: #输入匿名用户的密码，随便输入就可以，但是不能不输

230 Login successful. #登陆成功，使用 no_anon_password=YES 参数可以不验证密码

Remote system type is UNIX.

```txt
Using binary mode to transfer files.  
ftp> #登陆成功后会进入一个ftp的命令行，输入?可以看到很多命令  
ftp>pwd #使用pwd命令可以看到当前目录是根，因为/var/ftp就是ftp根目录  
257 "/"  
ftp>Is #使用Is命令可以查看当前目录  
227 Entering Passive Mode (172,168,0,10,204,161).  
150 Here comes the directory listing.  
-rw-r--r-- 10 0 12 Apr 10 02:25 a.txt  
drwxrwxrwx 30 0 4096 Oct 16 2013 pub  
226 Directory send OK.  
ftp> get a.txt #使用get命令下载a.txt  
local: a.txt remote: a.txt  
227 Entering Passive Mode (172,168,0,10,232,115).  
150 Opening BINARY mode data connection for a.txt (12 bytes).  
226 Transfer complete.  
12 bytes received in 7e-05 secs (171.43 Kbytes/sec)  
ftp>exit  
221 Goodbye.  
[root@client ~]# cat a.txt #在本地查看下载的文件内容  
hello world
```

5.1.3配置ftp，允许匿名用户上传，修改配置文件，添加如下选项，如下：

```txt
允许匿名用户上传文件  
[root@server ~]# echo "anon_upload_enable=YES" >> /etc/vsftpd/vsftpd.conf
```

若允许匿名用户创建目录，添加如下参数

```txt
[root@server ~]# echo "anon_mkdir_write_enable=YES" >> /etc/vsftpd/vsftpd.conf 
```

若允许匿名用户修改删除文件，添加如下参数

```shell
[root@server ~]# echo "anon_other_write_enable=YES" >> /etc/vsftpd/vsftpd.conf 
```

5.1.4 使用匿名用户上传文件测试，ftp 根目录为/var/ftp，该目录除 root 之外其他用户是没有

写权限的，所以用户不能直接在将文件上传至该目录，而且该目录的权限不能修改为777，

否则用户访问 ftp 时会被拒绝，/var/ftp 下有一个 pub 目录，该目录权限为 777，一般上传文

件会上传至 pub 目录，如下：

匿名登陆 ftp

```txt
[root@client ~]# ftp 172.168.0.10 
```

```txt
Connected to 172.168.0.10 (172.168.0.10). 
```

```txt
220 (vsFTPd 2.2.2) 
```

```txt
Name (172.168.0.10:root): ftp 
```

```txt
230 Login successful. 
```

```txt
Remote system type is UNIX. 
```

```txt
Using binary mode to transfer files. 
```

```txt
ftp>ls #查看ftp根目录下的内容
```

```txt
227 Entering Passive Mode (172,168,0,10,218,214). 
```

```txt
150 Here comes the directory listing. 
```

```txt
-rwxr-xr-x 10 0 12 Apr 10 02:32 a.txt 
```

drwxrwxrwx 2 0 0 4096 Apr 10 04:00 pub

226 Directory send OK.

ftp> cd pub #进入 pub 目录

250 Directory successfully changed.

ftp> ls #查看pub目录下的内容，pub目录是空目录

227 Entering Passive Mode (172,168,0,10,151,207).

150 Here comes the directory listing.

226 Directory send OK.

ftp> put redhat.txt #使用 put 命令上传 redhat.txt

local: redhat.txt remote: redhat.txt

227 Entering Passive Mode (172,168,0,10,60,77).

150 Ok to send data.

226 Transfer complete. #传输完成

13 bytes sent in 7.5e-05 secs (173.33 Kbytes/sec)

ftp> ls #查看

227 Entering Passive Mode (172,168,0,10,220,141).

150 Here comes the directory listing.

-rw------- 1 14 50 13 Apr 10 04:09 redhat.txt

226 Directory send OK.

可以看到文件redhat.txt上传成功，且文件的权限为600，这是由anon_umask参数

决定的，该参数默认值是 077

# 5.2)配置FTP实现实体用户访问

# 操作步骤

5.2.1 默认情况下，vsftp 的配置文件中已经开启了实体用户的访问权限，如下：

```ini
[root@server ~]# grep local_enable /etc/vsftpd/vsftpd.conf  
local_enable=YES 
```

5.2.2 创建两个实体用户测试，如下：

创建了两个用户 admin1 和 admin2，密码为：redhat

[root@server ~]# useradd admin1

[root@server ~]# useradd admin2

[root@server ~]# echo redhat | passwd --stdin admin1

Changing password for user admin1.

passwd: all authentication tokens updated successfully.

[root@server ~]# echo redhat | passwd --stdin admin2

Changing password for user admin2.

passwd: all authentication tokens updated successfully.

5.2.3 使用实体用户访问 ftp，如下：

[root@client ~]# ftp 172.168.0.10

Connected to 172.168.0.10 (172.168.0.10).

220 (vsFTPd 2.2.2)

Name (172.168.0.10:root): admin1 #输入用户名 admin1

331 Please specify the password.

Password: #输入密码

230 Login successful. #登陆成功

```txt
Remote system type is UNIX. Using binary mode to transfer files. 
```

```txt
ftp> pwd #使用 pwd 命令看到的，admin1 登陆之后的目录就是其家目录 257 "/home/admin1"
```

```txt
ftp> cd / #使用cd命令进入根，成功
```

```txt
250 Directory successfully changed. 
```

```txt
ftp> cd /etc/ #使用cd命令进入/etc，成功
```

```txt
250 Directory successfully changed. 
```

```txt
ftp> Ispasswd* #查看/etc下passwd开头的文件，成功 
```

```txt
227 Entering Passive Mode (172,168,0,10,208,194). 
```

```txt
150 Here comes the directory listing. 
```

```txt
-rw-r--r-- 10 0 1801 Apr 10 04:18 passwd
```

```txt
-rw-r--r-- 10 0 1760 Apr 09 01:24passwd-
```

```txt
226 Directory send OK. 
```

```txt
这种情况，实体用户可以随意的进入任何目录是非常危险的，所以需要配置用户不能进去家目录以外的目录
```

# 5.2.4 配置实体用户不能跳出家目录，如下：

添加如下参数，并重启 vsftpd 服务

```txt
[root@server ~]# echo "chroot_local_user=YES" >> /etc/vsftpd/vsftpd.conf 
```

```txt
[root@server ~]# service vsftpd restart 
```

```txt
Shutting down vsftpd: [OK] 
```

```txt
Starting vsftpd for vsftpd: [OK] 
```

# 5.2.5 再次使用 admin1 访问 FTP，如下：

[root@client ~]# ftp 172.168.0.10

Connected to 172.168.0.10 (172.168.0.10).

220 (vsFTPd 2.2.2)

Name (172.168.0.10:root): admin1

331 Please specify the password.

Password:

230 Login successful.

Remote system type is UNIX.

Using binary mode to transfer files.

ftp> pwd #登陆成功后，使用 pwd 看到当前目录就是根目录

257 "/"

ftp> cd /etc/ #当直接进入其他目录时，提示失败

550 Failed to change directory.

# 5.2.6配置部分实体用户可以跳出家目录，部分用户不能跳出，如下：

开启chroot列表，指定列表文件路径

[root@server ~]# echo "chroot_list_enable=YES

> chroot_list_file=/etc/vsftpd/chroot_list" $> >$ /etc/vsftpd/vsftpd.conf

将 admin2 用户加入到/etc/vsftpd/chroot_list 文件中

[root@server ~]# echo admin2 $>$ /etc/vsftpd/chroot_list

重启 vsftpd 服务

```txt
[root@server ~]# service vsftpd restart  
Shutting down vsftpd: [ OK]  
Starting vsftpd for vsftpd: [ OK] 
```

# 5.2.7 使用 admin1 和 admin2 分别访问 FTP，如下：

```txt
root@client ~]# ftp 172.168.0.10
Connected to 172.168.0.10 (172.168.0.10).
220 (vsFTPd 2.2.2)
Name (172.168.0.10:root): admin1
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> pwd
257 "/"
ftp> cd /etc/ #admin1 还是无法跳出家目录
550 Failed to change directory.
使用 admin2 访问 ftp
[root@client ~]# ftp 172.168.0.10
Connected to 172.168.0.10 (172.168.0.10).
220 (vsFTPd 2.2.2)
Name (172.168.0.10:root): admin2
331 Please specify the password.
Password: 
```

```txt
230 Login successful.  
Remote system type is UNIX.  
Using binary mode to transfer files.  
ftp> pwd  
257 "/home/admin2"  
ftp> cd /etc/ #admin2 可以跳出家目录  
250 Directory successfully changed.  
当 chroot_local_user=YES，实体用户不可以跳出家目录，当同时  
chroot_list_enable=YES，chroot_list_file 文件中定义的实体用户可以跳出家目录，其他用户不能跳出家目录
```

5.2.8 修改 chroot_local_user=NO，其他配置不变，如下：

将chroot_local_user $\equiv$ YES注释，默认表示NO   
[root@server\~]#tail-n5/etc/vsftpd/vsftpd.conf   
anon_other_write_enable $\equiv$ YES   
no_anon_password $\equiv$ YES   
#chroot_local_user $\equiv$ YES   
chroot_list_enable $\equiv$ YES   
chroot_list_file=/etc/vsftpd/chroot_list   
重启vsftpd服务   
[root@server\~]#service vsftpd restart   
Shutting down vsftpd: [OK]   
Starting vsftpd for vsftpd: [OK]

# 5.2.9 使用 admin1 和 admin2 分别访问 FTP，如下：

使用 admin1 访问 ftp

[root@client ~]# ftp 172.168.0.10

Connected to 172.168.0.10 (172.168.0.10).

220 (vsFTPd 2.2.2)

Name (172.168.0.10:root): admin1

331 Please specify the password.

Password:

230 Login successful.

Remote system type is UNIX.

Using binary mode to transfer files.

ftp> pwd

257 "/home/admin1"

ftp> cd /etc/ #admin1可以跳出家目录

250 Directory successfully changed.

使用 admin2 访问 ftp

[root@client ~]# ftp 172.168.0.10

Connected to 172.168.0.10 (172.168.0.10).

220 (vsFTPd 2.2.2)

Name (172.168.0.10:root): admin2

331 Please specify the password.

Password:

230 Login successful.

Remote system type is UNIX.

Using binary mode to transfer files.

```txt
ftp> pwd  
257 "/"  
ftp> cd /etc/ #admin2 不可以跳出家目录  
550 Failed to change directory.  
当 chroot_local_user=NO，实体用户可以跳出家目录，当同时  
chroot_list_enable=YES，chroot_list_file 文件中定义的实体用户不可以跳出家目录，  
其他用户可以跳出家目录
```

# 5.3) 配置 FTP 用户访问控制

/etc/vsftpd 目录下有两个文件：ftpusers 和 user_list，ftpusers 中定义的用户不可以访

问 ftp，当 userlist_ecable=YES 时，user_list 文件才会生效，当 userlist_deny=NO 时，

只有 user_list 中定义的用户可以访问 ftp，当 userlist_deny=YES 时，user_list 中定义的

用户不可以访问 ftp，当一个用户同时存在 ftpusers 和 user_list 文件中，该用户不可以访

问 ftp，当一个用户即不存在于 ftpusers 也不存在于 user_list，该用户不可以访问 ftp。

# 操作步骤

5.3.1开启用户列表，默认已经开启，如下：

```ini
[root@server ~]# grep userlist /etc/vsftpd/vsftpd.conf  
userlist_enable=YES 
```

添加 userlist_deny=NO

[root@server ~]# echo userlist_deny=NO $> >$ /etc/vsftpd/vsftpd.conf

重启 vsftpd 服务

[root@server ~]# service vsftpd restart

Shutting down vsftpd: [ OK ]

Starting vsftpd for vsftpd: [ OK ]

5.3.2 将 admin1 加入 ftpusers，将 admin2 加入 user_list，如下：

[root@server ~]# echo admin1 $> >$ /etc/vsftpd/ftpusers

[root@server ~]# echo admin2 $> >$ /etc/vsftpd/user_list

正常情况下 admin1 将无法访问 ftp，admin2 可以访问 ftp

5.3.3 使用 admin1 和 admin2 访问 FTP，如下：

使用 admin1 访问

[root@client ~]# ftp 172.168.0.10

Connected to 172.168.0.10 (172.168.0.10).

220 (vsFTPd 2.2.2)

Name (172.168.0.10:root): admin1

331 Please specify the password.

Password:

530 Login incorrect.

Login failed. #访问失败

使用 admin2 访问

[root@client ~]# ftp 172.168.0.10

Connected to 172.168.0.10 (172.168.0.10).

220 (vsFTPd 2.2.2)

Name (172.168.0.10:root): admin2

331 Please specify the password.

Password:

230 Login successful. #访问成功

Remote system type is UNIX.

Using binary mode to transfer files.

# 5.3.4 将 admin2 也加入 ftpusers，如下：

[root@server ~]# echo admin2 $> >$ /etc/vsftpd/ftpusers

当一个用户同时存在于 ftpusers 和 user_list 两个文件中时，该用户将不能访问 ftp

# 5.3.5 使用 admin2 访问 ftp，如下：

[root@client ~]# ftp 172.168.0.10

Connected to 172.168.0.10 (172.168.0.10).

220 (vsFTPd 2.2.2)

Name (172.168.0.10:root): admin2

331 Please specify the password.

Password:

530 Login incorrect.

Login failed. #访问失败

# 5.3.6 创建一个新用户 admin3，如下：

```txt
[root@server ~]# useradd admin3  
[root@server ~]# echo redhat | passwd --stdin admin3  
Changing password for user admin3.  
passwd: all authentication tokens updated successfully. 
```

# 5.3.7 使用 admin3 访问 ftp，如下：

```txt
[root@client ~]# ftp 172.168.0.10  
Connected to 172.168.0.10 (172.168.0.10).  
220 (vsFTPd 2.2.2)  
Name (172.168.0.10:root): admin3  
530 Permission denied. #直接拒绝  
Login failed. 
```

# 5.3.8 使用匿名用户访问，如下：

```txt
[root@client ~]# ftp 172.168.0.10  
Connected to 172.168.0.10 (172.168.0.10).  
220 (vsFTPd 2.2.2)  
Name (172.168.0.10:root): anonymous  
530 Permission denied. #拒绝访问  
Login failed.  
因为匿名用户 anonymous 即不存在于 ftpusers 也不存在于 user_list，所以被拒绝 
```

# 5.3.8当启用了用户列表，匿名用户将无法访问，可以将匿名用户加入user_list文件，如下：

```txt
[root@server ~]# echo anonymous >> /etc/vsftpd/user_list 
```

# 5.3.9 再使用匿名用户访问，如下：

[root@client ~]# ftp 172.168.0.10

Connected to 172.168.0.10 (172.168.0.10).

220 (vsFTPd 2.2.2)

Name (172.168.0.10:root): anonymous

230 Login successful. #访问成功

Remote system type is UNIX.

Using binary mode to transfer files.

# 7.3.6 SAMBA

# 1) 概述

Samba是在Linux和UNIX系统上实现SMB协议的一个免费软件，由服务器及客户端程

序构成。它能够使windows用户通过“网上邻居”，等熟悉的方式直接访问Linux上的

资源，也能使 linux 利用 SMB 客户端程序访问 Windows 的共享资源。SMB（Server

Messages Block，信息服务块）是一种在局域网上共享文件和打印机的一种通信协议，

它为局域网内的不同计算机之间提供文件及打印机等资源的共享服务。SMB协议是客户

机/服务器型协议，客户机通过该协议可以访问服务器上的共享文件系统、打印机及其他

资源。通过设置“NetBIOS over TCP/IP”使得 Samba 不但能与局域网络主机分享资源，

还能与全世界的电脑分享资源。

# 2) 功能

提供windows风格的文件和打印机共享。

在 Windows 网络中解析 NetBios 的名字。

提供 SMB 客户端，linux 用户可以利用 smbclient 利用类似于 ftp 的形式访问 windows

资源。

提供命令行工具，利用该工具可以有限制地支持 windows 的某些管理功能。

# 3) 命令和参数

表一配置文件参数  

<table><tr><td>全局参数</td><td>说明</td></tr><tr><td>workgroup</td><td>服务器工作组名称</td></tr><tr><td>server string</td><td>服务器描述信息</td></tr><tr><td>netbios name</td><td>主机的NetBIOS名称，每一台主机的NetBIOS名称是不同的。</td></tr><tr><td>interfaces</td><td>监听接口，注释后表示监听所有</td></tr><tr><td></td><td></td></tr><tr><td>hosts allow</td><td>允许访问的主机列表，注释后表示允许所有</td></tr><tr><td>guest account</td><td>指定 guest 账号的名字，否则为 nobody</td></tr><tr><td>log file</td><td>指定日志文件的保存路径</td></tr><tr><td>max log size</td><td>日志文件容量上限，达到上限则重新记录，单位为 KB</td></tr><tr><td>security</td><td>服务器安全级别，共 5 种，默认级别是用户：
共享 (Share)：当客户端连接到 Samba 服务器后，不需要输入 Samba 用户名和口令就可以访问 Samba 服务器中的共享资源。
用户 (User)：默认级别。Samba 服务器负责检查 Samba 用户名和口令，验证成功后才能访问相应的共享目录。
域 (Domain)：Samba 服务器本身不验证 Samba 用户名和口令，而由 Windows 域控制服务器负责。此时必须指定域控制服务器的 NetBIOS 名称。
服务器 (Sever)：Samba 服务器不验证 Samba 用户名和口令，而将输入的用户名和口令传递给另一个 Samba 服务器来校验。此时必须指定负责验证的那个 Samba 服务器的名称。
活动目录域 (ADS)：Samba 服务器不验证 Samba 用户名和口令，而由活动目录域服务器来负责。同样需要指定活动目录域服务器的 NetBIOS 名称。</td></tr><tr><td>passwd backend</td><td>passwd backend 的参数设定有三种</td></tr><tr><td></td><td>smbpasswd: 使用 smbpasswd 给系统用户设定 Samba 密码。t dbsam: 使用数据库文件 passdb.tdb, 如果使用 smbpasswd 设定 Samba 用户的话, 则用户必须为系统用户。同时可以使用 pdbedit 命令建立 Samba 账户Ldapsam: 使用 LDAP 方式验证用户</td></tr><tr><td>password server</td><td>指定密码验证服务器</td></tr><tr><td>共享段参数</td><td>说明</td></tr><tr><td>comment</td><td>共享段描述信息</td></tr><tr><td>browseable</td><td>是否可以被浏览</td></tr><tr><td>writable</td><td>是否可写。</td></tr><tr><td>valid users = %S</td><td>具有合法登入身份的用户登入时, 家目录变更为自己的家目录。</td></tr><tr><td>guest ok</td><td>是否允许 guest 访问。</td></tr><tr><td>printable</td><td>是否可以打印。</td></tr><tr><td>path</td><td>共享目录的路径</td></tr><tr><td>share modes</td><td>共享模式设定</td></tr></table>

表二 命令说明  

<table><tr><td>write list</td><td>该目录除了+*的组员可以拥有读写权限之外，其他用户仅可读。</td></tr></table>

<table><tr><td>命令</td><td>说明</td></tr><tr><td>smbpasswd</td><td>修改samba用户的密码:-a增加samba用户-d锁定samba用户-e解锁samba用户-n设置samba用户无密码-x删除samba用户</td></tr><tr><td>testparm</td><td>检查samba配置文件语法:-v列出没有配置的参数</td></tr><tr><td>smbclient</td><td>客户端访问工具:-L表示列出</td></tr><tr><td>smbstatus</td><td>查看samba共享资源被使用的情况</td></tr></table>

# 4) 安装

samba 的安装很简单，服务端需要安装 3 个包：samba，samba-common，samba-

client，命令如下：

```batch
yum -y install samba samba-\* 
```

# 5) 启动

samba 每次启动都需要启动 nmbd 和 smbd 这两个服务，nmbd 主要是用来解析工作组，

NetBIOS name，使用的是 UDP 137 和 UDP 138 端口；smbd 是用来管理主机分享的目

录，档案及打印机等，使用的是 TCP 139 和 TCP 445 端口。

```txt
service nmbd start 
```

```txt
service smbd start 
```

# 6) 配置

samba的主配置文件是/etc/samba/smb.conf，该配置文件中分为全局配置和共享段配

置，相冲突的配置会被共享段配置覆盖，文件中井号和分号后面的内容均被视为注释内容。

可以使用 testparm 命令来检查配置文件的语法。

# 环境介绍：

主机名：server IP：172.168.0.119 （Samba 服务端）

主机名：client IP：172.168.0.10（Linux 客户端 1）

主机名：remote IP：172.168.0.11（Linux 客户端 2）

主机名：Jone IP：172.168.0.1 （Windows 客户端）

# 6.1) 配置Samba，实现匿名访问

# 操作步骤：

6.1.1 在 server 端创建目录/data，创建几个测试文件，如下：

```txt
[root@server ~]# mkdir /data  
[root@server ~]#echo "hello world" > /data/a.txt  
[root@server ~]#echo "HELLO WORLD" > /data/b.txt 
```

6.1.2 修改配置文件，如下：

```txt
修改全局配置  
security = share #修改安全级别为share  
共享段配置增加如下内容  
[redhat] #共享名  
path = /data #共享目录的路径  
public = yes #允许匿名访问 
```

6.1.3重启smb服务，如下：

```txt
[root@server ~]# service smb restart  
Shutting down SMB services: [ OK ]  
Starting SMB services: [ OK ] 
```

6.1.4Linux客户端访问测试，如下：

浏览

```markdown
[root@client ~]# smbclient -L 172.168.0.119 
```

Enter root's password:

#直接回车

Domain=[MYGROUP] $\mathtt { O S = }$ [Unix] Server=[Samba 3.6.9-151.el6]

Sharename Type Comment

redhat Disk #可以看到有一个redhat的共享

IPC$ IPC IPC Service (Samba Server Version 3.6.9-151.el6)

Domain $=$ [MYGROUP] $\mathtt { O S = }$ [Unix] Server=[Samba 3.6.9-151.el6]

Server Comment

SERVER Samba Server Version 3.6.9-151.el6

Workgroup Master

MYGROUP SERVER

# 访问下载

[root@client ~]# smbclient //172.168.0.119/redhat #访问时需加上共享名

Enter root's password:

#直接回车

Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]

Server not using user level security and no password supplied.

smb: \> ls #使用 ls 查看共享目录下的文件

D 0 Mon Apr 20 16:38:07 2015

DR 0 Mon Apr 20 16:18:49 2015

```txt
a.txt 12 Mon Apr 20 16:37:55 2015  
b.txt 12 Mon Apr 20 16:38:07 2015  
40317 blocks of size 262144. 25079 blocks available 
```

smb: $\mathbf{\Pi}^{*}$ get a.txt #下载

```txt
getting file \a.txt of size 12 as a.txt (1.5 KiloBytes/sec) (average 1.5 KiloBytes/sec) smb: \> exit #退出 
```

```txt
[root@client ~]# cat a.txt #查看刚刚下载的文件
```

```txt
hello world 
```

上传文件

```txt
[root@client ~]# echo "nin hao" > c.txt #在客户端创建一个文件
```

```txt
[root@client ~]# smbclient //172.168.0.119/redhat #访问samba服务端 
```

```txt
Enter root's password: 
```

```javascript
Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6] 
```

```txt
Server not using user level security and no password supplied. 
```

smb: $\mathbf{\Pi} > \mathbf{I}\mathbf{s}$

```txt
D 0 Mon Apr 20 16:38:07 2015 
```

```txt
.. DR 0 Mon Apr 20 16:18:49 2015 
```

```txt
a.txt 12 Mon Apr 20 16:37:55 2015
```

```txt
b.txt 12 Mon Apr 20 16:38:07 2015 
```

40317 blocks of size 262144. 25078 blocks available

```txt
smb: \> put c.txt 
```

```txt
NT_STATUS_ACCESS_DENIED opening remote file \c.txt #上传失败 
```

6.1.5Windows客户端访问测试，如下：

按下Win+R键，输入如下内容：

\\172.168.0.119 回车

看到如下内容，表示访问成功：

![](images/c1db9e44c9020e6d899d45e3f2afa2534e97f813cf906a106ac8dfc5d8cea5c6.jpg)

进入redhat目录，查看文件，同样，在这里可以将文件复制至windows本地，就好比下载一样。

![](images/40c55d871d5ed0632d4a5c47970fd55ec20d7aae1347fa77029fc86bae194cfd.jpg)

上传测试，从Windows本地复制一个文件，然后在redhat目录下粘贴，提示如下：

![](images/f429cd881fb6097c51c9b143aabc8b93d59e2ce2703be62964dcb7e5a2d475aa.jpg)

6.1.6配置客户端的写权限，允许上传，同时还要修改共享目录的权限，如下：

修改配置文件

[redhat]

path $=$ /data

public $=$ yes

writable $=$ yes #开启写权限

修改目录权限

[root@server ~]# chmod 777 /data/

重启服务

[root@server ~]# service smb restart

Shutting down SMB services: [ OK ]

Starting SMB services: [ OK ]

6.1.7客户端测试，如下：

Linux 客户端

[root@client ~]# smbclient //172.168.0.119/redhat

Enter root's password:

Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]

Server not using user level security and no password supplied.

smb: $\backslash >$ put c.txt

putting file c.txt as \c.txt (0.4 kb/s) (average 0.4 kb/s) #上传成功

smb: \> ls

D 0 Mon Apr 20 22:44:46 2015

DR 0 Mon Apr 20 16:18:49 2015

a.txt 12 Mon Apr 20 16:37:55 2015

c.txt A 8 Mon Apr 20 22:44:46 2015

b.txt 12 Mon Apr 20 16:38:07 2015

Windlws客户端，登陆之后，新建一个文件

![](images/e8e1ba54fd5611323f7a86d4918dbb3ccf93af631a343b45af3ed000e6dc51ed.jpg)

新建文件成功

# 6.2) 配置 Samba，实现用户名密码访问

# 操作步骤：

# 6.2.1 创建 samba 用户，如下：

先创建本地用户，为了安全可以设置用户的默认 shell 为/sbin/nologin 不设置密码

[root@server ~]# useradd -s /sbin/nologin user1

[root@server ~]# useradd -s /sbin/nologin user2

转换为 samba 用户

[root@server ~]# smbpasswd -a user1

New SMB password:

Retype new SMB password:

Added user user1.

[root@server ~]# smbpasswd -a user2

New SMB password:

Retype new SMB password:

Added user user2.

# 6.2.2 修改配置文件，如下：

修改全局配置

security $=$ user #修改安全级别为 user

共享段配置增加如下内容

[redhat]

path $=$ /data   
public $\equiv$ no #禁止匿名访问   
writable $\equiv$ yes

重启服务  
```ini
[root@server ~]# service smb restart 
```

```txt
Shutting down SMB services: [OK] 
```

```txt
Starting SMB services: [OK] 
```

# 6.2.3Linux 客户端测试，如下：

浏览   
```txt
[root@client ~]# smbclient -L //172.168.0.119 
```

```txt
Enter root's password: #回车，浏览不需要密码
```

```txt
Anonymous login successful 
```

```javascript
Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6] 
```

```txt
Sharename Type Comment 
```

```txt
redhat Disk 
```

```powershell
IPC$ IPC IPC Service (Samba Server Version 3.6.9-151.el6) 
```

```txt
Anonymous login successful 
```

```javascript
Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6] 
```

```txt
Server Comment 
```

```txt
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
```

```txt
SERVER Samba Server Version 3.6.9-151.el6 
```

Workgroup Master

MYGROUP SERVER

访问

[root@client ~]# smbclient //172.168.0.119/redhat -U user1 #指定 user1 用户

Enter user1's password: #输入 user1 的密码

Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]

smb: \> ls#登陆成功，可以查看有哪些文件

D 0 Mon Apr 20 22:50:16 2015

DR 0 Mon Apr 20 16:18:49 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

a.txt 12 Mon Apr 20 16:37:55 2015

c.txt A 8 Mon Apr 20 22:44:46 2015

b.txt 12 Mon Apr 20 16:38:07 2015

40317 blocks of size 262144. 25077 blocks available

smb: \> get c.txt #下载文件

getting file \c.txt of size 8 as c.txt (7.8 KiloBytes/sec) (average 7.8 KiloBytes/sec)

smb: \> rm a.txt #删除文件

smb: \> ls #再次查看服务器上的文件

```txt
D 0 Tue Apr 21 08:57:14 2015  
DR 0 Mon Apr 20 16:18:49 2015 
```

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

c.txt A 8 Mon Apr 20 22:44:46 2015

b.txt 12 Mon Apr 20 16:38:07 2015

40317 blocks of size 262144. 25077 blocks available

# 6.2.4Windows 客户端测试，如下：

Windows客户端测试

Windows默认会保存之前的共享连接，测试前需清楚之前的密码，在cmd命令行输入如下：

C:\Users\J.one>net use * /del #删除之前的连接

您有以下的远程连接:

\\172.168.0.119\redhat

继续运行会取消连接。

您想继续此操作吗? (Y/N) [N]: y #输入 y 确认

命令成功完成。

按下Win+R键，输入如下内容：

\\172.168.0.119 回车

![](images/dd60c5900246eeafc2d86b7c8b44680fb0bf4e567ca73e1149f62707749e6491.jpg)

# 6.3) 配置 Samba，实现用户的访问控制及读写权限

# 操作步骤：

6.3.1创建一个新用户，如下：

```txt
创建用户user3，并将其加入user2组  
[root@server\~]#useradd-s/sbin/nologinuser3-Guser2  
[root@server\~]#iduser3  
uid=502(user3)gid=502(user3)groups=502(user3),501(user2)  
[root@server\~]#smbpasswd-a user3  
NewSMBpassword:  
Retype newSMBpassword:  
Addeduseruser3.
```

6.3.2 修改配置文件如下：

```txt
[redhat]  
path = /data  
public = no  
writable = no #关闭writable权限，write list才会生效  
write list = user1,@user2 #user1可写，user2组可写  
valid users = user2,user3 #user2和user3可读  
hosts allow = 172.168.0.10 172.168.0.1 #允许172.168.0.10和172.168.0.1访问  
hosts deny = 172.168.0.0/24 #拒绝172.168.0.0的网段访问  
注释：user1可写，但是没有读权限，所以user1将无法访问；user3不可写，但是user3属于user2组，所以user3可写；访问地址允许和拒绝相冲突时，允许优先，不考虑顺序。 
```

# 6.3.3客户端读写测试，如下：

```txt
使用user1访问，可使用%接密码  
[root@client\~]# smbclient//172.168.0.119/redhat-Uuser1%redhat#  
Domain=[MYGROUP]OS=[Unix]Server=[Samba3.6.9-151.el6]  
tree connect failed:NT_STATUS_ACCESS Denied #访问拒绝  
使用user2访问  
[root@client\~]# smbclient//172.168.0.119/redhat-Uuser2%redhat  
Domain=[MYGROUP]OS=[Unix]Server=[Samba3.6.9-151.el6] 
```

smb: \> ls

D 0 Tue Apr 21 08:57:14 2015   
DR 0 Mon Apr 20 16:18:49 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

c.txt A 8 Mon Apr 20 22:44:46 2015

b.txt 12 Mon Apr 20 16:38:07 2015

40317 blocks of size 262144. 25077 blocks available

smb: \> rm c.txt #删除文件

smb: \> ls

D 0 Tue Apr 21 09:44:17 2015

DR 0 Mon Apr 20 16:18:49 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

b.txt 12 Mon Apr 20 16:38:07 2015

40317 blocks of size 262144. 25077 blocks available

smb: \> put c.txt #上传文件

putting file c.txt as \c.txt (1.6 kb/s) (average 1.6 kb/s)

smb: \> ls

D 0 Tue Apr 21 09:45:35 2015

DR 0 Mon Apr 20 16:18:49 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

c.txt A 8 Tue Apr 21 09:45:35 2015

b.txt 12 Mon Apr 20 16:38:07 2015

40317 blocks of size 262144. 25077 blocks available

使用 user3 访问

[root@client ~]# smbclient //172.168.0.119/redhat -U user3%redhat

Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]

smb: \> ls

D 0 Tue Apr 21 09:44:27 2015

DR 0 Mon Apr 20 16:18:49 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

c.txt A 8 Tue Apr 21 09:44:27 2015

b.txt 12 Mon Apr 20 16:38:07 2015

40317 blocks of size 262144. 25077 blocks available

smb: \> rm c.txt #删除文件

smb: \> ls

D 0 Tue Apr 21 09:45:27 2015

DR 0 Mon Apr 20 16:18:49 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

b.txt 12 Mon Apr 20 16:38:07 2015

40317 blocks of size 262144. 25077 blocks available

smb: $\backslash >$ put c.txt #上传文件

putting file c.txt as \c.txt (3.9 kb/s) (average 3.9 kb/s)

smb: \> ls

D 0 Tue Apr 21 09:45:35 2015

DR 0 Mon Apr 20 16:18:49 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

c.txt A 8 Tue Apr 21 09:45:35 2015

b.txt 12 Mon Apr 20 16:38:07 2015

40317 blocks of size 262144. 25077 blocks available

测试结果：user1 不可读，虽然有写权限也没用，user2 可读可写，user3 可读，虽然

不在可写列表，但是 user3 属于 user2 组，而 user2 组在可写列表，所以 user3 可写

# 6.3.4客户端访问测试，如下：

上一步 client（172.168.0.10）已经访问成功

使用 remote（172.168.0.11）访问，将被拒绝

[root@remote ~]# smbclient //172.168.0.119/redhat -U user2%redhat

Domain $=$ [MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]

tree connect failed: NT_STATUS_ACCESS_DENIED #访问失败

# 6.4) 客户端挂载

客户端安装 cifs-utils 包

[root@client ~]# yum -y install cifs-utils

手动挂载

[root@client ~]# mount -t cifs //172.168.0.119/redhat /mnt/ -o username=user2

Password: #输入 user2 密码，也可以使用%接密码

[root@client ~]# df -h

Filesystem Size Used Avail Use% Mounted on

/dev/mapper/lv-root 15G 4.9G 9.3G 35% /

tmpfs 935M 76K 935M 1% /dev/shm

/dev/sda1 194M 45M 140M 24% /boot

/dev/mapper/lv-home 504M 54M 425M 12% /home

//172.168.0.119/redhat9.9G 3.3G 6.2G 35% /mnt

[root@client ~]# cd /mnt/

[root@client mnt]# ls

b.txt c.txt 新建文本文档.txt

# 配置自动挂载

[root@client ~]# umount /mnt

[root@client ~]# echo "//172.168.0.119/redhat /mnt cifs

defaults,username $=$ user2%redhat 0 0" >> /etc/fstab

[root@client ~]# mount -a

[root@client ~]# df -h

Filesystem Size Used Avail Use% Mounted on

/dev/mapper/lv-root 15G 4.9G 9.3G 35% /

tmpfs 935M 76K 935M 1% /dev/shm

/dev/sda1 194M 45M 140M 24% /boot

/dev/mapper/lv-home 504M 54M 425M 12% /home

//172.168.0.119/redhat9.9G 3.3G 6.2G 35% /mnt

由于/etc/fstab这个文件的权限是644，写上密码会非常不安全，正确配置如下：

创建密码文件并，并修改权限为 400

[root@client ~]# echo "username $=$ user2" $>$ /etc/samba/passwd

[root@client ~]# echo "password $=$ redhat" $> >$ /etc/samba/passwd

[root@client ~]# chmod 400 /etc/samba/passwd

更改自动挂载设置，使用 credentials 指定密码文件

//172.168.0.119/redhat /mnt cifs defaults,credentials=/etc/samba/passwd 0 0

[root@client ~]# umount /mnt

[root@client ~]# mount -a

[root@client ~]# df -h

Filesystem Size Used Avail Use% Mounted on

/dev/mapper/lv-root 15G 4.9G 9.3G 35% /

tmpfs 935M 76K 935M 1% /dev/shm

/dev/sda1 194M 45M 140M 24% /boot

/dev/mapper/lv-home 504M 54M 425M 12% /home

//172.168.0.119/redhat9.9G 3.3G 6.2G 35% /mnt

# 6.5) 用户访问家目录

6.5.1用户的家目录默认是共享的，配置文件中如下内容为家目录配置：

[homes]

comment $=$ Home Directories

browseable $=$ yes

writable $=$ yes

6.5.2 当 security $=$ user时，使用smbclient浏览时可以看到如下内容：

[root@client /]# smbclient -L //172.168.0.119

Enter root's password:

Anonymous login successful

Domain $=$ [MYGROUP] $\mathtt { O S = }$ [Unix] Server=[Samba 3.6.9-151.el6]

Sharename Type Comment

homes Disk Home Directories #多出了一个 homes 的共享名

redhat Disk

IPC$ IPC IPC Service (Samba Server Version 3.6.9-151.el6)

# 6.5.3 访问方法，如下：

直接使用 homes 共享名访问

[root@client ~]# smbclient //172.168.0.119/homes -U user2%redhat

Domain=[MYGROUP] $\mathtt { O S = }$ [Unix] Server=[Samba 3.6.9-151.el6]

smb: \> ls #访问成功，可以看到目录下的内容

D 0 Wed Apr 22 17:01:05 2015

D 0 Tue Apr 21 16:36:09 2015

.gnome2 DH 0 Wed Jul 14 23:55:40 2010

.bash_logout H 18 Wed Aug 29 19:19:40 2012

.bash_profile H 176 Wed Aug 29 19:19:40 2012

.mozilla DH 0 Fri Apr 17 17:40:28 2015

.bashrc H 124 Wed Aug 29 19:19:40 2012

hello 0 Wed Apr 22 17:01:05 2015

如果用户知道自己的家目录名称，也可以使用家目录名称访问

[root@client /]# smbclient //172.168.0.119/user2 -U user2%redhat

```txt
Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]  
smb:\>Is #访问成功，可以看到目录下的内容  
. D 0 Wed Apr 22 17:01:05 2015  
.. D 0 Tue Apr 21 16:36:09 2015  
.gnome2 DH 0 Wed Jul 14 23:55:40 2010  
.bash.logout H 18 Wed Aug 29 19:19:40 2012  
.bash_profile H 176 Wed Aug 29 19:19:40 2012  
.mozilla DH 0 Fri Apr 17 17:40:28 2015  
.bashrc H 124 Wed Aug 29 19:19:40 2012  
hello 0 Wed Apr 22 17:01:05 2015 
```

6.5.4 用户只能访问自己的家目录，不可以访问其他人的家目录，如下：

```txt
正常情况下，用户的家目录只有用户自己有读写权限，其他人是没有权限的  
[root@server ~]# II /home/  
total 12  
drwx-----.4user1user14096Apr2116:46user1  
drwx-----.4user2user24096Apr2217:01user2  
drwx-----.4user3user34096Apr2109:21user3  
用户访问其他用户的家目录时，可以连接，但是无法查看和读写  
[root@client /]# smbclient //172.168.0.119/user1-Uuser2%redhat  
Domain=[MYGROUP]OS=[Unix]Server=[Samba3.6.9-151.el6]  
smb:\>Is  
NT_STATUS_ACCESS Denied listing\*#user2无法查看user1家目录的内容
```

# 6.6) 配置 Samba 的 SELinux 安全选项

当系统开启了selinux服务时，samba的访问就有收到限制，需要对samba有关的selinux进行配置才可以实现正常访问。

# 6.6.1 当服务端 selinux 开启时，如下：

查看服务端selinux状态  
[root@server ~]#getenforce  
Enforcing #服务端selenux为强制模式  
客户端访问  
[root@client /]# smbclient //172.168.0.119/redhat-Uuser2%redhatDomain=[MYGROUP]OS=[Unix]Server=[Samba3.6.9-151.el6]  
smb: $\mathbf{\bar{I}}>$ ls  
NT_STATUS_ACCESS Denied listing\* #被拒绝

# 6.6.2 当服务端 selinux 关闭时，如下：

```txt
临时关闭selinux  
[root@server\~]#setenforce0 #临时关闭  
[root@server\~]#getenforce  
Permissive #状态为允许 
```

客户端访问

[root@client /]# smbclient //172.168.0.119/redhat -U user2%redhat

Domain $=$ [MYGROUP] $\mathtt { O S = }$ [Unix] Server=[Samba 3.6.9-151.el6]

smb: \> ls #成功列出文件

D 0 Tue Apr 21 09:45:35 2015

DR 0 Wed Apr 22 16:23:14 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

c.txt A 8 Tue Apr 21 09:45:35 2015

b.txt 12 Mon Apr 20 16:38:07 2015

# 6.6.3 修改共享目录的 context 值，开启 selinux，如下：

[root@server ~]# chcon -Rt samba_share_t /data/ #修改 context 值

[root@server ~]# ll -Zd /data/

drwxrwxrwx. root root system_u:object_r:samba_share_t:s0 /data/

[root@server ~]# setenforce 1 #开启 selinux

[root@server ~]# getenforce

Enforcing #selinux 状态为强制

# 6.6.4用户访问测试，如下：

[root@client /]# smbclient //172.168.0.119/redhat -U user2%redhat

Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]

smb: \> ls #成功列出文件

D 0 Tue Apr 21 09:45:35 2015

DR 0 Wed Apr 22 16:23:14 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

c.txt A 8 Tue Apr 21 09:45:35 2015

b.txt 12 Mon Apr 20 16:38:07 2015

# 6.6.5用户访问家目录，如下：

```ini
[root@client /]# smbclient //172.168.0.119/homes -U user2%redhat  
Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]  
smb: \> ls  
NT_STATUS_ACCESS-denied listing \* #访问失败 
```

# 6.6.6修改sebool值，实现用户在selinux开启时正常访问家目录，如下：

查看 sebool 值

```txt
[root@server ~]# getsebool -a | grep samba | grep home  
samba_create_home_dirs --> off  
samba_enable_home_dirs --> off #enable_home_dirs 的值是 off，表示关闭  
use_samba_home_dirs --> off 
```

开启 enable_home_dirs

```txt
[root@server ~]# setsebool -P samba_enable_homedirs=1 #1 表示开，也可用 on
```

[root@server ~]# getsebool -a | grep samba_enable_home

```txt
samba_enable_home_dirs --> on #已经开启 
```

用户访问

[root@client /]# smbclient //172.168.0.119/homes -U user2%redhat  
Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]  
smb: $\tilde{\mathbf{I}}$ Is #列出成功  
. D 0 Wed Apr 22 17:01:05 2015  
.. D 0 Tue Apr 21 16:36:09 2015  
.gnome2 DH 0 Wed Jul 14 23:55:40 2010  
.bash.logout H 18 Wed Aug 29 19:19:40 2012  
.bash_profile H 176 Wed Aug 29 19:19:40 2012  
.mozilla DH 0 Fri Apr 17 17:40:28 2015  
.bashrc H 124 Wed Aug 29 19:19:40 2012  
hello 0 Wed Apr 22 17:01:05 2015

# 6.7) 配置 Samba 用户别名

当本地用户转换成samba用户之后，访问者就已经知道服务器上有该用户了，为了系统安全，可以使用设置别名来隐藏真实用户。

# 6.7.1 查看已经存在的 Samba 用户，如下：

```txt
[root@server ~]# pdbedit -L   
user1:500:   
user2:501:   
user3:502: 
```

# 6.7.2设置别名，如下：

配置user1，user2和user3的别名分别为admin1，admin2和admin3  
[root@server\~]#echo"user1 $\equiv$ admin1">>/etc/samba/smbusers

[root@server ~]# echo "user2 $=$ admin2" >> /etc/samba/smbusers

[root@server ~]# echo "user3 $=$ admin3" $> >$ /etc/samba/smbusers

注释：一个用户可以设置多个别名，用空格隔开，别名的密码就是用户的密码

# 6.7.3 修改配置文件，指定用户别名文件，如下：

系统中已经存在了用户别名文件：/etc/samba/smbusers，在全局配置中添加如下内

容：

username map $=$ /etc/samba/smbusers

重启服务

[root@server ~]# service smb restart

Shutting down SMB services: [ OK ]

Starting SMB services: [ OK ]

# 6.7.4客户端使用别名访问，如下：

[root@client ~]# smbclient //172.168.0.119/redhat -U admin2 #使用 admin2 访问

Enter admin2's password:

Domain=[MYGROUP] OS=[Unix] Server=[Samba 3.6.9-151.el6]

smb: \> ls #访问成功

D 0 Tue Apr 21 09:45:35 2015

DR 0 Wed Apr 22 16:23:14 2015

新建文本文档.txt A 0 Mon Apr 20 22:50:16 2015

c.txt A 8 Tue Apr 21 09:45:35 2015

# 7) 扩展：

# 7.1) Linux 挂载 Windows 共享

在 Windows 上共享一个文件夹 Scripts，在 Linux 客户端查看

[root@client ~]# smbclient -L //172.168.0.1

Enter root's password:

Domain $=$ [JONE-THINK] OS=[Windows 7 Professional 7601 Service Pack 1]

Server=[Windows 7 Professional 6.1]

Sharename Type Comment

ADMIN$ Disk 远程管理

C$ Disk 默认共享

D$ Disk 默认共享

E$ Disk 默认共享

F$ Disk 默认共享

IPC$ IPC 远程 IPC

Q$ Disk 默认共享

Scripts Disk #可以看到 Scripts 文件夹

在Linux客户端访问，如果使用用户密码访问，需使用-U选项接上用户名，用户名是

Windows 上的用户

[root@client ~]# smbclient //172.168.0.1/Scripts

Enter root's password:

Domain $=$ [JONE-THINK] $\mathrm { O S } =$ [Windows 7 Professional 7601 Service Pack 1]

Server=[Windows 7 Professional 6.1]

smb: \> ls

D 0 Thu Apr 23 08:28:44 2015   
D 0 Thu Apr 23 08:28:44 2015

system-security_and_optimization_scripts.sh A 15887 Tue Apr 21 17:03:28 2015

Linux客户端挂载，如果使用用户密码挂载，需使用-o选项接上用户名

[root@client ~]# mount -t cifs //172.168.0.1/Scripts /mnt/

Password: #匿名挂载不需要密码，直接回车

[root@client ~]# df -h

Filesystem Size Used Avail Use% Mounted on

/dev/mapper/lv-root 15G 4.9G 9.3G 35% /

tmpfs 935M 76K 935M 1% /dev/shm

/dev/sda1 194M 45M 140M 24% /boot

/dev/mapper/lv-home 504M 54M 425M 12% /home

//172.168.0.1/Scripts 101G 4.4G 96G 5% /mnt

# 7.2) 语法测试

语法测试，如果提示有错误信息，就表示语法有误，错误配置系统会忽略，某些参数

配置过，但是没有显示出来，表示该参数是默认配置，如：browseable $=$

yes，writable $=$ no 等

[root@server ~]# testparm #直接执行 testparm

Load smb config files from /etc/samba/smb.conf

rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)

Processing section "[homes]"

Processing section "[printers]"

Processing section "[redhat]"

Loaded services file OK. #看到这个信息，表示语法正确

Server role: ROLE_STANDALONE

Press enter to see a dump of your service definitions #提示回车会看到配置信息

[global] #全局配置

workgroup $=$ MYGROUP

server string $=$ Samba Server Version %v

username map $=$ /etc/samba/smbusers

log file $=$ /var/log/samba/log.%m

max log size $= 5 0$

idmap config * : backend $=$ tdb

cups options $=$ raw

[homes] #家目录配置

comment $=$ Home Directories

read only = No

[printers] #打印机配置

comment $=$ All Printers

path $=$ /var/spool/samba

printable $=$ Yes

print ok = Yes

```hcl
browseable = No 
```

```txt
[redhat] #自定义配置 
```

path $=$ /data

```txt
valid users = user2, user3 
```

```txt
write list = user1, user2, @user2 
```

```txt
hosts allow = 172.168.0.10, 172.168.0.1 
```

```txt
hosts deny = 172.168.0.0/24 
```

测试一台机器是否有访问权限，语法如下：

testparm <配置文件 $> <$ 客户端主机名 $> <$ 客户端 $\mathrm { I P } >$ #主机名可以随便写，但是不能不写

# 客户端测试

```txt
[root@server ~]# testparm /etc/samba/smb.conf client 172.168.0.10 
```

```txt
Load smb config files from /etc/samba/smb.conf 
```

```txt
rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384) 
```

```txt
Processing section "[homes]" 
```

```txt
Processing section "[printers]" 
```

```txt
Processing section "[redhat]" 
```

```txt
Loaded services file OK. 
```

```txt
Server role: ROLE_STANDALONE 
```

```txt
Allow connection from client (172.168.0.10) to homes #允许访问家目录 
```

```txt
Allow connection from client (172.168.0.10) to printers #允许访问打印机 
```

```txt
Allow connection from client (172.168.0.10) to redhat #允许访问redhat共享 
```

[root@server ~]# testparm /etc/samba/smb.conf client 172.168.0.11

Load smb config files from /etc/samba/smb.conf

rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)

Processing section "[homes]"

Processing section "[printers]"

Processing section "[redhat]"

Loaded services file OK.

Server role: ROLE_STANDALONE

Allow connection from client (172.168.0.11) to homes #允许访问家目录

Allow connection from client (172.168.0.11) to printers #允许访问家目录

Denied connection from client (172.168.0.11)

Deny connection from client (172.168.0.11) to redhat #拒绝访问 redhat 共享

# 7.3.7 VNC

# 1) 概述

VNC (Virtual Network Computer)是虚拟网络计算机的缩写。VNC 是一款优秀的远程控制工具软件，由著名的 AT&T 的欧洲研究实验室开发的。VNC 是在基于 UNIX 和 Linux操作系统的免费的开源软件，远程控制能力强大，高效实用，其性能可以和 Windows 和MAC 中的任何远程控制软件媲美。

# 2) 组成

VNC基本上是由两部分组成：一部分是客户端的应用程序(vncviewer)；另外一部分是服务器端的应用程序(vncserver)。VNC的基本运行原理和一些Windows下的远程控制软件很相像。VNC的服务器端应用程序在UNIX和Linux操作系统中适应性很强，图形用户界面十分友好，看上去和Windows下的软件界面也很类似。在任何安装了客户端的应用程序(vncviewer)的Linux平台的计算机都能十分方便地和安装了服务器端的应用程序(vncserver)的计算机相互连接。另外，服务器端 (vncserver)还内建了 Java Web 接口，这样用户通过服务器端对其他计算机的操作就能通过Netscape显示出来了，这样的操作

过程和显示方式比较直观方便。

# 3) 命令和参数

在 Linxu 系统中，VNC 常用的命令有 vncserver，vncpasswd 和 vncviewer，其中

vncserver，vncpasswd 属于服务端命令，vncviewer 属于客户端命令。

表一 vncserver 命令说明  

<table><tr><td>选项</td><td>说明</td></tr><tr><td>-geometry</td><td>分辨率，如：600x800,1024x768</td></tr><tr><td>-kill</td><td>将启动的 vnc 端口关闭</td></tr><tr><td>-list</td><td>显示已经启动的 VNC 桌面</td></tr><tr><td>::&lt;num&gt;</td><td>将 vnc 启动在哪个端口，:1 表示 5901 端口</td></tr></table>

# 4) 安装

# 4.1) 服务端安装

服务端安装VNC之前必须安装图形界面，一般都使用GNOME桌面，安装方法如下：

# yum -y groupinstall "X Window System""Desktop"

安装 VNC 服务包 tigervnc-server，如下：

# yum -y install tigervnc-server

# 4.2)

# 客户端安装

# 4.2.1) Linux 客户端

Linux 客户端连接 VNC 时，本地也需要安装图形界面，若没有安装也可以使用第三方显

示图形界面的工具，如：Xmanager。安装图形界面的的方法如下：

```batch
yum -y groupinstall "X Window System""Desktop" 
```

安装 VNC 客户端包 tigervnc，如下：

```txt
yum -y install tigervnc 
```

# 4.2.2) Windows 客户端

Windows 客户端常用的有 TigerVNC 和 RealVNC，任选其中一个安装即可，安装方法这里不做介绍。

# 5) 启动

VNC 启动会在服务端监听一个端口，默认从 5901 开始，一个桌面占用一个端口，一个桌面同时只能被一个用户连接，第二个用户连接时会挤掉第一个用户的连接。每个用户创建的

VNC桌面被远程用户连接时，将以创建VNC桌面的用户身份接入系统，如：root用户创建的VNC桌面，远程用户连接时，将以root用户身份登陆系统；admin1用户创建的VNC桌面，

远程用户连接时，将以admin1用户身份登陆系统。所以一般情况下，不要使用root用户直接创建VNC桌面，在需要使用root用户的权限时，可以使用普通用户连接，然后使用su -切换至 root 用户。

# 启动方法如下：

执行 vncserver 命令启动 VNC，若是第一次启动，会提示设置密码

[root@workstation ~]# vncserver

You will require a password to access your desktops.

Password: #输入密码

Verify: #再次输入密码

New 'workstation.example.com:1 (root)' desktop is workstation.example.com:1

Starting applications specified in /root/.vnc/xstartup

Log file is /root/.vnc/workstation.example.com:1.log

从上面可以看出创建了一个新的桌面 workstation.example.com:1 (root)

再次启动执行vncserver命令，因为试一次已经设置了密码，所以不会再提示设置密

码

[root@workstation ~]# vncserver

New 'workstation.example.com:2 (root)' desktop is workstation.example.com:2

Starting applications specified in /root/.vnc/xstartup

Log file is /root/.vnc/workstation.example.com:2.log

创建了第二个桌面 workstation.example.com:2 (root)

# 6) 配置

默认情况下，VNC不需要做什么配置，设置了密码，启动了服务，远程用户就可以连接访问了。

# 环境介绍：

主机名：workstation IP：172.168.0.253 （VNC 服务端）

主机名：vncclient IP：172.168.0.123 （Linux 客户端）

主机名：Jone IP：172.168.0.1 （Windows 客户端）

# 6.1) 设置密码

第一次执行vncserver启动VNC时，会提示用户设置密码，用户也可以手动使用

vncpasswd命令设置自己的密码，为了保证安全，VNC的密码最好不要与用户登陆操作系统

的密码相同，每个用户都可以设置自己的VNC密码，密码文件保存在用户家目录下的.vnc目

录中的 passwd 文件里面。

# 方法如下：

使用 vncpasswd 更改密码

[root@workstation ~]# vncpasswd

Password: #输入密码

Verify: #再次输入密码

查看密码文件

[root@workstation ~]# ll ~/.vnc/passwd

-rw-------. 1 root root 8 May 28 12:46 /root/.vnc/passwd

# 6.2) 启动服务

每执行一次vncserver命令就将创建一个VNC桌面，桌面号从1开始，对应端口从5901

开始，以此类推，如下：

创建一个VNC桌面1

[root@workstation ~]# vncserver

New 'workstation.example.com:1 (root)' desktop is workstation.example.com:1

Starting applications specified in /root/.vnc/xstartup

Log file is /root/.vnc/workstation.example.com:1.log

查看端口，5901已经处于监听状态

[root@workstation ~]# netstat -tulnp | grep vnc

tcp 0 0 0.0.0.0:5901 0.0.0.0:* LISTEN 6104/Xvnc

再创建一个VNC桌面2

[root@workstation ~]# vncserver

New 'workstation.example.com:2 (root)' desktop is workstation.example.com:2

Starting applications specified in /root/.vnc/xstartup

Log file is /root/.vnc/workstation.example.com:2.log

查看端口，5902端口也被监听

[root@workstation ~]# netstat -tulnp | grep vnc

tcp 0 0 0.0.0.0:5901 0.0.0.0:* LISTEN 6104/Xvnc

tcp 0 0 0.0.0.0:5902 0.0.0.0:* LISTEN 6477/Xvnc

创建一个指定编号的VNC桌面5

[root@workstation ~]# vncserver :5

New 'workstation.example.com:5 (root)' desktop is workstation.example.com:5

Starting applications specified in /root/.vnc/xstartup

Log file is /root/.vnc/workstation.example.com:5.log

查看端口，5905端口也被监听

[root@workstation ~]# netstat -tulnp | grep vnc

```batch
tcp 0 0.0.0.0:5901 0.0.0.0:* LISTEN 6104/Xvnc  
tcp 0 0.0.0.0:5902 0.0.0.0:* LISTEN 6477/Xvnc  
tcp 0 0.0.0.0:5905 0.0.0.0:* LISTEN 6846/Xvnc 
```

查看用户创建的VNC桌面，每个用户都只能查看自己创建的桌面

```objectivec
[root@workstation ~]# vncserver -list 
```

TigerVNC server sessions:

```txt
X DISPLAY #PROCESS ID 
```

```txt
:5 6846 
```

```txt
:1 6104 
```

```txt
:2 6477 
```

可以看到当前用户已经创建了3个VNC桌面，桌面号分别为1,2,5，每个桌面进程都

有一个对应的PID

# 6.3) 关闭服务

关闭VNC桌面时，使用vncserver命令中的-kill选项，加上指定的桌面号就可以关闭指

定的桌面。如下：

关闭桌面 2

```txt
[root@workstation ~]# vncserver -kill :2 
```

```txt
Killing Xvnc process ID 6477 
```

列出桌面，只剩下桌面1和桌面5了

```objectivec
[root@workstation ~]# vncserver -list 
```

TigerVNC server sessions:

```txt
X DISPLAY #PROCESS ID 
```

```txt
:5 6846 
```

```txt
:1 6104 
```

查看端口，只有5901和5905被监听

```txt
[root@workstation ~]# netstat -tulnp | grep vnc 
```

```batch
tcp 0 0 0.0.0.0:5901 0.0.0.0:* LISTEN 6104/Xync
```

```batch
tcp 0 0 0.0.0.0:5905 0.0.0.* LISTEN 6846/Vync 
```

6.4) 开机启动

6.4.1) 修改/etc/sysconfig/vncservers 文件，添加如下内容：

```txt
VNCSERVERS="1:root 2:admin1" 
```

```txt
VNCSERVERARGS[1]="-geometry 800x600" 
```

```txt
VNCSERVERARGS[2]="-geometry 1024x768" 
```

注释：

1:root 表示使用 root 用户启动桌面 1，2:admin1 表示使用 admin1 用户启动桌面 2

VNCSERVERARGS[1]="-geometry 800x600" 表示设置桌面 1 的分辨率为 $8 0 0 \times 6 0 0$

VNCSERVERARGS[2]="-geometry 1024x768"表示设置桌面 2 的分辨率为 $1 0 2 4 \times 7 6 8$

分辨率根据用户需求自定义设置

6.4.2) 设置 VNC 开机启动，如下：

[root@workstation ~]# chkconfig vncserver on

# 6.4.3) 测试

可以将机器重启，在重启之后检查是否有5901和5902端口监听，如果有再使用客户端

连接，连接成功则表示设置成功；也可以 kill 掉已经创建的 VNC 桌面，然后执行 service

vncserver start 命令来模拟。如下：

首先给 admin1 用户设置 VNC 密码

[root@workstation ~]# su - admin1 #切换到 admin1 用户

[admin1@workstation $- ] \$ 1$ vncpasswd #设置密码

Password:

Verify:

[admin1@workstation $- ] \$ 1$ exit

logout

[root@workstation ~]#vncserver -list #列出当前已经创建的 VNC 桌面

TigerVNC server sessions:

X DISPLAY #PROCESS ID

:5 6846

:1 6104

[root@workstation ~]# vncserver -kill :1 #kill 桌面 1

Killing Xvnc process ID 6104

[root@workstation ~]# vncserver -kill :5 #kill 桌面 5

Killing Xvnc process ID 6846

[root@workstation ~]# netstat -tulnp | grep vnc #检查 VNC 端口，没有端口被监

听

[root@workstation ~]# service vncserver start

Starting VNC server: 1:root #开始以 root 用户创建桌面 1

New 'workstation.example.com:1 (root)' desktop is workstation.example.com:1

Starting applications specified in /root/.vnc/xstartup

Log file is /root/.vnc/workstation.example.com:1.log

2:admin1 #开始以 admin1 用户创建桌面 2

New 'workstation.example.com:2 (admin1)' desktop is

workstation.example.com:2

Starting applications specified in /home/admin1/.vnc/xstartup

Log file is /home/admin1/.vnc/workstation.example.com:2.log

[ OK ]

[root@workstation ~]# netstat -tulnp | grep vnc #检查端口，有 5901 和 5902

tcp 0 0 0.0.0.0:5901

0.0.0.0:*

LISTEN

8755/Xvnc

tcp 0 0 0.0.0.0:5902

0.0.0.0:*

LISTEN

8865/Xvnc

# 7) 客户端连接

# 7.1) Linux 客户端连接

Linux客户端需启动图形界面，或者配置好DISPLAY环境变量和第三方显示图形界面的

工具，如下：

执行命令：vncviewer 主机名/IP：桌面号 ，如下图：

![](images/ad2ba710eda2d884e755609e4b030ffe47b7ff1dec5c62e550c01de64d8f5ee0.jpg)

连接成功后会弹出密码提示框，输入密码，密码验证成功后，就会出现VNC服务端

workstation.example.com 的桌面，如下图：

![](images/21e8cfba68a7fff684ec216b355d38b3d97433501c2879d79950f8838414a307.jpg)

现在就可以对 workstation.example.com 这台机器进行远程控制了。

# 7.2) Windows 客户端连接

在 Windows 上打开 VNC 客户端，输入 workstation.example.com:2，如下图：

![](images/bc3b642e7f142f7c078583dceb219465388710fbc30035a4eff7a89f4781cdfb.jpg)

连接成功后会弹出密码验证框，如下图：

![](images/1a82b41fa35750765790fa2f829f5e8fe29259faf1c8414df059553140268662.jpg)

密码验证成功后，会出现 VNC 服务端 workstation.example.com 的桌面，如下图：

![](images/86ad890a046272b0f959e661b91c8d1bcb8d2e3b6cd0ff2868dac97483b58b77.jpg)

现在就可以对 workstation.example.com 这台机器进行远程控制了。

# 7.3.8 sftp

本章节主要描述行里在RedHat Linux下使用sftp服务的配置规范。默认情况下，需关闭操作系

统的 sftp 服务，具体参考”关闭 SFTP 服务”。

# 7.3.8.1 SSHD服务安装

SFTP 为 SSH 的一部分，在 SSH（RedHat Linux 中为 OPENSSH）软件包中，已经包含了一个叫作 SFTP（Secure File Transfer Protocol）的安全文件传输子系统，SFTP 本身没有单独的守护进程，它必须使用sshd守护进程（端口号默认是22）来完成相应的连接操作。正常情况下，安装完操作系统后，默认已经安装SSH服务。

为保证sshd服务的安全性，应在/etc/ssh/sshd_config配置文件中放开如下配置的注释并做相应的修改。请参考章节 6.20“SSHD 配置”。

# 7.3.8.2 SFTP用户配置

SFTP不支持匿名用户登录，在搭建SFTP之前需创建SFTP用户，为方便统一管理，SFTP用户要求如下：

(1) 创建 SFTP 用户时用户家目录放在/home 目录下。  
(2) 限制操作系统登陆，为了保证操作系统安全，应限制SFTP用户不能登录操作系统，在创建 SFTP 用户时应指定该用户的 Shell 为/sbin/nologin，限制该用户只能登陆 SFTP。  
(3) 为了方便统一管理及配置，创建 sftpgrp 组，所有 SFTP 用户加入 sftpgrp 组。  
(4) 必须对SFTP用户的密码限制，包括时效限制(口令每90天修改一次)、复杂程度限制(长度最少 8位)、非空限制、重复使用次数限制(不得使用 6次之内重复的密码)。请参考6.13“*口令策略设置”。

用户创建示例如下（以下为创建 sftpusr1 和 sftpusr2 的示例）：  
```txt
# groupadd sftpgrp  
# useradd -s /sbin/nologin -G sftpgrp sftpusr1  
# id sftpusr1  
uid=2108(sftpusr1) gid=2108(sftpusr1) groups=2108(sftpusr1),2107(sftpgrp)  
#passwd sftpusr1  
Changing password for user sftpusr1.  
New password: #输入密码  
Retype new password: #确认密码  
passwd: all authentication tokens updated successfully. 
```

```txt
#useradd -s /sbin/nologin -G sftpgrp sftpusr2   
#id sftpusr2   
uid=2109(sftpusr2) gid=2108(sftpusr2) groups=2109(sftpusr2),2107(sftpgrp)   
#passwd sftpusr2   
Changing password for user sftpusr2.   
New password: #输入密码   
Retype new password: #确认密码   
passwd: all authentication tokens updated successfully. 
```

# 7.3.8.3 SFTP数据目录

 为了保证数据的安全及传输效率，建议SFTP的数据存放在独立的存储上面，与系统数据分离，存储的挂载点统一为/sftp，文件系统使用LV的形式，且必须是单独的VG，不能与系统VG公用。  
 为了将不同的SFTP用户的数据分离开来，SFTP用户数据统一放在/sftp目录下以SFTP用户名命名的目录下（/sftp/[username]），/sftp/[username]目录即为 SFTP 用户的根目录。  
 为了保证系统的安全性，需要启用SFTP用户的chroot功能（默认未启用），不允许SFTP用户跳出进入SFTP用户根目录以外的目录。打开chroot功能，需设置SFTP用户根目录的拥有者为root用户，权限为755，此时SFTP用户对SFTP用户根目录已无写权限，所以需要在SFTP用户根目录下新建目录供SFTP用户上传数据使用，该目录名称可根据需求自定义创建，但需保证SFTP用户具有读写权限。

配置示例如下（为 sftpusr1 与 sftpusr2 创建 SFTP 用户根目录及数据上传目录）：

```txt
创建SFTP用户根目录  
# mkdir /sftp/sftpusr1  
# mkdir /sftp/sftpusr2  
若使用root创建SFTP用户根目录，以下4步可省略，目录默认权限已经755，目录拥有者默认已经是root  
# chown root /sftp/sftpusr1  
# chmod 755 /sftp/sftpusr1
```

```shell
# chown root /sftp/sftpusr2
# chmod 755 /sftp/sftpusr2
创建SFTP用户数据上传目录及赋权
# mkdir /sftp/sftpusr1/data1
# chown sftpusr1:sftpgrp /sftp/sftpusr1/data1
# ls -ld /sftp/sftpusr1/data1
drwxr-xr-x 2 sftpusr1 sftpgrp 4096 Mar 15 15:24 /sftp/sftpusr1/data1
# mkdir /sftp/sftpusr2/data2
# chown sftpusr2:sftpgrp /sftp/sftpusr2/data2
# ls -ld /sftp/sftpusr2/data2
drwxr-xr-x 2 sftpusr2 sftpgrp 4096 Mar 15 15:24 /sftp/sftpusr2/data2 
```

# 7.3.8.4 SFTP服务配置

编辑/etc/ssh/sshd_config 文件，添加及修改内容如下。

 注释以下行：

```txt
#Subsystem sftp /usr/libexec/openssh/sftp-server 
```

 添加以下行：

```txt
Subsystem sftp internal-sftp 
```

 (可选)限制 SFTP 用户空闲的超时时间。修改主配置文件/etc/ssh/sshd_config，添加以下行：

以下参数需添加在第一个Match开头的上一行。

以限制SFTP用户空闲的超时时间300秒为配置示例：

```txt
ClientAliveCountMax 0  
ClientAliveInterval 300 
```

 在配置文件的末尾添加以下行：

```txt
Match Group sftpgrp 
```

```txt
ForceCommand internal-sftp  
AllowTcpForwarding no  
X11Forwarding no  
ChrootDirectory /sftp/%u 
```

# 主要语法解释：

Match Group sftpgrp：表示对 sftp 组进行匹配访问控制

ChrootDirectory /sftp/%u：表示限制 SFTP 用户的根目录在/sftp/%u，%u 表示SFTP 用户的用户名，这里%u 代表所有在 sftpgrp 组的用户。

注：

SFTP用户的chroot功能和ssh登录不能同时使用，首先，系统配置本身不能满足；其次，两者同时满足是有冲突的，因为配置了chroot就是为了限制SFTP用户进入SFTP用户根目录以外的目录，但若允许ssh登录，那么该用户在ssh登录之后仍然可以进入其他目录。

 完成以上配置后，需要重启SSHD服务，操作如下：

```txt
service sshd restart 
```

# 7.3.8.5 SFTP日志配置

为保证安全及达到监控的效果，需要开启SFTP的日志做为审计，为防止sftp用户频繁操作，需将日志保存在单独的目录/var/log/sftp中，配置方法如下：

 创建日志目录。

```shell
# mkdir -p /var/log/sftp 
```

 编辑/etc/ssh/sshd_config 文件。

在 Subsystem 行尾添加如下内容：

```txt
Subsystem sftp internal-sftp -f AUTHPRIV -l INFO
```

在ForceCommand行尾添加如下内容：

```txt
ForceCommand internal-sftp -f AUTHPRIV -l INFO
```

 使用root用户在SFTP用户的根目录下创建dev目录，确保dev目录的权限为755，拥有人和拥有组为root。

以 SFTP 用户 sftpusr1 和 sftpusr2 为配置示例：

```shell
# mkdir /sftp/sftpusr1/dev
# mkdir /sftp/sftpusr2/dev
# ls -ld /sftp/sftpusr*/dev
drwxr-xr-x 2 root root 4096 Apr 20 10:29 /sftp/sftpusr1/dev
drwxr-xr-x 2 root root 4096 Apr 20 10:29 /sftp/sftpusr2/dev 
```

 使用root用户在dev目录下创建log文件，确保log文件的拥有人和拥有组为root，如下所示。

# 以 SFTP 用户 sftpusr1 和 sftpusr2 为配置示例：

```shell
touch /sftp/sftpusr1/dev/log   
# touch /sftp/sftpusr2/dev/log   
ls -l /sftp/sftpusr*/dev/log   
-rw-r--r-- 1 root root 0 Apr 20 10:48 /sftp/sftpusr1/dev/log   
-rw-r--r-- 1 root root 0 Apr 20 10:48 /sftp/sftpusr2/dev/log 
```

注：

log文件的权限之后会发生变化，不需要管它。如果有其他的SFTP用户，以上两步创建dev目录和log文件的操作同样需要执行。

 编辑/etc/rsyslog.conf 文件，配置 sftp 日志文件/var/log/sftp/sftp.log，如下所示。

```txt
The authpriv file has restricted access.  
authpriv.\* /var/log/secure #在此行下方添加  
authpriv.info /var/log/sftp/sftp.log #添加的 sftp 日志文件 
```

 在/etc/rsyslog.conf 文件中，添加 sftp 的日志文件监听接口，如下所示。

# 以 SFTP 用户 sftpusr1 和 sftpusr2 为配置示例：

```powershell
$AddUnixListenSocket /sftp/sftpusr1/dev/log
$AddUnixListenSocket /sftp/sftpusr2/dev/log 
```

注：

一个用户添加一行，有多少个用户就要添加多少行。

 配置 sftp 日志 logrotate 转储策略，并自动删除时间较老的日志文件，根据我行需求，sftp 日志需每天转储一次，转储时压缩，并保留一个月（30 天），配置方法如下所示。在/etc/logrotate.d/目录下创建 sftp 日志转储配置文件 sftp，并加入如下所示配置：

/var/log/sftp/sftp.log{ daily rotate 30 compress copytruncate dateext dateformat $-\% \mathrm{Y}\% \mathrm{m}\% \mathrm{d}$ sharedscripts postrotate /bin/kill -HUP `cat /var/run/syslogd.pid $2>$ /dev/null` $2>$ /dev/null || true Endscript }

 执行以下命令，重启 sshd 和 rsyslog 服务。

```txt
service sshd restart #service rsyslog restart 
```

 执行以下命令，检查 log 文件的权限。

以 SFTP 用户 sftpusr1 和 sftpusr2 为配置示例：

```txt
ls -l /sftp/sftpusr*/dev/log  
回显如下类似信息，表示log文件权限正确。  
srv-rw-rw-1 root root 0 Apr 20 11:05 /sftp/sftpusr1/dev/log  
srv-rw-rw-1 root root 0 Apr 20 11:05 /sftp/sftpusr2/dev/log
```

# 7.3.8.6SFTP用户黑白名单配置

默认情况下，系统中所有设置了密码的用户均可以登录SFTP服务器，如需对用户或组进行限制，可在配置文件/etc/ssh/sshd_config中使用以下参数进行限制。

以下参数需添加在第一个 Match 开头的上一行。

```txt
AllowUsers [user1 user2...] #用户白名单，多个用户使用空格隔开  
AllowGroups [group1 group2...] #用户组白名单，多个组使用空格隔开  
DenyUsers [user1 user2...] #用户黑名单，多个用户使用空格隔开  
DenyGroups [group1 group2...] #用户组黑名单，多个组使用空格隔开
```

# 注：

以上参数同样会影响用户的 SSH 登陆，请谨慎使用。

# 匹配规则及顺序如下：

 以上四个参数若都不配置，则允许所有用户登录 SFTP。  
 若配置了 DenyUsers 或 DenyGroups 或者两个都配置了，则拒绝 DenyUsers 中的用户和 DenyGroups 中组的用户，允许其他的所有用户。

# 以 SFTP 用户 sftpusr1 和 sftpusr2 为配置示例：

```txt
DenyUsers sftpusr1   
DenyGroups sftpgrp1   
以上配置将只拒绝sftpusr1用户和sftpgrp1组中的所有用户，其他用户将被允许。
```

 若配置了 AllowGroups 或 AllowGroups 或者两个都配置了，则仅允许 AllowGroups 中的用户和AllowGroups中组的用户，拒绝其他所有用户。

# 以 SFTP 用户 sftpusr1 和 sftpusr2 为配置示例：

```txt
AllowUsers sftpusr2   
AllowGroups sftpgrp1   
以上配置将只允许sftpusr2用户和sftpgrp1组中的所有用户，其他用户将被拒绝。
```

 若配置了 DenyUsers 或 DenyGroups 或者两个都配置了，并且配置了 AllowGroups 或AllowGroups 或者两个都配置了，则仅允许 AllowGroups 中的用户和 AllowGroups 中组的用户，拒绝其他的所有用户（包括不存在于DenyUsers中的用户和DenyGroups中组的用户），若一个用户同时存在于拒绝策略（DenyUsers 或 DenyGroups）和允许策

略（AllowGroups 或 AllowGroups）中，则该用户将被拒绝。

以 SFTP 用户 admin、sftpusr1 和 sftpusr2，组 sftpgr1 为配置示例：

```txt
AllowUsers sftpusr2 admin   
AllowGroups sftpgr1   
DenyUsers sftpusr1 admin   
DenyGroups sftpgrp2   
以上配置将只允许sftpusr2用户和sftpgroup组中的所有用户，其他用户和用户组中的成员将被拒绝，admin用户同时存在于AllowUsers和DenyUsers中，所以会被拒绝，若sftpusr2用户属于sftp组，则sftpusr2用户也会被拒绝。
```

注：

由于用户和组的黑白名单同样会影响用户和组的SSH登陆，所以在配置黑白名单时，需要确保SSH登陆用户不受限制，否则会造成用户无法登陆。

# 建议配置

```txt
DenyUsers bin daemon adm lp sync shutdown halt mail uucp operator games gopher ftp nobody vcsa saslauth postfix sshd 
```

以上配置将系统内uid低于100的所有非root用户加入到黑名单，其他系统用户根据需要添加，添加后列表内用户将无法SSH与sftp登陆。

 完成以上配置后，执行以下命令，需要重启 SSHD 服务。

```txt
service sshd restart 
```

# 7.3.8.7SFTP主机中的用户黑白名单配置

如果需要限制某个特定的用户在特定主机的访问权限，则可以在用户黑白名单中用户名后面加上主机IP，来绑定用户和主机的访问权限，不支持对用户组的限制。

以下参数需添加在第一个Match开头的上一行。

#主机用户白名单，多个用户用空格隔开，同一用户与多个主机用逗号隔开，如下所示。

AllowUsers [user1@ip1 user2@ip1,ip2 ]

#主机用户黑名单，多个用户用空格隔开，同一用户与多个主机用逗号隔开，如下所示。

DenyUsers [user1@ip1 user2@ip1,ip2 ]

匹配规则与顺序和用户黑白名单相同。

# 配置示例如下所示。

 配置拒绝 sftpusr1 从 172.168.0.61 和 172.168.0.62 访问，同时拒绝 sftpusr2 从任何主机访问。

DenyUsers sftpusr1@172.168.0.61,172.168.0.62 sftpusr2

 配置允许 sftpusr1 从任何主机访问，同时仅允许 sftpusr2 从 172.168.0.0 网段访问。

AllowUsers sftpusr1 sftpusr2@172.168.0.0/24

 配置允许 sftpusr1 从除了 172.168.0.61,172.168.0.62 之外的所有主机访问，同时拒绝sftpusr2 从任何主机访问（允许与拒绝冲突时，拒绝优先）。

AllowUsers sftpusr1 sftpusr2@172.168.0.0/24

DenyUsers sftpusr1@172.168.0.61,172.168.0.62 sftpusr2

# 7.3.8.8SFTP主机黑白名单配置

默认情况下，系统中防火墙已经关闭，所有网络可达的主机均可访问SFTP服务器，如需对主机或者IP进行限制，可通过配置文件/etc/hosts.allow（白名单）和

/etc/hosts.deny（黑名单）来实现，默认情况下，两个文件为空，即允许所有网络可达的主机。

语法示例：

SSHD: 10.1.1.1 server1 #主机和 IP 的写法，多个用空格或者逗号隔开

SSHD: 10.1.1. 10.2. #网段的写法，多个用空格或者逗号隔开

SSHD:.example.com #域名的写法，多个用空格或者逗号隔开

SSHD: ALL #表示所有

# 匹配规则及顺序如下所示：

 若/etc/hosts.allow 和/etc/hosts.deny 均为空，则允许所有。  
 若/etc/hosts.deny 为空，不论/etc/hosts.allow 是否为空，均允许所有。  
 若/etc/hosts.deny 不为空，不论/etc/hosts.allow 是否为空，则只拒绝/etc/hosts.deny中的主机；若一个主机同时存在于/etc/hosts.deny 和/etc/hosts.allow 中，则允许优先。

# 行内缺省配置：

为防止不明网络的主机连接，深圳和上海的服务器默认黑白名单规则应按如下设置：

 在/etc/hosts.deny 中添加如下内容。

SSHD: ALL #拒绝所有主机连接SSH

 在/etc/hosts.allow 中添加如下内容。

SSHD: 10.0. 10.1. 10.2. 10.3. #允许深圳和上海的主机连接 SSH

以上配置将允许深圳和上海的主机连接SSH，并拒绝其他所有主机，对于有特殊需求，可按实际情况进行配置。

注：

以上配置立即生效，不需要重启任何服务，且同时满足于SSH连接和SFTP登陆，需谨慎配置。

# 7.3.8.9 SSHD服务管理

# 7.3.8.9.1 启动服务

SFTP使用sshd守护进程（端口号默认是22），启动sshd守护进程后，默认已经启动了SFTP，启动方式如下所示。

 在 RedHat Enterprise Linux Server 6 上:

# service sshd start

 在 RedHat Enterprise Linux Server 7 上:

# systemctl start sshd.service

由于SSHD服务默认已经启动，在配置完SFTP之后，需要使用restart来重启SSHD守护进程，方法如下所示。

 在 RedHat Enterprise Linux Server 6 上:

# service sshd restart

 在 RedHat Enterprise Linux Server 7 上:

# systemctl restart sshd.service

# 7.3.8.9.2 查看服务状态

 在 RedHat Enterprise Linux Server 6 上:

```txt
service sshd status 
```

 在 RedHat Enterprise Linux Server 7 上:

```txt
systemctl status sshd.service 
```

# 7.3.8.9.3 设置 SSHD 开机启动

 在 RedHat Enterprise Linux Server 6 上:

```txt
#chkconfigsshd on 
```

 在 RedHat Enterprise Linux Server 7 上:

```txt
systemctl enable sshd.service 
```

# 7.3.8.9.4 关闭 SFTP 服务

 若是关闭sftp服务，请执行步骤1。  
 在实际应用中，按照行里的安全要求，需要修改sftp的相关配置，请参考“不允许基于GSSAPI 的用户认证”

1. 执行以下命令，编辑/etc/ssh/sshd_config 文件。

```txt
#vim /etc/ssh/sshd_config
注释以下行，编辑完成后，按 Esc 键，输入“:wq”保存退出。
#Subsystem sftp /usr/libexec/openssh/sftp-server
```