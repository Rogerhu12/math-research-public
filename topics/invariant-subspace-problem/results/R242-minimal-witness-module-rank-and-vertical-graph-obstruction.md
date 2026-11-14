# R242：最小见证的交换子模秩、垂直商图与共同正则器

日期：2026-11-13（UTC+8）。作者：normal_states。
恢复说明：原稿已于本轮执行环境丢失前完成；本稿按同一证明恢复，补明共同图与各分量最大图的区别。

状态：以下模秩加强、垂直部分处理及正则器充分条件均完整。它们准确指出最小有限秩见证必须具有的无界图障碍；尚未证明这种障碍在实际慢符号下不存在。没有从所有行像的普通闭包相等直接推出图范数稠密。

## 1. 固定设置

沿用实际 Haar 空间上的 $A$，记
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},
\qquad \mathfrak C=\{A\}'=\overline{\mathbb C[I,A]}^{\mathrm{SOT}}.
$$
R88 给 $\mathfrak C$ 交换，且每个 $C\in\mathfrak C$ 都有一致有界的多项式序列强逼近。因此每个闭 $A^{(r)}$ 不变子空间也被 $\mathfrak C^{(r)}$ 保持。

固定 $S\in\mathcal A$，并假设 $S$ 在全 $H$ 稠密像。目标是 $S_N$ 或 $S_Y$；不将有限头压缩当作代数同态。

假设 $\mathcal J=S\mathcal A$ 存在有限秩分离泛函。R228 的商轨道附录证明：一般有限秩分离泛函与正有限秩分离泛函具有同一个最小秩 $d$。取最小秩正见证
$$
\rho=\sum_{i=1}^d f_i\otimes f_i,\quad
\operatorname{Tr}\rho=1,\quad x=(f_1,\ldots,f_d),
$$
并置
$$
M=\overline{\mathcal A^{(d)}x},\qquad
N=\overline{S^{(d)}M},\qquad Q=M\ominus N.
\tag{1.1}
$$
则 $x\in Q$，$Q\ne0$。以下讨论 $d>1$；$d=1$ 的缺口已经是原 $H$ 内不变限制的慢符号稠密像。

## 2. 低秩限制加强为有界交换子模秩

**命题 2.1。** 若 $r<d$、$\Gamma\in M_{d\times r}(\mathfrak C)$、$u\in H^{(r)}$，并且 $m=\Gamma u\in M$，则 $m\in N$。

**证明。** 若 $q=P_Qm\ne0$，则
$$
\psi(F)=\langle F^{(d)}m,q\rangle
=\langle F^{(r)}u,\Gamma^*q\rangle
\tag{2.1}
$$
满足 $\psi(SF)=0$、$\psi(I)=\|q\|^2>0$。第二式来自交换性，且至多含 $r<d$ 个向量配对，违反一般有限秩见证的最小秩。故 $q=0$。证毕。

常系数矩阵给旧的低 Schmidt 秩限制；本命题允许完整有界交换子。特别，若 $m_i=C_i g$、$C_i\in\mathfrak C$ 且 $m=(m_i)\in M$，则 $m\in N$，无需 $g$ 循环。若 $m=x$，便排除 $d>1$；排除剩余秩一见证仍需额外输入，例如共同源的循环性与 $S$ 全空间稠密像。

**坐标不变性。** 对任意 $U\in GL_d(\mathfrak C)$，$M'=UM$、$N'=UN$ 闭且不变，并满足 $N'=\overline{S^{(d)}M'}$。若 $m'=\Gamma u\in M'$、$\Gamma$ 宽度小于 $d$，对 $U^{-1}\Gamma u$ 应用命题即得 $m'\in N'$。没有把 $U$ 假设为酉，也没有声称 $U\rho U^*$ 保持原正湮灭条件。

## 3. 所有更小宽度的交换子矩阵像都看不到该商

**命题 3.1。** 对任意 $1\le r<d$ 和 $R\in M_{r\times d}(\mathfrak C)$，
$$
\boxed{\overline{RN}=\overline{RM}.}
\tag{3.1}
$$

**证明。** 令 $L=\overline{RM}\subset H^{(r)}$。它闭且 $A^{(r)}$ 不变，交换性给
$$\overline{RN}=\overline{S^{(r)}L}.$$
若右侧真小于 $L$，取 $0\ne z\in L\ominus\overline{S^{(r)}L}$，则
$$F\longmapsto\sum_{i=1}^r\langle Fz_i,z_i\rangle$$
是秩至多 $r<d$ 的非零正分离泛函，矛盾。证毕。

对 $M',N'$ 也成立：将 $R$ 换为 $RU$ 即可。所有坐标投影、常系数行及宽度 $d-1$ 的交换子矩阵都涵盖在内。但 (3.1) 仍是目标 Hilbert 空间中的通常范数闭包，不保证 $RN=RM$，也不给逆图的有界性。

## 4. 准确除去垂直部分；剩余图必无界且非全域

固定分解 $H^{(d)}=H^{(d-1)}\oplus H$，记 $P$ 为前 $d-1$ 坐标投影。定义
$$
V_0=\{v\in H:(0,v)\in M\},\qquad
V=0\oplus V_0,\qquad L=\overline{PM}.
\tag{4.1}
$$
$V_0$ 闭且 $A$ 不变。每个 $(0,v)$ 由宽度1的常系数列生成，故命题2.1给 $V\subset N$。

令 $K=H\ominus V_0$。对 $u\in D:=PM$，取 $(u,w)\in M$ 并定义 $Tu=P_Kw$。选择无关，因为两种 $w$ 之差在 $V_0$。又 $(0,P_{V_0}w)\in V\subset M$，故 $(u,Tu)\in M$。于是
$$
\boxed{M=\mathcal G(T)\oplus V}
\tag{4.2}
$$
为 Hilbert 正交直和，$T:D\subset L\to K$ 单值且稠密定义。

若 $u_n\to u$、$Tu_n\to w$，则 $(u,w)$ 是闭空间 $M$ 中向量的极限，所以 $u\in D$、$Tu=w$；故 $T$ 闭。这里不把闭子空间的坐标像预设为闭。

不假设 $K$ 对 $A$ 不变。正确作用是商压缩
$$\widehat F=P_KF|_K\quad(F\in\mathfrak C),$$
因为 $V_0$ 对 $F$ 不变。直接将 $F^{(d)}(u,Tu)$ 的垂直部分除去，得到真实域等式
$$
F^{(d-1)}D\subset D,\qquad
TF^{(d-1)}u=\widehat FTu.
\tag{4.3}
$$
因此 $S$ 在图范数 $\|u\|_T^2=\|u\|^2+\|Tu\|^2$ 下有界，范数至多 $\|S\|$。

由于 $V\subset N$，若 $D_N=PN$，则
$$
N=\mathcal G(T|_{D_N})\oplus V.
\tag{4.4}
$$
$D_N$ 图范数闭且真小于 $D$；由 (3.1) 的坐标矩阵得 $\overline{D_N}^{\|\cdot\|}=L$。将 $N=\overline{S^{(d)}M}$ 通过商映射 $M\to M/V\simeq\mathcal G(T)$，则
$$
\boxed{
D_N=\overline{S^{(d-1)}D}^{\|\cdot\|_T}
\varsubsetneqq D,\qquad
\overline{D_N}^{\|\cdot\|}=L.
}
\tag{4.5}
$$
这里 $V\subset N$ 保证 $N/V$ 闭；没有要求 $SV=V$。

**推论 4.1。** $T$ 必无界且 $D\ne L$。若 $T$ 在 $D$ 上有通常范数界，则闭性和 $D$ 稠密性使 $D=L$；图范数与普通范数等价后，(4.5) 迫 $D_N=D$，矛盾。若直接假设 $D=L$，闭图定理也产生同一矛盾。

对任意 $U\in GL_d(\mathfrak C)$ 的 $UM,UN$ 重复以上构造仍成立。因此任何最小秩 $d>1$ 的见证，在每种有界交换子可逆坐标变换后、准确除去垂直部分所得到的坐标图，都必须真无界、非全域。

也可从任意非零常系数行 $R:H^{(d)}\to H$ 出发：常系数酉变换将它变成第一坐标，再除去 $M\cap\ker R$。该垂直部分中各向量的分量线性张成维数小于 $d$，所以仍包含于 $N$。剩余闭图的域在 $\overline{RM}$ 稠密，却仍不能全域或有界。对任意交换子行不能未经证明地声称其核全在 $N$；以上一般坐标变换版本用的是可逆矩阵及命题2.1。

## 5. 共同闭乘子的正则器充分条件

固定实际循环向量 $g=1$。对任意有限族 $h_1,\ldots,h_r\in H$，R34 的对称配对给初始列算子
$$
T_0:p(A)g\longmapsto(p(A)h_1,\ldots,p(A)h_r)
\tag{5.1}
$$
可闭：若第一坐标趋零且全部输出有极限，每个分量的 R34 可闭性迫其极限为零。记其共同闭包为 $T:D(T)\subset H\to H^{(r)}$。这里取整个列的共同闭包，不自动将其等同于各分量闭包的最大交域。

其图是闭 $A^{(r+1)}$ 不变图。R88 的强多项式逼近使每个 $C\in\mathfrak C$ 保持该图，故 $TC=C^{(r)}T$ 于 $D(T)$。

假设存在 $R\in\mathfrak C$ 满足：

1. $I\in\overline{R\mathcal A}^{\mathrm{SOT}}$；
2. $RH\subset D(T)$，且 $B:=TR:H\to H^{(r)}$ 有界。

条件2的有界性已由全域包含与闭图定理推出；仍明列，以区别于只在某个共同稠密域中有界。$B$ 的各分量 $B_i$ 都在 $\mathfrak C$。

**命题 5.1。** 这两个条件保证 $S$ 在 $\mathcal G(T)$ 中稠密像，并且
$$
(h_1,\ldots,h_r)\in
\overline{\{(SFh_1,\ldots,SFh_r):F\in\mathcal A\}}.
\tag{5.2}
$$

**证明。** 先证 $RH$ 是图核心。对任意 $u\in D(T)$，条件1允许对有限族 $u,(Tu)_1,\ldots,(Tu)_r$ 同时选择 $F_\alpha\in\mathcal A$，使
$$
RF_\alpha u\to u,\qquad
(RF_\alpha)^{(r)}Tu\to Tu.
$$
后者等于 $TRF_\alpha u$，故 $(R,TR)H$ 在图中稠密。这是对指定有限元组的强拓扑逼近，不需要给该逼近网整体一个统一算子范数。

有界列 $\Gamma u=(Ru,Bu)$ 满足 $S^{(r+1)}\Gamma=\Gamma S$。由 $SH$ 稠密，$\overline{\Gamma SH}$ 包含 $\Gamma H$，继而为整个图，证明图稠密像。

对 (5.2) 可直接保留原代数。$Tg=(h_i)$ 给 $B_ig=Rh_i$；循环 $g$ 和 $SH$ 稠密给多项式 $p_n$ 使 $Sp_n(A)g\to g$。于是
$$
Sp_n(A)Rh_i=B_iSp_n(A)g\to B_ig=Rh_i
$$
同时成立。令 $M_h=\overline{\mathcal A^{(r)}(h_i)}$、$N_h=\overline{S^{(r)}M_h}$。$R$ 保持 $M_h$，所以上式给 $(Rh_i)\in N_h$。$N_h$ 被 $\mathcal A^{(r)}$ 保持；再用条件1在 $(h_i)$ 上强逼近，得 $(h_i)\in N_h$。证毕。

因此，对一个假想正有限秩见证的支撑元组，只要构造这样的 $R$，便有 $x\in N$，与 $x\in Q\setminus\{0\}$ 矛盾。$R$ 可以依赖于有限元组，不需要一个对全 $H$ 同时有效的固定正则器。

## 6. 未支付的步骤与 R230 的位置

R34 只给共同列可闭，不给条件2。共同稠密定义域、在真空上的取值、或者普通范数逼近，都不能替代 $RH\subset D(T)$。

R203/R170 已排除由非零 UHF 算子对无界逐位局部有限乘子作这种全域正则化。已有正一阶预解式确实位于 UHF 外，但尚不能假设它们覆盖任意元组的共同闭乘子图。

R230 已排具有某个 $r>9$ 的 Walsh 次数指数矩的正正常湮灭态，覆盖全部相对相位的 R16 乘积有限张成。这是直接泛函分解的排除，不需要上述共同源图正则化，也不被共同产品源的障碍否定。本稿不再将一般复产品见证当作未排范围。

(3.1)、(4.5) 与命题5.1之间的差别是：前两式容许一个普通范数稠密、图范数闭且真小的 $D_N$；命题5.1会给有界交换子列稠密参数化整个图，从而排除这种情形。一般元组的这种参数化尚未构造。未知商上不自动存在原共轭，垂直部分也不能略去。

