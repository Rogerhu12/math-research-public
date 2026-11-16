# R858：冻结的原 41 单 Z 消费者与待到达响应源

日期：2026-11-16。状态：**方法与完整代码已备；原 R854 的真实响应输入尚未到达，未启动本消费者的数学任务。**

## 1. 固定原来源与实际计算范围

数学方法为 [原加法链与完整尾界](R858-original-p41-single-Z-from-chain-and-tail.md)，SHA256 `39bca8a312c32b81f0813100dcbdbe4ff4a11f9cb66abbab6a9af98c1a66bbf7`；原来源契约 `569aa684267e4c4ae76581ce6ad6c6b4fd2ad62b45869ed87809a4c22151eeee`。保SP、ZA、41S的全部规范和真实c0/c1。

实际消费R852的839节点原程序、原四响应切口、17个准确域常量及已经计算的五C；不重解原unit-chart或旧C/Q秩。点是原f4(c1)，不是另一个f_R(c1)。沿1,2,4,5,10,20,21,42七步链，使用正secant加法式计算β42，最终Z(P)=(Z(42P)−β42)/42。

实际t/u两个深盘条件、整H_n系数和对所有后续项成立的尾界必须分别得到。负赋值球、B=lambda b原e7/f2域、σ对完整球及原s共轭保留；最后五行是cχ·Trace14(C_j Z+D_j)/2，cχ保留符号值，不置1。没有用84次域迹或额外因子6。

## 2. 冻结代码及请求

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| scripts/R858_original_p41_ball_arithmetic.py | 34080 | 767b01cba9bfa966d1a545b72abe51fe0b9edc407638db5947ec5dba28637fa3 |
| scripts/R858_original_p41_single_Z_consumer.py | 59095 | 85fd249b705005e1ad81712350990414915eb78f3d4622571bc2361183b7521e |
| scripts/R858_public_original_p41_single_Z.py | 53760 | fb77d8fb452a5efbc2cc8e9b7af8a090813ebd9c9e8fb416ee62ea09be88c8ab |
| .github/workflows/serre-R858-original-p41-single-Z.yml | 6505 | e9591fa4640e931af7fea9db69a32dab920ca3dc96b287bd6d59eef874515003 |
| notes/R858-original-p41-single-Z-public-request-pending.json | 15782 | 5288ae542e1d3dc8ed7ab975e8e4131f2d056507450785a46394a1e7edb9e823 |

RESULT为 `R858-original-p41-single-Z-and-elliptic-rows`，FINAL为 `p41-original-p41-single-Z-and-elliptic-rows-certificate.json`。CLI接受 `--config --retained --output --budget-minutes`。exact-leaf B precision256、series block16、目标Z/五行B精度7、maxterms10000、预算300分钟；均按各字段在核心中的身份/控制划分处理，目标不代实际精度。

pending请求中 `producer_inputs_pending=true`，`sources.R854`、`inputs.response_certificate`、`inputs.four_response_balls` 都为null。workflow只自动匹配未来活跃请求文件 `R858-original-p41-single-Z-public-request.json`；本次pending登记不会触发。当前观察到的R854为run43805506433/source dc6ffb07b398e5262d6b1e62dbc72378a163b5f3，仍在原数学步骤；没有预填未来artifact/manifest/config/SHA。

## 3. 真实已取来源及未来最小响应闭包

已逐SHA/schema读取R852的13件、CM的8件、R791的9件，共30直接选件，并通过冻结R852纯IO取得原9件载体及原270叶的全部SHA/父子配置同一性。原2.53MB载体 `44d40476878e6de8a2121e81b2ab6f68e57d3b4c19857119095f7477e978f8b4` 完整保留；后继从R852当前包直接续载，不再请求旧R847或旧CM/R791已到期artifact。

未来R854只取真实final、four-response stage、source-audit/stage-index、unit-minor/left-inverse界、完整原残差certificate、残差向量及其last-digit依赖/元数据。大型operator和residue inverse不搬入本消费者。允许读取已真实认证但未达父请求阈值的球，前提是原R854明确认证标志、完整残差、逆界和实际精度都存在；不得把失败过程或目标精度充作球。

## 4. 续算与终点

每个阶段原子保存。同tag恢复保所有已成stage和最新current；旧false FINAL只是历史快照，不能锁住之后的新stage。外层timeout在预算后留900秒，再TERM/短宽限/KILL，缺core receipt就如实保缺失；不补造数学结束信息。新的真实输入球身份变化须保持新的来源tag，不能把旧球改标签。

终点区分“实际计算Z球”“正绝对精度”“达到请求精度”，五行也逐个记录真实B精度。零球不是准确零证。全tail只有严格整数不等式实际满足后才通过。Y/Picard、全球Hecke校正、非p项、完整height、A.1和全p一致性保持未成。

本地只读源码、AST和原源IO，没有运行新数学。原机器产物不进Git/Release；后继必要原输入和检查点只用一日Actions artifact。
