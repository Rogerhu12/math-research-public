# M12：已扩充 exact-query 输入的真实父链核

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。

首次 G12 原源扩充已真实产生 13185 查询，但旧 local-extension 入口仅允许父 report 的 script_sha256 等于最初 Fraction streamer。因此下一次真实 h 新查询不能直接把 G12 extension report 冒作原 producer。新 `2ecf-m12-extend-exact-tail-queries-local-v2.py` 显式支持已知 producer 链。

允许的身份只有当前注册的原 Fraction streamer、固定 v1 extension SHA `78d9d18434598cfd2174112221d26e5c57972d5e701ec66f7aeb15f1b1f89ee0` 和本 v2 的实际 SHA。每一级都核 report/cache/query-recipe/manifest 哈希，并要求实际 ancestor bundle。对 extension，还实际加载被声明的 parent cache 和当时原 streamer 生成的新半径 cache，确认二者互不重叠、恰好合成该级全部查询；每条 query_radius 和全部 coefficient 值逐项相等，不能只看 flags。所有 endpoint/原 546 诊断数组、完整原 source 二 jet 证明及原窗口/范围身份也逐级相同。新入口明确只消费原 Q-free source。

实际已对现有 G12 的 13185 查询核完：原 h487 的 4631 条 + 当时原 Fraction streamer 新算的 8554 条全部通过；自然 exit 0，2.608672686 秒，峰 RSS 291996 KiB。没有新增源查询，也没有新 h 场或新非线性结果。

下一物理 h 输入调用时，真实的 1..12000 个新半径仍由未改动 Fraction streamer 重新准确积分，24 个原 raw blobs 仍逐 bytes/SHA256/Git-blob SHA1 验证；旧源值只拷贝，不拟合、不换 g。例：

```bash
python scripts/2ecf-m12-extend-exact-tail-queries-local-v2.py --scripts scripts --manifest notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json --raw-directory <verified-original-24-blobs> --old-report <actual-G12-report.json> --old-cache <actual-G12-report.json.npz> --old-queries <actual-G12-grid.json.queries.json> --ancestor-bundle <actual-h487-report.json> <actual-h487-report.json.npz> <actual-h487-grid.json.queries.json> --queries <actual-new-h-grid.json.queries.json> --out <fresh-h-query-report.json>
```

若继续多级 h，增加每一级实际 ancestor bundle；消费者不能仅凭未知 source SHA 的自述跳过验证。`verify_actual_parent_chain` 是本次已真实执行的相同入口函数，回执列出实际被核的完整两级链。

- `2ecf-m12-extend-exact-tail-queries-local-v2.py` SHA256 `eb47b8aded42491b49ecc7314cc2563dc5a180c79dffd81cdf98f14d443a8ec5`。
- `exact-query-parent-chain-check.json` SHA256 `f478ae55ab35d9e8a4b110ea0822d5f42ed61b6b61bb0697f8206b18bb599294`。
- 实际 G12 report SHA256 `1a222405e67641f5968c3bca36d50e372356ddc9508aeaf25e2267e51b0a698d`；cache SHA256 `8c95cfeb3c5ebd186cf299d449d0835d718900c947669a8a862de6d68ff4eacf`。
