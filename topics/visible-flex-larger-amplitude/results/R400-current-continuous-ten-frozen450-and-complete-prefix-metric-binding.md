# R400：连续 C 十参数族的真实全 450 冻结输入与完整前缀相对度量接线

作者：AI。日期：2026-11-15。

状态：**以下来源条件、同参数冻结、准确 Hermite 解释及闭区间前缀比较结论已证明；四个独立源码是 source-only 实现。没有实际 accepted 连续 C 十族父场，没有执行新的 450 求解、闭场生产或度量计算，也没有填入未来参数、阈值或通过结果。**

本文补的是旧 nine/finite-Gauss 类型不能承接已发表连续十族的实际缺口。它不重复 R251 的一般算子判据，不把 R294 指出的有限多项式/接口缺陷用新标签消掉，也不把有限 185/189 的十参数搜索结果称为这里的连续 C 目标。所有科学求值、编译和运行仅在指定公开仓库 Actions；本次仅源文、来源字段和解析推导。

## 400.1 三个不同对象与结论边界

设实际连续十族 factory 产生完整准确表达式 $a_*(s;p)$，$p\in\mathbb R^{10}$，长度 $L_*>0$。其语义叶为同一模型 C 的 cut $E_0,E_1,E_2$，不是三个人为独立选出的浮点目标。准确对象保留原 C 的全部允许根族、原 core、真实 cut、两个过渡、coast、cut collar 和全部十个控制项。

同一个 factory 文件还由独立 numeric 源编译为有限数值求值器 $a_{\rm num}(s;p)$，数值长度是实际 binary64 字词 $L_{\rm num}>0$。准确 DAG 与这个求值器必须分列：cut 盒中点不因此成为一个已经实现的共同准确 C；数值多项式逐点返回和准确 DAG 也不因此恒等。R294/R298 的原有限对象边界仍适用，不能由新 source SHA 证明浮点接口的准确两 jet 相等。

假如原完整物理 BVP 在这个数值求值器上真正接受，则保存其完整节点数组 $Y_i,Y'_i$；以原完整有限 ODE 二阶公式现场返回的 $Y''_i$ 为另一组有限字词。本文的几何比较对象定义为通过这些**同一组完整节点两 jet** 的准确实 Hermite 场 $F_H$。它不是未经误差比较的 rounded `PhysicalQuintic` renderer，也不是已经证明的准确等距解。

| 对象 | 数据/定义 | 本文可支付的责任 |
|---|---|---|
| 准确连续十族 $g_*$ | 完整 DAG、全十个实际冻结 dyadic 系数、共同 C 叶及允许根族 | 准确目标的闭区间包含与坐标拉回 |
| 数值 full 453/450 问题 | 当前 numeric 编译、原全 RHS/边界/当前 H/完整原门 | 实际来源和维数绑定；不制造成功 |
| 准确 Hermite 前缀 $F_H$ | 全部 338 分量的同组 $Y,Y',Y''$ 节点字词 | 准确两 jet 拼接；完整闭前缀相对算子比较 |
| rounded 保存场/renderer | 原有限多项式系数与原求值顺序 | 原件身份保留；与 $F_H$ 的全域误差尚未认证 |
| 完整 shared-B 闭面 | 真 current-C 径向场、同一个 B、领圈、配准、cut patch、两帽 | 本文四源尚不生产；完整责任明确保留 |

准确 C 的某个成员若尚未被合法选定，本文冻结的是同一准确族、同一十参数点和同一数值编译来源；不是声称某个共同准确 C 根已被现场浮点代表选中。下面的区间结论对原盒所包含的每一个允许准确成员同时成立。

## 400.2 精确源码身份与复用边界

本次四个独立源码位于 `computations/`，没有改写旧源：

| 独立源 | 字节数 | SHA256 |
|---|---:|---|
| [geometry_20261115_continuous_ten_same_metric_profile.py](../computations/geometry_20261115_continuous_ten_same_metric_profile.py) | 30,299 | `3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6` |
| [geometry_20261115_continuous_ten_frozen450_checkpoint.py](../computations/geometry_20261115_continuous_ten_frozen450_checkpoint.py) | 36,989 | `43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae` |
| [geometry_20261115_continuous_ten_frozen450_saved_prefix.py](../computations/geometry_20261115_continuous_ten_frozen450_saved_prefix.py) | 18,759 | `1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520` |
| [geometry_20261115_continuous_ten_frozen450_prefix_metric.py](../computations/geometry_20261115_continuous_ten_frozen450_prefix_metric.py) | 32,761 | `011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84` |

上游连续十族的真实发布是 `d428ec98fd6ab726b2d4fac3a732f4ccb8698bce`：

- [准确十族 factory](../computations/geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py)，46,691 B，SHA256 `72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682`。
- [数值十族编译器](../computations/geometry_20261115_continuous_ten_fixed_power_scalar_numeric_v3.py)，24,933 B，SHA256 `7dedb7134cd2efc43f136c4a87795f06c6f3824c12a25261b6886c624f6e4ddd`。
- [完整增广 flow 适配](../computations/geometry_20261115_continuous_ten_fixed_power_augmented_v3.py)，6,474 B，SHA256 `a248e9577bf6f522b86c7c9b32d3fd51cc49dc9468760ef1d3e78e33062f9e0f`。

主要数学核心保持原源码：

| 责任 | 原完整来源 |
|---|---|
| 338 物理、112 core、$k$ 活动参数增广流 | `geometry_20261114_full_dn_augmented.py` / `f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e` |
| 全物理 FFT RHS | `geometry_20261114_r225_free_core_bvp.py` / `a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08` |
| 原物理角完整边界 | `geometry_20261114_physical_test_boundary.py` / `3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681` |
| 全材料角 trace 与边界 | `geometry_20261114_full_dn_boundary.py` / `4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2` |
| 原完整 nonlinear full-DN owner | `geometry_20261114_full_dn_solve.py` / `c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162` |
| 全 338 nodal 二 jet、Fourier、material/SE2 算式 | `geometry_20261114_large_core_saved_prefix.py` / `51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0` |
| 准确有限场六 jet 算术 | `geometry_20261115_shared_active_interval_balls.py` / `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` |
| 原 R251 四 Loewner 判据与完整闭格 DFS | `geometry_20261115_shared_field_relative_metric.py` / `a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17` |

profile 源完整核自己的 8 个直接来源及实际自己源；checkpoint writer 还要求原 core 的 `FROZEN_SOURCES` 与当前 owner 的来源表逐项包含在实际完整闭包中。SavedPrefix 保留原 23 项物理来源表，连同本次 reader/profile；prefix metric 核本次 SavedPrefix、十族 factory、675 六 jet 和 a601 算子核心，并记录保存场完整来源表。没有以“名称相近”替代 SHA。

prefix metric 用隔离 module 实例加载 675 的纯 jet/Fourier 函数，显式装入同一科学运行的 Arb/NumPy backend；**不调用** 675 的旧 `initialise_runtime`、`geometry.load_shared_bundle`、e70d 的完整闭场 loader 或 6b06 的旧 `RefinedTail`。本次没有为新目标借用旧 frozen-tail 数组。

## 400.3 全十参数及真正 453→450 问题

参数顺序固定为

$$
p=(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3,\xi).
$$

前三组分别在三个原真实支撑上乘 $1,(2x-1),(2x-1)^2$；第十项只在 support 1 上乘 $(2x-1)^4$。每项公共因子为

$$
w^2\,64x^3(1-x)^3,\qquad x=(s-\ell)/w,
$$

支撑外为零。三个端点导数槽的零性来自三重端点因子。这里支撑的 $\ell,w$ 是准确 DAG 的值；数值编译器的相应字词单列，不能互换。全部十系数和全部实际支撑必须保留。精确实加法允许按实际定义求和；numeric 的有限运算顺序与其误差仍单独负责。

`CurrentTenProfile.view` 有三个明确视图：

| 视图 | 活动标量 $k$ | 固定 core 目标 $K$ | 完整未知量 | 分离边界左/右 |
|---|---:|---:|---:|---:|
| 七个 shape 固定、前三个活动 | 3 | 3 | $338+112+3=453$ | $341+112$ |
| 全十个参数冻结 | 0 | 0 | $338+112=450$ | $338+112$ |
| 全十个活动，作为独立能力 | 10 | 10 | $460$ | $348+112$ |

三种情况均保 $M=T=112$；不会把 460 或 453 叫作 450。四源 checkpoint 的接受契约仅处理实际 453 或实际 450，不暗示已有全十活动求解。

### 命题 400.3：冻结等式与接受责任

若某个真实 453 结果在实际十字词 $p^*$ 处接受，且冻结后保持同一个准确 factory/DAG、同一个共同 C 叶来源、同一个数值编译和同一组 $p^*$ 字词，则 `all-ten-frozen` 的标量函数与原 453 现场在 $p^*$ 处的标量函数相同；准确目标族在该点也相同。新全 450 问题释放原三个固定 core 目标，仍需重新求解其完整 450 方程及 $338+112$ 边界。

**证明。** 三活动视图把传入前三个系数和保留七个 shape 合成为同一个全十向量；零活动视图把该全十向量直接固定。两者调用同一个原十族 `raw_jet`/编译对象。因此每次有限标量求值的输入来源与全参数字词相同。准确对象采用同一个 DAG 和同一组有理参数，故相同。增广结构中删除的是三个不再未知的常参数变量，边界同时取消三个原固定 core 目标；原 338 物理状态、112 core 未知量及全部 112 末端方程均未减少。原已接受 453 数组不能证明这个不同的 450 边值问题已解。证毕。

`freeze_at_current_state` 对冻结前后 `current_target_identity` 做完整同对象比对，只产生 `actual_450_accepted=False`。`fresh450_seed` 可保每个原节点的前 450 个 seed 字词并重新求全 450 RHS，但始终是新初猜；该例程没有成功字段生成权。原全节点/中点/RMS preflight、当前 H、FD、非线性 full-DN 与最后新 audit 仍须由真实新求解支付。

## 400.4 真正现场 checkpoint 的最小合同

checkpoint schema 为 `R400-current-continuous-ten-complete-physical-DN-checkpoint-v1`。它不是把 old nine schema 改名；原完整 full-DN JSON 原字节单独复制保留。原 core 的 `fixed_modes=3` 是旧核心的固定文字 metadata，原样留存；真实本次 $K,k$ 从现场 flow/boundary/SeparatedBoundary 对象与完整数组形状绑定，不能根据这条旧文字误判 450。

### 400.4.1 现场来源前提

`LiveCheckpointWriter` 必须由真实连续十族运行，在原 full-DN 最终接受之后调用。它接收**该运行仍存活的** owner、flow、boundary、SeparatedBoundary、原 core module、raw native client 与实际完整来源闭包。配置原件、当前 C sampler result、真正创建的 native owner、完整 source/geometry identities 均交叉核。

这是一项来源前提和可执行接口；不是说有同 schema、写了 `origin` 或人为置 `success=True` 的 JSON 就能证明曾运行。本文没有真实 accepted 父、没有调用 writer，也没有创建一个虚拟 parent。尚未完成实际 continuous-ten 453/450 调度入口时，不能把这几个可调用组件称为已经运行的同场闭面链。

### 400.4.2 保持的原门与原完整数据

writer 只记录并核原已有职责：

- 原 core 源及成功/status 0；完整 collocation RMS $\le10^{-6}$、原完整 BC $\le10^{-11}$、原 frozen-physical RMS $\le10^{-6}$。
- 原 current-H 真实解后 full FD，原 $5\cdot10^{-5}$ 实现阈值、原 Richardson 契约和两组完整边界字段。
- 当前 nonlinear client 配置的原 32 轮、10 档、$2\cdot10^{-9}$、全 $\eta=0$ 敏感度；全 112 cut H、全 $338\times112$ J，最后真实全 stage audit。
- 所有 577 个 native 节点及每节点完整 224 shape 字词；实际 H 的 signed-zero sidecar 与 raw SHA；`meanSlope`、`meanSecond`、`backgroundSlope`、`backgroundSecond` 等原字段全保。
- 原 H trace 在真实末端重算，用旧 closed-loader 已有 $10^{-12}$ 关联容差。词是否完全相等另报告；未添加新的零误差门。
- 完整 physical $Y,Y'$、augmented $U,U'$、全部节点、全部 core、活动参数；physical RHS 与 augmented RHS 分别原样保留，**不要求它们逐词相同**。前者原来是在末参数冻结后求值，后者保留节点原活动量。
- 原 constant-core/constant-parameter drift、height seam、原 physical-cut audit 均保，不添加新的 seam/mean/drift/准确域阈值。

原 H 已导出 sidecar 的负零可恢复；原 J JSON 未导出的负零信息不能从 JSON 再造，故 J 的新摘要明确只是 decoded float64le identity。原完整 response 原字节仍在输入成员中；不把 decoded identity 叫作未曾导出的 native 原数组词身份。

450 writer 必须另有真实 453 或 450 own-schema parent，且全 `current_target_identity` 同一。此处同 job 的来源比对有意严格，不自动应用跨 run 语义转移；如将来需要 R383 式跨 run 转移，应独立给出实际输入来源和对应桥，不能删除原来有意义的来源字段。

## 400.5 完整准确 Hermite 前缀，而非 rounded 多项式恒等声明

SavedPrefix 不调用旧 LargeCoreSavedPrefix constructor。它保留原完整物理的后续方法，但用新 checkpoint 与新 scalar view 构造实际输入，保留 $r_0,\ldots,r_{112}$、$t_1,\ldots,t_{112}$、$z_0,\ldots,z_{112}$ 共 338 行；$z_0$ 未删除，任何 mean 不被另加回几何。

第一 jet 是原 accepted 冻结 RHS。第二 jet 沿原 51eab 算式，在每个真实节点、当前冻结 scalar 及完整 physical state 上计算；节点原 RHS 与本地重新求值的差是诊断，不用它替换保存第一 jet，也不增加接受门。

给节点 $s_i<s_{i+1}$、$h=s_{i+1}-s_i$、$t=(s-s_i)/h$。对每个完整坐标，设左两 jet 为 $(y_0,d_0,e_0)$，右两 jet 为 $(y_1,d_1,e_1)$。所有节点字词先解释为准确 dyadic。有

$$
c_0=y_0,\quad c_1=hd_0,\quad c_2=\frac{h^2e_0}{2},
$$

$$
A=y_1-c_0-c_1-c_2,\quad
B=hd_1-c_1-2c_2,\quad C=h^2e_1-2c_2,
$$

$$
(c_3,c_4,c_5)=
\left(10A-4B+\frac C2,\ -15A+7B-C,\ 6A-3B+\frac C2\right).
$$

准确 $P(t)=\sum_{j=0}^5c_jt^j$ 在两端给出指定值、对 $s$ 的一阶、二阶导数。相邻 cell 复用同一节点两 jet，所以准确 Hermite 解释在每个前缀内部节点为 $C^2$。这是 R294/675 已用准确节点解释在这个新类型上的实际应用，并非 rounded 系数的端点取消被假定准确。

原 `PhysicalQuintic` 数值接口仍保留供原 reader/renderer 使用；本次 metric 源只用 `exact_prefix_coefficients` 的准确有理系数。两种场在所有点是否相同、其全域差以及将来 shared-B 修补误差，仍待真实比较。完整 BVP 的 finite residual 也不是准确 Hermite 场的等距恒等式。

## 400.6 全材料角与六 jet 责任

对同一个 actual full-core $c_1,\ldots,c_{112}$，

$$
\Phi(\phi)=\phi+\sum_{m=1}^{112}
\frac{(1-4m^2)c_m}{2m}\sin(2m\phi),
\qquad
\rho(\phi)=\Phi'(\phi).
$$

SavedPrefix 保留旧 R237 对完整系数的准确有理三角界。若它未给出严格正下界，现适配会报告原 material-inverse 责任未付；这不是一个新 BVP 数值拒绝，也不证明 $\rho$ 真为零。本文没有为了通过而替换 core 或加人为正下限。

令 $q=\phi/(2\pi)$。原 675 六槽 jet 是实际导数

$$
(F,F_s,F_q,F_{ss},F_{sq},F_{qq}),
$$

不是 factorial-scaled 系数。所有 338 Fourier 系数按原公式重建物理向量；所有 material 变换由完整 $\Phi$ 求导。`angle_density` 将同场 interval $\Phi_q$ 与既有 R237 严格界相交，不以有限 angular 采样代替闭覆盖。有限 $\phi$ Fourier 表达不推出材料 $\theta$ 也是有限带宽，反向也不推出。

前缀 Gram 在一个固定 SE2 变换和整体下片 $z$ 反射下不变。因此 prefix-only metric 可用 identity rigid gauge，并同时枚举两份反射前缀；这并不产生真实与 tail 接合的全局 registration，也不支付反射接缝的 $C^2$ 条件。

## 400.7 新目标的准确公共 $u$ 拉回

实际数字长度仅取原 word 的准确有理解释 $L_{\rm num}$。共同坐标是

$$
u=\frac{s_{\rm num}}{L_{\rm num}}\in[0,1],
\qquad s_*=L_*u.
$$

准确目标在 $(u,\theta)$ 为

$$
g_* = L_*^2\,du^2+a_*(L_*u;p^*)^2\,d\theta^2.
$$

故在实际保存前缀的 $(s_{\rm num},q)$ 上，它精确拉回为

$$
g_{11}=\left(\frac{L_*}{L_{\rm num}}\right)^2,\qquad
g_{12}=0,\qquad
g_{22}=a_*\left(L_*\frac{s_{\rm num}}{L_{\rm num}};p^*\right)^2
          \Phi_q(q)^2.
$$

这里不能沿用旧 finite-Gauss 前缀的 $g_{11}=1$，不能把 $L_*$ 改为 compiler 的字词长度，也不能用某个几何 B 的导数替代准确 C 目标。自然长度与准确 cut 均来自原 DAG；不重新归一原 binary cut，不在 natural $R_{\rm out}$ 外作 $E=1$ 平延拓。

### 命题 400.7：全 piece/support 的闭区间包含

设真实 $L_*$、每个准确 piece 的 anchor/width 及全部系数均被同一次准确 DAG 向外计算所得盒包含；每个 width 有严格正下界。给完整闭数字区间 $[a,b]\subset[0,L_{\rm num}]$，定义

$$
U=\left[\frac a{L_{\rm num}},\frac b{L_{\rm num}}\right],
\qquad S=\mathcal L\,U.
$$

对每个原 piece $j$，计算

$$
T_j = \frac{S-\mathcal A_j}{\mathcal W_j}
       \cap[\ell_j,h_j],
$$

其中 $[\ell_j,h_j]$ 是该 piece 在原准确定义中完整保留的 local interval。空交可略过；非空交全部调用原十族 `piece_range`，并对所有候选结果作 hull。所得三盒包含闭区间上所有允许准确成员的 $a_*,a_{*,s},a_{*,ss}$。

**证明。** 任取一个原允许准确 C 成员及一个 $s_{\rm num}\in[a,b]$。实际 $s_*=L_*s_{\rm num}/L_{\rm num}$ 在 $S$。原准确 DAG 的完整 piece 分解覆盖真 $[0,L_*]$，故它至少属于一个真实 piece；共享端点允许属于两片。真实 width 为正，准确 local coordinate $(s_*-\alpha_j)/w_j$ 因外包除法属于 $T_j$。原 factory 的 `piece_range` 对完整系数多项式及每个真实 control support 作外包：support 内与 $[0,1]$ 闭交，跨 support 时把零值分支并入；求导来自同一多项式。全部十个准确系数都按实际冻结点参与，没有舍掉 $\xi$ 或七个 shape。因此该实际三 jet 在该候选盒，继而在全部 hull 中。对任意实际成员与点均成立。独立 interval 运算丢失相关性只会加宽包含，不会选出新的准确 C。证毕。

程序每个 target cell 枚举**全部**原 accurate pieces，不从 nominal midpoint 选一片，不把不确定准确边界改为数值切点。根计划只需按 actual Hermite 节点分割；其内部 crossing 由上述所有候选闭并集负责。原 core 的裁剪 local interval、两 transitions、coast、collar 和十个 support 项都保留。

该包含结论不承诺固定粗 C 叶会随空间细分变窄到任意精度；没有可计算实数名称时不能从连续性或 $C^2$ 猜有限终止。也不从相对 metric 测试推整个十族准确 $|a_s|<1$ 域已认证；必要的真实末参数完整域责任保持独立。

## 400.8 原四 Loewner 条件的实际接入

设准确场的 Gram 矩阵为

$$
G=\begin{pmatrix}E&B\\ B&C\end{pmatrix}
=\begin{pmatrix}
F_s\cdot F_s&F_s\cdot F_q\\
F_s\cdot F_q&F_q\cdot F_q
\end{pmatrix}.
$$

给明确的 $0<\eta<1$，并设准确 target 对角分量的有效盒为
$g_i\in[\underline g_i,\overline g_i]$、$\underline g_i>0$。原 a601 形成

$$
P=(1+\eta)\operatorname{diag}(\underline g_1,\underline g_2)-G,
\qquad
N=G-(1-\eta)\operatorname{diag}(\overline g_1,\overline g_2).
$$

完整保存四项 $P_{11},\det P,N_{11},\det N$ 的闭区间严格下界。若四项都严格正，则二维 Sylvester 判据给 $P,N$ 正定，从而对这个闭 cell 上每个实际场/准确 target 成员有

$$
(1-\eta)g_* \prec G\prec(1+\eta)g_*,
\qquad
\left\|g_*^{-1/2}(G-g_*)g_*^{-1/2}\right\|_{\rm op}<\eta.
$$

这正是原 R251 判据；没有用逐分量最大误差代替算子范数。新源仅更换**真实目标输入**为 400.7 的准确十族和长度拉回，四个算式、strict 条件、Gram 所用完整六 jet 均保持。

某个 interval margin 不严格正只说明当前包围未证该 cell；它不是某点失败的反证。程序可继续原四子闭细分；达到 work/depth/time 限制即完整保留未付范围。源码不默认 $\eta=10^{-6}$，不预填任何字段已通过。

## 400.9 完整闭格、终端未付与其它闭面责任

初始计划沿每个真实 Hermite cell、两份反射前缀和完整 $q\in[0,1]$ 闭角区间枚举。rank、radial block 和 angular index 都可由 immutable plan 重建，角 $0,1$ 作为同一圆的闭端点均保留；共享空间端点亦保留。

每个未证 cell 按原 `split_cell` 分为四个闭子 cell。完整 DFS 有三类记录：

1. 已证/未证的 terminal closed cell，含其原 interval 运算和准确 target 候选。
2. 当前 root 的全部剩余 DFS cells，严格保地址、depth 和 dyadic path。
3. 尚未开始的 root rank 后缀。

已完成但未证的 terminal cells 仍在完整临时 ledger；未访空间不因最大见证或局部坏对数而丢失。若 input/setup/output 阶段异常，结果保整前缀责任未付；已有 ledger 可作为身份记录，却不能从截断日志补造整体通过。

`complete_accurate_ten_prefix_relative_operator_bound` 仅在完整 prefix partition 已遍历且每个完整 root 均被原严格判据支付时为真。即使它为真，以下仍是 false/unpaid：

- 完整 current-C native 径向场、同一个 shared B、两个 collar、两帽的实际比较；
- prefix/tail/collar/cuff/reflection 的准确 $C^2$ 接缝与目标 atlas 兼容；
- rounded renderer 与准确 Hermite 场的全域误差；
- 全闭曲面 standard 4、reach、held、embedding、全相位条件与整个课题完成。

原帽目标是原帽图形自身的诱导 metric，相对自身误差为零；不是“帽 target tensor 为零”。但目前没有实际新 shared-B/cap 输入，不能把这条结构事实记为某个未来帽已付。R248 的全相位归约也只能在其真实 family/共同材料角/全局接缝前提下使用，不在这里提前声明。

## 400.10 真实 shared-B 全闭链尚缺什么

旧 e70d loader 的实际路径明确依赖旧 complete/port/config/source relationship，随后实例化 6b06 `RefinedTail` 与旧 frozen-background 提供者。仅把 SavedPrefix schema 和 `load_shared_bundle` 名称换成 ten 会悄悄回到旧目标。因此本文没有这样做。

新 checkpoint 的 577×224 $Q/\Pi$ 和末端 338×112 J 也**不是**完整径向 Cartesian 场：全部径向 F、F_r、F_rr、mean 累计/规范、当前 geometry、完整 Fourier 节点及它们的共同来源仍须真正生产。实际完整后继必须具备：

| 输入组件 | 必须保留的内容 |
|---|---|
| 当前 C 真径向读回 | 同一末 native owner/checkpoint；所有真实半径与节点；全部112 shape、零模/means；全 F/F_r/F_rr 或来源明确的完整系数 |
| 有限 between-node 场 | 明确有限表达式及其真实两 jet，不把点标签当一致导数；所有拼接词/端点身份 |
| 同一 B | 实际完整 rational 节点及值/一阶/二阶；两 active sheets、collar、两帽使用同一个几何对象 |
| 完整 material/SE2/cut | 同一完整 core、真实 Phi、一个全局 rigid registration、cut chart 两导数、完整角修补所有混合项 |
| 真七元组 loader | `paths, plan, assembly, table, saved, A, binding`；新 ten/current-C identities，原 τ/空间责任/相位/帽合同不削弱 |
| 真目标 | 同一准确十族前缀与同一 C 尾部 $E(r)$，完整实际 cut/natural-Rout 包含；不能用 $1+(B')^2$ 改写目标 |

四源中的 `complete_closed_input_scope` 是这份准确缺口的可执行输出，不是兼容旧 7 元组的假返回。正在推进后继 current-C 径向 producer，不等实际 accepted 场才写接口；但只有真实完整 field 输入后才能执行相应几何，不能以一个 mock/fixture 支付它。

## 400.11 可调用 API 与最薄接线

### 400.11.1 当前 profile 与冻结

```python
owner = CurrentTenProfile(actual_factory_directory,
                          actual_factory_result_sha256,
                          code_directory)
view = owner.view(actual_ten_words, "three-active")
flow = owner.flow(original_augmented_module, actual_full_probe, view, workers)
boundary = owner.boundary(
    original_physical_boundary_module, view, actual_fixed_core_target,
    flow, actual_tail_map,
    height_sign=actual_height_sign,
    material_angles=actual_material_count,
    physical_angles=actual_physical_count,
)
```

所有名字中 `actual_*` 都是未来真实运行提供的值；本文没有为它们填默认成功输入。原实际 driver 仍须拥有初猜、当前 H、原 FD、原 full-DN main 和最后 audit。

同场冻结调用：

```python
frozen_view, frozen_flow, freeze_record = freeze_at_current_state(
    owner, actual_accepted_flow, actual_final_ten_words)
seed = fresh450_seed(
    owner, frozen_flow, actual_parent_mesh, actual_parent_augmented_states,
    parent_receipt=actual_complete_parent_receipt)
```

新 `owner.boundary` 的 target 长度必须为 0，$K=k=0$；不能把原 core 的 `coefficients[:3]` 不加处理地传给零活动视图。真实独立450运行必须用这个实际零 target 构造原完整边界，原求解器其它数学保持。这里没有通过修改旧 `fixed_modes` 标签来假装改过边界。

### 400.11.2 真现场 writer 与独立 reader

```python
writer = LiveCheckpointWriter(
    actual_owner, actual_flow, actual_boundary, actual_separated_boundary,
    original_full_dn_module, actual_raw_native_client,
    driver_source=actual_driver_path,
    complete_source_sha256=actual_complete_closure,
    original_law=actual_original_probe_law,
    parent=actual_accepted_parent_or_None,
)
receipt = writer.capture(
    original_result=actual_unannotated_full_dn_file,
    fd_result=actual_current_H_FD_file,
    fd_anchor_response=actual_FD_anchor_file,
    final_native_response=actual_fresh_final_audit_file,
    physical_cut_audit=actual_complete_cut_audit_file,
    out=fresh_owned_RUNNER_TEMP_directory,
)
```

三活动设计结果用 `parent=None`；零活动450必须传实际 `Checkpoint` parent。writer 自身不解 BVP，不给父 success 造假；`Checkpoint(...).require_frozen450()` 明确拒绝只有453的输入。

SavedPrefix 入口为：

```text
python computations/geometry_20261115_continuous_ten_frozen450_saved_prefix.py
  --checkpoint-directory ACTUAL_450_DIRECTORY
  --checkpoint-sha256 ACTUAL_MANIFEST_SHA
  --code-directory ACTUAL_PINNED_COMPUTATIONS
  --out FRESH_RUNNER_TEMP_METADATA
```

它现场求原全部二 jet 并构造完整保存场；没有本地 science，也没有未来 accepted 请求。

### 400.11.3 准确前缀 metric

```text
python computations/geometry_20261115_continuous_ten_frozen450_prefix_metric.py
  --directory ACTUAL_450_DIRECTORY
  --checkpoint-sha256 ACTUAL_MANIFEST_SHA
  --code-directory ACTUAL_PINNED_COMPUTATIONS
  --eta EXPLICIT_RATIONAL_ETA
  --precision-bits EXPLICIT_BITS
  --sqrt-bits EXPLICIT_SQRT_BITS
  --initial-angular-depth EXPLICIT_INITIAL_DEPTH
  --max-depth EXPLICIT_MAX_DEPTH
  --max-visited-cells EXPLICIT_CELL_BUDGET
  --budget-seconds EXPLICIT_WALL_PLAN
  --out FRESH_OWNED_OUTPUT
```

此CLI要求明确所有科学工作参数，没有选未来 field/eta。计时包含 source/runtime/input 解释；检查点在每个完整 cell 前，不是异步进程硬杀钟。原每 cell 完整计算不被预算中途当成功提交；外层 Actions step/job 时间仍需未来运行单独声明。

输出 `result.json` 与一份 `summary.json`；必要摘要≤90000B，若超限只给身份并返回70，不分包大raw、不声称完整读回。`large-arrays/` 仅原 job 临时含 source/target/exact-field identities、完整闭格 ledger 与所有 pending。程序不上传 artifact、Release 或 Git raw。所有未证但正常完成的区间诊断不作为native失败；实际执行异常有非零退出。

## 400.12 小结论、真实缺口与原目标保持

本次已经给出可运行的来源组件、真正450输入格式、完整物理 SavedPrefix 与准确十族前缀比较器；它们不依赖任何伪 accepted 场。准确 ten DAG 的全参数、支持、真实累计长度和 C 叶没有用旧nine或finite-Gauss模型替代。准确 Hermite 前缀的内部 $C^2$ 来自同组节点两 jet，并未借小 endpoint gap 冒恒等。

未支付的核心不藏在 schema 内：真实连续十族非零 full453 父与新450接受还不存在；完整 current-C 径向 F/F_r/F_rr+B、全闭七元组 guard、实际全局 seams/atlas/metric/reach/held 仍需实际完整输入与原责任。源码公开和本文条件证明都不是课题完成，也不是新增求解前门。

R400 将这些来源与数学对象分开，允许后继沿同一个已明确目标继续真实计算；它不撤原 static/R24、原全部物理方程、原当前H→FD→full-DN→fresh audit次序或README原完成条件。
