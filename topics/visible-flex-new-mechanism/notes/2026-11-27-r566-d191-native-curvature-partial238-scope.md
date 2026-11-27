# B030 d191：只续原238个 bracket，再实际消费 native 曲率

2026-11-27，会话 `Astra-new-mechanism-1f4a61a4-20261127`。
可信度：新声明范围、纯源码及纸面消费协议；本地没有执行优化、编译、ODE、FFT或科学探针。

## 1. 实际问题与本次改变

原 normal56e8 的真实终态是81q `d1914e0ff7ba…`，完整接受 eta
`.21585219167801023`；22次 backend均只有一份完整J，随后21次实际行/峰交换，
最后一次在原定位队列的时钟内退出。已支付602.5985322480003秒J却来不及执行第一次
native MODEM1 BFGS更新。这是本次接入已审 native-H 实现的直接输入依据。

本次先把**同原298f候选、同1580 fine、同oracle的最后238个 bracket**做完，
保留1678个原已付峰。随后用完整原 B030 working/coarse/fine/实际峰/nested/物理门
继续真实下降；唯一算法改动是在真正的新SLSQP启动时，允许已审接口给一个近似正定初始H。
不会把前段没有输出的H或乘子补造出来。初始H是单位阵。

已发实现和完整算法证明见
[native初始曲率实现说明](2026-11-27-r566-native-initial-curvature-and-true-secant-implementation.md)，
source `6ba735d841e525bc27183c1d10c776547fb7925d`；其patch、builder和helper均不改。
原终态收据见
[normal56e8原日志收据](2026-11-27-r566-normal56e8-original-terminal.md)。

## 2. 准确原输入及不重复的工作

原 run [45909082053](https://github.com/Rogerhu12/math-research-public/actions/runs/45909082053)，
job `140212809662`，source和实际runtime pull均为
`5cd6055b7595090b1f0f82a0b270788cc1c9ee53`。
唯一原stdout 20715698 B，SHA-256
`6a9eea4f5e95cc092191985480afa0f0652cf50b47835b27ed9c78f0010b9c88`。
唯一原FINAL 471344 B，SHA-256
`4814ae42508b64b877786f9a40b12ffc037aa4bfde3ae5c115c16ab3a6b93c95`。
唯一原PARTIAL 343899 B，SHA-256
`2703398aed83e46a3570d6b5712368840eeae734d235b2d3285f4c32ce6c9218`。
日志只在自然结束后下载一次，未作旧诊断回放。

| 必要原状态 | 实际值 |
|---|---|
| 真保留81q | `d1914e0ff7baa35be99012afdd7af12ed3dbfe3cd876298762b9cedd2aa2e3a8` |
| 真接受eta / 工作e | `.21585219167801023` / `.21585220167801022` |
| 当前coarse | 789，SHA `8099c2d47e03f2d4be3a75dc1db596b2f729b2d54e4cb33e21c09d2398856473` |
| 当前与保留资格fine | 同一1580数组，SHA `ace4e97f3167657401810ae69d4c17422c324c4e0c09b9fd5acd347c09f0ff5b` |
| 实际 physical / working 库 | 1763 / 720 |
| 原未采用 physical / working proposals | 11 / 15 |
| FFT / fine角数 | 1536 / 3072 |
| 实际/拟定trust | `.3003387451171875`，上一trust决策仍未完成 |
| 原完整scalar rows | 2805194 |

这份d191在当前1580网已完整合格，不再付一次相同q baseline。末端pending库随后实际
采用时，仍要按原outer逻辑支付新的完整coarse行，任何新候选仍完整支付其fine/峰等门。
所有旧fine浮点坐标永久并入，不因新coarse的中点变动而丢失。

未闭候选是 `298f9fb92a46f64c7a96851127e22531ba6e1fd849fa4de5f402ae2865517f39`。
其完整coarse/fine/nested已付；fine eta `.21551677238651737`。原1916个bracket中
1678已做、238未做，原已付11342次objective和59.286542224000186秒。
原oracle identity为
`def5c2dc3a82376fb8fa782acff05ce52f2111272d6844f27dc0222e2a3e90a2`。
1678个峰的canonical JSON SHA为
`6302e042213dbdc8854ce2d9ab5431aa1050ac94ca86010f447a641e405f414c`，
其逐field最大值与原FINAL完全一致。

这些已付峰中ball/strip工作margin已经分别失败
`2.9141946422586024e-7` / `6.816510597076539e-7`。
所以298f不能仅凭较低metric被接受。新范围仍完成原队列并保全其全部新工作证据，
不以已知失败为由把238个原未闭输入静默丢弃。原saved-queue helper照常检查同q、
同oracle、同fine数组以及每个bracket的原坐标；只在剩余238项调用objective。
必要重建原oracle/FFT状态的费用完整计入新clock；旧1678峰不重定位。

## 3. native初始化的精确消费位置

新driver从已发normal56e8复制原outer/callback数学，并把入口1390 baseline替成
已发partial391的原saved-bracket消费块。原callback、全部约束fun/jac、原物理boxes、
trust规则、恢复phase、epigraph独立抬升和raw/best两轨均保留。

在真实科学clock已经开始、原输入已恢复后，创建一次 `TrueSecantSLSQP`，
跨当前run内的outer保留该对象。原 `minimize(...)` 的全部参数直接转交其
`minimize(...)`；任何物理接受仍完全由未改的原callback决定。

初次构建只发生在第一个真实backend，和所有优化工作共用原deadline。
从官方SciPy 1.17.0精确C/h/nnls源码生成已审patch，在实际wheel的LP64 OpenBLAS上构建；
source fetch、patch、compiler、import、失败尝试及版本/符号核对全部由冻结builder计费。
不用一个额外问题试跑native，不重算旧科学数据来“验证”后端。

wrapper在其原SLSQP第一次native调用时已经支付当前完整J；新接口只读这同一C及g。
后续交换若函数语义相同、旧非零乘子所有行均存在，冻结原实际QP乘子，
用新C对应原行求secant，再作已审Powell阻尼和有界正定化。
缺任一原非零乘子行就不更新，已有H只作启发式初值；phase/语义改变则回到I。
不重新求一个旧J、不补一个新数值差分、不截断小非零乘子。

语义绑定包含完整原field、geometry、orbit、row构造源码，实际par/geo、phase、FFT及参数顺序；
变量q不放进“固定行函数”的签名。当前working子集变动允许按原行key匹配，
新加入的行仍在新QP中使用真实值和真实导数。
MODEM1已由原native消费的secant立即清除，不能外部再更新一次。

该H不构成数学Hessian证书。内部RESET_BFGS仍原样重置I；新接口不改QP目标、
不可行增广、线搜索、接受容差、物理门或全场定义。

## 4. 必要状态与费用边界

每次原snapshot/FINAL增加当前真实曲率checkpoint：82维对应3403个packed LDL值、
实际QP anchor和固定乘子梯度、全部非零原行乘子与语义指纹、失败/重置/更新计数。
不保存完整J、巨大native workspace、临时C源或编译二进制。

helper内checkpoint上限524288 B；若全pending超上限，就明确整体舍弃pending，
仍保H。不能只截断小乘子以伪称完整secant。没有当前真实H时写null，下一段从I开始。
这次首次输入没有任何旧H/乘子。新必要输入的完整FINAL与原1678峰已足够继续，
旧原log/大中间数据不入库。

原完整成本账逐层保留，包括本段原22份J/1464块/238236个定位objective及所有oracle操作。
原已知科学链下界为 `17099.551640495` 秒，较早外部截断费用仍未知。
本次native builder/seed LA/native调用和原优化子费用均包含于同一新elapsed，
不会把重叠子时间再加一遍制造总成本。

范围保持单job、maximum_seconds=2400、final_reserve_seconds=30；原其他数值参数不变。
自然时钟终态、原容量门、原异常、未闭队列或不合格候选都如实记录，不称优化完成。
其后继续消费真实终态；此新范围不授连续范数、固定g族或课题README完成。

## 5. 冻结字节与Actions入口

| 文件/输入 | 字节 | SHA-256 |
|---|---:|---|
| `scripts/r566_native_d191_partial238_20261127.py` | 60295 | `23a5e6df8de9ec8bafa60e8e7527038b2961fe03fe8e2b293f07232a9b7c9fbf` |
| `.github/workflows/visible-r566-native-d191-partial238-20261127.yml` | 5877 | `ca8956203de255d4d6912e13dd422f8c8a65aa822733396a02eb2a439a9da189` |
| `computations/request-r566-native-d191-partial238-20261127.json` | 868286 | `3030d05ad50554b023b49b16b96e1bb665eab09e2c5e7cf84da3b038c05c6e4e` |
| 新stdin必要状态 | 768665 | `85e68500a0f3f23cac49d3d92fbc4b270442f3edbfb332478ee2792000d75e11` |

request为 `computations/request-r566-native-d191-partial238-20261127.json`，
单lane `rounded-core-B030-d191-native-partial238`。40条文件绑定、原FINAL逐字和1678峰
canonical SHA已作本地纯文本/JSON/hash核对，driver只作AST解析，未科学执行。
request不足1 MB，不切块、不存可重算的整份原日志。

规则metadata采用root在00:01 UTC实际pull并读过的public
`7ad798390451dda805da35f99eb1c232d4a935a3`、private
`724f5769d39c1f05826ed6c36792a5bb66da6aa0`；根及课题README差异均为空。
新工作流由新request的push触发，复用同B030并发组，不另dispatch、不与其自身旧scope并跑。
