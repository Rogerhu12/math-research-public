# Request196：完整 current128 链中的 R414 SIMD digit 入口

作者：OpenAI / ChatGPT，2026-11-15。

## 1. 本次执行对象

本请求独立从原 actual91 保存的真实 failed73 BASE 初猜重生：恢复原 78 份公开源和两个历史 geometry ready 输入，重新付原 binary64 withJ 与完整 R273，再进入原持久 binary128 owner。只有真实当前 owner 末态存在，才在它尚未清理的同 job 中依次运行完整 stage、boundary、endpoint 与独立 audit。

唯一数值实现变化是把 request192 的 R405 packed digit partial 接到已刊 [R414](../results/R414-complete-signed-digit-SIMD-and-RN113-equivalence.md)。R414 对同有限输入准确整数点积提供 AVX2 even/odd 完整处理与 scalar fallback，所有跨指数 bit、wide integer、原 packing 规则和唯一 RN113 仍使用原 R405。R402 的小系数形成、名义因子两代回、实际完整 C 方向残差及原 RK 公式没有改。

本请求不是旧186/190/192结果续接，没有其末态或已清理列的输入；旧失败也不作 accepted anchor。没有预填新run、新CPU后端、提速倍率、完整stage完成或任何科学接受。没有孤立 benchmark、fixture、列子集或新的非零/误差阈值门。

## 2. 最终文件与身份

本次新增发布九件；下表 SHA256 均为完整 UTF-8 原文，文件带其实际末 LF。所有路径除 workflow 外均在 topics/visible-flex-larger-amplitude 下。

| 角色 / 路径 | bytes | SHA256 |
|---|---:|---|
| computations/geometry_20261115_native_simd_digit_operator_trace128.hpp | 29035 | b183eeecf4f3009bf202dd0f465c8d4fdb17d8cc0ce14bb90d1ed5e6ecf485ac |
| computations/geometry_20261115_native_simd_digit_operator_stage128.cpp | 12670 | b6537c6ce86754a6a2a75eb928e543a7083fa2311eb70a4764066f2a70dda91a |
| computations/geometry_20261115_native_simd_digit_operator_final128.py | 29167 | 9a860d42f47881d23bd8a19042aa6614f596363c7a4ac39ffd4e301907fecbab |
| computations/geometry_20261115_native_simd_digit_operator_final128_same_job.py | 38340 | a3a879a1a57a36f278941dd06a513a46d66a2b7ef61b30d0730b30cc99c537f7 |
| computations/geometry_20261115_native_simd_digit_operator_final128_bridge.mjs | 15787 | cb6ae99b241f2f2d3e5640364287378dc61ff174432a75deb5fa9edc840e2344 |
| computations/root_20261115_native_simd_digit128_necessary.py | 37020 | a1106a6a3f6530d149ee21a38e90a6b271f55ee3738b4548bac3017b4c8995dd |
| computations/public-native-simd-digit-final128-request.json | 61089 | cf914ce6affdeb5fa457113c9e28e62868398bd002577bfa3f6bb992c140c080 |
| .github/workflows/visible-larger-public-native-simd-digit-final128.yml | 29968 | fd48ee6c5524d83ac2dd5af35dc706a655bb795690e5a00808a3513b9559bfe8 |

第九件是本接口。与请求192逐文件完整差异同时交付；它们是源码差异，不是科学输出或本地数值检验。

### 2.1 已刊 R414 与原 R405

R414 kernel 已独立发表于 b811cfce956d254834a1df852fe4dab930243e7b：

- geometry_20261115_native_simd_exact_digit128.hpp：9006 B / 1695b945c706523036ab85d46e1db89494719ff1b5a86efe469c39d696a556e6。
- R414 proof：15800 B / 9b5bd117b0a44a618ff15ebf77dbb4dda9271d66cf4ed03276021eba86085d95。
- R414 源接口的公开版是 8166 B / 3840dcdf2063e8fb39bb6b237b88b3d405fb34cf42bfd5fdb931088ab2b7a32f；本请求不执行或 pin 这份说明文档。

原 geometry_20261115_native_exact_digit128.hpp 18871 B / 5c2a0cb17c5fedfa5fe98b193d586b2e82171de20ddc61bcbfdf04ec556329fc 继续作为实际 include。新 SIMD 头文件直接包含它；本请求同时复制二者到同一受管临时编译目录。

### 2.2 77 原 pin 与新增 7 源的关系

基线是公开 request192，source 6f6ae85b05d4c717bc2b80601c6e5d603dc9a0a2。其 request 54752 B / a04aa73c1ae4a1f73af77203233295914937f421c45295f9bbac8908e17352cd；workflow 29498 B / 6c56f6f4d36faacc214b6706e891fb454399b62ecc475fadc3f75febf7498def。

request196.source_sha256 完整保留那 77 个 basename/SHA 对，未替换任何旧值，再加：

1. 已刊 R414 kernel；
2. 新 trace header；
3. 新 stage executable source；
4. 新 component launcher；
5. 新 same-job helper；
6. 新 Node bridge；
7. 新必要 reader。

故前置 source 表为 84。新 kernel 虽已单独刊出，仍属于相对192新加入的第七个来源；不是第十个需要再次改写的发布文件。

84 是本请求的完整显式前置表，并不等于 84 个源都作为同一种运行代码执行。原192六个 entry/header/stage/reader 角色保留为不变历史源；不加载其科学结果或执行其旧入口。原 R405 kernel 是实际调用；原190 header、186共享 primal header、qualified R305 fallback、R283 prefix、原 owner/probe/packet 和原四组件相关源仍按实际依赖使用。组件临时 source_receipts 沿原 OWN_PINS 与原组件 base.PINS 的并集记录真实来源，不伪称历史源码标签就是新可执行。

原 78 public source restoration 与原两个历史 ready 数据输入是另一个已有来源合同；不是把它们虚算进上述84。其原 bytes/SHA/blob/环境槽与 request192 一致，只采用本请求独立临时目录。

## 3. 唯一触发、schema 与当前对象

新 workflow 只在 main 的新 computations/public-native-simd-digit-final128-request.json 变化时由 push 触发。job key 为 nativesimddigitfinal128，独立 concurrency group，cancel-in-progress=false。没有 dispatch、PR或未来run号写入配方。

| 对象 | 独立 schema |
|---|---|
| request | public-native-persistent128-simd-digit-final-components-request-v1 |
| same-job helper | native-persistent128-simd-digit-same-job-final-components-procedure-v1 |
| component launcher | native-persistent128-simd-digit-contracted-trace-final-components-launch-v1 |
| stage report | native-persistent128-complete-simd-dyadic-recorded-stage-maps-v1 |
| 必要摘要 | native-simd-digit128-complete-chain-necessary-readback-v1 |
| 临时编译绑定 | native128-simd_digit-operator-compiler-input-v1 |

request 的 exact_digit_implementation 结构键保留，表示仍然执行完整 R405 exact-digit 政策；其实际 entry/header/stage/reader、各schema已明确为新196，新增 SIMD_kernel 与 complete_signed_partial_implementation，不混用旧source标签。

## 4. 完整同 job 链路

### 4.1 输入与 fresh64 入口

输入仍是 actual91 原官方 artifact：run43672150224、artifact14145200674、10267458 B、SHA256 78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6、source b78f0dd1471a118d2ed21467602509d188c2ab67。原选中 state SHA为 f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6。它是原 failed73 BASE，不是83 rejected trial或已接受锚。

旧完整 artifact 只在 Actions 暂时取入并核原身份，不新上传。原 fetch helper、78源恢复、两个ready历史blob恢复、原config/geometry/target/H/全部577 sigma/far/full576 stage责任保持；后者不会由“相同文件名”替代其原字节证明。源码只恢复已公开准确历史输入，不将可重算数据重新写 main。

Node bridge 从真实 fresh64 当前配置导出完整 trace packet 和原物理 geometry/table packet。原 fresh withJ 与 R273 在 packet之前实际执行，所有129248行、完整577 penalty/常数仍参与。此处原64 J继续是持久128迭代的明确近似 chord，不能冒本请求新stage J。

### 4.2 持久 binary128 owner

原 owner 源及 CPP unchanged。中间真实接受态以128字词保留；只有其明确的当前残差投影进入原64 R273方向解，恢复方向后仍在128中试原十档。原最大32方向、每方向10档、原严格 sigma-scaled norm 与 tol2e-9保持。这里不是重写原 Newton 或改变接受阈值。

same-job helper 仍以原可逆源码视图在 owner 清理前插入四组件，并把大原记录留在当前临时 journal/fullsummary；原数学 body、原probe全部反向替换责任保留。helper实际source SHA经env明确交给Node bridge，避免伪造历史owner schema，也避免source SHA循环。没有读取旧运行剩余state文件或仅凭SHA再生某个接受态。

### 4.3 全部 stage 与方向

真实 current128末态和同job packet存在后，新组件实际读取末态的128字词。每个stage从其真实输入node n+1和全部224个标准方向开始，使用原实际cell原子子步列表；不以576×12猜网格。全部226态含两mean保持，端口ratio方向与原cut/far完整行仍付。

新 trace header 保留 request192 完整 R402/R405矩阵形成、完整literal sine/cosine/Gram布局、实际已选root更新及实际Cholesky因子记录。只将以下调用接到R414 namespace：

- 原 PackedVector、prepare与packing常数的兼容入口；
- 整个 DenseMap::apply_batch；
- 全部 RightCache::left_multiply 的每个准确点积；
- 对应完整Stats及join。

没有新增系数近似、列截断、只选某些mode或跳过Gram项。原 H_s小矩阵形成、全3输入小权重、actual Lhat两次代回、每个完整 $C\,d s-\mathrm{right}$、所有实际finite检查和RK标量算式保持192程序；仅错误标签/schema等身份文字独立。

stage范围仍 first_stage=0、stages=576、first_column=0、columns=224。原 optional reference-columns 为none，不新增对拍作为前门。成功stage只有完整原子步和全部请求列完成才写完整stage payload；任何资源/数学异常留真实partial/error。源层保证不缩范围，不预言所有范围能在实际墙钟内完成。

### 4.4 boundary、endpoint与独立audit

原 boundary全112、endpoint混合定义338×112、独立全几何audit仍由原数学源+原v2 JSON资格修复执行。新wrapper明确识别新stage来源并绑定相同current128 state SHA/bytes；没有把新stage报告重标为旧R302 source。

缺少实际完整stage时boundary不启动；缺少实际boundary时endpoint不启动，并保原理由。独立audit仍有原保留预算和独立原stage/RK检查，不因stage缺项自动删掉。原完整末态只按同job真实对象传递。

即使有限四组件均complete，也不自动构成native/fullDN接受。原endpoint first112/meanSlope与其余second/meanSecond的来源区别、原C-based物理径向程序并非有限root径向导数的区别保持，不因R414准确整数归约变成完整连续精度证书。

## 5. 实际编译、CPU选择与统计

新component launcher在原临时目录逐字复制六件：

1. 新 SIMD trace header；
2. 原 R405 exact digit header；
3. 新 R414 SIMD digit header；
4. 原190 recorded-operator header；
5. 原186 hoisted primal/fallback header；
6. 新 stage CPP。

原 qualified v2 helper继续真实生成同目录中的原 R305 fallback视图，并保原R283 generated prefix SHA。原引号资格化只处理其已声明词法工程范围；新源不冒旧源码哈希。实际命令仅改为所复制的stage translation-unit路径，原所有compiler flags及link选项保留。

原编译为g++、gnu++17、O3、OpenMP、frounding-math、ffp-contract=off、fno-fast-math、quadmath。没有全局 -mavx2、-march=native 或额外BLAS依赖。AVX2只在R414函数级target内；运行时依据实际CPU支持选择，unsupported执行完整scalar。新ISA选择不改变数学分支或任何接受门。

实际stage.aggregate statistics.exact_digit_statistics保原R405所有字段并新增：

- runtime_selected_digit_backend、avx2_body_compiled；
- scalar_digit_blocks、avx2_digit_blocks；
- avx2_complete_octets、avx2_even_products、avx2_odd_products；
- scalar_backend_products、avx2_scalar_tail_products；
- delegated_zero_calls、delegated_wide_calls、largest_digit_block；
- R414同输入完成dot条件范围、未声称整stage逐词对拍和非科学门的scope字段。

actual backend与专用body被编译是不同信息；若未完成任何packed block，其计数诚实为零，不能据选择名字冒实际执行了相关科学项。新源码仍按原per-stage统计所有权和末尾join，不并发写同一Stats。

R414证明只保障符合合同且完成的原字词dot正确性；它不证明宽fallback、packing、两回代或完整链都能获得某个倍数提升。也不保证不同程序在相同墙钟触发时具有相同已完成后缀。真正吞吐和失败范围只从实际输出读取。

## 6. 原科学与墙钟预算

| 项目 | 本请求原值 |
|---|---:|
| 原native最大方向 / 每方向trial | 32 / 10 |
| eta / solve tolerance | 1 / 2e-9 |
| 完整原残差行数 | 129248 |
| 原shape / complete态维数 | 224 / 226 |
| stage / input nodes | 576 / 577 |
| native factor workers / max factor bytes | 2 / 2147483648 |
| owner线程 | 4 |
| 全科学绝对预算（含fresh64/QR/编译） | 19200 s |
| 末必要读回与清理保留 | 120 s |
| owner请求上限 | 6000 s |
| owner内部独立replay保留 | 1200 s |
| stages / boundary / endpoint / audit科学上限 | 8000 / 600 / 600 / 1800 s |
| 四组件额外allocation | 345 / 720 / 345 / 345 s |
| 组件内部清理读回 / process grace | 30 / 15 s |
| science step / wholejob | 330 / 350 min |
| 原规则同步周期 | 2700 s |

component额外allocation是上限，不承诺在其中编译或科学完成。原父绝对deadline、audit保留、fresh64/prebridge计费、owner动态截短都继续按原函数执行，没有把上表各上限当可相加后重置的预算。进程树超时仍由原受管pid/starttime/组生命周期处理；资源结束与数学拒绝分开。

全科学期间只允许真实Actions运行；本交付仅源文本、JSON、字节/hash和完整差异读取。没有执行本地AST、C++编译、科学import、数值计算、基准或fixture。workflow本来已有的Python/Node源码语法阶段保留，真实可执行编译仍由实际组件负责。

## 7. 单份必要摘要与实际失败责任

新reader沿已付182/186/190/192语义：

- 完整读取当前实际owner/fourcomponent临时JSON、原journal和stderr文件；
- 原owner所有真实trial与必要evaluation字段保留；只有整个原字典逐值相同时才共享正文；
- 原key-set索引区别字段缺失与显式null；
- 全部stage accounting保显式原地址、原总子步、已付步和未付后缀、原error；只把完全相同的非地址字段合并；
- boundary/endpoint/audit原flags、最大残差与当前实际源/输入身份按原necessary scope返回；
- 成功stage/列大表、矩阵和raw数组只保原身份、计数、覆盖和明确未逐值返回范围；
- 编译/子进程原错误文件被实际读入，必要原错误行及完整字节身份按原选择规则返回，不从缺日志推原因；
- 新runtime/backend整数统计作为aggregate小对象完整保留，未从预期维数重算或补值。

没有解码传输大树，没有新分片report或artifact。单份ASCII必要payload仍硬限90000B，report job只核原字节数/SHA/schema后原样打印。若超限或缺必要字段，则显式protocol70、summary_complete=false，不能伪装成科学成功或用裁掉失败行来过限。

原科学child的70、component的科学退出、component本地transport70以及最终必要reader70分别保留；不得凭一个总failure标签把资源/工程错误当数学反证。无摘要则report打印真实missing及范围，不补未来成功。

唯一公开边界标记：

BEGIN_VISIBLE196_NECESSARY_SUMMARY

END_VISIBLE196_NECESSARY_SUMMARY

GITHUB_OUTPUT仍为scalar_summary、scalar_summary_sha256、scalar_summary_bytes。payload不含打印额外LF；实际文件/运输SHA按原reader规则分别记录。

## 8. 静止后清理与规则同步

新必要reader在原科学child结束后运行。主动删除条件仍同时包括：

1. 实际necessary summary/transport完整；
2. 实际close record确认child_reaped；
3. reader观察owned quiet并给cleanup_allowed；
4. workflow再次检查本请求独立临时目录对应的存活进程。

未付条件就明确skip主动删除，保当前runner现场直到平台销毁，不上传或改成持久数据。旧readonly actual91输入目录只在本job属主、真实目录及contained路径成立时恢复属主写/遍历权限后删，不修改其科学原bytes。

request196自己的根目录为 RUNNER_TEMP/visible-native-simd_digit-final196；内部owner work为 native-simd_digit-final128-owned-work，close为native196-child-close.json。公开原78临时源和actual91临时父目录也有196独立名字。原186/190/192/193不被此cleanup匹配。

原3b8规则runner未改；只用触发checkout实际已读的README全文更新其原baseline字典，保2700s真实pull/rebase/diff与遇新规则停整科学进程组。当前reviewed根/题blob分别21bd547f56590b7f2dd279d0297efb289a9b2783和bff8aea253a9e6a7a4fac28d810ac454c5499fec。科学checkout不由规则工作树更新替换。

原GITHUB_TOKEN仅恢复输入/规则调度必要步骤使用；科学bootstrap清除原声明的token环境键。没有把PAT放源码/参数，未增加网络数据归档。

## 9. 差异阅读顺序与完成边界

最小审阅路径是：

1. 已刊R414 kernel/条件证明；
2. trace完整diff：新include/namespace/API/Stats和实际小统计；
3. stage完整diff：同全576×224循环，仅新schema、namespace和identity；
4. launcher完整diff：双digit头复制/pin与新schema，原四组件函数/预算保；
5. helper/bridge完整diff：新身份、独立路径与原当前owner前清理衔接；
6. reader完整diff：新schema/路径/四scope字段，其余必要选择和90KB不变；
7. request/workflow完整diff：77旧pin不变+7新源、84一致、原科学预算与门逐项保。

源码中仍存在exact_digit_statistics等结构键，是同一准确digit数据的原结构，不是声明实际source仍为192。所有具备身份含义的producer/schema/source SHA、入口、编译源与实际run必须是本请求真实值。

本次静态字节工作已具备可直接发布的完整入口；未独立验证速度或产生新scientific outcome。正式结果号预留R415，必须等待真实完整运行，并按真实已付/未付范围成文。R414的低层正确性不替代该结果，也不将单个后端选择、stage完成或native当前norm误写成课题完成。
