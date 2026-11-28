# q=.012/λ=.004 后继：每个原 Newton 接受步完整保存与真实限制观察

此前完整节点只在新 J 之前保存；实际中断发生在同一 factor 的第6次 solve 之后，没有付到新 J，故未保存这些 chord 步。独立后继在原 `accepted` tuple 赋值和原 STATS/refresh 更新之后只添加一次完整 x/Y/p/pscale 的文件保存，不重新求 RHS/J，不改原浮点语句、line search、mesh或任何验收门。每个完整节点文件不变，latest 指针原子替换；即便写新节点时终止，旧完整指针仍可用。所有这些节点仍明确为未获整个 BVP/RMS/metric/physical BC 接受的初猜。

执行前严格对照实际安装的原 released Newton 编译代码，若不一致便工程拒绝。真实原函数文件与原释放版本源码/编译结构合同已读核，四个新源的 py_compile 和新入口 --help 均返回0；没有新增 BVP/J测试。运行期间仅对已执行的真实原 Newton 节点保存。旧冻结入口不改。

新的 observer 保存自有实际数值进程的 PID/startticks/SID、cgroup成员关系、实际 cgroup mounts、memory.max/high/current/peak/events等文件的可读状态与数值差、/proc/PID/limits，以及 join 后的真实 kernel rusage。不可读不等于无限；计数变化也不会直接归因为本进程 OOM。当前此执行环境 cgroup文本为0::/，无可见cgroup挂载、惯常路径缺失，不能凭主机MemAvailable断言容器限额。未更改限制/挂载/namespace。

后继保持真实 `0fdf914d…` 615×73 nodal initializer与同一 λ=.004 原定义，只将原径向 RHS/Jac 批量32改为16以降低实际瞬时数组尺寸；所有节点和所有原列仍计算。旧完整 CSR/QR/非线性重叠调度门及512MiB外部余量不降低。当前只是准备，等待已接力的原generic8outer大J窗口完成，绝不同时新开。下一实际返回才可判断接受或失败。
