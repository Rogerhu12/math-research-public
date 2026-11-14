# R110 续篇：实际严格负叶的能源恢复与所选强弱源的真实下界

2026-11-13，visible-exact-astra-ac0d。

**状态：完整原生报告已实际恢复，新增源下界已证明并实际运行。** 本篇的域仅为原连续核心证书的第60叶

$$
I_{60}=\left[
\frac{6112257798907291}{72057594037927936},
\frac{6124895493223875}{72057594037927936}\right].
\tag{E.1}
$$

所有系数取原准确 $\delta_5\pm10^{-9}$、真实无限角 Fourier 对象；输入仍是 R105 的五个归一化配对余弦高度及独立 regular 第六行。这里是正半径一叶，负侧反射的 Gram 另加同一份，不隐去 $1/\sqrt2$ 的配对归一。

## 1. 原丢失九场和连续能源已真实恢复

完整文件在 `data/native_core_20261113_ac0d`。九场数组
`energy9_leaf0060.npz.gz` 的 SHA256 为

```
1283562ea206e75c6572af57522f1ed1fd8e53eeebd909179977077df9dd9177
```

与原执行记录完全一致。新的连续 consumer 重新检查完整实径向域、所有闭角格、真实正性和严格负曲率；没有只从旧收据复制增长率。整个 quarter 核心含正领圈，不能用这一叶的严格负能源穿过它。

保主交换子符号、把其余交换子交给 base 能源驱动的实际两层比较是

$$
\binom{E_0^{1/2}(r_+)}{E_{1/2}^{1/2}(r_+)}
\le
\begin{pmatrix}
1.001233000&0\\
0.547748974&1.002805800
\end{pmatrix}
\binom{E_0^{1/2}(r_-)}{E_{1/2}^{1/2}(r_-)}
 +\binom{1.571705948}{6.577174363}\|\mathfrak f\|_{L^2(I_{60})}.
\tag{E.2}
$$

显示值向外放宽完整有向值，源 norm 是原报告明示的完整三源积空间。反向对应矩阵及源向量可取

$$
\begin{pmatrix}1.002072179&0\\0.548440868&1.004498605\end{pmatrix},
\qquad \binom{1.572364832}{6.582730126}.
\tag{E.3}
$$

这是实际执行 `fourfold_phase_strict_core_kernel_tame_energy_v2.py` 的结果。不能在每叶反复把 base 初值界代回高阶能源后累乘；全域应按两层有序矩阵及相应 Duhamel 核组合。

另一份 characteristic-density consumer 也已运行。32项矩阵指数尾界过松，保留该原报告；增加到96项后完整尾 $<1.126\,10^{-50}$，但转换成物理强状态后的齐次常数仍约322.117、源常数仍约1540.663。它是另一套已付范数中的界，不能与 (E.2) 的能源矩阵直接取数值大小比较，更不能称其为完整核心强逆。

## 2. 完整 exact-time 三源 Gram 已实际计算

`core_source_leaf0060_exact_time.json` 和其小 NPZ 保存全部时间多项式交叉项的准确积分，所有有限 Fourier 输出及完整真系数误差。采用原 R107/R110 的同一弱源表示

$$
P\widehat w=\partial_rR_r+\partial_\theta R_\theta-R_0,
\qquad
\mathfrak f=(R_0,R_r,R_\theta)
\in L^2(dr;H^{1/2}\oplus H^{3/2}\oplus H^{3/2}).
\tag{E.4}
$$

这里 $R_r=a\widehat w_r+b\widehat w_\theta-p_N$，$R_\theta$ 是原真实高角负荷，完整低角残差放在 $R_0$。angular mean、全部高输出及真实通量约定均保留。

实际完整三源算子上界为

$$
\|\mathfrak f:\mathbb C^5\to
 L^2(I_{60};H^{1/2}\oplus H^{3/2}\oplus H^{3/2})\|
<113.023699.
\tag{E.5}
$$

仅凭这个大上界不能判断真实源一定大。下一节给一个独立的方向下界，明确区分这两件事。

## 3. 同一所选弱源确有超过31.557的方向

取准确单位输入 $e_4=(0,0,0,0,1)$，即同一五列配对余弦高度空间的第五列。记 $T_f$ 为 `radial_all/Hthreehalf` 的完整**有限多项式**负荷算子，$G_f=T_f^*T_f$。报告中的已选择 Hermitian Gram 中心为 $G_c$，并已证明

$$
\|G_f-G_c\|\le\epsilon_G,
\qquad \|T_{\rm true}-T_f\|\le E.
\tag{E.6}
$$

完整输入给

$$
\epsilon_G<2.080\,10^{-13},\qquad
E<25.657470443.
$$

注意这里 $G_c$ 是有限 Gram 的带误差中心；没有把它认作真实无限源 Gram，也没有使用后者很大的 PSD 半径去作错误的特征值下界。

从准确 NPZ 的 binary64 对角元素取其精确二进有理值后，区间计算给

$$
\|T_f e_4\|\ge
\sqrt{(G_c)_{44}-\epsilon_G}
>57.21512430074095.
$$

反三角不等式与 (E.6) 因而证明，在完整同一参数盒上

$$
\boxed{\quad
\|R_r(e_4)\|_{L^2(I_{60};H^{3/2})}
>31.55765385827514,
\qquad \|\mathfrak f\|>31.55765385827514.
\quad}
\tag{E.7}
$$

新 consumer `scripts/fourfold_phase_core_source_lower_bound.py` 实际重新读取完整 Gram 数组，核原 producer、依赖及数组 SHA，并使用有向 Arb256位求平方根和差。完整输出是 `core_source_leaf0060_actual_lower_bound.json`。没有使用浮点特征向量或有限频率外推；输入 $e_4$ 的 norm 准确为1。

**适用边界。** (E.7) 是这个有限核心参考、这个物理通量选择和这个强三源范数的真实下界。它不是分布 $P\widehat w$ 在任意范数下的下界：添加 solenoidal 通量、利用不同方向之间的抵消、换用更准确的全角参考或真实高求解都会改变相应估计。它也不是精确全 PDE 不可逆、无近邻嵌入或主课题无解的结论。

但它排除了“继续把其余174叶的同一种非负源 norm 加上去，就能使这份总 norm 小于1”的可能性。按同一规范增加径向域只增大 $e_4$ 的平方积分。下一步应改善参考或用真正的传播/反馈相关结构，不能把 (E.5) 的113重新标成一个小误差门。

## 4. 重放和完整数据

从本题目录依次运行；若已有证据，使用新输出目录以保留它们：

```sh
python scripts/fourfold_phase_core_energy_fields.py \
  --leaf-report data/core_uniform_flow_ci/43307149760/block_60_80/span_0060_root.json \
  --out data/native_core_20261113_ac0d/energy9_leaf0060.json
python scripts/fourfold_phase_strict_core_energy.py \
  --field-report data/native_core_20261113_ac0d/energy9_leaf0060.json \
  --out data/native_core_20261113_ac0d/energy9_leaf0060_continuous.json
python scripts/fourfold_phase_strict_core_kernel_tame_energy_v2.py \
  --energy-reports data/native_core_20261113_ac0d/energy9_leaf0060_continuous.json \
  --refine-first-moments --method signed \
  --out data/native_core_20261113_ac0d/energy9_leaf0060_kernel_v2.json
python scripts/fourfold_phase_characteristic_density_energy.py \
  --energy-reports data/native_core_20261113_ac0d/energy9_leaf0060_continuous.json \
  --matrix-terms 96 --out data/native_core_20261113_ac0d/energy9_leaf0060_density96.json
python scripts/fourfold_phase_core_even_weak_residual_exact.py \
  --cover-root data/core_uniform_flow_ci/43307149760 \
  --field-report data/native_core_20261113_ac0d/energy9_leaf0060.json \
  --side 1 --bits 320 \
  --out data/native_core_20261113_ac0d/core_source_leaf0060_exact_time.json
python scripts/fourfold_phase_core_source_lower_bound.py \
  --source-report data/native_core_20261113_ac0d/core_source_leaf0060_exact_time.json \
  --out data/native_core_20261113_ac0d/core_source_leaf0060_actual_lower_bound.json
```

全部原生进程真实退出码为0。完整报告、数组和本次各源 SHA 见
`notes/2026-11-13-R110-native-energy-source-manifest.json`。
主问题仍需转折区、正帽、同一完整反馈 Schur、全源右逆及真正非线性收敛。
