# R811 — 原三个 canonical Soulé 类的严格核交为零与同一 Heegner 全局比较

日期：2026-11-15。**状态：已证明。** 对 R804 原来定义的三个指定全局类，局部化为零必迫该类本身为零。因此它们不能以非零类落入原严格 Selmer 核。本篇不证明这三个类本身非零，不证明整个 Selmer 群的局部化单射，也不改变原二阶行的线性组合及其全部外部。

证明使用的是同一原模数的椭圆单位、真实复共轭、反循环变量的反演，以及一个已存在的 good pair。两个局部 Coleman 映射在**先除去 p、再于增广点完成**的环中确为同构。本文不以“伪零余核”代替这个条件。

## 1. 原类与结论

沿用 [R804](R804-original-order-eighteen-soule-classes-and-negative-two-localization.md) 的完整来源。对
$$
j\in\{4,10,16\},\qquad
\nu_j=\eta_j\psi_0^{-1}\bar\psi_0^2,\qquad
V_j=E_{\mathfrak P}(1)\widehat\nu_j^{-1},
\tag{1}
$$
保留同一个 cyclic18 域、固定系数嵌入、模数
$\mathfrak f=(34\delta)$、Kato 正单位、辅助理想 $(5)$、
幂等元 $e_{\eta_j}$，以及
$$
z_j=\frac1{30}\operatorname{pr}_K
          \operatorname{tw}_{\nu_j}(e_{\eta_j}u_\infty).
\tag{2}
$$
特别是，本文的 $z_j$ 不是另选的 Selmer 生成元。

记
$$
H_{f,0}^1(K,V_j)=
\ker\bigl(H_f^1(K,V_j)\xrightarrow{\operatorname{loc}_{\mathfrak p}}
                        H^1(K_{\mathfrak p},V_j)\bigr).
$$

**定理。** 在原普通 ray 及原固定好素数范围内，
$$
\boxed{
E_{\mathfrak P}z_j\cap H_{f,0}^1(K,V_j)=0.
}
\tag{3}
$$
等价地，
$$
\boxed{
z_j\ne0
\ \Longleftrightarrow\
\operatorname{loc}_{\mathfrak p}z_j\ne0
\ \Longleftrightarrow\
I_{j,-2,p}\ne0 .
}
\tag{4}
$$

最后一个等价仍使用 R804 的原周期与 Euler 规范：
$$
\log_j(\operatorname{loc}_{\mathfrak p}z_j)
=-34^2c_j\theta^9\Omega_p^4
 \frac{1+\pi_0/\bar\pi_0^2}{1+\bar\pi_0/\pi_0^2}\,
 I_{j,-2,p}^{\,2}.
\tag{5}
$$
本文没有将(5)中的平方改成线性点对数。

以下固定一个 $j$，省略部分下标。所引 [Ca] 为 Castella 的发表版
*Tamagawa number conjecture for CM modular forms and Rankin–Selberg convolutions*，
含 Castella–Parker 附录：
[完整 v3 PDF](https://arxiv.org/pdf/2407.11891v3)、
[保留所有共轭标号的 HTML](https://arxiv.org/html/2407.11891v3)。
本文只用其正文中以下已经证明的结果；不用附录中尚待局部非零的逆命题。

## 2. 两套角色约定与两个素位

在原理想角色的约定中置
$$
\lambda=\eta_j^{-1}\psi_0^3,\qquad
\phi=\lambda\mathbf N^{-2}=\nu_j^{-1}.
\tag{6}
$$
$\lambda$ 正是 R806 反射后的 weight4 角色。其导子为 $34\delta$，
中心特征为 $\eta_K$，且
$$
w(\lambda\mathbf N^{-2})=-1.
\tag{7}
$$
这里有限 $\eta_j$ 在有理对角上平凡；
2处的三次部分、17处的十八阶部分、3处的 $\delta$ 导子均保留。
因此 [Ca] 的 $\mathfrak d_K\Vert\mathfrak f_\lambda$ 条件成立，
不是把十七处分歧或三处导子略去。

[Ca] 以几何互反定义 p-adic avatar，且把 $\mathbf N$ 的 avatar
记为 $\varepsilon_{\rm cyc}^{-1}$。在其 infinity-type 约定下，
$\lambda$ 为 $(-3,0)$，$\phi$ 为 $(-1,2)$。转换回原算术互反后，
精确的表示对应是
$$
T_\phi\otimes E=\widehat\nu_j,\qquad
T_{\phi^\tau}\otimes E
=\varepsilon_{\rm cyc}\widehat\nu_j^{-1}=V_j .
\tag{8}
$$
此处 $\phi^\tau=\phi^*$ 是共轭自对偶关系；不是把 $\nu_j$ 与
$\nu_j^{-1}$ 在同一互反约定下相认。

令 [Ca] 的 $v=\mathfrak p$、$\bar v=\bar{\mathfrak p}$。
$T_\phi$ 在 $(v,\bar v)$ 的 Tate 指数为 $(-1,2)$，
$T_{\phi^\tau}$ 则为 $(2,-1)$。
所以 R804 的原类在 $T_{\phi^\tau}$；
稍后 Heegner 类的目标分量在 $T_\phi$。
必须作真实 $\tau$ 共轭，并把局部位从 $v$ 移到 $\bar v$，
才能比较两个全局类。

这里的 $\tau$ 是上同调中改变 $G_K$ 作用的共轭同构。
固定系数域的标量只作标量，不对 $\mathbf C_p$ 任意延拓一个复共轭。

## 3. 同一个原椭圆单位在反循环塔上的提升

令 $K_\infty/K$ 为反循环 $\mathbf Z_p$ 扩张，
$\Gamma=\operatorname{Gal}(K_\infty/K)$。
把(2)的 $\operatorname{pr}_K$ 暂换为
$\operatorname{pr}_{K_\infty}$，定义
$$
\mathbf c_j=
\frac1{30}\operatorname{pr}_{K_\infty}
        \operatorname{tw}_{\nu_j}(e_{\eta_j}u_\infty)
\in H_{\rm Iw}^1(K_\infty,T_{\phi^\tau})\otimes E.
\tag{9}
$$
其增广特殊化严格为
$$
\mathbf c_j(0)=z_j.
\tag{10}
$$

R804 先从 $K(34\delta p^\infty)$ 范数到
$H K(E_0[p^\infty])$，再扭曲和下降；
[Ca, §4.2] 则把同一个 Kato 单位直接扭曲、范数到 $K_\infty$。
范数传递性与扭曲自然性使两个路径相同。
而 $\nu_j(e_{\eta_j})=1$，故没有附加18因子。
若采用 Robert 单位，必须在两个路径同时乘原 $-1/12$；
本文固定 Kato 单位，未作这一换标。

[Ca, Theorem 4.2.1] 的无平滑类
$\mathbf c^{\rm Ca}_{\phi^\tau}$ 也来自该原单位，
差别只在已显示的平滑算子。明确保留该定理的 Artin 约定，置
$$
s_{5,j}(T)=
\sigma_{(5)}-\phi^\tau(\sigma_{(5)}),\qquad
d_j(T)=s_{5,j}(T)/30.
\tag{11}
$$
于是同一原类满足
$$
\mathbf c_j=d_j(T)\mathbf c^{\rm Ca}_{\phi^\tau}.
\tag{12}
$$
(11)中的 $\sigma_{(5)}$ 若转换成原算术 Artin，
须连同角色一起反转，不能只反转一个符号。

所需且确实成立的是
$$
d_j(0)\ne0.
\tag{13}
$$
证明如下。有理理想 $(5)$ 在反循环 $\Gamma$ 中平凡；
有限 $\eta_j$ 在它上面平凡，而原 $\psi_0((5))=-5$。
故在几何 Frobenius 写法中
$\phi^\tau(\sigma_{(5)})=-1/5$；
等价的算术写法也给一个非一标量。
所以(11)没有增广零。原平滑因子
$25-\nu_j((5))=30$ 始终保留，未把 $d_j(0)$ 约定成1。
这一比较只把两个**已指定单位来源**对应起来，
不借一维性另选一个方便的类。

令
$$
C(T)=\mathscr L_v(\phi).
$$
[Ca, Theorem 4.2.1] 给注入的局部映射及真实有限余核，
并给
$$
\operatorname{Col}^{\rm EU}_v
 \bigl(\operatorname{loc}_v\mathbf c_j\bigr)
=d_j(T)C(T).
\tag{14}
$$
原 CM 周期如与 [Ca, §2.1.2] 作固定基变换，
应在(14)的映射及函数两边同步作同一非零基变换。
这不会制造增广零，也不改变 R804 的原标量式(5)。

由(7)及 [Ca, Proposition 4.3.2]，
$$
\boxed{C(T)\ne0\text{，作为反循环 Iwasawa 函数。}}
\tag{15}
$$
这不是 $C(0)\ne0$ 的假设；$C(0)$ 仍是待判的指定值。

## 4. 增广完成环：两个 Coleman 映射确为同构

扩大有限系数域以包含一个稍后选定的 good pair 的全部系数。
在 $\Lambda_{\mathscr O}^{\rm ur}$ 中取相应系数因子，
先反演 p，再局部化于增广理想，最后完成。记所得环为
$$
\mathscr R=\mathscr F[[T]],\qquad T=\gamma-1.
\tag{16}
$$
$\mathscr F$ 是所选不分歧完成系数域的分式域。
它是一个 p-adic 系数域，不在本文被冒认为代数数域。
上述局部化与完成是平坦操作。

需要强调有限余核的实际用法。
[Ca, Theorems 4.2.1 and 3.2.2] 给的是注入且有限余核的 Coleman 映射。
其有限余核被一个 p 幂杀掉；因此反演 p 后余核已经为零，
随后(16)的平坦完成仍保持同构。
特别是，不可能仍有 $\Lambda/(T)$ 这类支撑在增广点的余核：
它不是被一个 p 幂杀掉的有限余核。


这一步不用仅有特征理想等式的“伪同构”来替代定理中更强的映射结论，
也不从一般 Perrin–Riou 映射无条件声称增广处可逆。

还需保留真正的局部特殊化。对局部 Iwasawa 上同调复形作
$T=0$ 的导出张量，普遍系数正合列给
$
0\longrightarrow
 H^1_{\rm Iw}/T H^1_{\rm Iw}
 \longrightarrow H^1(K_v,T_{\phi^\tau})
 \longrightarrow H^2_{\rm Iw}[T]\longrightarrow0,
\tag{16a}
$
再作相同的有理系数扩张。
所以左边到实际局部群是注入；不需要假设右端为零。
这一点保证“原特殊化的局部类为零”真的迫
Iwasawa 局部类被 $T$ 整除。
这里只使用局部的标准导出 Shapiro 特殊化，
没有断言全局 Selmer 控制映射满射或整个有限层局部化单射。

反循环共轭满足
$$
\tau\gamma\tau^{-1}=\gamma^{-1},\qquad
\iota(T)=(1+T)^{-1}-1=-\frac{T}{1+T}.
\tag{17}
$$
于是
$$
\tau(a\,\mathbf c)=\iota(a)\tau(\mathbf c).
$$
记
$$
\mathbf c_j^\tau=\tau(\mathbf c_j),
$$
它位于 $T_\phi$ 的全局 Iwasawa 上同调中。
把原 EU Coleman 映射真实输送到 $\bar v$：
$$
\operatorname{Col}^{\rm EU,\tau}_{\bar v}(x)
=\iota\!\left(
 \operatorname{Col}^{\rm EU}_v(\tau^{-1}x)\right).
\tag{18}
$$
两个半线性操作使(18)成为 $\mathscr R$-线性同构，且
$$
\operatorname{Col}^{\rm EU,\tau}_{\bar v}
  (\operatorname{loc}_{\bar v}\mathbf c_j^\tau)
=d_j^\iota C^\iota.
\tag{19}
$$
这里完整的 $\iota$ 不可删掉。

## 5. 真正的 good pair 与伴随因子

由(6)–(7)和 [Ca, Lemma 5.1.2]，选取一个 good pair
$(\psi,\chi)$，满足
$$
\lambda=\psi\chi,\qquad
g=\theta_\psi,\qquad
L(\psi^\tau\chi,2)\ne0.
\tag{20}
$$
它的 $\psi$ 导子为与 $pD_K$ 互素的 cyclic 理想，
全部局部 self-dual 条件按该 lemma 支付。
本篇不要求也不使用只在 weight2 中定义的 strong-good-pair 条件。

置
$$
\phi'=\psi^\tau\chi\mathbf N^{-2},\qquad
A(T)=\mathscr L_v(\phi'),\qquad
B(T)=\mathscr L_v(g,\chi).
\tag{21}
$$
$\phi'$ 的 infinity type 为 $(2,-1)$；
它在所用 Katz 映射的经典插值范围内。
所以(20)及实际插值公式给
$$
\boxed{A(0)\ne0.}
\tag{22}
$$
此处普通 Euler 因子的 p 赋值分离排除了例外零：
两个 ordinary 根的赋值为0与3，中心 Tate 指数为2，
相应因子不可能等于 $1-1$。
周期、Gamma 因子及全部坏处因子也非零。
(22)只说 $A$ 在 $\mathscr R$ 中为单位，不说其原整数值一定是 p 单位。

[Ca, Proposition 2.3.1] 的完整因子分解为
$$
\boxed{B(T)^2=u(T)C(T)A(T),\qquad u\in\mathscr R^\times.}
\tag{23}
$$
这里 $C$ 的模数为 $34\delta$，伴随 $A$ 使用其真实更大导子；
不能把二者都换成某个方便的 imprimitive 层。
(15)、(22)、(23)保证 $B(T)\ne0$，但仍允许 $B(0)=0$。

由 [Ca, Theorem 3.2.2]，有真正的 Iwasawa Heegner 类
$\mathbf Z_{g,\chi}$。按其(3.2)的 CM 直和分解，取第一分量
$$
\mathbf Z_j\in H_{\rm Iw}^1(K_\infty,T_\phi)\otimes\mathscr R.
\tag{24}
$$
在 $\bar v$，第二分量 $T_{\phi'}$ 的 Tate 指数为 $-1$，
其有限局部群为零；第一分量指数为2，其有限群为全部 $H^1$。
所以整个 Heegner Coleman 图准确降为同一个局部秩一模上的同构
$$
\operatorname{Col}^{\rm H}_{\bar v}:\mathcal H_{\bar v}\xrightarrow{\sim}\mathscr R,
\qquad
\operatorname{Col}^{\rm H}_{\bar v}
  (\operatorname{loc}_{\bar v}\mathbf Z_j)=B(T).
\tag{25}
$$
此处使用的是 [Ca, Theorem 3.2.2] 的
$\operatorname{Col}_{\bar v}\operatorname{loc}_{\bar v}
=\mathscr L_v(g,\chi)$，并非误写成同一 $v$。

$\mathbf Z_j(0)$ 是实际 Heegner 类第一分量乘
$$
\mathcal E_p(g,\chi)
=\left(1-\frac{\chi(v)p}{\alpha}\right)
 \left(1-\frac{\chi(\bar v)p}{\alpha}\right),
\tag{26}
$$
$\alpha$ 为普通单位根。
两因子均为 $1+p\mathcal O$，故这一真实特殊化没有另加零因子。

## 6. 同一全局秩一模中的比较

令
$$
\mathcal M=
\check{\mathcal S}_{\rm rel}(\phi)\otimes\mathscr R.
\tag{27}
$$
“rel”只放宽两个 p 位；其余位保持原未分歧条件。
椭圆单位类的原包含由 [Ca, Proposition 4.3.3] 的证明及其注7给出；
Heegner 类满足更强的 Bloch–Kato 条件。
增添 good pair 的辅助坏素位也不改变这里的有理系数源：
原一维表示在这些位的局部 $H^1$ 为零。
故 $\mathbf c_j^\tau,\mathbf Z_j$ 确在同一个(27)中。

[Ca, Proposition 4.3.4] 的证明明确支付
$\check{\mathcal S}_{\rm rel}(\phi^\tau)$ 为 torsion-free、秩一。
作真实 $\tau/\iota$ 输送后，(27)也是 torsion-free、秩一。
由(19)、(15)及 $d_j\in\mathscr R^\times$，
$$
\operatorname{loc}_{\bar v}:\mathcal M\longrightarrow\mathcal H_{\bar v}
\tag{28}
$$
是非零映射。其源和目标都秩一，所以核为 torsion；
源无 torsion，从而(28)注入。

这只是**反循环 Iwasawa 模在指定增广完成后的注入**。
尚未特殊化就不能把它冒称
$H_f^1(K,V_j)\to H^1(K_{\mathfrak p},V_j)$ 注入；
一般特殊化会有控制余项。下面通过实际类恒等式避开这个问题。

由第4节与(25)，两个局部映射都是同一
$\mathcal H_{\bar v}$ 到 $\mathscr R$ 的同构，故存在唯一
$r_j(T)\in\mathscr R^\times$，使
$$
\operatorname{Col}^{\rm H}_{\bar v}
=r_j(T)\operatorname{Col}^{\rm EU,\tau}_{\bar v}.
\tag{29}
$$
置 $q_j=r_jd_j^\iota$。把(19)、(25)送入(28)，得到
$$
B\,\mathbf c_j^\tau=q_j C^\iota\,\mathbf Z_j.
\tag{30}
$$
这是实际全局上同调恒等式；不是仅比较两个局部数。

因为 $C\ne0$，可写 $C=T^a c(T)$，其中 $c(0)\ne0$。
于是
$$
e_\iota(T):=\frac{C^\iota}{C}
=\left(-\frac1{1+T}\right)^a
  \frac{c(\iota(T))}{c(T)}
\in\mathscr R^\times.
\tag{31}
$$
(31)是增广完成环内的直接代数式；
没有声称全局 Katz 函数 $C^\iota=C$，也没有假设 $C(0)\ne0$。

由(23)代入(30)，在 torsion-free 的 $\mathcal M$ 中约去非零 $B$，
得到关键式
$$
\boxed{
\mathbf c_j^\tau
=\mathfrak u_j(T)B(T)\mathbf Z_j,\qquad
\mathfrak u_j(T)=
\frac{q_j(T)e_\iota(T)}{u(T)A(T)}
\in\mathscr R^\times .
}
\tag{32}
$$
分母的可逆性只用(22)，不是待证的原 Katz 非零。
所有在增广点可能消失的因子已经明确留在 $B$ 中。
由(23)还知 $a=2\operatorname{ord}_T B$，所以
$e_\iota(0)=1$；即使 $C(0)=0$，(32)的单位仍有定义。

## 7. 特殊化：仅 canonical 类的严格核交为零

全局上同调的增广特殊化与真正 $\tau$ 交换，而
$\iota(T)$ 在 $T=0$ 仍为0。由(10)、(32)，
$$
\boxed{
\tau z_j=\mathfrak u_j(0) B(0)\mathbf Z_j(0).
}
\tag{33}
$$
这个式子在一个忠实系数扩张后的全局 $H^1$ 中成立。
因此右边为零确实使原 $z_j$ 为零；不是只使某个局部或数值投影为零。

若 $\operatorname{loc}_{\mathfrak p}z_j=0$，
(10)与真正的局部特殊化注入(16a)说明
$\operatorname{loc}_v\mathbf c_j$ 在局部 Iwasawa 模中被 $T$ 整除。
$\operatorname{Col}^{\rm EU}_v$ 为线性映射，
所以(14)给 $d_j(0)C(0)=0$。
由(13)，
$
C(0)=0.
$
(22)–(23)迫 $B(0)=0$，再由(33)得 $z_j=0$。
反向的 $z_j=0\Rightarrow\operatorname{loc}_{\mathfrak p}z_j=0$
当然成立。这证明(3)及(4)的第一个等价。
最后用 R804 的原式(5)、全部非零 Euler/周期因子和局部对数同构，
得到(4)的第二个等价。

证明没有使用特殊化后的 Selmer 群维数为一，
没有假设 Heegner 类 $\mathbf Z_j(0)$ 非零，
也没有以非零的 Iwasawa 类替代其指定特殊化非零。
若 $\mathbf Z_j(0)$ 非零而其局部对数为零，(33)仍允许
原 canonical 椭圆单位类为零；这与高权局部化的现有未知完全相容。

## 8. 原来源中的准确收益与仍开的门

R804 第6节原来仅把指定值识别为
$z_j$ 在严格 Selmer 商中的局部像。
本文把这三个**指定类**的门进一步化为它们在全局上同调中是否为零：
$$
I_{j,-2,p}=0\quad\Longleftrightarrow\quad z_j=0.
\tag{34}
$$
它没有证明任一个 $z_j\ne0$。
一般 Selmer 类可能仍有非零严格核；
本文的结论只限(2)的三个 canonical 类及各自张成的一维线。

尤其实际 R801/R804 的原线性行仍为
$$
\lambda^{2N}\Omega_p^2
 \sum_{j=4,10,16}\alpha_{j,N}I_{j,-2,p}.
\tag{35}
$$
(33)不把三个不同表示的全局类变成(35)的线性组合；
$\mathfrak u_j(0)$ 也未声称在 $\overline{\mathbf Q}$ 中。
所以本文不据此调用点对数的代数线性独立，
不删除 R807/R809 的完整联络交换子，不删除任何 W 外部。

下一实际问题已经明确为：证明原(2)至少一条全局特殊化非零，
或得到可作用于(35)及原中央补域的同源线性关系。
原三个中央同时为零的排除仍未完成。

## 9. 使用的已发表条款

所有下列条款均按 [Ca] 含附录的完整 v3／发表版核对：

- §2.1.1、§2.2.2：几何互反、范数与共轭自对偶约定；
- Proposition 2.3.1：完整 Katz–Heegner 平方因子分解，单位因子保留；
- Theorem 3.2.2：真实 Heegner 塔、特殊化 Euler，以及**有限余核**局部 Coleman 图；
- Proposition 3.5.1、Lemma 3.4.2：同一个 CM 直和与两个普通局部条件；
- Theorem 4.2.1：同模数 Kato 单位、实际平滑算子与**有限余核** Coleman 图；
- Proposition 4.3.2：由真实 root −1 得 $C(T)\ne0$，并非 $C(0)\ne0$；
- Propositions 4.3.3–4.3.4 的证明：原 relaxed 全局模的包含、秩一及无 torsion；
- Lemma 5.1.2：当前 weight4 的 good pair 存在与真正临界伴随值非零。

R806 支付本篇三条 $\lambda$ 的完整有限角色、导子和 root；
R804 支付原 $34\delta$ 单位、30平滑、固定 Artin/CM 周期与(5)。
本篇没有新数值计算，也没有新增可重算数据文件。
