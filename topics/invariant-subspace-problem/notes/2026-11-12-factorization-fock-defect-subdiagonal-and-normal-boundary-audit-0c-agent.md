# 分解与 F. & M. Riesz 接口的原始条件审查

日期：2026-11-12（UTC）。作者：literature。

状态：完整模型障碍与一个明确的商弱零充分条件，不另编号。
本稿没有证明慢符号的普遍限制稠密像，也没有否定全交换子代数可能具有独立证明的泛函分解性质。

## 1. 要解决的实际问题

记
$$
\mathfrak C=\{A\}',\qquad
\mathcal A=\overline{\mathbb C[A]}^{\|\cdot\|},
\qquad \mathfrak U=\text{实际物理 UHF 代数}.
$$
取 R185、R188 的任一慢符号
$$
S_N=\sum_{j\ge0}(j+1)^{-2}N_j,\qquad
S_Y=\sum_{j\ge0}(j+1)^{-2}N_j(I+N_j)^{-1},
$$
统一记为 $S$，并置
$$
J=\overline{S\mathcal A}^{\|\cdot\|}.
$$
它在原 Haar 空间上单射、稠密像，但 $J$ 是非标准范数闭理想。

真正尚缺的是
$$
I\in\overline{J}^{\mathrm{SOT}}
=\overline{S\mathbb C[A]}^{\mathrm{SOT}}.
\tag{1.1}
$$
这等价于 $S$ 在全部有限放大不变子商上的单射与稠密像。
有限秩泛函判据及 WOT/SOT 与正常泛函的区别，见
[既有接口笔记](../notes/2026-11-12-slow-symbol-functional-factorization-interface-and-vacuum-obstruction-0c-agent.md)。

下面只核查三种常见来源的精确假设，避免把它们误当成 (1.1) 的证明。

## 2. 标量完整 Pick 乘子定理的实际范围

已核 Davidson–Hamilton 的作者全文
[*Nevanlinna–Pick Interpolation and Factorization of Linear Functionals*](https://www.math.uwaterloo.ca/~krdavids/Preprints/DavHamNP.pdf)，
DOI [10.1007/s00020-011-1862-7](https://doi.org/10.1007/s00020-011-1862-7)。

PDF 印刷第19页 Theorem 5.2、其第20页证明及 Corollary 5.3，
给完整 Pick 核乘子代数的 $\mathbb A_1(1)$ 分解。
第20页结尾说明第一向量可取为相应乘子代数的循环向量。
证明先用全 Fock 代数的理想压缩，再传到标量完整 Pick 模型。

这不是“任意交换、有循环向量的算子代数”定理。
标量函数乘子不能直接忠实表示本题非零拟幂零 $A$：
若 $M_\varphi$ 是再生核空间的有界乘子，则
$$
M_\varphi^*k_x=\overline{\varphi(x)}\,k_x.
$$
拟幂零性迫所有有效点值为零，从而 $M_\varphi=0$。
一个有界代数同态又会把实际 $A$ 的拟幂零性保留下来，
所以不能既把 $\mathcal A$ 或 $\mathfrak C$ 送进这种标量乘子代数，又保持忠实。
完整证明也已记录在 R203 §9。

但不能据此排除一般 Fock 理想压缩：
压缩算子可以具有非零幂零或拟幂零元素。
下一节使用本模型另一条实际性质处理有限行的原表示情形。

## 3. 有限行 Fock 理想压缩必带一个非零秩一缺陷

### 3.1 全 Fock 空间与理想子空间

令
$$
\mathcal F_d=\ell^2(\mathbb F_d^+)
$$
为 $d$ 个字母的全 Fock 空间，$d\ge1$ 有限。
$\Omega$ 为真空向量，$L_i,R_i$ 分别为左右创建算子。
有
$$
L_iR_j=R_jL_i,\qquad
\sum_{i=1}^dL_iL_i^*=I-P_\Omega.
\tag{3.1}
$$

设 $\mathfrak J$ 是全 Fock 解析代数 $\mathfrak L_d$ 的弱算子闭双侧理想，
$$
M=\overline{\mathfrak J\mathcal F_d},\qquad
N=M^\perp,
$$
并假定所讨论的理想压缩非零，即 $N\ne\{0\}$。
在上述原文的理想商模型中，真理想正对应这个非零压缩。

$M$ 对全部 $L_i$ 不变。
同时，$R_i$ 与 $\mathfrak L_d$ 交换，故
$$
R_i M\subseteq M.
\tag{3.2}
$$
因而 $N$ 对全部 $L_i^*$ 不变。
令
$$
T_i=P_NL_i|_N.
$$
则
$$
T_i^*=L_i^*|_N.
$$
所以
$$
\begin{split}
I_N-\sum_{i=1}^dT_iT_i^*
&=P_N\left(I-\sum_{i=1}^dL_iL_i^*\right)|_N\\
&=P_NP_\Omega|_N\\
&=(P_N\Omega)\otimes(P_N\Omega).
\end{split}
\tag{3.3}
$$
最后一个记号表示 $x\mapsto\langle x,P_N\Omega\rangle P_N\Omega$。

### 3.2 缺陷确实非零

若 $P_N\Omega=0$，则 $\Omega\in M$。
由 (3.2)，$R_w\Omega\in M$ 对每个有限字 $w$ 成立。
这些向量形成 Fock 正交基，故 $M=\mathcal F_d$，与 $N\ne0$ 矛盾。
因此
$$
\boxed{
I_N-\sum_{i=1}^dT_iT_i^*
\text{ 是非零秩一正算子}.
}
\tag{3.4}
$$

这一步没有仅说“压缩保留一个秩一项”；
已经排除了该项可能被压成零的情形。

## 4. 原 Haar 表示不容纳这种有限行模型

R164 的实际渐近交换代数 $\mathfrak E$ 满足
$$
C^*(\mathfrak U,\mathfrak C)\subseteq\mathfrak E,\qquad
\mathfrak E\cap\mathcal K(H)=\{0\}.
\tag{4.1}
$$

若原 Haar 空间上有有限个 $T_i\in\mathfrak C$，
并存在一个酉算子把它们同时识别为第3节的非零 Fock 理想压缩，
则
$$
I-\sum_iT_iT_i^*
$$
既属于 $\mathfrak E$，又由 (3.4) 是非零有限秩算子。
这与 (4.1) 矛盾。

故
$$
\boxed{
\text{有限行、原表示酉实现的非零 Fock 理想压缩模型，
不能给本题 }\mathfrak C\text{ 提供该分解接口。}
}
\tag{4.2}
$$

同样的计算处理可数行，但须额外假定
$\sum_iT_iT_i^*$ 在原空间按算子范数收敛：
此时缺陷仍属于范数闭代数 $\mathfrak E$。
若只有强算子收敛，则不能用 (4.1)，本稿不排除这种模型。

也不排除任意非酉相似实现。
若相似度量 $G$ 恰好属于 $\mathfrak E$，则
$$
G-\sum_iT_iGT_i^*
$$
在有限行或范数收敛行的情形仍属于 $\mathfrak E$；
若它是非零有限秩，则照样矛盾。
但一个任意有界可逆相似算子并不保证这种度量属于 $\mathfrak E$，
所以不能把酉情形无条件改写为一般相似情形。

这些结论只排除指定模型来源，不否定 $\mathfrak C$ 自身的 $\mathbb A_1$ 或循环第一因子性质。

## 5. UHF 中的对角条件期望与密度障碍

### 5.1 连续 gauge 与物理对角

在低 $m$ 位物理空间上，把基标为
$r=0,\ldots,2^m-1$。
对矩阵单位定义
$$
\alpha_z(e_{rs})=z^{r-s}e_{rs},
\qquad z\in\mathbb T.
\tag{5.1}
$$
与嵌入 $X\mapsto X\otimes I$ 相容：
嵌入后的行列指标同时增加相同的 $2^m$ 倍数，差 $r-s$ 不变。
于是 (5.1) 给整个 $\mathfrak U$ 上的点范数连续圆群作用。

真实加权加一算子满足
$$
\alpha_z(A)=zA.
\tag{5.2}
$$
也可逐项从实际 carry 展开核对：每个局部项的总二进位位移都是1。

令
$$
\mathbb E_{\rm diag}(X)
=\int_{\mathbb T}\alpha_z(X)\,dm(z).
\tag{5.3}
$$
它是范数收缩的条件期望。
有限头中，只有 $r=s$ 的矩阵单位存活；
故其像是物理对角 UHF 子代数，即由有限柱事件乘法算子生成的交换 $C^*$ 代数。

由 (5.2)，
$$
\mathbb E_{\rm diag}(A^n)=0\quad(n\ge1).
$$
先对多项式，再按范数闭包，
$$
\boxed{
\mathbb E_{\rm diag}(F)=\chi(F)I
\qquad(F\in\mathcal A).
}
\tag{5.4}
$$
因此
$$
\mathbb E_{\rm diag}(\mathcal A+\mathcal A^*)
\subseteq\mathbb CI.
\tag{5.5}
$$
物理对角显然还有非标量投影。
所以 $\mathcal A+\mathcal A^*$ 不可能在 $\mathfrak U$ 中范数稠密。

这也说明“$C^*(\mathcal A)=\mathfrak U$”即使可用，
也不能替代线性空间 $\mathcal A+\mathcal A^*$ 的密度：
条件期望在两者上的像不同。

### 5.2 迹表示中的弱星密度仍失败

令 $\tau$ 为 UHF 的乘积迹，考虑有限 von Neumann 包络
$$
M_\tau=\pi_\tau(\mathfrak U)'',
\qquad
\mathcal B=\overline{\pi_\tau(\mathcal A)}^{\,w^*}.
$$
圆群作用保迹，(5.3) 延伸为正常条件期望
$$
\mathbb E_\tau:M_\tau\to D_\tau,
$$
其中 $D_\tau$ 是物理对角的弱星闭包。
由正常性与 (5.4)，
$$
\mathbb E_\tau(\mathcal B)\subseteq\mathbb CI,
\qquad
\mathbb E_\tau(\mathcal B+\mathcal B^*)\subseteq\mathbb CI.
\tag{5.6}
$$
$D_\tau$ 非标量，故
$$
\boxed{\mathcal B+\mathcal B^*\text{ 不在 }M_\tau\text{ 中弱星稠密}.}
\tag{5.7}
$$

这里讨论的是迹包络中的弱星闭包。
没有声称 (5.3) 在原 Haar 表示的整个 $B(H)$ 上是正常条件期望；
也没有用 (5.7) 直接断言原 Haar 的全 $\mathfrak C+\mathfrak C^*$ 的密度性质。

还可直接看到迹包络中的正常态扩张不唯一。
取一个迹为 $1/2$ 的非平凡物理柱投影 $p$，令
$$
h=2p-I,\qquad 0<\varepsilon<1.
$$
两个不同的正常态
$$
\omega_\pm(X)=\tau((I\pm\varepsilon h)X)
$$
在 $\mathcal B$ 上都等于 $\tau|_{\mathcal B}$：
因为 $h$ 对角且 $\tau(h)=0$，(5.6) 给 $\tau(hb)=0$。
这个结论同样只属于指定的迹表示。

### 5.3 原 Haar 表示中的有限秩见证

原 Haar 表示也有直接的弱算子密度障碍，
但须用它自己的连续泛函证明。

固定 $m\ge1$，写成物理张量分解
$$
H=\mathbb C^{2^m}\otimes H_{\ge m}.
$$
取不同的低头标准基向量 $e_h,e_k$，
并令 $\Omega_{\ge m}$ 为同一个尾常向量。
记
$$
v_h=e_h\otimes\Omega_{\ge m},
\qquad
v_k=e_k\otimes\Omega_{\ge m},
$$
以及秩至多二的正常泛函
$$
\varphi(T)=\langle Tv_h,v_h\rangle-\langle Tv_k,v_k\rangle.
\tag{5.8}
$$

真实归一化幂满足
$$
A^{2^m}=d_mN_m,\qquad
N_m=I_{<m}\otimes\widetilde N_m.
\tag{5.9}
$$
后一式是精确张量恒等式：递归
$N_m=E_m+\eta_mE_m^*N_{m+1}$
只涉及第 $m$ 位及更高位，并不含低 $m$ 位。
若 $2^m\nmid n$，$A^n$ 把低头柱 $h$ 移到另一头柱，
故
$$
\langle A^nv_h,v_h\rangle=
\langle A^nv_k,v_k\rangle=0.
$$
若 $n=\ell2^m$，由 (5.9)
$$
A^n=d_m^\ell I_{<m}\otimes\widetilde N_m^\ell,
$$
两个对角矩阵元仍相等。因此
$$
\varphi(A^n)=0\qquad(n\ge0).
\tag{5.10}
$$
同理 $\varphi((A^*)^n)=0$；
这也可由 $\varphi(T^*)=\overline{\varphi(T)}$ 直接得到。

$\varphi$ 是 WOT 连续的。
R88 给 $\mathfrak C=\overline{\mathbb C[A]}^{\rm SOT}$，
所以 (5.10) 进一步推出
$$
\varphi(\mathfrak C)=\varphi(\mathfrak C^*)=0.
\tag{5.11}
$$
然而对头投影
$$
p_h=(e_h\otimes e_h^*)\otimes I_{\ge m}
$$
有 $\varphi(p_h)=1$。
于是
$$
\boxed{
\mathfrak C+\mathfrak C^*
\text{ 不在原 Haar }B(H)\text{ 中 WOT 稠密}.
}
\tag{5.12}
$$
特别地，$\mathcal A+\mathcal A^*$ 也不稠密。
本节完全不需要在 Haar 表示上延拓 (5.3) 为正常条件期望，
也没有把迹表示的正常泛函转移到 Haar 表示。

## 6. 原始非交换 F. & M. Riesz 定理不能直接填补缺口

已核原始期刊全文：

D. P. Blecher, L. E. Labuschagne,
[*Noncommutative function theory and unique extensions*](https://www.impan.pl/shop/publication/transaction/download/product/90875),
Studia Mathematica 178 (2007), 177–195，
DOI [10.4064/sm178-2-4](https://doi.org/10.4064/sm178-2-4)。

原页178定义：在具有忠实正常有限迹的 von Neumann 代数中，
该理论的最大次对角代数须满足正、负两边线性和弱星稠密。
原页183定义其 F. & M. Riesz 性质；
原页187的 Theorem 3.4 在最大次对角前提下，
把该性质与对角有限维等价。
正常与奇异部分均相对于所指定的 von Neumann 表示分解。

第5.2节否定本题自然迹包络的必要密度条件，第5.3节另给原 Haar 表示的直接有限秩障碍。
因此，不能把这个原定理用于 $\mathcal A$ 后便把其“正常部分”
认作 Haar 表示中的正常泛函。

即使改用另一个更大的次对角代数，
还必须另证慢主理想的消去泛函相容地延拓到该代数的适当理想。
仅有
$$
J\subseteq\mathcal A\subseteq\text{更大的解析代数}
$$
不允许扩大泛函原本消去的集合。
本稿没有作这种未经证明的延拓。

## 7. 一个针对慢主理想的明确商弱零充分条件

记 Banach 商映射
$$
q:\mathcal A\to\mathcal A/J.
$$
若能证明
$$
\boxed{
q(N_j)\longrightarrow0
\quad\text{在 Banach 空间 }\mathcal A/J\text{ 的弱拓扑中},
}
\tag{7.1}
$$
则 (1.1) 成立。

证明如下。
取任意有限秩 Haar 泛函
$$
\varphi(T)=\sum_{\nu=1}^d\langle Tf_\nu,g_\nu\rangle
$$
并假设 $\varphi(J)=0$。
它在 $\mathcal A$ 上的限制是范数连续的，
故下降为某个
$$
\psi\in(\mathcal A/J)^*,\qquad
\varphi|_{\mathcal A}=\psi q.
$$
由 (7.1)，$\varphi(N_j)\to0$。

另一方面，实际高位算子满足
$$
N_j\longrightarrow\tfrac12I\quad\text{于 Haar-WOT}.
$$
所以
$$
\varphi(N_j)\longrightarrow\tfrac12\varphi(I),
$$
进而 $\varphi(I)=0$。
有限秩分离判据给 $I\in\overline J^{\mathrm{WOT}}$；
线性子空间的 WOT 与 SOT 闭包相同，得到 (1.1)。

事实上统一有界的 $N_j$ 还使 Haar-WOT 极限可用于所有迹类正常泛函，
所以 (7.1) 是一个比仅检查有限秩更强的充分接口。
本稿不声称它是必要条件。

### 7.1 当前已知信息没有证明 (7.1)

边界表示中 $N_j$ 强趋零；
因此每个边界正常向量泛函在这些像上趋零。
R195 也给指定边界核和后续部分上全部非零快符号的精确型。
但是尚未证明：

1. $\mathcal A/J$ 的范数由边界核上的限制表示决定；
2. 该表示忠实或具有所需的范数比较；
3. 每个 $(\mathcal A/J)^*$ 泛函都来自该边界表示的正常泛函。

故边界的强零极限尚不能提升为 (7.1)。
也不能从“没有非零有界 Haar–边界交织算子”
直接推出这里所需的所有商对偶泛函分离。

(7.1) 精确描述了一条可能的正常/边界接口；
其证明仍然是新的待解工作，不是本稿的已得结论。

## 8. 使用范围

本稿实际完成的是：

- 标准有限行 Fock 理想压缩的非零秩一缺陷计算；
- 由 R164 得到的原 Haar 表示模型障碍；
- UHF 对角条件期望对范数 Dirichlet 密度及迹包络最大次对角密度的否定；
- 对原始分解与 F. & M. Riesz 定理的假设、表示和页码核验；
- 商弱零条件 (7.1) 推出慢符号强主理想单位的完整充分证明。

它没有把任何模型障碍改写为实际慢符号的非普遍性。
完整 Hilbert 不变子空间问题和慢符号的任意限制范围问题都仍未解决。
