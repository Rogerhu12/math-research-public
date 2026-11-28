# RET73：三份旧 finite-mode refinement 输出的完整退存

日期：2026-11-28。仅移除三份生成的有限线性物理 Fourier 诊断，毛计 100378 B。完整来源、原配置文件身份、逐报告全部必要标量、恢复命令和未知项见 [provenance](../computations/legacy-finite-mode-refinement-retention-73-complete-provenance.json)。root 在 fresh HEAD 对照确切 path/blob/bytes 后普通提交；本工作不写 refs 或队列。

## 1. 删除集合和固定恢复

固定恢复提交为 `bdcf84039b32d5c9071cd256fdf9e1635b963a97`。路径均在本课题 notes/ 下，三个完整小正文已读。

| 文件 | B | Git blob | SHA-256 |
| --- | ---: | --- | --- |
| numerical-m2-tail-opt-refine.json | 33429 | 6f4443af872d8897713280849ad9a5ead229cb78 | c4119a6f634790ba1487ca1cb780641886960834bafbd2bfbb132499b66eb385 |
| numerical-m2-tail-smallcut-30-refine.json | 33540 | 03582fa299b17a630dcde955c093be296d86b178 | 392f0346dbc8a244c665582204f023875ed66a96035663cb29902334460e1b02 |
| numerical-m2-tail-smallcut-35-refine.json | 33409 | cba95de450725cf47fd39b69fa27ce2275d63191 | b8387a88efb16cd4909233f76927fbe7ca276683300e7716f382dc80a08cc287 |

没有删除配置、port、原搜索资源、任何 nonlinear 状态、保存场、证明或科学源。RET42 曾将这三份后续诊断列为当时保留记录；其完整账本继续保留。本批为这三份明确增加新固定 Git 恢复合同，不改写 RET42 原始时点的描述。

## 2. 完整生成器和源闭包

实际完整生成接口是外部课题的：

`topics/visible-flexible-closed-surface/scripts/closing_weighted_modes_diagnostic.mjs`

完整 1169 B，SHA-256 `975e2bbeed7b01e3b878e96df4da53a2114c6c0ae81de7afceca0803d4a00705`，Git blob `4ed9dec7103fd8bdcdd119c486166aee388ef513`。

它读取整个 input JSON，取 `raw.config ?? raw`，调用 weighted 的完整 createRecalibrationFactory 与 assemble，再将全部 mode 列表逐项交给 diagnosePhysicalMode，累积完整 rows 并写 output。三个原报告的 positiveWarpWeights 及输入配置对应 weighted 构造，不能替成相似名称的 unweighted 入口。

本批登记完整 13 源：这个入口、weighted、recalibrated、loader 及 loader 所验证的九个原始模块。原 loader 先看相邻课题目录，再看 CLOSING_TAIL_CACHE；它实际检查九个 Git blob。恢复时须保持这个查找次序的责任，不能让不匹配的邻目录遮盖正确 cache。原 balanced/rejoin/smooth/momentum/raw-Cauchy 导入在完整九文件集合内闭合；这些真实代码保留所有默认值、原校准积分、有限 RK、全部原径向记录与形式二阶几何公式。

该调用没有读取旧 nonlinear response、未知 scratch 或另一个被删的诊断报告。前期优化搜索不是重算这些固定配置诊断所需的输入；完整搜索资源与结论仍由已刊 RET42 保存。

## 3. 完整参数不从文件名猜测

三份原报告 config 与现保留的以下完整配置 JSON 逐对象严格相等：

- opt：`computations/numerical-m2-tail-opt-config.json`，1753 B，SHA `7a2faae86b82c5fad27c112a5ee3d6489790e9c08d087c9326fc169458fb1f7a`。
- cut .30：`computations/numerical-m2-tail-smallcut-30-optimized-config.json`，1754 B，SHA `865e19571c00fc68658555d1e85ac07d32b884e54a81cccf4192da1c02b4b270`。
- cut .35：`computations/numerical-m2-tail-smallcut-35-optimized-config.json`，1752 B，SHA `938d10c172c9a73b7c90c3fdbb03659438d2d294f60301e9cc4263e818703ea2`。

全部 controls、正 warp weights、cut、width、curvatureBound、calibrationSteps、warpSteps、quadratureTolerance、caps、orientation 及其余原字段都在这些完整保留配置中；没有只抄一个前七维摘要替代完整参数。

三个原 row 明确给出 mode=2、far=48、steps=512、angularSamples=32；形式测试幅度依次为 .0002、.00015、.00008。完整有效重算命令为：

`node <restored-source-topic>/scripts/closing_weighted_modes_diagnostic.mjs <complete-config.json> <new-output.json> 512 2 48 <amplitude>`。

这是从完整源 CLI 和报告中实际参数恢复的有效完整调用，不能冒称取得了原操作系统 argv。原 input 的操作系统绝对路径、run ID、exit code、wall/memory limit、运行时构建和历史 writer self-SHA 均未在这些报告记录，台账明确为 null。现在完整源的可核身份并不是未知原 self-SHA 的代填。

## 4. 原有限结论完整保留

以下数值来自原输出，没有重新计算。

| 配置 | cutSlope | 线性 T 正性幅度采样门 | gradient 幅度门 | 形式 max abs curvature |
| --- | ---: | ---: | ---: | ---: |
| opt / rCut .60 | 5.696892857398272 | .0003076019293884065 | .3000000000000221 | 5.99990029460799 |
| rCut .30 | 11.856884030602924 | .0002116564874498456 | .1500000000000081 | 7.999390718951923 |
| rCut .35 | 10.349188896222387 | .00011479353136388941 | .17499999999997415 | 7.9993898282415055 |

三份形式几何的 sampled minProjectionD 依次为 .9988584920266643、.9996188920653392、.9998241090933093；linearAngularBranchMinimum 依次为 .3498090197364738、.2913045009520713、.3030966200838944。每份精确峰值位置、所有其他顶层统计、阈值定义、形式几何 scope 及全部必要已记录标量均见台账。各 48 行 cellRows/cellThresholds 的原全字仍由 Git 恢复，未重新编码入新账本。

原报告明确区分两类门：gradientAmplitudeThreshold 是 r/(m abs(f)) 的角投影诊断；另一个 r*w/(m abs(f)) 只控制归一化 P，并不是嵌入或图表示的必要条件。这一区别保留。

三个配置本身是不同 metric。所谓 refinement 是每个固定配置内部的原有限积分采样，不能将不同配置之间的数值比较写成 same-g 收敛。形式二阶场还在幅度平方阶违反 nonlinear Gauss；sampled curvature、线性正性或投影值均不构成完整 nonlinear tail、连续角度、闭面、嵌入或 reach 证明。

## 5. 后续实际成功与失败仍在原完整记录

[原 M2 状态总记](numerical-m2-status.md) 的完整 27647 B 留树。它保留这些线性设计之后实际求解的独立结论，包括更大 continuation 试点失败、有限 minA 分支限制、M24/N384 FFT 网格 audit 失败、随后正确网格实际结果及更高幅度尚未完成的责任。这里没有用三份线性屏幕替换那些实际 nonlinear 记录，也没有把原文件存在推断为已知进程 exit code。

[RET42 完整账本](../computations/legacy-three-coordinate-design-histories-retention-42.json) 37031 B 继续保留全部原设计搜索来源与参数；其 blob 为 `2f6d443d29800448e62a55717a59d2b7b404c7b9`。本次仅退三个明确后续生成报告，不复退原搜索历史，也不涉及原驱动未闭合的 Nelder。

## 6. 读者、恢复与执行边界

已知引用来自 RET42 的记录和原状态说明。搜索不是全部消费者不存在的证明。任何未来需要完整 report 数组、原全字或 original wholeSHA 的读者，先从固定提交用对应完整 path 恢复；台账的 scalar 摘要不是数学输入替代品。

原输出精确恢复采用每项记录的 `git show` 命令，将完整 blob 放到独立恢复根中的原相对路径。科学重算读取全部配置和完整源；不宣称跨平台浮点结果或新路径字段逐字相同。旧原字身份由 Git 保证。

本批只做小文本、完整源接口、参数对象等号和元数据/哈希；没有本地科学、AST、数值算例、compile、基准或重放。没有为退存或当前科学加入新的验证门。所有源、参数、proof、port 和活输入仍留树；最终发布只处理 fresh path/blob/bytes 完全匹配的三项。
