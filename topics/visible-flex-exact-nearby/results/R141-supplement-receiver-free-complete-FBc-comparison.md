# R141 supplement: one complete receiver-free $F B_c$ comparison

2026-11-20, visible-exact-astra-ac637-20261120, positive_inverse.

**已证明：** 下列独立比较计算的对象、全部算子项、域、精确有限支持与后继消费公式。本文没有运行新科学数值，尚未给出该比较的数值上界或任何新可逆性结论。计算目标只有一个，保存三条 directed scalar：完整 row、column、norm 上界。

原 W2C 固定小中心配方已由 R139 的完整 centre mean 下界排除；本计算供 R141 吸收真实低中心后的新参考逆使用。它不重新计算旧 50 目标中的任何一条，也不要求原大中心范数小于 $1/128$。已成 L 三量、centre mean 排除与 endpoint 诊断保持只读。

## F1. 精确对象及单位

沿用 [WJK](R133-supplement-joint-centre-Green-kernel-and-complete-collar-cross-terms.md) 的 (JK.1)–(JK.7) 及 [W2C](R133-supplement-complete-collar-Volterra-dual-feedback-candidate.md) 的整个候选。角测度归一化，物理频率 $4j$，径向测度普通 $dr$，区间从真实 root $a=r_*$ 到 $R=25/8$。令

$$
\mathscr X=L^2(I;E_L),\quad \dim E_L=193,\qquad
K_0=\{97,\ldots,160\},\quad K_1=\{97,\ldots,224\}.
\tag{F.1}
$$

高带均含原 odd/even 两分量，$\dim K_0=128$、$\dim K_1=256$。$\Pi_0,\Pi_1$ 为这些正交角投影。原 $S$ 在 odd 坐标为 1，在 even 坐标（包括独立 mean）为原正权 $q$。定义

$$
B_c=B_{HL,c}S^{-1},\quad L_c=\partial_r-A_c,\quad
G=G_{0,160},\quad E=A_c-D,\quad P_0=\chi G\chi.
\tag{F.2}
$$

$A_c$ 保持同实际 $\eta$ principal 与 repaired degree32 lower centre；它是原 WVC hybrid 试算子，不冒充真 $DF(Q_{\rm repair})$。$B_c$ 已包括一次且仅一次右侧 $S^{-1}$。本文保存的量为

$$
f_0\ \ge\ \|\Pi_0F B_c\|_{\mathscr X\to L^2(I;K_0)}.
\tag{F.3}
$$

因此不能再给 (F.3) 右乘第二个 $S^{-1}$。此目标不包含 $G_f$、R141 低逆、端点原子或任何物理角转换。那些算子须由各自完整证书消费 (F.3)；它们没有因源侧比较而消失。

## F2. 全 $P,Q^*,R_c$，先作精确 collar 消去

沿用原 $c$、$\chi$、宽 $1/16$ 的 $\psi$，以及

$$
(Jf)(r)=\int_a^{\min(r,c)} f(s)\,ds,\qquad
(J^*f)(s)=\mathbf1_{[a,c]}(s)\int_s^R f(r)\,dr.
\tag{F.4}
$$

第一式在 $c$ 之后保留常值延拓；第二式的上端始终是 $R$。令

$$
P=P_0+\psi(J+JA_cJ),\quad
Q^*=P_0+(-J^*+J^*A_cJ^*)\psi,\quad
R_c=(L_cP-I)B_c .
\tag{F.5}
$$

由 $J'=P_c$、$\psi P_c=P_c$ 与 $P_cA_c=A_cP_c$，完整残差在取绝对值之前恒等于

$$
\begin{split}
R_c={}&\bigl[
(\chi^2-P_b)I+(\chi'I-\chi E)G\chi\\
&+\psi'(J+JA_cJ)-\psi P_bA_cJ-\psi A_cJA_cJ
\bigr]B_c .
\end{split}
\tag{F.6}
$$

这五个加项全部保留。特别在 collar 上仅剩
$P_cR_c=-P_cA_cJA_cJB_c$，原 $-B_c$ 已由精确微分恒等式消去，而不是用两条正上界相减。transition 的 $\psi'$、body 的 $\psi P_bA_cJ$ 及 primal/dual collar 交叉项均在后续 (F.7) 内。

原完整 WJK 算子满足

$$
F=P+Q^*-Q^*L_cP,\qquad
\Pi_0F B_c=\Pi_0PB_c-\Pi_0Q^*R_c.
\tag{F.7}
$$

该式等价于 (JK.8) 的 body 项与全部五个 collar 项。本文使用完整差的三角上界，明确不声称获得了 (F.7) 两项之间的 signed cancellation。

## F3. 支持限制是精确关系，不截断实际高未知

同 centre 的 local 系数带宽为 64，两个 primitive 因子带宽各 32。principal 不改变频率。因此

$$
B_c:\mathscr X\to K_0,\qquad
PB_c:\mathscr X\to K_1,\qquad
R_c:\mathscr X\to\{97,\ldots,288\}.
\tag{F.8}
$$

且 $B_c$ 仅接受 low $33\le j\le96$ 的 128 个 odd/even 坐标。其 mean 输入列精确为零；同一事实不授实际全 degree96 的 $\Delta B$ mean 列为零。

在 $Q^*$ 的每个词中至多有一个带宽64 的 $A_c$。其左端投影 $\Pi_0$ 故给

$$
\Pi_0Q^*=\Pi_0Q^*\Pi_1,\qquad
\Pi_0F B_c=\Pi_0PB_c-\Pi_0Q^*\Pi_1R_c .
\tag{F.9}
$$

这是返回到 $K_0$ 时的精确支持论证。完整 $R_c$ 仍先构造至288，然后才在有限试算子的返回路径应用 $\Pi_1$。不能把 (F.9) 用于真实 $G_HR_c$ 或据此删掉实际无限高未知。

返回 $\Pi_0A_c\Pi_1$ 的范数由其真正伴随限制 $\Pi_1A_c^*\Pi_0$ 估计，包含 drift 的系数角导数。源码使用 `Astar160`；它没有把 `A160` 原样当作相反方向的范数。

## F4. 可直接执行的完整正比较

新最小模块 `fourfold_codazzi_complete_FBc_raw_math.py` 的
`build_receiver_free_WJK_comparisons` 以同一完整 context 构造

$$
\mathcal E_F=
\mathcal E_{\Pi_0PB_c}
+\mathcal E_{\Pi_0Q^*\Pi_1}\mathcal E_{R_c},
\qquad
|\Pi_0F B_c x|\preceq\mathcal E_F |x|.
\tag{F.10}
$$

每个 pointwise 比较使用完整有限角算子的 Schur norm；每个 integral 比较使用整径向 product cell 上的角算子 norm 上界。对 $J$ 可用 kernel $1_{\{s\in I_c\}}$，它在真实三角域外取1仍只是扩大正比较；其真正转置使用全部输出 $r\in I$，故不会漏掉 $J^*$ 的 $c$ 到 $R$ 段。

`assembly._complete_private_centre_norms` 提供同一 whole centre 的有限系数费用；`assembly._complete_modal_norm_comparison(..., low=False, ...)` 仅提供高 reference $G_{0,160}$ 的完整 kernel 比较。新模块不调用该函数的 `low=True` 分支、不调用旧 joint-centre 或完整50图，也不调用任何低 Green 或端点范数。

设155 comparison cells 的真实长度为 $\ell_i$。正比较的 forward 用输入全1，reverse 用输出全1，并按同一 $\ell_i$ 执行真正积分与转置。分别得到整域 row 上界 $r_F$、column 上界 $c_F$。operator-valued Schur 不等式给

$$
\|\Pi_0F B_c\|\le \|\mathcal E_F\|_{L^2\to L^2}
\le\sqrt{r_Fc_F}\le f_0 .
\tag{F.11}
$$

pointwise 项在这项比较中带本地乘子权，不能误乘或漏乘径向长度。当前 kernel 库的 `PointwiseNormComparison`、`PositiveComposition`、`PositiveSum` 与 `complete_positive_comparison_norm` 已按此约定构造。全部算子在普通 $dr$ 的相同 Hilbert 块间相乘；不把正积分比较的 reverse 改成无质量的矩阵转置。

## F5. 三条保存结果及包含保证

公共 owner `fourfold_codazzi_complete_FBc_raw_owner.py` 先完成原18项 readonly admission、原21 historical inputs 与原29 whole records 的一致身份，之后才导入固定 Python 3.12.14、python-flint 0.9.0 的320-bit directed runtime。同原153 parents、4650 rows、4801 intersections、155 comparison panels及完整 reference/diagonal chain构造 context。所有当前 inputs 的完整 bytes/hash 在新工作后复核。

只计算一个完整目标，按顺序保存：

1. `complete_projected_WJK_FBc_raw_row_ratio_upper`；
2. `complete_projected_WJK_FBc_raw_column_ratio_upper`；
3. `complete_projected_WJK_FBc_raw_norm_upper`。

每个值先取实际 directed upper，保存完整75位十进制 ball，再读取已写文件并检查字节对象一致和 `saved.contains(original_upper)`。后继乘积及比较只用读回区间的 upper；展示文字不代替这个包含证明。任何失败保留此前完整前缀且不自动重跑。

科学 wall cap 固定为2400秒；该 cap 仅限制这一个公共子计算，不能解释为停止本课题工作。私有图只有有限角系数与155格 scalar kernel tiles，没有24,480细胞稠密矩阵、193原子数组、公共大数据或 Release。context 的其他原算子可作为纯定义存在，但本 owner 不应用它们，也不重新计算任何已成数值目标。

## F6. 低193证书之后的精确消费：同 WJK 的完整 centre

以下是**条件性消费公式**；只有未来 R141 的同对象 low certificate 成功且 (F.11) 实际保存后才可执行，不由本文宣称其门已过。

令 $\mathscr Z=\mathscr X\oplus\mathbb R^{97}\oplus\mathbb R^{96}$，使用原193 output atoms 权重。记 $O$ 为 low body加全部原子观察，$G_L$ 为 R141 的真实 varying hybrid low block、原 reference 边界逆，$T_L$ 为其连续二类增广逆。未来证书提供

$$
\begin{split}
\|\operatorname{pr}_B OG_LB_{LH,c}\|&\le g_B,&
\|\operatorname{pr}_A OG_LB_{LH,c}\|&\le g_A,\\
\|\operatorname{pr}_B(T_L-I)\iota_B\|&\le c_B,&
\|\operatorname{pr}_A(T_L-I)\iota_B\|&\le c_A .
\end{split}
\tag{F.12}
$$

实际 $B_{LH,c}$ 的高输入仅 $K_0$；其经 $G_L$ 产生的完整 mean、body、97+96 atoms 全在 (F.12)。令 $k_B=g_Bf_0,\ k_A=g_Af_0$。若 $k_B<1$，则同 **有限 WJK $F$** 的完整连续 centre $T_c$ 可逆，而不要求 $k_A<1$。原因是反馈只读 body 输入，增广方算子为

$$
I-\begin{pmatrix}K_B&0\\K_A&0\end{pmatrix}.
\tag{F.13}
$$

原子输入保留恒等嵌入，没有尝试读取任意 $L^2$ 输入的端点迹。由 $T_c=(I-K)^{-1}T_L$，有

$$
\begin{split}
b&=\frac{c_B+k_B}{1-k_B},\\
a&=c_A+\frac{k_A(1+c_B)}{1-k_B},\\
\|T_c-I\|&\le M_C=\sqrt{b^2+a^2},\\
\|T_c\|&\le
\frac{\sqrt{(2+b)^2+a^2}+\sqrt{b^2+a^2}}2 .
\end{split}
\tag{F.14}
$$

证明最后式可把整个增广 operator 的正比较限制到 body/atoms 两个块，使用 $\left(\begin{smallmatrix}1+b&0\\a&1\end{smallmatrix}\right)$ 的最大奇异值公式。所有193 atoms在 $a$ 中联合保留；mean 不因 $B_c$ 的单个零输入列而从低逆中删除。

这正是 [R137 finite bridge](R137-supplement-continuous-to-finite-principal-lift-bridge.md) 需要的 full CFB continuous centre，随后还须新付

$$
M_{\rm mesh}\ge
\|\Lambda_h S[(A_{L,c}-D_f)S^{-1}+B_{LH,c}FB_c]\|.
\tag{F.15}
$$

这里 $B_c$ 仍是 (F.2) 已含右侧 $S^{-1}$ 的对象。$\Lambda_h$ 必须用原24,480细胞的 parent/160 真长度（含该桥的 $1/\pi$），不能用 R141 的1424 certification refinement。本文独立计算没有执行该新 mesh source 目标或任何 finite $\rho$ 比较。

## F7. 与真正 $G_H$ 的关系及未付义务

真实 actual full-family given-head $G_H$ 是另一个无限维逆；有限 $F$ 不等于它。原 [W2H](R133-supplement-two-sided-high-feedback-and-complete-centre-correctors.md) (W2H.12)、(W2H.19) 给完整双侧 primal/dual 残差恒等式。若改为 $G_L$ receiver，须同时改其全部 source、dual、atoms，并支付

$$
\Delta A,\quad \Delta B,\quad \Delta C,\quad
R_c-\Delta A\,PB_c-\Delta B,
\tag{F.16}
$$

包括288 centre残差、416 family残差和真正 $G_H$ 的全 collar/body源。不能把 (F.9) 的返回投影移给这些实际高残差。

本目标成功只意味着 (F.3) 的完整有限试算子 norm 已取得；即使后继 (F.14) 成功，也仍分别保留：

- 完整 actual-family 与 $F-G_H$ 费用；
- 实际 physical-angle、density 两 mean、$\Theta,\nu$、真实 outer193行与root97补行；
- 原七独立 primal/dual/source/affine ports和原 source/mean 单位；
- 原 finite $\rho$、已付 $\kappa=3$ 径向 tail及其实际 Schur余项；
- WPN 的两个原 RHS $f_f,g_t$，包括非零径向 mean-zero tail与源；
- 非线性、负侧/腰/帽匹配、全频精确族和课题 README 的几何标准。

上述 scope 在新 owner 输出中均显式为未授。完整公式证明与未来数值门严格分开。
