# R672 原子续接报告的完整几何消费者

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / geometry_path。

## 1. 独立新版与固定来源

原消费者是
[actions_closed_geometry_combine.py](../scripts/resume_20261120/actions_closed_geometry_combine.py)。完整原源 SHA256 为
`f61319c27fbbecf3905052d0f0dea81e567900e8757d10fc57d592aa21d08bdb`。

新增独立文件
[actions_closed_geometry_combine_v2.py](../scripts/resume_20261120/actions_closed_geometry_combine_v2.py)，完整 SHA256：

`6c02b43e451b5e98107e6cd2638fe442f31b5eed8fe288da61ed8e5302c92156`。

原文件不变。新源仅增加一个完整曲率报告 producer 分支、该分支的实际
身份与逐胞覆盖核验，以及诚实的新 provenance/schema。原 11 个 helper
函数逐个作了静态 AST 对照，全部相同；从 `H, beta` 读入到所有 target
判定的整个 Fraction 公式块逐字相同。`py_compile` 已通过。没有执行
consumer、数学核、几何扫描、fixture 或 Git 操作，没有修改运行中的队列。

本源接受以下两种曲率输入：

| 完整曲率 producer | SHA256 | 新消费者分支 |
| --- | --- | --- |
| 原 `actions_closed_curvature.py` | `8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385` | 保留原 f613 的兼容行为 |
| 新 `actions_resume_closed_curvature.py` | `f47610f9c43e7c2016fe9d2f93e7e86172da9f7994f8ee901f74a495665f33cd` | 同场原子续接完整报告，数学 kernel 必须仍为 8ca |

新 schema 为 `same-fullclosed-R670-R672-exact-R650-combination-actions-v2`。
报告写实际新 `source_sha256`、`base_consumer_source_sha256=f613...` 和
`curvature_provenance`，不把新 producer 或 consumer 冒标为旧源。

## 2. 实际同场与 profile 绑定

命令每次读取实际 `--bundle` 和 `--node-report` 的 SHA；代码没有固定任何
历史候选或 node 文件 SHA。即使同一路径在另一公开 Actions 再生为不同
实际文件，新报告也必须绑定本次实际文件才能被消费。

原 f613 的检查全部保留，包括：

- first 与 curvature 的 bundle/node SHA 等于当前实际输入；
- 四个径向、向外运算和 Laurent 数学依赖为原已绑定源；
- 当前符号节点数、完整 $M$、整个 scalar 身份以及准确 $S,R,H,$ width
  与两份报告一致；
- 当前 bundle 的非零 R671 lambda 明确拒绝，原多项式 profile 范围不扩大；
- first geometry 可以是原 eaa，或已证 0faa 半径续化，后者必须保留实际
  原 eaa 报告及其同 bundle/node 的完整祖先身份；
- first 的完整原胞覆盖、正支持/第一形式、帽界与非平面来源仍单独核对。

对 f476 新曲率分支还逐项要求：

1. schema 为 `R672-complete-curvature-continuation-v1`，实际 producer 为
   f476，`kernel_source_sha256` 为 8ca，first context 为 eaa。
2. 外层和 `field_binding` 内的数学依赖、bundle/node SHA 完全相同，
   `field_binding.field_metadata` 与报告的准确 profile/标量 metadata 一致。
3. 原多项式 profile、真实欧氏形算子、原法向约定、未修改数学核等声明
   完整；不得假设历史 candidate SHA 或继承另一个候选的曲率值。
4. 若 kernel 使用了可选 first-form 下界，该 first 报告 SHA 必须等于本次
   实际原 eaa 输入；当合并器当前输入是 0faa 半径续化时，绑定的是它已核实
   的原 eaa 祖先，而不是把 radius 新报告冒称为 kernel 当时读过的报告。
5. 如果 f476 明确没有使用可选 first 下界，则相应 binding 与记录中的
   使用标志必须一致。这种调用仍可用自己完整六 jet 读出的正第一形式界，
   不强造一份未实际使用的 first 报告。

可选 first 的身份核验不要求历史路径字符串相同；要求的是所指真实报告的
SHA 与当前输入/祖先完全一致。曲率结果仍必须绑定当前实际 bundle/node。

## 3. 新分支的完整胞与统一界检查

本消费者读 f476 的完整 `best` 和 `best_sources`，不接受仅含 coverage
摘要的跨 job 文件。它没有重新执行或回放 raw journal；raw journal 的
实际绑定与恢复由固定 f476 producer 负责。消费者如实记录
`raw_journal_replayed=false`，并对 producer 已输出的完整证据进行检查。

每个有效胞需要：

- 胞编号属于当前全部原胞，完整 $Q/r/L$ 配置与正 dyadic 覆盖规则合法；
- `curvature_bound_certified=true` 且未付浸入盒为零；
- 曲率上界为有限非负数，$E$ 与 $|F_\phi\times F_s|^2$ 下界严格正；
- 全原胞点、所有原模态和完整解析尾已经覆盖，确用实际第一形式和严格
  向外运算，没有用采样 $a(s)$ 替代几何；
- first-form reuse 标志与本次实际 first binding 相符；
- 对应 immutable 完整返回或旧 kernel 报告的来源路径、SHA 和种类存在。

`best` 的键、`best_sources`、实际已覆盖编号和计数必须一致。完整范围为
当前全部 $0,\ldots,J-2$；当前 923 节点即 922 胞，不硬编码另一个候选的
节点数或 hash。

消费者用 `Fraction` 将各个二进制浮点端点作为准确有理数读入，并要求

$$
U_{\mathrm{covered}}=\max_i u_i.
$$

只有覆盖全部原胞，报告的 `continuous_curvature_upper` 才可等于该最大值；
否则全域字段必须为空，完整几何合并保留曲率未付。浮点字段和 exact 字符串
均与实际最大值核对。每胞 target 计数及全域 target 标志也必须和报告给定
的准确阈值一致。

`8.1` 仅是前一调度器的细化目标，不是新几何合并器添加的硬阈值。只要
完整有限上界确实有效，最终 reach 条件仍按原准确 R650 公式计算；不会因
`target_certified=false` 就把一条真实完整曲率界删除，也不会因
`target_certified=true` 就跳过真实比例判断。

原两个平帽曲率为零、镜像与 R248 相位保持绝对曲率的完整范围声明同样
核对。报告的调度状态单独保留：一个预算 checkpoint 即使已经有完整严格
覆盖，也可以提供其真实界；一个自然退出但仍缺胞的报告则不能提供完整域
曲率证明。状态字符串本身不替代实际覆盖。

## 4. 原有几何公式与结论边界完全保留

在原 marker/grip 前提 $\beta=1/4$、$H>1$、$R>9/20$ 下，仍用
$h=1/1000$ 和原完整 body 界计算

$$
D_{\mathrm{marked}}=D+2h,
\qquad
L_{\mathrm{marked}}=\min(L,H-h),
$$

$$
\sigma_{\mathrm{marked}}=\min(\sigma,64/267),
\qquad
K_{\mathrm{marked}}=\max(K,5),
$$

$$
\operatorname{reach}_{\mathrm{lower}}
=\min(\sigma_{\mathrm{marked}},1/K_{\mathrm{marked}}).
$$

reach、held 与 grip 比例继续除以同一个 marked 直径上界；grip 直径下界
仍为 $9/10$。阈值仍为 $3/100$、$1/5$、$1/5$，全部用准确 Fraction 比较。
同场完整嵌入、正欧氏形状距离及反射排除仍要求原有 first/非平面/固定
witness 条件，没有删去任何条件。

`metric_certified`、`fixed_metric_refinement_certified` 和
`topic_completion_certified` 继续为 false。新增 producer 分支只允许使用
同一数学核已实际返回的完整曲率界；它不付统一近等距、不付另一个模型，
不把有限采样或调度完成当作研究完成。

## 5. 完整候选命令，未执行或排队

以下路径沿 worker03 的实际 runner 约定；实际 bundle/node/first 的 SHA
全部在执行时重新读。`REPO` 为固定 source checkout，`WORK` 为 runner
工作目录。代码依赖仅为本完整新源、Python 标准库与既有 NumPy；它只读
报告和 bundle 的小标量字段，不调用 scalar oracle、场或 Fourier 变换。

消费实际 f476 续接报告：

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_closed_geometry_combine_v2.py" \
  --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --first-geometry "$WORK/postprocess/continue-direct-radius-refined.json" \
  --curvature "$WORK/postprocess/continue-full-curvature-resume.json" \
  --out "$WORK/postprocess/continue-exact-geometry-combination-v2.json"
```

若当前 8ca 原进程自然完成，仍可用同一新消费者；完整命令仅将曲率输入
指向该实际原报告：

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_closed_geometry_combine_v2.py" \
  --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --first-geometry "$WORK/postprocess/continue-direct-radius-refined.json" \
  --curvature "$WORK/postprocess/continue-full-curvature.json" \
  --out "$WORK/postprocess/continue-exact-geometry-combination-v2.json"
```

输出文件必须是新的；已有组合结果不会被覆盖。当前工作没有替换旧队列项、
没有重启或停止任何进程。是否以及何时让后继 job 使用此源由父代理统一
安排；源码完成本身不冒充一次实际组合结果。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
