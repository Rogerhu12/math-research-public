# 97q：真实4bd9与原pending339的正常完整物理续算

2026-11-27，会话 `Astra-new-mechanism-1f4a61a4-20261127`。
这是实际终态的必要后继输入和薄wrapper。本地仅作原JSON、源码、AST、hash及必要网格坐标核对；没有运行优化、ODE、FFT或新科学诊断。所有既有科学函数保持已发布字节。

## 1. 从哪一个实际状态继续

来源是原pending330范围的自然终态：

- source `b86ec60074123372cc774ad13629f412512c79f6`；run [45916249440](https://github.com/Rogerhu12/math-research-public/actions/runs/45916249440)，job `140236066717`。
- 原runtime public pull `5777da76dbb3927ff9f4ec7c1a1b0d37b4237156`。
- 原科学2408.826496151秒，`scientific_clock_checkpoint_not_complete`；它既没有自然OptimizeResult，也没有数值stall，`stalled_outer_count=0`。
- 原完整事实见[唯一自然终态收据](2026-11-27-r582-pending330-original-terminal.md)。

实际保留97q为

`4bd9258b175c5d8e67140c0a7b6eeb68ee98cfe12479673c756a88e6ee8fea48`。

其η为 `3.616136752215837e-5`，原物理违反为0、工作违反为 `1.4877377021299543e-10`。它属于原完整16203×3072 fine资格，不把工作余量写成精确0。原材料实际身份为

`0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`。

| 源实际状态 | 原值 |
|---|---|
| p / epsilon | `.181` / `.0010000000000000009` |
| 当前phase | metric |
| 当前coarse | 334径向×1536角 |
| 当前和资格fine | 同一16203径向×3072角 |
| 当前/拟定trust | 2 / 2 |
| 已登记pending | 5个径向点，0个角升级 |
| 原明确拟定下一coarse | 339径向×1536角 |

原334 coarse SHA为 `74d43ced0bdef271c2c4fa65092c2fe39e32285998d02f5fecf2efa54a8394f8`；原16203 fine SHA为 `f4770c7aab814ba2e9e47421f28c287e82e5c72e3c1eb9808cb2644576f3d129`。五个pending是

```text
.1529296875, .153369140625, .30366210937500004,
.638671875, .8695631219545128
```

该数组SHA为 `d9ec0078c586b9175002191da96ddf2d9b6c516843ca0ced41970ca470a537d9`；拟定339 coarse的SHA为 `005cdecbffc954799526aafbbb9547c089b34f850e880feaf05538bb6c000d03`。新输入逐字保留来源FINAL，并按原driver采用这五个已付证据。339尚未优化过，不伪装成来源已经通过的网格。

## 2. raw c4b9与真实half-copy 4bd9

最后raw候选为

`c4b916999bf27d2565550b3afb3c05f40dcb1c658c20a4591d0af8e21adb2ca2`。

它的完整当前backend行违反 `3.412826463316756e-6`、epigraph `3.581566503571331e-5`，没有fine资格，`retained_by_this_raw_callback=false`。

这次与上一来源的raw情况不同：同一次callback的独立fraction `.5` 物理副本，正是最后真实保留4bd9。副本完成完整fine并被接受，epigraph为 `3.609195544585496e-5`，原完整物理行违反 `1.4877199385615603e-10`。这没有把raw本身变成合格点。

新wrapper分别核对raw身份、原不可行行值、未获fine事实、`retained_from_separate_assessment=true`、独立half-copy身份和最后完整scan。真实best仍为4bd9；raw仅按已发布算法作为未合格warm候选保存。没有把raw工作向量改成接受副本，也不从未输出的第8份Jacobian虚构一个新的raw候选。

## 3. 八个新中点强制支付新的完整入口资格

原baseline复用分支比较p、q、完整scan标记、fine径向数组及角数。它没有独立的材料SHA复用判据；本scope不另声称有这一门。

对原JSON拟定339数组取相邻中点，再与原16203 fine作必要输入比较，新增以下八点：

```text
0.15146484375
0.1531494140625
0.1563720703125
0.30183105468750004
0.30629882812500003
0.6392578124999999
0.8695628696410034
0.8695633742680222
```

这是输入坐标的文本/JSON核对，没有求场值。原driver依然取永久fine、实际材料观察点、coarse及全部相邻中点的并集；因此新入口fine必不同于旧16203，至少包含其全部旧点和这八个新点。若必要材料重建增加其他真实观测点，也照原算法保留。最终真实fine大小和SHA由新run报告，不预先授予16211的资格。

同一个实际构造的field对象用于新入口完整扫描、后续全部backend、AD、粗网和fine。即使重建后的材料身份与来源不同，这个已经变化的fine也要求同一新对象支付完整新资格；不能借旧4bd9通过值。原 `material_mesh_binary64_sha256` 已含所有材料knots和六分量端点值，source身份及实际新mesh均如实保留，不换标签。

新的入口或交换若发现原working物理余量违约，仍进入原geometry restoration；满足原条件才回metric。所有ball、strip、正高、det、mean-E、曲率正负、mirror等原行、完整metric行、box、trust、粗网/全fine门、独立epigraph提升、物理回溯及raw/best分轨均不改。

## 4. 薄wrapper和原科学实现的边界

新wrapper先核原pending330 source/request，通过原父 `load_input` 取得固定材料seed、冻结reference q、原控制参数与所有历史ledger；然后仅以本次唯一原FINAL替换后继的实际状态、当前/拟定网格、pending、真实best及未合格raw。

`NonlinearRows`、`FineObserver`、StableField、tail columns、完整97q和第98个epigraph变量、原SLSQP接口及所有接受函数均保持原字节。本线最后一个backend已真实完成8份Jacobian，并有连续metric接受，不把B030的首callback交换饥饿形态套到这里。新范围不接82维native曲率helper，不补造未保存的旧SLSQP内部H/workspace。

原request中的 `initial_radial_nodes=298` 等历史字面参数照原值保留；真正续接网来自来源FINAL明确给出的339数组，不用历史基数重新生成一个网。原stage门、p目标 `.8`、末η门 `1e-7`、所有完整几何阈值保持。

单lane、单并发job，科学预算仍2400秒、末预留30秒；实际原子操作和真实elapsed照实计，不裁成标称预算。原串行97q组不变，只由本新request的push触发，不额外dispatch。

## 5. 全部已付与未闭成本

原2408.826496151秒内有8个metric接受、1个geometry restoration接受。17份完整fine恰为4份新网baseline加13份callback扫描；第五个backend入口复用同p/q/fine报告，不额外算第18份。

已折入完成outer的6J/78方向块/62 value，与仍在当前backend的 **8J/104方向块/36 value** 分开保留。总共14份完整Jacobian、182块、98 value；第8份Jacobian之后的backend没有自然返回，任何未输出候选或内存数组都不恢复、不伪造。

原17 fine / 2159块 / 275403径向点、846038016个R604观察点、41份物理回溯行评估、13次减半、11份独立epigraph提升、30份无metric承诺的粗网评估、全部未闭/拒绝工作均在逐字FINAL和新ledger中。所有更早normal311、pending298/279、paid resume、物理epigraph、原方向检查、field/ODE/Hermite准备、失败重建与独立几何计算仍保留既有账；嵌套ledger的重叠计数不再加成独立耗时。

新field必要再生、实际新网入口、完整J、value line search、全部物理门/回溯/fine及失败尝试计入本次新时钟。旧方向检查、七点诊断、种子比较与24/48/96拟合不重放。

## 6. 几何与固定度量资格没有随q转移

4bd9的mean q[64:80]与q[96]均已改变，真实高度为 `.6986806496374112`。q80仍是tail首列。旧59a4单场连续reach证书不能仅凭同0d材料转给4bd9；若消费固定已证圆参考，仍须支付本候选自身完整δ/α/K。

原fine随带的R604观察不是连续上界，其当前mean参考也没有在这次范围重新认证。当前有限mean metric仍会改变；这里没有固定g下的任意精化、宏观相位族或精确存在声明。原p阶段误差门仍未过，不提前升级p，也不把本次正常续算写成达到README完成标准。

## 7. 原字节与本次冻结文件

原stdout7572735 B，SHA256 `69731f4c7ffa1529bc8bad76cf8a84949b94e1f58648fe1cfeccc0698949b7bd`；唯一FINAL522743 B，SHA256 `772b22e0ac7b2079041c36c09e34490cf602f3f49da814efe769ef8c1aa99ab2`。只把必要逐字FINAL置于后继输入，不提交完整stdout或新数据数组。

| 本次文件或stdin | 字节 | SHA256 |
|---|---:|---|
| `scripts/r582_physical_pending339_resume_20261127.py` | 12903 | `714bd52cb6b5267fd8b5fe43e9862eb17190648c27e33d35141695445e04e91c` |
| `computations/request-r582-physical-pending339-resume-20261127.json` | 548691 | `e6974a69e08c5bb69b8b37f057c9355bb90395bc3e992b9b2e6b4eb9b0bdeae9` |
| `.github/workflows/visible-r582-physical-pending339-resume-20261127.yml` | 6268 | `13edb698cb738ae8ff38a2b8314fbdd3021d2ac5156e40e7d0ec97df6bdfa148` |
| 必要完整stdin | 527897 | `c2ede476f04ec15408426786ce91f0da0652b6a39f70c6dfa79861c7a7983eb4` |

42条文件绑定、45个sparse路径、唯一原FINAL逐字身份、正确matrix lane `actual-4bd9-0d-pending339`、原common参数完全相同，均只作本地文本/AST/JSON/hash核对。

规则metadata采用root已实际pull/读过的public `922616ef53f3ca2297dfe531784c19081ee54813`、private `50c1c0039e5e9ff8c6979369a8059aad7efc3ddf`；发布前若root已有更新的实际已读号，只更新request规则metadata及本节对应字节身份，不动科学源或必要stdin。
