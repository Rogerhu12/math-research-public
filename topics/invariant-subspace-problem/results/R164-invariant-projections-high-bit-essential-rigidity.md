# R164：不变投影的高位渐近交换、忠实 Calkin 表示与共振限制的非本质正规性

日期：2026-11-12（UTC）。作者：literature。

状态：完整证明。本稿以真实进位恒等式和 R161 为输入，给出实际模型的新压缩约束；不声称慢平方共振核已被排除。

## 1. 结论与符号

令
$$
H=L^2(\{0,1\}^{\mathbb N},\mu),\qquad
J_j=M_{\chi_j},\qquad \chi_j(y)=(-1)^{y_j}.
$$
$\mu$ 是公平乘积测度。$J_j$ 是自伴酉算子。

沿用真实模型
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
E_j=e_{10}^{(j)},\qquad
N_j^2=\eta_jN_{j+1},\qquad
\|N_j\|=1,
\tag{1.1}
$$
其中 $\eta_j\le e^{-770\,16^j}$。并且
$$
A=\alpha_0N_0,\qquad
N_j=A^{2^j}/d_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1}.
\tag{1.2}
$$

记 $\mathfrak U$ 为各有限物理张量矩阵代数在此表示中的范数闭包，即本模型的 UHF 代数。
记 $\operatorname{Lat}A$ 为全部闭 $A$ 不变子空间，$P_M$ 为到 $M$ 的正交投影。

**定理1.1。** 对每个 $M\in\operatorname{Lat}A$，
$$
\boxed{
[P_M,J_j]\longrightarrow0\quad\text{强*}.
}
\tag{1.3}
$$
定义
$$
\mathfrak E
=\{T\in B(H):[T,J_j]\longrightarrow0\text{ 强*}\}.
\tag{1.4}
$$
则 $\mathfrak E$ 是含单位的 $C^*$ 代数，并且
$$
\boxed{
C^*(\mathfrak U,\{A\}',\{P_M:M\in\operatorname{Lat}A\})
\subseteq\mathfrak E,\qquad
\mathfrak E\cap\mathcal K(H)=\{0\}.
}
\tag{1.5}
$$
Calkin 商映射在 $\mathfrak E$ 上忠实且完全等距。特别，对所有 $T\in\mathfrak E$，
$$
\boxed{
\|T\|_{\rm ess}=\|T\|,\qquad
\sigma_{\rm ess}(T)=\sigma(T).
}
\tag{1.6}
$$
这里本质谱采用 Fredholm 定义。

同样结论适用于全部不变子商之间有界交织的零延拓（§4.5），以及 $\mathfrak E$ 的所有投影角代数、有限矩阵放大和矩形压缩（§5）。

**定理1.2。** 令 $X$ 是任意复杂 $\ell^2$ 第一阶实际闭乘子，且 $M\in\operatorname{Lat}A$ 满足
$$
M\subseteq\operatorname{Dom}X,\qquad
X(M)\subseteq M,\qquad X|_M\in B(M).
\tag{1.7}
$$
令 $P=P_M$。则 R161 给出的有界算子
$$
X^*P,\qquad (X^*P)^*=\overline{PX},\qquad XP
\tag{1.8}
$$
都属于 $\mathfrak E$；上三角分解的有界非对角块及其伴随也属于相应的 $\mathfrak E$ 矩形角。
这里 $\overline{PX}$ 指 $PX$ 在 $\operatorname{Dom}X$ 上的唯一有界延拓。

**推论1.3。** 在 R161 的慢平方共振设置中，若
$$
M=\ker(X-Y)\ne\{0\},\qquad
Y=(a^2I-B_2)^{1/2}\in\mathcal A,\qquad \chi(Y)=a\ne0,
\tag{1.9}
$$
则 $Y_M=Y|_M$ 不本质正规；更精确地，
$$
\boxed{
0<
\|Y_M^*Y_M-Y_MY_M^*\|
=
\|Y_M^*Y_M-Y_MY_M^*\|_{\rm ess}.
}
\tag{1.10}
$$
因此其自交换子不可能是非零紧算子、Hilbert–Schmidt 算子或迹类算子，且 $Y_M$ 不可能是正规算子的紧扰动。

该推论只给未知核的必要条件。它没有证明这个压缩实际上本质正规，也没有由必要条件直接排核。

## 2. 高位的真实强极限

### 2.1. 常向量表示中的物理升降

设 $f$ 只依赖有限多个低位。当 $j$ 高于这些位时，
$$
E_jf=\mathbf1_{\{y_j=1\}}f,\qquad
E_j^*f=\mathbf1_{\{y_j=0\}}f.
\tag{2.1}
$$
这是物理基 $e_0,e_1$ 与参考向量 $(e_0+e_1)/\sqrt2$ 的直接计算。

由 (1.1)，
$$
\|N_j-E_j\|\le\eta_j,\qquad
\|N_j^*-E_j^*\|\le\eta_j.
\tag{2.2}
$$
先在柱函数上使用 (2.1)，再以一致有界性延到 $H$，得到
$$
\boxed{
N_j-\frac{I-J_j}{2}\longrightarrow0\quad\text{强},\qquad
N_j+N_j^*\longrightarrow I\quad\text{强}.
}
\tag{2.3}
$$
第二个收敛因各项自伴也为强*收敛。

第一式只声称强收敛，不声称强*收敛。事实上在高于 $f$ 的有限支撑时，
$N_j^*f$ 接近 $(I+J_j)f/2$，而不是 $(I-J_j)f/2$。

令 $S_j=I-2E_j$。已有真实估计
$$
\|V_j-S_j\|\le8\eta_j,\qquad \sup_j\|V_j\|\le6
\tag{2.4}
$$
与 (2.1) 给
$$
\boxed{
V_j-J_j\longrightarrow0\quad\text{强},\qquad
V_j^*+J_j\longrightarrow0\quad\text{强}.
}
\tag{2.5}
$$
不将这两条不同符号的极限合并为错误的强*近似。

### 2.2. 弱零酉序列

对任意固定柱函数 $f,g$，高于其支撑的 $j$ 满足
$$
\langle J_jf,g\rangle=0.
$$
由柱函数稠密和 $\|J_j\|=1$，
$$
\boxed{J_j\longrightarrow0\quad\text{弱算子拓扑}.}
\tag{2.6}
$$
因此对每个固定 $f\in H$，$J_jf$ 弱趋零且范数恒为 $\|f\|$。

## 3. 全部不变投影的强*渐近交换

固定 $M\in\operatorname{Lat}A$，置 $P=P_M$、$Q=I-P$。
因为 $N_j$ 是 $A$ 的标量倍幂，
$$
QN_jP=0,\qquad PN_j^*Q=0.
\tag{3.1}
$$
故
$$
[P,N_j]=PN_jQ=P(N_j+N_j^*)Q.
\tag{3.2}
$$
由 (2.3)，右侧强趋 $PIQ=0$。取伴随，
$$
[P,N_j]^*=Q(N_j+N_j^*)P\longrightarrow0
\quad\text{强}.
$$
所以
$$
\boxed{[P,N_j]\longrightarrow0\quad\text{强*}.}
\tag{3.3}
$$

由 (2.3) 第一式，
$$
J_j-(I-2N_j)\longrightarrow0\quad\text{强}.
$$
固定有界算子 $P$ 与强零序列的交换子仍强趋零，于是
$$
[P,J_j]\longrightarrow0\quad\text{强}.
$$
由于 $P,J_j$ 都自伴，
$$
[P,J_j]^*=-[P,J_j],
$$
故这同时是强*收敛，证明 (1.3)。

稍后还需
$$
\boxed{[P,V_j]\longrightarrow0\quad\text{强*}.}
\tag{3.4}
$$
为避免在强收敛序列右侧乘随 $j$ 变化的向量，使用精确式
$$
V_j=I-2N_j+2N_j^2(I+N_j)^{-1}.
\tag{3.5}
$$
因 $\|(I+N_j)^{-1}\|<3$，
$$
\|V_j-(I-2N_j)\|\le6\eta_j.
$$
(3.3) 立即给 (3.4)。
此外 $V_jM\subseteq M$，故
$$
[P,V_j]=PV_jQ,\qquad
\operatorname{Ran}[P,V_j]\subseteq M.
\tag{3.6}
$$

本节没有把 $P$ 设为物理柱投影，也没有从“总本质支撑全测”推导点态压缩公式。

## 4. 渐近交换代数与忠实 Calkin 表示

### 4.1. $\mathfrak E$ 是 $C^*$ 代数

因为 $J_j=J_j^*$，
$$
[T,J_j]^*=-[T^*,J_j].
$$
所以 (1.4) 等价于同时要求
$[T,J_j]\to0$ 强和 $[T^*,J_j]\to0$ 强。

对 $S,T\in\mathfrak E$，
$$
[ST,J_j]=S[T,J_j]+[S,J_j]T
$$
强趋零；对伴随使用同式。因此 $\mathfrak E$ 对乘法和伴随封闭，显然也对加法、标量乘法封闭且含 $I$。

若 $T_n\in\mathfrak E$ 且 $\|T_n-T\|\to0$，则
$$
\|[T-T_n,J_j]\|\le2\|T-T_n\|.
$$
先固定 $n$ 取 $j\to\infty$，再取 $n\to\infty$，得到 $T\in\mathfrak E$。
故它是范数闭的 $C^*$ 代数。

### 4.2. 实际 UHF 代数、全部交换子及不变投影都在其中

任意有限物理张量矩阵 $T$ 与所有充分高位的 $J_j$ 精确交换。
对其范数极限也有
$$
\|[T,J_j]\|\longrightarrow0.
$$
故 $\mathfrak U\subseteq\mathfrak E$。§3 给出全部 $P_M\in\mathfrak E$，于是 (1.5) 的包含成立。

这里实际 $A,\mathcal A,V_j$ 都确实属于 $\mathfrak U$。
例如对 $m>i$，把 (1.1) 递归在第 $m$ 位截断为零得到有限张量算子 $N_i^{[m]}$，且
$$
\|N_i-N_i^{[m]}\|
\le\prod_{\nu=i}^{m-1}\eta_\nu\longrightarrow0.
\tag{4.1}
$$
所以 $N_i\in\mathfrak U$。
又因 $\|N_i^2\|=\eta_i<1$，
$$
(I+N_i)^{-1}
=(I-N_i)\sum_{k\ge0}N_i^{2k}
$$
按范数收敛于 $\mathfrak U$ 内，故 $V_i\in\mathfrak U$。
最后 $A=\alpha_0N_0$，所以 $\mathcal A\subseteq\mathfrak U$。

事实上整个有界交换子 $\{A\}'$ 都包含于 $\mathfrak E$。
若 $T\in\{A\}'$，则 $[T,N_j]=0$。
由 (2.3) 第一式，在固定输入上比较 $J_j$ 与 $I-2N_j$，得到
$$
[T,J_j]\longrightarrow0\quad\text{强}.
$$
同时 $[T^*,N_j^*]=0$，而 (2.3) 的两式相减给
$$
N_j^*-\frac{I+J_j}{2}\longrightarrow0\quad\text{强}.
$$
故 $[T^*,J_j]\to0$ 强，证明
$$
\boxed{\{A\}'\subseteq\mathfrak E.}
\tag{4.1a}
$$
因此主包含中的 $\{A\}'$ 不需要是 UHF 的范数子代数；这里使用其真实交换关系分别处理两个伴随方向。
特别，所有保持 $M$ 的有界交换子限制都服从 §5 的本质范数和谱刚性。

全部有界乘法算子也属于 $\mathfrak E$，因为它们与每个 $J_j$ 交换。

### 4.3. 本质范数等于原范数

取 $T\in\mathfrak E$、固定单位向量 $f$ 及任意紧算子 $K$。
由 $J_jf\rightharpoonup0$，
$$
KJ_jf\longrightarrow0\quad\text{范数}.
$$
由 $[T,J_j]f\to0$，
$$
TJ_jf-J_jTf\longrightarrow0.
$$
因此
$$
\|T+K\|
\ge\limsup_j\|(T+K)J_jf\|
=\|Tf\|.
$$
对单位 $f$ 取上确界，再对紧 $K$ 取下确界，
$$
\|T\|_{\rm ess}\ge\|T\|.
$$
反向不等式由 $K=0$ 得到，故 (1.6) 的范数等式成立。
特别若 $T$ 紧，则 $T=0$。

这证明 Calkin 商映射在 $\mathfrak E$ 上是忠实等距的 $*$ 同态。
对每个有限 $n$，在 $H^n$ 使用
$$
J_j^{(n)}=J_j\oplus\cdots\oplus J_j
$$
重复同一证明；矩阵各项的强*交换给整个矩阵的强*交换。
于是
$$
\|[T_{rs}]\|_{\rm ess}=\|[T_{rs}]\|
\quad([T_{rs}]\in M_n(\mathfrak E)),
\tag{4.2}
$$
即完全等距。

### 4.4. 谱和本质谱相等

忠实含单位 $C^*$ 嵌入保持谱；故 (1.6) 的谱等式可直接由 Calkin 表示得到。

也可直接验证其 Fredholm 含义。
若 $T\in\mathfrak E$ 是 Fredholm，闭值域使 $0$ 在 $T^*T$ 的谱中或者不出现，或者是孤立点。
投影到 $\ker T$ 的谱投影属于 $C^*(I,T)\subseteq\mathfrak E$，且为有限秩，因此必为零。
对 $T^*$ 同理，得到 $\ker T^*=\{0\}$。
Fredholm 值域又闭，故 $T$ 是有界可逆的。
所以
$$
T\in\mathfrak E\text{ Fredholm}
\quad\Longleftrightarrow\quad
T\text{ 可逆}.
\tag{4.3}
$$
将其用于 $T-\lambda I$，即得
$\sigma_{\rm ess}(T)=\sigma(T)$。

### 4.5. 全部不变限制及不变子商之间的有界交织

先设 $M,N\in\operatorname{Lat}A$，且有界算子
$$
B:M\longrightarrow N
$$
满足 $BA|_M=A|_N B$。
把 $B$ 零延拓为 $T=BP_M\in B(H)$，并将输出自然嵌入 $H$。
$B$ 也交织 $N_j$ 的两个限制，所以
$$
[T,N_j]=B[P_M,N_j].
\tag{4.4}
$$
这里右侧有定义，因为 $[P_M,N_j]$ 的像落在 $M$ 内。
(3.3) 给 (4.4) 强*趋零。
分别用
$$
N_j-\frac{I-J_j}{2}\to0\text{ 强},\qquad
N_j^*-\frac{I+J_j}{2}\to0\text{ 强}
$$
处理正向和伴随，得到 $T\in\mathfrak E$。
所以全部这类交织的零延拓，也可加入 (1.5) 的 $C^*$ 生成集合。

同一事实适用于真正的不变子商，而不要求它们的正交代表空间在 $A$ 下不变。
具体设
$$
N_\nu\subseteq M_\nu,\qquad
N_\nu,M_\nu\in\operatorname{Lat}A,\qquad
K_\nu=M_\nu\ominus N_\nu,\qquad \nu=1,2,
$$
并令 $P_\nu=P_{M_\nu}-P_{N_\nu}$。
$M_\nu/N_\nu$ 的 Hilbert 表示为 $K_\nu$，诱导算子是
$$
A_\nu=P_\nu A|_{K_\nu}.
$$
由于 $A$ 保持 $M_\nu,N_\nu$，每次压缩丢弃的向量落在 $N_\nu$ 中，后续作用仍留在 $N_\nu$。
归纳给
$$
A_\nu^k=P_\nu A^k|_{K_\nu},\qquad
N_{j,\nu}:=A_\nu^{2^j}/d_j=P_\nu N_j|_{K_\nu}.
\tag{4.5}
$$
又由 (3.3) 的线性性，
$$
[P_\nu,N_j]\longrightarrow0\quad\text{强*}.
\tag{4.6}
$$

若 $B:K_1\to K_2$ 有界且 $BA_1=A_2B$，令
$T=P_2BP_1$ 表示其零延拓。
由 (4.5) 的交织关系，有精确的两边界公式
$$
\boxed{
[T,N_j]=T[P_1,N_j]+[P_2,N_j]T.
}
\tag{4.7}
$$
右侧强*趋零，故与限制情形相同，$T\in\mathfrak E$。

因此，$\mathfrak U$、全部不变投影，以及全部不变子商之间有界交织的零延拓共同生成的 $C^*$ 代数，在 Calkin 代数中仍忠实且完全等距。
例如任何非零这类交织都不是紧算子；矩形 Fredholm 交织必为实际有界同构，详见 §5。
这里没有把子商嵌入误当成原算子的真实不变子空间。

## 5. 投影角、矩形压缩与有限放大

设 $P,Q\in\mathfrak E$ 是正交投影。这里可取任意两个 $A$ 不变投影，或其补投影；无需假设它们互相交换。

若 $T\in Q\mathfrak E P$，把它视为
$$
T:PH\longrightarrow QH.
$$
其在 $H$ 上的零延拓仍记为 $T$。
矩形紧算子 $PH\to QH$ 的零延拓是 $H$ 上紧算子；
反之，把 $H$ 上紧算子左右压缩仍紧。
因此矩形本质范数恰等于零延拓的本质范数。
由 §4，
$$
\boxed{
\|T:PH\to QH\|_{\rm ess}
=\|T:PH\to QH\|.
}
\tag{5.1}
$$
特别 $QTP$ 只要属于此角，就不能是非零紧算子。

如果 $P=Q\ne0$，$P\mathfrak E P$ 是以 $P$ 为单位的 $C^*$ 代数。
它在 $PH$ 的 Calkin 代数中仍忠实。
所以对任意 $T\in P\mathfrak E P$，
$$
\boxed{
\sigma_{B(PH)}(T)
=\sigma_{\rm ess,\,PH}(T).
}
\tag{5.2}
$$
这里使用的是 $PH$ 上的谱，不把 $H$ 上零延拓额外产生的零谱点混入。

同样，矩形 $T\in Q\mathfrak E P$ 若在 $PH\to QH$ 意义下 Fredholm，则实际为有界同构。
可分别对 $T^*T\in P\mathfrak E P$ 和 $TT^*\in Q\mathfrak E Q$ 应用 §4.4 的有限秩核投影论证。

所有结论可有限放大。
例如 $M_1,\ldots,M_n\in\operatorname{Lat}A$，令
$$
\widehat P=P_{M_1}\oplus\cdots\oplus P_{M_n}.
$$
矩阵算子
$$
\widehat P[T_{rs}]\widehat P,\qquad T_{rs}\in\mathfrak E,
$$
在 $\bigoplus_rM_r$ 上的本质范数等于原范数，且其谱等于该空间上的本质谱。

对自伴压缩，(5.2) 表示不存在孤立且有限重数的离散谱点。
它不预先确定谱位于正半轴、负半轴或某个特定区间。

## 6. R161 的有界限制与非对角块也在 $\mathfrak E$

本节处理第一阶乘子可能无界的情形，避免仅以 $Y\in\mathfrak U$ 为前提。

令 $X$ 为任意复杂 $\ell^2$ 第一阶闭乘子，且 $M$ 满足 (1.7)。
记 $P=P_M$、$Q=I-P$。

### 6.1. 实际有界伴随交换子

R161 已证明
$$
\operatorname{Dom}X=\operatorname{Dom}X^*
\tag{6.1}
$$
以及
$$
D_j=[X^*,N_j]\in B(H),\qquad \|D_j\|\longrightarrow0.
\tag{6.2}
$$
这里 (6.2) 是完整共同域上的真实恒等式。

由 R125，$V_j$ 和 $(I+N_j)^{-1}$ 保持 $\operatorname{Dom}X$，并与 $X$ 在该域交换。
结合 (6.1)，这些算子也保持 $\operatorname{Dom}X^*$。
逆交换子恒等式于是给
$$
F_j:=[X^*,V_j]
=-2(I+N_j)^{-1}D_j(I+N_j)^{-1},
\tag{6.3}
$$
以及
$$
\boxed{\|F_j\|\le18\|D_j\|\longrightarrow0.}
\tag{6.4}
$$
没有把 $X^*$ 当成与 $V_j$ 精确交换。

### 6.2. 两个方向分别验证强交换

R161 的图二次型估计给
$$
T:=X^*P\in B(H),\qquad
\|T\|^2\le\|X|_M\|^2+\|C_a\|.
\tag{6.5}
$$
令 $W=T^*$。对 $f\in\operatorname{Dom}X$，
$$
Wf=PXf.
\tag{6.6}
$$

先证 $[T,J_j]\to0$ 强。
由 (3.6)，$[P,V_j]$ 的像严格落在 $M$。
因此虽然 $X^*$ 在全空间可能无界，此处仍有合法的有界恒等式
$$
X^*[P,V_j]=T[P,V_j].
\tag{6.7}
$$
使用 (6.3)，对全体 $f\in H$，
$$
\begin{split}
(TV_j-V_jT)f
&=X^*PV_jf-V_jX^*Pf\\
&=T[P,V_j]f+F_jPf.
\end{split}
\tag{6.8}
$$
其中 $V_jPf$ 在 $\operatorname{Dom}X^*$ 内，且 $[P,V_j]f\in M$；
所以每一步都有实际定义域依据。
(3.4) 和 (6.4) 使 (6.8) 强趋零。
再用 $V_j-J_j\to0$ 强分别作用在固定 $f,Tf$ 上，
$$
[T,J_j]\longrightarrow0\quad\text{强}.
\tag{6.9}
$$

再证伴随方向。若 $f\in\operatorname{Dom}X$，由域保持和 $XV_j=V_jX$，
$$
\begin{split}
(WV_j-V_jW)f
&=PXV_jf-V_jPXf\\
&=[P,V_j]Xf\longrightarrow0.
\end{split}
\tag{6.10}
$$
所有 $WV_j-V_jW$ 的范数均不超过 $12\|W\|$。
因 $\operatorname{Dom}X$ 稠密，(6.10) 延为全 $H$ 上的强收敛。
再次使用 (2.5)，
$$
[W,J_j]\longrightarrow0\quad\text{强}.
\tag{6.11}
$$
由于 $W=T^*$，(6.9)—(6.11) 恰给 $T\in\mathfrak E$，且 $W\in\mathfrak E$。

这个论证没有把任意强小向量送入无界 $X^*$。
(6.7) 的关键是交换子像落在已经具有有界 $X^*$ 限制的 $M$ 内。

### 6.3. 全部有界块及本质范数

因为 $X(M)\subseteq M$，
$$
XP=WP\in\mathfrak E.
\tag{6.12}
$$
R161 的上三角有界非对角块零延拓为
$$
B=WQ,\qquad B^*=QT.
\tag{6.13}
$$
所以 $B,B^*\in\mathfrak E$。
特别
$$
\boxed{
\|X|_M\|_{\rm ess}=\|X|_M\|,\qquad
\|B:M^\perp\to M\|_{\rm ess}=\|B\|.
}
\tag{6.14}
$$
$X|_M$ 在 $M$ 上的谱也等于本质谱。

更一般，全部有界表达式，由 $P,XP,W,T,B,B^*$ 及 $\mathfrak U$ 经有限和、积、伴随、范数极限得到者，都在 $\mathfrak E$ 中。
这不把无界右下块 $Z$ 或未经证明的二阶自然乘积纳入有界 $C^*$ 代数。

## 7. 慢平方共振的进一步必要条件

沿用 R161 的共振记号：
$$
B_2=\sum_j a_j^2(I-V_j^2),\qquad
Y=(a^2I-B_2)^{1/2}\in\mathcal A,\qquad \chi(Y)=a\ne0.
\tag{7.1}
$$
这里 $a=a_{j_0}$ 是最低非零第一系数，$X$ 是相应的非恒定第一阶闭乘子。
R144、R161 已建立
$$
M=\ker X_{u^2-a^2}=\ker(X-Y),
\tag{7.2}
$$
以及
$$
M\subseteq\operatorname{Dom}X^n,\qquad
X^n|_M=Y^n|_M\quad(n\ge1).
\tag{7.3}
$$
本节只使用这些已证明的域关系。

### 7.1. 压缩能量全部保留在 Calkin 商中

R161 的有界自交换子形式是
$$
C_a=4M_{r_a}+K_a,\qquad
r_a=\sum_j|a_j|^2\chi_j,
\tag{7.4}
$$
且
$$
\|K_a\|\le
\left(144\eta_*+\frac{1296\eta_*}{1-\eta_*}\right)\|a\|_2^2.
\tag{7.5}
$$
$C_a$ 是有限 $V_i^*,V_j$ 交换子和的范数极限，所以 $C_a\in\mathfrak U$。
由于 $Y\in\mathcal A\subseteq\mathfrak U$，
$$
Y_M^*Y_M-Y_MY_M^*,\qquad PC_a|_M,\qquad BB^*
\tag{7.6}
$$
都属于 $P\mathfrak E P$。

R161 的精确式
$$
BB^*
=Y_M^*Y_M-Y_MY_M^*-PC_a|_M\ge0
\tag{7.7}
$$
在 $M$ 的 Calkin 代数中仍为同一正性等式。
由于表示忠实，(7.6) 中每个算子的范数、谱和正性都可从其 Calkin 像完整恢复。

特别，
$$
BB^*\text{ 紧}\ \Longrightarrow\ B=0,
\tag{7.8}
$$
而
$$
PC_a|_M\text{ 紧}\ \Longrightarrow\ PC_a|_M=0.
\tag{7.9}
$$
(7.8) 单独不被宣称已迫使 $M=0$。

### 7.2. 共振限制不可能本质正规

假设 $M\ne0$。
因 $\mathcal A$ 的唯一字符为 $\chi$，$Y-aI$ 在全 $H$ 上拟幂零。
$M$ 被 $Y$ 保持，因此
$$
\|(Y_M-aI_M)^n\|
\le\|(Y-aI)^n\|,
$$
故
$$
\sigma(Y_M)=\{a\}.
\tag{7.10}
$$
这没有利用未经证明的伴随不变性。

若 $Y_M$ 本质正规，则
$$
L:=Y_M^*Y_M-Y_MY_M^*
$$
是紧算子。由 $L\in P\mathfrak E P$ 及 §5，必有 $L=0$。
于是 $Y_M$ 正规。结合 (7.10)，正规谱理论给
$$
Y_M=aI_M.
$$
由 $X|_M=Y_M$，得到
$$
M\subseteq\ker(X-aI).
$$
但 $X-aI$ 仍是非零的第一阶闭乘子，R125 已证明其单射。
故 $M=0$，矛盾。

所以 $L\ne0$，且由本质范数等式，
$$
0<\|L\|=\|L\|_{\rm ess},
$$
证明 (1.10)。
若 $Y_M$ 是某个正规算子的紧扰动，其自交换子必紧，也被同一论证排除。

这项条件比“$Y_M$ 在未知核上有界”更强，
但尚不能从现有条件推出 $Y_M$ 本质正规。

### 7.3. 另一个普适限制

对于任意满足 (1.7) 的非恒定第一阶 $X$，如果
$$
X|_M=\lambda I_M+K,\qquad K\text{ 紧},
$$
则 $K\in P\mathfrak E P$，故 $K=0$。
再由 R125 的 $\ker(X-\lambda I)=0$，得到 $M=0$。

因此非零 $A$ 不变空间上的有界第一阶限制不可能是标量加紧算子。
这个结论不预设慢平方关系。

## 8. 范围与尚未解决的缺口

1. (1.3) 是对每个固定向量的强*渐近交换，没有给所有单位向量统一的算子范数收敛率。
2. 因而不能把它自动用于位数随参数增长的高位乘积；该操作需要新的定量控制。
3. $\mathfrak E$ 没有非零紧元，并不表示它交换或其算子正规；UHF 代数本身已提供大量非正规元。
4. 谱等于本质谱没有确定未知压缩 $PM_{r_a}|_M$ 的正负，也没有把压缩识别为某个支撑集上的乘法。
5. 不本质正规性是慢平方共振非零核必须满足的新约束。当前仍未证明这个条件与其他真实模型结构矛盾。
6. 本稿不建立完整 Hilbert 不变子空间问题的解，也不声称本课题候选已经无任何非平凡闭不变子空间。

## 9. 依赖与复核记录

- 真实物理递归、$\|N_j\|=1$、$N_j^2=\eta_jN_{j+1}$、$V_j$ 与纯物理矩阵的误差：原模型已证结果。
- R125：复杂 $\ell^2$ 第一阶闭乘子的 $C$ 自伴性、有限柱图核心、实际交换子域保持及全部标量移位单射。
- R144、R161：慢平方共振核的平方根分支、完整幂域，以及通常伴随同域和有界自交换子形式。
- 本稿作者独立全文核验 R161 初稿 blob 0e4816311f7ed61922d77673976198db418094a2；特别检查了真实进位、双图核心、通常伴随域、$[X^*,N_j]$ 的完整域式及 $BB^*$ 符号。
- R164 新增内容为 §§2–7 的高位强*渐近交换、相关 Calkin 忠实性、无界第一阶有界块的实际域处理和共振限制的非本质正规性。它不重复 R161 的有界自交换子主定理。
