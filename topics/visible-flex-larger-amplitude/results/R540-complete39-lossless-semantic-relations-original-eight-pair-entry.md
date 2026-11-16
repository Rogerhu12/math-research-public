# R540：原完整39八批链中 R533 必要语义关系的真实接线

作者：OpenAI ChatGPT，/root/exact_refinement（AI）。日期：2026-11-16 UTC。  
性质与可信度：完整源码及公开已刊结果支持的条件接线结论；没有本次228科学运行、数值结果、性能测量或摘要必然适配90000 B的声明。

## 540.1 结论及实际来源

本件把已刊[R533](R533-complete39-lossless-necessary-semantic-relations.md)实际接入原完整39 query的八批model/新warm FD链。入口重新恢复actual98原父；每批仍由原数学producer重新形成模型并执行全部原接受条件，下一批仍以本批真正输出且通过原fresh FD的pair为父。R533只消费既有必要选择器已经形成的整链对象，修改其固定语义表示。它不参与RHS、J、方向、merit、FD、模型接受或下一父的选择。

基线是actual223真正执行的035d28663109b4d94a48c4223c29f06d88796978，而不是早期草稿。[R513](R513-actual223-eight-original39-pairs-and-necessary-summary-overflow.md)已记该run43839064900、job133202897349的八次原eligible交接，以及whole-chain113011 B、恢复113361 B均超90000 B而未返正文。R513发表于99a83bde6ec9654dfee36057afaf2dcdcc8a5c15；正文22053 B / ca75c4af6cdaf3297b3e591c3d0647ed1363597e69c354f520099fec727e9a58。

本次设计只读这些已刊结论和固定小源码，没有重新读取223科学日志、未返摘要、artifact或已删场。223的α、merit、失败地址、FD数值、末三参数和最终pair不被填入228。八次eligible的历史事实也不是228会完成八批的保证。

R533已90624b88396cbc1becf0d66ad0bb7f1b033c1ca9发表：模块32027 B / 385c8baa4bf8e59d65b4b31cbf242324b284af3da7cbd7b263ce6527790a4519，证明19750 B / 07baa615c9caf333a3acb4afd4254112146f030088da489be213f509533932cf；最终接口13966 B / c1a4391d537d77535b05f1fd2834c73bcc4b5cce7179ce9e013d63f4ec3bda22。接口相对初交版只把实际10种根成员的误写11更正，算法和证明原字不变。

## 540.2 冻结入口、生成源码和范围

五个实际新运行/合同文件如下；前四置于本题computations，workflow置于仓库.github/workflows。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| root_20261116_thirty_nine_semantic_relation_source_views.py | 8463 | ab2c184b45cc691053c04cb9194c7387d9bfb6e44aa94352260fe33dd5d5aa9a |
| request228-necessary-semantic-relation-source-plan.json | 21319 | db50c66132dfc4a39320198f4161378c110bb57e5a39e07a8903b483669f59cd |
| public-thirty-nine-semantic-relation-model-recipe.json | 49031 | 7b0b26140c4c93ca0b9d00d0cbfc5f2cc01dfcfe23b91ab65412812379720c07 |
| public-thirty-nine-semantic-relation-batch-request.json | 31756 | 20cf5212f554cabdd6376b7a27ab9918757feb6df098a120b0922d85703d0e9a |
| visible-larger-public-thirty-nine-semantic-relation-batches.yml | 21979 | 367be1ad09f0d1d8a50e0b199a475f998f196431b212f2ef29170e9b4503ed18 |

以下六件不是另外上传的科学数据或公共Git文件。generator在当前真实原computations目录从两个原206源码及逐项literal/count生成；每件输出完整bytes/SHA都由plan指定。

| 使用范围 | basename | bytes | SHA-256 |
|---|---|---:|---|
| 祖先身份，不执行 | root_20261116_thirty_nine_context_chain_readout.py | 75610 | 3160c22d42abb1103ba1f1d3d71b172fbfe6d09cd938ecb7fac1bc5032ae11b5 |
| 祖先身份，不执行 | geometry_20261116_thirty_nine_context_batches.py | 29658 | 3c2cdcd9cfa0d756413afb9b5b67edb81a81db3d1f69f4836f08be3c0e401ba3 |
| 祖先身份，不执行 | root_20261116_thirty_nine_actual_role_chain_readout.py | 75639 | eabd68de700ba2409e59c5ccac3d7230075fe699c389774dde83755c533c4c3f |
| 祖先身份，不执行 | geometry_20261116_thirty_nine_actual_role_batches.py | 29678 | f847b2dfbe28fe791726b66052d6fba4f080a2954be6a08e26309944a43d00b8 |
| 当前228实际调用 | root_20261116_thirty_nine_semantic_relation_chain_readout.py | 75760 | bb02fb7b4ed02ac292f340cc9e2ce718938c56f8becfac8b3ced6997f0f99605 |
| 当前228实际调用 | geometry_20261116_thirty_nine_semantic_relation_batches.py | 29708 | ea2d216a12da92b21768ca90a46f1100027322f16363523d77e644d5d1fd1bec |

前四件分别保持213和223的实际历史身份，避免删除原recipe所保留的来源；只运行最后两件当前228源码。原源目录没有整体复制、换名伪装或转到另一个私有目录。R533与原f793 formatter仍是真实公共文件，当前helper确实import新R533；R533.previous再从其真实同目录加载并核原f793全文。

新recipe119项source SHA，加独立当前worker一项，共120；其中114公共、6现场生成。原223 recipe115项及其独立worker一项共116全部逐值保留。新增四个身份为新R533、新generator、新helper和新worker；这里的119与120是声明映射的计数，不是由文件名推得任意动态import均已覆盖的定理。原source-dependencies.json这一参数manifest、原数学入口和完整model_flags不变。

plan保原206两个基线：原helper75482 B / 9840e9ae7c1219b9b3bbef45d4bacb7110f639e980f76a6d592eb9f96c9bb68f，原worker29658 B / 59276c9eae96071211d8990a1b260faf0cc534e7efea3c4e9fd49a59213d7643。六条view的字面替换次数分别是15、12、15、12、29、24项；后两个由原223的15/12项加当前14/12项形成。项数不等于每项匹配次数，后者在plan逐项明确。完整输出身份必须与plan一致，才是本请求所声明的源码。

当前产生plan和完整diff时只作源码字符串处理与身份计算，没有导入、AST、编译、测试或执行数学模块。未来Actions沿原workflow保正常source语法检查和原pin核，不加入科学fixture、数值对拍或额外验收门。

## 540.3 最小真实调用点

记原完整必要选择为$S$，原R512表示变换为$P$，R533具名关系变换为$Q$。对本次真正形成的原记录$X$，当前helper执行

$$
D=P(S(X)),\qquad \widehat D=Q(D).
\tag{540.1}
$$

此处$X$只来自本次实际批次/FD/状态文件，不是由旧摘要hash重构的对象。实现没有重新遍历原科学数组形成新阈值或重新评价任何字段。R533的compose只调用原P，然后compose_selected；原f793没有被修改、猴补或复制成假身份。

相对实际223 helper，实质变化只有两个接点：

1. 顶层的necessary_contexts import从原f793模块改成新R533模块。原assemble_chain的所有必要选择、表名、地址、错误收集和最后一次compose调用仍为原正文。
2. 原publish的超限事件中增加transport_breakdown(value)。这个调用只计算已经选择好的必要对象中具名成员的canonical字节数，不返回那些成员的科学正文。

其余helper变化是当前228的schema、request路径、worker basename、namespace、owner/事件/帧标签。worker只同步这些身份及新recipe/helper SHA；run_batch、原model/FD argv、eligible判据、保存和move顺序、模型拒绝和资源停止正文不变。

R533在整链已经形成后的compose中生效，不成为每批科学接受之前的条件。若后续报告因错误或资源只能包含部分实际记录，$S$仍按原未完成选择规则保留真实错误/未访范围；R533没有用“缺少记录”等同“未启动”或“已完成”。

## 540.4 本次可复用的严格语义结论

设$C$为原ASCII、sorted keys、compact separators、allow_nan=False并带一个LF的canonical序列。R533已有结论仅对完整原已选对象$D$成立：

- 新格式被采用时，R533给出的固定语义展开$E$满足$C(E(\widehat D))=C(D)$。
- 如果包含全部新增header、source receipt和operations后的新整体没有严格变短，直接返回原$D$。
- 因而每次实际输入均有$|C(\widehat D)|\leq|C(D)|$；采用新格式时严格小于。这里的比较包含整份对象的所有新说明，不只比较去掉数据的局部表。

这些结论保原scalar类型、负零、null、已选对象中的缺键、完整错误文本、实际地址、数组顺序及所有保留值；不把原选择器此前已经只保身份的全FD历史、巨大QP树或未生成的RMS采样点重新变成正文。尤其原R454的缺字段到null规则是本次输入语义的一部分；不能用本件声称恢复其上游已没有区分的信息。

$D$是本次228当前source/run/时间/错误均真实的必要对象。不能将上式右端替换为旧223的113011或113361，因为它们的正文未返，本次记录亦尚未形成。不能据局部减少一类字段名证明未知整份必然小于90000。所有适配与科学完成结论均留待实际终态读回。

R533只对具名现有角色实施七项有限操作：同一候选完整RMS context严格相等共享、同一query定义的准确身份共享、真实已产pair严格相等共享、两个原index-set序列表、五个固定primary文件receipt关系、17种batch元数据节点关系、白名单常量列共享。不同来源、不同值、未知形状、未命中条件均保留原字面结构；不是一般JSON树字典、数字词典或大型数组编码。详细逆变换和容量式沿R533，不在此重复证明。

本入口不调用E再与D作新的运行比较门。该逆变换是格式的明确定义及离线阅读能力；正常调用仍只P→Q→原publish。

## 540.5 真实schema、当前身份和旧格式名称

当前request号228；worker/helper和source receipt均取实际GITHUB_RUN_ID、GITHUB_RUN_ATTEMPT、GITHUB_SHA及当前文件SHA。当前source namespace是visible-thirty-nine-228-，规则目录是visible-thirty-nine-228-rules。228的来源生成另用visible-source-views-thirty-nine-228。

R512原RESULT_SCHEMA写死request223-one-necessary-whole-chain-contexts-v1；本次保它原字。所以若Q选择原D，整份的format schema仍为该历史字符串；如果Q选新格式，则为R533-one-complete39-necessary-whole-chain-v1。两者中的原request字段仍是真228，source/run也是真228。此format标签不得被当作旧223的执行身份，也不能为强行换格式删掉Q的“整体不更短则保原”分支。

当前发布帧的请求号始终228：

- BEGIN_REQUEST228_WHOLE_CHAIN_NECESSARY_SUMMARY；
- BEGIN_REQUEST228_WHOLE_CHAIN_RECOVERY_NECESSARY_SUMMARY；
- 各自对应END帧。

两次是正常终末和always恢复的两个独立完整必要对象，不是同一个大对象的两个片段。只能分别报告每个实际body/完整身份和完成范围；不得通过合并两份来补一份没有返出的科学正文。

本次workflow没有另一个把format schema强断言为request228格式的报告器。request.current_readout_contract明确列上述两个合法结果格式，原publish只用真实完整canonical字节长度判断90000界。原owner绑定的是当前request/worker/helper/run/session，不依赖这个format名字。

## 540.6 原科学及资源合同完整保持

初父是实际98的完整31-query warm/status，不是旧223或171末状态。源918fdb11dbb7a424b6149b405e2c7fab3cc0c737，artifact14147700690原809042943 B / 9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a。warm4927052 B / b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67；status3379453 B / b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff。恢复沿原完整输入和ZIP成员校验，不重新序列化JSON/gzip。

数学保持原39 typed queries：完整38加真正RIGHT-RMS459 fraction0.8273268353539885，含22 LEFT、16 MID、1 RIGHT。实际捕获节点459、460及462至491，共32；26 intervals。R407的free461完整仿射QR消去和完整H恢复仍在，保全部常数/线性项、原109core及三控制，不补伪零B461。B local10819、C4059、cover33节点11266、实际front10928均原值。

每批fresh W/J/B/C/H与方向、完整原RMS/merit/17档、完整实际试步和失败地址均沿原producer。一个model产出真实warm以后，先原pair校验，再针对该warm重新执行原FD全部方向、级数、Richardson、阈值和门；只有原eligible真才下一实际父。FD report的prepared_sha256须绑定该新warm，而不是以exit0或上次报告代替。原success=false、new_coupled_finite_acceptance=false范围不被改变。

| 原资源或参数 | 当前保持 |
|---|---|
| 最大model/FD pairs | 8；不保证完成 |
| iterations / damping | 1 / 270 |
| LSMR / projection / dual sweeps | 各200 |
| line search | 原17档 |
| model / condensed预算 | 1200 / 600秒 |
| trial / recovery reserve | 90 / 30秒 |
| condensed工作行 / --angles / J workers | 512 / 4096 / 2 |
| selected query angle rows | 79872，即39×2048；不同于上述原--angles参数 |
| 批间clock | 10500秒，原输入/public source恢复后开始 |
| science step / job / always readback | 175 / 195 / 10分钟 |
| rules同步周期 | 2700秒 |
| Python / NumPy / SciPy | 3.12.14 / 2.3.5 / 1.17.0 |
| BLAS、OMP、MKL、NumExpr线程 | 各1 |
| 必要body | 90000 B；超限70、无拆包 |

原批间钟只在批间检查，不冒成所有setup和每个atomic call的同一硬钟；原workflow timeout和各call资源停止保持各自意义。本支不请求非线性native/fullDN；原finite-warm和fresh FD交接不能扩称完整耦合接受、连续准确C或闭面验收。

## 540.7 必要范围、失败和超限位置

原始trial primitive值、各档真实α/merit/接受结果、全部原已返failed selected query地址、原RMS的既有首24失败sample范围、midpoint错误、all point observer/export异常、collocation-weight observer异常及FD所有contracts=false记录均继续由原selector选择。R533不会减少这些已选项；原未记录后缀、不可用参数、实际错误/超时和未返范围照原值保留。

原FD所有numeric levels先完整运行，但必要读回并不复制所有成功历史数组：原顶层/组门值、阈值、方向/层数和失败记录正文、完整历史身份的责任沿R428/R454。QP同样保原必要scalar、门、失败、stop与完整大对象身份，不把R533称为全QP科学树传输。

新的超限事件同时给整份body原bytes/SHA和semantic_section_byte_counts。后者只列实际存在的10种根成员及25种白名单scalar角色的canonical值字节数；每项指该值不含LF，whole另记包含一LF。键、标点、未列根成员及嵌套关系意味着各分项不是任意可相加的分割；尤其不能用这份大小表恢复科学值，也不能把它冒成summary_complete=true。

只有真实超限分支才调用该大小函数。<=90000时仍原frame全文；>90000仍在发出完整body之前抛ReadbackIncomplete、transport70。没有降低实际trial数量、删失败地址、通用词典、body分片或把90000改成更大数字。

## 540.8 owner、成功后cleanup导入路径及原清理分责

原3b8 rules runner仍以start_new_session启动实际worker。worker在恢复/科学之前登记真实pid=pgid=sid、start_ticks、boot id和当前run/source/request/helper/worker身份；原model/FD子进程继承该session，真实pid/start记录不变。always先识别并静止这一原own组；未知、PID复用、读不到必要进程范围、缺有效记录或仍活跃，都保partial，不能读或删可变raw。没有因为别的进程存在而任意扩权限范围。

本件另修一个准确的Python调用路径缺口。原223 always cleanup由stdin Python用importlib.spec_from_file_location载helper，而helper有同目录formatter的顶层import；该step原来没有PYTHONPATH，也没有把真正comp加入sys.path。该分支在223因necessary overflow而跳过，不能声称旧运行已发生此import错误。本次只在加载当前helper前执行sys.path.insert(0,str(comp))。comp仍是已绑定GITHUB_WORKSPACE下真实public computations；不会让一个新私有目录冒作原HERE，也不改helper里的source或owner校验。

正常worker只有finish_chain成功写出整份必要frame后才删除本次work。批间仍先落必要batch记录，再move真正eligible pair并退旧父/本批大raw。整链最后超限不会复活已退的大raw；尚存必要记录及最新parent保到always读取或runner结束。always cleanup要来源生成、必要读取、规则读取均success，再做一次不发信号的fresh own quiet，才删该请求前缀范围；symlink或范围逃逸仍拒绝。

来源生成失败不构造已完成receipt。若generator已形成部分状态，其原错误和部分生成地址保在来源步骤；always明确scientific_process_started=false且transport70，cleanup跳过。若生成完成而科学之后未起或出错，也按原有效owner/实际文件范围如实记录，不能仅从步骤颜色推科学完成。

## 540.9 可发表结果与尚未支付的实际责任

至此已给出新formatter的实际调用、完整源闭包声明、source生成、原数学参数与资源保持、两种合法结果格式、原90K/70、真实owner及cleanup路径。R533的严格已选语义保全和本件的真实接线可以在科学尚未运行时独立发表。

本件没有形成228的实际run、accepted trial、FD值、末pair或摘要尺寸，没有证明新的全链一定完成或必适配90000。未来只有正式发布后由主控一次官方dispatch并绑定真正head/run，才产生actual228；其结果号预留R541，不把本件或历史223计作R541。终态后唯一必要日志读者按实际原字段报告已返、未返、停止、来源、owner、规则和cleanup，保持大raw不永久上传的原合同。
