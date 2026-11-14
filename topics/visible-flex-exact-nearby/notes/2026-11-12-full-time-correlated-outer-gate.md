# 整个普通时间段的相关外域门

## 1. 已付对象与范围

本次使用准确仿射点 
\(\delta_3=-7832869216826619/4611686018427387904\)，其对象文件为
`type_fixed_step02_d5_exact_affine_step3_object.json`。没有把该点替换成
rounded 导出图，也没有将结果转给不同的 \(\delta_4\)。有限参考是
`r61_step3_shared_forward/manifest.json` 的第 419 段，使用整个 `[0,1]`：

\[
\tau_a=1116681926568983/2251799813685248,\qquad
\tau_b=70659179602557/140737488355328.
\]

令 \(\tau=\tau_c+h u\)。所有实际径向像相交的 common spans 都被准确
Fraction 列出，共三个，其中中间 span 长度为准确 \(2^{-53}\)。对每个
span 的解析延拓分别付外域门，再覆盖实际场所在的时间子集。没有声称
跨样条 knot 的实际时间函数整体解析。

初值标签中心为 \(x_0=1/2+i/512\)，有限参考状态是物理角
\(\theta=Y=x/4+U\)。采用时间外半径 \(R=3\)、更大圆盘 \(S=4\)，
物理状态 Cauchy 半径 \(A=1/50\)，时间阶 40、状态阶 20、Q512、
160 bits。角标签外半径为 \(R_x=4\)。

完整有限检查已经证明：三个 germ 的整个时间盘都允许
\(h_x=1/4096,1/1024,1/256\) 的标签外圆盘及额外状态管
\(1/65536\)。这是实际场及其头两个物理角导数的外域/模数证书；
它本身不支付整个初值角弧的相关残差，也不支付完整分支的累计流误差。

## 2. 不再用宽盒 FFT 的高频噪声支付外圈

在柱坐标标架记 \(X=F_r\)、\(H=(aT)_r\)。对于固定复径向盒与
normalized 角带 \(|\operatorname{Im}(4\theta)|\le\sigma\)，写
\(\beta=\sum b_k\sin(4k\theta)\)、\(\gamma=\sum g_k\sin(4k\theta)\)。
可取

\[
 I=\sum_k\bigl[(|\Re b_k|+|\Re g_k|)\sinh(k\sigma)
                   +( |\Im b_k|+|\Im g_k|)\cosh(k\sigma)\bigr],
\]
\[
 B_r=\sum_k(|b'_k|+|g'_k|)\cosh(k\sigma),\qquad
 M_{X\mathrm{src}}=(|a'|+|a|B_r)e^I.
\]

于是 \(H\) 每个分量的第 \(k\) 个准确 Fourier 系数至多
\(M_{X\mathrm{src}}e^{-\sigma|k|}\)。真实原函数在非零频率上的水平
乘子总模为 \(1/(4|k|-1)\)，竖直乘子模为 \(1/(4|k|)\)。令所需
内部 normalized 角宽为 \(s<\sigma\)，\(q=e^{-(\sigma-s)}\)，便有

\[
\begin{aligned}
 |X_r|&\le M_{X\mathrm{src}}\left[1-\frac23\log(1-q)\right],\\
 |X_\theta|&\le-\frac23M_{X\mathrm{src}}\log(1-q),\\
 |X_z|&\le |Z'|-\frac12M_{X\mathrm{src}}\log(1-q).
\end{aligned}
\]

这里 \(X_\theta\) 表示柱坐标的切向分量，不是对 \(X\) 求角导。
水平零频率的径向分量至多 \(M_{X\mathrm{src}}\)，切向分量准确为零；
竖直零频率为 \(Z'\)。这些事实使用原相位的准确角奇偶性，复径向
延拓保留此奇偶性。该预算直接支付真实无限原函数，没有把有限 FFT
系数的高频区间宽度当作真实高频谱。

源码只在有限个明确的有效 \(\sigma\) 上形成各自独立正确的上界，
再选较小者。候选为 \(1/8,4/25,1/5,8/25,1/2\)，每个先检查
\(\sigma>s\)。选择时的浮点比较只选择一个已经有效的界，不参与
证明其大小。本次选到 \(\sigma=1/8\)。

原始宽盒 FFT 方案产生约 \(1.5\times10^9\) 的外圈 \(|D|\) 界，
其时间尾约 \(4.6\times10^4\)，完全不能分离分母。新真实 Fourier
预算把同一外圈 \(|D|\) 界降到 143 以下。旧尝试只是界失败，不能
据此认定实际复场存在极点。

## 3. 相关时间/状态 Taylor 与完整双尾

相位、\(a,a'\) 为冻结径向多项式与有限三角多项式的准确组合。
只在状态偏移零处求一次真实 \(X(u,0)\) 的时间系数，有限原函数和
无限误差按此前 time engine 付费。其余状态系数由准确恒等式

\[
 \partial_s X=(a'T+aT_r)-JX,\qquad
 J(X_1,X_2,X_3)=(-X_2,X_1,0)
\]

递推。若 \(X=\sum X_j(u)s^j\)、\(H=\sum H_j(u)s^j\)，则

\[
 X_{j+1}=(H_j-JX_j)/(j+1).
\]

这避免对有限截断原函数求角导后冒充真实 \(a'T+aT_r\)。实现使用
已独立验证的 `TimeAngleJet` 矩形系数环。\(D,M,W\) 的状态一、二阶
系数还逐项与独立的物理角导数公式核对，全部包含同一值。

设解析量 \(F\) 在 \(|u|\le S,|s|\le A\) 上满足 \(|F|\le M\)，
保留 \(0\le i<m,0\le j<n\) 的真实 Taylor 系数。写
\(q_t=R/S\)、\(q_s=d/A\)。在内部双盘上的完整余项可取

\[
 M\frac{q_t^m}{1-q_t}\frac{1-q_s^n}{1-q_s}
       +M\frac{q_s^n}{1-q_s}.
\]

证明顺序是先截断状态：在整个内部时间盘上用统一 \(M\) 支付状态尾；
每个已保留状态系数在更大时间盘上至多 \(M/A^j\)，再分别支付其
时间尾并求和。未知时间/状态角落没有丢弃。有限系数在取模之前
保留时间和状态相关性。

\(D,M,W\) 以及各自前两次角导数的粗外模无需除以 \(D\)。曲率
\(K\) 另用准确 \(a,E\) 的外盘不为零门及完整时间 Taylor 尾支付；
同步 \(E\) 的无限误差在形成 \(K\) 前已经加入。最后才检查内部
\(|D|>0\)、\(\Re(-K)>0\)，并形成

\[
 f=-t_*\cos\tau\,\frac{M+\mathrm{sign}\sqrt{-K}\,W}{D},
\]

以及 \(f_\theta,f_{\theta\theta}\) 的有向模数界。

## 4. 完整第 419 段结果

在最大已付标签半宽 \(h_x=1/256\)、\(R_x=4\) 下，原有限 Fourier
参考的状态变化为 0.012738540 以下，加上状态管后 \(d<0.012753799\)。
以下均取三个 germ 的共同保守界：

| 量 | 严格共同界 |
|---|---:|
| \(|D|\) | 大于 0.75 |
| \(\Re(-K)\) | 大于 0.5769 |
| \(|f|\) | 小于 0.555 |
| \(|f_\theta|\) | 小于 17.71 |
| \(|f_{\theta\theta}|\) | 小于 2386 |
| \(D\) 的时间尾 | 小于 0.011834 |
| \(D\) 的状态尾 | 小于 0.030930 |

\(h_x=1/64,R_x=4\) 的有限参考状态变化上界已达 0.160193，超过
本次 \(A=0.02\)；报告明确记录这一入口拒绝。它不是极点的证明，
也不能把 \(h_x=1/256\) 的结果插值延长至此范围。

固定中心标签的整个时间段残差也重新计算，三个 germ 的 \(e_0\)
界分别约为 \(4.0042\times10^{-8},2.0276\times10^{-8},2.4902\times10^{-9}\)，
\(e_1\) 界分别约为 \(1.0567\times10^{-6},8.1435\times10^{-7},
6.6864\times10^{-7}\)。此时完整场时间尾已低于
\(1.549\times10^{-20}\) 和 \(9.739\times10^{-20}\)。因此剩余残差
主要来自有限参考及将极短活动 germ 外推到整个时间段的代价，不能
用进一步压小时间尾替代参考修正。后续可将两个近重合 knots 放在
一个有限左端 cap 中统一核验，其余区仅用实际所属主 germ；本报告
尚未进行这种分段，也未将这种改进计入已付界。

## 5. 接口、身份与重放

新入口不修改已冻结 time engine。主接口为：

```python
gate = StateTaylorOuterGate(
    model, theta_coefficients,
    larger_time_radius=4,
    state_cauchy_radius=Fraction(1, 50),
    state_precision=21,
)
domain = gate.bound(exact_total_physical_state_radius)
```

`theta_coefficients` 可以包含高于原参考七次的有限修正多项式；每次
仍重新构造该参考中心处的真实场系数和外域。初值角弧导致的有限
参考变化、修正多项式在外双盘的变化，以及额外状态管都须加入
`exact_total_physical_state_radius`，且严格小于所付 \(A\)。不能
只更改参考而沿用旧的较小状态半径。

| 文件 | SHA256 |
|---|---|
| `scripts/fourfold_phase_time_outer_taylor_gate.py` | `dedbda9a689fcb49642aca4bd69cfbcdc502d71836b2480968606e74d40051a4` |
| `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_reference419_full_outer_gate.json` | `8e3a554dbd6a4de90508765bbfe8562dc95d76dd765bfbe1aacd1923ce9d1b66` |

报告完整保存对象、根证书、参考 manifest/shard、依赖源码的 SHA，
准确时间端点、真实根细化轨迹、全部 common spans、每个 germ 的
各个角弧门、失败原因、真实曲率界与场尾预算。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_time_outer_taylor_gate.py \
  --manifest data/phase_ring_continuation/r61_step3_shared_forward/manifest.json \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json \
  --segment 419 --time-order 40 --state-order 20 \
  --time-outer-radius 3 --larger-time-radius 4 --state-cauchy-radius 1/50 \
  --angle-outer-radius 4 --angle-halfwidths 1/4096,1/1024,1/256,1/64 \
  --out /workspace/scratch/f6a2c7886477/newton-experiments/reference419_full_outer_gate_replay.json
```

`complete` 仅表示所有必需 germ 已完成计算；每个具体角弧是否严格
通过须读取 `complete_arc_domain_proofs`。本次前三个宽度为 true，
最后一个为 false。完整 R31/R60/R61/R63 的其他输入仍须独立支付。
