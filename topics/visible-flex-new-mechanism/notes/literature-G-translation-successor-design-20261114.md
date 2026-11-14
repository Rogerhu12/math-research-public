# G 平移链的单个后继：只运行第三阶新权块

状态：**实现及小人工检查已完成；真实第三阶目标尚未运行。**  
日期：2026-11-14。新脚本独立于已发表的 first/second producer，旧文件不改。

## 1. 本次唯一数学目标

[R128](../results/R128-second-G-translation-separation-and-76-query-control.md)
已经严格证明 $N^2G\notin R_8$，且完整权 $-1$ 响应维数恰为 $29$。
本次只检验
$$
N^3G\stackrel{?}{\in}R_8.
$$
$G$ 的真仿射权为 $1$，所以新目标权为 $-2$。按已发八维二阶基和
$36$ 维完整第三基的实际整权，共有 **50 个**该权原响应列。
没有重跑前两阶的 $20$ 列、$36$ 列、依赖证明或原有理评价。

脚本文件为
[literature_G_translation_successor.py](../scripts/literature_G_translation_successor.py)。
它支持一次显式给定 $3\le j\le10$，但**一次调用只计算一个 $j$**。
本次公开请求固定 $j=3$。以后若需要 $j+1$，必须另行绑定紧前一次完成的
真非成员报告；不能自动扫整链。前一步已经得到原式成员或零目标时，输入门拒绝继续。

真实平移生成元仍是
$$
N(\xi)=1,\qquad N(q^{(a)})=N(\bar q^{(a)})=0,\qquad
N(I F)=I(NF),
$$
其中 $I$ 是同一真实右端锚的有符号原函数。它不是完整 $\partial_\xi$。
从旧原 $G$ 施加 $j-1$ 次 $N$ 仅用于与上一公开目标的原式 SHA 比对；
不评价这些旧目标，不重新形成旧响应块。

## 2. 默认前驱证据与来源绑定

默认前驱是公开 run `43651413950`，source
`ba3a19be3ef851fbeb29ff491618e18622064f12`，lane
`g_second_translation`。

| 输入 | 字节数 | SHA256 |
|---|---:|---|
| G-second-translation.json | 41062 | `2828278fa8f881fbb53a2c6518a63d3067521c9860f07652c7e0080696cc5723` |
| receipt.json | 33699 | `3abf0890dd897cfb2d4b1fa6ec2daef7c3f26a230613a48827cf7e2a8018ac68` |
| literature_G_second_translation.py | 24396 | `3c37aeae4b39ecf68932a069878b41d890afbe2fd4ee9d8675195edc4e5d6bc1` |

默认 $N^2G$ 的两个原式哈希为

- mode $-4$：`2f4985b03d739f86dfb97a6aa688afcb4c52a21a8c632ab3950cd36900d81c8e`；
- mode $-2$：`c40b69eef9041cf7c381c95a1d6061910d9cbc99c82f541db576ff6c4f69abd3`。

输入门同时核主报告、终端 publisher receipt、run/source/lane、
原 producer 文件名/字节/SHA、紧前阶数、原目标哈希、完成状态、
真非成员子式和有理分母门。要求 retained 原列数与已证上界一致，
并要求所有丢列的 fresh 原式依赖计数等于原列数减 retained 数。
报告的语义是消费这些已发表证据，**不是在这里独立重验旧代数**。

更后的阶数使用同一个源文件，但必须显式更改全部相应的
`--previous-*` 输入，包括报告及 receipt 的路径/长度/SHA、
run/source/lane、原 producer 文件身份和两个原目标哈希。
若仅把 `--order` 改成 $4$ 而仍用默认 $N^2G$，阶数门会失败。
新 generic 主报告自身保留足够字段，可作为下一次独立调用的前驱。

原 $G$、$W_{36}$ 和局部导出仍只消费 R115 已发的完整原 DAG；
源依赖按冻结 first helper 的身份再次核对。没有编译旧第四 forcing、
恢复旧 $W$ 或重做局部密度。

## 3. 新块的准确判定链

1. 枚举完整 $E_8\times W_{36}$ 中整权之和为 $1-j$ 的原列，
   保同一实系数同时作用于 mode $-4$、$-2$。
   每个使用到的第三模板均从原式核其已发真权。

2. 正规形式只用于提出有限列依赖和候选系数。每条丢列关系均回到
   原式重新组合，并通过有声的右端积分分部恒等式核零。
   由此给出真响应维数的**上界**；代表矩阵秩本身不冒真独立性。

3. 若新目标有候选成员关系，也从两 mode 原式重新核零。
   成功即严格得 $s=j$，记
   `further_translation_orders_needed=false`。
   真零目标分支同样回原式核零后停链。

4. 若只有非零代表余项，则另用已发原右 Volterra 多项式评价器，
   在同一真实有理测试 pair、同一组查询点上评价 retained 原列和新目标。
   不评价 word 代表。只有实际控制秩达到上述真上界且增广多一个秩，
   才能写 `nonmember_certified`。有限域只用于证明真实有理子式非零；
   不把模值当实数符号或把模泛函系数当 $\mathbb Q$ 系数。

5. 若原列像秩低于上界、预算不足或实施检查失败，保留相应回执，
   不宣布非成员，也不擅自推进下一阶。

真非成员由单齐次权块及实际 $R_8$ 的整权直和结构推出
$N^jG\notin R_8$。它是完整 universal 算子命题；
不是所有合法 profile 圆都不能匹配，更不是本题有限弯曲的不可能性。
R122 的实际共同查询控制仍需其已证有限构造、共同物理域和基准成本。

## 4. 输出与资源

默认研究预算沿用前块，不扩大：

- 240 秒，1024 MiB 软轮询内存门；
- 原有理多项式最大次数 256、操作检查上限 10000000；
- 24 个参数点、两个 mode 和实/虚行，共 96 个候选评价行；
- 固定 bump power 8，实际原 DAG 扫描必须核最高输入 jet 不超过 7；
- 质数 2147483647，评价器重新核质数及所有遇到的有理分母可逆；
- 主 JSON 上限 90000 B，完整压缩报告上限 2500000 B；
- 新可携原式 gzip 上限 2000000 B、解压文本上限 40000000 B；
  三项预留合计 4590000 B，所有输出仍受 4800000 B 总门限制。

主 schema 为 `visible-flex-G-translation-successor-original-v1`。
主报告中的 checkpoint 保请求阶数/权、前驱身份、原目标哈希、
新原列上界和完整依赖摘要、真子式或阳性关系、全部停止条件。
完整报告在任何正常、资源或实施异常出口均先尝试写 gzip。

若增广原矩阵的 JSON 大于 16000 B，主 checkpoint 只保其行列数、
SHA、选行、行列式与精确有理泛函定义；完整矩阵仍保在完整报告的
`original_evaluation.dual_certificate` 中。这只限制小报告体积，
不删除完整证据，不重建矩阵或换评价列。

建议本次文件名：

- `G-translation-successor-development.json`；
- `G-translation-successor-development-complete-report.json.gz`；
- `G-third-translation.json`；
- `G-third-translation-complete-report.json.gz`；
- `G-third-translation-original-expressions.json.gz`。

### 新权块原式可携导出

在本次 50 个新原响应已完整形成、依赖/成员/原有理评价之前，
保存目标及 **全部 50 列的两 mode 原根**，而不是只保存 retained 列。
schema 为 `visible-flex-G-translation-successor-original-v1-original-expressions`；
`content_scope` 为 `one-translation-target-and-complete-new-response-block`。
保存 producer/source/run、前驱绑定、原目标身份、全部 label、
`column_records`、原根 SHA 和真实右端原函数 atom DAG。
解码直接复用既有 `old.decode_expressions`，不需再构造任何旧响应。
若目标已准确核零而未构造响应块，则单独声明 `zero-target-only`。

补充导出使用冻结旧 `serialize_expressions` 的原式格式。
主 checkpoint 在 `portable_new_block_expression_export` 保存
文件名、压缩/原文字节与 SHA、根数、atom 数、完整范围和是否已持久化。
后续消费者还须核 publisher receipt；导出本身不冒充依赖或秩证书。

补充导出不是数学证明的发布门。若原根序列化超过 300000 项、
原文或 gzip 超出专用预算，记录准确失败范围并继续数学判定；
不把已经成功的子式/原式身份改成 `output_limit`。
反之，完整数学报告仍有独立 2500000 B gzip 预算。
主报告压缩矩阵时完整矩阵也仍留在该独立报告里。
每个源只生成本次新块，没有因此重跑前驱块。

## 5. 本地已完成的范围

只运行 `py_compile` 和新消费者的 `--toy-only`。19 项人工检查全过，
没有读真实 $G$ 或前驱原目标，没有评价研究 profile，也没有编译任何研究响应列。
检查包括三次外/内坐标微分、三层嵌套原函数、独立三阶有限差分、
真实权下降、前驱阳性/阶数跳跃/分母门缺失/来源被改时拒绝，
以及小主报告压缩不破坏完整原矩阵；新增原式可携 round trip、压缩/原文字节身份和补充导出预算失败不改变数学状态。

开发回执：
`G-translation-successor-development.json`，6259 B，
SHA256
`c0c46f1f6074228d2590dc7a5716998146da0ddcc1b66f82ec48b998ef8c1f26`。
耗时约 0.0069 秒，峰值 RSS 15.25 MiB。此处只说明人工接口，
不预告第三阶研究结果。

冻结源：39670 B，SHA256
`a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406`。

## 6. 本次公开 Actions 最小调用

在本公开仓库中先执行：

~~~text
python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_G_translation_successor.py
python topics/visible-flex-new-mechanism/scripts/literature_G_translation_successor.py --toy-only --order 3 --output "$OUT/G-translation-successor-development.json"
~~~

人工接口成功后，只运行：

~~~text
python topics/visible-flex-new-mechanism/scripts/literature_G_translation_successor.py --order 3 --output "$OUT/G-third-translation.json"
~~~

默认路径完整绑定上表的已发表前驱目录和既有 G/W 原式导出。
实际计算还检查 `GITHUB_ACTIONS=true` 与
`GITHUB_REPOSITORY=Rogerhu12/math-research-public`，不允许以普通本地调用跑研究。
本次没有请求 $j=4$ 或更后目标；只有读完新的真实结果后才决定是否需要它们。
