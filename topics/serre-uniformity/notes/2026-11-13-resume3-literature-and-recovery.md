# 接手与文献现状（2026-11-13，resume3）

## 已核对的主问题状态

截至本轮实际检索，未找到已经完成 Serre 一致性主问题的公认结果。此句只记录所查来源，不声称穷尽文献。

- Furio–Lombardo, *Serre’s uniformity question and proper subgroups of C_ns^+(p)*，arXiv:2305.17780v2，2025-11-25 final version；摘要明确排除 p>5 的特定指数三子群。结合既有结果，p>37 的剩余非满像恰为完整 C_ns^+(p)。原文：https://arxiv.org/abs/2305.17780v2 。
- Serre 的例外射影像排除范围 p>13，Mazur 的非CM有理素数度同源排除范围 p>37，Bilu–Parent–Rebolledo 的分裂Cartan正规化子排除范围 p≥11、p≠13；p=13由 Balakrishnan–Dogra–Müller–Tuitman–Vonk 补齐。以上范围亦逐项见 Furio–Lombardo, *On 7-adic Galois representations for elliptic curves over Q*, Proceedings LMS 133 (2026), e70193, §1，https://doi.org/10.1112/plms.70193 。该文仍将一般一致性列为开放。
- Genao–Mayle–Rouse, *A uniform bound on the smallest surjective prime of an elliptic curve*, Ramanujan J. 70 (2026), article 22, Theorem 2，https://doi.org/10.1007/s11139-026-01376-8 ：最小满射素数至多7；不提供最大非满射素数的一致上界。本题R52已用此输入，本轮不重复登记为新结论。

## 恢复状态

最新实际main基线：1e2d77c37ec2ce3f784278b01122c846d9f6a4d6。两README对旧交接基线dfdb25c706c7f8a750131eb2f961e51f825ea0b2无差异。题目完成标准不变。

旧工作树 `/workspace/scratch/64b49fd2bdbb/math-research` 不存在；本轮新部分克隆仅检出本题。已检查本题log、notes文件清单及第三次恢复检查点。

旧交接“待推bridge”已由远端提交3f147daf4完成：

- `scripts/p41_kernel_level_bridge47.py`，7325 bytes，SHA256 `d541c21e522307950f58288d45af881bbd3ebcf2825bbebc03ebafab15bcb853`。
- `scripts/data/p41_kernel_level_bridge47_verified.json.gz`，8750 bytes，SHA256 `a94e53917b57bcec416b13dd72241abfb9c2d36c9661ea982196c30cb42a0701`。

未保存的常数DAG、四阶、完整level运输及scalar primitive atlas必须实际重建；历史计数不能代替新文件。R210、R211–215、R217只有交接梗概，须重新给出完整证明，不能由旧结论式自动恢复其可信度。根会话保持tracked文件和git单写；辅助工作分别写当前workspace的独立目录，收到后立即接入适当的note或result并推送。
