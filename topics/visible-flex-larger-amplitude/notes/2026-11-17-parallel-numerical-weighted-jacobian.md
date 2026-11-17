# 完整加权尾 Jacobian：卷积与零模梯度运输

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。本条给出已经实测的有限方程求导实现；它没有新增大幅解或几何通过结论。完整方程、实际旧小参数接受场和物理角规范见 [加权尾运行](2026-11-17-parallel-numerical-weighted-phi-tail.md)。

## 完整零模行没有省掉

令 `m(y,z)=Q_N(rho B)`，`g=grad_y m`，完整有限速度为 `F`，且 `z_x=2 ell z`。前 `2M` 行仍为完整 Ptilde 方程与完整 K 方程的字面有限投影。它们的 Jacobian 由四个点态偏导与 DFT 卷积得到；所有索引按 N 取模，保留实际有限采样的 alias，未删非线性乘积或物理高模。

最后一行满足 `g.F+2 ell z m_z=0`。对每个状态坐标求导、使用 Hessian 对称性，得到

\[
 J_{c,j}=-\frac{D_{(F,2\ell z)}g_j+
                  \sum_{a<2M}g_aJ_{a,j}}{g_c}.
\]

新实现用一次点态 complex directional derivative 计算梯度运输，再用 FFT 得到所有状态坐标的运输量。它代替对 `2M+1` 个全局状态逐列运行完整 RHS。`g` 是 `Q_N(rho B)` 的字面梯度，包括 `rho_phi` 与完整 weighted 均值；没有把加权 Kbar 或 T 的均值当零。此处也没有使用沿接受解的数值差分来替代 Jacobian。

源码：[fast operator](../scripts/parallel_20261117_weighted_tail_fast.py)、[全行比较器](../scripts/parallel_20261117_weighted_jacobian_check.py)。原逐列 complex-step 实现保留，可由 BVP 的 `--fast-jacobian` 显式选择新实现。

## 真实输入的三态比较

输入是已接受的旧物理 M8/N512、lambda=1e-7 四 cell 场，SHA256

```text
ca2dcbd728446dbec42326e1e8cd4f4e826cefe9c80109781ef2378f6fec8715
```

背景 SHA 为 `362509077ff7b1ce5011c838b73b5de056ced76257295be5ca53d5e6ddb357ce`。取其实际节点 `0,1945,3889`，使用同一实际 source-index 坐标和相应 `(s,ell,z)`。M112 比较仅把这三个局部 M8 状态零填充到 M112，**不是**接受了一个 M112 BVP，也不是谱精化证据。rho 始终保留原 core 全部 112 个系数。

| 比较 | 全矩阵相对 Frobenius 差 | 最大绝对差 | 零模整行相对差 | 逐列 / 新实现秒数 | 本次加速 |
|---|---:|---:|---:|---:|---:|
| M8、N512、17 状态 | 4.58343e-16 | 3.63798e-11 | 2.34489e-15 | .0191851 / .00232412 | 8.25 倍 |
| M112、N2048、225 状态 | 1.09062e-14 | 1.26996e-8 | 1.50060e-12 | 1.97876 / .0115245 | 171.70 倍 |

在写独立比较器之前，同一 M8 三态测到 `.0121889 / .00155738 s`，即 7.83 倍；M112 测到 `1.86616 / .00950634 s`，即 196.31 倍。计时随并行负载变化，结论是这个具体 finite Jacobian 的实测成本下降，不能视为求解器整体时间或统一条件数保证。上表使用完整可复现比较器的重新运行，误差逐值一致。

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_weighted_jacobian_check.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-weighted-tail-d4-m8-scale1e7.json.gz \
  --background /workspace/scratch/16f63c8bce6b/parallel-prefix-tail-d4-s64-w06-k6.json \
  --modes 8 --angles 512 \
  --out /workspace/scratch/16f63c8bce6b/parallel-weighted-jacobian-m8-repro.json
```

第二行比较仅将 `--modes 112 --angles 2048`，并将输出改成 `parallel-weighted-jacobian-m112-repro.json`。两个输出 SHA256 依次为

```text
f6aad07134c2598b056e1cfd5dcabb27990d6c3fabdde013ff93013a42e5b9ee
0881668fad173313d81f191658675b7d41fe5f5d6304e80b7c852382cb91540b
```

源 SHA256：

```text
parallel_20261117_dynamic_tail.py
e21034c9f1208506d16f1bed3cc46c470fdf15425c6466eb0f9623ad0fcfa8b5
parallel_20261117_weighted_tail.py
89c8d13add0d1930581269fde33e577804bc333afcf986a0837dfbae07f44c4d
parallel_20261117_weighted_tail_fast.py
6443424ecc791fe26c453935747d2fbd81d3df8528c0d4dda21f46ac6f890330
parallel_20261117_weighted_jacobian_check.py
53a5b24e7950460774818b095eeec32767d6cfabeb3ed3d89cd028ea0776e98a
```

## 同步实现的明确边界选择

本次保存的两个 BVP runner 还增加两个显式选项，默认行为保持旧定义。

`--deep-columns` 接受同一个背景、同一个深端 `(r,logw,mu)`、每个实际角频率的 homogeneous 列。它验证输入背景 hash 和频率，保留 u、v 而不在图 pole 除 u。材料版使用对应整数频率；物理版使用其完整广义频率，不将二者混用。输出中的 `deep_boundary.boundary_kind` 是本次边界类型的权威字段：`actual same-source finite far columns` 表示同源有限 far 传递。旧 `definition` 字串仍提及 ideal 函数，应结合该字段读；这不构成非线性无限尾 DN 证书。

`--allow-height-turn` 仅移除原额外 chart 条件 `y=1+K>0`，并保留 `S,D,L,N>0`。完整方程只除 L，均值导数 `Q_N(rho L/D^(3/2))` 仍严格正；几何变量 `a=sqrt(D/S)`、`b=-z y P/sqrt(S)`、`A_r=z y U/(r S sqrt(D))` 在 y=0 光滑。故它是显式扩大到原正根 chart 外的有限问题，不是假称旧 y>0 条件已通过。完整几何、嵌入和 reach 仍需实际检查。

两个 runner 在启动时记录完整依赖 SHA、deep-column SHA 和正确角规范的 height anchor。新源码随后用于真正的短桥接背景非线性幅度延拓；其接受与失败将另记，不把本条导数比较代替新解。
