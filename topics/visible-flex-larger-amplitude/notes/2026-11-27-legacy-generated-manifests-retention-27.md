# 第27次旧派生清单保留处理：四个输出清单与完整参数

本条按根 README 的 raw 保留规则处理已经可由完整源与输入再生的旧输出清单。只从当前树移除下表四个文件，共 **2368284 bytes**；源程序、原始请求、完整配置、完整 spec、原输入、其他同目录记录以及既有结论全部保留。没有重跑科学计算，没有新增数值，也没有把运行输出改名当作原始参数存回仓库。

全部原小请求、配置、来源身份、实际核查结果与精确恢复定位保在 [完整参数账本](../computations/legacy-generated-manifests-retention-27-complete-parameters.json)。该账本保留 request54 的完整16来源及全部参数、request45 的完整4来源及全部参数，并完整保留 rawcell0steps 的原配置、runtime 配置和启动意图内的原命令/78来源声明。大 spec 原文件不删除、不截断、不复制进账本。参数账本记录的是本次处理前原参数本身，不是重新生成的场或数组。

## 1. 四个被移出当前树的派生文件

下列路径均相对于本课题目录；全部 exact bytes 均可在已公开固定提交 `86311afa06452f2d4bf38a583aafcaedf16f3c6d` 恢复。本次先查文件大小，再流式核 SHA；没有整读这些大 JSON 的数组条目到会话。

| 原路径 | bytes | SHA256 |
|---|---:|---|
| `notes/public-actions-43622149326-1-rawcell0steps/native-rawcell0-step-capture/rawcell0-step-array-manifest.json` | 938674 | `fcfc6f76d7bba92aa38eb793dc055d2dbbe7ab098218ac1c036f2ad67512ede6` |
| `notes/public-actions-43634889730-1-directld/native-rawcell0-direct-ld/direct-ld-array-manifest.json` | 609264 | `06004e6d6d526efd10e5ac29747585af163c0dfb23f64398eb226f58744de384` |
| `notes/public-actions-43634889730-1-directld/rawcell0-direct-ld-correction/new-system-array-identities.json` | 483189 | `ebd2bd6bc1ea72ce6d08da6f2e867749498c637feed818765103cdc64bb6833f` |
| `notes/public-actions-43627827085-1-condensedqp/condensed-warm/domain-operator/manifest.json` | 337157 | `2b0cf4ad85a3397cb69121ee6fa5b2c261d2a2a9655b9c57da0c61014fabc83e` |

对应 Git blobs 依次为 `466740e6d32162a130cdf4a62816b78d25ebb8dc`、`193505116ac43a05d246c4b820185399171e6e96`、`75d9da255c3f1f0652b2df04ad2cacfe923a82ae`、`c373e9e5b41b889922d4e71410fa869ac5a07975`。处理前逐项核对工作树完整 SHA、字节数与固定提交 blob 身份相符。

## 2. 为什么它们是输出；原生产器保留

本次核对以下完整小源码的身份，并定点读取写入位置：

1. `geometry_20261114_native_rawcell0_step_capture_hook.mjs` 的 `saveManifest` 从实际 `arrays`、`metadataPackets` 和完成状态写出 `rawcell0-step-array-manifest.json`。它是在原捕获器已经产生数组后的输出清单，完整 hook 保留，SHA 为 `2695cd2dc0abc66fe3f8ae8987b6ae3b50b884f692a418198347a61dddf24435`。
2. `geometry_20261114_native_rawcell0_direct_ld_capture_hook.mjs` 的 `saveManifest` 从实际长双精度捕获数组和 chunk ledger 写出 `direct-ld-array-manifest.json`，完整 hook SHA 为 `3499f7abb96a4f25c4c3a986d97dc8aea3b21742770aabe7abe2822ad8b3caf4`。
3. `exact_20261114_rawcell0_direct_ld_equilibrated_correction.py` 在构造完整 `RawCell0DirectLDSystem` 并导出输入之后，从 `system.arrays`、`system.J_rows` 写出 `new-system-array-identities.json`，完整源 SHA 为 `42e10320252935015c65bbc34579947e559182bb1b2a74ca1aa13a6597c064b9`。原完整1372系统及输入绑定来源不改。
4. `geometry_20261114_twelve_query_domain_operator.py` 的 `export` 从既有完整 capture/factors 输出十二种 query、原 midpoint 输入与 endpoint 因子，再将 `description()` 和所有已写文件的记录写为 `manifest.json`，完整源 SHA 为 `6a428d2f8412659cbd318321aa992c3b4565ff41177131a9cc9d268c6fbb7b1f`。原 condensed warm 的生产路径及全配置仍在；没有删减成少数 query 或仅12行示例。

第4项的调用者 `geometry_20261114_full_angle_projection_warm.py`、原 condensed QP、warm 和 response 全源继续保留。完整源的实际字节数、当前 blob 与 SHA 都在参数账本中；所列生产器的原科学运算本次未执行。

## 3. 完整原参数与来源漂移

原 `direct-ld-request-identity.json`（7809 bytes、SHA `d8d5a0ed6ce97ab1f06547ebea892def70fd9d54ba91aa40bcea98b36b769d2b`）仍在原路径。它的真实 request54 绑定源提交 `7eb383af1ca2bb04c7eaef9c65578dbc124269d8`，完整请求保有16来源、原28/41输入身份、全部精化/预算/门槛参数。原请求 SHA 与文件 SHA 分列保留，不混用。

原 condensed `followup-request-identity.json`（2724 bytes、SHA `cc29d51ab525ca0822459dd0677f3c34a672fac8714bd6c974dbb9f1805a2744`）也仍在原路径。它是 **request45**，绑定 `3689913753612b02021e439082eaf1c166091183`，不是47。原完整4来源、父 warm/status、1200/600/90/30预算、256行、200 sweeps 及未增加非线性阈值的参数全部保留。

逐项核对这两份原请求的20项源时，18项当前完整 SHA 仍与原声明相同，另两项有真实版本差异。本次另外从原提交读取并核实这两份完整原源，而没有用当前版本代替原科学身份：

| request54 原源 | 原 bytes | 原完整 SHA256 |
|---|---:|---|
| `geometry_20261114_native_direct_ld_trial_replay.py` | 29918 | `99204fcd615affc393a04800f62f80d05dce5225a90ece6c27b4b00e4c241160` |
| `root_20261114_publish_actions.py` | 10340 | `699c696af338018deb97a53127cde1f9d9c743776b26670c69c3ae03dc7485df` |

完整原 `rawcell0-step-spec.json` 为180567 bytes、SHA `ac6f99929ea09e30e97a3a2b2649a2b25d24f7a05d5adae4357a1034299c0da0`；原 `direct-ld-spec.json.gz` 为145192 bytes、SHA `ba9894bf30440cdbfb7a58684abbb2901193cf8c2cf3456425814cc2369d9d05`。两者都保在原路径；本次仅流式核身份，没有整读大文件或删任何原参数。全部小配置也同时保留原文件与账本内完整值，不以节选代替。

## 4. 恢复边界

恢复某一清单应在 scratch/runner 中读取固定历史，例如用 `git show 86311afa06452f2d4bf38a583aafcaedf16f3c6d:topics/visible-flex-larger-amplitude/<上表路径>` 输出到临时文件，再核上表 whole-file SHA。这个操作只恢复该清单的原始字节；若某消费者需要原 payload，还必须恢复其完整原输入和全载荷。不能因为有 manifest 身份就声称旧大数组已经重新取得，也不能因为保留了源码就声称再次科学计算会逐字复制历史浮点输出。

本次没有声称所有动态消费者已被枚举；需要历史清单的旧读者必须使用明确历史输入，不应在缺文件时退回空清单、减少行或默认成功。旧请求中历史 artifact 的字样照原参数保留，不构成本会话新增 artifact 上传的许可。本次不新增或迁移任何 raw artifact，也不修改已登记科学结论、旧失败、未知前缀和后续全量读取责任。
