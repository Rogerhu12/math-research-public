# R1069 — 固定 √17 形式叶的准确 1/4 算术高度与完整 theta 极成本

日期：2026-11-28 UTC。会话：Astra-rank2-Sha-0b097461-20261127。

**以下固定来源、形式叶、全部好素数的 p-闭合分类、准确 1/4-arithmetic 饱和界及完整复极点成本已证明。** 本篇不给原 canonical 泛函增加零行，也不把这里的高度系数替换成原饱和矩阵的 Smith 增益。主目标仍未完成。

[R1062 §13](R1062-original-translated-miller-jets-and-critical-weight-germs.md) 已在原整 CM 形式群、实际 symmetric lift 和完整 Hall 权下支付范数恰为 17 的规范。其固定平方根特化产生本文的同一个有理物理级数。本文处理这个特化的全局形式叶和高度，保留分母的全部真实零点。

## 1. 固定有理来源及与旧参考商的区别

记
$$
 E_b:\quad y^2=x^3+b,\qquad
 \omega_b=\frac{dx}{2y},\qquad
 x_b(z)=z^{-2}+\cdots,\quad y_b(z)=-z^{-3}+\cdots,
 \quad \sigma_b(z)=z+\cdots .
 \tag{1}
$$
取 $a=\sqrt{17}>0$、$B=17^3=4913$。从不改变微分规范的同质性得到
$$
 \begin{aligned}
 x_B(z)&=a^2x_1(az),&
 y_B(z)&=a^3y_1(az),&
 \sigma_B(z)&=a^{-1}\sigma_1(az),\\
 \Theta_{2,b}(z)&=x_b(z)\sigma_b(z)^2,&
 \Theta_{2,B}(z)&=\Theta_{2,1}(az).
 \end{aligned}
 \tag{2}
$$
例如曲线同构
$$
 j_a:E_1\longrightarrow E_B,\qquad (x,y)\longmapsto(a^2x,a^3y)
$$
满足 $j_a^*\omega_B=a^{-1}\omega_1$，故
$j_a(\exp_{E_1}(az))=\exp_{E_B}(z)$。
这固定了后文形式叶的实际斜率，而非只固定两曲线的同构类。

保持原完整来源
$$
 \begin{aligned}
 R_S(x)&=\frac17x^2(X+1)(X-8)(7X^2-4X+16),\qquad X=x^3,\\
 S_{34,1}(z)&=\sigma_1(z)^{34}R_S(x_1(z)),\\
 H(z)&=\frac{S_{34,1}(z)}{\Theta_{2,B}(z)}
      =\frac{S_{34,1}(z)}{\Theta_{2,1}(\sqrt{17}\,z)} .
 \end{aligned}
 \tag{3}
$$
所有因子均按原首项归一。因此
$$
 H(z)\in z^6\bigl(1+z^6\mathbf Q[[z^6]]\bigr).
 \tag{4}
$$
这里 $z^6(1+z^6\mathbf Q[[z^6]])$ 只表示次数型和首项；不声称全部有理系数在每一素数处整。式(4)由 $S_{34,1}$ 的有理系数和 $\Theta_{2,1}$ 只含 6 的倍数次项直接得到，因为 $a^{6j}=17^{3j}$。换 $a$ 为 $-a$ 不改变 $\Theta_{2,1}(az)$。

保持 R1062 的范围，若 $p>211$、$p\equiv2\bmod3$ 且 $(17/p)=1$，可将同一个代数数 $a$ 嵌入 $\mathbf Q_p$。它对 $L=K_p$ 的范数是 $a^2=17$。R1062(G81)--(G83)于是把(3)接回同一个严格形式群参数 $v$，给
$$
 H(z(v))\in v^6\mathcal O_L[[v]]^\times
$$
以及原完整平移/Hall 身份。这个整性是原形式群坐标中的结论；没有把 $z$ 当作整形式参数，也没有把因子各自的边界收敛当作前提。

须与 [R310](R310-jzero-actual-rankzero-frame-third-kind-and-central-transpose.md) 区分：R310 的 $S/H_3$ 是同一 $b=17$ 曲线上的有理商，$H_3$ 是已识别的真实 $E_{4913}$ rank-zero Hecke 向量。本文的 $\Theta_{2,B}$ 是(2)的 degree-two 截面。二者没有因参考曲线相同便成为同一来源；R310 的中央质量和第三类转置不能直接给本文的 $H$ 新中央零。

## 2. 真正固定的有理形式叶

令
$$
 A=E_1\times E_B,\qquad O_A=(O,O),
 \qquad
 D_b=2y\,\partial_x+3x^2\,\partial_y,\qquad
 V=D_1+D_B .
 \tag{5}
$$
$D_b$ 是 $\omega_b$ 的对偶不变向量场。因 $A$ 光滑射影且 $V$ 处处非零，
$\mathcal F=\mathcal O_A V$ 是定义在 $\mathbf Q$ 上的正则一维代数叶状结构。
其经过 $O_A$ 的光滑形式叶为
$$
 \widehat{\mathcal C}:
 z\longmapsto\bigl(\exp_{E_1}(z),\exp_{E_B}(z)\bigr).
 \tag{6}
$$
用两个有理形式群对数的等式也可定义(6)，所以该形式叶定义在 $\mathbf Q$ 上，原点的剩余域次数是 1。这里的 $z$ 仅用来表示同一不变 Lie 时间。

在第二因子上用 $j_a^{-1}$ 识别到 $E_1$ 后，(6)成为
$$
 z\longmapsto(\exp_{E_1}(z),\exp_{E_1}(az)).
 \tag{7}
$$
其斜率是 $\sqrt{17}$，不是 17，也不是一个全局 CM endomorphism。

**命题 1。** $\widehat{\mathcal C}$ 的几何 Zariski 闭包是整个 $A$。

**证明。** (7)的复解析像是连通解析子群。其 Zariski 闭包是连通代数子群；这一点由加法和取逆的代数性，以及稠密子集在这些运算下封闭得到。两个投影均非平凡。

若闭包为一维，则它是 $E_1^2$ 中的椭圆子群。由椭圆曲线同源的对偶，存在不全为零的 $\alpha,\beta\in\operatorname{End}_{\overline{\mathbf Q}}(E_1)=\mathcal O_K$，使其被 $[\alpha]P+[\beta]Q$ 杀掉。对(7)在零点微分，得
$$
 \alpha+a\beta=0.
$$
两个投影非平凡使 $\alpha\beta\ne0$，于是 $a\in K=\mathbf Q(\sqrt{-3})$，与 $a=\sqrt{17}$ 矛盾。闭包故为二维。

一个代数方程若在原点的形式叶上为零，则其沿(7)的解析拉回在一个邻域为零，再由恒等定理在整个复平面为零。因此形式闭包和上述解析像闭包相同。$\square$

## 3. 实际 Hasse 标量与四个素数类

只需删除有限坏集 $\{2,3,17\}$。两条 Weierstrass 曲线及(5)在其余素数都有好整模型。

对好素数 $p$，记
$$
 \mathsf H_b(p)=[x^{p-1}](x^3+b)^{(p-1)/2}\in\mathbf F_p .
$$
当前微分规范下，Cartier 算子和受限 Lie 幂分别满足
$$
 \mathcal C(\omega_b)=\mathsf H_b(p)^{1/p}\omega_b,
 \qquad
 D_b^p=\mathsf H_b(p)D_b .
 \tag{8}
$$
这里没有隐去一个只对某曲线有效的微分比例。第一式可直接由
$$
 \omega_b=\frac{(x^3+b)^{(p-1)/2}\,dx}{(2y)^p}
$$
及 Cartier 对 $x^jdx$ 的公式求得；分子的次数小于 $2p-1$，只有 $x^{p-1}$ 项留下。第二式是对偶不变向量场的受限幂公式，所用的不变微分正是同一个 $\omega_b$。

若 $p\equiv2\bmod3$，分子没有 $x^{p-1}$ 项，故
$$
 \mathsf H_1(p)=\mathsf H_B(p)=0.
 \tag{9}
$$
若 $p\equiv1\bmod3$，设 $s=(p-1)/6$，则
$$
 \mathsf H_b(p)=\binom{3s}{2s}b^s,\qquad
 \mathsf H_B(p)=17^{(p-1)/2}\mathsf H_1(p)
             =\left(\frac{17}{p}\right)\mathsf H_1(p).
 \tag{10}
$$
$\binom{3s}{2s}$ 模 $p$ 非零，因为其三个阶乘的指标都小于 $p$。

两个因子上的导子交换，所以 $V^p=D_1^p+D_B^p$。因而
$$
 \boxed{
 \mathcal F\bmod p\text{ 对受限 }p\text{ 次幂封闭}
 \iff
 p\equiv2\bmod3
 \quad\text{或}\quad
 \left(\frac{17}{p}\right)=1.
 }
 \tag{11}
$$
普通且 $(17/p)=-1$ 时，$V^p=\mathsf H_1(D_1-D_B)$，与 $D_1+D_B$ 线性无关；这里 $p\ne2$。惰性时 $V^p=0$，不依赖任何 canonical 坏条件。

令 $\chi_{-3}(p)$ 和 $\chi_{17}(p)$ 是两个二次特征。两二次域 $K$ 与 $\mathbf Q(\sqrt{17})$ 不同，其合成域的 Galois 群为 $C_2\times C_2$。四个 Frobenius 类各有自然密度 $1/4$：

| $\chi_{-3}(p)$ | $\chi_{17}(p)$ | 两曲线约化型 | 原叶是否 p-闭合 |
|---|---|---|---|
| $+1$ | $+1$ | 普通 | 是 |
| $+1$ | $-1$ | 普通 | 否 |
| $-1$ | $+1$ | 超奇异；固定 $a\in\mathbf Q_p$ 的目标类 | 是 |
| $-1$ | $-1$ | 超奇异 | 是 |

所以 p-闭合集的密度准确为 $3/4$。Chebotarev（在这里也可用模 51 的素数算术级数定理）和部分求和给
$$
 \frac{\displaystyle
       \sum_{\substack{p\le x\\\mathcal F\bmod p\ {\rm p\!-\!closed}}}
                       \frac{\log p}{p-1}}
      {\displaystyle\sum_{p\le x}\frac{\log p}{p-1}}
 \longrightarrow \frac34 .
 \tag{12}
$$
这正是下一节原文所用的加权密度。有限删去坏素数不改变(12)。

## 4. 上界：同一形式叶是 1/4-arithmetic

本节引用 M. Herblot，*Algebraic points on meromorphic curves*，
[作者全文](https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf)，
Definition 2.5、Lemma 3.3、Definition 3.5、Proposition 3.6（原稿 §§2--3，尤其印页 19--20）。

这里的 $\alpha$-arithmetic 约束的是同一 ample 格上沿形式叶的实际评价映射的高度。它不是给某一指定 Newton 泛函的估值命名。其含义是：对任意有限地点集 $S\subset\Sigma_{\mathbf Q}$ 和任意 $\varepsilon>0$，相应评价高度有
$$
 \sum_{v\in\Sigma_{\mathbf Q}\setminus S} h_v(\varphi_{D,\widehat{\mathcal C}}^k)
 \le \left(\alpha+\varepsilon\right)k\log k+C_{S,\varepsilon}(k+D)
 \tag{13}
$$
型的统一界，以及每一地点 $v$ 上的 $h_v(\varphi_{D,\widehat{\mathcal C}}^k)\le C_v(k+D)$。这里 $D$ 是 ample 截面幂次，$k$ 是沿同一形式叶的 jet 阶；不得将它们直接替换成原矩阵的独立角数。

Proposition 3.6 的全部输入在本例中分别是：

- 射影簇 $X=A$ 定义在 $\mathbf Q$；
- $O_A$ 是光滑有理点；
- $\mathcal F$ 是其邻域内的实际正则代数叶状结构；
- $\widehat{\mathcal C}$ 是该叶状结构经过 $O_A$ 的形式叶；
- 所用加权 p-闭合密度由(12)准确给出 $\beta=3/4$。

该命题的方向是 $\beta\mapsto1-\beta$，所以
$$
 \boxed{\widehat{\mathcal C}\text{ 是 }1/4\text{-arithmetic}.}
 \tag{14}
$$
也可直接看到其主项来源：一般好素数的局部评价成本至多
$k\log p/(p-1)$，p-闭合处改为 $k\log p/(p(p-1))$。
后者对全部素数可求和；前者仅剩密度 $1/4$ 的普通、非平方类。
所有固定坏处均收入(13)的线性项。

## 5. 复一致化的阶 2 与 1/4 的最优性

(6)给来自 $\mathbf A^1(\mathbf C)$ 的同一全平面一致化，原点微分非零。其射影坐标可以用
$$
 \bigl(\sigma_b^3,\ \sigma_b^3x_b,\ \sigma_b^3y_b\bigr),
 \qquad b=1,B,
 \tag{15}
$$
再取 Segre 乘积得到。每个三元组的三个函数均为整函数且无共同零：
在周期格点，最后一个的极与 $\sigma_b^3$ 的三重零准确抵消。
它们满足 $\log^+|f(z)|\le C(1+|z|^2)$。这是 sigma 的二次增长与
$x_b,y_b$ 在固定基本域上的极被(15)消除后的直接估计。

因此(15)给 Herblot Definitions 5.1、5.4--5.5 所需的实际
$\Theta^*(\mathcal L^{-1})$ 全局截面，范数由
$A_1\exp(A_2|z|^2)$ 控制；可取光滑射影紧化
$\mathbf P^1$、唯一删点 $\infty$ 和 $\rho_\infty=2$。
$\mathcal L$ 可取原两个 Weierstrass ample 线丛的外积；
换 ample 度量只改变固定常数。于是该一致化的阶至多为2。
从任一因子的正平移不变曲率拉回为非零常数面积形式，也可看到其
Nevanlinna 特征具有正的二次主项，故这个自然一致化的阶确为2。

现在完整使用原文 Theorem 6.1（印页31）：

- 基底是 $\mathbf Q$；
- 只有一个形式叶和一个点，故 $m=1$、点域次数 $d_1=1$；
- 形式叶光滑一维；
- 其复一致化满足上述 $\rho=2$ 输入；
- 命题1给其 Zariski 闭包维数 $r=2$。

若该叶是某个 $\alpha$-arithmetic，$\alpha>0$，该定理给
$$
 \frac1{\alpha}\le \frac{r}{r-1}\rho=4 .
 \tag{16}
$$
若 $\alpha=0$，则它也是任意正 $\varepsilon$-arithmetic，仍与(16)
在 $\varepsilon<1/4$ 时矛盾。结合(14)，得到
$$
 \boxed{
 \inf\{\alpha\ge0:\widehat{\mathcal C}\text{ 是 }\alpha
                         \text{-arithmetic}\}=\frac14,
 \quad\text{且端点 }\frac14\text{ 已取得}.
 }
 \tag{17}
$$
这不是由某个有限 Taylor 计算猜出的“临界常数”。上界来自所有素数的
实际受限 Lie 幂，下界来自同一个非代数形式叶的完整一致化和定理(16)。

## 6. 高斯平衡仍保留完整二次极点成本

回到固定物理函数(3)。设
$$
 \Lambda=\operatorname{Per}(E_1,\omega_1),\qquad
 \mathcal A_\Lambda=\operatorname{area}(\mathbf C/\Lambda).
$$
$\Theta_{2,1}$ 是 degree-two theta 截面，其零点在 $E_1$ 上准确为
$$
 Q_\pm=(0,\pm1).
$$
二者是不同的简单零；在周期格点，$x\sigma^2$ 的原点值为1。
因此 $\Theta_{2,1}(az)$ 的全部复零是两个不同的
$\Lambda/a$ 陪集，均为简单零。

$S_{34,1}$ 是 degree-34 的整 theta 截面。它在每个基本域有34个零，
计重数；原 $R_S$ 的唯一极在 $O$、极阶28，故 $O$ 的零阶恰为6。
没有把 $S$ 替换成只有原点零的 sigma 幂。

两者只有有限多个共同零。事实上，对一个固定的 $S$ 零陪集
$P+\Lambda$ 和一个固定的分母零陪集 $(Q+\Lambda)/a$，若有两个不同
交点，其差 $\lambda\ne0$ 满足
$$
 \lambda\in\Lambda,\qquad a\lambda\in\Lambda .
$$
因 $\Lambda=\Omega\mathcal O_K$，这迫 $a\in K$，矛盾。
两边各只有有限个陪集，因此公共零总数有限。

格点的圆盘计数于是给固定函数 $H$ 的完整极点与零点计数
$$
 \begin{aligned}
 n_\infty(R,H)&=\frac{34\pi}{\mathcal A_\Lambda}R^2+O(R+1),\\
 n_0(R,H)&=\frac{34\pi}{\mathcal A_\Lambda}R^2+O(R+1).
 \end{aligned}
 \tag{18}
$$
有限个抵消只影响余项。令 $N_\infty$ 为积分极点计数，得
$$
 \boxed{
 N_\infty(R,H)=\frac{17\pi}{\mathcal A_\Lambda}R^2
                                  +O(R+\log R).
 }
 \tag{19}
$$
标准 Nevanlinna 特征满足
$$
 T(R,H)\ge N_\infty(R,H),\qquad T(R,H)=O(R^2),
 \tag{20}
$$
后一个界由两个整 theta 函数的二次增长得到。所以 $H$ 的亚纯增长阶
准确为2。

式 $34-2a^2=0$ 的确消掉共同物理 Lie 变量中的二次高斯主项。
它表现为(18)的零、极二次密度相同，而不是使两个正计数都消失。
特别对任意固定非零多项式 $P(U)\in\mathbf C[U]$、$\deg P=D$，
$P(H)$ 在 $H$ 的每个极点有准确的 $D$ 倍极阶，故(19)的主项也乘 $D$。
若把系数扩为 $E_1$ 上的固定椭圆函数，最高系数的零也仅能在上述
分母极集合中消掉有限多个点，同样不能免费删去其正密度极成本。

内在地，(3)是
$$
 \operatorname{pr}_1^*\mathcal O_{E_1}(34O)
 \otimes\operatorname{pr}_2^*\mathcal O_{E_B}(-2O)
 \tag{21}
$$
的亚纯截面在(6)上的 theta 框架表达，不是 $A$ 上的有理函数。
若在全局辅助截面中清分母，第二因子的负 degree-two 费用必须真实
补回；不能凭形式叶上的高斯平衡把这个全局线丛费用置零。

## 7. 对原 canonical 与 Smith 预算的准确范围

本文新固定的是两个全局量：

1. 原有理形式叶的最优算术高度指数为 $1/4$；
2. 原固定比值 $H$ 的全部 theta 极仍有(19)的正二次主项。

这两个量都在没有任何 canonical 坏假设时成立。特别是
$p\equiv2\bmod3$、$(17/p)=1$ 的目标素数类已经属于(11)的自动
p-闭合部分。将原 canonical 坏条件再写成这个裸叶的 p-闭合，
不会增加任何有限处收益。

(17)针对 Herblot 的同一 ample 评价旗标，不是原
$M_D$、同一个修正 $R$ 或全部 $j!C$ Smith 指数的计算。
(19)也不给原 canonical 外权、参考 Hall 因子或有限相位赋零。
因此本文没有降低此前需要比较的
$\sum_p g_{p,D}\log p$ 与 $3M_D\log D$ 的主预算。

可以继续消费的实际输入仍是 R1062(G82)--(G85)和
[R1067 的完整 native Euler 续证](R1067-original-first-wild-rubin-native-euler-continuation.md)：
在同一原 Hall 和内部，读取 $H(v(u)\oplus Q)$ 的有限加法 jet，
保全部参考字、外权、阶乘和 native carry。
若这些真实 covector 在坏条件下产生新约束，需要逐式作用在该全和；
不能把(17)的裸叶界或(4)的有理系数替代这一工作。

## 来源与查重范围

- R1062(G73)--(G85)：exact Norm17、全 symmetric lift、中心与原 Hall
  相位、完整平移核及固定平方根特化。
- R310：不同的同曲线真实 $S/H_3$ 商，全部24极及中央转置；本文没有
  重登记它的第三类结论。
- [R14](R14-elliptic-exponential-pclosure.md)：旧直接椭圆指数叶的
  p-闭合分类；其环境与本文的两条椭圆曲线不同。
- [旧代数化输入笔记](../notes/2026-11-12-fixed-difference-bost-inputs.md)：
  大小、收敛半径、tame 共振及完整 A-analytic 输入的区别。
- M. Herblot, *Algebraic points on meromorphic curves*，2012-04-18 作者稿，
  [原文 PDF](https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf)：
  Definition 2.5，§3 的受限 p 次幂约定，Lemma 3.3、
  Definition 3.5、Proposition 3.6，Definitions 5.1、5.4--5.5，
  Theorem 6.1。本文只取这些原定理的精确方向，并逐项验证输入。

本篇没有执行新的数学计算，没有创建扫描、缓存或可重算数值产物。
