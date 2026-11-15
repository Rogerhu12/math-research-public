# R747 — 两个完整返回的原来源恢复与仅 p 层的有限门模型

日期：2026-11-15。**状态：下述来源恢复、完整有限门及代数下降结论已证明。**

本篇将 R742 的两条完整 W/V 返回，连同实际负一观察、全部伙伴、条件质量和17投影，逆搬回原 $e_0$ 与原 Y 轴。这样，R745 为非整返回轴显示的 $34\cdot36^2p$ 清分母模型可以在这两个**指定返回项**上换成原 degree34 来源及其 p-primary 平移。共同代数覆盖只增加 p 的幂。

这里不删原坏处的有限向量，不把完整34维来源自动缩成 R735 两线。有限门在 K 上的自然下降也不等于 R749 只作用点因子的投影。尤其，R742 的过滤非零式及其原外部反号仍完整保留，不能由本篇另赋中央零。

## 1. 同一个固定 p、同一个实际权

沿 R742，固定原合格普通素数 p，及
$$
K=\mathbf Q(\omega),\quad \delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad
\kappa=\pi_0/\bar\pi_0=p\lambda^2,\quad
\Omega=\Omega_p .
\tag{1}
$$
$p$、$\lambda$、$\kappa$ 在本篇始终固定。$\mathrm N(\kappa)=1$。

原六输入、原 C 平均及三个 A 伙伴都保留。使用 R686/R740 的行
$$
\begin{aligned}
Y&=A+c+2d,& W&=A+3\delta c+4d,\\
b_Y&=(20+3\omega)/17,& Z&=W-b_YY,\\
\alpha&=17-3\omega,&V&=36Y-\alpha W,\\
E&=(5+6\omega)A-29c-(58+87\omega)d .
\end{aligned}
\tag{2}
$$
$\Phi_\infty$ 是 R742 从原 q 的**完整两个 C 支**取得的权：
$$
\Phi_\infty=\sum_{a=0}^{30}E^a\phi_{a,\infty}.
\tag{3}
$$
每个 $\phi_{a,\infty}$ 只依赖与 Y、Z、E 正交的三个伙伴，保其原混次
$b^{d/6}\Omega^d$ 归一。全部实际整逆系数在 $K(\lambda,\kappa)$；本篇没有换一个测试。
也可逐项保原 $C^\perp$-unit 指示，不将它误改成一个未知条件系数。

令
$$
B_i=b_iZ+e_iE,\qquad
\begin{array}{c|cc}
i&b_i&e_i\\ \hline
1&-(170+117\omega)/526&-(4+9\omega)/263\\
3&(170+291\omega)/526&(2-3\omega)/263
\end{array},
\quad
\Delta_\ell=1_{B_1\in p^\ell}-1_{B_3\in p^\ell}.
\tag{4}
$$
所有固定分母仍由原射线排除。固定 $r=1$ 的 R742 恒等式只用
$1\le\ell\le125$；以下对每个有限 $\ell\ge1$ 单独成立。

## 2. 先分原域，再逆搬完整 core

定义四个原六变量指示权
$$
\begin{aligned}
m_{P,\ell}&=1_{\{Y,Z,E\ {\rm unit}\}}\Delta_\ell,\\
m_{G,\ell}&=m_{P,\ell}1_{\{W,V\ {\rm unit}\}},\\
m_{W,\ell}&=m_{P,\ell}1_{\{W\in p\}},\\
m_{V,\ell}&=m_{P,\ell}1_{\{V\in p\}}.
\end{aligned}
\tag{5}
$$
这是带符号的门；$\Delta_\ell$ 仍是两个原完整门之差。

由 $36Y=V+\alpha W$，在 Y-unit 上不可能 W、V 同时属于 p。因此有逐点恒等式
$$
\boxed{m_{P,\ell}=m_{G,\ell}+m_{W,\ell}+m_{V,\ell}.}
\tag{6}
$$
不需额外附加某条未出现的 L-unit 条件，也没有遗失 W、V 同深的一支：
它在 (5) 的 Y-unit 上本来为空。

记物理秩一变换
$$
P_{L,t}=I+(t-1)\frac{\bar L^{\,t}L}{N(L)},\qquad L=W,V .
$$
R692 的完整来源恒等式为
$$
e_0|_{\{W\in p\}}=\lambda(P_{W,\kappa})_*e_1,\qquad
e_0|_{\{V\in p\}}=\gamma\lambda(P_{V,\kappa})_*e_1,\qquad
\gamma=\chi_A\chi_E .
\tag{7}
$$
这里保原全部伙伴，$\chi_A^2=\chi_E^2=1$；没有只在 W/V 边际使用 (7)。

准确写出 (7) 后的观察：
$$
\begin{array}{c|cc}
&Y\circ P_{L,\kappa}&Z\circ P_{L,\kappa}\\ \hline
L=W&y_W=(V+\alpha\kappa W)/36&
z_W=(263\kappa W-\bar\alpha V)/612\\
L=V&y_V=(\kappa V+\alpha W)/36&
z_V=(263W-\bar\alpha\kappa V)/612
\end{array}.
\tag{8}
$$
E 及 (3) 的另外三个伙伴被这两个变换逐个固定。

在 V-unit 上，$y_W,z_W$ 都为单位；在 W-unit 上，$y_V,z_V$ 都为单位。
这只用原固定系数为单位及 $\kappa\in p\mathcal O$。
所以 (7) 对 (5) 的真实限制准确给
$$
\begin{aligned}
\int \frac ZY E^a\phi_{a,\infty}m_{W,\ell}\,de_0
&=\lambda\int_{\{V,E\ {\rm unit}\}}
 \left(1_{b_1z_W+e_1E\in p^\ell}
       -1_{b_3z_W+e_3E\in p^\ell}\right)
 \frac{z_W}{y_W}E^a\phi_{a,\infty}\,de_1,\\
\int \frac ZY E^a\phi_{a,\infty}m_{V,\ell}\,de_0
&=\gamma\lambda\int_{\{W,E\ {\rm unit}\}}
 \left(1_{b_1z_V+e_1E\in p^\ell}
       -1_{b_3z_V+e_3E\in p^\ell}\right)
 \frac{z_V}{y_V}E^a\phi_{a,\infty}\,de_1 .
\end{aligned}
\tag{9}
$$
右边正是 R742 的完整 $H_W,H_V$，包括其常数质量项和全部 $\kappa$ 高阶项。
本篇使用 (9) 从右向左，未将 $z_L/y_L$ 截成第一项。

特别，原 W-quarter 来源与 $P_{L,\kappa}$ 必须合在一起逆搬。
只看裸 $e_1$ 的二处角色，不能代表 (9) 的左边。

## 3. 原 Y 的四个实际代数来源

对 $j=P,G,W,V$ 定义真实一变量测度
$$
\boxed{
\nu_{j,a,\ell}
=\Omega^{-1}Y_*
 \left(ZE^a\phi_{a,\infty}m_{j,\ell}\,e_0\right).
}
\tag{10}
$$
这些测度均支撑在 Y-unit；定义中的所有六变量门仍完整保留。
其生成函数是
$$
F_{j,a,\ell}(z)
=\Omega^{-1}\int
 e^{Yz/\Omega}ZE^a\phi_{a,\infty}m_{j,\ell}\,de_0 .
\tag{11}
$$
$Z/\Omega$ 是实际正交一阶矩，不是把负一积分先算成某个系数。

R745 的完整 Fourier、Mumford 平移和正交 jets 定理给：
(11) 是有限个真正 theta 截面的代数线性组合。
每个混次块的 $\Omega$ 按该块次数逐项抵消；(10) 的额外 $\Omega^{-1}$
准确抵消 Z 的一阶微分。因此没有遗留一般的 $\mathbf C_p$ 伙伴质量。

由 (6) 得**整个来源**等式
$$
\nu_{P,a,\ell}
=\nu_{G,a,\ell}+\nu_{W,a,\ell}+\nu_{V,a,\ell}.
\tag{12}
$$
若 $I_{-1}(\nu)=\int_{\mathbf Z_p^\times}x^{-1}\,d\nu(x)$，则
$$
\begin{aligned}
p_a(\ell)&=\Omega I_{-1}(\nu_{P,a,\ell}),&
G_a(\ell)&=\Omega I_{-1}(\nu_{G,a,\ell}),\\
\lambda H_{W,a}(\ell)&=\Omega I_{-1}(\nu_{W,a,\ell}),&
\gamma\lambda H_{V,a}(\ell)&=\Omega I_{-1}(\nu_{V,a,\ell}).
\end{aligned}
\tag{13}
$$
(13) 记录了两返回的外部标量；不能把 $\lambda$ 或 $\gamma$ 吸入一个未指定 period。

## 4. p-primary 提升与准确的共同 line bundle

以下先对原 $e_0$ 的一个 tensor 项证明，再对完整 C 平均求和。
生成列使用 R745 的约定
$$
\iota_Y(z)=y^t z,\qquad
y=(\delta,2\delta,\gamma_7,\bar\gamma_7,1,2),
\tag{14}
$$
不是 $\bar y^t z$。

取原 Y 与其五个正交伙伴的加法 isogeny
$$
s:E_{17}\times B\longrightarrow E_{17}^6 .
$$
其固定度数只含已排除的坏素数，故对本篇 p 有
$$
s:(E_{17}\times B)[\mathfrak p^M]
 \xrightarrow{\ \sim\ }E_{17}^6[\mathfrak p^M].
\tag{15}
$$
因此每个六变量 formal p-primary 平移都有**唯一的 p-primary 提升**。
不需任意选择带二挠或十七挠误差的有理逆。

原正交分裂是
$$
s^*\mathcal L=\mathcal L_{34}\boxtimes\mathcal L_B,
\qquad \mathcal L_{34}\simeq\mathcal O(34[0]),
\tag{16}
$$
带原 rigidification、半特征及全部 Mumford 因子。
R745 已逐项付清原 C 有理旋转：它固定 Y，只改变 B 的实际 isogeny/微分；
其原固定 cover 及有限相位仍保留，不被 (15) 删除。

设 $M\ge\ell$。把 (5) 的单位门和深度门按原 Fourier 恒等式展开，
每一项是 $E_{17}^6[\mathfrak p^M]$ 的 formal 平移。
经 (15)，在 Y 因子上的真实 line bundle 必为
$$
t_t^*\mathcal L_{34},\qquad t\in E_{17}[\mathfrak p^M],
\tag{17}
$$
其余 p-primary 标签、中心配对全部在 B 因子及代数系数内。
沿 B 取有限正矩只收缩该外张量因子，不改变 (17) 的 automorphy。

于是 (11) 所属的准确有限池为
$$
\boxed{
\mathscr T_{34,M}
=\sum_{t\in E_{17}[\mathfrak p^M]}
       H^0(E_{17},t_t^*\mathcal L_{34}),
}
\tag{18}
$$
在保各自 flat twist 的直和中理解其生成函数及相加。
这不是先把全部 flat twist 认成同一个裸 $S_{34}$。

令
$$
a_M=\bar\pi_0^{\,M},\qquad N_M=34p^M .
\tag{19}
$$
在 $\operatorname{Pic}^0(E_{17})\simeq E_{17}$ 下，
$t_t^*\mathcal L_{34}\otimes\mathcal L_{34}^{-1}$
对应 $\pm34t$，符号取决于 Picard 识别约定，不影响下一消去。
$[a_M]^*$ 在 $\operatorname{Pic}^0$ 上是对偶同态 $[\pi_0^M]$；
它准确杀掉 $\mathfrak p^M$-torsion。故
$$
[a_M]^*t_t^*\mathcal L_{34}
\simeq[a_M]^*\mathcal L_{34}
\simeq\mathcal O(N_M[0]).
\tag{20}
$$
第二式没有新增二挠 twist：$p^M$ 为奇数，
$[a_M]$ 的 kernel 中每个非零点与其负点配对，kernel 点和为零。
所有同构按原 rigidification 固定，沿用 R745/R742 的 Mumford 周期因子。

因此 $F_{j,a,\ell}(a_Mz)$ 全落同一完整 degree $N_M$ 代数 theta 空间。
这个共同模型只增加 p 的幂。
它不增加额外的 $36^2$、二处或三处覆盖，也不删除原 degree34 模型已有的17 gluing。

在所选 ordinary p 处，$a_M$ 是单位。
实际测度与负一观察的变换为
$$
F(a_Mz)\longleftrightarrow[a_M]_*\nu,\qquad
I_{-1}([a_M]_*\nu)=a_M^{-1}I_{-1}(\nu).
\tag{21}
$$
所以原值准确为 $a_M\Omega I_{-1}([a_M]_*\nu)$，而非换一个未知 period。
(20) 没有额外的 p 进赋值损失；Fourier 展开的 $p^{-M}$ 等显式分母照旧保留，
最终有界性来自原 (10)，不能逐项误认每个 Fourier 系数都是整的。

取 $M=125$ 即同时容纳 R742 的 $r=1$ 全部有限门。
(20) 是对 (9) 这两个可逆 core 返回的加强；
它不否定 R745 对任意非整返回轴所给的 $34\cdot36^2p$ 通用模型。

## 5. 全相位及 homogeneous gate 的自然代数下降

本节只说明 gate 算子的定义域，不把它当作点因子投影。

对原一条 K 线性行 L，
$$
1_{L(\xi)\in p^m}
=\frac1{p^m}\sum_{a\bmod p^m}\zeta_{p^m}^{aL(\xi)}
\tag{22}
$$
对应 formal p-primary 平移的完整平均。
若 L 有固定的 prime-to-p 分母，则在
$E[\mathfrak p^m]$ 上用其唯一逆；(22) 不因此引入另一坏素数的 torsion 点。
若该行不是 primitive，则保 (22) 中的原重复次数，不改归一因子。

在 (20) 的共同覆盖上，所需 p-primary 子群是 theta group 的 isotropic 子群。
其 canonical 平移不是一个裸 $F(z+t)$：
它是 R745(8)、R742(24) 所给、带全部配对的 Mumford lift。
这组 lift 的乘积由 Bannai–Kobayashi Proposition 1.14 给出。
在相应 p-primary isotropic 子群上，交换配对为一，
故得到真实子群作用。

也可从同一 line bundle 的 p-isogeny 下降核定其代数规范。
对单个 Y 因子，
$$
\mathcal O(34p^M[0])\simeq[\pi_0^M]^*\mathcal L_{34}
$$
给 $\ker[\pi_0^M]$ 的自然下降 lift。
该 lift 与原对称 rigidification 相容。
在奇数阶子群上，对称 splitting 唯一：
两个 splitting 的商是子群角色；
与 $[-1]$ 相容迫该角色的平方为一，故它只能为平凡角色。
原 Mumford 半点规范给同一对称 splitting。
多变量逐因子使用，再经 (15) 运输，仍保所有中心相位。

因而 (22) 的完整算子可以写成
$$
\mathsf A_{L,m}
=\frac1{p^m}\sum_{a\bmod p^m}
          \widetilde{\mathsf T}_{a t_{L,m}},
\tag{23}
$$
其中 $t_{L,m}$ 的像及其重数在 K 定义，
$\widetilde{\mathsf T}$ 为上述实际 lift。
换 $\zeta_{p^m}$ 只重排同一个平均。
$G_K$ 也重排该完整子群和其 canonical lift，故 (23) 是 K 定义的代数算子。
单位门为 $1-\mathsf A_{L,1}$，
$\Delta_\ell=\mathsf A_{B_1,\ell}-\mathsf A_{B_3,\ell}$；
其乘积逐项给 (5)，不把交域改成独立概率或独立边际。

原实际权的系数在 K，正交微分按 K 上的代数微分归一。
因此，未再加非 K 系数投影时，(11) 的完整有限组合具有自然 K 下降。
单个 Fourier 项、单个正交 torsion jet 的系数通常不在 K；
下降是所有配对、系数及平移一起共轭后的结果。

这里尤其不能推出
“固定这些代数系数，只对点作 p-ray trace 后，所有非平凡项消失”。
R749 的实际 $Q_2\otimes17^{2/3}$ 反例正说明自然半线性下降与
固定系数 point-only trace 不同。
把 (23) 接到 R748/R749 时，仍须保实际每个系数和对应点特征。

## 6. 两条17投影也在同一原来源上恢复

令 $\mathcal P_\chi^Y$ 为 R742 的完整17投影。
同篇已通过兼容 CRT 代表及全 Mumford 相位证明：
原有限 p 门、原有限正矩与这个投影相容。
这里使用其已付来源级范围，不对一个已积分的 $\mathbf C_p$ 数任意投影。

定义
$$
\nu_{\chi,j,a,\ell}
=\Omega^{-1}Y_*
 \left(ZE^a\phi_{a,\infty}m_{j,\ell}\,
             \mathcal P_\chi^Y e_0\right).
\tag{24}
$$
则 (12)–(13) 逐个 $\chi$ 完整成立。
对右边两个返回，严格使用
$$
\mathcal P_\chi^{Y_\kappa^L}
=\omega_{17}(P_{L,\kappa})^{-1}
   \mathcal P_\chi^Y\omega_{17}(P_{L,\kappa}),
\qquad L=W,V .
\tag{25}
$$
于是
$$
\begin{aligned}
p_{\chi,a}&=\Omega I_{-1}(\nu_{\chi,P,a,\ell}),&
g_{\chi,a}&=\Omega I_{-1}(\nu_{\chi,G,a,\ell}),\\
\lambda h_{\chi,a}^W&=\Omega I_{-1}(\nu_{\chi,W,a,\ell}),&
\gamma\lambda h_{\chi,a}^V&=\Omega I_{-1}(\nu_{\chi,V,a,\ell}).
\end{aligned}
\tag{26}
$$
(26) 把 R742 的全部 $\mathcal C_{17}$ 返回数据恢复到同一个
$\mathcal P_\chi^Ye_0$，而非宣称两个原返回的裸局部向量相同。

(18)–(21) 可在先作此固定投影的完整 theta 模型中使用；
共同覆盖上的投影必须是其实际运输，不可因 degree 增大而换成另一个角色标签。
这是整个 finite bad-place 向量的恢复。
它不等于证明剩余二处空间已经是一条线，
也不等于证明每个伙伴收缩只产生 $D_{2,17}$ 或 $D_{4,17}$ 乘一变量函数。

## 7. 同一过滤总行及中央桥的准确剩余

将 (26) 代进 R742(33)，其左边仍只是有限多个
$$
\Omega I_{-1}(\nu_{\chi,j,a,\ell}),\qquad
j=G,W,V,\quad 0\le a\le30,\quad1\le\ell\le125
\tag{27}
$$
的已指定代数线性组合。它们全部来自同一个原来源及同一个原 q。
对 $\chi=\tau_2,\tau_4$，过滤总和分别为 R742 的非零
$\mathfrak I_{2,\infty}$、$\mathfrak I_{4,\infty}$，所有固定系数原样保留。

原 paired-T 外部也没有因此消失：
$$
\mathcal O_{\chi,\rm pair}^{T}
=-\mathcal I_{\chi,\rm pair}^{T}
\tag{28}
$$
继续是完整分区恒等式，经过相同过滤仍给相反数。

因此本篇推进的是 (27) 的实际共同来源和覆盖成本，
不是在一个无条件恒等式中添加新的算术零。
若要使用 R748/R749，还须在 (24) 的全部实际来源上证明：
原有限坏处向量、伙伴收缩及 p-Schwartz 分解确落已识别点公式的范围，
并保每个代数系数及点特征。总负一矩的角平均本身不替代这一步。

对未取 R742 一阶极限的原外部，观察仍含整个
$\log(1+\kappa\,\text{线性行}/\text{单位行})$。
固定有限门并不使这个 logarithm 变成局部常值函数或有限正矩多项式。
R745 以及本篇支付的是 (27) 的完整负一行；
它们没有给整条 logarithm 外部一个有限点对数公式。

主目标仍需原 $J'_S,J'_T,J'_U$ 的已付零或非零，
与某条**完整同域**的新算术关系发生实际联系。
各个外部的独立表达、完整相消或另一已付中央返回，至少仍须支付一项。
本篇不把 (27) 的非零总和当作该主桥已经闭合。

## 依赖与原文

- [R742](R742-fixed-seventeen-operators-and-same-gate-primitive-limit.md)：
  实际固定 p 权、至多125层门、全部17相位及两投影总行。
- [R745](R745-finite-p-gates-algebraic-theta-sources-and-orthogonal-jets.md)：
  原度数34外张量分裂、代数正交 jets、各齐次周期抵消。
- [R737](R737-common-depth-elimination-and-native-primitive-strips.md)、
  [R686](R686-original-yz-core-and-same-source-st-unit-failures.md)、
  [R692](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)：
  原六变量分区及全来源 W/V core。
- [R749](R749-point-factor-projectors-and-finite-character-extraction.md)：
  自然下降与 point-only 投影的区别。
- K. Bannai, S. Kobayashi,
  [Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers](https://arxiv.org/pdf/math/0610163),
  arXiv v4，Propositions 1.14、2.19；原 formal 平移、Mumford lift 及其配对规范均沿用 R742/R745。

本篇不新增数值运行或生成数据。
