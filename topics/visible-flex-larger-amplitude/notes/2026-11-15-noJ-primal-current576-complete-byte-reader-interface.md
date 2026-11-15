# 实际73完整字节读取器：新同主路径576快照、R273和原行账

作者：`/root/exact_refinement`，GPT-6 Astra Pro，AI辅助；2026-11-15 UTC。

**类型：独立只读实现接口。已完成源码/AST核对，尚未读取73原artifact。** 它不运行或导入任何科学producer，不重新计算任何范数、矩阵作用、有理残差、QR、RHS/J/ODE、优化或原试步。实际科学结果保留原来的成功、失败或中断状态；字节回执不会替代或增加数学验收。

## 1. 已发生的run与来源

本入口固定到已经启动的actual73：run `43657001633`，源commit `9515d5aaf7c68f8efd366438d6bd81ce73c3486f`。artifact必须实际属于该run，名称为`visible-mainline-nojprimalnative-43657001633-<attempt>`；artifact id、完整ZIP大小和SHA256仍由CLI在真实生成后给出，代码没有伪填未来产物。

读取器独立派生自actual61已执行成功的`exact_20261114_read_current576_artifact.py`（65526字节，`791300246051bad9064a39cc181d0b5eb6d66d7978d73a28f0c8028f6d8e0329`）。旧源码未修改。新文件：

`exact_20261115_read_noj_primal_current576_artifact.py`，76963字节，SHA256 `c062117765addc2acf7b82ca1aa6ad87027ebab8d32c75673af382d24dd26f06`。

新文件中的科学source身份直接固定实际73的launcher `938fbec2…`、hook `099798e9…`、adapter `48297483…`、QR入口 `70bc10df…`及新flow `f9b292c4…`。所有完整64位SHA均在源码常量和原producer的`frozen_sources`中核验，缩写仅用于本段阅读。

实际传输仍复用`exact_20261114_fetch_pinned_public_artifact.py`，SHA `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。只在内存替换明确的actual tuple和读回schema，并在原API metadata核原run source commit；原HTTPS、跨host去Authorization、完整ZIP流式大小/SHA、CRC、路径/符号链接防护与新目录发布流程不改。token仅来自该Actions步骤的环境。

## 2. 失败初猜和新实现的身份分开

actual61的失败末状态仅是初猜。读取器核全部五个固定父件收据及首轮raw状态`b34daaf8…`，不要求父结果成功、不装载其旧J/因子，也不把旧withJ norm标成当前缓存。父件完整tuple沿已冻结69选择取件器和73producer回执；读取器不重复下载原61父artifact。

新`primal-flow-installation.json`与每轮snapshot局部副本必须逐字同身份。读取范围包括完整新module、两个原public依赖SHA、所有unique engine、576个stage到engine的索引、原factory参数及原root/rhs/rk4/local-J引用保留声明。依赖函数SHA按原保存记录绑定；读取器不执行这些函数，也不把记录的source SHA冒作新的数学误差证明。

原core中的唯一correction调用插入仍逐字可逆，原evaluate和十档trial正文完整SHA保留。**整个withJ流已改变**，因此旧“只改一个correction而其余流完全不动”的全局标签必须为false；core范围的唯一替换与新engine属性安装分别核验。原ready仅说明安装前原constructor来源。

## 3. 每轮完整快照与方向

完整目录是`native-noj-primal-current576-damped/iteration-NNN/`。每轮只有该真实fresh evaluation的十阵：完整577×224状态、576×224×224 J、stage out/residual、实际cut/far、H/target/σ/far graph。每个原chunk和全部576 J块独立核SHA、行序、形状、来源；负零按原bytes保留。后续轮使用各自当前状态，不重复强制首轮状态。

所有577个R273因子、每节点一次罚块、完整纯常数和实际z/δ继续消费已保存字节。确认1153次QR、1152次形成的原报告与完整464891392字节因子/常数账，核上下三角布局和实际underflow位模式；不重做三角解或系数形成。

完整方向checkpoint的全部129248个词与raw δ、负零sidecar逐字对应。全部cut112、576×224 stage、far112原方程整数账必须保存全部129248行和578个typed块。读取器验证顺序、每块绑定、原sigma词、记录的最坏见证operand字节及摘要，但不重新求和、除sigma、选最大值或求有理范数。原L2目标/梯度与原σ无穷范数按producer保存值读取。

首轮`current576-row-resolution.json`若存在，则绑定本轮stage11/Pi75的原out、输出节点state、r、σ四个词与原tol。该行是actual61/69各自的共同norm argmax，**不是**路径差最大的Pi104。读取器只复制保存的相邻词及有理比值，不调用`nextafter`或`Fraction`。诊断失败或缺省会诚实保留，不抹除其它科学读数，不成为接受门。

原非线性更新、最终sensitivity、fresh audit及native接受数学由原流程执行；本工具不重新验证它们的计算，只保全原文件和来源。对应trial/最终响应的语义读数由另一份native结果说明处理。

## 4. CLI与小报告

实际artifact已生成后在公开Actions使用：

```bash
python -u computations/exact_20261115_read_noj_primal_current576_artifact.py \
  --run-id 43657001633 \
  --source-commit 9515d5aaf7c68f8efd366438d6bd81ce73c3486f \
  --artifact-id "$ACTUAL_ARTIFACT_ID" \
  --artifact-name "$ACTUAL_ARTIFACT_NAME" \
  --expected-size "$ACTUAL_ZIP_BYTES" \
  --expected-sha256 "$ACTUAL_ZIP_SHA256" \
  --download-out "$RUNNER_TEMP/native73-original" \
  --out "$VISIBLE_OUT/native73-readback"
```

两个输出目录必须独立新建。代码只允许`GITHUB_ACTIONS=true`且仓库精确为`Rogerhu12/math-research-public`。源checkout须保原producer `frozen_sources`完整closure，以及新reader、冻结byte helper `exact_20261114_audit_damped_chain_bytes.py`（`5618d29c…`）和上述transport；不需要NumPy/SciPy来读取，也不导入科学adapter或QR类。

小报告沿成功61读者的稳定名称：`original-native-outcome.json`先写；然后`source-and-loop-byte-identity.json`、各轮`original-readout.json`/`reader-status.json`/`byte-summary.json`，最终`current576-readback-summary.json`。每份非压缩报告严格小于100KB。完整file inventory、raw ledger摘要及源级字节细节放`large-arrays/`并gzip，沿现publisher仅留artifact。

原科学失败、无iteration、部分snapshot或子进程未完成都有独立分支，不要求native_accepted=true。一个字节问题可使本reader非零退出，但原标量结果在深入核对前已保存；这不是原数学接受或后继调度的额外条件。

## 5. 本地已做的核对

完整新源AST通过；十四个标准库字节/IEEE/描述器/见证函数整AST与冻61一致；完整577factor/常数循环和十阵/J流读取仅按新身份标签变化后逐字相同。transport、byte helper、R273/kernel、core/evaluate/ten-trial原SHA、形状和物理固定输入保持。相对完整diff、`reader-source-static-check.json`和`reader-static-compatibility.json`同目录提供。

未本地导入新reader或任何数值模块，未消费未来73数组，未执行科学或构造新native结果。实际大包只由公开Actions读者读取，后续数值结论必须引用其真实原报告。
