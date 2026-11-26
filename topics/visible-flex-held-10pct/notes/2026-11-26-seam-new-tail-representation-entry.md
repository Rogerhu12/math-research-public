# 新 accepted 尾场的完整 shared-R 表示与认证入口

维护：Astra-held10-06bbeb39-20261126 / seam_geometry。

**状态：入口已写；源代码编译、独立多项式恒等式检查，以及使用实际同源文件的完整 R58 背景定义恢复已执行通过。尚未收到实际 accepted 新场，因此本文没有新增的 full-H、桥尾匹配、全尾连续误差或闭曲面数值结论。**

这组入口接原 native 包的实际保存状态、单条原均值链和已有 shared-R 导出方法，不复用 warm-.25 的非旋转场界。大数组、全部阶段数据和完整输出留在公共 runner；仓库只保存代码及实际执行后的小记录。

## 1. 数据入口与 warm 身份

新增脚本：

- [seam_restore_true_background.py](../scripts/resume_20261126/seam_restore_true_background.py)：同一 R58 背景定义的恢复与已付区间复用。
- [seam_export_tail_geometry.py](../scripts/resume_20261126/seam_export_tail_geometry.py)：新 accepted 包到原均值链、shared-R 全段和唯一节点索引。
- [seam_certify_tail_geometry.py](../scripts/resume_20261126/seam_certify_tail_geometry.py)：对新段实际重算连续界，并从新最深节点构造自己的 $C^2$ collar。

首先执行原 `seam_cut_height_compatibility.load_packet` 的所有原门：`response.converged` 为真、无 failure、有限非负 residual 不超过原 `config.solveTolerance`，该 tolerance 不放宽；实际 port、完整 background config、spacing/modes 和原 cut jets 一致。

入口另外要求完整 checkpoint states，以及

$$
\texttt{request.height}
=\texttt{checkpoint.cutHeight}
=\bigl(H_j f^j\bigr)_{j=1}^{24}.
$$

$H$ 必须来自指定 JSON 文件的指定字段，保存整个引用及 SHA；$f$ 必须显式给出。原主 continuation 使用 NumPy 幂，独立 recorded-height 入口使用 Python 幂，命令必须声明相应原算术，不用近似相等掩盖字节差。

$f<1$ 只标为 warm-scaled；$f=1$ 只标为**这个已绑定参考 $H$ 的未缩放有限尾候选**。它不自动证明该 $H$ 来自已接受的最终耦合前缀，不证明精确 DN，也不证明闭曲面。

此入口调用的原 batch exporter 当前固定 `M=24, quadrature=512, spacing=3`。更高维或不同角网格必须另立明确导出合同，不能通过删除检查混入。

## 2. 原 native 均值链与公共二阶节点

可以直接指定完成的 native record，也可以指定当前 runner 的 `native-runs` 目录。自动选择会逐个 stage 从原二进制 input 的已记录 offset 读取完整初值，与当前 accepted checkpoint 的 `states[stage+1]` **逐数完全匹配**；两个 mean 初始槽也必须正好为零。只有匹配以后才调用原
[extract_q060_native_mean_chain.py](../scripts/resume_n4/extract_q060_native_mean_chain.py)
执行完整文件 SHA、payload token 和输出协议核验。

均值链仍为同一记录从最深 stage 向 cut 的固定 binary64 累加顺序。扰动均值和背景原 primitive 是两个不同槽；不把扰动零模设零，不另行积分替换，也不把背景的 finite primitive 当真积分定义。

随后调用未改变数学内容的
[export_q060_shared_r_tail_batch.mjs](../scripts/resume_n4/export_q060_shared_r_tail_batch.mjs)：

- 不输入旧 warm-.25 的 anchor 或 previously-certified stage；
- 内部边界 $k$ 取外侧 stage $k-1$ 的内端完整物理 $R$ 二阶 jet；
- 每个相邻段复制**同一份**半径、值、一阶导和二阶导；
- stage0 的 cut 节点及最深节点都来自这次 actual packet；
- 平面 Fourier 模、全部高度模及原均值保持原表示；
- 原平面 FD 二阶值仅作为新 Hermite 映射的字面节点参数。

新 `canonical-boundary-node-index.json` 再逐项核验共同二阶数组、唯一节点数和原均值。所有段都导出时必须恰有 $S+1$ 个唯一边界节点和 $S$ 个段；每个段内部的完整 literal-R knots 留在相应压缩数据文件。索引引用这些数组而不将它们写进 Git。

上侧尾的高度合同是

$$
z(R,\theta)
=z_b-\bigl(h_{\rm R58}(R)-h_{\rm R58}(R_{\rm cut})\bigr)
       -\mu(R,\theta),\qquad
z_b=Z_c+\mu_{\rm cut}.
$$

这里 $\mu$ 包含整条原扰动零模及全部非零模。$Z_c$ 是新前缀自己的真实 cut mean primitive，不是旧 R60 的数值区间，也没有被人为设为零。

## 3. R58 背景只在完整数学身份一致时复用

恢复脚本从冻结原 factory 再生其 160 个有限 binary 校准常数，输入物理参数来自既有 reference binding。原 factory 和 dump 源码 SHA 先核验。再生成的 `parameters` 与 **全部** `cells`，连同记录中的历史 port/factory 定义标签，组成原 oracle 指定的规范对象，其 SHA 必须恰为

`e764e2cc370f0b7a8a55324f2744702017c16690195f45db92ca66b9781bae56`。

若不一致，立即失败；不修改目标哈希，不舍弃某个参数，也不把差异称作 roundoff 后继续。

一致时，真实函数、全部校准参数、真积分 integrands 与 R58 是同一个数学对象。因此可以复用
[2026-11-20-q060-tail-tight-integral-execution.json](2026-11-20-q060-tail-tight-integral-execution.json)
已经执行并完整保留的 $A,B,A_H,B_H$、真归一化、真高度区间。这一步不再计算旧全背景积分。

新记录明确区分：

- `checkpoint_sha256` 是原数学定义的历史 port 标签，**不是**新输入文件 SHA，也不声称旧文件已恢复；
- 新 input、原 dump 新 output、恢复脚本和新 constants 序列化分别有真实路径与 SHA；
- `source_sha256` 对 normalization 表示这些区间所属的原 proof kernel；新适配器另有 SHA；
- 原完整 proof output 的历史 SHA 只作为已执行来源，未冒称已经得到旧完整输出字节。

新 oracle 接收的是“同一定义的旧区间 + 新序列化身份”的诚实复用记录。所有非旋转段仍必须用其新节点重新认证。

## 4. 新全段认证及新 deep collar

新认证入口只复用原
[certify_q060_shared_r_tail_batch.py](../scripts/resume_n4/certify_q060_shared_r_tail_batch.py)
的 `certify(o,d)` 多项式/区间方法。原 main 中 warm-.25 checkpoint 的固定身份没有被转移到新数据。

每个新段都重新核验 source、packet、mean-chain、manifest、数组及 map hash，实际构造精确 quintic、逐项验证端点二阶相等，并对连续 $R$ 和全部角计算：

$$
\|g^{-1/2}(g_F-g)g^{-1/2}\|,\qquad
\|dV\|,\qquad
\|\nabla_g^2V\|,\qquad
|\kappa|.
$$

需要时仍用真 R58 背景 oracle 的连续半径 cover 和 Fourier 同频合并；不把 JS profile 误差当作已经支付。metric allocation 保持 $10^{-6}$，曲率 allocation 取现有总方案的 $10$。

最深 collar 直接取这次 shared-R 最深节点 $R_0$，其原两个 mean anchor 都必须为零。令固定 cuff 半径为 $a_0$，取

$$
R_i=(R_0+a_0)/2,\qquad L=R_0-R_i,\qquad u=(R-R_i)/L.
$$

用原右端 quintic Hermite 基

$$
H_0=10u^3-15u^4+6u^5,\quad
H_1=-4u^3+7u^4-3u^5,\quad
H_2=\tfrac12u^3-u^4+\tfrac12u^5
$$

构造 $\sum_{j=0}^2L^jH_j(u)J_j$。$J_j$ 是这次新场上侧完整 Cartesian 扰动 jets。外端匹配所有二阶数据，内端完整二阶数据为零，内侧只留同一个 R58 背景直至固定平盘。

新的 Fourier-Bernstein 界全用新节点算。法向差使用保守的通用估计：若背景正交切架中的扰动 Frobenius 界为 $\eta$，则叉积差不超过

$$
\tau=\sqrt2\,\eta+\eta^2/2.
$$

在 $\tau<1$ 时，两单位法向距离不超过 $2\tau/(1-\tau)$。这次没有搬用旧 collar 数字。

整个尾盘所有段及 collar 若都证明欧氏平面微分扰动小于 $1$，则平面投影在整个凸圆盘上单射：对任意两点沿直线积分，扰动距离严格小于原点距。该结论只涉及当前尾盘分量，不代替它与前缀的全局分离。

绝对 radius/support 仍明确以**新** $z_b\in[1/10,32/25]$ 为条件。报告不把这一条件写成已证明，也不把任何尾盘局部证书称为整张闭曲面完成。

## 5. 公共 runner 命令

全部 `WORK` 目录必须在 Git checkout 外。`SOURCE` 是与 accepted packet 绑定的实际 source topic，`PORT` 是同源原端口。

```bash
python scripts/resume_20261126/seam_restore_true_background.py \
  --source-topic SOURCE --outdir WORK/true-background

python scripts/resume_20261126/seam_export_tail_geometry.py \
  --tail-response WORK/tail_accepted.json.gz --source-port PORT \
  --native-record-dir WORK/native-runs \
  --height-reference WORK/prefix-run.json \
  --height-reference-key raw_return.candidate_H \
  --warm-factor 0.25 --height-arithmetic numpy \
  --stages all --outdir WORK/new-tail-map

python scripts/resume_20261126/seam_certify_tail_geometry.py \
  --geometry-bundle WORK/new-tail-map/geometry-bundle.json \
  --constants WORK/true-background/true-background-constants.json \
  --normalization-certificate WORK/true-background/true-background-normalization-reuse.json \
  --outdir WORK/new-tail-certificates
```

若只需立即支付 cut 修补和深锚数据，可先单独导出 `--stages 0,1151`；它仍清楚报告未覆盖整个尾。完整验收必须另实际完成所有段。

本次本地检查：三个脚本 `py_compile` 通过；18 条右端 Hermite 基端点恒等式、4 个精确平方根上界例子及零扰动的 R58 条件 placement 算术通过。

实际背景恢复另已完成：同源 factory SHA 为 `740e672…`，Node `v24.22.3`，入口 exit 0，用时 $4.124735$ 秒。全部 160 个有限校准参数和完整规范定义重新得到原 `e764e2…` SHA，随后 oracle 校验通过。新 constants 和 interval-reuse 文件分别有真实新 SHA，详见
[实际恢复小记录](2026-11-26-seam-true-background-restore-execution.json)。
这次只恢复同一个已证背景的定义及可用输入，没有重跑旧全积分或旧非旋转场认证，也未运行伪造 accepted packet 或新场替代品。
