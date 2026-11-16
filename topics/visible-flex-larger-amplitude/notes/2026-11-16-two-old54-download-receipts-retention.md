# 两份旧 actual54 取回目录清单的当前树清理

日期：2026-11-16（UTC）。作者：ChatGPT（AI）。范围：仓库保留策略与元数据；不是新的科学结论。

## 删除的准确范围

本次只从当前树删除以下两份历史下载/解压目录清单，不删除 actual55/57 的 result、summary、逐 trial 记录，不改任一求解程序或已冻结请求。两份完整旧文件仍可在已发布的 494cc311a431553e61ad44202985e2737c6e92a2 提交中查看。

| 原路径（相对课题） | bytes | 原 SHA-256 | Git blob |
|---|---:|---|---|
| notes/public-actions-43636504089-1-directldtrial/actual54-artifact-fetch-receipt.json | 702911 | 08cf13c34e662465ea2175f5417e9541f64cc75fd32bb4dff2de2412778097d3 | faed3c4200b1e2a8a26e0f9f4067d79bafdf4902 |
| notes/public-actions-43637356027-1-dampedchain/actual54-artifact-fetch-receipt.json | 702911 | 4ccd70eef393015736691fcdbb0815c3a5b940ab5a94d26a75a677469ece3b99 | 26c4e9b65be0ade1c0712c84d461a191c987968c |

- [第一份完整历史文件](https://github.com/Rogerhu12/math-research-public/blob/494cc311a431553e61ad44202985e2737c6e92a2/topics/visible-flex-larger-amplitude/notes/public-actions-43636504089-1-directldtrial/actual54-artifact-fetch-receipt.json)。
- [第二份完整历史文件](https://github.com/Rogerhu12/math-research-public/blob/494cc311a431553e61ad44202985e2737c6e92a2/topics/visible-flex-larger-amplitude/notes/public-actions-43637356027-1-dampedchain/actual54-artifact-fetch-receipt.json)。

合计移除当前树中的 1405822 字节；本说明和紧凑日志另计。历史提交不重写，不另存副本、编码包或 artifact。实际最新总容量以后续 Git tree 的完整 blob 元数据为准。

## 内容与原始生成来源

两份全文均已读取并解析为 JSON。schema 均为 pinned-public-actions-direct-LD54-complete-artifact-fetch-v1，scientific_computation_performed=false。它们是公开 Actions 下载、校验及解压形成的元数据，主体为2293个文件的路径、字节、CRC、SHA、模式列表；没有把这份清单当作逐科学值审计或数学证书。

两份 extraction 对象与 pinned_input 对象逐 JSON 值完全相同；全部顶层字段中只有 completed_utc、current_actions_run_id、output_directory 不同。原实际调用分别为 run43636504089/attempt1（完成时刻2026-11-14T20:16:12.956485+00:00）和 run43637356027/attempt1（2026-11-14T20:25:38.727256+00:00）。各次时间和临时路径属于历史事实，重新执行不承诺逐字重现这些环境字段。

二者固定的同一原输入：run43634889730、artifact14129522378、名称 visible-mainline-directld-43634889730-1；历史下载457357361 B，ZIP SHA-256 df3a54716ecbed8645783373657f7e40b08429173ca976efc73ecc7e8ce5f819。原 source commit 为7eb383af1ca2bb04c7eaef9c65578dbc124269d8。该 artifact 的旧存在/过期字段只是原收据记录，本次没有重新访问、重下或保证其当前可用。

保留的完整生成源码：

- computations/exact_20261114_fetch_pinned_public_artifact.py，SHA-256 51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859。
- computations/root_20261114_fetch_pinned_direct_ld54.py，SHA-256 96e07ffe20e8d28f15d77c1f2acca1ff9d60b5646de1144978b0add777b82331。
- 原两次 workflow 的固定输入和输出动作均保持，不改 source pin：visible-larger-public-direct-ld-trial.yml，17146 B / 929bd093c1a3ba1043b6a8b1d0cf13c2b7a2e0d3caac9b27ef389a59015af2b6；visible-larger-public-damped-chain.yml，19136 B / 38735293705b4ea156116732fad924d7a4c1c94cb9750e34bf393e2258c13f9b。

## 实际引用检查

[公开 Actions run43832094284](https://github.com/Rogerhu12/math-research-public/actions/runs/43832094284)、job133179620547在精确494cc311a431553e61ad44202985e2737c6e92a2上完成只读部分克隆与文本引用扫描。科学程序没有执行。首次独立行政run43831861019因runner没有rg停止；第二次使用已存在的git grep -I -l -F，没有安装或改变科学运行时。

范围是整个 topics/visible-flex-larger-amplitude、全部 .github/workflows 和根README。精确搜索两条完整仓库路径、两个目录名、共同basename、两SHA-256与两Git blob。全部命中仅五个文件：两个旧workflow、actual55-ten-trial-decision、actual57-damped-chain-QR-and-original-exact-readback、actual57-original-ten-trial-no-decrease。

两个workflow的同名命中是从各自运行临时捕获目录复制 _pinned_public_artifact_receipt.json 到本次临时输出目录，属于生成动作，不是读取本次删除的 notes 路径。其余三说明只链接各自保留的 result、summary 或逐trial记录。两个完整被删路径、两SHA-256、两Git blob没有被扫描范围内的文件引用。这个结果是明确字面引用范围，不冒充对任意动态构造路径的普遍程序证明。

目前正在准备的219十六个新执行源也逐完整文本核过上述两路径和两SHA，均无命中。219的原始科学输入按独立历史commit/path/blob恢复 actual63 prefix、accepted96、原port及actual91尾初猜，不以这两份下载目录清单作为父。其它现行计算入口的 source pin、科学数据和已运行runner工作区不因当前树删除而改变。

本次遵守根README第15项，仅保生成源码、输入/运行/身份与紧凑结论，并使课题当前树低于200000000 B。没有扩大科学预算、修改参数或放宽任何原门；清理不支付尚未完成的112/fullDN、闭面、metric、reach或幅度条件。
