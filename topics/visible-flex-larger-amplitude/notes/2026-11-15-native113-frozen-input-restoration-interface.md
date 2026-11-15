# Request113：清理后的历史几何输入临时恢复

AI 协作记录：ChatGPT /root（GPT-6 Astra Pro）与 amplitude，2026-11-15 UTC。

这是 request113 的第二版工程接线，仍使用原 request113 数学实验；没有新实验编号、未来 run 或接受结果。本地只读源码及历史字节、检查 YAML/Bash/Python 语法，没有导入或执行数值模块。

## 已发生的启动失败

首跑为 run `43687907457`，source `7308ea262f596e4caf1cf49ab7c16cdca6a7f504`，job `132732158878`。原日志 65,777 B，SHA256 `a5e0a15ade430c551f6df14e2846824a52ebdd8167f620e92021912726284c37`。C++ 已成功编译；实际可执行文件 SHA256 为 `91efd6f2984be486609928cc1c0112bbe5fa268ae8e7ebe3f37dc57c040b0196`。

失败来自冻结的 `exact_20261114_true_tail_client.py`：`TailClient.__init__` 没有收到可选历史输入路径，因而调用 `public_asset(DEFAULT_STORED, ...)`。该函数回退到 `git show HEAD:<path>`；104 清理后，当前 HEAD 已无 `2026-11-13-strong-m28-recovered-full-audit-r1-ready.json`，命令以 128 退出。没有启动 native worker，没有新的 snapshot、方向或完整残差评价。不能由这次启动错误推断 binary128 数值实验的成功或失败。

## 最小修改及原消费者

三个 request113 科学源与 28 个源码 pin 全部不变。只修改原工作流及请求 JSON：

1. 从固定公开历史提交 `8bd267107cc8710d371f3b62c02986655ac965b0` 读取两份原 ready 字节，核 Git blob、文件大小和 SHA256，然后只写到 `$VISIBLE_OUT/frozen-geometry-inputs/`。
2. 向后续步骤设置原客户端已支持的 `VISIBLE_FLEX_FROZEN_LEDGER_READY`、`VISIBLE_FLEX_FROZEN_STORED_READY`。没有改客户端、factory 或数学条件。
3. 清理结束时，只给本请求的只读父包目录 `actual91-primal128113-parent` 中属于当前 uid 的真实目录补 owner `rwx`，不跟随符号链接、不改文件内容，再执行原删除。

历史 commit 若不在初始浅检出内，工作流按完整 SHA 临时 fetch；不切换 HEAD、不更新 main。读取前后均核 triggering checkout。恢复后的临时几何输入由原 output tree 的最终清理一并删除，不进入 Git、Release 或新的 artifact。Git 自身可能缓存历史对象；这是临时 checkout 的取件缓存，不是新提交或输出归档。

两份输入的精确身份如下，路径均相对于仓库根。

| 原环境槽 | 原路径 | 字节数 | Git blob | SHA256 |
|---|---|---:|---|---|
| `VISIBLE_FLEX_FROZEN_LEDGER_READY` | `topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json` | 109004 | `4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3` | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| `VISIBLE_FLEX_FROZEN_STORED_READY` | `topics/visible-flex-larger-amplitude/notes/2026-11-13-strong-m28-recovered-full-audit-r1-ready.json` | 29774 | `b6c44fe237750f13c8b10366f15525b481a74e09` | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

已读的原消费链为：

- `exact_20261114_true_tail_client.py`，SHA `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09`：优先使用这两个 env 文件，保原 file/hash/source 责任；同样的路径向 Node 子进程传递。
- `tail_frozen_geometry.mjs`，SHA `db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3`：把这两个路径传入原校准 factory。
- `strong_frozen_calibration_factory.mjs`，SHA `77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247`：读取内嵌 160 行表、物理参数、warp 标量及五/七点历史指纹，保其原 source/geometry 检查。JSON 中记录的旧机器 trace、checkpoint、旧 reference 路径没有被再次打开。

原 factory 其余文件来自既有 78 源恢复目录与原 `source-origin.json`；首跑这一恢复已经成功。旧95 driver 直接将真实91父 binding 的 `config` 写成当前配置，不调用 `prepare_config()` 的 `DEFAULT_CONFIG` 回退路径；本修复不恢复或替换另一份默认配置。这两份 ready 是几何来源，不是已接受 native 尾，也不使失败73/95/103成为成功锚。

## 不变的数值责任

原 fresh with-J、完整 R273 方向、全部 129248 行、两种显式 inner-root 配置、7200 秒独立 binary128 实验、额外原64完整 no-J base、原64十档控制、32 次迭代上限、`eta=1`、`tol=2e-9`、最终敏感度和完整 audit 均不变。320 分钟 science step、350 分钟 job 以及原 45 分钟真实规则同步也不变。恢复和清理没有加入数值接受条件。

仍须等待实际第二跑的真实结果。特别是完整128实验在 partial 或 error 后返回同一 fresh R273 方向给原控制路径的责任，没有改变；本修复不声称已经执行这个路径。

## 已发布文件及静态范围

完整替换 `.github/workflows/visible-larger-public-native-primal128.yml`（17706B / `db8a479b000c7ba227b0b678b6486fe6bd4f005465261bdfdddf4fc2856159af`）和 `computations/public-native-primal128-request.json`（13124B / `ce294b5eb4136dd083cf0ad17912fda85d23630192fcc223c8bf37dbc8456136`）。同编号113，仅新增工程revision、首失败身份、两历史输入身份和清理范围。完整差异保在Git历史。

本地11个Bash块、7个inline Python AST通过；原28源码pin、全部数值请求字段及既有retention字段逐值不变。root读完整两差异、原client环境槽及接口后发布；没有本地执行科学、运行factory或提前评价128结果。可重算本地检查receipt及空科学源diff不提交、不增验收门。

没有改变源文件 SHA；三个113源码继续为：CPP `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d`、bridge `3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8`、probe `ba3564ca6ef5329326861a66a948292280e2ab9e311eb8912c11d4e24d7d8409`。
