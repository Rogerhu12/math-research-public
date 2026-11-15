# Request143：原连续 C 完整112深端图的公开执行接口

- 作者：AI（geometry）。
- 状态：独立请求与工作流已完成源码检查，尚未指定或预填实际运行结果。
- 科学依据：[R312](../results/R312-continuous-C-complete112-zero-tail-and-head-connection.md)，已发表commit c7b79fa81ebe13a3e8ead6a046b942471b3f8971，原证明26,907 B/SHA256 036289ed624b59456cfee700217f442d26104cae76bf33d9affd8ec618c9ac73。
- 源码细节：[完整112深端生产器接口](2026-11-15-continuous-C-complete112-deep-far-producer-interface.md)。本页负责真实输入恢复、独立调用、输出和临时数据生命周期，不重复完整证明。

## 1. 唯一科学请求

本次只计算声明C原准确根族在F=159处的完整112个线性深端图包围。固定物理频率为2,4,...,224；数学端口159对应physical node160，包含全部source cell n≥160。

生产器为geometry_20261115_stored_continuous_C_far_graph.py，16,333 B，SHA256 fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a。参数只有：

| 参数 | 实际请求值 |
|---|---:|
| far_port | 159 |
| precision_bits | 256 |

准确根选择仍未解析为某一具体序列。每个输出区间依据R312，统一包含原允许根族的每一种固定选择；mode2的准确零图来自原准确校准定义和半线唯一性。源码不运行有限RK校准、不用65/64替代原根、不读取旧zero-J或readylineargraph。

这次完整112深端包围的任务与完整cut DN不同。有限头传播、真实cut域、各mode在cut处的高度分母、非零native求解和全BVP仍未完成；这些字段在producer和readout中均明确保留。工作流不添加BVP接受门，也不把Actions成功当成这些后续责任已经通过。

## 2. 冻结运行文件

| 文件 | bytes | SHA256 |
|---|---:|---|
| public-original-continuous-C-far-graph-request.json | 9331 | c5e9931aaefe1b8d4cd8c45a77009b3e7975ed43c77dd319f13304f7855bb3b5 |
| visible-larger-public-continuous-C-far-graph.yml | 22674 | 93bcf11b4058b2fe04dd4bc7767fdce8193490faa830f7966849c213ab80e7b5 |

提交目标为本题computations/请求文件、仓库.github/workflows/工作流和本题notes/本完整接口。可重算static receipt及两份完整diff仅保留临时草稿，不提交Git。两份相对request139的完整diff身份如下：

- JSON diff：12,345 B，307433ac4a0f0f5e12820bc3126a3283f2f80a69e487ed8cd69aca388673d966；
- YAML diff：32,386 B，be2ce7bd7859ca8883f271991ece9023eaea400e1d0ba5402746af03c1fe716e。

原request139、原v1/v2/v3数学源和原两份证明均不改。此处从139复用的是实际来源和运行框架；不复用其积分结果、不声称139已完成，也不把139的工作预算悄悄变成另一项同名测试。

## 3. 三份真实原输入

三份输入逐dict沿用139，全部来自已知历史commit 8bd267107cc8710d371f3b62c02986655ac965b0。恢复只使用确切Git对象及原文件字节，不重序列化，不执行原native或calibration来“重新生成相似输入”。

| 输入 | bytes | SHA256 |
|---|---:|---|
| 原T112完整config | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| 原calibration ledger ready | 109004 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |
| 原stored reference ready | 29774 | c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d |

准确历史路径分别为：

1. topics/visible-flex-larger-amplitude/notes/public-actions-43588155190-1-prepare112/T112-config.json；
2. topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json；
3. topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json。

两个ready的原Git blob分别为4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3和b6c44fe237750f13c8b10366f15525b481a74e09。运行时只写到本请求owned临时original-inputs下的tail-config.json、ledger-ready.json和stored-ready.json。

如果历史commit尚未在本checkout中，按既有公开partial-fetch方案只补该commit，再按固定路径解析blob、取原bytes并核大小/SHA。不会将历史raw重新加入main、Release或artifact。运行HEAD始终保本次dispatch，不checkout历史branch。

三个原输入没有实际已接受场。config的有限mode设置也不等于本次已生成一个新的非零场。原冻结p、160行浅表、保存warp和完整源指纹由v3的metadata binder绑定；不将它们的存在误称为已经执行完整E积分。

## 4. 源码、证明和规则身份

现computations的11个pin是139的原10个pin加新far producer，全部原SHA不变。11项包括四个连续C Python文件、四个原runtime公式源，以及原public_resume、source-dependencies.json、rules_runner三项执行/来源工具。

公开原source恢复仍通过冻结exact_20261114_public_resume.py调用prepare_public_source一次。该工具SHA为11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5；source-dependencies.json为7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941。原外部五个公式文件仍由同一source-origin及九公式pin验证。

计数口径明确：

- 当前computations钉住11个文件；
- 原公式来源共9个，其中4个已经在上述11项中；
- 所以不同公式及执行来源文件合计16，其中13个是科学公式/生产器，3个是恢复/同步/来源metadata；
- 证明另计R286与R312两份，不混作源码数量。

新entry只借f12f7470版本的metadata binder和Arb工具。v3中所有积分函数都不会被调用；其9aa0、004010来源文件仍由原binder逐SHA绑定。R286 proof使用原37491 B/81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb。R312使用本页首部已发布原字节。

预检会用AST读取新entry的BINDER_NAME/BINDER_SHA256、PROOF_NAME/PROOF_SHA256、MODEL_SCHEMA和SCHEMA，与request逐项比较；再核v3的原PINS、REVISION和两旧producer身份。只有这项有限来源检查；没有fixture、额外科学审核或以数值斜率大小决定是否运行。

本次reviewed双README为：

- README.md：21bd547f56590b7f2dd279d0297efb289a9b2783；
- topics/visible-flex-larger-amplitude/README.md：bff8aea253a9e6a7a4fac28d810ac454c5499fec。

rules_runner仍原3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde；只在原包装层把实际已读当前README原文和blob传入其BASELINES，保原pull/rebase与规则变更停止语义，周期2700秒。日志明确记录原内嵌baseline与本次实际reviewed baseline，不冒旧记录已经是新规则。

## 5. 唯一workflow与调用顺序

工作流仅由main上的以下路径变化触发：

~~~text
topics/visible-flex-larger-amplitude/computations/public-original-continuous-C-far-graph-request.json
~~~

独立concurrency group为visible-larger-public-continuous-C-far-graph，cancel-in-progress=false；它不会覆盖或取消139、其他native或prefix请求。

运行顺序为：

1. sparse checkout当前源码、双README和R286/R312；
2. 建立$RUNNER_TEMP/visible-continuous-C-far143自有根；
3. Python3.12.14与python-flint==0.9.0；
4. 核全部本次源码/证明/规则/request身份；
5. 按固定历史对象恢复三原输入；
6. 原public_resume恢复原公式来源一次；
7. 原rules_runner包装新far entry；
8. always读实际result和完整行流，形成有界元数据；
9. always仅清本请求自有临时根；
10. 独立report job打印实际摘要及SHA，缺摘要则明确unavailable。

科学子进程CLI与生产器接口完全对应：三组文件+SHA、runtime-computations、source-topic、R286 proof、R312 tail-proof、far-port159、precision-bits256以及新的out。没有queries参数，没有积分预算参数，没有有限头求解参数。

job工程上限40分钟，science step15分钟，report5分钟。它们只限制资源；超时不构成几何反例。原rules周期2700秒不改。GH_TOKEN只给原规则同步父进程；启动数值子进程前清除GH_TOKEN、GITHUB_TOKEN和MR_TOKEN，不污染科学协议。

## 6. 完整读回而不归档原始行

生产器原result和stdout保真实来源/端口、完成mode列表、全部未访问mode后缀、原geometry包围、行流SHA、明确未付项。结果schema为R312-original-C-root-family-complete112-deep-far-enclosure-v1。

workflow的只读阶段执行原文件SHA/字节检查，不重新计算区间或谱。它完整遍历临时JSONL：

- 行数和频率必须等于实际completed_modes的有序前缀；
- 每行mode_index、frequency、端口、schema与request对应；
- 每行保原准确根族scope、原/物理Robin坐标顺序；
- 没有用65/64替换actual根，没有有限头/cut-DN冒名；
- 完整result、input-binding、行流的所有直接descriptor均逐bytes/SHA核；
- 未访问后缀必须逐频率完整保留；
- 新结果所绑定的三原输入SHA仍等于request。

这些是读回来源和输出范围，不是增加科学接受门。读者不作新矩阵乘法、不求根、不重算Gram或任何interval表达式。

完整112数值行不会分块塞进stdout，也不写GITHUB_OUTPUT。原行流只在job里临时存在。primary只保原result、完整频率/后缀、行流bytes/SHA、来源与未付范围，另附原rules_runner真实结束信息。它使用单份不超过90,000B的JSON传给GITHUB_OUTPUT。超限则明确报大小/SHA及工程失败，不静默截行、不改数学参数、不将未付部分标为完成。

日志边界为：

~~~text
BEGIN_REQUEST143_ACTUAL_CONTINUOUS_C_DEEP_FAR_SCALAR_SUMMARY
{one complete compact JSON}
END_REQUEST143_ACTUAL_CONTINUOUS_C_DEEP_FAR_SCALAR_SUMMARY
~~~

摘要SHA口径是UTF8紧凑JSON本体，不含分隔LF。report核同一bytes/SHA；没有实际摘要时输出独立unavailable schema，不生成假数值。

生产器本身的退出0只表示全部112条深端区间已写出。primary继续显式保cut_DN_matrix=null，finite_head_propagation_performed=false，requested_cut_domain_verified=false，cut_height_denominators_verified=false，以及full_BVP_or_closed_surface_accepted=false。

## 7. 清理边界与失败语义

无upload-artifact、无Release上传、无raw publisher。标量读回在always步骤完成后，下一always步骤只删除已明确命名的visible-continuous-C-far143根，且检查它不是symlink、确在RUNNER_TEMP之内、不是RUNNER_TEMP本身。checkout源码、Git历史和其他请求目录都不属于删除范围。

若科学进程只写部分行，原result保已写前缀与未访问suffix；若初始化或source binding前失败，readout明确No final producer result并保原规则/child日志范围。清理失败单独记工程错误，不改数学结果。这样raw不会因成功、异常或读回失败而被当作应该进入main的档案。

科学输出和来源恢复都可由本request+源+原历史身份再生。保留的是脚本、参数、真实run/commit、摘要和SHA。此处不预填尚未发生的run_id、job_id或任何实际成功数值。

## 8. 已做的静态范围与真正后继

本地已核11个当前实际文件pin，解析全部新Python和7个inline Python AST，并对9段shell作bash-n。三原输入、原九公式SHA、原R286证明与139逐dict一致；只有新增生产器和R312来源、独立请求/目录及针对深端图的readout发生变化。未导入科学源、未执行任何Arb函数、未跑旧fixture，也未发起Git或Actions mutation。

R312已发表；143不是证明登记前置条件。143也不以139的E结果为前置，但两者责任不同：本次深端图不能替代139的完整有限头积分和真实Rout。真正后继要以同一连续C的有限头表达传播全部112列，保cut所属域和高度投影的实际非零责任；可复用R277完整两端消元结构，不能拿旧finite零J换一个source标签。

