# R338　actual150：持久128全行下降与独立回放完成，严格230列导出器编译失败

本条记录真实公开 request150 的全部已返回阶段及未执行范围。两个 Actions job 均绿色，表示编排和完整读回受控完成；本次严格证书没有开始数值执行，不能由绿色状态推出230列证书、native接受或fullDN完成。后续应修复已实际定位的编译词法和名称解析问题，保持原科学式及验收条件。

## 338.1　实际运行、读回与原字节身份

真实 run 为 [43721616091](https://github.com/Rogerhu12/math-research-public/actions/runs/43721616091)，源提交为 d1d4c01a283d20a1d20131ece43cdcfb05ce757d，compute job 132834627616、report job 132850326043 均为 success。原请求 public-native-literal-root-certificate-request.json 的 SHA256 为 f6171df844a9688d3674c4bdb9f31885aae512e8440bb4118b13ff2a9a4906d2；实际启动记录逐项保留58个源码身份。实际源身份和运行参数见该提交的请求及 visible-larger-public-native-literal-root-certificate.yml，不以后来文件替换本次来源。

两份终态官方日志各只取一次，直接解析JSON和字节身份，没有在本地运行任何模型、矩阵动作、范数、Fraction或区间算术：

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| compute 原 job 日志 | 880993 | 9e8d037efcc0a276f0f1d996fa7932160f5333f45523cd6202280385f7c58deb |
| report 原 job 日志 | 79872 | 0f36f07ab272d2cab25511871d79a91167999216cf608c7984f21b1b779130f9 |
| BEGIN_VISIBLE150_SCALAR_SUMMARY 内原JSON，不含分隔LF | 37584 | 361d0c4f372fb666413886baad53550fc28cc3b76928a57810b695cf1509f65d |
| 清理前 launcher/result.json 原规范JSON | 98517 | d1283b014dfbbaf2eb2d77217d24129f8bfc19f80896131c4720e9365ff2b6f2 |
| exporter 编译器完整 stderr | 22236 | a4d909416a83364a318f8bb33a5a9bca472b04ce90077f5d5c0809a1debc9551 |

原 launcher/result.json 分为638个完整值成员与4个容器事件，共642条语义记录。读回保留原数字的JSON词法文本，逐成员检查原规范字节数和SHA，再重组整树；整树的98517字节及SHA与原文件记录一致。不是把二进制64或128数值重新求值后生成替代文件。576个原 packet cell 描述全部在该树中恢复；没有把这些描述冒充已存完整科学数组的独立再次检查。

编译器stderr同时以149个原行和2个字节块读回，字节块分别12000、10236字节。每行、每块与整件的原size/SHA均吻合。没有70KB总长截尾，没有遗漏的不可分行；空stdout与外层空stderr也保留各自零字节身份。全部可重算数值文件仅在原Actions临时目录形成，读回后按原规则清理；本文不把原大数据重新放入Git、Release或artifact。

## 338.2　真实输入与两类QR不可混同

本次先从真实 actual91 artifact 重新恢复原失败末态作为字面初猜，重新运行完整64位基点和R273，不读取已删除的113、133或140现场：

- actual91 run 43672150224，artifact 14145200674，原ZIP 10267458字节，SHA256 78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6。
- 初猜577×224原状态SHA256 f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6。
- 新鲜64位snapshot/result.json为1316字节，SHA256 64e4986ec42762f18b5949fd80723020b9c9d491a3582d98bafd25c2440eb2bb。
- 576个完整224×224旧精度J的原数组身份为1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4；此处是本次重新形成并逐字绑定的数组，进入128迭代后仅作固定近似chord，未标成当前128映射的导数。
- 原sigma数组SHA256 ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc；原far图395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54；原cut目标e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d。物理H身份仍c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f。
- 两个历史ready、原78源与全部literal64几何/角表均按原请求恢复，未再校准g，也未从一张表重造另一张表。

前置64位R273的原精确全行读回129248行、1153次QR、577个罚项、129248个纯常数行均已返回。其原64位基态norm为0.000060618737006888706；该前置方向的exact affine最大残差原显示为9.685623139820915231844260456306540893890861679791289092058094119E-11。这是前置64位模型的信息，不是接下来的128当前右端，也不是最终230列证书。

持久128 owner在自己的当前残差处另做一次R273。其固定chord矩阵身份为 ac980227832c8496f67fc908bf843b5391cbe411aef656212bcf128abc4b7896。完整行序保持 cut112、stage576×224、far112，共129248；节点577，列129248。该次实际记录为：

| 原记录项 | 原值 |
|---|---|
| eta CLI | 1 |
| 完整QR次数 | 1153 |
| 完整形成调用数 | 576 |
| augmented rows | 258496 |
| 罚项节点块 | 577 |
| 纯常数行 | 129248 |
| 因子及常数原字节数 | 464891392 |
| QR elapsed_seconds | 6.450837740999987 |
| 当前128右端转64后改变的项数 | 128969 |
| 非零转零项数 | 0 |
| 原sigma归一转换误差最大原显示 | 4.10665514535721833358792197700840237e-21 |
| formed residual infinity原longdouble显示 | 9.685824747510231713e-11 |
| full unpreconditioned model gradient L2原显示 | 1261309.1059448874298 |

最后两项是原longdouble数值读数，不是R314/R325严格误差界。右端的近似QR转换未覆盖原128残差或状态。全577×224方向在128中按原sigma乘已解z64形成；原记录 different_from_R273_delta64_entries=129182，maximum_scaled_recovery_difference=6.21420740974797949698112574685574514e-28，nonzero128_from_zero64_recovery_entries=0。全方向.f128为2067968字节、SHA256 a2364e304467a1cd83d744430e66a8c623c69e789dbe72381e69deaa346e18a3。这里没有局部裁切、cut/far额外投影或状态回写64。

## 338.3　唯一实际128试步与完整末态

原32方向上限、每方向十档1至1/512、原sigma无穷范数严格下降规则及原2e-9停止阈值保持。真实执行只有方向0、trial0、alpha=1，随后达到shooting阈值而停止；未访问方向1至31、该方向trial1至9。未访问不是拒绝，也不是补算的成功。

初始完整128评价：

- norm = 0.000122096054597410989492629881621789239；
- binary128原hex = 0x1.000dd1f7889da0c80213a1f62c65p-13；
- 最坏stage11、Pi104、global row2791，input node12、output node11；
- 完整576段、129248行，failed_stages=[]，evaluation_error=null；
- root calls27772、Newton_steps904、line_search_trials904、maximum_iterations1、fallback_returns0；原阈值返回计数27772。

唯一试步完整返回 accepted=true，reason=strict-original-norm-decrease：

- alpha = 1，原hex 0x1p+0；
- changed128_state_words=126690，其中changed128_with_same64_cast_values=11183；
- elapsed_seconds = 805.319227762；
- norm = 9.68582474751023176032080482454992093e-11；
- binary128原hex = 0x1.a9fcb11a67aa9fdf970095730bcp-34；
- below_original_tolerance=true，完整576段与129248行，failed_stages=[]，budget_exhausted=false；
- 最坏stage9、Q1、global row2128，input node10、output node9；
- 最坏原残差4.99890220172700756918252291853272271e-25，原sigma5.16104960810073433235339041548094359e-15。

末次返回root统计仍是27772 calls、904 Newton更新、904试探、0fallback，maximum_iterations=1。最大已返回相对root残差原显示7.97942273584970897156361583077509912e-14；minA=0.999999999975949816097646428367803865，minD=0.999999999999985782663062751174097867，minS=0.999999999999999999999999999688946329。这些是原所选有限停止策略的返回统计，不是对准确F真根的外包。

最终状态2067968字节，SHA256 e0f20c36d59ac200796a03441e7b5604224e3add414361a11cc6ff3586dffba2。最终残差同字节数，SHA256 18cfb3face9b286513f624003984d318bc6b6c735ed803a3cbffde15dc6be39b。完整576×226段输出2082816字节，SHA256 13195bbb4249c47b158399c36d173de0fc8bfc80e3b9f5ad98ed1411ff715f9e；其两mean列未删。原mean_height_sum=0.0226842463487103007695708959242220956，hex 0x1.73a8a00cef80fae4744e57d3f5bp-6。

本次shooting结果与R308已有的持久128实质进展相容；本条只根据actual150自身原输出陈述，未借别的run补足本run责任。

## 338.4　独立fresh128 replay的真实范围

同job清理前启动独立进程，直接读取最终binary128状态；alpha=0字面复制，不先转64。独立进程返回完整cut、576stage、far的129248残差及每段全部226输出。原记录：

- independent_fresh_replay_complete=true；
- fresh_replay_full_residual_words_equal_owner=true；
- fresh_replay_all226_output_words_equal_owner=true；
- 残差和完整段输出的原SHA分别仍为18cfb3fa…、13195bbb…；
- replay norm、最坏行、原root统计与末owner记录同值；
- owner与replay的process returncode均0，wall_timeout=false，stderr均零字节。

这是完整有限残差与均值的独立回放，不是原几何审计、112边界响应、338×112端点灵敏度或fullDN。所有状态和段输出已在原临时目录清理，不能据这些hash捏造以后可续的128现场。

## 338.5　后置230列严格消费尚未进入数学计算

本次明确选择最终状态的 stage10、RK step0、field0，原root policy，320bits，完整230列：224个形状坐标及6个独立环境坐标。目标是R314/R325固定记录字段输入的严格传播，不是整个576段及上游RK误差的证明；即使完成也不会自动付清完整native终检。

清理前交接确已发生，实际末状态与owner summary被逐字绑定。原owner handoff为110832字节，SHA256 34c2886848b5f3a739cc527502da6dc61fb5e59ffb383ab5b979a3f95a0fb932。完整packet为10348368字节、SHA256 1c9df6b2aa203d526eee11fe443ebcb474584c677b76ed3901b6a0f6c1f37aa8，涵盖576 cells、6943原子RK步、20829几何采样及原2048角表。完整packet结构规范JSON为79506字节，SHA256 0557fb2e87c5f529551d3027b48004148f04eacaba6e955508c68e3fe4585bb5；literal w、w2、E没有互相推造。额外physical query packet只形成，不表示原物理audit已执行。

实际失败发生在exporter编译：

1. temporary-qualified geometry_20261115_native_operator_trace128.hpp 第339行的原诊断表达式被无空格token替换变为 failure.empty()?"null":::quoted(failure)。编译器原文为 expected ':' before '::' token，随后expected id-expression及括号错误。temporary-qualified geometry_20261115_literal_root_field_tape128.cpp 第220行也出现同一三冒号。
2. exporter中第11、57、91、146行的无资格BatchStats同时遇到 operator_trace128::BatchStats、shared_trace128::BatchStats以及全局using别名。编译器原文明确reference to 'BatchStats' is ambiguous。其后reported non-class type int、invalid initialization of reference等为同一编译过程的后续诊断，不能解释成root矩阵或数值导数失败。
3. 实际compiler returncode=1，timed_out=false，elapsed_seconds=0.6654833709999366，allowed_seconds=300；exporter可执行文件未产生。
4. launcher error为ValueError('actual-exporter-compilation-returned')，其traceback完整保留；child returncode=2。export=null，certificate=null，scientific_summary=null，procedure_completed=false，scientific_certificate_complete=false。严格consumer从未启动，所有230列索引0至229均未执行；不存在遗漏的已完成证书行。
5. 原certificate_unresolved=false、budget_exhausted=false并不表示已排除未决或全部证明：它们与export/certificate为null共同表示失败在区间算法前。不能把缺失结果读成域反证、可逆性反证、root停止策略失效或资源耗尽。

原JSON资格化记录准确保留两份临时源：exporter原13437字节/2aa2ad6737ca16854350967bddf49846e345ba5195d799d21dcc40a870c925bb，替换后13441字节/425422732388512435fc2dbecadc1098ff3a1c2400ac3f620b91879fb6cd846e；operator header原24617字节/950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0，替换后24641字节/046fafc0421ebf22a68437abab62594a525acbec815a660719f91a2c18cd0a0e。原调用计数分别2、12，逆替换等同原源的检查只证明替换来源，不保证生成C++词法合法。

## 338.6　总资源、过程退出与未付终检

绝对全局deadline从science入口开始计入fresh64全J/R273前置；本次并非到期。进入owner时剩余18285秒；请求owner6000、replay reserve1200，证书science cap9000、export cap1200、组件total10650，另保清理读回。进入证书前remaining_scientific_seconds_before=15731，退出后15730，resource_partial=false。

实际外层elapsed_seconds=3350.381450517；owner launcher elapsed_seconds=2432.99851193；wall guard2434.306183377秒、guard_returncode0、wall_timeout=false。阶段时间是各原计时范围，本文不据其差值另算未保存的耗时拆分。

原64 worker被明确受控停止，没有执行原64十档回溯，也没有把128结果写回64响应；original_driver_exit_code=2属于这一受控源程序结束。外层procedure_complete=true、summary_complete=true、transport_complete=true，与后置certificate科学失败是不同字段。两job绿色不覆盖该失败。

以下原最终责任仍未付，均按实际false/null保留：

| 责任 | actual150 |
|---|---|
| 所选字段的严格primal证书 | false，exporter未编译成功 |
| 完整224形状列及6环境列证书 | false，230列均未运行 |
| 上游RK误差、完整RK stage证书 | false |
| 完整576 stage列、cut/stage/far129248严格导数 | false |
| 112边界响应 | false |
| mixed endpoint338×112灵敏度 | false |
| 原C-based物理审计/原几何终检 | false |
| fullDN完成或接受 | false |
| native_accepted | false |
| F真根外包、C=F_e、IEEE roundmap导数、动态分支稳定性 | 均未声称 |

下一项有明确工程依据：独立版本保证条件运算符冒号与全局::quoted之间有词法分隔，并按实际exporter所需的operator统计结构显式资格化BatchStats。旧150/152来源保持原样；修复不更改原root/RHS、R273、224/226/means范围、严格证书公式、原阈值或最终验收门。真实新执行仍须重新形成fresh输入和持久状态，不能从本次已清理raw的hash恢复现场。R334的后置37-query诊断是独立任务，不以该编译问题为其新的数学门。
