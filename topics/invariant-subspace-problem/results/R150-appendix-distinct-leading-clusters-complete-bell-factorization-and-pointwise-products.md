# R150 附录：不同高次根簇的完整 Bell 分解、重复簇乘积与真实核运输

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。

状态：完整证明；根代理与 kernel_resume_1cf 已独立核查原 Bell 消失阶、Banach 解析分解及指定真实词域。本文接续[全部高次剪切与有界相伴部分](R150-appendix-all-polynomial-shears-fixed-complex-line-and-higher-companion-parts.md)，处理多个不同最高次中心同时存在的原普通点态多项式。不能由各点态因子分别循环直接推出它们的乘积循环；以下对原乘积的完整 Bell 实现作一次有限分核。

## 1. 原函数与一个有限系数条件

保持前稿的原函数范围。取
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
b\in\ell^2(\mathbb R),\quad |b_j|\le C_0a_j,\qquad
\psi\in\mathbb R.
$$
取复行 $d^0,d^1$ 满足
$$
d^\nu_j=0\quad(a_j=0),\qquad
\sum_{a_j>0}|d^\nu_j|^2/a_j<\infty,
$$
以及任意复 $e^0,e^1\in\ell^1$ 和复常数 $u_*,v_*,\gamma$。令
$$
u=u_*+\sum_j(a_j+d^0_j+e^0_j)\chi_j,\qquad
v=v_*+\sum_j(e^{i\psi}b_j+\gamma a_j+d^1_j+e^1_j)\chi_j.
\tag{1.1}
$$

固定整数 $k\ge2$。令标量 $F(x,y)$ 关于 $y$ 首一，次数为 $M\ge1$，并满足
$$
i+kj\le kM\qquad([x^iy^j]F\ne0).
\tag{1.2}
$$
因而
$$
\widehat F(t,s)=t^{kM}F(t^{-1},t^{-k}s)
=\sum_{q\ge0}t^qH_q(s)
\tag{1.3}
$$
是真正的有限多项式。假设
$$
H_0(s)=\prod_{\ell=1}^q(s-\kappa_\ell)^{m_\ell},
\quad
\kappa_\ell\ne0,\quad
\kappa_\ell\ne\kappa_j\;(\ell\ne j),\quad
\sum_\ell m_\ell=M.
\tag{1.4}
$$
这里及以下，下标 $\ell$ 枚举根簇；(1.3) 中的 $q$ 只枚举 $t$ 次数。

对每个簇要求以下有限消失条件：
$$
\boxed{
H_q^{(j)}(\kappa_\ell)=0
\quad\text{只要 }q+j<m_\ell.
}
\tag{1.5}
$$
等价地，
$$
\boxed{
t^{m_\ell}\ \text{整除}\ 
\widehat F(t,\kappa_\ell+t z)
\quad\text{于 }\mathbb C[t,z].
}
\tag{1.6}
$$
等价性直接由有限 Taylor 展开给出；所以 (1.5) 不涉及未知算子域或收敛条件。

**定理 1。** 在 (1.1)—(1.5) 下，对每个 $\lambda\in\mathbb C$、整数 $r\ge1$ 和任意复 $\ell^2$ 第一阶指数权 $e^w$，
$$
\boxed{
[F(u,v)-\lambda]^r e^w
\text{ 对原实际 }A\text{ 循环。}
}
\tag{1.7}
$$
所有 $m_\ell$ 都允许大于1。本文没有要求最高根简单，也没有要求某一簇内部的首位平移互素。

## 2. 不同最高中心的普通点态乘积

一个直接可用的范围是
$$
F(x,y)=\prod_{\ell=1}^q G_\ell(x,y-\Psi_\ell(x)),
\tag{2.1}
$$
其中每个 $\Psi_\ell$ 的次数均为同一个 $k\ge2$，最高系数为 $\kappa_\ell\ne0$；$G_\ell(x,s)$ 关于 $s$ 首一，次数为 $m_\ell\ge1$，且
$$
i+(k-1)j\le(k-1)m_\ell
\qquad([x^is^j]G_\ell\ne0).
\tag{2.2}
$$
先设各 $\kappa_\ell$ 不同。

在第 $\ell$ 个簇处，
$$
x=t^{-1},\qquad y=\kappa_\ell t^{-k}+t^{-(k-1)}z.
$$
因为 $\Psi_\ell(x)-\kappa_\ell x^k$ 的次数至多 $k-1$，
$$
t^{k m_\ell}
G_\ell(t^{-1},\kappa_\ell t^{-k}+t^{-(k-1)}z-\Psi_\ell(t^{-1}))
=t^{m_\ell}J_\ell(t,z),
\tag{2.3}
$$
其中 $J_\ell$ 是真正的多项式。这准确来自 (2.2)；每个剩余 $t$ 次数都非负。

对 $j\ne\ell$，同一归一式是多项式，且在 $t=0$ 的值为
$$
(\kappa_\ell-\kappa_j)^{m_j}.
$$
所以 (2.1) 满足 (1.2)—(1.6)，最高符号为
$\prod(s-\kappa_\ell)^{m_\ell}$。定理1因而给
$$
\boxed{
\left[\prod_\ell G_\ell(u,v-\Psi_\ell(u))-\lambda\right]^r e^w
\text{ 对全部 }\lambda,r,w\text{ 循环。}
}
\tag{2.4}
$$

相同最高系数的因子可以先并为同一簇。确实，选定该簇内一个 $\Psi$，则
$$
G_j(x,y-\Psi_j(x))
=G_j(x,s+\Psi(x)-\Psi_j(x)),\qquad s=y-\Psi(x).
$$
差 $\Psi-\Psi_j$ 的次数至多 $k-1$，因此保持 (2.2) 的权。它们的乘积仍首一，新的 $s$ 次数是原次数之和。

所以 (2.4) 也允许任意多个相同最高系数的因子。只有不同最高系数之间才需要下面的分簇。

## 3. 实际算子输入及任意非零中心

记 $\mathfrak C=A'$。它是交换、范数闭的有界算子代数。

[复加权主行稿](R150-appendix-weighted-complex-main-real-controlled-skeleton-and-all-shear-powers.md) 给出真实闭第一阶算子
$$
Z=X_{a+d^0}+\omega,\qquad L=Z^{-1}\in\mathfrak C,\qquad
Y=e^{i\psi}X_b.
\tag{3.1}
$$
其中 $\omega$ 可固定为足够大的正数；$Z$ 最大增生、空谱，$L$ 有界、单射且拟幂零。所有所需实际 first 及其闭图与 $\mathfrak C$ 交换。

对任意固定 $\kappa\ne0$，令
$$
W_{k,\kappa}=(Y-\kappa Z^k)_{\rm can},\qquad
T_{k,\kappa}=W_{k,\kappa}L^{k-1}.
\tag{3.2}
$$
下标 can 指 R186 的规范最大闭图。$T_{k,\kappa}$ 闭，且其完整图与 $\mathfrak C$ 交换。在共同自然深域上，
$$
T_{k,\kappa}=YL^{k-1}-\kappa Z.
\tag{3.3}
$$

前稿对 $\kappa=1$ 已证明：对任意 $d\ge1$、任意 $B_j\in\mathfrak C$，
$$
\ker\left(T_{k,1}^d+\sum_{j<d}B_jT_{k,1}^j\right)
=\{0\}
\quad\text{于自然域 }\operatorname{Dom}T_{k,1}^d.
\tag{3.4}
$$
同一结论适用于每个 $\kappa\ne0$。只需将辅助骨架换为 $\kappa^{-1}Y$，它仍是一条固定复直线上的实受控骨架，然后乘上非零标量 $\kappa$：
$$
T_{k,\kappa}
=\kappa\bigl[(\kappa^{-1}Y-Z^k)_{\rm can}L^{k-1}\bigr].
$$
有限多个 $\kappa$ 可共用 (3.1) 的 $Z,L$；原共享位移 $\omega$ 的预算不依辅助行的控制常数，只需相应增大两符号 first 所用的 $c$。也可起初一次增大 $\omega$。

因此本文使用的准确输入是
$$
\boxed{
\ker Q(T_{k,\kappa})=\{0\}
\quad
\text{对任意自然首一 }Q,\ 
\text{任意有界 }\mathfrak C\text{ 系数及 }\kappa\ne0.
}
\tag{3.5}
$$
它不要求系数的有限谱，也不要求这些系数属于 $\mathcal A$。

## 4. 原完整 Bell 保持每一簇的消失阶

固定 $\lambda,r,w$，记
$$
D=rM,\qquad d_\ell=r m_\ell.
$$
首先保持原普通多项式
$$
J(x,y)=[F(x,y)-\lambda]^r.
$$
其归一式为
$$
t^{kD}J(t^{-1},t^{-k}s)
=[\widehat F(t,s)-\lambda t^{kM}]^r.
\tag{4.1}
$$
因为 $kM\ge m_\ell$，(1.6) 给出
$$
t^{d_\ell}\mid t^{kD}J(t^{-1},
\kappa_\ell t^{-k}+t^{-(k-1)}z).
\tag{4.2}
$$
其最高符号准确为
$$
H(s)=\prod_\ell(s-\kappa_\ell)^{d_\ell}.
\tag{4.3}
$$

对原 $u,v,w$ 构造全部联合 Bell 多项式
$$
P_{\rm old}(x,y)
=\sum_{p,q\ge0}
\frac{B_{pq}}{p!\,q!}\partial_x^p\partial_y^qJ(x,y),
\qquad B_{pq}\in\mathcal A,\quad B_{00}=I.
\tag{4.4}
$$
这是一项不删的原 Bell 式，不把它换成各个因子的 Bell 算子之积。

为核查 (4.2) 对全部导数保持，固定一个 $\kappa=\kappa_\ell$ 和 $N=kD$，记
$$
\mathcal T_N K(t,z)
=t^N K(t^{-1},\kappa t^{-k}+t^{-(k-1)}z).
$$
准确微分恒等式为
$$
\boxed{
\mathcal T_N(\partial_x K)
=\bigl[Nt-t^2\partial_t-((k-1)tz+k\kappa)\partial_z\bigr]\mathcal T_NK,
}
\tag{4.5}
$$
$$
\boxed{
\mathcal T_N(\partial_y K)
=t^{k-1}\partial_z\mathcal T_NK.
}
\tag{4.6}
$$
这里两次均保持同一个 $N$。右侧的每一项保持理想
$t^{d_\ell}\mathfrak C[t,z]$，所以任意混合 Bell 导数都保持消失阶 $d_\ell$。

在原权 $\operatorname{wt}x=1,\operatorname{wt}y=k$ 下，非零导数项严格降权。因此 (4.4) 仍满足权不超过 $kD$、关于 $y$ 首一，其最高符号准确是标量多项式 (4.3)。

### 4.1 实际有界坐标代换也保持消失阶

把原两个倾斜 first 准确写到 (3.1)：
$$
x_{\rm old}=Z+H,\qquad
y_{\rm old}=Y+RZ+K,\qquad H,K,R\in\mathfrak C.
\tag{4.7}
$$
全部系数有界且互相交换；这是前述复加权主行稿已经支付的完整 first 域等式。

设
$$
P(x,y)=P_{\rm old}(x+H,y+Rx+K).
\tag{4.8}
$$
在每个实际共同深域上，它正是最初规范 Bell 算子的核心表达式。

有限 Taylor 公式给
$$
P_{\rm old}(x+H,y+Rx+K)
=\sum_{p,q}
\frac{H^p(Rx+K)^q}{p!\,q!}
\partial_x^p\partial_y^qP_{\rm old}(x,y).
\tag{4.9}
$$
代入簇坐标后，$\partial_y^q$ 的 $t^{(k-1)q}$ 与 $(Rx+K)^q$ 合成
$$
(Rt^{k-2}+Kt^{k-1})^q.
\tag{4.10}
$$
由于 $k\ge2$，这里没有负幂；其余 $\partial_x$ 用 (4.5)。所以 (4.8) 仍保持每个 $t^{d_\ell}$ 消失阶。

有界 $x$ 平移和 $y\mapsto y+Rx+K$ 都严格降低最高权修正，也保持关于 $y$ 的首一性。于是
$$
\widehat P(t,s)=t^{kD}P(t^{-1},t^{-k}s)\in\mathfrak C[t,s]
\tag{4.11}
$$
关于 $s$ 首一、次数为 $D$，并准确满足
$$
\widehat P(0,s)=\prod_\ell(s-\kappa_\ell)^{d_\ell},
\qquad
t^{d_\ell}\mid\widehat P(t,\kappa_\ell+t z).
\tag{4.12}
$$

## 5. 在有界交换代数中的解析分簇

本节只是有限系数 Banach 代数运算，不对无界算子作解析函数演算。

令
$$
H_\ell(s)=(s-\kappa_\ell)^{d_\ell},\qquad H=\prod_\ell H_\ell.
$$
取有限系数空间
$$
E=\bigoplus_\ell\mathfrak C[s]_{<d_\ell},
\qquad V=\mathfrak C[s]_{<D}.
$$
线性映射
$$
\mathcal L(v_1,\ldots,v_q)
=\sum_\ell v_\ell\prod_{j\ne\ell}H_j
\tag{5.1}
$$
由一个有限标量矩阵给出。因标量 $H_\ell$ 两两互素，该矩阵可逆：若其输出为零，模 $H_\ell$ 后得到 $v_\ell=0$，再由维数相同得到满射。其标量逆矩阵也在 $E,V$ 上给出有界逆。

写
$$
\prod_\ell(H_\ell+v_\ell)
=H+\mathcal Lv+\mathcal N(v),
$$
其中 $\mathcal N$ 是至少二次的有限多项式映射。求
$$
v=\mathcal L^{-1}\bigl[\widehat P(t,\cdot)-H-\mathcal N(v)\bigr].
\tag{5.2}
$$
先选充分小的固定系数球，使 $\mathcal L^{-1}\mathcal N$ 在该球上 Lipschitz 常数小于 $1/2$；再令 $|t|$ 充分小，使右侧把此球映入自身。

从 $v=0$ 开始的逐次代入一致几何收敛。每一步关于复 $t$ 解析，局部一致极限也解析。因此存在 $\varepsilon>0$ 和首一有限 $s$ 多项式
$$
P_\ell(t,s)\in\operatorname{Hol}(|t|<\varepsilon;\mathfrak C)[s],
\qquad\deg_sP_\ell=d_\ell,
$$
使
$$
\boxed{
\widehat P(t,s)=\prod_\ell P_\ell(t,s),\qquad
P_\ell(0,s)=H_\ell(s).
}
\tag{5.3}
$$
这给出了所用局部分解的完整构造；不需要假设一般 Banach 代数具有标量多项式的分根性质。

### 5.1 每个因子仍具有自己的准确消失阶

固定 $\ell$。对 $j\ne\ell$，
$$
P_j(0,\kappa_\ell)
=(\kappa_\ell-\kappa_j)^{d_j}I
$$
是非零标量单位。因此在形式环 $\mathfrak C[z][[t]]$ 中，
$$
\prod_{j\ne\ell}P_j(t,\kappa_\ell+t z)
$$
有逆。由 (4.12)、(5.3) 得
$$
t^{d_\ell}\mid P_\ell(t,\kappa_\ell+t z).
$$
各个 $z$ 系数本来就解析，前 $d_\ell$ 个 $t$ 系数为零，所以
$$
\boxed{
Q_\ell(t,z)=t^{-d_\ell}P_\ell(t,\kappa_\ell+t z)
}
\tag{5.4}
$$
在 $t=0$ 可去奇点，并是解析系数的首一 $z$ 多项式，次数恰为 $d_\ell$。

式 (5.4) 中的除法已经在有界系数的解析函数中完成；后面不会代入任何负次 $L$。

### 5.2 有限 Bézout 系数

把 (5.1) 的 $H_j$ 换为 $P_j(t,s)$。其有限矩阵在 $t=0$ 为已知单位，所以在缩小后的圆盘内，Neumann 级数给出解析逆矩阵。将该逆作用于常数多项式1，得到
$$
E_\ell(t,s)\in\operatorname{Hol}(|t|<\varepsilon;\mathfrak C)[s],
\qquad\deg_sE_\ell<d_\ell,
$$
且
$$
\boxed{
\sum_\ell E_\ell(t,s)\prod_{j\ne\ell}P_j(t,s)=1.
}
\tag{5.5}
$$

## 6. 仅在有界拟幂零 $L$ 上代入解析系数

若 $C(t)=\sum_{n\ge0}C_nt^n$ 在某个原点圆盘内解析，系数 $C_n\in\mathfrak C$，定义
$$
C[L]=\sum_{n\ge0}C_nL^n.
\tag{6.1}
$$
因 $L$ 拟幂零，$\|L^n\|^{1/n}\to0$；而任一更小圆盘的 Cauchy 系数界给 $\|C_n\|\le C\rho^{-n}$。所以 (6.1) 在算子范数中绝对收敛，不要求 $\|L\|<\varepsilon$。

所有系数与 $L$ 交换，绝对收敛的 Cauchy 乘积说明 (6.1) 是代数同态。记
$$
p_\ell(s)=P_\ell[L](s),\qquad
e_\ell(s)=E_\ell[L](s),\qquad
q_\ell(z)=Q_\ell[L](z).
$$
它们都是只有有限个 $s$ 或 $z$ 次数的 $\mathfrak C$ 系数多项式，并准确满足
$$
\widehat P[L](s)=\prod_\ell p_\ell(s),
\qquad
\sum_\ell e_\ell(s)\prod_{j\ne\ell}p_j(s)=I,
\tag{6.2}
$$
$$
\boxed{
p_\ell(\kappa_\ell I+Lz)=L^{d_\ell}q_\ell(z),
\qquad q_\ell\text{ 首一、次数 }d_\ell.
}
\tag{6.3}
$$
(6.3) 来自已经可去奇点的 (5.4)，不是形式除以 $L^{d_\ell}$。

### 6.1 解析系数确实保持已付的真实词域

(6.1) 的每个极限仍属于范数闭代数 $\mathfrak C=A'$。R186 的每个实际单 first 闭图与整个 $\mathfrak C$ 交换，所以这些极限保持其完整定义域。

也可直接检查极限步骤：若 $C_n\to C$ 为算子范数收敛、$X$ 为其中一个闭 first、且 $XC_nx=C_nXx$，则
$$
C_nx\to Cx,\qquad XC_nx\to CXx.
$$
$X$ 的闭性给 $Cx\in\operatorname{Dom}X$ 和 $XCx=CXx$。再逐个 first 归纳，得到同一系数保持每一个已付有限混合词域。

因此解析分解没有引入新的未付无界域。下面只在指定深输入上作用有限多项式；不形成无界 $S$ 的无限幂级数。

## 7. 同一个正则器将原规范核送入所有有限分核运算

设原普通向量 (1.7) 的规范最大 Bell 实现为 $\mathcal P$。假设
$$
0\ne f\in\ker\mathcal P.
$$
取 [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) 对本文全部有限 first 族的同一个单射共同正则器 $\mathcal R\in\mathfrak C$。

选有限 $N\ge k(3D+2)$，必要时再按原有限族的具体展开增加固定深度，使
$$
h=\mathcal R^Nf
\tag{7.1}
$$
进入全部长度不超过 $N$ 的所需真实混合词域。$\mathcal R$ 单射给 $h\ne0$，而原规范图的交换性给
$$
\mathcal Ph=0.
\tag{7.2}
$$
在此输入上，$\mathcal P$ 的作用准确等于 §4 的 $P(Z,Y)$。

在指定深域上简记
$$
S=YL^k.
$$
这只是有限自然运算的记号；本文不需要给整个 $S$ 另取闭扩张。由 $ZL=LZ=I$ 的真实逆恒等式，
$$
\widehat P[L](S)h=L^{kD}P(Z,Y)h=0.
\tag{7.3}
$$
每个 $L$ 次数都非负：一个原项 $Z^iY^j$ 对应
$L^{kD-i-kj}S^j$，而 (1.2)、(4.11) 给 $kD-i-kj\ge0$。

令
$$
h_\ell=e_\ell(S)\prod_{j\ne\ell}p_j(S)h.
\tag{7.4}
$$
由 (6.2)，
$$
\boxed{\sum_\ell h_\ell=h.}
\tag{7.5}
$$
同一有限多项式恒等式和 (7.3) 给
$$
\boxed{p_\ell(S)h_\ell=0.}
\tag{7.6}
$$

这里的域预算可以逐项数清：

- (7.4) 的 $S$ 次数至多 $D-1$；每次 $S=YL^k$ 只消耗一个 first 词长度，全部有界系数保持剩余域。
- (7.6) 的原多项式恒等式只需至多 $2D-1$ 次 $Y$ 作用。
- 对 $h_\ell$ 再作用 $T_{k,\kappa_\ell}^{d_\ell}$，每一步在深域中至多消耗 $k$ 个 first；总计至多 $(D-1)+kd_\ell$。
- 原 $P(Z,Y)$ 的词长度不超过 $kD$。

所以 (7.1) 选定的有限深度同时覆盖所有分核和随后自然相伴幂。没有在产生 $h_\ell$ 后假定一个未经核查的定义域不变性。

## 8. 每一簇落入已知无核的自然首一多项式

在这些已付词域上，(3.3) 给
$$
\boxed{
S=\kappa_\ell I+L T_{k,\kappa_\ell}.
}
\tag{8.1}
$$
所有有界系数与 $T_{k,\kappa_\ell}$ 的完整图交换。逐次使用其规范作用在共同自然域上的准确表达，得到
$$
h_\ell\in\operatorname{Dom}T_{k,\kappa_\ell}^{d_\ell}.
$$
于是将 (8.1) 代入有限多项式恒等式 (6.3)，在这个指定输入上准确有
$$
0=p_\ell(S)h_\ell
=L^{d_\ell}q_\ell(T_{k,\kappa_\ell})h_\ell.
\tag{8.2}
$$
$L$ 单射，所以
$$
q_\ell(T_{k,\kappa_\ell})h_\ell=0.
$$
$q_\ell$ 关于自然 $T_{k,\kappa_\ell}$ 首一，全部系数有界且属于 $\mathfrak C$。因此 (3.5) 给 $h_\ell=0$，对每个 $\ell$ 成立。

由 (7.5) 得 $h=0$，与 (7.1) 的单射性矛盾。故
$$
\ker\mathcal P=\{0\}.
$$
R186 在原完整空间上的 $C$ 自伴性给 $\overline{\operatorname{Ran}\mathcal P}=H$。原指数向量 $e^w$ 的循环图核心再给
$$
[\mathcal Pe^w]_A=\overline{\operatorname{Ran}\mathcal P}=H.
$$
而 $\mathcal Pe^w$ 正是未改动的原普通点态向量 (1.7)。定理1及 (2.4) 得证。

全证明没有把原 $\operatorname{Dom}\mathcal P$ 等同于任何一个 $\operatorname{Dom}T_{k,\kappa_\ell}^{d_\ell}$。使用的是一个真实单射正则器、有限个有界系数和指定深输入上的有限分核。

## 9. 一个同时含两个重复最高簇的实例

取任意 $1/2<\sigma\le1$，
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=i\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j.
$$
置
$$
F(x,y)=\bigl[(y-x^2)^2-4x^2\bigr]
       \bigl[(y+x^2)^2-4x^2\bigr].
$$
它的最高符号为
$$
H_0(s)=(s-1)^2(s+1)^2.
$$
两个簇均为重簇；各自都容许旧二次剪切的真实首位碰撞。本文给
$$
\boxed{
\left[
\bigl((v-u^2)^2-4u^2\bigr)
\bigl((v+u^2)^2-4u^2\bigr)-\lambda
\right]^r e^w
\text{ 对全部 }\lambda,r,w\text{ 循环。}
}
$$
这不是把两个已循环向量相乘的推论。常数移位 $\lambda$ 与外部点态幂均在原完整 Bell 中一起处理。

## 10. 与旧结果的关系及剩余条件

[不同最高根簇的跨核排斥](R150-appendix-disjoint-leading-roots-cross-kernel-exclusion-and-real-structure.md)证明两个最高符号互素的独立规范算子不能同时有非零核，并在实结构下排除部分单核。它没有将一个普通点态乘积的完整 Bell 核分成若干核；其正文也明确不从因子循环推乘积循环。

[全部高次剪切稿](R150-appendix-all-polynomial-shears-fixed-complex-line-and-higher-companion-parts.md)处理一个最高中心及其全部平衡余项。本文在它的任意有界交换系数自然首一无核结论上，新增多个不同最高中心之间的完整 Bell 分簇。最高根简单的交集范围按此前 Newton 结果扣除，新增包含 §9 的多个重复簇。

(1.5) 是本定理的充分条件，不声称必要。例如
$$
F(x,y)=(y-x^k)^m+x^{km-1},\qquad m>1,
$$
满足原权界，但
$$
\widehat F(t,1+t z)=t^m z^m+t
$$
不满足所需 $t^m$ 消失阶。它不能由本文的分簇定理处理，失败也不表示它有非零核。

本文还不包括零最高根簇、任意不同次数中心的混合，以及模去
$\mathbb C a+\ell^1+\ell^2(a^{-1})$ 后不落在一条固定复直线的辅助骨架。真正常见证的专属聚合上界、一般慢主理想和普通复 Hilbert ISP 继续保持未完成状态。
