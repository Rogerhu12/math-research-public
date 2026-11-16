# true53 已付正有限方向：完整双网 first jet、原标量线与实际门

日期：2026-11-16。本文定义一个新研究任务，消费已经完成的一个正有限方向，继续原完整双网与实际几何。有限 LP、旧 hard J、源点普通 geometry 以及旧开发/检查均不重新执行。源点仍为实际接受53；有限增益本身不授完整网格下降或实际接受。

## 1. 两个闭合来源

完整原 MODEL 来自 run43811870681/research133115100791、source42f95905deec3024dfee7a687bdc806d38c79baf。该次 Hildreth 观察及其23次分离已经闭合；后来的任务直接读取原5743软梯度、2937 hard行、五条补梯度、163物理盒、652 norm/physical行、320外界行、原完整e/f与所有绑定。

原 MODEL JSON+LF 为27365833字节，SHA256 926681688d09311883c64dfa1dc40599a62d1904d7f6dbcaf478893fe14bd539；其余三个必要原记录及整日志指纹由请求明确绑定。MODEL binding 为 e095e93d1455302af6904e703e762adad05d9cdef7220761c468e3ea0efca9a1。

新有限主问题来自 run43817336585/job133132261671、source de1c7d5a2dfa7b82d63c8e98f460eea269dbdeca；1LP、34迭代、68个 Newton 系统完成。9658原行通过，修复 finite gain 为7.0414711481267545e−6、h为.25000001109908276。原159方向 SHA256：
3fade7f704238c45a9eca095af36035ab10c4741e059d000359cc9d0600f5e09。

完整 finite COMPLETE 为185626字节，SHA256 489ecc703840abc6e1c360b10478dbe6ab480002d15f667054b40d912263ff63；FINAL_CLOCK 为132797字节，SHA256 d6e46f0342664aa8021424114912242bbcc54e7374169c8aeb5635932180b7f8。原日志1559099字节，SHA256 f597ac00baf733e0de6f0d88647b0c162a37cc9e33e428bd6371a93032e7c087。

该有限任务含BOM失败后的总科学14.132776896000024秒；祖先完整累计1608.573003992秒、128普通几何值。新任务从这个闭合事实继续，不另加一次旧1594.440227096秒，也不重置任何旧solver余额。

## 2. 原始数学对象不变

同一固定 g 与 b0、永久 enriched reference、159→163坐标、物理上下界、全部14实际门、原两网格、pool4448/4549及版本13/14均保留。完整状态物理SHA为9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e。

保原 norm penalty μ=1e−6、metric proposal ε=1e−8、固定目标.26、B=.00025、hard原单位容差1e−7及原实际下降阈值1e−7。已付原 bank/guard学习/全部补normal/原半径与controller状态只随checkpoint保存，不自动重训或扩张预算。

真正输出原159方向 p 后，先形成原binary64候选 state+p，再用实际差 (state+p)−state 作第一次完整扫描。此处没有同时扫描一个理想p来重复付导数。所有缩放实际点仍再次通过 exact163盒与原hard/guard/norm域；没有用线性预测替代普通geometry。

## 3. 仅恢复新 JVP 所必需而原 MODEL 未保存的输入

原24输入恢复的是同一个field、坐标、g/b0、grid与gate。该恢复不调用旧普通geometry、旧hard J或有限主问题入口。

原 MODEL 已保存 e/f，直接使用。新 first-jet 接口恢复 U=X_s 与 T，使用原scalar field、target frame与周期primitive：
U=a_s P_{−1}T+a P_{−1}T_s+(0,0,b)；
原五个null height方向仍按原支持范围加入。

这属于未保存输入的必要恢复，其实际耗时从新任务开始就计入。没有把它称为免费操作；也没有运行完整普通位置/曲率/二阶geometry来再次验收源53。

细网角度保持原表达式 arange(2*Ncoarse)*pi/Ncoarse，不重排浮点乘除顺序。两网为160×384和160×768，完整点数61440/122880。

对实际159方向，仅使用原方向frame导数，得到dU、dT，再形成de=2U·dU、df=T·dU+U·dT。每网两条原metric分支的完整一阶值为
phi(e,f)+phi_e de+phi_f df；
这一步不以phi(e+de,f+df)冒一阶模型，也不生成全网159参数轴张量。

固定目标常数支始终在最大值内。完整一阶增益扣同一个真实物理norm penalty。只有正增益且原域合格才进入原标量阶段。若不合格，最多提取四个真正新全网argmax的原159梯度，保留输入供后继包含新cut的有限问题；不重开旧23次分离或旧LP。

## 4. 标量线及真实实际门

标量线完全复用本次已生成的 e/f/de/df。保真实alpha=0的基线、由原hard目标与精确物理盒推得的合法区间；若合法下端为正，也不能把它当作新的零基线。

搜索最多62次完整四分支查询，另外最多两次为实际fallback准备，共64次。整个区间优化只给离散完整affine光谱的观察结果，不宣连续网格证书或精确最优性。

实际阶段最多三条不同物理候选：所选alpha，以及两次朝同一合法下端的中点。每条先按原159→163检查真实舍入后的所有域条件，再付原coarse geometry/14门，合法时付fine geometry/14门，并以原双网至少1e−7下降判接受。源53的普通geometry请求在新objective中直接拒绝；已有接受记录不重放。

拒绝实际候选如产生原value-only pool新行，保存新行后停止这个固定方向，不在发生改变的pool上继续假装原模型不变。最多新增一个接受点54。所有开始后失败的实际geometry也照原计数收费。

## 5. 一个新科学账户与完整可续输入

同一600秒钟在数值库导入之前开始，包含两个原stdout读取、24输入恢复、U/T输入、新JVP、必要新梯度、scalar、实际值、所有失败、最终大输出及主报告写入。

| 项目 | 本任务上限 |
|---|---:|
| 必要 first-jet 输入恢复 | 1 |
| 不同新方向的完整双网 JVP | 2（本入口先只用实际舍入方向1次） |
| 真正新argmax梯度 | 4 |
| 标量session / 完整查询 | 1 / 64 |
| 不同实际候选 / 普通网格值 | 3 / 6 |
| 源53普通geometry / 新hard J / 新finite LP | 0 / 0 / 0 |
| 旧或新独立开发检查 | 0 |

原完整大数组不写Git、artifact、Release或跨run cache。新U/T与已完成de/df在一个原普通stdout CACHE中保留；进入scalar时包含其完整line_cache，去掉同一de/df的重复副本。只存后继真正必要的数组，不重复旧MODEL或全部可重建frame/two-jet中间张量。

若接受54，再从原已付accepted_cache直接取新点的Xs、T、e/f、radial/theta，另一个CACHE保留；不调用geometry/JVP，不以Xt/a另算T。未来checkpoint记录这两类cache的原stdout身份；旧源点数据不能冒充54的模型。

整次数学stdout的首跑上限为78MiB，读报告原log上限80MiB，留runner文本余量。原日志以一次普通记录传送各缓存，不分块、编码或经Git转存。所有序列化时间计同600秒，FINAL_CLOCK在大输出与COMPLETE写入/flush之后采样，且对后续费用权威。

report job只读原日志和既有数值，输出紧凑语义、原literal记录字节/hash与不展开的checkpoint/cache身份；无科学库、无重新求值。报告成功不等于科学成功。

## 6. 源码、规则与完成边界

本任务源码分scope、paid domain、必要first jets、原line adapter、原actual adapter、两源transfer、accepted cache提取、audit和read-only report；全部源码SHA与原依赖清单在同一小请求中。

公开workflow在research与report前分别真实pull公开/私有规则，输出根/题README差异并要求按已读规则；私有令牌在科学或报告进程前移出环境。仅用公开仓库自己的Actions执行。原有唯一QUEUE进行中状态维持，不把本次单个数值任务称为主课题完成。

本任务无论得到新cut、实际下降或有限失败，都会把原费用和完整状态保存为可接续的原stdout身份，并继续open。主几何的C²全族、固定g精化、非局部reach与振幅门仍以题README的原完成标准为准。
