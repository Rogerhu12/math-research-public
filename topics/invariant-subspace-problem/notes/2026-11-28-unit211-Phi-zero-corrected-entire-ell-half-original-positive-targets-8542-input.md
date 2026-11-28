# 首次新输入：正确 Phi 的整个 ell-half、同 lambda 原模块与正 z/D 目标

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（Asia/Taipei）。
- 状态：未执行；不预定 gcd 次数、矩阵秩、正幂返回或整支排空。
- 源：2026-11-28-unit211-Phi-zero-corrected-entire-ell-half-original-positive-targets-8542.py。
- Git blob：bcb71ff5af8cc5634c18887e1ca00a0524e66d18。
- SHA256：bd14e7724b688d596d51207ac859143321a7526407b9c702a3641dbeb1d957b4。
- 19640 字节；120 秒、1 GiB，外层可为 135 秒；两份小源码依赖。不得提高预算或重复失败数学门。

## 1. 真正的新原纤维及旧单位

沿已经纠正的当前 $\Phi=0$、$D\ne0$ 原图，令 $s=u-1$。本次只取整个尚未关闭的

$$
\ell=\frac12,\qquad Q=4(u-1)(u-2).
\tag{1}
$$

由正确的 $\Phi$ 恒等式，二者在原 $Q\ne0$ 图等价。不是取一个模点、一个复根或已知边界双数点。直接有

$$
\begin{aligned}
\delta&=1-4s(u-2),&
m&=u-\tfrac12,&
M&=-2s^2,&bc&=-\frac{s^2}{2\delta},\\
T_0&=-4s^2,&
J&=-4s,&P_{02}&=4s^2(u-2),&
P_f&=16s^4,\\
A&=4s,&
B&=16s^2(2s^2-3),&
L&=2s(u-2),\\
f&=\frac u2-(u-2)(\lambda-\tfrac12)
       -\frac{(u-2)^2}{s}(T+\tfrac12).
\end{aligned}
\tag{2}
$$

所以原三真均值的头在此曲线上为

$$
\det H_{012}
=-\frac{1024s^{10}(u-2)^7(2s^2-3)}{\delta^4},
\tag{3}
$$

已由当前原 $Q,\delta,s,M,A,B$ 支付。这里 $u$ 的单位性只引用独立的[原零基均值排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)；$m$ 只引用[完整原等权排除](../results/R150-appendix-unit211-equal-weights-complete-original-exclusion.md)及其正确 Phi 范围静审。未采用旧撤回的 Rbar、H1/H42、583、NP5 结论。

原 $A=0,B=0$ 的完整正确排除已支付 (3)。$\theta$、新的纯 $u$ 因子没有被当单位。$\ell-\tfrac12$ 正是本次整零纤维，不会被反演。整个已刊原 $I_{10}$ 及所有物理值条件仍保留；本次从其原 $I_6$ 子系统寻找正目标。

## 2. 专门化先于展开，明确不重放旧门

两份完整依赖先在 AST 外核 SHA：

1. 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py，SHA256 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。
2. 2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py，SHA256 84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0。

第一份只读 def param(p): 以前 4007 字节的正确四原式定义，前缀 SHA256 dd105b713040712dad7cebeefb489c8e1cf53f56cb5fce8ff0de0bf681d6c669。在定义自由符号后，立即以 (1) 替换 $Q$，然后才构造正确 $R,W,O,N_1$。因此从未展开一般权上的旧 C6。

第二份只读 R=env['R']; 至 seeds=[rN,rNS,rPS,c1,c2] 之前的 10153 字节，片段 SHA256 ccfe93b7ba226f39592c69087a9f5aa08fa556ca320c84831809fdbe878c26d1。仍保其正确三均值规则、完整原 NS/PS 定义和两个 overlap 的必要系数；跳过旧顶层 assert、显示、动作/缺陷检查循环及不需要的定义。内层每次原乘法的三坐标恒等式仍存在，因为它正是本次系数定义的同源实现。

本次不执行旧全图十五列证明门、旧两 cofactor 结果门、旧固定十二阶门、旧头因式门或任何撤回源。新的原计算发生在整 (1) 上，并始终由这个专门化同态运输已刊的原来源。不是先删某个纯 $u$ 头零点再把结果说成整图。

两内层 alarm 都被同一个最初的绝对截止时间钳住；相同的 1 GiB 硬界不会被提高。

## 3. 新的同 lambda 原关系

记 $v=(1,T,z)$，已刊正确原 $I_6$ 的三坐标种子为

$$
G=(r_{N_1},r_{NS},r_{PS},c_1,c_2),
\tag{4}
$$

其完整呈示为 $G,M_TG,M_zG$ 的十五列。这里三生成不表示三列自由，两个 overlap 和全部动作列都不能删。

在新曲线上，分别取 $(N_1,NS,PS)$ 及 $(N_1,c_1,c_2)$ 的原三列 cofactor。只清旧已付权分母、只除所有三个实际乘子的共同多项式，并完整返回三坐标，得两条 $\lambda$ 次数至多六的原标量

$$
C_0e_0,\ C_1e_0\in I_6.
\tag{5}
$$

这是本曲线的必要系数构造，不是复算原全图两 C6 的证明。新的共同乘子可能在这条曲线上增大；只有三个乘子都完整精除并返回才使用，未知共同零仍在这个原恒等式内。

首次在 $\mathbb Q(u)[\lambda]$ 求

$$
g=aC_0+bC_1,\qquad g\ \text{首一},
\tag{6}
$$

每个短除法返回完整乘积，最后把 (6) 复合回 (4) 的五个原种子，三坐标全部返回。所有新纯 $u$ 分母均保存；不把函数域非零视为原权单位。

若两标量均为零，准确保留整支；若返回常数，则只在清回完整纯 $u$ 覆盖之后作必要排除。若 $\deg_\lambda g=d>0$，完整保留其全部重数。程序没有预设 $d=2$，也没有从已知 bipartite 双数边界反推这个原 gcd。

## 4. 完整 3d 容器及固定正目标

在 $\mathbb Q(u)[\lambda]/(g)$ 上，仅用

$$
\lambda^j e_i,\quad 0\le j<d,\quad i=0,1,2
\tag{7}
$$

作为 $3d$ 个固定坐标。把十五条原列各乘 $\lambda^j$，得到 $15d$ 条原列；逐列保留除 $g$ 的商和余式，并核每个完整除法。没有把 (7) 当成原商的自由基。

列消元保存原列组合，所有被保留的消元列都逐 $3d$ 坐标回原矩阵。其秩只解释为 $\mathbb Q(u)$ 上的余商信息，不能直接排整个物理纤维。

首次目标按源码事先固定为：

1. 原 $z,z^2,\ldots,z^{3d}$；
2. 仅当第一组均无零余式时，原 $D,D^2,\ldots,D^{3d}$。

这里

$$
z=Qt,\qquad
D=\ell(2\lambda^2-2\lambda+1)-T^2
  =bc(h-k)^2.
\tag{8}
$$

正 $z$ 作用由同一个 $M_z$，正 $D$ 作用由

$$
M_D=\ell(2\lambda^2-2\lambda+1)I-M_T^2
\tag{9}
$$

给出。完整十五列及原矩阵缺陷保证这些是真正原商作用；不假设裸三坐标乘法结合或交换。$D$ 只作正乘，从未反演其范数、某个值或矩阵。

$3d$ 仅是固定测试上限。只有某一正幂的实际余式为零、并且返回完整原组合时，才登记目标；没有返回则保留，不凭维数猜幂零。

## 5. 终端三坐标及全纯 u 极点

若某目标返回，源码把有限容器内的原列组合再提升成三条完整 $\lambda$ 多项式恒等式：

$$
p_n-\sum_j\gamma_j\lambda^{a_j}r_j
=g\sum_{i=0}^2q_i e_i.
\tag{10}
$$

这里 $p_n$ 是原 $z^n$ 或 $D^n$ 的逐步原规则余式；每个 $q_i$ 的短除、整个 (10) 的三坐标、(6) 的原五源都实际返回。不是仅输出 matrix rank 或一条模余式。

令 $\Gamma(u)$ 为以下**实际最终有理系数分母**的完整最小公倍数：首一 $g$、它的五原种子乘子、输入列短除、各正目标作用的余式及 $g$ 商、终端 $\gamma_j$ 和 (10) 的 $q_i$。源码逐项核分母整除这个 LCM。

于是 $\Gamma g\in I_6$。每次正目标动作的误差由旧已付规则误差和一项 $gq$ 组成，全部分母已入 $\Gamma$，故归纳给

$$
\Gamma^2(z^n-p_n)\in I_6
\quad\text{或}\quad
\Gamma^2(D^n-p_n)\in I_6.
\tag{11}
$$

此幂次不随动作步数增加：归纳中乘的是原多项式 $z$ 或 $D$，没有新纯 $u$ 逆；新添的规则误差至多需要 $\Gamma$，$gq$ 至多需要 $\Gamma^2$。再由 (10)，得到

$$
\Gamma^2z^n\in I_6
\quad\text{或}\quad
\Gamma^2D^n\in I_6.
\tag{12}
$$

这里只剥 $\Gamma$ 中原先已付的权因子，留下完整 $C(u)$；结论为

$$
C(u)^2z^n\in I_6
\quad\text{或}\quad
C(u)^2D^n\in I_6
\tag{13}
$$

（在原已付系数环中）。若 (6) 已返常数，则相应为一次 $C(u)\in I_6$。所有未知纯 $u$ 头、内容或最终极点的整零纤维都保留在 $C=0$；消元过程中已约消的主元不额外删图。

物理 $D$ 已由当前 distinct-singleton 范围支付；物理 $t$ 已由[正确整个 t-zero 排除](../results/R150-appendix-unit211-Phi-zero-true-entire-tzero-original-exclusion.md)支付，所以 $z=Qt$ 亦已付。因而 (13) 是整个 (1) 的必要纯 $u$ 覆盖。只有实际 $C$ 为已付单位才得整支排空；否则完整 $C=0$ 纤维继续处理。此正目标结论并不把已知 $D=0$ 双数边界称为原物理解。

## 6. 输出与失败边界

只输出源、参数定义、次数、字节数、SHA、完整返回计数及小回执，不保存任何系数载荷、缓存或分片。若触及首次 120 秒或 1 GiB 边界，准确保留已完成阶段；未返 gcd、未返原矩阵、未返正幂、未返完整 cover 均不能相互替代。该唯一数学门不重跑、不增限，不以边界模型或泛域计算补称成功。
