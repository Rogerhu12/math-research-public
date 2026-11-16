# Request226 / R536：真实有限root词、完整原128链及必要读回接口

作者：ChatGPT /root；必要reader：amplitude；物理路径子件：geometry（AI-assisted）  
日期：2026-11-16  
状态：**完整执行来源与条件接口已成；实际run/head必须在正式单次dispatch之后记录。** 实际结果预留R537。本接口不是一份数值结果，不预填原6000秒是否足够、J/FD/fullDN接受或90K容量。

对应[R536完整条件证明](../results/R536-original128-root-finite-words-complete-full112-entry.md)，真正数值source来自已刊R535；后置R522/R515原字保持，不使用R534 projected64模型。

## 1. 本次四运行件

全部相对topic，workflow除外。

| 对象 | 路径 | bytes | SHA256 |
|---|---|---:|---|
| generator | computations/root_20261116_live128_root_words226_source_views.py | 30464 | 14a86c71268ccd017c6e85294c7af9b714c2234063c2ef1953caf35458bd6052 |
| source plan | notes/r536-live128-root-words226-complete-source-plan.json | 62193 | 772e3da8b00d692672802b0e61f0e038b08b0014b03ad7e136f9cb312412ba69 |
| request | computations/public-live128-root-words-original-full112-FD-fullDN-request.json | 71828 | 668518481e635c4832df3a5ab8a9709585d2358546904cee0eeab0df032e2c64 |
| workflow（相对repo） | .github/workflows/visible-larger-public-live128-root-words-original-full112.yml | 18755 | 0d23754153779173dc6d4973ba06325896f193c0316f043cc10258cae4dd93c1 |

证明与本接口一并刊出，展开的十一caller和两个R535 C++ view不刊Git。原R522三件仍由其已刊生成器实际形成。当前科学输入不是226专门缩小的fixture；完整原112链、所有原门和原资源scope保留。

来源计数345public+16generated=361。全部原225的342public保原值；R518十二与R527十一中间源在内存按完整plan复原，不落为旧名执行；三R522、两R535、十一新caller才是当前生成集合。完整source plan及冻结request给全部源，不以这个数字替代对实际callee的来源责任。

## 2. 实际schema、命名与祖先边界

| 角色 | 当前字面 |
|---|---|
| request | public-live128-root-words-original-full112-FD-fullDN-request-v1 |
| request_number | 226 |
| namespace | visible-live128-root-words226 |
| source preparation | R536-live128-root-words-source-view-preparation-v1 |
| current policy | R536-current-H-live128-root-words-client-policy-v1 |
| owner | R536-current-H-live128-root-words-owner-call-v1 |
| pipeline | R536-current-H-live128-root-words-call-pipeline-v1 |
| assembly | R536-current-H-live128-root-words-response-assembly-v1 |
| runner | R536-live128-root-words-original-full112-owned-procedure-v1 |
| fullDN | R536-live128-root-words-actual63-H-original-FD-and-complete-fullDN-v1 |
| science necessary | R536-live128-root-words-original-full112-necessary-v1 |
| source necessary | R536-live128-root-words-source-view-preparation-v1-necessary |
| 原job clock | R493-original-full112-live128-job-deadline-v1 |

原225 request64734B/42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285和plan55391B/6e8109e64bafb6e78428298ccc25a5b4d71df29c0b224b0ea20076da006dd1c6保字节，原R527_source_composition成员是明确祖先，不是本次producer。新R536_source_composition负责当前actual request/source/namespace。

owner内部VIEW_PLAN仍原R527 engineering来源及其完整derived SHA，不能把该嵌套JSON也随外层标签改掉。真正owner_scope的compile_owner由R535明示替换，实际安装和编译另有回执。源文件还在或source准备完成，不等于原运行体全字未改。

## 3. Source准备的具体CLI与文件

COMP必须是GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations。SOURCE_META必须是RUNNER_TEMP/request226-source-preparation。调用如下：

~~~sh
python -u "$COMP/root_20261116_live128_root_words226_source_views.py" prepare \
  --request "$COMP/public-live128-root-words-original-full112-FD-fullDN-request.json" \
  --request-sha256 668518481e635c4832df3a5ab8a9709585d2358546904cee0eeab0df032e2c64 \
  --out "$RUNNER_TEMP/request226-source-preparation"

python -u "$COMP/root_20261116_live128_root_words226_source_views.py" readback \
  --request "$COMP/public-live128-root-words-original-full112-FD-fullDN-request.json" \
  --request-sha256 668518481e635c4832df3a5ab8a9709585d2358546904cee0eeab0df032e2c64 \
  --out "$RUNNER_TEMP/request226-source-preparation"
~~~

prepare先核原221和225合同、所有345public、全部metadata计划以及本生成器完整身份。original_scientific_contract的唯一说明勘误是output_jets_order；生成器先复制整个原对象，再只按计划改这个字段，逐对象要求其余内容完全一致，不跳过整个scientific contract验证。

R522子生成器在SOURCE_META/R522记录；R535实际CLI为：

~~~sh
python -u "$COMP/root_20261116_native_root_finite_words.py" \
  --source-plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/R535-native-root-finite-words-complete-source-plan.json" \
  --binding-out "$RUNNER_TEMP/request226-source-preparation/R535/source-binding.json"
~~~

完整R535 plan10232B/f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b和adapter10892B/1c99623e2cd63d0a4700011c96e5054645cf7dd8ee5cf3357f0c77d1727026db保原字。它只写两个source include及binding，不执行C++编译或数值。

主source-views.json有当前run四键、request/plan/source身份、全部实际public校验记录、R518/R527文本中间身份、两个child完整状态、生成及未生成角色和真实错误。源child非零时仍观察已实际存在的两个R535输出，保真实完整匹配/partial信息；不把存在文件直接推为全部source准备成功。

readback输出RUNNER_TEMP/request226-source-necessary.json，frame BEGIN_REQUEST226_SOURCE_PREPARATION_NECESSARY / END_REQUEST226_SOURCE_PREPARATION_NECESSARY。它给source_necessary_json、source_necessary_bytes、source_necessary_sha256、source_readback_complete、source_preparation_complete这些step outputs。全body包括完整原source stderr；90000B超限70保完整临时scope身份，不拆科学raw。

## 4. 十一当前执行源与五个原后置/数值view

十一caller的全部完整身份见R536证明表及source plan。关键真实入口为：

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| owner | geometry_20261116_live128_root_words226_same_call_owner.py | 21969 | 934e92b1d381e5c268346556327fb76147c20e73bb9b4b9ddb6ca91aad7ab3fb |
| current_call | geometry_20261116_live128_root_words226_current_call.mjs | 36879 | aa05fa425b41382b0177772c21b8134040925fdca323e3aa35ab3473c414055c |
| fullDN | geometry_20261116_live128_root_words226_original_full_dn.py | 37692 | 97bb244447ef809ed17cf73fe3dde75c440630e9d9441c3b188a73f7d7cd32bc |
| runner | geometry_20261116_live128_root_words226_owned_run.py | 38985 | 8801c39604dfa6c7a6087886fffb3aefefdcf9f1a0c51152acbb6ff93793a0fd |
| reader | root_20261116_live128_root_words226_necessary.py | 52189 | e90e3abd2e40ebd469bcd8d4dd7f221848c9926c91b86c8e2ee29235b1be864a |

原R522三件operator29617/082d、stage12880/49a7、component33416/93ec保原字。新R535 source primal25230/3e1c、trace34950/2e12保已刊完整字节。所有源在同HERE实际存在后才进入原输入/科学流程；不能把未来generated view按普通Git文件抓取。

R535 cache只安装到实际owner的原编译函数。原stage组件及R515三个物理site不是由此自动重编成另一个缓存版本；它们保自己的真实source和compiler receipt。全source图不能因“cache”这个同名词被合并。

## 5. 原输入、资源和实际科学CLI

以下对象与225完全相同：original_inputs、actual63、actual91_artifact、runtime、live_call_resources、resources、reviewed_README_blobs、retention，以及原lanes。历史accepted prefix仍只作为原开放前缀；actual63 warm未继承完整native/fullDN接受；actual91 artifact仍只是原失败73的完整初猜。

原固定输入commit8bd267107cc8710d371f3b62c02986655ac965b0及六输入完整path/blob/bytes/SHA保在冻结request。原Public78按原helper恢复；原status字节及whole artifact身份按实际文件核，不重新序列化冒旧SHA。已经删去的221或其它run state不能由摘要续父。

NS必须是RUNNER_TEMP/visible-live128-root-words226。真实runner和reader使用：

~~~sh
python -u "$COMP/geometry_20261116_live128_root_words226_owned_run.py" prepare \
  --request "$COMP/public-live128-root-words-original-full112-FD-fullDN-request.json" \
  --request-sha256 668518481e635c4832df3a5ab8a9709585d2358546904cee0eeab0df032e2c64 \
  --namespace "$RUNNER_TEMP/visible-live128-root-words226"

python -u "$COMP/geometry_20261116_live128_root_words226_owned_run.py" run \
  --request "$COMP/public-live128-root-words-original-full112-FD-fullDN-request.json" \
  --request-sha256 668518481e635c4832df3a5ab8a9709585d2358546904cee0eeab0df032e2c64 \
  --namespace "$RUNNER_TEMP/visible-live128-root-words226"

python -u "$COMP/root_20261116_live128_root_words226_necessary.py" \
  --request "$COMP/public-live128-root-words-original-full112-FD-fullDN-request.json" \
  --request-sha256 668518481e635c4832df3a5ab8a9709585d2358546904cee0eeab0df032e2c64 \
  --namespace "$RUNNER_TEMP/visible-live128-root-words226" \
  --out "$RUNNER_TEMP/visible-live128-root-words226-necessary.json"

python -u "$COMP/geometry_20261116_live128_root_words226_owned_run.py" cleanup \
  --request "$COMP/public-live128-root-words-original-full112-FD-fullDN-request.json" \
  --request-sha256 668518481e635c4832df3a5ab8a9709585d2358546904cee0eeab0df032e2c64 \
  --namespace "$RUNNER_TEMP/visible-live128-root-words226" \
  --summary "$RUNNER_TEMP/visible-live128-root-words226-necessary.json"
~~~

原prepare恢复输入，不开科学钟；run在规则同步/首factory前建立唯一原19200秒job deadline。owner6000、replay1200、stage8000、boundary/endpoint600、audit1800、120秒收尾预留、原factor cap19200及原线程数量保。所有call按实际剩余裁定，没有新H或缓存重新开钟。

原M112/N2048、576段/577节点、224全方向、226局部状态、两mean和338×112输出保；native32×10/tol2e-9、root30×20、outer8、prefix17trial、全部FD两组各10方向/3步长/2Richardson/原适用收缩、RMS1e-6、BC1e-11、FD5e-5、final fresh J/audit不变。

## 6. 真正编译安装与来源记录

same-call owner实际构造原engineering scope，得到owner_scope后才调用install_root_finite_words。它要求source-views.json当前226/R536/run/complete，且generated中本owner的实际identity一致。随后读取唯一路径R535/source-binding.json，核整个body与source child实际返回相等，加载完整固定SHA的R535 adapter，最后在同owner_scope调用install_owner_compiler。

三个记录位于call/owner-call-procedure.json：

- root_finite_word_cache_source_preparation：完整source-views.json descriptor；
- root_finite_word_cache_source_binding：actual_file descriptor与整个actual_binding；
- root_finite_word_cache_compiler_installation：R535真实安装函数完整返回。

初始值明确null，按真实阶段更新；失败时不造后继record。原owner_scope.main随后真正调用已安装compile_owner，沿原g++ flags、原process group、原编译时限和原remaining clock。实际compiler output写在owner/summary.json的compilation.root_finite_word_cache_compilation_source_binding中；compiler_completed=true只在真正原g++0且executable存在时形成。

原actual_cpp_source 7789仍是persistent CPP，其include链已由明确R535 source替换。新included_primal_source/included_trace_source_view与原ancestors分列，旧frozen_R283_numerical_prefix_is_byte_identical和only_frozen_trace_standalone_main_excluded诚实false。install的actual_compile_not_yet_called=true不被reader提升成编译成功。

## 7. 五原物理source的实际输入目录

current_call真实创建call/physical-source-inputs，包含以下原字节：ac2f core、2b96 physical jets、36e4 metric、b12f cusp、206d numerical slope。原源来自实际Public78 topic/source-root及真正HERE，完整digest和实际原路径在source plan中给定。

每件先核原SHA，独占写副本并复核bytes/SHA。完整或partial记录在call/physical-source-input-binding.json；ctx.record.actual_physical_source_input_binding记录其真实descriptor。sourceReceipts使用真实五件相对basename，runPipeline最后fields将original_source_root设为实际副本目录，原pipeline/owner/物理binder因此一致。

该修复没有修改原packet数值生成体或缩减整条session/source closure。新的binding文字/SHA如实保；失败复制不等于数学拒绝，副本complete不等于owner/compile/packet/fullDN成功。reader固定同call路径完整选择这份小manifest，不以五件计数替代实际源身份。

## 8. Science必要、报告与清理

真正science frame为BEGIN_REQUEST226_ROOT_WORDS_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY及对应END。单份ASCII JSON连同实际末LF的完整字节身份由marker/step outputs记录，body全≤90000B。overflow仍70，raw保到原正确清理或runner销毁，不分段/通用编码传输。

所有旧选择保持：实际call、H/trial/owner/stage/endpoint/audit、FD/fullDN、rules和stderr。新增完整RootStats、18cache字段/full last、原真实compiler和source安装、五源manifest按附录的具名表表达；全表头/索引/值都计入同90K。不保证新信息在所有运行里必能装下。

workflow中source必要直接使用generator实际输出；science必要先运行真实reader，再对真实文件核request/schema/run/SHA后转发同一body。report分别核单份source/science bytes/SHA及真正run/source，不能用一个scope补另一个或以job颜色当科学结论。若science文件缺失或后续运输验证失败，会把该step此前的necessary_readback_complete显式置false。

cleanup仍需两份必要scope完整、实际当前request/run/source ownership和重新观察的owned namespace quiet。科学partial已完整读回并满足原条件时仍可清理其自有raw；未完整读回、超限70、未知owner或quiet未证时保留。source metadata与必要文件在科学namespace外，不由原science cleanup冒额外权限删除。

## 9. 正式注册、唯一dispatch与未付

workflow文件visible-larger-public-live128-root-words-original-full112.yml只有workflow_dispatch，没有push触发，防止发布与显式派发重复启动。主控真实发布后对main只做一次官方POST；官方返回run和head后另记绑定。预留R537是本次226实际结果，不能借225、227或229来源补其字段。

原当前模型仍全部128后置；本请求没有R534 projected64、R531 workers或连续C的另一族。将来组合必须新来源/新请求，不能悄改本运行文件继续用本SHA。

全部源与条件证明完成即可发布/执行，不另加独审、数值fixture、benchmark或短跑前门。真实成本、原6000完成、完整后置/FD/fullDN接受、90K容量及课题的闭场/全域比例/精化目标都仍由实际结果承担。

## 附录：实际reader的完整选择及具名逆

下列选择/表示正文来自amplitude的完整reader子件，并已真实并入本节最终52189B/e90e3abd2e40ebd469bcd8d4dd7f221848c9926c91b86c8e2ee29235b1be864a reader。其原过渡52199B/18e3853d不是本次实际执行身份；当前226名称/pins/schema/frame已全部级联。本附录的逻辑与字段原字保留，标题只改为附录编号。

### A2. 实际选择接点

原Reader.evaluation没有root_statistics。本次在原complete/budget/stages/norm/failed_stages等选择之后，仅在原字典确有该成员时，加入**完整root_statistics**。不以新cache对象替换其它原RootStats字段。

现成owner_record已经逐原evaluation/current/final键调用该选择器。因此原initial、trial、iteration、final、error等行保原位置并返回真实RootStats。原owner_final的重复副本保持原选择，只对相等的统计对象共享正文。

原summary.owner_records以外：

- 对现有journal fallback中未属于原selected事件集合、但实际evaluation/current/final包含root_statistics的行，增加additional_root_evaluation_records；original_record_index指该实际records序列，不能称为未记录的物理log行号。
- 对原independent_fresh_replay.records，增加实际携带RootStats的evaluation记录及原序号；不据replay.complete虚构统计。
- 若records成员存在但并非list，保original_records_member原值；缺失成员与null不混淆。

原journal仍仅取persistent128_raw_owner_record这条原观察事件，避免把其它转发事件冒新求值。原失败地址、缺失、read error和日志身份继续由现成Reader处理。

### A3. 完整18计数与last

完整root_statistics.root_finite_word_cache对象按原键值保留，**不限于18个已知计数**。当前R535 header声明的18项为：

~~~text
fixed_requests
fixed_builds_started
fixed_builds_completed
fixed_qualified_builds
fixed_nonfinite_mode_fallbacks
fixed_nonfinite_angular_fallbacks
fixed_mode_pairs_formed
fixed_angular_pairs_formed
fixed_evaluations_used
fixed_evaluations_fallback
fixed_evaluations_without_local_cache
u_builds_started
u_builds_completed
u_qualified_builds
u_nonfinite_mode_fallbacks
u_mode_words_formed
u_angular_rows_used
u_angular_rows_fallback
~~~

原schema、last_present、完整last（phase、mode_zero_based、angle_zero_based、两项used标志）、counter_scope、last_merge_order及其它实际成员全部保留。缺成员不补零，last_present=false/last=null按原字保留；读取不要求计数为正，不把qualification、builds_completed或last位置当完整角域/全部stage或native接受。

本文依据已读取R535 header7102/6706eae6、adapter10892/1c99623e、完整plan10232/f3b7900f以及原767a4c4b persistent owner。R535中U计数可在原D/S/A检查前增加，last按原stage合并次序决定，不能把它解释成全进程最后墙钟事件。

### A4. 实际准备、安装与编译各自来源

每个真实call另读同目录owner-call-procedure.json，保文件存在/完整bytes/SHA/读取错误和选定过程身份、call/run/source/PID、返回、resource/error/traceback字段。三个明确新增成员按**实际存在性**读取：

| 原成员 | 实际范围 |
|---|---|
| root_finite_word_cache_source_preparation | 当前source-views.json完整descriptor |
| root_finite_word_cache_source_binding | actual_file descriptor与完整actual_binding |
| root_finite_word_cache_compiler_installation | 原install_owner_compiler完整返回 |

这三项初始null会保持null；不存在时输出中仍不存在，不制造空dict或默认false。保两项真实新过程旗original_persistent_main_solve_replay_source_unchanged、root_primal_uses_declared_R535_finite_word_source；不保留一个未经实际源支持的“原root数值体全字未改”声明。

owner/summary.json若有compilation，返回其**完整原对象**，包含root_finite_word_cache_compilation_source_binding的真实完整值。R535原adapter只在实际g++返回0且executable存在后形成compiler_completed=true记录；reader不从prepare或installation推这一步，不从无compilation成员推数学失败。

编译未返时仍能读到owner-call-procedure的source/installation阶段和实际错误，原stderr完整选择也不减。reader没有从source-binding里的compiler_completed=false改写成true，没有从compiler输出存在推root曾完成。

### A5. 物理源码实际复制记录

current_call的actual_physical_source_input_binding descriptor作为原call-result中的明确新增成员保留。同时固定读取同call/physical-source-input-binding.json，并完整保留其原JSON值和文件identity。

当前schema R536-actual-current-physical-source-input-view-v1及source/call_number/actual_directory/original source root/topic、complete、五个sources的原顺序和每个original/actual descriptor、original_files_modified、source_bytes_executed_as_new_science等都保留；若有partial/error或其它实际成员同样保留，不截5项为计数。

文件不存在与JSON null通过actual_file.present区分；解析失败进入原metadata_read_errors。复制complete不推出owner启动、compile通过、packet数值完成或任何科学接受。此读取没有重做复制，也未改五份原源码或完整数值packet。

### A6. 八种固定具名表示及上下文

全body末尾新增R536_root_finite_word_cache_metadata，schema R536-complete-root-word-and-source-records-v1。仅以下八类字典可被具名引用；没有扫描/编码任意科学对象树。

| catalogue | 唯一reference key | 实际上下文 |
|---|---|---|
| root_statistics | R536_root_statistics_ref | 上述实际evaluation/current/final中的root_statistics |
| root_finite_word_cache | R536_root_finite_word_cache_ref | root_statistics的同名原成员 |
| owner_compilation | R536_owner_compilation_ref | actual_calls[*].owner.compilation |
| root_cache_compile_binding | R536_root_cache_compile_binding_ref | 上行对象中的root_finite_word_cache_compilation_source_binding |
| root_finite_word_cache_source_preparation | R536_root_cache_preparation_ref | actual owner-call-procedure对应字段 |
| root_finite_word_cache_source_binding | R536_root_cache_source_binding_ref | actual owner-call-procedure对应字段 |
| root_finite_word_cache_compiler_installation | R536_root_cache_installation_ref | actual owner-call-procedure对应字段 |
| physical_source_input_binding | R536_physical_source_input_binding_ref | actual_calls[*].physical_source_input_binding.original_value |

共享须对**完整原对象**核同一类型、全部键、逐数组顺序与每个完整值；不是选几个计数或仅SHA相等。bool/int/float区分，有限字值不舍入，±0区分，NaN不共享。源码JSON无IEEE NaN payload，仍沿旧safe_selected的非有限标量展示责任，不冒payload等价。

非dict值保持原literal，不进入引用表。因而缺失、null、空dict、空list、false各有原含义。原文件全文identity保实际serialization；具名对象共享不声称JSON字典成员写入顺序逐字相同。

### A7. 精确逆与可逆性

对每个catalogue：

1. 建立长度record_count的列表。
2. 对每group中的第k个original_record_indices值i，建立恰有columns这些键的字典。
3. 第j列若含constant，取该完整值；否则取original_values[k]。置于列表第i项。所有原row index保留，因此组间顺序不丢。
4. 在上节明确上下文中，将单键reference对象换成对应catalogue[index]。
5. root_statistics展开后，仅再展开其原root_finite_word_cache成员；owner_compilation展开后，仅再展开其原root_finite_word_cache_compilation_source_binding成员。其余四类直接展开完整原源记录，不递归解释任意其它字典。

列常量只在这一列所有完整值严格相等时共享；不同key-set归不同group，所以缺键永不变为null。数组原值不排序、不做值差或数字编码。完整相等对象的重复引用展开后，在每个原上下文还原同一完整parsed-JSON字典；不相等对象各有独立index。这逐项证明新增必要表示保全原已选元数据。

本逆只还原新字段的选定metadata，不声称恢复未选科学数组、未生成文件或被原selector省略的其它量。新表头、索引、全值和完整来源都在同一正文计入90K。


