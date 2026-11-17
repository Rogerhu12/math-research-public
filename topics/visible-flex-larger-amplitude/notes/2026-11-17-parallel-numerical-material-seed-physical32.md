# 材料初猜经完整重解得到物理 M32 非零尾

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。本条在已登记 [best4 短桥背景](2026-11-17-parallel-numerical-best4-tail-continuation.md) 上，实际接受了物理 M32/N1024、lambda=1e-4 的完整加权 BVP。此前物理 M8/N512 在同幅度的直接尝试失败，不能据此推断这个背景的完整非线性数学上界。

## 初猜和目标严格区分

新的 [weighted_tail_seed.py](../scripts/parallel_20261117_weighted_tail_seed.py) 保留完整物理 BVP，将 `--material-input` 只作为明确的未接受初猜入口。真实角度关系是

\[
\theta(\varphi)=\varphi+
\sum_{j=1}^{112}\frac{\rho_j}{2j}\sin(2j\varphi),\qquad
\widetilde P=\rho(\varphi)P(\theta(\varphi)).
\]

在目标角网对材料 sine/cosine 展开作字面投影。K 的物理均值重新按 phi 平均，不能直接沿用材料 K 均值。这是一个线性初猜变换，既不伪造 `success=true` 的物理父，也不把投影后的场当作接受解。

随后完整重解所有 `2M+1=65` 个状态行。目标仍为原物理 trace 的前32个 Dirichlet 系数、同一个固定背景、完整112项 rho、实际同源广义角频率 far 列，以及字面 weighted mean。非均值 K 在浅端读出而不额外钉住；phi 高度 anchor 仍为 `.9703876955889461`。

M8 到 M32 时保留空间、采样均值与有限广义角谱也相应改变。因此这是同 g 下更高阶的完整有限问题，不是完全同一个有限矩阵的纯求解器比较，更不是已经证明向无限问题收敛。

## 实际接受结果

初猜来自材料 lambda=1e-4 接受场 `parallel-best4-material-scale1e4.json.gz`，SHA

```text
53f16fabdcf1ed7e9555ed2a946f2e2c1c1bdf006ba633a1ef3f9716af9ecbd2
```

物理 BVP 在5轮、4594节点、93.31秒后接受。始终保留 S,D,L,N 正性；此接受场的 y 也仍正。

| 量 | 实际值 |
|---|---:|
| source-index collocation RMS | 9.988768630813888e-7 |
| BC 最大值 | 1.9109063290057016e-18 |
| sampled weighted mean 漂移 | 3.9233196905000614e-12 |
| sampled min D | .9997424424777003 |
| sampled min L | .9398888318104633 |
| sampled min y | .9461587788762995 |
| sampled max abs P | .013287471660835645 |
| sampled max abs K | .05384122112370049 |
| 浅端 K sampled mismatch | 3.376631638841168e-5 |
| 实际 physical-r 完整 K 方程余项 max | 4.54350761163216 |

最后两行完整保留：没有完成 prefix-tail jet 接合，也不能把 collocation 接受替代真实 Cartesian Gram。K 比较参考的均值规范限制已在 best4 note 说明。几何径向积分读出、N 加密与进一步 lambda 延拓另行处理。

新输出 `parallel-best4-weighted-m32-scale1e4.json.gz` 的 SHA256：

```text
47c4f2838c24c319717d7493417ef1424fa49675bcce9ec720bef1f8d3a59bed
```

## 全部身份与复现

背景 SHA `487373a8445674658cb36ddbd20445e774612269720f58c0e6db492f38c24e15`，物理 trace SHA `36688dcba2bacef79d497b92a118b58141447f2630a9c735e75a63cf4aab719b`。实际 M32 深列从相同 scalar source、far32、depth4、每源段512步得到，SHA `fa6c65a363f7fc973c2fe1fef871e9f9c3de701381af2a0f42cbda1aa8a39434`。频率不作小数截断，直接由本次完整 generalized eigensystem 传入：

```python
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, 'topics/visible-flex-larger-amplitude/scripts')
from parallel_20261117_dynamic_tail import Background
from parallel_20261117_weighted_tail import WeightedMean, weak_deep_boundary
r = Path('/workspace/scratch/16f63c8bce6b')
bg = Background(r/'parallel-best4-background.json')
trace = json.loads((r/'parallel-trace0992-physical-m112.json').read_text())
q = WeightedMean(32, 1024, trace['rho_cos_coefficients'])
frequencies = weak_deep_boundary(q, bg)[2]['frequencies']
subprocess.run([
    'node', 'topics/visible-flex-larger-amplitude/notes/'
            '2026-11-17-parallel-model-calibrate-tail.mjs',
    '--source', str(r/'parallel-tail-source'),
    '--input', str(r/'parallel-best4-background.json'),
    '--out', str(r/'parallel-best4-physical-m32-columns.json'),
    '--depth', '4', '--steps', '512', '--far', '32',
    '--modes', json.dumps(frequencies)], check=True)
```

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_weighted_tail_seed.py \
  --background /workspace/scratch/16f63c8bce6b/parallel-best4-background.json \
  --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-physical-m112.json \
  --deep-columns /workspace/scratch/16f63c8bce6b/parallel-best4-physical-m32-columns.json \
  --material-input /workspace/scratch/16f63c8bce6b/parallel-best4-material-scale1e4.json.gz \
  --modes 32 --angles 1024 --scale 1e-4 --fast-jacobian --allow-height-turn \
  --tol 1e-6 --max-nodes 14000 --batch 32 \
  --out /workspace/scratch/16f63c8bce6b/parallel-best4-weighted-m32-scale1e4.json.gz
```

seed runner SHA `c96d340f5ddb520a71e521de62ed1bce21cc16d1098f9d2a1e2c250c33ac00d0`。其完整依赖版本分别为 dynamic `e21034c9f1208506d16f1bed3cc46c470fdf15425c6466eb0f9623ad0fcfa8b5`、weighted `89c8d13add0d1930581269fde33e577804bc333afcf986a0837dfbae07f44c4d`、fast `6443424ecc791fe26c453935747d2fbd81d3df8528c0d4dda21f46ac6f890330`、fresh-J helper `8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae`；far 传播源仍为已刊的 `9f2b98321e22ca71ab343de9f8aa01bee68beaee1d731705a156ed6664618f8f`。参数配置、背景重建与来源恢复按 best4 note；重建后所有深列和 BVP 必须引用同一重建背景 hash。raw 只在仓库外。
