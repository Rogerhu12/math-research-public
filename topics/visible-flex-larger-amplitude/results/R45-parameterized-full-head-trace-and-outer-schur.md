# R45：46参数真实头迹、完整二阶接缝与外头 Schur 条件

作者：exact_closure（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**已证明（条件工具及实际 cut 常数）。** 本文把 R43 的固定浅高度
问题推广为真正的46参数全频头迹，给出参数导数的正算子公式、
外头所需的非线性迹余项，以及 node12 的完整连接和二阶高度界。
最后给出包含全部高频边界的连续外头 Schur 条件。

本文没有支付 R43 的实际428个联合门，也没有支付外胞元0..11的
连续 Green 核、候选残差和 Schur 逆。此前90734仅观察到矩阵装配，
其终态未知，不用作存在证书。本文的参数化与外头存在结论均以明确
列出的门为前提；第5节的单 cut 有理常数已单独核算。

## 1. 固定对象、对称性与参数数目

固定 R26 的同一个真实径向源、R18 的完整深图和 R43 的连续
角宽 $\tau(r)$、正包络 $V(r)$、平衡系数 $B_n$。
真实 node12 记为 $r=b$；node225对应数学 $F224$。
胞元12..224内的 $r,w,w_r,E=1+w^2$ 始终来自同一个实函数。
不把保存的浮点半径、独立保存的 $E,E'$ 或有限连接动量换作它。

本文使用当前计算的反射对称、$\pi$ 周期高度：非均值高度为
$\cos(2j\theta)$ 级数，角导数为相应正弦级数。低频高度参数为

$$
a=(a_1,\ldots,a_{46})\in\mathbb R^{46},\qquad
\delta Q_{2j}(b)=a_j .
\tag{45.1}
$$

这里 $Q=h_\perp/r^4$，$a_j$ 是实余弦的完整幅度。复化时使用
$\mathbb C^{46}$；两个 signed Fourier 系数各为该幅度的一半。
本文不把一般同时含正弦、余弦的92个实方向称作46维。

令 $L_*$ 是 R38 或 R39 的准确低46辅助解，$z_*^0$ 是其准确
far低高度参数。其存在、修正盒和 far 界可以已知，而不必先把
每一点算成浮点数。整个中心仍只含46个非均值高度模，完整 mean
每次由同一 holonomy 小根补回。

其余浅频率 $|m|\ge94$ 的高度和径向迹均是本问题的输出。
它们不能再任意设为零，或当成一个任意全 Dirichlet 数据的无限维
自由输入。

## 2. 真线性参数提升及其可计算列

对每个 $m=2j$，取 R29/R42 的真实齐次列 $\Phi_m$，满足准确的
线性 far 条件并归一化为 $(\Phi_m)_Q(b)=1$。其定义依赖已证明
非零的浅高度 chart 分母。定义

$$
\Lambda a=\sum_{j=1}^{46}a_j\Phi_{2j}.
\tag{45.2}
$$

这些是全部46个真实模的列；未表示的 $j=9,\ldots,46$ 不能用
M8保存轨道的零填充来支付。

用 R43 的每胞元物理强范数 $X_n$，记可计算非负列 $\mathsf A_{nj}$，使

$$
X_n(\Lambda a)\le a_n^+(a):=
\sum_{j=1}^{46}\mathsf A_{nj}|a_j|.
\tag{45.3}
$$

一个直接有效的列是

$$
\begin{aligned}
\mathsf A_{nj}=(1+m)\bigg[&
\sup_{I_n}\frac{e^{\tau(r)m}B_n m r^3
                    |(\Phi_m)_Q(r)|}{V(r)}\\
&+\sup_{I_n}\frac{e^{\tau(r)m}}{V(r)}
\left(m^2r^3|(\Phi_m)_Q(r)|+
\frac{\sqrt{12}\mu_n}{r^4w(r)}|(\Phi_m)_\Xi(r)|\right)\bigg],
\quad m=2j.
\end{aligned}
\tag{45.4}
$$

式中两个分量先各自取径向sup，再求模和。若使用带符号的实际
$m^2r^3Q+\sqrt{12}\mu_n\Xi/(r^4w)$，可进一步收紧第二项；
(45.4)不依赖这种收紧。它直接来自 R33 的 canonical 到物理恒等式。
实余弦两半已合并，所以不再乘2。

用 $\mathcal E$ 表示准确 far 低高度评估，坐标已吸收
$e^{38m}/S_F$。记

$$
|\mathcal E\Lambda a|_1\le e^+(a):=
\sum_{j=1}^{46}e_j|a_j|.
\tag{45.5}
$$

若未归一化的 far 列满足 $\phi_{Q,m}(F224)=1$，可取

$$
e_j=\frac{e^{38m}}{S_F|\phi_{Q,m}(b)|}.
\tag{45.6}
$$

分母必须用同一真实列的严格非零包络。此式是独立 far 评估，
没有把窄条带的范数免费提升到38。R42的逐面板列和完整胞元列
足以给 (45.4)–(45.6)；它们不是新的径向 ODE 定义。

## 3. 均匀参数盒与完整头解

保留 R43 的428个未知块

$$
Y=(\ell_n,h_n,u,\delta z),\qquad
\|\delta z\|_1/Z=r_z,
\tag{45.7}
$$

其中低变化 $\ell$ 的浅低高度为零；中频 $h$、无限频率 $u$
没有额外的浅高度约束。令

$$
e=\Lambda a+\ell+h+u.
\tag{45.8}
$$

准确映射的前三个分量仍取 R43 (43.3)，将其中 $e$ 换成
(45.8)。最后一个分量改为

$$
T_z(a,Y)=\mathcal E\Lambda a+\mathcal E T_\ell(a,Y).
\tag{45.9}
$$

所以在固定点上
$z_*^0+\delta z=\mathcal E(L_*+\Lambda a+\ell)$，没有放松真实
far高度一致性。低块中仍是 $f(L_*+e)-f(L_*)$；不得重新加入
一个并不存在的纯低中心残差。高块仍保留 $f(L_*)$ 及真实深图
全部高输出。

取一个复参数域 $\mathcal P$，设

$$
\bar a_n\ge\sup_{a\in\mathcal P}a_n^+(a),\qquad
\bar e\ge\sup_{a\in\mathcal P}e^+(a).
\tag{45.10}
$$

对428个半径 $x=(r_{{\rm lo},n},r_{{\rm mid},n},r_\infty,r_z)$，
在 R43 所有正映射公式中改用

$$
t_n=\bar a_n+r_{{\rm lo},n}+r_{{\rm mid},n}+r_\infty,
\tag{45.11}
$$

并在 far 正映射中加入 $\bar e/Z$。其余核、完整 mean 和深图
常数保持原来的实际对象。导数矩阵仍是 R43 (43.8)–(43.9)，
只要求其 $\rho$ 覆盖 (45.11)。特别地，$t_n$ 包含确定参数提升的
范数，不能在判断非线性定义域时将其删掉。

**定理45.1。** 假设全部核和参数列确实属于同一实对象，并且
改后的428个自映射门、完整 mean 域、far球域及正权收缩门在
$\mathcal P$ 上一致成立。则每个 $a\in\mathcal P$ 有唯一的盒内
全频头解 $Y(a)$。它准确接到 R18 无穷深尾，浅低高度恰为
$Q_{2j,*}(b)+a_j$；其全部高浅高度由解给出。映射 $a\mapsto Y(a)$
在参数域内部全纯，实参数给实解。

**证明。** (45.3)–(45.5)与 R43 的逐模固定质量证明给出改后的
正映射。参数固定时，$\Lambda a$ 不计入未知差，但参与全部非线性
导数的工作域。均匀的正权 $W$ 使每个映射的 Lipschitz 常数不超过
同一 $q<1$。在同一个完备闭盒内应用 Banach 定理。

每次迭代均由有界线性算子、完整 mean 小根、点态逆和 R18 的
解析深图组成，在复参数域内全纯；统一收缩使其在每个参数紧集上
一致收敛，故极限全纯。实性由实系数与唯一性保持。

低 Green 与低深边界提升均有零浅低高度；(45.2)因此直接给出
(45.1)。高两窗按准确 far trace 向外传播，未加浅端零约束。
完整 mean 及二阶深接缝由 R43 的论证保持。证毕。

在任一紧参数子域上，有限头部的正分母有统一余量；固定正角宽
控制所需角导数，准确 Darboux式给径向二阶导数的连续依赖。
R18的统一加权衰减控制余下无穷尾及 cuff 两阶极限。因此选定同一个
连续 mean高度规范后，上述参数族也在整个头部的 $C^2$ 拓扑下连续。
这仍没有涉及外头和完整闭曲面的几何性质。

这给的是46维真实全频迹流形。在任何投影到浅低高度的坐标中，
导数的该子块是恒等矩阵，所以46个方向没有因使用高频输出而减少。
它不声称完整浅 Dirichlet 数据可以任意指定。

## 4. 参数导数和外头需要的迹余项

沿用 R43 的正导数块 $\mathsf L,\mathsf H,g,f$ 和完整矩阵 $J$。
对一个参数方向 $\dot a$，置

$$
d_n=\sum_j\mathsf A_{nj}|\dot a_j|,\qquad
d_z=\sum_je_j|\dot a_j|/Z.
\tag{45.12}
$$

保持未知 $Y$ 不动时，参数导数有正列

$$
c(\dot a)=
\left(\mathsf Ld,\ \mathsf Hd,\ \sum_ng_nd_n,
\ \sum_nf_nd_n+d_z\right).
\tag{45.13}
$$

这里参数不直接进入高深图：高深图以独立 $\delta z$ 为变量；
参数对该变量的真实影响已由最后一块及 $J$ 的 far 列保留。
故不存在少算一条深图导数链的问题。

由正权收缩，Neumann级数逐项非负且收敛，给

$$
|D_aY\,\dot a|_{\rm blocks}
\le (I-J)^{-1}c(\dot a).
\tag{45.14}
$$

**证明。** 对固定点方程求导，得
$D_aY=(D_YT)D_aY+D_aT$。在正权范数中逆算子等于收敛的
Neumann级数。每一项由对应的非负 $J$ 幂和 (45.13) 控制。
也可以先对有限次迭代求导，再按同一几何级数取极限。证毕。

完整物理场还须加入直接提升 (45.12)。例如 cut 物理导数的上界为

$$
d_b(\dot a)=d_{12}+
[(I-J)^{-1}c(\dot a)]_{{\rm lo},12}+
[(I-J)^{-1}c(\dot a)]_{{\rm mid},12}+
[(I-J)^{-1}c(\dot a)]_\infty.
\tag{45.15}
$$

R43 的214维分解可以用于构造这个解，但最后仍须保留428行的
实际正算子界。式 (45.14)没有把一个有限网格 Newton 逆当作
全频真实参数导数。

下面给 R44 (44.54)所需的二次迹余项。令参数范数为
$\|a\|_* =\sum_j|a_j|/u_j$，其中全部 $u_j>0$。假设定理45.1
在复球 $\|a\|_*<R$ 上均匀成立。令 $\mathcal T(a)$ 是值于一个
固定外头迹 Banach 空间的准确迹，并假设

$$
\sup_{\|a\|_*<R}\|\mathcal T(a)-\mathcal T(0)\|\le M.
\tag{45.16}
$$

则对任意 $0<r<R$，取
$B=D\mathcal T(0)$、
$\mathcal R_{\mathcal T}(a)=\mathcal T(a)-\mathcal T(0)-Ba$，有

$$
\|\mathcal R_{\mathcal T}(a)\|
\le\frac{2M}{(R-r)^2}\|a\|_*^2,
\qquad
\|D\mathcal R_{\mathcal T}(a)\|
\le\frac{4Mr}{(R-r)^2}
\quad(\|a\|_*\le r).
\tag{45.17}
$$

**证明。** 在 $\|a\|_*\le r$ 处沿两个单位复方向分别取半径
$(R-r)/2$ 的 Cauchy圆。其和仍位于参数球内，所以混合二阶导数
范数至多 $4M/(R-r)^2$。沿 $ta$ 积分一次或两次，得到
(45.17)。可先取略小圆再取极限，避免开球边界问题。证毕。

R44使用 $\mathcal T=(P,K_\perp)$ 时，第5节给有界迹映射及明确
$M$：可用 $M=\varepsilon_b[ar a_{12}+
2(r_{{\rm lo},12}+r_{{\rm mid},12}+r_\infty)]$，其中参数球内
统一使用同一修正盒。这里减的是准确参数化中心 $Y(0)$；不把
辅助低中心与全频中心混为同一个迹。

## 5. node12 的完整连接与二阶高度常数

### 5.1 一次明确的角宽损失

记固定角宽的 Wiener 范数

$$
\|v\|_{\sigma,s}=\sum_m(1+|m|)^s e^{\sigma|m|}|v_m|.
\tag{45.18}
$$

在 cut，令 $\tau_b=\tau(b)$、$\sigma=1/64$、
$\varepsilon_b=V(b)/w(b)$。实际共同 q003 角宽的严格常数为

$$
\tau_b-\sigma>1/8,\qquad B_{12}\ge4,
\qquad \varepsilon_b\le A_{12}<2^{-51}.
\tag{45.19}
$$

对 R39 的真实强M20参考，显式选择同一个 q003 角宽，按 R42
将 $V_n$ 重标为 $s_nV_n$。全部213个形状参数、$B_n$ 和真实源相同，
$0<s_n<18$，并在 cut 有

$$
\varepsilon_b^{\rm strong}\le s_{12}A_{12}<2^{-46}.
\tag{45.20}
$$

原 strong 包保存的角宽函数与 q003 角宽略有不同；(45.20)只对
这里明确选定的共同角宽与重标包络使用，不声明两角宽逐字相同。

由 $\sup_{x\ge0}xe^{-x/8}=8/e<3$，有

$$
\|v_\theta\|_{\sigma,1}\le3\|v\|_{\tau_b,1},
\qquad \|v\|_{\sigma,2}\le4\|v\|_{\tau_b,1}.
\tag{45.21}
$$

$8/e<3$ 可由 $e>1+1+1/2+1/6+1/24=65/24>8/3$ 核算。
这支付 R41 所需额外角导数；后面的外头未知空间固定在选定条带，
不能每迭代一次再免费缩窄。

### 5.2 完整 mean、连接正向映射与唯一反解

设完整非均值 cut 场的物理强范数 $X\le2$。分成两个分量的质量
$X_p+X_k=X$，于是

$$
\|P\|_{\tau_b,1}\le\varepsilon_bX_p/B_{12},
\qquad
\|K_\perp\|_{\tau_b,1}\le\varepsilon_bX_k.
\tag{45.22}
$$

取 $R_0=1/256$。由 (45.19)–(45.20)，
$R:=\varepsilon_bX\le R_0$。R33 的完整 holonomy 根 $M$ 满足
$|M|\le4R^2$、$\|DM\|\le16R$，令 $K=K_\perp+M$。
利用 (45.21)及 $B_{12}\ge4$，有

$$
T_*:=\|K\|_{\sigma,1}+\|P\|_{\sigma,2}
\le R_0+4R_0^2=65/16384<1/128.
\tag{45.23}
$$

R33 (33.9)–(33.11) 的 Banach代数证明，改以
$W_{\sigma,1}$ 为基础代数、$P$ 多付一个角导数，直接给

$$
G:=\frac{\Gamma-1}{w^2}=K+P_\theta+\mathcal R(K,P),
\qquad
\|\mathcal R\|_{\sigma,1}\le2T_*^2.
\tag{45.24}
$$

没有使用有限 Fourier 投影。完整 mean 方程使 $G_0=0$。由于
$\|P\|_{\sigma,1}+\|P_\theta\|_{\sigma,1}
=\|P\|_{\sigma,2}$，

$$
\eta:=\|P\|_{\sigma,1}+\|P_\theta\|_{\sigma,1}
        +\|G\|_{\sigma,1}
\le2T_*+2T_*^2<1/32.
\tag{45.25}
$$

所以同一迹属于 R41 的完整连接唯一正根域。全部 $K$、mean及
未表示高频都由 $P,G$ 唯一恢复。

若两个真实场或同一参数导数的 broad-strip 物理差为 $d$，则
由完整 mean 导数及 (45.21)，

$$
\begin{aligned}
\|\delta P\|_{\sigma,1}&\le\varepsilon_b d/B_{12},\\
\|\delta P\|_{\sigma,2}&\le4\varepsilon_b d/B_{12},\\
\|\delta K\|_{\sigma,1}&\le(1+16R_0)\varepsilon_b d,\\
\|\delta K_\theta\|_{\sigma,1}&\le3\varepsilon_b d.
\end{aligned}
\tag{45.26}
$$

为控制 $\mathcal R$ 的全部方向导数，在半径 $T_*$ 的复圆上使用
$2T_*<1/20$ 和 (45.24)，Cauchy估计给
$\|D\mathcal R\|\le8T_*$。因此

$$
\boxed{\ \|\delta G\|_{\sigma,1}\le
(1+8T_*)[(1+16R_0)+4/B_{12}]\varepsilon_b d
<3\varepsilon_b d.\ }
\tag{45.27}
$$

例如右侧无量纲系数不超过
$(17/16)(33/16)=561/256<3$。沿实际允许域内的线段积分，得到
两点差版本。$(P,K_\perp)$ 的联合迹范数则直接不超过
$\varepsilon_b d$，给第4节的 $M$。

### 5.3 高度的全部 polar 二阶迹

非均值高度及角向、混合导数满足

$$
\begin{aligned}
\|\delta h_\perp\|_{\sigma,1}
 &\le bV(b)d/(2B_{12}),\\
\|\delta h_\theta\|_{\sigma,1}
 &\le bV(b)d/B_{12},\\
\|\delta h_{\theta\theta}\|_{\sigma,1}
 &\le3bV(b)d/B_{12},\\
\|\delta h_r\|_{\sigma,1}&\le\tfrac54V(b)d,\\
\|\delta h_{r\theta}\|_{\sigma,1}&\le3V(b)d.
\end{aligned}
\tag{45.28}
$$

第一行使用最小非零频率 $|m|=2$。第四行包括完整 mean 斜率。
高度的零模积分常数不在第一行里：可以选择一个统一的 cut高度
平移规范；若最终固定 cuff 或握持区已固定该常数，则必须保留
相应标量位置匹配，不能另逐胞元重置。

径向二阶迹可以避免任何隐藏的 $1/w$。由 R41 的准确 Darboux式，
置

$$
y=1+K,\quad T=P_\theta,\quad
L=y+ET,\quad A=1+w^2(yT-P^2),\quad
B_0=(K_\theta-P)^2,
\tag{45.29}
$$

则

$$
\boxed{\ h_{rr}=w_r\frac{A}{L}
             +\frac{Ew}{r}\frac{B_0}{L}.\ }
\tag{45.30}
$$

因为 $p=wP$、$h_r=wy$，R41 (41.33) 的分子各项均含一个
可与分母中的 $w$ 准确约去的因子，直接得到 (45.30)。
它不是以径向差分近似 $h_{rr}$。

R31 的真实背景主曲率界 $|\kappa_i|\le8$ 与 $w\le1/2$ 给

$$
|w_r|\le8E^{3/2}<12,\qquad
Ew/r\le8E^{3/2}<12.
\tag{45.31}
$$

在 $W_{\sigma,1}$ 代数中，(45.22)–(45.26)给

$$
\|K\|\le2R_0,\quad \|P\|\le R_0/4,\quad
\|T\|\le3R_0/4,\quad \|K_\theta\|\le3R_0,
\tag{45.32}
$$

以及

$$
\|L^{-1}\|\le(1-3R_0)^{-1}<4/3,\qquad
\|A\|\le2,\quad \|B_0\|\le16R_0^2.
\tag{45.33}
$$

差分的代数界为

$$
\|\delta L\|\le3\varepsilon_b d,\qquad
\|\delta A\|<\tfrac12\varepsilon_b d,\qquad
\|\delta B_0\|\le26R_0\varepsilon_b d<\tfrac18\varepsilon_b d.
\tag{45.34}
$$

详细地，$\delta K,\delta P,\delta T,\delta K_\theta$ 可分别用
$5/4,1/4,3/4,3$ 乘 $\varepsilon_bd$ 控制。故 $\delta A$ 的系数
不超过
$\tfrac14[R_0(5/4)+2(3/4)+2R_0(1/4)]<1/2$；
$\delta B_0$ 的系数不超过 $2(4R_0)(13/4)=26R_0$。
这些估计同时适用于实际差分和方向导数。

用 $\delta(L^{-1})=-L^{-1}(\delta L)\widetilde L^{-1}$，得到

$$
\begin{aligned}
\|\delta h_{rr}\|_{\sigma,1}
&\le12\left[\frac{1/2+1/8}{3/4}
 +\frac{3(2+16R_0^2)}{(3/4)^2}\right]\varepsilon_b d\\
&=(138+1024R_0^2)\varepsilon_b d
<\boxed{144\varepsilon_b d}.
\end{aligned}
\tag{45.35}
$$

所有运算在同一完整 Wiener代数中进行。此式是固定真实 $g$ 下
的 polar 二阶高度迹界；若需要 Cartesian 边界图的范数，还必须
用 R30/R27 的坐标转换和真实边界半径，不能将二者混称。

### 5.4 已执行的实际常数账本

脚本
[closure_cut_trace_interface_constants.py](../computations/closure_cut_trace_interface_constants.py)
仅用准确 dyadic 输入和 `Fraction`。它检查全部213个 q/strong
包络的同源形状、重标系数、(45.19)–(45.20)、角导数损失、
完整 mean 域、连接域和 (45.34)–(45.35)。
15项比较全部为真；新的执行经资源包装器记录真实退出码0，
wall 1.3001秒、峰24488 KiB，无 ODE、Arb长循环或算子求逆。

准确结果为
[cut常数](../notes/2026-11-12-closure-cut-trace-interface-constants-r1.json)，
退出记录为
[资源与退出码](../notes/2026-11-12-closure-cut-trace-interface-constants-r1-resource.json)。
其 $h_{rr}$ 系数为准确有理数 $8833/64=138.015625<144$。
旧32851终态未能从过期会话取回，所以本节明确引用 fresh r1 执行。
这些小常数不是完整头部存在、外头误差或强前缀匹配的证书。

## 6. 全部边界计数与准确二阶拼接

设外胞元0..11的真实高度解在 node12 给出完整非均值高度
$h_\perp^{\rm out}$ 和完整连接 $G^{\rm out}$。内侧使用定理45.1
的真迹 $(h_\perp^{\rm in}(a),G^{\rm in}(a))$。
实际边界条件是以下全部条件：

1. 低46高度决定参数 $a_j=Q^{\rm out}_{2j}(b)-Q_{2j,*}(b)$。
2. 全部 $|m|\ge94$ 高度满足
   $h_{\perp,\rm hi}^{\rm out}=h_{\perp,\rm hi}^{\rm in}(a)$。
3. 低46连接满足 $G_{\rm lo}^{\rm out}=G_{\rm lo}^{\rm in}(a)$。
4. 全部 $|m|\ge94$ 连接满足
   $G_{\rm hi}^{\rm out}=G_{\rm hi}^{\rm in}(a)$。
5. 统一的 mean 高度常数匹配；若它是全问题的自由平移规范，可一次
   选定，若已由固定几何约束确定，则保留一个相应的标量条件。

两侧 $G_0=0$ 都来自完整 mean 根。不存在另一个任意可选的 mean
斜率或 mean Dirichlet ODE；但也不能据此删掉第5项的实际位置条件。

**命题45.2。** 两侧真实背景相同、均满足 R41 的唯一正根域，且
上述完整条件成立，则两侧高度的全部二阶迹相同。若两侧确实解
完整 Darboux方程，其局部水平 development 经一次公共平面刚体
对齐后可按 $C^2$ 接合。

**证明。** 同一 $h_\perp$ 给同一 $P$ 及所有角导数，同一完整
$G$ 经 R41 唯一正根给同一 $K$，包括 mean。因此 $h_r$ 和
$h_{r\theta}$ 相同。式 (45.30)在同一真实 $r,w,w_r,E$ 下给同一
$h_{rr}$；第5项及角向微分给其余高度二阶迹。

水平 development 的一阶场由 R41 (41.36)–(41.38)和同一角frame
唯一确定。对齐一个切向frame和一个点后，一阶及二阶数据一致，
由 R32 的局部平直性构造得到 $C^2$ 拼接。各段所需经典正则性
可逐原 source光滑段使用，再凭公共迹通过接口。证毕。

本命题不给整面单射、reach、全时嵌入或全局拓扑证书。
有限 worker保存的 $\Pi$、canonical $\Xi$ 和完整 $G$ 分属不同
坐标，必须按同一实源的准确公式转换；不能直接用一个有限斜率
字段代替上述连接条件。

## 7. 连续外头 Schur 条件

R44 给真实半径上兼容保持的外头候选，其第一方程残差恒为零，
完整 mean由标量根补回；真实 Darboux缺陷及非线性响应都只进入
第二源列。喂给 Green 的 $\mathscr P_\perp(\mathcal J/L)$ 还须
支付 $L^{-1}$ 的 Wiener范数，实角上 $L>0$ 本身不够。
这些要求与下述抽象条件一并保留。

令 $a\in\mathbb R^{46}$，$x\in\mathcal X$ 表示实际外头未知场与
其它需要联解的高频、几何边界变量。空间 $\mathcal X$ 和残差空间
$\mathcal Y$ 必须是固定的 Banach空间，包含所选连续径向范数、
全部高频以及真实接口条件。外端哪些量已固定，由实际强前缀问题
决定；高频若由前缀求解吸收，就作为该问题的未知与方程，不能
在组装时擅自改为零。

将真实方程写成

$$
F(a,x)=\bigl(F_{\rm fin}(a,x),F_{\rm inf}(a,x)\bigr)=0,
\quad F_{\rm fin}\in\mathbb R^{46},\quad F_{\rm inf}\in\mathcal Y.
\tag{45.36}
$$

低浅高度关系可通过坐标/提升内置；46个有限行可以选为剩余低
连接条件。$F_{\rm inf}$ 保留连续外头方程和所有剩余高高度、
高连接、实际外端边界条件。若 mean位置或核心控制再增加有限
未知与约束，相应扩大有限块即可；不能以46为由删除它们。

参数化真头对 (45.36) 的贡献使用第4节准确迹导数 $B$，而不是
只取线性背景的逐模斜率。它一般耦合不同频率。

在一个实际候选处取有界线性参考

$$
\mathcal L=
\begin{pmatrix}A&B_1\\ C&D\end{pmatrix}:
\mathbb R^{46}\times\mathcal X\longrightarrow
\mathbb R^{46}\times\mathcal Y.
\tag{45.37}
$$

这里 $B_1$ 是外头算子的块名，不是第4节的迹提升 $B$。
假设真实连续块 $D$ 有有界逆，且

$$
\|D^{-1}\|\le\kappa_D,\qquad
S=A-B_1D^{-1}C,\qquad
\|S^{-1}\|\le\kappa_S.
\tag{45.38}
$$

这是外头连续问题所需的逆门。单个有限网格 Jacobian 的可逆性，
或 node12 的极小端点，并不提供 (45.38)。
Schur 消元给

$$
\delta a=S^{-1}(r-B_1D^{-1}s),\qquad
\delta x=D^{-1}(s-C\delta a),
\tag{45.39}
$$

故完整逆有非负两块上界

$$
\mathsf M=
\begin{pmatrix}
\kappa_S&\kappa_S\|B_1\|\kappa_D\\
\kappa_D\|C\|\kappa_S&
\kappa_D+\kappa_D\|C\|\kappa_S\|B_1\|\kappa_D
\end{pmatrix}.
\tag{45.40}
$$

可按径向胞元、频率或物理分量继续细分正块，证明不变。
R44的 $R\Phi(b,a)B$ 有限秩公式是相应边值选取下的直接实现；
使用全部频率时仍须先支付其固定 Banach空间有界性。

**定理45.3。** 假设定理45.1在所用参数域成立，R44的完整根、
连续残差和非线性定义域成立，并已支付 (45.38)。在候选
$y_0=(a_0,x_0)$ 周围给定正块半径 $r$，设

$$
|F(y_0)|_{\rm blocks}\le e,\qquad
|[DF(y)-\mathcal L]v|_{\rm blocks}\le
\mathsf E(r)|v|_{\rm blocks}
\tag{45.41}
$$

在整个盒中成立，且盒内参数仍在定理45.1的域中。
若

$$
\mathsf M e+\mathsf M\mathsf E(r)r<r,
\qquad
\max_i\frac{(\mathsf M\mathsf E(r)W)_i}{W_i}<1
\tag{45.42}
$$

对某个正权 $W$ 成立，则存在唯一盒内的完整外头与真实内头匹配解。
其高度满足完整 Darboux方程，并按命题45.2在 node12 二阶拼接。

**证明。** 在固定 Banach空间上使用
$\mathcal N(y)=y-\mathcal L^{-1}F(y)$。
由 (45.40)–(45.41)，中心残差不超过 $\mathsf M e$，导数不超过
$\mathsf M\mathsf E(r)$。沿线段积分给自映射条件，正权不等式给
严格收缩。Banach定理给唯一零点。由于 $F$ 按 (45.36)包含全部
连续方程与边界，零点没有丢掉高频迹。
R44完整 mean恒等式恢复 mean方程，命题45.2给二阶接合。证毕。

这里没有假设“每次损失一点解析宽度的逆”是一个固定空间的有界
算子。若外头证明使用变条带或各段不同归一，必须把这些选择固定
在 $\mathcal X,\mathcal Y$ 及 (45.41)中，再核实际有界性。

## 8. 当前可执行接线与尚待核销项

已明确并证明的接线顺序是：

1. 对 R43 的同一个完整核，加入 (45.3)–(45.6) 的46参数列，
   用实际428行门建立统一参数球及 (45.14)。
2. 以固定的 $\sigma=1/64$ 在 node12 得到 R44所需完整
   $(P,K_\perp)$、连接及全部polar二阶迹；mean位置规范只选一次。
3. 在真实外0..11上构造 R44兼容候选，连续包围真实第二源残差、
   全频外头核、准确参数迹导数和迹余项。
4. 以 (45.38)–(45.42)支付实际外头与强前缀边界问题；所有高频
   输出须进入同一联解，不另设未经授权的零边界。

第1项实际联合门与第3–4项当前仍未支付。第5节的小常数、R39
有限46辅助解或新g强M20有限响应均不能替代它们。
即使这些头部接合完成，课题还需全幅度、全时闭曲面、固定握持区、
全时reach及固定问题加密证据；本文不提前宣布课题完成。

## 引用

- R18、R26：准确深图、真实源函数和统一半径定义。
- R29、R42：真实线性列、有向 Green 与完整四核来源。
- R31–R33：真实背景曲率、完整高度发展、mean与全频源。
- R38、R39、R43：准确辅助中心及完整联合映射的条件。
- R41：完整连接唯一逆与真实单cut Darboux二阶迹。
- R44：兼容保持的真实外头候选、连续残差和两点核。
