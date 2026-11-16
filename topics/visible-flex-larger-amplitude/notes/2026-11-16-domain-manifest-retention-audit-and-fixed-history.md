# 两份历史 domain manifest 的当前引用判读与固定历史恢复

作者：ChatGPT（AI 协作者 /root/amplitude）  
日期：2026-11-16（UTC）  
可信度：已完成所列固定树、字面引用和明确调用路径的行政审计；不是任意动态依赖不存在的证明，不运行或接受任何科学结果。

## 1. 可执行的迁移结论

本次建议仅从未来 main 移走下表两份旧 `domain-operator/manifest.json`，合计 **1,456,843 bytes**。这里的“移走”是普通提交删除这两条当前路径，精确旧字节仍由已存在的固定 Git 历史恢复；没有历史重写。没有数组、gzip、科学 source、request 或当前输入进入该集合。本文完成时尚未执行删除，实际操作与固定扫描提交之后的新引用守护由 root 负责。

结论来自真实 r6 必要正文及下述当前读取/生成函数。当前保留的旧续算入口用父 warm/status；真正读取 domain manifest 的旧完整字节审计从其固定原 ZIP 的临时解压目录读取。两候选所列232和250个 payload 在扫描时的当前树均不在原目录内。故保留大索引不会使缺失的原科学现场完整，移走索引也不改变已核续算的输入。本结论不许删除那些 warm/status 或原科学数组，不声称所有可能的外部、动态或未来调用都不需要旧索引。

| 候选 | 完整原路径 | bytes | 原 Git blob | SHA256 |
|---|---|---:|---|---|
| c26 | `topics/visible-flex-larger-amplitude/notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/domain-operator/manifest.json` | 701874 | `51b52c3660ef47b47b12024f2932a3ca41927e47` | `3d2aa285471b58ccc859729366d26a8ca6332f5ece6eb8d88c423d97b062d0bb` |
| c28 | `topics/visible-flex-larger-amplitude/notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm/domain-operator/manifest.json` | 754969 | `613e0701158c163053a29253fcde18561c6dac91` | `6e983683817eaf153f20686f2aa2b12c05bd397e738172b7d5c675527ad68eac` |

精确旧字节在恢复头 `e6d389dfe1f79669f5b616497dc91bf92a70637d` 与本次扫描头 `d1956f73114f35a23d1d7caa323589fa8b7eb690` 均绑定到上表同一 blob。两个历史链接分别为：

- [c26 固定历史](https://github.com/Rogerhu12/math-research-public/blob/e6d389dfe1f79669f5b616497dc91bf92a70637d/topics/visible-flex-larger-amplitude/notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/domain-operator/manifest.json)。
- [c28 固定历史](https://github.com/Rogerhu12/math-research-public/blob/e6d389dfe1f79669f5b616497dc91bf92a70637d/topics/visible-flex-larger-amplitude/notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm/domain-operator/manifest.json)。

历史文稿中的旧 main 路径可由本索引转到这两个固定链接；本文不重写旧结论，也不将历史索引当作实际运行输入替身。

## 2. 真正执行的审计与返回范围

r6 是独立只读公开 Actions，run **43880461847**、job **133344650926**、attempt1、事件 push。workflow 位于临时 branch `visible-flex-larger-domain-manifest-audit-r6-20261116`，实际 workflow head 为 `d51d8dff185ae04937ba81671fd7dccdda429e62`。工作流文件 `.github/workflows/visible-larger-two-domain-manifest-retention-audit-r6.yml` 为42027B、SHA256 `d50f9d14d7b49e4976fe25b6682bc4a9141e510712833154dafd62694cb115c6`。

**扫描对象不是 workflow head**，而是固定提交 `d1956f73114f35a23d1d7caa323589fa8b7eb690`，root tree `d75ecdd73bcc7ba9c69fe3a26fc93946ae37f532`，本题 tree `50e5025f2aa8ebc94f693d001da37fbeb6b0653b`。真实配置 `remote.promisor=true`、`partialclonefilter=blob:none`、`sparseCheckout=true`；`git ls-tree -r -z --full-tree FIXED` 不带 `-l`，不会为了未选对象的 size 逐一取大 blob。

完整必要正文 **89713B / SHA256 `d9d1424a2729b31adc0f8815eba8507dc33c62e4d8856b0f599eebc8fe50d59b`** 已一次完整返回并读完。它在 Actions 内的原文件为 `$RUNNER_TEMP/domain-manifest-retention-audit/necessary.json`，schema `fixed-head-two-domain-manifest-retention-audit-v6`，frame `BEGIN_FIXED_DOMAIN_MANIFEST_RETENTION_AUDIT` 至对应 END。这里不把 run success 标签当作正文：实际正文报告 errors=[]、全部声明的 literal 扫描 complete、全部77份题内 gzip 解码至 EOF、最后 `git status` 原字节为空且 worktree unchanged。未执行科学 source、科学算术或删除，也未请求科学日志。

本次唯一下载的终态行政 job 日志，connector 返回文本 UTF-8 重编码身份为153598B / `2adeeafa04da958c5c4a2a667d27ff07e6d1211ea527a8ca29be3e3a8b8a4662`；这不是 HTTP raw bytes。root 未重复读取该日志。

### 2.1 完整 selection predicate 与实际后端

常规 Git mode仅100644/100755。文本扩展名并集为：

`.py .mjs .js .json .yml .yaml .hpp .h .cpp .cc .c .sh .toml .ts .tsx .md .markdown .rst .txt .ini .cfg .xml .html .css`。

再并入完整 basename `.gitattributes .gitignore .gitmodules COPYING Dockerfile LICENSE Makefile README`，以及本题路径下全部 `.gz`。在这个精确固定树上：

- tracked regular blobs：55,685；非regular为空。
- 当前 source/config/input partition：31,197文件（从已选文本排除明确历史文档 predicate 与两 candidate self）。
- 历史文档 partition：12,081文件；suffix为.md/.markdown/.rst/.txt或大小写归一后的readme/license/copying basename。
- 本题gzip：77文件，77全部解码完成，decoded bytes总60,078,173，failed_files=[]。
- 未选补集：12,328文件，其 size 明确为 null；没有请求它们的 blob size。补集完整路径清单2462280B / `7beab4bb53467f61042bc7d22c7238b46d78482d7fcf931bab77708ef0db510f`，只是精确描述未扫范围，不称其无依赖。

未扫补集为：其它题gzip6657；无扩展名13，.cjs109，.csv1，.diff47，.gp37，.jsonl608，.lock201，.log4521，.mix56，.npz3，.patch8，.png1，.recipe49，.sing4，.spec10，.ssi1，.stop2。其它题 gzip、数值数组及这些未选格式不被本结论概括为无引用。

实际 rg 不存在；真实后端为 `python-standard-library-complete-byte-lines`，逐个选中文件以rb读取每完整行并查每个ASCII literal，没有导入仓库source。621个实际批次全部保原kind/起始path index/path count；一个共享状态为exit0、stderr0B、SHA `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`。共享只在整个三元组相等时使用；逆为给每行前三值拼回其显式state_index对应完整三元组，原顺序不变，没有填不存在的批次或空stderr。

固定树完整metadata inventory为9094316B / `f43aedb69329cc3d15521562adf1d45ca8c42b95138cfcbb505064af907ee655`。选中全路径清单4876967B / `d97d0acefb74abdbcf9b2081a3f556db3f12331d86b3dbe5db964ab65374f1bb`。这些身份界定范围，不替代未返回的内容证据。

## 3. 精确字面量及其量词

实际高特异 pattern 数为 **16**，不是17。每候选依次为完整repo路径、topic相对路径、run目录、producer目录、runID、Git blob、manifest SHA、model SHA：

```json
[
  "topics/visible-flex-larger-amplitude/notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/domain-operator/manifest.json",
  "notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/domain-operator/manifest.json",
  "public-actions-43671882961-1-condensedqp",
  "twenty-six-condensed-warm",
  "43671882961",
  "51b52c3660ef47b47b12024f2932a3ca41927e47",
  "3d2aa285471b58ccc859729366d26a8ca6332f5ece6eb8d88c423d97b062d0bb",
  "b0dc7d5daf8344a07c07c7d53bd714c707ec3aceef9d3adee2fcf11004d2fc34",
  "topics/visible-flex-larger-amplitude/notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm/domain-operator/manifest.json",
  "notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm/domain-operator/manifest.json",
  "public-actions-43674854261-1-condensedqp",
  "twenty-eight-condensed-warm",
  "43674854261",
  "613e0701158c163053a29253fcde18561c6dac91",
  "6e983683817eaf153f20686f2aa2b12c05bd397e738172b7d5c675527ad68eac",
  "f04722650551ecb516d33fd680ba4c83a74e9a181609c5e457b7b29cf94aef4b"
]
```

下表是在已声明当前 partition 加题内gzip中，扣除candidate自身后的完整直接匹配；一个原行可命中多pattern，故列数不可相加作不同文件/行数量。

| pattern index | 实际文件组 | 命中行 | 全部出现次数 |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 |
| 2 | 1 | 1 | 1 |
| 3 | 9 | 424 | 427 |
| 4 | 10 | 24 | 24 |
| 5 | 0 | 0 | 0 |
| 6 | 1 | 1 | 1 |
| 7 | 1 | 1 | 1 |
| 8 | 0 | 0 | 0 |
| 9 | 0 | 0 | 0 |
| 10 | 2 | 5 | 5 |
| 11 | 7 | 17 | 17 |
| 12 | 7 | 15 | 15 |
| 13 | 0 | 0 | 0 |
| 14 | 0 | 0 | 0 |
| 15 | 1 | 1 | 1 |

总直接集合是 **23组、476个实际匹配行**，其中416行来自保留的旧actual89 transport gzip。候选完整路径/其Git blob零literal匹配，仅对本谓词/固定树成立；不能因此推出任意拼接路径、编码、外部或未来引用不存在。

另外 **8个泛constructor literal** 为：

```json
[
  "domain-operator",
  "domain_operator",
  "condensed-array-manifest",
  "optimization-intent",
  "geometry_20261114_twenty_six_query_domain_operator",
  "geometry_20261114_twenty_eight_query_domain_operator",
  "captured-twenty-six-query-original-RMS-and-collocation-midpoint-domain-v1",
  "captured-twenty-eight-query-original-RMS-and-collocation-midpoint-domain-v1"
]
```

泛constructor扫同31,197文件，实得282匹配文件、509 file-pattern pairs、3690地址行。逐文件身份清单67982B / `f7cf58202bddb1e6a9c3033b9e4a5ae8a5b8b224be7f659d66b3be7ecff4c121`；完整地址清单508678B / `a427d9b17966a9dc0883484c51c968848abaef1195f46c166f92310eb95bcd36`。本次仅返回这两清单完整身份及按pattern实际计数，**没有返回这282文件逐项路径/3690地址**，也不把它们一概认作两候选的运行读者。

历史文档真实扫描时另加入两schema，即18patterns；实得19匹配文件、50行。匹配文件身份清单4192B / `36a9b88c11bf6e164f1839a02bf077367fdb7fd6d49dc56551c21389878fd38b`；全部地址stream9661B / `2cb2b8f964b2fee4613928e0d3f5046a0116bf4950078b3dfc81ddf4cf1d214e`。正文没有逐项返回历史文档路径/地址，本文明确承认历史引用存在，以固定Git恢复索引承担旧引用责任，不称“全仓无引用”。

## 4. 全23组具体引用判读

下列地址是当前固定源的1-based行号；完整必要正文还保留每匹配行的原起始字节、完整行bytes及每pattern全部行内offset。作者按这些身份和地址读取相关源/JSON，并沿实际读取函数判读。下表用作者说明表达依赖，不重新刊原Actions输出或旧transport全账。编号对应r6完整文件表：

| 文件表索引 | 路径（本题内相对路径，workflow除外） | 全部匹配行或完整组范围 | 实际责任 |
|---:|---|---|---|
| 22 | `.github/workflows/visible-larger-public-condensed-qp.yml` | 82,83,84,306,345 | 当前旧 condensed 工作流的 sparse 选择与 PYPARENT94 恢复。实际只开 warm-001.json.gz、driver-status.json 或其 gzip，并向下一三十一 query 入口传 --resume/--parent-status；不打开候选 domain manifest。 |
| 23 | `computations/public-completed-readback-request.json` | 8,10 | 旧 request89 完整回执任务的原 artifact/run 名；其消费对象是精确固定 ZIP，经 --download-out 真下载。不是候选 main 路径。 |
| 24 | `computations/public-condensed-qp-request.json` | 87,96,529,553,571,686 | 当前保留的旧 request98：actual94 父 warm/status、两代 entry introduction history 及拒绝行来源；实际输入 tuple 与 manifest 路径不同。 |
| 25 | `computations/root_20261114_read_completed_twenty_six_prefix.py` | 46 | WARM_DIR 常量。audit_domain 确实打开 domain-operator/manifest.json，但 context 来自 fetch_original 返回的临时完整原 artifact；该历史审计的功能不能误称从不读 manifest。 |
| 26 | `computations/root_20261115_check_request98_static.py` | 124,131,132 | 旧 request98 静态脚本：替换父目录名并核 /tmp 的 actual94 warm/status；不以候选 manifest 为输入。仅阅读源码，未运行其 AST/compile 代码。 |
| 27 | `computations/root_20261115_check_thirty_one_sources.py` | 158,159 | 旧三十一 query 来源检查：读取实际父 warm/status，并核源与布局；匹配地址不读候选 manifest。仅阅读，未运行。 |
| 28 | `computations/root_20261115_read_actual89_complete_receipt_bytes.py` | 24,26,27 | 旧 actual89 回执附录。固定旧 /tmp 完整读回包；334–354 的 link 只比较 manifest/NPZ descriptor 与旧 transport inventory，明确不打开缺失 NPZ/f64。 |
| 29 | `computations/root_20261115_read_actual94_primary_bytes.py` | 19,22,23 | 旧 actual94 primary reader 的 run/WARM_DIR/PARENT_DIR；读取显式 --published-directory 的已下载 packet 及父 warm/status。没有这里两条候选 main 路径的固定依赖。 |
| 30 | `computations/root_20261115_verify_request98_static.py` | 73 | 旧 request98 字节检查的 /tmp model-000.json 来源；不读 domain manifest。仅阅读，未执行检查程序。 |
| 31 | `notes/2026-11-15-actual89-primary-identity-readback.json` | 17,22,28,33,49,247 | actual89 primary 结果的 model/status/QP/warm 文件身份及 run_id；这是保留的已产回执。 |
| 32 | `notes/2026-11-15-actual94-dispatch-source-crosswalk.json` | 18 | actual94 dispatch-source-crosswalk 的 run_id；保留的来源回执。 |
| 33 | `notes/2026-11-15-actual94-frozen-results.json` | 47 | actual94 frozen-results 的 original_run；保留的旧结论身份。 |
| 34 | `notes/2026-11-15-actual94-primary-identity-readback.json` | 17,22,28,33,49,292 | actual94 primary 结果的 model/status/QP/warm 身份及 run_id；保留的已产回执。 |
| 35 | `notes/2026-11-15-actual94-root-independent-byte-readback.json` | 4 | actual94 independent-byte-readback 的 run_id；保留的旧审计说明。 |
| 36 | `notes/2026-11-15-request89-complete-reader-root-static-readback.json` | 61,63 | request89 static readback 保存的原 artifact tuple；不是当前科学输入。 |
| 37 | `notes/2026-11-15-request94-root-static-readback.json` | 758,763 | request94 static readback 保存的 /tmp parent warm/status 身份；不是候选 manifest 的运行读取。 |
| 13 | `notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/condensed-array-manifest.json` | 2133 | 保留的 condensed-array-manifest 仅以 original_B_model_sha256 关联原模型；这个模型 SHA 不等于候选 manifest 文件路径或文件 SHA。 |
| 17 | `notes/public-actions-43674854261-1-condensedqp/followup-request-identity.json` | 87,96,498,528,643 | actual94 followup 保存 actual89 父目录/warm/status 和旧拒绝来源；完整 followup 保留，不将其参数删去。 |
| 19 | `notes/public-actions-43674854261-1-condensedqp/parent89/restore-identity.json` | 2 | parent89/restore-identity.json 的 parent_run；完整 warm/status 恢复回执保留。 |
| 20 | `notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm/condensed-array-manifest.json` | 2214 | 保留的另一份 condensed-array-manifest 的 original_B_model_sha256；仍保留该清单和其关联。 |
| 38 | `notes/public-actions-43676206729-1-receipts/completed-readback-request-identity.json` | 10,12 | 原 request89 readback 的运行内 request identity，保存原 artifact tuple；保留。 |
| 39 | `notes/read_actual89_primary_bytes.py` | 22,31,52,79,91 | 旧 primary reader 按显式 --published-directory 和 --parent-directory 读 packet/warm/status；源码保留。 |
| 40 | `notes/2026-11-15-actual89-original-transport-receipt.json.gz` | 416 个实际行；首34、末3386 | 旧 actual89 完整 transport 回执的 gzip 解码引用，共416匹配行（行34至3386之间，非连续范围声明）。包含 archive member 名及候选26 manifest SHA；它记录原解压成员身份，不能由哈希重建缺失数组。此 gzip 完整保留。 |

### 4.1 真续算输入与输出manifest分开

固定当前 `visible-larger-public-condensed-qp.yml` 在82–84仅稀疏选actual94的warm/status；301–352的PYPARENT94真正读取、验SHA/bytes、按原gzip透明解码并写parent94副本。353–371向原thirty_one入口传 `--resume`、`--parent-status` 及其实际SHA。其父目录同candidate28目录，只是目录相同；不能把目录引用等同每一个子文件都是运行输入。这里没有把domain manifest传给求解器。

原二十六/二十八入口将真实warm/status与prepared/accepted/tail-anchor交给原构造。原 `geometry_20261114_full_angle_projection_warm.py` 的main392–393读prepared/resume/accepted/tail_anchor；465为本次 `domain.export(.../domain-operator)`。原full_angle_domain_operator.export655–708、twenty_six.export467–516、twenty_eight.export479–528先导出本次NPZ，再由 `self.description` 和真实files写manifest。这证明这些producer路径写出新manifest，不能扩大成任意旧读者都不读取manifest。

已读取的四个原entry/producer文本身份为：

| 原source basename | bytes | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_six_query_collocation_observer_warm.py` | 16728 | `e10055b6e6d5604d247ecfbe637f8ca01b2b1337a7a528da8e25cbe48e6b8b25` |
| `geometry_20261114_twenty_six_query_condensed_warm.py` | 43689 | `b9954eb5caffca7e3e001e66b07b0628a8275a22139ca3000cf527e258023197` |
| `geometry_20261114_twenty_eight_query_collocation_observer_warm.py` | 16736 | `fc5a3e4b35557a7056d96cd7ade6756b861f3667e44aea83d51e4f5cd59c7dfc` |
| `geometry_20261114_twenty_eight_query_condensed_warm.py` | 46021 | `990029102808ede1134bd9e6a163b6da84ae0d9189857f49af216ba64bfa188c` |

这些科学source全部保留；未运行它们，未改变其任何原门。

### 4.2 确有旧manifest consumer，但它的来源不能被混淆

`root_20261114_read_completed_twenty_six_prefix.py` 的 `audit_domain`565–579确读 `context["directory"]/domain-operator/manifest.json`，验model descriptor并读全部声明NPZ。其 `main`861–877先 `fetch_original(args)`，后 `readout(root,...)`，再audit。 `fetch_original`191–238使用精确public-artifact transport与mandatoryrun/artifact/source/bytes/SHA，把完整原ZIP解到 `--download-out` 并返回这个root。因此这是真正的**历史完整artifact审计依赖**，不能删掉它的manifest后声称旧审计仍能直接运行；但它不是当前main这两条独立历史副本的读取路径。

保留的 `public-completed-readback-request.json` 绑定actual89 artifact14145231618、expected687750414B、SHA `e2859210d8baf814f4b6f88fbea5a0157ebbfce55c4c6a02429d4c64848c3583`，`recover_original_publication=false`。本审计未再下载它，未承诺它现在仍可在Actions服务取到。将来重放这个历史审计，需实际完整原archive/全部原payload；单从Git恢复manifest不能补齐它们。

`root_20261115_read_actual89_complete_receipt_bytes.py`334–354进一步明确：它只将旧audit记录的descriptor和旧transport inventory匹配，不重新读取缺失NPZ/f64。这个源及旧transport gzip都保留；其中记录的232files/原manifest身份不因迁移而抹去。旧primary readers按显式临时published目录/父目录读取自己的packet，本文不改这些API，更不把其历史metadata变成新科学接受。

## 5. 原producer、输入与参数保留

两个manifest各自原source_map有9项；合并10个不同source。r6逐个真实取当前文件bytes/SHA，全部等于各自声明值；完整current source绑定如下：

| source basename | 当前bytes | 原声明且实际相等的SHA256 |
|---|---:|---|
| `geometry_20261114_constrained_collocation.py` | 18309 | `70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8` |
| `geometry_20261114_hermite_domain_constraints.py` | 23762 | `d9e004c827add0074c2e6dd6c854763c7157e5049cd5360c1f85ad440462f4ce` |
| `geometry_20261114_full_angle_domain_direction_probe.py` | 27821 | `794788a17db22189b80d65b7def84f3515ca587ea59ffce96fe8887a071665e8` |
| `geometry_20261114_full_dn_augmented.py` | 11311 | `f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e` |
| `geometry_20261114_fft_frenet.py` | 2143 | `973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401` |
| `geometry_20261114_r225_free_core_bvp.py` | 23914 | `a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08` |
| `geometry_20261114_full_angle_domain_operator.py` | 38319 | `af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7` |
| `geometry_20261114_twenty_five_query_domain_operator.py` | 32768 | `55fe72b1bad9cf3ee26b1d29a1a6cefb7f0f62f2570d7703bb8f3dfcd01b2260` |
| `geometry_20261114_twenty_six_query_domain_operator.py` | 32954 | `b5b72fde97ece27c034a5f1ae3c81f0c0288b4092050f63e96296f764e7068c8` |
| `geometry_20261114_twenty_eight_query_domain_operator.py` | 33705 | `25767045b9a26764bfdb89881832ec7da01de1ac86ebc491402c7b9801175cd0` |

| 项 | c26 / actual89 | c28 / actual94 |
|---|---|---|
| 原科学run | 43671882961 | 43674854261 |
| 原source commit | `032c513ab5db8aff98a6efca2070375418846098` | `b75f41fa32b8ead9bb5121b725a0afe1a2f5ae5c` |
| 原request SHA | `a1a5bcd0a523d0903a0223c2b670eb4289e9d889bea95ff6b1c749f82aaba844` | `480f8d887402eb2c3b818c8fe672831019755f189d373f9ea09a6b3c4ab3af10` |
| 原model SHA | `b0dc7d5daf8344a07c07c7d53bd714c707ec3aceef9d3adee2fcf11004d2fc34` | `f04722650551ecb516d33fd680ba4c83a74e9a181609c5e457b7b29cf94aef4b` |
| 原父run | 43668743515 | 43671882961 |
| 原resume SHA | `d38c6968225535cb26c46c9dc3f9892603ef0c94942d9c571356fa016bccf69e` | `8985f7a5f146f0e98af04d5b1fc3d86648c7e6007403d9be54b1ed8ca4143fc9` |
| 原parent-status SHA | `7d6e7fa1fa3e92397d353f1e9b7c2a9c12d750f9714c2e79b1cfdfc40862a235` | `c78528682d239d941ccc1391df004c8da3b51d60b6315c6d30334828d0204540` |
| typed query / angle rows | 26 / 53248 | 28 / 57344 |
| complete local B dimension字段 | complete_B_local_dimension=7439 | expected_complete_B_local_dimension=8115 |
| manifest列出的原payload数 | 232 | 250 |
| 原路径payload当前存在数 | 0 | 0 |

不能把c28的“expected”字段改写成实际求解完成。原共用输入身份：prepared `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`、accepted `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`、tail config `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`、zero anchor `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`。

原两request的declared budgets均为overall1200秒、candidate600秒、trial reserve90秒、recovery reserve30秒、working rows512、dual sweeps200、lambda270、LSMR200、projection sweeps200、original trial count17。原selectedleft/midpoint intervals、完整query_specs、source tuple及其余参数仍在下表**完整followup原文件**中，不在本行政note重抄一遍科学输入；r6已明确selected键、原缺键保持缺键、未选其余字段仍由原完整文件保留。原scientific_thresholds_changed=false、native_tail_requested=false、research_goal_completed=false都不提升。

232/250个原导出path清单的身份分别为42520B/`52b5a87c7c7641c003a46b700871d0cbab7039d263928c9128b1a632e1bbf5d3`和46344B/`1bf36136c9005a2dd2b3d7c01bcb06bd6ff4703f4c9aafa96524eea1efab17cc`。r6在当前固定tree查这些路径，均不在；这只说明既有缺失，既不新删数组，也不声称原数组被重新验证。

### c26 保留的五个同目录记录

| 原路径（相对本题） | bytes | SHA256 |
|---|---:|---|
| `notes/public-actions-43671882961-1-condensedqp/T112-config.json` | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| `notes/public-actions-43671882961-1-condensedqp/followup-request-identity.json` | 32099 | `26e828589423cf91040e972c535aff7bba96fe7576ebbe9eb148a6ced2c874f5` |
| `notes/public-actions-43671882961-1-condensedqp/parent86/restore-identity.json` | 685 | `6e0a7980212a214ceac8c7a80148646e87e7352db8dfd6da0457a000cc229254` |
| `notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/condensed-array-manifest.json` | 76985 | `956a9525945d821ee0478e4bb0fd3479792e96dd31e1287d2a3920b767555285` |
| `notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/optimization-intent.json.gz` | 260060 | `3c03551b8ca819a48300b799fa77a23ca248c8f88837eed3d19cfe2f8a7b1efa` |

### c28 保留的五个同目录记录

| 原路径（相对本题） | bytes | SHA256 |
|---|---:|---|
| `notes/public-actions-43674854261-1-condensedqp/T112-config.json` | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| `notes/public-actions-43674854261-1-condensedqp/followup-request-identity.json` | 39230 | `81c457b58c777b6678badfd1043d0c1a542563cb92c472fdf019aaa0e98563c8` |
| `notes/public-actions-43674854261-1-condensedqp/parent89/restore-identity.json` | 685 | `b43cc9c01887d4388612b89c3d03530774cc59fd8870530285e929d2b7592ed3` |
| `notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm/condensed-array-manifest.json` | 82437 | `04d51029bd230ae6723c28ebc5a42e77d421571a95163183d875224d45ef26c1` |
| `notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm/optimization-intent.json.gz` | 273988 | `2299c942f74e7bc57feda62ec90a29205d9efaf4d76242338224dd890e6b1ca1` |

## 6. 全部审计尝试及未返回边界

六个版本都是独立临时branch的行政push；没有派发科学、修改main或执行删除。下列“attempted body”仅在明确实际返回其描述符时登记；失败全文没有返回即保持未读，不能借后一次成功补成前一次已读。每个行政job的终态日志由本作者唯一取一次；root没有重复读。r1的取消控制日志例外由root唯一读取。

| 版本 | 实际run / job | workflow head | 固定扫描head | 实际范围与必要正文 |
|---|---|---|---|---|
| r1 | 43875316393 / 133326721690 | e35f4018f337b52aa5f224a3c40677569cdbbc1c | e6d389dfe1f79669f5b616497dc91bf92a70637d | partial/sparse准备被精确取消，扫描未起，无必要body。原两处ls-tree -l可能拉未选blob size，未将准备完成伪填。 |
| r2 | 43876493640 / 133330794832 | d2158a86591f04b57f1fb40e87da3f14c81f619d | 同e6 | 去-l，partial/sparse成功；扫描后candidate变量覆盖selection，原KeyError 'unscanned_scope'，无完整body。 |
| r3 | 43877200322 / 133333219886 | d81c24c76b6d4cc9f5603153ca5719cd9850cab9 | 同e6 | 修两变量，attempted299716B / 09bc95c19252df8ecb0bf25fa7afb90f1eaff3f292aec0bd51de2132e4c38e96，原90KB门→70；只返descriptor，正文未返。 |
| r4 | 43878219911 / 133336795039 | 27ac3f6c1521a69fee7203f3cb2f2cfca5d49732 | 同e6 | 去preview并共享constructor文件表，attempted209282B / e174d62e06fe8322e0a1dacad81774df3e11e1f032786804e8ffd4cfe5bcf85c→70；正文未返。 |
| r5 | 43879526439 / 133341368186 | 5f92c6018817e79bd5bded05c099ba397ab3deea | 6a520319b255d63f5fe4eebcb7d94e584d91b088 | 历史文档明确aggregate，attempted213144B / a66e91c2385de4a0c469271e265505f3d194efc1eaa66b345cdf214d1f48e7cd→70；正文未返，返回实际字段size诊断。 |
| r6 | 43880461847 / 133344650926 | d51d8dff185ae04937ba81671fd7dccdda429e62 | d1956f73114f35a23d1d7caa323589fa8b7eb690 | 上述新必要scope与具名批次共享；89713B / d9d1424a2729b31adc0f8815eba8507dc33c62e4d8856b0f599eebc8fe50d59b，完整返回/读完，所有声明扫描complete。 |

r1控制run43876419867/job133330544786由root精确核旧run/head/path，2026-11-16T13:30:34.7269207Z只POST一次cancel，HTTP202；它不是科学run，root已给行政记录。r1准备step随后cancelled，scan skipped。本作者没有重复该控制log。

r5真实诊断字段：file identities72654B/302项，actual command records64731B，candidates25809B，constructorindex19505B/282files509pairs，direct13673B/23groups476lines，history2597B/19files50lines。这是r6把泛constructor改成明确aggregate身份、把重复同一空stderr状态具名共享的依据；没有把前一213144正文拆片、编码或提高90KB，r6也不承诺原未返泛地址已经读到。

全部原终日志身份仅指connector返回文本的UTF-8重编码，不冒HTTP raw：

| 版本 | 返回文本bytes | SHA256 |
|---|---:|---|
| r1 | 11715 | 3f1fe368448df2f15521b0538b71350765cf6d9ec6f9d9940ebc4071c9298e23 |
| r2 | 49300 | 610f3570e10728fc97c09d51939456083e39c33f51bee5dc1def6d20ec917d4f |
| r3 | 49703 | 0519e55de8de659c9cb4a2b4524613a10e48249ac0748bd2474aec4f5aab9248 |
| r4 | 49996 | 842dbce9b82e8cf1070e067145ad4c41514032f9b396810f8c57bc83fe14182c |
| r5 | 59850 | 48e6a079882c04ce821bba4f32a79d74a9a05148022820099aa211fffcc68377 |
| r6 | 153598 | 2adeeafa04da958c5c4a2a667d27ff07e6d1211ea527a8ca29be3e3a8b8a4662 |

## 7. 直接引用文件的完整身份

这23组均保留，不在删除集合。数字是§4文件表索引，完整path和解释在§4，避免将run目录名偷换成manifest输入。匹配的源/JSON均按完整原文件身份定位；gzip对应存储字节身份，实际匹配地址位于解码字节流。

| 索引 | bytes | Git blob | SHA256 |
|---:|---:|---|---|
| 22 | 27554 | `f998c08cc5320559204b7b2d5a67f4f2f1afdc99` | `7b8091cdedcf601bdd678c6b0a8c25b5d65b56ea86bed67db2fa7816a845aa92` |
| 23 | 1685 | `6e619d7a2954e683c92aadc7891e4b655a695da4` | `3ac6ac20b7f993b9a71900283738f3dcf1758056823e88450e8bfc569345dca9` |
| 24 | 27611 | `6aa7cc61e52b314c31699e8849fb9a9cc5c11b62` | `de47834ecc9f81437ae5bb5efb18a3368cf1b5006f2f6627d821e06c32a1df2d` |
| 25 | 50510 | `c34b85f1b8fc554574bffb2b46033d4bd374b0d6` | `36743c90d689525b975cec0acc66cdfa8051588ff8ce38f61e52120ad94c8527` |
| 26 | 10947 | `4cb3fd609beaaff3bd4f725326302f5e62edad78` | `8857e952a07df2a850fa074717661c601f6041d6ea303040b9375d3237966a00` |
| 27 | 11442 | `4d01377f1cbf3d0c5685176cf7c80ce616c389b6` | `3a443b6fc680fa2a937186ecbc07cf000834e23185b3e6ae2e641d63a4688111` |
| 28 | 33475 | `8806f70125b98fba38106b24f9d504ef8d5d3505` | `568a2f4f9e05ea99b9bebb287983d0c010207bc8e0143532b21cbb6f2e40ccc5` |
| 29 | 25836 | `45c492970ee7fb813ec3c6faa018941eb2c9ddef` | `35c9c98beee3b8bd33314b814652036e0ff9534bd551ff3483aa4222cc84c3bc` |
| 30 | 6290 | `7a8ecbee4deea4e65c806fb9e7578ac1d9e73a7d` | `f6d2f454efad44263afd281c46584ad17fdb6f0e78d0cdbd463808fa7b644cab` |
| 31 | 35922 | `bd32fb6d7e91bbabbe13756e7c7d89171bb7c8b3` | `118e377166cfbe9f55aa9b98c3ed8411525bcfbcf269b73426477c225dff3438` |
| 32 | 16837 | `bf9b09423dacd1b517060a21fd370dec43fad2a0` | `293a48526e1030de94f2022738509b1823ebadbb39b0062ecbaf031d626ecdc9` |
| 33 | 1824 | `4d141076f4a4d2070867637ecc9dc79249076234` | `775ad840948d9d2038cd9c774f6360e8c254c2a203be96751c5f04853f77d79b` |
| 34 | 33778 | `d1fd4a440028a2be251849a5f604f4a926720fca` | `19b656a9b806253c557fcdd4790e82d7c1524d14c5aec357eab4572cb33bac9f` |
| 35 | 798 | `5a1686989b9a4205f97a6361bf16343e0b8d55b1` | `16007d505eb6b9ab9cf013c12e39c7ae408a8388010ba5723424d013172e2b33` |
| 36 | 2868 | `86a53e04ab5d2a7e60be983fcd08fb292da0b05b` | `8f82b75ce14e2790ffa79a7866e12bc3361171764174e408bf42330394b3df78` |
| 37 | 39287 | `1193325200c687ec011e638ff870a3561d096830` | `df8c2372e16e4e5c822daa9c276756c346c200b79bef0198f49403524d5fca78` |
| 13 | 76985 | `ee768f7c5e5fb5dd46f54efdd176186031a85763` | `956a9525945d821ee0478e4bb0fd3479792e96dd31e1287d2a3920b767555285` |
| 17 | 39230 | `ff7e5871300ebfea3902f3545a735d8235c4daa0` | `81c457b58c777b6678badfd1043d0c1a542563cb92c472fdf019aaa0e98563c8` |
| 19 | 685 | `65a02d8b345587e9f78232428a4c92211eaee3d9` | `b43cc9c01887d4388612b89c3d03530774cc59fd8870530285e929d2b7592ed3` |
| 20 | 82437 | `e9dd485a7a84db74efd0b224e87132ee99173d57` | `04d51029bd230ae6723c28ebc5a42e77d421571a95163183d875224d45ef26c1` |
| 38 | 2595 | `64cc5ac9fd4416e65bbb42f161b045fdf918d3fa` | `de14cea4b2ed231b63da867411cb52483e341936479d2236aa65c2f85366afa1` |
| 39 | 9494 | `637f7d2d77b3714a6ed588cf637aa53e5b648181` | `2bfad303c3e86c9b47748b1f6bd3ece059b5ac79fbc523862ba60e7d57e776a8` |
| 40 | 25760 | `0fe0e18fdbfbe3d19582c63bc5b4813cbfda8118` | `9c83bad1c5dd2c659bb6091ac59e3d16b30e98c8de58215bae200c3a4a84443d` |

## 8. 恢复与最终提交责任

恢复只需已存在公开Git历史，不需要本次Actions raw。对每个候选原路径先建立其父目录，然后使用：

```sh
git show e6d389dfe1f79669f5b616497dc91bf92a70637d:topics/visible-flex-larger-amplitude/notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/domain-operator/manifest.json > topics/visible-flex-larger-amplitude/notes/public-actions-43671882961-1-condensedqp/twenty-six-condensed-warm/domain-operator/manifest.json
git show e6d389dfe1f79669f5b616497dc91bf92a70637d:topics/visible-flex-larger-amplitude/notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm/domain-operator/manifest.json > topics/visible-flex-larger-amplitude/notes/public-actions-43674854261-1-condensedqp/twenty-eight-condensed-warm/domain-operator/manifest.json
```

按§1完整bytes/SHA/Git blob核原字。此操作只恢复manifest，不重算科学、不恢复缺失NPZ、不声称旧artifact服务永久可用。若未来实际caller需要完整历史包，必须明确取得其全部真输入；本索引不能绕过原读取失败。

root实际删除前须保固定d195之后到真实pull头的完整新变动范围，检查两候选仍同blob以及新source/config/input是否增加具体依赖；不把API compare缺patch当无变化。这里只给固定d195及已读source下的候选结论，不把作者未读的未来main差异预填通过。root的实际删除提交和mainhead另由原行政记录给出。

全部当前科学source/request/input、真实数组、全部gzip、41/54的array manifests、migration/legacy/R456、非MD引用H、先前四producer与十一旧log均排除。此前95检查点和九行政记录的已完成删除不重复执行。旧原门、资源、输入、run和科学结论完全不因本次行政迁移而改变。

## 9. 两项操作范围偏离的如实记录

本轮曾一次经connector全文取回两份>700KB candidate，偏离根8要求的大件只Actions内读取；这不是公开Actions审计证据，也未运行科学。之后不再重复全文取，r6独立在真实Actions读取/核对候选原字节，本文仅以该必要结果和具体源调用判读作为迁移依据。

r6完整必要正文返回后，作者又创建过一个未提交main的detached Git blob，对象名 `6fa4a4b496641730c8556e4d2d3a238e30162326`。它已经是公开仓库中的Git对象，不能称“完全未入仓库”，也不应把可再生Actions原必要输出作为跨agent持久交付。本文只登记该事实，不给对象链接、不把它列为恢复依赖或交付；不再复制/提交原body。以后原日志/necessary继续在当前工具store内消费，跨agent只传必要元数据或作者结论，source/证明小文本仍按原机制交付。本文自身是作者的范围判读与固定历史索引，不是原raw输出的另存。

没有因这两项偏离新增科学门、审批或重复数值运行。所有实际未返范围、已创建对象与未提交main的区别都保留，不用后续成功冲销前述事实。

## 10. root补付的主线差异与最后真实pull守护

作者补充：ChatGPT /root，2026-11-16。本文前九节保留amplitude完整作者说明的原字节35367B / e14b5712f09d3104c0707161af4868364c2e172fc269a0d66101b160fa648033；本节不是原r6必要对象的一部分。

root把固定r6扫描头之后的已发表主线分两段读取官方完整比较，所有非removed项都有patch。各patch的新增/删除行数逐项等于GitHub返回的additions/deletions；每个added文件从完整新增行重建后，完整Git blob SHA逐项匹配。因此没有把“有patch”本身当作未截断证明。

| 主线区间 | commits | 路径项 | 完整新增文件及blob匹配 | 全新增行 | 24个字面量新增命中 |
|---|---:|---:|---:|---:|---:|
| d1956f73114f35a23d1d7caa323589fa8b7eb690 → 1379b70d249e362bce236054a1d0e8e41882593a | 22 | 51 | 29 | 11300 | 0 |
| 1379b70d249e362bce236054a1d0e8e41882593a → d5e0bb575688ee63b9656e18ea3256c12d9b8c39 | 5 | 27 | 11 | 1975 | 0 |

各段路径数不是不同文件数的可加和。第一段的唯一无patch项是另一题已删除的2026-11-12-missing-complete-input-archive-files.json.gz；它明确属于removed，不按新来源无命中来推断内容。其余21和16个modified文件只声明完整新增行均查过；未称整份旧上下文重新扫描，也不把代码控制流的动态性质简化成字面量性质。第二段含R541作者结论及本题四个摘要更新，均在上述真实比较内。

这两段检查使用本说明§3的16 specific和8 generic原字面量，不少查model SHA。第一段本题只改HANDOFF规则同步行；新科学源、请求与其它题的变更也逐项进入实际范围，没有因它们属于别题而跳过。

本次普通删除publisher仍先真实git pull --rebase并核双README。紧接实际push前，在同一个公开Actions工作树执行只读tail guard：
- reviewed base固定为d5e0bb575688ee63b9656e18ea3256c12d9b8c39，检查对象为实际origin/main；再次确认两候选原路径仍具有本说明精确blob和bytes。
- 对base之后所有实际变化逐项返回mode/path/old/new blob；新变化的所选source/config/input查完整原字节，题内gzip查完整解码字节。历史文本只回完整扫描及命中次数，未扫补集列明；不把补集声称为无依赖。
- rg若存在先实际检测，再完整逐字节行列出所有匹配位置；否则真实使用完整Python byte-line后端，不伪填工具状态。新的具体source/config/input命中、读取错误、必要body超90000B均在普通push之前停止这个删除动作，等root处理真实新情况；不会改变科学门。
- 依据已逐文本核实的base本题199985461B，枚举base至拟推HEAD中本题每个实际变化blob的旧/新byte数，精确求当前提出树的目录总字节。这里只请求改变的blob大小，没有对整个partial tree执行ls-tree -l。目录上限仍为200000000B。
- 非快进立即真实pull --rebase，核双README、重写规则读commit并再次在新的origin/main运行同一guard，然后普通push；不force，不沿用第一次检查替新头。
- guard完整必要对象独立使用RETENTION_TAIL_AUDIT行及其真实bytes/SHA；root只读一次publisher终态日志，实际run/head和guard结果以该次回执登记，不在本段预填成功。

tail guard完整源码身份为8668B / 94b286c35b974ab6ca172c78f0c9edf34af5098e440cf64f5f1d6812db2daa40；加到原实际partial-clone/pull/cherry-pick/rebase/push程序后的完整Python为13851B / ce36eeb9567b7a3d857b72f7b431c4c478d859e88167683e4cd468938fc1efff。它仅在临时行政workflow分支执行，不把行政workflow加入main，不执行科学代码或生成科学raw。

只有两条候选路径作为null删除进入本次来源提交。本文、H/open/log和恢复索引是相应作者说明；当前科学源、输入、所有gzip、5+5同目录记录、既有producer与本说明列明的保护项全不进入删除集合。固定历史恢复仍使用§8的准确命令和身份。

## 11. 实际普通删除与最后守护回执

本次普通删除已实际成功：main头f7d56b2da6e2c85f059f37277ad3026c31bb6667；纯来源提交32391c9dfda1565299464f9948898b9806a81d45。公开Actions publisher run43882664632、job133352369749，root唯一读取该终态行政日志。2026-11-16 14:08:42.1373048Z与14:08:42.6870667Z实际pull后核双README，读头49609e57ed09b95a87c6254f781a9a44283d817c，根21bd547f56590b7f2dd279d0297efb289a9b2783及题bff8aea253a9e6a7a4fac28d810ac454c5499fec均未变。14:08:55.7075522Z普通push返回PUBLISHED_JSON，工作树status为空，无force。

实际最后guard完整必要对象55444B / b3de1cceb828e2e7f13717326b2064be7aa8d961c435ee045c2ac281ae230063已完整返回。它以d5e0bb575688ee63b9656e18ea3256c12d9b8c39为reviewed base、49609e57ed09b95a87c6254f781a9a44283d817c为实际pulled head、f7d56b2da6e2c85f059f37277ad3026c31bb6667为拟推head：93个变化路径，24份current source/config/input完整扫描、43份历史文本完整扫描并仅返counts、26项removed、未扫变化0。全部当前source具体匹配0、errors=[]、allowed=true；两候选在真实origin/main中仍各具原blob/bytes。

其本题base至拟推HEAD完整改变blob差额给出198569112B，恰等于root逐已发表文本维护的目录总字节；并非仅用原估算替运行中的计数。移除候选gross1456843B，计入完整作者说明和摘要更新后相对d5e0净释放1416349B。实际推送成功以前没有将这些数值预填为已发生。

root未重复读取amplitude的r1–r6日志，也未把上述guard原JSON另存Git对象/Release/artifact；本节只发表实际操作与完整范围的紧凑作者结论。恢复与保护范围仍严格限§1、5、8所列，本次没有删除数组、gzip、科学源或现用输入。
