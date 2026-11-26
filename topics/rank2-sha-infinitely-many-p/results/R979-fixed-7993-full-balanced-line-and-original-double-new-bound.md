# R979 — 在7993消费原 canonical 非零：完整 balanced 线、strict 核与原双新增广界

会话：Astra-rank2-Sha-0b097461-20261127，geometry 子任务。

**状态：下述固定系数素数的结论已证明。** 本篇消费 R817 已实际计算的三个原负二值，不增加数值运行。它无条件确定这一个素数上的三个完整有理 balanced Selmer 群及其 ordinary 严格核，并在同一个原双新类上去掉 R940 的底类非零前提。所得增广界是上界，允许该双新类为零；不产生原端点非零，不限制辅助模数的大小，也不产生无穷系数素数的结论。

## 1. 固定原表示与唯一系数素数

取 R817 的同一个
$$
p_*=7993,\qquad \pi_*=69-32\omega,\qquad
\omega\mapsto4748,\quad\zeta_{18}\mapsto203\pmod {7993}.
\tag{1}
$$
三标签仍是 $j=4,10,16$。设
$$
\lambda_j=\eta_j^{-1}\psi_0^3,\qquad
\nu_j=\eta_j\psi_0^{-1}\bar\psi_0^2,\qquad
V_j=E_{\mathfrak P}(1)\widehat\nu_j^{-1}.
\tag{2}
$$
这是 R804/R811 的原表示；在 R891 的算术 Tate 约定中，其最小格为
$$
T_{0,j}=\mathcal O_0(\rho_j),\qquad
\rho_j=\eta^{e_j}\psi_0^3\varepsilon_{\rm cyc}^{-1},
\qquad(e_4,e_{10},e_{16})=(5,17,11).
\tag{3}
$$
因 $18\mid7992$，所选最小系数环 $\mathcal O_0=\mathbf Z_{7993}[\mu_{18}]$ 就是 $\mathbf Z_{7993}$。允许原先固定的有限系数扩张 $\mathcal O/\mathcal O_0$，但检测先在最小格上做，最后才作有限自由基变换。以下省略一个固定的标签。

原局部条件在 $\mathfrak p_*$ 为 full，在 $\bar{\mathfrak p}_*$ 为 zero；在其余位取原 Bloch–Kato 条件。由 R811 的真实共轭比较，这正是 $V$ 的 Bloch–Kato 条件，记为 $\operatorname{Sel}_{\rm bal}(K,V)$。

本篇不把7993说成包含全部另用几何同余条件的巨大 CRT 射线成员。这里实际需要并已具备的条件是：$p_*>211$、在 $K$ 分裂、素于 $2\cdot3\cdot7\cdot13\cdot17$，且原十八阶角色在 $p_*$ 未分歧。R817(4)–(7)又给原 primary 生成元及
$$
\eta_j(\mathfrak p_*)=\eta_j(\bar{\mathfrak p}_*)=-1.
\tag{4}
$$
因此 R885 的原 ordinary 稳定化式适用。R897/R901/R908 中本文所用的 finite tame 原类、两次增广及新增惰性位局部式，只使用上述普通条件、原固定 tame level 和新增位条件；其清分母保留为原固定 $D$，不要求 $p_*\nmid D$。本文不用其它 CRT 条件下的有限域全除子计算或有限 $\ell$-adic shadow。

## 2. 原 Katz 非零确实给整个 Selmer 线

R817 的公开运行已给同一原整 theta 测度的
$$
\Omega_{p_*}^{-7990}(I_{4,-2,p_*},I_{10,-2,p_*},I_{16,-2,p_*})
 \equiv(2522,2828,3696)\pmod {7993}.
\tag{5}
$$
原周期为单位，因此三个 $I_{j,-2,p_*}$ 都非零。R806 的完整 primitive Katz 平方比较和 R811 的平滑比较，保留原导子 $34\delta$、30平滑、Artin 基和非零代数常数，给
$$
\mathscr L_v(\lambda_j\mathbf N^{-2})(0)\ne0.
\tag{6}
$$
这里只使用非零；不由(5)断言 R806 的 $c_j$ 是7993单位。

应用 Castella 发表版本的 Theorem A.1.1。其假设在此逐项为：$r=2$；按该文几何互反约定 $\lambda_j$ 的 infinity type 为 $(-3,0)$；中心特征是 $\eta_K$；导子为 $34\delta$，素于7993；$p_*$ 在 $K$ 分裂且大于3。R811 §2 已给完整角色核对及真实 $\tau$ 输送，不需要把两个相反互反约定下的角色直接相认。该定理以(6)推出整个 Bloch–Kato 群维数1。输送回(2)得
$$
\boxed{\dim_E\operatorname{Sel}_{\rm bal}(K,V_j)=1.}
\tag{7}
$$
这一步使用的是已支付的 $p$-adic Katz 值，未以 R818 的复解析秩一替代(6)，也未先假设原 $q/q^4$ 端点非零。

R817 的原 canonical 类是
$$
z^{\rm can}_{j,p_*}
=\frac1{30}\operatorname{pr}_K
 \operatorname{tw}_{\nu_j}(e_{\eta_j}u_\infty),
\tag{8}
$$
并且其实际 ordinary 局部化非零。式(8)本来属于同一个 Selmer 群，所以由(7)
$$
\boxed{\operatorname{Sel}_{\rm bal}(K,V_j)=E z^{\rm can}_{j,p_*},\qquad
 \ker\bigl(\operatorname{loc}_{\mathfrak p_*}:
 \operatorname{Sel}_{\rm bal}(K,V_j)\to H^1(K_{\mathfrak p_*},V_j)\bigr)=0.}
\tag{9}
$$
这是整个有理 Selmer 群的严格核结论，强于 R811 只对 canonical 张成子空间的结论；它仅在(1)这个已检测素位使用(5)。

## 3. 对原端点的准确后果

保持原端点类 $c_1=z^{\rm end}_{j,p_*}$，不把(8)改名为 $c_1$。式(9)给
$$
c_1=0\quad\Longleftrightarrow\quad
\operatorname{loc}_{\mathfrak p_*}c_1=0.
\tag{10}
$$
它没有判定这两个等价条件是否成立。

若另行证明这个原 $c_1\ne0$，则 R893 的原条件定理适用。由(9)原局部化非零，R885 的实际特殊化单位 $\mathscr E_{p_*}$ 不产生新零，故
$$
\boxed{c_1\ne0\ \Longrightarrow\ s=\operatorname{ord}_T D(T)=0
\quad\text{在 }p_*=7993.}
\tag{11}
$$
这里不把 $c_1=0$ 的情形代入 R893 的单位比例；当 $c_1=0$ 时，R893 的原假设未满足，不能据(11)为其全局提升指定增广阶。

## 4. 原双新类及定理的量词

保持 R940 的原 finite tame 双新项、原格和原固定尺度：
$$
R_i=\mathcal O[C_{h_i}],\quad
A_i=R_i/(N_i),\quad j_i=\sigma_i-1,\quad
h_i=p_*^{e_i},\quad e_i=v_{p_*}(q_i+1),
$$
$$
\mathcal N_{12}=j_1j_2x_{12},\qquad
x_{12}\in H^1(K,A_1\otimes A_2\otimes T).
\tag{12}
$$
其中 $q_1,q_2$ 为不同的原允许惰性有理素数，素于 $30\cdot34p_*$。对 $m\le\min(e_1,e_2)$，定义同一个真实系数映射和实际下降
$$
\pi_m:A_1\otimes A_2\to\mathcal O/p_*^m,
\quad\sigma_1,\sigma_2\mapsto1,
\qquad
\kappa_{12,m}=(\pi_m)_*x_{12}.
\tag{13}
$$
不把 $x_{12}$、$\mathcal N_{12}$ 或 $\kappa_{12,m}$ 假定为非零。

**定理。** 对每个标签，有一个有限整数 $B_*\ge0$，只依固定 $p_*,T$ 和原固定 $D$，使对每个 $m\ge1$ 存在正密度的允许惰性素数集合 $\mathcal Q_m$，满足 $q\equiv-1\pmod{p_*^m}$。若 $q_1\in\mathcal Q_m$，而 $q_2\ne q_1$ 为任一允许惰性素数且 $p_*^m\mid q_2+1$，则同一个(13)满足
$$
\boxed{p_*^{B_*}\kappa_{12,m}=0.}
\tag{14}
$$
这条定理不要求原 $c_1\ne0$。若 $m>B_*$，令 $M=m-B_*$，则
$$
(\pi_M)_*x_{12}=0,
\tag{15}
$$
且有唯一原像
$$
x_{12}^J\in H^1(K,J_{12,M}\otimes T),\qquad
J_{12,M}=(p_*^M,j_1,j_2)(A_1\otimes A_2).
\tag{16}
$$
式(16)仍是系数子格中的上同调原像，不是 scalar 整除陈述。

## 5. 同一原格的本原线与惰性检测

令 $\Sigma$ 为 $K$ 中位于 $2,3,17,p_*$ 上的素位。R891 的坏位计算给所有 $v\mid2\cdot3\cdot17$ 上的有理局部群为零。故下列固定复形的有理一阶上同调正是(7)：
$$
C_0=\operatorname{Cone}\bigl(C^\bullet(G_{K,\Sigma},T_0)
\longrightarrow C^\bullet(K_{\bar{\mathfrak p}_*},T_0)\bigr)[-1].
\tag{17}
$$
原17惯性元在 $T_0/p_*^a$ 上为 $-1$，从而所有全局 $H^0(K,T_0/p_*^a)$ 为零。R921(39)的 $\bar{\mathfrak p}_*$ 惯性计算同样给所有局部残余 $H^0$ 为零：原 Tate 指数为 $-1$，$p_*>211$。因此
$$
S_0:=H^1(C_0)
$$
无 $\mathcal O_0$-挠，且是全局 $H^1$ 中原有理 Selmer 线的饱和格。由(7)，$S_0$ 自由秩一。固定本原生成元 $z$；它只是检测向量，不改任何几何来源。

精确约化给 $S_0/p_*\hookrightarrow H^1(K,T_0/p_*)$，故 $z\bmod p_*\ne0$。对真实共轭类 $z^c$ 也成立。按 R940 §4 及其中引用的原有限测试注 A.2–A.5，在同时平凡化 $T_0/p_*^m,T_0^c/p_*^m,\mu_{p_*^m}$ 的原有限阿贝尔域 $\Omega_m$ 上，可以选
$$
\tau\in G_{\Omega_m},\qquad z(\tau)=1,\quad z^c(\tau)=0
\pmod{p_*^m}.
\tag{18}
$$
该联合满像只用原两个不同角色、完整17惯性和最小系数环；不需要 $z$ 是原端点。这里正是 R940 原证明可以替换其秩一来源、但不能删掉本原检测向量的地方。

令 $c$ 为实际阶二复共轭元，$g=c\tau$。在两个 cocycle 的共同有限测试域中，$g$ 在 $K$ 上非平凡，在 $\mu_{p_*^m}$ 上为取逆。其平方在 $G_K$ 中，且
$$
z(g^2)=z(c\tau c)+\rho(c\tau c)z(\tau)
       =z^c(\tau)+z(\tau)=1\pmod{p_*^m}.
\tag{19}
$$
Chebotarev 应用于这个真实共轭类给 $\mathcal Q_m$；可以再删任意固定有限集合。对其中每个 $q$，原 $T_0$ 的 $K_q$-Frobenius 为 $-q$，于是
$$
H^1_{\rm unr}(K_q,T_0/p_*^m)\simeq\mathcal O_0/p_*^m,
\quad\operatorname{loc}_qz\text{ 为生成元。}
\tag{20}
$$
选定上方素点时读数为1；改变 frame 只乘同步单位。真正被检测的是固定本原 $z$，没有在这一步检测原 $x_{12}$ 非零。

## 6. 完整残余群、有限 Bockstein 指数与原局部零

固定数域、有限 $\Sigma$ 和有限自由格给 $H^2(C_0)$ 为有限生成 $\mathcal O_0$-模。只取其挠子模，定义有限整数 $b_*$ 使
$$
p_*^{b_*}H^2(C_0)_{\rm tors}=0.
\tag{21}
$$
这不声称 $H^2(C_0)$ 没有自由部分，也不声称 $b_*=0$。每个 $m$ 的完整残余群有精确列
$$
0\longrightarrow S_0/p_*^m
\longrightarrow H^1(C_0/p_*^m)
\longrightarrow H^2(C_0)[p_*^m]
\longrightarrow0.
\tag{22}
$$
所以
$$
p_*^{b_*}H^1(C_0/p_*^m)
\subset (\mathcal O_0/p_*^m)z.
\tag{23}
$$
此处没有把完整残余 Selmer 群换成可提升子群；(21)–(23)显式支付所有不可提升的连接类。系数扩大后同式成立，因为 $\mathcal O/\mathcal O_0$ 有限自由。

R940 结论A及其§2–3不使用任何底类非零假设，因而仍给原(13)的唯一下降及
$$
D\operatorname{loc}_{q_1}\kappa_{12,m}
=D\operatorname{loc}_{q_2}\kappa_{12,m}=0,
\quad D\kappa_{12,m}\in H^1(C_0/p_*^m)\otimes_{\mathcal O_0}\mathcal O.
\tag{24}
$$
所有原 $q/q^4$ 端点、Artin、旧副本和清分母均在这个 $D$ 中保留。由(23)，存在 $a\in\mathcal O/p_*^m$ 使
$$
p_*^{b_*}D\kappa_{12,m}=a z.
\tag{25}
$$
在 $q_1\in\mathcal Q_m$ 处局部化：(24)使左边为零，(20)使右边只有 $a=0$ 才能为零。故(25)为零。写 $D=p_*^d u$、$u\in\mathcal O^\times$，可取
$$
\boxed{B_*=b_*+v_{p_*}(D).}
\tag{26}
$$
这证明(14)，而且是针对同一个原 $\kappa_{12,m}$，没有重新选类。

若 $m>B_*$，系数映射
$$
T/p_*^M\xrightarrow{\ p_*^{B_*}\ }T/p_*^m
$$
在 $H^1$ 上单射：其 cokernel 是 $T/p_*^{B_*}$，该模的 $H^0$ 已由17惯性为零。原 $\kappa_{12,m}$ 先约化到 $M$，再经过这个单射，恰为 $p_*^{B_*}\kappa_{12,m}$。于是(14)给(15)。最后应用
$$
0\to J_{12,M}\otimes T\to A_1\otimes A_2\otimes T
\xrightarrow{\pi_M}T/p_*^M\to0
$$
的上同调列，(15)给存在性，右端 $H^0=0$ 给唯一性，得到(16)。

## 7. 零情形及不能从这个界得到的结论

如果原 $c_1=0$，上述(7)–(9)仍由独立的原 canonical 输入成立，(14)的证明仍成立。这并不证明 $x_{12}\ne0$。如果实际 $x_{12}=0$，则对所有允许 $m$ 都有 $\kappa_{12,m}=0$，(14)–(16)恒成立，任意大的允许辅助模数同样可以出现。因此本篇的有限 $B_*$ **不是**对 $q_i$、$e_i$、$n=q_1q_2$ 或任意层数的上界。

即使 $x_{12}\ne0$，它也可能映到 $\kappa_{12,M}=0$。要把(15)用于排除一个候选，必须另行证明：在同一 $p_*$、同一原格、同一两个辅助位且 $q_1\in\mathcal Q_m$ 的条件下，实际 $(\pi_M)_*x_{12}\ne0$。本篇没有这种非零输入；其它系数素数的 shadow、$H^1(J\otimes T)$ 中的非零或未取增广的 $x_{12}\ne0$，都不提供它。

因此这里新支付的是一个已知非零 canonical 底对**整个**原有理 Selmer 问题的消费，及其对原双新上界的固定素数应用。原 $c_1$ 的真实非零、这个条件在无穷多个 $p$ 上成立、跨 $p$ 的 $B_p$ 控制，以及主目标的通常全 $\Sha[p^\infty]$ 有限性均未由本篇取得。

## 8. 依据与执行范围

- [R817](R817-fixed-prime-original-negative-two-and-nonzero-fixed-cycles.md)：(1)、(4)、(5)、原 canonical 全局及 ordinary 非零，含唯一公开运行及全 hash。本篇不重跑该计算。
- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)、[R804](R804-original-order-eighteen-soule-classes-and-negative-two-localization.md)、[R811](R811-canonical-soule-classes-and-global-heegner-comparison.md)：原 finite 角色、完整 Katz 比较、平滑、period 与 $\tau$ 输送。
- F. Castella，*Tamagawa number conjecture for CM modular forms and Rankin–Selberg convolutions*，发表版本 [v3 HTML](https://arxiv.org/html/2407.11891v3)、[v3 PDF](https://arxiv.org/pdf/2407.11891v3)，Theorem A.1.1 及其证明。本篇仅用已验证(6)的正向结论，不用 weight4 的复秩一推出 AJ 非零。
- [R891](R891-original-ring-class-anti-kummer-and-one-prime-descent.md)、[原有限测试注](../notes/2026-11-16-original-endpoint-finite-test-chebotarev-refinement.md)：原最小格、17惯性、共轭两类的联合有限像。
- [R893](R893-original-endpoint-augmentation-square-and-primitive-heegner-comparison.md)：只在 $c_1\ne0$ 时使用的原增广比较。
- [R940](R940-original-double-inert-descent-and-bounded-augmentation.md)、[R921](R921-original-inert-residual-local-matrix-and-integral-bockstein.md)、[R908](R908-original-inert-augmentation-specialization-and-point-shadow.md)：同一个原双新下降、局部零、完整残余连接类及固定尺度。本篇将其条件秩一输入替换为(7)，其余原类不变。

本篇没有数学程序、数值扫描、新选系数素数或保存可重算数据。
