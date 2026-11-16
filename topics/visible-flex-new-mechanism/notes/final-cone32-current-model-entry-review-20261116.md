# 原唯一 cone32：完整实际返回记录与累计预算入口审读

日期：2026-11-16；会话 Astra-new-mechanism-9974ea84。root 已全文静态读本次设计、三个 Python、workflow 和 request，并阅读其直接调用的原恢复、budget、未来 checkpoint、序列化接口。**没有在本地执行新科学、人工、求解器、语法或开发检查；本文不是运行通过报告。** 具体来源合同见 [设计](final-cone32-after-paid-vector-values-design-20261116.md)。

## 1. 为什么此刻有一个未用槽

[最新实际](paid-MaxTime-vector-first-actual-and-new-soft-row-20261116.md) source `b8577eaaa8d8327495db13bd1f684348ede6cb06`，run43798128882/job133071559203，原方向三尺度全拒，最后新增 fine159001。原真实点52不变，池4448/4544、版本13/13；原31/32锥还剩一个尚未启动的槽。新入口没有重试原失败方向，也不对旧缺失rho/norm作恢复。

最新最终权威科学钟是773.3401341169999锥任务秒和1129.469954378原累计秒，真实值122=61粗+61细。原上限1200/1800秒、96/160值不变；可用交集426.65986588300007秒和36值。原HiGHS64封存。本入口最多一个新模型28、一次新cone32；必要粗细恢复、J、完整factory与真实trial全部计费。

## 2. 本次源码身份

| 对象 | 字节 | SHA256 |
|---|---:|---|
| final_cone32.py | 28899 | `14c79c042f6c820ddb1c18c11d636c5f659fe9219f86ae6125357076cc581b79` |
| final_cone32_recovery.py | 33925 | `c2b6076210b6830e0fa5ca41a1285911caf7c6f538c42b88bc330d3a0277c68e` |
| final_cone32_audit.py | 37176 | `209fd7bea540c8a9d055d8dd2cb249c4fedc73e17ed98d7bfaa104c53b40c720` |
| visible-final-cone32.yml | 4536 | `d2a6530cac260db3fc01ed8c7b7617229125b70712f816ae6706c61c50d82511` |
| request-final-cone32.json | 40422 | `39458fd2dff42510a5719491e2402ce37ef69663986eecf11896b10a21c2e332` |
| 设计 note | 10129 | `09cd273039a34c01d3f8f229b63c499bf33ca01c80c86280d2319250601ed5cf` |

request 的189项绑定=170 Python+12 workflows+5人读MD+2来源JSON。root把原182项逐项与已发表request比较：无改动，原98个参数相同。七个新增或桥接绑定均以实际文本SHA核同。实际runner在当前源上再次按这份闭包读取，这属于真实入口身份检查，不重执行旧科学。

## 3. 真实恢复对象与未更换的方法

最新纯值objective `d6008a66…6e336`仍作为来源身份保留。constructor显式恢复checkpoint同时携带的真实原仿射definition `e101bd90…26b6`，逐字段检查实际基类和原finite-cone method。没有把纯值对象的旧SHA改标签，亦没有把原模型27的池/J绑定用于新模型。

原field/factorizer、g/b0、163参考、159→163精确映射、98参数、原cfg64/160/1800/10.0均保持。完整bank512及8独立补充法向、62events/61commits/pending0、gamma、全部两池IDs/历史与13/13版本按实际checkpoint恢复，constructor不调用旧learn或commit。fine159001留在当前selected软行。

root特别读了继承的 `bind_restored_current_cache`：真正新两网必须原全部门通过，物理SHA等于点52，两个实际标量只按原容差对比；随后同一进程cache才供J和完整factory。没有额外独立final几何。必要冷参考原函数会重新计算并完整付费，不声称跨进程缓存存在。

原value-only COMPLETE未导出六新值之后的mutable组件计时，故旧组件计时收据与六条真实wrapper调用、adapter99.716150581秒分别保存。本attempt的组件timer从0且明确标作用域；122值及两个真正科学钟完整继承，不将不同口径组件冒作精确累计。

## 4. 预算和资格路径

`ContinuedCone32Clock`在读取request、源码身份与唯一来源log之前启动；两起点分别回移上述终值。ledger以source31、当前空event表和原成本收据恢复，只允许原charge在backend constructor之前把31变32；第二次charge无入口。prepare/constructor/_wall/value/J/factory/oracle/solver/trial都受原相交时钟和计数约束。冷调用与backend不能抢占，真实超出仍收费，后置检查退出。

root对新旧recovery做源码文本差异：assess、实际学习、严格两网下降、原回溯与controller保持；只把源点27/旧池改为52/13,13，模型编号从28开始，调用新的完整记录包装。原四锥内循环仍有其数学代码，但全局剩余只准一次。本入口没有SOC、第二solver、旧方向重试或新covered资格。

原Clarabel0.11.1、200迭代、单线程和三项1e−9不变。Solved/AlmostSolved才可进入原候选修复；完整线性/box、half-cone原单位残差、全网rho上调和下降floor均保留。MaxTime的有限向量仅被保存，不能据此升级为原合格候选。

## 5. 真实161在任何筛选之前保存

新的 `solution.x`一旦shape161且全有限，先保存全部161个原二进制有理坐标、原scale159、实际乘法p159、两个数组SHA、原rho/norm及当前模型binding。随后才读取后端status/timing、记录原单位linear/bound和cone残差，并走任何资格过滤。

既有 `cone_call_semantic`仅压缩原cone tags/row source和支持收据，root确认它保留新增完整向量字段。即使outer附加报告或末次保存发生异常，audit仍从同一个ledger把本attempt全部event独立写入 `all_current_cone_events`。记录旗从真正161/159列表与rho/norm对应项计算；没有有限返回时为null，不冒作保存成功。

真实trial同样保159独立和163物理精确向量。若末点仍52，14门引用原已付真实收据；只有真正新trial接受到53且index/物理SHA对应，才引用该trial新两网门。较早future checkpoint时间不代最终COMPLETE科学钟。

## 6. 唯一实际入口和读回

本次workflow只因新request的main推送触发。先实际partial checkout/pull --rebase，核公开根/题README差异和私有规则/QUEUE，再detached回本次源SHA；若规则变或pull失败，不启动研究，先读差异执行。随后按189项闭包执行一次audit。

原日志只读run43798128882/job133071559203一次，严格核3765299B/SHA917036…a42f51和四个原tag；更早12/11/9与本来源6检查都是已付证据，不重新下载祖先日志或运行它们。**新developer=0、旧checks=0、tinycone=0。**

输出标签为 `FINAL_CONE32_PUBLIC_PULL/PRIVATE_PULL/REQUEST/PRIOR_WORK_REUSED/MODEL/COMPLETE`。完整数组和checkpoint只留runner临时文件、原stdout，不进入Git/artifact/Release/cache。后续只依据真实原stdout报告新调用、残差、验收、池和所有成本；未开始项不写通过，失败不重置预算，不增加第33次调用。一个子题结束后继续新的实际未付问题，主任务的同g、精度、全时reach、嵌入和幅度门仍不放宽。
