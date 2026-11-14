# 公开 request23：完整候选与原无 J 遍历完成，norm 降至0.041773但未接受

[run 43605912092](https://github.com/Rogerhu12/math-research-public/actions/runs/43605912092)，固定源 `ac0fcc220082194344b98f0e6a728453f55222e8`，zerorkprobev3 job `132480432221` 实际成功。artifact `14117693541` 为17,008,955字节，ZIP SHA256 `385bfef92698faed324011e72907ee7282b8b74d1275a1ed150377ea085f382d`。这是[独立 v3 探针](2026-11-14-zero-rk-native-probe-v3-interface.md)的真实结果，不是原完整 native solve/J/audit 的接受。

## 1. 实际原尺度残差

v3 完成577节点、每节点224分量的完整候选。一次原 `evaluate(candidate,target,false,originalScales)` 遍历全部576个 stage，所有原无 J flow guards 均通过，原 methods/graphs/gains/far/layout 结束身份保持。

| 量 | 实际值与范围 |
| --- | --- |
| request19 原冷初猜 no-J norm | `13414069.968482966` |
| request23 候选原 no-J norm | `0.04177307820740199` |
| 新/旧 no-J norm 比 | `3.114124073122471e-9` |
| 原 solve tolerance | `2e-9`，本次候选未达到 |
| 零态线性块残差最大值 | `1.6749038195331316e-5`，只属候选线性计算 |
| 原 evaluate 次数 | 1 |
| 原 native solve 次数 | 0 |

原非线性最大项位于 stage10、rawCell0、rawSegment7、Pi 第95模（column206）：实际残差 `-2.1596910229217223e-16`，除以原 scale `5.170054771158893e-15` 后为 `0.04177307820740199`。原 scale 继续由完整 H/r⁴ 和原 gains 第零模定义，没有用候选分母替代，也没有重定标使残差变小。

零态线性残差的最大项另在 stage8、Pi 第76模，实际 residual `-8.639736061993863e-20`，原 scale `5.15834757867e-15`。两个 norm 来自不同实际计算，不能互相替代，也不能仅凭差值将所有残差归因于某一种误差。全部112行 cut 残差和112行 far 残差在原浮点计算中均为零；这不等于精确实数 Robin 缺陷自动为零，见 [R264](../results/R264-native-underflow-seed-contract-and-rounding-ledger.md)。

原 no-J API 不返回可靠的全 stage minA/minD，本次只报告所有原 branch checks 已返回通过，不伪造域裕量。本次没有 J、fresh audit 或 accepted tail response。

## 2. 完整下溢与符号零记录

实际共有51次非零结果舍入到零：47次高度除法、4次 momentum 乘法。涉及模号66至112、source node261至562。第一例与request22一致，为节点261→262的第112模；这次完整位记录确认结果是负零：

- 左操作数：`0100000000000080`，即最小负 subnormal；
- 分母：`009bff3f1d3e7140`，数值 `275.8821411118115`；
- 实际结果：`0000000000000080`，即负零；
- 原 source scale：`2.4870696617090834e-19`；原 target scale：`2.554646771884616e-19`。

51个事件中25个结果为负零。四个乘法下溢发生在node540、541、542、543的第69模；后续高度除法也被分别真实记录。已经是零的后续传播没有被重复统计为新下溢。所有事件都有真实 operands/result/双尺度位身份和精确局部损失重建表达式，不用 Number 把不可表示损失再算成零。

完整候选中9,546个符号零位置有显式索引。按索引恢复后，全部577×224个 binary64 的 SHA 与原 producer 逐字节一致：

`6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8`。

原577个 scale 的 binary64 SHA 也核一致：

`ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc`。

## 3. 保全与后继范围

71件主要证据分块的文件/解压原文 SHA、记录维数和顺序已核对，含1793个 construction 事件、全部576×112个块、全部577个候选节点、576×224个线性残差、576×224个原无 J 非线性残差和完整边界行。所有原 H 模式、shape列、深侧状态、原尺度与原 native 检查均保留。

该真实结果支持将**同一完整候选**作为初猜送入原完整 native solve/J/fresh audit，仍须由那些原门决定是否接受。后继只注入首次同 H 的 `opts.initial`，不改原 solve 主体，不走几何 warm remesh，不用零幅比预测，也不将本次 probe 成功重新标成 solved tail。

原件 SHA256：

- `summary.json`：`aa93fb8afbd0c8ce3ec49859f3bcfae465696654f626ed1678ceb430329ec6ea`。
- `candidate-checkpoint.json`：`e3952fbd34fa00370e70d78529b219385278c93d11a36df3855d6fcda148e10c`。
- `candidate-initializer-identity.json`：`38f6f6cdbcc7fbe4aece5bddc175fd75dcefdf347eec74b8c1d58d6949d4980e`。
- `launcher-result.json`：`f4fcb485b35026197489449e52b91bdd8ba6c2058b9145962b75c7ee7f27a27b`。

本地仅读取已产生的记录、恢复明确的符号零表示并核字节/维数/清单，未重跑工厂、预测、残差或尾求解。
