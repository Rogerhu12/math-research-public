# 冻结目标度量后的真实主曲率约束试验

日期：2026-11-14。公开本题数据与独立微分几何推导。

**结论：已实现并实际运行真实 shape operator 罚项。原最佳场的曲率可以降低，但本轮每个降低都伴随显著的固定目标度量误差；没有得到通过等距和曲率门的场。** 这些结论只针对当前 $b=.9$ 母线和该有限初值，不排除有内部特征圆/回折的其他几何设计。

新增独立脚本 `../scripts/eccentric_curvature_search.py`，复用原 Cartesian trial space，未修改 `eccentric_collar_search.py`。全程保持 14 个径向控制点、6 阶 Fourier、312 个未知量；两端开圆领、偏心 $e=.02$、完整边界二阶 jet 和物理尺度保持原设置。

## 1. 这次冻结的目标是什么

源文件是 `eccentric-search-design-002-curvature-seed.json`。对源场 $X_*$ 定义

\[
\bar g(s)=\begin{pmatrix}
\langle X_{*,s}\cdot X_{*,s}\rangle&\langle X_{*,s}\cdot X_{*,u}\rangle\\
\langle X_{*,s}\cdot X_{*,u}\rangle&\langle X_{*,u}\cdot X_{*,u}\rangle
\end{pmatrix}.
\]

角括号是整个材料圆的平均。源场最高 Fourier 阶为 $M=6$，二次乘积阶至多 $12$，故 $2M+1=13$ 个均匀角点按三角正交性准确取平均，浮点舍入另论。整条径向函数由同一源系数和同一母线公式定义；不是对每次迭代重新取平均或重新拟合。

令 $W(s)\bar g(s)W(s)^T=I$。优化中的度量残差始终为

\[
\big((Wg_XW^T-I)_{11},\sqrt2(Wg_XW^T-I)_{12},(Wg_XW^T-I)_{22}\big).
\]

这保证目标固定，也处理可能非零的 $\bar F$。优化本身是软最小二乘，输出场仍可能伸缩；所以 **“固定目标”不等于“已得到固定度量等距族”**。各 JSON 记录源文件 SHA-256，并明确 `fixed_metric_refinement_demonstrated=false`。

## 2. 罚项用的是实际主曲率

记

\[
A=X_s,\ B=X_u,\ U=X_{ss},\ V=X_{su},\ Z=X_{uu},\quad
\nu=\frac{A\times B}{|A\times B|}.
\]

实际第一基本形式为 $E=A^2,F=A\cdot B,G=B^2$，第二基本形式为 $l=\nu\cdot U,m=\nu\cdot V,n=\nu\cdot Z$。令 $d=EG-F^2=|A\times B|^2$，则

\[
H=\frac{Gl+En-2Fm}{2d},\qquad
K=\frac{ln-m^2}{d},\qquad
Q=4H^2-2K=\kappa_1^2+\kappa_2^2.
\]

增加的残差是

\[
r_\kappa=\lambda\max\!\left(\frac{\sqrt Q}{12}-1,0\right).
\]

$\sqrt Q\le12$ 足以推出两个实际主曲率的绝对值都不超过 $12$；但这里它仍是有限节点上的软约束。所有归一化均使用**当前场的实际 $g_X$、单位法向和第二基本形式**，没有用未归一的二阶导数或冻结目标 $\bar g$ 代替实际 shape operator。

### 解析 Jacobian

对 $Q$ 先作微分：

\[
dQ=\frac{4H\,d(Gl+En-2Fm)-2\,d(ln-m^2)+(2K-8H^2)\,d(EG-F^2)}{d}.
\]

法向的变化准确为

\[
d\nu=\frac{I-\nu\nu^T}{|A\times B|}
       (dA\times B+A\times dB).
\]

再把它代入 $dl=d\nu\cdot U+\nu\cdot dU$ 及 $dm,dn$，得到对五个位置 jet 的梯度，最后链到 Cartesian B 样条/Fourier 系数。活动罚项乘 $\lambda/(24\sqrt Q)$；非活动罚项取零导数。实际浸入退化时拒绝评估，不把被正则化的法向当真曲率。

两随机方向的中心差分检查中，单独曲率部分 Jacobian 的相对误差分别为 $1.53\cdot10^{-9}$ 和 $5.18\cdot10^{-9}$；整个残差分别为 $1.47\cdot10^{-9}$ 和 $4.84\cdot10^{-9}$。这只验证实现的一致性，不是连续数学误差界。

## 3. 实际权重试验

源场的密审计使用 4097×128；优化后的各场独立检查使用 1025×96。第一小试配置为每段 6 个 Gauss 点、24 个角点；其余为每段 10 个 Gauss 点、32 个角点。最后一行从 $\lambda=1$ 输出续算；其余均从原源场出发。这不是经全局最优化认证的 Pareto 前沿。

| 数据文件（本目录） | 权重 $\lambda$ | 函数评估 | 固定目标相对算子误差最大值 | 实际 $\max|\kappa_i|$ 采样值 | shape Frobenius 采样最大值 |
|---|---:|---:|---:|---:|---:|
| `eccentric-curvature-target-intrinsic-audit.json` | 0，仅审计 | 0 | .0003348939 | 75.0416 | 75.0451 |
| `eccentric-curvature-fixed-w001-small.json` | .01 | 6 | .0023924874 | 74.6707 | 74.6742 |
| `eccentric-curvature-fixed-w01.json` | .1 | 25 | .1480662607 | 59.3307 | 59.3357 |
| `eccentric-curvature-fixed-w1.json` | 1 | 70 | .5715192476 | 17.9036 | 17.9234 |
| `eccentric-curvature-fixed-w10.json` | 10 | 50 | .5386365316 | 13.4995 | 13.5254 |

因此曲率改善是真实的几何变化，但同时产生了不可接受的目标度量误差。最强权重的场仍未达到 true $|\kappa|\le13$：配置点的 Frobenius 最大值约 $12.0477$，密采样却得到 $13.5254$，再次表明不能把配置点达标当作全域曲率上界。

最强权重的横向跨度至少 $2.54407$；用该跨度和采样主曲率作必要尺度检查，$1/(D_{\rm lower}\kappa_{\rm sample})\approx.02912$，仍不足以支持 reach/D=.03，更没有检查全局点对距离。所有这些输出都未证明嵌入、未闭帽、未建立 reach 下界，也没有足够的等距精度。

## 4. 冻结目标的内禀曲率是否先把上限排除了

令

\[
h=\bar E-\bar F^2/\bar G,\qquad r=\sqrt{\bar G}.
\]

去掉径向角 gauge 并以 $d\tau=\sqrt h\,ds$ 回参，可直接得到

\[
K_{\bar g}=-\frac1r\left(\frac{r''}{h}-\frac{r'h'}{2h^2}\right).
\]

脚本用源场一、二阶 jet 求 $\bar E',\bar F',\bar G',\bar G''$；$X_{ssu}$ 只通过准确的有限 Fourier 角微分取得，没有径向有限差分，也没有引入第三径向导数。

4097 个径向点的结果为

\[
K_{\bar g}\in[-1.11297443,55.70343851],\qquad
\sqrt{\max|K_{\bar g}|}\approx7.46347,\qquad
\sqrt{2\max|K_{\bar g}|}\approx10.55495.
\]

对真正的等距浸入，$|\kappa_1\kappa_2|=|K_{\bar g}|$，所以这些是主曲率及 Frobenius 的必要下界诊断。它们没有排除 Frobenius 上限 $12$；数值上却已使上限 $10$ 不相容。由于尚未包住舍入和连续区间误差，这里没有把有限采样提升为严格不存在定理。

## 5. 复现

从仓库根运行，例如 $\lambda=.1$：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-new-mechanism/scripts/eccentric_curvature_search.py \
  --source topics/visible-flex-new-mechanism/notes/eccentric-search-design-002-curvature-seed.json \
  --limit 12 --weight .1 --radial-order 10 --angles 32 --max-nfev 70 \
  --out topics/visible-flex-new-mechanism/notes/eccentric-curvature-fixed-w01.json
```

$\lambda=1$ 仅改变 `--weight` 和输出名。$\lambda=10$ 另传 `--resume .../eccentric-curvature-fixed-w1.json --max-nfev 50`，仍指定同一个 `--source`。密审计用 `--weight 0 --audit-only --angles 64 --audit-radials 4097`。首轮 Jacobian 检查加 `--jacobian-check`。

本轮因此完成了一个明确的失败搜索改进：原先被遗漏的真实曲率被纳入目标、独立复核，并与固定目标度量误差逐项分开。继续改变母线、加入内部回折或更换初值属于新的几何设计；不能把本表解释为全部偏心 bearing 机制的失败。
