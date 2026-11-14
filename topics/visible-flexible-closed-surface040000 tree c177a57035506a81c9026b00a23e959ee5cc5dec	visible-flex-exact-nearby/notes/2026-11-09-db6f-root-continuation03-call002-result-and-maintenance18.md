# continuation03 第二点失败及空间维护18的闭合记录

## 原有限DN的实际失败

call2 的 s=127/128 在原36轮上限、tol2e−9、floor.05下返回 multiple-shooting line search failed，最后基点 iteration5/norm2.604516507642326/minA.07763554415662655/minD.9915670399254011。响应 eb7518a7955764f7563f365b9e1b08ea1e9346148c12b66a007650e9cca47460 真实存在；这次不是ENOSPC中断。失败checkpoint只作诊断，未冒称收敛warm。

root闭合请求检查实际 exit0/a8f124，重核83入口、8响应源、原方程配置、精确幅度路径及865×30有限状态。控制器保留call1=63/64，按原规则将步长减为1/256，继续call3=253/256；父工具session3046未退出，不从文件推断完成。

闭trials文件是累计日志：7行属于call1，22行属于call2，不能将全文件29行都算成call2。call2共有5 accepted、5 residual-not-decreasing、10 momentum-root-solver-rejection、2 momentum-guard-rejection；最后iteration5的10次试步为2 guard、6 momentum-root、2可评估但不下降。末两点lambda=1/256与1/512的norm为2.760465083646105和2.6401266603560583。它们不证明更小步长会下降，也不证明目标无解；更小步长只读诊断接口另行准备，未改当前算法。

原响应、两个旋转闭日志和其中所有call2的失败stage输入均按原SHA封存；active03 progress/trace/iteration不在本发布中。

## 空间维护18

先有未参与数学优化者的fresh预检：单个d445大promisor包只有27个同分区独有OID，P/O无交集。root完整阅读预检和最终脚本静态审查后，真实执行已审脚本1f82bf03…；工具9271a5/session84439后以f368cf实际exit0关闭。新自包含rescue54c960…恰27OID/414447B；包含全部包的新MIDX逐owner/offset验证后，唯一零owner为d445，标准expire只删该包。

root实际记录300bb676…和独立root工具观察c3e96e17…分别封存。独立后验实际exit0/18b7ad，使用不变保留idx加预先冻结目标/loose列表重构原集合，与现状逐元素相同：indexed120121/allpresent120763/P118413/O1708；22个保留原pack的mtime_ns/inode/bytes、refs/loose/idx均同。当前23包合5290124822B，净减664937148B。没有跨分区重打包、对象丢失、数学输入或活动控制器改动；独立后验不冒称另行观察过去的删除前状态。

root已全文阅读正式静审/后验说明及闭清单，再次逐文件核哈希。本维护只保留原对象，不能作为数学收敛证据。
