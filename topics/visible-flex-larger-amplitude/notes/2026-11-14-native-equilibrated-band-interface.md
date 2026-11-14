# 原有限 native 矩阵的幂二均衡与精确残差误差修正

2026-11-14。独立入口：

`../computations/geometry_20261114_native_equilibrated_band_correction.py`

本地仅解析源码 AST；没有运行矩阵、整数残差、LAPACK、原 native 或任何科学数值。所有实际计算只用本公开仓库 Actions。原 capture、原 band、原 exact-row kernel、原 native 方程/容差/source bytes 不变。

## 1. 此次必要性与输入对象

真实 request28 捕获了同一非零 H、同一 577×224 基态的完整原 native J、残差、cut/far、原 scales 与原校正。真实 request34 用一般带状 partial-pivot LU 重解同一系统，虽然 `factor_info=solve_info=0`，其原尺度浮点缺陷仍约为 $4.1559\times10^{30}$，该行精确二进制实代数缺陷约为 $5.2938\times10^{30}$。因此它尚未给出可用的原 Newton 方向，也不足以支持重做十档原试步。

本次处理这一个具体线性缺口。输入只需已锁 request28 完整 capture：

- result SHA `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`。
- 全 J SHA `394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19`。
- 完整原数据由冻结 `geometry_20261114_native_captured_band_correction.py` 的 `CapturedArrays` 逐文件/逐 chunk 绑定；该源 SHA 为 `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390`。
- 全行整数核直接复用冻结 `exact_20261114_native_allrows_dyadic_residual.py` 的 `stage_job`、`boundary_job`、decode 和最大值比较；该源 SHA 为 `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f`。

没有新 J、新 flow、新 H、native worker、nonlinear trial、endpoint J 或 audit。旧数据仍只读；大阵不重新写入 Git。

## 2. 同一原系统与显式对角变换

令 $A\delta=-r$ 是 [R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md) 的完整保存数组系统。行依次为 cut 的 112 行、576 个完整 224 行 stage、far 的 112 行；列依次为每节点全部 Q/Pi。stage 是

$$J_n\delta_{n+1}-\delta_n=-r_n,$$

cut 是 $\delta_{0,Q}=-r_c$，far 是

$$\delta_{D,Pi}-G_D\delta_{D,Q}=-r_f.$$

完整维数 129,248。原 far 是保存的 112 项对角 G；完整 J 稠密块、$-I$、两边界均保持，故带宽仍为 $kl=112,ku=335$，LAPACK 存储 560×129,248，约 579 MB。

新方案取整数指数 $\ell_i,c_j$，在实数层定义

$$R=\operatorname{diag}(2^{\ell_i}),\quad C=\operatorname{diag}(2^{c_j}),\quad
\widetilde A=RAC,\quad \widetilde b=-Rr,\quad\delta=Cz.$$

每个幂二对角都严格非零，因此这只是同一保存有限系统的可逆行列表示变化。原 $\sigma_n$ 没有被替换：所有质量比较始终回到原 equation order 的 $e_i/\sigma_i$。不将形成后的浮点矩阵当成与实数 $RAC$ 自动逐字相等；其形成误差单列，最终残差仍对原 A 读回。

### 初始化保持深侧节点尺度

对每个实际 binary64 $\sigma_n>0$，通过其精确 mantissa/exponent 选择**绝对距离最近**的幂 $2^{q_n}$；两个相邻幂等距时取较小幂。列初值在节点 n 的全部 224 分量取 $c_j=q_n$；cut/stage n/far 行分别取 $\ell_i=-q_0,-q_n,-q_D$。所以深侧很小的原尺度仍进入初始坐标，而非只从单位尺度开始。

节点指数及全部初始/最终行列指数保存为 `<i4` 文件。只保存整数指数，不先把极大/极小单独的 $R,C$ 生成为浮点数。

### 按真实原系数选择均衡指数

对每个非零保存 binary64 $A_{ij}$，`frexp` 给出精确整数

$$k_{ij}=\lfloor\log_2|A_{ij}|\rfloor.$$

因此在不形成 scaled 浮点矩阵的情况下，行最大项的精确 floor-log2 是

$$u_i=\max_{j:A_{ij}\ne0}(k_{ij}+\ell_i+c_j).$$

一次行步为 $\ell_i\leftarrow\ell_i-u_i$；再从同一原系数重读列最大指数 $v_j$，取 $c_j\leftarrow c_j-v_j$。每轮都保留实际各项、指数范围与步量。默认最多 3 轮；全行列步量均为零即停。精确零系数不贡献最大值，所有非零（包括 subnormal）均保留。

最终每项只计算一次

```python
ldexp(original_Aij, row_exponent[i] + column_exponent[j])
```

不会先形成 `sigma_next/sigma`、不会做先乘列再乘行的中间缩放，也不会因这些中间步骤先下溢。

`matrix_formation` 记录每项最终缩放的可逆 bit 检验、非零变零计数及实际示例。如果存在不能逐位反向恢复的 subnormal 舍入，报告如实保留，不声称完全精确的浮点变换；原 A 和整数指数足以重建全部形成误差。非有限形成值则退出并保留已完成诊断，不能交给 LAPACK 后静默传播。没有删行、删模或阈值截断。

## 3. 同一 LU 的精确原残差修正

均衡后只做一次 `dgbtrf`。初始解以及至多 3 次后续误差修正都用同一 `dgbtrs` 和原 pivot 数组，不再 factor、不再 J。

初始右端是保存原 $-r$ 乘对应幂二。得到完整 $\widehat\delta$ 后，全部 129,248 原行以精确 binary64 实代数计算

$$e=A\widehat\delta+r.$$

每个原有限操作数解码为整数乘二的幂；所有乘积在公共单位 $2^{-2148}$ 下精确累加，没有浮点 dot、阈值或遗漏非零乘积。原 $\sigma$ 也按其真实 bits 解码；跨 stage 的 $\max|e_i|/\sigma_i$ 用整数交叉乘比较，只有十进制显示使用四舍五入。

误差修正右端由精确 $-2^{\ell_i}e_i$ **一次 correctly rounded nearest/ties-even** 到 binary64，再解

$$\widetilde A\,\Delta z=\operatorname{RN}(-Re),\qquad
\Delta\delta=\operatorname{RN}(C\Delta z),\qquad
\delta_{new}=\operatorname{RN}(\widehat\delta+\Delta\delta).$$

这里的新浮点更新仍有恢复和加法舍入，所以每个完整候选都重新针对原 A 做全行精确残差。只有原 $\sigma$ 范数严格减小，才替换保留的 best；全原坐标 update 逐字节不变、范数未减小、显式预算耗尽或非有限更新均停止，并保留前一完整最佳方向及实际原因。此比较是线性求解算法选择，不是新 native 接受条件。

### 从精确 dyadic 到 binary64 的一次舍入

若精确数为 $m2^p$，令 $n=|m|$，选择

$$q=\max\{0,\operatorname{bitlength}(n)-53,-1074-p\}.$$

整数除法将 $n/2^q$ 按 nearest/ties-even 舍入成整数 $t$。其有效位不超过 53 位；唯一进位情况 $t=2^{53}$ 本身也精确可表示。之后 $t2^{p+q}$ 已在 binary64 正常或 subnormal 格点上，故 `float(t)` 和最后 `ldexp` 不引入第二次舍入；溢出显式报错，真实负数下溢到零则保存负零。精确实数零采用正零约定。不能先将巨大 $m$ 转 float 后再缩小。

每次全部精确 e、整数行指数与最终 RHS bits 都保留，足以重建本次右端舍入损失。该完整整数残差是误差修正所需计算，不是等待额外证书批准才允许原试步。

## 4. 输出、预算和下游兼容

默认资源预算：3 轮纯指数均衡、1 次完整 band LU、最多 1+3 个完整方向的精确原残差扫描、2 个整数 worker。每次完整扫描访问全部 28,901,376 个 stage 乘积位置与 112 个 far 乘积位置。若没有改善或更新逐位不变，立即停止后续修正。实际时间、RSS、每次残差进度和失败信息全部由 Actions 记录，不预设收敛。

每个候选保留：

- 全原坐标 δ 原始 `<f8` 及完整有符号零 checkpoint。
- 全 cut/stage/far 精确 e 的 gzip JSONL（每项为有符号十六进制整数和二进制指数）。
- 正确舍入后的完整 refinement RHS、各次原坐标增量。
- 精确原 $\sigma$ 全局最大、实际最坏位置及完整原 binary operand witness。
- 是否真正改善以及保留/停止原因。

最终对 best 再调用原冻结 band consumer 的完整普通浮点缺陷读回和精确最坏浮点行，保留与 actual28 原校正的同口径比较；这不是把浮点读数覆盖掉精确全行结果。精确全行结果只关于保存的有限数组，不自动是原非线性流精确导数，也不证明真实 trial 下降。

大阵统一在 `large-arrays/`，只进入 artifact，Git 保存小 manifest/hash 与有界 checkpoint。完整 J 不复制；LU 不写重复的大文件。每次 bounded direction checkpoint 另保存，最终兼容原 trial replay 的三件输入：`result.json`、`direction-checkpoint.json.gz`、`output-array-manifest.json`。

兼容 schema 仍为 `original-captured-native-full-band-correction-v1` / `complete-original-native-band-direction-v1`，但 `source_sha256` 明确属于本新源，`algorithm` 和 `scaling` 明确写新算法。不能用旧 B39 SHA 冒名。后继 trial 入口应显式给本 producer 文件名/SHA 和真实 result SHA。

所有输出保持 `native_accepted=false,task_completed=false,new_J_calls=0,original_native_calls=0,nonlinear_trials=0`。`diagnostic_completed=true` 只表示这次有限预算的线性运算与证据保存完整；它不会触发 native 试步。

## 5. Actions 命令

继续复用已经修好并明确来源的 actual28 artifact 下载步骤。`CAPTURE28` 是其 `native-correction-capture` 目录，保留原 metadata 与 `large-arrays`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python "$C/geometry_20261114_native_equilibrated_band_correction.py" \
  --capture-directory "$CAPTURE28" \
  --equilibration-passes 3 \
  --refinement-steps 3 \
  --exact-workers 2 \
  --out "$OUT/captured-native-equilibrated-band-correction"
```

出错也保留同目录中的全部已完成阶段、候选与 manifest；原输入目录不写入。实际结果返回后再决定下一步，不从源代码或 LAPACK info0 推定可用方向。
