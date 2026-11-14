# Actual41 捕获包的独立固定 PIN 下载入口

公开 Actions run `43622149326`、job `132530011605` 已完成逐原 RK 步捕获，source commit 为 `0beffe5a963015a4063a8c53d4a92fec32205005`。下面五个值来自这次实际 artifact，既不是未来占位值，也不指向旧 actual28 包。

| 固定字段 | 实际值 |
|---|---|
| run_id | 43622149326 |
| artifact_id | 14124209116 |
| artifact_name | visible-mainline-rawcell0steps-43622149326-1 |
| archive bytes | 349636774 |
| archive SHA-256 | 356d9d81959739a22e9347d7ceba6fd4880ad61db70dca73096a4c5b71dc73a8 |

新入口 `computations/exact_20261114_fetch_pinned_rawcell0_steps.py` 只复用已冻结下载内核 `exact_20261114_fetch_pinned_public_artifact.py`。内核的完整 SHA 固定为 `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`；原文件不改，原 actual28 入口仍只接受它自己的实际 PIN。

新入口加载该标准库内核的独立模块实例，仅替换内存中的 `PIN`、回执 `SCHEMA`、以及 `public_metadata` 的本地来源追加器。原 main、环境核验、CLI tuple 全等、GitHub metadata 核验、流式 bytes/SHA、HTTPS、跨 origin 去 Authorization、ZIP 路径与文件类型检查、独占目标发布、receipt 最后移动与只读封存函数全部不改。

原回执顶层 `source_file/source_sha256` 继续准确标识旧内核；回执的 `public_artifact_metadata.local_pin_adapter_identity_not_GitHub_metadata` 同时记录新入口文件/SHA、冻结内核文件/SHA、实际41 PIN、内核原28 PIN 和仅三项内存替换范围。键名明确这是本地 adapter provenance，不能冒称 GitHub 返回字段。来源在原内核计算最终回执 SHA、移动和封存之前加入；没有事后修改已封存回执。

## Actions 调用

只在本公开仓库运行；job 具有 `actions: read`，`GITHUB_TOKEN` 仅在本下载 step 的环境传入。目标必须是独立的、尚不存在的 `RUNNER_TEMP` 子目录。命令中不放 token：

```sh
python topics/visible-flex-larger-amplitude/computations/exact_20261114_fetch_pinned_rawcell0_steps.py \
  --run-id 43622149326 \
  --artifact-id 14124209116 \
  --artifact-name visible-mainline-rawcell0steps-43622149326-1 \
  --expected-size 349636774 \
  --expected-sha256 356d9d81959739a22e9347d7ceba6fd4880ad61db70dca73096a4c5b71dc73a8 \
  --out "$RUNNER_TEMP/actual41-step-capture-input"
```

实际提取路径以回执 `extraction.files` 为准。后续动态 step consumer 的 `--step-directory` 指向其中包含 `result.json`、`rawcell0-step-summary.json`、`rawcell0-step-array-manifest.json` 的真实捕获目录，另用该已完成 result 的真实完整 SHA 调用 `--step-result-sha256`。压缩包 SHA 与内部 result SHA 是不同身份，不能混用；当前下载入口不预填内部 result SHA。

下载器仅保全输入，不执行科学运算、不构造新 J、不判定新矩阵的数值有效性。完成标志是下载 step 成功及最终只读 `_pinned_public_artifact_receipt.json`；整个目录的发布不声称原子性。旧下载内核相同的完整 metadata/ZIP/凭据规矩继续有效，输出目录已存在则拒绝覆盖。

本入口在本地只作 AST/compile 与源 SHA 检查，未在本地联网下载、未冒充已经在 Actions 验证新入口。首次实际执行的回执应另行记录。
