# 第二十六次旧 raw 保留范围调整：八份完整历史 domain manifest

**本次普通提交实施 §1 八个准确路径的移出；保全部原请求、源码、参数、父输入与固定恢复。以下 §1–5 保留代理交付时的候选审阅范围，§6 记录 root 的实际实施；没有新科学计算。**

本次实际固定 checkout 为 `8a0fa66bb446e51d932b7d4aef8e19557138dd3b`。八份候选的存在、文件大小、完整 SHA-256 和 Git blob 已在此树逐件核过；大于100KB的 raw 正文没有输出或整读到对话，仅流式计算身份。它们合计 **3475931 B**。这不是已执行删除，也不是任意动态消费者不存在的证明。

## 1. 精确候选与恢复身份

| run / request | topic 相对路径 | bytes | SHA-256 | Git blob |
|---|---|---:|---|---|
| public-actions-43648987661-1-condensedqp / 64 | `notes/public-actions-43648987661-1-condensedqp/nineteen-condensed-warm/domain-operator/manifest.json` | 518039 | `a9364db3c0ba3ef37bd9d64d7b925a5ec7d291a9a41fdc4b99bda6471c7e0954` | `dc4a87f2c1b4b9e821eb5ebd62d18581ebb41179` |
| public-actions-43640358327-1-condensedqp / 60 | `notes/public-actions-43640358327-1-condensedqp/seventeen-condensed-warm/domain-operator/manifest.json` | 466834 | `fd72338179e4a1353dc9e82d308c2328d10f4a0cf1879f5e2d60516afee41dca` | `6cf906fe7fa0029f7cad4213d95cdabb9ebd78a6` |
| public-actions-43638348140-1-condensedqp / 58 | `notes/public-actions-43638348140-1-condensedqp/seventeen-condensed-warm/domain-operator/manifest.json` | 466833 | `e09e4f61dff43318373ee81e7494a3bef1b6e61515cd9bcd517d7a0395d82266` | `6656c38ca64a882e4e82f0841510f641d7fd7e0f` |
| public-actions-43636630003-1-condensedqp / 56 | `notes/public-actions-43636630003-1-condensedqp/sixteen-condensed-warm/domain-operator/manifest.json` | 439797 | `011d625e66076bd2317257020e8ca74a3780b6e8a4d6640c3bf1bd3c239d0aee` | `b4e92c76f8f927fb48d8fe37fbb4bc592bd58858` |
| public-actions-43634517255-1-condensedqp / 53 | `notes/public-actions-43634517255-1-condensedqp/fifteen-condensed-warm/domain-operator/manifest.json` | 415619 | `b011c6447dce6bcfdf93bd3180c1f81f4f55652dd8d383836ceacd0b9741fd61` | `497affc122d5a66098e9584fc762bc5e93dac93b` |
| public-actions-43632815810-1-condensedqp / 51 | `notes/public-actions-43632815810-1-condensedqp/fifteen-condensed-warm/domain-operator/manifest.json` | 415616 | `8dd26216a5f3a73e747857161ff8ae419eadf17da2d538c358f918b0657138cb` | `6179284554c9a305fecb55e4c83ffa79061d460d` |
| public-actions-43631235905-1-condensedqp / 49 | `notes/public-actions-43631235905-1-condensedqp/fourteen-condensed-warm/domain-operator/manifest.json` | 388579 | `750aa053902670a8948c6eaa7cfdd2fb34f38cbcc128b308159ddea41715c1ae` | `54b841e38c5b72f40d58cc3c791b9bb57366806d` |
| public-actions-43629964624-1-condensedqp / 48 | `notes/public-actions-43629964624-1-condensedqp/thirteen-condensed-warm/domain-operator/manifest.json` | 364614 | `ea09bdaff9a2f7ee5f607bf849276dcdba1c60039fd74bbb7ba345269ca5fe7a` | `bd1c978a3d6768b75dc8535a49cffb5b7bdcadd0` |

以上完整字节均可由固定提交恢复，不能靠哈希重建：

```sh
git show 8a0fa66bb446e51d932b7d4aef8e19557138dd3b:topics/visible-flex-larger-amplitude/<表中相对路径> > <runner恢复路径>
```

恢复后逐件核表中完整 SHA-256；恢复一份清单不代表其枚举的科学数组已恢复，更不代表原数学或当前新场成功。

## 2. 保留的完整原请求、数学源与原父链

| request | 原 source commit | 原请求 SHA（request 身份） | 保留的 followup 文件 SHA | 原父 run |
|---:|---|---|---|---:|
| 64 | `d625bb293e07541b4bf717524e14a45392be03aa` | `db72372106b2b2e1bffafd8c022fbc0ec6cb3ea6b3c6f0d14fa3845bf7549550` | `061c30961af2cb90b6bd8c68c99eab30badd66e503273f1ae87aa02fe1e06d32` | 43646179305 |
| 60 | `da346d172715761d7da23da84c92d97a92b438de` | `e527bcc1a8503b6c13b955aeb6b8211ce6d0e3e255547d1b6defd18f68115a45` | `75736967e97221e1d8a7db5ef01610931faa8e8c53249b09a4cf449227dbbf64` | 43638348140 |
| 58 | `ba8bc4f4acd547fd5219826da4f6e35f859bca56` | `619665ceff173a279717e060dd11e1cd2d0384f52b032b036fc4e8e3fa0b8f51` | `9945033fc8c9c04acbe1f61507b9860f37a421e1e0fffa4d98341c4af3fcf408` | 43636630003 |
| 56 | `b8a19c16fc1363ffa1a66f39b9403e0dfa93e169` | `f37564a69401be1feee795150804c6e5a3f2f4e548687dc84cedc67132523ea0` | `aa89f7621f0605efafffcd37c1ac3b17e20946f4d31eada5bab91af6d6e2cfee` | 43634517255 |
| 53 | `dd3156cfe7e5197029ce45fff5beb53115de3680` | `9cb0860829ed9c0a6049db418a05a7bbd595ae8e33044177de809144424afce4` | `74afd2eed62fb873a1db9236a091b753ec412fe3f902c4e6ddc7f8d42d8791ae` | 43632815810 |
| 51 | `bd3fc94a6092313313daf607328a9695e80c17f4` | `e5f92fefce1675596da7320a0f1e1068e712fd4ddc3af747f7e5fd215337d3a2` | `1c85ea3bc3478266caa45dd4a2f3d64bdf78147fed8ef3fa15402e8385e58a35` | 43631235905 |
| 49 | `d5c99bef58700db0da1a3de2faba3e94d60b1dc1` | `284b647c2dad81ec9cca43e6acbf3b0be5507e672bff61d9aa2b3f2c001c6e30` | `5519de17ce0698d9c2967771f28912dab1c324d5addb28408a7fb9cbea4233c9` | 43629964624 |
| 48 | `86acdf3b193efb6ad536545e22c46584fcc0bdd5` | `19e2967ebbfb5577096230cfc83798fd162fab0c5417bd85d4c4153895b9a1ca` | `0434c481a7c030b0953fb2007d16f9303eefd6b713bb287dcecce4f2d6e8cd80` | 43627827085 |

每个完整请求路径是该候选 run 目录下的 `followup-request-identity.json`，本次原样保留。它给出完整 source_sha256、参数预算、实际 warm/status 双身份和必要原父关系。请求48/49/51/53所列全部7/10/13/13源逐项与当前源码相同；请求56/58/60/64分别18/22/22/31项中，仅行政发布器 `root_20261114_publish_actions.py` 的当前字节不同，所有其余声明源逐项匹配。该差异不能宣称消失：若重演原发布过程，发布器须从该行原 source commit 获取并核原请求SHA；当前发布器不能冒旧发布器。数学生成者及 typed-domain 源实际相同。

必须保留：所有 warm、status（包括gzip传输别名）、optimization-intent、condensed-array-manifest、完整请求、原始参数/源、实际父输入和恢复脚本，以及全部其它 sibling。本文不建议删除这些。原大payload已缺失的部分不计本次释放。

## 3. 真正生成者与 export 控制流

各候选由对应 `computations/geometry_20261114_<name>_query_domain_operator.py` 的 `export` 写出；对应 `..._condensed_warm.py` 的 `_run_engine` 把真实 capture 与该 operator 传给原完整 engine。实际源码身份如下：

| name | domain 源 SHA / bytes | warm 源 SHA / bytes | export 原行 |
|---|---|---|---|
| thirteen | `d674a64e11cfac1f57f0c24166546a55045847633935dddb8ef53df4024d3cff` / 28524 | `7785f4eb905da4c3e80ba988c79fa8a34b0a27017e6b8abc99764d8105eccc7c` / 38686 | 403–452 |
| fourteen | `049ab10d130c94d5b1849a2af3b0e3f4848819bb9b7af68230488c25ba778464` / 28612 | `331b59edadfa1fb7d5f8c64e6f0119c63a62f5e2a3df999549ef7effd932aac8` / 38790 | 404–453 |
| fifteen | `c6581f0b8fdef4c3bc48d364c6845cff9a4244b043a4d14c772ef6fd3b2503e8` / 28770 | `f1310edc94fb3a9c9f95b5dad98e7073c1879997b9a9bdf06c5028e91f83351e` / 39048 | 406–455 |
| sixteen | `a92efa1735832d144cb65d617beb2d9018d7822f5cc7d3846d00757abfb2db2a` / 28955 | `b5bfc20259b2d182ac881cf9dab7062912578fb489ef17940c259082bf184815` / 39265 | 409–458 |
| seventeen | `5bb4f214d4d2505185448a9162c0d995bdb6c37168e6d9542dfe6202e8f21a41` / 29119 | `f8131287af5d10653692f6e5b7c3cf8ee1d4f17757c3017007b20061598f317b` / 39496 | 411–460 |
| nineteen | `945114799a2cf564c59b463e1429b55119d4ad421bc5f3414c7143333e43d35e` / 29481 | `63ec6bd0da782933ad01628c686499d6325fa10df2c624f97c6f131a233e8d39` / 40216 | 417–466 |

实际控制流：各 warm 的 `_run_engine` 设置 `engine.EndpointJacobianCapture = domain.capture_queries` 和 `engine.FullAngleDomainOperator = domain.<真实类>`，在原参数上调用 `engine.main()`。engine由 twelve-query → observed-seven → seven-query 的原模块引用最终指向 `geometry_20261114_full_angle_projection_warm.py`；后者实际第465行调用 `domain.export(args.out/"domain-operator")`。export从本次完整当前 capture/原固定因子和数组生成 payload 与 `self.description()`，写 `manifest.json` 并清除已导出 factor cache；不以本次候选旧manifest作数学初猜。它拒绝覆盖已有manifest，所以重算须使用新的实际输出目录。

重算会重新生成当前运行的路径、时序和行政元数据；不承诺与旧manifest逐字相同。旧精确字节另由§1固定提交恢复。完整算法仍须有原实际accepted/prepared/anchor/config和warm/status；不得只恢复manifest就称已重算完整科学。

## 4. 消费范围与当前只读扫描的边界

已对当前 topic `computations/`、`scripts/` 及仓库 `.github/` 做固定 literal 文件名扫描，literal集合含八候选的完整 topic 相对路径、完整run目录、SHA-256、Git blob；没有这些 literal 的源码/配置命中。这是明确字面范围，不证明路径拼接、动态目录参数或其它文件没有消费者。当前 runner raw 或全topic gzip尚未由本次额外扫描。

真实通用消费者确实存在：旧 completed-prefix/readback 路径会从显式下载/恢复 root 读取 `domain-operator/manifest.json`，然后核完整payload与模型。已有完整说明 `notes/2026-11-16-two-twenty-domain-manifest-retention.md` §3–5 与 `notes/2026-11-16-domain-manifest-retention-audit-and-fixed-history.md` 描述这种动态读取责任；不能借这些说明把本八候选的逐件字节视作已审。未来真执行某个旧reader时必须实际供给其完整恢复路径。

因此这份交付是 root 第26批决策所需候选、固定恢复与精确源入口定位；root可结合正在保留的固定恢复链决定普通移出main副本。它不直接触发删除，不改既有科学结论，不把旧保存策略写成今后继续提交可重算raw的许可。

## 5. 本次工作的实际限制

只使用标准库读取小请求/小完整源、AST定位、流式文件哈希和Git blob身份；没有导入科学模块、运行旧求解器、读取大raw正文到对话、删除文件或改refs。任何实际净释放容量须在root真正普通提交前后实算；这里只给毛候选总量。

## 6. root 复核及本次普通提交

root 分段完整读 30,993-byte 候选 metadata，逐项独立核八个原文件大小、固定提交的 blob/size、八份小原请求完整 SHA；没有再次整读或重算八份大 raw 的 SHA。候选 SHA 来源仍是 §5 明确记载的代理流式身份核验，不改写成 root 的新科学读取。八份完整原请求本体和全部 verified_sources 在下面4 个分卷逐对象保留，各卷小于 60,000 bytes；原地请求和所有其他 sibling 均不移出。

root 又逐字节核 31 个不同小源文件所对应的 33 个原 name/SHA 版本，并只用标准库 AST。唯一当前漂移是四份请求中的行政发布器，三个历史版本分别为 10,413、10,372、10,357 bytes；已从每份原 source commit 实取小完整源并核相应 SHA。4 个分卷保每个源的当前身份、是否相同，及这些原发布器的准确恢复 commit/blob/size/SHA。没有把当前发布器当作原字节。

root 完整读 thirteen 的实际 export 体并逐一读其余五种 export 的全部差异；差异仅原查询数的 docstring 和 artifact_scope 文字，数学数组生产与拒绝覆盖路径完整保留。另核原 full_angle_projection_warm 的实际 domain.export 调用。它从完整当前 capture 和 factor cache 生成清单，不以待移出清单作为场的初猜。原请求保持完整预算、实际 warm/status 身份、查询角色、原父 run 和全部 source_sha256；没有凭 request 另造一份未经原记录证明的 argv。

这次仅普通移出八个准确 manifest，毛大小 3,475,931 bytes。恢复原字节须用 §1 固定历史，若实际再运行旧动态 reader，还须恢复它真正需要的全部 payload；原有缺失 payload 不因本次保留台账而自动补齐。新科学再生只在公开 Actions，使用完整原源/真实父输入/原参数和新输出目录，不覆写旧输出，不把新输出预填成旧 SHA。当前 06/07 运行、新源码、所有未知返回与课题完成标准不受该历史生成文件保留调整改变。

完整小台账：

- `computations/resume-20261127-legacy-domain-manifests-retention-part-001.json`：37285 bytes，SHA256 `fca42d348e5065d6eba98501485ef57b0e8ef9f96e85453d94a19ee03750ccba`。
- `computations/resume-20261127-legacy-domain-manifests-retention-part-002.json`：49805 bytes，SHA256 `d0acecd99164b8e789b4d4a7859300ba2c7e4446ea274185dda27cb21003e0ee`。
- `computations/resume-20261127-legacy-domain-manifests-retention-part-003.json`：52794 bytes，SHA256 `6b6dc1c330d7aedc1e5b6b2b6126710eff2b97326632d10b363af63fa5dbd483`。
- `computations/resume-20261127-legacy-domain-manifests-retention-part-004.json`：23372 bytes，SHA256 `f2d0f0a53163ced6c43fcaac7f010e0cd0be2926ee07719d26164710133acf57`。
