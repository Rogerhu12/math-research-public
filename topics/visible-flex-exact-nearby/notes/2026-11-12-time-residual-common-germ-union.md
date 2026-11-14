# 跨径向样条节点的有限 germ 并集残差界

## 1. 本次接口及精确对象

新接口 `scripts/fourfold_phase_field_time_germ_union.py` 处理一个有限参考
时间段穿过径向样条节点的情形。它保留冻结的严格单 span 时间引擎
`fourfold_phase_field_time_taylor.py` 和实际 Bernstein 适配器不变。

本次输入仍是准确 R57 仿射点
\(\delta_2=-15291006546051/9007199254740992\)，显式径向对称化、无限 R33
原函数和同步目标度量均保持同一定义。保存的参考仍是
`r61_step2_bernstein_forward/manifest.json`，SHA
`2a76ac79b15f28aa3ea95f708d10e073b346e0c23809a0c8021d391c1c2a816a`。
物理状态为 \(Y=x/4+U\)，\(q=e^L\)，本支 `sign=-1`。

算法不求任何样条节点的时间预像。尤其是两个节点间只有
\(2^{-53}\) 的时候，不会按这个间距生成极短时间段。

## 2. 有限并集命题

令 \(I\) 是一个严格内部的实时间段，
\(r(\tau)=t_*\sin\tau\)，其中 \(t_*\) 使用同一准确对象的认证根区间。
先由有向运算得到

\[
r(I)\subseteq[r_-,r_+].
\]

所有实际标量的二进制节点及其准确负反射构成有限有序节点集合。
取与 \([r_-,r_+]\) 相交的**全部闭共同区间** \(J_1,\ldots,J_m\)。
源码检查它们首尾覆盖径向包络且相邻端点准确相等，接触端点的区间也
不遗漏。外端点从 Arb `lower()/upper()` 的准确 dyadic 值转成 Fraction，
中途不使用浮点最近值决定覆盖。另将每个实际 B-spline 的合法域
`[knots[degree],knots[-degree-1]]` 及其准确负反射取交集，要求整个
真实径向包络严格位于此交集内；不会以全部节点的最大范围替代各
spline 的共同合法域。

对每个 \(J_i\)，用准确 Fraction 中点分别选定各个原标量在正、负
径向侧的真实 B-spline span，再以其完整多项式定义解析延拓。由此得到
\(F_i\)、同步 \(E_i,K_i\)、以及局部严格区特征场 \(f_i\)。
时间坐标仍使用同一个真实 \(t_*\)；不把每个延拓的曲率零点重新当成
时间尺度。

逐个延拓在**整个**参考时间段及较大的复时间盘上认证：

\[
\sup_I|Y_\tau-f_i(Y)|\le \epsilon_{0,i},\qquad
\sup_I|L_\tau-\partial_\theta f_i(Y)|\le \epsilon_{1,i},
\]

以及共同状态管内 \(|\partial_\theta^2 f_i|\le M_i\)。
每个界均包含无限原函数和 \(E_i\) 的误差、全部高阶时间 Cauchy 尾和
实际分母门。延拓在 \(J_i\) 外不是原始分段样条；在这里只作为一个
便于认证的扩大计算域。

对每个真实 \(\tau\in I\)，至少有一个 \(i\) 满足 \(r(\tau)\in J_i\)。
这个位置的实际几何及所需径向 jet 与该 germ 相同，因此

\[
|e_0(\tau)|\le\max_i\epsilon_{0,i},\qquad
|e_1(\tau)|\le\max_i\epsilon_{1,i},\qquad
|f_{\theta\theta}(\tau,z)|\le\max_iM_i.
\]

这一点不要求跨节点的实际场具有一条全局解析时间 Taylor 展开。
各 Taylor 级数属于各自解析 germ；最后只把它们的**函数值上界**合并。

代码还检查每个被使用的 B-spline 在内部节点满足
`degree − multiplicity >= 2`。因此物理标量、\(F_{rr}\)、
\(E'=2\langle F_r\cdot F_{rr}\rangle\) 及 \(a''\) 在节点连续。
严格区的实际 \(f,f_\theta,f_{\theta\theta}\) 因而连续拼接，且各 germ 的
分母门提供共同角向 Lipschitz 界。本次所有标量的最小内节点正则性
实际上至少为 \(C^4\)。

\(Y,L,q\) 在整个 \(I\) 始终是同一份有限参考。先对
\(e_0,e_1,f_{\theta\theta}\) 取最大值、\(|q|\) 取共同上下界，再做
**一次** R60 比较；不能把不同 germ 各自的终点误差简单取最大值来
替代整个实际分段场的累积误差证明。

## 3. 演示一：保证穿过一个真实节点

取参考第 654 段的准确归一子段 `[5/8,7/8]`，固定 \(x=1/2\)。其准确
时间端点为

\[
\left[
\frac{36271372797928523}{72057594037927936},
\frac{36293706851665433}{72057594037927936}
\right].
\]

实际径向像包含在
\([0.1149971980481257,0.1150619183224070]\) 内，并保证穿过准确节点

\[
k=\frac{8286623314361713}{72057594037927936}
\quad\text{（保存的 binary64 0.115）}.
\]

列出的两个共同区间是

\[
\left[
\frac{8173936700574847}{2^{56}},\frac{8286623314361713}{2^{56}}
\right],\qquad
\left[
\frac{8286623314361713}{2^{56}},\frac{8466767299456533}{2^{56}}
\right].
\]

两个区间都不能单独容纳整个实际径向像，故此例确实使用了跨节点并集。
合并后的保守有向结果为

\[
\|e_0\|_\infty<1.171733910\times10^{-6},\qquad
\|e_1\|_\infty<4.796083697\times10^{-4}.
\]

各 germ 外复时间盘的 \(|D|>0.7991\)、
\(\operatorname{Re}(-K_i)>0.5724\)。全部高阶时间尾分别小于
\(2.127\times10^{-16}\)、\(1.863\times10^{-15}\)。
若单独定义真实左端初值匹配参考，则整个实际分段场的物理角误差小于
\(3.632280\times10^{-10}\)。

## 4. 演示二：间距只有 \(2^{-53}\) 的两个节点

取参考第 653 段的准确归一子段 `[19/64,21/64]`，固定
\(x=1/2+i/512\)。准确时间端点为

\[
\left[
\frac{35729351395522433}{72057594037927936},
\frac{35750959674103047}{72057594037927936}
\right].
\]

其真实径向像包含于
\([0.1134231507577456,0.1134860257410598]\)，保证穿过两个准确不同节点

\[
k_- =\frac{8173936700574839}{2^{56}},\qquad
k_+ =\frac{8173936700574847}{2^{56}},\qquad
k_+-k_-=2^{-53}.
\]

共需三个 germs，分别覆盖

\[
\left[\frac{8106479329266893}{2^{56}},k_-\right],\qquad
[k_-,k_+],\qquad
\left[k_+,\frac{8286623314361713}{2^{56}}\right].
\]

中间 germ 用准确 Fraction selector 读取两侧原 spline 的多项式；
不会把两个节点视为相等，也不除以这个共同区间的长度。
三份报告全部通过，合并结果为

\[
\|e_0\|_\infty<3.310735361\times10^{-7},\qquad
\|e_1\|_\infty<4.341193249\times10^{-4}.
\]

各 germ 的 \(|D|>0.8010\)、
\(\operatorname{Re}(-K_i)>0.5799\)。全部高阶时间尾分别小于
\(2.149\times10^{-16}\)、\(2.032\times10^{-15}\)。
在单独的左端匹配初值问题中，整个实际分段场的物理角误差小于
\(9.930979\times10^{-11}\)。

两例均使用 Q512、160 bits、时间阶 16、外时间半径 8、
\(R_0=3/1000\)、\(R_E=1/400\)、归一角原函数条带 \(8/25\)、
状态管半径 \(1/65536\)。这些仍是固定标签和指定时间子段的结果，
没有全初值条带、完整分支、转折 collar、参数导数或 Wiener 残差结论。

## 5. 可重放文件

| 文件 | SHA256 |
|---|---|
| `scripts/fourfold_phase_field_time_germ_union.py` | `53704f95997e92eca13b74e9466c8ccb60a0ce04c4360e91b23eef9b10c712b5` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_reference_time_union_single_knot.json` | `63561906deee3971f39ba8b3dcdd62c2b4d0b5f82154ee1fc87fa84b9e0eaa49` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_reference_time_union_near_knots.json` | `982edf9491e36658d1600f648d700ab19e3efe1e351988a2d6e9e3e4e45c4d1a` |

各 JSON 另完整记录实际对象、根、参考 shard 和依赖源码的 SHA；
逐 germ 保存全部保留时间系数、外盘门、无限尾和精确 common span。
成功结束前 `complete` 一直为 `false`，每完成一个 germ 即保存。

在课题目录重做第一例：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_field_time_germ_union.py \
  --manifest data/phase_ring_continuation/r61_step2_bernstein_forward/manifest.json \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_root_tight.json \
  --segment 654 --sub-left 5/8 --sub-right 7/8 \
  --initial-label-real 1/2 --initial-label-imag 0 --quarter-nodes 512 \
  --out /workspace/scratch/f6a2c7886477/newton-experiments/r61_union_single_knot_replay.json
```

第二例改为 `--segment 653 --sub-left 19/64 --sub-right 21/64`
及 `--initial-label-imag 1/512`，输出使用独立路径。
通用 `FixedGermTimeModel` 暴露与冻结 `FieldTimeModel` 同样的已缓存
时间系数和残差方法，可继续供角变量 Taylor 层使用。
