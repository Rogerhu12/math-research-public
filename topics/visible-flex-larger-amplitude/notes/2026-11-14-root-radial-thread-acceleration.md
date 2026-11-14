# 在原实际 A 上加速径向 RHS，不改数学问题

/root（GPT-6 Astra Pro，AI辅助），2026-11-14。

**状态：实际代码优化和有限数值一致性结果。没有产生新曲面。**

## 改动及原因

原 A 的九控制响应记录中，完整 Jacobian 装配约64.84秒、平衡分块 QR约20.53秒，而全作业约2081秒。主要时间花在每个控制的全步/半步正负扰动对完整径向场评价 RHS。现有 QR 已用稳定的平衡分块消元，因此本次保留它，优化彼此独立的径向批次。

新 `root_20261114_radial_threads.py` 仍调用已构造 Flow 的原 `fun`，保留原24点批界、全部有限Fourier模式、实际角网、每点浮点运算及返回列的顺序。每个线程深拷贝自己的 Flow（包括已构造的 Fourier-Jacobian 表），避免共享可变缓存；返回后合计原回调计数。不 fork 进程，能与原资源记录线程及 tail worker 共存。异常会正常向调用者传播；没有放宽 Newton、RMS、完整H、边界或最终audit条件。

通用入口 `root_20261114_threaded_entry.py` 只临时替换 `root_radial_batching.value`；`state_jacobian`、边界与原目标入口原样执行。原源文件均未修改，包装器、被调用入口及适配器SHA保存于本次运行记录。线程数默认4，BLAS/OMP/MKL仍为1。

## 实际比较

完整复现脚本为 `root_20261114_radial_thread_benchmark.py`。它读取真A的原固定视图，加载当前正确provider，先构造原Fourier-J表，再分别调用原serial value与新value。脚本默认从原保存包读取 config.angular=1280，实际Flow仍为1280；请求值、原配置值和实际值分别记入结果，不将低角测试替代生产配置。对全部2590个物理节点、97维状态，共251230个返回值：

- 每个 binary64 值逐位相同，最大绝对差为0。
- 两条路径都产生108次原24点批回调。
- 本次并发负载下，原serial为42.145730287秒，新4线程含复制为17.425925490秒，约2.42倍；峰值RSS363896 KiB。
- 这是本机本次测量，不能解释成所有未来任务固定有2.42倍加速。此前显式请求512而原Flow按最低规则使用520的低角诊断也逐位相同；该次72.65秒→20.60秒只是不同离散与负载的测量，不能冒称原A生产1280结果。原先未提交草稿把这一低角测试称为生产配置，现已纠正；本节及摘要均为重新实际运行的1280比较。

完整小结果及原文件哈希见 [benchmark](2026-11-14-root-radial-thread-benchmark.json)。数值一致性检查针对实际 A，保持以后原方程接受标准继续适用；不能用该优化代替未来新设计的非线性求解。

## 复现与使用

在恢复原 A fixed-view 与91个固定依赖源后，运行：

```bash
python computations/root_20261114_radial_thread_benchmark.py \
  --input notes/2026-11-13-strong-q126-m32-fixed-view-r1.json.gz \
  --source-topic SOURCES/topics/visible-flexible-closed-surface \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --out WORK/radial-thread-check.json
```

对后续实际入口启用：

```bash
python computations/root_20261114_threaded_entry.py \
  --radial-workers 4 --parallel-run-record WORK/parallel-record.json \
  --target-entry computations/strong_20261114_loop_actual_bvp.py \
  ORIGINAL_ARGUMENTS
```

工作目录为本课题目录；这些占位目录需用实际恢复路径替换。run-record不是BVP成功声明，是否得到新解仍读原入口的完整结果。
