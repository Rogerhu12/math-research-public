# 独立公开 run07：完整 warm 与 R690 reference 必要输入

## 1. 范围和实际状态

本批只准备下一完整 reference-centred normal 方向所需的两个实际输入生产器：原完整 warm recipe，随后原完整 R690 axisymmetric reference。它不是已完成科学结论的重复证明，不调用未返回的 seed19，也不把其未知后续地点当作空集。`finish_when_done=false`；后续完整科学来源和适用历史消费仍由独立完整参数明确追加。本说明及四件入口尚未执行科学计算。

截至本次准备，run05 `45870334713/1`、job `140083791897` 的科学控制器仍由 GitHub API 报 `in_progress`。公开索引只到实际18，当前 seed19 未返回。对该 job 日志先实际作 HEAD：GitHub API 返回303，独立下载实体 HEAD 返回404；没有可供有界尾读的日志实体，也没有整读未知大小日志。不能由旧索引推断子进程停在何处。

本批不声称新 run 的 warm、reference、profile 或 field 与旧 run 逐字相同，也不因元数据或 SHA 改变而声称数学目标不同。实际新输入生成后仍须按完整 scalar 定义、chart、carrier、源和自由变量身份绑定。有限格点覆盖与历史 protected/typed/线性工作集的责任不是同一件事；本 bootstrap 未改变任何一项。

## 2. 已公开规则提交

请求的 `rules_read_commit` 是已由公共 GitHub branch API 实际确认的提交：

`5ba0a710721368db72afcd4cb1a9400844bf0c26`。

随后分别以此确切公开 ref 读取两份 README，并核完整文本 SHA256：

| 文件 | SHA256 |
|---|---|
| 根 README | `581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102` |
| 本题 README | `3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d` |

两者均与已读规矩一致。这不是未发布的本地 commit。控制器首次真实 pull 及后续每次 publication pull 仍比较这两份 README；变化时打印实际差异并停止该控制器等待研究代理读取新规矩。既有周期3000秒规则检查保持原字节。

## 3. 完整必要输入闭包

第一项是已公开完整 `rebuild_axisymmetric_so3_warm.py`，22706 B，SHA256 `561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4`。请求仍给 `stop_after=warm`。该完整 recipe 保留原五段 prefix 恢复、pulse 和完整 warm producer；不传 `--implementation`，不启动旧 af89/e8/QP 方向。它实际生成后继所需：

- `fullclosed_solver/data/fullclosed-hold-warm.npz`；
- `fullclosed_solver/data/fullclosed-hold-warm.json`；
- `fullclosed_solver/data/pulse-a5-complete-base.json.gz`。

第二项完整来源是 `resume-20261126-run05-returned-steps-archive-001.json` 的 `complete_objects[0]`。新对象只改 `id`、说明 `scope`，新增完整来源记录 `reconstruction_source`。下列科学字段逐值完全相同：`script`、`parent_bundle`、全部有序 `args`、`outputs`、完整 `summary`。

其实际完整 producer 是 `so3_axisymmetric_reference.py`，SHA256 `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3`。完整参数仍为 N2048、seed integration order8、panels128、scalar admission300秒、积分容差 `1e-18`、尾截取 `1/8`，以及原 `a04_historical_location_seeds.json` 全部十一份历史 payload。M160、J923、1845 legacy 加5532 Gauss 的全部7377 observation 保留。没有缩小变量、删除尾、借旧优化场作 T0 或用 SHA 生成 raw。

五项完整输出仍是 `axisymmetric-R690-reference-v2-first/` 下的 `report.json`、`reference.npz`、`observations.npz`、`locations.json`、`supplied-location-provenance.json`。后继必须使用这些本 run 实际返回身份；此处不预填任何输出 SHA 或数值。

## 4. 独立控制器和触发

`public_actions_controller_parallel07_compact_metadata.py` 是完整已修05控制器9aa09573的副本，仅把 HANDOFF 标记 `parallel-05` 改 `parallel-07`，把对应中文标签 `Actions05`/`并行05` 改07。其它源码完全相同；`controller-05-to-07.diff` 保留精确差异。仍导入完整 `public_actions_followups_compact_metadata.py`，SHA256 `3cb1e706ab43dac6e952ce00b41e83055112d2ee65edb37682d1f05e94f2ee3f`。真实子进程返回事件在 publisher 之前落 runner，cleanup 只在公开渲染副本压缩；完整原 cleanup 明细保在 runner。

原58000/60000字节单条及分卷、95000字节队列/索引、10000字节 HANDOFF、200000000字节题目录守卫均保留。根代理在发布前须先为新07 HANDOFF 槽留下实际容量；本说明不削弱守卫，也不修改其它槽。

新 workflow 的公开路径为 `.github/workflows/visible-larger-centered-normal-20261126-07.yml`。它监听 main 上唯一请求路径 `topics/visible-flex-larger-amplitude/computations/resume-20261126-actions-request-07.json` 的 push；也保留 `workflow_dispatch`。并发组独立且 `cancel-in-progress=false`。job350分钟，controller budget20000秒，原持续准入机制不变。Python3.12.14、NumPy2.3.5、SciPy1.17.0、CPU Torch2.5.1、所有线程和依赖来源参数逐字沿用原完整 workflow，不通过新本地 fixture 或科学前门。

## 5. 旧实际耗时仅作安排依据

run05 第1卷为53029 B，SHA256 `6eca69a388330b3e539aac4e2c793ce8256c724d52abf11adc8c8e85d49d08b3`，实际记录 warm `130.617365684`秒、完整 reference step `308.66245129099997`秒，合计约7.32分钟，未包括依赖安装、排队和 publication。

这只是已发生的原输入构造时长，不是 run07 的保证，不包含后续历史生产、seed 平均值、normal 根、QP 或连续证明成本。新原始 scalar 求积是实际限时自适应过程；其新字节和数值精度必须实读。

## 6. 本批四件及实际静态检查

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `public_actions_controller_parallel07_compact_metadata.py` | 19006 | `9a554b0613a2a6766c25c27f46d5fa3d96c9291af0da475aebefd46ee5d63aea` |
| `visible-larger-centered-normal-20261126-07.yml` | 2238 | `a3baddc9a489b44f0a444ae2bc740fdb0239ece83d3c8aa8f9ea164afc507c7e` |
| `resume-20261126-actions-request-07.json` | 2361 | `ba0f4a6afa1e7c7491b1c6e8584f5fe2955192695eb32b5d89a92c26de795337` |
| `resume-20261126-followups-07.json` | 6078 | `8416f67f118d2e90503901f1bad0dc604f8477a6e035d3f05de4fd3f192722c5` |

实际只执行了纯文本/JSON/AST/compile/哈希检查：控制器全文相等替换核；完整原对象五个科学字段相等核；两份 README 公共 ref 和本地字节 SHA 核；四件无尾空白；队列6078 B低于原95000界。未 import 科学模块，未计算 F/J/root/QP，未修改仓库/refs/活动队列，未 dispatch。

完整新方向、全部适用历史消费、连续度量和几何、固定问题精化与 README 完成标准均未由本 bootstrap 支付。下一必要构造可以先并行运行；是否以及如何消费未返回 seed19 的位置/保护责任，必须在独立完整来源和明确新算法契约中处理。
