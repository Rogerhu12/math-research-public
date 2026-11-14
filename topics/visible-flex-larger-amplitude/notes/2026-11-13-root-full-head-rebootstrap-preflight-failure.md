# 完整真head重代入：r1预检失败与保守修复

作者：/root（GPT-6 Astra Pro，AI辅助），2026-11-13。

r1 actual exit1，153.283s/294520KiB；无ODE/新的source积分。前四块原正有理head+centre恒等式通过，block4的`positive_head_replacement`在128位上舍入后失败，未生成完整bootstrap或cut证书。

原因是未变的centre项支配该块，新head的改善小于其128位舍入尺度。新精确正有理和不超过旧精确上界，但将新和上舍入后可能略超过旧界。修复先逐块准确验证新正有理和≤旧界，再用两个独立有效上界的min：旧精确界与新向上舍入界。这样不假设浮点舍入为零，也不改变任何数学域或省略原centre。

fresh v2源4d11ae17d6e3f901b9f6c704a32e0db99a151216de9fec40a9e9f378933de40c在独立r2输出运行；本失败包不宣称r2已完成。全部旧冻结输入保持原SHA。
