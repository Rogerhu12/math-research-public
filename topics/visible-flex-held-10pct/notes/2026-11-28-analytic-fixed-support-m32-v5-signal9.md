# 固定 g 的 M32 v5：真实 signal 9 终态，完整更新 nodal 已保留

v5 的父会话 session85064 实际 exit 247；它的唯一 Python 子进程实际 returncode=-9，即 signal 9，运行 638.239257594 秒。`RUSAGE_CHILDREN` 报峰 1450012 KiB。没有证据把这次终止归给某个 OOM 事件或原数学分支失败；本条只登记观察到的进程终态。

日志命名问题已在真实全维路径消除。v5 实际完成两次 1497 节点、97 状态、32 参数的原完整 CSR / QR：每个完整系统 145241 维、32824466 个 stored entries；两因子共六次线性 solve，已观测原 J residual 最大值为 1.8471670997248155e-18。最后一次为第二因子的首次 solve，原残差 max=1.0981782161152004e-18、相对 l2=6.231947870586015e-11。之后进程被 signal 9 终止，未有外层 RMS 行、原 raw_return、physical 返回或 metric audit。不能因线性方向返回而晋级 BVP。

最新**实际保存**的完整 nodal 文件 SHA 为 `dedd80ae45e10bfecb02a4369f51f9751c2ed2e41c3f140f66cdbad3f5b65544`，仍为 1497 x、97×1497 y、32 p、31 pscale；这是第二次完整 J 前保存的已更新状态，不再是最初1497初猜。p0=7.089383593385811e-6，对应 q_actual=.06000042536452339。它不是完整 solver 返回，也未必包含被终止前所有尚未保存的试探更新。后继只能从此真保存状态继续，不重播旧初猜。

原 v5 源保持 SHA `213ed5dffdb3925cdae43c22c0d1ac1fe6496f7c42a92ce254ddc99952ae85d7`。原 run.json 仍诚实保留运行中状态；外部不可变 `actual-process-terminal.json` 记录真实终止，不回写/冒充原 solver 终态。运行记录、完整 nodal/manifest、父终态和控制台 SHA 均见同名 JSON。

下一步只读核资源生命周期：fixed=True 的 flow(p0) 总是同一个固定 Flow，且原解析 control Jacobian 不运行设计分支的 delta± Flow 重建；不能直接搬用另一个 design 链的垃圾环原因。原 rhs-block64、jac-batch32 与短调用/异常路径的 GC 边界仍将独立核对。新的资源实现和恢复入口须独立命名，原模型、mean1168、全部原门不变；此记录不含新恢复执行或接受结论。
