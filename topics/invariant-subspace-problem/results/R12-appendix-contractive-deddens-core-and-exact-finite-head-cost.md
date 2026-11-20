# R12 附录：收缩 Deddens 有限头核心与最优有限头成本

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：以下强稠密性、同一输入硬截断及有限头最优成本公式均给完整证明。** 本稿在原 Haar 空间与原权上工作；不把 Deddens 算子当成 $A$ 的交换子，也不推出原普通不变子空间问题已解。一般 $L^2$ 输入的误差保留为真实积分，不预设尾速率。

内部对象为 [R9](R9-radial-odometer-and-nilpotent-approximants.md)、[R12](R12-normalized-powers-and-compact-commutant.md) 的同一个算子。Deddens 路线此前结论见 [完整边界附录](R12-appendix-deddens-algebra-localizing-and-uniform-cost-obstruction.md)。以下仅借用其定义，所需乘积、成本与逼近论证均重写于本文。

## 1. 原对象及两个结论

令 $H=L^2(\mathbb Z_2,\mu)$，$Uf(y)=f(y-1)$，$A=M_wU$，其中

$$
w(y)=\alpha_{v_2(y)}\quad(y\ne0),\qquad w(0)=0,
$$

$$
\alpha_j=e^{-L_j},\qquad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{1.1}
$$

于是 $\alpha_0=e^{-20}>\alpha_1>\cdots>0$，$w$ 是连续非负函数，只有一个零点。置

$$
h_n(x)=\prod_{a=1}^{n}w(x+a),\qquad
\beta_n=\|A^n\|=\|h_n\|_\infty,\qquad h_0=\beta_0=1.
\tag{1.2}
$$

每个 $h_n$ 连续，其零集为有限集合 $\{-1,\ldots,-n\}$。由保测平移，

$$
\|A^\ell f\|^2=\int h_\ell(x)^2|f(x)|^2\,d\mu(x).
\tag{1.3}
$$

定义

$$
\mathcal D_A=
\left\{X\in B(H):\exists C<\infty,
\|A^\ell Xf\|\le C\|A^\ell f\|
\quad(\ell\ge1,\ f\in H)\right\},
$$

$$
c_A(X)=\inf\{C:\text{上述全部不等式成立}\}.
\tag{1.4}
$$

不属于 $\mathcal D_A$ 时记 $c_A(X)=\infty$。

低 $m$ 位分解为

$$
y=r+Nz,\qquad N=2^m,\quad 0\le r<N,
$$

$$
H\simeq\mathbb C^N\otimes L^2(\mathbb Z_2),\qquad
f\longmapsto\big(N^{-1/2}f(r+Nz)\big)_{r=0}^{N-1}.
\tag{1.5}
$$

有限头矩阵的次序始终是 $0,1,\ldots,N-1$。记 $\mathcal T_{\rm fin}^0$ 为所有在某个分解 (1.5) 下形如 $B\otimes I$、且 $B$ 为严格下三角矩阵的算子之并。

**定理 A：收缩强稠密性与实际费用。**

1. $\mathcal T_{\rm fin}^0\subset\mathcal D_A$，而且

   $$
   \overline{\{X\in\mathcal T_{\rm fin}^0:\|X\|\le1\}}^{\rm SOT}
   =
   \overline{\{X\in\mathcal D_A:\|X\|\le1\}}^{\rm SOT}
   =
   \{R\in B(H):\|R\|\le1\}.
   \tag{1.6}
   $$

2. 对任何低 $m$ 位矩阵 $B=(b_{rs})$、整数 $j\ge0$，令
   $D=N2^j$、$K=D+N-1$。对每个满足 $K<2^J$ 的 $J$，本文显式构造同一输入硬截断所得算子 $X_{j,J}\in\mathcal T_{\rm fin}^0$，使

   $$
   \|X_{j,J}\|\le\|B\|,\qquad
   c_A(X_{j,J})\le
   \frac{\alpha_0}{\alpha_{J-1}}\,\||B|\|
   \le\frac{\alpha_0}{\alpha_{J-1}}\sqrt N\,\|B\|,
   \tag{1.7}
   $$

   其中 $|B|=(|b_{rs}|)$ 是逐项绝对值矩阵。先 $J\to\infty$、再 $j\to\infty$ 时，$X_{j,J}$ 强趋 $B\otimes I$。

3. 该逼近对任何 $f\in H$ 满足

   $$
   \|(X_{j,J}-T_j)f\|
   \le\|B\|
   \left(\int_{G_{J,K}^c}|f|^2\,d\mu\right)^{1/2},
   \tag{1.8}
   $$

   其中 $T_j=B\otimes U_{\rm tail}^{2^j}$，
   $\mu(G_{J,K}^c)=K2^{-J}$。只有在 $f\in L^\infty$ 时才进一步得到
   $\|B\|\|f\|_\infty\sqrt{K2^{-J}}$。

**定理 B：有限头最优成本。**

对任意 $N\times N$ 矩阵 $B$，有

$$
B\otimes I\in\mathcal D_A
\quad\Longleftrightarrow\quad B\text{ 为下三角矩阵}.
\tag{1.9}
$$

若 $B$ 下三角，定义连续下三角矩阵函数

$$
C_B(t)_{rs}=
\begin{cases}
b_{rs}\dfrac{\beta_s}{\beta_r}
\displaystyle\prod_{a=s+1}^{r}w(t+a),&r\ge s,\\[6pt]
0,&r<s,
\end{cases}
\tag{1.10}
$$

空积为一。则

$$
\boxed{c_A(B\otimes I)=\max_{t\in\mathbb Z_2}\|C_B(t)\|.}
\tag{1.11}
$$

这个连续最大值又精确等于至多 $2N$ 个显式有限矩阵范数的最大值，见 §7；不必以 (1.7) 的粗上界替代实际成本。

## 2. 范数乘积与同一好集合上的阈值

先证明以后用到的原范数公式：

$$
\beta_n=\prod_{a=1}^n\alpha_{v_2(a)},\qquad
-\log\beta_n
=nL_0+\sum_{r\ge1}(L_r-L_{r-1})
\left\lfloor\frac n{2^r}\right\rfloor.
\tag{2.1}
$$

给定 $x$，连续 $n$ 个数 $x+1,\ldots,x+n$ 中，每个模 $2^r$ 零同余类至少出现 $\lfloor n/2^r\rfloor$ 次。将 $L_{v_2(x+a)}$ 展开成 $L_0$ 与差分之和，得到 $h_n(x)$ 不超过 (2.1) 右边的乘积。在 $0$ 的足够小的 $2$-进邻域内，$x+a$ 与 $a$ 的 $2$-进阶对全部 $1\le a\le n$ 同时相等，所以此上界在正测集合上取到。这证明的是本质上确界，不是仅在单点取到的点值。

给定 $K<2^J$，定义

$$
G_{J,K}=
\{x:x+a\notin 2^J\mathbb Z_2,\quad 1\le a\le K\}.
\tag{2.2}
$$

这些被排除的模 $2^J$ 类互不相同，因而

$$
G_{J,K}
=\{x:0\le x\bmod 2^J\le2^J-K-1\},\qquad
\mu(G_{J,K}^c)=K2^{-J}.
\tag{2.3}
$$

固定 $n\le K$，令

$$
a_r(x,n)=\#\{1\le a\le n:x+a\in2^r\mathbb Z_2\}.
$$

连续区间的同余类计数给

$$
\left\lfloor\frac n{2^r}\right\rfloor
\le a_r(x,n)\le
\left\lfloor\frac n{2^r}\right\rfloor+1.
\tag{2.4}
$$

若 $x\in G_{J,K}$，则全部 $x+a$ 的阶小于 $J$，从而

$$
-\log h_n(x)
=nL_0+\sum_{r=1}^{J-1}
(L_r-L_{r-1})a_r(x,n).
\tag{2.5}
$$

由于 $n<2^J$，(2.1) 中 $r\ge J$ 的项全零。相减并用 (2.4)，得到

$$
0\le\log\frac{\beta_n}{h_n(x)}
\le\sum_{r=1}^{J-1}(L_r-L_{r-1})
=L_{J-1}-L_0.
\tag{2.6}
$$

因此对同一个 $x\in G_{J,K}$ 和全部 $n\le K$，

$$
\boxed{\frac{h_n(x)}{\beta_n}
\ge\frac{\alpha_{J-1}}{\alpha_0}.}
\tag{2.7}
$$

费用阈值的指数是 $L_{J-1}-L_0$，没有额外的区间长度 $K$ 乘子。$K$ 出现在坏集合的测度中。

## 3. 全部正向大平移实现有限头矩阵

固定低 $m$ 位矩阵 $B$ 和 $j\ge0$，令

$$
D=N2^j,\qquad n_{rs}=D+r-s,\qquad K=D+N-1.
\tag{3.1}
$$

全部指数严格为正：

$$
1\le D-(N-1)\le n_{rs}\le K.
$$

定义

$$
T_j=\sum_{r,s=0}^{N-1}
b_{rs}M_{\mathbf1_{\{y\bmod N=r\}}}U^{n_{rs}}.
\tag{3.2}
$$

若输出坐标是 $y=r+Nz$，则

$$
y-n_{rs}=s+N(z-2^j).
$$

所以在 (1.5) 下有精确等式

$$
T_j=B\otimes U_{\rm tail}^{2^j},\qquad
\|T_j\|=\|B\|.
\tag{3.3}
$$

全部矩阵条目使用同一个尾平移，因而保留 $B$ 的真实算子范数。若只给某一三角部分加周期，通常没有这个范数结论。

有限尾柱函数对充分大的 $2^j$ 平移不变，且这些函数稠密。尾平移是酉算子，因此

$$
U_{\rm tail}^{2^j}\to I\quad{\rm SOT},\qquad
T_j\to B\otimes I\quad{\rm SOT}.
\tag{3.4}
$$

## 4. 硬截断、全幂成本与未触及的高尾

对 $2^J>K$ 取

$$
q_{j,J}=\mathbf1_{G_{J,K}},\qquad
k_J=\frac{\alpha_0}{\alpha_{J-1}},\qquad
X_{j,J}=T_jM_{q_{j,J}}.
\tag{4.1}
$$

由 §2，对每个 $n_{rs}$ 都有

$$
0\le q_{j,J}(x)\le1,\qquad
q_{j,J}(x)\le k_J\,h_{n_{rs}}(x)/\beta_{n_{rs}}.
\tag{4.2}
$$

显然 $\|X_{j,J}\|\le\|B\|$。下面核实全部幂的成本，保留完整矩阵，不对 $N^2$ 个条目粗求和。

对任意正整数 $\ell,n$，有限乘积恒等式给

$$
h_\ell(x+n)h_n(x)=h_n(x+\ell)h_\ell(x).
$$

因此在有限零集外，

$$
\frac{h_\ell(x+n)}{h_\ell(x)}
=\frac{h_n(x+\ell)}{h_n(x)}
\le\frac{\beta_n}{h_n(x)}.
\tag{4.3}
$$

此式也对 $\ell<n$ 成立。对全部整数只须去掉可数个零点。

在 (1.5) 中以 $t$ 表示输入尾变量，令
$g_s(t)=h_\ell(s+Nt)f(s+Nt)$；对应输出尾变量是 $t+2^j$。加权后的矩阵条目为

$$
b_{rs}q_{j,J}(s+Nt)
\frac{h_\ell(r+N(t+2^j))}{h_\ell(s+Nt)}.
\tag{4.4}
$$

因为 $r+N(t+2^j)=s+Nt+n_{rs}$，由 (4.2)–(4.3)，其绝对值至多 $k_J|b_{rs}|$。逐点矩阵绝对值支配及 $\ell^2$ 范数的单调性给该矩阵范数至多 $k_J\||B|\|$。对尾变量积分，

$$
\|A^\ell X_{j,J}f\|
\le k_J\||B|\|\,\|A^\ell f\|
\qquad(\ell\ge1).
\tag{4.5}
$$

故 $X_{j,J}\in\mathcal D_A$，并且

$$
c_A(X_{j,J})\le k_J\||B|\|
\le k_J\||B|\|_{\rm HS}
=k_J\|B\|_{\rm HS}
\le k_J\sqrt N\|B\|.
\tag{4.6}
$$

这支付了原 $B$ 的相位、全部输入分量和同一个输入 cut。

硬截断还给一个准确结构。若输入的低 $J$ 位数字为 $a\in[0,2^J-K-1]$，则每个 $1\le n_{rs}\le K$ 都满足

$$
a<a+n_{rs}<2^J.
\tag{4.7}
$$

因此平移没有越过低 $J$ 位的边界，所有高尾位保持不动。输入与输出数字严格递增，且所有系数仅依赖低 $J$ 位。于是 $X_{j,J}$ 精确是一个低 $J$ 位严格下三角矩阵张量尾恒等，即属于 $\mathcal T_{\rm fin}^0$。

固定 $j,K$ 时，$G_{J,K}$ 随 $J$ 增大而增大，其补集的交集为有限集合 $\{-1,\ldots,-K\}$。故 $M_{q_{j,J}}\to I$ SOT，从而 $X_{j,J}\to T_j$ SOT。并且直接有

$$
\|(X_{j,J}-T_j)f\|
\le\|B\|\,\|(q_{j,J}-1)f\|
=\|B\|\,\|\mathbf1_{G_{J,K}^c}f\|.
\tag{4.8}
$$

对一般 $L^2$ 向量，该项由积分绝对连续性趋零，不能只用 $\|f\|_2$ 和坏集合测度写出统一速率。若 $f\in L^\infty$，则 (2.3) 才给
$\|B\|\|f\|_\infty\sqrt{K2^{-J}}$。

**可选软截断。** 若需任意实预算参数 $k$，也可取

$$
q_{j,k}(x)=\min\left(1,\,
k\min_{n\in\{n_{rs}\}}\frac{h_n(x)}{\beta_n}\right).
\tag{4.9}
$$

同样的逐点矩阵论证给
$\|T_jM_{q_{j,k}}\|\le\|B\|$、
$c_A(T_jM_{q_{j,k}})\le k\||B|\|$，
而 $k\to\infty$ 时强趋 $T_j$。硬截断的额外优点是它精确保留未触及高尾，并落在有限头严格下三角核心内。

## 5. 从有限头到整个收缩单位球

设 $R\in B(H)$ 且 $\|R\|\le1$。令 $H_m$ 为低 $m$ 位柱函数空间，$P_m$ 是其正交投影；将压缩 $P_mR|_{H_m}$ 看成 $N\times N$ 矩阵 $B_m$，定义

$$
R_m=B_m\otimes I.
\tag{5.1}
$$

有 $\|R_m\|\le1$。若 $f\in H_p$ 且 $m\ge p$，其尾因子是常函数 $1$，所以

$$
R_mf=P_mRf\longrightarrow Rf.
\tag{5.2}
$$

柱函数稠密且范数一致有界，因而 $R_m\to R$ SOT。对每个 $m$，§3–4 先用 $j$ 再用 $J$ 将 $R_m$ 逼近为 $\mathcal T_{\rm fin}^0$ 中的收缩算子。

取一列可数稠密柱函数，并对第 $m$ 步选 $j_m,J_m$，使当前算子在前 $m$ 个柱函数上的误差小于 $1/m$。所得真正的有限头严格下三角收缩列强趋 $R$。强极限的范数下半连续性给反向包含。这证明 (1.6)；其中 $\mathcal T_{\rm fin}^0\subset\mathcal D_A$ 亦由下一节完整有限头分类再次确认。

特别，对任意收缩 $R$、有限输入族 $f_1,\ldots,f_t$ 和 $\varepsilon>0$，存在同一个 $X\in\mathcal T_{\rm fin}^0$ 使

$$
\|X\|\le1,\qquad
\max_{a\le t}\|Xf_a-Rf_a\|<\varepsilon.
\tag{5.3}
$$

经过有限头目标逼近后，该输入族可共享同一组 $j,J$，其真实成本由 §4 或下面的最优公式计算。

## 6. 全部有限头成员及最优成本的连续公式

固定 $N=2^m$ 和 $B$，考虑 $B^{\rm loc}=B\otimes I$。给定 $\ell\ge1$，在 (1.5) 的尾变量 $z$ 上置

$$
D_\ell(z)=\operatorname{diag}
\big(h_\ell(r+Nz)\big)_{r=0}^{N-1}.
\tag{6.1}
$$

各对角条目几乎处处严格正。由 (1.3)，满足
$\|A^\ell B^{\rm loc}f\|\le C\|A^\ell f\|$ 的最小常数恰是

$$
\operatorname*{ess\,sup}_{z\in\mathbb Z_2}
\|D_\ell(z)BD_\ell(z)^{-1}\|.
\tag{6.2}
$$

两向均为有限维矩阵乘法算子的范数公式。若需直接核验必要性，可在出现违背的正测集合上，从可数稠密单位向量中选一个常向量测试，再截去权过小的集合；不需要选择可测最大特征向量。$h_\ell$ 有界且正几乎处处，故这些截断测试都在原 $L^2$ 中。

将 (6.2) 对全部 $\ell\ge1$ 取上确界，恰得 $c_A(B^{\rm loc})$。令 $t=Nz+\ell$。因为对于 $0\le s\le r<N$，

$$
\prod_{a=s+1}^{r}w(Nz+a)
=\prod_{a=s+1}^{r}\alpha_{v_2(a)}
=\beta_r/\beta_s,
\tag{6.3}
$$

乘积相消给

$$
\frac{h_\ell(r+Nz)}{h_\ell(s+Nz)}
=
\frac{\beta_s}{\beta_r}
\prod_{a=s+1}^{r}w(t+a)
\qquad(r\ge s).
\tag{6.4}
$$

若 $r<s$，则相应式子是

$$
\frac{h_\ell(r+Nz)}{h_\ell(s+Nz)}
=
\frac{\beta_s/\beta_r}
{\displaystyle\prod_{a=r+1}^{s}w(t+a)}.
\tag{6.5}
$$

先假设 $B$ 下三角。(6.4) 表明 (6.2) 中的矩阵就是 $C_B(t)$。当 $\ell=1,\ldots,N$ 时，$t=Nz+\ell$ 已经覆盖全部模 $N$ 类，而 Haar 测度在各类上的条件分布是缩放后的 Haar 测度。因此

$$
c_A(B^{\rm loc})
=\operatorname*{ess\,sup}_{t\in\mathbb Z_2}\|C_B(t)\|.
\tag{6.6}
$$

$C_B$ 连续且 Haar 测度满支撑，所以本质上确界等于最大值，得到 (1.11)，并证明全部下三角局部矩阵属于 $\mathcal D_A$。

反之，若存在 $r<s$ 且 $b_{rs}\ne0$，选择
$a_0\in\{r+1,\ldots,s\}$。当 $t\to-a_0$ 时，(6.5) 的分母含
$w(t+a_0)\to0$；其余有限个不同整数位移的权在该点非零。所以对应条目的绝对值在每个充分小的正测 $2$-进邻域内无界。

取 $\ell\in\{1,\ldots,N\}$ 与 $-a_0$ 同模 $N$，上述发散已发生在这个固定 $\ell$ 所对应的尾变量中。矩阵算子范数至少是该条目的绝对值，任何其他条目都不能抵消它，故 (6.2) 无穷。这证明 (1.9)。

## 7. 最优成本只需至多两个端点乘以 $N$ 个模类

对下三角 $B$，固定一个模 $N$ 类 $t\equiv a\pmod N$。在
$q=1,\ldots,N-1$ 中，至多有一个 $q_0$ 满足

$$
a+q_0\equiv0\pmod N.
\tag{7.1}
$$

其他 $q$ 上有

$$
w(t+q)=\alpha_{v_2(a+q)},
\tag{7.2}
$$

且该阶小于 $m$，完全不依赖尾变量。

若不存在 $q_0$，则 $C_B(t)$ 在该类上固定。若存在，唯一可变的权为

$$
v=w(t+q_0)\in
\{\alpha_m,\alpha_{m+1},\ldots\}\cup\{0\}.
\tag{7.3}
$$

每个正值都在该模类的一个正测子集上取得，零值是这些值的极限。由于 (1.10) 的每个连续区间乘积最多含这个特殊位置一次，存在两个明确矩阵 $C_{a,0},C_{a,1}$，使

$$
C_B(t)=C_{a,0}+vC_{a,1}.
\tag{7.4}
$$

矩阵范数对实数 $v$ 凸，而 $0\le v\le\alpha_m$。两端都由实际值或其极限达到，故

$$
\sup_{v\in\{\alpha_m,\alpha_{m+1},\ldots,0\}}
\|C_{a,0}+vC_{a,1}\|
=
\max\big(
\|C_{a,0}\|,
\|C_{a,0}+\alpha_m C_{a,1}\|
\big).
\tag{7.5}
$$

这也保留本质上确界：即便 $v=0$ 只在单点取得，正测的
$v=\alpha_{m+k}\to0$ 足以逼近相同矩阵范数。

于是，对每个模 $N$ 类把特殊权分别替换成 $0$ 与 $\alpha_m$，其余权使用 (7.2)，代入 (1.10)；这些至多 $2N$ 个矩阵范数的最大值，**精确等于** $c_A(B^{\rm loc})$。没有特殊位置的模类只需计算一次。

当 $m=0$ 时只有标量矩阵，上述公式退化成
$c_A(B^{\rm loc})=|b_{00}|$。一般 $m$ 时，模类 $a=0$ 没有特殊位置并给 $C_B(0)=B$，故该公式还直接显示
$c_A(B^{\rm loc})\ge\|B\|$。

## 8. 实际可优化接口与尚未支付的普通桥

对于固定的低 $m$ 位插值问题，

$$
\|B\|\le1,\qquad c_A(B\otimes I)\le C
\tag{8.1}
$$

完全等价于：$B$ 下三角、$\|B\|\le1$，以及 §7 中至多 $2N$ 个实际端点矩阵范数均不超过 $C$。各端点矩阵都是 $B$ 的线性函数，所以这些是有限凸约束。若还指定有限向量上的线性插值约束，便得到一个真实有限维费用问题。将 §4 的硬 cut 矩阵代入，则得到该具体构造的最优 Deddens 成本，不再只能使用 (1.7) 的充分上界。

所有参数、权、低位矩阵与未触及高尾都属于原 Haar 模型。该工具没有把输入换成另一个便宜模型，也没有把坏集合上的真实质量删除。

不过，未知 $A$-不变子空间未必被这些 $B\otimes I$ 保持。此前完整 Deddens 附录已证明：任何统一 $c_A$ 预算族都不能 localize。故强稠密性不能把 $J$ 或 $k_J$ 固定，也不能直接代入需要统一 Deddens 常数的 Lomonosov/Lacruz 递推。要推进普通问题，仍须把同一递推输入的真实费用与 $A$ 幂衰减或原返回预算闭合。本文提供的是可计算、收缩且保持有限头来源的正向工具，而不是对该剩余桥的证明。
