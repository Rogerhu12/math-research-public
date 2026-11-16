# R876：九个域范数生成元、原两投影与刚性化 Hecke 理想

日期：2026-11-16。状态：**本篇证明一条有限、完整的原 Hecke 理想消费者路线；尚未执行新的铅笔、范数理想或谱支持计算。** 原 R873 消费者首 run 已完成原件运输，但在新数学开始前停止；十七个对应系数尚未成，本文不预填其输出。R872 当前首 scope 的点函数/低权来源也不是下文六个128维空间的已成基。

本文使用原 $Y=X_1/\mu_3$、$g=127$、$H=K_Y+C$、$\deg H=272$，及原 $K=\mathbf Q(\sqrt{-3})$ 结构。保持原 $-3$ 下降、level82、所有同态相位与原 $82^2$ 截面尺度，不引入 $T_5$ 或未扭曲曲线。

依赖：

- [R873 原循环七对应](R873-original-cyclic-seven-correspondence-from-short-section-norms.md)，特别是原两投影、$P(U)=0$、目标 $z,w$ 的嵌入及 §10 的 dual-seven 范数同构；正式证明 SHA256 为 `e6401ca85f64c5b9a19afbf9bee2b8f4199864e82eff2e4689bdae882735716f`。
- [R870 原有理 Picard 挠判与支持](R870-original-rational-Picard-torsion-and-T7-support-certificates.md)，保留 $\operatorname{Nm}_{\pi_t}\pi_s^*$ 的冻结方向。
- [R849 原五个完整极理想图](R849-certified-original-global-function-and-five-polar-ideal-DAGs.md) 和 [GP](../notes/R839-original-global-addition-polar-ideals-and-eta-DAG.md)：这里使用 `eta_degree_zero_fractional_ideal`，不换成三同源后的 `real_descent_degree_zero_fractional_ideal`。
- [原刚性化纤维](../notes/2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md)、[原 YP](../notes/2026-11-16-original-Y-RR-connections-and-Hecke-period-row.md) 及 [原有限 RR](../notes/2026-11-16-original-Y-finite-RR-matrices-and-source-leaves.md)：原线丛、局部帧与真正双图 RR 条件。
- R806 原 $W=M_w$、R820 原正规两图及 R860 原 adjugate 函数嵌入；它们均按实际完成 producer 保留，不重求旧乘法矩阵。

## 1. 本篇实际消去的计算

设原循环七对应的正规曲线为 $\mathcal C_7$，两支为
$$
p=\pi_s:\mathcal C_7\longrightarrow Y,\qquad
q=\pi_t:\mathcal C_7\longrightarrow Y,\qquad
\deg p=\deg q=8.
\tag{876.1}
$$
$p$ 保留原椭圆曲线与原 level82 结构，$q$ 取指定循环七商。记 $F=k(Y)$、$E=k(\mathcal C_7)$；有限域版本也允许总秩八的泛点可分代数，不以一个猜测的不可约性代替真对应来源。

本篇不要求先材料化 $p_*\mathcal O_{\mathcal C_7}$ 的2176维 $k[z]$ 正规整基。新的范数运算只需：

1. 原 $E/F$ 的实际八维乘法，或等价的源绑定 unit-solve 表达式；
2. 目标线丛的两个真实全局截面；
3. 九个八维域范数；
4. 原 $Y$ 两图上的完整分式理想运算。

这是完整范数线丛的生成元公式，不是只在一个稠密开集或一个 $z$ 纤维上比较理想。$P$ 的首项、$P'$ 或所选 adjugate 分母的零点不从曲线上删去。

## 2. 任意八次有限曲线映射的九范数引理

令 $p:C\to Y$ 为光滑射影曲线之间的有限平坦映射，次数八；令 $\mathcal M$ 为 $Y$ 上的线丛，且 $u,v\in H^0(Y,\mathcal M)$ 在整个 $Y$ 上无共同零点。用任一非零 generic frame $e$ 将它写为
$$
u=a e,\qquad v=b e,\qquad a,b\in F.
$$
再给一个实际映射 $q:C\to Y$。令 $t_0,\ldots,t_8\in k$ 两两不同；在本项目特征零及特征大于八的约化中可固定 $t_i=i$。

范数线丛按行列式定义
$$
\mathcal N=\operatorname{Nm}_{p}(q^*\mathcal M)
=\det(p_*q^*\mathcal M)\otimes\det(p_*\mathcal O_C)^{-1}.
\tag{876.2}
$$
其 generic frame 是 $\operatorname{Nm}_p(q^*e)$。在这个同一帧中定义九个有理函数
$$
n_i=N_{E/F}\bigl(q^*a+t_iq^*b\bigr),\qquad 0\le i\le8.
\tag{876.3}
$$

**引理。** 九个 $n_i$ 在这个 generic frame 中完整生成 $\mathcal N$ 的嵌入分式理想。等价地，九个截面 $\operatorname{Nm}_p(q^*(u+t_iv))$ 在整个 $Y$ 上无共同零点。

**证明。** 固定源点 $P\in Y$，在 $p^{-1}(P)$ 的每个点 $Q$ 选择 $q^*\mathcal M$ 的局部基。因为 $u,v$ 无共同零点，所得两个局部系数的约化不同时为零。对每个几何点 $Q$，至多一个常数 $t$ 使 $u+t v$ 的约化为零。次数八的 scheme-theoretic 纤维长度八，所以其几何支撑至多八点。九个不同常数中至少一个在全部这些点都不坏。

于是该线性组合在整个半局部纤维邻域生成 $q^*\mathcal M$；其范数截面在 $P$ 生成 $\mathcal N$。这对每个 $P$ 成立。这里没有使用 étale 性；非约化纤维中“约化非零”恰使局部系数为单位。

若用 DVR 形式核验同一结论，在统一 generic frame 中写局部线丛格为 $\varpi_Q^{m_Q}\mathcal O_Q$，则所有组合的赋值至少 $m_Q$，而选出的组合在全部 $Q$ 同时取等号。精确公式为
$$
v_P N_{E/F}(x)
=\sum_{Q\mid P}[\kappa(Q):\kappa(P)]\,v_Q(x).
\tag{876.4}
$$
分歧已在 $v_Q(x)$ 中体现；这里不能把剩余域次数漏掉，也不能另乘一次分歧指数。所得最小赋值恰是行列式范数格的指数。故九生成元给完整格。$\square$

generic frame 改为 $e'=c e$ 时，$a,b$ 同乘 $c^{-1}$，所以九函数同乘 $N_{E/F}(q^*c)^{-1}$；与此同时 norm frame 正乘 $N_{E/F}(q^*c)$。两者完全抵消。因而(876.3)是同一线丛的规范描述，不引入未定单位、周期或 Manin 尺度。

特别地，计算域范数可用任意真正 $F$ 基；行列式比与基变换无关。无须把幂基误称为整基，更无须假设 $F[U]$ 在所有闭点已经正规。

## 3. 原五个输入与一个公共参考空间

原 R849 的准确理想为
$$
\mathcal L_j=\mathcal O_Y(-Z_j),\qquad
Z_j=q_jE_{g_j}-p_jE_f,\qquad
\deg Z_j=0,\qquad 1\le j\le5.
\tag{876.5}
$$
这里 $p_j/q_j$、全部七共轭、原目标同源常数与负 Picard 类号均沿 R791/R849；本文不重新归一。原 $\eta_{h_j}=-[\mathcal L_j]/q_j$。

从这里起采用 R849 分式理想嵌入的同一 generic frame $1$；若 RR producer 使用另一帧，先按 §2 的范数转移回此嵌入。

取
$
\mathcal M_j=\mathcal L_j(254P_0),\qquad
\mathcal M_0=\mathcal O_Y(254P_0).
\tag{876.6}
$$
六者度数都为 $254=2g$，故
$$
h^0(\mathcal M_j)=128,\qquad h^1(\mathcal M_j)=0,
$$
且各自全局生成：减任一点后度数253大于 $2g-2=252$，评价映射满射。

对每个 $j=0,\ldots,5$，若已取得一个真实无基点二截面铅笔 $(u_j,v_j)$，记按(876.3)生成的完整分式理想为 $J_j$。则
$$
J_j=\operatorname{Nm}_{p}(q^*\mathcal M_j),\qquad
J_jJ_0^{-1}=\operatorname{Nm}_{p}(q^*\mathcal L_j).
\tag{876.7}
$$

因此参考 $M_0$ 只算一次供五方向共用；不另求 $\operatorname{Nm}_p(q^*P_0)$ 的点分解，不把目标椭圆点的分歧多重性猜成一。总共六个铅笔、每个九个范数即可给五个完整 Hecke 理想。每个 $J_j$ 度数2032，商度数零。

本公式也可只对一个 $j$ 与参考 $j=0$ 先执行。它不要求先得到全部五个方向的支持。

## 4. 两个截面的完整性只需一个672阶子式

这里的 $V_2=H^0(Y,2H)$ 是原已成418维空间，截面本身已含 $82^4$ 尺度；本篇不会再乘一次该尺度。

给定两个已经由真实双图来源证明属于同一 $\mathcal M$、且至少一个非零的截面 $u,v$，设其共同零除子为 $Z\ge0$。准确乘法图为
$$
\mu_{u,v}:V_2\oplus V_2\longrightarrow H^0(Y,\mathcal M+2H),
\quad(a,b)\longmapsto ua+vb.
\tag{876.8}
$$
它的源维数836。剥去共同零点后是无基点铅笔，Koszul 正合列给
$$
\ker\mu_{u,v}=H^0(Y,2H-\mathcal M+Z).
$$
右端度数 $544-254+\deg Z=290+\deg Z>252$，故
$$
\dim\ker\mu_{u,v}=164+\deg Z,\qquad
\operatorname{rank}\mu_{u,v}=672-\deg Z.
\tag{876.9}
$$
目标度数798、维数672。因此一个实际非零672阶子式恰好认证 $Z=0$；不需要先材料化目标的672维基，也不把两个候选的模线性独立当成无基点。

此判据并不要求先取得完整128维基：任何两个真正属于 $\mathcal M$ 的截面，只要通过(876.9)，已经足够。若使用128维 RR producer，则须保它实际完整的原线丛与双图 membership 来源，不能把预期 RR 维数当作已经算出的基。

### 4.1 三个完整原 z 纤维给816行

原 $z:Y\to\mathbf P^1$ 的次数为272。选三个不同有限值 $z=a_1,a_2,a_3$，其完整 scheme-theoretic 纤维避开当前有理表示的分母，并保各线丛的实际局部基。它们的总长度是816。由于
$$
816>798=\deg(\mathcal M+2H),
$$
对目标空间的全纤维评价是单射。因而(876.8)可形成一个
$$
816\times836
\tag{876.10}
$$
的真实有限矩阵；一个672阶非零子式已经给完整无基点证书。

“完整纤维”是原272秩有限代数，包含重根与非拆剩余域；不能只挑该纤维内一个点。若纤维非 étale，仍在长度272的商代数中评价。只要原选定分母在该代数中可逆，整个函数/线丛评价合法。

这不生成新的 $q$ 尾。原418个 $V_2$ 截面及原两图乘法/评价来源直接复用。新计算只有新两个截面在三个实际有限代数中的评价、836个乘积列、672阶子式及其源身份。

### 4.2 搜索的有限边界不是实际成功声明

在无限特征零域，真实128维基的全局生成性保证无基点铅笔存在。有限域也只接受实际(876.9)证书。可用一个确定性备用搜索：固定任一非零 $u$，对真基 $s_0,\ldots,s_{127}$ 试
$v(T)=\sum T^is_i$。$u$ 的几何零支撑至多254点，每点至多127个坏参数；所以在多于 $254\cdot127$ 个不同常数中必有一个无基点值。基域不够大时可作明确的有限域扩张，完整记录原剩余域及降域身份。首个预算只检查有限前缀时，全部失败仅表示该前缀未给证书。

## 5. 真两投影、原 −3 下降与刚性化方向

(876.7)直接按 R873 便于函数计算的方向 $\operatorname{Nm}_{p}q^*$ 写成。冻结的 R870 运算是
$$
\mathcal H_7(\mathcal L)=\operatorname{Nm}_{q}(p^*\mathcal L).
\tag{876.11}
$$
R873 §10 的原 dual-seven involution $\jmath$ 有
$p\jmath=q,\ q\jmath=p$。它的平方由标量 $7I$ 的原 level82 作用消去，且与原 $-3$ 下降相容。因此
$$
\operatorname{Nm}_{q}(p^*\mathcal L)
\xrightarrow{\;\jmath\;}
\operatorname{Nm}_{p}(q^*\mathcal L).
\tag{876.12}
$$
该同构同时运输行列式 norm 的分子与分母；对基的排列号在两处抵消。本文每个输出都必须记录(876.12)，不能只说两个 endomorphism 自伴或有相同特征多项式。

原 RF 帧也保持。写 $\delta_j=p_j-q_j$，原 $P_0$ 局部参数为 $t$，则
$$
e_{j,0}=t^{-7\delta_j},\qquad
m_{j,0}=t^{-7\delta_j-254},\qquad
m_{0,0}=t^{-254}.
\tag{876.13}
$$
相除恰回到原 $e_{j,0}$。在原 $P_1$，原 $L_j$ 单位帧与参考移动因子都沿既成 RF 来源；不得替换为新任意 CM 常数。

范数线丛的源 $P_0$ 纤维按完整长度八的有限代数定义：
$$
\operatorname{Nm}_p(q^*\mathcal L)|_{P_0}
=\det\bigl((p_*q^*\mathcal L)\otimes\kappa(P_0)\bigr)
 \otimes\det\bigl((p_*\mathcal O_C)\otimes\kappa(P_0)\bigr)^{-1}.
\tag{876.14}
$$
这里包括非约化结构，不能以八个互异点值之积代替。对(876.7)、(876.12)施
$\operatorname{Rig}_{P_0}(L)=L\otimes L(P_0)^{-1}$
得到同一原刚性化 Hecke 线丛；比较同构在纤维上的作用也同时取逆张量。

九个生成元给的是同一 generic frame 中的**实际嵌入理想等式**，不是只给抽象 Picard 类。更换无基点铅笔不会改变这个分式理想。若后继选择其中某个局部生成元作帧，必须同时保存其与(876.14)原 determinant frame 的单位转移。首个仅做谱支持的消费者可保这个有限纤维/单位为准确表达式；它不能将尚未求值的单位写成1，也不能据此删除任何非 $p$ 校准项。

## 6. 不展开对应整基的有限函数算术

令 R873 真输出给
$$
P(U)=0,\qquad q^*z=U,\qquad q^*w=V=\frac{K(U)}{P'(U)}
\tag{876.15}
$$
以及相应原源函数叶。只在函数域中除以首项与 $P'$；这不声称这些分母在所有闭点都是单位。

原正常基 $\beta_0=1,\ldots,\beta_{271}$ 与已成 $W(z)=M_w(z)$ 满足
$(\beta_0,\ldots,\beta_{271})W=w(\beta_0,\ldots,\beta_{271})$。
设
$$
A=VI-W(U),\quad Q=A_{\{1,\ldots,271\},\{1,\ldots,271\}},\quad
r=A_{0,\{1,\ldots,271\}}.
$$
原 principal cofactor 是 $T$ 的首一271次多项式，而 $w$ 的原最小多项式次数272，故它在原函数域不为零；真正目标嵌入保持非零。因此 $Q$ 在 $E$ 中可逆。一次准确转置 unit-solve
$$
Q^{\mathsf T}h=-r^{\mathsf T}
\tag{876.16}
$$
给 $q^*\beta=(1,h^{\mathsf T})$。实际只需求这一右端，不要求显式272阶幂基逆或271阶完整逆；解后核全272条 $q^*\beta\,A=0$（包括余下首列关系）和 $\beta_0=1$，作为成功出口。该新目标代入可给全部六铅笔及以后 Hecke 迭代共用。

若某实际截面具有原 normal 表达 $s=\sum a_i(z)\beta_i$，则
$q^*s=\sum a_i(U)(q^*\beta_i)$。原 field/phase/分母均保留。对于每个 $q^*(u_j+t v_j)$，在实际八维 $F$ 代数中形成乘法矩阵并取其行列式，正是(876.3)。可以保存八次 companion 上的精确有理表达式，或在合法有限域中材料化；二者不得互相冒充。

原 $W$、原 normal 基、原 $V_2$、R873 的旧范数前缀与原128空间若已有完成输出，均只读复用。新目标 unit-solve、九个范数及理想运算各自原子保存；已成的 $j,t$ 不能在续算时重做。

## 7. 有限域支持见证的准确范围

这条路线可先在一个**真实合法的好约化域**执行。它不要求先把六个特征零128维基展开成巨大有理数；但必须先有：

- 原 $Y$、两图、$H$、$P_0$ 及五个 $L_j$ 的同一整模型/约化身份，实际分母和过渡均合法；
- 原循环七对应两投影在该模型上的来源，特征不为 $2,3,7,41$；只读一个模 $P$ 不能代替这个几何来源；
- 原系数域的真实剩余域分解。不能假定原14次场多项式在辅助素数下不可约或全分裂；
- 真正对应于原五个 $L_j$ 约化的截面及两图完整 membership。只在模 $p$ 中构造的截面可以用于这个有限域消费者，但不因此称其特征零坐标已完成；
- 实际无基点 minor、完整九范数理想、参考商及每次 Picard 运算的完整双图证书。

在这些条件下，算法计算的是原 $\mathcal H_7(L_j)$ 的真约化。R870 已成 $n_iP_i(T_7)$ 与全部16个谱块可直接消费，不重算 $T_7$，更不新算 $T_5$。若某个实际有限域类
$$
\overline{\,n_iP_i(T_7)\xi_j\,}\ne0
\tag{876.17}
$$
被完整有限 Picard 算法认证，则原有理类 $n_iP_i(T_7)\xi_j$ 不为零；R870 的挠判随即证明 $E_i\eta_{h_j}\ne0$ 于有理 Picard 空间。

非零出口可用完整 degree-zero RR 空间为零的准确证书，或已证明唯一性的有限 Picard 正规形式。一个点/单个 $z$ 纤维的非零值不是(876.17)，也不能把一个任意模 lift 的非零当作原 Picard 类的非零。反之，模类为零始终保持未决，不能反推特征零 inactive。

为控制迭代大小，可在每次真正 Hecke 运算后将 degree-zero 类再移动到254度，重新取无基点铅笔；于是几何度数不随 $P_i$ 的整数系数增长。对应的目标嵌入(876.16)和公共原基础来源保持复用。这是实际 Picard 运算的有限流程，不是已执行80项支持计划的声明。

## 8. 最小消费者契约及当前缺口

新的最小 scope 可以只选一个原 $j$，加参考 $j=0$：

| 输入/新阶段 | 必须保留的真实字段 | 准确出口 |
|---|---|---|
| 原类 | R849 `eta_degree_zero_fractional_ideal[tau/sigma]`、原 $p_j,q_j$、R850/RF帧 | 同一原 $L_j$，不是三同源后的另一理想 |
| 参考移动 | 原 $P_0$、$M_j=L_j(254P_0)$ 与 $M_0$ 两图 | 254项按(876.7)准确取消 |
| 两真实截面 | 各自双图 membership/原normal或unit-solve表达；若有128basis则保其producer | 不能只给预计128维 |
| 铅笔评价 | 三个实际完整纤维、分母逆、816×836矩阵的672minor | 全局无共同零点 |
| 对应 | R873真证书、17系数与原 $P,K/P'$、源/靶/dual7 | 同一实际八次范数 |
| 目标normal嵌入 | (876.16)实际解、全272关系及归一 | 不计算原 $W$ 或原source逆 |
| 范数函数 | 每个 $j,t$ 的实际8×8乘法/行列式或其准确DAG，$t=0,\ldots,8$ | 每个函数是真域范数 |
| 两图范数理想 | 九个生成元的完整像、参考逆理想及过渡 | 完整 $H_7(L_j)$ |
| 刚性化 | 同generic frame、(876.13)–(876.14)、$\jmath$ 的分子/分母运输 | 原 $P_0$ 刚性化，不造单位值 |
| 可选支持 | 真好约化/原剩余域、R870多项式、完整非零 Picard 证书 | 仅实际通过的块标 active |

当前尚未得到六个 $\mathcal M_j$ 的真实无基点铅笔，也未得到新的九范数理想或(876.17)见证。R873 尚未完成的新系数不得填为 producer。R872 已成的146/418固定空间也不能当作本表128维输入。源码、参数、纸面证明及简明来源/SHA登记可入Git；机器矩阵、回执、理想与各次范数向量仅在一日 active artifact/carrier 续传。

本篇准确新增的是：完整范数可由九个原域范数生成元得到；672阶子式有一个明确的三全纤维入口；六个移动空间只需一个公共参考；所有这些等式保原源靶、分歧、剩余域次数与刚性化。实际 Hecke 活跃支持、校准主函数、非 $p$ 项以及原高度仍待各自真实出口。
