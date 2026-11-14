# 实际 Walsh 对角正常泛函的右模与慢符号湮灭者排除

日期：2026-11-12（UTC）。独占作者：literature。l2_moments 已独立核对第2节的局部分块、递归平方关系以及对角测试的最低位剥离机制。

**状态：以下给出完整实际证明。** 本稿保留所有 dyadic carry。所讨论的“对角”是相对于原 Haar 空间的 Walsh 正交基，不是物理柱集基，也不是负整数边界表示。

记 $\mathfrak F$ 为 $\mathbb N_0$ 的有限子集全体。对任意复序列 $p=(p_F)_{F\in\mathfrak F}\in\ell^1(\mathfrak F)$，定义迹类算子和正常泛函
$$
\rho_p=\sum_F p_F\,|\chi_F\rangle\langle\chi_F|,
\qquad
\Lambda(p)(T)=\operatorname{Tr}(\rho_pT)
=\sum_Fp_F\langle T\chi_F,\chi_F\rangle.
\tag{0.1}
$$
不要求 $p_F$ 为非负数。

**主定理。** 令
$$
b_j=(j+1)^{-2},\qquad
S_N=\sum_{j\ge0}b_jN_j,\qquad
S_Y=\sum_{j\ge0}b_jN_j(I+N_j)^{-1}.
\tag{0.2}
$$
对这两种实际慢符号分别有
$$
\boxed{
\Lambda(p)(S_\bullet F)=0\quad(F\in\mathcal A)
\quad\Longrightarrow\quad p=0.
}
\tag{0.3}
$$
因此全部非零 Walsh 对角正常正态都不可能是相应主理想的湮灭者。允许无限秩、任意慢的最高位尾及任意慢的次数尾；没有要求 Walsh 次数指数矩。

证明分成三个真实接口：

1. 对角正常泛函在解析右乘下，构成一个有界 $\ell^1$ 模；相应递归算子的平方关系仍准确保留 carry。
2. 这个对角泛函表示在 $\ell^1$ 上单射；由实际有理函数构造精确配置柱测试，随后才取原子极限。
3. 两种慢符号在此模上的算子具有零核。这里完整支付双尺度误差，并使用 R60 的已证加权多项式不等式及严格负常数；不使用核在小扰动下连续。

## 1. 原空间、尾交换子及矩阵坐标

沿用原 Haar 空间
$$
H=L^2(\mathbb Z_2,\mu)
=\bigotimes_{j\ge0}(\mathbb C^2,\Omega_+),
\qquad \Omega_+=(e_0+e_1)/\sqrt2.
$$
在第 $j$ 位使用 Walsh 坐标 $(1,\chi_j)$；全空间的基仍为 $\chi_F$。

实际归一化幂满足
$$
\|N_j\|=1,\qquad N_j^2=\eta_jN_{j+1},
\qquad
N_j=E_j+\eta_jE_j^*N_{j+1},
\tag{1.1}
$$
$$
E_j=e_{10}^{(j)},\qquad
0<\eta_j\le e^{-770\,16^j}.
\tag{1.2}
$$
$N_j$ 精确只作用于第 $j$ 位及其后方。令 $H_j$ 为这段实际尾空间，$\mathscr C_j=\{N_j\}'\subset B(H_j)$。每个更高 $N_k$ 是 $N_j$ 的非零常数倍幂，故所有使用它们的有理函数均属于相应实际解析代数。

在 Walsh 坐标中，置 $t=\eta_jN_{j+1}$，有准确分块
$$
N_j=
\begin{pmatrix}
(1+t)/2&(1-t)/2\\
-(1-t)/2&-(1+t)/2
\end{pmatrix}.
\tag{1.3}
$$
这是把物理分块 $\left(\begin{smallmatrix}0&t\\ I&0\end{smallmatrix}\right)$
作一次局部 Hadamard 坐标变换得到的。

令
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
s_j=(I+t)(I-t)^{-1}.
$$
由 (1.3) 或直接乘逆，
$$
V_j=
\begin{pmatrix}
0&-I\\ I&2s_j
\end{pmatrix}.
\tag{1.4}
$$
这里所有逆都是真实范数收敛的逆：$\|t\|\le\eta_j<1$，
而 $(I+N_j)^{-1}=(I-N_j)(I-N_j^2)^{-1}$。

若 $T\in\mathscr C_j$，则 $T$ 与
$N_j^2=\eta_j(I\otimes N_{j+1})$ 交换。因此 $T$ 的每个 Walsh 块都属于
$\mathscr C_{j+1}$，特别与 $s_j$ 交换。比较 $TV_j=V_jT$，得到
$$
\boxed{
T=\begin{pmatrix}A&B\\-B&D\end{pmatrix},
\qquad D=A-2s_jB.
}
\tag{1.5}
$$
其中 $\|A\|,\|D\|\le\|T\|$。以后只在这些实际块上运算。

## 2. 右乘 $N_j$ 的精确对角公式

定义零点邻域解析函数
$$
a(z)=\frac{1+z}{4}+\frac{z}{1+z}
=\frac{1+6z+z^2}{4(1+z)},
$$
$$
c(z)=\frac{1+z}{4}-\frac{z}{1+z}
=\frac{1-2z+z^2}{4(1+z)}.
\tag{2.1}
$$
由 (1.5)，$B=(A-D)/(2s_j)$。把它代入 (1.3) 与 $T$ 的乘积，两个对角块准确为
$$
\boxed{
(N_jT)_{00}=a(t)A+c(t)D,\qquad
(N_jT)_{11}=-c(t)A-a(t)D.
}
\tag{2.2}
$$
例如第一个块先等于
$(1+t)A/2-(1-t)B/2$；代入 $B$ 即得 (2.2)。
这一步不丢弃 $t$，也不将不同块上的对角压缩冒充乘法同态。

还记录两个标量恒等式：
$$
a(z)+c(z)=\frac{1+z}{2},\qquad
a(z)-c(z)=\frac{2z}{1+z},
$$
所以
$$
\boxed{a(z)^2-c(z)^2=z.}
\tag{2.3}
$$

## 3. 在 $\ell^1$ 与 Hilbert 空间上共同构造递归模

把 $H_j$ 同时按 Walsh 基识别为
$\ell^2(\mathfrak F_j)$，其中 $\mathfrak F_j$ 是 $[j,\infty)$ 的有限子集。
同一矩阵也作用在 $\ell^1(\mathfrak F_j)$。
以下算子在这两种范数中同时构造；没有把 $\ell^1$ 与 $H_j$ 等同。

对整数 $m>j$，先令 $\widehat N_m^{[m]}=0$，再向低位递归定义
$$
\widehat N_j^{[m]}=
\begin{pmatrix}
a(\eta_j\widehat N_{j+1}^{[m]})
&-c(\eta_j\widehat N_{j+1}^{[m]})\\
c(\eta_j\widehat N_{j+1}^{[m]})
&-a(\eta_j\widehat N_{j+1}^{[m]})
\end{pmatrix}.
\tag{3.1}
$$
对 $j\ge m$ 取零；有限矩阵张量上更高尾恒等后仍记相同符号。

### 3.1 范数、平方及交换关系

$a(0)=c(0)=1/4$。对每个 $n\ge1$，
$a,c$ 的 $n$ 次 Taylor 系数的绝对值之和恰为 $2$。
所以对 $\|R\|\le1$，
$$
\|a(\eta_jR)\|+\|c(\eta_jR)\|
\le\frac12+\frac{2\eta_j}{1-\eta_j}<\frac35.
\tag{3.2}
$$
该估计在 $\ell^1$、$\ell^2$ 中都成立：块矩阵的范数不超过两个函数范数之和。
从终端向下归纳得到
$$
\boxed{
\|\widehat N_j^{[m]}\|_{\ell^1\to\ell^1},
\ \|\widehat N_j^{[m]}\|_{H_j\to H_j}
\le\frac35.
}
\tag{3.3}
$$

由 (2.3) 及块系数交换，
$$
(\widehat N_j^{[m]})^2=\eta_j\widehat N_{j+1}^{[m]}.
\tag{3.4}
$$
同时全部 $\widehat N_j^{[m]}$ 两两交换：低一层的块系数是上一层算子的解析函数，归纳后即得。
因此 $\widehat N_j^{[m]}$ 幂零，其幂零阶至多 $2^{m-j}$；
更高 $\widehat N_k^{[m]}$ 是 $\widehat N_j^{[m]}$ 的非零常数倍幂。

### 3.2 截断极限及纯主项

对 $\|R\|,\|Q\|\le1$，幂差恒等式及系数和给
$$
\begin{aligned}
&\|a(\eta_jR)-a(\eta_jQ)\|
+\|c(\eta_jR)-c(\eta_jQ)\|\\
&\hspace{15mm}\le
\frac{2\eta_j}{(1-\eta_j)^2}\|R-Q\|
\le4\eta_j\|R-Q\|.
\end{aligned}
\tag{3.5}
$$
这也不要求 $R,Q$ 彼此交换。

令 $\eta_*=\sup_j\eta_j<1/100$。
比较两个终端 $m'>m$，递归 (3.5) 给
$$
\|\widehat N_j^{[m']}-\widehat N_j^{[m]}\|
\le\frac35\,4^{m-j}\prod_{i=j}^{m-1}\eta_i
\quad(j<m),
\tag{3.6}
$$
在两种范数中同时成立。因此存在相同矩阵的范数极限
$\widehat N_j$，且
$$
\boxed{
\|\widehat N_j-\widehat N_j^{[m]}\|
\le4\eta_{m-1}(4\eta_*)^{m-j-1}\quad(j<m).
}
\tag{3.7}
$$
极限保留 (3.3)、平方关系及全部交换关系：
$$
\widehat N_j^2=\eta_j\widehat N_{j+1}.
\tag{3.8}
$$

在 (3.1) 中把子算子置零，得到局部矩阵
$$
\frac14\begin{pmatrix}1&-1\\1&-1\end{pmatrix}
=\frac12E_j^*,
\tag{3.9}
$$
最后一个等号是在原 Haar Walsh 坐标中书写。
由非恒定 Taylor 系数的绝对和，
$$
\boxed{\|\widehat N_j-\tfrac12E_j^*\|\le3\eta_j.}
\tag{3.10}
$$

该模仍具有真实平方关系 (3.8)。它不是把原算子直接改成平方零模型，也没有声称它来自 UHF 的正或星同态。

## 4. 完整正常右模恒等式

对 $p\in\ell^1(\mathfrak F_j)$ 定义
$$
\Lambda_j(p)(T)=\sum_{F\in\mathfrak F_j}
p_F\langle T\chi_F,\chi_F\rangle,\qquad T\in\mathscr C_j.
\tag{4.1}
$$
其范数至多 $\|p\|_1$。

**命题4.1。**
$$
\boxed{
\Lambda_j(\widehat N_jp)(T)=\Lambda_j(p)(N_jT)
\quad(p\in\ell^1,\ T\in\mathscr C_j).
}
\tag{4.2}
$$
这是在交换子测试代数上的泛函恒等式；并不说矩阵 $\rho_pN_j$ 本身是 Walsh 对角算子。

**证明。** 先用有限终端 $\widehat N_j^{[m]}$。记其 (4.2) 的最大缺陷为
$$
\delta_j^{[m]}=
\sup_{\|p\|_1\le1,\ \|T\|\le1}
\left|\Lambda_j(p)(N_jT)
-\Lambda_j(\widehat N_j^{[m]}p)(T)\right|.
\tag{4.3}
$$
在终端 $j=m$，有 $\delta_m^{[m]}\le1$。

若某层的缺陷为 $\delta$，则对该层的每个正整数 $n$，准确 telescoping 给
$$
\left|
\Lambda(p)(N^nT)-\Lambda(\widehat N^np)(T)
\right|
\le n\delta\|p\|_1\|T\|.
\tag{4.4}
$$
这里使用 $\|N\|\le1$、$\|\widehat N\|_{\ell^1}\le3/5$，
而 $N^kT$ 仍在同一交换子代数中。
(4.4) 也可对 $n$ 归纳，不涉及未界算子。

把 $p$ 按第 $j$ 位拆成 $(p_0,p_1)$。
对 (1.5) 的 $T$，(2.2) 将 $\Lambda_j(p)(N_jT)$ 写成
$$
\begin{aligned}
&\Lambda_{j+1}(p_0)\bigl(a(t)A+c(t)D\bigr)\\
&\quad+\Lambda_{j+1}(p_1)\bigl(-c(t)A-a(t)D\bigr).
\end{aligned}
\tag{4.5}
$$
另一方面，(3.1) 对应的权重为
$$
\binom{
a(\eta_j\widehat N_{j+1}^{[m]})p_0
-c(\eta_j\widehat N_{j+1}^{[m]})p_1}{
c(\eta_j\widehat N_{j+1}^{[m]})p_0
-a(\eta_j\widehat N_{j+1}^{[m]})p_1}.
\tag{4.6}
$$
在 $a,c$ 的绝对收敛幂级数中逐项使用 (4.4)，且
$\|A\|,\|D\|\le\|T\|$。由于
$$
\sum_{n\ge1}n\bigl(|a_n|+|c_n|\bigr)\eta_j^n
=\frac{2\eta_j}{(1-\eta_j)^2}\le4\eta_j,
$$
得到
$$
\delta_j^{[m]}\le4\eta_j\delta_{j+1}^{[m]}.
\tag{4.7}
$$
所以
$$
\delta_j^{[m]}\le4^{m-j}\prod_{i=j}^{m-1}\eta_i\longrightarrow0.
$$
结合 $\widehat N_j^{[m]}\to\widehat N_j$ 的 $\ell^1$ 算子范数收敛，
即得 (4.2)。证毕。

由 (4.2) 反复应用，任意多项式，以及在实际侧和模侧均按算子范数收敛的级数，都具有同样的右模恒等式。
特别置
$$
\widehat Y_j=\widehat N_j(I+\widehat N_j)^{-1}.
\tag{4.8}
$$
有 $\|\widehat Y_j\|\le3/2$。
实际侧 $\sum_{n\ge1}\|N_j^n\|<\infty$，由 $N_j^2$ 的范数不超过 $\eta_j$ 即可证明；
模侧则由 $\|\widehat N_j\|\le3/5$ 得几何收敛。
因此
$$
\boxed{
\Lambda_j(\widehat Y_jp)(T)
=\Lambda_j(p)\bigl(N_j(I+N_j)^{-1}T\bigr).
}
\tag{4.9}
$$
所有高位算子都是 $N_0$ 的幂或解析函数，故这些等式在全空间的 $\Lambda=\Lambda_0$ 上同时成立。

## 5. 精确对角柱测试及 $\Lambda$ 的单射性

**命题5.1。** $\Lambda$ 在 $\ell^1(\mathfrak F)$ 上单射。甚至只需其在 $\mathcal A$ 上为零，即可推出 $p=0$。

**证明。** 定义真实有理函数
$$
J_j=2N_j(I+N_j^2)^{-1}\in\mathcal A.
\tag{5.1}
$$
由 (1.3)，其 Walsh 块准确为
$$
\boxed{
J_j=
\begin{pmatrix}
I&(I-t)(I+t)^{-1}\\
-(I-t)(I+t)^{-1}&-I
\end{pmatrix}.
}
\tag{5.2}
$$
其两个对角块恰为 $I,-I$，没有 $O(\eta_j)$ 误差。

对有限集合 $K$，所有更高 $J_k$ 在最低位 $j=\min K$ 上张量恒等。
因此先按这个最低位取对角，再递归处理余下位，得到
$$
\boxed{
\langle J_K\chi_F,\chi_F\rangle
=\sigma_K(F),\quad
J_K=\prod_{j\in K}J_j,\quad
\sigma_K(F)=(-1)^{|K\cap F|}.
}
\tag{5.3}
$$
这里只对这种已验证的不同位乘积逐次剥离；没有使用一般的“取对角保乘法”。

于是对任意低 $m$ 位模式 $G\subset[0,m)$，
$$
Q_{m,G}
=\prod_{j<m}\frac{I+\sigma_j(G)J_j}{2}\in\mathcal A
$$
具有准确对角
$$
\langle Q_{m,G}\chi_F,\chi_F\rangle
=\mathbf1_{\{F\cap[0,m)=G\}}.
\tag{5.4}
$$
若 $\Lambda(p)|_{\mathcal A}=0$，(5.4) 给全部有限柱质量为零。
固定任意有限 $F_0$，令 $G=F_0\cap[0,m)$ 后 $m\to\infty$。
对每个有限 $F$，相应示性函数趋于 $\mathbf1_{\{F=F_0\}}$；
它们绝对值不超过一。由 $\sum_F|p_F|<\infty$ 的支配收敛，
$$
p_{F_0}=0.
$$
这里不需要 $Q_{m,G}$ 的算子范数统一有界；被支配的是准确的对角值。
由于 $F_0$ 任意，命题得证。证毕。

## 6. 两个慢符号在模上的实际算子

在 $\ell^1$ 与 $H$ 上同时定义
$$
\widehat S_N=\sum_{j\ge0}b_j\widehat N_j,\qquad
\widehat S_Y=\sum_{j\ge0}b_j\widehat Y_j,
\qquad b_j=(j+1)^{-2}.
\tag{6.1}
$$
两级数均按算子范数绝对收敛，范数统一小于 $3$。
由第4节及 $\ell^1$ 可和性，
$$
\boxed{
\Lambda(\widehat S_\bullet p)(T)
=\Lambda(p)(S_\bullet T)
\quad(T\in\{A\}').
}
\tag{6.2}
$$

接下来证明
$$
\boxed{\ker_H\widehat S_N=\ker_H\widehat S_Y=\{0\}.}
\tag{6.3}
$$
不能仅由 (3.10) 的小范数差推出 (6.3)，所以后两节完整给出所需尾估计。

### 6.1 真实低头截断及统一误差

对给定 $k$，在 (3.1) 的终端 $k$ 上置
$$
\widehat Y_j^{[k]}
=\widehat N_j^{[k]}(I+\widehat N_j^{[k]})^{-1}.
$$
对两模型分别令
$$
G_k=\sum_{j<k}b_j\widehat N_j^{[k]}
\quad\text{或}\quad
G_k=\sum_{j<k}b_j\widehat Y_j^{[k]}.
$$
每个更高截断幂是 $\widehat N_0^{[k]}$ 的常数倍幂；
$\widehat Y_j^{[k]}$ 也为该幂零矩阵的零常数多项式。
因此
$$
\boxed{G_k^{2^k}=0,\qquad \|G_k\|<3.}
\tag{6.4}
$$

(3.7) 与 $\sum_j b_j<2$ 给 $N$ 模型的低头误差小于
$8\eta_{k-1}$。
逆差恒等式和
$\|(I+\widehat N)^{-1}\|\le5/2$
使 $Y$ 模型的低头误差小于 $50\eta_{k-1}$。

对高位，(3.10) 已给 $N$ 模型误差 $3\eta_j$。
由于 $(E_j^*)^2=0$，
$$
(\tfrac12E_j^*)(I+\tfrac12E_j^*)^{-1}=\tfrac12E_j^*,
\qquad \|(I+\tfrac12E_j^*)^{-1}\|\le3/2.
$$
再用逆差恒等式，得到
$$
\|\widehat Y_j-\tfrac12E_j^*\|
\le(5/2)(3/2)\,3\eta_j<12\eta_j.
\tag{6.5}
$$
于是两模型都满足
$$
\boxed{
\left\|\widehat S_\bullet-
\left(G_k+\frac12\sum_{j\ge k}b_jE_j^*\right)\right\|
\le100\eta_{k-1}.
}
\tag{6.6}
$$
右侧控制整个算子的范数，而不只某个指定矩阵元。

## 7. 双尺度加权多项式估计排除模上的核

本节使用 [R60](../results/R60-critical-multiplier-injective-dense-and-cyclic.md)
§§1–3 已完整证明的两个标量输入。重列其全部用到的量：
$$
g_0=\log\frac{\sqrt{20}+1}{\sqrt{20}-1},\qquad
d\omega_0(u)=\frac{\sqrt{20}}{\pi u\sqrt{(u-1)(20-u)}}\,du,
$$
$$
h(u)=\frac12\int_1^\infty
\log\left(1-\frac{u}{x^2}+\frac{u^2}{2x^4}\right)\,dx.
\tag{7.1}
$$
$\omega_0$ 为概率测度。次数至多 $d$ 的多项式 $p$ 满足
$$
\log|p(0)|\le d g_0+\int_1^{20}\log|p(u)|\,d\omega_0(u),
\tag{7.2}
$$
且严格证书给
$$
\boxed{
g_0+\int_1^{20}h(u)\,d\omega_0(u)<-13/100.
}
\tag{7.3}
$$
(7.3) 的完整有理/区间证书见
[常数证书](../notes/2026-11-12-critical-negative-integral-certificate-0c.md)。
本稿只改变尾系数的归一化时间，并逐项核对新的误差。

令 $M=m+1$，取
$$
k=\left\lfloor\frac34\log_2 M\right\rfloor,
\quad
H_{k,m}=G_k+\frac12\sum_{j=k}^{m-1}b_jE_j^*,
\quad
C_m=\frac12\sum_{j\ge m}b_jE_j^*.
\tag{7.4}
$$
当 $M$ 充分大时，$1\le k<m$。三段作用于不交的头、中、尾，所以
$$
H_{k,m}^{\,2^k+m-k}=0,\qquad
d_m:=2^k+m-k-1\le M+M^{3/4},
$$
$$
\|H_{k,m}\|+\|C_m\|<8.
\tag{7.5}
$$
这里真实低头只截到 $k$ 位，没有把 $2^m$ 阶真实有限链写成 $m$ 次多项式。

在参考向量 $1$ 上，尾指数的范数准确为
$$
F_m(t):=\|e^{-tC_m^*}1\|
=\prod_{j\ge m}
\left(1-\frac{t b_j}{2}+\frac{t^2b_j^2}{8}\right)^{1/2}.
\tag{7.6}
$$
置 $t=2uM^2$，$1\le u\le20$。
令 $\ell(q)=\tfrac12\log(1-q+q^2/2)$，有
$|\ell'(q)|\le1/2$。
对 $f_u(x)=\ell(u/x^2)$，$|\partial_x f_u(x)|\le u/x^3$。
长度 $1/M$ 的左端点 Riemann 和误差因而满足
$$
\boxed{|\log F_m(2uM^2)-Mh(u)|\le u/2\le10.}
\tag{7.7}
$$
同时 $|\ell(q)|\le q/2$ 给 $h(u)\ge-u/2$，故
$$
F_m(2uM^2)\ge e^{-10M-10}.
\tag{7.8}
$$

取 $f\in\ker\widehat S_\bullet$。
由 (6.6)，$\|(H_{k,m}+C_m)f\|\le100\eta_{k-1}\|f\|$。
因 $H_{k,m},C_m$ 交换，准确积分式给
$$
e^{tH_{k,m}}f-e^{-tC_m}f
=\int_0^t e^{(t-s)H_{k,m}}e^{-sC_m}
(H_{k,m}+C_m)f\,ds.
$$
所以误差范数至多
$$
100t e^{8t}\eta_{k-1}\|f\|.
\tag{7.9}
$$
$16^{k-1}\ge M^3/256$，故 $\eta_{k-1}\le e^{-3M^3}$。
在 $t\le40M^2$ 上，(7.9) 除以 $\|f\|$ 后不超过
$$
4000M^2e^{320M^2-3M^3}\le e^{-20M}
\tag{7.10}
$$
对全部充分大的 $M$ 成立，例如 $M\ge128$ 已足够。
该误差也小于 (7.8)。

令
$$
p_m(u)=\langle e^{2uM^2H_{k,m}}f,1\rangle.
$$
这是次数不超过 $d_m$ 的多项式，且 $p_m(0)=\langle f,1\rangle$。
(7.7)—(7.10) 给
$$
|p_m(u)|\le2\|f\|e^{Mh(u)+10},\qquad1\le u\le20.
$$
用 (7.2)—(7.3) 得
$$
|\langle f,1\rangle|
\le2\|f\|\exp\left(10-\frac{13}{100}M+g_0M^{3/4}\right)
\longrightarrow0.
$$
因此两种模上的核都与 $1$ 正交。

### 7.1 从一个真空配对推广到全部核

定义
$$
U_j=I-4\widehat N_j.
$$
它们两两交换，保持 $\ker\widehat S_\bullet$，且 $\|U_j\|<4$。
由 (3.10)，
$$
\|U_j^*-(I-2E_j)\|\le12\eta_j.
\tag{7.11}
$$
纯因子 $(I-2E_j)$ 在参考向量上产生 $\chi_j$。

下面明确支付全次数合成。
对有限 Walsh 多项式 $x$，按首次误差位 $j$ 展开
$U_F^*1-\chi_F$。
对每个 $K\subset[0,j)$，令
$$
Q_{j,K}
=|1_{[0,j]}\rangle\langle\chi_{K\cup\{j\}}|\otimes I_{>j}.
$$
它先把给定低头 Walsh 块换回参考真空，保留全部高尾系数。
有
$\sum_{K\subset[0,j)}\|Q_{j,K}x\|^2\le\|x\|^2$。
实际前缀范数不超过 $4^{|K|}$；误差位付 $12\eta_j$；
后方纯乘积作用于参考真空仍是正交 Walsh 向量。
因此由 Cauchy–Schwarz，线性合成映射
$$
\mathcal W\chi_F=U_F^*1
$$
满足
$$
\boxed{
\|\mathcal W-I\|
\le12\sum_{j\ge0}\eta_j17^{j/2}<1.
}
\tag{7.12}
$$
具体地，固定 $j$ 的系数平方和是
$\sum_K16^{|K|}=17^j$，其余误差和由 (1.2) 绝对收敛。
所以 $\mathcal W$ 有界可逆，$\{U_F^*1\}$ 的张成在 $H$ 中稠密。

对 $f\in\ker\widehat S_\bullet$，每个 $U_Ff$ 仍在该核内。
前面已证其与 $1$ 正交，于是
$$
\langle f,U_F^*1\rangle=\langle U_Ff,1\rangle=0
\quad\text{对全部有限 }F.
$$
稠密性迫 $f=0$。这完成 (6.3)，没有使用未证明的纯核投影极限。

## 8. 主定理、正常性范围及独立例子

假设 (0.3) 的湮灭条件成立。
由 (6.2)，
$$
\Lambda(\widehat S_\bullet p)(F)=0\quad(F\in\mathcal A).
$$
$\widehat S_\bullet$ 在 $\ell^1$ 上有界，所以其输出仍在 $\ell^1$。
命题5.1给
$$
\widehat S_\bullet p=0.
$$
另一方面 $\ell^1(\mathfrak F)\subset\ell^2(\mathfrak F)=H$，
且同一矩阵在两空间中的有界延拓相容。
故 (6.3) 迫 $p=0$。主定理得证。

这里对角序列可以任意复数，因而结论也排除非正的非零对角正常泛函。
对一般非对角迹类算子，本稿没有建立这样的 $\ell^1$ 模表示；
不能因此宣称任意正常泛函都被排除。

这条结果超出次数指数矩类。
例如取互不相交的有限集合 $F_n$，$|F_n|=n$，并取
$$
p_{F_n}=\frac{1}{c\,n^2},\qquad
c=\sum_{n\ge1}n^{-2},\qquad p_F=0\text{ 对其余 }F.
$$
则 $\rho_p\ge0$、$\operatorname{Tr}\rho_p=1$，但对每个 $r>1$，
$$
\sum_F r^{2|F|}p_F=\infty.
$$
它不满足 R230 的任何次数指数矩条件。

这个例子也不保持函数非负锥：$\rho_p1=0$，而 $\rho_p\ne0$。
如果它保函数正锥，则对每个有界实函数 $f$，
$-\|f\|_\infty1\le f\le\|f\|_\infty1$ 会迫 $\rho_pf=0$；
再由有界函数在 $L^2$ 的稠密性迫 $\rho_p=0$，矛盾。
故它也不属于 R235 的保锥密度类。
本稿仍将它排除为两种实际慢符号的湮灭者。

## 9. 未合并的边界

本稿没有把对角模块 $\widehat N_j$ 认作原 $N_j$ 的有界相似变换，也不声称它是 UHF 星表示的像。第4节仅建立在 $\{A\}'$ 上测试的右模恒等式；这已足以应用第5节的注入测试。

R210–R211 的实际奇异正状态不由 (0.1) 的 $\ell^1$ 序列给出，所以与本稿没有冲突。那些状态的配置原子极限不受本稿的支配收敛控制。

一般非对角正常正态、任意有限秩正常见证、未知不变子商的全部范围缺口，以及普通 Hilbert 不变子空间问题仍未解决。有限 Walsh 带宽的非对角泛函若要化到这里，必须另付实际尾块逆的模作用；不能照抄纯模型的有限翻转公式。
