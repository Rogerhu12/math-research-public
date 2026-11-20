# R138 补篇：实际全频外端旋转能量严格为负，mean 缺陷有明确支出

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**已证明。** 使用[已付正支撑的同一周期圆锚](R138-supplement-actual-positive-support-for-repaired-physical-frame.md)和原真实 homogeneous exterior graph，存在一个明确、全圈周期的旋转/位置方向提升，使外端旋转能量满足
$$
\boxed{\quad
\mathcal B_R\le
-2\pi a_R^2s_R\|c_\perp\|_{H^{-1/2}_\theta}^2 .
\quad}
\tag{O.1}
$$
独立物理 mean 没有置零；它在边界二次型中的正项已被严格负余量吸收。提升的初始角缺陷准确为一个 mean 秩一项，并由同一个实际 mean derivative 控制。没有用辅助 cooperative Robin 线替换外图，也没有裁掉外部低高频混合。

(O.1) 是 $H^{-1/2}$ 能量迹上的全频结论。第 8 节用同一实际正高图的 base-order 与 negative-one 两个已闭窗口，证明 prescribed high-stable 输入为零的 given-head 齐次核有 $H^{1/6}$ 外迹，故可直接使用本式。任意粗自由 stable 输入和全部旧粗源的统一 coercivity 没有因此获授。内端 193 加 high 行和内部 residual 吸收仍待支付。

## 1. 与已付 support 完全相同的 base frame

以下都在 $R=25/8$ 的原物理角 $\theta$ 上。简写
$$
a=a_R,\quad t=b_0(R)=a'(R)/e(R)<0,\quad
z=-a_RC_{\rm ref}(R)>0,\quad
h=4347844570122155/4503599627370496>0.
$$
原尾半径方向 $a_r<0$ 及符号见
[完整物理匹配](R133-supplement-full-physical-trace-matching-and-waist-reflection.md)，(M.13)--(M.14)；
$t^2+z^2=1$ 来自原真实旋转 metric。第一个 support 补篇的准确圆锚是
$$
F=ae_r+he_z,\qquad
X=te_r+ze_z,\qquad Y=e_\theta,\qquad n=ze_r-te_z.
\tag{O.2}
$$
它给
$$
s_R=F\cdot n=az-ht>0,\qquad
h t^2\le h|t|\le s_R,\qquad az\le s_R.
\tag{O.3}
$$
本文始终取原点 $p=0$、$\sigma=1$，不另对齐外帽。
对 Qrepair 中心，前篇已证明整个径向模型的 $s\ge9/10$；
这里的 $s_R$ 是同一个量的端值。

## 2. 真正物理外图与已付的两侧 Sobolev 界

写物理曲率方向为
$$
b(\theta)=\sum_{n\in4\mathbb N} b_n\sin n\theta,\qquad
c(\theta)=c_0+\sum_{n\in4\mathbb N}c_n\cos n\theta,
\qquad c_\perp=c-c_0.
\tag{O.4}
$$
$J_\theta$ 的乘子是 $i\operatorname{sgn}(n)$，故
$J_\theta\sin n\theta=\cos n\theta$。原准确
homogeneous physical exterior derivative 是
$$
J_\theta b=-\mathsf Q c_\perp+T c_\perp,\qquad
c_0=Cc_\perp,\qquad \langle b\rangle=0,
\tag{O.5}
$$
其中 $\mathsf Q$ 是全部真实 $q_n$ 的乘子，
$T=D_Zd$、$C=D_Zc_0$。其定义和符号是
[完整物理 L2 外图](R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md)，(L.9)--(L.11)；
这不是把保存候选的非零边界 residual 当成零。

实际全频乘子已证
$$
99/100<q_n<1 .
\tag{O.6}
$$
其同一真实端口来源为
[实际 $25/8$ 端口](R133-supplement-actual-regular-R25over8-vector-and-long-ports.md)，
(P.1)--(P.5)，及上述 L2 外图中 $q_n>.9999999999993$ 的已付界。
紧支 $\nu$ 控制在此外端为零。

[完整 full-delta 负窗证明](R133-supplement-full-delta-negative-one-positive-source-and-regular-ports.md)，第 5 节，
先用实际 $L^2$ module、translation commutator 与 adjoint 得到 $L^2$ 和
$H^{-1}$ 两端界，再选择其 $H^{-5/6}$ 应用。
[实际成功记录](R133-supplement-actual-full-delta-negative-one-positive-source-graph.md)
已经通过这些同对象门。因此同一插值论证也给
$$
\boxed{\quad
\|T\|_{H^{-1/2}\to H^{-1/2}}<1/4000,\qquad
\|C\|_{H^{-1/2}\to\mathbb R}<1/32000.
\quad}
\tag{O.7}
$$
这里使用的是该证明已经控制的两端，未由单一 $H^{-5/6}$ bound 猜另一个阶数。
完整修补族 $|\delta|\le10^{-8}$ 的外图均在这份合同中；
本文的 base frame/support 仍先取已证的 $\delta=0$ Qrepair 对象。

$H^s$ 使用原归一化 Fourier 范数。因此
$$
\mathcal N^2:=\|c_\perp\|_{H^{-1/2}}^2
=\frac12\sum_{n\in4\mathbb N}\frac{c_n^2}{\langle n\rangle},
\qquad \langle n\rangle=(1+n^2)^{1/2}.
\tag{O.8}
$$
独立 height、ordinary Robin 和 mean 源在 homogeneous 核问题中取其原零数据；
它们在非齐次逆中仍是独立输入，本文没有给它们重新归一化。

## 3. 周期旋转/位置提升及准确初始角缺陷

以真实 $2\pi$ 圆上的零均值 primitive 定义
$$
\boxed{\quad
\omega_R=I_{2\pi}\{a(-cX+bY)\}.
\quad}
\tag{O.9}
$$
该 primitive 删除的是被积向量的平均；物理 $c_0$ 本身仍存在。
四重反射类及 (O.2) 给
$$
\left\langle a(-cX+bY)\right\rangle=-azc_0e_z.
$$
因此旋转能量补篇 (E.4) 的准确初值为
$$
\boxed{\quad H_R=azc_0e_z.\quad}
\tag{O.10}
$$

为逐项核对，令 $\omega_R=\omega_\rho e_r+\omega_T Y+\omega_z e_z$；下标 $T$ 是切向分量，$\omega_\theta$ 仍表示角导数。
mean 曲率产生的项为
$$
\omega_R^{(0)}=atc_0Y .
$$
每个 $n\in4\mathbb N$ 的其余项准确是
$$
\begin{split}
\omega_\rho^{(n)}
 &=-\frac{a(b_n+ntc_n)}{n^2-1}\sin n\theta,\\
\omega_T^{(n)}
 &=-\frac{a(nb_n+tc_n)}{n^2-1}\cos n\theta,\\
\omega_z^{(n)}
 &=-\frac{azc_n}{n}\sin n\theta .
\end{split}
\tag{O.11}
$$
直接用 $e_{r,\theta}=Y$、$Y_\theta=-e_r$ 即可核出 (O.9)--(O.10)。
全部分母非零，因为非mean物理频率从 $4$ 开始。

(O.11) 还给
$\langle a\omega_R\times Y\rangle=0$：水平分量由四重等变平均为零；
竖直分量的平均是 $a\langle\omega_\rho\rangle=0$。
所以可取周期位置方向
$$
\delta F_R=I_{2\pi}(a\omega_R\times Y),\qquad
\delta O_R=\omega_R\times O_R .
\tag{O.12}
$$
其位置角缺陷准确为 $p_R=0$。这给 R138 径向方向方程的明确初值，
未额外施加一组 curvature 边界条件，也没有删去 mean 或初始角缺陷。
它是当前算子分析的周期提升；实际外帽的非线性 frame/位置匹配仍按原完整构造办理。

按 (E.3) 及 R138 位置方向方程径向延拓 (O.12)，便得到与同一 base frame
一致的单一周期方向。只选了一个整体旋转和一个整体平移规范；
不是在各角或各扇区重新调整刚体。

## 4. 外端二次型的完整准确求和

对 $\lambda=F\cdot(\omega\times d\omega)$，令
$\mathcal B_R=\int_0^{2\pi}\lambda(\partial_\theta)\,d\theta$。
把 (O.11) 代入 (O.2)，所有不同 $n$ 以及 mean/nonmean 交叉项因完整角积分相消。
准确得到
$$
\boxed{\begin{split}
\mathcal B_R={}&2\pi h a^2t^2c_0^2\\
&+\pi a^2\sum_{n\in4\mathbb N}
\frac{-h b_n^2+(2ns_R-az/n)b_nc_n+t s_Rc_n^2}
     {n^2-1}.
\end{split}}
\tag{O.13}
$$
例如 mean 项来自
$\omega=atc_0Y$、
$\omega_\theta=-atc_0e_r$，其符号是正，不能删除。
(O.13) 对非mean每模同时保留 $b^2,bc,c^2$，不是只取 leading cross term。

该式先在光滑数据上成立；右侧在 $b,c_\perp\in H^{-1/2}$ 时连续，
因为 cross multiplier 为 order $-1$、两个平方项为 order $-2$。
(O.9) 相应给 $H^{1/2}$ 的旋转迹，故左侧也有一致的 Sobolev 配对定义。
完整外图的有限 Fourier 稠密延拓给同一 (O.13)，没有对未知方向作截断。

## 5. 全频负性及独立 mean 的吸收

置
$$
w_n=\frac{2ns_R-az/n}{n^2-1}.
$$
由 (O.3) 和 $n\ge4$，
$$
\frac{2s_R}{n}\le w_n\le\frac{32s_R}{15n},
\qquad
\frac{2s_R}{\langle n\rangle}
 \le w_n\le\frac{11s_R}{5\langle n\rangle}.
\tag{O.14}
$$
最后一步可用 $\sqrt{17}<33/8$。因此 $w$ 加权范数与
$H^{-1/2}$ 的正平方范数比介于 $2s_R$ 和 $(11/5)s_R$ 之间。
同一个 $T$ 在该加权空间的范数小于
$$
\sqrt{11/10}/4000<1/2000 .
$$
把 (O.5) 的全部有符号非mean行代入 cross term，(O.6)--(O.7) 给
$$
\sum_n w_n b_nc_n
\le-\left(\frac{99}{100}-\frac1{2000}\right)
       \sum_n w_nc_n^2
<-\frac{49}{50}\sum_n w_nc_n^2 .
\tag{O.15}
$$
这里的 $b_n$ 是 $J_\theta b$ 的对应实 cosine 系数；$T$ 可有全部低高混合，
不需要与 $w$ 对易。范数等价已经支付这种不对易。

$t<0,h>0$，所以 (O.13) 中另外两个 nonmean 平方项非正，可保守丢掉。
另一方面，实际 mean 行给
$$
2\pi h a^2t^2c_0^2
\le 2\pi a^2s_R(1/32000)^2\mathcal N^2 .
\tag{O.16}
$$
而 (O.14)--(O.15) 的负项不小于
$(49/25)\pi a^2s_R\sum c_n^2/\langle n\rangle
=(98/25)\pi a^2s_R\mathcal N^2$。
这严格超过 (O.16) 加 $2\pi a^2s_R\mathcal N^2$，
证明 (O.1)。这是使用真实 DN 与真实 holonomy mean 的实际负型，
不是一个未核的“若边界为负”条件。

## 6. 同一初始缺陷已被负外型控制

(O.11) 给一个方便的非最优界
$$
\|\omega_R\|_{L^2_{\rm normalized}}\le6a\mathcal N,\qquad
\|H_R\|_{L^2_{\rm normalized}}
       \le \frac{az}{32000}\mathcal N,\qquad p_R=0 .
\tag{O.17}
$$
第一式可逐项用
$\langle n\rangle^{1/2}/(n-1)<1$、$n\ge4$，
先界两水平分量及竖直分量，再用
$\|b\|_{H^{-1/2}}\le(1+1/4000)\mathcal N$ 和
$|c_0|\le\mathcal N/32000$。
它保留 mean 产生的物理频率 $1$ 旋转项。

回到旋转能量补篇使用的非归一化真实圆积分，
(O.1)、$s_R\ge9/10$ 和 $z\le1$ 于是给
$$
\boxed{\quad
\|\omega_R\|_2<7\sqrt{-\mathcal B_R},\qquad
\|H_R\|_2<\frac1{30000}\sqrt{-\mathcal B_R},\qquad p_R=0.
\quad}
\tag{O.18}
$$
这些是由已付外图直接导出的初始数据预算，不含待求正区 inverse。
若 $\mathcal N=0$，则同图给 $b=c_0=0$，此时两边均为零，按非严格不等式理解。

## 7. 去掉常量 mean 缺陷的径向导数费用

定义
$$
\mathcal M(r)=\int_0^{2\pi}F\cdot(\omega\times H)\,d\theta,
\qquad \widetilde{\mathcal B}(r)=\mathcal B(r)-2\mathcal M(r).
\tag{O.19}
$$
旋转能量补篇 (E.10)、$F_r=eX$ 和乘积法则准确给
$$
\boxed{\quad
2\mathscr Q
=\widetilde{\mathcal B}_R-\widetilde{\mathcal B}_L
 +\int\!\!\int
 \{eX\cdot(\omega\times H)
       +P\cdot(\omega\times\omega_r)
       +2F\cdot(\omega\times H_r)\}\,d\theta\,dr .
\quad}
\tag{O.20}
$$
这仅是原同一能量恒等式的分部积分，未改变未知方向、域或原端口。
它避免把外端常量 mean 缺陷 $H_R$ 直接乘上退化处未受控的 $\omega_r$；
含 base 缺陷的其余两项仍明确保留。

在 (O.10) 的真实初值处，只有 mean 贡献
$$
\mathcal M_R=2\pi a^3ztc_0^2.
$$
所以 (O.13) 的 nonmean 部分完全不变，mean 系数改为
$2\pi a^2(ht^2-2azt)c_0^2$。
因为 $t<0$、$|t|\le1$，
$$
0\le ht^2-2azt\le2s_R.
$$
第 5 节的同一严格余量因此也给
$$
\boxed{\quad
\widetilde{\mathcal B}_R
\le-2\pi a^2s_R\mathcal N^2 .
\quad}
\tag{O.21}
$$
(O.18) 同样可把右侧的 $-\mathcal B_R$ 换成
$-\widetilde{\mathcal B}_R$。这已经支付修改后外端的全部 mean 项；
没有声称修改后的内端或体误差已经满足吸收门。

## 8. 同对象齐次核的外端强窗升级

这里固定原完整 $Q^\delta$ 正区线性化及其真实外图；
第 1 节的 support 实例仍取 $\delta=0$。
令 $h=h_L+h_H$ 属于
[实际 negative-one 完整图](R133-supplement-actual-full-delta-negative-one-positive-source-graph.md)
的域，$h_L$ 为原 193 维 head，$h_L\in L^2_rE_{193}$。
假设整个齐次问题的 prescribed high stable 根输入、独立 ordinary/height/mean 外源及 affine jump 源均为零。
head 不是置零：其全部体耦合与外端低模/mean 数据均保留。

对这个具体齐次核有
$$
\boxed{\qquad
h(R)\in H^{1/6}_\phi,
\qquad (b(R),c(R))\in H^{1/6}_\theta
\subset H^{-1/2}_\theta .
\qquad}
\tag{O.22}
$$
因此 (O.1)、(O.18) 和 (O.21) 可直接用于这个原弱域中的核。

**证明。** 原体生成元保 band192；head-to-high 源只到 shell288。
这是
[实际全实参数正高逆](R133-supplement-actual-full-real-delta-outer-and-positive-high.md)
第 3 节与
[负窗合同](R133-supplement-full-delta-negative-one-positive-source-and-regular-ports.md)
(N.7) 的同一耦合。
故给定 $h_L\in L^2_rE_{193}$ 所产生的 high 普通源属于
$L^2_rH^{1/3}_\phi$，甚至属于每个有限角 Sobolev 阶。
无须给 $h_L$ 加径向光滑假设。
反向 high-to-head 只看有限 shell，故原 head 分布方程亦给分片 $H^1_r$；
其端值和完整 mean 行有定义。原域中已有的端口解释与此一致。

现在保持整个 $h_L$ 及其实际外端数据，使用
[实际 base-order 七列根到外端图](R133-supplement-actual-full-real-delta-positive-high-root-to-regular-graph.md)
第 1--5 节另构造 high 解。
全部七列都按原合同保留：stable 列为零，普通列包含刚才的完整 head 强源，
$B$ 列包含其全部外端 low/mean 输入，原齐次 affine jumps 仍为零。
所得解在整个正区满足 $Z_H\in L^\infty_r\ell^2$，且解的是同一算子、同一真实外图。
它嵌入原 $Y=M^{-1}Z$ 的 negative-one 域，满足与原解相同的七个输入。
由那份已经证明的 given-head 完整高图的唯一性，两解相同。
此处不使用尚未闭合的有限 head/high Schur，也不假定 full positive inverse。

准确状态恢复见
[全实参数图合同](R133-supplement-full-real-delta-positive-high-root-to-regular-graph.md)
(P.1) 与
[同一全局参考](R133-supplement-global-positive-reference-and-current-collar.md)
(G.6)--(G.13)：
$$
x_j=\operatorname{diag}(-i\operatorname{sgn}j,1)h_j
   =M^{-1/6}T_M Z_j,
\qquad
T_M=(p+g)^{-1/2}
\begin{pmatrix}p&-g\\1&1\end{pmatrix}.
\tag{O.23}
$$
真实外端 $1/8<p(R)<1/5$、$0<g(R)<2$，从而
$$
\|T_M(R)\|^2
\le\frac{p^2+g^2+2}{p+g}
\le p+g+\frac2p
<\frac15+2+16<25.
$$
所以原 $Z(R)\in\ell^2$ 确给 $h_H(R)\in H^{1/6}$。
有限 head 不影响此阶数。
最后，原负窗合同 (N.9) 支付了同一个完整 physical/moving chart
及其 adjoint 在 $|s|\le2$ 的乘积、primitive 和 composition；
其 physical 曲率导数转换将 $H^{1/6}_\phi$ 映到 $H^{1/6}_\theta$。
这保留独立 mean，证明 (O.22)。

若允许自由的 rough high stable 根输入，上述 base-order 重构只有在该输入亦属于强窗时才能进行，不能自动删成零。
同样，(O.22) 不给所有 $L^2_rH^{-2/3}$ 粗普通源的统一强窗界。
若使用 R138 第 6 节的 hybrid $A_c$ 而非这两份图的原同一个算子，
必须保留 (J.33)--(J.34) 的 principal 差源并另证其强窗，不能用“同中心”代替这一步。

## 9. 当前还需完成的真正内端步骤

本文将原完整外端图在同一 R138 frame 上变成了准确负型，
并把周期提升的 mean 角缺陷明确给出。它没有给原 root 行重新定义坐标。
内端仍须把原 low even96、high stable 和 mean 关系，经完整
$\mathfrak M_Q$ 及同一径向方向传播代入 (E.16)，估计其实际二次型。
内部 base residual 与物理源仍通过 (E.6)、(E.10) 进入；
(O.18) 只支付其真实外端初值，不能把全程 $H$ 设零。

第 8 节已支付同算子、零 high-stable 输入的齐次核外端能量域。
一般非齐次旧窗的定量常数及自由 rough stable 根输入仍须按其原强度办理；
外端负型本身不替代内端 193 加 high 行和残差吸收。

