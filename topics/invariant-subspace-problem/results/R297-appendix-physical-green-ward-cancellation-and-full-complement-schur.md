# 奇数硬端：保物理投影的 Green–Ward 消去与固定无权源 Schur 公式

日期：2026-11-14 UTC。作者：Astra-ISP-789f / literature_audit。

**状态：本文全部恒等式与同源等价已证明；尚未得到与位数、正权无关的有限范数界。** 下述 Ward 式消去了一个完整层 Green 逆，但保留真实的末端正交投影。最后的 Schur 式仍使用整个补空间的逆，不能先压缩到下一出生再求逆。

## 1. 空间、物理内积与完整逆

取 $M=2r+1$、$r\ge1$、$b_i>0$。$\mathcal H_j$ 是 $j$ 元子集的平方自由物理空间，子集基正交归一。记

$$
d=\sum_i b_iE_i,\qquad A=\sum_i b_i^{-1}E_i,
\qquad e=A^*.
$$

所有伴随和正交投影均针对这个内积。令

$$
U=\ker d\cap\mathcal H_r,\quad
V=\ker d\cap\mathcal H_{r-1},\quad
V_a=\ker A\cap\mathcal H_{r-1},
\quad A_U=A|_U:U\to V.
\tag{1.1}
$$

$[A,d]=0$ 保证 $A_U$ 的目标空间正确。置

$$
R=d|_{\mathcal H_r}:\mathcal H_r\to\mathcal H_{r-1},
\qquad F=RR^*>0,
$$
$$
P=P_U,\qquad Q=I-P=R^*F^{-1}R.
\tag{1.2}
$$

低出生的完整最小提升及其 Gram 是

$$
J_j=(d^j/j!)^\dagger|_V,\quad L_j=J_j^*J_j
\quad (j=1,2,3).
$$

特别地

$$
J_1=R^*F^{-1}|_V,
\qquad L_1=P_VF^{-1}|_V.
\tag{1.3}
$$

式 (1.3) 必须按“完整 $F^{-1}$ 后压缩”理解。

设 $\mathfrak c_j:\mathcal H_j\to\mathcal H_{M-j}$ 为补集酉映射；它满足 $\mathfrak c_j^*=\mathfrak c_{M-j}$。中央自伴算子作用在同一个 $\mathcal H_r$ 上：

$$
K=d|_{\mathcal H_{r+1}}\mathfrak c_r,
\qquad H=A|_{\mathcal H_{r+1}}\mathfrak c_r.
\tag{1.4}
$$

$K,H$ 都可逆。其矩阵在不交 $r$ 元子集 $I,J$ 处分别为 $b_\ell$、$b_\ell^{-1}$，其中 $\ell$ 是唯一剩余位；其他位置为零。

完整层可逆性可由无权升降直接看出。若 $d_0=\sum E_i$、$e_0=d_0^*$，则

$$
d_0e_0^k f=k(M-2s-k+1)e_0^{k-1}f
\quad(f\in\ker d_0\cap\mathcal H_s).
\tag{1.5}
$$

用 $\mathcal H_j=\ker d_0\oplus\operatorname{Ran}e_0$ 逐层归纳得到这些正交链。其中央一次删除和跨中央三次删除的每条链系数均非零。正权 $d$ 与 $d_0$ 通过逐层正对角算子相似，故 $R$ 满射、中央 $d$ 和跨中央 $d^3$ 可逆。

## 2. 保顶度量的实际目标算子

硬端创新的消逆结果为

$$
\mathcal K=A_U^*L_1L_3^{-1}L_1A_U
\quad\text{作用于 }U.
\tag{2.1}
$$

这里引用的准确创新识别见 [R297 硬端消逆](R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md)；以下只处理这个同一物理算子。

记 $p=\prod_i b_i$，并令 $Z=\operatorname{diag}(b_J^2)$ 作用在完整 $\mathcal H_{r-1}$ 上。顶提升有

$$
J_3=\frac{(-1)^{r-1}}p\mathfrak c_{r-1} Z|_V,
\qquad ZV=V_a.
\tag{2.2}
$$

为自足地核查第一式，令 $D_j=\operatorname{diag}(b_I)$ 于 $\mathcal H_j$。则 $d=D_{j-1}^{-1}d_0D_j$、$e=D_{j+1}^{-1}e_0D_j$。无权 primitive 多项式 $f$ 满足 $f(x+t\boldsymbol1)=f(x)$，从而 $f(\boldsymbol1-x)=(-1)^{r-1}f(x)$。在 $r+2$ 元子集处取值，得到 $e_0^3f/6=(-1)^{r-1}\mathfrak c_{r-1}f$。由 (1.5)，这正是 $d_0^3/6$ 的逆；再去权即得 (2.2)。第二式也直接来自 $A Z=Z_{r-2}d$，其中 $Z_{r-2}=\operatorname{diag}(b_I^2)$。

在完整 $\mathcal H_{r-1}$ 上定义自伴可逆矩阵

$$
M_3=RKR^*.
$$

补集与删除/上升交换给

$$
(d^3/6)\mathfrak c_{r-1}=M_3/6.
\tag{2.3}
$$

故 $S=(M_3/6)|_{V_a}:V_a\to V$ 是同构，且

$$
S^{-1}=\frac{(-1)^{r-1}}p Z|_V,
\quad J_3=\mathfrak c_{r-1}S^{-1},
\quad L_3^{-1}=SS^*.
\tag{2.4}
$$

这里 $S^*:V\to V_a$ 是两个实际子空间之间的伴随，不是完整 $M_3$ 在错误目标空间上的限制。

定义真正的顶物理输入算子

$$
\boxed{
T=\frac16 A_U^*L_1M_3|_{V_a}:V_a\longrightarrow U.
}
\tag{2.5}
$$

由 (2.4) 立即有

$$
\boxed{TT^*=\mathcal K.}
\tag{2.6}
$$

所以 $\mathcal K\preceq\kappa I_U$ 恰等价于 $\|T\|^2\le\kappa$，或 $T^*T\preceq\kappa I_{V_a}$。这种改写没有放弃 $L_3$：$V_a$ 的原内积正是经补集搬回的整个 $\operatorname{Ran}J_3$ 的物理内积。

## 3. 完整 Green 的源保持消去

首先有

$$
P eP_V=P e\quad\text{于完整 }\mathcal H_{r-1}.
\tag{3.1}
$$

事实上 $V^\perp=\operatorname{Ran}d^*|_{\mathcal H_{r-2}}$，而 $e$ 与 $d^*$ 交换，所以 $eV^\perp\subset\operatorname{Ran}R^*=U^\perp$。当 $r=1$ 时该补空间为零，结论相同。由 (1.3)，

$$
A_U^*L_1=P eF^{-1}|_V.
\tag{3.2}
$$

两个混合中央恒等式为

$$
KH=I+eR,\qquad HK=I+R^*A,
\qquad AK=RH,\qquad Ke=HR^*.
\tag{3.3}
$$

前两式来自 $[d,e]=[A,d^*]=M-2\deg$ 在 $\mathcal H_r$ 上等于 $I$；后两式由删除交换及取伴随给出。因而 $H|_U=K^{-1}|_U$，并且取伴随得

$$
P K^{-1}=PH.
\tag{3.4}
$$

将 (3.3)–(3.4) 代入完整 Green，有精确等式

$$
\begin{aligned}
P eF^{-1}R
&=P K^{-1}H R^*F^{-1}R\\
&=PH^2Q.
\end{aligned}
\tag{3.5}
$$

因此 (2.5) 化为

$$
\boxed{T=\frac16 PH^2QKR^*|_{V_a}.}
\tag{3.6}
$$

令 $G_1$ 表示上出生真实第一 Gram。中央 $d$ 可逆，且 $e|_U$ 是其逆在 $U$ 上的限制，因此

$$
G_1=PH^2|_U.
\tag{3.7}
$$

对 $v\in V_a$，混合关系在 $\mathcal H_{r-1}$ 上给 $AR^*v=3v$；由此

$$
HKR^*v=(I+R^*A)R^*v=4R^*v.
\tag{3.8}
$$

把 $Q=I-P$ 代入 (3.6)，再用 (3.7)–(3.8)，得到所需的同源 Ward 差：

$$
\boxed{
T=\frac16\bigl(4PHR^*-G_1PKR^*\bigr)|_{V_a}.
}
\tag{3.9}
$$

两项必须作为同一个差处理。式 (3.6) 中的 $P$ 也不可删去；[两个自然完整提升的已证发散例](R297-appendix-unprojected-lift-obstruction-with-bounded-physical-fee.md)已经说明完整提升与投影后最小费用不同。

## 4. 固定无权源坐标及两侧真实度量

以下固定两个正交归一的坐标嵌入：

$$
\mathsf U_0:\mathbb C^u\longrightarrow\ker d_0\cap\mathcal H_r,
\qquad
\mathsf V_0:\mathbb C^v\longrightarrow\ker d_0\cap\mathcal H_{r-1},
$$
$$
u=\binom Mr-\binom M{r-1},\qquad
v=\binom M{r-1}-\binom M{r-2},
\quad\binom M{-1}=0.
\tag{4.1}
$$

置

$$
\mathsf E_0=e_0\mathsf V_0/\sqrt3,
\qquad D=D_r,\quad D_-=D_{r-1},\quad\epsilon=(-1)^r.
\tag{4.2}
$$

$\mathsf E_0$ 是等距嵌入，其像正交于 $\operatorname{Ran}\mathsf U_0$，因为 $d_0e_0=3I$ 在 $\operatorname{Ran}\mathsf V_0$ 上成立。

用无权中央矩阵 $K_0=d_0\mathfrak c_r$，有

$$
K=pD^{-1}K_0D^{-1},\qquad H=p^{-1}DK_0D,
$$
$$
K_0\mathsf U_0=\epsilon\mathsf U_0,
\qquad K_0\mathsf E_0=-2\epsilon\mathsf E_0.
\tag{4.3}
$$

最后两式同样可从 primitive 多项式的补集取值直接证明。对上出生，每个不交 $r$ 元子集之和为 $\epsilon$ 倍原坐标。对低出生 $f$，$K_0e_0f$ 的每个坐标中，每个 $(r-1)$ 元子集被计数两次，故结果为 $2(-1)^{r-1}e_0f$。

实际源的坐标嵌入是

$$
X=D^{-1}\mathsf U_0:\mathbb C^u\to U,
\qquad Y=D_-\mathsf V_0:\mathbb C^v\to V_a.
\tag{4.4}
$$

定义

$$
A_\pm=\mathsf U_0^*D^{\pm2}\mathsf U_0\quad(u\times u),
$$
$$
B_\pm=\mathsf U_0^*D^{\pm2}\mathsf E_0\quad(u\times v),
\qquad
J_+=\mathsf V_0^*D_-^2\mathsf V_0\quad(v\times v).
\tag{4.5}
$$

于是 $X^*X=A_-$、$Y^*Y=J_+$，均严格正定。它们通常都不等于单位阵。上源第一 Gram 的物理配对矩阵为

$$
X^*G_1X=p^{-2}A_+.
\tag{4.6}
$$

令 $\mathcal T=X^*TY$ 为 $T$ 的双边配对矩阵；这不是直接把非正交坐标视为欧氏坐标所得的矩阵。由

$$
R^*Y=\sqrt3D\mathsf E_0,
$$
$$
X^*HR^*Y=\epsilon\sqrt3\,p^{-1}B_+,
\qquad
X^*KR^*Y=-2\epsilon\sqrt3\,pB_-,
\tag{4.7}
$$

并使用 (4.6) 处理 $G_1$ 的源度量，(3.9) 给出

$$
\boxed{
\mathcal T=\frac{\epsilon}{\sqrt3p}
\bigl(2B_++A_+A_-^{-1}B_-\bigr).
}
\tag{4.8}
$$

非交换次序 $A_+A_-^{-1}B_-$ 是由真实组合产生的。输出坐标为

$$
TY=XA_-^{-1}\mathcal T.
\tag{4.9}
$$

所以一般硬端费用的准确固定源目标是

$$
\boxed{
\mathcal T^*A_-^{-1}\mathcal T\preceq\kappa J_+.
}
\tag{4.10}
$$

若把 $A_-$ 或 $J_+$ 删除，便不再是 (2.1) 的物理范数问题。

## 5. 乘积权强制的整个补空间 Schur 抵消

本节将 (4.8) 的两项进一步合成一个完整 Schur 块。令

$$
W=D^2,\quad P_0=\mathsf U_0\mathsf U_0^*,\quad Q_0=I-P_0,
\quad \mathcal Q=\operatorname{Ran}Q_0,
$$
$$
B=\mathsf U_0^*W|_{\mathcal Q}:\mathcal Q\to\mathbb C^u,
\qquad C_Q=Q_0W|_{\mathcal Q}>0.
\tag{5.1}
$$

以下 $C_Q^{-1}$ 总是在维数 $\binom M{r-1}$ 的整个 $\mathcal Q$ 上求逆。定义

$$
\mathscr R=WK_0W,\qquad
\mathscr R_{01}=\mathsf U_0^*\mathscr R\mathsf E_0,
\qquad
C_{11}^{\rm inv}=\mathsf E_0^*C_Q^{-1}\mathsf E_0.
\tag{5.2}
$$

为说明为什么 $\mathscr R$ 的第一补空间行只落在 $\mathsf E_0$，置

$$
q_i=b_i^{-2},\quad S_q=\sum_iq_i,\quad
N_q=\sum_iq_i n_i,
$$

其中 $n_i=E_i^*E_i$ 是占据投影。令 $K_q$ 是中央不交矩阵：若 $I,J$ 不交且剩余位为 $\ell$，则其元素为 $q_\ell$。逐坐标给

$$
\mathscr R=p^2K_q,
\qquad
K_q=S_qK_0-N_qK_0-K_0N_q.
\tag{5.3}
$$

对 $f\in\operatorname{Ran}\mathsf U_0$，由 $[d_0,N_q]=d_q:=\sum_iq_iE_i$ 且 $[d_0,d_q]=0$，有 $d_0^2N_qf=0$。故

$$
N_q\operatorname{Ran}\mathsf U_0
\subset\operatorname{Ran}\mathsf U_0\oplus\operatorname{Ran}\mathsf E_0.
\tag{5.4}
$$

配合 (4.3)，这证明

$$
\mathsf U_0^*\mathscr R|_{\mathcal Q}
=\mathscr R_{01}\mathsf E_0^*,
\qquad
\mathscr R_{01}=\epsilon p^2\mathsf U_0^*N_q\mathsf E_0.
\tag{5.5}
$$

整个 $W$ 的块逆给

$$
B_-=-A_-BC_Q^{-1}\mathsf E_0,
\qquad B_+=B\mathsf E_0.
\tag{5.6}
$$

置 $\Lambda=\epsilon K_0|_{\mathcal Q}$，则 $\Lambda\mathsf E_0=-2\mathsf E_0$。对 (5.2) 的第一块行做完整乘法，有

$$
\epsilon\mathsf U_0^*\mathscr R|_{\mathcal Q}
=A_+B+B\Lambda C_Q.
\tag{5.7}
$$

右乘 $C_Q^{-1}\mathsf E_0$，再用 (5.5)–(5.6)，得到共同差的完全消去：

$$
\boxed{
2B_++A_+A_-^{-1}B_-
=-\epsilon\mathscr R_{01}C_{11}^{\rm inv}.
}
\tag{5.8}
$$

因此真正的配对矩阵也可写成

$$
\boxed{
\mathcal T=-\frac1{\sqrt3p}\mathscr R_{01}C_{11}^{\rm inv}.
}
\tag{5.9}
$$

再令 $J_q=\mathsf V_0^*d_q\mathsf U_0:\mathbb C^u\to\mathbb C^v$。因 $\mathsf U_0^*e_0=0$ 和 $[N_q,e_0]=e_q=d_q^*$，有

$$
\mathsf U_0^*N_q\mathsf E_0=J_q^*/\sqrt3.
$$

所以同一式等价于

$$
\boxed{
\mathcal T=-\frac{\epsilon p}{3}J_q^*C_{11}^{\rm inv}.
}
\tag{5.10}
$$

这里 $d_q$ 是无权 primitive 源之间的真实删除，而 $C_{11}^{\rm inv}$ 保持全部更低出生的 Schur 消元。一般来说

$$
C_{11}^{\rm inv}\ne
(\mathsf E_0^*W\mathsf E_0)^{-1}.
$$

式 (5.9)–(5.10) 只把共同差识别为同一个 Green 块；没有断言该块自动收缩。

## 6. 尚需支付的共同正预算

准确的剩余问题可以用 (4.10) 或以下同一正块表述：

$$
\begin{pmatrix}
\kappa J_+&\mathcal T^*\\
\mathcal T&A_-
\end{pmatrix}\succeq0.
\tag{6.1}
$$

全部矩阵必须来自同一个乘积对角 $W=D^2$，且 $J_+$ 来自相邻物理层的 $D_-^2$。本文未证明存在普适有限 $\kappa$，也未产生实际 Boolean 反例。特别是不能分别估计 (3.9) 或 (4.8) 的两个大项，不能去掉 (3.6) 的 $P$，也不能把 (5.2) 的完整补空间逆替换成预先压缩后的逆。

等权时 $q_i$ 恒定，$d_q\mathsf U_0=0$，故 (5.10) 直接给 $T=0$；一般非等权的联合费用仍须由同源正性来支付。原 graph 的费用接口没有因本稿的有限硬端恒等式而自动关闭。
