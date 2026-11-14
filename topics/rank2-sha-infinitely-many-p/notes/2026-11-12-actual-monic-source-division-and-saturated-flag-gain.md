# 原 monic 修正源的共同除法、真实前缀矩阵与累计旗标收益

日期：2026-11-12。**状态：以下精确源像、共同前缀公式、局部格指数及
全部实际 jump 的累计收益均已证明。** 累计式不要求商和余项分别处于
前缀核。当前可支付的收益仍低于 R159 所需的主阶，本文不将它称为
严格预算。

## 1. 只用原两条 theta 行的实际多项式

固定 R180 的惰性 $p=4r-1\ge7$、$p\ne11$，并置

$$
R=r(p-1),\qquad \varpi^R=p,\quad
\lambda=\varpi^r,\quad\gamma=\varpi^p,\quad
\Omega=p(r+2p).
\tag{1.1}
$$

源始终是

$$
E_D=\mathbb Z_p[\mathcal A,B]_{\le D},\qquad
\mathcal A=A_2,\qquad
\mathcal C=B-\mathcal A+22\mathcal A^2.
\tag{1.2}
$$

取 $1\le n\le p-1$，令

$$
J=(n+1)r-\left\lfloor nr/p\right\rfloor-1,
\qquad d=2p+J.
\tag{1.3}
$$

R180 构造了具体的整 $p$ 进系数多项式

$$
\mathcal P=\mathcal P_{p,n}
=\mathcal C^p+\sum_{i=0}^{p-1}c_i(\mathcal A)\mathcal C^i,
\qquad
c_i(\mathcal A)=\mathcal A^{2(p-i)}
                \sum_{j=0}^{J}w_{ij,n}\mathcal A^j,
\tag{1.4}
$$

其中 $w_{ij,n}\in\mathbb Z_p$，且

$$
\deg_{\mathcal A,B}\mathcal P\le d,\qquad
[B^p]\mathcal P=1,\qquad
\frac{\mathcal P(\gamma T)}{\lambda^p\gamma^{2p}}
                      \in p^n\mathcal O_{K'}[[T]].
\tag{1.5}
$$

最后的记号是在实际 $s=\gamma T$ 曲线上求值。
$\mathcal A/\gamma,B/\gamma$ 在该图上均整。
这些是逐 $p$ 的局部源与格；本文不声称 $w_{ij,n}$ 为有理数，
也不把 $\mathcal P_{p,n}$ 当成所有素数共同的全局多项式。

这里还保留一个实际低前缀。R180 的未准备多项式沿曲线的阶
至少为 $N_n+1$，其中 $N_n=(n+1)r-1$。
Weierstrass 单位不改变此阶。截掉 $\mathcal A$ 次数大于 $J$
的项，因 $\mathcal A,Z=O(s)$，只可能从 $J+1$ 阶改变；
$J\le N_n$。最后乘 $\mathcal A^{2p}$，得到

$$
\boxed{\quad
\operatorname{ord}_s\mathcal P(\mathcal A(s),B(s))\ge d+1.
\quad}
\tag{1.6}
$$

记 $\nu=d+1$。这是已知的消失阶下界，不是假定首系数为单位，
也不声称该阶一定准确等于 $\nu$。
输出 $s,w$ 及 R174 的 $v=V(w)$ 首项均为一，故准确前缀及其
第一个可能非零系数在这些参数中保持不变。

## 2. 完整 monic 除法：实际源像而非自由余式空间

先在 $\mathbb Z_p[\mathcal A,\mathcal C]$ 中工作，另用 $Z_0$
表示形式上的 $\mathcal P$ 值；它不是 R178 的除法坐标
$Z=\mathcal C/\mathcal A^2$。
monic 关系给出自由模分解

$$
\mathbb Z_p[\mathcal A,\mathcal C]
\simeq
\bigoplus_{i=0}^{p-1}\mathcal C^i
                     \mathbb Z_p[\mathcal A,Z_0],
\qquad Z_0\longmapsto\mathcal P.
\tag{2.1}
$$

存在性是按 $\mathcal C$ 次数的 monic 除法。
唯一性可直接看最高次数：若
$\sum_{i<p,q}f_{iq}(\mathcal A)\mathcal C^i\mathcal P^q=0$，
不同对 $(i,q)$ 的最高 $\mathcal C$ 次数 $i+pq$ 互不相同，
最大非零项不能消失。

这是整的双向 Gauss 等距：从原系数作除法不会引入分母，
反向代回 $Z_0=\mathcal P$ 亦整。两方向的算子范数均至多一，
故有限多项式的系数 $p$ 进最大范数准确相等。
原 $B$ 与 $\mathcal C$ 的互换
$B=\mathcal C+\mathcal A-22\mathcal A^2$ 也是整多项式自同构，
同样双向等距；它并不保持总次数。

给出无需选择商的共同矩阵。按基
$1,\mathcal C,\ldots,\mathcal C^{p-1}$，令 $M_{\mathcal C}$
为乘 $\mathcal C$ 的伴随矩阵：前 $p-1$ 列把基向下一位移动，
末列为

$$
(Z_0-c_0,-c_1,\ldots,-c_{p-1})^{\mathrm t}.
$$

置

$$
M_B=M_{\mathcal C}+(\mathcal A-22\mathcal A^2)I_p.
\tag{2.2}
$$

原单项式 $\mathcal A^aB^b$ 的准确余式向量为
$\mathcal A^aM_B^b e_0$。因此原次数 $D$ 的**真实像**是

$$
\boxed{\quad
\mathscr I_D=
\operatorname{span}_{\mathbb Z_p}
\{\mathcal A^aM_B^b e_0:a,b\ge0, a+b\le D\}.
\quad}
\tag{2.3}
$$

$E_D\to\mathscr I_D$ 是整等距同构。
该像在整个右侧多项式自由模中 $p$ 饱和：若 $pQ\in\mathscr I_D$，
整地代回得 $pP\in E_D$，故原多项式 $P$ 的高于 $D$ 次项为零，
且 $P\in E_D$；于是 $Q\in\mathscr I_D$。
这个论证不把 $\mathscr I_D$ 替换成更大的余式空间。

## 3. 真实次数成本与有限前缀矩阵

由 (1.4)，

$$
\deg_{\mathcal A}c_i\le2(p-i)+J\le (J+2)(p-i).
$$

取 $h=J+2$，给 $\mathcal A,\mathcal C,Z_0$ 的权分别为
$1,h,ph$。monic 约化不会增加该权；
$B=\mathcal C+\mathcal A-22\mathcal A^2$ 的权至多 $h$。
故 (2.3) 中每个出现的项都满足

$$
\boxed{\quad
\mathcal A^l\mathcal C^i Z_0^q:\qquad
0\le i<p,\quad l+hi+phq\le hD.
\quad}
\tag{3.1}
$$

这给出实际有限计算的环境，但不是原次数 $D$ 的免费不变性。
一般不能把 $h$ 换成 $d/p$：对 $i=p-1$，(1.4) 仅保证
$\deg c_{p-1}\le J+2$，与此处的 $h$ 正相配。
同时，(3.1) 仅是 $\mathscr I_D$ 的外部支撑界，不能删掉
(2.3) 的实际像条件。

令

$$
A(v)=\mathcal A(\gamma_v(v)),\quad
C(v)=\mathcal C(\gamma_v(v)),\quad
H(v)=\mathcal P(\gamma_v(v)).
$$

若原源的余式为
$\sum q_{i,l,q}\mathcal A^l\mathcal C^i Z_0^q$，其第 $k$ 行
准确为

$$
\boxed{\quad
r_k=
\sum_{i,l,q}q_{i,l,q}
\sum_{m=0}^k[v^m]H(v)^q\,
                [v^{k-m}]A(v)^lC(v)^i.
\quad}
\tag{3.2}
$$

同一系数向量必须同时满足 (3.2) 的全部 $0\le k'<k$ 零行。
这就是完整耦合的前缀；没有将 $q=0,1,\ldots$ 的各块分别置零。
因 (1.6)，$q\nu>k$ 的块在截至 $k$ 的矩阵中准确为零。
但投影掉这些块后，必须保留 **实际像的投影格与其商范数**；
该投影格不因 (2.3) 饱和就自动等于其所在环境的饱和格。

这里的 monic 余式次数可达 $q\le\lfloor D/p\rfloor$，
相应 $\mathcal A$ 次数成本已在 (3.1) 支付。
下一节为了仍留在原总次数 $D$ 内而使用的乘法格，范围是
$q\le\lfloor D/d\rfloor$。二者不同，不可交换。

## 4. 真正的除幂源格与准确指数

对 $0\le t\le\lfloor D/d\rfloor$，定义同一
$E_D\otimes\mathbb Q_p$ 中的局部格

$$
\mathscr L_t=E_D+
\sum_{q=1}^t p^{-(n+8)q}\mathcal P^qE_{D-qd}.
\tag{4.1}
$$

所有乘积确实在原总次数 $D$ 的有理空间中。
由于 $[B^p]\mathcal P=1$，乘 $\mathcal P^q$ 是整 Gauss 等距；
尤其对任意整数 $a\ge0$，
$\mathcal P^qQ\in p^aE_D\Longleftrightarrow
Q\in p^aE_{D-qd}$。可先模 $p$ 用多项式整环，随后逐次提升。
这里额外取八层，是下一节由同一个规范初始权支付的固定收益。

因此精确有

$$
\frac{p^{-(n+8)t}\mathcal P^tE_{D-td}}
 {p^{-(n+8)t}\mathcal P^tE_{D-td}\cap\mathscr L_{t-1}}
\simeq E_{D-td}/p^{n+8}E_{D-td}.
\tag{4.2}
$$

证明必要方向时，乘 $p^{(n+8)t}$ 后
$p^{(n+8)t}\mathscr L_{t-1}\subset p^{n+8}E_D$，于是上述等距迫使
$Q\in p^{n+8}E_{D-td}$。反过来 $Q=p^{n+8}Q_1$ 时，把一个
$\mathcal P$ 乘入 $Q_1$，准确放回 $\mathscr L_{t-1}$。
这里没有要求这些项分别有任何前缀消失。
由此

$$
\boxed{\quad
I_t:=\log_p[\mathscr L_t:E_D]
 =(n+8)\sum_{q=1}^t\binom{D-qd+2}{2}.
\quad}
\tag{4.3}
$$

## 5. 同一输出格上的全阶范数

以 $v=\gamma y$ 缩放时，R177 的整参数互换保留 (1.5)。
对任意整系数 $Q\in E_{D-qd}$，有

$$
\left(p^{-(n+8)q}\mathcal P^qQ\right)(\gamma y)
            \in\varpi^{q(\Omega-8R)}\mathcal O'[[y]].
\tag{5.1}
$$

所以每个实际行满足

$$
v_p\left(r_k(p^{-(n+8)q}\mathcal P^qQ)\right)
                 \ge\left\lceil\frac{q\Omega-pk}{R}\right\rceil-8q.
\tag{5.2}
$$

若 $Q$ 原齐次次数为 $m$，右边还可加上 $pm/R$ 后再取上整，
因为 $A(v)/\gamma,B(v)/\gamma$ 都整。
这些是完整输出系数的界；不要求 $Q$ 或 $\mathcal P^qQ$ 单独
处于所讨论的高前缀。

取 R173/R179 的准确整基线

$$
e_p(k)=0\ (k<r),\qquad
e_p(k)=N+\left\lfloor\frac{N-1}{p-1}\right\rfloor,
\quad N=\lfloor k/r\rfloor\ge1.
\tag{5.3}
$$

原 $E_D$ 的全部系数在 $v$ 参数下满足 $v_p(r_k)\ge-e_p(k)$。
另一方面，对所有 $k\ge0$ 有
$0\le\delta_k:=pk/R-e_p(k)<2$，而
$\Omega/R=9+(p+9)/(p^2-1)>9$。
对 $q\ge1$，
$q\Omega/R-\delta_k>9q-2\ge8q-1$，故

$$
\left\lceil q\Omega/R-\delta_k\right\rceil\ge8q.
$$

因此 (5.2) 对 $q\ge1$ 也不弱于同一基线。
结合 (4.1) 的整数生成元，得到

$$
\boxed{\quad
\|r_k\|_{\mathscr L_t\cap\ker(r_{<k})}\le p^{e_p(k)}.
\quad}
\tag{5.4}
$$

范数的单位球准确是该局部格与同一理性前缀的交。
对单个前缀，这尚未声称原 $E_D$ 必须包含于
$p^{n+8}\mathscr L_t$；真正可无条件累计的结论如下。

## 6. 全部饱和 jump 的准确累计收益

令 $M=\binom{D+2}{2}$。原 $\mathcal A,B$ 的代数独立性使其
各单项式的有限有理 jet 矩阵有满秩；同一非零有理子式在
$\mathbb Q_p$ 中仍非零。因此原有理源的完整准确零前缀有
$M$ 个非零 jump，记为

$$
k_0<k_1<\cdots<k_{M-1}.
$$

这组 jump 只依赖有理源空间，$E_D$ 与 $\mathscr L_t$ 完全相同。
对任一格 $L$ 记
$L^{(i)}=L\cap\ker(r_{<k_i})$。各相邻商是饱和的自由秩一
$\mathbb Z_p$ 模。若该商的行像为 $p^{v_i(L)}\mathbb Z_p$，
准确的局部 jet 范数便是 $p^{-v_i(L)}$。

选分别适配同一旗标的格基。非零 jet 子矩阵三角，其行列式
赋值为 $\sum_i v_i(L)$。而
$[\mathscr L_t:E_D]=p^{I_t}$ 准确说明两格基的行列式相差
$p^{-I_t}$ 乘一个单位。因此

$$
\boxed{\quad
\sum_i\log\|r_{k_i}\|_{E_D}
=\sum_i\log\|r_{k_i}\|_{\mathscr L_t}-I_t\log p.
\quad}
\tag{6.1}
$$

所有范数均取对应的真实前缀商范数。
这一步保留全部商、余项及混合列的抵消，不需要它们各自落在
前缀核。由 (5.4)，得到无条件的全 jump 上界

$$
\boxed{\quad
\sum_i\log\|r_{k_i}\|_{E_D}
\le\left\{\sum_i e_p(k_i)
      -(n+8)\sum_{q=1}^{t}\binom{D-qd+2}{2}\right\}\log p.
\quad}
\tag{6.2}
$$

收益在实际深处发生，而非人为提前分配。
在从 $\mathscr L_{q-1}$ 加到 $\mathscr L_q$ 时，新生成元
的消失阶至少为 $q\nu$；所以 $k_i<q\nu$ 的真实行像理想
完全不变。该步的全部指数
$(n+8)\binom{D-qd+2}{2}$ 由其后的 jump 商共同承担。
这没有给每一晚行分配相同增益，也没有把单个 primitive
多项式的 Gauss 改良直接当成所有行的改良。

原输出参数 $s\to w\to v$ 的首项为一，故对这些准确前缀
每个 $r_{k_i}$ 本身的值不变，(6.1)–(6.2) 无额外高阶换参
损失。若只以一般固定单位作首项，亦只乘单位，不改变本地范数。

## 7. 当前累计收益的规模与未付的严格门

取最大的 $t=\lfloor D/d\rfloor$。因被求和函数递减，

$$
\sum_{q=1}^t\binom{D-qd+2}{2}
\le\frac1d\int_0^D\frac{(D-x+1)(D-x+2)}2\,dx
=\frac1d\left(\frac{D^3}{6}+\frac{3D^2}{4}+D\right).
\tag{7.1}
$$

由 (1.3) 有 $d+1=\lceil(\Omega+nR)/p\rceil$。
又 $n+8<(\Omega+nR)/R-1$，且 $p/R<1$，故
$n+8<pd/R$。从而

$$
I_t\le\frac{p}{R}
       \left(\frac{D^3}{6}+\frac{3D^2}{4}+D\right)
       =O(D^3/p).
\tag{7.2}
$$

有非零修正块必须 $d\le D$，特别 $p\le D/2$。
用基本素数和 $\sum_{p\le D}\log p/p=O(\log D)$，这些已构造
指数的总规模至多 $O(D^3\log D)$。
原 $M\asymp D^2$ 个 jump 有 $\sum k_i\gg D^4$，所以这仍是
当前全 jump 主尺度中的低阶修正，不能单独改变 R159 的严格门。
这里给的是规模上界，不把它误写成每个素数都取得同一渐近主项。

这个账本也适用于 R183 已构造的任意精度族。
对该族令 $\Omega_q$ 为规范初始权、$n$ 为额外精度、$d$ 为
已付原次数。其准确关系为
$d+1=\lceil(\Omega_q+nR)/p\rceil$。
安全的整除层数可取
$a=n+\lfloor\Omega_q/R\rfloor-1$；同一上整估计保留基线，且

$$
a\le\frac{\Omega_q+nR}{R}-1<\frac{pd}{R}.
\tag{7.3}
$$

若把这些关系及乘积均按各自已经支付的次数相加计费，并要求
总次数至多 $D$，所生成的共同格包含于
$p^{-\lfloor pD/R\rfloor}E_D$。
因此即使合并全部这样的族，其指数也至多
$M\lfloor pD/R\rfloor=O(D^3/p)$。
该界明确限于此已付次数账本；不排除实际高次项额外相消而
降低真实次数，也不排除完整中央条件提供新的精度或新格。

真正的正面接合是 (6.1)：只要以后能在同一实际源中构造更大的
累计格指数，并维持 (5.4) 或更强的准确输出界，就可以直接进入
完整斜率和，无须先强迫每一商、余项分别消失。
当前 R180 的精度与次数近似成正比；原两条完整中央条件是否能
给超出此比率的真实源与指数，尚未支付。

## 依赖

- [R180：原多层 monic 源与完整系数支撑](2026-11-12-original-theta-multiple-precision-source-polynomials.md)。
- [R183：任意精度原源及准确次数](../results/R183-arbitrary-precision-original-theta-source.md)。
- [R178：原坐标、清分母与一次精度](2026-11-12-original-theta-as-source-and-integral-correction.md)。
- [R177：canonical 缩放及整输出换参](2026-11-12-full-depth-canonical-as-reduction-and-source-initial-form.md)。
- [R179：原同源的全深度行与准确基线](2026-11-12-full-depth-common-jet-core-and-as-defect.md)。
- [R176：保留混合块的除幂格](2026-11-12-actual-divided-source-lattices-and-prefix-saturation.md)。
- [R159：完整 jump 的次数敏感斜率标准](2026-11-12-degree-sensitive-jets-and-direct-slope-boundary.md)。
