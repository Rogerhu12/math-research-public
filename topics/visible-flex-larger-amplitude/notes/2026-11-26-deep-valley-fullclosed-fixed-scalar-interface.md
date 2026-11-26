# 深谷固定标量的完整 canonical 入口

**状态：已实现的源码与解析接口；尚无本入口的科学返回。** 这是 R690 新标量的实际 fullclosed 接线，不是原场证书的转移，也不是 moving-mean 设计。科学运行只在公开仓库 Actions。原始数据和可重算 carrier 仅保留在同 runner scratch；公开源码、命令、run、紧凑结果及 SHA。

## 1. 字节绑定与数学对象

新源为 `scripts/resume_20261126/deep_valley_reference_factory.py`：

- factory SHA-256：`4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1`；
- R690 标量源：`e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2`；
- 原 R671 完整物理/J/J* factory：`2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216`。

新 canonical schema 为 `deep-valley-fixed-scalar-fullclosed-lift-v1`。它固定 R690 的同一个 $S$、新 $a_n,I_n,R_n$、原节点上同一个 $\eta$，并固定 $\lambda=1$。几何表示为

$$
F=q+\eta a_n e_r(\Theta)+\eta(H-I_n)e_z.
$$

目标是**固定**的

$$
g_n=ds^2+a_n(s)^2d\theta^2.
$$

完整 Gram 算子直接以 $a_n\rho$ 归一化。没有 `MeanMetricOperator`，没有把 $a_n$ 消去的 moving angular mean。所有原 $q$、自由 core、$H$、原节点/中点、同标量 Gauss 观测、原母范数和幅度约束仍由完整 solver 使用。

模型 identity 纳入新 scalar definition/source、原 scalar 输入/source、原完整 operator/source、当前 observation/node report 的 SHA、同一精确 $\eta$ 和 mesh。原 q/H/core 是新 seed 的坐标；数学场本身已改变，不声称原度量、几何或接受性保持。

## 2. 原父到新输入的显式 prepare

只在 prepare 的显式 `allow_original_parent=True` 分支允许读取原 R671 canonical 父。它先按原 R671 的完整 definition 核对真实来源，再创建新 observation/node carrier；普通 `from_files` 只接受新 schema。

保持原 mesh 和每个精确 $\alpha S+\beta$ 节点，替换全部必要的 $a$ 值、完整误差和 $R$。在改动尾段之前，$a$ 的原 literal carrier 可保持，但重新计算其对新精确标量的完整误差。准确 cap literal 取本次持久化的 $R_n$ carrier；误差支付该实际字，而非另一中点。

`transfer_seed(..., source_lambda=1, mode='keep-q')` 保持全部自由坐标字节。由于 $I_n$ 的终端积分改变，非尾部的 $\eta(H-I_n)$ 也可能改变；所以它明确报告 `physical_field_unchanged=false`。

一次 prepare 命令的输入为真实已返父及其全部已知几何位置：

~~~sh
python "$TOPIC/scripts/resume_20261126/deep_valley_reference_factory.py" \
  --bundle "$PARENT_BUNDLE" \
  --observations "$PARENT_OBSERVATIONS" \
  --node-report "$PARENT_NODES" \
  --scalar-input "$ORIGINAL_SCALAR" \
  --scalar-source "$TOPIC/notes/2026-11-17-parallel-model-full-hold-oracle.py" \
  --integer-source "$TOPIC/notes/2026-11-17-parallel-inward-integral-enclosure.py" \
  --hold-source "$TOPIC/scripts/parallel_20261117_negative_hold_profile_ivp.py" \
  --observed-source "$TOPIC/scripts/resume_20261120/gauss_observed_closed_gram.py" \
  --operator-source "$TOPIC/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
  --batch-source "$TOPIC/scripts/resume_20261120_batched_closed_gram.py" \
  --eta-start-node 885 --angles 2048 --stage-block 64 --panels 128 \
  --scalar-tail-cutoff 1/8 --scalar-integral-tolerance 1e-18 \
  --scalar-admission-seconds 300 \
  --witness-input "$ALL_CURVATURE_MEMORY" \
  --radius-witness-input "$ALL_RADIUS_MEMORY" \
  --outdir "$WORK/deep-valley-fixed-scalar-prepared"
~~~

多个实际 memory 文件可重复给相应参数。不能把缺失的已知位置用空 manifest 代替；该入口迁移的是位置，不迁移原数值。

输出在新目录：

| 文件 | 含义 |
|---|---|
| `seed.npz` | 同 q/core/H、明确新模型的 seed |
| `observations.npz` | 同 observation plan 的新 $a_n,R_n$ carrier 与误差 |
| `nodes.json` | 同 $\alpha S+\beta$ 的新 scalar/model/node 定义 |
| `reference-profiles.npz/json` | 全部需要的 $(a_n,a_{n,s},a_{n,ss},I_n,I_{n,s},I_{n,ss})$ 及误差 |
| `locations.json` | 旧/新 carrier 都声明的完整位置转移 |
| `report.json` | 身份、实际尺寸、计数、迁移性质和未完成标志 |

新 location schema 为 `deep-valley-same-symbolic-location-transfer-v1`。每个 cell、binary64 $u,\phi$ 和 protection 位完整保留；新 solver 消费新 carrier 的 manifest，而非把原 carrier 与新 field 混交旧 collector。

## 3. 完整数值 factory API

`TailLiftContext.from_files`、`create_pair`、`save_carrier`、`transfer_seed`、`bundle_arrays` 的参数形状延续原 R671。新 constructor 另允许显式设置标量工作预算和精度；这些仅控制包围宽度，不改变精确标量定义。

`point_adapter(original)` 直接调用字节绑定 R671 的原函数。原 point module 的实际 `__file__` 和函数源码身份不伪装；它的 `fields_at` 经当前 problem/context 的 `lift_at` 取新 $f,h,k$。所有 core/$H$ 导数仍走原完整链。由于 $\lambda=1$ 时 $h=\eta$ 未变，原物理高度方向和母范数的 $h$ 结构仍适用。

但是**对原 factory.definition 源码硬绑定的 helper 必须另建诚实的新 binder**。尤其原 R681 current-J coarse assembler 和 R674 continuous reader 不能靠改 metadata 冒充接受新模型。新的 helper 可以复用原完整代数，须将实际新 canonical/source 作为输入，并独立发表源码。

新 solver 应先完整读一次新 seed 的全部原/Gauss Gram 行、全部永久 curvature/radius/amplitude 位置，再求当前固定 $g_n$ 的方向。新的当前 J/current Gram/v5、QP、全部旧行和幅度双支均继续使用同一个 new scalar identity。改变 scalar 是另一个输入，不得在同一条固定-$g_n$ 加密序列中混入。

## 4. 连续证书责任

R690 标量整数包围包括完整无限振荡尾，`reference_at_affine` 支持 $S$ 包围横跨新拼接点的情形；未达请求积分宽度时仍返回全域有效盒。

数值 carrier 和完整 sampled screen 都不是连续证书。新连续 reader 必须：

1. 按新 canonical 与实际 scalar/source/carrier 校验；原 R674 正常拒绝新 schema。
2. 在原 scalar/eta 分割中加入精确 $S-d/4$、$S-d/8$ 和计算采用的纯尾切点。
3. 支付新 $a,I$ 的全部一、二阶误差及完整 angular lift；不删任何原有限 Fourier mode。
4. 对同一个新 bundle 重新得到 $D,L,E,W^2$、support 和 $K$；旧父任何数值均不继承。
5. 连续 metric 比较同一个固定 $g_n$，并保留纯尾的准确 $a_n=R_n+t+\mathrm{flat}$，不能以 old out-ramp quintic 代替。

首 prepare 报告固定将 `whole_new_seed_Gram_or_geometry_read_performed`、`accepted_nonlinear_step`、`new_nonradial_exact_solution`、`topic_complete` 设为 false。只有后续真实 solver/reader 的返回可以填写对应事实。该入口为继续工作准备完整实际输入，未声称绕开 R669 的新输入已经产生非轴对称精确解。
