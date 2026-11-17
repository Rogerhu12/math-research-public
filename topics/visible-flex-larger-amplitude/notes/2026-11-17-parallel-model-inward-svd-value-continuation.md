# 固定全谱 SVD 组合边界的首个实际值同伦校正

2026-11-17，Astra-larger-parallel-16f63c8b / constructive_model。

**实际数值证据；有限 BVP 接受，但未达到课题完成标准。** 从同一个真内向 `.997` 父出发，固定109个 $U^T$ 组合与原327项母向量，$\beta=63/64$ 的完整边值校正已经接受。完整 collocation RMS 为 $9.36885640066\times10^{-9}$，109个目标组合残差为 $4.31964454199\times10^{-12}$。独立同档 $C^2$ quintic 读出的实际 Gram 为 $2.70840323349\times10^{-6}$，仍超过 $10^{-6}$；这不是闭面或 reach 结果，也不是零目标边界的解。

## 1. 精确区分的新边界与不变的母输入

母父始终为 `parallel-inward0997-m112.json.gz`，SHA256：

```text
11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327
```

保持原 $M=112,N=2048$、区间 $[0,.997]$、全部338个投影 Frenet ODE、229个浅端行与原前三个 core 参数。标量剖面仍为同一个 `inward_scalar_profile`：cut `.995`、curvature `1.5`、两 ramp 各 `.02`、GL32；未更改 $a(s)$。高阶 core 仍是未知，因此不能说计算 $\phi$ 坐标下的 $\rho$ 逐字不变；公共材料坐标的完整对齐与加密收敛并未由本次有限试验给出。

令 $v(y)\in\mathbb R^{327}$ 依次包含未投影速度 R/T/Z 三分量在 $j=113,\ldots,221$ 的遗漏系数，R/Z 为余弦、T 为正弦。使用 [完整角导数与可达行源](../scripts/parallel_20261117_omitted_reachable_rows.py) 及 [固定 SVD 源](../scripts/parallel_20261117_omitted_svd_boundary.py) 在**原母父**上生成的薄矩阵 $U\in\mathbb R^{327\times109}$。本次109个右端方程为

$$
U^T v(y(.997))-\beta\,c_{\rm parent}=0,
\qquad c_{\rm parent}=U^T v(y_{\rm parent}),
\qquad \beta=63/64. \tag{1}
$$

$U$、原327项母值与109项 $c_{\rm parent}$ 全程固定；没有随 Newton 步重选行、重算 U 或把新场重定义成母父。使用 $U^T$，**不乘奇异值逆矩阵**，未以缩放指标代替目标残差。$\beta\ne0$ 时目标本身非零，因此组合函数值非零是预期行为。

[新 driver](2026-11-17-parallel-model-inward-svd-boundary-bvp.py) 复用已冻结 only-Z driver 的全部 ODE/Jacobian、浅端条件、QR 和 `feasible_newton`，只替换右函数与其固定目标。原 only-Z 零目标在1800点预算内失败，本次从原接受母父重新开始，未使用那个未接受终态作为初值。

## 2. 导数、真正全段校正与终态

初端109×338组合 Jacobian 的数值秩为109；最大/最小奇异值分别为134727.525489与 `.00794046564966`，原条件数 $1.69672071429\times10^7$。五个复步方向的最大相对误差 $2.02750276410\times10^{-15}$。真正启动时 (1) 的最大残差为 $1.21497025298\times10^{-6}$；这里不是把约 $7.78\times10^{-5}$ 的组合函数值误当成目标误差。

实际求解保持 `tol=1e-8, bc_tol=1e-11, max_nodes=1800`。510节点，1次外迭代；第一次完整 QR 的约化条件数为 $6.84932980167\times10^7$。接受三个 $\alpha=1$ 的 Newton 步，约44.923秒后成功，无需加节点。

| 终态量 | 实际结果 |
|---|---:|
| 完整 collocation RMS | $9.3688564006614\times10^{-9}$ |
| 109项组合对固定目标的最大残差 | $4.319644541989073\times10^{-12}$ |
| 109项组合函数值最大绝对值 | $.00007654312734257256$ |
| 全327项原始谱最大绝对值 | $.00010623419066030799$ |
| 原始R谱最大绝对值 | $.00010623419066030799$ |
| 原始T谱最大绝对值 | $.000015233317835459494$ |
| 原始Z谱最大绝对值 | $.00000782140745627725$ |
| 采样 core $\rho_{\min}$ | $.16601838127643642$ |
| 轴向 core gap | $.9599974531114652$ |

全部327项原谱单独留在最终输出中；不能把109项组合的残差当成所有遗漏速度已经消失。由于高阶 core 变化，原约 `.9600010` 的 gap 亦有微小变化，本场不能无条件继续使用 `.96` 作为严格下界。

## 3. 必要的实际 $C^2$ quintic 读出

使用冻结 `parallel_20261117_prefix_inward_readout.py`，`--angles 2048 --radial-subdivisions 4`，与原 principal/Schur 比较同档。覆盖509个 quintic 胞元，共5,212,160点；采用相同节点0/1/2 jets 定义实际 $C^2$ 曲面，没有用 ODE 残差代替几何读数。

得到实际相对 Gram 算子误差

$$
2.708403233489359\times10^{-6},
$$

最坏样本在 $s=.997$、$\phi=2.705942109830271$。实际最大主曲率采样为6.300458691196396，最小 Gram determinant采样 `.02756210292164792`，core $\rho$ 保持正。这些样本未暴露新域或曲率问题，支持继续有限值同伦；它们不是连续全域或 reach 证明。

反射前缀的原点球直径 proxy 为3.50901951865992，采样 witness 距离 `.9599974531114654`。由于仍是带边前缀，不能将该 proxy 或 witness 比值记作闭曲面的 $D$、$\delta_{\rm hold}/D$。

## 4. 冻结身份与完整命令

新 driver SHA256：

```text
397bbdd79f79a56db3062a97f8837ded0f4f0d247fa4b4e772353a0bd78b4e15
```

其复用的 only-Z 基础 driver 为 `d6b9f58cf75f2e9dc0aa6777263d901edd71f4e5216eff3bbe82c59c8782b4eb`；全过程没有修改它。

| 固定输入 | SHA256 |
|---|---|
| `parallel-inward0997-reachable-rows.json` | `295b6d9e54d9d23d6b3c6934f94d8d0b1e4c0849ac4bf0ea15a0ac04231c6a32` |
| `parallel-inward0997-svd-boundary.json` | `51df267686fe6b4336a9ba0c3252069956d93a180fe6a7fca7159bedd98e949a` |
| `parallel-inward0997-svd-boundary.arrays.npz` | `526ccc77a5fcd2cf77b7968c691617945820dc4ee6eb44fc3bfdd8192f9ebccb` |
| U 的 little-endian float64/C-order 字节 | `31afd5135a6f09fcc5b2efa501a2e7e87bf10f3675e8c44923b943b89a3003da` |

两个算子源分别为 `875969591ef9a73bc22ff0ddccf9ce1e900fd7b83a736188c93e8e6ff01d51ce`、`38d9a9924a452506135e9bd049e911bba98f59ba5b01e575415c40e39891de98`。driver核对上述母父、报告、数组、U字节、原母向量与源身份后才启动。运行前 definition（其中同时保存实际初始 probe）在仓库外 `parallel-model-inward-svd-b63of64.json.gz.solver.definition.json`，SHA256 `05ce2708bfe7adeaa4159d824cf5933c0d41ed7ba9e9c171a90ca93f0bd72418`。

从仓库根执行本次已完成命令：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-inward-svd-boundary-bvp.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-inward0997-m112.json.gz \
  --target-parent /workspace/scratch/16f63c8bce6b/parallel-inward0997-m112.json.gz \
  --row-report /workspace/scratch/16f63c8bce6b/parallel-inward0997-reachable-rows.json \
  --svd-report /workspace/scratch/16f63c8bce6b/parallel-inward0997-svd-boundary.json \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-inward-svd-b63of64.json.gz \
  --beta .984375 --tol 1e-8 --max-nodes 1800

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_inward_readout.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-model-inward-svd-b63of64.json.gz \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-inward-svd-b63of64-readout.json \
  --angles 2048 --radial-subdivisions 4
```

最终 BVP 文件 SHA256 为 `ed429833dc450bd821fcf868a7e84a800b4ec8b9cfce84181cbc7a9cab667aaf`，实际读出报告为 `8797c243e74bf447187c994588465542baf7a438401f6527936607a3eadd83e1`。基础 driver 另生成的 `.solver.gz` 是内部临时输出；其尚未改写的旧边界标签与数值不得冒充上述最终文件。wrapper最终明确绑定固定SVD定义，并重新报告真正目标残差。所有可再生 raw 都只保留在仓库外。

### 首步大小的设计动机

[已冻端点 predictor](../scripts/parallel_20261117_svd_endpoint_predictor.py)（SHA256 `fa1f0dc0b92bb8bb7e93442ba258b8864cf36a2af36a83cc9f8922848f5eda87`）曾对同母父作孤立端点的 $1/64$ 最小二乘步，组合非线性余项约 $8.48\times10^{-9}$、端点 $\min H/W$ 约 `.6145`。它只用于选择首个目标步长，没有验证内部 ODE 或内部域。本次真正初猜仍是原接受父的完整510节点场；上述三步全段 Newton 校正与实际 quintic 读出才是本条新增的数值结果。
