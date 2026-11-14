# 原线性大孔窗口、全序列 Legendre 预算与加权最小修复能量

日期：2026-11-13（UTC）。作者：boundary_next。状态：完整实际中间证明；普通 ISP 与无权 $N=M$ 仍未完成。

[R254 第十二附录](../results/R254-appendix-factorial-preimages-carry-jets-and-large-low-output-windows.md) 已给阶乘相容原像、局部 carry 的指数导数范数与平方模型的大窗口低输出近似；[R271](../results/R271-increasing-head-actual-lift-and-log-four-thirds-stable-range.md) 已用逐头升级闭合真实提升，证明了 $4/3$ 次对数权饱和。本稿不重复登记该权阶。

这里独立把两条新接口应用于原 $T$ 的线性模型 $L_m=A_m+D_m$，使用原物理位号 $\eta_{m-1}$，没有移用平方图的提升。再保留原线性单层残量的合并头幂，优化四次预算，并对每个大整数 $q$ 选择头长。所得严格增量为：

1. 原线性大窗口投影和原 Hilbert 范数的逐头稳定像提升；
2. 饱和系数 $c>K_*=3(16/770)^{1/3}=0.8247664896\ldots$，非零真缺陷的全序列必要尾常数 $K_*/2$，不付稀疏网格的额外 $16$ 倍；
3. 对全部整数孔层的原最小修复能量，给加权覆盖/Bessel 不等式和正凸平均判据。

最后一个能量级数是否对所有实际核向量发散仍未知。一般 Hilbert 尾不能替代这项证明。

## 1. 原物理线性模型

沿用 [R239 原线性修复](../results/R239-appendix-direct-linear-boundary-repair-and-stable-lift.md) 的原边界记号：
$$
T=\sum_{j\ge0}(j+1)^{-2}N_j
\quad\hbox{或}\quad
T=\sum_{j\ge0}(j+1)^{-2}Y_j,\qquad
Y_j=N_j(I+N_j)^{-1},
$$
$$
M=\ker T,\qquad N=\overline{BM},\qquad D_{\rm def}=M\ominus N.
$$
头包含原物理位 $0,\ldots,m-1$，不是删除原首位后的图尾。令
$$
m\ge5,\qquad d=2^m,\qquad
D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad
L_m=A_m+D_m.
$$
真实有限头满足
$$
A_m^d=0,\quad [A_m,D_m]=0,\quad
\|A_m\|\le6,\quad \|D_m\|\le1.
\tag{1.1}
$$
所有真实 Cayley 因子都保留在 $A_m$ 中。原截断给
$$
\|T-L_m\|\le26\eta_{m-1},
$$
$$
-\log\eta_{m-1}
=\frac{175}{2}d^4-\frac{315}{4}d^3+150d.
$$
特别，对所有 $m\ge5$，
$$
\boxed{\eta_{m-1}\le e^{-80d^4}.}
\tag{1.2}
$$
这是 $175/2-(315/4)/d>80$ 的直接结果；没有沿用平方模型的 $1400d^4$ 物理常数。

以下 $\mathcal H^{(m)}_\ell$、$P_\ell$ 数第 $m$ 位之后的高尾孔，头因子保留恒等；$\mathcal N$ 和 $\tau_Q(w)=\|\mathbf1_{\{\mathcal N>Q\}}w\|$ 始终数原全部物理孔。

## 2. 阶乘原像与真实 carry 的全部导数

固定 $D=D_m$，定义
$$
\mathcal U_R(f)=\sum_{k\ge0}\frac{R^k}{k!}\|D^kf\|,
\qquad
\|X\|_{\delta,R}
=\sum_{k\ge0}\frac{R^k}{k!}\|\operatorname{ad}_D^kX\|.
\tag{2.1}
$$
因为 $D$ 有界，任意 $f\in H$、$X\in B(H)$ 的这些量都有限。R254 第十二附录的实际 Leibniz 证明直接给
$$
\|XY\|_{\delta,R}\le\|X\|_{\delta,R}\|Y\|_{\delta,R},
\qquad
\mathcal U_R(Xf)\le\|X\|_{\delta,R}\mathcal U_R(f).
\tag{2.2}
$$
孔截断在 $\mathcal U_R$ 中是收缩，因为
$D^kP_{\le a}=P_{\le a-k}D^k$。

在输入孔数至多 $q$、最大原像阶 $d$ 上，取同一辅助头的相容原像 $R_t$。本稿的纯系数 $(j+1)^{-2}$ 经 $j'=j-1$ 就是原附录的 $(j'+2)^{-2}$；使用稍大的参数
$$
R=512\sqrt{q+d+1}(m+q+d+2)^{3/2}
\tag{2.3}
$$
是有效的统一上界。该附录的递推对任意指定最大阶成立，并没有要求最大阶必须恰为平方模型的 $2d$。于是
$$
DR_t=R_{t-1},\quad R_0=I,\quad
R_t\mathcal H_p^{(m)}\subseteq\mathcal H_{p+t}^{(m)},
$$
$$
\boxed{\|R_tf\|\le\frac{R^t}{t!}\mathcal U_R(f).}
\tag{2.4}
$$
同一精确双和还保留较粗但随后有用的逐幂界
$$
\boxed{\|R_tf\|
\le\sum_{k=0}^q (2R)^{k+t}\|D^kf\|.}
\tag{2.5}
$$
两条界都在完整有限孔输入层成立；位置不需有限。各 $R_t$ 与原有限头 $A_m$ 交换。

令 $K_\ell=L_{\ell+1}-L_\ell$，$\ell\ge m$。它只作用原前 $\ell+1$ 个物理位，且
$$
\|K_\ell\|\le52\eta_{\ell-1}.
$$
它与 $D_m$ 的交换子只有位 $m,\ldots,\ell$ 参与。逐位 $\operatorname{ad}_{E_j}^3=0$ 给
$$
\|K_\ell\|_{\delta,R}
\le52\eta_{\ell-1}
\prod_{j=m}^{\ell}(1+R(j+1)^{-2})^2.
\tag{2.6}
$$
这使用真实有限头差，不把实际高尾预先当纯尾。

置 $E_m=L_m-T=-\sum_{\ell\ge m}K_\ell$。若
$$
x=\log(2+R)\le d^3,
\tag{2.7}
$$
则由 (1.2)、(2.6)，
$$
\begin{aligned}
\|E_m\|_{\delta,R}
&\le52\sum_{r\ge0}
 \exp[-80d^4\,16^r+2(r+1)x]\\
&\le104e^{-80d^4+2d^3}
\le e^{-79d^4}.
\end{aligned}
$$
相邻项比小于 $1/2$；最后一步用 $d\ge32$。因此
$$
\boxed{\epsilon_m(R):=\|E_m\|_{\delta,R}\le e^{-79d^4}.}
\tag{2.8}
$$
级数在导数范数中收敛，也在原算子范数中收敛到同一个实际误差。

## 3. 实际核上的线性指数导数吸收

定义
$$
H_m(R)=\sum_{j=0}^{d-1}\frac{R^j}{j!}\|A_m^j\|.
$$
对 $w\in M$，准确有
$$
Dw=-A_mw+E_mw,
$$
以及有限代数恒等式
$$
D^kw=(-A_m)^kw+
\sum_{j=0}^{k-1}(-A_m)^jD^{k-1-j}E_mw.
\tag{3.1}
$$
超过 $d-1$ 的头幂为零。对 (3.1) 乘 $R^k/k!$ 并求和，用
$(j+1+\ell)!\ge j!\ell!$，得到
$$
\mathcal U_R(w)
\le H_m(R)\|w\|+RH_m(R)\mathcal U_R(E_mw)
$$
$$
\le H_m(R)\|w\|
+RH_m(R)\epsilon_m(R)\mathcal U_R(w).
\tag{3.2}
$$
$\mathcal U_R(w)$ 本来有限，所以这里的吸收不是形式级数论证。

在 (2.7) 下，由 (1.1)，
$$
H_m(R)\le d[6(2+R)]^d,\qquad
\log H_m(R)\le2d^4.
$$
结合 (2.8)，$RH_m(R)\epsilon_m(R)<1/2$，从而
$$
\boxed{\mathcal U_R(w)\le2H_m(R)\|w\|.}
\tag{3.3}
$$

这一步始终使用实际核方程 $Tw=0$；没有在环境全空间上给纯尾幂虚构四次衰减。

## 4. 大窗口的原线性低输出正交投影

定义有限和
$$
\mathcal R_{m,q}
=\sum_{j=0}^{d-1}(-A_m)^jR_{j+1}.
\tag{4.1}
$$
由相容性和 $A_m^d=0$，
$$
L_m\mathcal R_{m,q}=I
$$
在所述完整有限孔输入范围准确成立。由 (2.4)，
$$
\boxed{
\|\mathcal R_{m,q}f\|
\le RH_m(R)\mathcal U_R(f).
}
\tag{4.2}
$$
这是有限源次数上的实际右逆，不延拓成整个 Hilbert 空间上的满射逆。

固定 $w\in M$，取
$$
r_0=P_{\le q-1}L_mP_{\le q}w
=P_{\le q-1}E_mw,\qquad
z=\mathcal R_{m,q}r_0.
$$
$L_m$ 只下降零次或一次尾孔，故
$$
P_{\le q}w-P_{\le q}z
\in
\mathcal W^{\rm lin}_{m,q}
:=\mathcal H_{\le q}^{(m)}
 \cap\ker(P_{\le q-1}L_m).
$$
(2.2)、(2.8)、(3.3)、(4.2) 给
$$
\|z\|\le2RH_m(R)^2\epsilon_m(R)\|w\|
\le e^{-74d^4}\|w\|.
\tag{4.3}
$$
末一步的对数正项至多
$\log2+d^3+4d^4$，负项为 $-79d^4$，而 $d\ge32$。

令 $v_{m,q}$ 为 $w$ 到上述实际闭空间的正交投影。最佳逼近性给
$$
\boxed{
\|v_{m,q}\|\le\|w\|,\qquad
\|v_{m,q}-P_{\le q}w\|\le e^{-74d^4}\|w\|.
}
\tag{4.4}
$$
原高尾只付 $\tau_q(w)$，系数为 $1$。

本稿采用参数范围
$$
\boxed{4d\le q\le e^{d^3/4},\qquad m\ge5.}
\tag{4.5}
$$
因为 $R\le2048q^2$，
$$
\log(2+R)\le8+2\log q\le d^3,
$$
所以本节所有假设同时成立。

## 5. 单层残量与准确 Legendre 预算

记 $v=v_{m,q}$、$r=L_mv$。原线性低输出恒等式给
$$
r\in\mathcal H_q^{(m)},\qquad r=A_mv_q,
$$
$$
D^kv=P_{\le q-k}(-A_m)^kv,
$$
$$
\boxed{
D^kr=(-1)^kA_m^{k+1}v_{q-k},
\qquad 0\le k<d.
}
\tag{5.1}
$$
特别 $D^dv=D^dr=0$。这些是准确层身份，已经在原线性稿逐项证明；在这里 $q$ 可以更大，证明不变。

令
$$
c_{m,q}=\mathcal R_{m,q}r,\qquad k_{m,q}=v-c_{m,q}.
$$
则
$$
k_{m,q}\in\ker L_m,\quad
c_{m,q}\in\mathcal H_{[q+1,q+d]}^{(m)},\quad
k_{m,q}\in\mathcal H_{\le q+d}^{(m)}.
\tag{5.2}
$$
由有限伴随多项式 $\mathcal A_mL_m=D^d$，还准确有
$D^dc_{m,q}=0$。

原真实头进位计数给
$$
\|A_m^n\|\le6^n e^{-\gamma(n-m)_+^4},
\qquad \gamma=770/256.
\tag{5.3}
$$
将 (2.5)、(5.1) 合并在同一个实际头幂中，
$$
\|(-A_m)^jR_{j+1}r\|
\le\sum_{k<d}
(2R)^{j+k+1}
\|A_m^{j+k+1}v_{q-k}\|.
$$
置
$$
\Theta=\log(12R),\qquad
C_\gamma=\frac{3}{4^{4/3}\gamma^{1/3}}.
$$
准确的一元最大值是
$$
\sup_{s\ge0}(\Theta s-\gamma s^4)
=C_\gamma\Theta^{4/3}.
\tag{5.4}
$$
于是
$$
\boxed{
\|c_{m,q}\|\le e^{F(m,q)}
 \|P_{[q-d+1,q]}v\|,
}
$$
$$
\boxed{
F(m,q)=2\log d+m\Theta+C_\gamma\Theta^{4/3}.
}
\tag{5.5}
$$
这里没有分别支付输入导数和外层右逆的两个头长度。

在 (4.5) 下，$\Theta\le11+d^3/2\le d^3$、$m\le d/2$、
$C_\gamma<1$，因而
$$
F(m,q)\le2d^4.
\tag{5.6}
$$
由 (4.4)，
$$
\boxed{
\|c_{m,q}\|
\le e^{F(m,q)}\tau_{q-d}(w)
   +e^{-72d^4}\|w\|.
}
\tag{5.7}
$$
同时直接用 $\|v\|\le\|w\|$，有
$$
\|c_{m,q}\|\le e^{2d^4}\|w\|,\qquad
\|k_{m,q}\|\le2e^{2d^4}\|w\|.
\tag{5.8}
$$

## 6. 原线性模型的逐头实际提升

下面独立构造原 $L_m$ 核到 $N$ 的提升；没有调用平方图的 $J$ 或其提升误差。

设旧头为 $p$、$z=2^p$，且
$$
k\in\ker L_p,\qquad
k\in\mathcal H_{\le Q}^{(p)}.
$$
旧伴随多项式给 $D_p^zk=0$。原物理系数保持原位号：
$$
D_{p+1}=D_p-(p+1)^{-2}E_p.
$$
由于 $E_p^2=0$、它与 $D_p$ 交换，
$$
\boxed{D_{p+1}^{z+1}k=0.}
\tag{6.1}
$$
将第 $p$ 位归入新头不会增加剩余尾孔数。令
$$
r=L_{p+1}k=(L_{p+1}-L_p)k.
$$
$L_{p+1}$ 与 $D_{p+1}$ 交换，所以
$$
r\in\ker D_{p+1}^{z+1}
 \cap\mathcal H_{\le Q}^{(p+1)},\qquad
\|r\|\le52\eta_{p-1}\|k\|.
\tag{6.2}
$$

在新头维数 $2z$ 上，使用其线性相容逆
$$
\mathcal R'=\sum_{j<2z}(-A_{p+1})^jR'_{j+1}.
$$
相容原像对输入 $\ker D_{p+1}^{s}$、$s=z+1$ 的已证粗界是
$$
\|R'_tf\|\le(2R')^{s+t-1}\|f\|.
$$
这里
$$
R'=512\sqrt{Q+2z+1}(p+1+Q+2z+2)^{3/2}.
$$
由 $\|A_{p+1}\|\le6$，得
$$
\boxed{\|\mathcal R'r\|
\le2z(12R')^{4z}\|r\|.}
\tag{6.3}
$$
实际指数甚至至多 $3z$，上式保守地放宽为 $4z$。

置 $k'=k-\mathcal R'r$，则 $L_{p+1}k'=0$，新尾孔数最多增加 $2z$。此后用新模型的准确核方程重置
$D_{p+1}^{2z}k'=0$，不把核阶的粗增加无限累积。

现在固定
$$
m_0\ge5,\quad d_0=2^{m_0},\quad
1\le Q_0\le e^{d_0^3/3},\quad
k_0\in\ker L_{m_0}\cap\mathcal H_{\le Q_0}^{(m_0)}.
$$
递归置
$$
m_n=m_0+n,\quad d_n=2^nd_0,\quad
Q_n=Q_0+2d_n-2d_0
$$
并重复上述一步，得到 $k_n\in\ker L_{m_n}\cap\mathcal H_{\le Q_n}^{(m_n)}$。

在第 $n$ 步写 $z=d_n$。新辅助常数满足
$$
R'_n\le512(Q_0+5z)^2,
$$
$$
\log(12R'_n)\le\tfrac23d_0^3+13+2\log z.
$$
因此 (6.3) 的完整成本满足
$$
\begin{aligned}
\log(2z)+4z\log(12R'_n)
&\le \tfrac83zd_0^3+52z+8z\log z+\log(2z)\\
&\le3z^4.
\end{aligned}
\tag{6.4}
$$
最后一步对 $z\ge32$ 成立，使用 $d_0\le z$；余下正项小于 $z^4/3$。

由 (1.2)、(6.2)，
$$
\boxed{
\|k_{n+1}-k_n\|
\le e^{-76d_n^4}\|k_n\|.
}
\tag{6.5}
$$
全部误差和小于 $2e^{-76d_0^4}$，所以
$$
\|k_n\|\le2\|k_0\|,\qquad
\|k_\infty-k_0\|\le4e^{-76d_0^4}\|k_0\|
\le e^{-75d_0^4}\|k_0\|.
\tag{6.6}
$$
这是实际 Hilbert 极限。$L_{m_n}\to T$ 为算子范数收敛，故
$Tk_\infty=0$。

每步差的原全部孔数最多为
$$
m_{n+1}+Q_{n+1}\le Q_0+5d_n.
$$
故对每个固定 $c>0$，
$$
\sum_n\|e^{c\mathcal N}(k_{n+1}-k_n)\|
\le2\|k_0\|\sum_n
 e^{c(Q_0+5d_n)-76d_n^4}<\infty.
$$
初值也只有有限孔，因此
$$
k_\infty\in M\cap\operatorname{Dom}e^{c\mathcal N}
\quad(c>0).
$$
取 $c=4$，Cauchy--Schwarz 给 $k_\infty\in X_3$。由旧的已证
$M\cap X_3\subseteq N$，得到 $k_\infty\in N$，没有用本稿新权结论循环证明。

所有步骤线性，因而得到实际有界线性映射
$$
\boxed{
\Lambda^{\rm lin,inc}_{m_0,Q_0}:
\ker L_{m_0}\cap\mathcal H_{\le Q_0}^{(m_0)}
\longrightarrow N,
\quad
\|\Lambda^{\rm lin,inc}k-k\|
\le e^{-75d_0^4}\|k\|.
}
\tag{6.7}
$$

## 7. 完整原线性修复和提升的组合

对 (4.5) 的 $m,q$，$q+d\le e^{d^3/3}$，故 (6.7) 可用于 (5.2) 的全部 $k_{m,q}$。令
$$
n_{m,q}=\Lambda^{\rm lin,inc}_{m,q+d}k_{m,q}\in N.
$$
用 (5.8) 支付修复向量的全部范数，得到
$$
\boxed{
\|n_{m,q}-(v_{m,q}-c_{m,q})\|
\le e^{-72d^4}\|w\|.
}
\tag{7.1}
$$
它同时支付了大窗口低方程、准确单层高尾修复以及全部无限真实进位提升。

## 8. 为每个整数 q 选择头长

对每个整数 $q\ge128$，定义
$$
\boxed{
m(q)=\max\!\left\{5,
 \left\lceil\frac{\log(4\log(q+2))}{3\log2}\right\rceil
 \right\},\qquad d(q)=2^{m(q)}.
}
\tag{8.1}
$$
准确有 $q\le e^{d(q)^3/4}$。若 $m(q)=5$，则 $4d(q)=128\le q$；
否则 $d(q)^3<32\log(q+2)\le32q$，也给 $4d(q)\le q$。
所以 (4.5) 对所有这些整数同时成立。

当 $q\to\infty$，
$$
d(q)\asymp(\log q)^{1/3},\qquad
m(q)=O(\log\log q).
$$
(2.3) 的 $R=512q^2(1+o(1))$，故
$$
\Theta=2\log q+O(1).
$$
由 (5.5)，
$$
\boxed{
F(m(q),q)
=\bigl(K_*+o(1)\bigr)(\log q)^{4/3},
}
\tag{8.2}
$$
其中
$$
\boxed{
K_*=2^{4/3}C_\gamma
=\frac3{(16\gamma)^{1/3}}
=3(16/770)^{1/3}
=0.8247664896\ldots.
}
\tag{8.3}
$$
$m(q)\Theta=O(\log q\log\log q)$ 是严格低阶项。这里不需要相邻 $m$ 的稀疏孔窗口插值。

**定理 8.1。** 对两个原实际边界，任意 $c>K_*$ 都有
$$
\boxed{
M\cap\operatorname{Dom}
 \exp\!\left(c[\log(2+\mathcal N)]^{4/3}\right)
\subseteq N.
}
\tag{8.4}
$$

证明：若 $w$ 在左侧，则
$\tau_s(w)\le C_w e^{-c[\log(s+2)]^{4/3}}$。
因为 $d(q)=o(q)$，
$\log(q-d(q)+2)=\log q+o(1)$。
由 (5.7)、(8.2)，$c_{m(q),q}\to0$。由 (4.4)，
$v_{m(q),q}\to w$，且 (7.1) 的实际提升误差趋零。
故 $n_{m(q),q}\to w$ 强收敛，$N$ 闭，结论成立。
未声明临界等号 $c=K_*$。

**定理 8.2。** 若 $0\ne w\in D_{\rm def}$，则
$$
\boxed{
\limsup_{Q\to\infty}
\frac{\log(\|w\|/\tau_Q(w))}
 {[\log(Q+2)]^{4/3}}
\le K_*/2.
}
\tag{8.5}
$$

证明：以下简写 $c_q=c_{m(q),q}$、$v_q=v_{m(q),q}$。
由 $n_{m(q),q}\in N$、(7.1)、$v_q\to w$，
$$
\langle c_q,w\rangle\to\|w\|^2.
$$
$c_q$ 至少有 $q+1$ 个高尾孔，所以充分大 $q$ 时
$$
\|c_q\|\tau_q(w)\ge\tfrac12\|w\|^2.
$$
结合 (5.7) 和尾单调性，吸收明确的小误差后，
$$
e^{F(m(q),q)}\tau_{q-d(q)}(w)^2
\ge\tfrac14\|w\|^2.
\tag{8.6}
$$
对任意充分大的整数 $Q$，取 $q=2Q$，则
$q-d(q)\ge Q$、$\log q=\log Q+O(1)$。
用 $\tau_Q\ge\tau_{q-d(q)}$ 和 (8.2)，即得 (8.5)。
不存在稀疏网格的 $16$ 倍损失。

## 9. 全部整数层的原最小修复能量

对固定实际 $w\in M$ 和 (8.1) 的每个 $q$，令
$$
r_q=L_{m(q)}v_q,
$$
$$
\mathcal C_q(w)=
\left\{c\in\mathcal H_{[q+1,q+d(q)]}^{(m(q))}:
L_{m(q)}c=r_q,\quad D_{m(q)}^{d(q)}c=0\right\}.
\tag{9.1}
$$
(5.2) 证明它非空；它是原 Hilbert 空间的闭仿射集。因此存在唯一最小范数元 $c_q^{\min}$，定义
$$
\lambda_q(w)=\|c_q^{\min}\|.
$$
原候选给
$$
\boxed{
\lambda_q(w)\le
e^{F(m(q),q)}
\left[\tau_{q-d(q)}(w)+e^{-74d(q)^4}\|w\|\right].
}
\tag{9.2}
$$
又 $\lambda_q\le e^{2d(q)^4}\|w\|$，因此同一个实际逐头提升适用于
$v_q-c_q^{\min}$。所得 $n_q^{\min}\in N$ 满足
$$
n_q^{\min}=w-c_q^{\min}+\rho_q,\qquad
\sup_{q\ge Q}\|\rho_q\|\longrightarrow0.
\tag{9.3}
$$
例如右侧余项可用
$$
\tau_Q(w)+2e^{-72d(Q)^4}\|w\|
$$
统一控制。

每个 $c_q^{\min}$ 的原全部孔支撑包含于
$$
I_q=[q+1,q+\ell_q],\qquad
\ell_q=d(q)+m(q).
\tag{9.4}
$$
与仅取稀疏 $m$ 窗口不同，这些 $I_q$ 会重叠。但重叠可以准确加权。

**引理 9.1（真实孔窗口的覆盖界）。** 对每个原孔次数整数 $p$，
$$
\boxed{
\sum_{\substack{q\ge128\\p\in I_q}}\frac1{\ell_q}\le2.
}
\tag{9.5}
$$

证明：$\ell_q$ 单调，且 $m(q)\le d(q)/2$、$q\ge4d(q)$，所以
$\ell_q\le3q/8$。
若 $p\in I_q$，则 $q<p<2q$。
由 (8.1)，此时 $m(p)-m(q)\le1$：相应未取整量之差小于
$\log2/(3\log2)<1$。
故 $d(p)\le2d(q)$，并有
$$
\ell_p\le2d(q)+m(q)+1\le2\ell_q.
$$
另一方面 $p\in I_q$ 蕴含
$p-\ell_p\le q\le p-1$，可用的整数 $q$ 至多 $\ell_p$ 个。
每个 $1/\ell_q\le2/\ell_p$，得 (9.5)。证毕。

因此，任意单位向量 $h_q$ 若支撑于 $I_q$，则
$$
\sum_{q\ge Q}\frac{|\langle h_q,w\rangle|^2}{\ell_q}
\le2\tau_Q(w)^2.
\tag{9.6}
$$
它直接由逐次数非负求和及 (9.5) 得到，不假设这些向量正交。

## 10. 加权正凸平均与真缺陷的能量尾和

**定理 10.1。** 对任意实际 $w\in M$，
$$
\boxed{
\sum_{q\ge128}
 \frac1{\ell_q(1+\lambda_q(w)^2)}=\infty
\quad\Longrightarrow\quad w\in N.
}
\tag{10.1}
$$

证明：置
$$
a_q=\frac1{\ell_q(1+\lambda_q^2)},\qquad
A_{Q,R}=\sum_{q=Q}^Ra_q.
$$
对有限和，逐孔次数使用 Cauchy--Schwarz 与 (9.5)，得到
$$
\left\|\sum_{q=Q}^Ra_qc_q^{\min}\right\|^2
\le2\sum_{q=Q}^Ra_q^2\ell_q\lambda_q^2
\le2A_{Q,R}.
\tag{10.2}
$$
将 (9.3) 的 $n_q^{\min}\in N$ 作正凸平均，故
$$
\operatorname{dist}(w,N)
\le\sup_{q\ge Q}\|\rho_q\|
 +\sqrt{2/A_{Q,R}}.
$$
先令 $R\to\infty$，再令 $Q\to\infty$，用 (9.3) 即得结论。
所有平均都是有限正权平均，没有使用条件收敛的修复级数。

**定理 10.2。** 若 $0\ne w\in D_{\rm def}$，则对充分大的 $Q$，
$$
\boxed{
\sum_{q\ge Q}\frac1{\ell_q\lambda_q(w)^2}
\le\frac{8\,\tau_Q(w)^2}{\|w\|^4}.
}
\tag{10.3}
$$

证明：由 (9.3) 和 $w\perp N$，
$$
\langle c_q^{\min},w\rangle\to\|w\|^2.
$$
所以充分大 $q$ 时 $\lambda_q>0$，且
$$
|\langle c_q^{\min}/\lambda_q,w\rangle|^2
\ge \frac{\|w\|^4}{4\lambda_q^2}.
$$
以 $h_q=c_q^{\min}/\lambda_q$ 代入 (9.6)，即得 (10.3)。

例如，因 $\ell_q=O((\log q)^{1/3})$，若某个实际核向量满足最终统一界
$$
\boxed{
\lambda_q(w)^2
=O\!\left(q(\log q)^{2/3}\log\log q\right),
}
\tag{10.4}
$$
则 (10.1) 的级数由
$\sum 1/(q\log q\log\log q)=\infty$ 发散，因而 $w\in N$。
因此，非零真缺陷必须满足
$$
\limsup_{q\to\infty}
\frac{\lambda_q(w)^2}
 {q(\log q)^{2/3}\log\log q}=\infty.
\tag{10.5}
$$
这里所有能量都在原 Hilbert 范数中最小化，没有额外首位图度量，也没有把环境 $D^*$ 的下界当作压缩伴随下界。

## 11. 仍需解决的实际缺口

本稿的全整数加权判据严格利用了可重叠的真实修复窗口，而不是只把旧稀疏窗口换一个记号。它给出了更强的最小修复能量接口。

但是当前上界 (9.2) 仍含
$\exp((K_*+o(1))(\log q)^{4/3})$。一般 Hilbert 尾可以远慢于足以抵消这个因子的速度；(9.2) 没有证明 (10.1) 发散，也没有证明 (10.4)。

原实际 $D=M\ominus\overline{BM}$ 是否为零、正则核是否在整个 $M$ 内稠密以及普通 Hilbert ISP 仍未完成。下一项是控制真实特殊残量的最小修复能量本身，而非用任意原像或环境联合能量代替它。

完整来源：
- [R239 原线性单层修复与独立真实提升](../results/R239-appendix-direct-linear-boundary-repair-and-stable-lift.md)；
- [R254 相容多次纯尾原像](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)；
- [R254 阶乘原像、真实 carry jets 与大窗口](../results/R254-appendix-factorial-preimages-carry-jets-and-large-low-output-windows.md)；
- [R271 平方模型逐头真实提升及既有 $4/3$ 权阶](../results/R271-increasing-head-actual-lift-and-log-four-thirds-stable-range.md)；
- [R239 已证实际指数权核饱和](../results/R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md)。
