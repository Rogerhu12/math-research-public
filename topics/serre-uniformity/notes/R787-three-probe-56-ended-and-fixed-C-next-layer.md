# R787：56维增量三probe的实际结束与固定C后继

本篇只登记实际公开运行与已有准确拒绝的含义。
原目标仍是同一个原power5函数关系；没有恢复真实A/B，也没有得到beta、eta或高度。
这一有限队列耗尽不是关系不存在的证明，更不能推出原430位不足。

## 1. 实际运行及读回

数学运行是
[run43754407301](https://github.com/Rogerhu12/math-research-public/actions/runs/43754407301)，
job132935305617，source
`1827d794565f94455e4f251f20d1979b55fee783`。
原核心为
`c642ec35823dace0ccac4e225e43581398dcce5737dd51cae6a2a903f6028700`，
包装器为
`7449600243a81bd31b5109fdadd0da2e3aa1930fea00772761154703555d4ed9`。
核心收据记录1275.36323109秒，exit2、error=null、complete=false。

实际小IO是
[run43757804966](https://github.com/Rogerhu12/math-research-public/actions/runs/43757804966)，
job132945626587，source
`159a739622e264ea8dd1f0a400c0cb7ab0fd40d5`，
reader
`4ceb3d896cedec19263a5b3e5a0f734725004c54ff229cf642c473d375cbef19`。
该次只读既有阶段，不导入数学核心，不重做LLL、旧Dixon或任何候选准确验算。

原ZIP有186个文件，manifest含184项。
纯IO逐字核对全部182个非carrier文件；两个carrier只核原manifest身份，
不把未重下载的carrier说成此次已重新逐字核。
数学运行结束时原冻结verify已经核过1380个原输入和138个旧42维来源文件。

## 2. 实际56维范围

第三probe确为原A的第0个坐标，三probe索引是C0、C1、A0，
其合并坐标编号为0、1、1214。
旧42行构成完整整数格基，其基变换行列式为1；
新增56行的基变换行列式为−1。
输入56行、LLL原始56行和完整幺模见证均已保存。
因此本次没有把短行子格冒充完整格，也没有再次运行旧42维LLL。

本次实际情况为：

- 新的准确候选验算56个，引用旧准确拒绝0个。
- 56个候选均为原ell处单位；14整数D的最大分量位数在9641至9643之间。
- 56个候选的第一次非零关系阶全部是1。
- remaining_schedule为空，candidate_search_exhausted=true。
- 节点、格数、时间三种budget_reached均为false。

这些是原实际字段，不从请求中的56节点预算反推执行数量。
每个完整拒绝都有对应结果和closed-work receipt；只有该已完成失败候选的大payload退役。
全部56行和原完整准确失败记录仍在一日artifact中。

## 3. 准确含义

原消元式强制第0阶成立。
实际first_nonzero_relation_order=1说明每对被构造的整A/B在第1阶就不是关系。
false FINAL中的exact_verified_orders=0是完整成功出口的计数，
不能解释成每个候选没有通过第0阶。

三probe含原A0仍不足以强制全部A坐标成为真正有理数域解；
在模M的同余类中选择中心代表仍可使准确残差非零。
本次否定的是这56对具体的整A/B。
它不排除保持同一个C而改变A的其它可能，也不排除其它D。

旧42维候选同样在第1阶失败，但不能把其拒绝改名为本次新验算。
本次来源字段明确记录没有引用旧拒绝。
两套完整D来源将交给不同的新障碍消费者，旧129阶验算不重复。

## 4. 已证后继接口

[固定C下一模层方法](R787-original-fixed-C-next-digit-obstruction-and-shared-source-contract.md)
已经证明，对去content前的固定整C，可以使用

$$
\Omega(C')=D\Omega_0+P(C_yq_C)
$$

消去全部A的提升选择。
先在原280维整坐标环模Mell求残差、逐坐标除M，再按原selection求分支及还原clear；
次序不能颠倒。
该计算只复用已成的A模ell逆，原selection已有所需各支kappa逆。

当前先实现branch0及原70个q块覆盖的146个剩余行。
若任何一个坐标非零，则严格排除这个固定C与任意准确A组成关系。
若全部为零，只能报告这一前缀必要条件通过。
该scope不降低原129阶完整正面证书的要求。

新的Omega数值、固定C排除及更深current在本篇登记时均尚未得到。
原430位同核续算和其它真实原函数消费者继续进行。
不重算430位、旧格、原14支大逆或已完成失败候选的大payload。

## 5. 下一消费者所需的真实来源

下表只保存重新取得必要一日输入的身份；原始矩阵、整数行和机器证书不进Git。

| 对象 | 字节数 | SHA256 |
|---|---:|---|
| 原数学artifact14178104533的ZIP | 216929678 | a6c23bc84d379f96f67233243d5a5fc3838f18cd913502088b4a08de455d4451 |
| 原full-outputs-manifest.json | 38367 | 7418100ba952913eeab8a60604d92ad4ad5ffdd49d3204602897641198ef77f0 |
| 原1380输入carrier | 189156436 | ad0c9493b6dc6f6ed99b37c58941000c638fcad683992e9b538a81a2123ed6e4 |
| 旧42来源carrier | 6594510 | 7d3ca58e7bb6103084d6fbf9783cbd417978a376b7d4627d19e9814511f4dd5f |
| 旧基与第三probe证书 | 2296339 | e8b173eb8fa265013e9966ffba4bdd5f75f6b63e19236dd4384ff84f3454ca56 |
| 新56输入格阶段 | 3426905 | f8cece1ec565cba15738e65ea01304d58edda1ba0cec44f7a1c24270b2a7c730 |
| LLL原始56行阶段 | 4527249 | bfe1b7e82811779e1c1969f40cfc1e292c27d6685393860ed560268f51dd526a |
| 完整56格与候选阶段 | 5918823 | 6cafcdaa430b9c5d01b233330414c30c398ee5e52fc489644085f69f5e6b6c25 |
| 新search-current | 7579 | 57cf83173d0f6bbb333024c38f5bec539979da2fd4847c2e3affc2cb26950b31 |
| 完整stage-manifest | 16710 | ef20938323a147b2a288a9d9214d07537fcb309b312b0397d008678f42d6c567 |
| 原false证书 | 15951 | 8fb5edad08b95c3d28fbb0c99fb0ae91cbbc990fdcc6db8b44013c6519d854c9 |
| 原core-receipt | 933 | fb61c07ccbee07ae3c0d81183e419e91fabf77090776054ce4275ccfcc5e40e2 |

小IO的完整132066B summary仅在artifact中，
SHA256为`d00f5345aa5b4a8a1b906512dd1d13e2a2cd62a526000739d2dfa56e6e03249e`。
小IO artifact14179245885的ZIP为21321676B，
SHA256为`5c7d0801a7b5e17a91a32487c1d3e6e22e5ff971bfdef6f8c7e7842e38958b66`。
此次Range实际传输21217276B/11请求；没有声称重哈希全部216929678B ZIP。
原数学artifact到期时间为2026-11-16 20:09:38UTC；
小IO artifact到期时间为2026-11-16 20:23:40UTC。
