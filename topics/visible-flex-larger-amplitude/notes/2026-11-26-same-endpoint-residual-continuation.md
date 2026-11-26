# 同一端点方程的残差延拓：完整未运行候选

日期：2026-11-26。状态：**条件代数已逐式说明；完整候选源码与参数已备，尚无科学运行。** 本文不把辅助求根参数当作题目的弯曲参数t，不改变固定标量度量，不增加根坐标半径，不把有限阶段的成功当作存在/唯一性证书。

本稿准备时固定moment-Q首轮尚未返回。现在其实际19–20初根失败及实际23支撑必要式严格通过均已登记；root据此选用本完整后继，原历史不改。当前公开积分方向继续运行；本候选排在其后并要求读取它的完整地点报告，详见§8。

## 1. 固定的问题与改变的部分

固定原完整自由点x、材料角phi、reference0f042、固定度量6ffc、18个准确字面Q参数及definition05dc。完整端点方程为

$$
C(z;x,\phi)
=\Gamma_x(\phi)-P_x(\phi)
+\int_0^S \exp([W(s,\phi)z]_\times)T_y(s,\phi)\,ds=0.
$$

Q的全部参数、fixed-chart延拓、两个准确wide支撑、全部core/omega/H自由量、径向积分规则、原六jet、原implicit J/J转置和真实几何筛，均来自完整固定Q入口44ac/ff500。新源独立命名、完整复制，原源不改。只有数值根策略改为下述残差延拓；根坐标仍必须处于同一个开球 $|z|<r$，首候选明确 $r=0.75$。

定义 $c_0=C(0;x,\phi)$，引入辅助参数 $\lambda\in[0,1]$：

$$
H(z,\lambda;x,\phi)=C(z;x,\phi)-(1-\lambda)c_0.
$$

在固定x、phi下，$H(0,0)=0$，而 $H(z,1)=C(z)$。因此辅助过程有明确起点，最终必须回到原始闭合方程。它既不把最终目标缩小成 $(1-\lambda)c_0$，也不改变固定g。$\lambda<1$ 时，辅助切向积分一般仍有非零端点缺陷；这些阶段不被作为闭合场、QP候选场或物理弯曲族成员返回。

## 2. 条件导数与同阶段下降式

假定真实C在某邻域光滑且 $A=C_z$ 可逆。对某条准确的 $H=0$ 局部分支求导得到

$$
A\,\frac{dz}{d\lambda}+c_0=0,
\qquad
\frac{dz}{d\lambda}=-A^{-1}c_0.
$$

这只是局部隐函数公式，不能推出分支会留在0.75球内或延续到1。代码在每个已接受数值阶段读取完整Cz，用该式作可选预测；预测非有限、线性解失败或预测点不在原球内时，校正从上一接受的z开始。它不通过扩大球容纳预测点。

在固定 $\lambda_*$ 的校正阶段，残差为
$r=H(z,\lambda_*)$，$D_zH=C_z=A$。准确Newton方向 $d=-A^{-1}r$ 满足

$$
D\!\left(\tfrac12|H|^2\right)[d]=r^TAd=-|r|^2.
$$

若 $r\ne0$，同时 $D|H|[d]=-|H|$。故在准确可逆/光滑/内点条件下，充分小的正alpha满足与原根法相同形式的残差范数Armijo条件

$$
|H(z+\alpha d,\lambda_*)|
<(1-\sigma\alpha)|H(z,\lambda_*)|,
\qquad |z+\alpha d|<r.
$$

源实际仍只进行原18次有限回溯和有限精度C/Cz评价。有限预算失败、真实工作雅可比不可用、浮点非有限，都作为相应数值失败记录；不由这段条件代数推断不存在根，亦不保证这18次中一定有成功alpha。

## 3. 完整数值策略与回退

每个实际角分别持有一对已接受的数值状态 $(z_a,\lambda_a)$；整个角块保持完整C/Cz评价，实际调用次数按整个块记录，未把已完成角从成本中省略。

初始设 $z_a=0,\lambda_a=0$。如果原始 $C(0)$ 已满足原容差，则该角直接记 $\lambda_a=1$，并仍在最终重新读取原C及最终Cz。否则按下列完整步骤推进：

1. 取 $\lambda_*=\min(1,\lambda_a+h)$，记录实际增量 $\delta=\lambda_*-\lambda_a$。所有地址保留原literal phi.hex，不把子批次索引冒作全角坐标。
2. 在原完整Cz上作可选切向预测。合法预测用于本阶段的起点；否则保留 $z_a$ 为起点。
3. 固定这次的 $c_0,\lambda_*$，用完整C/Cz和原Newton/Armijo/开球条件校正H。每一次被尝试的校正都有真实残差读取；不可用的旋转点不被拿去强行求值。
4. 阶段只有在其返回z的完整H残差重新通过原容差且仍在原开球内时才接受。成功则更新 $(z_a,\lambda_a)$；失败则恢复到阶段开始前的同一对已接受状态，丢弃该阶段所有中间z。
5. 成功后的下一步长为实际增量乘growth；失败后的下一步长为实际增量乘shrink。特别是接近1时使用实际delta，不对一个已被1截断的旧大步长反复缩减、重复尝试同一个目标lambda。
6. 每角最多64次阶段尝试，最小步长为1/65536。耗尽时如实返回最后已接受lambda、原C残差、原球内控制范数和所有阶段失败原因；没有达到1的状态不返回为场。

首候选的步长参数为 initial_step=0.25、minimum_step=1/65536、growth=1.5、shrink=0.5、maximum_stage_attempts=64、predictor=true。这些是明确的数值政策，未声称其为最优值或其实际加速已得到证明。

阶段校正保留原参数：容差2e-12、最多24次Newton、18次回溯、Armijo常数1e-4、开球半径0.75。这个新策略总预算可能超过一次旧Newton预算；源码和读数明确记录全部实际阶段及其成本，没有把多阶段过程伪称原24次预算内的改进。

## 4. 只在原方程上返回场及导数

所有角必须准确达到数值标签 $\lambda=1$。然后代码不带任何辅助offset重新读取原始C，检查实际残差容差与原开球，再读取最终原Cz及其数值奇异值诊断。只有这一步通过，才把根交给原后续流程。即使每一级H都曾达到容差，最终原C不通过也返回失败。

原 _finish_jets、_constraints、_jet_jacobian 和 _implicit_jet_value 正文保持AST相同。最终角向根导数仍满足原C的方程：

$$
C_z z_\phi+C_\phi=0,
$$

$$
C_z z_{\phi\phi}
+C_{\phi\phi}
+2C_{\phi z}z_\phi
+C_{zz}[z_\phi,z_\phi]=0.
$$

实现继续使用原完整6×6或9×9下三角jet约束系统及value-preserving implicit surrogate，在当前完整自由x上求一阶J/J转置。延拓、预测和所有Newton迭代保持detach；不对它们反向传播，也不把中间lambda的 $D_xc_0$ 支路错误带入最终方程。最终lambda=1时该offset系数准确为零，而所有C自身的完整core/omega/H与材料图依赖保留。

这保证的是算法接口和条件隐式公式一致。它不把有限容差数值根提升为准确隐函数；最终Cz的工作奇异值仍无积分/舍入区间，跨角唯一分支与连续误差责任仍未支付。

## 5. 完整新来源及实际身份规则

新operator直接从完整44ac固定Q源派生。37个原方法保持AST相同，包含全部旋转、W、core/cap、C、完整六jet、原J/J转置、输入/输出和固定场缓存。_get_roots仅把已经存在的literal角字传入新根诊断；原缓存与角jet升级主体不变。_solve_roots、初始化、failure/metadata以及新增延拓方法明确属于新源。

新geometry仅换完整source/schema guard，原物理几何和所有选行/全点筛正文不变。新driver从内部 def save_report(): 到文件末尾与原ff500逐字相同；QP、公共slack Phase I、原全自由坐标及母范数、全旧C、永久发现点与真实回溯未改。它仍先完成根与完整场baseline，再进行任何恢复/metric方向。

新model包括完整延拓政策、来源和明确的辅助参数含义，所以旧44ac checkpoint/旧branch标签不能通过改文件名被当成新场。首候选从同一实际reference和原完整自由初点开始；没有接受旧失败根，没有改H，没有继承旧Phi、reach或root证书。

新report/reader保存每角完成lambda、成功/拒绝阶段数、实际Newton更新、完整C/Cz评价计数、最后实际角字和完整阶段归因。root_iterations包含后来被拒绝阶段里确实发生的Newton更新；原方程直接评价计数与Cz内部图评价分开说明。初始失败仍保完整report，纯reader的parent使用实存reference，未要求捏造final.npz。

## 6. 复现材料与当前实际验证范围

候选消费已经公开的18参数文件：

- computations/frozen-zero-moment-Q-actual16-parameters.json，3618字节，SHA256 df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c；
- 完整definition为05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e；
- source/trace来源仍是实际15–16，参数文件是独立完整的小输入序列化，不冒9353字节runner输出的逐字副本。

完整候选源均不运行外部片段注入：

| 完整文件 | 字节 | SHA256 |
|---|---:|---|
| so3_zero_moment_continuation_operator.py | 75387 | 3f37789f1624b97cb7f83b1795ac5fe96be3b3026d4078115078f12e8fd4e34a |
| so3_zero_moment_continuation_geometry.py | 46500 | 613d33aff305a41a6d2857406309add0bb5d3c787be5b8f31ad4c7768446fb20 |
| fullclosed_zero_moment_continuation_so3_qp.py | 59525 | 9649ed99b614c468258646145948d7c06feb356c72806c73727728ea498ed88e |
| launch_zero_moment_continuation_so3_actions.py | 13641 | e57eb3d7f85a0abb44fb75ea56e918a9cd254025a718936bc163b82131f774d9 |
| read_zero_moment_continuation_so3_report.py | 31611 | a0c927aa9d7608a16ad7c051861903ebb533be3602325c2aada60ed6b1ccae61 |
| derive_zero_moment_continuation_entry.py | 38959 | cc2836a7d04d8df88fdb5e969d9502df953f99f15c03af54efdc380bc51b0200 |

可移植deriver包含新增政策和所有新方法的完整正文，输入五份完整旧源并核其SHA，生成五份完整新源；没有依赖未提交的片段文件。已实际用纯标准库运行它并核五份输出逐字相同，完成AST/compile/重复字面dict键检查，以及原物理/隐式方法和完整driver科学主循环比对。没有本地导入科学库或执行任何F/J/根/矩计算。

两步候选参数为 zero-moment-Q-residual-continuation-first-ready.json，16468字节，SHA256 61042b976d4de0fefee444c8627286f2cb2592803e8219ad5148750a84800da2。首完整命令116个argv字，已实际纯 --print-command 通过；后继为只读完整归因。它保留原1×16 metric方向、4×64 restoration、同mu=0.01、N2048、全部幅度/reach预算和真筛，并明确列全部延拓参数。尚未排科学运行，也没有新数值结论。

## 7. 边界与下一真实决策

原同球内Newton失败可能来自步幅、局部分支、控制子空间或支撑几何；延拓只处理其中的求根路径问题，不能保证解决控制空间本身的限制。若其实际lambda无法到1、需要越过原球、Cz实际不可用或最终原C不通过，须保完整失败轨迹，再据实际证据改输入或方法，不能靠辅助lambda小于1来接受一个未闭合场。

即使最终所有数值根与原真几何筛通过，也仍需全角连续分支、严格积分/浮点费用、全域metric、全部t的嵌入/reach与固定g的实际精化。有限continuation轨迹不等于题目的连续弯曲族；本候选不改变README的任一完成标准。

## 8. root实际发布、已有证据及完整地点依赖

2026-11-26 17:10 UTC：完整六源按上表原字发布；root亲读新增政策、全部根推进/回退/最终原C与Cz、全部其他源码差异，另核AST/compile、闭合source pins及ff500主循环后缀逐字。两代理已独立审。没有在本地执行科学运算。

[真实19–20](2026-11-26-actual-fixed-moment-Q-initial-failure-19-20.md)说明同cd530/H/05dc的原直接Newton初根失败；[真实23](2026-11-26-actual-03b-supported-chord-pass.md)说明同支持必要式在原H严格通过。后者不证明本控制族有根，也不给必须降低H的理由。本次选择只改同一原方程的数值求根路径。

正式完整参数为 computations/resume-20261126-zero-moment-residual-continuation-ready.json，17475B，SHA256 1ea4cc8cd36dca1857d5bb0994ccffff90555c28c74fce2898ee7fca94c93239。上节61042/16468B是原完整备稿；本次只补地点输入和明确来源说明，116个原科学argv字全部按原序保留。新增四个 --manifest 参数对，连同原reference共五份：reference locations、实际3的完整606报告、实际17的完整SOC报告、实际21的完整R696报告，以及前序积分方向的完整报告。前三个实际方向的新旧literal地点均来自同0f042/6ffc/carrier b025和N2048材料域，不继承其值、范数、Phi或证书。

积分报告此刻是**计划的必需前序输出**，尚未声称返回、成功或任何SHA。完整launcher会要求该文件存在，driver会核同carrier/角数并走完整history；缺文件必须实际失败，不能静默省掉该方向可能发现的位置。若真实26在报告生成前失败，须先登记真实原因，再准备有明确来源边界的新参数。该依赖不是从未知报告冒造一个科学结论。

两步已追加03b的现有积分科学步及其纯归因之后；原已有完整步骤对象逐值不变，活动队列92518B、SHA256 cabb82d4917838c6aecfc47dbddb56331f383332e3c1e92da61afdafb6b1aabf。本入口本次尚无实际返回；没有提前宣称lambda=1、闭合场或后继QP完成。
