# 显式背景转包 v3：独立源码与参数预检审查

审查者：`/root/independent_geometry`，2026-11-09。作者：`/root/tail_theory`。**结论：PASS，范围是新入口的参数与文件身份门、原转包数学保持，以及一个真实已关闭检查点的只读预检。没有运行新的几何转包、径向网格、metric、曲率、root、flow 或 solver。**

## 1. 冻结对象与发现的旧门缺陷

受审脚本为 `scripts/db6f-tail-transfer-background-v3.py`，SHA256 为 `bdf6307fd93328b1ae70923caac2687fa19b0187ca9c723fe5d7072d7799a47b`。其数学基准是已审的 `db6f-root-transfer-background.py`，SHA256 为 `35aa82514ec2be4b78cf3670e97343d0ba50085a7a6a687273108fbb6eb09705`。

此前显式入口 v2，SHA256 `7e58e063788127e3f6f5ed609c4851d395436aa22da421e8e0d320eff527b184`，正确区分了键缺省与 `null`，但仍使用 Python 值相等。独审指出：`False == 0`、`True == 1`，这种相等也递归出现在列表和字典内。例如，把未知参数从 `false` 改为数字 `0`，v2 的差异表仍为空。这不满足其所声称的严格 JSON 参数门。

作者保留了 v2 与其历史预检，另存 v3。独立检查器实际重现了上述 v2 接受反例，再核 v3 拒绝同例。没有通过改写旧文件来消去失败记录，也没有把该纯参数门反例解释为已审 M8/M12 输入发生过物理改变。

新策略为 `visible-flat17-bookkeeping-keys-v2`，canonical JSON SHA256 为 `2b4fd1d141d9116157037d05748ab2a019c9033441453ee8e6ab917eb355eae3`。canonical 形式按键排序、无额外空白、ASCII 转义；逐参数值另设 `allow_nan=False`。键存在性先比较，随后比较完整 canonical JSON 值。因此：

- 新增或删除未知 `null` 不能隐身。
- 布尔、数字及其嵌套变化不能利用 Python 的数值别名隐身。
- 非有限数值被拒绝。
- 字典的键顺序不构成变化；数组顺序仍有意义。
- 整数 `1` 与浮点写法 `1.0` 也被保守地区分。这可能多拒绝一个数学上等值的输入，不会扩大许可的物理变化范围。

## 2. 恰好四个新许可键

独立检查新集合严格等于旧 `NUMERICAL_KEYS` 加以下四项，没有增添第五个新例外：

| 新键 | 允许类型 | 固定背景之外的作用 |
|---|---|---|
| `iterationCheckpointFile` | 字符串或 `null` | 迭代恢复记录路径 |
| `trialDiagnosticFile` | 字符串或 `null` | trial 诊断记录路径 |
| `trialStatePrefix` | 字符串或 `null` | trial 状态记录前缀 |
| `sharedEngines` | 布尔或 `null` | 选择数值 worker 的共享引擎配置 |

前三项在已冻 trial/shared worker 中仅进入文件记录分支；`sharedEngines` 在 coupled 客户端处选择共享 worker。它们不改变定义旋转背景的物理参数或冻结校准表。即便数值 worker 的选择改变某个离散解或其浮点轨迹，也不能因此挪用旧图的 metric 或曲率界；新图仍须由自己的 manifest 与证书支付。

所有其余参数的 canonical 值与键存在性都必须相同。这包括 `calibrationSteps`、cut/cuff、cap、保护层、源控制和解析背景参数。新的未知变化仍被拒绝。旧数值键集合的数学解释沿用其已审范围，本次没有重新扩大它。

独立检查器运行了 19 个纯字典接受/拒绝案例。覆盖四个许可字段、已知和未知物理变化、未知新增/删除 `null`、冻结校准计数改变、嵌套控制变化、两种布尔/数值别名、非有限数值以及新字段类型错误。全部符合预期。没有为这些检查保存假 manifest、假 checkpoint 或假 packet。

## 3. 文件身份与真正的同背景前提

`source_preflight` 对旧 manifest、已有 packet 完成状态和二者 hash 关系进行检查，重新读取 packet data 的真实文件计算 hash；要求背景定义键恰为 `checkpoint / calibrations / alpha / cell_zero_A / inner_A / outer_B`，逐一核对文件身份，并把背景 checkpoint 连接到旧 manifest 的输入 SHA。

这是一条**以已审原始包为前提**的转包接口。文件身份检查没有重新证明原始包的解析包含性，也没有仅凭一个自填 hash 字典产生背景数学证明。本次实际输入是已审的原始包；配对 consumer 还独立 pin 这六份冻结文件的指定 SHA，并核其 height、positive-alpha、tight-alpha、A/B 与 bookkeeping 的连接。新入口没有更换目标 $g$。

对正式模式，参数门在原 `grid` 调用前后各付一次，随后仍由真实旧新网格检验同一 cuff/cut 物理域。已保存的径向增量、精确归一化和原包分区继续进入原来的严格算法。这里没有把参数预检中的 checkpoint 借作新几何 manifest。

## 4. 原严格转包数学没有改变

审查者全文比较源码，并由独立 AST 检查逐项核实六个函数完全相同：`check`、`sha`、`grid`、`fraction_vectors`、`affine_coefficients`、`write_npz`。从旧包物理左右端点构造开始，经过新网格与旧包交分割、两侧二进邻值、正长度交集选择、Fraction 仿射换元、系数 hull 和余项 max，直到输出数组写入的**完整数学块**也与旧源 AST 完全一致。

新增的预检、参数与来源检查没有修改传入的网格、系数数组或余项。由此前已审转包证明，同一精确物理点所需的所有旧片仍被包含，边界薄盒仍取全覆盖的系数 hull。输出仍只是 $w$、$w_r$ 的逐点区间多项式包；不能对包中多项式求导而宣称获得新的背景导数证书。

这是静态的算法保持结论。本次没有运行正式转包，因此没有生成或认证一个新 manifest 上的转包数据。

## 5. 两种模式的隔离

参数模式必须同时给真实 `--new-checkpoint` 和 `--check-parameters-only`，并禁止 `--new-manifest`。它只解包参数、比较差异并核已有文件身份，随后返回。输出没有 `finished`、`new_manifest`、`new_manifest_sha256`、`finite_tail_manifest_sha256` 或新 `data_file` 字段，明确标记未转包、未创建图和零新 root/flow/solver。

正式模式必须给真实 `--new-manifest`，禁止参数模式 checkpoint；输出以新的实际脚本 SHA、旧 base SHA、完整 policy 与 policy SHA 记录身份。它不伪写旧实现 SHA。已有输出路径会被拒绝覆盖。配对 consumer 也要求正式 `mode=finite-background-grid-transfer` 与 `finished=True`，不接受参数预检作为正式转包。

## 6. 独立实际重放

输入为已关闭 $s=.25$ tail checkpoint，SHA256 `07db124d2da380171b99e6d577255b43d4f5496fbd6d982d5dea1a6df873c2e5`。只检查其参数与文件身份，不利用它声称最终 M15 联解或新图已经完成。

独立脚本为 `scripts/db6f-audit-transfer-v3-interface.py`，SHA256 `323a50a92391883c44c1fed3760d819715cc7babb5fc04700aa07b9b4048fb28`。实际命令从仓库根目录执行：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-audit-transfer-v3-interface.py \
  --author-preflight topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-transfer-v3-quarter-policy-preflight.json \
  --replay-prefix /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-audit-transfer-v3-quarter-replay \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-audit-transfer-v3-interface.json
```

检查器与它启动的纯参数预检均实际 exit 0。预检用时约 0.171 秒，峰值子进程 RSS 27,918,336 bytes。新预检 JSON 与作者记录**逐字节相同**，共同 SHA256 为 `1e5a70147345f2acb83c6d491df70e4843daeff685077b96dce59be28fd7a519`。重新得到相同十二项允许的数值/记录参数差异。

机器报告为 `notes/2026-11-09-db6f-audit-transfer-v3-interface.json`，SHA256 `618e01b5068ac4b60c8eda4db80d8e8df28115d17ec07f1e765b37e611aec047`。同 stem 的 replay、log 与 execution 记录已关闭，完整 argv、退出码与 hash 可重查。没有新 root、flow、solver、网格计算、曲面数据或 metric 计算。

## 7. 配对 consumer 与剩余工作

`db6f-audit-closed-budget-transfer-v3.py` 由本审查者实现，因此不在这里冒充它的独立审查。它已由 `tail_theory` 全文审查并独立执行参数预检；见 `notes/2026-11-09-db6f-tail-review-closed-budget-transfer-v3.md`，SHA256 `be9d4e9253fe719033c8d1a18bd6b85ea777171249b780bfe604802a5be13c51`。该审查明确不自审其作者负责的 producer，两个角色与证据分开记录。

未来最终 M15 真联解成立后，仍需实际 XYZ export、自己的共同 cut 与圆领、真实转包、各几何/metric/曲率账本，以及最后独立全流程。本次接口通过不代付这些工作，不修改已认证 M8/M12 的任何数据，不宣称 README 完成。
