# 实际 Artin–Schreier 坐标、共同零理想与 Hecke 二阶判别式

日期：2026-11-12。**已证明。** 本篇保留原完整环类迹，
把实际二阶行的整纤维消失写成规范的局部理想。
对 R141 的非 CM 简单总迹，进一步得到一个底曲线函数的二重零判据。
尚未证明原 CM 点避开这个二重零集合。

## 1. 两个实际总迹及统一算子

取 R137 的连通 étale $C_p$ 覆盖
$$
                  \pi:Y\longrightarrow Z,\qquad
                  \Gamma=\langle\tau\rangle,\quad p\ge7.
\tag{1}
$$
其中已经保留真 full-level 的中心商、nonsplit torus 的两条轨道，
以及原 $U$ 迹；$\tau$ 的作用约定仍为 $\tau h_v=h_{\tau v}$。
以下也用于同一几何构造在 R139 的 $E_{389}$ 上的版本。
在源 ordinary 点附近，所用全部函数正则。

对实际 $U$ 迹函数 $B$，记
$$
 N_\Gamma=\sum_{j=0}^{p-1}\tau^j,\quad
 D_1=\sum_{j=0}^{p-1}j\tau^j,\quad
 D_2=\sum_{j=0}^{p-1}\binom j2\tau^j,
 \qquad n=N_\Gamma B,\quad A=D_1B,\quad F_2=D_2B.
\tag{2}
$$
这里 $F_2$ 是函数，不是原 Heegner 二次域。两个实际输入为：

| 原曲线与函数 | 完整 $B$ | 总迹 $n$ |
|---|---|---|
| $E_{17}$，R135 的 companion $h_p$ | R137 的原 $u$ 项 $h_p+V_3h_p$ 迹，等于原 $\pi$ 的 $2u$ 项迹 | 恒为 $0$，因为 $a_\ell(E_{17})=0$ |
| $E_{389}$，R141 的 $g_p=\Theta^{p-2}\bar f/H^p$ | 类数 $1$ 的原 $u$ 项去 $p$ 原函数迹，无 $V_3$ 项 | $a_\ell(E_{389})g_p\circ r_{\rm src}$ |

第二行只在 $a_\ell(E_{389})\not\equiv0\pmod p$ 时使用。
R141 已证明：除 $O(X^{3/4})$ 个 $p\le X$ 外，在源域
$\mathbb Q(\sqrt{-7})$ 分裂的合法 $p$ 上，$g_p$ 在两个固定
最大阶 CM 源点都是简单零点。由于 (1) 及其到源的映射在这些
ordinary 点 étale，$n$ 在每个带原 CM 标签的底点也有简单零点。
这里没有声称 R140 的无穷大因子集合已经满足该分裂条件。

置 $\Delta=\tau-1$。在 $\mathbb F_p[\Gamma]$ 内准确有
$$
 \Delta D_1=-N_\Gamma,\qquad
 \Delta D_2=N_\Gamma-D_1.
\tag{3}
$$
例如由 $N_\Gamma=(\tau-1)^{p-1}$ 可得
$D_1=-\tau\Delta^{p-2}$、$D_2=\tau^2\Delta^{p-3}$，继而得到 (3)。
所以统一的变换式是
$$
             \tau A=A-n,\qquad
             \tau F_2=F_2+n-A.
\tag{4}
$$
只有第一行的 $n=0$ 情形，才能把它简化为
$A\in k(Z)$ 和 $\tau F_2=F_2-A$。

## 2. 整 AS 坐标及精确局部正规形

令 $z\in Z$ 是所用函数正则的闭点，
$R=\widehat{\mathcal O}_{Z,z}$ 为完备离散赋值环，
$S$ 为 (1) 在其上方的有限 étale $R$-代数。
可以选取 $y\in S$，使
$$
 S=R[y],\qquad y^p-y=c\in R,\qquad \tau y=y+1,
\tag{5}
$$
且 $1,y,\ldots,y^{p-1}$ 为 $R$-基。这里允许 $S$ 是分裂乘积，
不假设剩余扩张一定为域。

为完整说明 (5)，有限 étale 代数的迹在每个剩余纤维满射，
故可取 $e\in S$ 满足 $\operatorname{Tr}(e)=1$。
令 $y=-D_1e$，由 (3) 得 $\tau y-y=1$。
于是 $y^p-y$ 不变，属于 $R$。在忠实平坦基变换 $R\to S$ 后，
$y$ 的 $p$ 个共轭为 $y+j$，两两差是单位；
Vandermonde 行列式可逆，故该首一 AS 代数到 $S$ 的映射为同构。

式 (4) 给唯一的 $a,g\in R$，使
$$
 \boxed{\quad
 A=-ny+a,\qquad
 F_2=\frac n2 y(y+1)-ay+g.
 \quad}
\tag{6}
$$
证明只需先观察 $A+ny$ 不变；再从 $F_2$ 中减去 (6) 的两个
非恒定项，(4) 说明余项不变。若换整坐标 $y'=y+b$、$b\in R$，
则
$$
 a'=a+nb,\qquad
 g'=g+ab+\frac n2 b(b-1).
\tag{7}
$$
因此理想
$$
                         \mathcal I=(n,a,g)\subset R
\tag{8}
$$
不依赖整 AS 坐标。

更准确地，$\mathcal I$ 是 $F_2$ 在有限自由 $R$-模 $S$ 中的
系数理想，即由所有 $R$-线性函数 $S\to R$ 在 $F_2$ 上的值生成。
因为 (6) 的次数至多 $2<p$，系数为
$n/2,n/2-a,g$，它们生成的正是 (8)。若 $t$ 为 $R$ 的参数，则
$$
 F_2\in t^eS
       \quad\Longleftrightarrow\quad
 n,a,g\in t^eR.
\tag{9}
$$
特别地，**整个几何纤维**的二阶行都为零，当且仅当
$n(z)=a(z)=g(z)=0$。不能只检查分裂纤维的一个分量。

## 3. $E_{17}$：共同零理想与原 AS 覆盖

此时 $n=0$，所以
$$
                  A=a,\qquad F_2=-ay+g,\qquad
                  \mathcal I=(a,g).
\tag{10}
$$
换 $y$ 只把 $g$ 改为 $g+ab$，理想不变。
整纤维消失准确等价于 $a(z)=g(z)=0$，共同消失阶为
$\min(v_z(a),v_z(g))$。

R137 已证明 $A\ne0$、$F_2\ne0$。故
$$
             \mathcal R=-F_2/A,\qquad
             \tau\mathcal R=\mathcal R+1,\qquad
             \mathcal R^p-\mathcal R\in k(Z)
\tag{11}
$$
确实生成原 $C_p$ 函数域扩张，而非另造的同次数覆盖。
局部 (10) 给 $\mathcal R=y-g/a$；它可能有来自底环的主部。
因此 $\mathcal R$ 的极点不表示原覆盖在那里分歧，
也不排除 $(a,g)$ 在 ordinary 点非平凡。

另有真正下降的微分
$$
                 W=A\,dF_2-F_2\,dA\in\Omega^1_{k(Z)/k},
       \qquad d\mathcal R=-W/A^2.
\tag{12}
$$
R137 的公共简单超奇异极点界说明 $W$ 至多有二阶超奇异极点：
两函数首项都是 $t^{-1}$ 时，可能的三阶项相消。
若在一个 ordinary 底点 $F_2\in t^eS$ 且 $A\in t^eR$，则
$W\in t^{2e}\Omega^1_{S/k}$，从而底点上也有同样的消失下界。
这里不预设 $W\ne0$；一般 AS 生成元仍可能是函数域中的 $p$ 次幂。
微分的下降和极点界并不自动给原 CM 点上的非零值。

## 4. $E_{389}$：真正的二阶判别式

一般 $n$ 下，定义实际函数
$$
                  \boxed{\ \mathscr D=A^2-nA-2nF_2.\ }
\tag{13}
$$
将 (4) 直接代入可见 $\tau\mathscr D=\mathscr D$，所以
$\mathscr D\in k(Z)$。由 (6) 有同一局部式
$$
                          \mathscr D=a^2-na-2ng.
\tag{14}
$$
它也可写成原 $p$ 条完整 $U$ 迹的二次组合。记 $B_j=\tau^jB$，
则
$$
 \mathscr D
  =\left(\sum_j jB_j\right)^2
       -\left(\sum_jB_j\right)\left(\sum_jj^2B_j\right)
  =-\sum_{i<j}(i-j)^2B_iB_j.
\tag{15}
$$
这里的权是 $\mathbb F_p$ 权，不是正实权；(15) 不提供正定性。

**简单总迹处的精确判据。**
设 $n(z)=0$、$v_z(n)=1$。则
$$
 \boxed{\quad
 F_2|_{\pi^{-1}(z)}=0
  \quad\Longleftrightarrow\quad
 v_z(\mathscr D)\ge2.
 \quad}
\tag{16}
$$
若 $\mathscr D$ 恒为零，右边按无穷阶解释。
这是整纤维条件，不是某个任意同次数覆盖的点值条件。

证明如下。在 $z$ 处，(14) 首先给
$\mathscr D(z)=a(z)^2$。所以其为零当且仅当 $a(z)=0$。
再微分 (14)，在 $n(z)=a(z)=0$ 时得到
$$
                         d\mathscr D(z)=-2g(z)\,dn(z).
\tag{17}
$$
因为 $dn(z)\ne0$、$2$ 可逆，
$\mathscr D(z)=d\mathscr D(z)=0$ 当且仅当 $a(z)=g(z)=0$；
(9) 正好把后者识别为原 $F_2$ 的整纤维消失。证毕。

对 R141 的合法 $p$ 与带原 CM 标签的底点 $z$，
$n=a_\ell g_p$ 的简单零已付清，所以 (16) 直接适用。
这把尚未解决的实际有限行非零变为：
$$
              \mathscr D(z)\ne0\quad\hbox{或}\quad
                          d\mathscr D(z)\ne0.
\tag{18}
$$
没有使用尚未证明的平方自由性。

## 5. 失败时的精确阶数与算术 Frobenius

仍设 $v_z(n)=1$。若 (16) 失败，即二阶行整纤维为零，
则 (8) 恰为 $(t)$，所以
$$
                        F_2\in tS\setminus t^2S,\qquad
                        A\in tS\setminus t^2S.
\tag{19}
$$
第二式由 (6) 中 $y$ 的系数 $-n$ 直接得到。
令
$n_1=n/t\bmod t\ne0$、$a_1=a/t\bmod t$、$g_1=g/t\bmod t$。
首个正规 jet 准确为
$$
 \frac A t=-n_1y+a_1,\qquad
 \frac{F_2}t=
       \frac{n_1}{2}y^2+\left(\frac{n_1}{2}-a_1\right)y+g_1
          \quad\bmod t.
\tag{20}
$$
因此在几何纤维的 $p$ 个分支中，$A$ 至多有一个分支的阶大于
$1$，$F_2$ 至多有两个。特别至少 $p-2$ 个分支的 $F_2$ 零阶
准确为 $1$。

若该实际算术纤维为非平凡的次数 $p$ 扩域，
即其 Frobenius 为 $\tau^h$、$h\ne0$，则剩余 $y$ 的最小多项式
次数为 $p$。(20) 的非零一次、二次多项式都不可能在它处为零。
因此此时每个算术分支上 $A,F_2$ 的阶均准确为 $1$，
而且
$$
                       v_z\bigl(N_{Y/Z}(F_2)\bigr)=p.
\tag{21}
$$
当原 $p$ 位完全分裂时，使用整个置换纤维和 (9)、(20)，
不能以一个完成中的平凡 Galois 作用代替全部 $p$ 个分量。
上述所有 $\tau$ 等式是 deck 等式；仅在原带标记 CM 纤维上，
才按实际 Artin 元识别其算术 Frobenius。

非 CM 情形的 $W=A\,dF_2-F_2\,dA$ 一般不下降。准确有
$$
                    \Delta W=F_2\,dn-n\,dF_2.
\tag{22}
$$
如果整纤维 $A,F_2$ 都为零，则 $W$ 在该纤维也必为零，
实际至少有 (19) 所给的二阶公共因子。
所以不能先从 $dn(z)\ne0$ 宣称 $W(z)\ne0$，再以此排除失败。

## 6. 原 $Q$ 的单位比较及未付的特殊输入

全部判据仍使用原 Heegner $Q$，未更换迹或挪动 CM 点。
在兼容的 Manin 微分规范下，R135 给 $E_{17}$：
$$
            B|_{\rm CM}=-\bar a_p\,s\,\bar z_Q,
                    \qquad z_Q=\log_0(Q)/p,
\tag{23}
$$
其中 $s$ 是实际 $p$-Artin 元。它是群环单位。
对 $E_{389}$，R134 的实际去 $p$ Coleman 公式逐字给类数 $1$ 的
完整迹
$$
       B|_{\rm CM}
          =\overline{(s^2-a_ps+p)z_Q}
          =s(s-\bar a_p)\bar z_Q.
\tag{24}
$$
R139 的 $a_p\not\equiv0,\pm1$ 保证其 augmentation
$1-\bar a_p$ 为单位。原 $Q$ 非 formal 时，
用同一实际 Frobenius 群环单位使它 formal，或用合法的 $p$-单位
倍定义 $\log_0(Q)/p$；R139 的整格比较保证两种表述相同。
对 (23)、(24) 应用 $D_2$ 不改变该单位可逆性。

因此在任一个合法 $p$ 位上，原 $F_2$ 的纤维值非零就给
R130、R139 的实际半局部证书非零，并推出
$\Sha(E/\mathbb Q)[p^\infty]=0$。
在全部 $p$ 位上该有限证书为零，仅说明这项充分检验没有成功；
本篇不把它反向升级为 $\Sha$ 无限或全局点已被 $\delta^2$ 整除。

R141 的一阶源非零已经转化为 (16)–(20) 的严格约束。
下一项需要原模形式或原 CM 同源轨道的特殊输入，证明实际
$\mathscr D$ 在指定点不是二重零。一般 étale 覆盖、总迹简单零、
以及原 Hecke 行作为函数非零，都没有独立支付这条指定点条件。

## 来源与证明范围

- R135 的原 companion、完整类数 $2$ 迹及群环单位；其原始来源为
  A. Buium、B. Poonen，*Independence of points on elliptic curves
  arising from special points on modular and Shimura curves, II:
  local results*，Compositio Math. **145** (2009), 566–602，
  [作者全文](https://math.mit.edu/~poonen/papers/local.pdf)，
  Theorem 3.17、Corollary 3.19。
- [R137 的实际 Hecke 行](2026-11-12-actual-hecke-row-and-fourier-independence.md)
  与[环类覆盖](2026-11-12-torus-cover-and-actual-cm-trace-row.md)；
  好约化和连通模型的原始来源为 B. Cais、B. Conrad，
  *Modular curves and Ramanujan's continued fraction*（2006 作者版），
  [Theorems 2.2–2.3](https://virtualmath1.stanford.edu/~conrad/papers/J5final.pdf)。
- R139 的非 CM 整范数一系统及有限二阶充分检验；
  [R141 的固定源简单零](2026-11-12-noncm-fixed-cm-source-simple-zero.md)
  给本篇 (16) 所需的真实 $v_z(n)=1$。
- (3)–(22) 的群环、整 AS 正规形、理想、判别式和零阶均在本文
  完整证明；不依赖一个额外的平方自由或特化非零定理。
