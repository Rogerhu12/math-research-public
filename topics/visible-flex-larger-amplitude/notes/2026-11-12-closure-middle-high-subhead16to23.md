# 中高频胞元16..23的实际补矩阵

2026-11-12，exact_closure。

tail代理在混合有序标量源核与真实正流时定位了新的具体缺项：
2050..4096窗最坏出现在cell16，4098..8190窗最坏在cell18。
它们来自跨胞元齐次放大的过粗界，本地源对角核已很小。

只对cells16..23补同两频窗，不重做12..15或已有24..224。
未改动的 `closure_positive_subhead_matrices.py` 使用同一真实
源和相同规范，作业66350已formal exit0，resource也记录
exitcode0。共6950个面板，最大AB小于0.249428，22.8561秒，
峰35016KiB。全8个cell已保存，绝非端点插值或遗漏项补零。

包为 `2026-11-12-closure-middle-high-subhead16to23.json.gz`，
summary保存包SHA与同源输入SHA，resource保存完整命令：

```bash
python computations/strong_resource_run.py \
  --out notes/2026-11-12-closure-middle-high-subhead16to23-resource.json -- \
  python computations/closure_positive_subhead_matrices.py \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --source-ledger notes/2026-11-12-closure-wide-strip-head-ledger-paid-source.json \
  --start 16 --far 24 --bands 2050:4096,4098:8190 \
  --out-prefix notes/2026-11-12-closure-middle-high-subhead16to23
```

这里far24只是矩阵输出范围；`RealHead`仍使用同一物理源和原
真实半径锚点。与24..224包一样，输出坐标为
$(Q,\Xi/\nu_m)$，向外跨cell须再乘第二分量 $1/\rho$。
正流部分区间的比较论证见
`2026-11-12-closure-middle-high-subhead-matrices.md`。本补件未
自行宣称全频源Green或完整闭合已经支付，由tail代理在其
保留源位置和连续strip的实际核中消费。
