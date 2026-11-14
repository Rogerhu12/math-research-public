# 时间块共享的真实根细化

## 1. 新入口的用途

`scripts/fourfold_phase_field_time_refined_root.py` 增加两个接口：

```python
package = prepare_refined_root(object_path, root_certificate, nodes=512)
model = RefinedGermTimeModel(
    object_path, root_certificate, tau_center, time_halfwidth,
    refined_root=package, cell=optional_common_cell,
    nodes=512, order=16,
)
```

根证书仍是原有输入身份；manifest 与原证书的 SHA 对应关系保持不变。
新函数在该根区间内作真实无限原函数的 interval Newton，并把有向
收缩轨迹写入新报告。这里没有用一个任意更精确的中心值替代认证根。

同一进程中的根包按准确对象 SHA、原根证书 SHA、工作位数、Fourier
节点数和解析预算参数缓存，多个普通时间块或有限 germ union 块可
共同使用。缓存不会跨不同参数点复用。

没有传 `cell` 时，整个真实实时间径向像必须在一个准确 common span
内。显式传入 `cell` 时，只认证该 span 的解析延拓；完整实际时间
覆盖仍须使用此前的有限 germ union 规则，列全所有相交 spans，再
统一取最大值。根包已经检查各实际 B-spline 的共同合法域与反射以及
内部至少 \(C^2\) 的拼接条件。

## 2. 证明与保留的误差

根由同一准确仿射对象的 \(C=a'E'-2a''E\) 决定。每次收缩使用

\[
t_*\in I\cap\left(m-\frac{C(m)}{C'(I)}\right),
\]

其中 \(m\) 是当前区间中点，\(C'(I)>0\) 经有向运算验证。先有原
证书保证唯一真根位于 \(I\)；均值定理保证每一步保留该根。
原函数无限 Fourier 尾和同步 \(E\) 的无限误差在构造 \(C,C'\) 前
已加入。缩小后的根球还必须包含于原输入根球。

普通时间模型随后重新构造同一真实
\(r=t_*\sin\tau\) 的全部时间系数。\(r_0=t_*\sin\tau_0\) 仍按同一
定义锚定，组合变量的零常项来自恒等式。没有仅修改旧模型的 `root`
字段而保留围绕旧中心计算的系数。

场、角导数、外复时间盘分母门、无限原函数误差、时间 Cauchy 尾和
R60 比较直接继承冻结 `FieldTimeModel` 方法。因此本次只收紧同一
数学对象的输入包络，没有更换曲面、参数、有限参考或残差定义。

## 3. 同一个实际参考子段的重放

重放准确 \(\delta_2\) 对象的原第 653 段中心 `[31/64,33/64]`，标签
\(x=1/2\)，与
`type_fixed_step02_d5_exact_affine_step2_reference_time_segment653_real.json`
完全同一有限参考及物理时间。

使用 Q512、160 bits 后，根球半径降至
\(2.838\times10^{-29}\) 以下。两个残差中心时间系数的不确定性变化为：

| 系数 | 原 binary 端点根包产生的球半径 | 新真实根细化后的球半径 |
|---|---:|---:|
| \(e_0\) 的时间常项 | \(8.742\times10^{-14}\) 以下 | \(8.810\times10^{-27}\) 以下 |
| \(e_1\) 的时间常项 | \(1.446\times10^{-12}\) 以下 | \(1.389\times10^{-26}\) 以下 |

两个场、17 个时间阶、实虚两分量的共 68 个报告区间逐项检查，全部与
旧证书对应区间相交。完整真实参考残差仍为

\[
\|e_0\|_\infty<4.357573579\times10^{-7},\qquad
\|e_1\|_\infty<5.492791817\times10^{-4}.
\]

因此旧参考自身的残差并未因为收紧根而消失。新入口的作用是去掉
输入根包造成的约 \(10^{-12}\) 不确定性底，为后续更精确的参考留出
计算余量。

## 4. 文件与重做命令

| 文件 | SHA256 |
|---|---|
| `scripts/fourfold_phase_field_time_refined_root.py` | `7969b0dcf5ff43babe762dfdbb00836f4b4c3173965f923525ca64ab43886d79` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_reference_time_segment653_native_root.json` | `7b095a26a125b376e4de136e65dffbb3f0b4f02d948eb9c06078a5033844abcc` |

新报告完整保存原根球、新根球、每步 \(C,C'\) 及交集、真实 \(E\)
无限误差、原对象/原证书身份、全部参考与残差系数和外盘门。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_field_time_refined_root.py \
  --manifest data/phase_ring_continuation/r61_step2_bernstein_forward/manifest.json \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_root_tight.json \
  --out /workspace/scratch/f6a2c7886477/newton-experiments/reference653_native_root_replay.json
```

本次报告仍只覆盖固定标签和该实际时间子段。局部 R60 的左端匹配
假设、完整分支累计误差、全初值条带和 Wiener 认证的区别保持不变。
