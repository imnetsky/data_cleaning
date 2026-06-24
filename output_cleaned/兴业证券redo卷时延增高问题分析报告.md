Date: 2025-03-21
Revision: 1.0 兴业证券数据库应用 redo 卷时延增高问题 分析报告
Product Type/Serial Number Microcode Revision Case Number
VSP F5100/31031&31029 90-09-22-00/00 05047439 目录
1 问题概述 ....................................................................................................................................... 3
2 问题分析 ....................................................................................................................................... 6
2.1 存储Dump日志分析 ....................................................................................................... 6
2.1.1 应用对应的 MDKC 存储日志分析 ...................................................................... 6
2.1.2 应用对应的 RDKC 存储日志分析 ....................................................................... 9
2.2 性能数据分析 ................................................................................................................. 16
2.2.1 存储资源利用率分析 .......................................................................................... 16
2.2.2 Redo 日志卷性能分析 ......................................................................................... 17
2.2.3 关于存储读写响应时间 ...................................................................................... 20
3 结论和建议 ................................................................................................................................. 21
1 问题概述 从 2025/3/10 开始，有两套数据库应用（UF20-DB01BHP 和 ZYO32_DB01JQ）所使用的 redo 日志卷陆续出现时延增高的现象，统计到的事件如下（以ZYO32_DB01JQ 为例）：
*** 2025-03-10 10:08:00.374
Warning: log write elapsed time 30839ms, size 7KB
*** 2025-03-10 10:08:24.394
--
*** 2025-03-10 10:19:05.334
Warning: log write elapsed time 30125ms, size 1KB
*** 2025-03-10 10:19:29.342
--
*** 2025-03-10 13:02:20.342
Warning: log write elapsed time 30420ms, size 1KB
*** 2025-03-10 13:03:35.341
--
*** 2025-03-10 13:09:10.534
Warning: log write elapsed time 30370ms, size 0KB
*** 2025-03-10 13:09:16.543
--
*** 2025-03-10 13:50:49.334
Warning: log write elapsed time 30155ms, size 2KB
*** 2025-03-10 13:51:01.341
--
*** 2025-03-10 13:57:14.359
Warning: log write elapsed time 30504ms, size 1KB
*** 2025-03-10 13:57:47.360
--
*** 2025-03-10 14:03:02.751
Warning: log write elapsed time 11065ms, size 1KB
*** 2025-03-10 14:03:11.755
--
*** 2025-03-10 14:28:47.574
Warning: log write elapsed time 30814ms, size 1KB
*** 2025-03-10 14:29:50.581
--
*** 2025-03-10 14:42:13.240
Warning: log write elapsed time 11178ms, size 2KB
NSS2 is not running anymore.
--
*** 2025-03-10 14:55:53.264
Warning: log write elapsed time 11115ms, size 4KB
*** 2025-03-10 14:55:56.284
--
*** 2025-03-11 09:41:35.222
Warning: log write elapsed time 11021ms, size 2KB
*** 2025-03-11 09:42:32.234
--
*** 2025-03-11 09:50:22.335
Warning: log write elapsed time 30971ms, size 6KB
*** 2025-03-11 09:50:28.340
--
*** 2025-03-11 10:06:32.714
Warning: log write elapsed time 11037ms, size 1KB
*** 2025-03-11 10:06:59.721
--
*** 2025-03-11 10:32:39.325
Warning: log write elapsed time 11227ms, size 8KB
*** 2025-03-11 10:33:21.331
--
*** 2025-03-11 13:14:10.358
Warning: log write elapsed time 30656ms, size 1KB
*** 2025-03-11 13:14:19.361
--
*** 2025-03-11 13:55:35.638
Warning: log write elapsed time 30959ms, size 1KB
*** 2025-03-11 13:56:08.641
--
*** 2025-03-11 19:55:31.390
Warning: log write elapsed time 11359ms, size 1KB
*** 2025-03-11 19:56:10.392
*** 2025-03-12 09:40:35.638
Warning: log write elapsed time 30239ms, size 1KB
*** 2025-03-12 09:44:38.642
--
*** 2025-03-12 10:34:49.422
Warning: log write elapsed time 11062ms, size 5KB
*** 2025-03-12 10:40:04.431
--
*** 2025-03-12 11:13:31.351
Warning: log write elapsed time 30087ms, size 3KB
*** 2025-03-12 11:13:49.368 这两套应用分别连接到位于福州滨海数据中心和上海金桥数据中心的日立 GAD 双活存 储，涉及的这4台存储配置情况如下表。
bh71 bh72 jq71 jq72
SN 31031 31251 31029 31028 安装位置 福州滨海 福州滨海 上海金桥 上海金桥 磁盘 50*7.6TB NVMe 50*7.6TB NVMe 50*7.6TB NVMe 50*7.6TB NVMe
6D+2P 6D+2P 6D+2P 6D+2P 可用容量 247.58 247.58 247.58 247.58
(TB)
Cache 1TB 1TB 1TB 1TB
CHB 4对 4对 4对 4 对 前端口 24*32Gbps 24*32Gbps 24*32Gbps 24*32Gbps
Firmware 90-09-22-00/00 90-09-22-00/00 90-09-22-00/00 90-09-22-00/00
SVOS 9.9 9.9 9.9 9.9 备注 GAD Primary GAD Secondary GAD Primary GAD Secondary 应用和存储的连接拓扑示意图如下：

应用使用的日志卷为：
⚫ UF20-DB01BHP:03:22，使用的存储端口为：3C/4D
⚫ ZYO32_DB01JQ:40:6B，使用的存储端口为：3A/4B
2 问题分析
2.1 存储 Dump 日志分析
2.1.1 应用对应的 MDKC 存储日志分析 从 MDKC 存储（31029）底层日志可以看到 ZYO32_DB01JQP 应用对应的 4B 端口在部 分时段出现了I/O传输延迟的现象，出现延迟的卷正是这套应用所使用的Redo日志道卷，大 部分为写I/O(SCSI CMD=2A:write）方向，根据出现的SSB 特征码D034/D031,I/O传输延 迟的原因为“等待数据传输”，问题指向存储外部链路端，其构成组件包括
1)FC-HBA(WWN=100000620B3AC203)、2)FC-HBA 到交换机的光纤线、3)FC-HBA在交换机 上的SFP 模块、4)存储4B 端口上的SFP 模块、5)存储 4B 到交换机的光纤线、6) 存储4B 端 口在交换机上的SFP 模块：
Refcode = D034 : fcmxrwtov Sync command Read/Write JOB TOV
DATE TIME PORT LDEV# CMD KEY/ASC HG-NAME WAIT REASON HOST WWN / IQN F C ID
2025/03/11 19:55:32 4B 00:04:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203 490000
2025/03/11 10:32:42 4B 00:04:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203 490000
2025/02/13 23:11:12 4B 00:04:6C 8A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203 490000
2025/02/13 23:01:26 4B 00:04:6C 8A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203 490000
2025/02/13 09:59:30 4B 00:04:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203 490000
2025/02/13 09:53:15 4B 00:04:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203 490000
2025/02/13 09:49:28 4B 00:04:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203 490000
2025/02/12 10:10:25 4B 00:04:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203 490000 根据存储端4B 端口的错误计数器，没有发现用于判断4B 端口SFP模块和4B 端口到交 换机的连线的计数器有异常增长情况，因此可以排除 4B 端口SFP 模块和4B 端口到交换机的 连线问题：
⚫ CRC: 如果该计数器不为0，基本上为存储端口SFP 模块问题；
⚫ EOFa: 如果该计数器不为0，基本上为存储端口到交换机之间的连线问题
PORT LABEL = 4B
16G FC Port Statistics
| Hex_Count | Decimal_Count | Port_Stats_Description
|-----------|---------------|---------------------------------------------------

---------------------------------------
| 00000000 | 0 |Link Failure
| 00000000 | 0 |Loss of Sync
| 00000000 | 0 |Loss of Signal
| 00000000 | 0 |Primitive Sequence Protocol Error
| 00000000 | 0 |Invalid Transmission Word
| 00000000 | 0 |Invalid CRC
| 00000000 | 0 |LIP Occurred
| 00000000 | 0 |Link UP
| 00000000 | 0 |Link Down_LoopInitializeTimeout
| 00000000 | 0 |Loss of Signal
| 00000000 | 0 |Loss of Received Clock
| 00000000 | 0 |NOS_OLS >200ms continuously Received
| 00000000 | 0 |Link Reset Received
| 00000000 | 0 |LIP F7 Received
| 00000000 | 0 |LIP F8 Received
| 00000000 | 0 |Connected P2P Mode
| 00000000 | 0 |Port Configuration Changed
| 00000000 | 0 |L-Bit Detected
| 00000000 | 0 |Connection Fabric P2P
| 00000000 | 0 |Connection Fabric Loop
| 00000000 | 0 |Connection Private Loop
| 00000000 | 0 |Connection P2P
| 00000000 | 0 |NOS or OLS for >200 mSec (or user defined value) in the

init f/w control block
| 00000000 | 0 |P2P Link Event Timeout
| 00000000 | 0 |Loop Initialize Protocol Error
| 00000000 | 0 |LR Initiated by 16G_CHA Protocol CHIP
| 00000000 | 0 |LRR Received by 16G_CHA Protocol CHIP
| 00000000 | 0 |LIP generated by ISP due to tout when attempt to transmit

non-data frame
| 00000000 | 0 |Response Queue Full
| 00000000 | 0 |ATIO Queue Full
| 00000000 | 0 |Drop AE due to lack of resources
| 00000000 | 0 |ELS Protocol Error Detected by Firmware
| 00000000 | 0 |OPEN Device Failed
| D0B5C113 | 3501572371 |Transmit Frame Count from 16G_CHA Protocol CHIP
| 630B2376 | 1661674358 |Received Frame Count From 16G_CHA Protocol CHIP
| 00000000 | 0 |Discarded Frame Count From 16G_CHA Protocol CHIP
| 00000001 | 1 |Frame Dropped by Firmware
| 00000000 | 0 |LIP Primitives Received
| 00000000 | 0 |NOS Primitive Received
| 00000000 | 0 |OLS Primitive Received
| 00000000 | 0 |Not Used
| 00000000 | 0 |Not Used
| 00000000 | 0 |Class2 Sequence Timeout
| 00000000 | 0 |P_RJT Frame Tramsmit
| 00000000 | 0 |Failure to allocate exchange resource when receiving a

frame for a new exchange
| 00002630 | 9776 |ABTS Received
| 00000001 | 1 |Received sequences with a missing frame
| 00000000 | 0 |Correctable Error
| 0109FD7E | 17431934 |Mailbox Commands Issued
| 00000000 | 0 |Failure to allocate NportHandle when receiving an ELS frame
| 00000000 | 0 |Received EOFa

-------------------------------------------------- 写I/O过程及错误特征码（示意）：
2.1.2 应用对应的 RDKC 存储日志分析 从RDKC 存储（31028）底层日志也可以看到ZYO32_DB01JQP 应用对应的4B 端口在部 分时段出现了I/O传输延迟的现象，读和写方向都有，
⚫ 写 I/O 延迟，原因为“等待数据传输”，指向存储外部链路，依然和同一块 FC-HBA 卡有关（WWN=100000620B3AC203）：
DATE TIME PORT LDEV# CMD KEY/ASC HG-NAME WAIT REASON Host WWN
2025/03/20 22:53:36 4B 00:40:6C 8A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/20 09:55:16 4B 00:40:6D 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/20 09:51:53 4B 00:40:6D 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/20 09:36:02 4B 00:40:6D 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/18 22:53:28 4B 00:40:6C 8A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/12 10:35:00 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/11 10:06:43 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/11 09:41:45 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/10 14:56:07 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/10 14:42:27 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/03/10 14:03:16 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/02/13 10:47:46 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/02/13 10:18:25 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/02/13 10:12:59 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/02/13 10:08:54 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/02/13 10:04:38 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
2025/02/13 09:53:47 4B 00:40:6B 2A B/C001 ZYO32_DB01JQP Wait for Data Transfer 100000620B3AC203
⚫ 读I/O延迟，出现的频率更高一点，原因主要为“等待数据传输”，指向存储外部链 路，依然和同一块 FC-HBA卡有关（WWN=100000620B3AC203）：
DATE TIME PORT RESET TYPE WAIT REASON Possible HG-NAME Possible HBA-WWN
3/20/2025 22:58:43 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 22:56:06 4B ABTS(Abort Sequence) Wait due to Slot Busy ZYO32_DB01JQP 100000620B3AC203
3/20/2025 22:52:09 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 22:52:08 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 22:49:11 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 22:48:18 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 16:52:27 4B ABTS(Abort Sequence) Wait for DMA Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 16:48:38 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 16:46:54 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/20/2025 16:38:16 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 13:01:20 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 9:54:10 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/20/2025 0:52:19 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/19/2025 23:10:53 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 23:14:40 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 23:13:57 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 23:13:32 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 22:59:51 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 22:54:01 4B ABTS(Abort Sequence) Wait for DMA Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 22:53:46 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:38:28 4B ABTS(Abort Sequence) Wait for DMA Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:32:06 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:29:43 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:27:20 4B ABTS(Abort Sequence) Wait for DMA Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:25:59 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:23:10 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:22:29 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:18:10 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:16:38 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 19:15:38 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/18/2025 16:53:15 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/18/2025 16:45:05 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/17/2025 20:05:15 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/13/2025 1:24:46 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/12/2025 20:30:07 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/12/2025 16:57:10 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/12/2025 16:43:21 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/11/2025 23:45:34 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/11/2025 23:13:58 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/11/2025 23:00:34 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/11/2025 22:58:43 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/11/2025 22:51:26 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/11/2025 19:53:33 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/11/2025 19:50:55 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/11/2025 19:46:28 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/11/2025 19:45:45 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/11/2025 19:37:34 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/11/2025 16:50:24 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/11/2025 16:41:32 4B ABTS(Abort Sequence) Wait for DMA Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/11/2025 16:39:53 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/10/2025 23:13:20 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 22:48:44 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/10/2025 22:46:41 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:44:44 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:44:23 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:44:00 4B ABTS(Abort Sequence) Wait for DMA Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:34:27 4B ABTS(Abort Sequence) Wait for DMA Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:32:49 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:28:39 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:28:33 4B ABTS(Abort Sequence) Wait due to Slot Busy ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:26:05 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:25:06 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:24:58 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:23:49 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:20:55 4B ABTS(Abort Sequence) Wait due to Slot Busy ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:20:40 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 19:17:45 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 16:51:52 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/10/2025 16:50:57 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
3/10/2025 16:49:43 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
3/10/2025 16:43:13 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:34:38 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:33:20 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:32:36 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:29:28 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:27:23 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:21:24 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:20:56 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:20:28 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:20:26 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:20:17 4B ABTS(Abort Sequence) Wait due to Slot Busy ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:18:06 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:15:15 4B ABTS(Abort Sequence) Wait for DMA Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:12:34 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:11:16 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:08:35 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:08:29 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:08:03 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:03:54 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:03:14 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:02:43 4B ABTS(Abort Sequence) Wait for Stage/Destage ZYO32_DB01JQP 100000620B3AC203
2/13/2025 23:02:31 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/13/2025 11:19:49 4B ABTS(Abort Sequence) Wait for DMA Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/12/2025 10:32:58 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/12/2025 0:07:03 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/12/2025 0:03:06 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203
2/11/2025 23:54:35 4B ABTS(Abort Sequence) Wait for Data Transfer ZYO32_DB01JQP 100000620B3AC203 类似地，存储上4B 端口错误计数器并未出现异常增长，可排除存储4B 端口SFP 模块及 端口到交换机的链路问题：
PORT LABEL = 4B
16G FC Port Statistics
| Hex_Count | Decimal_Count | Port_Stats_Description
|-----------|---------------|---------------------------------------------------

---------------------------------------
| 00000000 | 0 |Link Failure
| 00000000 | 0 |Loss of Sync
| 00000000 | 0 |Loss of Signal
| 00000000 | 0 |Primitive Sequence Protocol Error
| 00000000 | 0 |Invalid Transmission Word
| 00000000 | 0 |Invalid CRC
| 00000000 | 0 |LIP Occurred
| 00000001 | 1 |Link UP
| 00000000 | 0 |Link Down_LoopInitializeTimeout
| 00000001 | 1 |Loss of Signal
| 00000000 | 0 |Loss of Received Clock
| 00000000 | 0 |NOS_OLS >200ms continuously Received
| 00000000 | 0 |Link Reset Received
| 00000000 | 0 |LIP F7 Received
| 00000000 | 0 |LIP F8 Received
| 00000001 | 1 |Connected P2P Mode
| 00000000 | 0 |Port Configuration Changed
| 00000000 | 0 |L-Bit Detected
| 00000001 | 1 |Connection Fabric P2P
| 00000000 | 0 |Connection Fabric Loop
| 00000000 | 0 |Connection Private Loop
| 00000000 | 0 |Connection P2P
| 00000000 | 0 |NOS or OLS for >200 mSec (or user defined value) in the

non-data frame
| 00000000 | 0 |Response Queue Full
| 00000000 | 0 |ATIO Queue Full
| 00000000 | 0 |Drop AE due to lack of resources
| 00000000 | 0 |ELS Protocol Error Detected by Firmware
| 00000000 | 0 |OPEN Device Failed
| 04B96737 | 79259447 |Transmit Frame Count from 16G_CHA Protocol CHIP
| DF924962 | 3750906210 |Received Frame Count From 16G_CHA Protocol CHIP
| 00000000 | 0 |Discarded Frame Count From 16G_CHA Protocol CHIP
| 00000000 | 0 |Frame Dropped by Firmware
| 00000000 | 0 |LIP Primitives Received
| 00000001 | 1 |NOS Primitive Received
| 00000000 | 0 |OLS Primitive Received
| 00000000 | 0 |Not Used
| 00000000 | 0 |Not Used
| 00000000 | 0 |Class2 Sequence Timeout
| 00000000 | 0 |P_RJT Frame Tramsmit
| 00000000 | 0 |Failure to allocate exchange resource when receiving a

frame for a new exchange
| 00002AED | 10989 |ABTS Received
| 00000000 | 0 |Received sequences with a missing frame
| 00000000 | 0 |Correctable Error
| 010A5D00 | 17456384 |Mailbox Commands Issued
| 00000000 | 0 |Failure to allocate NportHandle when receiving an ELS frame
| 00000000 | 0 |Received EOFa

读I/O过程及错误特征码（示意）：

2.2 性能数据分析
2.2.1 存储资源利用率分析 存储全局共享资源CPU 和Cache利用率均在合理范围内，未见异常，说明存储资源未出 现瓶颈：

2.2.2 Redo 日志卷性能分析 存储上显示 ZYO32_DB01JQP 应用所使用的 Redo 日志卷 40:6B 读写响应时间良好：写 延迟在0.23ms 左右，读延迟在0.1~0.5ms 之间波动（波动和负载及链路有关），存储上观测到 的性能压力较小，不存在性能问题：

2.2.3 关于存储读写响应时间 存储上的响应时间从数据帧被传输到存储端口开始计算，因此主机上看到的响应时间和 存储端不会完全一致，如果存储上的响应时间处于正常范围内，而主机上的响应时间偏大， 就可能是由于中间链路传输耗时所导致。
读I/O：延时可能出现在将目标数据传输至主机时所经过的链路 写 I/O：延时可能出现在 XRDY 状态帧传输至主机时所经过的链路以及和主机确认写完 成信号时所经过的链路
3 结论和建议 综上分析，Oracle数据库应用的Redo 日志卷出现时延增加是由于存储外部问题，主要指 向 FC-HBA 光纤卡（WWN=100000620B3AC203）到交换机这一侧的链路，建议重点排查这 一段的链路及所有相关组件（FC-HBA、光纤线及 SFP 模块）尤其是 FC-HBA 卡，或者通过 隔离法排除怀疑部件。
如果此类问题在隔离和排查后依然存在，建议如下：
1) 针对Redo 日志卷收集秒级性能数据（由于秒级收集的收集会产生性能开销，不建议 持续收集，一般收集 10分钟左右，可结合定时任务分段收集）；
2) 根据上述分析，存储的响应时间受到所经过的传输链路影响，如果怀疑存储内部资 源处理I/O耗时过久导致应用延迟变高，可部署收集程序获取存储内部处理I/O用时