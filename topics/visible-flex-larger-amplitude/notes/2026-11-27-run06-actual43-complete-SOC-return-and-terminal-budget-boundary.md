# Run06 实际43：完整原SOC分支返回及本次公开运行终态

## 1. 结论类型与实际边界

**启发式／数值证据。** 公开运行 [45904402595/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45904402595) 的实际第43步完整返回，退出码0。它沿实际41的完整场继续原 `892f` 全空间、同固定目标、同范数与显式阻尼 `.01` 的后退锚SOC求解；有限观测最大metric/Gram残差和本步真实重读的标量目标均下降，最后的有限几何及全部本分支永久位置筛查通过。它不是第42步新PCG场的后继。

2026-11-27 04:00:17 UTC 的真实公开索引已经到 `followup_budget_checkpoint/completed`。本次读取 GitHub API 时，job `140197563689` 与科学控制器 step5 均为 `completed/success`。索引完整实际阶段为1–43；已发表的第42步原日志诊断及完整修正pure v2没有实际返回，不能登记成实际44或45。终态只说明本次执行预算已结束，不是本题完成。

本记录不声称QP已经驻点，也不声称第43步实际接受了SOC修正而非原ray：这些细节未包含在这次已经返回的紧凑科学摘要中。原始完整科学报告仍只留runner，不通过连接器整读，不转存科学数组。

## 2. 实际公开证据的完整身份

| 对象 | 实际身份 |
|---|---|
| 运行／attempt | `45904402595/1` |
| job | `140197563689` |
| 请求 | `visible-larger-resume-20261126-06` |
| 请求文件SHA256 | `4dffef76945fcb596b88201bf83fb8d41a2b12bde28f95ca2e523792aead5c8d` |
| 初始源码提交 | `5990361e45dcc35c8f5b276c17719a65ebbe386f` |
| 实际控制器SHA256 | `acff1a861a5e080fc014627b8021ff40c4fa9848e36ebfec91c4e5b49e1b256f` |
| 终态索引Git blob | `e386bbaa09e4da43569f57ff7fe4605cb12ddb3b` |
| 终态索引记录时刻 | 2026-11-27 04:00:17 UTC |
| 实际39–43完整小卷Git blob | `962fa224433b21f1ae528603b20c3dd91f82571d` |
| 小卷UTF-8字节数／SHA256 | 53359 B／`f18985f0781e1450eecca36bd8f4ed563f037fc985bdc78f0a27056057e16e4c` |
| 实际43入口 | `scripts/resume_20261126/launch_so3_cached_interior_separation_soc.py` |
| 入口实际SHA256 | `6c594f20adba3fa519a10c68669a42e099fd6d1d24f2e5f4fa49ff583b4b038e` |
| 实际source commit | `c7315d1618baa5c278088a4974f1a5ee40d9a18d` |
| 完整科学driver SHA256 | `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8` |
| 完整真实report schema | `complete-normalized-parent-cached-interior-separated-SOC-v1` |
| 实际队列path commit | `dbed6c97d0cf9c56e0065743338b1aa9559e5e33` |
| 实际队列checkout commit | `d90cf9b3722c58a70047e8e6a2acb8d7e85bf91b` |
| 本步读取队列SHA256 | `06c39c47dc1f0ba8a70743ac7580bcb98718834e3ea7a9352ed5feb59c6f2870` |

原小卷准确路径是
[`notes/2026-11-26-public-actions-45904402595-1-part-004.md`](2026-11-26-public-actions-45904402595-1-part-004.md)。
总索引是
[`notes/2026-11-26-public-actions-45904402595-1.md`](2026-11-26-public-actions-45904402595-1.md)。
以上小卷包含原记录的完整命令、输入、source、输出、cleanup和实际摘要。字节身份是实际Git blob文字的身份，不是重新排版JSON的身份。

## 3. 本步真正使用的父场、固定目标与全部空间

| 项目 | 实际43值 |
|---|---|
| 固定原reference bundle | `d466ef7605281dcb951f821fe2de08953c53eb3a021a08a436f9529c6af4de04` |
| restart完整自由点／initial-new-field.npz | `4b2bfc8002c2c7dc34f5fae6d135aa7063435685e0f940a6a19e68ca9c61d79e` |
| restart完整report | `8a8b0fcb42a240f6e5d200c884d856415d4a01a27af9dd4174bb13502200b180` |
| restart真实driver | `892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8` |
| 完整model identity | `b28b7f76ea615cb317b4ca98f0d4b75a67c1e2792abc47e6f86c91266773d086` |
| 固定标量目标identity | `364e73ce2ed258b923c0dff10a1c4dfdc846e143930d4c56b55944d0d2c18853` |
| 坐标范数identity | `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa` |
| 全部自由变量 | 1333370 |
| 原完整正权逻辑残差行 | 45324288 |
| 完整typed rows helper | `e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021` |
| 完整半空间投影source | `a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e` |

本步真正的初点是实际41的 `4b2bfc…`，其完整10720258字节NPZ被再次写为本步 `initial-new-field.npz` 并返回完全相同SHA。完整目标、范数、源和自由变量由本次report真实绑定，不能把这里的原reference身份和restart当前自由点混为一项。

实际41最后公开的Phi、有限观测max和g，分别与本步实际初始读数的公开字值一致。这里没有跨目标相减，也没有用第42步PCG末场替代父41。本步所声明的 `.01` 是原同范数坐标中的完整参数；没有把别的范数下的阻尼移植进来。

## 4. 本步完整实际数值

| 读数 | 本步初始 | 本步最后 |
|---|---:|---:|
| 原有限观测最大metric/Gram残差 | 0.03657742603151771 | 0.03644443150324783 |
| 本步真实重读标量Phi | 0.006661487025358274 | 0.006581865385378358 |
| 真实几何最大约束g | -2.8896830484015368e-9 | -4.407987308496786e-10 |

完整report `complete=true`，最后 `final_geometry_feasible=true`、`all_permanent=true`。最终完整自由场是
`0298be406a26300a40c6e355218e473e0874f42b745a5388a61b86e757c15c56`。

本步返回 `metric_count=1` 和 `restoration_count=0`。这些是实际摘要的记录计数；不能仅凭这个计数补写其接受种类、SOC轮数、原ray步长、完整QP状态或线性驻点读数。最后 `final_mu=0.01`、`restoration_mu=0.01`，停止原因是 `declared_metric_direction_budget`。

本分支最终曲率永久位置计数为 2922，半径永久位置计数为 2876。计数不是地址集合摘要，不证明跨分支位置集合相等；后续须按完整report实际字面位置及typed记录消费，或使用已经明确来源闭合的独立全有限集合政策。

## 5. 本次成本与缓存实际返回

| 项目 | 实际值 |
|---|---:|
| 控制器本步elapsed | 2647.705153157003 s |
| 科学report总elapsed | 2640.022991566999 s |
| setup elapsed | 403.19802225199965 s |
| cache adoption elapsed | 9.859080414000346 s |
| 已采用冻结参考cache条目 | 2218 |
| missing条目 | 0 |
| fresh条目 | 3 |
| peak RSS | 3551832 KiB |

完整缓存manifest identity为
`27f49c5ccc5588681416e611b192127271ad20174b8568b243a804ae65831407`，`cache_completed=true`。这些是本次真实返回的成本，不据此比较未付同等成本的其他方向，也不把冻结参考cache命中称当前全F/J已经缓存。

返回后控制器依原清理规则移出一个明确可再算row cache，记录字节数3232088880；完整清理条目的canonical SHA256为
`2c935e0e385135fad94f4a96f84c084793402c53cc336529fe37570b915cb4db`。清理范围只限已经返回的child显式生成的可重算缓存，未删除父、输入或声明输出。此后重读若要求已清理缓存，所见异常是事后状态，不能倒推为原求解或原pure发生时的异常。

## 6. 完整实际输出身份

| 输出 | 字节数 | SHA256 |
|---|---:|---|
| `so3-closed-actual-profile-cached-backtracked-SOC-v2-second/report.json` | 33351376 | `64d691e09da2e1ec41222c8917cf9a13ce6b41d56e1ea2ec5e47a18d930d4d16` |
| `so3-closed-actual-profile-cached-backtracked-SOC-v2-second-command.json` | 16228 | `76573fdc675ab0a38817fface81d4dff63c8babd2fc34fe85bf4a27b0e5f126a` |
| `so3-closed-actual-profile-cached-backtracked-SOC-v2-second/initial-new-field.npz` | 10720258 | `4b2bfc8002c2c7dc34f5fae6d135aa7063435685e0f940a6a19e68ca9c61d79e` |
| `so3-closed-actual-profile-cached-backtracked-SOC-v2-second/final.npz` | 10720258 | `0298be406a26300a40c6e355218e473e0874f42b745a5388a61b86e757c15c56` |

原始33MB报告和完整NPZ不入Git、不经连接器整读；本note只保存可复现源码、全部参数、实际run与输出身份。

## 7. 完整原参数与历史依赖

本步保留原全部自由变量、所有原均值/几何/幅度行及本分支完整永久位置。参数是：2048完整角、stage block64、angle block8、integration order8、jet-sum范数、radial length `.05`、angular transition24、4线程；1个metric方向与64内层迭代、4个restoration方向各64迭代；15个ray试步、原192前缀、QP atol0/rtol1e−6；reach比 `.03` 与真实安全因子 `.992`；active band `.025`；幅度预算 `4.2/.9/1.01`；p4、epsilon `.001`、scale `.05`、legacy fraction `.5`；完整8轮SOC、tau0、inward fraction `.125`、feasibility tolerance `2e-11`。参数没有因本次runtime或结论而删改。

显式manifest包括本run固定目标prepare locations、原SO3 actual-profile首次report、严格内点restoration report和实际41完整report。cache donor也是真实41报告与其冻结参考cache。下面逐字保留实际科学入口argv，路径中的run与实际source worktree是原返回值：

```json
[
  "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
  "-u",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/followup-sources/0015-82dfd00cd4ad-c7315d1618ba/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_so3_cached_interior_separation_soc.py",
  "--repo",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/followup-sources/0015-82dfd00cd4ad-c7315d1618ba",
  "--parent-bundle",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-amplitude-first/final.npz",
  "--parent-report",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-amplitude-first/report.json",
  "--carrier",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-prepare-first/observations.npz",
  "--node-report",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-prepare-first/nodes.json",
  "--scalar-input",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
  "--manifest",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/deep-fixed-scalar-prepare-first/locations.json",
  "--eta-start-node",
  "885",
  "--angles",
  "2048",
  "--stage-block",
  "64",
  "--angle-block",
  "8",
  "--integration-order",
  "8",
  "--norm-kind",
  "jet-sum",
  "--radial-norm-length",
  ".05",
  "--angular-transition",
  "24",
  "--torch-threads",
  "4",
  "--damping",
  ".01",
  "--directions",
  "1",
  "--maxiter",
  "64",
  "--restoration-directions",
  "4",
  "--restoration-damping",
  ".01",
  "--restoration-maxiter",
  "64",
  "--line-trials",
  "15",
  "--active-rows",
  "192",
  "--qp-atol",
  "0",
  "--qp-rtol",
  "1e-6",
  "--reach-ratio",
  ".03",
  "--reach-safety-factor",
  ".992",
  "--active-band",
  ".025",
  "--marked-diameter-budget",
  "4.2",
  "--witness-lower-budget",
  ".9",
  "--amplitude-height-floor",
  "1.01",
  "--spectral-p",
  "4",
  "--spectral-epsilon",
  ".001",
  "--spectral-scale",
  ".05",
  "--legacy-fraction",
  ".5",
  "--target",
  "1e-9",
  "--scalar-admission-seconds",
  "300",
  "--scalar-integral-tolerance",
  "1e-18",
  "--scalar-tail-cutoff",
  "1/8",
  "--outdir",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/so3-closed-actual-profile-cached-backtracked-SOC-v2-second",
  "--restart-checkpoint",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/so3-closed-actual-profile-cached-backtracked-SOC-v2-first/final.npz",
  "--restart-report",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/so3-closed-actual-profile-cached-backtracked-SOC-v2-first/report.json",
  "--restoration-interior-margin",
  "1e-8",
  "--reference-cache",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/so3-closed-actual-profile-cached-backtracked-SOC-v2-first/frozen-parent-meridian-cache",
  "--reference-cache-report",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/so3-closed-actual-profile-cached-backtracked-SOC-v2-first/report.json",
  "--soc-rounds",
  "8",
  "--soc-tau",
  "0",
  "--soc-inward-fraction",
  ".125",
  "--soc-feasibility-tolerance",
  "2e-11",
  "--manifest",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/so3-closed-actual-profile-first/report.json",
  "--manifest",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/so3-closed-actual-profile-interior-restore-first/report.json",
  "--manifest",
  "/home/runner/work/_temp/visible-larger-research-45904402595-1/research/so3-closed-actual-profile-cached-backtracked-SOC-v2-first/report.json"
]
```

本步未把实际42的完整PCG报告显式加为manifest。实际42科学子进程确有完整成功返回，其独立新位置及完整末场不能因此丢失；下一同目标分支如接续，必须明确合并42与43的实际完整来源，再在新当前父重读相应值。不能用本步 `all_permanent=true` 外推成已经复读本run所有并行分支未知的地址/typed优先次序。

## 8. 第42步未闭合的纯读取与本次终态

第42步已确认的事实仍是：科学child退出0、完整科学report成功；pair因pure child退出1而整体失败。它的科学末场、own baseline变化与完整输入责任保持有效记录。旧pure源码中 `fixed_background_inverse` 实为完整政策dict而被当作scalar检查，是独立静态发现的明确合同错误；**当前仍没有本次原pure异常trace证实它就是实际42首先触发的错误**。

原日志诊断完整源 `28b100b7c0c7c984a1b4ac68e5d0615b12fb8f90a2ca3bcb7d7273ff655e6a78` 与完整修正pure源 `cfd248e7159bb2ff19d6947c4ab4e2f5bc9673e49eac94324cc676c759dad0bf` 已分别随公开提交 `6452508d6135797cf27f15af6df7cc6f0bb17013`、`41822e036487266bed5b372d90c61ab7f2781358` 入队。它们没有中断当时正在执行的43。终态索引没有这两个步骤的实际准入/返回记录，故这里不生成新的异常、纯读摘要、Pg、alpha或SOC记录。

API的实际终态是job及科学step success，而本题没有完成：有限观测最大残差仍约0.0364，完整连续误差与全部t证明责任没有被这些有限数值读数支付；本次亦未获得实际QP驻点/进一步精化结论。下一科学尝试应继续使用明确的新完整机制与来源，不以一次job预算结束收尾，不把未返的原后继任务标完成。

## 9. 复核范围

本note只读取公开53KB紧凑卷、小索引与job metadata，使用现成实际数字和完整argv。没有在本地执行F/J/QP/root、重算科学数值、整读大报告或通过SHA伪造raw。源与参数的详细复现链仍是原完整公开脚本与本run已经返回的依赖链；再次运行同命令不自动保证同二进制场或同永久地址集合。
