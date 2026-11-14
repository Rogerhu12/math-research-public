# R150 附录：Jacobian 证书中的真实 Bell 有界逆分母

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。
状态：已证明的条件判据；root 与 boundary_resume_1cf 全文核验原闭图、右输入顺序及二次增长预算。不把待求的标量理想归属当作已经成立。

## 1. 设置及精确结论

保留[完整合并矩 Jacobian 稿](R150-appendix-complete-moment-jacobian-certificates-regular-fibers-and-finite-exceptions.md) §§1–6 的原有限对数模式、固定中心、物理合并矩及指数权 $w$。
记原普通目标 $F$ 的完整标量多项式为 $Q=Q_F(W)$，原完整实际多项式为
$$
P=e^{\mathscr L}Q-\lambda I=Q-\lambda+K_Q.
$$
其规范最大闭实现为 $\mathsf P$，目标向量为
$[F(u)-\lambda]e^w$。
所有以下恒等式都使用这个完整 $Q$，不使用未经 Bell 变换的原 $F$ 的梯度。

允许把有限合并键表填充到同一个较大有限表。
新加入的键仍按其真实物理行去重；未出现在 $P$ 中的偏导为零。
有限不同键的原跨池矩阵及逆费用仍由原合并矩定理支付。
共同的 $\mathscr L$ 明确保留到 $\max(\deg Q,\deg S)$ 阶，并纳入这个共同键表所需的全部真实 $G_\beta$；较高阶导数在 $Q$ 上为零，因此不改变原 $P$ 的实现。

取固定标量多项式 $S(W)$、固定整数 $\nu\ge1$，并假设已经验证有限恒等式
$$
\boxed{
S^\nu=A_{\rm cert}(Q-\lambda)+\sum_g B_g\,\partial_g Q.
}
\tag{1.1}
$$
设
$$
S_{\rm act}=e^{\mathscr L}S=S+K_S
$$
的原规范最大闭实现为 $\mathsf S$。
另要求一个真实算子条件：
$$
\boxed{
\mathsf S:\operatorname{Dom}\mathsf S\longrightarrow H
\text{ 为双射，}\qquad V=\mathsf S^{-1}\in A'\cap B(H).
}
\tag{1.2}
$$
这是整个原 Hilbert 空间上的逆，既不是形式倒数，也不是未知不变空间中的假设逆。

**定理。** 在 (1.1)–(1.2) 下，
$$
\boxed{
\ker\mathsf P=0,\qquad
[F(u)-\lambda]e^w\ne0,\qquad
[[F(u)-\lambda]e^w]_A=H.
}
\tag{1.3}
$$
若同一标量证书的 (1.2) 对每个允许的 $w$ 都成立，则结论也对全部这些 $w$ 成立。
没有要求 $S$ 为原 Jacobian 理想的单位。
没有从某个目标的一次循环性推断其普通点态幂。

## 2. 有界逆准确保持全部自然词域与原核

先明确 (1.2) 的域用途。
由 [R88](R88-riesz-basis-bounded-multipliers-strong-closure.md) §7，每个 $V\in A'$ 都有一致有界的真实 $A$ 多项式序列 $p_n(A)$ 强趋 $V$。

取构造中任一实际闭 first 或其实际正分量 $Y$。
这些多项式保持 $\operatorname{Dom}Y$ 并与 $Y$ 在该域交换。
对 $x\in\operatorname{Dom}Y$，
$$
p_n(A)x\longrightarrow Vx,\qquad
Yp_n(A)x=p_n(A)Yx\longrightarrow VYx.
$$
$Y$ 的闭性给
$$
Vx\in\operatorname{Dom}Y,\qquad YVx=VYx.
\tag{2.1}
$$

对每个有序自然词 $Y_I$ 按右侧后缀长度归纳，得到
$$
V\mathcal D_N\subseteq\mathcal D_N,\qquad
Y_I Vx=VY_Ix\quad(|I|\le N),
$$
$$
\|Vx\|_{(N)}\le\|V\|\,\|x\|_{(N)}.
\tag{2.2}
$$
这里 $\mathcal D_N$ 保留所有长度不超过 $N$ 的词序，
图范数为这些词范数平方之和。
只使用每个 first 的闭性；没有声称单个自然混合词自身必闭，
也没有把复行共同域等同于更小的正分量共同域。

[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) §4 的规范图写作
$$
F_Px=R^d y,\qquad F_P,R\in A',\quad R\text{ 单射}.
$$
因而
$$
M:=\ker\mathsf P=\ker F_P.
$$
$A'$ 交换，所以
$$
VM\subset M.
\tag{2.3}
$$
同一有界图方程也给 $V\operatorname{Dom}\mathsf P\subset\operatorname{Dom}\mathsf P$ 及域内交换。
不要求 $V^*$ 保持 $M$。

由实际左右逆逐次消去，
$$
\mathsf S^\nu V^\nu=I\quad\text{于全部 }H,
\tag{2.4}
$$
且 $V^\nu H$ 位于自然 $\nu$ 次复合的定义域。
在足够深的共同自然词域上，这个自然复合与有限多项式
$S_{\rm act}(W)^\nu$ 的求值相同；
这是有限词逐次展开，未把两个未经证明相同的最大域互换。

## 3. 真实修正和正确的误差符号

定义有限实际多项式
$$
\Delta=S_{\rm act}^{\,\nu}-S^\nu,\qquad
H_{\rm fast}=\Delta-A_{\rm cert}K_Q-\sum_gB_g\partial_gK_Q.
\tag{3.1}
$$
$K_Q,K_S$ 的每个非零系数均至少含一个真实快累积量。
$\Delta$ 的二项展开也有此性质。
有限和积封闭说明 $H_{\rm fast}$ 的每个非零系数是已有四次幂型的快系数。

从 (1.1) 逐项计算，
$$
\begin{aligned}
\sum_g B_g\partial_gP
&=S^\nu-A_{\rm cert}(Q-\lambda)+\sum_g B_g\partial_gK_Q\\
&=S_{\rm act}^{\,\nu}-A_{\rm cert}P-H_{\rm fast}.
\end{aligned}
\tag{3.2}
$$
在已付共同深域上把 $V^\nu$ 保在右侧，使用 (2.2)–(2.4)：
$$
\boxed{
\sum_g(B_gV^\nu)\partial_gP
=I-A_{\rm cert}PV^\nu-E,\qquad
E=H_{\rm fast}V^\nu.
}
\tag{3.3}
$$

不必声称 $H_{\rm fast}V^\nu$ 仍属于某个原先较窄的快系数代数。
这里只需要已经足够的实际范数估计。
若 $H_j$ 是 $H_{\rm fast}$ 的一个非零系数，
$$
\|H_j^k\|\le C^k e^{-ck^4}.
$$
由于 $V$ 与 $H_j$ 交换，
$$
\|(H_jV^\nu)^k\|
\le \|V\|^{\nu k}C^k e^{-ck^4}.
\tag{3.4}
$$
有限多个系数的联合乘积也有同样的四次衰减，常数可依赖固定的 $V,\nu$ 和证书。

## 4. 二次增长词深和全部分母费用

令
$$
D=\max(1,\deg Q),\quad s=\max(0,\deg S),\quad
a=\max(0,\deg A_{\rm cert}),\quad
b=\max_g\max(0,\deg B_g),
$$
$$
L_0=2+D+a+b+\nu s.
\tag{4.1}
$$
零多项式的次数在这些粗上界中取零。
由有限微分指数，
$\deg K_Q\le D-2$、$\deg K_S\le s-2$（次数不足时该修正为零），
从而 $\deg H_{\rm fast}\le L_0$。

用原有限个正分量 $T_j$ 取
$$
q_r=(8L_0+8)(r+1)^2,\qquad \epsilon_r=r^{-3},
$$
$$
\mathcal R_r=
\left[\prod_j(I+\epsilon_rT_j)^{-1}\right]^{q_r}.
\tag{4.2}
$$
沿用已证明的增长正预解计算，
$$
\mathcal R_rH\subset\mathcal D_{q_r},\qquad
\mathcal R_rM\subset M,\qquad
\mathcal R_r\longrightarrow I\text{ 强},
$$
$$
\|W^\gamma\mathcal R_r\|\le(C+Cr^3)^{|\gamma|}
\quad(|\gamma|\le q_r).
\tag{4.3}
$$
(2.2) 使任意所需的 $V$ 次幂不消耗词深。

由 (3.4)、有限多项式展开和 (4.3)，
$$
\boxed{
\|E^k\mathcal R_r\|
\le\exp[-c_0k^4+C_0k\log(r+2)],
\qquad 0\le k\le r^2.
}
\tag{4.4}
$$
所有常数可以依赖固定证书和 $\|V\|$。
若 $H_{\rm fast}=0$，对应误差直接为零。

令
$$
T_r(E)=\sum_{k=0}^{r-1}E^k,\qquad
\widetilde B_{g,r}=B_gV^\nu T_r(E).
$$
由 (3.3)，在原 $M$ 的共同深域中，
$$
\boxed{\sum_g\widetilde B_{g,r}\partial_gP=I-E^r.}
\tag{4.5}
$$
其中 $A_{\rm cert}PV^\nu T_r(E)$ 的消失使用原核及已证域内交换。

$r$ 个块的显示多项式字数至多
$$
r[b+L_0(r-1)]=O(r^2).
$$
全部右输入中 $V$ 的次数至多
$$
\nu[r+r(r-1)]=\nu r^2.
\tag{4.6}
$$
所以相较原 Jacobian 证明，逆只额外产生
$\exp[O(r^2)\log^+\|V\|]$ 的固定预算；
$P^r$、局部交换子及反射展开仍有 (4.2) 的明确词深余量。

## 5. 原反射和原局部配对完成排核

对每个原跨池物理块，仍用实际合并行矩阵 $\Xi_B$，
把旧块输入中的 $B_g T_r$ 换为 $\widetilde B_{g,r}$：
$$
Q_B^{[r]}=
\frac14\sum_i\left[\sum_g(\Xi_B^{-1})_{ig}\widetilde B_{g,r}\right]
\prod_{\ell\ne i}t_{p_\ell}N_{p_\ell}.
\tag{5.1}
$$
全部输入先在原 $M$ 中形成；物理反射始终位于其左侧。
各项中的 $V$ 只在有界右输入内部与实际 first、快系数及 $N_p$ 交换，
从不穿过反射或未知限制的伴随。

(4.5) 使 $r$ 个块的真实最高项准确为
$$
r!\,t_E N_E(I-E^r)^r\mathcal R_rf.
\tag{5.2}
$$
矩阵维数、原匹配排序、每块一次提升、完整阶乘及原纯池平均均保持不变。
由 (4.4)，
$$
\|[(I-E^r)^r-I]\mathcal R_r\|
\le\sum_{j=1}^r\binom rj
e^{-c_0(rj)^4+C_0rj\log(r+2)}
\le e^{-c_1r^4}.
\tag{5.3}
$$
最大幂恰不超过已付的 $r^2$。

取原 $r=\lfloor\sqrt N\rfloor$、固定分离的 $K$ 个物理池。
全部输入和自然词的费用满足
$$
\log A_N\le Cr\log N+Cr^2\log(r+2)+Cr^2\log^+\|V\|
=o(r^4).
\tag{5.4}
$$
只对固定原 $P$ 进行反射和局部交换子展开。
一般有界 $V$ 没有被赋予额外的反射正则性；
它由 (4.6) 按右输入范数计费。
原 carry 的 $e^{-c16^{\mu N-1}}$ 仍压住 (5.4)。

因此原正确归一化及一致有界纯平均给
$$
\mathsf P^r\mathcal V_N^{[r]}\mathcal R_rf
\rightharpoonup e^{-K/2}f\qquad(f\in M).
\tag{5.5}
$$
误差 (5.3) 乘的是已经归一化的一致有界平均，不是增长的原输入费用。
对每个固定有限局部全矩阵 $D_0$，
$$
\|(\operatorname{ad}_P^rD_0)
\mathcal V_N^{[r]}\mathcal R_rf\|
\le
e^{-5r^4/6+105r^3+Cr^2\log(r+2)+Cr\log N+Cr^2\log^+\|V\|}\|f\|
\longrightarrow0.
\tag{5.6}
$$
仍保留局部展开两侧的原 $A$ 幂，没有从一般快系数提出未证的有界 $A$ 商。

完整全空间 $C$ 对称与 $g\in M$ 给
$$
B(D_0\mathsf P^r\mathcal V_N^{[r]}\mathcal R_rf,g)
=(-1)^r B((\operatorname{ad}_P^rD_0)
\mathcal V_N^{[r]}\mathcal R_rf,g).
$$
用 (5.5)–(5.6) 得 $B(D_0f,g)=0$ 对所有局部全矩阵。
原局部代数不可约，故 $M=0$。
再用原规范图的完整 $C$ 自伴性和 $e^w$ 多项式图核心，得到稠密像及 (1.3)。
这完成条件判据的证明。

## 6. 可直接使用的分母：空谱 first 的完整 Bell 平方

设一条实际 first $v$ 的倾斜闭算子 $D=X_{v,w}$ 已证明空谱，且各预解属于 $A'$。
令 $L=D^{-1}\in A'$。
空谱给 $\sigma(L)\subset\{0\}$，所以 $L$ 拟幂零。

完整 ordinary Bell 平方的真实实现为
$$
\mathsf S=D^2+C_1D+C_0,\qquad C_0,C_1\in A'\cap B(H),
$$
其中系数是原 $v,w$ 的真实系数，不删除二阶 Bell 修正。
在 $\operatorname{Dom}D^2=\operatorname{Ran}L^2$ 上，
$$
\mathsf S=(I+C_1L+C_0L^2)D^2.
$$
括号中除单位外是有限个彼此交换的拟幂零元之和，故为真实有界单位。
于是
$$
\boxed{
V=L^2(I+C_1L+C_0L^2)^{-1}\in A'\cap B(H).
}
\tag{6.1}
$$
$D^2$ 是有界单射 $L^2$ 的闭逆；左乘有界单位仍闭。
原单模式及多模式图核心识别这个实现恰为 $v^2e^w$ 的完整普通 Bell 最大图。
这是[真实偏导逆稿](R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md) §4 的同一证明；
这里明确只需已付的实际空谱 first，不需要该行本身为实数。

因此，若 $S=Q_{v^2}$ 属于同一个已付的有限合并键表，且其某个**自然代数幂** $S^\nu$ 满足 (1.1)，即可应用本稿。若该 first 引入新物理行，必须先另付这些行的合并、跨池矩阵及逆费用；空谱本身只保证这里的真实逆，不能免费保证新池结构。
这个 $S^\nu$ 不等于普通点态 $v^{2\nu}$ 的完整 Bell 多项式；
二者不能互换。
有限域证书、只在已知临界点消失或未核完的有理重构，都不足以代替 (1.1)。

## 7. 一般范围仍然保留

本稿提供从完整标量理想证书和真实有界逆到原向量循环性的完整桥梁。
它本身不证明任意 $S^\nu$ 属于给定 Jacobian 理想；
也不把任意符号多项式视为空谱算子。
所有未覆盖的临界纤维、无限模式、一般正常见证和原边界 $N=M$ 仍须各自证明。
普通可分无限维复 Hilbert ISP 的完成标准没有改变。
