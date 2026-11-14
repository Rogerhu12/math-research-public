# 已恢复 δ₄ 前腿的平均横截尺度

这里只读取已经逐字恢复的旧浮点结果，没有重跑 ODE，也没有给 δ₅ 或连续角带
提供新证书。用途是判断 R82 有符号参数积分需要的精度。

对象为准确仿射 δ₄（不是 δ₅），初值为旧 H₄ 的 1032 个均匀标签节点。
固定 H₄ 后，读取前腿已经包含移动端点项的 `final_parameter_column`，计算

\[
 w_j=\frac{4\,\texttt{final\_parameter\_column}_j}{H_4'(x_j+d)},
 \qquad d=\pi(15121+\sqrt5)/27422.
\]

浮点结果：平均 $0.00115358570874243$，节点范围
$[-0.0011976849566174713,\ 0.0025539905290892953]$。
归一化参数列本身的范围为
$[-0.0009486353880371484,\ 0.0040091997585618095]$。
旧全返回加权平均为 $0.002307171417490598$，两倍前腿平均减去此值为
$-5.738031577662284\cdot10^{-15}$。

因此浮点候选显示平均为正而点值变号，实际认证必须保留有符号平均。
$10^{-4}$ 量级的真正平均误差可能已经足以定号；这只帮助选择算法，不是误差门已过。
1032 点离散平均、有限 primitive、δ₄→δ₅ 参数移动和整个复带的费用均未在此支付。
R77 的准确平方恒等式不使这些有限节点变成严格真流输入。

输入 SHA256：

- `data/phase_ring_continuation/exact_affine_step4_shared_knot_dense1032/block_0000_forward.trace.json`：`ae87a30544996fc14f8590c0397174b569e1c2f50bcb4f8396fe3411a39cb042`。
- `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_dyadic_H.json`：`8bd6078f8c442b48bab2b15850b99e2455d616ab48e687abb22114a1f1bfe39b`。
- `notes/2026-11-12-D5-exact-affine-step4-shared-knot-Hnodes1032.json`：`4ef35b2a2eb3320a67b9a777859feeffb8448057c97c5e5e2053fbf86e156d01`。

从课题目录重读已有结果：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python - <<'PY'
import json, hashlib
from pathlib import Path
import numpy as np
base = Path('data/phase_ring_continuation')
trace = base/'exact_affine_step4_shared_knot_dense1032/block_0000_forward.trace.json'
hp = base/'type_fixed_step02_d5_exact_affine_step4_dyadic_H.json'
d = json.loads(trace.read_text())
H = json.loads(hp.read_text())
assert hashlib.sha256(hp.read_bytes()).hexdigest() == d['identity']['dyadic_conjugacy_sha256']
den = 2**H['denominator_power_of_two']
c = np.array([complex(int(r)/den, int(i)/den)
              for r, i in H['h_nonnegative_integer_coefficients']])
x = 2*np.pi*np.arange(len(d['initial_angles']))/len(d['initial_angles'])
k = np.arange(len(c))
shift = np.pi*(15121+np.sqrt(5))/27422
sp = 1+2*np.real(np.exp(1j*np.outer(x+shift, k[1:]))@(1j*k[1:]*c[1:]))
column = 4*np.array(d['final_parameter_column'])
w = column/sp
old = json.loads(Path('notes/2026-11-12-D5-exact-affine-step4-shared-knot-Hnodes1032.json').read_text())
print({'floating_delta4_only': True, 'mean': float(w.mean()),
       'range': [float(w.min()), float(w.max())],
       'twice_half_minus_old_full': float(2*w.mean()-old['sampled_weighted_twist_mean'])})
PY
```

若大轨迹目录已丢失，先按 HANDOFF 的真实恢复命令重建并核对历史 SHA，
不能伪造 `.trace.json` 来满足这里的输入身份。
