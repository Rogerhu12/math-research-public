# R672 完整曲率覆盖的同场续接入口

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / geometry_path。

## 1. 结论与范围

新增独立调度源 [actions_resume_closed_curvature.py](../scripts/resume_20261120/actions_resume_closed_curvature.py)，
完整源 SHA256：

`f47610f9c43e7c2016fe9d2f93e7e86172da9f7994f8ee901f74a495665f33cd`。

它只调度、保存和复用实际已返回的完整胞界；每个新科学调用仍直接调用冻结
`actions_closed_curvature.py` 的 `CurvatureReader.cell(cell, radial)`。
该数学核 SHA256 为
`8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385`，
其完整场上下文仍为冻结 R670 源 `actions_closed_postprocess.py`，SHA256
`eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599`。

源已经静态阅读并通过 `py_compile`。本说明没有新候选数值、没有科学执行、
没有改动 worker03 的已启动源或队列，也没有对未来作业作运行时间承诺。

本入口只支持原来的多项式 lift；非零 R671 参考尾明确拒绝。整个真实原域仍为
当前符号节点定义的全部 $J-1$ 个原胞，当前运行的 923 节点对应 922 胞。
每胞保留其全部真实 lift 分片、完整原 Fourier 系数、解析 Laurent/Taylor
余项和实际欧氏第一、第二基本形式。没有用采样 $a(s)$ 归一化曲率。
上片的界通过既有镜像与相位等距作用覆盖另一活动片；平帽曲率为零。
非平面、嵌入、reach、统一度量误差及课题完成均不由这个调度器单独认证。

`--target 8.1` 是本次连续曲率细化目标，不是 README 的完整完成标准。
即使每胞都具有有限曲率上界，若某些上界仍大于目标，报告仍明确
`target_certified=false`。

## 2. 原版的实际 checkpoint 能力与缺口

冻结 8ca 源在内存中逐胞追加 `attempts`，并取每胞已付曲率界的最小值。
它每返回 32 个完整胞，或该层当前 pending 全部返回时，将完整 JSON 通过
临时文件加原子 rename 写到 `--out`。这是真实可消费的同场证据。

原版没有 `--resume` 或 seed 导入参数；已有输出会被拒绝。
`--cells` 可以指定子集，但不能导入此前曲率界。其
`--first-geometry-report` 仅复用同候选的 $E$、$|F_\phi\times F_s|^2$
下界，并不是曲率续跑接口。

原版中途文件的 `complete_scope`、`continuous_curvature_upper` 等最终标志
在循环自然结束前仍可能保持初始值。因此判断一个实际中途文件已付了什么，
必须核其 `attempts`、`best` 和 `covered_original_cells`，不能把中途的
`complete_scope=false` 解释成所有已返胞都没有结论。

原版的定期写盘也意味着，进程若在两个 checkpoint 之间被外部终止，最多有
31 个已经在内存返回、但尚未写盘的胞，以及一个正在计算的胞，无法凭该
checkpoint 恢复。它们没有可恢复的实际证据，不能填成零，也不能把未知
成本说成零。本新入口不修改这段已启动程序。

当前 followup 控制器在子进程自然退出后才读取该步骤的 summary；子进程
运行期间的规则同步不会自动读取 R672 的中间文件。工作流硬时限也不会因
普通的本地原子 checkpoint 而自动延长。因此，本入口解决同 runner 的
精确逐胞续接，不声称已经解决硬时限前的跨 job 持久交接。

## 3. 实际证据绑定

初始读入当前 bundle 与 node report 时，记录其真实 SHA256，并核对 $J,M$、
终点与半径载体，以及原符号标量身份。完整 field binding 还包含四个实际
数学依赖的 SHA256：

| 角色 | 源文件 |
| --- | --- |
| 原完整几何 | `scripts/resume_20261120/fullclosed_geometry_interval.py` |
| 向外 IEEE 运算 | `scripts/parallel_20261117_arclength_interval_positive.py` |
| 同一准确径向场 | `scripts/resume_20261120/fullclosed_C0_difference_interval.py` |
| 完整 Laurent 角核 | `scripts/resume_20261120/fullclosed_C1_support_transfer.py` |

这些依赖由冻结 R670 上下文按其既有固定源 SHA 检查。可选 first geometry
必须是同一实际 bundle/node、全部原胞完整覆盖的 eaa 报告；它的实际文件
SHA 进入 binding。导入旧 8ca 结果时，保留同一个 first 报告绑定和同一个
Taylor 阶数；不把换候选、换 source、换模型或换 first 报告的结果混进来。

`--seed-report` 可重复，接受实际 8ca 中途或自然终态报告。读取时对同一份
字节计算 SHA，并先在 runner 保存不可变 snapshot，避免以后原报告被原子
更新而改变已引用证据。导入器逐条核验：

- 实际执行来自授权公共仓库 Actions，producer 确为 8ca；
- bundle、node、数学依赖、标量身份与当前 binding 相同；
- 实际 `selected_cells`、每条原 `level`、$Q/r/L$ 和 Taylor 阶数一致；
- 每条是完整原胞、完整模态和完整解析尾的向外界；
- 只有 `curvature_bound_certified=true`、未付浸入盒为零、$E$ 与法向平方
  下界严格正的条目可贡献曲率上界；
- 由实际 `attempts` 重建的逐胞最小界必须与该旧报告的 `best` 和
  `covered_original_cells` 一致。

原 8ca JSON 没有单独记录 beta 参数，本入口如实注明此点，不虚构其值。
beta 只参与 R670 支持向量相关量，未进入本 R672 欧氏形算子核；新调用仍
明确记录 `--beta`。旧执行命令中已经登记的参数也继续保留在原记录中。

如果重新生成 bundle 使 SHA 改变，即使文件名、参数或浮点读数很接近，
本接口也不会复用旧曲率结论。需要新的同场身份依据或独立转移证明。

## 4. 调度、原子返回与 resume

调度分成两个有次序的 pass。

1. 按声明的有限层级，先处理当前没有严格完整胞界的原胞。
2. 覆盖 pass 结束后，仅处理仍未覆盖或已有严格上界大于目标的胞。

同一胞、同一 $Q/r/L$ 和 Taylor 阶数已实际返回过，就不会在普通续跑中
再次调用。`radial_block` 是内存分组参数，不被冒称一个新数学覆盖层。
未付浸入的实际返回也被登记；它不提供曲率上界，但不会被隐式原参数重跑。
某个已失败的相同调用同样不自动重试，后继须显式提供新的配置。
尚无 durable 返回的中断调用保持未返回，可在恢复时重新支付该未付工作。

每个新完整胞的返回先写到默认目录
`<out 的 stem>-cells/return-<序号>-cell-<编号>.json`，再原子更新主报告。
原始返回含实际 producer SHA、冻结 kernel SHA、同场 binding、完整实际
配置、Actions 身份、完整 kernel 记录和实测耗时。旧 checkpoint snapshot
也留在该目录。主报告和 immutable raw 都被要求位于仓库外。

调用开始前，主报告记录 planned raw 路径和 `running` 状态。如果 raw 已
写完而主报告更新未完成，`--resume` 会验证该完整 raw，并恢复这条返回。
若 raw 不存在，则该调用仍为未返回；不推断上界，不假设零计算成本。
报告的已知 invocation wall time 与原调用登记仍保留。

`--resume` 只接受本新 producer 的同场报告及其实际 raw 文件，重新读
raw、重核 SHA 并重建 best，不盲信上次汇总的上界。它允许下一次 invocation
声明新的层级或目标，但原胞界仍按实际配置保留。旧 source 参数、执行身份、
父报告实际 SHA 和每条返回的实际耗时均保留，新的 `seconds` 只描述本次
invocation，不把重用的既付计算重新计成新运行。若手动导入相互重叠的多个
旧 snapshot，不能简单相加它们的整报告 elapsed time 充作独立总成本。

`--budget-seconds` 默认为 0，表示无 admission 时限。设为正数时：

- 到预算后停止接纳新的 reader setup 或完整胞调用；
- 已开始的完整胞自然返回并原子保存后才退出；
- 不为正常预算触发 SIGINT，不留下无人观察的子任务；
- 返回 `state=budget_checkpoint`，不是声称课题完成。

外部强杀或 Actions 硬上限仍可能中断当前胞或元数据写盘。源只恢复实际
保留下来的证据；不把操作系统级持久性或跨 job 可见性假装已经得到保证。

## 5. 汇总规则与短证明

令 $V$ 为已经拥有严格完整上界的胞集合，$u_i$ 为本次导入与新返回中
该胞所有有效上界的最小值。因为每条界覆盖同一真实完整胞，

$$
\sup_{C_i}|\kappa|\leq u_i\qquad(i\in V)
$$

仍成立。重用或取更小界不会改变场、原域、角频或物理分片。
当前已覆盖域的统一上界为 $U_V=\max_{i\in V}u_i$。
只有 $V=\{0,\ldots,J-2\}$ 时，才输出全原域
`continuous_curvature_upper=U_V`。否则全域字段为 null，
`covered_scope_curvature_upper` 只指明已返回的严格覆盖域。

令 $P=\{i\in V:u_i\leq81/10\}$。只有 $P$ 为全部原胞，才声明
`target_certified=true`。没有有效界的胞、已返回但未付浸入的胞、正在运行
或未返回的胞都保持显式未付。上述汇总在每胞返回后立即重建，不等待整层
或全部层级自然结束。

同样保留每个实际 best 记录的正第一形式下界。全原胞皆付则原活动片
严格浸入。最后 cuff 胞若有法向平方下界 $w_*>0$，利用原准确端口

$$
|F_\phi\times F_s|^2=R^2\rho^2
$$

得到 $|\rho|\geq\sqrt{w_*}/R_+$。连续性与 $\rho$ 的均值 1 再给
$\rho>0$。新汇总用纯有理的 dyadic 向下平方根计算这一较保守下界，
不调用新的几何读数；它不冒用原版仅在内存中的另一份 rho 下界。

平帽曲率为零，镜像/相位保持绝对主曲率。若同一实际模型还满足原
$H>1$、$R>9/20$ 的 marker 前提，报告给条件式
`max(U_V,5)`；其完整 marker 嵌入、支持、距离与 reach 仍须由几何
合并器逐项消费，不能从一个曲率字段推得。

## 6. 完整候选命令，尚未执行或排队

`REPO` 是本次固定 source checkout，`WORK` 是实际 runner 工作目录。
所有下面的文件必须来自当前同一真实场；路径只是 worker03 现有约定。
已刊完整源在 `REPO` 内，旧 8ca checkpoint、bundle 和 node/first 报告
来自该 runner 实际先前返回，不从旧候选的历史数值文件伪装生成。

首次导入实际旧 checkpoint：

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_resume_closed_curvature.py" \
  --repo "$REPO" --work "$WORK" \
  --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --carrier "$WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --manifest "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses.json" \
  --first-geometry-report "$WORK/postprocess/continue-direct-first-geometry.json" \
  --seed-report "$WORK/postprocess/continue-full-curvature.json" \
  --levels 256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96 \
  --target 81/10 --beta 1/4 --taylor-degree 12 --radial-block 4 \
  --budget-seconds 1800 \
  --out "$WORK/postprocess/continue-full-curvature-resume.json"
```

同 runner 的精确 journal 恢复：

```bash
python "$REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_resume_closed_curvature.py" \
  --repo "$REPO" --work "$WORK" \
  --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --carrier "$WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --manifest "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses.json" \
  --first-geometry-report "$WORK/postprocess/continue-direct-first-geometry.json" \
  --resume "$WORK/postprocess/continue-full-curvature-resume.json" \
  --levels 256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96 \
  --target 81/10 --beta 1/4 --taylor-degree 12 --radial-block 4 \
  --budget-seconds 1800 \
  --out "$WORK/postprocess/continue-full-curvature-resume.json"
```

这里的 1800 秒只是示范性的明确 admission 预算，不是旧执行参数，也没有
假定某一胞必能在该时间内返回。若原计划全部已尝试但目标未付，报告为
`plan_exhausted`；后继可根据实际瓶颈显式给出更高层级，不隐式追加无限
计算。异常为 `failed` 并退出非零，实际原始返回与失败日志保留。

主报告可直接供未来控制器提取的标量包括 `state`、`valid_cell_count`、
`expected_cell_count`、`target_paid_cell_count`、`uncovered_cell_count`、
`remaining_target_count`、`covered_scope_curvature_upper`、`complete_scope`、
`continuous_curvature_upper`、`target_certified`、`new_core_rho_lower`、
`conditional_four_p4_marker_curvature_upper`、`seconds` 和 `peak_rss_kib`。
每胞返回及预算/自然退出会打印一条紧凑 JSON；它们不是逐胞 raw 的公开副本。

本源 producer SHA 是新的 f476，不是 8ca。完整消费者若尚仅接受 8ca，必须
另加诚实的新 producer 分支并绑定 `kernel_source_sha256=8ca...`、实际输入
和完整范围；不能把新汇总的 `source_sha256` 伪写成 8ca 以绕过身份检查。

## 7. 跨 job 紧凑交接：仅设计，尚未作为输入实现

逐胞 raw、attempts、tail 诊断和数组只留 runner。未来硬时限前的公开交接
可保存一份有语义的紧凑证明摘要，而不是逐胞数值报告：

- 实际 producer/kernel/first、bundle/node/标量输入 SHA，及读取同一份
  checkpoint 字节所得的实际 SHA；
- $V$、$P$、未覆盖集合与 $V\setminus P$ 的区间编码；
- $U_V=\max_{i\in V}u_i$、$U_P=\max_{i\in P}u_i$ 等少量统一上界，必要时
  同域第一形式统一下界与 cuff 单独下界；
- 每个已用配置的实际已返回胞集合区间，避免后继把已返回但未通过的同配置
  当成从未尝试；实际返回次数、已知耗时和未返回范围。

这些集合是覆盖责任，统一上界只作用于其声明的域。它们不含逐胞曲率值或
完整 raw。后继在完全相同场身份下，可跳过已经达标的 $P$，只支付其余域。
对旧有效域 $V$ 的未细化部分仍使用旧 $U_V$；对新细化子域使用新统一界，
分域取最大值即可得到保守的合并结论。这样可能比保存全部逐胞最小值更松，
但无需重复已经登记的 $P$ 域结论。

例如旧未覆盖域不空时，即使 $U_P\leq8.1$，全域上界仍不能输出为 $U_P$。
必须等到补域有真实返回并形成完整域覆盖，才能合并全域结论。

本新入口的 `coverage_summary` 给出了上述集合区间和明确的
`compact_cross_job_resume_implemented=false`；它目前只接受实际 raw journal
恢复，**不接受紧凑摘要作为证据输入**。紧凑摘要的冻结 producer/consumer、
作业结束前真实发布与下一个 job 的实际同场输入材料化，均需父代理后续
明确接线。它不由这个源码草稿自动成立，也不构成对当前 worker03 的变更。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
