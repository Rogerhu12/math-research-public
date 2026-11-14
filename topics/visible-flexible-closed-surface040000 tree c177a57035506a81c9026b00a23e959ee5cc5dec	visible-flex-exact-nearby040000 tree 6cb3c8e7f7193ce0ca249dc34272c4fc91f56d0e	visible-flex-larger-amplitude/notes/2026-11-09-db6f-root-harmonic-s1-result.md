# 全幅值逐模 warm 的实际单请求：失败记录

状态：数值失败证据，非无解定理。Astra-visible-flex-db6f0b0e / root，2026-11-09。

原薄入口v2在98项已核来源绑定下于14:37:16UTC真实启动，root工具会话28395于14:37:32UTC闭合，父进程测时16.028842021005403秒。root随后从工具最终返回直接观察exit2（receipt75bf61），与实际child exit2相同；原worker由finally close后poll得到exit0。正常worker关闭不等于数学成功。详细原命令、实际child和闭文件哈希保存在 root-harmonic-s1-launch.json 与 root-harmonic-s1-observed-execution.json。

唯一实际请求是固定目标goal、jacobian=True、audit=True。原八源、原36轮/2e−9/default floor .05、原边界修正保持；输入是由call9到s=1的逐模Q/Pi初猜。实际trace先记录warm_initial_state，再记录request，随后直接记录 Error: momentum Newton line search failed。没有iteration事件、iteration CP或trial记录。原失败response只含failed、lastIteration、checkpoint，后两项均null，原包SHA8205dcefb590623700d14dd111bbf0ef6f9cd6defb8e9802de2e12dbad090c8e；没有残差、jets、Jacobian、audit或可接续的新checkpoint。

因此只能断言该初猜在原请求形成首个迭代基点记录前失败；当前日志不能给出具体RK子点、初始归一残差或minA，也不能将失败提升为目标DN无解。本次不再把同一无结果guess当作continuation成功点。原continuation02独立保持运行，已真成功到s=.875并继续.90625。

根在闭合后重新核对98项输入绑定及6件闭输出哈希，全部一致。实际summary正确标记SINGLE_TARGET_NOT_ACCEPTED_PREFIX_UNSOLVED，原失败schema未改；入口因缺少成功schema而拒绝。此为真实负结果，README/G5与true prefix状态均未改变。
