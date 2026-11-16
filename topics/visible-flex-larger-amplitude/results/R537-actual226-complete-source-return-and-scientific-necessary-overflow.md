# R537 — actual226完整来源返回与科学必要正文超限

作者：ChatGPT /root（AI）  
日期：2026-11-16  
状态：本次实际运行的完整可见结论；没有新增完整非零112场或可续算科学父。

## 537.1 实际结论

request226实际run **43863878883**，source **f93b079e400c336f12751728ba388d6a9e769779**，attempt1。compute **133287356711** failure、report **133353210426** success、整run failure。root在两job自然终态后各唯一读取一次日志，未读running科学日志。report success仅是回执运输成功。

来源必要正文含末LF共 **56393 bytes / 6123bc795d6558f4a67f82fdcda547145509639dca8f2465d8522f9c92c4ac5d**，完整返回，确认 **361=345 public+3 paired-generated+2 root-word-generated+11 caller-generated** 源准备完成。

科学reader形成的whole为 **109972 bytes / 74163314c33497b0e25f46a5e542eebc76ed0b9e08a2eb6625f5b76c602b1269**，超过原90000上限，**whole正文未返回**。实际返回 **1079 bytes / 33a0f4907b894bc3d56683d6dff1c5218fe6523a7dae9ceabab5fc9bd588279e** 小对象，明确transport_exit_code=70、necessary_readback_complete=false、cleanup_permitted=false。两job都是这一相同小对象，不能由report成功倒推科学接受。

compute另有独立可见事件：actual_exit_code=1、rules_returncode=1、science_returncode=1、resource_stop=null、external_signal=null、owned_processes_quiescent=true。cleanup明确removed=false，临时namespace因原科学必要域不完整留到runner销毁。

故本次原128迭代、root实际统计、norm/mean、FD/fullDN/末审计数值和内层失败原因都没有从科学whole返回。不能从SHA、code1、持续时长或R528/actual225的数值代填；transport70不等于数学拒绝、6000预算停止、tol失败、词不等或算法加速。

## 537.2 实际入口与复现资料

event=workflow_dispatch，created_at/run_started_at均2026-11-16T12:08:36Z，updated_at=14:10:11Z。元数据墙钟不是内层科学elapsed，不能作性能比较。

[实际run及两job](https://github.com/Rogerhu12/math-research-public/actions/runs/43863878883)；[固定source原workflow](https://github.com/Rogerhu12/math-research-public/blob/f93b079e400c336f12751728ba388d6a9e769779/.github/workflows/visible-larger-public-live128-root-words-original-full112.yml)。用此固定source的完整workflow、request、plan和生成器重做原运行；旧临时数据没有成为续算父。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `root_20261116_live128_root_words226_source_views.py` | 30464 | `14a86c71268ccd017c6e85294c7af9b714c2234063c2ef1953caf35458bd6052` |
| `r536-live128-root-words226-complete-source-plan.json` | 62193 | `772e3da8b00d692672802b0e61f0e038b08b0014b03ad7e136f9cb312412ba69` |
| `public-live128-root-words-original-full112-FD-fullDN-request.json` | 71828 | `668518481e635c4832df3a5ab8a9709585d2358546904cee0eeab0df032e2c64` |
| `public-live128-scoped-original-full112-FD-fullDN-request.json` | 54884 | `0fa9fe29153913252fd569cb2b99711c85b0afe72d8bc576adf629bd3e3f789e` |
| `public-live128-paired-cache-original-full112-FD-fullDN-request.json` | 64734 | `42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285` |

R536原合同保M112/N2048、699×453、3active+109core、338×112、双mean、全H/J/R273、原128值/tol/replay、FD/RMS/域/BC/merit、fullDN与末fresh J+audit。226没有后来R534完整近似投影模型，也没有R550/R561/R564/R572执行变更。后继算术证明或运行不得倒记本次。

原总19200秒及owner6000/replay1200/stage8000/boundary600/endpoint600/audit1800/readback120各责任按原合同；本次独立事件没有完整阶段elapsed，不推断哪个cap导致code1。预算和门的声明保持，不等于此次已实际支付。

## 537.3 来源准备的完整返回范围

主source-views.json为 **150675/4369c7734d2091308e8fed2daabb7c6426218fc73b828b720ccbec08868e22e6**，留在原job临时目录。56393必要对象完整覆盖规定的来源必要域，不等于150675原文件全文已返回。

该对象phase=source-prepared、complete/source_preparation_complete/necessary_readback_complete=true；error/actual_error=null，not_generated=[]，complete_original_source_stderr=[]，original_public_files_modified=false。verified_public_source_count=345，完整public file receipts仍保在绑定的临时preparation，不能把这句话说成345份源码全文被运输。

compiler_started/scientific_clock_created/scientific_code_evaluated/scientific_module_imported/science_success_inferred均false，严格限定**准备时点**。后续science step已运行并code1，不能由准备时false推整run从未编译或停在owner以前。绑定事件另明确Python compiled-not-imported、Node syntax-checked-not-executed，均公开Actions发生；其no_CXX_scientific_compilation_or_scientific_evaluation_yet同样是当时限定。

R522子actual_exit0、started/returned=true、scientific_child=false、starts_new_session=false，19项原public inputs保。其source-views.json **15817/0b2bb1fdf2a1cf84d552c325dbd4df31ce5018b73b40523a00e58692086e4526**；stdout **15898/70dadaf19edd1b73df2f4957730b6a3479f5aee08bee81ce59ba07f89577fb07**；stderr零字节/SHA **e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855**。selected source result complete/transport_complete=true、error=null/not_generated=[]，科学import/compile/execute=false，无新clock/cap。

R535子actual_exit0、started/returned=true、scientific_child=false、starts_new_session=false；source-binding.json **2098/77c580903972981cab7bf0f500f8442ce5512aa8eeaae2ed877bd2e9f291643b**，stdout **2122/100527889480d2cd853487d80405972a3f07d39bd9d03b781ea426881381afef**，stderr同空SHA。primal9/trace4字面替换完整逆变换保原文，source_preparation_complete=true/compiler_completed=false。只代表source-only子完成，不能推真正科学编译/命中统计。

其完整实际原source/header/adapter身份如下，均为来源证据：

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261115_native_primal128.cpp` | 23890 | `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d` |
| `geometry_20261115_native_trace_variation128.cpp` | 34622 | `8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d` |
| `geometry_20261115_native_persistent128.py` | 43371 | `767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322` |
| `geometry_20261115_native_persistent128.cpp` | 22364 | `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd` |
| `root_20261116_native_root_finite_words.hpp` | 7102 | `6706eae670bf5746eb42d194bd456d290c290d451ddc52d80359d0263f90e7cc` |
| `root_20261116_native_root_finite_words.py` | 10892 | `1c99623e2cd63d0a4700011c96e5054645cf7dd8ee5cf3357f0c77d1727026db` |

## 537.4 全部16项实际生成来源

每项取完整必要域的actual，不是只列计划expected。前三paired和两root-word项保旧输出字节；另11是真caller。全部literal old/new全文/顺序/count/逆变换在固定62193字节plan，必要正文也保R518/R527中间身份及替换摘要。本表不缩减原完整源码证明责任，不复制生成源为新数据归档。

| 角色 | 实际文件 | bytes | SHA-256 |
|---|---|---:|---|
| R522/operator | `geometry_20261116_native_paired_digit_operator_trace128.hpp` | 29617 | `082d5a1fdd900071fb1cc008304c5a4c97bce92b173851bda1514ec1682eb7be` |
| R522/stage | `geometry_20261116_native_paired_digit_stage128.cpp` | 12880 | `49a7e226eadc7748d5d2b3f94119c2e4dd7024348e6878c673e73b1a33db3b55` |
| R522/component | `geometry_20261116_live128_paired_digit_final_components.py` | 33416 | `93ecdd833922f833bdb50a8f264bc5db1913f5ce16dbb0cb4f7fbc7d285070f1` |
| R535/primal | `root_20261116_native_root_finite_words_primal128.cpp` | 25230 | `3e1cb0a416418fe56fbee889df5debdfc9ed097b797a1b8e086b563ce4fd9241` |
| R535/trace | `root_20261116_native_root_finite_words_trace128.cpp` | 34950 | `2e122e0ca6ad21e1c11ab711cc5af40a6955d3ff054f6cd445dbd885fbb98b12` |
| owner | `geometry_20261116_live128_root_words226_same_call_owner.py` | 21969 | `934e92b1d381e5c268346556327fb76147c20e73bb9b4b9ddb6ca91aad7ab3fb` |
| assembly | `geometry_20261116_live128_root_words226_response_assembly.py` | 28611 | `1a67a3fe236b97fca188a9fea454b863855bb3b63260a3d75bff9e272176d620` |
| system | `exact_20261116_live128_root_words226_current576_system.py` | 29003 | `a147c07d859db9207da385f582706fe908d9264aacffbc51b1b62bf6064e4151` |
| qr | `exact_20261116_live128_root_words226_current576_chain_qr.py` | 21844 | `54ffe440189fdc645e3c6aa8ffab8e6abb6c4e704b97479742bf88e4760137d5` |
| pipeline | `geometry_20261116_live128_root_words226_call_pipeline.py` | 19340 | `cab766daf5549d957454c14ca0365817fdf287a25a01944d597a19c6a4e42318` |
| call | `geometry_20261116_live128_root_words226_current_call.mjs` | 36879 | `aa05fa425b41382b0177772c21b8134040925fdca323e3aa35ab3473c414055c` |
| worker | `geometry_20261116_live128_root_words226_worker.mjs` | 8181 | `39f54dec2d7ff23d28a343296a5b5bfa33085d3ccbf3f96b1545b7cbe08de8f8` |
| client | `geometry_20261116_live128_root_words226_tail_client.py` | 32599 | `dfb8fcf39a118020fc59ea9febc0d2be6bb0d85edd82ac98bf6d8fe645357fa4` |
| fulldn | `geometry_20261116_live128_root_words226_original_full_dn.py` | 37692 | `97bb244447ef809ed17cf73fe3dde75c440630e9d9441c3b188a73f7d7cd32bc` |
| runner | `geometry_20261116_live128_root_words226_owned_run.py` | 38985 | `8801c39604dfa6c7a6087886fffb3aefefdcf9f1a0c51152acbb6ff93793a0fd` |
| reader | `root_20261116_live128_root_words226_necessary.py` | 52189 | `e90e3abd2e40ebd469bcd8d4dd7f221848c9926c91b86c8e2ee29235b1be864a` |

被完整绑定的旧元数据如下；原内容和所有原输入/资源对象不改。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `r515-physical128-radial-mode-cache-source-plan.json` | 8662 | `5950052fac0d9c23e96f29421c03df79f4748828b2d7a6e9a4ed7f40bd090666` |
| `r518-live128-cached-radial-complete-source-plan.json` | 48391 | `4f2097053bddff0bf07a18f09ffa846bd64eb2fa6dd3d9707ab7f24f3ef62f6b` |
| `r522-native128-paired-digit-source-plan.json` | 16347 | `724e46e0d70aefd70309e03d77d4719666058e56001c7a78f7544bada76b9ce7` |
| `r527-live128-paired-cache225-complete-source-plan.json` | 55391 | `6e8109e64bafb6e78428298ccc25a5b4d71df29c0b224b0ea20076da006dd1c6` |
| `R535-native-root-finite-words-complete-source-plan.json` | 10232 | `f3b7900f0e670441404c707dce2144241ee9b72581c5999dd8ce95b91764607b` |
| `public-live128-paired-cache-original-full112-FD-fullDN-request.json` | 64734 | `42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285` |

## 537.5 容量和输入恢复事件

capacity before/after相同：total154993672192、used62955745280、free92021149696字节；minimum_free_bytes_at_start68719476736。unused_ephemeral_runner_SDKs_removed=[]、scientific_payload_deleted=false、maximum_uncached_protocol_calls18、all_possible_calls_fit_not_proved=true、original320_minute_clock_not_started_yet=true。它是当时磁盘容量/未证fit，不是RSS或全科学会完成的证明。

preparation_return phase=complete、complete=true/error=null；preparation.json **69699/805d9d5c757b2bee2673d951e6cbe20b3b542f0ed80c702924d37948868ed87e**。descriptor不是全部输入数组，不能推后续门已过。

## 537.6 科学返回与溢出

独立science-return code1/1/1、resource_stop/external null、owned quiet true；execution.json **2460/4455e1ff040e665e87844cf5b1bd17dac03d6d956bc25f4abdf66e7cc6a42349**。当前没有execution全文，不补命令/错误/elapsed。

随后原reader选完整科学与错误必要域形成109972字节。90K上限未变，返回70的小对象保whole路径/bytes/SHA、request身份、run四键、scientific_success_not_inferred=true、no_segments_or_encoded_scientific_tree_returned=true、cleanup_permitted=false和necessary_readback_complete=false；unreturned_scope明确完整选定域超限，没有以成功视图替换科学与错误内容。

原whole临时定位为 /home/runner/work/_temp/visible-live128-root-words226/necessary-summary-overflow.json。它不是持久artifact；109972/SHA不能重建正文。没有分块/编码取回，没有存raw Git blob/Artifact/Release，没有提高上限。report重放小对象，两个相同运输对象不扩大语义覆盖。

文件有末LF，日志单行无末LF。完整身份如下，不能混用：

| 对象 | 含LF文件bytes / SHA-256 | 无LF单行bytes / SHA-256 |
|---|---|---|
| 来源必要 | 56393 / 6123bc795d6558f4a67f82fdcda547145509639dca8f2465d8522f9c92c4ac5d | 56392 / 2016b2a2ac6c3410efc502e99eae66014af2622c727ed5f8edcb2d8b2428a3d7 |
| 科学溢出回执 | 1079 / 33a0f4907b894bc3d56683d6dff1c5218fe6523a7dae9ceabab5fc9bd588279e | 1078 / 91228e3bf8d4939ca6ae1c11ae781d25ba3029a799c8dadd7481d73728ce40be |

两job的这两对象逐字相同，只在既有缓存核JSON和字节身份，没有再取终态日志。日志来源标识为compute **122489/2289e02658b1431a0d754db5e8b453bd4a962b4cf6eb9af182aab9a00cd5390c**，report **181218/9e07e54d604971323edeeb42ecadfd8c4a01f41cc05f2036e91294c2eac348ba**。原大日志不整篇嵌入对话/正文，不复制Git，不作科学数据分块运输；只提取各自<90K的原必要正文与小事件。

## 537.7 完整未返回责任

以下全都未从科学whole返出，不用其他run补齐：

- 当前H/十数组/全fresh J与R273值、native初值/各iterate、每root与line-search的完整residual/domain/branch。
- R535十八计数/full last/八表的实际数据；source生成成功不等于科学路径命中资格。
- 全576stage/129248行的完成数、未访地址、末向量、norm/mean/worst、各原cap实际elapsed与stop分类。
- replay开始/完成/词相等、postcomponents/FD/fullDN/final fresh J+audit的起止、值与门。未返不写成数学拒绝或未起。
- 全内层异常/stderr/域失败地址和cleanup前阶段账。独立可见quiet/null只能保它们自身的语义。

R528实际225首接受、次534/576的资源partial及具体数值不能迁移226。R535/R536条件算术与来源证明也不是本次性能测试；没有同次全值就不说R535比225快/慢或推进资源前沿。request232/236/237/240的后继修复不能回填本次。

## 537.8 quiet、cleanup与科学父

science-return确有owned_processes_quiescent=true，可以保留，但不扩成未返回的全部内层marker已经逐个返回。cleanup确有removed=false，理由为source or original-science necessary scope incomplete，namespace retained until runner destruction；其no_scientific_completion_or_quiet_inferred=true表示cleanup不新增推断，不抹掉此前science-return事件。

所以：有真实quiet事件；没有完整科学必要正文；没有主动removed=true；没有可续算接受父。runner最后销毁不等于已取得/持久保存检查点或可以从SHA恢复。

## 537.9 后继责任和完成标准

本次226合同不修改、不重派发、不事后缩小以造原结果。后继可在同job临时域完整读原选定对象，按明确source catalogue和完整可逆语义减少重复来源描述；仍须保全部原统计/异常/未访/70/false/末门，不能删科学字段过上限，更不保证必fit。已有R551/R554/R562/R565/R573分别承担自己真实入口/两reader，等待自己的实际终态，不据226overflow预填。

课题仍只有M96/N1024/scalar=.99开放前缀接受，完整非零112/338/450、同一g/固定H/整像hold/含反射E/全t闭嵌入reach/完整D/全域1e−6 metric及固定参数后实际精化均未被R537支付。记录这次完整可见失败边界后接open下一项，未到README标准不收尾。
