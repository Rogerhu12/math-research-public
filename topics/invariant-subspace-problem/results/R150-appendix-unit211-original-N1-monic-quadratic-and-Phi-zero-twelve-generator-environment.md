# 全原 unit211 的 N1 二次头与 Phi=0 的无几何分母十二生成元环境

日期：2026-11-27（Asia/Taipei）；2026-11-28 按真实原均值更正依赖范围  
会话：Astra-ISP-8542378f-20261127

> **2026-11-28 独立有效范围核验：** 本稿 §§1–3 的 N1 极化和两点矩式不依赖错误 compact E1，结论保留。原 §4 对旧 R2 的引用已替换为正确原式；旧第一头、H1、H42、583 或 h=k 的派生单位均不得由本稿恢复。参见[原定义更正与隔离](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md)。

## 1. 原 N1 的确切二次头

采用已完整证明的
[R150-appendix-unit211-compact-original-scalar-means-and-N1-identities.md](R150-appendix-unit211-compact-original-scalar-means-and-N1-identities.md)
中独立正确的原 $N_4$ 极化及 $N_1$ 归一；不采用其已撤回的 E1/R2 身份。完整正确的原式已由[七变量自含源](../notes/2026-11-28-unit211-corrected-dual-germ-compact-original-identities-8542.js)返回。令
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

准确指定此处坐标图为 $Q(1-Q)P_fP_{02}bc\ne0$。设
$
K_0=Q+4u-4,\quad L_0=Q-2(u-1)(u-2),\quad M_n=2uL_0-L_0^2-u^2Q.
$
由 $P_f=4(u-1)^2K_0$、$P_{02}=2(u-1)L_0$、$M_n=4bc(1-Q)Q$，只需局部化直接原乘积
$
U=Q(1-Q)(u-1)K_0L_0M_n.
$
令 $R=\mathbb Q[u,Q,\lambda,U^{-1}]$，$\ell=L_0/Q$。这些单位直接来自指定原图；没有借用旧错误第一头的任何排除。原矩多项式为
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

## 4. 其余原行与坐标范围

其余原均值必须使用[更正后的真实四行](R150-appendix-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads.md)。特别是令
$$
n_n=Q(T_0+4uf)-2V_n,\qquad \Delta_Q=1-Q,\qquad m=u-\ell,
$$
第一原行应为
$$
\overline R_{\rm true}
=4Q(f-u)(V_n-Qf)+bc\,z^2
+z(4bc\,uQ-\ell V_n)+\frac{m}{2\Delta_Q}z n_n.
$$
它与独立正确的 $W_4,\overline O$ 及全部原值条件，都在同一个 $\mathcal A$ 中施加为额外关系。原 N1 已作为首一关系使用，不能因此省略其余方程。

此前几何恢复若另有完整原图与同点来源，可继续使用
$$
N_{F,4}=4(u-\ell)D^2N_F,\quad
N_{C,4}=4(u-\ell)D^2N_C,\quad
4(u-\ell)D^2N_t=2bc\,Q\,S_nZ
$$
所给的额外行
$$
N_{F,4}f+N_{C,4}+2bc\,S_nZ\,z=0.
$$
本稿不为该几何恢复的 $D,S,\zeta,u-\ell$ 或 $S_nZ$ 支付任何新单位。若在其独立原图内检查某个实际非零目标及其幂，必须另外保全部边界与原来源；不能把 $DS_nZ$ 自动当作整个 $\mathcal A$ 的可逆元。

原解的坐标代数是这个秩十二自由环境的进一步商；该商未必自由、未必处处非零，也未由本稿排空。本次只修正依赖说明，没有重跑任何冻结计算，亦不恢复旧错误 Rbar 模型的三生成、有限界或排除结论。
