# 普通段的相关曲率门及完整时间尾优化

本包解决 forward 4 原 R6 扩域中的两个具体数值障碍，仍使用同一准确 δ5 几何、
同一参考时间尺度和各自真实 common span 的解析 germ。旧 R3 sampler 的点值预算不变。
没有新增全角时间 jet 网格。

## 1. 曲率保留时间相关性

设 r(u)=t sin(τ_c+h u)。旧直接复径向盒包住 r(|u|≤6) 后也包含根外的实点，
使 Re(−K)>0 的粗区间门失败；这不代表真实时间盘存在曲率零点。
`fourfold_ordinary_curvature_time_gate.py` 从同一准确实中心 r(0) 提取真实径向 K Taylor 球，
然后用常项准确为零的 r(u)−r(0) 复合。常项消去来自同一数学量的恒等式，
并非丢弃独立的近似根误差。

K 的构造先在 E 中加入原函数的全部无限 Fourier 误差，随后才计算
K=(a′E′−2a″E)/(2aE²)。实中心的全部真实时间系数为实数，因而只在此处采用实部投影。
保留 K_0,...,K_{m−1} 后，在独立更大的时间盘 |u|≤S_K 上重新以完整复原函数计算
a/E 排零与真实 |K|≤M_K。此处不要求 K 的实部有固定符号。
于是内盘 R 上的完整遗漏时间尾为

\[
 T_K=M_K\frac{(R/S_K)^m}{1-R/S_K}.
\]

有限边界函数为
P(φ)=Re[−Σ_{j<m}K_j R^j exp(ijφ)]。
在 N 个闭角 cell 的中心 φ_l 上，取 δ=π/N，并支付

\[
 P(\phi)\ge P(\phi_l)-|P'(\phi_l)|\delta
 -\frac{\delta^2}{2}\sum_{j<m}j^2|K_j|R^j .
\]

再减 T_K。所有 cell 的下界严格正后，Re(−K) 的调和最小值原理给整个 |u|≤R 的正下界。
所有有限系数、圆周评价、导数范数与完整尾均用 Arb/Acb 包围。
这保留了近转折主项约为 (τ+π/2)² 的相关性，不需把它拆成独立径向区间。

实际 forward 4 的两 germ，m=41、N=128、R=6、S_K=8：

| germ | Re(−K) 下界 | 完整遗漏时间尾 | 标量门 CPU |
| --- | ---: | ---: | ---: |
| 0 | 0.0041187307854 | 6.9522924×10⁻⁵ | 1.37 s |
| 1 | 0.0036252725866 | 7.4923817×10⁻⁵ | 1.27 s |

该门单独不证明 D 排零，完整场仍须下一节。

## 2. 不减旧球误差，选择完整尾的起点

旧保存的 invariant 时间系数包含按原 R3 付的真实 primitive 误差。
例如 forward 4 的第 40 阶 D 球范数约为 2.53×10⁻²⁶；直接乘 6⁴⁰ 后约为 3.38×10⁵。
这说明原球不足以直接高阶外推，不能从球中减去所谓噪声。

新 `fourfold_saved_time_optimal_cauchy_extension.py` 只保留前 m 项；其后的整个无限块
使用新的 invariant 外盘 S_I 支付。曲率外盘 S_K 与 invariant 外盘 S_I 分开。
在 |u|≤S_I 的窄/宽物理角带上分别付真实完整 invariant 模数 M、M′。
原保留 Fourier 范数 b_j 加完整新 Fourier 混叠/遗漏费用，形成
c_j=b_j+M′η/S_I^j。

每个 m=1,...,41 都给出一个独立正确的界：

\[
 \sup|V|\le \sum_{j<m}c_jR^j+
 M\frac{(R/S_I)^m}{1-R/S_I},\qquad V=D,M,W.
\]

对同一个真实实锚点 u_a，D 的变化界为

\[
 \sum_{1\le j<m}c_j(R^j+|u_a|^j)
 +M\frac{(R/S_I)^m}{1-R/S_I}
 +M\frac{(|u_a|/S_I)^m}{1-|u_a|/S_I}.
\]

选择其中数值最小的完整上界合法。程序保存所有 m 候选与被选 m，
M/W 的全模数和 D 的锚点变化可分别选取最优 m。
每一候选都支付全部无限尾，不存在删掉高阶球却未补偿的步骤。
外盘 invariant 模数不除 D、不取曲率平方根；因此可以用 S_I=12 或 16，
同时保留独立已付的 S_K=8。

## 3. 完整实际域

主 germ（索引 1）的实际比较：

| R / S_I / S_K | D 最优 m | D 下界 | 真实物理场 \|dθ/dτ\| 上界 |
| --- | ---: | ---: | ---: |
| 5 / 8 / 8 | 20 | 0.273286313314 | 0.505669217703 |
| 6 / 12 / 8 | 15 | 0.245410303059 | 0.623547262304 |
| 6 / 16 / 8 | 13 | 0.251476855393 | 0.689306539686 |

R6/S12 的完整两 germ 报告为
`data/phase_ring_continuation/step5_expanded_time_domain_full/forward_0004_optimal_R6_S12.json.gz`，
SHA256 `ac2eb927c994903ed2ca701682373794482249e1a60d0cb21667d490efb497b3`。
两 germ 都通过；索引 0 的 D 下界为 0.221880748412，真实场上界为 0.691293203471。
完整重放含初始化 CPU 6.92 秒、wall 41.81 秒；已有 sampler 时主 germ 的新门 CPU 2.18 秒。
这些字段均为完整真实场模数，尚未代表新的轨迹残差或整个返回图证书。

## 4. 接口与覆盖范围

```python
from fourfold_expand_optimal_time_domain import expand_domain
doc = expand_domain(path, out, R=6, S=12, curvature_outer=8,
                    models={main_index: old_scalar_sampler},
                    germ_indices=[main_index], bits=current_bits)
```

`models` 可省略。原 sampler 的较小共享原函数预算在新 majorant 计算后恢复，
实际 scalar 采样仍可用原 R3 入口。
只选主 germ 时，输出逐行带 `original_germ_index`，并只授予
`proved_selected_actual_germs`；整体 common-span 覆盖标志保留 false。
相邻真实小 cap 必须继续用原证明支付。
省略 `germ_indices` 时检查全部原 germs，仅全部通过才授予整体扩域。
`bits` 会按原统一工具约定设置当前 Arb 精度；复用高精度 sampler 时调用者传入当前精度。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_expand_optimal_time_domain.py \
  --domain data/phase_ring_continuation/step5_sharp_time_domain_full/forward_0004_r.json.gz \
  --R 6 --S 12 --curvature-outer 8 \
  --out data/phase_ring_continuation/step5_expanded_time_domain_full/forward_0004_optimal_R6_S12_replay.json.gz
```

保存的早期 `forward_0004_correlated_R6_S8.json.gz` 只改进 K、仍把全部 41 项 D 球直接外推，
因此整体失败；其源与报告保留为明确失败对照，不替代本正式输出。

## 5. 宽物理角带的实际失败范围

另一个独立候选是从旧角带 s 的 |D| 下界减去 (s′−s) sup_{s′}|D_θ|。
`fourfold_true_field_strip_perturbation.py` 确实在新更宽角带重新支付了真实 D_θ/M/W 全模数，
没有转授旧窄带 Fourier 范数。
turn 1/R6 的实际结果：s′=3/128 时 D_θ 上界为 4462.4133，D 下界为 −34.5484；
s′=1/32 时 D_θ 上界为 11686.7526，D 下界为 −182.2913。
两门都未通过。它们证明当前粗分量 majorant 不足以完成这次扩带，未证明真实 D 存在零点。
若后续需要更宽带，必须另外支付更精细的真实角信息。
