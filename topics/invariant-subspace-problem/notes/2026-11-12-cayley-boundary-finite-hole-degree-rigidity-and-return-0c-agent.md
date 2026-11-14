# R206：Cayley 边界符号的全有限孔次数刚性与有限次数返回

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整实际算子证明。

本稿完成 R205 留下的 $p\ge3$ 分支。核心是实际多源尾和的逐层消元，以及一个有限多项式降阶引理。结论在负整数边界表示内成立；不由此断言边界饱和 $N=M$，也不把边界结论移植到原 Haar 空间。

## 1. 主结论与系数范围

沿用 R174、R188、R205 的边界模型
$$
\mathcal H_-=\ell^2(\mathbb N_0),\qquad
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),
$$
以及
$$
W_n=\prod_{\nu=1}^n\alpha_{v_2(\nu)},\qquad
d_j=W_{2^j},\qquad
\mathsf N_j=B^{2^j}/d_j,\qquad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1}.
$$
对有限集 $S$ 记 $n(S)=\sum_{j\in S}2^j$、$e_S=e_{n(S)}$，并定义
$$
\mathcal H^-_{\le p}
=\overline{\operatorname{span}}\{e_S:|S|\le p\},
\qquad
\mathcal F_m=\operatorname{span}\{e_n:0\le n<2^m\}.
\tag{1.1}
$$
这是边界孔次数，不是原 Haar 表示的 Walsh 次数。

本稿的具体慢符号为
$$
T_Y=\sum_{j\ge0}\frac1{(j+1)^2}\mathsf Y_j.
\tag{1.2}
$$

**定理1.1（全有限次数的核与返回刚性）。**

1. 对每个有限 $p$，
   $$
   \boxed{\ker T_Y\cap\mathcal H^-_{\le p}=\mathbb Ce_0.}
   \tag{1.3}
   $$
2. 若 $x$ 与 $T_Yx$ 都有某个有限孔次数，则 $x$ 属于一个有限物理头。反过来，有限头输入的输出仍在同一有限头。

所以，R188 已构造的每个非真空边界核向量都必须具有任意高的孔次数。

为执行尾递归，证明使用稍宽的系数族：
$$
T_a=\sum_{j\ge0}a_j\mathsf Y_j,
\qquad a\in\ell^1,\qquad a_j\ne0\ \text{对每个 }j.
\tag{1.4}
$$
全部证明对 (1.4) 成立，允许任意复相位。每一层系数非零是本稿明确使用的条件；不把它改成未经证明的一般无限支撑条件。
由于 $\|\mathsf Y_j\|\le3$，(1.4) 按算子范数绝对收敛。

## 2. 最低位实际分块与奇分量问题

按最低位写
$$
e_{2n}\leftrightarrow(e_n,0),\qquad e_{2n+1}\leftrightarrow(0,e_n).
$$
令
$$
\beta=\alpha_0,\qquad Ce_n=\omega_ne_{n-1},\qquad
\omega_n=\alpha_{1+v_2(n)},\qquad Q=C/\beta.
$$
尾权记为
$$
\widehat W_n=\prod_{\nu=1}^n\omega_\nu,
\qquad \delta_j=\widehat W_{2^j},\qquad
\widehat{\mathsf N}_j=C^{2^j}/\delta_j,
\qquad
\widehat{\mathsf Y}_j=\widehat{\mathsf N}_j(I+\widehat{\mathsf N}_j)^{-1}.
\tag{2.1}
$$
R205 的实际分块，也可直接由加权后移逐列计算，给
$$
\mathsf Y_0=(I-Q)^{-1}\begin{pmatrix}-Q&I\\Q&-Q\end{pmatrix},
\qquad
\mathsf Y_j=I_2\otimes\widehat{\mathsf Y}_{j-1}\quad(j\ge1).
$$
这里 $\|Q\|=\alpha_1/\alpha_0<1$，所以所有逆合法。
把算子与输出都除以 $a_0$，并置
$$
b_j=a_{j+1}/a_0,\qquad D=\sum_{j\ge0}b_j\widehat{\mathsf Y}_j,
$$
则
$$
\boxed{
\frac{T_a}{a_0}
=(I-Q)^{-1}
\begin{pmatrix}(I-Q)D-Q&I\\Q&(I-Q)D-Q\end{pmatrix}.
}
\tag{2.2}
$$

设
$$
x=(u,v)\in\mathcal H^-_{\le p},\qquad
f=\frac{T_ax}{a_0}=(f_0,f_1)\in\mathcal H^-_{\le s},
\tag{2.3}
$$
其中 $p,s$ 都有限。最低位为1占用一个孔，因此
$$
u\in\widehat{\mathcal H}^-_{\le p},\quad
v\in\widehat{\mathcal H}^-_{\le p-1},\quad
f_0\in\widehat{\mathcal H}^-_{\le s},\quad
f_1\in\widehat{\mathcal H}^-_{\le s-1}.
\tag{2.4}
$$
$s=0$ 时最后一式理解为 $f_1=0$。
令 $g=Dv$。由 (2.2) 下行，
$$
Qu=Qv-g+Qg+(I-Q)f_1.
\tag{2.5}
$$
坐标 $n-1$ 上的等式是
$$
u_n=v_n+g_n-\frac\beta{\omega_n}g_{n-1}
+\frac\beta{\omega_n}\bigl((I-Q)f_1\bigr)_{n-1}.
\tag{2.6}
$$
记 $\nu(n)$ 为二进位1的数目，并置
$$
H=\max(p+1,s).
$$
若 $\nu(n),\nu(n-1)\ge H$，则 $u_n=v_n=0$，且
$$
\bigl((I-Q)f_1\bigr)_{n-1}
=(f_1)_{n-1}-\frac{\omega_n}{\beta}(f_1)_n=0.
$$
于是得到真实行约束
$$
\boxed{g_n-\frac\beta{\omega_n}g_{n-1}=0.}
\tag{2.7}
$$

下面证明的核心命题是：在 (2.3) 的条件下，奇分量 $v$ 必有有限头。$p\le1$ 时它已经是真空标量，故以下只需 $p\ge2$。

## 3. 实际系数与所有多源尾和的绝对收敛

令 $d=p-1\ge1$。$v$ 支持在 $\nu(n)\le d$ 上。
有限头上的逆是有限多项式，所以 $D$ 的真实形式系数为
$$
t_k=\sum_{\ell:\,2^\ell\mid k}
b_\ell(-1)^{k/2^\ell-1}\delta_\ell^{-k/2^\ell},
\qquad k\ge1,
\qquad t_0=0.
\tag{3.1}
$$
每个固定 $k$ 的和都是有限和；不要求这个形式幂级数在复平面有正收敛半径。
实际矩阵行是
$$
g_n=\frac1{\widehat W_n}
\sum_{z>n}v_z\widehat W_z t_{z-n}.
\tag{3.2}
$$
由于 $D$ 有界，这个坐标和首先由行的 $\ell^2$ 范数与 Cauchy–Schwarz 得到绝对收敛。

后面还需要把有限个 Cayley 层分别求和。这里给统一的完整估计。
实际 ruler 权满足
$$
\widehat W_{n(S)}=\prod_{j\in S}\delta_j.
\tag{3.3}
$$
例如 $0\le n<2^j$ 时 $\widehat W_{2^j+n}=\delta_j\widehat W_n$，按最高二进位逐次递推即得 (3.3)。

固定一层 $\ell$，置
$$
r_{\ell,j}=\delta_j\delta_\ell^{-2^{j-\ell}}.
$$
对 $j\ge\ell+1$，按长度 $2^\ell$ 分组实际权，奇数块的乘积为 $\delta_\ell$，偶数块至多额外乘 $\alpha_{\ell+2}/\alpha_{\ell+1}$。因此
$$
0<r_{\ell,j}
\le\left(\frac{\alpha_{\ell+2}}{\alpha_{\ell+1}}\right)^{2^{j-\ell-1}}.
\tag{3.4}
$$
较低 $j$ 只有有限项，故
$$
K_\ell:=\sum_{j\ge0}r_{\ell,j}^2<\infty.
$$
由 (3.3)，
$$
\begin{split}
\sum_{\nu(z)\le d}
\left(\widehat W_z\delta_\ell^{-z/2^\ell}\right)^2
&=\sum_{|S|\le d}\prod_{j\in S}r_{\ell,j}^2\\
&\le\sum_{k=0}^d\frac{K_\ell^k}{k!}<\infty.
\end{split}
\tag{3.5}
$$
再与 $v\in\ell^2$ 配对，得到
$$
\boxed{
\sum_{\nu(z)\le d}|v_z|\widehat W_z\delta_\ell^{-z/2^\ell}<\infty.
}
\tag{3.6}
$$
附加任意余数条件、符号或高位截断都不影响绝对收敛。下面所有逐层尾和、有限层重排和相邻尾相减均由 (3.6) 支付。

## 4. 共享全部源指标的真实多行系统

固定层 $\ell\ge0$ 和余数 $0\le h<2^\ell$。置
$$
L=\ell+d+1.
$$
对满足
$$
\boxed{
r\ge \ell+d+H+3+\lceil\log_2L\rceil
}
\tag{4.1}
$$
的整数 $r$，选择 $L$ 条行
$$
n_t=2^r-2^\ell+h-t2^L,
\qquad 0\le t<L.
\tag{4.2}
$$

### 4.1. 每条行都可使用 (2.7)

写
$$
\kappa_t=2^\ell-h+t2^L,
\qquad n_t=2^r-\kappa_t.
$$
有 $1\le\kappa_t\le L2^L$。
二进位取补给
$$
\nu(n_t)=r-\nu(\kappa_t-1),\qquad
\nu(n_t-1)=r-\nu(\kappa_t).
$$
因为 $\kappa_t\le L2^L$，两者都至少为
$$
r-L-\lceil\log_2L\rceil-1\ge H.
\tag{4.3}
$$
所以所有行都满足 (2.7)。

### 4.2. 所有行共享同一尾部 $z\ge2^r$

在 $0\le z<2^r$ 中，孔次数不超过 $d$ 的最大整数是
$$
2^r-2^{r-d}.
$$
(4.1) 及 $H\ge d+2$ 保证
$$
\kappa_t+1<2^{r-d},
$$
故 $n_t-1>2^r-2^{r-d}$。
所以 (3.2) 中 $g_{n_t}$ 与 $g_{n_t-1}$ 的所有非零源，在每条行上都恰可统一为
$$
z\ge2^r,
\qquad \nu(z)\le d.
\tag{4.4}
$$
这一步没有把不同尾截断误当成同一个和。

### 4.3. 所有源的两个进位层都严格小于 $L$

每个 (4.4) 中的 $z$ 至少有一个不低于 $r$ 的孔，而 $r>L$。因此其低 $L$ 位至多有 $d-1$ 个孔。
另一方面，$n_t$ 的低 $L$ 位与 $t$ 无关，等于
$$
2^L-2^\ell+h.
$$
其孔数为 $d+1+\nu(h)$，至少为 $d+1$。
若 $h\ge1$，$n_t-1$ 的低 $L$ 位至少也有 $d+1$ 个孔；
若 $h=0$，该孔数为
$$
(L-\ell-1)+\ell=d+\ell\ge d.
$$
故 $z$ 不可能与 $n_t$ 或 $n_t-1$ 模 $2^L$ 同余。于是
$$
\boxed{
v_2(z-n_t)<L,\qquad v_2(z-n_t+1)<L.
}
\tag{4.5}
$$
两个差均为正，所以这里没有对零取赋值。

乘 (2.7) 以 $\widehat W_{n_t}$，并用 $\omega_{n_t}=\widehat W_{n_t}/\widehat W_{n_t-1}$，得到
$$
\boxed{
\sum_{z\ge2^r}v_z\widehat W_z
\bigl(t_{z-n_t}-\beta t_{z-n_t+1}\bigr)=0.
}
\tag{4.6}
$$
(4.5) 说明它只涉及第 $0,\ldots,L-1$ 个 Cayley 层。

## 5. Vandermonde 分层与全部余数尾和消失

当 $t$ 增加1，两个指数 $z-n_t$ 和 $z-n_t+1$ 都增加 $2^L$。
对固定层 $j<L$，整除条件不变；由于 $2^{L-j}$ 为偶数，(3.1) 中的符号也不变。该层的整个尾和仅乘
$$
\lambda_{j,L}=\delta_j^{-2^{L-j}}.
\tag{5.1}
$$
因此 (4.6) 精确成为
$$
\sum_{j=0}^{L-1}Z_j\lambda_{j,L}^{t}=0,
\qquad 0\le t<L,
\tag{5.2}
$$
其中 $Z_j$ 是第 $t=0$ 行的第 $j$ 层完整尾和。
(3.6) 保证这一步合法；没有令各源分别满足方程。

实际权满足
$$
\frac{\delta_{j+1}}{\delta_j^2}
=\frac{\alpha_{j+2}}{\alpha_{j+1}}<1.
$$
所以
$$
\rho_j:=\delta_j^{-1/2^j}
$$
严格递增，而 $\lambda_{j,L}=\rho_j^{2^L}$ 两两不同。
(5.2) 的 Vandermonde 矩阵可逆，故每个 $Z_j=0$，特别 $Z_\ell=0$。

固定此 $r,\ell$，定义全部余数尾和
$$
F_{\ell,h}(r)=
\sum_{\substack{z\ge2^r\\z\equiv h\;({\rm mod}\;2^\ell)}}
v_z\widehat W_z(-\delta_\ell)^{-\lfloor z/2^\ell\rfloor},
\qquad 0\le h<2^\ell.
\tag{5.3}
$$
它们绝对收敛，由 (3.6) 只多一个固定余数因子。
令 $A_r=2^{r-\ell}-1$，则第 $t=0$ 行是 $n_0=2^\ell A_r+h$。
从 (3.1) 直接提取第 $\ell$ 层，第一项的共同因子是
$$
-b_\ell(-\delta_\ell)^{A_r}F_{\ell,h}(r).
$$
当 $h\ge1$ 时，第二项使用同一个商 $A_r$，所以 $Z_\ell=0$ 给
$$
F_{\ell,h}(r)=\beta F_{\ell,h-1}(r).
\tag{5.4}
$$
当 $h=0$ 时，$n_0-1$ 的商为 $A_r-1$，余数为 $2^\ell-1$；因此
$$
F_{\ell,0}(r)
=-\frac\beta{\delta_\ell}F_{\ell,2^\ell-1}(r).
\tag{5.5}
$$
使用了 $b_\ell\ne0$，其复相位不影响取消。
一周相乘得到
$$
\left(1+\frac{\beta^{2^\ell}}{\delta_\ell}\right)F_{\ell,0}(r)=0.
$$
因为 $\beta,\delta_\ell>0$，括号非零。于是
$$
\boxed{
F_{\ell,h}(r)=0\quad(0\le h<2^\ell)
}
\tag{5.6}
$$
只要 (4.1) 成立。
这里包含 $\ell=0$ 的单余数情形，其系数就是 $1+\beta/\delta_0$。

## 6. 最高孔位区间的有限多项式余式

固定 $r$，定义有限多项式
$$
P_r(z)=\sum_{n=2^r}^{2^{r+1}-1}v_n\widehat W_nz^n,
\qquad Q_r(z)=z^{-2^r}P_r(z).
\tag{6.1}
$$
若 (4.1) 对某层 $\ell$ 成立，它对 $r+1$ 也成立。
相减 (5.6) 的相邻尾，得到每个余数 $h$ 的有限等式
$$
\sum_{\substack{2^r\le n<2^{r+1}\\n\equiv h\;({\rm mod}\;2^\ell)}}
v_n\widehat W_n(-\delta_\ell)^{-\lfloor n/2^\ell\rfloor}=0.
\tag{6.2}
$$
这些恰是 $P_r$ 对 $z^{2^\ell}+1/\delta_\ell$ 的全部余式系数。
因该除式的常数非零，它与 $z^{2^r}$ 互素，故
$$
\boxed{1+\delta_\ell z^{2^\ell}\ \text{整除}\ Q_r(z).}
\tag{6.3}
$$

每个 $P_r$ 单项式已经占用最高孔 $r$。因此 $Q_r$ 能唯一写成
$$
Q_r(z)=\mathcal P_r(z,z^2,z^4,\ldots,z^{2^{r-1}}),
\tag{6.4}
$$
其中 $\mathcal P_r(x_0,\ldots,x_{r-1})$ 是 multiaffine 多项式，总次数至多
$$
D=d-1=p-2.
\tag{6.5}
$$
唯一性来自不同平方自由单项式的二进位指数互异。

(6.3) 不仅是某个点上的零值。它使每个低 $\ell$ 位余式系数为零，所以等价于完整多项式恒等式
$$
\boxed{
\mathcal P_r\bigl(x_0,\ldots,x_{\ell-1},
-\rho_\ell^{2^\ell},
\rho_\ell^{2^{\ell+1}},\ldots,
\rho_\ell^{2^{r-1}}\bigr)\equiv0.
}
\tag{6.6}
$$
其中 $\rho_\ell=\delta_\ell^{-1/2^\ell}>0$。低位变量自由的理由是：余式中的不同低位平方自由单项式仍对应不同的 $0,\ldots,2^\ell-1$ 次幂。

下面给出从这些余式到 $\mathcal P_r=0$ 的完整有限代数步骤，不跳过重分块时的交叉项。

## 7. 有限 multiaffine 多项式的降阶引理

先记一个初等零点事实。

**引理7.1。** 含至多 $M$ 个非零单项式的非零复多项式，在正实轴上至多有 $M-1$ 个不同零点。

**证明。** 乘一个标量后取非零实部，化为实多项式，正实零点全部保留，单项式数不增加。
对实多项式按单项式数归纳。除以最低次幂后，常数项非零；若有 $k$ 个正实零点，其导数有至少 $k-1$ 个正实零点。导数至多有 $M-1$ 项，归纳给 $k-1\le M-2$。单项式情形显然。证毕。

定义
$$
\mathfrak m(n,q)=\sum_{j=0}^{q}\binom nj,
$$
其中 $j>n$ 时二项式系数取0。

**引理7.2（完整降阶）。**
设 $\mathcal P\in\mathbb C[x_0,\ldots,x_{r-1}]$ 为 multiaffine 多项式，总次数至多 $D$。
给定 $0\le K_0<r$ 与不同的正实数 $\rho_0,\ldots,\rho_{K_0}$，假设对每个 $0\le\ell\le K_0$，
$$
\mathcal P(x_{<\ell},-\rho_\ell^{2^\ell},
\rho_\ell^{2^{\ell+1}},\ldots,\rho_\ell^{2^{r-1}})\equiv0.
\tag{7.1}
$$
置
$$
n_0=r-K_0,\qquad
n_q=n_{q-1}+\mathfrak m(n_{q-1},q),\quad1\le q\le D.
\tag{7.2}
$$
若 $n_D\le r$，则 $\mathcal P=0$。$D=0$ 时，任一条件直接给零。

**证明。** 先看 $\ell=K_0$ 的条件。把前 $K_0$ 个变量称作旧头，其余称作尾。
旧头次数为 $D$ 的系数只能是常数，因为总次数不超过 $D$。
(7.1) 使这些常数全为零。因此旧头次数至多为 $D-1$。

现在进行第 $q$ 轮，$1\le q\le D$。
归纳时旧头长度为
$$
K=r-n_{q-1},
$$
旧头次数至多为 $t=D-q$；尾有 $n_{q-1}$ 个变量。
令
$$
M=\mathfrak m(n_{q-1},q),\qquad K'=K-M.
$$
条件 $n_D\le r$ 保证各轮所需 $K'\ge0$。

若 $t\ge1$，取任意 $S\subseteq\{0,\ldots,K'-1\}$，$|S|=t$。
在原旧头展开中写 $x_S$ 的尾系数为 $\mathcal P_S$；它的尾次数至多为 $D-t=q$。
对每个
$$
\ell=K',K'+1,\ldots,K-1
$$
使用 (7.1)，并提取自由低位单项式 $x_S$ 的系数。
任何额外的旧头因子都将使旧头次数超过 $t$，已由归纳假设为零。
因此该系数方程恰为
$$
\mathcal P_S(\rho_\ell^{2^K},\ldots,\rho_\ell^{2^{r-1}})=0.
\tag{7.3}
$$
这里所有尾变量的指标都严格大于 $\ell$，因此没有负的特殊坐标。

将 $\mathcal P_S$ 中的尾变量代入 $z^{2^K},\ldots,z^{2^{r-1}}$，得到一个至多有 $M$ 项的一元多项式。
二进位指数互异，故此代入忠实。
(7.3) 给 $M$ 个不同正实零点，依引理7.1，此多项式及 $\mathcal P_S$ 都为零。

把旧头最后 $M$ 个变量移动到新尾后，不会重新产生新头次数 $t$ 的项：若一个旧项还含任一被移动的旧头变量，其旧头次数就超过 $t$；这些项早已为零。
新头长度因此为 $K'$，新头次数至多为 $t-1$。
这精确给出下一轮的归纳假设。

最后 $q=D$ 时 $t=0$，多项式已经与整个旧头无关。
同样取 $M$ 个层 $\ell=K-M,\ldots,K-1$，引理7.1 直接使全部剩余尾多项式为零。
此时不再需要另作重分块。证毕。

### 7.1. 只消耗固定次数的多项式数量的头变量

对 $q\ge1$，把一个至多 $q$ 元的子集按顺序放入 $q$ 个位置，并用0填充，可得
$$
\mathfrak m(n,q)\le(n+1)^q.
$$
所以
$$
n_q+1\le2(n_{q-1}+1)^q.
$$
逐步取二进位对数，使用 $\sum_{j=1}^q1/j!<2$，得到
$$
\boxed{n_D+1\le[4(n_0+1)]^{D!}\qquad(D\ge1).}
\tag{7.4}
$$
因此初始尾只含 $O(\log r)$ 个变量时，固定 $D$ 轮消耗仍仅为 $\log r$ 的一个固定次幂。

## 8. 奇分量的有限头结论及明确有限界

回到 (2.3)，$p\ge2$，$d=p-1$，$H=\max(p+1,s)$，$D=p-2$。
定义
$$
C=d+H+4,\qquad
K_0(r)=r-C-\lceil\log_2(r+d+1)\rceil.
\tag{8.1}
$$
当 $K_0(r)\ge0$ 时，每个 $\ell\le K_0(r)$ 都满足 (4.1)，因为
$$
\ell+d+H+3+\lceil\log_2(\ell+d+1)\rceil\le r-1.
$$
所以 (6.6) 提供引理7.2 所需的全部条件。
其初始尾长为
$$
n_0(r)=r-K_0(r)
=C+\lceil\log_2(r+d+1)\rceil.
\tag{8.2}
$$
由 (7.4)，对一切充分大的 $r$，$n_D(r)<r$，从而 $\mathcal P_r=0$。

如需一个不优化的明确界，可取
$$
k=\max(1,D!),\qquad A=d+H+7,
\qquad
\boxed{R_{p,s}=2^{16(A+k^2+1)}.}
\tag{8.3}
$$
对所有 $r\ge R_{p,s}$，令 $t=\log_2r$。
有 $r\ge d+1$，并由 (8.2) 得 $n_0+1\le A+t$。
又有 $t\ge A$、$t\ge16k^2$。
初等不等式 $\log_2x\le\sqrt x$ 对 $x\ge16$ 成立，故
$$
k\log_2[4(A+t)]
\le k(2+\sqrt{2t})<t.
$$
于是 $[4(n_0+1)]^{D!}<r$，同时 $K_0(r)\ge0$。
$D=0$ 时，$\mathcal P_r$ 是常数，任一余式条件已足以使它为零。

因此 $Q_r=0$ 对所有 $r\ge R_{p,s}$ 成立，即 $v$ 的所有最高孔位不低于 $R_{p,s}$ 的部分全为零。
我们证明了：
$$
\boxed{
x\in\mathcal H^-_{\le p},\ T_ax\in\mathcal H^-_{\le s}
\Longrightarrow v\text{ 有限头}.
}
\tag{8.4}
$$
$p\ge2$ 时可用 $v\in\widehat{\mathcal F}_{R_{p,s}}$；$p\le1$ 时 $v$ 本来就是真空标量。
该界不追求数值效率；R205 的二阶具体界远小于它。

若输出本来有有限头，(2.5) 立刻使 $Qu$ 也有有限头。所有后移权非零，再向右恢复一个坐标，就使 $u$ 及 $x$ 都有限头。以下把这一结论进一步推广到任意有限次数输出。

## 9. 有限次数输出时沿全偶分量递归

从精确矩阵 (2.2) 的两行相加，所有 $Q$ 项恰好消去，得到
$$
\boxed{f_0+f_1=D(u+v)+v.}
\tag{9.1}
$$
因此
$$
Du=f_0+f_1-v-Dv.
\tag{9.2}
$$
由 (8.4)，$v$ 有有限头；$D$ 保持每个有限头，所以 $Dv$ 也有有限头。
于是 (9.2) 是一个新的尾问题：输入 $u$ 的孔次数仍至多为原来的 $p$，输出 $Du$ 具有某个有限孔次数。
这个新的输出次数可以大于原来的 $s$，但始终是有限整数。

尾算子 $D$ 的系数仍属于 $\ell^1$，且每一项非零；尾权只是把 $\alpha_j$ 改成 $\alpha_{j+1}$。所以第2—8节可以继续应用。
每一步先把当前算子与输出除以其首系数，不改变孔次数或有限头性质。

固定任意有限整数 $J$，重复这个过程 $J$ 次，只沿每一步的全偶分量前进。
在第 $j$ 步分出的奇分量对应原向量中“最低一个孔恰位于 $j$”的全部系数。
每个这样的分量都有限头，有限个分量之和仍有限头。
因此得到准确结论：
$$
\boxed{
\text{对每个固定 }J，\ x\text{ 中至少一个低 }J\text{ 位有孔的部分具有有限头。}
}
\tag{9.3}
$$
这里没有要求递归过程中所有输出共享原来的次数界；只用每一轮更新后的有限次数来调用 (8.4)。

## 10. 用原输出次数完成最后的等间隔尾消元

现在固定的是原始输出次数 $s$，取
$$
J=s+1\ge1.
$$
使用 (9.3)，选择一个有限 $M\ge J$，足以包含全部低 $J$ 位出现孔的部分。
令
$$
x_{\rm fin}=P_{\mathcal F_M}x,\qquad x_{\rm tail}=x-x_{\rm fin}.
$$
则 $x_{\rm tail}$ 仍有至多 $p$ 个孔，且其支持满足
$$
n\ge2^M,\qquad n\equiv0\pmod{2^J}.
\tag{10.1}
$$
由于 $T_a$ 保持有限头，$T_ax_{\rm fin}\in\mathcal F_M$。
所以在所有高于该有限头的坐标，$T_ax_{\rm tail}$ 与原输出 $T_ax$ 完全相同。
不需要、也不声称 $T_ax_{\rm tail}$ 在全部坐标仍只有原来的次数 $s$。

对每个
$$
N=2^JK\ge2^M+2^J
$$
取行 $n=N-1$。它的低 $J$ 位全为1，故 $\nu(n)\ge J>s$，并且 $n\ge2^M$。因此
$$
(T_ax_{\rm tail})_{N-1}=0.
\tag{10.2}
$$
所有非零源都是 $2^J$ 的倍数，故这一行的源集合恰为 $z\ge N$，并且 $z-(N-1)$ 为奇数。
实际 Cayley 系数的奇数项只有第0层贡献：
$$
[z^k]\,\iota(T_a)=a_0d_0^{-k}\qquad(k\text{ 为奇数}).
$$
所以 (10.2) 精确化为
$$
0=a_0d_0^{N-1}
\sum_{z\ge N}(x_{\rm tail})_zW_zd_0^{-z}.
\tag{10.3}
$$
该尾和绝对收敛，证明与第3节一致，现在对原权和次数 $p$ 使用有限对称积估计。
$a_0\ne0$，故每个这样的尾和都为零。
将相邻阈值 $N,N+2^J$ 的尾和相减，由 (10.1) 其间只有一个允许的源位置，得到
$$
(x_{\rm tail})_NW_Nd_0^{-N}=0.
$$
所有实际权非零，所以 $x_N=0$ 对全部 $N\ge2^M+2^J$ 的允许位置成立。
因此 $x$ 具有有限头；例如剩余的尾至多还有位置 $2^M$，故 $x\in\mathcal F_{M+1}$。
这证明定理1.1 的有限次数返回结论。

## 11. 核、复系数与未解决边界

对任意满足 (1.4) 的系数，有限头上的 $T_a$ 是 $B$ 的无常数多项式，首项为
$$
\frac{a_0}{d_0}B.
$$
故在有限头上 $T_a=BU$，其中 $U$ 是与 $B$ 交换的可逆有限矩阵。
有限头核恰为 $\mathbb Ce_0$。
把前面的返回结论用于零输出，即得
$$
\boxed{\ker T_a\cap\mathcal H^-_{\le p}=\mathbb Ce_0\quad(p<\infty).}
\tag{11.1}
$$
整个证明只在第5节取消各 $b_\ell$ 时要求它们非零，没有使用它们的相位或符号。因此 (1.4) 的复系数推广已经包含在完整证明内。
如果最低非零系数位于 $s_0$，且之后每个系数都非零，可用 R205 附录的实际低 $s_0$ 位块对角分解，得到有限次数核为
$$
\mathcal F_{s_0}\cap\mathcal H^-_{\le p}.
$$
本稿不把此结论推广到有无限多个缺失层的系数列。

对具体慢符号，R188 的无限边界核与 (1.3) 相容：非真空核向量必须有无界孔次数。
这仍不决定
$$
\overline{B\ker T_Y}=\ker T_Y.
$$
有限孔次数空间在全 Hilbert 空间中稠密，不意味着它与这个未知闭核的交在核内稠密。
原 Haar 表示与此负整数边界之间也没有本稿构造的有界交织，所以不由本稿宣布原 ISP 已解决。

## 12. 内部来源与新增步骤

- R174：实际负整数边界与真实权；
- R188：慢 Cayley 符号及其非真空边界核；
- R200：边界右移定义域与仍未解决的饱和问题；
- R205 及复系数附录：实际最低位分块、有限列 Cayley 系数和低位块对角分解。

本稿新增且已独立写全的是：所有源共享的实际多行选择、每层尾和的绝对收敛、带负回绕因子的余数循环、最高孔位有限多项式的重整、有限 multiaffine 降阶、有限次数输出的全偶分量递归，以及最后使用原输出次数的单层等间隔尾消元。
