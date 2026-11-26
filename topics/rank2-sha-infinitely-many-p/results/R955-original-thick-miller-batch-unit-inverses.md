# R955 — 原 Miller 链在同一完整厚商中批量求逆，逐线及逐前缀回投

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

- 状态：**完整算法证明；独立实现及生产接线待真实原作业执行。**
- 本条只减少原 Artinian consumer 中重复的整模单位求解，不新增原有限 shadow、非零性或普通素数结论。
- 直接依赖：R931 原完整 Artinian 范数/消费端；R942 §8、§10、§11 的完整源原像、仿射单位求解与有界行模算法。
- 精确原源：`original_ys_artinian_shadow_consumer.py` SHA256
  `a543c957c539fecef082cf26860cb321a3731d0c19e29e34205d8346f279c2e4`。
  具体接口为 `_miller_component_norm`；原链由
  `original_shadow_tate_trace_tools.py::_miller_chain/_line_quotient` 生成。

## 1. 实际重复工作与保持的原对象

原 `_miller_component_norm` 在已经通过完整加法图和原椭圆方程门的同一个厚商
\[
Q=A/I
\]
上工作。这里 \(A\) 是原 \(306\) 维正规化仿射环，
\(I\) 是原四交点计算及完整 support 分割返回的真实理想；
\(Q\) 允许非约化、多个闭点及非分裂剩余域。
系数仍是同一个 \(k=\mathbf F_{r^2}\)，\(r=29,41\)。

固定本次调用的原 \((z_x,z_y)\)、原 Tate basis index、辅助点和
`reader.chains[index]`。一条链项是
\[
(\epsilon_i;a_i,b_i,c_i,d_i,e_i),
\]
其中 \(\epsilon_i\) 指示先平方，线分子分母准确为
\[
n_i=a_i z_x+b_i z_y+c_i,\qquad v_i=d_i z_x+e_i.
\]

原程序对每条线的 \(n_i\)、\(v_i\) 各调用一次完整厚商单位求逆；
分子逆元只用于证明该分子确实是整个 \(Q\) 的单位。
当相应系数准确表明它是 \(k^\times\) 的常数时，
原 `_line_inverse` 已直接使用该常数并验完整乘积。
本条保留这个常数路径，只把其余有限个非恒定因子集中求逆。

不得把「在某些点非零」当单位证明，也不得省掉分子单位门；
后者是原 Miller 线在整个厚除子上可求值的必要接受门。

## 2. 任意交换环上的完整乘积单位引理

设 \(Q\) 为有单位交换环，\(f_0,\ldots,f_{m-1}\in Q\)，
\(p_0=1,\ p_{i+1}=p_i f_i\)。
则
\[
p_m\in Q^\times\quad\Longleftrightarrow\quad
f_i\in Q^\times\quad(0\le i<m).
\]

从右到左显然。若 \(u p_m=1\)，则
\[
f_i\left(u\prod_{j\ne i}f_j\right)=1.
\]
此论证不要求 \(Q\) 是域、约化、整环或局部环，
也不需要选择闭点、统一参数、分裂域或幂零厚度上限。

只保前缀 \(p_i\)，从 \(u_m=p_m^{-1}\) 反向计算
\[
g_i=p_i u_{i+1},\qquad u_i=u_{i+1}f_i
\quad(i=m-1,\ldots,0).
\]
归纳给
\[
p_{i+1}u_{i+1}=1,\quad f_i g_i=1,\quad p_i u_i=1.
\]
因此每个 \(g_i\) 是准确的 \(f_i^{-1}\)，最终 \(u_0=1\)。
实现逐个检查这三个完整商内等式；不是只核总积后写一个布尔接受标志。

本条所用 \(u_m\) 仍由既有
`OriginalTriangularValueNormTools.inverse_unit`
计算。它通过 R942 完整原像与仿射增广源，返回
\[
xM_{p_m}-1=yH_I
\]
的完整多项式证书，再把 \(x\) 降到同一个 \(Q\)。
没有将整模方程换成分式域解或约化纤维上的解。

若任一真实因子在 \(Q\) 中为零，立即拒绝；
若它只是非零的零因子或其他非单位，完整总积单位求解必失败。
所以批量路径与逐因子路径接受的原线因子集合完全相同。

## 3. 原常数、垂直线及完整 Miller 函数身份

原 `_line_quotient` 有三个准确分支：

1. 输入含 \(O\) 时返回常数 \(1/1\)；
2. \(A=-B\) 时返回垂直式 \((X-x(A))/1\)；
3. 其余切线或割线返回
   \((Y-y(A)-s(X-x(A)))/(X-x(A+B))\)。

新实现不重建这三分支，不自行选择斜率；
它直接读取原链中的五个原 \(k\)-系数。
当分子两个变元系数均零，或分母 \(X\)-系数为零时，
仍调用原 `_line_inverse` 的准确常数路径。
因此零常数仍被拒绝，分母恒等于 \(1\) 的垂直线仍准确保留。
非恒定因子通过上节完整单位门，不靠一般位置假设。

本题 \(\ell=5,7\) 的实际二进制链分别有三条、四条：
\(5\) 的步骤是 \(T\mapsto2T\mapsto4T\mapsto5T=O\)；
\(7\) 的步骤是 \(T\mapsto2T\mapsto3T\mapsto6T\mapsto7T=O\)。
因 \(T\) 的精确阶为对应奇素数，
中间加数非零，且只有最后一步两项互为相反数。
故每条实际链恰有一个垂直线、一个常数因子（该线分母 \(1\)），
非恒定因子数分别恰为 \(5,7\)。
新实现逐项核后还检查这些计数，
不是以计数代替任何原因子或单位计算。
因此每个非空原加法图组件，完整多项式单位求解次数从 \(5\) 或 \(7\)
降为准确的 \(1\)；常数单位门仍逐项执行。
这只是求解次数的确定结论，不承诺尚未测得的总运行时间。

按原顺序设链累积值 \(F_i\)，初值 \(F_0=1\)。
每一步先按原 \(\epsilon_i\) 决定是否平方，再乘 \(n_i v_i^{-1}\)。
实现保留这段原递推，并独立维护完整商中的前缀分子分母
\[
(N_i,D_i),\qquad (N_0,D_0)=(1,1).
\]
平方步骤同时平方 \(N_i,D_i\)，然后分别乘原 \(n_i,v_i\)。
每一步准确回投
\[
F_iD_i=N_i
\]
到完整 \(Q\)，并逐线验证
\[
n_i n_i^{-1}=1,\quad v_i v_i^{-1}=1,\quad
(n_i v_i^{-1})v_i=n_i.
\]
因每个 \(v_i\) 的实际完整单位证书已经存在，
所有 \(D_i\) 也是单位，所以这些前缀身份唯一确定
原来那一个 Miller 函数在整个 \(Q\) 的值。
这不是只验证某个有共同零的交叉乘积；
在这里所有被除因子先已证明为完整商单位。

实现还在前后核同一个 `reader.chains[index]` 对象、
每个平方标记、五系数及顺序，
不准在批量步骤换成共轭链或另一归一化的 Miller 函数。

## 4. 原完整范数与输出路径保持

得到最终 \(F\) 后，仍调用原
`_evaluate_miller(chain, auxiliary, ..., k)`
计算原辅助点处的非零常数 \(c\)，构造完整商值 \(F/c\)。
随后仍调用同一 `tools.norm_unit(I,F/c)`：
对完整原 \(I\) 的所有基素多项式、所有非约化层，
计算到同一个 \(k\) 的完整范数。
辅助常数自然带完整商长度指数；不先降厚度、除子次数或 \(\ell\) 余数。

本条不修改原两个辅助点、两个完整加法图、
所有成分长度相加、四个原交点、[6]、Tate 校准矩阵、
完整 \(18\times9\) Artin 读数、三个原 CM 读数或其非零检测器。
原 `_miller_component_norm` 返回对象的已有字段全部保留；
新增的批量单位证书明确声明一份「总积完整单位求解」及各因子完整回投，
不伪称每个因子独立运行了原多项式求解器。

## 5. 有界作用域、源码接入与待执行门

新增 `original_miller_batch_units.py` 只保存当前一个实际组件的
有限个因子、前缀与逆元；没有跨理想、跨原函数或跨作业缓存。
所有乘法和降模使用原 `_WholeQuotient`、
同一个实际 engine、同一个完整 \(I\) 与同一个 \(k\)。

生产只在既有独立 Artinian wrapper 的离线进程中，
把原 `OriginalArtinianShadowConsumer._miller_component_norm`
绑定到此实现；原 consumer 文件及运行中的 F 作业不改。
接入前核原 consumer 完整 SHA256 和原方法对象，
接入后核实际绑定；完整原 `main()` 及全部数学接受门继续执行。
host manifest 必须增加新 helper，准确从 \(44\) 源变为 \(45\) 源，
request/implementation 标签同步，不能只改代码漏改来源数断言。

最终 wrapper 对原四 pair 的每个真实非空 Miller 组件逐项核：

- 两个 basis index、所有原线、常数/非恒定因子数与前缀回投均返回；
- 该组件只做一份完整总积单位求解；
- 实际调用既有全部层范数，旧完整长度与输出身份照旧；
- 所有新增证书均来自该次实际原消费过程。

原空除子或空加法图的既有路径继续是范数 \(1\)，
不伪造一次不存在的批量调用。
本条不为这一优化另开独立 fixture 或第二次原正规化作业。
接好唯一后继原生产入口后，
以真正原 \(306\) 维完整数据接受或拒绝此实现。

实现源码12700 bytes，SHA-256 `f763351681f110963652cd6ff3566e8240991ffad98c93580da0b2e1a7933fe2`。root已对照原consumer的逐线、辅助常数和完整norm调用及原两个二进制链；此处发布源码与证明，不把尚未运行的原306消费过程记为PASS。

## 6. 已审最小生产接线及当前持有版本

root已对照未改consumer的真实返回路径
`pair_summaries/full_original_pairing_norms/all_complete_components/whole_miller_norm`，
以及 `original_tate_reader` 的实际context键。新增wrapper逐个读取
原调用产生的batch记录；原0长路径只接受原norm1标志，不伪造调用。
helper导入时捕获原方法对象，绑定前后核相同对象和原完整文件SHA。
其余四类、一map、两geometry绑定及原完整main保持。

以下三件替代R942§13.14–13.15的持有版本；尚未写入触发路径，
仍等唯一F实际终点后接后继生产：

| 路径 | Git blob | 字节数 |
| --- | --- | ---: |
| scripts/produce-original-triangular-artinian-shadow.py | `02dc1f76f03c9aa779584c64f14e999369b2ccdb` | 18433 |
| scripts/launch-original-triangular-artinian-shadow.py | `33c973d77063d92dadbda935bad31435630a08e0` | 10318 |
| ci/original-triangular-artinian-shadow-request.json | `16a9668f6e7f80ec70d33745b2d38026f813620a` | 836 |

对应SHA-256分别为：

- producer：`957e97d425d2cda76225b29697918e785755e6b9da9b2cc5ecf58f01e49cfeb6`；
- launcher：`a06b3316bcf48cd6d6c5ae0c83f92c9b4e010f990db23a6b05b2bb1c9059c3ee`；
- request：`15967f981c59903374072a2e47bd1091f6660744adf45d7b6b7766dc9504d9ef`。

workflow仍为Git blob `5713d440f42e1bd2f638944ce2dc9d3d4ddd1d5b`。
host准确明列45个唯一完整来源；schema v4及implementation同步。
原两份PASS pins、r29/q2453/batch64/minimal、原两图/四交/九对/
所有厚层及全部18×9读数均不改。尚无这份后继原生产的实际回执。
