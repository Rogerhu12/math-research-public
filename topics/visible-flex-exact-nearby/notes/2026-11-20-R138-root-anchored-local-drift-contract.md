# R138 根锚定局部 drift 两标量消费者合同

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

公开入口建议 `fourfold_codazzi_root_anchored_local_drift.py`，对应 scratch 源
`r138_root_anchored_local_drift.py`。公开结果建议为
`root-anchored-local-drift.json`。本合同与科学源均未作任何本机新科学求值；
只完成 AST、原已成字段/hash 的静态读取与纯证明。

## 1. 完整新目标及真正根初值

数学依据为
[RA 根锚定局部 drift](../results/R138-supplement-root-anchored-local-drift-and-capacity.md)。
固定同一实际 Qrepair、同一个完整 moving 圆周、原 $m,u,v$ 与原

$$
d=-\beta I_\phi(u^2+Kv^2),\qquad
d_\phi=-\beta\Pi_0(u^2+Kv^2).
\tag{RD.1}
$$

新的完整目标仅为两个 scalar upper：

$$
D_{loc}\ge\int_{r_*}^{r_*+1/100}\|d_\phi(r)\|_\infty dr,
\qquad \Gamma_{loc}=\exp(D_{loc}).
\tag{RD.2}
$$

对应的辅助 flow 是 $\psi_r=-d(r,\psi)$、$\psi(r_*,\xi)=\xi$。
程序不求 flow，也不把 $r_*$ 换成 enclosure 端点；它只给其严格变分界
$\Gamma_{loc}^{-1}\le\psi_\xi\le\Gamma_{loc}$。
真正根上 moving 接收行与 flow 后根函数使用准确同一个角，因此 RA 的根容量
只付一次 $\sqrt{\Gamma_{loc}}$。physical $\Theta$、完整源 $H$ mean 和
原 $\mathsf H=\Theta_\phi(H\circ\Theta)$ 费用保持。

同一全域 body norm 可以另用原外端锚定 flow；本合同不把这两个辅助 flow
等同，也不删除原 body 的 Jacobian。原已选 GB 与原 RS 筛查均保持原结论；
本两标量不授新的体谱预算、根 finite Gram、完整 high 返回或正区逆。

预先固定唯一“接近1”的比较为

$$
\operatorname{upper}(\Gamma_{loc})<101/100.
\tag{RD.3}
$$

另只读比较新保存 upper 是否严格小于旧 X 保存 `Gamma` 的 lower。
后者比较的是两个已经选择的 scalar majorant，不能解释为实际旧 flow 的
最优 Jacobian 下界。任何比较为 false 都只表示该阈值没有被本 bound 证明；
只要完整两标量已成，科学结果仍可 `complete=true, proved=true`。

## 2. 最小输入与独立 admission

CLI 只有5项：

```
--positive --germ --physical --physical-execution --output
```

模块的 `admit_inputs(args)` 只作原完整字节还原、JSON/参数/分区 metadata 校验，
没有 Arb、原 producer、candidate numpy 或任何科学 import。
新数学只在 `run(args)` 内发生，要求
`GITHUB_ACTIONS=true` 和 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。
Arb 精度固定320bits。

| 输入 | 完整 SHA256 | 范围 |
|---|---|---|
| positive native | `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d` | 原完整4650闭行、3594接口及全 moving mean/primitive |
| true-root germ native | `397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864` | 原真正根整区间和同2549 candidate piece的完整复/实 germ |
| X complete actual | `1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec` | run44737045152/1，完整4651格及原 actual-DF/mean/接口 scope |
| X complete execution | `999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92` | 同完整actual身份、returncode0、单child、0旧target重算 |

`read`先核输入原完整压缩字节 SHA，再在原文件有 gzip magic 时解压JSON。
只读 historical inventory 是 **positive4 + germ1，共5项**；
没有 candidate5、旧 angular4、axis、mean、high41、signed矩阵或RS结果依赖。
原 candidate 身份仍经两完整native与X交叉核为
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`，
intrinsic object为
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。
不重新物化候选系数，不重新核任何旧数值目标。

科学源逐对象核同 exact alpha、fixed nu、metric eta、原 root interval与原
完整pair修补定义；X 的 complete/proved、4651格、actual-DF/完整mean/接口原scope
均保留。旧X的false body sufficient gate不改，也不作为新目标。
旧两个完整 scalar record `drift_derivative_integral` 与 `Gamma`原字只读保留，
不重新计算原全域积分或原exp。

### 原5项历史读取

positive4的历史 git blobs沿用当前原parts index：

```
21aeb58604b9b969f815ea23f437e3bcc9e069f5
3656cfd427b93a3fd7e58094aa7f6832d6e0296b
eddff9213f80635df57a35ce11b6751de1cbbda3
c26c0957b9eef2386e87f66a385d7871369eba55
```

每个原块解压后准确拼接成完整positive native，再核上述完整SHA。
原germ blob为 `2b90cfe80a6381badc29f02f7dcb3dce2584851d`。
历史恢复与其原 receipt 必须逐字记录；不新增科学数组或上传新容器。

### 当前必要 pins

除新 source/合同/worker/generator/manifest/workflow及原positive parts index外，
保留最终公开 RA、原 LC 平衡/容量、原 X 完整物理预算、原同Qrepair修补证明；
原正区完整closed-row接受证明可沿相同X输入链 pin。
X actual+execution两文件是直接输入。无需加入未来谱预算、旧RS单积分或
尚未求出的有限矩阵作为伪前置科学依赖。

## 3. 真根 padding、全部原接口及非负积分

原真实根满足

$$
r_*\in[r_{lo},r_{hi}],\quad
r_{lo}=1191984371497/5000000000000,\quad
r_{hi}=2383968743003/10000000000000.
$$

完整新的保守积分域固定为
$[r_{lo},r_{hi}+1/100]$。
第一片是 $[r_{lo},r_b]$，其中原body左端
$r_b=1192029371497/5000000000000$。
源码必须核此整片同时在原 scalar germ 与 complex rectangle的real domain内，
并保持germ原2549piece、compact bump整germ为零及原固定参数。

其后先验核整个4650行按原精确有理端点连续覆盖 $[r_b,25/8]$，
逐行保留 `fields_are_moving_phi_not_physical_theta`、
`complete_primitive_intermediate_retained`、`complete_mean_column_retained`。
所有3594个原interface metadata整对象按原序列hash，与X完整identity逐字相等。
只有与新短段相交的闭行进入新积分，最后一片仅在预先固定的新右端截断。

新分区每片都包含 row index 与 original candidate piece标签，保存完整分区hash与count；
原闭行已经证明的candidate/intrinsic包围直接读用，不从几条抽取行冒认完整输入。
无新子格、无新点求值、无 midpoint积分；原整行bound在其精确相交长度上积分。
因为积分费用非负，补出的 $[r_{lo},r_*)$ 与 $(r_*+1/100,r_{hi}+1/100]$
只增大上界。此论证不宣称补域是实际正区，亦不替换真实flow初值。

## 4. 原 moving Wiener 源与完整pair修补

每个body原闭行只读取：

```
bounds.U_A0
bounds.V_A0
bounds.drift_phi_A0
intrinsic.beta
intrinsic.K
```

前三者来自已成原Wiener $A_0$，后两者来自原完整signed real enclosure。
定义 $U_i,V_i$为其upper，$\beta_i,K_i$为绝对upper，
$d_i$为 `drift_phi_A0` upper。该角导原已含频率 $4j$，不再乘4。
完整 $v$ 含 mean；没有改为零均值 $v$。

germ只读取

```
moving_U_derivative_Astrip[0]
moving_v_derivative_Astrip[0]
complex_intrinsic_coefficients.beta.real
complex_intrinsic_coefficients.K.real
```

原 $A_{strip}$上界支配真圆周 $A_0$。由原Wiener投影 $\Pi_0$ norm不增，可取

$$
d_g=\beta_g(U_g^2+K_gV_g^2).
\tag{RD.4}
$$

原修补是准确完整pair bound
$\|e_u\|_{A_0}+\|e_v\|_{A_0}\le\varepsilon$，$\varepsilon=4\cdot10^{-18}$。
沿旧X的同一背景定义，整片保守使用

$$
\Delta S_i=\max(1,K_i)\{2(U_i+V_i)\varepsilon+\varepsilon^2\},
\qquad \widehat d_i=d_i+2\beta_i\Delta S_i.
\tag{RD.5}
$$

所有四个scalar来自原完整记录的lower/upper union，不用 `mid_float`、
`radius_upper_float`或缩短显示ball。每个bound的有限性与非负性须核。
germ/body同付一次(RD.5)，不重算修补系数，不将mean修补删除或重复当作新源。
额外因子2沿用原X安全费用；没有在新目标中偷偷收紧旧包围。

若原片精确相交为 $[l_i,r_i]$，其新贡献为
$(r_i-l_i)\widehat d_i$ 的有向upper。所有新片完整相加，得到(RD.2)第一项。
原系数在普通径向片上可piecewise；flow变分只积有界函数。
原Qrepair连续且原角导接口被保留，此处没有新增接口Dirac或删原界面。

## 5. 完整保存、读回及JSON schema

每完成一片，保存同一个累计 `integral_prefix`；准确字节读回后，以完整
decimal球的upper继续累加。它是单个新目标的可恢复证据，不是额外旧目标。
程序不覆盖已存在的前次完整结果或失败prefix。

完成全部新片后单独保存 `complete_drift_integral`，字节读回，再用其整球upper
取exp并保存 `complete_local_Gamma`；再次整球读回后才执行(RD.3)及旧Gamma比较。
ball格式为 `complete_decimal_ball_v1`，保完整整数midpoint、radius、decimal exponent、
`mathematical_direction=upper`，逐次核保存球包含完整有向值。
不允许仅保存float、十进制短显示或gate布尔来代替完整新scalar。

固定kind为 `R138_true_root_anchored_local_drift_budget_v1`；顶层准确24字段：

```
identity complete proved failure stage
expected_common_cells completed_common_cells completed_positive_rows current_exact_right
integral_prefix complete_drift_integral complete_local_Gamma saved_record_count
old_scientific_targets_called old_geometry_ODE_calls old_candidate_targets_called
old_X_targets_recomputed new_flow_ODE_calls new_capacity_ODE_calls published_arrays
whole_original_references scope strict_comparisons seconds
```

最终 `saved_record_count=2`，完整stage为
`complete-root-anchored-local-drift-budget`。
`integral_prefix`与最终完整积分是同一个目标，不能计成第三个新scalar。
所有old-target/old-geometry/new-flow/new-capacity/array计数均0。
完整 `scope` 明确保留真实root、fullmean、physicalTheta和原接口；
`localized_capacity_Gram_paid`、`new_spectral_body_budget_paid`、
`root_boundary_form_paid`、`positive_inverse_proved`、`final_topic_complete`
仍为false。没有把这两标量包装为原真实边界问题的可逆性。

运维失败必须如实保存在execution与未成科学prefix；科学比较false仍保完整成功结果。
公共worker只接收上述整个schema/完整两球，并在实际启动前已发表源与manifest。
实际Actions线程限制、真实pull/README检查、容量与非快进重试沿当前仓库规则。
