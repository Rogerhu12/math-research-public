# R716：不预先求极部修正的曲率 jet 提取与相对全尾

日期：2026-11-14。状态：**在 R616 的同一实际本原非消失前提内，以下构造、非零恒等式和完整尾界已证明；实际一般 $p$ 的代数模型计算与单一高度首项仍未执行。**

R703 使用代数曲率原函数，其中包含一个需以 Riemann–Roch 求出的 $\gamma_i$。本文给一个较大的代数函数空间，连这个具体的 $\gamma_i$ 也不必预先求出。代价是空间未必有表列的全部线性独立性；用完整有限关系矩阵处理所有关系，不能假设这些新增亚纯一次积分代数独立。

新的可提取值来自四个长度四的混合项，精确为 $-1/L_j^2,1/L_g^2,1/L_i^2,-1/L_g^2$。其非零性不会被任何极部修正、第二类周期、规范全纯差或 $Y$ 高度常数改变。

## 1. 同一实际高度和一个有限极点空间

保留 R634/R699/R703 的原 $X=X_1,c_1,z=a-1,q:X\to A$、实际 $\kappa$ 坐标与

$$
 L'(g_{-1,+},1)L(g_{-1,-},1)\ne0,\qquad
 \Lambda_i(c_1)=d_i,\qquad
 t_a=1+\frac{I_a}{L_a},\qquad L_a\ne0.
\tag{716.1}
$$

这里 $I_a=\int_{c_1}^{(\cdot)}\varpi_a$ 是原 $A$ 特征微分的形式积分。$L_a=\varpi_a(\log_p\beta)$ 不被假定为单位。

按 R699 §2 选一个代数的 $F$ 相容对称 splitting。它不改变真实 $E_{ij}$。固定 $1\le i<j\le g-1$，把相应代数曲率写成

$$
 \alpha_\nu
 =\sum_b\omega_{\nu b}\otimes[\eta_{\nu b}],
 \qquad \nu\in\{i,j\},\qquad
 \omega_{\nu b}\in q^*H^0(A,\Omega^1),\qquad
 \cup\alpha_\nu=0.
\tag{716.2}
$$

在某个有限数域 $K$ 上选一个点 $Q\ne c_1$，其闭包避开 R699 的整形式盘。扩张 $K$ 后可令 $Q$ 为 $K$-点。按 R699 §3，所有第二类代表 $\eta_{\nu b}$ 可只在 $Q$ 有极点，且在该 CM 盘正则。令

$$
 M=\max\bigl(2,\ \operatorname{poleord}_Q\eta_{\nu b}\bigr),
 \qquad
 \mathcal R=H^0(X_K,\Omega^1((M-1)Q)).
\tag{716.3}
$$

$M$ 只由已选代数代表决定，不是实际高度的未知常数。设 $G=g(X)$。由 Riemann–Roch，$Q$ 为一点且 $M-1>0$，

$$
 h:=\dim_K\mathcal R=G+M-2.
\tag{716.4}
$$

取 $\mathcal R$ 的代数基 $\rho_1,\ldots,\rho_h$，使

$$
 \rho_1=\varpi_i,\quad \rho_2=\varpi_j,\quad
 \rho_3=\varpi_g,\qquad
 x_a=\int_{c_1}^{(\cdot)}\rho_a\quad(1\le a\le h).
\tag{716.5}
$$

这些微分在 $X^\circ=X\setminus\{Q\}$ 正则。单个极点处的留数由留数定理为零，故它们都是第二类微分。所有 $x_a$ 在 $c_1$ 归零，其 Taylor 系数在 $K$ 中。$a>3$ 的积分一般不是全纯 Abel 积分，本文不把它们当作该类积分使用。

定义没有极部修正的二重积分

$$
 U_\nu^{\rm raw}
 =\int_{c_1}^{(\cdot)}
       \sum_b\omega_{\nu b}
               \int_{c_1}^{(\cdot)}\eta_{\nu b},
 \qquad U_\nu^{\rm raw}(c_1)=0.
\tag{716.6}
$$

## 2. 全部未知修正都进入已知的一次积分空间

**引理 716.1。** 存在某个常数线性式 $C_\nu$，使同一真实高度满足

$$
 \boxed{\quad
 \Lambda_\nu=d_\nu+U_\nu^{\rm raw}
                  +C_\nu(x_1,\ldots,x_h).
 \quad}
\tag{716.7}
$$

这个等式不需要先求出 $C_\nu$ 或任何 $\gamma_\nu$。

**证明。** 在 $Q$ 的局部参数 $u$ 中，$\eta_{\nu b}$ 的极阶至多 $M$，且留数为零。其局部原函数的极阶因此至多 $M-1$。乘全纯微分 $\omega_{\nu b}$ 后，

$$
 \sum_b\omega_{\nu b}\int\eta_{\nu b}
$$

的极阶仍至多 $M-1$。改变内积分常数只增加全纯微分，故这个极部是代数的，不依赖实际积分周期。所需极部的留数为曲率 cup 的标量，因 (716.2) 为零。

对任意给定的微分极部，Riemann–Roch 的唯一障碍是留数总和。于是存在

$$
 \gamma_\nu\in\mathcal R
$$

抵消上述极部。这里仅证明其在已知空间中存在，不求它的系数。所得 $U_\nu^{\rm raw}+\int\gamma_\nu$ 是 R699 §4 的同曲率原函数。BMS Proposition 3.5、Remark 3.6 给它与实际规范高度之差的微分为全局全纯微分；这个全纯空间包含于 $\mathcal R$。在 $c_1$ 取值给常数 $d_\nu$。因此全部差等于某个 $\mathcal R\otimes_K\mathbb C_p$ 微分的积分，证明 (716.7)。$\square$

这一步保留实际的第二类周期和 $-2\ell_\nu(P)$；它们只变成 $C_\nu$ 的未知常数系数，没有被设为零。与 R703 的 $\mu_3$ 降维相比，这里使用较大的单极点空间，以换取不预先计算 $\gamma_\nu$。

## 3. 一个允许有关系的显式有限函数族

写

$$
 A_1=\frac{2x_1}{L_i}+\frac{x_1^2}{L_i^2},\quad
 A_2=\frac{2x_2}{L_j}+\frac{x_2^2}{L_j^2},\quad
 A_3=\frac{2x_3}{L_g}+\frac{x_3^2}{L_g^2}.
\tag{716.8}
$$

R696 给原候选 $\omega=\omega_0=0$。用 (716.7)，同一外积严格等于

$$
 E_{ij}
 =(d_iA_1-U_i^{\rm raw}-C_i)(A_2-A_3)
 -(d_jA_2-U_j^{\rm raw}-C_j)(A_1-A_3).
\tag{716.9}
$$

取以下标记函数族 $\mathscr B^{\rm raw}$：

| 函数 | 个数 |
|---|---:|
| $x_ax_b,\ 1\le a\le b\le3$ | $6$ |
| $x_ax_b^2,\ 1\le a,b\le3$ | $9$ |
| $x_a^2x_b^2,\ 1\le a<b\le3$ | $3$ |
| $x_ax_b,\ x_ax_b^2,\ 4\le a\le h,\ 1\le b\le3$ | $6(h-3)$ |
| $U_i^{\rm raw}x_2,\ U_i^{\rm raw}x_3,\ U_i^{\rm raw}x_2^2,\ U_i^{\rm raw}x_3^2$ | $4$ |
| $U_j^{\rm raw}x_1,\ U_j^{\rm raw}x_3,\ U_j^{\rm raw}x_1^2,\ U_j^{\rm raw}x_3^2$ | $4$ |

其个数为 $D_0=6h+8$，全部 Taylor 系数在 $K$ 中，全部迭代长度至多四。(716.9) 给一个明确的常数组合

$$
 E_{ij}=\sum_{B\in\mathscr B^{\rm raw}}c_BB.
\tag{716.10}
$$

这次不声称整个标记族线性独立。新增亚纯积分可能产生精确函数关系。下面只先证明，任何这样的关系都不能涉及四个指定的顶层混合项。

## 4. 四个顶层混合系数不受任何函数关系影响

令

$$
 H=H^1_{\rm dR}(X_K),\qquad F^1=H^0(X_K,\Omega^1)\subset H.
$$

对单个删点有自然同构

$$
 H^1_{\rm dR}(X_K)\xrightarrow{\sim}
 H^1_{\rm dR}(X^\circ_K).
\tag{716.11}
$$

例如用局部 Laurent de Rham 复形可得到删点正合序列，其唯一新增项是 $Q$ 的一维留数项；该项到 $H^2_{\rm dR}(X)$ 的映射是次数一，故同构。这同时解释了这里坚持只删一个 $K$-点的便利。

取一个补空间 $H=F^1\oplus W$。R634 §6 的实际 NS 独立性及 BMS Lemma 7.12 表明，$\alpha_i,\alpha_j$ 在

$$
 (F^1\otimes H)/(F^1\otimes F^1)
$$

中线性独立。记其在 $F^1\otimes W$ 的投影为 $\bar\alpha_i,\bar\alpha_j$。

**引理 716.2。** 若

$$
 \sum_{B\in\mathscr B^{\rm raw}}b_BB=0
\tag{716.12}
$$

作为 $c_1$ 处形式级数成立，则四个系数

$$
 b_{U_i^{\rm raw}x_2^2},\quad
 b_{U_i^{\rm raw}x_3^2},\quad
 b_{U_j^{\rm raw}x_1^2},\quad
 b_{U_j^{\rm raw}x_3^2}
\tag{716.13}
$$

全部为零。

**证明。** 先对 $K$ 系数的关系，在光滑连通开曲线 $X^\circ$ 上应用 BMS Theorem 3.15 的迭代长度过滤和 $D_4$。形式零在一个邻域给解析零，Vologodsky identity principle 使 (716.12) 为零函数；该原理适用于光滑连通开簇，见 BMS §3.1 及 Proposition 9.1 证明中的同一联络论证。所有 Taylor 系数在 $K$ 中，且列数有限，所以全部形式关系的 $\mathbb C_p$ 空间是其 $K$ 关系空间的标量扩张：无限系数矩阵的行空间有限维，可从其中选有限行基。因此对 $K$ 关系的结论也给全部 $\mathbb C_p$ 关系的结论，无需把未知高度常数先假定为代数数。

全部长度至多三的表列项被 $D_4$ 杀掉。纯四次项只用 $x_1,x_2,x_3$，其 $D_4$ 在 $(F^1)^{\otimes4}$ 中。将 $D_4$ 再投影到

$$
 H^{\otimes4}/(F^1)^{\otimes4},
\tag{716.14}
$$

便只剩 (716.13) 对应的四个张量：

$$
 \bar\alpha_i*(\varpi_j*\varpi_j),\quad
 \bar\alpha_i*(\varpi_g*\varpi_g),\quad
 \bar\alpha_j*(\varpi_i*\varpi_i),\quad
 \bar\alpha_j*(\varpi_g*\varpi_g).
\tag{716.15}
$$

这里 $*$ 是 shuffle 乘法；平方的因子二由这个定义完整保留。

BMS Lemma 7.10、Corollary 7.11 在 $m=2,k=1$ 的情形给注入

$$
 \operatorname{Sym}^2(F^1)\otimes(F^1\otimes W)
 \lhook\joinrel\longrightarrow
 H^{\otimes4}/(F^1)^{\otimes4}.
\tag{716.16}
$$

$\bar\alpha_i,\bar\alpha_j$ 独立；$\varpi_i,\varpi_j,\varpi_g$ 独立，其平方也独立。因此 (716.15) 是四个独立向量，强迫 (716.13) 全为零。$\square$

这里对新增亚纯积分只使用它们是一次积分，所以相关项长度至多三；没有把它们的上同调类误放进 $F^1$。

**推论 716.3。** 四个对应系数在函数空间

$$
 \mathcal V=\operatorname{span}_{\mathbb C_p}\mathscr B^{\rm raw}
$$

上定义了良定的线性泛函。对真实 $E_{ij}$，其值精确为

$$
 \boxed{
 -L_j^{-2},\quad L_g^{-2},\quad
 L_i^{-2},\quad -L_g^{-2}
 }
\tag{716.17}
$$

且均非零。

**证明。** 良定性正是引理 716.2。展开 (716.9) 中
$-U_i^{\rm raw}(A_2-A_3)+U_j^{\rm raw}(A_1-A_3)$ 即得四个值。$\square$

## 5. 有限代数关系矩阵与实际 jet 恒等式

设 $\mathscr B^{\rm raw}=(B_1,\ldots,B_{D_0})$。所有函数都由有限个代数微分在 $c_1$ 归零的长度至多四迭代积分组成。按 R699 §8 构造它们的公共非零代数微分算子 $\mathcal L$，并令

$$
 T=\{n\in\mathbb Z_{\ge0}:\mathcal P_{\mathcal L}(n)=0\},
 \qquad
 J_T=([z^n]B_\ell)_{n\in T,\,1\le\ell\le D_0}.
\tag{716.18}
$$

$T$ 有限，矩阵全在 $K$。R699 的首阶论证给

$$
 \boxed{\quad
 \ker_{\mathbb C_p}J_T
 =\{(c_\ell):\sum_\ell c_\ell B_\ell=0\}.
 \quad}
\tag{716.19}
$$

因为若矩阵核中的组合非零，其首阶必在 $T$，与 $T$ 中所有系数为零矛盾。反向显然。

因此可以通过有限的精确代数消元求出全部函数关系，并选取一组列基

$$
 \widetilde B_1,\ldots,\widetilde B_D,\qquad D\le D_0.
\tag{716.20}
$$

每个原 $B_\ell$ 都是这些基函数的 $K$ 线性组合：从 $J_T$ 的列关系得出组合后，(716.19) 保证它是完整级数恒等式，而不只是有限精度关系。引理 716.2 还说明四个顶层混合列必须包含在任何这样的列基中；若漏掉其中一列，其余列张成它将给一个被该引理禁止的关系。

选 $D$ 个行 $S\subset T$，使

$$
 J_S=([z^s]\widetilde B_\ell)_{s\in S,\ell}
\tag{716.21}
$$

可逆。设 $\ell_0$ 是其中 $U_i^{\rm raw}x_2^2$ 的列，令

$$
 (a_s)_{s\in S}=e_{\ell_0}^{\,t}J_S^{-1}\in K^S.
\tag{716.22}
$$

**定理 716.4（不含 $\gamma$ 的真实 jet 提取）。** 同一实际外积满足

$$
 \boxed{\quad
 \sum_{s\in S}a_s[z^s]E_{ij}=-\frac1{L_j^2}\ne0.
 \quad}
\tag{716.23}
$$

另三列给 (716.17) 的另三个值。特别

$$
 \min_{s:a_s\ne0}
 \bigl(v_p(a_s)+v_p([z^s]E_{ij})\bigr)
 \le-2v_p(L_j).
\tag{716.24}
$$

**证明。** 在列基中写 $E_{ij}=\sum c_\ell\widetilde B_\ell$。其四个顶层混合系数因引理 716.2 不因消去其他列而改变，故目标列系数是 $-L_j^{-2}$。把 $S$ 行 Taylor 系数左乘 (716.22) 即得恒等式，非阿基米德不等式给 (716.24)。$\square$

提取行只依赖实际代数曲率、第二类代表、$\mathcal R$ 的基及有限代数 jet。它不依赖任何具体极部修正 $\gamma_\nu$、规范高度值、全局第二类周期或 $Y$ 高度常数。

## 6. 同一免修正函数基上的完整相对尾

仍用 R699 的

$$
 w=z/\lambda^3,\qquad b_p=3p/(p+1).
$$

对全部 $\rho_a,\omega_{\nu b},\eta_{\nu b}$ 给出整形式盘上的代数下界

$$
 \rho=f_\rho(w)\,dw,\qquad
 v_p([w^n]f_\rho)\ge a_\rho\quad(n\ge0).
\tag{716.25}
$$

它们均仅在 $Q$ 有水平极点，且 $Q$ 避开该盘；R699 的清分母论证适用。此处没有 $\gamma_\nu$，故也不需其整性证书。

一次积分的下界为 $a_{\rho_a}-\lfloor\log_p n\rfloor$；令

$$
 u_\nu^{\rm raw}=\min_b(a_{\omega_{\nu b}}+a_{\eta_{\nu b}}),
\tag{716.26}
$$

则 $U_\nu^{\rm raw}$ 的下界为
$u_\nu^{\rm raw}-2\lfloor\log_p n\rfloor$。对表中每个单项式按出现次数相加这些权，得 $b_\ell$，并有

$$
 v_p([z^n]B_\ell)\ge
 b_\ell-b_pn-4\lfloor\log_p n\rfloor
 \qquad(n\ge1).
\tag{716.27}
$$

列基 (716.20) 直接由原列中选择，所以可直接沿用所选列的 $b_\ell$；不需要对消元后的未知高度系数另估分母。

对整数 $h_0\ge3$，令

$$
 f_n=p^{h_0n}[z^n]E_{ij},\quad
 M_{h_0}=(p^{h_0s}[z^s]\widetilde B_\ell)_{s\in S,\ell},
 \quad \delta_{h_0}=h_0-b_p>0,
$$
$$
 C_{h_0}
 =\min_{\ell,s}\{b_\ell+v_p((M_{h_0}^{-1})_{\ell s})\}.
\tag{716.28}
$$

R703 的矩阵恒等式现在逐字适用：对全部 $n$，

$$
 f_n=\sum_{s\in S}
 \left(\sum_\ell
 p^{h_0n}[z^n]\widetilde B_\ell
 (M_{h_0}^{-1})_{\ell s}\right)f_s.
\tag{716.29}
$$

故

$$
 \boxed{\quad
 v_p(f_n)\ge
 \min_{s\in S}v_p(f_s)+C_{h_0}
 +\delta_{h_0}n-4\lfloor\log_p n\rfloor.
 \quad}
\tag{716.30}
$$

右侧的前缀最小值有限，由 (716.23) 已知不全为零。所有其余常数完全代数，不含具体 $\gamma_\nu$ 或任何未知高度常数。

选择 $N_{h_0}=p^K>\max S$、$K\ge1$，使

$$
 C_{h_0}+\delta_{h_0}p^K-4K>0.
\tag{716.31}
$$

R703 的完整跳点下包络证明给所有 $n\ge N_{h_0}$ 的系数赋值严格大于前缀最小值。这样的 $K$ 一定存在。于是完整最大系数绝对值在 $n<N_{h_0}$ 达到，在 $v_p(z)\ge h_0$ 盘的零点总重数至多 $N_{h_0}-1$。若实际共同 Abel 首阶为 $m$，非零零点总重数至多 $N_{h_0}-m-2$。

这些结论来自 R703 已完整证明的矩阵相对尾和逐根除法；它们同时包含 $h_0=3$ 的边界与 $h_0=4$ 的原 R317 候选盘。

## 7. 增强的准确边界

相对于 R703，本篇从有限 jet 提取器及其相对尾的输入中删除了：

- 一个具体的代数极部修正 $\gamma_i,\gamma_j$；
- 这两个修正微分的单独整性常数；
- 全部第二类全局周期、规范高度常数及其赋值。

仍需原曲线的代数模型、真实商给出的曲率、代数第二类代表、已知有限极点空间的基及其整性证书。这些数据不能由把原 Abel 首项换名为高度首项得到。本文没有实际求出一般 $p$ 的矩阵行、首非零阶或首项赋值，也没有通过这个固定 $p$ 零点数界证明绝对 Serre 一致性。

实际有限前缀仍随规范常数改变。此处证明的是若干特定线性提取值和相对无限尾不受这些未知量影响，不是整个真实高度函数已经只由曲率唯一确定。

## 来源与使用范围

- A. Besser, J. S. Müller, P. Srinivasan，*p-adic adelic metrics and Quadratic Chabauty I*，arXiv:2112.03873v4，2026-01-16，<https://arxiv.org/html/2112.03873v4>。Theorem 3.15 给长度过滤、低长度消失及 shuffle；Lemma 7.10、Corollary 7.11 给 (716.16) 的注入；Lemma 7.12 的实际 NS 适用性由 R634 §6 核准。Identity principle 的一般光滑连通簇范围见 §3.1 和 Proposition 9.1 的证明。
- R634：同一实际规范外积及 NS 类独立性；R682：原 CM 对数分量非零及任意共同首阶；R699：代数曲率、单极点代表、同曲率全纯差、整盘及首阶算子；R703：有限代数 jet 关系的提取和相对全尾。
- R696/R317：原候选靶值 $\omega=\omega_0=0$ 与实际深盘。全部 R616 前提继续保留。
