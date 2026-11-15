# Request152：原140完整链路的显式 JSON 名称限定与清理前完整读回

作者：ChatGPT / amplitude，AI 协作源码实施。日期：2026-11-15。

## 1. 本次承担的实际工作

本请求重新执行完整的原140链路：暂时恢复真实actual91初猜及两份原历史几何输入，构造当前原64 worker，现场形成完整fresh64 J和R273方向，建立新的持久binary128 owner；随后在同一owner临时状态仍存在时，依次请求完整576×224的R305 stage响应、112边界响应、混合338×112端点读回，以及独立原物理程序audit。旧140的状态与因子已清理，不从其SHA恢复，不使用150单field替代完整链路。

唯一数值源码差异是已单独发表的共享shim在临时编译副本中把指定JSON helper调用由 `quoted(` 限定为 `::quoted(`。原数学函数、运算顺序、矩阵尺寸、root策略、32×10持久owner迭代、原容差和所有阶段的完整性条件保持。新的helper和bridge只承担当前身份、调用接线、错误原文及完整标量报告运输。

已知名称解析阻断来自固定源码：非const `std::string` 参数可使ADL选中 `std::quoted(string&)`，与原三目字符串分支不兼容。原140实录只付清编译进程return1，不含编译器错误正文。本接口不把源码诊断冒成原140已经打印的诊断，也不保证修正这一阻断后所有组件一定完成。

## 2. 固定来源与55件闭包

原140四份接线基线：

| 角色 | 原文件 | 原字节 | 原SHA256 |
|---|---|---:|---|
| 同job helper | geometry_20261115_native_operator_final128_same_job.py | 30043 | f0ca0d4300252a7db2cb95da4ea6991605b59cea2132fa2526faafb58e120141 |
| bridge | geometry_20261115_native_operator_final128_bridge.mjs | 16367 | 00f1a43b95295cb29bec930b06a6418e7b5245cfb06d122fd9c1314cfa68dfd1 |
| 请求 | public-native-operator-final128-request.json | 28483 | 1eb108e7834b4e3c8644dc346ae1965d376fb0c93cc662f63d28a2b9ec9f3d40 |
| workflow | visible-larger-public-native-operator-final128.yml | 24807 | bd511de4fc1e578641aa4a4e2d2a8e49d847b5ea595740f98c50b2054d56aca8 |

新请求逐值保留原52个source pins，另外加入两个新运行源和共享shim，总数55。原140 helper/bridge仍属于历史来源闭包，不再作为活动entry执行。原R305 launcher `geometry_20261115_native_operator_final128.py` 的a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef仍由共享shim显式载入并执行原main；完整数值consumer和binder的原身份仍保留。

共享shim为公开commit `62120ebe8dbdcd9d06693267d950add2bf494340` 的 `geometry_20261115_native128_qualified_json_components.py`，15058 B / SHA256 `e609fb0aeae3142fcdb779004ddc0966e86c87c437da0984f50ffa814fb40d36`。本请求仅使用 `--operator-components`；不会执行或要求strict-field-certificate分支的三份额外源码。

在本入口实际触及的临时编译副本中，共享shim严格核原源SHA、预先声明的替换次数、派生全文SHA、整篇逆变换，以及唯一被改的CPP命令参数；stage另复制其operator header。数值源的Git文件不被修改。

| 编译文件 | 替换次数 | 执行副本SHA256 |
|---|---:|---|
| geometry_20261115_native_operator_trace128.hpp | 12 | 046fafc0421ebf22a68437abab62594a525acbec815a660719f91a2c18cd0a0e |
| geometry_20261115_native_operator_stage128.cpp | 9 | ad61daf7f86f46bac20102764e65d4448f23a725a7db4917235ea789cf7075bd |
| geometry_20261115_native_boundary128.cpp | 4 | 994c0b8b52f1f5d7bc18db0fc5430d962bafcb6060bb61b276a50f8bddceb8ed |
| geometry_20261115_native_physical_final128.cpp | 49 | 05a4a97c41e0e53347b51fc6eb9936eba62a73e224e267e3c3e14c6e5b74014f |

同shim中列出的field exporter两处限定属于150使用范围，不由152执行。完整来源说明见已发表的共享shim接口。

## 3. 两个新运行源及实际身份

| 新活动文件 | 字节 | SHA256 |
|---|---:|---|
| geometry_20261115_native_operator_qualified_final128_same_job.py | 41293 | 7c6b02680f4159e4666bf5111438b9fcaaf043b4994cd258bad43a2ab397c4f6 |
| geometry_20261115_native_operator_qualified_final128_bridge.mjs | 17193 | 0ccbc8241740b830b3eed0ba2b0e257a21ce93922848c88ad5b500ac5e5e9258 |

顶层实际schema为 `native-persistent128-qualified-JSON-same-job-final-components-procedure-v1`。每个stage/boundary/endpoint/audit的launcher摘要必须来自 `native-persistent128-qualified-JSON-contracted-trace-components-launch-v1` 和共享shim的真实SHA。stage数值报告仍为原 `native-persistent128-shared-angular-contracted-trace-stage-maps-v1`，其数学实现未改。

桥接没有循环source hash：helper固定新bridge SHA；bridge从实际同job环境读取并核helper SHA。现场packet和所有原78来源、追加的原解析slope adapter，以及同一fresh snapshot的完整绑定仍按原140执行。共享shim验证后继prior时核新schema、同一实际entry及完整来源集合，旧摘要不能改标签后充当本次prior。

原owner的两处内存源码变换保持原文：在唯一清理anchor之前调用post-owner组件，原有限输出fallback额外保留post-owner字段。原probe的两处纯元数据反向变换也保持：明确原64最终责任未执行，以及桥返回的运输完整性进入原报告。没有移动hook到原状态清理之后，没有把binary128状态回写到原64 native worker。

## 4. 完整阶段与列读回

原helper的 `scientific_projection` 是有限索引，省去了完整 `stages` 和 `column_records`。新helper保留该原索引，另在每个实际组件进程返回后、任何owner清理之前读取完整 `summary.json`，逐字段无损输出：

- 每个object记录完整key集合，每个array记录长度；子项以字符串key/整数index的类型化JSON路径定位。
- 完整stage集合和column集合按原顺序保留，每行的所有字段均进入分段；不只保失败行，也不只保数量或hash。
- 其余小值直接保留；过大的object/list递归分段，过长字符串按明确字符区间完整分段。每个事件JSON最多90000字节；常规值使用72000字节软上限留足wrapper开销。
- 每一段有真实index、类型化路径、原值或容器声明、该段canonical字节数/SHA；整组有canonical全文字节数/SHA、段数与段metadata序列SHA。
- 对Python原canonical summary，重组后按相同sorted compact encoder可逐字恢复原文件。如果某实际JSON文件的原序列化不同，还额外输出其全部原始文本字节分段；不把重序列化摘要冒成原文件SHA。
- JSON不完整或解析失败时仍保其原字节和实际异常；此时 `parsed_fields_complete=false`，不制造空stage、零column或猜测未访问后缀。

主要事件为 `qualified_same_job_scalar_tree_part` 和 `qualified_same_job_scalar_tree_complete`；每组label形如 `stages-complete-component-summary`。这些事件沿既有 `NATIVE_PERSISTENT128 ` marker进入原fresh watcher，全部保留在compute原日志。

完整summary的原科学flags、实际returncode、resource_partial、各阶段未访问suffix、实际输入/输出身份和编译进程信息都在完整树中。原有限report只承担索引；它若仍超限，必须按原协议诚实报告transport incomplete，不据此补齐科学结果或改returncode。

## 5. 错误正文与日志生命周期

共享shim发出的每条原 `NATIVE_PERSISTENT128 ` stdout事件，在组件返回之后原字节转发到既有marker流，清理前完成；包括临时编译来源和实际编译错误读回。新helper还分段保留完整组件stdout、外层stderr及本组件临时目录内的全部stderr日志和compiler stdout。这样共享shim对单个超长原行的显式未转发记录，不会成为实际错误正文的唯一残留。

Node bridge和Python诊断均把原stderr改为有序12000原字节段。每段先形成可逆UTF-8/surrogateescape文本，再把文本序列化成ASCII内层JSON，置于text_json_ascii字段；外层frozen watcher只会看到ASCII字符串，不会接到lone surrogate。读回对该字段先json.loads，再encode('utf-8','surrogateescape')即可恢复原字节。Node遇到非UTF-8块时逐原高字节编码U+DC80至U+DCFF后再转内层JSON，同样严格还原。这仅编码原错误/诊断日志，不读取任何科学二进制矩阵。每段记录offset、原字节数、SHA；末receipt记录整文件原SHA、全部段数、已转发总字节及完整性。长错误不截断，不只留hash，也不把运输失败说成数学拒绝。

workflow的always诊断步骤在owned cleanup之前，再读取仍存在的stderr、compiler stdout以及四个明确组件stdout文件。它不遍历输出科学矩阵内容、不复制worker协议数组。正常路径已读回的诊断可以再次出现；路径和原SHA使重复范围明确。若进程被整个job强制杀死且always无法完成，不能声称日志或科学已完整；保实际已有事件，不从缺失尾记录推断成功。

目录所有权、same-process-group规则监控、PID/starttime受限终止、只删除本次可重生临时树的责任保持。实际原91只读输入树仍仅为同属主真实目录补u+rwx后删除；不改输入字节、不删共享源目录。

## 6. 不变的实际预算与依赖

| 层次 | 原值 |
|---|---:|
| 全科学单调时钟总预算，从fresh64 factory开始计 | 19200秒 |
| 清理/读回保留 | 120秒 |
| 持久128 owner请求预算 | 6000秒 |
| owner独立fresh replay保留 | 1200秒 |
| stage科学cap | 8000秒 |
| boundary科学cap | 600秒 |
| endpoint科学cap | 600秒 |
| 独立audit科学cap | 1800秒 |
| stage/boundary/endpoint/audit overhead | 345 / 720 / 345 / 345秒 |
| 线程 | 4 |
| science step / job | 330 / 350分钟 |
| 原规则runner真实pull周期 | 2700秒 |

原32方向、每方向十个alpha、eta CLI `1`、129248完整行、576stage、577node、226态、224shape、原solve tolerance $2\times10^{-9}$ 全保。原root30×20及原8e−14/fallback5e−12字面策略不变。既有预算分配和剩余时间裁剪公式逐字保持，不把打印日志当额外科学预算，也不增加模型评估。

boundary仍须实际完整stage输入，endpoint仍须实际完整boundary输入；audit独立保留预算。原组件returncode判据保持：即便原组件已经计算完而其compact运输返回70，也不把70改成0或静默允许依赖继续。完整读回现在能明确这两个范围。无预算足够/编译必过/全224完成的预言。

## 7. 输入与公开Actions接线

actual91为原失败73 BASE的真实输入，只作初猜，绝非accepted anchor：

- run43672150224，source b78f0dd1471a118d2ed21467602509d188c2ab67；
- artifact14145200674，10267458字节，ZIP SHA256 78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6；
- 原result SHA256 0b7200064336361ecb36b0627495fca298b7af758ed37d34d6ae6b1a1898db04；
- 原binding SHA256 0119e12bfc7f98732189b76b3fdfa23ae05229937a8ea998c9aa38890ff11d0a；
- 原selected state SHA256 f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6。

完整ZIP由原固定取件器在Actions临时取入并校验。两份几何ready按原历史commit `8bd267107cc8710d371f3b62c02986655ac965b0` 的准确Gitblob、size/SHA恢复至原环境槽；它们只提供constructor几何字面输入。完整78原源码照原public resume恢复。当前checkout科学源不因规则监控pull而替换。

唯一触发文件为 `topics/visible-flex-larger-amplitude/computations/public-native-operator-qualified-final128-request.json`；独立workflow `.github/workflows/visible-larger-public-native-operator-qualified-final128.yml`。Python3.12.14、Node24.22.1、numpy2.3.5、scipy1.17.0及原action commit全部保留。Git的merge.stat=false只减少规则同步diffstat，不改变规则检查；两README必须是已读21bd547f…/bff8aea2…，改变则按原runner停科学。

| 接线文件 | 字节 | SHA256 |
|---|---:|---|
| public-native-operator-qualified-final128-request.json | 34173 | 9b69f49733d53c23395871a9311e4d0eedea58a221f30cb9fe10de58cac51cd8 |
| visible-larger-public-native-operator-qualified-final128.yml | 28467 | 7cc94e0b66f432a54ae8626ae7a22da0282b39dfe6b33a551a5558ac8a36df7f |

报告job打印 `BEGIN_VISIBLE152_SCALAR_SUMMARY` / `END_VISIBLE152_SCALAR_SUMMARY` 内的原有限索引以及其原SHA。完整阶段/列/诊断分段保留在compute日志，不把它们重新拼入GITHUB_OUTPUT导致重复超限。若无索引则诚实标明missing；原未完成suffix只从实际记录读取。

## 8. 科学作用域与静态验证边界

这次没有改变R305数值微分实现，也没有付清其与原dL浮点图逐字等价。C不被当作F_e；名义factor残差导数不被假定为零；没有新增方向误差外包。混合338×112仍按原定义：first112及meanSlope来自有限root-trace RHS变分，second/meanSecond/height保原对称差分程序。独立物理audit仍是原C-based物理jet/metric程序，不是连续ODE证明或有限root径向精确导数证书。

即使本次全部组件成功，也不能据此重标原native/fullDN已接受。实际128 owner原shooting门、各组件实际完整性、旧64控制停止以及未付的完整科学责任分开报告。原数学门未因JSON修复或额外日志变更而放宽。

本地只做源码读写、原52与新增3个SHA核对、1个新Python AST、Node bridge语法、workflow的13个shell语法及9个inline Python AST、JSON/YAML解析。没有导入或运行科学模块，没有C++数值编译/fixture，没有本地模型、J、QR、FD或audit执行。实际编译错误、所有数值结果、资源partial和最终范围只由本仓库公开Actions原输出确定。

完整四份文本diff可从上列原140基线与新文件逐字再生，随交付置于独立/tmp目录供主控阅读；不写repo、不更新ref、不派发。正式脚本、参数、run及输出SHA按根规则留存，可重算raw不进入Git、Release或新artifact。
