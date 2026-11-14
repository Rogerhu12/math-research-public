# 已保存 Bernstein 参考的一个真实严格时间子段

## 1. 对象与本次得到的结论

本记录把 `fourfold_phase_field_time_taylor.py` 的真实无限原函数场接到
**已经冻结的** R61 Bernstein 参考上。没有重新生成参考系数，也没有由
局部 ODE 形式级数替代已保存参考。本次覆盖参考第 653 段的中心
`[31/64,33/64]`，分别固定两个准确初值标签

\[
x=\tfrac12,\qquad x=\tfrac12+\tfrac{i}{512}.
\]

各报告都覆盖该子段的**全部实时间**；两个离散标签不构成全初值圆、
全条带边界或完整往返的认证。

几何是准确 R57 仿射点

\[
\delta_2=-\frac{15291006546051}{9007199254740992},
\]

由 origin `0d17500a…`、direction `8db5d57d…` 在 Arb 中准确组合，随后
采用显式径向对称化和真正无限 R33 原函数。输入身份如下。

| 输入 | SHA256 |
|---|---|
| `type_fixed_step02_d5_exact_affine_step2_object.json` | `aa5df888dbf672c9e221f03e80cfa06c3c9c94a5dd7dd4f29fe15b1d795d99b1` |
| `type_fixed_step02_d5_exact_affine_step2_root_tight.json` | `c2cfad858f64a0082d131eb492993c6a237ab249220dfe61593323c8d1cdfeeb` |
| `r61_step2_bernstein_forward/manifest.json` | `2a76ac79b15f28aa3ea95f708d10e073b346e0c23809a0c8021d391c1c2a816a` |
| 冻结时间场引擎 `fourfold_phase_field_time_taylor.py` | `5f8b0294bc3cc6f19444ebf2d8e5106bdabaecab44576a77593890b2c42c312a` |
| 本次适配器 `fourfold_phase_reference_time_sample.py` | `2f89af783fd4a0a1c16caa39b1cb18377ce5e6fa7d5ee0ef8c117c2b47f0c189` |

这个参考由旧 Q256 浮点轨道构造；保存下来的二进制 Fourier / Bernstein
系数随后**定义准确有限参考**。本次真实场采用 Q512 的有限原函数计算，
另付所有无限 Fourier 尾，因而没有把 Q512 截断定义成真实场。

## 2. 准确时间、坐标及组合

原参考段的准确端点是

\[
a=\frac{4440509093625825}{9007199254740992},\qquad
b=\frac{4526942207948281}{9007199254740992}.
\]

本次子段的准确端点是

\[
\tau_- =\frac{35859001067006117}{72057594037927936},\qquad
\tau_+ =\frac{35880609345586731}{72057594037927936}.
\]

写作 \(\tau=\tau_0+h v\)，其中

\[
\tau_0=\frac{4483725650787053}{9007199254740992},\qquad
h=\frac{10804139290307}{72057594037927936},\qquad -1\le v\le1.
\]

适配器验证 manifest 的准确 `angular_scale=4` 与保存的 `sign=-1`。
状态是物理角

\[
Y(\tau,x)=x/4+U(\tau,x),\qquad q(\tau,x)=\exp L(\tau,x),
\]

初值标签 \(x\) 才是周期 \(2\pi\) 的归一角。故本次残差准确为

\[
e_0=Y_\tau-f(Y),\qquad e_1=L_\tau-\partial_\theta f(Y).
\]

没有把 \(Y\) 再乘 4，也没有把物理 \(\theta\) 导数换成 \(x\) 导数。

固定标签后，每个 Bernstein 控制点通过

\[
c_0+\sum_{k=1}^{129}\left(c_ke^{ikx}+\overline{c_k}e^{-ikx}\right)
\]

在 Arb 中求值。随后准确代入原段坐标
\(u=1/2+v/64\)，计算
\(\sum_{j=0}^7\binom7j u^j(1-u)^{7-j}b_j\)。
由此得到有限七次时间多项式；有向求值误差留在系数球内。
实标签的系数为实数是公式的共轭对称恒等式，只有在该条件下去除
纯计算产生的虚部宽度。复标签保留全部复系数。

真实 \(r=t_*\sin\tau\) 的整个实子段位于共同样条区间

\[
\left[
\frac{8173936700574847}{72057594037927936},
\frac{8286623314361713}{72057594037927936}
\right].
\]

该结论包括认证根区间的不确定性。引擎在选定的准确多项式 germ 上
构造局部解析延拓，另证真实实轨道始终在此区间内。

## 3. 有向连续残差及来源

计算精度 160 bits，保留时间阶 16，外时间半径 \(R=8\)，
径向原函数预算盘 \(R_0=3/1000\)，均值预算盘 \(R_E=1/400\)，
原函数归一角条带宽 \(8/25\)，额外状态管半径 \(d=1/65536\)。
原函数的完整外盘像、\(D\ne0\) 与
\(\operatorname{Re}(-K_0)>0\) 均由引擎验证。

以下十进制界均向保守方向留余量；可重放的完整有向球在 JSON 中。

| 量 | \(x=1/2\) | \(x=1/2+i/512\) |
|---|---:|---:|
| \(\sup_{|v|\le1}|e_0|\) 上界 | \(4.357574458\times10^{-7}\) | \(4.525209134\times10^{-7}\) |
| \(\sup_{|v|\le1}|e_1|\) 上界 | \(5.492791832\times10^{-4}\) | \(5.671564491\times10^{-4}\) |
| \(e_0\) 的全部高阶时间尾上界 | \(2.132\times10^{-16}\) | \(2.144\times10^{-16}\) |
| \(e_1\) 的全部高阶时间尾上界 | \(1.873\times10^{-15}\) | \(1.995\times10^{-15}\) |
| 外复时间盘 \(|D|\) 下界 | \(0.8019\) | \(0.8002\) |
| 外复时间盘 \(\operatorname{Re}(-K_0)\) 下界 | \(0.5783\) | \(0.5783\) |
| 实时间参考 \(|q|\) 下界 | \(2.16474\) | \(2.16478\) |
| 实时间参考 \(|q|\) 上界 | \(2.16530\) | \(2.16535\) |

两个标签的均值 \(E\) 无限尾上界均小于
\(8.806\times10^{-28}\)。实标签的原函数一阶时间外盘尾误差小于
\(2.532\times10^{-33}\)。

实标签时间中心的有向残差已与零分开：

\[
4.2333390248\times10^{-7}<e_0(0)<4.2333407733\times10^{-7},
\]

\[
0.0005405288963741<e_1(0)<0.0005405288992660.
\]

对应计算球半径分别只有 \(8.742\times10^{-14}\) 与
\(1.446\times10^{-12}\)。因此这个参考子段的主要误差来自已定义参考
本身，不能通过缩小时间 Cauchy 尾或增加区间计算位数消掉。
这并不单独判定旧参考的哪个构造步骤造成误差；它给出了同一准确对象、
同一坐标下参考与真实场之间的直接差。

## 4. 局部 R60 结论与范围限制

引擎另算 R60 的 \(A,B,C\) 及严格管门。**如果**在这个子段左端令
真实解初值准确等于参考左端值，即局部 \(r_0=0\)，则两种标签都通过：

| 标签 | 子段内真实物理角误差上界 |
|---|---:|
| \(1/2\) | \(1.307060\times10^{-10}\) |
| \(1/2+i/512\) | \(1.357345\times10^{-10}\) |

这里左端匹配是一个单独的局部初值问题定义。没有把全 forward 支
已经累积的误差设成零，没有授予整个初值条带、全时间轨道、转折
collar、参数导数或完整 Wiener 残差。

初次同段 `[3/8,5/8]` 的尝试通过了真实实径向单 span 检查，但外
复时间盘的粗区间分母门失败，程序抛出
`true field denominator not separated from zero on the outer disk`。
该失败只表示所用外盘区间估计未证明排零，不表示实际场有奇点。
本次随后缩小到 `[31/64,33/64]`，未更改几何、参考系数、初值标签或
分支。完整时间覆盖将需要有记录的时间细分或更锐的外盘分母门。

## 5. 冻结文件与精确重做入口

| 文件 | SHA256 |
|---|---|
| `type_fixed_step02_d5_exact_affine_step2_reference_time_segment653_real.json` | `547c5ec474b49c57c40cbac349ececeafd116e936e83f94bdba17dfca0da723b` |
| `type_fixed_step02_d5_exact_affine_step2_reference_time_segment653_complex.json` | `27320866721ab55ee539096f5279b095e9cccb283f3ff1f69cca389eb5eb8c7f` |

在课题目录运行；建议将重放输出写到独立 scratch 路径，避免覆盖历史
报告的耗时和运行记录。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_reference_time_sample.py \
  --manifest data/phase_ring_continuation/r61_step2_bernstein_forward/manifest.json \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_root_tight.json \
  --segment 653 --initial-label-real 1/2 --initial-label-imag 0 \
  --sub-left 31/64 --sub-right 33/64 --quarter-nodes 512 \
  --out /workspace/scratch/f6a2c7886477/newton-experiments/r61_segment653_real_replay.json
```

第二份报告只将 `--initial-label-imag` 改为 `1/512` 并指定独立输出。
外盘失败的首次尝试只把子段改为 `3/8`、`5/8`；它按设计拒绝写出
成功证书。所有依赖源及实际 shard 的 SHA 均另写在成功 JSON 中。
