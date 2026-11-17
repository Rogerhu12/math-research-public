# 完整弱尾高度对直接径向积分的校准

本条只记录一次已实际运行的有限候选交叉检查。它排除了直接高度优化中一个具体误判来源：同一个已接受弱尾高度经过径向构造仍保持约 `1.4e-7` 的实际采样 Gram 误差，因此当前某些强制样条/端点候选的约 `0.29` 误差不能归罪于这个径向积分实现。这里没有新的闭曲面、无限尾、reach 或振幅一结论。

## 输入和字面构造

输入是 best4 背景的材料 `M=8`、`lambda=0.0014` 接受场，其状态 SHA-256 为

`09d206be0c9c0a47df006920c99f33e8a95e915542f04b068b3899d767549cde`。

固定标量背景 SHA-256 为

`487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15`。

源码始终对输入原字节计算摘要。材料平均高度的浅端锚为 `0.9196724087226285`。物理角密度取真实 M112 切口中的完整 `rho`，在 `N=512` 等距物理角点上评价材料有限高度模 `cos(2j Theta(phi))`；不插值材料角样本。

高度取 `HeightModes.at_r` 的实际积分 K 定义，同一候选的 `h_r`、`h_{r phi}` 由其有限系数直接评价。浅端平面圈和转角由这一弱高度本身的角向原函数构造，未缩放完整前缀的 XY 圈。后续按 [R631](../results/R631-compatible-height-actual-geometry-and-C2-radial-map.md) 的径向方程积分：

\[
S=1-\frac{h_\phi^2}{r^2\rho^2},\quad
D=(1+w^2)S-h_r^2,\quad
q=r\rho\sqrt S,\quad
a=\sqrt{D/S},\quad b=-h_rh_\phi/q,
\]

\[
\alpha_r=\frac{h_r(h_{r\phi}-h_\phi/r)}{r\rho S\sqrt D},\qquad
F^{xy}_r=b(\cos\alpha,\sin\alpha)+a(\sin\alpha,-\cos\alpha).
\]

角导数是所得平面位置数组的字面 FFT 导数，未用 Darboux 误差预测或目标切向量代替。径向域为

`[1.167318285443017, 1.6884392650708613]`。

## 实际输出

| 每段 Gauss 阶 | 径向面板数 | 评价点数 | 最大实际相对 Gram 算子误差 |
|---:|---:|---:|---:|
| 4 | 55 | 112640 | `1.2925768999684059e-7` |
| 8 | 55 | 225280 | `1.4047244678572218e-7` |
| 16 | 55 | 450560 | `1.3737270454505800e-7` |
| 8，逐原面板二分 | 101 | 413696 | `1.3788305086581687e-7` |

二分后面板数不是简单的 110，是因为原源端点中存在只差一个浮点单位的重复位置；新节点取精确浮点去重。该校准保留了原优化器当时的面板定义，未把这些微小重复区间解释为实际结构。

在最后一行，最坏点为 `r=1.6884384823715646`、`phi=pi/2`。实际归一化 Gram 三项为

`rr=0`，`phiphi=-1.3788305086581687e-7`，`rphi=-9.855154769164976e-17`。

`min D=0.9964483548046017`，整个径向区间的最大转角变化约 `3.659034742247158e-4`。这些是有限点求积比较，不是全域误差上界；约 `1e-7` 的量级也不能在此被视为只剩积分误差。

## 对后续优化的实际意义

这项检查**没有**把弱尾替换成满足真实完整前缀切口和有限外端平坦约束的候选。当前直接高度试验中的三个操作——改浅端高度二阶 jet、截取自由角模、强制原有限末端非均值高度二阶 jet 为零——都会改变实际曲面。把完整弱高度原样代入能恢复低 Gram，说明这些改变必须逐项单独评估，而不能把原接受场的低误差传给其样条拟合。

独立弱场在有限深端仍有非零高度角模；本校准不声称该端为圆圈或平领。后续优化继续支付真实 lambda=1 切口、外部平坦接缝和实际曲率。

## 可复现文件

- 冻结源：[direct-height-exact-warm-check.py](2026-11-17-parallel-model-direct-height-exact-warm-check.py)，SHA-256 `5ddd8e500452f402f64d0f3c4354c1fdda0e5078d7b092a1a4f736d8bda1cffd`。
- 仓库外历史输出 `parallel-model-exact-warm-radial-check.json`，SHA-256 `5356bafc98aee6411897c14b93a16ad20e4ea210a8d4d6358f4ad664329a4c45`。
- 本次同刊的[高度模 API](2026-11-17-parallel-geometry-height-mode-api.py) SHA-256 `dc3be256fd0566d4c2dd21b2bb362d81b04e8481167e35027a73a061237775f8`。该源只依赖此冻结 API、角原函数 helper 及固定 Background 定义，不导入仍在修改的直接优化器。raw不入库。

在本课题目录，令下述路径分别指向相同摘要的原始输入：

```sh
OPENBLAS_NUM_THREADS=1 python notes/2026-11-17-parallel-model-direct-height-exact-warm-check.py \
  --trace /workspace/scratch/16f63c8bce6b/parallel-model-trace0992-jets.json \
  --state /workspace/scratch/16f63c8bce6b/parallel-best4-material-scale0014.json.gz \
  --background /workspace/scratch/16f63c8bce6b/parallel-best4-background.json \
  --mean-anchor .9196724087226285 \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-exact-warm-radial-check.json
```

输入物理切口摘要 `5db66710248b645f455e1f156bc4dc6654dafd08b4387cefccbcfda1137979f8`；它只提供物理角密度。所有高度及初始 XY 圈都来自上述弱尾场。

切口可由已刊 `scripts/parallel_20261117_prefix_node_trace.py` 从 b677 输入，参数 `--s .992 --angles 2048` 重建；输出改为上述 trace 路径。该源 SHA `dcc00dddf11bed8235ab1a6c733ab5186e92421ad29bc30ef25730f781445d98`，保完整112项rho，不需保存额外原始数组。
