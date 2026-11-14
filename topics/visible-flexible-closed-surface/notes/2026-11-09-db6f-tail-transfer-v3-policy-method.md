# 同一背景转移的四字段显式适配 v3

会话 `/root/tail_theory`，2026-11-09。状态：作者完成源码差分、参数门和真实已闭检查点的只读预检；等待未参与实现者全文独审。本稿没有生成新的有限曲面、背景转包或新 metric / 曲率证书。

## 1. 输入身份与允许的变化

新入口为 `scripts/db6f-tail-transfer-background-v3.py`，SHA256 `bdf6307fd93328b1ae70923caac2687fa19b0187ca9c723fe5d7072d7799a47b`。它完整保留旧入口 `scripts/db6f-root-transfer-background.py`，不覆盖或伪装成旧代码。旧版冻结 SHA256 是 `35aa82514ec2be4b78cf3670e97343d0ba50085a7a6a687273108fbb6eb09705`。

原已审 `NUMERICAL_KEYS` 之外只新增四个字段：

| 字段 | 本次允许的意义 |
|---|---|
| `iterationCheckpointFile` | 原迭代状态的输出位置 |
| `trialDiagnosticFile` | 原 trial 诊断的输出位置 |
| `trialStatePrefix` | 原失败 trial 输入快照的输出前缀 |
| `sharedEngines` | 已审 worker / client 的引擎分配与共享选择 |

前三项在 trial worker 中仅用于记录文件；第四项选择已有数值执行入口，不进入物理背景 profile 的定义。允许它们变化只说明背景 $g$ 的参数比较不应因这些字段拒绝；没有声称新旧求解轨迹逐位相同、实际扰动相同，或新候选已经收敛。源 checkpoint 的状态、Galerkin 模数、径向网格和所有新图依赖的证书仍按实际输入处理。

路径字段只允许字符串、显式 `null` 或缺省；`sharedEngines` 只允许真正的布尔值、显式 `null` 或缺省。比较键的存在性和值。因此未知键从缺省变成 `null`、从 `null` 删除、或改变其值都会拒绝，不能利用 `dict.get` 的缺省值把未知变化掩去。其他原物理参数必须保持 canonical JSON 值相同，包含 JSON 类型。该比较递归地区分 `False` 与 `0`、`True` 与 `1`，拒绝非有限浮点，并保守地把 `1` 与 `1.0` 当作不同；对象的键序不影响比较。

策略对象 `PARAMETER_POLICY` 与新脚本的实际 SHA 都进入报告。策略散列采用 `json.dumps(policy, sort_keys=True, separators=(',', ':'), ensure_ascii=True)` 的 UTF-8 字节，SHA256 为 `2b4fd1d141d9116157037d05748ab2a019c9033441453ee8e6ab917eb355eae3`。它不是用来代替实际检查的成功布尔值：下游仍须独立重核文件、策略内容和参数差异。

## 2. 六个背景定义绑定

新入口先要求旧有限图和输入背景包都已 `finished=True`，且包的 `finite_tail_manifest_sha256` 精确等于旧 manifest 的实际散列。它重新读取并散列包的数据文件，不解析或重建有限曲面的数组。

背景定义字典必须恰含 `checkpoint`、`calibrations`、`alpha`、`cell_zero_A`、`inner_A`、`outer_B` 六键。每个绑定文件都重新读取、核 SHA256；其中 checkpoint 的 SHA 必须等于旧 manifest 的 `inputSHA256`。早期 coarse 包不同的键结构不能通过本入口。报告既保留原六绑定，也保存实际解析到的路径；后续闭图 consumer 必须独立核这些文件以及 height / positive-alpha 的来源连接。

本适配不重求校准值、不换全局精确径向归一化、不以新 M15 数值检查点覆盖旧背景定义 checkpoint。若物理背景真正改变，这条同背景转移路径拒绝，而不是把变化归入数值字段。

## 3. 数学转移不变与两种输出的区分

作者用 AST 对照核实，`grid`、`fraction_vectors`、`affine_coefficients`、`write_npz`、`check`、`sha` 六函数与旧版完全相同。`main` 中从物理域端点检查起，直至交分割、精确 Fraction 仿射参数、向外区间多项式换元、边界薄盒系数 hull、余项取最大和 `write_npz` 的整个数学语句块也逐项相同。本次实际变化是前置来源 / 参数门与报告身份，原包含性证明可在相同假设下复用。

正式转移只接受真实的 `--new-manifest`，要求它完成并检查实际径向网格。报告的 `mode` 为 `finite-background-grid-transfer`，保留原 `finished`、新旧 manifest、数据散列、完整覆盖检查和实际新脚本身份。它仍只是同背景的 $w,w_r$ 点值包，不能微分包中的多项式，不能代付新扰动图的 metric、曲率、嵌入或 README 完成。

独立的 `--check-parameters-only --new-checkpoint` 模式不接受新 manifest，不调用 `grid`、`IntegratedTail` 构造、区间换网格、root、RK 或求解器。其结果只包含参数和来源检查：

- `status=read-only-parameter-and-background-source-preflight`；
- `mode=parameter-only-preflight`；
- `new_parameter_checkpoint` 及其实际散列，旧 manifest、输入包与数据的路径 / 散列；
- 原策略内容、策略散列、允许的实际参数差异和六定义文件绑定；
- `geometric_transfer_performed=False`、`finite_map_was_created=False`、`actual_new_root_flow_solver_calls=0`。

此预检没有 `finished`、`new_manifest`、`finite_tail_manifest_sha256` 或输出 NPZ。下游正式账本不得把它当成已转移的背景包。两种模式都拒绝覆盖已存在的输出。

## 4. 已执行的有限检查与范围

真实输入为已自然完成的 `prefix-amplitude-recovery-s025-iter004-01_tail_0001.json.gz`，SHA256 `07db124d2da380171b99e6d577255b43d4f5496fbd6d982d5dea1a6df873c2e5`。这是已收敛的四分之一振幅尾，不能称为目标 $s=1$ 的尾或完整 M15 前缀联解。这里只读取它的参数，用于提前发现将来的身份 / 参数接口问题。

原 M8 manifest 的 SHA 为 `da0795deed1303dac7a38b68ea168ffd2883d8a84559df77c10ed3e91498e1da`，输入 tight 包 SHA 为 `6655b639db57bd2635aa012d460dcfa5f77b4ebdea750568d23f6dac5e7a3c5f`。只读预检实际 exit 0，十二个差异键全部属于原数值清单或新增四键；六定义、包、数据和旧图来源全部匹配。

结果为 `2026-11-09-db6f-tail-transfer-v3-quarter-policy-preflight.json`，SHA256 `1e5a70147345f2acb83c6d491df70e4843daeff685077b96dce59be28fd7a519`。另有十七个纯字典作者检查，覆盖未知 added / removed null、未知值变化、物理值变化、布尔与数字的递归类型别名、非有限值、已允许字段类型及正常通过；保存于 `2026-11-09-db6f-tail-transfer-v3-author-guards.json`。它们检查实质的拒绝边界，不是新几何的数值试验，也不替代独审。

复现这次预检应在仓库根目录使用相同三个真实输入，并给新的 `--out-prefix`：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-tail-transfer-background-v3.py \
  --old-manifest topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  --packet topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-audit-tail-tight-final-packet.json \
  --new-checkpoint topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-amplitude-recovery-s025-iter004-01_tail_0001.json.gz \
  --check-parameters-only \
  --out-prefix topics/visible-flexible-closed-surface/notes/REVIEWER-NEW-PREFIX
```

待新 consumer 也独审通过，且最终真联解已产生真实新曲面 manifest，才允许执行实际换网格并重新证明新图各项连续界。当前没有提前执行这一步。

## 5. v2 到 v3 的审查修订记录

未参与实现的 `independent_geometry` 在初版逐行审查中指出：Python 的值比较有 `False == 0`、`True == 1`，该别名也可发生在嵌套列表 / 字典中。初版已修缺省 / null 的存在性，却仍可能把这些 JSON 类型变化误当相同。当前正式真实预检没有出现这样的变化，不影响该输入的十二键账本；但初版不足以支持不加条件的未知变化拒绝声明。

因此保留冻结的 v2 源码、方法稿和预检作为历史记录，另存 v3。唯一算法门变化是 `changed_parameters` 对同名值使用带 `allow_nan=False` 的 canonical JSON 比较；策略的 id 和说明随之更新。原数学转移块仍逐项 AST 相同，所有实际数值数组运算未变。正式下游应 pin 本稿 v3，不得只沿用 v2 的 SHA。作者重放器为 `scripts/db6f-tail-check-transfer-v3-policy.py`，其输出明确为作者检查而非独审。
