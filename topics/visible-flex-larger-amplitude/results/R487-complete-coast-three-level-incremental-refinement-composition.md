# R487：完整 coast 包围在同场三级增量精化中的实际组合

作者：ChatGPT（AI）。日期：2026-11-16。

## 487.1 对象、来源与本结论的边界

本结论给出独立 request216 的条件包含证明与可执行来源组合。其真实祖先是 request214 的完整同 job 链，而不是把 request207 的全 M 重算路径重新命名。request214 的正式源提交为 `29df28d35ef85a7c4a6474c28451c58d9f25c802`；原 request 的字节身份为 42062 B、SHA256 `c81530feca5c61e9a901937abf2e5c2704562f6eeaff0cbb70b817ec48519fe1`。本结论依赖已发表的 [R483](R483-complete-coast-Bernstein-ranges-in-current-metric-consumers.md) 的区间包含论证，以及 request214 已有的实际首场、R456 同远端族精化、R464 增量 M 精化三层责任。

request216 沿用 request214 的准确 C 定义、深根全族、原九参数加第十参数的准确字值、原 205 子合同、原两阶段 453→450 求解、首闭面参数策略、R456/R464 全部科学方法与原接受条件。唯一新的数学求值作用点，是后置 metric 与 fixed-target evidence 中对准确负速度 coast 分片的三 jet 包围。新的来源组合把这一作用点接到首场、真正的同远端族加密场和真正的增量 M 场；各场仍必须由自己的完整求解与原检查点写入者真实产生。

本结论不声称 request216 已运行，不声明严格成功、加速或更小的实际误差。初点 factory 的域扫描没有被替换；新的 range helper 不能倒填该扫描的未决结论。旧日志、旧结果哈希和旧接受状态也不是本次状态数组的恢复来源。

下文中“同一准确目标”指同一个原 C/root 语义、准确控制点和 DAG 所定义的函数。完整闭面相同还要求首个实际 construction 的宽度、帽高、全部 marker、材料图及运输、尾帽和归一化解释一并固定；只比较十参数不能证明完整闭面相同。实际来源 receipt 与准确对象相同是两个层次，均分别记录。

## 487.2 固定准确对象上的 coast 三 jet

设真实 coast 局部坐标为 $t=(s-S_1)/\ell$，$\ell>0$，并把完整三项 coast bump 合并为次数至多 8 的多项式 $P(t)$。原定义在该片上的三个准确表达式为

$$
a(t)=A-\kappa\ell t+\ell^2P(t),\qquad
a_s(t)=-\kappa+\ell P'(t),\qquad
a_{ss}(t)=P''(t).
$$

这里 $A,\kappa,\ell$ 均来自当前同一个原 factory/DAG 和当前 C 语义叶；不是从数值 compiler 的输出反解的常数。全部十个原参数仍参与原定义，coast 三系数仅是其实际对应的第 3、6、9 项。其余参数、其余支撑和第十项没有被删去。

R483 helper 首先核原定义与实际分片结构，保所有可能的准确 piece 与其实际 local interval 的闭交。对不满足已识别 coast 结构的情形，它调用原 range 路径，而不是用未经证明的重写。其他分片全沿原路径。实际原 72c 定义中的 $S_1=\operatorname{constant}(\mathrm{end}+\mathrm{dA})$，第二个支撑为 $\operatorname{constant}(\mathrm{end})$ 与 $\operatorname{constant}(\mathrm{dA})$；这些是 recipe 的准确有理常数。因此“前两支撑的右端不超过 coast 左端”的检查没有把一个非退化的 C 包围盒同自身分离，也不因该假想依赖而必然回退。

**命题 487.1（当前三 jet 包围的包含性）。** 假定当前原表达树给出的各准确 C 语义叶均被其当前区间包含，原 coast 结构识别条件成立，且 helper 的向外区间运算覆盖相应准确实运算。则 helper 返回的三个区间同时包含该输入闭 cell 上每一个合法原根、每一个可能准确分片位置的 $a,a_s,a_{ss}$。

证明。把 $\ell$ 和 $t$ 分别仿射映到单位闭区间。在半径表达式中，$\ell$ 的次数不超过 2、$t$ 的次数不超过 8，故使用完整 $3\times9=27$ 个张量 Bernstein 系数。Bernstein 基函数非负且和为 1，因此全部准确值位于所有系数的凸包中；各系数的向外区间包围再取 hull 仍包含原集合。这个结论不要求各系数独立可达。对 $a_s$，其关于 $\ell$ 是仿射式，故在完整 $\ell$ 区间的两个端点上分别使用完整次数至多 7 的 Bernstein 系数即可包含全矩形。对 $a_{ss}$ 使用完整次数至多 6 的 Bernstein 系数。零宽坐标区间按同一闭表达式退化，不能除以零宽度。

原 $A,\kappa,\ell$ 间的相关性被矩形包含放大时只会增加集合，不能遗漏真实根。支撑外的准确零项、各分片闭端点和所有可能分支仍完整加入。最后对这些候选取 hull 保持包含性。因此得到命题。更详细的完整系数与回退责任见 R483，而不是在本结论中另设数值比较门。证毕。

该命题不声称新 hull 必严格小于旧 hull。不同表示和区间依赖可使两者相同、相交或一方更宽；实际输出必须据实报告。它也不把 literal numeric profile 视为准确 C 的实现点，更不把 compiler 字值与准确参数的偏差忽略。

## 487.3 实际 metric 与 evidence 的作用点

各实际场仍使用自己的原 checkpoint、Saved/Prefix、完整径向 replay、cuff atlas、shared field 和原 M 维度来源。新 consumer 只在原 Prefix.inspect 或对应完整目标 range 路径形成一个局部 `CoastTargetRange`，委托当前实际 target 读取同一表达式与叶盒。它不向原 target 模块写入属性，不把旧模块的全局变量猴补成新实现，也不更改 checkpoint、数值 profile 或 actual_driver_source。

准确公共坐标仍使用当前准确总长与数值坐标长度各自的原角色。特别是精确目标中的 $L$ 与当前记录的 $L_{\mathrm{num}}$ 不被混为同一字值；实际 piece 的 local interval、所有支撑、可能的准确逆像和原端点都保留。R483 的局部变量消除与完整 Bernstein 只改变包围的求值方式，没有重新选根、重新定义长度或在 midpoint 选择一个 piece。

**命题 487.2（闭 metric consumer 的条件保全）。** 在命题 487.1 及原 consumer 的全部输入条件下，把该 consumer 的准确目标三 jet 包围换为上述新包围，保留原场包围、坐标变化、分片覆盖、严格不等式和未决策略，则它所证明的每个域/metric 结论仍是对原准确目标的结论。

证明。原 consumer 的后续运算只要求目标 jet 位于输入区间，不要求该区间来自某一种代数表示。命题 487.1 提供相同对象的包含。原严格谓词仍在包含整个真实集合的区间上判定，因此其真值证明范围不扩大到原输入之外。不能证实的 cell 仍进入原未决/细分路径；原资源和异常责任也不改变。证毕。

request216 的统一 evidence 源显式支持四个原实际 family：`original112`、`resolution112`、`completeM`、`incrementalM`。这不表示一次运行自动生成四个场。本入口真实三层分别为首场 `original112`、R456 场 `resolution112`、R464 场 `incrementalM`。三个 measure 和最终 compare 都调用同一新的 R487 evidence 源及 schema，不把旧 R459 或未接 union 的五视图身份当成本次实际证据。

完整 base 闭域包围与真实有限 t 网格仍是原两种责任。每层实际 t 网格为 4、8、16 等分，使用共同的四个原 witness；证据中的全 t 转移仍以原共同材料、准确相位共轭和其条件为依据。有限 t 点不是完整 t 闭域证明。相邻层严格 sup 下降、上界改善和无法判定仍由原 comparison 字段分别表达；较小的上界本身不能证明真实误差严格下降。

## 487.4 真正的三级父链与完整闭面条件

首层仍重新执行原 205 子合同的真实 C、factory、完整 112 远端族、当前 453 和冻结参数 450，再由原原子检查点写入者产生首场。它没有把历史 actual202 的状态/J 作为当前状态，历史十词只按原 205 来源规定使用。

第二层使用 R456 已有的同远端族复用与新网格采样机制。五个明确 factor 均为 2：径向 mesh、field/native angles、native steps、material angles、physical angles。所有必需旧径向节点与新增 knot 的完整并集仍由原逻辑形成；`max_nodes=2400` 只是容量，不能据此预先声称真实节点数或丢弃超容量节点。若容量不够，原层真实 partial。

第三层在第二层真实 accepted checkpoint 存在时，以其为实际父，增至 $M=128$。四个分辨率 factor 均为 1，含义是保留第二层真实已有的角数、steps、材料与物理计数，不是返回旧初始网格。R462/R463/R464 的增量远端族逻辑保留原 112 模态的完整真实来源，并真正计算新增模态及全部新的物理采样/完整 M 求解。没有以旧 112 行补零冒充新增响应。

**命题 487.3（条件父链）。** 若三层的各自原接受、完整返回、来源绑定和 owned quiet 条件实际成立，则本入口的第二、第三层分别消费其直接上一层的真实检查点和实际网格。它们的状态、J、FD、原门和返回身份各属于本层；没有从上一层继承本层尚未执行的接受结论。

证明。各 owner 的输入是实际父 launch、adapter-status、checkpoint、config、C/far 及源 receipt，而不是前一层成功标签。R456/R464 的原相容性检查和全部 solver 调用保留。新 R487 postsolve 来源仅识别这些实际 receipt 所对应的场，重新调用该场的径向、atlas、shared、metric 与 reach。新 held 视图只把实际新的 postsolve tuple 接到原完整 held consumer，不转移旧场证书。故在全部条件满足时直接父链成立；任一真实未返点只留下原缺口，不由源组合补造。证毕。

完整闭面比较还要求实际首个 construction 的 A/B、宽度、帽高、全部 marker、材料 pullback、尾帽及 transport/normalization 条件。原首次参数策略 `b49769f1…` 与共同材料实现 `50bf2d04…` 不变。真实 first B 缺失时，依赖它的 measurement 记录 unpaid；这不会成为新增的 BVP、网格精化或 held 前门。仅有同一准确 C 与十词，不能把本来未执行的共同材料拉回声明完成。

## 487.5 实际来源生成与调用闭包

本入口保留原 request214 的全部 251 个公开 source pin，并增加 9 个明确公开源，因此公开表为 260 项。原 R464 的 15 个实际生成视图、已刊 R483 的 5 个 metric/evidence 视图和本次 R487 的 13 个来源视图组成 33 项生成表。两表无同名覆盖，完整表为 293 项。

13 个本次视图承担以下真实调用责任：

1. R464 union metric 与统一 evidence，真正使用当前 union 的 Prefix/Checkpoint loader。
2. 首场 block-postsolve 的 base、parameter wrapper、necessary reader、held 与原闭面 orchestrator。
3. R456 的 postsolve、necessary reader、held。
4. R464 union 的 postsolve、necessary reader、held。

这些视图逐字绑定各自的原 baseline，精确替换有唯一计数，并核完整生成输出身份。旧源码只读。视图生成在实际 checkout computations 目录发生，因此后续模块的实际 `__file__`、HERE、导入路径和记录的 source SHA 都指向新文件；不能只改变 JSON 标签而仍执行旧函数。

实际顺序是：先绑定 outer216 与其原 214/205 子合同，建立原唯一 namespace/clock；再于同一个 job 依次运行原 R464、R483 和 R487 三个源文本生成器；随后原 dispatch 的源码/正常 Actions 语法步骤看到真实生成文件；新 owner.prepare 再绑定完整来源及实际三份生成 receipt；最后原科学与后置三层消费者启动。生成器只构造公开源码文本，不导入/执行目标科学模块，不编码或搬运科学数组。

旧 205 dispatch 使用其原 schema 的明确派生实例。其实际 source 表为 195 项：原 154、当前三个 metadata source、33 个生成源，以及五个额外 coast source/plan 依赖。其余公开祖先与 caller 仍在 outer216 的完整 260 项表逐项保留。195 不是把 outer 的 293 项省略为科学闭包，而是原 dispatch 的实际角色表；正常 caller/source 绑定另外支付剩余来源。

源生成失败、尚未写完 receipt、完整输出身份不符或原正常语法阶段失败时，不伪造成功回执，也不绕开原启动流程。必要读回保实际完成的生成阶段与未确认阶段、原错误和原文件身份。新的 reader 明确读 `source-preparation216/result.json`，与 owner 实际写入位置相同；没有从旧 214 准备目录取替代记录。

## 487.6 有限资源计划而非收敛声明

request216 保原 job 绝对钟与阶段裁剪。科学预算 18900 秒及读回/关闭保留 2700 秒都来自原 205 namespace，生成、初始原链和两个后继共享该时钟。新角色不重启时钟；总 job 上限仍为原 360 分钟。末段 900 秒为原 terminal measurement/close 计划保留，不是额外总资源。

原有限上限保持如下：

|角色|声明上限（秒）|仍需满足的实际条件|
|---|---:|---|
|R456 新网格采样 / 全 450|900 / 7200|剩余绝对钟、容量、原完整输入|
|增量 M deep / sampling / 全 M 求解|300 / 12000 / 7200|真实裁剩余，不承诺新增模式完成|
|每层 radial / atlas / shared|600 / 120 / 300|原完整闭片与实际场来源|
|每层 metric / reach|600 / 600|原包含、未决及资源策略|
|witness / held / measurement / display|120 / 300 / 300 / 120|各实际必需输入存在|
|最终 comparison|120|只比较真实已产生的结果|

完整误差 measurement 的 `measurement_width_goal=1/100000000` 和 `metric_reference_eta=1/1000000` 沿原工作计划保留，不变为新的 solver 接受阈值。原 RMS、native、boundary 或 full-DN 容差与全域相对 Gram 算子误差之间没有被本组合另立数值等同。有限三个层次和有限 t 网格也不构成“已经任意精化到机器误差”的结论。

实际时间不足可以导致某角色尚未启动、某模式/片/方向未返回或某 evidence 不完整。源与预算声明不能替代这些实际记录；后继父缺失时不允许造一个成功检查点继续。原可独立推进的角色仍按原入口运行，不因新增 metric 或 B 缺口增加求解门。

## 487.7 必要读回、异常与清理

新的三层 chain 必要摘要仍是一个不超过 90000 B 的对象。它保全部原必要 source/input/result 身份、真实 trial/FD/native 范围、失败地址、未返回/未访范围、测量各层与 comparison 原字段以及显示各帧必要 metadata。原 first-chain 的 R477 读者继续保完整 point_index、radius_word、role、actual_error_type、actual_error、all_pending_closed_fragments、retained_original_leaf_rows 与 complete_point_not_returned 等实际存在字段，不补造不存在的返回。

新增 coast worker 仅输出必要的实际实现来源、完整范围工作计数和最后位置。它不是完整区间账本的编码，不用计数推断全域已付。来源生成记录只含公开源码、实际字节/hash、当前阶段与错误；不是科学数据归档。原大 arrays、cover ledger、逐行 witness 和临时显示仍只留 RUNNER_TEMP。

若新的三层 chain 必要摘要超过 90000 B，其原分支仍以真实运输失败/70 表达，不拆包，不把删除字段后的小摘要冒完整成功。独立 composition 的纯 metadata readback 沿原214的 require(len(record)<=90000)，超限会抛 ValueError 并退出1；不能把所有原必要 scope 的错误退出都统称70。两者均不写完整读回授权。科学 partial、读回 partial 和进程静止是不同状态。scope 或错误没有成功传回，不能由绿色 job 标签推断其已经付清。

新增 owned role 保原 pid/session/group/start-time 与实际子进程关闭记录。清理前须原全部必要 readback marker、新 composition marker、新 chain marker及实际 owned quiet 全部满足，且 source/run/namespace 绑定相同。不能确认静止、必要读回失败或源准备失败时，报告实际 cleanup 未授权/未执行范围；不与仍写 raw 的 child 并发删除。该资源生命周期不是新数学接受门。

## 487.8 本结论已经与尚未支付的责任

本结论支付的是：同一准确目标的 coast 包围改写在原 metric/evidence 中的条件包含；真实 R464 union 三层路径上的完整新来源组合；统一实际 evidence family/schema；原时钟、读回和 owned cleanup 合同的显式传递。

本结论没有支付新的实际 C 积分或 head 细化，没有执行新的 full-domain initial factory 扫描，没有保证原有限 C 盒足够窄，没有声称新的 native/J/FD/full-DN/闭面几何已经成功，也没有把 R483 的五视图误当已经覆盖 R464 union。本次另有明确 13 视图完成真实 union 接线，其执行结果仍须未来公共 Actions 如实返回。

源作者只作文本与纸面推导、完整字节身份/差异整理；未在本地执行科学、导入目标模块、AST、编译、数值对拍或额外 fixture。原 Actions 正常语法/输入绑定流程沿用，未建立新的独立审计前门。

具体最终文件、准确 SHA、全部 baseline 差异和入口参数见 [request216 接口](../notes/2026-11-16-request216-complete-coast-incremental-refinement-interface.md)。该接口和当前源码是 future-run 合同，不是本次实际结论 R488。
