# R858 — 原三个 Artin 部分的满三级 CM 垂直消失与泛纤维单射

日期：2026-11-16。**状态：下述 Chow、CM reciprocity 与泛纤维结论已证明。**

本篇保留 R857 的实际满三级三fold、整个 Scholl 对应、原端点循环以及全部有限 Artin 作用。新增结论是：在原三个十八阶角色及其逆角色的部分，R857 允许的全部垂直 CM 代表也严格消失。因此该部分的泛纤维限制是单射。

这不证明原端点循环或其泛纤维双点迹非零。R817 的固定素数7993检测的是 R814/R854 的 canonical cycles，未检测 R830/R831 修复后的另一端点循环；本篇不交换这两个对象。

## 1. 原对象与 point-factor 角色

固定
$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,\qquad
E_0:y^2=x^3+1,\qquad A=E_0^3.
$$
令 $\mathcal E$ 是包含原角色值与 $K$ 的固定系数域。所有 Chow 群均用有理系数再张量 $\mathcal E$。Galois 始终只作用于几何循环，**不作用于 $\mathcal E$ 中的标量**。

R806、R844 的三个原角色满足
$$
\eta_4=\eta^{13},\qquad \eta_{10}=\eta,\qquad
\eta_{16}=\eta^7,\qquad
\operatorname{ord}(\eta)=18.
\tag{1}
$$
它们均切出同一个实际 ring class field
$$
H_{34}/K,\qquad \operatorname{Gal}(H_{34}/K)\simeq C_{18},
\tag{2}
$$
在3处不分歧，而且 $\eta_j^2$ 的阶为9。本篇对
$$
\chi\in\{\eta_4^{\pm1},\eta_{10}^{\pm1},\eta_{16}^{\pm1}\}
\tag{3}
$$
同时成立，故不改变原 CM 型与逆角色的约定。

沿 R857，原满三级纤维为
$$
\mathcal E'_\tau:\quad
V^2+\tau UV+V=U^3-5\tau U-(\tau^3+7).
\tag{4}
$$
其实际全三挠标架已在 $K(\tau)$ 上逐点给出。记满三级自乘的标准大解消为
$$
\pi:W_3\longrightarrow\mathbf P^1_\tau.
$$
四个 cusp 为 $I_3$。采用同一个完整 Scholl 对应
$$
\varepsilon_3
=\frac{1-s}{2}\frac{1-\iota_1}{2}\frac{1-\iota_2}{2}
 \vartheta_1\vartheta_2,\qquad
\vartheta_i=\frac19\sum_{T\in\mathcal E'[3]}\tau_{T,i}.
\tag{5}
$$
这里 $s$ 交换两个椭圆因子；(5)不是在原模型上任择的裸八项表达。

R857 已付全 Chow 同构
$$
\Theta:(A,\Pi)\longrightarrow(W_3,\varepsilon_3),\qquad
{}^t\Theta\Theta=81\Pi,\qquad
\Theta{}^t\Theta=81\varepsilon_3.
\tag{6}
$$
$\Theta$ 包含原完整图形、解消和 Scholl 投影。所有例外分量与原次数规范均保留。

每个几何代数循环定义在有限域上，故 $G_K$ 在其有限 Galois 轨道张成空间上的作用因子化经过有限群。定义
$$
\operatorname{CH}^2(W_{3,\overline K})[\chi]
=\{z:\sigma z=\chi(\sigma)z\text{ 对所有 }\sigma\in G_K\}.
\tag{7}
$$
在一个足够大的有限 Galois 域上，(7)等价于实际有限幂等元
$$
e_\chi=\frac1{|\operatorname{Gal}(L/K)|}
\sum_{\sigma\in\operatorname{Gal}(L/K)}
\chi(\sigma)^{-1}\sigma.
\tag{8}
$$
扩大 $L$ 不改变它在原有限轨道上的作用。本篇仅使用这些有限平均，不作任何 $p$-adic 极限的 point-factor 投影。

## 2. 满三级的每个 order3 deck 平均在 Scholl Chow 动机上为零

固定 Weil pairing 后，三级基的改变给
$\operatorname{SL}_2(\mathbf F_3)$ 的实际作用。中心 $-I$ 在自乘上是同时逆
$\iota_1\iota_2$，在(5)的两反号部分上为恒等。因此它在
$(W_3,\varepsilon_3)$ 上下降为
$$
\operatorname{PSL}_2(\mathbf F_3)\simeq A_4.
\tag{9}
$$
所有基变换置换三挠平移，并与因子逆、因子交换相容，所以与(5)交换。标准大解消吹起完整节点集合，deck 作用随之延拓；也可在共同等变解消上取同一图形对应。

R857 的实际等变元为
$$
u=([\omega],1,1)\text{ on }A,
$$
$$
\sigma:\quad
(\tau,U_1,V_1,U_2,V_2)
\longmapsto
(\omega^2\tau,\omega U_1,V_1,\omega U_2,V_2)
\text{ on }W_3,
\qquad
\sigma\Theta=\Theta u.
\tag{10}
$$
$\sigma$ 是(9)中的非平凡三阶元。原两条 Chow CM 线上
$u$ 的特征为 $\omega,\omega^2$；因此作为真实 Chow 对应有
$$
\Pi(1+u+u^2)\Pi=0.
$$
由(6)、(10)，
$$
\boxed{
(1+\sigma+\sigma^2)\varepsilon_3
=\frac1{81}\Theta\Pi(1+u+u^2)\Pi{}^t\Theta=0.
}
\tag{11}
$$
这是完整 Chow 恒等式，不是从 Betti 维数单独猜出的消失。

$A_4$ 的四个三阶子群彼此共轭。因此对任意非平凡三阶 deck 元 $T$，
$$
\boxed{
\frac{1+T+T^2}{3}\,\varepsilon_3=0.
}
\tag{12}
$$
若选择了阶6的 $\operatorname{SL}_2(\mathbf F_3)$ lift，其三次幂为中心；中心已在(5)上为恒等，故(12)完全相同。不会增加未定的 metaplectic 或负号。

## 3. 任意 CM fibre divisor 的实际定义域

暂取任意虚二次场 $F$，整数 $c\ge1$，并记
$$
\mathcal O_c(F)=\mathbf Z+c\mathcal O_F,\qquad
H_c(F)/F=\text{该 order 的 ring class field}.
$$
令 $s$ 是 $X(3)$ 上的一个 CM 点，其椭圆纤维 $B_s$ 有
$\operatorname{End}(B_s)=\mathcal O_c(F)$。取
$$
0\ne\xi\in\mathcal O_c(F),\qquad \overline\xi=-\xi.
$$
沿 R857 的 Poincaré cross 规范定义
$$
D_\xi=\Gamma_\xi-B_s\times[O_s]
-\deg(\xi)[O_s]\times B_s,\qquad
Z_{s,\xi}=\varepsilon_3 i_{s,*}D_\xi.
\tag{13}
$$
以有理 endomorphism 起步时先清分母；(13)所给类在有理 Picard 群中随 $\xi$ 线性。

**定义域断言。** (13)的实际几何循环定义在
$$
K\,H_{3c}(F).
\tag{14}
$$
特别这里不是任意附加 ray class 或任意模型的全三挠坐标域。

证明如下。将 CM 椭圆写为 $\mathbf C/\Lambda$，其中 $\Lambda$ 是 proper
$\mathcal O_c(F)$ 格；局部可取自由的一阶格。CM 主定理的 torsion 版本给 idèle 对格和三级基的乘法作用。底层 CM 点的稳定子是
$F^\times\widehat{\mathcal O}_c^{\,\times}$；在3处固定完整三级基，需要
$1+3\mathcal O_{c,3}$，其余位仍为 $\mathcal O_{c,\ell}^{\times}$。

由于 $(\mathbf Z/3\mathbf Z)^\times=\{\pm1\}$，模3的全部 scalar 已由全局单位 $\pm1$ 吸收。准确有
$$
\mathbf Z_3^\times(1+3\mathcal O_{c,3})
=(\mathbf Z_3+3\mathcal O_{c,3})^\times
=\mathcal O_{3c,3}^{\times},
\tag{15}
$$
且在其它位 $\mathcal O_{3c,\ell}=\mathcal O_{c,\ell}$。所以实际全局稳定子为
$$
F^\times\left((1+3\mathcal O_{c,3})
\times\prod_{\ell\ne3}\mathcal O_{c,\ell}^{\times}\right)
=
F^\times\widehat{\mathcal O}_{3c}^{\,\times}.
\tag{16}
$$
这里(16)中的等号是在有限 idèle 群中；局部 $\mathbf Z_3^\times$ 模
$1+3\mathbf Z_3$ 的正负号可由同一个全局 $\pm1$ 消去，其在其它位仍是允许的单位。CM reciprocity 遂给 $H_{3c}(F)$；若所选连通 full3 分量需要先附 $K$，只作(14)的同一 compositum。

还须付 fibre cycle 的下降。任何 CM 同构与 $\xi$ 交换，且
$$
([a]\times[a])_*D_\xi=D_\xi
\qquad(a\in\mathcal O_c(F)^\times).
\tag{17}
$$
这是图形和两轴逐项保持的等式，不是一般挠平移断言。因此三级模点的单位自同构、原椭圆模型的 quadratic 或 exceptional $\mu_4,\mu_6$ twist，都不扩大(13)的定义域。给定某个 twist 的全三挠坐标域可以严格更大；本篇没有将那个域认成(14)。

在 $G_F$ 下，$\xi$ 的 CM 嵌入固定；在完整 $G_\mathbf Q$ 下允许其变为
$\overline\xi=-\xi$。这最多是已在 $H_{3c}(F)$ 内的 CM 二次方向，不产生另一个任意 Artin twist。系数 $\mathcal E$ 始终按(7)–(8)固定。

## 4. 原 CM 场 $F=K$：新增三次层的完整迹为零

先设 $c>1$。此时
$\mathcal O_c(K)^\times=\{\pm1\}$，且对所有 $c$，包括 $3\mid c$，都有
$$
\mathcal O_c(K)/3\mathcal O_c(K)\simeq
\mathbf F_3[\epsilon]/(\epsilon^2).
\tag{18}
$$
例如用基 $1,c\omega$，其多项式为
$T^2+cT+c^2$，模3具有一个二重根；二阶 $\mathbf F_3$-代数仍有非零 nilpotent。因此当 $3\mid c$ 时也不能把它误认成 scalar 代数。

由(15)–(18)，
$$
\operatorname{Gal}(H_{3c}(K)/H_c(K))
\simeq
\mathcal O_{c,3}^{\times}/
\mathbf Z_3^\times(1+3\mathcal O_{c,3})
\simeq C_3.
\tag{19}
$$
这个完整相对群来自3处单位，因而由3惯性生成。其它位的稳定子没有变化。

非平凡单位 $1+b\epsilon$ 在 $\Lambda/3\Lambda$ 上是非平凡
unipotent 三阶矩阵，行列式为1。主定理把(19)生成元的作用准确识别为同一三级基上的这个矩阵，或按互反约定取其逆。由于底层 CM 理想类在该相对群下不变，(17)使 fibre divisor 没有额外 scalar。故对某个实际三阶 deck $T$，
$$
Z_{s,\xi}^{\sigma}=T_*Z_{s,\xi}
\quad\text{或 }T_*^{-1}Z_{s,\xi},
$$
以及
$$
\boxed{
\operatorname{Tr}_{H_{3c}(K)/H_c(K)}Z_{s,\xi}
=(1+T+T^2)Z_{s,\xi}=0.
}
\tag{20}
$$
(20)对每一份三级标架轨道成立，不要求把所有不同标架轨道合并。

现在处理 $c=1$。这时 $\mathcal O_K^\times=\mu_6$ 的像已经杀掉
(18)的 projective $C_3$，所以
$H_3(K)=H_1(K)=K$；不能使用“层次数3”。但是 $[\omega]$ 对 CM 椭圆的作用在任意三级基上给一个非平凡三阶 deck，它固定该 CM 模点。其在 fibre 上是同时 CM 自同构，故由(17)固定
$D_\xi$。结合(12)，
$$
\boxed{Z_{s,\xi}=0\qquad(F=K,\ c=1).}
\tag{21}
$$
这没有声称给定原模型 $E_0$ 的所有三挠坐标都在 $K$。

取(3)中任一 $\chi$。它在3惯性上平凡。对 $c>1$ 的有限轨道，若
$\chi$ 根本不因子化经过 $H_{3c}(K)$，其 isotypic 投影已为零；若能因子化，则由(19)它在该相对 $C_3$ 上平凡。先作该子群平均，再用(20)，得到
$$
\boxed{
e_\chi Z_{s,\xi}=0
\quad\text{对原 }K\text{ 的全部 CM orders 与 full3 标架}.
}
\tag{22}
$$
不要求 conductor 恰为34，也没有预设某个局部 test vector 非零。

## 5. 其它 CM 场：完整环类 Galois 群不容原九阶部分

设 $F\ne K$，置 $H=H_{3c}(F)$。Ring class reciprocity 给
$$
\operatorname{Gal}(H/\mathbf Q)
=\mathcal A\rtimes\langle\iota\rangle,\qquad
\mathcal A=\operatorname{Gal}(H/F),\qquad
\iota a\iota^{-1}=a^{-1}.
\tag{23}
$$
$\iota$ 可取实际 complex conjugation，故 $\iota^2=1$。这里不要求
$\mathcal A$ 循环。

(13)及其全部 Galois 共轭的 $\mathcal E$-线性张成空间定义在
$KH$ 上。因此其 $G_K$ 作用因子化经过
$$
G=\operatorname{Gal}(KH/K).
$$
分两种情形：

1. 若 $K\not\subset H$，则 $G$ 就是(23)的 generalized-dihedral 群。其 abelianization 是
   $\mathcal A/2\mathcal A\times C_2$，指数不超过2。
2. 若 $K\subset H$，则 $G$ 是(23)的 index2 子群。因为 $F\ne K$，它不是 rotation subgroup $\mathcal A$。
   令 $\mathcal A_0=G\cap\mathcal A$；选 $b\in G\setminus\mathcal A$，则
   $b^2=1$ 且 $bab^{-1}=a^{-1}$。所以
   $G=\mathcal A_0\rtimes\langle b\rangle$，其 abelianization 同样指数不超过2。

因此 $G$ 的任意一维特征都只有阶1或2。原 $\chi$ 有十八阶，
$\chi^2$ 精确九阶，故不可能出现在该有限 $G_K$-模块中。得到
$$
\boxed{
e_\chi Z_{s,\xi}=0\qquad(F\ne K).
}
\tag{24}
$$

这个证明涵盖完整 ring class 诱导，而不只一句“唯一 quadratic inducing field”。它也包含 complex conjugation 对 $\xi$ 的负号、全部剩余域和任意有限 trace。随后把循环写在更大的域上，不会改变其本来已经经过 $KH$ 的几何作用。

若外加一个新的几何 Artin motive，当然会改变群表示；本篇从未向原 fibre divisor 插入这种对象。代数系数作为固定标量也不能替代那个几何 twist。

## 6. 全部垂直部分的原角色消失

记
$$
\mathcal V=
\ker\!\left(
\varepsilon_3 CH^2(W_{3,\overline K})_{\mathcal E}
\longrightarrow
CH_0((\mathcal E'_\tau)^2_{\overline K(\tau)})_{\mathcal E}
\right).
\tag{25}
$$
目标只把**常数域**延拓到 $\overline K$，没有把 $\tau$ 的函数域代数闭包化。

R857 的完整 localization、cusp 两 ruling 计算和光滑 fibre 的 Rosati 计算给：
$\mathcal V$ 由全部 $Z_{s,\xi}$ 的几何类的有限线性组合生成。每个循环表达只涉及有限个 CM 点和有限个定义域。非 CM 光滑纤维与全部 cusp 已被同一个(5)杀掉。

取 $z\in\mathcal V\cap CH^2[\chi]$。把一个有限垂直代表及其全部共轭放入同一个有限 Galois 域 $L/K$，对该代表施(8)。第4节支付 $F=K$ 的每一项，第5节支付 $F\ne K$ 的每一项，故
$$
\boxed{\mathcal V[\chi]=0.}
\tag{26}
$$
因此得到本篇主定理：
$$
\boxed{
\operatorname{res}_\tau:
\varepsilon_3 CH^2(W_{3,\overline K})_{\mathcal E}[\chi]
\ \hookrightarrow\
CH_0((\mathcal E'_\tau)^2_{\overline K(\tau)})_{\mathcal E}
\quad\text{为单射}.
}
\tag{27}
$$
特别，原三个角色部分中任何有限 CM fibre 线性组合均为零；这里的 CM fields 和 orders 全部允许，不仅限于 $K$ 或34。

(27)也适用于在原固定有限域上表示的循环。有理 Chow 系数下有限常数扩域的 restriction–corestriction 复合是扩域次数，所以不会因扩域而失去原类。若某泛纤维等式在 $\overline K(\tau)$ 上成立，其有理等价只用有限多个代数常数，先降到一个有限常数扩域，再应用同一论证即可。

## 7. 同一原端点与同一双点迹的准确等价

对 R857 的原实际循环保留
$$
\mathcal Z_{\rm Sch}=\Theta\mathcal Z_{\rm orig},
\qquad
\mathcal Z_9=\Gamma\mathcal Z_{\rm orig}.
$$
令下标 $\chi$ 表示同一个有限 point-factor 投影。若原有序对和 CM 方向已经位于该角色中，这个下标只是把既有来源写明，并非另添一条中央零。

对完整 $\mathcal Z_{9,\chi}$ 的泛纤维，仍使用原实际有限剩余域和点：
$$
z_{\tau,\chi}
=\sum_\rho c_\rho
\operatorname{Tr}_{L_\rho/H(\tau)}[P_\rho,Q_\rho].
\tag{28}
$$
令
$$
\mathfrak T_{\tau,\chi}
=\frac12\sum_\rho c_\rho
\operatorname{Tr}_{L_\rho/H(\tau)}
\left(
([P_\rho]-[O])\times([Q_\rho]-[O])
-
([Q_\rho]-[O])\times([P_\rho]-[O])
\right).
\tag{29}
$$
所有水平例外分量也在(28)–(29)中。原 $L_\rho/H(\tau)$ 是真实水平曲线产生的有限扩张，未替换成基域上的 section。

R857 已证明
$$
\operatorname{res}_\tau\mathcal Z_{{\rm Sch},\chi}
=(\phi\times\phi)_*\mathfrak T_{\tau,\chi},
$$
且三同源的双因子 push 在此有理 $CH_0$ 上为单射。结合(6)、(27)，准确得到
$$
\boxed{
\mathcal Z_{{\rm orig},\chi}=0
\ \Longleftrightarrow\
\mathcal Z_{{\rm Sch},\chi}=0
\ \Longleftrightarrow\
\mathfrak T_{\tau,\chi}=0.
}
\tag{30}
$$

这比 R857 的“迹零当且仅当存在有限 CM 垂直代表”多支付了一步：
在原角色中，任何这种垂直代表已经为零。

但(30)没有判定这三项是否为零。两份椭圆曲面几何 Mordell–Weil 群仅挠，也不能消去(29)：那一结论只涉及 $\overline K(\tau)$ 上的点，(29)却包含各 $L_\rho$ 上的双点外积及其**同步有限迹**。即便另能消去两个单点迹，也未消去这个双点迹。

原 period 与全来源尺度维持 R857 的实际式：
$$
AJ_{W_3}(\mathcal Z_{{\rm Sch},\chi})(-\Omega_3/18)
=
AJ_A(\mathcal Z_{{\rm orig},\chi})(\Omega_A).
\tag{31}
$$
原 source3、$6^{-2}$、$12^{-2}$、$D_X=1632$、$D_C=816$、全部 $q_0/q_2$ 与 $\eta_j$ Artin 系数均未变化。

## 8. 导子34的真实 local3 同源及 CM divisor 倍数

本节把前面的消失放回 R857 的实际同源，不只给抽象 field obstruction。

原 native 曲线为
$$
\mathcal E_\tau:\quad V^2+\tau UV+V=U^3,
$$
三同源 $\phi:\mathcal E_\tau\to\mathcal E'_\tau$ 的核是
$\langle(0,0)\rangle$，并满足
$$
U'=U+\tau/U+U^{-2}.
\tag{32}
$$
其对偶核在(4)上正是
$$
D=\left\langle
\left(-\tau^2/3,\,
\frac{\delta(\tau^3-27)/9+\tau^3/3-1}{2}\right)
\right\rangle .
\tag{33}
$$
第二坐标用 $D'=2V'+\tau U'+1$ 的正号选择；换 $\delta$ 为 $-\delta$
只换核的生成元。

为核(33)，原三除多项式除去 $U=0$ 后为
$$
3U^3+\tau^2U^2+3\tau U+3.
$$
在其任一根上，(32)给 $U'=-\tau^2/3$，故这就是
$\phi(\mathcal E_\tau[3])=\ker\widehat\phi$，没有以某个任择 full3 line 代替。

其余三条核由实际点
$$
Q_i=(\tau\omega^i+3\omega^{-i},\,4),
\qquad i=0,1,2
\tag{34}
$$
生成。取 $S=\langle Q_0\rangle$，则 $S\ne D$，并且
$$
\mathcal E_\tau
\xrightarrow{\phi}\mathcal E'_\tau
\longrightarrow\mathcal E'_\tau/S
\tag{35}
$$
是一个真正 cyclic degree9 同源：复合核阶9，而它与
$\mathcal E_\tau[3]$ 的交只有 $\ker\phi$，阶3，因此不是 $E[3]$。
这给实际的非回溯两边；不同 full3 标架可置换(34)，但不能使两边成为同一核。

现在设中点 $\mathcal E'_s$ 的 endomorphism order 是 $\mathcal O_{34}(K)$。
因为3在 $K$ 分歧且不除34，
$$
\mathcal O_{34}/3\mathcal O_{34}
\simeq\mathbf F_3[\epsilon]/\epsilon^2.
$$
四条 $\mathbf F_3$-直线中恰有一条在整个 order 下稳定，即唯一
horizontal 3-ideal 核；另外三条均下降到 $\mathcal O_{102}$。
这可以直接从指数3超格的 multiplier ring 核对：稳定线保最大3-adic order，非稳定线的 multiplier ring 是
$\mathbf Z_3+3\mathcal O_{K,3}$，其它位不变。

所以(35)两端的 CM orders 只能是
$$
(34,102),\quad(102,34),\quad(102,102).
\tag{36}
$$
不能把它当成两个 order34 点之间的 $\mathcal O_{34}$-稳定 cyclic9 同源。

CM divisors 的倍数也固定。对任一 degree3 同源
$\psi:B_c\to B_{c'}$，同 CM 方向及 R854 的 cross 规范给
$$
(\psi\times\psi)_*D_{c\delta}
=\frac{3c}{c'}\,D_{c'\delta}.
\tag{37}
$$
因此中点 order34 至一个 horizontal order34 端点时系数为3；
至一个 descending order102 端点时系数为1；相反 ascending
order102 至34时系数为9。两次对偶复合的系数为9，正好与
$[3]$ 的双因子 push 在 cross divisor 上相合。

(33)–(37)付清真实3-local/order及 divisor 运输，却不取消第4节的完整 ring-class trace。原 $\eta_j$ 在3处不分歧，故其 order34 满三级 CM 轨道的同角色投影仍被(20)严格杀掉。

## 9. 与原 canonical 检测的边界及后续实际问题

R817 的固定7993计算重建的是三个原 $B_4$ eigenline 的 unit 负二矩。
经 R814 的实际 AJ 平方式，它检测先于 $p$ 固定的
$\Delta_j$；R854 再经真实 CM contraction 得到非零 $H_j$。
这一检测没有涉及后来 R830/R831 的修复端点
$\mathcal Z_{\rm orig}$。原同一 degeneracy 的旧 diagonal 甚至已由
R829 证明全 Chow 类为零。因此不能把7993搬到(30)来宣布
$\mathfrak T_{\tau,\chi}\ne0$。

本篇也不把 $H_j$ 的非零与(26)相冲突：$H_j$ 位于 R814 所选
good-pair cusp form 的另一 Kuga–Sato 三fold。它到本篇
$(W_3,\varepsilon_3)[\chi]$ 的**实际循环对应**仍未支付。
如果以后构造了一个保持原 $\chi$ 的 Chow 同构，并把 $H_j$ 非零地送来，
则(26)–(27)迫使其像有非零泛纤维限制；不能是本篇有限 CM fibre
类的线性组合。它必须保留该实际对应产生的水平部分。

当前可以继续处理的是(29)本身的完整有限 trace，或寻找上述真实
canonical correspondence。主中央同时零的排除、指定 AJ 对无穷 $p$
的非零以及 full $\Sha[p^\infty]$ 主目标均未在本篇宣称完成。

## 10. 引用与证据范围

1. [R857](R857-original-full-three-scholl-and-generic-cm-cycle-criterion.md)，
   main `d540a5f17cc6c17d955009ce4055c9706a1303d6`：
   实际满三级模型、Scholl 对应、81倍 Chow 互逆、完整泛纤维双点迹、
   cusp/非 CM 消失与 CM divisor localization。
2. [R852](R852-original-schoen-correspondence-and-exact-chow-inverse.md)、
   [R851](R851-original-schoen-map-and-horizontal-cycle-transport.md)：
   原 CM 两条可逆 Chow 线、同一个三阶作用和全部图形倍率。
3. [R844](R844-original-genus-four-cm-order-seventeen-and-two-neighbors.md) §2：
   原 $\eta_j$ 的完整定义、$H_\eta=H_{34}$、在3处不分歧和其阶18；
   本篇仅引用这些已付角色事实，不使用其后来已排除的 genus4 假设。
4. J. S. Milne, *The Fundamental Theorem of Complex Multiplication*，
   [作者原稿](https://www.jmilne.org/math/articles/2007c.pdf)，
   Theorem3.10、Remark3.11及Theorem3.13，印页22–24：
   保留实际有限 Tate 格和 torsion 的 idèle reciprocity。
   Theorem3.10 没有假设 endomorphism order 必须最大；
   页23注12也明确非最大 order 范围。第3–4节的稳定子
   (15)–(16)、dual-number 商和特殊单位处理在本篇逐项给出。
5. Milne, *Modular Functions and Modular Forms*，
   [作者稿](https://www.jmilne.org/math/CourseNotes/MF.pdf)，
   §12，特别 Remark12.5 与 Proposition12.6：
   quadratic orders、proper CM 格与 ring-class 规范。
   (19)也已由本篇局部单位商自含得到，无需只凭 class number 猜层次数。
6. [R854](R854-original-canonical-cm-contraction-and-threefold-heegner-cycles.md)：
   (37)沿同一 Poincaré/CM graph normalization；
   [R817](R817-fixed-prime-original-negative-two-and-nonzero-fixed-cycles.md)
   与 [R814](R814-common-fixed-good-pair-and-three-original-aj-squares.md)：
   第9节严格区分的原7993检测及 canonical 对象。
7. Gordon–Murre，
   [*Chow motives of elliptic modular surfaces and threefolds*](https://arxiv.org/pdf/alg-geom/9610007)，
   §3.3、§4.1、§5.1，为(5)及 deck/Scholl 相容的原始来源。
   本篇的(11)另由 R857 已证明的完整 Chow 同构直接支付，
   不新假设实现忠实性。

本篇没有新增数值扫描、计算证书或自由非零假设。

## 附录 A. 同一 local3 消失的独立 toric 判据

本附录只核对第4节已经证明的满三级 CM trace 消失，
不把局部 Hom 为零代替该节的 Chow 证明，也不增加原中央零。

满三级 Scholl 因子的归一 cusp form 是
$$
g_9(z)=\eta_{\rm Dedekind}(3z)^8
=\theta(\psi_0^3),
\tag{A1}
$$
其中 $\psi_0$ 是原 $E_0:Y^2=X^3+1$ 的 Hecke 角色。
这里 $\psi_0^3$ 的2部分消去，3处导子为 $(\delta)$，
所以其 theta form 的 level 为9、weight 为4、中心角色平凡。
这个身份也可由 level9 的一维 cusp 空间和首系数1确定；
它只固定本附录的局部表示，不重选(31)的几何三微分。

令 $F=\mathbf Q_3$、$K_3=F(\delta)$，并令
$\epsilon_{K_3/F}$ 为对应的二次角色。它是3处导子1的分歧角色，且
$$
\epsilon_{K_3/F}(-1)=-1.
$$
把 $(\psi_0^3)_3$ unitary 化，记为 $\kappa$。
原 CM 极化和中心角色给
$$
\kappa^c=\kappa^{-1},\qquad
\kappa|_{F^\times}=\epsilon_{K_3/F},\qquad
\kappa(-1)=-1.
\tag{A2}
$$
故原 $\pi_3$ 的 base change 是 $\kappa\oplus\kappa^{-1}$。

对于本文任一原 $\chi=\eta_j^{\pm1}$，既有完整局部角色给
$$
\chi\text{ 在3处不分歧},\qquad
\chi(\delta)=-1,\qquad
\chi^2=1,\qquad
\chi|_{F^\times}=1.
\tag{A3}
$$
特别 $3=-\delta^2$ 使 $\chi(3)=1$。这里保留了 uniformizer 的
负号；“不分歧”不等于把整个局部角色设成1。
原 order34 的唯一3素理想平方为 $(3)$ 且非 principal：
若 $a+34b\omega$ 的范数为3，则 $b\ne0$ 时范数至少867，而
$b=0$ 时需 $a^2=3$。故它在 $C_{18}$ 中是唯一二阶元；
三个原指数13、1、7均奇，确给 $\chi(\delta)=-1$。

设 $\psi_F$ 为任一非平凡加性角色，
$\psi_{K_3}=\psi_F\circ\operatorname{Tr}_{K_3/F}$。
Tate 的对偶 epsilon 恒等式准确为
$$
\epsilon\!\left(\tfrac12,\theta,\psi_{K_3}\right)
\epsilon\!\left(\tfrac12,\theta^{-1},\psi_{K_3}\right)
=\theta(-1).
$$
由(A2)–(A3)，两个 base-change 因子互为逆，
于是
$$
\epsilon_{\rm BC}
:=
\epsilon\!\left(\tfrac12,
 \pi_{3,K_3}\otimes\chi,\psi_{K_3}\right)
=(\kappa\chi)(-1)=-1.
\tag{A4}
$$

必须区分这个 base-change epsilon 与 Rankin–Selberg epsilon。
Cai–Shu–Tian，*Explicit Gross–Zagier and Waldspurger formulae*，
Algebra & Number Theory 8 (2014)，印页2554–2555，
§3 的实际定义及 Tunnell–Saito 判据为
$$
\begin{aligned}
\epsilon_{\rm RS}
 &=\epsilon_{K_3/F}(-1)\epsilon_{\rm BC},\\
\dim\operatorname{Hom}_{K_3^\times}
       (\pi_3^B,\chi^{-1})=1
&\iff
\epsilon_{\rm RS}
 =\chi(-1)\epsilon_{K_3/F}(-1)\epsilon(B).
\end{aligned}
\tag{A5}
$$
$\epsilon(B)=1$ 对 split quaternion，等于 $-1$ 对 division quaternion；
$\pi_3^B$ 表示在相应 quaternion 上的 Jacquet–Langlands 表示。
原文链接：
<https://msp.org/ant/2014/8-10/ant-v8-n10-p.pdf>，
印页2555的 §3A 开头。所引用的是这一明确规范，不能只保判据右边
而漏掉第一行的二次角色因子。

代入(A3)–(A4)，$\epsilon_{\rm RS}=+1$，而(A5)右边为
$-\epsilon(B)$。故所需局部 quaternion 必须为 division：
$$
\boxed{
\operatorname{Hom}_{K_3^\times}
(\pi_3,\chi^{-1})=0
\quad\text{对原 split }GL_2(\mathbf Q_3)\text{ 表示}.
}
\tag{A6}
$$
这与第4节的原全层 Chow 计算相合：原不分歧 $\chi$ 不允许把
满三级 CM divisor 的 relative $C_3$ trace 当成一个非零 toric
来源。该局部计算本身不构造 division Shimura 来源，也不提供
它与 $\mathcal Z_{\rm orig}$ 或 R854 的 $H_j$ 之间的循环对应。
它尤其不改变第9节关于7993检测对象的区别。
