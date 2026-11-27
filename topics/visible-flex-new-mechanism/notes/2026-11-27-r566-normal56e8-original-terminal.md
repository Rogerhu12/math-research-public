# B030 normal56e8 原终态：d191 真接受与最后238个未闭 bracket

2026-11-27，会话 `Astra-new-mechanism-1f4a61a4-20261127`。
可信度：唯一原 Actions 完整日志的数值观察；没有新增本地科学计算。

真实保留81q从56e8的 eta `.22244446600107332` 进至
**`.21585219167801023`**，本段15次 metric 接受、0次 restoration。
它仍是 B030 原静态设计的有限资格，不是固定 g 收敛、连续角证书或 README 完成。

## 1. 原运行与逐字收据

- run [45909082053](https://github.com/Rogerhu12/math-research-public/actions/runs/45909082053)，
  job `140212809662`；唯一 source `5cd6055b7595090b1f0f82a0b270788cc1c9ee53`。
- 科学源 `scripts/r566_normal56e8_physical_resume_20261127.py`，53694 B，SHA-256
  `def9207558641dc38f6bef4a9e8058673b13ea27b225428000355e6d66425f9d`。
- request `computations/request-r566-normal56e8-resume-20261127.json`，319274 B，SHA-256
  `25e1272a92303d5cc00c250b2a977ef74adfdc21181678781c85a7dae56fdd26`。
- lane `rounded-core-B030-normal56e8`，原 stdin 278477 B，SHA-256
  `d7cef97eb7fb9f44b7c7819f16341fa55f869bf1cf08cbd22a788eec87cc6cbb`。
- public 实际 pull 到上述 source，根及本题 README diff 均为空；private 实际 pull 到
  `ebd31244c69fb695b007ec72eee5183f5edda493`，根 README 匹配、QUEUE 为本会话。
- job `23:08:06–23:48:08 UTC`，Actions `success`；子进程
  `23:08:33.913975–23:48:05.299929 UTC`，returncode 0。
- 新科学 **2370.339514432 秒**，终态
  `cooperative_clock_or_unresolved_localizer_checkpoint`，outer21 / metric。
- 原 stdout **20715698 B**，SHA-256
  `6a9eea4f5e95cc092191985480afa0f0652cf50b47835b27ed9c78f0010b9c88`。
- 唯一原 `WORKING_ROWS_FINAL` JSON **471344 B**，SHA-256
  `4814ae42508b64b877786f9a40b12ffc037aa4bfde3ae5c115c16ab3a6b93c95`。
- 唯一原 `THETA_PEAK_LOCALIZER_PARTIAL` JSON **343899 B**，SHA-256
  `2703398aed83e46a3570d6b5712368840eeae734d235b2d3285f4c32ce6c9218`。

日志只在自然结束后下载一次。两个 JSON 是原行的逐字截取，未重序列化冒充原输出。
全部可重算日志留在原 Actions，不入库。

## 2. 新1390资格确已支付，终态1580与保留资格相同

本段按声明只为原56e8新付了其已经采用的1390 fine，而没有重放旧1388资格或旧1519队列。
原新网 identity 为 `345b946a64a98732feaa0936c97f79cacb470908c6cd6efeeb60eaf03aab6ec3`；
新1389个候选全部定位，9937次 objective，52.425141414秒；新网真实 eta
`.222444466001073`，工作 margin 最大违反 `1.2358994036509863e-12` 在原容差内。
这次同q资格更新没有计成一次 metric 接受。

终态真正保留81q的 SHA-256 为
`d1914e0ff7baa35be99012afdd7af12ed3dbfe3cd876298762b9cedd2aa2e3a8`。
它完整通过 **1580×3072** fine 和 **1898/1898** 原枚举角峰；定位13102次 objective、
75.38824316699993秒。完整网格 eta 为 `.21585205595200493`，加入峰以后真实接受值
是 `.21585219167801023`，峰在 `s=.525, theta=.31937579449122877`。
物理 violation 和原工作 margin 最大违反均为0。

| 实际数组 / 库 | 长度 | binary64 SHA-256 |
|---|---:|---|
| 当前 coarse 径向 | 789 | `8099c2d47e03f2d4be3a75dc1db596b2f729b2d54e4cb33e21c09d2398856473` |
| 当前永久 fine | 1580 | `ace4e97f3167657401810ae69d4c17422c324c4e0c09b9fd5acd347c09f0ff5b` |
| 保留q已合格 fine | 1580 | 与当前永久fine逐项相同 |

当前实际 physical orbit **1763**、working行 **720**、FFT **1536**；pending分别为
**11** 个 physical orbit与 **15** 条 working proposal。全部原坐标均保留。
真实和拟定下一 trust 都是 `.3003387451171875`；最后 outer 尚未完成 trust决策。
保留q的工作 epigraph 是 `.21585220167801022`，原完整 scalar rows 为 **2805194**。

| 保留q完整有限观察 | 值 |
|---|---:|
| 最大曲率 | `16.374273294087242` |
| 曲率位置 | `s=.7593749999999999`, `theta=1.5707963267948966` |
| mean-E最小 / 最大 | `.997850505674843` / `3.3269673871570498` |
| det最小 | `.8952966018696698` |
| 球半径最大 | `1.011493873091814` |
| abs(y)最大 | `.3926035037046724` |
| z最小 | `.02` |

当前fine既已完整合格，下一续算不得为了进入新算法再重放一次同q baseline。
这不替以后实际改变的网格、q或峰队列授格。

## 3. 全部15次真实接受

以下原 fraction 全为1；没有把 e 抬升记作实际改善。q栏为原全SHA的前12位。
原日志记录每个完整q；所有接受均独立通过全 coarse、fine、峰、nested和原物理门。

| outer | q SHA前缀 | 真实完整 eta |
|---:|---|---:|
| 2 | `fe560a6c66a2` | `.22160151738421052` |
| 3 | `99833fbd810d` | `.2210819250729271` |
| 4 | `a95e58e4d8c2` | `.2205882485461421` |
| 5 | `cac38d50389f` | `.22013043320540632` |
| 7 | `3a0529734065` | `.2196576361744909` |
| 8 | `ae57b76761bc` | `.2192361723965889` |
| 10 | `0d7fd62f3dc7` | `.21880463623277352` |
| 11 | `3b1ac53ee2d6` | `.21839617658485683` |
| 13 | `0fa22294eee0` | `.2179901644510307` |
| 14 | `690ded712b25` | `.21760861767564177` |
| 15 | `4458550cb1aa` | `.21722314035597223` |
| 16 | `4eca9ff98189` | `.21689117341692898` |
| 17 | `2699fb123b4c` | `.21648427610853213` |
| 19 | `f540dfd9641f` | `.21619585567452818` |
| 20 | `d1914e0ff7ba` | `.21585219167801023` |

outer0、1、18得到完整合格但没有严格改善的候选；其网格eta分别是
`.228858461135937`, `.22450872751941744`, `.21668457940404331`，正确没有接受。
其余三个完整 fine 拒绝是真实物理 margin：outer6 strip
`1.7553506659242352e-7`；outer9 ball `1.34496856396462e-6`；outer12 strip
`4.4465329195574055e-8`。没有仅靠 epigraph 抬升越过这些物理门。

本段22次 callback / 22次working trial均fraction1，0次working recovery / 0次耗尽。
working与coarse各22次e抬升、fine17次抬升、61次原working recheck全部计费；raw数组保持原样。

## 4. 最后298f候选：1678已付、238未闭，仍没有接受

原 raw q 与独立物理评估副本相同，SHA-256为
`298f9fb92a46f64c7a96851127e22531ba6e1fd849fa4de5f402ae2865517f39`。
raw e `.21549901134171212`，独立 working lift
`3.014984887805827e-6`、coarse lift `1.0331481042125112e-5` 后，评估e为
`.21551235780764205`。原working/coarse及box均通过。

它已完成同一 **1580×3072** full fine，网格eta `.21551677238651737`；三项 nested差
分别 `1.9984014443252818e-15`, `7.551115731750784e-16`, `8.809497131778697e-14`。
原共有1916个 bracket，完成 **1678** 个，剩余 **238** 个。
已付11342次定位objective、59.286542224000186秒；四批开始、三批完整结束。
oracle identity为 `def5c2dc3a82376fb8fa782acff05ce52f2111272d6844f27dc0222e2a3e90a2`。

已经支付的这1678峰里，metric-minus已到 `.2155184402678356`，高于网格值；
ball / strip工作margin违反已分别为 `2.9141946422586024e-7` 和
`6.816510597076539e-7`，所以它已经不具备原物理接受资格。
最后238个 bracket 仍是原范围未闭工作，下一段保持同q / 同fine / 同oracle只完成它们，
与1678个真实原峰合并并保留新的工作证据；不能把最后候选或较小raw e代替d191。

## 5. 再次出现的真实曲率学习瓶颈

原22条backend-start、22个完整J、21条outer-complete逐事件对应。
21次实际结束原因为 **18次 epigraph后新峰交换 + 3次失败fine峰交换**；
最后第22次由上述原部分队列的时钟中断，0次自然backend返回。
所有完整J共 **602.5985322480003秒**，方向块1464，未退休active计数为null。

结合已登记官方MODE0 / callback / MODEM1控制流，这一段也都在能形成第一次新native
BFGS secant之前结束。原日志仍没有 H 或 QP乘子可恢复。
下一新native范围只从 I开始，并在随后真实已付J/QP上学习，不追造旧H。
旧曲率实现与新坐标接口均不会反写这个已自然完成的source。

## 6. 本段全部费用与继承

| 新费用 | 原终态值 |
|---|---:|
| 科学秒 | `2370.339514432` |
| metric / restoration接受 | `15 / 0` |
| outer开始 / 完成 / native自然返回 | `22 / 21 / 0` |
| working value keys / 完整J / 方向块 | `105 / 22 / 1464` |
| J秒 | `602.5985322480003` |
| complete coarse / fine / localization | `82 / 23 / 22` |
| 新网baseline尝试 / 完成 / 合格 | `1 / 1 / 1` |
| 定位候选 / 完成 / 剩余 | `35267 / 35029 / 238` |
| 定位objective | `238236` |
| working / physical交换 | `21 / 19` |
| Oracle构造 / FFT准备 | `290 / 2697` |
| point evaluations | `243178` |
| point values / parameter directions | `1984356 / 3741552` |
| exact-core点 / nonuniform summed点 | `1417546 / 1523327` |
| point_sets / subset / primitive Fourier fields | `238562 / 4460 / 24273` |
| Oracle构造秒 / prepare秒 | `63.00308645799922` / `654.2317597279994` |
| point秒 / point-set秒 | `1409.3732756239942` / `103.05379754500882` |
| 旧diagnostic / 新restriction observation | `0 / 0` |

各子时间包含于原科学elapsed，不额外相加制造总成本。
源已知链下界 `14729.212126063` 秒仍原样保留，加本段后为
`17099.551640495` 秒；更早外部截断 / 未输出费用仍未知，不能写成精确总成本。
下一输入为准确d191、原298f部分候选、1678个已付峰与完整238剩余队列、
1580永久fine及两类pending库。新算法不得更换这些物理来源。
