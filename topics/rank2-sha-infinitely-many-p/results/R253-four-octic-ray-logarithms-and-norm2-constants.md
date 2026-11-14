# R253 — 四个真实八次 ray 对数、六维独立性与 norm-two 非齐次常数

日期：2026-11-13。**状态：四个明确全局单位的乘法独立、四个原八次角色对数的非零及代数系数独立性、连同两个 CM17 对数的六维独立性、完整分布式及原解析半径均已证明。尚未将它们等同于三条秩二曲线的中央导数。**

这次使用真正的八次 ray 角色。它们的原对数中心值非零，与此前
三个四次角色的中心值零不同。中心化后的 norm-two 分布含四个
已经证明非零的固定常数，不能把该项省去。

## 1. 固定十七挠点和一个明确的全局单位

取原
$$
E_0:y^2=x^3-x,\qquad dz=dx/(2y),\qquad \beta=4-i.
$$
固定 $P\in E_0[\beta]\setminus\{O\}$。R59 的实际 division 多项式给
$$
\begin{aligned}
K(X)={}&(4-i)X^8+(-12+20i)X^6\\
 &+(28+10i)X^4+(-20-12i)X^2-i,\qquad K(x(P))=0.
\end{aligned}
\tag{1}
$$
令
$$
r(z)=\frac{x(z)-1}{x(z)+1},\qquad
r_j=r(3^jP)\quad(0\le j\le3).
$$
设 $T=r(P)$。把 $X=(1+T)/(1-T)$ 代入 (1)，准确得到
$$
\frac{(1-T)^8}{16i}K\left(\frac{1+T}{1-T}\right)=f(T),
\tag{2}
$$
其中
$$
\begin{aligned}
f(T)={}&T^8+(8-4i)T^7+(-4+8i)T^6+(-8-12i)T^5\\
 &+(-10-48i)T^4+(-8-12i)T^3+(-4+8i)T^2\\
 &+(8-4i)T+1.
\end{aligned}
\tag{3}
$$
这是 $\mathbf Z[i]$ 上首一、常数项一的多项式。因此 $r(P)$ 和它的
逆都是代数整数；四个 $r_j$ 都是全局代数单位，不只是除去某些素数后的单位。

对高斯素理想 $(2+i)$ 约化，$i=3\in\mathbf F_5$，(3) 变为
$$
\bar f=T^8+T^7+T^5+T^4+T^3+T+1.
\tag{4}
$$
精确证书给出
$$
T^{5^8}\equiv T\pmod{\bar f},\qquad
\gcd(T^{5^4}-T,\bar f)=1.
\tag{5}
$$
并列出第二式的多项式 Bezout 证书。(5) 证明 $\bar f$ 不可约：
第一式使每个不可约因子的次数整除八，第二式排掉所有整除四的次数。
由 Gauss 引理，$f$ 在 $\mathbf Q(i)$ 上不可约。所以
$$
L=\mathbf Q(i,x(P))=\mathbf Q(i,r(P)),\qquad
[L:\mathbf Q(i)]=8.
$$

## 2. 真正的八阶 Galois 作用

原椭圆曲线的三倍公式是
$$
x(3P)=x(P)
\frac{x(P)^8+12x(P)^6+30x(P)^4-36x(P)^2+9}
     {(3x(P)^4-6x(P)^2-1)^2}.
\tag{6}
$$
在 (1) 的八次商环中，它准确约化为
$$
g(X)=(-2+i/2)X^7+(6-10i)X^5+(-14-5i)X^3+(10+13i/2)X.
\tag{7}
$$
证书逐项核定
$$
K(g(X))=0,\quad g^{\circ4}(X)=-X,\quad
g^{\circ8}(X)=X\quad\pmod K,
\tag{8}
$$
而前八个像互异。因 (1) 不可约，$X\mapsto g(X)$ 定义 $L/\mathbf Q(i)$
的阶八自同构 $\sigma$；它们已给出全部八个共轭。几何上正是
$P\mapsto3P$，不是另外挑选的单位排列。

由于 $3^4=13=-4\bmod17$，且 $i$ 在 $E_0[\beta]$ 上为 $4$，
(8) 也来自 $x(iP)=-x(P)$。于是
$$
\boxed{\sigma^j(r_0)=r_j,\qquad r_{j+4}=r_j^{-1},
       \qquad r_{j+8}=r_j.}
\tag{9}
$$

## 3. 四单位乘法独立的严格证书

这一部分只作一个固定数域的严格复区间计算，不扫描目标素数。
在八个根中，取 (1) 在下列有理盒中的唯一根：
$$
-\frac{22533}{10000}<\Re x_0<-\frac{22532}{10000},\qquad
\frac{11246}{10000}<\Im x_0<\frac{11247}{10000}.
\tag{10}
$$
用 (6) 运输同一个根，令
$$
\ell_j=\log|r(3^jP)|\qquad(0\le j\le3)
$$
表示这个复嵌入中的实对数。256-bit Arb 的全根隔离和有理区间
运算给出下面的严格界：

| $j$ | $10000\,\ell_j$ 的下界 | 上界 |
|---:|---:|---:|
| 0 | 7149 | 7151 |
| 1 | 6330 | 6332 |
| 2 | −22928 | −22927 |
| 3 | −1882 | −1880 |

这些是严格包含区间，不是由浮点近似猜测的等式。特别
$$
\boxed{|\ell_2|-|\ell_0|-|\ell_1|-|\ell_3|
>\frac{7562}{10000}>\frac34.}
\tag{11}
$$
所有数值步骤只涉及固定八次多项式根、四个有理函数值和四个实对数；
脚本同时给出更窄的含误差区间和每个有理界的布尔验证。

假设 $\prod_{j=0}^3r_j^{n_j}$ 是根单位。施以
$1,\sigma,\sigma^2,\sigma^3$ 再取上述绝对值对数，得到
$$
\mathcal R(n_0,n_1,n_2,n_3)^{\mathsf T}=0,\qquad
\mathcal R_{a,j}=\ell_{a+j},\quad\ell_{j+4}=-\ell_j.
$$
把列按 $2,1,0,3$ 排列，每行的对角元绝对值都是 $|\ell_2|$，
其余三项的绝对值和为 $|\ell_0|+|\ell_1|+|\ell_3|$。
由 (11)，矩阵严格行对角占优，故可逆。这里也可直接证明：
若核向量非零，选其绝对值最大的坐标，所在行的对角项严格大于
其余项之和，矛盾。因此
$$
\boxed{r_0,r_1,r_2,r_3\text{ 在 }L^\times/\mu(L)\text{ 中乘法独立。}}
\tag{12}
$$
这个结论没有使用尚未证明的椭圆调节子或 Sha 有限性。

## 4. 四个八次原对数及六维代数独立关系

固定任意 $p>19$ 及代数闭包到 $\overline{\mathbf Q}_p$ 的嵌入，
使用标准 $\log_p$。令 $\zeta=\zeta_8$，对 $k=1,3,5,7$ 定义真正的
八次角色
$$
\chi_k(3)=\zeta^k\quad\text{于 }\mathbf F_{17}^\times.
$$
因为 $i=3^{12}$，准确有
$$
\chi_k(-1)=1,\qquad \chi_k(i)=-1.
$$
取原挠点对数 germ
$$
\Psi_k(z)=\sum_{a\in\mathbf F_{17}^{\times}}
       \chi_k(a)^{-1}\log_p r(z+aP),\qquad C_k=\Psi_k(0).
\tag{13}
$$
由 (9) 将十六项两次配对，得到准确的四项式
$$
\boxed{C_k=4\sum_{j=0}^3\zeta^{-kj}\log_p r_j.}
\tag{14}
$$
四个单位的 $p$ 进对数在 $\mathbf Q$ 上线性独立。事实上，若有整数
线性关系，它使相应全局单位的局部对数为零；单位上 $\log_p$ 的核
是根单位，所以该乘积本身是代数根单位，与 (12) 矛盾。

Brumer 的 $p$ 进对数定理把这种 $\mathbf Q$ 线性独立提升为
$\overline{\mathbf Q}$ 线性独立。(14) 的四乘四矩阵是四个不同
八次根对应的 Vandermonde 矩阵，故可逆。因此
$$
\boxed{C_1,C_3,C_5,C_7
\text{ 在 }\overline{\mathbf Q}\text{ 上线性独立；特别全部非零。}}
\tag{15}
$$

还可同时加入 R246 的两个固定对数。若
$$
\left(\prod r_j^{n_j}\right)17^m
\left(\frac{4+i}{4-i}\right)^n
$$
是根单位，先比较 $L$ 中位于 $(4+i)$、$(4-i)$ 之上的有限赋值。
四个 $r_j$ 都是全局单位，所以得到 $m+n=m-n=0$。
随后 (12) 给出所有 $n_j=0$。再用 Brumer 及 (14)，得到
$$
\boxed{
C_1,C_3,C_5,C_7,\quad
\log_p17,\quad \log_p\frac{4+i}{4-i}
\text{ 六者在 }\overline{\mathbf Q}\text{ 上线性独立。}}
\tag{16}
$$
这里只证明线性独立，不声称这些对数的乘积代数独立。

## 5. 原 norm-two 与奇 CM 分布的全部常数

令 $\Phi_k=\Psi_k-C_k$。二挠分布笔记已从原除子和常数归一证明
$$
r(iz)=r(z)^{-1},\qquad r(z+T_0)=-r(z)^{-1},
\qquad E_0[1+i]=\{O,T_0\}.
$$
故 $\Psi_k(iz)=\Psi_k(z)$，且
$$
\boxed{\Phi_k\in z^4\overline{\mathbf Q}_p[[z^4]],\qquad
\sum_{Q\in E_0[1+i]}\Psi_k(z+Q)=0,\qquad
\sum_{Q\in E_0[1+i]}\Phi_k(z+Q)=-2C_k\ne0.}
\tag{17}
$$
这里 $\log_p(-1)=0$；最后的非零结论由 (15) 给出。四次角色的中心
为零，不能把它们的齐次分布直接沿用到这四个八次角色。

对奇 $\alpha\in\mathbf Z[i]$、$(\alpha,\beta)=1$，记
$n=N\alpha$、$\epsilon_\alpha=1$ 若 $\alpha=1\bmod2$，
$\epsilon_\alpha=-1$ 若 $\alpha=i\bmod2$，并令
$$
\mu_{k,\alpha}=\epsilon_\alpha\chi_k(\alpha\bmod\beta).
$$
原准确范数式
$\prod_{Q\in E_0[\alpha]}r(z+Q)=r(\alpha z)^{\epsilon_\alpha}$
逐项取 $\log_p$，再以 $a\mapsto\alpha a$ 置换原十七标签，给
$$
\boxed{\begin{aligned}
\sum_{Q\in E_0[\alpha]}\Psi_k(z+Q)
 &=\mu_{k,\alpha}\Psi_k(\alpha z),\\
\sum_{Q\in E_0[\alpha]}\Phi_k(z+Q)
 &=\mu_{k,\alpha}\Phi_k(\alpha z)+(\mu_{k,\alpha}-n)C_k.
\end{aligned}}
\tag{18}
$$
这些是完整原 germ 的恒等式，包括原中心常数。

特别 $\pi=2+i$、$\bar\pi=2-i$ 模 $\beta$ 分别是
$6=3^{15}$、$15=3^6$，而两者的 $\epsilon$ 都为 $-1$，所以
$$
\boxed{\mu_{k,\pi}=-\zeta^{-k},\qquad
       \mu_{k,\bar\pi}=i^k.}
\tag{19}
$$
其绝对值为一，因而 $\mu_{k,\pi}-5$、$\mu_{k,\bar\pi}-5$ 都不是零。
式 (18) 的 norm-five 常数也都是非零的明确代数倍 $C_k$。

## 6. 同一原解析半径与相邻权全纯来源

令 $u=x^{-1/2}$ 为原形式参数，在 $p>19$ 处取首项为 $z$ 的支。
各个 $aP$ 在好约化处不会落在 $r$ 的二挠零极点上，故
$$
\frac{d}{du}\log_p r(z(u)+aP)\in\mathcal O[[u]].
$$
角色系数是单位，所以 $d\Psi_k/du$ 同样整。又因 $\Psi_k$ 在
$u\mapsto iu$ 下不变，若
$$
\Phi_k(z(u))=\sum_{m\ge1}b_m u^{4m},
$$
则准确有 $4m\,b_m\in\mathcal O$，即
$v_p(b_m)\ge-v_p(m)$。在 R54 的原半径
$R=p^{-1/(2p)}$ 上，
$$
\boxed{\|\Phi_k\|_R\le
\sup_{m\ge1}p^{v_p(m)}R^{4m}=R^4.}
\tag{20}
$$
证明最后等号：$m=p^a b$、$p\nmid b$ 时，只须比较 $b=1$；
$a=0$ 的最大值是 $R^4$，而 $a\ge1$ 时指数
$a-2p^{a-1}\le-1<-2/p$。原 $u(z)$ 在该盘等距，故此界也用于
实际加法变量 $z$。这次使用的是四个角色和的真实 $i$ 不变性；
不是把每个单独平移对数的线性首项成本任意删掉。

仍令 $F=S_8^{17}$，$\mathcal F(z)=F(\beta z)$，其实际次数为
$N=1156$。于是
$$
\mathcal H_k(z)=\mathcal F(z)\Phi_k(z)
$$
是一个固定实际对数来源、中心质量零，且 R54/R245 的共同 gauge
余项满足同样的 $R^4$ 界。其完整 $\mathcal J_{Nc_0}$ 因而收敛。
对未中心化来源 $\mathcal F\Psi_k$，中心质量准确为 $C_k$，
不能以归一化为由预设该质量是 $p$ 进单位。

真正可用于相邻权投影的全纯来源为
$$
\boxed{\mathcal B_k=-\frac18\mathcal F\,\Phi_k'' .}
\tag{21}
$$
$\Phi_k''$ 是固定代数椭圆函数；其极点至多二阶，在
二挠点减去 $aP$ 处。$\mathcal F$ 在这些点的零重至少十七，
故 (21) 全局全纯。它有 $i$ 特征 $-1$，在原点从 $z^2$ 开始或
更高，特别质量零。全体 $[2]$ 拉回后，它位于 R248/R251 的
真实 degree-$4624$ 相邻权模型；这一步不把其有限投影当中央泛函等变。

## 7. 带真实 theta frame 的完整 Mellin 分布

以下式子把新常数交给后续原投影，而不换成裸 ray 行。
对 (18) 的任意一个固定奇 $\alpha$，排除其有限坏素数，令
$$
U_{\alpha,p}=\alpha^{p+1}/N\alpha,\qquad
J_{\mathcal F}(u)=\mathcal J_{Nc_0}(\mathcal F;u),\qquad
J_{\mathcal H_k}(u)=\mathcal J_{Nc_0}(\mathcal H_k;u).
$$
将 (18) 乘实际共同 frame $\mathcal F(\alpha z)$，直接应用完整
$\mathcal J_{nNc_0}$ 及已证明的 CM 缩放，得
$$
\boxed{\begin{aligned}
&\sum_{Q\in E_0[\alpha]}
\mathcal J_{nNc_0}\bigl(\mathcal F(\alpha z)\Phi_k(z+Q);u\bigr)\\
&\quad=U_{\alpha,p}^{u}
\left[\mu_{k,\alpha}J_{\mathcal H_k}(u)
+(\mu_{k,\alpha}-n)C_k J_{\mathcal F}(u)\right].
\end{aligned}}
\tag{22}
$$
左侧每个 germ 以及 theta frame 都明确，不把它偷换成
$\mathcal J$ 与未支付的平移算子交换。

norm-two 方向则由 (17) 给出更短的实际式：
$$
\boxed{\begin{aligned}
&\sum_{Q\in E_0[1+i]}
\mathcal J_{2Nc_0}\bigl(\mathcal F((1+i)z)\Phi_k(z+Q);u\bigr)\\
&\quad=-2C_k\,U_{1+i,p}^{u}J_{\mathcal F}(u).
\end{aligned}}
\tag{23}
$$
因此左侧的真实中心质量是 $-2C_k\ne0$。求中央导数时还必须保留
$-2C_k(\log_pU_{1+i,p}+J_{\mathcal F}'(0))$；不能把 (23) 的非零
质量当成原秩二曲线的非零中央导数。

式 (22)–(23) 使用完整 germ 及共同 frame，故所有移权和以后做
协变微分时的交换差仍由原对象决定。新输入是四个已经非零且独立的
固定对数和实际非齐次分布；其到原 $A/B/H$ 的完整中央比较仍须完成。

## 精确证书和来源

- [脚本](../scripts/check-ray17-octic-log-constants.py) 与
  [输出](../scripts/check-ray17-octic-log-constants.json) 包含 (2)、
  (5) 的全部有限域证书、(7)–(9) 的原商环运算，以及 (10)–(11)
  的严格全根隔离和区间比较。没有目标素数样本外推。
- 原十七 division 模型：R59；原二挠除子和 norm 分布：
  [二挠对数分布笔记](../notes/2026-11-13-two-torsion-log-distribution-and-primitive-projection.md)。
  原共同比例及完整解析半径：R54、R245、R248。
- A. Brumer，*On the units of algebraic number fields*，
  Mathematika **14** (1967)，121–124，Theorem 1，
  [DOI](https://doi.org/10.1112/S0025579300003703)。
  此处所用准确单位对数形式也见 R. Sharifi，
  [Iwasawa Theory，Theorem 1.5.17](https://math.ucla.edu/~sharifi/notes/iwasawa-ch01.html)，
  核读日期 2026-11-13。
