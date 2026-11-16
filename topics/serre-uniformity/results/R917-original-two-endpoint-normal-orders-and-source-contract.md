# R917：原两个端点的八阶正规 order 与可续接来源合同

日期：2026-11-16。状态：本文给出下一公开消费者的准确算法和来源闭包；**尚未执行新的端点系数展开、order 扩大或端点范数求值**。R914 已于真实 run43898224893 成功，下文绑定其实际完成来源。本文不修改已冻结的 R903、R907 或 R914。

本篇接 [R912](R912-original-eight-dimensional-endpoint-lattices-and-norm-frames.md) 的端点格算法，将它落实为两个可以先于五个目标 RR 空间完成的有限对象：原循环七对应在 $P_0,P_1$ 的完整秩八正规 order、它们相对原 primitive 坐标及原参数的标记。新增的共同清分母式避免在 $θ$ 有零的端点先作一次无必要的除法；每次正规化只解一个至多八未知量的有限线性核。

## 1. 原对象与本次实际地方

保持 [R873](R873-original-cyclic-seven-correspondence-from-short-section-norms.md) 的原方向

$$
p=π_s:C_7\longrightarrow Y, \qquad q=π_t:C_7\longrightarrow Y, \qquad \deg p=\deg q=8.
\tag{917.1}
$$

原 primitive 函数是 $U=q^*z$，原关系及靶函数是

$$
P(U)=\sum_{i=0}^8 a_iU^i=0, \qquad q^*w=K(U)/P_U(U), \qquad
K(U)=\sum_{i=0}^7 k_iU^i.
\tag{917.2}
$$

$a_i,k_i$ 的特征零含义始终是 R873 的原2058列单位解；[R882](R882-certified-original-cyclic-seven-common-place-coefficients.md) 已在同一合法地方给出全部17列并完成全部2200行乘回。这里没有新的2058逆或 Fourier 尾。

首消费者实际地方固定为

$$
\ell=1000000753, \quad ζ=549966761, \quad s=99932770.
\tag{917.3}
$$

所有 residue 数组只能在该原地方合用。数值正规 order 是该地方的实际 $k[[ρ]]$-order，$k=\mathbf F_\ell$；不得把其中选出的模常数基变换改称已展开的特征零基。原特征零对象及其有限正规化定义仍由同一准确 $P,K$ 给出，两个字段分别保存。

原局部参数和形式域为

$$
ρ_0=z-z(P_0), \qquad
ρ_1=ι^*ρ_0=z-2β_{72}-z(P_0), \qquad
R_\epsilon=k[[ρ_\epsilon]], \quad F_\epsilon=k((ρ_\epsilon)).
\tag{917.4}
$$

$ι=T^{41}$ 是原 $K$-线性几何 involution，不是算术共轭；常数 $s$ 不变。R914 的完整 $146\times146$ 作用及560行乘回才允许把完整 $V_1/τ$ jets 从 $P_0$ 运到 $P_1$，R853 的三列和 R866 的127维全纯矩阵均不能替代它。

R873/R912 给这两个原端点的几何局部型为两个长度一因子和两个长度三因子。保持非拆域及全部幂零元，正规 order 的特殊纤维几何型为

$$
\bar k\oplus\bar k\oplus\bar k[π]/(π^3)\oplus\bar k[π]/(π^3).
\tag{917.5}
$$

原好约化和 tame 条件在 (917.3) 成立；因此其正规 order 的 trace discriminant 阶恰为4。本文的小核论证也适用于特征零；若另用剩余特征，必须保原好约化并要求特征大于16，不能仅列避开 $2,3,7,41$。

## 2. 十七列只需一次共同清分母

令

$$
θ_0=θ/τ, \qquad A=N_{692}/τ^4.
\tag{917.6}
$$

R807 的原准确关系为 $\widehat E_6/τ^3=A/θ_0$。原2058个函数分为2050个 $V_8/τ^8$ 单项式和八个

$$
(A/θ_0)^2\,m_r, \qquad m_r\in V_2/τ^2,
\tag{917.7}
$$

其中 $m_r$ 正是原补列索引 $0,1,2,3,73,74,75,76$，并保 R873 已存的原叶 recipe。对每个 $c\in\{a_0,…,a_8,k_0,…,k_7\}$，用同一个原坐标列分解

$$
c=v_c+(A/θ_0)^2m_c, \qquad
\widetilde c=θ_0^2v_c+A^2m_c.
\tag{917.8}
$$

$v_c\in V_8/τ^8$，$m_c\in V_2/τ^2$。故 $\widetilde c$ 是原 $V_{10}/τ^{10}$ 函数，在两个实际端点的原 $τ$ 图上正则。定义

$$
\widetilde P=θ_0^2P, \qquad \widetilde K=θ_0^2K.
\tag{917.9}
$$

因 $θ_0$ 属于源函数域且与 $U$ 无关，准确地有

$$
\frac{P}{a_8}=\frac{\widetilde P}{\widetilde a_8}, \qquad
\frac{K(U)}{P_U(U)}=\frac{\widetilde K(U)}{\widetilde P_U(U)}.
\tag{917.10}
$$

这没有换一个对应，也没有忽略 $a_8$；它只在进入局部算法前取消一个真实共同因子。特别是无需先求 $1/θ_0$，也不把端点的 $θ_0$ 当作单位。

### 2.1 可直接消费的展开叶

全部17个 $\widetilde c$ 的 jets 只需要：

1. R914 的两个 $273\times146$ 原 $e_i/τ$ jet 矩阵；$e_i=82^2T_{1,i}$ 的尺度已经含在源中。
2. R873 的2050个八叶 recipe、八个二叶补列，以及 $N_{692}$ 的非零四叶 recipe；它们均已内嵌在原 source-target DAG。
3. R807 的 $θ$ 在原146列中的准确有理坐标，以及 $N_{692}$ 的962个 numerator/一个 common denominator。
4. R882 的 $2058\times17$ 原同地方坐标矩阵。

每个原有理分母只减一次；无新增 $82$、$82^2$ 或 $82^8$ 乘子。每个单项式的叶序可作交换性缓存，但必须保原 source coordinate index 和 recipe 身份。

R883 已实际完成 $P_0$ 的 $θ_0,A$ 前三项；新消费者直接复制这三项，展开时只补第3阶及以后，并将完整新列与旧前缀逐项绑定。$P_1$ 的全部项来自 R914 的真正几何运输，不拿旧 $z=0$ 的 R885 值代入。

现有精度是 $O(ρ^{273})$。17个新完整 jets 和每个 recipe 块分别原子保存；预算中断后只做尚未完成的块。R914 的真实 producer 已可读取，使用下文实际矩阵与 jet 原件，不能用预计的反射矩阵或模数填空。

## 3. 初始首一 order：一次准确消首项

以下固定一个端点，记 $ρ=ρ_\epsilon$。设实际已知精度为 $N$，令

$$
a=v_ρ(\widetilde a_8)<N.
\tag{917.11}
$$

若尚未看见非零首项，返回 NeedPrecision，并保实际已知下界 $v_ρ(\widetilde a_8)\ge N$；不把零截断当作准确零。对每个 $i<8$，已知非零系数使用真实阶 $b_i$，全零截断只使用下界 $b_i\ge N$。选择最小非负整数 $h$，满足

$$
b_i+h(8-i)\ge a \quad(0\le i<8).
\tag{917.12}
$$

置 $Θ=ρ^hU$。原首一关系为

$$
G(Θ)=Θ^8+\sum_{i=0}^7g_iΘ^i, \qquad
g_i=ρ^{h(8-i)}\widetilde a_i/\widetilde a_8\in R.
\tag{917.13}
$$

实际构造先取单位 $d=ρ^{-a}\widetilde a_8$，再将已证明整的 numerator $ρ^{h(8-i)-a}\widetilde a_i$ 除以 $d$。因为负阶的全部可能系数已经由 (917.12) 覆盖，所有八个 $g_i$ 至少保有统一精度 $N-a$。无需先构造一个只有 $N-2a$ 精度的任意 Laurent 逆。

由原 generically separable 八阶关系得到

$$
O_0=R[Θ]\subset E=F[U]/(P).
\tag{917.14}
$$

保存原未首一的17列、$a,h$、单位 $d$、完整八个首一系数及其 source-bound 准确表达式。以 $1,Θ,…,Θ^7$ 作基，通过 (917.13) 直接归约全部64个乘积，保存完整512个结构系数和1。不得删去不约化因子或将特殊纤维根拆开后只保约化值。

## 4. 每步扩大只需至多八未知量的小核

设当前整 order $O$ 已保存完整乘法、1、相对原 primitive 基的 Laurent 多项式基变换 $B$ 和逆。按 R912，令

$$
J=\sqrt{ρO}, \qquad O'=(J:J), \qquad O\subset O'\subset ρ^{-1}O.
\tag{917.15}
$$

在当前剩余代数 $O/ρO$ 的完整8维基中，trace pairing 的核就是其 nilradical。设核维数为 $r$，取实际列矩阵 $C\in\operatorname{GL}_8(k)$，前 $r$ 列为这个核、后列为固定顺序补基。于是

$$
J=C\operatorname{diag}(I_r,ρI_{8-r})R^8.
\tag{917.16}
$$

对待定 $v\in O/ρO$，记在 $C$ 基中的乘法矩阵为 $M(v)$。条件 $vJ\subset ρJ$ 等价于下面四个块条件：

| 输出行 | 输入列 | 必须消失的 $ρ$ 系数 |
|---|---|---|
| $0\le k<r$ | $0\le j<r$ | 第0项 |
| $r\le k<8$ | $0\le j<r$ | 第0、1项 |
| $r\le k<8$ | $r\le j<8$ | 第0项 |
| $0\le k<r$ | $r\le j<8$ | 无额外条件 |

因此这是一个至多八未知量的 $k$-线性核，输入只用当前乘法表的第0、1阶。不同 lift 相差 $ρO$，而 $O$ 保持 $J$，故核条件不依赖 lift。实际保存全部方程行、行标签、pivot/free 列、完整核和乘回。

设此核维数为 $k_0$，把其原当前基坐标作为 $C'$ 的前 $k_0$ 列并补为可逆矩阵。新基变换为

$$
S=C'\operatorname{diag}(ρ^{-1}I_{k_0},I_{8-k_0}), \qquad
B'=BS.
\tag{917.17}
$$

保存 $B'$ 和准确 Laurent 多项式逆，完整核 $B'B'^{-1}=I$。这里所有系数均属于实际 $k$；不把它们自动提升成原 $K$ 的连接或 order 基。

### 4.1 不漏负阶的完整乘法验证

先用常数基变换 $C'$ 运输完整乘法张量。令 $e_i=1$ 表示第 $i$ 新列被除以 $ρ$，否则为0。其第 $(i,j;k)$ 结构系数再乘

$$
ρ^{e_k-e_i-e_j}.
\tag{917.18}
$$

最低可能新阶为 $-2$。消费者必须检查这些可能的全部负阶系数为零，再保完整新整乘法；这给实际整性，不只是模 $ρ$ 的闭合。当前表若有精度 $N_O$，统一保守精度取 $N_O-2$，不把正移位恢复的额外项混入统一证书。1 同时按 $S^{-1}$ 运输并核双侧单位。

每个已完成扩大阶段完整记录源表、两个小核、常数矩阵、$ρ$ 次数、所有精度损失及新表。中断后只读取已成扩大，不重复已接受的小核。

## 5. 正规停止是可核的 discriminant 4

用完整乘法先算每个基元的 trace，再算八阶 trace Gram 矩阵。其 determinant 使用无除法递推，避免为判阶作任意 series pivot 除法。若实际首个非零项在第 $d$ 阶，便准确知道当前 discriminant 阶 $d$。尚未出现非零项只能报 $d\ge N_O$ 并请求精度。

每次 (917.17) 扩大后

$$
d'=d-2k_0.
\tag{917.19}
$$

消费者同时核新表的实际 determinant 阶与这个恒等式，保常数 determinant 因子。若 $d>4$，R912 的 $J$-socle 论证保证 $k_0>0$。因此在精度充足时算法有限；最多发生 $(d_0-4)/2$ 次单维扩大。

**只有**完整整乘法、1、基变换逆、原关系及实际 $d=4$ 全部核过，才把该端点标为 normal-order complete。原因是任意当前整 order $O\subset B$ 满足

$$
v_ρ\operatorname{disc}(O)=v_ρ\operatorname{disc}(B)+2\operatorname{length}_R(B/O),
\tag{917.20}
$$

而原正规 order 的右首项由 (917.5) 为4。若精度或预算不足，保真实当前 order、discriminant 下界及所需新增项；不得称端点不存在。

完成时仍保存整个8维特殊纤维乘法。其 trace radical 的维数4、平方的维数2和立方为0可作为来源相容的实际验证；不据此删去任何幂零方向，也不以四个约化值替代原八维代数。

## 6. 原参数与 determinant 帧

相对原 $1,U,…,U^7$ 基，初始 $Θ$ 基的 determinant 是 $ρ^{28h}$。若全部扩大 index 长度之和为 $I$，各常数基变换 determinant 的积为 $u\in k^\times$，则最终正规基的 determinant 比为

$$
uρ^{m}, \qquad m=28h-I.
\tag{917.21}
$$

实际保存 $h,I,u,m$ 和完整 Laurent 基矩阵；不只保一个阶数。R883/R914 原参数给

$$
t=c_0ρ_0+O(ρ_0^2), \qquad
t-1=c_1ρ_1+O(ρ_1^2), \qquad c_1=-c_0.
\tag{917.22}
$$

因此 (917.21) 在原 $t-\epsilon$ 帧中的首系数为

$$
u c_\epsilon^{-m}.
\tag{917.23}
$$

一般一个已知有符号阶 $d$ 的 Laurent 标量，其 $t-\epsilon$ 首项同样是原 $ρ_\epsilon$ 首项乘 $c_\epsilon^{-d}$。这保留原负极阶对应的正 $c$ 幂，不能把几何反射的负号改成另一 CM 相位。

原微分按 [R860](../notes/R860-original-adjugate-semilinear-descent-and-rational-differential.md) 保留

$$
\nu=82τ\,dq_Y/q_Y, \qquad ι^*\nu=\nu.
\tag{917.24}
$$

本 scope 不计算新的 $g$、$Γ$ 或 $\nu/dρ$ 数值；其准确标记与原比例保持在 DAG，未计算的数值字段为 false。正规基的真实数值 determinant 也不等于任一目标九 Norm 的帧。

## 7. dual-seven 与后继目标格保持原定义

R873 的 canonical dual-seven 将原 $\operatorname{Nm}_q p^*$ 运输为本表示的 $\operatorname{Nm}_p q^*$。本 scope 只保存原同构、scalar7、diamond 和 $-3$ 的出处，以及新 order 基的形式 pullback；它同时作用于

$$
\det(p_*q^*M)\otimes\det(p_*\mathcal O)^{-1}
\tag{917.25}
$$

的两因子。没有已成 actual change-of-basis 就不填写其模矩阵，不把自伴随当作原刚性化比较。

对于 R907 将来的真实截面 $u_j=\Phi_ja_j,v_j=\Phi_jb_j$，R912 的后继完整标量仍是

$$
\operatorname{Nm}(q^*\Phi_j)\det U_j,
\tag{917.26}
$$

其中 $U_j$ 是 $q^*a_jB+q^*b_jB$ 的完整秩八格基。相对九截面坐标的公共因子相消不删除 (917.26)。本次没有 $U_j$、$\Phi_j$ 两端实际值或九目标 Norm；相应字段保持 false，R903/R907 来源并非完成 geometry order 的前提。

靶函数 $q^*z=U$ 在最终基中的准确 Laurent 坐标由 $B^{-1}$ 和 $ρ^{-h}Θ$ 直接定义；$q^*w$ 保 (917.10) 的原准确分式。后继若计算它，必须对原八维完整代数的乘法矩阵作有阶数的求逆，不能要求端点的 $P_U$ 是特殊纤维单位，也不能拿 R885 的 $z=0$ 目标行代替。

## 8. 最小真实来源与尚缺字段

| 组 | 本 scope 实际消费 | 不重做的原算术 |
|---|---|---|
| R873 | source-target DAG、原17列 accurate unit-solve 描述、成功证书及 metadata | 原八支 Norm、2058选行、V8尾 |
| R882 | 17列同地方坐标、same-place interface、source audit、成功 metadata | 原2058逆、全部2200行乘回 |
| R807 | 原 $θ$146坐标、$N_{692}$962坐标及 metadata | 原 M6 小核与 V4 成员解 |
| R883 | 已成前三项、原 $c_0$/$t$ 帧、成功 metadata | 旧前三项和 $c_0$ |
| R914 | 两个完整146叶 jets、完整反射及原点/参数来源、成功 metadata | 143新RHS、旧273正常 jets |

R873 的小 DAG 已内嵌需要的2050+8+非零 V4 recipes，因此不为本 scope 运输旧344MB载体、20MB逆或整个2050 Fourier族。R807 真原件可以由 R883 已保存的原 intake 包续存；纯运输route不改变 R807 原 producer 身份或数学 tag。所有选件逐原 manifest 的 bytes/SHA 核；路径只在 expanded config，不进入数学身份。

R914 已真实完成：run `43898224893`、job `133407590978`、source `1b397d402ac0d6ff5872f77c1409fba356ff77c6`；core SHA `c7dded45af13c7cd37b9c5261d917c2e81d3c179debe963296bbd8caf746e004`，configuration SHA `feb2b20f1e95bd9be878d47b2045b4da57352489c24c02f3ac1bce8ab0b2a432`。最终证书13921 B，SHA `8c2ce53f706174878076587879cff870abb3549783145156295f4601ae3bbdb0`；full manifest6251 B，SHA `fbc71afa26e27789c02814da7004db2b442bd2312441c22a3e9303d63e8b3f36`。完整146作用及560行准确乘回、两个叶矩阵和272正常函数273项均已真完成。

本 scope 的两件叶矩阵为 `R914-iota-original-P0-V1-jets.json.gz`（205777 B，`b0d5137d3ddeb3df57570782b308729583f7c052d905f6b3113de968a39c9c44`）和 `R914-iota-P1-V1-jets.json.gz`（205866 B，`055ffec11eedc141e49f0a023eb13b63b7a18e6ba36db20e2d2d95bd03b9dcf7`）。原参数帧 stage4816 B，SHA `75f5ae4757ad0acbd00a5d8243818aa434eb0846dcb323b49c665c07498d8c45`，实际 $c_1=645187085$；它保持准确 $c_1=-c_0$ 来源，不扩称273项 $t$ 尾已成。

真实 artifact14241065505 为6647816 B，ZIP SHA `94eba2eaa86ad7ee48796b6d93d7df39b637b260683d08970488150848f91bee`，到期 `2026-11-17T15:37:49Z`。结束纯 IO 已核完整 ZIP、全部37个 manifest 输出及469原载体成员；不重任何数学。R917 可填这个实际来源，但新的 discriminant、扩大次数、order 基及端点结构常数仍全部由后续 Actions 实际产生。R903/R907 等未消费未来源保持 null。

## 9. 原子输出及可恢复边界

新数学输出统一为 `R917-endpoint-*.json.gz`，均有独立 result、真实新 core SHA、helper SHA、proof/method 和全部原 source identity。来源 producer 的字节及 tag 原样保留，不能覆写为新 stage。

顺序为：source audit；两个端点的原叶/recipe 分块；17个共同清分母 jets；primitive order；每次 trace-kernel、idealizer-kernel、扩大基和新完整表；normal-order certificate；特殊纤维及原参数 determinant 帧。所有完成项原子写入；current 单列 `complete=false`；stage manifest 只列当前实际完成的数学阶段。真正已成 source 不因首请求不同预算而重算。

最终两端各有独立布尔：`common_cleared17_jets_computed`、`normal_order_certified`、`full_length8_special_fibre_preserved`、`primitive_and_original_t_determinant_frames_computed`。只有两端全部目标真完成才 `complete=true`。NeedPrecision 保端点、当前阶/精度、缺失系数、最后完成 stage；budget 保实际 current，不用一个 false FINAL 的历史 SHA 约束更晚断点。

始终另外列明：特征零 order 基未展开、靶272坐标未完成、五个 $J_j$ 格未完成、两端九目标 Norm 数值未完成、$\operatorname{Nm}(q^*\Phi_j)\det U_j$ 原帧数值未完成、Hecke/Picard 活跃支持及高度未完成。完成 geometry order 不改变这些边界。

本篇所有新的多项式乘法、八阶 determinant、小核、order 基变换和帧求值只在原公开仓库 Actions 执行；本地仅源码、AST、源字节/JSON/hash 处理。
