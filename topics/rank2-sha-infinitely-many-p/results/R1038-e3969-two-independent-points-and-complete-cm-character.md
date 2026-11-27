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

## 10. 同一个 Hermitian 类的最小 degree126 frame

固定真正的代表和全局尺度
$$
 \alpha=1/7=N_{K/\mathbf Q}(\gamma_7^{-1}),\qquad
 \kappa_\infty=|\delta^3\alpha|=3\sqrt3/7 .
 \tag{35}
$$
这与 (29) 同类，却不是保持 Gaussian 不变时改支撑。
原嵌入始终是
$\iota_\alpha(x+y\delta)=
\left(\begin{smallmatrix}x&9\alpha y\\-y/(3\alpha)&x\end{smallmatrix}\right)$。

### 10.1 二处完整相位与实际负系数

用 R302 的四陪集 $e_j=\mathbf1_{j/2+2\mathbf Z_2}$，
$f_A=e_0-e_2,f_B=e_1+e_3$。
$\alpha\equiv7\bmod8$，且 $\alpha/(-1)$ 是二进平方，
故原 Weil 指数是 $\alpha=1$ 的共轭；Hecke 因子仍是
$\omega^2$，不能也一并共轭。令 $\zeta_8=e^{\pi i/4}$，准确有
$$
 \mu(\omega)=-\omega^2\zeta_8^{-1},\qquad
 \mu(g_*)=\mu(-g_*)=\zeta_8^3,\quad g_*=(-11+4\delta)/13 .
 \tag{36}
$$
完整核在输出 $b/2$、输入 $a/2+2\mathbf Z_2$ 的项为
$\mu(\omega)(2\sqrt2)^{-1}
 \zeta_8^{-3\alpha(a^2+b^2-4ab)}$。
四分之一环带外支撑逐项相消；在 $(f_A,f_B)$ 上得到
$$
 M_{\omega,2}=-\frac{\omega^2\zeta_8^{-1}}{\sqrt2}
 \begin{pmatrix}1&\zeta_8^3\\ \zeta_8^3&i\end{pmatrix}.
 \tag{37}
$$
置 $t_-=(\sqrt3-1)/\sqrt2$，直接代入给
$M_{\omega,2}(1,-t_-)^{\mathsf t}=(1,-t_-)^{\mathsf t}$。
$g_*$ 的四个非零项仍为 $a=3b+2\bmod4$ 及相位
$(-1,1,-1,1)$；这是 (36) 与原核整体共轭的结果。
$-1$ 为反射。这些生成整个 $K_2^1$，故
$$
 \boxed{\phi_{E,2}=f_A-t_-f_B,\quad
 v_2=(1,-t_-,-1,-t_-),\qquad n_2=3-\sqrt3.}
 \tag{38}
$$
负号属于原向量，不能从 R959 的 $+t_-$ 搬用。

### 10.2 野三处的真实单位缩放

在 $\mathbf Q_3$ 取 $s_3^2=1/7$、$s_3\equiv7\bmod9$。
原 Schrödinger 单位变换为
$$
 \phi_{E,3}^{(\alpha)}(x)=\phi_{E,3}^{(1)}(s_3x).
 \tag{39}
$$
它将完整积分核共轭；平方缩放不改 Weil 指数，且 $|s_3|_3=1$，
所以范数仍是 $n_3=18f_1$。
若 $x=n/18$，则 $9s_3x\equiv8n\bmod9$。
(33) 向量偶，此处准确读取 $v_3(n)$，其中
$v_3(\pm1)=f_1,v_3(\pm2)=f_2,v_3(\pm4)=f_4$，三的倍数处为零。

$f_1$ 是 R393(13) 原整数的 $\zeta_9\mapsto\zeta_9^2$ 共轭，故
$$
 f_1^3-9f_1^2+18f_1-9=0,\qquad
 N_{\mathbf Q(\zeta_9)^+/\mathbf Q}(f_1)=9.
 \tag{40}
$$
没有引入随权或随 p 变化的归一分母。

### 10.3 分裂七处的完整 isometry、投影与 Haar

固定 $\delta_0^2=-3,\delta_0\equiv2\bmod7$。
两 split 支按 (27)，令 $\vartheta(u)=u^2\bmod7$ 的 $\mu_3$ 提升。
Yang 1997 (2.28) 的原 isometry 是
$$
 \rho_\alpha\phi(a)=|A|^{1/2}\psi_7(Aa^2/2)
 \int\psi_7(Aab+Ab^2/4)\phi(b)\,db,\qquad
 A=\delta_0^3/7,\quad7A\equiv1\bmod7 .
 \tag{41}
$$
将自然向量 $\vartheta^{-1}\mathbf1_{\mathbf Z_7^\times}$ 代入，
输出支撑恰在 $\mathbf Z_7$、以 $7\mathbf Z_7$ 为周期；
七个完整坐标为
$$
 7^{-1/2}\zeta_7^{3a^2}
 \sum_{b\in\mathbf F_7^\times}\vartheta(b)^{-1}\zeta_7^{5b^2-ab}.
 \tag{42}
$$
每个基 $e_a^{(7)}=\mathbf1_{a+7\mathbf Z_7}$ 的范数平方为 $1/7$。

在 $T_7=\{x+y\delta:x^2+3y^2=1\}$ 上，原有限模型是
$$
 W_7(g)_{ab}=\frac{i(\frac y7)}{\sqrt7}
 \zeta_7^{5\{x(a^2+b^2)-2ab\}/y}\quad(y\ne0),\qquad
 W_7(-1)e_a=-e_{-a}.
 \tag{43}
$$
绝对 i 由完整有限 Gauss 合成确定：
$\sum_b\zeta_7^{cb^2}=i(\frac c7)\sqrt7$，所以 prefactor 必须是
$i^{-1}(\frac{3/2}7)(\frac y7)=i(\frac y7)$。
特别这里是负反射，不能抄十三处正反射。

写 $t=x+2y$。自然 quadratic splitting 为 $t^3$，
实际单位角色为 $t^2$，故有限特征是 $\tau_7(t)=t$，
不是重数二的 quadratic 角色。
取 $g_0=(4,3)$，$t=3$ 对应 $\zeta_6=-\omega$，令
$\Pi_7=6^{-1}\sum_{j=0}^5\zeta_6^{-j}W_7(g_0^j)$。
四个非中央幂的 $5x/y$ 为 $2,5,2,5$，
Legendre 符号为 $-,-,+,+$。完整投影给
$$
 \boxed{\begin{aligned}
 f_7(a)&=3\sqrt7(\Pi_7e_0)(a)
 =\sqrt7\mathbf1_{a=0}
   +i(\omega^2\zeta_7^{2a^2}-\omega\zeta_7^{-2a^2}),\\
 f_7(0)&=\sqrt7+\sqrt3,\qquad
 n_7=\left\|\sum_af_7(a)e_a^{(7)}\right\|^2
      =3(7+\sqrt{21})/7 .
 \end{aligned}}
 \tag{44}
$$
它实、偶、非零；范数由正交投影及实际 $1/7$ Haar 得到。
(41) 与 (44) 在同一重数一有限线上。
非紧 uniformizer 仍移到不交环带，不能声称逐向量固定。

Yang Corollary2.13 的单位范数陪集
$\sqrt7\mathbf1_{1+7\mathbf Z_7}$ 经六个紧单位平均，
平方范数成为 $1/6$；归一后 theta 积分平方多六。
因此原因子 $7/36$ 准确变为
$$
 \boxed{c_7(0)=7/6.}\tag{45}
$$

### 10.4 完整 CRT、half-period 和 Gaussian

其余有限点取原标准球。有理支撑恰为 $x=n/18$，且
$$
 \boxed{a_n=v_2(n\bmod4)v_3(n\bmod9)f_7(2n\bmod7).}
 \tag{46}
$$
二处用 $9^{-1}=1\bmod4$，三处用 (39)，七处用
$18^{-1}=2\bmod7$。全部系数实、偶，并满足
$$
 a_{n+252}=a_n,\qquad(-1)^na_{n+126}=-a_n.
 \tag{47}
$$
三个非零局部支撑经 CRT 同时达到，所以全序列非零。

保持 $\Lambda=\mathbf Z+s_0\mathbf Z$、
$s_0=(1-\omega)^{-1}$，定义
$$
 F(Z)=\sum_na_ne^{\pi i(\delta/3)n^2/252+2\pi inZ},\qquad
 S_{\rm raw}(Z)=e^{126\sqrt3\pi Z^2}F(Z).
 \tag{48}
$$
完整换指标给
$F(Z+1)=F(Z)$、
$F(Z+s_0)=e^{-126\pi is_0-252\pi iZ}F(Z)$。因此
$$
 S_{\rm raw}\in H^0(\Lambda,\mathcal O(126O)),\quad S_{\rm raw}\ne0,
 \tag{49}
$$
无额外 flat characteristic。令
$b_m=\sum_na_nH_m(\sqrt\kappa n/18)e^{-\pi\kappa n^2/18^2}$、
$h=\sqrt\kappa/(36\pi i)$，原 Hermite 生成式给
$$
 \sum_mb_mT^m/m!=S_{\rm raw}(hT),\qquad
 126\sqrt3\pi h^2=-1/(8\pi).
 \tag{50}
$$
完整有限不变性与全局 $\mu_6$ 给 $b_m=0$ 当 $6\nmid m$。
所以原来源在整个 principal 空间
$\sigma^{126}\mathbf C[X]_{\le21}$ 中。

## 11. 全权实平方与原378实际线的唯一匹配

对 $6\mid m$，(26)、(27) 的所有坏单位角色保持，
二、三的 uniformizer 也保持。
split 七处非紧参数随权变化，但单位环带及非零赋值矩阵系数为零
的事实不变；同一个完整有限 Schwartz 适用于全部这些权。

置
$$
 c(0)=(1+2^{-1})^{-1}(1-7^{-1})^{-1}=7/9,\qquad
 \mathcal N_m=\frac{n_2n_3n_7}{\sqrt{2\kappa}}\frac{m!}{(4\pi)^m}.
$$
三处扩张本身分歧，不属于 Yang Theorem1.11 的未分歧坏集合
$S_1$，不因导子四另添三处费用。类数一与完整根单位群给体积比六。
原范数公式与 (45) 准确给
$$
 \boxed{\begin{aligned}
 L(\psi_E^{2m+1},m+1)&=C_E\frac{(4\pi)^m}{m!}b_m^2,\quad6\mid m,\\
 C_E&=\frac{2}{6c(0)}\frac{\pi}{3\sqrt3}
          \frac{\sqrt{2\kappa}}{n_2n_3n_7}>0 .
 \end{aligned}}
 \tag{51}
$$
这是同一实来源的完整平方。已证秩下界与 CM rank-zero
定理的逆否命题给 $L(E,1)=0$，故 $b_0=0$；原来源至少六阶。

令 $\Omega_E\Lambda$ 为 E 对 $dx/(2y)$ 的实际周期格。
固定正实 $\theta^6=3969$，$\Omega_E=\Omega_1/\theta$；
不省微分缩放。由全部坏角色、原 theta-group 作用和 R400 的
整平方—整测度比较，原算术线的三个完整好位本征值是
$$
 (\mathscr N_{13},\mathscr N_{19},\mathscr N_{31})
       =(-1,\omega,\omega^2).
 \tag{52}
$$
这里先有完整 bad Schwartz；(52) 本身不承担算术命名。

这里的十三、十九、三十一处只用
[R400 的全测度平方刚性](R400-full-square-interpolation-determines-core-and-e24-cmseven-phase.md)，
不借用 §12 中 $p>211$ 的通常 Selmer 范围。
具体地，因 $b_0=0$ 而整个来源非零，取一个正权
$m_0\in6\mathbf Z$ 使 $b_{m_0}\ne0$。保持 (50) 的 $h$ 和阶乘，置
$$
 t_m=\frac{b_m}{m!\,h^m\Omega_E^m}.
$$
由 (51) 和 CM 临界值代数性，$(t_m/t_{m_0})^2$ 为代数数，
故各 $t_m/t_{m_0}$ 本身为代数数。有限个 Taylor 坐标确定
整个 degree126 多项式，遂先得到一条代数线。
再乘一个固定非零代数标量，清这三个普通处的有限个系数分母；
这个标量允许为非单位，R400 的全 core 身份线性齐次，仍可应用。
这一顺序不借尚未匹配出的分母91、首六阶或其具体坐标。


R1037 §9 全64列回执给 (52) 的共同块秩一，
label 为 $(5,4,\mathrm{linear},2)$，完整质量行零，
$\delta$ 层 $[0,1,0,0]$、dyadic 层 $[0,1]$、7-old交为零。
原 $[\delta]^*$ 与三个完整算子交织且单射，
故 (49) 的拉回必是这条实际非零线。
回执还返回首六阶与全部有理坐标，不据维数猜首阶。

定义两条首 $z^6$ 系数为一的规范来源，准确有
$$
 \boxed{\Phi_{378}(z)=\delta^{-6}\Phi_{126}(\delta z)
             =-\Phi_{126}(\delta z)/27.}
 \tag{53}
$$
$\Phi_{378}=\sigma^{378}P_{378}(X)$ 的全64坐标来自
run45973650826 / job140419911466 的唯一
R1037_COMPLETE_MASS_ZERO_CANONICAL 原记录；
向量 SHA256 为
5d578c544bb1e01467c49837f1c579c172a014376e969fcc868ea458409c2b7b。
其 $X^{63}$ 系数零、$X^{62}$ 系数一、最小公分母91。
两个原 quotient 及其差的实际完整投影是
$$
 \boxed{\Pi_EF_{378,A}=-\frac{185328}{35}\Phi_{378},\quad
 \Pi_EF_{378,B}=-\frac{160056}{835}\Phi_{378},\quad
 \Pi_E(F_{378,A}-F_{378,B})=-\frac{29829384}{5845}\Phi_{378}.}
 \tag{54}
$$
三者均非零，不将除 $B_{12}$ 的操作当作中央同态。

对任意 $b\ne0$，完整物理齐次式是
$$
 \Phi_{378,b}=\sigma_b^{378}\sum_{j=0}^{62}c_jb^{62-j}x_b^{3j}
            =b^{-1}\Phi_{378,1}(b^{1/6}z).
 \tag{55}
$$
物理值 $b=3969$，共同模型可取原 $b=17$，均保持整个式子。
置 $\widehat\Phi=91\Phi_{378}$。由 (50)–(53) 与
$\varpi_E=s_0\Omega_E$，有固定非零代数数 $\widehat\kappa_E$ 使
$$
 \boxed{\mathscr E_{E,m}:=
 \frac{(2\pi/\sqrt3)^mL(\psi_E^{2m+1},m+1)}
 {m!\varpi_E^{2m+1}}
 =\frac{\widehat\kappa_E}{s_0}378^{-m}\widehat s_m^2,\quad6\mid m,}
 \tag{56}
$$
其中 $\widehat\Phi_{378,3969}=\sum_m\widehat s_mz^m$。
若 $S_{\rm raw}(Z)=C_{\rm raw}\Phi_{126,3969}(\Omega_EZ)$、
$\kappa_{126}=C_EC_{\rm raw}^2/\Omega_E$，则
$$
 \widehat\kappa_E=729\kappa_{126}/91^2 .
 \tag{57}
$$
$729=\delta^{12}$ 来自 (53)。实际首个非零系数 m=6 与
CM 临界值代数性付 $\widehat\kappa_E\in\overline{\mathbf Q}^{\times}$，
其有限赋值始终保留，不逐权选平方根或删固定非单位。

## 12. 新曲线自己的普通与惰性通常全 Selmer 桥

逐项应用 [R970 §6](R970-original-e65-cube-rank2-degree130-source-and-central-bridge.md)、
[R973 §6](R973-original-degree130-arithmetic-spectrum-and-e260-source.md) 及
[本会话已审 mixed-period note](../notes/2026-11-27-mixed-weight-period-audit-and-height-difference-scope.md) 的完整证明，不以新谱代替 Selmer 定理。ray conductor 为 $(126)$，
射线次数准确是
$$
 [K(126):K]=\frac{(4-1)(81-27)(7-1)^2}{6}=972=2^2 3^5 .
 \tag{58}
$$
原 E1 参考只新增七处去因子。写
$\rho=\psi_1((\gamma_7))=\omega\gamma_7=-2+\delta$，
$\rho\bar\rho=7,\rho+\bar\rho=-4$，完整因子为
$$
 E_7(m)=(1-\rho^{2m+1}/7^{m+1})
        (1-\bar\rho^{2m+1}/7^{m+1}).
 \tag{59}
$$
在普通 $p-1\mid m$ 或惰性 $p+1\mid m$ 整支上，
$E_7(m)\equiv E_7(0)=12/7\bmod p$，所以 $p>211$ 时为单位；
仍保其整个随权函数。野三处用 (26)、(33)、(39)、(58)，
不能复制旧 E17 的导子一角色。

### 12.1 普通

固定坏集之外，$p>211,p\equiv1\bmod3$。
(55) 每项原点阶 $378-6j\ge6$，
固定分母91和 CM sigma 整性给有界整测度。
在同一原单位 cut 和相容单位周期下写 Mellin 为
$\widehat G_{E,p}(T)$。
两个真实 Katz 因子均为
$1-\pi_p^m/\bar\pi_p^{m+1}$，$\pi_p=\psi_E(\mathfrak p)$。
由 (56) 的原单位矩极限，准确有
$$
 \mathcal K_{E,p}(T)=\frac{\widehat\kappa_E}{s_0}\Omega_{p,E}
 (1+T)^{-\log_p\langle378\rangle/\log_p(1+p)}
       \widehat G_{E,p}(T)^2 .
 \tag{60}
$$
同一分支中央插值与 $L(E,1)=0$ 给
$\widehat G_{E,p}(0)=0$，不是由全质量零偷推单位质量零。

Agboola–Howard 的通常单 CM Selmer 比较、原基层控制与
$\mathbf Q$ 二次分解适用：最大整环 CM、正根数、好普通、
$p\nmid972$ 均已支付；辅助好惰性11的中心因子 $-132$ 为单位。
保 primitive 2、3、双7及实际 period，若
$r=\operatorname{rank}E(\mathbf Q)$、
$r_p=\operatorname{corank}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]$，则
$$
 \boxed{r+r_p\le2\operatorname{ord}_0\widehat G_{E,p},\qquad
 \widehat G'_{E,p}(0)\ne0\Longrightarrow
 r=2,\ \Sha(E/\mathbf Q)[p^\infty]\text{ 有限}.}
 \tag{61}
$$

### 12.2 惰性与完整 period 比

令 $p=6s-1>211,d=p+1$，同一 E1 上取
$c=[z^d]\log(\sigma/z)$，$v_p(c)=-1$。定义整个 Newton 来源
$$
 a_h=(378c)^{-h}[z^{dh}]
       (\widehat\Phi_{378,1}e^{-378cz^d}),\qquad
 \widehat J_{E,p}(v)=\sum_{h\ge0}a_h(v)_h .
 \tag{62}
$$
原严格圆盘/Hurwitz 估计逐项给
$$
 v_p(a_h)\ge\left\lceil\frac{h(p-1)+6}{2p}\right\rceil,\qquad
 \widehat J_{E,p}\in pv\mathcal O\langle v\rangle,\qquad
 \widehat J_{E,p}(k)=k!(378c)^{-k}[z^{dk}]\widehat\Phi_{378,1}.
 \tag{63}
$$
原整同构微分为 $F_\theta^*\omega_E=\theta^{-1}\omega_1$、
$\theta^6=3969$。Gaussian 同时变成 $\theta^dc$，
Newton 中的 $\theta^{dh}$ 全消；物理半因子为
$3969^{-1}\widehat J_{E,p}$，共同 E17 模型为
$17^{-1}\widehat J_{E,p}$。

R303/R943 完整 BKO signed 格与同一椭圆单位类给
$0\ne\mathcal A_{E,p}\in\mathcal O[[T]]$。
新增 finite 费用是 (26)–(45)、(58)、(59)；
同阶 Tate/Gamma、阶乘、p处 $1+1/p$ 只在准确比中消，
不能单称为单位。
Kato Lemma15.11 的两个已定义图、(15.16.1) 与
Theorem12.5(1) 的逐权 pullback 按原 audit 消去共同秩一标量；
不用“由同一 motivic 图诱导”的未证加强。
因此每个允许权有原赋值身份，特别
$$
 \boxed{v_p\mathcal A_{E,p}(x_{dk})=
       v_p(\widehat\kappa_E)+2v_p\widehat J_{E,p}(k).}
 \tag{64}
$$
参考 $J_{0,p}\in1+p\mathcal O\langle v\rangle$；
(59) 在整支为单位，辅助好惰性 $\ell\equiv1\bmod p$ 的原因子
模 p 为2。全部新坏位与原 period 都保留。

沿 $k=p^n$ 比较 n 的系数，得
$\operatorname{ord}_0\mathcal A_{E,p}
=2\operatorname{ord}_0\widehat J_{E,p}$，
非零 $\mathcal A$ 亦排除 $\widehat J\equiv0$。
BKO Theorem6.2 的基层通常 Selmer 不等式在正号格给
$$
 \boxed{r+r_p\le2\operatorname{ord}_0\widehat J_{E,p},\qquad
 \widehat J'_{E,p}(0)\ne0\Longrightarrow
 r=2,\ \Sha(E/\mathbf Q)[p^\infty]\text{ 有限}.}
 \tag{65}
$$
这包括通常全群，不把 signed 挠性本身当作全 Sha 有限。

完整有限证书仍是
$$
 L_H=\sum_{h=1}^H(-1)^{h-1}(h-1)!a_h,\qquad
 M_H=\left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!),
$$
$$
 \widehat J'_{E,p}(0)\ne0
 \quad\Longleftrightarrow\quad\exists H:\ v_p(L_H)<M_H.
 \tag{66}
$$
(63) 给真实尾误差至少 $M_H\to\infty$。

最小 degree126 来源在同一特征零 Newton 插值上满足
$$
 J_{378}(v)=\delta^{-6}q_\delta^vJ_{126}(v),\qquad
 q_\delta=\delta^{p+1}/3\in1+p\mathcal O,\qquad
 j_{378}=-j_{126}/27 .
 \tag{67}
$$
普通原单位 cut 的 $[\delta]$ 推前同样保相应单位幂，
质量为零后首导数差恰为 $\delta^{-6}$。
这只支付两条原来源之间的零条件，不将 B12 商、任意乘子
或谱分量变成中央同态。

固定删集包括原通用比较的有限坏集、2、3、7、13及
(57) 固定归一的非单位素数，均不随权或 H 变化。
$n_2,n_3,n_7$ 的范数只涉及2、3、7，ray只涉及2、3。
本节因此给真正新增的固定 rank至少二曲线与全 Selmer 判据。
无穷多个 p 的联合中央非零仍要在原实际读者中证明；
(54) 的非零投影本身不承担该量词。



## 13. 原126的完整回乘、全部因子与确切六 sigma 来源

### 13.1 唯一原回执的实时消费

这里不重算 R1037 的有限谱。新的轻消费者先从公开 Actions 实时读取
run45973650826 / job140419911466，核 source22ac87ec033d658aa19b32d417c493f5748aa122、
原 request/script/三依赖/host/workflow 的完整绑定及 HOST_COMPLETE，
再核43787B报告、2892B唯一质量零记录和全部64坐标的哈希。
它没有把原输出坐标写进源码。

对 $0\le j\le21$，真正的规范 $\delta$ 拉回列是
$$
 -\frac1{27}\sigma(\delta z)^{126}x(\delta z)^{3j}
 =\sigma(z)^{378}E_j(X),\qquad
 E_j(X)=-\frac{(-3)^{63-3j}}{27}
        X^{42-2j}(X+4)^{3j}.
 \tag{68}
$$
这是 $\sigma(\delta z)=\delta\sigma(z)^3x(z)$、
$x(\delta z)=-(X+4)/(3x^2)$ 的整函数身份。
程序用全部22列求解，核秩22，并将所得向量重新乘回
**全部64个原坐标**。不是由最高22项或首几个 jet 判同。

实际成功回执为：

| 项目 | 实际值 |
|---|---|
| 新 run / job | 45977711940 / 140433521280 |
| 新 source | 311f91e77e8071abc6f55d889e8880931634600d |
| 脚本 | scripts/check-original-e3969-degree126-descent.py |
| 脚本 SHA256 | 69301ff117727e240e30a4b0d4fc01c902ea4d8064abdf4933f920964372024e |
| stdout 字节 / SHA256 | 9031 / 7db4f9ca3c0213b34fbb4d4c203562df5a3d8bb224fd7d1ea521494141a0cee1 |
| job log 字节 / SHA256 | 18319 / 1b0c92fc2ef97d0e60929a71c386a58c4eff6811fb6878a9dd922f106b16b548 |
| 完整126系数 SHA256 | 13d764a56c600c55af4a9d644f5bab5807a5ca490dae34f8d3b747322b650404 |
| 数学阶段秒数 | 0.8931892800000014 |

输出准确为 PASS_COMPLETE_E3969_DEGREE126_DESCENT。
完整22系数、因式、角多项式及三次角拉回都在同一个9031B原 stdout，
没有只返回摘要哈希，也没有省略原来源核验。

### 13.2 完整126分子

记
$$
 \begin{aligned}
 Q_7(X)&=7X^2-4X+16,\\
 C_3(X)&=X^3-96X^2+48X+64,\\
 D_{13}(X)&=13X^4+52X^3+1536X^2+1024X+256,\\
 S_7(X)&=X^6+564X^5-5808X^4-123136X^3\\
       &\hspace{20mm}-189696X^2-49152X+4096.
 \end{aligned}
 \tag{69}
$$
原实际分子完整等于
$$
 \boxed{
 \Phi_{126}=\sigma^{126}P_{126}(X),\qquad
 P_{126}=\frac1{91}X(X+1)(X+4)(X-8)^2
                   Q_7C_3D_{13}S_7 .}
 \tag{70}
$$
其次数20、首一、最小公分母91。公开消费者对 (70) 的完整乘积与
(68) 的全部坐标回乘分别核验。因此 (70) 是 (51)–(53) 的那条
实际算术来源，没有新增选择或投影。

原点展开还直接给
$$
 \Phi_{126}(z)=z^6+\frac{15836}{35}z^{12}+O(z^{18}),\qquad
 \Phi_{378}(z)=z^6-\frac{427572}{35}z^{12}+O(z^{18}).
 \tag{71}
$$
确切地，$P_{126}$ 的 $X^{19}$ 系数为 $3223/7$，
$\sigma/z=1+z^6/210+O(z^{12})$、
$x=z^{-2}-z^4/7+O(z^{10})$；
故第一系数是 $3223/7+126/210-60/7=15836/35$。
第二式按 (53) 全缩放，而非重新拟合。

### 13.3 固定除法多项式逐项证明六 sigma 身份

令
$$
 \pi=(7+\delta)/2=4+\omega,\qquad
 \bar\pi=(7-\delta)/2 .
$$
保 R961 原 CM division 相位
$$
 2\pi R_\pi=7X^2-4X+16+\delta(X^2+44X+16),\qquad
 \sigma(\pi z)=\pi\sigma(z)^{13}R_\pi(X).
 \tag{72}
$$
共轭式也保持原相位。完整乘法立即给
$$
 D_{13}=13R_\pi R_{\bar\pi}
       =\frac{(7X^2-4X+16)^2+3(X^2+44X+16)^2}{4},
 \quad
 \sigma(\pi z)\sigma(\bar\pi z)=\sigma^{26}D_{13}.
 \tag{73}
$$
因此四次因子并非由零点猜出。

对整数 division 多项式采用
$\sigma(nz)=(-1)^{n-1}\psi_n\sigma(z)^{n^2}$。
在 $y^2=x^3+1$ 上
$$
 \psi_2=2y,\quad \psi_3=3x(X+4),\quad
 \psi_4=4y(X^2+20X-8),\quad
 \psi_5=5X^4+380X^3-240X^2-1600X-256 .
$$
原完整递推给
$$
 \begin{aligned}
 \psi_7&=\psi_5\psi_3^3-\psi_2\psi_4^3\\
 &=27X(X+4)^3\psi_5
       -128(X+1)^2(X^2+20X-8)^3
 =Q_7S_7.
 \end{aligned}
 \tag{74}
$$
最后一步只是 (69) 的整数多项式乘法；例如两边完整展开均为
$$
 7X^8+3944X^7-42896X^6-829696X^5-928256X^4
 -1555456X^3-2809856X^2-802816X+65536 .
$$
故 $\sigma(7z)=\sigma^{49}Q_7S_7$。

另外，原三倍和 $\delta$ 图给
$$
 x(3z)=\frac{C_3(X)}{9x^2(X+4)^2},\qquad
 y(\delta z)=-\frac{y(X-8)}{3\delta X}.
$$
结合 $\sigma(3z)=3x(X+4)\sigma^9$、
$\sigma(2z)=-2y\sigma^4$ 与 (68)，准确得到
$$
 \begin{aligned}
 \sigma(3\delta z)&=3\delta\,\sigma^{27}x(X+4)C_3,\\
 \sigma(2\delta z)&=-2\delta\,\sigma^{12}xy(X-8),\\
 \sigma(2\delta z)^2&=-12\,\sigma^{24}x^2(X+1)(X-8)^2.
 \end{aligned}
 \tag{75}
$$
(73)–(75) 相乘，所有相位和常数均保，给出本节的新完整来源：
$$
 \boxed{\displaystyle
 \Phi_{126}(z)=
 \frac{\sigma(7z)\sigma(\pi z)\sigma(\bar\pi z)
       \sigma(3\delta z)\sigma(2\delta z)^2}{-3276\delta}.}
 \tag{76}
$$
六个实际轴是
$$
 a=(7,\pi,\bar\pi,3\delta,2\delta,2\delta),\qquad
 \sum_iN(a_i)=49+13+13+27+12+12=126,\qquad
 \prod_i a_i=-3276\delta .
 \tag{77}
$$
因此 (76) 的原点首项确为 $z^6$。
(76) 是同一完整来源的整函数身份，不只在某个商、某些 torsion 点
或有限阶 Taylor 窗内成立。其系数在 $91^{-1}\mathbf Z$；
固定好位 $p>211$ 的整性不新增坏素数。

### 13.4 原角的所有公共基点及精确适用范围

令 $\Theta=\sigma^2x$、$t=-1/X$，则
$\Phi_{126}=\Theta^{63}f_{63}(t)$。
完整原角为
$$
 \begin{aligned}
 f_{63}(t)=\frac1{91}&\,t(4t-1)(t-1)(7+4t+16t^2)(1+8t)^2\\
 &\cdot(-1-96t-48t^2+64t^3)\\
 &\cdot(13-52t+1536t^2-1024t^3+256t^4)\\
 &\cdot(1-564t-5808t^2+123136t^3-189696t^4
                    +49152t^5+4096t^6).
 \end{aligned}
 \tag{78}
$$
它的次数为20、首 $t$ 系数为−1。全部实际阶为：

| 原点或因子 | $0$ | $1$ | $-1/8$ | $1/4$ | $h_7=7+4t+16t^2$ | $\infty$ |
|---|---:|---:|---:|---:|---:|---:|
| $f_{63}$ | 1 | 1 | 2 | 1 | 1 | 极20 |
| $(1-4u)^{63}f_{63}(-27u/(1-4u)^3)$ | 1 | 1 | 2 | 3 | — | 极61 |

第二行的有限点按 $u$ 坐标读取。
三次拉回的完整系数哈希为
587989b2aecc2204b7cd227512b0e033aa8f646ac11772145573e6c4cdda38bd；
公开回执同时保全部62个系数。

这些阶说明新来源满足 R996 的旧公共除子和角帽：
权63的四个指定基点至少各一阶，$h_7$ 至少一阶，
$\deg f_{63}=20=\lfloor64\cdot63/195\rfloor$。
所以不能把它登记为旧正规化之外的额外角维数，
也不能把 R1030 三次域的物理矩阵秩相加。
实际新增内容是 (51)、(61)、(65) 已付的**另一条固定 rank至少二
算术来源**、(70) 的全部原坐标及 (76) 的真实六 sigma 输入。

后继可把它放入同一原 Gaussian/单位 cut 的必要行。
(76) 没有赋予各 sigma 因子的中央零，也没有将来源乘法、
$B_{12}$ 除法或角多项式线性代数变成中央泛函的乘法规则。
其无穷 p 的贡献仍须由完整物理矩阵和全部尾误差实际消费。
