# 第145轮：原 warm 下的当前全576 R273 修正、完整112高度路径与原全场责任

本接口登记独立可运行源码、明确输入及一次有界实验。尚无第145轮运行号、当前场、方向、接受步或最终物理结果。全部科学执行只发生于本公开库 Actions；本次编写时终端不可用，未运行 Python AST、Node 命令、编译器或任何数值函数。已经完成的检查是完整源文本、JSON、哈希、精确 diff，以及 hook 文本去除静态模块包装后的 V8 语法解析；该解析没有调用 hook、worker 或构造器。

## 1. 实际问题与本次改动边界

R315 的实际124保留了原冷启动、原 tangent warm 和局部图修正。在真实零请求成功之后，13个已完整返回的正高度请求均在其原十个 nonlinear trial 被 D/S/A guard 拒绝；位置同为 stage0、rawCell0、rawSegment8。各正请求的当前完整 withJ 基点已经返回，因此失败不能概括为“基点没有算出”。第15号请求被规则同步发现的新 README 中断，不能补成另一个数学拒绝。

本轮保持实际124的六个设计系数、lambda=.001、原四输入、两 ready、原78来源及原 warm 路径。只把原 nonlinear loop 内唯一的局部图 correction 调用换为当前完整系统的 R273 候选。每次候选使用本次 H、本次 states、本次已经实际返回的576个 J、原 residual/cut/far/scales。不存在旧 H、旧 J、actual28/57/61/73 或124 checkpoint 的缓存复用。

这是修正策略的独立实验。原 root/RHS/flow/withJ/noJ 的 binary64 实现没有改为128；也没有把原 stage J 改称有限迭代轨迹的准确微分。R283/R305/R314 的其他微分或后验责任不在本轮自动支付。

为避免重复已见的13次缩高度拒绝，本轮保留零→正的路径，但在**第一个身份绑定的正高度原数学拒绝**后停止，不再减半高度重试。该停止规则限制本次实验的访问范围，不替换 native 内部十档试步或其接受条件。

## 2. 真实参数来源与全部输入

recipe 只保存真实来源的参数，不冒原 status、接受场或 native parent。它使用 actual119 第3批末点：

$$
(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3)
=(0.41654476801167684,\ 0.23884336093393582,\ 0.5270922473095916,\
-0.13437878055563054,\ -0.005765450212224129,\ 0.4141025261683763).
$$

来源 run 43693462669，source 6fffce1f36e876f3b08a1c73198a7fde259d94d6；原 status SHA 10c31f1da398f537f1c9dfb19a162bb6aadb30e7e57fddafffebf7a9a60c08e4，原紧凑摘要73546 B / 4ec08e23ea41bc3f443f04f613270163c9e8624d8b4172ab2a35f998b75acf5a。仅采用其 literal 六系数，前三个 active、后三个固定。lambda=.001 是显式实验参数。低三阈值没有被加入该非零全场入口的前置门。

四数学输入从公开历史提交 8bd267107cc8710d371f3b62c02986655ac965b0 的原 blob 恢复到 RUNNER_TEMP，逐 size/SHA 绑定：

| 输入 | 完整字节数 | SHA256 |
|---|---:|---|
| accepted / 原 free3 stage00 | 2614352 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared / 原 prepare112 | 4220043 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| tail anchor / 原零响应初猜资料 | 6815 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| 原 T112 config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

完整公开相对路径写在 request.inputs；没有通过已删 raw 的 SHA 伪造恢复。旧零响应 J 只承担原初猜职责。新 H_star 必须由新的完整 preflight、实际物理场及原 true_height 形成，不能从R315引用的几个 H 分量拼成目标。

同一历史提交还恢复原两个 geometry ready：

- ledger ready：109004 B / 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6，Git blob 4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3。
- stored ready：29774 B / c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d，Git blob b6c44fe237750f13c8b10366f15525b481a74e09。

它们通过原有 VISIBLE_FLEX_FROZEN_LEDGER_READY、VISIBLE_FLEX_FROZEN_STORED_READY 槽位消费，是几何输入，不是本轮已经接受的非零尾场。原78来源恢复器保持11399783...的实际脚本和其完整 source-dependencies；不读取 HEAD 中已删除的历史 ready。

## 3. 八个新运行源与明确基线

新 client 是原 exact_20261114_true_tail_client.py（1cdf0e14...）的子类，保留原 constructor、ready/capacity 校验、协议、cache、solve 和 close。它只为原 Node 命令增加一个 --import hook，配置里不写 initialCheckpoint，也不导入任何已成功或失败的状态。

新 system、QR、hook 的基线是先前公开的 current576 live 实现。旧 live 的“completed61 literal seed”前提被移除，替换为**未导入状态的实际 worker session**；没有把旧成功锚条件放宽成假通过。

| 新源 | 准确文本基线 | 基线 SHA256 | 基线 Git blob |
|---|---|---|---|
| `exact_20261115_original_r273_current576_system.py` | `exact_20261114_live_current576_damped_system.py` | `9346c0a7e7c7f562d20b02126b82c8819c687a7575aea38258e9796cabb8db4a` | `1758fe3199fc0430884a51e7af037d39370f9dfb` |
| `exact_20261115_original_r273_current576_chain_qr.py` | `exact_20261114_live_current576_damped_chain_qr.py` | `ee174e8283f3b5454a8b3dbe751dbd4f41f4f0dba1bd9d240b627bd2748f889f` | `975c04053ef4e6dfc3208315bc98a6dca5841405` |
| `geometry_20261115_original_r273_tail_client_hook.mjs` | `geometry_20261114_current576_live_tail_client_hook.mjs` | `7e83b398fe0f8a8801700d50c640b1e97bc185ec07627468f94fc54de61a58f5` | `6d65ee892bfd211056635c16ae105a53da8ea52b` |
| `geometry_20261115_original_r273_tail_client.py` | `geometry_20261114_current576_live_tail_client.py` | `c9f3377748480d4905a32f7f858e2b9a5bcb8a697b7b7806ffc409e635ed1189` | `12b2c13d24fd0391eb62fb5fdf20969f6a564e3e` |
| `geometry_20261115_original_r273_height_path.py` | `geometry_20261115_original_tail_height_path.py` | `e830a1679908cdc0cdd8c1ecd5663bbf6b82b24a3d52e44cf678aedc227eee48` | `2af3d9c7bc801a1c2d0371e082005bc4504d16bf` |
| `geometry_20261115_six_control_r273_height_full112.py` | `geometry_20261115_six_control_height_continuation_full112.py` | `557f3aab83116c1d8eef83e4c83306e8058749ccdb56b2ec8808effd2e16bf21` | `63daafb270571dae55e1020cd7d06cc87675f71c` |

后两基线位于实际124提交 b1df8ec306e596256a317df925464af6acaa31c6。前四基线这次从公开原文件读取后，与既有保存的全文逐字相同；表列 Git blob 给出内容身份。全部文件位于 topics/visible-flex-larger-amplitude/computations/。

新 request 保留原124的全部103来源锁定，另加四个已公开依赖：

- `exact_20261114_native_damped_chain_qr.py`：`9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`。
- `exact_20261114_native_allrows_dyadic_residual.py`：`0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f`。
- `geometry_20261114_native_captured_band_correction.py`：`b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390`。
- `exact_20261114_seeded_zero_tail_client.py`：`a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776`。

再加本轮八运行源，共115 pins。原124/120入口、wrapper、reader和旧22e publisher仅保来源，不作为本轮执行入口；原 R273 9b95... 与 exact kernel 0bc8... 真正被当前新 QR 子进程加载。

已完成纯文本比对：

- system 从 def _json 到文件末，逆转 exact-context 类名后整段逐字等于原9346。完整 J 分块读取、全部输入导出、整数原行 context 和 worst witness 的实现没有改式。
- QR 完整 diff 只改系统类名/来源、schema 和临时保存标签；因子类仍逐 SHA 加载9b95，原完整 exact readback 调用0bc8。没有重写 factor、normal equation、秩截断或省略原行。
- full112 entry 从 def temporary_paths 到 def main 之前整段逐字等于实际124入口。完整 prepare、profile、actual boundary FD、SharedNativeClient、original_full_solve 均在该段内。
- 新 path 保原 request/response/source/trace/trial 绑定及数学错误分类，只改新 client 身份和首次正请求拒绝后的路径策略。
- 以上是源文本身份，不冒本地 AST 或数值等价测试。

## 4. hook 精确改动与原 warm 保全

原 disk core SHA 为 ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3；原 runtime core SHA 为 f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f。

运行时只替换唯一文字：

    const cor=correction(ev,states,target);

为当前 bridge 调用，传入原 ev、states、target、scales、it、M、K、depth。原 internal solve 的唯一边界、evaluate 和十档 trial 源分别绑定 d7d063fe...、9725a6c9...、603924d1...；实际 instrumentation 保原文、替换文、哈希和精确逆向还原记录。Function.toString 不被伪造。

engine-loader 在原唯一 coreURL 编译锚点前插入该变换；worker-loader 在原唯一 let initial,predicted=false 后插入每次 request 的 context 记录。后者**不赋值 initial 或 predicted**。原冷初始化、tangent predictor、warm fallback、last 更新和最终 sensitivity 都继续走原代码。旧原 worker 与两个加载包装的实际 SHA 仍分别绑定。

新 session_origin 明示：

- imported_native_state=False；
- imported_response_cache=False；
- supplied_seed=False；
- original_warm_predictor_and_fallback_retained=True。

它同时保存本次 input/runtime config 和 source-origin 收据、完整 numerical source map 和数学配置。call1也不是外部 seed。每个正整数 native_call 的独立 request.json 保存完整112 height、Jacobian/audit请求布尔、negative-zero sidecar；当前 snapshot必须逐词匹配该次 request H。后续协议请求继续同一个原 worker/owner。

## 5. 每次 correction 的完整当前系统

每次只有原 withJ 已返回后才能 capture。保存格式例如：

    science/full-DN/true-tail-original-r273/
      call-0001/request.json
      call-0001/current-corrections.jsonl
      call-0001/iteration-000/snapshot/
      call-0001/iteration-000/qr/
      call-0001/iteration-000/returned-correction.json

示例编号只说明格式，不预定实际 call 或 iteration 数量。实际缺失或中断目录按原件读回。

snapshot 三个 schema 分别为：

- original-r273-current-native576-withJ-snapshot-result-v1；
- original-r273-current-native576-withJ-snapshot-context-v1；
- original-r273-current-native576-withJ-snapshot-arrays-v1。

十个原 Float64 little-endian/C-order 数组保完整 bytes、每chunk SHA、总 raw SHA 和 shape：

| 数组 | shape |
|---|---|
| base-states | 577×224 |
| stage-residuals | 576×224 |
| stage-out | 576×224 |
| original-scales | 1×577 |
| cut-residual、end-residual | 各1×112 |
| original-far-graph、physical-height、cut-target | 各1×112 |
| stage-jacobians | 576×224×224 |

J 保原每4 stage一chunk。rawNode 是实际九项 [0,72,144,216,288,360,432,504,576]，不能混同577状态节点。完整原 cells、profile breakpoints、portRatio/mu、graphs/gains/far、config/source都绑定；每段已返回的 meanHeight/minA/minD另作原值 metadata，允许原 nonfinite 分类元数据，不给 minA/minD增加 finite 门。

capture 不另调 RHS/J/ODE。cut residual 是本次 states[0]−target 的原 binary64表达；不假定初值严格zero cut，也不将cut或far方向投影。每个请求内 H/target/scales/far身份不变，每次 iteration 的完整 states/J/r仍从实际本轮取得。

输入 binding schema 是 original-r273-current-native576-complete-linear-system-binding-v1。它明确区分 snapshot receipt、session origin、current request、native_call、iteration、sequence、当前 state SHA和新矩阵身份。身份 metadata含本次来源，不能仅凭两个模型metadata SHA不同推断数值矩阵不同，反之也不以旧schema套新当前点。

## 6. R273 原方程、罚项与诊断范围

变量是全577个节点的224形状分量，节点顺序不重排。原线性行是：

$$
r_{\rm cut}+\delta Q_0,\qquad
r_n+J_n\delta x_{n+1}-\delta x_n\quad(0\le n<576),\qquad
r_{\rm far}+\delta\Pi_{576}-G_{\rm far}\delta Q_{576}.
$$

stage n 的入口是 node n+1，出口为 node n。原 row scales依次用 sigma0、sigma_n、sigma576，共129248行；原577个正scale全部保留。

R273沿原sigma列坐标 z_n=delta x_n/sigma_n，对完整行的原scale加权二范数和全部577个节点的 eta²‖z_n‖² 求同一个已冻结 square-root 候选。eta CLI明确为字符串1，不是自动扫描或隐藏新 ridge。它改变修正策略，不改最终残差方程或native tolerance。

原9b95完整动态因子类、577因子/全部纯常数、原边界形成值与factor-index均产生；原完整129248行整数/dyadic readback、formed-model/gradient等诊断也保留。它们是当前保存有限矩阵及保存有限delta的报告，不等于非线性重新evaluate的残差，不是原native接受门。原科学不调用 normal-matrix/Riccati inverse，也不通过秩截断省掉弱方向。

输出 schema：

- complete-native-original-r273-current576-damped-square-root-direction-v1；
- complete-native-original-r273-current576-damped-direction-v1；
- complete-native-original-r273-current576-damped-direction-arrays-v1。

child stdout/stderr只进每iteration的独立文件，不写原worker JSON协议。child完整退出后，hook验证该点result/binding/manifest、完整577×224 delta/negative-zero sidecar和checkpoint身份，再还给原loop；factor/exact/L2报告不决定是否接受。returned_maxChartCondition=null 明示本新候选不计算旧图 chartCondition；不将其填0或假称原局部图已良态。

## 7. 原十试步、路径及full112最终责任

每次 correction 返回后原 ten-loop仍按原十个alpha逐一重新noJ，原 guard/strict norm及失败报告原文保留。原迭代上限32、tolerance2e−9不改。全部112Q/112Pi、226维flow中的两个mean、cut/stage/far都保持原原生范围。

路径策略完整列在recipe/request，原零请求先行；第一个正值 s=1/64。只在原 native 真converged后晋升 last_converged_s及调用者记录；原worker last的更新仍由原worker负责。成功后下一increment×2、上限1/4，s达到1时直接传原H_star完整数组，不通过乘1另造近似目标。

中间请求 jacobian:false 仅不请求返回 endpoint J；原native内部fresh withJ仍执行。s=1必须 jacobian:true。任何数学拒绝必须从真正原response、配置、source、current H和原trace/trials完成绑定后分类；不依据Python异常文字或空response猜成mathfailure。

第一个正高度原数学拒绝使本轮path停止；protocol/record/QR异常停止为明确partial。不能把新QR exception当原DSA拒绝。零请求失败单独记录。最大64 bootstrap calls和总墙钟只限制资源，不给不存在性结论。

s=1真通过后，同一个 SharedNativeClient/worker继续：

1. 原真实current-H完整338×112 endpoint response及完整边界 FD；
2. 原full-DN main，338物理行、完整112core、3active控制，共453状态，left341/right112；
3. 原RMS/material/域/边界、17 inner trials、8 outer预算；
4. 最后fresh native J与原audit，以及原physical final cut audit。

collocation tolerance1e−6、BC1e−11、FD5e−5及原native2e−9不变。原高109自由core没有因初猜低三简化而删除。未支付的phase保持缺失/false；中间H收敛、完整QR成功、独立readout成功都不能写成full-DN或完整闭曲面成功。

本轮并未将最终原 graph-based heightJetJacobian/sensitivity改成R273边界导数。它仍必须真实执行并通过原责任，可能自身失败；此时不得借已成功的 nonlinear correction填充 endpointJ或audit。也不把既有旧64 J或audit贴为新128结果。

## 8. 预算、完整临时产物与清理边界

wrapper的18000秒绝对科学预算从启动独立scientific child前开始，包含新的prepare/preflight、零请求、所有H请求、withJ、QR/exact、FD/fullDN和最终audit。不是每次correction另得18000秒。

client把同一monotonic deadline的实际剩余量映射到本机Unix时间，hook启动新因子前读取剩余秒数，传给原factor budget并留60秒transport余量。外层wrapper拥有实际科学进程组，墙钟/规则信号时先TERM后按原宽限KILL。factor局部budget不能替代全局绝对stop。没有预承诺32×10或最后audit能在本run全部完成。

资源参数：Node heap6144 MiB、exact workers2、factor raw上限2147483648 B、BLAS/OMP/MKL线程各1；job350分钟、science step330分钟。每个闭合correction已知固定binary704387088 B，包含原两个formed-boundary-rho；它不含可变整数ledger/JSON/其他full-DN产物，不冒完整磁盘上界。

同步child成功退出、完整delta已在内存验证、returned-correction和journal写完之后，后续原native仅使用内存delta，不再读该correction的线性payload。此时对 snapshot/large-arrays 与 qr/large-arrays 全部文件逐bytes/SHA清点，保存完整inventory和retirement收据，再只删除这两个闭合目录。原states及delta不被改写。因子、常数、exact ledger是先真实产生再清理，没有省略计算冒已完成。

retirement异常只记录清理失败，不改已经完成的候选，也不作为native拒绝。未闭合/失败child产物留至末readout；always cleanup随后只清本request的RUNNER_TEMP树。所有recomputable raw、完整field和factor都不上传artifact、Release或Git。旧frozen helper中历史descriptor标签不授权新上传；本轮顶层保存合同明确temporary-only。

## 9. 原值读回、失败传输与90KB边界

client在每次原solve返回或抛错后，将实际closed correction journal逐行打印为 request145_original_R273_correction。大记录显式标 summary_complete=false 并保原record size/SHA；不把被省略字段变成空成功。

新reader只读已有JSON/log，不读取已删除大数组或重跑模型。它分别保留：

- 原height path全request主表、完整原trace/trials/response与warm/fallback事件；
- 每correction的实际H/state/matrix身份、withJ原norm/minA/minD、eta、完整QR原summary、factor计数/formed model/exact读数；
- 真正child exit/signal、原stderr/stdout文本范围、bridge-failure及原checkpoint/delta描述符；
- 完整临时raw清点/删除receipt的scope；这些metadata不冒新数组字节审计；
- 原endpointJ、boundary FD、fullDN/finalaudit是否实际返回，以及原全部失败/partial标志。

reader还按实际iteration目录补充被外层信号中断、尚未写journal的点；没有returned-correction就不称方向已经返回。每个额外compute事件也有明确89KB范围，超限为省略记录而非造成功。

最终紧凑JSON≤90000 B，经GITHUB_OUTPUT传给独立report job。首次降级即 summary_complete=false，明确被摘要的section及原完整对象哈希；极端情况记录真实transport_error，绝不由readout成功推断scientific成功。hash口径是compact UTF8 JSON，不含打印分隔LF。report job只打印这一个摘要与bytes/SHA；主控需要时可再读compute事件。原重新计算数据不作为新长期附件。

## 10. 实际CLI与工作流

科学wrapper：

    python -u root_20261115_six_control_r273_height_run.py \
      --request public-six-control-r273-height-request.json \
      --recipe actual119-batch3-r273145-lambda0p001-recipe.json \
      --inputs-directory "$VISIBLE_MATH_INPUTS" \
      --source-topic "$VISIBLE_SOURCE_TOPIC" \
      --out "$VISIBLE_BASE/execution"

其科学entry收到四个恢复input、明确新client及SHA、原source-root、jac_workers2/max_nodes1200/material_angles4096/physical_angles4096/node_heap6144/outer_iterations8。eta/exact-workers/factor-bytes由request里的明确R273参数传入子进程env，没有环境里未声明的科学默认实验。

新workflow是 .github/workflows/visible-larger-public-six-control-r273-height.yml，仅新request路径触发，独立concurrency、cancel-in-progress=false。原124/128/140不被取消或修改。Python3.12.14、Node24.22.1、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、所有action commit沿实际124锁定。

原3b8b6dd5... rules runner保每2700秒真实独立镜像pull/rebase及规则变更stop；其BASELINES只用本次checkout经Gitblob校验的完整README bytes显式覆盖。根预读pin21bd547f、课题bff8aea；H须≤10000B且恰一条规则同步记录。Git设置保merge.stat=false。science checkout不被规则镜像改写，token只进process环境/gitCLI。本次源码通过小文本集成保存对象不等于又发生一次真实pull。

工作流Actions开头进行115来源SHA/Python AST和新hook Node语法检查，它们仅验证输入程序是否可读可执行，不额外设置数学接受门。本次本地只完成源文本检查；不声称这些Actions步骤已经执行。没有fixture或人工审批等待。

## 11. 冻结文件清单

下列 runtime、recipe、request 位于本topic computations；workflow位于 .github/workflows/。每件都是一个完整小文本Git blob，不是文件分片；blob创建不移动任何branch/ref。

| 文件 | 字节数 | SHA256 | Git blob |
|---|---:|---|---|
| `exact_20261115_original_r273_current576_system.py` | 28284 | `3557608524becae2bbf1c2100af12c865082329efccbd5078008cb2c8591c101` | `201df7ef56490681985ea825172ffaeb2e7ac15d` |
| `exact_20261115_original_r273_current576_chain_qr.py` | 21836 | `d5d9874242499df7a79fe4411a420de0cfe8464c64c80dd9c18ec501d226a296` | `3c83010c02930241539f3a225bd5af8f9732dc3b` |
| `geometry_20261115_original_r273_tail_client_hook.mjs` | 46729 | `f13b0a0d3f7e6d3487f0eda92dc9e76117137ee106c9f33471e762e35c9106e0` | `bc95be5fd5edb50ff5b49d57ce24838f06e9a7ae` |
| `geometry_20261115_original_r273_tail_client.py` | 18253 | `2fe2c25233061de0fd89b7af72cba5ddd2e2d144889492ec42156f781c4828a9` | `53559673565da980e55a58bcfd9927f44644520a` |
| `geometry_20261115_original_r273_height_path.py` | 23355 | `73c62d94a60eb1ee2fd50d68c14d6af29c590729fcdb764c5c4036ca963305ed` | `59e0b294ecde023f1525fefb72fc2fd020eda692` |
| `geometry_20261115_six_control_r273_height_full112.py` | 46439 | `d1f21025a91234252c856cb15bf26ce48e2628e8fa92352a9d98ffd53b14a69d` | `e70e762a79f6ccb021e5a35f188552f1f9949e36` |
| `root_20261115_six_control_r273_height_run.py` | 9959 | `f5f86bbac39011ea18396aecd62db2af86a2f2ed787199523e0ac8cb3a89f754` | `533d2d4639e232b6c3c9155d6b48e67aaad0df27` |
| `root_20261115_six_control_r273_height_scalar_readout.py` | 37864 | `be629d07ce38ad67ea436f8ce1cf55b3484c06e5db7fff575ad755d4bac9d84d` | `4a1bea3d6b8a0d5abc7f93cd7fba9b706896e3f1` |
| `actual119-batch3-r273145-lambda0p001-recipe.json` | 5807 | `e9f724327bbe0303d1de4e832e2f56cd704cd71c6d396d5cfbc4eb00fb78ef33` | `a9f25e7b378a85798423e24cca608dd32ad317e9` |
| `public-six-control-r273-height-request.json` | 27494 | `8800b003bb21dc36d7d4a9739d9f0e8e9f16109754d2d4a9c8f628012a24c99c` | `ba40915842a86adc911aa2b8ad5e8b1f5edac991` |
| `visible-larger-public-six-control-r273-height.yml` | 17831 | `ee8c23ff2d31828416a2d21fd6b5ddc2fe1db0df0efe8cff84e8f12c9a494904` | `e6240358da0aa6714a1ce902aa1cae32b481914e` |

完整相对diff的基线为第3节所列原件及实际124 wrapper/reader/recipe/request/workflow。diff和静态检查可从源重新取得，不是不可替代的科学数据，也不是第145轮接受的附加门。

本接口仅给出尚未运行的第145轮可执行合同。实际开始、原拒绝、工程失败、资源中断、当前H端点成功或最终full-DN结果，均待原Actions记录逐项决定。
