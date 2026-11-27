# Run06 actual41：完整缓存后退锚 SOC 方向的真实返回与新 PCG 准入

## 1. 实际范围与原证据

公开运行是 [45904402595/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45904402595)。本条仅登记其实际第 41 步 `complete-normalized-parent-cached-backtracked-SOC-v2-20261126-rebuild06`，不把重建命令当作旧 run04 数值或地址集合的逐字再现。

第 41 步实际 `completed`、退出码 0、控制器计时 `2584.1379223000004` 秒。完整公开小卷是 `notes/2026-11-26-public-actions-45904402595-1-part-004.md` 的阶段 39–41 版本：Git blob `f23c4e5c7ab1af09f92fd0f0c487b6e22d48454a`，31,725 字节，SHA256 `56413f1bbe6e2f5e6f1340ce9700d707cfd4f968305c6d00e4a118fe2c452ff8`。其中第 41 项完整保留实际 argv、全部输入、输出、源码提交、公开摘要和清理元数据；`summary_errors=[]`、`missing_outputs=[]`。30,797,988 字节原科学报告只在 runner，未通过连接器整读或另存 Git。

索引在 `2026-11-27 02:37:04 UTC` 已将第 41 步列为完成，并把当前阶段明确记录为 `complete-current-PCG-from-actual40-after41-independent-pair-20261127-run06` 的 `running`。该索引 Git blob `3b91c590c8c096828dd635e0e37e183861fe47e7`，6,758 字节，SHA256 `86dccfec995afcc4f17485fd78f9d19fc467c18ff8a94e7eaf7519b535103eb9`。这只证明新分支已准入并启动，不证明其已生成方向或通过任何数学检查。

## 2. 源码与真正的父场

| 项目 | 实际身份 |
|---|---|
| 完整 launcher | `launch_so3_cached_interior_separation_soc.py`；SHA256 `6c594f20adba3fa519a10c68669a42e099fd6d1d24f2e5f4fa49ff583b4b038e` |
| 完整科学 driver | SHA256 `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8` |
| 实际科学源码提交 | `cbe78160ad9a65743ff6bfa49cc4b8623c90ed46` |
| 完整行 helper | `e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021` |
| 全行投影源 | `a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e` |
| 固定物理参考 bundle | `d466ef7605281dcb951f821fe2de08953c53eb3a021a08a436f9529c6af4de04` |
| 真正自由变量 restart / 初始 bundle | `75f0fd9fab2b2c542fdaf3da6fef970332e252d6da364e35a19219420c46bdd3` |
| restart 报告 | `e62c283ee56a36e82e626762f002c484a5bd5209ad576813983784a64d6f3d84` |
| restart 完整 driver | `0f542de9ab1f91f5ca27a0efe315b0ee96beddd3e3972ba12fbc5140221623a6` |
| 本 run 模型 | `b28b7f76ea615cb317b4ca98f0d4b75a67c1e2792abc47e6f86c91266773d086` |
| 固定标量目标身份 | `364e73ce2ed258b923c0dff10a1c4dfdc846e143930d4c56b55944d0d2c18853` |
| 完整坐标范数身份 | `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa` |

报告 schema 是 `complete-normalized-parent-cached-interior-separated-SOC-v1`。参考 bundle 与自由变量 restart 是两个不同职责，不能把固定参考的 `d466` 当作这一步实际起算的自由点。科学入口在本 run 实际第 40 步的完整 `75f0` 自由点上继续；其初始新文件 SHA 与该 bundle 全字相同。

实际使用的队列版本来自 `f71e5cc32fb4d2dbfcd4f176c7ebd54e56831111`，SHA256 `bd9f89b6fb6476cc0c373ca6313f28df5cd3696486dccbf39c1cecd701d1b3c4`；控制器记录该次 checkout 为 `436fabfd264165e875e305d6fec5efd53b5fc97b`。后续队列归档与插入新分支，不改写本项已实际执行的 argv。

## 3. 完整数值参数与来源保留

本项原 argv 完整见上述固定 Git blob。本条归纳其全部数值选项，保留来源和父报告职责：

| 选项 | 实际值 |
|---|---|
| eta 起始节点；全角数 | `885`；`2048` |
| 径向块；角块；径向积分阶 | `64`；`8`；`8` |
| 坐标范数；径向长度；角向过渡 | `jet-sum`；`.05`；`24` |
| CPU torch 线程数 | `4` |
| metric 阻尼；方向预算；内层预算 | `.01`；`1`；`64` |
| restoration 阻尼；方向预算；内层预算 | `.01`；`4`；`64` |
| ray 预算；原几何行数 | `15`；`192` |
| QP atol；rtol | `0`；`1e-6` |
| reach 比例；真实筛安全阈值；活动带 | `.03`；`.992`；`.025` |
| marked 直径；见证下界；H floor | `4.2`；`.9`；`1.01` |
| 谱目标 p；epsilon；scale | `4`；`.001`；`.05` |
| legacy 正测度比例；目标误差参数 | `.5`；`1e-9` |
| 标量准入秒数；积分容差；尾切点 | `300`；`1e-18`；`1/8` |
| restoration 内缩余量 | `1e-8` |
| SOC 轮预算；tau；内缩比例；投影容差 | `8`；`0`；`.125`；`2e-11` |

实际完整变量数仍是 `1333370`，逻辑全角残差行数 `45324288`。本条不把后者当作 quarter bridge 的实际存储行数。

固定参考来自本 run `deep-fixed-scalar-amplitude-first/{final.npz,report.json}`，载体与节点分别来自 `deep-fixed-scalar-prepare-first/{observations.npz,nodes.json}`，原 scalar 输入来自 `fullclosed_solver/data/pulse-a5-complete-base.json.gz`，完整初始地点 manifest 为 `deep-fixed-scalar-prepare-first/locations.json`。restart 是本 run `so3-closed-actual-profile-interior-restore-first/{final.npz,report.json}`。缓存 donor 是本 run `so3-closed-actual-profile-first/frozen-parent-meridian-cache` 与其完整 `report.json`。没有下载旧 run 缓存或凭旧 SHA 合成父场。

## 4. 同一次真实重读中的下降和有限几何

| 原报告字段 | 本步实际初始 | 本步实际末态 |
|---|---:|---:|
| 有限观测最大 metric/Gram 残差 | `0.036852426460348` | `0.03657742603151771` |
| 原 Phi | `0.006837042552562241` | `0.006661487025358274` |
| 完整当前有限筛的最大 g | `-5.35015665104055e-09` | `-2.8896830484015368e-09` |

末态 `final_geometry_feasible=true`、`all_permanent=true`。最终永久曲率地点计数为 `2871`，永久半径地点计数为 `2821`；这些只是实际计数，不能代替地址集合、保护角色或各 typed 行的完整身份。本步 raw 报告会作为新 PCG 分支的必读完整 manifest，从而消费本步真实新增地点。

本步 `metric_count=1`、`restoration_count=0`，停止原因为 `declared_metric_direction_budget`；最终 metric 与 restoration 阻尼均为 `0.01`。原 Phi 与自由点确实发生改变，但公开摘要未给 `accepted_metric` 数量字段，本条不把 `metric_count` 改名为接受计数；也不从 driver 名字推断最终采用了 corrected SOC 或原 ray。

第 40 步的末 bundle 与本步初始 bundle 全字相同，然而第 40 步已返 Phi 为 `0.00683704255256235`，本步重新读取为 `0.006837042552562241`；两次有限 max、g 也有末位差。以上下降只在本步 own initial 与 own final 之间作比较，不用前步旧 Phi 冒充本步 baseline。

## 5. 缓存与成本的真实记录

| 字段 | 实际返回 |
|---|---:|
| adopted cache entries | `2213` |
| missing entries | `15` |
| fresh entries | `5` |
| cache prepare 秒数 | `9.882097796999005` |
| 完整 setup 秒数 | `399.65287753099983` |
| driver 总秒数 | `2575.5652588209996` |
| 控制器子进程秒数 | `2584.1379223000004` |
| peak RSS 原字段 | `3454320` |

缓存 manifest 为 `5a7b60b17f64e7a45793160ea4a2529d7dc93ac72fe3965ea0ad5d04ed2249a6`，`cache_completed=true`。三个 cache 数量保原字段语义，不能仅凭这些数值推断缺失条目与新计算条目的集合关系。

返回后，控制器仅按已登记规则移除了一个新生可重算行缓存，原记录 `3232088880` 字节；完整清理细目留 runner，其公开 canonical metadata SHA256 为 `27b3344c8cfa81bb04f4faf21eb3a6b128f400fb2bd4aa541b76dc1b6583d22e`。此记录不表示删掉父输入、报告、末 bundle 或永久地点。

## 6. 本步输出与仍未读取的方向细节

| 输出，相对于本 run research 目录 | 字节数 | SHA256 |
|---|---:|---|
| `so3-closed-actual-profile-cached-backtracked-SOC-v2-first/report.json` | 30797988 | `8a8b0fcb42a240f6e5d200c884d856415d4a01a27af9dd4174bb13502200b180` |
| 同目录 `initial-new-field.npz` | 10720258 | `75f0fd9fab2b2c542fdaf3da6fef970332e252d6da364e35a19219420c46bdd3` |
| 同目录 `final.npz` | 10720258 | `4b2bfc8002c2c7dc34f5fae6d135aa7063435685e0f940a6a19e68ca9c61d79e` |
| `so3-closed-actual-profile-cached-backtracked-SOC-v2-first-command.json` | 15215 | `d479f0bce6b56f97f07c8e8d1ee3a3b95bb359d7298367efedf272e8bbf3628a` |

本公开摘要**没有**给出实际 alpha、末 projected-gradient/tolerance、内层收敛状态、末活动面、各 SOC 轮、修正与 fallback 的真实排序或接受种类，也没有给 J/J* 成本。它们不是零，不由 64 预算或 `complete=true` 推为收敛。原纯报告入口的后继是否实际返回须单独读公共记录；本条不重跑科学方向来填空。

## 7. 新 PCG 分支与本次结论的边界

新 `b527` pair 是已经独立刊载的完整当前八列 PCG/SOC 分支：以真实第 40 步完整 `75f0/e62` 为自由点父，显式读取本次第 41 步 `8a8b` 报告的全地点，保留四次原历史后继与原 history-PCG 队列。它没有把第 41 步末点 `4b2b` 偷换为自己起点，也没有把四个未返后继说成完成。02:37:04 的索引只确认它此时 running。

本条成立的数值结论是：原完整 `892f` 在此真实父与全有限筛下，返出上述新的完整末场，own Phi 与有限观测 max 均下降，末场通过现行有限几何筛。它没有完成全域度量证书、全 t 几何证书或固定同 g 的实际精化，不构成原题完成或不可行证明。
