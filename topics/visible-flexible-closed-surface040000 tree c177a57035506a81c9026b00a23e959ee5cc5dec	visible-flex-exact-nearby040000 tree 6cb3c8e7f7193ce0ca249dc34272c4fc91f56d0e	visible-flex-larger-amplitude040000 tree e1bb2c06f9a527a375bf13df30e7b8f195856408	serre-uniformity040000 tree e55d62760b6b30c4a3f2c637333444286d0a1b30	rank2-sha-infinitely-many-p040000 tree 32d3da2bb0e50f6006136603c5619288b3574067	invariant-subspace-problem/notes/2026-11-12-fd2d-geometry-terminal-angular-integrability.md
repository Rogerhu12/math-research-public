# R174：新尾控制域的真实末端角 jet

完整证明在 [R174](../results/R174-integrable-terminal-angular-jets-and-actual-body-cut-limits.md)。本文闭存该证明的有限系数消费者，不是 body 或 BVP 运行报告。

## 已证明的输入和结论

R172 的准确末格使用真实物理坐标 $s$，令 $\tau=S-s$。raw 是 $\tau/\ell$ 乘保存的末行，尾权重仍复合 R172 明确的 $\sigma$，物理半径和 $K$ 不改坐标。R170 八段局部 Bernstein 控制非负，保证真实尾曲率 $\kappa\ge0$；全局控制可以为负。

准确曲率下界 $K\ge k_-\tau^3$ 与非负曲率的 Glaeser 估计结合，给 $|h_{uu}|\le C_0+C_1/\sqrt\tau$。这个界覆盖 $\kappa\asymp\tau$ 时与 raw 的相消区，也覆盖全零尾开弧。故 $\alpha_{uu}$ 径向可积，完整 II 的值和角一导有真实 cut 迹。R124 实际标架/位置的角两导继而有真实 cut 极限。R126 的边界二 jet 函数可以取其自身角导，不需要内部 $II_{uu}$ 一致收敛。

实际拼接仍需真实积分得到的边界位置、标架和 jet 对齐；没有把形式 II 或有限 ODE 容差当成这些证据，也没有添加径向 $C^3$ 要求。

## 唯一实际消费

输入为第 27 轮 `grouped27-trial-back00-a01-accepted.npz`，SHA `2b65810c5c09985d54544e6ca697ee609f066a17ecbce4b83e89adad0b52ae6f`，共 131 节点、K31、tail16、profile7。R171 准确 profile packet SHA 为 `7bedd394db9ab0fc3b1d3186c49225ae8f7765ca6d28a80560aeb8842a26ee7c`；R172 definition 的准确末格宽度上下端与它核合。没有将浮点末点当成准确 $S$。

只运行一次修正 JSON 整数解析后的消费，真实自然退出 0：session `75277`，初始 chunk `13f7a8`，终结 chunk `73097f`，内部耗时约 0.160 s。此前一次启动在把 JSON 字符串转 Fraction 时真实退出 1，尚未计算常数；原因和回执均保留。

保存的常数是准确有理上界，以下仅为方便阅读的浮点显示：

| 量 | 上界显示 |
| --- | ---: |
| $M_0$ | 0.325211431 |
| $M_2$ | 50.3420501 |
| $B_0,B_1,B_2$ | 2050.78130，13268.6390，204127.275 |
| $|h_{uu}|$ | $9656.7363+521.1754/\sqrt\tau$ |
| $|\alpha_{uu}|$ | $5234.6067+260.5877/\sqrt\tau$ |
| $|\alpha|,|\alpha_u|$ | 5.54213，40.98089 |

这些界为终端余项提供明确可积模，不是实际最大值；它们本身也未提供一个可接受的 whole body 误差预算。`body_variation_bounds` 要求调用者提供实际 $r,b,v,c$ 初值的上界，没有暗填一组初值。

另用 R170 的严格扩大见证 $P(q)=(q-1/2)^2+1/128$ 核有限系数入口。其全局中间控制为负，八段局部控制仍为正，度 23 曲率控制和一、二导上界正常生成。每个局部多项式在三个有理点核了乘积恒等式；连续界来自准确控制凸包及完整证明，未使用这 24 个点冒充区间证书。

## 接口

- `terminal_angular_majorant(controls, raw_last_left, modes, ...)`：从真实有限系数和准确末格宽度/phase 数据生成有理上界。
- `terminal_integrals(packet, epsilon)`：给终端 $h_{uu}$、$\alpha_{uu}$ 积分余项及值/一导迹的余项。
- `body_variation_bounds(packet, initial_bounds, epsilon=...)`：条件于真实初值范数，给 R124 的角变分范数与 cut 余项。

本组没有求 ODE、body、F/J、normal、QP 或 BVP，没有修改任何输入或物理 $g$。R172 旧 `AccurateLastCell` 的旧域 guard 和源码保持不变；完整新尾域仍使用后续显式 adapter，不能将负全局控制送入旧入口。
