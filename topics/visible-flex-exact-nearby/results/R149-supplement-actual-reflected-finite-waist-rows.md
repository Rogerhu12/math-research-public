# R149 补篇：96 个 reflected finite waist rows 的实际完整认证

2026-11-26，visible-exact-astra-198c63d-20261126 / correlated_energy。

**公共 Actions run45787309600/1 已完成 RW 声明的全部96行、480个新小球。** [完整 scientific conclusion](../notes/reflected_waist_rows_ci/run-45787309600-1/actual-reflected-waist-rows.json) 的 complete/proved 均为 true，actual_returncode=0；[完整 execution](../notes/reflected_waist_rows_ci/run-45787309600-1/execution.json) 记录唯一科学 child、returncode0、没有 timeout。事件提交为953233c73ee96413e1a87c61a87bb7c14f11e2a8，实际科学 checkout 为820514d32819b31321219f74751e5eedef01a641。

本次支付的是 [RW.14–22](R149-supplement-reflected-finite-waist-rows-from-complete-conjugacy.md) 的明确 finite row trial 及完整误差。真正 PDE 列、signed96 matrix inverse、target $\mathcal B^{-1}$、transported $\Theta$ 和 full incoming inverse 均未在本次证明；原总任务仍未完成。

## RWA1. 完整对象、原件和保存链

固定 $L=4096,N=1024,j=1,\ldots,96$，原物理频率为 $4j$。真实 target basis 始终为
$$
g_j(x)=\sqrt2\cos(4j(x-a/2)),\qquad a=2\mathcal H(0),
$$
没有把反射中心置零。全部 exact H24/K48 rational coefficients、原两个零 translation 的完整源码 AST 资格，以及 $G=K_{48}\circ H_{\rm fin}$ 的整个复合均已核对；terminal rotation 没有被当成 $K_{48}$ 的常数槽。

30件当前 text inputs 和4件历史原 native 全部按原 bytes/SHA256/Git blob 读取。历史恢复 commit 固定46f127c7153f5393dcd2a00f42d4c1d3662c294d。原 W 的全部8个 loss 记录保留，selected loss 精确为1/250；原 $K_{W,0}$ 只取 WTA 的固定 $J_s=268435456$ 成功行，未换成另一个 dyadic 结果。完整 admission 在 reserve marker 和数值 import 前已通过，随后 owner 又核同一全件。

唯一 trial 是 RW.14 的 **exact sampled DFT**，不是其 enclosure midpoint。private 完整4096点 grid 和每行全部1025个非负频 real coefficient 都保存并逐项读回，负频由已证 even identity 确定。96行一共98400个 real coefficient enclosure；这些可重建数组均未发布、上传 artifact 或 Release。公开结果保留每件完整 carrier 的 hash/bytes 和所有声明小球。

每行的 signed mean、Parseval norm upper、compound error upper 先通过 candidate 回读，再写入正式 pending record；incoming 和 physical 两球只消费该正式保存的 compound error upper。完整五球再经整件回读，才推进 completed row prefix。实际结果没有剩余 candidate/pending/current target，正式 prefix 恰为 row_001 至 row_096。

三个原 scalar records 原样保存在 copied_prior_scalar_records 中，分别是 selected $\|\mathcal H-G\|_{A_{1/128}}$、完整 $\|G-Id\|_{A_{1/128}}$ 与固定 $J_s$ 的 same inverse $L^2$ bound。旧 KAM、transport、normalizer、receiver、HS 或任何旧科学 target 的调用数均为0。

## RWA2. 原件首行和末行的五球

下表逐字抄录该 actual 的首行和末行；没有重新求 max、积分、DFT 或误差组合。mean 一项是 signed enclosure，其余是已保存 upper 的 whole ball。

| 原字段 | row_001 | row_096 |
|---|---|---|
| `mean` | `[-0.0079660966625910259256685541348469260794836475300331 +/- 4.63e-53]` | `[2.14365e-39 +/- 5.87e-45]` |
| `trial_l2` | `[1.0010677920585834866469544022026657888028141871792 +/- 2.66e-50]` | `[1.0000000000000000000000000000000000000000000146548 +/- 4.04e-50]` |
| `compound_error` | `[1.2501797468470328632670643493979641654704278959005e-6 +/- 3.64e-56]` | `[0.00012001725527507492113575209113066502853008917427944 +/- 3.08e-55]` |
| `incoming_error` | `[1.2501797469115760802871108168630469160303956166242e-6 +/- 2.17e-56]` | `[0.00012001725528127106994787749222453273877234904822648 +/- 1.66e-54]` |
| `physical_error` | `[8.8401057669761824417637530595305567918759716680672e-7 +/- 1.84e-57]` | `[8.4865015064402418875079930758105254369487815151955e-5 +/- 1.26e-55]` |

第一行的非零 mean 被完整保留。末行 mean 的小球也未被改写为零。三个误差分别围住
$$
\|g_j\circ\mathcal H-p_j\|_2,\qquad
\|\widehat T_0^{-*}\iota_+(g_j\circ\mathcal H)-\iota_+p_j\|,
\qquad
\|z_j^\partial-z_{j,\rm app}^\partial\|.
$$
真实 incoming 只在本次声明的96个 reflected cosine observations 上取得这些 row errors；physical primitive 使用两个 half nonmean components。两条独立 density mean row 仍分别为原 identity、精确 norm1，不代表 physical mean matching equations 已解。

首行全 carrier：26289B，SHA256
`4e4d5e2f29658e8f7556ada257a3bed74e34e4717edaa5b511e41d71510a3eac`。
末行全 carrier：23306B，SHA256
`8f9db58a0beda33799e29a98d8123bb10efd8043c44543c30f9cf2d2b04f9b97`。
完整 grid：412085B，SHA256
`4411b74c8b2288e8e7d2803906f01b5d60fe98e5998edc244450451e1493502c`。
其余94行的整件 hash 和全部小球都在同一个86146B actual 中，未使用分件摘录冒充全件。

## RWA3. 实际执行身份与后继消费

| 完整原件 | Git blob | bytes | SHA256 |
|---|---|---:|---|
| scientific conclusion | 05e179aa3a8815c84e8d09db9f2693f0e1930374 | 86146 | b0faf218c059b6f7ee113a5f127a7518e78d2c87dc70b4dcf650ce97594c7fa4 |
| execution | 7d60a03a1ea9fe101724cba161bb1402cf4c6cb6 | 16042 | 3cfc1cbc9f8b1c5fe450c779146042c6b7f4bd4f42ca48606c4c9309e94a0b00 |
| input manifest | 4b24e937843efdafb328bf692bbcfa9f19dd4f9c | 14822 | be8da3e31973d9c3725a4dcb4834287a1add06121e3853ea4308b08b656fac05 |
| owner | 286d4410d1abbf410ba35e45e0a9209fbc6c241f | 53358 | d4d703990c78deefb93f7db8076f5eaf729ff38c58e18069f341595111f46f6d |
| pure row math | 65ff3491563d78a670f046f4bd706829bff15151 | 12663 | c8f40a0d50c6b55c58016adca749aed00c8236f3eab653987ddd941f047cdf09 |

runtime 为 Python3.12.14、python-flint0.9.0、320bit；owner 记录 wall3.8963921470000003s，worker child wall3.994033507999994s。execution 记录5次 pull/README 检查及完整 receipt hash chain，保留首件和最后3件全文，原规则 commit96edc677044b6ad7c7fd3aa2f65bf77d9c0e27a1、Nov20 receipt 与两当前 README 一致。

后继 [SC](R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md) 列计算应读取这整个 actual/execution/manifest，按同一 exact DFT 定义物化必要 row carrier，再与其真实 trial 腰列作 signed Hilbert pairing。已成480球不得重算或替换。对于也在原 $|k|<J_s$ trial 空间中的列，RW.26 仍只消去 row-trial 项的 $K_{W,0}$；真正 PDE column error 的完整 receiver 费用保持。

本次没有 PDE residual、实际 signed matrix entries、有限逆或 full $\nu$/phase/mean Schur。下面的工作是计算同一物理 root96 列的 signed trial 和完整真系数 residual，然后用已成 rows 与原完整 inverse 链验证它们；本篇不把这些未成条件写成成功。
