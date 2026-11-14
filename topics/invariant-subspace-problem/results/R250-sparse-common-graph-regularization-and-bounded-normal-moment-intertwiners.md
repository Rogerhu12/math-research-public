# R250：稀疏逐位共同图正则化与正常矩的有界双边实现

日期：2026-11-13（UTC+8）。作者：normal_states；Astra-ISP-1cf 复核。状态：已证明的中间结论；下列定理及交织方向完整证明，原交换正则器仍未构造。本文是 [R248](R248-adaptive-walsh-damping-of-normal-annihilator-moments.md) 的加强接口，不把两个变形表示等同，也不排除一般正常湮灭者。

## 1. 实际输入和结论

沿用原 Haar 空间 $H$、Walsh 基 $\chi_F$、共轭
$C\chi_F=(-1)^{|F|}\chi_F$，以及
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad V_F1=\chi_F,\qquad \|V_j\|\le6.
$$
令 $J_j=M_{\chi_j}$。R164 的真实高位结论给
$$
V_j-J_j\longrightarrow0\quad\text{强},\qquad
V_j\longrightarrow0\quad\text{WOT}.
\tag{1.1}
$$
全部 $J_j$ 酉。这些式子在任意可数 Hilbert 放大中仍成立：先对有限个分量验证，再用统一范数界控制分量尾。

固定 $1/2<\sigma<1$，令 $\beta_j=(j+2)^{-\sigma}$。下文构造
$$
\delta_j=
\begin{cases}
1,&j\in I=\{i_n:n\ge1\},\\
\beta_j,&j\notin I,
\end{cases}
\qquad i_1<i_2<\cdots,\quad i_n\ge2^n,
\tag{1.2}
$$
使 $D=D_\delta$，$D\chi_F=\delta_F\chi_F$，满足新的共同图结论：

**定理1。** 给定任意可数族 $f_\nu\in H$，可以选择同一个 (1.2)，使每个 R34 的最小闭轨道乘子
$$
M_{f_\nu}:\ p(A)1\longmapsto p(A)f_\nu
$$
都满足
$$
DH\subset\operatorname{Dom}M_{f_\nu},\qquad M_{f_\nu}D\in B(H).
\tag{1.3}
$$
它不是交换正则器：$D\notin A'$。

**定理2。** 对任意正常泛函 $\phi$，可以选择同一个 (1.2)，并构造有界 $C$-对称算子 $H_{\phi,\delta}\in B(H)$，使
$$
B(H_{\phi,\delta}\chi_G,\chi_F)
 =\delta_F\delta_G\,\phi(V_FV_G).
\tag{1.4}
$$
其中 $B(u,v)=\langle u,Cv\rangle$。特别
$$
H_{\phi,\delta}1=h_\delta,\qquad
\langle H_{\phi,\delta}1,1\rangle=\phi(I).
\tag{1.5}
$$
这里 $h_\delta$ 正是 R248 的阻尼矩向量。

设 $A^+=DAD^{-1}$、$A^-=D^{-1}AD$ 分别表示下面验证的有界实际变形；对 $S=S_N,S_Y$ 同样记 $S^+,S^-$。则
$$
A^+H_{\phi,\delta}=H_{\phi,\delta}A^-,
\qquad
S^+H_{\phi,\delta}=H_{\phi,\delta}S^-.
\tag{1.6}
$$
若 $\phi(S\mathcal A)=0$，则更有
$$
\boxed{S^+H_{\phi,\delta}=H_{\phi,\delta}S^-=0.}
\tag{1.7}
$$
对于非零正正常泛函，$H_{\phi,\delta}\ne0$。

这比一个非零 $h_\delta\in\ker S^+$ 多给出一个全域有界的双边矩实现；但它的输入和输出属于相反阻尼的表示，不能因此推出原 $S$ 的强主理想单位。

## 2. 紧合成上的高位两份渐近正交

令 $\mathcal K$ 为 $H$ 的有限或可数放大，$\widetilde V_j,\widetilde J_j$ 为对应对角放大。

**引理2.1。** 对任意紧算子 $T:H\to\mathcal K$，
$$
\|[T,\widetilde V_jT]\|\longrightarrow\|T\|.
\tag{2.1}
$$
这里行算子定义于 $H\oplus H$。

**证明。** 由 (1.1) 的强收敛及紧性，
$$
\|(\widetilde V_j-\widetilde J_j)T\|\to0.
$$
因为 $\widetilde J_j$ 酉，
$$
T^*\widetilde V_j^*\widetilde V_jT\to T^*T
$$
于算子范数。又 $\widetilde V_j\to0$ WOT，有限秩逼近两端的紧算子给
$$
T^*\widetilde V_jT\to0
$$
于算子范数。因此行算子的 Gram 矩阵按范数趋于
$$
\begin{pmatrix}T^*T&0\\0&T^*T\end{pmatrix}.
$$
取范数及平方根得到 (2.1)。这里没有错误地声称
$V_j^*V_j\to I$ 强；只在紧算子两端压缩后得到范数极限。证毕。

## 3. 逐次升级保持整个轨道 Bessel 合成

先给一个向量 $\mathbf f=(f_\nu)_\nu\in\mathcal K$。对任何只有有限多个 $\delta_j=1$、其余为 $\beta_j$ 的中间权，定义
$$
T_\delta\chi_F=\delta_F\widetilde V_F\mathbf f.
\tag{3.1}
$$
该算子是 Hilbert–Schmidt，因为
$$
\sum_F\delta_F^2\|\widetilde V_F\mathbf f\|^2
\le\|\mathbf f\|^2\prod_j(1+36\delta_j^2)<\infty.
\tag{3.2}
$$

固定一个中间权，记 $T=T_\delta$。若把尚未升级的第 $j$ 位改成1，新合成按“不含 $j$”和“含 $j$”两类列分解为
$$
T_{\mathrm{new}}=[T|_{H_{j,0}},\ \widetilde V_jT|_{H_{j,0}}],
\tag{3.3}
$$
其中 $H_{j,0}$ 是不含第 $j$ 位的 Walsh 闭子空间；第二份定义域通过
$\chi_G\leftrightarrow\chi_{G\cup\{j\}}$ 酉识别。这一式子准确使用新权1；旧的 $\delta_j$ 不出现在不含 $j$ 的列中。因此
$$
\|T_{\mathrm{new}}\|\le\|[T,\widetilde V_jT]\|
\longrightarrow\|T\|.
\tag{3.4}
$$

取正数 $\epsilon_n$ 使 $\sum_n\epsilon_n<\infty$。从 $\beta$ 开始，归纳选择尚未使用且
$i_n>\max(i_{n-1},2^n-1)$ 的高位，使第 $n$ 次升级后
$$
\|T_n\|\le(1+\epsilon_n)\|T_{n-1}\|.
\tag{3.5}
$$
这由引理2.1可行。全部中间 $T_n$ 仍为 Hilbert–Schmidt，故每一步都可继续使用引理。

式 (3.5) 给统一范数界。对每个固定有限 $F$，其权值只可能在有限多次升级中改变，所以 $T_n\chi_F$ 最终稳定。由稠密性，$T_n$ 强收敛到有界 $T_\delta$，其列仍满足 (3.1)。

对于任意可数族 $f_\nu$，先选非零标量 $c_\nu$ 使
$\sum_\nu|c_\nu|^2\|f_\nu\|^2<\infty$，再对
$\mathbf f=(c_\nu f_\nu)$ 使用上面的构造。每个分量合成
$$
T_{f_\nu,\delta}\chi_F=\delta_FV_Ff_\nu
\tag{3.6}
$$
均有界。可以同时把所需的共轭向量也放入同一个放大中。

## 4. 最小闭乘子的真实域

先说明有限 Walsh 向量属于 $\operatorname{Dom}M_f$。
$V_F\in\mathcal A$，故存在多项式 $p_k(A)\to V_F$ 于算子范数。于是
$$
p_k(A)1\to\chi_F,\qquad p_k(A)f\to V_Ff.
$$
由最小乘子的闭性，
$$
\chi_F\in\operatorname{Dom}M_f,\qquad M_f\chi_F=V_Ff.
\tag{4.1}
$$

对任意 $u\in H$，取有限 Walsh 多项式 $u_n\to u$。则
$$
Du_n\to Du,\qquad
M_fDu_n=T_{f,\delta}u_n\to T_{f,\delta}u.
$$
再次用闭性得到
$$
Du\in\operatorname{Dom}M_f,\qquad M_fDu=T_{f,\delta}u.
\tag{4.2}
$$
因此 (1.3) 是真实最小闭域上的结论，而非只在形式系数上成立。
没有需要假定所有有限 Walsh 多项式本身构成 $M_f$ 的图核心。

## 5. 两个相反阻尼的实际有界表示

R248 的局部 carry 展开可同时用于权 $\delta$ 和倒数权。若局部项支撑在
$[j,r]$，其有限局部对角相似或逆相似的条件数都至多
$$
\prod_{\ell=j}^r\delta_\ell^{-1}
\le(r+2)^{\sigma(r-j+1)}.
\tag{5.1}
$$
对 $r>j$ 的实际 carry 系数有
$$
\alpha_r/\alpha_j\le e^{-770\,16^{r-1}}.
\tag{5.2}
$$
所以两方向的全部局部级数按范数绝对收敛。由此定义实际有界
$A^+,A^-,N_j^+,N_j^-,V_j^+,V_j^-$，保留所有平方递推及有理函数关系。

两方向的 $N_j^\pm,Y_j^\pm$ 都有
$$
\|N_j^\pm\|+\|Y_j^\pm\|\le C\delta_j^{-1}+e_j
$$
的界，其中高位误差 $e_j\to0$。因
$\sum_j(j+1)^{-2}\delta_j^{-1}<\infty$，
两种 $S^\pm$ 也都按范数收敛。这里有限低位只贡献有限常数。

准确交织为
$$
DA=A^+D,\qquad A D=D A^-,
$$
$$
DS=S^+D,\qquad S D=D S^-.
\tag{5.3}
$$
由于原 $A,S$ 都 $C$-对称，且 $D$ 与 $C$ 交换，
$$
(A^-)^\top=A^+,\qquad(S^-)^\top=S^+,
\qquad X^\top=CX^*C.
\tag{5.4}
$$
这也可直接比较有限 Walsh 矩阵后用有界性延拓。

合成算子的正确方向是
$$
\boxed{
T_{f,\delta}A^-=A T_{f,\delta},\qquad
T_{f,\delta}S^-=S T_{f,\delta}.
}
\tag{5.5}
$$
例如写 $S\chi_F=\sum_Gc_G\chi_G$。R248 已证明
$\sum_G6^{|G|}|c_G|<\infty$，以及准确算子式
$SV_F=\sum_Gc_GV_G$。故
$$
T_{f,\delta}S^-\chi_F
=\sum_G\frac{\delta_F}{\delta_G}c_G\delta_GV_Gf
=\delta_FSV_Ff
=ST_{f,\delta}\chi_F.
$$
左侧用 $S^-\chi_F$ 的 Hilbert 展开和有界合成取极限；右侧的重排由上述绝对和支付。
$A$ 的局部展开满足同样条件。有限 Walsh 向量稠密，得到 (5.5)。

## 6. 正常泛函的有界双边矩

任意正常泛函可写成
$$
\phi(T)=\sum_{\nu\ge1}\langle T f_\nu,g_\nu\rangle,\qquad
\sum_\nu\|f_\nu\|^2<\infty,\quad
\sum_\nu\|g_\nu\|^2<\infty.
\tag{6.1}
$$
例如由迹类的奇异值展开，把奇异值的平方根分别分配给两端。正泛函可取 $g_\nu=f_\nu$。

令 $\mathbf f=(f_\nu)$、$\mathbf{Cg}=(Cg_\nu)$，选择第3节同一个 $\delta$，使两个放大合成
$$
T_{\mathbf f,\delta},\quad T_{\mathbf{Cg},\delta}:H\to\mathcal K
$$
均有界。令 $\mathcal C$ 为 $\mathcal K$ 的逐分量共轭，定义矩形转置
$$
T^\top=C T^*\mathcal C.
$$
它是有界线性算子，并满足
$B(T^\top u,v)=\mathcal B(u,Tv)$，其中
$\mathcal B(\mathbf u,\mathbf v)=\sum_\nu B(u_\nu,v_\nu)$。

置
$$
\boxed{
H_{\phi,\delta}
=T_{\mathbf{Cg},\delta}^{\top}T_{\mathbf f,\delta}.
}
\tag{6.2}
$$
于是
$$
\begin{aligned}
B(H_{\phi,\delta}\chi_G,\chi_F)
&=\delta_F\delta_G\sum_\nu
B(V_Gf_\nu,V_F Cg_\nu)\\
&=\delta_F\delta_G\sum_\nu
\langle V_FV_G f_\nu,g_\nu\rangle\\
&=\delta_F\delta_G\phi(V_FV_G).
\end{aligned}
\tag{6.3}
$$
中间步骤只用真实 $C$-对称性；级数由两端平方可和及有界算子控制。
由于 $V_F,V_G$ 交换，(6.3) 对 $F,G$ 对称，故
$H_{\phi,\delta}^\top=H_{\phi,\delta}$。

取 $G=\varnothing$，得到其第一列
$$
H_{\phi,\delta}1
=\sum_F(-1)^{|F|}\delta_F\phi(V_F)\chi_F,
$$
即 R248 的 $h_\delta$。

把 (5.5) 在适当矩形方向转置，再用 (5.4)，可得
$$
A^+H_{\phi,\delta}=H_{\phi,\delta}A^-,
\qquad
S^+H_{\phi,\delta}=H_{\phi,\delta}S^-.
$$
也可对两端 Walsh 矩阵逐项使用 (6.3) 核对。

若 $\phi(S\mathcal A)=0$，则 $SV_FV_G\in S\mathcal A$，所以
$$
\begin{aligned}
B(S^+H_{\phi,\delta}\chi_G,\chi_F)
&=\mathcal B(S^{(\infty)}T_{\mathbf f,\delta}\chi_G,
                  T_{\mathbf{Cg},\delta}\chi_F)\\
&=\delta_F\delta_G\phi(SV_FV_G)=0.
\end{aligned}
$$
完全性和有界性给 (1.7)。特别
$$
\operatorname{Ran}H_{\phi,\delta}\subset\ker S^+,\qquad
\overline{\operatorname{Ran}S^-}\subset\ker H_{\phi,\delta}.
\tag{6.4}
$$

## 7. 仍然不能推出的结论

1. $H_{\phi,\delta}$ 一般不是 Hilbert 正算子，即使 $\phi\ge0$。式 (6.3) 是不含星号的解析双边矩，不是 Gram 矩阵 $\phi(V_F^*V_G)$。不能借正性改写它。
2. $H_{\phi,\delta}$ 交织 $A^-$ 与 $A^+$，一般不在原 $A'$ 中。
3. 原 $S$ 单射、稠密像经 (5.3) 只给 $S^-$ 单射和 $S^+$ 稠密像；并不给 $S^-$ 稠密像或 $S^+$ 单射。因此 (1.7) 尚不迫 $H_{\phi,\delta}=0$。
4. $D$ 保留无限多个无阻尼位，故 R248 的高幂强单位仍在两个变形中成立；但纯两位拼接附录已排除“仅靠此性质就证明慢核为零”。
5. 对任意非零原交换子 $R$，不可能有 $RH\subset\operatorname{Ran}D=\operatorname{Dom}D^{-1}$，见 R248 §6。因此不能通过 $R=DQ$（$Q$ 有界）把本共同图正则器补成所需的原交换子。

新结论是：任意可数个真实闭轨道乘子都可同时被一个保留无限多个无阻尼位的 Walsh 噪声从右正则化；任意正常泛函因此有一个全域有界、$C$-对称的阻尼双边矩实现。假想慢理想湮灭者还迫该算子在相反阻尼的两个真实表示之间两侧被慢符号杀掉。当前仍缺把这条双边结构转回原表示，或从真实正常矩方程导出 $S^+$ 的特殊核不能出现。
