# R634：同一有理 CM 点校准消去真实商的全部高度矩阵

日期：2026-11-14。状态：**在 R616 明列的实际本原非消失前提内已证明。** 本文给出不含未知 $A$-高度矩阵的有限组真实局部高度方程，证明每个方程在每个局部盘上非恒零，并给出同一 $c_1$ 参数的一、二阶系数公式。没有证明这些首项是 $p$ 单位，没有计算固定 $Y$-线性高度或有限目标集的数值，也没有据此声称绝对 Serre 一致性已经解决。

本证明直接延续已发布 R593、R596、R616 的同一规范。

## 1. 原曲线、实际商、同一个 CM 点

固定 $p\geq41$、$p\equiv5\pmod6$，设 $N=p+1$，取 R575 确认的正 CM 甲板方向及 R616 的本原角色 $\theta_{-1}$。以下假定

$$
 L'(g_{-1,+},1)L(g_{-1,-},1)\ne0,
 \qquad
 g_{-1,\pm}=\operatorname{AI}_{K/\mathbb Q}
                   (\Psi\theta_{-1}\kappa_4^{\pm1}),
 \quad K=\mathbb Q(\sqrt{-3}).
 \tag{634.1}
$$

这是 R616 已给出多种充分区域的同一前提；$g_{-1,-}$ 只在该篇真实 CM 点的 Gross–Zagier 因子化中使用，不把它改称 $Z_p$ 的原实际商。这里不声称 (634.1) 已对全部惰性素数成立。

沿用 R593、R597：

$$
 X=X_1=Z_p,\qquad \phi:X\longrightarrow Y=W_p,
 \qquad v=a^3,\qquad j=6912v(1-v),
$$
$$
 q:J_X\longrightarrow A=A_{-1,1},\qquad
 \iota(x)=[x-c_0],\qquad j_A(x)=q\iota(x).
 \tag{634.2}
$$

$c_0$ 是 $a=0$ 上的指定有理 CM 点；$c_1$ 是 $a=1$ 上、同一个 $\mu_6$ 保持的 CM 项链所给的有理点。取

$$
 \beta=j_A(c_1)=q[c_1-c_0]\in A(\mathbb Q).
 \tag{634.3}
$$

R616 在 (634.1) 下证明

$$
 F=\operatorname{End}_{\mathbb Q}^0(A)
    =\mathbb Q(\mu_N)^+,\qquad g=[F:\mathbb Q]=\dim A,
$$
$$
 A(\mathbb Q)\otimes\mathbb Q=F\beta,
 \qquad
 \log_p:A(\mathbb Q)\otimes\mathbb Q_p
                \xrightarrow{\sim}\operatorname{Lie}(A)(\mathbb Q_p).
 \tag{634.4}
$$

特别 $\beta$ 非挠，且 $A$ 在 $\mathbb Q$ 上单。所有下文的对数和 Abel 积分来自这个真实 $A$，不是另一个三次扭曲，也不把另一覆盖的 $c_0$ 积分搬到当前 $c_1$。

因为 $p\equiv-1\pmod N$，$p$ 在 $F$ 完全分裂。写

$$
 \mathcal F=F\otimes\mathbb Q_p\simeq\mathbb Q_p^g.
 \tag{634.5}
$$

下文的外积空间维数必须至少二。这里确有 $g\geq3$：若 $\varphi(n)\leq4$，则 $n\in\{1,2,3,4,5,6,8,10,12\}$，而 $N\geq42$。故

$$r=g-1\geq2.\tag{634.6}$$

这不是对任意低维商的结论；若 $g\leq2$，本文下面的两坐标外积不能给所需方程。

## 2. 实际极化、修正线丛及原高度符号

固定 R593 的甲板不变 $\mathbb Q$ 极化 $\lambda$，以及

$$
 q^\dagger=\lambda_{J_X}^{-1}q^\vee\lambda,
 \qquad\kappa=qq^\dagger\in F^{\times}.
 \tag{634.7}
$$

$\kappa$ 全正。真实次数零空间与其对偶为

$$
 F^0=\{h\in F:\operatorname{Tr}_{F/\mathbb Q}(\kappa h)=0\},
 \qquad
 \mathcal W=\mathcal F/\mathbb Q_p\kappa
       \simeq(F^0\otimes\mathbb Q_p)^*,
 \tag{634.8}
$$

其中对偶配对为 $([u],h)\mapsto\operatorname{Tr}(hu)$。不删去 $\kappa$ 而误用普通迹零空间。

对 $h\in F^0$，R593 的真实线丛是

$$
 \mathscr L_h=q^*\mathcal L_h\otimes
                       \phi_*^*\lambda_Y(\eta_h),
 \quad \lambda_{\mathcal L_h}=\lambda h,
 \quad \iota^*\mathscr L_h=0
          \text{ 于 }\operatorname{Pic}(X)\otimes\mathbb Q.
 \tag{634.9}
$$

使用该篇的 $c_{\rm clear},c_{\rm triv}$、真实无零截面以及 $s_h(c_0)=1$ 的归一；全部全局及局部高度除回同一个因子。取 $F^0$ 的一个有理基，先为这有限个基向量选共同倍数与这些归一截面，再用张量积和有理倍数定义一般 $h$。所以所有局部、全局函数对 $h$ 线性。R596 的 $\eta_h$ 和 $\ell_h$ 也按同一个线性选择构造。

设

$$
 P(x)=\log_p\phi_*[x-c_0]\in\operatorname{Lie}(J_Y)(\mathbb Q_p).
$$

R593 (593R.28)、R596 (596.24) 与 R616 的原符号为

$$
 \rho_h(x)=Q_h(\log_pj_A(x))+2\ell_h(P(x))
                          -\lambda_{p,h}(x)\in\Omega_h
       \qquad(x\in X(\mathbb Q)).
 \tag{634.10}
$$

此处 $h_Y$ 是 theta 高度极化所得配对，Poincaré 配对为它的两倍。本文保持 (634.10) 的正号及因子二；不会在不改有限目标集的情况下反转 $\rho_h$。

## 3. 改成 $F$ 相容 splitting，真实 $\rho$ 和有限目标不变

为了利用实乘，将 $A$ 部分的 $p$ 处 splitting 取成 $F$ 相容。这里有这样的选择，不需要任何普通约化或单位根假设。

$H^1_{\rm dR}(A/\mathbb Q_p)$ 是秩二的 $\mathcal F$-模，Hodge 子模是秩一。$F$ 上的 Rosati 为恒等，极化配对是一个 $\mathcal F$-双线性交替配对取迹。对 (634.5) 的每个二维分量选一条与 Hodge 线互补的线，得到 $F$ 稳定的 Lagrangian 补空间。由这个补空间构造规范 Poincaré splitting，得到对称且 $F$ 相容的高度 $b_\lambda^F$。

比较的起点是 R593 (593R.16)、(593R.26) 已按 $q^*\mathcal L_h$ 与 $\phi_*^*\lambda_Y(\eta_h)$ 两因子规范度量作张量所定义的同一度量；$Q_h$ 本来就是 $A$ 上的高度。保持 $J_Y$ 的 splitting、全局 idèle 角色 $\chi$、原点刚性化及全部 $p$ 外项不变。R593 的 $q\phi^*=0$、$\phi_*q^\dagger=0$ 使 $A$ 与 $J_Y$ 在 $J_X$ 的同源分解中正交。因此可在 $J_X$ 上取实现这两个因子度量的正交积 splitting，在其余因子任取补空间；下面全部线丛使用由此得到的同一个 purely mixed Poincaré curvature。随后只改变 $A$ 因子的 splitting，$Y$ 及其余因子保持。这里不从一个带有任意跨 $A$ 项的 $J_X$ splitting 起步，也不主张下面仅含 $\operatorname{Lie}(A)$ 的比较式已覆盖那种未指定的选择。

比较的是同一个 Poincaré 双扩张上的两个 canonical $\chi$-splittings。其差下降为基底上的连续双加性函数。局部群的有限商不贡献到无挠目标 $\mathbb Q_p$，通过对数可写成双线性形式

$$
 B:\operatorname{Lie}(A)\times\operatorname{Lie}(A^\vee)
                                      \longrightarrow\mathbb Q_p.
$$

对称线丛的平方是沿 $x\mapsto(x,\lambda h(x))$ 的 Poincaré 拉回；原点刚性化消除常数。因此令

$$
 \Delta_h(u)=\tfrac12 B(u,(\lambda h)_*u),
 \tag{634.11}
$$

就有下列同一规范的精确等式：

$$
 Q_h^F(u)-Q_h(u)=\Delta_h(u),
$$
$$
 \lambda_{p,h}^F(x)-\lambda_{p,h}(x)
                         =\Delta_h(\log_pj_A(x)).
 \tag{634.12}
$$

第二式对所有 $p$ 进点成立，因为它直接比较同一线丛、同一实际截面上的两个 log functions；没有只在有理点上推断后再任意延拓。Picard 零次的 $Y$ 修正不变。

于是

$$
 Q_h^F(\log_pj_A(x))+2\ell_h(P(x))
                -\lambda_{p,h}^F(x)=\rho_h(x)
 \tag{634.13}
$$

作为真实局部函数恒等成立。所有 $p$ 外项也没有改变，故使用的是原来的 $\Omega_h$。此处的规范 splitting、函子性与同一双扩张上的比较采用 Besser–Müller–Srinivasan 的 Proposition 4.30 及 §6；具体的相消由 (634.11)–(634.13) 给出。

## 4. 一个 $\mathcal F$ 元素控制所有 $A$-高度矩阵

$F$ 相容的 splitting 与 Rosati 自伴性给

$$
 b_\lambda^F(ax,y)=b_\lambda^F(x,ay)
                \quad(a\in F),
 \qquad Q_h^F(x)=b_\lambda^F(x,hx).
 \tag{634.14}
$$

在 $p$ 外这是规范高度的函子性；在 $p$ 处是所选 $F$ 稳定 splitting 的函子性。它们给全局等式，继而通过 (634.4) 延拓到实际对数空间。

由非退化迹配对，存在唯一 $\mathcal C\in\mathcal F$，使

$$
 \operatorname{Tr}(h\mathcal C)=b_\lambda^F(\beta,h\beta)
                         \quad(h\in\mathcal F).
 \tag{634.15}
$$

由 (634.4)，存在唯一局部解析/Vologodsky 函数 $t:X(\mathbb Q_p)\to\mathcal F$，满足

$$
 \log_pj_A(x)=t(x)\log_p\beta,
 \qquad t(c_0)=0,\quad t(c_1)=1.
 \tag{634.16}
$$

这里 $\mathcal F\log_p\beta\to\operatorname{Lie}(A)$ 为同构。对有理 $x$，$j_A(x)=t(x)\beta$ 于 $A(\mathbb Q)\otimes\mathbb Q$ 且 $t(x)\in F$。由 (634.14)，

$$
 Q_h^F(\log_pj_A(x))=\operatorname{Tr}(h\mathcal C t(x)^2)
                      \qquad(x\in X(\mathbb Q_p)).
 \tag{634.17}
$$

因此原来一族未知矩阵全部包含于同一个 $\mathcal F$ 元素 $\mathcal C$；不需要假定这个高度非退化或 $\mathcal C$ 的任何分量是单位。

定义对 $h$ 线性的局部函数

$$
 \Lambda_h(x)=\lambda_{p,h}^F(x)-2\ell_h(P(x)),
 \qquad\Lambda(x)\in\mathcal W.
 \tag{634.18}
$$

必须同时而非逐坐标定义有限目标。对 $q=2,3$，把同一个局部点处所有 $h$ 的归一化 $\mathbb Q$-valuation 合成向量 $\lambda_q(x_q)\in\mathcal W$，令

$$
 \Omega=\left\{\chi_2(2)\lambda_2(x_2)
                    +\chi_3(3)\lambda_3(x_3):
             x_2\in X(\mathbb Q_2),\ x_3\in X(\mathbb Q_3)\right\}.
 \tag{634.19}
$$

R593 和 BMS Lemma 7.1 保证它有限；其它 $q\ne p$ 的项为零。它保留各坐标来自同一个局部点的相关性。若只掌握各坐标的有限集合，可以改用其笛卡尔积作为一个明确较大的充分目标集；不能称这个乘积等于 (634.19)。本文没有计算 (634.19) 的数值。

于是准确的向量高度关系是

$$
 [\mathcal C t(x)^2]-\Lambda(x)=\omega(x)\in\Omega
                        \qquad(x\in X(\mathbb Q)).
 \tag{634.20}
$$

由于 $c_1$ 本身有理，令 $\omega_0=\omega(c_1)$，则

$$
 [\mathcal C]=\Lambda(c_1)+\omega_0.
 \tag{634.21}
$$

这个校准使用同一个真实点及同一个 $\Omega$。若 $\omega_0$ 尚未计算，应让它遍历全 $\Omega$；不能因为待排除候选属于某个偶局部分支，就擅自把 $c_1$ 的目标也限制到该分支。

## 5. 显式外积消元：不再含 $\mathcal C$ 或任何高度矩阵

写 $\kappa=(\kappa_1,\ldots,\kappa_g)$。所有 $\kappa_i\ne0$。固定同构

$$
 \pi:\mathcal W\xrightarrow{\sim}\mathbb Q_p^r,
 \qquad
 \pi([u])_i=u_i/\kappa_i-u_g/\kappa_g
                      \quad(1\leq i\leq r).
 \tag{634.22}
$$

其对偶基是第 $i$ 分量 $1/\kappa_i$、第 $g$ 分量 $-1/\kappa_g$、其余分量零的 $h^{(i)}\in F^0\otimes\mathbb Q_p$，确实满足加权迹条件。这些 $p$ 进基向量仅是第 2 节有理基的线性组合；没有声称它们各自定义一个 $\mathbb Q$ 线丛。

对每对有限目标 $(\omega,\omega_0)\in\Omega^2$，定义

$$
 d_i=\Lambda_i(c_1)+(\omega_0)_i,
 \qquad V_i(x)=t_i(x)^2-t_g(x)^2,
$$
$$
 W_i(x)=d_i t_i(x)^2-\Lambda_i(x)-\omega_i,
 \tag{634.23}
$$
$$
 \boxed{\mathcal E_{ij}^{\omega,\omega_0}(x)
               =W_i(x)V_j(x)-W_j(x)V_i(x)}
             \qquad(1\leq i<j\leq r).
 \tag{634.24}
$$

**定理 634.1（CM 校准消元）。** 在 (634.1) 下，每个 $x\in X(\mathbb Q)$ 对其 $\omega=\omega(x)$ 及同一个真实 $\omega_0=\omega(c_1)$ 满足全部方程

$$\mathcal E_{ij}^{\omega,\omega_0}(x)=0.\tag{634.25}$$

式 (634.24) 不含 $\mathcal C$、任何 $A$-高度矩阵或其未定公共标量。

证明。设 $\gamma_i=\mathcal C_i/\kappa_i$。由 (634.21)，$\gamma_i-\gamma_g=d_i$。由 (634.20)，

$$
 (\gamma_g+d_i)t_i(x)^2-\gamma_gt_g(x)^2
                             -\Lambda_i(x)=\omega_i,
$$

即 $W_i(x)=-\gamma_gV_i(x)$，所以所有二阶行列式为零。整个推导没有除以 $V_i$；即使在 $c_1$ 等 $V$ 为零的点也成立。$\square$

无坐标写法也有助于固定归一。任取 $C_0\in\mathcal F$，使 $[C_0]=\Lambda(c_1)+\omega_0$。则 (634.25) 等价于

$$
 \left([C_0(t^2-1)]-(\Lambda(x)-\Lambda(c_1))
                            -(\omega-\omega_0)\right)
                  \wedge[\kappa(t^2-1)]=0
       \quad\text{于 }\bigwedge^2\mathcal W.
 \tag{634.26}
$$

若把 $C_0$ 换成 $C_0+c\kappa$，第一因子只增加第二因子的 $c$ 倍，故外积不变。有限目标平移没有被遗漏。

## 6. 同一真实局部函数在每个盘上非恒零

仅凭抽象二步商的中心维数，不能推出某个指定局部高度函数非零。这里直接核对 BMS Theorem 7.9 对 (634.24) 的适用条件。

**引理 634.2。** 第 2 节的 $r$ 个有理基线丛 $\mathscr L_h$ 的 NS 类线性独立，位于

$$\ker\bigl(\iota^*:\operatorname{NS}(J_X)\otimes\mathbb Q
                         \to\operatorname{NS}(X)\otimes\mathbb Q\bigr).$$

证明。其 Picard 零次修正不改变 Chern 类，故 NS 类为 $q^*[\mathcal L_h]$。有理同态 $s=q^\dagger\kappa^{-1}$ 满足 $qs=1$，从而 $s^*q^*=1$，所以 $q^*$ 在 NS 的有理张量上单射。$h\mapsto[\mathcal L_h]$ 是 $F\simeq\operatorname{NS}(A)\otimes\mathbb Q$ 的同构。次数由 $\operatorname{Tr}(\kappa h)=0$ 消去，且 R593 已给真实拉回平凡及无零截面。$\square$

将这些类扩充到整个 NS 核的一个有理基。对新添类，利用 Abel autoduality 的 $\operatorname{Pic}^0(J_X)\simeq\operatorname{Pic}^0(X)$ 修正，使曲线拉回平凡，再清分母、按同一基点归一。全部线丛使用第 3 节同一个 purely mixed curvature。

BMS v4 的 Theorem 7.9（printed p.51；完整证明 pp.51–53）说明：一组全纯 Abel 积分和这些真正平凡化线丛的规范局部高度函数，没有非零的多项式关系。其 Lemma 7.12 的关键是 $D_2$ 局部高度在全纯积分二次张量模去后的独立性：它映到独立的有理 Chern 类模 $F^2H^2_{\rm dR}$。因此 Picard 零次修正不会破坏这个独立性。本应用不需要整个 $J_X$ 的秩等于其维数。

$t_i$ 是 $q$ 拉回的 $g$ 个线性独立全纯积分的可逆线性变换；可把它们扩充到 $X$ 的全部全纯积分。用 (634.18) 将各局部高度减去 $2\ell_h(P)$，只是对这些变量作可逆的三角线性变换。换到 (634.22) 的 $\mathbb Q_p$ 基同样可逆。因此这些全纯积分与 $\Lambda_1,\ldots,\Lambda_r$ 仍无非零多项式关系。

首先，每个 $V_i=t_i^2-t_g^2$ 是非零函数。可直接用上述独立性；也可用 $d(t_i-t_g)\ne0$，以及 $t_i(c_1)+t_g(c_1)=2\ne0$。

现在把 (634.24) 看作全纯积分和形式变量 $\Lambda_1,\ldots,\Lambda_r$ 的多项式。所有 $d_i$、$\omega_i$ 是固定的 $\mathbb Q_p$ 常数，包括 $\Lambda_i(c_1)$ 这种取值，不是随 $x$ 变化的额外变量。形式偏导为

$$
 \frac{\partial\mathcal E_{ij}}{\partial\Lambda_i}=-V_j,
 \qquad
 \frac{\partial\mathcal E_{ij}}{\partial\Lambda_j}=V_i.
 \tag{634.27}
$$

由于相应的形式多项式 $V_i,V_j$ 非零，$\mathcal E_{ij}$ 是非零多项式。BMS Theorem 7.9 遂给：

**定理 634.3（逐目标、逐盘非恒零）。** 对每个 $(\omega,\omega_0)\in\Omega^2$ 和每个 $1\leq i<j\leq r$，(634.24) 是非零 Vologodsky 函数，并且不在任何局部盘上恒为零。

最后一句使用该定理证明开头的 identity principle：若一个 Vologodsky 函数在一个点的邻域恒零，则其全局恒零。这里作用于已经固定实际曲率、截面和 splitting 的同一个函数，不是通过任意中心平移改变函数后再比较。

因为真实拉回截面无零无极，函数在整个 $X(\mathbb Q_p)$ 局部解析。$X$ proper，$X(\mathbb Q_p)$ 紧；非恒零解析函数的零点在每个小闭盘内有限，结合有限覆盖可得总零点有限。因此任意固定一对 $i<j$ 已给

$$
 X(\mathbb Q)\subseteq
 \bigcup_{(\omega,\omega_0)\in\Omega^2}
 \{x\in X(\mathbb Q_p):\mathcal E_{ij}^{\omega,\omega_0}(x)=0\},
 \tag{634.28}
$$

右侧为有限集。使用全部 $i<j$ 的交能进一步缩小这个必要集合。此处没有给出该集合中的点数或点的列表，也没有将其有限性升级为对所有 $p$ 的统一排除。

## 7. 原 $c_1$ 参数下的准确前两阶

在指定 $c_1$，$j$ 在非分裂 Cartan 粗模 CM 点的零阶为一，且 $j'(a)|_{a=1}=-20736\ne0$。所以

$$z=a-1\tag{634.29}$$

是这个有理点的 $\mathbb Q$ 局部参数。写

$$
 t_i=1+A_i z+B_i z^2+O(z^3),\qquad
 \Lambda_i=\Lambda_i(c_1)+L_i z+M_i z^2+O(z^3),
$$
$$\delta_i=(\omega_0)_i-\omega_i.\tag{634.30}$$

令 $V_i=v_{i,1}z+v_{i,2}z^2+O(z^3)$、$W_i=\delta_i+w_{i,1}z+w_{i,2}z^2+O(z^3)$。直接展开同一 (634.23)，得到

$$
 v_{i,1}=2(A_i-A_g),\qquad
 v_{i,2}=2(B_i-B_g)+A_i^2-A_g^2,
$$
$$
 w_{i,1}=2d_iA_i-L_i,\qquad
 w_{i,2}=d_i(2B_i+A_i^2)-M_i,
 \tag{634.31}
$$
$$
 [z]\mathcal E_{ij}=\delta_iv_{j,1}-\delta_jv_{i,1},
 \tag{634.32}
$$
$$
 [z^2]\mathcal E_{ij}=\delta_iv_{j,2}-\delta_jv_{i,2}
                         +w_{i,1}v_{j,1}-w_{j,1}v_{i,1}.
 \tag{634.33}
$$

在同一目标分支 $\omega=\omega_0$，一次项为零，二次候选首项是 (634.33) 后两项。本文不声称这个二次项非零，更不声称它是单位；定理 634.3 只保证某个有限阶非零。

$A_i$ 是同一实际 Abel 微分在 $c_1$ 的值除以同一 $\log_p\beta$ 分量。R571/R578/R605 的实际微分 jet 只有在明确匹配微分、周期及系数域基后才能代入；不能把另一点的 $M_0$ 或反向扭曲有限和直接作为这里的 $A_i$。同样 $L_i,M_i$ 含真实修正线丛的局部高度与固定 $\ell_h$，不是单独的 Abel 积分系数。

## 8. 外积第二因子的真正首阶：不会因 CM 对数比例而丢失

尽管尚未控制 (634.33)，可对向量 $V$ 给一个精确的定性首阶结论。写同一有理映射在 $c_1$ 的形式对数

$$
 \log_pj_A(c_1+z)=\log_p\beta+u_mz^m+O(z^{m+1}),
 \qquad u_m\ne0,
 \tag{634.34}
$$

其中 $m\geq1$ 是第一个非零阶。它有限，因为 $q\iota$ 非常值：否则 $\iota(X)$ 生成 Jacobian 会迫使 $q=0$。在 $\mathbb Q$-定义的 Lie 基下，$u_m\in\operatorname{Lie}(A)(\mathbb Q)$；这是 $\mathbb Q$-定义的局部映射 $j_A-\beta$ 的特征零形式群对数系数。

写 $t=1+T_mz^m+O(z^{m+1})$，则 $T_m\log_p\beta=u_m$，而

$$
 [\kappa(t^2-1)]=2[\kappa T_m]z^m+O(z^{m+1}).
 \tag{634.35}
$$

**引理 634.4。** $[\kappa T_m]\ne0$；因此 $V$ 的首非零阶恰为 $m$。

证明。若 $[\kappa T_m]=0$，由 (634.8) 得 $T_m=c\in\mathbb Q_p$。因 $u_m\ne0$，$c\ne0$，于是

$$\log_p\beta=c^{-1}u_m\in(\mathbb Q u_m)\otimes\mathbb Q_p.$$

这是一条真代数直线。对非挠代数点 $\beta$ 应用 Fuchs–Pham 的 $p$ 进解析子群定理（Theorem 2.2），得到正维代数子群，其 Lie 代数包含于该直线且含 $\beta$（或先取进入相应连通分支的非零倍数）。因 $\beta$ 有理，所有 Galois 共轭子群都含它。该子群在某个数域定义，只有有限多个共轭；取交、再取连通分支，仍含 $\beta$ 的一个非挠倍数，故正维，在 $\mathbb Q$ 上定义，并且维数至多一。它是 $A$ 的真 $\mathbb Q$-阿贝尔子簇，与 $g\geq3$ 和 $\mathbb Q$-单性矛盾。$\square$

这个引理没有证明 $m=1$，也没有给 $u_m$、$\log_p\beta$ 或 $[\kappa T_m]$ 的 $p$ 赋值。R317 的原候选满足 $v_p(a-1)\geq4$；若改写 $z=p^3w$，第 $n$ 项精确乘上 $p^{3n}$。没有统一的系数下界时，不能因此直接丢弃全部高阶项。

## 9. 仍需计算的真实输入与应用边界

(634.24) 已消去 $b_\lambda^F(\beta_i,\beta_j)$、全部 $A$-高度矩阵以及共同标量。保留下来的输入是：同一实际商的 Abel 积分；明确几何点 $\beta=q[c_1-c_0]$ 的对数；同一真实修正线丛和截面的局部函数 $\lambda_{p,h}^F$；R596 的固定 $Y$-线性高度 $\ell_h$；同一有限目标集合 $\Omega$。

这些输入中没有未知的 Mordell–Weil 生成元选择，但不等于已经算出全部高度。尤其本文不把 $\ell_h$ 当零，不声称已计算 $\Omega$。可用实际 CM 对数的非零分量清除 (634.16) 的分母而不改变零点集合；有限精度所需的除法损失仍取决于它们的真实赋值。

结论只在 (634.1) 以及 R616 已证明的充分区域中适用。它没有把固定 $p$ 的有限集合变成所有 $p$ 的统一界，也没有给原 $X_1$ 与变化 $X_d$ 之间的高度运输。后续要排除原候选，仍须对 (634.32)–(634.33) 或更高真实系数、有限目标的距离及完整尾部给出可用控制。

## 文献及准确使用位置

1. Amnon Besser, J. Steffen Müller, Padmavathi Srinivasan, *p-adic adelic metrics and Quadratic Chabauty I*, arXiv:2112.03873, v4（2026-01-16），<https://arxiv.org/pdf/2112.03873>。Proposition 4.30 及 §6 给规范 Poincaré log/高度；Lemma 7.1 给真实平凡化的有限坏处取值；Theorem 7.9（printed p.51）及 Lemma 7.12、完整证明（printed pp.52–53）给本文实际多项式函数的代数独立性与逐盘 identity principle。本文不以 Remark 7.14 的抽象密度讨论代替指定函数的非零证明。
2. Clemens Fuchs, Duc Hiep Pham, *The p-adic analytic subgroup theorem revisited*, arXiv:1502.00768（2015），<https://arxiv.org/pdf/1502.00768>，Theorem 2.2（printed p.2）。本文第 8 节使用它后另给有理点的 Galois 交下降论证。
3. 本仓库 R593（真实修正线丛、清分母、截面、$\Omega$ 和正确 $\rho$ 符号）、R596（同一固定 $\eta_h$ 的对数线性化）、R597（原 $v=a^3$ 与两覆盖分离）、R616（同一真实 CM 点非挠、$F\beta$ 生成、实际对数同构及充分区域）。未采用任何未恢复旧稿的数值或哈希。
