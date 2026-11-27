# 新 meridian 积分值族的完整历史转移适配

日期：2026-11-27。

## 实际变更

本独立完整源 `fixed_fejer_meridian_memory_transfer.py` 从原 `transfer_fixed_fejer_stage_point_memory.py`（78863 字节，SHA-256 `afa2d6397c331b5bf55dd461bbf52a35839ff610d3db0f12a043e8eceef3b6ed`，Git blob `7f1f3971893d8895d7e1b8cc3612e563a44d3095`）派生。新源 78920 字节，SHA-256 `ae9e5b316e785bf85a223cb210ca812551bf615f0f56b8861f817877b9208021`，Git blob `732698d4f1ba5d4a312ff95701c30b462473dce9`。

全部变化为五处单次字面替换：当前 transfer schema；当前完整 source-binding SHA；同目录 binder basename；definition 中原 stage-point-only 的政策事实；definition 的 changed_model_fields 描述。完整补丁在再生器和 manifest 中保留，反向替换后整个原 78,863 字节源逐字恢复。

新 binder 为 `fixed_fejer_meridian_source_binding.py`，41,894 字节，SHA-256 `15cd8e201db8aeef7139baf0e82d9d18fcf190194cd33dc8b112bebe05a7dffc`，Git blob `54d58893654598e94687a448e2beccc776e1cfb4`。本次已完整取回该文件，并核其实际接口：

```python
compatible_legacy_model(old, new, current_pins, *, source_directory)
```

transfer 的 `_compatible_models` 只把完整实际 old/new 模型和当前全部 source pins 传给这一原签名。新 binder 先验证实际新模型及 policy，然后分别核实际旧模型；它只剥离明确的工作实现来源/schema/policy 以及 calibration 的两个来源字段，再比较余下完整定义。这里不以缓存为理由放松固定 target、base、seed/profile、Q、normal partition、自由布局或积分合同。

## 原历史和真实父的范围

原 PARENT_FAMILIES 整块逐字保留。它含真正受支持的同一 Fejér 目标父 `477499/274d`，以及原五个旧 peer 来源族。没有给 run13–17 或其它尚未完整适配的来源增加别名/兼容项。

独立模式只声明原接口支持的未知 peer；没有读过的 terminal report、final 点、typed 发现次序或完成状态不补空、不伪继承。旧 target 家族继续只承担已声明 provenance/未知责任，不成为当前新 target 的变量父。新 source 自己的同源 restart 仍由完整 caller source、schema、model 和 whole report 精确绑定。

以下全部完整函数正文逐字保留：`_parent_family`、`requested_parent_memory`、`load_memory`、`seed_from_complete_prior_final`、`validate_seed_metadata`、`validate_metadata`、`_complete_input_reports`、`_input_identity`、`_reread_transfer_parents` 和 `_reread_seed`。

原完整 walker 导入全部 inbound history、三类显式/受保护地址和全部 typed 行；原 ordinal、发现点以及来源 annotation 全保。typed prefix 不因默认候选 cap 而截断。原 source path、whole report/输入记录和实际 current caller 继续完整重读。原 120 对 source provenance 由本族完整 lower 锁表原样保存；上层新 source table 需保留这些真实父对，并另列新 runtime，不能覆盖成别名。本 transfer 对 caller 的全部 pins 逐项读取，没有写死一个较小角色数。

## 完整 final 十三成员

终态父必须先通过自己的整个真实 pure reader，且满足原完整 final/geometry 条件。checkpoint 的十三个实际成员、原 shape/dtype、全部 core/omega/H 字、固定 mesh/chart/前三槽、原标量、原积分/N、实际点摘要均按原正文验证，再重建全部自由词。reference seed 与 base.initial 保持冻结；旧 roots、J、Phi、工作场值、可行性或连续证据不迁入。

本次保留原 `_input_identity` 的全部 whole-file 要求，包括实际 preparation report。没有把跨 runner 的不同 metadata SHA 仅凭“同一个数学 g”改成相等。可接受父须真实满足原输入合同；未满足时不能借本 transfer 命名掩盖。独立固定参考初点模式不虚构父，仍按原接口合法存在。

## 动态 caller 和新缓存诊断

新 driver 的实际源码 SHA 从当前完整文件读取，其 SOURCE_PINS 也从同一字节读取，不在本 transfer 中预填尚未终锁的 driver hash。当前 normal 通过新的完整 source binder 绑定到 `388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4`。新增 meridian 缓存诊断只在完整 operator/latest 层消费；本 transfer 没有向旧 root snapshot 添加不存在字段。

本交付只改变严格来源接口和真实工作政策描述。独立、strict-terminal、同源 restart、显式完整 final seed 的所有原参数语义保留。没有新 CLI、没有削减数值预算、没有新增科学门。本机没有科学、AST、编译或 fixture 执行；仅做完整源文本替换、SHA 和原父逆向比对。未来实际 report、point、model、checkpoint、packet 和运行结果均未填。

## 完整再生

`reproduce_fixed_fejer_meridian_memory_transfer.mjs` 只读取整个原源，核 bytes/SHA，应用全部五处精确替换，核完整新源并反向还原原全文，然后写出完整新 Python 文件。

```text
node reproduce_fixed_fejer_meridian_memory_transfer.mjs --parent-source /absolute/original/transfer_fixed_fejer_stage_point_memory.py --output-source /absolute/new/fixed_fejer_meridian_memory_transfer.py
```

原 source 和新 source 均保留；本交付没有更改 refs 或队列。
