# R293 附录：全出生首阶与全高度加强 S1 的统一常数等价

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：以下有限模型传输及量词等价已证明；没有证明该统一常数有限。** 本稿续[首阶 S1/S2 强位传输](R293-heavy-bit-transfer-of-strengthened-first-edge-sos.md)。新增是一般高度的双分支极限，从而将其中首阶到第二阶的结论真正迭代；并非未经核验地反复套用首阶公式。

## 1. 加强缺陷与常数

对一个任意有限正权 Boolean 行，在出生 $s$ 及下出生 $s-1$ 使用同一实际归一最小逆 Gram $G_j,L_j$，令
$$
C_j=G_j^{-1},\qquad G_0=I,\qquad
B=\left.\sum b_i^3E_i\right|_{K_s}.
$$
完整高度为 $h=N-2s$。对 $1\le n\le h$，在最高处令 $C_{h+1}=0$；其余逆只在真正合法高度使用。定义
$$
\delta_{n+1}=\frac1{n+1}(C_nB^*L_{n+2}-C_{n-1}B^*L_{n+1}),
$$
$$
\boxed{
E_n^{(\kappa)}=
\kappa C_nG_{n-1}C_n-C_{n+1}
-\delta_{n+1}L_{n+2}^{-1}\delta_{n+1}^*,\qquad \kappa>0.
}
\tag{1.1}
$$
出生零时省略下出生及桥项。$\kappa=1,n=1$ 是 R275 的 S1。所有项齐次缩放一致；这里只研究一个固定的、与位数、权行、出生、高度无关的 $\kappa$。

**定理。** 下列两命题等价：

1. 每个有限正权 Boolean 行及每个高度至少为一的出生，都满足 $E_1^{(\kappa)}\succeq0$；
2. 每个有限正权 Boolean 行及每个合法出生、全部 $1\le n\le h$，都满足 $E_n^{(\kappa)}\succeq0$。

若某个实际第 $m$ 高度严格违反 (1.1)，则加入 $m-1$ 个足够强但有限的正权，可得到出生增加 $m-1$ 的实际首阶严格违反。没有把无限大权当成允许模型。

这是非严格普适性质的等价。每个有限首阶严格正，只能经极限立即推出更高阶非负，不能由本定理免费推出所有高阶严格正。

## 2. 保留三个旧出生的共同源

沿用首阶传输稿的旧行与记号：
$$
U=K_{r+1},\quad V=K_r,\quad W=K_{r-1},
$$
$$
U_j=\Gamma_{j,r+1},\quad X_j=\Gamma_{j,r},\quad
Z_j=\Gamma_{j,r-1},\quad
A=C|_U,\quad B=C|_V.
$$
新增权为 $\sqrt t$，$\varepsilon=t^{-1}$。新上、下出生的共同源是
$$
\mathcal E_t(x,y)=(x-\mathcal J_{1,r}y,\sqrt\varepsilon y),
$$
$$
\mathcal F_t(u,v)=(u-\mathcal J_{1,r-1}v,\sqrt\varepsilon v).
$$
源 Gram 为 $U_0(t)=\operatorname{diag}(I,X_1+\varepsilon I)$、
$V_0(t)=\operatorname{diag}(I,Z_1+\varepsilon I)$。

记新上、下第 $j$ Gram 形式为 $H_j(t),L_j(t)$。完整一位公式给
$$
H_j=
\begin{pmatrix}P_j&-P_jq_j\\-q_j^*P_j&D_j+q_j^*P_jq_j\end{pmatrix},
\quad
P_j=\varepsilon U_{j-1}+O(\varepsilon^2),
\quad D_j=X_{j+1}+\varepsilon X_j,
\tag{2.1}
$$
以及相同形式的 $L_j$，其中将 $U,X,q$ 换成 $X,Z,\rho$。旧最高硬端的 $P_j=\varepsilon U_{j-1}$ 是准确等式，故仍服从显示展开。

剪切的准确差分是
$$
q_j-q_{j-1}
=\frac1j\bigl(U_{j-1}^{-1}A^*X_{j+1}
-U_{j-2}^{-1}A^*X_j\bigr),
$$
$$
\rho_j-\rho_{j-1}
=\frac1j\bigl(X_{j-1}^{-1}B^*Z_{j+1}
-X_{j-2}^{-1}B^*Z_j\bigr).
\tag{2.2}
$$
只在 $j=1$ 的差分中把下标 $-1$ 精度按零解释。三次桥仍是准确矩阵
$$
\mathcal B_t=\begin{pmatrix}A&tI-T\\0&B\end{pmatrix},
\quad T=CR-R_-B,
\tag{2.3}
$$
其中 $T$ 固定。

## 3. 一般 $n\ge2$ 的完整双分支极限

设新上出生的高度为 $h_{\rm new}\ge n\ge2$。它对应的旧上、主、下高度分别为 $h_{\rm new}-1,h_{\rm new}+1,h_{\rm new}+3$。因此以下旧缺陷均在合法高度，包括最高硬端。

令新加强缺陷的源形式为
$$
\mathbf E_n^{(\kappa)}(t)
=\mathcal E_t^* E_{n,\rm new}^{(\kappa)}\mathcal E_t.
$$
其准确式为
$$
\begin{aligned}
\mathbf E_n^{(\kappa)}={}&
\kappa U_0H_n^{-1}H_{n-1}H_n^{-1}U_0
-U_0H_{n+1}^{-1}U_0\\
&-\frac1{(n+1)^2}V_nL_{n+2}^{-1}V_n^*,
\end{aligned}
\tag{3.1}
$$
$$
V_n=U_0H_n^{-1}\mathcal B_t^*L_{n+2}
-U_0H_{n-1}^{-1}\mathcal B_t^*L_{n+1}.
\tag{3.2}
$$
若 $n=h_{\rm new}$，从 (3.1) 删除不存在的第二精度项，而不是解释一个虚构的 $H_{n+1}$。

**极限定理。** 在有限维算子范数中，
$$
\boxed{
\begin{pmatrix}t^{-1/2}I_U&0\\0&I_V\end{pmatrix}
\mathbf E_n^{(\kappa)}(t)
\begin{pmatrix}t^{-1/2}I_U&0\\0&I_V\end{pmatrix}
\longrightarrow
\begin{pmatrix}
E_{n-1,U}^{(\kappa)}&0\\
0&X_1E_{n+1,V}^{(\kappa)}X_1
\end{pmatrix}.
}
\tag{3.3}
$$
$E_{n-1,U}^{(\kappa)}$ 使用旧上出生 $U_j$、桥 $A$ 及其下出生 $X_j$；
$E_{n+1,V}^{(\kappa)}$ 使用旧主出生 $X_j$、桥 $B$ 及其下出生 $Z_j$。这两个度量从未混同。

### 3.1 相邻 Gram 乘积的主项

写 $\eta_n=q_n-q_{n-1}$。相对 $H_n$ 的三角分解，$H_{n-1}$ 的中间块准确为
$$
\begin{pmatrix}
P_{n-1}&P_{n-1}\eta_n\\
\eta_n^*P_{n-1}&D_{n-1}+\eta_n^*P_{n-1}\eta_n
\end{pmatrix}.
$$
由于 $n\ge2$，这里 $P_{n-1}=O(t^{-1})$，与首阶的 $H_0=U_0$ 情形不同。故
$U_0H_n^{-1}H_{n-1}H_n^{-1}U_0$ 的上块为
$$
t\,U_{n-1}^{-1}U_{n-2}U_{n-1}^{-1}+O(1),
$$
交叉为 $O(1)$，下块为
$$
X_1X_{n+1}^{-1}X_nX_{n+1}^{-1}X_1+O(t^{-1}).
\tag{3.4}
$$
第二精度形式的上块为 $tU_n^{-1}+O(1)$、交叉有界，下块趋于 $X_1X_{n+2}^{-1}X_1$。硬端时两个旧下一精度都为零，准确对应删除该项。

### 3.2 创新的两个主项

由 (2.1)–(2.3)，$V_n/(n+1)$ 的上左块趋于
$$
\frac{U_{n-1}^{-1}A^*X_{n+1}+q_n
-U_{n-2}^{-1}A^*X_n-q_{n-1}}{n+1}
=q_n-q_{n-1}=\eta_n.
\tag{3.5}
$$
它的下左块为 $O(t^{-1})$。下右块则趋于
$$
\frac{X_1}{n+1}
\bigl[-\rho_{n+2}+X_{n+1}^{-1}B^*Z_{n+3}
+\rho_{n+1}-X_n^{-1}B^*Z_{n+2}\bigr]
$$
$$
\hspace{20mm}=X_1(\rho_{n+2}-\rho_{n+1}).
\tag{3.6}
$$
最后的等式使用 (2.2) 中准确的 $1/(n+2)$；括号是 $(n+1)$ 倍的同一剪切差，故系数恰好抵消。

$L_{n+2}^{-1}$ 的上块为 $tX_{n+1}^{-1}+O(1)$、交叉有界、下块趋于 $Z_{n+3}^{-1}$。所以创新费用的上块主项为
$$
t\eta_nX_{n+1}^{-1}\eta_n^*,
$$
下块趋于
$$
X_1(\rho_{n+2}-\rho_{n+1})Z_{n+3}^{-1}
(\rho_{n+2}-\rho_{n+1})^*X_1,
\tag{3.7}
$$
交叉为 $O(1)$。结合 (3.4)–(3.7)，在上分支作 $t^{-1/2}$ 同余即得 (3.3)。固定旧模型时，显示的收敛误差为 $O(t^{-1/2})$；没有对一个趋于奇异的完整 Gram 免费取逆。

## 4. 首阶的特殊缩放及常数保持

首阶不能把 (3.3) 直接代入 $n=1$，因为 $H_0$ 的上块是 $I$，不是 $O(t^{-1})$。首阶传输稿已核过 $\kappa=1$ 的完整式；同一展开保留 $\kappa$ 后得到
$$
\boxed{
\begin{pmatrix}t^{-1}I_U&0\\0&I_V\end{pmatrix}
\mathbf E_1^{(\kappa)}(t)
\begin{pmatrix}t^{-1}I_U&0\\0&I_V\end{pmatrix}
\longrightarrow
\begin{pmatrix}
\kappa I_U&\kappa A^*X_1\\
\kappa X_1A&X_1(\kappa AA^*+E_{2,V}^{(\kappa)})X_1
\end{pmatrix}.
}
\tag{4.1}
$$
因为 $\kappa>0$，对上面的 $\kappa I$ 取真实 Schur 补，恰余
$X_1E_{2,V}^{(\kappa)}X_1$。$\kappa AA^*$ 仍完全消去，常数没有损失。

## 5. 普适性质的等价与有限反例回传

假设所有实际首阶都满足 $E_1^{(\kappa)}\succeq0$。固定任意旧模型及出生：先用 (4.1) 得 $E_2^{(\kappa)}\succeq0$。若已知所有模型的第 $m-1\ge2$ 阶非负，给任意旧目标出生加一个强位，使新出生增加一。新高度减少一，仍足以使用第 $m-1$ 阶。由 (3.3) 的下分支得旧第 $m$ 阶非负。归纳得到全部合法阶；反向蕴含只需取 $n=1$。

若旧 $E_m^{(\kappa)}$ 有严格负向量 $v$，当 $m\ge3$ 时在 (3.3) 取源 $(0,X_1^{-1}v)$，极限二次型严格负。$m=2$ 时在 (4.1) 取
$$
(x,y)=(-A^*v,X_1^{-1}v),
$$
极限二次型仍准确等于 $\langle E_2^{(\kappa)}v,v\rangle$。有限维范数收敛使同一见证对所有充分大的有限新增权保持负号。逐次重复，得到首阶的实际有限正权严格违反。

## 6. 准确用途与仍未支付的部分

任意普适 $\kappa$ 的加强式都蕴含相同常数的普通相邻序，因为其桥费用为正。于是若能对全出生证明一个有限的首阶加强常数，本稿把它传给全部高度，而不必另外假设一般 S2 已解决。这里的前提依然是所有正权和所有出生，未由已有低出生或低占据结果满足。

相同常数的普通相邻序并不单独蕴含加强式；本稿没有倒置这条蕴含，也没有把 R281 的普通常数等价重计成加强常数已经存在。已知普通普适常数至少为一，故任何本稿的普适加强常数亦至少为一。一般 $\kappa=1$、一般有限 $\kappa$、原 graph 返回源及普通 Hilbert ISP 都仍未由本稿关闭。
