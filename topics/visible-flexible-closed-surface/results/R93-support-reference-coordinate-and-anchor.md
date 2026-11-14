# R93：支撑参考换图、同一物理 g 与入口背景锚定

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

**状态：已证明的坐标和表示工具，含一个实际 warm 参考的严格可逆界。** 本文说明如何用固定的多谐波支撑参考 $c^*$ 代替纯单模材料 warp，保持同一个物理度量，并正确运输位置及全部两 jet。入口背景若同时锚到参考支撑曲线，则 R91 的有限模入口误差确实二阶于 $c-c^*$，没有额外固定 round-background 尾。本结果没有改动当前活动 M15 或已定的 M15/W22 生产计划；给出的 warm 参考不是新的联解。

## 1. 固定参考的全域角图

沿用 R91 的 $h_c,\rho_c,A_c,\Gamma_c$，令参考 $c^*$ 有限且
$\rho_*(\psi):=\rho_{c^*}(\psi)\ge r_*>0$。在 $0\le s\le L$ 取固定 $C^2$ 函数 $\chi$，满足

$$
\chi(0)=1,\qquad 0\le\chi\le1,\qquad
\chi(L)=\chi'(L)=\chi''(L)=0.
\tag{1}
$$

例如 $\chi=1-10(s/L)^3+15(s/L)^4-6(s/L)^5$ 满足这些条件，也可使用已证明范围的当前 adaptive spline 乘 cutoff。定义

$$
P_*(\psi)=A_{c^*}(\psi)-\psi,
\qquad \Theta_*(s,\psi)=\psi+\chi(s)P_*(\psi).
\tag{2}
$$

则

$$
\rho:=\partial_\psi\Theta_*
=(1-\chi)+\chi\rho_*(\psi)
\ge\min(1,r_*)>0.
\tag{3}
$$

因此每个 s 上 $\Theta_*$ 都是定向保持的圆周微分同胚。它满足
$\Theta_*(s,\psi+2\pi)=\Theta_*(s,\psi)+2\pi$，由逆函数定理，逆图对 $(s,u)$ 联合 $C^2$。这里不要求参考是某个已完成二维解；正的 $\rho_*$ 即足以给出真实角坐标。

在 s=L，角图与恒等图的全部两 jet 相同：

$$
\Theta_*=\psi,\quad \Theta_s=\Theta_{ss}=\Theta_{s\psi}
=\Theta_{\psi\psi}=0,\quad\Theta_\psi=1.
\tag{4}
$$

所以 cut 上的尾部材料角、所有物理 Fourier 模式及两 jet 不改变。若在中心 s=0 反射拼接两半，另取 $\chi'(0)=0$，则 $\chi(|s|)$ 是 $C^2$，因为其一阶左右极限同为0、二阶左右极限同为 $\chi''(0)$；无须增加 $C^3$ 条件，也无须强迫 $\chi''(0)=0$。

## 2. 物理度量完全相同

固定物理材料坐标 $(s,u)$，原度量为

$$
g=ds^2+a(s)^2du^2.
\tag{5}
$$

用 (2) 写它，仅得到同一张量的坐标表达

$$
g_*=(1+a^2\Theta_s^2)ds^2
+2a^2\Theta_s\rho\,ds\,d\psi+a^2\rho^2d\psi^2.
\tag{6}
$$

物理正交方向仍是

$$
D_s=\partial_s-\frac{\Theta_s}{\rho}\partial_\psi,
\qquad a^{-1}D_u=\frac1{a\rho}\partial_\psi.
\tag{7}
$$

这没有改变 a、尾部 source、物理层、支撑幅度未知量或时间族的物理范围。$c^*$ 是写同一材料角的固定参考数据，不是通过调整物理 `warp_reference` 来更换 g。

更具体地，设旧图材料角为 $\Theta_o(s,\xi)$，也有正角导数。定义唯一的

$$
\Phi(s,\psi)=\Theta_o(s,\cdot)^{-1}(\Theta_*(s,\psi)).
\tag{8}
$$

若原实际映射在旧图写成 $F_o(s,\xi)$，则

$$
F_*(s,\psi)=F_o(s,\Phi(s,\psi))
\tag{9}
$$

就是同一个物理映射在新图的表达。每个时刻的像、直径、Hausdorff 变化、嵌入性和 reach 都不变；固定 H 只随参数图运输。式 (4) 允许在尾、圆领和固定帽上把坐标变化接成恒等；中心用上一节的 C² 反射规则。于是它同样适用于原有闭曲面的公共图册。

相对 metric 算子误差也准确不变。若 J 是坐标变换的可逆微分，误差张量和目标分别变成 $J^T\Delta g J$ 与 $J^TgJ$。其最大绝对 Rayleigh 商满足

$$
\sup_{v\ne0}\frac{|v^TJ^T\Delta gJv|}{v^TJ^TgJv}
=\sup_{w\ne0}\frac{|w^T\Delta gw|}{w^Tgw},
\tag{10}
$$

因为 $w=Jv$ 是双射。因此坐标变换本身既不能隐藏原图的 metric 缺陷，也不会给同一图创造新缺陷。

## 3. 全部两 jet 的材料运输

以下旧图的量都在 $(s,\Phi(s,\psi))$ 评价。记 $\rho_o=\partial_\xi\Theta_o$。从
$\Theta_o(s,\Phi)=\Theta_*(s,\psi)$ 逐次求导，得到

$$
\Phi_\psi=\frac{\Theta_{*,\psi}}{\rho_o},\qquad
\Phi_s=\frac{\Theta_{*,s}-\Theta_{o,s}}{\rho_o},
\tag{11}
$$

$$
\begin{aligned}
\Phi_{\psi\psi}&=
\frac{\Theta_{*,\psi\psi}-\Theta_{o,\xi\xi}\Phi_\psi^2}{\rho_o},\\
\Phi_{s\psi}&=
\frac{\Theta_{*,s\psi}-\Theta_{o,s\xi}\Phi_\psi
-\Theta_{o,\xi\xi}\Phi_s\Phi_\psi}{\rho_o},\\
\Phi_{ss}&=
\frac{\Theta_{*,ss}-\Theta_{o,ss}-2\Theta_{o,s\xi}\Phi_s
-\Theta_{o,\xi\xi}\Phi_s^2}{\rho_o}.
\end{aligned}
\tag{12}
$$

所有分母由角图正性支付。对 (9) 的正确 Cartesian 链式法则是

$$
\begin{aligned}
F_{*,\psi}&=F_{o,\xi}\Phi_\psi,&
F_{*,s}&=F_{o,s}+F_{o,\xi}\Phi_s,\\
F_{*,\psi\psi}&=F_{o,\xi\xi}\Phi_\psi^2+F_{o,\xi}\Phi_{\psi\psi},\\
F_{*,s\psi}&=F_{o,s\xi}\Phi_\psi+
F_{o,\xi\xi}\Phi_s\Phi_\psi+F_{o,\xi}\Phi_{s\psi},\\
F_{*,ss}&=F_{o,ss}+2F_{o,s\xi}\Phi_s+
F_{o,\xi\xi}\Phi_s^2+F_{o,\xi}\Phi_{ss}.
\end{aligned}
\tag{13}
$$

这些式子保留平流、混合二阶和旋转基项；如果旧数据以圆柱分量保存，应先形成相应 Cartesian jet 或同时求基向量导数。直接把同一角数组换个名字不等于 (13)。

在 cut，旧、新角图都有 (4)，故 $\Phi=\psi$、$\Phi_\psi=1$，其余非平凡一、二阶导数都为零。于是 (13) 原样保留 terminal 完整两 jet，已有真实 DN 的物理角定义不受换图影响。

## 4. 入口背景锚定去掉固定 round 尾

R91 已证明：固定新参考图 $u=A_{c^*}(\psi)$ 后，若所有支撑频率不超过 M，

$$
\Gamma_c(A_{c^*}(\psi))=
\gamma_{c^*}(\psi)+L_{c^*}(c-c^*)(\psi)+\mathcal R_{c-c^*}(\psi),
\tag{14}
$$

其中基线和线性项都在圆柱 M 空间，$\mathcal R$ 是 R91(20) 的准确 Taylor 积分余项，且其 C¹ 范数满足 R91(21)–(22) 的二阶界。

若仍用未截断圆背景 $e^{iA_{c^*}(\psi)}$，R91(25) 中的固定背景尾不能删除。现在明确选择入口背景

$$
B_*(0,\psi)=\gamma_{c^*}(\psi).
\tag{15}
$$

初始有限表示定义为

$$
\widehat F_M(0,\psi)=B_*(0,\psi)+
P_M[\Gamma_c(A_{c^*}(\psi))-B_*(0,\psi)].
$$

于是由 (14) 和投影恒等直接得到

$$
\boxed{\quad
\widehat F_M-\Gamma_c=-(I-P_M)\mathcal R_{c-c^*}.
\quad}
\tag{16}
$$

特别地 $c=c^*$ 时，入口是准确的有限支撑曲线，其角导数为 $\rho_*e_\theta$，理想相对 G 缺陷准确为零。它不是由增大物理层数或改 g 把固有误差压小。

更一般地，若 R91(23) 给 (16) 的导数差上界 $\varepsilon$，则准确曲线满足 $|\Gamma_c'|=\rho_*$，所以

$$
\left|\frac{|\widehat F_M'|^2}{\rho_*^2}-1\right|
\le\frac{2\varepsilon}{r_*}+\frac{\varepsilon^2}{r_*^2}.
\tag{17}
$$

因此在固定 M、共同正曲率半径邻域内，它确实二阶于 $c-c^*$。这首先是连续 Fourier 的准确陈述；精确 N 点投影也有同一二阶性质，因为它对有限基线和线性项严格重现，离散线性投影只作用于二阶余项。若要实际数值上界，应使用该有限投影自己的算子范数或直接从保存的入口系数计算；binary 存储与三角求值舍入仍另计。

## 5. 在内部平滑回到原 round 背景

锚定并不要求把整个前缀都当作缩放支撑柱。取另一个固定 $C^2$ 函数 $\eta$，满足

$$
\eta(0)=1,\quad\eta'(0)=\eta''(0)=0,
\qquad\eta(L)=\eta'(L)=\eta''(L)=0.
$$

同样的五次 $1-S(s/L)$ 即可使用。写
$U=e^{i\Theta_*(s,\psi)}$、$\gamma_*:=\gamma_{c^*}(\psi)$，并定义水平背景

$$
C=(1-\eta)U+\eta\gamma_*,\qquad
B_*(s,\psi)=a(s)C(s,\psi),
\tag{18}
$$

竖直背景仍为零；整体竖直均值按照原方程积分。当前 $a(0)=1$，故 (15) 成立。在 cut，$B_*$ 与 $a(s)e^{i\Theta_*}$ 的全部两 jet 相同，并由 (4) 与原 round 背景接合。

为使后续实现的导数明确，下面列出所需公式：

$$
\begin{aligned}
C_\psi&=(1-\eta)U_\psi+\eta\gamma_*',&
C_{\psi\psi}&=(1-\eta)U_{\psi\psi}+\eta\gamma_*'',\\
C_s&=(1-\eta)U_s+\eta'(\gamma_*-U),\\
C_{ss}&=(1-\eta)U_{ss}-2\eta' U_s+\eta''(\gamma_*-U),\\
C_{s\psi}&=(1-\eta)U_{s\psi}+\eta'(\gamma_*'-U_\psi),\\
C_{s\psi\psi}&=(1-\eta)U_{s\psi\psi}+\eta'(\gamma_*''-U_{\psi\psi}).
\end{aligned}
\tag{19}
$$

这里 $U_s=i\Theta_sU$、$U_\psi=i\rho U$、
$U_{ss}=(i\Theta_{ss}-\Theta_s^2)U$、
$U_{\psi\psi}=(i\rho_\psi-\rho^2)U$、
$U_{s\psi}=(i\rho_s-\rho\Theta_s)U$，以及

$$
U_{s\psi\psi}=
[i\rho_{s\psi}-2\rho\rho_s+i\Theta_s(i\rho_\psi-\rho^2)]U.
\tag{20}
$$

再用 $B_*=aC$ 的乘积法则，例如
$B_{*,ss}=a''C+2a'C_s+aC_{ss}$、
$B_{*,s\psi\psi}=a'C_{\psi\psi}+aC_{s\psi\psi}$。
混合 $(s,\psi,\psi)$ 导数只用一次径向导数和有限 Fourier 的角导数；没有对全题增加径向 C³ 条件。

如果写未知曲线为 $F=B_*+qY$，完整几何速度仍是原同一物理 Frenet 方程

$$
W=V_{\rm normal}+\frac{\Theta_s}{\rho}F_\psi.
$$

有限模右端相应为 $Y_s=q^{-1}P_M(W-B_{*,s})$，均值仍按原定义另积。这里改变的是有限表示的已知背景，不是目标 g 或完整未截断方程。旧 finite map 的准确换图是 (9)，而把换图后数据再次有限投影通常只是新初猜；必须重新求真正的非线性解，不能把该重新投影称为等距新曲面。

## 6. 当前 M15 warm 给出的具体可逆参考

选择现有 `2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz`（SHA256 `cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc`）中的参考：第一系数取其保存的 `actual_primary_amplitude`，其余系数取保存参数与保存尺度的 binary64 乘积，随后全部作为精确 dyadic 数定义 $c^*$。这是一个明确的坐标参考，不声称该 warm 已解。

由 $|\cos|\le1$，全圈严格有

$$
\rho_*(\psi)\ge1-\sum_{j=1}^{15}(9j^2-1)|c_j^*|
>\frac{192273551481}{10^{12}}>0.19.
\tag{21}
$$

沿用该保存对象自己的 adaptive scalar chart，按既有目标供应器的**精确有理 clamped spline** 定义 $\chi$，在 normalized $s/L=3/4$ 后乘原五次 cutoff。它的全部 spline knots 及 $3/4$ 将区间分段，每段再八分，得到520个有理小区间。每个多项式由幂基转为 Bernstein 基；基函数非负且和为1，所以系数最小/最大值包围该段全域。实际有限 Fraction 算术给

$$
0\le\chi(s)\le1
\tag{22}
$$

准确成立，因而 (21) 同时是完整 s 范围的新角图的正下界。它不是从有限采样估计 spline 的极值。

相对原纯参考 $q_{ref}=\mathrm{binary64}(0.1)$，同一三角和还给

$$
\|\Theta_* -\Theta_o\|_\infty
\le {1196458679\over10^{12}}<0.001197,
\tag{23}
$$

$$
\|\partial_\psi\Theta_* -\partial_\psi\Theta_o\|_\infty
\le {966272827\over125000000000}<0.007731.
\tag{24}
$$

证明分别使用 $\sum_j|(1-9j^2)(c_j^*-c_j^o)/(3j)|$ 和
$\sum_j|(1-9j^2)(c_j^*-c_j^o)|$，再乘 (22)。所以这给出的是一个具体、全圈且全径向可逆、与旧图接近的参考。

还可由旧图的 $\rho_o\ge1-w$ 得出换图本身

$$
\|\Phi-\psi\|_\infty
\le\frac{1196458679/10^{12}}{1-w}<0.006.
\tag{25}
$$

这里取同一周期提升。旧 $\rho_o$ 对角的 Lipschitz 常数至多 $3w$，所以由 (11)、(23)、(24)

$$
\|\Phi_\psi-1\|_\infty
\le\frac{D_\rho+3wD_A/(1-w)}{1-w}<0.111,
\tag{26}
$$

其中 $D_A,D_\rho$ 是 (23)–(24) 的有理上界，w 为 R91(15) 的 exact binary 值。末两不等式可直接对这些有理数交叉相乘验证。

实际程序为 [78718-geometry-reference-support-chart.py](../scripts/78718-geometry-reference-support-chart.py)，4845 B，SHA256 `9e5773c1527f42e0545ff9e228d3894558e0c1809e5d068ab54d0b51d98ef229`；实际 **154645 自然 exit0**，约0.44秒。报告为
[2026-11-10-78718-geometry-m15-warm-reference-support-chart.json](../notes/2026-11-10-78718-geometry-m15-warm-reference-support-chart.json)，3161 B，SHA256 `ec8cefe7111a57a9fa1152206d808b83e8b9d83969b5612f6951c24b78b4caa3`。
报告保存参考系数和有限标量，不生成新曲面；0 BVP、0 DN。

### 6.1 对这个参考，仅换 warp 的理想 M15 表示确实超过原目标

这一条专门说明第4节 anchor 的实际作用；所研究的表示尚未用于生产，不能把本结论写成当前原 warp 的 M15/W22 失败。

固定上述 $c^*$，取 $c=c^*$、M=15，入口材料图为 $u=A_{c^*}(\psi)$，但仍采用原“未截 round 背景加投影”形式。令 $z=e^{3i\psi}$，

$$
P(z)=\sum_{j=1}^{15}\frac{(1-9j^2)c_j^*}{6j}(z^j-z^{-j}),
\qquad E=e^P,\qquad E_{16}=\sum_{n=0}^{16}\frac{P^n}{n!}.
\tag{27}
$$

R91(25) 在 $c=c^*$ 时只剩背景尾。取 Laurent 系数绝对和范数，记
$A=\|P\|_{\mathcal A}$、$B=\|z\partial_zP\|_{\mathcal A}$。由幂级数逐项求导和几何尾，

$$
\|E-E_{16}\|_{\mathcal A}\le
\varepsilon_0:=\frac{A^{17}}{17!\,[1-A/18]},
$$
$$
\|z\partial_z(E-E_{16})\|_{\mathcal A}\le
\varepsilon_1:=\frac{BA^{16}}{16!\,[1-A/17]}.
\tag{28}
$$

本参考 A 满足分母为正。写 $E_{16}=\sum f_jz^j$。背景尾的物理角导数多项式为

$$
S_{16}(z)=\sum_{|j|>15}(1+3j)f_jz^j.
$$

连续投影的导数余项至多 $\varepsilon_0+3\varepsilon_1$。精确 N2048 投影的 alias 只可能来自 $|j|\ge2048-15=2033$，而 $E_{16}$ 的次数至多240；故 alias 完全来自余项，其导数影响至多 $46\varepsilon_0$，使用 R91(12) 的互不重复折叠系数。于是实际精确节点模型的尾 S 满足

$$
|S(z)-S_{16}(z)|\le
\varepsilon:=47\varepsilon_0+3\varepsilon_1,
\qquad |z|=1.
\tag{29}
$$

在两轴 $z=1,-1$，所有量为实数。精确 G 误差为

$$
G-1=\left(1+\frac{S}{\rho_*(\psi)}\right)^2-1.
\tag{30}
$$

把 S 置于 $[S_{16}-\varepsilon,S_{16}+\varepsilon]$。同一次有理计算已证这个区间的绝对值小于 $\rho_*$，因此 (30) 在该区间严格递增，直接代入两个端点就得到严格有符号上下界。这没有把 FFT 采样当作全角证明。

使用 (27) 的准确有理多项式，实际得到在 $\psi=0$ 时

$$
\boxed{\quad
G-1>
\frac{4192408365956328056743}{10^{30}}
>4.19\cdot10^{-9}>2\cdot10^{-9}.
\quad}
\tag{31}
$$

另一轴的值约 $-1.96098\cdot10^{-10}$；全角上界至多 $4.592\cdot10^{-8}$。这准确地区分了证实超目标的点态下界与较保守的全角上界。两轴估计中的 C¹ 截断余项约 $2.81\cdot10^{-23}$，alias 余项约 $2.47\cdot10^{-23}$；所有最后有符号界用 Fraction 运算，而非这些显示小数决定。

因此，对于这个具体参考，单独换 warp 后继续旧 round split，连其理想精确算术模型都仍有大于原目标的入口缺陷；(15)–(16) 的背景 anchor 正好消除这一个固定尾。此结论不涉及实际代码新三角表的舍入，更不否决原材料图下正在求解的曲线。

完整方法为 [78718-geometry-reference-round-tail-v2.py](../scripts/78718-geometry-reference-round-tail-v2.py)，4240 B，SHA256 `150edc65964a7377da7ef197c01ab4a07c7b93f9b18ca3a39335c2fcd426f173`。实际 **be28a9 自然 exit0**，约1.18秒；报告
[2026-11-10-78718-geometry-m15-reference-round-tail-v2.json](../notes/2026-11-10-78718-geometry-m15-reference-round-tail-v2.json)，2428 B，SHA256 `89f384447574c99e9397c08541332889ad8e98c0cbaa10c5b195943fc533397f`。
原只算上界的 v1 运行 222c62 自然 exit0，其源码和报告仍保存；两次均0 BVP、0 DN。

## 7. 后续实际使用的准确范围

参考 $c^*$ 在一次求解中固定。因此目标坐标、已知背景及其参数导数都固定；未知 c 只进入原支撑入口和真正的曲线未知量。若以后从一个实际输出选择更新的 $c^*$，应先按 (8)–(13) 运输已有曲线及其 jet，再形成新的有限初猜并真正重求。若在一次 Newton 过程中让参考随未知参数偷偷变化，却沿用旧 Jacobian，就已不是本文的固定参考方法。

本稿给出了同一物理 g 的合法坐标改进及入口二阶误差机制。它没有证明内部 nonlinear Galerkin 误差变小、没有给新 DN 响应，也没有给完整闭面的 reach 或收敛。在当前主计算及已安排的下一次 M15/W22 中仍保留原材料 warp；只有实际新 prefix 的误差定位确有需要时，才考虑采用这一工具。
