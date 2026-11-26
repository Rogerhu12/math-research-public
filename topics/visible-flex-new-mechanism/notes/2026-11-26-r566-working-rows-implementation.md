# B030 工作行后端：完整物理约束保留，局部 Jacobian 限制到真实径向子集

日期：2026-11-26。会话：Astra-new-mechanism-0105020f-20261126。

## 1. 为什么这次换后端

最近的 [run 45819650602](https://github.com/Rogerhu12/math-research-public/actions/runs/45819650602)，job 139908280075，在完整 START 后由 runner 终止，没有新完整 callback、FINAL 或 backend return。原因未知；本包不把它断言为 OOM。实际 START 已采用全部 571 个径向节点、1276 个实际峰值轨道；q 是此前完整 callback 的同一 81 个系数，trust=1.20135498046875，尚无可以推断的新 trust 适配。完整 1144×3072 观察加 1116 个已定位角括号给 eta=0.25895160785933824，真实几何缺陷观察为零。

原 CombinedRows 在全部 571×1536 均匀约束与全部实际峰点上形成约 190 万行、82 列的稠密 Jacobian。新包改变局部优化所用的矩阵表示：只对当前实际证据选出的 field/orbit 行形成导数，同时所有完整约束仍决定每次候选能否接受。它不是减少原物理问题或删去未选中的约束。

本包只续 B030。B038 不在 scope。

## 2. 原输入、完整 START 与费用身份

输入保留前一 generic request 的完整 source_state_json 原文本（143976 B，SHA256 `0f22f75b4ac02c3e6c286b894b310c85bc61f3959ca4476397fc487fc59262ba`），继续使用原 source loader 的源提交 Git object、物理参数、q、原实际/待采纳坐标和 trust 核对。随后加入最近 run 的 START 小标题数据；其中 q 和坐标不重复存两份，而是由已验证的原 callback 与完整待采纳提案重建。

重建的全部 START 必须逐字满足：

- 原提交 `b8fd978de20dfdc9f4921c4c9168fb77f6afc6c1`。
- 实际执行 wrapper SHA256 `cc1a1fa3fdca03d1b15fcd2ee6151133a64ab64a571f20990c1f029d5babc1b0`，再次从该提交原 Git object 核对。
- 原完整 stdout：576947 B，SHA256 `5cc35960724511c9de99271622d8cdd25e6c8266045d5c39f4ae1f9a00d38afb`。
- 完整 START JSON：74878 B，SHA256 `be0ca792a9dea74b01e50142c400ed40a2a53d33d6268610ca0aeefe37532de4`。
- 原 81q binary64 SHA256 `7e708ba7a973e8505a81e94073707e8c39504d1f3285253f97e3564382992080`。
- 571 径向、1276 峰轨道、1536 FFT 角节点、原 trust、metric 阶段和空新 pending 必须全部一致。

原链已记录科学秒数下界 2853.2676457370003，加最近 START 中已完成且不重计的 localizer 22.603199331 s，得到 2875.8708450680003 s。它不是总费用。此前两段 46.3705572 / 27.382752 s 的截断 wall 区间、最近 START 至外部 shutdown 的 68.2931574 s，以及最近 START 前未闭合的程序工作都明确保留为未知或 wall 记录，不能再次当作精确科学秒数相加。没有虚构外部中止后未知 trial、pending 或 Jacobian 计数。

源输入经已有 stdin runner 传输，完整 SHA256 核对；没有长 argv 限制或新的临时科学文件。

## 3. 子径向模型与工作行的准确含义

当前候选物理参数、源模型、角 FFT/原语、全平尾、参数边界均未改。特别是 B030 的 p=.85、q=.15、offset=.15、ball=1.012、原 strip/reach 联合预算、mean_E_floor=.25、det_floor=.1、geometry margin=.001、feasibility tolerance=1e-8 保留。

每个工作行记录 field、实际径向节点以及原均匀角索引或原实际角 theta。均匀行使用原数组里的四个角索引值，不能用浮点 theta±pi 重新制造近邻角；实际峰使用原四轨道定义。每行仍取完整四轨道的最小值，AD 对同一个实际 argmin 取列。Phase I 的共同 sigma 在选 argmin 后相加，保持原次序。

同一真实工作 s 所需的行合并处理，每批最多 24 个工作 s，再补 0、L 及构造器所需的至少五圈。所有实际工作 s 受保护；近邻 filler 不能替换它。原 full pointset 将已记录峰映到保留径向节点（允许差至 1e-12）的既有规则也保持：工作行明确使用同一个全网实际节点，原峰 s 另存为证据；不产生新的径向插值或独立近似。

对每个子径向模型，每一圈仍计算全部 1536 个 FFT 节点。位置、空间一二 jets、角原语、诱导 E/F、曲率和真实 mean E 的公式均复用原 AngularOracle。mean E 始终为同圈完整 1536 点均值；绝不改成工作角点均值。原模型的径向基、背景高度和空间 jets 在各 s 求值，角积分与 mean E 都逐圈进行，因此限制要计算哪些 s 不改变所选行的数学值或参数导数。

导数按原 16 方向分块，每个子径向批分别播种完整 81 参数中的相应列，再写回该批实际 field/orbit 行。最后额外列仅对 sigma 或 metric epigraph t 取 1。每块 AD 都重构相同工作行值，超过 1e-12 相对尺度的差异会明确退出，不能静默使用错误列。原全部物理行的稠密 Jacobian 不再构造。

## 4. 工作行的选取与完整接受门

首次新全粗网值读取用于确定这套新局部矩阵的实际证据，不复跑旧已完成的初始 fine/localizer。对每个 field，均匀网选径向局部低值及全局最坏值，实际峰库选当前最坏值；每组最多六个证据行。mean E 的 nr×1 行单独处理，不误用角轨道的 nr×(nt/4+1) 索引。

工作矩阵最多 512 行，这只限制局部矩阵大小。全部 571 圈×1536 旧均匀不等式和全部 1276 个四轨道约束一直作为完整必要条件；新的已观察违约坐标也全部进入 physical pending。新增径向点只追加到全部原 actual 节点的受保护集合，距离任何已有点不超过原 1e-12 容差的新点按原 pointset 规则映到保留节点；不能用近邻新点替换原 571 个浮点坐标。细网构造也保护全部实际粗网节点。工作矩阵只从这些实际证据中取有限行。达到工作矩阵容量时保留完整提案并诚实退出该 scope，不把未选行删掉。

每个 callback 的次序：

1. 先读工作行。工作行仍不满足的内部 SLSQP 迭代不接受；它不是实际已接受状态。
2. 工作行满足时，读取全部实际粗网/峰库值。任何遗漏到工作矩阵之外的必要行违规，都拒绝此候选；从真实负行中选证据加入工作矩阵，重新开始局部 backend。完整最小值先计算、后选证据，未选中的违规不能藏在选取预算之外。
3. 粗网全部通过后，才执行完整细网：全部实际径向节点、所有相邻中点与原 97 点背景网合并，完整 3072 角。比较同 q 的 coarse/fine e、f、相对 mean E 与 tau×curvature，原阈值 1e-7。
4. 使用原 a879 完整实际角 localizer：所有观察到的括号按每批 512 处理，绝无总候选截断。未完成或 unresolved 的定位不能接受。
5. 对真实 fine 网和完成的实际峰，要求同一 geometry margin 和 sigma/t epigraph 均满足 1e-8。这里明确收紧旧 callback 只用未加 margin 物理几何作最终接受的情形：新工作后端不允许候选靠遗漏的 fine 硬行或低估的 t 获得接受。所有实际违约坐标进入完整物理提案；仅其每 field 最坏六个作为下一小矩阵的证据，剩余仍约束接受。
6. 在上述完整门通过之后，Phase II 才按真实完整 eta 比实际保留态严格改善 1e-12 接受；Phase I 按完整 margin 缺陷改善 1e-10，或真正恢复至 tolerance 接受。原未加 margin 的实际物理几何资格也保留。

SLSQP 内部 candidate、最后自然返回值和实际保留 q 是三个明确状态。只有第六步可以改变保留 q。新增约束或工作行的提案不会凭空成为已优化输入。下一 outer 明确采纳后再构造相应模型。

## 5. 新限制映射的一次必要观察

同一公开 run 内，在实际新工作行上做一次限制映射观察：

- 以完整 571 圈模型的真实点求值对比子径向行值；
- 子径向 AD 的一个确定方向，对比完整模型同一方向正负 1e-6 参数差分；
- 两边角 FFT 都为 1536，mean E 都保持完整圈；
- value 最大差阈值 1e-9，方向相对 L2 阈值 3e-4。

这检验的是新“选哪些径向圈、哪些 field 行、列怎样拼回”的映射，既不重复旧 oracle 的 uniform/非均匀角 parity，也不建立独立科学预检 run。所用工作 Jacobian 可直接留给同一优化器，不为检查另造完整稠密 Jacobian。结果是浮点观察，不能替代连续误差证明。

## 6. 真实状态、trust 与费用

在首次科学工作前、每个已完整处理的 callback、每个 outer 完成以及最终出口，都 flush：

- 实际保留 81q 及 binary64 SHA256；
- 实际保留的完整观察摘要和其网格；
- 当前完整必要径向/峰库；
- 尚未采纳的全部物理峰与工作行；
- 当前工作 field/orbit 行；
- 实际 backend trust、单独的下一 trust 提案以及适配决策是否已完成；
- 最近 trial 的 q、t、已完成/未完成资格与是否接受；
- 自然 backend return（如存在）和它尚不能自动证明的接受身份。

新库采纳后，旧保留 q 的旧资格不会自动被标成新网格资格。完整所选约束、试探是否资格通过和哪个网格给出旧摘要都可见。

trust 规则保留原尺度和区间：仅实际接受步接近原盒边界时放大 1.5；只有 backend 自然结束、没有接受也没有任何待加入约束时才减半；约束交换本身不伪造“失败收缩”。所有实际值均在快照里。达到最小 trust 而无实际改进时退出该 scope，留下完整状态。

每个 oracle 构造/求值/AD/点值的费用计数保留。live oracle 与已退休 oracle 恰好各计一次；正在使用的工作矩阵计数另列，完成或异常退出时才归入累计。因此完整 callback 里既不漏当前成本，也不把同一累计快照重复相加。constructor wall、程序总 elapsed 也记录，未完成操作只能保留实际已有计数与 elapsed，不能编造完成计数。

## 7. 可复现包及范围

- 源：`scripts/r566_working_rows_full_acceptance_20261126.py`。
- 请求：`computations/request-r566-working-rows-20261126.json`。
- 工作流：`.github/workflows/visible-r566-working-rows-20261126.yml`。
- 复用 `run_inverse_state_stdin_20261126.py` 做真实 public/private pull、README 差异检查、QUEUE 会话核对、所有源 SHA 绑定及凭证移除。
- 单公开 job，科学 scope 2400 秒，30 秒 final reserve，job 50 分钟；原 numpy/scipy/Python 和固定 Actions commits 不变。
- 本地仅作源码静态阅读、AST/JSON/哈希、原 stdout 解析和小输入身份整理。没有执行几何模型、优化、科学求积或新数值检查。
- stdout only；无 raw 数组/表格 artifact、Release、Git 或跨运行 cache。

当前仍是静态逆设计，g 随 q 变化。有限角/径向观察、实际峰定位和本次小矩阵选择都不证明连续嵌入、全对 reach、固定 g 精化或 README 完成。新后端的唯一意义是将已完成的大物理问题继续解下去，同时避免把所有约束的导数同时摊成巨大稠密矩阵。
