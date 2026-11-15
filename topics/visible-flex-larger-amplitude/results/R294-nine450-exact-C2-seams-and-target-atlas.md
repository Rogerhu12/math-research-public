# R294：九控制 450 场的准确全局 C² 拼接与同一目标图册的兼容责任

2026-11-15，geometry，GPT-6 Astra Pro，AI-assisted。

**状态：完整结构定理与条件定理，已证明；没有新的科学执行或实际场证书。** 本文将已发表的九控制 SavedPrefix、shared-B 闭组装和准确有限场解释器接成一个完整接缝论证。它支付的是由具体构造保证的恒等式，明确分离原目标度量仍需满足的图册条件。没有已接受九控制 450 场时，本文不填造节点、误差、曲率、reach、握持幅度或通过标志。

主要结论是：**共享准确节点 Hermite、完整角函数切口修补、R249 中央反射和真实 cuff/帽边界条件，可以给整个闭材料面上的 $C^2$ 相位族；这一几何结论不要求离散 ODE 残差为零，也不要求标量求值器返回的 ap/app 恰为其半径公式的真实导数。** 后一种导数关系却不能在目标图册拼接时省略。内 cuff 的模型 C 平延拓，与最外 natural $R_{\rm out}$ 的非平端口，也必须区别。

## 294.1 对象、源码及本条实际新增量

本文针对以下原链：

- 九控制 450 的真实接受件由 [e8deb SavedPrefix](../computations/geometry_20261115_nine_control_same_metric_saved_prefix.py) 读取；
- [69bb shared dispatch](../computations/geometry_20261115_nine_control_shared_closed_dispatch.py) 保全部九标量系数、同一材料核心、原完整 native 尾、R249 入口规范形和新 shared guard；
- [675 ExactFiniteField](../computations/geometry_20261115_shared_active_interval_balls.py) 从该七元组解释准确有限函数；
- 两帽使用 [a3ada 的原图表达](../computations/geometry_20261115_fixed_cap_rational_balls.py)，新九控制 loader 身份按已发表的专用 binder 保留；
- 目标前缀标量由完整九控制实表达给定；若采用尾模型 C，则其定义及模型层选择按 [R286](R286-original-stored-continuous-integral-and-metric-bridge.md)，不是令 $g$ 等于 $1+(B')^2$。

本次实际只读的关键源码身份如下。这里 SHA 识别定义；没有把一个 hash 当作尚未产生的实际场。

| 文件 | SHA256 |
|---|---|
| geometry_20261115_shared_active_interval_balls.py | 675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b |
| geometry_20261115_nine_control_same_metric_saved_prefix.py | e8deb4136dbaf021d2648e02a2cdb774db4ebe1836b239b609472c596fc70404 |
| geometry_20261115_nine_control_shared_closed_dispatch.py | 69bbba2647b2356f2c4023c74a938e29d1b93effcb1c99385fdaa73b78b9d17d |
| geometry_20261114_large_core_saved_prefix.py | 51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0 |
| geometry_20261114_shared_background_normal_form.py | da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9 |
| geometry_20261114_shared_background_closed_assembly.py | ac635c11aa31925a4175876ffa2c8b959766629aebf9e3abaf97a68ca0e096cb |
| geometry_20261114_large_core_closed_assembly.py | e70d27a92bf153e49e50016706db854b339d96d3414d7f4c00a5993e1f7609c0 |
| geometry_20261114_inlet_parity_normal_form.py | ce5f287c1de870b6bf71d1650d6942e23fd2bdd23a25af72ec5b637599a97410 |
| geometry_20261114_full_prefix_operator.py | a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703 |
| geometry_20261115_small_core_nine_control_family.py | 086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629 |
| geometry_20261115_nine450_scalar_interval.py | 0c4353d18f1b6b2290cac6907c26a78f04d17909b3a9c83aeac696f29a44f6a0 |
| geometry_20261115_nine450_shared_field_relative_metric.py | 4b13425a34d8de2d168632fa0c24474542257e51fb60c2ed5a0b8501beadc975 |
| geometry_20261115_fixed_cap_rational_balls.py | a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e |
| geometry_20261115_stored_continuous_E_cover.py | 9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed |

原完整标量的来源还包括 full_scalar_profile 的 8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b、prefix_controls_profile 的 f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24 和 lifted_modes_profile 的 13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5。后两者只改变原三个控制的支撑和独立频率身份；九控制解释器保其真实嵌套表达。

已付结果的使用范围是：

| 已有结果 | 本文直接使用 | 本文新增 |
|---|---|---|
| [R249](R249-shared-node-inlet-parity-normal-form.md) | 入口投影、准确共享节点定义、原 $g$ 下修补费用 | 将入口与完整 tail/cut/collar/两帽接成一份全局结构定理 |
| [R248](R248-finite-C2-phase-family-and-global-reductions.md) | 共同材料面、强 $C^2$ 相位连续性及已声明全相位归约 | 逐项核本次 675/69bb 函数满足哪些结构前提 |
| [R282](R282-local-cross-Gram-cuff-charts-and-complete-phase-responsibility.md) | 物理角到共同材料角及真实 cuff 图 | 不重证其局部交叉 Gram 或完整点对责任 |
| [R279](R279-finite-field-direct-continuous-curvature-certificate.md) | 同一准确有限场的直接曲率判据 | 不以曲率点态判据代替接缝恒等式 |
| [R251](R251-direct-relative-operator-metric-certificate.md) | 同一目标的四 Loewner/算子比较 | 给目标在同一 seam atlas 中的完整兼容式 |
| R286 | 原冻结来源下模型 C 的连续 $E_*$ 与内 cuff 平端 | 明确最外端非平公式、不能使用的延拓及与前缀 atlas 的差项 |

### 294.1.1 四种对象不得混为一谈

1. 保存的有限节点、RHS、二阶节点 jet、FFT 系数，是所选有限函数的定义数据，也有原求解的来源身份。
2. PhysicalQuintic 的 longdouble 系数、节点覆盖分支及浮点三角函数，是一个数值求值器；它不是自动具有精确端点恒等式的实函数证明。
3. 675 的准确有限函数，把共享节点的 binary64 数解释为 dyadic 实数，再准确重建 Hermite；使用完整实际 FFT 节点、准确 shared-B、准确三角函数及完整切口修补。以下几何定理针对它。
4. 同一个参考 $g$ 是独立对象。前缀的完整九标量、尾的原目标来源/明确模型 C、帽的原图 target 均须保留；不能由第3项的 $B'$ 反过来定义一个更易通过的 $g$。

因此，准确有限函数的结构 $C^2$ 不会把数值 renderer 的逐位输出、原连续 BVP 解及本次后处理函数说成完全相同的对象。与浮点 renderer 的误差仍是另一个可计算责任。

## 294.2 共同材料面、完整角映射和换图

记中央到物理切口的前缀参数为 $s\in[0,L]$。尾的物理半径为 $r\in[c,R]$，其中 $c>0$ 是 cuff，$R$ 是当前实际闭场 cut。两片通过中央反射圆接合；各尾的 cuff 与各自一张 Cartesian 闭圆盘粘合。仅按这些已指定边界身份取商，得到连通闭材料面，拓扑为两张圆盘与一个圆柱的通常粘合，因而为球面。这里只讨论材料拓扑，不由它推出像嵌入。

保所有实际核心系数，定义

$$
\Phi(\phi)=\phi+\sum_{m=1}^{M}\frac{(1-4m^2)c_m}{2m}\sin(2m\phi),
\qquad
\rho(\phi)=\Phi'(\phi)\ge\rho_*>0.
\tag{294.1}
$$

当前 SavedPrefix 使用已有 R237 完整圆上的严格下界；本文不另加有限角采样。因为 $\Phi(\phi+2\pi)=\Phi(\phi)+2\pi$ 且严格递增，它给圆上的光滑微分同胚。共同材料角是 $\theta=\Phi(\phi)$。精确函数使用真实 $\pi$，整圈端点由周期恒等式相接。

在 prefix/tail 处，同一 $\theta$ 被识别；在 cuff/帽处，帽边界点是 $(c\cos\theta,c\sin\theta)$。不能把活动端的物理 $\phi$ 当作帽极角，也不把 $\Phi^{-1}$ 当作帽极点附近的 Cartesian 换图。极点直接用帽的 $(x,y)$ 坐标。R282 的局部 cuff 图完全适用。

若先在 $\phi$ 中求导，则准确材料两 jet 是

$$
F_\theta=\frac{F_\phi}{\rho},\qquad
F_{u\theta}=\frac{F_{u\phi}}{\rho},\qquad
F_{\theta\theta}=\frac{F_{\phi\phi}}{\rho^2}
-\frac{\rho_\phi F_\phi}{\rho^3}.
\tag{294.2}
$$

$\Phi$ 与径向坐标无关。对完整切口函数使用这些混合项，不能把有限 $\phi$ Fourier 带宽宣称为有限 $\theta$ 带宽。675 是先组成 $\theta=\Phi(\phi)$ 再对实际复合函数求导；它没有作这样的带宽替换。

## 294.3 共享 Hermite 内缝：准确成立的部分

给相邻端点 $a<b$、$h=b-a$ 及两端的完整值/一阶/二阶 jet。用 $t=(u-a)/h$ 写

$$
P(t)=c_0+c_1t+\cdots+c_5t^5,
$$

其中

$$
\begin{aligned}
c_0&=Y_a,&c_1&=hV_a,&c_2&=\tfrac12h^2A_a,\\
U&=Y_b-c_0-c_1-c_2,&
V&=hV_b-c_1-2c_2,&
W&=h^2A_b-2c_2,\\
c_3&=10U-4V+\tfrac12W,&
c_4&=-15U+7V-W,&
c_5&=6U-3V+\tfrac12W.
\end{aligned}
\tag{294.3}
$$

这些式子适用于实向量，亦逐实、虚分量适用于复系数。

**引理294-A。** 式(294.3) 是唯一的五次以内实多项式，准确匹配两端全部三项 jet。如果有限分割的相邻片使用同一份公共端点 jet，所得函数为 $C^2$。与固定光滑角函数线性组合、再作同一径向无关材料角复合，仍为 $C^2$，而所有角向及混合两 jet 在 seam 相同。

**证明。** 左端三式由 $c_0,c_1,c_2$ 直接给出；右端三式由 $U,V,W$ 及后三个系数代入得到。若两个满足条件的多项式相减，其在0和1各有至少三重零，次数不超过5，所以恒为零。相邻片的零、一、二阶导数在公共端点连续相接。逐片导数延续与一维基本定理给整体 $C^2$；相同整角函数的恒等式可继续角向微分，给混合项。□

在675中，该引理实际作用于以下三种完整数据：

- **前缀状态。** 每个径向单元保 $3M+2$ 个状态分量，包括完整 $z_0$；从同一 nodal 三数组准确构造多项式，而不读 PhysicalQuintic 已舍入的系数。
- **尾的全部 Cartesian FFT。** 每个实际径向节点保所有零模、非零模、Nyquist、三坐标及三项径向 jet。实际 complex128 字词作为系数数据，准确 Hermite 对其每个实、虚分量应用。无模态截断，也不把“mean”置零。
- **共享标量背景 $B$。** da4a 的 SharedBackground 从整份准确 nodal 表构造同一实 Hermite 并核六端点恒等式，故其位置、一阶、二阶值是同一个函数的导数。

675 的径向分割是原 prefix 节点、全部 native 节点、全部 $B$ 节点、cuff、inner、cut 及**准确** $R-W$ 的共同细分。若旧 plan 中另存的浮点 $R-W$ 与准确减法略有不同，两者都不能靠标签合并；675 保实际背景节点和自己的准确 patch 起点。细分不改变函数，不产生新的接缝。

尾节点中的一、二阶数据是否恰好等于连续 native ODE 的导数，影响连续解近似解释，却不影响式(294.3)所定义有限场的结构 $C^2$。该区分正是使用准确有限函数的目的。

### 294.3.1 PhysicalQuintic 的节点覆盖不能代替此引理

原 PhysicalQuintic 先用 longdouble 算式生成系数，随后在准确命中保存节点时，以原 binary64 nodal 值覆盖求值结果。将已经舍入的系数逐个当作准确实数，所得片多项式记为 $\widehat P_i$。要使这个“片多项式加节点覆盖”实函数为 $C^2$，必要且充分的是每个公共点 $x_j$ 满足

$$
\widehat P_{j-1}^{(d)}(x_j)
=\widehat P_j^{(d)}(x_j)
=Y_j^{(d)},\qquad d=0,1,2.
\tag{294.4}
$$

若 stored width 与准确端点差不同，也须按实际多项式的物理自变量在 $x_j$ 求这两个极限，不能预设规范坐标准确等于1。

必要性来自单侧极限；充分性同引理294-A。单独改变一个端点的返回值不能改变单侧极限。即使(294.4)的差小于任意指定正容差，也不是 $C^2$ 恒等式。本文没有为当前未知实际输入断言这些差非零或为零。

675 已明确采用式(294.3)的独立准确规范形，因而避免把这项未经证明的浮点恒等式当前提。它也不因此认证整个数值 renderer 的误差为零。

## 294.4 完整 prefix↔tail 切口：几何两 jet 的结构证明

把同一 proper planar SE(2) 后的完整前缀写作 $P(s,\theta)$。675 用实际记录角 $\beta$ 的准确正弦/余弦及实际平移定义这一个变换；位置包含平移，所有径向导数只受同一个线性旋转。它不把独立舍入矩阵的近正交性当作准确正交性。

设未修补的准确尾为 $T(r,\theta)$，由前节 shared-B 与完整 FFT Hermite 给出。切口数据记

$$
P_j(\theta)=\partial_s^jP(L,\theta),\qquad
N_j(\theta)=\partial_r^jT(R,\theta),\quad j=0,1,2.
$$

令 $v<0,b$ 为675明确记录的 supplied cut-chart coefficients，即原 A.ap、A.app 的准确 dyadic 值；此处**不假设**它们是标量半径公式的真实导数。定义

$$
D_0=P_0-N_0,\qquad
D_1=\frac{P_1}{v}-N_1,\qquad
D_2=\frac{P_2}{v^2}-\frac{bP_1}{v^3}-N_2.
\tag{294.5}
$$

$N_j$ 必须由本场自己的 $B,B',B''$ 和全部末 FFT 节点重新形成。旧 background 下的 cut-difference cache 不是该式的输入。ac635 正是清空旧 cache 后重建，675 则直接准确组合。

取 $0<W<R-\mathrm{inner}$，$t=(r-R+W)/W$。在 $[R-W,R]$ 上令

$$
\begin{aligned}
H_0(t)&=10t^3-15t^4+6t^5,\\
H_1(t)&=-4t^3+7t^4-3t^5,\\
H_2(t)&=\tfrac12t^3-t^4+\tfrac12t^5,
\end{aligned}
$$
$$
\widetilde T(r,\theta)
=T(r,\theta)+H_0(t)D_0(\theta)
+WH_1(t)D_1(\theta)+W^2H_2(t)D_2(\theta),
\tag{294.6}
$$

更内侧不加该修补。

**命题294-B。** 式(294.6)在 patch 起点为 $C^2$，在 cut 准确有

$$
\widetilde T(R,\theta)=P_0,\qquad
\widetilde T_r(R,\theta)=P_1/v,\qquad
\widetilde T_{rr}(R,\theta)=P_2/v^2-bP_1/v^3.
\tag{294.7}
$$

取任意光滑局部函数 $\gamma$ 满足

$$
\gamma(0)=R,\qquad \gamma'(0)=v,\qquad
\gamma''(0)=b.
\tag{294.8}
$$

则在共同 cut 图 $(z,\theta)$ 中，

$$
F(z,\theta)=
\begin{cases}
P(L+z,\theta),&z\le0,\\
\widetilde T(\gamma(z),\theta),&z\ge0
\end{cases}
\tag{294.9}
$$

为 $C^2$。存在这样的图，并且它不要求 $\gamma$ 等于原有限标量求值器。

**证明。** 三个 $H_k$ 在0的前三项导数均为零，在1满足 $H_k^{(j)}(1)=\delta_{kj}$，$0\le j,k\le2$。式中 $W^k$ 与物理径向微分的 $W^{-j}$ 恰相消，给(294.7)及内端零两 jet。

可取 $\gamma(z)=R+vz+bz^2/2$ 于足够小邻域。因 $v<0$，缩小邻域后 $\gamma'<0$，给合法径向换图；$z>0$ 映到 $r<R$。组合的一阶径向导数为 $\widetilde T_rv=P_1$，二阶为 $\widetilde T_{rr}v^2+\widetilde T_rb=P_2$。这些等式针对整个 $\theta$ 函数，角向及混合导数同样相接。□

这里所有 $D_j(\theta)$ 是完整角函数。前缀的有限 $\phi$ 表达经 $\Phi^{-1}$ 后通常不是有限 $\theta$ Fourier 和；原完整切口修补没有把它投影到某个 $\theta$ 频带。仅在若干角节点匹配，不能替代(294.5)—(294.7)。

$\gamma$ 的三阶及更高系数不影响本节几何 $C^2$。它们在下一节的**目标张量**二阶换图中可能出现，二者不能混为同一责任。

## 294.5 collar、固定两帽、中央反射及角周期

### 294.5.1 collar 与两帽

在共同材料角中，上尾为

$$
T(r,\theta)=r e_\theta+B(r)e_z+J\,U(r,\theta),
\qquad J=\operatorname{diag}(1,1,-1),
\tag{294.10}
$$

其中 $U$ 含全部实际 Cartesian Fourier 模。内 collar 是从 cuff 的零径向两 jet 接到真实 inner 节点的同一个准确 Hermite。因此

$$
U(c,\theta)=U_r(c,\theta)=U_{rr}(c,\theta)=0
\quad\hbox{对所有 }\theta.
$$

shared-B 的原准确 cuff 数据为

$$
B(c)=H,\qquad B'(c)=B''(c)=0.
\tag{294.11}
$$

所以 collar 的完整 Cartesian 两 jet 与平图 $r e_\theta+He_z$ 一致。R282 已给出 $(r,\theta)$ 与帽 Cartesian 图之间不经过极点的合法 cuff atlas；(294.10)不是把物理 $\phi$ 误当 $\theta$。

实际固定帽是

$$
C_\pm(x,y)=\bigl(x,y,\ \pm[H+b_\pm(x,y)]\bigr),
\qquad x^2+y^2\le c^2,
\tag{294.12}
$$
$$
b_\pm(x,y)=\sum_{j\in I_\pm}
A_j\left(1-\frac{|(x,y)-q_j|^2}{R_j^2}\right)_+^4.
\tag{294.13}
$$

函数 $t\mapsto(t_+)^4$ 为 $C^3$，其零延拓的前三阶导数在0为零。因此每个完整帽图为 $C^3$，包括 marker 的支持边界及帽极点，不需要极角在那里成为坐标。

若所有实际 marker 的闭支持严格位于自帽内部，则存在 marker-free cuff 环带，(294.11)—(294.13)自动给两帽接缝 $C^2$。一个准确的字面充分条件是

$$
c>R_j>0,\qquad |q_j|^2<(c-R_j)^2.
\tag{294.14}
$$

这正是原 cap binder 对实际词记录的 support predicate，不从 schema 推出其值。原 plan 选的中心/半径设计具有明显内侧余量；实际有限图仍应使用其保存字词，而不是用重新生成参数顶替。

严格内支撑只是已有构造方便使用的充分条件，**不是新增的必要门**：更一般地，只要 $b_\pm$ 的完整边界两 jet 为零，几何接缝即成立。若支持触边且以(294.13)的零三 jet 结束，也可直接使用该恒等式；若一个非零 marker 穿过 cuff，则不能默认条件成立。$H$ 的正负不参与本节 $C^2$ 证明；原组装对正帽高的其他限制和嵌入责任不被本文改变。

### 294.5.2 中央反射

R249 的共享入口投影使整个前缀准确满足

$$
P_z(0,\theta)=0,\qquad
(P_s)_{xy}(0,\theta)=0,\qquad
(P_{ss})_z(0,\theta)=0.
\tag{294.15}
$$

69bb 的默认 read_saved 路径实际调用该投影；675 另记录完整 nodal 三块的字面零值。若另一调用明确关闭该规范形，便不能只凭 loader 名称借用(294.15)。

在有符号 $u$ 中，用 $P(u,\theta)$ 与 $JP(-u,\theta)$ 拼接。左右0/1/2径向迹分别比较 $P$ 与 $JP$、$P_s$ 与 $-JP_s$、$P_{ss}$ 与 $JP_{ss}$，相等正好是(294.15)。所有角向迹由恒等式微分得到。统一 proper XY SE(2) 与 $J$ 交换，不移动反射平面 $z=0$。尾部的绝对 mean/帽高 offset 不得再施加到整个前缀，否则第一个条件改变。

### 294.5.3 周期角与商身份

前缀的整模三角函数、完整 FFT 及 $\Phi$ 的圆 lift 保证角周期两 jet 相同。公共节点、cut、同侧 cuff 和周期端点仅按上述材料身份识别；上下两帽不因空间位置偶然相同而识别，远处同像点也不由本节免除。

## 294.6 全局几何结构定理与全部相位

**定理294-C。** 给定一份真实完整九控制450/69bb输入，采用675所声明的准确有限函数。假设原正径向宽度/节点次序、$\rho_*>0$、同一完整角/SE(2)/FFT/B身份成立；中央使用(294.15)；两帽在各自 cuff 满足前节边界零两 jet 条件。则：

1. 准确基态是上述闭材料面上的一个 $C^2$ 映射。prefix 内节点、所有 native/B 内节点、patch 起点、物理 cut、collar inner、两 cuff、中央反射与角周期全部包括在内。
2. 使用原相位规则
   $F_\alpha^{\rm active}(u,\theta)=R_\alpha F_0^{\rm active}(u,\theta-\alpha)$，固定两帽不动，所得每个 $F_\alpha$ 仍为全局 $C^2$；$\alpha\mapsto F_\alpha$ 在强 $C^2$ 拓扑下连续。因而 $\alpha=\pi t/2$ 的原有限 $t$ 区间亦满足该正则性。
3. 若准确基态在活动片上是正则浸入，则所有相位的活动片都是正则浸入；固定帽本身是图，自动正则。此处没有自动证明活动片的 Gram 正定、全局单射、reach 或幅度。

**证明。** 第1项由引理294-A、命题294-B及第294.5节在有限 atlas 中逐 seam 拼接得到。每个图中片内函数本来是 $C^2$，所有闭边界两 jet 一致，因此并无遗漏的单侧导数。这里尚未使用任一目标 $g$ 的微分恒等式。

共同材料角旋转作用在圆柱上平移 $\theta$，在帽上用普通 Cartesian 旋转，给光滑材料作用。把 marker 从基态中分离，未标记帽在该作用与环境 $R_\alpha$ 下不变；marker 是固定的、边界零两 jet 的独立 $C^2$ 函数。cut、中央和周期的完整角恒等式经同一平移保持；在 cuff，$R_\alpha r e_{\theta-\alpha}=r e_\theta$，零两 jet 仍为零。因此第1项的拼接对所有 $\alpha$ 成立。

强 $C^2$ 连续性沿 R248：在紧材料面上，对一个 $C^2$ 函数作光滑参数平移及刚体旋转，0/1/2导数均一致连续；不要求第三阶导数。固定 marker 不产生参数变化。最后，环境正交变换及材料可逆换图保微分秩；帽的 XY 微分为单位矩阵。□

本定理给的是所述结构条件下完整的几何接缝证明。它不要求重跑一个 fixture 才能登记，也不是用尚不存在的实际场声称已达到 README 完成标准。


## 294.7 完整九标量：自动 $C^2$ 的控制项与未自动成立的基底接口

冻结九参数写作 $(p_1,p_2,p_3,\vartheta_1,\vartheta_2,\vartheta_3,\eta_1,\eta_2,\eta_3)$，其中源码中的 theta1—theta3 是前三个新增形状系数，不是材料角 $\theta$。每个原支撑保准确 left $\ell_i$ 和独立保存的正 width $w_i$，令 $x_i=(s-\ell_i)/w_i$。完整半径是

$$
a_9(s)=a_{\rm base}(s)
+\sum_{i=1}^3 w_i^2\,64x_i^3(1-x_i)^3
\bigl[p_i+\vartheta_i(2x_i-1)+\eta_i(2x_i-1)^2\bigr],
\tag{294.16}
$$

每个控制在 $x_i\notin(0,1)$ 时为零。原嵌套三控制部分及所有基底支段均保留。

**命题294-D。** 式(294.16)的每个新增控制及其零延拓是 $C^2$；全部九控制不会改变基底在任一接缝处的零、一、二阶跳跃。它们不能修复一个原有限 Gauss/branch 接口的非零 jump。

**证明。** 每个多项式都有因子 $x^3(1-x)^3$，所以在0和1的0/1/2导数均为零。仿射换元与固定 $w_i^2$ 保此性质。有限个全局 $C^2$ 项的任意冻结线性组合仍为 $C^2$，其两侧 jet 跳跃为零。加到基底后，基底的跳跃不变。□

数学支撑右端是 $\ell_i+w_i$，不能因为另存 right 与它接近就用 right 替换。完整解释器保二者为可能分割点，控制公式只用真实 stored width。原控制位于非轴前缀内部，因而在中央及外 connector/cut 附近应准确消失；该事实须来自实际支持数据和原构造，不由一次浮点控制值恰为零来代替。

### 294.7.1 已自动成立的基底部分

原 initial law 的准确四次表达，在自己的过渡点与其线性延拓匹配值、一阶及二阶。它在0满足 $a(0)=1,a'(0)=0$。原 scalar shared-knot 前缀则使用与(294.3)相同的准确 Hermite 代数，第一节点由同一准确 initial law 重建。因此这些内节点的 $C^2$ 是构造恒等式。

加入内部九控制后，中央邻域仍有 $a_9'(0)=0$。在共同中央图中把目标 $ds^2+a_9(s)^2d\theta^2$ 偶延拓，系数的两阶连续性正由这一零一阶条件及同一单侧二阶值给出。与几何的 R249 三块投影不同，这一目标条件来自原 scalar，而非把几何节点改零后推断出来。

### 294.7.2 有限 Gauss 原语必须按自身求导

以任一原 phase panel $[\ell,b]$ 为例，保存的有限节点/权重是 $\xi_j,\omega_j$，真实实函数 integrand 为 $f$。源码 partial panel 对应

$$
Q_\ell(u)=(u-\ell)\sum_j\omega_j
f\bigl(\ell+\xi_j(u-\ell)\bigr).
\tag{294.17}
$$

直接求导得到

$$
\begin{aligned}
Q_\ell'(u)
&=\sum_j\omega_j\bigl[f(z_j)+(u-\ell)\xi_jf'(z_j)\bigr],\\
Q_\ell''(u)
&=\sum_j\omega_j\bigl[2\xi_jf'(z_j)
 +(u-\ell)\xi_j^2f''(z_j)\bigr],
\qquad z_j=\ell+\xi_j(u-\ell).
\end{aligned}
\tag{294.18}
$$

特别地，记 $m_k=\sum_j\omega_j\xi_j^k$，则

$$
Q_\ell'(\ell)=m_0 f(\ell),\qquad
Q_\ell''(\ell)=2m_1 f'(\ell).
\tag{294.19}
$$

没有准确矩恒等式时，连 $m_0=1,m_1=1/2$ 也不能由“原表是 Gauss 生成的”这一描述推出。即使这些低阶矩准确成立，(294.18)在非零长度处仍不是对任意非多项式 $f$ 恒等于 $f(u),f'(u)$。本题原 $f$ 含三角函数复合，不能以多项式求积精确度跳过这一点。

累计有限原语在 phase panel 分界处，左侧完整 panel 与右侧 cache 若使用**同一准确有限和**，其值相接是恒等式。其导数相接还分别需要

$$
Q_{\ell}^{\prime}(b)
=m_0^{\rm next}f_{\rm next}(b),\qquad
Q_{\ell}^{\prime\prime}(b)
=2m_1^{\rm next}f_{\rm next}'(b).
\tag{294.20}
$$

phase 本身的平滑性不单独证明(294.20)。物理表达 $a_0+LQ((s-S)/L)$ 的真实导数是 $Q'$ 与 $Q''/L$；源码另返回的正弦 slope 和解析 angle derivative 只能在另有等式证明时替代它们。

这里不是宣布当前实际表已经失败。它指出一个准确的未付恒等式：没有运行或读取某个实际 live descriptor 时，不知道其真实差值；即使算得很小，也只能形成求值误差估计，不能把非零量称为接缝恒等式。

### 294.7.3 独立常数、mask、clip 与实际分界

原 descriptor 另外保 turn.end_radius、turn_end、bridge_start、每段 a0/s0/s1/length、外 coast speed、48/64点表及 mask 容差。它们是独立保存的 binary 常数。不能无证明地把 stored turn_end 改写为准确的 prefix_end 加 stored length，也不能把另存 end_radius 自动当作(294.17)的准确末值。

原桥段按最后一个匹配的 segment 选择，左界含原 $10^{-13}$ 容差，末右界含原 $10^{-12}$ 容差，局部规范参数再 clip 至 $[0,1]$。在一个被选中而尚未到其真实 s0 的开区间，clip 会使该支半径为常数，其真实一、二阶导数为零；前一个支在同一切换点的真实导数必须与此比较。不能只检查名义 s0/s1 上各自标注的端点 jet。

因此，准确有限 scalar 的必要且充分 $C^2$ 接缝条件是：在完整 breakpoint 集的每一个实际选支点，左右被选实函数的值、一阶、二阶一致，且该点本身选出的函数值等于公共极限。该集合包括 shared knots、initial law 分界、turn 各 phase panel、实际主分支边界、全部 segment mask/clip/phase 点及所有 $\ell_i+w_i$。完整九解释器已经保这些位置；它的区间包围不自动证明等式。

原 CompleteProfile 的若干 $5\times10^{-12}$ 端口检查针对当次返回的三数值。它们仍保留在原求解流程中，但既不是(294.18)的导数恒等式，也不是上述完整 breakpoint 条件。本文不添加或修改该求解门。

## 294.8 同一 cut atlas 的目标张量：完整兼容方程

现在固定一个已经明示的目标，不从有限场重新拟合：

$$
g_P=ds^2+a(s)^2d\theta^2,\qquad
g_T=E(r)\,dr^2+r^2d\theta^2,\qquad a>0,\ E>0.
\tag{294.21}
$$

$a$ 必须是当前全部九系数的同一真实函数；$E$ 必须是原目标的同一连续解释。采用模型 C 时，须明确 R286 的模型层约定及真实径向定义域，不能直接把旧有限返回值视为它的认证结果。

用第294.4节的共同 material-angle cut 图，令

$$
\gamma(0)=R,\quad \gamma'(0)=v<0,\quad
\gamma''(0)=b,\quad \gamma'''(0)=c_3.
$$

假设两侧系数在各自闭端有相应连续两 jet。记 $a_j=a^{(j)}(L)$、$E_j=E^{(j)}(R)$。尾目标在该图的两项系数是

$$
A(z)=E(\gamma(z))\gamma'(z)^2,\qquad
C(z)=\gamma(z)^2.
\tag{294.22}
$$

**定理294-E。** 在原同材料角、纯径向 cut atlas 中，(294.21)给一个 $C^2$ 目标张量，当且仅当

$$
\boxed{a_0=R,\qquad a_1=v,\qquad a_2=b}
\tag{294.23}
$$

及

$$
\boxed{
\begin{aligned}
E_0v^2&=1,\\
E_1v^3+2E_0vb&=0,\\
E_2v^4+5E_1v^2b+2E_0b^2+2E_0vc_3&=0.
\end{aligned}}
\tag{294.24}
$$

若只讨论 $C^0$ 张量，取零阶的 $a_0=R$ 和第一式；若只讨论 $C^1$，另取 $a_1=v$ 与第二式。$C^2$ 张量的完整版本再加入 $a_2=b$ 与第三式。本文列清这些层级，不把 $C^2$ 目标额外加成原数值 BVP 验收门。

**证明。** 在前缀侧，径向系数的三项迹为 $(1,0,0)$；角向系数的三项迹为 $(a_0^2,2a_0a_1,2a_1^2+2a_0a_2)$。对(294.22)直接求导，角向得到 $(R^2,2Rv,2v^2+2Rb)$，因 $a_0,R>0$，逐次相等恰给(294.23)。径向三项迹恰为(294.24)左侧。系数与角无关，所有角向、混合导数相同，故这些条件充分；必要性来自相同图中的两侧迹。□

这支付的是当前实际采用的材料身份和换图，不声称可以擅自更换边界角参数来绕过条件。几何切口修补使用的 $v,b$ 与目标切口使用的 $v,b$ 必须是同一个图的系数。第294.6节的“存在几何 $C^2$ 图”本身不证明它就是原目标所需的光滑 atlas。

### 294.8.1 准确弧长图和三阶自由度

对给定连续正 $E$，原向内的准确弧长图可由

$$
z=-\int_R^r\sqrt{E(\xi)}\,d\xi
\tag{294.25}
$$

定义。它局部可逆，径向目标准确成为 $dz^2$。若 $E\in C^2$，其逆 $\gamma$ 为 $C^3$，并有

$$
v=-E_0^{-1/2},\qquad
b=-\frac{E_1}{2E_0^2},\qquad
c_3=\frac{E_2}{2E_0^{5/2}}-\frac{E_1^2}{E_0^{7/2}}.
\tag{294.26}
$$

这些是(294.24)的一个明确解，不是重新选择 warp 或改变目标。对给定非零 $v$，前两式一旦成立，第三式也可直接解出 $c_3$；它不改变几何两 jet。

若材料 atlas 要一直用光滑多项式换图，可取具有(294.26)前三阶迹的局部多项式 $\gamma$；上述 $C^2$ 张量拼接只依赖这些迹。无需把一个只由 $E\in C^2$ 保证为 $C^3$ 的准确弧长图另称为 $C^\infty$。

但是，原程序保存的 $-1/\sqrt{\widehat E}$ 与 $-\widehat E'/(2\widehat E^2)$ 是有限计算结果。将它们单独当准确 dyadic 后，不能据原公式名称断言它们恰等于(294.26)，更不能把 $\widehat E$ 与模型 C 的真实 $E_0$ 默认为同一个数。$a_0,a_1,a_2$ 也必须是半径实表达的真实迹，不能用其独立返回的三个标签代替。

如果前缀半径的真实迹没有满足(294.23)，单独调图的三阶项不能补零阶或一阶冲突。完整切口几何修补可以接任意给定非零 $v,b$，但不能因此改变 $a$ 或 $E$。

### 294.8.2 中央和两 cuff 的目标兼容

中央目标沿 $s=|u|$ 反射。若 $a$ 在0有单侧 $C^2$ 且正，则 $a(|u|)^2$ 为 $C^2$ 当且仅当 $a'(0)=0$。第294.7.1节的准确 initial law 与内支撑九控制支付该结构条件；它不能支付更远 connector 的接口。

在 cuff 附近以 Cartesian $(x,y)$ 表示尾目标，有

$$
g_T=I+(E(r)-1)\,e_r\otimes e_r,\qquad r=\sqrt{x^2+y^2}>0.
\tag{294.27}
$$

若 $E(c)=1,E_r(c)=E_{rr}(c)=0$，则(294.27)与平帽的 $I$ 具有相同完整两 jet，因为 $e_r$ 在 $r=c>0$ 邻域光滑。若帽 marker 支撑内部，帽的同图目标为

$$
g_{\rm cap}=I+Db_\pm\otimes Db_\pm,
\tag{294.28}
$$

并在 cuff 环带准确等于 $I$。更一般地，(294.13)在触边点的零三 jet 亦足以令(294.28)的两 jet 与 $I$ 相同。帽 target 的局部误差恒零，不单独证明这一跨缝条件；这里已把所需迹列出。

## 294.9 模型 C：内 cuff 可平延拓，natural 外端不可平延拓

### 294.9.1 内 cuff

在 R286 明示约定 C、正原数据、准确深根规则或原允许根族及真实保护端兼容条件下，该文已证明

$$
E_*(r)\to1,\qquad (E_*)_r(r)\to0,\qquad
(E_*)_{rr}(r)\to0\quad(r\downarrow c).
\tag{294.29}
$$

这是覆盖全部无限深尾的导数结论，不是有限样点接近1。赋值 $(1,0,0)$ 并在 cuff 内的平领取 $E_*=1$，得到合法 $C^2$ 延拓。结合(294.27)—(294.28)，它准确支付模型 C 与两帽 target 的 cuff atlas 兼容，前提是帽自身的原边界迹成立。

这不要求 $w_*$ 在 cuff 为 $C^2$；R286 只需其 $C^1$，而 $w_*^2$ 的额外小量给 $E_*$ 的二阶平端。也没有把实际 shared-B 的导数改写成 $w_*$。

### 294.9.2 natural 外端的完整两阶公式

令原 R286 log-length 为 $\sigma$，以免与前缀 $s$ 混淆。记

$$
\zeta=\frac{r_{\rm cut,bin}}{r_{\rm old,bin}}>0,\qquad
r_o=r_{o,\rm out}>0,\qquad
w_o=\epsilon_{\rm phys}(2d_0)^{11/4}r_o^{-7}>0.
\tag{294.30}
$$

这些保持原冻结常数，实际自然外半径是 $R_{\rm out}=R_*(\sigma_{\rm out})$，不自动等于名义 cut。

**命题294-F。** 原 cut-preserving 最后 port 在 natural 外端满足

$$
\boxed{
\begin{aligned}
E_*(R_{\rm out})&=1+w_o^2,\\
(E_*)_r(R_{\rm out})&=-\frac{14w_o^2}{\zeta r_o},\\
(E_*)_{rr}(R_{\rm out})&=\frac{210w_o^2}{\zeta^2r_o^2}.
\end{aligned}}
\tag{294.31}
$$

因原数据正，第一项严格大于1，第二项严格负，第三项严格正。因此将外侧设为 $E\equiv1$ 连 $C^0$ 都不能匹配；设为常值 $E\equiv E_*(R_{\rm out})$ 也不能匹配 $C^1$。内 cuff 的平延拓结论不适用于此处。

**证明。** 原最后 port 恢复 raw 值，$r_{o,\sigma}=r_o/\sqrt{12}$，故

$$
w_\sigma=-7w/\sqrt{12},\qquad w_{\sigma\sigma}=49w/12.
$$

原 $\chi=1-S$ 与 $j_0=1+(\zeta-1)S$ 在最外端满足 $\chi=\chi_\sigma=0$、$j_0=\zeta$、$(j_0)_\sigma=0$。完整连续径向速度 $V=R_{*,\sigma}$ 因而退回

$$
V=\zeta r_o/\sqrt{12},\qquad V_\sigma=\zeta r_o/12.
$$

所有乘 $\chi$ 或 $\chi_\sigma$ 的原 warp 项在这里准确消失，不需要舍弃六 primitive 中任何一项。链式法则给

$$
w_r=\frac{w_\sigma}{V}=-\frac{7w_o}{\zeta r_o},
\qquad
w_{rr}=\frac{w_{\sigma\sigma}V-w_\sigma V_\sigma}{V^3}
=\frac{56w_o}{\zeta^2r_o^2}.
$$

由 $E_*=1+w_*^2$，分别求导即得(294.31)。□

原 finite warp 的 flat 段可能在别处给常 slope；最后的 cut-preserving 覆盖有自己的优先次序，不能借前面的 flat 标签略去它。这里也没有将旧捕获 $r_{\rm old,bin}$ 换成新实算 $r_o$。

### 294.9.3 当前有限场 cut 与真实定义域

对当前有限场 cut $R$，只有已经证明 $R$ 落在模型 C 的真实定义域内，才能使用 $E_*(R)$。一个 whole-natural-domain 包围与 $R_{\rm out}\in[L_R,U_R]$ 至多直接支付 $R\le L_R$ 的包含关系；$R\in(L_R,U_R]$ 的包含仍未证，$R>U_R$ 则已超出该已证域。不能把一个未付后缀设成平尾、重选 warp、平移半径或把 $R$ 改名为 $R_{\rm out}$。

若最终目标本来指定使用整个自然域，还须保完整材料域识别；在较短的现有场域上比较一个合法限制，不会自动构造被省略的自然后缀。若目标明确在原已固定场域上使用该连续系数的限制，也须如实记录该同一对象及包含关系。

已发表九 metric consumer 的实际行为与此一致：它只在真实已付 closed query 的并内返回包围，cut 包含未证或越界的格保持未付。source 4b13425a34d8de2d168632fa0c24474542257e51fb60c2ed5a0b8501beadc975 与接口e364369fd235c9b01791c4552339af1a41bf2b888220c2f0b363e9a07930a226均没有 naturalRout 后平延拓的声明。当前没有因本条证明而新增实际 $E$、$R_{\rm out}$ 或 metric 数值结果。

## 294.10 保同一 $g$ 的准确几何修补，以及不能修补的对象错误

### 294.10.1 已有准确 Hermite 与新的独立修补

将真实共享节点作为准确定义数据并用(294.3)重建，已经是675/R249明确采用的有限对象；不需重新求 BVP 才能证明其内缝。若未来要从一份**字面舍入片多项式**出发修复非零端点差，则必须明确选择公共两 jet、用准确 Hermite 在相邻有限窗口匹配，并以新对象/新来源记录，不能只改旧文件的 C² 标签。

同样，若原目标已经固定了合法 cut atlas $\gamma_g$，而现有几何修补采用的 $v,b$ 不等于其真实一、二阶系数，可以在同一个目标 atlas 中，以

$$
v_g=\gamma_g'(0),\qquad b_g=\gamma_g''(0)
$$

重新形成(294.5)—(294.6)，保持完整 prefix、材料角、$B$、两帽及原 $g$ 不动。这是一个**新的有限位置函数**。它在指定目标 atlas 中结构 $C^2$，但旧实际接受状态、旧 native 方程、旧采样曲率或旧 metric 证书不随之被改标签。

如果是目标 $a,E$ 本身在该固定材料识别处违反(294.23)—(294.24)，修改 $F$ 不能使这两个不兼容目标系数突然相等。把目标 scalar 换成一个更平滑的 Hermite、把有限 Gauss 换成真积分、移动 cut 或重设 warp，都是另一项模型/目标选择，不能作为“原 $g$ 不变的几何修补”偷偷实施。本文不选择这些变更。

### 294.10.2 完整两 jet 的可审计误差预算

对一个宽度 $W$ 的右端修补，令其三个完整角差为 $\Delta_k(\theta)$，定义

$$
A_{kj}=\sup_\theta|\partial_\theta^j\Delta_k(\theta)|,\qquad
0\le k,j\le2.
$$

这里范数是完整三维向量范数。R249 的同一 Hermite 基（反向参数及一次导数基变号）给

$$
\sup_{r,\theta}|\partial_r^i\partial_\theta^j\Delta F|
\le e_{ij}:=\sum_{k=0}^2W^{k-i}B_{ik}A_{kj},
\qquad
B=
\begin{pmatrix}
1&2/5&1/20\\
5&2&1/4\\
20&12&2
\end{pmatrix}.
\tag{294.32}
$$

该式支付整个修补窗口和完整角，不仅端点。前缀换到材料角时必须用(294.2)及完整 $\rho_*$、$\rho_\phi$ 包络；native 部分保全部 FFT、零模中的完整 mean 及 Nyquist。宽度缩小时一、二阶费用可能放大，不能由位置差小推出曲率差小。

在固定正目标 $g$ 上，记 $A=dF\,g^{-1/2}$、$B_1=d(\Delta F)\,g^{-1/2}$。若同域已有 $\|A^TA-I\|\le\varepsilon_0$ 和 $\|B_1\|\le\varepsilon_1$，则

$$
\bigl\|(A+B_1)^T(A+B_1)-I\bigr\|
\le\varepsilon_0+2\sqrt{1+\varepsilon_0}\,\varepsilon_1+\varepsilon_1^2.
\tag{294.33}
$$

证明为展开 Gram 差并取算子范数；最终比较始终是同一个 $g$。若旧对象只分片可微而非全局 $C^2$，不能给它借一个不存在的全局曲率输入；新准确场可直接走 R279 的完整六 jet 判据。浮点 renderer 的三角函数、材料逆和系数求值误差也不包含在(294.32)中，除非已另行包围。

若两完整位置映射的全域一致差不超过 $\varepsilon$, 则完整像的 Hausdorff 距离不超过 $\varepsilon$、直径差不超过 $2\varepsilon$。对于原 held 论证实际使用的点到完整目标像距离，同一见证给

$$
\left|\operatorname{dist}(\widetilde F_\alpha(p),\widetilde F_0(M))
-\operatorname{dist}(F_\alpha(p),F_0(M))\right|\le2\varepsilon.
\tag{294.34}
$$

这些是三角不等式，不能替换 README 的 held/刚体商定义。reach 与嵌入性仍需新完整曲率/局部图/所有点对责任，不能仅凭(294.34)继承。原 static+R24 路线、R241 完整覆盖和两帽 marker/唯一刚体责任均保留。

### 294.10.3 小 target jump 不能冒精确解的同目标极限

本条不把尚未计算的 jump 宣布为非零。但若在同一合法图中已证明目标的两侧零阶值不同，则有一个精确障碍：对任一固定非零切向量 $\xi$，写 $q_\pm=g_\pm(\xi,\xi)>0$。任何连续诱导形式若在两侧具有相对误差至多 $\varepsilon<1$，其公共极限必须同时位于 $[(1-\varepsilon)q_\pm,(1+\varepsilon)q_\pm]$，所以必要有

$$
\varepsilon\ge\frac{|q_+-q_-|}{q_++q_-}.
\tag{294.35}
$$

因此正但很小的真实 jump 仍不能被称为 $C^0$ 恒等式，也不能在不改变同一 $g$ 时许诺误差无条件趋零。若 $g$ 的值连续而一阶迹真不匹配，则它也不能准确等于某个 $C^2$ 映射的诱导形式，因为该诱导形式至少为 $C^1$。这只是对象辨别，不是给当前未知场填造误差底线或宣布原问题不可能。

## 294.11 当前可自动支付与仍需真实输入的最小清单

| 责任 | 本文已给的结构结论 | 不能从来源标签/小残差推出的部分 |
|---|---|---|
| 完整 prefix 内节点 | 同份准确 nodal Hermite 自动 $C^2$ | literal longdouble 系数及节点覆盖的精确恒等式 |
| native/B 内节点 | 全部共享 FFT 三 jet 与同一准确 $B$ 自动相接 | FFT 数值解对连续 native 解的误差 |
| 切口 patch 内端 | 三个完整基的零两 jet，准确 $C^2$ | 任意删模或重用旧背景 delta 的版本 |
| prefix↔tail 几何 cut | 命题294-B在已声明 $v,b$ 图中完整相接 | 该图与原连续目标 atlas 是否相同 |
| inner/collar | 共用真实 node0 与零端 Hermite | 丢均值、Nyquist或独立重算 node0 的版本 |
| cuff/帽几何 | 完整非轴零两 jet、$B=(H,0,0)$、marker 边界零两 jet | 真实 marker 穿过 cuff 而仍宣称平邻域 |
| 中央反射 | R249 三块准确投影，统一 XY SE(2) 保持 | 未规范化调用，或额外给整个 prefix 作高度平移 |
| 材料/角周期 | 完整 $\Phi$、正密度、准确周期函数 | 把 $\phi$ 当 $\theta$，或把逆角投影为有限带宽 |
| 九标量控制 | 每个真实支持上的 degree6/7/8 零延拓为 $C^2$ | 基底 finite-Gauss/clip/mask 接口自动 $C^2$ |
| 目标中央 | 原准确 initial law 与内支撑给 $a'(0)=0$ | 几何入口投影代替目标条件 |
| 目标 cuff | R286 内端 $(1,0,0)$ 加原帽边界条件 | 将这项结论搬到 naturalRout |
| 目标 outer/cut | (294.23)—(294.26)完整 atlas 条件 | nominal cut等于naturalRout、有限返回ap/app等于真导数 |
| 全相位几何 | 定理294-C与R248，强 $C^2$ 连续 | 全局单射、reach、幅度、目标误差数值及精化收敛 |
| 真实来源 | 原450接受件、全参数/节点/原尾/guard须真实绑定 | 在当前main重构profile后只写origin即可冒live现场 |

这一清单不是新的审批流程或 BVP 门。它把既有构造的自动恒等式从仍需真实数据/定义的责任中分开，让后续同场消费者能够引用已付结构，而不重复做虚假的有限 jet 采样审查。

## 294.12 结论及下一准确接线

在有真实完整输入时，现有675准确表达无需再改数学，即可按本条证明支付所有**几何结构接缝**；只须引用其真实对象、原R249选择和实际帽边界条件。全局正则性、R279曲率、R241点对/reach、完整 held/刚体商以及原目标的算子误差仍由同一场负责。

目标方面，最薄的实际后继是从现场完整 descriptor 取准确标量分支及所有端点，从真实模型 C 包围取有效径向域和 $E$ 两 jet，在原固定图册中解释(294.23)—(294.24)。如果实际定义的等式由构造保证，就直接引用该恒等式；如果构造只给有限容差返回值，就保留其误差语义，不把它升级为等式。若必须改变位置函数，则按第294.10节作为独立准确修补并重新支付几何误差，原 $g$ 不变。

本次只进行了源码、既有证明和身份元数据阅读，以及上述解析推导。未导入科学模块、未执行 finite-Gauss、区间积分、ODE、BVP、FFT、曲率或 metric 数值计算；未改冻结源、目标、warp、原求解门或任何已接受状态。没有造新 fixture、实际闭场或通过证书。
