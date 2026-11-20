# R138 固定短根段单积分消费者合同

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

公开科学入口建议为 `fourfold_codazzi_radial_weight_root_budget_screen.py`；
scratch 源 `r138_radial_weight_root_budget_screen.py` 实现同一内容。
本合同只定义一个新完整数值目标：RS.15 的正积分 upper $T$。
它没有求值新的实际结果；只作 AST、原已成文件字段和 hash 的静态检查。

## 1. 数学目标与两个不同范围的门

完整证明为
[径向权无关的根预算筛查](../results/R138-supplement-radial-weight-independent-root-budget-screen.md)。
保持原真实 Qrepair、固定 $p=\tfrac12e_z$、原低1..96与全高 $j\ge97$。
只固定 $\ell=1/100$，不选择或求解任何新 $\alpha$、容量 ODE、finite Gram。

令 $r_*$ 为原真实根，$x=r-r_*$，$f=(1-x/\ell)_+$，
$v_+=v(r,0)$、$v_-=v(r,\pi/4)$、$\eta=-\gamma m>0$。
两反射轴上 $u=0$ 且物理角等于 moving 角。定义

$$
h(r)=\frac{222}{125}\min_\pm\frac{|v_\pm|}{1+Kv_\pm^2}.
$$

唯一新上界必须完整覆盖

$$
T\ge\int_{r_*}^{r_*+1/100}h(r)
\left[\frac{(26/25)^2}{\eta\ell^2}
       +385^2\eta K(1-x/\ell)^2\right]dr.
\tag{RC.1}
$$

$26/25$、385 是 RS.7–RS.10 由已成 high41 球给出的纯解析有理放宽，
并非本次重新计算的两个科学范数。独立 moving mean、原 mean rank 和环境
primitive 在该证明中保留；程序不重新求任何根 Fourier norm。

保存完整 $T$ 球并读回后，仅比较：

| 上端比较 | 可得范围 |
|---|---|
| $\operatorname{upper}(T)\le225$ | 使用原已选 GB 体预算和原 X `Gamma` 的整类 LC 径向权及自由外截段接收器门被排除 |
| $\operatorname{upper}(T)\le160$ | 使用同一已选 GB、任意两个双向 scalar Jacobian upper 的整类同式接收器门被排除；其平方根积至少1 |

前者不能冒充后者；两者均不排实际 BVP、不证明奇异、不排可达根迹或直接逆。
它们不授原误差的最佳下界，也不排另一个更紧的 GB 体预算。
若上端超过阈值，仅相应筛查未排除；目标仍可 `complete=true, proved=true`。
程序不将这种完整 false 门重试成另一个同名目标。

## 2. 独立 readiness/admission 与最小原输入

入口无需 W2C context。所有科学 import、Arb 和候选数组的读取均在 `run` 内，
并要求 `GITHUB_ACTIONS=true` 及本仓库身份；模块导入与 AST 不执行数值。
参数如下，13项全部显式：

```
--definition-source --positive --candidate --germ
--high --high-execution --two-mode --two-mode-execution
--physical --physical-execution --body-budget --body-execution
--output
```

其中 `definition-source` 只允许原
`scripts/fourfold_codazzi_root_axis_support.py`，SHA
`d152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79`。
仅调用其纯 `read` 和 `load_candidate`，不调用原 `run`、轴 ODE 或
`private_root_angular_definition`。旧数组的准确还原是原输入 materialization，
不作为新科学结果发布。

### 原 native 三对象

| 参数 | 完整 SHA256 | 资格 |
|---|---|---|
| positive | `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d` | 同原4650闭行、全部3594接口、完整 mean 和四块原容器 |
| candidate index | `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413` | 原5个lossless cubic shards、6145 nodes、65分量、完整 dyadic float 定义 |
| whole root germ | `397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864` | 原真实根整区间、原2549 piece、同参数中心与 scalar/complex germ |

只读恢复的 historical inventory 与原 axis 包完全相同：positive4、candidate5、germ1，
共10项。原 candidate index 和 positive parts index 是当前小文件；没有新增容器。
整个 positive 文件仍须先还原并核完整 SHA，不能只拿待积分的几行当原证书。

### 完整已成 actual 与 execution

以下8个当前小文件全部以精确 hash 读取。源码逐 execution 核 run/attempt、
成功 returncode、完整科学对象 SHA、0旧重算/旧producer与单 child 身份。

| 对象 | run/attempt | actual SHA256 | execution SHA256 |
|---|---|---|---|
| high41 | 44750653724/1 | `f3f97be683009e9c8ae461c25dfd17d782a61ea6feaf9b8b7967b3e28a9e835d` | `e753dd0ea848302ccbe41dc90a3cd8ab1a1a211985d7a7d3691d7ab6384a7687` |
| signed96/97 | 44745192261/1 | `95c80fdeeb3cf75327f028b1020db5aeda0fa3502aa6c0b3546c17ac6d2258c2` | `f66a976a0433204c9c043ab977d58439f091d2304b6cd9ef1df13eac0ae2c0f2` |
| X | 44737045152/1 | `1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec` | `999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92` |
| GB | 44745355257/1 | `5b5f374fb68e66ce25725195a9d574940e5ee7e9b273b6b55da90ada261ec492` | `9bc00f39ab9656ef3e3afbc64f3df20d8340bbe85b92be4bc17141a80f28a18f` |

high 内的 whole `two_mode` 必须逐对象等于独立读取的 complete signed 结果；
后者内 whole `physical_budget` 必须等于独立 X。signed结果中原 axis 与 mean 的
整对象也仅读：原 SHA 分别为 `b300ea209acb2239a93a87aa3f14d6d9c5f0ed3b5b88ea44b415e5078ea0cd92`
及 `de3a14606aa432fbd1f7707c277a33110f81ce6ca23fdfc6bfdf7e9d497623b4`。
其原 executions 已被这条完整输入链绑定；不另调用轴或 mean source。

旧实际球的直接 admission 仅检查原 RS 前提：

- `complete_new_scalar_bounds` 中 $b_0<1,b_1<2,b_2<2,(g_m)_0<3$；
- high32768格、全41条及 high positivity/Neumann 两门真实完成；
- signed32768局部与32768非局部格完整，三个原整球满足(RS.2)；
- 原独立 mean 的完整 `actual_mean_denominator` 下端大于17/20；
- X 的 `complete_derived_energy_bounds.Gamma` 下端大于59/50；
- GB6条完整，`new_records.aEE_upper` 所选球下端大于11/10；
- 原 same-Qrepair、complete mean、full high、非奇异/非全逆的 scope 保持。

这些只是读取已保存证据并核定准入，不把旧 scalar、旧矩阵或其严格门作为新目标。
`whole_original_references` 保存这些整个文件的 hash/identity/scope引用，不复制旧科学数组。

### 建议保留的当前数学 pins

除本科学源、合同、运维入口、generator、两个 index 和上述8小文件外，建议 pin：

- 最终公开 RS 证明；LC 的真实 η 平衡/准确容量证明；
- 原 actual high41、signed96/97、GB actual 证明；
- X 完整物理 residual 预算证明（同实际物理规范与旧 Gamma）；
- R138 `exact-residual-transport-and-fixed-interior-point`，提供同 $G$ 的 $222/125$；
- R133 `exact-continuous-repair-of-final-centre`，提供完整 repair $A_0<4\cdot10^{-18}$、parity和原接口连续性；
- R133 `whole-positive-reference-floor-and-cached-producer`，提供原正区 $K\ge0$ 和完整 native scope。

无需再 pin/读取未知未来 finite Gram、容量数值、原 negative 参数源或旧大日志。

## 3. 真根、原分区和两个轴的准确构造

固定原 $r_*\in[r_{lo},r_{hi}]$。完整新积分的保守外区间是
$[r_{lo},r_{hi}+1/100]$，并非以端点替换真正 $r_*$。
分区第一片是 $[r_{lo},r_b]$，其中 $r_b$ 为原 positive `BODY_LEFT`；
它必须同时在原2549 candidate piece、scalar germ 和 real complex rectangle 内。
其后逐原4650行相交至 $r_{hi}+1/100$，严格保留每个 candidate/intrinsic 接口；
最后一行仅作已声明的目标边界截断。

每片固定等分32个精确 rational 子片。程序核完整4650原 cover 从 $r_b$ 连到25/8，
再核新子区间无缺口、无反序，保存原接口 metadata hash 和新完整分区 hash。
新分区数组只在私有内存使用，公开仅 count/hash。

在一个原 candidate piece，descending cubic 的第$d$个系数准确取

$$
P_{+,d}=\alpha\sum_{j=1}^{32} c_{d,32+j},\qquad
P_{-,d}=\alpha\sum_{j=1}^{32}(-1)^j c_{d,32+j}.
\tag{RC.2}
$$

每个原 binary64 值以 `Fraction.from_float` 准确物化后求和，乘同一 exact amplitude。
Horner 的变量是整子片 $r-\texttt{nodes[piece]}$，不是片中点。
均值不再重算：body 用原 `row.bounds.mean_v`，germ 用原
`moving_mean_v.real`，均取其完整 signed lower/upper。

Qrepair 的全 $A_0$ 差给同两个轴 $|\Delta v_\pm|\le\varepsilon$、
同 mean $|\Delta m|\le\varepsilon$，$\varepsilon=4\cdot10^{-18}$。
所以分别使用

$$
v_\pm\in m_{old}+P_\pm+[-\varepsilon,\varepsilon],\qquad
\eta\in-\gamma(m_{old}+[-\varepsilon,\varepsilon]).
\tag{RC.3}
$$

没有丢 mean，也没有把 axis repair 当作零。两个 ball 之间相关性可以丢弃，因为
这里只有 upper enclosure；不在一个轴上重复额外加两个 repair 费用。
新 integral 内使用同旧 candidate 的线性投影定义不等于重跑旧轴 support 目标。

完整 gamma/curvature 来自原 `intrinsic` signed records，germ 对应 complex记录的real部分。
每个 body原闭行须仍有 $K>0$。首 germ 因跨真正根可包含负数，只有真正积分部分
$r\ge r_*$ 使用已付 $K\ge0$，取 $K\in[\max(0,K_{lo}),K_{hi}]$。
它不宣称 $r_{lo}<r_*$ 的填充区域也具有正曲率；填充区域只承载非负积分 majorant。
所有本次除式均另核 $\gamma>0,m_{repaired}<0,\eta>0,v_\pm<0$ 和正 denominator。

## 4. 完整 whole-cell upper 积分

对一个精确子片 $[l,r]$，有

$$
x=r_{actual}-r_*\ge\max(0,l-r_{hi}),\qquad
f\le \max\left(0,1-\frac{\max(0,l-r_{hi})}{\ell}\right).
\tag{RC.4}
$$

程序分别包住 $(-v_\pm)/(1+Kv_\pm^2)$，再取两个 upper 的较小者。
这合法支配两真商的 minimum；没有取 midpoint 或错误取 lower。
乘 $222/125$ 后与(RC.4)、完整 $\eta,K$ 合成为(RC.1) integrand upper。
导数成本 $(26/25)^2/(\eta\ell^2)$ 在整个保守覆盖中保留；真实区间外的
多余非负费用不会缩小真实 integral。每子片乘真实精确长度的有向 Arb enclosure。

因此积分 upper 是每一 whole 子片的正费用之和。没有交替符号抵消要求、
没有用点求积代替全片，也没有人为删 root 或尾段。
每个原片的32子格完成后，保存当前完整 directed sum，准确字节读回，再以该
保存球的 upper 继续累加。它是同一目标的断点，不是新增原目标结论。
最终确认全部新片和全部子片后，单独保存 `complete_test_integral`，再从磁盘
读回其完整球作两个门比较。

## 5. 科学 JSON 的准确26字段与有限发布

固定 kind 为 `R138_radial_weight_independent_root_budget_screen_v1`；
建议输出名 `radial-weight-root-budget-screen.json`。顶层字段恰为：

```
identity complete proved failure stage
expected_common_cells completed_common_cells expected_subcells completed_subcells
completed_positive_rows integral_prefix complete_test_integral current_exact_right
old_scientific_targets_called old_axis_targets_called old_mean_targets_called
old_high_41_targets_recomputed old_signed_matrix_entries_recomputed
old_GB_X_targets_recomputed old_geometry_ODE_calls new_capacity_ODE_calls
published_arrays whole_original_references scope strict_gates seconds
```

共1个新完整科学 scalar，即 `complete_test_integral`；`integral_prefix`只保同一累计目标，
最终二者相同。ball格式为 `complete_decimal_ball_v1`，含完整 integer midpoint、
integer radius、decimal exponent 和 `mathematical_direction=upper`。
所有旧调用/数组计数恒为0；目标开始前或途中异常保存真实 failure/已成前缀，
不能把未算子格补零或将准备过程写成complete。

严格完成 stage 为 `complete-radial-weight-independent-root-screen`。
两门分别同步到：

```
scope.original_Gamma_LC_receiver_budget_excluded
scope.all_scalar_Jacobian_LC_receiver_budgets_excluded
```

`scope.complete_integral_target_proved=true`只在整目标完成后设置；
`actual_positive_boundary_problem_singular`、`localized_receiver_budget_proved`、
`positive_inverse_proved`、`final_topic_complete`始终false。
whole result 与完整 execution 按现有最小公共 worker 保存；不发布候选系数、轴轨迹、
分区/子片科学数组、capacity矩阵或大日志，不创建 artifacts/Releases。
科学 child 的数值线程变量沿现有四项设为1，原 source/contract/manifest/README规则照常保留。
