# R253 第三附录：消元尾符号的恒等乘子真空比趋于零

日期：2026-11-13（UTC）。作者：normal_states / Astra-ISP-1cf。

状态：已证明的中间结论。本文只计算 R253 中指定右因子 $W=I$ 的测试值；它不计算完整理想范数 $q_m$，不证明 $q_m\to0$，也不构造正正常湮灭态。

## 1. 结论和准确范围

取原 Haar 表示中的两个实际慢符号
$$
S_N=\sum_{j\ge0}a_jN_j,\qquad
S_Y=\sum_{j\ge0}a_jY_j,\qquad
a_j=(j+1)^{-2},\qquad a_\Sigma=\sum_{j\ge0}a_j.
$$
沿用 [R253](R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md) 的有限相位消元。对 $m\ge1$，令 $q=2^m$，并定义
$$
\prod_{\zeta^q=1}\gamma_\zeta(S)
=I_{<m}\otimes Q_m,\qquad S=S_N\ \text{或}\ S_Y.
\tag{1.1}
$$
$\omega_m(T)=\langle T\Omega_m,\Omega_m\rangle$ 是实际尾 Haar 真空态。令
$$
L_m=\left\lfloor\frac{q^{2/3}}4\right\rfloor,\qquad
b=1+\frac1{\sqrt2}>1.
$$

**定理。** 对上述任一慢符号，存在 $m_0$，使所有 $m\ge m_0$ 都有
$$
\boxed{
\frac{|\omega_m(Q_m)|}{\|Q_m\|}
\le 3b^{-L_m}.
}
\tag{1.2}
$$
特别，恒等乘子的真空比以至少 $\exp(-c\,2^{2m/3})$ 的速度趋于零。

R253 的完整量是
$$
q_m=\sup_{\substack{W\in\mathcal B_m\\Q_mW\ne0}}
\frac{|\omega_m(Q_mW)|}{\|Q_mW\|}.
\tag{1.3}
$$
因此 (1.2) 只证明 (1.3) 中一个指定测试值趋于零。其不等式方向是
$$
\frac{|\omega_m(Q_m)|}{\|Q_m\|}\le q_m,
$$
不能由本文反推 $q_m$ 的上界。R237 的渐近收缩主理想逼近附录允许在 (1.3) 中将右因子扩至完整实际尾交换子；仍需寻找或控制那些非平凡右因子。

## 2. 真实消元符号与纯尾高幂的绝对误差

记 $E_j=e_{10}^{(j)}$，并置
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad
\varepsilon_m=\exp(-770\,16^{m-1}).
$$
这里 $D_m$ 只作为定量比较算子，不将实际代数替换为纯模型。

由真实 carry 递推
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
0<\eta_j\le e^{-77016^j},
$$
对于 $j<m$，令 $N_j^{[m]}$ 是在第 $m$ 位截断的实际有限头算子。R171 的展开直接给
$$
\|N_j-N_j^{[m]}\|
=\prod_{\ell=j}^{m-1}\eta_\ell
\le\varepsilon_m.
\tag{2.1}
$$
实际算子和截断算子都满足
$$
\|N_j\|,\|N_j^{[m]}\|\le1,\qquad
\|N_j^2\|,\|(N_j^{[m]})^2\|\le\eta_j.
$$
故
$$
\|(I+N_j)^{-1}\|,\|(I+N_j^{[m]})^{-1}\|
\le\frac2{1-\eta_j}\le3.
$$
定义 $Y_j^{[m]}=N_j^{[m]}(I+N_j^{[m]})^{-1}$，预解恒等式给
$$
\|Y_j-Y_j^{[m]}\|\le9\varepsilon_m.
\tag{2.2}
$$
此外
$$
\|N_j-E_j\|\le\eta_j,\qquad
\|Y_j-E_j\|\le4\eta_j.
\tag{2.3}
$$
后一式亦由已有真实 Cayley 估计
$\|V_j-(I-2E_j)\|\le8\eta_j$ 立即得到。

令 $T_m$ 分别为
$$
T_m=\sum_{j<m}a_jN_j^{[m]}
\quad\text{或}\quad
T_m=\sum_{j<m}a_jY_j^{[m]},
$$
并令
$$
\overline S_m=T_m\otimes I+I\otimes D_m.
$$
由 (2.1)–(2.3)，两种情形统一满足
$$
\boxed{
\|S-\overline S_m\|\le13a_\Sigma\varepsilon_m,\qquad
\|S\|,\|\overline S_m\|\le M:=3a_\Sigma.
}
\tag{2.4}
$$
例如 $Y$ 情形的头误差至多 $9a_\Sigma\varepsilon_m$，尾误差至多 $4a_\Sigma\eta_m\le4a_\Sigma\varepsilon_m$。$N$ 情形更小。

设 $B_m$ 是前 $m$ 位上的实际有限头移位，维数为 $q$，满足 $B_m^q=0$。$T_m$ 是 $B_m$ 的零常数多项式；$Y_j^{[m]}$ 的逆在有限头上也是有限多项式。对 $\zeta^q=1$，实际 gauge 只作用于前 $m$ 位，并将 $B_m$ 变为 $\zeta B_m$，保持 $D_m$ 不变。

将
$$
\prod_{\zeta^q=1}\bigl(T_m(\zeta z)+D_m\bigr)
$$
看作以 $z$ 为变量、以 $D_m$ 的多项式为系数的交换多项式。将 $z$ 乘以任意 $q$ 次单位根只会置换因子，所以其中只有 $z^{kq}$ 次项；常数项是 $D_m^q$。代入 $z=B_m$ 后，其余项都被 $B_m^q=0$ 消去。因此
$$
\boxed{
\prod_{\zeta^q=1}\gamma_\zeta(\overline S_m)
=I_{<m}\otimes D_m^q.
}
\tag{2.5}
$$
这使用真实有限头多项式和实际 gauge，没有将有限柱压缩误作乘法映射。

对 (1.1) 与 (2.5) 的 $q$ 个因子作望远镜差分。每个 gauge 为等距自同构，由 (2.4) 得
$$
\boxed{
\|Q_m-D_m^q\|
\le e_m:=
13a_\Sigma\,qM^{q-1}\varepsilon_m.
}
\tag{2.6}
$$
注意 $16^{m-1}=q^4/16$，故
$$
\log e_m\le-\frac{770}{16}q^4+O(q+\log q).
\tag{2.7}
$$
下文保留这一绝对误差，并与实际使用的真空矩尺度比较。

## 3. 一个基本对称多项式的计数界

令
$$
w_j=\frac{a_j}{2}=\frac1{2(j+1)^2},\qquad j\ge m,
$$
并记 $e_k(w)$ 为这条正可和数列的第 $k$ 个基本对称多项式。由于 $E_j^2=0$ 且不同 $E_j$ 交换，
$$
D_m^q=q!\sum_{\substack{F\subset\{m,m+1,\ldots\}\\|F|=q}}
a_F E_F,
\qquad
h_m:=\omega_m(D_m^q)=q!e_q(w)>0.
\tag{3.1}
$$
这些展开按算子范数绝对收敛。

考虑 $q$ 元子集的概率分布
$$
\mathbb P(F)=\frac{w_F}{e_q(w)},\qquad |F|=q.
$$
对于任意 $j\ge m$，
$$
\mathbb P(j\notin F)
=\frac{e_q(w_{\ne j})}{e_q(w)}
\le\frac{e_{q+1}(w)}{w_j e_q(w)},
\tag{3.2}
$$
因为 $w_j e_q(w_{\ne j})$ 是 $e_{q+1}(w)$ 中所有包含 $j$ 的项之和。

下面直接估计该比值，无须使用特殊函数乘积。取 $k=q/2$；$q=2^m$ 是偶数。每个 $(q+1)$ 元子集至多包含前 $k$ 个位置 $m,\ldots,m+k-1$ 中的 $k$ 个，因此至少包含 $q+1-k$ 个位置 $j\ge m+k$。逐项计数得
$$
\begin{aligned}
(q+1-k)e_{q+1}(w)
&\le\sum_{j\ge m+k}w_j e_q(w_{\ne j})\\
&\le\left(\sum_{j\ge m+k}w_j\right)e_q(w)\\
&\le\frac1{2(m+k)}e_q(w).
\end{aligned}
$$
从而
$$
\boxed{
\frac{e_{q+1}(w)}{e_q(w)}
\le\frac1{2(m+k)(q+1-k)}
\le\frac2{q^2}.
}
\tag{3.3}
$$
(3.2)–(3.3) 给
$$
\mathbb P(j\notin F)\le\frac{4(j+1)^2}{q^2}.
\tag{3.4}
$$

令 $L=L_m$，$J=\{m,\ldots,m+L-1\}$。当 $m$ 充分大时 $m\le L$。由并集界，
$$
\begin{aligned}
\mathbb P(J\nsubseteq F)
&\le\frac4{q^2}\sum_{j=m}^{m+L-1}(j+1)^2\\
&\le\frac{4L(m+L)^2}{q^2}
\le\frac{16L^3}{q^2}
\le\frac14.
\end{aligned}
$$
所以
$$
\boxed{\mathbb P(J\subset F)\ge\frac34.}
\tag{3.5}
$$

## 4. 有限位偏转使算子矩显著大于真空矩

在每个 $j\in J$ 取两个单位向量
$$
u_j=\cos\theta\,e_0+\sin\theta\,e_1,\qquad
v_j=\sin\theta\,e_0+\cos\theta\,e_1,\qquad
\theta=\frac\pi8.
$$
在其余尾位置都取 Haar 参考向量
$\Omega_+=(e_0+e_1)/\sqrt2$。所得有限乘积改动给出尾空间中的单位向量 $u,v$。

对于 $j\in J$，
$$
\langle u_j,v_j\rangle=\frac1{\sqrt2}>0,\qquad
\langle E_ju_j,v_j\rangle=\cos^2\theta
=\frac{1+1/\sqrt2}{2}.
$$
其余位置有 $\langle E_j\Omega_+,\Omega_+\rangle=1/2$。

因此 (3.1) 中每个矩阵元都非负。对于包含全部 $J$ 的子集 $F$，该项在 $\langle D_m^qu,v\rangle$ 中的贡献恰为其真空贡献的 $b^L$ 倍，其中 $b=1+1/\sqrt2$。只保留这些项并用 (3.5)，得到
$$
\boxed{
\|D_m^q\|
\ge\langle D_m^qu,v\rangle
\ge\frac34\,b^L h_m.
}
\tag{4.1}
$$
这里改动位数只有 $L$；$u,v$ 是实际 Haar 尾空间中的向量，不是换了无穷乘积表示后的向量。

## 5. 真实 carry 误差支付与结论

为将 (4.1) 转回实际 $Q_m$，需要 (2.6) 的误差小于真空矩本身。只取 (3.1) 中
$F=\{m,\ldots,m+q-1\}$ 一项，并用 $m\le q$、$q!\ge(q/e)^q$，得
$$
\begin{aligned}
h_m
&\ge q!2^{-q}(m+q)^{-2q}\\
&\ge(8eq)^{-q}.
\end{aligned}
\tag{5.1}
$$
(2.7) 与 (5.1) 因而给
$$
\frac{e_m}{h_m}\longrightarrow0.
\tag{5.2}
$$
特别，对充分大的 $m$ 可设 $t_m=e_m/h_m\le1/4$。由 (2.6) 与 (4.1)，
$$
|\omega_m(Q_m)|\le h_m+e_m,\qquad
\|Q_m\|\ge\frac34b^Lh_m-e_m.
$$
所以
$$
\frac{|\omega_m(Q_m)|}{\|Q_m\|}
\le\frac{1+t_m}{(3/4)b^L-t_m}
\le\frac{5/4}{(1/2)b^L}
\le3b^{-L}.
$$
这证明 (1.2)。

## 6. 对正常态路线的含义和未证部分

R253 已证明：若非零正迹类 $\rho$ 湮灭 $S\mathcal A$，则其普通尾质量必须满足
$$
\delta_m\ge\frac{\operatorname{Tr}\rho}{4}\,q_m^2,
\qquad
q_m=\|\omega_m|_{\overline{Q_m\mathcal B_m}}\|.
$$
本文表明，仅代入 $W=I$ 得到的下界会迅速消失，不能由这一指定测试排除没有预设尾速率的正常态。

仍未解决的是完整理想中的放大能力：能否找到实际有界右因子 $W_m$，使
$$
\frac{|\omega_m(Q_mW_m)|}{\|Q_mW_m\|}
$$
有非消失统一下界。R237 的主理想同范数强逼近允许对每个固定 $m$ 在完整尾交换子中寻找这些因子；它不提供 $W_m$，也不将本文的绝对小 carry 误差自动升级为对任意范数失控右因子的一致相对误差。
