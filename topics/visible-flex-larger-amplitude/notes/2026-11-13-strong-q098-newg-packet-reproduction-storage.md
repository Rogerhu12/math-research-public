# q098 径向派生包的复现与存储补记

作者：`/root/geometry_audit`（GPT-6 Astra Pro，AI 辅助），2026-11-13。

依据根 README 规11，**35个可在约77秒内从原接受数组重新生成的径向派生块只保留工作区，不提交 Git**。仓库保留完整源、原命令及资源、contract、原运行 manifest、完整 SHA 清单与数学说明；昂贵接受解的原始 physical/raw/tail 数据仍是已归档的输入。

此前 `2026-11-13-strong-q098-newg-patch-mean-archive-manifest.json` 的 SHA
`9d05daad01c1c8e7f701ff8b4b485851b2ef86f77f74cef069c16ab4e4ce8139`
保持不变。它是完整执行产物目录，包含当时暂放入题目目录的35个派生文件名；其中列出的35个 `radialNNN.json.gz` 现在按本补记排除出版本库。这项存储调整不改变数学输出、输入身份或已通过的端点门。

正式提交文件清单见 `2026-11-13-strong-q098-newg-patch-mean-compact-archive.json`。其中单独列出35个 `scratch_only_derived_chunks`，每件记录实际工作区路径、SHA、字节数和完整原区间范围。工作区原块位于：

`/workspace/scratch/d1aa462cfc02/geometry-work/q098-newg-packet-r1/packet-radial000.json.gz`

至 `packet-radial034.json.gz`。已有实际输出不重算，仅逐件核保存身份及覆盖后保留。

## 完整再生

在题目目录运行下列命令，所有相对 `notes/...` 输入拼写保持原样。`/path/to/pinned-topic` 指恢复出的原 source revision `869436630c99aa5a68afb55bd8877c826034d117` 的 `topics/visible-flexible-closed-surface`，并包含原 `source-origin.json`。输出前缀必须是全新路径。

```bash
python computations/strong_resource_run.py \
  --out /fresh/output/q098-packet-resource.json -- \
  python computations/strong_newg_patch_mean_packet.py \
  --input notes/2026-11-13-strong-q098-m28-newjac-actual-r1.json.gz \
  --raw notes/2026-11-13-strong-q098-m28-newjac-actual-r1-raw-collocation.json.gz \
  --tail notes/2026-11-13-strong-q098-m28-newjac-actual-r1-tail-response_0003.json.gz \
  --source-topic /path/to/pinned-topic \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --interior-audit notes/2026-11-13-strong-q098-interior-fullmean-audit.json \
  --angular-panels 96 --intervals-per-chunk 64 \
  --out-prefix /fresh/output/q098-packet
```

原 source SHA 为 `53e8ced73a96becf434f3e8c2bca5caf2ea8240b717e7b67dfce36901a393210`。输出的35块按序与紧凑清单逐件比较完整 SHA；块内容使用准确原 binary64 有理值、准确 fmpq Bernstein 变换、确定的128bit向外端点、排序固定的 JSON 和 `gzip mtime=0`。全部2211区间、85状态、三阶次的科学数据可由原输入完整再生，不依赖有限采样或缓存。

原运行 manifest 与资源记录包含 elapsed/RSS 等运行观测，新运行这些值会变化，不能要求整个新运行 manifest/resource 的字节 SHA 与旧运行相同。数学 chunk 及 contract 的 SHA 则按同一实际输入身份逐件核；若恢复改变了输入相对路径拼写，应先恢复原 `notes/...` 拼写，不能通过重标 SHA 隐去差异。

原执行资源、原完整 run manifest 和35块科学 SHA 共同保留原 formal0 证据。本补记没有把完整径向状态 jet 改称连续 Cartesian、mean、闭面或 reach 证明。
