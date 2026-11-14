# R236：二次闭像核的再次中央约化、非退化新核与闭斜投影

日期：2026-11-12。状态：完整的实际子商结构定理。以下关闭若干结构分叉，但不宣称排除原慢分支核。

## 1. 设置和已经支付的输入

设
$$
X=a_*I+\sum_j a_jV_j,\qquad a\in\ell^2\setminus\ell^1,
\qquad Y=\phi(B_2)\in\mathcal A,\qquad T=X-Y,
$$
其中 $\phi$ 是零点邻域的标量解析芽，代入取通常全纯演算。假设
$$
0\ne M=\ker T,\qquad M\perp CM.
\tag{1.1}
$$
R161、R208、R212、R233 已给：

- $T$ 闭、$C$ 自伴，且 $\operatorname{Dom}T=\operatorname{Dom}T^*$。
- $M,CM$ 均包含在该真实域中，$X,X^*$ 在这两个外块上有界。
- 旧中央空间 $K=(M\oplus CM)^\perp$ 上有自然闭商 $T_K$，它与共同正则器的最大图一致。
- 令 $M_r=\ker T^r$，全部幂取真实自然域，则
  $$
  \mathcal B(T^{r-1}M_r,M_r)=0,\qquad
  N_r=M\cap\overline{\operatorname{Ran}T^r}\ne0
  \tag{1.2}
  $$
  对每个有限 $r\ge1$ 成立。每个 $T^r$ 都是 R176 的闭、$C$ 自伴的最高系数为单位的实际多项式。

本稿主要分析 R233 尚余的旧中央单射分支：
$$
\boxed{\ker T_K=0.}
\tag{1.3}
$$
第 2 节的第一次新约化不需要 (1.3)；第 3 节以后说明何处使用它。

写
$$
M_2=\ker T^2,\qquad
N=N_2=M\cap\overline{\operatorname{Ran}T^2}
=M\cap(CM_2)^\perp.
\tag{1.4}
$$
$N$ 是非零闭 $A$ 不变子空间，包含于全等向的 $M$ 中，因此也是全等向的。它不必等于 $M$。

全文采用 $\mathcal B(u,v)=\langle u,Cv\rangle$，Hilbert 内积对第一变量线性。

## 2. 用 $N_2$ 作外块，原二次广义核完整下沉

### 2.1 两个准确包含

式 (1.2) 在 $r=2$ 时给
$$
TM_2\subset N.
\tag{2.1}
$$
另一方面，若 $Tx\in N$，则 $Tx\in M\subset\operatorname{Dom}T$，故 $x$ 在真实自然二次域中且 $T^2x=0$。于是
$$
\boxed{T^{-1}N=M_2.}
\tag{2.2}
$$
这里的 $T^{-1}N$ 只包含原域中的向量。

由 $N\subset(CM_2)^\perp$ 及双线性形式的对称性，
$$
\boxed{M_2\subset L_N:=(CN)^\perp.}
\tag{2.3}
$$
这两个包含是选择 $N=N_2$ 的具体作用；不能对任意原核子空间直接假定它们。

### 2.2 新中央算子的真实域和闭性

令
$$
K_N=L_N\ominus N=(N\oplus CN)^\perp,\qquad C_N=C|_{K_N}.
$$
这是实际 Haar 不变旗 $N\subset L_N$ 的 Hilbert 子商。其有界移位记为
$$
A_N=P_{K_N}A|_{K_N}.
$$
$K_N$ 本身不被宣称对原 UHF 代数不变。

由于 $N\subset M$，两个外投影 $P_N,P_{CN}$ 都把全空间送入 $\operatorname{Dom}X$。因此
$$
\operatorname{Dom}T
=N\oplus\mathcal D_N\oplus CN,\qquad
\mathcal D_N=K_N\cap\operatorname{Dom}X.
\tag{2.4}
$$
该中央域在 $K_N$ 中稠密。$T$ 在 $N$ 上为零，$T^*$ 在 $CN$ 上为零；除中央块外，其余块均有界，理由与 R212 相同：$X^*P_N$ 有界，其伴随提供 $P_NX$ 的真实有界延拓；$X|_{CN}$ 也有界。

故有
$$
T=
\begin{pmatrix}
0&F_N&D_N\\
0&S&H_N\\
0&0&0
\end{pmatrix},
\qquad
S=P_{K_N}T|_{\mathcal D_N}.
\tag{2.5}
$$
$S$ 是闭算子。若 $x_\nu\in\mathcal D_N$、$x_\nu\to x\in K_N$ 且 $Sx_\nu\to y$，则
$$
Tx_\nu=F_Nx_\nu+Sx_\nu\to F_Nx+y,
$$
原闭性给 $x\in\mathcal D_N$、$Sx=y$。有界外块的通常伴随域计算还给
$$
S^*=C_NS C_N,\qquad
\operatorname{Dom}S^*=\operatorname{Dom}S=\mathcal D_N.
\tag{2.6}
$$
$T$ 在 $L_N$ 上的自然商图已经闭，正好是 (2.5)，而不是另一个未经识别的最大域。

共同实际正则器 $R(s)$、固定参数单位比及 $TR(s)$ 保持 $N,L_N$，故可以下降到此子商。与 R212 相同的两段闭图论证识别自然图与其最大正则化图。下面不依赖任何尚未证明的物理删除算子下沉。

### 2.3 新核没有丢掉额外的交集

对 $x\in\mathcal D_N$，$Sx=0$ 等价于 $Tx\in N$。由 (2.2)、(2.3)，
$$
\boxed{\mathcal E:=\ker S=M_2\ominus N\cong M_2/N.}
\tag{2.7}
$$
这一次完整的 $M_2$ 都进入自然商，不需要再写一个未知的 $M_2\cap L_N$：式 (2.3) 已明确支付了该条件。

## 3. 旧中央单射迫使新核的双线性型代数非退化

现在使用 (1.3)。R212 的准确旧核公式给
$$
M_2\cap(M\oplus K)=M.
\tag{3.1}
$$
令
$$
\operatorname{Rad}_{\mathcal B}(M_2)
=\{x\in M_2:\mathcal B(x,M_2)=0\}.
$$
若 $x$ 在此根空间内，因 $M\subset M_2$，有 $\mathcal B(x,M)=0$，故
$x\in(CM)^\perp=M\oplus K$。由 (3.1)，$x\in M$，再由定义得到 $x\in N$。
反向包含由 (1.4) 直接成立。因此
$$
\boxed{\operatorname{Rad}_{\mathcal B}(M_2)=N.}
\tag{3.2}
$$

因为 $N$ 与整个 $M_2$ 双线性正交，(3.2) 下沉到 (2.7) 后给
$$
\boxed{
x\in\mathcal E,\quad
\mathcal B_N(x,\mathcal E)=0
\ \Longrightarrow\ x=0,
\qquad
\mathcal B_N=\mathcal B|_{K_N}.
}
\tag{3.3}
$$
这是代数非退化性。它没有给正下界
$\sup_{\|y\|\le1,y\in\mathcal E}|\mathcal B_N(x,y)|\ge c\|x\|$，
也没有证明相应压缩 Gram 算子的逆有界。

原来的两种情况现在有准确解释。

- 若 $N=M$，则 $M_2\subset(CM)^\perp$，由 (3.1) 得 $M_2=M$。新中央空间就是旧 $K$，新核为零。
- 若 $N\ne M$，则 $\mathcal E$ 至少包含非零的 $M\ominus N$，因此是一个非零、代数非退化的中央核。

所以在旧中央单射分支中，$N$ 真包含于 $M$ 时，新的中央核必然不再全等向。这不是从原物理反射免费递归所得，而是由二次广义核的根空间准确算出。

## 4. 非退化新核与闭像的稠密直和

以下假设 $N\ne M$。令
$$
\mathcal R=\overline{\operatorname{Ran}S}.
$$
由 (2.6)，
$$
\mathcal R=(C_N\mathcal E)^\perp.
\tag{4.1}
$$
于是 (3.3) 给
$$
\mathcal E\cap\mathcal R=0.
\tag{4.2}
$$
同时
$$
(\mathcal E+\mathcal R)^\perp
=\mathcal E^\perp\cap C_N\mathcal E=0,
$$
最后一步等价于 (3.3)。因此
$$
\boxed{
\mathcal E\dotplus\mathcal R\text{ 在 }K_N\text{ 中稠密，且两者 }\mathcal B_N\text{ 正交。}
}
\tag{4.3}
$$
未证明该直和闭。

这也排除了新中央算子上的非平凡有限广义延长。若 $S^2x=0$，
则 $Sx\in\mathcal E\cap\operatorname{Ran}S=0$，所以
$$
\boxed{\ker S^r=\ker S=\mathcal E\qquad(r\ge1),}
\tag{4.4}
$$
全部幂取自然域。零根在这个代数意义下已稳定；这里没有声称零是孤立谱点。

$S$ 仍无界。否则由闭性，其域等于全 $K_N$，(2.4)–(2.5) 会使 $T$、从而 $X$ 有界，与 $a\notin\ell^1$ 相反。因此 $\mathcal R\ne0$。$\mathcal E,\mathcal R$ 均对实际 $A_N$ 不变，且非零时无限维。

## 5. 未闭直和的规范投影确是闭无界算子

定义
$$
\operatorname{Dom}\Pi=\mathcal E\dotplus\mathcal R,\qquad
\Pi(e+r)=e.
\tag{5.1}
$$
它稠密定义，$\Pi(\operatorname{Dom}\Pi)\subset\operatorname{Dom}\Pi$，且
$\Pi^2=\Pi$ 在该域上成立。

它是闭算子：若 $e_n+r_n\to x$ 且 $e_n\to y$，由于两个子空间都闭，
$y\in\mathcal E$、$x-y\in\mathcal R$，所以 $x\in\operatorname{Dom}\Pi$、$\Pi x=y$。

其完整通常伴随域也能明确计算：
$$
\operatorname{Dom}\Pi^*
=\mathcal R^\perp\dotplus\mathcal E^\perp,\qquad
\Pi^*(u+v)=u
\quad(u\in\mathcal R^\perp,\ v\in\mathcal E^\perp).
\tag{5.2}
$$
事实上，$z\in\operatorname{Dom}\Pi^*$ 要求存在 $w$，使
$\langle e,z\rangle=\langle e+r,w\rangle$ 对所有 $e,r$ 成立；
这正是 $w\in\mathcal R^\perp$、$z-w\in\mathcal E^\perp$。

由 (4.1)，
$$
C_N\mathcal E=\mathcal R^\perp,\qquad
C_N\mathcal R=\mathcal E^\perp.
$$
因此
$$
\boxed{\Pi^*=C_N\Pi C_N.}
\tag{5.3}
$$
这不等于通常伴随同域；此处没有证明
$\operatorname{Dom}\Pi=\operatorname{Dom}\Pi^*$。

若 (4.3) 的和闭，则它等于全 $K_N$，$\Pi$ 有界，且是非平凡的
$\mathcal B_N$ 对称幂等算子。若该和不闭，则 $\Pi$ 无界，并有
$$
\boxed{\sigma(\Pi)=\mathbb C.}
\tag{5.4}
$$
证明很直接：$0,1$ 分别有非零核 $\mathcal R,\mathcal E$；若
$\lambda\notin\{0,1\}$，则
$$
(\Pi-\lambda I)(e+r)=(1-\lambda)e-\lambda r,
$$
其像恰为原来的稠密非全域 $\operatorname{Dom}\Pi$，不能满射到 $K_N$。
这些 $\lambda$ 是连续谱点。不能从闭性和幂等关系自动推出有界性。

由于 $A_N$ 保持两个子空间，它保持 $\operatorname{Dom}\Pi$，并满足
$$
\Pi A_N=A_N\Pi\quad\text{于 }\operatorname{Dom}\Pi.
\tag{5.5}
$$
本节得到的是实际子商上的闭模投影，不是原全空间上未经提升的有界交换子。

## 6. 有界分离投影的准确判据

### 6.1 与一致非退化性的等价

记
$$
V=P_{C_N\mathcal E}|_{\mathcal E}:
\mathcal E\longrightarrow C_N\mathcal E.
$$
它单射且稠密值域：单射由 (3.3)，而其伴随的核为
$C_N\mathcal E\cap\mathcal E^\perp=0$。

由 (4.1)，
$$
x\in\operatorname{Dom}\Pi
\iff P_{C_N\mathcal E}x\in\operatorname{Ran}V.
\tag{6.1}
$$
于是以下三项等价：

1. $\Pi$ 有界；
2. $\mathcal E+\mathcal R$ 闭；
3. 存在 $\delta>0$，使
   $$
   \|P_{C_N\mathcal E}e\|\ge\delta\|e\|
   \quad(e\in\mathcal E).
   \tag{6.2}
   $$

若 (6.2) 成立，$V$ 的稠密值域同时闭，故 $V$ 满射，$\Pi=V^{-1}P_{C_N\mathcal E}$ 有界。反过来，若 $\Pi$ 有界，则
$\Pi P_{C_N\mathcal E}e=e$，直接给 (6.2)。

### 6.2 与旧非对角商伴随域的等价

保留 R233 旧中央块的记号
$$
\mathcal D_H
=\{c\in CM:H_1c\in\operatorname{Ran}T_K\},
\qquad J_H=T_K^{-1}H_1.
$$
令 $M_0=M\ominus N$。R233 的多值部分公式给
$$
\overline{\mathcal D_H}=CM_0.
\tag{6.3}
$$
新核在旧三块坐标中准确表示为
$$
\mathcal E
=M_0\oplus\{(0,-J_Hc,c):c\in\mathcal D_H\}.
\tag{6.4}
$$
这里 $J_H$ 闭，但未必有界。

对 $m\in M_0$，
$$
\sup_{\substack{e\in\mathcal E\\\|e\|\le1}}
|\mathcal B_N(m,e)|
=
\sup_{\substack{c\in\mathcal D_H\\c\ne0}}
\frac{|\langle m,Cc\rangle|}
{\bigl(\|J_Hc\|^2+\|c\|^2\bigr)^{1/2}}.
\tag{6.5}
$$
右侧是闭图 Hilbert 空间
$(\mathcal D_H,\|c\|_{\rm gr}^2=\|c\|^2+\|J_Hc\|^2)$
到 $CM_0$ 的嵌入 $\iota:c\mapsto c$ 的伴随范数。

若 (6.2) 成立，(6.5) 说明 $\iota^*$ 下方有界，故
$\iota\iota^*\ge\delta^2I$，从而 $\iota$ 满射。于是
$\mathcal D_H=CM_0$，闭图定理使 $J_H$ 有界。

反过来，若 $\mathcal D_H=CM_0$，则 $J_H$ 有界，(6.4) 是有界图参数化。
相对于 $M_0\oplus CM_0$，其双线性型的两个非对角块都是自然的非退化配对，
右下块是有界形式
$\mathcal B_K(J_Hc,J_Hc')$。形如
$$
\begin{pmatrix}0&I\\I&G\end{pmatrix}
$$
的有界块形式具有有界逆
$\begin{pmatrix}-G&I\\I&0\end{pmatrix}$。
因此 (6.2) 成立。综上，
$$
\boxed{
\Pi\text{ 有界}
\iff
\mathcal D_H=CM_0
\iff
\mathcal D_H\text{ 在 }CM\text{ 中闭}.
}
\tag{6.6}
$$

注意 R233 已证明 $\mathcal D_H$ 不可能在整个 $CM$ 中稠密。
式 (6.6) 只比较它与较小的 $CM_0$；并未重新打开已排除的
$F T_K^{-1}$ 全局可闭分支。

## 7. 共同正则器对斜投影域究竟给出什么

由原共同正则器下降得到的 $R_N(s)$ 保持 $\mathcal E$ 与
$\mathcal R$，所以保持 $\operatorname{Dom}\Pi$，并有
$$
\Pi R_N(s)x=R_N(s)\Pi x
\quad(x\in\operatorname{Dom}\Pi).
\tag{7.1}
$$
强趋恒等同时给
$$
R_N(s)x\to x,\qquad
\Pi R_N(s)x\to\Pi x.
\tag{7.2}
$$
若固定 $t>0$，单位比 $R_N(s)=R_N(t)U_{s,N}$ 也保持两个子空间，
则 $R_N(t)\operatorname{Dom}\Pi$ 是 $\Pi$ 的图核心。

这些结论没有证明
$$
R_N(t)K_N\subset\operatorname{Dom}\Pi.
\tag{7.3}
$$
由 (6.1)，(7.3) 等价于实际值域包含
$$
\operatorname{Ran}\bigl(P_{C_N\mathcal E}R_N(t)\bigr)
\subseteq\operatorname{Ran}V,
\tag{7.4}
$$
这正是一个尚未付清的限制除法问题。

若 (7.3) 将来成立，闭图定理才会给 $\Pi R_N(t)$ 全域有界。
目前只有 (7.1)–(7.2) 的已在域内图逼近。也没有证明某个已知循环向量
属于 $\operatorname{Dom}\Pi$；全平面谱并不能提供该信息。

## 8. 原像与闭像之间的严格分离

在旧中央单射条件 (1.3) 下，R233 已给
$$
M_r=M_2\quad(r\ge2).
\tag{8.1}
$$
若 $u=T^2z\in M$，则 $T^3z=0$，且该三次域由
$T^2z\in M\subset\operatorname{Dom}T$ 自动支付。
由 (8.1)，$z\in M_2$，所以 $u=0$。因此
$$
\boxed{
M\cap\operatorname{Ran}T^r=0
\quad(r\ge2),\qquad
M\cap\overline{\operatorname{Ran}T^r}=N\ne0
\quad(r\ge2).
}
\tag{8.2}
$$
第二式使用真实 $C$ 自伴幂与 (8.1)。

这给一个明确的正则化边界。若有界算子 $Q$ 保持 $N$，并在 $N$ 上单射，
则不可能满足
$$
Q N\subseteq\operatorname{Ran}T^2.
\tag{8.3}
$$
否则 $QN\subset N\cap\operatorname{Ran}T^2=0$，与 $N\ne0$、单射性矛盾。
特别，保持实际不变子空间的普遍单射正则器不能被无证地用于把
$N\subset\overline{\operatorname{Ran}T^2}$ 升级成真实二次原像。

此处 (8.3) 与第 7 节新的斜投影域问题是两个不同的值域问题，不能互相替代。

## 9. 新核上的删除缺陷对每个非零向量都必须保留

令 $b_j$ 是 R208 的真实删除算子，并设
$$
b_{j,N}=P_{K_N}b_j|_{K_N}.
$$
由 (2.4)，它保持 $\mathcal D_N$。从 (2.5) 的真实域展开，
$$
[b_{j,N},S]
=P_{K_N}[b_j,T]|_{K_N}+\mathfrak E_j,
$$
$$
\mathfrak E_j
=-P_{K_N}b_jP_NF_N+H_NP_{CN}b_j|_{K_N}.
\tag{9.1}
$$
$\mathfrak E_j\to0$ 强，但没有先给出除以 $a_j$ 的速率。

对 $x,y\in\mathcal E=\ker S$，$C_N$ 对称性给
$$
\mathcal B_N([b_{j,N},S]x,y)=0.
$$
沿 R208 的同一好子列 $a_j^{-1}[b_j,T]\to I$ 强，故
$$
\boxed{
\frac{\mathcal B_N(\mathfrak E_jx,y)}{a_j}
\longrightarrow-\mathcal B_N(x,y).
}
\tag{9.2}
$$
由于新核已证明代数非退化，右侧对任何 $0\ne x\in\mathcal E$ 都不是恒零的
关于 $y$ 的泛函。更准确地，
$$
P_{C_N\mathcal E}\left(\frac{\mathfrak E_jx}{a_j}\right)
\rightharpoonup -P_{C_N\mathcal E}x,
\tag{9.3}
$$
并有
$$
\boxed{
\liminf_j\frac{\|\mathfrak E_jx\|}{|a_j|}
\ge \|P_{C_N\mathcal E}x\|>0
\qquad(0\ne x\in\mathcal E).
}
\tag{9.4}
$$
所有极限和下极限均沿上述好子列。
式 (9.3) 由 (9.2) 对 $C_N\mathcal E$ 中的所有测试向量直接得到；
相应投影序列的有界性也由一致有界原理随之成立。

因此在 $N\ne M$ 分支，对新中央核的每个非零向量，两个跨块项都不能
合起来成为 $o(a_j)$。原空间的强单位交换子在这里被准确抵消，
不是可以再次免费使用的核全等向证明。

## 10. 剩余问题的范围

本稿得到的二择为：

- 若 $N=M$，旧中央单射分支没有二阶广义延长，且二次真实像与原核完全分离。
- 若 $N\ne M$，再次中央约化产生非零、代数非退化、无更高广义延长的新核；
  它与新闭像形成稠密双线性正交直和。其规范投影闭且 $C_N$ 自伴，
  是否有界精确取决于 (6.6)，尚未决定。

本稿没有证明 $N=M$ 或 $N\ne M$ 必定发生其中指定一支，没有证明
$\mathcal D_H$ 闭，没有把代数非退化说成一致非退化，也没有将原物理位算子
无条件下降为新子商上的物理模型。

旧中央本来有核的情形仍只保留第 2 节的准确
$\ker S=M_2/N$；第 3 节的根空间等式在那里可能失效，不能照搬后面的
非退化和斜投影结论。