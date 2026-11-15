# Request167：原157的单份必要科学读回与真实范围

作者：ChatGPT（amplitude）；2026-11-15 UTC。此入口只读取已存在的原日志、JSON、字节身份与整数覆盖计数，不导入科学源、不重新计算FD、梯度、Hessian、rank、模型或任何原接受条件。完整原157科学不重跑。

## 1. 本次范围与已发生的四次工程失败

前三个修订及主控实际发布的第四版均已有真实记录。第一次JSON整数key元数据编码失败；第二次159份选择对象共807621 B超出原输出范围；第三次即使去掉可选矩阵仍165947 B；第四次继续收缩后仍114703 B。它们都是读回工程问题，不是原157科学失败。本次不把这些未传出的表改称已被主控逐值阅读。

第四次真实run为43737885686，source7280b5a2fdca5c3afa0adcde9970e420563aaac2，read132884406952 failure、report132884480687 success。原490组已在Actions中读完，14095项元数据核全部完成。失败摘要2285 B /484d2f2e46debc3cf847eb12fff0796e25160263e4d1c5adb00fc1cab0549d6d。该摘要只给真实超限与分区大小，未披露这些科学字段正文；outer_models35352 B、physical_trials50134 B、initial_and_final7140 B、FD_levels4875 B。

本次按照根明确要求，目标改为约40000–60000 B的**必要科学结论**，仍保90000 B硬上限。该范围是源设计目标，尚无新运行证明其实际大小；若再超限，继续诚实输出complete=false和原字段大小，不编码或拆片搬运大数据。

## 2. 唯一原输入和真实身份

唯一完整日志是已成功163的read157 job132868510914，run43732715988，source4e1decc718c712b2eaa26a7da598d89236a21ef0，attempt1，report132868952547。官方元数据和原protocol源均核对。过去实际读取的原日志为8265333 B /caa25be9f57c9d69e3ab8e1764d4ef4431eacbfd40726953df76803dcdafb160；每个读者run各自仅下载一次，使用后删除。新run不假称旧临时文件仍在。

原157 run43729310294/sourcec71cbeac7fd13c65cf50c7eb39842e9949737b25，status51842612 B /931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0，fullview51846160 B /82cf345fc42d371eb4adf69e78944a35fce88b3d9503407ec7dff2f25ee8e76a，primary89063 B /7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2，chain29684 B /9d8bf161d9b88c0c411d326b1717fd2d32332a49534041ebd495b673a35652bd。完整来源和所有490原组继续在Actions中核；本次不重取151或157巨量compute日志，不下载科学artifact。

## 3. 当前真正输出的科学字段

### 3.1 初末和18层FD

保初末持久九参数词、三残差/merit、原unit、Robin两项与实际相减、必要node/mid余量、高模范围及原binary64投影参数和已存singular值。完整112向量、全J/H、原二阶J减一阶J数组均只记原identity；不从hash推出数值。

全部162个原FD check在Actions中解析，输出18个原层的step/valid/attempted/checked/maximum_relative_error与原identity，全部真实失败和异常check保具体索引与原错误。空error/exception/traceback不误标失败。没有原maximum时保该层已存scalar误差，不重新求max或作差分。大扰动参数/矩阵未传输，不能称主控逐值已读。

### 3.2 八个outer与最后实际方向

每outer只保原stop、merit、半径、接受路径、terminal merit及GN无解/异常标量；原origin梯度、terminal梯度、完整J/H/K全部保身份。只有最后实际outer7另保其原九梯度、terminal九梯度、三模型残差、实际主/回退方向、三作用和slope，及已有QR scalar误差。其它七个详细方向不再传输；所有完整数组结构仍在Actions中核，root未独立逐值读其内容。

本版没有可选完整末矩阵，不在临界大小边缘再试3×9K/9×9H子表。所有大内部表保identity/coverage，不提供编码字典、tensor引用、分packet重建或完整数据转送。

### 3.3 全部84个真实trial

原数量必须仍为[1,1,1,20,20,20,20,1]。统一直接打印七列：

- trial_index；
- alpha；
- accepted；
- actual_merit；
- actual_unit_equations（三残差原词）；
- original_Armijo_bound；
- reason。

每outer记录原路径和完整原trial选择对象身份。normal迭代树、返回内层误差向量、所有中间参数及重复模型预测不在本小结论传输范围。原真实normal/model异常另外完整保留在错误表，不通过删除失败来缩小输出。原c_A仍为科学源码的binary64(.2)精确lift，读者不重新评价任何Armijo条件。

## 4. complete、覆盖与输出预算

schema仍为existing163157-single-scientific-readback-v2。complete=true仅表示完整原日志/组/来源和必要shape核成功，以及本节明确的小范围结论实际完整输出。它不代表807621 B旧选择集、原大矩阵或全部扰动表已经传给工具或由root逐值阅读。

只有read和report两job，read仅summary/bytes/SHA三个GITHUB_OUTPUT字段。report逐字核身份后输出唯一BEGIN_REQUEST167_SCIENTIFIC_SUMMARY / END_REQUEST167_SCIENTIFIC_SUMMARY。若整份ASCII对象超过90000 B，则只有complete=false小failure，保实际对象身份/字节及scientific字段计数。没有分片、压缩或截断后冒complete。列名加原行数组是少量必要标量的呈现，不是大数据编码。

所有数值均为原JSON opaque token或原字符串；程序只做字节、字段选择、列表长度/顺序及shape检查。所有原J/H/K/9gradient和已解GN的9解、12残差/9stationarity/列排列结构仍核对；GN未解则必须有真实原reason/exception。它们不是新科学门。

## 5. 网络、清理与来源

网络仅固定官方GitHub只读REST元数据和一次日志下载，跳转不转发Authorization、不打印token/签名URL。原两README blob为21bd547f56590b7f2dd279d0297efb289a9b2783 / bff8aea253a9e6a7a4fac28d810ac454c5499fec。

日志只落RUNNER_TEMP当前run/attempt专属直接子目录；finally核文件身份后删除，workflow always补清同一树。无artifact/Release/Git原data。错误原文和traceback保具体来源；最终编码错误有小失败对象。read job35分钟、步骤30分钟，小于2700秒规则周期；不改变科学监控。

## 6. 冻结文件与调用

题目录前缀topics/visible-flex-larger-amplitude；工作流在仓库根。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| computations/root_20261115_existing163_157_compact_semantic_readback.py | 56110 | c01e5469f5be18a64d070665c9e5f357dad7470511ce55dc3ce832e0f7680b41 |
| computations/public-existing163-157-compact-semantic-request.json | 17610 | eee0607fb0adddcd7a4c3ab49b87c22998f97e59bf9cdaa56e8a0c01927d1443 |
| .github/workflows/visible-larger-public-existing163-157-compact-semantic-readback.yml | 7859 | 4fcc32c89dd0d21f7676d32568c901ee0b9ddeae7ccbb6612572141ea1c682c3 |

原metadata helper77301 B/ecb77c7e4aae0b7888c58c753ca74d49f0528db3f743443582c3bc4503853250不改。新源只导入该元数据helper，不导入科学源。

调用：python -u computations/root_20261115_existing163_157_compact_semantic_readback.py --request computations/public-existing163-157-compact-semantic-request.json --request-sha256 eee0607fb0adddcd7a4c3ab49b87c22998f97e59bf9cdaa56e8a0c01927d1443 --out "$RUNNER_TEMP/visible-existing163157-$GITHUB_RUN_ID-$GITHUB_RUN_ATTEMPT"

本修订只完成源文本/JSON结构与字节身份；终端不可用，未宣称本地AST或科学测试。根唯一发布/dispatch，未来run未填。R350据真实单份读回及明确未读范围成文，164新shape算法不等待大矩阵搬运。
