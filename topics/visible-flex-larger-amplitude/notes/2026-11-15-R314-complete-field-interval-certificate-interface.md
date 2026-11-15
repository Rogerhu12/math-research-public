# R314/R325 独立完整 field 严格证书：可执行接口

## 1. 本次实现与当前运行的关系

本包实现一个独立的同 job 消费者：从仍在现场的真实 persistent128 owner 末态，按明确 stage/RK-step/field 重做该 cell 的原 primal 前缀，记录所选 field 的成功有限 root trace；随后对该 trace 的准确实扩展做整数向外区间后验验证。

它不改 request140、145、原113、R283、R302、R305 或原 owner。没有当前数值证书、没有未来 run/接受值。实际请求号由主控预留150；源交付本身不派发。

严格验证对象是所选 field 的真实 binary128 输入字所定义的准确点。它不是从 cell 初始点直到该 field 的严格 RK 误差证明，也不是完整576段的 native 方向或112边界响应。完整226输出、224 shape输入列与可选6独立几何列在这个明确对象上全部保留。

## 2. 三运行源冻结表

| 文件 | bytes | SHA-256 |
|---|---:|---|
| geometry_20261115_literal_root_field_tape128.cpp | 13437 | 2aa2ad6737ca16854350967bddf49846e345ba5195d799d21dcc40a870c925bb |
| exact_20261115_literal_root_field_certificate.py | 40570 | 659ecdc003eb54a4fc22b8b42828a2b33f576690559de14b7cde54d7efe11849 |
| geometry_20261115_literal_root_field_certificate.py | 18294 | cd73cb044e72052b38c6fc9d6517a7e436517f15777a4ace74333bb8a92af596 |

上述三件均为独立新文件。旧数学文件原 bytes 不改。

导出器包含原 R305 header，header 又包含原 R302 shared trace 与 R283 完整前缀。两个带记录的方向函数只增加已形成向量的写出。剥去记录语句、函数名及路径参数后，正文逐字回到原函数：

- 原 returned_L_direction 正文 SHA：fba46dc785a45495bbc8a8d01747e01de709e1de3375e3f989c001380d7a14eb；
- 原 rhs_direction_operator 正文 SHA：acae4c18fc49c580fba448d535bf8925a32804fde8bb7547766ec51f5bd40ace。

这些是源字符串逆向核，不是数学执行或数值 fixture。当前终端不可用，未本地编译 C++、未运行 Python AST、未导入或执行任何科学函数。实际编译、语法检查与科学运行只放 Actions。

## 3. 已发表基础与闭包

核心数学来源如下：

| 文件 | SHA-256 |
|---|---|
| geometry_20261115_native_primal128.cpp | 1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d |
| geometry_20261115_native_trace_variation128.cpp | 8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d |
| geometry_20261115_native_shared_trace128.hpp | bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b |
| geometry_20261115_native_operator_trace128.hpp | 950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0 |
| geometry_20261115_native_final128_components.py | ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045 |

前四完整文本分别来自公开 d70e89b2 与 ea24ec16；原 input binder 为 d70e89b2 的最后一件。launcher 复用其 bind_inputs(component=stages) 与已读 descendant process stopper。因该 binder 原本核十二源，实际闭包必须完整提供其 PINS，再加入 R305 header 与三新源。某旧组件仅作来源核而未执行，不因此称其科学已支付；实际 command 列出本次编译/调用的文件。

生成 include 的方法完全沿原完整前缀：在原 R283 唯一独立 main 前截取；该前缀 SHA 必须是

fd676b38fbc83abeccf85ca6956b325d15b26425f9147e3d52d2283cd1ae4956。

编译使用 g++、GNU++17、O3、OpenMP、frounding-math、ffp-contract=off、fno-fast-math 与 quadmath。这里沿已发表 R305 的 O3 标志，不声称原113所有编译命令逐字相同。实际编译 stdout/stderr、进程状态、全部源及生成前缀 SHA 均记录。

## 4. 真现场输入与无接受门绑定

launcher 接收以下五组 path/SHA：

1. 原 QPR11301 packet；
2. 原 packet-binding；
3. 实际执行 owner 的 source；
4. 同 job 实际 owner summary；
5. 仍存在的全部577×224 binary128 state。

原 binder 核同一 GITHUB_REPOSITORY/RUN_ID/RUN_ATTEMPT/SHA、原 call identity、packet/binding、owner原 source及固定CPP、末state原 bytes、state没有回写binary64等。原 owner 可为容差达到、预算停止或其它诚实末点；绑定不要求 native 接受。

必须在 owner 原清理前调用。已经删除的 state 只有 SHA 时不能使用本入口；另一个 run 的 raw 也不能伪装为本 job 现场。若后继请求重新执行原 fresh64→R273→persistent128，则该新 owner 的实际末点与新 run 身份重新绑定。

严格 consumer 在输入阶段再次核全部临时 manifest 与五输入 bytes/SHA；保原 state/packet/owner关系，并精确比较每一个 frequency/cos/sin/225Gram 的 binary64→binary128 lift。它还从完整 packet 找到所选 stage/step 的实际几何5字、mu/ratio/h，逐字核入当前 constants。原 policy 的stop/fallback字必须仍是原常量字。

## 5. 导出器选择与真实记录

C++ 参数顺序为：

    executable PACKET CURRENT_STATE OUT SECONDS STAGE RK_STEP FIELD POLICY COLUMNS

POLICY 为 original 或 refined。COLUMNS 为 state224 或 state224-plus-environment6。

从原 node stage+1 的224个state字、原两个零mean初值开始，逐原 atomic RK 步重放至指定 field。四个field的输入严格沿原括号：a原输入、b使用h*a/2、c使用h*b/2、d使用h*c。每个原 root 分支搜索只真实执行一次；其成功已接受 Newton 更新、原F/C、实际名义Cholesky与两回代字进入 tape。原30×20及原两种policy范围不改。

选择一个内部 field 后，导出的独立输入Jacobian是**该 field 输入坐标的224个单位列**，不是已从 cell 初始状态传播到该 field 的224列。初始均值输入两列未请求；完整226输出含mean两行仍保。

六个可选列固定为：

| 列 | 独立方向 |
|---|---|
| 0–223 | 当前field的224 shape坐标 |
| 224 | r |
| 225 | r' |
| 226 | w |
| 227 | w2 |
| 228 | E |
| 229 | mu |

这些几何变量独立，绝不令 w2=w*w 或代入未付的连续E导数。真实 profile 参数、采样位置、dh/ratio及拓扑方向另有其责任。

每个完整 nominal column 最后才写 complete.json。若某列中途出错/预算结束，不制造完整方向；报告 columns_completed 与未访问后缀。成功 root tape 已完成但只有部分列时，严格消费者可保已完成列，不能用它们冒全224。

## 6. 临时数据与输出schema

导出 schema：

- literal-root-field-tape-v1；
- literal-root-field-export-result-v1；
- literal-root-field-evidence-binding-v1；
- literal-root-field-temporary-files-v1。

主要原 arrays 全为 little-endian binary128：

- frequency112、cosine N×113、sine N×112、独立Gram N×225；
- constants17：sq2/sq12/floor/outertol/原stop/原fallback/orientation，当前r/dr/w/w2/E/mu/ratio/h，选定policy的stop/fallback；
- field输入226、名义target113、返回e113/L113/F113、名义RHS226与flux112；
- 每个成功update的e113/F113/C113²/Lc113²/forward113/solve113与实际backtrack；
- 每列完整seed226/env6、每update的target/de/dF/225beta/dC-action/rhs/dsolve与末L方向113、RHS方向226。

root-trace.jsonl 保重放前缀与所选field实际root事件。manifest遍历完整已写文件，不假称某未写方向可从hash恢复。

严格证书主schema：

literal-root-fixed-trace-field-interval-certificate-v1。

launcher主schema：

literal-root-field-certificate-launch-v1。

large-arrays 仅为同job临时区间、nominal字与证书细目，不上传artifact/Release/Git。公开保源、参数、实际run/source、输入/outputSHA及紧凑原结论。若显式 retain-temporary-for-same-job，原调用者仍负责本job末清理。

## 7. 严格算术及数学范围

consumer 使用stdlib整数定点闭区间。端点是整数乘2的负bits次幂；乘法/商均显式向下和向上，sqrt用整数isqrt加平方比较。默认320bits，可显式160–4096。精度改变验证成本/包围宽度，不改变原F/C、原rootpolicy或求解接受门。

每次实际已选更新：

1. 从当前准确trace的e盒与完整物理输入形成真F/C盒与angular局部严格偏导；
2. 全113×113 interval Cholesky正pivot证明准确Cholesky域；
3. 从名义Lc候选构造dyadic Y，严格形成全矩阵 N≥|I−YC|；只有q=max行和<1才给inverse界；
4. 对完整残差 C*s帽−F，用12个正Neumann项及其严格余项，得到准确s的盒；
5. e←e−实际α*s盒；
6. 对每列完整dF、225Gram方向、dC*s盒形成rhs并作同一inverse包围，再更新de。

其中 dC*s盒包含准确primal solve误差，不设名义factor/forward/backward残差导数为零。

纯形成缺陷另在实际名义e字处计算，和上述传播e盒的额外不确定性分开。完整 factor、forward、backward、F/C形成、直接/分解solve残差逐行保存。两个区间形式包同一真实残差，不要求区间端点逐字相等。

返回后按原全226 RHS对值/方向作完整外包。所有列都与实际名义R305数值方向逐行相减形成误差区间；全部两mean保留。C始终独立Gram矩阵，不代替真实F_e。

[R325](../results/R325-complete-literal-field-interval-enclosures-for-fixed-root-traces.md) 给完整包含性与有限Neumann余项证明；[R314](../results/R314-verified-posteriori-bounds-for-literal-root-traces-and-directions.md) 给其更广范围的后验责任。

## 8. 未决、partial和原native的区别

下列字段互不代替：

| 字段 | 含义 |
|---|---|
| tape_ready | 实际选定field的成功finite-root原记录存在 |
| fixed_trace_primal_field_certified | 所有记录更新与全部226 RHS的准确实盒已证 |
| requested_columns_certified | 所请求列全完成 |
| complete_224_shape_columns_certified | 完整0–223 shape列已证 |
| complete_6_independent_environment_columns_certified | 实际完整230列中六几何列也已证 |
| unresolved | 域/SPD/inverse比较或原列缺失未能支付 |
| budget_exhausted | 真实资源停止，不能补未访问后缀 |
| summary_complete | 紧凑传输是否完整；overflow须exit70 |
| native_accepted | 本消费者始终false，不覆写原owner结果 |

dynamic_branch_stability_proved、actual_equation_root_enclosure_proved、complete_RK_stage_certified、complete_576_stage_columns_certified、complete_cut_stage_far_129248_certified、complete_112_boundary_response_certified、original_physical_audit_completed 均保持false。

这不是把物理责任删掉，而是准确记录本次只支付所选完整field的固定trace。后续要得到stage/129248/112/338/finalaudit，须真正传播相应完整链。q≥1或区间过宽不证明原C奇异，也不证明原问题无解。

## 9. 可直接执行的launcher CLI

    python geometry_20261115_literal_root_field_certificate.py \
      --packet ACTUAL_PACKET --expected-packet-sha256 ACTUAL_SHA \
      --packet-binding ACTUAL_BINDING --expected-packet-binding-sha256 ACTUAL_SHA \
      --owner-source ACTUAL_OWNER_SOURCE --expected-owner-source-sha256 ACTUAL_SHA \
      --owner-summary ACTUAL_OWNER_SUMMARY --expected-owner-summary-sha256 ACTUAL_SHA \
      --state ACTUAL_CURRENT_F128 --expected-state-sha256 ACTUAL_SHA \
      --stage DECLARED_STAGE --RK-step DECLARED_STEP --field DECLARED_FIELD \
      --policy original --columns 230 --bits 320 \
      --export-seconds EXPLICIT_CAP --certificate-seconds EXPLICIT_CAP \
      --certificate-reserve-seconds EXPLICIT_RESERVE \
      --total-seconds EXPLICIT_COMPONENT_TOTAL \
      --absolute-deadline-unix ACTUAL_GLOBAL_DEADLINE \
      --out FRESH_RUNNER_TEMP_DIRECTORY

这些 ACTUAL 值必须从同job原件形成，不能在请求中填未来SHA。stage/step/field选择是本次诊断参数，完整native的最坏行不由本消费者重新挑选。

可直接调用严格consumer：

    python exact_20261115_literal_root_field_certificate.py \
      --tape-directory ACTUAL_TAPE --binding-sha256 ACTUAL_SHA \
      --bits 320 --seconds EXPLICIT_CAP --first-column 0 --columns 230 \
      --out FRESH_CERTIFICATE_DIRECTORY

它会自行检查GITHUB_ACTIONS/公开仓库及同jobowner绑定。不是可以在本地运行的byte-only入口。

## 10. 生命周期与预算

同一组件总期限从launcher开始，另受显式global绝对期限裁剪。binding/读取/编译/重放/全部方向/严格验证都消耗该总量；不是每个阶段各自重新给总时间。

编译最多300秒。导出与certificate各有显式科学cap，导出之前保留certificate reserve；还保30秒局部清理/读回。实际可用时间不足时不启动该阶段，报告resource-partial。进程继承原规则runner进程组；超时沿已发表PID/starttime后代身份停止，不能留下独立科学后台。

本包不假设某个field或230列能在给定预算内完成。首次真实运行前没有性能证据；完整各列/更新后的进度由原记录逐个输出。若尚未得到完整field，后续列不得伪补。stderr逐字保有界文本并保完整SHA；长stderr明确只保身份，不能说已经全文读。

summary先保原结果，再作90KB上界传输。任何删字段fallback都显式summary_complete=false并exit70；scientific flags与transport状态区分。完整失败/预算原因及未访问后缀保留，不因为procedure正常结束就称证书成功。

主控后续可从原91来源重新执行fresh64当前J/R273/持久128到真实末态，在其清理前调用本入口。该新request须从science开始给全局期限，包含fresh前置；不能只给此组件重新计时后遗漏原耗时。当前140/145不因本包被修改、取消或加门。

## 11. 当前交付状态

已完成三完整源码、精确来源/CLI/作用域、两个记录函数全文逆向一致核、R325包含性证明。未本地语法执行、未编译、未科学运行、未假造任何actualtape或证书。原source已由公开blob读取，新的<100KB文本仅以blob交主控；Git/ref/dispatch仍由主控统一完成。
