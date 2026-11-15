# R353：actual166 完整37查询的仿射区间证书与点态 Hermite 分解

日期：2026-11-15。性质：真实公开 Actions 原结果读取与字节核对；本结论没有在本地重算多项式、范数、矩阵动作或科学模型。

## 353.1 结论与准确范围

Request166 已实际完成原37查询模型、在新warm上的原FD和独立R334诊断。原模型接受 α=1/8；当前固定权重 merit 从43.363003729098274变为43.33605694766103。原native、非线性fullDN和最终闭场接受均未支付，不能用工作流绿色代替这些门。

新诊断已完整处理75776行、每行9个准确多项式系数与17个原二进缩步，完成148份真实查询点态比较及148份完整453分量Hermite恒等式。α=1/8及所有更小的13档，完整75776个仿射参考闭区间均取得严格正性证书；α=1、1/2、1/4各有端点反证，并各保350、76、4行区间未决。没有未访问的仿射行，没有资源截断或诊断异常。

最接近原接受步的α=1/4，原完整线性reserve仍为正；但保留完整非线性域多项式P的仿射查询参考已经在12个角行失去严格正性。其坏行集合与真实查询的12个坏行完全相同，分别属于已选LEFT464和MID471。因此，这次最近拒绝的存在不需要归因于遗漏查询，也不需要仅靠Hermite余项才会出现。它没有证明Hermite余项可忽略：α=1时仿射参考另有4个坏行，而对应真实查询没有失域。

全部Hermite分解仍是四个实际返回α上的点态恒等式，不是沿α整段的真实RHS二阶余项包围。这个剩余责任对应[R354](R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md)；R353不把[R334](R334-exact-domain-clearance-polynomial-and-Hermite-defect-transfer.md)的仿射证书重标为真实非线性路径证书。

## 353.2 唯一实际运行、来源与计算预算

- run：43734326402，https://github.com/Rogerhu12/math-research-public/actions/runs/43734326402 。
- 固定source：c3a7531db21286c7b4dec98904f8ac4a020dafa4。
- compute job：132873459541，所有原步骤success；原规则runner记录16:14:33 UTC开始、16:32:45 UTC结束，science_returncode=wrapper_returncode=0，README_change=null。
- 完整官方compute日志：3139676B，SHA256=0a9a3426e74a64e189cfdfd86e8b1df2c2323464bb6d226d1990df4901d04e8d。唯一读取一次，没有下载非终态日志或另取旧158大原件。
- 原model进程893.818396783秒；原新warm FD进程22.47191702500004秒；独立诊断进程130.997258053秒，诊断自身记录130.65817317799997秒。
- 完整pipeline记录1092.3843730869999秒，global_science_seconds=6000、diagnostic_seconds=1800、cleanup_readback_reserve_seconds=180。三个子进程均exit0，external_resource_deadline_triggered=false，pipeline.exception=null、resource_partial=false。

原模型仍为λ=270、LSMR200、projection200、17档原回溯、working-row512、dual200；原完整A/AT/H/C/outside恢复、全部域/RMS/真实merit门与原FD未改。只有后置观察绑定修复和独立诊断拥有新身份；没有让诊断成为原模型接受前置条件。

实际source检查记载97项：原90项、原批次worker1项、158来源3项、新capture/consumer/orchestrator3项；三参数文件不变。新三源分别为：

|源|SHA256|
|---|---|
|geometry_20261115_R334_thirty_seven_bound_return_capture.py|e32e941648cc35aef45f4f19ef050f90798e2ca0759b887afc2fff5b782a962b|
|exact_20261115_R334_thirty_seven_bound_candidate_diagnostic.py|6171fbbbbb79457751b7ba8a26c47c111ba5b1f4f91db8170689441df865eb00|
|geometry_20261115_R334_thirty_seven_bound_same_job.py|0979811b4d2a3bf60cd2e4ac6fbc24ee89327c7eb3cc65934567eea28e566778|

原37 domain / warm / observer / FFT / full-angle engine分别绑定2e189fbf…、293045c6…、2f70133e…、973898fc…、7d75a44a…；准确完整hash在上述request的97项闭包和原result.original_scientific_source_bindings中。request SHA为34d8773014637fb30f0dc3dfaf6ef5ef8ff66927901a134c638e42f88a04928c；基础155 recipe SHA为f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea。R334 proof使用已发表2fd386b8410de271142187cd8911ceb073673665faa0baf96bc8d2b7822b6602。

父仍是可恢复的actual98原31 warm/status，不是已删的141、155或158末态。实际完整ZIP809042943B/SHA9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a，run43677587785/artifact14147700690，中央目录457项。Actions核全ZIP size/SHA后只提取两件并核原成员CRC：

|父件|字节|SHA256|
|---|---:|---|
|warm-001.json.gz|4927052|b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67|
|driver-status.json|3379453|b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff|

未提取成员没有被冒称完成解压或独立数组审计。四个原数学输入按公开历史commit918fdb11dbb7a424b6149b405e2c7fab3cc0c737逐原件恢复：

|输入|字节|SHA256|
|---|---:|---|
|accepted.json.gz|2614352|b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff|
|prepared.json.gz|4220043|0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714|
|tail-anchor.json.gz|6815|e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51|
|tail-config.json|2161|01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5|

## 353.3 原37查询模型、四次实际试步和FD

完整B为21个LEFT加16个MID，每个2048角，共75776行；local support为物理node463至491的29个338块加3个标量控制，共9805维。原完整坐标236036，高109外部自由core及所有outside变量未固定成零。查询顺序保持：

- LEFT：463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487。
- MID：471,472,473,475,477,479,480,481,482,483,484,485,486,487,489,490。

相对原35仅新增MID489/490，同时捕获489/490/491端点；相对实际98原31父输入的query变化另按原报告明确，不把两种参考混同。

原四个已访问试步如下。其余17槽中的4至16号是在α=1/8已接受后未访问，不是实际试验失败。

|trial|α|原接受|线性β²最小值|线性reserve最小值|原预测unregularized merit下降|
|---|---:|---|---:|---:|---:|
|0|1|false|0.00042441358125799855|1.609823385706477e-15|0.19148805579721587|
|1|1/2|false|0.0006366194677895898|0.00021220679062899928|0.1024685216952421|
|2|1/4|false|0.0007427224110553854|0.0003183097338947949|0.0529153842967796|
|3|1/8|true|0.0007957738826882832|0.0003713612055276927|0.026877973010679432|

四次原方向斜率均为−0.21838603098375256。接受试步原实际下降0.02694678143724616、实际/预测比1.0025600303467597；阻尼惩罚不在实际merit中。

α=1时原MID487 RHS失域，原β²最小−0.07787348001852168，同时还有多个已选LEFT失域。α=1/2时MID471原β²最小−0.042792191869085006；α=1/4最近拒绝为：

|已选查询|query index|原最坏angle|原φ|原β²最小|原负角数|
|---|---:|---:|---:|---:|---:|
|LEFT464|1|54|0.16566992509164924|−0.2683086899521916|4|
|MID471|21|44|0.1349903093339364|−0.19167001275188889|8|

α=1/8时全部37个查询无负角或非有限角，原两组698点RMS检查invalid_count均0，complete_boundary_max=6.857449986338445e-9、constant_collocation_max=0。原最大physical collocation残差从0.00710763096028075变为0.007107481419522546，仍在interval461、原row155819；该行原冻结权重199.00690823502174，不以trial RHS重算权重。

局部QP原停止原因maximum-working-row-budget，最终stage511、dual200到maximum-dual-sweeps。原全linear slack最小1.609823385706477e-15、负数0；这些是普通浮点原报告，不是完整QP最优性或严格外包。完整condensation记载complete=true、全局维236036、local9805、freecore109和112全局边界均保留。

原FD在本次新warm实际执行：最大四阶relative directional error=8.81884772255149e-10，二阶最大=0.00000988344249574147，原threshold=0.00005；implementation_check_passed=true、second_order_truncation_contracts=true，left/right offblock最大0。该FD复用了原completed nonlinear J，但nonlinear_DN_evaluated=false、nonlinear_native_at_current_H_solved=false、full_BVP_solved=false；不能以FD通过冒本次native或fullDN。

这些原α、merit和FD字面数值与[R346](R346-actual158-original37-accepted-step-and-post-model-binding-failure.md)相同；完整输出文档身份不同。没有从相同标量推出两次全部科学数组逐字相同。

## 353.4 配对修复的真实闭合

本次capture实际保存12次evaluate、185次angular返回、1个domain和1份最终方向，observation_complete=true、errors=[]。完整domain实际有37个base angular返回和74个控制返回。

37项query_control_matching_readback均按原station binary64 word与原explicit scalar_control_jets身份匹配；每个查询在本次实际恰有两个同身份返回，选其首个字面相同代表，并保全部候选和全部74调用。LEFT使用原scalar_control_jets，MID使用原original_scalar_control_jets；数组身份完整包含shape、NUL、dtype、NUL、C-order bytes。没有重算控制值，没有抛弃额外observer调用，也没有把“每查询恰2次”写成未来的固定假设。

158在此处要求返回总数等于37导致程序错误；本次74是实际导出的计数，不能倒填成158当时未导出的事实。

最终原方向是全局选择器实际选中的完整coefficient_direction，不是LSMR初稿或未选恢复候选。其236036个binary64词原raw SHA为23f95dc5a91e3e2909cc6dc3978bbabc4f35536c183f7890b3f82184a89f85b8；scaled_direction原raw SHA为07e0fc09a9bdd72c4e205bbb0fed7249f61816fc47c2ba98b685dce52a86d857。完整B model身份4b351ed38caa47969192c1d6461a51855c99d05634d1a80ab9aff5794846081c保持绑定。

原29个chunk action保node463–491各自真实call身份：463–464来自call0、465–480来自call1、481–491来自call2；每份完整453分量由338个physical与115个常数分量组成。缓存依据真实chunk/call/参数/physical身份，不能仅按node合并可能不同的原word。当前Actions验证308份原packet的完整NPZ和每个数组raw descriptor；本次本地只读取这一实际验证记录和结果，不假称另外取得这些payload重新审计。

## 353.5 75776行、九系数和全部17档的准确仿射结论

每行使用保存的有限word构成准确dyadic仿射参考a(α)、ν(α)、d(α)、e(α)，并完整形成

$$
P(\alpha)=a(\alpha)^2\lvert d(\alpha)\times e(\alpha)\rvert^2
-\nu(\alpha)^2\lvert d(\alpha)\rvert^6.
$$

P的次数至多8，保存全部9个准确整数乘二幂系数。每个[0,2^{-j}]闭区间使用全部9个Bernstein系数，统一正分母280。a的两个端点为正且P所有Bernstein系数为正时，才记严格区间证书；端点严格反证与Bernstein不足的未决分开。P>0本身排除d=0或d×e=0；没有省掉域分母责任。

|j|α|完整行|端点strict行|闭区间strict行|端点反证行|区间未决行|未定义行|
|---:|---:|---:|---:|---:|---:|---:|---:|
|0|1|75776|75698|75348|78|350|0|
|1|1/2|75776|75760|75684|16|76|0|
|2|1/4|75776|75764|75760|12|4|0|
|3|1/8|75776|75776|75776|0|0|0|
|4|1/16|75776|75776|75776|0|0|0|
|5|1/32|75776|75776|75776|0|0|0|
|6|1/64|75776|75776|75776|0|0|0|
|7|1/128|75776|75776|75776|0|0|0|
|8|1/256|75776|75776|75776|0|0|0|
|9|1/512|75776|75776|75776|0|0|0|
|10|1/1024|75776|75776|75776|0|0|0|
|11|1/2048|75776|75776|75776|0|0|0|
|12|1/4096|75776|75776|75776|0|0|0|
|13|1/8192|75776|75776|75776|0|0|0|
|14|1/16384|75776|75776|75776|0|0|0|
|15|1/32768|75776|75776|75776|0|0|0|
|16|1/65536|75776|75776|75776|0|0|0|

全部17档都访问了完整75776行，undefined_count=0。α=1/4的12个端点非正global rows原样为：

2102,3018,3126,4042,43052,43062,43978,43988,44076,44086,45002,45012。

其余4个区间未决global rows为45105,46031,46129,47055；这些行端点仍严格正，不能把Bernstein未决写成真实域失败。α=1/8最小P端点与最小Bernstein下界均是正准确dyadic；原最小索引均32768。未在本地将这些大整数转换成近似新数值。

此证书仅属于新后置算术明确形成的仿射参考。该参考的FFT/标量动作是独立后置有限word形成，不冒原稀疏B.matvec逐bit相同；完整原Bz被读取核身份，未反造参考输入。它也不把complex-step原J或有限FFT形成词称为IEEE离散roundmap的准确导数。

## 353.6 真实四档点态结果与仿射参考的精确边界

四个真实返回α各有37份2048角记录，共148份。全部记录complete=true、complete_rows=2048，准确a非正标志均false，geometry undefined范围均空；原normal与cross β²均无非有限角。每份准确实际P非正角集合，均与同一原返回normal β²非正集合、cross β²非正集合逐索引相同。此处只是比较已保存原集合，没有本地重算P或β²。

将原global row标签按固定query_index/angle_index映射作集合对照：

|α|仿射端点非正行|真实点态非正行|逐行集合关系|
|---:|---:|---:|---|
|1|78|74|仿射另外有MID486的angle84,940,1108,1964；真实没有这些坏行|
|1/2|16|16|完全相同|
|1/4|12|12|完全相同|
|1/8|0|0|完全相同、全37查询点态正|

最近拒绝α=1/4的坏角完整为：

- LEFT464：54,970,1078,1994。
- MID471：44,54,970,980,1068,1078,1994,2004。

原模型在相同α的全部线性reserve为正，而完整P的仿射端点已经反证这12行，说明一次线性域近似没有保住这次有限步的完整域非线性。这个判断不需要把刚补入的MID489/490作为失败首因；也不证明增加约束永远无用、λ需改变或原QP已最优。

α=1/8之后的13档没有原非线性返回。新诊断只支付了它们的仿射参考，不补跑原trial，也不把pointwise_query_defects_complete=false写成失败；原unavailable_original_trial_query_scopes逐档保query0–36与angle0–2047全范围。

## 353.7 全453分量Hermite恒等式与尚未支付的整段责任

全部148份实际query都完成453分量恒等式核对，exact_identity_equal_count逐份均453，完整临时Hermite账67044行。其余项分成：

1. 实际端点state形成与理想α方向之差；
2. 实际左右端点RHS相对原完整J/P方向的余项，经原h与Hermite权重组合；
3. 实际query程序和准确Hermite字面表达式之间的有限形成差；
4. 准确端点动作形成的query方向与保存rounded方向之间的差。

各分量准确总和等于实际query−base query−α乘保存query方向。原base和actual query各自的程序差都保留，不默置零；所有338个physical和115个常数/参数分量均覆盖。所有原pointwise_only=true，whole_trial_segment_RHS_second_derivative_bound=false。

在最近拒绝α=1/4上，原record的actual_query_minus_affine最大绝对项分别为：

|query|原最大分量|原准确dyadic字面值|
|---|---:|---|
|LEFT464，q1|226|−0x699c752b × 2^{-69}|
|MID471，q21|226|0x21e1aa587 × 2^{-67}|

这里没有本地计算小数、比值或新的范数。原RHS_defect、node_formation、query_program_finite_formation、direction_word_formation及左右RHS余项的独立极值/非零分量范围都在完整原result中；不同项的最大位置可以不同，不能把各项最大值直接相加称某一坐标的等式，也不能从这两行推出唯一误差主因。

因此后继若要把仿射参考证书传给真实整α Hermite查询，需要[R354](R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md)的全453有限参考、原scalar控制沿段变化、全部角上分母/域正下界、完整DFT投影及形成误差项。当前原node RHS/J/实际返回已足够做同现场独立后置构造；仍不能将既有点态差冒成全段二阶界或IEEE程序总误差。该诊断不得反改本次原模型/FD判定。

## 353.8 完整原日志、语义成员与raw身份

本次日志包含8个完整语义文档，共910个成员/容器事件，逐文档canonical size/SHA和全部子成员size/SHA均闭合。日志拼接的两处step开头BOM按传输分隔处理；原完整日志字节和SHA不修改。不存在以浮点重新序列化近似数字来“凑”SHA：重建保存原JSON数值词法。原442529B模型摘要的single_frame_summary_complete=false仅说明单帧有界输出不足，完整66成员语义流已闭合；不把单帧省略冒成丢失整个原结果，也不抹去该原标志。

|完整语义文档|canonical字节|canonical SHA256|成员/容器|
|---|---:|---|---:|
|batch-000/complete-original-summary|442529|5a92f6f5f076f8d5d7a13cacdd62d29491472b112f33de02442b8d85fee01b2c|66|
|request166/pipeline-final|9739|6c2defffd881f3576648c931324a467b22c74f6ff0dfe96ebaab569c983bfd0e|1|
|request166/original-rule-monitor-result|431|a1c8326dbebcece11df088c3a57c0e007baa318c2be6631fb0afeac7ec10d169|1|
|request166/pipeline.json|9739|6c2defffd881f3576648c931324a467b22c74f6ff0dfe96ebaab569c983bfd0e|1|
|request166/original-pair-summary.json|442529|5a92f6f5f076f8d5d7a13cacdd62d29491472b112f33de02442b8d85fee01b2c|66|
|request166/post-model-diagnostic/result.json|1619445|ef284448bf950be33c4b173f371886a5321be7683ac954e93d5dc6e29035b9b6|773|
|request166/post-model-diagnostic/summary.json|792|59f461b7ba910a541c178862b9c6ac7560451611081dd1e58e2cc399e7e6f2ef|1|
|request166/capture-status|50650|aa9609e0db3c2fbd2ef1b76d63bbd45f2ddd3423ccdfc2fd6a6f6c777a70accf|1|

语义身份统一为解析后JSON、key排序、ASCII紧凑编码加一个末LF，明确不是任意原文件字节。独立result原文件为1619445B/SHAea5cc6d9c8b7e5dfda12e49aaad6cafd61bb9be5c769a6db24b45f5fe368f64b；其语义身份为同长度ef284448…，差异已准确定位并恢复：原四个slot.angular_by_query在Python里是整数key，原writer按整数排序；重读JSON后key成为字符串，语义writer按字符串排序。只在这四处按原源码恢复原key顺序、全部数字词法不变，便逐字重构原ea5cc6d9…文件SHA。其它numeric-looking key仍保持原已解析来源的字符串排序。

原模型五件输出身份如下；它们仅在本job临时保存，后续不能靠hash伪造恢复：

|原件|字节|SHA256|
|---|---:|---|
|thirty-seven-condensed-warm/model-000.json|814412|8dc1bd88a63afbb707a11d8dfa90753be3be97d9b3b51b323e7815f7c6582ae3|
|thirty-seven-condensed-warm/driver-status.json|3647467|6aa6b8dbef94e05c3994b65459ec55474e20a21b1aa82e3e9ef5a540660c5b89|
|thirty-seven-condensed-warm/condensed-QP-summary.json|128722|9f6b0e1b38f6a0b178038d70de0d5e89f536a9675b904702cff301f4831aeab6|
|physical-response/response-check.json|2839006|3868a1fba9eea80179cb1ffedfb2dcf9b02589c66cf77106ba7e0236ac1ad573|
|thirty-seven-condensed-warm/warm-001.json.gz|4943010|b35eb9d368dd6b813895d74b7e9528e6ce584b81e7f6bf07fa5813165375fa5c|

新诊断四本完整临时账：

|账本|完整JSONL行|gzip字节|未压缩字节|gzip SHA256|
|---|---:|---:|---:|---|
|all-row-polynomials-and-Bernstein.jsonl.gz|75776|1077786246|2574328420|02e0d345241aa955b0dd8dee7a7a269497c314d108a7230d53a13dfd2ce55982|
|actual-query-point-geometry.jsonl.gz|303104|52848711|371142216|550474ec23450b9105b10c452ed2cfd73a400d21e60278bad5657db98f31fd5a|
|all453-pointwise-Hermite-decomposition.jsonl.gz|67044|14160176|104340171|bb684fa8ba3547e0f854c9793b91ea6c98d288d8384c1a90a6a70723b94aff66|
|original-chunk-exact-JP-actions.jsonl.gz|29|275597|1420796|6a95262245a434450049bebbe6a2aecd8d759ab71243945c52f870bdbe94764c|

原总未压缩账字节3051231603，小于本请求8GiB资源上限；原结果记录完整写入。根据第15条，以上可重算账本、packet和新warm均未上传artifact/Release或Git。全部原结果、范围、反证/未决索引、来源和字节身份已在同job语义日志完整读回后清理，不能把保留hash当仍有raw现场。日志中的packet/ledger核验是Actions实际执行范围；本次本地读取不扩大成重新下载这些数组或整数账科学复核。

## 353.9 可直接复做的入口与下一责任

公开request为computations/public-thirty-seven-R334-bound-diagnostic-request.json；workflow为.github/workflows/visible-larger-public-thirty-seven-R334-bound-diagnostic.yml。同job次序仍为真实actual98双原件恢复→原37完整模型→实际新warm原FD→新capture绑定下的独立R334算术→完整原语义读回→只清本job临时目录。

完整consumer参数原样为：--capture <当次R334-return-capture> --model-directory <当次thirty-seven-condensed-warm> --code-directory <本次pinned computations> --seconds 1800 --max-ledger-bytes 8589934592 --out <新post-model-diagnostic>。其中source、parent、最终实际方向和完整query身份均由当次原件取得，不存在可接受伪status或旧Bz反推输入的路径。

当前原标志必须共同保留：original_model_accepted=true、原FD implementation_check_passed=true、scientific_completed=true、resource_partial=false；同时success=false、new_coupled_finite_acceptance=false、nonlinear_native_or_full_DN_run=false、native_or_full_DN_accepted=false。R353支付有限仿射证书和真实返回的完整点态差分解，未完成主课题目标。

最直接的后继是保持这个真实同现场对象，补原R354整段有限RHS余项及字面形成责任，而不是盲增query或从点态数据推全段界。若将来需要新的求解轨迹，必须重新取得真实父或同job保留合法现场；本次已删raw不能冒续接。
