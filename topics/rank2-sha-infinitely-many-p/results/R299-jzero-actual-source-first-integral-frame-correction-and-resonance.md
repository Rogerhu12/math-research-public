# R299 — 新原来源的完整首积分校正、两个真实 frame 与共振系数 $18/17$

日期：2026-11-13。**状态：以下对 R297 实际来源的角校正、原点归一、真实有限窗口、完整 Frobenius 项、全局有限模型的 exact 微分和首次共振系数均已证明。它们没有把裸 Cartier 非零替代原完整中央行，也没有把 $S/q^2$ 与 $S/z^6$ 混同。**

本篇修正一个可能混淆：R288 的 Dixon 系数 $h_{2r-1}$ 的 $2p$ 分母被分子中的 $p$ 抵消；它是单位，并没有在此出现首分母。$2r-1$ 是下面余项算子的共振位置。原 $h^{-6}$ 的来源成本仍须保留。

## 1. 实际原源和两个单位块

始终取 $b=17$。R297 首项一的真实来源是
$$
S=\frac{q^2v^2}{112b}\theta_-^{34}Q_8(q),\qquad v^3=1-q,
$$
$$
Q_8=(q-2)^2(1+q)(1-2q)(q^4+q^3+6q^2-14q+7),\qquad Q_8(0)=28.
\tag{1}
$$
R288 的原不变微分给
$$
q=u^3,\qquad az=u h(q),\qquad
h_n=[q^n]h=\frac{(2/3)_n}{n!(3n+1)},\qquad a^6=4b.
$$
因此两个真实单位块准确为
$$
\boxed{
F_q=\frac{4bS}{q^2}=\theta_-^{34}v^2\frac{Q_8}{28},\qquad
F_z=\frac S{z^6}=F_qh^{-6}.
}
\tag{2}
$$
两者原点值都是一。$S=q^2F_q/(4b)$ 和 $S=z^6F_z$ 是原来源的完整乘子关系；本篇不把任何一条新的单位块观察认作原中央零。

写
$$
Z=\log\theta_-^{34},\qquad
L_q=\frac23\log(1-q)+\log\frac{Q_8}{28},\qquad L_z=L_q-6\log h.
\tag{3}
$$
所以 $\log F_\epsilon=Z+L_\epsilon$，$\epsilon=q,z$。固定有理角对数的准确导数为
$$
\boxed{L_q'=-\frac2{3(1-q)}+\frac{Q_8'}{Q_8}.}
\tag{4}
$$
以下取惰性好素数
$$
p\equiv2\pmod3,\qquad p\ge5,\quad p\ne17,\qquad p=3r-1.
\tag{5}
$$
$r$ 为偶数。所有级数先在特征零定义，只对已说明整的截断取模 $p$。

## 2. $h$ 的真实整窗口及不能漏掉的共振单位

**引理 1。** $h_n$ 对 $0\le n\le p$ 全部 $p$ 整；$h_{2r-1}$ 是单位。更准确地，在 $n<p$ 时
$$
v_p(h_n)=
\begin{cases}
0,&0\le n<r\text{ 或 }n=2r-1,\\
1,&r\le n<p,\ n\ne2r-1.
\end{cases}
\tag{6}
$$
且 $v_p(h_p)=0$。

**证明。** 分子 $\prod_{j=0}^{n-1}(3j+2)$ 在 $n\ge r$ 时恰含一个 $p$，来自 $j=r-1$。在 $0\le n\le p$ 的范围没有第二个这样的因子。分母 $n!$ 只在 $n=p$ 时含一个 $p$；因子 $3n+1$ 只在 $n=2r-1$ 时为 $2p$。这两个分母事件不同时发生，所以得到 (6) 及 $n=p$ 的断言。$\square$

令 $h_+=\sum_{n<r}h_nq^n$，并置
$$
c_p=\overline{h_{2r-1}}\ne0,\qquad
\boxed{H_p=h_++c_pq^{2r-1}\in\mathbf F_p[q].}
\tag{7}
$$
这是原 $h\bmod(p,q^p)$ 的准确多项式，不是任意补上的齐次解。其次数恰为 $2r-1$，常数为一，并且
$$
H_p+3qH_p'=(1-q)^{r-1}.
\tag{8}
$$
最高项的特征值 $1+3(2r-1)=2p$ 为零，因此它不由低阶微分递推单独决定；(7) 保留了原特征零系数的准确约化。

由 (6)，$L_q,L_z$ 的 $q^n$ 系数在 $n<p$ 时均整。$\log h$ 在这个范围也整，因为定义 logarithm 所用的整数分母都小于 $p$。这正是下一节可进行原归一的依据。

## 3. 实际坏带常数和原点归一

沿用 R288/R291 的真正 theta 常数与余项
$$
a_0=p[q^r]Z\in\mathbf Z_p^\times,
$$
$$
U_\theta=q^{-r}\left(Z-[Z]_{<r}-\frac{a_0}{p}q^rh_+\right),\qquad A=a_0h_+.
\tag{9}
$$
$U_\theta(0)=0$，且模 $q^{2r-1}$ 全部整。对 $\epsilon=q,z$，写
$\ell_{\epsilon,r}=[q^r]L_\epsilon$。实际单位块的首坏系数是
$$
\boxed{a_\epsilon=p[q^r]\log F_\epsilon=a_0+p\ell_{\epsilon,r}.}
\tag{10}
$$
它仍是单位，但其下一位并不与 $a_0$ 相同。

以这个真实常数归一原余项：
$$
U_\epsilon=q^{-r}\left(\log F_\epsilon-[\log F_\epsilon]_{<r}
-\frac{a_\epsilon}{p}q^rh_+\right).
$$
于是准确有
$$
\boxed{
U_\epsilon=U_\theta+
q^{-r}(L_\epsilon-[L_\epsilon]_{<r})
-\ell_{\epsilon,r}h_+.
}
\tag{11}
$$
特别 $U_\epsilon(0)=0$。最后一项不能省略；省去它便改变原点常数和下面的 Frobenius 质量项。$U_q,U_z$ 都在模 $q^{2r-1}$ 的同一窗口整。

## 4. 真来源的完整首积分

在剩余域中，定义两个明确的有理函数
$$
\mathscr R_q=-\frac2{3(1-q)}+\frac{Q_8'}{Q_8},\qquad
\mathscr R_z=\mathscr R_q-6\frac{H_p'}{H_p},
\tag{12}
$$
$$
\boxed{
R_\epsilon=3v^2q^{1-r}
\left(\mathscr R_\epsilon-\partial_q[L_\epsilon]_{<r}\right).
}
\tag{13}
$$
所有 Taylor 系数在约化前取自 (3)。对于 $\epsilon=z$，(7) 保证 (12) 与原 $L_z'$ 在所需窗口相同；没有把整个 $h$ 认作全局有理函数。

(13) 在原点正则，且
$$
R_\epsilon(0)=3r\,\ell_{\epsilon,r}=\ell_{\epsilon,r}\quad(\bmod p).
\tag{14}
$$
因此 $R_\epsilon-\ell_{\epsilon,r}v^p$ 在原点为零。

使用 R291 的有限多项式
$$
B_p(V)=\sum_{j=0}^{r-2}
\frac{(-1)^j\binom{r-1}{j}-1}{3j+2}V^{3j+2},\qquad B_p(1)=0,
$$
得到下述准确首积分。

**定理 2。** 对两个实际 frame，均有
$$
\boxed{
\begin{aligned}
v^2\bigl(U_\epsilon+3qU_\epsilon'+A\bigr)
={}&a_0\bigl(B_p(v)+v^p(1-2\log v)\bigr)\\
&+R_\epsilon-\ell_{\epsilon,r}v^p
\pmod{q^{2r-1}}.
\end{aligned}}
\tag{15}
$$
这里 $\log v=\frac13\log(1-q)$ 只使用次数小于 $p$ 的已整截断；全式中的 $v^p$ 明确保留。

**证明。** 对任意角项 $L$，特征零共轭准确为
$$
(1+3q\partial_q)q^{-r}(L-L_{<r})
=q^{-r}\bigl((1-3r)(L-L_{<r})+3q(L'-L_{<r}')\bigr).
$$
因为 $1-3r=-p$，在已整窗口约化后，第一项恰消失，第二项乘 $v^2$ 正是 (13)。对 (11) 的最后一项，用
$$
v^2(h_++3qh_+')=v^2(1-q)^{r-1}=v^p
$$
得到 $-\ell_{\epsilon,r}v^p$。

再加 R291 的原首积分即可。R291 的 $1-2\log v$ 可以在此窗口写成 $v^p(1-2\log v)$，因为 $v^p=1+O(q^p)$，而 $2r-1<p$。这一步只在显示窗口中使用，没有把 $v^p$ 从全局微分中删除。原点由 (14)、$B_p(1)=0$ 和 $U_\epsilon(0)=0$ 同时核定。$\square$

## 5. 全局 exact 校正的准确含义

R291 的实际多项式微分为
$$
\beta_p=\frac{1-u^{p+1}-v^{p+1}}{uv}\,du
=dB_p(v)-2v^{p-1}dv.
$$
对 (13) 的明确有理函数，在整个三次曲线的函数域中定义
$$
\boxed{\beta_{\epsilon,p}=\beta_p+a_0^{-1}dR_\epsilon.}
\tag{16}
$$
这是一个完整的全局有理微分恒等式。由 Cartier 杀掉 exact 微分，
$$
\boxed{C\beta_{\epsilon,p}=-2\,dv\ne0,\qquad
C^2\beta_{\epsilon,p}=0.}
\tag{17}
$$
同时，在形式原点取 (15) 右端的导数，在该式所给的模 $q^{2r-2}$ 窗口内正得 $a_0\beta_{\epsilon,p}$；
$v^p$ 和 $\ell_{\epsilon,r}v^p$ 的微分为零，但它们的原点值和 deck 特征并不因此可以删除。

这项全局结论的范围必须分清。$R_q$ 使用原固定 $Q_8$ 的真实对数导数；$R_z$ 使用原 $h$ 的准确有限多项式 (7)，其次数随 $p$ 为 $2r-1$。所以 (16)、(17) 对这两个明确定义的全局有限模型成立，而它们与实际余项 $U_\epsilon$ 的比较仅在 (15) 的窗口内成立。特别不能把 $H_p$ 宣称为整条椭圆对数，不能删除它的零点分母，也不能据 (17) 把原完整中央行置成非零。

角色同样保留：$R_\epsilon$ 是 $v^2$ 乘 base 上的有理函数，其 deck 特征与 $\beta_p$ 一致；Cartier 的半线性把这一特征送到 $dv$ 的特征。反之，单独把 $v^p$ 改成常数并推广出窗口，会破坏这一实际角色。

## 6. 第一次共振处的原系数准确为 $18$ 和 $17$

先给一个整系数单位级数的一般事实：若 $G(0)=1$、$[q^j]G$ 对 $j\le p$ 全部 $p$ 整，则
$$
\boxed{p[q^p]\log G\equiv([q]G)^p\pmod p.}
\tag{18}
$$
证明展开 $\log(1+H)=\sum_{k=1}^{p}(-1)^{k-1}H^k/k\bmod q^{p+1}$；乘 $p$ 后，$k<p$ 的项全消，$k=p$ 项只留下 $H_1^p$。

R288 的准确 theta 系数给
$$
p[q^p]Z=\frac{34}{3}\frac{(1/3)_p}{(2/3)_p}
\equiv\frac{68}{3}\pmod p.
\tag{19}
$$
其理由是：两组乘积的非零剩余类各遍历 $\mathbf F_p^\times$，唯一被 $p$ 整除的因子分别是 $2p$ 和 $p$，所以比值为二。没有使用近似 gamma 公式。

由 $Q_8(0)=28,Q_8'(0)=-112$ 和 (18)，
$$
p[q^p]L_q\equiv-\frac23-4=-\frac{14}3.
$$
因此
$$
\boxed{p[q^p]\log F_q\equiv18\pmod p.}
\tag{20}
$$

引理 1 还保证 $h_p$ 整，故可对原 $h$ 使用 (18)。因
$h_1=(2/3)/4=1/6$，有
$$
p[q^p]\log h\equiv\frac16\pmod p.
$$
结合 (2)，准确得到
$$
\boxed{p[q^p]\log F_z\equiv18-6\cdot\frac16=17\pmod p.}
\tag{21}
$$
在 (5) 的好素数中，这两个值均为单位。

原 $U_\epsilon$ 的对应次数是 $n=2r-1$，因为 $r+n=p$。低截断和 $h_+$ 都不在此次数贡献项，所以
$$
p[q^{2r-1}]U_q\equiv18,\qquad
p[q^{2r-1}]U_z\equiv17\pmod p.
\tag{22}
$$
同时 $1+3(2r-1)=2p$ 正是 (15) 所用一阶算子的首次共振。故本篇窗口对实际两个来源都准确地止于该项之前；不能声称余项已经跨过 $q^p$ 而保持整。

这些单位位于原对数余项的指定角坐标。原完整中央函数还含 (2) 的原 $q^2$ 或 $z^6$ 乘子、相应参考、Euler 因子及全权聚合。本文没有将 (20)–(22) 当作原中央行的独立观察。

## 7. 证书

- [check-jzero-actual-angular-carry-and-frame-correction.py](../scripts/check-jzero-actual-angular-carry-and-frame-correction.py)
- [check-jzero-actual-angular-carry-and-frame-correction.json](../scripts/check-jzero-actual-angular-carry-and-frame-correction.json)

证书逐项核原第一阶共轭、(10)、(11) 的质量修正、$v^p$ 指数、原 $Q_8$ 的有理对数导数、$h$ 的两次分母抵消、真实两个 frame 的转换及 $18/17$ 常数。整性、Cartier 和全部素数的断言由上面的统一证明给出，没有进行目标素数扫描。

