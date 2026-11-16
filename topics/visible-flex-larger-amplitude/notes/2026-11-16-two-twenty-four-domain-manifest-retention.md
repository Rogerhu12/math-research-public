# 两份旧 twenty-four domain manifest 的固定历史保留与当前引用审计

作者：ChatGPT（AI，amplitude agent）  
日期：2026-11-16

**可信度：已完成本次固定头的真实字节/引用审计及指定 producer/consumer 源码判读；不是新的科学计算、数值接受或任意动态程序无依赖证明。**

## 1. 结论、唯一候选与保护范围

建议在 root 完成固定扫描头到最终实际 pull 的新增变化守护后，普通删除 main 中下列两份历史 domain manifest，并用本说明及其固定 Git 历史链接保留原来源。只移动这两份完整历史 JSON 清单，不移动同目录的数组清单、参数请求、任何实际数组或 gzip、原 warm/status、科学源及其它输入。本文不自行操作 Git refs 或执行删除。

| 候选 | 固定文件 | bytes | Git blob | SHA256 |
| --- | --- | --- | --- | --- |
| c24a | [notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json) | 650502 | `264be53d2b49692ae38e7bcf653ad5b57be60ec3` | `5c20a6fdd0d0450c248107c90a5bb2e754a05d76d0e102a421f127233b135839` |
| c24b | [notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json) | 650500 | `8a75bd0bdcb69b0c62e0069674f4d7694b3b53d5` | `d08e1ba67554e7aad58368820997186c4a0364e77aa28b8831986d3ffeb70676` |

两件毛额合计 **1,301,002 bytes**；净腾出量须扣除实际本说明及 root 最终变更的字节，不能把毛额冒成净额。两件都不是现有原参数请求或原科学程序：各自列出 215 个当时导出文件。本次固定 tree 中，两份清单所列的 215 条 payload 路径各自均不存在，present 列表为空。这只是该固定树的路径事实，不证明原数组从未存在，不承诺重现原科学字词，也不授权删除其它位置的数组。

真正读取关系已区分：原 producer 从同次 capture 写新 manifest；完整 artifact reader 从原固定 ZIP 的新临时提取目录读 manifest 及全 NPZ；后续 warm 延续实际父 warm/status；保留的 JSON 记录/数组清单保存原 model 身份。本文保全部17组、94行高特异命中，没有把共有目录词算作正在读取 main 副本，也不以关键词零命中作为唯一依据。

保护范围包括所有当前 scientific source/request/input、原 warm/status、全部 gzip/真实数组、41/54 数组清单、四份先前 producer、十一份旧 log、migration/legacy/R456 以及有非 Markdown 引用的 H。两候选目录内本次实际存在的所有兄弟文件均保留。先前95个checkpoint、九件行政记录、两份旧domain和两份twenty-five清单不再提议删除。旧25审计不替代本次24实际结果。

## 2. 实际行政运行与完整必要读回

| 项目 | 实际值 |
| --- | --- |
| repository | Rogerhu12/math-research-public |
| 固定扫描及本次恢复 commit | `439d4f63a4e60e831f4655c27704fca081db2e09` |
| 固定root tree | `3646dbede75169aacb6a2ef169851e72d40a7f94` |
| 固定topic tree | `f35251021eb11f7b49cc49f5ab9268ffcb9d71b2` |
| 只读workflow分支 | visible-flex-larger-two-twenty-four-manifest-audit-20261116 |
| 实际workflow head | `1dd4e4e798dd17146633ce33d100e133fb85a4d8` |
| workflow path | `.github/workflows/visible-larger-two-twenty-four-domain-manifest-retention-audit.yml` |
| workflow全文身份 | 42592 bytes / `397a162e0f03ee8d6ca0f32f8a0cc66b8d29fd9d2fe15f3bc98c4a6b636b4fa0` |
| 实际run / job | [43895375578](https://github.com/Rogerhu12/math-research-public/actions/runs/43895375578) / 133397372679 |
| event / attempt | push / 1；唯一行政push |
| 创建 / 官方终态更新 | 2026-11-16T15:21:01Z / 2026-11-16T15:22:42Z |
| 实际必要frame结束 | 2026-11-16T15:22:38.3278141Z |
| 步骤范围 | setup、partial/sparse、实际扫描、complete job均success；按下面实际正文而非success标签得结论 |
| 完整必要frame | BEGIN_FIXED_DOMAIN_MANIFEST_RETENTION_AUDIT / END_FIXED_DOMAIN_MANIFEST_RETENTION_AUDIT |
| 完整必要正文 | 76213 bytes / `be4d85819de48b8de8ebc9fe281f6983ca32eaa11074f4bf910a14a565ac66be` |
| 日志返回文本 | 140886 UTF-8 bytes / `9c902828d2468c452a21a0a1723e240511372981c4cf70cba14833a2d4060760` |
| 日志身份含义 | connector已解码文本重新UTF-8编码的身份；不是HTTP原始响应字节 |
| 唯一终态阅读 | 本agent只取该job日志一次，未取running log、未重取旧科学日志 |
| 原容量与出口 | 76213 < 90000；未触发70；没有分片、删字段或抬限 |
| errors / worktree | errors=[]；git status为空；repository_worktree_unchanged=true |

workflow head 是本次行政代码版本；扫描/recovery head 是被查仓库版本，二者没有混用。原必要对象的 GITHUB_RUN_ID、attempt、SHA、workflow ref 全部与官方身份一致。本文及后续 root 结论不用先前消息中错误的“15:24”时间标签。

两份大于100KB的候选正文仅在本次公开 Actions 内读取、解析并核原 Git blob 与 SHA；没有通过 connector 全文打开。返回的行政 raw/necessary 只留当前临时工具状态，没有创建 Git blob、提交或重新链接为交付。写入仓库的是本篇作者解释和必要身份/地址，不是完整 raw 输出。

## 3. 实际检索域、回退、历史与未扫补集

本次真实 partial clone 使用 remote.origin.promisor=true、filter=blob:none、sparseCheckout=true。固定 tree 仅用 git ls-tree -r -z --full-tree，不使用 -l，不为未知大blob询问size。先用完整tree路径确定predicate，再稀疏检出实际需要的文本与本题gzip；未知未选blob大小明确为null。

| 实际项 | 值/身份 |
| --- | --- |
| 完整tree原输出 | 9138631 bytes / `2eafbb7a4ed830674a2bff62f65e7c8fa5b08d22eb9bd85142e38267e4edc24b` |
| tracked regular blobs | 55977 |
| 本题blob数量 | 9520 |
| 本题实际已选文件字节和 | 198947275；不是全topic总量 |
| 本题未选blob数量/大小 | 43 / null |
| selection文件 | 9815552 / `d6e676bdf55cd0635f542b490b3ac210ac2042d4bc82384d688a22ee7db8c502` |
| 全部已选路径序列 | 4906487 / `eaa318faad8bffdcb5b564a7cff671146c6f5f0d137ec1c90873d0f58b30947f` |
| sparse pattern文件 | 4862836 / `09099befcfc1e1aca9585865ef6b472ff39ac900bd2da03846d7c3242a25798b` |
| 当前source/config/input | 31352 |
| 历史文档实际扫描 | 12219 |
| 本题gzip实际EOF | 77/77；decoded 60078173 bytes；failed=[] |
| gzip完整逐文件元数据列表身份 | 23962 / `b15440a896a4d0a43f72ff4845aa8d231653087ac41bcf276f07357abb9f28f1` |

完整文本后缀 predicate 为 `.py`、`.mjs`、`.js`、`.json`、`.yml`、`.yaml`、`.hpp`、`.h`、`.cpp`、`.cc`、`.c`、`.sh`、`.toml`、`.ts`、`.tsx`、`.md`、`.markdown`、`.rst`、`.txt`、`.ini`、`.cfg`、`.xml`、`.html`、`.css`；完整 basename 集合为 `.gitattributes`、`.gitignore`、`.gitmodules`、`COPYING`、`Dockerfile`、`LICENSE`、`Makefile`、`README`。仅regular modes100644/100755。另将本题路径前缀下所有 .gz 解码到EOF；不评价其中科学数值。

历史文档的明确分类为大小写归一后的 .md/.markdown/.rst/.txt，以及 readme/license/copying basename。其它已选文本（包含其它题目的source/config/input）进入完整当前直接引用扫描。两个候选自身不参加自引用检索，而已先完整读核其自身身份。

runner没有rg，实际使用标准库逐完整字节行回退；没有把“rg不存在”冒成零命中。全部626批次实际行的序列已核：direct-current-inputs 262批，首index0、每批120路径、末index31320/count32；constructors同262批；historical-documents-aggregate 102批，末index12120/count99。它们分别覆盖31352、31352、12219路径。所有实际state是exit0、stderr0 bytes、空串SHA256；共有表只在原三个字段全等时共享，原批次顺序/起点/count保留。

| 批次原表 | 字段/精确身份 |
| --- | --- |
| 批次列 | kind, first_path_index, path_count, state_index |
| state列 | exit, stderr_bytes, stderr_sha256 |
| 唯一实际state | [0,0,`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`] |
| 完整626批次数组canonical身份 | {"bytes":22061,"sha256":"f0942f81a35d522511fceeea20f204b4b5dbd6d3fcf4dab0c99a9711d00223ce"} |
| 完整逆 | 按每原批次取前三列，再拼接该state_index的三个原值；不填缺项、不补未运行批次 |

**未扫补集明确保留**：固定tree全部tracked blob中不满足上述完整predicate者，共 12327 件。没有读取其blob大小，bytes=null；没有声称它们无引用。精确完整路径清单身份 2462095 bytes / `16666879e39a2e4db93342fd4a47aaae9b6e4b9484ec1d6017ba585ae34da4c5`。该补集由固定tree与完整predicate唯一确定，不把未知大小算零。

| 未扫类别 | 后缀 | 文件数 | bytes |
| --- | --- | --- | --- |
| gzip_outside_topic | .gz | 6656 | null |
| other_suffix_or_binary | (no suffix) | 13 | null |
| other_suffix_or_binary | .cjs | 109 | null |
| other_suffix_or_binary | .csv | 1 | null |
| other_suffix_or_binary | .diff | 47 | null |
| other_suffix_or_binary | .gp | 37 | null |
| other_suffix_or_binary | .jsonl | 608 | null |
| other_suffix_or_binary | .lock | 201 | null |
| other_suffix_or_binary | .log | 4521 | null |
| other_suffix_or_binary | .mix | 56 | null |
| other_suffix_or_binary | .npz | 3 | null |
| other_suffix_or_binary | .patch | 8 | null |
| other_suffix_or_binary | .png | 1 | null |
| other_suffix_or_binary | .recipe | 49 | null |
| other_suffix_or_binary | .sing | 4 | null |
| other_suffix_or_binary | .spec | 10 | null |
| other_suffix_or_binary | .ssi | 1 | null |
| other_suffix_or_binary | .stop | 2 | null |

本次nonregular为空。未知外部、计算拼接、编码、未来引用和未扫后缀责任不因literal结果消失。

### 3.1 历史文档与generic constructor的必要表示

历史文档实际扫描完毕，但其逐项路径/行地址没有回传；只返回完整匹配文件清单和地址流的身份及每pattern计数。generic同样是共有构造词扫描，不能把数百泛命中全称为两候选的实际读取者，也不从其聚合表推出动态无关。两类明确范围如下。

| 范围 | 实际数量 | 完整身份 |
| --- | --- | --- |
| 历史匹配文件 | 14 | {"bytes":3188,"sha256":"0eadfc2cbaa6af27ce682a6274934da7edd728bc31eaa2b84d17be7c70188884","row_count":14} |
| 历史匹配行/地址流 | 25 | {"bytes":4896,"sha256":"8cba505554fe220025802a28e8ea0fd4251807076eb667d7fd477992d0b2ab2c","record_count":25,"format":"canonical UTF-8 JSON [path,line,start,bytes,line_sha256,all_pattern_offsets] then LF for each match in actual scan order"} |
| generic匹配文件 | 280 | {"bytes":67441,"sha256":"a945faba7f331749ab3c82db9f1a3add453b1169b94ab6d9d02965ba4da871f4","row_count":280} |
| generic file-pattern pairs | 657 | 完整实际计数 |
| generic地址记录 | 4027 | {"bytes":557106,"sha256":"cb72e4b1a7f453ba5b8923e4ff24ae4e979a822ddfb6bd3f2cec1c5560557f63","row_count":4027} |

全部具体candidate命中仍完整列出文件身份与每行/字节/模式出现地址（第6节）。本次topic gzip没有任何具体candidate literal命中；所有77件仍真实读至EOF，这不是未读而写零。

## 4. 原producer、参数、原输入与真正读取方式

两候选schema相同：captured-twenty-four-query-original-RMS-and-collocation-midpoint-domain-v1。它们是不同run/不同state的完整历史导出，不是可互换的一份结果。

| 项目 | c24a / actual76 | c24b / actual79 |
| --- | --- | --- |
| 原run | 43661532089 | 43663293492 |
| 原source commit | `1377826d89317b491f75036cafd63c3ea5bea5f1` | `31d2ad909638aa3eb3211a9ea0feed632c0e9a2b` |
| 原request SHA256 | `ea45ed8054693e21694d07720ee5c519d28863a721f492ab638b7e2f2f8e94ee` | `fb8985c3ae11c6fbd6c7fe8dd57f18f5f152c1a346d339134ca98696ce43ac09` |
| 原request/时间 | [76,"2026-11-15T01:01:22.599055Z"] | [79,"2026-11-15T01:22:23.779618Z"] |
| 原B model SHA256 | `f74b464eb3fcfe233cc084195e1fed50ab70b52aac07472343c5a96d1d1714d1` | `656a644d77d438deb67f454a8c588ae9c05043570691072d6779300c92157fc3` |
| 实际父run | 43659610548 | 43661532089 |
| 实际父source | `145d7a53ec05a64d39d0a36ac3e441e3475cb9bf` | `1377826d89317b491f75036cafd63c3ea5bea5f1` |
| 实际父public目录 | `notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm` | `notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm` |
| 实际父warm SHA | `204b208393218923f8abf9a36b6f03d29306409155447f561b2c2f4c373001a3` | `bba24c1f882d14751c4272148ee0cd6271c584485c6d0d3efaafa1a081a2a97f` |
| 实际父status原JSON SHA | `09d944723fb6be152e90ba283fc44d33d455f1a52bc73787a329fcdc7d97ea73` | `a1a67b9a1e0e97aa23404a8fa6c5936805de34f763f0076516c4f736aedc4cb5` |
| 完整followup文件 | [notes/public-actions-43661532089-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/followup-request-identity.json) | [notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json) |
| 完整followup bytes/SHA | 24905 / `d51f3a4e321f33b777ee435b9de59d12ce09e4741a3ecff4edd1d037474d7a3f` | 26901 / `816dabdcdfe43c8c4f36de9e68fa99c896bfff925444f2e4becead7788fa809f` |

原两请求共同的显式预算完整为 `{"overall_seconds":1200,"candidate_seconds":600,"trial_reserve_seconds":90,"recovery_reserve_seconds":30,"local_working_rows":512,"dual_sweeps":200,"lambda":270,"lsmr_iterations":200,"projection_sweeps":200,"original_trial_count":17}`；两者该对象相同。其selected_query_count=24、selected_angle_row_count=49152、complete_B_local_dimension=7101；原left-RMS interval列表 `[466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485]`，原midpoint列表 `[473,475,477,480,481,482,484,485]`。这些是原请求元数据，未做新数值求解或重新评价有效性。scientific_thresholds_changed、native_tail_requested、research_goal_completed均为原false。

原source_entry为geometry_20261114_twenty_four_query_collocation_observer_warm.py，mathematical_producer为geometry_20261114_twenty_four_query_condensed_warm.py，optimizer_schema为exact-constraint-twenty-four-query-condensed-complete-H-warm-v1。未选的原request字段仍留完整followup；没有把不在selected map里的query_specs/可选键填成null或假称不存在。原真正24行族的0.17267316464601146 left-RMS和0.5 midpoint定义仍由原producer源码解释，不重选。

两候选manifest返回的原input_identity完整如下（仅身份，不读取或重造对应科学输入）：

| 键 | c24a | c24b |
| --- | --- | --- |
| resume_sha256 | `204b208393218923f8abf9a36b6f03d29306409155447f561b2c2f4c373001a3` | `bba24c1f882d14751c4272148ee0cd6271c584485c6d0d3efaafa1a081a2a97f` |
| source_prepared_sha256 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| source_accepted_sha256 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| actual_tail_config_sha256 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| actual_zero_anchor_sha256 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |

两份manifest声明的九个producer/原kernel源，均由本次Actions逐原文件完整SHA核，与声明值一致；它们在第6节file0..8完整列明。另为确认实际I/O链，从同一固定head读取下列小于100KB的原源，逐全文SHA核到原followup/reader指定身份；只读文字，没有import/AST/执行任何数学。

| 实际source | bytes | Git blob | SHA256 |
| --- | --- | --- | --- |
| [computations/geometry_20261114_twenty_four_query_condensed_warm.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_four_query_condensed_warm.py) | 42798 | `4692288aada60b7cb98c615bc210b86007d3d129` | `b453b53d4ae759e0bc50d5d789beb04e53c18903adaf427c2a28c0382827d452` |
| [computations/geometry_20261114_twenty_four_query_collocation_observer_warm.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_four_query_collocation_observer_warm.py) | 16732 | `92c8d1b085f9c636f4adffd2a3ac09b0c81cfc3a` | `f6639751ea97bd857ad05ad0a36d38d11024dac25f6ecc0610fef2d9fe90cf35` |
| [computations/geometry_20261114_twenty_four_query_condensed_response.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_four_query_condensed_response.py) | 2622 | `03241d7d156b334e650f0ba9ef344fa57af8f943` | `87261854684d5844c97d59b328db2aa070b015b565baf46dfb7e811808b3bb87` |
| [computations/exact_20261114_fetch_pinned_public_artifact.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/exact_20261114_fetch_pinned_public_artifact.py) | 28006 | `8ee390d0c1449a6a532d72158172af278f1c7cf3` | `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` |

### 4.1 Producer不是旧main manifest的读取者

原24 domain operator 的119–140行以同次problem/state/capture构造完整operator；459–508行的export从该对象写完整数组和self.description()，已有数组/manifest一律拒绝覆盖。它的原base FullAngleDomainOperator.export（655–708行）同样从当前对象写新输出，并明确Git发布属于外层。这是输出生产路径，不是读本次旧main候选作为输入。两份实际manifest各列215件，是这两次原结果的事实，不是对任意未来capture文件数的承诺。

原warm的151–176行及347–381行只绑定实际--resume/--parent-status与预期SHA；首父为actual74，续算可为完成的own-schema warm。它的327–340行将新24 operator类接原engine后调用原main；observer的55–94、293–299行保原CLI/parent身份并委托该真实producer。没有把旧main domain manifest补作新的求解输入。原response保完整实际新warm FD consumer，来源与原产物身份均未改。

warm的647–658行另外生成兄弟condensed-array-manifest.json，保存结果和actual_parent_warm/original_B_model身份；**这个兄弟清单保留**，不能因名字相似而一并删除。

### 4.2 确有原artifact reader，目录来自真实固定ZIP

file21的fetch_original（191–238行）使用SHA锁定的51224788原transport，核原run/source及完整ZIP，传入--download-out并在返回后核原transport receipt；readout（345–346行）令directory=root/WARM_DIR，audit_domain（564–579行）读取该directory/domain-operator/manifest.json并核原model绑定及所有NPZ。main（812–875行）先真实fetch成功才进行这些读回。

原transport的349–384行强制输出为RUNNER_TEMP下新不存在的绝对目录；481–544行下载、核整ZIP、完整安全解压、独占发布后封只读。它不能把已有本题main notes目录当合法download_out。因此这里确实存在“需要domain manifest”的程序，但需要的是**固定原artifact内的完整manifest与payload**，不是两份main历史副本。本文没有豁免其完整artifact读取，也没有假定旧artifact仍在线或由历史SHA可重造数组。

保留的原readback请求和addendum明确指向：

| 原artifact | run | artifact ID | 原size | 原SHA256 |
| --- | --- | --- | --- | --- |
| `visible-followup-condensedqp-43661532089-1` | 43661532089 | 14140726714 | 640977134 | `b57824ec8cb6ef22525966725fd333c4dfb1a0111aa403ccf54117d02ab7289c` |
| `visible-followup-condensedqp-43663293492-1` | 43663293492 | 14141611284 | 639331603 | `c2432e485c0d7e1c2a047d43ade9b0ec9bb159a1e266c8cee81a1b163f298257` |

这些只是已有固定输入的原身份，本次未重新下载它们、未读取科学日志、未执行旧reader，也未对旧科学成败作新判定。

### 4.3 真实父warm/status不因目录整理消失

actual79的followup、parent76 restore记录把actual76作为父，后续actual84的followup、parent79 restore把actual79作为父。restore记录实际内容是warm-001.json.gz和透明解压后的driver-status原字节；没有domain manifest读取条目。原warm/status的SHA、存储与解码关系在这些保留文件中完整存在。原输入责任仍须在实际后继执行中满足，不能用本篇容量结论代替。

## 5. 全部17组具体引用判读

| file索引 | 真实引用文件 | 实际行数 | 判读/保留 |
| --- | --- | --- | --- |
| 21 | [computations/root_20261114_read_completed_twenty_four_prefix.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/root_20261114_read_completed_twenty_four_prefix.py) | 1 | 唯一直接匹配的可执行 reader：第46行只是 WARM_DIR 常量。实际 fetch_original 191–238 行把经过固定run/source/ZIP核对的新提取目录作为 root；345–346 行形成 root/WARM_DIR；564–579 行从该目录读取原 domain manifest 和完整 NPZ；812–875 行强制先完成 fetch 再 readout/audit。其原读取义务保留，但对象不是本次 main 的两份候选副本。 |
| 22 | [notes/2026-11-15-actual76-primary-identity-readback.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/2026-11-15-actual76-primary-identity-readback.json) | 6 | actual76 原主字节身份 JSON。匹配处是原run及 /tmp/visible-larger-actual76-published 中 status/model/summary/warm 的已读身份，不是执行读取候选的脚本。完整记录保留。 |
| 23 | [notes/2026-11-15-actual79-primary-identity-readback.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/2026-11-15-actual79-primary-identity-readback.json) | 8 | actual79 原主字节身份 JSON。除本run输出身份，还明确保 actual76 父 warm/status 路径；它们是真实父输入责任，全部保留，不能与本次 domain manifest 混同。 |
| 24 | [notes/2026-11-15-actual84-primary-identity-readback.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/2026-11-15-actual84-primary-identity-readback.json) | 2 | actual84 原主字节身份 JSON。两处是 actual79 父 warm/status 的 /tmp 路径；没有把其改成 domain manifest。该记录及真实输入责任保留。 |
| 25 | [notes/actual76-completed-reader-addendum.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/actual76-completed-reader-addendum.json) | 29 | actual76 completed-reader addendum。包含原artifact pin、原报告副本路径、原B model SHA以及完整condensed-root数组描述；它是已发生读回的身份/结论载体，不是从main候选读取数组的当前程序。全文保留，不据旧诊断重新宣称科学通过。 |
| 26 | [notes/actual76-completed-reader-route-static.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/actual76-completed-reader-route-static.json) | 2 | actual76 原reader source-only route JSON，两处是原artifact run/name。完整artifact pin继续保留，旧source-only检查不是本次执行或删除依据。 |
| 27 | [notes/actual79-completed-reader-addendum.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/actual79-completed-reader-addendum.json) | 29 | actual79 completed-reader addendum。与actual76同类，原artifact pin、报告、原B model及raw数组描述均保留；不把数组描述等同数组仍在main或可以恢复数值。 |
| 13 | [notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json) | 1 | 候选c24a的兄弟 condensed-array-manifest.json 第2133行保存 original_B_model_sha256。该兄弟清单不是删除对象，其全部文件/数组描述和结果引用原样保留。 |
| 28 | [notes/public-actions-43662815323-1-receipts/completed-readback-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43662815323-1-receipts/completed-readback-request-identity.json) | 2 | 原completed readback请求的 original_artifact run/name；实际指固定原ZIP 14140726714。仍按原reader来源读取，保留该完整请求，不转成从main候选输入。 |
| 16 | [notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json) | 3 | actual79 followup 请求的 actual_parent_run、nearest_rejection.parent_run 和 actual_parent_public_directory，均指actual76父。真实resume/status SHA与目录责任在原请求里保留；共同父目录并不表示读取其domain manifest。 |
| 18 | [notes/public-actions-43663293492-1-condensedqp/parent76/restore-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/parent76/restore-identity.json) | 1 | actual79保存的 parent76/restore-identity.json。实际恢复 warm-001.json.gz 与透明解压后的原status，并保原字节SHA；没有候选manifest恢复或读取条目。完整保留。 |
| 19 | [notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json) | 1 | 候选c24b的兄弟 condensed-array-manifest.json 第2133行保存它的 original_B_model_sha256。该完整兄弟清单保留，未把模型标识改写成另一个科学模型。 |
| 29 | [notes/public-actions-43665645276-1-receipts/completed-readback-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43665645276-1-receipts/completed-readback-request-identity.json) | 2 | 原completed readback请求的 original_artifact run/name；实际ZIP 14141611284。完整请求/父信息保留，未再次下载原科学artifact。 |
| 30 | [notes/public-actions-43666177645-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43666177645-1-condensedqp/followup-request-identity.json) | 4 | 后续actual84的followup请求：actual_parent_run、nearest_rejection及actual_parent_public_directory指actual79；另一个 first_actual_parent_run 是完整来源历史。保真实warm/status输入以及原请求，不能只因已旧而删去。 |
| 31 | [notes/public-actions-43666177645-1-condensedqp/parent79/restore-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43666177645-1-condensedqp/parent79/restore-identity.json) | 1 | 后续actual84的 parent79/restore-identity.json 实际保warm和status两输入的存储/解码身份。它们全部保留，domain manifest不在这份restore记录的输入中。 |
| 32 | [notes/public-actions-43668743515-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43668743515-1-condensedqp/followup-request-identity.json) | 1 | 后续actual86 followup中的 first_actual_parent_run=actual79 是继承的condensed入口历史；全文和全部源pins保留。未据此推断所有将来动态路径都不存在。 |
| 33 | [notes/public-actions-43671882961-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43671882961-1-condensedqp/followup-request-identity.json) | 1 | 后续actual89 followup中的相同 first_actual_parent_run 是沿既有入口继承的历史字段；全文保留。这里只解释该实际JSON位置，不给未知动态读者作零证明。 |

以上每份引用文件均原样保留。没有发现候选本身以外的repo完整path、topic相对path、候选Git blob或候选manifest SHA的直接命中；命中的是共有producer目录、原run、父目录或原B model。这个有限域文字事实与上面的实际I/O来源论证共同构成建议，不单靠零命中，更不排除未知计算拼接/外部/未来读取。generic命中不自动等于可执行读取，若root最终delta出现未解释的新reader必须沿真实来源处理。

## 6. 全部具体地址与文件身份

下列34件身份直接来自本次固定Actions返回；包括两候选、全部现存兄弟、原九源与所有具体匹配文件。两个大候选没有通过connector打开。辅助四小源已在第4节另列。

| 索引 | 固定文件 | bytes | Git blob | SHA256 |
| --- | --- | --- | --- | --- |
| 0 | [computations/geometry_20261114_constrained_collocation.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_constrained_collocation.py) | 18309 | `deb4856235d2d57a7003495a0e15c748be41b9b3` | `70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8` |
| 1 | [computations/geometry_20261114_hermite_domain_constraints.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_hermite_domain_constraints.py) | 23762 | `885ff3e6b69c44b2488e24afd11606a52fb42f87` | `d9e004c827add0074c2e6dd6c854763c7157e5049cd5360c1f85ad440462f4ce` |
| 2 | [computations/geometry_20261114_full_angle_domain_direction_probe.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_full_angle_domain_direction_probe.py) | 27821 | `5ff83a675e97bf5d70f9009e1e937e2ae86ac54b` | `794788a17db22189b80d65b7def84f3515ca587ea59ffce96fe8887a071665e8` |
| 3 | [computations/geometry_20261114_full_dn_augmented.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_full_dn_augmented.py) | 11311 | `05608a21d822a3150d0ac4fba656909f85c33b6d` | `f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e` |
| 4 | [computations/geometry_20261114_fft_frenet.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_fft_frenet.py) | 2143 | `a6470e86bceae9c0406751a00793c77d77de2bfd` | `973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401` |
| 5 | [computations/geometry_20261114_r225_free_core_bvp.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_r225_free_core_bvp.py) | 23914 | `64ad4f0b9ca6b1edb4a46d27ff5f6b87154e3a95` | `a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08` |
| 6 | [computations/geometry_20261114_full_angle_domain_operator.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_full_angle_domain_operator.py) | 38319 | `ce7849914e2abc4eb4a7130d705cd0531243cb24` | `af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7` |
| 7 | [computations/geometry_20261114_twenty_three_query_domain_operator.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_three_query_domain_operator.py) | 32291 | `3a0b545e3819abf515ec63e33f8fb234f0627705` | `755d9bf2a01c5c417b28bfd265ee76712bba54a9fdeddf34ea56c4668abefe98` |
| 8 | [computations/geometry_20261114_twenty_four_query_domain_operator.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_four_query_domain_operator.py) | 32451 | `6703e3d796fd840bbe3a3dbd17434c31b61ff424` | `06933e9341664d63b5a9eaeb00998daa1be7b1c1d143a60f1ae2ef05efa9db36` |
| 9 | [notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json) | 650502 | `264be53d2b49692ae38e7bcf653ad5b57be60ec3` | `5c20a6fdd0d0450c248107c90a5bb2e754a05d76d0e102a421f127233b135839` |
| 10 | [notes/public-actions-43661532089-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/followup-request-identity.json) | 24905 | `65e1907451649daf59abed540b609470b8bbc828` | `d51f3a4e321f33b777ee435b9de59d12ce09e4741a3ecff4edd1d037474d7a3f` |
| 11 | [notes/public-actions-43661532089-1-condensedqp/T112-config.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/T112-config.json) | 2161 | `543d8364593985305438dda6a0c89b4b1a9c7ec5` | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| 12 | [notes/public-actions-43661532089-1-condensedqp/parent74/restore-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/parent74/restore-identity.json) | 685 | `2eafa535cd9d7a8f4002591535c42619d15325ec` | `6649961c43f38f64e0bd60c0960178d778b96854c4c5e2ac0b451e06f9b10a84` |
| 13 | [notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json) | 75747 | `8693eb7b30a48087e3e11b1ad87fb739f2a44179` | `274a90a449417c256ec4a48e12ce4e4e522e0870eda86253a08873c1fe111d15` |
| 14 | [notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/optimization-intent.json.gz](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/optimization-intent.json.gz) | 204185 | `59d371236c4cb331cace44d5da422b58093d7619` | `aab67b16ea52da5e17d48c518e67d7c903fa2bb5675d59ff893dba5e681ad60d` |
| 15 | [notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json) | 650500 | `8a75bd0bdcb69b0c62e0069674f4d7694b3b53d5` | `d08e1ba67554e7aad58368820997186c4a0364e77aa28b8831986d3ffeb70676` |
| 16 | [notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json) | 26901 | `49f9bd332e0fb9fd013bbaf88f3cd4b1e8a949df` | `816dabdcdfe43c8c4f36de9e68fa99c896bfff925444f2e4becead7788fa809f` |
| 17 | [notes/public-actions-43663293492-1-condensedqp/T112-config.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/T112-config.json) | 2161 | `543d8364593985305438dda6a0c89b4b1a9c7ec5` | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| 18 | [notes/public-actions-43663293492-1-condensedqp/parent76/restore-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/parent76/restore-identity.json) | 685 | `acc150f367aaa731316c4009623736c057c39c8c` | `c646f8d832954bd7d06a06cfb078e838451c01310f9d9cadb2cff74988820d51` |
| 19 | [notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json) | 75748 | `dc8a879b81682c8f58b4f95f39516e77f6b1f5bf` | `97e24581b501bc865a1731a38f6b8c0d7cc041ef911ebb0b756d4d9cc3e47b6c` |
| 20 | [notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/optimization-intent.json.gz](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/optimization-intent.json.gz) | 216641 | `1eb89f23feb5b61e8a2334088e66489b41ecb646` | `9398ff5a679df2a1617b5475cc4a95590a270cef8b39d3b5ff8830b10c50dd8a` |
| 21 | [computations/root_20261114_read_completed_twenty_four_prefix.py](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/computations/root_20261114_read_completed_twenty_four_prefix.py) | 50285 | `6ba9687d98fedd8018a45142c2e1d06ea5ee0051` | `1aa4da4e721aa12a9f4d6257e3a6b6a7b328059de217ba42268d73a018e9828c` |
| 22 | [notes/2026-11-15-actual76-primary-identity-readback.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/2026-11-15-actual76-primary-identity-readback.json) | 27754 | `835da243ce7cfff1204fc098c9ef9a4e1232adab` | `5c5bc17fe33c262369f822a66c18d7cbabeccc0b3a9df1bc9d7ef322e5e46eba` |
| 23 | [notes/2026-11-15-actual79-primary-identity-readback.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/2026-11-15-actual79-primary-identity-readback.json) | 27752 | `7189544c57bb22c9f28b9721899b3112617d061f` | `1aec1f1070ea9bfa9749bcb97809d9c728a9eb3f4c98dd833cda8da8ab5b3fee` |
| 24 | [notes/2026-11-15-actual84-primary-identity-readback.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/2026-11-15-actual84-primary-identity-readback.json) | 28544 | `ee2f259650b96df9b288d04c8b412eae4fd5908a` | `f13487e8888d64f9fee769ebbb05965bd9626d86f1ab50edd5051a07c4441481` |
| 25 | [notes/actual76-completed-reader-addendum.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/actual76-completed-reader-addendum.json) | 58513 | `939a9d6912cb9ac27df06f2a407274705890e9c3` | `867d5b383faa3859ffc247792ba9ea093f12abb2add0be9dc5d6571dadf27c39` |
| 26 | [notes/actual76-completed-reader-route-static.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/actual76-completed-reader-route-static.json) | 1720 | `9c40a26c1c3c2757fe4f28f348baa3a5c542cade` | `871de03561e6fa2cd570e01d1d0d0dde147b4e72fa6be81f924a1b0f266ee472` |
| 27 | [notes/actual79-completed-reader-addendum.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/actual79-completed-reader-addendum.json) | 59230 | `ad3361751974aea7623e89f8da4d4b8e47619c43` | `7217b108cd6635c3479ea6a29a76c45484db73867103b616538b6cbdfe3fd552` |
| 28 | [notes/public-actions-43662815323-1-receipts/completed-readback-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43662815323-1-receipts/completed-readback-request-identity.json) | 2300 | `fe01f3e8fe85fb2a21486e2a5d673d345029995d` | `f509322ac97ae4743dc0e3780267218a9a7ff973b3ceaf6d125e6cd87833c40a` |
| 29 | [notes/public-actions-43665645276-1-receipts/completed-readback-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43665645276-1-receipts/completed-readback-request-identity.json) | 2361 | `be50e919c0082fb46490498906686be09996750e` | `fac58314c1cb79e973a4df4982f065837ef4174a26a4f38c0c8d3a085025e331` |
| 30 | [notes/public-actions-43666177645-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43666177645-1-condensedqp/followup-request-identity.json) | 28528 | `f4237e3126a3d0c65c00fe1eb1c08f35b17f8e0f` | `afba5a8235f844ff1a4742048041265b069016d732017667dff082d047ef4992` |
| 31 | [notes/public-actions-43666177645-1-condensedqp/parent79/restore-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43666177645-1-condensedqp/parent79/restore-identity.json) | 685 | `79d0f9438336345e9bdf45428f7a2d113b7d7f5c` | `5b2a4399c4ef9c8e7245c5e67379de2d2228a8454627623252c3b3b9a137cef5` |
| 32 | [notes/public-actions-43668743515-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43668743515-1-condensedqp/followup-request-identity.json) | 32085 | `72440382dd243506122fa259539a5f1031caec24` | `b279bdf3a20cf129b4d35b98e4d2b97d18cd436f7794841648151199bb218531` |
| 33 | [notes/public-actions-43671882961-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43671882961-1-condensedqp/followup-request-identity.json) | 32099 | `49032d5b7d1f10463ad5bf1d9ca4bc55bdf51efb` | `26e828589423cf91040e972c535aff7bba96fe7576ebbe9eb148a6ced2c874f5` |

地址解释：原文件行号从1开始，行起点为0起始byte offset，line_bytes包含原行实际字节；pattern索引按第7节，后面的数组是该pattern在本行的全部0起始byte位置。所有representation均为tracked_file_bytes，本次没有gzip匹配组。下面保全部94行与所有命中位置，不附截断预览或省略不利地址。

### file 21：computations/root_20261114_read_completed_twenty_four_prefix.py

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 46 | 1780 | 40 | 3:[12] |

### file 22：notes/2026-11-15-actual76-primary-identity-readback.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 3 | 79 | 25 | 4:[12] |
| 12 | 652 | 102 | 3:[54] |
| 17 | 874 | 98 | 3:[54] |
| 22 | 1091 | 109 | 3:[54] |
| 27 | 1319 | 100 | 3:[54] |
| 37 | 1753 | 105 | 3:[54] |

### file 23：notes/2026-11-15-actual79-primary-identity-readback.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 3 | 79 | 25 | 11:[12] |
| 12 | 652 | 102 | 3:[54] |
| 17 | 874 | 98 | 3:[54] |
| 22 | 1091 | 109 | 3:[54] |
| 27 | 1319 | 100 | 3:[54] |
| 37 | 1753 | 105 | 3:[54] |
| 47 | 2193 | 100 | 3:[54] |
| 52 | 2413 | 102 | 3:[54] |

### file 24：notes/2026-11-15-actual84-primary-identity-readback.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 47 | 2193 | 100 | 3:[54] |
| 52 | 2413 | 102 | 3:[54] |

### file 25：notes/actual76-completed-reader-addendum.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 33 | 1112 | 27 | 4:[14] |
| 35 | 1171 | 67 | 4:[51] |
| 42 | 1487 | 72 | 3:[24] |
| 43 | 1559 | 102 | 3:[54] |
| 49 | 1829 | 68 | 3:[24] |
| 50 | 1897 | 98 | 3:[54] |
| 63 | 2488 | 88 | 3:[24] |
| 64 | 2576 | 118 | 3:[54] |
| 70 | 2860 | 79 | 3:[24] |
| 71 | 2939 | 109 | 3:[54] |
| 79 | 3271 | 63 | 3:[15] |
| 85 | 3481 | 59 | 3:[15] |
| 97 | 3888 | 70 | 3:[15] |
| 104 | 4151 | 59 | 3:[13] |
| 168 | 7787 | 99 | 7:[32] |
| 573 | 20199 | 76 | 3:[15] |
| 584 | 20577 | 79 | 3:[15] |
| 595 | 20974 | 99 | 3:[15] |
| 606 | 21384 | 88 | 3:[15] |
| 617 | 21771 | 76 | 3:[15] |
| 629 | 22162 | 78 | 3:[15] |
| 640 | 22539 | 80 | 3:[15] |
| 651 | 22916 | 78 | 3:[15] |
| 662 | 23307 | 94 | 3:[15] |
| 673 | 23710 | 90 | 3:[15] |
| 684 | 24121 | 98 | 3:[15] |
| 695 | 24535 | 93 | 3:[15] |
| 706 | 24929 | 82 | 3:[15] |
| 717 | 25332 | 98 | 3:[15] |

### file 26：notes/actual76-completed-reader-route-static.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 29 | 1191 | 27 | 4:[14] |
| 31 | 1250 | 67 | 4:[51] |

### file 27：notes/actual79-completed-reader-addendum.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 33 | 1112 | 27 | 11:[14] |
| 35 | 1171 | 67 | 11:[51] |
| 42 | 1487 | 72 | 3:[24] |
| 43 | 1559 | 102 | 3:[54] |
| 49 | 1829 | 68 | 3:[24] |
| 50 | 1897 | 98 | 3:[54] |
| 63 | 2488 | 88 | 3:[24] |
| 64 | 2576 | 118 | 3:[54] |
| 70 | 2860 | 79 | 3:[24] |
| 71 | 2939 | 109 | 3:[54] |
| 79 | 3271 | 63 | 3:[15] |
| 85 | 3481 | 59 | 3:[15] |
| 97 | 3888 | 70 | 3:[15] |
| 104 | 4151 | 59 | 3:[13] |
| 168 | 7782 | 99 | 14:[32] |
| 573 | 20191 | 76 | 3:[15] |
| 584 | 20569 | 79 | 3:[15] |
| 595 | 20966 | 99 | 3:[15] |
| 606 | 21376 | 88 | 3:[15] |
| 617 | 21763 | 76 | 3:[15] |
| 629 | 22154 | 78 | 3:[15] |
| 640 | 22531 | 80 | 3:[15] |
| 651 | 22908 | 78 | 3:[15] |
| 662 | 23299 | 94 | 3:[15] |
| 673 | 23702 | 90 | 3:[15] |
| 684 | 24113 | 98 | 3:[15] |
| 695 | 24527 | 93 | 3:[15] |
| 706 | 24921 | 82 | 3:[15] |
| 717 | 25324 | 98 | 3:[15] |

### file 13：notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 2133 | 61391 | 97 | 7:[30] |

### file 28：notes/public-actions-43662815323-1-receipts/completed-readback-request-identity.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 10 | 357 | 29 | 4:[16] |
| 12 | 420 | 69 | 4:[53] |

### file 16：notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 66 | 7785 | 38 | 4:[25] |
| 134 | 9644 | 33 | 4:[20] |
| 321 | 15244 | 115 | 2:[45]; 3:[86]; 4:[60] |

### file 18：notes/public-actions-43663293492-1-condensedqp/parent76/restore-identity.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 2 | 2 | 29 | 4:[16] |

### file 19：notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 2133 | 61393 | 97 | 14:[30] |

### file 29：notes/public-actions-43665645276-1-receipts/completed-readback-request-identity.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 10 | 357 | 29 | 11:[16] |
| 12 | 420 | 69 | 11:[53] |

### file 30：notes/public-actions-43666177645-1-condensedqp/followup-request-identity.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 70 | 8319 | 38 | 11:[25] |
| 140 | 10199 | 33 | 11:[20] |
| 322 | 15381 | 115 | 3:[86]; 10:[45]; 11:[60] |
| 357 | 17218 | 46 | 11:[33] |

### file 31：notes/public-actions-43666177645-1-condensedqp/parent79/restore-identity.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 2 | 2 | 29 | 11:[16] |

### file 32：notes/public-actions-43668743515-1-condensedqp/followup-request-identity.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 425 | 20246 | 46 | 11:[33] |

### file 33：notes/public-actions-43671882961-1-condensedqp/followup-request-identity.json

representation=`tracked_file_bytes`。

| 原行 | 行起点byte | line_bytes | 全部pattern出现位置 |
| --- | --- | --- | --- |
| 407 | 19874 | 46 | 11:[33] |

## 7. 本次15个literal、8个generic及全部计数

下表是实际literal数组，不从旧25结果替换计数。files是当前直接匹配组的文件数；一行可以命中多个pattern，因此pattern行数不能相加冒成94个去重匹配行。

| index | literal | 角色 | files | lines | occurrences |
| --- | --- | --- | --- | --- | --- |
| 0 | `topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json` | c24a:repo_path | 0 | 0 | 0 |
| 1 | `notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json` | c24a:topic_relative_path | 0 | 0 | 0 |
| 2 | `public-actions-43661532089-1-condensedqp` | c24a:run_directory | 1 | 1 | 1 |
| 3 | `twenty-four-condensed-warm` | c24a:producer_directory; c24b:producer_directory | 8 | 69 | 69 |
| 4 | `43661532089` | c24a:run_id | 6 | 11 | 11 |
| 5 | `264be53d2b49692ae38e7bcf653ad5b57be60ec3` | c24a:git_blob | 0 | 0 | 0 |
| 6 | `5c20a6fdd0d0450c248107c90a5bb2e754a05d76d0e102a421f127233b135839` | c24a:manifest_sha256 | 0 | 0 | 0 |
| 7 | `f74b464eb3fcfe233cc084195e1fed50ab70b52aac07472343c5a96d1d1714d1` | c24a:model_sha256 | 2 | 2 | 2 |
| 8 | `topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json` | c24b:repo_path | 0 | 0 | 0 |
| 9 | `notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json` | c24b:topic_relative_path | 0 | 0 | 0 |
| 10 | `public-actions-43663293492-1-condensedqp` | c24b:run_directory | 1 | 1 | 1 |
| 11 | `43663293492` | c24b:run_id | 7 | 12 | 12 |
| 12 | `8a75bd0bdcb69b0c62e0069674f4d7694b3b53d5` | c24b:git_blob | 0 | 0 | 0 |
| 13 | `d08e1ba67554e7aad58368820997186c4a0364e77aa28b8831986d3ffeb70676` | c24b:manifest_sha256 | 0 | 0 | 0 |
| 14 | `656a644d77d438deb67f454a8c588ae9c05043570691072d6779300c92157fc3` | c24b:model_sha256 | 2 | 2 | 2 |

全部generic数组与实际聚合计数如下；这些路径/逐项地址未回传，完整列表身份见第3节，不据此证明所有动态无关。

| index | generic literal | files | lines | occurrences |
| --- | --- | --- | --- | --- |
| 0 | `domain-operator` | 49 | 579 | 579 |
| 1 | `domain_operator` | 240 | 2811 | 2883 |
| 2 | `condensed-array-manifest` | 64 | 90 | 90 |
| 3 | `optimization-intent` | 65 | 90 | 90 |
| 4 | `captured-twenty-four-query-original-RMS-and-collocation-midpoint-domain-v1` | 1 | 1 | 1 |
| 5 | `geometry_20261114_full_angle_domain_operator` | 113 | 288 | 288 |
| 6 | `geometry_20261114_twenty_three_query_domain_operator` | 65 | 88 | 88 |
| 7 | `geometry_20261114_twenty_four_query_domain_operator` | 60 | 80 | 80 |

历史扫描patterns为上述15个direct加末项schema `captured-twenty-four-query-original-RMS-and-collocation-midpoint-domain-v1`（index15）。完整实际计数：

| pattern index | 历史匹配行 | 历史全部出现次数 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 2 | 1 | 1 |
| 3 | 5 | 5 |
| 4 | 8 | 10 |
| 5 | 0 | 0 |
| 6 | 0 | 0 |
| 7 | 2 | 2 |
| 8 | 0 | 0 |
| 9 | 0 | 0 |
| 10 | 1 | 1 |
| 11 | 10 | 12 |
| 12 | 0 | 0 |
| 13 | 0 | 0 |
| 14 | 2 | 2 |
| 15 | 0 | 0 |

## 8. 必须保留的兄弟文件与固定历史恢复

两候选的实际现存兄弟各五件如下，全部排除删除。原warm/status如果位于其它原保留输入或artifact路径，同样不删；当前两候选目录没有列出的文件不能被写成仍在该目录。本审计不修改任何原metadata引用。

| 候选 | 保留兄弟 | bytes | SHA256 |
| --- | --- | --- | --- |
| c24a | [notes/public-actions-43661532089-1-condensedqp/T112-config.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/T112-config.json) | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| c24a | [notes/public-actions-43661532089-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/followup-request-identity.json) | 24905 | `d51f3a4e321f33b777ee435b9de59d12ce09e4741a3ecff4edd1d037474d7a3f` |
| c24a | [notes/public-actions-43661532089-1-condensedqp/parent74/restore-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/parent74/restore-identity.json) | 685 | `6649961c43f38f64e0bd60c0960178d778b96854c4c5e2ac0b451e06f9b10a84` |
| c24a | [notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json) | 75747 | `274a90a449417c256ec4a48e12ce4e4e522e0870eda86253a08873c1fe111d15` |
| c24a | [notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/optimization-intent.json.gz](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/optimization-intent.json.gz) | 204185 | `aab67b16ea52da5e17d48c518e67d7c903fa2bb5675d59ff893dba5e681ad60d` |
| c24b | [notes/public-actions-43663293492-1-condensedqp/T112-config.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/T112-config.json) | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| c24b | [notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json) | 26901 | `816dabdcdfe43c8c4f36de9e68fa99c896bfff925444f2e4becead7788fa809f` |
| c24b | [notes/public-actions-43663293492-1-condensedqp/parent76/restore-identity.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/parent76/restore-identity.json) | 685 | `c646f8d832954bd7d06a06cfb078e838451c01310f9d9cadb2cff74988820d51` |
| c24b | [notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/condensed-array-manifest.json) | 75748 | `97e24581b501bc865a1731a38f6b8c0d7cc041ef911ebb0b756d4d9cc3e47b6c` |
| c24b | [notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/optimization-intent.json.gz](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/optimization-intent.json.gz) | 216641 | `9398ff5a679df2a1617b5475cc4a95590a270cef8b39d3b5ff8830b10c50dd8a` |

两份215-path完整导出列表的身份分别为 c24a 39569/`773bfcc85fa7013f77d133dc8c8963c540f797443bdec6a6ba54dcd66d3b71d5`；c24b 39569/`52f9e1a7cfc23b3b7eb97e6ebde1aba6084b9a18138d233d57e45e37ebf8e7f0`。两列表的present=[]、absent_count=215只限该固定tree中的这些确切路径，不扩成其它数组可删结论。

普通删除后，原完整清单仍由下列固定Git历史保留。恢复只应在新的明确目录中按其原path取得准确原字节，并核上述bytes/SHA；不能把它冒作当下科学状态，也不能从manifest alone恢复已不在仓库中的科学数组。

**c24a**：[notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json)

~~~sh
git show 439d4f63a4e60e831f4655c27704fca081db2e09:topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json > topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json
~~~

恢复范围仅该完整历史manifest；预期 650502 bytes / `5c20a6fdd0d0450c248107c90a5bb2e754a05d76d0e102a421f127233b135839`，原Git blob `264be53d2b49692ae38e7bcf653ad5b57be60ec3`。应先在目标中保留/建立相应父目录；此处只是恢复recipe，没有执行。

**c24b**：[notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/439d4f63a4e60e831f4655c27704fca081db2e09/topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json)

~~~sh
git show 439d4f63a4e60e831f4655c27704fca081db2e09:topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json > topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/twenty-four-condensed-warm/domain-operator/manifest.json
~~~

恢复范围仅该完整历史manifest；预期 650500 bytes / `d08e1ba67554e7aad58368820997186c4a0364e77aa28b8831986d3ffeb70676`，原Git blob `8a75bd0bdcb69b0c62e0069674f4d7694b3b53d5`。应先在目标中保留/建立相应父目录；此处只是恢复recipe，没有执行。

固定commit、完整source/request/parent、原producer版本、model、全部兄弟与真正artifact输入pin已同时保留。恢复本文件不重跑科学，也不承诺旧ZIP仍可下载。普通main删除不改写上述Git历史。

## 9. 本次实际范围与最终发布责任

本作者已一次完整读取实际76213-byte必要body，核其完整frame、SHA、官方run/job/source、实际search completion/errors/工作树；又按返回的固定小文件逐字核source身份并读取所有94行的具体上下文和真正I/O路径。没有把原650KB候选全文带入工具，没有保存任何Actions raw到Git，没有用旧25审计替代本次结果。

本说明支持的集合恰为第1节两条path；所有原sources、request/input、兄弟数组清单、gzip/数据、warm/status、原reader/producer及现有引用文档均保留。净容量按最终新增文本实数扣除，不预报200MB阈值已经满足。

root仍独占实际refs和删除。最终普通提交前，须沿本次固定439d到实际pull完整检查新变化：对这两候选再核原blob/bytes/SHA；对新增/变更的已选source/config/input按本次23个实际direct+generic文字分类检索，保实际未扫补集；不能把缺patch、未读generic或其它课题变动当零。root会把该真实最终delta范围另附本说明或同次行政记录。本文没有预付尚未发生的guard，也没有增加科学运行、测试或接受门。


## 10. 最后真实pull守护合同及新增R589来源判读

本节为root作者补充，尚未冒充未来guard回执。删除只由公开Actions行政分支做实际blob:none/sparse克隆、git pull --rebase origin main、双README差异核定和普通push。每次NFF立即重新pull/rebase、核规则并重新执行本节完整guard；不force，不将429/超时或未知返回当成功。

最终guard从本次真实固定439d4f63a4e60e831f4655c27704fca081db2e09到实际origin/main用完整git diff --raw --no-abbrev --no-renames -z取全部变化；所有新/变已选source/config/input读全blob，topic gzip解码全EOF，历史文本实际扫描并仅按原历史域列计数；所有被删/未选变化原路径、mode、blob显式列出。任何未扫变化、未解释的具体或generic source命中、读取/扫描错误、candidate全blob/bytes/SHA不一致或topic超200000000 B都停止该次普通删除。实际全必要report若超90000仍退出70，完整body未回返不能授权删除，不删字段或分片。

两候选最终实际main均重新读全blob核bytes与SHA256；这些大候选只在Actions内核，connector不读其全文。所有source hit保完整原文件身份及全部行/byte/pattern位置。本文fixed audit predicate之外的旧补集依旧是已声明未扫，不能称无引用；本节对新增未扫变化保守要求空。容量以f7d56b2da6e2c85f059f37277ad3026c31bb6667已核198569112 B为base，测量其后全部topic变化Git blob size，包含本次note/索引/H和仅这两删除，不用全tree -l。

root已完整读取本次fixed之后自己正式发表的R563/R571/R586/R580/R589全部新增source/config；R589之前这些新文件没有本次23个literal命中。R589中只有完整request246出现generic source-pin词：98952 bytes、SHA2565c48bf2add2def97a6f1d86dc85d6159822e035ce50d61ca42e2179dc3a924b0、Git blob8fa63defd52be07ab65379779bb404537f960737，路径computations/public-live128-named-necessary-original-full112-FD-fullDN-request.json。它的全部21命中都是/source_sha256下的原producer-source键；同一JSON pointer的每个值与完整冻结240 request97177/e4ad6178a06d2cf270f3469c4cbcce4747c8876e7c95c50f829be58c9f6c437a逐值相同。没有任何0–14具体candidate词，也没有新增consumer从main候选读取的代码。完整新增generator/plan/workflow也没有23词命中。

本节guard只对该完整path/blob/bytes/SHA允许已解释generic indices16/20/21/22（15个direct在前，再接本篇8个generic）；任何不同字节或另一路径不继承此解释。不是按basename、wildcard、旧检查通过或任意将来request号放行。

| 原246行 | /source_sha256键 | 原240＝当前246完整值 | 23-pattern indices |
| --- | --- | --- | --- |
| 86 | geometry_20261114_eighteen_query_domain_operator.py | ec43c049542f523e1c4f2b1956c07a9216497eb066a8f6f22ceddd8f11e2c051 | 16 |
| 87 | geometry_20261114_eleven_query_domain_operator.py | 55358acb92bac869ba2ca1daf2da7772d57be31ccd1fcfd9f7324af80f8ea20b | 16 |
| 92 | geometry_20261114_fifteen_query_domain_operator.py | c6581f0b8fdef4c3bc48d364c6845cff9a4244b043a4d14c772ef6fd3b2503e8 | 16 |
| 96 | geometry_20261114_fourteen_query_domain_operator.py | 049ab10d130c94d5b1849a2af3b0e3f4848819bb9b7af68230488c25ba778464 | 16 |
| 98 | geometry_20261114_full_angle_domain_operator.py | af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7 | 16,20 |
| 121 | geometry_20261114_mixed_query_domain_operator.py | 34115f81cf5a09c3d07a6b79f408459fb014ca580ad0a992f8a639ff937ba854 | 16 |
| 128 | geometry_20261114_nineteen_query_domain_operator.py | 945114799a2cf564c59b463e1429b55119d4ad421bc5f3414c7143333e43d35e | 16 |
| 155 | geometry_20261114_seventeen_query_domain_operator.py | 5bb4f214d4d2505185448a9162c0d995bdb6c37168e6d9542dfe6202e8f21a41 | 16 |
| 159 | geometry_20261114_sixteen_query_domain_operator.py | a92efa1735832d144cb65d617beb2d9018d7822f5cc7d3846d00757abfb2db2a | 16 |
| 161 | geometry_20261114_ten_query_domain_operator.py | 5c9b145862a4f12cbbc5334e1b96e540458a58908c4889b966979995700d5dbd | 16 |
| 165 | geometry_20261114_thirteen_query_domain_operator.py | d674a64e11cfac1f57f0c24166546a55045847633935dddb8ef53df4024d3cff | 16 |
| 169 | geometry_20261114_thirty_one_query_domain_operator.py | 44c82d410f1e52f45e6b87f9e9eb86b3aeccb0e937510f04561855360347128f | 16 |
| 170 | geometry_20261114_twelve_query_domain_operator.py | 6a428d2f8412659cbd318321aa992c3b4565ff41177131a9cc9d268c6fbb7b1f | 16 |
| 176 | geometry_20261114_twenty_eight_query_domain_operator.py | 25767045b9a26764bfdb89881832ec7da01de1ac86ebc491402c7b9801175cd0 | 16 |
| 180 | geometry_20261114_twenty_five_query_domain_operator.py | 55fe72b1bad9cf3ee26b1d29a1a6cefb7f0f62f2570d7703bb8f3dfcd01b2260 | 16 |
| 184 | geometry_20261114_twenty_four_query_domain_operator.py | 06933e9341664d63b5a9eaeb00998daa1be7b1c1d143a60f1ae2ef05efa9db36 | 16,22 |
| 188 | geometry_20261114_twenty_one_query_domain_operator.py | 0007a3dd345cb60172c75ef6490fa3f0bbcfdc178be90e532120302fc6c15a65 | 16 |
| 192 | geometry_20261114_twenty_query_domain_operator.py | 16157412cbb4af0d01ade0cb3e373413fda175059186ccf17ef3b1d727d27ce1 | 16 |
| 196 | geometry_20261114_twenty_six_query_domain_operator.py | b5b72fde97ece27c034a5f1ae3c81f0c0288b4092050f63e96296f764e7068c8 | 16 |
| 200 | geometry_20261114_twenty_three_query_domain_operator.py | 755d9bf2a01c5c417b28bfd265ee76712bba54a9fdeddf34ea56c4668abefe98 | 16,21 |
| 204 | geometry_20261114_twenty_two_query_domain_operator.py | 083abbf5e7f6dfede4f717d059192011e2ca4f895ff2f57e2d3760f49d06feb0 | 16 |

完整guard作者代码身份为10798 bytes / af69f12cf41289b7f683eac9b94918b8db8fa570bf7217ae2a780ed238f729d5；它随临时行政workflow保存，未放入main作为新的科学门。本节只是完整最后守护合同及已读source的具体解释；真实各次pull head、scan counts、全部guard必要身份、NFF与最终push/capacity回执在成功后另附，不能在执行前预填。


### 10.1 第一次最终delta的真实超限与具名行政列关系

第一次行政publisher实际run43897549903/job133405098678、workflowhead a7f2f819be19e5c57a5fdcb9caba4ddb086e28d4；源提交b7c326a26695c6a82765a18cc6b6d3cfb09525f4。它在2026-11-16 15:33:16.2691016Z及15:33:17.1184875Z真实pull后核已读5b02d2b878ab91e1f5bad59316c246657ef209c4，双README未变。15:34:10.4978914Z实际最终delta对象131809 bytes/SHA25633d367037e81f717dc2eaa31033afe913a9cc9a29c460af28db8003eb2a5dfe7超90000；只返实际descriptor、complete_body_returned=false、allowed=false、退出70。没有PUBLISHED_JSON、没有push或main删除；不能从这份未返正文猜其counts、matches或errors。

新一轮不复用该未返body，也不从其SHA重造值，而从同439d固定头到新实际pull完整重做全部扫描及候选全字节核。唯一表示改动仅为九个固定行政record family：all_changed_paths、source_scans、historical_scans、current_source_matches、reviewed_generic_source_matches、unresolved_current_source_matches、unscanned_changes、candidate_original_main_identities、topic_capacity.complete_changed_file_deltas。

这些全行按原键顺序分组，所有原列值逐行保留，只有完整canonical值完全相等才共享constant列；path列的完整原字符串统一列在同一body的complete_paths，其精确引用只发生在上述九族已知path字段。全record_count、原record_indices、columns及所有unknown/error/count/match原值均保，不遍历或编码任意树，不编码源文件内容、candidate全文或科学数值。其它原root/topic_capacity成员原样保留。

逆映射先按完整行列恢复九族原字典序列，再仅将path的单键RT4_actual_changed_path引用展开为同body的完整路径，恢复原数组位置及原键顺序；最后删除唯一新增relation成员。以原ASCII JSON insertion order、逗号/冒号separator、无附加LF canonical，必须恢复记录的原整个object bytes/SHA。有限列表的每个列值来自完整原行，constant仅全等时共享，故这项逆是逐字段原对象的精确逆；缺失字段不是null，空列表不是未运行。原allowed判定不改变，仍要求全部未知/未扫/错误为空与容量合格。

只有这个全候选body比全原body严格短才采用；新一轮若仍超过90000仍70且不发布。完整必要仍一份，未分片、抬限或删字段；实际第二轮范围和最终push回执仍需其真实终态，不能由本表示证明提前得到。


## 11. 第二次实际完整delta、精确逆与普通push回执

第二次行政publisher run43898233580/job133407510586，workflowhead ad40aa4c3568c15c1a62e9572ba4481c589fa309，来源提交687704e253104aaba1d8a76ba5bc50196a7a8707。2026-11-16 15:36:58.2907396Z及15:36:59.3465247Z真实pull后核已读bf30a01f2e26a906cb62f2b2482ae629019de42b，根README21bd547f56590b7f2dd279d0297efb289a9b2783及本题bff8aea253a9e6a7a4fac28d810ac454c5499fec未变。

| 此轮真正完整返回项 | 实际值 |
| --- | --- |
| 完整单body必要字节/SHA | 88874 / 55287e8df6d362bff43158bd7483b58e34b544c650dc2440a7bbe47892937093 |
| 同次原完整行政对象字节/SHA | 141568 / 4e6189aaf90da8ff7f6a3a0e1105982864c84cc6679392115a6a223481925a07 |
| 全部变化 | 138 |
| 全source/config/input完整扫描 | 56 |
| 历史文本完整扫描 | 79 |
| 先前已删除路径 | 3，均在其它topic；不是本次新增删除 |
| 未扫变化/错误 | [] / [] |
| source命中 | 21，恰为第10节完整request246的21条原source pins |
| 未解释source命中 | [] |
| 完整path catalogue | 211个完整原字符串 |
| 实际topic容量变更行 | 95 |
| 候选再核 | 两原blob、650502/650500及全SHA均准确相同 |
| 检索实现 | rg不可用，完整字节逐行fallback |
| 完整原allowed | true |
| 普通main push | 2026-11-16T15:38:07.1149659Z成功，无本轮NFF |
| 正式main | 8d1cfb2062e40c08ffd1334ea28fc0aab07f4f46 |
| 完整实际topic bytes | 198761353，小于200000000 |

root仅一次取第二轮终态行政日志，完整88874 body已回返；按本篇九族逆规则恢复所有原记录、完整路径、键顺序和其余原成员，其完整ASCII canonical字节/SHA准确等于此轮141568/4e6189aa。此为行政metadata的完整逆核，不是科学算术、科学fixture或新接受门。第一轮131809与第二轮141568来自不同实际pull头，不能混为同一个原对象或推断第一轮未返内部值。

此轮全部3个“先前已删除”地址是：topics/visible-flex-exact-nearby/notes/2026-11-12-actual-canonical-physical-constant-split.json、topics/visible-flex-exact-nearby/notes/2026-11-12-saved-circle-field-multidomain-budgets.json、topics/visible-flex-exact-nearby/notes/2026-11-13-R109-paired-E-and-compact-gap-budget.json。这里只完整报告固定439d到实际pull之间的变化，不认领这些删除，不对它们另作操作。

本次源提交和正式main只删除第1节两份24-domain manifest；原兄弟/所有真实输入保留。actual_proposed_head与最终main同8d1cfb2，工作树空。最终完整guard代码14432/fd69e9f9063bf919a0704a51f255f6493e8b814fd60c47aa3054a3fb7f997d6c；完整行政publisher21585/e58595bdb94bb8e25993aebb51974f2a5677b6166f1e2ab7848baec11220bce9，均在上述行政workflow固定head可恢复，main不新增行政workflow。实际raw/完整必要对象未保存到Git；这里是作者范围判读、完整身份与精确恢复责任。
