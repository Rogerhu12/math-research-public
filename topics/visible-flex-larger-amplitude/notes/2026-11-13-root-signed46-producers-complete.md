# 原完整46模 signed geometry/source 已实际恢复

作者：/root（GPT-6 Astra Pro，AI辅助），2026-11-13。

本条记录两个**真实完成**的生产者，不把它们称为外侧非线性解、46-cut自映或课题完成。此前丢失的进程终态仍为unknown；本轮有独立的实际wait4退出记录。

## 不变对象与完整执行

两者仍用R88的同一个固定中心：真实线性m2、m4，原候选m6至m40；保留全部20个非零输入、完整mean及所有46个输出。原10793个材料叶和底层10933个旧Green子片是不同计数，未替换。

| 生产者 | 冻结入口SHA256 | 实际资源 | 完整输出SHA256 |
|---|---|---|---|
| signed geometry v3 | `98b5e8a0b06688830b7aee69df9f6a76f39f94d8b259a093d476bbf78abee642` | formal0；1047.294s；35416KiB | `7b785c177478d2b960172f85286005bcc6dbdcc2de5eb2cec56bffad6c998e5d` |
| complete source v3 | `3a19cb838f256cc9dd454267b5a32c2e280df927cc21820a2a8a867ad160eb59` | formal0；243.394s；38704KiB | `87a3464406e8f4193a3507d18fcf9a21c5c1d4ceb3e84aca784684af3c06af18` |

geometry保持256bit、24阶Taylor、160层根预算、100余项预算；18组全部完成，10870个Taylor片及8个根括片覆盖所有原材料叶，69次局部拒绝均被后续细化替代。真实signed两柱、Wronskian、F及各片锚全部原门通过。没有用有限Robin替换真实内头斜率。

source保持完整mean根与旧严格界相交，使用R107同中心二次均值包围及R108完整Wiener逆尾。四项Neumann求值中保留分子零模和c²，最后才取46个非零输出；完整未投影分子支付所有省略项。17个原门全部真。

实际10793行中，q=2和q=4的完整逆域全部通过；q=8通过9900行，q=16通过5102行。每行每模仅在该q确实通过时使用它；不合法者保留原σ=1/64严格尾。496478个模行的最终选择计数为：原σ29677，q2为169215，q4为294310，q8为3276，q16为0。没有将一个全局粗帽未通过解释为逐行必定失败，也没有使用任何失败的逐行域。

## 归档与重现

完整primary、原实际resource和全部554件生成文件的路径/长度/SHA256已存于`2026-11-13-root-signed46-producers-manifest.json`。两组生成目录共155670827B；依根README可再生大中间数据规则，不再向已很大的topic添加这150MB。保留冻结源、全部已入库科学输入、参数和生成文件hash；本轮本地原件仍在，供当前消费者直接读取。

实际resource保留完整argv。移到新工作区时，应保持topic为cwd和所有科学输入，选择fresh输出前缀、work-dir及input-root，用python-flint0.9.0实际重跑；随后把**新生成**primary的实际SHA和formal0 resource交给`root_outer_fixed_centre_low46_ordered_v2.py`。不能编辑旧primary中的绝对路径并冒称原hash，也不能伪造旧耗时或退出记录。生成的科学片内容可按manifest比对，含运行元数据的primary不承诺重跑逐字相同。

## 紧接的工作

两producer正式完成后，原ordered v2（SHA`b80ecd71be918161e0a862e4636822d5d5ac72993179c1a71600cd6a4fc354e6`）已真实开始两遍完整有序消费。它先保有符号累加，再付当前片部分积分，读P/K/C/U和完整LR−Z0；不能由本条提前推断该消费成功，更不能越过β、未知场误差、全46切口和中高频联合条件。
