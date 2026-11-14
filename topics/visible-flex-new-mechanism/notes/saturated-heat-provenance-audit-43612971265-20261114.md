# 首轮饱和热延拓：来源与冻结状态审计（43612971265）

日期：2026-11-14。状态：来源、文件及准确状态核对通过；课题未完成。本稿只读已有 Actions 输出，并重算文件摘要、JSON 身份摘要和准确有理系数。没有在本地重新评价研究几何、运行优化或更换候选。

本审计与机制代理的实际几何审计互补。workflow 成功、输出身份正确与几何达到目标是不同事实；本轮求解器在 250 次函数评价预算处终止，`success=false`。

## 1. 准确来源与发布回执

- 仓库：`Rogerhu12/math-research-public`。
- Actions run：`43612971265`，attempt `1`，lane `ellipse_saturated_heat`。
- 实际执行源码：`228c619517f1c67e87769b5db0fdf162a8a10600`。
- 原始归档：[actions-43612971265-1-ellipse_saturated_heat](actions-43612971265-1-ellipse_saturated_heat/receipt.json)。
- 发布者从源提交 pull/rebase 到 `eb291d1ffef8e64abebbc90048a50aa9a70c6a35` 后，记录根 README 与本题 README 均无差异；回执 `readmes_read_commit` 为该提交。
- 回执明确 `design_is_not_fixed_metric_refinement=true`、`task_complete=false`。这与本轮保留同一度量而改变物理帽及热基场的事实相容。

回执列出 **77 个来源文件**。本代理直接对共享树检查其中 74 个的原始字节数及 SHA256，全部相同。其余三个文件在本轮后因新 lane 发生了明确更新；根代理从上述执行源提交逐文件 `git show`，对全部 77 个的原字节和 SHA256 再核，全部匹配。三个不能以最新工作树代替旧源的文件是：

| 文件 | 执行源字节数 | 执行源 SHA256 |
| --- | ---: | --- |
| `.github/workflows/visible-new-mechanism-search.yml` | 48037 | `8850107146b1a1f710fc0bf8d5d80c859fcc1adfea6025380a7b977a86a5874a` |
| `scripts/publish_actions.py` | 14660 | `a491c30c513c4df3f55b1eb60c6fcd030705f1ff723b8adadabd89212d7c436c` |
| `computations/request.json` | 1264 | `8eb1e420d6d274a1a4b40bbc30173590e1701741c60a2615d9cda6aa47d763e1` |

另外，主报告自己列出的 **13 个实际求解依赖**全部同时匹配回执、共享源码字节及此前已核冻结 SHA：

| 求解依赖 | SHA256 |
| --- | --- |
| bent_flat_tail_port.py | `26f32a6ed77c82a2c67320ecbdf12031a3186fa5ae1a83b553ac722a7593dcfa` |
| cosine_connector_radial_seed.py | `662292c1603a834e8295f7b36648f3c16f3b3904383c883dc8aa7faee4e40fc5` |
| ellipse_frame_port.py | `4371f3d816c913b0e7a34f5568672f8f318fd3a923c83e3b28e3ec731c67689b` |
| frame_collar_bent_tail.py | `b62725bb7e82349306dd041f59529d54f32e7bea8c5cca413b3a27b515ffe6ab` |
| frame_collar_bvp.py | `64dffdbfc6456fe022105d264442d307c8f88022cdf755ec0a41ea97fff93d00` |
| frame_collar_enriched.py | `1b2557048c8b02b75201d151bf3ceb89d046734f93a9195bfe283c620a10f028` |
| frame_collar_polygonal.py | `56a4013f78aa120bb2eaa17e430c6212f4af808fb7e87951a26164129bc0aaaa` |
| frame_collar_polygonal_heat.py | `15dec10f4adbe5f7adce7f0a6f3abbfbfbe0fcdf14d52f1d08272cb1246a209f` |
| frame_collar_polygonal_saturated_heat.py | `483d0decb4cedd083ee3c9da8b499096c4aa51b3c23bb0140f8f7281f5a248fa` |
| frame_collar_residual_audit.py | `58d972ec1dbbaba35d1ed1600ea14f1cd5934601cf5f7a209e95795e5099b9ee` |
| polygonal_flat_tail_port.py | `3870844de95284c570839f489a6c6be74c825cbf6631d21684ff4374cae78797` |
| polygonal_tail_heat_extension.py | `abb965c27ce1aa19acd74a54cf301b3ff5589182a116d69819963717d56aa699` |
| polygonal_tail_saturated_heat_extension.py | `cda1570637d8b9bdc8d5891a944ee6fc2a6a2252d56141c2a6b8053b73ccfcdc` |

没有把后来更新的 workflow 或发布脚本冒作本次执行源码。

## 2. 八个输出的压缩及原文完整性

所有文件均按原始字节读取；gzip 另行解压，并独立核对压缩字节数、压缩 SHA256、原文字节数、原文 SHA256。八个输出的四项全部匹配回执。JSON 读取同时拒绝非有限常量。

| 输出 | 保存 / 原文字节数 | 保存 SHA256 | 原文 SHA256 |
| --- | ---: | --- | --- |
| Gaussian-heat-development-check.json | 15712 / 15712 | `96a7a158f6ced04e5db394bf41db2ddfddc48ad68a140406a5f56b991012969d` | `96a7a158f6ced04e5db394bf41db2ddfddc48ad68a140406a5f56b991012969d` |
| frame-ellipse-six-cap-saturated-heat-fixed-checkpoint.json.gz | 170116 / 1029006 | `969a144e05c3dd58b1aa46785fdb900229f3125e0f410c1337de889133d34959` | `085ff0fd86b108a7ab62352c98636a284ce422107a53dcb681d4e687d32f285a` |
| frame-ellipse-six-cap-saturated-heat-fixed-initial-heat-comparison.json | 4322 / 4322 | `c5f875217524fefc611660c2b9a2c7921431cebe0ed994a5b7bca048937d9147` | `c5f875217524fefc611660c2b9a2c7921431cebe0ed994a5b7bca048937d9147` |
| frame-ellipse-six-cap-saturated-heat-fixed-old-ball-replay.json | 10516 / 10516 | `014110d71d1cb44258bc57f49aed73720f9181cc544d1bd47a8f0e4053102356` | `014110d71d1cb44258bc57f49aed73720f9181cc544d1bd47a8f0e4053102356` |
| frame-ellipse-six-cap-saturated-heat-fixed.json.gz | 170116 / 1029006 | `969a144e05c3dd58b1aa46785fdb900229f3125e0f410c1337de889133d34959` | `085ff0fd86b108a7ab62352c98636a284ce422107a53dcb681d4e687d32f285a` |
| frame-saturated-heat-development-check.json | 10785 / 10785 | `ab912cb87606e4163fbeefc56a607f87a8584e99e523384b7159457dd9981457` | `ab912cb87606e4163fbeefc56a607f87a8584e99e523384b7159457dd9981457` |
| polygonal-flat-port-development-check.json | 3960 / 3960 | `79f8b29c06c7bfaa972099a9a40a228d40b864520ed9d5ec7dd032f8df62832b` | `79f8b29c06c7bfaa972099a9a40a228d40b864520ed9d5ec7dd032f8df62832b` |
| saturated-heat-development-check.json | 5211 / 5211 | `e1f6e18cbf3b6cdd09b542bfbc0424f3c7d76b6df5690b7fbdd9d941a2b63036` | `e1f6e18cbf3b6cdd09b542bfbc0424f3c7d76b6df5690b7fbdd9d941a2b63036` |

最终主报告和最终 checkpoint 不仅解析后相同，其 gzip 原字节也完全相同；两者原文都是 1,029,006 字节。这是同一个已选最终状态的两个保存入口，不是两次独立求解。

## 3. 暖源与新状态没有混淆

唯一暖输入为 [43604231319 的冻结 enriched 报告](actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json)：

- 原文件 987,644 字节，SHA256 `6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3`。
- 暖源执行提交 `f64c2c0daa077f9e13aa12f0475e3eeb069a191c`。
- 暖源数学状态 `56f1e738059a135d7ecd6c9c6d04293018a46b29f416945c28781c5333c8d3c8`。
- 暖源角/径向空间 `c293bdac88cf10bd5df59cea964f5fc3564b4018feb377379fbf1c5994067fbb`。

主报告的 `original_enriched_model_record` 与暖源实际 JSON 中每个对应字段完全相同；锚中的准确系数、原空间、原完整度量字典也分别全等。初值没有裁剪、重拟合或换用后来失败的 bent-tail 状态。

暖源与新最终状态都包含 234 个系数，角列计数为 `u=9,v=8,beta=9`。逐个将 JSON binary64 数转换成 `Fraction.from_float`，与记录的准确有理字符串比较，两个状态全部匹配。最终优化后 234 个系数均与暖源不同，这是同一新模型内的实际优化；不将初态与末态称为同一数学状态。

新末态的全部十项 canonical JSON SHA256 均由内容独立重算匹配：

| 身份 | SHA256 |
| --- | --- |
| full_model_definition | `6a1313b7046c77d7cb2e3d697b842af61be61a5cd0d1aa1c93002b9b5efba535` |
| space_definition | `7700fa5ec0a3f3619b10216b8673a77c7b298710c8f9919cfa2eeb448b05b3ab` |
| base_anchor_definition | `5171d9676cd0a3928ff37419b92f270061d0e67b48838cfc40b22b74413f3ae0` |
| heat_extension_identity | `80b6f204958f3aa632860cfe346d2ca93fdcaad0fc6272afda2603a71c780497` |
| tail_physical_identity | `110199445b89af16ca7550aef276a84af534eda5b9b3eb9d1b619dc4a472cf10` |
| core_physical_identity | `caaf925860078f5a8fd654e25b69c2cccb417a5cc9795deb76a2c9887b85c4fb` |
| port_identity | `bf2811f3fa53879dc99951cb6b0e0e126c9ddeded34a9c49e56a2a3c27999226` |
| sampling_definition | `37fa4f2517c65a467d3c315beed07fa5c031d3570908636fdcfff849cb7f186b` |
| shape_budget | `8bdade0d6a86df169ba886cf9a6fbdc114e2ebc76833dfeb6536b4cad69ebd14` |
| mathematical_state | `e266cb0dcb9f5d528e19a30e9a6722091b2035abf0ddbd6df4f6634f7c7c585e` |

数学状态主体还逐字段核为“准确模型 SHA＋当前 234 个准确有理系数”，没有以打印后的短小数重新定义模型。

## 4. 同一准确度量与明确改变的物理模型

本轮 `metric_model` **整个字典**与暖源完全相同。径向种子的数学身份为
`ce41cbe5b74f4c20862ecb9042c714d6507259eea602a8590c5beab11234152f`；
整体度量数学身份为
`f8b81d3a177457f084cbf04379bb9979036f98ce2a8d7e2fbf04fccaadbdf870`。
这两个摘要也独立重算匹配。此处 `log_basis_free_count=0`，准确 log-metric 系数为空，故本轮没有在求解中改变径向度量。

准确核心仍为长半轴 1、短半轴 7/25、半宽 1/50 的椭圆柱；周长定义保留为准确椭圆周长除以 2π，未冻结成某个求积小数。连接长度 9/10、末内盘半径 11/50、末段 S11、负曲率参数 3/10 等完整身份均未变。

物理帽、固定基场及目标包围条件则确实改变：本轮为 R44 的二重对称六帽、`c=w/4` 的饱和反射、无限热定义、球半径 101/100 与条带半宽 19/50。这一变化是新的连续表示/设计，不能把它与旧纯平尾 enriched 模型直接作同物理场精化比较；保留同一个 g 并不消除这种区别。

## 5. 初态及末态 GH 比较确实固定状态

核对不仅依赖输出的 `true` 字段。按源脚本的完整字典构造，分别用暖初系数和新末系数重建 `identity_bundle`：它同时包含 model、space、anchor、heat、metric、tail、core、port 和全部准确系数。所得 SHA 正好是：

- 初态 GH32/64：`9bb46da7fa09d6d1a24357f046cf442d00c991d849f684cb9c26d78b2d29c8cf`。
- 末态 GH32/64：`677775c6c21a712361d74b5118b51f3207d78a9030536d7bf394d791d2f65eeb`。

两组之间因优化而改变系数；每一组内部的物理模型和系数保持相同。对 model、space、anchor、heat 的任意嵌套层检查，均无 `GH_order` 或 `heat_order` 数值身份键。GH 阶数只出现在评价定义中。

初态 61×192 比较的 value/s/theta 最大差为 `1.0775144148933435e-5`，低于事先固定的工程门 `1e-4`；初 cost `0.0864240012904799` 低于工程限 1。因此规则选择 GH32，并没有执行 GH64/128 追加分支。之后仅在 GH32 上运行一次、最多 250 nfev 的优化；所有已存历史行均为 GH32，最终 `nfev=250`、`njev=250`。`evaluations_seen=251` 中的额外一次是源代码在 solver 返回后的显式目标评价，不是第二次优化。

同一 GH32 目标的已选 cost 从 `0.0864240012904799` 降至 `0.08061707650183658`。末态 GH64 只是同一 234 系数的重新评价，未再优化。

| 同状态求积差 | 初态 61×192、中心 GL4 | 末态 121×384、中心 GL8 |
| --- | ---: | ---: |
| scalar value | 5.7491199800807635e-8 | 7.265341483986276e-8 |
| scalar s | 1.0775144148933435e-5 | 1.9252754170695496e-5 |
| scalar theta | 6.043698212332416e-6 | 1.2573552221395445e-5 |
| scalar ss | 6.76906922467424e-3 | 9.6208142690557e-3 |
| scalar ss_theta | 1.5103476738640893 | 2.147266776540846 |
| reconstructed R | 4.502647096962444e-6 | 1.2602344311951523e-5 |

这些是同状态离散比较，**不是无限热积分的连续误差界**。尤其高阶 scalar jet 差明显较大，不能由初态工程门推得曲率证书。末态细网的两个 cost `0.07747839824575421` 与 `0.07747839827401803` 也不应与粗网求解 cost 直接相减当成进一步优化：网格和中心求积阶均不同。

末态的 Π 角加密单独固定 GH32；GH32/64 比较单独固定 121×384 网格和中心 GL8。报告没有将这两种评价变化混为一个“新解”。

## 6. 旧报告回放与前缀检查

独立旧球预算回放保留原尾、原度量和原 234 系数，使用原已发表的 121×768 网格。将回放实际 JSON 的六个主要摘要直接与暖源原 JSON 比较，全部完全相同：

- R 最大样本 `1.5992538243182652`；
- metric 相对算子误差 `1.7279955894758574`；
- 面积最小样本 `0.2199999999999999`；
- 主曲率绝对值最大样本 `39.11621322010752`；
- 原高度正违反值 0；
- 原 signed-side 高度余量最小值 0。

旧场在新球/条带下的样本极值是 `0.9849302796139343` 与 `0.9612481269375266`。这仅说明这个网格上的新包围检查，并未把旧场的明显度量误差变成合格候选，也未给连续包含证书。

初态新模型与旧场在补丁前缀至 t=0.746 的同网格回放中，X、Xs、Xt、Xss、Xst、Xtt 和 R 的差均为 0；度量与初始自由系数逐位相同。它是准确身份的数值回放核验，不等于全连续几何证明。

独立保存的 old-ball-replay JSON、initial-heat-comparison JSON 与主报告的对应内嵌对象逐字段完全相同。

## 7. 四个人工开发检查的真实差异

三个独立人工检查——准确六帽端口、原 Gaussian 模块、饱和源模块——在 Actions 中的 JSON 与此前冻结的本地开发 JSON 原字节相同。

完整饱和 runner 的开发检查原文 SHA 由本地
`af6c033facaccd6a25a66985a63c649f585b03acae06033018102b3be9bdf8d2`
变为 Actions 的
`ab912cb87606e4163fbeefc56a607f87a8584e99e523384b7159457dd9981457`。
递归逐叶比较只发现一个浮点结果不同：

`checks[0].full_parameter_Jacobian_relative_error`
从 `3.369883139609635e-9` 变成 `3.3781307072815307e-9`。

所有其他数值、源码身份、模型身份和状态标签完全相同。可准确记为这一浮点评估末位差；本审计没有猜测具体库或硬件原因，更没有用不同 SHA 掩盖一次模型替换。

## 8. 审计结论及未付范围

本次数据可追溯到明确的公开执行源；来源、输出、准确系数、冻结度量、GH 同状态比较和旧场回放核验均通过。它保存了一个真实运行到 250 nfev 的新连续表示内候选，不是阶段报告中虚构的数值。

这些核验不能推出达到题目要求。主报告仍明确：连续热积分误差未证、连续 metric 未证、嵌入未证、完整闭面未构造、全曲面 reach 未证、`task_complete=false`。实际几何是否合格应读取本轮的独立几何审计，不以发布成功或工程门通过代替。

另外，新的三阶 Cauchy 窄类障碍证明针对当前有限解析自由空间的准确 R=0；它不提供正残差下界，故既不删除本轮真实近似输出，也不将本轮失败扩大成一般 C2 连接不存在。
