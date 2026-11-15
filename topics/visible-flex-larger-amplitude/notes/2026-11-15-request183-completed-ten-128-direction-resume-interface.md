# Request183：真实十参数末点、同一 Decimal50 状态的 128 方向续算接口

作者：OpenAI ChatGPT（amplitude）；2026-11-15。所有科学执行仅限本公开仓库 GitHub Actions。本稿没有新运行结果、未来 run ID 或已完成场的声明。

## 1. 已付证据与本次具体动作

[R389](../results/R389-actual178r3-complete-ten-eight-acceptances-and-actual-restart.md) 的实际178r3完整八方向均接受，但已采用非零第十系数，不能通过旧178入口再次构造 `p9+[0]` 来声称接续。本次从该原末十个 Decimal 字符串重新建立完整同一有限字面模型；实际首个 primal、十列 forward、初始 FD 全部重新执行。父残差、merit、J、FD 或旧已清除的临时状态不作为本次求值结果。

本次仅把明确的方向总范围扩展为最多16个原八方向块，共128个完整十维方向；每块直接调用冻结6b55函数，不复制或改变其 Newton、径向 clip、Cauchy、域判断或20档真实线搜索。一个持久状态、一个全局2400秒科学时钟贯穿全部块。每个后续块开始，重新形成当前位置全部十列响应。只有原返回词 `Explicit eight full-ten direction budget completed` 允许进入下一块。原20档全拒或任何非预算停止立即结束，不在同一点重新试一块。

这是在已观察八次真实接受之后扩大同一方法的实际工作范围。父第3方向曾有较小 merit 却不满足原 Armijo 的档位，故本次不把“下降”替代原充分下降门，也不声称接受步长会继续增大。所用有限精度方向和全部最终检查仍有 [R378](../results/R378-fixed-shape-ten-coordinate-minimum-norm-Newton-and-Cauchy-descent.md) 与 R389 已公开的准确性边界。

## 2. 真实父身份与输入点

| 项 | 原已完成178r3 |
|---|---|
| run | `43753070697` |
| source commit | `195cd2d42fe7f73b112022c1f06d50c7e7d9c154` |
| compute / report job | `132931097320` / `132931551767` |
| producer schema | `R259-fixed-power-ten-scaled-minimum-norm-Newton-full3-v1` |
| producer SHA256 | `3e5c8a34f5043fac35addf09627e16e59dcfc7287bb7ec087805be5dcac1474e` |
| 原 status | 970477 B / `d32b951ea9bdb1aaa1ade19f0844ca4eb96a89bb8fc0943c3cf453d6c22b4d8e` |
| 单份必要 summary | 80163 B / `d816bef85711aea3dcdc6ef29ed4fcb4aa0ee5a24ca24e9b7ef4a87c2f38fbef` |
| 参数来源路径 | `final.parameters` |
| 原结论 | 8次接受、原八方向预算结束；不是非线性 native 或完整非零场 |

配方完整保留这十个真实50位数值输入词。特别是第十词为
`0.00093743918442139073375164637457095209406810504324798`，不会清零或先投影为 binary64 再重新称为高精度输入。父末三方程原词与父末 merit 仅供新 primal 的逐词只读比较；不相等将记录，不成为新增接受门。原输入词是数值输入，不是准确根、区间证书或高精度真实解。

仍沿实际157九词一次定义坐标尺度：
$S_j=0.01\max(1,|p^{157}_j|)$，$0\le j<9$，$S_9=0.01$。这里0.01为冻结搜索源的 Decimal 字面量；所有16块使用同一组尺度。它们不由当前178r3点、每个接受点或块边界重估。新缩放坐标 trust 半径继续为1。旧九族的 `0.0000390625` 仅作为历史来源记录，绝不当作本十维步长或新的 trust 半径。

冻结形状为原0924族 catalogue3，即 support1 / power4；形状在所有旧九坐标 FD 扰动、十维 forward、真实试探以及最终消费中完全固定，既不重新挑选六候选，也不把新系数塞入旧九坐标身份。

## 3. 数学对象及继承范围

本次仍是原699节点、698局部单元、七状态传播、每单元十输入的有限字面对象；三个低模链和全部112个固定原线性末端残差责任保留。原所有 mesh、mid、base、controls、频率、target、完整112×112零锚 slope-J 均由真实四输入和冻结祖先源重新构造。形成表仍为原 binary64 样本后准确提升为 Decimal，不声称这些表在 Decimal 中重新形成。

旧九 literal binding 的 canonical SHA 为
`cc10a080eafa19e282ca22cefa62af57dadaf0ab19e54b0a4e6f7e7188ec32d3`；
完整十 literal binding 为
`065b11752c4b72422df2d9564748f2418f0a277401877c00c359d72171eefcbd`。
新 producer 首次构造时核实际原表与这些已记录身份；这是输入对象来源绑定，不是额外的数值精度或科学接受阈值。

非零ξ父点没有支付任何“将ξ置零仍合法”的新科学责任。旧九模型仅为原表绑定而构造，不调用其独立九点 primal、response 或 zero-extension 比较。新初点从完整十族直接评价。状态明确写
`zero_extension_not_evaluated_in_nonzero_ten_resume=True`，
`old_nine_parameters_relabelled_as_new=False`。
删除这一不属于非零十维续接的反事实求值，不减完整十点本身的域、forward、FD、全112或最终检查。

本对象不是准确连续 R323 目标，不能借180的准确 coast 全域结论覆盖它，也不能把本次的有限Gauss标量、返回的导数样本或形成 J 宣称为连续 $C^2$ 或区间导数证书。原 native/current nonlinear tail 仍未在这条低模候选搜索中调用；完整112线性残差不是当前非线性尾的替代品。

## 4. 一次128方向调用的精确生命周期

1. 核本次请求、配方、46个实际 consumed source、所有114源及11支撑源字节。按历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复原四输入到本次 `RUNNER_TEMP`，按原78入口恢复依赖源。
2. 导入冻结 family/model/search，构造原字面表与独立十族，读取父十词为一个 Decimal50、ROUND_HALF_EVEN owner。真实评价初点；只记录父 F/W 比较。
3. 支付原初始完整十列 forward 和三档十列 Decimal FD；另在明确 binary64 投影处支付完整十列响应和三档十列 FD。投影不替换 owner。
4. 块0使用原初始 description 的完整十列 J。后续每个实际进入的块，都在当前 owner 的十词上真实形成新 J；forward primal 是否与原实 primal 逐词相同只记录，不成为新门。
5. 每块原函数最多8方向，每方向最多20实际档 $1,1/2,\ldots,2^{-19}$。严格使用原完整三残差 $W=\frac12F^TF$、实际形成的严格负斜率与原 Armijo。系数 $c_A$ 是 `Decimal.from_float(0.2)` 的准确 binary64 提升，不改成数学 $1/5$。
6. 已接受 state 从原函数原样返回并继续持有；没有JSON往返重精度、没有 block 边界 binary64 投影、没有父 J 或 merit 冒充新值。每个下一块只在原八方向预算结束后进入。
7. 任一块出现原全20拒、无有限负方向、原单位停止词或科学异常时停止后续块。原2400秒总时限到达记 resource partial；不能称“全20拒”或“无下降方向证明”。第16块完成时写独立总预算词 `Explicit128 directions in16 original eight-direction blocks completed`。
8. 若预算和控制流真实到达末端，支付原 final完整十列 forward、三档十列 Decimal FD、binary64 投影的完整十列和三档十列 FD，并执行原 scalar Arb160/14与完整453 circle消费者。共初末12个FD层、120个轴检查；不在每个八方向块另加一套最终门。
9. 全部原 final flags 独立保存。流程完成或16块全部用尽不推出原 unit tolerance、全112、nonzero/native/fullDN 或成功；未执行的最终检查保持未付。

新编排给原局部方向追加 `block_index` 与 `global_direction`。原函数自身仍保存局部0…7索引，不改变原求值事件或数值。对块>0首行的旧通用标签 `initial_complete_ten_J_from_initial_description` 只作元数据纠正，明确它来自该块的实际 fresh response。块的 `continued` 只在实际进入下一块、且全局时限检查已通过后置真；“允许继续”与“已继续”分列。

## 5. 精度、方向与最终消费者的边界

原6b55仍按完整 $(JS)^T$ 的10×3列主元QR形成最小范数候选，在缩放单位球上径向 clip。约定、主元回代顺序与 Cauchy 条件遵循R378；不截断小奇异值、不引入秩通过条件、不换残差权重、不组成正规方程。有限QR、残差动作与形成 slope 是实际提议量；不因 FD relative error 小而断言最弱方向准确、精确满秩、驻点或收敛。

每次真实试探重新执行完整十族 primal及原域；即便线性模型预测下降，也必须通过原完整三方程 Armijo。末端 binary64 projection 的 scalar/453证据只属于明确投影点。其与持久 Decimal 参数差值、各参数 binary64词及原身份继续由实际状态记录；reader只回传必要责任标记与身份。该 projection 没有作为新的迭代状态，也没有被称为同一准确点的连续域证明。

全局小残差或各终门尚未观察。本接口不预填新178r3以外的父点、未来run/状态SHA/接受数，也不假称旧已清除 payload 现仍存在。

## 6. 必要读回：完整工作范围与有限传输范围

新 reader 在Actions内读取整个临时 status、全部实际方向/真实trial、初末四个description及全部120 FD记录。它不导入科学模块，不重算 $F,J,W$、FD、norm、rank或任何区间。原merit极值通过解析原Decimal字符串并比较顺序选择，未形成新差值或科学量。

单份ASCII JSON必须不超过90000 B。必要字段为：

- 初末十参数原词、完整三个原残差、原未加权 merit；父身份、当前run/source/recipe/input/模型身份及原 final flags。
- 128个计划方向行，每行包含全局索引、是否启动、是否接受、原接受α、前后原W、原形成斜率、实际trial数、未访问trial后缀、原停止理由及完整方向记录身份。未启动方向全部列出，不截掉尾部。
- 16个计划块行，保实际启动、原八方向是否返回、方向/接受/trial数、原stop、实际continued、首J来源及forward与owner词比较。
- 所有实际trial的总数、接受数、原reason分类、原域flag分类、原merit极值对应的真实α/F/Armijo/reason、全部实际异常，以及完整原trial列表身份。完整所有seed/实际十词、112向量、节点最小值表只读于Actions，不搬运。
- 初末 Decimal 和binary64的12层原FD step、valid、maximum_relative_error、十列覆盖与全部真实异常；扰动大表仅原身份。有效不等于弱方向准确证书。
- 原 scalar 域、circle/两RMS及其他实际gate的必要标量/布尔/异常；大FFT/投影树保持原身份，未读取或未执行字段不补造。

当前 J、d、Jd 与 trial向量在记录存在时检查相应形状；完整Q/R方向模型经整个原status读取和身份记录，不声称 reader 另作所有Q/R矩阵形状审计，更不声称下游root逐值读了这些大表。旧728ac reader只复用纯元数据description/FD方法；其硬8方向的旧build/main不调用。

不使用字典压缩、编码数组、分包重建或新artifact传输大科学表。stderr的必要原工程错误文本在清理前完整保留；科学stdout只记录身份。summary超过上限时输出真实大小、各section大小、原status身份、实际阶段及失败说明，退出70，不冒完整读回、不将工程超限称数学拒绝。没有局部数值测试或未来大小保证。原实际错误过多仍可能使必要摘要超限，该风险如实由上述路径报告。

## 7. 全局资源、规则同步与清理

| 层 | 固定责任 |
|---|---|
| producer | 原2400秒科学clock，只建立一次，不在16块重置；包含初始、实际搜索和可到达的final消费者 |
| wrapper child | 原2400秒墙钟，含导入/setup；SIGTERM请求原partial checkpoint |
| 退出宽限 | 原90秒，随后才能kill；必须wait/reap所有本wrapper启动的child |
| 元数据reader | 300秒，30秒退出宽限 |
| science step / job | 50分钟 / 65分钟 |
| 原规则runner | 原3b8源，2700秒真实pull/rebase/read规则；只更新已核README baseline |

外层child时钟比producer开始更早，可能先达到deadline；这种实际资源partial不把未执行的final重标为通过。初末FD或Arb较长时同样可能未付，不临时缩预算或降门。规则变更导致停止与数学全拒分开。

独立workflow设置 `merge.stat false` 避免历史大数据删除的diffstat读取；原真实pull逻辑不改。科学checkout/source始终绑定当前实际push，规则runner自己的原baseline/改写H责任保留。子进程不继承GitHub输出及显式凭据变量，规则同步所需权限仍由原外层负责。

只有必要摘要完整且≤90000、三份receipt逐字核对、实际owner静止且所有children已wait/reap后，才显式删除本request拥有的临时科学树、四输入和78源缓存。读回失败/超限时不主动删同job现场，但runner销毁后不存在长期恢复承诺。没有原数据入Git/Release/artifact，输入Git对象缓存也只是临时runner存储。

## 8. 源闭包和独立身份

- 全source表从原178r3的112件保留全部字节，再增加新producer与新wrapper，合计114。
- 支撑表保原10件，再增加新reader，合计11。原728ac作为纯元数据帮助源被实际import；旧wrapper不执行。
- 新producer直接 consumed closure 为46：原九祖先41 +冻结family0924/model8cb8/search6b55 +旧178producer3e5只hash基线 +当前producer。
- 与原178的45件闭包相比只追加当前独立producer，原45个摘要都保留；旧3e5 main不运行，不能称本次仍由旧schema生产。
- 新producer schema `R259-completed-ten-persistent-scaled-Newton-continuation-v1`。
- 新配方 schema `R259-completed-ten-persistent-Newton-resume-recipe-v1`。
- 新wrapper schema `request183-one-persistent-completed-ten-continuation-v1`。
- 新必要reader schema `request183-complete-ten-continuation-necessary-readback-v1`。

配方允许两种明确来源：本次硬锁的真实178r3末十词；或将来本producer own-schema的真实已完成、至少一次接受的十点。后者必须提供真实run/source/status/summary身份、producer一致及完整十字符串；当前请求没有填入任何未来对象。未来更换父配方/请求的来源绑定仍须完整说明，不能仅替旧origin标签。基础表、固定S、形状与原policy保持。

四输入逐原size/SHA从同历史commit恢复。原accepted配置、prepared完整mesh、零尾anchor、T112-config仅承担原有限对象输入责任，零尾anchor不冒本次当前非零native锚。

## 9. 冻结文件、实际入口和完整差异

| 文件 | bytes | SHA256 |
|---|---:|---|
| `geometry_20261115_completed_ten_joint_newton_resume.py` | 41433 | `57569d4734ec10f64db71416ab2e61a37db2b724addad64413938c16d803f1d6` |
| `root_20261115_completed_ten_joint_newton_resume_readout.py` | 23326 | `eed7c6a5de9c83bf7bd6ecffa034bb8e0e57f00dac0c26651d3b6429a404e91d` |
| `geometry_20261115_completed_ten_joint_newton_resume_temporary.py` | 22267 | `8b9d994b749bdbfc1d2435aeb60f75fe2362aaa19ae4050e988b56abf1e2ca50` |
| `completed-ten-joint-newton-actual178r3-parameters.json` | 11689 | `ea0aa4ea67fb5a1dbc883cd5b641bc230414516a8a1fa79bf55fd3d1e38cf2bb` |
| `public-completed-ten-joint-newton-resume-request.json` | 49751 | `6a5ef150715a4ee2256a8bb23e5db8be69f158ca531f1440dada39fb787e8fd9` |
| `visible-larger-public-completed-ten-joint-newton-resume.yml` | 27272 | `a14fc2eb08e97afed669d4aefac253dd281f95a48806e7ac2e87103d3ae7b721` |

科学入口通过wrapper实际传入 `--directions 128 --backtracks 20 --decimal-digits 50 --interval-bits 160 --interval-depth 14 --wall-seconds 2400`，其余四原输入与参数配方由请求路径及真实SHA提供。wrapper一次启动一个科学child，不启动16个重新初始化的owner。

唯一push触发文件为
`topics/visible-flex-larger-amplitude/computations/public-completed-ten-joint-newton-resume-request.json`；
新工作流为 `.github/workflows/visible-larger-public-completed-ten-joint-newton-resume.yml`。本稿不触发运行，不含实际183run。
临时输出 `completed-ten-joint-newton-resume-temporary/science/completed-ten-joint-newton-resume-status.json`；summary原帧
`BEGIN_VISIBLE183_COMPACT_SUMMARY` / `END_VISIBLE183_COMPACT_SUMMARY`，SHA不含日志分隔LF。实际目录细节以冻结wrapper的 `science` 路径为准。

完整文本差异分为producer相对3e5、reader相对728ac、wrapper相对960507、recipe相对原8891 B、request/workflow相对178r3六份；另给文字replacement来源表。producer numerical6b55文件保持原15144 B / `6b55a6d223f0103bb0396a578d89cfd06c6b4888d38dbb4d518eaa3ecb6f2861`，family0924/model8cb8均不改。只做源文本、JSON及字节检查；未在本地导入或执行科学，未增加独立fixture、精度验收或审批流程。所有实际语法/依赖检查仍沿Actions已有前置。

下游真正全三非线性校正的185是另一独立算法责任，不在183中暗接，也不借其未来结果说明183可收敛。
