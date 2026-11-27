# 全原 unit211 的 N1 二次头与 Phi=0 的无几何分母十二生成元环境

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 原 N1 的确切二次头

采用已完整证明的
[R150-appendix-unit211-compact-original-scalar-means-and-N1-identities.md](R150-appendix-unit211-compact-original-scalar-means-and-N1-identities.md)
的原均值、原 $N_4$ 极化及 $N_1$ 归一。令
$$
z=Qt,\quad \delta=b-c,\quad \rho^2=1-Q,\quad
m=\rho\delta=u-\ell,\quad
J=2u(1-u)+\ell Q,
$$
$$
G=\lambda P_{02}+(u-1)T_0.
$$
原 E0/N0 的同一点恢复给
$$
V_n=Jf-G+bc\,z,\qquad
W_*=T_0+4uf,\qquad N=QW_*-2V_n.
$$
此时 $f$ 仍为自由未知，并未假设 $\Phi=0$，也未先解原 $N(V)$ 线。

令 $N_1^*=4bc\,\rho^2Q^2N_1$。其作为 $(f,z)$ 二次式的 $z^2$ 系数是
$$
\boxed{[z^2]N_1^*=-4(bc)^2\ell Q(u-1).}
$$
因此在当前已支付
$$
bc\,\rho Q\,\ell(u-1)\ne0
$$
的原域内，N1 对 $z$ 有真正的非零权参数二次头。这里不含 $\Phi$、$D$、$S\zeta$、原两线行列式或任何范数。

证明只需提取已经支付的紧凑式。记
$$
\alpha=\ell(1-u)-m,\quad
\beta\rho=\ell\rho^2-m(1-u),
$$
$$
A_V=(2u-1)\ell+3m,\quad
B_U\rho=(2u-1)m+3\ell\rho^2.
$$
因 $[z]V_n=bc$、$[z]N=-2bc$、$W_*$ 与 $z$ 无关，紧凑极化式的 $z^2$ 系数恰为
$$
4(bc)^2\{\alpha(1+\rho^2)-2\beta\rho
              +\rho^2A_V+\rho B_U-2u\rho^2\}.
$$
括号内先合并为
$$
\ell(1-u)+\{\ell(1+u)-2u\}\rho^2+2m\rho^2.
$$
用 $m=u-\ell$、$1-\rho^2=Q$，它等于
$$
-\ell Q(u-1).
$$

原 $P_j=3\tau((g_0-\tau(g_0)\mathbf1)^2
(g_1-\tau(g_1)\mathbf1))$ 在 E0/N0 恢复后关于 $f,z$ 至多一次：$g_0$ 只含权参数，$g_1$ 的每项关于 $f,z$ 仿射。因此 $N_1=N_v-\frac{4\lambda}{3}P_j$ 的二次头不受该项影响。这证明上式在 $f$ 自由时即成立，不需要 P1 的额外代入。

等价地，未清分母的原 $N_1$ 对 $z^2$ 的系数是
$$
-\frac{bc\,\ell(u-1)}{\rho^2Q},
$$
而对原 $t^2$ 的系数是
$$
-\frac{bc\,\ell Q(u-1)}{1-Q}.
$$
三种归一必须区分。

## 2. Phi=0 上先保 z，不解几何分母

现在限制到原 $\Phi=0$ 面，继续保当前已付权单位。令
$$
\ell=1-\frac{2(u-1)(u-2)}Q,\quad
T_0=-Q-4(u-1),\quad J-Q=-4(u-1)^2,
$$
$$
P_{02}=2(u-1)\ell Q,\quad P_f=T_0(J-Q).
$$
原 P1 是
$$
P_f f+P_c=0,\qquad
P_c=QP_{02}(\ell+T)-G T_0.
$$
所以
$$
f=-P_c/P_f
$$
关于 $T$ 仿射，全部分母都是已经支付的权参数单位；它不依赖 $z$，也不需要 $D$ 或 $S\zeta$ 的逆。

将它代入紧凑原 $N_1^*$，并用已付的同一点 P1 身份 $P_j=3wP_{02}$、$w=\lambda-1-T$，得到
$$
N_1^*(T,z)=L z^2+A(T)z+B(T),
\qquad
L=-4(bc)^2\ell Q(u-1).
$$
这里
$$
\deg_T A\le1,\qquad \deg_T B\le2.
$$
于是原 N1 可写成真正的首一关系
$$
g_2(T,z)=z^2+\frac{A(T)}Lz+\frac{B(T)}L=0.
$$
只倒置已付权单位 $L$。不解原 $N(V)$ 线，故不会在此引入 $S_nZ$ 分母。

## 3. 与原矩关系组成真正的十二生成元环境

令 $R$ 是 $\mathbb Q[u,Q,\lambda]$ 在当前已付权单位处的局部化，$\ell$ 按上式代入。原矩多项式为
$$
F_6(T)=M K^2-4(u-\ell)^2D^3,
$$
$$
M=\ell(2u-\ell Q)-u^2,\quad
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell TA_2+2T^3.
$$
它的 $T^6$ 首项是已付权单位 $4\ell^2(1-Q)$。除去该首项得到 $\widehat F_6$，其首一性不依赖几何分母。定义
$$
\mathcal A=
R[T,z]/(\widehat F_6(T),g_2(T,z)).
$$
先按首一 $\widehat F_6$ 除法，再在 $R[T]/(\widehat F_6)$ 上按首一 $g_2$ 除法，给出唯一表示
$$
\sum_{i=0}^5 a_iT^i+\sum_{i=0}^5 b_iT^iz.
$$
所以 $\mathcal A$ 是一个自由 $R$ 模，秩为 **12**，基为
$$
1,T,\ldots,T^5,\quad z,Tz,\ldots,T^5z.
$$
这个结论对商中的零因子也成立：只用两条真正首一关系，不要求商是域或约化代数。

原 $\Phi=0$ 点满足两条关系，因此给出 $\mathcal A$ 的同一点取值同态。这个自由十二维环境是包含原点的有限环境，不等于原解集；还须施加其余原方程及物理单位。

## 4. 原 N(V) 与其余均值保为额外行

此前实际恢复记号满足
$$
N_{F,4}=4(u-\ell)D^2N_F,\quad
N_{C,4}=4(u-\ell)D^2N_C,
$$
$$
4(u-\ell)D^2N_t=2bc\,Q\,S_nZ.
$$
由于 $z=Qt$，原 $N(V)$ 线现在保为
$$
N_{F,4}f+N_{C,4}+2bc\,S_nZ\,z=0.
$$
这是 $\mathcal A$ 中的额外原必要行，**没有**倒置 $S_nZ$。其余原均值使用已付的 $R_2,W_4,O_8$ 紧凑式，约化到同一十二生成元环境即可。原 N1 已作为首一关系使用，不能误认为其余原值条件也随之成立。

物理上仍需 $D,S,\zeta$ 非零。后续若使用单位目标，可以保
$$
U=D S_nZ
$$
及它的实际幂作为原点非零目标，检查完整原行组合；不能把整个 $\mathcal A$ 中的 $U$ 自动当可逆元。

本稿直接利用已完成的原恒等式提取二次头并给出真正首一的环境，不要求重放失败的统一 Gram 或两几何分母代入。随后实际参数运算须保这些同一点行和全部权单位零支，不能用形式十二维性直接宣称排空原面。
