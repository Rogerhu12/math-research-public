# 闭图预算 v3 的显式转移入口独审

审查者 `/root/tail_theory`，2026-11-09。**PASS，范围限新 consumer 的来源 / 参数门、两模式隔离及旧数值账本保持。** 没有运行新图转包或几何、metric、曲率运算，没有 root、RK 或 solver 调用。

受审文件为 `scripts/db6f-audit-closed-budget-transfer-v3.py`，SHA256 `5ef8d229e0a19bc83381a2cdcaef8b24309e00a1fdc6b9409b20d7ca34092e49`。作者为 `independent_geometry`，审查者没有参与该 consumer 的实现。审查者实现了它所调用的 transfer producer；因此本审查不冒充 producer 的独立审查。该部分由另一审查链支付。

## 1. 身份与背景定义

新 consumer 显式 pin 三个代码身份：旧闭图预算 `0d68b718a43a69b24a865b1932e2700a47190724a3be4ea3f1202b56d1a59641`、旧转移 `35aa82514ec2be4b78cf3670e97343d0ba50085a7a6a687273108fbb6eb09705`、新转移 v3 `bdf6307fd93328b1ae70923caac2687fa19b0187ca9c723fe5d7072d7799a47b`。报告声明与磁盘实际文件都要通过这些检查；不会把新入口伪写为旧脚本身份。

允许的参数集合由 consumer 独立列出，并与导入的新 producer 实际集合比较；新增项恰为四个已审 I/O / engine 分配字段。策略内容和 canonical SHA256 `2b4fd1d141d9116157037d05748ab2a019c9033441453ee8e6ab917eb355eae3` 均独立核对。参数差异按存在性和 canonical JSON 比较，含嵌套类型，不会把缺省与 null、布尔与数字视为同值；未知变化拒绝。

`verify_definitions` 要求正式六键恰好齐全，并固定每个定义的实际 SHA。它重读六文件，再核 height / positive-alpha 的相同 checkpoint、calibration 表、positive-alpha 指向的 height 证书、tight-alpha 指向的 A/B 原输入以及共同 bookkeeping。`verify_source_context` 继续核旧 manifest 自身和实际 source checkpoint、参数字典、原包、原数据文件及六定义映射。这些检查没有用成功布尔值代替实际文件内容散列。

## 2. 参数预检不能进入正式预算

只读模式要求 producer 的明确 preflight status / mode，排除 finished、finite-tail hash、新 manifest hash、输出 data-file 字段，并要求零 root / flow / solver、未创建图、未转包三个标记。实际新 checkpoint 只贡献可读取参数及其 SHA，绝不被改造成几何 manifest。

CLI 同时拒绝几何、metric、moment、tail-first 或正式背景转包参数，之后立即返回。该调用图只读元数据及已有文件的哈希；没有调用 `grid` 或 `ExactHermite`。新输出自己也明确 `radial_grid_was_evaluated=False`、`geometry_metric_curvature_were_evaluated=False`、`README_complete=False`。

正式模式则必须有完整新 manifest 和 producer 的正式 `finished=True`、`mode=finite-background-grid-transfer`。它复核该实际 manifest 与输入 checkpoint / 参数、旧新真实精确径向域、跨度数和 transferred packet 的完整覆盖；只有此后才执行原闭图预算。故预检输出无法作为正式转移替代品。现阶段没有构造未来候选的假 manifest，也没有执行这条正式分支。

## 3. 旧数学账本保持

除新增的来源与参数接口，正径向归一化检查之后的旧几何 / Fraction / 体积矩 / metric 转移计算保持不变。审查者独立比较 Python AST：从 `positiveExactGlobalRadialAlphaProved` 检查到函数末尾，删去新报告中唯一的 `base_closed_budget_script_sha256` 字段后，与冻结 `db6f-root-closed-budget-v2.py` 完全相同。此前的 `q`、有向显示舍入和 `record` 也未变。

这只证明本次适配没有改原账本的不等式或算术，不重新证明旧几何引理，不把新的数值候选视作旧 M8/M12 曲面，也不提供新图自己的连续一阶、metric、曲率或 reach 结论。

## 4. 独立实际重放

审查者对作者真实已闭 $s=.25$ 检查点的参数预检执行了以下新 consumer 命令，实际 exit 0：

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-audit-closed-budget-transfer-v3.py \
  --check-transfer-policy-only topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-transfer-v3-quarter-policy-preflight.json \
  --height topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-audit-tail-background-height-rerun.json \
  --positive-alpha topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-audit-positive-radial-alpha.json \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-review-closed-budget-v3-preflight.json
```

它独立重新得出相同十二个允许差异键，所有实际来源和证明连接通过。输出没有几何完成声明。重放只支付这个真实元数据输入；未来最终 M15 联解 / 实际 XYZ manifest 仍需独立运行正式转包、重新证明新图所有依赖扰动的界，并通过最终全流程复核。
