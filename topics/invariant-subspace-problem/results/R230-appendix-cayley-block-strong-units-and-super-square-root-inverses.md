# R230 附录：Cayley尾块收缩强单位与超平方根次数逆增长

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065；有限块估计由 normal_next 给出。AI-assisted，GPT-6 Astra Pro。

**状态：已证明的中间结论。** 本文构造原 Haar 交换子中的一类非零收缩 $P$，它有真正收缩强单位、$1\in\operatorname{Ran}P$，而逆在有限 Walsh 次数上的增长严格超过任何 $\exp(C\sqrt q)$。因此它超出 R230/R261 的规范正一阶预解式乘积族。没有证明它是慢符号的分母，也没有为任意正常湮灭者完成专属配对。

并行主线 [R267第一附录](../results/R267-appendix-summable-vacuum-drift-and-super-square-root-inverse-growth.md) 已有超平方根逆构造，[R267第二附录](../results/R267-appendix-blaschke-block-strong-units-and-linear-degree-inverse-type.md) 更已给线性次数逆下型。本稿是直接用实际 $N_j$ 的收缩Cayley因子、再以自适应有限柱逼近构造乘积的独立完整实现；不把越过平方根界重复计为新范围，也不声称本稿下界强于线性下型。其可复用步骤是不用准确块乘积公式的正交增量收敛，以及靠实际扩张性处理全部未选逆因子。

## 1. 原模型、列代数及定理

保持原实际
$$
H=L^2(\mathbb Z_2),\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
\mathfrak C=\{A\}'.
$$
$1$ 对 $A$ 循环。每个有限 Walsh 柱 $u$ 有实际有界列算子
$X_u\in\mathcal A$，满足 $X_u1=u$。实际归一化幂和纯比较矩阵满足
$$
N_j=A^{2^j}/d_j,\qquad
\|N_j-E_j\|\le\eta_j,\qquad
\|N_j\|=\|E_j\|=1,\qquad
E_j=e_{10}^{(j)},\quad
\eta_j\le e^{-770\,16^j}.
\tag{1.1}
$$
纯 $E_j$ 仅用作已知有限局部比较；最终所有因子均用实际 $N_j$ 定义。

**定理。** 存在 $P\in\mathfrak C$ 和 $U_n\in\mathcal A$，使
$$
\boxed{
\|P\|\le1,\quad
1\in\operatorname{Ran}P,\quad
PU_n\longrightarrow I\ {\rm SOT},\quad
\|PU_n\|\le1.
}
\tag{1.2}
$$
$P$ 单射且像稠密，$g=P^{-1}1$ 是实际 $A$ 的循环向量。
令 $G=P^{-1}$，则全部有限 Walsh 柱属于 $\operatorname{Dom}G$。

存在有限 Walsh 字符 $\chi_n$，其次数 $q_n\asymp n^{19/10}$，以及固定 $c>0$，满足充分大 $n$ 时
$$
\boxed{
\|\chi_n\|=1,\qquad
\|G\chi_n\|
\ge
\exp\!\left(cq_n^{10/19}\log q_n\right).
}
\tag{1.3}
$$
因而对每个固定 $C>0$，
$$
\frac{\|G\chi_n\|}{e^{C\sqrt{q_n}}}\longrightarrow\infty.
\tag{1.4}
$$
这里不预设 $G$ 在完整的每个有限次数空间上有界；下界已经在明确的有限柱上成立。

## 2. 已支付的有限块估计

使用[有限块 Cayley 完整证明](../results/R230-appendix-finite-block-cayley-vacuum-and-walsh-gain.md)。在任意 $Q$ 位块上令
$$
K_Q^0=\frac2{Q+1}\sum_{j\in I}E_j,\qquad
F_Q^0=(I-K_Q^0)(I+K_Q^0)^{-1}.
$$
$K_Q^0$ 是幂零收缩，$F_Q^0$ 增生，即 $\operatorname{Re}F_Q^0\ge0$。
块常数向量记为 $\Omega$，全块 Walsh 字符记为 $\chi_I$。完整估计为
$$
\|F_Q^0\Omega\|\le\frac{10}{\sqrt{Q+1}},\qquad
0\le\langle F_Q^0\Omega,\Omega\rangle\le\frac4{Q+1},
\tag{2.1}
$$
$$
\|F_Q^0\chi_I\|\ge c_0\sqrt Q,\qquad
c_0=\frac{\sqrt3}{8e},\qquad
\|F_Q^0\|\le2Q+1.
\tag{2.2}
$$
均值为实数。对 $\lambda>0$，$R^0=I+\lambda F_Q^0$ 可逆且扩张，
$$
\|R^0x\|\ge\|x\|,\qquad
\|(R^0)^{-1}\|\le1,\qquad
\|R^0\chi_I\|\ge c_0\lambda\sqrt Q.
\tag{2.3}
$$
置
$$
\mu=\langle (R^0-I)\Omega,\Omega\rangle,\qquad
\sigma^2=\|R^0\Omega-(1+\mu)\Omega\|^2.
$$
则
$$
0\le\mu\le\frac{4\lambda}{Q+1},\qquad
\sigma^2\le\frac{100\lambda^2}{Q+1},
\tag{2.4}
$$
$$
\|R^0\Omega\|=\sqrt{(1+\mu)^2+\sigma^2}.
\tag{2.5}
$$

关键实际扰动也已支付。对远物理块 $I=\{h,\ldots,h+Q-1\}$，取
$$
\varepsilon=e^{-770\,16^h},\qquad
K^{\rm act}=\frac{2\sum_{j\in I}N_j}{Q+1+2Q\varepsilon}.
\tag{2.6}
$$
$K^{\rm act}$ 是真实 $\mathcal A$ 中的收缩，谱为 $\{0\}$，且
$\|K^{\rm act}-K_Q^0\|\le4\varepsilon$。
定义
$$
F^{\rm act}=(I-K^{\rm act})(I+K^{\rm act})^{-1},\qquad
R^{\rm act}=I+\lambda F^{\rm act}.
$$
它们均属于 $\mathcal A$，$F^{\rm act}$ 增生，$R^{\rm act}$ 可逆且扩张，其逆为收缩。若 $4\varepsilon(Q+1)\le1/2$，则
$$
\boxed{\|R^{\rm act}-R^0\|\le16\lambda(Q+1)^2\varepsilon.}
\tag{2.7}
$$
因此块起点可以同时超过任意指定有限头，并使实际误差小于任意事先给定的正数。

这些因子的可逆性发生在实际 $\mathcal A$ 内：$K^{\rm act}$ 是 $A$ 的零常数多项式；$I+K^{\rm act}$ 及
$(1+\lambda)I+(1-\lambda)K^{\rm act}$ 的常数字符都非零。没有使用纯块的幂零性来定义真实逆。

## 3. 参数和每步自适应物理位置

固定
$$
Q_i=\lceil i^{9/10}\rceil,\qquad
\lambda_i=i^{-1/5},\qquad
e_i=2^{-i},\qquad
\delta_i=e^{-i^3},\quad i\ge1.
\tag{3.1}
$$
只依赖块形状的纯算子范数上界记为
$$
L_i=1+\lambda_i(2Q_i+1).
$$
由 (2.4)，相应纯均值和方差满足
$$
0\le\mu_i\le4i^{-11/10},\qquad
\sigma_i^2\le100i^{-13/10}.
\tag{3.2}
$$
两个级数都收敛。令
$$
r_i=\sqrt{(1+\mu_i)^2+\sigma_i^2}.
$$
则
$$
1\le r_i\le1+\mu_i+\tfrac12\sigma_i^2,\qquad
\sum_i(r_i-1)<\infty.
\tag{3.3}
$$

归纳构造互不相交且严格向高位移动的物理块 $I_i$、实际因子 $R_i$ 和向量
$$
g_0=1,\qquad g_i=R_i g_{i-1}.
$$
已知 $g_{i-1}\in H$ 后，选一个有限头长度 $h_i$，超过此前全部块的终点，并使
$$
a_i=\Pi_{h_i}g_{i-1},\qquad
\|g_{i-1}-a_i\|
\le\frac{e_i}{2(1+L_i)}.
\tag{3.4}
$$
有限柱条件期望强趋恒等，故这种选择总能实现。再在 $h_i$ 之后选一个连续的 $Q_i$ 位块 $I_i$，远到 (2.7) 给
$$
\|R_i-R_i^0\|\le\delta_i,
\tag{3.5}
$$
其中 $R_i^0$ 是同块的纯比较因子。
所有选择在此之前的数据确定后作出，不改变原权、不置换未知子空间。

特别，每个 $R_i$ 是实际 $\mathcal A$ 中的可逆扩张算子。所有 $R_i$ 彼此交换；但证明不会假设它们与纯比较因子或条件期望交换。

## 4. 真正向量乘积的收敛

先证明 $\sup_i\|g_i\|<\infty$。因 $a_i$ 不依赖新块，
$$
\|R_i^0a_i\|=r_i\|a_i\|.
$$
用 (3.4)—(3.5)，
$$
\begin{aligned}
\|g_i\|
&\le\|R_i^0a_i\|+
 \|R_i^0(g_{i-1}-a_i)\|+
 \|(R_i-R_i^0)g_{i-1}\|\\
&\le(r_i+\delta_i)\|g_{i-1}\|+\frac12e_i.
\end{aligned}
\tag{4.1}
$$
$\sum_i(r_i+\delta_i-1)<\infty$、$\sum_i e_i<\infty$，故逐次迭代给某个固定有限 $M$，
$$
\boxed{\sup_i\|g_i\|\le M.}
\tag{4.2}
$$
这一步不把各 $R_i$ 的全空间范数乘起来。

现在分解增量：
$$
g_i-g_{i-1}=\mu_i a_i+v_i+\zeta_i,
\tag{4.3}
$$
其中
$$
v_i=(R_i^0-(1+\mu_i)I)a_i,
$$
$$
\zeta_i=(R_i-R_i^0)g_{i-1}+
(R_i^0-I)(g_{i-1}-a_i).
$$
有
$$
\sum_i\|\mu_i a_i\|\le M\sum_i\mu_i<\infty,
\qquad
\|\zeta_i\|\le M\delta_i+\tfrac12e_i,
\tag{4.4}
$$
所以误差级数也按范数绝对收敛。

$v_i$ 是有限柱，其对前 $h_i$ 位的条件期望为零。此前所有 $v_j$、$j<i$ 都只依赖该头，所以
$$
\langle v_i,v_j\rangle=0\quad(i\ne j).
\tag{4.5}
$$
而
$$
\|v_i\|^2=\sigma_i^2\|a_i\|^2\le M^2\sigma_i^2.
$$
由 (3.2)，$\sum_i\|v_i\|^2<\infty$，故正交级数 $\sum_i v_i$ 在 $H$ 中收敛。结合 (4.3)—(4.4)，得到
$$
\boxed{g_i\longrightarrow g\in H.}
\tag{4.6}
$$
每个实际 $R_i$ 扩张，因而 $\|g_i\|\ge1$，特别 $\|g\|\ge1$。

这里既支付了实际 carry，也支付了较早向量对新物理块可能并不独立的问题。正交性只用于经过真实有限柱逼近后的 $v_i$，没有将实际 $g_{i-1}$ 错当成有限支撑向量。

## 5. 逆积的全空间强极限与循环性

记
$$
U_n=R_n\cdots R_1\in\mathcal A,\qquad
P_n=U_n^{-1}=R_1^{-1}\cdots R_n^{-1}\in\mathcal A.
$$
每个逆因子为收缩，故 $\|P_n\|\le1$。又 $U_n1=g_n$，所以
$$
P_ng_n=1,\qquad
\|P_ng-1\|\le\|g-g_n\|\longrightarrow0.
\tag{5.1}
$$

令 $M_g=\overline{\mathbb C[A]g}$。每个 $P_n\in\mathcal A$ 保持这个闭轨道，故 $P_ng\in M_g$；由 (5.1)，$1\in M_g$。原 $1$ 循环，因而
$$
\boxed{M_g=H.}
\tag{5.2}
$$
这是先证明 $g$ 循环，再建立整个空间的极限，未从一个向量上的收敛免费推出强收敛。

对任意多项式 $p$，
$$
P_n p(A)g=p(A)P_ng\longrightarrow p(A)1.
$$
$\{p(A)g\}$ 稠密且 $\sup_n\|P_n\|\le1$，遂存在收缩 $P$，使
$$
\boxed{P_n\longrightarrow P\ {\rm SOT},\qquad Pg=1.}
\tag{5.3}
$$
各 $P_n$ 交换 $A$，强极限亦然，所以 $P\in\mathfrak C$。尤其 $P\ne0$。

## 6. 同一实际强单位、逆列和完整图核心

固定 $n$，当 $k\ge n$ 时，实际因子的交换性给
$$
P_kU_n=\prod_{i=n+1}^kR_i^{-1},
\qquad \|P_kU_n\|\le1.
$$
令 $k\to\infty$，得到
$$
\|PU_n\|\le1.
\tag{6.1}
$$
并且
$$
PU_n1=Pg_n\longrightarrow Pg=1.
$$
$PU_n$ 交换 $A$，$1$ 循环，(6.1) 遂给
$$
\boxed{PU_n\longrightarrow I\ {\rm SOT}.}
\tag{6.2}
$$
它们是所需的真正收缩强单位，$U_n$ 本身不要求一致有界。

若 $Px=0$，则由交换性和 (6.2)，
$x=\lim_nPU_nx=\lim_nU_nPx=0$。
又每个 $PU_nH\subseteq\operatorname{Ran}P$，所以 $P$ 像稠密。
定义实际闭稠密逆
$$
G=P^{-1},\qquad\operatorname{Dom}G=\operatorname{Ran}P.
$$
它的闭性直接来自 $P$ 有界。

对每个有限 Walsh 柱 $u$，
$$
P X_u g=X_uPg=X_u1=u,
$$
故
$$
\boxed{u\in\operatorname{Dom}G,\qquad Gu=X_ug.}
\tag{6.3}
$$
还准确有
$$
U_nu=X_ug_n\longrightarrow X_ug=Gu.
\tag{6.4}
$$
这里使用实际交换性，未把 $U_n$ 当作对所有 $H$ 向量有界收敛的算子族。

R244 聚合逆图附录的全部假设现已满足。为明确图核心，也可直接证明：$g$ 循环，且 R88 的有界强列逼近使 $\{X_ug:u\text{ 为有限柱}\}$ 稠密。给定 $v\in H$，取这些向量趋于 $v$，相应的 $u=P X_ug$ 趋于 $Pv$，而 $Gu=X_ug\to v$。所以全部有限柱是 $G$ 的完整图核心，且 $G=X_g$ 是原最小闭乘子。

## 7. 远段 Walsh 字符的实际逆增长

对整数 $n$，取远段块 $i=n,\ldots,2n$，令
$$
\chi_n=\prod_{i=n}^{2n}\chi_{I_i},\qquad
q_n=\sum_{i=n}^{2n}Q_i.
\tag{7.1}
$$
块彼此不交，所以 $\chi_n$ 是范数为 $1$ 的单个有限 Walsh 字符，次数恰为 $q_n$，并且
$$
q_n\asymp n^{19/10}.
\tag{7.2}
$$

纯因子在互不相交的块上张量分解。由 (2.3)，
$$
\begin{aligned}
\left\|\prod_{i=n}^{2n}R_i^0\chi_n\right\|
&=\prod_{i=n}^{2n}\|R_i^0\chi_{I_i}\|\\
&\ge\prod_{i=n}^{2n}c_0\lambda_i\sqrt{Q_i}\\
&\ge c_0^{n+1}n^{(n+1)/4}.
\end{aligned}
\tag{7.3}
$$
这里 $9/20-1/5=1/4$。充分大 $n$ 时，(7.3) 至少为 $\exp((n\log n)/8)$。

这个下界必须送回实际因子。由
$$
\|R_i^0\|\le1+\lambda_i(2Q_i+1)\le6i^{7/10},
\qquad
\|R_i\|\le7i^{7/10},
$$
对两个有限乘积作望远镜差分，(3.5) 给
$$
\begin{aligned}
\left\|
\prod_{i=n}^{2n}R_i-\prod_{i=n}^{2n}R_i^0
\right\|
&\le(n+1)e^{-n^3}
 \bigl(7(2n)^{7/10}\bigr)^n\\
&\le e^{-n^3/2}
\end{aligned}
\tag{7.4}
$$
对充分大 $n$ 成立。这不要求真实因子与纯因子互相交换。
因此
$$
\left\|\prod_{i=n}^{2n}R_i\chi_n\right\|
\ge\exp((n\log n)/16)
\tag{7.5}
$$
对充分大 $n$ 成立。

最后不能忽略未选中的早、晚因子。它们不需要误差比较：所有实际 $R_i$ 互换且各自扩张。对每个 $k\ge2n$，可将选中段移到最右侧，余下因子的乘积仍扩张，于是
$$
\|U_k\chi_n\|
\ge\left\|\prod_{i=n}^{2n}R_i\chi_n\right\|.
\tag{7.6}
$$
固定 $n$ 后用 (6.4) 令 $k\to\infty$，得到
$$
\|G\chi_n\|\ge\exp((n\log n)/16).
\tag{7.7}
$$
(7.2) 将它转成 (1.3)。因为 $10/19>1/2$，(1.4) 随即成立。

## 8. 一个可调的严格超平方根区间

同一证明不局限于 (3.1) 的具体指数。取
$$
\frac23<a<1,\qquad
1-\frac a2<s<a,\qquad
Q_i=\lceil i^a\rceil,\qquad
\lambda_i=i^{a/2-s}.
\tag{8.1}
$$
此时
$$
\mu_i=O(i^{-s-a/2}),\qquad
\sigma_i^2=O(i^{-2s}),
$$
两者可和；$s>1/2$ 由 (8.1) 自动保证。每个纯块的 Walsh 增益至少 $c\,i^{a-s}$，其中 $a-s>0$。所有因子范数只有多项式增长，故同一 $e^{-i^3}$ carry 预算继续足够。

于是对相应构造出的 $P$，
$$
q_n\asymp n^{1+a},\qquad
\|P^{-1}\chi_n\|\ge
\exp(cq_n^\beta\log q_n),\qquad
\beta=\frac1{1+a}\in(1/2,3/5).
\tag{8.2}
$$
对区间中每个固定 $\beta$ 都可构造一个这样的 $P$。没有声称同一个 $P$ 同时实现所有端点，也没有声明 $3/5$ 是所有可能正则器的极限。

## 9. 与已证障碍及实际开放问题的关系

R230/R261 的规范正一阶无穷预解式乘积，在每个完整次数 $\le q$ 空间上的逆成本是 $\exp(o(\sqrt q))$。本稿 (1.3) 已在单个有限柱上违反任何 $\exp(C\sqrt q)$ 上界。因此本稿 $P$ 不能属于该规范族，包括乘非零常数后的同一族。

新因子是实际有限尾块收缩的 Cayley 变换，再取增生预解式。它们的可控低真空扰动、允许很大的其他向量增益，以及相邻物理块间的自适应选择，都是证明所需；不能只写“取更多一阶正因子”来替代。

$P$ 已满足 R244 聚合判据允许的全部结构条件，所以可以把它用于新的专属矩搜索：
$$
|\phi(X_u)|\le C_\phi\|P^{-1}u\|
\quad(u\text{ 为有限柱}).
$$
但 (1.3) 只给某些方向上的逆增长下界，并不提供这个对全部有限列的泛函界，更不自动给 $Pf_i\in\operatorname{Dom}X_{Cf_i}$。尚未证明任何给定正常湮灭者满足上述界。

本文也没有证明 $P\in S B(H)$、$\operatorname{Ran}P\subseteq\operatorname{Ran}S$，或 $\operatorname{Ran}P$ 包含 R263 的某个指定指数次数域。那些结论需要独立的真实值域或完整次数上界。Haar 普通不变格、一般正常湮灭者、边界 $N=M$ 以及普通 Hilbert ISP 仍开放。

## 已用完整来源

- [有限块 Cayley 估计及实际进位](../results/R230-appendix-finite-block-cayley-vacuum-and-walsh-gain.md)：本文 §2 的全部尺度、增生性和误差。
- [R244 聚合逆图判据](../results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)：结构条件满足后的正常矩接口。
- [R261 零型逆成本](../results/R261-infinite-positive-resolvent-inverses-zero-type-degree-domains.md)：与规范正一阶族的严格区别。
- R88：真实有限柱列与有界强逼近；本文不把纯矩阵代数作用移到未知限制。
