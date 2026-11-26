# 原 M12 中央 ramp：同一 g 的三档实际 C2 位置加密

2026-11-26，Astra-visible-flex-6a65e705/g5_and_exact。
本记录只覆盖原物理 $0\le\sigma\le T_u\epsilon$ 的第一个 $K\le0$ ramp。
没有闭图、全域连续误差证书、正曲率段稳定性或 README 第 5 条完成结论。

## 1. 固定对象与真正的有限位置图

源码为 `../scripts/6a65-m12-central-ramp-hermite-flow.py`，SHA256
`532b6ffbf256f085229ab56febc02601f99a6678c047daf3630fdd29881f846a`。
它复用 R116 的同一 Gauss–Codazzi 方程和
`fd2d-gc-ellipse-hybrid-flow.py` 的“只截断 n,m、位置和标架逐角推进”表示，
但入口换成原 M12 保存的准确有理中央截面，按其精确弧长积分归一到固定 $f(0)=1$。
原 M12 $g$、物理参数、三个多项式 ramp 区间和终点均不改变。

目标的原 ramp 法则准确为 $f=1+vR P(\sigma/R)$、
$f'=vF(\sigma/R)$、$f''=vF'(\sigma/R)/R$，
其中 $R=T_u\epsilon$、$\eta=.05$，$F,P$ 是原已登记的 flat-acceleration 分段多项式。
入口与几何数值积分使用固定中央 chart
$du/d\theta=|\gamma'_0(\theta)|/a_{\gamma_0}$。
同一个 $a_{\gamma_0}$ 的定义是精确积分，三档都以同一 512×32 求积评价；
本数值记录没有给该求积的严格余项，不把其浮点数重新定义为另一个 $g$。

DOP853 的状态及 RHS 只产生有限图的节点输入。程序随后：

1. 将位置、所选一阶和二阶径向 jet 变为准确 C3/反射模约束的 Cartesian Fourier 系数，并存成明确 binary64 数；
2. 在准确有理物理网格上作共享零至二阶端 jet 的五次 Hermite 插值；
3. 在每个真实径向单元的内部 Gauss 点，直接微分这张位置图，再算完整 $E,F,G$ 和主曲率。

因此实际有限图的度量观察没有用辅助标架正交性或 ODE RHS 代替位置导数。
中央节点的位置高度准确为零，第一径向 jet 准确置为 $e_z$，第二 jet 准确置为零；
所以每档的中央反射接合在有限函数定义中都是 $C^2$。
内部径向接合因共享两 jet 也是 $C^2$；角向使用同一个完整周期 Fourier 表示。

## 2. 三档实际结果

| 最大 shape Fourier 频率 | 径向步长上限 | 实际 Hermite 单元 | 独立观察角节点 | 每单元 Gauss | 实际图 metric 采样峰值 |
|---:|---:|---:|---:|---:|---:|
| 95 | .002 | 145 | 768 | 6 | 2.1443590268118953e-10 |
| 191 | .001 | 287 | 1536 | 8 | 4.314835056092037e-12 |
| 383 | .0005 | 571 | 3072 | 8 | 3.6668767176161476e-12 |

相应采样能量为 $1.27726448171149\cdot10^{-21}$、
$4.4872911524794114\cdot10^{-26}$、$3.3361029459961353\cdot10^{-26}$。
三档实际曲率采样峰值均约 $5.11272468$。
最细级使用更小 ODE 容差；它的 RHS 观察误差反而约 $7.17\cdot10^{-12}$，
实际 Hermite 图峰值为上表值，两个量没有混记。

这给首个固定物理子域的一条真实数值改善链。两档细级已接近此 binary64
位置重构的精度量级；没有据此证明无限维收敛，也没有把子域表格当作整个闭族的第 5 条证据。
特别是后续正曲率 ramp、down 段、bridge 和真正平直截口尚未接通。

## 3. 实际命令与身份

以下从仓库根运行；M12 原数据的恢复方法与 SHA 见 R220。
输出路径必须为新路径，全部数组和扫描 JSON 留在 scratch。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-central-ramp-hermite-flow.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-central-ramp-M95-h002-dd20.json \
  --modes 95 --step .002 --gauss 6 --observation-multiple 2

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-central-ramp-hermite-flow.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-central-ramp-M191-h001.json \
  --modes 191 --step .001 --gauss 8 --observation-multiple 2

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-central-ramp-hermite-flow.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --out /tmp/visible-flex-6a65e705/exact-work/m12-central-ramp-M383-h0005.json \
  --modes 383 --step .0005 --gauss 8 --observation-multiple 2 --rtol 2.4e-14 --atol 3e-16
```

三次均实际 exit 0。现用 M95 receipt 是修正 adapter 身份后的真实复跑，
其生成场 hash 与初次 M95 运行相同，因为该更正只触及本流程不用的旧图径向二阶观察器。

| 输入级别 | 实际耗时（秒） | 生成场 `.field.npz` SHA256 |
|---|---:|---|
| M95 | 2.8718580510030733 | `847e0a0faaaffacd64aed650eeff86c72a37d6945b861f904f479a98a8de7602` |
| M191 | 11.30786345800152 | `ed4b7391d4d3c1b52ee13c49182577c225f2702d29c87ad9af47804b6b2df651` |
| M383 | 36.77745874300308 | `73dbff55c9b2d52704d7d3fe22d8ca0c46193460980130329f4498bf23423b04` |

M191/M383 报告 SHA256 分别为
`9b3a7415f229435999b9b2b1395c363b35b9e0458223e1c321223e5760e853ff`、
`2150e655504482a655c3d2aefbecf41b7d5dc17d7c295558bd5704d6dd11d4be`。
M95 当前 receipt 的 SHA256 为
`4048e102eff2bbcc608b199316ac7fb41ca56f631abb1305686cca373c7a04d9`。

下一消费者是 `6a65-m12-ramp-exact-coast-c2-glue.py`：将本真实有限图的出口曲线
作为新 R137 输入，按原 $f(R)$ 准确归一，并在最后一段 ramp 用完整三端迹校正
实现真正的 $C^2$ 位置拼接。该拼接的误差和新曲线连续域独立记录。
