# Request124：原同一worker的完整H(s)延拓与full112交接

类型：独立科学入口与来源接口；尚无124实际run或数值结论。
作者：ChatGPT /root/exact_refinement，AI-assisted，2026-11-15。

## 1. 具体实验与原120证据

本入口以真实120首冷请求的失败为动机，只改变“如何给同一原尾worker到达当前完整物理高度H”的初猜策略。它重新使用实际119第3批的六个参数、原四数学输入及原完整预检，真实形成当前112维 $H_*$；不从120摘要重建H、场或尾checkpoint。

真实120为run43694844403，source ace38440324f09471482826136584da38960c417；compute132752997196失败、report132753527828成功。原紧凑摘要19463B、SHA256 4f2be484a9d33faf5b9072bbb0c22989d885351a28a229f504aed34d1f081b85。它记录第一次当前H请求报“Error: momentum branch D/S/A rejected”，lastIteration为null，没有原Newton试步或实际响应J，故不能当作已接受尾锚，也不能据字符串断定浮点原因。124不继承该失败状态。

参数顺序固定为 $[p_1,p_2,p_3,\theta_1,\theta_2,\theta_3]$，字面初值为：

    [0.41654476801167684, 0.23884336093393582, 0.5270922473095916,
     -0.13437878055563054, -0.005765450212224129, 0.4141025261683763]

仍选显式 $\lambda=0.001$、原完整112模/2048角及453态方形问题。三odd固定，前三p为3个active设计坐标，全部112core未知量含高109保留。旧零尾J仅用于原圆/低三初猜；无低三阈值、旧高核证书或“父native成功”前置门。

原807f入口、120workflow及122有限trace变分实验一字不改。本入口不改善primal算术精度，不替换root、RHS、RK、局部J、原576stage/cut/far/均值、尺度或阈值。

## 2. 完整文件身份

每件都是一个正常UTF-8小文本；没有数据分片、base64载荷、raw上传、tree/commit/ref修改。下表Gitblob仅用于主控集中发布。

| 文件 | Bytes | SHA256 | Gitblob |
|---|---:|---|---|
| `geometry_20261115_original_tail_height_path.py` | 23078 | `e830a1679908cdc0cdd8c1ecd5663bbf6b82b24a3d52e44cf678aedc227eee48` | `2af3d9c7bc801a1c2d0371e082005bc4504d16bf` |
| `geometry_20261115_six_control_height_continuation_full112.py` | 45097 | `557f3aab83116c1d8eef83e4c83306e8058749ccdb56b2ec8808effd2e16bf21` | `63daafb270571dae55e1020cd7d06cc87675f71c` |
| `root_20261115_six_control_height_path_run.py` | 9677 | `0836ed339974d5f21cdbd110f1a78ba5fb9232f5ee4f22c74849b2ee16d133dc` | `18c8ed5d1029916fde5c5063ca5f564f12e1f442` |
| `root_20261115_six_control_height_path_scalar_readout.py` | 26540 | `4a0ab4a7ad8fbd62dd5fced0f15431498934d000af2681e137dc237b8ebaf5be` | `4618ee385777f1afef2fc6c1bc5552c81ac47407` |
| `actual119-batch3-height-path124-lambda0p001-recipe.json` | 4057 | `b590eb0c33d55ff13a1b6ec3722d5dfe9f316a774207a1b8dda7925e6f159416` | `876cd8ff6f75805b31fbb0bedf8156bc5ade9572` |
| `public-six-control-height-path-request.json` | 22159 | `b76f94ada5b146f79c868af219662fdb39b98c9cd9b00b9d8667f34e7f337ab1` | `a00ee387df4ed121078d74af8e6855a11060d32b` |
| `visible-larger-public-six-control-height-path.yml` | 16958 | `7a4b1c05a60ac11ad7a4da639e829f72eba5825e96181fb4893da2bba79e309a` | `8f8ff42fb8e5c55da058d683682254004de332da` |

数学基线是actual120发布的 geometry_20261115_six_control_full112.py：42683B/SHA807f6a35e0d66aee7a2f324e4573bd2b9e9be8feab1972e4b073aa8ee91ed7a2/Gitblob32b8dbb61153a97bb937f2868578373148b2b57d。

新request保留原120全部99个source pin，再加本次helper、adapter、process wrapper、reader四件，合计103。旧807f、120wrapper/reader和22e publisher只保来源，不作为124入口执行。原78公开源恢复责任没有减少。新adapter的完整runtime来源另随实际binding保存，不把103个调度pin全冒为同一层数值模块。

完整可逆文字差异为 request124-exact-source-replacements.json，30097B/SHA81beeacd57d413efcc2723f03de084b0d5b66d6b9abd3fb4a00db5437a1b3731/Gitblob6f7aa4829ce0b4b0bd7fb8ff8adb2d7a20a7b807。它列出四个旧base的ref/path/Gitblob、每一处old/new全文及次数；主控可从actual120 ref重建新文件并核完整SHA，不能把replacement字符串交给会解释美元特殊串的替换机制。

## 3. H路径、参数和同一owner

目标路径为

$$H(s)=sH_*,\qquad 0\le s\le1.$$

每次都保全部112个坐标，不删高模、不对小量阈值化、不把物理H当作raw Q或另做端口换算。中间数组为逐坐标binary64乘法；最终$s=1$直接复制原始H星号数组的词，不再次乘1，也不从前一成功点或报告插值。

| 项 | 本次明确值与语义 |
|---|---|
| 初始请求 | 真正原worker、112个正零、jacobian:false、audit:false |
| 首个正增量 | $1/64$ |
| 原响应成功后 | 用实际本次$\Delta s$乘2，上限$1/4$ |
| 已绑定的原数学拒绝后 | 同一上一成功点不动，实际本次$\Delta s$除2 |
| 最小拟议增量 | $2^{-20}$；再缩小则资源partial |
| 最大bootstrap请求数 | 64，包含零请求、失败请求和末端完整J请求 |
| 末端请求 | 原H星号完整数组、jacobian:true、audit:false |
| 总科学墙钟 | 18000秒，覆盖新预检、bootstrap、原FD/fullDN，不是每请求重新计时 |
| 原后续预算 | native32次Newton/每次10档，fullDN8个outer/原17试步；全部照原配置 |

本次按主控明确选择，在**第一次到达$s=1$的请求里直接要求完整J**，不额外先做同H的无返回J请求。这样没有把一个先前无J响应冒成末端成功；末端这一次完整原请求本身可能失败。

中间jacobian:false仍执行原Newton每轮withJ和保留的flow Jacobians；只控制请求末端完整338×112响应J的输出，不能称作省掉原Newton导数的廉价无J求解。所有中间收敛仅为H路径尾解；它们既不是当前完整prefix场的解，也未付最终audit。

helper借用由新adapter创建的唯一SharedNativeClient，不创建第二worker，不给cache_key/cache_value/worker last/tangentPredictor赋值。helper不关闭owner；结束后原adapter/原fullDN保持单一关闭责任。helper要求初次client.calls=0且无checkpoint/cache，避免把任意历史状态冒本次零起点。

零点的原tangent predictor可能unavailable；原amplitude warm从零点计算高度比可能无效。该情况照原fallback进入cold initial，不能虚构warm方向。缩小s也不保证原normalized残差更好。

## 4. 只有原真实数学拒绝才缩步

原TailClient先读worker JSON并把完整request/response/config/source/capacity/seconds写临时gzip，再检查原converged、严格残差、全部jets/均值、所请求J与audit。新helper在每次请求前保存in-flight状态，原调用返回或抛异常后读取**这个call的完整原gzip**及本次新增trace/trials字节，核：

- Python原request的112个H词、jacobian/audit、client.calls增量恰1；
- 完整原config/source/capacity等于当前原client持有的真实对象；
- 原trace中恰一个同call/request和一个相符的终端response或failure，没有混入别的call；
- 原成功由原client全部验证返回，再由未改SharedNativeClient核完整当前H；
- 原失败只有明确原数学消息或正常converged:false，并且Python缓存仍是请求前对象/高度，才可不推进last_s并缩步。

原worker的最外层catch也包trace/checkpoint/I/O。它在sol.converged后先更新last，再写response记录，因此“Python异常”或任意failed字符串都不是可安全缩步的证据。缺失/损坏JSON、原记录写入失败、trace不全、未知failed、已收敛却缺J/jet、原成功协议不匹配、意外缓存命中、source/call不一致一律停止为protocol-or-record-partial。不得拿失败checkpoint或accepted-trial-recovery-only文件替换原收敛last。

可识别原数学错误的literal集合仅来自所钉源码：momentum profile范围、D/S/A、momentum SPD/line search/iteration、initial mean root/iteration、tail graph chart singular、Fourier-product/physical-jet/batched momentum Jacobian不正，以及带完整有限norm后缀的原multiple-shooting line search失败。集合外不猜测类别。后者不是新残差接受阈值，只是原失败消息识别；原client的所有真正数值判据不改。

零H本身若被原数学拒绝，无上一个成功零基点可回退，直接结束并记录该事实；不据此证明正路径无解。最小增量、64请求及墙钟耗尽只记录尚未到达的$s=1$和最后真实成功s。异常记录不完整时，不声称worker last未变化。

## 5. D/S/A：现有源码能定位到哪里

下列是实际读取的原文件位置，不是124新增root观察器。

| 来源 | 位置与范围 |
|---|---|
| 78718-tail-fourier-root-momentum.mjs，13809B，SHA cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88 | evaluateL第45行，唯一同文throw：$D>floor,S>floor,A>floor$的联合否定；没有r/角/三个值 |
| repro/source-root/.../general_root_tail_momentum.mjs，13095B，SHA182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c | 原通用evaluateL第38行，同文throw；仍是依赖/原初始化factory的一部分 |
| 78718-tail-tangent-core.mjs，17250B，SHA ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 | initial第68–74行只graphs/gains线性填态，无root或DSA throw；evaluate第94–99行给异常附stage/rawCell/rawSegment |
| 同core原trial循环第145–153行 | 若试步evaluate失败，既有trialDiagnostic可保stage/rawCell/rawSegment；不保r/角/DSA值 |
| 78718-prefix-tail-tangent-fourier-worker.mjs，12294B，SHA36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a | 外catch只String(e)、lastIteration/checkpoint，不输出附着的stage属性 |

120/124 ready后的fourier-root backend走product-flow/rhsWithJacobian/Fourier root，split RHS接已经得到的knownRoot。原通用split内部root没有被当作同一次额外真实root调用。原root对内部trial的DSA异常有既有catch；外部同文异常不告诉读者这是哪一次RK/root或哪个角。

若一个冷请求原failed确为DSA、没有warm/iteration/trial且lastIteration为null，按这些原调用顺序可标“首次完整withJ evaluate未返回”，并排除在纯线性initial()中抛DSA的解释。仍不能给具体stage、r、角、D/S/A或浮点主因。helper只记录这条明确源码推断和原字段；后续有trial时，直接保其真实定位，不补假数值。

## 6. 回到原完整FD/fullDN与最终门

仅在同worker返回原$s=1$完整H/J、原严格残差和全部jets均已通过后，新adapter沿807f原文继续：

1. 原actual_boundary_fd：原三处扰动、原方向、原步长/Richardson层与$5\times10^{-5}$阈值、原二阶收缩合同。
2. 同一owner交回未改original_full_solve，原完整banded/core主循环、全部453行、112core与3activep、全node/mid/RMS/BC和17试步保留。
3. 每个后续新H仍实际原native求解，最终当前H完整J与原audit、physical cut/seam、场与边界门仍由原代码决定。

helper完成不设置success/new_coupled_finite_acceptance。只有原fullDN driver原最终结果能令这些字段为真。H路径s、core目标幅度lambda、曲面族相位t是不同参数。即便本次完整有限field接受，原无限尾、闭合、全t强C²、同场metric、reach/held与整任务责任仍不能从bootstrap继承。

## 7. 真实输出与partial

临时目录结构如下；全部保留到对应reader用完，再由workflow只删本request RUNNER_TEMP目录。

- execution/process-status.json与science-stdout-stderr.log：原子进程状态、总预算、返回码/外信号，wrapper不推论科学接受。
- science/adapter-status.json：原preflight/当前H/FD/fullDN实际阶段与height-path停止原因。
- science/height-path/height-path-input-binding.json：完整pre-path adapter binding、原source/config/ready、policy与原H星号字面/词SHA。
- science/height-path/original-H-star.f64le：896个原字节，仅临时；保负零位置。
- science/height-path/height-path-status.json与height-path-requests.jsonl：所有实际请求，包括in-flight尚未完成项。
- 每请求trace/trials分段副本：完整原新增字节，不重evaluate；原full-DN/true-tail_####.json.gz与trace/trials仍原地保存。
- 原initial-guess、actual-H-response、full-DN所有原文件沿原接口生成；某阶段没有进入就保持缺失。

Python原request可逐词绑定；worker JSON会把负零写为正零，所以其checkpoint/trace只按原JSON有限数值身份，不假称保存序列化前全部负零词。到$s=1$的**输入**始终核原H星号词SHA。

每个请求的compute stdout保完整实际response摘要、原trace和trials、消息与metadata SHA。独立report job输出至多90000B：优先保全部最多64条bootstrap主表、H星号、真实末s/状态、原J/失败/lastIteration/试步计数和后续FD/fullDN结果。大trace/trial详细段会显式改成计数与SHA，标summary_complete:false；不借读回裁剪通过任何科学门。主表的H原词SHA与worker JSON规范摘要SHA分别命名，不混用。

原首次请求H现在是零；reader的native.first_actual_requested_H因此是零。实际目标应读actual_current_H和height_path.H_star，不能拿“第一次请求”字段误当120原目标。

## 8. 执行接口、来源恢复和预算

底层独立adapter CLI沿807f保留：

    python geometry_20261115_six_control_height_continuation_full112.py \
      --recipe RECIPE --expected-recipe-sha256 SHA \
      --accepted ACCEPTED --prepared PREPARED --tail-anchor ZERO_ANCHOR \
      --tail-config ORIGINAL_T112 \
      --tail-client exact_20261114_true_tail_client.py \
      --expected-tail-client-sha256 1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09 \
      --tail-source-root RESTORED_TOPIC/repro/source-root \
      --out TEMP/science --work TEMP/factors \
      --jac-workers 2 --max-nodes 1200 --material-angles 4096 \
      --physical-angles 4096 --node-heap 1536 --outer-iterations 8

实际workflow经新的stdlib process wrapper启动，并由wrapper设置同一18000秒monotonic总deadline。外部3b8规则runner原2700秒真实pull/rebase/规则变化stop保持；子science checkout仍是触发SHA。规则异常/信号不被归入数学拒绝。原350min compute、330min science step留出真实规则同步、终止与读回余量，不扩大每次原数值预算。

四输入仍从真实公开历史8bd267107cc8710d371f3b62c02986655ac965b0逐blob/size/SHA恢复：accepted b4d2b98a…、prepared0f94dd88…、zero tail anchor e788a28d…、原T112config01930f3b…。两ready原env槽逐真实SHA恢复；其完整tuple在request中。原T112没有initialCheckpoint，不从95/103或其他失败native状态启动。

workflow新trigger为computations/public-six-control-height-path-request.json，独立concurrency visible-larger-public-six-control-height-path。原source恢复、runtime版本、输入和原完整维数保持。按第15条没有upload-artifact、Release或Git raw输出；只发布小脚本/recipe/request/来源SHA/紧凑结论。旧publisher22e不执行。

## 9. 静态事实与尚未执行范围

已在隔离JS文本环境对真实旧source完整SHA、所有精确replacement次数、正反全文恢复、新文件SHA/Gitblob、请求pins/CLI字符串作检查。原active_profile、curve_with_exact_nodes、bound_original_preflight、prepare_problem、actual_boundary_fd、original_full_solve六个函数全文逐字相同。SharedNativeClient和owner关闭/原接收条件也未改。

终端在首个helper写入中断；该无回执调用已终止，旧/tmp版本不能作为交付。最终完整小文本已用现有GitHub连接创建独立blob，没有任何branch/tree/ref变更。**本地未运行Python AST、bash-n、模块import、fixture或科学计算**；workflow沿原起步完整source AST验证，正式执行仍只由主控在公开Actions发起。这个环境限制不是新数学验收门，也没有用合成数值代替实际实验。

当前只交付可运行源码与原件身份；没有124结果、H路径可达性、成功native/fullDN或新几何结论。若首次正H仍拒绝、tangent predictor无法建立、末端J失败或资源用完，报告其原证据与最后真实s，不推断无解、路径单调改善或全局精度底线。
