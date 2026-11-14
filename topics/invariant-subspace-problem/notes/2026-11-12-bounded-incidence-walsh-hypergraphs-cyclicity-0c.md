# R137：任意固定次数、有限参与数 Walsh 超图的全 H 循环性

日期：2026-11-12 UTC。作者：Astra-ISP-0c017065。
状态：完整证明。高阶纯乘子按不交块分色后只有平方根次数增长；真实 carry 差为有界 C 对称扰动。适用次数 p 任意固定，不局限于二阶。

## 1. 主定理

固定整数 $p,d\ge1$。设 $\mathcal F$ 是非空有限物理位集的可数族，满足
$$
1\le |F|\le p,\qquad
\#\{F\in\mathcal F:j\in F\}\le d\quad(j\ge0).
\tag{1.1}
$$
即每个位至多参与 $d$ 个非零 Walsh 单项式。给定
$$
f=a_*+\sum_{F\in\mathcal F}a_F\chi_F,\qquad
\sum_F|a_F|^2<\infty.
\tag{1.2}
$$
则
$$
\boxed{f\ne0\quad\Longrightarrow\quad
\overline{\mathbb C[A]f}=H.}
\tag{1.3}
$$
系数允许任意复相位和任意平方可和尾，不要求 $f$ 有界或乘子有界。

更准确地，(1.2) 的实际闭乘子 $X_f$ 为 C 自伴，有限柱为图核心，且与全部有界交换子域交换。如果 $f$ 非常数，则每个 $\lambda\in\mathbb C$ 都满足
$$
\ker(X_f-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(X_f-\lambda I)}=H,
\qquad f-\lambda\text{ 循环}.
\tag{1.4}
$$

## 2. 有限分色成为不交的有限块族

把 $\mathcal F$ 看作一个图的顶点，两个不同集合相交时连边。每个
$F$ 至多与 $|F|(d-1)\le p(d-1)$ 个其他集合相交。枚举这个可数图，
依次使用前面邻居尚未占用的颜色，得到至多
$$
L=p(d-1)+1
\tag{2.1}
$$
种颜色。每个颜色类 $\mathcal F_\ell$ 内的位集两两不交。
这个贪心构造对无限图仍成立，因为每个顶点的全部邻居数已经有统一上界。

以下先估计一个不交颜色类，再有限相加。记
$$
\|a^{(\ell)}\|_2^2=\sum_{F\in\mathcal F_\ell}|a_F|^2,\qquad
\sum_{\ell=1}^L\|a^{(\ell)}\|_2
\le\sqrt L\,\|a\|_2.
\tag{2.2}
$$

## 3. 一个不交块族的纯乘子只有平方根次数增长

沿用纯一位算子
$$
S_j=I-2E_j,\qquad S_j1=\chi_j,\qquad
\|S_j\|=1+\sqrt2<3.
$$
对一个非空块 $F$，置
$$
T_F^0=\prod_{j\in F}S_j.
$$
它只作用于该有限块，满足
$$
T_F^01=\chi_F,\qquad
(T_F^0)^*1=C\chi_F=(-1)^{|F|}\chi_F,\qquad
\|T_F^0\|\le3^p.
\tag{3.1}
$$
两向量都与块真空 $1$ 正交，因为 $F$ 非空。

将每个块空间分为真空与其正交补：
$$
H_F=\mathbb C1\oplus H_F^\circ.
$$
按非真空块的个数分级；未被这些块覆盖的物理位作为不受算子作用的额外张量因子。对应等级 $n$ 的空间是对所有 $n$ 元块集合 $J$ 的正交和，每一项在 $J$ 的块中取 $H_F^\circ$，其他块取真空。

令 $P_F$ 为块真空投影、$Q_F=I-P_F$。由于 $P_FT_F^0P_F=0$，
每个局部算子恰分成：

- 创建部分 $Q_FT_F^0P_F$，将真空送到单位向量 $\chi_F$；
- 删除部分 $P_FT_F^0Q_F$，其伴随将真空送到单位向量 $(-1)^{|F|}\chi_F$；
- 内部部分 $Q_FT_F^0Q_F$，只在已经非真空的块上作用，范数至多 $3^p$。

对加权和
$$
T_\ell^0=\sum_{F\in\mathcal F_\ell}a_FT_F^0,
$$
创建部分从等级 $n$ 到 $n+1$ 的范数不超过
$\sqrt{n+1}\|a^{(\ell)}\|_2$。证明与通常无重复创建相同：
对输出块集合按被新加入的块作 Cauchy，再对输入块集合求和；局部创建向量范数为1，内部维数不影响估计。删除部分取伴随，界为
$\sqrt n\|a^{(\ell)}\|_2$。

内部部分保持每个占据块集合 $J$。在该直和分量上，
$$
\left\|\sum_{F\in J}a_FQ_FT_F^0Q_F\right\|
\le3^p\sum_{F\in J}|a_F|
\le3^p\sqrt n\,\|a^{(\ell)}\|_2.
\tag{3.2}
$$
因此在块等级不超过 $q$ 的空间上，
$$
\|T_\ell^0x\|
\le(2+3^p)\sqrt{q+1}\|a^{(\ell)}\|_2\|x\|.
\tag{3.3}
$$
对系数尾使用同样估计，证明有限系数和在这个限制空间上按算子范数收敛。

通常物理 Walsh 次数不超过 $q$ 的向量，非真空块数也不超过 $q$，
因为每个非真空块至少贡献一个非空 Walsh 坐标。因此 (3.3) 对整个
$H_{\le q}$ 成立。另一方面，每个 $T_F^0$ 是至多 $p$ 个单坐标算子的乘积，
只可能将物理次数提高至多 $p$。所以所有颜色相加后，纯乘子
$$
T_0=a_*I+\sum_Fa_FT_F^0
$$
在 $\mathcal D=\bigcup_{q\ge0}H_{\le q}$ 上良定义，并满足
$$
T_0H_{\le q}\subseteq H_{\le q+p},\qquad
\|T_0x\|\le K\sqrt{q+1}\|x\|,
\tag{3.4}
$$
其中可取
$$
K=|a_*|+(2+3^p)\sqrt L\,\|a\|_2.
$$
通常形式伴随 $T_0^\dagger=CT_0C$ 满足相同估计。这里不同颜色的算子不需要在通常伴随意义下交换；只使用有限和及共同次数界。

## 4. 纯 Dirac 的整个解析向量与 C 自伴闭包

在 $\mathcal D\oplus\mathcal D$ 上定义对称 Dirac 块
$$
\mathscr L_0=\begin{pmatrix}0&T_0^\dagger\\T_0&0\end{pmatrix}.
$$
对 $x\in H_{\le q}\oplus H_{\le q}$，(3.4) 给
$$
\|\mathscr L_0^n x\|
\le K^n\prod_{r=0}^{n-1}\sqrt{q+pr+1}\,\|x\|
\le(K\sqrt p)^n\sqrt{\frac{(q+n)!}{q!}}\,\|x\|.
\tag{4.1}
$$
因此其幂指数级数及一次算子像级数在每个有限实时间区间一致收敛，
全部 $\mathcal D\oplus\mathcal D$ 向量都是整个解析向量。

为明确所用结论，可重复 R125 §3 的自含缺陷证明：
$$
U(t)x=\sum_{n\ge0}\frac{(it)^n}{n!}\mathscr L_0^nx
$$
属于闭包的域，导数等于 $i\overline{\mathscr L_0}U(t)x$；对称性使
$\|U(t)x\|=\|x\|$。若 $\mathscr L_0^*\xi=\pm i\xi$，逐项配对给
$\langle U(t)x,\xi\rangle=e^{\pm t}\langle x,\xi\rangle$，
令相应方向的 $t$ 趋无穷便迫 $\xi=0$。两缺陷核为零，而闭对称算子的
$\pm i$ 值域由图范数恒等式闭且稠密，所以闭包自伴。

Dirac 的图范数按两个分量分解，得到
$$
\boxed{\overline{T_0}^{\,*}=C\overline{T_0}C.}
\tag{4.2}
$$
有限柱是图核心：对固定 $x\in H_{\le q}$ 取有限坐标条件期望，
(3.4) 使输入及像同时趋近；再使用 $\mathcal D$ 的闭包核心定义。

## 5. 实际 carry 差是有界算子

实际 $V_j=(I-N_j)(I+N_j)^{-1}$ 满足
$$
\|V_j\|\le6,\qquad \|V_j-S_j\|\le8\eta_j,\qquad \eta\in\ell^2.
$$
对任意 $F$，按其有限指标排序逐项 telescoping。即使混合的纯/实际因子不交换，恒等式仍给
$$
\left\|\prod_{j\in F}V_j-\prod_{j\in F}S_j\right\|
\le8\,6^{p-1}\sum_{j\in F}\eta_j.
\tag{5.1}
$$
由 $|F|\le p$ 及每个位参与至多 $d$ 次，
$$
\sum_F\left(\sum_{j\in F}\eta_j\right)^2
\le p\sum_F\sum_{j\in F}\eta_j^2
\le pd\|\eta\|_2^2.
\tag{5.2}
$$
所以
$$
K_f=\sum_Fa_F\left(\prod_{j\in F}V_j-\prod_{j\in F}S_j\right)
\tag{5.3}
$$
按算子范数绝对收敛，并满足
$$
\boxed{\|K_f\|\le8\,6^{p-1}\sqrt{pd}\,\|a\|_2\|\eta\|_2.}
\tag{5.4}
$$
实际因子彼此交换且 C 对称，纯因子也各自彼此交换且 C 对称。
因此每个差项及其范数极限均 C 对称。

置
$$
X_f=\overline{T_0}+K_f,\qquad
\operatorname{Dom}X_f=\operatorname{Dom}\overline{T_0}.
\tag{5.5}
$$
有界扰动给闭性、有限柱图核心及
$$
X_f^*=CX_fC.
\tag{5.6}
$$
有限实际乘子在 $\mathcal D$ 上趋于 $X_f$；作用于1时得到 (1.2)，故
$X_f1=f$。

## 6. 真实域交换、有限 gauge 差与循环性

对每个有界 $D\in\{A\}'$，有限实际乘子 $X_n$ 均与 $D$ 交换且 B 对称。
对 $x,z\in\mathcal D$，
$$
B(Dx,X_fz)=\lim_n B(Dx,X_nz)
=\lim_n B(DX_nx,z)=B(DX_fx,z).
$$
C 自伴和图核心使伴随定义适用，给
$Dx\in\operatorname{Dom}X_f$、$X_fDx=DX_fx$；再通过图逼近及闭性推广到全域。
因此 $X_f$ 与全部有界交换子真实域交换。

对有限柱 $u=X_u1$，
$$
X_fu=X_uf.
$$
有限柱图核心给 $\overline{\operatorname{Ran}X_f}\subseteq\operatorname{cyc}_A(f)$；
反向由 $X_fA^n1=A^nf$ 得到。所以
$$
\overline{\operatorname{Ran}X_f}=\operatorname{cyc}_A(f).
\tag{6.1}
$$

若 $\zeta^{2^m}=1$，其 gauge 只改变满足 $F\cap[0,m)\ne\varnothing$
的项。这类项至多 $dm$ 个，因此是有限个真正解析乘子的差：
$$
U_\zeta X_fU_\zeta^*=X_f+F_\zeta(A).
\tag{6.2}
$$
严格地说，先在有限部分和 $\mathcal D$ 上证明恒等式；$U_\zeta$ 双向保持
$\mathcal D$ 和有限柱，而右侧为有界扰动，所以取双方图闭包得到 (6.2)，包含域相等。

现在 R125 §9 的闭加性 cocycle 定理全部条件成立。非标量时稳定子为有限
dyadic 群，非零解析差在任意闭不变限制上像稠密；B 跨核配对使核中两两反射乘积只含有限 Fourier 模式，遍历全支撑把核压为有限维，最后由 A 单射拟幂零排除。故 (1.4) 成立。非零常数 $f$ 则直接循环，证明 (1.3)。

## 7. 明确的任意高阶、重叠且无界的例子

对任意固定 $p\ge3$，取
$$
F_j=\{j,j+1,\ldots,j+p-1\},\qquad
f=\sum_{j\ge0}\frac1{j+1}\chi_{F_j}.
\tag{7.1}
$$
每个位至多参与 $p$ 个集合，所以定理以 $d=p$ 适用。系数属于 $\ell^2$
而不属于 $\ell^1$，Walsh 集合互不相同，故 $f\in H_p$ 非零。
相邻项重叠 $p-1$ 个坐标，不是两两独立块的点态乘积。

$f$ 没有本质有界代表：前 $m$ 位条件期望在前 $m$ 位全为0的正测柱上等于
$$
\sum_{0\le j\le m-p}\frac1{j+1},
$$
随 $m$ 发散。若 $f$ 有界，所有条件期望的无穷范数应一致有界，矛盾。
所以 (7.1) 给每个固定高阶上的实际无界循环向量，其相位和尾还可任意替换为非零平方可和系数。

可再加入任意复 $\ell^2$ 第一阶项：把对应 singleton 集合并入支撑，每个位的参与数至多增加1，证明仍适用。

## 8. 一个加权分色推广

(1.1) 的统一参与数可换成如下条件：$|F|\le p$，支撑逐位局部有限，并且存在不交块颜色类的可数分解
$$
\mathcal F=\bigsqcup_{\ell\ge1}\mathcal F_\ell,\qquad
Z:=\sum_{\ell\ge1}
\left(\sum_{F\in\mathcal F_\ell}|a_F|^2\right)^{1/2}<\infty.
\tag{8.1}
$$
此时结论仍成立。

确实，§3 的纯估计对各颜色求绝对和，常数可换成
$|a_*|+(2+3^p)Z$。对每个不交颜色类，
$$
\sum_{F\in\mathcal F_\ell}\left(\sum_{j\in F}\eta_j\right)^2
\le p\|\eta\|_2^2.
$$
因此实际差范数不超过 $8\,6^{p-1}\sqrt p\,Z\|\eta\|_2$。
有限系数截断在这些界下收敛，可由对颜色的可和控制和每个颜色内的
$\ell^2$ 尾界证明。其余闭算子步骤不变；逐位局部有限性仍使每个固定 gauge
只改变有限项。

(8.1) 不由一般的 $\ell^2$ 系数或逐位局部有限支撑自动得到。本稿不声称所有固定次数向量或所有局部有限高次数向量都已循环。
一般无限参与行、无限次数及完整 ISP 仍待解决。
