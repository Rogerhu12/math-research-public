# λ=.32：真实新接缝 H 保内部初值与原尾接受

**状态：数值证据与真实执行身份；不是连续几何证书。**

原 λ=.32 内解及节点 H 真尾已经接受。其 post-tail 恢复在原 outer 0 得 BC $4.9901870686\times10^{-10}$，保存了完整前缀审计，但物理 quintic 的接缝 H 与原节点 H 有末位差异。原新 H 求解在 iteration 2 以残差 $3.667837241951283\times10^{-9}$ 线搜索失败；这不是同 H 缓存命中，也没有重复已接受 inner。

本条沿用已登记的 [保内部新 H 入口](../scripts/resume_m3/solve_preserved_interior_original_tail.py)，源 SHA `af65f13ceb394589e9578c535ca337ca80b86bcb3bf4291b509af966b785b614`，不再修改算法。输入明确绑定原节点真接受 `5e163453…`、真实接缝失败 `67fc2235…` 和实际恢复计划 `7a261af2…`。它复制整个真接受尾，仅用原 JavaScript `H/rCut**4` 编码新 cut Dirichlet，并把 `cutHeight` 设为实际新 H。

实际 H 差集为分量 0、1、2、3、4、7；经过原除法编码后，完整状态差集恰为 node 0 的分量 0、1、2、3、4。其余全部 $1153\times16$ 状态，包括所有内部/深端与切口动量，逐位保持。`rawStates` 依原 `rawNode` 一致重取，候选仍明确标为未接受；原重加载 ratio=1、边界修补为零。旧/新 H、五个边界差值和完整输入哈希保存在 [紧凑记录](../scripts/resume_m3/trace_path_lam032_seam_preserved_execution.json)。记录中原 accepted 与 iteration-2 failed 状态的差异只是只读比较，不能把迭代后每一差异全归因于初始预测器。

唯一原 worker 随后在 iteration 0 真实接受：

$$
\mathrm{residual}=1.8339186209756414\times10^{-9}<2\times10^{-9}.
$$

完整 208 个有限 Jacobian 元素与有限尾 audit 返回，全部最终状态与候选逐位相同。没有额外 Newton 修正、比例扫描、自动重试或新全 stage 定位。本次也没有运行前缀 BVP、mean-height 积分、prefix audit 或 seam audit。

实际 session **66671**，启动块 `5fb98b`、终态块 `f841c6`；observer 于 **2026-11-18 04:54:52 UTC** 记录 child=0，原 worker=0。真实新 H 尾文件为 `m3_work/trace-path-lam032-seam-preserved-v1/seed_tail_0001.json.gz`，SHA-256：

`cd1f6d4ae2a5a26b3a2d6b96273a87c482df713d9bb2acdd99b9df21539e0eb5`。

该真实响应交给只补缺失 seam 的原后处理；已保存的物理 quintic 与前缀审计保持。原 prefix metric 为 $5.30874420344815\times10^{-4}$，仍高于最终 $10^{-6}$ 门；本条尾接受不代替最终 λ=1 的完整 metric、固定问题收敛、闭合几何或 10% 持握结论。
