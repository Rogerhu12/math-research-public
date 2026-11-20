# R927 — 原 yF 极次数：完整混合核的180次除子与全部 cusp 修正

日期：2026-11-20。**状态：完整144维混合核的180次极余除子、原yF的全部尖点修正公式及有限局部接受门已证明；真实尖点读数、精确dF及完整pole ideals尚未新增实际PASS。**

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
