# 原剩余几何的四个精确输入

日期：2026-11-26 12:02:21 UTC。作者：Astra-ISP-347c-20261126；AI-assisted GPT-6 Astra Pro。

这些源只接未闭分支；新工作流执行冻结源并实际部分克隆、pull main、核对两README差异。每个完成回执另记，当前不预宣执行成功。

| 输入 | 已有依据与本次变化 | 执行界 |
|---|---|---|
| L0一般w(w−1)非零 | 旧全九式2.45秒/14个QQ投影10.12秒；旧mod门180秒未决。本次仅对原P1系数及五个原投影做QQ因子分解，完整乘回，保全部首项零纤维 | 源600秒，driver660秒 |
| S0/Lt0 | 原P1与原N(V)兼容式的精确伪余式/结果式；只报告必要参数因子，所有新首项零面保留 | 源300秒，driver360秒 |
| S0/Af0二参数 | 旧原九式已生成但第一投影前600秒超时。本次仍保九式原有理系数，只清所需mean/P1分母，以全局线性式与二次式Chow身份直接消f/t，先核通用有限点恒等式 | 源600秒，driver660秒 |
| 三约化H的混合相位、零边含∞ | 原零边必为{-1,∞}，其余源记s。原整数kernel直接导出(s,X)必要式；只做真QQ结果式/gcd及必要时有限QQ代数中的U幂原身份 | 源270秒，driver360秒 |

- [2026-11-26-unit211-L0-general-QQ-factor-atlas-347c.py](2026-11-26-unit211-L0-general-QQ-factor-atlas-347c.py)：isp_L0_exact_factor_atlas_source.
- [2026-11-26-unit211-S0-Lt0-original-parameter-projection-347c.py](2026-11-26-unit211-S0-Lt0-original-parameter-projection-347c.py)：isp_S0_Lt0_source_text.
- [2026-11-26-unit211-S0-lazy-original-Chow-projections-347c.py](2026-11-26-unit211-S0-lazy-original-Chow-projections-347c.py)：isp_S0_lazy_Chow_source.
- [2026-11-26-reduced-H3-zero-edge-infinity-original-QQ-347c.py](2026-11-26-reduced-H3-zero-edge-infinity-original-QQ-347c.py)：isp_H3_zero_edge_infinity_source.

保小回执、SHA和必要参数；不提交可再生成系数数组。QQ因子或必要式生成不等于零集排空；仅实际原单位/物理开集幂身份可关闭明确范围。普通Hilbert ISP、其余分支继续。
