
文档说明


<table><tr><td colspan="2">文档名称</td><td colspan="3">YUM源服务器资源需求</td></tr><tr><td colspan="2">内容描述</td><td colspan="3"></td></tr><tr><td colspan="5">修订历史</td></tr><tr><td>日期</td><td>版本</td><td>修订者</td><td>修订说明</td><td>评审人员</td></tr><tr><td>2022.05.24</td><td>0.1</td><td>郭灏</td><td>初稿，添加资源需求</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>

# 目 录

一、 资源需求.. 

二、 系统环境部署需求.. 

2.1 磁盘需求.. 

2.2 分区划分.. 3 

三、 防火墙开通需求.. 3 

# 一、资源需求

<table><tr><td>主机名</td><td>系统版本</td><td>CPU</td><td>内存</td><td>磁盘</td><td>功能</td></tr><tr><td>rhel7-sync</td><td>RHEL 7.9</td><td>2 or above</td><td>4G or above</td><td>380G</td><td>连接CDN同步RHEL 7 repository</td></tr><tr><td>rhel8-sync</td><td>RHEL 8.6</td><td>2 or above</td><td>4G or above</td><td>380G</td><td>连接CDN同步RHEL 8 repository</td></tr><tr><td>yum</td><td>RHEL 7.9/8.6</td><td>4 or above</td><td>8G or above</td><td>700G</td><td>YUM源服务器</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# 二、系统环境部署需求

# 2.1 磁盘需求

可以部署两块磁盘（一块磁盘也可以） 

<table><tr><td>磁盘</td><td>大小</td><td>VG</td><td>备注</td></tr><tr><td>磁盘1</td><td>80G</td><td>rootvg</td><td>尽量分配到SSD</td></tr><tr><td>磁盘2</td><td>300G/600G</td><td>datavg</td><td></td></tr></table>

# 2.2 分区划分

<table><tr><td>Mount Point</td><td>LV命名(建议)</td><td>最低配置</td><td>备注</td></tr><tr><td>/boot</td><td></td><td>2G</td><td>必须是分区</td></tr><tr><td>/</td><td>/dev/mapper/rootvg_rootlv</td><td>40G</td><td></td></tr><tr><td>/var</td><td>dev/mapper/rootvg_varlv</td><td>20G</td><td>用于存放vmcore</td></tr><tr><td>/home</td><td>dev/mapper/rootvg_homelv</td><td>10G</td><td>按需求配置</td></tr><tr><td>swap</td><td>dev/mapper/rootvg_swaplv</td><td>8G</td><td>按需求扩展</td></tr><tr><td>/data</td><td>dev/mapper/datavg_datalv</td><td>300G/600G</td><td>按需求配置(matavg)</td></tr></table>

# 三、

防火 

# 墙开通需求

<table><tr><td>端口</td><td>协议</td><td>源地址</td><td>目标地址</td></tr><tr><td>443</td><td>tcp</td><td>本机</td><td>access.redhat.com</td></tr><tr><td>443</td><td>tcp</td><td>本机</td><td>cdn.redhat.com</td></tr><tr><td>443</td><td>tcp</td><td>本机</td><td>subscription.rhsm.redhat.com</td></tr><tr><td>443</td><td>tcp</td><td>本机</td><td>china.cdn.redhat.com</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>