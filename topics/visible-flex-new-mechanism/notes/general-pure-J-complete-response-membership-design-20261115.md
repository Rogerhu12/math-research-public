# 一般 pure J 对完整真权负二响应像的单目标设计

日期：2026-11-15。**新实现与纸面算法；本稿撰写时研究实际尚未运行。** 本地仅运行新增小人工接口；全部真实原根归约及条件性原函数评价只在本公开仓库 Actions 中执行。R151 为后继结果预留号，不预报其成员状态或 pure 维数。

## 1. 实际问题与最小新增范围

[R143 实际记录](R143-general-pure-J-fixed-relation-unresolved-20261115.md) 对固定的 R133 六列表示给出 392 项原差、65 项非零 sound 代表。它没有证明候选为假，也没有证明一般 pure 非成员。继续换一条未经完整覆盖的六列猜测没有付清这个问题。

本次仍只取 [R136](../results/R136-acceleration-coefficient-beyond-response-and-G-orbit.md) 的

$$
J=\operatorname{gr}_{-2}[h^{-4}k^0\omega^0(\log h)^0]\bar A_{hh},
\qquad \pi J=J_{-4}.
\tag{1}
$$

其中 $-2$ 是 profile 仿射权，$-4$ 是相位模式。原 J pure 根有 80 项，SHA256
`2efefe7d9d902bb0050e4f19fc16b09060216c2376530d920ef265ee9ce96ad3`。

R131 的真权 $-2$ 已有完整 50 列、10 条完整原关系、40 个真实基列。消费这 40 个原基列的 pure 根即覆盖 $\pi(R_{-2})$。本次不再编译任何响应，不复算旧完整关系、G³ 目标或旧完整两模式秩。

只检测真权 $-2$ 足以处理 $\pi J\in\pi R$ 的完整一般 pure 成员问题：R105 的缩放表示有限 Laurent，R 仿射不变，$\pi$ 与缩放交换。若其他权的响应组合给 (1)，对该恒等式取权 $-2$ 投影，仍得到由 $R_{-2}$ 给出的表示。不能用其他权混合弥补该齐次成员门。

R138 已证明整个 G 仿射轨道的 pure 像在 $\pi R$ 内，因此本次不追加 G³ 或其他轨道列。完整 J 已在 $R+\operatorname{Orb}(G)$ 外的事实，与其 pure 投影是否属于 $\pi R$ 是不同问题。

新增内容严格限于：40 个已发 pure 原根的单模式归约；由此产生的新 pure 依赖的原差证明；一个 J 的求解与原差；仅在该原差未决时，对 J 和真正保留的 pure 原根作一次原有理评价。幂尾代入、mixed 归约、forcing/W/N/v4/新响应编译均为零。

## 2. 新源及精确输入

新源：[literature_general_pure_J_membership.py](../scripts/literature_general_pure_J_membership.py)，37092 B，SHA256

~~~text
1a84590f8b6f0c35a1df5f251a8ffa0e9f4da65ea2cc3bd777e752482ef05bcc
~~~

它只 import 已发表的 `literature_general_pure_J_identity.py` 及其已绑定依赖；该旧 helper 为 24639 B，SHA256
`ddacad3474844368e3546f4e4b0f92e71eb276363cd283ad4f300259e8161f63`。旧源不改。

沿用旧 `load_original`，逐项绑定主报告、publication receipt、源/run、export schema/content_scope、压缩和原始长度/SHA，以及所有原根 SHA。读取两模式 export 中的 mixed 根只为解析与身份核对；本次研究运算仅选 pure 根。

### 2.1 完整五族原式导出中的 J

目录：`notes/actions-43654534244-1-acceleration_layer_mixed`。

- Run `43654534244`，source `1177f251dc3d9455adf88b585e4c0e4bd6f7e69b`。
- 主报告 `acceleration-layer-mixed.json`，57753 B，SHA256 `baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745`。
- `receipt.json`，35241 B，SHA256 `3c147ca2edaa03d4c27fa0694adca26764c0f98c8fde363387359d8fddccc494`。
- 导出 `acceleration-layer-mixed-original-expressions.json.gz`，318634 B，SHA256 `b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e`。
- 原始 1909429 B，SHA256 `7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38`。
- 原生产者 47656 B，SHA256 `271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c`。

完整 `family_records` 数 314，附加指定权记录 10，原根共 648。J 必须同时对应 `family_0051_-4` 与 `selected_0000_-4`，整个状态根恰只有权 $-2$；不裁剪不匹配的其他项来凑目标。

### 2.2 完整真权负二响应的已证基

目录：`notes/actions-43653293263-1-g_translation_successor`。

- Run `43653293263`，source `2f0add61f44365d713abf836beaa8b0be2806a3d`。
- 主报告 `G-third-translation.json`，25014 B，SHA256 `b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3`。
- `receipt.json`，34619 B，SHA256 `a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523`。
- 导出 `G-third-translation-original-expressions.json.gz`，157782 B，SHA256 `226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e`。
- 原始 889438 B，SHA256 `eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7`。
- 原生产者 39670 B，SHA256 `a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406`。

旧主报告的 `response_upper_bound` 必须给原列 50、真上界 40、完整原关系数 10，关系证书 SHA256 必须为
`a6453e43e03f92bc27c9a278e8115d64ece6eed9ddf1f82febdfd12fd05a9498`。

准确保留的**块内原列号**为

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
20,21,22,23,25,27,28,29,31,32,33,35,36,39,40,41,46,47,48,49
~~~

新 0–39 的消费位置、旧 0–49 的块内原列号、R116 全局号 $8j+a$ 分开记录，不能互换。真实二次/第三索引、第三模板原 SHA 和原 pure 根 SHA 都逐项保留。

这里只消费已经完整证明的 50→40 上界。不会因旧完整两模式的秩为 40 就声称新 pure 像也是 40 维。

## 3. 新 pure 张成与原差证明

记 40 个被消费的 pure 原根为 $C_0,\ldots,C_{39}$。用 R138 已绑定的同右锚 `ProfileNormalizer` 各归约一次，得到 sound word 代表 $w_i$；同样归约唯一目标 $\pi J$。既有 normalizer 不修改，也不宣称完备或对表达式选择必然线性。

在有限有理 word 行上用 `ExactWordSpan` 求消元基。它只提供候选关系

$$
w_j=\sum_i a_{ji}w_i.
$$

对每一个拟丢掉的新 pure 列，重新从原根构造

$$
\Delta_j=C_j-\sum_i a_{ji}C_i,
\tag{2}
$$

交给单独的原差 normalizer，保留其完整原 DAG、有理系数、SHA 和完整归约代表。只有 (2) 的原差 sound 为零，才准删除该列。

若某条候选关系的原差未归零，就把该原列保留在真实覆盖集合中；不能仍按较小的 word 秩给真实上界。设所有已核零关系删去后剩 r 列，则准确得到

$$
\dim\pi(R_{-2})\le r,
\tag{3}
$$

其原因是全部 40 个原函数已由这些 r 个原函数和明确的原身份覆盖。r 不预设等于实际维数，也不以模素数秩亏给新的上界。

随后只求解一次目标。无论其 word 余项是否为零，都从原根构造所提议表示的完整原差

$$
\Delta_J=\pi J-\sum_i c_iC_i
\tag{4}
$$

并独立作 sound 归约。这避免将“若干标签线性组合为零”直接当作完整原式恒等。

若 (4) 归零，则已经证明一般 pure 成员，停止这一个查询，不进入任何原 profile 评价。若 (4) 未归零，仍只记未决，接下一节的一个严格有条件分离门。

## 4. 仅在未决时的一次原有理 pure 评价

只评价 J 与 (3) 的 r 个保留**原根**，不评价 word 代表、不重建响应。沿用已发表准确有理 Volterra evaluator，取一对固定测试函数

$$
t=\xi-2\in[0,1],\qquad
f=[t(1-t)]^8,\qquad
g=[t(1-t)]^8(1+2t+3t^2+5t^3),\qquad q=f+ig,
$$

区间外延为零。所有列用同一个 q、同一个真实右端原函数。只给 evaluator 绑定颜色 q；不允许 $\bar q$ 根进入这个新 pure 计算。

先扫描所有实际原 DAG 的最大输入 jet。只有其所需阶数不超过该零延拓的 $C^7$ 正则性才继续。profile 对不声称满足三矩圆条件；它只用于 universal 原函数分离。原式是有限 jets、乘法和同右端积分的连续组合，故若得到非零原有理子式，可在对应 $C^m$ 范数下平滑这些零延拓并保留非零子式，得到共同空右 collar 内的光滑输入。这是从有限正则测试提升一般光滑非成员的依据。

取 $t=j/25$，$j=1,\ldots,24$，仅保 pure 的实、虚部共 48 行。固定模素数 $p=2147483647$，先确定性验素；所有出现的有理分母必须可逆。输入和积分均由 $\mathbb Q(i)$ 运算在模 p 下的准确像实现，不是浮点积分或随机零判断。

如果 r 个控制列在这些原值上达到秩 r，且加入 J 后存在非零 $(r+1)$ 阶增广子式，结合 (3) 才得到真正非成员。准确泛函为

$$
\Lambda=\operatorname{ev}_{\rm last}
-\operatorname{row}_{\rm last}(A)\,A_{\rm pivot}^{-1}
\operatorname{ev}_{\rm pivot}.
\tag{5}
$$

它在 $\mathbb Q$ 上准确杀全部保留原列，故由 (2) 及旧 50→40 原关系也杀全部原响应。模 p 非零增广行列式证明相应有理行列式非零，所以 $\Lambda(\pi J)\ne0$。原系数为实数时这同时是实函数空间中的分离，不能以复值标签取代两实输出。

若控制秩未达到 r，或没有增广升秩，则仍未决；不把模 p 解当作正的函数恒等式，也不把秩亏当作实际纯维数上界。不更换第二个测试对、不追加余下起始目标、不自动提高预算。

若原控制秩已达到 r，即使增广不升秩，(3) 也准确确定该权 pure 响应维数 r；但 J 的成员状态仍须原恒等式，不能由有限值拟合推出。

## 5. 资源、持久化与消费接口

默认研究预算为 240 s、RSS 1024 MiB、500000 节点、100000 原子、120000 项、每 normalizer 500000 次 IBP 调用、8192 位有理系数。条件性原评价至多 20000000 个多项式运算，最高次数 256。预算耗尽只结束本次计算并保存未决状态，不结束主课题。

主报告 `general-pure-J-membership.json` 保持小于 90000 B。完整证书 `general-pure-J-membership-certificate.json.gz` 至多 2500000 B，完整报告 fallback 至多 2000000 B；总预留小于 4800000 B。完整原数据只由 Actions 自己的终端 Git 发布，API 只读小主报告与 receipt。

证书包含：

- 40 个被消费 pure 原根、唯一 J 及新原差的统一原 DAG；全部原根 SHA。
- 全部新 pure word 代表的完整有理行和 SHA；不只摘要或秩。
- 每条新 pure 候选依赖的准确系数、完整原差与 sound 零/未决结果。
- 唯一 J 的候选系数、word 余项和独立原差完整代表。
- 若进入条件评价，保同一测试对、全部 pure 原多项式模有理系数、行标签、完整值矩阵与增广子式/泛函证书。

每完成 10 个新 word 列、5 个新依赖以及完成上界、目标或最终结果时，覆盖写同一完整 gzip 进度文件。metadata 记录当时的 `phase` 和已保存列数；部分数据不会冒充完整数学结论。旧完整原输入仍由其既有 publication 身份引用，不改写。

新 `decode_word_rows(owner, rows)` 可恢复这些 pure 代表，严格保有理系数、局部 jet、word 和同一 owner。它供后继复用新 pure 行，不能把这些行的 formal 独立性冒充真实独立性。

## 6. 新增小人工开发结果

本地仅运行 `--toy-only`，没有载入任何研究原 DAG。当前源的八项小人工全部通过：

1. 原保留列顺序，以及重复/缺列拒绝。
2. mixed 根不能进入 pure 接口。
3. 新 pure 依赖候选与原差准确核零。
4. 原差未决时保留该真实控制列。
5. 单目标的完整原表示核零。
6. 完整 pure word 行序列化/恢复。
7. 一个新人工 pure 原根的准确有理评价接口。
8. 不允许小于真实覆盖上界的子式冒充完整非成员。

回执 `general-pure-J-membership-artificial-development.json`，16929 B，SHA256
`a7b007b3b91abfb22b386ddec65197fb67f7079c38395fb85e1a9ea95e297246`。用时 0.005374732 s，RSS 15.25 MiB。早期人工调用发现 `ring.x` 必须调用成 `ring.x()`，已在新源修正；此错误未接触研究目标。

以上是小人工开发结果，绝不是 R151 实际已经通过。公开 job 仍先运行本源的相同新人工，再进入单一新研究门；不重跑旧 R143 固定六列问题。

## 7. 准确公开调用与依赖目录

从仓库根执行：

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_general_pure_J_membership.py \
  --toy-only \
  --output /tmp/visible-pure-J-membership/general-pure-J-membership-development.json

python topics/visible-flex-new-mechanism/scripts/literature_general_pure_J_membership.py \
  --family-directory topics/visible-flex-new-mechanism/notes/actions-43654534244-1-acceleration_layer_mixed \
  --response-directory topics/visible-flex-new-mechanism/notes/actions-43653293263-1-g_translation_successor \
  --max-seconds 240 --memory-mib 1024 \
  --output /tmp/visible-pure-J-membership/general-pure-J-membership.json
~~~

研究入口强制要求 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`，不能在本地伪造环境运行。新 lane 可用 `general_pure_J_membership`；上述两输入目录和 scripts 即为必要 sparse 输入，不需要 R133 的大幂尾证书或其他历史 actual 目录。

## 8. 结果解释的边界

成员身份只支付 J 的一般 pure 函数及 R146 已证明的输运范围；它不证明所有 80 起始条目、全部五族或整个 U 的 pure 像都已支付。

真正非成员若成立，则因为 $J\in U$，给一个实际成本空间在一般 pure 投影中的新商方向；但仍不能由独立性推其真实成本正负、实际有符号控制或不可闭合。R138 仍保证整个 G 轨道 pure 落在旧响应像内。

任何未决或预算失败都准确保留。完整 mixed、逐 s ruling、高阶收敛、有限连续族、闭嵌入、全时 reach 与宏观幅度仍须按主课题继续推进。
