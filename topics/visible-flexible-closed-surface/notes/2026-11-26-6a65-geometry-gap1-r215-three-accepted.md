# gap 1 / 外段 .05 / R215：三次真正接受的完整 LM

2026-11-26，Astra-visible-flex-6a65 / geometry_mechanism。**3 次 full normal、5 次实际非线性 trial、3 次接受；三个独立 Node 进程均自然退出 0。**

本次接着 [首次新设计基线](2026-11-26-6a65-geometry-gap1-r215-first-value.md)，保持新 gap $1$、外段增加 $.05$、R215 完整帽引导以及四次 metric $\tau=.05$。每一步重新形成本目标的完整 normal，未借旧 R204 normal；每次只做一个 LM 搜索，保存后退出，下一进程从实际接受态继续。

## 实际结果

| 接受态 | 总平方目标 | 最大相对 metric | 最大曲率样本 | 最大 $|y|$ | 最小 held 距离样本 | $A$ | $Z$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 新基线 | $4.2570051061$ | $.7291817664$ | $24.52988202$ | $.9001692319$ | $.5935941364$ | $.5213620655$ | $.5381046561$ |
| 1 | $2.6852827616$ | $.6383193972$ | $22.81535189$ | $.8903522801$ | $.5950431996$ | $.5841319222$ | $.5361803628$ |
| 2 | $.9792052983$ | $.7033176662$ | $22.14062763$ | $.8421443383$ | $.6189958651$ | $.8147560220$ | $.5307500652$ |
| 3 | $.2427674894$ | $.7389708287$ | $17.01381050$ | $.8349021547$ | $.6251744630$ | $.8454837980$ | $.5384471976$ |

第 1 步实际 full trial 和 half trial 分别返回目标 $90.3973761796$ 与 $4.9475068798$，均拒绝；quarter trial 真正接受。第 2、3 步均在 first full trial 接受。实际 normal 时间分别 $22.701$、$25.936$、$20.018$ 秒，进程外观测墙时分别 $52.6256$、$31.9012$、$26.7271$ 秒。整个串行子进程组观测的最大 RSS 为 $321804$ KiB。

第 3 态的有限球半径最大值为 $1.4406293661$；扣除 R215 高度允许量后，最大 excess 为 $-.0102233922$。当前有限板宽已经落入引导 $.885$，但 held 尚未达到最终 $.64$，曲率仍高于 $1/.097$，metric 远高于 $10^{-6}$。因此这些步骤没有完成真实闭核或强目标。

## 峰值没有因总目标下降而自动改善

| 接受态 | 完整二次 metric 平方项 | 额外四次 metric 平方项 | metric 最坏点 | 该点 $r_E$ | 该点 $r_F$ |
| --- | --- | --- | --- | --- | --- |
| 1 | $.0496950478$ | $2.3787686637$ | $(.5598236915,\pi)$ | $.6383191448$ | $-.0004013765$ |
| 2 | $.0207958047$ | $.6876394596$ | $(.2030282569,\pi)$ | $.7033176385$ | $-.0001393892$ |
| 3 | $.0105954835$ | $.1972645612$ | $(.2346108715,0)$ | $.7389558259$ | $.0033296649$ |

完整积分项明显下降，但最大 metric 从第 1 步后又升高，并移到前段长轴；主要是 $E$ 方向超速。不能据总目标下降宣称 uniform metric 改善，更不能拿新增观察点代替同一准确 g 的真正求解加密。

第 3 态 held 最坏点为 $s=.7073686136,u=\pi/2$，实际坐标约 $(.000126899,.831987494,.161191405)$，说明当前剩余排球缺陷仍来自真实外前缀。尾和新帽的完整条件预算没有替这个点支付距离。

## 源码与进程身份

入口：[6a65-geometry-run-gap-length.cjs](../scripts/6a65-geometry-run-gap-length.cjs)。它消费 [新设计完整工厂](../scripts/6a65-geometry-gap-length-value.cjs) 的 provider，包含 R211 四次 curvature、恢复版四次 metric 及 R215 全参数几何行。每次使用原完整 R206 Schur 核和 R195 LM，halfBandwidthBlocks 为 4，最多 8 个 damping attempts，实际试用步长为 $1,1/2,1/4$。

单步命令形式：

```sh
node --expose-gc --max-old-space-size=128 \
 topics/visible-flexible-closed-surface/scripts/6a65-geometry-run-gap-length.cjs \
 topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json \
 PARENT_STATE_JSON FRESH_PREFIX
```

首次 PARENT_STATE_JSON 为 gap1-delta005-R215-value01-seed.json，后两次依序读取上一真实接受态。输出写在 /tmp/visible-flex-6a65e705/geometry-work；外层 Python supervisor 保存独立的自然退出回执，没有由运行中的 Node 自填 OS 退出成功。

| 真正输出文件尾名 | SHA-256 |
| --- | --- |
| gap1-delta005-R215-lm01-state.json | 4041c7ad0bed5a48910da1a70ebe2f5957e6820124fed60079ab2762645bdff1 |
| gap1-delta005-R215-lm02-state.json | 74b24bff48adc938cb467adf03becca029283a16065267f8498b908ab64630d0 |
| gap1-delta005-R215-lm03-state.json | 90f335c1605f4ef54115561d74ba5246d3f150ff92929034d903d70d1f164e11 |

三个对应的 lm01-exit.json、lm02-exit.json、lm03-exit.json 均记录 returncode 0。以上 raw 状态和退出回执可由脚本重算，只保存在 scratch，不进入 Git 或 Actions artifacts。完整参数向量、准确 fixed-g 冻结、连续 metric/曲率余项和核心非局部 reach 的工作仍未完成。
