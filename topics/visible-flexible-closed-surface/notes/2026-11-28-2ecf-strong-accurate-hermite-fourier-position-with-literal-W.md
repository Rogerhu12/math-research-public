# H65 准确双端的 64 元 Hermite–Fourier 实际位置和冻结目标

固定 G10/G11 的设计 3 第三次冻结度量位置，完整父态、端口、三套采样取自 [H65 冻结目标与四次实际位置步](2026-11-28-2ecf-h65-frozen-design-three-sextic-four-actual-steps.md) 和 [原 36 维目标设计](2026-11-28-2ecf-h65-two-space-six-actual-metric-designs.md)。保持原 $s$、原 literal $b,S$，准确前缀与尾片按 [R261](../results/R261-strong-same-metric-physical-refinement-and-complete-prefix-reach.md)、[R265](../results/R265-accurate-weighted-polar-connector-global-embedding.md) 接合。冻结目标 $a_*(s)=a_0(s)\exp(\sum_{j=1}^{36}\alpha_j B_j(s))$ 的身份为 `52902e395f030eb515a7906e7c35993d05525f7bdbafd24137cf2d676818b55f`，36 个准确二进数、其原 clamped quintic 物理 knot 和独立 $a_0$ 均保持。

在原连接器区间 $[b,S]$，取最接近均匀划分 65 个边界的原 G10 径向节点（192 角组）。对每个内部节点，分别取原位置 $P,P_s,P_{ss}$ 的完整角离散 Fourier 变换，复系数按其存储二进数解释。由它们**定义一个新的实际位置**，与隐式极坐标源的误差须另算。左右边界不取这个 Fourier 代理，改用 R265 的准确 Γ95 coast 和准确 R205 cut 的全角 $P,V,A$。每元用三种左右位置端迹作物理径向 quintic Hermite，因此相邻元及两端均按全部六个 jets 准确 $C^2$ 接合。

在选定的 64×80 模型，以上只展开原 polar 底场。把父态完整 6615 个准确二进数 $W$ 在其自己的 45 行 quintic 径向基底、147 个 Cartesian Fourier 通道上直接加回。$W$ 在两端的全二阶零迹保持。角系数存为 $\Re\sum_{k=0}^{80}c_{ijk}e^{iku}$；任意阶角导数乘 $(ik)^j$。元内可读文件的 `weights(t,h,j)` 沿原 $s$ 微分。NPZ 内含完整 `knots,coefficients,endpointProxy,physicalW,Wknots,alpha,alphaKnots`；`endpointProxy` 用于将来误差估计，准确求值须覆盖两端为 R265 端迹。仅有限观察用 `numerical_endpoint_pair` 的原生高阶端口求值；未作原缓存逐字等于真端口之声明。

| 场及有限观察组 | 最大相对度量误差 | 最大自身曲率 | 最小面积比 |
|---|---:|---:|---:|
| 原冻结态 G11，668×256 移位 | .143465314 | 28.806499 | .937611127 |
| 将底场和 W 一起插值的 64×72，G11 | .146711893 | 28.976111 | .937612430 |
| 原 6615 W 独立保留，64×80，G10 958×128 | .140241818 | 28.889381 | .939004489 |
| 同一新场，G10 958×192 | .140241818 | 28.889381 | .937407133 |
| 同一新场，G11 668×256 移位 | .143431819 | 28.815158 | .937611517 |

两条生产观察入口分别自然退出 0（15.735 与 8.262 秒）。64×72 的 G11 误差比原父态高，故后继优先使用保留原完整 $W$ 的 64×80 实际场。它的独立峰轻微下降，整场自身曲率仍远高于强边界；本条新增优化尝试和接受均为 0。三组是同一新位置的完整有限观察，连续度量、全域嵌入、reach 和全闭强指标另算。该显式场也已交给逐环真弧长归一化的固定 $g$ 后继试算。

## 再生

先按前引 H65 物理源、冻结设计 3 和第三次固定 $g$ 位置步的命令生成两个 prepared/observer、两个设计态和 Γ95 两个 master。`S` 指公开 scripts，`W` 指该组数据目录，`OUT` 是新目录。新原场和观察不改变这些输入。

```bash
set -eu
mkdir -p "$OUT"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
args=(--scripts "$S" --prepared "$W/polar-physical-H65-prepared.json"
  --state "$W/polar-H65-frozen-design3-sextic-step03-step01-state.json"
  --frozen "$W/polar-H65-two-space-design-step03-step01-state.json"
  --independent "$W/polar-physical-H65-independent.json"
  --ramp "$W/gap105-prefix-ramp-master.npz" --coast "$W/gap105-prefix-coast-master.npz")
python "$S/2ecf-strong-port-hermite-fourier-position.py" "${args[@]}" \
  --cells 64 --modes 72 --output "$OUT/strong-physical-hf64m72.json"
python "$S/2ecf-strong-port-hermite-fourier-background-physical-W.py" "${args[@]}" \
  --cells 64 --modes 80 --output "$OUT/strong-physical-hf64m80-W.json"
```

| 对象 | 本次 SHA-256 |
|---|---|
| 2ecf-strong-port-hermite-fourier-position.py | `ab700905375904e572e2834ab49df58e66faa20e392e850c2040006699c95748` |
| 2ecf-strong-port-hermite-fourier-background-physical-W.py | `86b1f1574b10db01db45a636e40ba090f11510b0d270146d9da63829e58ffa07` |
| strong-physical-hf64m72.json | `6c2123e0bb947a367d3d24aaa053a61c8713af3531411c5be8d37376e6373196` |
| strong-physical-hf64m72.json.field.npz | `57c370e9294cfc721bbd2eb6add27219a2cbc290d3dacac1987999cbf5012ca0` |
| strong-physical-hf64m80-W.json | `6e9dc0acf08851725780e6b6998c7897750a3966cb39d100934d3fb3a5a8c036` |
| strong-physical-hf64m80-W.json.field.npz | `eaa0835dc7ea5207f2a93cb0ba9b1d1634f2e00c5cb8964fe954b47601990d86` |

运行时间所在的报告可随机器改变。两次均以同一父位置 `a92d4fe576c791a86841c3f4508c6ae51e7181798ad507411145558f5cde8e6e` 和设计态 `b3f45552b07e8d9587c4ec05ea02fb749c3ed63beddda11f222c90bfc7b35c11` 为输入。
