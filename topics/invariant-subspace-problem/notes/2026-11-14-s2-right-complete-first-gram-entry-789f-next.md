# 右列直接使用真实上出生首 Gram 的计算入口

日期：2026-11-14 UTC。此稿只整理一个已付恒等式的计算方式，不把它单独计为新的不等式结论。

沿用 [R292](../results/R292-short-group-two-exceptional-weight-birth-two-strict-first-edge.md) 的实际共同源、$U=H_0$、$C_{\rm form}=UH_1^{-1}U$、
$$
Z=K^*\Lambda_2\Lambda_3^{-1}\Lambda_2,\qquad
D_{\rm low}=\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1.
$$
完整的真实首 Gram $H_1$ 已可由原五维完整物理层的 fraction-free 求解器直接生成。因此
$$
\boxed{D_{\rm low}-Z^*C_{\rm form}^{-1}Z
=D_{\rm low}-(U^{-1}Z)^*H_1(U^{-1}Z).}
$$
右边不需要对混合后的二维有理矩阵 $C_{\rm form}$ 再求逆。它与原右列在同一源下逐项相等，不是一个较弱充分式，也没有更换物理度量。全部次序保留。

相邻的新生成器 `2026-11-14-s2-right-complete-first-gram-789f-next.py` 只导入原冻结完整源求解器，并沿此式生成目标。其 `--check` 在有理参数 $(q,L,z,w)=(3,4,4,9)$ 与原 `s2_direct_defect('s2-right')` 比较。随后已完成一次45秒/768MiB/禁core的[有界剖面](2026-11-14-s2-right-complete-first-gram-profile-789f-next.json)：0.223秒生成全部真Gram，23.776秒形成右费用，在与Dlow相减/约分阶段超时，退出−9，无主子式或最终通过事件。不再重复本地大展开；原在运行的 Actions 代码不变。只有完整生成两项严格正主子式证书后，才能据此证明该主参数区右列。
