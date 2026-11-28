# R1185：原 CM 点差的有效高度与实际半秩商成本

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 本文对 R1011、R1182 的同一个 $X_1,c_0,c_1,q_C,\beta$，去掉 Fuchs–Pham 输入中独立未知的 CM 点高度：构造仅依原 Belyi 覆盖次数的可计算整数函数，统一控制原分支纤维中每个点的稳定 Arakelov 高度，再通过原 Jacobian 主极化和实际商映射给出 $h(\beta')$ 的上界。

所得界保留实际商的极化比较证书、射影倍二公式及局部倍数 $M$。本文不给这些商模型成本关于 level $p$ 的统一小界，也不据此声称 R1182 的隔离半径已经覆盖某个固定深度盘。所有算法仅在纸面证明终止；本文未执行数学计算。

## 1. 原对象与结论

沿用 [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md) 和 [R1182](R1182-original-effective-Abel-jet-valuation-and-CM-disc-radius.md)：

$$
X=X_1=\operatorname{Norm}
 \bigl(X_{\rm ns}^+(p)\times_j\mathbf P^1_b\bigr),
\qquad j=6912b^3(1-b^3),\qquad g=g(X),
$$
$$
c_0:b=0,\qquad c_1:b=1,\qquad
D_0=(3-N)[c_1-c_0],\qquad N=1+\delta+\delta^2,
$$
$$
q_C:J_X\twoheadrightarrow C,\qquad q_CN=0,\qquad
\beta=q_C(D_0),\qquad \beta'=M\beta.
\tag{1185.1}
$$

这里 $c_0,c_1$ 仍由原同一 $\mu_6$-稳定 CM 项链指定；$q_C$ 是已经清除同源分母的原实际同态，$M$ 是 R1182 (1182.8) 的实际整数。原 Abel 映射 $f_C(x)=q_C[x-c_1]$ 满足精确恒等式

$$
\beta=3q_C[c_1-c_0]=-3f_C(c_0).
\tag{1185.2}
$$

取 $C$ 上一个在 $\mathbf Q$ 上定义的对称 ample 线丛 $\mathcal L$，使其完整线性系给出射影正规嵌入 $\iota:C\hookrightarrow\mathbf P^s$。记对应绝对对数射影高度为 $h_\iota$，对应二次规范高度为 $\widehat h_{\mathcal L}$。在 §6 说明如何从任意既有嵌入得到这一数据，以及如何保留原嵌入的高度。

**定理 1185.1。** 存在本文明确给出终止算法的绝对整数函数 $H_{\rm br}(D)$，以及从实际 $(J_X,C,q_C,\mathcal L)$ 的有限代数数据可取得的证书 $K\ge1,E_{\mathcal L}\ge0$，使

$$
D_p=3p(p-1),\qquad
h_{\rm Ar}(c_0),h_{\rm Ar}(c_1)\le H_{\rm br}(D_p),
\tag{1185.3}
$$
$$
\boxed{\quad
h_\iota(\beta')\le
18M^2K\frac{g}{g-1}H_{\rm br}(D_p)
+\frac{E_{\mathcal L}}3.
\quad}
\tag{1185.4}
$$

$K$ 的证书是指定线丛 $\Theta_0^{\otimes K}\otimes(q_C^*\mathcal L)^{-1}$ 的一个 very ample 幂及其闭嵌入；$E_{\mathcal L}$ 的证书是原 $[2]$ 的四次坐标公式及一个齐次 Nullstellensatz 恒等式。两者都可有限验证，不以“选择一个兼容极化”隐藏数值尺度。

## 2. 仅依 Belyi 次数的全部原分支点高度

### 2.1 一个可实际枚举的有限覆盖列表

固定整数 $D\ge2$。对任一几何连通 Belyi 覆盖

$$
x:Y\longrightarrow\mathbf P^1_{\overline{\mathbf Q}},\qquad
2\le n=\deg x\le D,\qquad g_Y\ge2,
\tag{1185.5}
$$

Riemann–Hurwitz 给 $g_Y\le D$。置

$$
\Lambda_D=\bigl(2(D+1)D^2\bigr)^{10D^2+12D},
\qquad A_D=2^{\Lambda_D}3^{\Lambda_D^2}.
\tag{1185.6}
$$

Bilu–Strambi，*Quantitative Riemann existence theorem over a number field*，Theorem 1.2，正式版第 320 页，应用于分支集合 $\{0,1,\infty\}$，给出保持原函数 $x$ 的平面模型

$$
F(x,y)=0,\qquad
\deg_XF=g_Y+1\le D+1,\quad \deg_YF=n\le D,
$$
$$
[L:\mathbf Q]\le\Lambda_D,\qquad
h_{\rm aff}(F)\le\Lambda_D.
\tag{1185.7}
$$

该文使用对数 affine 高度，且明定 $h(\infty)=0$。故每个系数 $\alpha$ 都满足 $\deg(\alpha)\le\Lambda_D$、$h(\alpha)\le\Lambda_D$。

这给一个不依赖实数高度比较的有限枚举。令 $\mathcal A_D$ 为所有次数不超过 $\Lambda_D$、整数系数绝对值不超过 $A_D$ 的非零多项式的全部代数根。这个集合有限且可用最小多项式及根的隔离数据枚举。它包含 (1185.7) 的全部系数：若 $P_\alpha\in\mathbf Z[T]$ 是本原最小多项式、次数为 $e$，其 Mahler 测度为 $\exp(eh(\alpha))$，于是每个系数满足

$$
|\operatorname{coeff}(P_\alpha)|
\le2^e\exp(eh(\alpha))
\le2^{\Lambda_D}\exp(\Lambda_D^2)<A_D.
\tag{1185.8}
$$

枚举所有以 $\mathcal A_D$ 为系数、$\deg_XF\le D+1$、$2\le\deg_YF\le D$ 的多项式，然后执行有限代数筛选：绝对不可约；光滑射影正规化的亏格至少二；$x$ 的次数不超过 $D$；正规化上的 $x$ 除 $0,1,\infty$ 外不分歧。最后一项使用函数域正规化及 different，或等价地逐有限分支计算局部 ramification index，包括无穷远；不能仅把未正规平面方程的判别式零点都认成真实分支点。上述步骤都是数域上多项式分解、正规化及有限线性代数的算法。

所得有限列表记为 $\mathcal F_D$。无需判定其中哪些模型相互同构，重复模型不影响后续最大值。也无需枚举某个几何曲线的全部 $\mathbf Q$-twists：Theorem 1.2 已保证每个 (1185.5) 都与列表中某个保持 $x$ 的模型同构。该同构可以取在 $\overline{\mathbf Q}$ 上；两个代数有限覆盖的覆盖同构组成有限型、零维的代数同构空间，一个复同构因而给一个代数同构。

### 2.2 将整个原分支纤维送到同一个有理非分歧值

对每个 $F\in\mathcal F_D$，令 $Y_F$ 为其光滑射影正规化，并取

$$
T_F=x^{-1}\{0,1,\infty\}_{\rm red}.
\tag{1185.9}
$$

这是在系数数域 $L_F$ 上 Galois 稳定的有限非空集合。Scherr–Zieve 的 separated Belyi 构造，在 $S=\varnothing,T=T_F$ 时不仅使 $T_F$ 避开新分支纤维；其 Theorem 1.1 的证明实际给出

$$
\varphi_F:Y_F\longrightarrow\mathbf P^1_{L_F},\qquad
\operatorname{Br}(\varphi_F)=\{0,1,\infty\},\qquad
\varphi_F(T_F)=\{a_F\},\quad
a_F\in\mathbf Q\setminus\{0,1\}.
\tag{1185.10}
$$

这里 $a_F$ 为有限值。原文的三步是：Proposition 2.1 取 $\varphi_1(T_F)=\{\infty\}$ 且 $\infty\notin\operatorname{Br}(\varphi_1)$；Proposition 3.2 取 $\varphi_2\in\mathbf Q(X)$，把当前分支集合送入 $\mathbf P^1(\mathbf Q)$，并使 $\beta_F=\varphi_2(\infty)\in\mathbf P^1(\mathbf Q)$ 避开该集合；Proposition 3.3 取 $\varphi_3\in\mathbf Q(X)$，把新分支集合送入 $\{0,1,\infty\}$，同时 $\varphi_3(\beta_F)\notin\{0,1,\infty\}$。因此 $\varphi_F=\varphi_3\varphi_2\varphi_1$ 确实把全部 $T_F$ 送到同一个 $a_F$，包括原来位于 $x=0$ 的两个指定点。

这个构造有效：第一步的 Riemann–Roch 空间可由数域上的有限线性代数求出；需要的 generic 选择可枚举有理系数并检验有限坏条件。后两步的多项式、分式及避开有限整数集合的素数均由原证明构造。也可以枚举 $L_F(Y_F)$ 中的有理函数并检验 (1185.10)；存在定理保证这一搜索终止。这里使用的只是 separated Belyi 定理及其构造，不使用同文中的猜想性 Diophantine 后果。

最后以保持 $\{0,1,\infty\}$ 的六个分式线性变换之一复合，可使

$$
0<a_F\le\frac12<\frac23.
\tag{1185.11}
$$

这不改变覆盖次数或“全部 $T_F$ 取同一值”的性质。

### 2.3 可计算整数函数

写 $d_F=\deg\varphi_F$、$g_F=g(Y_F)$。若 $a_F=A_F/B_F$ 为既约分数、$B_F>0$，取一个由整数位数直接得到的整数 $b_F\ge h_{\rm naive}(a_F)=\log\max(|A_F|,B_F)$；例如取 $1+$ 该最大整数的二进制位数。定义

$$
H_F=3b_Fd_F^2+
\left\lceil\frac{6378031d_F^5}{g_F}\right\rceil,
\qquad
H_{\rm br}(D)=\max\bigl(\{1\}\cup\{H_F:F\in\mathcal F_D\}\bigr).
\tag{1185.12}
$$

有限枚举以及对其中每一项的终止搜索证明 $H_{\rm br}$ 是绝对可计算的整数函数；不声称该算法实际可行，也不声称 $H_{\rm br}$ 多项式增长。

Javanpeykar，*Polynomial bounds for Arakelov invariants of Belyi curves*，Theorem 4.5.1，正式版第 120 页，给出：对任意 Belyi 覆盖 $\varphi:Y\to\mathbf P^1$、$0<a\le2/3$ 的有理数以及**每个** $P\in\varphi^{-1}(a)$，

$$
h_{\rm Ar}(P)\le
3h_{\rm naive}(a)(\deg\varphi)^2
+\frac{6378031(\deg\varphi)^5}{g(Y)}.
\tag{1185.13}
$$

故 $h_{\rm Ar}(P)\le H_F$ 对全部 $P\in T_F$ 成立。稳定 Arakelov 高度在有限数域扩张及 $\overline{\mathbf Q}$-同构下不变：其定义使用半稳定最小正则模型上的 Arakelov 度并除以底域次数，两个同构对象可在共同有限扩张上比较。因此得到

$$
\boxed{\quad
\deg x\le D\quad\Longrightarrow\quad
h_{\rm Ar}(P)\le H_{\rm br}(D)
\quad\text{对每个 }P\in x^{-1}\{0,1,\infty\}.
\quad}
\tag{1185.14}
$$

这一步没有以“存在一个小点”代替原 CM 点；也没有把几何有限性误当作对无限多个有理 twists 的朴素模型高度界。

## 3. 对原 $X_1,c_0,c_1$ 的应用

原函数

$$
x=\frac j{1728}=4b^3(1-b^3)
\tag{1185.15}
$$

是 $X_1$ 上的 Belyi 函数。事实上，原 $X_{\rm ns}^+(p)\to\mathbf P^1_j$ 仅在 $j=0,1728,\infty$ 分歧；$b\mapsto4b^3(1-b^3)$ 是次数六的 Belyi 映射。两者的纤维积在这三值之外有限 étale，正规化后的指定原连通分支仍如此。

原模曲线 $j$ 映射的次数为 $p(p-1)/2$，所以即使不假设纤维积次数相乘取等号，仍有

$$
\deg(x:X_1\to\mathbf P^1)\le
6\cdot\frac{p(p-1)}2=D_p.
\tag{1185.16}
$$

$x(c_0)=x(c_1)=0$。在 R1011 的范围，$g\ge\dim C\ge2$。于是 (1185.14) 直接给 (1185.3)。若需要完全只用 $p$ 的系数，可用 $g/(g-1)\le2$；本文保留较准确的原 $g$。

## 4. Arakelov 高度与 Jacobian 主极化的准确系数

本篇 $h_{\rm Ar}(P)$ 的规范是：在使 $X,P$ 半稳定且有定义的有限数域 $L$ 上，若 $\mathcal X$ 是最小正则模型、$\overline\omega$ 为带 Arakelov 度量的相对对偶化层，则

$$
h_{\rm Ar}(P)=
\frac{(\overline\omega,\overline P)}{[L:\mathbf Q]}.
\tag{1185.17}
$$

这与 Javanpeykar 上述定理 §2.3 以及 Javanpeykar–von Känel，*Szpiro's Small Points Conjecture for Cyclic Covers*，§2 (4) 的规范相同。

令 $\widehat h_J$ 是原 Jacobian 主极化的二次 Néron–Tate 高度。Javanpeykar–von Känel 在其 (5) 定义

$$
h_{\rm NT}(P)=\widehat h_J((2g-2)[P]-K_X),
\tag{1185.18}
$$

其 Lemma 4.4(i)，正式版第 1093 页，适用于任意亏格至少二的曲线，不要求曲线是该文后节讨论的循环覆盖，给出

$$
h_{\rm NT}(P)\le2g(g-1)h_{\rm Ar}(P).
\tag{1185.19}
$$

该证明中的式 $2h_{\rm NT}(P)=-e(X)+4g(g-1)h_{\rm Ar}(P)+(\Phi,\Phi)/[L:\mathbf Q]$ 固定了这里主极化高度的二分之一规范，不能再额外乘二。

置 $v_i=(2g-2)[c_i]-K_X$。由二次高度的平行四边形恒等式及非负性，

$$
(2g-2)^2\widehat h_J([c_1-c_0])
=\widehat h_J(v_1-v_0)
\le2\widehat h_J(v_1)+2\widehat h_J(v_0).
$$

故

$$
\boxed{\quad
\widehat h_J([c_1-c_0])
\le\frac g{g-1}\bigl(h_{\rm Ar}(c_0)+h_{\rm Ar}(c_1)\bigr)
\le\frac{2g}{g-1}H_{\rm br}(D_p).
\quad}
\tag{1185.20}
$$

原 $\delta$ 是曲线自同构，在 Jacobian 上保持主极化。因而 $N^\dagger=N$、$N^2=3N$，$1-N/3$ 是高度内积的正交投影。这也给出同一个原点差的界

$$
\widehat h_J(D_0)
=9\widehat h_J\bigl((1-N/3)[c_1-c_0]\bigr)
\le9\widehat h_J([c_1-c_0]).
\tag{1185.21}
$$

这里在 $J(\overline{\mathbf Q})\otimes\mathbf Q$ 上取二次型；不需要 $\delta$ 本身在 $\mathbf Q$ 上定义。

## 5. 原商映射的有限极化比较证书

用原有理点 $c_1$，把 $W_{g-1}\subset\operatorname{Pic}^{g-1}(X)$ 平移到 $J_X$，得到在 $\mathbf Q$ 上定义的 theta 线丛 $\Theta_0$。其 Néron–Severi 类给原主极化。$\Theta_0$ 不必对称，也不假设存在有理 theta characteristic；其二次规范高度仍是上述 $\widehat h_J$。

因为 $\Theta_0$ ample，对足够大整数 $K$，线丛

$$
\mathcal A_K=
\Theta_0^{\otimes K}\otimes(q_C^*\mathcal L)^{-1}
\tag{1185.22}
$$

ample。所需的 $K$ 可以通过有限证书取得，而不调用一个未知的 Néron–Severi 锥算法：同时枚举正整数 $K,r$ 及 $H^0(J_X,\mathcal A_K^{\otimes r})$ 的有理全局截面，检验这些截面无共同零点并给出闭嵌入。截面、线丛同构及嵌入均以有限 affine cover 上的多项式数据表示；闭嵌入可由图像的齐次理想及各坐标开集上的环映射检验。ample 的定义保证某一对 $(K,r)$ 有这样的证书，所以穷举终止。它保留原 $q_C$ 的全部整数尺度。

任一 ample 线丛的二次规范高度非负；对于非对称 $\mathcal A_K$，可通过 $\mathcal A_K\otimes[-1]^*\mathcal A_K$ 的对称化看出。高度的张量可加性及同态函子性于是给

$$
0\le\widehat h_{\mathcal A_K}^{\rm quad}(P)
=K\widehat h_J(P)-\widehat h_{\mathcal L}(q_CP),
\qquad P\in J_X(\overline{\mathbf Q}).
\tag{1185.23}
$$

用 (1185.2)、(1185.20) 得

$$
\widehat h_{\mathcal L}(\beta')
=9M^2\widehat h_{\mathcal L}(q_C[c_1-c_0])
\le18M^2K\frac g{g-1}H_{\rm br}(D_p).
\tag{1185.24}
$$

等价地，也可先用 (1185.21) 再应用 (1185.23)；两种算法给同一个系数，不能重复计入两个因子九。

## 6. 射影高度与倍二误差的有限证书

### 6.1 选择嵌入时不改变原点或原商

对任意既有射影嵌入 $\iota_0:C\hookrightarrow\mathbf P^{s_0}$，记 $\mathcal L_0=\iota_0^*\mathcal O(1)$。可取

$$
\mathcal L=
\bigl(\mathcal L_0\otimes[-1]^*\mathcal L_0\bigr)^{\otimes3}.
\tag{1185.25}
$$

这是有理对称 ample 线丛，且在特征零其完整线性系射影正规。这里可以直接消费 Sekiguchi，*On projective normality of abelian varieties*，Theorem 2.3，第 321 页：对 ample $L$，$H^0(L^a)\otimes H^0(L^b)\to H^0(L^{a+b})$ 在 $a\ge2,b\ge3$ 时满射；取 $a=3,b=3m$ 归纳即得 $L^3$ 正规生成。very ampleness 也可直接由原 very ample $\mathcal L_0$ 的 Segre 乘积及其三次幂得到。

这只更换 $C$ 的坐标，不更换 $C,q_C,c_i,\beta$。若在 R1182 中采用新嵌入，则其 Fuchs–Pham 模型常数、向量场分母及 chart 仍须按这个嵌入选取，不能无说明沿用旧数值。

若坚持保留原 $\iota_0$，也有明确比较。原 $\iota_0(P),\iota_0(-P)$ 的三次 Segre–Veronese 坐标是 $H^0(C,\mathcal L)$ 完整基的有理线性组合。记该实际矩阵的高度误差上界为 $c_T\ge0$，则

$$
3\bigl(h_{\iota_0}(P)+h_{\iota_0}(-P)\bigr)
\le h_\iota(P)+c_T,
\qquad
h_{\iota_0}(P)\le\frac{h_\iota(P)+c_T}{3}.
\tag{1185.26}
$$

$c_T$ 可由矩阵各处的系数范数直接给出；这里用了普通射影高度非负。因而下文的界也可转换回原 FP 嵌入，不强迫重新选模型。

### 6.2 四次公式与上下界

对称性给 $[2]^*\mathcal L\simeq\mathcal L^{\otimes4}$。由射影正规性，原倍二映射的坐标可表示为有理系数齐次四次式

$$
[2]P=[F_0(x):\cdots:F_s(x)],\qquad
F_i\in\mathbf Q[X_0,\ldots,X_s]_4,
\tag{1185.27}
$$

且 $F_i$ 在 $\iota(C)$ 无共同零点。取其齐次理想的有限生成元 $Q_\ell$。齐次 Nullstellensatz 给某个整数 $v\ge4$ 及有理齐次多项式 $G_{ji},H_{j\ell}$，使每个 $j$ 满足

$$
X_j^v=\sum_iG_{ji}F_i+\sum_\ell H_{j\ell}Q_\ell,
\qquad \deg G_{ji}=v-4.
\tag{1185.28}
$$

可以用有理 Gröbner 消元取得，亦可枚举 $v$ 后解线性方程；无共同零点保证终止。这是所需下界的有限可验证证书。

在有限地方 $w$，令 $A_w$ 为 $1$ 与所有 $F_i$ 的系数绝对值的最大值，$B_w$ 为 $1$ 与所有 $G_{ji}$ 的系数绝对值的最大值。在无穷处，若 $\|P\|_1$ 是多项式系数绝对值总和，准确取 $A_\infty=\max\{1,\max_i\|F_i\|_1\}$、$B_\infty=\max\{1,\max_j\sum_i\|G_{ji}\|_1\}$，将 Nullstellensatz 的全部求和计入。由 (1185.27)–(1185.28)，对 $x\in\iota(C)$ 有

$$
B_w^{-1}\|x\|_w^4
\le\|F(x)\|_w\le A_w\|x\|_w^4.
\tag{1185.29}
$$

除有限多个有理素数外，$A_w=B_w=1$。取一个可计算有理数或整数 $E_{\mathcal L}$，大于等于 $\sum_w\log A_w$ 和 $\sum_w\log B_w$；全部系数在 $\mathbf Q$ 上，扩域后按绝对高度权重求和给同一常数。因此

$$
\bigl|h_\iota([2]P)-4h_\iota(P)\bigr|\le E_{\mathcal L}
\quad\text{对全部 }P\in C(\overline{\mathbf Q}).
\tag{1185.30}
$$

取 $\widehat h_{\mathcal L}(P)=\lim_{r\to\infty}4^{-r}h_\iota([2]^rP)$，逐次相减并求几何级数，得到准确常数

$$
\bigl|h_\iota(P)-\widehat h_{\mathcal L}(P)\bigr|
\le E_{\mathcal L}\sum_{r\ge0}4^{-r-1}
=\frac{E_{\mathcal L}}3.
\tag{1185.31}
$$

结合 (1185.24) 即证 (1185.4)。这个 $1/3$ 来自倍二的高度倍率四，不把它替换为未经定义的高度比较常数。

## 7. 代入原 R1182 的准确范围

若 R1182 的 FP 射影嵌入已取为上面的 $\iota$，其原参数 $\mathsf h=\log\max\{3,H_\iota(\beta')\}$（$H_\iota=\exp h_\iota$）可在估值界中用以下明确上界替换：

$$
\mathsf h_* =\max\left\{\log3,
18M^2K\frac g{g-1}H_{\rm br}(3p(p-1))
+\frac{E_{\mathcal L}}3\right\}.
\tag{1185.32}
$$

若保留原嵌入 $\iota_0$，则用 (1185.26) 给

$$
h_{\iota_0}(\beta')\le
\frac13\left(
18M^2K\frac g{g-1}H_{\rm br}(3p(p-1))
+\frac{E_{\mathcal L}}3+c_T\right).
\tag{1185.33}
$$

由此，原 $\beta=-3f_C(c_0)$ 的点高度不再是独立未知量，而由 level 次数和实际商坐标证书控制。仍须保留：原商模型及其 invariant-derivation 常数、$\ell_m=\Omega(-,U_m)$ 的有理系数高度、Néron 基变换、原同态尺度和进入形式指数 chart 的倍数 $M$。本文没有界定这些量随 $p$ 的增长，也没有把任何有限第一层 Cartan 标记提升为任意高层。

已成的 [R1184](R1184-original-uniform-cubic-CM-disc-and-Neron-integrality.md) 将原指定分支的 Néron 整 chart 固定为 $t=b-1=p^3w$。与它合用时，R1182 的 $U_m$、$\ell_m$ 的系数高度、首项估值上界 $B$ 及本原首项估值 $e_m$ 都须在这一实际参数中重算，不能保留旧 $a$ 的 jet 高度数值。本文的点高度界与参数无关；即使 $a=3$ 固定，首项估值界仍有上述明确保留的模型依赖。

## 8. 原始文献与实际消费位置

1. Y. F. Bilu–M. Strambi, **Quantitative Riemann existence theorem over a number field**, *Acta Arithmetica* **145** (2010), 319–339，Theorem 1.2，第 320 页；消费保持原覆盖函数的次数、系数高度和定义域次数界。DOI [10.4064/aa145-4-2](https://doi.org/10.4064/aa145-4-2)；[正式全文](https://www.impan.pl/shop/publication/transaction/download/product/82405)。
2. Z. Scherr–M. E. Zieve, **Separated Belyi maps**, *Mathematical Research Letters* **21** (2014), 1389–1406；消费 Theorem 1.1 及 Proposition 2.1、3.2、3.3 的完整构造。[作者全文](https://websites.umich.edu/~zieve/papers/mochizuki.pdf)，2013-10-25 版本 PDF 第 9–10 页的证明逐步给出 $\varphi(T)=\{a\}$、$a\in\mathbf Q\setminus\{0,1\}$；不是只引用标题中的“分离”。
3. A. Javanpeykar, **Polynomial bounds for Arakelov invariants of Belyi curves**, with an appendix by P. Bruin, *Algebra & Number Theory* **8** (2014), 89–140，§2.3 及 Theorem 4.5.1，第 120 页；消费指定有理纤维中每个点的高度界，未用 Theorem 4.5.2 的小点存在性替换原点。DOI [10.2140/ant.2014.8.89](https://doi.org/10.2140/ant.2014.8.89)；[正式全文](https://msp.org/ant/2014/8-1/ant-v8-n1-p04-s.pdf)。
4. A. Javanpeykar–R. von Känel, **Szpiro's Small Points Conjecture for Cyclic Covers**, *Documenta Mathematica* **19** (2014), 1085–1103，§2 (4)–(5)，第 1088–1089 页；Lemma 4.4(i)，第 1093 页。[正式全文](https://ems.press/content/serial-article-files/26254)。消费部分对一般曲线无循环覆盖前提。
5. T. Sekiguchi, **On projective normality of abelian varieties**, *Journal of the Mathematical Society of Japan* **28** (1976), 307–322，Theorem 2.3，第 321 页。DOI [10.2969/jmsj/02820307](https://doi.org/10.2969/jmsj/02820307)；[正式全文](https://www.jstage.jst.go.jp/article/jmath1948/28/2/28_2_307/_pdf/-char/ja)。只在特征零消费 ample 三次幂的正规生成。

以上五个实际输入均已亲读对应定理与证明段。所有高度归约和倍数系数由本文逐式推出；没有执行枚举、假设 GRH，或使用未验证的模型高度常数。
