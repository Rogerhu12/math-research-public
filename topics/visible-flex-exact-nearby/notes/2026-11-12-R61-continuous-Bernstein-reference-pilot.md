# R61 全初值角参考：连续 Bernstein 定义与严格有限界

2026-11-12。此 pilot 完成的是一个明确有限参考函数的连续复角界，
不是实际 ODE 残差或 KAM 接受。它服务于验证实现；下一准确参数点
应使用同一时间网格的完整射线，避免大量不同网格并集。

## 1. 参考函数的准确含义

从准确 δ₂=−15291006546051/9007199254740992 的完整258真实节点
forward dense 输出选择系数。构造脚本仅使用浮点运算选系数；
随后保存的每个 binary64 实部、虚部都被定义为准确 dyadic 数。
不声称构造前后的插值恰好相同，也不把构造舍入假设为零。

函数为 Y(τ,x)=x/4+U(τ,x)、q(τ,x)=exp L(τ,x)。U、L 在 x 上
是129次实 Fourier 多项式，在每个实时间段上是7次 Bernstein
多项式。正频率系数保存，负频率取共轭，零频率严格为实数。
偶数采样点数的 Nyquist 正系数减半，保持这个明确实 Fourier 定义。

共881段。首尾时间准确为 −π/2、π/2，内部时间是保存 binary64
数的准确有理值。每段使用这些准确时间定义 u=(τ−left)/(right−left)。
构造时只在相邻段共用同一个 endpoint 系数；逐位一致的 b₇、b₀
使 U、L、Y、q 在每个内部接缝准确连续。时间导数可分段不连续，
R61 的逐段积分允许这种情况。

## 2. 连续界的证明

设 cₖ(u) 的每个 Bernstein 顶点实部、虚部绝对值分别不超过 Rₖ、Iₖ。
实 u∈[0,1] 的 Bernstein 基非负且和为1，故
|cₖ(u)|≤Cₖ=√(Rₖ²+Iₖ²)。对实 Fourier 多项式，整个初值角 strip
|Im x|≤S 上有

\[
|\operatorname{Im}Y|\le S/4+2\sum_{k≥1} C^U_k\sinh(kS),
\]

\[
\min_j b^L_{j,0}-2\sum_{k≥1}C^L_k\cosh(kS)
\le\operatorname{Re}L\le
\max_j b^L_{j,0}+2\sum_{k≥1}C^L_k\cosh(kS).
\]

因此 |q|=exp(Re L) 的上下界也覆盖连续全时间和全初值角。
所有非平凡四则、sqrt、sinh/cosh/exp 由 Arb 192 bits 包围。
numpy 仅对有限输入作准确绝对值和最大值选择；未用普通 FFT
或浮点求和作为这些界的证明。

H 的 dyadic 整数系数与参考初值的准确差直接给
||H−4Y₀||_{A_S}，连同 q₀ 的模长下界支付 R61 初始半径。
本次 q₀=1 准确成立；输出为保持统一算法而给稍松的浮点下界。

## 3. 完整有限验证结果

| 归一角宽度 S | 全分段虚部绝对值上界 | 全分段 q 模长下界 | 全分段 q 模长上界 | 初值 Wiener 误差上界 |
|---|---:|---:|---:|---:|
| 1/512 | .001984404804 | .02916552679 | 19.12936940 | 4.078145e−15 |
| 1/256 | .003975292167 | .02889420180 | 19.30899977 | 4.663955e−15 |
| 1/128 | .008003221422 | .02781265273 | 20.05986776 | 6.204311e−15 |

表中数值刻意松于有向 JSON 的端点；q 下界向下取值。
所有880个内部接缝的 Y/L 跳跃严格为0。
即使 S=1/128，参考物理角虚部仍小于几何域宽度1/64。
真实流还必须支付 |q|R 的附加半径，不能仅凭这张表声称已在域内。

## 4. 冻结身份和复放

- 构造源 `scripts/fourfold_dense_fourier_reference.py`：
  05a4464394562068bac4ede64a1bcc1fa6363bf8afee97f11e16951eb7d222e9。
- 验证源 `scripts/fourfold_fourier_reference_bounds.py`：
  96fc0a9b2e75e2c84f080aefb6fb85b2101ab7410586462c63fa68f2ba784878。
- 参考 manifest `data/phase_ring_continuation/r61_step2_bernstein_forward/manifest.json`：
  2a76ac79b15f28aa3ea95f708d10e073b346e0c23809a0c8021d391c1c2a816a。
- 输出 `notes/2026-11-12-R61-step2-Bernstein-reference-bounds.json.gz`：
  f9a9c2161f6d2d2d824919d1218f86b61c071ba60082255914a365a4aa3cd1ea。

此探索参考共25MB，可由完整 frozen trace 的生成入口重做；按根数据规矩，
本次只存脚本、manifest、有限界及复放命令，不把所有中间系数分片入库。
重做时必须匹配 manifest 的每个分片 SHA，否则重新定义并重新验证参考。
最终真正用于 ODE 证书的参考应保存其必要分片，不能只存采样结果。

在本课题目录执行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/fourfold_dense_fourier_reference.py \
  --trace-dir data/phase_ring_continuation/exact_affine_step2_dense258 \
  --leg forward --rays 258 --basis bernstein \
  --out-dir data/phase_ring_continuation/r61_step2_bernstein_forward
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/fourfold_fourier_reference_bounds.py \
  --manifest data/phase_ring_continuation/r61_step2_bernstein_forward/manifest.json \
  --conjugacy data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_dyadic_H.json \
  --widths 1/512 1/256 1/128 \
  --out notes/2026-11-12-R61-step2-Bernstein-reference-bounds.json.gz
```

构造器拒绝覆盖已有 manifest，重放用空的相同相对目录或新的输出目录。
目录名也进入 provenance；若重放到新目录，应比较数学数组并重新记录
新的完整 manifest hash，不冒称元数据逐字相同。

实际待付的是同一参考的 e₀=Yτ−f(τ,Y)、e₁=Lτ−fθ(τ,Y)、
二阶场界、根与参数变化、两腿接续及完整 Wiener 端点误差。
