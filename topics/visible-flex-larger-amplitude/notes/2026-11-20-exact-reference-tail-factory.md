# R671 解析参考尾：完整算子工厂与 Actions 构造接口

日期：2026-11-20。会话：Astra-resume-public-20261120 / geometry_path。

**状态：新源码已写成，只做 AST/编译语法与现有入口的文本核对，尚未执行科学代码。** 数学表示见 [R671](../results/R671-exact-reference-tail-affine-lift.md)。本条不登记新数值结论。科学构造、真实场读出和求解仅在本仓库公开 GitHub Actions 执行。

新完整模块为 [exact_reference_tail_lift.py](../scripts/resume_20261120/exact_reference_tail_lift.py)。它不改旧已执行源，保留相同 scalar、符号 mesh、$M$、固定 core 条件、所有旧自由变量、原全部 Gram 行与角 orbit 权。改变的是物理场的解析 lift；所有新场都必须重新读真实 Gram 和几何，不能继承旧证书。

## 1. 最小可导入接口

```python
ctx = exact_tail.TailLiftContext.from_files(
    bundle=parent_npz,
    carrier=original_gauss_carrier_npz,
    node_report=fullclosed_hold_warm_json,
    scalar_input=pulse_a5_complete_base_json_gz,
    scalar_source=original_fullhold_source,
    integer_source=original_integer_oracle_source,
    hold_source=original_hold_profile_source,
    observed_source=original_gauss_operator_source,
    eta_start_node=885,
    lambda_value=1.0,
)
problem, native = ctx.create_pair(
    original_dense_source, original_batch_source,
    N=2048, stage_block=64, quarter=True,
)
```

`problem` 有全部原节点/中点/Gauss 行；`native` 只作为原节点结构的 coarse $B/B^T$ 模板。不得把 `native` 的旧行目标代替 `problem` 的全行目标。两个对象共用同一新 scalar 表及定义。

例子的 `885` 是当前已有 Hold 节点，原符号定义为

$$
s_{885}=\frac{55}{64}S+
\frac{3794841132413436715}{36893488147419103232}.
$$

这只是一个明确的未试算构造参数，不是已优化的选择。工厂要求起点严格在原 Hold cut 后。$\eta=1$ 的起点不另选浮点近似，而是查找符号定义恰为 $(1,-\mathrm{width})$ 的原节点；当前为 `894`。它在 out ramp 前，仍属于弯曲度量。所有输入/源码 SHA、$\lambda$、两个节点的准确符号定义都进入模型身份。

`lambda_value=0` 直接调用原 observed 与 batch 工厂，返回原算子类；没有先作拟合或投影。非零 $\lambda$ 使用 R671 的方便形式

$$
f_\lambda=(1-\lambda)f+\lambda\eta a,
\quad h_\lambda=(1-\lambda)\chi+\lambda\eta,
\quad k_\lambda=-\lambda\eta I.
$$

`lift_scalar9` 的列顺序固定为

```text
h, h_s, h_ss, f, f_s, f_ss, k, k_s, k_ss
```

为准确复用原自由坐标导数，`lift_scalar` 保留前六列视图。原 core 的 $\Theta,\rho,\rho_\phi$ 链不变；原分母 $a\rho$ 使用原 carrier，未被新 lift 的 $a$ 中点值替换。

## 2. 原 oracle 的使用与误差范围

工厂读取原 `true_scalar_nodes`，把每个原观察行的 `(cell,u)` 转为准确的

$$
(1-u)(\alpha_iS+\beta_i)+u(\alpha_{i+1}S+\beta_{i+1}),
$$

其中存储的 binary `u` 被视为准确有理参数。这与原 Gauss carrier 的位置定义相同。$\eta$ 支撑内的 $a,I$ 以及两阶导数均由原 `FullHold` 的 integer/Fraction oracle 得到；$I$ 是原末端高度增量减去当前位置高度增量的**向外区间运算**，不是两个普通浮点积分相减后另定义 scalar。导数用原 $\alpha,\kappa$ 的 sine/cosine 分支，不用端点易抵消的 $\sqrt{1-a_s^2}$。

支撑外的新修正严格为零，不需为原 prefix 另定义或积分 $I$。raw carrier 同时保存 `reference_active`，未激活位置的参考六列零填充值不代表 scalar 为零。所有原行的新九列 profile 都完整保存。任意几何点使用同一 oracle，按准确符号位置缓存，不对新 $I$ 作径向插值。

新的 scalar carrier 有逐项向外绝对误差记录；这并不是完整浮点场的区间证明。$q$ 的现有 double Hermite、旧 $\chi$ 的 double 计算、symbolic mesh 的载体误差仍须由后续完整证书处理。新 profile 非多项式，不再援用旧 degree-six 径向 lift 或 Gauss 多项式精确性声明。

## 3. 真正更换的物理入口

新 mixin 完整覆盖以下入口：

| 入口 | 新行为 |
|---|---|
| `_first_batch_uncached`、`set_base` 的实际缓存 | 使用新 $h_s,f_s$，再加入 $k_s e_z$ |
| `_first` | 从同一个新批量速度入口读取，避免缓存与单点公式分叉 |
| `six_jets` | 全部位置、径向二导、混合导、角二导使用同一新 profile |
| `physical_jet_batch`、`physical_fields_batch` | 返回完整六 jet，位置含 $k$，$F_{ss}$ 含 $k_{ss}$ |
| `_lift_scalar(s)` | 返回新前六列，已有节点从共同表读取；使原 coarse 高度补偿准确改用 $h_\lambda$ |
| `lift_at(cell,u)` | 用原符号位置返回新九列，供任意点真读和 cotangent 使用 |
| `affine_diagnostics` | 帽端明确读 legacy 前缀的 `2*(J-1)` 行；不把最后新增 Gauss 行冒充帽节点 |

原 batched 完整 `jvp/vjp` 的公式在新前六列与新基场下仍准确：固定 $k$ 不产生未知量方向，但新基场必须含 $k_s$，因为 Gram 对基场的微分随之变化。高度列用 $h_s$，core 列用 $f,f_s$；所有原相对 metric 分母导数保持。

全空间求解器还必须绑定：

```python
geometry_module.fields_block = exact_tail.fields_block_observed
point_module = exact_tail.point_adapter(original_point_module)
```

`point_adapter` 创建原 point 模块的隔离命名空间，重绑定其函数，再更换任意点 `fields_at/pullback_at`。这样原 witness、working-set 和几何不等式入口都会读新物理场。stage cotangent 本身依旧只需前六列；固定 $k$ 的方向导数为零。没有修改原模块对象或其文件。

旧 coarse/v7 的独立 `ArbitraryField` 会直接实例化旧 dense 类，尚未由本工厂自动迁移，因此不能原样拿它读取新 bundle。本轮接线对象是下述独立新全空间入口与上述统一 point adapter。

原 `PhysicalSubspace` 的高度节点列通过 `native._lift_scalar` 得到 $B-h_\lambda$。因此原可逆物理高度坐标、完整 DI、角 $H^2$ 范数、coarse 白化继续使用真实新列；不能只给 full residual 换工厂而继续用旧 $B-\chi$。

## 4. 初猜迁移、raw 材料化与后继身份

```python
x, affine = problem.pack(parent_qjets, parent_H, require_affine=True)
x, migration = ctx.transfer_seed(
    problem, x, source_lambda=0.0, mode="nodal-projection",
)
record = ctx.save_carrier(raw_npz_path, compact_json_path)
arrays = ctx.bundle_arrays(problem, x)
```

`mode="keep-q"` 保留坐标数组，明确这是更换 lift 后的新场。`mode="nodal-projection"` 把旧 lift 减新 lift 的三 jet 加入原 $q$ 节点，其中径向 $e_r(\Theta)$ 只在**残差坐标的初始化**上作当前完整角网格 Fourier 投影。新的解析 lift 本身仍未截断。core 与终端数组字面保留。

这个投影一般不能保持连续场不变：有限角投影有误差，共享五次单元内部也因新解析函数而变化。报告记录当前角网格上的节点投影差异；它不是连续误差证书，也不算已接受的非线性步。迁移后必须用 `problem` 和新 point adapter 重读全部实际 Gram/曲率/半径/永久点，然后才决定是否进入原 QP。

非零 source lambda 要求输入 bundle 带实际匹配的 `reference_tail_model_json`，核对同一 scalar、符号 mesh、$\eta$、旧 source lambda 与 source 身份。`bundle_arrays` 只保留必要固定 scalar 数组、当前 $q/H$/core 和新的 canonical 模型 tag，不把旧场诊断或证书数组带过去。后继必须继续通过这个工厂读取，不能把含新 $q$ 的 NPZ 交给旧六列 lift 算子并沿用其几何值。

`save_carrier` 在本 job 的 work 中写完整九列与参考数组 NPZ，以及少量标量的 JSON 说明，记录实际 source/输入 SHA。raw 不进入仓库。公开结论可以只引用该小 manifest 与 raw 的实际 SHA。

## 5. 一个明确但尚未执行的 Actions 构造命令

以下 `$REPO` 是固定源码 checkout，`$WORK` 是现有真实重建链根目录。所有依赖都在公开仓库；scalar 输入、原 node report 与 Gauss carrier 由已刊 `rebuild_a04_chain.py` 生成。本命令只材料化新 profile/初猜，**不包含真场筛选或求解**；独立新 full-QP 入口随后负责这些工作。

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_lift.py" \
  --repo "$REPO" \
  --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-next-six.npz" \
  --carrier "$WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --eta-start-node 885 --lambda-value 1 \
  --angles 2048 --stage-block 64 \
  --write-seed nodal-projection --source-lambda 0 \
  --outdir "$WORK/geometry_path/exact-reference-tail-materialized"
```

实际入口若直接构造同一个 context 并接 QP，可省去这个单独材料化命令，避免在同 job 重算同一输入。该模块没有另建 fixture、独立审计门或额外批准流程；当前只登记新实现和完整依赖接口，所有数值状态保持未执行。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
