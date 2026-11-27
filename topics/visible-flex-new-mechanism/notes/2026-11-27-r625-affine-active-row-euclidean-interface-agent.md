# R625 后继接口：实际仿射活动行与原 Euclidean 阻尼

**状态：纯源码接口与纸面等价关系，未在本地执行科学。** 使用方是原全行 BVP 的新高度可行方向实现；这个 helper 不生成新候选，不调用反馈、M、rho、ruling、积分或新的物理观察点。

源码 `scripts/r625_affine_active_rows_euclidean_agent.py`，19509 B，SHA-256 `0d555bb870a06ae498a2cbb73babde1ebec0fa7a67ee3d49b38aada07ec8d082`。底层仍是已发布的 `r625_complete_rows_euclidean_qr_svd_agent.py`，SHA `56a089e6d5348fdf9d55f78138f76775de66f686976269ad08c1f2636a1d8555`；没有修改该文件。

## 输入输出与准确数学问题

调用：

```python
factor = AffineActiveRowEuclideanFactor(A, b, C, g, clock, counts, label)
direction, report = factor.solve(positive_lambda)
```

`A,b` 已经含原行权，并已由调用方准确消去原末十个已知增量及本模式固定的长度增量。`C d=g` 是同一剩余坐标下的全部实际活动高度等式；`g` 必须已经扣除原已知增量的贡献。固定当前实际高度时，完整高度增量为零，但剩余列的右端仍是负的已知增量贡献，不能未经扣项便置零；固定当前值也没有把它吸附到盒壁。返回 direction 的维数、顺序与输入 A 的剩余原坐标一致，由调用方回填原全部已知增量。

给定完整行的数学问题是

$$
\min_{Cd=g}\|Ad-b\|^2+\lambda\|d\|^2,\qquad \lambda>0.
$$

设 C 有 m 个独立行、n 个剩余坐标。完整 QR

$$
C^T=Q_1R,\qquad Q=[Q_1\ N]
$$

给出 `d0=Q1 solve(R.T,g)` 与全部解 `d=d0+Ny`。因为 `N.T@N=I`、`N.T@d0=0`，

$$
\|d\|^2=\|d_0\|^2+\|y\|^2.
$$

因此只需对 **所有原目标行** 的 `(A@N,b-A@d0)` 求原 Euclidean 阻尼解，再回填 `d0+Ny`；常数 `lambda*||d0||^2` 不改变 y 的最小点，没有漏掉原惩罚的交叉项。正交零空间变换保原惩罚，没有加入列归一化。底层全 QR / R 全 SVD 保留每个目标奇异方向，不截秩，不构造正规方程。

无活动约束时直接用原 A,b；m=n 且可用时只有一个 d0，正确返回这个与 lambda 无关的方向，不向底层传零列矩阵。m>n 时显式失败，不删除活动等式来制造满行秩。

## 有限精度边界

实际源码在完整 C.T QR 后使用明列的数值依赖尺度

`eps64 * max(n,m) * Frobenius_norm(C)`。

若 R 的任一对角绝对值不超过该值，或者因子非有限，则**整个这个活动集合的参数化失败**。不会删掉一行、改 C、截掉目标谱或宣称准确秩已认证。这是该线性构造的数值可用性规则，调用方记录失败并保原状态；它不是新增的物理资格门。

浮点 Q、N、d0 不能据纸面等式当作准确逆证书。每次原坐标方向返回前记录：

- `C@d-g` 的原活动等式缺陷；
- `A@d-b` 的全部原加权行缺陷；
- `N.T@(A.T@(A@d-b)+lambda*d)` 的约束切空间正则 stationarity；
- 原方向 Euclidean / infinity 范数及非有限观察项个数。

在仿射约束下，完整未投影梯度通常不为零，不把它当失败。观察算术 overflow 记为 `None` 和对应计数，不据观察值大小拒绝一个有限方向；调用方原未缩放 prediction、信赖域、真实曲线物理盒、全部原 nonlinear 门仍决定下一步。

## 缓存、时钟与费用

同一真实 A,b,C,g 的 factor 可用于多个正 lambda；状态或活动集合一变，调用方建立新因子。该 helper 不自行混用缓存，不读取旧别点矩阵。完整输入 SHA、矩阵/约束维数、phase、每个已开始/完成步骤及异常都有小型 receipt。`.receipt` 是当前记录；模块 `factor_receipts()` 包含构造器尚未进入调用方缓存就失败的记录，且捕获底层因子失败留下的原 partial receipt。

全部完整 C.T QR、R.T 求解、A@N、A@d0、底层全 QR/SVD、每个 lambda solve、原坐标回代和必要线性读数都有实际计数/时间，并在合适边界调用既有 public science clock。总构造和总 solve 时间包含内因子时间，子项不能再相加冒作独立费用。所有矩阵与因子只在内存；receipt 不输出原矩阵、N、d0、方向数组或谱数组。

调用方仍负责实际高度行来源与全曲线门。这个线性等式求解器没有声称活动行保证所有节点、连续曲线或全部物理盒。本文及源码准备仅执行文本、AST、hash；科学 QR、SVD、浮点范数和求解都留在声明的公开 Actions 中。
