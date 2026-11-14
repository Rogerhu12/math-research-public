# R233：中央非对角商的可闭性与广义核投影

日期：2026-11-12。状态：完整真实域说明及可闭分支排除。若中央算子单射，则本稿证明其非对角商必不可闭；不宣称排除原慢分支核。

## 1. 设置及本稿的额外条件

沿用 R212 中央闭域附录：

$$
H=M\oplus K\oplus CM,
\qquad \operatorname{Dom}T=M\oplus\mathcal D_K\oplus CM,
$$

$$
T=\begin{pmatrix}0&F&D\\0&T_K&H_1\\0&0&0\end{pmatrix},
\qquad T_K^*=C_KT_KC_K,
\qquad H_1=C_KF^*C|_{CM}.
\tag{1.1}
$$

$F,D,H_1$ 有界，$\ker T=M$，$L=(CM)^\perp=M\oplus K$。原 $A$ 的块形式为

$$
A=\begin{pmatrix}A_M&U&V\\0&A_K&W\\0&0&A_c\end{pmatrix}.
\tag{1.2}
$$

在本稿中额外假设

$$
\boxed{\ker T_K=0.}
\tag{1.3}
$$

由 $C_K$ 自伴性，$T_K^*$ 也单射，$T_K$ 及 $T_K^*$ 都有稠密值域。若 (1.3) 不成立，本稿讨论的 $T_K^{-1}$ 不能作为单值算子使用，应返回 R212 中央核分支。

## 2. 实际非对角商及其原参数核心

定义稠密域算子

$$
G=F T_K^{-1}:\operatorname{Ran}T_K\subset K\longrightarrow M,
\qquad G(T_Kx)=Fx\quad(x\in\mathcal D_K).
\tag{2.1}
$$

其图正好是 $T(\operatorname{Dom}T\cap L)$ 在 $(M,K)$ 两坐标交换后的集合：

$$
\operatorname{Graph}G
=\{(T_Kx,Fx):x\in\mathcal D_K\}.
\tag{2.2}
$$

左乘有界算子 $F$ 并不自动保留闭性。因此，虽然 $T_K^{-1}$ 闭，(2.1) 此时还不能宣称闭或可闭。

取共同一阶正则器的中央子商 $R_K=R_K(t)$。记

$$
S_K=T_KR_K\in B(K).
$$

固定参数单位比 $R_K(s)=R_KU_{s,K}$ 和中央图核心给

$$
\boxed{\quad
\overline{\operatorname{Graph}G}
=\overline{\{(S_Kz,F R_Kz):z\in K\}}.
\quad}
\tag{2.3}
$$

具体地，对 $x\in\mathcal D_K$，令 $x_s=R_K(s)x$。则 $x_s\to x$、$T_Kx_s\to T_Kx$，而 $Fx_s\to Fx$；又 $x_s=R_KU_{s,K}x$，所以每个逼近对都在 (2.3) 右侧参数集合中。反向包含来自 $R_KK\subset\mathcal D_K$。

$S_K$ 单射且稠密值域：单射性由两个因子单射，稠密像由 $R_KK$ 是 $T_K$ 的图核心及 $\operatorname{Ran}T_K$ 稠密得出。但这些性质与 (2.3) 本身并不排除图闭包含非零竖直部分。

## 3. 伴随域的准确判据

对 $m\in M$，$m\in\operatorname{Dom}G^*$ 当且仅当存在 $z\in K$ 使

$$
\langle Fx,m\rangle=\langle T_Kx,z\rangle
\qquad(x\in\mathcal D_K).
$$

由 $T_K^*$ 的定义，这等价于 $z\in\operatorname{Dom}T_K^*$ 且 $T_K^*z=F^*m$。单射性使 $z$ 唯一。因此

$$
\boxed{\quad
\operatorname{Dom}G^*
=\{m\in M:F^*m\in\operatorname{Ran}T_K^*\},
\qquad G^*m=(T_K^*)^{-1}F^*m.
\quad}
\tag{3.1}
$$

这里 $G^*$ 的域未必稠密。稠密定义算子 $G$ 可闭的充要条件正是 $\operatorname{Dom}G^*$ 在 $M$ 中稠密。

利用 (1.1) 的共轭关系，置

$$
\mathcal D_H
=\{c\in CM:H_1c\in\operatorname{Ran}T_K\},
\qquad J_Hc=T_K^{-1}H_1c.
\tag{3.2}
$$

$J_H$ 是域为 $\mathcal D_H$ 的闭算子：若 $c_n\to c$、$J_Hc_n\to k$，则 $T_KJ_Hc_n=H_1c_n\to H_1c$；$T_K$ 闭性给 $k\in\mathcal D_K$ 且 $T_Kk=H_1c$。这里没有假定 $\mathcal D_H$ 稠密。

式 (3.1) 等价于

$$
\operatorname{Dom}G^*=C\mathcal D_H,
\qquad G^*=C_KJ_HC|_{\operatorname{Dom}G^*}.
\tag{3.3}
$$

## 4. 原二次广义核的实际参数化

设 $f=(m,k,c)\in\operatorname{Dom}T$。由 (1.1)，

$$
Tf=(Fk+Dc,\ T_Kk+H_1c,\ 0).
$$

若 $f\in\ker T^2$，则 $Tf\in\ker T=M$，所以

$$
T_Kk+H_1c=0.
$$

反过来，若 $c\in\mathcal D_H$、$k=-J_Hc$，则 $Tf\in M\subset\operatorname{Dom}T$，故真实自然二次域已经付清，且 $T^2f=0$。因此

$$
\boxed{\quad
\ker T^2
=M\oplus\{(0,-J_Hc,c):c\in\mathcal D_H\}.
\quad}
\tag{4.1}
$$

第二项的图闭性由 $J_H$ 闭性得到，并不要求该图在 $CM$ 上有全域。

特别地，记 $p_{CM}$ 为第三坐标投影，则

$$
p_{CM}(\ker T^2)=\mathcal D_H.
\tag{4.2}
$$

由 (3.3)，得到准确的分叉：

$$
\boxed{\quad
G\text{ 可闭}
\iff
\overline{p_{CM}(\ker T^2)}=CM.
\quad}
\tag{4.3}
$$

还有对应的有界分支：

$$
\boxed{\quad
G\text{ 有有界全域延拓}
\iff
p_{CM}(\ker T^2)=CM.
\quad}
\tag{4.4}
$$

证明 (4.4) 的反向时，$\mathcal D_H=CM$ 使闭算子 $J_H$ 全域，闭图定理给它有界，故 (3.3) 给 $G^*$ 全域有界，从而 $G$ 的闭包是有界全域算子。正向则直接由有界延拓得到 $\operatorname{Dom}G^*=M$。

所以“投影稠密”与“投影满射”分别对应可闭和有界延拓，不能混同。第 7 节将利用实际删除交换子排除本题的投影稠密情形，从而同时排除这两个分支。

## 5. 非齐次不变图及多值部分

$TA=AT$ 的 $(M,K)$ 块给

$$
FA_Kx=A_MFx+UT_Kx\quad(x\in\mathcal D_K).
\tag{5.1}
$$

$T_K$ 与 $A_K$ 作域交换。因此 $A_K$ 保持 $\operatorname{Ran}T_K$，且在这个域上

$$
\boxed{\quad
GA_K=A_MG+U.
\quad}
\tag{5.2}
$$

这是非齐次式。不能删掉实际 $U$，将 $G$ 叫作普通模交织算子。

在 $(K,M)$ 的坐标顺序中，图 (2.2) 对有界三角算子

$$
\begin{pmatrix}A_K&0\\U&A_M\end{pmatrix}
\tag{5.3}
$$

不变，因而其闭包也不变。定义闭图关系的多值部分

$$
N=\{m\in M:(0,m)\in\overline{\operatorname{Graph}G}\}.
\tag{5.4}
$$

由 (5.3)，$N$ 是 $A_M$ 的闭不变子空间。一般稠密定义算子的图正交补判据给

$$
N=(\overline{\operatorname{Dom}G^*})^\perp_M
=C\left[(\overline{\mathcal D_H})^\perp_{CM}\right].
\tag{5.5}
$$

这里可直接验证竖直部分公式：与图正交的向量恰为 $(-G^*m,m)$、$m\in\operatorname{Dom}G^*$；一个竖直向量 $(0,n)$ 与这些向量全正交，当且仅当 $n\perp\operatorname{Dom}G^*$。

若

$$
E=\overline{T(\operatorname{Dom}T\cap L)}\subset L,
$$

则交换坐标识别给 $N=E\cap M$。因此 (5.5) 是实际原算子限制像闭包中的子空间，而不是只在形式关系空间中出现的符号。

作为一般图分类，$N=0$ 等价于图可闭；第 7 节将排除本题的这一情形。若 $0\ne N\ne M$，留下一个真正的多值不变部分；若 $N=M$，则 $\mathcal D_H=0$，(4.1) 给 $\ker T^2=M$。此时图闭包是整个 $K\oplus M$：它包含全部竖直 $M$，第一坐标投影又包含稠密的 $\operatorname{Ran}T_K$，闭性即给全空间。

## 6. 中央无核时所有更高广义核在二阶稳定

在本稿条件 (1.3) 下，还可得到

$$
\boxed{\quad
\ker T^n=\ker T^2\qquad(n\ge2),
\quad}
\tag{6.1}
$$

其中每个幂都取真实自然域。

事实上，$\operatorname{Ran}T\subset L$。若 $T^nf=0$、$n\ge2$，令 $y=Tf\in L$。在 $L=M\oplus K$ 上，$T$ 的限制是

$$
\begin{pmatrix}0&F\\0&T_K\end{pmatrix}
\quad\text{于 }M\oplus\mathcal D_K.
$$

自然迭代的中央分量是 $T_K$ 的相应自然幂。由于 $T_K$ 单射，它的所有自然幂都单射，所以 $T^{n-1}y=0$ 迫 $y$ 的中央分量为零，即 $y\in M$。于是 $T^2f=0$。反向包含来自 $TM=0$，而 $M\subset\operatorname{Dom}T$ 自动支付后续全部自然域。

式 (6.1) 不排除二阶广义核严格大于 $M$；其可能性由 (4.1) 中尚未判定的 $\mathcal D_H$ 精确记录。

## 7. 实际广义链恒等式关闭可闭分支

本节先不需要 (1.3)。记 $M_r=\ker T^r$，全部幂取真实自然域。R208 给一列 $j\to\infty$，$a_j\ne0$，使

$$
b_j\operatorname{Dom}T\subseteq\operatorname{Dom}T,
\qquad a_j^{-1}[b_j,T]\longrightarrow I\quad\text{强}.
\tag{7.1}
$$

### 7.1 有限广义链的望远镜恒等式

取 $r\ge1$、$u,v\in M_r$。每个 $T^ku$、$T^{r-1-k}v$（$0\le k<r$）都在 $\operatorname{Dom}T$，所以 $b_jT^ku$ 也在该域。$C$ 对称性逐项给

$$
\begin{aligned}
&\mathcal B([b_j,T]T^ku,T^{r-1-k}v)\\
&\quad=\mathcal B(b_jT^{k+1}u,T^{r-1-k}v)
-\mathcal B(b_jT^ku,T^{r-k}v).
\end{aligned}
$$

对 $k$ 求和即得准确望远镜式

$$
\sum_{k=0}^{r-1}
\mathcal B([b_j,T]T^ku,T^{r-1-k}v)
=\mathcal B(b_jT^ru,v)-\mathcal B(b_ju,T^rv)=0.
\tag{7.2}
$$

这里仅使用 $b_j$ 保持一次域，没有假定它保持 $\operatorname{Dom}T^r$。

沿 (7.1) 的好子列除以 $a_j$ 并取强极限，有限和变为

$$
\sum_{k=0}^{r-1}\mathcal B(T^ku,T^{r-1-k}v)
=r\,\mathcal B(T^{r-1}u,v)=0.
$$

所以

$$
\boxed{\quad
\mathcal B(T^{r-1}\ker T^r,\ker T^r)=0
\qquad(r\ge1).
\quad}
\tag{7.3}
$$

$r=1$ 恢复原核全等向性；$r=2$ 是这里需要的新链约束。

### 7.2 任何有限阶广义核在 $CM$ 上的投影都不稠密

因为 $M\perp CM$ 且 $M\ne0$，$p_{CM}M=0$ 不稠密。现在对 $r\ge2$ 归纳：若 $p_{CM}M_r$ 稠密于 $CM$，则对任意 $u\in M_r$，向量 $T^{r-1}u\in M$。由 (7.3)，它与 $M_r$ 双线性正交，因而与其稠密的 $CM$ 投影配对为零。这迫使 $T^{r-1}u=0$。

于是 $M_r=M_{r-1}$，与归纳假设矛盾。故

$$
\boxed{\quad
\overline{p_{CM}(\ker T^r)}\ne CM
\qquad\text{对每个有限 }r\ge1.
\quad}
\tag{7.4}
$$

这个结论不需要中央算子单射。

在当前设置，$T^r$ 是最高系数为单位的实际有界系数多项式，域为 $\operatorname{Dom}X^r$：$Y$ 与 $X$ 作域交换并保持每个幂域，故 $(X-Y)^r$ 的自然域与该多项式域一致。R176 因而给 $T^r$ 闭且 $C$ 自伴。于是可将 (7.4) 写成实际非零子空间

$$
\boxed{\quad
N_r:=M\cap\overline{\operatorname{Ran}T^r}
=M\cap(C\ker T^r)^\perp\ne0.
\quad}
\tag{7.5}
$$

这些 $N_r$ 都是闭 $A$ 不变子空间，且

$$
N_{r+1}\subseteq N_r,\qquad
T^{r-1}\ker T^r\subseteq N_r.
\tag{7.6}
$$

每个非零 $N_r$ 必无限维：实际 $A$ 单射且拟幂零，不能在非零有限维不变空间上仍保持单射。没有由各 $N_r\ne0$ 推出它们的无限交非零。

### 7.3 非对角商必不可闭

现在恢复 (1.3)。由 (4.3) 与 (7.4) 的 $r=2$ 情形，

$$
\boxed{\quad G=F T_K^{-1}\text{ 不可闭。}\quad}
\tag{7.7}
$$

所以 (5.4) 的多值部分必须非零，且由 (5.5)、(7.5)，

$$
\boxed{\quad
N=N_2=M\cap\overline{\operatorname{Ran}T^2}\ne0,
\qquad T\ker T^2\subseteq N.
\quad}
\tag{7.8}
$$

也可以直接看出矛盾：若 $\mathcal D_H$ 稠密，取 $u_c=(0,-J_Hc,c)$，则 $Tu_c\in M$。式 (7.3) 使 $Tu_c$ 与稠密的 $\mathcal D_H$ 配对为零，故 $Tu_c=0$，于是 $u_c\in M$ 迫 $c=0$。这将给 $\mathcal D_H=0$，不能在非零 $CM$ 中稠密。

### 7.4 原限制像的闭包确为平方像闭包

本稿中的 $E=\overline{T(\operatorname{Dom}T\cap L)}$ 还有准确识别

$$
\boxed{\quad E=\overline{\operatorname{Ran}T^2}.\quad}
\tag{7.9}
$$

一个包含由 $\operatorname{Ran}T\subset L$ 直接得到。为证明反向，取 $x\in\operatorname{Dom}T\cap L$，并选 $Tz_n\to x$。固定 $s>0$，$R(s)$ 映全空间入 $\operatorname{Dom}T$，保持该域并与 $T$ 交换。因此

$$
w_{n,s}=R(s)Tz_n=T R(s)z_n
$$

落在 $\operatorname{Ran}T\cap\operatorname{Dom}T$，而 $R(s)z_n\in\operatorname{Dom}T^2$。又因 $TR(s)$ 有界，

$$
w_{n,s}\to R(s)x,\qquad
Tw_{n,s}\to TR(s)x.
$$

所以 $TR(s)x\in\overline{\operatorname{Ran}T^2}$。再令 $s\downarrow0$，共同图逼近给 $TR(s)x\to Tx$，得到 (7.9)。这里没有直接把范数稠密的 $\operatorname{Ran}T$ 当成图稠密；先固定真实正则器才完成两段极限。

在中央单射条件下，(6.1) 和 $C$ 自伴性进一步给

$$
\overline{\operatorname{Ran}T^n}
=\overline{\operatorname{Ran}T^2},
\qquad N_n=N_2=N\qquad(n\ge2).
\tag{7.10}
$$

## 8. 剩余的实际分叉

本稿已排除中央单射时 $F T_K^{-1}$ 的可闭分支，因而也排除其有界延拓；不是仅记录一个尚未决定的二择。

尚未判定的是 $N$ 等于 $M$ 还是为其真子空间，以及中央核是否本来就非零。若 $N=M$，则 $\ker T^2=M$ 且闭图关系为整个 $K\oplus M$；若 $0\ne N\ne M$，得到更细的实际不变子空间与非零多值部分。两者都与当前已知条件相容，尚不构成对原 $M$ 的矛盾。

在不假设中央单射时，(7.3)–(7.6) 仍成立，但不能把它们升级为所有广义核全等向、所有 $N_r=M$ 或无限交非零。下一步仍需利用原分支的实际系数、尾进位或中央耦合来缩小这些剩余情形。
