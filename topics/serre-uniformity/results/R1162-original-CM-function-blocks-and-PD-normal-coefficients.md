# R1162 — 原 CM 形式函数的有限 e-block 与精确 PD 法向系数

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126。

**状态：已证明的整系数算法。** 本文把已给定的原整形式函数、
或已在整标架中写出的形式矩阵，转换成真实扭点 PD 环的有限法向输入。
每个所需系数的指标、精度和阶乘均明确给出。
结合 R1155 §16 时，只对**已经识别到同一强可除格**的函数坐标
给出 Fontaine–Laffaille 读取式；没有将任意 rational raw
dilogarithm 表达先当作该坐标，也没有报告尚未算出的中央 $F_0$。

## 1. 保持原坐标、原标记和两种截断

沿用 [R1155 §16](R1155-original-primitive-dilogarithmic-Frobenius-readout.md)
所消费的 R712 §2、R978 的严格 CM 坐标。令
$$
p>37,\qquad q=p^2,\qquad e=q-1,\qquad
\mathcal O=\mathcal O_F,\qquad \mathcal R=\mathcal O[[z]],
$$
其中 $F/\mathbb Q_p$ 未分歧并包含原常数及 $\mu_e$。
原 Gaussian/cubic good supersingular reference 上有
$$
[-p](z)=-pz+z^q,\qquad [a](z)=az\quad(a\in\mu_e).
$$
原非零 $p$-torsion 坐标满足 $\varpi^e=p$。
不在这里改变 differential、CM 标记或 Miller 根尺度。

置
$$
g=z^e-p,\qquad
S=\bigl(\mathcal O[z,\gamma_r(g):r\ge0]\bigr)^\wedge_p,
\qquad \gamma_r(g)=g^r/r!,
\tag{1162.1}
$$
并保持
$$
\psi|_{\mathcal O}=\sigma,\quad\psi(z)=z^p,\qquad
\operatorname{ev}(z)=\varpi,\quad
\operatorname{ev}(\gamma_r(g))=0\quad(r>0).
$$
$\sigma$ 是原未分歧 $p$-Frobenius。
这里的 $z$ 是整 Lubin–Tate 坐标，不是完整 elliptic logarithm。

R1147 §20 的 degree twelve jet 是 **coefficient distribution**
的 augmentation jet。本篇的指标 $j+ke$ 则是实际函数 $f(z)$
的次数。两者不同；尤其不能因前者只需十二阶，就删去后者的
$e+j,2e+j,\ldots$ 次项。

## 2. 实际 tame projector 与全部 e-block

给定
$$
f(z)=\sum_{n\ge0}c_nz^n\in\mathcal R,
$$
对 $0\le j<e$ 定义
$$
\mathcal P_jf
=\frac1e\sum_{a\in\mu_e}a^{-j}f(az).
\tag{1162.2}
$$
因为 $e$ 为 $p$-单位，这是原整环上的真实 projector。
原 Teichmüller 字符的正交性给
$$
\boxed{\quad
\mathcal P_jf=z^jF_j(z^e),\qquad
F_j(T)=\sum_{k\ge0}c_{j+ke}T^k\in\mathcal O[[T]],
\qquad f=\sum_{j=0}^{e-1}\mathcal P_jf .
\quad}
\tag{1162.3}
$$
这是整等式，不仅是模 $p$ 的同余。

若实际有限求和中的系数是 $a^w$，它选的是
$j\equiv-w\pmod e$；若还有原 coefficient tensor 的作用，
必须连同该作用使用同一个 projector。
本式不通过一个未校准的“权”字样，猜测 $z_{12}$ 应属于哪个 $j$。

在原 torsion 点上，
$$
\boxed{\quad
\varpi^{-j}(\mathcal P_jf)(\varpi)
=F_j(p)=\sum_{k\ge0}p^k c_{j+ke}\in\mathcal O.
\quad}
\tag{1162.4}
$$
因此对任意整数 $h\ge0$，
$$
F_j(p)\equiv\sum_{k=0}^{h}p^kc_{j+ke}
\pmod {p^{h+1}}.
\tag{1162.5}
$$
这里每个 $c_{j+ke}$ 只需模 $p^{h-k+1}$。
所有 $k>h$ 的完整尾都在 $p^{h+1}\mathcal O$ 中，
并随 $k$ 趋向无穷而趋零。

若另已证明 $F_j(p)\in p^h\mathcal O$，可对整个
(1162.5) 的有限和除以 $p^h$ 后约模 $p$；
不可在未有逐项整性的情况下先逐个删项或逐个除 $p$。

## 3. 函数系数到真实 PD 法向系数的精确公式

R1155 (1155.98) 的原整基是
$z^j\gamma_r(g)$，$0\le j<e$。
本篇对一个已整 $f$ 明确给出其展开：
$$
\boxed{\quad
f(z)=\sum_{j=0}^{e-1}z^j\sum_{r\ge0}\gamma_r(g)m_{j,r},
\qquad
m_{j,r}=r!\sum_{k\ge r}
 \binom{k}{r}p^{k-r}c_{j+ke}
=F_j^{(r)}(p).
\quad}
\tag{1162.6}
$$
显示的 $r!$ 不可省略。

先对一个多项式用 $z^e=p+g$ 直接展开：
$$
z^{j+ke}
=z^j(p+g)^k
=z^j\sum_{r=0}^{k}
 \binom{k}{r}p^{k-r}r!\gamma_r(g).
$$
这给有限版本的 (1162.6)。
对一般形式级数，$\mathcal R\to S$ 是连续映射：
$z^{ep}=(p+g)^p\in pS$，故其幂趋零。
对每个固定 $r$，内和因 $p^{k-r}$ 而收敛；
另一方面 $m_{j,r}$ 被 $r!$ 整除，故随 $r\to\infty$
$p$-进趋零。多项式恒等式因而在同一个 $p$-完备环中收敛
到 (1162.6)。没有在分歧点处直接求和一个无估值控制的
rational sigma 或 dilogarithm 级数。

现在取 $0\le r\le i\le28$，并置
$L=i-r+1$。由 (1162.6)，有精确的有限输入式
$$
\boxed{\quad
m_{j,r}\equiv
 r!\sum_{k=r}^{i}
 \binom{k}{r}p^{k-r}c_{j+ke}
 \pmod {p^{\,i-r+1}}.
\quad}
\tag{1162.7}
$$
因为 $k>i$ 时 $k-r\ge i-r+1$，整个被删尾已经在
所模的整理想中。对剩余的 $k$，要求
$c_{j+ke}\bmod p^{i-k+1}$ 足够：
其误差乘 $p^{k-r}$ 后仍在 $p^{i-r+1}$ 中。
二项式系数只可能增加整除性，不会降低这个精度。

特别，在本来的 small-weight 范围 $r\le28<p$ 内，
$$
\boxed{\quad m_{j,r}\equiv r!\,c_{j+re}\pmod p.\quad}
\tag{1162.8}
$$
该式只选第 $r$ 个真正的 $e$-block；
它不是把所有高于十二阶的函数项设为零。

## 4. 函数展开的滤过条件也可以精确检查

设 $a\ge0$，并令 $\operatorname{Fil}^aS$ 是原
$r\ge a$ 的 PD 基元素闭包。对 $f\in\mathcal R$，
由唯一展开，以下条件等价：
$$
f\in\operatorname{Fil}^aS
\quad\Longleftrightarrow\quad
F_j^{(r)}(p)=0
\quad(0\le j<e,\ 0\le r<a).
\tag{1162.9}
$$
这要求原系数中的**等式**，不是仅要求其模 $p$ 消失。

亦可写为
$$
\boxed{\qquad
\mathcal R\cap\operatorname{Fil}^aS
=g^a\mathcal R.
\qquad}
\tag{1162.10}
$$
证明如下。对 $F_j(T)\in\mathcal O[[T]]$，代换
$T=p+G$ 与其逆 $G=T-p$ 在 $(p,T)$-完备环上连续。
低于 $a$ 次的 Taylor 系数是
$F_j^{(r)}(p)/r!$；由于 $\mathcal O$ 无挠，
它们为零正好等价于 (1162.9)。
故 $F_j(T)=(T-p)^aH_j(T)$，其中
$H_j\in\mathcal O[[T]]$。
代回 $T=z^e$ 并对 $j$ 求和即得 (1162.10)；
反向显然。

因此，若某个 raw 整函数尚不满足对应的 (1162.9)，
就不能仅因它整而把它标为某个指定的 filtered section。
本判据不替代原格或其标架的同一性。

## 5. 与原 FL 窗口拼接时的精确阶乘抵消

本节是一个明确带前提的推论。
令 $M$、适配整基 $e_b$、其 weights $w_b$ 及整基
$F_b=p^{-w_b}\varphi_M(e_b)$ 全部是
R1155 §16 中的**同一个实际**强可除格。
设已经在此基中给出
$$
x=\sum_b f_b(z)e_b
 \in\operatorname{Fil}^i(S\otimes_{\mathcal O}M),
\qquad
f_b(z)=\sum_{n\ge0}c_{b,n}z^n\in\mathcal R,
\qquad 0\le i\le h\le28.
\tag{1162.11}
$$
当 $w_b\le i$ 时，令 $r_b=i-w_b$。
实际滤过由 (1162.9) 保证 $f_b$ 的法向系数
在 $r<r_b$ 时为零。R1155 (1155.102) 只留下
$r=r_b$ 和 $0\le j<p$。
再以 (1162.8) 代入，其中的 $r_b!$ 与
(1155.102) 的 $1/r_b!$ 准确相消，得到
$$
\boxed{\quad
\operatorname{ev}\!\left(p^{-i}\varphi(x)\right)
\equiv
\sum_{b:\,w_b\le i}\ \sum_{j=0}^{p-1}
 (-1)^{r_b}
 \sigma\!\left(c_{b,j+r_be}\right)
 \varpi^{pj}F_b
 \pmod {p\,(\mathcal O_L\otimes M)} .
\quad}
\tag{1162.12}
$$
原 normal carry 的号 $(-1)^{r_b}$ 仍在。
特别，没有留下一个可任意吸收的 factorial、
cusp width、CM period 或 p-unit 尺度。

由于 $(F_b)$ 为整基，而且
$1,\varpi^p,\ldots,\varpi^{p(p-1)}$ 在 $\mathcal O_L/p$
上对 residue field 线性独立，
(1162.12) 作为**完整向量**为零，当且仅当
$$
c_{b,j+(i-w_b)e}\equiv0\pmod p
\quad\text{对全部 }w_b\le i,\ 0\le j<p .
\tag{1162.13}
$$
对一个额外线性或二次投影的单坐标，
必须先执行原实际投影；不能把这个完整向量判据
冒作那个单坐标必非零。

(1162.12) 只读明确有限的矩形表：
原四十三格取 $i\le14$；原至多二次 tensor 关系取
$i\le28$。
需要的实际函数次数可达到 $28e+p-1$。
这正是保留高 block 的理由，不能用 degree-twelve
coefficient jet 替代。

## 6. 原运算、Frobenius 字符和输入精度

(1162.2) 是原 tame 群的整 projector，
$\psi$ 在系数上施 $\sigma$，所以
$$
\psi(\mathcal P_j f)=\mathcal P_{pj\bmod e}(\psi f).
\tag{1162.14}
$$
直接检查时，$\sigma(a)=a^p$ 与
$\psi(z)=z^p$ 同时出现，不能只运输其中一个。
若实际输入还含 $M$ 的角色，(1162.12) 中的 $F_b$
必须一并保持；本式没有给 coefficient action 添加一个
新的“平凡化”。

对有限个已经给出的整形式函数，
有限加法、乘法、可逆矩阵求逆、整系数群态射，以及
已经证明整的原 finite transfer，都可先在 $\mathcal R$
中执行，再应用 (1162.6)。
其相容性来自原环映射与原乘法，特别
$$
\gamma_r(g)\gamma_s(g)=\binom{r+s}{r}\gamma_{r+s}(g).
$$
不能把右边的 binomial 删除后逐法向 degree 相乘。

本篇没有在 raw cover 的 degree 含 $p$ 时反除该 degree。
闭点/标记的 multiplicities、所有 crossed products、
同一根的零上链以及 ordered 中央 gauge 仍须照原来源保留。
R1155 §14 已证明的原 $R_\psi(u)\in\mathcal H(\mathcal R)$
可逐整矩阵槽应用本篇；但这一步本身仍只得到其
**raw formal matrix** 的法向表。
(1162.12) 的 $\varphi$ 作用于 filtered input $x$；
不能把已经是 Frobenius 矩阵的 $R_\psi$ 逐槽再施一次
$\varphi$，然后把该二次操作叫作原读数。

若要读 (1162.7) 的全部表，只需每个 block
$c_{j+ke}$ 至模 $p^{i-k+1}$，$0\le k\le i$。
若另外从输入单位求
$\kappa=(\psi(u)/u^p-1)/p$，
该除 $p$ 的输入精度须另多一位；
不能把本篇对已给 $f$ 的精度表误当为生成 $f$ 的全部预算。

## 7. 已闭算法与仍须识别的原对象

本篇支付了以下两个实际有限步骤：

1. 一个已整的原形式函数在真正 $\varpi^e=p$ 点上，
   其有限值精度由 (1162.5) 给出；
   其完整 PD 法向系数由 (1162.6) 给出，
   所需有限表及不等精度由 (1162.7) 给出。
2. 若这些函数已是同一原强可除格中的坐标，
   则 (1162.12)–(1162.13) 是该格的精确有限
   Frobenius 读取及完整向量零判据。

尚未在这里支付的接口是：
将 §15 的 rational raw comparison、
R1147 §§17–20 的原兼容塔和 coefficient jet，
写到 (1162.11) 的同一原整标架中，并识别实际
same-root/central gauges 的法向系数。
“两个 rational torsors 相同”不自动给这份整坐标表；
“各原点都 crystalline”也不能代替它。
因此本篇没有称已计算 $z_{12}$、
没有删除 global subtraction，
也没有从一个未算的表宣称整个 supersingular disk 唯一。

全部新的 projector、normal Taylor、精度、滤过交及
factorial 消去由上面的整代数证明自足给出。
严格 LT 坐标、原 43 格及其 PD window 分别只消费
[R712 §2](R712-actual-M2-second-digit-and-Lubin-Tate-two-block-reduction.md)、
[R1147 §§14–20](R1147-original-canonical-moment-Heisenberg-lift.md)、
[R1155 §16](R1155-original-primitive-dilogarithmic-Frobenius-readout.md)。
本篇没有数学程序执行。
