# R899 原七极 trace 的 K 固定完整 RR 基：由实际坐标归一化直接下降

日期：2026-11-16。状态：**本文证明的是准确构造及其充分证书；新的评价矩阵、418 子式及变基尚须公开 Actions 实算。** 不预填 R894 新十六步或本消费者的成功数值。

来源：

- [R894 原七常数域极除子 trace 与有界下降](R894-original-seven-conjugate-pole-trace-and-bounded-descent.md)；
- [R880 六个原共轭 D* 完整空间](R880-certified-original-six-conjugate-Dstar-RR-inputs.md)；
- [R890 原 Ef 有界代表及固定首项](R890-certified-original-Ef-bounded-representative-and-marked-frame.md)；
- [R872 点 jets 与固定 Picard 空间](R872-certified-original-P0-jets-and-fixed-Picard-spaces.md)及其[来源证明](../notes/R872-original-point-jets-and-bounded-two-weight-RR-kernels.md)；
- 已成 R827 原正规基、七个完整 Krylov 纤维；已成 R885 原完整纤维特征关系，保全部 Artin 代数而不分拆几何点。

本篇只处理 $\operatorname{Gal}(L/K)$，其中 $K=\mathbb Q(\zeta_3)$、$L=K(b)$，阶为7。它不把 K 固定当成 $\mathbb Q$ 固定，也不替换原 Y 的 $c_Y$、原局部参数或 Picard 类。

## 1. 本次准确输入与目标

原 $Y/K$ 的亏格为127；原 $H$ 次数272。记 R894 的度零原除子为
$$
T^0=\sum_{j=0}^{6}E_{\gamma^j f}-8442P_0.
\tag{899.1}
$$
这里每个原极除子 $E_{\gamma^jf}$ 次数1206，并且在 $P_0$ 的系数都是1。所以
$$
\deg T^0=0,\qquad \operatorname{ord}_{P_0}(T^0)=-8435.
\tag{899.2}
$$
七项均是原常数域共轭，故 $T^0$ 在 K 上定义；不是 Hecke 对应范数。

R894 若实际完成，其输出为一个有效次数272、避开原 $P_0$ 的 $D_N/L$，完整原空间
$$
W_N=H^0(Y_L,\mathcal O(3H-D_N)),\qquad \dim_L W_N=418,
$$
以及保持原全部标量的准确函数 $Q_N$，满足
$$
T^0=(D_N-H)+\operatorname{div}Q_N,\qquad
Q_N=Q_{\rm orb}F_N,\qquad
Q_{\rm orb}=\prod_{j=0}^{6}\widetilde Q_j .
\tag{899.3}
$$
本篇不重新选择 $D_N$，也不重做其16步。

令
$$
V_K=H^0(Y,\mathcal O(2H-T^0)),\qquad V_L=V_K\otimes_K L.
$$
因为 $\deg(2H-T^0)=544>252=2g-2$，Riemann–Roch 给
$$
\dim_K V_K=544+1-127=418.
\tag{899.4}
$$
由(899.3)，正乘 $Q_N$ 给准确同构
$$
W_N\xrightarrow{\ \cdot Q_N\ }V_L.
\tag{899.5}
$$
选 R894 已成的原正常基为行向量
$\mathbf w=(w_1,\ldots,w_{418})$。本次目标是实际给出 $V_K$ 的418个固定函数，而不是仅重复(899.5)的存在性。

## 2. K 定义的评价泛函与实际子式

在原 $\tau$ 图中
$$
R_\tau=\bigoplus_{i=0}^{271}K[z]\beta_i,\qquad
z=\sigma/\tau,\quad \beta_0=1,\quad \beta_1=w.
\tag{899.6}
$$
这是原正规环的完整自由基；$\gamma\in\operatorname{Gal}(L/K)$ 固定 $z,\beta_i$。不能把这条常数域作用与 $c_Y(z)=z-2\beta_{72}$ 混淆。

对 $a\in K$，原完整纤维
$$
A_a=R_\tau/(z-a)
$$
是272维 K 代数，$\bar\beta_0,\ldots,\bar\beta_{271}$ 为其原 K 基。允许非约化和非域纤维。每个坐标泛函
$$
\lambda_{a,i}:A_a\longrightarrow K
\tag{899.7}
$$
都是 K 线性的，不选某个几何点、不删除 nilpotent。

选择若干原 K 定义的纤维；它们必须避开原 $P_0$，并处于原 $\tau$ 图。于是 $V_K$ 的函数在这些纤维上无极：允许的有限极只来自(899.2)的 $P_0$。原 $T^0$ 正支撑上的零不造成函数极。

对已成的 $\mathbf w$ 构造完整评价矩阵
$$
\mathcal H_{(a,i),j}=\lambda_{a,i}(Q_Nw_j)\in L.
\tag{899.8}
$$
每个行标签都是准确的二元组 $(a,i)$，按选定整数节点和原正常基顺序保留。

**本篇不声称三纤维自动给单射。** 直接把有零条件的线丛嵌入函数环评价时，纤维可能与 $T^0$、$D_N$ 共同支撑相交；仅以 $3\cdot272>544$ 不能忽略这件事。$Q_N$ 的分母是单位，甚至 $Q_N$ 本身在纤维上为单位，都不能单独排除那种共同支撑。

所用出口严格更直接：在全部实际行中找到418行 $J$，并认证
$$
A=\mathcal H_J\in\operatorname{Mat}_{418}(L),\qquad \det A\ne0.
\tag{899.9}
$$
原辅助素点的一次真实单位子式足以认证(899.9)，前提是每个输入都是同一个准确对象的合法约化。这里没有预设某个三节点组合达到418秩。

由(899.4)，这些418个 K 泛函在 $V_K$ 上构成同构
$$
\Lambda_J:V_K\xrightarrow{\sim}K^{418}.
\tag{899.10}
$$
证明：标量扩张后的矩阵就是(899.9)，故其秩418；核和余核经忠实域扩张后为零，原映射也是同构。

## 3. 归一化基自动 K 固定

在同一个准确字段中定义
$$
P=A^{-1},\qquad
\mathbf s=Q_N\,\mathbf w\,P.
\tag{899.11}
$$
所有原选行和列顺序固定，故(899.11)给明确的418个函数，每个函数可用该矩阵的一列准确 unit-solve 表达。

它们满足
$$
\Lambda_J(s_j)=e_j .
\tag{899.12}
$$
对任意 $\gamma\in\operatorname{Gal}(L/K)$，空间 $V_L$ 和全部 $\lambda_{a,i}$ 都来自 K。因此
$$
\Lambda_J(\gamma s_j)=\gamma\Lambda_J(s_j)=e_j.
$$
由(899.10)的唯一性，
$$
\gamma s_j=s_j\quad(1\le j\le418).
\tag{899.13}
$$
所以 $\mathbf s$ 是 $V_K$ 的完整 K 基。

这条证明不要求数值求出另外六个 $\gamma(A)$，也不要求那些共轭子式在同一个辅助 residue embedding 中都是单位。一个真实约化下的单位认证足以使准确 $A$ 可逆；(899.13)在特征零内成立。原16步中的选行、自由坐标或第二锚参数不需要另行搜索或重放。

“明确 K 基”在此指(899.11)的全部 source-bound 函数表达式、完整418个准确列以及其实际约化。它不声称已展开每个 K 有理系数。后续若只需函数运算或同点评价，可直接消费这些准确 unit-solve 叶。

## 4. 两种基中的下降矩阵和七重 cocycle

R894 在 $\mathbf w$ 上的原作用是
$$
\alpha_\gamma(\mathbf w)
 =\frac{\gamma Q_N}{Q_N}\gamma(\mathbf w)
 =\mathbf w C_\gamma .
$$
对(899.8)取 $\gamma$，得
$$
\gamma A=A C_\gamma,\qquad
C_\gamma=A^{-1}\gamma A
        =P\,\gamma(P)^{-1}.
\tag{899.14}
$$
这是旧基中的明确准确矩阵 DAG；若没有求值 $\gamma A$，不把它称为已计算的模数组。

另一方面，(899.11)给
$$
C_\gamma\gamma(P)=P.
\tag{899.15}
$$
因此在新的扭下降基 $\mathbf wP$ 中，作用矩阵准确为
$$
I_{418}.
\tag{899.16}
$$
等价地，实际函数基 $Q_N\mathbf wP$ 被普通常数域作用逐列固定。新矩阵(899.16)由唯一性证明，不需要另外一轮数值相乘来“猜”它。

旧基七重 cocycle 按顺序望远镜：
$$
C_\gamma\,\gamma(C_\gamma)\cdots\gamma^6(C_\gamma)
=A^{-1}\gamma^7(A)=I_{418}.
\tag{899.17}
$$
它保原乘子 $\gamma Q_N/Q_N$ 的方向，不换其逆，不动第一 Picard 槽。

本篇没有声称 $D_N$ 自身在 K 上定义。新的 K 函数基与一个 K 定义的次数272代表是不同出口；后者需要后续真实有界 flip，不能仅从(899.13)改标原 $D_N$。

## 5. 原完整 Artin 环上的可执行评价

在辅助素点 $\ell=1000000753$、原 $\zeta$ 与 $s$ embedding 中，直接复用 R827 的旧 $W(a)$、$K_a=[e_0,W(a)e_0,\ldots,W(a)^{271}e_0]$ 及其已成逆。复用 R890 的
$$
E_{3,a}=(a^k e_i)_{(i,k)\in V_3}
$$
及 $K_a^{-1}E_{3,a}$，不重求原正常 V3 评价。

R885 已在 $a=0,\ldots,7$ 给原完整关系
$$
\chi_a(T)=T^{272}+\sum_{i=0}^{271}c_{a,i}T^i.
$$
其原节点字段是 characteristic_coefficients_ascending_T，共273项。只消费实际所用的旧节点；不再求特征多项式。
于是全部算术在
$$
\mathscr A_a=\mathbb F_\ell[T]/(\bar\chi_a)
\tag{899.18}
$$
内执行，保全部272坐标和 nilpotent。

一个原正常向量 $v$ 的循环坐标是 $K_a^{-1}v$；乘后用 $K_a$ 送回原 $\bar\beta_i$ 坐标。整环评价的单位判断必须是
$$
\gcd(d(T),\bar\chi_a(T))=1,
\qquad d(T)d^{-1}(T)\equiv1\pmod{\bar\chi_a(T)},
\tag{899.19}
$$
而不是某一个根上的非零。也可按相同旧 W/K 构造乘法矩阵，单 RHS 求 $d\,x=1$ 并全272乘回；本篇优先消费已有 $\chi_a$，不要求建立完整272立方乘法表。

所有实际出现的除法都先认证(899.19)。若原表达式在某纤维有不可直接除的分母，即使数学上可能约去，也只能报告该节点不适用于本直接 DAG 评价。不得用一个任意逆、伪约分或降到某个剩余域替代。

## 6. Q_N 的最小准确叶

七个原函数的定义保持
$$
\widetilde Q_j
 =\left(\frac{a_j}{v_j}\right)^3
   \frac{q_C}{q_\chi^4},\qquad
q_C=u_C/\tau^2,\quad q_\chi=u_\chi/\tau^2.
\tag{899.20}
$$
$a_j,v_j$ 都按原 V3 帧解释，同权之比不再插入 $\tau$、82 或 $\theta$。共同 $q_C,q_\chi$ 只评价一次。六个非零 $\sigma$ 方向的 a/v 小阶段已经来自真实六 D*。第0方向的原 R880 选择阶段只保存原 a 的角色与点值，不虚构尚未保存的正常坐标数组：在旧节点0至4直接消费 R845 的 `section_evaluation_mod_prime`，并沿原选择/来源绑定同一 a；v 直接消费已成正常坐标叶。只有确需节点5或6时，才按原 V3 权界由旧节点0至3唯一插值各正常系数（次数至多 $3-\epsilon_i$），以旧第4点全272坐标乘回，再评价新需节点。这是必要的新小插值叶，不重做原完整正常转换、旧 a 纤维乘法或旧 Krylov 逆。

$F_N$ 沿 R894 真实保存的主函数树求值：
$$
F_{\rm new}=(q\,F_{\rm left}F_{\rm right})^{-1},
\qquad q=u/\tau^3.
\tag{899.21}
$$
读取16个新节点及2个已成 R890 节点的原未缩放 u；同一父项出现两次时仍保两次。所有 q 叶和相同源的 Artin 值按实际 file/bytes/SHA 和节点缓存，避免重算共享子树。不能用 P0 的单位常数冒充 q 的全纤维值。

然后
$$
Q_N(a)=
 \left(\prod_{j=0}^{6}\widetilde Q_j(a)\right)F_N(a)
\tag{899.22}
$$
作用于完整正常 $W_N$ 的418列，得到(899.8)。这是真正新增的函数乘法；原16flip、Krylov、正常基转换、点 jets 和 t 常数全部直接复用。

首 scope 按原整数顺序尝试旧节点0至6，先形成三个可用整纤维；实际秩不足时可加入其余已成节点。每个拒绝、可用节点、矩阵块、选行和逆都原子保存。达到418单位子式及全部已取行乘回后才完成。旧七节点仍不足时只保诚实未完成状态；不能将其解释为无 K 基，也不能不经来源新增节点或重建旧逆。

## 7. 完整 418 的有限输出

设原 R894 正常坐标矩阵为
$$
B_N\in\operatorname{Mat}_{690\times418}(L).
$$
消费者应保：

1. 所选完整纤维、原 K 基行号和全部准确 source specs；
2. 每个实际分母的完整 Artin 单位证书与逆乘回；
3. 完整 $\overline{\mathcal H}$、选定418原行 $J$、完整 $\bar A^{-1}$；
4. 两边逆乘回及完整已取行 $\overline{\mathcal H}\bar P$；
5. $\bar B_N\bar P$ 的全部690×418正常坐标，以及(899.11)的准确 unit-solve 定义；
6. 新固定基的准确 $I_{418}$ 下降矩阵与(899.14)的旧基矩阵 DAG；
7. 来源和界限标志：K 固定已由唯一性认证，$\mathbb Q$ 固定/原 K 有理系数展开/连接与高度没有据此完成。

实际模矩阵不能被改标签成特征零数组。准确对象由原源、所选原行、完整方程和 unit-solve 一起定义，(899.13)再严格证明它位于原 K 空间。

## 8. 同时保原 P0 与 t 首项

R894 已保
$$
Q_N=\lambda_\rho\rho^{-8435}+\cdots
   =\lambda_t t^{-8435}+\cdots,\qquad
\lambda_t=\lambda_\rho c^{8435},
\tag{899.23}
$$
其中 $c=(t/\rho)(P_0)$ 是原 R883 已成值；标量没有缩放成1。

原 R890 的 P0 正常 V3 泛函记为 $\epsilon_0$。对新基，各系数准确为
$$
[\rho^{-8435}]\mathbf s
 =\lambda_\rho\,\epsilon_0 B_N P,\qquad
[t^{-8435}]\mathbf s
 =\lambda_t\,\epsilon_0 B_N P.
\tag{899.24}
$$
这只需原点泛函与新变基，不需要新的 jets。

因为 $D_N$ 避 P0，原完整 $W_N$ 在 P0 无基点，所以(899.24)的准确行并非全零。消费者仍须记录全部418个实际约化系数，只有其中真正为单位的第一列才登记为后续原标记截面 $s_0$；不从特征零非零直接预填模单位。若本处未检到单位，只保已成 K 基及真实待精化的点值状态。选定的原函数不重新缩放；经实际单位认证的 $s_0$ 在 P0 的准确极阶为8435，而不是8442。

这一标记可以交给后继 K 定义有效代表/有界群运算；本篇只完成 K 固定完整空间、真实标记与准确下降矩阵，不替代那个后继计算。

## 9. 新范围与尚未发生的数值

旧 R894 已证明抽象半线性 datum，旧 R866 处理原全纯微分的 $\mathbb Q$ 结构；本篇的新增是原七极 trace 的实际418维 K 固定函数基及其低成本来源算法。它不重复旧抽象下降结论，也不把 rational-looking 模系数当 K 结构。

该构造只需一个新418单位归一化，不需要六次原16flip回放。准确旧基矩阵仅给(899.14)的 DAG；新的 K 基矩阵由(899.13)严格确定为单位矩阵。所有新 Artin 乘法、逆、秩和变基仅在公开 Actions 执行。写稿时没有 R899 新数值，R894 来源必须实际完整后才可绑定。

原五 $L_j$、YP/FM 的128/144/634空间、原 Hecke 支持、non-p、Poincaré/指定 splitting 与高度仍沿原定义消费；不能由本条 K 固定基跳过这些对象。

