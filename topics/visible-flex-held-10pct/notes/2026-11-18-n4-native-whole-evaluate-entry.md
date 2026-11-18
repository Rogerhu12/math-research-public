# n4：原完整尾评估的 native 批接口与实际尖点网格

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

本条登记独立来源树里的完整 evaluate 接口，以及实际执行通过的静态输入身份检查。随后启动的一次全尾评估另记真实终态；本条不预判其残差或 DN 验收。

## 1. 改动限于流提供者

入口仍读取原完整失败态 b4356eab…：M20、spacing4、N512、物理深度8、parts32、每普通区间 RK16、原生产 projectionFloor=.05。原物理轮廓、全部40个状态分量、完整 H、原线性远端图和节点均保留。

install_native_batch_adapter.py 在独立 n4_work/native-batch-source-v1 中只对原 core 作三个可逆的字面替换：增加 lazy backend、让 lexical evaluate 一次取得全部原次序的 flows、增加只读接口。worker 只换工厂 import。逆替换逐字节恢复原文件；split 工厂和 same-mu engine cache 不改。五项语法检查实际返回0，未通过语法检查来声称数学验证。

backend 在 split 工厂的 Object.assign 已完成后才缓存固定 DN 的系数。每次完整 evaluate 启动一个已编译的 CLI，而非逐尾段启动进程。当前库仍是已登记的 formed-moment、普通 RK 和字面隐式 Jacobian 实现；没有叠加 shifted-root 或补偿求和。

原左右端残差、归一尺度、far Robin、稀疏线性系统及其后向误差门、线搜索和 2e-9 接受阈值没有修改。cutJets、物理 jets、有限差分和 audit 仍用原 .05 的引擎。实际 DN 求解与这些审计尚不能由本条静态接口检查代替。

## 2. 状态、导数和均值单位

每段输入直接为原 states[n+1] 的40个分量，加两个初值为0的均值分量。输入没有乘 portRatio。原 profile 已由 subdivision 改写为该段坐标，故 geometry(...).drdx 不再乘一次分段尺度。

native 完整保存42个末态及 $42\times40$ 变分矩阵。回到原 Node 求解器时，只将 $\pi$ 的输出行与相应 Jacobian 行除以该段原 portRatio；没有输入列缩放。原 sparse correction 和切口图仍消费前40行形成的 $40\times40$ 矩阵。每段均值高度仍是原两个附加分量的和。

二进制 token 只绑定输入 payload。来源树、CPP、header、CLI 和数学运行库另行核验，不能把 token 解释为来源证明。失败时保留输入、部分输出、stdout、stderr、真实返回码和错误分类。原 trial catch 没有改写，因此任何已记录的工程中断都不能被后续泛称为数学障碍。

## 3. 实际尖点网格与静态身份

producer 分别照原 variational 路径的 integrationGrid 和原 scalar 路径的 splitIntegrationInterval 构造全部网格，再要求二者的字面 $x,h$ 字节一致。RK 中点保持原 x+h/2，没有换成代数上相等但浮点结果可能不同的表达式。

实际缓存完成后的计数为：

| 项目 | 实际值 |
|---|---:|
| 尾段数 | 2304 |
| RK 步总数 | 36891 |
| 各段不同系数点总数 | 76086 |
| 含额外尖点步的尾段数 | 27 |
| 完整输入字节数 | 21640952 |
| state-only 输出的协议字节数 | 940120 |
| fullJac 输出的协议字节数 | 31905880 |

两个输出大小由已测段数及固定格式给出；此时尚未把预期大小称为完整输出已生成。静态准备约1.20秒，也不是全尾流的运行时间。

在任何 native 调用之前，原43、38、175三个样例的全部144个已存系数点、原 state 三角表、126个输入分量、全部原网格 $x,h$、$\mu$、端口比例和归一尺度均逐位一致。独立只读 collector 还直接解码整个输入，核对2304段全部原40分量及两个0均值、系数块/网格哈希、EOF和 payload token。

完整表和状态只保存在 scratch。可发布记录保留来源、哈希、命令、上述总计数和标量，不把逐段网格或场表放进仓库。

## 4. 接续状态

固定计划 a466fa5c… 的唯一 observer 会话67330已经开始一次原完整 evaluate(states,target,true,scales)。这一步没有调用 Newton correction、DN solve、cutJets 或 audit；即使同态残差低于门，也仍须由后续原 DN/Jacobian/audit 全流程实跑验收。

完成标准所需的精确圆弧、完整闭族、连续误差证明与10%几何比例仍未由本条支付。
