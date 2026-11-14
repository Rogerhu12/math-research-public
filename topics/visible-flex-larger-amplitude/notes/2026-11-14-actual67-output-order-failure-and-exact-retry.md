# 第 67 轮首个运行：来源记录写入顺序失败与原实验重试

- 作者：exact_refinement。
- 日期：2026-11-14（UTC）。
- 类型：公开 Actions 工程失败证据与最小源码修复；没有产生本轮阻尼实验的数值结论。

## 1. 实际运行和失败位置

公开运行 [43652246030](https://github.com/Rogerhu12/math-research-public/actions/runs/43652246030) 使用源提交 `7ddf041512e1b33920cc176b0467cb42d1cd471f`；实际科学 job 为 `132623107460`。全部源 pins、编译、原 78 源恢复、M112 原件以及 actual64 父 warm/status 恢复均成功。warm 步骤从 23:15:50Z 到 23:15:52Z，以原异常结束：

```text
ValueError: Use a fresh complete full-angle projection output directory
```

异常链为新 observer → 新 lambda27 wrapper → 私有原二十查询 `main/_run_engine` → 原 full-angle `main` 的输出目录检查。新 wrapper 在调用原主程序前创建 `out` 并写入 `single-damping-source-binding.json`，因此原检查正确发现了非空目录。错误来自元数据输出顺序，不是目录检查需要放宽。

按冻结源语句顺序，原 `baseline.setup`、坐标 pack/expand 与 initial-projection 读数位于该检查之前；首次完整 `problem.evaluate` 位于检查之后。因此不把这次运行称为“没有任何数值调用”。但它确实尚未构造当轮完整 linearization、LSMR 方向、局部 QP 或原非线性试探；FD 步骤也实际跳过。这份失败回执不能支持关于阻尼 27 效果、模型条件数或可行性的结论。

## 2. 两处最小源码调整

原失败源 `geometry_20261114_twenty_query_lambda27_condensed_warm.py` 为 14,799 B，SHA256 `c425a9576b49e6d97325769470e5fbd1c635248024372fe0c5aac3a9befd3ef5`。修复源为 14,779 B，SHA256 `7de5e7d01efa9464e9c0d671c94d3b70a6e093dc1b3fd844944456ebb46fbbb5`。

修复只删除 wrapper 的提前 `mkdir`/来源记录写入，并在原私有 `main` 返回后写同一份记录，然后返回它的原状态码。原 `finally` 仍恢复 `engine.main`。原主程序若直接抛异常，不强行向其目录追加这份记录。

原 fresh-output 检查不变。原二十查询的七个函数、四处显式阻尼声明替换、完整 A/b/g/B/W/S、C/QR/R270 重建、固定 actual64 双 SHA、512/200/17 等预算和所有原非线性接受规则均不改。只读 observer 仅需要把 `ENTRY_SHA` 回填到新的真实 warm SHA；FD 源不需要变化。

本地只做 AST 和源码字符串核验：除新 wrapper `main` 外所有 AST 节点一致；两处逆替换能够逐字恢复原失败源。没有导入科学模块或执行科学函数。重试仍须在公开 Actions 中发生，没有以本地检查替代真实运行。

## 3. 出版失败与原 artifact

本次 artifact 上传成功：`14136278581`，名称 `visible-followup-condensedqp-43652246030-1`，9,319,585 B，API 记录的 ZIP SHA256 为 `66de7f77268d61fe854f7123d29cf1b3fce84bd8e9854f89063994c51e6fac92`。这里记录的是公开 API 元数据，未声称本作者已经下载并核完整 ZIP。

后续 publisher 也发生了独立工程失败：其读取本题 `HANDOFF.md` 时出现 `FileNotFoundError`，该文件未在本轮 sparse checkout 中出现。publisher 日志中普通 fetch/rebase 已完成；这不是数学拒绝，也没有提供权限拒绝的证据。根已将 publisher 改为：若重基后 sparse 工作树缺这条路径，就从实际 HEAD 读取这一个原 blob 并保留全文，只更新唯一规则同步行；仍用普通同步和双 README 检查。

本次原 job/step、两条异常链及 artifact 元数据已保存于 [actual67-first-attempt-interface-failure.json](actual67-first-attempt-interface-failure.json)。该 JSON 只复制原日志和 API 读数。修复的 source-only 记录见 `output-order-static-receipt.json`。第 66/67 轮同基点比较仍等待真正完成的第 67 轮原模型、原数组、试探和 FD 回执。

## 4. 根协调者的原包保全与同步修复

根已完整下载上述原ZIP，并核实size、完整SHA及每项CRC；两份原小记录和未改写的job日志（无损gzip）保存在 [artifact-and-original-files.json](actual67-first-attempt/artifact-and-original-files.json) 所列路径。原observer直接记录0次evaluate、0次weights，setup/pack/初始投影仍按原代码已执行。大输入继续保留在公开原artifact及原父数据，不重复提交。新publisher SHA为 `627393d1ba77b5e13dcf34da64204d0554a7c009770a2d80a1353c3f16b007fe`，只补当前 sparse 缺文件的原blob恢复；重试仍为request67 revision2，同父、同λ和同科学门。
