# 有符号窗口的完整有限消费者与真实局部检查

状态：R182 给数学表示及真实正曲率域；本说明记录另名程序与一次真实有限比较，不声称新 F 已改善或全域几何已经通过。

`fd2d_gc_signed_trace_problem.py` 以不可变原 archive 明确恢复相同物理/离散结构，再创建新 representation。新 archive 由新类检查自己的 schema、原身份和完整窗口定义，从不伪装成旧 R155 archive。原尾域 R170、54 参数、131 网格、固定 atlas/coast/尾函数及物理 $g$ 均保持。新增两窗为中段正号 $[.90,.915,.985,.99]$ 与晚段负号 $[1.423,1.428,1.442,1.445]$；仅整帽支持在平台内的共同迹列可消元。晚 node118 不消整列。

负号代数按 $P_-(S)=-P_+(-S)$ 实现；完整值、角导和参数导一同变换。状态偏导的两重符号相消，$K$ 的值/角混合偏导则保留外层负号。原准确 PSD cut 旁路只用于原正号末窗，不能用于新的负号窗。所有旧文件保持未改。

新窗所遇到的整单元，在全部真实物理断点及窗口四端点分片后，以 G8 同点积分完整实际 RHS。精确端项是完整实际 $n,m$ 的两端函数差；角漂移、原 metric 导数、尾及七个物理参数列全部保留。没有把 raw 与 nonlinear delta 分别用不同点求积。没有落在新窗的单元保持原 R152/R153/R155 消费者；旧 coast 另由 R165 保持。有限积分规则明确改变，须建立新的 baseline/normal，不能沿用旧 35 的数值或线性化。这个 G8 仍是有限规则，不冒连续积分误差为零。

实际命令（本课题目录）为：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python scripts/fd2d-run-observed-command.py \
 --receipt notes/2026-11-12-fd2d-signed-trace-local-01-process-receipt.json -- \
 python scripts/fd2d-signed-trace-local-check.py \
 --request notes/2026-11-12-fd2d-raw-bump-dyadic35-request.json \
 --out-prefix notes/2026-11-12-fd2d-signed-trace-local-01
~~~

仅这一次实际执行，session84514，ac4fe6→d09eae，child/wrapper/终端全部自然0，内部3.917537秒。输入是旧真正接受态 b075，不是未完成的35试步。复做应改新输出 stem，保留原实际回执。

节点84、118的完整状态/尾/物理参数合方向差分与解析 JVP 相对差分别约 $3.87\cdot10^{-9}$、$1.28\cdot10^{-8}$。node118 的新负支值约为 $(n,m,l)=(-.00484265,0,-8.07838474)$，其实际 $Kpprox.03912080545$；节点平台 Gauss 仅剩浮点评价值约 $10^{-14}$。这是新非线性场代数的有限比较，不是原场已经达到 Gauss 的证明。

两个非零单元82、118真正消费完整 split-G8，retained/high JVP 相对差均小于 $5.93\cdot10^{-9}$。它们的真实 retained L2 反而分别约11.81和38.92；局部变换不冒整体改善。新初始 warm 的共同迹规范变化仅在证明的整帽平台，实际节点函数舍入差至多 $1.78\cdot10^{-15}$。新文件按自身 schema 保存后被自身新构造器真正重新读取，原源/旧态未覆盖。

新 warm 是明确的表示初值，并非 Armijo 接受态。下一由独立 context 全链计算新完整 F，装其自己的 normal，并支付真实试步。连续 $K$ 的充分线性域由 R182 另导出；采样 guard 或浮点 QP 成功都不能冒连续域证书。
