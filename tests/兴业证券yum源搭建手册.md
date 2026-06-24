# 兴业证券

# yum 源搭建与补丁更新手册

![](images/f9d23ecc48f0357879adc7563f2cd00c5da484fee8c4ee17c560c0de658834a9.jpg)


redhat. 


文档版本信息


<table><tr><td>版本</td><td>作者</td><td>时间</td><td>备注</td></tr><tr><td>1.0</td><td>邬灏</td><td>2019-12-18</td><td>创建文档</td></tr><tr><td>1.1</td><td>邬灏</td><td>2020-01-10</td><td>修改文档</td></tr></table>

# 目 录

兴业证券.. 

yum源搭建与补丁更新手册. 

一、 环境简介.. .3 

二、 离线 CDN 文件导出.. . 3 

三、 建立 repo 文件.. 2 

# 一、环境简介

目前，兴业证券搭建了一套satellite服务器，与红帽官网连通，主要用于红帽仓 库源下载。另在测试环境中搭建了 yum 源服务器。 

由于网络原因暂时从无法 CDN 完整下载 repository，暂时使用离线 iso 建立 yum 源。 后期等待下载完毕后iu，将satellite中的仓库导出到测试环境yum服务器中。并在 yum 服务器中搭建 apache，为当前环境提供 yum 源。 

# 二、离线CDN文件导出

将 satellite server 上的 content 拷贝到 yum 服务器 

```shell
# scp -r /var/lib/pulp/sat-content/content/dist/rlel/server/6/6Server/x86_64/os  
root@192.25.97.30:/home/apache/html/rlel6_new/  
# scp -r /var/lib/pulp/sat-content/content/dist/rlel/server/6/6Server/x86_64/extras  
root@192.25.97.30:/home/apache/html/rlel6_new/  
# scp -r /var/lib/pulp/sat-content/content/dist/rlel/server/7/7Server/x86_64/os  
root@192.25.97.30:/home/apache/html/rlel7_new/  
# scp -r /var/lib/pulp/sat-content/content/dist/rlel/server/6/6Server/x86_64/extras  
root@192.25.97.30:/home/apache/html/rlel7_new/ 
```

# 三、建立 repo 文件

在/home/apache/html/repo 目录下建立新的 repo 文件。RHEL6 系统的 repo 文件名为 rhel6.repo，RHEL7 系统的 repo 文件名为 rhel7.repo。 

```ini
# cat /home/apache/html/repo/rhel6(repo
[os]
name=RHEL6-OS
baseurl http://192.25.97.30:9090/rhel6_new/os/
gpgcheck=0
enabled=1
[extras]
name=RHEL6-EXTRAS
baseurl http://192.25.97.30:9090/rhel6_new/extras/os
gpgcheck=0
enabled=1
# cat /home/apache/html/repo/rhel7(repo
[os]
name=RHEL7-OS
baseurl http://192.25.97.30:9090/rhel7_new/os/
gpgcheck=0
enabled=1 
```

[extras]   
name $\equiv$ RHEL7-EXTRAS   
baseurl $\coloneqq$ http://192.25.97.30:9090/rhel7_new/extras/os/   
gpgcheck $= 0$ enabled $= 1$ 

repo文件修改完成后，在客户端机器上测试： 

wget -P /etc/yum.repos.d/ http://192.25.97.30:9090/repo/rhel7.repo -r -np -nH --cutdirs 3 

yum clean all 删除缓冲， 

yum repolist 刷新源 

安装源的更新需要注意一下几点 

1) 确保所有 rpm 来源于红帽官网，或者红帽原厂工程师， 

2) 确保 rpm 适用于那个操作系统版本，6 和 7 的 rpm 不能混用，提前向 redhat 工程 师确认后使用 

3) 避免使用 rpm 命令直接安装， 使用 yum 命令可以解决依赖，完整性，并对版本 来源进行集中管控 