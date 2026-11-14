# R232：中央核约化中的必需耦合与本质范数

日期：2026-11-12。状态：完整的实际中央结构结论。不宣称这些耦合已经给出高位归一化误差的小量。

## 1. 真实中央分解

沿用 R212 及其中央闭域附录。设

$$
X=a_*I+\sum_j a_jV_j,\quad a\in\ell^2\setminus\ell^1,
\quad Y=\phi(B_2)\in\mathcal A,
\quad T=X-Y,
$$

$$
0\ne M=\ker T,\quad M\perp CM,
\quad L=(CM)^\perp,\quad K=L\ominus M.
\tag{1.1}
$$

$K$ 非零且无限维。原空间分解为 $M\oplus K\oplus CM$，而真实闭域为

$$
\operatorname{Dom}T
=M\oplus\mathcal D_K\oplus CM,
\qquad \mathcal D_K=K\cap\operatorname{Dom}X.
\tag{1.2}
$$

中央附录已证明

$$
T=\begin{pmatrix}
0&F&D\\
0&T_K&H\\
0&0&0
\end{pmatrix},
\qquad \operatorname{Dom}T_K=\mathcal D_K,
\tag{1.3}
$$

其中 $F:K\to M$、$D:CM\to M$、$H:CM\to K$ 有界，$T_K$ 闭且 $C_K$ 自伴，$C_K=C|_K$。

由于 $C$ 交换两个外块，$T^*=CTC$ 的相应块恒等式为

$$
H=C_KF^*C|_{CM}.
\tag{1.4}
$$

因此 $F=0$ 当且仅当 $H=0$。这个结论不要求新中央核存在。

## 2. 两个耦合不可能为零

**定理 2.1。** 在 (1.1) 的实际设置下，

$$
F\ne0,\qquad H\ne0.
\tag{2.1}
$$

**证明。** 假设 $F=0$，则 (1.4) 给 $H=0$。如果 $x\in\ker T_K$，由 (1.3)，$Tx=0$；但 $x\in K$ 且 $\ker T=M$，所以 $x=0$。因此 $T_K$ 单射。又因 $T_K^*=C_KT_KC_K$，其伴随也单射，从而

$$
\overline{\operatorname{Ran}T_K}=K.
\tag{2.2}
$$

$M\subset L$ 是 $A$ 的实际不变旗。因此关于同一正交分解，

$$
A=\begin{pmatrix}
A_M&U&V\\
0&A_K&W\\
0&0&A_c
\end{pmatrix}.
\tag{2.3}
$$

$A$ 保持 $\operatorname{Dom}T$，且 $TA=AT$ 在该域上成立。对 $z\in CM$，$z\in\operatorname{Dom}T$，故 $Az\in\operatorname{Dom}T$。比较 (1.2)、(2.3) 的中央分量可知

$$
W(CM)\subset\mathcal D_K.
\tag{2.4}
$$

这先支付了下面 $T_KW$ 的真实定义域。

在 $F=H=0$ 下，$TA=AT$ 的 $(M,K)$ 块和 $(K,CM)$ 块分别给

$$
UT_Kx=0\quad(x\in\mathcal D_K),
\qquad T_KWz=0\quad(z\in CM).
\tag{2.5}
$$

由 (2.2) 及 $U$ 有界，第一式迫 $U=0$；由 $T_K$ 单射和 (2.4)，第二式迫 $W=0$。于是 $K$ 同时对 $A$、$A^*$ 不变，即 $P_K$ 与 $A$、$A^*$ 都交换。

R31 给 $C^*(A)=\mathfrak U$，其中 $\mathfrak U$ 是当前纯乘积表示中的全部有限物理张量矩阵的范数闭包，其表示不可约。可在这里直接验证所需事实：若正交投影 $P$ 与全部有限局部矩阵交换，令 $Q_m$ 是前 $m$ 位投到参考真空的局部正交投影。它们满足 $Q_m\to P_{\mathbb C1}$ 强，故 $P1=c1$；全部局部矩阵作用于 $1$ 的向量稠密，再由交换关系得 $P=cI$。所以 $P_K$ 只能为零或恒等。

这与 $K\ne0$、$M\ne0$ 及 $K\perp M$ 相矛盾。故 $F\ne0$，再由 (1.4) 得 $H\ne0$。证毕。

本证明利用实际 $A$ 的不可约性，不是从 $T_K$ 的全平面谱推导新核，也没有把一般图投影直接当成闭算子。

## 3. 明确核验有界延拓 $P_MX$ 的高位渐近交换

为了证明非紧性，不能把 $XP_M=YP_M$ 的伴随误认作 $P_MX$。以下重写需要的两个方向。

记 $\mathscr J_j$ 为乘以第 $j$ 位 Walsh 符号的自伴酉算子，并定义

$$
\mathfrak E=\{B\in B(H):[B,\mathscr J_j]\to0\text{ 强*}\}.
\tag{3.1}
$$

这是范数闭 $C^*$ 代数：乘积用交换子 Leibniz 式，伴随用 $\mathscr J_j^*=\mathscr J_j$，范数极限用 $\|[B,\mathscr J_j]\|\le2\|B\|$。所有有限局部矩阵与充分高位的 $\mathscr J_j$ 精确交换，故 $\mathfrak U\subset\mathfrak E$。

### 3.1 不变投影属于 $\mathfrak E$

实际高位有

$$
N_j-\frac{I-\mathscr J_j}{2}\to0\text{ 强},
\qquad N_j+N_j^*-I\to0\text{ 强}.
\tag{3.2}
$$

若 $P$ 是任意 $A$ 不变子空间的正交投影，置 $Q=I-P$，则

$$
QN_jP=0,\qquad PN_j^*Q=0.
$$

因此 $[P,N_j]=PN_jQ=P(N_j+N_j^*-I)Q\to0$ 强，伴随也强趋零。使用 (3.2) 在固定输入上的差，得到 $[P,\mathscr J_j]\to0$ 强；该交换子反自伴，所以也强*趋零。

这适用于 $P_M,P_L$，因而也适用于

$$
P_K=P_L-P_M,\qquad P_{CM}=I-P_L.
\tag{3.3}
$$

此外，

$$
V_j=I-2N_j+2N_j^2(I+N_j)^{-1},
\qquad \|V_j-(I-2N_j)\|\le6\eta_j,
$$

所以

$$
[P_M,V_j]\to0\text{ 强*},
\qquad [P_M,V_j]=P_MV_j(I-P_M),
\tag{3.4}
$$

且交换子的像落在 $M$。

### 3.2 $X^*P_M$ 的有界性及其真实交换子

R161 给 $\operatorname{Dom}X=\operatorname{Dom}X^*$ 和有界自交换子形式。因为 $X|_M=Y|_M$ 有界，

$$
G=X^*P_M\in B(H).
\tag{3.5}
$$

R161 的实际进位计算还给

$$
D_j=[X^*,N_j],\qquad
\|D_j\|\le36\sum_i|a_i|\widetilde R_{ij}\to0,
\tag{3.6}
$$

其中 $\widetilde R_{jj}=1$，$\widetilde R_{ij}=\alpha_{\max(i,j)}/\alpha_{\min(i,j)}\le\eta_*^{|i-j|}$（$i\ne j$）。最后的趋零由 $a\in\ell^2$ 与可和卷积核得出。这个交换子是完整域恒等式，$N_j$ 保持 $\operatorname{Dom}X^*$。

令 $R_j=(I+N_j)^{-1}$。它和 $V_j$ 都保持该域，逆交换子恒等式给

$$
[X^*,V_j]=-2R_jD_jR_j,
\qquad \|[X^*,V_j]\|\le18\|D_j\|\to0.
\tag{3.7}
$$

此处 $R_j$ 只是本节的有界逆记号，不是另一稿的物理头图平方根。

由 (3.4) 的像包含，$X^*[P_M,V_j]=G[P_M,V_j]$ 有定义且有界。所以

$$
[G,V_j]=G[P_M,V_j]+[X^*,V_j]P_M\to0\text{ 强}.
\tag{3.8}
$$

### 3.3 伴随方向确实给 $P_MX$，而不是 $P_MX^*$

置 $Z=G^*\in B(H)$。对所有 $f\in\operatorname{Dom}X$，

$$
Zf=P_MXf.
\tag{3.9}
$$

因此，使用 $V_j$ 保持 $\operatorname{Dom}X$ 且与 $X$ 作域交换，

$$
[Z,V_j]f=[P_M,V_j]Xf\longrightarrow0
\quad(f\in\operatorname{Dom}X).
\tag{3.10}
$$

$Z$ 有界、$\sup_j\|V_j\|<\infty$，故交换子范数一致有界。由域稠密性，(3.10) 延拓到每个固定 $f\in H$。

又有 $V_j-\mathscr J_j\to0$ 强，故分别在 (3.8)、(3.10) 中替换固定输入输出，得到

$$
[G,\mathscr J_j]\to0\text{ 强},
\qquad[Z,\mathscr J_j]\to0\text{ 强}.
$$

$Z=G^*$，这恰好同时支付两个伴随方向。因此

$$
\boxed{\quad G=X^*P_M\in\mathfrak E,
\qquad Z=(X^*P_M)^*\in\mathfrak E,
\quad Z|_{\operatorname{Dom}X}=P_MX.
\quad}
\tag{3.11}
$$

这里没有使用 $XP_M$ 的伴随来替代所需延拓。

## 4. 两个中央耦合的本质范数等于原范数

把 $F:K\to M$ 以零延拓看成全空间算子 $\widetilde F$。由真实中央域上的定义及有界延拓唯一性，

$$
\widetilde F=(Z-P_MY)P_K.
\tag{4.1}
$$

式 (3.3)、(3.11) 以及 $Y\in\mathcal A\subset\mathfrak U$ 说明

$$
\widetilde F\in\mathfrak E.
\tag{4.2}
$$

为自含起见，若 $B\in\mathfrak E$、$x$ 是固定单位向量、$Q$ 紧，则 $\mathscr J_jx\rightharpoonup0$，故 $Q\mathscr J_jx\to0$，而

$$
B\mathscr J_jx-\mathscr J_jBx\to0.
$$

所以 $\|B+Q\|\ge\|Bx\|$。对 $x$ 取上确界、对紧 $Q$ 取下确界，得到

$$
\|B\|_{\mathrm{ess}}=\|B\|.
\tag{4.3}
$$

应用于 (4.2)，并注意矩形算子与其零延拓具有相同本质范数，得

$$
\boxed{\quad
\|F:K\to M\|_{\mathrm{ess}}=\|F\|>0.
\quad}
\tag{4.4}
$$

由 (1.4) 的两个反酉变换，同样有

$$
\boxed{\quad
\|H:CM\to K\|_{\mathrm{ess}}=\|H\|=\|F\|>0.
\quad}
\tag{4.5}
$$

特别地，两者都无限秩且不紧。中央正量 $F^*F$ 也满足

$$
\|F^*F\|_{\mathrm{ess}}=\|F\|^2>0.
\tag{4.6}
$$

还可保留一个直接的实际弱复制形式：对任意固定单位 $x\in K$，令 $x_j=P_K\mathscr J_jx$。由于 $P_K\in\mathfrak E$，$x_j-\mathscr J_jx\to0$，故 $\|x_j\|\to1$、$x_j\rightharpoonup0$；并由 (4.2)，

$$
\|Fx_j\|\longrightarrow\|Fx\|.
\tag{4.7}
$$

这展示了非零耦合不能由有限秩修正消除。

## 5. 与中央递归缺陷的关系

R212 中央附录的两个误差项为

$$
\mathcal E_j
=-P_Kb_jP_MF+H P_{CM}b_j|_K.
$$

本稿证明其中的两个固定耦合算子 $F,H$ 必须真实存在，而且不能作为紧误差删去。但它没有证明 $a_j^{-1}\mathcal E_j$ 的强极限，也没有由 $F^*F>0$ 宣布中央双线性型正定。

尤其，$F,H$ 非紧与 $b_j\to0$ 强并不矛盾；(4.7) 的弱复制也未给随输入变化而统一的 $b_j/a_j$ 预算。中央核上的精确配对抵消式仍是下一步必须处理的实际条件。
