# R36：在同一46模盒中吸收真实非线性深图的低端反馈

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**已证明。** R35 的同一真实头部、同一46个浅高度和同一非等半径
盒，允许把 far 处的46个实际**线性**斜率条件替换为 R18 **完整
非线性深图的低46斜率投影**。这是一个联合边界固定点：深端低
高度随头部校正改变，反馈项也随之改变，不是只在参考高度上
一次性加入边界差。

新增映射仅消耗 R35 现有盒不变性余量的不到 $2^{-194}$，新增
Lipschitz常数小于 $2^{-217}$。因此原盒继续不变，总收缩常数
仍小于 $4/5$，新的辅助边值问题在该盒中唯一有解。

**范围。** 深图 $\Gamma$ 是 R18 的完整全频图，构造时保留
全部高模与mean；本结果只将其低斜率投影装入46模辅助头部。
高深迹、头部自产无限高频及完整mean在接缝的匹配仍待 R33
联合问题支付。不能从本结果宣称完整头部已与深尾 $C^2$ 接合。
外0..11胞元、实际强H向量和强前缀仍不在本结果内。

## 1. 完整深图和其二次差

令 F224 对应 physical node225，取 $\tau_F=38$。沿用

$$S_F=\epsilon\delta_{224}^{11/2}/r_c^3,
\qquad z_j=e^{38(2j)}Q_{2j}(F224)/S_F.$$

这里 $(-1)^{224j}=1$，无额外相位。设

$$\mathcal D(z)=\Gamma_{224}(z)-\Gamma^{\rm lin}_{224}(z).$$

R18 给出完整raw范数界

$$\|\mathcal D(z)\|\le C_D|z|_1^2,\qquad
C_D=2^{1967},\quad |z|_1\le2^{-1947}.
\tag{36.1}
$$

低46高度分量严格为0；低46斜率及全部高频高度/斜率都在
$\mathcal D$ 内。R15/R18 已在共同复球上建立完整图的全纯性。
因此在 $|z|\le Z\le2^{-1948}$ 内，由半径Z的复方向圆盘，

$$\|D\mathcal D(z)\|\le4C_D Z.
\tag{36.2}
$$

具体地，圆盘内参数模长至多2Z，故 (36.1) 的上界为
$4C_DZ^2$，Cauchy导数估计再除Z。零点由二次消失得到同样结论。
这使用已证明的复球估计，不是把一个实数函数值界直接微分。

记 $\mathcal D_{\rm lo}$ 为低46的斜率投影。投影范数至多1，
所以 (36.1)–(36.2) 原常数继续成立。

## 2. 准确的边界提升

在一个低模上令 $\phi$ 是实际线性深子空间的列，归一为
$\phi_Q(a)=1$，$a=r(F224)$；令 $\psi_Q(b)=0$、
$\psi_{\Xi,12}(b)=1$，$b=r(\mathrm{node12})$。其物理Wronskian

$$W_m=\mu_{12}\phi_Q(b)$$

严格非零，全部46模都由 R29 已算出的真实有符号列支付。
若深端canonical斜率缺陷为 $d_m^{\rm phys}$，则齐次浅高度的
准确提升是

$$\mathcal B_m d_m^{\rm phys}(r)
=\frac{\mu_{224}}{W_m}\psi_m(r)d_m^{\rm phys}.
\tag{36.3}
$$

证明是直接检验：$\psi_Q(b)=0$；实际线性深斜率记 $t_m$，则

$$\psi_\Xi(a)-t_m\psi_Q(a)=W_m/\mu_{224}.$$

所以 (36.3) 的far斜率缺陷恰为 $d_m^{\rm phys}$。
这保留了连续物理动量的 $\mu$ 因子，未把不同胞元canonical
$\Xi$ 当作同一个分量。

对归一输入 $d_m=(\mathcal D_{\rm lo})_m$，应代入

$$d_m^{\rm phys}=S_Fe^{-38m}d_m.$$

因此在cell k的 R35 范数中，一个实际可计算上界是

$$
K_k=\max_{m=2,4,\ldots,92}
\frac{\mu_{224}S_F}{\mu_{12}|\phi_Q(b)|}
e^{(\tau_k-38)m}
\left[(1+m)^3\sup_k|\psi_Q|
+(1+m)\sup_k|\psi_\Xi|\right].
\tag{36.4}
$$

两分量sup分别计算。cells12/13使用 R35 的逐面板真实sup，其余
胞元使用原真实有符号列和合法局部包络。取对角Fourier块的
最大值后，得到 $X_k(\mathcal B d)\le K_k|d|_1$，无需乘46。

## 3. 同一盒的参数评估与反馈常数

记 R35 的参考上界、盒总半径与距离权为 $x_k,U_k,W_k$。
准确深端低高度评估算子 $\mathcal E$ 在其距离中满足

$$|\mathcal E(V-\widetilde V)|_1
\le e_D\,d(V,\widetilde V),$$
$$e_D=\frac{W_{224}x_{224}}{S_F}
\max_{m=2,4,\ldots,92}
 \frac{e^{(38-\tau_{224})m}}{(1+m)^3}.
\tag{36.5}
$$

全部46模参加最大值，最坏模仍为m92。这是有限角频的准确
范数转换，没有省略高38个自由低参数。

在同一距离中，边界提升常数可取

$$b_D=\max_k\frac{K_k}{W_kx_k}.
\tag{36.6}
$$

R35整个盒已证明 $|z|_{38}<2^{-2203.2158}$，故本结果保守取

$$Z_*=2^{-2203}.$$

严格区间计算给

$$\log_2b_D<2214.046525,\qquad
\log_2e_D<-2197.6662471.
\tag{36.7}
$$

这些单独的数值很大或很小，是给定归一规范的结果；实际反馈
由它们和 $C_DZ_*$ 的乘积决定，不能单看 $b_D$ 判断失稳。

由 (36.1)–(36.2)，边界映射在原盒的大小与Lipschitz界分别为

$$X_k(\mathcal B\mathcal D_{\rm lo}(z))
\le K_kC_DZ_*^2,$$
$$L_{\rm bd}\le4b_DC_DZ_*e_D<2^{-217.6197}.
\tag{36.8}
$$

原R35每行的不变性余量记

$$s_k=U_k-1-\sum_nA_{kn}U_n^2>0.$$

逐行直接比较，而非只用最小全局余量，得到

$$\max_k\frac{K_kC_DZ_*^2}{x_ks_k}
<2^{-194.2772}<1.
\tag{36.9}
$$

所以新增边界项严格小于原来每一行的剩余盒半径。

## 4. 新的联合固定点与准确边界条件

在 R35 同一连续场范数中，取满足物理接口连续性和齐次浅高度
的闭子空间，再施加相同盒不等式；**不预先要求迭代输入满足线性
far条件**。R35 的源、小球、余量和距离界都只使用盒内范数，
不依赖该预先约束。新的far条件由固定点方程自身施加。
在这个同半径盒中定义

$$\mathcal T(V)=G\Pi_{46}N(Y^0+V)
+\mathcal B\mathcal D_{\rm lo}
  \bigl(z^0+\mathcal EV\bigr).
\tag{36.10}
$$

第一项是 R35 已证明的完整mean点态源投影。第二项每次都在
当前低深高度上求 R18 的真实非线性图。

(36.9)使新映射仍将原盒映入自身；(36.8)和R35给总Lipschitz界

$$L_{\rm total}\le0.749997627237571+2^{-217.6197}<4/5.$$

因此同一完整距离空间上的Banach定理给唯一固定点。其浅端
高度没有变化，而深端低46斜率满足

$$\Xi_{2j,\rm phys}(a)
=S_Fe^{-38(2j)}\Gamma_{\Xi,j}\bigl(z(Y^0+V)\bigr),
\qquad1\le j\le46.
$$

这一等式是真实图的低投影，不是带容差Robin
近似或仅在原参考 $z^0$ 上评价的固定外力。

由于盒未扩大，全部R23小球和R34深图定义域继续成立。正则性
及完整mean根沿用R35，但头部高模式尚未进入辅助微分方程，
所以完整mean与完整高trace的接缝等式仍不能从低投影等式推出。

## 5. 完整mean的同时记录

在同一个 $Z_*$ 上，程序另外按 R18 (9.7)–(9.8)记录

$$|\kappa_0(a)|\le2^{99}\epsilon\delta_{224}^{33/4}Z_*^2,$$
$$|\overline v(a)-\overline v(r_c)|
\le r_c2^{853}\epsilon\delta_{224}^{25/4}Z_*^2.
\tag{36.11}
$$

这是完整真实深尾的slope和唯一cuff高度规范，不把它们设为0。
本结果没有将这两个界偷换成头部mean已匹配；后续全频头部应
保留同一个通量小根并沿全尾积分一次，不能逐圈重置高度。

## 6. 算术与复现

入口 `computations/closure_nonlinear_low_far_lift.py` 从同一真实
列组、R35逐面板盒和已付非等半径证书出发；核对六个列组及
输入SHA。所有标量边界、sup与乘积均用192位Arb向外包围。
完整 $K_k$、主导模、逐行余量消耗、$b_D,e_D$ 和mean界保存于
`notes/2026-11-12-closure-nonlinear-low-far-lift.json`。

```bash
python computations/strong_resource_run.py \
  --out notes/2026-11-12-closure-nonlinear-low-far-lift-resource.json -- \
  python computations/closure_nonlinear_low_far_lift.py \
  --columns notes/2026-11-12-closure-real-linear-q003-low46-recovered.json.gz \
  --ordered notes/2026-11-12-closure-ordered-green-low46-v2.json.gz \
  --reference notes/2026-11-12-closure-variable-reference-farball.json \
  --box notes/2026-11-12-closure-anisotropic-low46-box.json \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --out notes/2026-11-12-closure-nonlinear-low-far-lift.json
```

会话29303正式 exit0；wait4记录也为exitcode0，8.56377秒、峰
RSS92880KiB。代码及全部实际输入的SHA在结果中保存。

## 7. 仍须支付的完整问题

R18同时给出的非零高频深迹应成为头部的内端两分量数据；浅端
高频高度必须由全解产生。完整头部的高频非线性源需要R33的
逐模径向密度和无限频带界，不能把本结果的46模投影结论外推。
低边界反馈如今已经实际支付，可作为全频联合固定点的一个稳定
块使用，但未替代那些高频块、外头、强幅或全时空间证书。
