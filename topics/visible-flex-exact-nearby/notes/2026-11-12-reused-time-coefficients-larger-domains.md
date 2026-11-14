# 用已付真实时间系数扩展场的复时间域

这里复用的是保存的真实无限原函数 D/M/W 的时间系数 DFT 球范数，
不是把有限多项式的小尾直接当成真实场尾。两份入口为
`fourfold_saved_invariant_time_extension.py` 与 `fourfold_expand_saved_time_domain.py`。
它们不改旧 scalar sampler 原 R3 的公共原函数预算；新外盘预算计算后立即恢复该旧预算。

## 完整补集

设旧报告给出在物理角带宽 s 上各保留时间系数的有限 Fourier 范数 b_j，
时间圆盘中心与尺度完全不变。新取 1<R<S，并在 |u|≤S 上分别支付
角带 s 和更宽角带 s′ 的整个真实 invariant 模界 M 与 M′。
旧 Fourier 网格的混叠加遗漏频率因子记为 η。
则完整 j 阶系数范数满足 c_j≤b_j+M′η/S^j。
若保留 m 项，新内盘上的完整无限时间余项为

\[
 M\frac{(R/S)^m}{1-R/S}.
\]

同一个真实 R59 实锚点 u_a 的 D 下界减去

\[
 \sum_{j=1}^{m-1}c_j(R^j+|u_a|^j)
 +M\frac{(R/S)^m}{1-R/S}
 +M\frac{(|u_a|/S)^m}{1-|u_a|/S}
\]

即得整个新盘的 D 排零门。全部复角都已纳入上述范数，外盘 invariant 预算不除 D，
也不使用曲率平方根。曲率分支另外在内盘 R 上真实验证。

转向 germ 用同一个准确根的 K(t−ρ) 除根级数，保留所有实际径向系数及
`M_K/R_K * q^degree/(1-q)` 无限径向余项，验证 Q 的实部严格正。
普通 germ 当前入口直接验证完整复径向像上的 a/E 排零与 Re(−K)>0；
这个充分门可能因矩形区间包裹而拒绝可行域。拒绝本身不是实际奇点的证明。

只允许准确同中心、同尺度或准确反射 u→−u、r→−r。
继承源有时间平移或缩放时，本入口拒绝免费迁移系数；报告保存原来源文件、哈希、germ 和反射符号。
新的输出逐 germ 给出新 invariant 模数、完整补集、曲率分支和真实场模数，
不以旧 `inherited` 字段冒充已付较大域。

## 实际结果

输入始终为准确 δ5 对象及冻结 shared1032 的时间段。

| 输入 | R/S | 实际结果 |
| --- | --- | --- |
| forward 1，完整 turn germ | 6/8 | 通过：D>0.314222963868，\|f\|<0.316943985400 |
| forward 4，原两个普通 germs | 6/8 | 两个普通曲率复盘门均未通过，整段不能升级 |
| forward 419，原三个普通 germs | 6/8 | 前二 D 下界负，第三通过 D>0.03269801328、\|f\|<29.39446975；整三 germ 域不能升级 |

完整 turn 1 报告为
`data/phase_ring_continuation/step5_expanded_time_domain_full/forward_0001_R6_S8.json.gz`，
SHA256 `26bd69302c35e6127fc357eff80fab4ce4bf5db8674d3f1c207221746c77dc1c`。
实际计算 CPU 6.09 秒、wall 34.88 秒，其中包括根与 sampler 初始化。
已有真实 sampler 时无需重复初始化。

保持旧角 N2048/K895、相同工作角带和目标费用，完整解析预算允许 turn 1
时间节点数从 52 降到 30，解析误差 `2.06402229225e-21` 小于目标四分之一
`2.17735993983e-21`。这是新布局可行性；仍须重新实际采样并支付节点球误差，
不能把该布局报告称为新的残差证书。

419 已有独立 sharp 单 germ 的 order40 R6 域；本次旧三 germ 域的失败不撤销该独立输入。
主 germ 扩域与相邻小 cap 的真实费用可分开，但必须由调用者保留正确对象与时间覆盖。

## API 与重放

```python
from fourfold_expand_saved_time_domain import expand_domain
doc = expand_domain(original_path, new_output, R=6, S=8)
```

可选 `models={germ_index: initialized_scalar_sampler}` 复用已初始化 sampler。
必须检查 `proved_full_physical_angle_and_complex_time_domain`，不能仅检查 `complete`。
失败时继续使用原已付 R3 域。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_expand_saved_time_domain.py \
  --domain data/phase_ring_continuation/step5_sharp_time_domain_full/forward_0001_r.json.gz \
  --R 6 --S 8 \
  --out data/phase_ring_continuation/step5_expanded_time_domain_full/forward_0001_R6_S8_replay.json.gz
```

以 `forward_0004_r.json.gz` 或原 `type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json`
为输入即可重放两个已保存失败范围。所有输出必须另命名，保留原报告。
这批结果只供应真实场解析域；尚未支付整条返回流或 KAM 结论。
