# 两份二十二／二十三查询历史域导出 manifest 的当前引用核对与固定历史恢复

作者：ChatGPT，/root/amplitude；日期：2026-11-16（UTC）。

**可信度：已证明，限本文固定树、实际扫描范围、已逐源追踪的生产／读取关系和条件性保留结论。本文没有执行新的科学计算，不证明任意动态或外部调用不存在，也不授权修改任何数学门。**

本说明建议在最终真实 pull 的新增引用核对完成后，普通移走下面两份历史 `domain-operator/manifest.json` 的 main 副本，并用其固定 Git 历史链接保留可恢复身份。只涉及这两个完整路径；原 warm、status、全部现存数组、gzip、源、request、followup、condensed-array-manifest 和历史读回均保留。两份候选毛字节为 **1,228,897 B**，净容量变化还须扣除本文和最终登记文字。作者未执行删除、push、dispatch 或 ref 变更。

实际证据来自一次新的公开 Actions 扫描。旧二十四、二十五查询的整理结论不充当本次两份候选的证据。本次两个大 manifest 全文只由 Actions 的固定稀疏工作树读取；没有通过连接器打开其 >100 KB 正文。后续源码解释只读取已知 <100 KB 的原源／保留元数据。

## 1. 两个候选的完整身份与唯一恢复点

固定扫描及恢复提交：`7af9e725e58983a740d3cb53c66b73166914e247`。固定仓库根 tree：`44045481ef78281ccfdec2f9206801f2318a8b5b`；固定 topic tree：`2334b1212456f1878f7ea3d55575aed8ac0d86c3`。扫描工作流自己的 head 与被扫描提交不同，见 §2。

| 候选 | 完整仓库路径 | bytes | Git blob | SHA-256 |
| --- | --- | --- | --- | --- |
| c22 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/domain-operator/manifest.json | 602356 | 7ee414b47e8304272bba5da7d728f4cc5d05d507 | a55ba6fc73873a9ae5de85c7e93d6250d872d30ffe3172b024ef3128151f06a3 |
| c23 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/domain-operator/manifest.json | 626541 | e66c6d341aefcc1a89015995af497d6a2bbeaba0 | 4d682aaeabf25e480ca1aeaeedbcce6504324cff8e28e4da007f0e15eae9390f |

两份原文分别可从 [topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/domain-operator/manifest.json) 与 [topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/domain-operator/manifest.json](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/domain-operator/manifest.json) 恢复。Actions 已按固定文件实际全部字节核验 Git blob 哈希、字节数和 SHA-256；这些不是由目录名或预期值代填的结果。

| 候选 | 原数学运行／request | 原 source commit | 原 request SHA-256 | manifest schema | 原 B model SHA-256 |
| --- | --- | --- | --- | --- | --- |
| c22 | 43656584956 / 72 | eff90c141df410e83e273d568e4b707903bf8df2 | bdeed8cf973e1c9d09462044d89dcb582da4cdd8231521359658e80eba22d5b9 | captured-twenty-two-query-original-RMS-and-collocation-midpoint-domain-v1 | caf431a6f00ee9429cacc37480952605b38b18abfa200e1673fe0fb888332574 |
| c23 | 43659610548 / 74 | 145d7a53ec05a64d39d0a36ac3e441e3475cb9bf | d3bc7e4adbf0b1036864a2f8c5344b413b5eca1043b7d2b1ef9bbfd7fc977920 | captured-twenty-three-query-original-RMS-and-collocation-midpoint-domain-v1 | 3f45cfe3e690d3e5c97f9712bcdeae3a973909d1d63acff2432ad443a3acaedb |

原 schema 标记的是当时实际捕获的有限域线性化，不是当前连续 C、完整闭面、native 或最终 full-DN 的接受证明。恢复这份 JSON 不会恢复它所列的科学数组，也不会重新取得原 warm 或创造新的接受状态。

## 2. 一次实际扫描、失败的连接器传输和原正文恢复

原只读审计的官方运行是 [43901415619](https://github.com/Rogerhu12/math-research-public/actions/runs/43901415619)，job `133418735831`，attempt 1，事件 `push`，created `2026-11-16T15:53:52Z`，最终 `completed/success`。工作流 head 为 `6d51f1491d3a3f8210c3ab4e41b568bc10b3d26a`，分支 `visible-flex-larger-twenty-two-three-manifest-audit-20261116`；工作流路径 `.github/workflows/visible-flex-larger-domain-manifest-audit-twenty-two-three.yml`，完整 42,657 B / `312bbf4a273f2691299037576fed0e016a2b44b436f67973ed870812aa910082`。其固定扫描对象仍是 §1 的 7af9 提交，而非行政 workflow head。

首次和第二次专用 job-log 连接器调用均只返回 `-32603` internal error，没有任何 Actions 日志正文。一次允许的官方 GET 工具回退返回 HTTP 400、端点不受该工具支持，也没有日志正文。这三次都不记作已读取原日志，更不据 job success 推定候选安全。

随后仅作标准 Actions API 只读恢复，没有重跑扫描。恢复工作流用本公开仓库的 `GITHUB_TOKEN` / `actions:read`，在读取前核原 repository、run/head/path、attempt、job 及原成功终态；对原 job 日志 API 只请求一次，302 后的 signed URL 不打印，跨主机请求不携 Authorization 或 API 凭据。它从唯一原 `BEGIN_FIXED_DOMAIN_MANIFEST_RETENTION_AUDIT` / 对应 END 帧中逐字取出原必要正文，校验原 `RETENTION_AUDIT_IDENTITY`、固定扫描头、schema、原运行身份和 90,000 B 上限；只去掉 Actions 行时间戳传输，不重新编码原正文。

恢复运行是 [43903425678](https://github.com/Rogerhu12/math-research-public/actions/runs/43903425678)，job `133425803611`，attempt 1，head `66cda18c2edf9cc9144493eff84793a33ebeab37`，created `16:04:33Z`，updated `16:04:46Z`，最终 `completed/success`。恢复源码 `.github/workflows/visible-flex-larger-retention5-log-recovery.yml` 为 7,970 B / `859a0d8207e1228a27ac19f765e61208c033b115ab05c0b141b054a2d7f1b2ef`。作者只成功读取该恢复 job 的终态日志一次。

| 真实层次 | bytes | SHA-256 | 可据此作出的陈述 |
| --- | --- | --- | --- |
| 原 HTTP job-log 全字节；由恢复 Actions 内部读取和计量 | 141761 | ac48e8e723e6ecb5fa57ab9af09ecc02381e9414bccaf8b078203c0abe177b42 | 恢复程序实际读取的原日志身份；不冒称本地拿到了这份 HTTP 原流 |
| 连接器返回的恢复日志解码文本，UTF-8 重编码 | 92018 | 61757db3eb027b52807750845d4e1c2fc9fc495bbc0db5fbe3a388d6dc304432 | 仅返回文本身份，不是 HTTP raw |
| 完整原必要帧正文 | 77014 | 1b8e8bd748eaae7ea8a90921763427bc7a52a9e09902bb379ca3a5e9db9ee856 | 与原 RETENTION_AUDIT_IDENTITY 同 bytes/SHA，全部实际返回，未超 90,000 B |

完整必要正文的原临时路径为 `/home/runner/work/_temp/domain-manifest-retention-audit/necessary.json`；schema 是 `fixed-head-twenty-two-three-domain-manifest-retention-audit-v1`。本说明使用这份完整正文的实际字段以及固定源文字，绝不把错误包装、overflow descriptor 或工作流成功标签当作其替代。

本次扫描和恢复都没有写科学 Git 对象、保存原日志／必要正文为 detached blob 或上传 artifact。本说明本身是作者对来源、用途及恢复责任的分析，不是对原 raw body 的另存副本。没有要求再次下载原科学 ZIP 或重新读取任何科学运行日志。

## 3. 实际读取范围、未扫范围与搜索完成责任

本次实际使用 partial clone / promisor `blob:none` 和 sparse checkout。树 inventory 的命令是 `git ls-tree -r -z --full-tree FIXED`，没有 `-l`，没有为了取得未选对象的大小而隐式拉取全部 blob。完整根 inventory 9,163,856 B / `96b1e26bb32505a58cedddffe5867cbf0ce2f479fecdb722584d0d598ebe2833`，共 56,141 tracked blobs；其中本题 9,556。实际已选本题文件字节合计 198,887,599 B；本题另有 43 未选 blob，大小未请求，因此这个合计不称作本题总容量。

选择规则是：regular mode `100644` 或 `100755`；下列文本后缀或精确 basename，另并入本题下每一个 tracked `.gz`。后缀为
`.py,.mjs,.js,.json,.yml,.yaml,.hpp,.h,.cpp,.cc,.c,.sh,.toml,.ts,.tsx,.md,.markdown,.rst,.txt,.ini,.cfg,.xml,.html,.css`；
精确 basename 为 `.gitattributes,.gitignore,.gitmodules,COPYING,Dockerfile,LICENSE,Makefile,README`。本题外 gzip、其他 suffix、二进制均按下表明确保留未扫。文件集合由固定 tree 和该完整 predicate 定义，不依赖可变 main。

| 实际集合／记录 | 数量或 bytes | 完整身份 |
| --- | --- | --- |
| 稀疏选择 JSON | 9849274 | 1a970d21fea47e4317158c0fd7cc11fc03e3be69b1a86071a6a63cb5ae4c77c7 |
| 完整 selected path list | 4923348 | a0824f488d7d5abd255561a66714de065e5371b2fc0b4dd256fa4a926376ad0f |
| 实际 current source/config/input：排除历史文档 predicate 与两候选自引用 | 31429 | path list 3639443 / 7599e6beae46c5988ed811dcf99bcbea151969e5c224f18914d78334ddfaa026 |
| 实际历史文档 | 12306 | path list 1272526 / 3f8133fd29ef8d05e3118200cfda317275de55693ad4e2d276ca620cfed7a8ab |
| 本题全部 tracked gzip，完整解码 EOF | 77 | per-file inventory 23962 / b15440a896a4d0a43f72ff4845aa8d231653087ac41bcf276f07357abb9f28f1 |
| 完整未扫 path inventory | 12327 | 2462095 / 16666879e39a2e4db93342fd4a47aaae9b6e4b9484ec1d6017ba585ae34da4c5 |
| 实际 Git sparse pattern file | 4879533 | 8d6d98ed22791b3113a29d7b81fc54ffad1b674018bedc22e118f272bdf93cf4 |

runner 上 `rg_executable=null`，实际 backend 是 `python-standard-library-complete-byte-lines`，不是一次没有执行的 rg 扫描。它以 rb 打开每个所选原文件，对每条完整字节行检查全部固定 ASCII literal；没有 import 任何科学源。全部 627 批的实际记录均返回，原 error 列表为空。唯一共享批次状态是实际 `exit=0, stderr_bytes=0, stderr_sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`；不是把缺失 stderr 补成空。固定批次序列完整可由下表恢复：每组前面的批次按首 index `120j`、count 120 排列，最后一批明确列出；实际各行均用上面完全相等的状态，组序依表不变。

| 批次 kind | 批数 | 全文件数 | 末批 first_path_index / path_count |
| --- | --- | --- | --- |
| direct-current-inputs | 262 | 31429 | 31320 / 109 |
| historical-documents-aggregate | 103 | 12306 | 12240 / 66 |
| constructors | 262 | 31429 | 31320 / 109 |

77 个 gzip 全部实际解码到 EOF，合计 decoded bytes 为 60,078,173；failed_files=[]。它们的所有高特异命中本应进入同一 direct_reference_groups，本次全部 18 组均为 tracked_file_bytes，因此没有 gzip 高特异命中。这个事实不是 gzip 内不存在泛来源名、数值或未知编码引用的证明。所有 gzip 自身一律不在删除集合。

### 3.1 完整未扫补集

未扫集合严格是固定 tree 中不满足上述 predicate 的 12,327 tracked blobs；每类 bytes 都是 `null`，不是零。完整路径 inventory 的身份已列出，未返回的路径正文不冒称已经逐项阅读。

| 未扫 class | suffix | 文件数 |
| --- | --- | --- |
| gzip_outside_topic | .gz | 6656 |
| other_suffix_or_binary | (no suffix) | 13 |
| other_suffix_or_binary | .cjs | 109 |
| other_suffix_or_binary | .csv | 1 |
| other_suffix_or_binary | .diff | 47 |
| other_suffix_or_binary | .gp | 37 |
| other_suffix_or_binary | .jsonl | 608 |
| other_suffix_or_binary | .lock | 201 |
| other_suffix_or_binary | .log | 4521 |
| other_suffix_or_binary | .mix | 56 |
| other_suffix_or_binary | .npz | 3 |
| other_suffix_or_binary | .patch | 8 |
| other_suffix_or_binary | .png | 1 |
| other_suffix_or_binary | .recipe | 49 |
| other_suffix_or_binary | .sing | 4 |
| other_suffix_or_binary | .spec | 10 |
| other_suffix_or_binary | .ssi | 1 |
| other_suffix_or_binary | .stop | 2 |

这些 .jsonl/.log/.recipe/.npz 等可能包含历史或其他用途的名字，本文不排除。任意构造路径、外部数据库、未来 source、编码文本也不由固定 literal 查找排除。推荐移走静态副本的依据还包括 §4–6 对实际生产和 artifact reader 的明确来源分析，以及 §9 的可恢复边界；不是以“未扫等于无引用”论证。

### 3.2 历史文档与泛 constructor 的返回边界

历史文档 predicate 是 casefold suffix `.md,.markdown,.rst,.txt` 或 basename `readme,license,copying`。实际扫描 12,306 文件，12 文件／25 行有命中。完整匹配文件 identity list 为 2,746 B / `6d77ba37092e019ef7345f5a0834d47f44fa0f23f0eed87cc7523cb2145084ce`（12 行）；完整匹配地址流 4,963 B / `a5e03f465dfe4df387ad6afbdf0629eaa9f9117e46fe3006d68f286c38e1e058`（25 行）。其逐文件路径和逐行地址没有在必要正文返回，不在本文冒称已读。它们保留在固定 Git 树，历史链接可按 §9 恢复，不用作可执行 consumer 缺失的负证明。

泛 constructor 对全部 31,429 当前 source/config/input 实际扫描；279 匹配文件、742 文件／pattern 对、4,160 地址行。完整文件 identity list 67,149 B / `bf11656ec9b1361a8b998bbcd952f2e0b230f272b9159ecc8d3bcbb38ad9de9b`（279 行）；完整地址 list 574,263 B / `5ea9d0f779cf17868e6341a24c20f9227c976ff6530bff9adcd0a2d5a09b508c`（4,160 行）。这里同样只返回计数和完整 identity，没有逐项泛地址正文。不能将所有 `domain_operator` 字样说成这两个候选的实际文件读取，也不能说泛路径已全部人工判为无关。

§8 给出全部 16 个高特异 literal、10 个泛 literal 及实际计数。所有当前高特异文件、全部 93 匹配行的行号／字节起点／整行长度／每次 occurrence offset 都在 §7 完整列出；作者据这些地址重新读取了相关 <100 KB 固定源／JSON，作出下文用途解释。


## 4. 真实生产链：新模型导出与 parent 输入分开

原 manifest 自述的输入身份如下。它们保留原 warm / prepared / accepted / tail config / zero anchor 的绑定；整理不能改这些输入，更不能由 SHA 恢复缺失值。

| 候选 | resume SHA-256 | source_prepared SHA-256 | source_accepted SHA-256 | actual_tail_config SHA-256 | actual_zero_anchor SHA-256 |
| --- | --- | --- | --- | --- | --- |
| c22 | 3f45b939752cbe338ab5037a481ee2639b40783950ca4664d23c8ff168f4d535 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| c23 | f59e8c64399a9fed392a8f8c3976209aaa3fa662c5c6ea65d864342cca697213 | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |

固定树中声明的全部 operator 依赖都实际逐字核了当前 identity。两套各九个声明源：共同的约束、Hermite、direction probe、full-DN、FFT、r225、full-angle 源保留；c22 的余两源是 twenty_one 与 twenty_two operator，c23 的余两源是 twenty_two 与 twenty_three operator。所有比较 `current_bytes_match_declared_source` 实际为 true。其完整 path/bytes/blob/SHA 在 §7 身份表 F0–F8、F15 给出。

除此以外，为说明实际调用而非只根据 manifest 字面判断，作者按固定 7af9 逐层非递归 tree 元数据取得下列原源的大小后，读取完整 <100 KB 文本并核身份。没有 import 或运行任何一个模块。下面的源码链接均固定到同一个提交。

| 实际原源（computations/） | bytes | Git blob | SHA-256 |
| --- | --- | --- | --- |
| [geometry_20261114_twenty_two_query_condensed_warm.py](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_two_query_condensed_warm.py) | 42120 | d80779d54d300a909163a5ea270018d4c0e06ad0 | 2b01d4384f312a435b4e00feb9296c93a15aebe063a29fe9c588ac230aaf867a |
| [geometry_20261114_twenty_two_query_collocation_observer_warm.py](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_two_query_collocation_observer_warm.py) | 16728 | e7bb216e4b48df421718cfed37ced1aff2479708 | 240837606d8b98214d25a6c0fe8b5546ce5b4994349bea39af32e96e22241ffa |
| [geometry_20261114_twenty_three_query_condensed_warm.py](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_three_query_condensed_warm.py) | 42436 | 1a64103722df5918bf75d420176f208eb9df8215 | 1fe5b698e452112583ee82a81ab7890095c7f3f31de05cdfb60c79e35039721c |
| [geometry_20261114_twenty_three_query_collocation_observer_warm.py](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_three_query_collocation_observer_warm.py) | 16736 | 134f5382c92f0d11c8fe467d4e43986686ec11da | 06ed3a98c48cbb2feffbc319f08c6509012f5ab9f7a460a5af3d6f74e73fc697 |
| [geometry_20261114_twelve_query_projection_warm.py](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/computations/geometry_20261114_twelve_query_projection_warm.py) | 15035 | 1afd743648100f1453760ce8e8540878991c4c08 | 10ed25405930f3775d8fb88f007aa50be4a53f4b3421904be959f1890ed67477 |
| [geometry_20261114_observed_seven_projection_warm.py](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/computations/geometry_20261114_observed_seven_projection_warm.py) | 13822 | 33c5918af48d4a2a40f1b06018a05ff2d3cb42d9 | 94395d54fcf58941180de23731fc2b5bb41fed8608dbda4c17903fffc862e228 |
| [geometry_20261114_seven_query_projection_warm.py](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/computations/geometry_20261114_seven_query_projection_warm.py) | 7431 | 60ad4327cb4057b8a070557b7ab53b37dc138c34 | f6598a5e4738f6c2c310eccc9fd791b68c3731ad3fc3adfd83414450d95c8394 |
| [geometry_20261114_full_angle_projection_warm.py](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/computations/geometry_20261114_full_angle_projection_warm.py) | 36439 | d1fe5e5f595c319dfde4752295709fa7acc16fb2 | 7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152 |
| [exact_20261114_fetch_pinned_public_artifact.py](https://github.com/Rogerhu12/math-research-public/blob/7af9e725e58983a740d3cb53c66b73166914e247/topics/visible-flex-larger-amplitude/computations/exact_20261114_fetch_pinned_public_artifact.py) | 28006 | 8ee390d0c1449a6a532d72158172af278f1c7cf3 | 51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859 |

调用关系按实际源如下。

1. 两个 `*_collocation_observer_warm.py` 的 `main` 只解析已有 `--out / --resume / --expected-resume-sha / --parent-status / --expected-parent-status-sha` 等来源参数，核各自数学 entry、原 collocation 与真实 engine SHA，暂装只读 observer 后实际调用 `entry.main()`，finally 恢复对象。它记录当次返回数组和来源，未把两份 Git manifest 当作 parent 输入，也没有以目录存在补造成功。
2. 两个 `*_condensed_warm.py` 的 `main` 与 `_run_engine` 真读 `args.resume`、`parent_status`，逐 SHA 核匹配；前者初始 parent 是 actual68，后者是 actual72，或其明确同 schema 后继。它们核原 status 的 latest warm basename 和完整 producer 来源。c23 中的初始 actual72 warm 是 `f59e8c64399a9fed392a8f8c3976209aaa3fa662c5c6ea65d864342cca697213`，不是候选 manifest，也不是其中任何数组名。父记录的完整准确身份在 §6。
3. `_run_engine` 将 `engine.FullAngleDomainOperator` 明确设成 `TwentyTwoQueryDomainOperator` 或 `TwentyThreeQueryDomainOperator`，将 capture/query 原方法一起绑定后调用真实 `engine.main()`。这条 engine 引用沿 `twelve_query_projection_warm.engine = observed.engine`、`observed_seven.engine = previous.engine`、`seven_query_projection_warm` 对 `full_angle_projection_warm` 的原 import，最终是 36,439 B / `7d75a44a…` 的原 source；不是以相同变量名猜测被调用模块。
4. 原 `geometry_20261114_full_angle_projection_warm.py` 的 `main` 从 prepared/resume/accepted/tail anchor 等真实参数读数据并核 SHA，建立原 state、同次 complete linearization/capture 和 domain。明确的导出接点是 `domain.export(args.out/"domain-operator")`，随后将真实返回保存为 `model["domain_operator_export"]`。它不是从 notes 中读旧 `domain-operator/manifest.json` 来继续模型。
5. 两个 operator 的构造器先 `capture.assert_matches(problem,state)`，在当次原 state/capture 上形成有限 B/Gamma/Pi；`export` 依次新写各 NPZ、保每个文件和数组 identity，再以 `manifest=self.description(); manifest["files"]=files` 写新 manifest。若输出文件已存在，它抛出原错误；不是读取旧文件当缓存。此时将 `self._factor_cache=None` 是该次完整导出后的原生命周期，也不建立对 main 静态 manifest 的新依赖。

原二十二查询有 22 个 typed query、45,056 个选中角行，二十三查询有 23 个、47,104 行；两者完整 B local dimension 都是 7,101。两者 15 个 left-RMS interval 是 `[466,467,468,469,470,471,472,473,475,477,479,480,481,482,484]`；c22 的 midpoint 是 `[473,475,477,480,481,482,485]`，c23 明确再有 484。本文只抄原已声明 metadata，不重算任何 query、方向、误差或接受结论。

两份原 followup 的完整文件继续保留。所选预算均为 overall 1200 s、candidate 600 s、trial reserve 90 s、recovery reserve 30 s、local working rows 512、dual sweeps 200、lambda 270、LSMR 200、projection sweeps 200、original trial count 17。原 `scientific_thresholds_changed=false`、`native_tail_requested=false`、`research_goal_completed=false` 也原样保留。没有把旧参数改成新运行计划；未选 request 字段全部仍在各原 followup 文件中。

| 候选 | 完整保留 followup | bytes | Git blob | SHA-256 |
| --- | --- | --- | --- | --- |
| c22 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/followup-request-identity.json | 21979 | 6dec04878fce0a5a8161360902e16c39b1eb9ca1 | 9954937addf1a71cb144a9f4f249e64df26958ea067456f07b4580a395f1e066 |
| c23 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/followup-request-identity.json | 23284 | 00655b565104f8e7cb5a9b8ee9164186f7876602 | 68904da796b9faffda4e2ed91db8776d189def971d5a509ea4e0f89152ba5e7e |

## 5. 真实读取链：artifact manifest 是必要输入，Git 副本不是该入口的数据根

不能说这两类 manifest “没有消费者”。固定树中的两个 completed-prefix reader 都有真实 `audit_domain`，会打开 `directory/"domain-operator"/"manifest.json"`，校验其 SHA 等于同一原 `model["domain_operator_export"]["manifest_sha256"]`，检查全部 typed query 顺序／shape／2048 角网格，并逐 `manifest["files"]` 调 `npz_file`，然后按每 query 的完整行、Gamma/Pi 和原 descriptor 组合核字节。其存在和原责任均保留。

关键是这个 `directory` 如何取得：

- `main` 要求显式的 original run、artifact ID/name、完整 ZIP size/SHA、原 source commit、parent directory/warm/status SHA、`--download-out` 和 `--out`。
- `fetch_original` 先按 SHA `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` 加载原公开 artifact transport；要求 metadata 的 workflow head 等于给定原 source，真正运行完整 pinned ZIP 下载／解包，核 success receipt、全部 PIN 和 ZIP SHA，然后返回 `root=args.download_out`。
- transport 的 `validate_output` 严格要求全新绝对路径位于当次 `RUNNER_TEMP`，父链无 symlink、目标不能已存在。它核完整 ZIP size/SHA 后安全解包、校验各原 member，按原 no-replace 流程发布并只读封存；不是选择仓库 checkout 的 notes 目录或从 Git manifest 补齐缺文件。
- `readout(root,out)` 才设置 `directory=root/WARM_DIR`，读取原 status、model、warm、FD 和 QP 报告；`audit_domain` 的根沿这条真实下载路径传下去。两处高特异 source 命中分别就是该 `WARM_DIR` 常量（F22 行46、F23 行45）。
- reader 的 `audit_condensed` 另外完整读取 sibling `condensed-array-manifest.json` 与其数组，属于保留责任；不因本次候选整理删除或跳过。

因此，保留这两个 source 的全部原逻辑、全部 original artifact pins 和相应保留文件，同时将 main 的历史 JSON 副本移到固定历史，并不改变已读入口所要求的实际 artifact 数据根。若原 artifact 已过期、缺失或被外部移走，不能用一个 Git manifest 的 hash 伪造完整重放；本文没有询问当前 artifact 下载可用性，也没有新取这两份巨大科学 ZIP。这是明确的恢复边界，不是以“旧 artifact 一定仍可下载”保证安全。

两条保留的 readback request 中实际 PIN 如下，全部文本按固定身份已读。其 request 自身不删除。

| 原 run / reader receipt run | artifact ID/name | expected ZIP bytes | expected ZIP SHA-256 | 原 source commit |
| --- | --- | --- | --- | --- |
| 43656584956 / 43658612002 | 14138023704 / visible-followup-condensedqp-43656584956-1 | 605047997 | 5948c9b4de7f02677382afcc67651f0d8332871aa551ae7f710d0acf0e0aa5b2 | eff90c141df410e83e273d568e4b707903bf8df2 |
| 43659610548 / 43660861684 | 14139672567 / visible-followup-condensedqp-43659610548-1 | 625544155 | 679504e5c7e7c933821b66fc4b0f4118395ee75e8d151b1c435d434002437134 | 145d7a53ec05a64d39d0a36ac3e441e3475cb9bf |

原数学的 source 字节、request、startup/free-space 条件、原审核字段和错误语义均不改变。我们没有重新证实上述历史运行的科学结果；本次只核其既有读取路径和保存身份。

## 6. 全部当前高特异命中的用途判读

实际 18 文件／93 匹配行中，**没有**完整候选 path 或 manifest SHA/Git blob 的当前高特异命中（两候选自身排除）；但有真实 producer-directory、原 run 和 B model 名字命中。下列分类由每个固定文件的实际相应字段以及 §4–5 的源共同支持，不以关键词缺失作为唯一论据。全部文件保留；§7 是完整原地址，§8 是完整 literal 表。

### 6.1 F22/F23：两条真正的 artifact reader

这两处实际是可执行源码，必须按 §5 保留。不能因它们只有一个目录 literal 而称作“纯文稿”。它们需要从原 ZIP 取得全部对应 manifest/数组；当前 main 的两份 notes 静态副本不被该 API 读取。此次整理不改 reader 参数或改为绕过缺失文件。

### 6.2 F24/F25/F26：primary identity readback 中的旧临时路径

`actual72-primary-identity-readback.json` 的 `/run_id` 及 `/files/0,1,2,3,5/file`；actual74 的对应字段及 parent72 的 `/files/7,8/file`；actual76 的 `/files/7,8/file` 是原已读报告、warm 和 status 的临时路径／identity。其字面路径以 `/tmp/visible-larger-actual72-published/` 或 `actual74-published/` 开始，指到 driver-status、model-000、condensed-QP-summary 或 warm-001，未指到候选 manifest。本文保留这些 JSON 原字，不把历史临时路径解释成当前 checkout 的自动 loader。

### 6.3 F27/F28：completed-reader addendum 中的原 ZIP、报告、B model 与原 raw descriptor

每份 29 行命中都已经逐字段读到：

- `/original_artifact_pin/run_id` 与 `artifact_name`；
- `/five_original_report_copies_verified/{0,1,3,4}/{original_file,artifact_file}`；
- `/four_previously_published_report_bytes_equal/{0,1,3}/file`；
- `/previously_published_actual_warm_verified/file`；
- `/byte_audit_scope/original_B_model_sha256`；
- `/root_raw_file_descriptors/0..13/file` 的全部十四原路径。

最后十四个是 `condensed-root/` 下的 original-g、local-indices、affine-original-linear-term-error、complete-affine-column、local-root、local-affine、local-gradient、local-center，以及 recovery-000 的 requested-local、actual-full、original-H-residual、local-mismatch、rhs、rhs-embedding-error。它们是既有数组身份记录，不是此次读取这些 raw 的动作。本次不下载它们、不删除任何尚存数组，也不从 descriptor 补出数组内容。

两 addendum 的 B model SHA 分别与本次两候选自述一致，但该等式仅指 `original_B_model_sha256`。不能将其他 `model-000.json` 的 SHA、完整 warm SHA 或 source SHA 与 B model SHA 混为一个对象；例如 c23 followup 的 `actual72_original_model_sha256=09f1d116d03ba7f3a69b65e94550e72bcb8afce84ef72bb498b8aa24e57fbe73`，下一级 c24 的 `actual74_original_model_sha256=75d3e63d4837a47816890ff49232aa43237b0b44d0531d63a6dbe57291fa2a26`，都不是本次候选 B model 词。

### 6.4 F13/F20：两个 sibling condensed-array-manifest 的真实模型关联

它们在行2133的 `/original_B_model_sha256` 分别是 c22/c23 的 B model SHA。这个关联有真实用途：原 condensed audit 使用它及独立的完整 array descriptor 核原 QP 数据。**这两份 sibling 不删。** 拟移走的是独立 `domain-operator/manifest.json` 静态副本；其原文由固定历史完整恢复。不能通过删除一份候选，声称另一份数组清单已无必要或其数组已核过。

### 6.5 F29/F30：completed-readback 的显式原 artifact 选择

全部命中为 `/request/original_artifact/{run_id,artifact_name}`，具体完整 PIN 已在 §5 表给出。它们选择原 ZIP、并声明 readback 是原有限导出数组的字节读取，不是新科学运行。保留 source SHA、minimum_free_bytes=4294967296、父 warm/status 和所有原完整 request；本次不把它们改到 Git notes 路径。

### 6.6 F17/F19 与 F31/F32：后继 warm 的实际父对象

F17 的命中是 `/request/actual_parent_run`、`/request/nearest_rejection/parent_run`、`/request/actual_parent_public_directory`；F19 是其 `/parent_run` restore receipt。F31/F32 同结构指向 c23 原 run。这里真实传给下一数学 entry 的是 warm/status 及 source 身份，不是域导出 manifest。完整明确的对象如下：

| 被后继引用的父 | warm bytes / SHA-256 | status 原 JSON bytes / SHA-256 | status gzip bytes / SHA-256 |
| --- | --- | --- | --- |
| actual72，F17/F19；source eff90c141df410e83e273d568e4b707903bf8df2 | 4837630 / f59e8c64399a9fed392a8f8c3976209aaa3fa662c5c6ea65d864342cca697213 | 2213797 / 73a0c0148f6166608ce47ecd4831b6e09a013e50907bfe7aae7468b687ce857f | 265087 / ca0d071817362575517592e703b15e37f7394e2a40876d5ccbe273bea946ede7 |
| actual74，F31/F32；source 145d7a53ec05a64d39d0a36ac3e441e3475cb9bf | 4849039 / 204b208393218923f8abf9a36b6f03d29306409155447f561b2c2f4c373001a3 | 2532904 / 09d944723fb6be152e90ba283fc44d33d455f1a52bc73787a329fcdc7d97ea73 | 291640 / b481c6154bb0359cb4e5e92144728f95acef4e82f0212045965e636d380dc608 |

restore receipt 明写透明解压并核原 JSON 字节，`original_JSON_reserialized=false`。这些父目录、warm/status 和 receipt 全保；目录名相同不能推出其下每一个历史导出文件都是后继输入。§4 的实际 entry 源说明其 resume/status 入口，本文没有运行该后继或代判其科学终态。

### 6.7 F33/F34/F35：冻结 entry 的初始父历史

命中各自为 `/request/entry_introduction_history/original_actual74_parent_run`，或 `/request/parent_frozen_entry_introduction_history/original_actual74_parent_run`。这些明确嵌套字段保留原 query entry 引入时的来源。三个 request 的当前 `actual_parent_run` 分别已经是 43661532089、43663293492、43666177645，不是该嵌套历史词 43659610548。完整原 source/参数不改；不能将嵌套历史 run 自动当作本次会读其 domain manifest 的可执行指令。

上述逐项解释穷尽已返回的全部 18 个高特异匹配文件。对于泛 constructor 的其他 279 文件，本文保留 §3.2 的实际扫描／未返回地址边界，没有把它们逐一伪称为已读源码。最终变动守护仍须由 root 对固定头后的所有实际变化完成；新增未知具体 reader 必须按真实文件再处理。


## 7. 全部原文件身份和高特异匹配地址

以下 F 编号只是本说明中的完整固定文件表。它不改变原文件 path、类型、字节或来源；每个文件的 mode 都是实际 `100644`。下面给出完整仓库路径。F9/F16 是唯一两个候选；其他所有行均保留。

| F | 完整原路径 | bytes | Git blob | SHA-256 |
| --- | --- | --- | --- | --- |
| F0 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_constrained_collocation.py | 18309 | deb4856235d2d57a7003495a0e15c748be41b9b3 | 70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8 |
| F1 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_hermite_domain_constraints.py | 23762 | 885ff3e6b69c44b2488e24afd11606a52fb42f87 | d9e004c827add0074c2e6dd6c854763c7157e5049cd5360c1f85ad440462f4ce |
| F2 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_full_angle_domain_direction_probe.py | 27821 | 5ff83a675e97bf5d70f9009e1e937e2ae86ac54b | 794788a17db22189b80d65b7def84f3515ca587ea59ffce96fe8887a071665e8 |
| F3 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_full_dn_augmented.py | 11311 | 05608a21d822a3150d0ac4fba656909f85c33b6d | f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e |
| F4 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_fft_frenet.py | 2143 | a6470e86bceae9c0406751a00793c77d77de2bfd | 973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401 |
| F5 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_r225_free_core_bvp.py | 23914 | 64ad4f0b9ca6b1edb4a46d27ff5f6b87154e3a95 | a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08 |
| F6 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_full_angle_domain_operator.py | 38319 | ce7849914e2abc4eb4a7130d705cd0531243cb24 | af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7 |
| F7 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_one_query_domain_operator.py | 32226 | dacd95feb7cdeb9d8113d261145d8ca86dbd7314 | 0007a3dd345cb60172c75ef6490fa3f0bbcfdc178be90e532120302fc6c15a65 |
| F8 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_two_query_domain_operator.py | 32106 | c40b1a0358be6e914e032e94a1cf6c77bb18734c | 083abbf5e7f6dfede4f717d059192011e2ca4f895ff2f57e2d3760f49d06feb0 |
| F9 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/domain-operator/manifest.json | 602356 | 7ee414b47e8304272bba5da7d728f4cc5d05d507 | a55ba6fc73873a9ae5de85c7e93d6250d872d30ffe3172b024ef3128151f06a3 |
| F10 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/followup-request-identity.json | 21979 | 6dec04878fce0a5a8161360902e16c39b1eb9ca1 | 9954937addf1a71cb144a9f4f249e64df26958ea067456f07b4580a395f1e066 |
| F11 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/T112-config.json | 2161 | 543d8364593985305438dda6a0c89b4b1a9c7ec5 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| F12 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/parent68/restore-identity.json | 685 | 4d429365f0984d7ec74cdba057eefef9b6396b30 | 8dc91eac77a817cf26c515fcf1fd71be056e4b0aa981f07d57899f0f0b9fdb4c |
| F13 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/condensed-array-manifest.json | 74717 | c10b330569929fcb1a1eabb9f4aa4f22998248c4 | 3cc8b4fe928e7af8216e1ffe18aa6c5c314943efcfea7d071ea6c6f0b9443fce |
| F14 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/optimization-intent.json.gz | 179601 | eb5233c835a2eb83569e318103a758bef58a7e3b | 01b0f8afa4d6ab70f0973dd8d00b44083443b56be04abef4ffc5f9e3dbc1a802 |
| F15 | topics/visible-flex-larger-amplitude/computations/geometry_20261114_twenty_three_query_domain_operator.py | 32291 | 3a0b545e3819abf515ec63e33f8fb234f0627705 | 755d9bf2a01c5c417b28bfd265ee76712bba54a9fdeddf34ea56c4668abefe98 |
| F16 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/domain-operator/manifest.json | 626541 | e66c6d341aefcc1a89015995af497d6a2bbeaba0 | 4d682aaeabf25e480ca1aeaeedbcce6504324cff8e28e4da007f0e15eae9390f |
| F17 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/followup-request-identity.json | 23284 | 00655b565104f8e7cb5a9b8ee9164186f7876602 | 68904da796b9faffda4e2ed91db8776d189def971d5a509ea4e0f89152ba5e7e |
| F18 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/T112-config.json | 2161 | 543d8364593985305438dda6a0c89b4b1a9c7ec5 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |
| F19 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/parent72/restore-identity.json | 685 | 85e26ffcc24b49dca30159dc1d218f09090cafb2 | f1929fae2986961aa00e3896aef1bb0cf6fdc396e4d8a9582404c01287209b76 |
| F20 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/condensed-array-manifest.json | 75262 | 1efff6eb1a46ae790850e8aacba0dba24cc6067c | a2269845b20498f645798e506cd1ab29f66e5270e2e1356f8610e9d72e443017 |
| F21 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/optimization-intent.json.gz | 191691 | d5a7156800d93e92a2daf8819a25101aa7b61097 | 506c4ccb939633551f9d43e3ccff2014c197dace7ccd017437e803b43d76cab4 |
| F22 | topics/visible-flex-larger-amplitude/computations/root_20261114_read_completed_twenty_three_prefix.py | 50265 | 5c8a809de5ba9cf8b535484ed59ed44664e2a553 | 528e5024d875a476fb5761db9d4adb6991d6e252d010117e273c1f35b93eba60 |
| F23 | topics/visible-flex-larger-amplitude/computations/root_20261114_read_completed_twenty_two_prefix.py | 49975 | 294ab306c9b5321765c5a519da23881b59588776 | f3a3570daaac6909f22990abddd70faab9677be6f77a3a2c37dd3c17a08668db |
| F24 | topics/visible-flex-larger-amplitude/notes/2026-11-14-actual72-primary-identity-readback.json | 25953 | 98cd15743d93c129926691af822601cab2820b57 | 447ccbde94295caba757e81fd3ddfb6a6bbe412bc0eca11aee8c2e279d492a3c |
| F25 | topics/visible-flex-larger-amplitude/notes/2026-11-14-actual74-primary-identity-readback.json | 26825 | d7c1cb5c07a783fb5af68766e9cb0dbed7784428 | 943e5ab8e05a22b63f4ca70dadda67fd99d33dc4cb928070b95b31b8bff6d355 |
| F26 | topics/visible-flex-larger-amplitude/notes/2026-11-15-actual76-primary-identity-readback.json | 27754 | 835da243ce7cfff1204fc098c9ef9a4e1232adab | 5c5bc17fe33c262369f822a66c18d7cbabeccc0b3a9df1bc9d7ef322e5e46eba |
| F27 | topics/visible-flex-larger-amplitude/notes/actual72-completed-reader-addendum.json | 51085 | c468e4997b62a65e7e251f08f71dca229c9909e9 | a37eeb45c05142c97a3f356aa054bef99c46491dd7ae40dfe5f872ba5e7b1f3e |
| F28 | topics/visible-flex-larger-amplitude/notes/actual74-completed-reader-addendum.json | 52951 | 25418c933ff14029ff2e71b2823f51ad53402413 | 6f30a1240de07f4fe77ebb5692e53cc4a5e92c40edb58a7c50f950fa70b19f11 |
| F29 | topics/visible-flex-larger-amplitude/notes/public-actions-43658612002-1-receipts/completed-readback-request-identity.json | 2305 | 1bf8467af89fecb473927ab00d06853b256adeda | 969bb0a852e914b2a9953e55d237f9a718da22243d028a33c0f0de8fbb5433ed |
| F30 | topics/visible-flex-larger-amplitude/notes/public-actions-43660861684-1-receipts/completed-readback-request-identity.json | 2306 | bd33e83c4cf789a31830f78afd22244237b7d63e | ac26ebe01b0ef94654fd15ce9b4601bf7cf2556fdec9fa1e425966acd5615e4a |
| F31 | topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/followup-request-identity.json | 24905 | 65e1907451649daf59abed540b609470b8bbc828 | d51f3a4e321f33b777ee435b9de59d12ce09e4741a3ecff4edd1d037474d7a3f |
| F32 | topics/visible-flex-larger-amplitude/notes/public-actions-43661532089-1-condensedqp/parent74/restore-identity.json | 685 | 2eafa535cd9d7a8f4002591535c42619d15325ec | 6649961c43f38f64e0bd60c0960178d778b96854c4c5e2ac0b451e06f9b10a84 |
| F33 | topics/visible-flex-larger-amplitude/notes/public-actions-43663293492-1-condensedqp/followup-request-identity.json | 26901 | 49f9bd332e0fb9fd013bbaf88f3cd4b1e8a949df | 816dabdcdfe43c8c4f36de9e68fa99c896bfff925444f2e4becead7788fa809f |
| F34 | topics/visible-flex-larger-amplitude/notes/public-actions-43666177645-1-condensedqp/followup-request-identity.json | 28528 | f4237e3126a3d0c65c00fe1eb1c08f35b17f8e0f | afba5a8235f844ff1a4742048041265b069016d732017667dff082d047ef4992 |
| F35 | topics/visible-flex-larger-amplitude/notes/public-actions-43668743515-1-condensedqp/followup-request-identity.json | 32085 | 72440382dd243506122fa259539a5f1031caec24 | b279bdf3a20cf129b4d35b98e4d2b97d18cd436f7794841648151199bb218531 |

### 7.1 全部 93 行的完整字节地址

所有组的 representation 都是 `tracked_file_bytes`。行号从 1 开始，行起点和 occurrence offset 是原文件字节地址；“整行 bytes”保原行长度。记号 `Pj@[a,b]` 明确表示 §8 的高特异 literal j 在该完整原行中的全部零基 byte offsets，多个 pattern 用分号分开。这是原必要地址的直接表述，不包含省略号、预览截断或未指明的余行。文件全文已由上面完整 identity 绑定；不要求在本说明重复整行原内容。

#### F22：§6.1：原 artifact 目录常量

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 46 | 1771 | 41 | P11@[12] |

#### F23：§6.1：原 artifact 目录常量

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 45 | 1693 | 39 | P3@[12] |

#### F24：§6.2：primary 收据

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 3 | 79 | 25 | P4@[12] |
| 11 | 527 | 101 | P3@[54] |
| 16 | 748 | 97 | P3@[54] |
| 21 | 964 | 108 | P3@[54] |
| 26 | 1191 | 99 | P3@[54] |
| 36 | 1624 | 104 | P3@[54] |

#### F25：§6.2：primary 收据

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 3 | 79 | 25 | P12@[12] |
| 11 | 527 | 103 | P11@[54] |
| 16 | 750 | 99 | P11@[54] |
| 21 | 968 | 110 | P11@[54] |
| 26 | 1197 | 101 | P11@[54] |
| 36 | 1632 | 106 | P11@[54] |
| 46 | 2073 | 99 | P3@[54] |
| 51 | 2292 | 101 | P3@[54] |

#### F26：§6.2：parent 收据

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 47 | 2193 | 101 | P11@[54] |
| 52 | 2414 | 103 | P11@[54] |

#### F27：§6.3：完整历史 addendum

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 33 | 1119 | 27 | P4@[14] |
| 35 | 1178 | 67 | P4@[51] |
| 42 | 1494 | 71 | P3@[24] |
| 43 | 1565 | 101 | P3@[54] |
| 49 | 1834 | 67 | P3@[24] |
| 50 | 1901 | 97 | P3@[54] |
| 63 | 2491 | 87 | P3@[24] |
| 64 | 2578 | 117 | P3@[54] |
| 70 | 2861 | 78 | P3@[24] |
| 71 | 2939 | 108 | P3@[54] |
| 79 | 3270 | 62 | P3@[15] |
| 85 | 3479 | 58 | P3@[15] |
| 97 | 3885 | 69 | P3@[15] |
| 104 | 4147 | 58 | P3@[13] |
| 168 | 7775 | 99 | P7@[32] |
| 546 | 19451 | 75 | P3@[15] |
| 557 | 19828 | 78 | P3@[15] |
| 568 | 20224 | 98 | P3@[15] |
| 579 | 20633 | 87 | P3@[15] |
| 590 | 21019 | 75 | P3@[15] |
| 602 | 21409 | 77 | P3@[15] |
| 613 | 21785 | 79 | P3@[15] |
| 624 | 22161 | 77 | P3@[15] |
| 635 | 22551 | 93 | P3@[15] |
| 646 | 22953 | 89 | P3@[15] |
| 657 | 23363 | 97 | P3@[15] |
| 668 | 23776 | 92 | P3@[15] |
| 679 | 24169 | 81 | P3@[15] |
| 690 | 24571 | 97 | P3@[15] |

#### F28：§6.3：完整历史 addendum

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 33 | 1112 | 27 | P12@[14] |
| 35 | 1171 | 67 | P12@[51] |
| 42 | 1487 | 73 | P11@[24] |
| 43 | 1560 | 103 | P11@[54] |
| 49 | 1831 | 69 | P11@[24] |
| 50 | 1900 | 99 | P11@[54] |
| 63 | 2492 | 89 | P11@[24] |
| 64 | 2581 | 119 | P11@[54] |
| 70 | 2866 | 80 | P11@[24] |
| 71 | 2946 | 110 | P11@[54] |
| 79 | 3279 | 64 | P11@[15] |
| 85 | 3490 | 60 | P11@[15] |
| 97 | 3898 | 71 | P11@[15] |
| 104 | 4162 | 60 | P11@[13] |
| 168 | 7797 | 99 | P15@[32] |
| 560 | 19883 | 77 | P11@[15] |
| 571 | 20262 | 80 | P11@[15] |
| 582 | 20660 | 100 | P11@[15] |
| 593 | 21071 | 89 | P11@[15] |
| 604 | 21459 | 77 | P11@[15] |
| 616 | 21851 | 79 | P11@[15] |
| 627 | 22229 | 81 | P11@[15] |
| 638 | 22607 | 79 | P11@[15] |
| 649 | 22999 | 95 | P11@[15] |
| 660 | 23403 | 91 | P11@[15] |
| 671 | 23815 | 99 | P11@[15] |
| 682 | 24230 | 94 | P11@[15] |
| 693 | 24625 | 83 | P11@[15] |
| 704 | 25029 | 99 | P11@[15] |

#### F13：§6.4：保留 B model 关联

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 2133 | 61391 | 97 | P7@[30] |

#### F29：§6.5：原 artifact PIN

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 10 | 357 | 29 | P4@[16] |
| 12 | 420 | 69 | P4@[53] |

#### F17：§6.6：实际父 warm/status 来源

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 62 | 7279 | 38 | P4@[25] |
| 130 | 9139 | 33 | P4@[20] |
| 299 | 14008 | 113 | P2@[45]; P3@[86]; P4@[60] |

#### F19：§6.6：实际父恢复收据

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 2 | 2 | 29 | P4@[16] |

#### F20：§6.4：保留 B model 关联

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 2133 | 61393 | 97 | P15@[30] |

#### F30：§6.5：原 artifact PIN

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 10 | 357 | 29 | P12@[16] |
| 12 | 420 | 69 | P12@[53] |

#### F31：§6.6：实际父 warm/status 来源

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 66 | 7835 | 38 | P12@[25] |
| 134 | 9693 | 33 | P12@[20] |
| 303 | 14542 | 116 | P10@[45]; P11@[86]; P12@[60] |

#### F32：§6.6：实际父恢复收据

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 2 | 2 | 29 | P12@[16] |

#### F33：§6.7：entry 引入历史

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 332 | 15880 | 51 | P12@[38] |

#### F34：§6.7：entry 引入历史

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 344 | 16539 | 51 | P12@[38] |

#### F35：§6.7：entry 引入历史

| 行号 | 原行 start byte | 整行 bytes | 全部 pattern offsets |
| --- | --- | --- | --- |
| 412 | 19567 | 51 | P12@[38] |

## 8. 完整查找词与实际计数

### 8.1 高特异 literal

以下16项次序与全部 Pj 地址一一对应，含两份完整 path、topic-relative path、run directory/name/ID、Git blob、manifest SHA 和 B model SHA。

| P | 完整 literal | 当前命中文件 | 当前命中行 | 全部 occurrence |
| --- | --- | --- | --- | --- |
| 0 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/domain-operator/manifest.json | 0 | 0 | 0 |
| 1 | notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/domain-operator/manifest.json | 0 | 0 | 0 |
| 2 | public-actions-43656584956-1-condensedqp | 1 | 1 | 1 |
| 3 | twenty-two-condensed-warm | 5 | 35 | 35 |
| 4 | 43656584956 | 5 | 9 | 9 |
| 5 | 7ee414b47e8304272bba5da7d728f4cc5d05d507 | 0 | 0 | 0 |
| 6 | a55ba6fc73873a9ae5de85c7e93d6250d872d30ffe3172b024ef3128151f06a3 | 0 | 0 | 0 |
| 7 | caf431a6f00ee9429cacc37480952605b38b18abfa200e1673fe0fb888332574 | 2 | 2 | 2 |
| 8 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/domain-operator/manifest.json | 0 | 0 | 0 |
| 9 | notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/domain-operator/manifest.json | 0 | 0 | 0 |
| 10 | public-actions-43659610548-1-condensedqp | 1 | 1 | 1 |
| 11 | twenty-three-condensed-warm | 5 | 35 | 35 |
| 12 | 43659610548 | 8 | 12 | 12 |
| 13 | e66c6d341aefcc1a89015995af497d6a2bbeaba0 | 0 | 0 | 0 |
| 14 | 4d682aaeabf25e480ca1aeaeedbcce6504324cff8e28e4da007f0e15eae9390f | 0 | 0 | 0 |
| 15 | 3f45cfe3e690d3e5c97f9712bcdeae3a973909d1d63acff2432ad443a3acaedb | 2 | 2 | 2 |

这些计数只是对 §7 实际返回完整地址的逐项计数。候选自身没有参加 direct scan；不能以 self 被排除造成的零，冒称候选内容不含任何关联。

### 8.2 泛 constructor literal 与实际计数

| G | 完整 literal | files | lines | occurrences |
| --- | --- | --- | --- | --- |
| 0 | domain-operator | 47 | 577 | 577 |
| 1 | domain_operator | 239 | 2824 | 2896 |
| 2 | condensed-array-manifest | 64 | 90 | 90 |
| 3 | optimization-intent | 65 | 90 | 90 |
| 4 | captured-twenty-two-query-original-RMS-and-collocation-midpoint-domain-v1 | 1 | 1 | 1 |
| 5 | geometry_20261114_full_angle_domain_operator | 112 | 285 | 285 |
| 6 | geometry_20261114_twenty_one_query_domain_operator | 79 | 109 | 109 |
| 7 | geometry_20261114_twenty_two_query_domain_operator | 69 | 95 | 95 |
| 8 | captured-twenty-three-query-original-RMS-and-collocation-midpoint-domain-v1 | 1 | 1 | 1 |
| 9 | geometry_20261114_twenty_three_query_domain_operator | 65 | 88 | 88 |

G4/G8 是完整 schema；其他 G 是广泛的目录/实现/来源名字。它们是泛构造扫描，不自动代表实际读这两个完整文件的对象。泛匹配完整 identity 和未返回个体地址已在 §3.2 明确保留。

### 8.3 历史文档完整逐 pattern 计数

历史搜索的前16项恰为上述 P0–P15；历史项16/17分别是 G4/G8。表中“行”可因同一行多个模式而重叠，不应直接求和当成25个唯一匹配行。

| 历史 pattern index | 对应 literal | matching lines | all occurrences |
| --- | --- | --- | --- |
| 0 | P0 | 0 | 0 |
| 1 | P1 | 0 | 0 |
| 2 | P2 | 2 | 2 |
| 3 | P3 | 4 | 4 |
| 4 | P4 | 8 | 10 |
| 5 | P5 | 0 | 0 |
| 6 | P6 | 0 | 0 |
| 7 | P7 | 2 | 2 |
| 8 | P8 | 0 | 0 |
| 9 | P9 | 0 | 0 |
| 10 | P10 | 2 | 2 |
| 11 | P11 | 4 | 4 |
| 12 | P12 | 9 | 11 |
| 13 | P13 | 0 | 0 |
| 14 | P14 | 0 | 0 |
| 15 | P15 | 2 | 2 |
| 16 | G4 | 0 | 0 |
| 17 | G8 | 0 | 0 |



## 9. 只移两份静态副本的条件结论、完整保留项与恢复方法

### 9.1 本次支持的操作范围

在 §1 的固定头上，完整具体引用及实际源说明以下有限结论：两个候选是从各自原有限模型导出的历史 manifest 副本；本次找到的真正 executable readers 以原 pinned artifact 的全新临时根为输入；后继 warm 链显式需要原 warm/status/input/source，并不消费这两份 Git notes manifest 来重建模型。因此，在最终 publisher 完成该固定头后全部实际变动的守护、且两候选仍逐字匹配 §1 的情况下，可以将且仅将 F9/F16 从 main 普通移走，保留其固定 Git 历史和此处解释。

这不是一个“所有动态依赖都不存在”的证明，也不是对任何科学结果重认证。没有改变原 reader 对 artifact 内 manifest/NPZ 的强制校验。若今后新调用者明确需要 main 的这份路径，应先用固定历史恢复其准确字节，或给出真实新的来源合同；不可只以旧 SHA 或目录名字假称该正文仍存在。本文不提供一个遍历目录批量删除的泛规则。

本次审计本身 `read_only=true`、`scientific_source_imported_or_executed=false`、`scientific_logs_requested=false`、`deletion_performed_or_authorized=false`；actual errors=[]、final_git_status 为空、repository_worktree_unchanged=true。删除权仍由 root 按本题已有授权实际执行；作者没有改变任何 ref。

### 9.2 所列科学 payload 的真实当前范围

| 候选 | manifest 原列出 payload 数 | 当前 fixed tree present | 当前 fixed tree absent | 完整 payload path-list 身份 |
| --- | --- | --- | --- | --- |
| c22 | 199 | 0 | 199 | 36346 / 54036f2a60fc6d6bd6341ef7d457c097c08f93554e523ec7f52fb9d0ca8ff6a8 |
| c23 | 207 | 0 | 207 | 38312 / 526527786346bfc3ad4f63d1ea0ec69e0a9713cd75352db80d491c91cf82f0dd |

这两个 absent 数只针对各候选自身列出的完整相对路径、按实际候选目录解析后在固定 tree 中查到的结果。不扩大成“所有旧科学数组已经不存在”，也不包括 sibling condensed-root 或外部 artifact。原 199/207 个 payload 的正文没有在本次必要摘要中返回；完整路径清单的身份保留，但不从该身份重新生成值。

固定 Git history 可靠地保留这两份已经提交的 JSON 字节；它不是所有原数组的备份承诺。原 artifact 可用性、外部持有的完整 ZIP、原 runner 临时文件是否仍在，都没有被这次行政任务重新验证。完整历史重放仍须满足 §5 的实际 ZIP/NPZ/parent 输入合同；缺任何项如实失败，不能用此次整理或 old completed 标记补过。

### 9.3 必须保持的实际 sibling

以下十项是 Actions 在固定树实际列出并完整核身份的 sibling；它们只是特别指明的保护项，保护范围还包括所有其他现存输入／数组／warm/status/source。每个实际 mode 都是 `100644`。其完整身份也已经在 §7 F 表保留，下面列出明确处置，避免只看相邻目录误删。

| 候选目录 | 完整 sibling path | bytes | SHA-256 | 处置 |
| --- | --- | --- | --- | --- |
| c22 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/T112-config.json | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 | 原字完整保留 |
| c22 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/followup-request-identity.json | 21979 | 9954937addf1a71cb144a9f4f249e64df26958ea067456f07b4580a395f1e066 | 原字完整保留 |
| c22 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/parent68/restore-identity.json | 685 | 8dc91eac77a817cf26c515fcf1fd71be056e4b0aa981f07d57899f0f0b9fdb4c | 原字完整保留 |
| c22 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/condensed-array-manifest.json | 74717 | 3cc8b4fe928e7af8216e1ffe18aa6c5c314943efcfea7d071ea6c6f0b9443fce | 原字完整保留 |
| c22 | topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/optimization-intent.json.gz | 179601 | 01b0f8afa4d6ab70f0973dd8d00b44083443b56be04abef4ffc5f9e3dbc1a802 | 原字完整保留 |
| c23 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/T112-config.json | 2161 | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 | 原字完整保留 |
| c23 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/followup-request-identity.json | 23284 | 68904da796b9faffda4e2ed91db8776d189def971d5a509ea4e0f89152ba5e7e | 原字完整保留 |
| c23 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/parent72/restore-identity.json | 685 | f1929fae2986961aa00e3896aef1bb0cf6fdc396e4d8a9582404c01287209b76 | 原字完整保留 |
| c23 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/condensed-array-manifest.json | 75262 | a2269845b20498f645798e506cd1ab29f66e5270e2e1356f8610e9d72e443017 | 原字完整保留 |
| c23 | topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/optimization-intent.json.gz | 191691 | 506c4ccb939633551f9d43e3ccff2014c197dace7ccd017437e803b43d76cab4 | 原字完整保留 |

原 parent warm/status 的准确大小和 stored/decoded SHA 已在 §6.6 保留。这些数字是原 restore identity 的记载；本次没有下载或重验对应巨大 warm/status 正文，更不会据一份 receipt 造出原数组。

另外完整保留：

- 全部现在的科学源码、request、input、当前执行工作流和 source plans；所有 41/54 array manifests。
- 所有 gzip、NPZ／原 raw arrays、优化意图、迁移／legacy／R456 来源及先前有非 MD 引用的 H。
- 原四 producers 与十一旧 log、当前本文列出的原 completed readers、所有 source map 和 readback/addendum。
- 任何原 warm、status、followup、T112 config、restore receipt 与两个 `condensed-array-manifest.json`。
- 已完成的 95 个 checkpoint、九项行政记录、旧二十四／二十五 manifest 的既有整理不再列为本次操作，也不将它们此前结论迁移到当前两个候选。

### 9.4 精确历史恢复，不重写原科学输入

完整恢复位置就是 §1 的 fixed commit。以下仅为以后确有需要时，在公开 Actions 新临时目录中取回两个已提交 JSON 的明确方法；本次未执行。前提是该公开仓库的固定 commit/object 已合法可读。保持原路径来源声明，不把该恢复输出当新运行产生的数据。

```bash
restore_root="$RUNNER_TEMP/retention5-historical-domain-manifests"
mkdir -- "$restore_root"
git -C "$GITHUB_WORKSPACE" show 7af9e725e58983a740d3cb53c66b73166914e247:topics/visible-flex-larger-amplitude/notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/domain-operator/manifest.json > "$restore_root/twenty-two-manifest.json"
git -C "$GITHUB_WORKSPACE" show 7af9e725e58983a740d3cb53c66b73166914e247:topics/visible-flex-larger-amplitude/notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/domain-operator/manifest.json > "$restore_root/twenty-three-manifest.json"
wc -c "$restore_root/twenty-two-manifest.json" "$restore_root/twenty-three-manifest.json"
sha256sum "$restore_root/twenty-two-manifest.json" "$restore_root/twenty-three-manifest.json"
```

期望返回准确的 `602356 / a55ba6fc73873a9ae5de85c7e93d6250d872d30ffe3172b024ef3128151f06a3` 与 `626541 / 4d682aaeabf25e480ca1aeaeedbcce6504324cff8e28e4da007f0e15eae9390f`。Git blob 分别仍是 `7ee414b47e8304272bba5da7d728f4cc5d05d507`、`e66c6d341aefcc1a89015995af497d6a2bbeaba0`。恢复只发生在新临时文件，不覆盖当前 checkout，也不导入数学模块。若要真实重新安装到当前主树，应按当时明确授权和实际 source binding 另作可追溯变更；本段不自动执行该操作。

原两 request 的完整生产 recipe、来源表和所有未选参数始终留在 F10/F17；当前保留的 artifact reader requests 是 F29/F30，原具体 ZIP 和 parent 选择在 §5–6 已完整给出。它们比一个孤立 manifest 更明确地记录原重放需要什么，但也不绕过原 missing-input 错误或资源门。

### 9.5 固定审计之后的最新 main

本作者说明的当前引用量词截至 `7af9e725e58983a740d3cb53c66b73166914e247`。它不把此后新 R581/R593 等文件自动纳入已扫描范围。root 的最终普通 publisher 应在真实 pull 后记录：

1. fixed head 至实际 pulled head 的完整 changed-file 集合，所有新增／修改 selected source/config/input 真实字节和身份，删除、未扫变化和任何 API patch 缺失不得当作零变化。
2. 本文16个高特异 + 10个泛 literal 的完整实际新命中；具体新 reader 要按真实来源解释。泛命中可来自已知 source_sha256 历史 pin，但必须给出同 pointer/同值／完整文件身份的实际证据，不能全局忽略。
3. 两候选依然同一 blob/bytes/SHA，所有保护项不在删除集合。
4. 实际普通提交与最终容量。若 publish 遭 non-fast-forward，真实 pull/rebase 后继续核新增 delta，不能把旧审核头冒当前头。

这些是最终已有删除动作的来源边界，不是新的科学验收门。本文到此没有填写未来 publisher head、最终删除结果或任何未来容量；root 可在下一节按真实事件补齐。

## 10. root 的最终普通发布方案与逐次真实 pull 守卫

维护：ChatGPT /root（AI），2026-11-16。第1–9节作者正文已完整；本节说明本次已有授权下实际准备的狭窄删除步骤，实际运行回执在成功后追加。本文没有以一个将来的检查填充当前成功。

行政守卫逐次以原固定扫描头7af9e725e58983a740d3cb53c66b73166914e247为起点，到本次真实 git pull --rebase 后的 origin/main，取完整 no-renames/no-abbrev/NUL-delimited raw diff。每项新或变更的 source/config/input 按原选取规则读取完整blob字节；本题gzip完整解码到EOF。历史文稿单独记完整身份/逐pattern计数；删除文件逐项记路径；所有未选变化和任何错误完整列出，不将其默作零。

扫描使用第8节全部16个高特异literal及10个泛literal，共26项，按P0–P15再G0–G9顺序。rg若可用先作固定字串presence，再逐完整字节行形成全部真实行号、字节偏移、行字节/SHA及全部occurrence；rg不可用则直接完整byte-lines。它不依赖GitHub compare的patch或line-count是否缺失。

本次没有预设任何泛source匹配豁免：RT_REVIEWED_SOURCE_FILES为空。若最新current source出现任一这26项的匹配，先完整返回具体地址并停止该次删除，作者按真实新文件解释后再作明确窄变更；不会整体忽略泛词。root对现成13份本题新增源码/计划/request/workflow作作者文本查找，实际均无匹配，但这不替代公开Actions对全仓库最新delta的完整扫描。

两份候选在真实origin/main分别读取完整blob、size、SHA256，并与第1节全身份比较。另对 origin/main 到本次实际proposed HEAD 的完整raw diff作独立操作范围核对：全部changed paths必须恰等于本次声明的发布文件集合，实际deleted paths必须恰为这两个manifest。所有其他source/input/warm/status/数组/sibling的删除均被该合同拒绝。正常更新只有本文、HANDOFF、open、results索引、log；没有新科学数据进入Git。

容量守卫采用已实际普通发布的b68c76fdaa24bc5c1d0ac0b1be8bb2dfc7414e1c为近端基点，其真实publisher43906289507/job133435918519返回actual_topic_bytes=199961745。该数已由原f7d56b2da6e2c85f059f37277ad3026c31bb6667/198569112基数加全部topic changed blob sizes实际算得。当前guard从b68到proposed HEAD列出每项old/new blob及实际size差，形成完整容量；普通publisher另保原f7基点的全delta容量守卫，两者不以单个selected-files合计替代整个topic。上限仍200000000、单MD<100000、HANDOFF<10000、open<30000。无需ls-tree -l或大blob连接器读取。

为完整返回行政delta，沿已明示的命名行族关系保存九类表：all_changed_paths、source_scans、historical_scans、current_source_matches、reviewed_generic_source_matches、unresolved_current_source_matches、unscanned_changes、candidate_original_main_identities、topic_capacity.complete_changed_file_deltas。每组保原字段顺序、每个原record index、所有原值；相同列可记同一常量，完整path列表只在严格path字段上索引。展开全部记录并移除唯一关系字段后，必须恢复原整个canonical ASCII JSON的bytes/SHA。新actual_publication_change_contract不参与变换，完整保原值。它仅用于这些明确行政行，不编码科学值、源文本、候选正文或任意树。

只有这个表示严格小于完整原对象才选用；整个必要正文仍受90000字节上限，超限诚实70且不push。完整体内所有错误、unknown、匹配、计数、顺序和未扫项都保。允许普通删除的条件是未解释current source匹配为空、未扫变化为空、errors为空、容量合法，且上面的两候选/实际删除范围合同均真。未取得完整guard体就不据一个SHA宣称已经读到其内容。

普通push遇non-fast-forward/cannot-lock立即真实pull --rebase，再核双README、记读取commit到HANDOFF、重做上述完整最新delta和容量守卫后普通重推；不force、不覆盖别人提交。若README有变，原流程打印差异并停止该publisher，root只读差异后立即按新规矩继续已授权工作。行政workflow只在专用分支，不进main。

本次行政Python仅标准库/Git读写与上述明确元数据核对，不导入/运行数学源码，不读科学运行日志，不重跑原审计，不上传artifact、不再存原77014B必要body或原HTTP日志。最后的实际run/job/head、每次真pull/README、完整guard身份/展开身份/范围与容量，以及普通删除是否成功，必须由实际回执补记。

## 11. 最终真实删除、完整必要回传与普通推送

本节按唯一终态读取的行政publisher [43907010619](https://github.com/Rogerhu12/math-research-public/actions/runs/43907010619)、job133438441644的实际回执补记。source commit为279a722b69e3d1ab257b70a55bc75a88e3d9ecf8，专用行政分支head为4adebe950036153ebd0300c573f50290aed01ac5。真实普通main结果为 **f370f6f013f2d80fd87466bab2638230a9d25d2d**。本次没有NFF；16:24:33.0043245Z普通push成功，status为空，无force。

16:23:53.169/53.607Z真实pull后的origin/main为e6025a7ed5d7a00489777157aa19bb540ae11247。根README 21bd547f56590b7f2dd279d0297efb289a9b2783、课题README bff8aea253a9e6a7a4fac28d810ac454c5499fec均未变，HANDOFF已记该已读提交。行政workflow没有进入main。

实际最终守卫源码14920B/SHA129b17e0465a8ef23ea73654a1827f86b0b260ed9095046839af7b099d6b19c7；包含原真实partial clone/pull/README/普通push的行政程序22073B/SHA0aef6852eea8ad7188d91fa117ebc5e0a4a7865705622d52eee4854ad1b1588d。第10节声明的固定头、26项模式、空豁免、两个候选、近端容量与仅两删除检查均是实际执行的这份源。

### 11.1 完整返回而非只读identity

16:24:10.132/10.159Z实际返回的整个RETENTION_TAIL_AUDIT必要体为 **64670B / 79ee414645b107e813c222c3b78191822f5d0150a75ee27741364e6293305666**，低于90000。全体已唯一读取；root从缓存正文解出RT5九个明确行政行族，逐项按完整索引/字段次序/常量或原值列/全path表复原，恢复原整个canonical对象为 **93733B / 5a4d31d30d848b754bf7fbc995ea94fe6013619aac5fe6a70eb5c904f2f47c77**，与实际关系记录完全一致。原对象没有另作Git、artifact或detached raw保存。

恢复仅是行政元数据关系，不是项目科学算术；没有科学数组或候选全文编码。打印的shell源码echo里同名print字符串不算运行frame，解析只取真正时间戳后的严格frame起点。此处没有第二次下载日志或重跑审计。

固定7af9到实际pulled e6025的完整delta共 **138项：62个current source/config/input完整扫描，67个历史文稿完整扫描，9个既有删除路径**。141个完整path在该命名关系中均有原字符串，没有把路径摘要当原地址。current_source_matches、reviewed_generic_source_matches、unresolved_current_source_matches、unscanned_changes、errors五项均实际为空，allowed实际为true。这里的零只针对这一次固定literal和明确新变化范围；第3节全仓库原未扫补集及动态/外部引用边界照旧。

那9项既有删除是另一课题visible-flex-exact-nearby的旧R133 compact floating报告，已经存在于pulled main；它们列在完整delta供审核，**不是本次root新增的删除**。本次没有改该课题文件。没有把GitHub比较元数据中后段缺失的patch或0 line-count当成没有变化；138项来自真实完整raw diff。

两候选在实际origin/main的actual_blob、actual_bytes、actual_sha256分别逐项等于第1节的7ee414b4/602356/a55ba6fc与e66c6d34/626541/4d682aae。对应完整字节仅Actions读取，未走大正文连接器。

### 11.2 实际发布范围和容量逐项变化

实际origin/main到proposed/final f370f6f0只有下列7个发布路径；declared_paths与actual_paths逐字同。实际deleted_paths与两个expected_deleted_paths逐字同，故所有其他input/source/warm/status/array/gzip/sibling不在本次删除中。

| 本题内路径 | 原字节 | 新字节 | 差额 |
|---|---:|---:|---:|
| HANDOFF.md | 8266 | 8025 | −241 |
| log.md | 22598 | 23136 | +538 |
| notes/2026-11-16-two-twenty-two-three-domain-manifest-retention.md | 0 | 65948 | +65948 |
| notes/public-actions-43656584956-1-condensedqp/twenty-two-condensed-warm/domain-operator/manifest.json | 602356 | 0 | −602356 |
| notes/public-actions-43659610548-1-condensedqp/twenty-three-condensed-warm/domain-operator/manifest.json | 626541 | 0 | −626541 |
| open.md | 26783 | 27440 | +657 |
| results.md | 19085 | 19445 | +360 |

实际近端b68容量199961745B，经全部上述变化后为 **198800110B**。普通publisher独立从原f7/198569112基点加全部topic变化也返回同一198800110B。两manifest毛释放1228897B；扣除实际完整说明和登记变化后的净减少为1161635B。本节后续追加文字会按下一次真实publication另行计量，不把初次65948B冒成本节补记后全文大小。

原引用链、两真实artifact reader和它们要求的原完整ZIP/NPZ均没有改；两个sibling condensed-array-manifest的B model关联照旧保。恢复路径固定7af9、所有未付科学职责、外部artifact可用性边界和历史原参数保持。至此本次只有两份main静态副本被普通移出，准确历史原文仍可按第9节恢复；这不是对其他旧raw的批量删除授权，也不是任何新的数学成功。
