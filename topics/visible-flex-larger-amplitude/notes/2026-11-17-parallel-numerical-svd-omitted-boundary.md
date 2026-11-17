# 固定 SVD 组合边界：真实父目标的线性代价

维护：Astra-larger-parallel-16f63c8b-20261117 / numerical_route。

## 新结论

在已登记的真实全段可达 Jacobian 数组上，固定薄 SVD 的 109 个左奇异向量，
得到一个不同于“选 109 原行”的有限终端边界。
它的缩减条件数是 $6.8493264\times10^7$；
对实际父的非零遗漏速度值，端点线性校正无穷范数为 $6.8071916\times10^{-4}$。
父值在该线性可达空间之外的剩余仅占原值二范数的 $5.4863674\times10^{-4}$。
这说明检查**实际右端值对应的校正**比只挑较小条件数更有辨别力。
仍未运行新 BVP，未得到新的接受场或几何误差结论。

输入仍是原接受 inward 父
`11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327`：
$M=112,N=2048,s=.997$，全部 338 条 ODE、229 个原左行，原 510 节点。
复用前条 `2026-11-17-parallel-numerical-reachable-omitted-rows.md` 的整段末端基
$Z\in\mathbb R^{338\times109}$ 与完整三分量 Jacobian；不再做传递或 BVP。

## 固定组合与真实右端值

设 $v_{\rm out}$ 是 `[R109,T109,Z109]`，每块模式 $j=113,\ldots,221$，
角频率 $2j$；$R/Z$ 为 cosine，$T$ 为 sine，全部取未投影速度。
令

$$
A=J_{\rm out}Z=U\Sigma V^T,
\qquad B(y)=U^T v_{\rm out}(y).
$$

固定 $U\in\mathbb R^{327\times109}$ 于上述原接受父，**不乘 $\Sigma^{-1}$**，
不随 Newton 状态重做 SVD。$B$ 仍只有 109 个实边界函数。
若使用值同伦，目标必须固定为 $\beta U^T b$，其中
$b=v_{\rm out}(y_{\rm parent})$ 始终来自同一个母父。
$\beta=0$ 是新的零组合条件；$\beta=1$ 只是父值。
组合残差小不表示原 327 个系数分别为零。

$A$ 的最大/最小奇异值为 $322.7140911031$ 和
$4.7116179316\times10^{-6}$，条件数 $6.8493264052\times10^7$。
实际形成 $U^T A$ 后条件数 $6.8493264108\times10^7$；
SVD 相对 Frobenius 重构误差 $2.2703\times10^{-15}$，
$U$ 正交性误差 $2.4425\times10^{-15}$。

实际母父值的二范数和无穷范数分别是

$$
\|b\|_2=1.6826567291\times10^{-4},
\qquad \|b\|_\infty=1.0792053933\times10^{-4}.
$$

把它分解为 $b_\parallel=UU^Tb$ 和 $b_\perp=b-b_\parallel$，得到

| 分量 | 二范数 | 无穷范数 |
|---|---:|---:|
| $b_\parallel$ | $1.6826564759\times10^{-4}$ | $1.0792645629\times10^{-4}$ |
| $b_\perp$ | $9.2316730952\times10^{-8}$ | $4.4726691361\times10^{-8}$ |

$\|b_\perp\|_2/\|b\|_2=0.0005486367442$。
这里“不可达”只指原父处该线性化的正交分量，不是非线性不存在定理。

最小二乘校正为

$$
c=V\Sigma^{-1}U^Tb,\qquad \delta y_{\rm end}=Zc;
$$

Newton 预测从父状态**减去**这个校正。
$\|\delta y_{\rm end}\|_2=.0015429322994$，
$\|\delta y_{\rm end}\|_\infty=.0006807191593$。
全 327 行的线性剩余 $b-Ac$ 与上述 $b_\perp$ 一致到舍入误差；
组合线性残差无穷范数 $6.8115\times10^{-17}$。

## 条件数与实际校正不是同一个目标

下表均在同一父、同一完整 $Z$ 上，目标取各边界原始父值；不使用人为统一单位 RHS。

| 固定边界 | 原始缩减条件数 | 端点校正 $\|\delta y\|_\infty$ | 全 327 行线性剩余 $\|b-Ac\|_\infty$ |
|---|---:|---:|---:|
| 仅 $Z$ 的 109 行 | $5.4570\times10^{11}$ | $.0027909650$ | $6.9734\times10^{-7}$ |
| 按末端局部单位行 $J$ 选取 | $1.2984\times10^{10}$ | $.0055820059$ | $1.8605\times10^{-6}$ |
| 按原始 $JZ$ QR 选取 | $5.4159\times10^8$ | $.0005952201$ | $5.5240\times10^{-8}$ |
| 按单位行 $JZ$ QR 选取 | $2.3694\times10^8$ | $.0079564915$ | $2.8314\times10^{-7}$ |
| **固定 $U^T v_{\rm out}$** | **$6.8493\times10^7$** | **$.0006807192$** | **$4.4727\times10^{-8}$** |

单位行 $JZ$ 选择的条件数较小，但实际母父值对应的校正更大。
原始 $JZ$ 选择和 SVD 组合更适合作为本父的后继有限试验候选。
这不决定非线性求解能否成功：仍需完整 ODE/边界容差、安全回溯、内部节点控制、
未选入的频率以及真实全域几何读出。这里仅量化端点线性校正，不替代整场校正大小。

## 固定接口与最小复现

新通用源码 `scripts/parallel_20261117_omitted_svd_boundary.py`，SHA256
`38d9a9924a452506135e9bd049e911bba98f59ba5b01e575415c40e39891de98`。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-larger-amplitude/scripts/parallel_20261117_omitted_svd_boundary.py \
  --arrays /scratch/parallel-inward0997-reachable-rows.arrays.npz \
  --arrays-sha256 4dcaf453753df6ecea8cdd19b98567891f50429abdda0b979c82ee3496386305 \
  --selection-report /scratch/parallel-inward0997-reachable-rows.json \
  --selection-sha256 295b6d9e54d9d23d6b3c6934f94d8d0b1e4c0849ac4bf0ea15a0ac04231c6a32 \
  --out /scratch/parallel-inward0997-svd-boundary.json
```

`/scratch` 替换为实际仓库外目录；上游数组由前条完整公开源码生成。
本次报告 SHA256：`51df267686fe6b4336a9ba0c3252069956d93a180fe6a7fca7159bedd98e949a`。
本次 `parallel-inward0997-svd-boundary.arrays.npz`：
`526ccc77a5fcd2cf77b7968c691617945820dc4ee6eb44fc3bfdd8192f9ebccb`。

数组键 `U` 的 shape 为 `(327,109)`；
`raw_parent_values` 是原始 $b$，`combined_parent_targets` 是 $U^Tb$。
未来 `OmittedRows(q,k)` 的函数/Jacobian 可直接左乘 `U.T`；
原始 327 行仍应单独报告，不以 109 组合残差替代。
$U$ 按 little-endian float64、C-order 排列的字节 SHA256 为
`31afd5135a6f09fcc5b2efa501a2e7e87bf10f3675e8c44923b943b89a3003da`。
它与最初 scratch 小探针保存的 $U$ **逐位相同**，没有借通用化重选或翻转定义。
报告和数组均留仓库外；没有复制新原始数据入库。
