# 独审：同一有限图的独立 metric 收紧与旧曲率证书组合

审稿人 `/root/coupled_prefix`，2026-11-09。状态：**条件式数学差分和轻量实现检查 PASS。** 未参与该标量组合器实现；本稿不替代各输入证书的独立全域重跑，也不支付 README 第5门。

## 1. 冻结对象

目标为 `scripts/db6f-root-whole-metric-reach-v2.py`，SHA256

`20d9b6127625595afaf14daac4d23ccdd68d10f5d3a36d0697472f5df50d8fc3`。

旧版 `db6f-root-whole-metric-reach.py` 的 SHA256 为
`9dbb5f084d86227b5760a1b1d333b674d7586ec3b72ee195906cc5e7c147a3f8`。

已逐段核对完整差分。除新增 gzip 读取、可选参数、输入绑定函数和相应输出元数据外，唯一数值变化是

$$
\varepsilon_{\rm tail}
=\min(\varepsilon_{\rm old},\varepsilon_{\rm extra}).
$$

原有前缀/帽/尾曲率的最大值、正 support、直径、R10 reach、握持区与位移、严格体积矩、全部 Fraction 运算及完成状态字段未变。

## 2. 数学组合成立的条件

若两个已审完整证书分别对同一个精确有限映射 F、同一个目标 g 在整个尾及 collar 上给出 metric 上界，则它们的较小值仍是同一全域 metric 上界。旧证书已给出的**实际**主曲率上界只依赖该有限图，保持有效。无需因换用更紧的 metric 上界而重新解释或替换旧曲率数字。

因此 v2 取 metric 的 min、仍从旧完整报告读取 `principal_curvature_upper`，随后使用原 R10/Fraction 闭账本，逻辑正确。它没有把新旧不同图的指标拼在一起，也没有用 metric 改善自动支付源方程或极限存在性。

## 3. 新绑定函数的实际检查范围

`separate_metric_certificate` 核实新报告与旧完整报告的 finite-manifest SHA 相同，再检查 manifest 文件、packet 文件、packet 数据和逐行报告的数据 SHA。新 packet 必须 finished，其 finite manifest 必须仍相同；其非空 `background_definition_hashes` 必须与旧完整 packet 全字典相等。

覆盖检查要求已审后端的完整分割验证声明为 true、全部尾+collar 声明为 true、collar 包含、计数相同、有限跨数相同、选区为 `[-1,N]`、metric 浸入检查通过。之后独立读取逐行 gzip/JSON，检查行数、连续 packet-row 编号、每行有限非负上界、span 标签全集，以及报告全域上界严格等于逐行上界的 Fraction 最大值，且小于1。

**范围必须保留：** 这个标量函数并不独立重新打开 npz 并逐一核验 `u_left/u_right` 的无缝分割；它依据已审 metric-only 后端对这一点的验证声明，并用数据 hash 绑定到那份输入。`background_definition_hashes` 完整表示目标 g 的事实也由既有已审供应链支付。模块开头及输出 proof-dependencies 已明确输入数学有效性和独立审查是外部依赖，故这一分工没有形成当前组合公式的缺口。不能把本函数单独宣传为一个完整背景/分割证明器。

旧曲率报告、旧完整 packet/数据/行的绑定和所有完整性要求仍由原 main 分支执行；新函数未改这些变量。输出还保留旧 metric 上界和新报告完整绑定，允许追查 min 的两个输入。

## 4. 轻量独立重跑

审稿脚本 `scripts/db6f-prefix-review-whole-metric-v2.py` 执行了：

- 对已有 M12 critical-r01 闭账本，运行 v2 的无 extra 参数分支。原报告中的 **13 个 exact/Fraction 标量字段全部逐项相同**，实际曲率和 reach 未变化，README complete 仍为 false。输出为 `db6f-prefix-review-whole-v2-baseline-replay.json`。
- 以明确标为合成的微型元数据夹具检查18项输入契约：合法完整绑定被接收；错误 finite map、错误 packet map、unfinished、目标定义不同/空、数据 hash 不同、分割声明 false、collar 缺失、选区/计数错误、缺行/缺 span、行序错误、负数/非有限行界、全局最大值填高或填低均被拒绝。它们只测试绑定/拒绝逻辑，**不是几何证书**。

汇总 `db6f-prefix-review-whole-v2-checks.json` 绑定目标源、审稿源、实际旧报告、新重跑结果及命令。进程真实 exit0；没有重跑大型连续后端。首次调用测试夹具时，曾把旧报告中的 `notes/...` 路径按仓库根而非题目录解析，子进程在读预算前即报 FileNotFoundError；审稿辅助脚本改用原 `resolve` 规则后重跑通过。该次路径错误没有产生任何数值证书，不是数学拒绝案例。

## 5. 结论与重跑

**PASS，暂无必须修改的公式或条件逻辑。** 可在同一实际有限图/同一目标 g 的完整新 metric-only 证书已经被审查并完成后使用该选项；当前审查不预支尚未完成的新全域 bound。原真实 κ 证书照旧，G5 和最终网格交付仍为未支付。

在仓库根目录，使用新的输出路径：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-review-whole-metric-v2.py \
  --baseline-report topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-root-whole-metric-reach-m12-critical-r01.json \
  --replay-out /tmp/whole-v2-independent-baseline.json \
  --out /tmp/whole-v2-independent-checks.json
```

脚本要求目标 SHA 与本稿冻结值相同，并拒绝覆盖已有输出。
