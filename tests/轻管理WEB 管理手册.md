# 轻网管交换机

# SKS3200M-8GPY1XF

# Web 管理手册

版本：V1.0 

# 目录

轻网管交换机. 

SKS3200M-8GPY1XF. 1 

Web 管理手册. 

目录. 

1 前言.. . 5 

1.1 目标读者. 5 

1.2 本书约定. 5 

2 登录 Web 页面. . 6 

2.1 登录 Web 网管客户端 . 6 

2.2 客户端界面组成. .6 

2.3 Web 界面导航树. 

3 系统.. . 8 

3.1 系统信息. .8 

3.2 IP 设置. 9 

3.3 账户. . 9 

3.4 端口设置. . 10 

4 配置. .11 

4.1 VLAN.. 11 

4.1.1 802.1Q VLAN. .. 11 

4.1.2 802.1Q VID.. . 12 

4.2 QoS.. .13 

4.2.1 端口到队列. ..14 

4.2.2 队列权重. ..15 

4.3 环路设置. . 16 

4.3.1 环路检测/环路避免 .. 16 

4.3.2 STP 全局. . 17 

4.3.2 STP 端口. . 18 

4.4 IGMP 侦听.. ..19 

4.5 链路聚合. . 20 

4.7 端口镜像. . 22 

4.8 端口隔离. . 22 

4.9 带宽控制.. . 23 

4.10 巨型帧. ..24 

4.11 MAC 约束. . 25 

4.12 EEE.. ..25 

5 安全.. ..26 

5.1 MAC 地址. ..26 

5.1.1 MAC 查找. ..26 

5.1.2 静态 MAC. .. 27 

5.2 风暴控制. . 27 

6 监控.. .28 

6.1 端口统计. . 28 

7 工具. .29 

7.1 固件升级. . 29 

7.2 配置备份. . 30 

7.3 恢复出厂. . 30 

7.4 保存. ..31 

7.5 重启系统. . 31 

7.6 登出. ..31 


修订记录


<table><tr><td>日期</td><td>版本</td><td>描述</td></tr><tr><td>2023-07-01</td><td>V.1.0</td><td>第一版</td></tr></table>

# 1 前言

# 1.1 目标读者

本手册适用于负责安装、配置或维护网络的安装人员和系统管理员。本手册假定您了解 所有网络使用的传输和管理协议。 

本手册也假定您熟知与组网有关的网络设备、协议和接口的专业术语、理论原理、实践 技能以及特定专业知识。同时您还必须有图形用户界面、命令行界面、简单网络管理协议和 Web 浏览器的工作经验。 

# 1.2 本书约定

本手册采用以下约定方式。 

<table><tr><td>GUI 约定</td><td>描述</td></tr><tr><td>说明</td><td>操作内容的描述，进行必要的补充和说明。</td></tr><tr><td>注意</td><td>提醒操作中应注意的事项，不当的操作可能会导致数据丢失或者设备损坏。</td></tr></table>

# 2 登录 Web 页面

# 2.1 登录 Web 网管客户端

用户可通过打开 Web 浏览器，输入交换机缺省地址：http://192.168.10.12，按 Enter 键。 

# 说明：

设备支持浏览器：IE9.0 以上，Chrome23.0 以上，Firefox20.0 以上 

登录交换机时，应使 PC 的 IP 网段与交换机网段一致。首次登录时，设置 PC 的 IP 地址 为 192.168.10.x（x 代表 1~254，除 1），子网掩码设置为 255.255.255.0， 但 PC 的 IP 不 可与交换机相同， 即不能为 192.168.10.12。 

此时出现登录窗口，如下图所示。输入缺省用户名: admin 和密码: admin。单击<登录>按 钮，将看到交换机系统信息。 

![](images/4a920a0b78d11bfa6cba6a1ae130c8fc0703ab8593f9efd7c992d01af884f80a.jpg)


# 2.2 客户端界面组成

Web 网管系统的典型操作界面的介绍，如下图所示。 

![](images/010011cc210a617f79880c3cbb1a418c93470ec16388ff06dc6f26538e943e13.jpg)


# 2.3 Web 界面导航树

Web 网管的菜单主要提供系统、配置、安全、诊断、工具等菜单项。每个菜单选项下 又有子菜单。详细导航树的信息如下： 

<table><tr><td>菜单项</td><td>子菜单</td><td>二级子菜单</td><td>说明</td></tr><tr><td rowspan="4">系统</td><td>系统信息</td><td></td><td>显示端口状态与产品信息</td></tr><tr><td>IP设置</td><td></td><td>配置查看当前设备的管理IP地址</td></tr><tr><td>账户</td><td></td><td>配置查看设备用户信息</td></tr><tr><td>端口设置</td><td></td><td>配置查看设备所有端口信息</td></tr><tr><td rowspan="10">配置</td><td rowspan="2">VLAN</td><td>802.1Q VLAN</td><td>配置查看端口PVID VLAN</td></tr><tr><td>802.1Q VID</td><td>配置端口VID允许接受帧类型</td></tr><tr><td rowspan="2">QOS</td><td>端口到队列</td><td>配置查看端口队列</td></tr><tr><td>队列权重</td><td>配置查看队列权重</td></tr><tr><td rowspan="3">环路设置</td><td>环路协议</td><td>配置查看环路检测</td></tr><tr><td>STP全局</td><td>配置查看生成树全局信息</td></tr><tr><td>STP端口</td><td>配置查看生成树端口信息</td></tr><tr><td>IGMP侦听</td><td></td><td>配置查看IGMP Snooping</td></tr><tr><td>链路聚合</td><td></td><td>配置查看链路聚合</td></tr><tr><td>端口镜像</td><td></td><td>配置查看端口镜像</td></tr><tr><td rowspan="8"></td><td>端口隔离</td><td></td><td>配置查看端口隔离</td></tr><tr><td>带宽控制</td><td></td><td>配置查看端口速率限制</td></tr><tr><td>巨型帧</td><td></td><td>配置查看端口Jumbo帧</td></tr><tr><td>MAC约束</td><td></td><td>配置查看端口MAC约束</td></tr><tr><td>EEE</td><td></td><td>配置查看端口EEE节能状态和信息</td></tr><tr><td rowspan="2">MAC地址</td><td>MAC查找</td><td>查看MAC地址信息</td></tr><tr><td>静态MAC</td><td>配置查看静态MAC信息</td></tr><tr><td>风暴控制</td><td></td><td>配置查看风暴抑制信息</td></tr><tr><td>监控</td><td>端口统计</td><td></td><td>查看端口统计</td></tr><tr><td rowspan="6">系统工具</td><td>固件升级</td><td></td><td>更新升级设备软件版本</td></tr><tr><td>配置备份</td><td></td><td>更新升级设配置文件</td></tr><tr><td>复位</td><td></td><td>重置系统</td></tr><tr><td>保存</td><td></td><td>保存配置</td></tr><tr><td>重启</td><td></td><td>重启系统</td></tr><tr><td>登出</td><td></td><td>登出系统</td></tr></table>

# 3 系统

# 3.1 系统信息

根据所连接的交换机，能够非常直观地显示出该款交换机前面板上各端口的信息与产品 信息，其显示内容包括：产品型号，版本，MAC 地址等等。 

操作步骤： 

1. 单击导航树中的“系统 $>$ 系统信息”菜单，进入系统信息查看界面，如下图所示： 

系统信息 

<table><tr><td>设备类型</td><td>SKS3200M-8GPY1XF</td></tr><tr><td>MAC 地址</td><td>00:E0:4C:00:00:00</td></tr><tr><td>IP 地址</td><td>192.168.10.12</td></tr><tr><td>子网掩码</td><td>255.255.255.0</td></tr><tr><td>网关</td><td>192.168.10.1</td></tr><tr><td>固件版本</td><td>V0.3</td></tr><tr><td>固件日期</td><td>Jun 30 2023</td></tr><tr><td>硬件版本</td><td>V1.1</td></tr></table>

# 3.2 IP 设置

配置和查看设备的管理 IP 地址。 

操作步骤： 

1. 单击导航树中的“系统 > IP 设置”菜单，进入 IP 设置界面，如下图所示： 

-IP地址设置 

<table><tr><td>DHCP设置</td><td>关闭</td></tr><tr><td>IP地址</td><td>192.168.10.12</td></tr><tr><td>子网掩码</td><td>255.255.255.0</td></tr><tr><td>网关</td><td>192.168.10.1</td></tr></table>

应用 

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>DHCP 设置</td><td>Enable: 使能 DHCP 获取
Disable: 去使能 DHCP 获取</td></tr><tr><td>IP 地址</td><td>管理 IP 地址</td></tr><tr><td>子网掩码</td><td>IP 地址掩码</td></tr><tr><td>网关</td><td>IP 地址的网关</td></tr></table>

# 3.3 账户

用户可以检查和修改交换机的当前用户名、密码 

操作步骤： 

1. 单击导航树中的“系统 $>$ 用户账号”菜单，进入界面，如下图所示： 

用户账户 

![](images/e8749c9b681f81a6f50b9f7da9703dccae437cd8dd858e8a46353742f11463fb.jpg)


应用 

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>用户名</td><td>账户名称</td></tr><tr><td>新密码</td><td>账户密码</td></tr><tr><td>新密码</td><td>账户密码重新输入</td></tr></table>

# 3.4 端口设置

查询和配置以太网端口 

# 操作步骤：

1. 单击导航树中的“系统 $>$ 端口设置”菜单，进入界面，如下图所示： 

端口设置 

![](images/fe7f57ea7d77ac4d673e51c015aa890c312aad36e6323e3c384933acfedd9932.jpg)



应用


![](images/d3e997bc9ee1772d54a5134a38e07677a49512977389e427ff5bec62177258ca.jpg)



应用


<table><tr><td rowspan="2">端口</td><td rowspan="2">状态</td><td colspan="2">速率/双工</td><td colspan="2">流控</td></tr><tr><td>配置</td><td>实际</td><td>配置</td><td>实际</td></tr><tr><td>端口1</td><td>打开</td><td>自动</td><td>掉线</td><td>关闭</td><td>关闭</td></tr><tr><td>端口2</td><td>打开</td><td>自动</td><td>掉线</td><td>关闭</td><td>关闭</td></tr><tr><td>端口3</td><td>打开</td><td>自动</td><td>掉线</td><td>关闭</td><td>关闭</td></tr><tr><td>端口4</td><td>打开</td><td>自动</td><td>掉线</td><td>关闭</td><td>关闭</td></tr><tr><td>端口5</td><td>打开</td><td>自动</td><td>1000Full</td><td>关闭</td><td>关闭</td></tr><tr><td>端口6</td><td>打开</td><td>自动</td><td>掉线</td><td>关闭</td><td>关闭</td></tr><tr><td>端口7</td><td>打开</td><td>自动</td><td>掉线</td><td>关闭</td><td>关闭</td></tr><tr><td>端口8</td><td>打开</td><td>自动</td><td>掉线</td><td>关闭</td><td>关闭</td></tr><tr><td>端口9</td><td>打开</td><td>自动</td><td>掉线</td><td>关闭</td><td>关闭</td></tr></table>

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>状态</td><td>端口开关</td></tr><tr><td>速度/双工</td><td>端口速率</td></tr><tr><td>流控</td><td>流控开关</td></tr></table>

# 4 配置

# 4.1 VLAN

VLAN 的组成不受物理位置的限制，因此同一 VLAN 内的主机也无须放置在同一物理 空间里。如下图所示，VLAN 把一个物理上的 LAN 划分成多个逻辑上的 LAN ，每个 VLAN 是一个广播域。VLAN 内的主机间通过传统的以太网通信方式即可进行报文的交互，而处在 不同 VLAN 内的主机之间如果需要通信，则必须通过路由器或三层交换机等网络层设备才能 够实现。 

![](images/bee0575e5782dd013e8d2b4c90c73863585c47de4c8d025b15cfa65410c3fa71.jpg)


与传统以太网相比，VLAN 具有如下的优点： 

控制广播域的范围：局域网内的广播报文被限制在一个 VLAN 内，节省了带宽，提高 了网络处理能力。 

增强了 LAN 的安全性：由于报文在数据链路层被 VLAN 划分的广播域所隔离，因此各 个 VLAN 内的主机间不能直接通信，需要通过路由器或三层交换机等网络层设备对报 文进行三层转发。 

灵活创建虚拟工作组：使用 VLAN 可以创建跨物理网络范围的虚拟工作组，当用户的 物理位置在虚拟工作组范围内移动时，不需要更改网络配置即可以正常访问网络。 

此管理型交换机支持 802.1Q VLAN、基于端口的 VLAN。在缺省配置时，VLAN 为 802.1Q VLAN 模式。 

# 4.1.1 802.1Q VLAN

该设置页面功能相当于 Hybrid 接口类型 操作步骤： 

1. 单击导航树中的“配置 $>$ VLAN >802.1Q VLAN ”菜单，进入界面，如下图所示： 

-802.1QVLAN 

![](images/dc0c1b274bbce171e501d669bd2508cbc4002cd10f7ca89f7ccf94c1f43d51c1.jpg)



添加/修改


![](images/ac2826ae476315fe481f21fca4a4701b01e7a601d99a6aef7df5d227d125747e.jpg)



删除 全部选择


界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>VLAN</td><td>端口的默认 VLAN</td></tr><tr><td>VLAN 名字</td><td>VLAN 名称描述</td></tr></table>

# 4.1.2 802.1Q VID

操作步骤： 

1. 单击导航树中的“配置 $>$ VLAN >802.1Q VID ”菜单，进入界面，如下图所示： 

VLAN端口设置 

![](images/5ccaf8a3358a144d3096147df92754129be052e2726a9f659a0ee58efdc63384.jpg)



应用


<table><tr><td>端口</td><td>端口VLAN</td><td>接受帧类型</td></tr><tr><td>端口1</td><td>1</td><td>全部</td></tr><tr><td>端口2</td><td>1</td><td>全部</td></tr><tr><td>端口3</td><td>1</td><td>全部</td></tr><tr><td>端口4</td><td>1</td><td>全部</td></tr><tr><td>端口5</td><td>1</td><td>全部</td></tr><tr><td>端口6</td><td>1</td><td>全部</td></tr><tr><td>端口7</td><td>1</td><td>全部</td></tr><tr><td>端口8</td><td>1</td><td>全部</td></tr><tr><td>端口9</td><td>1</td><td>全部</td></tr></table>

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>端口 VID</td><td>端口的 VLAN 标识</td></tr><tr><td>允许接受帧类型</td><td>所有帧类型、只接受带标签的包、只接受不带标签的包</td></tr></table>

# 4.2 QoS

QoS（Quality of Service）用于评估服务方满足客户服务需求的能力，在 Internet 中， QoS 用于评估网络传送分组的服务能力。由于网络提供的服务是多样的，因此可以基于不 同方面进行评估。通常所说的 QoS，是对分组投递过程中可为带宽、时延、时延抖动、丢 包率等核心需求提供支持的服务能力的评估。带宽，又可称为吞吐量，表示一定时间内业务 流的平均速率，单位通常是 Kbit/s。时延，表示业务流穿过网络时需要的平均时间。对于网 络中的一个设备来说，一般将时延的需求理解为几种等级。例如分为两种时延等级，通过优 先队列的调度方法使得高优先级的业务尽可能快地获得服务，而低优先级的业务则需要等待 没有高优先级业务时才能获得服务。时延抖动，表示业务流穿过网络的时间的变化。丢包率， 表示业务流在传送过程中的丢失比率。由于现代的传输系统具有很高的可靠性，信息的丢失 往往发生在网络出现拥塞时。最常见的情况是队列溢出导致分组丢失。在传统的 IP 网络中， 所有的报文都被无区别的等同对待，每个网络设备对所有的报 文均采用先入先出的策略进 行处理，尽最大的努力（Best-Effort）将报文送到目的地，但对报文传送的可靠性、传送延 迟等性能不提供任何保证。 

网络发展日新月异，随着 IP 网络上新应用的不断出现，对 IP 网络的服务质量也提出了 新的要求。例如 VoIP 和视频等时延敏感业务对报文的传输时延提出了较高要求。如果报文 传送延时太长，将是用户所不能接受的。为了支持具有不同服务需求的语音、视频以及数据 等业务，要求网络能够区分出不同的业务类型，进而为之提供相应的服务。 

传统 IP 网络的尽力服务不可能识别和区分出网络中的各种业务类型，而具备业务类型 的区分能力正是为不同的业务提供差异化服务的前提，所以传统网络的尽力服务模式已不能 满足应用的需要。QoS 技术的出现便致力于解决这个问题。QoS 可以对网络流量进行调控， 避免并管理网络拥塞，减少报文丢包率。同时支持为用户提供专用带宽，为不同业务提供不 同的服务质量等，完善了网络的服务能力。 

不同的报文使用不同的 QoS 优先级，例如 VLAN 报文使用 802.1p，或称 CoS（Class of Service）字段，IP 报文使用 DSCP。当报文经过不同网络时，为了保持报文的优先级，需要 在连接不同网络的网关处配置这些优先级字段的映射关系。 

# VLAN 帧头中的 802.1p 优先级

通常二层设备之间交互 VLAN 帧。根据 IEEE 802.1Q 定义，VLAN 帧头中的 PRI 字段（即 802.1p 优先级），或称 CoS（Class of Service）字段，标识了服务质量需求。 

VLAN 帧中的 802.1p 优先级 

![](images/4d944cec336d9f9f2fc1439cc26328fc661a55c0c2f521f56759a5ce28b3fd44.jpg)


在 802.1Q 头部中包含 3 比特长的 PRI 字段。PRI 字段定义了 8 种业务优先级 CoS，按 照优先级从高到低顺序取值为 7、6、……、1 和 0。 

# IP Precedence/DSCP 字段

根据 RFC791 定义，IP 报文头 ToS（Type of Service）域由 8 个比特组成，其中 3 个比 特的 Precedence 字段标识了 IP 报文的优先级，Precedence 在报文中的位置如图所示。 

IP Precedence/DSCP 字段 

![](images/1553b79aeb9cdd15c40408a7228301b48d5b0c73f5b2b8435c79460e700ab316.jpg)


比特 0～2 表示 Precedence 字段，代表报文传输的 8 个优先级，按照优先级从高到低顺序 取值为 7、6、……、1 和 0。最高优先级是 7 或 6，经常是为路由选择或更新网络控制通信 保留的，用户级应用仅能使用 0 级 $\sim 5$ 级。除了 Precedence 字段外，ToS 域中还包括 D、T、 R 三个比特：D 比特表示延迟要求（Delay，0 代表正常延迟，1 代表低延迟）。T 比特表示 吞吐量（Throughput，0 代表正常吞吐量，1 代表高吞吐量）。R 比特表示可靠性（Reliability， 0 代表正常可靠性，1 代表高可靠性）。ToS 域中的比特 6 和 7 保留。 

RFC1349重新定义了IP报文中的ToS域，增加了C比特，表示传输开销（Monetary Cost）。 之后，IETF DiffServ 工作组在 RFC2474 中将 IPv4 报文头 ToS 域中的比特 $0 \sim 5$ 重新定义为 DSCP，并将 ToS 域改名为 DS（Differentiated Service）字节。DSCP 在报文中的位置如上图 所示。DS 字段的前 6 位（0 位～5 位）用作区分服务代码点 DSCP（DS Code Point），高 2 位（6 位、7 位）是保留位。DS 字段的低 3 位（0 位 $\sim 2$ 位）是类选择代码点 CSCP（Class Selector Code Point），相同的 CSCP 值代表一类 DSCP。DS 节点根据 DSCP 的值选择相应的 PHB （Per-Hop Behavior）。 

# 4.2.1 端口到队列

为数据帧的不同标记设置处理优先级 

# 操作步骤：

1. 单击导航树中的“配置 $> \mathrm { Q O S } >$ 端口到队列”菜单，进入界面，如下图所示： 

端口到队列设置 

![](images/d0664907aad667f03e11d5f972b452e65bf4ec23f47c570931f1d2af5f6ba34f.jpg)



应用


<table><tr><td>端口</td><td>队列</td></tr><tr><td>端口1</td><td>1</td></tr><tr><td>端口2</td><td>1</td></tr><tr><td>端口3</td><td>1</td></tr><tr><td>端口4</td><td>1</td></tr><tr><td>端口5</td><td>1</td></tr><tr><td>端口6</td><td>1</td></tr><tr><td>端口7</td><td>1</td></tr><tr><td>端口8</td><td>1</td></tr><tr><td>端口9</td><td>1</td></tr></table>

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>队列</td><td>范围 1-8</td></tr></table>

# 4.2.2 队列权重

权重为严格优先级时相当于 SP，权重为 1-15 的值时相当于 WRR（加权循环调度算法） 

# 操作步骤：

1. 单击导航树中的“配置 $> \mathrm { Q O S } >$ 队列权重”菜单，进入界面，如下图所示： 

一队列权重设置 

![](images/f494666f847e2ceae5180a4c51966013b2ce8c5554191437abd89cad73df7a88.jpg)


<table><tr><td>队列</td><td>权重</td></tr><tr><td>1</td><td>严格优先级</td></tr><tr><td>2</td><td>严格优先级</td></tr><tr><td>3</td><td>严格优先级</td></tr><tr><td>4</td><td>严格优先级</td></tr><tr><td>5</td><td>严格优先级</td></tr><tr><td>6</td><td>严格优先级</td></tr><tr><td>7</td><td>严格优先级</td></tr><tr><td>8</td><td>严格优先级</td></tr></table>

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>权重</td><td>默认为严格优先级，权重范围1-15</td></tr></table>

# 4.3 环路设置

# 4.3.1 环路检测/环路避免

设备通过发送环路检测报文并检测其是否返回本设备（不要求收、发端口为同一端口）以确 认是否存在环路。若某端口收到了由本设备发出的环路检测报文，就认定该端口所在链路存 在环路。当网络中出现环路时，对应的端口 LED 灯将会闪烁告警（启用环路避免时会阻塞 环路），以便给网络管理员释放该端口存在环路情况 

# 操作步骤：

1. 单击导航树中的“配置 $>$ 环路设置 $>$ 环路检测”菜单，进入界面，如下图所示： 

环路协议设置 

![](images/096e3ce5859cd73af2d6f1be65e57a369dffc1c72cee228397ec7f1d54b7050e.jpg)


环路协议设置 

<table><tr><td>环路功能</td><td colspan="2">环路检测</td></tr><tr><td>时间间隔(1~32767)</td><td>2</td><td>秒</td></tr><tr><td>恢复时间(0 or 4~255)</td><td>10</td><td>秒</td></tr></table>

环路协议设置 

<table><tr><td>环路功能</td><td>环路避免</td></tr><tr><td>时间间隔(1~32767)</td><td>2秒</td></tr><tr><td>恢复时间(0 or 4~255)</td><td>10秒</td></tr></table>

应用 

<table><tr><td>端口</td><td>状态</td></tr><tr><td>端口1</td><td rowspan="6">关闭</td></tr><tr><td>端口2</td></tr><tr><td>端口3</td></tr><tr><td>端口4</td></tr><tr><td>端口5</td></tr><tr><td>端口6</td></tr></table>

<table><tr><td>端口</td><td>环路使能</td><td>环路状态</td></tr><tr><td>端口1</td><td>关闭</td><td>转发</td></tr><tr><td>端口2</td><td>关闭</td><td>转发</td></tr><tr><td>端口3</td><td>关闭</td><td>转发</td></tr><tr><td>端口4</td><td>关闭</td><td>转发</td></tr><tr><td>端口5</td><td>关闭</td><td>转发</td></tr><tr><td>端口6</td><td>关闭</td><td>转发</td></tr><tr><td>端口7</td><td>关闭</td><td>转发</td></tr><tr><td>端口8</td><td>关闭</td><td>转发</td></tr><tr><td>端口9</td><td>关闭</td><td>转发</td></tr></table>

应用 

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>环路协议</td><td>关闭、环路检测、环路避免、生成树</td></tr></table>

# 4.3.2 STP 全局

快速生成树协议（RSTP） 用于在局域网中消除数据链路层物理环路，其核心是快速生 成树算法。RSTP 完全向下兼容 STP 协议，除了和传统的 STP 协议一样具有避免回路、动态 管理冗余链路的功能外，RSTP 极大的缩短了拓扑收敛时间，在理想的网络拓扑规模下，所 有交换设备均支持 RSTP 协议且配置得当时，拓扑发生变化（链路 UP/DOWN）后恢复稳定 的时间可以控制在秒级。RSTP 的主要功能可以归纳如下： 

1、 发现并生成局域网的一个最佳树型拓扑结构； 

2、 发现拓扑故障并随之进行恢复，自动更新网络拓扑结构，启用备份链路，同时保持 最佳树型结构； 

操作步骤： 

1. 单击导航树中的“配置 $>$ 环路协议 > STP 全局”菜单，进入界面，如下图所示： 

生成树设置 

<table><tr><td>生成树状态</td><td colspan="2">关闭</td></tr><tr><td>版本</td><td></td><td>RSTP</td></tr><tr><td>优先级</td><td></td><td>32768</td></tr><tr><td>最大老化时间</td><td>20</td><td>(6~40 Sec)</td></tr><tr><td>Hello 时间</td><td>2</td><td>(1~10 Sec)</td></tr><tr><td>转发延时</td><td>15</td><td>(4~30 Sec)</td></tr><tr><td>根优先级</td><td colspan="2">32768</td></tr><tr><td>根MAC地址</td><td colspan="2">00:E0:4C:00:00:00</td></tr><tr><td>根路径消耗</td><td colspan="2">0</td></tr><tr><td>根端口</td><td colspan="2">None</td></tr><tr><td>根最大老化时间</td><td colspan="2">20 Sec</td></tr><tr><td>根欢迎时间</td><td colspan="2">2 Sec</td></tr><tr><td>根转发延时</td><td colspan="2">15 Sec</td></tr></table>

应用 

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>版本</td><td>配置查看 STP 模式</td></tr><tr><td>最大老化时间</td><td>配置查看最大老化时间</td></tr><tr><td>欢迎时间</td><td>配置查看欢迎时间</td></tr><tr><td>转发延时</td><td>配置查看转发延时时间</td></tr></table>

# 4.3.2 STP 端口

# 操作步骤：

1. 单击导航树中的“配置 $>$ 环路协议 > STP 端口”菜单，进入界面，如下图所示： 

生成树设置 

![](images/7dacdf1c0046f990dd468a245a4436af7482f6ada854a2761f03599743fc30f4.jpg)



应用


<table><tr><td rowspan="2">端口</td><td rowspan="2">状态</td><td rowspan="2">角色</td><td colspan="2">路径消耗</td><td rowspan="2">优先级</td><td colspan="2">点到点</td><td colspan="2">边缘</td></tr><tr><td>设置</td><td>实际</td><td>设置</td><td>实际</td><td>设置</td><td>实际</td></tr><tr><td>端口1</td><td>转发</td><td>禁用</td><td>自动</td><td>2000000</td><td>128</td><td>真</td><td>是</td><td>否</td><td>否</td></tr><tr><td>端口2</td><td>转发</td><td>禁用</td><td>自动</td><td>2000000</td><td>128</td><td>真</td><td>是</td><td>否</td><td>否</td></tr><tr><td>端口3</td><td>转发</td><td>禁用</td><td>自动</td><td>2000000</td><td>128</td><td>真</td><td>是</td><td>否</td><td>否</td></tr><tr><td>端口4</td><td>转发</td><td>禁用</td><td>自动</td><td>2000000</td><td>128</td><td>真</td><td>是</td><td>否</td><td>否</td></tr><tr><td>端口5</td><td>转发</td><td>禁用</td><td>自动</td><td>20000</td><td>128</td><td>真</td><td>是</td><td>否</td><td>否</td></tr><tr><td>端口6</td><td>转发</td><td>禁用</td><td>自动</td><td>2000000</td><td>128</td><td>真</td><td>是</td><td>否</td><td>否</td></tr><tr><td>端口7</td><td>转发</td><td>禁用</td><td>自动</td><td>2000000</td><td>128</td><td>真</td><td>是</td><td>否</td><td>否</td></tr><tr><td>端口8</td><td>转发</td><td>禁用</td><td>自动</td><td>2000000</td><td>128</td><td>真</td><td>是</td><td>否</td><td>否</td></tr><tr><td>端口9</td><td>转发</td><td>禁用</td><td>自动</td><td>2000000</td><td>128</td><td>真</td><td>是</td><td>否</td><td>否</td></tr></table>

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>路径开销</td><td>配置查看端口路径开销</td></tr><tr><td>优先级</td><td>配置查看端口优先级</td></tr><tr><td>点到点</td><td>配置查看 P2P</td></tr><tr><td>边缘</td><td>配置查看边缘端口</td></tr></table>

# 4.4 IGMP 侦听

IGMP 侦听（Internet Group Management Protocol Snooping）是运行在二层设备上的 组播约束机制，用于管理和控制组播组。 

运行 IGMP 侦听的二层设备通过对收到的 IGMP 报文进行分析，为端口和 MAC 组播地 址建立起映射关系，并根据这样的映射关系转发组播数据。 

如下图所示，当二层设备没有运行 IGMP 侦听时，组播数据在二层被广播；当二层设 备运行了 IGMP 侦听后，已知组播组的组播数据不会在二层被广播，而在二层被组播给指定 的接收者，但是未知组播数据仍然会在二层广播。 

![](images/cf1e7e14505171e961f511d6850fce1a8272b02d4768b64b64757632582f8b80.jpg)


![](images/99569d082fa8c4fdc6526a302a70e4c69dc7ef09bb58703a4a4e7c26103f9790.jpg)


操作步骤： 

1. 单击导航树中的“配置 $>$ IGMP”菜单，进入界面，如下图所示： 

![](images/2ac1b9b5f1abd5f49db694f71724dcdff2cff4236dd33957573cc238c1006e61.jpg)


界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>打开</td><td>使能或去使能IGMP Snooping</td></tr><tr><td>显示IGMP表</td><td>查询IGMP组信息</td></tr></table>

# 4.5 链路聚合

链路聚合（Link Aggregation）是将一组物理接口捆绑在一起作为一个逻辑接口来增加 带宽和可靠性的一种方法。 

链路聚合组 LAG（Link Aggregation Group）是指将若干条以太链路捆绑在一起所形成 的逻辑链路，简写为 Eth-Trunk。 

随着网络规模不断扩大，用户对链路的带宽和可靠性提出越来越高的要求。在传统技术 中，常用更换高速率的接口板或更换支持高速率接口板的设备的方式来增加带宽，但这种方 案需要付出高额的费用，而且不够灵活。 

采用链路聚合技术可以在不进行硬件升级的条件下，通过将多个物理接口捆绑为一个逻 辑接口，实现增加链路带宽的目的。链路聚合的备份机制能有效提高可靠性，同时，还可以 实现流量在不同物理链路上的负载分担。 

如下图所示，SwitchA 与 SwitchB 之间通过三条以太网物理链路相连，将这三条链路捆 绑在一起，就成为了一条 Eth-Trunk 逻辑链路，这条逻辑链路的带宽等于原先三条以太网物 理链路的带宽总和，从而达到了增加链路带宽的目的；同时，这三条以太网物理链路相互备 份，有效地提高了链路的可靠性。 

![](images/5bd2bc00907781e39e23e02cc77d6f270075f77239560763a53977fca097bc59.jpg)


# 操作步骤：

1. 单击导航树中的“配置 $>$ 链路聚合”菜单，进入界面，如下图所示： 

![](images/e56a4b6859fe093241b8ef9cb16097ed204c827c78194ddbf5778252170d4aaa.jpg)


界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>聚合号</td><td>聚合组ID，最大支持2组</td></tr><tr><td>端口号</td><td>聚合组成员端口，最大支持4个成员</td></tr></table>

# 4.7 端口镜像

端口镜像是把交换机被镜像端口的报文复制到监控端口；监控端口通常会接入数据检测 设备，用户利用这些设备分析被镜像端口接收到的报文，进行网络监控和故障排除。 

1. 单击导航树中的“配置 $>$ 端口镜像”菜单，进入界面，如下图所示： 

端口镜像设置 

![](images/f29f898d9a9c24768efcd33bbca0200b23e7fd96cf9a75df00016d260e648303.jpg)



应用


![](images/45d4c12196f742ecbc8153e7ad1faa7f57afadadd74fac0949a5ec4d9b4326e6.jpg)



删除


界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>镜像方向</td><td>使能或去使能端口镜像，支持入方向，出方向和双方向</td></tr><tr><td>监控端口</td><td>只能选择一个普通物理端口，不包括链路聚合端口和源端口。</td></tr><tr><td>被监控端口列表</td><td>镜像源端口列表</td></tr></table>

# 4.8 端口隔离

端口流量之间有时不需要互相通信，但是广播、组播等报文会泛洪到各个端口之间，此 时可以通过端口隔离功能来实现端口与端口之间的报文隔离。 

1. 单击导航树中的“配置 $>$ 端口隔离”菜单，进入界面，如下图所示： 

端口隔离设置 

![](images/59b2c6287cd2fd1b7318b58bad652afc67fa4a56f899c5703602be091770d4f9.jpg)



应用


<table><tr><td>端口</td><td>端口隔离列表</td></tr><tr><td>端口1</td><td>1-9</td></tr><tr><td>端口2</td><td>1-9</td></tr><tr><td>端口3</td><td>1-9</td></tr><tr><td>端口4</td><td>1-9</td></tr><tr><td>端口5</td><td>1-9</td></tr><tr><td>端口6</td><td>1-9</td></tr><tr><td>端口7</td><td>1-9</td></tr><tr><td>端口8</td><td>1-9</td></tr><tr><td>端口9</td><td>1-9</td></tr></table>

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>端口</td><td>端口列表</td></tr><tr><td>端口隔离列表</td><td>对应端口报文允许转发到哪个端口</td></tr></table>

# 4.9 带宽控制

配置接口限速就是限制物理接口向外发送数据的速率。在流量从接口发出前，在接口的 出方向上配置限速，对流出的所有报文流量进行控制。 

1. 单击导航树中的“配置 $>$ 带宽控制”菜单，进入界面，如下图所示： 

带宽控制设置 

![](images/fcb864568e4733993fb773c1b427f153956d2788fb6e45f30f74bebfe747055e.jpg)



应用


![](images/5929740451fd517a05b4d2ad45f0cb4fa42801a127a957ac6e5675f58b2219cb.jpg)



应用


<table><tr><td>端口</td><td>入口速率(Kbit/sec)</td><td>出口速率(Kbit/sec)</td></tr><tr><td>端口1</td><td>不限制</td><td>不限制</td></tr><tr><td>端口2</td><td>不限制</td><td>不限制</td></tr><tr><td>端口3</td><td>不限制</td><td>不限制</td></tr><tr><td>端口4</td><td>不限制</td><td>不限制</td></tr><tr><td>端口5</td><td>不限制</td><td>不限制</td></tr><tr><td>端口6</td><td>不限制</td><td>不限制</td></tr><tr><td>端口7</td><td>不限制</td><td>不限制</td></tr><tr><td>端口8</td><td>不限制</td><td>不限制</td></tr><tr><td>端口9</td><td>不限制</td><td>不限制</td></tr></table>

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>端口</td><td>端口列表</td></tr><tr><td>类型</td><td>入口\出口</td></tr><tr><td>状态</td><td>使能或去使能端口限制</td></tr><tr><td>速率</td><td>速率限制值，范围:16到1,000,000 Kbit</td></tr></table>

# 4.10 巨型帧

设置端口最大 MTU 

操作步骤： 

1. 单击导航树中的“配置 $>$ 巨型帧”菜单进入界面，如下图所示： 

-巨型帧设置 

![](images/e0c49eaa8435d2f0470b232bba237e06ca561d61fbc8009d7ea682f18c7ef41b.jpg)


界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>巨型帧设置</td><td>设置端口MTU</td></tr></table>

# 4.11 MAC 约束

MAC 地址限制功能可以限制各端口下 MAC 地址学习数量，当超过限制数时不再学习 MAC 地址 

操作步骤： 

1. 单击导航树中的“配置 $>$ MAC 约束”菜单进入界面，如下图所示： 

-MAC限制设置 

![](images/533399e25ca9b1386a0ad4cc7b0a5462298050d257a8f91e18c4cf6a4b1923e3.jpg)



应用


<table><tr><td>端口</td><td>限制条数</td></tr><tr><td>端口1</td><td>不限制</td></tr><tr><td>端口2</td><td>不限制</td></tr><tr><td>端口3</td><td>不限制</td></tr><tr><td>端口4</td><td>不限制</td></tr><tr><td>端口5</td><td>不限制</td></tr><tr><td>端口6</td><td>不限制</td></tr><tr><td>端口7</td><td>不限制</td></tr><tr><td>端口8</td><td>不限制</td></tr><tr><td>端口9</td><td>不限制</td></tr></table>

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>状态</td><td>使能或去使能 MAC 地址学限制</td></tr><tr><td>限制条目</td><td>MAC 学习限制数值</td></tr></table>

# 4.12 EEE

使能 EEE（Energy Efficient Ethernet）节能功能后，如果在连续一段时间内接口状态始 终为 up 且没有收发任何报文，则接口自动进入低功耗模式；当接口需要收发报文时，接口 又自动恢复到正常工作模式，从而达到节能的效果。 

操作步骤： 

1. 单击导航树中的“配置 $>$ EEE”菜单进入界面，如下图所示： 

![](images/14dd9c6f57c54be4c31b9205b61f93ac5bde419f9e6e6a8d538a9480b0300126.jpg)


# 5 安全

# 5.1 MAC 地址

以太网交换机的主要功能是在数据链路层对报文进行转发，也就是根据报文的目的 MAC 地址将报文输出到相应的端口。MAC 地址转发表是一张包含了 MAC 地址与转发端 口对应关系的二层转发表，是以太网交换机实现二层报文快速转发的基础。 

MAC 地址转发表的表项中包含如下信息： 

目的 MAC 地址 

$\bullet$ 端口所属的 VLAN ID 

本设备上的转发出端口编号 

以太网交换机在转发报文时，根据 MAC 地址表项信息，会采取以下两种转发方式： 

 单播方式：当 MAC 地址转发表中包含与报文目的 MAC 地址对应的表项时，交换机 直接将报文从该表项中的转发出端口发送。 

广播方式：当交换机收到目的地址为全 F 的报文，或 MAC 地址转发表中没有包含对 应报文目的 MAC 地址的表项时，交换机将采取广播方式将报文向除接收端口外的所 有端口转发。 

# 5.1.1 MAC 查找

在该页，可以查看 MAC 地址表信息，为适应网络的变化，MAC 地址表需要不断更新。 MAC 地址表中自动生成的表项并非永远有效，每一条表项都有一个生存周期，到达生存周 期仍得不到刷新的表项将被删除，这个生存周期被称作老化时间。如果在到达生存周期前记 录被刷新，则该表项的老化时间重新计算。 

1. 单击导航树中的“安全 $>$ MAC 地址 > MAC 查找”菜单进入界面，如下图所示： 

-MAC地址信息 

<table><tr><td>编号</td><td>MAC 地址</td><td>VLAN ID</td><td>类型</td><td>端口</td></tr><tr><td>1</td><td>00:0E:C6:3C:0E:1F</td><td>1</td><td>动态</td><td>5</td></tr></table>

清空动态MAC 

![](images/74653025a9db3b3fe0a74bb5f5a2650b5fb246028d7d5e871e1ce6c08df235a2.jpg)


注意：MAC 查找显示等待过程会与设备中断通信 

# 5.1.2 静态 MAC

静态表项由用户手工配置，并下发到各接口板，表项不老化。该设置页面还可以对源、 目 MAC 进行过滤，配置后所有端口生效 

1. 单击导航树中的“安全 $>$ MAC 地址 $>$ 静态 MAC”菜单进入界面，如下图所示： 

# 静态MAC设置

![](images/bd416beef054990fad190a2c6ac92cd2ce8bd169d78f4f4b5abdaf4ead0e5609.jpg)



添加


MAC地址 

VLAN ID 

选 

删除 

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>MAC 地址</td><td>MAC 地址 e.g.: HH:HH:HH:HH:HH</td></tr><tr><td>VLAN ID</td><td>指定的 VLAN</td></tr><tr><td>端口</td><td>静态 MAC 绑定端口列表</td></tr></table>

# 5.2 风暴控制

风暴控制按以下形式来防止广播、未知组播以及未知单播报文产生广播风暴。设备支持 对接口下的这三类报文分别按包速率进行风暴控制。在一个检测时间间隔内，设备监控接口 下接收的三类报文的平均速率并和配置的最大阈值相比较，当报文速率大于配置的最大阈值 时，设备会对该接口进行风暴控制，执行配置好的风暴控制动作。 

当设备某个二层以太接口收到广播、组播或未知单播报文时，如果根据报文的目的 MAC 地址设备不能明确报文的出接口，设备会向同一 VLAN（Virtual Local Area Network）内的 其他二层以太接口转发这些报文，这样可能导致广播风暴，降低设备转发性能。 

引入风暴抑制特性，可以控制这三类报文流量，防范广播风暴。 

操作步骤： 

1. 单击导航树中的“安全 $>$ 广播风暴”菜单进入界面，如下图所示： 

风暴控制设置 

![](images/7214f66f4877733a7ba658b52df684ce035dece35e3ed2df1af4f7f0d7d2ed05.jpg)



应用


![](images/0fb95e98656969a4bc5b66f69cd26eba78ac870132dce5f67d7f0088160a51f5.jpg)



应用


<table><tr><td>端口</td><td>广播 (kbps)</td><td>已知组播 (kbps)</td><td>未知单播 (kbps)</td><td>未知组播 (kbps)</td></tr><tr><td>端口1</td><td>关闭</td><td>关闭</td><td>关闭</td><td>关闭</td></tr><tr><td>端口2</td><td>关闭</td><td>关闭</td><td>关闭</td><td>关闭</td></tr><tr><td>端口3</td><td>关闭</td><td>关闭</td><td>关闭</td><td>关闭</td></tr><tr><td>端口4</td><td>关闭</td><td>关闭</td><td>关闭</td><td>关闭</td></tr><tr><td>端口5</td><td>关闭</td><td>关闭</td><td>关闭</td><td>关闭</td></tr><tr><td>端口6</td><td>关闭</td><td>关闭</td><td>关闭</td><td>关闭</td></tr><tr><td>端口7</td><td>关闭</td><td>关闭</td><td>关闭</td><td>关闭</td></tr><tr><td>端口8</td><td>关闭</td><td>关闭</td><td>关闭</td><td>关闭</td></tr><tr><td>端口9</td><td>关闭</td><td>关闭</td><td>关闭</td><td>关闭</td></tr></table>

界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>风暴类型</td><td>广播、已知组播、未知单播、未知组播</td></tr><tr><td>端口</td><td>端口列表</td></tr><tr><td>状态</td><td>使能/去使能</td></tr><tr><td>速度</td><td>风暴抑制值</td></tr></table>

# 6 监控

# 6.1 端口统计

查询端口统计信息 

操作步骤： 

1. 单击导航栏中“监控 $>$ 端口统计”菜单，进入端口配置页面： 

端口统计 

<table><tr><td>端口</td><td>状态</td><td>连接状态</td><td>发送统计</td><td>发送错误包统计</td><td>接收统计</td><td>接收错误包统计</td></tr><tr><td>端口1</td><td>打开</td><td>掉线</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>端口2</td><td>打开</td><td>掉线</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>端口3</td><td>打开</td><td>掉线</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>端口4</td><td>打开</td><td>掉线</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>端口5</td><td>打开</td><td>在线</td><td>8327</td><td>0</td><td>8595</td><td>0</td></tr><tr><td>端口6</td><td>打开</td><td>掉线</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>端口7</td><td>打开</td><td>掉线</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>端口8</td><td>打开</td><td>掉线</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>端口9</td><td>打开</td><td>掉线</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

清空 

界面信息含义如下表所示。 

<table><tr><td>查询项</td><td>说明</td></tr><tr><td>端口</td><td>端口列表</td></tr><tr><td>状态</td><td>端口状态</td></tr><tr><td>连接状态</td><td>端口链路状态</td></tr><tr><td>发送正常报文统计</td><td>发送正确包数</td></tr><tr><td>发送错误报文统计</td><td>发送错误包数</td></tr><tr><td>接收正常报文统计</td><td>接收正确包数</td></tr><tr><td>接收错误报文统计</td><td>接收错误包数</td></tr></table>

# 7 工具

# 7.1 固件升级

系统版本固件的升级，点击升级后会进入升级模式，跳转升级页面后选择固件在线 升级 

操作步骤： 

1. 单击导航树中的“工具 $>$ 固件升级”菜单进入界面，如下图所示： 

固件升级 

进入固件升级模式 

升级 

![](images/2b088b65eec5a42cd8976508cf9eb063460a1e5339a1381d6809c406b466aaa3.jpg)


![](images/98509ba6beab7f3204a7241fa93ae263cc21b3aaf1c1808acf3e77bf133b427a.jpg)


![](images/bd99bf1a6d1a139bed473c6d84ec2e7305634c4b9585878721574c141f3b024d.jpg)


注意：点击确定以后，升级过程中请勿断电，停留在升级页面等待约 1 分钟升级完成 

# 7.2 配置备份

系统配置文件的升级和备份 

操作步骤： 

1. 单击导航树中的“工具 $>$ 配置备份”菜单进入界面，如下图所示： 

![](images/41711a81f198b3ac1ca083ea61b4c5321878f25f46cd4dd39f55df088897e06f.jpg)


界面信息含义如下表所示。 

<table><tr><td>配置项</td><td>说明</td></tr><tr><td>备份</td><td>备份配置文件</td></tr><tr><td>恢复</td><td>上传配置文件</td></tr></table>


注：上传配置后需重启生效 


# 7.3 恢复出厂

系统将恢复出厂配置 

操作步骤： 

1. 单击导航树中的“工具 $>$ 恢复出厂”菜单进入界面，如下图所示： 

![](images/bc1c481232988f84c378b06acc1bb86b0d4a88337ac0b0920a073d1222801041.jpg)


# 7.4 保存

保存配置 

操作步骤： 

1. 单击导航树中的“工具 $>$ 保存”菜单进入界面，如下图所示： 

![](images/2ea86394f1c11d12914ab8f656a5ad9575babc1514b1aab9a952a9435af17183.jpg)


# 7.5 重启系统

操作步骤： 

1. 单击导航树中的“工具 $>$ 重启”菜单进入界面，如下图所示： 

![](images/78ed40a493def2cfc63e9f698c1c81844c25c176ddfb89a0c59746d6b7bac119.jpg)


# 7.6 登出

操作步骤： 

1、单击导航树中的“工具 $>$ 登出”菜单，退出配置界面 

![](images/9951833509c5ec63a009db1f3105e099040c6e9f074d4e92ca01b40695b635b5.jpg)
