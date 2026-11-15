# R177 若通过完整原函数核：真实字符的延拓与几何排除范围

日期：2026-11-15。**条件性解释准备；不预设新的共同 word 实际通过。** 本稿只连接已发表定义与证明，不运行新的编译、LP、profile 查询或几何计算，也不占用新的结果编号。

依据 [R105](../results/R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](../results/R109-local-density-of-the-complete-fourth-quotient.md)、[R130](../results/R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R163](../results/R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md)、[R164](../results/R164-covariant-eight-matrix-multiplier-for-positive-affine-characters.md)、[R177](../results/R177-explicit-all-layer-positive-point-after-nine-original-relations.md) 及 [R179](../results/R179-universal-independence-of-fixed-color-remainder-words.md)。

## 1. 尚须满足的唯一新原函数条件

采用真实函数空间

$$
U=\mathcal U_4,\qquad R=\mathcal R_8.
\tag{1}
$$

R105 的 $U$ 是同一 canonical 目标规则、同一右锚、零传入 second/third scalar 历史下，实际同 scalar germ、frame $I\to I$、$M=T=0$ 有限路径之完整第四成本的实线性 span。成本是整个 $\xi$ 函数和完整相位对象，不是一个采样值。

R105(7) 同时证明：以同端口、frame 恒等的实际 $M=0$ 路径成本生成，允许其 $T$ 非零，得到同一个 $U$。这是 span 结论；没有给实际路径任意取负。

当前已发完整头部包括权 $-2$ 的全部十四族系数、真正的 $R_{-2}$ 比较基和全部平移分母呈示。R177 给其中全部 107 个 normal 值以及响应基上的零赋值，记作 $\ell_*$。旧线性表、R168、R174 和指定点实际已经支付它对**已发关系与头部约束**的一致性。

尚须新增的假设是：

> **条件 K。** 77 个保留字面基的完整共同规范表已完成，所有原列来源、同右锚转换和 R179 余 letter 语法正确；$\ell_*$ 消灭该共同表的全部核。

R179 证明这里的共同表核就是完整普适函数核。因此条件 K 恰使 $\ell_*$ 降到真正的 $U_{-2}$；它不是“没有再找到一条关系”或“暂未被某个部分表切除”。

矩阵系数为有理数时，完整有理核基也覆盖实线性核：有限有理矩阵的实核是其有理核的实张成。因此这里并未遗漏实数或无理数系数的真实关系。反过来，一条核关系被 $\ell_*$ 赋成非零，就排除 R177 指定点；其标量平方分解不会挽救这个原函数定义冲突。

以下各节均明确假设条件 K 成立。

## 2. 从单权赋值延拓到整个真实 U

R105 的有限 Laurent 仿射表示给真实整权直和

$$
U=\bigoplus_j U_j,\qquad R=\bigoplus_j R_j,
\qquad \mathsf N U_{j+1}\subset U_j.
\tag{2}
$$

R163 的完整单权生成定理为

$$
U_{-2}=R_{-2}+T_{-2},\qquad
R_{-2}+\mathsf N U_{-1}=R_{-2}+D_{-2}.
\tag{3}
$$

这里 $T_{-2}$ 由已发完整十四族的真权 $-2$ 系数生成；$D_{-2}$ 是同一份数据给出的全部平移分母。低层的分母保留了同一个八矩 cocycle：

$$
\begin{aligned}
D_0^{(-2)}&=\partial_\omega F_0^{(-2)}-\mathfrak c_{-2}(m_0),\\
D_{2,i}^{(-2)}&=\partial_\omega F_{2,i}^{(-2)}-\mathfrak c_{-2}(m_{2,i}),
\end{aligned}
\tag{4}
$$

最高层则为对应状态系数的 $\partial_\omega$。不能把 (4) 改成没有 cocycle 的单独状态导数。

设条件 K 给出的真实泛函为 $\lambda_{-2}$。因为当前指定点已经消灭完整分母呈示和响应，(3) 给

$$
\lambda_{-2}(R_{-2})=0,\qquad
\lambda_{-2}(\mathsf N U_{-1})=0.
\tag{5}
$$

定义整个 $U$ 上的实线性泛函

$$
\boxed{\lambda(V)=\lambda_{-2}(\Pi_{-2}V).}
\tag{6}
$$

其它权上的值准确为零，不需要重新编译或评价那些权。由 (2)、(5)，

$$
\lambda R=0,\qquad \lambda\mathsf N=0,
\qquad \lambda\mathsf P_{H,0}=H^{-2}\lambda.
\tag{7}
$$

有限维表示中 $\mathsf P_{1,d}=\exp(d\mathsf N)$，所以

$$
\boxed{\lambda\mathsf P_{H,d}=H^{-2}\lambda.}
\tag{8}
$$

这就是整个真实 $U$ 上的权 $-2$ 仿射字符。它非零：R177 对原 normal 90，即真实 $J\in U_{-2}$，赋值为 1。若条件 K 成立，这个值已是原函数值，不能再把 J 视为形式独立标签。

## 3. 同一个规范化乘子，不为路径另选参数

使用 R163 的同一八参考态和线性映射

$$
\Gamma(M)=\sum_i a_i(M)L_0(S_i^*),\qquad
\mathscr L=L-\Gamma(m),\qquad
L=v-\mathcal B_mN,\qquad m=m_0+m_2.
\tag{9}
$$

全部 $N^{[0]},N^{[2]}$、$\Gamma(m_2)$ 及真实导数已经包含在已发正规系数中。对任意真实开平端路径 B，

$$
\mathcal I(B)=\left[\int_B\mathscr L\,ds\right]\in U/R,
\qquad \Lambda(B)=\lambda\mathcal I(B)
\tag{10}
$$

良定义。一般 $M_B\ne0$ 时，$\Lambda(B)$ **不是**该路径的完整第四成本。

R164 对任何真实权 $-2$ 仿射字符已经给唯一协变的规范化乘子，不需要先假设其正性。R177 的实际完整系数取值给

$$
\boxed{\mu=(0,1/2,2,0,0,0,0,2),}
\qquad
c=0,\quad d=(0,1,6,0,0,0,0,4),
\tag{11}
$$

八坐标顺序为 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$。它们满足同一个 cocycle 的

$$
\mu\rho_g=H^{-2}\mu+\lambda\mathcal C_g,
\tag{12}
$$

因此

$$
\mathcal A_\lambda(B):=\Lambda(B)-\mu(M_B)
\tag{13}
$$

对所有起止状态、末 frame、时长与联动 $h,k$ 路径共用同一 $\mu$。

若要与 R140 的原环境延拓写法对齐，任选 $\widetilde\lambda$ 到包含原 L 与参考根的有限真实环境。应使用

$$
\mu_{\rm raw}=\mu+\widetilde\lambda\circ\Gamma.
\tag{14}
$$

于是 $\int\widetilde\lambda L-\mu_{\rm raw}M=\mathcal A_\lambda$。不能把未必属于 U 的原参考根 $L_0(S_i^*)$ 直接当作独立 λ 坐标，也不能把 (11) 与不同规范化下的原乘子混用。

## 4. 完整全路径严格正性

令 $r=\log h$、$v=r'$、$u=k/h^2$、$\psi=h u'$。R177 的完整十四族和准确边界恒等式给

$$
\begin{aligned}
\mathcal A_\lambda(B)=\int_B\Bigg[
&h^{-2}\left\{\frac{(1+k^2)^2}{4}+(k')^2+(1+k^2)v^2
+\frac{k^2}{4}(k'-2kv)^2\right.\\
&\left.\qquad+\left(v'-\frac23v^2\right)^2+\frac{34}{9}v^4\right\}
+\frac1{16}(\psi')^2+\frac{11}{48}v^2\psi^2
\Bigg]ds.
\end{aligned}
\tag{15}
$$

所有 normal、面积型、二次与四次速度项均已包含；原分部积分势在平端两端为零。真实角变量仍由

$$
\omega_s=\frac{k_s}{2h}
\tag{16}
$$

积分，frame 按真实 ODE 演化。没有假定这两个端量可以独立重置。

对任一有限正时长 B，$h>0$ 且光滑，因而

$$
\boxed{\mathcal A_\lambda(B)\ge\frac14\int_Bh^{-2}\,ds>0.}
\tag{17}
$$

这是所有真实开平端 scalar 路径上的严格结论，已经超过有限必要测试。结合 (7)、(14) 与 R140 的反向蕴含，$\lambda$ 是真实成本闭锥的非零正字符。

这里没有循环：先由条件 K 与完整头部得到真实线性字符，再用已证明的全 action 恒等式证明正性。不是先以正性为理由假定其原函数赋值良定义。

## 5. 对完整 M=0 路径的原第四成本结论

设 B 为同 scalar germ、frame $I\to I$ 的有限实际平端路径，且 $M_B=0$。由 R105，$V_B\in U$，即使 $T_B$ 非零也成立。

R109 的未取商身份为

$$
V_B=\int_B L\,ds
-\int_B\mathcal B_mH\,ds
-\frac16\int_B\mathcal B_A(\tau_{A,m})\,ds.
\tag{18}
$$

后两项的完整函数值在 R 中；常势端项由真实 $A(L)=M_B=0$ 消失，而不是被另设为零。又

$$
\int_B\Gamma(m)\,ds=\Gamma(M_B)=0,
\qquad \mu(M_B)=0.
$$

因此 (7)、(10)、(13)、(18) 准确给

$$
\boxed{\lambda(V_B)=\mathcal A_\lambda(B)
\ge\frac14\int_Bh^{-2}\,ds>0.}
\tag{19}
$$

特别地，对主构造要求更强的 $M_B=T_B=0$ 路径同样成立。这一结论排除任何非空此类路径的**完整 universal canonical 第四成本恒零**。所有实际连接、重复块及其历史均已由 (18) 保留；不依赖大 N 渐近，也没有把桥成本估成零。

同端口的有限个 $M=T=0$ 块可按 R83 真实相加，其 λ 值也相加为正。正仿射缩放只把该值乘以 $H^{-2}>0$，有限缩放不能使其等于零。对每条具体路径还可写下界 $L/(4\max h^2)$，但不声称在任意无界参数族上存在统一正间隙；闭锥中的极限与实际非空路径仍须区分。

frame/scalar 返回不等于中心线位置闭合。若进一步要求中心线真实闭合，所得路径只是上述类的子类，(19) 仍是其必要障碍；本稿不因 (19) 就宣布已经构造或分类了闭嵌入曲面。

### 5.1 R83 已覆盖的一种非零传入历史

R83 的完整传递式在 $M_B=T_B=0$ 时，对它所允许的任意同右 collar 传入 profiles $w,u$，准确化为

$$
(w,u,v)\longmapsto(w,u,v+V_B).
\tag{20}
$$

因此只改变这类传入 second/third scalar 历史不能改变该块的第四增量。这里需要 M 和 T 作为**完整算子**为零；仅在选定 profile 通道上低阶值为零不足以删除全部交叉项。

(20) 不授予改变目标度量、任意更换 canonical 恢复规则或未经分类的新 gauge。超出这条明确传递公式的选择，仍须另作完整证明。

## 6. Universal 非零与固定 profile 圆之间的区别

对一个任意预先给定的 profile 对 $(f,g)$，令

$$
\mathcal E_{f,g}:U\longrightarrow
\{\text{该对 profiles 上的完整输出函数}\}
\tag{21}
$$

为代入映射。$V_B\ne0$ 作为 universal 算子，不必推出
$\mathcal E_{f,g}(V_B)\ne0$；后一个映射可能有核。也不必存在一个只用这同一 profile 圆的查询泛函来表示当前 λ。

准确的附加条件是 $\lambda$ 消灭 $\ker\mathcal E_{f,g}$；更强但方便的充分条件是 $\mathcal E_{f,g}$ 在整个 U 上单射。未证明这个条件时，不能用 (19) 排除某个特殊圆上的几何解，更不能外推为所有 profile 圆都失败。

### 6.1 已有定理可给存在性的 faithful 固定圆

R105 第 8 节和 R96 已支付另一个完整构造：先固定有限真实成本基及必要辅助小族，选其共同合法物理区间 I，再在 I 内选一个非退化、归一、$C^\infty$ 三矩圆 $(f_*,g_*)$ 及有限真实查询，使

$$
\mathcal E_*:U\longrightarrow\mathbb R^{\dim U}
\quad\text{单射。}
\tag{22}
$$

于是 λ 可通过同一个圆上的有限查询运输为 $\lambda_*\mathcal E_*=\lambda$。对每条在这个共同 I 上确实合法的上述非空 $M=T=0$ 路径，

$$
\lambda_*\mathcal E_*(V_B)>0,
\tag{23}
$$

所以它不可能在该特选圆上支付完整 canonical 第四周期。这一圆由准确存在性构造选择，不能把它替换成任意既存候选，也没有给它的数值清单、导数界或 reach 控制。三矩配平不自动支付其所有低阶 ruling；(23) 是即使其它必要门可付时仍存在的第四周期障碍。

## 7. 与既有 P1 排除及主课题的关系

R98 的结果针对正长度 reciprocal 状态组合的 universal $P_1$，以及经 R96 转移后的特选圆。它不自动排除固定有限 N 时 $P_0+NP_1$ 的相消。

条件 K 若通过，(19) 直接作用于当前真实路径的**完整** canonical $V_B$；它不借用 P1 首项、圈数极限或分离不同 N 次数。因此对于确实属于这里的零矩、零第三闭端口路径，完整周期零被排除；不能仅以 R98 已有结论替代这一步。

同样必须保留：

- 原模型中的整个矩阵 M=0、整个第三算子 T=0，比仅对某个指定 profile 圆支付低阶 range 更强；后一类候选不因本文自动被排除。
- 目标规则仍为 $g_X+\varepsilon^2 dY_f\cdot dY_f$，全部右锚及恢复历史固定；不同目标或未纳入 (20) 的校正机制另论。
- 原第四周期的 universal 障碍，不是对所有负曲率带、所有光滑等距族或所有闭曲面的不可能性定理。
- 第四逐 s ruling、完整双 collar、高阶收敛、嵌入、reach 和宏观幅度并未由此得到解决。

## 8. 下一 actual 的两种解释

如果共同表只找到一条被 R177 违反的真核关系，则该点不能定义 λ；已证全 scalar action 正性仍是一条正确的形式坐标事实，却不产生 (19)。

如果完整 77 列处理完、所有规范语法与转换身份支付，并且指定点消灭完整核，则 (6)–(23) 都是现有定理的直接推论。此时没有还需补跑的 LP、相邻权编译或旧路径测试；真正新增的内容是原函数定义域终于成立。

若过程预算退出或只完成前缀，且未找到切除关系，只能保留相应部分证据，不能把它解释成条件 K 已通过。
