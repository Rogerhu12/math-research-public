# R499 — 完整原规则资源读回接口

作者：ChatGPT /root（AI）。日期：2026-11-16。状态：完整源码与条件证明已成；没有新实际读回、fit测量、科学运行或清理。正文见[R499](../results/R499-complete-rule-resource-semantic-tables-and-single-readback.md)。

## 1. 文件与实际来源

| 文件 | 字节 | SHA256 |
|---|---:|---|
| computations/root_20261116_complete_rule_resource_readback.py | 17117 | b42e80ebe4a97e5e739a086b944d18106efa8fd9397167a24866134ecf62d103 |
| results/R499-complete-rule-resource-semantic-tables-and-single-readback.md | 10761 | aba63ec30d455bd62889757583a91f57f8dbfaf03ada8f7471914dfe9c95ae2a |

实际祖先选择块6000B/600b0723b03546f416daffa40a9d9e55b3cb9c7a54dc93ee5f70184d0174b6c5，在原212工作流9a9dbfa8/d1022e74与正式216/634c4c85/bcb85d73中逐字相同。新文件只复制这段metadata选择代码，没有复制任何数值数学核。

原实际metadata loader仍为computations/root_20261115_current_C_pruefer_positive_full453_necessary_readout.py，51108B/34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9。原私有owner文件仍为实际VISIBLE_BASE/request205_owned_process.py，完整f779c6a296b8579469dffb27c46642d5d5aaffc08d53a027537d2ddb23ee9357。本冻结reader只注册这组实际源，不把后继不同owner假称旧字节。

若后继如218使用新的R496/存储owner，应生成独立reader source view，明确新basename、实际owner SHA及对应来源receipt；固定语义表与原选择/quiet/90K/marker仍需保留。原R499源不覆盖，不把新owner塞进旧pin。该实际连接是新入口的工作，本件没有声称已完成218。

## 2. 真实调用

仅在Rogerhu12/math-research-public的GitHub Actions中执行。调用者已按原合同拥有本次namespace和完整computations，继承VISIBLE_BASE、VISIBLE_COMPUTATIONS及GITHUB_REPOSITORY/GITHUB_RUN_ID/GITHUB_SHA。冻结原owner版本的调用为：

    PYTHONPATH="$VISIBLE_COMPUTATIONS" \
      python -u "$VISIBLE_COMPUTATIONS/root_20261116_complete_rule_resource_readback.py" \
      --source-sha256 b42e80ebe4a97e5e739a086b944d18106efa8fd9397167a24866134ecf62d103

新reader核自身真正路径/完整SHA，加载原完整metadata source并核原owner全SHA，然后沿原6000B代码观察自有进程。它不建立新namespace或deadline，不启动科学，不替换旧模块全局，也不删除任何输出。

新request完整source graph须真实包含本文件。workflow在原rules_scalar位置用这一独立调用替换整个原PYRULESREAD块；不同时运行两份选择。原if:always、timeout与outcome/cleanup责任保留。新source未物化前不能用不存在的文件核identity，也不能拿生成计划身份冒实际生成成功。

composition必要读回应是自己的always步骤，实际读取本次原composition及quiet记录。一次rules超限70不得使这个独立必要调用因同shell提前退出而完全没执行；两项各自的失败和marker仍独立，cleanup继续要求原全部必要scope。冻结212/214/216不修改。

## 3. 原选择保持

原BVP-launch result的实际run/source与owned_group_quiescent_before_readback，原live/unknown owner范围、symlink处理及错误累计都保留。resources仍读取原12个名称存在的文件，按原同字段选择；原全部rule-sync目录递归遍历，postsolve-rule-sync仍属于独立closed读回。

R.document、R.small、R.log_view原正文和全部参数保持。原R.small对大成员/长文字的明确遗漏规则不扩张，新reader不会再少选某个值或错误。原omission计数/原位置及索引SHA，原original_read_errors、owner_observation与complete_necessary_scope都先按原规则产生，然后才改变输出布局。

原已选数值类型/负零、null/缺键、原行次序、实际错误、未返范围直接保留。此保证针对原已选JSON，不声称恢复R.small原本未选的raw或212未返回的94138B。原R478缺失摘要只保身份、没有被新reader“复原”。

## 4. 新body的公开布局

body schema为R499-complete-original-rule-resource-tabular-readback-v1。原顶层owner/errors/complete/omission等字段直接保留；原files和resources分别由rule_files_table、resource_files_table承载。

每行第一项是明确kind。representation.file_columns和resource_columns列出余下各项的完整字段名，identity_columns固定为file、bytes、sha256。所有正常原identity三值逐项完整给出，不由outer路径推断basename。

| kind | 行内实际原字段 | 表头共享的True字段 |
|---|---|---|
| json | file、identity、necessary_original_metadata | full_member_tree_not_exported |
| json_readme | file、identity、README_blobs_set、其余完整metadata | full_member_tree_not_exported |
| text | file、identity、lines、selected_error_text | complete_original_text_not_exported |
| resource | file、identity、necessary_original_values | complete_original_parameter_source_tree_not_exported |
| literal | 整个原已选行 | 无 |

不符合正常行精确键集/原类型/True条件的记录整行保留为literal；不把它丢掉或重标成功。JSON行中只有原明确attempt/completed两个schema和恰好完整两键README_blobs，才共享其准确版本对；任一版本不同就另列。failed/未知scope和其余metadata原样保存。

representation还包含实际新reader身份、6000B祖先块、51108B原metadata reader、当前run/source、原selected ASCII canonical字节数/SHA、实际行类别计数及所有列/常量/map。原selected identity只描述本次实际已选对象；不承诺此前丢失文件可凭SHA恢复。

源码附带expand_rule_resource_summary，逐kind恢复原同名对象。它不在writer中调用，不构成新门；它明确说明全部表格的意义。proof按每个kind、完整identity和专门README map逐项证明expand(tabulate(S))=S，并保原canonical身份。

## 5. 字符、数字与单份传输

新canonical使用完整UTF-8 JSON、sort_keys=True、原紧凑分隔符、allow_nan=False和一个末LF。普通Unicode无需变成六字节escape；孤立surrogate如存在则明确保为JSON Unicode escape。数字仍由同一原JSON数值编码规则输出，不降精度、不换成hex编码、不抹负零。

原已选大日志仍只按原log_view给首两/末条必要错误；此来源和全部原错误细节没有再缩。这里没有压缩、分包或任意raw字典，也不输出可重新生成的数组或整个原payload。所有所选必要信息都在一个可直接读取的JSON正文内。

实际frame继续为：

    BEGIN_REQUEST205_NECESSARY_RULE_RESOURCE_SUMMARY
    <本次完整R499 JSON，含末LF>
    END_REQUEST205_NECESSARY_RULE_RESOURCE_SUMMARY

原identity事件仍名request205_necessary_rule_identity，其bytes/SHA指实际新packed UTF-8 JSON含LF。原over-budget事件仍名request205_necessary_rule_summary_over_budget，记录实际新bytes/SHA；超过90000即70、BEGIN前停止、无部分传输/cleanup marker。是否fit必须看真实执行，不借212旧未返正文推算成功。

## 6. 状态、marker与清理

| 实际情况 | 返回/输出责任 |
|---|---|
| packed超过90000B | 原70，完整body不输出，marker不写，原raw保留 |
| packed未超限但原complete_necessary_scope=false | 先完整单份输出，再原2，marker不写 |
| packed未超限且原scope完整 | 完整输出及identity后写原marker，正常返回 |
| 原环境/源/owner或文件读取异常 | 沿真实错误位置返回，不补任何完成状态 |

marker路径仍为VISIBLE_BASE/rule-readback-complete.json，schema仍为request205-complete-rule-resource-readback-v1。原repository/run/source、complete、quiescent与large_text_omission_scope_explicit含义不变；necessary_summary指新body真实bytes/SHA。它没有声称新body是旧物理布局，实际body的新schema/source清楚分列。

marker仍排在完整输出和原complete检查之后，以xb新建、flush/fsync；原owner静止与所有其他scope的清理条件保持。reader自身没有cleanup动作，不因表格变短删早期记录。新entry必须让原cleanup实际看全部必要outcome/marker，而不是看某step的success标签替代这些事实。

## 7. 当前范围

本文件/证明/源码已完成，尚无实际R499读回或新request。没有新FD/native/fullDN/接受场、误差下降、闭面或几何比例。实际临时存储R498、三层来源R496、逐H live128及README全部完成标准继续原工作；不把表示证明变成新科学门，也不在这个子题或阶段报告停止。
