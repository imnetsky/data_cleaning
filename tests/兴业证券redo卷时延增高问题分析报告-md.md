# 

### 兴业证券数据库应用 redo 卷时延增高问题分析报告

<html><body><table><tr><td>Product Type/Serial Number</td><td>Microcode Revision</td><td>Case Number</td></tr><tr><td>VSP F5100/31031&31029</td><td>90-09-22-00/00</td><td>05047439</td></tr></table></body></html>

# 

### 目录

1 问题概述 . 3  
2 问题分析 .. 6  
2.1 存储 Dump 日志分析 6  
2.1.1 应用对应的 MDKC 存储日志分析 6  
2.1.2 应用对应的 RDKC 存储日志分析 . 9  
2.2 性能数据分析 16  
2.2.1 存储资源利用率分析 . 16  
2.2.2 Redo 日志卷性能分析 . 17  
2.2.3 关于存储读写响应时间 20

3 结论和建议. 

# 

### 1 问题概述

从 2025/3/10 开始，有两套数据库应用（UF20-DB01BHP 和 ZYO32_DB01JQ）所使用的redo 日志卷陆续出现时延增高的现象，统计到的事件如下（以ZYO32_DB01JQ 为例）：

<html><body><table><tr><td>***2025-03-10 10:08:00.374</td><td></td></tr><tr><td>Warning: log write elapsed time 30839ms, size 7KB ***2025-03-1010:08:24.394</td><td rowspan="3"></td></tr><tr><td>*** 2025-03-10 10:19:05.334</td></tr><tr><td>Warning: log write elapsed time 30125ms, size 1KB ***2025-03-10 10:19:29.342</td></tr><tr><td>***2025-03-10 13:02:20.342</td><td rowspan="3"></td></tr><tr><td>Warning: log write elapsed time 30420ms, size 1KB ***2025-03-10 13:03:35.341</td></tr><tr><td></td></tr><tr><td>*** 2025-03-10 13:09:10.534</td><td rowspan="3"></td></tr><tr><td>Warning: log write elapsed time 30370ms, size 0KB *** 2025-03-10 13:09:16.543</td></tr><tr><td>*** 2025-03-10 13:50:49.334 Warning: log write elapsed time 30155ms, size 2KB</td></tr></table></body></html>

Warning: log write elapsed time 11178ms, size 2KB NSS2 is not running anymore.   
\*\*\* 2025-03-10 14:55:53.264   
Warning: log write elapsed time 11115ms, size 4KB \*\*\* 2025-03-10 14:55:56.284   
\*\*\* 2025-03-11 09:41:35.222   
Warning: log write elapsed time 11021ms, size 2KB \*\*\* 2025-03-11 09:42:32.234   
\*\*\* 2025-03-11 09:50:22.335   
Warning: log write elapsed time 30971ms, size 6KB \*\*\* 2025-03-11 09:50:28.340   
\*\*\* 2025-03-11 10:06:32.714   
Warning: log write elapsed time 11037ms, size 1KB \*\*\* 2025-03-11 10:06:59.721   
\*\*\* 2025-03-11 10:32:39.325   
Warning: log write elapsed time 11227ms, size 8KB \*\*\* 2025-03-11 10:33:21.331   
\*\*\* 2025-03-11 13:14:10.358   
Warning: log write elapsed time 30656ms, size 1KB \*\*\* 2025-03-11 13:14:19.361   
\*\*\* 2025-03-11 13:55:35.638   
Warning: log write elapsed time 30959ms, size 1KB \*\*\* 2025-03-11 13:56:08.641   
\*\*\* 2025-03-11 19:55:31.390   
Warning: log write elapsed time 11359ms, size 1KB \*\*\* 2025-03-11 19:56:10.392   
\*\*\* 2025-03-12 09:40:35.638   
Warning: log write elapsed time 30239ms, size 1KB \*\*\* 2025-03-12 09:44:38.642   
\*\*\* 2025-03-12 10:34:49.422   
Warning: log write elapsed time 11062ms, size 5KB   
\*\*\* 2025-03-12 10:40:04.431   
\*\*\* 2025-03-12 11:13:31.351   
Warning: log write elapsed time 30087ms, size 3KB   
\*\*\* 2025-03-12 11:13:49.368

这两套应用分别连接到位于福州滨海数据中心和上海金桥数据中心的日立 GAD 双活存储，涉及的这4 台存储配置情况如下表。

<html><body><table><tr><td></td><td>bh71</td><td>bh72</td><td>jq71</td><td>jq72</td></tr><tr><td>SN</td><td>31031</td><td>31251</td><td>31029</td><td>31028</td></tr><tr><td>安装位置</td><td>福州滨海</td><td>福州滨海</td><td>上海金桥</td><td>上海金桥</td></tr><tr><td>磁盘</td><td>50*7.6TB NVMe 6D+2P</td><td>50*7.6TB NVMe 6D+2P</td><td>50*7.6TB NVMe 6D+2P</td><td>50*7.6TB NVMe 6D+2P</td></tr><tr><td>可用容量 (TB)</td><td>247.58</td><td>247.58</td><td>247.58</td><td>247.58</td></tr><tr><td>Cache</td><td>1TB</td><td>1TB</td><td>1TB</td><td>1TB</td></tr><tr><td>CHB</td><td>4对</td><td>4对</td><td>4对</td><td>4对</td></tr><tr><td>前端口</td><td>24*32Gbps</td><td>24*32Gbps</td><td>24*32Gbps</td><td>24*32Gbps</td></tr><tr><td>Firmware</td><td>90-09-22-00/00</td><td>90-09-22-00/00</td><td>90-09-22-00/00</td><td>90-09-22-00/00</td></tr><tr><td>SVOS</td><td>9.9</td><td>9.9</td><td>9.9</td><td>9.9</td></tr><tr><td>备注</td><td>GAD Primary</td><td>GAD Secondary</td><td>GAD Primary</td><td>GAD Secondary</td></tr></table></body></html>

应用和存储的连接拓扑示意图如下：

![](images/c53b69ad857f131b90bc741db9d582c3a65fe16e54af36a01763a10819f3316e.jpg)

应用使用的日志卷为：

UF20-DB01BHP：03:22，使用的存储端口为：3C/4DZYO32_DB01JQ：40:6B，使用的存储端口为：3A/4B

# 

### 2 问题分析

2.1 存储 Dump 日志分析

2.1.1 应用对应的 MDKC 存储日志分析

从 MDKC 存储（31029）底层日志可以看到 ZYO32_DB01JQP 应用对应的 4B 端口在部分时段出现了I/O 传输延迟的现象，出现延迟的卷正是这套应用所使用的Redo 日志道卷，大部分为写 I/O（SCSI CMD $\vDash$ 2A:write）方向，根据出现的 SSB 特征码 D034/D031，I/O 传输延迟的原因为“ 等待数据传输”，问题指向存储外部链路端，其构成组件包括

1)FC-HBA(WWN $\mathbf { \bar { \rho } } = \mathbf { \rho }$ 100000620B3AC203)、2)FC-HBA 到交换机的光纤线、3)FC-HBA 在交换机上的SFP 模块、4)存储4B 端口上的SFP 模块、5)存储 4B 到交换机的光纤线、6) 存储4B 端口在交换机上的SFP 模块：

<html><body><table><tr><td>2025/03/11 10:32:42 2025/03/11 10:32:42</td><td>BECO# B358#</td><td>3C 4B 4B</td><td></td><td></td><td>xlmain It FCP Frame ceives from nOn-LOGIN HOST. qlsnhlliocb IL IocB was issued</td></tr><tr><td>2025/03/11 10:32:42</td><td>B3FE</td><td>3F 3F</td><td>4B</td><td></td><td>Information enhancement for transfer TOv</td></tr><tr><td>2025/03/11</td><td></td><td></td><td></td><td></td><td>snptovssb</td></tr><tr><td>10:32:42</td><td>B6AD#</td><td>3E</td><td>4B</td><td></td><td>tpcc xlfhostssb Information enhancement for transfer Tov/count error (Host information: Port ID, WnN)</td></tr><tr><td>2025/03/11 10:32:42</td><td>B6A9#3E D034#</td><td></td><td>4B 4B</td><td>04:6B</td><td>: snptov Complementing information log for transfer Tov (LM)</td></tr><tr><td>2025/03/11 10:32:42</td><td></td><td>3E</td><td></td><td></td><td>Ecmxrwtov Sync command Read/Write JoB Tov</td></tr><tr><td>2025/03/11 10:32:42</td><td>D031#</td><td>3F</td><td>4B</td><td>04 : 6B</td><td>fcmxssbtv Additional information SSB=d030/d034 (OPEN command, SCsI xeset/Tov)</td></tr><tr><td>2025/03/11 10:32:42</td><td>DDA1#</td><td>3E</td><td>4B</td><td></td><td>cktov_lm Data transfer (Tachyon) completion Tov</td></tr><tr><td>2025/03/11 10:32:42</td><td>DDA1#</td><td>3E</td><td>4B</td><td>04:6B</td><td>cktov_lm Data txansfex (Tachyon) completion Tov</td></tr><tr><td>2025/03/11 10:32:42</td><td>FEEB#</td><td></td><td>4B</td><td>LOGO</td><td>LINK ELS EvENT TYPe = LOGO</td></tr><tr><td>2025/03/11 10:32:33</td><td>D555#</td><td>3E</td><td>4B</td><td>04:6B</td><td>fcmxdsss Infoxmation enhancement log was output because job runing time of more than 1 sec vas detected</td></tr><tr><td>2025/03/1109:11:28</td><td>10E5</td><td>07</td><td></td><td></td><td>timdiv Async processing was performed forcibly</td></tr><tr><td>2025/03/11 08:54:30</td><td>10E5</td><td>E</td><td></td><td></td><td>timdiv Async processing was performed forcibly</td></tr><tr><td>2025/03/11 07:11:36</td><td>10E5</td><td>10</td><td></td><td></td><td>timdiv Async processing was performed foreibly</td></tr><tr><td>2025/03/11 07:00:43</td><td>10E5</td><td>0</td><td></td><td></td><td>: timdiv Async processing was performed forcibly</td></tr></table></body></html>

<html><body><table><tr><td colspan="11">Refcode = D034 : fcmxrwtov Sync command Read/Write JOB TOV</td></tr><tr><td>DATE TIME</td><td>PORT</td><td>LDEV#</td><td>CMD</td><td>KEY/ASC</td><td>HG-NAME</td><td>WAIT REASON</td><td></td><td>HOST WWN /IQN</td><td>FCID</td></tr><tr><td>2025/03/11 19:55:32</td><td>4B</td><td>00:04:6B</td><td>2A</td><td>B/C001</td><td></td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td><td>490000</td></tr><tr><td>2025/03/11 10:32:42</td><td>4B</td><td>00:04:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td></td><td>100000620B3AC203</td><td>490000</td></tr><tr><td>2025/02/13 23:11:12</td><td>4B</td><td>00:04:6C</td><td>8A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td></td><td>Wait for Data Transfer</td><td>100000620B3AC203</td><td>490000</td></tr><tr><td>2025/02/13 23:01:26</td><td>4B</td><td>00:04:6C</td><td>8A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td></td><td>Wait for Data Transfer</td><td>100000620B3AC203</td><td>490000</td></tr><tr><td>2025/02/13 09:59:30</td><td>4B</td><td>00:04:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td></td><td>100000620B3AC203</td><td>490000</td></tr><tr><td>2025/02/13 09:53:15</td><td>4B</td><td>00:04:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td></td><td>Wait for Data Transfer</td><td>100000620B3AC203</td><td>490000</td></tr><tr><td>2025/02/13 09:49:28</td><td>4B</td><td>00:04:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td></td><td>Wait for Data Transfer</td><td>100000620B3AC203</td><td>490000</td></tr><tr><td>2025/02/12 10:10:25</td><td>4B</td><td>00:04:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td></td><td>100000620B3AC203</td><td>490000</td></tr></table></body></html>







### 2 问题分析

2.1 存储 Dump 日志分析

2.1.1 应用对应的 MDKC 存储日志分析

根据存储端4B 端口的错误计数器，没有发现用于判断4B 端口SFP 模块和4B 端口到交换机的连线的计数器有异常增长情况，因此可以排除 4B 端口SFP 模块和4B 端口到交换机的连线问题：

CRC: 如果该计数器不为0，基本上为存储端口SFP 模块问题；EOFa: 如果该计数器不为0，基本上为存储端口到交换机之间的连线问题

<html><body><table><tr><td>PORT LABEL = 4B</td></tr><tr><td>16G FC Port Statistics</td></tr><tr><td>I Hex_Count I Decimal_Count I Port_Stats_Description</td></tr><tr><td colspan="3"></td></tr><tr><td></td><td></td></tr><tr><td>00000000 0 |Link Failure /</td><td></td></tr><tr><td>00000000</td><td>0 lLoss of Sync /</td></tr><tr><td>00000000 0 ILoss</td><td>of signal</td></tr></table></body></html>

<html><body><table><tr><td>00000000</td><td>cid:)</td><td>0</td><td>IPrimitive Sequence Protocol Error</td></tr><tr><td></td><td></td><td>0</td><td>IInvalid Transmission Word</td></tr><tr><td></td><td>00000000 |</td><td>0</td><td></td></tr><tr><td></td><td>100000000 |</td><td>0</td><td>IInvalid CRC ILIP Occurred</td></tr><tr><td></td><td>100000000 c:)</td><td>0</td><td>ILink UP</td></tr><tr><td></td><td>一00000000 cid:) 100000000</td><td>0</td><td>ILink Down_LoopInitializeTimeout</td></tr><tr><td></td><td>100000000 c:)</td><td>0</td><td>|Loss of Signal</td></tr><tr><td></td><td>00000000 c:</td><td>0</td><td>ILoss of Received Clock</td></tr><tr><td></td><td>00000000 —</td><td>0</td><td>INOs_OLs >200ms continuously Received</td></tr><tr><td></td><td>00000000</td><td>0</td><td>|Link Reset Received</td></tr><tr><td>100000000</td><td></td><td>0</td><td>|LIP F7 Received</td></tr><tr><td>100000000</td><td>—</td><td>0</td><td>|LIP F8 Received</td></tr><tr><td>100000000</td><td></td><td>0</td><td>IConnected P2P Mode</td></tr><tr><td>100000000</td><td>—</td><td>0</td><td>IPort Configuration Changed</td></tr><tr><td>100000000</td><td></td><td>0</td><td></td></tr><tr><td>100000000</td><td>|</td><td>0</td><td>|L-Bit Detected</td></tr><tr><td>100000000</td><td></td><td>0</td><td>IConnection Fabric P2P</td></tr><tr><td>100000000</td><td></td><td>0</td><td>IConnection Fabric Loop</td></tr><tr><td>100000000</td><td>|</td><td>0</td><td>IConnection Private Loop</td></tr><tr><td>100000000</td><td></td><td>0</td><td>IConnection P2P INos or OLs for >20o mSec (or user defined value) in the</td></tr><tr><td colspan="4">init f/w control block</td></tr><tr><td></td><td>100000000 (cid:)</td><td>0</td><td>IP2P Link Event Timeout</td></tr><tr><td></td><td>100000000 |</td><td>0</td><td>ILoop Initialize Protocol Error</td></tr><tr><td></td><td>100000000 |</td><td>0</td><td>ILR Initiated by l6G_CHA Protocol CHIP</td></tr><tr><td></td><td>100000000 |</td><td>0</td><td>ILRR Received by 16G_CHA Protocol CHIP</td></tr><tr><td></td><td>100000000</td><td>0</td><td>ILIP generated by IsP due to tout when attempt to transmit</td></tr><tr><td colspan="4">non-data frame</td></tr><tr><td></td><td>100000000 |</td><td>0 |Response Queue Full</td><td></td></tr><tr><td></td><td>100000000 |</td><td>0 |ATIO Queue Full</td><td></td></tr><tr><td></td><td>一00000000 |</td><td>0</td><td>IDrop AE due to lack of resources</td></tr><tr><td></td><td>100000000 cid:)</td><td>0</td><td>IELS Protocol Error Detected by Firmware</td></tr><tr><td>/</td><td>00000000</td><td>0</td><td>IOPEN Device Failed</td></tr><tr><td></td><td>ID0B5C113</td><td>3501572371</td><td>ITransmit Frame Count from 16G_CHA Protocol CHIP</td></tr><tr><td></td><td>630B2376</td><td>1661674358</td><td>IReceived Frame Count From l6G_ CHA Protocol CHIP</td></tr><tr><td></td><td>00000000</td><td>0</td><td>IDiscarded Frame Count From 16G_CHA Protocol CHIP</td></tr><tr><td></td><td>100000001 |</td><td>1</td><td>|Frame Dropped by Firmware</td></tr><tr><td></td><td>1 00000000 |</td><td>0</td><td>|LIP Primitives Received</td></tr><tr><td></td><td>100000000 —</td><td>0</td><td>INOs Primitive Received</td></tr><tr><td></td><td>100000000</td><td>0</td><td>IOLs Primitive Received</td></tr><tr><td></td><td>100000000 cd:)</td><td>0 INot Used</td><td></td></tr><tr><td></td><td>00000000</td><td>0</td><td>INot Used</td></tr></table></body></html>

<html><body><table><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>00000000 一</td><td>0</td><td>IClass2 Sequence Timeout</td><td></td></tr><tr><td></td><td>00000000 |</td><td></td><td>0</td><td>IP_RJT Frame Tramsmit</td></tr><tr><td></td><td>00000000</td><td></td><td>0</td><td>IFailure to allocate exchange resource when receiving a</td></tr><tr><td></td><td>frame for a</td><td>new exchange</td><td></td><td></td></tr><tr><td></td><td>00002630</td><td></td><td>9776</td><td>|ABTs Received</td></tr><tr><td></td><td>00000001</td><td>一</td><td>1</td><td>IReceived sequences with a missing frame</td></tr><tr><td></td><td>00000000</td><td></td><td>0</td><td>ICorrectable Error</td></tr><tr><td></td><td>0109FD7E</td><td></td><td>17431934</td><td>IMailbox Commands Issued</td></tr><tr><td></td><td>00000000</td><td></td><td>0</td><td>I Failure to allocate NportHandle when receiving an ELs frame</td></tr><tr><td></td><td>00000000</td><td>|</td><td>0</td><td>IReceived EOFa</td></tr></table></body></html>

### 



### 2 问题分析

2.1 存储 Dump 日志分析

2.1.1 应用对应的 MDKC 存储日志分析

写I/O 过程及错误特征码（示意）：

WRITE

![](images/1d00f1a8ef371b6d339b18ec2d5e12873593d18e28bd8f3f900d63c4f20a2261.jpg)

On a WRITE CMD Sequence, such as shown above, depending on which FRAME gets lost of damaged, will cause different SsB to be logged and cause a different level of Response Impact to the Host.   
Thus understanding the SsB that are logged and how they correspond with the above errors can help focusing on where to look for errors in a Fabric and/or Internally in a DKC.   
KEY SSB for WRITE IO related LINK issues : B65C, DDA1, B6FE, D034   
There is some Notes below on when some of above LOG relative to the timing of the "Xo to X4" errors above.   
The "Round-Trip Gaps 1 &2" shown above depend entirely on the DISTANCE between the HBA/INI and Target PORTS. Rule of thumb is "1ms'" per "100KM" per Round-Trip. This holds wel pretty well if the LINKS are purely DARK-FIBRE LINKS. If there is FCIP in a WAN things can change dramatically to the worse.

# 

### 2.1.2 应用对应的 RDKC 存储日志分析

从 RDKC 存储（31028）底层日志也可以看到 ZYO32_DB01JQP 应用对应的 4B 端口在部

分时段出现了I/O 传输延迟的现象，读和写方向都有，

<html><body><table><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2025/03/11 10:24:49</td><td>1396</td><td>44</td><td></td><td>: The number of segments per CPK as an additional information of ssB:13F3 occurred (Waiting for free segment) (Inhibited for 1 hour/Mp</td></tr><tr><td>2025/03/11 10:24:49</td><td>13F3#</td><td>44</td><td></td><td>s_gfsgm At Hit/Miss, segment reservation timeout</td></tr><tr><td>2025/03/11 10:24:29</td><td>10F5</td><td>4B</td><td></td><td>: timdiv Async processing was performed forcibly</td></tr><tr><td>2025/03/1110:06:44</td><td>FEFB#</td><td></td><td>PIOGI</td><td>: LINK ELS EVENI TyPe = PLOGI</td></tr><tr><td>2025/03/11 10:06:43</td><td>BECO#</td><td>3E</td><td></td><td>: xlmain It FCP Frame-receives from non-LOGIN HOsT.</td></tr><tr><td>2025/03/11 10:06:43</td><td>B358#</td><td>02</td><td></td><td>: qlsnhlliocb LL IocB was issued</td></tr><tr><td>2025/03/1110:06:43</td><td>B3FE</td><td>02</td><td></td><td>snptovssb Information enhancement for transfer Tov</td></tr><tr><td>2025/03/11 10:06:43</td><td>B6AD#</td><td>02</td><td></td><td>: tpcc_xlfhostssb Information enhancement for transfer Tov/count exxor (Host information: Port ID, Wi)</td></tr><tr><td>2025/03/11 10:06:43</td><td>B6A.9#</td><td>02</td><td></td><td>Complementing information log for transfer Tov (IM)</td></tr><tr><td>2025/03/11 10:06:43</td><td>D034#</td><td>02</td><td>40:6B</td><td>snptov fcmxzwtov Sync command Read/Write JoB Tov</td></tr><tr><td>2025/03/11 10:06:43</td><td>D031#</td><td>02</td><td>40:6B</td><td>fcmxssbtv Additional infoxmation of SsB=d030/d034 (OPEN command, SCSI reset/Tov)</td></tr><tr><td>2025/03/11 10:06:43</td><td>DDA1#</td><td>02</td><td></td><td>cktov_lm Data transfer (Tachyon) completion Tov</td></tr><tr><td>2025/03/11 10:06:43</td><td>DDA1#</td><td>02</td><td>4B 40:6B</td><td>cktov_lm Data transfer (Tachyon) completion Tov</td></tr><tr><td>2025/03/11 10:06:43</td><td>FEEB#</td><td></td><td>4B LOGO</td><td>: LINK ELS EVENT TYPe = LOGO</td></tr><tr><td>2025/03/11 10:06:34</td><td>D555#</td><td>02</td><td>40:6B</td><td>fcmxdssss Information enhancement log was output because job running time of more than l sec vas detected</td></tr><tr><td>2025/03/11 09:41:46</td><td></td><td></td><td>PLOGI</td><td></td></tr><tr><td>2025/03/11 09:41:45</td><td>FEFB# BECO#</td><td>3D</td><td></td><td>: LINK ELS EVENT TYPe = PLOGI : xlmain It FcP Frame-receives from non-LoGIN HosT.</td></tr><tr><td>2025/03/11 09:41:45</td><td>B358#</td><td></td><td></td><td>: qlsnhlliocb LL IocB was issued</td></tr><tr><td>2025/03/11 09:41:45</td><td>B3FE</td><td>C</td><td>4B</td><td>: snptovssb Information enhancement for transfer Tov</td></tr><tr><td></td><td></td><td></td><td>4B 4B</td><td></td></tr><tr><td>2025/03/11 09:41:45 2025/03/1109:41:45</td><td>B6AD#</td><td>0C B6A9# OC</td><td>4B</td><td>: tpcc_xlfhostssb Information enhancement for transfer Tov/count erxox (Host information: Port ID, WiN) Complementing information log for transfer Tov (IM)</td></tr></table></body></html>

<html><body><table><tr><td>Date</td><td>Time</td><td>SSB</td><td></td><td></td><td>MPPORTLDEV</td><td>Hitachi SSB Refcode Description</td></tr><tr><td>2025/03/1118:22:47</td><td></td><td>10E5</td><td>4E</td><td></td><td>:</td><td>timdiv Async processing was performed forcibly</td></tr><tr><td>2025/03/1117:07:36</td><td></td><td>10E5</td><td>4D</td><td></td><td>:</td><td>timdiv Async processing was performed forcibly</td></tr><tr><td>2025/03/11</td><td>16:50:24</td><td>12DD#</td><td>44</td><td></td><td>: c_rcvinv</td><td>When SCsI was reset, disabled message was received</td></tr><tr><td>2025/03/11</td><td>16:50:24</td><td>16BD</td><td>44</td><td></td><td>:</td><td>r_ssvlEbd Target of LtoL MsG clearance was detected</td></tr><tr><td>2025/03/1116:50:24</td><td></td><td>D031#</td><td>44</td><td>4B</td><td>40:62</td><td>fcmxssbtv Additional information of SSB-d030/d034 (OPEN cormand, SCsI reset/Tov)</td></tr><tr><td>2025/03/11 16:50:24</td><td></td><td>D030#</td><td>44</td><td>4B</td><td>40:62 : fcmxscrst</td><td>sCSI reset occurred (Information enhancement)</td></tr><tr><td>2025/03/1116:50:24</td><td></td><td>16AD#</td><td>44</td><td>4B</td><td>ssbl6al</td><td>Complementing information 2 of Erx-0xl699</td></tr><tr><td>2025/03/1116:50:24</td><td></td><td>16A1#</td><td>44</td><td>4B</td><td>- sr_jobclr</td><td>Complementing information of Err-0xl699</td></tr><tr><td>2025/03/1116:50:24</td><td></td><td>1699#</td><td>44</td><td>4B</td><td>sr_xstssb</td><td>sCSI reset processing execution (time etcof reset generating / Pson/Reboot / obstacle.) command, scsI reset/Tov)</td></tr><tr><td>2025/03/11 16:41:32</td><td></td><td>D031#</td><td>OE</td><td>4B</td><td>40:63 : fcmxssbty</td><td>Additional information of sSB=d030/d034 (OPEN</td></tr><tr><td>2025/03/1116:41:32</td><td></td><td>D030#</td><td>OE</td><td>4B 40:63</td><td>: fcmscrst</td><td>SCSI reset occurred (Information enhancement)</td></tr><tr><td>2025/03/11 16:41:32</td><td></td><td>16AD#</td><td>OE</td><td>4B</td><td>- x_ssbl6al</td><td>Complementing information 2 of Err=0xl699</td></tr><tr><td>2025/03/1116:41:32</td><td></td><td>16A1</td><td>OE</td><td>4日</td><td>sr_jobclx</td><td>Complementing information of Err-Oxl699</td></tr><tr><td>2025/03/11</td><td>16:41:32</td><td>1699#</td><td>OE</td><td>4B</td><td>sr_rstssb</td><td>SCSI reset processing execution (time etcof reset generating / Dso/Reboot / obstacle.)</td></tr><tr><td>2025/03/11</td><td>16:39:53</td><td>12DD#</td><td></td><td></td><td>c_rcvinv</td><td>When SCSI was reset, disabled message was received</td></tr><tr><td>2025/03/1116:39:53</td><td></td><td>16BD</td><td>OA</td><td></td><td></td><td>x_ssvlebd Target of LtoL MsG clearance was detected</td></tr><tr><td>2025/03/1116:39:53</td><td></td><td>D031#</td><td>OA</td><td>4B 40:61</td><td>:</td><td>fcmxssbtv Additional information of SSB-d030/d034 (OPEN conmand, SCSI reset/TOv)</td></tr><tr><td>2025/03/11 16:39:53</td><td></td><td>D030#</td><td>OA</td><td>4B</td><td>40:61 : fcmxscrst</td><td>SCSI reset occurred (Information enhancement)</td></tr><tr><td>2025/03/11</td><td>16:39:53</td><td>16AD排</td><td></td><td>4日</td><td>- I_ssbl6al</td><td>Complementing information 2 of Erx=0xl699</td></tr><tr><td>2025/03/1116:39:53 2025/03/11 16:39:53</td><td></td><td>16A1排</td><td>OA</td><td>4B 4B</td><td>: sr_jobclr</td><td>Complementing information of Err=Oxl699</td></tr><tr><td>2025/03/1115:46:18</td><td></td><td>1699#</td><td>OA</td><td></td><td>sr_Istssb</td><td>SCSI reset processing execution (time etcof reset generating/ PSON/Reboot / obstacle.)</td></tr><tr><td></td><td></td><td>AFBO</td><td>3c</td><td></td><td></td><td>rcfbk_flg Config BK during Online completed</td></tr></table></body></html>

### 

### 2.1.2 应用对应的 RDKC 存储日志分析

写 I/O 延迟，原因为“等待数据传输”，指向存储外部链路，依然和同一块 FC-HBA

卡有关（WWN=100000620B3AC203）：  

<html><body><table><tr><td>DATE</td><td>TIME</td><td>PORT</td><td>LDEV#</td><td>CMD</td><td>KEY/ASC</td><td>HG-NAME</td><td>WAIT REASON</td><td>Host WWN</td></tr><tr><td>2025/03/20</td><td>22:53:36</td><td>4B</td><td>00:40:6C</td><td>8A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/20</td><td>09:55:16</td><td>4B</td><td>00:40:6D</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/20</td><td>09:51:53</td><td>4B</td><td>00:40:6D</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/20</td><td>09:36:02</td><td>4B</td><td>00:40:6D</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/18</td><td>22:53:28</td><td>4B</td><td>00:40:6C</td><td>8A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/12</td><td>10:35:00</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/11</td><td>10:06:43</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/11</td><td>09:41:45</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/10</td><td>14:56:07</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/10</td><td>14:42:27</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/03/10</td><td>14:03:16</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/02/13</td><td>10:47:46</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/02/13</td><td>10:18:25</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr></table></body></html>

<html><body><table><tr><td>2025/02/13</td><td>10:12:59</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/02/13</td><td>10:08:54</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/02/13</td><td>10:04:38</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr><tr><td>2025/02/13</td><td>09:53:47</td><td>4B</td><td>00:40:6B</td><td>2A</td><td>B/C001</td><td>ZYO32_DB01JQP</td><td>Wait for Data Transfer</td><td>100000620B3AC203</td></tr></table></body></html>

### 



### 2.1.2 应用对应的 RDKC 存储日志分析



读I/O 延迟，出现的频率更高一点，原因主要为“等待数据传输”，指向存储外部链路，依然和同一块 FC-HBA 卡有关（WWN=100000620B3AC203）：

<html><body><table><tr><td>DATE</td><td>TIME</td><td>PORT</td><td>RESET TYPE</td><td>WAIT REASON</td><td>Possible HG-NAME</td><td>Possible HBA-WWN</td></tr><tr><td>3/20/2025</td><td>22:58:43</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>22:56:06</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait due to Slot Busy</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>22:52:09</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>22:52:08</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>22:49:11</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>22:48:18</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>16:52:27</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for DMA Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>16:48:38</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>16:46:54</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>16:38:16</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>13:01:20</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/20/2025</td><td>9:54:10</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td></td><td></td></tr><tr><td>3/20/2025</td><td>0:52:19</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/19/2025</td><td>23:10:53</td><td>4B</td><td>ABTS(Abort Sequence)</td><td></td><td></td><td>100000620B3AC203</td></tr><tr><td>3/18/2025</td><td></td><td>4B</td><td></td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td></td><td>23:14:40 23:13:57</td><td></td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/18/2025 3/18/2025</td><td></td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/18/2025</td><td>23:13:32 22:59:51</td><td>4B 4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/18/2025</td><td></td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203 100000620B3AC203</td></tr><tr><td>3/18/2025</td><td>22:54:01</td><td>4B</td><td>ABTS(Abort Sequence) ABTS(Abort Sequence)</td><td>Wait for DMA Data Transfer Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td></td></tr><tr><td>3/18/2025</td><td>22:53:46</td><td>4B</td><td>ABTS(Abort Sequence)</td><td></td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/18/2025</td><td>19:38:28</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for DMA Data Transfer</td><td>ZYO32_DB01JQP ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/18/2025</td><td>19:32:06</td><td></td><td></td><td>Wait for Stage/Destage Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203 100000620B3AC203</td></tr><tr><td></td><td>19:29:43</td><td>4B</td><td>ABTS(Abort Sequence)</td><td></td><td></td><td>100000620B3AC203</td></tr><tr><td>3/18/2025</td><td>19:27:20</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for DMA Data Transfer</td><td>ZYO32_DB01JQP</td><td></td></tr><tr><td>3/18/2025</td><td>19:25:59</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203 100000620B3AC203</td></tr><tr><td>3/18/2025</td><td>19:23:10</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/18/2025</td><td>19:22:29</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td></td></tr><tr><td>3/18/2025</td><td>19:18:10 19:16:38</td><td>4B 4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203 100000620B3AC203</td></tr><tr><td>3/18/2025</td><td></td><td></td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td></td></tr><tr><td>3/18/2025</td><td>19:15:38</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr></table></body></html>

<html><body><table><tr><td>3/18/2025</td><td>16:53:15</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/18/2025</td><td>16:45:05</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/17/2025</td><td>20:05:15</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/13/2025</td><td>1:24:46</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/12/2025</td><td>20:30:07</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/12/2025</td><td>16:57:10</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/12/2025</td><td>16:43:21</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>23:45:34</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>23:13:58</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>23:00:34</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>22:58:43</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>22:51:26</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>19:53:33</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>19:50:55</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>19:46:28</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>19:45:45</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>19:37:34</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>16:50:24</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>16:41:32</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for DMA Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/11/2025</td><td>16:39:53</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>23:13:20</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>22:48:44</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>22:46:41</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:44:44</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:44:23</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:44:00</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for DMA Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:34:27</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for DMA Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:32:49</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:28:39</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:28:33</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait due to Slot Busy</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:26:05</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:25:06</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:24:58</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:23:49</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:20:55</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait due to Slot Busy</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:20:40</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>19:17:45</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>16:51:52</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>16:50:57</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr></table></body></html>

<html><body><table><tr><td>3/10/2025</td><td>16:49:43</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td></td><td></td><td></td><td></td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>3/10/2025</td><td>16:43:13</td><td>4B</td><td>ABTS(Abort Sequence)</td><td></td><td></td><td></td></tr><tr><td>2/13/2025</td><td>23:34:38</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:33:20</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203 100000620B3AC203</td></tr><tr><td>2/13/2025 2/13/2025</td><td>23:32:36</td><td>4B 4B</td><td>ABTS(Abort Sequence) ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td></td><td>23:29:28</td><td></td><td></td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:27:23</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td></td></tr><tr><td>2/13/2025</td><td>23:21:24</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:20:56</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:20:28</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:20:26</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:20:17</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait due to Slot Busy</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:18:06</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:15:15</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for DMA Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:12:34</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:11:16</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:08:35</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:08:29</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:08:03</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:03:54</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:03:14</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:02:43</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Stage/Destage</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>23:02:31</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/13/2025</td><td>11:19:49</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for DMA Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/12/2025</td><td>10:32:58</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/12/2025</td><td>0:07:03</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/12/2025</td><td>0:03:06</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr><tr><td>2/11/2025</td><td>23:54:35</td><td>4B</td><td>ABTS(Abort Sequence)</td><td>Wait for Data Transfer</td><td>ZYO32_DB01JQP</td><td>100000620B3AC203</td></tr></table></body></html>





### 2.1.2 应用对应的 RDKC 存储日志分析

读I/O 延迟，出现的频率更高一点，原因主要为“等待数据传输”，指向存储外部链路，依然和同一块 FC-HBA 卡有关（WWN=100000620B3AC203）：

类似地，存储上4B 端口错误计数器并未出现异常增长，可排除存储4B 端口SFP 模块及端口到交换机的链路问题：

<html><body><table><tr><td colspan="2">PORT LABEL = 4B</td></tr><tr><td>16G FC Port Statistics</td><td></td></tr><tr><td>I Hex_CountI Decimal_Count</td><td>Port_Stats_Description</td></tr><tr><td colspan="2"></td></tr><tr><td></td><td></td></tr><tr><td>00000000 00000000</td><td>0 ILink Failure /</td></tr></table></body></html>

<html><body><table><tr><td>00000000</td><td></td><td>0</td><td>lLoss of Signal</td><td></td></tr><tr><td></td><td>100000000</td><td>0</td><td></td><td>IPrimitive Sequence Protocol Error</td></tr><tr><td></td><td>100000000</td><td>0</td><td>IInvalid Transmission Word</td><td></td></tr><tr><td>/</td><td>00000000</td><td>0</td><td>|Invalid CRC</td><td></td></tr><tr><td></td><td>00000000 c:</td><td>0</td><td>|LIP Occurred</td><td></td></tr><tr><td></td><td>00000001 |</td><td>1</td><td>|Link UP</td><td></td></tr><tr><td></td><td>00000000 c:</td><td>0</td><td>ILink Down_LoopInitializeTimeout</td><td></td></tr><tr><td></td><td>00000001 |</td><td>1</td><td>lLoss of Signal</td><td></td></tr><tr><td></td><td>100000000 |</td><td>0</td><td>|Loss of Received Clock</td><td></td></tr><tr><td>100000000</td><td>—</td><td>0</td><td></td><td>INOs_OLs >200ms continuously Received</td></tr><tr><td>100000000</td><td>—</td><td>0</td><td>|Link Reset Received</td><td></td></tr><tr><td>100000000</td><td></td><td>0</td><td>|LIP F7 Received</td><td></td></tr><tr><td>100000000</td><td>|</td><td>0</td><td>|LIP F8 Received</td><td></td></tr><tr><td>100000001</td><td>—</td><td>1</td><td>IConnected P2P Mode</td><td></td></tr><tr><td></td><td>00000000 |</td><td>0</td><td>IPort Configuration Changed</td><td></td></tr><tr><td>一00000000</td><td>|</td><td>0</td><td>IL-Bit Detected</td><td></td></tr><tr><td>100000001</td><td></td><td>1</td><td>IConnection Fabric P2P</td><td></td></tr><tr><td></td><td>100000000 c:)</td><td>0</td><td>IConnection Fabric Loop</td><td></td></tr><tr><td></td><td>00000000 c:)</td><td>0</td><td>IConnection Private Loop</td><td></td></tr><tr><td></td><td>00000000 |</td><td>0</td><td>IConnection P2P</td><td></td></tr><tr><td>100000000</td><td>|</td><td>0</td><td></td><td>INos or OLs for >200 mSec (or user defined value) in the</td></tr><tr><td colspan="5">init f/w control block</td></tr><tr><td></td><td>100000000 |</td><td>0</td><td>IP2P Link Event Timeout</td><td></td></tr><tr><td></td><td>100000000</td><td>0</td><td>ILoop Initialize Protocol Error</td><td></td></tr><tr><td></td><td>一00000000 |</td><td>0</td><td>ILR Initiated by 16G_CHA Protocol CHIP</td><td></td></tr><tr><td></td><td>100000000 c:)</td><td>0</td><td></td><td>ILRR Received by l6G_CHA Protocol CHIP</td></tr><tr><td></td><td>100000000</td><td>0</td><td></td><td>ILIP generated by IsP due to tout when attempt to transmit</td></tr><tr><td></td><td>non-data frame</td><td></td><td></td><td></td></tr><tr><td></td><td>100000000</td><td>0</td><td>|Response Queue Full</td><td></td></tr><tr><td></td><td>100000000</td><td>0</td><td>|ATIO Queue Full</td><td></td></tr><tr><td></td><td>一00000000 cid:)</td><td>0</td><td>IDrop AE due to lack of resources</td><td></td></tr><tr><td></td><td>100000000</td><td>0</td><td></td><td>IELs Protocol Error Detected by Firmware</td></tr><tr><td></td><td>100000000</td><td>0</td><td>IOPEN Device Failed</td><td></td></tr><tr><td></td><td>04B96737</td><td>79259447</td><td></td><td>ITransmit Frame Count from 16G_CHA Protocol CHIP</td></tr><tr><td></td><td>DF924962</td><td>3750906210</td><td></td><td>IReceived Frame Count From l6G_CHA Protocol CHIP</td></tr><tr><td></td><td>00000000 |</td><td>0</td><td></td><td>IDiscarded Frame Count From l6G_CHA Protocol CHIP</td></tr><tr><td></td><td>100000000</td><td>0</td><td>|Frame Dropped by Firmware</td><td></td></tr><tr><td></td><td>100000000 |</td><td>0</td><td>ILIP Primitives Received</td><td></td></tr><tr><td></td><td>100000001 —</td><td>1</td><td>INOs Primitive Received</td><td></td></tr><tr><td></td><td>00000000</td><td>0</td><td>IOLs Primitive Received</td><td></td></tr><tr><td></td><td>00000000</td><td>0</td><td>INot Used</td><td></td></tr></table></body></html>

<html><body><table><tr><td></td></tr><tr><td>00000000</td><td>0 INot Used</td></tr><tr><td>00000000 0 IClass2 Sequence Timeout</td><td></td></tr><tr><td>00000000 0 IP_RJT Frame Tramsmit</td><td></td></tr><tr><td>00000000</td><td>| 0 IFailure to allocate exchange resource when receiving a</td></tr><tr><td>frame for a</td><td>new exchange</td></tr><tr><td>00002AED |</td><td>10989 |ABTs Received</td></tr><tr><td>00000000 |</td><td>0 |Received sequences with a missing frame</td></tr><tr><td>00000000</td><td>0 ICorrectable Error</td></tr><tr><td>010A5D00</td><td>17456384 |Mailbox Commands Issued</td></tr><tr><td>100000000 |</td><td>0 I Failure to allocate NportHandle when receiving an ELs frame</td></tr></table></body></html>

### 



### 2.1.2 应用对应的 RDKC 存储日志分析

读I/O 过程及错误特征码（示意）：

READ

![](images/4e99fb7e1ece6ebd42007db59e4163ea29106f02cadb274cef1e6c9fe7eee02c.jpg)

READ LINK errors are dificult to track inside a DUMP.If the CMD is received OK, then the TARGET PORT simply sends the DATA and STATUS, without any feedback and has to assume the Frames get delivered OK. Likewise if the CMD never gets to the DKC Port (error Xo ) then the DKC PORT sends nothing. Should an error happen at timing ( X1 ) the HBA/INI wil get to know about it and issue an ABTS immediately. If the error is at TIMING X0 or X2 then the HBA/INI wil TIMEOUT and issue an ABTS.

![](images/d7e6953fcb3200d9f1225cd4062153355393bca1bef80a6b7ed047507490ebac.jpg)

Depending on where the ERROR happened the DKC PORT will either LOG :

a) RESETD LOG (RESET Received) b) $\cdot$ / 16A1 / 16AD / 16AE (RESET Received) c) $\cdot$ (ABTS Reset sent after Timeout waiting for Response)

# 

# 

### 2.2 性能数据分析

2.2.1 存储资源利用率分析

存储全局共享资源CPU 和Cache 利用率均在合理范围内，未见异常，说明存储资源未出现瓶颈：

Processor busy "SN:31028(VSP 5100, 5500, 5100H, 5500H)"From $\because$ 2025/3/12 8:00:00 to 2025/3/12 11:00:00(sampling rate $\because$ 1min)100- MPU010-MP010(00)[Av.9.12, MPU120-MP120(CO)[Avg. 11.4,Max. 15] Max. 15]MPUO10-MP010(01)[Avg.9.32.Max.16] Max.19]MPUO1O-MP01O(02)[Avg.6.63, MPU120-MP120(02) [Avg. 10.69,Max.15] Max.18]MPU01O-MP01O(03) [Avg.8.65, MPU120-MP120(03)[Avg,10.66,Max.14] Max.18]80-MPUO10-MP010(05)[Avg.8.39.Max. 14] Max.16]MPUO10-MP010(06)[Avg.6.83, MPU120-MP120(C6)[Avg.10.58,Max.15] Max,18]MPU010-MP010(07)[Avg.8.86, MPU120-MP120(07)[Avg.10.61,Max. 15] Max. 17]MPU010-MP01Q(0s)[Avg.8.72, MPU120-MP120(C5)[Avg.10.35,60 MPUd10-MPo10(9) [Avg.8.73,Max,15] Max, 17]MPU120-MP120(OA)[Avg.7.77.Max,11] Max,13]MPUO10-MP01O(0B)[Avg. 7.15. MPU120-MP120(CB)[Avg.7.93,Max. 11] Max. 12]MPU120-MP120(CC) [Avg.7.98,40 Max., 12] Max. 13]MPU120-MP120(OD) [Avg.7.99,Max. 11] Max, 13]MPU010-MP01O(0E)[Avg.7.57. MPU120-MP120(CE)[Avg.7.97.Max.12] Max.13]MPUO1O-MP010(OF)[Avg.7.59, MPU120-MP120(CF)[Avg.7.93,Max.12] Max, 13]Max,12] Max.13]20-Max. 12] Max, 13]MAAMaMAN MPUO10-MP010(12)[Avg.7.49, Max. 12] Max. 13] MPU120-MP120(12)[Avg.8.21,6A02025/3/128:01:00 2025/3/128:51:00 2025/3/129:41:00 2025/3/1210:31:00Time [min]

![](images/e0348175abb35662f3553dbe0264b2b92448775a47722c1dcc30199bfbe22160.jpg)  
Cache Write Pending Rate $[ \% 1 0 \% ]$ "SN:31028(VSP5100,5500,5100H, 5500H)"

# 

# 

### 2.2 性能数据分析

2.2.2 Redo 日志卷性能分析

存储上显示 ZYO32_DB01JQP 应用所使用的 Redo 日志卷 40:6B 读写响应时间良好：写延迟在 $0 . 2 3 \mathrm { m s }$ 左右，读延迟在 $0 . 1 { \sim } 0 . 5 \mathrm { m s }$ 之间波动（波动和负载及链路有关），存储上观测到的性能压力较小，不存在性能问题：

![](images/d9a6999a53b89add38bbb90ec07f8bdd717bd127e682103a2ed112210056577b.jpg)

![](images/9c829735cf83acdc19f612fe7be5f004032ef9a242cd578426776dd7ffaf93ea.jpg)

# 

### 2.2 性能数据分析

2.2.3 关于存储读写响应时间

存储上的响应时间从数据帧被传输到存储端口开始计算，因此主机上看到的响应时间和存储端不会完全一致，如果存储上的响应时间处于正常范围内，而主机上的响应时间偏大，就可能是由于中间链路传输耗时所导致。

读I/O：延时可能出现在将目标数据传输至主机时所经过的链路

Read Sequence :

![](images/01df992d4048b09fdf8e33fd254822486ddb9411f6d36748ac619e146648e508.jpg)

写 I/O：延时可能出现在 XRDY 状态帧传输至主机时所经过的链路以及和主机确认写完成信号时所经过的链路

![](images/87491f3f4ea27d6e14cdf8b2c50d34a01205ace8cbf9b59362315e7c50fd0be3.jpg)







### 3 结论和建议

综上分析，Oracle 数据库应用的Redo 日志卷出现时延增加是由于存储外部问题，主要指向 FC-HBA 光纤卡（WWN=100000620B3AC203）到交换机这一侧的链路，建议重点排查这一段的链路及所有相关组件（FC-HBA、光纤线及 SFP 模块）尤其是 FC-HBA 卡，或者通过隔离法排除怀疑部件。

如果此类问题在隔离和排查后依然存在，建议如下：

1) 针对Redo 日志卷收集秒级性能数据（由于秒级收集的收集会产生性能开销，不建议持续收集，一般收集 10 分钟左右，可结合定时任务分段收集）；  
2) 根据上述分析，存储的响应时间受到所经过的传输链路影响，如果怀疑存储内部资源处理I/O 耗时过久导致应用延迟变高，可部署收集程序获取存储内部处理I/O 用时