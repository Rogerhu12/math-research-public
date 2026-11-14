# R119 实际有限场：共享 C1 定义、坐标漂移残差与薄消费接口

2026-11-12，Astra-visible-flex-fd2d / metric_closure。

本接口接 R119 的准确固定材料 u 重建定义。
它已有一个真实旧 local stage 的字段和数值残差消费，但没有一份新强目标的完整小残差证书。
不会为尚未得到的解预写一个庞大的泛化框架。

## 1. 求解器应保存什么

当前状态振幅按

$$
[n_0,n_2,\ldots,n_{2K},m_2,\ldots,m_{2K}]
$$

排列，n 乘 cos，m 乘 sin。计算角可以是固定法向 φ，也可以是已明确的移动 ξ。
这些是实振幅，没有 $\sqrt2$ 或复 FFT 的半振幅歧义。

一份已闭存的 `solve_bvp` 输出应保留：

- 严格递增 `mesh = sol.x`；
- `values = sol.y`；
- 真插值一导 `first = sol.sol(sol.x,1)`；
- `rhs` 另存，不能用它覆盖真插值一导；
- 可选的真实中点 `midpoint_values`、`midpoint_first`；
- 原 `sol.sol.c` 另存，便于对照，不能在源报告中冒称它与另一份舍入数据逐位相同；
- 固定目标 candidate 的内容 SHA、固定 seed/chart 的准确定义和 SHA、动态 β 的完整定义；
- 中央准确曲线及定向标架的定义，或明确说明这份局部字段未提供初始几何。

若求解器改用 $n=n_{ref}e^\eta,m=n_{ref}\zeta$ 等正值变量，原 native η/ζ 数据仍须保留。
导出的 physical n,m 共享值/真一导可以定义另一份实际 C1 场；其全部角重建和径向重建误差
由后续残差支付，不能因入口 n 自动为正而跳过这些误差。

## 2. 数学上准确 C1 的有限定义

`scripts/fd2d_gc_shared_hermite_field.py` 提供 `write_field` 和 `SharedHermiteGCField`。
它绑定 shared binary64 节点、值和一阶 jet，而不是把各 span 独立舍入后的系数贴起来。

对 $h=s_1-s_0$、$t=(s-s_0)/h$，每个振幅准确定义为

$$
\begin{aligned}
c_0&=y_0,\qquad c_1=h\dot y_0,\\
c_2&=3(y_1-y_0)-h(2\dot y_0+\dot y_1),\\
c_3&=-2(y_1-y_0)+h(\dot y_0+\dot y_1),\\
y(s)&=c_0+c_1t+c_2t^2+c_3t^3.
\end{aligned}
\tag{1}
$$

这里每个保存的 binary64 数视为其准确有理值，h 也按准确有理差解释。
因此左右相邻 span 的值和一导**准确相同**，m,n 为 C1。
浮点评估器只是 (1) 的数值代表；严格 consumer 应对 (1) 用向外舍入运算，
不能把浮点评估器生成的系数再认作准确输入。
原 SciPy PPoly 的独立 binary64 系数可能含最后几 bit 的接口差；本定义明确支付了它，
没有以“C1 cubic”名称忽略非零跳变。

保存格式为小 JSON manifest 加 SHA 绑定的 `.npz.gz` 分片。
分片仅含 `nodes`、`values`、`first_s`，相邻分片共享一行；reader 逐项核对共享行、
有限性、dtype、完整径向覆盖及基底标签。
`chart` 是开放的准确定义记录，未被锁死成只能固定 φ；
`provenance.initial_geometry` 可绑定全域后验使用的准确中央曲线。
缺失初始几何时，consumer 不应默认 $d_0=k_0=0$。

## 3. 动态计算角中的物理残差

令 $u=U(s,\xi)$ 是一个明确的、周期且正向的计算坐标，记

$$
q=U_\xi>0,\qquad V=U_s,\qquad w=V/q.
$$

字段的 $n_s,m_s$ 在本节均指**固定 ξ** 的导数。
按固定材料 u 的准确函数反解 ξ 后，R119 的残差为

$$
\begin{aligned}
R_n&=n_s-w n_\xi-\frac{m_\xi}{aq}-\frac{a'}a(l-n),\\
R_m&=m_s-w m_\xi-\frac{l_\xi}{aq}+2\frac{a'}a m,\\
l&=\frac{m^2-a''/a}{n},\qquad
l_\xi=\frac{2m m_\xi-l n_\xi}{n}.
\end{aligned}
\tag{2}
$$

没有 $K_s$ 或 $l_s$。
因为 $s$ 固定时 ξ→u 是整圈双射，$\sup_\xi |R|=\sup_u|R|$，
可把严格逐径向上界直接送入 R119 的固定材料积分。
准确位置定义仍是**沿固定 u** 的 frame ODE；不能把移动连接的另一种有限残差图混同进来。
R119 §5.1 已单独区分这两种准确重建。

对当前拟用的渐变角

$$
U(s,\xi)=(1-\beta(s))U_{seed}(\xi)+\beta(s)\xi,
$$

有

$$
q=(1-\beta)q_{seed}+\beta,\qquad
V=\beta'(\xi-U_{seed}(\xi)).
$$

$U_{seed}(\xi)-\xi$ 是周期函数；它的常数积分规范必须明确，不能当作线性不周期角漂移。
若 $0\le\beta\le1$，则 $q\ge\min(1,q_{seed})>0$。
fixed balanced seed 法向角给 $q_{seed}=\rho_{seed}/a_0$。
准确常数由 R118 定义及新严格矩包支付；数值矩阵中使用的采样近似不改变这个物理定义。

## 4. 先消系数、后除正分母

直接把 (2) 的每个 O(1) 项分别取区间再相减，会损失需要的小残差。
记 $A=a'$、$B=a''$，定义

$$
\boxed{
\begin{aligned}
P_n={}&q\{a^2n n_s-aA(m^2-n^2)+AB\}
       -a^2Vn n_\xi-a n m_\xi,\\
P_m={}&q\{a^2n^2m_s+2aAmn^2\}
       -a^2Vn^2m_\xi-2amn m_\xi+am^2n_\xi-Bn_\xi.
\end{aligned}}
\tag{3}
$$

逐项代入 (2) 并乘正分母，即得准确恒等式

$$
\boxed{R_n=\frac{P_n}{a^2qn},\qquad
R_m=\frac{P_m}{a^2qn^2}.}
\tag{4}
$$

证明只用乘法分配律及 $K=-B/a$。
源码的 `codazzi_numerators` 只使用加、减、乘，能直接接已有向外舍入的
radial polynomial × 完整 Fourier 类型；小分子在系数层相消后再包围。
它包含 moving-chart 的 V 项，固定角只是 V=0 的特例。

实际连续消费所需的最小接口因此是：

1. 在合并的真实径向 knots 和目标 piece breaks 上，用 (1) 生成所有保存模态的
   n,m、$n_s,m_s,n_\xi,m_\xi$ 有限多项式；
2. 同盒读取准确 a、a′、a″ 目标包和准确 q,V 图册包；
3. 用 (3) 合并多项式系数，保留所有真实模态；
4. 在完整角弧上包围 $P_n,P_m$，独立证明 $a,q,n$ 的正下界，再用 (4) 相除；
5. 输出逐径向连续 $\sqrt{R_n^2+R_m^2}$ 上界，按 R119 积分；
6. 若还要 R119 曲率后验，再对实际分子和分母取角导。它仍不需要径向三阶目标导数。

现有 Fourier/Bernstein 区间工具和先前 normal-range 算术适配器可复用。
这里没有把未执行的第 1–6 步登记为已付，也没有为了等待全 BVP 写入无实际数据的庞大包围框架。

## 5. 已消费的真实 local stage

源码 `fd2d_gc_shared_hermite_field.py` 的 SHA256 为
`cc8d2802a0ebb0951c87a9ac309137ba7160749e1e31cc349c30bd124ea9df9c`。
producer `fd2d-gc-local-hermite-screen.py` 的 SHA256 为
`889fd00d97a4d75a5140c73205bc20303cd672651daf9063bd9f28d0d61fb432`。

它读取 numerical 已保存的 local-02 实际 DOP853 两端状态，区间
$[.5299999999999994,.5302999999999993]$，M63、384 角有限 RHS。
没有重新求 ODE。因为原 stage 没保存 dense interpolant，producer 如实选择
两个端点重新求值的有限 RHS 为**新 Hermite 场的定义一导**；
没有把它称作不可取得的 DOP853 dense-output 导数。

首次写目录真实遇到 ENOSPC，会话 67853 exit 1，未生成字段报告。
主线程释放经核验的重复 Git 传输缓存后，会话 40185 从同一保存端点消费，自然 exit 0。

实际字段为
`2026-11-12-fd2d-metric-gc-local-c1-field-01/field.json`，SHA256
`179501d375a1e2714424562355f2c7beec40a1753f0811bcfe0280db2dfda5db`。
实际报告 `2026-11-12-fd2d-metric-gc-local-c1-screen-01.json`，SHA256
`2107f1dc53087e70a1baae601a78f50215de6436537d58316f3b2aacfa6f6d5e`。

在 17 径向点、1024 角点，$n\ge.3458020164030087$，
$\max|R_n|=.03433103820946874$、$\max|R_m|=.4756056854130467$，
残差范数最大约 .475605816。
因此这份旧 M63 local 场不能用于宣称 R119 所需的小残差。
清分母式 (3)–(4) 与直接式 (2) 的数值差不超过 $5.64\times10^{-18}$。
这是一个真实局部字段的薄接口核对，不是新强核、全前缀或连续 metric 证书。

后续优先消费新的、真正闭存的 BVP 场。
初始曲线、尾接缝与全域几何继续分别绑定 R116/R118、R117 和对应几何证明；
不能让文件格式的完整覆盖标志替代任何未付的数学量。
