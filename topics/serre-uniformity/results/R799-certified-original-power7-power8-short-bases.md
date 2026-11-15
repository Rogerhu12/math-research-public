# R799：原七、八次准确短基与六次缺尾已完成

日期：2026-11-15。状态：**公开准确计算已完成。只登记原短基、新minor及六次必要尾；原函数关系、极除子、β、η和高度仍未完成。**

依据 [原最小基与锚点证明](R799-original-power7-power8-minimal-basis-construction.md)、[执行方法](../notes/R799-power7-power8-minimal-bases-method.md) 和 [R795 原六次短基](R795-certified-original-power6-short-basis.md)。

## 1. 实际计算与新minor

[公开 run43695571499](https://github.com/Rogerhu12/math-research-public/actions/runs/43695571499)成功。核心证书记用时 **555.8178967150001秒**，外层完成于2026-11-15 08:49:48.186094 UTC，退出0。

| 原空间 | 实际准确行数 | 本次系数范围 | 实际新minor |
|---|---:|---|---|
| 普通六次 $V_6$ | 1506 | 只补$q_Y^{82},\ldots,q_Y^{108}$ | 保原基，不重新选六次基 |
| 普通七次 $V_7$ | 1778 | $q_Y^0,\ldots,q_Y^{95}$ | 1778阶，det=534 mod739 |
| 普通八次 $V_8$ | 2050 | $q_Y^0,\ldots,q_Y^{108}$ | 2050阶，det=148 mod739 |

实际使用原三个锚点索引 **[0,1,73]**。七、八次最终索引的candidate_cursor分别为4518、9036，辅助素数均为739，bad_prime_states为空。没有据此登记两锚点无基点或其共同零次数；two_anchor_basepoint_free_certified_by_actual_minor均为false。

每个minor的全部元素取自保存的准确整数行，按完整20个原实坐标选行；保存的各列与选基时的模列全部相同。行列式非零证明特征零独立，结合下述已证维数才给完整基。

## 2. 原空间与准确规范

原$g=127$、$\deg\mathcal L=272$，故
$$
\dim H^0(7\mathcal L)=1778,\qquad
\dim H^0(8\mathcal L)=2050.
$$
原二十cusp同轨道给短界
$$
20\cdot96>272\cdot7,\qquad20\cdot109>272\cdot8.
$$
因此本次完整短展开在各原空间上单射。原R799已证明三锚点无基点，保证所扫描的原乘积张成；本次真实非零minor进一步认证实际选出的基。

原整数尺度分别为：
- $V_6$：$82^{12}=92420056270299898187776$；
- $V_7$：$82^{14}=621432458361496515414605824$；
- $V_8$：$82^{16}=4178511850022702569647809560576$。

每行同时保存完整40个$q_Y,\xi$坐标与20个$v,t$坐标；原$q_Y=\xi^{10}v$的相位逐项核实，反演固定性准确成立。六次新尾全部与原R775 mod739值比较通过。旧六次0–81、旧E1/M2/低幂、Hom、period或Laurent没有重算。

七次候选为原锚点乘原六次行；八次为两个原锚点直接乘原六次行。八次三因子用其实际足够stride，未偷偷生成七次95之后的系数。原recipe、整尺度及所有准确坐标随最终索引保留。

## 3. 来源与参数

| 项目 | 完整绑定 |
|---|---|
| 原source | 2ebb10bc2cca7000374f83fa855030723deca2f4 |
| 核心 scripts/R799_original_power7_power8_short_bases.py | 32ff9d381d6482e1fd623b6cc54efb26dcf7604767b1109f022e3b96d6cde054 |
| wrapper scripts/R799_public_original_power7_power8_short_bases.py | f74313ac65b2b34cc8079e3506e97c8ca60211a2cf92fcd64df01bc49f6211a4 |
| 原证明SHA | ca6abba83ba9bb0c843f3ef37b6fe3f703c380bc7e0be3339c05df9a7b7a54b4 |
| 方法SHA | d1e489cdf8dfeb2b7fc2607e10831b599b6dcd8b20330e554b9e8203020133f9 |
| 实际请求SHA | 5b726dc8d7f5e2b81141d1246a110eeb97341804b50f16b1cf90fb02636572f1 |
| workflow SHA | 78386c03135c5a464a11f71b3c7653812cc3a9e894945623cbdb7bd11b3b8e8e |

实际请求为notes/R799-public-power7-power8-short-bases-request.json，workflow为.github/workflows/serre-p41-original-power7-power8-short-bases.yml。参数固定新六次区间[82,109)、新短界95/108、维数1778/2050、锚点[0,1,73]、辅助素数起点739及64列选基批次。300分钟只是单次预算。

原三组输入为R775/run43679160495、R786/run43682100611、R795/run43692029484，真实消费文件数分别6、1244、1513；原输入由R795及其准确绑定的当前父bundle提供。完整producer/configuration/每项SHA均核过，没有把历史partial R775的整个producer身份冒作完成producer。

## 4. 输出及独立IO读取

| 输出 | 字节数 | SHA-256 |
|---|---:|---|
| p41-original-power7-power8-short-bases-certificate.json | 39586 | 5a6c7fbebbaee90cd17c40828556b2e27a53c83d3f18aa28a5f54cca02524b9b |
| R799-original-power6-tail-index.json.gz | 82103 | 1fcb5cb98c4a18bc02bbb2441a606eed1c7bba1fd7610e6ca6857e4fbfc22c6f |
| R799-original-power7-basis-index.json.gz | 121629 | b7889ae6e3ccf8607ce40215d68ca65f0075ac2f8638284690d8a4108e244847 |
| R799-original-power8-basis-index.json.gz | 140608 | bc202037fb41aaa3138432c387ed8a69ae3f324cc6fc87c0fc5f50894155d2fd |
| R799-exact-stages-manifest.json.gz | 265237 | b9cec9358d9adcf31f318dbe82853153e7f4ff318eed19853b8fb0187c4a280b |
| full-outputs-manifest.json | 1595203 | 41640ebc6bc567c52b5f6ee840f59776769c7ba851ff24e405a7150267168933 |
| R799-retained-producer-inputs.tar.gz | 126475998 | 85245eeffd6d0e0a47cf64bb2bcef14647c902ef2f4b0e24e33bf6d69cbad38d |

完整manifest共**5347个输出文件**，stage manifest共**5339项**。完整原artifact **14153724209**，名serre-global-R799-original-power7-power8-short-bases-43695571499-1；ZIP **453521743字节**，SHA-256 **b4a3f74d9139475af07c1a654e8a3febc38c5186a1bfded4e0e038742737a477**，保留至2026-11-16 08:49:49 UTC。

[公开纯IO run43699442183](https://github.com/Rogerhu12/math-research-public/actions/runs/43699442183)，source d9c4795a140a6815253f079eaf7936ac096a92ad，核完整ZIP、全部输出字节数/SHA、原source/request/core/wrapper，并执行原wrapper的verify(item,out)。09:29:18 UTC返回0，未导入或执行数学核心。其11540字节摘要SHA为fb70ab1bd00a3648c8d882df19666020fcfc92c66d5822403eee1bf2a4ea30f6，留在一日artifact14156101148。

## 5. 准确接续

[R801](R801-original-minimal-long-tails-and-exact-relation-interface.md)只能延伸这次最终选中的1778/2050条原recipe，不把候选缓存误当基。新六次只缺109–141，七次只缺96–175，八次只缺109–195；其他后继需求独立按已证明范围添加。七/八次可扁平为少数锚点乘子乘原V5，避免生成无用的整套V6高尾。

本次只提供短基和新尾，不提供原A/B、完整极除子、Jacobianη或高度。所有可重算行、完整证书和输入包仅通过当前一日artifact/bundle传递，Git/Release只保脚本、参数、run/source与输出SHA。
