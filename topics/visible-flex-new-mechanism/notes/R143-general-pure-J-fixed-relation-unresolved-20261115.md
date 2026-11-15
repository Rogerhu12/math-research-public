# R143 实际记录：J 的一条一般 pure 原式表示仍未决

日期：2026-11-15。**已完成的准确计算记录；一般 pure 成员问题未决。** 本次公开 Actions 检查了一条由已发表幂尾证书给出的固定有理组合。其 392 项原差经 sound 归约得到 65 项非零代表。归约并非完备，故本记录不证明该候选恒等式为假，更不证明 J 的一般 pure 分量不属于响应空间。

本记录放在 `notes/`，不将未付的函数非成员结论登记为定理。来源为 [R133](../results/R133-complete-m8-pure-cost-range-and-exact-tail-payment.md)、[R136](../results/R136-acceleration-coefficient-beyond-response-and-G-orbit.md)、[R138](../results/R138-general-pure-G-identity-and-affine-orbit-kernel.md) 及[本次设计](general-pure-J-one-original-relation-design-20261114.md)。

## 1. 被检验的准确目标

保持完整 canonical 相位约定、同一个右端 collar 和原函数锚。令

$$
J=\operatorname{gr}_{-2}[h^{-4}k^0\omega^0(\log h)^0]\bar A_{hh}.
$$

下标 $-2$ 是 profile 仿射权；下文 $J_{-4}$ 的下标是相位模式。二者不同。R136 已证明完整两模式的 J 属于真实成本空间 U，且不在 $R+\operatorname{span}\operatorname{Orb}(G)$ 中；这一完整函数结论不能替代本次一般 pure 投影的成员问题。

R136 的原导出中，J 的 pure 根为 `selected_0000_-4`，也恰为整个状态根 `family_0051_-4`：这个状态系数本身只有真权 $-2$。它有 80 个原项，SHA256 为

~~~text
2efefe7d9d902bb0050e4f19fc16b09060216c2376530d920ef265ee9ce96ad3
~~~

R133 的 `acceleration_quadratic` 组、几何系数编号 81，给出了其 $m=8$ 幂尾在六列响应中的准确表示。原十键为

~~~text
[-4, 0, 0, 0, 0, 2, 0, 0, 0, 0]
~~~

键顺序是 $(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss})$。此处只读取已发表表示作为一般函数恒等式的一个候选，没有重新代入幂尾，也没有预设幂尾投影忠实。

令 $C_i$ 为 R116 全局编号 i 的完整响应，编号规则为 $i=8j+a$，其中 j 是第三模板编号，a 是二次算子编号。所检查的唯一原差为

$$
\Delta=J_{-4}-\sum_{i\in\{0,6,12,13,26,34\}}c_i(C_i)_{-4}.
\tag{1}
$$

固定系数及与 R131 真权 $-2$ 原导出列的对应如下。

| R116 全局 i | R131 块内列 | 二次 / 第三索引 | $c_i$ |
|---:|---:|---|---|
| 0 | 0 | 0 / 0 | $52417629565513761/1575930037032578608$ |
| 6 | 34 | 6 / 0 | $1097809599290443/196991254629072326$ |
| 12 | 26 | 4 / 1 | $74015947055645095/37822320888781886592$ |
| 13 | 30 | 5 / 1 | $164536405113426417/12607440296260628864$ |
| 26 | 16 | 2 / 3 | $18912999385454629/3151860074065157216$ |
| 34 | 17 | 2 / 4 | $-6818100659546139/787965018516289304$ |

块内列号不能当成 R116 的全局列号。消费器按二次 / 第三索引及其原 SHA 逐一绑定。所有根已经含 canonical 模式归一化；本次没有再乘或除任何 $16$、$128$ 或其他相位因子。

## 2. 已发表输入的身份

J 来自公开 run `43654534244`，source
`1177f251dc3d9455adf88b585e4c0e4bd6f7e69b`，lane `acceleration_layer_mixed`：

~~~text
notes/actions-43654534244-1-acceleration_layer_mixed/
acceleration-layer-mixed-original-expressions.json.gz
~~~

压缩 318634 B / SHA256 `b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e`；原始 1909429 B / SHA256 `7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38`。

六列来自公开 run `43653293263`，source
`2f0add61f44365d713abf836beaa8b0be2806a3d`，lane `g_translation_successor`：

~~~text
notes/actions-43653293263-1-g_translation_successor/
G-third-translation-original-expressions.json.gz
~~~

压缩 157782 B / SHA256 `226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e`；原始 889438 B / SHA256 `eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7`。

固定系数的旧 R133 证书为 `geometry-ibp-certificate.json.gz`，压缩 483512 B / SHA256 `a62173b39804ab7f3b0c1f14a23f840a81813717bb8ce88d7659c0e64e90e2f1`，原始 4472950 B / SHA256 `3e0b01e2d7e3ed6634420524ea99ab8d4a9a56c280dd9a2da35365dca02067c7`。旧实际没有重跑。

## 3. 本次公开实际与完整输出

- Run：`43656084792`，attempt 1。
- Source commit：`82f3a12e75db8820fd25698c61089513d4c439aa`。
- Lane：`general_pure_J_identity`。
- 新源：[literature_general_pure_J_identity.py](../scripts/literature_general_pure_J_identity.py)，24639 B，SHA256 `ddacad3474844368e3546f4e4b0f92e71eb276363cd283ad4f300259e8161f63`。
- 设计：11539 B，SHA256 `91cb8722afd11234f26d1dd209958ac83b06833c0ffbc0bbdacecb6f6b17afc7`。
- 完成状态：`complete`；研究结果字段：`unresolved_nonzero_representative`。

公开目录为

~~~text
notes/actions-43656084792-1-general_pure_J_identity/
~~~

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `general-pure-J-identity.json` | 28753 | `ae03942be08c485fbf7d28aa62893f3b9528264cd64413440757547c1f07a903` |
| `receipt.json` | 35416 | `f78bec609d755b37881b1207c9eccddead02828827f29477d647f656f25ad3c9` |
| `general-pure-J-development.json` | 15634 | `f1b937161053fa9ae327e842095359cbc28ea2773d8a9391eb12298730f25c82` |
| `general-pure-J-identity-certificate.json.gz` | 15409 | `f01f2086a63569109b0051ad410c0ee715c421efaa3e48c0386aa5da4f2093f9` |

证书解压后 72868 B，SHA256
`8f59df432abb6b9120ae0146e7d88619f4dd15ed6d9aa5cef7bb78b37f994e12`。其中保存原 J、六列、原差、准确有理系数及归约代表；不用从摘要猜测原表达式。

同一公开 job 的三个新增小人工检查全部通过：全局列号与块内列号区分、重复算子对拒绝、带符号有理线性组合及未匹配项保留。它们未载入研究原 DAG，也没有重跑旧开发查询；用时 0.002931560 s。

研究实际用时 1.282467392 s，峰值 RSS 95.46875 MiB。输入身份、源 SHA、publication receipt、压缩及原始数据身份、原根 SHA 均由本次小主报告保留。

## 4. 准确得到的归约事实

先在原四次 pure profile 代数中形成 (1)，不对原函数值独立赋值。原差有 392 项，其 SHA256 为

~~~text
791bca3d02f59dac849aa09aae3c0cd59d6857ba2989f8f7fb588eb583d0ef70
~~~

随后仅对这条完整原差作同右锚的 sound 分部积分与 word 归约。所得代表有 65 项，最大局部 jet 阶为 2，最大 word 长度为 2；SHA256 为

~~~text
84daa76768fa50176218200bec11184921a5d75f31baba36723f4d928216f4a2
~~~

右分部积分计数：276 次 primitive 调用、175 次唯一最高 jet 改写、13 次第一层 shuffle、3 次幂 shuffle、0 次 cycle fallback。word 层 63 次 primitive 调用、10 次全深度 shuffle、14 次非空 word 多项式分部积分、0 次 cycle fallback。这些只是完整实际的运算记录，不把某种改写计数作为数学完备性的证明。

新增 pure 响应原式、mixed 响应原式、profile 评价、幂尾代入均为 0。旧 forcing、W、v4、N 响应编译为 0；旧秩及原依赖复算为 0。新计算范围恰为从已发原根形成并归约 (1)。

**本次可以确认：当前 sound 改写没有证明 (1) 恒零。** 非零代表可能仍含尚未使用的真实函数关系。没有原有理函数分离值或完备商论证，就不能将其改写成 $\Delta\ne0$。即使未来证出这条固定候选不成立，也不能由此排除 J 的其他响应表示。

R133 的完整 $m=8$ 投影恒等式仍成立；本次结果没有与它矛盾。R138 的一般 G 恒等式也仍成立。没有重置左尾、改换右锚或把一个局部密度非零冒充实际周期非零。

## 5. 实际结果指向的下一门

下一目标继续只取这个 J。R131 已保存真权 $-2$ 的完整 50 列和已证明的 10 条完整关系，给真实 R 的 40 列基。只投影这 40 个已保存的原根到 $-4$ 模式，就完整覆盖该权的一般 pure 响应像；无需新增响应编译。40 是完整两模式维数，不预告 pure 维数。

对这一完整 pure span 求解 J，若得到有理表示，应从原根形成并 sound 证明相应整条原差为零。若仍余未决代表，只有进一步付清真实 pure 上界及原函数分离证书后，才可作非成员结论。R138 已证明整个 G 轨道的 pure 像落在 R 的 pure 像中，因此此成员门不需要再追加 G 轨道列。

这个下一门仍不涉及幂尾扫描、重算完整 mixed、余下 79 个起始系数的盲扫描或已成原式的重复编译。任何成员结论只支付指定一般 pure 函数及已证明的协变范围；真实成本符号、实际有符号控制、完整 ruling 和课题完成标准仍须另付。
