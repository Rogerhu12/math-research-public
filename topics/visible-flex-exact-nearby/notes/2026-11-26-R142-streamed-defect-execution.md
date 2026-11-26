# R142：真实未成 defect 的完整母格积分接续入口

会话：visible-exact-astra-198c63d-20261126。日期：2026-11-26。

数学依据是 [PS 完整母格源积分证明](../results/R142-supplement-durable-complete-parent-source-moment-prefixes.md) 及其纯模块。这里保存可执行入口和真实准入边界；没有新的数值结果，也没有为仍运行的作业虚构 actual 文件或 manifest。

## 1. 唯一可接受的前件

首次只接受 run 45761859526/1 的完整真实 scientific、execution 和原 manifest。必须是数学子进程已经结束的未成结果，且完整 defect 六球尚未保存：certificate.defect 为 null，四源为空，whole point 未成，旧 completed_targets 为空。科学字段、来源绑定、全部当前输入收据、执行文件收据、原 model/refinement 和有序 gate prefix 都逐项核对。

如果旧结果已有完整 defect，不论严格门通过、失败，或后续四源/point 因时限未成，都拒绝这个入口。那些已成球必须原样消费。旧 packet/cell count、matrix checksum 或仅在内存存在的局部工作不能冒作源积分；原运行中未公开的载体确实无法从这些计数恢复。

后续只接受同一个不可变 owner/helper 产生的完整实际未成结果。可复用内容是 kind=R142_complete_parent_source_integral_prefix_v1 的整份三积分前缀，包含精确母格游标、对应 refined-cell 游标、全输出范围和完整保存球。每一次接续另以真实前件 SHA 定义 consumed marker，仍只有一个科学 child，不自动重试。

## 2. 每个已接受母格覆盖什么

三积分分别支付全径向 body、root97 和 outer96 的完整输出。源变量只在已接受的原母格范围内积分；输出变量从未截到该母格。原同格双三角、独立 even mean、真实长度和全部 193 原子都保留。

当前 owner 只处理 true_coefficient_defect。它先物化 source-independent A/B/K 输出协方差，再按原 155 母格顺序，只对尚未接受的母格调用原 parent provider 的完整 source moments。每个新母格结束后立即保存三项累计上界。原整个 parent 的系数集合和 PSD majorant 保持原定义，不能随 child 免费缩小。

这次调度需要额外的完整 source-independent 输出物化，并可能在下一作业重新物化同一比较 Green、U、A/B/K 和根 carry J。没有预称运行时间更短或 ε 更小。已经接受母格的 V、Z/Y source moments 和三积分贡献不得重新计算。

若 155 个母格的三积分已经完整保存，则无需再物化任何 Green 或输出矩阵：新 owner 只从整份原球读回有向上端，再计算三个平方根，完成六个完整范数球。

## 3. 事务顺序与失败保留

每个母格的新累计值先写到临时 candidate scientific document，再完整读回；检查整份文档相等、每个保存球 contains 原计算值，并绑定完整 source-prefix 语义和游标。通过后才将同一组 bytes 原子替换为正式 output，随后才更新内存中的 accepted cursor。下一数学步骤只使用这个保存读回的上端。

末个 refined cell 已经完成的母格先保存，再执行下一个时间预算检查；被打断的母格没有被计入 accepted count。若在完整母格之间失败，原先正式三积分前缀保留。整个 owner 的异常分支明确 complete=false、proved=false；已保存的六球及 completed_targets 不删除，也不得因此重算。

全 155 母格之后，六个 defect 球也先完整保存和读回，再用实际读回的 body_norm_upper 上端判断 ε<1。前缀只到部分母格时不输出完整 ε，也不宣称 inverse。

## 4. 一个目标与后继边界

唯一 ordered target：

complete_streamed_parent_true_hybrid_low_coefficient_defect

两个严格门分支的 complete_target_counts 都是 [1]。若 ε<1，proved 只表示这个完整低频混合 defect 门所给的 resolvent；四个普通源、193 atoms 的对应源响应和所有半径的 point/transversality 尚须各自后继实际完成。若 ε≥1，完整六球仍是成功完成的上界目标，proved=false；没有推出 BVP 奇异。

本入口没有 58 门的物理整体结论、224 表、32 表、真正负侧 incoming、ν/phase Schur 或非线性闭族结论。旧 R149 对称部方法若要消费这个后继 kind，必须显式绑定这个完整 actual/execution/manifest；不能给旧 R142 actual 换名，也不能把原 ε false 改成 true。

## 5. 源码与现有 worker

- owner：scripts/fourfold_codazzi_low_centre_streamed_defect_owner.py。
- 纯积分接续：scripts/fourfold_codazzi_low_centre_streamed_parent_moments.py。
- metadata generator：scripts/make_low_centre_streamed_defect_manifest.py。
- 原公共 worker：scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py，Git blob 661cc9930e772422e36c16dd9165af8b97d553e4，原样复用。

worker 的 entry role、kind、完整 scientific 字段、有序目标及允许目标数均由 manifest 决定。它允许一目标的 complete/false 分支，不要求 proved=true；完整历史恢复、实际 pull/README 检查、资源/并发容量、marker 和最终整件输出政策保持原实现。

新 generator 从原 77 输入 manifest 原 bytes 出发，加 8 个明确新输入：owner、pure、PS proof、本说明、generator 和三份真实前件。共 85 输入，14 scientific module bindings；旧 77 个 path/bytes/blob/SHA 不变。reviewed rules 继续使用 Nov20 的完整当前收据 SHA256 26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051。

不给三份真实前件，或文件尚未出现时，只输出 metadata readiness，不写执行 manifest/workflow。发现完整旧 defect 时同样不生成。取得实际合法前件后，在仓库根目录用以下参数提供明确新路径：

~~~sh
python topics/visible-flex-exact-nearby/scripts/make_low_centre_streamed_defect_manifest.py \
  --repo . \
  --previous-actual PATH_TO_COMPLETE_ACTUAL_FILE \
  --previous-execution PATH_TO_COMPLETE_EXECUTION_FILE \
  --previous-manifest PATH_TO_ITS_COMPLETE_MANIFEST \
  --manifest-out topics/visible-flex-exact-nearby/notes/NEW_STREAMED_INPUTS.json \
  --workflow-out .github/workflows/NEW_STREAMED_DEFECT.yml
~~~

这里只列调用形式，没有实际实例化文件。后继 workflow 的安装命令用 YAML block scalar；原 320-bit admission、768-bit directed arithmetic、Python 3.12.14、python-flint 0.9.0、原 16800 秒科学预算及公共 worker 20100 秒 child 上限保持。新科学仍只在本公开仓库 Actions 执行。
