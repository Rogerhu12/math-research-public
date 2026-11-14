# 绝对收敛的形式除法仍不识别真实右移域

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整的实际域障碍，不编号。

本稿处理 R185/R187 的具体慢符号 $T_N$。结论不是 $N=M$ 的肯定或否定，
而是说明即使逐项除以一个 $B$ 后的系列绝对收敛，也不能据此声称向量属于标准右移域。
在已知的真实边界子商上，这个有非零形式常数项的除法系列甚至在一个稠密 Banach 图空间上恒为零。

## 1. 一般闭图引理：此处不需要稠密像

设 $\mathscr K\ne0$ 为 Hilbert 空间，$C\in B(\mathscr K)$ 单射且拟幂零。
取 $d_j>0$、$a\in\ell^1$，并假设
$$
N_j(C)=\frac{C^{2^j}}{d_j},\qquad
\sup_j\|N_j(C)\|\le L<\infty,
\qquad
\sum_{j\ge0}a_jN_j(C)=0
\tag{1.1}
$$
按算子范数收敛。主应用中 $L=1$、$a_j=(j+1)^{-2}$。

定义
$$
\mathscr E_C=
\left\{v\in\mathscr K:
\sum_{j\ge0}|a_j|
\left\|\frac{C^{2^j-1}v}{d_j}\right\|<\infty\right\},
$$
$$
\|v\|_{\mathscr E_C}
=\|v\|+
\sum_{j\ge0}|a_j|
\left\|\frac{C^{2^j-1}v}{d_j}\right\|.
\tag{1.2}
$$

**引理 1.1。**
$\mathscr E_C$ 是 Banach 空间，并且
$$
\boxed{\operatorname{Ran}C\subsetneq\mathscr E_C.}
\tag{1.3}
$$
对每个 $v\in\mathscr E_C$，系列
$$
\mathscr H_Cv=
\sum_{j\ge0}a_j\frac{C^{2^j-1}v}{d_j}
\tag{1.4}
$$
绝对收敛，而且
$$
\boxed{\mathscr H_Cv=0.}
\tag{1.5}
$$
若额外已知 $\operatorname{Ran}C$ 稠密，则 $\mathscr E_C$ 在 $\mathscr K$ 中稠密；
稠密像不是 (1.3)—(1.5) 的证明假设。

**证明。**
各坐标 $v\mapsto C^{2^j-1}v/d_j$ 为有界算子。
把 (1.2) 的图嵌入
$\mathscr K\oplus\ell^1(\mathscr K)$，逐坐标取极限，
即得该图闭，因此 $\mathscr E_C$ 完备。

若 $v=Cw$，则
$$
\sum_j|a_j|
\left\|\frac{C^{2^j-1}v}{d_j}\right\|
=\sum_j|a_j|\|N_j(C)w\|
\le L\|a\|_1\|w\|.
\tag{1.6}
$$
所以 $\operatorname{Ran}C\subseteq\mathscr E_C$。

$C$ 不可能有正下界：若 $\|Cx\|\ge c\|x\|$，
反复作用给 $\|C^n\|\ge c^n$，与拟幂零矛盾。
由于 $\mathscr K\ne0$，可取单位向量 $w_k$ 使
$$
\|Cw_k\|\longrightarrow0.
$$
对每个固定 $j$，
$$
N_j(C)w_k
=\frac{C^{2^j-1}}{d_j}\,Cw_k\longrightarrow0.
$$
又 $\|N_j(C)w_k\|\le L$，由 $a\in\ell^1$ 的支配求和，
$$
\boxed{
\|Cw_k\|_{\mathscr E_C}
=\|Cw_k\|+\sum_j|a_j|\|N_j(C)w_k\|
\longrightarrow0.
}
\tag{1.7}
$$

若反而有 $\mathscr E_C\subseteq\operatorname{Ran}C$，
则 $C^{-1}:\mathscr E_C\to\mathscr K$ 是全域闭线性算子：
$v_k\to v$ 于 $\mathscr E_C$、$C^{-1}v_k\to y$ 时，
连续嵌入 $\mathscr E_C\to\mathscr K$ 及 $C$ 有界给 $Cy=v$；
单射性识别该逆。闭图定理遂给
$\|C^{-1}v\|\le K\|v\|_{\mathscr E_C}$。
把 $v=Cw_k$ 代入，与 (1.7)、$\|w_k\|=1$ 矛盾。
故 (1.3) 严格成立。

最后，(1.4) 绝对收敛，允许左乘有界 $C$：
$$
C\mathscr H_Cv
=\sum_j a_jN_j(C)v=0.
$$
由 $C$ 单射，得 (1.5)。证毕。

若 $a_0\ne0$，(1.4) 的形式常数项是 $(a_0/d_0)I$，
但整个实际系列在上述域上为零。
这没有提供一个有界、忠实的形式幂级数演算；
不能把“形式单位”一词直接变成它在此域上的可逆性。

## 2. 本题真实子商：稳定闭像的来源

以下固定
$$
T_N=\sum_{j\ge0}a_jN_j^-,\qquad
N_j^-=\frac{B^{2^j}}{d_j},\qquad
a_j=(j+1)^{-2},
$$
$$
M=\ker T_N,\qquad N=\overline{BM}.
$$
R185/R187 已证明 $N$ 无限维、$e_0\in N$，以及
$$
M\cap\ker B^r=\mathbb Ce_0\quad(r\ge1).
\tag{2.1}
$$

这里明确重述稳定闭像，避免仅从 $N=\overline{BM}$ 推出稠密像。
R187 的商代数 $\mathcal A/\overline{S_N\mathcal A}$ 中，
根理想 $\mathcal R$ 满足
$$
\overline{b^r\mathcal Q}=\mathcal R\quad(r\ge1).
$$
把这个范数闭理想等式送入 $M$ 上的连续表示，
R187 式(5.2)—(5.3) 得
$$
\overline{B^rM}=N\quad(r\ge1).
\tag{2.2}
$$
再由 $B$ 有界，
$$
\boxed{
\overline{BN}
=\overline{B\,\overline{BM}}
=\overline{B^2M}
=N.
}
\tag{2.3}
$$
(2.2) 是额外已证明的稳定性；它不是未知的 $N=M$。

在无限维 Hilbert 商
$$
\mathscr K=N/\mathbb Ce_0
$$
上令 $C$ 为 $B$ 的诱导算子。
若 $Cx=0$，取代表 $y\in N$，则 $By\in\mathbb Ce_0$，
所以 $B^2y=0$；(2.1) 给 $y\in\mathbb Ce_0$，故 $C$ 单射。
(2.3) 给 $C$ 稠密像。
同时
$$
\|C^r\|\le\|B^r\|,\qquad
\|N_j(C)\|\le1,
$$
所以 $C$ 拟幂零。$T_N$ 在 $N$ 上为零，故
$$
\sum_j a_jN_j(C)=0.
\tag{2.4}
$$
全部条件已经实际核实；这就是 R187 §7 的真实 quasiaffine 子商。

于是引理 1.1 给一个稠密 Banach 图空间
$$
\boxed{\operatorname{Ran}C\subsetneq\mathscr E_C\subseteq\mathscr K}
\tag{2.5}
$$
且 (1.4) 在其中恒为零。
特别，绝对收敛的逐项除法并不要求输入属于 $\operatorname{Ran}C$。

## 3. 原边界的闭像部分也有严格域分离

这一现象还可以在 $N\subseteq\mathcal H_-$ 中表达，不必仅留在子商。
定义
$$
\mathscr E_N=
\left\{x\in N:
\sum_j a_j\left\|\frac{B^{2^j-1}x}{d_j}\right\|<\infty\right\},
$$
赋予原范数加该级数的 Banach 图范数。其完备性同 §1。

显然
$$
BN\subseteq\mathscr E_N,\qquad e_0\in\mathscr E_N.
\tag{3.1}
$$
第一项由
$B^{2^j-1}(By)/d_j=N_j^-y$ 及 $\|N_j^-\|\le1$ 得到；
第二项因为 $j\ge1$ 时正次幂杀掉 $e_0$，只剩 $j=0$ 的一项。
(2.3) 因而说明 $\mathscr E_N$ 在 $N$ 中稠密。

令 $J_1$ 为 R200 的真正标准右移：
$$
J_1x=\sum_{n\ge0}
\frac{x_n}{\alpha_{v_2(n+1)}}e_{n+1}.
$$

若 $x\in N\cap\operatorname{Dom}J_1$，则
$B^{2^j-1}x/d_j=N_j^-J_1x$，因此
$\sum_j a_j\|B^{2^j-1}x/d_j\|\le\|a\|_1\|J_1x\|$。
这先给 $N\cap\operatorname{Dom}J_1\subseteq\mathscr E_N$。

**命题 3.1。**
$$
\boxed{N\cap\operatorname{Dom}J_1\subsetneq\mathscr E_N.}
\tag{3.2}
$$

证明：先构造单位 $y_k\in N\cap e_0^\perp$，使 $By_k\to0$。
由 §2 的单射拟幂零 $C$ 取单位商向量 $w_k$，满足 $Cw_k\to0$。
以正交代表实现商，取其单位提升 $y_k\in N\ominus\mathbb Ce_0$。
单射性保证 $w_k\rightharpoonup0$：
任意弱聚点被 $C$ 杀掉，只能为零；Hilbert 弱序列紧性给整个有界序列弱趋零。
因此 $y_k\rightharpoonup0$。
商范数给
$$
P_{e_0^\perp}By_k\to0,
$$
而 $\langle By_k,e_0\rangle\to0$ 由弱收敛及 $B$ 有界得到。
故 $By_k\to0$。

和 (1.7) 一样，固定 $j$ 后先用 $By_k\to0$，再以 $\ell^1$ 尾支配，得到
$$
\boxed{\|By_k\|_{\mathscr E_N}\longrightarrow0.}
\tag{3.3}
$$
另一方面，实际右移恒等式给
$$
J_1By_k=y_k-P_{\mathbb Ce_0}y_k=y_k.
\tag{3.4}
$$
所以 $\|J_1By_k\|=1$。

若 $\mathscr E_N\subseteq\operatorname{Dom}J_1$，
则 $J_1:\mathscr E_N\to\mathcal H_-$ 全域且闭，
因为 $\mathscr E_N$ 连续嵌入原 Hilbert 空间、$J_1$ 在原空间上闭。
闭图定理与 (3.3)—(3.4) 矛盾。
因此 (3.2) 成立。证毕。

故存在真实 $x\in N\subseteq M$，
其逐项除法系列绝对收敛，但 $x\notin\operatorname{Ran}B$。
本论证给出严格存在性，不声称已经算出这样一个 $x$ 的全部坐标。

## 4. 绝对除法系列的最大非可闭性

在 $\mathscr E_N$ 上置
$$
\mathscr H_Nx=\sum_j a_j\frac{B^{2^j-1}x}{d_j}.
\tag{4.1}
$$
这是从 Banach 图空间 $\mathscr E_N$ 到 $\mathcal H_-$ 的有界线性映射。
由于 $T_Nx=0$，
$$
B\mathscr H_Nx=T_Nx=0.
$$
所以 $\mathscr H_Nx\in\mathbb Ce_0$。再由 (3.1)，
$$
\mathscr H_N(By)=T_Ny=0\quad(y\in N),\qquad
\mathscr H_Ne_0=(a_0/d_0)e_0\ne0.
\tag{4.2}
$$

把 (4.1) 改看作原 Hilbert 空间 $N$ 中的稠密定义线性映射，
则其图闭包准确为
$$
\boxed{\overline{\mathcal G(\mathscr H_N)}=N\oplus\mathbb Ce_0.}
\tag{4.3}
$$
证明：$BN$ 在 $N$ 中稠密，而 (4.2) 在 $BN$ 上为零，
故图闭包含 $N\oplus0$。
它还含 $(e_0,(a_0/d_0)e_0)$；相减、数乘后含 $0\oplus\mathbb Ce_0$。
反向包含由全部输出都在闭的一维空间 $\mathbb Ce_0$ 得到。

所以即使每个输入处的级数绝对收敛，
这个形式除法映射作为原 Hilbert 空间上的算子仍不可闭。
在 $\operatorname{Dom}J_1\cap N$ 上，
它和 $T_NJ_1$ 相同；但 (3.2) 说明绝对系列还有真实右移域之外的输入。

## 5. 与饱和问题的准确关系

R200 已证明
$$
\overline{M\cap\operatorname{Dom}J_1}=N.
$$
本稿进一步说明，在已经稳定的闭像部分 $N$ 内，
绝对收敛的形式除法域仍严格越过真正右移域。
因此不能用“先逐项除以 $B$，验证绝对收敛，再作有限旗消去”
替代真实 $\operatorname{Ran}B$ 条件。

这里并未证明 $N=M$，也未证明 $N\subsetneq M$。
事实上，$\mathscr E_N$、$BN$ 和 $\operatorname{Dom}J_1\cap N$
均与 $N$ 内的稠密性相容；真正尚缺的是从这个稳定部分到整个 $M$ 的内部密度桥。


## 6. 在整个核中定义绝对域：它仍准确停留在稳定闭像部分

现在不预先要求输入属于 $N$，而定义
$$
\mathscr E_M=
\left\{x\in M:
\sum_{j\ge0}a_j
\left\|\frac{B^{2^j-1}x}{d_j}\right\|<\infty
\right\}.
\tag{6.1}
$$
本节仍取具体正系数 $a_j=(j+1)^{-2}$，特别是 $a_0\ne0$。
定义式采用原 $\mathcal H_-$ 的范数；没有把子商中的收敛当作原空间收敛。

**命题 6.1。** 有
$$
\boxed{\mathscr E_M=\mathscr E_N,\qquad
\overline{\mathscr E_M}^{\,\mathcal H_-}=N.}
\tag{6.2}
$$

证明：$\mathscr E_N\subseteq\mathscr E_M$ 显然。
若 $x\in\mathscr E_M$，则绝对收敛的和
$$
h=\sum_{j\ge0}a_j\frac{B^{2^j-1}x}{d_j}
$$
满足 $Bh=T_Nx=0$，故 $h\in\mathbb Ce_0\subseteq N$。
对每个 $j\ge1$，
$$
\frac{B^{2^j-1}x}{d_j}
=B\left(\frac{B^{2^j-2}x}{d_j}\right)\in BM\subseteq N,
$$
因为 $M$ 对 $B$ 不变。
$N$ 的闭性和级数的原空间收敛因此给
$$
\frac{a_0}{d_0}x
=h-\sum_{j\ge1}a_j\frac{B^{2^j-1}x}{d_j}\in N.
$$
于是 $x\in N$，即 $x\in\mathscr E_N$。
最后，$BN\subseteq\mathscr E_N$ 及 $\overline{BN}=N$
给出 (6.2) 的第二式。证毕。

因此，“整个核中绝对形式除法域稠密”恰与 $N=M$ 等价。
(6.2) 没有先证明该域在 $M$ 中稠密；它只精确标出未知密度的位置。

对任意 $x\in M$，所有有限除法部分和都有意义：
$$
H_nx=\sum_{j=0}^{n}a_j\frac{B^{2^j-1}x}{d_j}.
\tag{6.3}
$$

**命题 6.2。** 若 $x\in M\setminus N$，则
$$
\boxed{\|H_nx\|\longrightarrow\infty.}
\tag{6.4}
$$
等价地，若某个 $x\in M$ 的除法部分和存在一条有界子列，
则 $x\in N$。

证明：对固定 $x\in M$，$T_N$ 的算子范数级数收敛给出
$$
BH_nx=\sum_{j=0}^{n}a_jN_j^-x\longrightarrow T_Nx=0.
\tag{6.5}
$$
同时，每个 $j\ge1$ 的项属于 $BM\subseteq N$，故在 Hilbert 商
$\mathcal H_-/N$ 中，
$$
H_nx+N=\frac{a_0}{d_0}x+N
\quad\hbox{对所有 }n.
\tag{6.6}
$$

若 $\{H_{n_k}x\}$ 有界，取弱收敛子列，记其极限为 $h$。
由 (6.5) 及 $B$ 的弱连续性，$Bh=0$，
于是 $h\in\mathbb Ce_0\subseteq N$。
另一方面，商映射是有界线性映射，故弱连续；
(6.6) 迫
$$
h+N=\frac{a_0}{d_0}x+N.
$$
左边为零，因 $a_0/d_0\ne0$ 得 $x\in N$，矛盾。
因此没有有界子列。对非负实数序列 $\|H_nx\|$，
没有有界子列恰等于其趋向 $+\infty$，证明 (6.4)。证毕。

这里不声称这些范数单调。
也不声称反向命题“每个 $x\in N$ 都有一条有界除法部分和子列”成立；
$\mathscr E_N$ 中当然有完整收敛，但尚未给出整个 $N$ 的该项控制。
命题 6.2 因而是一个只向稳定闭像部分回收的必要判据，
并未排除 $M\setminus N$。
