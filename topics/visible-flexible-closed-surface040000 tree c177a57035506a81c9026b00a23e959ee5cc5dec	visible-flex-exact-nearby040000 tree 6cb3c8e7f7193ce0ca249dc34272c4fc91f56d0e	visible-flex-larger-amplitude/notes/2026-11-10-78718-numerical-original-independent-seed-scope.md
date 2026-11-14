# 最终独跑的原种子：已发表 M14、cold8000 与两段重放的区别

2026-11-10，Astra-visible-flex-78718bd0 / numerical_recovery。
**只读来源与协议解释；没有编写、准备或启动 cold8000 求解入口。**
本说明不新增 README 的数学完成条件，也不把输入预检或首 DN 称为独立全链。

## 1. 当前祖先真正声明的是哪一个 seed

原 97 项 reference 是
`notes/2026-11-09-db6f-prefix-spectral-affine-m14q512-01-launch.json`，
SHA256 `e45c553ea6832525c6a2719a197dbcc49a7ee5dd77badfb4b363e19a4b974a83`。
这里使用其冻结的**原真实 M14 输入和来源闭包**，并不使用后来或未来的 affine 试验结果。
原谱权真联解接口 §4 与实现 §1 已明确选择此输入，而非本轮 run02 的失败 CP。

所有下表文件实际位于本轮逐字重建的
`/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/`。
重建目录不是恢复旧进程。精确绝对路径、大小和全部散列另存
`2026-11-10-78718-numerical-original-independent-seed-bindings-01.json`。

| 角色 | 原文件 | SHA256 |
|---|---|---|
| 原真实 prefix seed | `2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14.json.gz` | `3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0` |
| 此 CP 自己的最后真 DN/J/audit | 同 stem 的 `_tail_0002.json.gz` | `009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762` |
| 原完整 tail config | 同 stem 的 `-tail-config.json` | `7b6f64680beb5ccc04d819b638a27499ab00b6742c964d41352339bec14da2c4` |
| 原 frozen profile | 同 stem 的 `-frozen-profile.json` | `bb55971c3463c27a10fcfddafd06a65e86f42d6c6d684adf2768e8dcd7d21b8e` |
| 原 chart | `2026-11-09-950f-prefix-adaptive-chart.json` | `c8c456a1ebc6b0ef1ac4af1a7540443a70229a1b9eda14d89294c610844a0035` |
| 原 linear port | `2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json` | `500e0a0c6d5388e07e3673ef192856804264c612edd6fe26ee09b882698a3702` |

原 CP 为 30,149 B，末包为 254,154 B。CP 声明 `solver_success=true`、
2633 节点和物理 collocation RMS `1.9978998186646144e-9`。
这只是已经关闭的旧有限 M14 联解身份；其整图未由这些数值达到本题最终 G5。
两 PP 块必须一并输入：`_coeff_00.npy.gz` 为 4,170,219 B、
SHA `233c33e9c194e66b45403d7044fe3e28fa4bcf9a1451ba9177b584b047d34db6`；
`_coeff_01.npy.gz` 为 1,064,379 B、
SHA `630dc63fead1d2ad46b24c6d71bb71a78c5874b192bc4aa19780374d71494028`。
原 summary/reproduction、已发布闭存清单及整个 reference 97 项继续有效，不能只拿 CP 头替代。

当前 direct-CSC run02 的 141 项 launch 正是从这对 M14 seed/末包出发；
当前 restart8000 v1 的 `ancestor_source_checkpoint/ancestor_tail_warm` 也保留这两个身份。
但 restart8000 的**直接** `source_checkpoint/own_actual_tail_warm` 是本轮失败 run02 CP
及其 `_tail_0003`，两者分别 SHA `b04af907…`、`b26fff3d…`。
这是公开记录的不同输入层，不能互相改名。

## 2. 原独跑协议实际要求什么

`2026-11-09-db6f-audit-final-independent-pipeline.md` §1 明确：
独跑可以用已有已审 warm/较粗解作为原输入，不需要重搜所有失败初猜和物理参数；
§5 也明确不必重走每段 amplitude continuation。审者必须在 fresh 进程中真正重求
完整 prefix + nonlinear DN 联解，再重新导出、作连续认证并生成网格。
最终 CP 的零更新重放、只重算固定 cut 的尾、读作者证书均不够。

同一协议 §3 的“只改 I/O、原 seed 不变”限定的是**一个冻结命令的精确 replay**。
它不意味着 README 另有“必须重现每一次失败”的条件；也不允许把一个换了 seed 的
新入口悄悄称为原命令仅 I/O 重放。区别应如实记录如下。

| 路线 | 实际重算范围 | 可以准确声称什么 |
|---|---|---|
| 从旧 M14 公开 seed 直接 cold8000 | 作者先另名冻结并完整审查：旧真 M14 + 自己旧末包；同 g/M14/N512/W14/tol/BC，max_nodes8000；审者真正执行全部新联解及后端 | 明确声明的独立冷启动计算路线。它与当前 failed-CP restart 命令不是逐字同 seed 的 replay。 |
| 旧 M14 seed → 6500 → 自己生成的失败 CP → 8000 | 审者按冻结参数真正生成自己的第一段和真出口，再以其自己的 CP/末包进入第二段，随后完整后端 | 对当前两段生成算法更直接的重放；第一段的数值结果仍须按实际状态报告，不能预造或强迫失败。 |
| 只把 root 失败 CP 指给另一个只读 prepare/final 检查 | 没有新候选求解 | 仅输入/身份预检，不能称已独跑。 |

第一条若被采用，seed、源和数值参数应由作者预先确定并审查，审者不参与选择或调优。
必须重新产生自己的成功 CP/实际末包、有限图及全部连续界；如果数学 payload 与作者
不同，就按原协议 §10 将它作为另一张同 g 图完整认证、比较并明确选择最终交付对象。
不能套用作者证书，不能声称两图逐字相同。这是新计算路线的诚实范围，
不是已经满足最终 README 或原精确 replay 的断言。

从工作最小性看，既有协议并未要求额外重做 6500 失败；直接从公开原 M14 seed 的
另名 cold8000 因而有明确依据。最终选择仍须与实际成功对象和完整复现包一致。
本说明没有对哪个 seed 更易收敛作新数值判断，也没有把 6599 的初猜诊断扩展到 cold seed。

## 3. M12 是更早的可选粗输入，不是当前 reference 的原 seed

旧 R21 metadata 声明的 M12 prefix 为
`topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64.json.gz`，
预期 SHA `2ab86890b3ddf84a6a23ddc1621b11ef05f90bb8e3c9899aeb06922d24b4e37e`；
其实际尾身份为同 stem 的 `_tail_0018.json.gz`，
预期 SHA `6241c30aa25355b73af2ed154e58dbc25297f7e11d97bfe040c64eb4e57458e2`。
这两个 SHA 此处来自已钉的 R21 common-cut/manifest，**本次未取回或核验这两个 M12 payload**。

协议一般允许已审粗解，但 M12→M14 涉及模式数及 tail parts4→8 的初猜转换，
须明确原 raw height/slope lift 后重新求 momentum、原边界 warm 修正与全部真实新 DN。
不能把它偷偷塞入仍硬钉 M14 seed 的原 97/141 输入门，也不能只补零旧 momentum。
所以“保原97/141祖先，仅移除本轮失败 CP 的重启依赖”的最小 cold8000 应回到第1节
已发表 M14 seed；直接从 M12 是另一条更早起点的明确新路线，无必要时不自动增加它。

## 4. 实际核查与未完成项

已逐字重验 reference 的 97 项，并把原 seed 的 8 个同 stem 文件及6个核心角色
写入配套小 JSON；这是哈希/JSON 检查，没有调用候选初始化、RHS、BVP、DN或导出。
root 的本轮失败 CP 仍按失败保存。restart8000-01 的工具出口未知，不由遗留文件推断；
restart8000-02 的工具退出由 root 的独占监控负责，本说明不消费其 session。

本轮尚无可采纳的最终成功 CP、正向终门或独立全链。任何 cold8000 新入口仍应另名、
另冻、审清完整身份与全部物理出口门；不改冻结的 restart8000 v1，也不因本说明启动求解。

### 来源

- `2026-11-09-db6f-prefix-spectral-true-m14-interface.md` §4：原 M14 真闭输入及原 restart 规则。
- `2026-11-09-db6f-prefix-spectral-true-m14-implementation.md` §1：原97项来源与五 I/O 差分。
- `2026-11-09-db6f-prefix-spectral-affine-m14-method.md` §1：引用真 M14 输入、不得混同 affine 输出。
- `2026-11-09-db6f-audit-final-independent-pipeline.md` §§1、3、5、9、10：实际独跑与不同 payload 的处理。
- `2026-11-10-78718-audit-restart8000-entry.md` §§4、7：本轮失败输入与启动前预检的范围。
