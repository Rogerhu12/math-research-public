# R815：两准确列的真实分母、49个早拒绝与剩余边界

本篇登记真实公开 run43755027718 的结束产物，
不把请求预算当作执行数量，也不把有限早拒绝当作原Mg不存在的证书。
原Mg与Gamma仍未恢复；原425-prime同核续算继续进行。

## 1. 固定原源与实际完成

数学运行
[43755027718](https://github.com/Rogerhu12/math-research-public/actions/runs/43755027718)
的job为132937184138，source为
`e1d8a95631eb11d1df0ccba4a781b05b6dd45c62`。
core为
`0008796890a0cfcf0b9aaaa40e26f0d8d26be38f8168c8fe918d86a7585a0ec1`，
修正后的runner为
`58d65088e16469651d9895b5fa3e8f93bd0f9c8db309852d1bf6d68b753bf8cd`。
它于2026-11-15 20:01:59UTC结束，exit2、error=null，
实际核心时间20.024274770000034秒。

此前run43754577366的旧META读取顺序错误发生在核心启动之前，
没有产生新数学阶段；本次只修该IO后使用同一个数学核心。
原425-prime、12707bit current、3037源闭包和原标量规范没有改变。

小IO
[43757804827](https://github.com/Rogerhu12/math-research-public/actions/runs/43757804827)
的review job为132945729049，source为
`159a739622e264ea8dd1f0a400c0cb7ab0fd40d5`，
reader为
`59140e7fbf44476504615a80bf756d3ee2f866080865566c9cba469dfe7ed863`。
它按真实manifest逐字核所选小阶段，只读已有准确乘法、扫描及拒绝结果；
不重算Wvg、gcd、LLL、RR或交换子。
两个carrier及旧561995095B current未重新下载。

## 2. 两个准确列实际得到的内容

[两列方法](R815-original-two-known-columns-reconstruction-method.md)
从原We0=e1和Mg e0=vg给Mg e1=Wvg。
本次真实计算得到原第0、1列，
分别有690和962个非零整数分子；每列用5×272个槽保完整支撑。
全部1652项原current同余、两列加权界以及其余高项为零均由原核心核过。

| 已保存量 | 实际二进制位数 | 实际十进制位数 |
|---|---:|---:|
| 原g首列约分分母dg | 2738 | 825 |
| 原W共同正分母dw | 6381 | 1921 |
| 初始乘积分母dw·dg | 9119 | 2745 |
| 去掉的联合整数content | 2634 | 793 |
| 两列共同正分母d01 | 6485 | 1953 |

d01的十进制整数文本SHA256为
`3b79d6474bdeab3e2c9e49f3a5f75d423bccb8e91cd4dba3fdb5840d0c32cb85`。
第0、1列分子的最大位数分别为6476和6477。
大整数与完整两列数组仅在一日artifact中。

d01是这两列的准确最小共同正分母，
因此原完整Mg的共同分母必须是它的倍数。
它本身尚不是完整Mg的分母证书。
候选使用这两列的准确不受中心区间限制的提升，
其余列仍来自原current的同余类。

此时交换子的第0列是构造恒等式：
Mg We0−W Mg e0=Mg e1−Wvg=0。
因此消费者按已证方法改查第1、2列，不把该恒零列作为新的通过证据。

## 3. 实际扫描、格与失败

旧扫描前缀停在21，已完成的标量RR不重做。
旧失败索引7属于现已准确知道的第1列，不再当作未知probe；
原其余失败索引10、11、12、13、15、17、20继续作为真实未定项来源。
旧候选拒绝与旧first-nonzero位置不沿用。

本次四对probe实际为
(10,11)、(12,13)、(15,17)、(20,24)。
末态next_coefficient_index=25、unpaired_failure=null、
completed_pair_count=4、scalar_RR_failure_count=8、scan_finished=false。
新的first_nonzero_nonfirst_column_positions为9和10，
对应原尚未知的第2列；不是旧第1列的位置4和5。

实际完成28个三维LLL阶段，共84行。
其中8行的D为零。
全部原始D文本有50个不同值，非零可接受D有49个不同值；
重复行不能重复计为新候选。
加入d01基准并按实际D去重后，实际候选定义仍为49个，
其中一个以actual_two_known_columns_denominator记录。
它们各只有一次早期准确检查：

$$
z=0,\qquad \text{output row}=0,\qquad \text{input column}=1.
$$

全部49次残差非零，并各有准确拒绝回执。
基准d01候选也在这个位置失败。
它的残差文本为19085bits、5745digits，
SHA256为`6dc9e4dec5cd895e57a140af1e561b5642893d2fe5a6f48b0cd07fea43d21145`；
这里只登记身份，不提交原整数。

所有候选都在早期出口结束。
complete_candidate_index_stage_names与
complete_exact_commutator_stage_names均为空。
没有完成完整272×272矩阵索引、原7点全交换子或Gamma。

实际停止原因是probe_pair_limit_reached=true，
candidate_search_exhausted=false，
all_original_coordinate_positions_scanned=false。
本次四对已完成，其余扫描尚未完成；不能说整个搜索空间已尽。

## 4. 结论与后继所保的工作

本次准确两列是新增可复用输入；
49个具体中心提升矩阵的失败不能否定原乘法算子。
也不能仅凭失败断言425个素数不足。

后继保留两列完整阶段、原425 current、next25扫描与全部28格/49个拒绝。
不重新乘Wvg，不重旧RR前缀，不重旧三维格，
不把改变了已知列的候选套用旧拒绝。
进一步的准确列须从原基的真实乘法关系推出并单独核同余/支撑；
不能把We0=e1擅自推广为所有Wej=e(j+1)。

原成功出口仍要求完整加权支撑、原六个模点与七个准确点的Mg交换子、
cyclic唯一性、原Gamma嵌套交换子及两张regular chart。
两列或单点成功不能降低这些要求。

## 5. 最小来源登记

原数学artifact14178355802的ZIP为2721387228B，
SHA256
`03c3c5925b949e4f8dcc89260fb807dace1649088c0bfb122910dba3275f90c8`，
到期2026-11-16 20:02:00UTC。
原ZIP有196个文件，manifest含194项。

| 必要阶段 | 字节数 | SHA256 |
|---|---:|---|
| full-outputs-manifest.json | 54863 | cdf06cf303d181f662cd9d57243df2d4cf785b0b0b4b5b1e85c1816e55d16e08 |
| 两准确列完整输入 | 1608842 | 8907fb65e6724d09ba21cca87b649c45631dc0e0f1c1d477f147447be4f4073c |
| 导入旧扫描证据 | 3507 | 068f3559359309210a4552ad921cc7a098dcb7ba05e8ad3415265ab5c1214b85 |
| 新probe-scan-current | 3463 | 3782cd81bae0a5a80e260b80ec8cde0539ee5af97619a8b19652fb5b130fb39d |
| 新stage-manifest | 14340 | b95a82f91557f6d817118f6c87c4b271455deb458ee87514c74c61cc6c79bbf5 |
| 原3037输入carrier | 2715514274 | 4c9a6d1e3c2c462efecabeba826697efbbc04a3357db1a74d8bd06027804a1b5 |
| 旧scan小carrier | 69819 | 2670b608d515c5e2be135f5254640f58c7ce6136926925b593d0722245f3f4d2 |
| false证书 | 16253 | e789cf88cd6aa4f2454c003c1d5699476c4ff91c283f092d8410cc7fa54125c5 |
| core-receipt | 995 | 895ad29be9d386d83c41712eb1798980413b8c5479ea0918f3fb9cfb020814a3 |

小IO完整summary为247794B，
SHA256 `e0379a3f0559b861cb423d7cd7b14b69936f7e010fdb8a8b40af1cacc64b9e4c`，
只在小IO artifact14178648672内。
该ZIP为6088672B，
SHA256 `dce88b740b464ebbf0ce61ed3d5f95064bd79c95b73083d477fb2b2350b0eca4`，
到期2026-11-16 20:23:57UTC。
本次Range实际传输5928242B/11请求；没有重哈希全部2.7GB ZIP的声明。
