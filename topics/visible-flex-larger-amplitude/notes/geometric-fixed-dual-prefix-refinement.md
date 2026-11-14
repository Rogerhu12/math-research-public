# 二控制候选的真正固定度量前缀加密

2026-11-10，geometric_amplification。**状态：数值证据；仍是带边、线性 tail-DN 前缀。**

本记录冻结 `root-dual-quadratic-q07-m20.json.gz` 中的实际物理 profile，允许入口核心的全部 support 系数成为边界未知量。它检验的是同一度量下的截断收敛，不再用每档重新调节 $\delta$、`vd` 的方式改善残差。没有接入真正非线性尾，没有闭合、全族嵌入或 reach 证书。

## 1. 冻结项与新未知量

物理度量为 $g=ds^2+a(s)^2d\theta^2$。准确的冻结 profile 是

```json
{"direction":"outward","vu":0.55,"vd":0.44677952493075596,"delta":0.15880707383811082,"ramp":0.4,"ramp_eta":0.05,"ramp_law":"flat","cycles":1}
```

其排序键、无空白 JSON 的 SHA256 为
`44baa11c4dc833095096d0f3ac58364ab328d5d7112e2464b6871fe31f63d13b`。
物理长度准确保持为保存的 float64 值 `1.7124958024211194`。一般角图与 core-blend 参考系数一直固定为 `[0.07, -0.0009800000000000002]`，频率 `[2,4]`。这些都是同一条加密链的输入；没有随实际求得的核心幅度重新生成参考图。

新脚本 `computations/geometric-fixed-dual-prefix.py` 复用原 two-control ODE，但改变其未知量布局：

$$
p_0=\log(q_{\rm actual}/q_{\rm gauge}),\qquad
p_1=\frac{q_4-q_{4,\rm reference}}{q_{\rm gauge}^2},
\qquad
p_j=\frac{q_{2(j+1)}}{\max(q_{\rm gauge}^{j+1},10^{-9})}\quad(j\ge2),
$$

其中 $q_{\rm gauge}=.07$ 恒定。全部参数只出现在核心边界条件，ODE 对参数的 Jacobian 准确为零。入口 Jacobian 使用固定材料角的完整 support 导数，而非固定法向角导数；径向长度、profile 和参考图均不依赖这些参数。

真实检查点初猜由 `geometric-checkpoint-core-pullback.py` 作物理角 pullback。没有把不同 Fourier 下标直接补零当作坐标恒等，也没有重置高度平均值。M20→M24 转换的位置投影误差约 $3.25\times10^{-13}$，高度平均值改变量及一、二 jet 的最大值分别为 $6.66\times10^{-16}$、$3.11\times10^{-15}$、$3.57\times10^{-14}$；参考图相同，所以这些修正只有数值舍入大小。每次真正求解都从自己的速度重新积分高度平均值。

首次实际 Jacobian 核对给出：状态方向导数相对差 $2.31\times10^{-15}$；参数 ODE Jacobian 为 0；完整入口参数方向导数的中心差分差约 $1.25\times10^{-10}$。

## 2. 旧 M20 的误差来源

直接比较保存的 $C^2$ PPoly 径向导数与有限 ODE 右端，再将同一曲线的 Frenet 速度在高角分辨率上重新投影。该分解没有重新解 BVP。

| 旧 M20 诊断量 | 最大采样值 |
|---|---:|
| 完整度量 FFT $\ell^1$ 误差 | $6.19813835\times10^{-6}$ |
| 径向 PPoly 速度残差 | $1.03725839\times10^{-7}$ |
| 保存节点上的径向速度残差 | $4.48\times10^{-17}$ |
| 有限 Fourier RHS 的速度投影缺陷 | $1.95385894\times10^{-5}$ |
| 384 点与 1024 点角求积导致的速度差 | $5.83\times10^{-15}$ |

角向度量 $G/a^2-1$ 的 $6.198\times10^{-6}$ 误差在保存节点上已经存在。将径向速度替换为重新投影的 RHS 后，$E-1$ 与 $F/a$ 的误差几乎不变。因此不能把问题归咎于径向 PPoly，也不能只增加角求积点数；主误差是未表示的 Fourier 速度。

这个区别有几何解释。在固定物理角坐标下，准确 Frenet 速度 $V$ 满足
$\partial_s|F_\theta|^2=2(a'/a)|F_\theta|^2$。若实际速度为 $V+e$，则

$$
\partial_s\left(\frac{|F_\theta|^2}{a^2}\right)
=\frac2{a^2}F_\theta\cdot\partial_\theta e.
$$

高频的速度投影误差可以通过角导数累积成 $G$ 的误差；零节点径向残差并不消除这种误差。

## 3. 已完成的固定 $g$ 加密

以下的 `metric` 是原 adaptive audit 对物理材料坐标计算的有限角 FFT $\ell^1$ 最大值。各档都包括保存节点、中点和另外的径向采样；它不是连续角度的区间包络。

| 频率数 $M$ | BVP 容差 | 最终径向节点 | 实际核心主系数 | `metric` | Fourier 速度尾 | 径向速度残差 |
|---:|---:|---:|---:|---:|---:|---:|
| 20，原设计检查点 | $10^{-6}$ | 466 | .07000000000000000 | $6.19813835\times10^{-6}$ | $1.95386\times10^{-5}$ | $1.03726\times10^{-7}$ |
| 24，固定 $g$ | $2\times10^{-7}$ | 760 | .06999896697835749 | $4.41907318\times10^{-6}$ | $2.00869\times10^{-5}$ | $6.39989\times10^{-9}$ |
| 32，固定 $g$ | $5\times10^{-8}$ | 1165 | .06999850542817766 | $1.26658218\times10^{-7}$ | $3.99762\times10^{-7}$ | $1.13822\times10^{-9}$ |
| 40，固定 $g$ | $10^{-8}$ | 2020 | .06999850315183198 | $1.15127137\times10^{-8}$ | $6.52023\times10^{-8}$ | $4.04626\times10^{-10}$ |

M24 用三次、M32 和 M40 各用两次 mesh 迭代达到各自容差。M32 的物理边界条件残差不超过约 $2\times10^{-16}$，M40 为 $1.473\times10^{-14}$。M24→M32→M40 的有限 Cartesian Darboux 误差从约 $.002910$ 降为 $9.19\times10^{-5}$、$4.07\times10^{-5}$，但这仍不是严格存在性证明。

同一固定材料点 $(s,\theta)$ 上的位置差包括完整高度平均值：

| 比较 | 最大点位差 | 点位 RMS 差 | 最大平均高度差 |
|---|---:|---:|---:|
| M20→M24 | $1.40046\times10^{-6}$ | $4.61033\times10^{-7}$ | $8.77167\times10^{-8}$ |
| M24→M32 | $1.01079\times10^{-6}$ | $2.42273\times10^{-7}$ | $3.78901\times10^{-8}$ |
| M32→M40 | $1.38710\times10^{-8}$ | $2.29651\times10^{-9}$ | $2.37107\times10^{-10}$ |

这不是最佳刚体对齐后的差，也不是材料重参数造成的假收敛：物理 $s$、参考材料角以及高度原点都相同。

进一步在相同物理 $(s,\theta)$ 坐标比较两 jet，包含由速度积分定义的平均高度一、二阶导数，得到以下最大采样差。它们没有按单位切向方向重新缩放；各档的共同 $a(s)$ 不变。

| 比较 | $F_s$ | $F_\theta$ | $F_{ss}$ | $F_{s\theta}$ | $F_{\theta\theta}$ |
|---|---:|---:|---:|---:|---:|
| M20→M24 | $8.15152\times10^{-5}$ | $4.61933\times10^{-5}$ | $.00641787$ | $.00288022$ | $.00167926$ |
| M24→M32 | $6.23311\times10^{-5}$ | $3.66006\times10^{-5}$ | $.00487326$ | $.00229261$ | $.00142845$ |
| M32→M40 | $1.12275\times10^{-6}$ | $7.11307\times10^{-7}$ | $.000104244$ | $.0000553469$ | $.0000494311$ |

因此不能只从 $10^{-6}$ 级位置接近就宣称 $C^2$ 收敛；这里另外检查了高阶差。末档径向二阶差比上一档缩小约 47 倍，为同一物理参数下的 $C^2$ 收敛提供了数值支持，但有限档比较不是 Cauchy 尾界或严格存在性证明。前两档完整位置和两 jet 差保存在 `geometric-fixed-q07-m20-to-m24-jets.json`、`geometric-fixed-q07-m24-to-m32-jets.json`；末档直接包含在 M40 检查点和轻量 summary 的 `shape_comparison` 中。

M24 的主要速度缺陷处，Frenet 根号余量约 $.707$，不是接近失域造成的求积问题。对同一 M24 曲线，仅提高 RHS 的 Fourier 投影到 M28/M32，缺陷即可从约 $2.01\times10^{-5}$ 降到 $2.10\times10^{-7}$/$4.81\times10^{-8}$。随后真正的 M32 解确实显著降低误差，故这个频谱诊断具有实际预测价值；不能把同曲线重投影本身冒充新的解。

## 4. 端口扩展与复现

M24 使用原 `computations/numerical-m2-port24.json`，SHA256 与输入检查点完全一致。M32 使用 `computations/numerical-m2-port32.json`；生成器只追加新的线性 DN 模式，原 24 项以及 `parameters`、`cut` 直接复制。M40 使用 `computations/numerical-m2-port48.json` 的前 40 项，其中旧 32 项同样原样保留。固定加密脚本要求同时提供 `--frozen-port`，逐项核对这些冻结值，失败就拒绝求解。端口文件中的 `extension_source` 记录新增模式的固定源码与线性运行来源。

```sh
python computations/geometric-fixed-dual-prefix.py \
  --input notes/root-dual-quadratic-q07-m20.json.gz \
  --source-topic /workspace/scratch/83b864ada613/visible-flex-source/topics/visible-flexible-closed-surface \
  --port computations/numerical-m2-port24.json \
  --out-prefix notes/geometric-fixed-q07-m24 \
  --modes 24 --angular 512 --tol 2e-7 --bc-tol 1e-9 --max-nodes 4000

python computations/geometric-fixed-dual-prefix.py \
  --input notes/geometric-fixed-q07-m24.json.gz \
  --source-topic /workspace/scratch/83b864ada613/visible-flex-source/topics/visible-flexible-closed-surface \
  --port computations/numerical-m2-port32.json \
  --frozen-port computations/numerical-m2-port24.json \
  --out-prefix notes/geometric-fixed-q07-m32 \
  --modes 32 --angular 640 --tol 5e-8 --bc-tol 1e-9 --max-nodes 5000

python computations/geometric-fixed-dual-prefix.py \
  --input notes/geometric-fixed-q07-m32.json.gz \
  --source-topic /workspace/scratch/83b864ada613/visible-flex-source/topics/visible-flexible-closed-surface \
  --port computations/numerical-m2-port48.json \
  --frozen-port computations/numerical-m2-port32.json \
  --out-prefix notes/geometric-fixed-q07-m40 \
  --modes 40 --angular 768 --tol 1e-8 --bc-tol 1e-10 --max-nodes 6000
```

输出 `geometric-fixed-q07-m24.json.gz`、`geometric-fixed-q07-m32.json.gz`、`geometric-fixed-q07-m40.json.gz` 及同 stem 的 `_coeff_*.npy.gz` 是实际完整数值检查点；系数为未四舍五入的 float64，分块文件各小于 5 MB，末档最大块为 4,243,519 字节。轻量 `-summary.json` 记录 profile 哈希、真实主幅度、误差、形状比较和来源。`-after-input-diagnostic.json` 是求解后的残差分解，`-spectrum.json` 与 `geometric-fixed-spectrum-screen.py` 保存同曲线频谱筛查。

本轮在 `metric` 降到所设 $10^{-8}$ 求解容差的同一量级后停止加频。末档 Fourier 速度尾仍大于径向插值残差，因此不能宣称已经撞到不可降低的机器／求解误差下限；这里只记录已经实现的同 $g$ 下降链与稳定的实际主幅度。

这条小幅核心固定度量链，与另一批幅度 $.38$、见证比例约 $.24$ 的强核心带边前缀，是不同候选。不能把两批候选的不同长处合并当成一个满足全部完成门的解。无论本前缀误差多小，非线性闭尾、固定握持区及全族 reach 条件仍未支付。
