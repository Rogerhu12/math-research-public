# 实际全截面有符号根初值：GCS 首次成功

**已实际完成。** [首次 run 46132087372/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46132087372) 对 [GCS 完整合同](R149-supplement-whole-signed-root-seed-at-the-physical-strict-cut.md) 给出真实截面初值。事件提交 `a3c58553c4591e6ddc97a493fcc12af2085a12a6`；job `140939260065`，2026-11-28 09:47:10–09:48:12 UTC，终态 success。采用原固定隐式成员，不把其参数换成零或区间中点。

## 整件身份及准入

首次完整小收据 19866 bytes，SHA256 `201c8215275b04dfa69c6a9b03248dea6bde01bd782969d006c823088c0637b7`，由 job 日志中完整 `GCS_WHOLE_SMALL_RECEIPT` 原字节提取，另与日志自报 bytes/SHA256 一致；完整原日志 zip 79622 bytes，SHA256 `835ea34954bbdf66bf7701b144a3ac0d55bfd37cc525e274203d28b2903f23ea`。不从摘要重造收据。

原 `seed_admission.admit` 对 76 个自然整件再次做字节准入，全部 bytes、SHA256、原 run/process/publication、参数及 stage 身份与首次收据逐项一致，总计 2606796 bytes，原 Taylor stages 70。事件提交上的 4 个计算/准入源及 workflow 共 5 个源码绑定通过。这次后置准入只读原 Git 内容，没有调用原 producer、native 或数学消费者。

首个 private 完整 gzip 为 **11131542 bytes**，SHA256 `9af56c23e91a021f0463aa01b68ea93916ba11d374ecd7323ce4c4b51b3da9ba`。producer 已按完整 schema 读回全部字节；共 **704512 个复矩形**，覆盖 **2048 个中心及 2048 个闭角格**。完整数组只在计算 job 私有空间；后继若必须重建此输入，必须匹配此原 whole bytes/SHA，不重新授予旧科学目标成功。

## 实际数学覆盖

物理 cut 为 `76285779072683/320000000000000`，原根区间为 `[1191984371497/5000000000000,2383968743003/10000000000000]`。角周期为 π/2，物理频率为 4j。所有有限 Fourier 系数经过完整桶 DFT，原 Taylor 与 holomorphic majorant 余项全部保留。以下阶数均从零阶计至所列最高阶，采用原 normalized jet 单位。

| 全部字段 | 实际最高角阶 |
| --- | ---: |
| G、Q、a0、b0、w1a、w1b | 6 |
| 四支 R（两射线、两符号） | 6 |
| T、chi、omega、sqrt_minus_T | 9 |
| phase_displacement_plus/minus | 9 |
| p_plus/minus、Xp | 8 |
| v0_plus/minus | 6 |
| radial_prefactor | 0 |

所有 22 个字段和每一中心/整角格均存在。收据的整格 binary64 外包端点如下；证明使用完整球，不把本表作为替代载体。

| 真实量 | 全圆下端点 | 全圆上端点 |
| --- | ---: | ---: |
| T | −1.7375716879685346e−5 | −1.737571070316215e−5 |
| omega | 4.8286153062569754e−8 | 4.828617880899347e−8 |
| p_plus、p_minus | 0.9999998512416269 | 1.000000145903371 |
| v0_plus、v0_minus | 0.999888889565761 | 0.9998895083128374 |

因此该实际截面有严格 `T<0`、`omega>0`、两方向 `p>0`、两 `v0>0`。四支 ratio 的有符号非零初值、完整高阶标签与共同 gap 可按上述 whole 身份送入后继；不能擅自置零。

## 已付范围

首次收据明确 `complete=true`、`proved=true`、`old_scientific_targets_recomputed=0`。它同时明确 `all_global_negative_cells_complete=false` 与 `uniform_high_response_proved=false`。这里实际付清真实 root cut 的初值，不把单截面的包络当作根到腰的全域误差，也不据此宣称完整物理逆或最终精确闭族已经完成。后继 GPR 使用同一 whole 初值、全部原负域格和完整圆周残差继续求真相位；幅度、强迫、全高接收和所有边界仍按各自合同支付。
