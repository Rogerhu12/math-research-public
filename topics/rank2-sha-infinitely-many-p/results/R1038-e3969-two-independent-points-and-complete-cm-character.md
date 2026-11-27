# R1038 — E3969 的两点独立性、完整三同源与原 CM 角色

日期：2026-11-27 UTC。**状态：以下秩至少二、完整同源/Kummer 身份、
Hecke 角色及导子已证明。** 这是一条真实可候选的固定曲线；
尚未将它认作 R1037 两条 degree378 输入的非零分量。
不存在从质量为零、有限好位吻合或数据库 rank 字段直接赋予新中央零的步骤。

## 1. 固定曲线、点与实际结论

置
$$
 E:\ Y^2=X^3+3969=X^3+63^2,\qquad
 E':\ y^2=x^3-147,
 \qquad K=\mathbf Q(\delta),\quad\delta^2=-3.
 \tag{1}
$$
以下全是原模型的有理点：
$$
 P=(18,99),\quad S=(-5,62),\quad T=(0,63)\in E(\mathbf Q),
 \qquad R=(7,14)\in E'(\mathbf Q).
 \tag{2}
$$
直接代入分别给
$99^2=18^3+3969$、$62^2=(-5)^3+3969$、
$14^2=7^3-147$。
本篇证明
$$
 \boxed{\operatorname{rank}E(\mathbf Q)\ge2.}
 \tag{3}
$$
更准确地，P、S、T 在 $E(\mathbf Q)/3E(\mathbf Q)$ 中线性独立，
而 $E[3](\mathbf Q)=\langle T\rangle$。
不使用 Sha 偶性，也不把一个 descent 上界当成 Mordell–Weil 下界。

## 2. 完整原三同源及有理核

定义
$$
 \begin{aligned}
 \phi:E'&\longrightarrow E,\\
 (x,y)&\longmapsto
 \left(\frac{x^3-588}{x^2},
       \frac{y(x^3+1176)}{x^3}\right),
 \end{aligned}
 \tag{4}
$$
以及
$$
 \begin{aligned}
 \widehat\phi:E&\longrightarrow E',\\
 (X,Y)&\longmapsto
 \left(\frac{X^3+15876}{9X^2},
       \frac{Y(X^3-31752)}{27X^3}\right).
 \end{aligned}
 \tag{5}
$$
直接以 (1) 消去 y² 或 Y²，(4)、(5) 满足目标曲线方程。
它们在 O 延拓为 O，在分母为零的点也按光滑射影曲线唯一延拓。
因此是保持 O 的非恒定椭圆曲线态射，即三同源。

微分逐式给
$$
 \phi^*\frac{dX}{2Y}=\frac{dx}{2y},\qquad
 \widehat\phi^*\frac{dx}{2y}=3\frac{dX}{2Y}.
 \tag{6}
$$
于是两个复合与 [3] 有同一微分。特征零下，保持 O 的同态之差若微分
为零只能是零同态，故
$$
 \phi\widehat\phi=[3]_E,\qquad
 \widehat\phi\phi=[3]_{E'}.
 \tag{7}
$$
两核准确为
$$
 \ker\phi=\{O,(0,7\delta),(0,-7\delta)\},\qquad
 \ker\widehat\phi=\{O,T,-T\}.
 \tag{8}
$$
特别 $\ker\phi(\mathbf Q)=0$，所以 $\phi$ 在有理点群上单射。
同时
$$
 \phi(R)=
 \left(\frac{343-588}{49},
       \frac{14(343+1176)}{343}\right)=(-5,62)=S.
 \tag{9}
$$

## 3. 两个 Kummer 映射，包含例外点

对曲线 $v^2=u^3+c^2$，函数 $v+c$ 的除子是
$3(0,-c)-3O$。其立方类按群律给同态。这也可完全由直线核定：
若 $v=mu+n$ 与曲线的三个交点为 $Q_i=(u_i,v_i)$，保交点重数，则
$$
 \prod_{i=1}^3(v_i+c)=(n+c)^3.
 \tag{10}
$$
证明是对首一方程
$u^3-m^2u^2-2mnu+c^2-n^2=0$
在 $u=-(n+c)/m$ 评价；m=0 直接成立。
竖直弦给
$(v+c)(-v+c)=-u^3$，而 $-1$ 本身是立方。
切线、重交点和零点/极点由同一重数身份及局部首项延拓，故未略去
任何群律例外。

因此本篇使用的真实同态为
$$
 \begin{aligned}
 \alpha:E(\mathbf Q)&\longrightarrow
                   \mathbf Q^\times/\mathbf Q^{\times3},
 &\alpha(X,Y)&=[Y+63],\\
 \beta:E'(\mathbf Q)&\longrightarrow
                   K^\times/K^{\times3},
 &\beta(x,y)&=[y+7\delta].
 \end{aligned}
 \tag{11}
$$
在 (11) 第一行的例外点固定
$$
 \alpha(O)=1,\quad \alpha(T)=[126],\quad
 \alpha(-T)=[126]^{-1}.
 \tag{12}
$$
后一项由
$(Y+63)(Y-63)=X^3$ 在 $-T$ 的局部展开得到；
出现的负号是立方，不另改类。第二行的非 O 有理点不会满足
$y+7\delta=0$，并设 $\beta(O)=1$。

全同源像上的立方身份是
$$
 \boxed{\begin{aligned}
 \alpha(\phi(x,y))
   &=\left[\left(\frac{y+21}{x}\right)^3\right]=1,\\
 \beta(\widehat\phi(X,Y))
   &=\left[\left(\frac{Y+63\delta}{3X}\right)^3\right]=1.
 \end{aligned}}
 \tag{13}
$$
第一式分子展开为
$y(x^3+1176)+63x^3=(y+21)^3$；
第二式为
$Y(X^3-31752)+189\delta X^3=(Y+63\delta)^3$。
(13) 在所有有定义的仿射点是函数恒等式；在 O、T、−T 与核点按
(11)–(12) 的 Kummer 延拓仍为平凡类。
这只是证明所需的全像消失，不使用尚未支付的完整 Selmer 上界。

## 4. 三个模三类独立，得到两个秩方向

两个有理立方类准确为
$$
 \alpha(P)=[162]=[2\cdot3^4],\qquad
 \alpha(T)=[126]=[2\cdot3^2\cdot7].
 \tag{14}
$$
它们在 $\mathbf Q^\times/\mathbf Q^{\times3}$ 独立：
7-adic 赋值先迫第二指数模三为零，2-adic 赋值再迫第一指数为零。

另一方面
$$
 \beta(R)=[14+7\delta]=[7(2+\delta)]
          =[(2+\delta)^2(2-\delta)].
 \tag{15}
$$
$2+\delta,2-\delta$ 是 K 中两个不同的 norm7 素元；
它们公因子只能除 $2\delta$，故在7处互素。
(15) 的两个素理想赋值为 (2,1)，所以此类非立方且恰有三阶。

现在假设
$$
 aP+bS+cT=3Q,\qquad a,b,c\in\mathbf Z,\quad Q\in E(\mathbf Q).
 \tag{16}
$$
对 (16) 施加 α；同态性及 (13) 给 $\alpha(S)=1$，
而三倍点的立方类平凡。由 (14) 得 $3\mid a,c$。
写 $a=3a_1,c=3c_1$；T 的水平切线是三重交点，故3T=O，于是
$$
 bS=3(Q-a_1P)=\phi\widehat\phi(Q-a_1P).
$$
结合 $S=\phi R$ 与 $\ker\phi(\mathbf Q)=0$，严格得到
$$
 bR=\widehat\phi(Q-a_1P).
$$
再施加 β，(13)、(15) 迫 $3\mid b$。
所以 P、S、T 在 $E(\mathbf Q)/3E(\mathbf Q)$ 中独立。

原三分多项式为
$$
 \psi_3(X)=3X(X^3+4\cdot3969).
 \tag{17}
$$
除 X=0 外，若有有理根必须 $X^3=-15876$，但右端7-adic 赋值为2，
不是三的倍数。因此 $E[3](\mathbf Q)$ 准确为 $\{O,T,-T\}$。
由 Mordell–Weil 群的有限生成结构，
$$
 \dim_{\mathbf F_3}E(\mathbf Q)/3E(\mathbf Q)
 =\operatorname{rank}E(\mathbf Q)+
   \dim_{\mathbf F_3}E[3](\mathbf Q).
$$
左端至少三、最后一项为一，(3) 得证。

## 5. 原 CM 角色、全部坏素支持与准确导子

本节沿用 R302 对 $E_1:y^2=x^3+1$ 的真实
Hecke 角色 $\psi_1$、原 CM type 与 $(2\delta)$ 导子。
取 $u^3=63$。同构
$$
 E_1\longrightarrow E,\qquad(x_1,y_1)\longmapsto(u^2x_1,63y_1)
 \tag{18}
$$
的 Galois 差为原 $\mu_3$ CM 作用。故对素于2、3、7的理想，
$$
 \boxed{\psi_E(\mathfrak a)=
 \psi_1(\mathfrak a)\left(\frac{63}{\mathfrak a}\right)_3^{-1}.}
 \tag{19}
$$
这里三次幂剩余符号采用原解析 CM type：
对 $\mathfrak p$，其约化为
$63^{(\mathrm N\mathfrak p-1)/3}$；
(18) 的 x 坐标 Galois 因子是该符号的平方，准确给 (19) 的逆。
因此没有猜测有限角色方向。

这个 Kummer 角色的全有限导子可直接证明。
在二处，63模2等于1，且3是单位，Hensel 给63的局部立方根；
所以 twist 在 K₂ 平凡，原 ψ₁ 的二处导子 (2) 保持。
在两个7处，63的赋值均为一，三次 Kummer 扩张 tame 全分歧，
角色导子各为一。
在 δ 处，令 $\varpi_L=u/\delta$，则
$$
 \varpi_L^3=7\delta.
 \tag{20}
$$
这是 Eisenstein 三次式；$\varpi_L$ 为局部整环的统一化元，
其 different 指数为
$v_L(3\varpi_L^2)=6+2=8$。
循环三次扩张的两个非平凡角色有同一 conductor，
different–conductor 公式遂给每个 conductor 指数四。
ψ₁ 在 δ 处的指数一不能抵消此更深角色。
因此
$$
 \boxed{\mathfrak f(\psi_E)=(2\cdot7\cdot\delta^4),\quad
 \mathrm N\mathfrak f=15876,\quad
 \operatorname{cond}(E/\mathbf Q)=3\,\mathrm N\mathfrak f=47628.}
 \tag{21}
$$
最后一式是原 CM Tate 表示从 K 诱导到 Q 的 conductor 公式；
其二次域 discriminant 的绝对值为3。
(19) 与无穷 type 固定整个 Hecke 角色，不只是以下三个好位值。
本篇没有据 (21) 自动宣称某个 theta 空间的 Schwartz 向量已经匹配。

## 6. R1037 的准确候选标签与尚待真实来源的一步

用 R1037 原生成元
$\gamma_{13}=(7+\delta)/2,\gamma_{19}=4+\delta,
\gamma_{31}=(11+\delta)/2$。
R302 的 $\psi_1(\gamma)/\gamma$ 依次为
$-\omega^2,1,\omega^2$。在对应三个 residue embedding 中，
63分别为11、6、1，其三次符号依次为 $\omega^2,\omega^2,1$。
所以 (19) 准确给
$$
 \left(\frac{\psi_E(\gamma_{13})}{\gamma_{13}},
       \frac{\psi_E(\gamma_{19})}{\gamma_{19}},
       \frac{\psi_E(\gamma_{31})}{\gamma_{31}}\right)
       =(-1,\omega,\omega^2).
 \tag{22}
$$
这些值的有理 traces 为 $(-7,-7,-4)$，但 (22) 的证明使用完整
twist 公式，未从三个 trace 反猜角色。
令 $\zeta_6=-\omega$，代 R1037 的原三个生成算子词，
得到候选
$$
 \boxed{(A,C,H)=(\zeta_6^5,\zeta_6^4,\zeta_6^2).}
 \tag{23}
$$
这个候选在 H 的线性部分；它的三处导子指数四与 R1037 的较低
27-Weil/δ-old 范围相容。**相容不是实际投影已非零。**
完整 degree378 谱现已在 R1037 §9 实际返回：该块秩一、整质量行零、
规范向量首阶六，两个原输入及其差的全投影均非零。全部有限 Schwartz
向量和同一 Gaussian/frame 的识别仍须完整支付，不能只由该候选标签跳步。

只有完成该来源识别，才可按已登记的原全权平方与 ordinary/signed
插值、通常全 Selmer 比较，建立它自己的 $J_E$；
本篇不把 (3) 直接变成一个尚未识别的 $J$ 的零值或导数条件。
尤其不由原两 rank-two 来源除以 $B_{12}$ 推出各商分量的中央零。
主目标要求的无穷 p 非零仍是后继必须证明的算术结论。

## 7. 出处与候选资料的实际使用范围

点的搜索线索来自 John Cremona 的原始 ecdata，
不是对数据库 rank 标签的引用证明。实际读取的
[allcurves.40000-49999](https://github.com/JohnCremona/ecdata/blob/master/allcurves/allcurves.40000-49999)
blob 为73e27153202034d16c8d003208753490e5c236a7；
[allgens.40000-49999](https://github.com/JohnCremona/ecdata/blob/master/allgens/allgens.40000-49999)
blob 为f040d40620753827740e062d81842b87c9c263cc。
其确切模型行是
$$
 47628c1:[0,0,0,0,-147],\qquad
 47628c2:[0,0,0,0,3969].
$$
本篇全部点、同源、立方类与独立性已在 (1)–(17) 逐式证明；
数据库中的秩字段和解析数据均未作为输入。

实际参考来源与 CM 规范：
[R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)；
新完整有限谱与原商：
[R1037](R1037-original-degree378-full-finite-spectrum.md)。

2026-11-27 09:29 UTC 根审：已独立读取上述两个原始 blob 的47628c行，模型与P、R、T坐标相符；秩、三同源/Kummer、三处局部导子及(22)的原三次符号均由本文手证，没有执行数学程序或引用数据库rank作为证明。


## 8. 全部坏位单位、uniformizer 与原 Hermitian 类

以下使用 R389 的算术 Frobenius reciprocity 和 R302 的
$\chi_1=\psi_1|\cdot|^{-1/2}$ 规范。
令 $\vartheta_a(t)=\operatorname{rec}(t)(a^{1/3})/a^{1/3}$。
在三处，(20) 给 $\vartheta_{63}=\vartheta_{7\delta}$。
记
$$
 g=1-3\delta,\qquad
 u=q\omega^j g^k\bmod9,\quad
 q\in\{1,2,4,5,7,8\},\quad0\le j,k\le2.
 \tag{24}
$$
R389 已逐项证明这给全部54个单位，且
$\vartheta_\delta(u)=\omega^k$、$\vartheta_\delta(\delta)=1$。

### 8.1 新因子 $\vartheta_7$ 的完整方向

$\vartheta_7$ 在有理三进单位上平凡。确切理由是复共轭固定
$7^{1/3}$ 并反转 $\mu_3$，局部 reciprocity 相容性给
$\vartheta_7(\bar t)=\vartheta_7(t)^{-1}$；对有理 t，
其值同时有阶除二与除三，故为一。

在两个7素理想，7的赋值都是一。算术 reciprocity 的 tame 公式是
$$
 \vartheta_{a,\mathfrak q}(t)=
 \left((-1)^{v(a)v(t)}
       \frac{a^{v(t)}}{t^{v(a)}}\bmod\mathfrak q\right)^{2},
 \qquad \mathrm N\mathfrak q=7.
 \tag{25}
$$
特别对单位 $\omega$，两处各给 $\omega^{-2}=\omega$。
二处7为局部立方，其他有限点无贡献，主 idèle 积因而准确给
$\vartheta_{7,3}(\omega)=\omega$。

对 g，写 $g=-2h$、$h=1+3\omega$、$h\bar h=7$。
在 $(h)$ 处 $\omega=2$，(25) 的值为
$(\bar h/2)^2=3^2=2=\omega$；
在 $(\bar h)$ 处 $\omega=4$，g为单位且值为
$g^{-2}=2=\omega^2$。两者乘积为一，故
$\vartheta_{7,3}(g)=1$。
同样，$\bar\delta=-\delta$ 且 $-1$ 为立方，前面的共轭关系迫
$\vartheta_{7,3}(\delta)=1$。
于是全三处角色是
$$
 \boxed{\begin{aligned}
 \vartheta_{7\delta}(q\omega^j g^k)&=\omega^{j+k},&
 \vartheta_{7\delta}(\delta)&=1,\\
 \chi_{E,3}(q\omega^j g^k)&=
        \varepsilon(q)\omega^{-j-k},&
 \chi_{E,3}(\delta)&=i,
 \end{aligned}}
 \quad
 \varepsilon(q)=q\bmod3\in\{\pm1\}.
 \tag{26}
$$
(26) 包含全部54个单位及统一化元，不由三个好位读取反猜。

### 8.2 二、七处的原完整数据

二处 twist 是局部立方，故
$\chi_{E,2}(u)=\operatorname{Teich}_{\mu_3}(u\bmod2)$、
$\chi_{E,2}(2)=-1$。

令 $\gamma_7=(5+\delta)/2=3+\omega$，
$\mathfrak q=(\gamma_7)$、$\bar{\mathfrak q}=(\bar\gamma_7)$。
在两 residue embedding 中，$\delta$ 分别为2、5，$\omega$ 分别为4、2。
由 (25) 取逆，七处单位角色在各自嵌入中都是 $u^2$。
主 idèle 公式另外准确给
$$
 \boxed{\chi_{E,\mathfrak q}(\gamma_7)
       =\omega^2\gamma_7/\sqrt7,\qquad
 \chi_{E,\bar{\mathfrak q}}(\bar\gamma_7)
       =\omega\bar\gamma_7/\sqrt7.}
 \tag{27}
$$
例如 $\gamma_7\bmod9=4\omega g^2$，所以 (26) 给三处单位值1；
二处值为 $\omega^2$，另一7处的单位值也是 $\omega^2$。
其乘积为 $\omega$，再保无穷分量 $(\gamma_7/|\gamma_7|)^{-1}$，
正好得到 (27) 第一式。第二式共轭。
全局 $\delta$ 的两个7单位值为 $\omega,\omega^2$，乘积一，
与 (26) 的 $\chi_3(\delta)=i$ 相容。

### 8.3 原 Gauss 和及全局类

保持 $\psi_{\mathrm{add},3}(t)=e^{-2\pi i\{t\}_3}$、
$\psi_K=\psi_{\mathrm{add}}\circ\operatorname{Tr}$。
三处 Tate 参数为 $c=\delta^5=9\delta$。
对 $u=A+B\delta$ 有
$\operatorname{Tr}(u/(2c))=B/9$。
取 $\zeta=\zeta_9$，由 (24)–(26) 得
$$
 G_3=\sum_{q,j,k}\varepsilon(q)\omega^{j+k}\zeta^{-B(q,j,k)}
     =-9.
 \tag{28}
$$
这里无需数值求和：三类 j 的 B 分别是
$-3qk,\ q(5-3k),\ q(4-3k)\bmod9$。
k求和只留下 $q=2,5,8$，每个系数为 $-3$。
j=0 的总和是−9；j=1、2 各是三个相隔三次幂的
$\zeta$ 项之和，故为零。$\chi_3(c)=i$，归一因子9，所以
$\epsilon_3(\chi_E,\psi_K/2)=-i$，再乘 $\chi_3(\delta)=i$ 得 +1。

二处是 R302 的原 +1；split 七处两个 epsilon 的积是
$\chi_{\mathfrak q}(-1)=1$，其 Hermitian 二次条件本来平凡。
其他好位也为正；无穷处仍为解析 CM type，其 epsilon 为 i。
因此全根数为 +1，而全部局部 dichotomy 对应
$$
 \boxed{\alpha_{\mathrm{Hermitian}}\in[1].}
 \tag{29}
$$
这里 [1] 是 $K/\mathbf Q$ 范数商中的类；
选 $\alpha=1$ 具体支付下节向量，不把它与最小 degree126/378 frame
的尚待完整识别混为一谈。

## 9. 原 conductor-four 三处 Schwartz 的完整新向量

本节在 (29) 的实际代表 $\alpha=1$ 上，复用 R391 的原九维
Schrödinger 模型和真实 Gaussian：
$$
 e_a=\mathbf1_{a/9+\mathbf Z_3},\qquad
 V=\mathcal S(3^{-2}\mathbf Z_3/\mathbf Z_3),\qquad
 \operatorname{vol}(\mathbf Z_3)=1 .
 \tag{30}
$$
仍取整个 torus 的拓扑生成元
$-1,\omega,g_*=(1+3\delta)/(1-3\delta)$。
R391 的 Rao 核不变；把 (26) 代入其完整 splitting，得到
$$
 \mu_E(\omega)=\mu_E(-\omega)=-i\omega,\qquad
 \mu_E(g_*)=\omega.
 \tag{31}
$$
例如 $\delta(\omega-1)=3\omega^2$ 的角色值为 $\omega$；
$\delta(-\omega-1)=\delta\omega^2$ 的值为 $i\omega$，
分别连原 Weil/Hilbert 因子便得 (31)。
$g_*$ 对应的 $\delta(g_*-1)=-9(1+3\delta)/14$ 与旧
R391 相同，因为新 $\vartheta_7$ 在此单位为一。

故 $g_*$ 的全部九列仍是
$\omega^{1-a^2}e_a$，负号仍是反射 $a\mapsto-a$。
整个不变向量只能在
$\langle e_1+e_{-1},e_2+e_{-2},e_4+e_{-4}\rangle$。
在此有序基，R391 的完整旧矩阵为
$$
 M=\frac1\delta
 \begin{pmatrix}
 \zeta^8&\zeta^5&\zeta^8\\
 \zeta^5&\zeta^5&\zeta^2\\
 \zeta^8&\zeta^2&\zeta^2
 \end{pmatrix},\qquad M^3=I,\quad M^* =M^2,\quad\operatorname{Tr}M=0 .
 \tag{32}
$$
新 $\omega$ 矩阵准确是 $\omega M$，不是任换旧不变线。
于是新向量为
$$
 \boxed{\begin{aligned}
 f_1&=3-\delta(\zeta^2-\zeta^7),\\
 f_2&=\delta(\zeta-\zeta^8),\\
 f_4&=-\delta(\zeta^2-\zeta^7),\\
 \phi_{E,3}&=f_1(e_1+e_{-1})+
             f_2(e_2+e_{-2})+f_4(e_4+e_{-4}).
 \end{aligned}}
 \tag{33}
$$
确切地，$f=3(I+\omega M+\omega^2M^2)(1,0,0)^{\mathsf t}$。
(32) 给 $\omega Mf=f$，再用 (31) 的另两生成元，证明它被
整个原 torus 固定。

所有坐标实，因为 $\bar\delta=-\delta$、
$\bar\zeta=\zeta^{-1}$。
在整数基 $1,\zeta,\ldots,\zeta^5$ 中，首坐标是
$3+\zeta-\zeta^2-\zeta^4-2\zeta^5$，非零；
这是 degree6 最小多项式 $\zeta^6+\zeta^3+1=0$ 下的准确余式。
正交投影 $\Pi=(I+\omega M+\omega^2M^2)/3$ 给 $f=9\Pi e_1$，故
$$
 \boxed{f_1^2+f_2^2+f_4^2=9f_1,\qquad
        \|\phi_{E,3}\|^2=18f_1>0.}
 \tag{34}
$$
这已经支付真实 wild 原向量、相位、支撑和范数。
R1037 §9 已独立返回真正的 degree378 完整谱和原两输入系数；
本节没有用局部向量存在预填该计算。全局 Gaussian/frame 及其余局部
向量仍须与这个实际完整块对齐。

本节直接使用 R391 已完整给出的核和矩阵，未重做已登记的旧结论。
新步骤是 (26)、(31) 的角色差以及 (33) 的真正新不变线。
原 splitting 的发表来源仍为 Yang 1999 Appendix (A1)–(A3)；
[作者全文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)，
本次已重新读取原局部角色与 lattice-to-Schrödinger 条件。
