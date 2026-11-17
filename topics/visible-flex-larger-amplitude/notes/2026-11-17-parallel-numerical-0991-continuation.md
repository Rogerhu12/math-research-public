# 新设计标量圆弧下的 M96 前缀 0.990 → 0.991

会话：`Astra-larger-parallel-16f63c8b-20261117`，数值支线。这里登记一个**新的有限开前缀数值解**，不是闭面、完整 tail、全时段或 reach 证书。R624 给出的完整卷积 Jacobian 已实际用于这一步，而不只停在矩阵比较。

## 1. 输入来源与新边界问题

起点是原公开 Actions run `43580643038` 的 free3 M96/N1024、`s=0.99` 已接受解。原运行源 revision 为 `be989410a0149c2d5b24feec5b32ba3f93ad5c70`。原数据曾在 commit `60321451c058c6a51da58c37ae5ec6f2d1145f74` 的

```text
topics/visible-flex-larger-amplitude/notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz
```

公开；按规则 15 后来删除。本次只将该已验证历史 blob 恢复到仓库外 scratch，输入 SHA256 为

```text
b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff
```

不重报旧段成功。保留完整 96 个偶 Fourier 模、1024 点非线性角采样，固定 core 的前三个系数，其余 93 个作自由 core 参数；保留完整 290 维 Frenet 方程和分离边界行。

在 `s0=0.99` 之后重新设计 scalar metric：令 `theta0=asin(a'(s0))`、`kappa=-a''(s0)/sqrt(1-a'(s0)^2)`，接

\[
\theta(s)=\theta_0-\kappa(s-s_0),\qquad
a(s)=a(s_0)+\frac{\cos\theta(s)-\cos\theta_0}{\kappa}.
\]

数学定义取原 exact-rational Hermite 末端 0/1/2 jet 接这条圆弧，因而保持该接缝的 C²。浮点评估得到 `a0=1.1666064106120295`、`v0=0.3579486389103069`、`u0=-2.0101206107275877`、`kappa=2.15275972133223`。其中 `v0` 与原末 knot 二进制值 `0.357948638910307` 差 1 ulp；这些计算值只用于近似求解，不作为精确接缝等式的位级证明。

新的终端边界：在**前一个实际已接受端点**建立正 Gauss principal-normal 矩阵，将此常数矩阵搬到新端点，以二阶 Taylor 预测作目标值。这是一个明确的新有限 BVP；它没有被宣称为非线性无限 tail DN。旧 `.012` 预测端点 projector 预检失败也不能用作该新 BVP 无解的论据。

## 2. 新接受结果

完整求解只用一轮 Newton，424 节点、423 单元，耗时 35.1702 秒。实际输出为 scratch 的 `parallel-continue0991.json.gz`，SHA256：

```text
b9b96a861d2d3b8f6eef86ea799e4c0bba9dae21fc6dab9de1d3703a49ade768
```

| 项目 | 值 |
|---|---:|
| 新端点 | 0.991 |
| collocation RMS 最大值 | 5.457043164769601e-7 |
| 边界残差最大值 | 1.0299920638612292e-18 |
| core 轴向 support gap | 0.9600009842481552 |
| sampled core rho 最小值 | 0.16603960569172482 |
| 反射开前缀直径上界代理 `2 max |F|` | 3.5016079258562813 |
| 端点 a | 1.1669633539145448 |
| 端点 a' | 0.3559376904185004 |
| 端点 a'' | -2.0117748196373655 |

上述 gap/直径代理只能描述开前缀的几何余量，不能替代完整曲面上的 held Hausdorff 下界或实际闭面直径。

### 实际 C² quintic 的独立读出

不能把 `rhs(y)` 当作插值场的实际导数。新 `parallel_20261117_prefix_readout.py` 从公共节点 `y,y'` 和完整解析微分所得 `y''` 定义唯一的分段 quintic。每段匹配公共二阶端点 jet；把这些 binary 节点数据解释为实数，所得场在接缝上数学 C²。读出使用这个 quintic 的**实际** `F_s,F_ss,F_theta,F_stheta,F_thetatheta`。

误差是归一化二维 Gram 差的算子范数，不是分别取三项的最大值。目标是该固定 scalar 和重新求出的固定 core rho 所给的 `ds²+a(s)²rho(theta)²dtheta²`。这是一个固定最终近似场的采样审计，尚不是沿继续求解过程中固定 core 的网格收敛定理。

| 角样点 N | 每单元径向分数 | 总样点 | 最大相对 Gram 算子范数 | 最大实际主曲率 |
|---:|---:|---:|---:|---:|
| 1024 | 0,1/2,1 | 1,299,456 | 8.353844566587575e-7 | 6.300054115323305 |
| 2048 | 0,1/4,1/2,3/4,1 | 4,331,520 | 8.353844566587575e-7 | 6.301142267678157 |

最大 Gram 样值在 `s=.991, theta=2.705942109830271`。最小 sampled Gram determinant 为 `0.027569150658263385`。两次读出都得到 sampled witness distance 最小值 `0.9600009842481552`；这不是连续 witness 距离下界。N=2048 是对同一个 M96 场加密求值，没有重新求解成 M192，也没有把采样稳定误称为连续域包络。

读出输出 SHA256 分别为：

```text
74191514ac3c556707c83a2966a23df10168a04816d3639b61fa8ce69bab5f0a
bb9768423df884efbdd56fb9062884c10367a4b46e58fe18d67cb8746c1d6324
```

## 3. 精确复现实参与版本

以下输入/输出路径都在仓库外，仅为本次运行位置；用上述 `git show` 恢复原输入后可换成本地路径。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_continue.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-free3-099-accepted.json.gz \
  --duration .001 \
  --out /workspace/scratch/16f63c8bce6b/parallel-continue0991.json.gz

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_readout.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-continue0991.json.gz \
  --radial-subdivisions 2 \
  --out /workspace/scratch/16f63c8bce6b/parallel-continue0991-quintic-r2.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_readout.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-continue0991.json.gz \
  --angles 2048 --radial-subdivisions 4 \
  --out /workspace/scratch/16f63c8bce6b/parallel-continue0991-quintic-r4-n2048.json
```

接受运行的 `continue.py` SHA256 是 `00c7e5563a49248b4d081f71a6c3e0da66c5bf2b5b5357e51537bc129e66b458`，在 R624 当次提交中保留。此后源码做三项保持问题定义的维护：抽出 `Profile` 模块；使新的接受输出可以继续输入并保留原圆弧起点；加入无下降时保留旧可行点的安全回溯。新保存点 `continue.py` SHA256 为 `d5da2b60dd3f6e0d061750ae172a474cbcae157b8923ff0512c0543dded3ae49`。新 `Profile` SHA256 为 `08b1894ca407a0c49b0de80427c669cafe702ab5878b1abf7b346994138d79b3`；读出源 SHA256 为 `045533247125e318d5b5051f0e98b286f287126f51c6e616d938019f8432d29c`；Frenet 源 SHA256 为 `7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831`。

运行使用已有 separated-QR 后端 `computations/geometry_20261114_separated_qr_bvp.py`，只改变完整 collocation 系统的存储/消元方式，不删状态或边界行。原 direct-CSC 尝试有内存失败，不作为数学反例。

## 4. 没有接受的较大步与当前边界

`.99→.996`、fixed3 的初版 QR 尝试在后续 Newton 试点失去 Frenet 可行性；没有接受结果。原 SciPy line search 在所有下降测试失败时仍会接受最后试点，后续保存版本已改为保留旧点。

`.99→1.002`、fixed1 尝试给更大的 core 自由度，但达到 800 节点上限后仍未接受：RMS `6.711240268086412e-4`、BC `1.3877787807814457e-17`，耗时 285.435 秒。输出 SHA256 `bb8eb1e80d4e4e63164d4cbb355302914c537159dd320543767c84cc1815b1b0`。这里 BC 小只表示该有限边界行匹配；内部残差仍大，不能据此发出 metric/闭合通过声明。

当前新结论是一个真实的新区间 `.990→.991` 和可重复的实际 C² 场采样。闭面接缝、全时段同 g、无限 tail、连续域误差上界、reach、完整图像 held 距离仍未解决。后续前缀延拓由主会话接手；本数值支线转向包含动态 K 零模的 tail BVP，减少每 stage 非线性均值根求解。
