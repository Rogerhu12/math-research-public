# R267：互不交奇数 Walsh 块的实际增生正则器与收缩强单位

日期：2026-11-13（UTC）。作者：normal_states；Astra-ISP-1cf 复核。

状态：以下实际块矩阵、增生补偿、无穷乘积强极限及同一组逆词强单位均已证明，属于中间结论。构造允许任意增长的有限 Walsh 块次数，未将这些正则器归入一阶类，也未证明它们满足任意假想慢湮灭者的 R244 配对条件。

## 1. 实际一位行及其正实部

沿用原 Haar 表示和全部真实 carry：
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
V_j=(I-N_j)(I+N_j)^{-1},\qquad
V_F1=\chi_F,\qquad \|V_j\|\le6.
$$
$\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$，$\mathfrak C=\{A\}'$。全部 $V_j$ 属于 $\mathcal A$、相互交换并且 $C$ 对称。

令 $\Omega_j=(e_0+e_1)/\sqrt2$、$\chi_j=(e_0-e_1)/\sqrt2$。在第 $j$ 位的 Walsh 分解
$$
H=H_{<j}\otimes
\bigl(\mathbb C\Omega_j\oplus\mathbb C\chi_j\bigr)
\otimes H_{>j}
$$
中，低位张量恒等暂略。写 $B_j=\eta_jN_{j+1}$。从物理块
$$
N_j=\begin{pmatrix}0&B_j\\I&0\end{pmatrix}
$$
直接求逆得到准确等式
$$
\boxed{
V_j=\begin{pmatrix}0&-I\\ I&2K_j\end{pmatrix},
\qquad
K_j=(I+B_j)(I-B_j)^{-1}.
}
\tag{1.1}
$$
这不是把有限柱压缩当成代数同态；矩阵条目仍为全部真实尾算子。

由 $\|B_j\|\le\eta_j<1$，
$$
\operatorname{Re}K_j
=(I-B_j^*)^{-1}(I-B_j^*B_j)(I-B_j)^{-1}
\ge\frac{1-\eta_j}{1+\eta_j}I.
$$
因而若 $P_j^1$ 为第 $j$ 位 Walsh 非真空投影，
$$
\boxed{
\operatorname{Re}V_j
=\begin{pmatrix}0&0\\0&2\operatorname{Re}K_j\end{pmatrix}
\ge 2\frac{1-\eta_j}{1+\eta_j}P_j^1
\ge P_j^1.
}
\tag{1.2}
$$
最后一步使用本题 $\eta_j\le e^{-77016^j}<1/3$。

更精确地，对任意尾向量 $h$，
$$
V_j(\Omega_j\otimes h)=\chi_j\otimes h,\qquad
V_j^*(\Omega_j\otimes h)=-\chi_j\otimes h.
\tag{1.3}
$$
两式完全不含余项。

## 2. 奇数块实部的准确零真空空间

对有限非空 $F$，令
$$
P_F^0=\prod_{j\in F}(I-P_j^1),\qquad Q_F=I-P_F^0.
$$
$P_F^0H$ 只要求 $F$ 中每一位为 Walsh 真空；所有补位允许任意向量。

按从低位到高位的顺序使用 (1.3)，每一步只把当前真空位变为 $\chi_j$，不改变其余位。利用实际 $V_j$ 的交换性，得到
$$
V_FP_F^0=J_FP_F^0,\qquad
V_F^*P_F^0=(-1)^{|F|}J_FP_F^0,
\tag{2.1}
$$
其中 $J_F$ 表示逐位 Walsh 翻转的乘积；在 $P_F^0H$ 上只是把这些真空位换成相应 $\chi_j$。

若 $|F|$ 为奇数，
$$
\boxed{(\operatorname{Re}V_F)P_F^0=0.}
\tag{2.2}
$$
由于实部自伴，(2.2) 同时给左侧零行。因此
$$
-6^{|F|}Q_F\le\operatorname{Re}V_F\le6^{|F|}Q_F.
\tag{2.3}
$$
又 $\sum_{j\in F}P_j^1\ge Q_F$，结合 (1.2)，
$$
\boxed{
-6^{|F|}\sum_{j\in F}\operatorname{Re}V_j
\le\operatorname{Re}V_F
\le6^{|F|}\sum_{j\in F}\operatorname{Re}V_j.
}
\tag{2.4}
$$

这里只对实倍数 $tV_F$ 使用上述对称实部。任意复数 $t$ 不满足同一零真空结论，不能不加条件地代入。

**具体增生块。** 取 $t\in\mathbb R$ 和 $b\ge |t|6^{|F|}$，定义
$$
\boxed{
L_{F,b,t}=b\sum_{j\in F}V_j+tV_F\in\mathcal A.
}
\tag{2.5}
$$
则 (2.4) 给 $\operatorname{Re}L_{F,b,t}\ge0$。所以
$$
R_{F,b,t}=(I+L_{F,b,t})^{-1}
$$
为有界收缩，并属于 $\mathfrak C$。

若 $|F|\ge3$ 为奇数，
$$
v_{F,b,t}:=L_{F,b,t}1
=b\sum_{j\in F}\chi_j+t\chi_F,\qquad
\langle v_{F,b,t},1\rangle=0,
$$
$$
\boxed{\|v_{F,b,t}\|^2=|F|b^2+t^2.}
\tag{2.6}
$$
因此 $t\ne0$ 时生成元本身有真实的高阶 Walsh 项。下面不需要证明一个所得极限无法用别的参数重新表示成其他已知正则器；新增的是允许这些块的直接构造与完整收敛证明。

## 3. 更一般的互不交有限块定理

以下定理只使用块向量的有限 Walsh 支撑、实际增生性和平方可和性。

取两两不交的有限位集 $F_\nu$。令 $v_\nu$ 为依赖 $F_\nu$ 的有限 Walsh 多项式，并假设
$$
\langle v_\nu,1\rangle=0,\qquad
L_\nu=X_{v_\nu}\in\mathcal A,\qquad
\operatorname{Re}L_\nu\ge0.
\tag{3.1}
$$
还要求
$$
\boxed{\sum_{\nu\ge1}s_\nu^2<\infty,\qquad s_\nu=\|v_\nu\|.}
\tag{3.2}
$$

定义
$$
R_\nu=(I+L_\nu)^{-1},\qquad
P_n=\prod_{\nu=1}^nR_\nu,\qquad
U_n=\prod_{\nu=1}^n(I+L_\nu).
\tag{3.3}
$$
全部因子为实际有界交换子，并且
$$
\|R_\nu\|\le1,\quad \|P_n\|\le1,\quad
P_nU_n=U_nP_n=I.
$$
每个 $U_n$ 属于 $\mathcal A$，但其范数不要求一致有界。

**定理。** 在 (3.1)—(3.2) 下：

1. $P_n$ 强收敛到非零收缩 $P\in\mathfrak C$。
2. $g_n=U_n1$ 在 $H$ 中收敛到 $g$，且 $Pg=1$。
3. 同一组有界逆词 $U_n$ 满足
   $$
   \boxed{\|PU_n\|\le1,\qquad PU_n\longrightarrow I\quad\mathrm{SOT}.}
   \tag{3.4}
   $$
4. $P$ 单射且稠密像，$g$ 对实际 $A$ 循环；最小闭乘子 $X_g$ 准确等于 $P^{-1}$。
5. 在任意有限放大及任意实际闭 $A$ 不变旗的子商上，$P$ 的诱导算子仍单射且稠密像。

这些结论不要求 $\sum_\nu\|L_\nu\|<\infty$，也不要求块大小一致有界。

## 4. 真实逆词的准确 Walsh 块乘积

对有限 $n<m$，记
$$
U_{n,m}=\prod_{\nu=n+1}^m(I+L_\nu),
\qquad
g_{n,m}=U_{n,m}1.
$$
因为 $L_\nu$ 是支撑于 $F_\nu$ 的有限 $V_J$ 线性组合，而不同 $F_\nu$ 不交，展开中每个乘积都不重复位。于是 $V_J1=\chi_J$ 准确给
$$
\boxed{
g_{n,m}=\prod_{\nu=n+1}^m(1+v_\nu).
}
\tag{4.1}
$$
右边是通常的 Walsh 函数乘积。只对这个真空列作此识别；没有声称算子乘法本身就是点乘，也没有删除 carry。

互不交位独立，且每个 $v_\nu$ 均值为零。因此
$$
\langle g_{n,m},1\rangle=1,\qquad
\|g_{n,m}\|^2=\prod_{\nu=n+1}^m(1+s_\nu^2),
$$
$$
\boxed{
\|g_{n,m}-1\|^2
=\prod_{\nu=n+1}^m(1+s_\nu^2)-1.
}
\tag{4.2}
$$
令
$$
d_n^2=\prod_{\nu>n}(1+s_\nu^2)-1.
\tag{4.3}
$$
(3.2) 保证无限乘积有限、$d_n\to0$，且 (4.2) 不超过 $d_n^2$。

同样，$g_n=\prod_{\nu\le n}(1+v_\nu)$ 满足
$$
\|g_m-g_n\|^2
=\left[\prod_{\nu\le n}(1+s_\nu^2)\right]
\left[\prod_{\nu=n+1}^m(1+s_\nu^2)-1\right].
\tag{4.4}
$$
所以 $g_n$ 在 $H$ 收敛。其极限满足
$$
\langle g,1\rangle=1,\qquad
\|g\|^2=\prod_{\nu\ge1}(1+s_\nu^2)<\infty.
\tag{4.5}
$$

## 5. 收缩尾积与非零强极限

写
$$
Q_{n,m}=\prod_{\nu=n+1}^mR_\nu.
$$
它是收缩，而且 $Q_{n,m}g_{n,m}=1$。因此
$$
Q_{n,m}1-1=Q_{n,m}(1-g_{n,m}),
$$
$$
\boxed{\|(Q_{n,m}-I)1\|\le\|g_{n,m}-1\|\le d_n.}
\tag{5.1}
$$
这正是强收敛需要的尾估计；只知道各个 $R_\nu$ 收缩并不能直接省掉它。

由于 $P_m=P_nQ_{n,m}$，
$$
\|(P_m-P_n)1\|\le d_n.
\tag{5.2}
$$
对任意固定 $F\in\mathcal A$，交换性给
$$
\|(P_m-P_n)F1\|\le\|F\|d_n.
$$
$\mathcal A1$ 稠密，且所有 $P_n$ 范数至多1，故 $P_n$ 在全 $H$ 强收敛到收缩 $P$。交换子代数强闭，故 $P\in\mathfrak C$。

又 $P_ng_n=1$、$g_n\to g$，所以
$$
\|P_ng_n-Pg\|
\le\|g_n-g\|+\|(P_n-P)g\|\longrightarrow0.
$$
从而
$$
\boxed{Pg=1.}
\tag{5.3}
$$
特别 $P\ne0$。

## 6. 同一组逆词给收缩强单位

固定 $n$，对 $m\ge n$，
$$
P_mU_n=Q_{n,m}.
$$
令 $m\to\infty$。由于 $U_n$ 是一个固定有界算子，
$$
\boxed{PU_n=\mathrm{SOT}\!-\!\lim_{m\to\infty}Q_{n,m},\qquad
\|PU_n\|\le1.}
\tag{6.1}
$$
由 (5.1)，
$$
\|(PU_n-I)1\|\le d_n.
$$
对固定 $F\in\mathcal A$，再次交换：
$$
\|(PU_n-I)F1\|\le\|F\|d_n.
$$
循环性和产品收缩界使之延伸到全 $H$，即 (3.4)。

若 $Px=0$，则交换性给 $PU_nx=U_nPx=0$，而左侧趋于 $x$，故 $x=0$。又每个 $PU_nH$ 包含于 $\operatorname{Ran}P$，所以 $P$ 稠密像。

置 $M=\overline{\mathcal A g}$。R88 使 $M$ 被整个 $\mathfrak C$ 保持；由 $1=Pg\in M$ 及 $1$ 循环，得到 $M=H$。因此 $g$ 循环。

最后，[R244 的聚合逆图附录](R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)在这里全部适用：
$$
P^{-1}(F1)=Fg\qquad(F\in\mathfrak C),
$$
全部有限柱构成 $P^{-1}$ 的真实图核心，故 $P^{-1}=X_g$。这也给同一逆词在整个 $\operatorname{Ran}P$ 上的准确逼近
$$
U_nu=(PU_n)P^{-1}u\longrightarrow P^{-1}u.
\tag{6.2}
$$
并未要求 $U_n$ 在全 $H$ 一致有界。

对有限放大和闭不变旗，R88 保证每个 $P,U_n$ 都保持旗。诱导的 $(PU_n)$ 仍收缩且强趋于商恒等。刚才单射和稠密像的两段论证原样成立，证明第3节第5项。没有把一般全空间稠密像无证下传，而是使用了同一组实际强单位。

## 7. 显式高阶族及一个已付的指数域

取两两不交的奇数位集 $F_\nu$，$q_\nu=|F_\nu|\ge3$，允许 $q_\nu\to\infty$。选择实数 $t_\nu$、非负数 $b_\nu$，满足
$$
b_\nu\ge6^{q_\nu}|t_\nu|,\qquad
\sum_\nu q_\nu b_\nu^2<\infty.
\tag{7.1}
$$
令
$$
L_\nu=b_\nu\sum_{j\in F_\nu}V_j+t_\nu V_{F_\nu}.
$$
第2节给实际增生性，而
$$
s_\nu^2=q_\nu b_\nu^2+t_\nu^2
$$
平方可和，故全部结论成立。

例如任给这些块，可取
$$
b_\nu=\frac{2^{-\nu}}{\sqrt{q_\nu}},\qquad
t_\nu=b_\nu6^{-q_\nu}\ne0.
$$
这给真正含无限多个高阶块的明确族。其他满足 (7.1) 的行可以不使生成元范数总和收敛。

记 $H_r=\operatorname{Dom}r^{\mathcal N}$。对 (7.1) 的具体补偿，逆真空源还有
$$
\boxed{g\in H_6.}
\tag{7.2}
$$
证明仍由互不交的准确 Walsh 乘积：
$$
\|6^{\mathcal N}g_n\|^2
=\prod_{\nu\le n}
\left(1+36q_\nu b_\nu^2+6^{2q_\nu}t_\nu^2\right).
$$
右侧由 (7.1) 一致有界，而且对应加权尾乘积趋于1，故 $g_n$ 在 $H_6$ 收敛到 $g$。

由 [R255 的真实 $\sqrt3$ 端点乘法定理](R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)，(7.2) 进而给一个实际范围包含：
$$
\boxed{H_{\sqrt3}\subseteq\operatorname{Ran}P,\qquad
P^{-1}:H_{\sqrt3}\to H\text{ 有界}.}
\tag{7.3}
$$
确切地，$g\in H_{\sqrt3}$，R255 使每个 $u\in H_{\sqrt3}$ 属于最小闭乘子 $X_g$ 的域，并给连续范数界；第6节已识别 $X_g=P^{-1}$，所以 $PX_gu=u$。

(7.3) 只是一个已付的固定指数域。它没有证明每个任意小平方根次数域都包含于 $\operatorname{Ran}P$，也没有给整个次数 $\le q$ 空间的零型 $e^{o(\sqrt q)}$ 逆界。不能把只针对一阶累计行的 R261 估计直接套给这些高阶块。

## 8. 与正常湮灭者接口的准确关系

本构造已经支付了 R244 聚合附录所需的全部正则器结构：$P\in\mathfrak C$、$1\in\operatorname{Ran}P$、同一组 $PU_n$ 收缩强趋于 $I$，以及循环 $g=P^{-1}1$。

因此，对任意正常泛函 $\phi$，以下仍等价：
$$
\phi(PF)=B(Fh,1)\quad(F\in\mathfrak C)
$$
与有限柱上
$$
|\phi(X_u)|\le C_\phi\|P^{-1}u\|.
$$
若非零正 $\phi$ 湮灭实际单射慢符号 $S$ 的主理想，任一满足该聚合界的本稿 $P$ 就给矛盾。

尚未证明对每个这样的假想见证都能选块及系数，使聚合界成立；也未证明本稿一般 $P$ 是 $S$ 的有界右倍数，或给 R253 的 $q_m$ 非消失下界。有限块增生性和非零无穷乘积解决的是正则器的合法构造及状态锚，指定见证的配对能力仍须另证。
