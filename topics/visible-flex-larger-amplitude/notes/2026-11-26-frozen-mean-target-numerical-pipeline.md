# R684 最终均值度量冻结、同一 g 求解及 R676 精化的完整数值入口

2026-11-26，Astra-larger-e4e2a2bf-20261126 / construction，含 solver 的固定目标粗 Gram 接口。

这是 [R684](../results/R684-rotational-mean-metric-design-and-frozen-target.md)、R676 精确物理传递与 R689 连续固定均值度量证书的实现登记，**没有新增科学求解、误差下降、性能或精化完成结论**。所有涉及实际场、数组、目标和求解的执行都强制检查 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。本会话只在本地作了源码准备、AST/compile、无数据的 `--print-command` 和 CLI 旗标静态对照。

新均值设计的目标可以随候选变；本入口从选定的真实设计候选开始把目标固定。当前诊断初始场仍有约百分之一误差，不能因有了冻结程序而称它是合格结果。先看实际设计求解、同场幅度及完整几何结果，再选择值得冻结的对象。下列命令需要真实已完成候选报告和对应字节，不能把示例路径当作实际运行证据。

## 1. 冻结对象到底是什么

选定父场为 $F_*$，其材料角为 $\theta=\Theta_*(\phi)$，$\rho_*=\Theta_*'$。固定全圈角数 $N_*$ 和显式正权，在每个真实径向点 $s$ 定义

$$
E_*(s)=\sum_{j=0}^{N_*-1}w_j|F_{*,s}(s,\phi_j)|^2,\qquad
C_*(s)=\sum_{j=0}^{N_*-1}w_j\frac{|F_{*,\phi}(s,\phi_j)|^2}{\rho_*(\phi_j)^2},
\qquad \phi_j=2\pi j/N_*.
$$

`physical` 为 $w_j=1/N_*$；`material` 为 $w_j=\rho_{*,j}/\sum_k\rho_{*,k}$。前者明确是固定物理角有限均值，不冒称材料 Haar 积分。两者均产生只依赖 $s$ 的合法新目标系数。完整反射奇偶性使材料交叉项全圈均值为零；所有实际交叉残差仍要约束，不能对正 quarter 的交叉项另求均值扣除。

固定目标是 $g_*=E_*(s)ds^2+C_*(s)d\theta^2$，以及已声明的 R661 四个 p4 帽内图的自身诱导度量。帽的竖直平移不改变这个度量。$N_*$、角权、原 $\rho_*$、原共享五次 q 与解析 f/h/k 公式及帽配方一经冻结，都不随当前求解点或后续精化改变。

这是在整个径向定义域上的明确连续公式，**不是对旧径向均值数组作插值**。新观察位置直接回到冻结父场的原五次单元和原解析 lift 求一阶 jet，随后算同一有限角和。因而当前 mesh、M、N 可以变，而目标自身的 mesh、M、N* 始终固定。

### Manifest 身份

`frozen_mean_metric.py --report ... --bundle ... --out ...` 读取真实已完成报告，核最终 bundle SHA、规范模型及原来源字节，写 schema `R684-frozen-rotational-mean-metric-v1`。输入恰有五个角色：`bundle`、`node_report`、`scalar_input`、`observation_carrier`、`reference_carrier`。最后一项是父实际 `exact-tail-lift-profiles.npz`；它与 Gauss 观察载体不同。来源恰有 `evaluator/factory/operator/observed/batch/scalar/integer/hold` 八个角色。

数学身份对以下 payload 作 `json.dumps(..., sort_keys=True, separators=(',', ':'), allow_nan=False)` 后的 UTF-8 SHA256：schema、averaging、full_angles、canonical_model_identity_sha256、五个 inputs 的 role→SHA、八个 sources 的 role→SHA、domain、cap_recipe、mean_definition。`canonical_model_identity_sha256` 先从完整规范模型独立重算。路径、bytes、provenance、source_commit 和未付证书旗标不进入数学身份；它们仍保留审计用途。R689 独立复算同一身份及全部字面定义，不只相信自报 ID。

源记录包含 `repo_relative_path` 与来源实际 git commit。读取旧 detached worktree 来源时，若绝对路径消失，冻结器只接受当前仓库中同相对路径且 SHA 完全相同的源码；并核来源 commit 对应 blob。不会仅因为路径同名就复用。下一 Actions job 的五个原始输入必须重建到相同 bytes，并可通过 `--target-bundle` 等五个显式 override 绑定；无法重建时明确失败，不能用当前精化场代替原冻结场。

## 2. 当前完整 Jacobian 与目标的严格分工

原中间归一化残差为 $r=(e,f,d)=(|F_s|^2-1,F_s\cdot F_\phi/(a\rho),|F_\phi|^2/(a\rho)^2-1)$。记

$$
A_*(s)=E_*(s),\qquad B_*(s)=C_*(s)/a(s)^2,\qquad
D_*(s)=\operatorname{diag}(A_*^{-1},(A_*B_*)^{-1/2},B_*^{-1}).
$$

则当前固定目标残差和导数准确为

$$
r_*(x)=D_*r(x)+(A_*^{-1}-1,0,B_*^{-1}-1)^T,
\qquad J_*(x)=D_*J(x),\qquad J_*^T(x)=J^T(x)D_*.
$$

`FrozenMetricOperator` 在原完整 current-field operator 外实现这三式；保留原 core、rho、Theta、q、H 和解析 lift 的全部链。当前 rho 仍在原 $J$ 内变化；冻结父的 rho* 只用于固定目标求值，不对当前变量求导。这里没有 moving-mean 的两均值投影，也不能沿用 R688 的均值扣除。**所有原角零模/径向均值残差约束都恢复**。

`fixed_radial(P)`、`fixed_angular(P)`、`fixed_scale(P,3)` 是当前观察位置上的只读固定系数；`target.identity` 绑定数学目标。当前完整自由变量、所有原 node/midpoint 与 Gauss 正权、quarter 轨道权、原 H² 母范数、物理 H 映射及 coarse whitening 都保留。全部曲率工作行和完整历史地点仍在；临时有限工作集不会替代全已知地点的真实 trial 筛查。

数值 wrapper 目前有意只支持 **exact nested affine refinement**：以 exact Fraction 核每个当前符号径向单元确实嵌入某个冻结父单元，按两分量 affine 端点计算旧单元坐标。最后向数值 evaluator 交一个 binary64 u，显式记录这个 carrier 的舍入误差，不将其当严格区间。R689 连续核用共同精确分割处理全 s，承担单独的 outward 误差证明。

R676 加密之后 eta 的**节点索引会变化**。固定的是原 exact affine 的物理 eta 左右端、lambda、width 和全部规范 profile 定义；后续 launcher 从真实 transfer report 的 `refined_model.eta_start_node` 和 `lambda_value` 读取参数，绝不把粗网格的 885 再当精细网格索引。

## 3. 完整固定目标粗 Gram 与 v5

`frozen_metric_coarse_moments.py` 只做当前固定目标的粗加速。若 $B_0R$ 是原已刊同母范数粗映射，$L_i$ 是 R664 在当前固定目标残差处的正块，$w_i$ 为完整正权，则

$$
G_c=\frac{k}{\sigma^2C_0}R^TB_0^T\sum_iw_iJ_i^TD_{*,i}L_iD_{*,i}J_iB_0R.
$$

这正是完整 $K_{00}$；不含 moving-mean 的 $UM$ 扣除项，不等于旧 g0 Gram。源码把原 R681 六方向局部导数三个残差行逐项乘 fixed_scale，再按原角矩和径向结构收缩。对任意粗坐标的二次型都是同一完整加权平方范数，准确实数下半正定。

原粗 `free_direction` 的 core 首块为 literal zero；helper 在使用角矩捷径前绑定完整源码契约。若不能证实该既有布局，明确在 PCG 开始之前选择原完整 fixed-target v3；不会用零 core 假设删掉完整外层 $J$ 的 core 导数。原 $\mu$、背景 $1/\mu^2$、原 frame 和 whitening 均不变。Cholesky/数值/资源失败不裁剪负谱、不加 jitter、不换 $\mu$，也不称为几何不可行；进入 v5 之后的失败按实际截断状态报告，不自动重跑另一模型。

每方向先在当前 bridge 和实际 damping 构造这个可选预条件，随后交 R685 v5 的完整 active-face constrained inverse。`--coarse-preconditioner none` 明确通过 v5 的 v3 分支。方向报告记录预条件来源、目标 ID、fixed_scale SHA、frame/Gram 实际代价、wrapper/base 各入口的真实 J/J*/residual 计数和实际 v5/v3 状态；不以静态预计零调用冒充测得加速。

默认 scalar line search 采用 R687 的 `centered_phi_normalized=Phi−constant`，原 `phi_normalized` 同时保存。它只按正多项式稳定计算同一目标减固定底数；梯度、正残差 Hessian、权重和 damping 单位不变。`--uncentered-objective` 可显式保留原 scalar evaluator。不同 p/epsilon/scale 或不同观察测度的 Phi 不相减。

## 4. 可执行顺序

全部命令在该公开 Actions runner 上执行。`FLEX_REPO` 是本次 followup 实际源码 checkout，`FLEX_WORK` 是 runner 的原始数据目录。`FLEX_PARENT` 必须选真实已完成且已经同场检查的设计父或后续固定目标父。最初全分支 carrier/node/scalar 路径仍如下；一旦精化，以其真实输出替换 current 输入，冻结 target 输入始终绑定最初固定字节。

### 4.1 只在选定真实设计父之后冻结

```bash
python "$FLEX_REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/frozen_mean_metric.py" \
  --repo "$FLEX_REPO" \
  --report "$FLEX_PARENT/report.json" \
  --bundle "$FLEX_PARENT/final.npz" \
  --out "$FLEX_WORK/frozen-mean-g/metric.json"
```

默认 averaging 和 N* 继承这个真实候选报告，不能把运行中的初始诊断直接当已选解。stdout 给 manifest SHA、target identity、averaging、full_angles；`continuous_positivity_certified` 与 `complete_problem_certified` 明确 false。冻结本身只建立对象，不提供几何/收敛结论。

### 4.2 相同当前网格继续求同一个固定 g

`FLEX_FIXED_TARGET`、`FLEX_DAMPING` 必须由实际后继预算明确设置。`--target` 现在是**必填**，不默认继承设计的 `5e-7`；它是本次数值停止阈值，不凭命名成为 README 的“原求解容差”。例如某次明确采用 1e-12 仍需要真实证明误差下降到算法实际可达底线，不能靠这一数值完成验收。

```bash
python "$FLEX_REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_frozen_metric_actions.py" \
  --repo "$FLEX_REPO" --work "$FLEX_WORK" \
  --parent-report "$FLEX_PARENT/report.json" \
  --bundle "$FLEX_PARENT/final.npz" \
  --carrier "$FLEX_WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --node-report "$FLEX_WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$FLEX_WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --manifest "$FLEX_WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses-compact.json" \
  --frozen-target-manifest "$FLEX_WORK/frozen-mean-g/metric.json" \
  --eta-start-node 885 --lambda-value 1 --angles 2048 \
  --damping "$FLEX_DAMPING" --directions 2 --maxiter 64 \
  --qp-atol 0 --qp-rtol 1e-6 --active-rows 192 \
  --reach-safety-factor .992 --active-band .025 \
  --spectral-p 4 --spectral-epsilon .001 --spectral-scale .05 \
  --target "$FLEX_FIXED_TARGET" \
  --outdir "$FLEX_WORK/fixed-mean-g-first"
```

完整 parent-report 合并器会额外读取父报告的全部历史 trial/SOC/active/final 位置，不是只传上述早期 compact 文件。位置按 `(cell, binary64 u, binary64 phi)` 精确区分，不作 round13 或任意读取大小截断。单个父已经进入精细网格时，应改用其实际 carrier/node/eta/N，不能照抄这里的原网格值。

### 4.3 精确传递后对同一个 g 继续求解

以下例选择一次径向二分、保留当前 M 与 N；若要同步提高 Fourier 和角数，可显式加 `--modes` 和 `--angles`，只接受保留原 modes/原角点的实际加密。完整当前父需要是已完成 fixed-target 父。`--target` 省略时严格继承这个 fixed 父的 target；传入不同值会失败。若首步直接从冻结的设计成员进入精化，必须另给 `--target` 明确声明第一次固定问题的数值精度，不能继承设计筛选阈值而改称收敛。

```bash
python "$FLEX_REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/refine_frozen_metric_actions.py" \
  --repo "$FLEX_REPO" --work "$FLEX_WORK" \
  --parent-report "$FLEX_WORK/fixed-mean-g-first/report.json" \
  --bundle "$FLEX_WORK/fixed-mean-g-first/final.npz" \
  --carrier "$FLEX_WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --node-report "$FLEX_WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$FLEX_WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --manifest "$FLEX_WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses-compact.json" \
  --frozen-target-manifest "$FLEX_WORK/frozen-mean-g/metric.json" \
  --radial-factor 2 --directions 2 --maxiter 64 \
  --outdir "$FLEX_WORK/fixed-mean-g-refine01"
```

这依次运行：完整精确父位置收集 → 已刊 R676 `refine_fixed_g_fullclosed.py --transfer-only` → 本固定目标 solver。不会执行或重新标记 R676 原 g0/p8 数值 readout。R676 的 Hermite restriction/zero padding、全部原正权观察点 inclusion 和永久位置重映射直接复用。真实输出位于 `.../transfer/`；固定求解目录是相邻 `fixed-mean-g-refine01-solve`，避免命令/plan 同名覆盖。

精化保留真实父的 p、epsilon、scale、qp atol/rtol、曲率安全值、active band、固定 target 阈值和 scalar evaluator。默认 damping 读父 final_damping，显式改变时记录实际值。目标身份始终同一个。强制报告实际方向/接受方向数和零方向退出；fine 初始已经低于 target 而零步退出时，**不能称误差继续下降**。

### 4.4 相同测度的精化比较

fine carrier 的 `refinement_parent_stage_map` 和父 carrier SHA 证明所有父径向观察点实际保留，角数只允许 dyadic supergrid 且逐点核旧角点的 binary64 相同。solver 从自身完整 fine 残差数组提取 literal 父 rows/angles，使用原父完整正权复读一次旧测度 spectral loss/max，不额外读一遍物理场或调用 J。

报告同时保存 fine 自己测度的 Phi 和 `common_parent_measure` 的 Phi；只后者与已记录的相同 g、p、epsilon、scale、权重父值相减。若双方有 R687 centered Phi，则再报同一底数消去后的差；父没有时不伪造该数。全部是普通浮点诊断，不是 outward 连续误差证书。真实 fixed-grid max change 与 actual direction counts 可直接揭示未下降或零步，不自动把 sample_target_reached 当收敛。

## 5. 最小应读取字段和剩余验收

每个固定求解 `report.json` 至少读取：

- `source_commit`（实际 followup checkout HEAD，另存 workflow_trigger_commit）、`source_sha256_by_role`、bundle SHA；
- `frozen_metric_target.target_identity_sha256`、manifest SHA、frozen/current angle counts、target_materialization；
- `initial`、`final_statistics` 中 max_relative_gram、legacy_max、完整 spectral 和可有的 common_parent_measure；
- `directions[*].fixed_target_preconditioner`、完整 qp status/advances/真实残差重读、true line-search trials；
- `actual_direction_count`、`actual_accepted_direction_count`、`zero_direction_exit`、`actual_fixed_grid_max_change`、`final_damping`；
- 完整 parent/末态永久位置数、`final_curvature_points/filter`、实际峰值内存与 row-cache 成本。

每个 refinement-plan 另读 transfer 的实际输入/输出 SHA、exact refined_model、同 g identity、fine 初始/最终统计、actual counts 和完整失败原因。`refinement_convergence_certified` / `topic_completion_claimed` 始终 false，直到外部实际完成证据改变结论；这个源不替验收作决定。

这些求解入口的现有曲率 filter 仅是必要点约束，**仍未保证**固定握持/20%整像振幅、全局嵌入、reach 或含反射 Euclidean 非平凡性。它们必须对同一 actual field 重新证明。当前会话正在另做完整 D/L 预算与 ±p 全变量保护；这不通过“非零 core”自动推得，亦不继承旧父约22.8%的幅度。R689 要在同一冻结目标和当前原场上付连续相对 Gram/正定性；原 R661/f122 组合器再付同场全局几何、marking 和幅度。源码和有限方向数不是这些结论。

## 6. 完整小源与静态核验

| 完整源 | Bytes | SHA256 |
|---|---:|---|
| frozen_mean_metric.py | 26935 | 9d6440ab9f86cfe5312b78643e704a3ec861f2c5b6fd45047461af92eca81d28 |
| fullclosed_frozen_metric_qp.py | 62374 | 2020d6873b90e9c874de01e0b71e702cb73a9121f21aba68a113d990694ff59c |
| launch_frozen_metric_actions.py | 16730 | abf90ba2f0c050dee5b4415a0eb4ef564e4655dfbc157cfe9c9dff722b211064 |
| refine_frozen_metric_actions.py | 13674 | 9bfc964502cab208fa77ae3e0dc045b5d1c1e9f7aedb3b36637b95b165d40ffe |
| frozen_metric_coarse_moments.py | 21978 | a531818d75040ff571ad1249eecb3c18f7341284d1cdd86d2032b0f8f4ef9f63 |

静态末审另补 actual geometry 读数完整性：grid radius/principal curvature 或任意 witness principal/radius 出现非有限值时立即返回 incomplete，不允许 NaN 比较被跳过后仍标 complete；没有新增数值 fixture 或接受门。

上述源已全部逐行检查无 trailing whitespace。四个 construction 完整源 AST/compile 通过；launcher 的纯 `--print-command` 生成139个 argv 项、68个 flags，全部与独立 fixed driver 的 argparse 定义匹配，v5/frame/v3/centered/目标源路径明确。没有导入实际场、读取科学 raw 或启动任何科学数值 fixture。

沿用来源身份：原 frame `324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da`；原 R681 moment helper `da083ae9b20674a29121c25d5b57ef867fba442559a50791b7fc0b43d4db5719`；R685 v5 `76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8`；原 v3 `fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4`；R687 centered `5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01`；R676 transfer-only `2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a`；完整历史合并器 `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60`；完整 mean-parent launcher `e88c426370fd4fafa9ac6aba445a5a4483fbf2321258cffb68fc5f17e7220cd4`。
