# R141 补篇：实际完成原 D 参考边界提升与全部 193 观察

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**已证明（公共有向计算）：** 同一固定 WVC 低参考 $D,S$、真正 root、原 $p_0=13/80$ 和 $\Theta$ 下，weighted right97 与 joint boundary193 两个完整边界提升的 body、root97、outer96、joint atoms193及complete范数上界均已实际保存。计算是 public run **44745017016/1**，两目标和十条完整球全部成功。这里仍只证明原参考提升；没有把它登记为实际低逆或物理外边界逆。

## 1. 实际运行和完整身份

本次 event commit为 `a06daaeb27241a930fb4ab793f51e4d8d48742ed`；实际数值 checkout为 `4c3342e2ae08fc8ff722e8f194471c005e7023d7`。完整输入、source、参数与公开结果是：

| 对象 | bytes | SHA-256 |
|---|---:|---|
| [recovery manifest](../notes/2026-11-20-reference-boundary-lifts-thread-recovery-inputs.json) | 72957 | `38ff0e8f5f3ca03a752a5836ec43baa72a31aefcf29a2d3e4421d0d399323f6d` |
| [whole scientific conclusion](../notes/reference_boundary_lifts_ci/run-44745017016-1/actual-scientific-conclusion.json) | 55295 | `087ebd3a222c6ef7be8b3ad2e427e272b2bb3f5b611c5acdcef4e03dd1fd2fdd` |
| [whole execution](../notes/reference_boundary_lifts_ci/run-44745017016-1/execution.json) | 58602 | `827fb78a31aceb6313cff5abd1ec1431dede6af06df959b2d43d83b48197e8b6` |
| [mathematical source](../scripts/fourfold_codazzi_reference_boundary_lift_math.py) | 11238 | `ffb9185a9c2d97df7a04b7bbb2016c3365378be2be14589d53574cd3ae32a588` |
| [public owner](../scripts/fourfold_codazzi_reference_boundary_lift_owner.py) | 27516 | `4f585a3bd252fd827329e1bd84647be3926a9c258b5e4e0d884be5be2d860d95` |
| [unchanged shared worker](../scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py) | 40772 | `98ef3773eab06178df086c5dcf551103c7cd3e00a5eca1c73cbfee089af84b1c` |

固定 runtime是 Python3.12.14、python-flint0.9.0、320bits，三个线程环境均为1。科学结果记录数学时间147.80307273秒；实际 child returncode为0，未超时，`complete=true`、`proved=true`、`failure=null`。

原全153 reference definitions、96 low profiles及155 complete Gram panels全部完成；每模每panel按16 whole subboxes包围。原 actual centre/family packets、$G_f/G_H$ action、实际低逆、旧五源率、旧完成目标和原 small-$K$50图的调用计数均为0。没有将已成结果重新当成新目标。

## 2. 参数、恢复和记录的完整性

运行保留同一 original reference chain
`6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac`
和 selected-diagonal chain
`b19d7e319a9ea4e49909e12b1dfe71ddc23adf5a273708288b3fe6b0cc3af8d2`，两条各153项。`reference_identity` 与已成 GH5 完整对象逐项相同；原24480 fine cells、$S$、原有限 $\rho^2$ 规则和真正 root保持原身份，本运行没有重算 finite-$\rho$ 目标。

结果具有完整39字段和25个依序通过的门；实际与 execution的82 current receipts逐项等于manifest。对82个当前文件的完整bytes、SHA和Git blob，以及全部Python AST，作了只读核对。execution中29条AST receipts也逐项对应当前文件。

21个完整历史恢复receipt（原19个加germ/budget两份）逐项核对全部manifest字段及实际恢复标志；原native25507783B的整连接SHA仍为
`1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c`。
scientific引用的是同一个execution内的完整恢复对象，不是截尾清单。其canonical整对象15033B、SHA
`8213b004a48508c580440cb7a38239d796c7afc9eece83bbd3f5a02e5b2d7ed4`，以及原WVC恢复对象13771B、SHA
`4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac`
均核对一致。本次后验审读没有重新恢复或计算这些旧科学数据。

执行的4条完整README pull receipts及其累积hash链一致，两个README差异均为空。已成 L、centre exclusion、GH5、GH4和两完整高图均保留 whole-object引用。原29同对象记录与GH5中的完整副本相同。

## 3. 完整十条已存有向球

下表逐字抄录完整scientific records。每条球包含计算中原directed upper；这里的数值资格是保存球的**上端点**，并非括号内展示中心。后继应从整个原JSON球读取，再取有向upper，不能从本表截取短小数。

| 输入空间 | 观察 | whole saved ball |
|---|---|---|
| weighted right 97 | body | `[6.59351549433281182016110108868683363528362452380847349363977448057479838743 +/- 1.65e-75]` |
| weighted right 97 | root 97 | `[1.00000013364478052685748595623455923653744837462515005394555619166629337171 +/- 4.12e-75]` |
| weighted right 97 | outer 96 | `[2.98867553141391177674726056850392430239799728108985659198075658864560084439 +/- 4.60e-75]` |
| weighted right 97 | joint atoms 193 | `[2.98867547158341688477720680604210525742621341165178167167375106013021446605 +/- 4.33e-75]` |
| weighted right 97 | body + joint atoms | `[7.23521750141214512638154697368534854760006952342164604529097149480006298455 +/- 3.07e-75]` |
| joint boundary 193 | body | `[6.59351549631729102033612814879660952570280195206699003618692904007555178213 +/- 2.60e-75]` |
| joint boundary 193 | root 97 | `[1.00000005233446951359647034882120127922018031992266249565864065898739490037 +/- 1.51e-75]` |
| joint boundary 193 | outer 96 | `[2.98867576824294230349482838428132168851815925425633387252751570074453415184 +/- 1.15e-75]` |
| joint boundary 193 | joint atoms 193 | `[2.98867547158341688477720680604210525742621341166214178691666182975053725449 +/- 4.63e-75]` |
| joint boundary 193 | body + joint atoms | `[7.23521749884064823875835764036920467413606769663763986312299763365289552727 +/- 3.51e-75]` |

各输出上界是独立合法的包围。较大的输出空间或输入空间，其某个独立计算上界不必大于另一空间另算的较松上界；这不表示实际算子范数违背子空间单调性。后继不从这些上界之间的数值差推断下界或范数相等。

## 4. 数学结论的准确范围

[参考边界提升与物理外块补篇](R141-supplement-reference-boundary-lifts-and-physical-outer-block-gate.md) 的 B4–B15给出本计算的完整公式。right97输入是

$$
r=(\Theta\lambda,\mu),\qquad
\lambda=x_L^o(R)+p_0x_L^e(R),\quad p_0=13/80,
$$

其中 $\mu$ 是原 moving-$\phi$ 独立 even mean。joint193输入另加原raw root-even96数据，采用Euclidean直和范数；没有在同一个模态上把两个lift输出宣布为正交。

输出是普通 $dr$ 下的 $S$-body、原root odd96加mean共97行、$\Theta$-weighted outer-even96行，以及全部193 atoms的联合范数。原mean body是常数lift乘真实 $q$，root mean观察为1，outer96不另添一个mean行。它不是physical-density mean或physical-$\theta$读出的免费替代。

每模的两列实际 signed body/atom Gram先组合，整格积分和同模cross项完整保留；joint输入的2×2上界按非负比较矩阵自身的最大特征值处理。所有mode、whole boxes、真长度和两端观察都已通过本次完整计算。因此十条球给出所声明两种参考提升的完整范数上界。

未来若同对象R141 low193真正逆和四个source receiver已实际成功，才可用 B4–B21将这些reference lifts通过 $T_L$ 与完整真实高反馈送入实际物理外97+96块。本次不提供那些尚未完成的source bounds；浮点endpoint诊断也不能替代它们。

## 5. 启动失败保留与后续限制

前一次 run44742799448/1 在 `declared thread settings` 门失败：19个准入门已过，reference/profile/Gram/target/record均为0，数学时间0。该完整失败的actual和execution继续作为本次82输入中的两项保留；没有覆盖其consumed marker。恢复只在原workflow补三个显式线程环境并换独立v2 marker，原79输入、owner、math、参数、25门39字段和shared worker都未改。故本次是这两个尚未完成科学目标的首次完整执行。

实际输出明确保留以下false scope：actual low boundary lift、actual low-high inverse、physical outer rows、原finite-$\rho$桥、原七端口、两条WPN RHS及课题完成标准。这里没有把参考 $D$ 当成实际 $A_{L,c}$，也没有把真实 $G_H$ 替换为旧WJK有限 $F$。

本次两个目标与十条球现作为完整只读成功冻结，后继只消费上述whole结果；不为显示、改字段或另起包装而重算。
