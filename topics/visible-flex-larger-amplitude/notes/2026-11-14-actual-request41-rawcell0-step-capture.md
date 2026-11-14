# actual41：868 个原步局部 J 已采集，72 个原出口与 mean 逐位保持

2026-11-14。公开 run **43622149326**，source **0beffe5a963015a4063a8c53d4a92fec32205005**，job **132530011605**，artifact **14124209116**（`visible-mainline-rawcell0steps-43622149326-1`）。ZIP 为349636774 B，SHA256 `356d9d81959739a22e9347d7ceba6fd4880ad61db70dca73096a4c5b71dc73a8`。取回时仅因本地空间重做了已核ZIP的提取，没有重跑科学计算。

## 1. 实际完成范围

[原步采集接口](2026-11-14-native-rawcell0-original-step-capture-interface.md)已在同一actual28基态运行，覆盖原 rawCell0 的全部 **72个stage**。真实完成 **868个原RK步、868个完整224×224局部J、3472次原field返回**。

其中原stage **11、28、31、63** 使用原cusp `integrationGrid`，各13步；其余68段各12步。原profile、原x/h算式、全部226项state、两个mean积分、原出口port及原H/far/graphs/gains/σ都保持各自原定义。局部变分每原步从单位切向开始，未相乘构造长J。

producer报告，并由取回后的独立字节审计确认：

- **全部72段最后的224项旧坐标出口，与actual28原 `stage-out` 逐位相同。**
- **全部72组 `[minA,minD,原mean和]` 与actual28原三项记录逐位相同。** 原mean和取producer的原加法结果；本地没有重新计算其和。
- 全部原226项入端、内部shape输出与所存完整state、原577节点映射及所有显式σ位都对应。
- 868个局部J全部有限，原guards都正常返回。没有据此把局部J认作精确连续导数，也没有推断新全系统已有效。

局部capture用时 **120.085秒**，完整launcher **144.8467704秒**。原native solve、独立no-J、原完整长J、整尾J、Newton trial、endpoint J及最终audit调用均为0。

唯一协议请求在原solve之前按计划抛出 `VISIBLE_NATIVE_RAWCELL0_STEP_CAPTURE_COMPLETE_V1`；原worker如实返回该failed字符串，随后exit0。`capture_completed=true`只表示限定采集完成；`native_accepted=false,task_completed=false`保持。

## 2. 局部 J 的现有统计

本表仅整理producer已经保存的逐块最大条目记录，没有本地重算任何J、矩阵范数、SVD、condition或极值。每个所列极值位置的实际原字节已核。

| 原stage / rawSegment | 实际local step | 已报最大绝对条目 |
|---|---:|---:|
| 44 / 3 | 10 | `1.5739595340282963e13` |
| 44 / 3 | 9 | `1.5331417670668938e13` |
| 44 / 3 | 11 | `1.4368422225223666e13` |
| 44 / 3 | 8 | `1.3142322861209266e13` |
| 43 / 3 | 0 | `1.1738208087660783e13` |
| 44 / 3 | 7 | `9.726514434692256e12` |
| 43 / 3 | 1 | `8.614090342111761e12` |
| 58 / 1 | 7 | `8.31861884226947e12` |

这些都是ordinary分支中的原步序号。尽管新单步块的条目尺度与先前长块不同，单看条目大小仍不能判断完整新系统的可解性、原σ缺陷或原nonlinear trial是否成功。下一步须实际组装同一捕获对象并检查完整方向。

原 `rhsWithJacobian` 已返回的 geometry number fields也全部保存：72个gzip packet，629099 B压缩、7547943 B解压。它们包含真实 `r,drdx,w,w2,E` 等数值bits和原field状态SHA；没有增加额外RHS、root或geometry调用。此处不提前把这些记录解释成新的局部稳定性结论。

## 3. 动态新系统的真实尺寸

原0..71的72个长块由实际868个局部块替换；原72..575的 **504个原块**仍可按原输入逐位复用。因此候选新系统为：

| 项目 | 实际metadata值 |
|---|---:|
| 新stage数 | 1372 |
| 新节点数 | 1373 |
| 完整未知数 | 307552 |
| 原节点数 | 577，全保 |
| 带宽 | `kl=112, ku=335` |
| LAPACK AB行数 | 560 |
| 单份AB字节预算 | 1377832960 |

`oldToNew`全部577个索引已核。shooting按外→内排，同一原段的捕获flow顺序反转；所有新增节点σ明确复制其原parent stage的σ，旧节点σ逐位不变。新cut/far/H仍绑定同一原件。

此layout尚未安装进原native对象，不是新系统成功结果。独立动态消费者的完整小metadata合同也已只读核过：全72report/window、868条schedule、完整1372个layout cells、577个oldToNew以及shape/port字段与冻结入口吻合。没有因此在本地构造系统或重算r。

后继将直接以原actual28为父，消费原504块与本次868局部块，保存独立新矩阵身份及完整缺陷。它不在失败578系统上累叠，不冒旧 `394ca2…` 矩阵。方向未来限制到旧577节点后，真正readback仍是原完整nonlinear no-J、原guards、原σ和原trial接受公式。

## 4. 产物身份与完整字节审计

| 产物 | 字节 | SHA256 |
|---|---:|---|
| `result.json` | 78403 | `6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf` |
| `rawcell0-step-summary.json` | 12021 | `ab20cc260b8a0a1e6642aa26c70b11575dee9a9245ac467482d8095f410e9594` |
| `rawcell0-step-array-manifest.json` | 938674 | `fcfc6f76d7bba92aa38eb793dc055d2dbbe7ab098218ac1c036f2ad67512ede6` |
| `rawcell0-step-spec.json` | 180567 | `ac6f99929ea09e30e97a3a2b2649a2b25d24f7a05d5adae4357a1034299c0da0` |
| `prospective-rawcell0-step-layout.json` | 236926 | `5f2e7ea49915dfca676277c81ef4e5463eab72bdcb1882aba437630a69d59ef4` |

[完整字节审计](2026-11-14-actual-request41-byte-identity-audit.json)覆盖本capture的全部 **3999个实际文件**：

- 381个top inventory文件，4711071 B，全部size/SHA相符。
- 原actual28全部29数组、116chunks、238972680 B重新流式核SHA，原输入和参考来源完整。
- 新289数组、3545chunks、354799016 B全部核SHA、shape、连续行序和交错chunk ledger全覆盖。
- 全868个局部J的finite/NaN/Inf/正负零位分类与producer统计相符；全部已报极值operand bits对应原数组位置。没有重新寻找极值。
- 全72个geometry packet的manifest/report描述符、压缩和解压SHA相符。
- 3472条field记录、71452个数值word，连同profile/step/field顺序、普通与cusp分支、实际x/h记录、原出口port均核。没有重新生成grid或执行浮点RK。
- 全部原226项输入、内部输出到完整state的对应、72段最终出口和72组guard/mean均逐位核；完整显式σ按声明的复制规则逐位核。

没有本地运行RHS、RK、J、dot、norm、线性求解或精确缺陷计算。新大数组及field packets仍只在Actions artifact中保全，仓库保存源、manifest与小结果。本题全闭面、幅度、reach、δE及完成标准未由本次采集核销。
