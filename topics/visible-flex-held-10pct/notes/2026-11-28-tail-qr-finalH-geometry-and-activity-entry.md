# 真 QR final physical-H 的绝对几何与完整三阶活动矩接入

状态：**七个独立入口已实现、编译和 help 实测；没有新的 λ1、几何、矩或非全等阳性结果。**
这些入口只消费真正新 QR/native4/chord3/8outer 的最终 physical-H，
不继承旧 λ=.002 的 R82/R90 数字，也不改变旧源码/旧报告。

## 1. 已具体修复的来源缺口

旧 `tail_actual_placement.py` 的高度校验明确使用
`raw_return.candidate_H` 和旧 `reference.source_run`。
旧 `closed_map_marker_cylinder_geometry.py` 明确拒绝
`source_tail_is_actual_coupled=True`，并锁旧 raw-H map/source 和 width=.12。
旧活动矩聚合又锁 `actual_original_R53_design` 与 phase=9/20。
它们是合法旧输入合同，不能通过改 label 接收新的 final physical-H。

本条增加独立源，所有科学入口先经
`qr_actual_coupled_prefix.accepted_coupled` 或其
`qr_coupled_prefix_continuous.CoupledContext`。
因此新 source_kind 固定为
`actual_lambda_one_qr_chord_final_physical_height`，
仍核完整原 source/raw/physical/native/config/全 H/state/J/audit、
真正 λ1 和 original 8outer 全部验收。
其 H 定义唯一为最终 physical endpoint binding 的 `candidate_H`；
raw H 只作为原始来源另列。

### 绝对位置：qr_tail_actual_placement.py

原 zcut + 整条 native mean + R58 真实总高程积分的公式原样保留。
新的 cut summary 和 defining-table report 都必须通过同一个
CoupledContext.require_report；其中真实 final physical-H binding、packet、
mean、source 全同。
完整 bundle 的 height-reference 必须恰是该 endpoint binding/key=candidate_H/factor1，
不是仅比较某个采样高度。

半径证明必须来自新 `qr_complete_tail_radius_identity.py`，
其同场 QR gate provenance 必须准确一致。
只有实际 c−Rc=0 的已完成全 bundle 才能用这个 identity 路径；
若新输入不满足，仍须单独支付真正的半径变换，不能钳值为零。

其余原完整 stage receipts、deep collar、平盘、法向偏差、原绝对半径、
支撑和曲率转移原样执行。旧 K<10 预算 false 字段仍保留。
新阳性只能由新全套真实证书产生，不复制 R80 的旧上界。

### 数值查询：qr_closed_map_numeric_report.py

固定真实数学图仍是 `qr_actual_closed_map.py`
SHA `57b39a97d9d5abcd3ae7dfb17697addb67a8094efba375996ea268a44068d92b`。
独立包装沿用已实用的 NumPy longdouble→JSON 展示修复；
只将有限、不会下溢为零的诊断 scalar 转成 Python float，
并单独保存 rendering source、真实 argv 和转换次数。
不会把这些展示数值称为向外舍入上界或连续证书。
`--help` 不触发构造或写入。

### 全时几何：qr_closed_map_marker_cylinder_geometry.py

同场新 cut、完整 placement、完整原尾几何证书、真 map query、
全谱/mean/公共两jet和 exact radius identity 必须一起匹配。
query 明确要求 actual coupled=True 及同一完整 QR gate provenance；
数学图源码固定到上述真实 QR 版本。

旧 width=.12 的特殊硬锁改为**三个实际来源的同一正 cut width**：
query、cut proof 和 absolute-height 全部准确相等。
这没有降低任何 metric 或几何门，也没有声称任意宽度已被证明。
新输入仍须真的完成该宽度的 cut 证书。

CLI 必须显式给 `--phase-end`；R87 使用 `4/5`。
原正柱长 0<ell≤1/100、canonical R67 正帽、真平盘高度、全支撑、
曲率、直径和 reach 转移均原样保留。
这些局部几何界对全部相位不变，故覆盖这个完整时间域；
共同握持刚体校正保持这些量。
是否 reach/D>.03 仍由实际新标量判断，
不因 source_kind 正确就把比例验收写成真。
握持直径/位移和固定问题收敛仍由相应证书另外支付。

## 2. 完整三阶活动矩与 E(3)

### qr_tail_third_activity_flux_bound.py

保留原完整投影单射、真实水平半径 r*、真实绝对高度 Z、
完整有限尾/deep/平盘的全部前提；再补严格同一个 QR final-H 绑定。
上下反射已经包含在
`2*z*Re(w^3)*(Xpsi_x*Xs_y-Xpsi_y*Xs_x)` 中，
故仍原样支付

$$
|A_{3,\mathrm{tail}}| \le \frac{4\pi_+ Z r_*^5}{5},\qquad \pi_+=22/7.
$$

没有重算旧几何多项式或真实背景积分；
未来使用的是新场自己的完整证据。
固定标记帽贡献不在这个活动尾界中。

### qr_cartesian_third_activity_moment.py 与 durable 入口

完整 prefix/core 的字段、D2 积分密度、径向 midpoint 误差、
完整角梯形误差、三重周期因子、上下反射因子和单覆检查
与已冻结 `analytic/chord_cartesian_third_activity_moment.py` 完全相同。
唯一源适配是改用新 QR CoupledContext。
所有原 Fourier 模、有限 mean、中心 lift、真实完整 cut correction 都保留。

正式运行用 `qr_cartesian_third_activity_moment_durable.py`：
真实 core 区间算完即写小 summary；
每个真正完成的径向贡献都落 flushed/fsynced journal，
保二进制64累计区间端点的 hex 和准确有理表示。
它不把部分域或中断状态写成全域已完成；
后继若需恢复，已完成贡献有真实可核的保存记录。

### qr_combine_closed_third_activity.py

严格核同一个真实 prefix 全域矩、tail 界、固定 canonical cap 与柱长。
逐叶核准确径向单覆，再以 Fraction 重加真实区间端点；
得到

$$
A_3(\ell)\in[A_{3,p}^-,A_{3,p}^+]
 +[-E_T,E_T]+\ell[m_3^-,m_3^+].
$$

当前柱长用 query 里的**字面 binary64 半长乘二**，
不偷换成名字近似的 1/200。
相位范围读已证明的完整几何 `phase_interval_exact`；
R87 因而仍为 [0,4/5]，没有残留旧 9/20。

只在完整区间严格排除零且固定帽 B3>0 时，
才据 R67 的最高权/最高频率论证登记含反射的 E(3) 非全等。
新区间若完全为负也可以证明非零，代码如实记录 sign=−1；
R67 的非恒定性只需 A3≠0，不额外要求其正号。
若区间含零，结果仍只是 enclosing，没有 δE 阳性。
这里不声称指定端点一定不同，也不提供尚未计算的定量 δE 下界。

## 3. 实际检查与源码

首轮七源 compile/help 实际全 return0；
随后只增加 source 身份两处严格检查的两源又编译/help 真过。
最终完整记录
`held10-design-work/qr-finalH-geometry-entry-check-20261128/current-source-checks.json`
SHA `60966e75a578a77e6d5932d7e9d3f14e08d4e8ee5636225c54391b7daf741b2f`，
配套仓库小 JSON 逐字相同。

还实际核了 15 项原数学段/函数的逐字或 AST 等价：
真实高度 primitive 与 scalar placement、全部逐 stage/deep 几何 receipt 转移、
帽/柱/全时 support/curvature/reach、
完整投影尾矩不等式、全部原 MomentVerifier 和积分函数、
完整径向覆盖/准确活动矩累加。
记录 SHA
`67cd05a4090c57322b38c62b35b29e24d92c164172a7630bcb4f458bd046ff43`。
这是源码等价检查；没有用它替代未来的真实新输入计算。

所有新增文件位于 `scripts/resume_20261128/tail/`：

| 源文件 | SHA-256 |
|---|---|
| `qr_tail_actual_placement.py` | `ff9928e281c5c7d541c2d9e994908117dfe9f21db953a20c21f2e66f19cf7be2` |
| `qr_closed_map_numeric_report.py` | `7e10f4e7ebdcae188c94be42889fe2990d1e08dd36b66474200a14deb66c5b4b` |
| `qr_closed_map_marker_cylinder_geometry.py` | `6ae95abb2341a7edf80c340c47fb53f29ae2097cb0813a46951b121c1b10ed5d` |
| `qr_tail_third_activity_flux_bound.py` | `987222cc93099100cbaef63c2388cfb931b877dcaa67a361996353470dc8b530` |
| `qr_cartesian_third_activity_moment.py` | `33143db55427c527b7e5bea9916009a0d484f95cc1dfcfd60b0a7039b322e164` |
| `qr_cartesian_third_activity_moment_durable.py` | `a5fad89bcaf381261a554ae43c89bd44e50b1c7c8b6423d61bb6fca8522719bd` |
| `qr_combine_closed_third_activity.py` | `af6059bc941c7eba594a104673246c4af886caf21ac93c0b40b92a407359ee98` |

## 4. 真输入到来后的调用关系

共同输入为 `<run>`=真正 QR coordinator.result.run，
`<coupling>`=该 coordinator summary。
完整新 bundle 由 fresh chunk 入口产生，
连续前缀/cut 和 table 来自同一个
`qr_coupled_prefix_continuous.py`。
后续按同一场顺序调用：

```text
qr_complete_tail_radius_identity.py verify
  --source-run <run> --coupling-summary <coupling>
  --geometry-bundle <bundle> --constants <constants>
  --normalization-certificate <normalization> --outdir <new-radius>

qr_tail_actual_placement.py
  --coupling-summary <coupling> --geometry-bundle <bundle>
  --constants <constants> --normalization-certificate <normalization>
  --cut-summary <actual-new-cut-proof> --radius-identity <new-radius/radius-identity.json>
  --original-summary <actual-stage0-certificate>
  --original-summary <actual-remaining-certificate> --outdir <new-placement>

qr_closed_map_numeric_report.py
  --source-run <run> --coupling-summary <coupling> --geometry-bundle <bundle>
  --cut-width <same-certified-width> --cylinder-half-length <actual-half-length>
  --canonical-r67-marker --out <new-map-query.json>

qr_closed_map_marker_cylinder_geometry.py
  --coupling-summary <coupling> --phase-end 4/5
  --cut-prefix-report <actual-new-cut-proof> --placement-report <new-placement/summary.json>
  --complete-original-certificate <actual-complete-tail-certificate>
  --full-map-query <new-map-query.json> --outdir <new-whole-geometry>

qr_tail_third_activity_flux_bound.py
  --coupling-summary <coupling> --placement-report <new-placement/summary.json>
  --complete-original-certificate <actual-complete-tail-certificate>
  --outdir <new-tail-flux>

qr_cartesian_third_activity_moment_durable.py
  --coupling-summary <coupling> --tables <actual-QR-table-report>
  --bundle <bundle> --cut-width <same-certified-width>
  --radial-parts 1 --outdir <new-complete-prefix-moment>

qr_combine_closed_third_activity.py
  --coupling-summary <coupling>
  --prefix-moment-report <new-complete-prefix-moment/summary.json>
  --tail-flux-report <new-tail-flux/summary.json>
  --closed-geometry-report <new-whole-geometry/summary.json>
  --out <new-closed-activity.json>
```

均从本目录以 `python` 执行；全部实际证书/数组保存在仓库外。
placeholder 不是已存在阳性文件。
旧 `closed_map_complete_metric.py` 的完整 inventory/同场聚合公式不锁 raw-H，
可以消费新同场 geometry 与新完整 finite metric supplement；
只有它要求的全域真实证明返回后，才会有新的整闭图 metric 结论。
后继 fixed-g 精化仍需真实运行，不由这些来源适配自动支付。
