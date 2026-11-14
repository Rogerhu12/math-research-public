# M15 原 Newton 方向的只读残差检查

状态：**有限精度诊断完成，全部探针真实 exit 0；没有接受新迭代，也没有得到 M15 联解。** 作者 `/root/coupled_prefix`，2026-11-09。

输入是已冻结的 M15 FAILED CP：`2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from14_tail_0001.json.gz`。使用同一 g、原 guard .05、原 M15/N256/p8/steps32。source-map 记录的两个派生模块只将原 `correction`、`scaleFor` 函数公开给探针，以及调整模块 import；没有改动其公式或原 evaluation。

## 1. 两条 RK 计算路径逐段相同

`db6f-prefix-tail-direction-probe.mjs` 复用原 warm-remesh 和同目标的 boundary correction，分别计算原 `evaluate(...,false)` 与 `evaluate(...,true)`。前者是原线搜索 state-only 路径，后者是原 Newton 的 variational 路径。

这次 864 个 stage 的全部归一 residual **逐位相同**，最大差为 0；两者原范数都是 $f_0=6.60078222010092$。最坏 stage 38、raw0 segment4。该结果排除本态两条 RK 路径不一致作为线搜索失败的解释，不扩张为所有输入的算术等价定理。

由原 `correction` 求得的同一方向 $\Delta$，逐段核验

$$
R_n+J_n\Delta_{n+1}-\Delta_n
$$

以及原远端 Robin 和固定 cut-height 线性条件，最大原归一残差为 $1.6077530736360947\cdot10^{-9}$，约为 $f_0$ 的 $2.44\cdot10^{-10}$。原 graph chart 条件数诊断为 $39850.69351187304$。这说明该有限线性系统被解得很准；它本身不是一个关于解析 Jacobian 的新证明，也不能保证有限大步降低非线性残差。

原方向逐字节保存为 `2026-11-09-db6f-prefix-m15-direction-base-direction.json.gz`，显式标明 UNSOLVED，并绑定输入 CP/config。后续只读 trial 复用该保存方向，未重新改算另一个方向。

## 2. 原十档之外确有下降，但极弱

原线搜索只试到 $1/512$，该点范数仍为 $7.437997034733075$。新独立探针只评价相同方向的四个更小步长，原 equation 和 guard 均不变：

| $\lambda$ | 原全域 shooting 范数 $f(\lambda)$ | 相对 $f_0$ |
| ---: | ---: | --- |
| $1/1024$ | $6.817074102267003$ | 上升 |
| $1/4096$ | $6.613603724904844$ | 上升 |
| $1/16384$ | $6.601289700732764$ | 上升 |
| $1/65536$ | $6.6007385285192015$ | 下降 $4.36915817185\cdot10^{-5}$ |

四个 trial 全部完成原 evaluation，最坏均在 stage38/segment4。最后下降仅约 $6.62\cdot10^{-6}$ 的相对量，距原 $2\cdot10^{-9}$ 求解容差仍很远。该点如果被原接受判据试到，满足其严格范数下降要求；本探针没有把它送回 worker 接受，也没有把它标为收敛解。

前三个点的指示量

$$
C(\lambda)=\frac{f(\lambda)-f_0(1-\lambda)}{\lambda^2}
$$

分别约为 $233558,242146,244373$，与很大的非线性二阶项相容。这里 $f$ 是最大范数，没有把该观察提升为可微性或二阶误差严格界。它与精确复现的双 RK、低线性残差、实际微小下降一起，排除了“当前方向没有任何可行下降”的强断言。

## 3. 下一步的范围

原十档 backtrack 确实未到达此下降区间，但单纯增加回溯只能据此恢复极强阻尼的一小步；不继续盲目沿这一路径跑很多轮。独立 stage 重放同时显示：大 trial 的默认初猜触 A guard；可行 A=1 seed 也未解掉相同 target，较低正 floor 的有限测试仍未找到 root。后者不证明无根，但不支持只改初猜或降 guard 就已解决当前问题。

主会话因此选择同一 g 的自由高模 cut-height 仿射 prefix 初猜：旧完整 M14/N512 真低模 DN/J 加新模线性 port，仅作 UNSOLVED warm，之后回原 M15 真 DN/BC 校正。该路径与当前数据同时保留，不修改上述失败或诊断文件。

## 4. 复算接口与绑定

脚本 `scripts/db6f-prefix-tail-direction-probe.mjs` 必需参数为 `--source-root`、`--config`、`--checkpoint`、`--out`，均指本题冻结源、上述原 M15 config/FAILED CP 和新输出路径。不传 `--direction` 时计算双路径基点、原方向及线性残差；之后可传生成的 `--direction ...-direction.json.gz` 和逗号分隔的 `--lambdas`。

实际分三次执行：base 不带 lambdas；第二次 `--lambdas 0.0009765625,0.000244140625,0.00006103515625`；第三次 `--lambdas 0.0000152587890625`。Node 使用 `NODE_OPTIONS=--max-old-space-size=1536`。三个数据/日志 stem 分别为 `prefix-m15-direction-base`、`prefix-m15-direction-small-trials`、`prefix-m15-direction-tiny-trial`，均带本日 `2026-11-09-db6f-` 前缀。

每份 JSON 记录输入 hash、脚本 hash 和 source-map hash，逐段数值留在磁盘。发布清单 `2026-11-09-db6f-prefix-m15-direction-publication.json` 只含已关闭文件，不含后续自由 cut 预测的活动输出。
