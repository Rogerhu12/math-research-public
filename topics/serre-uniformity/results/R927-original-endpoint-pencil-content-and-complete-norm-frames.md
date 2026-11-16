# R927：原两端铅笔理想的范数本原部分与完整范数帧

日期：2026-11-16。状态：本文给出新的有限算法、精度证明和实际来源合同，尚未执行本篇的新端点算术。原 R917 两端正规阶已经完成；R923 的目标正常坐标正在公开运行，实际来源仍须其完成证书。五个 R903/R907 铅笔在本篇首消费者中保持 null。

本文接 [R912](R912-original-eight-dimensional-endpoint-lattices-and-norm-frames.md)，不重新登记其中的九范数存在性或两端共同整数参数引理。新增步骤是：先从一个八次范数多项式直接得到整个局部理想的生成元；把完整 $\operatorname{Nm}\Phi$ 的首项计算移到每个真实函数叶的范数上；并用已成参考函数的准确单极与原配对关系，避免为一个254阶极点展开数百阶新的目标尾。

首执行范围只做原参考 $M_0$ 的两个端点。未来五目标的算法和输出字段在同一合同中明确保留，不把来源未完成解释为已经得到了其标定。

## 1. 原来源和固定约定

沿 [R873](R873-original-cyclic-seven-correspondence-from-short-section-norms.md)、[R876](R876-original-nine-norm-generators-and-rigidified-Hecke-ideals.md) 固定

$$
p=\pi_s,\qquad q=\pi_t,\qquad \deg p=\deg q=8.
\tag{927.1}
$$

直接计算方向为 $\operatorname{Nm}_p q^*$；原冻结 Hecke 方向 $\operatorname{Nm}_q p^*$ 仍通过原 canonical dual-seven 同构，同时运输 determinant 的分子、分母与两端帧。原 scalar $7I$、diamond、$-3$ 下降、$\nu$ 及其既有运输节点全部保留。

设 $k$ 为原特征零系数域，或实际原辅助域
$\mathbf F_\ell$，其中

$$
\ell=1000000753,\qquad
\zeta=549966761,\qquad s=99932770.
\tag{927.2}
$$

一般陈述另要求 $\operatorname{char}k=0$ 或 $\operatorname{char}k>16$，并满足原好约化条件。下文的17个整数不能在较小特征中被当作17个不同元素。

对 $\epsilon=0,1$，使用原

$$
R_\epsilon=k[[\rho_\epsilon]],\quad
F_\epsilon=k((\rho_\epsilon)),\quad
E_\epsilon=k(C_7)\otimes_{k(Y)}F_\epsilon,\quad
B_\epsilon=\overline{R_\epsilon}^{\,E_\epsilon}.
\tag{927.3}
$$

[R914 实际结果](R914-certified-original-full-V1-involution-and-P1-jets.md) 给完整146维几何反射及原参数
$\rho_0=z-z(P_0)$、$\rho_1=\iota^*\rho_0$。
[R917 实际结果](R917-certified-original-two-endpoint-normal-orders-and-frames.md) 给完整秩八正规 $B_\epsilon$，保持几何类型 $2+3+3$、全部剩余域和幂零。其实际可靠精度为271，不能解释为未来所有商都有271项。

[R923](R923-original-target-normal-coordinates-in-certified-endpoint-orders.md) 证明目标 $\tau$ 图适用，故原正常函数 $q^*z,q^*\beta_i$ 都整于 $B_\epsilon$。其执行以真正共同分母阶 $d_\epsilon$ 决定输出精度；本篇不预填 $d_\epsilon$ 或其完成值。

令原 $t_\epsilon=t-\epsilon$。原框架给

$$
t_\epsilon=c_\epsilon\rho_\epsilon+O(\rho_\epsilon^2),\qquad
c_1=-c_0,\qquad
c_0=354813668\pmod\ell.
\tag{927.4}
$$

这个模值与准确的 R883/R914 来源表达式一并保存，不重新归一为1。

## 2. 八次范数多项式的本原部分就是整个理想的指数

以下固定一个端点并略去 $\epsilon$。在已成 $B$ 基中，$M_a$ 表示乘以 $a$ 的矩阵，列为坐标。取 $a,b\in B$，且 $aB+bB$ 在 $E$ 的每个因子非零。定义

$$
D_{a,b}(T)=\det(M_a+TM_b)
          =N_{E/F}(a+Tb)\in R[T],\qquad \deg_TD_{a,b}\le8,
\tag{927.5}
$$

$$
\mu=\min_{0\le i\le8}v_\rho([T^i]D_{a,b}),\qquad
d_{a,b}(T)=\rho^{-\mu}D_{a,b}(T)\bmod\rho\ne0.
\tag{927.6}
$$

这里的最小值只取非零系数。实际截断内全部为零时，$\mu$ 尚未确定。

**引理 927.1。** 设 $B=\prod_\alpha B_\alpha$ 为完整正规半局部环，$v_\alpha$ 是各 DVR 的整数值赋值，$f_\alpha$ 为其剩余次数，且
$m_\alpha=\min(v_\alpha(a),v_\alpha(b))$。则

$$
\boxed{\quad
\mu=\sum_\alpha f_\alpha m_\alpha
=\operatorname{length}_R B/(aB+bB).\quad}
\tag{927.7}
$$

**证明。** 将 $T$ 当作 Gauss 变量，剩余变量在 $k(T)$ 中超越。各分支上
$a+Tb$ 的阶正是 $m_\alpha$：当两项阶相等时，超越的 $T$ 不会产生首项相消。行列式范数的赋值为 $\sum f_\alpha m_\alpha$。另一方面，$aB_\alpha+bB_\alpha$ 是 $B_\alpha$ 的 $m_\alpha$ 次极大理想幂，其 $R$ 长度为 $f_\alpha m_\alpha$。两者相等。

式 (927.7) 的赋值和中不再额外乘分歧指数。分歧并未丢失：若仅为证明而在各分支选均匀元，$d_{a,b}(T)$ 是一个非零常数乘以各剩余线性式之剩余域范数的 $e_\alpha$ 次幂。因此其次数按 $e_\alpha f_\alpha$ 计入，两个长度三部分完整保留。实际算法不拆这些分支，也不计算这个因式分解。证毕。

**推论 927.2。** 若 $d_{a,b}(\lambda)\ne0$，则

$$
g=a+\lambda b,\qquad
\boxed{\,aB+bB=gB\,}.
\tag{927.8}
$$

因为每个 $v_\alpha(g)\ge m_\alpha$，而其加权和已经等于 (927.7)，所有分支上都取到等号。这里不要求 $g$ 在 $B/\rho B$ 为单位；它可以生成有很大指数的完整理想。

对同一原 $a,b$ 的两个端点，两个非零 $d$ 各至多有8个根。因此从原整数 $0,\ldots,16$ 依次取值，必能选一个两端均满足 (927.8) 的 $\lambda$。本篇每个目标及参考各选自己的共同参数，不声称同一个参数同时适用于全部六个铅笔。

## 3. 不先求 Smith：一个共享分母给全八乘十六的双向证书

取 (927.8) 的生成元，不再除掉其首项常数。令

$$
U=M_g,\qquad
C_a=M_g^{-1}M_a,\qquad C_b=M_g^{-1}M_b.
\tag{927.9}
$$

则 $C_a,C_b\in M_8(R)$，且

$$
M_gC_a=M_a,\qquad M_gC_b=M_b,\qquad
\boxed{\,C_a+\lambda C_b=I_8\,}.
\tag{927.10}
$$

前两式给原16列进入 $gB$；最后一式给反向包含。准确格基就是原 $B$ 基逐列正乘 $g$，无需先做 $8\times16$ 的 Laurent Smith/Hermite 消元。原基列身份、全部16列的表达和反向式均保存，不把一个非零8阶子式当作整个理想等式。

设原乘法及 $a,b$ 已知到绝对精度 $N$，且 $\mu<N$。写

$$
\Delta=\det M_g=\rho^\mu u_\lambda,\qquad u_\lambda\in R^\times.
$$

只求一次 $\operatorname{adj}(M_g)$，则

$$
C_a=u_\lambda^{-1}\rho^{-\mu}\operatorname{adj}(M_g)M_a,\qquad
C_b=u_\lambda^{-1}\rho^{-\mu}\operatorname{adj}(M_g)M_b.
\tag{927.11}
$$

由已证明的整性，两分子的每个坐标都能整除 $\rho^\mu$。实现须完整核其前 $\mu$ 项为零，随后只逆单位 $u_\lambda$。两矩阵都至少可靠到

$$
\boxed{\,N-\mu\,}.
\tag{927.12}
$$

完整 (927.10) 在该精度逐坐标乘回。不能把先算 Laurent 逆损失的 $2\mu$ 再不必要地施加给已经证明为整的商。

若某个应整除的低阶坐标非零，这是来源/相容性失败。若 $\Delta$ 在已有范围内没有非零项，则记录实际下界和需要的对象，返回 NeedPrecision，不把它当成零理想。

相对于未缩放基 $gB$，原九个范数截面的纤维坐标为

$$
\det(\overline C_a+i\overline C_b)
=\frac{d_{a,b}(i)}{d_{a,b}(\lambda)},\qquad i=0,\ldots,8.
\tag{927.13}
$$

$\lambda$ 可以大于8，但它只选一个两端共同局部帧；原九个全局生成元不变。式 (927.13) 的零是该截面的纤维坐标零，不是全局函数零、Picard 类零或 inactive 判据。

## 4. 完整 Norm Phi 的首项可逐真实叶累积

[R907 执行方法](../notes/R907-original-Iz-pencil-and-nine-Hecke-norms-method.md) 的已冻结 function program，在真正 normal-section 叶之后只有 constant-one、乘法和整数幂。加法均已留在每个原正常截面的坐标中，不在下面被当作乘法处理。

对非零 $x\in F$，定义

$$
\mathcal L_\rho(x)=
\left(v_\rho x,\ [\rho^0](\rho^{-v_\rho x}x)\right)
\in\mathbf Z\times k^\times.
\tag{927.14}
$$

这是乘法群同态，群律为 $(m,c)(n,d)=(m+n,cd)$。于是对每个原函数叶 $h$，先在全部 $B$ 中评价 $q^*h$，求

$$
n_h=\det M_{q^*h}=N_{E/F}(q^*h),
\tag{927.15}
$$

并确定它的实际非零首项。其后沿原程序的乘法/整数幂节点，在 $\mathbf Z\times k^\times$ 中计算

$$
\mathcal L_\rho N(q^*\Phi_j).
\tag{927.16}
$$

范数的乘法性保证 (927.16) 与先完整评价 $\Phi_j$ 再取范数完全一致。它不是把 $\Phi_j$ 删除，也不是以相对九坐标代替它。

若某个原叶被重复引用，可按完整 source identity、原字段、原正常基位置及原字节 SHA 合并相同叶的整数指数，并保原完整 DAG 与合并映射。不能因两个模数组偶然相等而合并不同准确函数。所有非零指数所需的叶范数首项必须真的确定；未确定的零截断不进入乘法群。

这个改写有一个实际精度收益：最终主函数中的巨大正负整数幂只作用于已确定的 $(m,c)$，不会迫使八维 Laurent 级数反复损失精度。需要的输入精度由各原叶的真实首项决定，而非由展开全部大幂后的极阶决定。若某个叶的范数在现有精度内仍全零，只为该叶返回 NeedPrecision。

未来五目标中 $a_j,b_j$ 是原未缩放 normal $V_3$，而完整截面是 $\Phi_j a_j,\Phi_j b_j$。因此本篇的理想步骤消费 (927.5)；完整帧步骤还必须消费 (927.16)，两者分开保存后再按第8节正乘。

## 5. 参考已有三条函数，不必在端点直接逆高阶 u

[R879](R879-original-reference-pole254-pencil-from-completed-syzygies.md) 的真实 function-and-pencil 输出已经保存原正常 $V_2$ 的 $f,g,u$，并引用原 R872 的 $b$。准确关系为

$$
ug+bf=0,\qquad
v_0=\frac fu=-\frac gb,\qquad
(u,b)=I_{272P_0}\quad\hbox{在原 }\tau\hbox{ 图上}.
\tag{927.17}
$$

最后一个等式按原 $2H$ 框架归一化；它来自已认证的共同零除子，不能只从模配对式猜出。

原 $P_0$ 参数与首项为

$$
u=U_{272}\rho_0^{272}(1+O(\rho_0)),\qquad
f=\rho_0^{18}(1+O(\rho_0)),\qquad U_{272}\ne0,
\tag{927.18}
$$

$$
v_0=U_{272}^{-1}\rho_0^{-254}(1+O(\rho_0)).
\tag{927.19}
$$

原输出真实字段包括 numerator_normal_polynomial_mod_prime、
paired_normal_polynomial_mod_prime、denominator_normal_polynomial_mod_prime、
numerator_first19_local_coefficients_mod_prime 和
denominator_order272_unit_mod_prime。
三个数组已除原 $\tau^2$，不再施加权尺度或新的 $\tau$ 因子。

单纯对 $u$ 作八维行列式，可能因 (927.18) 需要超出 R923 现有范围的项。下面使用准确已成的消失阶和整个 target-$P_0$ 主分量，避开这个人为的大尾需求。

## 6. 只分出目标 P0 的整个主分量，不删除任何因子或幂零

令 $A=B/\rho B$。把原目标 $P_0$ 的最大理想沿真正 $q$ 拉回，得到 $A$ 中的理想 $I$。可使用原正常环的全部生成元减其原 $P_0$ 值；源点值来自既成 R914/R872，不用某个几何根替代它们。

令 $A_*$ 为支撑映到目标 $P_0$ 的所有局部因子的直积，$A_c$ 为全部其余因子的直积。在 $A_*$ 上，$I$ 含于 Jacobson radical，其八次幂为零；在 $A_c$ 的每个局部因子上，某个原目标最大理想生成元为单位，故 $I$ 是全环。因此

$$
I^8=0\times A_c,\qquad
\operatorname{Ann}_A(I^8)=A_*\times0.
\tag{927.20}
$$

这给一个最多八维的线性代数算法：保存真实 $I,I^2,\ldots,I^8$ 的完整列空间、乘法来源及 annihilator，求它的单位幂等元 $\bar e$。必须核

$$
\bar e^2=\bar e,\quad \bar e I^8=0,\quad
(1-\bar e)I^8=I^8,\quad
A=\bar e A\oplus(1-\bar e)A.
\tag{927.21}
$$

所有块都保留。长度三因子的幂零仍位于其完整块中；(927.20) 不是把 $A$ 换成约化商。

$\bar e$ 唯一提升为 $B$ 的幂等元。有限精度可从任一 lift 用
$e\mapsto3e^2-2e^3$ 迭代，每次将误差阶至少加倍。只使用原乘法，不逆不明单位。得到

$$
B=B_*\times B_c,\qquad r=\operatorname{rank}_R B_*,\qquad
r+\operatorname{rank}_R B_c=8.
\tag{927.22}
$$

如需坐标，分别选 $eB,(1-e)B$ 的模参数独立原列，组成完整8阶单位换基；保存两侧逆及全部乘回。任何块的范数是该完整自由块的 determinant，不是其闭点值的乘积。$r$ 的实际数值不预填。

### 6.1 目标 P0 块只需一个低阶范数

在 $B_*$ 中置

$$
r_0=q^*\rho_0=q^*(z-z(P_0)),\qquad
\mathcal L_\rho N_{B_*/R}(r_0)=(m,c).
\tag{927.23}
$$

若 $r=0$，约定空块范数为1，$(m,c)=(0,1)$。否则 $m>0$。原 $\rho_0$ 在目标 $P_0$ 是准确均匀参数，故

$$
m=\sum_{\substack{Q\mid p^{-1}(P_\epsilon)\\q(Q)=P_0}}
[k(Q):k]\,e_q(Q)
\le \deg q=8.
\tag{927.24}
$$

因此，只要该块的原目标坐标和乘法具有9项可靠精度，(927.23) 的首项必已显露。这是有限映射次数界，不假定哪两个固定支落在 $P_0$，也不假定某个长度三轨道的目标标签。

由准确 (927.19)，对 $\lambda\ne0$，

$$
\boxed{\quad
\mathcal L_\rho N_{B_*/R}(1+\lambda q^*v_0)
=\left(-254m,\ \lambda^r U_{272}^{-r}c^{-254}\right).\quad}
\tag{927.25}
$$

每个分支上 $1/v_0$ 有正阶，因此 $1+\lambda v_0$ 的首项由 $\lambda v_0$ 决定；其余单位的范数首项为1。这里保留了原 $U_{272}$，没有把参考框架归一为1。

虽最终极阶可很大，(927.25) 只使用旧 $U_{272}$ 和至多9项的新低阶范数，不需要新的254或272阶目标尾。

### 6.2 补块使用原配对关系，只除完整单位

在 $B_c$ 上，所有目标都不等于 $P_0$，故由 (927.17)

$$
uB_c+bB_c=B_c.
\tag{927.26}
$$

在模参数的完整 $B_c$ 上，$\det(M_u+\eta M_b)$ 是非零的次数至多 $8-r$ 多项式。取 $\eta=0,\ldots,8$ 中首个实际单位值，保存 determinant、完整逆和乘回。由 (927.17) 准确得到

$$
\boxed{\quad q^*v_0=(f-\eta g)/(u+\eta b)\quad\text{在 }B_c.\quad}
\tag{927.27}
$$

分母在整个补块是单位；不会因 $u$ 在个别分支为零而错误地停止，也不把所有分支都强迫使用同一个坏表示。不同端点可以选不同 $\eta$，因为它们按同一个准确关系表示原同一函数 $v_0$。

这个商无参数精度损失。必须完整核
$(u+\eta b)v_0=f-\eta g$；并在现有精度核原 $ug+bf=0$。取

$$
C_\epsilon(T)=\det(I+T M_{v_0|B_c})\bmod\rho,\qquad C_\epsilon(0)=1.
\tag{927.28}
$$

设

$$
d_\epsilon^{\rm ref}(T)=T^{r_\epsilon}C_\epsilon(T).
\tag{927.29}
$$

它是非零、次数至多8的多项式。选 $\lambda_0\in\{0,\ldots,16\}$，使两个端点的 (927.29) 都非零。若任一端有 $r_\epsilon>0$，此选择自动排除 $\lambda_0=0$；若两端 $r=0$，$\lambda_0=0$ 可合法给局部参考帧1。

由 (927.25)–(927.28)，原同一全局函数
$G_0=N(1+\lambda_0q^*v_0)$ 的完整两端首项为

$$
\boxed{\quad
\mathcal L_{\rho_\epsilon}G_0
=\left(-254m_\epsilon,\
 \lambda_0^{r_\epsilon}U_{272}^{-r_\epsilon}
 (c_\epsilon^*)^{-254}C_\epsilon(\lambda_0)\right).
\quad}
\tag{927.30}
$$

这里 $c_\epsilon^*$ 是 (927.23) 的范数首项，区别于原 $t/\rho$ 的 $c_\epsilon$。
空 $P_0$ 块约定 $\lambda_0^0=1$，包括 $\lambda_0=0$。

相对于生成元 $1+\lambda_0 v_0$，若 $B_*$ 非空，两矩阵在该块模参数上为 $0$ 与 $\lambda_0^{-1}I_r$；空块不作逆运算。在 $B_c$ 上为
$(I+\lambda_0 M_{v_0})^{-1}$ 与其正乘 $M_{v_0}$。前一断言保整个幂零块：$1/v_0$ 在每个 DVR 的阶至少254，而原 $p$ 分歧指数至多3，因此 $1/v_0\in\rho^{84}B_*$，并非仅在约化点消失。组合回原八维基后，完整两矩阵模参数满足

$$
C_{0,0}+\lambda_0 C_{0,1}=I_8.
\tag{927.31}
$$

它们给全部九个参考相对坐标。首 scope 保存这个完整8维余矩阵、准确的分式理想生成元表达式和实际 determinant 首项；不把尚未展开的整段 Laurent 格基称为已经展开。

## 7. 原参考本身的完整 determinant 帧没有被相消掉

另用直接的积分对 $(u,f)$，令 $g_0=u+\lambda_0f$。原分式理想为

$$
B+v_0B=(g_0/u)B,\qquad
\det U_0=\frac{N(g_0)}{N(u)}
=N(1+\lambda_0v_0).
\tag{927.32}
$$

第6节仅用原关系与旧准确单极来计算这个同一个商的首项，没有将分子和分母的原标量丢弃。实现同时保存 (927.32) 的完整来源 DAG 和 (927.30) 的实际值；不能只输出相对九坐标。

将 (927.30) 的整数阶记作 $m_0$、单位首项记作 $g_0^\rho$，则原 $t_\epsilon$ 帧中的单位是

$$
g_0^t=c_\epsilon^{-m_0}g_0^\rho.
\tag{927.33}
$$

特别是 $m_0=-254m_\epsilon$ 时，原 $t/\rho$ 单位以正幂 $254m_\epsilon$ 出现。两端使用各自的 $c_\epsilon$，保 $c_1=-c_0$，不将 $\rho_1$ 换成另一个表面参数。

## 8. 未来五目标的完整帧正乘方向

当真正 R907 铅笔及完整 $\Phi_j$ 程序到达后，在两个端点分别执行第2–4节。令

$$
g_j=a_j+\lambda_jb_j,\qquad
\mathcal L_\rho N(q^*\Phi_j)=(m_\Phi,c_\Phi).
$$

由 (927.6) 和 (927.8)，
$\mathcal L_\rho N(g_j)=(\mu_j,d_j(\lambda_j))$。
原完整范数商的同一全局生成函数为

$$
\boxed{\quad
G_j=\frac{N(q^*\Phi_j)\,N(g_j)}
           {N(1+\lambda_0q^*v_0)}
=N(q^*\Phi_j)\frac{N(g_j)N(u)}{N(u+\lambda_0f)}.
\quad}
\tag{927.34}
$$

因此

$$
\mathcal L_\rho G_j
=\left(m_\Phi+\mu_j-m_0,\
       c_\Phi d_j(\lambda_j)/(g_0^\rho)\right).
\tag{927.35}
$$

这正是 R912 的 $\operatorname{Nm}(q^*\Phi_j)\det U_j/\det U_0$，其中 $U_j=M_{g_j}$。$\Phi_j$ 和 $N(u)$ 均为正乘；参考 $N(u+\lambda_0f)$ 为除数。没有新的排列符号，也没有另插一个 $\tau$。

若 (927.35) 为 $(m_j,g_j^\rho)$，原帧单位为
$c_\epsilon^{-m_j}g_j^\rho$；两端比值仍按 R912 的同一全局函数与原 dual7 同构运输。
本篇不将这个单位比值直接命名为指定 theta/Poincaré period，不省任何非 $p$ 项或 theta 二挠。

## 9. 精度和特征零边界

所有数组注明绝对 $\rho_\epsilon$ 精度、原阶/原基和当前剩余地方。有限域的全部已知系数是准确有限域数，但不是展开的特征零代数数。

- 通用铅笔部分须实际看见 $\mu$，两矩阵可靠精度为 $N-\mu$；至少一项才可输出相对纤维坐标。
- 每个真实 $\Phi$ 叶须看见其范数非零首项；整数幂只在首项群中作用，不触发额外 Laurent 精度损失。
- 参考的 $P_0$ 块只需实际的 $(m,c^*)$。准确次数界为 $m\le8$；具有9项输入时已足。若实际已有较少项但已看见首项，亦可接受。
- 参考补块只除实际完整单位，保全部原乘回；原 $U_{272}$、源单极阶、旧 $t/\rho$ 来源必须同时通过。
- 本篇不给未知 $\mu,r,m,\lambda,\eta$ 预填数值。不足则按真实对象和真实下界保存 NeedPrecision，另一端仍可继续。

(927.7)–(927.35) 是在指定系数域中的准确恒等式与算法。实际首运行若在 $\mathbf F_\ell$ 执行，其新增数值旗标只声称该合法剩余处的完整局部理想、相对坐标或帧值。准确特征零的原函数、line bundle、unit-solve 和 determinant DAG 另字段原样保存。

尤其不能仅因某些低阶系数模 $\ell$ 为零，就声称它们在特征零为零或声称两者有同一实际赋值。若后继要提升一个新观测的 content 阶或局部生成元性质，须给相应的准确整除/局部除子下界，或原完整模型中的饱和与非零约化证明。第6节对参考所用的272、18、254阶是已有准确来源，不属于这种模零猜测。对未来一般目标，无此来源时不得把观察到的模阶改成准确特征零阶。

所有 Picard inactive、主类、真实 descent 立方、Poincaré 高度或全 $p$ 非消失旗标仍为 false。

## 10. 首 reference consumer 的最小来源与原子输出

### 10.1 已成/待成的分界

首 scope 只需要：

1. 真 R923 两端目标正常坐标、其完整272关系证书、实际精度和源 R917 正规阶/参数引用；未成功时 source 为 null。
2. 真 R917 两端完整 order、原帧及其原输入包中 R914 的原 $P_0$ 正常点值/生成元值。R917 原乘法和旧正规化绝不重算。
3. 真 R879 function-and-pencil、准确 unit-solve 定义、完整原参考证书及 source audit；这一个小文件已有 $f,g,u,U_{272}$。
4. 其原 source_anchor_b 指向的 R872 已成7193字节小叶，以及原共同零/配对身份的已成证书引用。只新取这个原文件，不为旧 guard 重取大418核。
5. R917 已续存的 R873 原 correspondence DAG 与 rigidified_Hecke_transport；R883/R914 原 $c_0,c_1$ 帧引用。

源运输只核真实 manifest、bytes/SHA、原 producer 身份与原子文件标签。载体续传不得把 R879/R872 旧数学 stage 改标为新 R927 stage。
本 scope 不依赖 R903/R907 的完成值；五方向来源字段保持 null。

### 10.2 必须保存的实际阶段

- source audit：准确输入闭包、当前地方、两个实际精度、原参考/相位/帧身份。
- 每端完整 target-$P_0$ 理想幂、annihilator、幂等元、完整块换基和两侧乘回；实际 $r$。
- 新 $f,g,u,b$ 端点评价及准确源绑定，不重新求任何旧系数。
- $P_0$ 块 $N(q^*\rho_0)$ 的完整可见前缀、实际阶/首项及 $m\le8$ 约束。
- 补块实际单位表示参数 $\eta$、完整单位逆、原配对/商乘回与 (927.28)。
- 两端共同参考 $\lambda_0$、全部九个参考相对坐标、完整8维两余矩阵和 (927.31)。
- 原参考 determinant 帧的 $\rho$ 阶/首项、原 $t$ 单位和两个端点的实际比值；完整 (927.32) 原 DAG。
- 分别标明实际有限域完成、特征零准确定义已保存、特征零系数/整个 Laurent 格未展开、五目标未完成。

所有 stage 原子保存并用新源码/证明/输入指纹标识。硬断只复用同 tag 已完成阶段；NeedPrecision 完成到哪个对象就保留哪个对象，不伪造终点。全部新数学只在公开 Actions 执行。

未来 target scope 在上述真参考阶段上再接 R907 的五个 source_original_a/source_original_b、真672证书、compiled-original-marked-function-program 与其所有原 normal-section 叶。它新增第2–4、8节的实际数值；没有这些来源时不得激活五方向或把表达式当成数值完成。
