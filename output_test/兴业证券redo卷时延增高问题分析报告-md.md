#

### 兴业证券数据库应用 redo 卷时延增高问题分析报告

---
文档概要：报告分析了2025年3月10日起兴业证券两套数据库应用（UF20-DB01BHP和ZYO32_DB01JQ）的redo日志卷时延增高问题，涉及福州滨海和上海金桥的日立GAD双活存储，通过存储日志和性能数据分析定位原因。
本段概要：分析兴业证券数据库应用redo卷时延增高问题，涉及VSP F5100存储及微码版本。
逻辑关联：下一节：目录
---

<html><body>| Product Type/Serial Number | Microcode Revision | Case Number |
| VSP F5100/31031&31029 | 90-09-22-00/00 | 05047439 |</body></html>

### 目录

---
文档概要：报告分析了2025年3月10日起兴业证券两套数据库应用（UF20-DB01BHP和ZYO32_DB01JQ）的redo日志卷时延增高问题，涉及福州滨海和上海金桥的日立GAD双活存储，通过存储日志和性能数据分析定位原因。
本段概要：概述问题分析与性能数据，涵盖存储日志、资源利用率及Redo日志卷性能，最后给出结论。
逻辑关联：上一节：兴业证券数据库应用 redo 卷时延增高问题分析报告
下一节：1 问题概述
---

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

### 1 问题概述

---
文档概要：报告分析了2025年3月10日起兴业证券两套数据库应用（UF20-DB01BHP和ZYO32_DB01JQ）的redo日志卷时延增高问题，涉及福州滨海和上海金桥的日立GAD双活存储，通过存储日志和性能数据分析定位原因。
本段概要：描述两套数据库应用从2025/3/10起redo日志卷时延增高，包含多个写耗时警告事件。
逻辑关联：上一节：目录
下一节：2 问题分析；与“”存在因果关系：概述中的时延问题促使了对存储日志的针对性检查。
---

从 2025/3/10 开始，有两套数据库应用（UF20-DB01BHP 和 ZYO32_DB01JQ）所使用的redo 日志卷陆续出现时延增高的现象，统计到的事件如下（以ZYO32_DB01JQ 为例）：

<html><body>| ***2025-03-10 10:08:00.374 |  |
| Warning: log write elapsed time 30839ms, size 7KB ***2025-03-1010:08:24.394 |  |
| *** 2025-03-10 10:19:05.334 |
| Warning: log write elapsed time 30125ms, size 1KB ***2025-03-10 10:19:29.342 |
| ***2025-03-10 13:02:20.342 |  |
| Warning: log write elapsed time 30420ms, size 1KB ***2025-03-10 13:03:35.341 |
|  |
| *** 2025-03-10 13:09:10.534 |  |
| Warning: log write elapsed time 30370ms, size 0KB *** 2025-03-10 13:09:16.543 |
| *** 2025-03-10 13:50:49.334 Warning: log write elapsed time 30155ms, size 2KB |</body></html>

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

<html><body>|  | bh71 | bh72 | jq71 | jq72 |
| SN | 31031 | 31251 | 31029 | 31028 |
| 安装位置 | 福州滨海 | 福州滨海 | 上海金桥 | 上海金桥 |
| 磁盘 | 50*7.6TB NVMe 6D+2P | 50*7.6TB NVMe 6D+2P | 50*7.6TB NVMe 6D+2P | 50*7.6TB NVMe 6D+2P |
| 可用容量 (TB) | 247.58 | 247.58 | 247.58 | 247.58 |
| Cache | 1TB | 1TB | 1TB | 1TB |
| CHB | 4对 | 4对 | 4对 | 4对 |
| 前端口 | 24*32Gbps | 24*32Gbps | 24*32Gbps | 24*32Gbps |
| Firmware | 90-09-22-00/00 | 90-09-22-00/00 | 90-09-22-00/00 | 90-09-22-00/00 |
| SVOS | 9.9 | 9.9 | 9.9 | 9.9 |
| 备注 | GAD Primary | GAD Secondary | GAD Primary | GAD Secondary |</body></html>

应用和存储的连接拓扑示意图如下：

![](images/c53b69ad857f131b90bc741db9d582c3a65fe16e54af36a01763a10819f3316e.jpg)

应用使用的日志卷为：

UF20-DB01BHP:03:22，使用的存储端口为：3C/4DZYO32_DB01JQ:40:6B，使用的存储端口为：3A/4B

### 2 问题分析

---
文档概要：报告分析了2025年3月10日起兴业证券两套数据库应用（UF20-DB01BHP和ZYO32_DB01JQ）的redo日志卷时延增高问题，涉及福州滨海和上海金桥的日立GAD双活存储，通过存储日志和性能数据分析定位原因。
本段概要：通过MDKC存储日志分析，发现I/O传输延迟问题，原因为“等待数据传输”，指向存储外部链路端组件。
逻辑关联：上一节：1 问题概述
下一节：2.1.2 应用对应的 RDKC 存储日志分析；与“”存在从属/组成部分关系：该章节是问题分析的一个具体分析维度，属于“”的子集。
---

2.1 存储 Dump 日志分析

2.1.1 应用对应的 MDKC 存储日志分析

从 MDKC 存储（31029）底层日志可以看到 ZYO32_DB01JQP 应用对应的 4B 端口在部分时段出现了I/O 传输延迟的现象，出现延迟的卷正是这套应用所使用的Redo 日志道卷，大部分为写 I/O(SCSI CMD $\vDash$ 2A:write）方向，根据出现的 SSB 特征码 D034/D031,I/O 传输延迟的原因为“ 等待数据传输”，问题指向存储外部链路端，其构成组件包括

1)FC-HBA(WWN $\mathbf { \bar { \rho } } = \mathbf { \rho }$ 100000620B3AC203)、2)FC-HBA 到交换机的光纤线、3)FC-HBA 在交换机上的SFP 模块、4)存储4B 端口上的SFP 模块、5)存储 4B 到交换机的光纤线、6) 存储4B 端口在交换机上的SFP 模块：

<html><body>| 2025/03/11 10:32:42 2025/03/11 10:32:42 | BECO# B358# | 3C 4B 4B |  |  | xlmain It FCP Frame ceives from nOn-LOGIN HOST. qlsnhlliocb IL IocB was issued |
| 2025/03/11 10:32:42 | B3FE | 3F 3F | 4B |  | Information enhancement for transfer TOv |
| 2025/03/11 |  |  |  |  | snptovssb |
| 10:32:42 | B6AD# | 3E | 4B |  | tpcc xlfhostssb Information enhancement for transfer Tov/count error (Host information: Port ID, WnN) |
| 2025/03/11 10:32:42 | B6A9#3E D034# |  | 4B 4B | 04:6B | : snptov Complementing information log for transfer Tov (LM) |
| 2025/03/11 10:32:42 |  | 3E |  |  | Ecmxrwtov Sync command Read/Write JoB Tov |
| 2025/03/11 10:32:42 | D031# | 3F | 4B | 04 : 6B | fcmxssbtv Additional information SSB=d030/d034 (OPEN command, SCsI xeset/Tov) |
| 2025/03/11 10:32:42 | DDA1# | 3E | 4B |  | cktov_lm Data transfer (Tachyon) completion Tov |
| 2025/03/11 10:32:42 | DDA1# | 3E | 4B | 04:6B | cktov_lm Data txansfex (Tachyon) completion Tov |
| 2025/03/11 10:32:42 | FEEB# |  | 4B | LOGO | LINK ELS EvENT TYPe = LOGO |
| 2025/03/11 10:32:33 | D555# | 3E | 4B | 04:6B | fcmxdsss Infoxmation enhancement log was output because job runing time of more than 1 sec vas detected |
| 2025/03/1109:11:28 | 10E5 | 07 |  |  | timdiv Async processing was performed forcibly |
| 2025/03/11 08:54:30 | 10E5 | E |  |  | timdiv Async processing was performed forcibly |
| 2025/03/11 07:11:36 | 10E5 | 10 |  |  | timdiv Async processing was performed foreibly |
| 2025/03/11 07:00:43 | 10E5 | 0 |  |  | : timdiv Async processing was performed forcibly |</body></html>

<html><body>| Refcode = D034 : fcmxrwtov Sync command Read/Write JOB TOV |
| DATE TIME | PORT | LDEV# | CMD | KEY/ASC | HG-NAME | WAIT REASON |  | HOST WWN /IQN | FCID |
| 2025/03/11 19:55:32 | 4B | 00:04:6B | 2A | B/C001 |  | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 | 490000 |
| 2025/03/11 10:32:42 | 4B | 00:04:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer |  | 100000620B3AC203 | 490000 |
| 2025/02/13 23:11:12 | 4B | 00:04:6C | 8A | B/C001 | ZYO32_DB01JQP |  | Wait for Data Transfer | 100000620B3AC203 | 490000 |
| 2025/02/13 23:01:26 | 4B | 00:04:6C | 8A | B/C001 | ZYO32_DB01JQP |  | Wait for Data Transfer | 100000620B3AC203 | 490000 |
| 2025/02/13 09:59:30 | 4B | 00:04:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer |  | 100000620B3AC203 | 490000 |
| 2025/02/13 09:53:15 | 4B | 00:04:6B | 2A | B/C001 | ZYO32_DB01JQP |  | Wait for Data Transfer | 100000620B3AC203 | 490000 |
| 2025/02/13 09:49:28 | 4B | 00:04:6B | 2A | B/C001 | ZYO32_DB01JQP |  | Wait for Data Transfer | 100000620B3AC203 | 490000 |
| 2025/02/12 10:10:25 | 4B | 00:04:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer |  | 100000620B3AC203 | 490000 |</body></html>

根据存储端4B 端口的错误计数器，没有发现用于判断4B 端口SFP 模块和4B 端口到交换机的连线的计数器有异常增长情况，因此可以排除 4B 端口SFP 模块和4B 端口到交换机的连线问题：

CRC: 如果该计数器不为0，基本上为存储端口SFP 模块问题；EOFa: 如果该计数器不为0，基本上为存储端口到交换机之间的连线问题

<html><body>| PORT LABEL = 4B |
| 16G FC Port Statistics |
| I Hex_Count I Decimal_Count I Port_Stats_Description |
|  |
|  |  |
| 00000000 0 |Link Failure / |  |
| 00000000 | 0 lLoss of Sync / |
| 00000000 0 ILoss | of signal |</body></html>

<html><body>| 00000000 | cid:) | 0 | IPrimitive Sequence Protocol Error |
|  |  | 0 | IInvalid Transmission Word |
|  | 00000000 | | 0 |  |
|  | 100000000 | | 0 | IInvalid CRC ILIP Occurred |
|  | 100000000 c:) | 0 | ILink UP |
|  | 一00000000 cid:) 100000000 | 0 | ILink Down_LoopInitializeTimeout |
|  | 100000000 c:) | 0 | |Loss of Signal |
|  | 00000000 c: | 0 | ILoss of Received Clock |
|  | 00000000 — | 0 | INOs_OLs >200ms continuously Received |
|  | 00000000 | 0 | |Link Reset Received |
| 100000000 |  | 0 | |LIP F7 Received |
| 100000000 | — | 0 | |LIP F8 Received |
| 100000000 |  | 0 | IConnected P2P Mode |
| 100000000 | — | 0 | IPort Configuration Changed |
| 100000000 |  | 0 |  |
| 100000000 | | | 0 | |L-Bit Detected |
| 100000000 |  | 0 | IConnection Fabric P2P |
| 100000000 |  | 0 | IConnection Fabric Loop |
| 100000000 | | | 0 | IConnection Private Loop |
| 100000000 |  | 0 | IConnection P2P INos or OLs for >20o mSec (or user defined value) in the |
| init f/w control block |
|  | 100000000 (cid:) | 0 | IP2P Link Event Timeout |
|  | 100000000 | | 0 | ILoop Initialize Protocol Error |
|  | 100000000 | | 0 | ILR Initiated by l6G_CHA Protocol CHIP |
|  | 100000000 | | 0 | ILRR Received by 16G_CHA Protocol CHIP |
|  | 100000000 | 0 | ILIP generated by IsP due to tout when attempt to transmit |
| non-data frame |
|  | 100000000 | | 0 |Response Queue Full |  |
|  | 100000000 | | 0 |ATIO Queue Full |  |
|  | 一00000000 | | 0 | IDrop AE due to lack of resources |
|  | 100000000 cid:) | 0 | IELS Protocol Error Detected by Firmware |
| / | 00000000 | 0 | IOPEN Device Failed |
|  | ID0B5C113 | 3501572371 | ITransmit Frame Count from 16G_CHA Protocol CHIP |
|  | 630B2376 | 1661674358 | IReceived Frame Count From l6G_ CHA Protocol CHIP |
|  | 00000000 | 0 | IDiscarded Frame Count From 16G_CHA Protocol CHIP |
|  | 100000001 | | 1 | |Frame Dropped by Firmware |
|  | 1 00000000 | | 0 | |LIP Primitives Received |
|  | 100000000 — | 0 | INOs Primitive Received |
|  | 100000000 | 0 | IOLs Primitive Received |
|  | 100000000 cd:) | 0 INot Used |  |
|  | 00000000 | 0 | INot Used |</body></html>

<html><body>|  |  |  |  |  |
|  | 00000000 一 | 0 | IClass2 Sequence Timeout |  |
|  | 00000000 | |  | 0 | IP_RJT Frame Tramsmit |
|  | 00000000 |  | 0 | IFailure to allocate exchange resource when receiving a |
|  | frame for a | new exchange |  |  |
|  | 00002630 |  | 9776 | |ABTs Received |
|  | 00000001 | 一 | 1 | IReceived sequences with a missing frame |
|  | 00000000 |  | 0 | ICorrectable Error |
|  | 0109FD7E |  | 17431934 | IMailbox Commands Issued |
|  | 00000000 |  | 0 | I Failure to allocate NportHandle when receiving an ELs frame |
|  | 00000000 | | | 0 | IReceived EOFa |</body></html>

###

写I/O 过程及错误特征码（示意）：

WRITE

![](images/1d00f1a8ef371b6d339b18ec2d5e12873593d18e28bd8f3f900d63c4f20a2261.jpg)

On a WRITE CMD Sequence, such as shown above, depending on which FRAME gets lost of damaged, will cause different SsB to be logged and cause a different level of Response Impact to the Host.
Thus understanding the SsB that are logged and how they correspond with the above errors can help focusing on where to look for errors in a Fabric and/or Internally in a DKC.
KEY SSB for WRITE IO related LINK issues : B65C, DDA1, B6FE, D034
There is some Notes below on when some of above LOG relative to the timing of the "Xo to X4" errors above.
The "Round-Trip Gaps 1 &2" shown above depend entirely on the DISTANCE between the HBA/INI and Target PORTS. Rule of thumb is "1ms'" per "100KM" per Round-Trip. This holds wel pretty well if the LINKS are purely DARK-FIBRE LINKS. If there is FCIP in a WAN things can change dramatically to the worse.

### 2.1.2 应用对应的 RDKC 存储日志分析

---
文档概要：报告分析了2025年3月10日起兴业证券两套数据库应用（UF20-DB01BHP和ZYO32_DB01JQ）的redo日志卷时延增高问题，涉及福州滨海和上海金桥的日立GAD双活存储，通过存储日志和性能数据分析定位原因。
本段概要：从RDKC存储日志分析，ZYO32_DB01JQP应用的4B端口在部分时段出现读写I/O传输延迟。
逻辑关联：上一节：2 问题分析
下一节：2.2 性能数据分析；章节名：
该章节与以下章节有关联：
---

从 RDKC 存储（31028）底层日志也可以看到 ZYO32_DB01JQP 应用对应的 4B 端口在部

分时段出现了I/O 传输延迟的现象，读和写方向都有，

<html><body>|  |  |  |  |  |
| 2025/03/11 10:24:49 | 1396 | 44 |  | : The number of segments per CPK as an additional information of ssB:13F3 occurred (Waiting for free segment) (Inhibited for 1 hour/Mp |
| 2025/03/11 10:24:49 | 13F3# | 44 |  | s_gfsgm At Hit/Miss, segment reservation timeout |
| 2025/03/11 10:24:29 | 10F5 | 4B |  | : timdiv Async processing was performed forcibly |
| 2025/03/1110:06:44 | FEFB# |  | PIOGI | : LINK ELS EVENI TyPe = PLOGI |
| 2025/03/11 10:06:43 | BECO# | 3E |  | : xlmain It FCP Frame-receives from non-LOGIN HOsT. |
| 2025/03/11 10:06:43 | B358# | 02 |  | : qlsnhlliocb LL IocB was issued |
| 2025/03/1110:06:43 | B3FE | 02 |  | snptovssb Information enhancement for transfer Tov |
| 2025/03/11 10:06:43 | B6AD# | 02 |  | : tpcc_xlfhostssb Information enhancement for transfer Tov/count exxor (Host information: Port ID, Wi) |
| 2025/03/11 10:06:43 | B6A.9# | 02 |  | Complementing information log for transfer Tov (IM) |
| 2025/03/11 10:06:43 | D034# | 02 | 40:6B | snptov fcmxzwtov Sync command Read/Write JoB Tov |
| 2025/03/11 10:06:43 | D031# | 02 | 40:6B | fcmxssbtv Additional infoxmation of SsB=d030/d034 (OPEN command, SCSI reset/Tov) |
| 2025/03/11 10:06:43 | DDA1# | 02 |  | cktov_lm Data transfer (Tachyon) completion Tov |
| 2025/03/11 10:06:43 | DDA1# | 02 | 4B 40:6B | cktov_lm Data transfer (Tachyon) completion Tov |
| 2025/03/11 10:06:43 | FEEB# |  | 4B LOGO | : LINK ELS EVENT TYPe = LOGO |
| 2025/03/11 10:06:34 | D555# | 02 | 40:6B | fcmxdssss Information enhancement log was output because job running time of more than l sec vas detected |
| 2025/03/11 09:41:46 |  |  | PLOGI |  |
| 2025/03/11 09:41:45 | FEFB# BECO# | 3D |  | : LINK ELS EVENT TYPe = PLOGI : xlmain It FcP Frame-receives from non-LoGIN HosT. |
| 2025/03/11 09:41:45 | B358# |  |  | : qlsnhlliocb LL IocB was issued |
| 2025/03/11 09:41:45 | B3FE | C | 4B | : snptovssb Information enhancement for transfer Tov |
|  |  |  | 4B 4B |  |
| 2025/03/11 09:41:45 2025/03/1109:41:45 | B6AD# | 0C B6A9# OC | 4B | : tpcc_xlfhostssb Information enhancement for transfer Tov/count erxox (Host information: Port ID, WiN) Complementing information log for transfer Tov (IM) |</body></html>

<html><body>| Date | Time | SSB |  |  | MPPORTLDEV | Hitachi SSB Refcode Description |
| 2025/03/1118:22:47 |  | 10E5 | 4E |  | : | timdiv Async processing was performed forcibly |
| 2025/03/1117:07:36 |  | 10E5 | 4D |  | : | timdiv Async processing was performed forcibly |
| 2025/03/11 | 16:50:24 | 12DD# | 44 |  | : c_rcvinv | When SCsI was reset, disabled message was received |
| 2025/03/11 | 16:50:24 | 16BD | 44 |  | : | r_ssvlEbd Target of LtoL MsG clearance was detected |
| 2025/03/1116:50:24 |  | D031# | 44 | 4B | 40:62 | fcmxssbtv Additional information of SSB-d030/d034 (OPEN cormand, SCsI reset/Tov) |
| 2025/03/11 16:50:24 |  | D030# | 44 | 4B | 40:62 : fcmxscrst | sCSI reset occurred (Information enhancement) |
| 2025/03/1116:50:24 |  | 16AD# | 44 | 4B | ssbl6al | Complementing information 2 of Erx-0xl699 |
| 2025/03/1116:50:24 |  | 16A1# | 44 | 4B | - sr_jobclr | Complementing information of Err-0xl699 |
| 2025/03/1116:50:24 |  | 1699# | 44 | 4B | sr_xstssb | sCSI reset processing execution (time etcof reset generating / Pson/Reboot / obstacle.) command, scsI reset/Tov) |
| 2025/03/11 16:41:32 |  | D031# | OE | 4B | 40:63 : fcmxssbty | Additional information of sSB=d030/d034 (OPEN |
| 2025/03/1116:41:32 |  | D030# | OE | 4B 40:63 | : fcmscrst | SCSI reset occurred (Information enhancement) |
| 2025/03/11 16:41:32 |  | 16AD# | OE | 4B | - x_ssbl6al | Complementing information 2 of Err=0xl699 |
| 2025/03/1116:41:32 |  | 16A1 | OE | 4日 | sr_jobclx | Complementing information of Err-Oxl699 |
| 2025/03/11 | 16:41:32 | 1699# | OE | 4B | sr_rstssb | SCSI reset processing execution (time etcof reset generating / Dso/Reboot / obstacle.) |
| 2025/03/11 | 16:39:53 | 12DD# |  |  | c_rcvinv | When SCSI was reset, disabled message was received |
| 2025/03/1116:39:53 |  | 16BD | OA |  |  | x_ssvlebd Target of LtoL MsG clearance was detected |
| 2025/03/1116:39:53 |  | D031# | OA | 4B 40:61 | : | fcmxssbtv Additional information of SSB-d030/d034 (OPEN conmand, SCSI reset/TOv) |
| 2025/03/11 16:39:53 |  | D030# | OA | 4B | 40:61 : fcmxscrst | SCSI reset occurred (Information enhancement) |
| 2025/03/11 | 16:39:53 | 16AD排 |  | 4日 | - I_ssbl6al | Complementing information 2 of Erx=0xl699 |
| 2025/03/1116:39:53 2025/03/11 16:39:53 |  | 16A1排 | OA | 4B 4B | : sr_jobclr | Complementing information of Err=Oxl699 |
| 2025/03/1115:46:18 |  | 1699# | OA |  | sr_Istssb | SCSI reset processing execution (time etcof reset generating/ PSON/Reboot / obstacle.) |
|  |  | AFBO | 3c |  |  | rcfbk_flg Config BK during Online completed |</body></html>

写 I/O 延迟，原因为“等待数据传输”，指向存储外部链路，依然和同一块 FC-HBA

卡有关（WWN=100000620B3AC203）：

<html><body>| DATE | TIME | PORT | LDEV# | CMD | KEY/ASC | HG-NAME | WAIT REASON | Host WWN |
| 2025/03/20 | 22:53:36 | 4B | 00:40:6C | 8A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/20 | 09:55:16 | 4B | 00:40:6D | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/20 | 09:51:53 | 4B | 00:40:6D | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/20 | 09:36:02 | 4B | 00:40:6D | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/18 | 22:53:28 | 4B | 00:40:6C | 8A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/12 | 10:35:00 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/11 | 10:06:43 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/11 | 09:41:45 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/10 | 14:56:07 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/10 | 14:42:27 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/03/10 | 14:03:16 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/02/13 | 10:47:46 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/02/13 | 10:18:25 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |</body></html>

<html><body>| 2025/02/13 | 10:12:59 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/02/13 | 10:08:54 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/02/13 | 10:04:38 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |
| 2025/02/13 | 09:53:47 | 4B | 00:40:6B | 2A | B/C001 | ZYO32_DB01JQP | Wait for Data Transfer | 100000620B3AC203 |</body></html>

读I/O 延迟，出现的频率更高一点，原因主要为“等待数据传输”，指向存储外部链路，依然和同一块 FC-HBA 卡有关（WWN=100000620B3AC203）：

<html><body>| DATE | TIME | PORT | RESET TYPE | WAIT REASON | Possible HG-NAME | Possible HBA-WWN |
| 3/20/2025 | 22:58:43 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 22:56:06 | 4B | ABTS(Abort Sequence) | Wait due to Slot Busy | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 22:52:09 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 22:52:08 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 22:49:11 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 22:48:18 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 16:52:27 | 4B | ABTS(Abort Sequence) | Wait for DMA Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 16:48:38 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 16:46:54 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 16:38:16 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 13:01:20 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/20/2025 | 9:54:10 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer |  |  |
| 3/20/2025 | 0:52:19 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP ZYO32_DB01JQP | 100000620B3AC203 |
| 3/19/2025 | 23:10:53 | 4B | ABTS(Abort Sequence) |  |  | 100000620B3AC203 |
| 3/18/2025 |  | 4B |  | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
|  | 23:14:40 23:13:57 |  | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/18/2025 3/18/2025 |  | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/18/2025 | 23:13:32 22:59:51 | 4B 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/18/2025 |  | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 100000620B3AC203 |
| 3/18/2025 | 22:54:01 | 4B | ABTS(Abort Sequence) ABTS(Abort Sequence) | Wait for DMA Data Transfer Wait for Data Transfer | ZYO32_DB01JQP |  |
| 3/18/2025 | 22:53:46 | 4B | ABTS(Abort Sequence) |  | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/18/2025 | 19:38:28 | 4B | ABTS(Abort Sequence) | Wait for DMA Data Transfer | ZYO32_DB01JQP ZYO32_DB01JQP | 100000620B3AC203 |
| 3/18/2025 | 19:32:06 |  |  | Wait for Stage/Destage Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 100000620B3AC203 |
|  | 19:29:43 | 4B | ABTS(Abort Sequence) |  |  | 100000620B3AC203 |
| 3/18/2025 | 19:27:20 | 4B | ABTS(Abort Sequence) | Wait for DMA Data Transfer | ZYO32_DB01JQP |  |
| 3/18/2025 | 19:25:59 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 100000620B3AC203 |
| 3/18/2025 | 19:23:10 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/18/2025 | 19:22:29 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP |  |
| 3/18/2025 | 19:18:10 19:16:38 | 4B 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 100000620B3AC203 |
| 3/18/2025 |  |  | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP |  |
| 3/18/2025 | 19:15:38 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |</body></html>

<html><body>| 3/18/2025 | 16:53:15 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/18/2025 | 16:45:05 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/17/2025 | 20:05:15 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/13/2025 | 1:24:46 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/12/2025 | 20:30:07 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/12/2025 | 16:57:10 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/12/2025 | 16:43:21 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 23:45:34 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 23:13:58 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 23:00:34 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 22:58:43 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 22:51:26 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 19:53:33 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 19:50:55 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 19:46:28 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 19:45:45 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 19:37:34 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 16:50:24 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 16:41:32 | 4B | ABTS(Abort Sequence) | Wait for DMA Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/11/2025 | 16:39:53 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 23:13:20 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 22:48:44 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 22:46:41 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:44:44 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:44:23 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:44:00 | 4B | ABTS(Abort Sequence) | Wait for DMA Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:34:27 | 4B | ABTS(Abort Sequence) | Wait for DMA Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:32:49 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:28:39 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:28:33 | 4B | ABTS(Abort Sequence) | Wait due to Slot Busy | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:26:05 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:25:06 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:24:58 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:23:49 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:20:55 | 4B | ABTS(Abort Sequence) | Wait due to Slot Busy | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:20:40 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 19:17:45 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 16:51:52 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 16:50:57 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |</body></html>

<html><body>| 3/10/2025 | 16:49:43 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
|  |  |  |  | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 3/10/2025 | 16:43:13 | 4B | ABTS(Abort Sequence) |  |  |  |
| 2/13/2025 | 23:34:38 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:33:20 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 100000620B3AC203 |
| 2/13/2025 2/13/2025 | 23:32:36 | 4B 4B | ABTS(Abort Sequence) ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
|  | 23:29:28 |  |  | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:27:23 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP |  |
| 2/13/2025 | 23:21:24 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:20:56 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:20:28 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:20:26 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:20:17 | 4B | ABTS(Abort Sequence) | Wait due to Slot Busy | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:18:06 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:15:15 | 4B | ABTS(Abort Sequence) | Wait for DMA Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:12:34 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:11:16 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:08:35 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:08:29 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:08:03 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:03:54 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:03:14 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:02:43 | 4B | ABTS(Abort Sequence) | Wait for Stage/Destage | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 23:02:31 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/13/2025 | 11:19:49 | 4B | ABTS(Abort Sequence) | Wait for DMA Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/12/2025 | 10:32:58 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/12/2025 | 0:07:03 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/12/2025 | 0:03:06 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |
| 2/11/2025 | 23:54:35 | 4B | ABTS(Abort Sequence) | Wait for Data Transfer | ZYO32_DB01JQP | 100000620B3AC203 |</body></html>

类似地，存储上4B 端口错误计数器并未出现异常增长，可排除存储4B 端口SFP 模块及端口到交换机的链路问题：

<html><body>| PORT LABEL = 4B |
| 16G FC Port Statistics |  |
| I Hex_CountI Decimal_Count | Port_Stats_Description |
|  |
|  |  |
| 00000000 00000000 | 0 ILink Failure / |</body></html>

<html><body>| 00000000 |  | 0 | lLoss of Signal |  |
|  | 100000000 | 0 |  | IPrimitive Sequence Protocol Error |
|  | 100000000 | 0 | IInvalid Transmission Word |  |
| / | 00000000 | 0 | |Invalid CRC |  |
|  | 00000000 c: | 0 | |LIP Occurred |  |
|  | 00000001 | | 1 | |Link UP |  |
|  | 00000000 c: | 0 | ILink Down_LoopInitializeTimeout |  |
|  | 00000001 | | 1 | lLoss of Signal |  |
|  | 100000000 | | 0 | |Loss of Received Clock |  |
| 100000000 | — | 0 |  | INOs_OLs >200ms continuously Received |
| 100000000 | — | 0 | |Link Reset Received |  |
| 100000000 |  | 0 | |LIP F7 Received |  |
| 100000000 | | | 0 | |LIP F8 Received |  |
| 100000001 | — | 1 | IConnected P2P Mode |  |
|  | 00000000 | | 0 | IPort Configuration Changed |  |
| 一00000000 | | | 0 | IL-Bit Detected |  |
| 100000001 |  | 1 | IConnection Fabric P2P |  |
|  | 100000000 c:) | 0 | IConnection Fabric Loop |  |
|  | 00000000 c:) | 0 | IConnection Private Loop |  |
|  | 00000000 | | 0 | IConnection P2P |  |
| 100000000 | | | 0 |  | INos or OLs for >200 mSec (or user defined value) in the |
| init f/w control block |
|  | 100000000 | | 0 | IP2P Link Event Timeout |  |
|  | 100000000 | 0 | ILoop Initialize Protocol Error |  |
|  | 一00000000 | | 0 | ILR Initiated by 16G_CHA Protocol CHIP |  |
|  | 100000000 c:) | 0 |  | ILRR Received by l6G_CHA Protocol CHIP |
|  | 100000000 | 0 |  | ILIP generated by IsP due to tout when attempt to transmit |
|  | non-data frame |  |  |  |
|  | 100000000 | 0 | |Response Queue Full |  |
|  | 100000000 | 0 | |ATIO Queue Full |  |
|  | 一00000000 cid:) | 0 | IDrop AE due to lack of resources |  |
|  | 100000000 | 0 |  | IELs Protocol Error Detected by Firmware |
|  | 100000000 | 0 | IOPEN Device Failed |  |
|  | 04B96737 | 79259447 |  | ITransmit Frame Count from 16G_CHA Protocol CHIP |
|  | DF924962 | 3750906210 |  | IReceived Frame Count From l6G_CHA Protocol CHIP |
|  | 00000000 | | 0 |  | IDiscarded Frame Count From l6G_CHA Protocol CHIP |
|  | 100000000 | 0 | |Frame Dropped by Firmware |  |
|  | 100000000 | | 0 | ILIP Primitives Received |  |
|  | 100000001 — | 1 | INOs Primitive Received |  |
|  | 00000000 | 0 | IOLs Primitive Received |  |
|  | 00000000 | 0 | INot Used |  |</body></html>

<html><body>|  |
| 00000000 | 0 INot Used |
| 00000000 0 IClass2 Sequence Timeout |  |
| 00000000 0 IP_RJT Frame Tramsmit |  |
| 00000000 | | 0 IFailure to allocate exchange resource when receiving a |
| frame for a | new exchange |
| 00002AED | | 10989 |ABTs Received |
| 00000000 | | 0 |Received sequences with a missing frame |
| 00000000 | 0 ICorrectable Error |
| 010A5D00 | 17456384 |Mailbox Commands Issued |
| 100000000 | | 0 I Failure to allocate NportHandle when receiving an ELs frame |</body></html>

读I/O 过程及错误特征码（示意）：

READ

![](images/4e99fb7e1ece6ebd42007db59e4163ea29106f02cadb274cef1e6c9fe7eee02c.jpg)

READ LINK errors are dificult to track inside a DUMP.If the CMD is received OK, then the TARGET PORT simply sends the DATA and STATUS, without any feedback and has to assume the Frames get delivered OK. Likewise if the CMD never gets to the DKC Port (error Xo ) then the DKC PORT sends nothing. Should an error happen at timing ( X1 ) the HBA/INI wil get to know about it and issue an ABTS immediately. If the error is at TIMING X0 or X2 then the HBA/INI wil TIMEOUT and issue an ABTS.

![](images/d7e6953fcb3200d9f1225cd4062153355393bca1bef80a6b7ed047507490ebac.jpg)

Depending on where the ERROR happened the DKC PORT will either LOG :

a) RESETD LOG (RESET Received) b) $\cdot$ / 16A1 / 16AD / 16AE (RESET Received) c) $\cdot$ (ABTS Reset sent after Timeout waiting for Response)

### 2.2 性能数据分析

---
文档概要：报告分析了2025年3月10日起兴业证券两套数据库应用（UF20-DB01BHP和ZYO32_DB01JQ）的redo日志卷时延增高问题，涉及福州滨海和上海金桥的日立GAD双活存储，通过存储日志和性能数据分析定位原因。
本段概要：分析存储资源利用率，显示CPU和Cache利用率合理，未见瓶颈。
逻辑关联：上一节：2.1.2 应用对应的 RDKC 存储日志分析
下一节：3 结论和建议；与“”存在并列关系：两者从不同角度（存储日志 vs. 性能指标）对同一问题进行剖析，相互补充，共同揭示根因。
---

2.2.1 存储资源利用率分析

存储全局共享资源CPU 和Cache 利用率均在合理范围内，未见异常，说明存储资源未出现瓶颈：

Processor busy "SN:31028(VSP 5100, 5500, 5100H, 5500H)"From $\because$ 2025/3/12 8:00:00 to 2025/3/12 11:00:00(sampling rate $\because$ 1min)100- MPU010-MP010(00)[Av.9.12, MPU120-MP120(CO)[Avg. 11.4,Max. 15] Max. 15]MPUO10-MP010(01)[Avg.9.32.Max.16] Max.19]MPUO1O-MP01O(02)[Avg.6.63, MPU120-MP120(02) [Avg. 10.69,Max.15] Max.18]MPU01O-MP01O(03) [Avg.8.65, MPU120-MP120(03)[Avg,10.66,Max.14] Max.18]80-MPUO10-MP010(05)[Avg.8.39.Max. 14] Max.16]MPUO10-MP010(06)[Avg.6.83, MPU120-MP120(C6)[Avg.10.58,Max.15] Max,18]MPU010-MP010(07)[Avg.8.86, MPU120-MP120(07)[Avg.10.61,Max. 15] Max. 17]MPU010-MP01Q(0s)[Avg.8.72, MPU120-MP120(C5)[Avg.10.35,60 MPUd10-MPo10(9) [Avg.8.73,Max,15] Max, 17]MPU120-MP120(OA)[Avg.7.77.Max,11] Max,13]MPUO10-MP01O(0B)[Avg. 7.15. MPU120-MP120(CB)[Avg.7.93,Max. 11] Max. 12]MPU120-MP120(CC) [Avg.7.98,40 Max., 12] Max. 13]MPU120-MP120(OD) [Avg.7.99,Max. 11] Max, 13]MPU010-MP01O(0E)[Avg.7.57. MPU120-MP120(CE)[Avg.7.97.Max.12] Max.13]MPUO1O-MP010(OF)[Avg.7.59, MPU120-MP120(CF)[Avg.7.93,Max.12] Max, 13]Max,12] Max.13]20-Max. 12] Max, 13]MAAMaMAN MPUO10-MP010(12)[Avg.7.49, Max. 12] Max. 13] MPU120-MP120(12)[Avg.8.21,6A02025/3/128:01:00 2025/3/128:51:00 2025/3/129:41:00 2025/3/1210:31:00Time [min]

![](images/e0348175abb35662f3553dbe0264b2b92448775a47722c1dcc30199bfbe22160.jpg)
Cache Write Pending Rate $[ \% 1 0 \% ]$ "SN:31028(VSP5100,5500,5100H, 5500H)"

2.2.2 Redo 日志卷性能分析

存储上显示 ZYO32_DB01JQP 应用所使用的 Redo 日志卷 40:6B 读写响应时间良好：写延迟在 $0 . 2 3 \mathrm { m s }$ 左右，读延迟在 $0 . 1 { \sim } 0 . 5 \mathrm { m s }$ 之间波动（波动和负载及链路有关），存储上观测到的性能压力较小，不存在性能问题：

![](images/d9a6999a53b89add38bbb90ec07f8bdd717bd127e682103a2ed112210056577b.jpg)

![](images/9c829735cf83acdc19f612fe7be5f004032ef9a242cd578426776dd7ffaf93ea.jpg)

2.2.3 关于存储读写响应时间

存储上的响应时间从数据帧被传输到存储端口开始计算，因此主机上看到的响应时间和存储端不会完全一致，如果存储上的响应时间处于正常范围内，而主机上的响应时间偏大，就可能是由于中间链路传输耗时所导致。

读I/O：延时可能出现在将目标数据传输至主机时所经过的链路

Read Sequence :

![](images/01df992d4048b09fdf8e33fd254822486ddb9411f6d36748ac619e146648e508.jpg)

写 I/O：延时可能出现在 XRDY 状态帧传输至主机时所经过的链路以及和主机确认写完成信号时所经过的链路

![](images/87491f3f4ea27d6e14cdf8b2c50d34a01205ace8cbf9b59362315e7c50fd0be3.jpg)

### 3 结论和建议

---
文档概要：报告分析了2025年3月10日起兴业证券两套数据库应用（UF20-DB01BHP和ZYO32_DB01JQ）的redo日志卷时延增高问题，涉及福州滨海和上海金桥的日立GAD双活存储，通过存储日志和性能数据分析定位原因。
本段概要：Redo日志卷时延因FC-HBA链路问题导致，建议排查相关组件，并给出持续问题时的性能数据收集方法。
逻辑关联：上一节：2.2 性能数据分析；与“”存在支持关系：
---

综上分析，Oracle 数据库应用的Redo 日志卷出现时延增加是由于存储外部问题，主要指向 FC-HBA 光纤卡（WWN=100000620B3AC203）到交换机这一侧的链路，建议重点排查这一段的链路及所有相关组件（FC-HBA、光纤线及 SFP 模块）尤其是 FC-HBA 卡，或者通过隔离法排除怀疑部件。

如果此类问题在隔离和排查后依然存在，建议如下：

1) 针对Redo 日志卷收集秒级性能数据（由于秒级收集的收集会产生性能开销，不建议持续收集，一般收集 10 分钟左右，可结合定时任务分段收集）；
2) 根据上述分析，存储的响应时间受到所经过的传输链路影响，如果怀疑存储内部资源处理I/O 耗时过久导致应用延迟变高，可部署收集程序获取存储内部处理I/O 用时