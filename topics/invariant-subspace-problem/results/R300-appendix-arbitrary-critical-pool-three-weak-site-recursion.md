# 任意临界偶数权池同时加入三弱位：全部旧出生交叉的真实首加强递归

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：下列完整有限维算子范数极限与有限正参数的严格传输已证明。** 旧 $2s$ 个正权、弱组三个内部正权均任意固定，$s\ge1$。本文推广七位联合边界，保留旧高度四源及其更低出生的真实交叉；不是把旧真空标量原样外推。结论是同常数的联合边界递归，不是一般奇数硬端内部的统一有限界。

## 1. 同一模型、三族完整上源与主结论

旧物理第 $j$ 层记为 $O_j$，其占据集合基正交归一。旧位数为 $2s$，定义

$$
d=\sum_{i=1}^{2s}b_iE_i,\qquad
A=\sum_{i=1}^{2s}b_i^{-1}E_i,\qquad e=A^*,
\qquad b_i>0.
$$

弱组三位的第 $j$ 层记为 $\mathcal W_j$，其行和对偶删除为

$$
d_w=\sum_{i=1}^3c_iE_i,\qquad
A_w=\sum_{i=1}^3c_i^{-1}E_i,\qquad c_i>0.
$$

实际新行是 $d_\epsilon=d+\epsilon d_w$，$\epsilon>0$，共有 $2s+3$ 位。其上源 $K_{s+1}(d_\epsilon)$ 高度一，低源 $K_s(d_\epsilon)$ 高度三。定义真实硬端费用

$$
\mathcal K_\epsilon
=(A+\epsilon^{-1}A_w)^*
 L_{1,\epsilon}L_{3,\epsilon}^{-1}L_{1,\epsilon}
 (A+\epsilon^{-1}A_w)\big|_{K_{s+1}(d_\epsilon)},
\tag{1.1}
$$

其中 $L_{j,\epsilon}=\Gamma_{j,s}(d_\epsilon)$，$\Gamma_{j,t}$ 始终是完整 $d^j/j!$ 的 Moore–Penrose 右逆限制到 $K_t$ 后的 Gram。由 [R297 硬端消逆](R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md)，(1.1) 的上界 $\kappa I$ 正是这个硬端的首加强 S1。

记

$$
U=K_s(d),\quad V=K_{s-1}(d),\quad W=K_{s-2}(d),
$$
$$
K=K_1(d_w),\quad K^a=K_1(A_w),\quad
S_w=\sum c_i^2,\quad p=\prod_{i=1}^{2s}b_i,\quad p_w=c_1c_2c_3.
$$

负出生空间约定为零；特别 $s=1$ 时 $W=0$。以下凡在负物理层上的项均省略，不构造不存在的逆。

上源的固定比较空间为物理正交直和

$$
\mathscr U=(U\otimes K)\oplus(V\otimes\mathcal W_2)
 \oplus(W\otimes\mathcal W_3).
\tag{1.2}
$$

弱补集酉映射记为 $\mathfrak c_w$，并定义

$$
R_w=P_{K^a}\mathfrak c_w:\mathcal W_2\to K^a.
\tag{1.3}
$$

它是余等距，$R_w^*R_w$ 为秩二正交投影。

对旧合法出生 $t$，当其高度至少二时，记

$$
G_j=\Gamma_{j,t}(d),\quad C_j=G_j^{-1},\quad
B_t=\left.\sum_i b_i^3E_i\right|_{K_t}:K_t\to K_{t-1},
\quad L_j=\Gamma_{j,t-1}(d),
$$
$$
\delta_t=\frac12(C_1B_t^*L_3-B_t^*L_2),
$$
$$
\boxed{\mathcal K_t^{(o)}
 =G_1(C_2+\delta_tL_3^{-1}\delta_t^*)G_1.}
\tag{1.4}
$$

若 $t=0$，下出生为空，全部桥项为零。$\mathcal K_t^{(o)}$ 是旧整个 $K_t$ 上的真实首加强标准化费用，不是普通相邻比。

**定理 1。** 第 2 节的实际源嵌入归一成等距映射
$\mathcal U_\epsilon:\mathscr U\to K_{s+1}(d_\epsilon)$ 后，

$$
\boxed{
\mathcal U_\epsilon^*\mathcal K_\epsilon\mathcal U_\epsilon
 \xrightarrow[\epsilon\downarrow0]{\|\cdot\|}
 \operatorname{diag}\!\left(
 I_U\otimes\mathcal K_w,\ 
 \mathcal K_{s-1}^{(o)}\otimes R_w^*R_w,\ 
 \mathcal K_{s-2}^{(o)}
 \right).
}
\tag{1.5}
$$

这里 $\mathcal K_w$ 是弱三位整个 $K_1(d_w)$ 的真实硬端费用。三个源族完整保留；中间块的 $\dim V$ 个弱方向零极限不能提前删除。一般 $s$ 的上、下源维数并不相等。

因此，如果两个旧首加强费用以及 $\mathcal K_w$ 的范数都严格小于同一个 $\kappa$，则所有充分小正 $\epsilon$ 的整个新增硬端都满足 $\mathcal K_\epsilon\prec\kappa I$。只有非严格旧界时，(1.5) 给同常数的极限上界；不能据此声称每个有限 $\epsilon$ 仍有同一非严格常数。

## 2. 完整上源、倒数低源及两个有限参数度量

旧代数关系为

$$
[d,e]|_{O_j}=(2s-2j)I.
$$

对旧 primitive $u$、高度 $h$ 和满足 $d_w^{h+1}v=0$ 的弱向量，定义

$$
E_{\epsilon,h}(u\otimes v)=
 \sum_{j=0}^h\frac{(-\epsilon)^j}{j!(h)_{\underline j}}
 e^ju\otimes d_w^jv.
\tag{2.1}
$$

相邻两项由 $de^ju=j(h-j+1)e^{j-1}u$ 精确抵消。对 (1.2) 三块使用 $h=0,2,4$，得到实际上源嵌入 $E_\epsilon$。其零参数值为物理正交嵌入，所以

$$
H_\epsilon=E_\epsilon^*E_\epsilon\to I,\qquad
\mathcal U_\epsilon=E_\epsilon H_\epsilon^{-1/2}.
\tag{2.2}
$$

按旧 primitive 维数公式计数，(1.2) 的维数正是
$\binom{2s+3}{s+1}-\binom{2s+3}{s}$，所以小正参数时覆盖整个上源。

处理真正顶逆需要倒数低源，而其固定源不再是整个旧物理层。准确空间为

$$
X=\ker(A^4|_{O_s}),\qquad
Y=\ker(A^2|_{O_{s-1}}),\qquad
\mathscr X=(X\otimes\mathcal W_0)\oplus(Y\otimes K^a).
\tag{2.3}
$$

以弱行 $A_w$ 为基、$\epsilon A$ 为扰动，使用 (2.1) 的同一个构造：$X$ 块从弱真空高度三开始，保留 $j=0,1,2,3$；$Y$ 块从弱 primitive 高度一开始，保留 $j=0,1$。条件 $A^4X=0$、$A^2Y=0$ 正好支付链末端，得到

$$
G_\epsilon:\mathscr X\longrightarrow K_s(A+\epsilon^{-1}A_w),
\qquad J_\epsilon^{\rm src}=G_\epsilon^*G_\epsilon\to I.
\tag{2.4}
$$

若 $p_t=\dim K_t(d)$，旧对偶代数分解给
$\dim X=p_s+p_{s-1}+p_{s-2}+p_{s-3}$、
$\dim Y=p_{s-1}+p_{s-2}$。于是
$\dim\mathscr X=p_s+3p_{s-1}+3p_{s-2}+p_{s-3}$，
正是整个新增低源的维数。

旧平方权对角算子记为

$$
\Xi_j e_I=\Bigl(\prod_{i\in I}b_i^2\Bigr)e_I\quad(I\subset\{1,\ldots,2s\},\ |I|=j),
$$

弱平方权对角算子记为 $Z_j$。在新第 $s$ 层上，$D_\epsilon$ 是实际平方权乘子，且 $p_\epsilon=pp_w\epsilon^3$。真正顶提升为

$$
\mathcal J_{3,s}(d_\epsilon)
 =\frac{(-1)^s}{p_\epsilon}\mathfrak c\,D_\epsilon|_{K_s(d_\epsilon)}.
\tag{2.5}
$$

这由加权 Boolean $\mathfrak{sl}_2$ 的高度三顶端得到；也可直接用占据基核查。定义

$$
W_\epsilon=p_\epsilon D_\epsilon^{-1}G_\epsilon.
\tag{2.6}
$$

它是 $\mathscr X\to K_s(d_\epsilon)$ 的双射，且

$$
W_\epsilon^*L_{3,\epsilon}W_\epsilon=J_\epsilon^{\rm src},
\quad
L_{3,\epsilon}^{-1}
 =W_\epsilon(J_\epsilon^{\rm src})^{-1}W_\epsilon^*.
$$

完整第一 Gram 是 $F_\epsilon=d_\epsilon d_\epsilon^*|_{\mathcal H_s}>0$。置

$$
T_\epsilon=W_\epsilon^*F_\epsilon^{-1}
 (A+\epsilon^{-1}A_w)E_\epsilon.
$$

因为两个配对输入都在真实低源，

$$
\boxed{
\mathcal U_\epsilon^*\mathcal K_\epsilon\mathcal U_\epsilon
 =H_\epsilon^{-1/2}T_\epsilon^*
 (J_\epsilon^{\rm src})^{-1}T_\epsilon H_\epsilon^{-1/2}.
}
\tag{2.7}
$$

有限参数中两个源 Gram 均保留。以下须先证明 $T_\epsilon$ 有界收敛，才能在末步使用它们趋于恒等。

## 3. 完整第一逆：四个弱占据块和唯一小 Schur

记

$$
R_j=d:O_{s-j+1}\to O_{s-j},\quad
F_j=R_jR_j^*,\quad N_j=F_j^{-1}\qquad(j\ge1,\ s-j\ge0),
$$

并记 $F_0=dd^*|_{O_s}$。每个现存 $F_j$、$j\ge1$ 都严格正定；$F_0$ 的核为
$C=\ker d^*|_{O_s}$，通常不同于 $U=\ker d|_{O_s}$。

弱算子记为

$$
c=d_w^*1,\quad\alpha=A_w^*1,\quad
B=d_w:\mathcal W_2\to\mathcal W_1,\quad
k=d_w1_{\mathcal W_3}=\mathfrak c_wc.
$$

按弱次数 $0,1,2,3$，完整 $F_\epsilon$ 是

$$
\begin{pmatrix}
F_0+\epsilon^2S_wI&\epsilon R_1^*\otimes c^*&0&0\\
\epsilon R_1\otimes c&F_1\otimes I+\epsilon^2I\otimes BB^*
 &\epsilon R_2^*\otimes B&0\\
0&\epsilon R_2\otimes B^*&F_2\otimes I+\epsilon^2I\otimes kk^*
 &\epsilon R_3^*\otimes k\\
0&0&\epsilon R_3\otimes k^*&F_3
\end{pmatrix}.
\tag{3.1}
$$

不存在的物理块整行整列省略。逆序消元得到

$$
K_3=F_3,\quad
K_2=F_2\otimes I+\epsilon^2P_W\otimes kk^*,
$$
$$
K_1=F_1\otimes I+\epsilon^2I\otimes BB^*
 -\epsilon^2(R_2^*\otimes B)K_2^{-1}(R_2\otimes B^*),
$$
$$
S_\epsilon=F_0+\epsilon^2S_wI
 -\epsilon^2(R_1^*\otimes c^*)K_1^{-1}(R_1\otimes c).
\tag{3.2}
$$

特别地 $K_j^{-1}=N_j\otimes I+O(\epsilon^2)$，且
$R_1^*N_1R_1=I-P_U$，所以

$$
S_\epsilon=F_0+\epsilon^2S_wP_U+O(\epsilon^4).
\tag{3.3}
$$

旧临界代数分解 $O_s=U\oplus\operatorname{Ran}(d:O_{s+1}\to O_s)$ 是线性直和，故 $P_C|_U$ 可逆。定义

$$
\mathcal H=P_C(P_CP_UP_C|_C)^{-1}P_C,\qquad
\mathcal J=\mathcal H|_U.
$$

则 $P_U\mathcal Ju=u$，并由真正 $C\oplus C^\perp$ 消元得到

$$
S_\epsilon^{-1}=(\epsilon^2S_w)^{-1}\mathcal H+O(1).
\tag{3.4}
$$

对任意四块物理列 $f$，定义

$$
\widehat f_2=f_2-\epsilon(R_3^*\otimes k)N_3f_3,
$$
$$
\widehat f_1=f_1-\epsilon(R_2^*\otimes B)K_2^{-1}\widehat f_2,
\qquad
\widetilde f_0=f_0-\epsilon(R_1^*\otimes c^*)K_1^{-1}\widehat f_1.
\tag{3.5}
$$

同一个完整逆配对为

$$
\langle w,F_\epsilon^{-1}f\rangle
 =\langle\widetilde w_0,S_\epsilon^{-1}\widetilde f_0\rangle
 +\langle\widehat w_1,K_1^{-1}\widehat f_1\rangle
 +\langle\widehat w_2,K_2^{-1}\widehat f_2\rangle
 +\langle w_3,N_3f_3\rangle.
\tag{3.6}
$$

所有余项是固定旧权、弱内部权下的有限维算子范数余项。

## 4. 全部顶测试、源列和可能非零的极限块

弱三位直接满足

$$
Bk=2p_w\alpha,\quad
B\mathfrak c_w|_{K^a}=-p_wZ_1^{-1}|_{K^a},\quad
Z_2^{-1}B^*|_{K^a}=-p_w^{-1}\mathfrak c_w|_{K^a},
$$
$$
P_{K^a}Z_1^{-1}(A_w|_{\mathcal W_2})=-p_w^{-1}R_w,\qquad
c^*\alpha=3.
\tag{4.1}
$$

从 (2.4)–(2.6) 的有限和直接得到：对 $x_0\in X$，

$$
(W_X)_0=\epsilon^3pp_w\Xi_s^{-1}x_0,
$$
$$
(W_X)_1=-\frac{\epsilon^2pp_w}{3}\Xi_{s-1}^{-1}Ax_0\otimes\alpha,
\quad
(W_X)_2=\frac{\epsilon p}{6}\Xi_{s-2}^{-1}A^2x_0\otimes k,
$$
$$
\boxed{(W_X)_3=-\frac p6\Xi_{s-3}^{-1}A^3x_0\otimes1_{\mathcal W_3}.}
\tag{4.2}
$$

最后一个常数项在旧四位真空特例中消失，在一般旧池中必须保留。对 $y_0\in Y\otimes K^a$，

$$
(W_Y)_0=(W_Y)_3=0,\quad
(W_Y)_1=\epsilon pp_w(\Xi_{s-1}^{-1}\otimes Z_1^{-1})y_0,
$$
$$
(W_Y)_2=p(\Xi_{s-2}^{-1}A\otimes\mathfrak c_w)y_0.
\tag{4.3}
$$

为写变换后的领先项，定义

$$
H_2=\Xi_{s-2}^{-1}+R_3^*N_3\Xi_{s-3}^{-1}A,\qquad
H_1=\Xi_{s-1}^{-1}+R_2^*N_2H_2A,
$$
$$
Q=\Xi_s^{-1}+R_1^*N_1H_1A,\qquad
H_Y=\Xi_{s-1}^{-1}+R_2^*N_2\Xi_{s-2}^{-1}A.
\tag{4.4}
$$

(3.5)、(4.1) 给

$$
\widehat{(W_X)}_2=\frac{\epsilon p}{6}H_2A^2x_0\otimes k,
$$
$$
\widehat{(W_X)}_1
 =-\frac{\epsilon^2pp_w}{3}H_1Ax_0\otimes\alpha+O(\epsilon^4),
\quad
\widetilde{(W_X)}_0=\epsilon^3pp_wQx_0+O(\epsilon^5),
\tag{4.5}
$$

以及

$$
\widehat{(W_Y)}_1
 =\epsilon pp_w(H_Y\otimes Z_1^{-1})y_0+O(\epsilon^3),
\qquad
\boxed{\widetilde{(W_Y)}_0=O(\epsilon^4).}
\tag{4.6}
$$

后一式的可能 $\epsilon^2$ 项含
$c^*Z_1^{-1}|_{K^a}=\alpha^*|_{K^a}=0$，所以准确消失。

另一方面，令 $f=(A+\epsilon^{-1}A_w)E_\epsilon$，对 (1.2) 的三族 $x,y,z$，其四块量级为

$$
\begin{array}{c|cccc}
 &f_0&f_1&f_2&f_3\\ \hline
x\in U\otimes K
 &\epsilon^{-1}(I\otimes\alpha^*)x&(A\otimes I)x&0&0\\
y\in V\otimes\mathcal W_2
 &O(1)&\epsilon^{-1}(I\otimes A_w)y+O(\epsilon)&(A\otimes I)y&0\\
z\in W\otimes\mathcal W_3
 &O(\epsilon)&O(1)&\epsilon^{-1}z\otimes\mathfrak c_w\alpha+O(\epsilon)&Az
\end{array}.
\tag{4.7}
$$

用同一 (3.6)，只有 $X\leftarrow x$、$Y\leftarrow y$、$X\leftarrow z$ 可留下常数项：

$$
T_{Xx}=\frac{pp_w}{S_w}P_XQ^*\mathcal J\otimes\alpha^*,
\tag{4.8}
$$
$$
T_{Yy}=-T_V\otimes R_w,\qquad
T_V=pP_Y\left(H_Y^*N_1-A^*\Xi_{s-2}^{-1}N_2A\right)|_V,
\tag{4.9}
$$
$$
T_{Xz}
 =\frac p2P_X(A^*)^2H_2^*N_2|_W
  -\frac p6P_X(A^*)^3\Xi_{s-3}^{-1}N_3A|_W.
\tag{4.10}
$$

这里所有投影 $P_X,P_Y$ 都是实际物理正交投影。

其余块为 $O(\epsilon)$：$X\leftarrow y$ 和 $Y\leftarrow x$ 由量级直接得到；$Y\leftarrow z$ 表面上的 $\epsilon^{-1}$ 项含
$P_{K^a}\mathfrak c_w(\mathfrak c_w\alpha)=P_{K^a}\alpha=0$。四块 Schur 其余项也由 (3.4)、(4.5)、(4.6)、(4.7) 一并趋零。

## 5. 加权不交恒等式与任意旧临界块的完整抵消

下面的有限恒等式统一支付三个非零块。若 $\ell+t+h=2s$，则从 $O_t$ 到 $O_\ell$，

$$
\boxed{
\frac1p\mathfrak c_{t+h}(d^*)^h
 =h!\sum_{i=0}^{\min(\ell,t)}
 \frac{(-1)^i}{(\ell-i)!(t-i)!}
 (A^*)^{\ell-i}\Xi_i^{-1}A^{t-i}.
}
\tag{5.1}
$$

**证明。** 对占据集合 $I,J$，$|I|=\ell$、$|J|=t$，右侧每个 $i$ 项的坐标是
$h!(-1)^i\binom{|I\cap J|}{i}/(b_Ib_J)$。相加得到零，除非 $I,J$ 不交，此时为 $h!/(b_Ib_J)$。左侧在不交时恰从补集剩余 $h$ 位得到同一系数，其他情形为零。证毕。

特别地，在旧中间层且 $v\in C=\ker d^*=\ker A$ 时，取 $h=0$ 得

$$
\Xi_s^{-1}v=\frac{(-1)^s}{p}\mathfrak c_sv.
\tag{5.2}
$$

为处理 (4.8)，令 $v=\mathcal Ju$，于是 $P_Uv=u$。定义旧完整 Green 序列

$$
q_0=v,\qquad q_j=N_jd q_{j-1}\quad(1\le j\le s).
$$

则 $v=u+d^*q_1$。由 $Aq_0=0$ 及真正混合关系
$[A,d^*]|_{O_{s-j}}=2jI$，逐层得到

$$
\boxed{Aq_j=-j(j+1)q_{j+1}.}
\tag{5.3}
$$

具体地，对 $F_jq_j=dq_{j-1}$ 作用 $A$，
$F_{j+1}Aq_j+2j\,dq_j=dAq_{j-1}$；归纳即得 (5.3)。因此

$$
q_j=\frac{(-1)^{j-1}}{(j-1)!j!}A^{j-1}q_1\qquad(j\ge1).
$$

由 (4.4)，$Q^*v$ 正是
$\sum_{j=0}^{\min(3,s)}(A^*)^j\Xi_{s-j}^{-1}q_j$。
补足至 $s$ 后，新增项全在 $\operatorname{Ran}(A^*)^4$，故被 $P_X$ 杀掉。用 (5.1) 的 $(\ell,t,h)=(s,s-1,1)$ 和 (5.2)，

$$
\begin{aligned}
\sum_{j=0}^{s}(A^*)^j\Xi_{s-j}^{-1}q_j
 &=\Xi_s^{-1}v+\frac{(-1)^{s-1}}p\mathfrak c_sd^*q_1\\
 &=\frac{(-1)^s}p\mathfrak c_s(v-d^*q_1)
 =\frac{(-1)^s}p\mathfrak c_su.
\end{aligned}
$$

而 $\mathfrak c_su\in\ker A\subset X$。所以

$$
\boxed{P_XQ^*\mathcal Ju=\frac{(-1)^s}p\mathfrak c_su,}
\tag{5.4}
$$
$$
\boxed{
T_{Xx}=\frac{(-1)^sp_w}{S_w}
 (\mathfrak c_s\otimes\alpha^*)|_{U\otimes K}.
}
\tag{5.5}
$$

这保留全部旧 Green 次序，并准确消去其条件数；没有把各大项分别估范数。

## 6. 真实首加强联合列及完整四阶核旗

对 (1.4) 的旧出生 $t$，定义同一物理层 $O_{t+2}$ 中的联合列

$$
\boxed{
M_t=\mathcal J_{2,t}C_2G_1
 -\mathcal J_{3,t-1}L_3^{-1}\delta_t^*G_1.
}
\tag{6.1}
$$

两个真实 MP 塔严格正交，所以

$$
M_t^*M_t=\mathcal K_t^{(o)}.
\tag{6.2}
$$

还需要其全层 Green 表达。令 $f\in K_t$，

$$
g=(dd^*|_{O_t})^{-1}f,\qquad
q=(dd^*|_{O_{t-1}})^{-1}dg.
$$

则

$$
\boxed{
M_tf=P_{\ker d^4|_{O_{t+2}}}
 \left[\frac12(d^*)^2g+\frac16(d^*)^3q\right].
}
\tag{6.3}
$$

**证明。** $P_{K_t}g=G_1f$，且 $g-G_1f=d^*q$。真实两带恒等式

$$
d^*|_{K_t}=\mathcal J_{1,t}C_1-\mathcal J_{2,t-1}B_t
$$

给 $(d^*)^2q=\mathcal J_{2,t-1}B_tG_1f$。再使用

$$
d^*\mathcal J_{1,t}=2\mathcal J_{2,t}C_2G_1-\mathcal J_{3,t-1}B_t,
$$
$$
d^*\mathcal J_{2,t-1}
 =3\mathcal J_{3,t-1}L_3^{-1}L_2-\mathcal J_{4,t-2}B_{t-1}.
$$

最后的真实第四塔正交于 $\ker d^4$，投影后恰得到 (6.1)。这里没有把完整 $d^*$ 当成第一带 $d_1^*$；更低出生项是由实际核旗投影支付的。

上述两带式可直接从 $[d,[d,d^*]]=-2\sum b_i^3E_i$、该三次删除与 $d$ 交换，以及完整 MP 核旗逐塔系数推出；对应完整证明见 [R275 三次桥](R275-appendix-exact-cubic-bridge-for-shear-innovations.md) 和 [R288 三塔身份](R288-appendix-general-birth-three-tower-s1-schur-cancellation.md)。它们不预设任何 S1 正序。证毕。

两项 (6.1) 都在 $\ker d^4$ 且正交于 $\ker d^2$。特别地，对 $t=s-2$，其像与旧 $U\subset O_s$ 正交。

最后，用对偶代数 $(A,d^*)$ 的完整链可逐链检查

$$
\mathfrak c_s(\ker d^4|_{O_s})=X,\qquad
\mathfrak c_{s+1}(\ker d^4|_{O_{s+1}})=Y.
\tag{6.4}
$$

例如在旧中间层，一个高度 $2j$ 的链被 $A^4$ 或 $(d^*)^4$ 杀掉的条件均为 $j<4$；在 $O_{s-1}$ 上，$A^2$ 与 $(d^*)^4$ 的零条件均为 $j<3$。因此 (6.4) 是真实子空间等式；补集酉性相应运输正交投影。

## 7. 旧高度二、四的所有 Green 项恰是两个真实首加强列

### 7.1 中间 $V$ 列

对 $f\in V$，置 $g=N_1f$、$q=N_2dg$、$h=N_2Af$。完整混合关系在旧 $O_{s-1}$ 上给

$$
AF_1g=F_2Ag+2dg,\qquad h=Ag+2q.
$$

(4.9) 因此化为

$$
T_Vf=pP_Y\left[
 \Xi_{s-1}^{-1}g-A^*\Xi_{s-2}^{-1}Ag-A^*\Xi_{s-2}^{-1}q
 \right].
\tag{7.1}
$$

在 (5.1) 分别取 $(\ell,t,h)=(s-1,s-1,2)$ 和
$(s-1,s-2,3)$。$P_Y$ 杀掉所有含左因子 $(A^*)^2$ 的项，故

$$
T_Vf=(-1)^{s-1}P_Y\mathfrak c_{s+1}
 \left[\frac12(d^*)^2g+\frac16(d^*)^3q\right].
$$

由 (6.3)–(6.4)，

$$
\boxed{T_V=(-1)^{s-1}\mathfrak c_{s+1}M_{s-1}.}
\tag{7.2}
$$

这直接识别完整同源算子，并未只借维数或名称识别费用。

### 7.2 最高弱占据的旧 $W$ 列

对 $f\in W$，置 $g=N_2f$、$q=N_3dg$、$h=N_3Af$。此时混合关系中的系数是四：

$$
AF_2g=F_3Ag+4dg,\qquad h=Ag+4q.
$$

保留 (4.10) 中来自 $W_X$ 第三弱占据块的完整项，得到

$$
T_{Xz}f=\frac p2P_X\left[
 (A^*)^2\Xi_{s-2}^{-1}g
 -\frac13(A^*)^3\Xi_{s-3}^{-1}Ag
 -\frac13(A^*)^3\Xi_{s-3}^{-1}q
 \right].
\tag{7.3}
$$

在 (5.1) 分别取 $(s,s-2,2)$ 和 $(s,s-3,3)$。$P_X$ 杀掉左因子至少四阶的所有项，因而

$$
T_{Xz}f=(-1)^sP_X\mathfrak c_s
 \left[\frac12(d^*)^2g+\frac16(d^*)^3q\right].
$$

再用 (6.3)–(6.4)，得到

$$
\boxed{T_{Xz}=(-1)^s\mathfrak c_sM_{s-2}.}
\tag{7.4}
$$

若删掉 (4.2) 的常数项，(7.3) 中 $h/3$ 就会丢失，无法得到这个共同抵消。旧高度四和高度六的交叉确实参与证明；它们最后准确合并成旧 $K_{s-2}$ 上的真实首加强列。

## 8. 全部交叉、范数收敛与同常数边界递归

合并 (5.5)、(7.2)、(7.4)，整个矩形 $T_\epsilon$ 在范数中收敛到

$$
\boxed{
T_0(x,y,z)=
\left(
 (-1)^s\frac{p_w}{S_w}(\mathfrak c_s\otimes\alpha^*)x
 +(-1)^s\mathfrak c_sM_{s-2}z,\ 
 (-1)^s(\mathfrak c_{s+1}M_{s-1}\otimes R_w)y
\right).
}
\tag{8.1}
$$

$X$ 与 $Y\otimes K^a$ 是 (2.3) 的物理正交源。第一输出块中的 $x,z$ 两项也准确正交，因为 $U\perp\operatorname{Ran}M_{s-2}$，而补集是酉。因此

$$
T_0^*T_0=
 \operatorname{diag}\!\left(
 \frac{p_w^2}{S_w^2}I_U\otimes P_K\alpha\alpha^*|_K,\ 
 M_{s-1}^*M_{s-1}\otimes R_w^*R_w,\ 
 M_{s-2}^*M_{s-2}
 \right).
$$

弱三位直接有

$$
\mathcal K_w=\frac{p_w^2}{S_w^2}P_K\alpha\alpha^*|_K,\qquad
\|\mathcal K_w\|
 =\frac{S_we_2(c^2)-9p_w^2}{S_w^3}<\frac14.
\tag{8.2}
$$

三变量 Schur 不等式
$S_w^3+9p_w^2\ge4S_we_2(c^2)$ 支付最后的严格界。

现在已证明 $T_\epsilon$ 有界并收敛，在 (2.7) 中使用
$H_\epsilon\to I$、$J_\epsilon^{\rm src}\to I$，即得 (1.5)。这也完整支付有限 $\epsilon$ 的非单位源 Gram。

具体地，令
$q_0=\max\{\|\mathcal K_w\|,\|\mathcal K_{s-1}^{(o)}\|,
\|\mathcal K_{s-2}^{(o)}\|\}$，省略空块。对每个 $\kappa>q_0$，存在依赖固定旧权、弱内部权和余量的 $\epsilon_0>0$，使全部 $0<\epsilon<\epsilon_0$ 满足 $\mathcal K_\epsilon\prec\kappa I$。若两个旧首加强费用均不超过同一 $q\ge1/4$，则联合边界极限不超过 $qI$，没有常数放大。

当旧池只有四位时，$W$ 是真空，
$\mathcal K_0^{(o)}=e_2(b^2)/(\sum b_i^2)^2\le3/8$。由 [R298 全五权硬端](R298-five-independent-positive-weights-birth-two-hard-top-strengthened-s1.md) 经 [R297 单弱位完整极限](R297-weak-bit-critical-pool-cancellation-and-first-edge-transfer.md)，任意旧四权的 $\mathcal K_1^{(o)}\preceq(743/782)I$。因而准确恢复已证七位联合边界及其充分小正参数严格区域。

一般旧池中，(1.5) 没有免费支付这两个旧首加强费用；也没有把任意固定权的 $\epsilon_0$ 当成跨不同权层次的一致阈值。一般奇数硬端内部的权无关有限常数，以及原 graph 的完整实际源费用，仍是未完成问题。
