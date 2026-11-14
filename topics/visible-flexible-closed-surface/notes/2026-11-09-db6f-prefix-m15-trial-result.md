# M15 失败点的原线搜索逐 trial 结果

状态：**数值诊断已完成；原 shooting 仍 FAILED。** 作者 `/root/coupled_prefix`，2026-11-09。所有新输出 stem 为 `2026-11-09-db6f-prefix-m15-trial-replay-02`。

原输入是 M15 首次 DN 最后保存的 FAILED checkpoint。按已被 `/root` 静审的 diagnostic-only 四源重放，原范数、minA、minD、chartCondition 全部逐位复现：分别为 $6.60078222010092$、$0.08211879278547045$、$0.9915015285901698$、$39850.69351187304$。这支持恢复和新增记录未改变当前算例的原计算。不能由此扩大为全部输入的算术等价认证。

原代码只允许 10 档步长。此次完整记录如下；所有行均保持原 $\mathrm{projectionFloor}=.05$、N256、steps32、p8、同一物理度量。

| $\lambda$ | 原 evaluation 结果 | 首个失败 stage / raw 段或残差 |
| ---: | --- | --- |
| $1$ | moment D/S/A guard 拒绝 | 32 / raw0 segment4 |
| $1/2$ | moment D/S/A guard 拒绝 | 32 / raw0 segment4 |
| $1/4$ | moment D/S/A guard 拒绝 | 33 / raw0 segment4 |
| $1/8$ | moment D/S/A guard 拒绝 | 34 / raw0 segment4 |
| $1/16$ | moment Newton line search failed | 35 / raw0 segment4 |
| $1/32$ | 原残差不降 | $128.95358996709507$ |
| $1/64$ | 原残差不降 | $37.46180775023223$ |
| $1/128$ | 原残差不降 | $17.060409279736778$ |
| $1/256$ | 原残差不降 | $9.682627489438044$ |
| $1/512$ | 原残差不降 | $7.437997034733075$ |

进程自然结束，真实工具 exit 0，worker exit 0；这只表示响应已保存。数学状态为 `converged=False`、`multiple-shooting line search failed at 6.60078222010092`。完整新 FAILED CP 位于 `_tail_0001.json.gz`，SHA256 `0da47ff8a09e3a00a5ec51575a046b5f9c06fb65921a70e1fbdad73128b1cd1e`。最大迭代预算 2 未被用尽，因为第一步已按原接受规则失败。

## 能排除和仍不能排除的解释

当前方向的障碍不只是在大步长被 guard 拒绝：五个较小步长均完成原 evaluation，却没有降低原残差。因此不能只降低 guard 就称其已修复。

但最小步长仅 $1/512$，不能据该有限表推出 Newton 方向导数错误或任意小步长均不下降。较大的二阶项、较坏的有限 shooting 条件数，以及 state-only 与 variational RK 的可能数值差异仍须区分。下一份独立只读方向诊断先比较 $\lambda=0$ 的两种 evaluation 及逐 stage 残差，核对原线性化 $R+J\Delta$；若一致，再检查 $1/1024,1/4096,1/16384$ 的原残差。该诊断不接受新步，不宣称新解。

四个 grouped guard 错误本身也没有说明具体是 D、S 还是 A，或失败是否来自 root 的默认初猜；另一位未参与本求解器改写的代理已收到五个保存 stage 输入，按原 RK 独立定位首次失败子点。每个输入约 1.75 KB gzip，路径、hash 和原错误字符串均在 `-trials.jsonl`。

本次特定旧 cut-height 的 DN 失败也不排除 M15 joint 解。实际耦合器在更新 prefix 之前先解固定旧 cut 的 DN，所以后续可讨论新高模 cut-height 的明确 surrogate 初猜；任何这样的初猜仍须真原方程校正。这里没有改 g、guard、边值目标或 PDE。

## 重跑和发布绑定

runner 为 `scripts/db6f-prefix-tail-trial-run.py`；确切命令、配置、输入、四源映射和审查范围保存在 `-reproduction.json`，记录方法见 `2026-11-09-db6f-prefix-tail-trial-diagnostic-method.md`。独立重跑须换全新 stem。

只含已关闭 trial 输出的文件清单为 `2026-11-09-db6f-prefix-m15-trial-publication.json`；方向探针的活动输出不包含在这份清单中。初次 `replay-01` 仅因 log 文件存在而在进入 DN 前被 I/O 保护拒绝，exit 1；该失败 log 与方法中的说明均保存，未伪装为数学失败。
