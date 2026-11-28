# 旧 Hermite v=.25 开放前缀的完整来源保全与普通退役

日期：2026-11-28。固定读取版本：`922382c228b1c8449cf3119a1cd5447185dc512b`。

本批仅建议从当前树普通移出 `notes/alternative-hermite-k045-v025-s065-m64.json`（290,388 B）。完整原数据仍可从固定 Git 提交逐字恢复。生成源码、完整参数、小结、失败记录、后继输入义务均保留。Nelder 候选未闭合原驱动来源，继续保留。本批没有读取这两个大数据文件，没有执行任何数值、Python、AST、fixture 或重跑；solver 没有删除文件、修改 ref 或队列。

完整台账：[legacy-hermite-v025-complete-retirement-provenance.json](../computations/legacy-hermite-v025-complete-retirement-provenance.json)，33112 B，SHA256 `409d9ade4d48ac9baa98a72a05e636a4a3b35b79b840f06c9b55ed4ea7c261c1`。

## 1. 原输出身份与已有完整记录

| 项 | 原身份 |
|---|---|
| 路径 | `topics/visible-flex-larger-amplitude/notes/alternative-hermite-k045-v025-s065-m64.json` |
| 字节数 | 290388 |
| Git blob | `764ccc0e6c03ddd3f840d577b288d2d14d9976fe` |
| SHA256 | `6d3ef805cb86aa901e51dc936af3027f4cdb89866caae7bcfc23239361443be6` |
| 当前元数据固定提交 | `922382c228b1c8449cf3119a1cd5447185dc512b` |

大体 SHA256 来自已刊完整小台账 `resume-20261126-legacy-three-late-boost-retention.json` 的 `/records/3`，本次没有重新下载或散列大体。该台账 25,858 B，SHA256 `2acac3ce6a794bd1aa1f8426dd310446e419c6f14dbc8d53263d7c4b3dfc174f`，blob `18775acb6eb83d70d9f6ac7d4585e56e41f98d6c`，已全文读取。新台账逐值保留该项全部非轨迹字段、原 41 行/41 状态/194 个末系数的计数与首末保存诊断；完整数值轨迹仍由固定 Git 提供。

原报告为有限 Fourier Frenet IVP 的开放片：从 s=0 实际到达 .65，status=success；原 seconds=29.14717388153076、calls=31580。保存的全样本 metric 最大值为 1.234212732015294e-11，曲率最大样本为 5.157343605233196，最小 Frenet margin 为 .8000934832296572。它不是闭面、连续域曲率包络、reach 或全时族证书。原 Python/NumPy/SciPy 版本、OS exit code、Actions run ID 未记录，仍为 null。

## 2. 实际生成器及完整输入

真正生成器是 `alternative-controlled-profile.py`，不是名称相似的 `alternative-hermite-cycle.py`。前者 7,561 B，SHA256 `0af61a3bfccf093bfe6c255f864c658c37119b890f362d5d2e16429d2969e430`；它完整动态载入 `alternative-outward-probe.py`，7,708 B，SHA256 `cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb`。本次两份源码全文已读，其完整 Git 身份和恢复版本在台账中。两源不改字节、不退役。

该次选无 `--input` 的原分支，全部初始 194 词由源码的 A=.38、M=64 确定：先全零，再设置原五个非零位置；没有依赖不可重建的外部初始轨道。N=1024。物理 profile 是原 `HermiteOutward` 的 v=.25、S=.65、k0=.45，原固定 metric 参数身份为 `a54b7030d158020cffbab506024e6936c9d2c1c6f296d9de3bc7ff2d30a7c993`。

完整语义重建 argv 已在原台账 `/reproduction/recipes/0` 和新台账完整保留：

```text
python topics/visible-flex-larger-amplitude/computations/alternative-controlled-profile.py
  --A .38 --M 64 --N 1024 --v .25 --S .65 --k0 .45
  --coast .1 --turn-length .4 --turn-speed -.6 --turn-fraction 1
  --rtol 1e-11 --maxstep .00025 --steps 40
  --out {work}/alternative-hermite-k045-v025-s065-m64.json
```

没有 `--input` 时，coast/turn 四项不参与此分支；其完整默认值仍保留。原字面 shell 命令没有记录，本段是源码和保存 config 对应的完整 argv，不能冒原命令逐字符转录。

原程序用 DOP853，atol=rtol*.01，每段 max_step=min(maxstep,(right-last)/2)，完整 40 宏观段保留成功状态；异常记录 repr(e) 并保最后成功段。完整 Fourier 投影、径向与角向 jet、域拒绝、数值统计都在原源码。线程环境的三个原设置也在台账。此处仅保存复现责任，没有安排重跑，也不宣称不同软件环境重算会逐字复现旧 JSON。

## 3. 实际消费者与祖先恢复义务

三个直接消费路径均由本次完整小源阅读确认：

- `alternative-controlled-profile.py:main` 的 `--input` 分支读取 config、reached_s、全部 final_coefficients 和继承样本误差，按明确的三个 Fourier 块映射到新 M，并登记整输入 SHA。原三次 late-boost 的完整源、参数、返回和失败在既有三段台账中。
- `geometric-alternative-core-screen.py:Prefix.__init__` 要求从核心开始的全部保存状态；以原有限 ODE 两 jet 重建五次插值，保真实竖直均值。其完整原参数为 widths 0/.05/.1/.2、angular 1024、radial 201、phases 33、polish 20，另原默认 core_angles 512 和 flat_radial 41。
- `geometric-cylinder-prefix.py:history` 递归读取每一 input 祖先并核整 SHA；`Trajectory.__init__` 检查完整状态、无间隙接合以及两侧 jet 差。实际 9,501 B 小返回的 `/manifest` 同时保存此 Hermite 原 SHA 和 late-boost M96 的原 SHA。本次也全文读了两消费者共用的 `geometric-alternative-geometry.py`。

后两读者及共用模块完整源码留在当前树。其读取规则不改。后继要消费原轨道时，应在 runner scratch 按旧相对路径恢复完整祖先链后再调用原 reader，不把近似重算值代入带原 input_sha256 的历史报告，不只恢复 late-boost 晚段然后冒完整前缀。

已有三段台账的 `/records/3/action=keep_ancestor_in_current_tree`、其复现说明的当前树选项，以及双 boost 台账的 `still_present=true` 是当时的可用性事实。本批新记录明确覆盖这些**可用性表述**：普通退役后使用固定 Git 恢复。旧台账本身和旧数值结论原字保留，不修改历史。

旧共振 late-boost 曾以 `FloatingPointError('domain at s=0.804067010527, margin=-0.008567397412')` 失败；最后成功段仍保。双 boost M96/M128 到达 s=1.15 但误差未过目标、且遮挡原 .76 见证的结论也完整保留。退休祖先的当前树副本不删除或升级这些失败和限制。

## 4. 精确恢复与科学重算分开

台账给出固定提交、完整路径、Git blob、字节数、SHA256 和可直接执行的恢复命令。恢复从原 Git 读取整个文件到 runner scratch，不解码、切片、差分或重新包装数据，也不把输出上传为新 Git 文件、Release 或 Artifact。以下命令未在本次执行：

```sh
LEGACY_HERMITE_ROOT="${RUNNER_TEMP:?}/legacy-hermite-v025"
mkdir -p "$LEGACY_HERMITE_ROOT/topics/visible-flex-larger-amplitude/notes"
git show 922382c228b1c8449cf3119a1cd5447185dc512b:topics/visible-flex-larger-amplitude/notes/alternative-hermite-k045-v025-s065-m64.json > "$LEGACY_HERMITE_ROOT/topics/visible-flex-larger-amplitude/notes/alternative-hermite-k045-v025-s065-m64.json"
printf '%s  %s\n' '6d3ef805cb86aa901e51dc936af3027f4cdb89866caae7bcfc23239361443be6' "$LEGACY_HERMITE_ROOT/topics/visible-flex-larger-amplitude/notes/alternative-hermite-k045-v025-s065-m64.json" | sha256sum -c -
```

三份已退 late-boost 原数据可按既有台账的固定 `9bbafc1e43290eae0a592245e39f291ff51051c7` 恢复；新台账给出全部逐项身份和原完整参数 JSON pointer。它们不计入本批新增释放，也不再次删除。

本批阅读的已知消费者都显式接收输入路径。这里不声称进行过仓库所有未来动态路径的穷尽证明；保存的是实际读者与完整恢复合同。既有索引列出的旧说明、完整小返回、失败说明和所有源均不动。

## 5. Nelder 候选继续保留

`numerical-m2-tail-gate-nelder.json` 的 519,142 B 正文未读取。本次全文读取其 1,017 B manifest、1,753 B input、1,835 B config 和当前 3,663 B wrapper。原 manifest 记录 driver SHA256 `f7d0b0bff82c1bbf1314216a19947d5a5e24ef5929b980dc822c46f123551331`，当前 wrapper 为 `7b7a8618b44ce21de07c671164abe0ec22725c57ffd995b947a48d6da2e054cb`。

当前路径历史只返回初始快照；仅去掉可见 sourceRoot/env 接线行也不匹配原 driver。故不能把当前驱动冒充原驱动，原输出、输入、config、manifest 和源码全部继续保留。本批不把这 519,142 B 算作回收，也不报告未读原搜索的成功、最优值或终止状态。

## 6. 发布边界

本包仅提供完整建议、原身份和恢复账。root 将决定并执行普通提交，且只允许删除总表中的一个精确候选。新增小记录的净容量由最终总表给出。没有新科学结论、求解门、测试门或运行改动。
