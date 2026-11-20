# R671 实际 v3 续步与同场完整首jet、活动非平面

2026-11-20，Astra-larger-resume-24b2ab87-20261120。来源是公开 Actions [44758209061/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44758209061) 已自然返回的[阶段36](2026-11-20-public-actions-44758209061-1-part-002.md)和[阶段37–38](2026-11-20-public-actions-44758209061-1-part-003.md)。全部科学执行发生在该公开runner。新场 `7fd352757ca69554b367f08c6a76f343729aef795f68f218e202e2cacd933c21` 是下面三项共同的实际身份；不从97fd或独立worker03移用几何。

## 1. 同物理模型的实际 v3 续方向

真实父是 `97fdc9ea3af7c24720db940b41a1d783894648984411fbf4aaf026259c3a8dcc`。同级入口425f以keep-q保lambda=1、eta开始节点885、J923/M160/N2048、原scalar g、全部正权行/永久位置/母范数和实际末mu `.0007539530259341321`。QP显式使用冻结v3 `fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4`；atol=0、rtol=1e-6、192工作行上限、256推进预算。

| 项 | 初始97fd | 实际末7fd |
|---|---:|---:|
| 完整 Phi | 9.526119203703808e-8 | 8.52075845296275e-8 |
| max relative Gram | .012594260006200009 | .012090779946503864 |
| 原 Jw | .19157178903063204 | .18886153028536073 |
| 全部已知点必要乘积 | .991950785480054 | .9919745966336464 |

真实接受alpha=.5，因此末mu保持原值。首满步真Phi `7.820234451294882e-8` 更低，但真实几何乘积 `1.0012676361492927`，未通过原`.992`门；不能把这个被拒满步当新父。返回总用时711.816081095秒，方向691.831253128秒，峰值RSS2,266,640KiB。

主QP仍是 `iteration_limit`。原欧氏初梯度 `4.413833219300035e-6`，停止容差 `4.413833219300034e-12`，末活动面投影梯度 `3.855561724075194e-7`，未达驻点条件。实际A/A*次数265/266，最长同面推进30，末真实线性残差已重读且报告相对递推缺陷0；不据末缺陷0就称整个优化收敛。

有11个raw负乘子，但最大规范化释放增益 `1.0771323078210294e-8` 小于这一步的实际释放阈值 `3.855561724075194e-8`。因此不能因raw最小乘子 `-.00029510113818817193` 独自宣称需要释放或释放代码失效。最大原线性违反仅 `1.0842021724855044e-19`，也不替代真实非线性几何筛。

这是真实后继父上的v3续算，不是同一个起点的v2/v3对照。没有无条件32步Krylov重启的源码性质已落实，当前数据不能单独量化其因果加速；同面长度、活动约束和几何允许步长仍独立。后续采用已准备的固定PCG加一次SOC，继续同7fd实际父、同lambda/eta、真实末mu和全部位置，不放松几何门。

## 2. 同7fd全922胞首jet及原闭体包围

完整R674读取器f122使用该新场自己的profile，同原整数scalar，全部角尾。实际 `complete_scope=true`、`embedding_certified=true`，并包括准确两帽与反射闭合：

| 已支付项 | 实际包围 |
|---|---:|
| 全域support下界 | .2945585763805267 |
| 最小法向平方下界 | .0068329523830282035 |
| 最小E下界 | .8356711639816239 |
| 原闭体连续D上界 | 4.118969405015079 |
| 固定见证点到整像距离下界 | .9393749684495676 |
| 原闭体held/D下界 | .22806068122424628 |
| core rho连续下界 | .15243018787425183 |

总用时66.273385812秒，报告核60.314219527秒。296个已保存解析尾锚、37次cache使用，未新增整数oracle anchor查询。完整实际配置为first/all、层次`256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96`、角Taylor12、scalar degree5、radial block4、panels128、beta=1/4、support目标.14；完整argv与来源在阶段37。

该first报告自己的 `nonplanarity_certified=false` 与 `marker_certified=false` 如实保留。独立后处理可以新增不同责任的证据，不能伪改原报告flag；这里也没有完整连续K或reach证书。

## 3. R675 同场活动内域非平面实际应用

冻结b36消费者直接使用上述同场完整嵌入报告和新7fd的准确有限高度jet，实际返回 `status=proved`：922个原胞全部满足非零高Z高度条件，最小选中绝对值为准确有理数

$$2970929898641149/144115188075855872.$$

准确正宽度、两镜像活动片、所有原胞非平面及“任何与活动内部相交的开片不为平面”均已支付。已知平帽内部明确排除。该应用没有再次计算嵌入、场值或scalar oracle：报告核.149435720秒，总入口6.017099804秒。

这是R675已有命题的真实同场应用，不新占结果编号，也不冒称四固定marker已经构造或Euclidean shape幅度已经支付；后两项在报告中均为false。完整曲率、连续metric和持续同g精化仍未完成。此新场的连续metric任务已排且尚未返回；不把原有限max当连续upper。

## 4. 实际文件与源身份

下面路径相对本run `research/`，完整输入SHA与来源提交见上列阶段卷。

| 文件 | SHA256 | bytes |
|---|---|---:|
| exact-tail-full-phi-v3-continuation/report.json | `8b1935fd34e6bb3b30415302506043e61f61827d62a42a1a991e3dd6efb5a1f7` | 10979585 |
| exact-tail-full-phi-v3-continuation/final.npz | `7fd352757ca69554b367f08c6a76f343729aef795f68f218e202e2cacd933c21` | 10381126 |
| exact-tail-full-phi-v3-continuation/exact-tail-lift-profiles.json | `cbebbbbd2abb771cc03d944f7ab3ff48fe883238aab8dfd2be3c560ba151b0a7` | 11249 |
| exact-tail-full-phi-v3-continuation/exact-tail-lift-profiles.npz | `37c952dac200c6569a8c7a39be1212f465001c112b441ebd087be94e272da78d` | 150840 |
| exact-tail-full-phi-v3-continuation-continuation-inputs/continuation-plan.json | `2c93e99901652957682c9e79ba330399075eab985cda87eb8eab870927abe813` | 37069 |
| postprocess/reference-tail-first-geometry.json | `1ddf4a1d388b6ef51f3e671ebcda7edd3c5a705b2a89d21a9975326fb78b36be` | 1032258 |
| postprocess/reference-tail-activity-nonplanarity.json | `210c6e0241149d1068f6c3fa95c4f336bdb69c18ed2163b8d084b5700bfe969c` | 37438 |

续步入口425f、首jet源f122和非平面源b36的实际完整SHA分别为：

- `425fd1d1254450afac26b2ca29ca4ffbb6fb93d59588163bef726e34999e4703`，源提交 `06a3b593f2e921f5c2734872410e2dba4e353e91`。
- `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225`，源提交 `12b9f68d8cad972be883a73cfe998918d5800759`。
- `b36d387fed072235e1aec8e77da130c9c9be095aed64be46485fc0890b21c09d`，源提交 `65636d182ad212e508ec0a67fa1b06da4e4877f9`。

所有报告的canonical模型都是 `b6adb4df6dbd85d6a940b45af44225adf18212e3dfc7f5744aa03144be04341a`。profile NPZ与旧同模型的字节相同不意味着场相同，场仍须绑定实际final bundle。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
