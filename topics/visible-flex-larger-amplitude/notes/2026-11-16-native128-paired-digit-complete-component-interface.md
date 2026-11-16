# R522：原全stage双输出整数核的完整组件接口

作者：ChatGPT /root（AI 协作），2026-11-16 UTC。

**已完成源、条件证明和实际组件调用接线；没有编译、科学运行、新request或性能结果。** [R522](../results/R522-complete-dyadic-matrix-pairs-and-shared-integer-plane-loads.md)的局部字等价仅针对原R414完整准确dyadic dot后一次RN113。本文明确真正文件、生成次序、compiler来源、原必要读回责任和未接的外层。

## 1. 本次五份文件

| topic内路径 | B / SHA256 |
|---|---|
| computations/geometry_20261116_native_paired_exact_digit128.hpp | 8729 / 480b1b9a197659722dfa19f8f3e491939b13b414fc60e63f9265b30aa20b1d47 |
| computations/root_20261116_native128_paired_digit_source_views.py | 10717 / 1554a5e5fb80f382c382aa6530b19b1bfc7b065371e96d66847195ecc396dfce |
| notes/r522-native128-paired-digit-source-plan.json | 16347 / 724e46e0d70aefd70309e03d77d4719666058e56001c7a78f7544bada76b9ce7 |
| results/R522-complete-dyadic-matrix-pairs-and-shared-integer-plane-loads.md | 14577 / 12db5415ef190e70c9683c3517df652b72744173006274b6e944487a0d006702 |
| 本接口 | 发布清单给真实完整身份，不在自身嵌入自身SHA |

三份展开view合计75913B，仅在未来Actions中生成，不额外保存到Git/Release/artifact。原数组、root tape、原科学现场没有新增永久副本。

## 2. 实际新kernel与范围

新namespace为paired_digit128。两个实际接口是：

~~~cpp
std::array<__float128,2> dot_pair(
    const exact_digit_simd128::PackedVector &left,
    const exact_digit_simd128::PackedVector &right0,
    const exact_digit_simd128::PackedVector &right1,
    exact_digit_simd128::Stats &statistics,
    exact_digit_simd128::Poll poll = nullptr);

std::vector<__float128> multiply(
    const __float128 *left, const __float128 *right,
    size_t rows, size_t inner, size_t columns,
    exact_digit_simd128::Stats &statistics,
    exact_digit_simd128::Poll poll = nullptr);
~~~

它直接包含原9006/1695 SIMD头，其原18871/5c2a完整decoder/packing/ExactSum/rounder仍由原include提供。没有替代binary128格式、设固定六limb或用double/FMA近似。

只有三个输入全部packed且非全零时共同循环；任一个全零或wide则对两个输出依原顺序调用原完整dot。只有一个右列某层active时调用原单partial；两层都active才共享左平面的load/odd shift。矩阵每行所有两列和奇数末列均写出；奇尾沿原完整dot。空维度、shape/null检查、所有原packing顺序与64MiB digit预算保留。

全部完整输出点积与原R414字等价，含subnormal/负非零下溢/准确抵消/+0和原带符号infinity。非有限输入由原decode处理；原matrix finite检查保，不将infinity变成stage通过。资源异常先后、NaN payload、日志和whole-run trace不在逐字命题内。

原GNU x86 runtime dispatch能用AVX2时才进入target("avx2")函数；否则完整scalar。没有全局target flag、外部BLAS、GPU或新数值依赖。没有实际硬件选择或速度数据。

## 3. 真实三view及完整来源计划

| role / 新basename | B / SHA256 |
|---|---|
| operator / geometry_20261116_native_paired_digit_operator_trace128.hpp | 29617 / 082d5a1fdd900071fb1cc008304c5a4c97bce92b173851bda1514ec1682eb7be |
| stage / geometry_20261116_native_paired_digit_stage128.cpp | 12880 / 49a7e226eadc7748d5d2b3f94119c2e4dd7024348e6878c673e73b1a33db3b55 |
| component / geometry_20261116_live128_paired_digit_final_components.py | 33416 / 93ecdd833922f833bdb50a8f264bc5db1913f5ce16dbb0cb4f7fbc7d285070f1 |

Operator来源为原29035/b183eeec，5个明确literal项：include、guard、完整multiply、RightCache全列循环和必要范围标记。它保simd_digit_trace128 namespace及原BatchStats；准确所有coefficients/RK/nominalfactor/C readback/两mean都不换正文。

Stage来源为真正R445 12691/eca87efc，3个literal项：新operator include、两个schema字符串及新范围标记。原576范围、atomic steps、226状态、224方向、原CLI参数处理、OpenMP、stage输出/错误/pending不变。

Component来源为原32027/2369787d。首先完整读取R515已发表8662/5950052f计划的component_layer，按原5项形成0a7f中间文本并核32429B完整SHA；该中间只是文本，不被import/执行。随后本条15项接实际new HEADER/STAGE/PAIR_KERNEL、保原祖先pin、同步schema和编译收据。R515实际物理adapter22e64c73及缓存header959d43bf保持原件，原完整四组件都继续调用。

计划列19个实际public输入，含R515 metadata计划；generator自身单独完整绑定。19不是任意动态import的自动闭包证明。原base组件的完整closure/原R283prefix及原物理CPP/头依旧由caller供应，实际组件load_baseline/source_receipts按原合同读核。新操作没有把源计划JSON装成可执行Python名单。

## 4. generator的完整调用

Generator schema：R522-native128-paired-digit-source-preparation-v1。

Plan schema：R522-native128-paired-digit-complete-component-source-plan-v1。

未来实际公开Actions中，原caller已拥有一个真实RUNNER_TEMP namespace后：

~~~bash
python "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations/root_20261116_native128_paired_digit_source_views.py" \
  --computations "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations" \
  --namespace "$EXISTING_OWNED_NAMESPACE" \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/r522-native128-paired-digit-source-plan.json" \
  --plan-sha256 724e46e0d70aefd70309e03d77d4719666058e56001c7a78f7544bada76b9ce7 \
  --out "$EXISTING_OWNED_NAMESPACE/R522-source-view-metadata"
~~~

EXISTING_OWNED_NAMESPACE须由真实原owner给出，以上不伪填一个已存在科学现场。Generator检查公开repository、GITHUB_ACTIONS、真实computations等于自己的HERE、实际Git HEAD等于GITHUB_SHA。namespace须已存在于RUNNER_TEMP下；out须为其中全新子目录。路径/环境在out创建前失败时没有成功receipt。

它把所有baseline和public输入完整读核，全部新字面文本先在内存形成并核完整SHA，随后exclusive create三个互异新名。每一真实写出后立即写source-views.json；错误保存已写views和明确not_generated后缀，不覆盖原文件。R515中间不另写出，已有R518的0a7f文件即使存在也不被替换。

没有import、AST、compile、root/RHS/FFT、worker启动或科学时钟创建。metadata elapsed只记源准备过程，不是科学总预算。实际运行若须计入某个既有总钟，由caller的原绝对clock承担，不可因该函数无clock便另开科学时间。

成功GITHUB_OUTPUT：

~~~text
paired_digit_component=<真实新component绝对路径>
paired_digit_component_sha256=93ecdd833922f833bdb50a8f264bc5db1913f5ce16dbb0cb4f7fbc7d285070f1
paired_digit_source_receipt=<原namespace中的source-views.json>
paired_digit_source_receipt_sha256=<实际生成receipt的完整SHA>
~~~

单份完整source返回帧为BEGIN/END_R522_NATIVE128_PAIRED_DIGIT_SOURCE，最多90000B。超限return70，只报告原件身份/实际尝试bytes/SHA及完整body未返，不拆、编码或截断成功。complete和transport_complete分列；源码已写不等于必要正文已返回或科学已起。

## 5. 实际组件CLI保留

生成组件仍是原真实可执行主流程，参数与原R515/R493 complete component相同。为避免伪造不存在的状态，真实参数由原caller从当前同call现场形成；本页不提供空的packet/state/parent冒“可运行实例”。

原实际 argparse 合同逐项保留：

| 参数 | 实际责任 |
|---|---|
| --component | 必填；stages、boundary、endpoint、audit |
| --packet / --expected-packet-sha256 | 原当前literal packet和真实完整SHA |
| --packet-binding / --expected-packet-binding-sha256 | 原packet绑定 |
| --owner-summary / --expected-owner-summary-sha256 | 原实际owner summary |
| --owner-source / --expected-owner-source-sha256 | 原实际owner源码 |
| --state / --expected-state-sha256 | 原同call完整binary128末state |
| --physical-packet / --expected-physical-packet-sha256 | 原物理packet，按原component适用 |
| --physical-binding / --expected-physical-binding-sha256 | 对应完整binding |
| --original-source-root | 原可选源码根合同 |
| --stage-output / --expected-stage-summary-sha256 | boundary消费同source真实完整stage |
| --boundary-output / --expected-boundary-summary-sha256 | endpoint消费同source真实完整boundary |
| --seconds | 必填；含绑定/编译的原component总wall allowance |
| --scientific-seconds-cap | 原主C++的可选独立上限，不增加总clock |
| --absolute-deadline-monotonic | 原同host父绝对clock；实际入口继续明确传入 |
| --threads | 必填，原1至4范围 |
| --first-stage / --stages | 原默认0/576；完整入口继续全576 |
| --first-column / --columns | 原默认0/224；完整入口继续全224 |
| --reference-columns | 原默认none；仅原显式诊断，不新增门 |
| --retain-temporary-for-same-job | 原完整caller必须继续传入，直到必要读回及quiet |
| --out | 必填，真实原RUNNER_TEMP下fresh输出 |

原source允许由wrapper前置--operator-components，仍按原分支弹出该标志。原参数范围、原错误、当前stage/column矩形校验和原component deadline形成完全未改。命令参数名不能用binding/owner等同义名替代。

所有固定输入/packet/schema/range绑定仍由原base.bind_inputs执行；本组件没有创建或恢复另一H。原full112 caller仍请求576段、全部224列和原226局部行，不能因CLI本来允许rectangle便缩小实际科学范围。

本条没有发布request或owner/pipeline替换件。R518实际owner的COMPONENTS名称/SHA/schema、assembly的对应tuple和reader尚指其原0a7f。后继完整入口必须同步真实新tuple和三view生成次序；原221或215不会自动使用本条文件。这个来源注册责任不构成原运行的新接受门。

## 6. 真实编译及准备收据

新component的STAGE_SCHEMA是R522-native-persistent128-complete-paired-dyadic-stage-maps-v1，主schema是R522-live128-paired-digit-final-components-launch-v1。Actual stage收到、写出和上层核验的schema同步，旧eca原件仍只作祖先。

原compile_stage形成完整原R283prefix后，以原g++ flags调用真实新stage：gnu++17、O3、OpenMP、frounding-math、ffp-contract=off、fno-fast-math，原300秒cap/同process manager/原stdout-stderr处理保。七个实际stage compiler copy包括newoperator/newkernel、原R405/R414、qualified recorded/hoisted和newstage；原general-geometry fallback另照旧qualified复制。

新准备收据：

~~~text
compile/paired-digit-source-binding.json
schema = R522-native128-paired-digit-operator-compiler-input-v1
returned process key = paired_digit_compile_source_binding
~~~

它保actual_launcher、actual_exact_digit_sources逐file原/执行身份、原R283prefix、原/实际argv、原qualified fallback、原eca和b183祖先、scientific_budgets_unchanged及local_runtime_validation_claimed=false。

该文件在原process manager调用前形成，所以不能从其存在推编译已经启动或成功。真正返回行在原compile.process和lifecycle内，含原started/returncode/timeout/elapsed及新binding key；未返回行只按实际部分状态处理。新组件仍将完整summary/实际source字节留原same-job目录，不用source receipt填数值值。

R515物理编译仍使用其physical-radial-mode-cache-source-binding.json与live128_physical_radial_mode_cache_source_binding，和本条stage binding区分。旧prepared ancestor CPP与实际CPP区分不变。两份receipt不能互相替代。

## 7. 原必要读回与后继责任

当前component本地bounded_view仍只是owner到parent的索引，真正scientific_report、全stage-accounting、所有四component、source/compile/lifecycle、temporary manifest都在完整原summary。单90KB的原超限处理不放宽。

后继完整necessary reader应消费真实新component/source/schema并正向选择stage的paired-digit-source-binding和实际返回行；它仍须保原FD/fullDN/全部trial/错误/partial/未访及原source范围。不能因为R518 reader已经认识R515 physical receipt就假定它认识本条新stage key。当前发表没有静默替换reader。

统计沿原Stats逐实际输出计数；新增operator标记明确pair实现、原one-row reservation、zero/wide/odd-tail后备和每pair至多两个原2048项block。乘法数与两份逻辑partial保持各自意义；shared load没有让224列变112列。

Source identity、compile return、四component complete、FD与fullDN accepted继续分别由原实际字段支付。内核的字等价不补严格continuous derivative、不改变原mixed-J合同、不减少两mean或独立audit。必要未返的原raw不能用SHA恢复内容。

## 8. 时间、所有权和清理

新kernel只调用既有poll function，最大共享reducer工作为两个原2048项整数block；没有私有time、科学budget或clock reset。实际有限时间下的完成范围可能与旧运行不同，原外部owner timeout/TERM→KILL/reap/quiet全部须由实际caller照旧执行。本文不宣称poll即硬实时终止。

Generator不启动科学进程、不创建owner、不写quiet/cleanup成功marker、不删除raw。Component原保留/清理行为没有改变，未来full caller必须继续传原retain选项并完成单份necessary与再次quiet才按原合同清理。不得以某个source-return或compiler receipt代替完整科学读回。

本次没有新的预算数值、初猜、科学门、预检对拍、benchmark或workflow。仅source证明已完；actual input/owner/请求源链连接、编译、完整科学结果、真实速度和README剩余各项都没有被预填。
