# R832：原规范高度外积的显式统一接触阶界

日期：2026-11-15。状态：**下述接触阶界和有限 jet 截断准则已证明。** 沿用 R616/R634 的同一本原非消失前提、原 $c_1$、原商和全部高度规范。本文没有计算任何新的高度值、周期或有限域数据。

本篇新增的是一个只依原曲线亏格的明确公式。R699/R703/R716 已证明原外积非恒零、可用代数微分算子找出有限首阶集合，以及完整相对尾界；这里不重复登记这些结论。新的界使有限 jet 窗口可以在求出该微分算子、实际高度常数或其首非零阶之前确定。它随 $p$ 增长，不是一个与 $p$ 无关的接触阶常数，也不直接排除原整盘的其他共同零点。

## 1. 同一个原外积与结论

设 $p\ge41$、$p\equiv5\pmod6$，并保留 R616 的实际本原乘积
$$
L'(g_{-1,+},1)L(g_{-1,-},1)\ne0.
\tag{832.1}
$$
令 $X=X_1$、$G=g(X)$、$z=a-1$，并使用 R634/R699 的
$$
\Lambda_h=\lambda^F_{p,h}-2\ell_h(P),\qquad
\beta=q[c_1-c_0],\qquad
t_a=1+\frac{I_a}{L_a},\qquad
I_a=\int_{c_1}^{(\cdot)}\varpi_a,\quad L_a\ne0.
\tag{832.2}
$$
$P$、原 $\eta_h$、Picard 零次项、$\kappa=qq^\dagger$、固定截面和刚性化均不变。原候选的坏处靶值仍是 R696 的 $\omega=\omega_0=0$。对 $1\le i<j\le g-1$，写
$$
d_\nu=\Lambda_\nu(c_1),\qquad
V_\nu=t_\nu^2-t_g^2,\qquad
W_\nu=d_\nu t_\nu^2-\Lambda_\nu,\qquad
E_{ij}=W_iV_j-W_jV_i.
\tag{832.3}
$$
R634 已证明这里的每个 $E_{ij}$ 非恒零；本篇将这个结论作为已证输入。R682 给共同 Abel 首阶 $m\ge1$ 及
$\operatorname{ord}_{c_1}E_{ij}\ge m+1$。

定义
$$
R(G)=21G+4,\qquad
\mathcal B(G)=R(G)-1+\binom{R(G)}2(6G-4).
\tag{832.4}
$$

**定理 832.1。** 在上述同一前提下，
$$
\boxed{\quad
m+1\le\operatorname{ord}_{c_1}E_{ij}\le\mathcal B(G).
\quad}
\tag{832.5}
$$
原六层的亏格为
$$
G=\frac{(p-1)^2}{4},
\tag{832.6}
$$
因此 (832.4)–(832.6) 给随 $p$ 明确、次数为六的接触阶上界。这个界不含任何未算出的规范高度常数、第二类周期、$L_a$ 的赋值或微分系统的具体矩阵条目。

更一般地，下文构造的同一个有限代数函数族的任意非零常数组合，哪怕常数在 $\mathbb C_p$ 中而非代数数，也满足同一上界。正是这个较强形式给第 7 节的完整有限关系矩阵。

## 2. 同一曲率的第二类代表可以统一限制到极阶 $2G$

只使用 R699.1 已证明的精确不变性：保持 $Y$ 的 splitting 和其他规范不变，为计算选一个代数的 $F$ 相容对称 splitting，原 $E_{ij}$ 完全不变。这一步不是以任意同曲率高度替换真实外积。原未知高度和周期仍将作为真实常数留在输出中。

在一个有限数域 $K$ 上，两个实际代数曲率写成
$$
\alpha_\nu=\sum_b\omega_{\nu b}\otimes[\eta_{\nu b}],
\qquad \nu=i,j,\qquad
\omega_{\nu b}\in H^0(X_K,\Omega^1),\qquad
\cup\alpha_\nu=0.
\tag{832.7}
$$
扩张 $K$ 后，选 $K$-点 $Q\ne c_1$。若还要使用 R716 的整盘尾界，可同时按 R699 §3 选择其闭包避开该盘；本篇的特征零接触阶证明只需要 $Q\ne c_1$。

**引理 832.2。** 每个 $H^1_{\rm dR}(X_K)$ 类都有只在 $Q$ 有极点、极阶至多 $2G$ 的第二类代表。

**证明。** 令 $U=X_K\setminus\{Q\}$。删去一个 $K$-点的留数正合列给
$$
H^1_{\rm dR}(X_K)\simeq H^1_{\rm dR}(U).
\tag{832.8}
$$
其原因是唯一新增的留数项 $K$ 到 $H^2_{\rm dR}(X_K)\simeq K$ 的次数映射为一；也可直接用局部 Laurent de Rham 复形得到这一正合列。仿射性使右侧由正则微分模正则函数的微分计算。

Riemann–Roch 给
$$
h^0\bigl(\Omega^1(2GQ)\bigr)=3G-1,\qquad
h^0\bigl(\mathcal O((2G-1)Q)\bigr)=G.
\tag{832.9}
$$
一个只有 $Q$ 处极点的微分自动留数为零。若
$\rho\in H^0(\Omega^1(2GQ))$ 在 $H^1_{\rm dR}(U)$ 中为零，则
$\rho=df$，其中 $f\in H^0(U,\mathcal O_U)$。特征零中，一个有 $n>0$ 阶极点的函数，其微分有恰 $n+1$ 阶极点。因此此处 $f$ 只能有至多 $2G-1$ 阶的 $Q$ 极点。核恰为
$$
dH^0\bigl(\mathcal O((2G-1)Q)\bigr),
$$
其维数为 $G-1$。故商空间维数为
$(3G-1)-(G-1)=2G=\dim H^1_{\rm dR}(X_K)$，且已经单射到 (832.8)，所以是同构。$\square$

把 (832.7) 的所有 $\eta_{\nu b}$ 选为此类代表。取
$$
\mathcal A=H^0(X_K,\Omega^1(2GQ)),\qquad
n=\dim_K\mathcal A=3G-1,
\tag{832.10}
$$
并取基 $\rho_1,\ldots,\rho_n$，使
$$
\rho_1=\varpi_i,\qquad \rho_2=\varpi_j,\qquad
\rho_3=\varpi_g.
\tag{832.11}
$$
这三个微分的独立性是原特征分解的一部分；当前有外积指标 $i,j$ 的情形自动满足 $G\ge3$。可先令 $\rho_1,\ldots,\rho_{n-1}$ 构成 $H^0(\Omega^1((2G-1)Q))$ 的基，再补 $\rho_n$。所有 $\omega_{\nu b}$ 和 $\eta_{\nu b}$ 均为这组基的常数线性组合。

令
$$
y_a=\int_{c_1}^{(\cdot)}\rho_a,\qquad
x_1=y_1,\quad x_2=y_2,\quad x_3=y_3,
\tag{832.12}
$$
以及
$$
U_\nu=\int_{c_1}^{(\cdot)}
 \sum_b\omega_{\nu b}\int_{c_1}^{(\cdot)}\eta_{\nu b},
\qquad U_\nu(c_1)=0.
\tag{832.13}
$$
R716.1 的极部证明在这里取 $M=2G$：内积分极阶至多 $2G-1$，乘全纯 $\omega_{\nu b}$ 后所需修正落在
$H^0(\Omega^1((2G-1)Q))\subset\mathcal A$；留数障碍由 $\cup\alpha_\nu=0$ 消失。与真实规范函数同曲率后的全纯差也在 $\mathcal A$ 中。因此有精确等式
$$
\boxed{\quad
\Lambda_\nu=d_\nu+U_\nu+C_\nu(y_1,\ldots,y_n),
\quad}
\tag{832.14}
$$
其中 $C_\nu$ 是真实的常数线性式。其系数可以是非代数的 $p$ 进数。

(832.14) 完整保留第二类全局周期、原规范全纯差和 $-2\ell_\nu(P)$，没有把其中任何一个系数设为零。选择新代表只改变这个表达的代数函数与常数，不改变 (832.3) 的真实函数。

## 3. 秩至多 $21G+4$ 的显式闭合微分系统

定义
$$
A_1=\frac{2x_1}{L_i}+\frac{x_1^2}{L_i^2},\qquad
A_2=\frac{2x_2}{L_j}+\frac{x_2^2}{L_j^2},\qquad
A_3=\frac{2x_3}{L_g}+\frac{x_3^2}{L_g^2}.
\tag{832.15}
$$
由 (832.3)、(832.14) 得到原式
$$
E_{ij}
=(d_iA_1-U_i-C_i)(A_2-A_3)
 -(d_jA_2-U_j-C_j)(A_1-A_3).
\tag{832.16}
$$

取以下有序标记函数列 $\mathscr F$。这里“标记”允许函数之间有关系，不假定列线性独立。

| 部分 | 函数 | 个数 |
|---|---|---:|
| 纯一次积分部分 | $1$；$x_b$；$x_ax_b$（$a\le b$）；$x_ax_b^2$（任意 $a,b$）；$x_a^2x_b^2$（$a<b$），其中 $1\le a,b\le3$ | $1+3+6+9+3=22$ |
| 其余一次积分部分 | 对每个 $4\le a\le n$，$y_a,\ y_ax_b,\ y_ax_b^2$，$1\le b\le3$ | $7(n-3)$ |
| 第一二重积分部分 | $U_i,\ U_ix_2,\ U_ix_3,\ U_ix_2^2,\ U_ix_3^2$ | $5$ |
| 第二二重积分部分 | $U_j,\ U_jx_1,\ U_jx_3,\ U_jx_1^2,\ U_jx_3^2$ | $5$ |

总数为
$$
R=22+7(n-3)+10=7n+11=21G+4.
\tag{832.17}
$$
(832.16) 是 $\mathscr F$ 的常数线性组合，全部真实未知常数只进入该输出行。

**引理 832.3。** 存在 $R\times R$ 的代数微分矩阵 $\Omega$，每个条目属于 $\mathcal A$，使
$$
d\mathscr F=\Omega\,\mathscr F.
\tag{832.18}
$$
所以系统在 $c_1$ 正则，而每个矩阵条目只有至多 $2G$ 阶的 $Q$ 极点。

**证明。** 对纯积分的乘积用 Leibniz 规则。$d(x_a^2x_b^2)$ 只出现 $x_ax_b^2$ 和 $x_a^2x_b$；$d(x_ax_b^2)$ 只出现二次单项式；其余依次降阶，故始终在纯部分。

对 $a\ge4$，
$$
d(y_ax_b^k)=\rho_a x_b^k+k\rho_b y_ax_b^{k-1},
\qquad k=0,1,2,
\tag{832.19}
$$
其中 $k=0$ 时第二项为空。第一项使用纯部分，第二项使用同一 $a$ 的已有列。

把内微分在 $\rho_a$ 中展开，有
$$
dU_\nu=\sum_a\omega_{\nu a}^{\,\prime}y_a,\qquad
\omega_{\nu a}^{\,\prime}\in H^0(X_K,\Omega^1).
\tag{832.20}
$$
因此 $d(U_\nu x_b^k)$ 的两类项是
$\omega_{\nu a}^{\,\prime}y_ax_b^k$ 和
$k\rho_b U_\nu x_b^{k-1}$。当 $a\le3$ 时，前者的函数因子属于纯部分；当 $a\ge4$ 时属于第二部分。后者属于相应的五列块。所有系数微分均为 $\rho_a$ 或全纯微分的代数组合，故属于 $\mathcal A$。这逐类证明了 (832.18)，也说明无需把所有长度四的词全部列入系统。$\square$

## 4. 一般接触阶引理：循环行与有理极部

以下引理不需要几何来源的非恒零定理，适用于任意满足所列条件的非零输出。

设 $k$ 是特征零常数字段，$X/k$ 光滑射影、几何连通、亏格 $G\ge1$，$P,Q\in X(k)$、$P\ne Q$。允许先扩充常数字段。设一个 $R$ 维形式解列 $F$ 在 $P$ 满足
$$
dF=\Omega F,
\tag{832.21}
$$
其中 $\Omega$ 是代数微分矩阵，每个条目只在 $Q$ 有极点，极阶至多 $M\ge1$。令 $\ell_0\in k^{1\times R}$ 为常数行，$f=\ell_0F$。

取全纯微分 $\nu$ 满足 $\nu(P)\ne0$。其存在性来自 canonical 线丛无基点：$G=1$ 时非零全纯微分处处不零；$G\ge2$ 时由 Riemann–Roch，
$h^0(K_X-P)=G-1$。后式可由 $h^0(P)=1$ 得到，而正亏格曲线上若有仅在 $P$ 的简单极点函数就会给次数一的有理参数，矛盾。

记
$$
K_\nu=(\nu)_0,\qquad
D=M Q+K_\nu+(K_\nu)_{\rm red},\qquad
d=\deg D\le M+4G-4.
\tag{832.22}
$$
令 $\partial_\nu$ 为 $dh=(\partial_\nu h)\nu$ 定义的有理导子，并置
$$
A=\Omega/\nu,\qquad
\ell_{r+1}=\partial_\nu\ell_r+\ell_rA.
\tag{832.23}
$$

**引理 832.4。** 若 $f$ 非零，则
$$
\boxed{\quad
\operatorname{ord}_P f
\le R-1+\binom R2d
\le R-1+\binom R2(M+4G-4).
\quad}
\tag{832.24}
$$

**证明。** 分四步。

第一步，逐次循环行的极部有明确界：
$$
(\ell_r)_a\in H^0(X,\mathcal O(rD))
\qquad(r\ge0,\ 1\le a\le R).
\tag{832.25}
$$
$A$ 的条目极部受 $MQ+K_\nu\le D$ 控制。若 $\nu$ 在一点有 $k$ 阶零，则局部导子最多使已有函数的极阶增加 $k+1$；$D$ 在该点的系数至少为 $k+1$。在 $Q$ 而 $\nu(Q)\ne0$ 的情形，增加至多一阶，也由 $M\ge1$ 吸收。在这些点之外，正则函数的导数仍正则。故
$\partial_\nu H^0(\mathcal O(rD))\subset H^0(\mathcal O((r+1)D))$，与乘 $A$ 一起归纳得到 (832.25)。$P$ 不在 $D$ 的支撑中。

第二步，令 $r$ 为全部循环行在 $k(X)$ 上张成空间的维数。因为 $f\ne0$，有 $1\le r\le R$，而首 $r$ 行
$\ell_0,\ldots,\ell_{r-1}$ 已经独立。确实，一旦
$\ell_s$ 属于此前行的 $k(X)$ 张成空间，对此关系施以
$\partial_\nu+\text{右乘 }A$，便见该空间在这一连接下稳定，后面的行不会再增加维数。

取首 $r$ 行组成的矩阵 $L$。任一非零 $r\times r$ minor 都是有理函数，(832.25) 给其极部至多
$$
\left(0+1+\cdots+(r-1)\right)D=\binom r2D.
\tag{832.26}
$$
因此其在 $P$ 的零阶至多 $\binom r2d$。特别，全部最大 minor 生成的局部理想的赋值至多这个数。

第三步，在 $P$ 的形式邻域取局部参数 $t$，使
$dt=\nu$、$t(P)=0$。特征零逐项积分给这样的形式参数，并且它与任意原代数参数有相同消失阶。系统在 $P$ 正则，故存在
$$
Y(t)\in\operatorname{GL}_R(k[[t]]),\qquad
Y(0)=I,\qquad Y'=AY.
\tag{832.27}
$$
令 $v(t)=\ell_0Y(t)$。由 (832.23)，
$$
L\,Y=
\begin{pmatrix}
v\\v'\\ \vdots\\v^{(r-1)}
\end{pmatrix}.
\tag{832.28}
$$
右乘形式可逆矩阵不改变最大 minor 理想：Cauchy–Binet 给一个方向的包含，乘 $Y^{-1}$ 给反向包含。

$v$ 的 $R$ 个分量在 $k$ 上张成一个恰为 $r$ 维的函数空间 $\mathcal V$. 这里可以完全在特征零形式级数中证明 Wronskian 判据：任何有限维的级数空间均可选一个常数基，其消失阶严格递增；这些基函数的 Wronskian 首系数是非零的整数 Vandermonde 因子乘各首系数，故非零。于是无限导数矩阵的行秩等于分量的常数张成维数。前两步给这一行秩为 $r$。

对分量作常数列变换，把 (832.28) 的非零部分选成 $\mathcal V$ 的一组基。其非零最大 minor 都是这一基的 Wronskian 的非零常数倍。因此
$$
\operatorname{ord}_P\operatorname{Wr}(\mathcal V)
\le\binom r2d.
\tag{832.29}
$$

第四步，选适配消失过滤的常数基，令其严格递增阶数为
$$
0\le a_0<a_1<\cdots<a_{r-1}.
$$
在参数 $t$ 中直接展开行列式，得到
$$
\operatorname{ord}_P\operatorname{Wr}(\mathcal V)
=\sum_{b=0}^{r-1}a_b-\binom r2.
\tag{832.30}
$$
其首系数中的因子 $\prod_{a<b}(a_b-a_a)$ 在特征零中非零；这里不要求它是 $p$ 进单位。由于 $a_b\ge b$，
$$
a_{r-1}\le
\operatorname{ord}_P\operatorname{Wr}(\mathcal V)+r-1.
\tag{832.31}
$$
每个非零常数组合的阶数至多 $a_{r-1}$。原解列 $F=YF(0)$，所以
$f=vF(0)\in\mathcal V$；将 (832.29) 代入 (832.31)，再用
$r\le R$，即得 (832.24)。$\square$

证明可在包含实际高度常数的 $k=\mathbb C_p$ 上完成。有理函数的极部次数、形式基础解及 Wronskian 论证在常数扩张后都保持。因此不能因为输出行含第二类周期或真实高度常数，就丢掉这一估计；同时，也没有任何一步把这些常数宣称为代数数。

## 5. 应用于原外积

对第 3 节的系统取 $P=c_1$、$M=2G$、$R=21G+4$。所有函数在 $c_1$ 正则，原 $z=a-1$ 是同一点的参数。R634 的非恒零输入与引理 832.4 于是给
$$
\operatorname{ord}_{c_1}E_{ij}
\le21G+3+\binom{21G+4}{2}(6G-4)=\mathcal B(G).
\tag{832.32}
$$
结合 R682 的下界，定理 832.1 的 (832.5) 成立。

此证明没有把深度符号 $D_2$ 或 $D_4$ 当作二阶、四阶普通导数。旧深度符号仅用于已经完成的非恒零输入；新的接触阶控制来自原代数系统的全局极部和普通形式 Wronskian。

## 6. 原六层亏格的统一公式

为使 $p$ 依赖不隐藏在 $G$ 中，这里将 R738 的原陪集论证写成一般 $p\equiv5\pmod6$ 的纸面计数，不运行新的有限群枚举。

R575 的原曲线在几何上是
$$
X=\operatorname{Norm}
\left(X_{\rm ns}^+(p)\times_j\mathbb P^1_a\right),
\qquad j=6912a^3(1-a^3).
\tag{832.33}
$$
原 $a=\sqrt[3]4\,u$ 扭曲不改变几何亏格。tame 群为 Brau–Jones 的 $H_6$ 图式；在行列式一分量中，六个陪集以
$k\in\operatorname{GL}_2(\mathbf F_2)$ 标记。R738 的相同标签给
$$
kS=kS_2,\qquad
kT=C^{-1}kT_2,\qquad
kR=C^{-1}kC,\qquad R=ST,
\tag{832.34}
$$
其中 $C$ 的阶为三。$S$ 在六标签上无固定点，$T$ 是一个六循环，$R$ 有三个固定点。

$p$ 因子的陪集是 $\mathbf P^1(\mathbf F_{p^2})$ 中非实点的无序共轭对，共 $p(p-1)/2$ 个。行列式一群在这些对上传递，因为非分裂 Cartan 的行列式范数已满射到 $\mathbf F_p^\times$。中国剩余定理给完整群在两个因素的直积上传递，故原几何曲线连通且指数为
$$
\mu=6\cdot\frac{p(p-1)}2=3p(p-1).
\tag{832.35}
$$

在 $p$ 标签上，右 $R$ 作用为 $z\mapsto-1/z-1$。阶为三的置换若固定一个两元素集合，就必须逐个固定其元素；因此固定共轭对只有
$\{\zeta,\zeta^2\}$。这里 $p\equiv2\pmod3$ 保证这是一对非实点。故完整 $R$ 固定点数为 $e_3=3$。tame $S$ 无固定点，故 $e_2=0$。

右 $T$ 作用为 $z\mapsto z-1$，每个非实共轭对的轨道长恰为 $p$；非平凡平移不能逐点固定，阶为奇数 $p$ 的平移也不能只交换这两个元素。与 tame 六循环结合，每个完整尖点轨道长为 $6p$，尖点数因而是
$$
c=\frac{\mu}{6p}=\frac{p-1}{2}.
\tag{832.36}
$$
含 $-I$ 的模群标准 genus 公式给
$$
G=1+\frac{\mu}{12}-\frac{e_2}{4}-\frac{e_3}{3}-\frac c2
=\frac{(p-1)^2}{4}.
\tag{832.37}
$$
这证明 (832.6)。在 $p=41$ 时与既有 R738 的实际 genus $400$ 一致；这里没有重跑该已成计算。

## 7. 对原有限 jet 与提取器的实际改进

保持第 2 节已经选好的代数代表。令 $\mathcal V_{\rm alg}$ 为第 3 节所有标记函数的 $K$ 常数张成空间。引理 832.4 对任意输出行同时适用，所以
$$
\mathcal V_{\rm alg}\otimes_K\mathbb C_p
\longrightarrow
\mathbb C_p[[z]]/(z^{\mathcal B(G)+1})
\tag{832.38}
$$
是单射。

特别，对 R716 的原标记族 $\mathscr B^{\rm raw}$，这里
$M=2G$、$h=3G-2$，标记列数为 $6h+8=18G-4$。完整矩阵
$$
J_{\le\mathcal B}
=\bigl([z^n]B\bigr)_{
0\le n\le\mathcal B(G),\ B\in\mathscr B^{\rm raw}}
\tag{832.39}
$$
的核恰为全部完整形式函数关系，不只是一个截断关系空间。全部条目仍在有限数域 $K$ 中。于是：

1. 不必先构造 R699 的 Ore 公共湮灭算子或求其 indicial 整数根，就可给准确关系计算一个预定的最终截止阶。
2. 可在 (832.39) 中选列基和可逆行子矩阵，所有提取行指标都满足 $n\le\mathcal B(G)$。
3. R716.23 的真实恒等式及另三个混合提取值保持：
$$
\sum_{n\in S}a_n[z^n]E_{ij}
=-L_j^{-2}\ne0,\qquad S\subset[0,\mathcal B(G)].
\tag{832.40}
$$
4. 因而即使尚不知道 $T_p$ 是否为零，原外积也必有一个非零 jet 位于这个明确窗口中。证明未给出哪个 jet 是首项，也未给其赋值。

本篇没有实际生成 (832.39)。它的窗口可能很大；已有较短首阶算子、已成 jet 或早期满秩证书应优先复用，不能因这个上界存在而重复计算。正式新算术仍只在公开仓库 Actions 执行。

## 8. 与原二阶商类和整盘排除的区别

在原 $m=1$ 情形，R785 的 $T_p$ 控制的是
$[z^2]E_{ij}$ 这一指定二阶块。定理 832.1 不证明 $T_p\ne0$，也不把一个 $n>2$ 的非零 jet 改名为二阶非零。它替代的是“必须先知道二阶非零才能为接触阶搜索给出截止”这一需求。

要把更高接触阶用于 R724 的盘上认证，仍需同时做到：

- 证明实际低阶系数精确为零，才可除去相应的 $z^e$；有限精度近零不提供这个精确因子；
- 使用同一实际规范高度和周期给出所需系数与完整尾部证书；
- 对除去中心精确因子的全部实际外积完成相应的 Bézout/共同根排除，而不能只用接触阶上界。

R703/R716 的相对全尾仍保留其代数整性常数和矩阵逆的 $p$ 进赋值；(832.4) 没有使这些量成为单位或与 $p$ 无关。对原 $p^4$ 候选盘的完全排除、R724.33 的实际有限 Bézout 以及全 $p$ 的一致存在性，仍是未闭合的高度输入。本篇既没有任换高度，也没有从实 Rosati 正性推出 $p$ 进非零。

## 来源与范围

- R634，原规范外积与每个 $E_{ij}$ 的非恒零；R682，原共同 Abel 阶和下界；R699，精确 splitting 不变性、单极点代表及真实规范全纯常数；R703/R716，完整有限关系、混合提取器与相对全尾。本文只加强其预定 jet 窗口，不重记这些结论。
- A. Besser, J. S. Müller, P. Srinivasan, *p-adic adelic metrics and Quadratic Chabauty I*, arXiv:2112.03873v4，2026-01-16，<https://arxiv.org/html/2112.03873v4>。同曲率全纯差及曲率表达的具体使用已经由 R699/R716 逐式固定；原第二类周期和规范线性项仍全部保留。
- R575，实际六层和原扭曲；R738 原陪集方法。一般 $p$ 的计数在第 6 节完整证明。J. Brau, N. Jones, *Elliptic curves with 2-torsion contained in the 3-torsion field*, Proc. Amer. Math. Soc. 144 (2016), 925–936，Theorem 1.4，<https://homepages.math.uic.edu/~ncjones/2tin3t.pdf>，为原 tame 模型来源。
- N. Dogra, S. Le Fourn, *Quadratic Chabauty for modular curves and modular forms of rank one*, Math. Ann. 380 (2021), 393–448，§3.1 Corollary 2，<https://link.springer.com/article/10.1007/s00208-020-02112-3>。旧笔记中的 $16g^3+15g^2-16g+10$ 是其好辅助素数下二重 QC 函数的零点估计；这里没有将该式直接用于原坏素数的长度四外积。第 4 节给的是独立的特征零形式接触阶证明，不需要好约化。
