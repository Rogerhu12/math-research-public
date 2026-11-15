# R652 — 原 sigma 的正则多项式系统、五次 jet 界与完整坏素数成本

日期：2026-11-15。**状态：已证明。**

R644 对原五来源的每个固定次数给出了有效有限坏素数集合，但没有估计所需的 jet 长度。本篇用原 sigma 的一个五变量正则多项式微分系统，把该长度明确界为 $O(D^5)$，并构造一个非零整数 jet 证书，付清其 $O(D^7\log D)$ 的对数高度。

零点重数只引用已经发表于 Duke Math. J. 的 Binyamini 定理；原变量、正则初值、换时、次数、整导数证书及全部成本在下面直接推导。这个长度界本身不删除整数证书的坏素数，也不把原中央零延到闭边界。

## 1. 原有限空间和结论

保持 R644 的全部原五来源、参数 $u=x^{-1/2}$、$b=17$ 与完整中央规范。对 $D\ge1$ 置
$$
K=66D,\qquad M=72D,\qquad d_*=K+2M=210D,
$$
$$
N_D^*=K(M+1),\qquad
\Lambda_D=64(210D+24)^5,\qquad
J_D^{\rm bd}=\Lambda_D-M.
\tag{1}
$$
继续使用 R644 的实际有理系数族
$$
B_{a,\beta,m}(u)
=u^K x(u)^a y(u)^\beta h(z(u))^m,
\quad h=\sigma/z,
$$
$$
\beta\in\{0,1\},\quad 2a+3\beta\le K,\quad0\le m\le M.
\tag{2}
$$

**定理 1。** R644 的确定逐行消元在至多 $J_D^{\rm bd}$ 阶终止。因此原 $u$-jet 长度可取
$$
\boxed{J_D\le64(210D+24)^5-72D.}
\tag{3}
$$
此外可构造一个非零整数 $A_D$，使
$$
\boxed{
p=6s-1>\Lambda_D,\quad p\nmid A_D
\ \Longrightarrow\
\mathcal A_{D,p}\cap\mathbf C_p\langle z/R_E\rangle
=\mathbf C_p.}
\tag{4}
$$
这里 $\mathcal A_{D,p}$ 是 R644 的整个实际 degree$\le D$ 多项式空间，允许系数依赖当前 $p$。

这个整数具有显示的高度界
$$
\boxed{
\log|A_D|\le\mathfrak H_D:=
\frac{N_D^*}{2}\log N_D^*
+N_D^*\Lambda_D\log\!\bigl(51(d_*+6\Lambda_D)\bigr)
=O(D^7\log(D+1)).
}
\tag{5}
$$
如果 $|A_D|=1$，左边取零。所有常数均已显示。

## 2. 原变量的正则系统

令 $\zeta=\sigma'/\sigma$，并在原 $z=0$ 附近定义
$$
U=u(z),\quad R=(1+bU^6)^{1/2},\quad
V=\zeta+\frac{x^2}{y},\quad
A=\frac{\sigma}{U},\quad Z=z.
\tag{6}
$$
这里的 $A$ 是本节实际 sigma 比值，不是旧原矩阵中的临界值；下文只用于明确的微分系统。

这些变量全部正则，初值为
$$
(U,R,V,A,Z)(0)=(0,1,0,1,0).
\tag{7}
$$
$V$ 的两个简单极准确相消。由
$x=U^{-2}$、$y=-U^{-3}R$、$dz/dU=R^{-1}$，
$$
\frac{dU}{dz}=R,\qquad
\frac{dR}{dz}=3bU^5.
$$
又因 $\zeta'=-x$、$x'=2y$、$y'=3x^2$，
$$
\frac{d}{dz}\!\left(\zeta+\frac{x^2}{y}\right)
=3x-\frac{3x^4}{y^2}
=\frac{3bx}{y^2}
=\frac{3bU^4}{R^2}.
\tag{8}
$$
最后，
$$
\frac{A'}A
=\zeta-\frac R U
=V+\frac1{UR}-\frac R U
=V-\frac{bU^5}{R}.
\tag{9}
$$
这里没有删去原 sigma 的一个 Gaussian。

引入一个仅用于本节估计的局部时间 $\tau$：
$$
\frac{d\tau}{dz}=R^{-2},\qquad \tau(0)=0.
$$
初值导数为一，所以它不改变任何零点阶。
按原 $U$ 直接积分得到
$$
\boxed{
\tau(U)=\int_0^U(1+bt^6)^{-3/2}\,dt
=\sum_{j\ge0}\binom{-3/2}{j}
 \frac{b^jU^{6j+1}}{6j+1}.}
\tag{10}
$$
乘回全部 $R^2$ 后，(8)–(9) 成为五变量的真正多项式向量场
$$
\boxed{
\mathscr V=
R^3\partial_U
+3bU^5R^2\partial_R
+3bU^4\partial_V
+(VR^2-bU^5R)A\partial_A
+R^2\partial_Z .}
\tag{11}
$$
其总次数至多七，系数为整数。
在 (7) 处的值是 $(1,0,0,0,1)$，所以该点**非奇异**。
这避免了直接使用 $u\partial_u$ 时原点成为奇点、无法套用非奇异重数定理的问题。

## 3. 完整基函数变成有界次数多项式

对 (2) 的每个基函数，定义 (11) 上的整单项式
$$
P_{a,\beta,m}
=(-1)^\beta
U^{K-2a-3\beta+m}R^\beta A^m Z^{M-m}.
\tag{12}
$$
所有幂均非负。沿原轨迹，准确有
$$
\boxed{
P_{a,\beta,m}(\tau)
=Z(\tau)^M B_{a,\beta,m}(U(\tau)).}
\tag{13}
$$
因为 $h=(\sigma/U)(U/z)=AU/Z$，(13) 保留了全部原 $z$ 分母，而非将 $U,Z$ 相认。

(12) 的总次数为
$$
K+M-2a-2\beta+m\le K+2M=d_*.
\tag{14}
$$
R644 已用原 sigma 准周期公式证明 $h$ 在椭圆函数域上超越，故 (2) 线性独立。于是任意非零常系数组合的 (12) 均不在原轨迹上恒零。
这个输入排除了重数为无穷的情形；没有用待证的中央非零来排它。

## 4. 所用的已发表重数定理与原 jet 长度

这里使用 Gal Binyamini,
*Multiplicity estimates: a Morse-theoretic approach*,
Duke Mathematical Journal **165** (2016), no. 1, 95–128，
Corollary 1，作者版本第 4 页，公式 (4)：
[原文 PDF](https://arxiv.org/pdf/1406.1858#page=4)，
[期刊 DOI](https://doi.org/10.1215/00127094-3165220)。

该推论给：在 $\mathbf C^n$ 的非奇异多项式向量场轨迹上，
次数至多 $d>n-1$ 的多项式若不恒零，其零阶至多
$$
2^{n+1}\{d+(n-1)(\delta-1)\}^{n},
\tag{15}
$$
其中向量场次数至多 $\delta$。
它不要求轨迹在整个环境空间 Zariski 稠密；本篇也没有增加这种假设。

将 (11)、(14) 的 $n=5,\delta=7,d=d_*$ 逐项代入，得到
$$
\operatorname{ord}_{\tau=0}\sum c_{a,\beta,m}P_{a,\beta,m}
\le64(d_*+24)^5=\Lambda_D .
$$
$Z(\tau)=\tau+\cdots$、$U(\tau)=\tau+\cdots$，故 (13) 给
$$
\boxed{
\operatorname{ord}_{u=0}
\sum c_{a,\beta,m}B_{a,\beta,m}
\le\Lambda_D-M=J_D^{\rm bd}
}
\tag{16}
$$
对全部非零复系数组合成立。
所以 (2) 的完整 $0,\ldots,J_D^{\rm bd}$ 系数矩阵满列秩。
矩阵有理，故该秩结论也在 $\mathbf Q$ 上成立；R644 的逐行算法必在此之前终止，证明 (3)。

## 5. 真正的整导数证书与高度

为同时控制分母，使用
$$
C_{a,\beta,m}(\tau)
=\tau^{-M}P_{a,\beta,m}(\tau)
=\left(\frac{Z(\tau)}\tau\right)^M
 B_{a,\beta,m}(U(\tau)).
\tag{17}
$$
共同因子是常数一单位，换参切线为一；(17) 的任何非零组合也具有 (16) 的阶数界。

按行号 $n=0,1,\ldots,J_D^{\rm bd}$ 对它们作有理消元，保留每条提高秩的行，直到满秩。得到 $N_D^*$ 个行号 $n_i$。
令 $q_0=(0,1,0,1,0)$，定义
$$
\boxed{
A_D=\det\left(
  (\mathscr V^{\,n_i+M}P_{a,\beta,m})(q_0)
 \right)\in\mathbf Z\setminus\{0\}.}
\tag{18}
$$
这是一个确定的整数算法，不需要选取任何目标素数。
非零性来自选中 jet 矩阵的满秩，因为两矩阵只相差行因子
$(n_i+M)!$。又
$$
n_i+M\le\Lambda_D.
\tag{19}
$$

写多项式系数的 $\ell^1$ 范数为 $\|\cdot\|_1$。
(11) 的每个分量的系数范数至多 $3b=51$，所以次数至多 $d$ 的多项式满足
$$
\|\mathscr VP\|_1
\le51\,d\,\|P\|_1,\qquad
\deg(\mathscr VP)\le d+6.
$$
(12) 各有系数范数一。
对任意 $k\le\Lambda_D$，迭代得
$$
|(\mathscr V^kP_{a,\beta,m})(q_0)|
\le51^k\prod_{j=0}^{k-1}(d_*+6j)
\le\{51(d_*+6\Lambda_D)\}^{\Lambda_D}.
\tag{20}
$$
$q_0$ 的各坐标绝对值不超过一，故求值不会增大这个界。
对 (18) 的每一列使用 Hadamard 界，立得 (5)。
这同时支付了原系数、次数和导数阶，没有将一个非零行列式当成无成本单位。

## 6. 整证书到原 p 进边界的准确运输

固定一个 $p>\Lambda_D$ 且 $p\nmid A_D$。
由 (19)，(18) 各行的阶乘在 $p$ 处是单位。
因此 (17) 在所选行上的实际有理 jet 子矩阵是整单位。

将 $h(z(u))$ 换成 R639 的同一 $T_{\rm g}(u)^{-1}$。
R644 已支付
$$
B^{(p)}_{a,\beta,m}(u)\in\mathcal O[[u]],
\qquad B^{(p)}_{a,\beta,m}-B_{a,\beta,m}
\in u^{p+1}K_p[[u]].
\tag{21}
$$
本节使用的所有行号均小于 $p$，故原有限 jet 逐项相同。

还须支付 (17) 的换时，不能只以特征零可逆代替整可逆。
式 (10) 的所有次数至多 $J_D^{\rm bd}$ 的系数在 $p$ 处整，
因为二项式系数只有二进分母，而 $6j+1<p$。
其切线是一，故同阶截断的逆也整。
同样，(11) 的整系数和整初值使 $U(\tau),Z(\tau)$ 的
第 $k$ 个系数具有整数分子和 $k!$ 分母；
到本节所需的 $\Lambda_D$ 阶均在 $\mathcal O$ 中。
因此
$$
B(u)\longmapsto
\left(\frac{Z(\tau)}\tau\right)^M B(U(\tau))
$$
在前 $J_D^{\rm bd}+1$ 条实际 Taylor 行上是整可逆的下三角变换。

从 (18) 的单位子矩阵遂得到：原完整规范后的 $u$-jet 在
$0,\ldots,J_D^{\rm bd}$ 内满列秩模 $p$。
R644 第 5–6 节的全部系数整性、Gauss 最大项及 $p^2-1$
个真实边界简单零点可以原样使用，给 (4)。
没有把 $\tau$ 当成原算术中央变量，也没有更改其 prime diagonal。

## 7. 坏素数的完整成本与尚未支付的桥

(5) 直接给原整数证书的全部坏素数估计：
$$
\sum_{\substack{q\mid A_D\\q>\Lambda_D}}
v_q(A_D)\log q\le\mathfrak H_D,
$$
$$
\boxed{
\sum_{\substack{q\mid A_D\\q>\Lambda_D}}
\frac{v_q(A_D)\log q}{q}
\le\frac{\mathfrak H_D}{\Lambda_D}
=O(D^2\log(D+1)).}
\tag{22}
$$
求和可进一步限制到本题允许的惰性素数，界仍成立。
特别 $p>\max(\Lambda_D,e^{\mathfrak H_D})$ 是不再查看
$A_D$ 的一个完全显示的充分范围；这只是一个很粗的指数界。

须区分三个已付量：jet 长度为五次多项式量，
整数证书对数高度为七次量，而所有坏素数仍保留在 (22)。
不能只保第一项，然后宣称原问题已经取得 $p>CD^5$ 的无例外算术 cutoff。

更根本地，R639 的原 $j_m=0$ 只给零初值正规解在每个严格
$R<R_E$ 的盘延拓；本篇的反证假设是闭 $R_E$ Tate。
两者之间的实际传播仍未建立。
原十九角/同 $R$/全部 carry 和有序 jet 成本也没有因使用
辅助空间 (2) 而消失。
本篇没有用一个辅助非零函数替代原 $J'_S,J'_T$。

新增的是原五来源全固定次数边界定理的明确 jet 上界、
确定的整导数证书及全部坏素数高度。
主目标与原全局严格成本门仍开放。

依赖：
[R644](R644-bounded-degree-original-polynomials-and-full-boundary-obstruction.md)；
[R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)；
[R635](R635-all-original-powers-and-formal-logarithm-boundary.md)；
Binyamini 的已发表 Corollary 1，如第 4 节所引。
