# R639：固定弧长规范化的纯右 er/fr 接口与真父可达空间的一次零目标诊断

**实际有限结论。** 固定 β=.75 真接受父 `852a673f...` 和构造角数2048，规范化后的径向/混合 Gram 函数可作为只依赖右端状态的有限函数，不需要丢掉左端材料密度导数或增加447态。完整1024×338端点 Jacobian 已实际建立；再从该真父重新运输全部338 ODE、229浅端条件的109维空间后，所选零目标线性校正仍需很大的端点改动。有限端点试值不支持直接发起这个零目标 BVP，故本次诊断到此停止。它不证明此类边界或真实等距问题不可解。

## 1. 为什么这个规范化接口仍是纯右边界

采用已冻结弧长规范化定义（reader SHA `0ad4400b648cfd2937b58c59a811c3a2cdb30af68e3b3c3e261091e097dbdaf2`）。记当前圈切向量为 $t=F_\phi$，构造节点速度 $q=\sqrt{t\cdot t}$，$q_N$ 是固定2048点实三角插值；$b=\operatorname{mean}q_N$，$\lambda=a/b$，$c=(0,0,z_0)$。角重参数由

$$
\int_0^{\psi(s,\theta)}q_N(s,\phi)\,d\phi
=b(s)\int_0^\theta\rho(\eta)\,d\eta
$$

定义，曲面为 $\widehat F=c+\lambda(F(s,\psi)-c)$。用同一有限投影 Frenet RHS 计算 $F_s$、$F_{s\phi}$、$c_s$，并完整保留 $\lambda_s$ 和 $\psi_s$。在源角 $\phi$ 评价时，

$$
W=\widehat F_s=\lambda F_s+(1-\lambda)c_s
+\lambda_s(F-c)+\lambda F_\phi\psi_s,
\qquad
\widehat F_\theta=a\rho(\theta)\frac{F_\phi}{q_N}.
$$

所以相对 Gram 槽为

$$
e=W\cdot W-1,\qquad
f=\frac{W\cdot F_\phi}{q_N},\qquad
g=\frac{|F_\phi|^2}{q_N^2}-1.
$$

这些表达式在源角位置不含左端 $\rho$；左端变化只改变该源角对应的材料角标签。因此这里的 $e,f$ 有限函数可以保留原338 ODE/229浅行的纯分离结构。它不同于直接使用未规范化的 $|F_\phi|^2/(a\rho(y_a))^2-1$，后者必须保留左端耦合。

本探针保留构造网格上全部有限对称槽：$e$ 的偶频余弦含均值和Nyquist共513项，$f$ 的偶频正弦共511项，合计1024项。采用 Parseval 正交权；不是从其中预先截取109项。构造节点上 $q_N=q$，但加密角度的 $g$ 误差仍须由原固定field读者实际支付。

## 2. 全部端点方向与旧母空间的有限预测

源 `parallel-model-retracted-gram-endpoint-probe.py` SHA：

`c8f1916682e8837568d7a3dfd2f0fccf46e1def68213a564a6211b52467753c0`。

实际对全部338状态方向使用步长 `1e-28` 的复步导数（FFT实算子按实/虚部复线性延拓，速度使用 $\sqrt{t\cdot t}$）。5个独立组合方向与完整矩阵乘积的相对无穷误差最大 `3.3947544382307734e-14`；一个中心差分方向在步长 `1e-8`、`2e-9` 的相对误差分别为 `1.10065e-5`、`4.40261e-7`。有限投影 RHS 与真父 saved RHS 的差为0。初始规范化 Gram 为 `6.393033356856169e-7`，$\|(e,f)\|_{L^2}=2.525044307873692e-7$，吻合同一field已有端点读出。

第一次只把这个真端点 Jacobian 乘原11960350母父的旧运输空间。它明确只是冻结预测，不是 β=.75 真父全段导数：约化秩109、条件数 `1.4092989e7`，零目标端点修正无穷范数 `.0140483461`，线性 range 外余量占原 $L^2$ 的 `.16477493`。这不足以支持新求解，故随后只重算一次真父空间。

## 3. 真852a父全段空间与有限小步结果

使用冻结 `scripts/parallel_20261117_omitted_reachable_rows.py`，在真852a父全部509胞上重新运输109维空间；全部338 ODE与229浅行保留，实际耗时19.980秒。该父线性化的collocation余项为 `1.4568538018932617e-14`，逐胞运输相对误差最大 `4.402884448248575e-15`，正交误差 `4.9960036108132044e-15`。旧/新空间最小主夹角余弦 `.9910854247636323`，不能把两者当成同一导数。

对真父空间 $Z$，令 $A=J_{e,f}Z$。其数值秩仍为109，最大/最小奇异值分别为 `2.8182938654312224`、`1.3889449483539e-7`，条件数 `2.029089683e7`。全秩最小二乘零目标校正给出

$$
\|\delta y\|_\infty=.02228780251251383,
\qquad\|\delta y\|_2=.04915095421513209.
$$

线性 range 外余量无穷范数 `1.6591344545323468e-8`，其 $L^2$ 占比 `.16143572839356013`。直接评价有限端点 $y-\alpha\delta y$ 得：

| α | 实际规范化 Gram | $\min H/W$ | 该端点 $(e,f)$ 系数 $L^2$ |
|---:|---:|---:|---:|
| 1 | `.0729967257347` | `.1678019972` | `.01003508752` |
| 1/4 | `6.3035517992e-5` | `.5061334042` | `1.566034183e-5` |
| 1/16 | `3.9144804542e-6` | `.6017904210` | `1.021958840e-6` |
| 1/64 | `6.1687968403e-7` | `.6146815067` | `2.568949117e-7` |

最小试步的无穷 Gram 略降，但 $L^2$ 已比原 `2.525044308e-7` 略升；其余所测步长明显变坏。上述点均未重新求解内部ODE/浅端条件，不能称为新接受场。按本次预先限定的诊断范围，不扩大步长扫描、不据此建立新的零目标 BVP。

## 4. 复现链与仓库外数据身份

两个新增源码均冻结；第二个辅助源 `parallel-model-retracted-gram-current-range.py` SHA为 `0f8636e9c7d0806c14309a913206b93ba34f14f0b3742e33a3c819b530f16a91`。以下保留原实际命令（工作目录为仓库根）。两脚本已逐字存为[端点源](../scripts/parallel_20261117_retracted_gram_endpoint_probe.py)与[真父响应源](../scripts/parallel_20261117_retracted_gram_current_range.py)；复现时把同名scratch脚本路径替换为这两条仓库路径，reference-reader使用已刊[固定规范化源](../scripts/parallel_20261117_prefix_arclength_readout.py)，字节身份保持。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  /workspace/scratch/16f63c8bce6b/parallel-model-retracted-gram-endpoint-probe.py \
  --scripts topics/visible-flex-larger-amplitude/scripts \
  --input /workspace/scratch/16f63c8bce6b/parallel-model-inward-svd-b075.json.gz \
  --reference-reader /workspace/scratch/16f63c8bce6b/parallel-prefix-arclength-readout.py \
  --reference-reader-sha 0ad4400b648cfd2937b58c59a811c3a2cdb30af68e3b3c3e261091e097dbdaf2 \
  --old-transfer-report /workspace/scratch/16f63c8bce6b/parallel-inward0997-reachable-rows.json \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-b075-retracted-gram-oldZ-probe.json

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_omitted_reachable_rows.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-model-inward-svd-b075.json.gz \
  --input-sha256 852a673f4464090f003fd44c3247a819cf9bae0418d07caf97f8edb0e3d39471 \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-inward-b075-reachable-rows.json

PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  /workspace/scratch/16f63c8bce6b/parallel-model-retracted-gram-current-range.py \
  --scripts topics/visible-flex-larger-amplitude/scripts \
  --input /workspace/scratch/16f63c8bce6b/parallel-model-inward-svd-b075.json.gz \
  --probe-module /workspace/scratch/16f63c8bce6b/parallel-model-retracted-gram-endpoint-probe.py \
  --probe-report /workspace/scratch/16f63c8bce6b/parallel-model-b075-retracted-gram-oldZ-probe.json \
  --transfer-report /workspace/scratch/16f63c8bce6b/parallel-model-inward-b075-reachable-rows.json \
  --out /workspace/scratch/16f63c8bce6b/parallel-model-b075-retracted-gram-currentZ-probe.json
```

输出仅在仓库外保存：

| 文件 | SHA256 |
|---|---|
| `parallel-model-b075-retracted-gram-oldZ-probe.json` | `8b05f8b49eac291af3835e25ed31da18884f91991f3341e430fdefa8e1108f1c` |
| 同名前缀 `.arrays.npz` | `e2e45b45757ccf4fdf375c5f0856f302837c0e28c29b6e4728d97f06ecd675f1` |
| `parallel-model-inward-b075-reachable-rows.json` | `b06454448e0d08469f69790695ac7f905071f8177625a3576136cdac6e5bff54` |
| 同名前缀 `.arrays.npz` | `7d53abbc3fe302a0beb957cc68974761840cbafdbbf4fba4c5a6d9c113ff2691` |
| `parallel-model-b075-retracted-gram-currentZ-probe.json` | `3362c194209e909d482658bfe491e2da956169e7aa7c52ef191bdb7273e9a47d` |
| 同名前缀 `.arrays.npz` | `ce7c5e8a02641f925a613ee861ff47b05b3148286c0c72a4f7edff2119c32fd9` |

全部限制：这是一个真父上的有限 Jacobian/可达方向诊断，没有新的BVP接受、全段修改、闭面、reach或完成标准结论。
