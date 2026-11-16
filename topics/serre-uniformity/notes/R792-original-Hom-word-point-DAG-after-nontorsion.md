# 原非挠证书之后的 Hom 字点值 DAG：五个原 η 加法输入

日期：2026-11-16。状态：本篇给出一个有明确前提的准确点值消费接口。它复用 R791、R804、R841 已证公式，不把这些公式重命名为新结果。只有同一个原点的非挠消费者实际成功后，下面以 Hom 字决定点值分支的规则才可启用。本文没有预填该成功，也没有接受旧标量 RR 候选。

## 1. 同一个原点、同一个整数 Hom 格

保持原 $p=41$、$K=\mathbf Q(\zeta)$、$L=K(b)$、
$C_b:y^2=x^3+b$，以及
$$
P=f(c_1),\qquad f=f_4,\qquad f(c_0)=O.
\tag{H1}
$$
R841 的已成功准确 DAG 给 $P$ 和 $[1-\zeta^2]P$ 的准确表达式。
它的四个线性响应叶仍由原 free-column1186 的单位图定义；没有把模
$\ell^{518}$ 响应或其十四个有理重构建议改成准确展开坐标。

记 $\Lambda$ 为 R791 的原十二维整数 Hom 格，列基仍是
$f_0,\ldots,f_{11}$。每个字保存其原十二整数坐标；需要用有理 Hom
时，另保共同正分母，不能取整后丢掉同源核。本文首 scope 只用
$\mathbf Z[T,\zeta]f\subset\Lambda$，故没有同态除法。
所有曲线映射都以原 $c_0$ 的零值规范化。

原 R791 已准确给
$$
T(u)=D_{\rho^{-1}}\sigma(u),\qquad
D_a(x,y)=(a^2x,a^3y),\qquad T^7=[\zeta^2],\quad T^{21}=1.
\tag{H2}
$$
微分列上的 $\rho\sigma$ 与点坐标上的 $D_{\rho^{-1}}\sigma$ 不得互换。
完整原 $\sigma,b,\rho,\rho_j=\prod_{i=0}^{j-1}\sigma^i(\rho)$，以及
$T,J,R$ 三个实际矩阵，均从 R791 已成来源直接读取。

## 2. 非挠成功后，哪些点值零判变成 Hom 字判定

唯一新增的先决证书是[原分裂处非挠方法](R792-original-padic-CM-point-nontorsion-method.md)
实际给出
$$
P=f_4(c_1)\text{ 非挠}.
\tag{H3}
$$
该方法的命题 N.2 使用同一个 R616 原有理点差和 R728 原
$\mathbf Q$-简单因子，推出每个非零原 primitive Hom 在这个点差的像都非挠。
这里不把 R726 的“充分大 $p$”直接用于 $p=41$，也不以非零切向代替(H3)。

因此，对 $u,v\in\Lambda$ 的实际点 $P_u=u(c_1)$，有
$$
P_u=O\iff u=0,\qquad
P_u=P_v\iff u=v,\qquad
P_u=-P_v\iff u=-v.
\tag{H4}
$$
理由是相应差或和仍是同一个原 primitive Hom；若字非零，其值不能为挠。
若字在有理 Hom 中为零，原实际整数同态也为零，因为 Hom 群无挠；
原 $c_0$ 规范排除了未知常数平移。

更具体地，每个非零字的值是有限点，且
$$
y_u\ne0,\qquad x_u\ne0,\qquad y_u^2-b\ne0.
\tag{H5}
$$
$y_u=0$ 给二挠点；$x_u=0$ 给 $[1-\zeta]$ 的有限核中的点，因而也是挠点。
最后一式由原曲线方程等于 $x_u^3$。若 $u\ne\pm v$，则
$x_u-x_v\ne0$：相同横坐标在原短 Weierstrass 模型上只能给相等或相反两点。

这些是带明确来源的有限分支规则，不是对任意 $L$ 表达式的零判算法。
例如一个无已识别 Hom 意义的 Poincaré 局部截面之和、原高度或
Jacobian 类仍不能由(H4)判零。

## 3. 点加法沿已有公式生成准确表达式

给定两点节点，先按原字处理 $u=0$、$v=0$、$u=-v$。
若 $u=v\ne0$，使用原椭圆倍点式
$$
m=\frac{3x_u^2}{2y_u},\qquad
x_{2u}=m^2-2x_u,\qquad y_{2u}=m(x_u-x_{2u})-y_u.
\tag{H6}
$$
分母 $2y_u$ 的非零证书是(H3)--(H5)及该实际非零 Hom 字。
若 $u\ne\pm v$，使用
$$
m=\frac{y_v-y_u}{x_v-x_u},\qquad
x_{u+v}=m^2-x_u-x_v,\qquad
y_{u+v}=m(x_u-x_{u+v})-y_u.
\tag{H7}
$$
分母由(H4)准确证明非零。分子可以为零，不需要先判。
取负和 CM 单位是 $-(x,y)=(x,-y)$、$[\zeta](x,y)=(\zeta x,y)$。

每个输出节点同时保存原十二维 Hom 字、坐标表达式根、实际分支类型，
以及每个 inverse 节点的非零证书引用。若整数 Hom 字为零，直接输出
$O$ 状态，不编码为 $(0,0)$。在(H3)已实际成立的首 scope 中，所有
非零字的点都有限；因此不需要为它们试探一个射影图或重复模零筛选。

上述群律与 R804 一致。本接口增加的是把其全局函数上的字判定，
通过同一个实际点的非挠证书合法用于 $c_1$ 点值，而不是重新证明群律。

## 4. 完整 Galois 运输是准确 DAG 操作

令 $\mathcal A_j$ 表示原 $\sigma^j$ 对整个准确 $L$ 表达式的作用。
对任意节点
$$
T^jP_u=\bigl(\rho_j^{-2}\mathcal A_j(x_u),
                  \rho_j^{-3}\mathcal A_j(y_u)\bigr).
\tag{H8}
$$
原 $c_1\in X(\mathbf Q)$，所以这里确是同一个原映射 $T^ju$ 在
同一点的值。$\mathcal A_j$ 必须作用于全部 $L$ 常数和全部单位图叶。
特别是一个 `unit_chart_solve` 叶的矩阵、右端和响应泛函一并共轭；
它不是只给现有模数组换标签，也不是只共轭外层 $b$ 系数。

实施上允许增加一个类型明确的 `original_L_automorphism` 节点，
其输入为旧准确子 DAG 的根，来源为 R791 的原 $\sigma(b)$、$\sigma(\zeta)=\zeta$
和原 Galois 作用。该节点的语义就是 $L$ 的这个已给自同构。
它可保留为精确运算节点，不要求立刻把2420个关系系数展开。
自同构把非零元素送到非零元素，故旧 inverse 的非零证明也随节点运输。

使用 $T^7=[\zeta^2]$ 缩短字时，横坐标乘 $\zeta^2$、纵坐标不变；
不能把它错写为七阶恒等。R791 的21阶作用、实际 $\rho_j$ 与原七个
Weil 分量均保留，不重算原 Hom 或 Galois 矩阵。

## 5. 首 scope 正是 R791 的五个原 η 加法点

R791(791R.13b)所需的小映射在指定分量为
$$
g_j=(1+T^j)f,\qquad j=1,\ldots,5.
\tag{H9}
$$
这五个映射不同于 R794/R804 已选择的五个较低次数映射；本接口不混换两份基。
从原 $P$ 和(H8)构造 $P_j=P+T^jP$，只需五个新的加法节点。
在 $K[T]$ 的原六次不可约模型中，$1\pm T^j$（$1\le j\le5$）
均非零，故这五次加法使用(H7)，且结果也非零。

原 R791 已成次数和比例保持如下：

| $j$ | $\deg g_j$ | $\deg[1-\zeta^2]g_j$ | 原 $r_j$ |
|---:|---:|---:|---|
| 1 | 2970 | 8910 | $31/67$ |
| 2 | 1674 | 5022 | $-41/67$ |
| 3 | 1800 | 5400 | $-34/67$ |
| 4 | 3024 | 9072 | $34/67$ |
| 5 | 3339 | 10017 | $103/134$ |

每个 $P_j$ 的七个同靶运输 $T^kP_j$ 可直接对该完整表达式应用(H8)，
再乘 $D_{\rho_k}$ 即得到位于 $C_{\sigma^k b}$ 的实际 Weil 分量
$\sigma^kP_j$。不必新增35次椭圆加法。

原实下降点也直接复用 R791(791R.6)：对任何这里的非零 Hom 点 $Q=(x,y)$，
$$
[1-\zeta^2]Q=
\left(-\frac{\zeta x(y^2+3b)}{3(y^2-b)},
      \frac{y(y^2-9b)}{3(1+2\zeta)(y^2-b)}\right).
\tag{H10}
$$
分母在(H3)下由(H5)非零；$3(1+2\zeta)$ 是原常数，不能省略。
因 $T$ 与 $[1-\zeta^2]$ 交换，结果确是原实映射
$(1+T^j)f_R$ 在 $c_1$ 的值。

如果以后需要 R794 的五个已选低次数点，可把同一个分支执行器用于
R804 §5 的既有八节点链；不得再次计算其整数循环表示或替换原五方向。
本首 scope 不把该可复用扩展列作已经完成的点值。

## 6. 原主函数的点值可以保留，η 与高度仍另有全局输入

写 $r_j=a_j/b_j$ 为上述原既约比例，$b_j>0$。
R791(791R.13d)的实际主函数在 $c_1$ 的值是
$$
\mathcal R_j(c_1)=
\frac{N_{L/K}(y_{P_j}^2-b)^{b_j}}
     {N_{L/K}(y_P^2-b)^{2b_j+a_j}}.
\tag{H11}
$$
分子分母每个因子均由(H5)非零。因此这也是一个可直接构造的准确 DAG 根。
`Norm` 可定义为七个明确原 $\sigma^k$ 节点的乘积，不需要新的数值选根。

如果以同靶 $T^k$ 点值乘积实现，必须使用
$$
N_{L/K}(y_Q^2-b)
=\frac{N_{L/K}(b)}{b^7}
 \prod_{k=0}^6\bigl(y_{T^kQ}^2-b\bigr).
\tag{H12}
$$
因为 $\sigma^k b=\rho_k^6b$，且
$\sigma^k(y_Q^2-b)=\rho_k^6(y_{T^kQ}^2-b)$。
故(H11)中该公共常数的总幂是 $-b_j-a_j$，不能因两边极除子相同而删除。
这里仅复用已有的原 Norm 恒等式；原 Norm 常数若已成则读其准确来源，
未展开时可保准确七因子表达式，不伪填一个有理数。

原
$$
e=\kappa v^\dagger v,
\qquad h_j=\kappa^{-1}e(s_j-r_j)
\tag{H13}
$$
完全不变。点值(H9)--(H11)没有给出全局极除子 $P_{g_j}$ 的闭点或
Jacobian 类，也没有给原 $c_0$ 处截面首项和刚性化常数。
若高度使用刚性化后的函数，须继续乘其真实 $c_0$ 比较常数；
本 DAG 的(H11)仅是 R791 写下的原有理函数本身在 $c_1$ 的值。
因此不把这些点或主函数值声明为已经计算了 $\eta_{h_j}$、
抽象 $A$ 的同源核原像或原高度。

## 7. 最小消费来源、准确 flag 与续接

首请求至少包含以下不可变身份：

1. R841 成功证书、原50节点程序、全部准确叶及其一日载体；
2. 同一 $P$ 的实际非挠成功证书、原分支/形式参数非零见证，以及它对同一
   R841/CM/R791 身份的绑定；非挠未成功时请求保持 pending，不推测；
3. 已成 R791 的原整数 $T,J,R$、$\sigma(b),\rho_j$、实下降/五比例及
   $\kappa v^\dagger v$ 来源。它们本已在 R841 载体中，不重算。

新 stage 分别保存来源核验、准确 Hom 字分支、五个点 DAG、七分量运输、
原实下降点与五个(H11)主函数根。每个完成阶段原子写入，可按同 tag 续接。
新算术仅在本公开仓库 Actions；复制旧 DAG/矩阵不标成新数学成果。

准确成功字段应逐项区别：

- `actual_nontorsion_source_verified=true`；
- `five_original_R791_addition_points_as_exact_DAG=true`；
- `all_addition_denominators_certified_by_original_Hom_words=true`；
- `original_Galois_transport_and_T7_phase_preserved=true`；
- `original_R791_comparison_function_values_as_exact_DAG=true`；
- `expanded_coordinates_exactly_certified=false`；
- `original_abstract_A_coordinate_preimage_recovered=false`；
- `actual_eta_or_height_computed=false`。

任一字段只有对应阶段实际完成后才置真。这个接口不再要求对(H6)--(H10)
中的分母作独立零试探，也不让一个尚未接受的 RR 点进入准确点程序。

## 原来源

- [R791](../results/R791-certified-original-Hom-descent-and-eta-inputs.md)，特别是(791R.1)--(791R.13d)。
- [R804](../results/R804-original-selected-map-reuse-in-integral-cyclic-module.md)，原点/函数群律、八节点链与完整目标运输。
- [R841 消费方法](R792-original-source-bound-CM-DAG-beta-interface.md)，原准确 $P$ 与实下降点表达式。
- [同一点的非挠方法](R792-original-padic-CM-point-nontorsion-method.md)，其命题 N.2 是本接口(H4)的必要实际前提。

源码、参数、纸面证明及简明 run/SHA 登记可入 Git；机器回执、DAG、矩阵与点值运算数组只在一日 active artifact/carrier 续传。
