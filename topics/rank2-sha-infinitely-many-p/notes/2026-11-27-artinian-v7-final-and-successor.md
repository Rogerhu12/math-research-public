# Artinian v7 的实际终点与商域表示修正

日期：2026-11-27（UTC+8）；会话：Astra-rank2-Sha-0b097461-20261127，geometry。

**状态：原 v7 已失败，准确原因为有限域表示的 API 假设，不是超时或 OOM。
原 F 的完整几何、四交和 shadow 没有 PASS。**

## 1. 实际运行回执

- 原 source：`6e79456aa2250a589306ba39d983ecdc46a2f267`。
- [run 45838674625 / job 139974211422](https://github.com/Rogerhu12/math-research-public/actions/runs/45838674625/job/139974211422)。
- job：2026-11-26 14:24:24–16:20:03 UTC；数学步骤：14:25:04–16:20:00 UTC；结局 `failure`，host 返回 1。
- GitHub job logs 原始字节（含原 BOM）：4,060,943 B；SHA-256
  `00a364947dc153704528b5a9ef9b857c9a51bbb820d8c742e373d588da359819`。
  日志只在临时目录读取，不入库；上述 API 及 source/run 足以重取。

已实际返回：两原特征零 PASS 认证、全部原正规化乘法与七个椭圆方程，
以及第一张图的 1530 长度厚商预检中的完整 Fitting 分离、整单位逆、
带共同零点的完整分式图和第一基素因子的完整范数层。
最后一条成功阶段是 16:19:56 UTC 的
`original two-chart relative thick norm preflight: pi 1/2, entire H_2`，
整个 306 行 HNF 已返回，商长 306，数学 elapsed 6884.487 秒。
第二个基素因子的商域构造随即失败；这既不是双图预检全部成功，
也不是原 F 的零极除子成功。

准确异常位置：

```
original_ys_artinian_norm_tools.py:524  ActualFiniteFieldQuotient(pi, ...)
original_ys_closed_point_tools.py:119  native_absolute_degree(self.field)
original_ys_closed_point_tools.py:50   card(field) == p**field.degree()
```

异常消息为 `Expected the original native absolute finite-field model;
degree() is not its degree over the prime field.`
`RANK2_TRIANGULAR_ARTINIAN_FAILED` 记录 elapsed 6884.976900202 秒。
后继不得简单重启这份未修改来源。

## 2. 确认的实现原因

`ActualFiniteFieldQuotient` 原先把 `P.quotient(pi).field_extension(...)`
的返回一律视作绝对有限域。Sage 对非素有限域上的多项式扩张可以返回
一般多项式商域；它的 `degree()` 是相对次数，故该返回不满足这里为
绝对坐标编码所需的断言。简单删断言或用相对次数代绝对次数都会误读
后续的坐标、Frobenius 次数和完整残余域次数。

已读官方资料：

- SageMath 10.6 原源码，
  [`polynomial_quotient_ring.py`](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/polynomial/polynomial_quotient_ring.py)，
  `PolynomialQuotientRing_domain.field_extension`。
- SageMath 官方
  [finite field extension 文档](https://doc.sagemath.org/html/en/reference/finite_rings/sage/rings/finite_rings/finite_field_base.html#sage.rings.finite_rings.finite_field_base.FiniteField.extension)：
  对非素底域给多项式时会退回一般商环表示；给整数扩张次数则返回绝对有限域及底嵌入。
- 同页 `free_module` 给指定底嵌入、指定基的向量空间双向映射。

后继须保留原 `P/(pi)`、原底域嵌入和全部正反映射，
另给符合真实绝对坐标接口的表示；不能只更改断言、抛掉二次常数、
任意替换原 omega，或用素域范数代原二次域范数。

## 3. 当前后继

正在构造并证明显式保底域的绝对有限域表示；仅修改相关表示层和真实入口 pin。
全部 306 行、厚度、两个图、原参数与完整 shadow 门保持。
在相同 Sage 10.6 上先执行针对这次真实 API 故障的有限域表示小入口；
它成功也不代表原大链通过。

完整表示同构与厚范数返回已证明于
[R974](../results/R974-original-residue-native-model-and-complete-norm-return.md)。
其第 6 节另追清了人工 1530 长度预检的数据流：它不向原 F/P、四交或
shadow 提供对象，只提供一个单独的 API 回执。按根规矩第 12 条，
后继将把它改成默认不执行的显式选项，并准确记录未执行。
实际原几何和每个厚层的数学返回门不变。v7 的 6885 秒中，
前约 4809 秒是真实来源/正规化/maps 的重生；首图人工预检约耗 2076 秒，
第二图人工预检尚未执行。不能把此前全部 115 分钟都算作人工预检开销。

针对这次真实失败的 API 修正已经在
`run45881262808/job140120885101`（source `cd89412822ef2497f97891969248bfdcc23b52fe`）
实际成功。完整日志 26,655 B / SHA-256
`a1f43397f9376521c630be7562831d6c74de31f8e6400f9366314dfa33afbd1d`；
RESULT 8,315 B / SHA-256
`99ec7d327ac73cfb354805c3fd6397ef0ccad40192956bc55790d06e8750a27a`。
详情见 R974 第 7 节。生产原大链未据此宣称成功。
