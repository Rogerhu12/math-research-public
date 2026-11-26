# R1068：原辅助 2、3 点集的完整 necklace 输入与精确点数

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明。** 对全部 $p>37$，R1067 已付款的原好模型
$X=X_{\rm ns}^+(p)$ 在 $2,3$ 的全部点，可由下面列出的五条
$\mathbf F_2$ 椭圆曲线、八条 $\mathbf F_3$ 椭圆曲线的真实
Frobenius-stable necklaces，经全部几何 isomorphisms 取商完整取得。
这包含特殊 $j$ 的所有 twists，没有把一个选定模型上的固定
necklaces 误当全部 coarse 有理点。

其点数准确为
$$
\boxed{
\#X(\mathbf F_2)=
\frac{p+4-2\left(\frac{-2}{p}\right)
              -\left(\frac{-1}{p}\right)
              -2\left(\frac{-7}{p}\right)}4,
}
\tag{1068.1}
$$
$$
\boxed{
\#X(\mathbf F_3)=
\frac{2p+9-5\left(\frac{-3}{p}\right)
               -3\left(\frac{-11}{p}\right)
               -3\left(\frac{-8}{p}\right)}6.
}
\tag{1068.2}
$$
这里 Legendre symbols 的分子均不被 $p>37$ 整除。
它们同时给 R1067 同一个全局候选在这两个辅助素处的实际完整点像预算，
以及逐点评价所需的准确原 level 数据。
本文没有把点数或一个 Frobenius 相似类当成已算出的 Kummer 标签，
更没有据此断言辅助共同像排除。全部为纸面证明。

## 1. 使用原 coarse 模型及真实 level 对象

R1067 给原 $X$ 在每个 $\ell\ne p$ 的 smooth proper 模型，
并保全部有限 étale cusps。原 $m=(p-1)/2$ 个 cusps 形成
$\operatorname{Gal}(\mathbf Q(\zeta_p)^+/\mathbf Q)$ 的简单传递轨道。
故
$$
\#\Sigma(\mathbf F_\ell)=
\begin{cases}
m,&\ell\equiv\pm1\pmod p,\\
0,&\text{否则}.
\end{cases}
\tag{1068.3}
$$
特别 $p>37$ 时 $\Sigma(\mathbf F_2)=\Sigma(\mathbf F_3)=\varnothing$。
下面的非 cusp 计数因此就是 (1068.1)–(1068.2) 的全部点数。

对 $\overline{\mathbf F}_\ell$ 上的椭圆曲线 $E$，
令 $\Omega_p(E)$ 为 $E[p]$ 上的无向 nonsplit necklaces。
Rebolledo–Wuthrich [RW, §2.1–2.3, Corollary 3, Proposition 4] 给
$$
\Omega_p(E)\simeq
\operatorname{PGL}(E[p])/N_{\rm ns},\qquad
|\Omega_p(E)|=\frac{p(p-1)}2.
\tag{1068.4}
$$
也可直接用非有理共轭线对表示：
$$
\Omega_p(E)\simeq
\bigl(\mathbf P^1(E[p]\otimes\mathbf F_{p^2})
             \setminus\mathbf P^1(E[p])\bigr)/
              \{z\sim z^p\}.
\tag{1068.5}
$$
一对共轭线的稳定子正是 nonsplit Cartan 的 normalizer；
这给 (1068.5) 与 (1068.4) 同一个实际群作用。

原 $X$ 的几何非 cusp 点是 $(E,\mathcal C)$ 的几何 isomorphism classes，
其中 $\mathcal C\in\Omega_p(E)$。
它的 $\mathbf F_\ell$ 点是这些 classes 的 Frobenius 固定点。
不得要求 necklace 的每颗 pearl 分别在 $\mathbf F_\ell$ 上定义；
也不得在有额外 automorphisms 时把 coarse 固定 class
自动当作某个预先选定 $E/\mathbf F_\ell$ 的固定 necklace。
[RW, §3.3] 明确保留这一区别，下一节完整支付它。

## 2. 特殊 j 的 twisted Burnside 及全部 twists

固定 $j\in\mathbf F_\ell$，取一个 $E/\mathbf F_\ell$，令
$A=\operatorname{Aut}_{\overline{\mathbf F}_\ell}(E)$，
$\pi$ 为实际 arithmetic Frobenius 在 $E[p]$ 上的作用。
$A$ 通过有限群作用于 $\Omega=\Omega_p(E)$，且 $\pi$ 归一化此作用。
允许 $A$ 的中心 $\{\pm1\}$ 在 $\Omega$ 上平凡。

对任意 $\pi$-稳定的 $A$-轨道 $O$，计数
$(a,x)\in A\times O$ 满足 $a\pi x=x$：
每个 $x$ 恰有 $|\operatorname{Stab}_A(x)|$ 个 $a$，
所以总数为 $|O|\cdot|\operatorname{Stab}_A(x)|=|A|$。
非稳定轨道贡献零。于是
$$
\#(A\backslash\Omega)^\pi
 =\frac1{|A|}\sum_{a\in A}\#\Omega^{a\pi}.
\tag{1068.6}
$$
本式不要求 $A$ 在 $\Omega$ 上自由，也不要求 $\ell\nmid|A|$。

所有 $a\in A$ 都给有限域上的一个 twist：
Frobenius 对有限 $A$ 的作用有有限阶，
因此 $a\operatorname{Frob}$ 在相应有限 semidirect product 中有限阶，
所定义 cocycle 是连续的。按 twisted conjugacy 取商，
得到全部同 $j$ 的 $\mathbf F_\ell$-isomorphism classes $E'$。
一个这样的类有 $|A|/|\operatorname{Aut}_{\mathbf F_\ell}(E')|$ 个代表 $a$。
因此 (1068.6) 等价于准确的质量公式
$$
\#X_j(\mathbf F_\ell)=
\sum_{\substack{E'/\mathbf F_\ell\\j(E')=j}}\
 \frac{\#\Omega_p(E')^{\pi_{E'}}}
      {|\operatorname{Aut}_{\mathbf F_\ell}(E')|}.
\tag{1068.7}
$$
$\{\pm1\}$ 的 kernel 已同时进入分母和重复的 twists，
不再额外乘二或除二。

这还给完整点集的构造：取所有同 $j$ twists 的
$\pi_{E'}$-固定 necklaces，再按全部几何 isomorphisms 识别。
任一 coarse Frobenius 固定轨道可选 $a$ 使 $a\pi$ 固定其中一个代表，
相应 twist 上它就是实际固定 necklace；故这个构造确实满射。
最终必须取上述几何商，不能把重复 twist 代表算成不同点。

## 3. 实际 Frobenius 的完整固定 necklace 表

令 $M\in\operatorname{GL}_2(\mathbf F_p)$。
从 (1068.5) 或 dihedral normalizer 直接得到：

| $M$ 的 projective 类型 | $\#\Omega_p^M$ |
| --- | ---: |
| scalar | $p(p-1)/2$ |
| 非 scalar unipotent | $0$ |
| split semisimple，projective order 不为 $2$ | $0$ |
| nonsplit semisimple，projective order 不为 $2$ | $1$ |
| split involution | $(p-1)/2$ |
| nonsplit involution | $(p+3)/2$ |

非 involution 的证明如下。
projective normalizer 的 Cartan 外元素全为 order $2$；
非 scalar unipotent 的 order 为 $p$，不整除 normalizer 的阶 $2(p+1)$。
其余非 involution 若固定 necklace，必须位于该 necklace 的 Cartan。
一个 nonsplit semisimple 元素的两个共轭 eigenlines 确定唯一这种 Cartan；
split 元素没有这种共轭线对。

对 involution 可给原点的显式名单。
若 $M$ 的 trace 为零、determinant 为 $\ell\bmod p$，
取实际 $E[p]$ 的基使
$$
M=\begin{pmatrix}0&-\ell\\1&0\end{pmatrix},\qquad d=-\ell.
\tag{1068.8}
$$
在 (1068.5) 的 affine 坐标中，它作用为 $z\mapsto d/z$。
固定共轭线对有两类：

- 交换两线：$z^p=d/z$，即
  $z^{p+1}=d$，取 $z\in\mathbf F_{p^2}\setminus\mathbf F_p$，
  再按 $z\sim z^p$ 取商。
- 分别固定两线：仅当 $d$ nonsquare 时有唯一 eigenline 对
  $\{\sqrt d,-\sqrt d\}$。

norm 方程总有 $p+1$ 个非零解。
$d$ square 时其中两个在 $\mathbf F_p$，故交换类为 $(p-1)/2$；
$d$ nonsquare 时全不在 $\mathbf F_p$，故交换类为 $(p+1)/2$，
再加一对 eigenlines。因而对 trace-zero Frobenius
$$
f_0(\ell,p):=\#\Omega_p^\pi
 =\frac{p+1}{2}-\left(\frac{-\ell}{p}\right).
\tag{1068.9}
$$
这既证明表中最后两行，又保留了每条真实 necklace 的坐标，
并非只给一个总数。

### 3.1 范围 l 小于 p²/4 时严排 scalar

设 $\alpha=a\pi$ 是 §2 中一个实际 twist 的 Frobenius，
$\deg\alpha=\ell$、$\operatorname{Tr}\alpha=t$，
$|t|\le2\sqrt\ell$。假设
$$
\ell<p^2/4.
\tag{1068.10}
$$
若 $\alpha$ 在 $E[p]$ 上为 scalar $b$，
取整数代表 $|b|\le(p-1)/2$。
$\alpha-[b]$ 杀掉整个 $E[p]$，故经过 separable quotient
$[p]:E\to E$ 因子化，其 degree 是 $p^2$ 的倍数。
但
$$
0\le\deg(\alpha-[b])
 =\ell-tb+b^2
 \le(\sqrt\ell+|b|)^2<p^2.
\tag{1068.11}
$$
只能为零，遂 $\alpha=[b]$，这与 $\deg\alpha=\ell$ 为素数矛盾。
因此没有 scalar。

若 discriminant $t^2-4\ell$ 模 $p$ 为零，
这时实际矩阵是非 scalar unipotent，固定数为零，
不能把它错误计成一个 Cartan。
又因为 $|t|<p$，trace 模 $p$ 为零当且仅当整数 $t=0$。
故在 (1068.10) 下
$$
\#\Omega_p^{\pi_E}=
\begin{cases}
f_0(\ell,p),&t=0,\\
1,&t\ne0,\ \left(\frac{t^2-4\ell}{p}\right)=-1,\\
0,&t\ne0,\ \left(\frac{t^2-4\ell}{p}\right)\in\{0,1\}.
\end{cases}
\tag{1068.12}
$$
标量排除使用实际 endomorphism 因子化，
不只是由 discriminant 非零作猜测。

## 4. F2 上全部模型、automorphisms 与实际点数

普通 $j=1$ 的两个 twists 是
$$
E_{1,A}: y^2+xy=x^3+A x^2+1,\qquad A=0,1.
$$
直接对 $x=0,1$ 计数得 traces $-1,+1$；
其 Frobenius discriminant 均为 $-7$，
且每个 $\mathbf F_2$-automorphism group 的阶为 $2$。

为核没有遗漏 supersingular twists，
在 $j=0$ 的一般方程
$$
y^2+y=x^3+a_2x^2+a_4x+a_6
$$
中作 $x=X+r,\ y=Y+sX+t$。
在 $\mathbf F_2$ 上，新的 $x^2,x$ 系数分别为
$a_2+r+s,\ a_4+r+s$，所以 $A=a_2+a_4$ 不变。
取 $s=a_2+r$ 可令新 $x^2$ 系数为零；
新常数为 $a_6+r(1+A)$。
因此恰有下面三个 classes：

| 原 $\mathbf F_2$ 模型 | trace | $|\operatorname{Aut}_{\mathbf F_2}|$ |
| --- | ---: | ---: |
| $y^2+y=x^3$ | $0$ | $2$ |
| $y^2+y=x^3+x$ | $-2$ | $4$ |
| $y^2+y=x^3+x+1$ | $2$ | $4$ |

automorphism 数也由同一变换取得：
$A=0$ 时保常数迫 $r=s=0$，$t$ 两种；
$A=1$ 时 $s=r$、$r,t$ 各两种。
$\mathbf F_2^\times$ 只有一个元素，所以没有遗漏额外 scaling。
普通两 twists 亦由一般 Weierstrass 变换归约为上述 $E_{1,A}$；
其非零 $a_6$ 必为一。

对 $t=\pm2$，discriminant 为 $-4$，固定数为
$\bigl(1-\left(\frac{-1}{p}\right)\bigr)/2$。
将全部五个模型代入 (1068.7)：
$$
\#X(\mathbf F_2)=
\frac12 f_0(2,p)
+\frac12\cdot\frac{1-\left(\frac{-1}{p}\right)}2
+\frac{1-\left(\frac{-7}{p}\right)}2.
\tag{1068.13}
$$
按 (1068.9) 展开正是 (1068.1)。
没有 cusp 项，因为 (1068.3) 在 $2$ 处为零。

## 5. F3 上全部模型、automorphisms 与实际点数

在 characteristic $3$ 先完成平方。
supersingular 的 $j=0$ 方程恰可写成
$$
y^2=x^3+a x+b,\qquad a\in\{1,-1\},\quad b\in\mathbf F_3.
$$
所有 $\mathbf F_3$ scaling 的 $u=\pm1$ 都不改变 $a,b$。
$x=X+r$ 把 $b$ 变成 $b+(1+a)r$。
所以 $a=1$ 时三个 $b$ 归并为一个 class；
$a=-1$ 时三个 $b$ 保留。全部四个 classes 为：

| 原 $\mathbf F_3$ 模型 | trace | $|\operatorname{Aut}_{\mathbf F_3}|$ |
| --- | ---: | ---: |
| $y^2=x^3+x$ | $0$ | $2$ |
| $y^2=x^3-x$ | $0$ | $6$ |
| $y^2=x^3-x+1$ | $-3$ | $6$ |
| $y^2=x^3-x-1$ | $3$ | $6$ |

点数直接用 $x^3=x$ 和 $\mathbf F_3$ 的平方 $0,1$ 得到。
$a=1$ 的 automorphism 迫 $r=0$，保 $y$ 的两个 signs；
$a=-1$ 则任意 $r\in\mathbf F_3$ 加两个 signs，
给上表的 $2,6$。

普通 curves 有非零 $x^2$ 系数，平移 $x$ 可消 $x$ 项，
所以全部四个 models 是
$$
y^2=x^3+A x^2+B,\qquad A,B\in\mathbf F_3^\times.
\tag{1068.14}
$$
$(A,B)=(1,2),(2,1)$ 给 $j=1$、traces $\pm1$、discriminant $-11$；
$(A,B)=(1,1),(2,2)$ 给 $j=2$、traces $\pm2$、discriminant $-8$。
每个 ordinary automorphism group 阶为二。
上述归约也说明没有其它 $\mathbf F_3$ classes。

$t=\pm3$ 的 discriminant 为 $-3$。
于是 (1068.7) 给
$$
\#X(\mathbf F_3)=
\frac23 f_0(3,p)
+\frac13\cdot\frac{1-\left(\frac{-3}{p}\right)}2
+\frac{1-\left(\frac{-11}{p}\right)}2
+\frac{1-\left(\frac{-8}{p}\right)}2.
\tag{1068.15}
$$
代入 (1068.9) 即得 (1068.2)，同样没有 cusp 项。

## 6. 从完整点集到原同标签辅助读数

这里保 R1067 的原 $V$、任意实际 $W\subset V$、
$F=\mathbf Q(\zeta_p)^+$ 及规范 $f_u=u^m/A(u)$。
给定 $p$，§4–5、(1068.5)、(1068.8)–(1068.12) 提供如下完整有限输入：

1. 在上表每个 $E/\mathbf F_\ell$ 上取实际 $E[p]$ 和实际 Frobenius。
2. trace-zero models 使用 (1068.8) 的 norm 方程共轭线对，
   加上该式规定的可能 eigenline 对；其它 models 只在 discriminant
   nonsquare 时取其唯一共轭 eigenline 对。
3. 对全部模型、全部固定 necklaces 按全部几何 isomorphisms 取商。
   §2 已证明所得集合准确为 $X(\mathbf F_\ell)$。
4. 对每个原几何商点 $y$，逐个 $\mathfrak q\mid\ell$ 使用
   R1062/R1067 的同一个 $f_u$ 作 residue evaluation，
   得完整
   $$
   \delta_\ell(y)\in H^1(\mathbf F_\ell,H_W).
   \tag{1068.16}
   $$

最后一步不能只保 Frobenius 的 trace、discriminant 或相似类。
若用 full-level 基评价原 Siegel products，必须同时记录
$(P,Q)$ 的 Weil pairing，并把系数 $\zeta_p$ 的剩余 embedding
与该 pairing 配准。将矩阵共轭到 (1068.8) 的任意
$\operatorname{GL}_2(\mathbf F_p)$ 换基可能改变 determinant；
相应 cyclotomic embedding 必须一起运输。
原 modular functions 在 normalizer 与几何 isomorphism 下的下降
保证如此取得的数值不依赖代表，但没有授权删掉这些尺度数据。

因此 (1068.1)–(1068.2) 给实际标签像的准确上界
$$
|\delta_2(X(\mathbf F_2))|\le \#X(\mathbf F_2)\le\frac{p+9}{4},
\qquad
|\delta_3(X(\mathbf F_3))|\le \#X(\mathbf F_3)\le\frac{p+10}{3}.
\tag{1068.17}
$$
右端可取整数 floor；本文保精确 (1068.1)–(1068.2) 时不需放宽。
这些是同一个原点的完整向量数目，不能把每个角色的可取值任意作直积。

若 R1067 的唯一全局候选为 $\phi$，其真实必要条件是
$$
\operatorname{loc}_2\phi\in\delta_2(X(\mathbf F_2)),
\qquad
\operatorname{loc}_3\phi\in\delta_3(X(\mathbf F_3)).
\tag{1068.18}
$$
R1067 的 exact visibility 仍必须先应用：
对 $\chi_j=\omega^{-2j}$，$\ell$ 只读到
$\ell^{2j+1}=1\bmod p$ 的角色；其余角色在该有限域 $H^1$ 中为零。
特别当 $\operatorname{ord}_p(\ell)$ 为偶数时，
该素对全部原 cuspidal $p$-torsion 没有额外标签筛力。
不能因为 (1068.17) 较小便声称 (1068.18) 已经排除一个候选。

本文给出了 (1068.18) 左右两边的同一原来源和完整有限点输入；
实际 circular-unit residues 与每条 necklace 的 $f_u$ 值，
以及适当变化辅助素的共同像，仍须进一步支付。

## 来源与核读范围

- M. Rebolledo and C. Wuthrich,
  *A moduli interpretation for the non-split Cartan modular curve*,
  Glasgow Math. J. **60** (2018), 411–434,
  DOI [10.1017/S0017089517000180](https://doi.org/10.1017/S0017089517000180)；
  [作者全文](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/xnonsplit.pdf)。
  实读 §2.1–2.3、Corollary 3、Proposition 4、§3.3 及 Proposition 7 后的
  normalizer 说明；只消费原 moduli/Galois 解释。
  全 fixed-count、twisted Burnside、scalar 排除及 characteristic $2,3$
  模型分类和点数均在本篇自证。
- R1067：所有 $\ell\ne p$ 的原 coarse 好模型、有限 étale cusp boundary、
  规范标签的 $p$-only 支撑及真实辅助 étale twists。
- R1062/R1064：原函数、Galois 角色、leading-coefficient 归一化及
  finite-field 标签。这里不改其函数源或以 Frobenius 相似类替代函数值。

root 独立纸核 fixed-necklace 两种 involution 数、twisted Burnside 与
两个小特征质量公式；global_route 逐个付清全部 Weierstrass classes、
实际 Frobenius 与 normalizer-level 来源。无数学程序执行。
