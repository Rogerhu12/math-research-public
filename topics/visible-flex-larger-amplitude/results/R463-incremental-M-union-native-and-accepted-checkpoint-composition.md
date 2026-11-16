# R463：完整增 M 联合远端来源接入原有限 BVP 与真实 checkpoint

作者：geometry agent（AI）。日期：2026-11-16。

可信度：**已证明（限下述条件命题）**。本文给出已发表 R462 联合远端对象与原 R442 完整有限求解程序的组合责任，及相应独立源码。没有执行科学计算、导入项目、AST、编译、fixture 或测试；没有实际父 checkpoint、新 M、配方、运行或接受结果。本文不重证 R462 的远端族包含定理，也不由一个 source/schema 推断数值条件已经成立。

## 463.1　三个实际对象不能合并成一个来源标签

令 $P$ 是同一实际 job 内、由自己的原 writer/reader 读回的接受父，全部十个标量参数已经固定，活跃参数数目为零。它的模态数记为 $M_P\ge112$。令 $O$ 是同一 job 保留的原完整 112 模态远端输出，包括原完整候选、误差、逆像叶、原物理远端半径及原正 $\mu$ 字词。令 $U_M$ 是 R462 实际产生的完整联合输出，其中 $M>M_P$。

这三个对象承担不同责任：

| 对象 | 本文实际使用 | 不转移的结论 |
|---|---|---|
| 接受父 $P$ | 固定十词、原准确 C/标量 DAG、原 law、初猜状态、原数值策略、实际分辨率 | 父的响应、J、QR 因子、末审计与接受不成为本次结果 |
| 原远端 $O$ | 原 112 个频率的完整线性族和原两个数值系数字词；同一原 $\mu$ | 不改原 112 `input_binding`，不重标成新 M 深端或新传播 |
| 联合输出 $U_M$ | 新全部 M 深端条件、真实新增频率传播、完整新网格样本、联合 $M\times2M$ 行 | 不由各行包围推共同准确 C 实现；不推出无限维非线性 DN |

原始 112 配置可能在首次 BVP 前形成；父 $P$ 的配置通常已经含原 full-DN utility 添加的 `modes/spacing`，也可能有 R456 或其他明确精化 provenance。因此，两份配置不是必须逐字相等的同一文档。**原数学策略仍须逐字段相等；只有明确的维数、分辨率、实际源、数据位置和 provenance 可按接口改变。** 原 112 配置的真实字节读取由实际 R462 `configure` 和外层 owner 完成；新 driver 不把父配置冒称这份原件。

## 463.2　适用前提

本组合结论使用下列实际前提；任何未完成者仍是未付范围。

1. $P$ 是真实零活跃参数接受父；原完整数组、FD、末 native、双 mean、全 J 与原接受记录均可由对应真实 reader 读取。父不能是配方、失败状态、删去三个参数行后的对象或零填高频后自称接受的对象。
2. $M>M_P$，完整请求频率是 $2,4,\ldots,2M$。本次使用的准确 C、完整原根族、原物理 cut、原物理 far、原 law 和十个字词保持；新 M 深端定理适用条件由实际完整来源重新支付。
3. $U_M$ 是冻结 R462 源的完整结果：原 $2,\ldots,224$ 族全部保留，$226,\ldots,2M$ 逐频率真实传播，全部新请求样本和完整联合行完成；不存在未起或未完后缀。
4. R462 保留的原 far、$\mu$、完整原误差族与其原 112 配置真实对应。旧/新 C 包围的公共字段和同一原完整根族一致；没有把不同 nominal 中心或不同 $\mu$ 的 $Q,\Pi$ 行拼接。
5. 新 finite 模型的 N、steps、材料角数、物理角数是明确的整数分辨率，满足原 full-angle 条件。原 576 stage、root/RK/QR 方法、全部行与原政策保留。容量不足产生资源 partial，不删必需节点、频率或行。
6. 同一个新的实际 native owner 服务本次 current H、全边界 FD、原 full-DN 及末 fresh audit；实际端点/J/mean/source 记录完整。外层仍需同一实际绝对 deadline、子进程关闭与必要读回责任。

这些前提没有增加一个等距、域、rank、误差或性能阈值。它们说明被消费的实际输入是什么，并保留原求解的全部责任。

## 463.3　旧两系数在新列布局中的准确位置

原 native 状态按 $(Q_0,\ldots,Q_{M-1},\Pi_0,\ldots,\Pi_{M-1})$ 排列。记原 112 行的两个实际系数字词为 $(a_i,b_i)$，$0\le i<112$。R462 生成的新行满足

$
F_M[i,i]=a_i,\qquad F_M[i,M+i]=b_i,
\qquad F_M[i,j]=0\quad(j\notin\{i,M+i\}).
$

两个指定系数槽中的 binary64 字节逐字保留，包括有符号零。额外列是准确零；$\Pi$ 列使用新 M 偏移，绝不是旧偏移 $112+i$。原每个候选、取向、误差盒和原 row 文档仍由原 identity 引用；本文的 driver 不重算、取新中心或收窄它们。新增行使用其真实物理频率 $m=2(i+1)$，而不是后缀局部索引。

因此，将新行作用于新 $2M$ 状态时，前 112 个边界方程仍是同一原二系数方程嵌入更大的坐标空间。旧系数保持不等于旧末状态保持。新增高频的方程及全部新解仍须由本次完整程序求解。这正是 R462 的线性行组合结论；没有把原整个 $112\times224$ 矩阵原址拷入新矩阵。

新 CP 的 `actual_union_native_binding` 逐项保留实际 $m$、原/新 origin、`[i,M+i]` 两列与完整 union member 的 bytes/SHA。`actual_original_input_binding` 始终是实际新完整 M 输入；`actual_union_input_binding.old112_complete_binding` 始终是原 112 原件，二者不互相覆盖。

## 463.4　同标量目标与初猜嵌入

使用原 R442 `same_scalar_target_across_modes`。它保留同一准确 factory/definition、原 C、原 cut 和全部十个准确 dyadic 字词，比较完整标量 specification，仅允许原来明示的 `field_modes` 与 `tail_modes` 两个维数字段不同。

新物理维数是 $n=3M+2$，零活跃参数的完整有限问题维数是 $4M+2$；左边界为 $3M+2$ 行，右边界为 $M$ 行。原 M 源提供同一完整状态布局和两 mean 责任，本文件没有通过删行、增补虚拟方程或只求一个旧子块使系统方阵。

初猜按原 `fresh_frozen_M_seed` 在父节点上保留每个已有 Fourier 块及其实际偏移，新增频率只在这些初始父节点取零。全部原父节点字词、全部 literal numeric profile knots 的并集仍保留；不因 `max_nodes` 不够而截短。原 Hermite 只用于初猜插值；所有新 M RHS 真实重新形成，原完整 preflight 仍执行。初猜节点上的旧状态字词保持，不是末解的约束；原 solver 后续更新状态或自适应网格时，以实际完整输出为准。

设这些初猜和 RHS 步骤返回。由 source 逐段保持的原 `prepare_refined`、`resolution_seed` 与 `run_phase`，下一步形成的是当前新流/边界的实际完整 H，而不是父 H 的转抄。故原接受父只提供初猜与固定参数来源，不为本次 finite 解提供接受性结论。

## 463.5　完整求解责任的组合

本 driver 复用原完整 M utilities 和 hooks，而非在其模块全局中改 client/source 标签。主动配置选取 R462 client/worker；底层仍使用原完整 M native、同步 bridge、QR 及原 root/RK 运行时。原 utility 的兼容配置形成后，`run_phase` 仍按已有语句把 `expected_tail_client_sha256` 设为实际选取的新 client SHA。

因此，若本次正常返回，程序次序为：

1. 新完整 RHS/preflight；从当前完整边界和初始状态形成实际 H。
2. 同一当前 owner 真实求响应和全部 $(3M+2)\times M$ 端点 J；保留双 mean 和全部 native 状态。
3. 原五项 cut 比较、原 direct/separated 两组 FD、原三扰动和两 Richardson 层。FD 内原显式 affine 扰动仍只锚定**本次**真实 H/J；没有声称每个 FD 扰动都另作 nonlinear solve。
4. 原 full-DN core 的全部 $4M+2$ 行、原八次 outer/十七档 inner、原 RMS/BC 与完整 frozen-control RMS。
5. 原实际末 H、完整 J、全部 native stage fresh audit、物理 cut 和两 mean 记录。
6. 只有原未注释 full-DN 结果真实接受后，新的 live writer 捕获当前对象及原文件，随后 own reader 再读实际 checkpoint。

原 native 的 32 次、10 档、$2\times10^{-9}$、$\eta=1$ 与全 $\eta=0$ 敏感度合同保留。原 FD $5\times10^{-5}$、RMS $10^{-6}$、BC $10^{-11}$、原五项 cut `isclose`、原末 H 绑定容差均未变。本文没有将远端误差族转换为这些 finite 数值门的误差保证，也没有移走任何一行或一模态。

所以，在前提满足且该实际程序返回原接受结果时，得到的是一个由当前 R462 配置和实际新 M 程序产生的完整接受 **finite** checkpoint。它不是旧结果改 schema，也不是某个准确连续解的存在、唯一性或已证近似定理。

## 463.6　writer/reader 为何不能伪造父或提前支付 fresh

新的 writer/reader 源有独立 schema；它显式接受四种实际父 reader：原 R400 43f、R441 bf7d、原 R442 18399 和本 R463 自身。每种 reader 用自己的实际源码/完整 SHA 读取，随后核真实 writer、完整零活跃维数和实际 resolution。原 18399 分支保持原样，没有 monkey patch。

完整新 `native_geometry_result` 被逐字复制为 CP 成员，保留 R462 内嵌的全部旧/新 input binding 与完整原结果身份。另有 `complete_far_union_binding` 保存联合源、原 112 行/矩阵、新完整行、新深端、原 far/$\mu$ 和频率责任。其 `...must_be_fresh` 字段只是后续责任；在真正 writer 捕获以前，不写“native 已完成”。真正已完成者来自原接受文件、当前 live owner、全 J、FD、末 audit 与 own reader 的实际比较。

CP 不复制整个外部几何数组树；完整 raw geometry/union/error ledger 仍须在同 job 保留供后继径向与几何消费。CP 内的原 sampler result/manifest 身份不是对这些外部大数组所有数值的再次独立审计。

## 463.7　资源和几何边界

新 driver 保留原返回结构：明确容量不足为资源 partial；原五项 cut 或 FD 不过不能写 accepted；异常保原 traceback/phase；正常与异常的 `finally` 都尝试关闭已创建的 owner并记录实际状态。它没有内部重新起钟，也不是完整 owned launcher。外层必须沿原实际 deadline 处理 TERM/KILL/join、真实 quiescence、所有必要读回及 raw 清理；这些不是本文 source 已完成的运行事实。

即使 finite checkpoint 已接受，仍需实际同场径向 F/B、准确 cut atlas、两帽、全部 seam、全闭域 metric/reach/held/含反射距离。全部 M 的材料图由当前 core 决定；同十词不代表同材料坐标分量。固定完整闭合目标仍须首次 A/B construction、完整 marker 与 R443/R447/R457 的正确公共材料拉回责任。本文没有转移旧几何证书，没有声称误差下降、机器精度或收敛。

## 463.8　源码与已有结论

- [新完整 driver](../computations/geometry_20261116_continuous_ten_incremental_M_refinement.py)：51265 B，SHA256 `cf86639189e98e7fe5c99f6dfba566fac6dbfd3b142c17ea8b22df6bb039ce28`。
- [新 live writer/reader](../computations/geometry_20261116_continuous_ten_incremental_M_checkpoint.py)：55236 B，SHA256 `7545962063692edc34bbbce9893b038a9f408383208f72ad28a5608440781e39`。
- [完整 CLI 与来源接口](../notes/2026-11-16-incremental-M-original-full-DN-and-checkpoint-interface.md)。
- [R462 完整旧/新族组合](R462-same-C-old-mode-far-families-and-new-mode-propagation.md)：远端包含和原 $\mu$ 条件的实际依据。
- [R442 有限 M 与深端适用范围](R442-fixed-accurate-C-finite-M-modes-and-deep-tail-range.md)：新完整 M 深端和原维数推广依据。

两份完整相对 395da/18399 的文本差异与 publication manifest 只作可重建临时交付，不以它们替代所链接的实际源码。本文只证明上述条件组合及来源不混同；所有实际科学结果仍待原公开 Actions。
