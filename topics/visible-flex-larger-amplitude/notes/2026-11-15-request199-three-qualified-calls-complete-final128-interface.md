# Request199：三处明确 namespace 与正确请求号下的完整 SIMD final128 链

作者：ChatGPT（AI，amplitude 分工），2026-11-15。独立 Request199／预留实际结果R424；没有预填未来run、接受或阶段成功。入口沿原196完整科学链，只修本接口明确的源码名字解析与必要读回请求身份。旧186／190／192／193／196文件和运行均不修改。

## 1. 实际动机与两个不同工程责任

[R403](../results/R403-actual190-persistent128-acceptance-stage-compile-block-and-partial-audit.md) 已直接记录190 stage的三处 `column_environment` 未限定调用引起编译歧义；完整128 owner已真实接受和replay，并不意味着stage编译成功。独立补丁的范围和条件程序等价见 [R423](../results/R423-qualified-column-environment-calls-and-unchanged-numerical-program.md)。三处只明确调用原 `preassembled_trace128` wrapper，未更换参数、函数体或任何数值式。

[R406](../results/R406-actual192-persistent128-return-and-request-number-readback-block.md) 又直接记录192的必要reader仍检查 `request_number==190`，在科学child返回后失败；报告本体也遗留编号190。因此本请求把必要reader的这两个整数明确改199。它们是正确来源和输出身份，不是新增科学阈值。

192实际返回的owner／replay与桥状态按R406保持，其stage具体错误未读，不能因为同源风险而冒称其ADL错误已经观察。旧196有同一reader静态风险，但不预填该运行结论。199不修订旧actual，也不从旧state SHA恢复科学现场。

## 2. 八件正文及独立五源

下面七个运行／请求正文与本接口组成八件发布包。R423 proof独立登记；新header也可先作为R423的源码结论发布，199仍逐字pin它。

| 文件 basename | UTF-8 字节 | SHA256 |
|---|---:|---|
| `geometry_20261115_native_preassembled_namespace_qualified_trace128.hpp` | 24775 | `f82cd9504fc7396664941a76e687abd489aae8766482977c80a675c9e9a9b9ae` |
| `geometry_20261115_native_simd_namespace_qualified_final128.py` | 31607 | `5ccfbf1344c2d524c2a74262ff481db0d4d36c363a16f7edec90ecd0102f19a3` |
| `geometry_20261115_native_simd_namespace_qualified_final128_bridge.mjs` | 15775 | `8462ff0e94afb00a4681c1ee5d65aeb1d2aff1424f92430067fc0a5c0a419841` |
| `geometry_20261115_native_simd_namespace_qualified_final128_same_job.py` | 38369 | `d01fb2edc7af8503fc39b5bfde9d8019de22d197f81138a23e84ae077815b476` |
| `root_20261115_native_simd_namespace_qualified128_necessary.py` | 37555 | `0e494660309d7c8e001eeb51c3809e268ce0df299643863bd93be3eb5dbb9b84` |
| `public-native-simd-namespace-qualified-final128-request.json` | 67933 | `7901f228bef74811d70e93fefe3eb8bc8e70675bfc4ffcc2d841112d889125d5` |
| `visible-larger-public-native-simd-namespace-qualified-final128.yml` | 31493 | `08427667b607b75f7431144d58d3269d955dd5b903cd4f0845aa99f34657133b` |

前五个源的仓库路径均在 `topics/visible-flex-larger-amplitude/computations/`；request同目录；workflow在 `.github/workflows/`；本接口在topic `notes/`。完整 `publication-files.json` 另给每件实际路径、blob与本地字节身份，供root发布；不向Git提交这份工作清单或可重算原输出。

原196的84个source pin全部逐值保留，再增加以下5个独立源，前置表共89项：

1. `geometry_20261115_native_preassembled_namespace_qualified_trace128.hpp`；
2. `geometry_20261115_native_simd_namespace_qualified_final128.py`；
3. `geometry_20261115_native_simd_namespace_qualified_final128_bridge.mjs`；
4. `geometry_20261115_native_simd_namespace_qualified_final128_same_job.py`；
5. `root_20261115_native_simd_namespace_qualified128_necessary.py`。

84不是所有文件都作同一种数学执行。原196四个launcher／helper／bridge／reader保留为历史字节来源，不执行旧入口；原196数学 header与stage继续作实际数学源，R405及R414 kernel继续实际被include。旧190的b16只作明确的原header基线，实际编译的对应include使用本新修复正文。

## 3. 不变的科学源与精确 source-view

直接复用的核心身份如下：

| 角色 | SHA256 |
|---|---|
| 196 SIMD数学 header | `b183eeecf4f3009bf202dd0f465c8d4fdb17d8cc0ce14bb90d1ed5e6ecf485ac` |
| 196 SIMD stage C++ | `b6537c6ce86754a6a2a75eb928e543a7083fa2311eb70a4764066f2a70dda91a` |
| R405完整113bit／wide／RN kernel | `5c2a0cb17c5fedfa5fe98b193d586b2e82171de20ddc61bcbfdf04ec556329fc` |
| R414 signed even／odd SIMD kernel | `1695b945c706523036ab85d46e1db89494719ff1b5a86efe469c39d696a556e6` |
| 原190 recorded header基线 | `b16fac2b38cc873da63a759f505fde7ccf5b3b6fd9bd0f709647b65be78a7dc8` |
| 共享186 hoisted primal／fallback header | `ab246a536ba65399174aeafb56582d398c648700c51e5b0d3b11c29090c2ec4d` |
| 通用R305 fallback原源 | `950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0` |
| 原v2 JSON／统计名限定shim | `5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf` |
| 持久128 C++ owner | `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd` |

新header只在原第353–354行的三个实际调用前增加 `preassembled_trace128::`，总增69字节。将字段0／1／2的三个新词各逆换一次，全部正文恢复原24706字节b16。声明、原hoisted委托、primal、finite检查、C方向残差、两三角回代、所有stage／column循环、root／RHS／RK数学均不改变。

原196 header的 quoted include basename仍是 `geometry_20261115_native_preassembled_operator_trace128.hpp`。新launcher在自己唯一、全新的RUNNER_TEMP编译目录中执行明确来源视图：

- 核原b16文件及新24775字节f82文件全部SHA；
- 核上述3个独特调用位置及完整逆变换；
- 将新f82原字节写到原include所需basename；
- 其余SIMD header、R405／R414 kernel、共享hoisted header及stage C++原样复制；
- 仍由旧v2 qualifier生成原R305通用fallback和原四组件的限定视图；
- 原R283 prefix保持原hash，stage实际translation unit与quoted include从同目录解析。

因此实际编译目录里的旧basename不再代表旧b16字节。新 `native199-three-call-source-view-v1` 记录旧original baseline、新independently frozen source、compiled include basename、三项replacement和whole_inverse_bytes_equal_original；compiler绑定逐件保 `original`、`executed`，仅此一件 `source_bytes_unchanged=false`。其余复制件为true，不能用一个“所有header逐字不变”笼统标签盖住这个区别。

编译命令仅切到实际临时translation-unit路径；原g++、gnu++17、O3、OpenMP、frounding-math、ffp-contract=off、fno-fast-math、quadmath及include顺序保持。没有新全局mavx2／march=native／BLAS依赖。R414原runtime CPU选择与完整scalar fallback沿原源码执行，不作为科学门。

## 4. 完整当前现场与四组件仍须真做

本次仍从公开原91 artifact恢复原failed73 BASE及原完整H、state、target、577 scales、far和576cell输入；它只是初猜。artifact `14145200674`／run `43672150224` 为10267458字节／`78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`。原78源码、原两个ready环境槽及历史Gitblob原字节恢复保持，原config不被默认配置替换。

完整真实执行顺序仍是：fresh64 withJ和完整R273→一个实际当前packet及physical packet→持久128 owner的原32方向／10alpha→独立fresh replay→全576×224当前状态stage→完整112 boundary→mixed338×112 endpoint→独立原physical audit。stage或boundary未完成时，依赖它的后继不伪造输入；独立audit保原预留机会。没有用single-field或一小组列替代完整链，也没有单独benchmark／对拍fixture前门。

持久owner的原约束保留：eta CLI `1`、原tol `2e-9`、129248行、全577penalty、224shape和226完整状态。当前r128到原QR接口的显式r64投影仍只是近似方向形成，更新后owner继续保原128词，不能把状态折回64冒精化。root原30×20、原binary64 stop/fallback literal的lift、原分支与实际finite-root trace都保留。

新的namespace补丁本身没有算术改变。196原数学仍属于 [R402](../results/R402-recorded-literal-block-operator-equivalence-and-rounding-scope.md) recorded-literal名义因子线性对象和[R405](../results/R405-complete-dyadic-digits-and-once-rounded-binary128-dot-products.md)／[R414](../results/R414-complete-signed-digit-SIMD-and-RN113-equivalence.md)的完整dot条件范围：不是把名义$\widehat L\widehat L^T$当成C，不假定C是真正$F_e$，不以精确整数归约声称整条导数误差已经外包。literal sine、cosine、Gram仍独立准确lift系数，不套理想三角恒等式。

所有113bit、实际指数跨度、12limb fast边界、wide完整fallback、符号、次正规固定量子直接RN、偶奇lane及scalar tail保留。实际backend与原所有digit统计由新运行原样产生；不因源码含AVX2就声称实际用了该后端或达到29倍吞吐。原完整C*ds-right、两回代与全部finite检查保持。

endpoint仍保原first112+meanSlope的有限trace/RHS变分与其余second／meanSecond原对称差分来源区别；audit仍是原C-based物理程序，不能冒成有限root的准确径向导数或连续ODE证书。即使四有限组件complete，也不自动变为native/fullDN接受。

## 5. 独立schema、argv和实际请求号

request schema为 `public-native-persistent128-simd-namespace-qualified-final-components-request-v1`，`request_number=199`，lane为 `nativesimdqualifiedfinal128`。唯一push触发文件是本新request；旧196触发路径不改。

当前component wrapper schema：
`native-persistent128-simd-digit-qualified-namespace-final-components-launch-v1`。

当前same-job schema：
`native-persistent128-simd-digit-qualified-namespace-same-job-final-components-procedure-v1`。

原SIMD stage C++没有变化，其科学report schema仍严格为：
`native-persistent128-complete-simd-dyadic-recorded-stage-maps-v1`。

新的necessary schema：
`native-simd-digit128-qualified-namespace-complete-chain-necessary-readback-v1`。

原owner的通用 `native-persistent128-chord-launch-summary-v1` 保持；具体source_sha256、cpp_source_sha256、input/state绑定仍核本次真实入口，不能仅凭schema借旧run。entry分派仍只读取sys.argv[1]，原guard的command-tail不被错误当作当前owner入口。

workflow实际启动新same-job helper并传原参数：
`--total-seconds 19200 --readback-cleanup-reserve-seconds 120 --final-stages-seconds 8000 --final-boundary-seconds 600 --final-endpoint-seconds 600 --final-audit-seconds 1800 --seconds 6000 --threads 4 --fresh-replay-reserve-seconds 1200 --matched-trace none --final-stage-columns 0`，连同本job恢复的 `--original91-directory`、`--source-topic` 和新 `--out`。component仍用 `--operator-components` 及原全部实际packet／state／physical输入SHA和当前absolute deadline。

necessary reader现在准确检查 `request["request_number"]==199`，形成正文的 `request_number` 也是199。它不放宽或取消身份检查。所有source basename、独立schema、workflow lane、report环境变量、关闭收据文件名和最终正文marker都与199一致；旧190／192／196字符串只在其历史来源、旧source名和如 `same_small_coefficient_graph_as190_claimed=false` 的原数学范围中保留。

## 6. 完整预算、资源区别与规则同步

本请求完整保原196资源对象，未延长预算、缩列或减stage：

| 范围 | 原合同 |
|---|---:|
| 全局source factory／fresh64／owner／四组件总钟 | 19200秒 |
| owner请求上限／fresh replay预留 | 6000／1200秒 |
| stage科学cap／额外分配 | 8000／345秒 |
| boundary科学cap／额外分配 | 600／720秒 |
| endpoint科学cap／额外分配 | 600／345秒 |
| 独立audit科学cap／额外分配 | 1800／345秒 |
| 读回清理预留 | 120秒 |
| threads／QR workers／factor cap | 4／2／2147483648字节 |
| science step／job | 330／350分钟 |
| 原规则同步周期 | 2700秒 |

这是同一个monotonic绝对deadline，从fresh64前开始计费，源码恢复、当前J／R273、packet和组件实际编译全部计入；不通过换入口重设。组件总分配包含绑定、编译及内部读回，科学C++ cap另保，独立audit预留仍影响实际剩余分配。未完成可以是资源、数值或工程，依原实际字段区分；不预填能完成8000秒内全部576×224。

Python3.12.14、Node24.22.1、numpy2.3.5、scipy1.17.0、原action pins、原6144MiB堆和单线程BLAS环境保持。token只供恢复和原规则runner，进入科学child前移除，本文／source不记录凭据。2700秒真实pull/rebase及README差异停机由冻结原runner执行，当前已读根／题baseline为21bd547f56590b7f2dd279d0297efb289a9b2783／bff8aea253a9e6a7a4fac28d810ac454c5499fec。没有替换原规则执行或唯一HANDOFF规则行责任。

## 7. 一份必要summary及本次明确增加的源视图读回

reader仍只做stdlib原JSON／文本／bytes处理，不重算矩阵、norm、域或interval。它在科学child实际返回后读取本job完整owner／component临时报告，保所有实际owner trial／evaluation、原key集合及相等字典引用，缺键不当null。stage／column原完整地址与未付范围保留；只有其余原字段完全相等才共享一条内容，不能猜一个suffix代替原地址。

原successful stage大矩阵、完整列详情和原trace数组只返回identity／count；完整原文件在Actions读取后按职责清理，不经编码分片搬运。所有实际原component flags、pending／失败、source／state绑定、science70与metadata70、audit原字段和真正原error都保持。原R414 runtime backend、各even／odd／tail／scalar／wide计数及原R405统计按实际报告读回，不由有无header推断。

本reader对新编译绑定仅增加一小项必要来源：`explicit_qualified_recorded_include_views` 返回实际compiler复制表中唯一有 `explicit_qualified_source_view` 的原行，包含旧b16、新独立header和实际include字节及逆变换结果。完整compiler绑定另保原identity；不搬完整stage科学表。component两个新declared flags也按原返回值选出，不自行写入成功值。

最终只在 `BEGIN_VISIBLE199_NECESSARY_SUMMARY`／`END_VISIBLE199_NECESSARY_SUMMARY` 之间输出一份必要ASCII JSON，硬上界90000字节。实际超过或缺必要字段时诚实失败，不能截科学范围、拆块编码或把内部owner compact当最终complete。原engineering stderr／compiler stdout在临时目录完整读取，正文只给必要原行、完整身份及明确遗漏范围；科学stdout不包装成错误数据另传。没有数值预演，不能保证未来任何实际报告必小于上限。

报告job只传这份正文的bytes／SHA并打印它，或显式“summary missing”状态。新的编号修复不让缺失原组件细账变成complete。root逐值可读范围以实际必要结论为准，不声称完整大矩阵已由root逐值读完。

## 8. owner静止与清理

owner／probe／bridge均继续把原raw清理推迟到原always必要reader后。新request-owned目录为 `native-simd_qualified_digit-final128-owned-work` 及各199独立前缀；关闭收据为 `native199-child-close.json`。原generic close schema保留，source/run及当前文件路径绑定真实本次对象。

只有必要summary_complete／transport_complete／cleanup_allowed都true且原child已reap，workflow才进一步检查同uid的实际request-owned路径进程是否静止；匹配进程、不可读项或缺收据都让cleanup跳过。旧91只读父目录只在本请求自身树内按同uid加owner权限，不跟符号链接，然后才删除。不会修改或终止其他运行的目录／进程。

原raw不进Git、Release或新artifact。即使skip主动cleanup，也不承诺runner销毁后仍可恢复；未来继续数学工作需要真实重新生成现场，不能把新summary／SHA当成完整128状态。

## 9. 完整差异、冻结与未付结论

同目录 `recorded-header-complete.diff` 是对原24706字节b16的全部990字节patch；其余6份 `*.complete.diff` 分别相对已发196的launcher、helper、bridge、reader、request、workflow。reader diff除新身份／小source-view字段外，明确列两个整数190→199的修复；不改变科学读取对象或放宽错误协议。request完整保旧84值，前置89集合与当前5源一致，workflow使用本真实schema与number，不残留“双public”等拼写来源。

已做范围仅原文本、准确字节、JSON字段与完整diff；没有本地编译、AST、科学import、数值对拍、微基准或新增fixture。公开Actions沿原流程完成实际编译与科学。各新文件小于100KB；blob只保源码／参数／接口，root唯一发布refs并调度。

R423只论三处C++名字解析，不把reader编号修复当数学证明。R403、R406是已有实际范围，不用它们预付199。实际R424必须据本请求真实source/run、完整必要正文、实际backend、各组件已付／未付和cleanup成文；本接口未宣布目标完成。
