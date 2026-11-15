# R248：完整四次谐波的平方幅度结构与互补双 block 的准确归约

日期：2026-11-15。完整纸面证明；没有执行新的 profile 积分、符号目标、函数秩、参数求根或几何计算。

本稿研究完整第四 ruling 的 $\cos4\theta,\sin4\theta$ 两个函数系数，保留全部局部恢复、变化 profile 的链式项、真实 s-history 和左尾。它不再只取 R231、R237、R241 的某个增长层。

主要结论有两条。

1. 对不交紧微包 $q=\sum_i c_i u_i$，完整 pure 四次分子积分只含 $c_i^2c_j^2$。证明不要求单个第二场局域；其真实跨包尾仍进入实函数系数。
2. 对 R239 的两个互补旋转完整 block，在可保证的非退化角范围内，两条完整四次谐波同时属于同一个偶端芽三矩空间，当且仅当每个未旋转 block 的一个实偶函数分别属于该空间。两个 block 不能依靠互补角相互抵消一个失败的完整 pure 条件。

本稿没有证明这两个实偶函数已经属于或不属于该空间，也没有给第四 ruling、period 或 joint 的解。

来源：[R56 完整分子恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 真实第二 history 与链式项](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R224 偶部 gauge 商](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)、[R231 完整领先门及中心化](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、[R239 完整不可分离圆](R239-nonseparable-third-order-circles-paying-four-exceptional-energy-gates.md)、[R243 完整偶函数的有限 jet 判据](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md)和 [R245 完整 block 加法及有限 history](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)。

## 1. 同一真实恢复与四次谐波规范

固定一条真实几何、同一个 profile 区间 $I=[\ell,r]$、同一个右零 collar 和同一个 s 起点。采用 R56 的 canonical characteristic 初值，即第二、第三 characteristic 函数在该共同起点为零；其余局部恢复量仍由原式决定。所有以下算子都使用这套初值；不在不同微包之间重新锚定。几何满足 $h>0$、$z=x+\omega\ne0$，并写

$$
e=hx+d,
\qquad
Y_u=F V_{Y_u}/z,
\qquad
V_{Y_u}=(-u'/2,0,hu-eu'/2).
\tag{1}
$$

用 $H(U,V)$ 表示对称双线性 forcing，规范为 $H(U,U)=(dU)^2$。令

$$
Z(u,v)=\operatorname{Range}H(Y_u,Y_v),
\qquad
C(a;u,v)=\operatorname{Range}H(Y_a,Z(u,v)).
\tag{2}
$$

这里的 Range 是 R56 的完整右锚恢复，包含真实局部场和 s 积分。若输入暂未满足左 collar 或 period 条件，(2) 仍指同一形式恢复式；它并不宣称该单项已是合法全局场。取普通复双线性延拓，不使用共轭内积。

对任意两个恢复分子定义

$$
\mathfrak b_s(U,V)
=\frac1{h(s)}\int_\ell^r
\partial_xV_U(s,x)\cdot\partial_xV_V(s,x)\,dx.
\tag{3}
$$

它是准确的分子积分。对于满足所需 collar 的完整 forcing，它就是 R56(4) 中的 ruling 配对；对于带左尾的单个分解项，只使用 (3) 的代数定义，不把它另称为该单项的完整 range 条件。

现在取真实合法圆

$$
\phi_\theta=f\cos\theta+g\sin\theta,
\qquad D_\theta=f^2-\phi_\theta^2,
\qquad q=f+ig.
\tag{4}
$$

双线性槽记号给

$$
Z_\theta=Z(f,f)-Z(\phi_\theta,\phi_\theta),
\qquad
W_\theta=-2\{C(\phi_\theta;f,f)
-C(\phi_\theta;\phi_\theta,\phi_\theta)\}.
\tag{5}
$$

因此第四 forcing
$-H(Z_\theta,Z_\theta)-2H(Y_{\phi_\theta},W_\theta)$
中，唯一四次于 $\phi_\theta$ 的部分对应以下齐次四次算子：

$$
\boxed{
\mathfrak P_s(u)
=-\mathfrak b_s(Z(u,u),Z(u,u))
-4\mathfrak b_s(Y_u,C(u;u,u)).
}
\tag{6}
$$

其余项对 $\phi_\theta$ 的次数至多二，不能产生第四谐波。由于

$$
\phi_\theta=\frac{q e^{-i\theta}+\bar q e^{i\theta}}2,
$$

完整 ruling 的 $e^{-4i\theta}$ 系数准确为 $\mathfrak P_s(q)/16$，实第四谐波部分则为

$$
\boxed{
\frac18\operatorname{Re}\{\mathfrak P_s(q)e^{-4i\theta}\}
=\frac{\operatorname{Re}\mathfrak P_s(q)}8\cos4\theta
+\frac{\operatorname{Im}\mathfrak P_s(q)}8\sin4\theta.
}
\tag{7}
$$

式 (7) 区分了单个复 Fourier 系数与实谐波幅度。它不是从某个 leading energy 猜出的规范。

## 2. 支撑在一个微包内的 forcing，其恢复外尾分子至多仿射

先证明一个直接来自 R56 的引理。设整个 forcing 的四个分子配对 $J,T_x,T_s,T_{sx}$ 支撑在固定紧区间 $J_i\Subset I$。在其右侧，真实右锚与 canonical 初值给恢复场为零。在其左侧，

$$
B_H=0,\qquad P_H=p(s),\qquad
\eta_{0,H}=-\frac12p_s.
\tag{8}
$$

其中 $p(s)$ 是从整个 forcing 真实积出的累计量，通常不为零。R56(5) 给

$$
(W_H)_s=K_0p-\lambda p_s,
$$

而 $K_0$ 对 x 至多二次，$\lambda$ 至多一次。故在该左外区间上，同一 canonical 初值产生

$$
W_H=a(s)x^2+b(s)x+c(s).
\tag{9}
$$

三个系数保留全部真实 s-history。置

$$
A_H=\frac12(W_H)_x+\frac{\eta_{0,H}}h
=a x+\frac b2-\frac{p_s}{2h}.
$$

由 R56(7)，

$$
V_H=(A_H,(x+\omega)p,eA_H-hW_H).
\tag{10}
$$

第三分量的二次项 $hx\cdot ax-hax^2$ 准确抵消，所以 (10) 的三个分量都对 x 至多仿射。特别

$$
\boxed{\partial_xV_H\text{ 在整个左外区间上与 x 无关。}}
\tag{11}
$$

这不是说左尾为零。左尾的常数和一次系数依赖真实局部恢复、全 s 积分及 $p,p_s$，均留在 (10) 中。若另加任意非 canonical 的 profile 初值，则必须另外检查其外尾；本引理不会把该新增输入自动消掉。

对任意紧 profile $u$，(1) 同时给

$$
\int_{\operatorname{supp}u}\partial_xV_{Y_u}\,dx=0.
\tag{12}
$$

最直接的理由是紧分子的端差为零。逐项写出亦为
$\int u'=\int u''=\int x u''=0$。因此它与另一个微包所产生的仿射外尾在 (3) 中准确正交。

## 3. 完整 pure ruling 的平方幅度定理

取有限个实 profiles $u_i\in C_c^\infty(J_i)$，其中 $J_i$ 两两不交，令

$$
q=\sum_{i=1}^N c_i u_i,\qquad c_i\in\mathbb C.
\tag{13}
$$

所有支撑在同一固定 x 坐标中。固定 u 与固定 x 的真实导数转换只增加同一 profile 的 x 导数，不改变支撑。于是不同微包的第一 forcing 逐点交叉为零，线性恢复给

$$
Z(q,q)=\sum_j c_j^2 Z_j,\qquad Z_j=Z(u_j,u_j).
\tag{14}
$$

每个 $Z_j$ 一般有非零左尾，不能从这里推其局域。第三场准确为

$$
C(q;q,q)=\sum_{i,j}c_i c_j^2 C_{ij},
\qquad C_{ij}=C(u_i;u_j,u_j).
\tag{15}
$$

$C_{ij}$ 的 forcing 是 $H(Y_{u_i},Z_j)$。虽然 $Z_j$ 可能非局域，但每项乘积和全部真实 s、x 导数都含 $Y_{u_i}$ 的一个因子。因此该 forcing 的四个分子配对支撑于 $J_i$。

若 $k\ne i$，$J_k$ 整体位于 $J_i$ 的左侧或右侧。右侧恢复为零；左侧则由 (11)、(12) 得

$$
\mathfrak b_s(Y_{u_k},C_{ij})=0.
\tag{16}
$$

这里没有忽略 $j$ 相对于 i、k 的位置，也没有把 $C_{ij}$ 的累计 history 置零。被消掉的是一个准确的“紧分子导数—仿射尾导数”积分。

将 (14)—(16) 放入 (6)，得到

$$
\boxed{
\mathfrak P_s\!\left(\sum_i c_i u_i\right)
=\sum_{i,j}c_i^2c_j^2 Q_{ij}(s),
}
\tag{17}
$$

其中可取对称的实函数矩阵

$$
\begin{aligned}
Q_{ij}={}&-\mathfrak b_s(Z_i,Z_j)\\
&-2\{\mathfrak b_s(Y_{u_i},C_{ij})
+\mathfrak b_s(Y_{u_j},C_{ji})\}.
\end{aligned}
\tag{18}
$$

式 (18) 是完整函数公式，不是渐近量：第一项保留两个真实第二左尾的全部配对；后两项保留恢复的全部局部和 chain 项、真实第三 history。它们通常不为零，也没有在本稿被认作独立函数。

因此没有 $c_i^3c_j$、$c_i^2c_jc_k$ 或四个互异幅度的项。平方幅度结论不需要三矩或第三相容性；只有把 (6) 解释成真实圆的第四谐波时，才使用 §1 的完整合法性条件。

## 4. 逐微包 $g=\pm f$ 的整个 pure 值为实

现在取

$$
f_0=\sum_i a_i u_i,\qquad
g_0=\sum_i s_i a_i u_i,
\qquad a_i\in\mathbb R,\quad s_i\in\{-1,1\}.
\tag{19}
$$

此时 $c_i=(1+i s_i)a_i$，所以

$$
c_i^2=2i s_i a_i^2,\qquad
c_i^2c_j^2=-4s_i s_j a_i^2a_j^2\in\mathbb R.
$$

由 (17)，

$$
\boxed{\mathfrak P_s(f_0+i g_0)\in\mathbb R\quad\text{对全部真实 s 成立。}}
\tag{20}
$$

它不限常状态、例外端芽或某个宽度极限。正负的 Prouhet 幅度也已包含在实 $a_i$ 中。

作固定正交变换

$$
f_\alpha=\cos\alpha f_0+\sin\alpha g_0,\qquad
g_\alpha=-\sin\alpha f_0+\cos\alpha g_0.
$$

则 $q_\alpha=e^{-i\alpha}(f_0+i g_0)$。由四次齐次性，

$$
\boxed{\mathfrak P_s(q_\alpha)=e^{-4i\alpha}P(s),\qquad
P(s)=\mathfrak P_s(f_0+i g_0)\in\mathbb R.}
\tag{21}
$$

这不是允许任意输入相位对成本锥作用的主张。这里明确构造新的实 pair，目标度量由最终第一 profile 定义；不称旋转保持先前指定的同一个目标度量。

## 5. 两个完整 block 的互补角不能互相隐藏失败的 pure 条件

取两个真正完整的 block $(f_{0,b},g_{0,b})$，$b=1,2$，每个都具有 (19) 的微包结构，其完整支撑包络不交。按 R245，“完整”包括真实第二和第三场在各自整包络外为零；不能只以微包支撑不交代替这个条件。

两 block 分别乘非零实幅度 $A_1,A_2$，并采用角

$$
\alpha,\qquad\beta=\frac\pi2-\alpha.
$$

由完整第四加法和 (21)，其总 fourth-pure 原函数是

$$
\boxed{
\mathfrak P_{\rm tot}
=A_1^4e^{-4i\alpha}P_1
+A_2^4e^{4i\alpha}P_2,\qquad P_1,P_2\text{ 均实。}
}
\tag{22}
$$

两个 block 即使是正伸缩的同构拷贝，在同一真实几何上也不能据此假定 $P_2$ 与 $P_1$ 成比例；本稿不使用这种假设。

现在取 R231/R243 的例外端芽

$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=k_e(1-2\varepsilon\sigma^2),\quad
\omega=k_e/h,\qquad \varepsilon>0, k_e\ne0.
$$

其共同偶部三矩空间为

$$
\mathcal W_e=\operatorname{span}_{\mathbb R}
\left\{h,\sigma^2,
\frac{1+4\varepsilon^2k_e^2\sigma^4}{h}\right\}.
\tag{23}
$$

令 $P_{b,e}=\operatorname{Ev}P_b$。如果使用中心化模型，则由原奇偶链 $P_b$ 本身已偶；如果使用全路径真实输入，就保留其实际 $P_b$ 后再取偶部。R224/R231 的中心比较只在同一个 (23) 商中进行，不能把实际前缀 history 独自删除。

在实函数商 $C^\omega_{\rm even}/\mathcal W_e$ 中，(22) 给

$$
\begin{pmatrix}
\bigl[\operatorname{Re}\mathfrak P_{{\rm tot},e}\bigr]\\
\bigl[\operatorname{Im}\mathfrak P_{{\rm tot},e}\bigr]
\end{pmatrix}
=
\begin{pmatrix}
A_1^4\cos4\alpha&A_2^4\cos4\alpha\\
-A_1^4\sin4\alpha&A_2^4\sin4\alpha
\end{pmatrix}
\begin{pmatrix}\bigl[P_{1,e}\bigr]\\\bigl[P_{2,e}\bigr]\end{pmatrix}.
\tag{24}
$$

若 $\sin4\alpha\cos4\alpha\ne0$，该实矩阵可逆，行列式为
$2A_1^4A_2^4\sin4\alpha\cos4\alpha$。所以

$$
\boxed{
\operatorname{Re}\mathfrak P_{{\rm tot},e},\,
\operatorname{Im}\mathfrak P_{{\rm tot},e}\in\mathcal W_e
\quad\Longleftrightarrow\quad
P_{1,e},P_{2,e}\in\mathcal W_e.
}
\tag{25}
$$

根据 (7)，左侧正是总圆的两条完整偶第四谐波均可落入三矩空间的条件。允许的二阶 homogeneous gauge 的偶部响应，以及第三 homogeneous gauge，均落在同一个 $\mathcal W_e$；因此不改变 (25) 的必要性。

式 (25) 不声称整个 fourth ruling 已可支付：还须处理其零次、二次谐波、奇部、其他 s 段、period 与同一个全局 gauge。反向箭头也仅对本节所列的两个偶第四谐波成立。

## 6. R239 的真实有限宽度构造可保证角矩阵非退化

R239 的相对节点参数满足 $\zeta\in[1/5,1/4]$，并使用

$$
\nu_0=-\frac1{2\zeta},\qquad
\nu_1=\frac1{\zeta(1-\zeta)(2-\zeta)},
\qquad
Q_0=\sum_{i=0}^3\nu_i^2,
$$

$$
S_0=\frac{3-\zeta}{\zeta(2-\zeta)^2}>0.
$$

以下是整个紧参数区间上的粗而严格的有理界：

$$
S_0\le\frac{240}{49},\qquad
\nu_0^2\ge4,\qquad
\nu_1^2\ge\frac{625}{81},\qquad
Q_0\ge\frac{949}{81}.
$$

因此

$$
0<\frac{S_0}{Q_0}
\le\frac{19440}{46501}<\frac12.
\tag{26}
$$

R239 已证明其真实有限宽度解 $\zeta(\delta)$ 满足

$$
t(\delta)=-P/Q\longrightarrow-S_0(\zeta_0)/Q_0(\zeta_0).
$$

在原 IFT 的正宽度域内再缩小一次 $\delta_0$，可同时保持全部支撑开条件、三矩、完整第三槽与四个已付能量，并确保

$$
-\frac12<t<0.
\tag{27}
$$

取原来的 $\alpha=\tfrac12\arcsin t$，则

$$
\sin4\alpha=2t\sqrt{1-t^2}\ne0,\qquad
\cos4\alpha=1-2t^2>\frac12.
\tag{28}
$$

故 R239 的两个互补角可以实际置于 (25) 的非退化范围。这只是选择已证明存在的更小正参数邻域，没有新的求根或实际积分，也不改变给定几何的合法区间。共同正归一化只给 (22) 乘一个正四次常数。

若另采用 R241 的共振 $\varepsilon=k_e^2/4$，式 (17)—(28) 仍成立；它们没有除以 $k_e^2-4\varepsilon$。共振付掉已识别增长层，不会令本稿的角矩阵退化。

## 7. 下一判定准确缩到什么

对最终冻结的一份未旋转 R239 完整 block，新的真实目标是 (6)、(18) 给出的**一个实偶函数** $P_e$ 是否在 (23) 中。它必须含全部局部/chain/真实 history，不是重新检查 $L_c,L_s,M_c,M_s$，也不是只检查某一个 Gaussian 增长系数。

R243 已给完整、有限、无需生成元独立性假设的 jet 判据；R245 已把所有真实 history 压到四个 Gaussian 原函数及其二次/面积生成元。所以 (25) 提供一个有明确原式来源的后续最小目标，而没有把尚未进行的判定当作结论。

若某个 block 的 $P_e\notin\mathcal W_e$，两互补 block 的整个偶第四 ruling 必失败，且不能由允许的 homogeneous gauge 修复。若两个都属于 $\mathcal W_e$，仅这两谐波门通过，其他完整条件仍保留。单个微包从未在证明中被赋予不存在的左 collar，也没有因平方幅度结构而被当成独立可正负支付的成本。
