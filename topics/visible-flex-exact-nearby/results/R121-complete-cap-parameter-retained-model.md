# R121：完整端帽参数覆盖及同族六维保留模型

2026-11-13，visible-exact-astra-ac0d。

**状态：已证明，并已实际运行全部区间计算。** 本篇关闭 R111 的原始报告恢复和全参数六维消费。它给出同一个参数盒上六维保留模型的统一逆界；核心仍是已认证的有限角 ODE，端帽使用完整无限维变分响应。完整核心高通道及其反馈 Schur 补没有由此关闭。

## 1. 同一对象和完整参数域

固定原准确仿射对象

$$
p_5=-\frac{7789843107295549}{4611686018427387904},\qquad
I=[p_5-10^{-9},p_5+10^{-9}].
$$

对象文件仍为 `data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json`，SHA256
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。
没有修改轮廓、目标平均度量、phase 系数或参数盒。

R111 的完整原生 producer 在 $[1/4,3]$ 使用复参数半径 $10^{-4}$、512 个 primitive 模、1024 个角节点、Arb192位；节点之间和全部无限 primitive 尾均由原证明包围。每一行分别覆盖完整实角与整个 $I$。

本次先保存198个已接受行的原样检查点：

$$
[1/4,\ 5212980234710965/9007199254740992].
$$

检查点没有 unresolved 或 pending 行；随后在同一 producer 的四个不重叠有理子区间重做剩余部分。四份完整续算分别接受303、280、269、259行，所有进程实际退出码为0。原 collector 逐行检查相同源码、依赖、对象、参数域、正性门和有理接缝，得到

$$
198+303+280+269+259=1309
$$

个 body 行准确覆盖 $[1/4,3]$。未从旧执行收据补出任何行。

同一 collector 又核对 main 上已经存在的322行自然 graft 证书、全部源和输入 SHA，并准确检查其联合覆盖 $[3,25/8]$。本次真实有向结果是

$$
\varepsilon_{\rm body}<0.001399180,\qquad
\varepsilon_{\rm graft}<0.001973601,
$$

所以对完整有限帽区和全部 $p\in I$，

$$
(1-\varepsilon)B_0\le B_p\le(1+\varepsilon)B_0,
\qquad \varepsilon=\frac1{500}.
\tag{121.1}
$$

这些小数均向外放宽原 Arb 上端点。完整合并报告为
`data/R111/ac0d_complete/complete_cap_parameter_comparison.json.gz`，SHA256
`02b2126762e9a3aff3313637aab97d3b7d7081826170e54a4d993e9acd7d9282`。

## 2. 同一个真实尾和全部 regular 端口

记 $C_{p,\Gamma_p}$ 为 R111 定义的完整正帽 DN form 在实际余弦/regular输入的压缩。对每个 $p$，比较中始终保持这个参数自身的同一个非负真实尾 $\Gamma_p$，包括其 mean 零核及独立的 regular trace/flux。

R111 的极小化比较由 (121.1) 给

$$
(1-\varepsilon)C_{0,\Gamma_p}
\le C_{p,\Gamma_p}
\le(1+\varepsilon)C_{0,\Gamma_p}.
\tag{121.2}
$$

旧 primal/dual 证书中的真实 Robin 球及逆 Robin 球本来就包围这些 $\Gamma_p$。因此，若 $C_*$ 和 $e_C$ 是已经计入旧六块的帽中心及误差，则

$$
\|C_{p,\Gamma_p}-C_{0,\Gamma_p}\|
\le\varepsilon(\|C_*\|+e_C).
\tag{121.3}
$$

这一步只新增参数 form 变化费。不能再支付一次 $e_C$，也没有额外的 $1/(1-\varepsilon)$。两帽配对和归一化余弦注入均为准确等距，其帽未知量为同一个 grounded $U=w/Y_z$；所以这里没有未支付的注入范数。

## 3. 已恢复的六维模型和实际 Banach 门

令 $K_p^{\rm fin}$ 为 R105 已认证的有限角偶核心 ODE 的端口 DN，$Y_p,S_p$ 为同族准确切口乘子的有限余弦压缩。其真实 ODE 跨越两个转折根，但不等同于未截断核心 PDE。

在五个余弦高度输入及一个 regular 输入上定义

$$
A_p=\operatorname{embed}(Y_p^*K_p^{\rm fin}Y_p-S_p)+C_{p,\Gamma_p}.
\tag{121.4}
$$

把帽有限 body 系数换成 $B_0$、保留同一个 $\Gamma_p$ 得 $\widetilde A_p$。本次原五入口已实际恢复175叶核心传播、完整切口和40行强 Gram；完整报告给

$$
\sup_{p\in I}\|\widetilde A_p^{-1}\|
<74.708434,
\qquad \sup_{p\in I}\|C_{0,\Gamma_p}\|
<1.172889190.
\tag{121.5}
$$

上述两项都来自 `data/native_core_20261113_ac0d/actual_even_low_paid_core.json` 的完整有向值，不是把旧收据中的四舍五入数值重新当输入。

新 consumer `scripts/fourfold_phase_even_low_parameter_complete.py` 核对所有完整输入、数组、源 SHA 和精确参数区间，再直接以原 Arb 端点计算

$$
e_{\rm new}=\varepsilon\sup_p\|C_{0,\Gamma_p}\|
<0.002345779,
$$

$$
\sup_p\|\widetilde A_p^{-1}\|\,e_{\rm new}
<0.175249428<1.
\tag{121.6}
$$

因此 Banach 逆公式对每个 $p\in I$ 合法，并且

$$
\boxed{\qquad \sup_{p\in I}\|A_p^{-1}\|<90.583064.\qquad}
\tag{121.7}
$$

对这个同一保留模型，尚可接受的额外绝对算子误差额度大于

$$
\frac1{\sup_p\|\widetilde A_p^{-1}\|}-e_{\rm new}
>0.01103959129.
\tag{121.8}
$$

完整数值报告为
`data/R111/ac0d_complete/actual_whole_parameter_retained_model.json`。
它明确保留 `paired_angular_mean_retained=true`、regular 两端口和完整帽响应，同时保留 `rigorous_full_Schur_inverse=false`。没有把有限可逆偷偷提升成全 PDE 可逆。$\square$

## 4. 重放与余下工作

四个实际续算的精确端点、命令、退出码和完整文件 SHA 见
`data/R111/ac0d_complete/execution_manifest.json`。从本题目录重放：

```sh
python scripts/fourfold_phase_cap_parameter_resume.py \
  --prefix data/R111/2026-11-13-ac0d-body-prefix.json.gz \
  --out-dir data/R111/ac0d_complete --parts 4 --workers 4 \
  --retained data/native_core_20261113_ac0d/actual_even_low_paid_core.json
```

原始 body producer 和原 collector 均没有修改。新 resume 脚本只安排不重叠实际任务，完整判断仍由原 collector 执行。prefix 的原退出状态保持为未完成整段；它只贡献已经接受且具有完整逐行证明的前缀。

R111 原“完整 body 报告尚未推送/whole-eta 六块尚未消费”的任务至此已经实际补齐。仍需完整高输入/体源响应、低高交叉及无限反馈 Schur、实际邻域强逆和真正非线性收敛；(121.8) 是具体剩余额度，不是这些未算项已经落在额度内的断言。
