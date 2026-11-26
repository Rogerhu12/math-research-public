# R683 的完整幅度行应用：显式向内预算与实际修正步

本文是 [R683](../results/R683-all-old-row-constrained-second-order-correction.md) 的完整实现应用说明，不重复登记该命题，也不把数值内缩参数登记为新可行性定理。本文交付完整小源；实际科学计算只由本公开仓库 Actions 执行。作者端仅作源文件构造、AST/compile 和字节身份核对，没有新增数值 fixture。

## 1. 这次修复针对什么

[实际 mean ray / all-row SOC 归因](2026-11-26-actual-mean-ray-and-all-row-SOC-attribution.md) 记录了两个不同问题：新的 moving-mean 方向整步真实目标下降，却被原曲率点筛截步；旧固定目标的全部 192 行 SOC 已把原全步的 reach product 从 `0.9920002900532436` 降至 `0.9920000000863105`，仍略高于原 `0.992`。后一结果说明原 `tau=0` 修正没有支付严格向内余量。它没有授权放宽原真实阈值，也没有证明所有潜在极值已经进入当前有限工作行。

当前入口因此同时提供：

1. 对全部原曲率行和新幅度行作同一次 R683 半空间修正；任何原 C 行都保留。
2. 只在真实整步、完整物理筛查拒绝后，按明确政策加入正内缩量。
3. 可选择把该次真实拒绝暴露的最坏曲率/直径组合及真正违反的幅度极值，重新在原父场求值和求完整导数，追加到 SOC 行族。
4. 对修正后的方向重新计算同一父的完整 `A z`，再独立读取其真实目标、全部网格和永久物理位置；不借用原方向的下降预测。

这些措施不增加原 QP 的迭代预算，也不更换 R688 当前 mean 粗 Gram、R685 活动面预条件器、原自由变量、母范数或阻尼单位。

## 2. 全部 typed 行的固定父定义

设原父为 `x`，完整原方向映射为 `T`，原 QP 方向为 `d`。对每一个原父有限不等式，固定父归一化 `n_i`，记

\[
c_i(z)=g_i(x+Tz)/n_i,\qquad C_i=Dg_i(x)T/n_i,
\qquad b_i=-c_i(0).
\]

原曲率乘积行保留其精确地址、主曲率分支和原半径搭档：

\[
g_i=\rho_{\rm reach}D_{r_i}|\kappa_{q_i}|-s_{\rm num},
\quad n_i=\|T^*Dg_i(x)\|.
\]

这里 `s_num` 仍是原数值阈值，例如 `0.992`；行中的直径搭档不会在读取该行时偷换成新的全局最大值。

幅度行用[完整 D/L 约束](2026-11-26-fixed-DL-whole-image-amplitude-constraints.md) 已给出的 `g<=0` 定义：body diameter、两支 witness distance、固定 R 的 cap diameter 和 H floor。新场的 `p_current` 每次由全部当前 core 系数重新计算；导数保留原自由 core 前缀额外项，之后整体经过原 `T*`。每个非零导数行用其父范数归一化；零导数行以 scale=1 保留，不因其零导数而删除。

完整 `C,b` 是实际 QP 刚刚使用的 mmap 和逐行记录。新 helper 不把幅度 `g` 冒充 reach product，不把新 schema 伪装为旧 R683 构造器输入；它独立绑定新 typed schema，仅复用原已刊 R683 半空间投影代数与纯地址验证。

## 3. 内缩修正应用的是原半空间命题

令 `r_i=c_i(d)` 为整步在固定父归一化下的真实逐行值，选

\[
\xi=\tau\|d\|^3+\theta\max_i\max(r_i,0),\qquad \tau,\theta\ge0.
\]

新入口要求这两个政策参数至少一个为正；首个建议执行配置为 `tau=0, theta=1/8`。该 `theta` 是明确的数值向内预算，不是已认证的 Lipschitz/MFCQ 常数。

以同一完整矩阵解

\[
\min_e\tfrac12\|e\|^2\quad\text{subject to}\quad
C_i e\le\min\{b_i-C_i d,\,-r_i-\xi\}\quad\text{for every row }i.
\]

R683 的纯代数立即给出 `C(d+e)<=b` 和 `r+Ce<=-xi`。这里适用的是一般有限 `g_i<=0`，并不需要行满秩。原双对偶坐标下降保留依赖行，并用真实 C 重建和直接复读；没有可行有限迭代，只报告数值预算内未获得修正，不推出几何不可能。

真实非线性可行性还含余项。若每行梯度在相关邻域 Lipschitz 常数不超过 `L`，则

\[
c_i(d+e)\le -\xi+L\|d\|\|e\|+\tfrac L2\|e\|^2.
\]

要由它直接认证可行，必须另付所需常数及局部假设。本文没有完成这些责任；`theta=1/8` 本身也不完成这些责任。实现因此始终保留原真实筛查，既不松 `0.992`，也不松幅度的 `g<=0`。

原 QP 的数值可行容差仍原样使用；它只用于候选半空间直接复读，不成为非线性验收容差。修正后逐 typed 行物理读取不完整时，helper 不返回可用候选。

## 4. 真正暴露的新极值怎样追加

`soc-separation=rejected-extrema` 时，追加地址来自这次完整真实拒绝记录，非预测的活跃点：

- 若原曲率筛拒绝，取其实际最坏曲率地址的两个分支，配实际主导直径搭档；若独立绝对曲率 cap 已明确启用，再保留该处两个绝对 cap 行。
- 对 body diameter / witness plus / witness minus 中真正正值的幅度极值，追加其确切 typed 行及 witness 符号。
- 所有新值和梯度均在同一原父 `x` 计算，包含完整原物理 pullback 和原 `T*`。每个旧行和旧 bound 原样复制到新 mmap 前缀。

新 parent bound 若为负，扩展明确不可用于“零步可行”的原 QP 声明；该次 SOC 不可用，记录需要真实 restoration 或合格父。原方向回溯若继续，任何接受候选仍须真实通过已经扩大后的永久位置全集。旧行未删除，新的负 bound 不被裁剪成零。

真实极值及幅度工作点在拒绝后同样进入永久位置集合。当前父或末态若永久集合计数发生变化，沿用完整幅度 driver 的重新读取规则。有限分离只覆盖此次报告的有限极值，不能冒充连续最大曲率或连续幅度证明。

若原曲率行数为 `m0`，追加幅度行数为 `a`，本次分离行数为 `s`，增广坐标数为 `n`，实际 QP C 为 `(m0+a)*n*8` 字节。若产生分离 mmap，另付 `(m0+a+s)*n*8` 字节；原曲率前缀缓存 `m0*n*8` 字节仍存在。driver 将这三项真实缓存字节逐方向记录，不把 mmap 磁盘大小称为 RAM 上界。每次分离最多增加两个曲率乘积行、可选两个绝对 cap 行及三个幅度极值行；当前实际新增数以返回报告为准。

## 5. 同父同目标的修正候选验收

原 QP 与其模型记录保持不变。若修正返回 `z=d+e`，新 driver 实际再调用一次 `A.matvec(z)`，使用同一父、同一完整 mean J/J*、同一正谱 Hessian 和虚拟 RHS `v`，得到

\[
s_z=v^TAz,\qquad \Delta\Phi_{{\rm model},z}=2s_z+\|Az\|^2.
\]

阻尼只进入原正则 QP 模型；没有被塞入真实 Phi 的下降值。真实修正候选以其自己的 `s_z` 检查严格下降和 Armijo，之后检查完整原曲率与幅度屏幕。原方向与修正方向的 trial index / update kind 分开保存。

接受修正时，保存实际修正 bundle、修正的独立模型预测和实际收益比。只有实际接受的全步且其同一步收益比超过原阈值时，才沿用原减半阻尼规则。若候选不可得或真实读取拒绝，仍从原 `alpha=1/2` 继续原 `d` 的回溯。该修正不冒充已解决 inner QP 的 stationarity；`iteration_limit` 仍原样记录。

新增 `A`/`A*` 入口计数来自实际计数器差值；预条件器的原计数不改。生成源时没有数值计数结果，也不宣称实际加速。

## 6. 完整可执行来源

全部源位于 `scripts/resume_20261126/`；下表身份为作者端静态构造完成时的完整字节 SHA256。

| 文件 | SHA256 |
|---|---|
| `complete_amplitude_rows_soc.py` | `734c1fcc80006e7da52ea7aa8cda4dea02e75714b4b550c20f64dae9cfe67061` |
| `derive_mean_amplitude_complete_soc.py` | `e731954fa5e62ec7b6bb7098f993fcc00ba03e9e924e15f7ea1d64472419d0a4` |
| `fullclosed_mean_amplitude_complete_soc.py` | `3adccbbef31545df8c33bc5144da6db4adb34549300c60da4de6789602b38a11` |
| `launch_mean_amplitude_complete_soc.py` | `954e9c94edac24a984c99a2439608b490b8327a669cbf94394de88208060f494` |
| `read_mean_amplitude_complete_soc_report.py` | `9cd0e0f06fb7cb5b5cb97352c17595b6a80f5f681b220d3b90955955b3a202fb` |

完整新 driver 由真实修复后的 amplitude v2 全体 `970f03ad...` 派生，而非旧失败的 `ae6fbf5e...`。其 source deriver 逐锚点验证原完整 bytes，再绑定完整生成体；报告使用独立新 schema。下游不得把该报告 relabel 成旧 R683/R688 构造来源，也不得从未验证的嵌套 provenance 顶层猜一个物理 source SHA。

launcher 保留完整 parent report 与 manifest 位置并集、同一 carrier / scalar / eta / lambda 绑定和幅度预算不放松检查。可显式给 `--damping`，或用 `--damping-from-parent` 从该实际完整 parent 的 `final_damping` 读取，并核对实际最终 bundle、mean averaging 和 p/epsilon/scale 单位。新纯 reader 使用本 source deriver 检验全体新源，归因原 QP、最终活动面、分离行、修正半空间、真实修正失败位置及同一步下降；不读 raw 科学数组，也不运行场/J。

## 7. 剩余责任

只有真实 Actions 返回能说明这个分支是否产生可接受修正、是否减少截步，以及实际成本是多少。当前仍未补齐连续 metric 误差、reach、全相位 held/E3、固定最终 g 的精化或完整闭合等距结论。旧 R671 source guard 不允许此 helper 自动跨到新 deep scalar 物理分支；若后者需要 SOC，必须独立绑定其真实物理定义及完整导数来源。

## 8. 实际选择的首父和完整排程

首父不是预计未来输出：run45762076394 stage51–53已经返回v2最终场 `643627931a699a9f9a9e928ca5a6e4a61bd7855eafeaaf5b6fb434db92f0eeaa`、完整原报告及其自己的全922first，见 [真实结果](2026-11-26-actual-amplitude-v2-directions-and-own-first.md)。本次完整请求保 [参数](../computations/resume-20261126-amplitude-complete-SOC-first-steps.json)，1×64、原mu由真实report读取、tau0/theta.125；失败v1新位置manifest也显式保留。后接独立纯报告归因及新最终场自身first。三个本次新生row缓存目录仅自然返回后按明确路径清理，不删除raw最终场/报告/输入。这里仅刊完整源并排执行，未预报SOC会接受。
