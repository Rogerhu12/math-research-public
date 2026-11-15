# R305 原有限 root trace 的共享角点算子与完整 final 消费接口

作者：GPT-6 Astra Pro（exact_refinement）  
日期：2026-11-15  
类型：独立算法实现/接口；Python AST 与源字节已核，C++ 尚未编译，科学尚未运行

## 1. 目的与当前事实

actual133 已真实用 current128 residual 形成完整 R273 RHS，持久 binary128 更新在唯一一次 $\alpha=1$ 试探后达到原 shooting tolerance，独立完整 replay 逐字一致；完整 stage 导数、338×112 endpoint 和物理 audit 尚未支付，见 [R308](../results/R308-actual133-persistent128-shooting-tolerance-and-identical-fresh-replay.md)。actual122 的单个方向读回仍花费很大，见 [R303](../results/R303-actual122-partial-finite-root-directions-and-controlled-stop.md)。因此本组只改进完整有限 trace 导数的重复工作，不改 actual133 的接受路径，不调原容差，不改正在运行的 request137。

本实现的严格解析对象是 [R305](../results/R305-literal-gram-root-contraction-and-nominal-factor-defects.md) 中固定成功分支的准确实表达式。新方向算法复用真实 primal 的接受更新、名义 Cholesky 与两回代结果，并采用共享角点偏导和 $dC\,s$ 收缩。它与旧逐 $dL_c$ 链在准确实算术中有同一对象；它们的 binary128 运算顺序不同。

明确不主张：IEEE 离散 rounding map 的导数、旧逐 $dL_c$ 链的 word 等价、名义分解残差导数为零、完整导数误差界、branch stability、native/fullDN 接受。未运行的新实现也没有实测速率或完整224列能在一次 job 内完成的保证。

## 2. 三个独立运行源

所有文件与既有计算源同放 `topics/visible-flex-larger-amplitude/computations/`；旧源不修改。

| 新源 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261115_native_operator_trace128.hpp` | 24617 | `950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0` |
| `geometry_20261115_native_operator_stage128.cpp` | 10682 | `86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926` |
| `geometry_20261115_native_operator_final128.py` | 21548 | `a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef` |

两个新 schema：

- 原 stage 科学报告：`native-persistent128-shared-angular-contracted-trace-stage-maps-v1`。
- 新 launcher 及后继身份：`native-persistent128-contracted-trace-final-components-launch-v1`。

新 stage 的 binary128 payload 文件名和矩阵顺序与 R302 的完整 stage 数据接口相同；schema 和 source 明确不同。旧 `ddbe` launcher 不能把它当旧 stage 输出直接读入。新 launcher 的 `validate_prior` 只接本新 schema、同一新 source closure、同一实际 owner/state，并把此来源一路保留到 boundary/endpoint 消费中。

原三个后继科学程序内部报告 schema 不改，外层新 wrapper 同时给出它们的准确来源和新 stage 数值实现身份；这不把旧源改名成新实现。

## 3. 真实输入：必须在当前 owner 清理前取得

新 launcher 用已冻结 `geometry_20261115_native_final128_components.py`（`ddbe1a49…`）的 `bind_inputs`，没有另造来源或成功锚。

每次必需五个原文件及其实际 SHA：

1. 完整 primal packet。
2. packet binding。
3. 真正 owner summary。
4. 真正 owner launcher source。
5. 完整577×224 binary128末状态。

原 binder 逐字验证 packet/table布局、owner源码与 CPP、owner实际 call/config 身份、全部状态 bytes，并核对当前 `GITHUB_REPOSITORY/RUN_ID/RUN_ATTEMPT/SHA` 与 owner 的 run 相同。状态文件必须是实际2067968字节，不能从 decimal、JSON、64位数组或已删 raw 的 SHA 伪恢复。

owner 可以是已达到 shooting 容差的点，也可以是明确失败/预算部分点；身份 binder 不增加 residual 门，也不要求 `native_accepted=true`。源必须仍证明状态未 roundtrip binary64。

actual133 的已清理末状态不能用其 SHA 直接续接。本实现需要同 job 清理前的真实现场，或按原来源重新运行得到的新现场；新 run 的真实 SHA 必须运行时取得。没有预填 future owner、run、残差或成功状态。

boundary/endpoint/audit 另要求 R302 原 physical packet、binding、原源码根；既有 binder 会逐块核完整 physical geometry/table/query schedule 与原源码。physical packet exporter 不执行新 root/J/solve/audit。

## 4. 完整 primal 和 literal 表如何保持

新 header 包含冻结 R302 `native_shared_trace128.hpp`；实际 primal 仍调用原 `capture_field/capture_root`。root 的30次外循环、20档内部回溯、原 root stop/fallback、所有真 guard 和失败语义均来自冻结 R283/113 前缀；实际成功更新最多29次的边界不改变。

每个 RK field 的原 branch search、原 $F$、独立 $C$、Cholesky 和两回代只执行一次，保存真正 tape。每列不再执行完整 $F/C$ 的 value shadow 或完整 $dL_c$ 分解链。

保留全部独立 literal64 表提升后的 words：cosine、sine、Gram、frequency、orientation、平方根常数，以及完整 geometry 的 $r,dr,w,w^2,E$、cell $\mu$、每原 RK 步长及 port ratio。特别是 $w^2$ 和 $E$ 不从 $w$ 重新定义；Gram 表不换成 cosine 外积；$C$ 不假设等于 $F_e$。

四个原 RK primal field 按原顺序先完整计算，所有226维状态和两个 mean 都保留；新方向不会反馈到 primal。原 cusp schedule、6943原子步及输入/输出节点顺序来自实际 packet，没有重新造调度表。

`prepare_point` 在每个实际用到的角点准备 $(P,P_t,L,U,w^2,E)$ 六个坐标下的局部偏导，使用原表达式的 dual arithmetic。一个角点准备的系数供全部请求列复用；常量表没有方向。实际 $K,S,D,A,\sqrt D,quad$、原 $C$ 和返回场 flux 的 value shadow 仍作源表达式一致性读取。它们属于实现一致性，不是新增非线性接受阈值。

## 5. 每个已接受 root 更新的完整收缩

设记录的更新为 $e^+=e-\alpha s$。新方向先依实际 target 与当前 $de$ 得到完整 $dL$，再形成所有113个 $dF$ 和全部225个 $d\beta$；没有丢高模、mean row 或 Gram列。准确实公式为

$$
dF=de+\frac1N\sum_n dq_n c_n,\qquad
d\beta_k=\frac1N\sum_n d\rho_n\,\Gamma_{nk}.
$$

独立原矩阵的结构作用为

$$
(dC\,s)_0=d\beta_0s_0+\sum_{j=1}^{112}\gamma_2d\beta_js_j,
$$

$$
(dC\,s)_i=\gamma_2d\beta_is_0+
\sum_{j=1}^{112}(d\beta_{|i-j|}+d\beta_{i+j})s_j,
\quad 1\le i\le112,
$$

其中 $\gamma_2$ 是 packet 的原 literal square-root word。没有形成每列完整 $dC$ 矩阵，再逐项微分一次113阶分解；改为对原记录的 $L_c$ 做两次三角求解，数值实现

$$
ds\approx (L_cL_c^T)^{-1}(dF-dC\,s),\qquad
de^+=de-\alpha ds.
$$

所有实际接受的 $\alpha$ 仍来自原 tape。初始 $de=0$，只有真实接受的 update 推进 $de$；原 fallback 返回最后实际 $e$ 时也相应返回完整 $d\tau+de$。原分支选择不求导。

准确实的等价式是 $ds=C^{-1}(dF-dC\,s)$；上面的名义 factor 数值实现不是原逐 $dL_c$ 的 word 等价式。每个已接受 root 更新完整读回 $L_cL_c^T-C$、$L_cv_c-F$、$L_c^Ts-v_c$、$Cs-F$，每个方向还读回全部113个 $Cds-(dF-dCs)$ 行。报告保原有限最大值与数量，记录 `nominal_factor_residual_derivatives_proved_zero=false`。这些数值残差不是误差外包或方向接受门。

R305 的缺陷恒等式说明为什么不能把这些残差的导数默置0。当前实现没有支付 $dR/da/db$ 的界，也没有把新/旧方向差当作准确误差证书。

## 6. 全226 RHS、一般参数方向与 port

共享算子保留完整 target、momentum、$P/P_t$、returned $L$、flux，以及所有224 shape RHS 和两个 mean RHS。返回 root 的最终 $dF$ reduction 不参与后续更新，也不是 RHS 输出，因此只省去这一未使用的 reduction；真实 primal $F$ 仍已原样计算。

header 的一般参数接口为：

- `EnvironmentDirection`：$dr_{geometry},d(dr_{geometry}),dw,d(w^2),dE,d\mu$；这里第一个量是对 geometry 半径坐标的参数方向，第二个是原 `Geometry.dr` 字段的参数方向，二者不混同。
- `StepDirections`：每列 $dh$ 及首点、中点、末点三组完整 geometry 方向；一个 cell 的 $d\mu$ 在三处必须是同一方向。
- `rk4_batch_parameters`：在原226维 RK四级中传播这些明确输入，不用不同字段互相补算。
- `post_port_direction(before,direction,ratio,ratio_direction)`：对原 Pi端口映射完整求导；shape Q不作该除法。

本 stage CLI 只执行**固定 geometry 的全部状态列**，所以一般参数输入全0，port ratio方向为0。它不声称已执行 profile/height 参数列；需要真实参数响应的 caller 必须明确提供完整 chain rule。新一般接口的存在不等于实际112边界响应已经完成。

每段输入 node $n+1$，输出 node $n$；原 stage residual 是 post-port 输出减保存 node $n$。列种子只在输入 node 的224 shape坐标，两个 mean 初值方向为0，之后完整推进。

## 7. 科学 stage 输出及部分范围

每个完成 stage 只有在所有请求列与全部原子步均返回后才写出下面五个 payload；不完整stage只保真实root事件与进度，不制造J。

| 临时文件 | binary128 C-order shape |
|---|---|
| `primal-full-output.f128` | `[226]`，port之前的原完整输出 |
| `full-columns-before-port.f128` | `[226, columns]` |
| `shape-columns-after-port.f128` | `[224, columns]` |
| `mean-columns.f128` | `[2, columns]` |
| `stage-residual.f128` | `[224]` |

完整原 residual 总文件仍为129248行，原cut112、全部stage576×224、far112顺序不变。缺少的stage段是 NaN 占位并带未完成标记，不能当零。只有576段全完成才读完整原归一化norm；只有576段且第0列起全部224列完成，才令 `complete_224_stage_columns=true`。

每个stage报告实际请求/完成状态、总原子步、已完成原子步、未完步后缀和错误。一个未完原子步可能已计算部分列/field，不能从完整步计数推断它们均未访问；本接口只承诺完整已保存的stage payload，未完成部分的真实root事件留临时日志。总报告还保实际 shared primal、成功更新、local partial、完整Gram作用、factor求解和全部线性readback行计数。

全部576×224列时，上述固定binary payload与完整 residual 总计939316736字节，另外还有root日志、summary、编译文件、manifest及后继 boundary/endpoint/audit数据。此数只是固定文件布局计数，不是完整磁盘/内存上界。root的实际回溯日志与每步tape取决于真实分支；不以actual133 maxiteration1保证下一次相同。

## 8. 可选旧链比较：诊断范围有限

`--reference-columns none` 默认不重复旧昂贵方向。可显式给全局shape列号逗号表；每个号必须落在本次请求矩形内，不能重复。

比较使用同一实际field/tape和**新传播到该field的同一切向输入**，调用冻结 R283的原逐 $dL_c$ RHS方向，保完整226维的差异最大值。它不是从stage初始独立传播整条旧链，也不是whole-stage两种J的完整比较，更不是误差界。

比较的普通错误只保 `reference_field_failures` 和原error，不能由其单独否定新算子的输出；共享墙钟预算耗尽则按真实resource partial停止。若一般geometry方向非0，旧参考接口不能表达，明确记为not applicable，不把它改成零。默认CLI的geometry方向本来就是0。

## 9. 后继完整112与338行如何接入

新 launcher 提供四种组件，实际命令和返回源分别记录：

| component | 真正科学源/输入责任 |
|---|---|
| `stages` | 新R305 stageCPP，真同job128状态，完整请求范围 |
| `boundary` | 未改 R302 boundaryCPP；必须读取新schema下同状态的完整576×224映射、两个mean行和原physical height forcing |
| `endpoint` | 未改 R302 physicalCPP；读取真完整boundary输出与原cut物理定义 |
| `audit` | 未改 R302 physicalCPP；独立读实际状态/原physical query schedule，不以stage或boundary完成为前门 |

boundary保112全部far齐次模式、577网格、完整cut/stage/far129248×112读回及两个mean；没有改成阻尼响应或只算低模。它消费的是本新数值实现的stage列，来源由wrapper显式保留。

endpoint中 local first-slope 的 RHS方向仍使用冻结R283逐 $dL_c$ 链，second/mean-second仍是原C-based物理jet程序的对称差分。由此形成的新wrapper输出是**新数值stage/boundary输入与原local endpoint程序的明确组合**；不冒作全部338行精确解析Jacobian或原64word等价。audit仍是原C-based有限物理程序的binary128提升，不把它改成有限roottrace径向导数。

原physical组件已有的 `C_equals_F_e_claimed=false`、`physical_Ldot_is_finite_root_trace_radial_derivative_claimed=false` 等限制仍保。任意单组件完成都不令 `native_accepted` 或 `fullDN_accepted` 变true。最终实际验收仍要把完整原责任与真实报告接齐；本组不加新阈值或替换原门。

## 10. Actions CLI 与真实期限

示意 stage 调用如下；所有路径/SHA来自同job实际生成的文件，不是预留值：

```bash
python -u geometry_20261115_native_operator_final128.py \
  --component stages \
  --packet "$ACTUAL_PACKET" --expected-packet-sha256 "$ACTUAL_PACKET_SHA" \
  --packet-binding "$ACTUAL_BINDING" --expected-packet-binding-sha256 "$ACTUAL_BINDING_SHA" \
  --owner-summary "$ACTUAL_OWNER_SUMMARY" --expected-owner-summary-sha256 "$ACTUAL_OWNER_SUMMARY_SHA" \
  --owner-source "$ACTUAL_OWNER_SOURCE" --expected-owner-source-sha256 "$ACTUAL_OWNER_SOURCE_SHA" \
  --state "$ACTUAL_STATE128" --expected-state-sha256 "$ACTUAL_STATE128_SHA" \
  --seconds "$COMPONENT_TOTAL_SECONDS" --threads 4 \
  --scientific-seconds-cap "$MAIN_SCIENTIFIC_SECONDS_CAP" \
  --absolute-deadline-monotonic "$PARENT_SCIENCE_DEADLINE" \
  --first-stage 0 --stages 576 --first-column 0 --columns 224 \
  --reference-columns none --retain-temporary-for-same-job \
  --out "$FRESH_RUNNER_TEMP_STAGE_OUTPUT"
```

`--seconds` 是整个组件的wall allowance，包括绑定和编译，不是科学执行之外再加时间。它被可选父级同host `time.monotonic()`绝对期限截短。父级期限应从最初fresh64 J/R273工作之前设定；launcher不能知道caller未传入的前置耗时。

可选 `--scientific-seconds-cap` 另限制主C++科学进程；实际秒数取该上限与扣除编译/读回预留后的剩余时间之小者。它让140沿用137的明确science caps，同时不因编译较快而超过这些科学上限。省略时沿原整个组件总cap约束；此项只增加资源区分，不改科学式或接受门。

每次编译上限300秒，实际再截剩余量。`g++ -std=gnu++17 -O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math`，链接quadmath；与冻结R302优化标志相同。新stage从冻结R283CPP唯一 `main` 前截出完整prefix，逐SHA核后编译；没有删root/guard或替换原表。所有编译只在Actions发生。

全组件固定预留30秒供清理/读回，每个科学进程再预留15秒受控结束；实际科学秒数由当时剩余量确定。资源不足时不启动该进程，保明确 `scientific_started=false/resource_partial=true`。编译或科学超时也保持resource身份；不能当原非线性拒绝或无解。

child继承原rules runner进程组；进程超时时复用原受控后代清理函数，按PID/starttime识别真实后代，不新建可逃过规则停止的session。新launcher不自行读写Git或同步H，仍须由公共workflow外层原规则监控包住。

boundary另传physical两文件/各SHA/原source-root、`--stage-output` 与新stage summarySHA；endpoint另传这些physical来源、`--boundary-output`及其summarySHA；audit只需physical来源和同一真实owner/state。stage/boundary中间结果用 `--retain-temporary-for-same-job` 保留供实际后继，不上传。默认完成后清理自有临时目录，仅留短compact。

## 11. 读回、清理及退出码

launcher输出marker为 `NATIVE_OPERATOR_FINAL128 `。完整原科学summary和所有临时文件生成path/size/SHA manifest；短view保总统计与全部576stage的完成/未完行表，完整每stage的细root统计留原临时报告及其SHA，不冒作短日志中已逐项展开。

bounded JSON上限90000bytes。若超限，科学状态不改，但明确 `summary_complete=false/transport_complete=false/transport_exit_code=70`；缩略view不得把缺失细节写0或猜未访索引。第二次仍超限时只发小错误身份及原full summarySHA，仍exit70，不用删除字段后exit0掩盖传输不完整。

- 0：所请求组件范围真实完整返回，短传输完整；仍非native/fullDN接受。
- 2：科学范围不完整、资源partial或实际工程/输入错误；报告保真实区别。
- 70：短传输不完整；不覆盖实际scientific completion。

依根规则15，不写artifact/Release/Git的可重算raw、完整数值报告或日志。父caller必须在仍有真实文件时消费下游，最后清理。新loader不会下载旧run，也不会以旧SHA拼一个状态。目录外的owner输入不由本launcher删除，仍由原owner/同job总控负责清理。

## 12. 固定来源闭包

新launcher直接硬锁前述新header/newstage及 `ddbe` 原组件模块；该模块的原12源 closure仍完整核对。它们是来源/绑定与可能消费者的闭包，不意味着stage-only调用执行了所有组件。实际执行范围由 `component`、完整compiler/scientific命令及lifecycle记录给出。

| 原源 | 固定SHA-256 |
|---|---|
| `geometry_20261115_native_final128_components.py` | `ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045` |
| `geometry_20261115_native_shared_trace128.hpp` | `bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b` |
| `geometry_20261115_native_batched_stage128.cpp` | `7c59da157746292d89c0857e7a0fa44bb590de1ae1a2e1b9cbea8ff18e006eab` |
| `geometry_20261115_native_boundary128.cpp` | `c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96` |
| `geometry_20261115_native_final128_packet.mjs` | `824b7440d2604e828df4326b1cef1b1bf332d203eeb7e81968704d2febdcd7c2` |
| `geometry_20261115_native_physical128.hpp` | `4b0569a245147e346149d462d974a80cac853bcf9d5abf13700b743acd33af35` |
| `geometry_20261115_native_physical_final128.cpp` | `a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415` |
| `geometry_20261115_native_trace_variation128.cpp` | `8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d` |
| `geometry_20261115_native_trace_variation128.py` | `8229212bb6804db7eee99ea661a490d3cced756e8a98471c09e22ad74cdb8b76` |
| `geometry_20261115_native_trace_variation128_bridge.mjs` | `61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7` |
| `geometry_20261115_native_primal128.cpp` | `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d` |
| `geometry_20261115_native_primal128_bridge.mjs` | `3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8` |
| `geometry_20261115_native_persistent128.cpp` | `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd` |

R283完整prefix为31738bytes / `fd676b38fbc83abeccf85ca6956b325d15b26425f9147e3d52d2283cd1ae4956`。本新source集合不改变前缀、原四133源、七个R302科学源、原137bridge/request/workflow或任何原容差。

## 13. 当前验证范围及下一实际请求

已做：完整源码阅读、Python AST、新文件及固定baseline SHA、stage相对R302完整diff。没有import科学模块、没有编译或执行C++、没有局部矩阵/范数/误差试算。新Cpp首次编译/科学结果必须由公开Actions原日志给出；编译或API错误若出现只修具体接口，不把静态未发现问题当真实成功。

原stage派生的完整diff为临时 `stage-relative-to-R302.diff`。新header/newlauncher是独立新增文件，其完整内容就是差异；静态receipt及frozen-file表均可从脚本字节重得，不必作为数值数据保存。

root预留request140供该独立实现，当前无伪造run或结果。真实137已经独立运行，其成功、partial或代价仍按原输出读取，不被本优化源提前覆盖。下一请求的实际来源、完整全局预算、编译与各组件剩余量由caller明确安排；无新的审查、fixture或数学通过门。
