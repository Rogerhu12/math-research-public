# R212 附录：中央闭域、最大图与递归交换子的精确缺陷

日期：2026-11-12。状态：完整域与压缩接口。本稿不宣称中央核自动全等向。

## A. 设置与域的独立一致性检查

沿用 R212 主稿：$X$ 是实际非 $\ell^1$ 一阶闭算子，

$$
\operatorname{Dom}X=\operatorname{Dom}X^*,
\quad X^*=CXC,
\quad Y=\phi(B_2)\in\mathcal A,
\quad T=X-Y,
$$

$$
0\ne M=\ker T,\qquad M\perp CM,
\qquad L=(CM)^\perp,\qquad K=L\ominus M.
\tag{A.1}
$$

记 $M^c=CM$，相应三个正交投影为 $P_M,P_K,P_{M^c}$。

首先，$M\subset\operatorname{Dom}X$。由 $C$ 自伴性，$M^c\subset\operatorname{Dom}X^*$，再由通常伴随同域性得到 $M^c\subset\operatorname{Dom}X$。所以 $P_M$ 和 $P_{M^c}$ 都把全空间映入 $\operatorname{Dom}X$，而 $P_K=I-P_M-P_{M^c}$ 保持该域。于是

$$
\operatorname{Dom}X
=M\oplus\mathcal D_K\oplus M^c,
\qquad \mathcal D_K=K\cap\operatorname{Dom}X,
\tag{A.2}
$$

且 $\mathcal D_K$ 在 $K$ 中稠密。

这已经给出 R212 中 $K$ 无限维结论的另一个独立检查：若 $K$ 有限维，则其稠密线性子空间 $\mathcal D_K$ 等于 $K$，(A.2) 迫 $\operatorname{Dom}X=H$。闭图定理将使 $X$ 有界，与非 $\ell^1$ 一阶行相反。这个短域论证不代替 R212 的定量 $\kappa_j$ 结论。

## B. 真实上三角闭算子与通常伴随

记 R161 的有界自交换子二次型为 $C_a$，$c_a=\|C_a\|$。在 $M$ 上 $X=Y$，故

$$
\|X^*|_M\|\le\sqrt{\|Y\|^2+c_a}.
$$

在 $M^c$ 上有 $X^*=Y^*$，同一二次型给出

$$
\|X|_{M^c}\|\le\sqrt{\|Y\|^2+c_a}.
\tag{B.1}
$$

$M$ 对 $X$ 不变，$M^c$ 对 $X^*$ 不变。因此，关于 (A.2) 的分解，$X$ 有真正的上三角形式

$$
X=\begin{pmatrix}
X_M&B&D\\
0&X_K&E\\
0&0&X_c
\end{pmatrix},
\qquad
\operatorname{Dom}X=M\oplus\mathcal D_K\oplus M^c.
\tag{B.2}
$$

这里 $X_M,X_c,B,D,E$ 均有界。特别地，$B=P_MX|_{\mathcal D_K}$ 的有界延拓来自有界算子 $X^*P_M$ 的伴随，而 $D,E$ 来自 (B.1)。不能只凭 $X_M$ 有界就宣布 $B$ 有界。

$X_K=P_KX|_{\mathcal D_K}$ 是闭算子。事实上，若 $x_n\to x\in K$ 且 $X_Kx_n\to y$，则

$$
Xx_n=Bx_n+X_Kx_n\longrightarrow Bx+y;
$$

闭性迫 $x\in\operatorname{Dom}X$ 且 $X_Kx=y$。

由于除中央块外全为有界算子，(B.2) 的通常伴随域是

$$
M\oplus\operatorname{Dom}X_K^*\oplus M^c.
$$

比较 $\operatorname{Dom}X^*=\operatorname{Dom}X$，得到

$$
\operatorname{Dom}X_K^*=\mathcal D_K.
\tag{B.3}
$$

$C$ 交换两个外块并保持 $K$。由 $X^*=CXC$ 还得到

$$
X_K^*=C_KX_KC_K,
\qquad C_K=C|_K.
\tag{B.4}
$$

中央块继承有界自交换子二次型：对 $x\in\mathcal D_K$，

$$
\|X_Kx\|^2-\|X_K^*x\|^2
=\langle (P_KC_a|_K-B^*B+EE^*)x,x\rangle.
\tag{B.5}
$$

这是通常伴随的真实块计算。右侧不只是 $P_KC_aP_K$；两个有界跨块能量项必须保留。

## C. 中央分支是自然闭商，而不是未经识别的压缩

$Y$ 及其伴随保持相应不变旗，所以它也是有界上三角块矩阵。其中央块

$$
Y_K=P_KY|_K=\phi((B_2)_K)
$$

属于 $\overline{\operatorname{alg}}(A_K)$，保持 $\mathcal D_K$，并在该域上与 $X_K$ 交换。

定义

$$
T_K=X_K-Y_K,\qquad\operatorname{Dom}T_K=\mathcal D_K.
\tag{C.1}
$$

它闭、$C_K$ 自伴，并满足 $\operatorname{Dom}T_K=\operatorname{Dom}T_K^*$。$T$ 的两个外侧对角块都是零，故可写成

$$
T=\begin{pmatrix}
0&F&D_T\\
0&T_K&H_1\\
0&0&0
\end{pmatrix},
\tag{C.2}
$$

其中 $F:K\to M$、$H_1:M^c\to K$、$D_T:M^c\to M$ 有界。

$T$ 在 $L$ 上的闭限制域为 $M\oplus\mathcal D_K$。将其图投影到 $(L/M)^2$，得到的正好是

$$
\{(x,T_Kx):x\in\mathcal D_K\}.
\tag{C.3}
$$

因为 $T_K$ 已证明闭，这个自然商图无需再扩大闭包。这里没有直接把一般无界算子的图投影说成闭图。

## D. 与共同正则器最大图及原参数核心相容

取 R128/R140 的共同一阶正则器 $R(t)$，固定一个 $t>0$ 并写 $R=R(t)$。所需实际性质为

$$
R(s)H\subset\operatorname{Dom}X,\qquad
XR\in\{A\}',\qquad R(s)\to I\ \text{强},
$$

$$
R(s)=R\,U_s,
\qquad U_s\in\{A\}'\ \text{有界单位}.
\tag{D.1}
$$

各正则器、单位比以及 $S=TR=XR-YR$ 都保持 $M,L$，所以有真实子商算子 $R_K(s),R_K,U_{s,K},S_K$。

从 (D.1)，$R_K(s)=R_KU_{s,K}\to I_K$ 强。因此 $R_K$ 单射且值域稠密：若 $R_Kx=0$，与 $U_{s,K}$ 交换后得到 $R_K(s)x=0$，令 $s\downarrow0$ 即得 $x=0$；其稠密值域也由 $R_K(s)K\subset\operatorname{Ran}R_K$ 得到。

中央块计算给出

$$
T_KR_K=S_K\quad\text{在全 }K\text{ 上},
\qquad
R_KT_K=S_K\quad\text{在 }\mathcal D_K\text{ 上}.
\tag{D.2}
$$

因此自然图包含于最大关系 $S_Kx=R_Ky$。反过来，若 $S_Kx=R_Ky$，令 $x_s=R_K(s)x\in\mathcal D_K$，则

$$
R_KT_Kx_s=S_KR_K(s)x
=R_K(s)S_Kx
=R_KR_K(s)y.
$$

由 $R_K$ 单射，$T_Kx_s=R_K(s)y$。强极限与 $T_K$ 闭性迫 $x\in\mathcal D_K$、$T_Kx=y$。所以

$$
\boxed{\quad
\operatorname{Graph}T_K
=\{(x,y)\in K^2:S_Kx=R_Ky\}.
\quad}
\tag{D.3}
$$

此外，$R_K(s)=R_KU_{s,K}$ 对每个域向量给出图逼近。因此

$$
\{(R_Kz,S_Kz):z\in K\}
\tag{D.4}
$$

是该最大图的原参数核心。这证明了原最大图与这里的自然商图确实相容。

同一论证将 $S$ 换为 $XR$，也识别 $X_K$ 本身的共同正则器最大闭图。

## E. 中央核的准确识别

对 $x\in\mathcal D_K$，由 (C.2)，

$$
Tx=Fx+T_Kx.
$$

所以 $T_Kx=0$ 当且仅当 $Tx\in M$。由于 $M\subset\operatorname{Dom}T$ 且 $TM=0$，这一条件自动给出真实自然二次域。因此

$$
\boxed{\quad
\ker T_K=K\cap\ker T^2
\cong (\ker T^2\cap L)/M.
\quad}
\tag{E.1}
$$

这里不能去掉 $\ker T^2\cap L$ 中的 $L$。本稿没有证明整个 $\ker T^2$ 都包含在 $L=(CM)^\perp$ 中。

若 $M_1=\ker T_K\ne0$，则 $M_1\subset\mathcal D_K$ 且 $X_K|_{M_1}=Y_K|_{M_1}$ 有界。它对 $A_K$ 不变，但它是否对 $C_K$ 全等向，需要新的证明。

## F. 中央交换子的两个真实误差项

令 $b_j$ 为 R208 使用的 Walsh 删除算子。它在原空间保持 $\operatorname{Dom}T$，且 $[b_j,T]$ 有界。由 (A.2)，压缩

$$
b_{j,K}=P_Kb_j|_K
$$

保持 $\mathcal D_K$。直接使用 (C.2)，在这个真实域上得到

$$
[b_{j,K},T_K]
=P_K[b_j,T]|_K
-P_Kb_jP_MF
+H_1P_{M^c}b_j|_K.
\tag{F.1}
$$

记最后两项之和为 $\mathcal E_j$。因为 $b_j\to0$ 强，$F,H_1$ 有界，确有 $\mathcal E_j\to0$ 强。然而沿 R208 的好子列，主项的尺度为 $a_j$：

$$
a_j^{-1}P_K[b_j,T]|_K\longrightarrow I_K\quad\text{强}.
\tag{F.2}
$$

单凭 $\mathcal E_j\to0$ 强，不能把它从除以 $a_j$ 的式子中删去。

这个缺口可以精确写到中央核的配对上。令 $x,y\in M_1=\ker T_K$，并记 $\mathcal B_K(x,y)=\langle x,C_Ky\rangle$。$T_K$ 的 $C_K$ 自伴性和 $b_{j,K}$ 的域保持给出

$$
\mathcal B_K([b_{j,K},T_K]x,y)=0.
$$

故 (F.1) 意味着精确恒等式

$$
\mathcal B_K(\mathcal E_jx,y)
=-\mathcal B([b_j,T]x,y).
\tag{F.3}
$$

沿 (F.2) 的好子列，

$$
\boxed{\quad
\frac{\mathcal B_K(\mathcal E_jx,y)}{a_j}
\longrightarrow-\mathcal B_K(x,y).
\quad}
\tag{F.4}
$$

所以中央核若并非全等向，则这些跨块项恰在 $a_j$ 尺度上保留了非零配对，而不是可自动忽略的误差。对任何 $y\ne0$，沿 (F.2) 的同一好子列取下极限，还得到

$$
\liminf_j\frac{\|\mathcal E_jx\|}{|a_j|}
\ge\frac{|\mathcal B_K(x,y)|}{\|y\|}.
\tag{F.5}
$$

反过来，若能从额外实际结构证明 $a_j^{-1}\mathcal E_jx\to0$ 对所有 $x\in M_1$ 成立，才可由 (F.4) 推出中央核全等向。本稿没有证明这个速率。

## G. 无界性与谱类在中央块中保留

$X_K$ 必无界；否则 (B.2) 全部块有界且域为全空间，$X$ 也会有界。$T_K=X_K-Y_K$ 同样无界。

还可识别其谱集合。R138 对原非 $\ell^1$ 一阶 $X$ 只留下空谱或全平面两支。若 $X$ 空谱，则 $R_0=X^{-1}$ 有界拟幂零，且与 $Y$ 交换。于是

$$
T=(I-YR_0)X
$$

在原自然域上具有有界逆，违 $M\ne0$。因此本稿条件下 $\sigma(X)=\mathbb C$。

令 $c=\chi(Y)=\phi(0)$。两个有界外对角块 $X_M=Y_M$、$X_c=Y_c$ 的谱都是 $\{c\}$。对 $\lambda\ne c$，(B.2) 的两外块可逆，真实上三角求解给出

$$
\lambda\in\rho(X)
\iff\lambda\in\rho(X_K).
\tag{G.1}
$$

因为原空间没有预解点，中央块也不能在 $\mathbb C\setminus\{c\}$ 有预解点；预解集开放性再排除唯一余点 $c$。故

$$
\sigma(X_K)=\mathbb C.
\tag{G.2}
$$

$Y_K-cI$ 是与 $X_K$ 作域交换的有界拟幂零算子。交换的有界拟幂零扰动不改变闭算子的预解集：在任一预解参数下，余下因子是 $I$ 加交换拟幂零乘积，因此可逆；反方向同理。所以

$$
\sigma(T_K)=\mathbb C.
\tag{G.3}
$$

这些只是谱集合与真实域的结论，不排除中央零核，也不证明其存在。尤其 (F.4) 表明，具有相同全平面谱和通常伴随同域，并不足以免费重跑原空间 R208 的全等向证明。

## H. 依赖与保留边界

- R161：原 $X$ 的通常伴随同域与有界自交换子。
- R128/R140：共同正则器、固定参数单位比及强趋恒等。
- R138：原非 $\ell^1$ 一阶算子的谱分类。
- R208：原核全等向、真实删除算子域保持及高位归一化交换子极限。
- R212 主稿：中央实际不变旗及定量逃逸成本。

中央图的闭性、最大图等式、原参数核心和 (E.1) 已在本稿各自证明；没有把一般图投影自动当闭算子，也没有把原空间的物理反射或有限柱测试无条件传给未知子商。
