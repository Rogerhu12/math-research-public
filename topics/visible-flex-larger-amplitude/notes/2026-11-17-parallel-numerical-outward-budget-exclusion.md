# 固定材料 chord 复读与 R=1.6 新参考背景的实际子午线排除

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。**可信度：参考表与 chord 为数值证据；排除部分引用独立完整证明。** 本条结清前一条近竖直参考设计尚未支付的真实端点约束。没有新的非线性接受场。

## 固定材料标签不能换成到圆的最近距离

[此前参考设计](2026-11-17-parallel-numerical-nearvertical-scalar-budget.md) 使用到目标圆的最近距离，它只给圆上对应可自由选择的较弱必要条件。补充读取原完整 rho112，令

\[
\Theta(\phi)=\phi+\sum_j\rho_j\sin(2j\phi)/(2j),
\]

并用真实 Frenet polar-frame 场转成全局 XY，直接计算固定标签的 `sqrt(|R exp(iTheta)-XYcut|²+(H-zcut)²)`。对原 R1.55 参考设计，N16384 的最坏值仍为 `1.1046441882323192`，最坏 phi=pi/2；但逐点固定标签 chord 可比最近圆距离大 `.02885142628`。这次最坏值相同不意味着两种条件等价。

该补充 raw `parallel-nearvertical0800-fixed-label-chord.json` SHA `7c85b8144965df469a5d0399a88b9956ae65f1b71334b8c4d88417f42742bc38`。新的短源 [cut_budget_check.py](../scripts/parallel_20261117_cut_budget_check.py) 明确读取固定标签和真实 major 切向，以下 R1.6 运行使用它；同源也可复读旧 R1.55 参考报告。

## R1.6 重新设计及其条件数值

真实 .8 cut 的 major 点不是 r_cut：其水平位置为 `x0=1.4309450325961603`，实际 s 切向为 `[.05497384094997361,0,.9984877950302165]`，速度 `1.0000000000065483`，单位竖直切向 `p0=.998487795023678`。因此，正投影 major 子午线在实际曲率不超过6.5时，接水平圆口至少需要半径 `1.58455853952288`；6.8预算下也至少需要 `1.57778147304`。旧 R1.55 没有支付这项实际切向条件。

使用同一已登记的 `nearvertical_background.py`（SHA `dd36b046ae9c15c5df0fc2a0780a7a8091fc32c47ed1f6311c3635c97f3d3118`），改 R=1.6、deep_w=.0001、height_slack=.0015；其余参数不变，生成新的2165行固定 Hermite 表。不能把旧 g 的任何接受转给它。

| 新参考量 | 数值 |
|---|---:|
| 主段参考高度积分 | .6793487061460884 |
| 条件参考圆口高度 H | 1.4411133029695975 |
| 含参考退休段的径向长度 | 1.1083814305187447 |
| N16384 固定材料最大 chord | 1.106766799080882 |
| 采样 chord 余量 | .001614631437862668 |
| 实际 Hermite 表最大采样曲率 | 6.5000025596229145 |
| 条件回头盖直径上界表达式 | 4.797887441939546 |

GL8→12/每实际表胞元的长度差约 `2.2e-16`；这些仍不是连续严格包络。固定标签与最近圆的逐点差可达 `.03005265767`。H 仍是材料高度均值加参考标量高度，不是已解非线性场的末端高度。

## 新的实际 major 上长度门仍将这条强幅设计排除

[R635](../results/R635-positive-projection-meridian-curvature-length-obstruction.md) 证明了包含负竖直坡度的完整包络。其前提是 major 反射子午线保持向外的正水平投影，终点为水平圆口，且实际子午线曲率有界。它限制 **实际 major 长度的上界**，并不是参考 g 的曲率条件。

该独立证明已对同一真实 b677/node330 作整数平方根及有理上 Riemann 和核验，使用更宽的条件框

\[
R\in[1.6-10^{-12},1.6+10^{-12}],\quad H\le1.45,\quad |\kappa|\le6.8.
\]

此框包含上面参考 H=1.4411133。它给 major 长度 `<.757370`，而 minor **仅水平位移**就 `>.831406450447`。所以在这些实际端点、正投影和曲率条件下，任何共同径向 g 的相对误差都必须 `>.092997`，远超过1e-6。证明已经计入近等距因子，并允许包络中有限的负坡度。

因此，新参考 g 虽通过下长度 chord、参考表曲率、条件帽直径及初步 flatten 半径检查，**仍不能在上述真实条件下接到原强父**。这里不把它保留为强幅候选，也不继续向它投入大幅 BVP。该排除不覆盖水平投影翻转的向内 Frenet 路线；条件 H 也不能被冒称已测实际高度。

独立核验报告 `parallel-model-positive-meridian-budget.json` SHA `6eaccee4f12067a51e200f6fdbe7f70835add7313d2e508f3daf119ac7e1681d`。本会话直接引用已有证明与报告，没有重算同一结论。

## 文件身份与复现

```text
parallel-nearvertical0800-r16-background.json
23b8fb09be112c93f2cae255162a1f369c36a653802e90f5493556ea5c7c1017
parallel-nearvertical0800-r16-report.json
267a004ecb18a5c00ec905d9b57ffaedcac75bf882a3cdf283d840b1d5c0f1bd
parallel-nearvertical0800-r16-cut-budget.json
2034ccfff93a78bbe7f1adcb90b3fd75d1965abd98b42647ada77b0d67564812
cut_budget_check.py source SHA256
6d0387fbf37746e174d1cfcb19cba8d2fce0c623950096104c442ca23babc7fd
```

在仓库外 scratch 根目录运行：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_nearvertical_background.py \
 --trace parallel-trace0800-physical-m112.json \
 --material-trace parallel-smooth0800-c6-material-trace.json \
 --cuff-radius 1.6 --deep-w .0001 --height-slack .0015 \
 --background-out parallel-nearvertical0800-r16-background.json \
 --out parallel-nearvertical0800-r16-report.json

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
 math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_cut_budget_check.py \
 --trace parallel-trace0800-physical-m112.json \
 --reference-report parallel-nearvertical0800-r16-report.json \
 --angles 16384 --actual-curvature-limit 6.5 \
 --out parallel-nearvertical0800-r16-cut-budget.json
```

未列出的生成参数全部沿用已登记配方：extension .07、rho .145、cap ramp .001、D预算4.8、生成曲率6.5、角度曲率过渡弧长.0001、peak gap .002、log_step .01、生成报告角点4096。trace 和材料投影文件的固定来源见前条 note。
