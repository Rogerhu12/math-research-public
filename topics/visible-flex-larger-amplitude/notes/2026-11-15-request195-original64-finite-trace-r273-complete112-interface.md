# Request195：原 binary64 成功有限 root 轨迹切向、当前 R273 与完整非零112入口

## 1. 本次实际要执行的变化

195 从原145同一明确六系数、$\lambda=0.001$、四份原数学输入及两份原几何 ready 重新生成现场。它保留原 binary64 noJ primal、原冷初值及 tangent warm/fallback/last/cache 策略、原每轮十档 noJ 回溯、原全部 guard 和严格残差下降。新变化是：withJ 不再把已有限步返回的 root 当作已准确解出的隐式方程根，而是逐次微分这次实际成功 root 轨迹中的 $F$、独立 Gram 构造、真实 Cholesky 和两次三角回代，随后传播全226状态/224形状列的原 RK 图。非线性修正仍由当前完整 R273 产生。

这是一个独立的可执行实现实验。R369/actual172 的向量分解没有逐 root 分支记录，不能证明本差异就是其 finite_secant 数千的唯一原因。195 不导入172、145或其他旧失败现场，也不把旧 $\|r+A\Delta\|$ 当作真实 noJ 导数；本次结果、进展或失败必须由新 Actions 原输出决定。原186/190/192以及其他正在运行的代码均不变。

依据是已发表 [R411](../results/R411-original64-finite-root-trace-matched-variation-and-full-return.md)，12390 B，SHA256 1d66947d6d02b1dac50aa6348e94b56c959336fa1ca52b1ee1450bd6b6ec342c，commit d377a0efde1e2f09074dce178fc18bbd66d70a0d。R283 的固定成功分支范围保留；本实现使用原 binary64 生产链，不能将先前独立 binary128 JVP 或有限精度算子源改名冒接。

## 2. 原字节来源与明确新参数配方

原145基线 commit a513ada7d1dbe1b2fa51d3f1f987c59b48233dba。其115个 source pins 全部逐键保留；增加三份 root/flow/loader、七份协议及 R273 接线、runner 和 reader，共127个 source pins。旧145入口和旧 publisher 作为来源，均不执行为本次入口。原78份公开生产源码由 prepare_public_source 恢复到临时 source tree，原文件不覆盖。

配方仍是 actual119 第三批真末六词，顺序 $[p_1,p_2,p_3,\theta_1,\theta_2,\theta_3]$：

    [0.41654476801167684, 0.23884336093393582, 0.5270922473095916,
     -0.13437878055563054, -0.005765450212224129, 0.4141025261683763]

原来源 run43693462669/source6fffce1f36e876f3b08a1c73198a7fde259d94d6；原第三批 status 1568824 B/10c31f1da398f537f1c9dfb19a162bb6aadb30e7e57fddafffebf7a9a60c08e4，短摘要73546 B/4ec08e23ea41bc3f443f04f613270163c9e8624d8b4172ab2a35f998b75acf5a。只复用真实参数，既不要求低三根门，也不声称该参数已经给出非零原生场。前三坐标为 active，后三 odd 系数固定；仍是 $K=3$、453维设计 BVP，不是同 $g$ 的450维细化。

四数学输入从原历史 commit 8bd267107cc8710d371f3b62c02986655ac965b0 精确恢复：

| 输入 | 原 bytes | 原 SHA256 |
|---|---:|---|
| accepted.json.gz | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared.json.gz | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail-anchor.json.gz | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail-config.json | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

e788 的零尾 J 仅用于未接受初猜，不替当前 $H$ 的真实尾响应。原 T112 config 无 initialCheckpoint；modes112、spacing2、quadrature2048、solveTolerance $2\cdot10^{-9}$、maxIterations32 均原字面。

两 ready 仍使用原既有环境槽，而非未来场或新求解接受锚：

- VISIBLE_FLEX_FROZEN_LEDGER_READY：109004 B/563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6，Git blob4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3。
- VISIBLE_FLEX_FROZEN_STORED_READY：29774 B/c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d，Git blobb6c44fe237750f13c8b10366f15525b481a74e09。

完整原路径、runtime basename、历史 commit 和逐件 bytes/SHA 均在 request，不把路径名相同当作数学身份。

## 3. 真正匹配的数学对象

root 模态数 $M=112$，root 向量维数 $J=M+1=113$；Gram 的全部余弦矩为 $2M+1=225$ 项，组装出的 Cholesky 方阵是 $113\times113$，不是225维方阵。所有 state 形状列为 $K=224$，连同两条 mean 状态，完整局部状态长度226。

对实际接受的第 $i$ 次 root 更新，源中先计算原 $F_i$ 和原独立 $C_i$，原程序实际分解/回代得到 $R_i,z_i,s_i$，并由真实回溯选 $\alpha_i=2^{-k_i}$。本切向将原选中的 $\alpha_i$ 作为固定分支常数，形成

$$
D L_{i+1}=D L_i-\alpha_i D s_i.
$$

$D C_i$ 来自原独立 Gram 标量及全部225项 literal-table 组合，不用 $C_i=F_{L,i}$。$D s_i$ 逐原下三角 Cholesky、forward 和 backsolve 图形成；原 factor、forward、solution 字词都是这次实际原求解所保存的值。没有用 $C_i^{-1}(D F_i-D C_i s_i)$ 省掉实际 factor 图的缺陷导数。

原 normal 停止是 $8\cdot10^{-14}\,\mathrm{scale}$，原失败回溯后的 fallback 条件是 $5\cdot10^{-12}\,\mathrm{scale}$。两者保持，fallback 名称不是精度证明。原循环30次、每次最多20档。成功 normal 或 fallback 返回均至多29次已接受更新；第29号迭代可接受第30次更新，但循环外随后是 iteration-limit throw，无成功外层 fallback。因此成功统计直方图合法索引为0..29；失败私有 tape 可真实记录30次，不丢最后更新。

零次更新成功返回时，$L=t$，方向是 $D t$，并非额外隐式求解。root 的初始 guess 在本新局部场入口明确未提供；若未来调用者提供额外独立 guess，该 guess 的方向未声明则报告接口错误，不能暗设为零。原 noJ 外部调用、冷初值和 warm 算法仍走其原代码。

切向本身仍以 binary64 数值运算实现。因此本次不预付 IEEE 离散舍入映射导数、邻域内分支不变、准确 root 的导数、连续 ODE 导数或严格舍入误差界。也不以 shadow 值逐词对拍作额外数值门：两处预览 Object.is 数值对拍已删除；AD 为形成偏导所需的局部 value 可以存在，但不替原 primal，也不以它与 primal 的相等阻断计算。只保原完整来源/形状/tape合同和实际新方向的有限性责任。

## 4. 原源的最小可逆安装

原实际生产模块：

| 原文件 | SHA256 | 本次作用 |
|---|---|---|
| 78718-tail-fourier-root-momentum.mjs | cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88 | 可选成功/失败 root tape；不改原 $F,C$、停止、试步或 solve 数值正文 |
| 78718-tail-fourier-root-split-engine.mjs | a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372 | 明确包入新完整变分 engine |
| f6tail_momentum_split_flux.mjs | 5d77ca058adb634547c91998002eeffb9de5395a9e1e130f7edd4fa65014f578 | 原 split RHS 的值仍原调用；新切向微分同式 |
| 78718-tail-tangent-core.mjs | ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 | 原 evaluate/32×10/阈值/终检；当前修正入口接原 R273 |
| 78718-prefix-tail-tangent-fourier-worker.mjs | 36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a | 原协议、warm、last、响应及额外来源/失败标量记录 |

Node 实际顺序是已有 capacity import → 新 finite-trace loader → 新 R273 correction hook → 原 worker/config。base client 原八项启动合同仍真实核对；不会因只改标签而漏装 loader。原1cdf协议复制为独立有名 source，仅增加明确身份及新文件闭包；其 complete response、cache/audited request 行为保留。

loader 对固定源 SHA 和唯一文本锚逐项核对，保存每段 before/after/count 与生成源 SHA。逆替换逐字恢复原 capacity-adapted root，split 逆替换恢复原 split wrapper。capacity 的原 $M\le64$ 扩展仍由既有07d45负责；新 loader 只接它实际给出的源，不独立再偷偷扩维。所有变换发生在 Node 模块装载内存，磁盘78个原文件不改。

原 root 的可选 observer 记录实际返回、真实被接受更新与原尝试分支。私有完整 factor/tape 不出必要摘要。每个 call 和末会话的 source manifest、加载标志、计数、异常位置另存；成功回执不由 source match 自动推出。

## 5. 全部226/224、RK、mean 与端点338责任

新 flow 保原 noJ RK 的四次 field 次序和所有状态表达式。特别保留 $h\,a/2$ 的原运算分组，不改成 $(h/2)a$；保原 $k/\mathrm{steps}$、$1/\mathrm{steps}$、cusp helper 的切分、重复端点/排序及原未切分分支的 $h$。每次四个 primal field 先全部完成，再从其实际 tape 形成四个完整局部 Jacobian 并传播 tangent；切向阶段不重复执行 root/RHS/profile，observer 不持有下一步可变数值数组的别名。

224形状列全付；局部 mean 行224保 $r_x w\,D L_0$，行225的形状方向为零但其 primal $r_xw$ 保留。两条 mean 不回馈 shape，与原方程结构一致。完整每 stage 返回226态、226×224切向，然后原 tail core 继续处理输入/输出缩放、cut/far和576段链。

这些完整局部列不能自动冒原112边界响应。原 tangentGraphAtCut 的完整 graph 传播、原 heightJetJacobian、原物理 cutJets、原 final audit 都还必须实际执行。原 $(3M+2)\times M=338\times112$ flat 矩阵顺序保其原返回约定：slope112、second112、两条 mean-correction 导数、height112。响应还需原 height/slope/second 各112及 meanSlope、meanSecond、meanSlopeCorrection、meanSecondCorrection 四标量全部有限。

旧 numerical-tail-slope-jacobian 的已发表首 slope/mean-slope替换路径继续消费当前 engine 的新局部 rhsWithJacobian；原 second-jet及 mean-second差分规则、原 finite difference step、原 full physical audit 不改。这里没有声称已实现完整二阶有限 root trace AD，也没有把旧64 J/audit贴到当前状态。本次真实链如未到终点或终检，相关项如实缺失/false，不能由 complete_local_jacobians 计数推得。

## 6. 当前 R273 与同 owner 的完整正 $H$ 链

每次修正先由同一个当前 worker 生成这次 $H$、全部577×224状态、576完整新 withJ、原 $r,\sigma$、cut 和 far。新 system/QR 两源只改来源绑定/元数据，不改原完整链因子数学和精确残差 kernel：

- factor exact_20261114_native_damped_chain_qr.py，9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33；
- dyadic exact_20261114_native_allrows_dyadic_residual.py，0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f；
- $\eta$ 原 CLI 字符串 "1"，exact workers2，factor上限2147483648 B；
- 全129248原行、全部577个 penalty node blocks，不删224列或任一 mean/端点责任。

原 exact ledger/affine最大值只用于读回，不成为原 native 接受门，也不能当作原 noJ 真导数。原十档实际 noJ 必须逐档求值，只有原严格 norm 下降和其余原条件才更新当前状态。195 不加172的同点额外 noJ baseline 或额外 $2^{-10},2^{-11},2^{-12}$ 诊断调用，避免混入另一实验路径。

$H(s)$ 仍先真 $H=0$，首正 $s=1/64$；接受后增量乘2、上限1/4；最多64个请求包括零与最终J。中间 jacobian:false 仍执行内部完整 withJ；$s=1$ 直接使用原 $H_*$ 的112字词并请求 jacobian:true，bootstrap不提前冒 final audit。原 warm 失败按原 cold fallback，不造非零接受锚。

沿145策略，首次正 $H$ 的身份完整原数学拒绝就结束本实验，不重复124的缩高序列。仅已实际读到、绑定该请求的原 failure response 才可称原数学拒绝；新方向非有限/源加载/协议/记录/资源异常均独立 partial，失败不提升 last。完成 $H_*$ 后同一 live owner 继续原3方向×3步 FD、原完整 fullDN及最后 fresh J/audit。

## 7. 原接受门和资源计划

| 层 | 原配置/预算 | 真正责任 |
|---|---|---|
| 全部物理场 | $M=112,N=2048$；material/physical angles4096 | 完整高109、core112、全部physical/mean和设计参数 |
| 增广 BVP | 每 node453；left341/right112；max_nodes1200 | 原全部方程与边界，非降维替身 |
| fullDN | outer8、原inner17 | 原域、RMS、merit和全部原接受条件 |
| 原 native | max32方向，每轮原10档 | 原 $2\cdot10^{-9}$、D/S/A、strict residual下降 |
| 原误差门 | collocation $10^{-6}$、BC $10^{-11}$、FD $5\cdot10^{-5}$ | 不放宽、不另加数值对拍或诊断门 |
| R273 | eta1、2 workers、2GiB factor | 原完整系统及实际global remaining时间 |
| 科学总墙钟 | 18000秒 | 从 runner 启动科学 child 前计，包括初猜、preflight、全部 $H$/J/QR/FD/fullDN/audit |
| Actions | science step330分钟、compute job350分钟 | 停止/读回/清理必须明确，不能声称资源上限保证全部32完成 |

runner 将同一 monotonic absolute deadline 传给 child；本实际 Linux Python time.monotonic 与 Node process.hrtime 所用时钟口径明确。新方向循环周期性检查此 deadline，原 R273仍按当时剩余量 clip并保原60秒transport余量。wrapper到时停止自己创建的新session；18000秒没有排除首次当前J或前置preflight费用。

完整224列的逐 root、逐 Cholesky、逐 RK代价可能很大。本接口没有未执行的速度估计，也不保证首次完整withJ、32个方向或finalaudit一定在该job完成。若未启动、被截止或未完成，保实际最后phase/原异常及已观察trial范围，不能把未访问后缀写为失败。raw清理后不能从SHA续接现场；后继若需重现，必须从原输入依同序重新计算，或另明确同job可用现场协议。

3b8 rules runner 不修改。显式以当前已读根21bd/topicbff替换其静态baseline，保每2700秒真实pull/rebase、规则变更停止和原HANDOFF唯一“规则同步记录：”。source checkout保持触发SHA；token只 process env/git CLI，不写文件、不打印。Git设置merge.stat=false避免原删raw diffstat；原发布路径只有root管理。

## 8. 进程所有权和清理先后

runner创建科学child时使用 start_new_session=True，并记录同次boot_id、PID、start_ticks、PGID、SID；wrapper自身也记录启动身份。原3b8父组是共享group，不能据其PGID粗暴杀组。本wrapper接SIGTERM/SIGINT只记信号，在主循环向已确认own child group转TERM，再按实际存活同身份成员KILL并wait。返回码与原科学接受状态分列。

always reader 在读取可能被写入的科学文件前，先核上述原receipt。仍在运行的本request wrapper只按准确PID/start/命令及目录核对后停止；独立child组按同boot、同leader start、同session/uid和成员启动范围确认，才可终止。PID重用、/proc读不全、来源不清、wrapper/child仍存活均不声称静止，读回70且保raw到runner销毁。

reader只在读前/读后均静止、所选原JSON/JSONL/必要错误字段均完成、单份摘要完整时写 readback-complete.json。workflow清理前再核marker的request/recipe/reader/summary字节、run/source、namespace、当前own quiet、原rules parent启动身份已消失及scalarstep success；只删本request整个临时namespace。失败或未知任何一项则打印skip原因，不删除未读/仍写原件。这个生命周期判断不是新的 native 数学门。

## 9. 单份必要原输出合同

唯一reader是标准库JSON/字节/进程metadata程序，不导入科学模块、不重算 $F,J,A\Delta$、FD或任何norm。整数计数相加只用于实际统计元数据，不当科学误差界。所有原二维/三维数组、factor、113维root tapes、全129248 exact行账都留Actions临时，仅给原文件或canonical对象身份。

必要输出是一份ASCII JSON，硬上限90000 bytes：

- 原process/规则终止、实际phase/预算/错误、source/四inputs/配方与proof身份；
- 原preflight失败地址及域记录、原FD顶层误差/阈值/两组门、原fullDN状态和实际接受字段；
- 每个真实协议响应的请求 $H$ 身份、原residual/lastIteration、完整返回数组与J的原身份/数量、四mean、原audit标量；
- 全部原native trace标量、每条真实十档trial的call/iteration/trial/step/baseNorm/kind/trialNorm/error和stage/rawCell/rawSegment等原地址；
- 每个已观察iteration列原十档中有record/无record槽位；缺记录不伪称已拒、未观察的新iteration或inflight call不编造；
- 每次当前R273的snapshot/J/δ身份、原QR退出/错误、exact原打印最大值及其原行地址、闭合raw退场回执；
- 新trace的实际normal/fallback/zero-update及root/backtrack/已微分更新/局部J计数、0..29成功histogram、各engine来源；明确累计调用不是独特状态或全stage完成证明；
- 全部必要错误位置和有界原错误文字、其完整原log字节身份；不声称已转出完整stderr、完整root tape或大科学树。

若必要选择超过90000，reader写明 summary_complete=false/transport_complete=false、原大必要投影身份、本地保留scope并退出70，不拆包或编码树绕限；数学原结果仍独立。报告job只打印同一短JSON及bytes/SHA，不重新从大输出推断成功。首次原summary失败的pipeline不因reportjob绿色冒科学完整。

帧名：

    BEGIN_REQUEST195_FINITE_TRACE_R273_NECESSARY_SUMMARY
    END_REQUEST195_FINITE_TRACE_R273_NECESSARY_SUMMARY

hash口径是紧凑ASCII JSON body，不含分隔LF；临时scalar-summary.json另加1 LF并由marker独立核。必要原字段之外，完整大数据不上传artifact/Release、不进Git，不把其hash当下一次已恢复输入。

## 10. 实际 CLI 与文件路径

科学wrapper由原rules runner启动：

    python -u root_20261115_six_control_finite_trace_r273_run.py
      --request public-six-control-finite-trace-r273-request.json
      --recipe actual119-batch3-finite-trace195-lambda0p001-recipe.json
      --inputs-directory <owned mathematical-inputs>
      --source-topic <fresh original-public-source topic>
      --out <RUNNER_TEMP>/visible-original64-finite-trace195/execution

新full112 driver收到新 --tail-client 与其明确SHA；参数、旧core入口及原四inputs不默取默认值。runtime原record仍在 science/full-DN/true-tail_*，新R273子目录为 science/full-DN/true-tail-finite-trace-r273，call-XXXX/iteration-XXXX保持原一次请求/迭代身份。source manifest和每call finite-trace-native-return.json不与旧145同schema混用。

always必要读回：

    python root_20261115_six_control_finite_trace_r273_scalar_readout.py
      --directory <owned namespace>/execution
      --request <fixed request>
      --recipe <fixed recipe>
      --rules-directory <owned namespace>/rule-sync
      --compute-outcome <original step outcome>
      --out <fresh owned namespace>/scalar-readout

未运行前没有actual run/job、原H、当前J、首次接受或最终native/fullDN结果可填。实际195结论预留R412，不以源码交付代表科学成功。

## 11. 来源差异与静态范围

七薄源的完整差异 thin-seven-relative-to-original145.diff 为77804 B/SHA5407e02dadfffb07e5d4e960bb7edb981120a90a50ea902918bbb9cf03a47ad2，blob66e246f53692505f7549ba231813e0cfcab26c11。base协议是原1cdf显式来源复制；current system/QR数学保持；hook只在原修正/安装及原返回记录处接新身份。driver的profile、prepare、original_full_solve和原数学门沿原145；新的protocol identity不能冒旧accepted/native状态。

runner完整diff相对已真实172的442ab034，未带172的额外secant科学调用。reader是独立新标准库源；recipe/request相对实际145，workflow相对真实172（含既有rules/进程读回接线）给完整diff。预览 recipe 的模糊225项标签已定向改为 root_vector_dimension=113 和 complete_Gram_cosine_moment_entries=225，并同步request/wf pin；数学源没有因此变化。

本地只做文本、原JSON、字节身份与精确replacement/diff；没有导入科学模块，没有执行AST/compile/数值/fixture。Actions既有source setup会对新实际源码/inlinePython执行语法解析、bash -n和Node --check，再执行正常流水线；未把语法或来源核对描述成数学接受证明。相关diff/清单是可从源重得的临时材料，正式仓库只需下面完整源、参数、工作流和本接口。

## 12. 最终发布映射

除workflow进 .github/workflows/ 外，下表全部源与配方/request进 topics/visible-flex-larger-amplitude/computations/。七旧预览或带多余末LF版本均由表中精确bytes/SHA替代；表中的blob只创建对象，不移动ref。

| 文件 | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| geometry_20261115_original64_finite_trace_variation.mjs | 11427 | 742ab15a2168084167eeab9879a074ee1cd586d33f324e837223134a8cbf9705 | 74f63fd0b40e095508de840700ad3bbc002ef7b6 |
| geometry_20261115_original64_finite_trace_flow.mjs | 9248 | a7a90668a7d2f4df93e0bd03d665f439dab2fb2461bedf544725cd01c2a7b470 | 91552a0e5820bb0fa98d1effac0a5cd258ba2ecf |
| geometry_20261115_original64_finite_trace_loader.mjs | 10180 | 55b2a4a344ae2eb7d78f26b7954b20f9cbe4e4969588bf3a236e7828d6f299ae | a8b8bf2cf0af4fa16ebf414bcd10e9041b7a42bd |
| exact_20261115_original64_finite_trace_tail_base.py | 19972 | 4f22690b9b72c8b2eaee919200b5329cd74342a9394ec8aaa49c0e8e10e18999 | 79a06327478ace5cc78d51edc3218f97982fd815 |
| geometry_20261115_finite_trace_r273_tail_client_hook.mjs | 53723 | 53d614393600affd5e4778c4966b94de0cf3dde14883d4b9bb616e33d604e123 | 6da913352c5a26403144d7e38f44ee5fdacdea7f |
| geometry_20261115_finite_trace_r273_tail_client.py | 20168 | b5dd4d8171e1f7452eba036d0c6518b76176bcc4420ba84c4e8d7357a143a2c8 | 56906451cdce14de4b77e987ad44bd3cff26a647 |
| exact_20261115_finite_trace_r273_current576_system.py | 29153 | e78b220aa620c45fbc6c4719915a89af61e8afeb3599b272575e999de374d27c | f21a310bc8abad5dbf30051cce7a87caf2aea041 |
| exact_20261115_finite_trace_r273_current576_chain_qr.py | 21967 | c0997c9eee50ca96f2e50785251dec966cb5560a541dfc15c9fedd423911d309 | 0b90bfae3b855acd46e23bee054ab8e63141f5b2 |
| geometry_20261115_finite_trace_r273_height_path.py | 23915 | 1194400acb9060e913e1fd8746b8fefa631b4e5cdd17c030564cafa1166d55af | 523807f0ccb8ffc1ab985956abd5f55f52a125d0 |
| geometry_20261115_six_control_finite_trace_r273_full112.py | 48523 | b468c64860272c35f523bcfc52e36ada0833e003a586eeb1e21ae574fe95df48 | 3ee795dff597d0a5bba3925a88d934c35afc6ef1 |
| root_20261115_six_control_finite_trace_r273_run.py | 14387 | 55acd82e3f0585ffce63911851fe4b5e65cb537de8b7c0baf7a32e150789d8e4 | 682c3f860daa33ae3c294c83a0496e077bb32c2b |
| root_20261115_six_control_finite_trace_r273_scalar_readout.py | 38967 | b6d22546b7258e0dc23f016238d7e0ed4769fa35f602d3db503f49f6ca45bbd9 | 7fef7ee139c709d7e47c3a1a0a04b4b684207d29 |
| actual119-batch3-finite-trace195-lambda0p001-recipe.json | 7985 | 70145aca5431029987f5c79d9fcd9830e5a4112c1e17d5626a9a2a139e93f124 | b9d828ef68c520e48a710e8cdcd360f337bc72eb |
| public-six-control-finite-trace-r273-request.json | 33381 | fd65aeff4517f481f1a78ad23c2b3514c9df6ec58c433d693788de5df000787b | fb5b27de14e7dab1ab6d3803d227d30122b67563 |
| visible-larger-public-six-control-finite-trace-r273.yml | 29958 | 0a18de732a08670b8a65c4ab61436655396066081aa7fba057fbddc9c507e4c2 | f6503b0a2335c1449810e89238097c9135c791d2 |


本接口的存放路径为 notes/2026-11-15-request195-original64-finite-trace-r273-complete112-interface.md。源/配方/workflow是可重算工作的可执行定义；本接口不保存raw、不给未来成功回执，也不要求另一个fixture或独立审核门才能执行已授权195。
