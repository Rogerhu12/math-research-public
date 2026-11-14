# 有限单弱位的完整共同缺陷铅笔与逐系数正性的实际失败

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：下述完整有限参数等价、旧缺陷识别、实际 Boolean 负向量及任意固定系数常数的发散障碍已证明。** 本文没有证明完整铅笔必正。负例针对把它逐次数拆为正块的充分路线；真实新增五位硬费用仍满足 R298 的统一严格上界。

## 1. 原物理源和完整共同平方

旧池有 $2s$ 个任意正权，$d=\sum b_iE_i$、$A_{\rm dual}=\sum b_i^{-1}E_i$。沿用 R297 的三个实际 primitive 源

$$
U=K_s(d),\qquad V=K_{s-1}(d),\qquad W=K_{s-2}(d).
$$

记

$$
G=\Gamma_{1,s-1},\quad L=\Gamma_{2,s-1},\quad
Z_j=\Gamma_{j,s-2}\ (1\le j\le4),
$$
$$
A_0=A_{\rm dual}|_U:U\to V,\qquad
A=A_{\rm dual}|_V:V\to W,\qquad R=A_0A_0^*.
$$

空的低出生块整体省略。全部 $\Gamma$ 是完整层逆后压到所列源的真实 MP Gram。

设旧三次桥 $F=(\sum b_i^3E_i)|_V:V\to W$，并置

$$
Q=F^*Z_2,\quad
\delta_2=\frac12(G^{-1}F^*Z_3-F^*Z_2),
$$
$$
\delta_3=\frac13(L^{-1}F^*Z_4-G^{-1}F^*Z_3),
\quad D=\delta_2+\delta_3,\quad
H_0=2G+QA.
\tag{1.1}
$$

新位权为 $a>0$，$t=a^2$。新上、下真实源使用

$$
E_a(x,v)=(x-a\mathcal J_{1,s-1}v,v),
\qquad
F_a(y,w)=(y-a\mathcal J_{1,s-2}w,w).
$$

上源物理度量为 $\operatorname{diag}(I_U,I_V+tG)$。

记新低源第一、第三阶 Gram 的形式为 $J_1(a),J_3(a)$。完整一位 MP 递推给

$$
P=(G^{-1}+tI)^{-1},\quad
V_1=Z_1+tZ_2,\quad V_3=Z_3+tZ_4,
$$
$$
J_1(a)=
\begin{pmatrix}I&0\\-aQ^*&I\end{pmatrix}
\begin{pmatrix}P&0\\0&V_1\end{pmatrix}
\begin{pmatrix}I&-aQ\\0&I\end{pmatrix},
$$
$$
J_3(a)=
\begin{pmatrix}I&0\\-a(Q+D)^*&I\end{pmatrix}
\begin{pmatrix}a^{-2}L&0\\0&V_3\end{pmatrix}
\begin{pmatrix}I&-a(Q+D)\\0&I\end{pmatrix}.
\tag{1.2}
$$

这些是真实形式，不是把非正交源坐标当成欧氏 Gram 算子。

新对偶删除在这两个同源中的准确矩阵为

$$
\boxed{\mathcal A_a=
\begin{pmatrix}A_0&a^{-1}I-2aG\\0&A\end{pmatrix}.}
\tag{1.3}
$$

为核 (1.3)，写 $e=A_{\rm dual}^*$、$R_1=\mathcal J_{1,s-1}$、
$R_-=\mathcal J_{1,s-2}$。旧高度二给 $e|_V=2R_1+A_0^*$，所以
$P_VA_{\rm dual}R_1=2G$；又 $dA_{\rm dual}R_1=A$，故
$A_{\rm dual}R_1=2G+R_-A$。代入两个源图即得 (1.3)。

原硬端费用在 $E_a$ 中的形式是

$$
\mathcal A_a^*J_1(a)J_3(a)^{-1}J_1(a)\mathcal A_a.
$$

下源度量由正确伴随与逆次序抵消；上源度量仍为
$\operatorname{diag}(I,I+tG)$。对输入 $(x,v)$ 定义

$$
r=P[aA_0x+(I-tH_0)v],\qquad
y=D^*r+V_1Av.
\tag{1.4}
$$

则整个费用准确为同一个共同平方

$$
\boxed{\|r\|_{L^{-1}}^2+\|y\|_{V_3^{-1}}^2.}
\tag{1.5}
$$

没有把 $D^*r$ 与 $V_1Av$ 分别取范数。

## 2. 临界对偶关系保留普通首缺陷

有以下准确恒等式：

$$
\boxed{QA=G^{-1}L-4G-R,}
\qquad
\boxed{H_0=G^{-1}L-2G-R.}
\tag{2.1}
$$

特别，

$$
3G+QA=G^{-1}(L-G^2)-R.
\tag{2.2}
$$

这里 $R=A_0A_0^*$ 前面没有额外的 $L^{-1}$。

证明使用真正旧端点 $eR_1=\mathcal J_{2,s-1}$。一方面

$$
A_{\rm dual}e|_V=4G+2R_-A+R.
$$

另一方面，实际塔分解给

$$
A_{\rm dual}\mathcal J_{2,s-1}
 =R_1G^{-1}L+\mathcal J_{2,s-2}A.
$$

对后一式作用 $d$，使用
$d\mathcal J_{2,s-1}=e|_V$、
$d\mathcal J_{2,s-2}=2R_--Q$ 以及 $A_{\rm dual}d=dA_{\rm dual}$，
得到 $A_{\rm dual}e|_V=G^{-1}L+2R_-A-QA$。比较即得 (2.1)。

还需两个已由真实硬端代数支付的关系：

$$
Z_1A=-(2\delta_2^*+\delta_3^*)G,\qquad
Z_2A=-\delta_3^*L.
\tag{2.3}
$$

第二式见 R297 的 (2.10)。第一式可直接在旧中间层的
$[A_{\rm dual},d^*]\mathcal J_{1,s-1}=0$
中投到 $\operatorname{Ran}\mathcal J_{2,s-2}$。这里
$e\mathcal J_{2,s-2}$ 的第三塔系数是二，因为
$d^3e\mathcal J_{2,s-2}=12I_W$；其余第二塔分量与第三塔正交。使用真实两带式，投影后的等式为
$$
2AL^{-1}G-2Z_2^{-1}Z_3F
 =-2FG+2Z_2^{-1}Z_1A.
$$
于是 $Z_1A=Z_2AL^{-1}G-Z_3F+Z_2FG
=-\delta_3^*G-2\delta_2^*G$。这证明第一式，不预设任何 S1 正序。

## 3. 对任意有限正 $a$ 的无逆三块二次铅笔

固定 $\kappa>0$。新增硬端的真实上界 $\mathcal K_a\preceq\kappa I$，当且仅当对每个 $(x,v)$，

$$
\|r\|_{L^{-1}}^2+\|y\|_{V_3^{-1}}^2
 \le\kappa\bigl(\|x\|^2+\langle(I+tG)v,v\rangle\bigr).
\tag{3.1}
$$

将 (3.1) 写成 Schur 正块后，在输出两块使用可逆矩阵

$$
\begin{pmatrix}P^{-1}&0\\-D^*&I\end{pmatrix}.
$$

输出度量变为

$$
\begin{pmatrix}
P^{-1}LP^{-1}&-P^{-1}LD\\
-D^*LP^{-1}&V_3+D^*LD
\end{pmatrix},
$$

而输出源列变为
$[\,aA_0,\ I-tH_0;\ 0,\ V_1A\,]$。再消去输入 $U$ 上的真正正块 $\kappa I_U$，得到精确等价：

$$
\boxed{\mathcal K_a\preceq\kappa I
 \quad\Longleftrightarrow\quad
 \mathscr P_\kappa(t)\succeq0,}
\tag{3.2}
$$
$$
\boxed{
\mathscr P_\kappa(t)=
\begin{pmatrix}
\kappa(I+tG)&I-tH_0^*&A^*(Z_1+tZ_2)\\
I-tH_0&(G^{-1}+tI)L(G^{-1}+tI)-tR/\kappa&
 -(G^{-1}+tI)LD\\
(Z_1+tZ_2)A&-D^*L(G^{-1}+tI)&Z_3+tZ_4+D^*LD
\end{pmatrix}.
}
\tag{3.3}
$$

这个矩阵作用于同一个物理 $V\oplus V\oplus W$，所有乘积次序均保留。

写成三次系数的完整清单：

$$
\mathscr P_\kappa(t)=\mathscr P_{\kappa,0}
+t\mathscr P_{\kappa,1}+t^2\mathscr P_2,
$$
$$
\boxed{
\mathscr P_{\kappa,0}=
\begin{pmatrix}
\kappa I&I&A^*Z_1\\
I&G^{-1}LG^{-1}&-G^{-1}LD\\
Z_1A&-D^*LG^{-1}&Z_3+D^*LD
\end{pmatrix},
}
\tag{3.4}
$$
$$
\boxed{
\mathscr P_{\kappa,1}=
\begin{pmatrix}
\kappa G&-H_0^*&A^*Z_2\\
-H_0&G^{-1}L+LG^{-1}-R/\kappa&-LD\\
Z_2A&-D^*L&Z_4
\end{pmatrix},
\qquad
\mathscr P_2=\operatorname{diag}(0,L,0).
}
\tag{3.5}
$$

这里“二次”指参数 $t$ 的次数，不是省略了新位的任意高次项。

## 4. 两端预算都保留；逐系数正性不是必要条件

先消去 (3.4) 中间正块，再用 (2.3)，得到

$$
\begin{pmatrix}
\kappa I-GL^{-1}G&-G\delta_2\\
-\delta_2^*G&Z_3
\end{pmatrix}.
$$

所以

$$
\boxed{
\mathscr P_{\kappa,0}\succeq0
\iff
G(L^{-1}+\delta_2Z_3^{-1}\delta_2^*)G\preceq\kappa I.
}
\tag{4.1}
$$

这正是旧 $V$ 的首加强费用；普通首边缺陷没有被单独丢弃。

一次块的第 1、3 主块若正，必须有

$$
A^*Z_2Z_4^{-1}Z_2A\preceq\kappa G.
\tag{4.2}
$$

由第二个 (2.3)，它正是旧高度二 $V$ 的最后加强费用。该强端预算不能从同一个旧首边的非严格界免费得到。

若 $\mathscr P_{\kappa,0}$ 和 $\mathscr P_{\kappa,1}$ 都正，则 (3.2) 当然成立。但下面证明，即使真实全部有限参数都有统一严格界，要求一次系数正的路线仍会对每个固定有限 $\kappa$ 失败。必须保留常数旧缺陷、一次负项和 $t^2L$ 的共同补偿。

## 5. 实际四权族：一次系数需要的常数发散

取旧四位

$$
b=(r,r^{-1},1,1),\qquad r>0.
\tag{5.1}
$$

这是实际完整 Boolean 模型。考虑交换最后两位的不变部分，旧 $V=K_1$ 的其中两个物理源由

$$
E_r=
\begin{pmatrix}
1&0\\
0&1\\
-r/2&-1/(2r)\\
-r/2&-1/(2r)
\end{pmatrix}
$$

表示，其物理度量是

$$
H=E_r^*E_r=
\begin{pmatrix}1+r^2/2&1/2\\1/2&1+1/(2r^2)\end{pmatrix}.
\tag{5.2}
$$

这个组不变部分同时约化 $d,d^*,A_{\rm dual}$、完整物理逆与 primitive 投影，故下面是完整源上的真实限制。

令 $z_i=b_i^2$、$S=\sum z_i$。完整第一层 Gram 为
$F_1=SI-2\operatorname{diag}(z)+bb^*$。准确的两个形式及算子为

$$
\widehat G=E_r^*F_1^{-1}E_r,\qquad
\widehat L=E_r^*\operatorname{diag}(z_i^2)E_r,
\quad G=H^{-1}\widehat G,\quad L=H^{-1}\widehat L.
\tag{5.3}
$$

第一式先逆完整 $F_1$；第二式使用旧高度二的完整顶逆，且本族 $\prod b_i=1$。再取

$$
A=(b_i^{-1})^*E_r,\quad
F=(b_i^3)^*E_r,\quad
Q=H^{-1}F^*/e_2(z),\quad H_0=2G+QA,
\quad R=G^{-1}L-4G-QA.
\tag{5.4}
$$

(5.4) 的 $R$ 正是真实 $A_0A_0^*$ 的限制。

一次块前两个主块的 Schur 正性要求

$$
\boxed{
\kappa(G^{-1}L+LG^{-1})
 \succeq R+H_0G^{-1}H_0^*.
}
\tag{5.5}
$$

令 $v_r=E_r(1,0)^T$。按 (5.2) 的物理内积，直接的有理化简给

$$
J(r):=\langle(G^{-1}L+LG^{-1})v_r,v_r\rangle
 =\frac{r^8+4r^6+8r^4+4r^2+1}{r^4+r^2+1}>0,
\tag{5.6}
$$
$$
N(r):=\langle(R+H_0G^{-1}H_0^*)v_r,v_r\rangle
 =\frac{P(r)}{8(r^4+r^2+1)^3},
$$
$$
P(r)=2r^{18}+r^{16}+14r^{14}+63r^{12}+160r^{10}
 +179r^8+138r^6+73r^4+14r^2+4.
\tag{5.7}
$$

所有分母在 $r>0$ 严格正。这两条等式由 (5.2)–(5.4) 的 $2\times2$ 有理矩阵展开即可重建；配套脚本保存精确计算而不是浮点谱。

所以一次块为正必须满足

$$
\kappa\ge\frac{N(r)}{J(r)}
 =\frac{P(r)}
 {8(r^4+r^2+1)^2(r^8+4r^6+8r^4+4r^2+1)}
 \sim\frac{r^2}{4}.
\tag{5.8}
$$

**结论：不存在一个有限的权无关 $\kappa$，能使所有实际 Boolean 模型的这个一次系数都为正。** 这排除了只扩大系数常数后再逐次数取正的路线。

## 6. 一个完整有理负向量；不反真实硬端

取 $r=3$、$\kappa=1$。此时

$$
\widehat G=
\begin{pmatrix}1881/236&27/236\\27/236&209/2124\end{pmatrix},
\quad
\widehat L=
\begin{pmatrix}171/2&1/2\\1/2&11/162\end{pmatrix},
\quad
H=\begin{pmatrix}11/2&1/2\\1/2&19/18\end{pmatrix}.
$$

在三个物理块 $V\oplus V\oplus W$ 中取

$$
u_1=E_3\binom{9330/8281}{274752/8281},\qquad
u_2=E_3\binom10,\qquad w=0.
\tag{6.1}
$$

亦即实际四坐标

$$
u_1=(9330/8281,\ 274752/8281,\ -657/91,\ -657/91),
\qquad
u_2=(1,0,-3/2,-3/2).
$$

它们都严格在原 $b^\perp$ 中。代入一次系数，精确得到

$$
\boxed{
\left\langle\mathscr P_{1,1}(u_1,u_2,0),(u_1,u_2,0)\right\rangle
=-\frac{31980847}{753571}<0.
}
\tag{6.2}
$$

构造上 $u_1=G^{-1}H_0^*u_2$，所以 (6.2) 正是 $J(3)-N(3)$，没有浮点核选择。

对任意 $r>0,a>0$，实际新增五权 $(r,r^{-1},1,1,a)$ 的整个硬端由
[R298 全五独立权定理](../results/R298-five-independent-positive-weights-birth-two-hard-top-strengthened-s1.md)
满足 $\mathcal K_a\preceq(743/782)I<I$。因此完整 $\mathscr P_1(t)$ 对每个 $t>0$ 都正，而其一次系数可按 (5.8) 任意严重地失去正性。这不是强化首边或原 ISP 的反例。

下一步可在完整半线上寻找保共同缺陷的矩阵平方分解，不能将
$\mathscr P_1(t)\succeq0$ 换成各系数分别为正。
