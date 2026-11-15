# request194：actual189 已返回 owner 的十参数完整三残差继续接口

## 状态、原问题和独立性

本入口承接 [R401](../results/R401-actual189-complete-ten-69-accepted-and-resource-partial.md) 的实际已返回十参数点。actual189 完成了 69 个原 Armijo 接受，随后原 2400 秒总预算用尽；最后一次完整原接受点可作新的数值初猜，但该运行没有 final、末次 FD 或原最终消费者，也不是 completed checkpoint。194 是另一个明确声明、重新形成当前状态和导数的完整实验。它不把 189 未访问的后缀改记为已完成，不恢复已删除 raw，不借用 185 的末次 FD、Arb 或 453 门。

科学算术、源码导入、AST/编译及运行检查只在公开仓库 Rogerhu12/math-research-public 的 Actions。根审阅限文本、字面来源、字节身份和纸上推理；没有本地执行科学函数，没有增加独立测试、fixture、科学预审或额外验收条件。原完整方法是 [R378](../results/R378-fixed-shape-ten-coordinate-minimum-norm-Newton-and-Cauchy-descent.md)、[R392](../results/R392-complete-three-residual-normal-correction-on-ten-parameter-predictors.md) 和 [189 完整接口](2026-11-15-request189-persistent-ten-full3-normal-continuation-interface.md) 中的十参数有限字面模型。连续 $C$ 十族、真实 full-DN 场及同一 $g$ 的冻结 450 在其他入口单独承担。

本次仅发布六个独立运行/参数文件及本接口。实际结果号留给 R410；source push 触发本工作流后，才记录官方 run/source/job 身份。本文没有预填实际接受、时长、FD 成功或最终门。

## 1. 实际父点：两条原始路径与诚实 partial 标记

原 run 为 43762371885，source 为 598951293035cb2e2fa705bc13e24cc1a5f59b8a；compute 132959791013、report 132971537272。原 producer 为 geometry_20261115_completed_ten_predictor_normal_resume.py，SHA-256 295c375b016a16bbdd7bffe68db7ffcdd3f715c33eee7a20147e9b5c379d0f8a。

原 status 为 29251870 字节 / 979e391ba22e13d3a4e8ca259f414391f3ac5f513395d9e33dfc73a13af5fdaf；实际必要摘要为 87897 字节 / 8549fc6e2bb1ca4514b789e0995083aa2a07425b37c37e7434140472757c0c15，摘要身份不含日志分隔 LF。raw status 只保原身份，已真实清理，不能依靠 SHA 恢复其内容。

新 recipe 的十词来自原摘要 current_accepted_ten_parameter_words，并与 trial_conclusion.first_and_last_selected_original_points[1].original.actual_parameters 逐词相同。对应方向 68、alpha_index 2、$\alpha=1/4$、normal_update 2、normal_trial 0，original_owner_direction_accepted 为 true。十词的原 canonical parameter list 是 554 字节 / 6cde2c5de1c286bcf423422a4b4f0f34bb6eb61f40660a1ff87e8e76c9f69205。新 recipe 明确保留 diagnostic_completed=false、resource_partial=true、final_present=false、is_completed_accepted_checkpoint=false，以及原 ResourceStopped signal 15 异常；parent_stop_reason 是原 null。

|坐标|作为新输入的原 Decimal 字词|
|---|---|
|0|0.30349714070335898202049490814191077205575467864259|
|1|0.22320768974262297170414986995579884450841998149419|
|2|0.34081705005491527094864297864650612156455583844009|
|3|-0.069175246714031320186776691087337749389739707375868|
|4|-0.015506713450726331055293869372957681520904387286358|
|5|0.93421350081504509386680316080616227348253782114646|
|6|1.0695276807467625106931097655550841166478724545351|
|7|0.62656309587554530255529775529366865178791645293775|
|8|0.94772070126252395783272186025386560172248319686079|
|9|0.38289088706268504028829015458735618531240133888561|

父点记录的 merit 是 1.7920048197146154915389967007746182829336465880156，原接受界是 1.8071251366356697005337935650872548377986862362431。原三分量分别为 -1.7615943523145452431444608100510072799378143829661、-0.0012850012319465674901032551952957891854271902654189、-0.69339262045003242682110304960776707343920701057102。这些量只用于来源说明；194 初始 $F,J,W$、当前状态与所有后续判定均重新形成，不把父记录直接当新模型输出。

原 actual185 / actual183 来源仍保留在 first_introduction_history；旧 3bec helper 的 POLICY 中 actual183 初始父字样是首次引入时的冻结源历史。新的 recipe 分支显式检查上述 actual189 returned owner。原自身 schema 的 completed-parent 分支保持，但不由本次 partial 父冒充进入。

## 2. 原数学方法和完整预算不变

旧 actual189 producer 的继续循环及数值函数体保持，新增源只替换身份、来源分支、元数据和 request194 事件名称。原 3bec 全三残差 helper、6b55 全十方向及 fixed_physical_scales、0924 固定 shape 家族、8cb8 Decimal 模型均按原 SHA 导入。旧 178/183/185/189 producer 只作为祖先来源核对，不执行其优化 main。

保持 support_index=1、power=4、catalogue_index=3；不在当前点或 FD 扰动点重新选择 shape。全部十坐标可变。九个物理尺度仍从 actual157 的原九字词固定为 $0.01\max(1,|p_j^{157}|)$，新增坐标尺度是 $0.01$，缩放球半径是 1。父历史 relative radius 0.0000390625 不控制本次信赖球，也不随新父点重新计算尺度。所有科学 arithmetic 保持 Decimal 50 位、ROUND_HALF_EVEN，原有限字面表/三模态传输/全部 112 终端行不变。

一个 persistent owner 承担至多 16 个原八方向块，共 128 个完整十参数方向。每一方向保留原 20 个真实 $\alpha$ 回溯，每一 $\alpha$ 保留至多 3 次完整 $3\times10$ normal 更新、每次原 20 个真实 normal 回溯。原 full minimum-norm QR、明确的 full Cauchy fallback、全三分量仿射目标、固定 $S$ 球的总位移投影，以及每个原 $\alpha$ 冻结的 $p,F,W,Jd$、slope 与 Armijo bound，全部保持。

只有原完整 Armijo 条件通过的点才可被 owner 采用。normal 工作点的仿射目标偏差下降本身不是 owner 接受，未接受工作点在下一个原 $\alpha$ 前丢弃。只有明确“八方向 budget 完成”的原 stop 允许进入下一块；unit 达标、原 20 档全拒或异常不会在同点重启。块之间不重置 owner、尺度、半径或总时钟；每次下一块首响应仍重新形成完整十列。

原请求的搜索上界保持为 156160 次新增 primal、7680 次完整 normal 十列响应，以及至多 127 次后续 outer 响应。这些是上界，并非将会执行的次数、接受保证或用时保证。189 实际只完成 69 次接受且耗尽预算，不能据其耗时推断 194 会完成 128 次。

起点和终点各原 Decimal / explicit binary64 projection FD 消费者保持；总计划是原 60 个 Decimal FD 加 60 个 projection FD，原步长字面仍是 2e-5、1e-5、5e-6。投影点与 Decimal owner 分开记录，不以投影场替换 owner。原 160-bit、depth 14 interval 消费者及完整 453 的 node/mid/RMS/FFT view 保留；七 shape 冻结、原三 active 不改。这一有限模型的最终 view 不等于真正非线性 native/full-DN 接受。

## 3. 六文件最终身份与祖先闭包

下面字节数及 SHA-256 是本次实际发布内容，文件均小于 100000 字节。除 workflow 外均位于 computations/。

|文件|字节|SHA-256|
|---|---:|---|
|geometry_20261115_actual189_ten_predictor_normal_resume.py|49778|0a40ce1edd7a2392a7024c7aba1d9434b935d5effb83f8f433b844e1aae692d6|
|root_20261115_actual189_ten_predictor_normal_resume_readout.py|49199|f6c0a5c2bf924038c8d3c89f4b1f4f6eec069cec05adffde22383d30dfb4d104|
|geometry_20261115_actual189_ten_predictor_normal_resume_temporary.py|22890|da346ac1d3bb238e39cf2ef15b68194e356035ae135cb668831852b52984b7f6|
|actual189-returned-ten-predictor-normal-parameters.json|17537|185d2891b78b5d7bcef5b46e8bf8a6730f3916acc850cba72393a9395cb8dc78|
|public-actual189-ten-predictor-normal-resume-request.json|67995|7482a654dae7a86aceef2b4125f2c0f2c3ba990fbd27c2f559af0e867f43057c|
|.github/workflows/visible-larger-public-actual189-ten-predictor-normal-resume.yml|32341|8c4721d39d8696fd06fa69091309528bd14cf4c193023afe5c721c3869b3cea6|

request 的 source_sha256 逐值保留原 119 项并加当前 producer，共 120 项；workflow_support_source_sha256 逐值保留原 13 项并加当前 reader 和 wrapper，共 15 项。当前 producer 的 consumed-source 闭包从原 49 增到 50，唯一增加项为当前 producer 自身；原 41 项 actual157 祖先及原 family/model/direction/normal-helper 全部保持。三个集合职责不同，不把全请求身份表误写为实际科学进口集合。

原四个科学输入从公开历史提交 8bd267107cc8710d371f3b62c02986655ac965b0 取原字节，重新核下列身份；不从私库或新旧跑次的失败目录拼装。

|输入|原字节|原 SHA-256|
|---|---:|---|
|accepted|2614352|b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff|
|prepared|4220043|0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714|
|tail_anchor|6815|e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51|
|tail_config|2161|01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5|

完整历史路径保存在 request.inputs；原 accepted/prepared/tail_anchor/tail_config 的每一字段、预期九 literal binding cc10a080eafa19e282ca22cefa62af57dadaf0ab19e54b0a4e6f7e7188ec32d3 与十 literal binding 065b11752c4b72422df2d9564748f2418f0a277401877c00c359d72171eefcbd 不变。原 R392 helper 证明身份 13940 字节 / c34e8e87b8a9d0d0ab673810d31bf823f4c218819ced96efb8f2cee22f6af2fa 保留。

运行时固定 Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0、python-flint 0.9.0，BLAS 线程数 1。原公开 source 恢复流程与全部原输入核对保持；当前所有导入/编译检查都在本次 Actions 中执行。

## 4. 一条必要结论的实际范围

189 的实际单必要摘要已为 87897 字节，接近原 90000 字节界；194 声明新的必要标量选择范围，不把大树编码、分包或改名后运输。reader 先完整读取当前原 status、全部原记录、FD 和终门，再进行以下明确选择：

1. 保留全部 128 个方向地址、16 个块地址、每个实际 $\alpha$ 的地址/原判定/计数、全部 owner merit、每个已接受点的原 Armijo bound，以及完整原 stop、异常、未返回和未访问后缀。没有记录的项与已记录 null 分开。
2. 所有 normal 层原 trial 均读取、计数、分类和绑定身份。必要摘要保留原 all-primal merit 极值、首末选中详细点、全部错误以及 pending / 未返回地址；不运输完整临时参数或状态数组。
3. 方向表显式去除 formed_full3_slope 列，仅另列可用原 slope 历史的字节身份、计数及首末原词。中间 slope 原词不传输；方向表列名和每行同步删除，未用 null 或零假装保留。
4. 原 $\alpha$ 表显式去除 predictor_merit 列，只保留该完整原标量序列身份、计数和未运输声明。所有 $\alpha$ 地址、接受/拒绝、normal 计数、选中 merit 与已接受 bound 仍保留，原全 primal 极值保持。此处没有重新计算任一预测值、slope 或 merit。
5. 原完整 initial/final FD 均照常执行；摘要延用旧必要 scope：所有原层的存在、错误、门、最大量和完整记录身份，全部最终 scalar/453/native 门与缺失状态。没有缩短 FD 运行层数。
6. 原 status、原 direction / trial list、科学 stdout、错误文本分别保整体字节身份；巨大 stdout 不打印。原错误文本小于等于 12000 字节时全文返回，否则明确选首尾及全文件身份，不伪称全文。

reader 不调用科学模块。不把 90000 字节上限当科学 acceptance；若真实必要摘要仍超界或结构不完整，则明确返回 reader code 70、错误和未完成身份，不能拆包回避。wrapper 的最后 summary 加入自身状态后也独立遵守同一单条上限。以上选择完全明示在 request.readout_contract 与 reader 新函数中，不沿用旧“所有 predictor/slope 原词均已运输”的声明。

## 5. 原时间、进程和清理责任

原 producer / whole child 均用同一个 2400 秒总预算，包括 imports、source binding、初始 FD、搜索和全部原最终消费者；producer 在 main 入口、身份 setup 之前启钟。wrapper 90 秒终止宽限；metadata reader 300 秒、30 秒终止宽限；science step 50 分钟，whole job 65 分钟。没有为了最终门另开科学时钟或减少搜索/FD，也不在 16 块之间复位总钟。

SIGTERM 请求原 producer 写 partial checkpoint；ResourceStopped(RuntimeError) 与原 NumericalFailure/ArithmeticError 分开。资源耗尽可以发生在长 FD、normal 工作或编码，未返回 call 不补成 domain rejection / all-rejected / stationarity。硬停止可能没有完整 checkpoint；原缺失状态须如实返回。

wrapper 与全部 children 保同一 rules-runner 所属进程组，不 detached；记录 actual argv、child exit 和 wait/reap、最终 own quiescence。report-only 只读取既有文件，不恢复或继续科学。只有必要摘要完整、原错误读回成功、reader metadata 完整、owner 与 post-reader 明确静止、run/source/wrapper 身份及摘要 bytes/SHA 均符合原条件时，always 清理当前本次临时科学目录、原输入目录与本次原源码恢复目录。未知、缺失、超界或未静止保留当前 ephemeral runner 中的内容，绝不当作数学接受；不上传 Git/Release/artifact，不创造 raw 永久备份。

工作流保原完整规则 runner 3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde。仅将已读双 README blob baseline 显式换到根 21bd547f56590b7f2dd279d0297efb289a9b2783、课题 bff8aea253a9e6a7a4fac28d810ac454c5499fec，原真实 pull --rebase、2700 秒周期、差异读取及变规停止行为保持。root 每次真实 pull 后也检查双 README，至少每小时一次，将实际已读提交写入 HANDOFF。

## 6. 仍须实际支付的结论

发布源和参数仅建立可复算入口。194 的原完整 unit、全部 FD、Arb、453 与 terminal gate 必须由它自己的实际运行给出；resource partial 不能冒充末态。即使该有限模型未来完成全部原门，也不自动支付连续 $C$ 十族的准确目标、338/112 当前非线性 native/full-DN、真实 453→同 $g$ 冻结 450、共享 $B$、全闭面接缝、675 六 jet、材料图/四 Loewner/闭 DFS、完整 $D$、固定 held patch、含反射的非刚性下界、全 $t$ reach 与最终精化责任。课题 README 完成标准保持。
