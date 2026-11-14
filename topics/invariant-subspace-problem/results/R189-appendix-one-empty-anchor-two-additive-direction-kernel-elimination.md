# R189 附录：一个空谱锚与第二加性慢方向的单核消元

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已复核消元、普遍分母、真实混合域与共振应用。
状态：完整证明。处理两个加性方向上的实际快系数多项式；一个方向具有可和相位缺陷。最大图、共同深域与原指数向量均保留。一般 Hilbert ISP 仍未完成。

## 1. 旧范围与新增结论

[R189](R189-empty-phase-inverse-mixed-type-and-universal-fast-fraction-field.md)
已经证明：一个可和相位缺陷 first 加任意有界交换扰动的逆 $L$，
使每个非零 $\mathcal G[L]$ 元素在所有有限放大不变子商上单射稠密；
它们并有强主理想单位。
其整个单变量分式场也已处理。
本稿不重复这条普遍分母定理。

[R169](R169-finite-gauge-koszul-cores-and-two-slow-mode-separation.md)
§§6–7 已给独立双加性方向的有限例外互素和一变量消元，
但明确指出：一般消元算子仅在全 $H$ 上单射稠密，
不能据此做未知核内的跨核配对。

[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)
已经把共同混合域、最大闭图、完整 $C$ 自伴、加性形式类归约和有限 gauge 联合循环推进到闭 first。
本稿复用这些域事实，不重新计为新增闭包结果。

这里新增的接口是：
**消去第二方向后，特意把消元多项式留在空谱锚上；
再用其实际逆化为 $\mathcal G[L]$ 的非零有界元。**
R189 因而确实提供未知限制上的稠密性。
有限例外的跨核正交遂排除单个双变量核。

## 2. 准确假设与最大实现

记
$$
\mathcal A=\overline{\mathbb C[I,A]},\qquad
\mathfrak C=\{A\}',\qquad
K=\operatorname{Frac}\iota(\mathcal G),\qquad
\Gamma=\mu_{2^\infty}.
$$
取
$$
u=a_*+\sum_j a_j\chi_j,\qquad
a\in\ell^2\setminus\ell^1,
$$
并假设存在 $\theta\in\mathbb R$，使
$$
\boxed{\sum_j\bigl(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\bigr)<\infty.}
\tag{2.1}
$$
另取任意
$$
v=c_*+\sum_j c_j\chi_j,\qquad c\in\ell^2.
$$
允许 $c=0$。
设
$$
X=X_u+H_1,\qquad Y=X_v+H_2,
\tag{2.2}
$$
其中
$$
H_i\in\mathcal A,\qquad
\gamma_\zeta H_i-H_i\in\mathcal G
\quad(\zeta\in\Gamma).
\tag{2.3}
$$
两者的实际域分别为原 first 的域。

(2.3) 包括所有共同复 $\ell^2$ 指数权的真实倾斜。
它也包括任意有界加性慢伙伴：
令 $v=0$、$H_2=S\in\mathcal A$，
只需 $\gamma_\zeta S-S\in\mathcal G$。
这里没有把一般 $\mathcal A$ 扰动自动当成具有快 gauge 增量。

给任意有限
$$
P(x,y)\in\mathcal G[x,y].
$$
使用 R186 的共同正则器 $R(t)\in\mathfrak C$，
其每个固定正整数幂在所有有限放大不变空间及子商上单射稠密，
并将 $H$ 映入相应阶数的全部混合自然词域。
写 $p=\deg P$，$R=R(t)$，
$$
S_X=XR,\qquad S_Y=YR,
$$
$$
Z=R^p,\qquad
Q_P=\sum_{i+j\le p}g_{ij}S_X^iS_Y^jR^{p-i-j}\in\mathfrak C.
$$
其规范最大闭实现为
$$
\operatorname{Graph}\mathsf P
=
\{(f,g)\in H\oplus H:Q_Pf=Zg\}.
\tag{2.4}
$$
当 $p=0$，这就是原有界系数算子。
R186 已证明 (2.4) 是相应自然混合多项式图的闭包，
与选取正则器和填充阶数无关，并且 $C$ 自伴。
没有声称原自然混合域本来就是闭域。

**定理 2.1。**
若 $\mathsf P$ 不是零算子，则
$$
\boxed{\ker\mathsf P=0,\qquad
\overline{\operatorname{Ran}\mathsf P}=H.}
\tag{2.5}
$$
因此，对每个循环且属于 $\operatorname{Dom}\mathsf P$ 的 $\xi$，
$$
\boxed{\mathsf P\xi\text{ 非零且循环}.}
\tag{2.6}
$$
不要求 $P$ 在任一变量上首一，也不要求最高系数为实际单位。

若 $a,c$ 在 $\ell^2/\ell^1$ 中线性无关，
则任何非零形式 $P\in\mathcal G[x,y]$ 都满足结论，
并自动给非零实际实现。
更一般，只需两个形式增量类独立，见 §4。

本定理的单射稠密结论在原 $H$ 上。
本文不据此宣称新双变量多项式在每个未知限制或子商上稠密；
证明中需要普遍稠密性的只有 R189 已处理的消元分子。

## 3. 空谱锚的实际逆与可用的普遍分子

R138/R189 给 $X$ 空谱，即使 $H_1$ 为任意有界交换扰动也成立。
置
$$
L=X^{-1}\in\mathfrak C.
$$
它全域有界、单射、稠密像且拟幂零。
R189 原文对旋转后的逆陈述；这里 $L$ 只差一个非零复标量，
所以其所有 $\mathcal G[L]$ 结论保持。

特别，对任意非零形式
$$
\rho(t)\in\mathcal G[t],
$$
实际 $\rho(L)$ 非零，并满足
$$
\boxed{
I\in\overline{\rho(L)\mathbb C[A]}^{\mathrm{SOT}},
\qquad
\overline{\rho(L)M}=M
}
\tag{3.1}
$$
对每个闭 $A$ 不变 $M$ 成立。
这里第二式确由第一式给出，未从全空间稠密像猜测。

若
$$
E(x)=\sum_{j=0}^k e_jx^j\in\mathcal G[x]\setminus\{0\},
$$
则在 $\operatorname{Dom}X^k$ 上准确有
$$
\boxed{
L^kE(X)=\rho_E(L),\qquad
\rho_E(t)=\sum_{j=0}^k e_jt^{k-j}\ne0.
}
\tag{3.2}
$$
$L$ 与全部有界交换子交换并保持所有混合词域。
(3.2) 只用真正逆关系 $LXf=f$，
可以在深共同域上逐次消去 $X$，没有对一个形式分母直接求值。

这就是后面将一变量结果式变为未知限制上稠密的有界分子的步骤。

## 4. 两个形式增量类与依赖分支

R186 §8 给每个实际闭 first 的形式原函数。
可取
$$
\sigma_X(z)=\sum_j a_j(v_j(z)-1)+\iota(H_1),
$$
$$
\sigma_Y(z)=\sum_j c_j(v_j(z)-1)+\iota(H_2),
$$
其中
$$
v_j(z)=\frac{d_j-z^{2^j}}{d_j+z^{2^j}}.
$$
常数项可以校正，使全部真实有界线性关系的常数准确保留。
这些形式只记录增量，不是给无界 $X,Y$ 定义形式求值。

真实同域协变为
$$
U_\zeta XU_\zeta^*=X+D_{\zeta,X},\qquad
U_\zeta YU_\zeta^*=Y+D_{\zeta,Y},
$$
$$
D_{\zeta,X},D_{\zeta,Y}\in\mathcal G.
\tag{4.1}
$$
令 $\alpha_\zeta f(z)=f(\zeta z)$、$h_\zeta=\alpha_\zeta\sigma-\sigma$，
则半线性多项式作用
$$
\Lambda_\zeta F(x,y)
=(\alpha_\zeta F)((x,y)+h_\zeta)
\tag{4.2}
$$
准确实现最大闭图的 gauge 共轭。

因 $a\notin\ell^1$，
R180/R186 §8.4 给 $[\sigma_X]\ne0$ 于 $\mathbb C((z))/K$。

如果两个类依赖，可写
$$
[\sigma_Y]=\gamma[\sigma_X],\qquad \gamma\in\mathbb C.
$$
R186 的实际线性关系与常数校正给：在共同一阶域上
$Y=\gamma X+S$，其中 $S\in\mathcal A$ 有界；
$\gamma=0$ 时 $Y=S$ 为全域有界算子，
其形式属于 $K$。
存在 $d,e\in\mathcal G$、$d\ne0$，使
$$
dS=e
\tag{4.3}
$$
为真实有界恒等式。
用一个足够高的有限 $d$ 幂清除 (4.3)，
便在足够深的共同自然域得到
$$
d^N P(X,Y)=E(X),\qquad E\in\mathcal G[x].
\tag{4.4}
$$
R186 §8.3 已证明这种有限清分母保持最大核，并将零形式准确识别为全域零算子。
因为当前 $\mathsf P\ne0$，$E$ 不能是零多项式。
R189 的单变量定理遂给 $\ker\mathsf P=0$。
完整 $C$ 自伴给稠密像。

因此依赖分支完全归于旧 R189。
后文只需处理
$$
\boxed{[\sigma_X],[\sigma_Y]\text{ 对 }\mathbb C\text{ 线性无关}.}
\tag{4.5}
$$
R166 的纯形式引理及 R186 §8.4 给：
两形式在 $K$ 上代数无关；
$K[x,y]$ 对 (4.2) 没有非零真稳定理想。

若 $a,c$ 模 $\ell^1$ 独立，R180 已保证 (4.5)，
不需另外计算任何形式原函数。

### 4.1 有限多模式但总增量类秩至多二

上述结论也适用于如下有限列表的直接归约。
原列表可含有限个闭 first 加有界加性扰动，以及有限个有界加性模式；
全部扰动和有界模式均满足 (2.3) 的快 gauge 增量条件。
假设它们的形式增量类总秩至多二，并且某个**实际常系数组合**
是满足 (2.1) 的非绝对可和 first 加允许的有界扰动。

保留这个实际空谱组合为第一基坐标 $X$。
类秩为二时，从原列表选第二个独立类的实际代表 $Y$；
它可为另一个闭 first 加有界项，或单个有界加性模式。
对每个其余模式，减去它在这两个类上的常系数组合。
R180/R186 §8.4 先迫其一阶行属于 $\ell^1$，
所以该差是一个真实有界算子 $S\in\mathcal A$；
其形式属于 $K$。
再按 R186 §§8.2–8.3 校正常数，给真正恒等式
$dS=e$，其中 $d,e\in\mathcal G$、$d\ne0$（允许 $e=0$）。

对任何给定的有限 $\mathcal G$ 系数多项式，清除这些有限分母后，
得到 (4.4) 型的真实深域恒等式，右侧现在是
$\widetilde P(X,Y)\in\mathcal G[X,Y]$。
R186 的有界填充恒等式保证最大核完全相同，
并保证原实现非零时归约实现非零。
因此定理 2.1 排除其核。
类秩为一时仅留下 $X$，结论直接归 R189。

这个推论只按**全部增量类总秩**计数，
不能因原列表中有一个空谱方向，就省去剩余独立的有界慢累积量。
原列表有三个以上独立增量类时，此推论不适用。

## 5. 除有限 gauge 外，两个形式多项式互素

本节复用 R169 §7 的论证，并明确它只依赖 §4 的形式输入，
所以对这里的闭 first 同样有效。

若 $P$ 在 $K[x,y]$ 中为单位，
它只依赖快系数，结论已由 R151 得到。
否则令不同不可约因子产生的主素理想为
$$
\mathfrak p_1,\ldots,\mathfrak p_s.
$$
对每个 $i$，
$$
H_i=\{\zeta\in\Gamma:\Lambda_\zeta\mathfrak p_i=\mathfrak p_i\}
$$
为子群。
它若等于 $\Gamma$，便产生非零真稳定理想，
与 §4 矛盾。

Prüfer $2$ 群的每个真子群有限：
若包含阶数任意大的元素，就包含每个 $\mu_{2^n}$，
从而等于整个 $\Gamma$。
因此每个 $H_i$ 有限。
对固定 $i,j$，
$$
\{\zeta:\Lambda_\zeta\mathfrak p_i=\mathfrak p_j\}
$$
为空或一个有限陪集。
有限并给一个有限 dyadic 子群 $\mu_h$，使
$$
\boxed{\gcd_{K[x,y]}(P,\Lambda_\zeta P)=1
\qquad(\zeta\notin\mu_h).}
\tag{5.1}
$$
这里 $h$ 为某个 $2$ 的幂。

没有把二变量互素当成单位理想。
下一节只消去 $y$，保留一个非零 $x$ 多项式。

## 6. 消元并把分子留在空谱锚上

固定 $\zeta\notin\mu_h$，写 $P_\zeta=\Lambda_\zeta P$。
由 Gauss 内容引理，(5.1) 使 $P,P_\zeta$ 在
$K(x)[y]$ 中互素。
在此一变量欧几里得环中取 Bézout 式，
再清除有限个 $x$ 有理分母以及有限个 $\mathcal G$ 分母，得到
$$
\boxed{
E_\zeta(x)
=
U_\zeta^{\rm pol}(x,y)P(x,y)
+
V_\zeta^{\rm pol}(x,y)P_\zeta(x,y),
}
\tag{6.1}
$$
其中
$$
E_\zeta\in\mathcal G[x]\setminus\{0\},\qquad
U_\zeta^{\rm pol},V_\zeta^{\rm pol}\in\mathcal G[x,y].
$$
这里上标 pol 用于与实际 gauge 酉算子区分。

若某个多项式与 $y$ 无关，它在 $K(x)[y]$ 中为单位，
同一消元仍成立。
所以没有遗漏次数为零或非首一最高系数的情形。

令 $k_\zeta=\deg E_\zeta$。
由 (3.2)，(6.1) 在足够深的实际共同自然域上给
$$
\boxed{
\rho_\zeta(L)
=
L^{k_\zeta}U_\zeta^{\rm pol}(X,Y)P(X,Y)
+
L^{k_\zeta}V_\zeta^{\rm pol}(X,Y)P_\zeta(X,Y),
}
\tag{6.2}
$$
其中
$$
0\ne\rho_\zeta\in\mathcal G[t].
$$
所有 $L$ 因子有界且保持全部混合词域。
因此 (6.2) 是有限自然词恒等式，
不是一个未经识别的形式最大域计算。

## 7. 真实深核测试与单核消失

令
$$
M=\ker\mathsf P.
$$
R186 给 $M$ 闭且 $A$ 不变，以及
$$
\ker\mathsf P_\zeta=U_\zeta M.
\tag{7.1}
$$
不能假定整个 $M$ 已属于 $X,Y$ 的自然域。

对当前固定的 $\zeta$，选一个有限 $N$，
大于 (6.2) 中全部乘积及每个中间词的总次数。
R186 的共同正则化与 gauge 域保持给
$$
f\in R^NM,\qquad
g\in U_\zeta R^NM
$$
时，两者处在所需全部混合自然域，且
$$
P(X,Y)f=0,\qquad P_\zeta(X,Y)g=0.
\tag{7.2}
$$

对 (6.2) 与原双线性形式
$$
B(f,g)=\int f(y)g(-1-y)\,d\mu(y)
$$
配对。
第一项由 $P f=0$ 消去。
第二项可以在已核准的深域中交换有限自然词，把 $P_\zeta$ 移至最外层：
$$
\begin{aligned}
B(\rho_\zeta(L)f,g)
&=
B\!\left(
P_\zeta(X,Y)L^{k_\zeta}V_\zeta^{\rm pol}(X,Y)f,g
\right)\\
&=
B\!\left(
L^{k_\zeta}V_\zeta^{\rm pol}(X,Y)f,P_\zeta(X,Y)g
\right)
=0.
\end{aligned}
\tag{7.3}
$$
第二个等号用原 $H$ 上完整 $C$ 自伴的 $\mathsf P_\zeta$；
输入向量确属其自然域。
没有在未知 $M$ 上使用一个未构造的共轭。

由于 $\rho_\zeta(L)$ 有界，
而 $R^NM$、$U_\zeta R^NM$ 分别在 $M$、$U_\zeta M$ 中稠密，
(7.3) 延为
$$
B(\rho_\zeta(L)M,U_\zeta M)=0.
$$
现在才使用空谱锚的关键输入 (3.1)：
$$
\overline{\rho_\zeta(L)M}=M.
$$
于是
$$
\boxed{B(M,U_\zeta M)=0\qquad(\zeta\notin\mu_h).}
\tag{7.4}
$$
每个 $\zeta$ 可有不同的消元式、正则化阶数和算子范数；
证明不需要它们的一致界。

对 $f,g\in M$，(7.4) 使
$f(y)g(-1-y)$ 的 Fourier 支撑包含于有限群 $\mu_h$。
有限柱条件期望在 $L^1$ 收敛，
所以该乘积在每个模 $h$ 柱上为常数。

若 $M\ne0$，严格正的 odometer 权及遍历性使其总本质支撑全测。
在每个柱上选 $f_0,g_0\in M$ 使反射乘积为非零常数；
任意 $f\in M$ 与同一个 $g_0$ 的乘积也为柱常数，
故 $f$ 在该柱上为 $f_0$ 的标量倍数。
这给 $\dim M\le h$。

原 $A$ 单射拟幂零，不允许非零有限维不变空间。
故 $M=0$。
原 $C$ 自伴给稠密像；
R186 的循环图核心给 (2.6)。
定理 2.1 得证。

独立情形的证明只要求 $P$ 是非零形式多项式；
若实际实现为零，上述 $M=H$ 同样会导致矛盾。
因此这一情形同时证明了实际求值的忠实性。

## 8. 两个主模式的全阶共振符号

本节给不是普通算子多项式改名的实际点态族，
并明确其慢辅助修正。

取任意两个复 $\ell^2$ 行 $a_1,a_2$，
对应 first $u_1,u_2$，
其中 $a_1$ 满足 (2.1)，且两行模 $\ell^1$ 独立。
取任意
$$
w=b_*+\sum_j b_j\chi_j,\qquad b\in\ell^2,
$$
并记真实倾斜
$$
R_j=V(e^{-2b_j}N_j),\qquad
X_i=X_{u_i,b}.
$$
这些倾斜满足 (2.3)。

对固定总阶数 $D$，令
$$
\ell_j(t)=t_1a_{1j}+t_2a_{2j},
$$
定义到 $D$ 阶的点态生成式
$$
\mathcal F_D(t)
=
\exp\!\left[
t_1u_1+t_2u_2+
\sum_{n=2}^D\frac{2^{n-1}}n
\sum_j\ell_j(t)^n(\chi_j-1)
\right].
\tag{8.1}
$$
每个 $n\ge2$ 的系数按 $L^\infty$ 绝对收敛。
设
$$
F_\alpha=\partial^\alpha\mathcal F_D(0),
\qquad |\alpha|\le D.
\tag{8.2}
$$
该有限 jet 不随更大的 $D$ 改变。
任意标量多项式
$q(z_1,z_2)=\sum_\alpha q_\alpha z^\alpha$
对应实际点态式
$$
\mathfrak F_q=\sum_\alpha q_\alpha F_\alpha.
\tag{8.3}
$$

### 8.1 全部实际快混合修正

[R270C](R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) §10 的同一位恒等式，对
$z=\ell_j(t)$ 给
$$
z+\log[1+z(R_j-I)]
=
zR_j+\sum_{n\ge2}\frac{(-1)^{n-1}}n z^n(R_j-I)^n.
$$
因此混合修正为
$$
G_\beta
=
(-1)^{|\beta|-1}(|\beta|-1)!
\sum_j a_{1j}^{\beta_1}a_{2j}^{\beta_2}
(R_j-I)^{|\beta|},
\qquad |\beta|\ge2.
\tag{8.4}
$$
每个和按算子范数绝对收敛，且
$$
G_\beta\in\mathcal G.
\tag{8.5}
$$
对 R270C 已证的
$G_n(a_1+s a_2)\in\mathcal G$
作次数 $n$ 的有限多项式插值，
提取各个 $s$ 系数，得到 (8.5)。
后者只使用 $\mathcal G$ 的线性封闭，
没有假设它是整个 $\mathcal A$ 的理想。

有限位恒等式和真实混合 jet 极限给
$$
\boxed{
\mathfrak F_qe^w
=
P_q(X_1,X_2)e^w,
}
\tag{8.6}
$$
其中
$$
P_q(z)
=
\exp\!\left(
\sum_{2\le|\beta|\le D}
\frac{G_\beta}{\beta!}\partial^\beta
\right)q(z).
\tag{8.7}
$$
指数在有限多项式空间中截断，
所以 $P_q\in\mathcal G[z_1,z_2]$。

(8.6) 的域不靠形式指数：
先在有限物理位验证有限 jets；
点态 first 截断在每个有限矩中收敛，
有界辅助截断在 $L^\infty$ 收敛，
并与 $e^w$ 的全部有限指数矩结合；
右端 (8.4) 按范数收敛，
R145/R186 的混合自然 jet 定理给每个实际词作用于 $e^w$ 的极限。
因此 $e^w$ 处在全部所需自然混合域，
(8.6) 确为原 Haar 空间等式。

### 8.2 单向量循环，不再只得两个 gauge 联合循环

(8.7) 的每个非恒定微分项至少降低总次数2，
所以非零 $q$ 的最高齐次部分完整保留。
两行模 $\ell^1$ 独立使 §4.5 成立；
定理 2.1 因而给
$$
\boxed{\mathfrak F_qe^w\text{ 非零且循环}\qquad(q\ne0).}
\tag{8.8}
$$
对非恒定 $q$，任意 $q-\lambda$ 仍非零，故
$$
\boxed{(\mathfrak F_q-\lambda)e^w
\text{ 对每个 }\lambda\in\mathbb C\text{ 非零且循环}.}
\tag{8.9}
$$

本结论是两模式共振线性变换 $q\mapsto\mathfrak F_q$ 的全多项式范围。
它没有把 $\mathfrak F_{q^m}$ 等同于 $(\mathfrak F_q)^m$；
一般点态幂不能从 (8.8) 自动推出。

## 9. 一个真正独立且全支撑重叠的不可约例子

取
$$
a_j=(j+1)^{-\sigma},\qquad
c_j=(-1)^j(j+1)^{-\sigma},\qquad
\frac12<\sigma\le1,
$$
$$
u=\sum_j a_j\chi_j,\qquad v=\sum_j c_j\chi_j.
$$
$u$ 的 first 满足正相位空谱条件。
$v$ 的正、负子列各自非绝对可和，因而没有可和相位缺陷方向；R138 的实际 first 谱分类给其全平面谱分支。
两行在 $\ell^2/\ell^1$ 中独立：
若 $\alpha a+\beta c\in\ell^1$，
在偶、奇子列上分别迫 $\alpha+\beta=0$、$\alpha-\beta=0$。

定义两个慢但有界的辅助
$$
s_2=\sum_j a_j^2(\chi_j-1),\qquad
s_3=\sum_j a_j^3(\chi_j-1).
$$
因 $c_j^2=a_j^2$，取
$$
q(U,V)=V^2-U^3-\lambda
$$
时，(8.3) 给准确点态表达式
$$
\boxed{
\left[
v^2-u^3+(2-6u)s_2-8s_3-\lambda
\right]e^w
\text{ 非零且循环}
}
\tag{9.1}
$$
对每个 $\lambda\in\mathbb C$ 和每个复 $\ell^2$ 指数权 $w$ 成立。

其自然实现为
$$
Y^2-X^3
+G_{02}-3G_{20}X-G_{30}-\lambda I,
\tag{9.2}
$$
全部 $G$ 系数快，但 $X,Y$ 是两个独立无界 first。
形式 $V^2-U^3-\lambda$ 对每个 $\lambda$ 在 $\mathbb C[U,V]$ 中不可约：
$U^3+\lambda$ 不可能是 $\mathbb C[U]$ 中的平方。
所以这里不是两条单模式结论的乘积。

R155 的辅助要求有界，而本例的 $v$ 不有界；
R150 的二变量矩形角也不存在，因为分别次数为3和2但 $U^3V^2$ 系数为0。
R270C/D 的一闭 first 多项式同样不覆盖两个独立行。
本文证明的是 (9.1)，不删去其真实慢修正而改称普通
$(v^2-u^3-\lambda)e^w$ 已解决。

## 10. 当前边界

1. 两个方向都在全平面分支时，消元分子一般仅知全空间单射稠密；
   本稿需要的 (3.1) 不再自动成立，原单核问题继续保留。
2. 第三个独立慢加性方向会使两个互素多项式的商通常仍正维，
   不能保证消去后只剩空谱锚的一变量多项式。
   本稿不由一个空谱模式推断任意多个慢模式的全部多项式循环。
3. 普通点态 $F(u,v)$ 的混合 Bell 修正通常不在 $\mathcal G$；
   本稿的全阶应用使用 (8.1) 的具体抵消。
4. R236 最新二位双池全阶判据已覆盖满足其标量行列式预算的
   单主行 $F_q+v_c-\lambda$，包括已列规则幂率和伸缩指数晚首偏离。
   本文不重新把那些单主行范围记为未闭；
   §9 的新增对象保留两个模 $\ell^1$ 独立的无界行。
5. R189 的普遍性质只用于 $\rho_\zeta(L)$；
   新 $\mathsf P$ 的全空间结论不自动下降到任意限制或子商。
6. 每次跨核恒等式都先进入同一个足够深的实际混合域。
   没有把未知核整个收入自然域，也没有把原空间的 $C$ 降到未知限制。
7. 两方向依赖的全部情形已明确归还 R189；
   新增的是独立两方向的单核消元及其实际共振点态应用。

一般独立全平面慢耦合和完整 Hilbert ISP 继续保留。
