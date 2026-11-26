# 完整 SOC 父报告进入固定 deep 度量精化：独立来源适配

本条是已有 R676/R690 精化入口的来源实现，不另立数学结论。
原五个精化源码不变，尤其真实节点生产者仍为
`refine_fixed_deep_scalar.py` 的 `5f1b285f…`。没有科学执行或粗场 fixture。

## 完整来源边界

新 `fixed_deep_refinement_parent_binding.py` 接受四种闭合身份：原完整
固定 deep driver `d3c35492…`、已刊原 fine driver `1745cfae…`、真正的
完整 deep 多轮 SOC driver `329ebd18…`、本次独立 fine 自身的明确新
schema 和完整实际 SHA。所有父须 complete=true，schema、报告 source
SHA 和实际完整源字节必须一致。

第三类另外绑定 `derive_deep_amplitude_separation_soc.py` 的 `d80f9af2…`，
调用它的完整 bind_report：从准确 `d3c35492…` 原体逐字重建整个 SOC
体，对 runtime roles、固定 profile、初末模型及谱参数完整核验。
没有把 SOC 报告改名来通过旧 ray binder。来源记录使用仓库相对路径，
不因不同 followup worktree 的绝对路径产生假不等。

原 fine 科学主体逐字保留，包括物理 eta、固定 profile/源/R/width、
原三个固定 core 与全部其余自由变量、精确角和径向包含、parent literal
a 重归一化、全部正权、同父谱参数/measure、完整范数、C 和幅度真筛、
完整永久点记忆与 line search。四个 `.diff` 给出完整源码差异。

## 算法范围

这个最小适配只增加可接受的真实父来源。fine 仍执行原 `1745cfae…`
完整 ray 算法，没有从父继承 SOC 轮次或修正。报告显式写出：

```text
fine_globalization_unchanged = true
parent_SOC_algorithm_inherited_by_fine_solver = false
same_SOC_globalization_refinement_claimed = false
```

因此不能把这个小适配当作相同 SOC 全局化的精化实验。真正同 SOC
完整 fine 体由独立的 solver 派生入口完成；它可以把本次 a616 完整体
作为准确 base，所有 parent 来源都仍是分开的明确身份。

## 五个锁定文件

| 文件 | 字节 | SHA256 |
|---|---:|---|
| fixed_deep_refinement_parent_binding.py | 4069 | b3e391847c6e1367ca43b3bc83f4f570aafd48e87eafe93f4d049d85b288cdbf |
| fullclosed_refined_deep_scalar_amplitude_qp_soc_parent.py | 77131 | a616e88c1f1bd256d298f167f05f0030488a7842ca4af42d53ba3f41d70dff85 |
| launch_refined_deep_scalar_actions_soc_parent.py | 25012 | d87826c2618d90cc0322f2fc89f04a518b1675ee3843f154655494b3d1fad643 |
| refine_deep_scalar_actions_soc_parent.py | 17574 | 58e426b0519253db8336bfdf07827dd482a4bd41285f0ba78ed5da50f816c665 |
| read_refined_deep_scalar_report_soc_parent.py | 16700 | 6777d58f8791968f6ee4fa5dd9b5f4aee9dcdcd90ae5cb72f89035f366c781cd |

新 fine schema 是
`complete-refined-fixed-deep-scalar-with-held-amplitude-budgets-soc-parent-v1`。
CLI 参数不变，只替换独立入口名。数学 target、所有准确物理定义及
5f1b 节点 producer 没有改变，不产生新的 freeze。

## 断线后的准确恢复与完整纯文本派生

执行环境曾丢失原 scratch。本次从公开原四份源码恢复全文，严格
按原锚点重建，五个结果均与断线前的完整 SHA256/字节数一致。根已
授权只 create_blob 上传未引用纯源码，唯一 commit/ref 仍由根执行；
没有传任何 raw 科学数组。

恢复后的纯标准库生成器 `derive_soc_parent_refinement.py` 消费
`soc_parent_refinement_source_edits.json`。后者是完整普通文本编辑清单，
含原全文 SHA、结果全文 SHA、每个被替换的原文字段与全部新文本，
不是二进制/科学数据或不完整补丁。生成器核完整原文和每段原子串，
输出完整新源并核原锁定 SHA，再做 AST/compile。读者可运行：

```sh
python derive_soc_parent_refinement.py \
  --source-dir <已刊原四源所在目录> \
  --outdir <新输出目录>
```

新编辑清单为 35633B，SHA256
`0855dd102e4215c8e57322c0ee2a8f8c64bb511db920bdb76d0c3ccff7484059`。
这次纯源码派生已实际产生上述四个完全相同结果；独立 helper 也已
实际 AST/compile、无尾空白和字节 hash 核对。没有执行科学 driver。

没有新 fine 数值报告、精化下降结论、连续 metric/reach/幅度证书或
课题完成声明。代码中的零步退出、停止阈值和同父统计边界仍按原说明。
