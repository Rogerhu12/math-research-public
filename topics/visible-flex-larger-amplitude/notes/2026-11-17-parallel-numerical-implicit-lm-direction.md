# R647 补记：原 1662 上保全行、保边界的一次 LM 方向

## 冻结问题与此次范围

从原 `1662`、602 节点 warm 出发，保留 `M160/N2048` 全部独立 Y/U 变量、全部 580328 个 raw Pr 残差和原 325/157 边界行。没有消费 `5b965` 后续失败态，没有改变 g、角模、残差权重或非线性容差。

此次只准备并计算一个阻尼最小二乘方向，固定 `damp=1,maxiter=128,atol=btol=1e-8,conlim=1e6`；随后用 R647 完整二次 ray 接口读 `alpha=1,.5,.25`。未调阻尼、未执行非线性迭代，也未把试点登记为物理接受父。一般 LM 原理不作为新定理；新增内容是这份完整有限系统的尺度、边界处理和真实运行结果。

## 完整右尺度与边界可行方向

记节点导数矩阵为 `CY,CU`。一次性逐节点/逐中点形成局部 dense 矩阵，每块用后丢弃，不装配全局 J。节点贡献是 `CY/CU` 各列平方和；每个实际 Hermite 中点的四块是

\[
 L_Y=\tfrac12C_Y-\tfrac{3}{2h}C_U,\quad
 R_Y=\tfrac12C_Y+\tfrac{3}{2h}C_U,\quad
 L_U=\tfrac h8 C_Y-\tfrac14 C_U,\quad
 R_U=-\tfrac h8 C_Y-\tfrac14 C_U.
\]

**先形成各块，再求列平方和**，因此包含全部交叉项及 `1/h`。另加入原 `BA/BB` 的端点列平方和。得到完整 `diag(JᵀJ)` 的数值估计 `d>0`，固定正对角尺度 `S=diag(d^(-1/2))`；没有任意截断或零列 floor。

两个端点分别取原边界矩阵 `B`，定义 `C=BS`。左 325 行有明确互异单位三角 pivot：固定 `R0/前三R`、全部 support 方程的 T 槽和全部 Z 槽。右 157 行用**原 binary64 BB 的准确整数运算**证明

\[
 \|BB^T-I\|_\infty<.005043172408891166<1.
\]

方法是把全部 binary64 条目乘同一个二的幂化为整数，准确计算整数 Gram 和行绝对和；报告保留整数分子、二幂分母和严格比较结果。正对角 S 保持满行秩，不要求尺度后的 Gram 接近 I。

数学上取 scaled coordinates 的正交投影

\[
 \Pi=I-C^T(CC^T)^{-1}C.
\]

两个端点以同一 S 的行归一化 QR 实现该投影，其余节点/U 槽保持恒等。以原 tiny BC 残差构造 `d0=S Cᵀ(CCᵀ)^(-1)(-r_bc)`，然后只求

\[
 \min_z\|r+Jd_0+JS\Pi z\|_2^2+\|z\|_2^2,
 \qquad D=d_0+S\Pi z. \tag{1}
\]

全算子仍有 580328 行，原 BC 仍参与实际 residual 和最终检查。实现的转置是 `Π S Jᵀ`；没有把不同尺度下的投影混用。QR 是浮点评价，其正交性和剩余原 BC 另行数值报告，不把它冒成逐位准确投影。

## 唯一预算的实际结果

完整列范数耗时 `33.9029 s`，范围 `1.90963629…3.2633269709e10`；S 范围 `5.53566378e−6….723643508`。行归一化 scaled 边界条件数为左 `36.7451`、右 `2.34698`。`d0` 最大 `2.55552e−17`，支付后的原 BC 最大 `3.08149e−32`。新 scaled/projected 算子的全向量伴随检验、除以双边范数积的相对差为 `1.36754e−19`。

唯一 LSMR 在 **60/128 次**迭代返回 `istop=2`，耗时 `27.9042 s`；LSMR 本体调用完整 Jv 60 次、完整 Jᵀv 61 次。独立重算的正则 normal residual 为 `3.55490907e−9`，相对 `||Aᵀb||` 为 `1.13173e−7`；LSMR 的条件估计为 `2.03141`。这不是原 Pr 方程已达到 `1e−8`，更不是非线性 BVP 收敛。

| 量 | 实际值 |
|---|---:|
| 原完整 raw SSE | 1.5321026127227238e−4 |
| 完整线性模型 SSE | 5.45386957703086e−5 |
| 正则惩罚 `||z||²` | 2.0204880809132013e−5 |
| 正则目标总值 | 7.474357657944062e−5 |
| 满步真实 raw SSE | 5.4538649626341434e−5 |
| 半步真实 raw SSE | 8.930902566339144e−5 |
| 四分步真实 raw SSE | 1.176182825212794e−4 |
| 原 BC 方向线性剩余最大 | 7.222078385283539e−24 |
| `max|dY|` / `max|dU|` | 9.98745888e−9 / 2.87943539e−5 |

三个读出步长均通过原 `S(alpha)<(1-.4alpha)S(0)` 门。满步 SSE 降低约 64.4%，并与完整线性模型非常接近；本次主要调整独立 U，不能据此声称几何轨道已经大幅推进。

R647 全向量 ray 给出 `r·j=−7.8466684692e−5`、`q²=2.9255817649e−14`。这次二次项很小，和前次真实 Newton 更新割线的四次项占优表现不同，但**两次基点不同，不作同点算法优劣比较**。全行 JVP 与 complex-step 相对差 `1.72010e−16`；直接 trial 与二次式最大差为节点 `5.155e−16`、中点 `1.092e−11`、BC `9.715e−17`，均保留实际浮点差异。

准备、唯一方向与 ray 总耗时 `74.3126 s`，最大 RSS `390944 KiB`。没有增加迭代预算或其他阻尼值。物理分支、实际 cubic/quintic Gram 与同 g 几何仍须另行审计；本条不替代这些门。

## 冻结身份与复现

- 新源 `parallel-implicit-lm-direction.py`，11907 B，SHA256 `90706d6a03e74b220dddffde98386d338504b9bbdef95f83bdacc34b34d062da`；[已刊源码](../scripts/parallel_20261117_implicit_lm_direction.py)。
- 原 warm `parallel-hold-m160-short-bvp-warm.json.gz`：`1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057`。
- 完整 Problem 源 `5b965b9c4f9979a5b8dcc38661de027570d04d55aceb86de0dc7b1217fb03aac`；多项式源 `ba0b17fc85af8510c7c45b22a8facecd59061f53b3f7fd4adb48d3380c74e1a2`。
- 完整 matrix-free 源 `ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4`；ray 源 `e67f7d1bf021fd88646e1a77057b4557418ff77ebd5032461d8a46dd7f6498fc`。
- `parallel-implicit-lm-direction-once.preparation.json`：`f691e4e31d53d04a10a4c16be6c23bf15fa0c7aaed56d2338c214b40e2618224`。
- `parallel-implicit-lm-direction-once.json`：`5ac4371a2ff1b7be659a21a507e62d9974c75878308610d095389cefda1b1a7f`。
- `parallel-implicit-lm-direction-once.ray.json`：`1192cd08b8806ebba417ad1e0ad23b0c0d323ff131d8254aabefda7695903353`。
- 原始方向 `parallel-implicit-lm-direction-once.direction.npz`：`5629db05e0cc7b014c6eb4375badb35ea1d408f40d8cdbccef88122e6150798e`；含完整 `Y,U,dY,dU,z`。方向 binary SHA 为 `260f3911be355756e9d1b2e74fb279e5fbcb79d2749a454385ec2327be3ed76d`。
- 对角/投影准备数组 `parallel-implicit-lm-direction-once.prepared.npz`：`d742521c362b0f680bf53a329784a516416da83fbfd226a23f3a4cb051c7a36c`。
- 完整日志 `parallel-implicit-lm-direction-once.log`：`f1ad8ccd69bb324e95529eef9557d1488962a2689b4fe8b5a83ab5aa7cc6ddad`。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_lm_direction.py \
  --topic math-research-public/topics/visible-flex-larger-amplitude \
  --problem-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_newton.py \
  --warm parallel-hold-m160-short-bvp-warm.json.gz \
  --polynomial-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_probe.py \
  --matrix-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_matrix_free.py \
  --ray-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_quadratic_ray.py \
  --out parallel-implicit-lm-direction-once.json --execute-direction
```

去掉 `--execute-direction` 只作准备。运行前后校验所有冻结源，报告含 SciPy LSMR 文件 SHA；所有 raw/数组留 scratch。普通 FFT、QR、列范数、LSMR 数值不是区间证书；只有明确标出的 BB 整数秩步骤使用准确算术。报告计时/平台字段可能使重跑后的文件 SHA 不同。

## 唯一 LM 满步的原 8192 物理审计

固定读取方向文件 `parallel-implicit-lm-direction-once.direction.npz`（SHA256 `5629db05e0cc7b014c6eb4375badb35ea1d408f40d8cdbccef88122e6150798e`），验证其中 Y/U 与原 `1662` warm 逐位相同，只对 `Y+dY,U+dU` 调用一次未改的 `P.physical_samples`。没有新求解、其他 alpha 扫描或初始 warm 重审。

602 个节点、601 个实际公共三次中点均用 8192 角采样。结果为：

| 指标 | 实际值 | 返回的极值位置 |
|---|---:|---|
| rho 最小 | .16601843096428737 | 原接口未返回角 argmin |
| Q 最小 | .027562119419843777 | node0，s=0，phi=0 |
| W 最小 | .0002193157012722163 | node569，s=1.0233471879626843，phi=3.124718864923051 |
| H 最小 | .00021257030236521406 | 同上 |
| 正分支 normal velocity 最小 | .014579874862806463 | 同上 |
| 实际公共三次 relative Gram 最大 | .0008046486684836207 | midpoint600，s=1.029958740822432，phi=pi/2 |

三组未保留二次频率 `j=161..320` 的系数最大绝对值分别为 `1.9024043994e−6 / 1.5696292581e−5 / 1.2763603799e−6`，共 480 个未保留标量模式；原审计接口只返回其最大值，没有返回对应节点/模式 argmax，不能把它们归到 Gram 最坏点。

所有已采样 rho/Q/W/H/normal 门通过，原 BC 实际剩余 `9.71445e−17`。但 raw 点约束三组最大值为 `.0013459734/.0056061525/.0008046487`。与原已存 preparation audit 的初始 Gram `7.50500727e−6` 相比，本次 Gram 增大，虽然完整 retained raw SSE 降低约 64.4%。这是降低兼容行与暂时增加单位速度误差的具体权衡；不能由 raw SSE 下降宣布几何改善。没有重运行初始审计；旧数据取自 `parallel-model-implicit-frenet-602-preparation.json`。

本条仍只是唯一代数试点的有限节点/中点读出，不是全角全径向证书或 C2 几何。公共三次的二阶径向导数可能跳；未来真实 C2 必须使用其明确共同二阶 jet 并重新读出。

[已刊读出源](../scripts/parallel_20261117_implicit_lm_physical_audit.py)，2039 B，SHA256 `839cd50d09aa19a1117b4c9846152bedf5959ab759d4cb6b296d7a4530944010`。报告 `parallel-implicit-lm-fullstep-physical.json` SHA256 `ebb364fee7e9a8d5fdfb587a1d89c440f4159862c8453105edf07dcf06c6fd84`；满步 Y/U binary SHA `759471bd87f8d856407750f80b6b794031689a6a1135d41260e5de80874a6f5b`。本次耗时 4.96074 s，raw 留 scratch。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_lm_physical_audit.py \
 --topic math-research-public/topics/visible-flex-larger-amplitude \
 --problem-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_newton.py \
 --warm parallel-hold-m160-short-bvp-warm.json.gz \
 --polynomial-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_probe.py \
 --matrix-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_matrix_free.py \
 --direction parallel-implicit-lm-direction-once.direction.npz \
 --out parallel-implicit-lm-fullstep-physical.json
```
