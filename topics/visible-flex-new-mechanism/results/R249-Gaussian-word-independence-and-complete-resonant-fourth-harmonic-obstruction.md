# R249：Gaussian 二重词的真实独立性与共振端芽的完整第四谐波障碍

日期：2026-11-15。**已证明，完整纸面结论。** 没有执行新的 profile 积分、符号目标、函数秩、参数求根或几何研究计算。

本稿隔离的是整个第四 ruling 的一个真实 Gaussian 面积原函数系数，不是另一条渐近必要层。在共振例外端芽上，它给出新的必要条件
$\int_I(q'')^4=0$。该条件严格排除 R239 的已构造双完整 block 圆，即使其 R231、R237 和 R241 的六个已识别能量条件全部为零。

本稿不排除所有三矩圆，也不排除所有可实现的共同 germ。普通复四次方没有普遍正性；本稿的严格符号只用于所述微包构造。

来源：[R56 原分子恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R71(12) 三次交换子](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R73 点态八矩与完整链式项](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R224 偶部 gauge 商](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)、[R231 中心化与真实能量](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、[R239 完整不可分离圆](R239-nonseparable-third-order-circles-paying-four-exceptional-energy-gates.md)、[R241 共振六能量](R241-complete-sigma-four-layer-and-resonant-exceptional-germs.md)、[R245 完整 Gaussian history 归约](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)和 [R248 完整第四谐波](R248-complete-fourth-harmonics-and-complementary-block-reduction.md)。

## 1. 端芽、原函数与结论

固定

$$
\kappa=k_e\ne0,\qquad h_e>0,\qquad
\varepsilon=\frac{\kappa^2}{4}>0,\qquad
H(\sigma)=e^{\varepsilon\sigma^2},
$$

$$
h=h_eH,\qquad
k=\kappa(1-2\varepsilon\sigma^2),\qquad
\omega=\frac{\kappa}{h}.
\tag{1}
$$

保持原共同物理区间 $I=[\ell,r]$、右零 collar 及物理支条件。定义

$$
j=2\varepsilon\kappa\sigma^2,\qquad
v=2\varepsilon\sigma.
$$

于是 $d=h\omega-k=j$，共振关系准确为

$$
v^2=\frac{\kappa j}{2}.
\tag{2}
$$

取真实三矩圆 $(f,g)$，令 $q=f+ig$。所有 profile 乘积及本稿的四次积分都是普通复乘法，J 是原正右积分。记

$$
\tau_q=-\frac13J((q'')^3),
$$

$$
M_4(q)=\int_I(q'')^4,\qquad
M_2^*(q,\tau_q)
=\int_I\{x^2q''\tau_q''+2q'\tau_q'\}.
\tag{3}
$$

这些是同一全区间上的真实数值，等价于共同左零 collar 的真实累计尾值，不是对每个 x 都成立的局部零身份。

**定理。** 若固定圆在具有 (1) 的真实几何上存在完整第四 ruling 解，包括允许的独立二阶 homogeneous gauge 和全部第三 homogeneous gauge，则必要有

$$
\boxed{M_4(q)=0,\qquad M_2^*(q,\tau_q)=0.}
\tag{4}
$$

更准确地，若其中任一个不为零，中心化完整 pure 第四 ruling 不属于偶部三矩空间

$$
\mathcal W_e=
\operatorname{span}_{\mathbb R}
\left\{h,\ \sigma^2,\
\frac{1+4\varepsilon^2\kappa^2\sigma^4}{h}\right\}.
\tag{5}
$$

对于复 pure 值，“属于”指实部和虚部同时属于该实空间。结论针对整个解析 germ；其证明始终保留真实负 Gaussian 常数尾，不作大 $\sigma$ 截断。

## 2. 基础有理函数域与常数

令

$$
\mathbb F=\mathbb R(\sigma,H),\qquad
D=\frac d{d\sigma}.
$$

先说明这是真正的有理函数域。若 H 对 $\mathbb R(\sigma)$ 代数，清分母后存在非零关系

$$
\sum_{m=m_0}^{m_1}a_m(\sigma)H^m=0,\qquad
a_m\in\mathbb R(\sigma),\quad a_{m_1}\ne0.
$$

除以最高项。沿实 $\sigma\to+\infty$，每个较低指数的指数衰减压过有理函数的任何幂增长，故左边趋于 1，矛盾。因此 H 超越。

把 $\mathbb F$ 嵌入实际 meromorphic germ。若 $Da=0$，其实际函数在一个无极点开区间上为实常数；上述嵌入单射遂给 $a\in\mathbb R$。所以

$$
\operatorname{Const}(\mathbb F,D)=\mathbb R.
\tag{6}
$$

在形式变量 y 中，同一导子为

$$
D=\partial_\sigma+2\varepsilon\sigma y\,\partial_y.
\tag{7}
$$

以下每一有理函数恒等都通过 $y=H$ 解释为真正函数恒等。

## 3. 任意有限组不同非零 Gaussian 字母模全导数独立

设 $S_0\subset\mathbb Z\setminus\{0\}$ 有限。声称

$$
Da=\sum_{r\in S_0}c_rH^r,\qquad
a\in\mathbb F,\quad c_r\in\mathbb R
\quad\Longrightarrow\quad c_r=0\ \text{全部成立}.
\tag{8}
$$

### 3.1 不可出现非 y 分母

设 $P\in\mathbb R(\sigma)[y]$ 为 monic 不可约多项式，$P\ne y$。若 $P\mid DP$，由 y 次数与最高系数可知

$$
DP=2\varepsilon d\sigma P,\qquad d=\deg_yP.
$$

写 $P=y^d+\sum_{i<d}a_i(\sigma)y^i$。每个非零低系数须满足

$$
\frac{a_i'}{a_i}=2\varepsilon(d-i)\sigma.
\tag{9}
$$

非零有理函数的对数导数在无穷远是 $O(\sigma^{-1})$，不可能等于 (9) 的非零一次式。因此所有低系数为零，$P=y^d$；不可约性迫 $P=y$，与假设矛盾。

若 a 在某个这样的 P 上有 m 阶极点，$Da$ 的 P 极点恰升至 $m+1$：最高极项含 $-m\,DP$，不能由其余项抵消。式 (8) 的右边是 Laurent y 多项式，没有该极点。于是 a 只能是

$$
a=\sum_{n=n_0}^{n_1}a_n(\sigma)y^n,\qquad
a_n\in\mathbb R(\sigma).
\tag{10}
$$

### 3.2 Laurent 系数无有理原函数

按 y 幂比较，得到

$$
a_n'+2n\varepsilon\sigma a_n=c_n,
\tag{11}
$$

其中不在 $S_0$ 的 $c_n=0$。任何有限复极点都会被第一项升一阶，第二项不会，因此 $a_n$ 没有有限极点，必为多项式。

当 $n\ne0$ 时，非零多项式 $a_n$ 的最高次在第二项升一阶，既不能被 $a_n'$ 抵消，也不能等于常数。故 $a_n=0$、$c_n=0$。n=0 时只有常数 $a_0$。这证明 (8)。

这个论证也可在复常域上逐字进行；本稿只需实常域及其普通复线性延拓。

## 4. 同锚二重词是真实独立的，不是形式系数假设

以后取

$$
S=\{1,-1,-2,-3\},
\qquad
E_r(\sigma)=\int_0^\sigma H(t)^r\,dt,
$$

$$
K_{r,s}(\sigma)=\int_0^\sigma H(t)^rE_s(t)\,dt,
\qquad
A_{r,s}=K_{r,s}-K_{s,r}.
\tag{12}
$$

所有积分使用同一个实际中心锚 0。一般词的前缀微分规范是

$$
D I_{r,w}=H^r I_w,\qquad I_\varnothing=1.
$$

**词独立引理。** 这些 iterated words 在 $\mathbb F$ 上线性独立；特别长度至多二的 $1+4+16=21$ 个词独立。

证明如下。反设存在有限非平凡关系，取其中最高词长最小者，再在该长度下取顶层非零系数数目最少者。除以一个顶层系数，使其为 1。微分后，如果任何其他顶层系数的导数不为零，就得到同一最高长度但顶层支持更小的非平凡关系，矛盾。因此所有顶层系数由 (6) 为常数。

微分后的关系长度下降。由最高长度的最小性，其每个形式系数都必须为零。对一个次长词 w，该系数形如

$$
Da_w+\sum_{r\in S}c_{r,w}H^r=0.
$$

式 (8) 迫全部 $c_{r,w}=0$，与原顶层至少一个系数为 1 矛盾。空词情形由实际函数 1 非零起始。证毕。

shuffle 身份准确给

$$
K_{r,s}+K_{s,r}=E_rE_s,\qquad
2K_{r,r}=E_r^2.
\tag{13}
$$

所以以下是同一 21 维 $\mathbb F$ 空间的另一组真实基：

$$
1,\qquad E_r,\qquad E_rE_s\ (r\le s),\qquad
A_{r,s}\ (r<s).
\tag{14}
$$

这里给 S 任选固定次序，随后专取 $A_{-2,-3}=K_{-2,-3}-K_{-3,-2}$ 的所写方向。式 (14) 将 R245 的有限生成结论提升为本函数域上的准确独立性；不是把未证的冗余生成元逐项置零。

尤其 $\mathcal W_e\subset\mathbb F$。若某个完整函数属于 (5)，则其在 (14) 中的每个面积系数必须为零。负指数 E 的真实常数尾从未扣除，也没有通过其渐近极限替换原函数。

## 5. 从 R73 取得两个真实 Gaussian 系数

令 $\mathsf M(\sigma)$ 为 R73 的 raw 八矩密度，$\mathsf m(0)=0$、$\mathsf m'=\mathsf M$。写对应二次算子为

$$
\Phi_{\mathsf m}
=Q_\sigma+\sum_{r\in S}E_r B_r,
\tag{15}
$$

其中 $Q_\sigma$ 是奇 Laurent 多项式系数的二次算子，$B_r$ 是与 $\sigma$ 无关的真实二次算子。R245 已从 R73 的五个 h 指数完整证明 (15)。

本稿只需 $B_{-2},B_{-3}$。先在原坐标中保留

$$
k=\kappa-j,\qquad d=j,\qquad
K_0=kx^2+\frac{\kappa^2-j^2-1}{h}x
+\frac{\kappa((\kappa-j)j-1)}{h^2}.
$$

R73(6)、(9)、(10) 及 (2) 逐项给：

$$
\begin{aligned}
8h^2 r_1={}&-j^4+\frac\kappa2j^3
-(\kappa^2+2)j^2+\frac\kappa2j+\kappa^2-1,\\
4h^2 s_0={}&-\kappa j^3+\kappa^2j^2
-(\kappa+2\kappa^3)j,\\
8h^3 r_0={}&-\kappa j^4+2\kappa^2j^3
-(2\kappa+4\kappa^3)j^2+2\kappa^2j-\kappa.
\end{aligned}
\tag{16}
$$

其余 raw 八坐标分别属于 h 指数 $1,0,-1$；本节没有把它们删出完整恢复，只因它们不贡献这两个指定的 E 系数。

对 $r\ne0$，$\int_0^\sigma j(t)^nH(t)^r\,dt$ 中 E_r 的准确系数为

$$
\mu_r(n)=\frac{(-1)^n(2n-1)!!\,\kappa^n}{r^n},
\qquad \mu_r(0)=1.
\tag{17}
$$

这是逐次分部积分的有限恒等：$D H^r=2r\varepsilon\sigma H^r$，每次提取的奇多项式边界在中心为零。所需表为

| r | $\mu_r(1)$ | $\mu_r(2)$ | $\mu_r(3)$ | $\mu_r(4)$ |
|---|---:|---:|---:|---:|
| $-2$ | $\kappa/2$ | $3\kappa^2/4$ | $15\kappa^3/8$ | $105\kappa^4/16$ |
| $-3$ | $\kappa/3$ | $\kappa^2/3$ | $5\kappa^3/9$ | $35\kappa^4/27$ |

代入完整 (16)，得到

$$
B_{-2}=a\,\Phi_{r_1}+b\,\Phi_{s_0},
\qquad B_{-3}=c\,\Phi_{r_0},
\tag{18}
$$

$$
\boxed{
a=-\frac{51\kappa^4+2\kappa^2+8}{64h_e^2},\qquad
b=-\frac{17\kappa^4+4\kappa^2}{32h_e^2},\qquad
c=-\frac{\kappa(41\kappa^4+27)}{216h_e^3}.
}
\tag{19}
$$

因而

$$
a+3b=-\frac{153\kappa^4+26\kappa^2+8}{64h_e^2},
\qquad c(a+3b)\ne0.
\tag{20}
$$

这里保留了全部 raw $h_s,k_s$ 项；若从常态矩阵或只取 $hkG$ 代替 (16)，就不会得到这些系数。

## 6. 指定面积系数在完整第四原式中的唯一来源

沿用 R248 的完整规范：

$$
Z(q,q)=K_2(q,q)-Y_{W_2},\qquad
W_2=\Phi_{\mathsf m}(q,q),
$$

$$
C(q;q,q)=K_C-Y_{W_C},
$$

$$
\mathfrak P_\sigma(q)
=-\mathfrak b_\sigma(Z(q,q),Z(q,q))
-4\mathfrak b_\sigma(Y_q,C(q;q,q)).
\tag{21}
$$

$K_2,K_C$ 都是 R56 的真实局部恢复，不能设零。R73 的完整第三 characteristic 方程为

$$
(W_C)'=
\ell_\sigma(q;q,q)
-\Phi_{\mathsf M}(q,\Phi_{\mathsf m}(q,q))
-\Psi_\sigma(q,\Phi_{\mathsf M}(q,q)).
\tag{22}
$$

它保留变化 profile 的 chain 项 $\Psi$。逐项检查 history 层次：

- $Z$ 对 $\mathsf m$ 线性，所以其平方至多含 $E_rE_s$；它不能产生反对称面积。
- 第三局部 $K_C$ 从 $H(Y_q,Z)$ 的 $P,B,\eta_0$ 恢复，至多对 $\mathsf m,\mathsf m'$ 线性，没有二重 s 原函数。
- $\ell-\Psi$ 的 s 积分没有累计 $\mathsf m$。R245 的完整奇偶证明使其为奇 Laurent 密度，原函数初等。
- 将 (15) 代入 (22)，涉及 $Q_\sigma$ 的各项经真实分部积分，只给 Laurent 系数及 Laurent 乘单个 E。其原因是 Q 为奇 Laurent，$Q_\sigma H^r$ 仍奇；即使指数和为零也只是普通多项式原函数。

因此唯一二重词项准确为

$$
(W_C)_{\rm two}
=-\sum_{r,s\in S}K_{r,s}\,
B_r(q,B_s(q,q)).
\tag{23}
$$

在 (13) 的统一基中，$A_{r,s}$ 的系数为

$$
-\frac12\{B_r(q,B_s(q,q))-B_s(q,B_r(q,q))\}.
\tag{24}
$$

这是整个第三 history 的系数，不是只挑某个预期来源。实际中心常数只在常元/单层中；完整 prefix 比较另由 R224 在同一个 $\mathcal W_e$ 商中支付。

记

$$
\mathcal E_\sigma(u,v)
=\mathfrak b_\sigma(Y_u,Y_v).
$$

由于 (21) 中 history 部分为 $+4\mathcal E_\sigma(q,W_C)$，完整 $\mathfrak P_\sigma(q)$ 的 $A_{r,s}$ 系数恰为

$$
\boxed{
-2\mathcal E_\sigma
\left(q,\,
B_r(q,B_s(q,q))-B_s(q,B_r(q,q))
\right).
}
\tag{25}
$$

式 (25) 已处理 $Z^2$、第三局部恢复和 chain 的所有其他潜在来源；本稿并非由一个孤立候选项不为零就宣告完整非成员。

## 7. 两个原算子交换子与三矩配对

按 R71/R73 的原坐标，置

$$
\mathcal P=\Phi_{r_0},\qquad
\mathcal R=\Phi_{r_1},\qquad
\mathcal S=\Phi_{s_0}.
$$

对角值为

$$
\mathcal P(q,q)=J((q'')^2),\quad
\mathcal R(q,q)=(q')^2+xJ((q'')^2),\quad
\mathcal S(q,q)=J(x(q'')^2).
\tag{26}
$$

R71(12) 给第一条；第二条由同一次右锚分部积分得

$$
\begin{aligned}
\mathcal P(q,\mathcal R(q,q))
-\mathcal R(q,\mathcal P(q,q))&=\tau_q,\\
\mathcal P(q,\mathcal S(q,q))
-\mathcal S(q,\mathcal P(q,q))&=3\tau_q.
\end{aligned}
\tag{27}
$$

例如令 $\rho=q''$，$\mathcal S(q,q)''=-\rho^2-2x\rho\rho'$、
$\mathcal P(q,q)''=-2\rho\rho'$。两项相减为
$-J(\rho^3)=3\tau_q$；右端零 collar 支付边界，左尾保留。

由 (18)、(27)，

$$
B_{-2}(q,B_{-3}(q,q))
-B_{-3}(q,B_{-2}(q,q))
=-c(a+3b)\tau_q.
\tag{28}
$$

故指定真实面积 $A_{-2,-3}$ 的完整系数为

$$
\boxed{
2c(a+3b)\,\mathcal E_\sigma(q,\tau_q).
}
\tag{29}
$$

下面保留全部三矩，而不只抽出其中一个。定义

$$
m_0=\int_Iq''\tau_q'',\qquad
m_1=\int_Ixq''\tau_q'',\qquad
m_2^*=M_2^*(q,\tau_q).
$$

因为 $\tau_q'=(q'')^3/3$、$\tau_q''=(q'')^2q'''$，且 q 在两 collar 为零，

$$
m_0=0,\qquad m_1=-\frac14M_4(q),
\tag{30}
$$

$$
m_2^*
=-\frac12\int_I x(q'')^4
+\frac23\int_I q'(q'')^3.
\tag{31}
$$

$\tau_q$ 自己可以有非零左常尾；上述式子没有把它设为紧 profile，只有 q 及相关导数的真实 collar 边界为零。

R56 第一分子配对的准确三矩式给

$$
\mathcal E_\sigma(q,\tau_q)
=\frac{1+j^2}{4h}m_0+\frac j2m_1+\frac h4m_2^*
=-\frac j8M_4(q)+\frac{h_eH}4m_2^*.
\tag{32}
$$

两个函数 $j=2\varepsilon\kappa\sigma^2$ 与 $H$ 在 $\mathbb F$ 中不成实常数比例。由 $\varepsilon>0,\kappa\ne0$ 和 H 的超越性，(32) 恒为零当且仅当

$$
M_4(q)=m_2^*=0.
\tag{33}
$$

本结论不需要对 $m_2^*$ 的符号作任何假设，也不把局部 tail 值与 (30) 的全区间积分混淆。

## 8. 从真实面积独立到完整偶部障碍

中心模型的第一场 TB 偶，第二场 N 偶/TB 奇，第三场 TB 偶/N 奇；这是 R231 由 R56 完整恢复得到的奇偶链。因此 (21) 本身是偶解析函数。

由 §4 的真实词独立性，如果 $\mathfrak P_\sigma(q)\in\mathcal W_e\otimes_{\mathbb R}\mathbb C$，则其 $A_{-2,-3}$ 系数必须为零。由 (20)、(29)、(33)，这迫 (4)。反过来，(4) 只清这一面积槽，绝不保证其他 Gaussian 槽、其他谐波或完整 ruling 已清。

R248 的精确规范给完整 $e^{-4i\theta}$ 系数
$\mathfrak P(q)/16$，实第四谐波幅度为
$\operatorname{Re}\mathfrak P(q)/8$、
$\operatorname{Im}\mathfrak P(q)/8$。于是复非成员必使至少一个真实第四谐波的偶部非成员。

R224/R231 的原式比较进一步说明：真实中心入 history、任意允许的二阶 homogeneous gauge 及全部第三 homogeneous gauge，均只能改变同一个 (5) 内的偶函数。即使 gauge 有任意光滑相位依赖，其第四 Fourier 系数仍在这个有限维空间。因此这是真正不能由这些 gauge 修复的完整 ruling 障碍。

只在同一解析 germ 内比较函数；没有把实际闭路径延伸到整条实轴，也没有重新选择目标度量或物理区间。

## 9. R239 单 block 与最终不可分离双 block 都严格违反此门

先取任一未旋转的完整 block，其微包形式为

$$
f_0=\sum_i a_i u_i,\qquad
g_0=\sum_i s_i a_i u_i,\qquad
s_i\in\{-1,1\},
$$

其中实紧 $u_i$ 的支撑两两不交，至少一个 $a_i u_i$ 非零。令 $q_0=f_0+ig_0$。逐包普通复四次方给

$$
\boxed{
M_4(q_0)
=-4\sum_i a_i^4\int_I(u_i'')^4<0.
}
\tag{34}
$$

严格性只用非零紧 profile 不可能满足 $u_i''\equiv0$。没有任何跨包项，也不需评价其真实积分数值。故该 block 的完整实偶 pure 函数必不属于 $\mathcal W_e$。

R239 最终取两个不交完整 block，分别旋转
$\alpha$ 和 $\beta=\pi/2-\alpha$，再乘非零实幅度 $A_1,A_2$。每个未旋转 block 都满足 (34)。因此最终 q 的四次矩为

$$
M_4(q)
=A_1^4e^{-4i\alpha}M_4(q_{0,1})
+A_2^4e^{4i\alpha}M_4(q_{0,2}).
\tag{35}
$$

R248 已在 R239 原 IFT 的更小正宽度开域内严格保证

$$
-\frac12<\sin2\alpha<0,\qquad
\cos4\alpha>\frac12.
$$

所以

$$
\operatorname{Re}M_4(q)
=\cos4\alpha
\{A_1^4M_4(q_{0,1})+A_2^4M_4(q_{0,2})\}<0.
\tag{36}
$$

这直接违反 (4)，也与 R248 的两个 block 分别必要 membership 完全一致。真实正伸缩、不同放置及最后共同正归一化只给各项乘正因子，不改变该严格号。

因此：

$$
\boxed{\text{R239 的该不可分离完整三阶圆，不能在 (1) 的共振端芽上完成第四 ruling。}}
\tag{37}
$$

它仍然满足已经证明的三矩、完整第三槽及 R231/R237/R241 六能量零。新的失败来自完整面积原函数，不与那些已付结论矛盾，也没有重新计算它们。

$M_4$ 只依赖 q 的二阶 profile 导数，并在固定紧 I 的 $C^2$ 拓扑连续。故 (36) 还排除该圆的一个 $C^2$ 邻域内、仍满足原合法三矩/低阶条件的圆，几何 germ 固定为 (1)。改变第一 profile 时目标按该新 profile 定义；不冒称沿 profile 变化仍保持原先同一个度量。

## 10. 边界与下一真正剩余自由度

本稿的非成员是整个真实解析偶函数的非成员，来自 §4 的实际独立性与 §6 的完整原式系数，不是 formal remainder、负数值或单层渐近。所有负 Gaussian 原函数保持其中心锚及真实常数尾。

结论仍有明确范围：

- 共振条件 $\varepsilon=\kappa^2/4$ 和 $b=0$ 已固定，没有把 (19) 自动用于其他 germ；
- 普通复四次矩可以通过其他 profile 方向发生相消，所以 (34)、(36) 不能扩为所有三矩圆的普遍非零；
- (4) 即使成立也只清指定面积槽，不给完整第四 ruling、period 或 joint 的充分性；
- 不把 profile 角度或幅度选择当成同一既定目标下的自由负成本。

下一构造若继续使用这个共振端芽，至少须准确支付 (4)，并保已有完整低阶与全函数条件；仅重复已付六能量或保持 (34) 的更多同类 block，不会消掉本稿的完整面积系数。
