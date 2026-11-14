# q105前缀首轮分解中断：正式退出与恢复点

工具session14476已正式exit137；wait4确认数值子进程被signal9结束。原因未知，
不能从wall或peak RSS断言OOM、时限、数学折点或不可解。wall=1388.4339752197266s，
user=162.535246s，system=4.636976s，peak RSS=608488KiB。

首个完整初始恢复点iterate-0001的x/y/p/三次系数5个分块全部重新核SHA通过；
2004节点、27参数，数值collocation_scaled_max=.03530332658931593，boundary=
6.225083349000171e−8。这是newton-entry而不是接受步；完整Jac/factor未返回，
没有后续Newton接受步，没有q105前缀终包，也没有新H尾请求。

首24H严格命中已实际完成fullJac+audit的92989c9b…包，未启动Node。该成功尾包
独立保留，不因前缀执行中断失效。下一轮使用独立disk-block入口压低同时常驻的
矩阵存储，并对真实factor每次solve做完整stream matvec后向核验；原方程、目标、
RMS、物理BC和全H真尾审计门均保留。未按旧内存路径盲目重跑。
