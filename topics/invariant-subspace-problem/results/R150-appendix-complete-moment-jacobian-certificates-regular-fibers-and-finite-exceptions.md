# R150 附录：完整合并矩的 Jacobian 证书、正则纤维与任意有限对数多项式的有限例外

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：已证明；Astra-ISP-1cf8c51d 与 boundary_resume_1cf 全文核对真实合并矩、Bézout 余项、二次深域、有限临界值及具体十四变量例。
本稿把已经支付的二次深度近单位用于一个准确的有限多项式 Bézout 证书。判据中的多项式是原普通目标的完整合并矩逆，不把它与原点态多项式的梯度混同。普通复 Hilbert 不变子空间问题仍未完成。

## 1. 原目标、完整矩逆和结论

取不同复指数 $\rho_1,\ldots,\rho_q$，$\operatorname{Re}\rho_\nu>0$，以及原固定中心模式
$$
u_{\rho_\nu}=-\kappa_{\rho_\nu}
+\sum_{p\ge0}
\frac{\rho_\nu(\log(p+2))^{\rho_\nu-1}}{p+2}\chi_p.
\tag{1.1}
$$
令 $F\in\mathbb C[x_1,\ldots,x_q]$ 非恒定，普通总次数为 $D\ge1$。
指数权为任意 $w=w_*+\sum_pw_p\chi_p$，$(w_p)\in\ell^2(\mathbb C)$。

按全部 $1\le|\omega|\le D$ 建立完整矩表，记
$$
g(\omega)=(|\omega|,\rho\cdot\omega-|\omega|),\qquad
c_\omega=\prod_\nu\rho_\nu^{\omega_\nu}.
$$
相同键准确合并，所得有限键表为 $\mathcal I_D$，大小为 $K$。
定义标量多项式
$$
\mathcal Q_F(Y)=
\left.
F(\partial_t)
\exp\left[
\sum_{|\omega|=1}t^\omega Y_\omega+
\sum_{2\le|\omega|\le D}
\frac{(-2)^{|\omega|-1}}{\omega!}t^\omega Y_\omega
\right]\right|_{t=0},
$$
$$
\boxed{Q_F(W)=\mathcal Q_F((c_\omega W_{g(\omega)})_\omega).}
\tag{1.2}
$$
它是有限可计算的普通标量多项式，次数至多 $D$。
它非恒定：令所有高矩 $W_{d,s}$（$d\ge2$）为零，所得恰是
$F(\rho_\nu W_{1,\rho_\nu-1})$。

定义这个准确多项式的临界值集合
$$
\boxed{
\Sigma_F=
\{Q_F(z):z\in\mathbb C^K,\ 
\partial_{W_g}Q_F(z)=0\text{ 对全部 }g\}.
}
\tag{1.3}
$$

**定理。** $\Sigma_F$ 是有限集，允许为空。对每个
$\lambda\notin\Sigma_F$ 和每个复平方可和 $w$，
$$
\boxed{[F(u_{\rho_1},\ldots,u_{\rho_q})-\lambda]e^w
\text{ 非零且对原 }A\text{ 循环}.}
\tag{1.4}
$$
$\Sigma_F$ 只依赖 $F$ 和原指数表，不依赖指数权 $w$。
其中的值只是本判据留下的候选，不表示它们真实存在非零核。

本结论没有普通齐次、实最高部分、最高曲线非零、实梯度或矩形首系数假设。
$\Sigma_F$ 是 (1.2) 的临界值集，不能换成原 $F$ 的临界值集。

## 2. 每个正则纤维的有限标量证书

固定 $\lambda\notin\Sigma_F$。
由定义，有限多项式列表
$$
Q_F-\lambda,\qquad
\partial_{W_g}Q_F\quad(g\in\mathcal I_D)
$$
没有共同复零点。
Hilbert Nullstellensatz 因而给有限标量多项式
$A_\lambda(W),B_{g,\lambda}(W)$，使
$$
\boxed{
1=A_\lambda(Q_F-\lambda)+
\sum_gB_{g,\lambda}\partial_{W_g}Q_F.
}
\tag{2.1}
$$
这是真正的单位理想证书，不是把多变量的“无共同因子”误认为单位理想。

所用标准来源是 Stacks Project，
[Theorem 10.34.1，tag 00FV](https://stacks.math.columbia.edu/tag/00FV)。
在代数闭域 $\mathbb C$ 上，若上述理想仍是真理想，它包含于一个极大理想；该定理使此极大理想给出共同复零点，矛盾，故理想为整个环。
因此 (2.1) 是有限多项式等式，无需任何分式或解析延拓。

以下只需要一个已经验证的 (2.1)，不要求对所有 $\lambda$ 同时选择连续或统一次数的证书。
证明中常数可以依赖固定的 $\lambda$ 及其有限证书。

## 3. 从标量证书到完整实际 Bell

原合并物理行是
$$
m_{d,s}(p)=\frac{(\log(p+2))^s}{(p+2)^d}.
$$
令 $t_p=e^{-2w_p}$、$R_p=V(t_pN_p)$。
原实际混合累积量为
$$
G_\beta=(-1)^{|\beta|-1}(|\beta|-1)!
\sum_p
\left(\prod_gm_g(p)^{\beta_g}\right)
(R_p-I)^{|\beta|},\qquad 2\le|\beta|\le D.
\tag{3.1}
$$
完整合并矩稿、R270B/C 的实际二阶消去及有限插值给
$$
G_\beta\in\mathcal G,\qquad \chi(G_\beta)=0.
\tag{3.2}
$$
这是实际共振累积量，不是一般普通慢 Bell 系数。

置
$$
\mathscr L=\sum_{2\le|\beta|\le D}
\frac{G_\beta}{\beta!}\partial_W^\beta,\qquad
P_0=e^{\mathscr L}Q_F,\qquad
P=P_0-\lambda I,
$$
$$
K(W)=P_0(W)-Q_F(W).
\tag{3.3}
$$
每个非零 $K$ 系数至少含一个 $G_\beta$；R151 的有限和积封闭保证它属于 $\mathcal G$ 且字符为零。
$K$ 是有限显示多项式，普通次数至多 $D-2$；$D=1$ 时 $K=0$。

R186 和完整生成恒等式给规范最大实现 $\mathsf P$，
$$
\mathsf P^*=C\mathsf PC,\qquad
\mathsf P e^w=[F(u_\rho)-\lambda]e^w.
\tag{3.4}
$$
全部真实原常数、倾斜及 Bell 项均保留。

为简写，下面省略固定 $\lambda$ 下标，将证书多项式记为
$A_{\mathrm{cert}}=A_\lambda$、$B_g=B_{g,\lambda}$，以区别原基础算子 $A$。

由 (2.1) 及 $P=Q_F-\lambda+K$，逐项得到
$$
\sum_gB_g\partial_gP
=1-A_{\mathrm{cert}}P+
A_{\mathrm{cert}}K+\sum_gB_g\partial_gK.
$$
定义
$$
\boxed{
E(W)=-A_{\mathrm{cert}}K-\sum_gB_g\partial_gK.
}
\tag{3.5}
$$
于是整个实际有限多项式有准确等式
$$
\boxed{
\sum_gB_g\partial_gP
=I-E-A_{\mathrm{cert}}P.
}
\tag{3.6}
$$
每个非零 $E$ 系数仍至少含一个 $G_\beta$，故属于 $\mathcal G$ 且字符为零。
(3.6) 使用原完整 $P$，没有把未知核换成某个尾多项式的核。

## 4. 精确次数预算和实际联合四次估计

记
$$
a=\max(0,\deg A_{\mathrm{cert}}),\qquad
b=\max_g\max(0,\deg B_g),\qquad
L_0=1+D+a+b.
\tag{4.1}
$$
零多项式在此按次数零作粗上界。
由 (3.5)，$\deg E\le L_0$。
令 $M=\ker\mathsf P$。

把原所有复一阶行拆成有限个实、虚正负部分，取非零正分量的实际最大增生 first $T_1,\ldots,T_J$。
对 $r\ge2$，取
$$
q_r=(8L_0+8)(r+1)^2,\qquad \epsilon_r=r^{-3},
$$
$$
\boxed{
\mathcal R_r=
\left[\prod_{\nu=1}^J(I+\epsilon_rT_\nu)^{-1}\right]^{q_r}.
}
\tag{4.2}
$$
这是全空间收缩，属于原 $A'$。
R186 的逐因子域计算和固定有界倾斜给
$$
\mathcal R_rH\subset\mathcal D_{q_r},\qquad
\|W^\gamma\mathcal R_r\|\le(C+Cr^3)^{|\gamma|}
\quad(|\gamma|\le q_r),
$$
$$
\mathcal R_r\longrightarrow I\text{ 强},\qquad
\mathcal R_rM\subset M.
\tag{4.3}
$$
强单位使用 $q_r\epsilon_r=O(r^{-1})$。
不假设整个 $M$ 预先属于一阶域，不把原复行共同域等同于正分量共同域。

将 $E$ 的固定有限非零系数列为 $E_1,\ldots,E_s$。
R151 的真实幂型给
$$
\|E_j^n\|\le C^ne^{-cn^4}.
$$
它们实际交换，所以
$$
\left\|\prod_jE_j^{n_j}\right\|
\le C^n e^{-c n^4/s^3},\qquad\sum_jn_j=n.
\tag{4.4}
$$
结合有限多项式展开及 (4.3)，得到
$$
\boxed{
\|E(W)^k\mathcal R_r\|
\le e^{-c_0k^4+C_0k\log(r+2)}
\qquad(0\le k\le r^2).
}
\tag{4.5}
$$
若 $E=0$，后续误差直接为零。
这里使用真实联合幂界，不从完整 $G_\beta$ 提出有界的原算子 $A$ 因子。

## 5. 原规范核中的多项式块近单位

令
$$
H_r(W)=\sum_{k=0}^{r-1}E(W)^k,\qquad
\widetilde B_{g,r}(W)=B_g(W)H_r(W).
$$
乘 (3.6)，得
$$
\boxed{
\sum_g\widetilde B_{g,r}\partial_gP
=I-E^r-A_{\mathrm{cert}}H_rP.
}
\tag{5.1}
$$
在原 $M$ 中的已付深域上，右端准确等于 $I-E^r$。

每个 $\widetilde B_{g,r}$ 的次数至多 $b+L_0(r-1)$。
$r$ 个块输入所消耗的原 first 字总数至多
$$
r[b+L_0(r-1)]\le L_0r^2.
\tag{5.2}
$$
加上 $P^r$、反射词和局部交换子只另需 $O(Dr)$ 层。
(4.2) 有明确余量。
这些系数一般不是全空间有界算子；只在右侧 $\mathcal R_r$ 已付的共同自然域上使用。

在 $K$ 个真实分离物理池中，每池 $N$ 位，取 $r=\lfloor\sqrt N\rfloor$。
任意跨池块的完整矩阵
$$
\Xi_B=(m_g(p_i))_{g,i}
$$
具有合并矩稿已付的统一逆费用
$\log^+\Delta_N^{-1}=O(\log N)$。
设 $u_i=t_{p_i}N_{p_i}$，真实一次反射系数为
$$
L_{p_i}=4\sum_gm_g(p_i)\partial_gP.
$$
取实际多项式块输入
$$
Q_B^{[r]}
=\frac14\sum_{i=1}^K
\left[\sum_g(\Xi_B^{-1})_{ig}\widetilde B_{g,r}\right]
\prod_{\ell\ne i}u_\ell.
\tag{5.3}
$$
由 (5.1)，其平方零顶部在原 $M$ 内恰为
$$
(I-E^r)\prod_i u_i.
$$
$r$ 个按原排序固定匹配的块，仍只有每块恰受一次提升能留在顶部。
故准确最高项为
$$
r!\,t_EN_E(I-E^r)^r\mathcal R_rf.
\tag{5.4}
$$
所有多项式输入在核内先形成，再施最左物理反射；没有移动到反射左侧。

(4.5) 给
$$
\boxed{
\|[(I-E^r)^r-I]\mathcal R_r\|
\le\sum_{j=1}^r\binom rj
e^{-c_0(rj)^4+C_0rj\log(r+2)}
\le e^{-c_1r^4}
}
\tag{5.5}
$$
对充分大 $r$ 成立。
最大幂 $r^2$ 和整个证书的最大次数都已由 (4.1)–(5.2) 支付。

## 6. 完整反射费用、局部四次界与排核

真实展开的输入系数及所有字范数满足
$$
\log A_N\le Cr\log N+Cr^2\log(r+2)=o(r^4).
\tag{6.1}
$$
常数现在允许依赖整个有限 Bézout 证书。
反射的仍是固定原 $P$；其明确实际 Bell 系数有原最高物理位壳及联合导数界。
右侧 (5.3) 只在已经支付的词域中使用，未给一般有界 $A'$ 系数附加未经证明的反射性质。

每个 first 字正规排序时只留在右侧或消耗为一次系数导数。
新增多项式字数为 $O(r^2)$，故联合阶乘、展开计数和正预解字范数至多产生 (6.1)。
选中位均在 $\mu N$ 之后，原真实 carry 和反射误差
$e^{-c16^{\mu N-1}}$ 压住这些费用。

与已证明的 Euler 近单位稿相同，原 $K$ 池平均及正确前因子
$(-1)^{Kr}(r!)^{K-1}(2/N)^{Kr}$ 给
$$
\mathsf P^r\mathcal V_N^{[r]}\mathcal R_rf
-\mathcal C_N(I-E^r)^r\mathcal R_rf\longrightarrow0,
$$
其中 $\mathcal C_N$ 一致有界且弱趋 $e^{-K/2}I$。
因此
$$
\boxed{
\mathsf P^r\mathcal V_N^{[r]}\mathcal R_rf
\rightharpoonup e^{-K/2}f
\qquad(f\in M).
}
\tag{6.2}
$$
(5.5) 只乘已归一后的一致有界纯平均，不乘增长的输入费用。

固定有限局部全矩阵 $D_0$。
只对真实有限头有
$$
P=P_{\mathrm{tail},h}+A\,U_h,\qquad\deg U_h\le D,
$$
此处 $A$ 是原基础算子。
保留交换子展开两侧的原 $A^j,A^{r-j}$ 后，原实际四次界给
$$
\|(\operatorname{ad}_P^rD_0)\mathcal V_N^{[r]}\mathcal R_rf\|
\le
e^{-5r^4/6+105r^3+Cr^2\log(r+2)+Cr\log N}\|f\|
\longrightarrow0.
\tag{6.3}
$$
全部自然字在 (4.2) 的范围内。

对 $f,g\in M$，原全 $H$ 上的完整 $C$ 对称与 $\mathsf Pg=0$ 给
$$
B(D_0\mathsf P^r\mathcal V_N^{[r]}\mathcal R_rf,g)
=(-1)^rB((\operatorname{ad}_P^rD_0)
\mathcal V_N^{[r]}\mathcal R_rf,g).
$$
用 (6.2)–(6.3) 得 $B(D_0f,g)=0$ 对全部局部全矩阵。
其不可约性迫 $M=0$。
完整 $C$ 自伴性及原 $e^w$ 图核心给稠密值域和 (1.4)。

这证明了每个具有有限证书 (2.1) 的正则纤维，且所有新域费用已经由明确的 $L_0$ 计算支付。

## 7. 临界值为什么只有有限个

本节独立证明所需有限性，不将标量临界值定理作为未说明假设。

设 $Q\in\mathbb C[W_1,\ldots,W_K]$ 为任意有限多项式，
$$
V=\{z:\partial_1Q(z)=\cdots=\partial_KQ(z)=0\}.
$$
若 $V$ 为空，结论成立。
否则 $V$ 是 Noetherian 仿射代数集，具有有限多个不可约分量 $V_1,\ldots,V_m$。
有限不可约分量的标准拓扑依据是 Stacks Project
[Lemma 5.9.2，tag 0052](https://stacks.math.columbia.edu/tag/0052)。

固定一个分量，令
$$
\mathbb K_i=\operatorname{Frac}(\mathbb C[W]/I(V_i)).
$$
这是特征零的有限生成域扩张。
原所有 $\partial_jQ$ 在该域中为零。
记 $q$ 为 $Q$ 的像；对任意 $\mathbb C$ 导子 $\delta$，链式法则给
$$
\delta q=\sum_j\overline{\partial_jQ}\,\delta\overline W_j=0.
\tag{7.1}
$$

以下给出微分常数的自含域论证。
若 $q\notin\mathbb C$，因 $\mathbb C$ 代数闭，$q$ 对 $\mathbb C$ 必超越。
可以将 $q$ 扩充成有限超越基
$q,t_2,\ldots,t_d$；$\mathbb K_i$ 是
$\mathbb C(q,t_2,\ldots,t_d)$ 的有限代数扩张。
特征零保证此扩张可分。

在基域上取通常导子 $\partial/\partial q$，它在 $q$ 上取值1、在其他基变量上取值0。
此导子可以扩到每个有限可分代数扩张：
若 $\alpha$ 的极小多项式为 $p(X)$，令
$$
\delta\alpha=-\frac{(\delta p)(\alpha)}{p'(\alpha)}.
\tag{7.2}
$$
可分性保证分母非零；先在 $L[X]$ 上扩导子并令 $X$ 的像取 (7.2)，则理想 $(p)$ 被保持，故导子下传到 $L[\alpha]$ 再扩至其分式域。
对有限代数生成元逐次进行，即得到 $\mathbb K_i$ 上的导子。
这与 (7.1) 冲突，因为它在 $q$ 上取值1。

故 $q\in\mathbb C$，即 $Q$ 在 $V_i$ 上恒等于某个标量 $c_i$。
每个分量至少有一个复点，因而其像恰为 $\{c_i\}$。
所以
$$
\boxed{Q(V)=\{c_1,\ldots,c_m\}}
\tag{7.3}
$$
是有限集。
应用于 (1.2) 即证明 $\Sigma_F$ 有限。

例如可由临界理想加方程 $t-Q_F$ 的消元求出一个非零一变量多项式，所有 $\Sigma_F$ 均在其零点中。
本证明只用有限性和各个正则参数的证书，不声称证书次数或系数在临界值附近一致有界。

## 8. 一个无齐次前提的明确目标

取原正实指数 $1,2,3,4,5$，令
$$
g_1=x_1x_5-\frac58x_2x_4,\qquad
g_2=x_2x_5-\frac56x_3x_4,
$$
$$
F=g_1^2+g_2^2+x_1.
\tag{8.1}
$$
这是具体的非普通齐次目标。
其最高普通齐次部分在原曲线上自身及梯度均为零。
又 $g_1^2$、$g_2^2$ 和 $x_1$ 的 $(d,s)$ 分别是 $(4,8)$、$(4,10)$、$(1,0)$；
若试图用 $ad+bs=\delta\ne0$，前两项迫 $b=0$，再比较最后一项迫 $a=0$，矛盾。
因此不能仅靠该显式 Euler 权条件处理整个 (8.1)。

本定理仍给一个有限、与 $w$ 无关的精确代数集合 $\Sigma_F$，使所有 $\lambda\notin\Sigma_F$ 的
$$
\left[
\left(u_1u_5-\frac58u_2u_4\right)^2+
\left(u_2u_5-\frac56u_3u_4\right)^2+u_1-\lambda
\right]e^w
\tag{8.2}
$$
非零且循环。

为使这里的例外集合完全具体，可以把 (1.2) 写成更小的有限矩阵多项式。
令 $x_\nu=\nu W_{1,\nu-1}$，取实对称矩阵 $B_i$ 使 $g_i(x)=x^{\mathsf T}B_i x$。
对九个独立二阶键变量置
$$
C_{\nu\mu}=-\nu\mu\,W_{2,\nu+\mu-2},
\qquad 1\le\nu,\mu\le5.
\tag{8.3}
$$
因为 $g_i(\nu t^\nu)=0$，准确有 $\operatorname{tr}(B_iC)=0$。
同时 $g_i(x+t v)$ 对 $t$ 至多一次，故 $F_4=g_1^2+g_2^2$ 的所有第三、第四物理方向偏导为零。
不同键的指数独立性使相应完整三阶、四阶矩系数也为零。

由 (1.2) 的有限微分指数，得到
$$
\boxed{
Q_F=
g_1(x)^2+g_2(x)^2+x_1
+8\sum_{i=1}^2x^{\mathsf T}B_iCB_i x
+8\sum_{i=1}^2\operatorname{tr}((B_iC)^2).
}
\tag{8.4}
$$
核验系数：二阶微分算子为
$\sum_{\nu,\mu}C_{\nu\mu}\partial_{x_\nu}\partial_{x_\mu}$；
它作用于 $g_i^2$ 给 $8x^{\mathsf T}B_iCB_ix$，再作用一次给
$16\operatorname{tr}((B_iC)^2)$，指数中的 $1/2!$ 给最后的8。
所有更高作用为零。

于是此例的 $\Sigma_F$ 正是 (8.4) 这个十四变量多项式的临界值集；更高键是未出现的自由变量，不改变该集合。
本节的一般判据只给有限例外；后续 §11 的显式完整向量场已进一步证明此例的临界集为空，零参数因而也已关闭。
新增的完整结论是对这个原具体目标及任意其他有限 $F$，所有可能未闭的标量参数均落在一个有限的、独立于 $w$ 的代数集合中。

## 9. 量词、已有范围与尚未解决的问题

对于任意固定非恒定一变量 $Q_{\rm out}$，可以把整个
$G=Q_{\rm out}\circ F$ 当作新的原普通多项式，重做 (1.2)–(1.3)。
因此
$$
[Q_{\rm out}(F(u))-\lambda]e^w
$$
对除有限集合 $\Sigma_G$ 外的全部 $\lambda$ 循环。
这不表示 $Q_{\rm out}(F(u))e^w$ 的零纤维必然已闭，也不把不同目标的有限集合混成一个统一有限集。

若 $F$ 或其完整矩逆具有已付的非零常数方向，临界集为空，恢复已有全参数结论。
若完整矩逆是非零权齐次的，Euler 恒等式使临界值只能为零，恢复上一稿。
本稿新增的是不要求任何齐次结构的任意有限普通目标的正则纤维和有限例外范围。

不从这些循环向量的稠密性宣称每个 $L^2$ 向量循环，不把一般正常见证预算或原连续尾 Schur 比较视为已完成。
普通复 Hilbert ISP 仍然开放。

## 10. 完整依赖

- [合并复对数矩稿](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)：原中心、全部矩比例、有限普通逆、实际 Bell 及跨池统一逆费用。
- [Euler 二次深度近单位稿](R150-appendix-homogeneous-nonzero-fibers-fast-bell-euler-and-quadratic-depth-near-units.md) §§3–7：真实联合四次预算、增长的多项式输入、完整顶部、反射和局部配对；本稿明确把次数常数增为 (4.1)。
- [R151](R151-quartic-analytic-approximation-gauge-stability.md)、[R270B](R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md)、[R270C](R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md)：(3.2)、(4.4) 的真实快系数与幂型。
- [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)、[增长正预解引理](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)：原规范核、正分量共同词域及全 $C$ 自伴。
- Stacks Project [Theorem 10.34.1 / 00FV](https://stacks.math.columbia.edu/tag/00FV) 与 [Lemma 5.9.2 / 0052](https://stacks.math.columbia.edu/tag/0052)：单位理想和有限不可约分量；所需特征零函数域导子论证已在 §7 全部给出。

## 11. 独立补充：一个显式多项式向量场消去完整矩梯度，关闭上述例子的零参数

本节单独升级 §8 的具体例子；normal_resume_1cf 与 Astra-ISP-1cf8c51d 已逐项核完九个二阶系数、二次型及向量场恒等。证明给出整个完整矩多项式的有限单位证书，不仅说明其临界值有限。

### 11.1 原实际目标及全参数结论

保留原五个正实指数 $1,2,3,4,5$ 和固定中心，简写
$$
U_\nu=\frac{u_\nu}{\nu}\qquad(1\le\nu\le5).
$$
只是对原模式作固定非零标量倍，不改变任何中心常数。
在显示变量 $y=(a,b,c,d,e)$ 中定义
$$
g_A=ae-bd,\qquad g_B=be-cd.
$$
取任意
$$
\alpha,\beta\in\mathbb C\setminus\{0\},
\qquad
\ell(y)=\ell_0+\ell_1a+\ell_2b+\ell_3c+\ell_4d+\ell_5e,
$$
并令
$$
F(y)=\alpha g_A(y)^2+\beta g_B(y)^2+\ell(y).
\tag{11.1}
$$
假设
$$
\boxed{\delta=\ell_1+\frac{\alpha}{\beta}\ell_3\ne0.}
\tag{11.2}
$$

**全参数结论。** 对每个 $\lambda\in\mathbb C$，包括 $\lambda=0$，以及每个复平方可和指数权 $w$，
$$
\boxed{[F(U_1,\ldots,U_5)-\lambda]e^w
\text{ 非零且对实际 }A\text{ 循环}.}
\tag{11.3}
$$
本节允许两个四次系数为任意非零复数。
它不从 (11.3) 自动推出 $[F(U)-\lambda]^h$ 或一般外层点态复合；那些目标仍需重做完整矩逆。

### 11.2 完整矩逆的准确有限表达

一次键变量正是 $y_\nu=W_{1,\nu-1}$。
记九个二阶键为
$$
w_j=W_{2,j},\qquad 0\le j\le8.
$$
全部高于二阶的键在本次完整矩逆中不出现。
原因是对每个物理曲线方向
$$
v(t)=(1,t,t^2,t^3,t^4)
$$
都有 $g_A(v(t))=g_B(v(t))=0$，所以
$g_i(y+sv(t))$ 关于 $s$ 至多一次，$g_i(y+sv(t))^2$ 至多二次。
完整三阶、四阶物理方向导数为零，按不同指数键的线性独立性，所有对应合并矩系数准确为零。

令
$$
C_{ij}=-w_{i+j-2}\qquad(1\le i,j\le5).
$$
这是一个对称 Hankel 矩阵；这里只是有限显示多项式，不是原 Hilbert 共轭 $C$。
取对称标量矩阵 $B_A,B_B$ 使 $g_i(y)=y^{\mathsf T}B_i y$。
有
$$
\operatorname{tr}(B_A C)=\operatorname{tr}(B_B C)=0.
$$

把
$$
\alpha y^{\mathsf T}B_A C B_Ay+
\beta y^{\mathsf T}B_B C B_By
=-\sum_{j=0}^8L_j(y)w_j,
$$
$$
\mathcal H(w)=
\alpha\operatorname{tr}((B_A C)^2)+
\beta\operatorname{tr}((B_B C)^2).
$$
§8 的完整有限 Bell 逆计算给
$$
\boxed{
Q_F(y,w)=
\alpha g_A^2+\beta g_B^2+\ell(y)
-8\sum_{j=0}^8L_j(y)w_j+8\mathcal H(w).
}
\tag{11.4}
$$
特别这不是只把原 $F$ 视为实际算子多项式后删掉 Bell 项。

为可直接核验，全部系数为
$$
\begin{aligned}
L_0&=\alpha e^2/4,&
L_1&=-\alpha ed/2,\\
L_2&=\alpha d^2/4+\beta e^2/4,&
L_3&=-\alpha eb/2-\beta ed/2,\\
L_4&=\alpha(ea+db)/2+\beta d^2/4-\beta ec/2,&
L_5&=-\alpha da/2+\beta(eb+dc)/2,\\
L_6&=\alpha b^2/4+\beta c^2/4-\beta db/2,&
L_7&=-\alpha ab/2-\beta cb/2,\\
L_8&=\alpha a^2/4+\beta b^2/4.
\end{aligned}
\tag{11.5}
$$
二次型是
$$
\begin{aligned}
\mathcal H(w)
={}&\alpha\left[
w_4^2+\frac12w_0w_8+\frac12w_2w_6-w_1w_7-w_3w_5
\right]\\
&+\beta\left[
w_5^2+\frac12w_2w_8-\frac12w_4w_6-w_3w_7
\right].
\end{aligned}
\tag{11.6}
$$
这些式子也可以从五维矩阵乘法直接展开取得。

### 11.3 真实完整多项式的单位向量场

定义只作用于上述十四个显示变量的多项式向量场
$$
\boxed{
\mathscr V=
\partial_a+\frac{\alpha}{\beta}\partial_c
+\left(a-\frac{\beta}{\alpha}c\right)\partial_{w_0}
+b\,\partial_{w_1}+c\,\partial_{w_2}.
}
\tag{11.7}
$$
它的系数只有常数或一次多项式，且作用于真实合并后的键。
不指定不兼容的原重复矩方向。

令
$$
v=\partial_a+\frac{\alpha}{\beta}\partial_c,\qquad
\eta=\left(a-\frac{\beta}{\alpha}c,\ b,\ c\right).
$$
从 (11.5) 逐项有
$$
vL_j=0\quad(0\le j\le5),\qquad
(vL_6,vL_7,vL_8)=\left(\frac{\alpha c}{2},-\alpha b,\frac{\alpha a}{2}\right).
\tag{11.8}
$$
从 (11.6) 有
$$
\partial_{w_0}\mathcal H=\frac{\alpha}{2}w_8,\quad
\partial_{w_1}\mathcal H=-\alpha w_7,\quad
\partial_{w_2}\mathcal H=\frac{\alpha}{2}w_6+\frac{\beta}{2}w_8.
$$
因此
$$
\eta\cdot(\partial_{w_0},\partial_{w_1},\partial_{w_2})\mathcal H
=\sum_j(vL_j)w_j.
\tag{11.9}
$$
这使 (11.4) 中全部含 $w$ 的导数项准确相消。

余下常数于 $w$ 的部分同样准确相消：
$$
\eta_0L_0+\eta_1L_1+\eta_2L_2
=\frac{\alpha}{4}(ae^2-2bde+cd^2),
$$
$$
v(\alpha g_A^2+\beta g_B^2)
=2\alpha(eg_A-dg_B)
=2\alpha(ae^2-2bde+cd^2).
\tag{11.10}
$$
最后 $v\ell=\delta$。将 (11.9)–(11.10) 代入 (11.4)，得到整个标量有限多项式恒等式
$$
\boxed{\mathscr VQ_F=\delta.}
\tag{11.11}
$$
(11.11) 对任意十四变量的取值成立，不只在一个曲线点或未知核上成立。

它就是 §2 的显式 Jacobian 证书：取 $A_{\mathrm{cert}}=0$，
并把 (11.7) 的五个系数除以 $\delta$ 作为相应 $B_g$，其他键系数置零。
所以 $Q_F$ 根本没有临界点，$\Sigma_F=\varnothing$。

### 11.4 从证书到实际算子的范围

将 (11.11) 接入 §§3–6 的实际 Bell 及近单位证明。
所有证书系数次数至多1；可以取其中 $L_0=1+4+0+1=6$，
同一正分量预解支付全部二次增长词深。
真实修正 $K=e^{\mathscr L}Q_F-Q_F$ 没有被删掉；
它进入
$$
E=-\sum_g B_g\partial_gK,
$$
其系数仍是真实快类零字符元。
原规范核上的有限近单位、完整反射及原 $C$ 配对均适用。
因此 (11.3) 对所有 $\lambda$ 和所有原权 $w$ 成立。
没有将 (11.7) 的多项式系数假称为全空间有界算子。

### 11.5 §8 原例的全部参数现已关闭

取
$$
\alpha=25,\qquad\beta=100,\qquad\ell(y)=a.
$$
则 $\delta=1$，并且
$$
5g_A(U)=u_1u_5-\frac58u_2u_4,\qquad
10g_B(U)=u_2u_5-\frac56u_3u_4.
$$
所以
$$
\boxed{
\left[
\left(u_1u_5-\frac58u_2u_4\right)^2+
\left(u_2u_5-\frac56u_3u_4\right)^2+u_1-\lambda
\right]e^w
}
\tag{11.12}
$$
对全部 $\lambda\in\mathbb C$，包括零参数，都非零且循环。

这里的最高普通四次部分沿原曲线及其全部梯度都为零；
全参数结论来自 (11.11) 的完整多项式证书。
本节没有声称该结论仅靠原 $F$ 的平滑性即可取得，也没有把两个平方项的已知循环性相加。

## 12. 后续独立计算：同一四次族的全部临界值与任意非零线性扰动的零纤维

本节精确计算 §11 四次族的完整合并矩临界集。
所有换元只发生在有限标量多项式 $Q_F$ 中；不把它们当作原闭算子的非线性相似或自然域等式。
算子结论最后只通过已经证明的原 Jacobian 证书定理取得。

### 12.1 允许的参数及记号

使用原 $U_\nu=u_\nu/\nu$，令
$$
F(y)=\alpha(ae-bd)^2+\beta(be-cd)^2+\ell(y),
\qquad
\alpha\ne0,\quad \beta\in\mathbb C,
$$
$$
\ell(y)=\ell_0+\ell_1a+\ell_2b+\ell_3c+\ell_4d+\ell_5e,
\qquad \tau=\beta/\alpha.
\tag{12.1}
$$
这次允许 $\beta=0$。
仍令 $w_j=W_{2,j}$，$0\le j\le8$。
从 (11.4)–(11.6) 提出 $\alpha$，记
$$
G=(ae-bd)^2+\tau(be-cd)^2,\qquad
L_j=L_j^{(\alpha=1,\beta=\tau)},
$$
$$
H=H^{(\alpha=1,\beta=\tau)}.
$$
则准确的完整矩逆是
$$
Q_F=\alpha\left[G-8\sum_jL_jw_j+8H(w)\right]+\ell(y).
\tag{12.2}
$$

### 12.2 九个矩变量的准确完成平方

$H$ 的 Hessian 记为 $J$，所以 $H(w)=\tfrac12w^{\mathsf T}Jw$。
对任意给定列 $L=(L_0,\ldots,L_8)^{\mathsf T}$，方程
$Jw_*=L$ 可以按以下顺序唯一解出：
$$
\begin{aligned}
(w_*)_8&=2L_0,&
(w_*)_7&=-L_1,\\
(w_*)_6&=2L_2-\tau(w_*)_8,&
(w_*)_5&=-L_3-\tau(w_*)_7,\\
(w_*)_4&=\tfrac12L_4+\tfrac{\tau}{4}(w_*)_6,&
(w_*)_3&=2\tau(w_*)_5-L_5,\\
(w_*)_2&=2L_6+\tau(w_*)_4,&
(w_*)_1&=-L_7-\tau(w_*)_3,\\
(w_*)_0&=2L_8-\tau(w_*)_2.
\end{aligned}
\tag{12.3}
$$
因此 $J$ 对每个复 $\tau$ 都可逆；没有除以 $\tau$。
所有 $(w_*)_j$ 都是 $y$ 的二次多项式。

为直接核验完成平方的剩余项，可以把 $Z_j=4(w_*)_j$ 写成
$$
\begin{aligned}
Z_8&=2e^2,&Z_7&=2ed,&Z_6&=2d^2,&Z_5&=2eb,\\
Z_4&=ea+db+\tau d^2-\tau ec,\\
Z_3&=2da+2\tau eb-2\tau dc,\\
Z_2&=2b^2+2\tau c^2-3\tau bd+\tau ae+\tau^2d^2-\tau^2ce,\\
Z_1&=2ab+2\tau cb-2\tau da-2\tau^2eb+2\tau^2dc,\\
Z_0&=2a^2-2\tau^2c^2+3\tau^2bd-\tau^2ae-\tau^3d^2+\tau^3ce.
\end{aligned}
\tag{12.4}
$$
令
$$
h(y)=ae-bd-\tau(ce-d^2).
$$
代入 (11.5) 的 $L_j$ 和 (12.4)，逐项展开给
$$
\boxed{
4G-\sum_{j=0}^8(4L_j)Z_j=-2h(y)^2.
}
\tag{12.5}
$$
这是有限整数系数恒等式；把 $\tau$ 也视为独立变量即可核验全部系数。
由 $Jw_*=L$，
$$
8H(w)-8L^{\mathsf T}w
=8H(w-w_*)-4L^{\mathsf T}w_*.
$$
所以 (12.5) 准确给出
$$
\boxed{
Q_F=8\alpha H(w-w_*)-\frac{\alpha}{2}h(y)^2+\ell(y).
}
\tag{12.6}
$$

### 12.3 纯标量三角坐标与临界点方程

现在只在标量多项式环中作
$$
z=w-w_*(y),\qquad r=a-\tau c.
$$
该变换是多项式可逆的：先由 $(r,b,c,d,e)$ 还原 $a=r+\tau c$，再由 $w=z+w_*(y)$ 还原矩变量。
因此它保持临界点与临界值，且无需讨论任何实际无界算子的图。

记
$$
m=\tau\ell_1+\ell_3,\qquad
x=(r,b,d,e)^{\mathsf T},\qquad
l=(\ell_1,\ell_2,\ell_4,\ell_5)^{\mathsf T},
$$
$$
h(x)=re-bd+\tau d^2=x^{\mathsf T}Bx,
$$
其中
$$
B=
\begin{pmatrix}
0&0&0&1/2\\
0&0&-1/2&0\\
0&-1/2&\tau&0\\
1/2&0&0&0
\end{pmatrix}.
\tag{12.7}
$$
此矩阵对全部复 $\tau$ 都可逆。
(12.6) 变成
$$
\boxed{
Q_F=8\alpha H(z)-\frac{\alpha}{2}h(x)^2+l^{\mathsf T}x+mc+\ell_0.
}
\tag{12.8}
$$

临界方程首先给 $z=0$，因为 $J$ 可逆。
若 $m\ne0$，对 $c$ 的偏导已经非零，所以没有临界点。

以下设 $m=0$。
对剩余四个变量，方程是
$$
l=2\alpha h(x)Bx.
\tag{12.9}
$$
定义
$$
\boxed{
\Delta=\ell_1\ell_5-\ell_2\ell_4-\tau\ell_2^2.
}
\tag{12.10}
$$
由 (12.7) 的直接逆矩阵，
$$
l^{\mathsf T}B^{-1}l=4\Delta.
\tag{12.11}
$$

如果 $l=0$，(12.9) 迫 $h(x)=0$：
若 $h\ne0$，可逆 $B$ 先迫 $x=0$，再与 $h\ne0$ 矛盾。
反之每个 $h=0$ 的点都是临界点。
它们的值都等于 $\ell_0$。

若 $l\ne0$，则临界点必有 $h\ne0$，并且
$$
x=\frac{1}{2\alpha h}B^{-1}l.
$$
代入 $h=x^{\mathsf T}Bx$，得到
$$
\boxed{h^3=\Delta/\alpha^2.}
\tag{12.12}
$$
当 $\Delta=0$ 时没有这样的非零 $h$，故没有临界点。
当 $\Delta\ne0$ 时，每个三次根都给一个真实的 $x$，并且代回确实满足全部临界方程。
变量 $c$ 自由，没有额外临界值。

在 (12.9) 上，
$$
l^{\mathsf T}x=2\alpha h^2.
$$
因此相应临界值是
$$
\lambda=\ell_0+\frac{3\alpha}{2}h^2,
\qquad
(\lambda-\ell_0)^3=\frac{27\Delta^2}{8\alpha}.
\tag{12.13}
$$
$\Delta\ne0$ 时三个值两两不同。

### 12.4 精确临界集与实际循环性

由以上完整计算，(1.3) 的准确临界值集合为
$$
\boxed{
\Sigma_F=
\begin{cases}
\varnothing,&m\ne0,\\
\varnothing,&m=0,\ l\ne0,\ \Delta=0,\\
\{\lambda:(\lambda-\ell_0)^3=27\Delta^2/(8\alpha)\},
&m=0,\ \Delta\ne0,\\
\{\ell_0\},&m=0,\ l=0.
\end{cases}
}
\tag{12.14}
$$
最后一行等价于整个线性部分为零，因为此时也有
$\ell_3=m-\tau\ell_1=0$。

对所有 $\lambda\notin\Sigma_F$，原实际
$$
[F(U_1,\ldots,U_5)-\lambda]e^w
$$
非零且循环，对任意复平方可和 $w$ 成立。
这是对原规范 Bell 的结论；§12.3 的标量换元没有被作为算子代换。

特别，若
$$
\ell_0=0,\qquad
(\ell_1,\ldots,\ell_5)\ne0,
$$
则无论处于 (12.14) 的哪一种情况，均有 $0\notin\Sigma_F$：
非空的三次集合此时三个值都非零，而最后一行不可能发生。
所以得到完整零参数推论
$$
\boxed{
\left[
\alpha(U_1U_5-U_2U_4)^2+
\beta(U_2U_5-U_3U_4)^2+
\sum_{\nu=1}^5\ell_\nu U_\nu
\right]e^w
\text{ 非零且循环}
}
\tag{12.15}
$$
只需 $\alpha\ne0$、$\beta$ 任意，以及非零线性部分。

例如取 $\alpha=\beta=1$、$\ell=b$，则
$m=0$、$\Delta=-1$。
此时 $F=(ae-bd)^2+(be-cd)^2+b$ 没有 §11 的非零常数方向 (11.2)，
但其准确候选例外仅为
$$
\lambda^3=27/8.
$$
因此零参数已经由 (12.15) 排除。
不声称这三个实际非零参数必然有核；只是当前完整 Jacobian 证书没有覆盖它们。

本节仍不把 $(F-\lambda)^h$ 的完整矩逆视为 $(Q_F-\lambda)^h$，也不据此扩张一般点态幂。

## 13. 独立加强：最低指数的唯一矩键、三个标量临界值与全部普通点态复合

本节使用一个实际闭算子的全域逆，覆盖 §§11–12 四次族的全部参数和全部外层多项式。
§12 对完整标量矩逆的临界集计算保持准确；但该有限集不再表示这个实际四次族尚未解决的参数。
这里没有使有临界点的标量多项式突然具有 Jacobian 单位证书，而是使用另一条已证明的实际偏导逆接口。

### 13.1 最低实指数的唯一纯矩键

先记录与最大指数同样合法的另一端。
取原实际参与的有限正实指数
$$
0<\rho_1<\cdots<\rho_q.
$$
对任意正整数 $k$，
$$
|\omega|=k,\qquad \sum_\nu\rho_\nu\omega_\nu=k\rho_1
\quad\Longrightarrow\quad \omega=ke_1.
\tag{13.1}
$$
因为
$\sum_{\nu>1}(\rho_\nu-\rho_1)\omega_\nu=0$，
每个系数都严格为正。
因此完整合并矩表中的键
$$
(k,k\rho_1-k)
$$
只有这个纯多重指标。
不同总度始终属于不同键。
这不要求其他高矩彼此独立，也不拆开任何已经合并的重复行。

取任意原普通多项式
$$
F(x)=a(x_>)x_1^t+\sum_{j<t}a_j(x_>)x_1^j,
\qquad t\ge1,\quad a\ne0,
\tag{13.2}
$$
以及外层 $Q(z)=q_hz^h+\cdots$、$q_h\ne0$、$h\ge1$。
对整个 $G=Q\circ F$，令 $k=th$。
准确有
$$
\partial_{x_1}^kG=k!\,q_h a^h.
\tag{13.3}
$$
完整普通转共振生成式给
$$
\partial_{Y_\omega}\mathcal Q_G
=\frac{(-2)^{|\omega|-1}}{\omega!}
\mathcal Q_{\partial^\omega G}.
\tag{13.4}
$$
由 (13.1)，合并后的真实唯一坐标满足
$$
\boxed{
\partial_{W_{k,k\rho_1-k}}Q_G
=\rho_1^k(-2)^{k-1}q_h Q_{a^h}.
}
\tag{13.5}
$$
若把每个原模式预先除以其固定非零系数 $\rho_\nu$，
相应物理行变为
$(p+2)^{-1}(\log(p+2))^{\rho_\nu-1}$；
这时 (13.5) 中的 $\rho_1^k$ 同样准确消失。
所有原固定中心也随同一个标量缩放，不能另外重置。

完整实际共振 Bell 修正的系数独立于显示变量 $W$，
所以它与 (13.5) 的偏导交换。
因此，只要原 $a(u)^he^w$ 的完整 ordinary Bell 规范实现
$\mathsf B_{a^h,w}$ 具有全域有界逆
$$
\mathsf B_{a^h,w}^{-1}\in\{A\}',
\tag{13.6}
$$
此纯矩偏导的真实规范实现也有全域有界交换逆。

(13.6) 可以由已发表的
[矩形 Bell 逆稿](R150-appendix-rectangular-bell-inverses-and-nonmonic-largest-logarithmic-modes.md)
§§2–5 支付：允许 $a$ 是较大模式中有限个实线性 first 加复常数组成的矩形顶项多项式。
其余 $a_j$ 不受矩形条件限制。
这里只将原稿最大指数的键唯一性改为已经证明的 (13.1)；
原真实图、逆和反射预算均不改变。

### 13.2 四次族的最高低指数系数

继续使用原固定中心
$$
U_\nu=u_\nu/\nu,\qquad \nu=1,\ldots,5,
$$
并在显示变量 $y=(a,b,c,d,e)$ 中取
$$
F(y)=\alpha(ae-bd)^2+\beta(be-cd)^2+\ell(y),
$$
$$
\alpha\in\mathbb C\setminus\{0\},\qquad
\beta\in\mathbb C,\qquad
\ell(y)=\ell_0+\ell_1a+\ell_2b+\ell_3c+\ell_4d+\ell_5e.
\tag{13.7}
$$
没有实系数限制，没有对 $\ell$ 的非退化要求。

对最低变量 $a$，这个多项式准确为
$$
F(y)=\alpha e^2a^2+(\ell_1-2\alpha ebd)a
+\alpha b^2d^2+\beta(be-cd)^2+
\ell_0+\ell_2b+\ell_3c+\ell_4d+\ell_5e.
\tag{13.8}
$$
故对每个固定非零外层 $Q$、$h=\deg Q\ge1$，
$$
\boxed{\partial_a^{2h}Q(F)=(2h)!\,q_h\alpha^h e^{2h}.}
\tag{13.9}
$$
最低键 $(2h,0)$ 在全部原模式中唯一。
(13.4)–(13.5) 因而给完整合并矩恒等式
$$
\boxed{
\partial_{W_{2h,0}}Q_{Q\circ F}
=(-2)^{2h-1}q_h\alpha^h\,Q_{e^{2h}}.
}
\tag{13.10}
$$
此式保留 $Q(F)$ 的全部普通 Bell，而非对 $Q_F$ 作形式幂运算。

对原任意复平方可和权 $w$，真实偏导因此为
$$
\boxed{
\mathsf D_h=(-2)^{2h-1}q_h\alpha^h\,
\mathsf B_{U_5^{2h},w}.
}
\tag{13.11}
$$
右端的规范图是原点态向量 $U_5^{2h}e^w$ 的完整 ordinary Bell 图。
以下逐项说明其实际逆和域。

### 13.3 单个正 first 的完整 Bell 逆及两个规范图的一致性

令 $X_+$ 为原正、未居中的第五归一行
$$
\sum_{p\ge0}\frac{(\log(p+2))^4}{p+2}\chi_p
$$
的 first。
其行正、平方可和且不可和。
[R134](R134-empty-spectrum-first-chaos-polynomial-cyclicity.md)
与实际计数半群稿给它的空谱及全平面预解。
原 $U_5$ 的常数和全部复权倾斜形成真实有界交换扰动，
所以实际一阶为
$$
T=X_++H_w,\qquad H_w\in\{A\}'\cap B(H),
\qquad \operatorname{Dom}T=\operatorname{Dom}X_+.
\tag{13.12}
$$
这里的倾斜级数按原行与 $w$ 的 $\ell^2\times\ell^2$ 估计范数绝对收敛。

记 $L_0=X_+^{-1}$。
它是有界、单射、稠密像的拟幂零元，且属于 $\{A\}'$。
$H_wL_0$ 也拟幂零，因此 $I+H_wL_0$ 是真实有界单位。
在完整一阶域上，
$$
\boxed{
T^{-1}=L_0(I+H_wL_0)^{-1}\in\{A\}'.
}
\tag{13.13}
$$
任意复标量平移同理，故 $T$ 空谱，$L=T^{-1}$ 拟幂零。
不使用一般的“有界扰动保持空谱”断言。

对固定 $m=2h$，完整单模式 Bell 是
$$
\mathsf B_m=T^m+\sum_{j<m}C_jT^j,
\qquad C_j\in\{A\}'\cap B(H).
\tag{13.14}
$$
系数都是原实际 Bell 系数，并未删去。
自然幂的整个域准确为
$$
\operatorname{Dom}T^m=\operatorname{Ran}L^m,\qquad T^m=(L^m)^{-1}.
\tag{13.15}
$$
在这个域上，
$$
\mathsf B_m=
\left(I+\sum_{j<m}C_jL^{m-j}\right)T^m.
$$
括号内的非恒定部分是有限个彼此交换的拟幂零项之和，仍拟幂零。
所以
$$
\boxed{
\mathsf B_m^{-1}
=L^m\left(I+\sum_{j<m}C_jL^{m-j}\right)^{-1}
\in\{A\}'.
}
\tag{13.16}
$$
(13.14) 因而在 (13.15) 的完整域上闭且满射。

自然实现与规范图的相等也已经支付。
同一 R186 正分量共同正则器 $R(s)^N$，$N\ge m$，
保持自然域且对 $x\in\operatorname{Dom}T^m$ 有
$$
R(s)^Nx\to x,\qquad T^mR(s)^Nx=R(s)^NT^mx\to T^mx.
$$
所以共同有限词域为 $T^m$ 的图核心；
(13.14) 左侧有界单位使同一集合也是 $\mathsf B_m$ 的图核心。
它的闭包就是原单模式规范 Bell 实现。

另一方面，(13.11) 最初从较大的完整合并矩表得到。
其原 $e^w$ 多项式轨道上的作用与上述单模式实现相同，均给
$U_5^me^w$ 及其 $p(A)$ 轨道。
R186 的规范图核心遂识别两个完整闭图。
所以 (13.16) 确实是 (13.11) 所需的原真实偏导逆，而不是在某个较小核心上碰巧成立的形式逆。

### 13.4 逆只放在右输入，原核与反射预算全部保持

对本次整个 $G=Q\circ F$，令
$M=\ker\mathsf P_{G,w}$。
由 (13.11)、(13.16)，
$$
\mathsf D_h^{-1}
=\bigl[(-2)^{2h-1}q_h\alpha^h\bigr]^{-1}
\mathsf B_{2h}^{-1}\in\{A\}'.
\tag{13.17}
$$
R186 的原有界核方程保证它保持 $M$；
同一交换域结论保证它保持所有所需正分量和原倾斜 first 的有限自然词域。

现在使用
[全域偏导逆稿](R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md)
§2 的原矩阵块接口。
记每块完整物理行矩阵为 $\Xi_B$，
选择该唯一键的坐标向量 $e_*$，并取
$$
b=\frac14\Xi_B^{-1}e_*,
\qquad
Q_B=\mathsf D_h^{-1}\sum_i b_i\prod_{j\ne i}t_{p_j}N_{p_j}.
\tag{13.18}
$$
完整一次反射系数为
$L_{p_i}=4\sum_gm_g(p_i)\partial_gP$。
于是在已付深域内，
$\sum_i b_iL_{p_i}=\mathsf D_h$，
每块平方零顶部通过
$\mathsf D_h\mathsf D_h^{-1}=I$ 准确还原。
$r$ 块的新增费用仅为固定的
$\|\mathsf D_h^{-1}\|^r$。

先用
$\mathcal R_r=R(r^{-2})^{c_G r}$
正则原核，固定 $c_G$ 足够支付全部
$O(r\deg G)$ 原自然字。
它强趋 $I$，保持 $M$，且 (13.17) 保持同一有限词域。
跨池矩逆成本仍为 $e^{O(\log N)}$；
取 $r=\lfloor\sqrt N\rfloor$ 后，
总对数费用仍为 $O(r\log N)$，
低于实际四次局部交换子预算。

所有输入先在 $M$ 中形成，原物理反射始终在最左；
(13.17) 从不穿过反射，其伴随从不施于未知 $M$。
没有另给任意 $A'$ 系数假设反射稳定性。
因此全域偏导逆稿的完整顶部、非零纯池弱极限、
两侧原 $A$ 四次因子与全 $H$ 上的 $C$ 配对逐项适用，
得到 $M=0$。
原规范图判据给出所需循环性。

### 13.5 全部外层复合与例外集的准确归属

综上，对 (13.7) 的全部复参数及任意非零一变量多项式 $Q$，
$$
\boxed{
Q(F(U_1,\ldots,U_5))e^w
\text{ 非零且对实际 }A\text{ 循环}.
}
\tag{13.19}
$$
$\deg Q=0$ 时是非零常数倍 $e^w$；其他情况均重新完成
(13.9)–(13.18)。
特别包括
$$
\boxed{
[F(U)-\lambda]^m e^w,\qquad
\lambda\in\mathbb C,\quad m\ge1.
}
\tag{13.20}
$$
$F$ 因为 $\alpha\ne0$ 必非恒定，没有零多项式例外。

例如 $\alpha=\beta=1,\ell=b$ 时，
§12 仍准确给完整标量矩逆的临界值
$\{\lambda:\lambda^3=27/8\}$。
(13.19) 说明这三个值的原实际向量同样循环，
并且全部普通点态幂和外层复合也已覆盖。
这不是标量临界集变空，而是实际偏导 (13.11) 虽然具有标量零点，
其原规范闭算子却有已经证明的全域有界逆。

本节不将该例的结论推广为任意多项式的临界值都可消去，
也不将 $\mathscr VQ_F=\delta$ 延伸为不成立的普通乘法法则。
新增的真实范围由最低键的唯一性和明确的正 first Bell 逆共同给出。

