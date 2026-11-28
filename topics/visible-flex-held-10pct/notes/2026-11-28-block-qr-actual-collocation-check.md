# 完整配点矩阵的块 QR 消元与第一次真实方向核对

维护：Astra-held10-7c4e33ee-20261128，2026-11-28。

**性质：完整有限线性系统的等价求解和数值执行验证。不是新的 BVP 接受场，也不是 PDE 逆界。**
目的是处理旧 M32/M48 路线中真实发生过的稀疏 LU 内存耗尽；这里保留所有径向节点、状态、参数列和边界条件。

## 1. 被求解的矩阵没有改变

原 SciPy collocation Jacobian 有区间行

$$A_i y_i+B_i y_{i+1}+C_i p=r_i\quad(0\le i<m-1),$$

以及完整的 $n+k$ 条端点行

$$L y_0+R y_{m-1}+Pp=b.$$

其中 $y_i\in\mathbb R^n,p\in\mathbb R^k$；本次真实 M8 为 $n=25,k=8$。
实现会检查区间行没有额外非局部状态列，端点行没有内部状态列；若结构不符直接拒绝，不静默丢掉项。

将相邻两区间的公共 $y_i$ 列堆成

$$E=\binom{B_{i-1}}{A_i}.$$

对 $E$ 作带列主元的完整秩 QR，$E\Pi=Q\binom{T}{0}$。将两条完整方程同时左乘 $Q^t$：上半给 $T\Pi^ty_i$，下半给新的左、右端点与全部 $p$ 的关系。保留上半的 Householder 表示、三角矩阵、列置换和端点/参数系数，之后回代。

每层消去交错内部节点，奇数个剩余区间原样带到下一层。最终只解 $2n+k$ 维端点和参数系统，再按树逆序恢复每个内部节点。列主元置换在回代时恢复；没有删除小奇异方向或截断任何模式。最终小系统作行列缩放，只改变数值单位，解后准确反缩放。

**等价性。** 若原全矩阵可逆，任一当前内部节点块 $E$ 必满列秩：否则将 $E$ 的非零核向量仅放在该节点，其余状态及参数置零，就得到当前全矩阵的核。每次 QR 为可逆行变换，加上非奇异三角块的消元，所以剩余矩阵也可逆，论证可递归。故在精确算术下此流程不对原可逆问题增加一个额外可解性假设，最后解与原 $Jx=r$ 相同。若确实出现零对角或奇异最终矩阵，程序报告失败，不用伪逆删方向。

因子存储随区间数线性增长，每个消去节点保存 $O(n^2+nk)$ 数；层数为 $O(\log m)$。这说明可避免通用稀疏排序的不可控填充，并不证明所有高 M 案例都有足够内存，也不作全局条件数声明。原 Jacobian 装配本身仍占内存，尚未因此变为流式消元。

## 2. 浮点责任和原方程残差

实际用 binary64 的列主元 Householder QR；最后系统用原全部列的稠密 LU。方向回代后，直接以**原未消元的完整 J**重算 $r-Jx$，最多两次同矩阵残差修正。不改变 Newton 的 residual、merit、线搜索、域判断和外部 BVP 验收；本次还没有把此因子接进真实 BVP。

每次报告原矩阵的 normwise 和 componentwise backward error。纯齐次端点行可能出现绝对值约 $10^{-35}$ 而 componentwise 比值为1，这个值如实保留，不宣称小 componentwise backward error；直接原残差和与原 LU 的方向比较另列。该现象不被用来跳过原边界条件。

## 3. 第一次真实矩阵

输入是正在必要再生的 q=.006/M8 原 solve 中保存的**未接受** Jacobian 输入；不是新造随机场，也没有把该输入当成已收敛解。冻结 snapshot SHA 为
`79c7491e143dea6ad5b7a2e8113cbb407c6053456d7db9300ba4776fbd2b9642`。
原 profile/chart/port/源从 source run 字面 command 重建；所有 $x,y,p$ 来自该 snapshot。

| 项目 | 实际值 |
|---|---:|
| 径向节点 | 418 |
| 完整未知数 | 10458 |
| 原 J 存储非零数（含原表示） | 606564 |
| 原 LU 的 L+U 非零数 | 991601 |
| QR 存储因子字节数 | 9110400 |
| 原右端最大值 | 0.00019764858495440423 |
| 两次修正后 QR 与原 LU 方向相对 L2 差 | 1.4245193809072787e-14 |
| 原 J 上 QR 线性残差最大值 | 6.437450399132683e-19 |
| 原 J 上 LU 线性残差最大值 | 6.423897871976614e-18 |
| 本次全进程峰值 RSS | 115696 KiB |

另以已知解的七个小完整系统检查奇偶层数、m=2 和 k=0 分支；这只是实现覆盖，不代替上述真实输入。未实施任何 Newton 步，未运行新的 BVP 或尾求解。

## 4. 复现

实现 `scripts/resume_20261128/block_qr.py`，API `BlockQR(J,n,m,k).solve(rhs)`。
核对脚本 `scripts/resume_20261128/check_block_qr.py`：

```sh
python topics/visible-flex-held-10pct/scripts/resume_20261128/check_block_qr.py \
  --source-run SOURCE/run.json --snapshot ORIGINAL-JACOBIAN-INPUT.npz \
  --outdir OUTSIDE_GIT/linear-comparison
```

snapshot 由原 `tail_observe_prefix.py` 保存，生成矩阵和向量只在 scratch，不入库。
本次输出 summary SHA：`41cd08aa45cd778d579de06875264118062a817ee43f87dc116622d006603747`；原实际稀疏矩阵文件 SHA：
`1a5d118972b34eadc2c28a03efef4a05a7564e329e956047c3d62cfc9dd294ca`。

因子源码 SHA：`ad93895f46ca1acfca45a1e43245513d7d4bbedc43c3526c764584ffc2ce9bb5`；核对源码 SHA：`3dcac440fa61c6299a71d0bcd868800e743e1b36643a56b5c607ee634ef01bed`。
继续以实际更高模输入验证数值行为，再将它作为资源备用接到同一原 Newton 流程；不能用这次 M8 比较推出高模存在性或10%目标完成。
