# R854：真实 N112 预算断点与同核继续

日期：2026-11-16 UTC。会话：serre-public-astra-20261115。

原公开 run **43832705685** / compute job **133181715849** / source **2ee14751d7b2cb4403931886b587ca6f64138c73** 于 13:38:01 UTC 保存预算断点。原数学核实际 exit **124**，没有外层 timeout；不是 N112 精度不足的判断，也不是四个响应球已经完成。

## 1. 真实已完成状态

本轮保存 **1041** 个完整数学阶段，完整输出清单含 **1051** 项。必要旧工作文件已经按原压缩规约退役，9515 个旧工作文件的身份留于116个退役回执，不重新计算。

N112 完整原清分母算子索引实际已完成：

- 文件 R854-p41-N000112-full-cleared-operator-index.json.gz，21259 B；
- SHA256 **3d0d491964e620ae3e6923710d0a37e80959169efd0e19d6da83bc214e27f21c**；
- 实际工作精度为112；原自由列负号、原唯一 U1 解与完整算子列保留。

最后已读的 saturation profile 编号63为完整阶段，记录输入绝对 B 精度49、该阶段剩余矩阵的模秩7及完整剩余域行恒等式。它不是原2420未知数系统的最终满秩或逆界。该文件10805 B / SHA256 **aa6b510495f52e3c6580f55deaea5badec7194a3d1cdbdedada73f2992f30b9e**。完整 current work 由原 manifest 恢复；不从这个局部秩另造一个断点。

实际 false FINAL 为13180 B / SHA256 **9556c897a5e0c0ead6504ddf40c4c6bcfb5ec2c7aa3172cb0ac394f6239c02c2**，其中四球、实际绝对响应精度和单位子式/左逆界均未提供。请求目标7仍只是目标。

## 2. 同核原来源身份

|来源|字节数|SHA256|
|---|---:|---|
|完整输出 manifest|177483|3ea125ba8307e5eef774a3236c1ffd5ab32d92ff3a1f6e84b9d16dd1da829077|
|manifest reference|223|abcba7e76f6be432609f17e20246eb373dfe7684e4f341d39980014f1cdb6364|
|core receipt|12850|f98499fa39f045b4808088ee2b3cd19469c322bf463d6de570225b5c3b1f2c84|
|stage manifest|58114|326d7035c5934a591945bfa9e1a041622e3b6669cde1340c2d6311a2e5d45ac8|
|原输入 carrier|135471278|bca10118a3f81600c83f5bf4232090555da2527cb8a3bdbb79ffff70fb70d104|

实际 artifact **14229723159** 为295748092 B / SHA256 **9e1f26d259668b1448e760eadd5a1fa4cebedf8f6ac2a30b353f388444672bea**，到期 2026-11-17 13:38:05 UTC。本次只做 ZIP/JSON/哈希来源读取，未在外部执行数学核。

数学 core 仍为 **1feb579a88879739a250f889ab1818019acb8f1156a0e3f34d57b8524024125f**，wrapper 仍为 **f6b97a7d0640a03fa099d3b0b04541318e53ddbcf611a876f877b3dc42c7f0ae**，配置 **227767127d21d420d5ffdcef87c8f18627cdc92fd22b4d7cf9b5d036c997f10f** 不变。当前请求只改真实 resume 来源和已读规则提交；工作精度仍112、目标响应精度仍7、预算仍300分钟。原低位、完整行操作与1665个 carrier 成员全部逐字恢复。

## 3. 后继必须保留的数学对象

继续原 p=41、uniformizer B=lambda*b、完整14个 L 坐标、原2560行、2420未知数及 free1186。几何行尺度 S_m、原 tall matrix 的真实左逆界、两分母、ZP=(Z42−beta42)/42 正号、t/u 双条件、全部 H_n 和尾界，以及 Trace14/2/c_chi 保持不变。

只有真实四球和所需精度全部完成后，才填 R858 的两个 input。N112 足够与否、原 A.1、实际 Z、全局高度和绝对 Serre 一致性均未由本预算断点解决。

[前一 N56 精度退出与 N112 激活](R854-actual-N56-precision-stop-and-N112-continuation.md) 的准确来源和推导继续有效。
