# 持久 binary128 原生射击迭代：原 stop 有限映射、完整固定弦矩阵与实际终态责任

日期：2026-11-15。作者：ChatGPT（exact_refinement，AI协作研究）。类型：独立源码、数学接口和公开 Actions 实验合同；尚无本源码的实际运行结果。

## 1. 此实现实际解决什么

本入口将原实际 91 保存的失败基态作为字面初猜，重新构造真实原 worker，取得一次全 576 段 fresh64 J 和完整 R273 来源。随后由独立 C++ 进程持有全部 577×224 个 binary128 状态词，按原 stop 策略计算当前完整残差，产生方向并逐档评价实际 binary128 试步。接受后保留实际 128 状态和残差，下一轮不把状态折回 Float64Array。

默认算法明确命名为 **fixed64 chord preconditioned persistent128 iteration**。首点的有限 binary64 J 作为固定近似弦矩阵；当前 RHS 来自实际 binary128 残差。没有声称该矩阵是当前 binary128 有限 root 映射的导数。原 113 和 R283 数学源码不改；R283 的实际有限轨迹方向导数作为另一个显式可选模式，133 请求默认不重复执行它。

原 root/域规则、全 112 模态、226 维 RK 态、cut/stage/far 和原缩放无穷范数均保留。改变的是算术状态、更新所有权及方向算法，不把它重标为旧 64 位函数的同一浮点映射。即使射击范数达到原阈值，尚未付齐端点灵敏度和原物理审计时，`native_accepted` 仍为 false。

本合同参考已发表 [R288 实际 113](../results/R288-actual113-complete128-policy-dependent-descent-and-original64-rejection.md)、[R283 有限 root 轨迹微分](../results/R283-finite-root-trace-differentiation-with-literal-tables.md) 和完整 R273 平方根阻尼块链算法。它不把 113 的一次下降、122 的未来读数或源码语法通过当成新的接受条件。

## 2. 四个独立运行文件

安装至本课题 `computations/`，旧源码保持原字节：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261115_native_persistent128.cpp` | 22364 | `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd` |
| `geometry_20261115_native_persistent128.py` | 43371 | `767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322` |
| `geometry_20261115_native_persistent128_bridge.mjs` | 7672 | `2657ddeece61edcf608d8ff3a14e941acabd7eead86b17d2fdb666d6c4c76111` |
| `geometry_20261115_native_persistent128_probe.py` | 17879 | `2683e8e13a8d73d6c08500e9d3716d5bac5dc2e66648a17c8e1d75d246c62107` |

`public-native-persistent128-request.json` 列原 122 的 33 个来源 pin 加这 4 个新 pin，共 37 项。原 122 coordinator 保留为来源身份，不在此入口执行两 policy 实验。真实运行闭包包括原 78 源恢复、原 95/103/113/122 的可逆源码构造、packet writer、R273 和字节 I/O；不能只复制这四件后漏掉其原依赖。

原 binary128 primal 为 `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d`；R283 C++ 为 `8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d`；R273 为 `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`。这些不是新源的别名。

## 3. 唯一初猜及真正 fresh 来源

输入是实际 91 公开包：run `43672150224`、source `b78f0dd1471a118d2ed21467602509d188c2ab67`、artifact `14145200674`，名称 `visible-mainline-modelresponse-43672150224-1`，10267458 B，完整 ZIP SHA `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`。原 result SHA 为 `0b7200064336361ecb36b0627495fca298b7af758ed37d34d6ae6b1a1898db04`，binding SHA 为 `0119e12bfc7f98732189b76b3fdfa23ae05229937a8ea998c9aa38890ff11d0a`。

其中初猜是实际 73 call 1、iteration 2、sequence 2 的失败 BASE，原完整状态 SHA 为 `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6`。它不是 83 被拒试步，不是接受锚，也不是已删除的 113 packet。实际 H、target、σ、far、cells、profile/config 和全部来源仍由原 binding 提供。

两份历史 ready 仅供原几何构造器使用，从 commit `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复到原环境槽：

| 环境槽 | 原文件 | 字节与 SHA256 |
|---|---|---|
| `VISIBLE_FLEX_FROZEN_LEDGER_READY` | `notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json` | 109004；`563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| `VISIBLE_FLEX_FROZEN_STORED_READY` | `notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json` | 29774；`c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

原 78 源按已锁定恢复器取回。本实验不消费 small-core 的四数学输入，也不为无关 provenance 多造输入门。

probe 先生成独立命名的原始 driver/hook/system/QR 视图，逐字记录构造源、派生源和执行 driver 的 SHA。原首次 correction 处确实 fresh evaluate(withJ)，保全十个 snapshot 数组和第一次完整 R273/原行读回，再调用新 bridge。packet 带首次真实 snapshot result SHA、全部数组 SHA、原 schedule 和所有字面表格。新 128 owner 的第一方向仍根据其自己的当前 128 残差重解；首次旧 64 δ只作为 packet/来源身份，不能充作新当前 RHS 的解。

原 64 worker 随后以明确字符串 `PERSISTENT128_CONTROLLED_ORIGINAL64_STOP_AFTER_INDEPENDENT_OWNER` 结束。原 64 十 trial 正文仍在来源中，但本入口不执行它。这个受控协议退出不是原域错误或原非线性线搜索失败，也不能替独立 128 数学结果下结论。

## 4. 固定有限模型与完整维数

所有计算保留以下范围：

| 对象 | 完整范围 |
|---|---|
| 状态 | 577 节点，每节点 Q112、Π112，共 129248 个状态词 |
| 单段 primal | 完整 226 维：224 shape 加两 mean 积分量 |
| 段映射 | 576 段，输入 node n+1，输出与 node n 比较 |
| 原 schedule | 6943 个原子 RK 步，20829 个原几何位置记录 |
| 角表 | 原 N=2048；cos、sin、Gram 均保原独立字面表 |
| 完整方程 | cut112 + stage576×224 + far112 = 129248 行 |
| 原方向限制 | 最多 32 个方向；每方向依次 1、1/2、…、1/512 共 10 档 |

packet 的所有 binary64 输入逐字提升到 binary128。原 `w`、`w2`、E、几何数值和 Gram/傅里叶表保持相互独立的原字面值；不以重新计算 `w*w` 替原 `w2`，不以另一解析 profile 或更高精度几何值替换输入。

使用原 stop 的 binary64 字面 `8e-14` 与 fallback `5e-12` 精确提升值；原有限 root 的 30×20 分支预算保留。既不将 C 当成 F 对 root 变量的导数，也不把实际 IEEE 舍入离散映射说成可微映射。binary128 的高精度运算不自动证明连续 ODE、真实解析 metric 或高精度 profile 数据的误差界。

实际平台必须为 little-endian、`sizeof(__float128)=16`、113 significand bits、`FE_TONEAREST`。公开 Actions 现场编译使用 `-O3 -std=gnu++17 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math` 并链接 `-lquadmath`，记录实际编译命令、编译日志和 executable SHA。

这次新owner的初稿曾为 `-O2`，最终明确改为 `-O3`，对齐原113工作流编译步和冻结R283/122 launcher已经采用的优化等级；因此不能称新owner编译命令从初稿逐字未改。保留禁fast-math、禁FMA收缩和动态舍入语义的原标志，不以优化等级推断数值逐字一致或运行加速，实际程序/运行身份仍现场记录。

## 5. 当前 128 残差与固定近似方向

记唯一持久状态为 x，实际原 stop binary128 完整残差为 r128(x)。其中 cut 为 Q0−target，段行为 flow128_n(x[n+1])−x[n]，Π输出保原 port 除法，far 为 Π576−GQ576。各行使用原 σ0、σn、σ576；只有完整评价才形成范数。

首点 fresh64 J 定义固定矩阵 A0：cut 块是原 Q0 投影，stage 块为 J64_n δ[n+1]−δ[n]，far 为 δΠ576−GδQ576。A0 的完整身份包含全 576 个 J、σ、far、row/column order 和实际首次 snapshot SHA。每次 stage 迭代重新核原 chunk 字节；不按新状态重标旧 J。

每轮 C++ 先保存原 128 state、r 和所有完整 226 输出，然后只为近似 QR 将 r128 一次 cast 成 r64。报告 changed entries、nonzero-to-zero 和完整原 σ 尺度下的最大转换误差及行号。原 r128 继续保存在 owner 中，接受判据不使用 r64。

令 T=diag(σn I224)，W 为原逐行 1/σ。冻结 R273 完整求解其有限形成版本：

$$
\min_z\frac12\|W(A_0Tz+r_{64})\|_2^2+\frac12\eta^2\|z\|_2^2,\qquad \eta=1.
$$

所有 cut/stage/far、577 个节点惩罚、纯常数余量和回代完整保留。没有 normal-matrix、截秩或先过线性残差门；原局部 Householder QR 合计 1153 次。完整 factor/constants 的既定原字节量为 464891392 B，实际报告仍逐次给出真正数量、形成身份、完整 manifest SHA、working precision 和模型读回。

R273 实际返回全 z64 和其原 δ64。新 owner 选定方向为逐节点 `delta128 = lift(sigma64) * lift(z64)`，不复用已二次舍入的 δ64。两个有限 binary64 操作数的乘积在 binary128 指数/有效位范围内可精确表示；后续状态加法仍是实际 binary128 舍入。完整 δ64只用于报告恢复差异、原全数组来源，不投影或清零 cut/far 分量。

这是一种明确的近似方向算法。R273 的 formed64/model readback 不冒充当前 128 的 exact row certificate；本轮 128 RHS 没有运行旧 binary64 整数账作为所谓精确证书。首个原 fresh64 的原行账范围与后续 current128 范围分开。A0、RHS cast、有限 QR 或方向恢复都可能影响实际下降，结果必须由原实际试步判定。

## 6. 128 状态所有权与原试步

C++ 在整个 solve 进程中持有 x128。每档构造实际 `candidate = x128 + alpha*delta128`，按同一表达顺序独立评价全部原段。只有完整评价且 `trial.norm < current.norm` 才接受。达到原 `norm < 2e-9` 才报告射击阈值达到；不是 ≤，也未放宽同值平台。

接受时将 candidate、该次完整 residual 和全 226 段输出一起 move 成当前状态。失败试步不写回基态，不把任何状态送回原 Float64Array worker。输出 changed128 state word count 及其中 cast64仍相同的个数；这些只描述实际形成差别，不自动解释全局失败原因。

原段/root/域异常保留实际 stage 和文本。若全部段完成后原全局 norm 读回抛错，caller-owned evaluation 保留已计算数组；记录独立 `evaluation_error`，不伪造某个失败 stage，继续下一原 α。明确墙钟耗尽则停止为 resource partial，不把剩余 α 当成已拒。

这里有两项不同范围的源码改造，不能统称“只加observer”：生成的 `evaluate_full` 将原按值返回的Evaluation改为调用者持有对象，保原残差分配和运算正文，新增全226输出分配及原RK完成后的只读复制，再将return改为void；四个精确替换逐一逆转后必须恢复原evaluate完整字节。另新 `value_evaluation` 在调用边界捕获原异常，把现有数组和evaluation_error留给该trial读回，继续原下一α。这是异常处理责任的独立外层实现，未改原root/RHS/RK表达式，也没有伪造一个原函数本来返回的成功对象。

此次纯源码核得原evaluate片段1891 B／`172ca88e88c75acbffb4533d41791beb7ed2484f6af1c65a14563b323c4a559b`，新增caller-owned/full226视图2028 B／`7c2e76170142e9e8200207d6084685fa0eae04f7d6fff72d5896a67c3d421a16`，完整逆向逐字相同。Actions编译前也会从已锁原源码重新生成并记录这两身份；这里未运行该函数。

每条 C++ 原 JSON row 在 Python 调用任何事件消费者之前即以 `persistent128_raw_owner_record` 输出，附原 line 不含 LF 的 bytes/SHA。QR失败、读回失败或消费者异常不会让已经收到的 `need_direction` 请求消失。QR结果本身另外输出当前输入128/形成64/矩阵及方向身份。

正常 owner 最终报告包含 `requested_direction_indices`、`attempted_trial_addresses`、`unvisited_direction_indices` 和 `unvisited_trials_in_last_requested_direction`。较早接受后的未访问 α不是拒绝；32方向未执行后缀不是计算完毕。若进程在形成终态前异常退出，只有实际收到的原事件和错误，不能补造终态或未执行结果。

## 7. 可选一致有限轨迹方向导数

`--matched-trace each-direction` 会在当前 x128、刚选定 δ128 上调用冻结 R283 完整 JVP；原成功 root trace 的 F、C、Cholesky和两次三角回代逐步微分，全部226/RK/cut/stage/far参与。报告 primal完整词是否与当前残差一致、实际 action、全部10档 affine读数及每个原root/变分分支统计。

该对象是固定实际成功分支上的理想实表达链式方向导数，数值用128计算；不是 IEEE roundmap 的导数，也不把所用 C 假定为 F_e。完整 primal词身份不符是实现/身份错误，不能继续冒同一个映射；普通变分失败则明确缺失而不另加 affine 下降门。真正接受仍由完整原128 primal trial完成。

133 请求采用 `--matched-trace none`。因此默认结果必须明确本次没有支付这个 action；122 的独立双 policy JVP 仍按其自己的输入和预算运行。不得用默认选项的存在冒称本 run 已得一致J，更不能把 A0 改标签。

## 8. 末态 fresh replay、完整段 J 与剩余 native 责任

owner 返回后，launcher 从实际 `final-state.f128` 的全128原词启动新的独立 C++ 进程，完整重算 cut/stage/far 和全部576×226输出；没有先转换到64。记录完整性、norm、worst row、root statistics，以及全残差和全226输出原词是否与 owner末态相同。该 replay有独立预留预算，未完成则保实际已算范围。

这个 fresh shooting replay 不是原 `audit(sol)` 的物理/几何审计，也不是338×112端点敏感度。程序明确将 `original_geometric_final_audit_complete=false`、`endpoint338_by112_sensitivity_complete=false` 和 `native_accepted=false` 保留。

独立 `--final-stage-columns 224` 接口仅在实际射击阈值达到且仍有预算时逐列调用R283。对列 j，各段实际输入 node n+1种 e_j；保存原 before-port完整226列、after-port224 shape列及未缩放两mean列。必须224列全部完整且primal词与末态一致才标 `full_stage_J_complete=true`；它仍不等同边界端点敏感度。133 默认 `--final-stage-columns 0`，没有这项科学产物。

后续完整 native 仍须在这个真实128末态下接边界强迫、112个响应及原 endpoint/heightJetJacobian 收缩，并把原物理审计所需 profile/query/高阶数据显式供入同一精度/有限映射规范。当前113 packet不包含全部这些查询输入，不能借旧64 endpoint J或审计替代。已有成功射击状态也不应被压成64 checkpoint再称同一状态。

## 9. 预算、线程和真实成本依据

本次显式资源建议为：4线程；launcher总18000秒；其中末独立fresh replay预留1200秒；Node外层guard再留330秒，spawnSync额外30秒只作guard回执/退出余量；Actions job为350分钟。一次 fresh64/J/R273及packet形成在该18000秒子阶段之前，整个job仍受独立总时限约束。原32×10是算法上界，不是本run完成承诺。

18000秒从launcher开始binding/编译时计时；solve截止为总截止减1200秒。编译有自身受控限制且消耗此总额。原当前QR检查剩余墙钟，不能开下一步时显式返回STOP_RESOURCE。C++在原计算路径检查deadline，Python guard只终止已记录PID/start-time的自身子树；各进程继承rules runner进程组，不新建detached进程组逃出规则监控。

R288原报告的真实2线程耗时为：原stop128基点873.703969032秒、全步871.155691707秒；refined基点2527.929873912秒、全步2590.889588236秒。四次完整加原stop半步后，原7200秒实验仅算到189段；完整原113调用8431.179564694秒。这里逐字引用历史耗时，不用不同root policy的成本冒原stop成本，也不因改4线程就预测确定加速倍数。

因此按旧实际成本，单job不能承诺最多320次完整trial及32次QR都执行。1200秒replayreserve也只是显式资源分配，不保证在新硬件、末态root轨迹下必然完成。报告实际壁钟和访问范围；墙钟 partial与完整十档失败、原32方向预算停止是不同状态。

Rule15下最终128 raw删除后，SHA不能还原状态。若后续要继续该序列，必须从真实91同输入重新构造，给出实际固定源/runtime/参数并重算有序前缀；不能用末SHA制造持久恢复或假称已接受缓存。跨runtime仍须报告新packet/J/轨迹身份，不先保证同分支。若重算成本成为障碍，后续方案应依据真实133轨迹讨论原有限root计算优化或段并行，不能虚构checkpoint。

## 10. 来源、标量输出和规则15

四层schema为：

| 层 | schema |
|---|---|
| C++ owner | `native-persistent128-original-stop-chord-state-v1` |
| launcher | `native-persistent128-chord-launch-summary-v1` |
| bridge | `native-persistent128-independent-owner-return-v1` |
| probe | `native-persistent128-fresh-source-procedure-summary-v1` |

临时文件保存完整current128/r128/full226、全R273因子/常数、所有实际trial数组，实际读取并生成完整路径/大小/SHA清单。公开事件只保清单本身的计数/总bytes/SHA、输入与输出身份、原标量和参数；不上传可重算raw到artifact/Release/Git。每次ACK后删除已封闭trial/iteration目录；不在子进程尚未关闭时清除其现场。guard完成回执缺失则记录cleanup deferred。

launcher及probe的最终scalar摘要上限为90000 UTF-8字节。正常标量摘要不重复完整原事件，原事件在compute日志逐条保留。任何因超限而删字段的fallback均明确 `summary_complete=false`、`transport_complete=false`、exit70；最终仍超限则打印失败收据并退出70。fallback保实际末态/范数/未访问后缀、fresh replay、stage-J与尚未付endpoint/audit标志，不把传输错误变成科学成功。

`procedure_complete` 只说明受控来源调用返回；数学 `stop_reason`、worker/guard退出码、source错误和transport状态分别报告。launcher无工程错误时可以受控返回0，即使数学结果为资源partial或十档拒绝；独立owner实际退出码/stop reason仍完整保留。因此绿色job不能解读为native成功。

最终probe写 `GITHUB_OUTPUT` 的 `scalar_summary`、`scalar_summary_bytes`、`scalar_summary_sha256`。bytes/SHA仅覆盖JSON payload，不含多行分隔LF。root可用独立report job只打印该小JSON，无raw上传；若科学step失败也应尝试报告已形成的真实小输出。

## 11. 公开 Actions 接线

在固定science checkout核所有源后，沿122既有流程：取真实91输入；恢复两ready；恢复78原source topic；使用原3b8 rules runner并读当前已知双README基线；每2700秒真实pull/rebase同步，规则变更按原helper停科学。镜像与science checkout分开，不能重标发生过未实际执行的pull。Git设置 `merge.stat=false`，防恢复历史raw删除造成无用diffstat。

核心命令为：

```bash
python computations/geometry_20261115_native_persistent128_probe.py \
  --original91-directory ACTUAL91_DIRECTORY \
  --source-topic RESTORED78_SOURCE_TOPIC \
  --seconds 18000 --threads 4 \
  --fresh-replay-reserve-seconds 1200 \
  --matched-trace none --final-stage-columns 0 \
  --out NEW_RUNNER_TEMP_DIRECTORY
```

实际目录由工作流给出。无未来run/result/accepted状态硬编码。原heap6144、首fresh64 exact workers2、max-factor-bytes2147483648与η1保留。root负责唯一workflow/request、Git与派发；本接口及源码准备不构成新的数学通过门。

## 12. 此次源码完成度

已做Python AST、纯字符串源码构造及逆向身份、Node `--check`、C++ `-fsyntax-only`；未编译可执行程序、未运行数值fixture、未导入科学适配器求任何root/J/QR/范数。相对root已读四源的完整diff和静态回执在临时目录，可从已发布源码重得，不作为需存储的数据结果。

最后修改集中于原事件先输出、90KB传输错误诚实退出、未执行后缀和异常时已有原行的保全。冻结原113/R283函数原件保持；新增调用者持有evaluation视图及外层catch的精确差异、完整逆向字节身份另列，R273数学不改。此次交付是可运行实现及明确边界，实际下降、原阈值、终态J和完整native责任必须由之后真实输出分别说明。
