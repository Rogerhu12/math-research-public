# 新atlas里的明确coast校正重置

状态：真实新初值，不是同场重表达或求解成功。

输入是atlas12四个真0批后的第8accepted；参数、物理g、全函数lifting与atlas保持。
独立producer只把节点correction改为(1−w)倍，w=0处逐位保全，w=1节点校正为0。
新格内函数是新节点系数的P1插值，不是旧P1乘窗；完整metadata和投影改变均明确。
这不是原plain-bump初始化，旧源码的double-init保护没有被绕过。

实际71923/bb6d23真exit0。新完整Gauss节点峰从1.749917984降至.919689690，
形式κ7.202043895不变，但raw升29.70316725、fullendpointCod58.73237201、
high3.45538279；这符合旧校正与known-lifting在rim处部分相消的真实诊断。
没有把初值的一项改善冒为全部指标改善。平台native仍只有baseδ0准确GC，
对当前不变δ的目标缺陷全部进入新F。

新的atlas13从该实体直接使用同endpoint/8cell/D2/v3完整联合驱动；其活动数据另存。
源/入参/新warm/完整报告与真实退出见本组manifest。
