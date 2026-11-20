# R927 — 原 yF 极次数：完整混合核的180次除子与全部 cusp 修正

日期：2026-11-20。**状态：完整144维混合核的180次极余除子、原yF的全部尖点修正公式及有限局部接受门已证明；§6–7进一步严格给dF=2160+9(e−z)及两个既有有限代数的完整读数门；§9已实际PASS e=0、z=96、dF=1296；完整pole ideals、四交除子及shadow仍待。**

本篇只针对 R924§15 已实际 PASS 的 $r=29$ 原约化。固定原 $k=\mathbf F_{29^2}$、原 $B=X_0(867)$、$g_B=85$，以及原中央退化 $\pi=\pi_2:Y=X_0(3468)\to B$，$\deg\pi=6$。以下180来自该实际有限域完整核，不来自特征零模次数或一个所选分母。R873 的特征零次数结果不能替代此处的约化计算。

## 1. 先区分原截面、原 sign 坐标与源参数

记

$$
S_B=\frac{3E_2(Q^3)-E_2(Q)}2=-D_Q\log T,
\quad L=\Omega_B(\mathcal C_B),\quad
D_S=\operatorname{div}_L(S_B)=2Z_{\rm ell},\quad\deg D_S=204.
\tag{1}
$$

这是 R882§6、R924§3 的固定权二截面；不是原 deck involution $S:z\mapsto z+1/2$。在 $Y$ 的 $u$ 参数中，真正的拉回截面是

$$
S_Y=\pi^*S_B=2S_B(u^2),
\tag{2}
$$

而非未带退化微分因子的 $S_B(u^2)$。R878、R882§7 的原 sign 权六坐标为 $V_{\rm sign}=\eta(Q)^{12}y_{F,17}$。它在 $B$ 上的原标量函数是

$$
v_F=V_{\rm sign}/S_B^3
    =A_F/(B_FS_B^3),\qquad A_F\in H^0(B,L^5),\quad B_F\in H^0(B,L^2).
\tag{3}
$$

这里 $B_F$ 是原分母截面，不能与原 level9 端点坐标同名混用。对(3)作退化拉回时，分子与分母的权十因子 $2^5$ 完整相消；对 $V_{\rm sign}/S_B^3$，相消的是 $2^3$。不能只把分母换为 $S_Y^3$ 而忘记分子同权拉回。

令 $\xi=y_s$、$v=\xi^2-1$。R882、R883 已识别的原函数给

$$
T=\frac{\xi^2(\xi^2-9)^2}{(\xi^2-1)^2},\qquad
\varepsilon=-\frac{\xi^3(\xi^2-9)^3(\xi^2-1)}{(\xi^2+3)^6},
\qquad
y_F=\frac{\pi^*v_F}{\varepsilon\theta_{17}^3}.
\tag{4}
$$

这里 $y_F$ 是已经按原 $\theta_{17}$ 扭曲至 $E_0$ 的消费者坐标，$\theta_{17}^6=17$ 且在 $r=29$ 为非零常数，不改变任何地方阶。特别保留

$$
\varepsilon^2=\pi^*\frac{T^3}{(T+27)^4},\qquad
R_F^3=v_F^2\frac{(T+27)^3}{T^3}-\frac{17}{T+27}.
\tag{5}
$$

后式就是 R926 已核的原身份；不能改成 $(v_F^2-17)$ 乘一个错误的简写幂。

## 2. 完整混合核准确给 $\deg D'=180$

定义有效除子

$$
D'=\bigl(\operatorname{Pole}_B(v_F)-3D_S\bigr)_+.
\tag{6}
$$

R924§15 的完整1429行系统，其全部核维数实际为144；这是原所有 $(A,B)\in R_5\oplus R_2$ 满足 $A=v_FBS_B^3$ 的空间。令某点的 $v_F$ 阶为 $a$，$S_B$ 的截面零阶为 $s$。一个 $B\in R_2$ 可以属于分母投影，恰当且仅当

$$
\operatorname{ord}(B)\ge\max\{-a-3s,0\}=D'(\text{该点}).
\tag{7}
$$

一旦满足(7)，$A=v_FBS_B^3$ 是唯一的全局 $R_5$ 截面。因此这个**完整**核的分母投影准确是

$$
H^0(B,M),\qquad M=L^2(-D'),\qquad h^0(M)=144.
\tag{8}
$$

若 $H^1(M)\ne0$，Serre 对偶给非零 $M\to\omega_B$。它在整曲线上单射，所以 $h^0(M)\le h^0(\omega_B)=85$，矛盾。故 $H^1(M)=0$。Riemann–Roch 给

$$
144=(408-\deg D')+1-85,
\qquad\boxed{\deg D'=180.}
\tag{9}
$$

这不声称 $\operatorname{Pole}(v_F)$ 本身次数180；(6)中的 $3D_S$ 不能丢掉，也不能将所选 $B_F$ 的全部零点都当作 $D'$。

## 3. 非 cusp 部分的完整消去

由 R883(B1)，

$$
T+27=\frac{(\xi^2+3)^3}{(\xi^2-1)^2}.
$$

在 $B$ 上 $\operatorname{div}_0(T+27)=3Z_{\rm ell}$，故

$$
\operatorname{div}_0(\xi^2+3)=\pi^*Z_{\rm ell},
\qquad \pi^*D_S=2\operatorname{div}_0(\xi^2+3).
\tag{10}
$$

(4)在这些点没有分子零点，极阶为六倍 $\operatorname{div}_0(\xi^2+3)$；其余非 cusp 点既无零也无极。因此

$$
\operatorname{Pole}(\varepsilon)=3\pi^*D_S,
\qquad
\operatorname{Pole}(y_F)|_{Y\setminus\mathcal C_Y}
=\pi^*D'|_{Y\setminus\mathcal C_Y}.
\tag{11}
$$

逐点证明为：若 $Q\mid c$、$e=e(Q/c)$，则非 cusp 处
$v_Q(y_F)=e\,[v_c(v_F)+3D_S(c)]$，取负部即(11)。这包含原 $D_S$ 上 $v_F$ 的任意高极与共零，不需要先计算每个 RF 剩余值。

## 4. 全部 cusp 的准确修正公式

对 $B$ 的每个**闭** cusp $c$，记

$$
t_c=v_c(T)\in\{289,1,-289,-1\},\quad
a_c=v_c(v_F)\in\mathbf Z,\quad
d_c=[\kappa(c):k],
$$

$$
\delta_c=\begin{cases}3t_c/2,&t_c>0,\\-t_c/2,&t_c<0.\end{cases}
\tag{12}
$$

$S_B$ 在每个 cusp 是 $L$ 的单位截面，因为其对数留数为 $-t_c\ne0$ 于特征29，故 $D'(c)=\max(-a_c,0)$。由(5)，在任一 $Q\mid c$ 上

$$
v_Q(\varepsilon)=e(Q/c)\delta_c,
\qquad
\operatorname{Pole}(y_F)(Q)=e(Q/c)\max(\delta_c-a_c,0).
\tag{13}
$$

R883 附录B已证明各 cusp 上恰有三条几何分支，指数各2；因此(13)为整数。为对原 $k$ 的闭点严格计数，使用完整基本等式
$\sum_{Q\mid c}e(Q/c)[\kappa(Q):\kappa(c)]=6$。将(11)与全部 cusp 的(13)相加，得到

$$
\boxed{\displaystyle
d_F=\deg\operatorname{Pole}_Y(y_F)
=1080+6\sum_{c\in\mathcal C_B(k)_{\rm closed}}d_c
\bigl[\max(\delta_c-a_c,0)-\max(-a_c,0)\bigr].}
\tag{14}
$$

所以

$$
\boxed{\displaystyle
\frac{d_F}{6}=180+\sum_c d_c
\bigl[\delta_c-\min\{\max(a_c,0),\delta_c\}\bigr].}
\tag{15}
$$

这里 $\delta_c$ 可为半整数；没有声称每一项或 $d_F/6$ 必为整数。乘回6后的(14)是完整整数次数。全部 $d_c$ 保留，不把36个几何 cusp 误当36个 $k$-有理 cusp。

每项修正非负，因而同一 $r=29$ 原约化严格有 $d_F\ge1080$。这个下界来自(8)的实际144维核及完整局部几何，未借用特征零模次数。**(14)尚不给一个未实际读取的精确 $d_F$ 数字，更不允许直接以240或2160代入消费者。**

## 5. 两个标号纤维可覆盖全部底 cusp，但仍须读真实局部值

R883(B1) 的六个 $\xi$ 值均在原 $k$ 中。对一个 $t_c=w>0$ 的底 cusp，原完成局部扩张在 $\xi=0,3,-3$ 各有一条二次分支；对 $t_c=-w<0$，相应为 $\xi=1,-1,\infty$。因为 $w=1$ 或289为奇数，每条局部扩张经除去偶幂后是 tame Eisenstein 二次扩张，剩余域不变。三条分支的次数已总计6，所以没有其它分支。

因此选择完整 $\xi=0$ 纤维的约化支集，准确覆盖 $T=0$ 的全部底 cusp，各一次、同一剩余次数；选择完整 $\xi=\infty$ 纤维，则准确覆盖 $T=\infty$ 的全部底 cusp。这个结论来自原已标号的 $Y/B$ 归一化，而非按两个点标签的相似性配对。已有六厚 cusp 纤维的实际原666坐标可用来保其身份。

但是(14)仍需这些点上原 $v_F$ 的准确截断正零阶。一个可终止的有限接受门是：取(3)的真实 $A_F,B_F$，在每个底 cusp 的单位框架 $S_B$ 下，令 $b_c=\operatorname{ord}_c(B_F/S_B^2)$。先以完整局部商读出

$$
0\le b_c\le\lfloor408/d_c\rfloor.
\tag{16}
$$

随后只需读取 $A_F/S_B^5$ 到阶 $b_c+\lceil\delta_c\rceil$：若在此前首次非零，得到准确 $a_c$；若整个此前窗为零，则已证 $a_c\ge\lceil\delta_c\rceil$，对应修正为零。$a_c\le0$ 时修正统一为 $\delta_c$，不必继续读取负阶的大小。若在 $Y$ 上实施，所有阶与上述门相应乘2，并用真正的 $\mathfrak q_Q$ 幂与原单位框架；不能把289重纤维的基参数误作局部均匀参数。

这给(14)一个有限、同原函数的局部接受门。它可先准确读总次数以决定消费者的循环呈示，但**不替代后续完整 pole ideal**；完整交理想仍须保每个真实极点及其重数。任何更小的局部门必须另行证明，不能由未读取的尖点值推测。


## 来源与准确接受范围

- [R924§3、§6、§15](R924-original-section-divisor-algebras-and-shadow-interface.md)：原DS、混合全核的完整性及其实际144维回执；[run44723394686/job136244599223](https://github.com/Rogerhu12/math-research-public/actions/runs/44723394686/job/136244599223)，source `7ffa56588b1146d192114d6e4267d51affb46e13`，result `0a8cc7cf92e277a00748c62bb8ee6bbd30fa3801fe839ebbe22e089a008e7f9f`。
- [R926§8–10](R926-original-cube-roots-in-sections-and-complete-identities.md)：同原RF全局身份、原根极次数及完整分母投影；不会以其240代替yF的极次数。
- [R882§6–7](R882-original-degree18-source-model-and-two-endpoint-coordinates.md)、[R883及附B](R883-original-relative-six-shadow-and-complete-boundary.md)：同原sign坐标、完整微分退化、epsilon/Artin尺度及六次覆盖的所有尖点。
- [R925§12–19](R925-original-ys-affine-rings-and-complete-divisor-ideals.md)：已PASS的原306整环、六厚纤维，以及正运行的原闭点/局部值与完整消费者；本篇给精确次数的有限门，不代任何完整有效交理想或原shadow。

本篇为纯符号推导，没有本地数学执行。root全文核完新证明，并独立从原全核及原epsilon除子得到相同公式；所有r29数值来源均是上述已经公开成功的完整核。


## 6. 用同原 RF 将次数进一步缩成两个有限读数

本节仍只针对已实际取得 R924§15、R926§8–9 回执的 $r=29$。沿用前节的原函数、原 $S_B,S_Y$、原 $k=\mathbf F_{29^2}$，不更换原 $v_F$ 或 $R_F$。特别已经严格知道

$$
\deg D'=180,\qquad \deg\operatorname{Pole}_B(R_F)=240,
\qquad
R_F^3=v_F^2\frac{(T+27)^3}{T^3}-\frac{17}{T+27}.
\tag{16}
$$

令 $Z_{\rm reg}\subset Z_{\rm ell}$ 为原 $R_F$ **没有极点**的约化子除子，包括 $R_F$ 的零点；定义

$$
e=\deg Z_{\rm reg}
=\sum_{c\in|Z_{\rm ell}|,\,v_c(R_F)\ge0}[\kappa(c):k].
\tag{17}
$$

令 $c_*$ 为原 $T$ 唯一极阶289的底 cusp，定义

$$
z=\max\{v_{c_*}(R_F),0\}.
\tag{18}
$$

该 cusp 是原 $\mathbf F_{29}$-有理点：它是原 $\mathbf F_{29}$ 函数 $T$ 的极除子中唯一具有此重数的几何点，故被 Frobenius 固定。于是(18)不漏剩余次数因子。

**命题。** 对同一原 $r=29$ 约化，准确有

$$
\boxed{d_F=2160+9(e-z).}
\tag{19}
$$

这里 $e,z$ 尚须由下述完整有限门实际读取；本式不把它们预设为零或相等。

### 6.1 每一类地方的完整阶比较

写 $a=v_c(v_F)$、$b=v_c(R_F)$。在非 cusp 且不属于 $Z_{\rm ell}$ 的点，(16)的两个系数都是单位。若 $a<0$，则 $3b=2a$；若 $a\ge0$，则 $b\ge0$。因此这里的 RF 极除子恰为 $\tfrac23D'$。该有理倍数逐点为整数，这是原立方恒等式的结果，不是整数舍入。

在 $Z_{\rm ell}$ 的任一点，$v_c(T+27)=3$，(16)右侧两项的阶为

$$
2a+9,\qquad -3.
\tag{20}
$$

若 $a<-6$，第一项严格支配，故
$-b=1+\tfrac23(-a-6)=1+\tfrac23D'(c)$。若 $a>-6$，第二项严格支配，故 $b=-1$、$D'(c)=0$。若 $a=-6$，则 $D'(c)=0$；未相消时 $b=-1$，相消时由于 $3b$ 为三的倍数，必有 $b\ge0$。故在**所有非 cusp** 上严格有除子等式

$$
\operatorname{Pole}(R_F)|_{B\setminus\mathcal C_B}
=\tfrac23D'|_{B\setminus\mathcal C_B}
+Z_{\rm ell}-Z_{\rm reg}.
\tag{21}
$$

再看 $T$ 零阶为 $w\in\{1,289\}$ 的 cusp。两项的阶为 $2a-3w$ 与0，它们不可能相等，因为 $w$ 为奇数。因此

$$
\operatorname{Pole}(R_F)(c)=\frac{\max(3w-2a,0)}3.
$$

令 $C_+$ 为前节(14)中全部 $T=0$ cusp 的带剩余次数修正和。因 $D'(c)=\max(-a,0)$，逐点相减给

$$
\deg\operatorname{Pole}(R_F)|_{T=0}
-\tfrac23\deg D'|_{T=0}=\tfrac23C_+.
\tag{22}
$$

在 $T$ 极阶为 $w\in\{1,289\}$ 的 cusp，两项阶变为 $2a$ 与 $w$。仍因奇偶不同不可能相等。如果 $2a>w$，则 $3b=w$，而 $3\nmid w$，矛盾。因此必有

$$
2a<w,\qquad a\in3\mathbf Z,\qquad b=2a/3\in2\mathbf Z.
\tag{23}
$$

所以这侧的 RF 极除子仍为 $\tfrac23D'$。把(21)–(23)按完整闭点次数相加，使用 $\deg Z_{\rm ell}=102$，得到

$$
240=\tfrac23\cdot180+102-e+\tfrac23C_+,
\qquad \boxed{C_+=27+\tfrac32e.}
\tag{24}
$$

令 $C_-$ 为全部 $T=\infty$ cusp 的修正和。由(23)，每项为
$w/2-\max(a,0)$。所有这些 $w$ 的带剩余次数和为306。极阶1时 $a\in3\mathbf Z$、$a<1/2$，所以 $a\le0$，不可能产生 RF 正零阶。唯一可能的正零位于 $c_*$，且其 $a$ 的正部为 $3z/2$。于是

$$
\boxed{C_-=153-\tfrac32z.}
\tag{25}
$$

将(24)、(25)代入前节 $d_F=1080+6(C_++C_-)$，恰得(19)。每个点的极与共零都在以上分类中保留，没有以选中分母的零次数代替真实极次数。

### 6.2 已严格得到的整除、范围与循环分支

原 $R_F$ 定义于 $\mathbf F_{29}$，这是 R926 RF 全局身份中无 $\omega$ 分量的实际门。原 $Z_{\rm ell}$ 由51个 $\mathbf F_{29}$ 上次数二闭点组成，无有理点。因此其 Frobenius 不变的子集 $Z_{\rm reg}$ 总几何次数为偶数，$0\le e\le102$。由(23)在 $w=289$ 处，$a\le144$，故

$$
z\in\{0,2,4,\ldots,96\},\qquad e\in\{0,2,4,\ldots,102\}.
\tag{26}
$$

特别

$$
\boxed{d_F\in18\mathbf Z,\quad1296\le d_F\le3078,\quad d_F\ne2256,}
$$

$$
\boxed{d_F<2256\iff e-z\le10;\qquad d_F>2256\iff e-z\ge12.}
\tag{27}
$$

这些界和等价式已经是实际原 $r=29$ 输入的严格推论；准确的 $e,z,d_F$ 数值仍未由此证明自动读出。

## 7. 两个读数可由既有有限代数完整取得

以下给一个不要求 RF 在 $D_S$ 上预先有单位分母的有限接受门。它使用原 R926 的**整个900维 RF 核**，而非任意选中的一条分式。

### 7.1 分母投影为何准确识别原极点

记 $P_R=\operatorname{Pole}(R_F)$，旧 RF 的完整 $R_6\oplus R_6$ 核为

$$
K_R=\{(N,D):N=R_FD\}.
$$

其分母投影准确为 $H^0(B,M_R)$，其中

$$
M_R=L^6(-P_R),\qquad \deg M_R=1224-240=984,
\qquad h^0(M_R)=900.
\tag{28}
$$

因为 $984\ge2g_B$，该线丛全局生成。具体地，对任意几何点 $c$，$\deg M_R(-c)>2g_B-2$，故 $H^1(M_R(-c))=0$，其全局截面到点纤维的映射满射。将截面看成 $L^6$ 截面时，全部分母的共同零除子因而**恰等于 $P_R$**，没有额外基点。因此

$$
R_F\text{ 在 }c\text{ 正则}
\quad\Longleftrightarrow\quad
\exists(N,D)\in K_R:\ D(c)\ne0.
\tag{29}
$$

“全900维”不能缩成所选一个分母。所有来源须保同一个原 M2 owner、整格及 recipes；该整个核已由 R926 的完整2313项门识别。

### 7.2 从原204维 $D_S$ 代数读取 $e$

沿用 R924 的实际 $A_S=\Gamma(D_S,\mathcal O)$ 以及原 $h\in R_2$ 的完整单位门。$h^3$ 是 $L^6|_{D_S}$ 的单位框架。对于一个六元原乘积 recipe，可在同一实际代数中直接求

$$
\frac{f_{i_1}\cdots f_{i_6}}{h^3}
=\left(\frac{f_{i_1}f_{i_2}}h\right)
 \left(\frac{f_{i_3}f_{i_4}}h\right)
 \left(\frac{f_{i_5}f_{i_6}}h\right).
\tag{30}
$$

每个括号来自已有完整 $R_2/S_BR_1$ 坐标，乘法是已经认证的全非约化乘法；无需新造 $R_6$ 零除子模型。用全部原1140个 R6 recipe 及完整核的900条分母行，评价所有 $D/h^3$。原120维基必须与 cube 的整基通过相同205前缀/实际变换核对。

令 $B_S=A_S/\sqrt0$，其 $\mathbf F_{29}$ 维数102。实际 DS 的 $F^2$ 已是原可分子代数投影，可保完整回代后在其像内计算。对全部分母的约化值 $\bar D/h^3$，求它们在 **整个 $B_S$ 中生成的理想**

$$
J=(\bar D/h^3:(N,D)\in K_R)\subseteq B_S.
\tag{31}
$$

有限约化代数是原剩余域的直积，理想在某个因子上为整个域，当且仅当至少一个生成元在那里非零。由(29)，这恰是 $Z_{\rm reg}$。因此

$$
\boxed{e=\dim_{\mathbf F_{29}}J.}
\tag{32}
$$

这等于在原 $k$ 上基变换后的完整几何次数，自动把每个二次点的两个原共轭因子都计入，无需另选 $\omega$。接受门须实际包含所有900生成元。若只知道任意一组分母值，必须求全部乘法闭包，不能将裸restriction秩当成(31)。但本处还可以利用已付的完整原空间，进一步严格省去闭包：

$$
\deg M_R(-Z_{\rm ell})=984-102=882>2g_B-2=168,
$$

故H1(M_R(-Zell))=0，完整900维H0(M_R)到M_R在Zell上纤维的restriction满射。在RF有极的因子，M_R→L6的纤维映射为零；在RF正则的因子，它是同一一维剩余域空间的同构。因此**全部900条分母的线性像本身就恰是(31)的完整理想**，其完整restriction矩阵的Fp秩准确等于e。这是原Riemann–Roch满射的推论，不是对任意分式或选中子核的秩猜测。

实际实现仍须从整个核求完整映像，保同一R6/原M2 frame、F²约化投影及全102维剩余代数。完整已分解的51个原因子也可逐个核“有无非零分母”，以真实剩余度加权回验(32)。最终核0≤e≤102且e为偶数。

### 7.3 从既有289重无穷 cusp 因子读取 $z$

选择原 $\xi=\infty$ 纤维中唯一厚度289的分量 $Q_*$。前节已证明它通过原 $\pi_2$ 映到 $c_*$，指数2、剩余域不变。令 $s=1/\xi$。已有完整六 cusp 回执给这一个原分量的完整代数

$$
A_*\simeq\mathbf F_{29}[\nu]/(\nu^{289}),
\tag{33}
$$

并保真实 $\nu$、全部289幂基和原666个 Y 截面标签。因此它是原 $Q_*$ 的全部289阶局部商，不是只保约化点。

在无穷图表用原单位截面 $J_0=\xi^4J$ 作框架。对全部原分母以及所需分子，读

$$
\pi_2^*D/J_0^6,\qquad \pi_2^*N/J_0^6
\quad\text{于整个 }A_*.
\tag{34}
$$

它们可由原120条基的 $\pi_2$ 拉回、已认证666基在该因子的全坐标及同一六元 recipes 乘法得到；保完整 $2^6$ 退化因子。由于 $J_0$ 在 $\xi=\infty$ 为单位，此框架没有添加或删除局部零阶。

若全部900条分母的剩余值都为零，(29)证明 $R_F$ 在 $c_*$ 有极，故 $z=0$。若有非零分母，按固定核行顺序选择首条，并取**同一核行**的配对分子。该分母在整个 $A_*$ 中可逆；实际核完整乘法逆后得到原 $\pi_2^*R_F$。

把所得元素读到已认证的 $1,\nu,\ldots,\nu^{288}$ 幂基。记首个非零系数的指标为 $j$。由(23)、(26)和 $e(Q_*/c_*)=2$，必有

$$
\boxed{0\le j=2z\le192,\qquad j\equiv0\pmod4.}
\tag{35}
$$

所以289阶已严格足够，不需要猜未知尾。若所有289项均零，或出现(35)以外的阶，应拒绝本门，而不能将其当作一个允许的更大零阶。最后取 $z=j/2$，再以(19)、(27)读取准确 $d_F$ 和循环分支。

这两门只读取支集和一个足长的完整局部值；所有 frame、kernel 与坐标都来自原已认证对象。它们仍不替代全局完整 pole ideals、四个完整交理想、实际输出残值或完整 trace；在实际公开回执完成以前，不填 $e,z,d_F$ 数字。


§6–7经root独立逐类地方阶推导和全文核，theta另独审完整frame/2^6/289厚度；§7.2的满射补强亦双审。全部均为符号推导，实际e、z仍未填写。

## 8. 两个完整有限读数的同进程公开实现

2026-11-20：已把§7落实为[原有限读者](../scripts/original_yF_finite_pole_degree.py)与[公开producer](../scripts/produce-original-yf-finite-pole-degree.py)。[完整实现契约](../notes/2026-11-20-original-yF-finite-reader-contract.md)逐项说明输入、框架、真实有限代数、回代与接受门。当前只登记已审源码和公开请求；**尚未取得本读者的实际PASS，不填写e、z或dF。**

本入口严格只接受r=29。宿主先鉴定既有原F/P的完整特征零PASS，经stdin送入断网、只读源码的固定Sage10.6容器；token仅留宿主读者。数学进程按顺序重建原cube、817项完整DS与Frobenius、2453项正规化及全部六厚cusp。全部原对象保留在同一进程，helper不重建另一份模型或有限域。

degree180的依据也在同进程中：必填`cube_receipt`含刚完成的原混合F核144、秩1116、完整0..1428窗及原S³坐标。helper核同选中坐标和来源，再引用§1的RR证明。RF的900×2280完整核与6941项原全局恒等式另核原回执，并由同一完整核给极度240；不能以紧缩R2中的单个分式替代全900条分母。

e门把完整204维DS的F²约化投影逐分量回到51个原二次残域，核204→102→204两矩阵恒等式。全部R6 recipes以真实R2成对乘积和单位h³求值；完整900×102限制像除核秩外，还逐个比较其标准行基与全部活跃因子的完整直积理想。所有非约化输入和204坐标回代保留，回执准确声明只对R6计算约化值。

z门重新核原∞因子的全部289幂链、666截面值和120×666的真实π2矩阵，保每条recipe的2⁶倍率。对全部900条分母读剩余值；有单位时只用同一核行的配对N/D，逐次求完整289项逆，最后回到原306维代数核D·D⁻¹=e及D·RF=N。真正首阶须在0..192且为4的倍数；全部分母剩余值零才由已证全局生成性给z=0。

返回值保e、z、dF、原全部上下文和两读数的完整矩阵。公开回执只输出度数、接受门、原点身份、源码和矩阵哈希；不写重算数据文件。最终仍明确区分约化精确dF、完整全局pole ideals、四大交理想、shadow及无穷p结论，后四门未由本实现支付。

| 文件 | SHA256 |
|---|---|
| `original_yF_finite_pole_degree.py` | `5d577d06decc79026ae0b1f454ade3d3a4602864e5feca4d14b9389ab4d09fb4` |
| `produce-original-yf-finite-pole-degree.py` | `4d5e93be8cf6807dc166221f3d09ba392abcdd6c637139d6baff3f55905a14ea` |
| `launch-original-yf-finite-pole-degree.py` | `f0a74ee2c5a92c7196303b4b995593183321f5c0ff8014f3a04570d6ce8060ce` |
| `ci/original-yf-finite-pole-degree-request.json` | `e84c6ea21708c02d5627e57cf806da75766c1fe86c055ed8ba642df24b0dfbfc` |
| `.github/workflows/rank2-sha-original-yf-finite-pole-degree.yml` | `759611eef00da88e6638ee89f6e86741c65d003c9b5cdaf7c3da74dd90318eb5` |

root已全文核helper、四前端与原生产者接口；theta独审完整RR/DS/289/π2读数，deep另独审全部真实owner/receipt/labels/矩阵shape与调用契约，global独审root四前端。AST、JSON/YAML及同一25项源码manifest静态检查通过，未在本地执行数学。请求固定原F/P认证source/run/job/result，实际运行回执另补。

公开请求已实际启动：run [44736604477](https://github.com/Rogerhu12/math-research-public/actions/runs/44736604477)，job `136289459332`，source `8e241304372d5844ac7387350fe8875f1a72d913`，创建于2026-11-20 12:32:17 UTC。当前仍运行，未登记数学PASS；原maps run44732115204及原Fp²局部 run44730598782也仍在其固定来源上运行。


## 9. 原两个有限读数实际PASS：e=0、z=96、dF=1296

2026-11-20 12:59:58 UTC，公开任务 [run44736604477/job136289459332](https://github.com/Rogerhu12/math-research-public/actions/runs/44736604477/job/136289459332) 完整成功。数学源为 `8e241304372d5844ac7387350fe8875f1a72d913`，固定Sage10.6镜像与§8参数；数学段用时1611.7093734379998秒。入口先鉴定同一原F/P特征零完整PASS，随后在同一断网进程重建原cube、DS及六厚cusp，没有从另一个函数或仅一个选中分母读值。

准确结果为

$$
\boxed{e=0,\qquad z=96,\qquad d_F=1296<2256.}
\tag{34}
$$

### 9.1 同原DS的完整零像

原混合F核144与RF完整核900在同一进程被重新核回；前者经§2给D′度180，后者给RF极度240。DS使用全部204坐标、102维真实约化代数以及51个原次数二因子，所有因子的全部900条分母限制秩均为0。原完整R6的1140条recipe经324个实际R2乘积类逐个在全409系数窗核回，并返回全204代数；整幅约化限制像确为零理想，故e=0。不是从一个失败的分母尝试推出不正则。

全部900分母约化值hash：`298d6c2e2c9d47e7c9e1777a138017ee76c96e0cd26136ade29b3cc0cb92ea34`；全部R6约化值hash：`23f8a5d9c9cc29c6ffdd7d1efc72d08bb6c5f9a42459f7064e5fd51d331acbcb`。所有51实际投影及全204回代门都通过。

### 9.2 原∞厚因子的首次非零阶恰为192

同原ξ=∞纤维的长度289原因子、全部连续幂及全部666坐标保持。其原点ID为 `897265026b2258b61c3d7c650427b7b4c542c72592bed4691811d345adb44f52`。原π2的120维底坐标在全部1225系数上核回，真实微分因子2⁶=64与J0=ξ⁴J框架完整保留。

检查全900条分母的剩余值后，原核第0行分母为单位。对该同一配对N,D作完整289长度求逆，逐精度2,4,8,16,32,64,128,256,289核回，再在原306纤维中验证D·RF=N。实际RF值的首非零幂恰为ν^192；完整局部坐标hash为 `2ce88df622ce0fa318a66adb641d8ac066efc6bd869cec86881282c30ad33789`。由原π2在该点的分歧指数2，得到z=96，恰到§7所证有限上界，而不是因截断零误判的值。

### 9.3 原消费者分支和完整长度现在确定

将实际两值代回§6的同原恒等式，给(34)。因此原消费者必须采用

$$
\text{输出 }A_bq_2:\quad A_aq_0-\varphi_rF,
\qquad r=29,
$$

四个有效交除子的完整度数均为

$$
\boxed{2256+29\cdot1296=39840.}
\tag{35}
$$

这只是确定呈示与应核全长度；原完整pole ideals和四个有效E仍须实际构造。按R925§21，在这个已付分支中，求交输入不含b，所以同原E00=E01、E11=E12严格成立；只有完整N/D与两图HNF等验门付后才可共用对象。四个输出的xout/yout及原Artin/两轴迹仍逐pair保留，不能把四个shadow标量合成两个。

本次完整结果hash为 `ed95578b73e57d24793deb8de510058e88b16f95d4dc361d3e2de579fabcfab6`，与公开输出 `RANK2_YF_FINITE_DEGREE_SHA256` 完全相同；完整job日志hash为 `85f2e517baacc9901213a5e22e2b78febbbdd9ae7fdd1bc2e3e90beff4ec4d17`。原helper SHA256 `5d577d06decc79026ae0b1f454ade3d3a4602864e5feca4d14b9389ab4d09fb4`；producer `4d5e93be8cf6807dc166221f3d09ba392abcdd6c637139d6baff3f55905a14ea`。源码与所有参数保§8，重算数据只在公开日志及同进程内，未入库。

仅此r29原约化的精确次数已付；不外推特征零精确度数、r41、ordinary、无穷p或原shadow非零。
