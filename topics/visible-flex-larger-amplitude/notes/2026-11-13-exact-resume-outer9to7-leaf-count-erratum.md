# 原 outer9..7 后验读出的总叶数文字勘误

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-13。

原 `2026-11-13-exact-resume-outer9to7-r148-update-proof.md` 第 13 行把三个胞元的总数写成 3930，这是加总文字笔误。正确为 **3940 个已成功子步**：cell9 的 1377、cell8 的 1316、cell7 的 1247。该行所列三个分项本来正确。

实际原 primary 的 `cells[*].profiles` 准确保存 `[1377,1316,1247]`，三个 `cellN_all_original_steps` 门分别核对原 `taylor + root_brackets`；源代码没有 3930 的数值或据此截断的循环。4842 个原实际门及全部成功数据不受此文字笔误影响。原 primary、原 source、原资源和原证明字节保持不变，本 sidecar 仅更正总数。

原 primary SHA256：`8b634c8c8541a05b154995060bd24a161f84998207c2e9620b531eb1a0a152b3`。原证明 SHA256：`f6cfa65146d87c9982b59f632c93e611ce0e8e914bad049af0985328ab00c8b8`。
