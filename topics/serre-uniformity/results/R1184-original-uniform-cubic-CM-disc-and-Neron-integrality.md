# R1184：原三次 CM 支路的统一完整解析盘与 Néron 整尾

会话：Astra-serre-24b8836b-20261126；root。

**状态：已证明。** 对原 $p\equiv5\pmod6$、$p>37$ 的指定 $\mu _6$-稳定 CM 项链，原 $X_1$ 上经过 $c_1$ 的分支在整个闭盘 $b-1\in p^3\mathbf Z_p$ 上有统一的解析参数。任一原实际 Jacobian 商的 Abel 映射在这个参数下具有 Néron 整微分，故 R1182 的图册指数可固定为 $a=3$。这个结论包括商在 $p$ 坏约化的情形。

这里固定的是完整图册和全部尾项的整性，尚未证明原首项为单位，亦未把这个闭盘中的全部点排除。R1182 的首项估值须用本篇的新参数重新计算；不能把旧图册中的 $B,e_m$ 原封不动搬来。没有把非 CM 椭圆曲线的有限 Cartan 结构提升到全部 $p^n$ 层。

## 1. 原对象和所要固定的尺度

沿用 [R616 §1](R616-original-CM-point-difference-and-explicit-height-basis.md) 与 [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)：

$$
X_1=\operatorname{Norm}\left(X_{\rm ns}^+(p)\times_j\mathbf P^1_b\right),
\qquad j=6912b^3(1-b^3),\qquad c_1:b=1.
\tag{1184.1}
$$

$c_1$ 使用原来的 $\mu _6$-稳定 CM 项链，且为有理点；原粗 $j$ 映射在相应的 Cartan 点处一次。取同一个实际商和基点

$$
q_C:J_{X_1}\longrightarrow C,\qquad
f_C(x)=q_C[x-c_1],\qquad t=b-1.
\tag{1184.2}
$$

本篇的解析图册结论不需 $C$ 简单或其秩条件；接 R1182 的排点结论时，仍须满足 R1011 的全部实际非挠和半秩范围。

取 $j=0$ 的 $p$ 整好约化模型

$$
E_0:\quad y^2=x^3+B_0,\qquad B_0\in\mathbf Z_p^\times,
\tag{1184.3}
$$

配同一项链 $\mathfrak n_0$。可以使用 $B_0=1$：在代数闭包中把原标记搬到这个模型；因为原粗点有理，而且整个 $\mu _6=\operatorname{Aut}(E_0)$ 固定指定项链，Galois 搬运中可能出现的自同构也固定它，所以搬回的 $\mathfrak n_0$ 是实际 Galois 稳定的标记。这里没有另选一个不相干的 $j=0$ 分支。

考虑同一细参数族

$$
E_u:\quad y^2=x^3+u x+B_0,\qquad u=pz,
\qquad \mathbb D_z=\operatorname{Sp}\mathbf Q_p\langle z\rangle.
\tag{1184.4}
$$

在整个闭单位盘上判别式为单位，故这是椭圆曲线族。以下先在一个含 $E_0[p]$ 坐标与 $\mu _6$ 的有限 Galois 扩张 $L/\mathbf Q_p$ 中构造，再作真实 Galois 下降。记 $R=\mathcal O_L\langle z\rangle$，所有估值均正规化为 $v_p(p)=1$。

## 2. 高度二给出的完整 Hasse 导数整性

在单位元取实际形式参数 $T=-x/y$。短 Weierstrass 方程的形式群定义在 $\mathbf Z_p[[u]]$ 上，写其乘 $p$ 级数为 $F_u(T)=[p]_u(T)$。其一次项恒为 $pT$，因而

$$
F_u(T)-F_0(T)\in uT^2\mathbf Z_p[[u,T]].
\tag{1184.5}
$$

原 $E_0$ 在 $p\equiv2\pmod3$ 超奇异，形式群高度为二。因此

$$
F_0(T)\bmod p=H(T^{p^2}),\qquad H'(0)\ne0.
\tag{1184.6}
$$

这里要用完整的 $p^2$ 次幂性质，而不仅是最低项次数。它也可由形式群同态的微分恒等式直接推出：特征 $p$ 中同态的原点导数为零，则其全部普通导数为零，故通过相对 Frobenius 分解一次；高度二使第二个同态的原点导数仍为零，再分解一次。所得最后同态的一次项为单位。

令 $F_u^{[j]}(T)$ 表示 Hasse 导数，即 $F_u(T+S)=\sum_{j\ge0}F_u^{[j]}(T)S^j$。由 (1184.6) 和 Lucas 二项系数关系，若 $p^2\nmid j$，则

$$
F_{pz}^{[j]}(T)\in p\mathbf Z_p\langle z\rangle[[T]].
\tag{1184.7}
$$

因为模 $p$ 的所有指数均为 $p^2$ 的倍数，而 $j$ 的最低两位不全为零时，相应二项系数被 $p$ 整除。代入 $u=pz$ 的其它项本来就被 $p$ 整除。这对全部 $j$ 成立，不是有限 Taylor 窗的截断断言。

置 $e=p^2-1$。原高度二 Newton 多边形给每个非零 $p$ 挠点的形式坐标 $r$ 精确赋值

$$
v_p(r)=\frac1e.
\tag{1184.8}
$$

确实，$F_0(T)/T$ 的常数项为 $p$，$T^{p^2-1}$ 系数为单位，较低系数均被 $p$ 整除。全部 $p^2-1$ 个非零根在这个单一斜率上；超奇异特殊纤维没有非零几何 $p$ 挠点，故所有几何挠点都在此形式邻域。两个不同根之差也有赋值 $1/e$：形式群差的参数等于普通差乘一个单位，而非零形式群差仍是非零 $p$ 挠点。

## 3. 整个闭 $u\in p$ 盘的逐根 Hensel 延拓

固定一个非零根 $r$，用与根间距相容的尺度

$$
T=r+r^2W.
\tag{1184.9}
$$

将 $F_{pz}(T)$ 除以 $pr^2$，得到 $R\langle W\rangle$ 中的实际方程

$$
G_r(W,z)=b_r(z)+a_r(z)W+\sum_{j\ge2}c_{r,j}(z)W^j=0.
\tag{1184.10}
$$

逐项系数满足如下完整估计。

1. 由 (1184.5) 和 $F_0(r)=0$，
   $$b_r(z)=\frac{F_{pz}(r)}{pr^2}\in zR.$$
2. $a_r(z)=F'_{pz}(r)/p$。形式不变微分给 $F'_0(r)=p\,\varepsilon_r$，其中 $\varepsilon_r\in\mathcal O_L^\times$；由 (1184.5)，
   $$a_r(z)\in\varepsilon_r+r zR,$$
   所以 $a_r$ 在整个闭盘上为单位。
3. 对 $j\ge2$，
   $$c_{r,j}=p^{-1}r^{2j-2}F_{pz}^{[j]}(r).$$
   若 $p^2\nmid j$，(1184.7) 给
   $$v_p(c_{r,j})\ge\frac{2j-2}{e}\ge\frac2e.$$
   若 $p^2\mid j$，则 $j\ge p^2$，直接整性给
   $$v_p(c_{r,j})\ge\frac{2j-2}{e}-1\ge1\ge\frac2e.$$

这些是 Gauss 范数估计，且随 $j\to\infty$ 趋于无穷；所有代入的级数在 $|r|<1$ 一致收敛。因此 (1184.10) 确实属于所写 Tate 代数，而非只有逐点解。

映射

$$
W\longmapsto-a_r(z)^{-1}\left(b_r(z)+\sum_{j\ge2}c_{r,j}(z)W^j\right)
\tag{1184.11}
$$

在 $R$ 的闭单位球上有严格收缩常数至多 $|r|^2<1$，并保留理想 $zR$。从零迭代得到唯一

$$
W_r(z)\in zR,\qquad
r(z):=r+r^2W_r(z),\qquad F_{pz}(r(z))=0.
\tag{1184.12}
$$

所以原根在整个闭盘中延拓，且 $v_p(r(z)-r)\ge2/e>1/e$。零挠点取恒零截面。不同原根的这些闭球互不相交，故获得全部 $p^2$ 个不同截面；泛纤维的 $E_{pz}[p]$ 有限 étale 且 degree $p^2$，这已经给出整个挠点族。

### 群律、配对、Galois 与原自同构

这个逐根搬运是群同构。实际形式群加法随 $u$ 整变化，其线性项 $T_1+T_2$ 与 $u$ 无关。代入两条 (1184.12) 后，和的参数与原和的参数之差有赋值至少 $2/e$。它是 $p$ 挠点，因而必须是原和所对应的唯一 Hensel 截面；原和为零时同样成立，因为其它根均有赋值 $1/e$。所以得到

$$
E_0[p]\times_L\mathbb D_{z,L}\ \simeq\ E_{pz}[p]
\tag{1184.13}
$$

的实际有限 étale 群同构，原点处是恒等。

Weil 配对也保留：它在任一对截面上的值属于 $L\langle z\rangle$，满足 $X^p=1$；这个整环中的函数只能等于一个常数 $p$ 次根，原点处的值决定该常数。Galois 对原根的作用保留所用邻近条件和方程，故由唯一性与 (1184.13) 相容。

对 $\mu\in\mu _6$，实际短模型间的同构是

$$
E_u\longrightarrow E_{\mu^4u},\qquad
(x,y)\longmapsto(\mu^2x,\mu^3y),\qquad T\longmapsto\mu^{-1}T.
\tag{1184.14}
$$

它同样保留每条 Hensel 截面的邻近条件；因此 (1184.13) 与这个跨纤维自同构严格相容。这里只构造了实际 $p$ 挠群的同构，没有声称它由椭圆曲线同源产生，也没有声称存在相容的全部 $p^n$ 层搬运。

## 4. 原项链的三次下降与完整粗 $j$ 盘

将原 $\mathfrak n_0$ 沿 (1184.13) 搬运，得到 $\mathbb D_z$ 上的实际非分裂 Cartan 项链。Galois 相容给 $\mathbf Q_p$ 上的族；(1184.14) 与原 $\mu _6$ 稳定性说明它给出的粗模态射在有效的 $\mu _3$ 作用 $z\mapsto\mu^4z$ 下不变。

加入 $\mu _3$ 后（这一步可取未分歧扩张），闭盘的商环准确为

$$
\mathcal O_L\langle z\rangle^{\mu _3}=\mathcal O_L\langle S\rangle,
\qquad S=z^3.
\tag{1184.15}
$$

事实上不变幂级数仅有 $3$ 的倍数指数。粗模态射因而下降到 $S$ 的整个闭盘，并由原 Galois 相容下降到 $\mathbf Q_p$。也可在有限 $j$-映射的盘上作这个下降：其逆像是 affinoid，环映射的像落在 (1184.15) 的不变环，故不需一个仅局部存在的商映射假设。

本族的实际 $j$ 函数为

$$
j=\frac{6912p^3S}{27B_0^2+4p^3S}
=p^3\frac{A S}{1+p^3 B S},
\qquad A=\frac{256}{B_0^2}\in\mathbf Z_p^\times,
\quad B=\frac4{27B_0^2}\in\mathbf Z_p^\times.
\tag{1184.16}
$$

于是 $J=j/p^3$ 与 $S$ 是闭单位盘上的互逆解析坐标：

$$
J=\frac{A S}{1+p^3BS},\qquad
S=\frac{J}{A-p^3BJ}.
\tag{1184.17}
$$

得到经过原 CM 项链点的实际解析截面

$$
\operatorname{Sp}\mathbf Q_p\langle j/p^3\rangle
\longrightarrow X_{\rm ns}^+(p)^{\rm an},
\tag{1184.18}
$$

与 $j$ 映射的复合为恒等。这包含闭盘的边界，并非只在原点的形式幂级数。尤其粗参数无需在 $\mathbf Q_p$ 中有立方根：立方根只用于构造细盘，(1184.15)–(1184.17) 已完成实际下降。

## 5. 原 $b=1$ 分支的统一解析参数

在原 (1184.1) 中置

$$
b=1+p^3w.
\tag{1184.19}
$$

直接展开给

$$
\frac{j(b)}{p^3}=-20736w+p^3w^2Q(w),\qquad Q\in\mathbf Z_p[w].
\tag{1184.20}
$$

因为 $p>3$，一次系数为单位；高次部分在闭盘上是严格收缩扰动。因此 (1184.20) 是闭单位盘的解析自同构。把它与 (1184.18) 组成，得到原纤维积中的同一分支；由正规化的泛性质提升到 $X_1^{\rm an}$，记为

$$
x:\mathbb D_w\longrightarrow X_1^{\rm an},\qquad
b(x(w))=1+p^3w,\qquad x(0)=c_1.
\tag{1184.21}
$$

该提升也可从有限曲线映射局部读取：存在到 $j$ 盘的截面使所选分支上的微分可逆，所以它在截面像上不分歧，正规化不改变此光滑分支。其它 Cartan 点或其它 $b$ 分支并未合并进来。

## 6. 形式 Néron 映射性质支付所有商的整尾

令 $\mathscr C$ 为原 $C/\mathbf Q_p$ 的完整 Néron 模型，$\widehat{\mathscr C}$ 为其沿特殊纤维的 $p$ 进完备化。Bosch–Schlöter 的 Theorem 6.2 说明：对于有 Néron 模型的有限型光滑群，只要模型拟紧或群交换，这个完备化就是相应刚性群的形式 Néron 模型。阿贝尔簇满足这些条件，包括坏约化。

在这里所用的映射性质是：从光滑、$p$ 进、拓扑有限型形式概形的泛纤维到 $C^{\rm an}$ 的刚性态射，唯一延拓到 $\widehat{\mathscr C}$。源

$$
\mathfrak D_w=\operatorname{Spf}\mathbf Z_p\langle w\rangle
\tag{1184.22}
$$

正满足全部条件；其泛纤维是本篇构造的完整闭盘。故实际复合 $f_C\circ x$ 唯一延拓为

$$
\mathfrak D_w\longrightarrow\widehat{\mathscr C}.
\tag{1184.23}
$$

原点截面送到单位截面。将 (1184.23) 在 $(p,w)$ 处完备化，任何实际 Néron 单位形式坐标 $T_i$ 的拉回都属于 $w\mathbf Z_p[[w]]$。常数项为零来自整条 $w=0$ 截面确实是单位，而不只是特殊纤维上同一点。

取 R1182 的原 $\mathbf Z_{(p)}$ 有理 Lie 基 $L_i$ 与其对偶整不变微分 $\omega_i$。则

$$
(f_C\circ x)^*\omega_i\in\mathbf Z_p[[w]]\,dw.
\tag{1184.24}
$$

写同一实际对数

$$
U^{(3)}(w)=\log_p f_C(x(w))
=\sum_{r\ge m}U_r^{(3)}w^r.
\tag{1184.25}
$$

它在 $w\in p\mathbf Z_p$ 中收敛并等于实际群对数；在形式层面其导数就是 (1184.24)。因此

$$
\boxed{\qquad rU_r^{(3)}\in\Lambda\quad\text{对全部 }r\ge1,
\qquad \Lambda=\operatorname{Lie}(\mathscr C)\otimes\mathbf Z_p.
\qquad}
\tag{1184.26}
$$

所有 $U_r^{(3)}$ 仍在原 $\operatorname{Lie}(C)(\mathbf Q)$ 中：$c_1$、$t=b-1$、$f_C$ 和 $L_i$ 全部有理，唯一的代数局部分支给有理 Taylor 系数；代入 $t=p^3w$ 仍有理。

于是 R1182 §2.2 所需的整数可以无条件对这个原分支取

$$
\boxed{a=3.}
\tag{1184.27}
$$

它不依赖所选 $C$ 的方程、商同源度或 Néron 坏纤维的具体结构。原商格没有被换成椭圆曲线的好约化格；整性来自到实际坏约化商的形式 Néron 映射性质。

## 7. 接到原半秩消去泛函，保留真正剩余成本

现在满足 R1182 的全部原半秩条件，保留同一 $\beta'=M\beta$、交错形式 $\Omega$、泛函 $\lambda_{\beta'}$ 及其本原化 $\lambda_0$。用新向量 $U_m^{(3)}$ 定义

$$
a_m^{(3)}=\lambda_{\beta'}(U_m^{(3)}),\qquad
e_m^{(3)}=v_p\bigl(\lambda_0(U_m^{(3)})\bigr),
\qquad \ell_p(m)=\lceil\log_p(m+1)\rceil.
\tag{1184.28}
$$

R1182 的同点解析子群论与有效线性形式定理仍适用，给可计算的 $B^{(3)}$；其系数高度必须从 $U_m^{(3)}$ 读取。整个原有理分支在

$$
\boxed{\quad
v_p(b-1)\ge
3+\ell_p(m)+\max\{0,e_m^{(3)}\}+1
\quad}
\tag{1184.29}
$$

内仅有 $c_1$。若原首阶 $m\le p-2$，准确整尾改善为

$$
\boxed{\quad v_p(b-1)\ge4+e_m^{(3)}.\quad}
\tag{1184.30}
$$

预定有限精度及对数截断仍由 R1182 §9 给出，使用新 $B^{(3)}$。没有执行数学程序。

本篇消去了“原 Abel 图册的未知缩盘指数”这一输入；以下成本仍实际存在：同一首项与原 MW 对数线的相对估值、原商的代数模型/极化尺度、有效线性形式中的系数和点高度，以及这些界同原候选深度的比较。仅由 (1184.27) 不能排除整个 $p^3$ 盘，更不能排除原全局其它分支或变化的 $X_d$。

## 来源和边界

- [R616](R616-original-CM-point-difference-and-explicit-height-basis.md) §1、[R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md) §§1、6：原 $\mu _6$-稳定项链、指定有理 $c_1$、同一 $b$ 参数和实际商。
- [R1182](R1182-original-effective-Abel-jet-valuation-and-CM-disc-radius.md) §§2、7、9：同一 Néron 格、首项估值、完整尾和本原化。本文的 $a=3$ 替代其图册缩盘输入，未替换其它实际数据。
- S. Bosch、K. Schlöter，*Néron models in the setting of formal and rigid geometry*，**Math. Ann. 301 (1995), 339–362**，Theorem 6.2，原刊第357页；[DOI](https://doi.org/10.1007/BF01446633)，[已实读原刊页](https://gdz.sub.uni-goettingen.de/fulltext/PPN235181684_0301/00000363?_format=xml)。只使用其正式形式 Néron 定理。
- C.-L. Chai，*A bisection of the Artin conductor*，[作者稿 §5.1](https://www2.math.upenn.edu/~chai/papers_pdf/bAcond_v21.pdf)：交叉核对上段 $p$ 进拓扑有限型光滑源的完整映射性质；不混入该稿 §5.2 的更一般非 $p$ 进形式空间。

完整挠点延拓、闭盘收缩、群律/Weil 配对、$\mu _3$ 与 Galois 下降均在本文纸面证明。没有数值窗，没有非 CM 全层 Cartan 提升，也没有将原 CM 参考当作待排候选本身。
