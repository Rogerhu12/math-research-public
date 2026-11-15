# R697 — 保完整三层的唯一最高项修正、原首像吸收与同 R 顶三 charge 余项

日期：2026-11-15。**状态：已证明。** 本篇继续 R689 的实际返回，区别两件事：曲线上的相同值，与在同一 $3C$ 上保留全部两个 normal 导数。后者的最高项修正是唯一的，其非固定角极有准确的充要清除条件。

在最高系数全为原固定角因子的显示范围内，所得返回保原全部三层，而且当最高缺口至少三时在同一 $\mathcal W_D$。若原立方来源本身处于首核，则更大的原 forcing 向量在**完整旧目标的模 $p$ 首像**中已被该来源吸收。到下一位，留下的不是任意新行，而是同一个 $R$ 产生的顶三 charge 以及原 $\mu_{\rm phys}d_2$。全文给出这些实际向量及准确提升判据，不宣称它们非零或为零。

## 1. 原范围和 R689 的 normal 差别

保 R689 的原符号
$$
\mathcal E=Y\partial_Y,\quad\delta=t\partial_t,\quad
d=1+8t,\quad h_7=7+4t+16t^2,
$$
$$
A=6(1-t),\quad B=-(1+2t),\quad
\mathcal R=\frac{t(154+160t+1792t^2)}{3d^2},
\quad p=6s-1>101.
\tag{1}
$$
取同一整因子
$$
F=\sum_{i=0}^bf_i(t)Y^i,\quad
1\le b<p,\quad f_0f_b\ne0,\quad f=f_b,
$$
其 $Y$ 次数在约化后不降。原三次 forcing 是
$$
K_F=e^3\mathcal R+A e^2\delta^2F
-2A e a_0\mathcal E\delta F+
A a_0^2\mathcal E^2F+B e^2a_0,
\quad e=\mathcal EF,\ a_0=\delta F.
\tag{2}
$$
原立方来源始终要求
$$
P^{\rm fact}=d^{-C_D}t^rQF^3\in\mathcal W_D,\qquad
D_0=3b+\deg_YQ\le D.
\tag{3}
$$
一般首核不能无证写成 (3)。

令
$$
h_+=b-\max\{i<b:f_i\ne0\},\qquad
\mathfrak m_3=Y^3t(t-1)^2h_7^3d^2.
\tag{4}
$$
R689 的 $K_F-FH_{\rm top}$ 以整式消去最高项，并在 $C:F=0$ 上保持值。然而它相对于 $K_F$ 的两个 normal 差是
$$
-eH_{\rm top},\qquad
-(\mathcal E^2F)H_{\rm top}-2e\,\mathcal EH_{\rm top}.
$$
以下不删这些差，而计算何时可以由同预算来源一次支付它们。

## 2. 保完整 3C 的最高项修正只有一个

定义有理函数
$$
\boxed{
c_F(t)=b^2\left[
b\mathcal R+
A\left(\frac{\delta^2f}{f}
-\frac{(\delta f)^2}{f^2}\right)
+B\frac{\delta f}{f}
\right].
}
\tag{5}
$$
式中只是有理函数求导；也可简写为
$b^2[b\mathcal R+A\delta^2\log f+B\delta\log f]$，
不使用正特征完整 log。

由 R521/R689 的原最高系数，
$$
(K_F)_{3b}=f^3c_F,\qquad
H_{\rm top}=f^2Y^{2b}c_F.
\tag{6}
$$
置
$$
\boxed{K_F^{[3]}=K_F-c_FF^3.}
\tag{7}
$$

**引理 1。** 在 $k(t)[Y]$ 或特征零分式域中，准确有
$$
\deg_YK_F^{[3]}\le3b-h_+,\qquad
K_F^{[3]}\equiv K_F\pmod{F^3}.
\tag{8}
$$
若要求一个次数不超过 $3b$ 的改变量属于 $(F^3)$，并消去 $K_F$ 的最高 charge，那么该改变量必为 $c_FF^3$。

**证明。** 最高项由 (6) 消掉。其余三次 charge 和至多为 $3b-h_+$。若改变量为 $F^3H(t,Y)$ 且 $Y$ 次数不超过 $3b$，由于 $f\ne0$，$H$ 只能与 $Y$ 无关；最高项又迫 $H=c_F$。证毕。

因此沿同一曲线，整形式的三层恒等式为
$$
\boxed{
K_F^{[3]}|_C=K_F|_C,\qquad
\mathcal EK_F^{[3]}|_C=\mathcal EK_F|_C,\qquad
\mathcal E^2K_F^{[3]}|_C=\mathcal E^2K_F|_C.
}
\tag{9}
$$
(9) 与完整有限 $\Gamma$ 中 $F^3$ 的值是两个不同问题；后者在第五节准确保留。

注意 (7) 一般不再含 R689 的低 charge 因子 $Y^{h_-}$：其常数 charge 可以是 $-c_Ff_0^3$。本文不沿用 R689 的双严格截面消失式。

## 3. 非固定角双极：准确必要条件

先在剩余域或其代数闭包工作，保 $\bar F$ primitive。
设 $t_0$ 是 $f$ 的一个非固定角根：
$$
t_0\notin\{0,1,-1/8\},\qquad h_7(t_0)\ne0,
$$
其重数为 $m$。若 $p\nmid bm$，则
$$
\delta\log f=\frac{mt}{t-t_0}+\text{正规项},
$$
从而
$$
\boxed{
c_F=
-\frac{b^2A(t_0)m t_0^2}{(t-t_0)^2}
+O((t-t_0)^{-1}).
}
\tag{10}
$$
首系数非零，所以极阶准确为二。

在原 (3)、$f_D<p$ 的范围，这里的 $m<p$ 自动成立。
确实，清同一 $d^{C_D}$ 后有
$$
3\deg_tF+\deg_tQ+r\le M_D=f_D+C_D.
$$
又 $C_D\le D/2$、$f_D\ge(9D-1)/2+4$，给
$M_D/3<p$，故 $\deg f<p$。
这不是对未受原来源预算控制的任意因子宣称重数为单位。

令 $V$ 为 $f$ 的非固定角根组成的首一平方自由因子，按原域下降。由 (10)，在 $k[t,Y,d^{-1}]$ 中
$$
\boxed{
d^{-C_D}t^rQ\,\mathfrak m_3K_F^{[3]}
\text{ 没有新有限极}
\quad\Longleftrightarrow\quad
V^2\mid Q.
}
\tag{11}
$$
整除按 $Y$ 的全部系数读取。

证明：在这些根处，$t,d,h_7,t-1$ 都是单位；primitive 性保证 $F$ 不被相应的 $t$ 因子整除。$K_F$ 正规，(10) 的 $c_FF^3$ 有准确双极。故每个根必须且只须由 $Q$ 支付两份零。(11) 在代数闭包逐根成立，因 $V$ 平方自由而下降。

在整层使用 (11) 时，需要所用 $F,Q$ 的同一个实际提升真的保持该因子与 $V^2\mid Q$；只有模 $p$ 的整除不能自动代替模 $p^2$ 的整除。下节给一个不需要额外自由因子的完整整范围。

## 4. 固定角最高系数的整三层返回

假设实际整最高系数具有
$$
\boxed{
f=c\,t^{a_0}(t-1)^{a_1}d^{a_d}
\prod_{\alpha:h_7(\alpha)=0}(t-\alpha)^{a_\alpha},
\quad c\in\mathcal O^\times,\quad a_\bullet\ge0.
}
\tag{12}
$$
如需拆开 $h_7$，在原有限非分歧扩张中工作；所有矩阵结论随后下降。(12) 是对**同一个所用整因子**的条件，不由一个任意提升的约化自动推出。

由
$$
\delta\log f=a_0+
\frac{a_1t}{t-1}+\frac{8a_dt}{d}
+\sum_\alpha\frac{a_\alpha t}{t-\alpha}
$$
直接得到 $c_F$ 的原 Gauss 损失上界
$$
\begin{array}{c|ccccc}
v&v_0&v_{h_7}&v_1&v_d&v_\infty\\ \hline
v(c_F)\text{ 的下界}&0&-8&-3&-4&-2 .
\end{array}
\tag{13}
$$
$t=1$ 的二次极由 $A$ 的一份零降为一次；无穷远
$\delta\log f$ 有常数极限、$\delta^2\log f=O(t^{-1})$，
所以有理次数最多一。整数重数不会制造 $p$ 分母。

因此
$$
\boxed{\mu(t,Y):=\mathfrak m_3c_F=Y^3\mu_0(t)}
\tag{14}
$$
是真正多项式，且其五类 Gauss 值至少为
$$
(1,1,0,3,3).
$$
尤其对每个真实预算 $N$，
$$
\boxed{\mu\mathcal W_N\subset\mathcal W_{N+3}.}
\tag{15}
$$
这由原逐列双向帽直接推出；没有额外角或新的算术来源。

定义
$$
B^{[3]}=
d^{-C_D}t^rQ\,\mathfrak m_3K_F^{[3]},\qquad
B^{\rm old}=
d^{-C_D}t^rQ\,\mathfrak m_3K_F.
$$
由 (7)、(14)，有整个来源上的准确恒等式
$$
\boxed{B^{[3]}=B^{\rm old}-\mu P^{\rm fact}.}
\tag{16}
$$
(13) 使两个三次项的角损失均被原 $\mathfrak m_3$ 支付；
同 R689 全十九个中间链，只是将三次因子 $F^3$ 的导数损失换为 (13) 的固定极。
因此
$$
\boxed{B^{[3]}\in\mathcal W_{D_0+3-h_+}.}
\tag{17}
$$
在
$$
\boxed{D_0+3-h_+\le D}
\tag{18}
$$
下，它是同一个原 $\mathcal W_D$ 的真实来源。特别 $h_+\ge3$ 已足够。

R689 的代表与本代表之差为
$$
\begin{aligned}
&d^{-C_D}t^rQ\,\mathfrak m_3
\bigl[(K_F-FH_{\rm top})-K_F^{[3]}\bigr]\\
&\hspace{2em}=
d^{-C_D}t^rQ\,\mathfrak m_3c_FF(F-fY^b)(F+fY^b).
\end{aligned}
\tag{19}
$$
其最高 charge 同样已降 $h_+$，并由同一角界属于 (17)。
所以在 (12)、(18) 下，R689 的两个确定 normal 补项确由一条同预算实际来源联合支付。不能分别给两个补项另选原像。

若实际提升已满足第三节的 $V^2\mid Q$，相同 Gauss 证明也可给 (17) 的更一般版本。但这并不自动给 (15) 对任意后续 $R$ 成立；后续 $R$ 未必还含 $V^2$。第五节为避免这一未付假设，明确保持 (12)。

## 5. 整个旧目标中的首像吸收

以下固定 (12)、(18)，并固定**原旧目标长度** $2s+\ell$ 及其十三行运输。对任意 $N\ge D$，用
$$
M^{(N)}:\mathcal W_N\longrightarrow Y_{\rm old}
$$
表示同一个 $P_{134}$、charge 四十、$g,t,a$、$\Gamma$、$c_*U_0m_{13}$ 的评价，只扩大来源预算；目标不变。记 $M=M^{(D)}$。

$\mu_{\rm phys}$ 是 (14) 在这个完整目标中的实际值。它整且至少含一份 $w$；不把它当可逆单位。由于原评价是乘法、$c_*U_0$ 和 $w^{13}$ 都保留，整有
$$
\boxed{
M^{(N+3)}(\mu H)=
\mu_{\rm phys}\,M^{(N)}(H).
}
\tag{20}
$$
有限截断没有删掉未知输入尾：源评价截断外乘 $w^{13}$ 后已在旧目标外，$\mu_{\rm phys}$ 的非负阶只使其更深。

若同一个 $P^{\rm fact}$ 的约化属于 $\ker\bar M$，(16)、(20) 立刻给
$$
\boxed{
\overline{M^{(D+3)}B^{\rm old}}
=\bar M\,\overline{B^{[3]}}
\in\operatorname{im}\bar M.
}
\tag{21}
$$
如果已知更强的 $\bar P^{\rm fact}\in\ker\bar J$，同式也在原完整 $J$ 中成立。

这是真正的旧首像成员性，不只是在 $C$ 或第一 normal 层上的相同值。原 $\bar\Gamma$ 中的 $F^3$ 可以活着，但 (21) 使用的是同一个实际首核及整个乘积恒等式 (20)，没有直接宣布 $F^3=0$。

因而在显示范围中，不能以 $B^{\rm old}$ 的某个曲线 forcing 单位证明旧首余核非零。它的原首像已由 (17) 的同预算来源吸收。下一位的差别如下完整保留。

## 6. 同一个 R 的顶三 charge：完整第一提升

固定一个实际提升
$$
P_2=P^{\rm fact}+pR\in\mathcal W_D,\qquad MP_2\in p^2Y_{\rm old}.
\tag{22}
$$
这比只知首核更强；不从 (21) 假定 (22) 可解。

按原 canonical charge 直和，令
$$
\Pi_{\le D}:\mathcal W_{D+3}\to\mathcal W_D,\qquad
\Pi_{>D}=1-\Pi_{\le D}.
$$
这是实际原列的整投影，不是物理 jet 投影。定义
$$
\boxed{C_R=\Pi_{>D}(\mu R).}
\tag{23}
$$
若 $R=\sum_{n=0}^DY^nR_n(t)$，则准确有
$$
\boxed{
C_R=
\sum_{n=\max(0,D-2)}^D
Y^{n+3}\mu_0(t)R_n(t).
}
\tag{24}
$$
这里只有原 $R$ 的最后三条 charge；它们各自包含全部原自由角系数，不能当三条自由目标列。来源秩上界是
$$
\sum_{n=\max(0,D-2)}^D(e_{n+1}+1),
$$
并非已经算出的物理秩。

取真正同预算来源
$$
Z_2^0=B^{[3]}-p\Pi_{\le D}(\mu R).
$$
由 (16)、(20)，整准确有
$$
\boxed{
MZ_2^0=
M^{(D+3)}B^{\rm old}
-\mu_{\rm phys}MP_2+pM^{(D+3)}C_R.
}
\tag{25}
$$

记 $F_{\rm old}=M^{(D+3)}B^{\rm old}$。
若要求表示它的来源首类固定为 $\overline{B^{[3]}}$，则
$$
\boxed{
F_{\rm old}\in M(Z_2^0+p\mathcal W_D)+p^2Y_{\rm old}
\iff
[\overline{M^{(D+3)}C_R}]=0
\text{ in }\operatorname{coker}\bar M.
}
\tag{26}
$$
证明：由 (22)、(25)，所需余项模 $p^2$ 恰为
$-pM^{(D+3)}C_R$，同预算的 $pS$ 只能补 $p\bar MS$。

若不固定这个首来源类，而允许加任意原首核，那么 (26) 右边相应改成在
$$
C_2(M)=\operatorname{coker}\bar M/
\beta_1(K_1(M))
$$
中为零。此时增加的正是原首次 Bockstein 像，不删去它。

(26) 的 $C_1$ 类对 (22) 中同一 $P^{\rm fact}$ 的第一提升选择不变：
若 $R$ 改为 $R+Q$ 且 $\bar Q\in K_1(M)$，则
$$
\overline{M^{(D+3)}\Pi_{>D}(\mu Q)}
=-\bar M\,\overline{\Pi_{\le D}(\mu Q)}.
$$
这里用的是 (20) 和 $\bar M\bar Q=0$，并不假定 $\mathcal E$ 或 $\mu$ 保持原右核或来源预算。

## 7. 同 P2 的第二余项与原 d2 的准确耦合

假定 (26) 已在 $C_1$ 中通过，固定一个真实 $S\in\mathcal W_D$ 满足
$$
M^{(D+3)}C_R+MS\in pY_{\rm old}.
\tag{27}
$$
定义
$$
Z_2=Z_2^0+pS.
$$
它满足 $MZ_2-F_{\rm old}\in p^2Y_{\rm old}$。由同一个 (25)，其完整第二代表准确为
$$
\boxed{
\Omega_{P_2,S}=
\overline{\frac{M^{(D+3)}C_R+MS}{p}
-\mu_{\rm phys}\frac{MP_2}{p^2}}
\in Y_{\rm old}/pY_{\rm old}.
}
\tag{28}
$$
两个除法分别由 (27)、(22) 支付。第二项是同一个原 $P_2$ 的完整第二 forcing，乘的是实际 $\mu_{\rm phys}$，不只是一个曲线值。

对这个固定 $Z_2$，存在同源 $T\in\mathcal W_D$ 使
$$
M(Z_2+p^2T)\equiv F_{\rm old}\pmod{p^3}
$$
当且仅当 (28) 在 $C_1(M)$ 中为零。若保首来源类
$\overline{B^{[3]}}$ 而允许改变第一修正，则相应的准确类在 $C_2(M)$ 中读取：改变 $S$ 的模 $p$ 首核部分恰加上 $\beta_1(K_1)$。不固定首来源类时还需进一步保原不同 $K_2$ 来源的第二像，本文不省略这一额外自由度。

特别，(28) 不能拆成“顶三 charge 项为零”和“原 $d_2$ 为零”两条断言。$\mu_{\rm phys}$ 至少含一份 $w$，在旧有限目标上未必单射；不能把它除掉后宣称原 $d_2$ 消失。

还可直接保第三提升的同一个来源：
若
$$
P_3=P^{\rm fact}+pR+p^2T,
$$
令 $C_T=\Pi_{>D}(\mu T)$ 及
$$
Z_3^0=B^{[3]}-p\Pi_{\le D}(\mu R)-p^2\Pi_{\le D}(\mu T),
$$
则整个旧目标上有
$$
\boxed{
MZ_3^0=
F_{\rm old}-\mu_{\rm phys}MP_3
+pM^{(D+3)}C_R+p^2M^{(D+3)}C_T.
}
\tag{29}
$$
这保留两条十三行、raw 第三 normal 项、实际 $U_1/p$ 和全部低行右逆高尾；没有换 $t,w,\epsilon$ 规范。若 $MP_3\in p^3$，也只能按 (29) 保留两个确定 cap 项，不能把它们视作可独立挑选。

## 8. 对非固定最高系数的同 R 限制

第三节的 $V^2\mid Q$ 可以支付 $B^{[3]}$ 本身，却不支付任意后续 $R$。即使 $P^{\rm fact}$ 的 free 极已经全部抵消，
$\mu R$ 在相同非固定根处仍可能有极，因而不属于 $\mathcal W_{D+3}$。
只有同一个实际 $R$ 还满足相应的 $V^2$ 整除，才可对它使用第五至第七节的原来源 cap 分解；到第三位，$T$ 也必须按实际需要检验。不能用分别选择的 $R$ 去支付来源整性、两条十三行和 (28)。

因此这里存在两种精确范围：

- 固定角最高系数 (12)：整乘子 (15) 对全部原来源成立，(21)–(29) 不漏任何 $R,T$；
- 允许 free 最高根：由 (10)–(11) 逐层支付实际分母；缺少某一层整除时，不能把它的物理正规值免费作为原列。

这是原 normal 消去的实际成本，不是凭局部展开为新的来源授权。

## 9. 与剩余主接口的关系

本篇把 R689 的两个 normal 补项在显示条件下联合返回，给旧完整首像的确切吸收式 (21)。随后把同一个 $R$ 的未支付部分压到原顶三 charge 的实际向量 (24)，并在 (28) 中与同一 $P_2$ 的完整第二 forcing 联立。所有源、目标和截断均已固定。

尚未证明一般实际候选满足 (12) 或 (11)，也未证明 (26)、(28) 的指定类为零或非零。原 $\bar E$ 高尾由 R334/R386/R687 给定，仍须真实代入；本篇不把它改成自由参数。一般首核、R651 的完整 $\mathcal D_\psi$、两个十三行门及全三中央条件的无穷素数结论继续开放。

依赖：[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)、[R514](R514-cubic-forcing-return-and-actual-mirror-tail-normal-form.md)、[R521](R521-exact-fixed-boundary-quotient-and-cubic-forcing-residue.md)、[R689](R689-original-integral-top-charge-reduction-and-complete-forcing-return.md)；原首核/第二余核及同修正范围见 [R449](R449-relative-second-cokernel-and-complete-carry-exact-sequences.md)、[R479](R479-original-carry-graph-and-two-normal-jets.md)、[R651](R651-original-higher-critical-branch-lift-and-complete-second-forcing.md)、[R687](R687-original-cm-three-digit-matrix-and-complete-same-correction-transport.md)。

本篇为全参数有理函数、整来源和有限矩阵证明；没有新增可重算数据或数值扫描。
