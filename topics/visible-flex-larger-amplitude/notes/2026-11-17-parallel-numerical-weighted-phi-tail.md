# 固定物理角的完整加权零模 BVP：一次真实非零运行

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。这里记录实际实现与一个小参数接受结果，不宣称全振幅接合、闭面、reach 或旧 full112 gate 通过。严谨的加权零模及广义角谱定义见 [固定物理角说明](2026-11-17-parallel-model-fixed-physical-angle-mean.md)。

## 为何保留物理角

真实前缀的物理角 Fourier 展开转换到材料角后会显著扩谱。直接保留原物理角 phi，固定 `dtheta=rho(phi)dphi`，状态取

\[
\widetilde P=\rho P=\frac{h_\varphi}{rw},\qquad
K=c_\varphi+\sum k_j\cos(2j\varphi).
\]

第一行 `Ptilde_x=s K_phi-(s+ell)Ptilde` 精确保有限物理 Fourier 空间；T 与 U 用完整 rho、rho_phi 求出。零模采用字面 `Q_N(rho B)` 的完整链式导数，**没有**将 `Q_N(rho Kbar_x)` 或 `Q_N(rho T_x)` 错当成零。本次真实 state 只有物理 M8，但 rho 保留来自同一接受 core 的全部 112 个系数，不随 state 截断改变 metric。

输入物理角 trace 为 `parallel-trace0992-physical-m112.json`，SHA256

```text
36688dcba2bacef79d497b92a118b58141447f2630a9c735e75a63cf4aab719b
```

它的 phi 规范高度均值是 `.9703876955889461`、K 均值是 `.023119658917963193`。这两个值不能替换成材料角均值 `.9196724` 与 `-.0920876`。本次计算参数 lambda 只缩放非均值 Dirichlet 数据；整体高度平移可固定在上述 phi 高度均值。本次输出本身没有高度积分，几何读出须从该 trace 读取这个 anchor。

## 深端没有错套材料 diagonal 行

物理基 `{1,cos(2j phi)}` 上，先计算精确的 weighted cosine Gram，再去掉常数的 weighted 投影。对正定的 reduced `G` 和 sampled weak energy `A` 解 `A v=lambda G v`。每个非零广义角频率 `sqrt(lambda)` 保留实值，不取整；将同一个理想稳定图函数按该频率和真实 orientation 作用，构造密集的 homogeneous 深端行。

这定义一个明确的**有限弱角模型边界**，不是材料 diagonal 在物理角下仍为 diagonal 的宣称，也不是完整非线性无限 tail DN。M8/N512 的前八频率为

```text
2.0203340440, 4.4550866067, 8.2870165452, 14.1552482974,
22.4609744299, 33.7648931028, 49.0228213436, 70.8424012566
```

它们离真正材料整数谱的高端差别明显，故该低阶结果只用作算法/设计探针。`G` 最小浮点特征值 `.0860003105691211`，sampled rho 最小值 `.16602038993539225`。局部真实小态上的字面 weighted mean 导数链残差 `1.13e-18`，另由完整非线性 BVP 直接验证其可运行性。

## 接受结果与实际限制

背景仍是 [前份真实 cut 设计](2026-11-17-parallel-numerical-prefix-scale-tail.md) 的四 cell、`.05` bridge、orientation −1、clamp6 固定 Hermite metric，SHA `362509077ff7b1ce5011c838b73b5de056ced76257295be5ca53d5e6ddb357ce`。取物理 M8/N512、`lambda=1e-7`，完整 17 维 BVP 在 7 轮、3890 节点上接受，耗时 `121.38992132199974 s`。

| 项目 | 值 |
|---|---:|
| 数值 source-index 坐标 RMS | 9.970629017589853e-7 |
| BC 最大值 | 4.336808689942018e-19 |
| sampled weighted mean 漂移 | 4.312487154623521e-11 |
| sampled max abs P | .005698874864799446 |
| sampled max abs K | .2944976405110431 |
| sampled min L | .6837838621822763 |
| sampled min D | .9999995754970664 |
| sampled min (1+K) | .7055023594889569 |

这里只接受了该有限 BVP。四分点真实插值导数除回物理 r 后，完整 K 方程余项最大约 `1088.001245835277`，coefficient-wise 相对物理 ODE 余项 `2.3264903864704385e-4`；既有窄 pulse 的物理导数放大，也有 M8 保留空间以外的实际 K 方程内容。后续必须使用完整 geometry Gram 读出与谱/径向加密，不能用小 weighted mean 或 solver success 遮盖它。

该背景的大幅放大结构尚待重设计；材料与物理角这两次小 lambda 求解不是对真实 lambda=1 连接的证明。实际 far 稳定列、valley/pulse 校准与几何积分重构在并行继续。

## 复现与身份

源 SHA256：

```text
parallel_20261117_weighted_tail.py
1385121f2524e657ac09d421cddcc4a7924419bea49f7d2e00aec6d909a5a3ca
parallel_20261117_weighted_tail_bvp.py
fc1bd9c59b33b0baa1b3d755ec33c765fdd712710ac46bec4b44601d328f4c0f
```

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_weighted_tail_bvp.py \
  --background /workspace/scratch/16f63c8bce6b/parallel-prefix-tail-d4-s64-w06-k6.json \
  --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-physical-m112.json \
  --modes 8 --angles 512 --scale 1e-7 --tol 1e-6 --max-nodes 12000 \
  --out /workspace/scratch/16f63c8bce6b/parallel-weighted-tail-d4-m8-scale1e7.json.gz
```

输出 SHA256：

```text
ca2dcbd728446dbec42326e1e8cd4f4e826cefe9c80109781ef2378f6fec8715
```

所有状态、rho 表、广义角谱与 background/trace 原始文件均只保存在 scratch；源码、参数和来源足以复查，本 note 不提交 raw 曲面数据。
