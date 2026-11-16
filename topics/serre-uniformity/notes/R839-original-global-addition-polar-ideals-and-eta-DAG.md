# 原全局单位解、三个射影子式与五个原 η 极理想的有限 DAG

日期：2026-11-16。状态：**本文证明一个新的全局分式理想等式，并给出其原来源表达式契约；没有执行新的函数域展开、理想 HNF、Jacobian 化简或高度计算。** 原基准极理想的八生成元已经由实际公开计算取得。原全局 $y=A/B$ 的准确单位解定义则早已登记，本文直接消费，不把 CM 四响应推广成一个未经证明的全局函数。

## 1. 已有的原全局函数，无需等待1186个系数展开

始终保留原 $f=f_4:X_L\to C$、$C:y^2=x^3+b$、$f(c_0)=O$、$\deg f=1206$，以及原 $\phi:X\to Y$。置 $K=\mathbf Q(\zeta)$、$L=K(b)$、$s=1+2\zeta$。原积分坐标仍是 $B_{\rm fld}^is^j$，$B_{\rm fld}=\lambda b$；不能把这里的 $B_{\rm fld}$ 与关系分母截面混淆。

[原单位选行证明](R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)的命题 U.1 已给如下**全局**定义。以原保存的2420阶矩阵、右端及自由列1186作

$$
\xi=M^{-1}r=\operatorname{adj}(M)r/\det M,
\qquad \mathbf b=Z\mathbf c,
\qquad A=\sum_{i=0}^{1233}a_iF_i^{(5)},\quad
B=\sum_{i=0}^{1233}b_iF_i^{(5)}.
\tag{GP.1}
$$

这里 $\mathbf a$ 是 $\xi$ 的前1234坐标，$\mathbf c$ 的1186个主元坐标是其余坐标；原自由列1186为1，其他27个自由坐标为0。准确整数 $Z$、原行列顺序、原未清 Laurent 算子和所有尺度均沿 U2–U8。

原真实单位子式使 $\det M\ne0$；R824 已证明完整核维数28，与该选行核相同。因而已有准确恒等式

$$
A=y_fB,\qquad B\ne0.
\tag{GP.2}
$$

这是完整129阶原关系的几何维数证明，不以518位近似或四个 CM 响应代替全部行。R840 的 $A_0,A_1,B_0,B_1$ 只是对同一个 (GP.1) 作四个线性响应。后继可立即把 $y_f=A/B$ 保存为有限源绑定表达式；不必先展开全部 $L$ 坐标，也不改成另一归一化的关系。

原准确矩阵叶必须仍指向实际1234个 real 行、原 $Z$、R781 的 $R_m,\kappa$ 与原 chart，不能只有一个无从恢复的“存在可逆矩阵”标签。原旧提升只可作为该解的合法模值，不替代这些准确叶。

## 2. 原基准极理想已经有具体八生成元

令 $E_f=(y_f)_\infty$，并按 [R805](../results/R805-original-two-affine-charts-and-small-polar-divisor-adapter.md) 保留

$$
E_f=\mathcal B+3D,
\qquad \mathcal B=\mathcal D_{\rm cusp}+P_0,
\qquad \deg\mathcal B=21,\quad\deg D=395.
\tag{GP.3}
$$

原固定21点铅笔为 $u_*,v_*\in V_2$。原完整 $H^0(3H-D)$ 的295个单位解基记为 $w_0,\ldots,w_{294}$。公开运行
[43780953543](https://github.com/Rogerhu12/math-research-public/actions/runs/43780953543)，source
`a43b6afad1ffdbcb0357eda63b7683df3c5d2c93`，已实际取得

$$
a_*=w_0,\qquad b_*=\sum_{i=0}^{294}w_i,
\qquad \operatorname{rank}(a_*V_3+b_*V_3)=1111.
\tag{GP.4}
$$

该真实子式为 $633901576\bmod1000000753$。原五纤维证明只用秩下界，未假设整个 $V_6$ 评价单射。其原43个完成阶段及14.88603302秒是实际记录，不是本篇重新运行。完整实际来源见 [R845 正式结果](../results/R845-certified-original-D-pencil-and-eight-pole-generators.md)。

按 [两截面与八生成元证明](R839-original-D-pencil-and-eight-generator-pole-ideal.md)，在 $U_\tau=Y\setminus\operatorname{div}\tau$ 上

$$
I:=I_{E_f}=
\left(\frac{u_*a_*^3}{\tau^{11}},
\frac{u_*a_*^2b_*}{\tau^{11}},
\frac{u_*a_*b_*^2}{\tau^{11}},
\frac{u_*b_*^3}{\tau^{11}},
\frac{v_*a_*^3}{\tau^{11}},
\frac{v_*a_*^2b_*}{\tau^{11}},
\frac{v_*a_*b_*^2}{\tau^{11}},
\frac{v_*b_*^3}{\tau^{11}}\right).
\tag{GP.5}
$$

$U_\sigma$ 图只把分母换成 $\sigma^{11}$；重叠上整组生成元乘 $(\tau/\sigma)^{11}$。它是同一嵌入函数域的有效 Cartier 理想，包含原全部重数，不仅是支撑或 Picard 类。

该实际 DAG 的来源为 `R839-pole-original-D-and-Ey-eight-generator-DAG.json.gz`，109669 B，SHA256
`9cf17e78cd112ee527fb6b25890d390d8c59305b9854c89bbbbafbef94730352`。
原 FINAL 为322708 B，SHA256
`1e71a62ce53d64791ed672591d52d792307e3931dbe0eeea78bed42cee266692`；
完整 manifest 为9206 B、53项，SHA256
`8bef49bfa53a00f1bdce31c947e030d92ff5abbae15d0115587f9cf869486099`。
原 artifact14188093176，110888459 B，ZIP digest
`34f85e3c564929e04eceb0f326353a77acc7010ecaee1df315704a75e315f8c0`。
这些已完成来源在本篇只作消费，不重新求铅笔或1111子式。

## 3. 三个射影子式直接给加法的完整极理想

以下所有分式理想都作为函数域的子模保存；约定
$I_E=\mathcal O_Y(-E)$，主理想 $(q)$ 的局部阶是 $\operatorname{ord}q$。因此
$I_{E+\operatorname{div}q}=qI_E$，乘号方向固定。

设 $P,Q:X_L\to C$ 是非零的原 $\mu_3$ 等变映射，并且 $P+Q$ 不是零映射。记

$$
x_P,x_Q\in L(X),\qquad u=y_P,\quad v=y_Q\in L(Y),
\qquad E_P=(u)_\infty,\quad E_Q=(v)_\infty.
$$

定义 $X$ 上的三个有理函数

$$
f_1=x_P-x_Q,\qquad f_2=u+v,\qquad
f_3=x_Pv+x_Qu.
\tag{GP.6}
$$

### 定理 GP.1（全局三生成元公式）

每个 $f_i^3$ 都在 $L(Y)$，且在 $Y$ 的任意仿射图上有准确分式理想等式

$$
\boxed{
I_{E_{P+Q}}=I_{E_P}^{\,3}I_{E_Q}^{\,3}
\bigl(f_1^3,f_2^3,f_3^3\bigr).}
\tag{GP.7}
$$

右边事实上是整理想。它不要求三项各自非零；只要求 $P+Q$ 非零，使整个理想非零。它同时覆盖两点有限、恰一点为 $O$、两点都为 $O$、二挠点、$x=0$、以及 $\phi$ 的分歧点。

**证明。** 在 $X$ 上令 $J_P=\mathcal O_X(-P^*[O])$，同样定义 $J_Q,J_{P+Q}$。短 Weierstrass 平面嵌入由 $\mathcal O_C(3[O])$ 的三个截面 $(x,y,1)$ 给出，$O=[0:1:0]$。在一个 DVR 中，若 $j_P$ 生成 $J_P$，则

$$
(j_P^3x_P,j_P^3u,j_P^3)
\tag{GP.8}
$$

是 $P$ 的一组原始齐次坐标：在 $P=O$ 时，$y$ 的准确三阶极点使中间坐标为单位；在 $P$ 有限时第三坐标为单位。对 $-Q$ 使用 $(j_Q^3x_Q,-j_Q^3v,j_Q^3)$。

$\mathbf P^2\times\mathbf P^2$ 对角的理想由三个二阶射影子式生成。限制到 $C\times C$ 后是曲线对角的完整概形理想，因为这个平面嵌入是闭浸入。第二点先取负，所得反对角恰是加法映射的 $[O]$ 纤维。拉回 $X$ 得

$$
J_{P+Q}=J_P^3J_Q^3(f_1,f_2,f_3).
\tag{GP.9}
$$

这里第三个射影子式实际是 $-f_3$；其负号不改理想，本文仍把原具体函数定义固定为 (GP.6)，不拿“理想中为单位”作为以后删去主函数标量的许可。式 (GP.8) 在两点同时为 $O$ 时依然原始，故 (GP.9) 无须在这处另作未证明的仿射延拓。

在光滑曲线的每个 DVR，有限生成的非零分式理想是主理想。因此

$$
(f_1,f_2,f_3)^3=(f_1^3,f_2^3,f_3^3),
\tag{GP.10}
$$

因为两边的阶都等于 $3\min_i\operatorname{ord}(f_i)$，约定 $\operatorname{ord}(0)=+\infty$。这是曲线 DVR 上的等式，**不是一般多变量环中的理想恒等式**。

原 $x_P,x_Q$ 具有相同 deck 字符，$u,v$ 不变，故三个立方都下降到 $Y$。再用原已证恒等式

$$
\phi^*E_P=3P^*[O],\quad
\phi^*E_Q=3Q^*[O],\quad
\phi^*E_{P+Q}=3(P+Q)^*[O]
\tag{GP.11}
$$

将 (GP.9) 立方，恰得到 (GP.7) 拉回 $X$ 的等式。原 $\phi$ 在光滑曲线间有限、满射且平坦；在每个 DVR 也可直接以正分歧指数乘局部阶。因此拉回相等迫原分式理想相等。右边局部阶等于有效除子 $E_{P+Q}$ 的阶，故它确实是整理想。证毕。

定理不把某个分式表达式的分母零点当作极点，也不先假设闭点拆分。相对于 R804(804.16)，它把“有限图的支撑删除、无穷图的支撑补回”吸收到已知的完整 $I_{E_P},I_{E_Q}$ 中；所需新操作是分式理想的乘积与三主分式理想之和，而不是新的支持集饱和计算。

## 4. 五个原 g_j 的三个函数全部在原 Y 上

继续用 R791/R803 的同一个算子

$$
T^jf=D_{\rho_j^{-1}}\sigma^j(f),\qquad
\rho_j^6=\sigma^j(b)/b,
\qquad 1\le j\le5.
\tag{GP.12}
$$

它是 Galois 作用加原目标同构，不是 $Y$ 上的自同构。以下把底域 Galois 算子写成 $\sigma^j$；仿射图锚截面 $\sigma$ 仍沿原记号，两者不能混读。

令

$$
u=y_f,\quad S=u^2-b=x_f^3,\quad
v_j=\rho_j^{-3}\sigma^j(u),\quad
r_j^x=x_{T^jf}/x_f.
\tag{GP.13}
$$

原 $x_f$ 本身不在 $L(Y)$；这里只用它的立方和相同比值。直接消费 R803(803.19)、R804(804.6)：

$$
r_j^x=\frac{U_j}{U_0}
\frac{v_j^2-b}{u^2-b}\frac{du}{dv_j},
\qquad \frac{U_j}{U_0}=\frac{h_{T^jf}}{h_f}.
\tag{GP.14}
$$

这里的 $h_f,h_{T^jf}$ 是原完整全局 Hom 微分，来自 R759/R774/R803 的同一规范；不能换成 $c_1$ 的切向值。原 $U_j$ 在694维 $M_6$，不冒称属于普通690维 $V_3$。成功 R807/R809 已给同一个 $C_j=\theta U_j/\tau^4$ 的准确正规坐标，故实际使用 $U_j/U_0=C_j/C_0$；共同 $\theta$ 及原尺度同时消去，没有新取立方根。

于是定理 GP.1 对 $g_j=f+T^jf$ 变成

$$
\boxed{
J_j:=I_{E_{g_j}}
=I^3(\sigma^j I)^3
\left(
S(1-r_j^x)^3,\ (u+v_j)^3,\
S(v_j+r_j^xu)^3
\right).}
\tag{GP.15}
$$

原目标缩放 $D_{\rho_j^{-1}}$ 不改 $y$ 的极理想，所以 $I_{E_{T^jf}}=\sigma^j I$；但它对具体函数的 $\rho_j^{-3}$ 仍须按 (GP.13) 保留。所有函数叶只在同一个 $L(Y)$ 运算。

每个 $1+T^j$ 在原 $\mathbf Q[T]\simeq\mathbf Q(\zeta_{21})$ 中非零，故 $g_j\ne0$。这排除了三个生成元同时为零的唯一无效分支。无需凭某个点的坐标或某个单独生成元非零来判原 Hom。原 R843 点非挠结论可以服务点值消费者，但本定理不依赖它。

式 (GP.15) 直接构造五个准确极理想，不必先运行 R804 割线式以取得 $y_{g_j}$。后继需要原三同源比较函数时，才在同一 DAG 上附加 R803(803.22) 的既有群律节点。两个任务共享 $u,v_j,r_j^x$，不重新求五套高权关系。

## 5. 全局微分比也是一个有限原源表达式

式 (GP.14) 不能留一个只接受 CM 数值的 `derivative` 黑箱。本节只是把 R805 已证明的函数域微分接口接到现成来源，不声称已展开 R815 的 $\Gamma$。

### 5.1 原 A、B 到正规坐标用同一个单位解节点

原 $S_5$ 基矩阵记为 $S_5\in\operatorname{Mat}_{1380\times1234}(\mathbf Q)$，原五次基短矩阵记为 $F_5$。两者都是已经完成的69阶原数据，尺度同为 $82^{10}$。采用实际 R809 原行集 $I_5$，对 (GP.1) 的两个准确系数表达式定义

$$
q_A=(S_5)_{I_5}^{-1}(F_5\mathbf a)_{I_5},\qquad
q_B=(S_5)_{I_5}^{-1}(F_5\mathbf b)_{I_5}.
\tag{GP.16}
$$

这是一个来源明确的1234阶有理单位解表达式，不要求先展开28个有理右端。原 $A,B\in V_5$，$S_5$ 又是该空间的完整原基，故选行唯一解就是准确坐标；准确归属已有几何证明，不以一次模匹配猜测。

按原 row mapping 把 $q_A,q_B$ 合成为正规多项式向量 $v_A,v_B$，就得到 $A/\tau^5$、$B/\tau^5$。这里 $B_{\rm fld}=\lambda b$ 只在需要从原积分基转换到 R809 的 $b,s$ 基时施一次；不能给原 $A,B$ 重插一个共同清分母或 content。该新类型必须标为 `exact_unit_solve_expression`，不能伪装成旧接口的已展开坐标数组。

### 5.2 只保存实际需要的 primitive 右端和导数

成功 R806 已准确给原正规基上的 $W=M_w\in\operatorname{Mat}_{272}(\mathbf Q[z])$，$z=\sigma/\tau$、$w=e_2/\tau$，以及真正 cyclic 见证。置

$$
\mathcal K=[e_0,We_0,\ldots,W^{271}e_0],\qquad
\chi(z,T)=\det(TI-W(z)).
\tag{GP.17}
$$

原 $\det\mathcal K(0)=489861234\bmod1000000007$ 已证明 $\mathcal K$ 在 $L(z)$ 可逆；$\chi$ 是原272次可分最小多项式。只对需要的向量 $v$ 保存 `solve(K,v)`，其第 $i$ 个坐标是函数的 $w^i$ 系数；不生成一份没有消费者需求的完整 $\mathcal K^{-1}$，也不宣称幂环已经整闭。

在 $L(z)[T]/(\chi)$ 中准确定义

$$
\partial_z w=-\chi_z(z,w)/\chi_T(z,w),\qquad
\partial_z F(z,w)=F_z(z,w)-F_T(z,w)\chi_z(z,w)/\chi_T(z,w).
\tag{GP.18}
$$

$\chi_T(z,w)\ne0$ 来自特征零可分性。行列式、形式求导、原单位 solve 及域商都是有限准确运算节点，可以共享，不要求先把行列式或函数商展开成一个巨大多项式。它们的原始系数是已经准确返回的全局 $W$，不是 R827 的五个纤维矩阵。

取 $F=u$ 得到一个全局准确 $d=\partial_z u$；$u$ 非恒定，所以 $d\ne0$。由于 $z$ 在 $K$ 上定义，原 $\sigma^j\in\operatorname{Gal}(L/K)$ 与 $\partial_z$ 交换。因此

$$
\partial_zv_j=\rho_j^{-3}\sigma^j(d),\qquad
\frac{du}{dv_j}=\frac{d}{\rho_j^{-3}\sigma^j(d)}.
\tag{GP.19}
$$

五个比值共享一份 $d$，不再执行五次无关导数恢复。$\rho_j$ 是常数但不是1；把它从分母漏掉会改变原目标相位。

这里没有等待一般 $M_g,\Gamma$ 的全部有理重构，也没有把它们的模像认作准确算子。若后继已有通过 R813/R817 的准确算子，可等价消费并复用；否则 (GP.17)–(GP.19) 是完整的原函数域定义。其实际分子次数、整数高度和求值成本仍需运行才知道，本篇不宣称该表达式展开一定便宜。

## 6. 五个原 η 输入和三同源主函数的方向

沿 R791 的原方向，记

$$
\lambda_j=2+r_j=p_j/q_j,
\quad(p_j,q_j)=(165,67),(93,67),(100,67),(168,67),(371,134).
\tag{GP.20}
$$

这只是原次数比的既约分子分母；不把 $r_j$ 与 (GP.14) 的函数 $r_j^x$ 混用。定义真正的 Galois 理想范数，即在 $Y_K$ 上下降的共轭乘积

$$
\mathfrak N(J)=\prod_{k=0}^6\sigma^kJ,
\qquad
\mathfrak L_j=\mathfrak N(J_j)^{q_j}\,\mathfrak N(I)^{-p_j}.
\tag{GP.21}
$$

负次幂表示可逆分式理想的逆；也可写 $\mathfrak N(I)^{-1}=(\mathcal O:\mathfrak N(I))$。不要与要求结果仍在 $\mathcal O$ 内的截断整理想商混淆。由 (GP.15)，准确有

$$
\mathfrak L_j=\mathcal O(-Z_j),\qquad
Z_j=q_j\sum_k E_{\sigma^kg_j}-p_j\sum_k E_{\sigma^kf},\qquad
\eta_{h_j}=-[\mathfrak L_j]/q_j.
\tag{GP.22}
$$

原 $h_j=\kappa^{-1}e_R(T^j+T^{-j}-r_j)$、原 $\kappa$、目标极化及 R791 的有理下降论证全部保留。负号是因为这里记录 $\mathcal O(-Z_j)$，不是 $\mathcal O(Z_j)$。原所选五方向再按 R794 实际矩阵 $C$ 运输；没有更换五个 $h_j$。

对原 $\alpha_3=1-\zeta^2$，准确

$$
E_{\alpha_3g}=3E_g+\operatorname{div}(y_g^2-b),\qquad
I_{E_{\alpha_3g}}=(y_g^2-b)I_{E_g}^3.
\tag{GP.23}
$$

于是原比较函数与清分母理想满足

$$
\mathcal R_j=
\frac{N_{L/K}(y_{g_j}^2-b)^{q_j}}
{N_{L/K}(y_f^2-b)^{p_j}},\qquad
\mathfrak L_j^R=\mathcal R_j\,\mathfrak L_j^3.
\tag{GP.24}
$$

此处同样是**正乘**，不是 $\mathcal R_j^{-1}$。它在函数域中保存完整主除子嵌入，不只保存 Picard 类。

如果实现把真范数换写成同靶 $T^k$ 的乘积，必须保 R803(803.28) 的原常数

$$
\mathcal R_j=
\left(\frac{b^7}{N_{L/K}(b)}\right)^{p_j-q_j}
\widehat{\mathcal R}_j.
\tag{GP.25}
$$

主理想对非零域常数不敏感，原 Poincaré 对数和高度规范却敏感。因此理想图之外另保原 $3s$、$\rho_j$、真范数、主函数 $\mathcal R_j$ 与原 $c_0$ 比较数据；不能因 (GP.24) 的理想相等把这些常数设成1。既有 Picard 二挠/对称代表比较、原 splitting 和第二类周期也没有被此公式消去。

## 7. 最小可消费图及准确来源闭包

下面的节点构成一个无循环的有限图。它的叶是既有精确产物，不是本篇新造数值。

| 节点 | 准确输入 | 输出含义 |
|---|---|---|
| 原单位函数 | R787/R781 原全矩阵叶、$Z$、chart、原完整核维数证书 | (GP.1) 的 $A,B$ 及 $u=A/B$ |
| 原正规换基 | R809 的全 S5 短行、原 row mapping、真实选行子式 | (GP.16) 的两个单位解向量 |
| 原函数域微分 | R806 全局 $W$ 与真实 cyclic 来源 | 一份 $\partial_z u$ 的 (GP.17)–(GP.19) 表达式 |
| 原 Hodge 比 | R809 六个准确 $C_j$ 分组、分母、rational scale | 同一个 $C_j/C_0=U_j/U_0$ |
| 原 Galois/目标 | R791/R759 的原 $L/K,\sigma,\rho_j$ | 五份 $v_j,r_j^x$，含原相位 |
| 原基准极理想 | 本篇§2的实际1111证书和八生成元 | 两图原 $I=I_{E_f}$ |
| 五个加法极理想 | (GP.15) 的十五个具体函数与原理想因子 | 五份完整 $J_j=I_{E_{g_j}}$ |
| 原 η 与比较 | 原 $p_j,q_j,C,\alpha_3$、真范数与群律叶 | (GP.21)–(GP.25) 的类输入及主函数 |

必须区分以下来源：

1. 原八生成元消费者只带690个原 real 行；(GP.1) 的全部系数图需要完整1234行及原 R781/选行来源。不能把690行载体冒称完整全局单位函数来源。
2. 原五个 fiber $W(c)$ 足够1111秩证书，却不足以定义 (GP.18)。这里必须恢复已完成 R806 全局34组准确多项式列及其分母；不重新计算旧列。
3. S5 的行和 minor 并不自动包括六个 $C_j$ 的准确坐标组。后者应按成功 R809 的六个 normal index、十二组坐标及目标尺度逐 SHA 接入；不能从其模像重造准确值。
4. R840 四个响应与 R841/R844 的点 DAG 不能替代这些全局叶。反过来，已有原精确单位解身份也不因尚未展开而丢失。
5. 只需对按需右端保留 `matrix_solve` 和 `determinant` 节点；不得为此重新求已成模逆或把完整巨大有理逆作为前置条件。

一份可执行图可采用如下有明确定义的操作类型：原字段/多项式叶、有限加乘、`unit_matrix_solve`、`determinant`、`polynomial_derivative`、原可分域中的 `divide`、作用于整个图的 `Galois_conjugate`、`fractional_ideal_sum`、`fractional_ideal_product`、`invertible_fractional_ideal_inverse`。每个除法节点附原非零依据：原单位子式、$B\ne0$、$C_0\ne0$、$\chi_T\ne0$、或非恒定映射的导数非零。新图不得通过一个未认证数值零测试替换这些条件。

理想图可保持因子结构，不展开 (GP.15) 中全部生成元乘积。若以后需要272阶整格/HNF、标准 Jacobian 代表或局部展开，再针对所需输出求值；那些是后续真实算术，不与本篇的准确嵌入表达式混称。

## 8. 完成标志与后续真实任务

新的表达式消费者可以准确认证：原全局 $u$ 的单位解身份、五个同靶相对函数图、五个完整极理想图、原 $\eta_{h_j}$ 的 Picard 输入表达式，以及主函数运输的准确方向。它不要求另解五套 Laurent 系统，不要求重新取三次根，也不要求先做 R804 的支持集饱和。

这些标志与以下字段应分开：

- `global_y_exact_unit_expression_defined`；
- `five_original_addition_pole_ideals_as_fractional_DAGs_certified`；
- `original_eta_Picard_input_DAGs_defined`；
- `expanded_global_function_coordinates_computed`；
- `normal_polynomial_ideal_lattices_materialized`；
- `Jacobian_standard_representatives_computed`；
- `original_rigidification_and_height_computed`。

本文只证明前三项的原源构造及其有限执行契约；没有新运行可供填写实际机器完成字段。最后四项不能从前三项自动填真。尤其一个有完整生成元的度零分式理想，不等于已经证明其 Picard 类为零；已有 $c_1$ 非挠与原点值也不替代指定高度的非零结论。

## 来源定位

- [原单位 chart 的 U1–U10](R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)：全局原关系、完整核维数与准确 solve 表达式，既有结论。
- [R840](../results/R840-certified-original-implicit-CM-value-and-first-jet.md)：该全局表达式的原 CM 四响应和518位实际计算。
- [R803 原函数复用](../results/R803-original-single-map-reuse-and-mixed-Hodge-ratios.md)，(803.18)–(803.29)：全局相对 $x$、Galois/目标尺度、五原方向及主函数常数。
- [R804](../results/R804-original-selected-map-reuse-in-integral-cyclic-module.md)，§§3–7：原相对群律与两反对角图；本文 (GP.7) 是它在已知两端完整极理想后的全局三生成元替代。
- [R805](../results/R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)，(805.12)–(805.20)：原 primitive/微分与正规两图、分式理想运算。
- [R806 真乘法](../results/R806-certified-original-primitive-multiplication.md)、[R809 真六向量](../results/R809-certified-original-six-Hodge-normal-vectors.md)：准确全局矩阵与六个已成原 Hodge 比来源。
- [R791](../results/R791-certified-original-Hom-descent-and-eta-inputs.md)，(791R.10)–(791R.13d)：原 $\eta$、三同源次数、范数和全部未删的比较函数。

本文新内容只在 (GP.7)/(GP.15) 的全局射影子式理想等式及它与这些真实输入的组合；没有重新登记上述已成全局单位解、群律或点非挠结论。
