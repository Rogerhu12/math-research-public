# 完整 P1：v2 实际结果与原式有理评价的分离泛函设计

日期：2026-11-14。本文记录已发生的 v2 Actions 结果，并定义下一项不同的准确检验。新有理 profile 检验尚未执行；本地仅运行本文第 7 节的小型人工开发检查。

## 1. 已有实际结果解决了什么

公开 run `43633746055`，源提交 `26c3f2c0308d179a094d3967cfb7189db426081e`，实际回执是 [full-phase-bridge-exact.json](actions-43633746055-1-full_phase_bridge_exact/full-phase-bridge-exact.json)。原字节 157380 B，SHA256：

`7c2cb9fece518fb6fbb15b6b4e034565dfcc5a10cf0e103a7011cd56dc4ac960`。

它在 122.3120001 秒内完整结束，峰值 RSS 121.64453125 MiB；不是预算退出，也没有正关系复核失败。

完整外槽第三算子的 152 个原始模板，先缩为 36 个原始模板的子集。其余 116 条线性关系都回到原始公式，用新正规化器复核为零。这里只得到真实函数空间维数不超过 36；36 个代表独立不等于真实函数独立。

五段真实 scalar 基准的三个系数分量分别从 495、238、198 个原始项缩为 42、0、0 项。后两分量对应 $a=2+\sqrt3$ 和 $\log a$；它们的两种 P1 模式已各自回到原式验证为零，因此不是要求把无关非有理系数假定独立后留下的障碍。

剩下有理常数分量的联合目标有 1202 个 word 项，36 列的代表秩为 36，消元后有 1374 项，余项 SHA256 为：

`57a70c438fa3cff7a523bc5c55b522eb1df6c9268ab416755c0c073dee60a4f4`。

该报告只预览前 24 项，不能从预览断言某个模式的全部余项已经消失。该结果也不证明函数非成员。已有 [R82](../results/R82-exact-pure-P1-endpoint-and-genuine-bridge.md) 的 pure 正关系和 [R81](../results/R81-real-third-hook-control-and-mixed-phase-response.md) 的真实 hook 方向均保持有效。

## 2. 下一项检验不再比较 word 代表

新文件是：

- `scripts/literature_rational_volterra_polynomial.py`：原始 profile DAG 的有理多项式评价、有限域精确化和分离子式。
- `scripts/literature_full_phase_rational_dual.py`：绑定上述实际回执、原始目标、36 个原始控制模板及完整基准。

两个模式始终使用同一组实控制系数。利用 [R80](../results/R80-complete-third-affine-class-and-P1-endpoint-obstruction.md)，所有真实第三控制变化都已落在该完整空间内；新程序不会再添加未定义的“可能还有的变量几何方向”。

程序重新生成当前输入所需的原始公式，并核对实际 v2 记录的全部 152 个原始模板 hash。它不重新求解旧 word 联合目标，也不把已有 116 条关系当作需要再次运行的研究任务。36 个保留列和五段原始基准通过旧回执的原式证明绑定。

对基准常数分量，程序使用

$$T_{\rm rat}=T_{\rm original}-\sum_j\alpha_jT_j,$$

其中 $\alpha_j$ 是已发布的基准吸收系数。**这里仍是原始公式的差，不是 42 项 word 代表。** 另外两个分量已准确落在同一真实控制空间内，先用已证系数支付；这不会限制随后可选的实控制变化。

程序对每个原始右积分节点真正进行多项式原函数计算，不使用 IBP 正规形来判定评价值。

## 3. 同一对实有理 profile 与共同右锚

固定支撑 $[2,3]$，令 $t=\xi-2\in[0,1]$，默认取

$$f(\xi)=[t(1-t)]^8,\qquad
g(\xi)=[t(1-t)]^8(1+2t+3t^2+5t^3),$$

并在支撑外取零。两个实函数均为 $C^7$，在共同更大紧区间 $I\Subset(1,\infty)$ 的两侧都有开放零 collar。它们只用于准确函数测试；**未施加三矩圆条件**，也不将其作为完整曲面候选。

取 $q=f+ig$，$\bar q=f-ig$。同一对 $f,g$ 用于全部 36 列、两个复模式和所有查询点，不允许按行更换 profile 或控制参数。默认 48 个查询点为

$$t_j=j/49,\qquad j=1,\ldots,48.$$

每点有 $-4,-2$ 两模式的实部、虚部，共 192 个实有理线性条件。

在支撑内部，共同右 collar 原函数准确等于从 $\xi=3$ 开始的原函数；支撑与实际外 collar 之间的所有原始 profile、场和右原函数均为零。对一般实现区间 $[l,r]$，评价器显式保留

$$D_\xi=\frac1{r-l}D_t,\qquad
I(F)(t)=(r-l)\left(\int_0^tF(s)\,ds-\int_0^1F(s)\,ds\right).$$

因此 $I'=1$ 且 $I(1)=0$；正右尾是 $J=-I$。程序不把左尾设为零，也不在新的 profile 槽调用中改变右锚。复乘法是普通双线性乘法，不取绝对值平方。

程序对原始第三模板和常态目标的输入 jet 阶数显式设门：均不得超过 4。与二阶算子复合后，用 $C^6$ 控制即可保证所需有限点值连续；本次 $C^7$ 零延拓有余量。若将来提高 jet 范围，程序会拒绝执行，必须先更新此正则性论证。

## 4. 为什么模质数可给准确有理反证

原始公式的系数有理，输入多项式系数有理，全部查询点有理。有限次求导、乘法和有固定右锚的多项式积分，仍给 $\mathbb Q(i)$ 中的值。分开实虚部后得到真实有理矩阵

$$A\in\mathbb Q^{192\times36},\qquad b\in\mathbb Q^{192}.$$

这里 $A$ 是 36 个真实第三控制的完整两模式响应，$b$ 是常态目标加 $T_{\rm rat}$ 的响应。恒等式若存在，则必有同一 $c\in\mathbb R^{36}$ 满足 $Ac=b$。

默认质数 $p=2147483647$ 先用整数试除准确检查。每一个实际出现的有理分母——包括原式系数、坐标比例和多项式积分的 $1/(j+1)$——都检查模 $p$ 可逆，完整分母集合及 hash 写入报告。因此计算是一个真实有理 straight-line 程序的合法模 $p$ 化，不是数值积分或随机近似。

只有以下情况才给负证书：找到 36 个控制行组成方阵 $A_0$，以及另一行 $(a_*,b_*)$，使

$$\det A_0\not\equiv0\pmod p,\qquad
\det\begin{pmatrix}A_0&b_0\\a_*&b_*\end{pmatrix}\not\equiv0\pmod p.$$

两者都是有定义模化的真实有理行列式，故在特征零中也非零。定义真正的有理评价泛函

$$\Lambda=\operatorname{ev}_*-a_*A_0^{-1}\operatorname{ev}_0.$$

由矩阵恒等式，$\Lambda(A_j)=0$ 对全部 36 列**准确成立**。另一方面

$$\Lambda(b)=b_*-a_*A_0^{-1}b_0
=\frac{\det\left(\begin{smallmatrix}A_0&b_0\\a_*&b_*\end{smallmatrix}\right)}{\det A_0}\ne0.$$

这就是由 Cramer/cofactor 定义的有理分离泛函。无需打印可能很长的特征零分数。报告给出全部选中点、模式和实虚部标签，37×37 模矩阵，两个非零行列式，模泛函系数，逐列零值，以及目标非零值；任何复核者可从绑定的原式 evaluator 和有理 profile 重新得到同一矩阵。

**若模控制秩小于 36，程序只报未定。** 不能把模小秩当作真实有理秩的上界。若模条件恰可解，也只报本次点值检验未分离，不能宣称全函数恒等式成立。以上成功门没有概率或浮点阈值。

## 5. 成功证书的范围

如果成功，首先严格排除“同一组真实控制对所有共同 profile 都有效”的 universal 完整 P1 恒等式；也排除所测试的这对有限正则 profile 的完整全函数匹配。它不排除其他 profile 平面，不排除多个不同 bulk pair 合并，也不把三矩、低阶双 collar 或完整曲面条件视为已付。

还有一个有限范围的连续性后果：非零增广子式在 $C^6$ 小扰动下仍非零。因此可把这对 $C^7$ 零延拓在共同支撑邻域内作 $C^6$ 光滑逼近，得到某些真正 $C^\infty$ profile 对仍不能通过该完整 P1 门。这不是一个已明确构造且配平三矩的 $C^\infty$ circle；报告不会把该存在性连续后果误写成已支付的具体几何输入。

不论成功与否，$P_0$、第四 ruling、更高阶、收敛、嵌入、reach 和宏观幅度均未由此支付。

## 6. 公共 Actions 命令和预算

在本公开仓库 Actions 中运行：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_full_phase_rational_dual.py --output "$OUT/full-phase-rational-dual.json"
```

默认总时限 300 秒，RSS 软轮询上限 1024 MiB，多项式次数上限 256，操作检查次数上限 20000000，输出上限 300000 B。质数、点数、bump 次数全部写入输入定义。改变它们是新的测试身份。

入口同时检查 `GITHUB_ACTIONS=true` 和 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。预算退出、源码/回执不匹配、分母不可逆、未支持的有理函数积分、输出超限都会留下明确失败回执，不能升为数学阴性。报告保留每列进度和逐列多项式 hash。完整原式评价不在本地运行。

## 7. 本地已做的小型人工检查

`--toy-only` 只检查：非单位区间的导数比例、真实有符号右锚、保留非零右端边界项、普通复平方、右积分 shuffle、原始小 DAG 的积分/jet 评价，以及 3×2 人工矩阵的分离泛函。另有两个反例门：模控制秩不足不得给结论，有限点模解不得给全函数正结论。

开发输出为 [literature-full-phase-rational-dual-development-toy-20261114.json](literature-full-phase-rational-dual-development-toy-20261114.json)，4903 B，SHA256：

`34f2acfd72010bed5463f72d102a3db6a3946e6e0ff9d11e983eb052a3ae127c`。

它没有编译实际目标，没有评价本节之前定义的研究 profile，没有运行几何积分或优化。研究结论等待公开 Actions 的新实际回执。
