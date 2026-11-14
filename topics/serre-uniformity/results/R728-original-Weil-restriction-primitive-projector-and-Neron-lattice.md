# R728：原正 CM 全族的显式 Weil restriction、本原投影与 p 处 Néron 格

日期：2026-11-14。状态：**本文的模型、分解、有限阶自同态、本原投影和 Néron 格公式已证明。** 原曲线到此模型的具体有理函数以及原点差的坐标仍未生成；本文不声称已算出高度首项。

沿用 R725 的原标记，不另选 CM 扭向。记
$$
n=p+1,\qquad m=n/6,\qquad
K=\mathbb Q(\sqrt{-3}),\quad
L^+=\mathbb Q(b),\quad L=L^+K,\quad C:y^2=x^3+b.
\tag{728.1}
$$
其中 $p\ge41$、$p\equiv2,5\pmod9$，$b=r_0^6$ 是 R725 的两个原 $p$-挠点乘积之差的六次幂。特别地，$F_p(T)\in\mathbb Q[T]$ 是 $b$ 的次数 $m$ 的最小多项式，并且在 $p$ 处 Eisenstein。

本篇将单个椭圆分量提升为实际 $\mathbb Q$-阿贝尔簇模型，并给出切出原本原因子的具体自同态。

## 1. 由有限方程给出的有理模型

定义
$$
B=\operatorname{Res}_{L^+/\mathbb Q} C.
\tag{728.2}
$$
这是维数 $m$ 的阿贝尔簇。其一个稠密仿射开集的方程完全明确：令
$$
X(T)=\sum_{i=0}^{m-1}x_iT^i,\qquad
Y(T)=\sum_{i=0}^{m-1}y_iT^i,
$$
将
$$
Y(T)^2-X(T)^3-T
\tag{728.3}
$$
除以 $F_p(T)$，令余式的全部 $m$ 个系数等于零。加法由同一商代数 $\mathbb Q[T]/(F_p)$ 中的椭圆加法给出；完整阿贝尔簇是上述 Weil restriction，不是任意奇异射影闭包。

因为 $L^+\cap K=\mathbb Q$，
$$
B_K=\operatorname{Res}_{L/K} C,\qquad
B_L=\prod_{\tau\in\operatorname{Gal}(L/K)}{}^\tau C.
\tag{728.4}
$$
后式只在 $L$ 上使用，未把通常非 Galois 的 $L^+/\mathbb Q$ 当作循环扩张。标准椭圆极化的外积在所有共轭间相容，下降为 $B$ 的一个 $\mathbb Q$-定义主极化 $\lambda_B$；取相应原点刚性化对称线丛 $\Theta_B$。

## 2. 所有正 μ6 标签逐项出现

R725 给有限角色
$$
\varepsilon=\theta\rho_p\cdot\kappa_4,\qquad
\psi=\psi_0\varepsilon,
\tag{728.5}
$$
以及循环扩张 $H/K$，满足 $[H:K]=n$、$[H:L]=6$，且 $C$ 的正 CM 角色为 $\psi|_{G_L}$。$\psi_0$ 是固定 $E_{27}:Y^2=X^3+16$ 的 primary 角色，$\theta$ 是原指定本原角色。记
$$
\mathcal A=\{a\bmod n:a\equiv1\pmod6\},\qquad
\psi_a=\psi_0\varepsilon^a.
\tag{728.6}
$$
对这些 $a$，$\kappa_4^a=\kappa_4$，故
$$
\psi_a=\Psi_{\theta^a}\kappa_4,\qquad
\theta^a(\zeta)=\zeta^{-1},\quad\theta^a(s)=-1.
\tag{728.7}
$$
因此它们正是同一六水平正标签的 $m$ 个角色，没有引入相反 $\kappa_4^{-1}$。

在包含全部系数的辅助 $\ell$-进域中，Weil restriction 的 Tate 模为诱导表示。其正 CM 部分准确分解为
$$
\begin{aligned}
\operatorname{Ind}_{G_L}^{G_K}(\psi|_{G_L})
&=\psi\otimes\operatorname{Ind}_{G_L}^{G_K}\mathbf1\\
&=\bigoplus_{a\in\mathcal A}\psi_a .
\end{aligned}
\tag{728.8}
$$
因为 $\operatorname{Gal}(L/K)$ 的全部角色是 $\varepsilon^{6j}$，$0\le j<m$。负 CM 部分为上述各项的复共轭；它们逐项不同，正负部分也不同，因为无穷型不同。

每个 $\theta^a$ 的阶大于二：$a\equiv1\pmod6$ 使其阶保留 $n$ 的完整二次幂部分和三因子。因此在 $p$ 处仍是非平凡惰性角色，而且 $\theta^a\ne(\theta^a)^p$；其 automorphic induction 为 cuspidal。原六水平局部标记只用 (728.7)，故 R575 的出现性同样适用于每一项，水平仍为 $108p^2$。

按有理 Galois 轨道合并，得到
$$
B\sim_{\mathbb Q}
\prod_{\substack{d\mid n\\v_2(d)=v_2(n),\ v_3(d)=1}} A_d,
\qquad \dim A_d=\varphi(d)/2.
\tag{728.9}
$$
$A_d$ 是阶为 $d$ 的上述正角色的有理同源类，每类一次。固定有限角色在 $\mu_6$ 上的原限制后，阶为 $d$ 的角色由固定 $K$ 的圆分 Galois 群传递置换，共 $\varphi(d)/2$ 项。全体恰有 $m$ 项。其系数域也不是仅凭维数指定：对阶 $d$ 的角色，primary 生成元的 CRT 让有限部分遍历 $\mu_d$，故 Hecke 值生成的 $K$-域为 $K(\mu_d)=\mathbb Q(\zeta_d)$；中央角色平凡，取复共轭固定域即得全实系数域 $\mathbb Q(\zeta_d+\zeta_d^{-1})$。

(728.8) 已识别实际 Galois 表示，(728.9) 使用 Tate 模的同源判据，不凭维数猜同源。特别地，
$$
A_n\sim_{\mathbb Q}A_{\theta,1}.
\tag{728.10}
$$
若 $n$ 只含素因子 $2,3$，则 (728.9) 只有 $d=n$，$B$ 本身就是原本原因子的一个显式同源模型；不宣称此条件覆盖全部素数。

## 3. 真实的有限阶移位自同态

取 $g\in\operatorname{Gal}(H/K)$ 的生成元，令
$$
\sigma=g|_L,\qquad
r=r_0/\sqrt[3]4,\qquad
\rho=g(r)/r,\qquad
\eta=g^m(r)/r.
\tag{728.11}
$$
R725 给 $r^6=b/16$，且 $h(r)=\varepsilon(h)^{-1}r$ 对全部 $h\in\operatorname{Gal}(H/L)$ 成立。因此
$$
\rho\in L^\times,\qquad
\rho^6=\sigma(b)/b,\qquad
N_{L/K}\rho=\eta=\varepsilon(g^m)^{-1}\in\mu_6,
\tag{728.12}
$$
其中 $\eta$ 的阶恰为六。第一式来自交换性：$\operatorname{Gal}(H/L)$ 在 $g(r)$ 和 $r$ 上的因子相同。

写 $D_u(x,y)=(u^2x,u^3y)$，方向由源和靶的常数项确定。通过 (728.4) 的分量表示，定义
$$
(T(P))_\tau
  =D_{\tau(\rho)^{-1}}(P_{\tau\sigma}),
\qquad P_\tau\in{}^\tau C.
\tag{728.13}
$$
因 $\tau(\rho)^6=\tau\sigma(b)/\tau(b)$，每项确为 $\,{}^{\tau\sigma}C\to{}^\tau C$ 的同构。循环公式与 $\operatorname{Gal}(L/K)$ 的下降作用相容，故 $T\in\operatorname{Aut}_K(B_K)$。它是给出坐标比例的真实自同态。

正 CM 约定中，单位 $u$ 的乘法为 $[u]=D_{u^{-1}}$。遍历一个循环给
$$
\boxed{T^m=[\eta],\qquad T^n=1.}
\tag{728.14}
$$
若 $T^k=1$，分量置换先迫使 $m\mid k$，再由 $\eta$ 的六阶得到 $6m\mid k$，所以 $T$ 的阶恰为 $n$。

可用 R725 的 $p$-惯性生成元作 $g$，因为 $H/K$ 在 $p$ 完全分歧而 $\kappa_4$ 在 $p$ 平凡。此时 $\rho=g(r_0)/r_0$，全部比例由原 $p$-挠点有限乘积给出，无需另解未知六次根。

R725 的实选择使复共轭 $c$ 固定 $r$，且 $cgc=g^{-1}$。所以
$$
c(\rho)=g^{-1}(\rho^{-1}),\qquad
\boxed{cTc=T^{-1}.}
\tag{728.15}
$$
后一式可逐分量代入 (728.13) 验证。每个分量映射保持椭圆原点和标准主极化，因而
$$
T^\dagger=T^{-1}
\tag{728.16}
$$
其中 $\dagger$ 为 $\lambda_B$ 的 Rosati 对合。

## 4. 自同态代数与可计算的 Hodge 矩阵

通过 $H^0(B_K,\Omega^1)\simeq L\,\omega_C$ 的 trace 识别，
$$
\boxed{T^*(f\omega_C)=\sigma^{-1}(\rho f)\omega_C.}
\tag{728.17}
$$
将 $f\omega_C$ 写成各分量的 $\sum_\tau\tau(f)\omega_{{}^\tau C}$，(728.13) 使第 $\tau$ 项拉回为 $\tau(f\rho)\omega_{{}^{\tau\sigma}C}$；重新编号即得公式。

其特征多项式为 $U^m-\eta$：在分量基中是带非零权的长度 $m$ 循环，权乘积为 $\eta$。负 CM 特征多项式为 $U^m-\bar\eta$，故有理 Tate 空间上的多项式为
$$
(U^m-\eta)(U^m-\bar\eta)=U^{2m}-U^m+1.
\tag{728.18}
$$
各根不同。又 (728.8) 的全部 $G_K$-特征互异，Tate 同态定理给中心化子维数恰为 $2m$。因此
$$
\operatorname{End}_K^0(B_K)=\mathbb Q[T]
 \simeq\mathbb Q[U]/(U^{2m}-U^m+1).
\tag{728.19}
$$
$K$ 已通过 $T^m=[\eta]$ 包含于右侧。

置 $S=T+T^{-1}$，它在 $\mathbb Q$ 上定义。令
$$
D_0(Z)=2,\quad D_1(Z)=Z,\quad
D_{j+1}(Z)=ZD_j(Z)-D_{j-1}(Z).
$$
由 $D_m(S)=T^m+T^{-m}=1$，
$$
\boxed{
\operatorname{End}_{\mathbb Q}^0(B)
 =\mathbb Q[S]\simeq\mathbb Q[Z]/(D_m(Z)-1).
}
\tag{728.20}
$$
该多项式的 $m$ 个根互异，对应 (728.18) 的互逆根对。(728.15) 在整个 (728.19) 上给有理下降，故右侧就是全部固定代数。

将 $\sigma(b)$、$\rho$ 表示在 $1,b,\ldots,b^{m-1}$ 中，(728.17) 给完整 $m\times m$ Hodge 矩阵，系数仅用 R725 的除法多项式和域运算，不含未知高度。

## 5. 原本原因子的显式有理投影

令 $c_n(j)$ 为 Ramanujan 和，完全用整数公式
$$
c_n(j)=\sum_{d\mid(n,j)}d\mu(n/d)
$$
计算。定义
$$
\boxed{
e_n=\frac1n\sum_{j=0}^{n-1}c_n(j)T^j,\qquad E_n=ne_n.
}
\tag{728.21}
$$
在任一 $T$-特征根 $\xi$ 上，其特征值为一当且仅当 $\xi$ 阶为 $n$，否则为零。这由有限循环群正交关系直接给出。因而
$$
e_n^2=e_n,\quad E_n^2=nE_n,\quad e_n^\dagger=e_n.
\tag{728.22}
$$
又 $c_n(-j)=c_n(j)$，所以 $E_n\in\operatorname{End}_{\mathbb Q}(B)$。

令
$$
A^{\mathrm{mod}}=E_n(B),\qquad
B^{\mathrm{rem}}=(n-E_n)(B).
\tag{728.23}
$$
这两个有理阿贝尔子簇由具体自同态的像给出，并且
$$
A^{\mathrm{mod}}\sim_{\mathbb Q}A_{\theta,1},\qquad
\dim A^{\mathrm{mod}}=\varphi(n)/2.
\tag{728.24}
$$
为核对投影标签，在 $H$ 上以缩放 $g^i(r)$ 把第 $i$ 个分量识别到固定 $E_{27}$。在此循环基中，$T$ 的相邻项为一，绕回项为 $[\eta]$；$g$ 的正 CM Galois 作用除去共同的 $\psi_0(g)$ 后恰为逆循环矩阵 $T^{-1}$。因此 (728.8) 中 $\psi_a$ 对应的 $T$-根准确为 $\varepsilon^a(g)^{-1}$，其阶为 $\operatorname{ord}(\varepsilon^a)$。这也固定了同一个原 $g$，不需改变 CM 标签。阶为 $n$ 的根恰对应 $(a,n)=1$ 的原正轨道。

加法同源
$$
\iota:A^{\mathrm{mod}}\times B^{\mathrm{rem}}\longrightarrow B
\tag{728.25}
$$
的核被 $n$ 杀掉：交集上的 $E_n$ 同时等于 $n$ 和零；而
$E_n+(n-E_n)=n$ 保证满射。因此
$$
p\nmid\deg\iota.
\tag{728.26}
$$
此结论来自具体投影，不来自任意 CM 同源的存在性。

## 6. 真实 p 处 Néron 余切格中的逆 different

设 $F=\mathbb Q_p$、$F'=\mathbb Q_p(b)$。R725 给
$$
[F':F]=m,\quad \mathcal O_{F'}=\mathbb Z_p[b],\quad
\mathfrak D_{F'/F}=(F_p'(b)),\quad
v_{F'}(\mathfrak D)=m-1.
\tag{728.27}
$$
扩张完全温和分歧。$C/F'$ 的 $y^2=x^3+b$ 为类型 II 最小模型，
$\omega_C=dx/(2y)$ 为真实 Néron 微分。

令 $\mathcal C/\mathcal O_{F'}$ 为其 Néron 模型。
$\operatorname{Res}_{\mathcal O_{F'}/\mathbb Z_p}\mathcal C$ 是 $B_F$ 的 Néron 模型。直接核映射性质：对任意光滑 $\mathbb Z_p$-scheme $Z$，其在 $\mathcal O_{F'}$ 上的基变换仍光滑，泛纤维映射经 $\mathcal C$ 唯一延拓；Weil restriction 本身光滑。椭圆 Néron 模型的准射影性保证此 restriction 可表出。这是 BLR §7.6 构造在本例的应用。

于是 $\operatorname{Lie}(\mathcal B)\simeq\mathcal O_{F'}$，而其 $\mathbb Z_p$-对偶必须通过 trace 配对识别：
$$
\boxed{
\omega_{\mathcal B}
 =\mathfrak D_{F'/F}^{-1}\omega_C
 =F_p'(b)^{-1}\mathbb Z_p[b]\,\omega_C.
}
\tag{728.28}
$$
$f\omega_C$ 作用于切向量 $v\in\mathcal O_{F'}$ 的值为
$\operatorname{Tr}_{F'/F}(fv)$。所以 $\mathcal O_{F'}\omega_C$ 通常不是此 trace 识别下完整的 Néron 余切格。

一组明确的格基为
$$
\left\{\frac{b^j}{F_p'(b)}\omega_C:0\le j<m\right\}.
\tag{728.29}
$$
它是整个逆 different 的基，不宣称逐项等于 $1,b,\ldots,b^{m-1}$ 的 trace 对偶基。

因为 $p\nmid n$，(728.21) 在 $\omega_{\mathcal B}$ 上为整 idempotent。
(728.25) 的素于 $p$ 次数同源在 Néron Lie 格上为同构：一个核被 $n$ 杀掉的同源有反向同源，两个合成均为 $[n]$，在 $\mathbb Z_p$ 微分上均可逆。因此
$$
\boxed{\omega_{\mathcal A^{\mathrm{mod}}}=e_n^*\omega_{\mathcal B}}
\tag{728.30}
$$
是在此识别下的真实直接和格。联用 (728.17)、(728.21)、(728.29) 给本原因子的完整格矩阵。

这只比较显式 $A^{\mathrm{mod}}$ 和 $B$。尚未证明原
$J_{X_1}\to A_{\theta,1}\to A^{\mathrm{mod}}$ 的微分格指数素于 $p$；KS/Manin 比例仍须沿那一条实际同态计算。

## 7. 显式极化与 NS 线丛代表

令 $\lambda_A$ 为 $\lambda_B$ 在 $A^{\mathrm{mod}}$ 上的限制。
$e_n$ 对 Rosati 自伴，使 (728.25) 两分量正交，因而
$$
\iota^*\lambda_B=\lambda_A\times\lambda_{\mathrm{rem}},
\qquad p\nmid\deg\lambda_A.
\tag{728.31}
$$
后式由 $\lambda_B$ 主极化和 $p\nmid\deg\iota$ 得到。

$S$ 保持本原分量，限制后生成
$$
\operatorname{End}_{\mathbb Q}^0(A^{\mathrm{mod}})
 =\mathbb Q(\zeta_n+\zeta_n^{-1}).
\tag{728.32}
$$
Rosati 在此全实域上恒等。通过 $\lambda_A$ 的对称同态识别，
$\operatorname{NS}(A^{\mathrm{mod}})_{\mathbb Q}$ 的维数也是
$g=\varphi(n)/2$。

可直接给出有理定义的线丛，而不只列抽象 NS 元素。写
$S_j=T^j+T^{-j}=D_j(S)$；这些都是 $\mathbb Q$-定义的整自同态。令
$$
\mathscr D_j=(1+S_j)^*\Theta_B\otimes(S_j^*\Theta_B)^{-1}
                                      \otimes\Theta_B^{-1}.
\tag{728.33}
$$
极化的二次公式给
$$
\lambda_{\mathscr D_j}=2\lambda_B S_j.
\tag{728.34}
$$
所以 $\Theta_B|_{A^{\mathrm{mod}}}$ 及
$\mathscr D_j|_{A^{\mathrm{mod}}}$，$1\le j<g$，
给该模型 NS 空间的一组有理基。$D_j$ 首一、次数 $j$，使这些类与
$1,S,\ldots,S^{g-1}$ 三角换基。线丛已由明确外积和拉回给出，适合生成 Poincaré 纤维及曲率数据。

它们仍不是 R593 原 $X_1$ 上指定的完整张量。
原 Picard 零次修正、截面、$\mu_3$ Norm、局部刚性化须经原商映射运输，不能因 NS 维数相同而删除。

## 8. 原 q 与 β 的准确剩余接口

Weil restriction 的伴随性为
$$
\operatorname{Hom}_{\mathbb Q}(J_{X_1},B)
 \simeq\operatorname{Hom}_{L^+}((J_{X_1})_{L^+},C).
\tag{728.35}
$$
因此，若生成以 $c_0$ 为原点的实际映射
$$
f:(X_1)_{L^+}\longrightarrow C,\qquad f(c_0)=O,
\tag{728.36}
$$
其 Jacobian 同态经 (728.35) 给 $Q_f:J_{X_1}\to B$，且
$$
Q_f[c_1-c_0]\longleftrightarrow f(c_1)\in C(L^+).
\tag{728.37}
$$
原本原点差的模型坐标为 $E_nQ_f[c_1-c_0]$，其投影已是
(728.13)、(728.21) 的有限群运算，不再留一个抽象 idempotent。

但 (728.36) 本身还未生成。待核的有理函数对必须满足
$$
y_f^2=x_f^3+b,\qquad f(c_0)=O,\qquad
f^*\omega_C=\frac{dx_f}{2y_f},
\tag{728.38}
$$
且其 Hodge 分量须与 R575 原六水平 Cartan 向量相符。标准
$\Gamma_1(108p^2)$ 归一 Fourier 系数或 CM 同源类相同，都不直接给出此比较比例。

若投影后同态非零，原本原因子的简单性保证其满射到 $A^{\mathrm{mod}}$；
与指定 $q_1$ 比较仍须记录实际同源和同一微分的准确常数。R724 的全部线丛、联络、分裂与非 $p$ 局部项随后沿这个比较运输。

本文给出原目标阿贝尔同源类的有限方程、全部原角色分解、具体本原投影、真实 Néron 格及极化/NS 代表。没有代入任意第三类微分，没有宣称已算出原 $\beta$ 坐标或高度外积首项。R726 的充分大 $p$ 非挠及 rank/log 结论可用于后续计算，但不能补出 (728.36) 的有理函数。

## 来源与依赖

- [R725](R725-original-CM-elliptic-model-and-splitting-field.md)：实际域、原正角色、非零 $r_0,b$、$F_p$ 和最小椭圆模型。
- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)、[R616](R616-original-CM-point-difference-and-explicit-height-basis.md)：实际正 CM 出现性、原六水平标签与指定点差。
- [R724](R724-original-Chow-Heegner-height-matrices-and-canonical-jet-evaluation.md)：原高度规范及必须保留的运输数据。
- J. González, J.-C. Lario, *Modular elliptic directions with complex multiplication*, Comment. Math. Helv. 86 (2011), 317–351，Theorems 1.1–1.3；<https://arxiv.org/pdf/0810.4224>。本文的有限阶自同态和投影直接由公式构造，未套该文不同 CM 域的特殊例子。
- S. Bosch, W. Lütkebohmert, M. Raynaud, *Néron Models* (1990), §7.6；Weil restriction 的可表性、光滑性与映射性质。相同基础性质可核 B. W. Jordan, K. A. Ribet, A. J. Scholl, *Modular curves and Néron models of generalized Jacobians*, Compositio Math. 160 (2024), 945–981, §1.1，<https://doi.org/10.1112/S0010437X23007662>。本例的 Néron 映射性质与 trace-dual 格推导已写于 §6。
