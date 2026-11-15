# R824：原free1187的365位完整断点与同核续算

日期：2026-11-15。状态：**真实预算断点；原27+244准确生成元仍未全部得到。**

## 1. 已结束运行

run43732499815，job132867842693，
source442f3d16a9b914154e8b81bc61597d650044fd61，
于2026-11-15 20:56:05.457300 UTC结束，退出码1。
wrapper error=null；核心实际例外为BudgetStop：
只保完整来源阶段和每个目标的最新lift以供续接。

本次已到原权五free1187的第365位完整lift；
最后阶段日志为lift365、history365及current完成，之后在下一次correction前检查预算时退出。
这不是数学反例，也不把工作流failure解释为准确极模不存在。

已冻结的数学身份保持：
core1ece3cf45f57fda2d1fe40f38efb3e225d2e05ce910a917eb38dbcd85fe3d1cb，
wrapperc590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c。
仍请求权五全部新方向及权六全部已选方向，reconstruct_every_digits=8，预算300分钟。
原free1186继续由R787独立处理，不在R824重算。

## 2. 实际小IO回读

在当前工作区只做标准库Range、SHA和JSON读取，没有导入数学核心。
读取真实artifact的原manifest、run/core/input以及current指针，
共18次Range、266064字节；没有下载完整1.35GB ZIP或51.6MB lift。
来源run/source、API artifact摘要与已下载各成员的SHA分别保留；
不把此次小传输称为全ZIP重新摘要。

| 原文件 | 字节 | SHA256 |
|---|---:|---|
| full-outputs-manifest.json | 181920 | f45e21931d00e1c0ad321e391b7298952760cf15c2087d80c9d24a8b0b408557 |
| run-receipt.json | 425 | 7ac3777f036d0bc6edd1623c40cbf292d83e55858d5c1577de84e93c56e52513 |
| core-receipt.json | 362 | a7f49478d6fed8a00f5c8cc39e82e535396f603799eb568e91dc48942b5f210c |
| public-actions-input.json | 10059 | f5c7d154d57f4f34529e1a5e5b19f093ddfb540c2fb50cda2723f082f0154d8a |
| R824-power5-free-1187-current.json.gz | 5692 | c6ddf4fbe4342370522e47b58e7d2977e6c810f85d1f0068165a74869d724552 |


manifest共725项，ZIP共727个文件。current的complete=true，
保原field/configuration、free1187、ell1000000753、归一“该free为1其余0”，
绑定：

- 最新lift：R824-power5-free-1187-lift-00000365.json.gz，51597850字节，a7a95048d8c1455b395c1d74863f7e1ef0eb7638d3710ab60fb7d824f1aea414。
- 最新历史：R824-power5-free-1187-history-00000365.json.gz，5741字节，f3778c40c9d7f466e51580b0eae09c9b4ae0e9a856b07927b478cd4136fa6627。
- 原必要输入bundle：612745716字节，71b16a02e29ecd682b23ab2cfa475194188acdb41c0380561eeb9af9580983ac。
- retained-inputs-receipt.json：1098638字节，917d5a344a4dac6c457a857ec4382cd950139e6292a86a5268102269156f3cb2。

后两条大输入只从实际manifest登记，未在本地重新展开或验证数学。
下一公共续算由冻结wrapper按全部原字节/SHA恢复和认证。

## 3. 同一核心的下一请求

只把R824-public-original-global-polar-generators-request.json的resume换为上述真实已结束来源；
expected_conclusion为failure。
原core、wrapper、proof、method、八个producer身份、权数、prime、
输入顺序、搜索参数及数学configuration都不改变。

新artifact为14179899060，
serre-global-R824-original-global-polar-generators-43732499815-1，
1357977101字节，
ZIP SHA256 bc2789d423dc4c5c961fdba89c38bd75d59470acc711a40b426f67d9087a9bc1，
到期2026-11-16 20:56:06 UTC。
原wrapper先准确恢复全部已完成R824阶段、原612745716字节输入包和最后完整current，
从它继续；不回到已成初始profile，不重算旧Schur分支或365个已成lift。

准确27个新权五及244个权六生成元全部完成后，
仍须原1778纤维minor/全长1206等已证出口。
现无新的特征零A/B、原函数、极除子、eta或高度值。
