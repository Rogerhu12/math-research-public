# 原 Bell 三次幂的严格非成员性、完整权九来源核及自然权十二下界

作者：Astra-ISP-789f / normal_annihilator（AI-assisted：GPT-6 Astra Pro）  
日期：2026-11-16

## 1. 已完成的结论

对既有完整十七变量原梯度模型，令 $J$ 为十七条原梯度生成的理想，令 $b$ 为既定匹配三次数域中的原 Bell 多项式。本次真实原矩阵运算证明

$$
\boxed{\,b^3\notin J_E\,}.
$$

这里保留全部六个 mean 变量与十一个 Hankel 变量，没有固定参数纤维、没有删去来源，也没有倒置任何 mean 或 Hankel 多项式。

同时，完整加权九次来源矩阵满足

$$
\boxed{\operatorname{rank}_{\mathbf Q}M_9=16046,\qquad
\dim_{\mathbf Q}\ker M_9=396.}
$$

因此此前证明独立的 $396$ 条原 Koszul 关系恰为整个权九来源核的一组基。此句是特征零结论；本稿不未经另证声称这 $396$ 条指定向量在模七约化后仍独立。

结合原自然幂齐次化定理，本次还得到：

$$
\boxed{\,t^K\notin
(J_E,\ b-t^3)\quad(1\le K\le11).\,}
$$

若归一 Bell 方程 $b=1$ 与原梯度之间存在单位来源恒等式，其最小最大来源权至少为 $12$。本稿没有给出权十二的正来源，也没有断言归一理想已空或非空。

## 2. 原模型、权和三有理目标

采用原变量

$$
y=(y_0,\ldots,y_5),\qquad H=(H_0,\ldots,H_{10}),
$$

权分别为 $1$ 和 $2$。原 $R_3$ 的权为 $6$，十一条 $H$ 梯度的权为 $4$，六条 $y$ 梯度的权为 $5$。这些十七条梯度与独立原 $N,\Gamma$ 模型的完整多项式身份，已在原模型生成器及父系数审计中逐项核验；本入口保留这些原固定常数归一，不作参数相关的行缩放。

固定数域为

$$
E=\mathbf Q[d]/(f(d)),
$$

其中原匹配三次式为

$$
f(d)=3725d^3-43931504d^2+6080833024d+52565262336.
$$

原 Bell 的权为 $3$。在基 $1,d,d^2$ 中精确写成

$$
b^3=c_0+d\,c_1+d^2c_2,\qquad
c_i\in\mathbf Q[y,H]_9.
$$

父审计已实际构造全部三个有理分量，并从原 Bell 完整乘法独立核回。此处不是把模 $127$ 的一个匹配线性根搬到模 $7$。

完整来源空间为

$$
\left(\bigoplus_{i=0}^{10}\mathbf Q[y,H]_5\,e_i\right)
\oplus
\left(\bigoplus_{a=0}^{5}\mathbf Q[y,H]_4\,e_{11+a}\right).
$$

全部字典尺寸为

$$
\dim \mathbf Q[y,H]_9=49368,\quad
\dim \mathbf Q[y,H]_5=1264,\quad
\dim \mathbf Q[y,H]_4=423.
$$

故来源列数为

$$
11\cdot1264+6\cdot423=16442.
$$

令 $M_9$ 表示上述完整原来源映射，并令

$$
\widetilde M_9=[M_9\mid c_0,c_1,c_2].
$$

矩阵尺寸分别是 $49368\times16442$ 与 $49368\times16445$。

由于原梯度均加权齐次，若某个 $c_i$ 属于整个原理想，取任意来源恒等式的权九分量，就必得到上述完整来源空间中的恒等式。因此完整权九矩阵的非成员性排除整个原理想成员性，不仅排除某个人为来源支撑。

## 3. 特征零秩上界

已发表

[R150-appendix-original-weight-nine-koszul-rank-ceiling-and-rigorous-cube-obstruction.md](R150-appendix-original-weight-nine-koszul-rank-ceiling-and-rigorous-cube-obstruction.md)

给出 $396$ 条独立原来源关系：

- 十一条四次梯度之间的 $55$ 条 Koszul 关系，各乘六个权一变量，共 $330$ 条；
- 四次梯度与五次梯度之间的 $11\cdot6=66$ 条 Koszul 关系。

其独立性使用既有完整权六来源独立性及原分量比较，未使用本次有限域秩。因此在本次运算之前已经严格知道

$$
\operatorname{rank}_{\mathbf Q}M_9
\le16442-396=16046.
$$

本次不会把有限域来源秩当作特征零上界；有限域只负责提供一个真实原子式下界。

## 4. 合法的模七原矩阵

父完整系数审计已真实检查全部 $134399$ 个原有理系数，证明它们在 $7$ 处整。原 $J_3$ 行列式模七为 $1$。原 $f$ 约化为

$$
\bar f(d)=d^3+6d^2+6.
$$

它在 $\mathbf F_7$ 的七个值依次为

$$
(6,6,3,3,5,1,4),
$$

均非零，故为不可约三次式。所有原系数的实际约化、三个目标的完整数域乘法及全部权字典身份，均见

[R150-appendix-original-bell-cube-prime-seven-admission-and-complete-weight-nine-dictionaries.md](R150-appendix-original-bell-cube-prime-seven-admission-and-complete-weight-nine-dictionaries.md)。

新消费者再次核全部 $134399$ 个有理系数和完整字典，随后构造全部 $49368$ 原行、全部 $16442$ 原来源列与全部三个目标列。实际逐坐标插入并检查的原系数产品数为

$$
7023209.
$$

完整输入位面文件大小 $304501928$ 字节，SHA 为

~~~
a687e06da033c68708ee53a5658d95d6259c35a113d36584de78a8868b55b02d
~~~

全部原行在开始消元之前已经构造并封存。随后程序按原字典顺序流式读行；只需一个真实原子式超过上界，便可结束。

## 5. 真实原子式与特征零提升

实际处理到原行前缀 $0,\ldots,16371$ 时，已经得到

$$
\operatorname{rank}_{\mathbf F_7}
\widetilde M_9[0{:}16372,:]=16047.
$$

完整状态记录了：

| 项目 | 真实值 |
|---|---:|
| 已处理原行数 | 16372 |
| 独立原行数 | 16047 |
| 原来源主元数 | 16046 |
| 目标主元数 | 1 |
| 按到达顺序选出的原子式行列式模七 | 6 |
| 逐实际主元取消次数 | 57352603 |

每条保存行都规范为其真实领先坐标 $1$，每次取消都核该原坐标严格为零。原行标签严格递增，主元列互异；完整三位面值、所有未用尾位和保存主元乘积均检查通过。独立原小矩阵自测也验证了非排序主元到达情形的原子式行列式公式。该公式本身如下：每条新行仅减去先前已选行的倍数，再除以记录的非零领先系数；故选中原方阵到保存方阵的行变换行列式为这些系数乘积的逆。将保存行及其同名主元列同时按主元位置排序，所得方阵为单位上三角；两个相同置换的符号相消。因此原选中方阵的行列式严格等于记录系数的乘积，毋须主元按到达顺序单调。

唯一目标主元的原列为 $16442$，即 $c_0$；其原行为 $16370$，规范前系数为 $3$。因此选中的 $16047$ 阶原子式只使用 $16046$ 条原来源列和 $c_0$，而不需要其他两个目标列。这给出

$$
\operatorname{rank}_{\mathbf F_7}[M_9\mid c_0]\ge16047.
$$

这里所有三个目标均完整保留在实际输入中；上述更窄结论来自实际选中原列标签，并非预先删去另两个目标。

由于目标列排在所有原来源列之后，任何目标主元行的来源部分全零；它不能制造新的来源主元。因此实际的 $16046$ 个来源主元也给出

$$
\operatorname{rank}_{\mathbf F_7}M_9\ge16046.
$$

原矩阵在 $\mathbf Z_{(7)}$ 上有定义。模七非零子式的原有理行列式不为零，所以

$$
16046
\le\operatorname{rank}_{\mathbf Q}M_9
\le16046.
$$

从而原来源秩恰为 $16046$。同理

$$
\operatorname{rank}_{\mathbf Q}[M_9\mid c_0]\ge16047,
$$

故

$$
c_0\notin\operatorname{im}_{\mathbf Q}M_9.
$$

本稿对完整增广矩阵只断言秩至少 $16047$，不声称其全秩恰为 $16047$。未处理的 $32996$ 行无法降低已付子式的秩。

整个原来源核的维数于是恰为 $396$；第3节的 $396$ 条独立关系全部属于该核，故已经张满整个权九来源核。

## 6. 原数域 Bell 三次幂及所有共轭

理想 $J$ 定义在 $\mathbf Q$ 上。平坦标量扩张给出

$$
E[y,H]/J_E
\simeq
E\otimes_{\mathbf Q}\bigl(\mathbf Q[y,H]/J\bigr).
$$

基 $1,d,d^2$ 在 $\mathbf Q$ 上线性独立，故

$$
[c_0]+d[c_1]+d^2[c_2]=0
\quad\Longleftrightarrow\quad
[c_0]=[c_1]=[c_2]=0.
$$

已付 $[c_0]\ne0$，因此 $[b^3]\ne0$。同一证明适用于该原匹配数域的每个嵌入；不是只在某个有限域根或某个实数参数点上成立。

这仍只是三次幂的严格非成员性。它既不排除更高幂可能进入原理想，也不把某个归一 Bell 非零分支的整个临界理想判为空或非空。

## 7. 自然齐次幂与来源权

原自然幂定理见

[R150-appendix-original-bell-natural-power-homogenization-and-positive-source-gate.md](R150-appendix-original-bell-natural-power-homogenization-and-positive-source-gate.md)。

设

$$
A=E[y,H]/J_E.
$$

因 $t^3-b$ 关于 $t$ 首一，商

$$
A[t]/(t^3-b)
$$

在 $A$ 上自由，基为 $1,t,t^2$。将 $K=3q+r$、$0\le r<3$，则 $t^K$ 的余式为 $b^q t^r$。所以

$$
t^K\in(J_E,b-t^3)
\quad\Longleftrightarrow\quad
b^{\lfloor K/3\rfloor}\in J_E.
$$

若 $b$ 或 $b^2$ 属于 $J_E$，乘以相应幂也会使 $b^3$ 属于 $J_E$，与本次结论矛盾。又 $J_E$ 由正权齐次多项式生成，$1\notin J_E$。因此所有 $1\le K\le11$ 都排除。

若存在

$$
1=\sum_{\nu=1}^{17}A_\nu F_\nu+C(b-1),
$$

令其最大来源权为

$$
k=\max\left\{
\max_\nu\bigl(\operatorname{wt}A_\nu+\operatorname{wt}F_\nu\bigr),
\operatorname{wt}C+3
\right\}.
$$

按原加权齐次化定理，权 $k$ 的原来源给出 $t^k\in(J_E,b-t^3)$。故本次严格推出

$$
k\ge12.
$$

这是对所有原多项式来源的下界，不只针对某次标准基算法选出的来源截面。没有使用标准基计算超时或某个算法未找到纯幂的现象来证明非成员。

## 8. 执行与完整身份

根另以独立 Python 只读检查完整原输入、全部最终状态、native 回执及日志的字节数和 SHA，并重核全部 $16047$ 个保存行的规范系数、真实原行列标签、唯一主元、未用尾位与系数乘积；同原构造和消元源码均全文独审。该检查没有将未处理行冒称已完成消元。

本次在隔离本地执行器实际完成，exec session 为 $78867$。观察启动时间为 2026-11-16 11:02:56 UTC，最终回执写入时间为 2026-11-16T11:04:30.289514+00:00。

资源参数为 600 秒、2048 MiB。实际总耗时

$$
94.89522280699748\ \text{秒},
$$

其中 native 内部耗时

$$
72.31550364699797\ \text{秒}.
$$

完整输入构造于约 $22.30$ 秒完成。wrapper 记录峰值 RSS 为 $398492$ KiB。程序达到严格阈值后正常 exit $0$，不是预算退出。

数学绑定：

~~~
408ae85f9bb8f01a40d3eb52e0b2425966639dc3e92c92b81ff321483fdb87d4
~~~

主原回执：

- $6416$ 字节；
- SHA 3bb3cee65f3b95da4e9849ec039f0cc2eb5ba36f025deca37575ebb1380808da。

完整最终状态：

- $99170664$ 字节；
- SHA b2ddc46652c741c4dca3b97ad012024c65de4917404eddb0f6f57c4a85df9f9b；
- generation $2$，complete-row-state-slot-0.bin。

native 小回执：

- $983$ 字节；
- SHA 7b170042c72534036429c5f90a64f0838205b4a53014a2657ad72bc1fff8b611。

完整源码和接口为：

- notes/2026-11-16-r150-original-weight9-prime7-stream-rank-789f.py；
- notes/2026-11-16-r150-original-weight9-prime7-stream-rank-native-789f.cpp；
- notes/2026-11-16-r150-original-weight9-prime7-stream-rank-inputs-789f.json；
- notes/2026-11-16-r150-original-weight9-prime7-stream-rank-interface-789f.md。

仅执行身份与输出 SHA 保存于

notes/r150-bell-prime7-execution-789f/local-20261116-original-weight9-stream-rank.json。

实际完整原输入、原行列选择、规范主元、数学回执和检查点都只保临时，不进入仓库。完整输入及状态可由上述冻结源码和参数重建；本结论不依赖未来重建时的数组继续存活。
