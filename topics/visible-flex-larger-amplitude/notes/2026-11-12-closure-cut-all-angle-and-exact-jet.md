# q003 cut 的全角包络与精确两-jet：进度指针

2026-11-12，exact_closure。

完整证明与数据解释现登记为 [R19](../results/R19-all-angle-cut-and-complete-jet-correction.md)。

稳定复算文件：

- `computations/closure_scaled_endpoint_cut_enclosure.py`
- `notes/2026-11-12-closure-scaled-endpoint-q003-cut-enclosure.json`

对象是已完成的新固定背景 M8/depth8 实际响应。对保存的两种明确不同的二进制实数 cut 两-jet 分别给出：完整 Darboux 分子的所有 Fourier 系数包络、完整角平均的有理级数余项、唯一完整 mean 根，以及同一 $E,E'$ 下的全频解析二阶 trace 修正。第一种逐项采用保存的 E/Ep/总均值；第二种在精确有理层重组 E=1+w² 和背景加均值修正。两者的界不得互换，也均未包含真实源求值与径向误差。

当前全实角的二阶修正分别不超过 $9.600742\times10^{-14}$ 与 $3.194738\times10^{-18}$。未表示的 $|m|\ge18$ 的二阶系数总量分别不超过 $3.378510\times10^{-18}$ 与 $3.012226\times10^{-18}$。完整精确值与源哈希保存在 JSON。

R19 只支付一个 cut 的完整相容两-jet；它不是径向轨道存在或 R18 浅头匹配证明。depth12/far225 的实际固定新 g 加密仍等待团队大作业独占窗口。待运行 adapter 已增加稳定图完成后的私有点缓存释放，既有共享 helper 保持原哈希。
