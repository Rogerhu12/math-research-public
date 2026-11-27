# 第 37 批保留说明：八份 actual41 下载目录收据

本轮只指定八个旧 `actual41-artifact-fetch-receipt.json.gz` 作普通 Git 移出，合计 **1,663,643 B**。它们是同一固定 actual41 ZIP 在八次后续公开 Actions 中形成的下载、解压目录与文件身份收据。原科学计算源、完整请求、全部参数、实际结果、矩阵与场数据及其余保留文件均不在删除清单中。

这是一份交 root 实施的保留账，不声称本稿准备时已经删除文件或写入任何分支。完整机器可读记录为 [2026-11-27-actual41-eight-download-receipts-retention37.json](2026-11-27-actual41-eight-download-receipts-retention37.json)，完整 SHA-256 `ebb79d44069b4068b8cc6823448f62a4aa2c3c8d39589a6e992f993ce9781cc8`，68987 B。它保留每一对象的实际 run、固定 source commit、完整工作流与发布器身份、原请求身份、全部下载/复制/发布参数，以及精确八项 `delete_entries`。

## 1. 八个原对象及准确恢复位置

所有目录都位于 `topics/visible-flex-larger-amplitude/notes/`；每行文件名均为 `actual41-artifact-fetch-receipt.json.gz`。目录列表元数据来自同一实际 main 快照 **`61ce5c1bbc94ee093d42087b85173b4ec3b0c142`**，该提交的 Git tree 为 `c0f68111459789a8be58cd9377ba312eccf5a87f`。

| 原目录 | gzip 字节数 | 原 Git blob |
|---|---:|---|
| `public-actions-43623850723-1-rawcell0band` | 207957 | `bd547f265d632f688b9d03bef3482eb137e95694` |
| `public-actions-43626121246-1-rawcell0gauge` | 207954 | `844830a911ed7b5e60484f606b2e06f9725efbb2` |
| `public-actions-43627297724-1-receipts` | 207955 | `b3d8b6dbeea6e7c96305b99a6d2573c3924506d8` |
| `public-actions-43630351235-1-stage43probe` | 207954 | `ac7e0aaaf013f47202a5384e425785060c8deece` |
| `public-actions-43634201913-1-directld` | 207954 | `3d6f761933f94ddf83b5b60de6f7053ca283d1a2` |
| `public-actions-43634889730-1-directld` | 207955 | `c43064f0deb6cc61f94b4c7aae2c015b99f92ca1` |
| `public-actions-43636504089-1-directldtrial` | 207957 | `c864985ec75b6e360b563abe14f57e0738c6ca06` |
| `public-actions-43637356027-1-dampedchain` | 207957 | `4bf5dbba8cf25596fb613f996368c8208c6d90d8` |

固定提交、完整原路径、Git blob 和字节数共同给出原压缩字节的准确恢复定位。本轮没有读取、解压或重新计算这些二进制文件的 SHA-256。已经读取的小记录没有提供它们的完整 gzip SHA-256 或未压缩收据 SHA-256，因此 ledger 的这两个字段均为 `null`；这表示未取得该摘要，不表示零值、空文件或与别的对象摘要相等。

需要恢复历史原件时，可从上列固定提交取对应路径，或直接取记录中的 Git blob。例如下列命令只是恢复方法，未在本次准备中执行：

```sh
git show 61ce5c1bbc94ee093d42087b85173b4ec3b0c142:topics/visible-flex-larger-amplitude/notes/public-actions-43623850723-1-rawcell0band/actual41-artifact-fetch-receipt.json.gz > /tmp/retention37-actual41-43623850723.json.gz
```

准确历史恢复使用 Git 中的旧对象；它不依赖该 Actions artifact 今天是否还在保留期内。本次没有检查或重新下载 artifact，也不把其当前可取性设为普通移出的先决条件。

## 2. 原下载包与收据严格区分

八次下载都指向原 actual41 的同一个固定包。这五个值来自完整下载 adapter、各实际 source commit 的工作流和既刊 [原接口说明](2026-11-14-pinned-actual41-artifact-fetch-interface.md)：

| 参数 | 准确原值 |
|---|---|
| source run / attempt | `43622149326 / 1` |
| artifact ID | `14124209116` |
| artifact name | `visible-mainline-rawcell0steps-43622149326-1` |
| 完整 ZIP 字节数 | `349636774` |
| 完整 ZIP SHA-256 | `356d9d81959739a22e9347d7ceba6fd4880ad61db70dca73096a4c5b71dc73a8` |

原接口另记录 job `132530011605` 与 source commit `0beffe5a963015a4063a8c53d4a92fec32205005`。ZIP 摘要只属于 ZIP；它不是本轮任何 JSON 或 gzip 收据的摘要，也不是 ZIP 内某个科学结果的摘要。

生成链是：固定 ZIP 的原下载与安全解压 → 最后写入 `_pinned_public_artifact_receipt.json` → 原工作流复制为 `actual41-artifact-fetch-receipt.json` → 当时的完整发布器压缩并发布到本表目录。下载入口只保存输入身份和目录信息；不进行新的 ODE、J、根、矩阵或场计算。后续同一 job 的科学运行状态保持原记录，不由下载收据重判。

## 3. 完整生成源与固定参数保留

两份完整生成代码保留在 `topics/visible-flex-larger-amplitude/computations/`。本次实际读取了八个 source commit 下的两文件全文，全部逐字等于下列既刊原件；也核了固定恢复提交下的当前原件：

| 完整源 | 字节数 | SHA-256 | Git blob |
|---|---:|---|---|
| `exact_20261114_fetch_pinned_rawcell0_steps.py` | 6278 | `328403614476954cddfdc9b7c764e27d668d44042f8da3efa63cb2e8076c5b79` | `b1635f04934c740ad07908a2da301ff7fa84f7d8` |
| `exact_20261114_fetch_pinned_public_artifact.py` | 28006 | `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` | `8ee390d0c1449a6a532d72158172af278f1c7cf3` |

`exact_20261114_fetch_pinned_rawcell0_steps.py` 在独立模块实例内仅替换原下载内核的 `PIN`、`SCHEMA` 和 `public_metadata` 的本地来源追加器。CLI 全 tuple 核验、GitHub metadata 与 ZIP 完整 bytes/SHA 核验、路径/类型/CRC 检查、独占新目录、收据最后写入及只读封存仍由完整原内核执行。收据同时保留原内核与本地 adapter 的真实来源，未把本地来源字段冒作 GitHub metadata。

完整必填下载 argv 在每条 ledger 中保留为 15 个原命令词，只有各 run 的独立 `--out` 目录不同。原调用形式是：

```sh
python -u "$VISIBLE_COMPUTATIONS/exact_20261114_fetch_pinned_rawcell0_steps.py" \
  --run-id 43622149326 --artifact-id 14124209116 \
  --artifact-name visible-mainline-rawcell0steps-43622149326-1 \
  --expected-size 349636774 \
  --expected-sha256 356d9d81959739a22e9347d7ceba6fd4880ad61db70dca73096a4c5b71dc73a8 \
  --out "$ORIGINAL_INDEPENDENT_OUTPUT"
```

这里 `$ORIGINAL_INDEPENDENT_OUTPUT` 只是说明用符号；下表给出各工作流实际规定的目录模板，不修改原 argv：

| 后续 run | `RUNNER_TEMP` 下原输出目录 |
|---|---|
| `43623850723` | `actual41-step-capture-input-43623850723-1` |
| `43626121246` | `actual41-step-capture-input-43626121246-1` |
| `43627297724` | `actual41-receipt-input-43627297724-1` |
| `43630351235` | `stage47-original41-43630351235-1` |
| `43634201913` | `direct52-original41-43634201913-1` |
| `43634889730` | `direct52-original41-43634889730-1` |
| `43636504089` | `direct55-original41-43636504089-1` |
| `43637356027` | `damped57-original41-43637356027-1` |

原工作流使用 Python `3.12.14`，下载 step 的既有时限为 15 分钟。内核固有参数为 1,048,576 B 流块、1,048,576 B metadata 上限、8 次重定向上限、60 秒单请求超时；没有遗漏的可选 CLI 数值参数。仓库须为本公开仓库、执行环境须为 GitHub Actions/Linux，目标必须是 `RUNNER_TEMP` 下尚不存在的真实目录；token 只从 step 环境传入，本文不记录凭据。

每个原发布器的完整 source commit、路径、字节数、Git blob、SHA-256，以及对应七词发布 argv 和原 YAML step 均在 ledger 内。压缩表达式准确保留为 `gzip.compress(src.read_bytes(), mtime=0)`；原规则只对大于 1,000,000 B 的 `.json/.jsonl/.log` 压缩，加 `.gz` 后在压缩体小于 5,000,000 B 时发布。本次只读这条规则，没有读取或重压收据。

## 4. 实际后续 run 与完整原请求

以下 source commit 和终态来自已经读取的 GitHub run metadata。`failure` 是整次工作流的历史终态，不能用来推断此前下载步骤失败，也不能改变原科学结果。所有 attempt 均为 1。

| run | lane | 实际 source commit | 历史 API 终态 |
|---|---|---|---|
| `43623850723` | `rawcell0band` | `34abbdf26804307a61fa4d18139c969c1cf9c445` | `success` |
| `43626121246` | `rawcell0gauge` | `5c6f45fcac65d96f6b64c8d97f842efcd280f342` | `success` |
| `43627297724` | `receipts` | `d07eeb32ec7e72f8982b0c8f3c9352e4a0e34e1f` | `success` |
| `43630351235` | `stage43probe` | `c9c466f468d49e3f4699d0e0247109e83047bdb5` | `success` |
| `43634201913` | `directld` | `61831d6a76b2a06e0c22f7fe03aad87d1b69d39f` | `failure` |
| `43634889730` | `directld` | `7eb383af1ca2bb04c7eaef9c65578dbc124269d8` | `failure` |
| `43636504089` | `directldtrial` | `6b7e9846ab9062614618856d4d6772c847a303c2` | `failure` |
| `43637356027` | `dampedchain` | `adbdf144b14ae7adc71df09948a5c05f8a30e8b8` | `failure` |

原完整工作流、请求和发布器都按各自实际 source commit 读取，不能以今日同名文件覆盖旧参数。ledger 为八份请求保留完整路径、原字节数、whole SHA-256、Git blob 和固定 source commit；这些原请求文件不在删除清单中，也没有抽掉它们的原数值参数。

| run | 完整原请求文件 | 字节数 | 完整请求 SHA-256 |
|---|---|---:|---|
| `43623850723` | `public-mainline-request.json` | 2616 | `96b8e0bce17e99f30543d7d2a88f2e0c91549d22ef16c30a1f7bafc403359963` |
| `43626121246` | `public-mainline-request.json` | 2158 | `e4d4a535f34d0060b749a0ce84cfbe3bd49f30d6c609b00a640868a3bc1bcf63` |
| `43627297724` | `public-receipt-request.json` | 1210 | `3e3903b1e10e9ac6d11fc63da0f607c54c15714c112498566b2eb666b0860106` |
| `43630351235` | `public-native-stage-probe-request.json` | 2388 | `1a4f637705aaa70f61e07e3c83220ce0bc7d861a3057b6b4ee4c8bfdb5755b0b` |
| `43634201913` | `public-native-direct-ld-request.json` | 3754 | `ea6f3448bd2779cd91bdfb028269b103803f6ea760fae28cf360db30f59434b9` |
| `43634889730` | `public-native-direct-ld-request.json` | 4118 | `1970636d2f8fdd443f0153edc7334274c9f65252811b673c500600a423761031` |
| `43636504089` | `public-native-direct-ld-trial-request.json` | 5044 | `52e88bc76f11ed206e7409d44fa0db0dc45f1c6933448a3873814759d0fc79c4` |
| `43637356027` | `public-native-damped-chain-request.json` | 5783 | `30708e170f40a51b3796c20fe9923e5ce6589f758d388797aeaf21ee5684d48f` |

六个目录中仍有独立的 `receipt-read-intent.json`、`stage-probe-request-identity.json` 或 `direct-ld-request-identity.json`。本次完整读取这些 1,390–9,879 B 小文件，其内完整 `request` 与实际 source commit 的原请求逐字段等同；其 whole SHA、Git blob、bytes 与原路径也保存在 ledger 中。这些小文件全部保留。前两个 mainline 目录没有对应同名独立 intent 的目录记录，所以用原完整请求和实际工作流身份，不臆造 intent。

## 5. 保留范围与本次实际读取边界

本次删除集合精确等于第 1 节八个 gzip 路径。既有科学请求、源文件、参数、矩阵/场结果、真实失败记录、其他 receipt 和目录中的其余结果均保持；不再次处理先前已经移出的 actual54 两份收据。既刊 [同类 actual54 下载收据保留说明](2026-11-16-two-old54-download-receipts-retention.md) 说明的是同一种行政元数据处理，但其旧路径、摘要和检查结果没有移借给本次八文件。

本次只读取 Git 目录/提交/run 元数据、完整小源、完整小请求和小 intent；没有读取任何待移出的 gzip payload，没有调用下载器、发布器、科学程序或新的 Actions 任务。没有新增独立扫描、科学重跑或机械准入门。源与参数已保留；若日后原 artifact 仍可下载，原生成过程可重做，但新时间、run 与临时目录信息可能使收据字节不同。需要历史原字节时应使用本稿的固定 Git 恢复定位，而不是声称重下载一定复现历史文件。

发布与普通删除由 root 在同一受控 Git 流程中实施；本稿与 ledger 的准备没有更改 ref。扣除本批说明和 ledger 后，净空间节省按本次实际新增文件大小计算，不把 Git 历史对象大小冒作当前 topic 工作树大小。

