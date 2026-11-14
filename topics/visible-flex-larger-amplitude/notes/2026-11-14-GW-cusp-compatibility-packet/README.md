# 原 GW cusp 局部输入小包

本包只无损提取既有完成读出消费过的字节，没有执行新的数学计算。来源是历史 `A-RK48-cusp-resolved-r4` 的 f8/f16 层和 GW 完整共同网格结果，具体原路径、整文件 SHA、节点索引及逐片段 SHA 见 `manifest.json`。

旧 GW 消费者没有单独保存完整 Cartesian GW 二阶节点数组；它保存/消费的是 512 角、12 列的原 point 文件，随后以 `TargetMetricTail.node_coefficients` 动态形成 GW 二阶规则。本包明确记录这个边界，不能称这些原 point 的空缺 XY 二阶列已经是保存过的 GW `rr`。

三个 `nodes/*.f64le.gz` 是原压缩文件的逐字节副本，未解码重存。它们分别位于共同 cusp、f8 内端、f16 内端，提供完整 512 角数据。四份节点 `rows/*.json` 与一份背景行是原大 JSON 中相应对象的原字节子串。`original-GW-common-grid-report.json` 是旧完整输出原样副本。所有原容器的 SHA 已与旧 GW 输出启动时记录一致。

独立 `exact_20261114_GW_cusp_compatibility.py` 仅允许在本公开仓库 Actions 执行。它严格检查三份原 GW 数学 helper 的 SHA，调用原 GW 类而不调用 default-rr 节点规则，重建该局部有限场，并分解

`P = Q_cusp + E (10u³ − 15u⁴ + 6u⁵ − 1)`。

`Q_cusp` 是共享三次速度的积分，位置锚在两层共同的 cusp。这个锚不改变径向一、二阶分解，并使 `F_theta` 和 metric 的局部比较有相同的实际 cusp 位置。背景使用原保存的 17 个 `r,w,w_r,E` 点，角网格至少为原共同检查的 1024；没有重算 ODE、射击或完整尾读出。

输出包括原 quintic、积分速度项、位置兼容项各自的完整六 jet 局部差、`F_theta` 与 metric 变化，以及最坏 `theta=0` 点上对已重建二进制 Fourier 节点的有理数代数影子。后者区分消费端多项式求值舍入，不能消除节点生成时的误差。完整节点 Fourier 系数和多项式保存在输出 NPZ。

运行方式：

```bash
python -u "$C/exact_20261114_GW_cusp_compatibility.py" \
  --packet "$N/2026-11-14-GW-cusp-compatibility-packet" \
  --out "$OUT/GW-cusp-compatibility"
```

其中 `C`、`N` 分别为本题 computations、notes 路径。此处不预先称误差来自 roundoff；`E` 同时可能包含真实截断、源点重构和接口误差。局部积分速度场没有替换当前闭曲面，局部有限样本也不是连续 metric 或收敛证书。
