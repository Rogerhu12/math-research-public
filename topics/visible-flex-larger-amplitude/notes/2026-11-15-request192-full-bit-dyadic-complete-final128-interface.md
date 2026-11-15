# Request192：完整 dyadic 点积与一次 RN113 的 recorded-operator 全链接口

作者：OpenAI / ChatGPT，2026-11-15。

## 1. 请求作用与独立身份

本请求直接执行完整当前128位链：真实原91输入恢复 → fresh64完整J/R273 → 持久128 owner与独立 replay → 全576阶段×224状态方向 → 原112边界 → 原混合338×112端点 → 独立原audit。它是独立的新运行，不读取已删除的160状态，也不使用正在执行的186/190结果作为父状态。

数学依据分别为 [R402](../results/R402-recorded-literal-block-operator-equivalence-and-rounding-scope.md) 的记录系数/名义因子准确实算子，以及 [R405](../results/R405-complete-dyadic-digits-and-once-rounded-binary128-dot-products.md) 的完整位点积。R405证明和内核已公开于2008c440cdbea749a507f7bfc11b018d33ce5d55；192只消费该内核最终18871B/5c2a0cb1字节。

192的关键变更是实际形成的有限矩阵输入：保留每一个binary128字词的符号、全部significand位及完整指数，点积准确归约后只作一次RN113；全224列按场批量执行以复用解包与packing。原primal/root/名义因子现场保留。小系数形成仍是binary128；完整算子准确导数或误差外包仍未付，R405不替它支付。

本文没有未来run、速度或接受结论。所有科学计算和编译仅由本公开仓库Actions执行。没有独立fixture、局部benchmark、额外rank/精度接受门，也没有预先宣称8000秒能够完成576阶段。

## 2. 最终文件与来源闭包

以下SHA均指最终完整UTF-8源码/配置原字节。除workflow位于仓库根.github/workflows，运行源码和request位于本题computations。kernel是已经发布的R405原件，其余六运行源、request、workflow和本接口是192独立发布件。

|角色|文件|bytes|SHA256|
|---|---|---:|---|
|kernel|geometry_20261115_native_exact_digit128.hpp|18871|5c2a0cb17c5fedfa5fe98b193d586b2e82171de20ddc61bcbfdf04ec556329fc|
|header|geometry_20261115_native_exact_digit_operator_trace128.hpp|28018|c80e4288f39ffc32fd569a7810d95ffa01fa14671fc2b1bc6acdb0d890698809|
|stage|geometry_20261115_native_exact_digit_operator_stage128.cpp|12664|a9f13b780ee41d2233a238ac3e833afe7228a69f254040576c91bdcb2a3e236c|
|launcher|geometry_20261115_native_exact_digit_operator_final128.py|28767|b6fc7a0e2053b51baf5c47273614f57858238a377289215accc53a50bba6311f|
|helper|geometry_20261115_native_exact_digit_operator_final128_same_job.py|38353|a1bd516f9c7af35ce4e04154edc31e70363cd066cb7188df15edc359b02b26b4|
|bridge|geometry_20261115_native_exact_digit_operator_final128_bridge.mjs|15783|8a42c96fb50c9fbfecc881ba10ad7e067c36deb28e69184873b63517719874a6|
|reader|root_20261115_native_exact_digit128_necessary.py|36795|cb01ec862ad0ae0164ba73c9b25c21cb5a1657f9ea64fafbcbb104aa99862c9e|
|request|public-native-exact-digit-final128-request.json|54752|a04aa73c1ae4a1f73af77203233295914937f421c45295f9bbac8908e17352cd|
|workflow|visible-larger-public-native-exact-digit-final128.yml|29498|6c56f6f4d36faacc214b6706e891fb454399b62ecc475fadc3f75febf7498def|

本请求源表为原190完整70 pins原值保留，再加七个实际新运行源，共77。保留旧文件作来源约束不等于执行旧入口：

- 新stage实际include新算子header；新header同时includeR405内核及原190 header。
- 原190 header提供原容器、元数据SHA、原标量helper等，并继续include原186 hoisted header。
- 原186 header继续实际提供D6现场记录、完整primal、名义因子回代和原reference接口。
- 原950e operator header由原v2 qualifier在同一个临时编译目录生成4610派生副本；完整非空geometry参数batch仍走这个原R305 fallback。
- 原190 stage/launcher/helper/bridge/reader只作为冻结来源，不能误作本次执行件。旧70所有pins未改。
- 原R283数值prefix、shared trace、boundary与physical来源按原v2 qualifier消费；不加入strict single-field证书三源，也不以single-field代替576×224。

编译时精确复制新header、R405 kernel、原190 header、原186 header和新stage，逐字SHA核对；随后绑定原qualified fallback与完整原prefix。只有实际translation-unit路径改为这个临时副本，原g++ flags不变。引入的依赖仅为已经使用的GCC unsigned128和标准C++容器，无Boost/BLAS。

## 3. 真实原输入与首个当前现场

参数与数学输入完整沿原190：

|来源|真实身份|
|---|---|
|原91 run/source|43672150224 / b78f0dd1471a118d2ed21467602509d188c2ab67|
|原artifact|14145200674，10267458B，SHA78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6|
|原result SHA|0b7200064336361ecb36b0627495fca298b7af758ed37d34d6ae6b1a1898db04|
|原binding SHA|0119e12bfc7f98732189b76b3fdfa23ae05229937a8ea998c9aa38890ff11d0a|
|真实BASE state SHA|f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6|
|状态范围|原73失败BASE，native call1 / nonlinear iteration2 / snapshot2；不是已接受尾|
|原两ready恢复commit|8bd267107cc8710d371f3b62c02986655ac965b0|
|ledger ready|109004B / 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6|
|stored ready|29774B / c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d|
|原78源|由原pinned public_resume恢复；按manifest实际原bytes/SHA逐件绑定|

两ready仍只是constructor geometry输入。原失败BASE只是本次初猜。全当前H、target、far、sigma、所有cells、原577节点和129248行均由原现场重生，不能从旧输出SHA“恢复”一个不存在的current-state文件。

第一次fresh64 J/R273保原η=1、全惩罚与原完整因子。进入128后仍只有current residual投影成64给固定chord QR，实际state持久保128，方向用原sigma和z的准确lift在128中恢复。原32方向、每次10档、2e−9尺度范数停止与独立fresh replay保持。

本请求没有把新stage矩阵加入原128非线性接受条件。全stage、boundary、endpoint、audit是后续实际必须付的责任；各组件完整不能自行授予native/fullDN终结论。

## 4. 独立数值数据流与精度边界

### 4.1 全位输入和两条相同合同的归约路径

R405内核解包实际finite binary128字词，逐字保全部113-bit significand和原指数。仅删除significand中实际为零的尾位并补偿指数。每行/每列按真实最低占用位、最高占用位确定其20-bit层数。六层只在公共跨度≤120位时成立，不能对所有输入硬套六层。

fast path最多12层；每个digit-pair局部区间至多2048项，乘法前两个int32分别提升为int64，部分绝对和严格小于2^51。全不同指数结果加入正/负宽整数，而不是先折回浮点。跨度太宽或显式packing预算不足时，完整113×113→226位乘积逐项宽累加；两路都在准确相减后执行同一个一次RN113。

subnormal直接按2^-16494量子舍入，不先113位再二次舍入。准确总和为零明确取+0；负非零量下溢为零保−0。输入非有限直接报错；溢出输出Inf再由原finite责任失败，不clamp。宽路径不删任何指数尾部、不用近似零替代未做部分。真实allocation/deadline异常按原资源范围报告。

这只证明传入内核的有限字词点积。它不证明产生那些字词的小系数、root矩阵或整个RHS是准确导数。

### 4.2 显式装配H_s与完整literal G

为避免190仍在每个angular node执行完整J² Gram-action，192先形成R402的H_s系数图，再对完整literal G转置作一次准确点积矩阵乘法。所用s是实际update.solve.out，所有2M+1 Gram列都保留。

这里有一个额外且显式的新有限图：H_s中的sqrt2*s以及少量重复系数相加仍先在binary128形成；它们与190逐角乘积的结合顺序不同。因此：

- 准确实展开仍按R402记录系数表达式。
- 实际H_s系数形成误差没有因为下游dot准确而消失。
- 不声称H_s或完整dL与190、186、R305原字相同。
- sine、cosine、gram仍是各自独立保存的binary64-lift literal表，绝不调用理想三角积化和差、FFT或Toeplitz替换。

原small momentum/target D函数原文复用。原完整226 RHS与RK每个标量公式保留；方向loop重新组织成全列batch，不能声称整个旧RK函数文本逐字相同。

### 4.3 只读basis与全部224列

一次实际stage executable建立不可变LiteralBases：

- 完整Gram转置；
- 上下拼接的sin与实际binary128 frequency*cos basis；
- 均值列明确为1的L basis，其余为原cos字词；
- 按原表达式形成的sin*invN转置。

这些表的原形状、完整binary128内容SHA写入本次临时literal-bases-identity.json。全部stage线程只读共享其解包/packing缓存，不按可变指针地址猜缓存身份。计时、矩阵SHA及packing计数仍计入同一个8000秒stage预算。

每个实际field中先消费完整原root轨迹，形成所有真实root maps和final flux maps，然后对全部224列批量作用。各列之间只有读共享常量，没有数学耦合。root更新仍按同一个实际k序列进行；每列各自de、原alpha和右端均完整保存。

### 4.4 名义因子及原C残差

每个实际右端仍调用原hoisted factor_direction_solve，原forward/backward三角回代循环不改。准确实名义作用对象仍是记录的Lhat Lhatᵀ逆，不能写成未经证明的C逆。

每次实际更新、每个方向、每个完整C行，仍用原顺序形成C*ds−right、检查finite并记录最大残差和完整行计数。root-right形成、de更新、完整RHS、RK、post-port输出均保原finite责任。新dot内核不代替这些检查，也不把这组读数提升成区间外包。

非空geometry parameter batch原样转交完整原R305接口，包含原h/geometry/μ方向；本stage请求仍是零geometry参数的全部224状态列，不能静默清零一般方向。

## 5. 四个实际组件与退出边界

顺序与原190相同：

1. stages：当前完整128节点状态，全部576×224，同原原子RK细分；只有某stage所有原子步和所有请求列真实返回后才落它的完整payload。
2. boundary：仅在本次stage完整输入实际存在、schema/source/shape/manifest匹配后启动原112右端和boundary QR。
3. endpoint：仅在实际boundary完成后，消费真实当前state、stage与boundary，形成原混合338×112责任。
4. audit：独立预留预算，仍从真实当前128节点逐stage重放原physical/metric程序；stage或boundary未完成不冒其成功，也不因此抹去独立audit责任。

批量field执行中断时，completed_column_steps只有完整RK列真正完成才增长；full_rhs_columns及各kernel计数是实际已做的更小工作。step_count直到该原子RK整体返回才增长。接口不凭这些局部计数推断未形成的完整J或阶段。

原stage source返回码、组件wrapper返回码、元数据协议70与原controlled64停止分别保存，不能因job failure反推数学拒绝，或因必要readback成功称全科学成功。

## 6. 资源保持原值

|职责|预算|
|---|---:|
|全调用绝对monotonic预算|19200秒|
|最终读回/清理预留|120秒|
|128 owner上限|6000秒|
|owner独立replay预留|1200秒|
|完整stages|8000秒|
|boundary|600秒|
|endpoint|600秒|
|独立audit|1800秒|
|各组件allocation overhead|345 / 720 / 345 / 345秒|
|stage线程|4|
|科学step/job|330 / 350分钟|
|原规则真实pull间隔|2700秒|

全fresh64恢复、真实J/R273、packet和physical导出、实际编译、缓存形成均收费到同一个绝对deadline。不存在只放宽外层job却漏旧child timeout的变更。所有guard、进程组、原uid/pid-starttime和grace规则沿原190。资源未完不冒数学反证。

192没有改变原32×10/η1/2e−9门，原exact_workers2、node_heap6144MiB和max_factor_bytes2147483648也未改。没有减少576、224、129248或原audit细分。没有新独立benchmark或性能估计通过门。

## 7. 同job元数据与一次必要读回

新的主要schema为：

|实际对象|schema|
|---|---|
|request|public-native-persistent128-exact-digit-final-components-request-v1|
|same-job helper|native-persistent128-exact-digit-same-job-final-components-procedure-v1|
|component launcher|native-persistent128-exact-digit-contracted-trace-final-components-launch-v1|
|stage|native-persistent128-complete-dyadic-recorded-stage-maps-v1|
|必要summary|native-exact-digit128-complete-chain-necessary-readback-v1|

内部资源计划/lifecycle的独立exact_digit schema由同一helper与bridge逐字对接；它不是旧190字段的重标签。当前源SHA、真实run/source环境和所有原输入/输出file receipts仍绑定本次执行。

同job临时目录使用native-exact_digit-final128-owned-work；close receipt为native192-child-close.json。完整原stdout/stderr、root traces、矩阵、column payload、owner journal及四组件summary只保本次Actions临时文件。

always必要reader仅做stdlib JSON/字节/SHA选择，不打开科学array进行新计算。它保原owner所有实际trial/evaluation与实际key-set，只有完整字面相等的evaluation才共享；保全部请求stage的真实地址和原失败/未完字段，只有非地址字段完整相等才共享一个正文。成功大列、矩阵、因子等只给原identity/count和已读取范围。

192新增完整聚合digit计数：真实span/limb最大值、fast/wide调用、integer partial数量、原nonfinite失败、rounded-zero/subnormal/overflow、宽整数长度等。它们是实际运行结果，不作为接受门。完整原C残差、原component flags、所有真实异常与未启动下游仍属于必要范围。

公开只输出一份ASCII JSON，硬上限90000 bytes，标记为BEGIN_VISIBLE192_NECESSARY_SUMMARY / END_VISIBLE192_NECESSARY_SUMMARY。没有将完整大树、科学stdout或矩阵编码/拆分后搬运。若实际必要选择超限，诚实transport_complete=false并返回协议70，不能声称complete，也不靠删科学试探通过读回。

工程错误原文按原reader的必要行选择规则返回，同时保完整原file bytes/SHA及明确未返回范围。编译错误不能只有SHA却丢失所有可解释原文；但科学大stdout不伪装成诊断分包。

## 8. 清理责任

原owner/probe的临时metadata视图与插入点沿190，只换实际helper/bridge/component身份。数值owner的原每次trial/QR消费规则保留；最终组件现场直到必要reader执行后才允许清理。

清理需要：

- 实际fresh child已wait/reap且close收据成立；
- 本次必要summary真实完成、transport完整；
- 观察到request-owned目录内没有仍活跃的owned进程；
- workflow再次核同目录/uid/containment与对应原收据。

science失败但必要scope完整且owner已静止，可以清本次可再生临时文件；必要scope不完整、读回超限或quiet未付则明确skip。runner最终销毁不等于可恢复现场。没有上传新artifact、Release或Git raw，没有把输出换名当后继accepted原件。

actual91旧只读树的权限恢复仍只限本request真实同uid owned目录，不跟随符号链接、不操作其他目录。新入口不执行任何外部消息或分支变更。

## 9. 文件差异与静态完成范围

同目录八个完整diff逐一对应190基线：header、stage、launcher、helper、bridge、reader、request、workflow。新kernel直接消费已发布R405最终原件；没有另造有相同名字的不同本地数学源。

源码/JSON字节比对已经确认：

- 原70个source SHA完全保留；七个新值与真实完整源码hash一致，共77。
- 原91输入tuple、两历史ready、原compiler配置和完整wall_clock_envelope对象逐项不变。
- helper中的component schema与新launcher完全相同，bridge/schema/动态owner SHA合同对齐。
- compiler临时include树明确含新kernel与原190/186 header，并保qualified原fallback/prefix。
- 新科学编译仍只在真实Actions完整流程发生。

这里没有本地科学导入/执行、C++编译、语法fixture或独立数值测试完成的声明。既有Actions的源字节/AST/bash前置仍按原workflow存在；没有另加“先证明快/先通过额外精度”之类新门。

## 10. 性能与研究结论的责任

整数归约准确不等于快。六层×六层仍有36个digit-pair dot；更宽行列可需要更多层或完整宽回退。共享packing能摊销解包，矩阵预装配和列batch能减少重复现场工作，但真实缓存、CPU向量化、factor/C残差及root/primal成本必须实付。

原160在8000秒只完成20/576阶段是已发表实际动机；不能据此声称新实现必达某倍吞吐，也不能从186/190仍在运行推出其结果。192必须以真实全链退出、所有实际范围和原最终门评价。每dot的正确舍入、记录算子准确实代数、有限root导数误差、native/fullDN接受与连续模型证明是不同责任，本文不相互替代。

本接口只交可直接公开运行的独立源码与具体接线；R406留给未来actual192实际结果，不预写成功或失败。
