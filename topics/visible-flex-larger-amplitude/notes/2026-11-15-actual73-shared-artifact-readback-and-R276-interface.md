# 实际第 73 轮：同一原包的完整读回与独立 R276 诊断

类型：Actions 读取/诊断接口；不是新的 native 数值结论。  
作者：exact_refinement。日期：2026-11-15。

## 1. 已发生的唯一原件

本请求绑定已终态的公开 run `43657001633`，source `9515d5aaf7c68f8efd366438d6bd81ce73c3486f`。官方 artifact 元数据已经实际读取：

- ID：`14141540502`；
- name：`visible-mainline-nojprimalnative-43657001633-1`；
- ZIP：1752742419 B；
- SHA-256：`3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9`。

原 job/native step 的 failure 不被当作具体数学原因，也不能替代原结果内容。新请求没有预写 iteration 数、native result SHA、范数或接受结论。

## 2. 唯一下载与调用顺序

共享原件目录为 `$RUNNER_TEMP/original-completed-43657001633`。新独立标准库编排器 `exact_20261115_actual73_readback_packets.py` 的顺序是：

1. 调用冻结 `c0621177…` reader 的原 `fetch_original`，仍用原 `51224788…` 完整 HTTPS/metadata/ZIP 大小与 SHA/CRC/安全解包路径。
2. 在完整字节审计开始前，逐字复制本节列出的原结果、trace、trial 与每个实际 iteration 小件。
3. 调用同冻结 reader 的原 `run_reader` 与原标准库 byte utility；没有修改审计函数或重新调用下载。
4. 工作流下一独立 `always()` step 调用冻结 `bd4ff360…` 的 R276 科学消费者，使用同一解包根。
5. 原件发布恢复、reader artifact 上传和有界收据发布均保留 `always()`，不因后继诊断失败删除原产物或改原科学结论。

第 4 步有新的精确整数科学算术，明确标为 `byte_only_audit=false`。它不是第 3 步的字节核对，也不要求第 3 步 PASS 后才启动；其输入仍须通过自己原有完整身份绑定。

## 3. 全文原包导出

原根级保存：`noj-primal-current576-request-identity.json`、`native-noj-primal-current576-damped.log`、`rule-sync/runner-result.json`。

原 `native-noj-primal-current576-damped/` 下保存存在的：

`result.json`、`current-correction-summary.json`、`current-corrections.jsonl`、`native_trace.jsonl`、`native_trials.jsonl`、`native_stderr.log`、`native_0001.json.gz`、`native_iteration.json.gz`。

按实际存在的 `iteration-[0-9]+/` 目录动态枚举，不预设轮数。每轮保存存在的 `qr-launch.json`、`qr-exit.json`、`qr.stdout.log`、`qr.stderr.log`、`returned-correction.json`、`bridge-failure.json`、`qr/summary.json`、`snapshot/result.json`、`snapshot/context.json` 和 `snapshot/context.json.gz`。两种 context 名分别按是否实际存在记录，不能将缺失名改写为存在。

所有副本放在 reader artifact 的 `request73-readback/large-arrays/original-native-packets/`，原相对路径保留。gzip 包保持原压缩字节，不解压重序列化。每件记录原 bytes/SHA 与副本路径，复制后再核副本摘要。不存在的文件列入完整 manifest，不构造内容。完整 manifest 为 `large-arrays/original-native-packet-manifest.json.gz`；小入口为 `original-native-packets-before-audit.json`。

原 producer 并未为十个 noJ trial 每次额外导出完整状态与残差向量；本导出不会补造这些数组。真实 trial 只能按原记录的 scalar、拒因和已有原件解释。已接受状态可能在下次 freshwithJ correction snapshot 中出现，但不能据此冒称所有 trial 数组已存在。

## 4. R276 的真实 SHA 选择

后继 step 再核同完整 transport receipt 的 repository、run/artifact tuple、ZIP bytes/SHA 和原 source commit。没有第二次下载。

若原 `result.json` 存在且含真实 `current_correction_summary`，读取该文件实际完整 SHA 传 `--native-result-sha256`。若没有这一完整桥收据而存在原 `current-corrections.jsonl`，明确用 partial 模式，传其实际 `--partial-records-sha256`；原 trial journal 存在时也必须传实际 `--partial-trials-sha256`。这只是从已核原包确定接口，不填入未来假身份。原 result 或 partial journal 的 bytes/SHA、准确 argv、transport receipt SHA 均保存。

若两种输入都不存在，只记录无法进行该诊断，没有原模型可制造。原 result JSON 无法解码则如实记录接口错误，不静默把坏 JSON 解释成成功或换模型。

实际调用仍是冻结 `exact_20261115_native_affine_infinity_prediction.py`：`--native-kind native73 --original-run-id 43657001633 --original-source-commit 9515d5aaf7c68f8efd366438d6bd81ce73c3486f`；所有实际已记录 iteration 为默认范围，没有预选较好轮。输出 `request73-affine-infinity/` 与 byte report 分离，日志、CLI 绑定和 step return code 另存。

消费者使用每轮原 129248 行的保存残差、真实正尺度及完整 exact ledger，计算十个原 powers-of-two 试步的 affine 预测和 R276 区间。没有重算 RHS/J/ODE/QR、矩阵作用或非线性 trial。这里的精确 affine 模型不包含实际状态更新或重算 flow 的浮点舍入，不能被改称 native 下降保证。

诊断 step 不提供 token；调用子进程时还显式移除可能继承的 `GITHUB_TOKEN`、`GH_TOKEN`。原文件及原 nonlinear 接受状态不被诊断修改。

## 5. 发布与资源

现有 `visible-larger-public-completed-readback.yml` trigger 不变。对既有 prefix reader 的映射和参数路径保留；仅给 `native73` 加上述包导出编排器和明确请求的 R276 step。

`recover_original_publication` 范围新增 `native73`，映射原 `current576native` lane；prefix 的 `condensedqp` 映射不变。仍使用 publisher SHA `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`，原 source/run 通过明确恢复环境绑定，恢复 receipt 记录本次 reader run。只是重发原保存文件，不重科学。

原 `.json.gz`、日志和完整 manifest 在 reader artifact 完整保留。任何 `large-arrays` 路径按冻结 publisher 策略不进入 Git；通过恢复原发布可取得有界原报告和日志。byte reader 与 R276 的新报告在本次 `receipts` 发布目录下，避免冒充原73产物。

本草案预留 8 GiB 原字节读取空间，job 120 分钟沿现 route；这是存储/读回资源声明，不改原 73 科学预算。原 archive、snapshot/factor 和所有 partial 文件在本 job 内不主动删除。完整原包仅下载一次。

## 6. 冻结文件与静态核对

| 文件 | 字节数 | SHA-256 |
| --- | ---: | --- |
| `exact_20261115_actual73_readback_packets.py` | 11509 | `d97eb11b51ff621f10d31a4da5aa942bca405ec36a64dd298e551eddc1d0e9d7` |
| `public-completed-readback-request.json` | 3184 | `60097d6734c8847436454b4248056a983ea668e98b9f3443f598a249cfc9284d` |
| `visible-larger-public-completed-readback.yml` | 20586 | `3cd2eba49eb7ec1b9407447322c5793a8488e93cade643a99bd078539ea2c74b` |
| `2026-11-15-actual73-readback-route-static-check.json` | 6891 | `b2a1d4e75035567c71ea05812d24e88b3445b3b20fb30c94a519a414ae7d473c` |

实际官方 artifact tuple 与本请求逐字段一致；6 个入口 source pins、冻结 reader 的另 10 项原来源 SHA 均已本地哈希核对。新源只标准库；唯一 fetch、原件导出、原 byte audit 的源码顺序已核。8 段 shell 经 `bash -n`，5 段内嵌 Python 和全部入口源码经 AST。原科学代码均未 import、执行或改变；没有下载1.75GB原包到本地、重算任何范数/有理账或启动 Actions。

两份相对当前 route/request 的 `.diff` 随稿保留。本接口交付不是新的独立审查或科学准入门；真实原件和独立诊断结果仍以 Actions 保存输出为准。

最终接线仅另改四个展示name，使整个job及上传/出版明确含独立精确诊断。原静态回执锁定8be1基线，最终3cd2标签变更的全部非name YAML字段逐项相同，见 `2026-11-15-actual73-route-label-only-check.json`；源、request、run、env、预算均不改。
