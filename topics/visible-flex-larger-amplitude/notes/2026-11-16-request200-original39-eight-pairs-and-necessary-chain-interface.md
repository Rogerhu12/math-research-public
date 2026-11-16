# Request200：从真实 actual98 重做完整 39-query 八对链及必要读回

作者：AI（ChatGPT，exact_refinement）；日期：2026-11-16。

## 1. 目的与实际基线

actual191（run43766271165/source7891ee252147194137c2a933b6407a7c2c0ac19f）已完成八个真实原进展 pair 及其 fresh FD，但两个整链必要对象分别 210886 B、215693 B，超过原 90000 B；未输出正文，返回传输码70。完整证据及未读范围见 [R404](../results/R404-actual191-eight-real39-pairs-and-necessary-summary-overflow.md)。本次不会从 SHA 恢复末 pair、沿用未读 merit/alpha 或把重算标成 actual191 继续。

本次明确从同一个实际可恢复的 actual98 原 warm/status 重新生成一条完整39轨迹。原 39 个 query、全部数学源、真实试步/门、FD 和资源预算不变；只改 necessary reader、worker 身份与记录三个原参数的小附记。数学与读回责任见 [R428](../results/R428-complete39-necessary-chain-readout-and-original-science-contract.md)，14476 B / `16616ba70a4ee0ec535d90d857136c74f1e276c48fee9888c73fa4babfb81ca9`。

当前只有完整源码/配方/工作流，没有未来 run/job/输出 SHA。实际 source commit、run/job 和科学结果必须由发布后的官方事实填写；本接口不预报八对一定完成或摘要一定小于90KB。

## 2. 五件运行文件与来源闭包

| 目标路径 | bytes | SHA256 |
|---|---:|---|
| computations/root_20261115_thirty_nine_necessary_chain_readout.py | 62855 | `abf42d92c980566e20a4c8a7fbd90976669240bf8cc8bed06d3b6e1705fa79b8` |
| computations/geometry_20261115_thirty_nine_necessary_batches.py | 29611 | `68d53286565c892cdcebd131fb73c2c32b25d6ff865a6da706bec03dbfdbe8e5` |
| computations/public-thirty-nine-necessary-model-recipe.json | 31236 | `2b9c71c067dfb8a7ff9fcd7111e4eff884a68e197504c38e14b128b6ecb8692f` |
| computations/public-thirty-nine-necessary-batch-request.json | 13428 | `305088672e8eeccb46e48931b87f5a55b9ed41ccc9b8f19d958b71711b7e1ad9` |
| .github/workflows/visible-larger-public-thirty-nine-necessary-batches.yml | 13285 | `0de9e7174a2f291481583c91f76f8f43c9aa951e2515617358d8b6e9af8d4536` |

表中 computations 均相对 `topics/visible-flex-larger-amplitude/`，workflow 相对仓库根。

当前新配方保 actual191 的原 103 个 source pins，并加原191 worker的 `9631f34c...` 作为明确来源，得到104个原身份；新增 `root_20261115_thirty_nine_necessary_chain_readout.py` 得到配方105项，独立新 worker 再占一项，共106。所有旧104哈希逐项保留，无删项、无旧科学源字节替换；原一件参数 manifest 不变。

原五件数学源继续是 domain `0dc60f8a...`、warm `568d1f22...`、FD `fc92e7d9...`、observer `59fa547d...`、noncontiguous condensation `b7a5f7e6...`。原 full model 及其递归恢复代码仍从真实历史源 `918fdb11dbb7a424b6149b405e2c7fab3cc0c737` 读取。旧191 reader/worker只作已发生实验与实现基线，不执行旧编排。

源树的现有正常校验保留：Actions 核 source、参数、原 recipe、README 原字节，并解析所有 Python 源；这里未另加数学对拍、fixture 或数值预检。组装过程中只做文本/JSON/字节身份工作，未本地 import、AST、编译或任何科学计算。

## 3. 真正输入与完全相同的科学问题

唯一首父：

- actual98 run `43677587785`，artifact `14147700690`，原source `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`；
- ZIP 809042943 B / `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`；
- 原 warm 4927052 B / `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`；
- 原 status 3379453 B / `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`。

原 `51224788...` transport完整核 ZIP size/SHA、中央目录及所取两个真实成员后，只解必要 warm/status；不从摘要伪造输入。四件数学输入仍为原 accepted/prepared/tail-anchor/tail-config，按原 `918f...` 路径和完整 SHA 恢复。原 tail-anchor `e788a28d...` 仍明确是原零H线性输入，不能称已经做了新非零 native H。

全部39 query与actual191字面一致：22 LEFT、16 MID，加原 RIGHT-RMS459 fraction `0.8273268353539885`；所有2048角，79872 selected角行，26个 capture interval。真实B支撑为459、460及462至491，共32节点/10819 local坐标；free461仍完整存在，由原R407全仿射hole QR消去并恢复，不填零B。原C4059和完整H/outside作用保留。

workflow把新recipe与actual191原recipe逐字段核同：query specs、全部实际端点、gap condensation、数学entry、domain/FD入口、参数manifest、原model flags及真实父身份。它不把这些来源检查变为新的科学接受阈值。

## 4. 原命令、预算与真正批次状态

原 model flags 逐项不变：

```text
--iterations 1 --damping 270 --lsmr-iterations 200
--projection-sweeps 200 --line-search-steps 17
--budget-seconds 1200 --angles 4096 --jac-workers 2
--condensed-budget-seconds 600
--condensed-trial-reserve-seconds 90
--condensed-recovery-reserve-seconds 30
--condensed-max-working 512 --condensed-dual-sweeps 200
--condensed-store-root
```

每批仍先完整原 model，再在其新 warm 上做原全部 fresh FD。只有原 status 真有一步进展、完整 warm/status来源匹配，且 FD 原 `implementation_check_passed`、新preparedSHA、`complete_current_warm_boundary_FD_actually_recomputed` 都成立，才晋级下一父。所有原实际试步、域与merit、线性reserve和FD阈值均原样。

最多8对；between-batches10500s从初次输入/源恢复完成后开始。175min科学step覆盖恢复与每个原child，195min job包含安装和必要读回/清理，always读回最多10min。原单child预算不被“剩余批次数”重写。没有保证八对在一次job一定完成；中断/资源状态和未访范围按实际输出。

worker主CLI：

```text
python -u <comp>/geometry_20261115_thirty_nine_necessary_batches.py
  --repo-root <fixed checkout>
  --request <comp>/public-thirty-nine-necessary-batch-request.json
```

workflow通过原 `root_20261114_current576_rules_runner.py` 调用它。原2700秒真实pull/rebase、README比较/实际变化停止不改；BASELINES仅赋当次已读的根 `21bd547f56590b7f2dd279d0297efb289a9b2783` 与课题 `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。科学checkout固定，不跟规则同步切科学源。真实 NFF 与规则变更由原runner处理，未假称任何未来pull已经发生。

独立trigger是新request文件，concurrency group为 `visible-larger-thirty-nine-necessary-pair-batches`，`cancel-in-progress=false`。它不取消或修改191、195、197等已有run。原权限 `contents:write`（规则H同步）与 `actions:read`（actual98原件运输）保留；token仅在现有process环境，传给科学child前去除，owner记录不读argv/environment/token。

## 5. 必要读回：保值而减少重复

新schema为 `request200-one-necessary-whole-chain-readback-v1`。共同来源/输入/查询定义只放一次；八个批次保真实status、输入/输出pair、门、停止、所有已返回trial、原文件身份、FD必要顶层/分组结论。原QP只保实际选择、完整模型门/后验范围、helper错误和预算状态，不重复整个选择历史/condensation树。

所有实际trial的必要浅标量原值保留；所有原返回的selected-query、RMS、midpoint失败地址保留，不只保最近或最坏。原RMS producer每fraction自身最多给前24个invalid样本，本reader不再次截取；原总invalid_count与样本范围分责。缺失trial或未提交状态不被标作已评/通过，也不自动冒“从未执行”。 两个域记录的复用只指已选择的必要 JSON 逐字段相等；不宣称未输出的两个原完整 report 或原文件字节相同。

worker直接从已消费的真实warm选择原 `complete_scalar_profile.frozen_design_parameters` 和 `optimization_warm.actual_global_scalar_parameters` 两份三项记录，附原profile/height身份；不导出状态、高度或矩阵数组，不新求profile，也不制造可续接场。形状/原字段缺失如实标未完整，未转换为新的数值门。

原FD所有科学层照跑；必要摘要保原顶层误差/阈值与直接/分离两组门、方向与层数，以及每个原 contracts is False 收缩项的 group/direction/两原索引和完整原记录；成功数值历史只身份，不重算收缩门。所有 returned midpoint point 的 angular_observer_exception/observer_export_exception 独立收取，不限 bad-index；原 report.collocation_weight_observer_error 亦保必要标量和完整原异常串，traceback/entry仅身份。compact_domain 透传这些字段。原trial表是有限人可读标量表，不是大树字典编码。

单份输出仍按ASCII JSON加一个LF算 bytes/SHA，上限90000。正常marker：

```text
BEGIN_REQUEST200_WHOLE_CHAIN_NECESSARY_SUMMARY
END_REQUEST200_WHOLE_CHAIN_NECESSARY_SUMMARY
```

always若有实际残留，用 `WHOLE_CHAIN_RECOVERY` 对应marker。读者不拆一个大科学对象为多个输出；任何必要内容仍超限，就只记真实字节身份、`summary_complete=false`、传输70并保未读暂存。摘要容量成功不是科学接受条件，本接口不预填未来长度。

## 6. 生命周期与异常边界

原owner/session方案完整保留，只有请求与文件身份切到200：

1. 在恢复或首科学调用前记录本次pid/pgid/sid/start_ticks/boot_id及run/source/request/worker/helper。
2. 原model/FD继承同一个session；每child真实身份记录，逐一wait/reap。
3. 每批完整必要小记录先写、flush/fsync、原字节核回，再移动真实pair并退休该批大raw；不把reader对象当数学输入。
4. 正常整链先打印完整≤90KB必要摘要再删自身work目录。
5. always先按原身份确认own组静止；只有明确本组的活进程可按原TERM15s/KILL5s规则处理。未知/PID复用/未证静止时partial70，既不读也不删活动数据。
6. workflow最终只有necessary、rules实际读回success且新静止核查成功，才删对应 `visible-thirty-nine-200-*`；否则明确skip，保残留直到临时runner销毁。

always CLI：

```text
python -u <comp>/root_20261115_thirty_nine_necessary_chain_readout.py
  --readback-only --temporary-root <RUNNER_TEMP> --code-directory <comp>
```

原stderr读回、失败stdout必要末片范围、规则结果缺失等继续如实记录。原raw/矩阵/每层FD历史均只Actions临时；不用artifact、Release、Git数据、base64或语义分包保存。原原件可再生，不能把末SHA当外部checkpoint。

## 7. 完整差异与交付状态

与actual191的完整临时源差异：

| 差异 | bytes | SHA256 |
|---|---:|---|
| 两核心源 | 48448 | `1667d64525c185b6f8a95533b1c284cc9b6af205f1ce0bbb9ec7047bc1bdce71` |
| recipe | 5839 | `e3ac01f813fc938ba36cf7cdd8bf6d6946fb34b143360138c6eb98b33f0a376c` |
| request | 6403 | `095a4b557b42741d1d347f1874ad97e91241768d7765f63087e54957fc7ae3b6` |
| workflow | 13723 | `d76afc29fecf2da1219c962dcb4f8129cba2f61ed4c85ed2f598a988b71b683f` |

这些差异和纯文本身份回执可从公开源码再生，不属于需要永久保存的大数据。已在本地做的只有完整源码阅读、字符串修订和SHA/JSON字段身份检查；未做本地AST/编译/科学/fixture。原104pin、三参数来源、query/spec/gap/完整模型flags逐项文本核同。reader/worker/report的200guard与独立namespace一致。

本次是具体公开Actions入口，不是额外批准门。发布后若真实八对及读回完成，再按原字段回答接受幅度、最近拒绝位置、merit和后继；若partial或失败，也按相同必要范围记录。即使所有进展与FD通过，`success`、`new_coupled_finite_acceptance`和完整native/fullDN/finalaudit责任仍原样，不能借传输成功替代。
