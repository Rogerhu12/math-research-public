# 保存稠密参考多项式的准确端点跳跃

本节只认证明确的有限参考函数。它不认证 ODE 残差、真实解、真实
Jacobian、初始 H 或参数二阶 Taylor 费用。

## 1. 准确输入和参考函数

将保存的每个 binary64 时间、状态及 DOP853 系数还原为准确有理数。
设第 i 段时间端点为 tau_i、tau_{i+1}，保存的归一化分母为 h_i != 0，
初值为 Y_i，七个向量系数为 F_{i,0},...,F_{i,6}。参考函数定义为：

    z=(tau-tau_i)/h_i
    P=0
    for k,f in enumerate(reversed(F_i)):
        P=(P+f)*(z if k%2==0 else 1-z)
    P=P+Y_i

此嵌套式是次数至多 7 的有理系数多项式。它在 tau_i 的值准确等于
Y_i。验证程序另逐项核对 dense_t_old=accepted_tau[:-1] 和
dense_y_old=accepted_state[:-1]，所以相邻段右侧初值是保存的
accepted_state；这些等式不从数值算法名称推断。

允许时间顺序递减。所有端点代入都使用有符号 h_i 和准确时间差。
特别是 h_i 不自动替换成 tau_{i+1}-tau_i：二者都以保存的 dyadic
数为准，并单独比较。

## 2. 端点值和跳跃

令 z_i=(tau_{i+1}-tau_i)/h_i。若 z_i=1，嵌套式从外层直接给出
P_i(tau_{i+1})=Y_i+F_{i,0}；若 z_i!=1，用完整有理嵌套式计算。
两种分支都没有浮点多项式求值。

定义跳跃向量 d_i=Y_{i+1}-P_i(tau_{i+1})。保存的轨迹可以不连续；
本证书不会将 d_i 强制设成零。对每个状态分量 c、每条射线 r，
准确计算 S_{c,r}=sum_i |d_{i,c,r}|，再对 r 取最大值。若后续误差
传播只需未加权的总跳跃，则 max_r S_{c,r} 是该分量的统一上界。
若后续需要不同的传输权重，必须按各段的 jump 与真实证明的权重
重新组合；未加权总和不会自动给出加权结果。

JSON 中的 binary64 上界先由有理数转换为 binary64，再按有理比较
检查是否向下；若向下，向 +infinity 取下一浮点数。于是显示的
上界 b 始终满足 exact_binary64(b)>=S。最大总跳跃同时保留准确
分子、分母，以便独立验证。

## 3. 状态解释

本射线包的三行分别是 theta、log_J 和固定径向位置的参数变分。
第三行的局部多项式没有包含整分支结束时的移动两端点校正。该校正
属于返回映射参数列的定义，不能被当成积分状态的跳跃费用。

参考权 q=exp(log_J polynomial) 在每个闭段严格为正。若需要跨段的
q 比值，可由准确的 log_J 跳跃再做有向指数估计；本 jump 程序仅给
log_J 的准确跳跃，不将其解释成真实 Jacobian 的跳跃。

## 4. 同一新 trace 的实际重新计算

执行器恢复后重新积分 exact-affine 第二步对象的第一块 43 条射线；
不是恢复丢失前 trace 的字节。对象 JSON SHA 为
`aa5df888dbf672c9e221f03e80cfa06c3c9c94a5dd7dd4f29fe15b1d795d99b1`，
准确参数仍为 `-15291006546051/9007199254740992`。
新 forward trace 是 141 段，SHA
`60b0cc65c70ff5aafe872a3a405b3402d96792d61e3db34a485cd0b3b7a36492`；
新 backward trace 是 177 段，SHA
`ec274caa578f35092a21384e4173562d56499658a84097db4950d183093614f2`。
二者都由当前重建 runner 真实重跑生成。

在这两个 trace 上，保存 h 均准确等于相应两个 dyadic 时间的差，
故所有端点 z=1；程序同时保留一般 z 的准确分支。
非零标量跳跃数分别为 88 和 133。每条射线先按段累加绝对跳跃，
然后取所有射线最大值，得到以下向外 binary64 上界：

| 分支 | theta 总跳跃 | log_J 总跳跃 | 固定 x 参数态总跳跃 |
|---|---:|---:|---:|
| forward | 3.6687114527951883e-20 | 7.37257477290143e-18 | 3.3881317890172014e-21 |
| backward | 0 | 1.0625181290357943e-17 | 6.776263578034403e-21 |

每段的分量最大值、每条射线的总和、最大总和的准确分子和分母
已写入 `block_0000_forward_jumps.json` 与
`block_0000_backward_jumps.json`。它们与两个 trace 同在
`data/phase_ring_continuation/exact_affine_step2_dense258/`。
实际计算源 `scripts/fourfold_dense_trace_jumps.py` SHA 为
`bc9e18c464bbfd523f7ba5e83ee44ae883a3791a4b5d1a656a626e3bdca873bd`。

准确重跑命令见 recovered-exact-affine-evaluator 笔记第 4 节。
这些有限 jump 费用可以接到 R60 的参考误差传播，但不支付其真正
ODE 残差或整个初值/复角管。跨两个分支的参数列用链式法则与移动
端点修正合成，不能把第三积分状态的 reset 误称为遗漏的跳跃。
