# Request126：实际125九参数到最多八个原批次的临时续算

分类：公开Actions中的有界候选编排接口，不是低三共振根、非零场或native接受证书。  
作者：OpenAI ChatGPT（amplitude agent）。  
日期：2026-11-15。

## 1. 已付依据与本次边界

[实际125正式结论](../results/R284-actual125-nine-control-eight-further-acceptances.md)记录同一九控制族又完成8个方向、8个接受、17个原外试探，未加权完整三残差merit从431.4178353348037变为279.12365756925647。原unit/full112/nonzero/native/success仍为false。末方向7的alpha1虽有原normal_target_tolerance=false、第二误差−3.078167399695153e−8，仍被原完整三方程Armijo接受；本编排保留这个事实与原接受语义，不额外要求该内层标志变true。

本次从那个真实末点出发，最多启动8个独立原8方向进程。每个子进程都用原冻结family/search，重新形成当前状态、完整3×9响应，并执行自己的全部最终FD、域和圆场检查。不是把原单次方向上限改成64；不共用旧J、旧merit、旧状态或上批证书，也不以跨批merit相减决定是否继续。

每批相对信赖半径明确重置0.1，原批内半径更新保留。父125的末半径不被猜测、转抄或假称继承。最多8批及3600秒批间资源检查是显式编排预算；已启动子批不会在3600秒时被该检查截断。

## 2. 真实父来源与九个初参数

父run43698258576，source36f7152b0b32072dd938f22e67d4d861484b266a；原producer仍为824c0967…九控制入口。主控已完整读回并重构原scalar view：

| 已付原件 | 字节数 | SHA256 |
|---|---:|---|
| 原nine-control-curved-status.json | 1883163 | 688d64e20510b862636cf1259aaacfc352dfe1c3733642c1cef6b9b38e7fe9b8 |
| 原正常primary | 63133 | 53a0186f3f798749b3de535f1f421d211bdadeeceedc8d0dcca9a17f2ee4d916 |
| 原8组重构完整scalar view | 118379 | 56c7fef05b0af2563589084cfb7d8cbfbce5593f3260ad8089f188b217467ea6 |

顺序仍为[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]：

```json
[0.39396138153791915,0.2289775739245636,0.4799638646417009,-0.042583884935461724,-0.028628164749511718,0.6613896829495851,0.2816195291196621,0.22690410400034677,0.06857724943199425]
```

本次首recipe只有原五字段schema/origin/literal_parameters/input_sha256/family，origin使用上述实际status与primary的完整身份。首批只读取这份小recipe；不重新下载父大status或借用其数值模型。初始参数与来源来自主控已核真实读回，编排自身不声称独立重读了外部父payload。

后续批次不同：它们的前一批完整status、primary及原trace文件就在同一runner临时目录，编排和冻结reader会实际读到原字节后才生成下一recipe。下一recipe的run/source取当时真实GITHUB_RUN_ID/GITHUB_SHA，producer仍指原824c九控制科学入口，不伪标为wrapper。每次保留全部九个final.parameters字面值及其binary64 word一致性；三个eta不会被置零。

## 3. 五件正式文本

computations与notes路径均相对topics/visible-flex-larger-amplitude；workflow路径相对仓库根。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| computations/geometry_20261115_nine_control_temporary_batches.py | 43812 | b15a6571a1ebc5dc72f1037212fd86a10d7a5848957c2faca4ae9e7fd69f21bb |
| computations/actual125-explicit-nine-control-batch-parameter-recipe.json | 2289 | 4dd8745b635feaad260188dba50d008a98033951fe8201ab731064b5473975db |
| computations/public-nine-control-batch-request.json | 41012 | 7825a4724f9efec18291df84ab0381c1696e05fb73869a27e7da4ae9f623c826 |
| .github/workflows/visible-larger-public-nine-control-batches.yml | 18133 | f54989d2d31ca99e354898212db2774eaf8551767c17b7f470f6f831d0e29d51 |
| 本接口 | 以发布字节SHA为准 | 不在自身正文写自引用SHA |

新wrapper是独立stdlib编排文件，基线为已执行121的geometry_20261115_six_control_temporary_batches121.py（31414B，8ac33f77b3438a4417cbd6b4840428ff25706911464d7ae0a530b82501c674bd）。旧119/121/123/125源均不改。

原83科学源映射全部保留，只增加新wrapper，合计84；两项辅助源仍是原rules runner与原f57 reader。当前科学producer及初始父producer的26项消费闭包相同，wrapper另有独立source身份，不把自己插入原科学producer账本。

| 不变的核心源 | SHA256 |
|---|---|
| geometry_20261115_small_core_nine_control_family.py | 086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629 |
| geometry_20261115_small_core_nine_control_curved_recipe.py | 824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf |
| root_20261115_small_core_nine_control_curved_scalar_readout.py | f57a7dfae95f3e629aa412003e10ea4e32a9821b754c3d575318f97b09b7317d |
| root_20261114_current576_rules_runner.py | 3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde |

wrapper本体不写死125或未来run/参数，因此同源后续使用必须由新的真实请求明确提供首recipe；本次126请求则完整绑定实际125，没有未来结果。

## 4. 每批调用与原停止语义

原科学schema是R259-nine-control-full-three-two-normal-curved-trust-recipe-v1。原recipe schema仍是R259-explicit-nine-control-raw-quadratic-shape-recipe-v1。原搜索自己检查family定义、当前同源origin和全部输入；编排不执行模型import或数学动作。

每批原科学CLI保initial-relative-radius0.1、candidate-steps8、backtracks20、normal-iterations12、normal-backtracks20、normal-target-tolerance1e-8、candidate-resonance-tolerance1e-8、interval-bits160及interval-depth14。699节点、112场/尾、2048/4096角和全部三个unit方程、完整12×9方向QR、二法向/七切向、原0.2Armijo都不改变。

原original_stop函数正文逐字沿121，仅由新常量绑定九控制reader。下列原因停止链：

- 原外部资源或规则信号、child非零退出、原异常或未完成；
- 原reader的进程、协议或完整schema没有完成；
- 原unit停止旗标true，或原full112候选旗标true；
- 原接受点数为零；
- 原停止原因不是明确的8方向预算结束，或原记录方向数不是8；
- 最多8批完成，或批间3600秒资源预算已到。

本编排不另检查下降幅度、奇异值、数值rank、normal误差或独立FD阈值作为续算条件。所有最终FD/域/圆检查均由每个原child实际执行并原样读回；是否停止仍按上述既有算法语义，不能据“又跑满8批”推出共振根、非零场或native接受。

原zero_added_quadratic_reduction仍作同前六参数的零eta反事实参考比较，不覆盖真实非零eta。其比较范围是原evaluate保存数组，不是独立旧六族J。原辅助求值如抛异常仍可能结束准备阶段；125已经实际成功不构成未来全部参考点有效的保证。没有修改这一冻结程序行为或添加新科学门。

## 5. 同runner真实状态链

每批目录为batch-NNN/science，incoming recipe位于独立recipes目录。每次科学进程退出后按顺序：

1. 保原stdout/stderr的临时原字节和SHA；它们不是新的科学producer。
2. 用该批独有GITHUB_OUTPUT文件调用冻结f57 reader。reader的每个stdout字节同步tee到原compute日志和本批临时reader.stdout。
3. 核原reader输出协议、UTF-8字节/SHA与实际run/source；将完整primary单独打印。
4. 完整读取该批原status，核当前26源、四输入、原family、incoming recipe、fresh initial参数及原trace字节。
5. 只有真正已完成原status及正常分段读回才产生after-batch-NNN.json；它只载真实原final.parameters、原status/primary字节身份及同一family/input身份。
6. 先保存与打印短restart recipe及批次元数据，再删除已消费的该批临时raw。下个child只消费短recipe，不能打开上批模型或场文件。

f57在primary过大时可以把final搬到具名完整段。新wrapper因此不硬索引summary.final：final若inline则与原status的参数逐word比对；若搬出，则核该具名完整段记录，下一参数仍直接取已经完整读过的原status。primary始终保留原status身份，因此不会把别的批次输出误认作本批结果。原完整方向段和primary绑定同一原status SHA。

原status尚未读完、reader协议失败或中断时不生成可续的假recipe。记录保留原child返回码与独立读回异常，不能把工程问题改称数学失败。所有后续recipe都由同run实际原件产生，不使用旧文件计时/压缩元数据冒逐字重演。

## 6. 每批完整日志与紧凑链索引

每批reader的原stdout有外框：

```text
BEGIN_VISIBLE_NINE_BATCH_001_ORIGINAL_READER_STDOUT
…冻结f57的原BEGIN/END方向段、原段JSON与原SHA事件…
END_VISIBLE_NINE_BATCH_001_ORIGINAL_READER_STDOUT
```

这些内容按原字节流传递，不重新编码任何方向段；即使reader后来失败，已输出的完整或部分段仍留在原日志。每批另有BEGIN_VISIBLE_NINE_BATCH_001_PRIMARY及完整原primary正文、字节数/SHA。batch编号只在外框和wrapper事件中添加，不修改原f57的run/source、segment schema或JSON值。

因此八批内相同的原outer-000等段标签，以批次外框及原status SHA区分。原primary保存每个组的canonical value身份、segment index身份和重构说明；原17列trial_rows及全部原外trial不被wrapper截断。原reader对inner原始详细记录的既有范围也不扩大为“全部raw已公开”。

chain-metadata.json可以在临时目录保完整编排元数据，不把其增长变成新的每批科学门。--report-only只取固定列的紧凑batch_index_rows：原status/primary/view/stdout身份、原停止原因、方向/接受数、两端原merit、原旗标、九参数、半径和下一recipe等。它不拼接八份primary，也不复制八组完整FD或source大树。

report通过chain_summary/chain_summary_bytes/chain_summary_sha256三项GITHUB_OUTPUT传一次紧凑索引。独立report job核字节后打印BEGIN_VISIBLE126_CHAIN_SUMMARY。若索引意外超90KB，返回明示compact_chain_transport_complete=false的小错误索引和真实已知结果指针，不能冒完整成功；各批完整primary与方向段已经在compute日志，不会因report大小丢掉。

## 7. 运行与临时输入责任

新唯一push trigger为：

```text
topics/visible-flex-larger-amplitude/computations/public-nine-control-batch-request.json
```

concurrency独立为visible-larger-public-nine-control-batches，cancel-in-progress:false；未设置额外手动dispatch或旧125触发。当前交付没有实际126 runID或结果预报。

原四数学输入按相同历史8bd267107cc8710d371f3b62c02986655ac965b0在本次RUNNER_TEMP恢复。新wrapper的--original-input-paths只接这四个真实临时路径，逐size/SHA核对；不要求104清理后的main原数据路径重新存在。原78源码缓存也在本次独立RUNNER_TEMP位置。

核心wrapper CLI为：

```text
python geometry_20261115_nine_control_temporary_batches.py
  --request <当前public-nine-control-batch-request.json>
  --request-sha256 <当前真实请求SHA>
  --repository-directory <固定science checkout>
  --original-input-paths <本次original-input-paths.json>
  --rules-directory <本次rule-sync>
  --out <本次nine-control-temporary-batches>
```

它仍运行在原rules runner进程组；没有新session、没有另加child timeout。孩子环境移除独立GITHUB_OUTPUT、Git/token字段，reader只获得自己独有临时GITHUB_OUTPUT；metadata rules runner保持原同步权限。原2700秒真实pull/rebase/README差异停止机制不变。

Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0及单线程保持。整链3600秒仅批间检查，science step75分钟、compute90分钟、report10分钟与既有119范围一致。外部截止可以产生partial；不能把没完成的方向、FD、域或圆检查写成已付。

workflow在always紧凑链报告之后才清理本请求临时wrapper目录、原输入和源码缓存。各完成批早已在读回后删除；失败批若尚留临时raw，也只在整个科学step结束并形成always报告后清除。没有artifact、Release或main raw归档，清理成功不代表任何科学接受。

## 8. 与121/125的可直接审读差异

wrapper相对实际121的8ac33f77…独立新增，主要变化为九维身份与own26闭包、外置真实初始recipe、RUNNER_TEMP四输入映射、f57 stdout逐字tee、primary具名字段搬移兼容，以及紧凑列式chain report。原停止判断正文逐字不变，原status读取只把消费源计数24改26；原参数word身份方法和原GITHUB_OUTPUT三项协议解析保留。

request/workflow相对实际125的31bd2312…与1dfa0c45…给出完整diff。原83源、两辅助源、四输入、运行版本和每批数值参数完全同；只新增wrapper pin、实际125父recipe、批次预算/输出协议和唯一触发。原科学family/search/reader没有任何diff。

本地环境当前不可用。本次完成的是纯JavaScript文本变换、JSON/UTF-8 SHA与来源一致性检查，没有声称重新执行Python/Bash AST，也未导入数值模型、构造科学fixture或运行科学。workflow仍在公开Actions依原preflight逐source字节及AST核对；这不是额外数学接受门。交付只create_blob，没有tree、commit、ref更新或dispatch。实际126如何接受、拒绝或中止，只能由其真实输出给出。
