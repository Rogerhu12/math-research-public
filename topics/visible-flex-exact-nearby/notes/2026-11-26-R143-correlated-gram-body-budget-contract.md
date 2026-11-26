# R143：全4651片相关 Gram 新目标

2026-11-26，`visible-exact-astra-198c63d15049-20261126 / correlated_energy`。

科学源为 `scripts/fourfold_codazzi_correlated_gram_body_budget.py`，
数学依据是 [CV.1–CV.5](../results/R138-supplement-correlated-v-eta-four-vertex-body-Gram.md)、
[SG.14–SG.17](../results/R138-supplement-complementary-Gram-spectral-body-energy.md) 与
[R143 OC.1–OC.5](../results/R143-correlated-body-energy-and-optimal-root-screen.md)。
这次计算只改变同一能量的包围方法，不改变实际 $Q_{repair}$、固定 $\eta_0,\nu_0$、
完整 moving mean、物理角、真根、原4650正片与3594接口。

## 1. 新目标与方向

| 保存记录 | 完整数学目标 | 方向 |
|---|---|---|
| `C_correlated_upper` | 全4651片 CV.5 四角点最大值；完成后才与旧 SG 整球 upper 取 min | upper |
| `wE_correlated_upper` | SG.14，以新完整 $C_{corr}$ 代入 | upper |
| `aEE_correlated_upper` | SG.15 的新 E 平方体费 | upper |
| `aEB_correlated_upper` | SG.15 的新交叉体费 | upper |
| `optimized_root_necessary_upper` | R143 OC.5 的最优非负方向必要测试 | upper |
| `root_allowance_correlated_lower` | 仅 body 三门都严格为真时的 SG.17 半余量 | 条件性 lower |

前五条全部保存读回才称完整。body 门 false 时仍完成五条 upper 并保存 false；
不产生条件性 lower。必要测试的 upper 不大于零才排除当前 CV/RA 非负费用格式。
正值只表示这条必要测试未排除，不能推出真实根型、全频逆或闭曲面存在。

## 2. 完整只读来源

原输入恢复沿用既成 SG 的 positive4+germ1 精确历史定义：

- positive native SHA256 `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`；
- true-root germ SHA256 `397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864`。

当前完整 X/Y/GB/RS 的 actual/execution 仍为既成 SG 合同里的四对，均整读、核原
身份与成功/失败资格。新增的旧 SG actual/execution 是 run **44767124478/1**：

- actual SHA256 `24c5923eb7a0b34c566c785ec11e33e7881b3ce6c35613a60cb9532238cf1b5e`；
- execution SHA256 `ce2787cd11267f3d47dcbab8f2dd76851ca64ebec09a72767bac313235f7438a`。

旧 SG 通过的 body/必要门与 RX 的独立排除都保持原资格。只读旧 SG 的
`C_spectral_upper`作为同一谱常数的完整另一个 upper，不执行 SG.12。
其他旧 CE、漂移、曲率、mean、Fourier norm、残差、容量、积分和根迹目标不重算。

## 3. 有向实现

完整原球先按旧 X/SG 加入原 pair 修补 $4\cdot10^{-18}$：$U,V,m_+$加，
$v_-,m_-$减，$\gamma,K$保持 intrinsic 原球。$m_->0,v_->0,\gamma_->0$逐片严格检查。
第一 germ 仍只支配真正根右侧；body 原 $K>0$ 与完整 mean 保留。

对每片的两个完整 $t=\gamma m$ 端点及两个 $r=|v|$ 端点，求

$$
M_r=1+U^2+K_+r^2,\qquad
\Delta_r=(1+U^2-K_+r^2)^2+4U^2K_+r^2,
$$
$$
\operatorname{upper}
\frac{M_r(t+t^{-1})+|t-t^{-1}|\sqrt{\Delta_r}}
 {2(2/5)r}.
$$

同一个 $r$ 同时出现在 $M_r,\Delta_r$ 和分母；不把分母另改成 $v_-$。
320-bit Arb 对整个式子作区间算术；先保持完整表达式再取最终 upper。
判别式采用非负和，不以独立端点替换 $K_+r^2$ 的各次出现。
全部4651片完成前不与旧完整 SG 取 min；每64片和最后一片保存真实累计最大值。

随后 SG.14–SG.15 的三条新常数都用上游保存整球的 upper。
R143 OC.5 则用保存 $a_{EE},a_{EB}$ 和旧 $a_{BB}$ 的 lower：

$$
N_+=\operatorname{upper}
\left(\frac{23}{30}-a_{EE,-}
-\frac{a_{EB,-}^2}{4(1-a_{BB,-})}\right).
$$

旧 GB 完整球保证 $a_{BB}<1$，所有费用非负；这正好向有利预算方向放宽。
不把保存 upper 的数值 lower 说成实际残差的 lower。
条件性 allowance 仍完整保留原 $r_E,r_B$，分子用 determinant lower，分母用
完整 upper，且只在两个对角与 determinant 三门严格为真后形成。

## 4. 运行与输出

CLI 的13项是

```
--positive --germ --physical --physical-execution
--composed --composed-execution --body-budget --body-execution
--root-screen --screen-execution --old-spectral --old-spectral-execution --output
```

`admit_inputs`/`admit_saved_budgets`只做原字节/JSON/身份/分区检查；科学算术只在
公开 Actions 的 `run` 内。唯一新目标 kind 为
`R143_complete_correlated_Gram_body_budget_v1`，完整输出
`correlated-gram-body-budget.json`。原27顶层字段保留，new_records数为5或6；
原四个旧输入对加旧 SG 对均在 whole references 中保留。

RN.15 的三个严格必要比较使用 $C_{corr}<23,w_E<22,a_{EE}<23/30$。
其通过/违反与最优二维测试分开记录；没有把必要比较赋成充分条件。
`positive_inverse_proved`、`root_boundary_form_paid`、
`actual_positive_boundary_problem_singular`、`final_topic_complete`均保持 false。

本地仅允许静态源码、元数据和证明工作；没有本地科学求值。
worker 复用既有同步/历史恢复/不重算/失败前缀保存方式；不保存任何新数组、
artifact 或 Release。新科学结果只保完整小结论、输入参数、run 与哈希。
