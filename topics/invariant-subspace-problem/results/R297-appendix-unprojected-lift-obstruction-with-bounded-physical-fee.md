# 奇数硬端：两个自然完整提升的范数会发散，最小物理提升仍有界

日期：2026-11-14 UTC。作者：Astra-ISP-789f / literature_audit；对角提升由 root 提出。

状态：**已证明的方法边界**。本稿只排除对下述两个完整提升直接取统一范数上界；不反驳硬端目标，也不产生 Boolean 相邻不等式反例。所有空间均采用物理平方自由基的原内积。

## 1. 硬端目标与两个真提升

设 $M=2r+1$，$d=\sum_i b_iE_i$，$A=\sum_i b_i^{-1}E_i$，$b_i>0$。记

$$
U=\ker d\cap\mathcal H_r,\qquad
V=\ker d\cap\mathcal H_{r-1},\qquad
A_U=A|_U:U\longrightarrow V.
$$

下出生的完整 Moore--Penrose 提升为

$$
J_j=(d^j/j!)^\dagger|_V,\qquad L_j=J_j^*J_j.
$$

[硬端消逆稿](R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md)已证明真正硬端创新费用为

$$
\mathcal K=A_U^*L_1L_3^{-1}L_1A_U.                       \tag{1.1}
$$

所以任何物理映射 $W:U\to\mathcal H_{r+2}$ 满足

$$
J_3^*W=L_1A_U                                             \tag{1.2}
$$

都给出 $\mathcal K=W^*P_{\operatorname{Ran}J_3}W$。关键是这里的物理正交投影不能随意删去。

以下记 $R=d|_{\mathcal H_r}$，$F=RR^*$，$Q=R^*F^{-1}R=P_{U^\perp}$，$\mathfrak c$ 为相应层间的补集酉映射。中央两个自伴矩阵为

$$
K=d|_{\mathcal H_{r+1}}\,\mathfrak c,
\qquad
H=A|_{\mathcal H_{r+1}}\,\mathfrak c.
$$

于是有两个不先逆 $L_3$ 的具体提升：

$$
W_{\rm can}=\frac16\mathfrak c\,RKQH^2|_U,               \tag{1.3}
$$

以及令 $p=\prod_i b_i$、$Z=\operatorname{diag}(b_J^2)$ 在完整 $\mathcal H_{r-1}$ 上，

$$
W_{\rm diag}=(-1)^{r-1}p\,\mathfrak c\,Z^{-1}F^{-1}A_U.  \tag{1.4}
$$

两个式子都确实满足 (1.2)，不是近似提升。对 (1.4)，利用硬端顶提升

$$
J_3=\frac{(-1)^{r-1}}p\mathfrak c Z|_V
$$

直接得到 $J_3^*W_{\rm diag}=P_VF^{-1}A_U=L_1A_U$。对 (1.3)，完整方阵恒等式

$$
(d^3/6)\mathfrak c=RKR^*/6
$$

给出 $J_3^*=6P_V(RKR^*)^{-1}\mathfrak c^*$；又 $RH^2|_U=A_U$，故

$$
\begin{aligned}
J_3^*W_{\rm can}
&=P_V(RKR^*)^{-1}RK R^*F^{-1}RH^2|_U\\
&=P_VF^{-1}A_U=L_1A_U.
\end{aligned}
$$

这里 $AK=RH$ 由 $[A,d]=0$ 与补集关系直接给出；又 $KH=de$，且 $de|_U=I$，中央 $K$ 可逆，故 $H|_U=K^{-1}|_U$。因此 $RH^2|_U=A_U$：对 $u\in U$，$AKHu=Au=RH^2u$。

## 2. 五位的同一精确源

取 $M=5,r=2$，正权

$$
(b_0,b_1,b_2,b_3,b_4)=(t,t^{-1},1,1,1),\qquad t>0.
$$

在物理二次基上定义 $u$：

$$
u_{01}=3,\qquad
u_{0j}=-t^{-1},\qquad
u_{1j}=-t,\qquad
u_{jk}=1\quad(2\le j<k\le4).                              \tag{2.1}
$$

每个删除方程直接给 $du=0$。例如第 $0$、$1$、$j\ge2$ 行分别为

$$
3t^{-1}-3t^{-1}=0,\quad
3t-3t=0,\quad
-1-1+2=0.
$$

此源的范数为

$$
\|u\|^2=3(t^2+t^{-2}+4).                                  \tag{2.2}
$$

置 $S_3$ 作用于三个等权位 $2,3,4$。其在 $U$ 中的不变空间恰为 $\mathbb C u$：若四类坐标依次为 $x,y,z,w$，删除方程强制 $y=-x/(3t)$、$z=-tx/3$、$w=x/3$。$H$ 和 $P_U$ 与此作用交换，且直接乘法给

$$
\|Hu\|^2=\|u\|^2,
\qquad
P_UH^2u=u.                                                  \tag{2.3}
$$

具体地，$Hu$ 的四类坐标为 $3,-t,-t^{-1},1$，故第一式直接成立；第二式由第一式与不变空间一维推出。因此 (1.3) 在该源无需计算完整 $P_U$：

$$
W_{\rm can}u=\frac16\mathfrak c RK(H^2u-u).
$$

## 3. 两个完整提升都无统一界

按完整 $\mathcal H_1$ 的坐标 $0,1,2,3,4$ 排列，直接矩阵乘法给

$$
\mathfrak c^*W_{\rm can}u=
\begin{pmatrix}
-2t+3t^{-1}-t^{-3}\\
-t^3+3t-2t^{-1}\\
-t^2+2-t^{-2}\\
-t^2+2-t^{-2}\\
-t^2+2-t^{-2}
\end{pmatrix}.                                               \tag{3.1}
$$

记 $P(t)=t^4+4t^2+1$，于是

$$
\boxed{
\frac{\|W_{\rm can}u\|^2}{\|u\|^2}
=\frac{(t^2-1)^2(t^4+1)(t^4-t^2+1)}{3t^4P(t)}
\sim\frac{t^4}{3}.}                                         \tag{3.2}
$$

另记 $q=F^{-1}A_Uu$。这里 $p=1$、$Z=\operatorname{diag}(t^2,t^{-2},1,1,1)$，直接解五个线性方程得

$$
Z^{-1}q=
\begin{pmatrix}
(t^4-1)/(2t^3)\\
(1-t^4)/(2t)\\
-(t^2-1)^2/(2t^2)\\
-(t^2-1)^2/(2t^2)\\
-(t^2-1)^2/(2t^2)
\end{pmatrix}.                                               \tag{3.3}
$$

这组方程可不借逆矩阵核查：

$$
A_Uu=(3(t-t^{-1}),-3(t-t^{-1}),2-t^2-t^{-2},2-t^2-t^{-2},2-t^2-t^{-2})^T,
$$

而 $F$ 的对角元为 $\sum_i b_i^2-b_j^2$，非对角元为 $b_i b_j$；将 $q=Z(Z^{-1}q)$ 代入即可。

由 (1.4) 的全局负号不影响范数，得到

$$
\boxed{
\frac{\|W_{\rm diag}u\|^2}{\|u\|^2}
=\frac{(t^2-1)^2(t^4-t^2+1)(t^4+6t^2+1)}{12t^4P(t)}
\sim\frac{t^4}{12}.}                                        \tag{3.4}
$$

所以即使固定 $M=5,r=2$，对这两个具体完整提升都不存在与正权无关的有限范数上界。

## 4. 同一源的实际最小提升没有发散

由于 $V=b^\perp\subset\mathcal H_1$ 且 $J_3=-\mathfrak c Z|_V$，其补集坐标中的值域为 $ZV$；正交补恰为 $\mathbb C Z^{-1}b$。令 $v=Z^{-1}b=(t^{-1},t,1,1,1)^T$，物理正交投影给

$$
\begin{aligned}
\langle u,\mathcal Ku\rangle
&=\|P_{ZV}Z^{-1}q\|^2\\
&=\|Z^{-1}q\|^2-
\frac{|\langle v,Z^{-1}q\rangle|^2}{\|v\|^2}.
\end{aligned}                                                \tag{4.1}
$$

将 (3.3) 代入得到完全化简的真费用

$$
\boxed{
\frac{\langle u,\mathcal Ku\rangle}{\|u\|^2}
=\frac{(t^2-1)^2(t^4+8t^2+1)}
 {3(t^4+3t^2+1)(t^4+4t^2+1)}
<\frac13,
}                                                            \tag{4.2}
$$

且当 $t\to\infty$ 时趋于 $1/3$。严格上界由置 $x=t^2$ 后的恒等式

$$
(x^2+3x+1)(x^2+4x+1)-(x-1)^2(x^2+8x+1)
=x^3+28x^2+x>0
$$

直接给出。这里的上界只对明确给出的同一源 $u$，没有断言整个五位算子的最大费用也小于 $1/3$。

两个完整提升在 (3.2)、(3.4) 中的发散完全来自 $\operatorname{Ran}J_3$ 的正交补分量。后续若沿这两条提升继续，必须保留 (4.1) 类型的真实正交消去；把投影删除后求统一粗界这一充分路线已被上述正权 Boolean 家族严格排除。一般硬端 $\mathcal K\le\kappa I$ 仍未证明，也未被本稿反驳。
