# 原源 C2 自由度扩充后的第一真实直接步与实际角谱

日期：2026-11-28。此条只谈原有限尾 source，不含另行构造的平滑 Q；原 g、参数与时间范围均未改变。前场为已实际返回的保 H2 cold 场，新增节点重数来自局部 C2 enrichment，不能把浮点 knot 与原源准确半径等同。

## 同一个实际场的精确暖转移与真步

h487 的 487 个唯一物理片保留；125 个既有新增节点各补到三重，quintic 自由径向列 486→736，角列仍 98，完整 unknowns 47,628→72,128。`6a65-m12-exact-radial-angular-warm-transfer.py` 实际 exit 0：准确 Boehm 插入 250 个结点，然后 binary64 存储。存储变化的原 target 一阶界 4.245003383302405e-19，二阶界 2.07851208263671e-13，均显式支付；没有把存盘后的浮点场称为绝对相等。

在准确转移场上，`2ecf-m12-h2-cached-direct-lm-v2.py --transfer-receipt ... --lambda-step 1e-13 --steps 1 --hessian-step-cap .05` 实际接受 alpha=1。原完整三 Gram 非线性残差、所有角向耦合与自由内部接口均保留；H2 正则仍仅作用于增量。

| 相同定义的观察 | 该步之前 | 该步之后 |
|---|---:|---:|
| 全部 G6/N384 训练峰 | 8.260458611849639e-10 | 6.388298380502648e-10 |
| G6/N384 训练能量 | 4.566061443149762e-21 | 3.421301152856882e-21 |
| 全部 G8/N768 独立峰 | 8.260458152801774e-10 | 8.057573884765639e-10 |
| G8/N768 独立能量 | 5.450641428716725e-21 | 4.306355743961051e-21 |
| 既有两微区 546 点/N768 峰 | 8.260458648889868e-10 | 6.737671149647871e-10 |
| 全部既有祖先独立观察 union 峰 | 8.260458152801774e-10 | 8.057573884765639e-10 |

训练与独立峰明显分离，必须同时报告。真实正则化法方程相对残差 2.552593252548093e-11；未正则化原法方程相对残差 .0014164901318653774。其余诊断：方向 H2 范数平方 2.6621158935656063e-9，二 jet 浮点增量筛选 .031032263160402238。不能把本步描述为原未正则化方程已收敛。

单线程实步含完整独立前后观察用时 333.827369123 秒，RSS high-water 970300 KiB。缓存 v2 的实际生产记录只含 N384/N768 两组，每组各阶首次返回均与原 evaluator 精确比对。实步、R226、旧全相位几何、R236 四阶段全部 exit 0；独立微区与祖先消费者也各实际 exit 0。

## 连续旧界尚未通过

同一新场的 R226 端点三重零 jets 全成立。旧全 source 几何消费 reach/D 下界 .018305231618758227，未过 .03；R236 连续度量三角界 3.234423210009066e-5，未过 1e-6。实际采样下降并没有令这些保守连续界自动成立。新的局部二 jet R249 与完整 source-cross-Gram 抵消应分别凭实际返回记录；本条不借它们预告通过。

## 残差角谱的实际横轴与有限含义

`2ecf-m12-actual-residual-angular-spectrum.py` 在本场训练峰、独立峰及两个邻近训练点取 N1536。其 FFT 横轴是 **基底的均匀 theta_j=2*pi*j/N**：原 `bvp.central_chart` 先取该 theta，再由 `glue.material_angle(central,theta)` 得真实非均匀 u(theta)、rho=J/a；`WholePosition`/`joint.background` 在真实 u(theta) 评估原源，`basis.angular` 在相同 theta 注入修正。不是把均匀 u 的谱误认作 theta 基底截断。

独立峰在前缀 q=1.9615931081854077、z=.7935966654864236。其完整 `(e,sqrt(2)f,g)` Gram 平方谱在频率 >96、>144、>192、>256 的占比分别为 .89658474555、.54976825955、.29712713145、.13656220746。尾训练峰 r=.51324536283310729734 的 >96 占比仅 .000217760108，说明两处残差形态不同。这里是实际有限采样诊断；Gram 误差模态并不与可独立校正的模态一一对应，未给出严格截断下界或必要性定理。

据此实际 M48/N768 同 g 角加密已另起；同时准备 G12/G14 的真实源查询及全部旧观察 union。不得只把 G6 训练下降当最终收敛。

## 实际 C2 观察器接口

`2ecf-m12-declared-basis-observer.py` 用既有已检 C2 basis adapter 消费完整 unit_knots，仍验证每个 saved basis/source hash，原微区精确半径、全部原源六 jets 与祖先点集合不动。对于暖场，旧 union 脚本的 before 把新场独立初始 field 与 extra 点的零修正 source 混合；新 wrapper 丢弃这条不一致的 before-union，仅报告同一 saved field 的 after-union，以及独立标明的 source-before-extra。表格前一列来自前一实际场完整 union，而非该混合量。

- `warm-transfer.json`：`5ed28def47e26698f0e311bff8c72363560eb14c6ae2f7482b49b1f104cd47bc`。
- `warm-transfer.json.field.npz`：`02a3b63fd9762e6e6616d3c6ce9a4a002a5e8efee8762e7a1f1af47fd557b2b7`。
- `result.json`：`4e296d02d152dd9c7d25eeed2ca233c26e840003812336083c386d61530f5de8`。
- `result.json.field.npz`：`201de8909dc707c7d91749d812585233d49120c076468e9f2aebe97271114aed`。
- `correction-bounds.json`：`c9da434c525316713c62c9d3e8f4381319673f9aabbb699c48b4898a5ed83350`。
- `geometry.json`：`ebe16520890d127af619be57a86f1ce500b8208b2cdbe7896e8ad545eca0145a`。
- `metric-budget.json`：`e892520c8682e47a668fb9a632e5faa2ca4f40b7b2fce5528d412cee851071b4`。
- `microspan-observer.json`：`ec5a221701a986e7b244e0cc28732c06498a5179d2e7570184f47f16cdb6f4d7`。
- `ancestor-observer-union.json`：`efe633266b993e70c1b9689d7f4e1127000480e3a47a4ddfda27e9893726946a`。
- `angular-spectrum.json`：`95dc6d1889a3e656a222c20cfcf8f040ce6deadc1989f3ac1a37758dc02aae0a`。
- `execution.json`：`f167d721d2469388cd996ec962133def6f1ca5de3aa4ec194d1a106de0304d69`。
- 源码 `2ecf-m12-declared-basis-observer.py`：`21d05c8945a13dd76895b361c6eb0397035a8fafe06dc5a259e829b7af42302d`。
- 源码 `2ecf-m12-actual-residual-angular-spectrum.py`：`347954bccd7e121a8ac60476602729028015a04699e82b730abc6e5d708f52ee`。

大数组、原 field 与逐点谱保留本地 scratch，不进 Git。此条未宣告 README 任一未闭合完成门槛已经满足。
