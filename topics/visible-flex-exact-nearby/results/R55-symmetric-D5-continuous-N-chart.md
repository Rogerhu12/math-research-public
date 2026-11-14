# R55：新 D5 对称图的连续负 N 图表与局部简单根

2026-11-12，constructive-route。

**状态：已证明的中间结论，含有向浮点区间证书。** 对本文明确指定的
无限 R33 图，证明整个实核心的实际第二基本形式分量 $N$ 严格为负，
并给出同对象输出径向度量的一对局部简单根。所有角度都被覆盖；
径向 knot 单元、DFT、三角函数、无限角尾和基本运算舍入均进入界中。

对象是由保存输入**先显式偶/奇平均，再作 R33 无限 primitive**得到的
曲面图，不是既往正负同根浮点射线所隐含的近似镜像对象。本文没有
把旧返回误差变成已认证的返回误差，也没有支付复角域、参数管、
完整 PDE 传递、闭帽或精确等距族。

## 1. 适用的精确标量判据

设 $a=a(x)>0$，并令
$$
\phi=\theta+\pi/2+\beta(x,\theta),\qquad
T=(\cos\gamma\cos\phi,\ \cos\gamma\sin\phi,\ \sin\gamma).
$$
设 R33 图满足 $F_\theta=aT$。记
$$
e_\phi=(-\sin\phi,\cos\phi,0),\qquad
e_\gamma=(-\sin\gamma\cos\phi,-\sin\gamma\sin\phi,\cos\gamma),
$$
$$
P=1+\beta_\theta,\qquad
C=F_\theta\times F_x,\quad A=|C|,\quad
n=C\cdot F_{\theta\theta}.
$$
有准确恒等式
$$
\boxed{\quad
n=-a^2\left[
 P\cos\gamma\,\langle F_x,e_\gamma\rangle
 -\gamma_\theta\langle F_x,e_\phi\rangle
\right].
\quad}
\tag{55.1}
$$
证明：$T_\theta=P\cos\gamma\,e_\phi+\gamma_\theta e_\gamma$，
而 $T\times e_\phi=e_\gamma$、$T\times e_\gamma=-e_\phi$。于是
$$
n=a^2(T\times F_x)\cdot T_\theta
=a^2F_x\cdot(T_\theta\times T),
$$
即 (55.1)。这个式子包含旋转基的 $\theta$ 导数，所以 $P$ 中的常数
$1$ 不能丢掉。证毕。

假设在所考察的参数区域内有统一界
$$
P\ge P_0>0,\quad |\gamma|\le\Gamma,\quad
|\gamma_\theta|\le G,\quad
(F_x)_z\ge Z>0,\quad |(F_x)_{\rm horizontal}|\le H,
$$
$$
a_-\le a\le a_+,\qquad |(F_x)_z|\le Z_{\rm abs}.
\tag{55.2}
$$
置
$$
c=1-\Gamma^2/2,\qquad B=cZ-\Gamma H,\qquad
\Phi=P_0cB-GH.
\tag{55.3}
$$
若 $c>0,B>0,\Phi>0,a_->0$，则
$$
\boxed{\quad
-n\ge a_-^2\Phi>0,\qquad
N:=\frac nA\le
-\frac{a_-^2\Phi}{a_+(H+Z_{\rm abs})}<0.
\quad}
\tag{55.4}
$$

证明：$\cos\gamma\ge c$、$|\sin\gamma|\le\Gamma$，所以
$\langle F_x,e_\gamma\rangle\ge cZ-\Gamma H=B>0$；
同时 $|\langle F_x,e_\phi\rangle|\le H$。两个正乘子 $P,\cos\gamma$
可分别用 $P_0,c$ 代下界，(55.1) 得到 $-n\ge a_-^2\Phi$。
由于 $n\ne0$，叉积 $C$ 非零，浸入性随之成立。最后
$$
A\le |F_\theta|\,|F_x|
\le a_+(H+Z_{\rm abs}),
$$
给出 (55.4)。证毕。

这是充分条件，不声称任意负 $N$ 都必须满足这些独立标量界。
若只以 Fourier 系数绝对值和估计 $P$，当前对象会得到负的粗下界；
下一节保留实际角多项式信息。

## 2. 全角与径向区间的有限验证

本题的相位为有限和
$$
\beta=\sum_{k=1}^{24}b_k(x)\sin(4k\theta),\qquad
\gamma=\sum_{k=1}^{24}g_k(x)\sin(4k\theta).
$$
固定一个径向闭单元 $I$，对每个系数和所需径向导数使用有向区间。
设
$$
B_2=\sum_k(4k)^2\sup_I|b_k|,\qquad
G_2=\sum_k(4k)^2\sup_I|g_k|.
$$
取四分之一周期 $L=\pi/2$ 的 $J$ 个等距节点，$\delta=L/(2J)$。
若区间三角运算给出各节点上的 $P$ 和 $\gamma_\theta$ 包络，则
$$
P_0=\min_j\underline P(\theta_j)-\delta B_2,
\qquad
G=\max_j\overline{|\gamma_\theta(\theta_j)|}+\delta G_2
\tag{55.5}
$$
是整个 $I\times\mathbb R/(2\pi\mathbb Z)$ 上的有效界。
这是实函数的中值定理：任意角点到一个节点的周期距离不超过 $\delta$，
且 $|P_\theta|\le B_2$、$|(\gamma_\theta)_\theta|\le G_2$。
四重标量对称把一个四分之一周期的结论延拓至全圆。
另取 $\Gamma=\sum_k\sup_I|g_k|$。

为控制 $F_x$，使用同一无限 R33 primitive 的有限直接 DFT 多项式
$$
(F_x)_{\rm horizontal}=
\left(U_0+\sum_{m\ge1}U_m\cos(m\theta),\
             \sum_{m\ge1}V_m\sin(m\theta)\right)+\text{误差},
$$
$$
(F_x)_z=Z_0+\sum_{m\ge1}W_m\cos(m\theta)+\text{误差}.
$$
这里书写在正交旋转基中；$m$ 为 $4$ 的倍数。若有限多项式与无限
primitive 的向量误差不超过 $\varepsilon_x$，可采用
$$
\begin{aligned}
H&=\overline{|U_0|}
  +\sum_{m\ge1}\max(\overline{|U_m|},\overline{|V_m|})
  +\varepsilon_x,\\
Z&=\underline{Z_0}-\sum_{m\ge1}\overline{|W_m|}-\varepsilon_x,\\
Z_{\rm abs}
 &=\overline{|Z_0|}+\sum_{m\ge1}\overline{|W_m|}+\varepsilon_x.
\end{aligned}
\tag{55.6}
$$
第一式使用
$|(U\cos m\theta,V\sin m\theta)|\le\max(|U|,|V|)$，
再作向量三角不等式。所有有限系数都由区间直接 DFT 产生；
$\varepsilon_x$ 同时包含解析 Fourier 尾及混叠。它不是将有限
primitive 的角导数默认为准确单位切向量。

径向区间由全部正、负输入 knots 的并集分割。每个闭单元上，各 spline
等于该单元的一个多项式；用左右端点确定本 span，再在闭 span 内选择
一个精确 binary64 中心（极窄单元时可为端点），对同一多项式用有向
de Boor 计算 Taylor 系数，再以区间 Horner 计算整个闭单元。
共同 knots 在核心中均为简单 knots，相关原 spline 为五次，故低四阶
导数连续。Taylor 的第五系数取所选 span 多项式的值，即使中心为端点
也不改用相邻 span 的第五系数；所需的低阶 jet
在端点按连续性取相同极限。这样不需要从闭单元中删掉浮点邻接 knots
之间的微小区间。

三角节点不是直接调用未经定误差的 libm：脚本通过 Machin 公式的
有理 arctan 余项包住 $\pi$，再用 32 阶 Taylor 和显式 Lagrange 余项
计算 $|\text{argument}|\le2$ 的 sine/cosine。解析尾中的 exp 使用
有理 Taylor/几何余项和有向平方。基本 binary64 运算后取相邻外侧
浮点数，区间求和逐项进行。所用计算模型是 IEEE 正确舍入的基本
加减乘除；没有把 FFT 或三角库的输出当作准确数。

## 3. 当前新 D5 图的准确输入

本次输入来源于标记 $p=0.4413514918092046$ 的有限 phase predictor：

- data/phase_ring_continuation/type_fixed_step02_d5_jet_corrected_probe.npz；
- SHA256：0dcfb37f84a1b3d6197b375aa8700628a00398c0b509ce5da6c92f1ecf489199。

从它物化并冻结全部 radius、phase、mean、height slope 的 binary64
控制点和 knots：

- data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz；
- SHA256：0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b。

这些控制点与 knots 按准确实数解释。先把实际周长半径 $a$、加权后的
$\beta$ 定义为准确偶平均，把 $\gamma$ 定义为准确奇平均；高度定义为
偶 slope 从 $0$ 出发的准确积分，故 $Z$ 准确为奇函数。
之后按 R33 作无限角 primitive。保存的旧 floating height origin
只保留来源信息，不用它定义这里的高度常数。没有施加 Gaussian 平滑。

参数标记只指明来源点，不声称这个点已经实现 D5 的准确旋转数。
本对象也仍有非零 metric 残差。

## 4. 已得到的全核心常数

置准确有理端点
$$
r_*=\frac{1080863910568919}{4503599627370496}
>0.2399.
$$
它是输入 JSON 中 binary64 0.24 的准确实数值。使用
$|x|\le r_*$、quarter DFT 节点数 $256$、角 Lipschitz 节点数 $4096$，
径向最大单元宽度的浮点标记为 $0.0005$。全部 592 个闭单元通过 (55.3)，
零失败单元。输出给
$$
\Phi\ge0.37235144337277765,\qquad
-n\ge0.425295506732287,
$$
$$
N\le-0.3092073265707723.
$$
上列显示值本身按其保存的 binary64 外向端点解释。为给出简洁的纯有理
结论，逐单元准确分数比较后得到
$$
\boxed{\qquad
\Phi>0.37235,\quad -n>0.42529,\quad N<-0.3092
\quad (|x|\le r_*,\ \theta\in\mathbb R).
\qquad}
\tag{55.7}
$$
特别地，每个点都是浸入点，R37 需要的实际 $N<0$ 实图表在整个核心成立。
这一结论不从采样 $N$ 的最小值推导。

有限包络、所有单元和依赖 hashes 位于
data/phase_ring_continuation/type_fixed_step02_d5_jet_core_N_interval.json，
SHA256 538c3edbd89c2e322f5921ab62f08ff9f12dece2d878d19014daa2db6d866b28。
另有 core_N_coverage.json：把每个输出端点还原为准确 dyadic 数，
核对首端为 $0$、末端为 $r_*$、所有相邻端点准确相同、592 个单元均
通过，并对 (55.7) 作准确 Fraction 比较。它也记录各组输入 knots 在
核心中的最大重数均为 $1$。

由显式径向反射，若 $Q=\operatorname{diag}(1,1,-1)$，则
$F(-x,\theta)=QF(x,\theta)$，
$F_x(-x,\theta)=-QF_x(x,\theta)$，$F_\theta(-x,\theta)=QF_\theta(x,\theta)$。
因此 $C(-x)=QC(x)$，$n(-x)=n(x)$、$A(-x)=A(x)$。
正半轴的闭单元证书准确覆盖负半轴，未假设原始二进制 spline 自带精确反射。

## 5. 同一对象的局部目标根

对同一无限图取
$$
E(x)=\langle |F_x|^2\rangle,\qquad g_0=E(x)\,dx^2+a(x)^2\,d\theta^2.
$$
目标曲率由
$$
C_0=a'E'-2a''E,\qquad K_0=\frac{C_0}{2aE^2}
$$
给出。使用已经冻结的 simple-root 程序的直接区间 DFT/尾方法，在同一 frozen inputs 上
重新计算，证得唯一局部正根 $t$ 被 binary64 端点
$[0.2383968,0.2383972]$ 包含；可以安全写成纯有理包络
$$
\frac{2383967}{10^7}<t<\frac{2383973}{10^7}.
\tag{55.8}
$$
在准确有理 collar
$$
I_{\rm turn}=
\left[\frac{238397}{10^6}-\frac1{4096},
      \frac{238397}{10^6}+\frac1{4096}\right]
$$
上，$a,E>0$，并且
$$
\boxed{\qquad 53<K_0'(x)<68.\qquad}
\tag{55.9}
$$
所以该 collar 中只有这一个根，根左侧 $K_0<0$、右侧 $K_0>0$。
令 $\kappa(x)=K_0(x)/(x-t)$，在根处按连续性延拓，则中值积分式给
$$
53<\kappa(x)<68\quad(x\in I_{\rm turn}).
\tag{55.10}
$$
输入原始点的根区间宽度内实际有更紧的 $K_0'>60.098$ 下界；
这里采用整个 collar 上的统一数值。

完整输出为
data/phase_ring_continuation/type_fixed_step02_d5_jet_symmetric_root_interval.json。
其输入 hash 与 §3 准确相同。反射给出相应的负根及反向的导数符号。
本节仅排除 collar 内的额外根，没有据此宣称整个曲面上的型别组件
已经全部分类。

## 6. 可重放入口及尚未支付的部分

从本课题目录运行：

    OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_core_N_interval.py \
      --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_jet_corrected_probe.npz \
      --inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
      --out data/phase_ring_continuation/type_fixed_step02_d5_jet_core_N_interval.json \
      --right .24 --max-radial-step .0005 --quarter-nodes 256 --angular-nodes 4096 --resume

若 frozen inputs 已存在，程序只读该明确输入，不重新生成 profile。
初次不存在时才物化保存。完整输入 hash、源 hash 和三个 interval 依赖
hash 都写进结果；恢复时输入和算法参数改变会被拒绝。

闭单元覆盖与严格有理常数的复核：

    python scripts/fourfold_phase_core_N_coverage.py \
      --certificate data/phase_ring_continuation/type_fixed_step02_d5_jet_core_N_interval.json \
      --out data/phase_ring_continuation/type_fixed_step02_d5_jet_core_N_coverage.json

同对象局部根：

    OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_root_interval.py \
      --inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
      --left .2383968 --right .2383972 --quarter-nodes 256 \
      --collar-radius .000244140625 \
      --out data/phase_ring_continuation/type_fixed_step02_d5_jet_symmetric_root_interval.json

结果 (55.7) 是一个真实连续实图表输入；(55.9) 是同对象真实简单根输入。
仍须支付所有实核心 $K_0$ 符号、复角管中的 $n$ 零点排除、参数邻域与
二阶 Taylor 常数、实际 ODE 误差及共轭误差范数。既往近似镜像射线必须
在这个明确对象上重算或支付对象变更误差，不能直接转授。
完整全频 PDE 逆、无限平尾/闭帽和任务要求的可见等距闭族仍未完成。
