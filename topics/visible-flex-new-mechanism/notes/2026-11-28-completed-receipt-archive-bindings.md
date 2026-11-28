# 已自然结束计算的原始终态与接收归档

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。本记录只绑定原有科学工作及其可继续输入；两接收器均未执行新科学求值。Actions 的 success 不是数学通过。

## 八份原始终态

首次接收器 [run 46158534504](https://github.com/Rogerhu12/math-research-public/actions/runs/46158534504)，job 141020428088，源提交 `1858f6a734922868935e9fffa853ec0c4a72b1ce`，自然成功。接收耗时 33.904191173 秒，科学求值数为 0，failures=[]。原已完成日志分别只读一次；不是重跑原源代码。

artifact `15268777040`、`visible-completed-receipts-46158534504-1`，5,268,344 bytes，ZIP SHA256 `4984be237dfef952f2e1406b67c42ddeb072344790fe1ecb490eb46bc1bc84c0`，到期 2026-12-28 15:12:04 UTC。每项均有 `Rxxx/final.json` 的原始 literal、source、paid-events；R705 另保原已付状态 ZIP。未来消费者须核 run/head/attempt、artifact 元数据与整个 ZIP 的字节身份，再核成员，不从摘要拼造参数。

| 项目 | 原 run / job | 原 source head | literal FINAL bytes / SHA256 |
|---|---|---|---|
| R695 | 46148919282 / 140990956410 | `9d2e6c88623a42b351b65e9bf5eb502631839253` | 2134905 / `443e1e0b9066d398bce833acb6facc7616ccf205914ebee8dc8acfb7d2e9f33d` |
| R711 | 46152161518 / 141000942072 | `9e577e4e27e0b4b9d7a8ce29542d05147c23c54f` | 272843 / `db82b8eebb3d582cecb3452be5a96650011f9628d0cc1f6f7b68fe11315a7a97` |
| R643 | 46134171516 / 140945669998 | `bc7799966d423e6ee7bb43f19c7a5549c8eb3dbd` | 767450 / `70ee43cfad39392f013f05ef1404e765eadfcc33405e993d2041b96d20367f61` |
| R631 | 46133637169 / 140944040121 | `df0c989652a0f243a1bae3cb37e116932455cc99` | 129649 / `1b4f32b1c49c79a65cbe2496ed9e97c48277376803c6cbe6eef418ad7e4c5ad3` |
| R702 | 46150227928 / 140995038056 | `89f416b3c39057ef22441e194f343a24553ebe27` | 4911306 / `9c82b6348f075264b45654b49bbc77e63424cd0bd677ec103a26da563b343f79` |
| R707 | 46153308216 / 141004422866 | `427914e2e6ff476e78d0a73e4e66b4771ed6c396` | 530466 / `74037bee236af9cb69b2aec58c9d4f4100c91b80963b38c7151556db4295f024` |
| R705 | 46153586472 / 141005268888 | `0fafb2760fe60ae072f1754dd1daa7983c42b5a3` | 46941 / `3d50b5292c8a3dff23e3369f2aaaf833bbb9b4d372628f3cfb33157386d40204` |
| R703 | 46151140087 / 140997832329 | `1b2ba533d51b4f4b416d30dcee1aaa516b2c64be` | 39163 / `bd5a52dcc40e31e898d3e02b99e4e5c0d449bfd697ac95faa8a168082c6012b2` |

原 JSON 的字面字节 SHA、排序键重编码 SHA、float64 小端打包 SHA 是三种不同身份，不互相冒充。全部原历史、拒绝、费用及未完步骤仍在对应 literal 中。

## 缺失细字段及 R714

第二接收器 [run 46160444905](https://github.com/Rogerhu12/math-research-public/actions/runs/46160444905)，job 141026351719，源提交 `84e75e64d3f20c230691db17e0330c6b00bab983`，2026-11-28 15:33:00–15:33:08 UTC 自然成功。I/O 3.181919059 秒，科学求值 0、原八份日志新请求 0、R714 原日志请求恰 1，failures=[]。旧八份只消费上述已验证 ZIP；保留全部选中原字典字段，长数值数组只在报告中以身份引用，原 literal 仍取首次归档。

artifact `15269471319`、`visible-completed-receipt-detail-46160444905-1`，369,435 bytes，ZIP SHA256 `ed0eb01838ce3a8668e7d4851cae6a42dd1baab398b47b73a0bd76dd12501a15`，到期 2026-12-28 15:33:06 UTC。内有各项 `Rxxx-details.json` 及 `R714/final.json`、source、原 partial（若有）。R714 原 run `46154358456`、job `141007604570`、head `015a97501eeea47636826c4fe655a5dbf89d8c98`；literal FINAL 为 912,015 bytes / `68e30fc5e115d6bfde3f044eb1637b25d7892baa2cee1bb5f0ca34c646408009`。其原 41,008,609-byte 日志 SHA 为 `fa23fd64edfce18091fa3103ab5233c68def12871187aee7bc63f5382f650f57`，没有把大日志入库。

接收脚本分别为 `completed_receipt_recovery_20261128.py`（17,825 bytes，SHA `c4c11a492e0aa6c066a98b09e99b6615ca9d903502890034ce98f832bfd321e8`）和 `completed_receipt_detail_20261128.py`（23,648 bytes，SHA `7f32ba4b50cfc92731980e55878bed2c7b252652850629d7729996b746296ecc`），workflow 均固定源身份、只读权限，后一脚本也固定前一解析器身份。原始科学结果逐项另记，不能把数组投影或日志接收成功当全点证明。
