# Request160：v2明确编译修复后的完整128末态组件

作者：ChatGPT /root；日期：2026-11-15。状态：独立源码和唯一请求已完成；尚无本请求的实际运行结果。本地仅操作来源文本、JSON结构、字节和SHA；科学编译、矩阵、模型评价及测试只在本公开仓库Actions。

本请求接实际152的全部原责任。实际152的完整读回见[R337](../results/R337-actual152-complete128-replay-and-final-component-compile-block.md)，共用编译修复见[v2接口](2026-11-15-native128-qualified-json-statistics-v2-interface.md)。它从实际91原输入重新计算，不从已清理的152末态或其hash续接；实际shooting曾达容差不构成未来重复结果的承诺。

## 1. 完整新文件和原公开基线

新Python、MJS和request在本题computations；workflow在仓库根.github/workflows。本文在notes。旧152的全部原文件、请求、run和科学结果保持其原身份。

| 新文件 | 字节 | SHA-256 | Git blob |
|---|---:|---|---|
| geometry_20261115_native_operator_qualified_v2_final128_same_job.py | 41364 | `024a3c67ada93c908d86c68c4ba0326270d81d314a9c154439f5fc42266b8d2d` | `3f76106aa1c7e16b00cb03376474371cce914d10` |
| geometry_20261115_native_operator_qualified_v2_final128_bridge.mjs | 17228 | `f68e51d1d95aa0ccb0bd9b56e759fa5b20c36f03643f35292af6add633e0b9b5` | `17c86b3057d57a7e0d5ea554968142eb780c3b9c` |
| public-native-operator-qualified-v2-final128-request.json | 37592 | `cfa6fe343d227a98a3a755263ea7302ad7f3437f71adc82effd5a639d88ee697` | `2f1405da4493093158892bc3344ec6ea5c1df246` |
| visible-larger-public-native-operator-qualified-v2-final128.yml | 28811 | `f2af3e84ec060aa0117d21d12842b20cd88d20735e9560fb140a70cfe4446b7d` | `a37e1a7cd724142981ebb6e15091f99acfcda788` |

共用geometry_20261115_native128_qualified_json_components_v2.py已随161提交ce2b12c0f391a008343866ed9fe649f44d91ed28发布：17484字节，SHA-256 `5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf`，Git blob `1662a4021ee399881e7e05e01e1468ed69f65b07`。160独立消费它，不要求161先成功；其strict-field分支在160不执行。

原四件逐字取自实际152触发提交0bee3ef1e3587c2a530d98f5657f12e16179b489：

| 原文件 | 字节 | SHA-256 |
|---|---:|---|
| geometry_20261115_native_operator_qualified_final128_same_job.py | 41293 | `7c6b02680f4159e4666bf5111438b9fcaaf043b4994cd258bad43a2ab397c4f6` |
| geometry_20261115_native_operator_qualified_final128_bridge.mjs | 17193 | `0ccbc8241740b830b3eed0ba2b0e257a21ce93922848c88ad5b500ac5e5e9258` |
| public-native-operator-qualified-final128-request.json | 34173 | `9b69f49733d53c23395871a9311e4d0eedea58a221f30cb9fe10de58cac51cd8` |
| visible-larger-public-native-operator-qualified-final128.yml | 28467 | `7cc94e0b66f432a54ae8626ae7a22da0282b39dfe6b33a551a5558ac8a36df7f` |

原source_sha256的55个键和每一个原值全部保留；新增本次runtime、bridge及共用v2三项，总58。workflow的完整58名称集合与request一致。原52/47更早来源声明仍保留，独立新源相对原52的计数由3变6，不把旧shim/runtime当成新执行别名。原78-source公开历史恢复与实际79件slope-adapter消费范围依原152保持。

## 2. 实际错误及唯一编译变换

实际152原stage compiler return1、12456字节stderr和audit compiler return1、4723字节stderr均已完整核原行/原byte段，且两者未超编译时限。stage与physical中条件冒号紧接生成的::quoted，形成三冒号；stage另有两个BatchStats使用点在operator_trace128和shared_trace128之间歧义。后继boundary/endpoint缺实际stage而未启动。这是已经观察的编译问题，不是区间反证、共振结论或预算失败。

v2从SHA固定的原始未资格化C++文本生成RUNNER_TEMP副本。每个quoted(替换成一个ASCII空格后接::quoted(；这个前导空格把条件冒号与作用域token分开。只在stage两个原使用点明确写operator_trace128::BatchStats。所有数值表达式、根分支、原F/独立C、Gram形成、因子/回代、统计类定义/基类和physical使用的shared统计类型不变。

| 160实际可能编译的原件 | quoted次数 | v2副本字节 / 完整SHA-256 |
|---|---:|---|
| geometry_20261115_native_operator_trace128.hpp | 12 | 24653 / `4610e1e851a1f3b51f829355f08ef4555d1dc212b61f193db2edce5bb2a13435` |
| geometry_20261115_native_operator_stage128.cpp | 9 | 10747 / `2f45f84a462e0ee9f9613344994ca3117ffac0bab664c141b24e02b44ea753f8` |
| geometry_20261115_native_boundary128.cpp | 4 | 12505 / `37f6aab4604d6c39069486527eacda8c599c69ab496dadbbc74e92175fcd17ff` |
| geometry_20261115_native_physical_final128.cpp | 49 | 18202 / `ecf14bf4d5cfd7a9f7796d0fa513822a05ca6cdc5a3ecc291859cff58a91b265` |

stage只改std::vector<BatchStats> stats(p.depth)和size_t done=0;BatchStats total的两个声明。v2另声明exporter四处统计资格化供161消费；160不因此请求strict exporter/证书。每件临时源保准确计数、全逆变换等于原字节和声明的完整新SHA；原g++ flags、-O3、OpenMP、舍入选项及-lquadmath不变。

新runtime/bridge只更新文件名、来源SHA、schema、owned临时名及说明文字；全部替换逆序恢复后等于各自原152全文。workflow除同类身份/独立namespace改动外，只把完整source集合从原55扩为58；恢复原source块并反转声明替换后逐字等于原workflow。没有吞掉异常或新增数学检查。

## 3. 原输入与当前完整状态责任

实际输入仍为原91：run43672150224，source b78f0dd1471a118d2ed21467602509d188c2ab67，artifact14145200674，完整ZIP10267458字节，SHA `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`。原result、binding、577×224失败BASE state、H、target、sigma、far及全部literal/cells均按原完整身份恢复。它不是83 rejected trial或成功native锚。

两份原几何ready仍按8bd267107cc8710d371f3b62c02986655ac965b0的原Git blob及完整bytes/SHA恢复，使用原environment槽，只承担原constructor几何输入；没有恢复小core四输入、旧133/140/152末态或旧试探packet。request的inputs、frozen_geometry_inputs、预算、原容差/迭代、完整读回协议和三个旧历史证据块与152对应结构完全相同。

完整fresh64现场重新形成J及R273，保全部129248行、577节点penalties/常数，eta=1。之后原binary128 owner持有完整原状态，每轮从当前128残差取近似chord右端的64副本；固定初始64 J明确不是当前128精确DF。方向在128中用原sigma64和解出的z64准确提升后相乘。32方向上限、每方向十alpha、strict原sigma-scaled infinity norm下降与原2e-9全部保持。独立full226 fresh replay仍真实执行或明确partial。

原64流程在独立128实验返回后受控停止，不能把该协议exit2当数学失败或把128状态写成原64 accepted native checkpoint。matched_trace=none，原owner重复224方向循环仍不请求；全stage方向由后置完整组件承担。原失败BASE、当前H及far责任没有通过改锚降低。

## 4. 清理前的全部四个组件

同job必须把本次真实存在的packet、binding、执行owner source、precleanup owner summary、final-state.f128交给原消费者；每件全SHA核当前文件。缺实际状态则记未启动，不能由历史达tol推填。状态存在时不额外要求native_accepted先为true。

1. stages：原R305独立cached-angular/nominal-factor contracted action，全部576段、每段224方向；完整226状态包括两个mean。保持原root有限trace、独立C及全部角表，不偷换成单个selected field或仅少数列。
2. boundary：只在原stage数学输入完整时执行原R302完整112边界响应和全部链；其实际依赖条件与退出码不变。数值pivot不是严格非共振证书。
3. endpoint：只在原boundary完整时执行全部338×112混合端点响应。前112坡度及meanSlope用有限root trace RHS variation；second、meanSecond、height沿原对称cut程序。全338解析导数的声明仍false。
4. audit：保留独立预算，即使stage或boundary未完成也按原真实状态/几何尝试原物理jet和metric程序；它使用原C-based physical jet定义，不冒finite-root径向导数、连续ODE证书或无穷尾。

stage科学schema仍native-persistent128-shared-angular-contracted-trace-stage-maps-v1，未改成旧R302 stage标记。组件总schema更新为native-persistent128-qualified-JSON-and-statistics-contracted-trace-components-launch-v2；新同jobschema为native-persistent128-qualified-v2-JSON-same-job-final-components-procedure-v1。真实source及schema互相核对。

四项都完成也不自动构成原native/fullDN接受，更不能完成本题闭面/全t/同g/reach/整像held标准。当前实验是完整原有限末态责任；159的新C非零BVP及整面课题按各自真实来源并行继续。

## 5. 真实预算、依赖和终止

| 范围 | 原预算/预留 |
|---|---:|
| 从fresh64源/J/R273之前起的science绝对deadline | 19200秒 |
| 全局读回与cleanup预留 | 120秒 |
| owner请求上限，含fresh replay | 6000秒 |
| owner内fresh replay预留 | 1200秒 |
| stages / boundary / endpoint / audit科学cap | 8000 / 600 / 600 / 1800秒 |
| 对应组件overhead allocation | 345 / 720 / 345 / 345秒 |
| 单次compile cap | 300秒 |
| science step / compute job | 330 / 350分钟 |
| report job | 5分钟 |
| 原规则同步周期 | 2700秒 |

所有阶段用同一Python monotonic_ns绝对deadline的实际剩余时间；Node通过Python预算reader取值，不混用时钟起点。fresh64、J、R273、packet、binding、编译和读回都计入同一期限；编译开销allocation不保证科学全列完成。dependent组件不在缺输入时启动，audit预留和原cleanup grace保留。所有child留在原规则进程组，终止只匹配本请求PID/starttime后代。

原未访范围、active stage/step/column/query、因缺前置未启动、strict/math未决、I/O/编译异常与resource partial逐原记录分开。若强制终止来不及生成准确后缀，不据完整范围猜出实际已付位置。没有把19200重置到owner开始或提高预算；也未承诺新的compile或全224会成功。

## 6. 完整原字段和错误读回

沿152原实现保留NATIVE_PERSISTENT128 marker、90000-byte帧/72000语义value软界及完整typed-tree成员流。所有对象键、数组长度、键/下标路径、完整stage/column行与未访范围均保留；字符串分段或独立原canonical byte流不以hash代替内容。整体原文件bytes/SHA、重组canonical身份与原序列化有差异时的完整原JSON字节通道都保持。

每个组件正常、失败或异常返回后，先读其实际stdout、外层stderr和保留的子compile/science stdout/stderr，再读取完整原summary。原错误按12000-byte UTF8-surrogateescape分段，并在内层ASCII JSON中转义；offset/index/每块与整流SHA均保留，没有总错误字节截断。Node保完整owner stderr；workflow always补读仍存在的命名诊断后才删除本请求临时树。

primary小于90000字节只是完整compute语义流的索引。所有原returncode、summary_complete/transport_complete、partial/null/absent均保留；另一通道恢复完整文本只另记transport recovery，不篡改原child退出或科学flags。实际大型状态/因子只声明其原字节数/SHA和执行范围，不声称凭SHA完整读入矩阵或可恢复已删文件。

最后report使用BEGIN_VISIBLE160_SCALAR_SUMMARY/END_VISIBLE160_SCALAR_SUMMARY及实际SHA/bytes，对原完整primary逐字核同。原所有子事件标记保留，解析器可按旧152的无数值重建通道读取。所有raw仅RUNNER_TEMP；consumer结束和原诊断读回后才cleanup，不写Git/Release或新artifact。

## 7. 规则、来源检查与已做范围

workflow只由本独立request路径的main push触发；并发组visible-larger-public-native-operator-qualified-v2-final128，cancel-in-progress=false。原其他请求不修改、不等待。科学checkout固定为实际触发提交；原rules runner在独立镜像每2700秒真实pull/rebase并更新H的规则行，双README变化依原逻辑立即停止科学以应用新规则。

根README blob为21bd547f56590b7f2dd279d0297efb289a9b2783，topic为bff8aea253a9e6a7a4fac28d810ac454c5499fec；160发布前另核当前main，仅有变化才读差异。终端失联期间官方集成读取/发布不是git pull；不伪记真pull，恢复后补做。规则/取件token不传科学child，个人PAT不入任何源或连接参数。

已经完成：原公开四文本读取；55原source键/值逐项保持；58 workflow名称集合及三个新增source实际SHA一致；runtime/bridge全部明确替换可逆回原全文；workflow来源块和所有替换可逆回原全文；JSON语法及所有修改后的元数据字段核对；原预算、科学参数和输入结构逐项同。请求的六个experiment变化键恰为launcher、bridge、entry、component_launcher、component_report_schema、same_job_report_schema。

尚未声称：本地Python AST、Node语法、bash语法、C++编译或任何科学测试通过。本地没有可用终端；Actions沿原正常语法检查和真实编译执行，没有新增fixture、独立审查批准或数值门。本接口不含未来run ID、证书数值或接受锚。
