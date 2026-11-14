# 边界有限真实头的定量 Jordan 相似与纯尾模型的形式像闭包

日期：2026-11-12。独占作者：critical_kernel。

**状态：完整证明。** 本稿中的 $T$、$H_m$ 都指负整数边界表示中的有界慢符号，绝不指 R236 的原 Haar 无界中央算子。两个独立结论为：

1. 两个实际慢边界符号的前 $m$ 位真实头，可以化为单 Jordan 链；$m\ge3$ 时相似条件数不超过 $\exp(221\,16^{m-1})$。
2. 对任意有限循环幂零头加纯尾删除模型，只要一个形式向量的每个尾孔次数层分别在 Hilbert 空间中，而且其形式伴随像是 Hilbert 向量，则该像属于真实伴随像的闭包。

第二个结论不要求形式原像全局平方可和。最后给出相似后真实进位余项的预算，并指出动态改变头长度时尚需控制的具体截断项。不宣称由此已证明边界 $N=M$ 或原 Haar 慢核为零。

## 1. 实际有限头与权恒等式

在
$$
\mathcal H_-=\ell^2(\mathbb N_0),\qquad
Be_n=\alpha_{v_2(n)}e_{n-1},\quad Be_0=0
$$
中，记
$$
W_0=1,\qquad W_n=\prod_{\ell=1}^n\alpha_{v_2(\ell)},\qquad
d_i=W_{2^i}.
$$
本题的实际权满足
$$
W_n=\prod_{i\in\operatorname{bits}(n)}d_i,\qquad d_0=e^{-20},
$$
$$
\Lambda_i:=-\log d_i
=100\,16^i-105\,8^i+(150i+25)2^i
\le100\,16^i.
\tag{1.1}
$$

固定 $a_i=(i+1)^{-2}$。取 $m\ge3$、$D=2^m$，令 $B_m$ 为 $B$ 在
$\operatorname{span}\{e_0,\ldots,e_{D-1}\}$ 上的真实有限头。
分别定义
$$
F_{N,m}(z)=\sum_{i<m}a_i\frac{z^{2^i}}{d_i},
$$
$$
F_{Y,m}(z)=\sum_{i<m}a_i\frac{z^{2^i}}{d_i+z^{2^i}}.
\tag{1.2}
$$
在第二式中只需要零点附近的真解析芽；对幂零矩阵代入等于其有限 Taylor 截断。

固定其中之一，简写 $F_m$，并令
$$
H_m=F_m(B_m).
\tag{1.3}
$$
这是实际慢符号在前 $m$ 位上的真实头，不是把其中的低位 carry 删除。
两模型均有
$$
F_m(0)=0,\qquad F_m'(0)=d_0^{-1}\ne0,\qquad
\|H_m\|<6.
\tag{1.4}
$$
最后一个粗界来自 $\|\mathsf N_i^{[m]}\|\le1$、
$\|\mathsf Y_i^{[m]}\|\le3$ 和 $\sum_i a_i<2$。

因此 $H_m$ 是指数恰为 $D$ 的循环幂零矩阵。

## 2. 更大的实际小圆盘

取
$$
\boxed{\rho_m=\exp(-110\,8^{m-1}).}
\tag{2.1}
$$
它比 R238 用于全参数递推的保守圆盘更大；本节单独证明所需界。

### 2.1 无极点与低位控制

对 $1\le i<m$，
$$
\frac{\rho_m^{2^i}}{d_i}
\le
\exp\!\left(100\,16^i-110\,8^{m-1}2^i\right)
\le e^{-10\,16^i}<\frac12.
\tag{2.2}
$$
最低位也有 $\rho_m<d_0/2$。所以两个模型在 $|z|\le\rho_m$ 上都解析，
Cayley 模型的全部分母均不为零。

记 $G_m(z)=F_m(z)/z$。对 $2\le i<m$，
$$
\begin{aligned}
\log\frac{\rho_m^{2^i-1}}{d_i}
&\le \Lambda_i-110\,8^i(2^i-1)\\
&=-10\,16^i+5\,8^i+(150i+25)2^i.
\end{aligned}
\tag{2.3}
$$
除以 $16^i$ 后，右侧为
$$
-10+\frac5{2^i}+\frac{150i+25}{8^i}.
$$
后两个正项从 $i=2$ 起递减；$i=2$ 时 (2.3) 正好为 $-940$。
因此
$$
\frac{\rho_m^{2^i-1}}{d_i}
\le
\exp\!\left(-\frac{235}{64}\,16^i\right)
\qquad(i\ge2).
\tag{2.4}
$$
对 $i=1$，$m\ge3$ 给
$$
\Lambda_1-110\,8^{m-1}
\le1110-7040=-5930.
\tag{2.5}
$$
这些界在 $i$ 上显然可和。

在 $\mathsf N$ 模型中，$G_m$ 的最低项就是 $d_0^{-1}$。
在 $\mathsf Y$ 模型中，该项为 $(d_0+z)^{-1}$，其差满足
$$
\left|(d_0+z)^{-1}-d_0^{-1}\right|
\le2\rho_m/d_0^2.
$$
其余 Cayley 项只需在 (2.4)–(2.5) 之外再乘 $2$。于是两模型统一有
$$
\boxed{
|G_m(z)-d_0^{-1}|<1
\qquad(|z|\le\rho_m).
}
\tag{2.6}
$$

### 2.2 逆芽的真实解析圆盘

置
$$
r_m=\frac{\rho_m}{2d_0}.
$$
若 $|w|\le r_m$，在 $|z|=\rho_m$ 上，
$$
|F_m(z)-z/d_0-w|
\le\rho_m+\rho_m/(2d_0)
<\rho_m/d_0.
$$
Rouché 定理因此给出 $F_m(z)-w$ 在该圆盘内恰有一个零，按重数计。
它必为单零，随 $w$ 解析变化。故零点附近的逆芽
$$
\psi_m=F_m^{-1}
$$
实际在闭圆盘 $|w|\le r_m$ 的某个邻域中解析，并满足
$$
\boxed{
|\psi_m(w)|\le\rho_m\qquad(|w|\le r_m).
}
\tag{2.7}
$$
于是对全部整数 $k,n\ge0$，
$$
\left|[w^k]\psi_m(w)^n\right|
\le \rho_m^n r_m^{-k}
=(2d_0)^k\rho_m^{n-k}.
\tag{2.8}
$$
当 $k<n$ 时该系数为零；$n=0$ 时除 $k=0$ 外也严格为零。
本节始终是有限真实解析函数，没有对无限形式 $F$ 使用 Cauchy 公式。

## 3. 链基、逆矩阵及 $221$ 常数

令 $J_D$ 为无权后移 Jordan 矩阵：
$$
J_De_k=e_{k-1}\quad(k\ge1),\qquad J_De_0=0.
$$
定义可逆链基矩阵 $K_m$：
$$
K_me_k=(H_m^*)^ke_0,\qquad 0\le k<D.
\tag{3.1}
$$
由于 $H_m^*K_m=K_mJ_D^*$，
$$
H_m=K_m^{-*}J_DK_m^*.
\tag{3.2}
$$
这里 $K_m^{-*}=(K_m^{-1})^*$。若记 $V_m=K_m^{-*}$，
则 $H_m=V_mJ_DV_m^{-1}$。

由 (1.4)，
$$
\|K_m\|
\le\left(\sum_{k=0}^{D-1}\|(H_m^*)^ke_0\|^2\right)^{1/2}
\le\sqrt D\,6^{D-1}.
\tag{3.3}
$$

### 3.1 逆矩阵的准确权位置

把一个有限头向量 $h$ 写成普通形式多项式
$$
\sum_{n<D}\frac{h_n}{W_n}z^n.
$$
$H_m^*$ 对应乘以 $F_m(z)$，模 $z^D$。
因此链基的矩阵为
$$
K_m=D_W C_{F_m},\qquad D_W=\operatorname{diag}(W_0,\ldots,W_{D-1}),
\tag{3.4}
$$
其中 $C_{F_m}$ 是截断复合 $p(z)\mapsto p(F_m(z))$ 的矩阵。
于是
$$
K_m^{-1}=C_{\psi_m}D_W^{-1},
$$
$$
(K_m^{-1})_{kn}
=\frac{[w^k]\psi_m(w)^n}{W_n}.
\tag{3.5}
$$
分母是输入列的 $W_n$，不是输出行的 $W_k$。

### 3.2 不能把两个最坏成本独立相加

对 $0\le n\le k<D$，结合 (2.8) 和 $2d_0<1$，
$$
\begin{aligned}
\log\!\left(W_n^{-1}\rho_m^{n-k}\right)
&=110\,8^{m-1}k\\
&\quad+\sum_{i\in\operatorname{bits}(n)}
\left(\Lambda_i-110\,8^{m-1}2^i\right).
\end{aligned}
\tag{3.6}
$$
每个括号都非正，因为 $i<m$ 且
$$
\Lambda_i\le100\,16^i
=100\,8^i2^i
\le100\,8^{m-1}2^i.
$$
所以
$$
\log\!\left(W_n^{-1}\rho_m^{n-k}\right)
\le110\,8^{m-1}k
<220\,16^{m-1}.
\tag{3.7}
$$
这正是保留真实二进制权位置的作用。若独立取 $W_n^{-1}$ 和逆芽系数的最大值，会支付一个不需要的额外损失。

由 (3.5)–(3.7)，
$$
\|K_m^{-1}\|\le D\,e^{220\,16^{m-1}}.
\tag{3.8}
$$
结合 (3.3)，
$$
\log\bigl(\|K_m\|\,\|K_m^{-1}\|\bigr)
\le220\,16^{m-1}
+\frac32\log D+(D-1)\log6.
$$
对 $D=2^m\ge8$，
$$
\frac32\log D+(D-1)\log6<4D\le D^4/16=16^{m-1}.
$$
因此
$$
\boxed{
\|V_m\|\,\|V_m^{-1}\|
=\|K_m\|\,\|K_m^{-1}\|
\le e^{221\,16^{m-1}}\qquad(m\ge3).
}
\tag{3.9}
$$

这同时适用于 $T_N$ 和 $T_Y$ 的真实有限头。有限的 $m=1,2$ 如需使用，可另吸收入一个绝对常数；本稿所有渐近应用只取 $m\ge3$。

## 4. 有限循环幂零头加纯尾的形式像闭包

本节可独立于第 1–3 节使用。

设 $\mathcal F$ 是一个 $D$ 维空间，$H$ 是其上的循环幂零矩阵。
取任意有界可逆 $V$ 使
$$
H=VJ_DV^{-1}.
$$
纯尾空间按孔次数正交分级：
$$
\mathcal K=\bigoplus_{q\ge0}\mathcal K_q.
$$
设 $D_{\rm tail}$ 为一个有界纯孔删除算子，
$$
D_{\rm tail}\mathcal K_q\subset\mathcal K_{q-1}.
$$
在本题中可取 $D_{\rm tail}=\sum_{j\ge m}a_jE_j$；$a\in\ell^1$ 保证它有界。

定义
$$
T_0=H\otimes I+I\otimes D_{\rm tail}.
\tag{4.1}
$$
称 $h=(h_q)_{q\ge0}$ 为逐尾次数 Hilbert 形式向量，如果
$$
h_q\in\mathcal F\otimes\mathcal K_q
$$
对每个固定 $q$ 成立，而不要求 $\sum_q\|h_q\|^2<\infty$。
$T_0^*h$ 逐层有意义：其第 $q$ 层仅涉及 $h_q$ 与 $h_{q-1}$。

**定理 4.1。** 若这样的形式向量满足
$$
T_0^*h=y
$$
逐层成立，且 $y$ 真正属于 $\mathcal F\otimes\mathcal K$，则
$$
\boxed{y\in\overline{\operatorname{Ran}T_0^*}.}
\tag{4.2}
$$
特别，若又 $T_0y=0$，则 $y=0$。

### 4.1 完整证明

令 $\mathcal V=V\otimes I$，并置
$$
A=J_D\otimes I+I\otimes D_{\rm tail},\qquad
h'=\mathcal V^*h,\qquad y'=\mathcal V^*y.
$$
$\mathcal V$ 只作用于有限头，因此 $h'$ 仍逐尾次数属于 Hilbert 空间，
$y'\in H$，且
$$
A^*h'=y'.
\tag{4.3}
$$

给无权 Jordan 头的 $e_i$ 赋级 $i$，把“头链指标 $i$ 加尾孔数 $q$”作为总次数。
记其第 $g$ 层投影为 $P_g$。每个 $P_gh'$ 只由至多 $D$ 个尾次数层组成，
所以真正属于 Hilbert 空间。

$A^*$ 在这个分级中严格升一次：
$$
A^*P_gH\subset P_{g+1}H.
$$
因此 (4.3) 等价于
$$
P_0y'=0,\qquad P_gy'=A^*P_{g-1}h'\quad(g\ge1).
$$
对任意 $Q\ge1$，
$$
\sum_{g=0}^QP_gy'
=
A^*\left(\sum_{g=0}^{Q-1}P_gh'\right).
\tag{4.4}
$$
括号是有限个真实 Hilbert 向量的和，所以右侧在真正的 $\operatorname{Ran}A^*$ 中。
左侧随 $Q\to\infty$ 在 Hilbert 范数中趋向 $y'$，因而
$y'\in\overline{\operatorname{Ran}A^*}$。

又因
$$
T_0^*=\mathcal V^{-*}A^*\mathcal V^*,
$$
且 $\mathcal V^*$ 全域可逆，
$$
\operatorname{Ran}T_0^*=\mathcal V^{-*}\operatorname{Ran}A^*.
$$
有界可逆变换保持闭包，得到 (4.2)。
若 $T_0y=0$，则 $y\perp\overline{\operatorname{Ran}T_0^*}$，与 (4.2) 合并得 $y=0$。证毕。

### 4.2 显式真实像逼近

证明还给出实际向量
$$
h^{(Q)}=\mathcal V^{-*}\sum_{g=0}^{Q-1}P_gh',
$$
满足
$$
T_0^*h^{(Q)}
=\mathcal V^{-*}\left(\sum_{g=0}^QP_g\right)\mathcal V^*y
\longrightarrow y.
\tag{4.5}
$$
没有要求 $(h^{(Q)})$ 有界，也没有对未知形式 $h$ 使用闭图定理。

对固定 $m$ 的实际有限头，(3.9) 使 (4.5) 的输出截断算子范数不超过
$e^{221\,16^{m-1}}$。这个数只控制固定头的真实像逼近成本。

## 5. 相似后真实 carry 的可用预算

R234 的实际局部差分解给
$$
T=T_0^{(m)}+E_m,\qquad
T_0^{(m)}=H_m\otimes I+\sum_{j\ge m}a_jE_j,
$$
$$
E_m=\sum_{L\ge m}K_L,\qquad
\|K_L\|\le52e^{-770\,16^{L-1}}.
\tag{5.1}
$$
$K_L$ 只作用于前 $L+1$ 位。
该式是实际算子差，而非在形式级数中丢掉高位。

由超几何尾，
$$
\|E_m\|\le104e^{-770\,16^{m-1}}.
\tag{5.2}
$$
用 $\mathcal V_m=V_m\otimes I$ 作第 3 节相似变换，
$$
\boxed{
\|\mathcal V_m^{-1}E_m\mathcal V_m\|
\le104e^{-549\,16^{m-1}}.
}
\tag{5.3}
$$
若某个已经证明的估计只额外支付 $r$ 个相似条件数，则数值预算为
$$
\kappa(V_m)^r\|E_m\|
\le104e^{-(770-221r)16^{m-1}}
\qquad(r=1,2,3).
\tag{5.4}
$$
右侧对这三个固定 $r$ 均趋零。

式 (5.4) 只是可用预算。不能由“还有正余量”直接省略其具体目标范数、形式配对收敛或移动截断项。

## 6. 动态头长度仍需控制的明确边界

第 4 节对每个固定 $m$ 都成立。但真实缺陷向量满足的是
$$
Tf=0,\qquad T^*h=f\ \text{逐行},
$$
不是同一个 $T_0^{(m)}$ 的两条方程。

此外，(4.5) 的投影在原 Hilbert 度量中一般不正交。
令
$$
\Theta_{m,Q}
=\mathcal V_m^{-*}
\left(\sum_{g=0}^QP_g\right)\mathcal V_m^*.
$$
则
$$
\|\Theta_{m,Q}\|\le\kappa(V_m).
\tag{6.1}
$$
因为 $\mathcal V_m$ 只改有限头，若一个向量的尾孔次数不超过
$Q-(D-1)$，则 $\Theta_{m,Q}$ 在它上面严格为恒等；若尾孔次数大于 $Q$，
则该向量被严格杀掉。
因此
$$
\|(\Theta_{m,Q}-I)y\|
\le
(1+\kappa(V_m))
\left\|\mathbf1_{\{\text{尾孔数}>Q-D+1\}}y\right\|.
\tag{6.2}
$$

对固定 $m$，(6.2) 足以给强收敛；对随 $Q$ 增长的 $m(Q)$，却需要另证右侧趋零。
一个任意 Hilbert 向量的尾没有已知速度，不能把
$\kappa(V_{m(Q)})\to\infty$ 与未定速度的尾直接相乘后宣布收敛。

R239 及其优化可使缺陷形式原像的各孔层增长大幅降低；
(3.9)、(5.3) 则使动态头相似的常数明显小于实际 carry 衰减。
这些是可组合的真实输入。尚待付清的是同一实际缺陷向量上的能量或移动度量截断，
而不是再把纯模型的定性结论直接传到实际模型。
