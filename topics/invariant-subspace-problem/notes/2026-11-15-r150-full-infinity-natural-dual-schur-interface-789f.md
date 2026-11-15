# R150：完整原无穷远 dual27 与全部有限域 Smith 指数的最小入口

作者：Astra-ISP-789f / normal_annihilator。  
AI-assisted，GPT-6 Astra Pro。


> **首版已实际失败，不能据此声称预基主块为 $I_{3333}$。** run 43731615668、step full-infinity-original-dual27-through21，execution source 6855eb1f8c715681dd45312fc17f6d86de6e17ab：全部4433原系数通过、native编译成功，但在 all3333 original prebasis pivot products 断言处退出1，尚无jet ledger。本文件保留首次入口历史；有效后继为 [完整自然三角尾 v2 接口](2026-11-15-r150-full-infinity-natural-dual-schur-v2-interface-789f.md)，它实际核单位三角结构并在正向及转置两侧保留全部低次数尾。下面原先的单位阵前提不得用于数学结论。

## 1. 首版历史状态与输入范围

本文件冻结新的可执行接口与代数证明，不记载尚未发生的数值结果。代码未在本地编译、运行；主线程将在实际 Actions 中解析、编译并执行。旧会话结束后的临时数组不可续用，本入口从仍可定位的六件历史输入独立恢复。

研究对象是同一原十七式、全部 $6188$ 个次数至多三的来源、全部 $4367$ 个次数一至五的输出，在真实自然无穷远参数 $u=1/s$ 下的矩阵

$$
A(u)\in\mathbb F_{31}[u]^{4367\times6188}.
$$

对 N 的线性部分反转至权十，对 N 的二次部分保为常项，对六条 Gamma 的二次部分反转至权五。原 primitive 整数模型的全部 $4433$ 个参数系数先与冻结 native 模型逐项比较；所有十七行原固定尺度与公共分母均在 $31$ 处为单位。因此本入口不使用共动一阶矩阵代替原自然矩阵。

最小历史身份见 [输入清单](2026-11-15-r150-full-infinity-dual27-minimal-input-locations-789f.json)。新原数据只有同一 native 模型、预基 forward/backward、旧 full1007 operations、旧 full first-jet receipt 与 primitive 模型。它不恢复 selected985 来源 DAG、kernel36、任意旧 p 进位来源或旧多项式正常形输出。恢复仅在当前 job 临时执行，逐件核 stored 与 raw SHA256。

另读取两份小文本：已完成同选 $B$ 的 $243/21$ 回执，以及 [原泛参数十三核定理](../results/R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md)。两份均锁全文字节与 SHA。

## 2. 完整常数单位块及其转置

原预基有 $3333$ 列，旧 full source DAG 给出另外 $1007$ 列。完整记录包含全部 $2855$ 个非预基来源的 I/R/B/Z 事件。native 逐事件核原来源编号、已经存在的主元、系数、全部操作计数，并核后续 J/P/Q/C/0 审计记录；它不重算旧第一连接。

首版曾要求预基重放后的全部 $3333^2$ 主分量为单位阵；这一要求已在实跑中失败，不能作为已证身份。每个新 full 基列按真实原 $A_0$ 列先减预基，再沿其 I/R/B 来源轨迹消去；实际核其 leading component 与原 receipt 的非零主元系数。这些 full 基列未统一归一，转置回代保留除以该真实主元的步骤。

记实际得到的原单位输出集为 $I_0$，原单位来源集为 $J_0$，大小均为 $4340$。剩余原输出集 $F_0$ 大小 $27$，剩余原来源集 $T_0$ 大小 $1848$。三者均在临时完整 native receipt 中保存，不用相同数量代替同一字典。

令

$$
W=\iota_{J_0}\bigl(A_0[I_0,J_0]\bigr)^{-1}\pi_{I_0}.
$$

native 通过既有来源 DAG 的转置作用计算 $W^T$，未分配 $4340$ 阶新逆矩阵，也未作大 Gaussian 消元。具体顺序为：原预基 F/B 正向作用、减原 full 列的预基坐标、full 来源 DAG 正向作用、full 图像三角消元的转置回代、预基正规余项的转置回代。所有复用对象都是同一原常数矩阵上的实际来源操作。

初始二十七列为

$$
L_0=\iota_{F_0}-W^TA_0^T\iota_{F_0}.
$$

它们在 $F_0$ 上的坐标严格为单位阵；native 随后实际核全部

$$
A_0^TL_0=0
$$

的 $6188\times27$ 个坐标。连同真实单位块给出的下界，得到本次实际常秩恰为 $4340$。本接口不会仅凭旧 receipt 中的秩数字跳过这一检查。

## 3. 原自然 u 的完整递推

固定自由输出坐标，定义

$$
L_k=-W^T\sum_{a=1}^{\min(10,k)}A_a^TL_{k-a},
\qquad k\ge1.
$$

每一阶的完整残量是

$$
R_k=A_0^TL_k+
\sum_{a=1}^{\min(10,k)}A_a^TL_{k-a}.
$$

native 实际核 $R_k$ 在全部 $4340$ 个原单位来源上为零，并保存全部 $6188\times27$ 个坐标。剩余 $1848\times27$ 矩阵记为 $S_k$。高阶 $L_k$ 的全部二十七个自由输出坐标严格为零。

形式上，这一构造正是

$$
L(u)=\iota_{F_0}
-\iota_{I_0}
  \bigl(A(u)[I_0,J_0]^T\bigr)^{-1}
  A(u)[F_0,J_0]^T,
$$

$$
A(u)^TL(u)\big|_{J_0}=0,\qquad
S(u)=A(u)^TL(u)\big|_{T_0}.
$$

因 $A_0[I_0,J_0]$ 是单位，所写形式逆存在。每一阶都保原完整来源，不将 $1848$ 行再投影到一个未经付费的有限行族。

## 4. 为什么完整度数 21 足够

已付同选原方阵 $B(u)=A(u)[I,J]$ 在 $\mathbb F_{31}[[u]]$ 的全部正 Smith 指数最大为 $21$、总和为 $243$。同一 $B$ 在函数域可逆，故 $\pi_I$ 在 $\operatorname{im}A\otimes\mathbb F_{31}((u))$ 上单射。

若 $\operatorname{coker}A$ 的一个扭类由 $x$ 代表且在 $\operatorname{coker}A_I$ 中为零，则 $x_I=(Ay)_I$。扭性给 $x-Ay$ 属于上述函数域像，而其 $I$ 坐标为零；单射迫 $x=Ay$。所以

$$
\operatorname{tors}\operatorname{coker}A
\hookrightarrow\operatorname{coker}A_I.
$$

原来源包含 $J$ 又给出

$$
\operatorname{coker}B\twoheadrightarrow
\operatorname{coker}A_I.
$$

因此 full 的每个正 Smith 指数均至多 $21$，总长度至多 $243$。这是同一原矩阵的子商论证，未从仿射 $s=0$ 的长度搬到无穷远。

[原泛参数十三核定理](../results/R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md) 给出原整系数模型所有 $4355$ 阶子式恒零。它们约化模 $31$ 仍零；同选 $B$ 的非零性给相反下界。因此 full 的函数域秩恰为 $4354$，常数单位消去后 $S(u)$ 的函数域秩恰为 $14$。二十七个原输出方向中有十四个正指数和十三个真正的形式自由方向。

wrapper 对全部 $1848$ 行作小单位 Schur 递推。每次实际选取常数单位子式，保原行、原列标签，逐系数核单位逆乘积；不能删除未达到截止深度的正方向。系数 $0,\ldots,21$ 全保后，必须付清十四个正指数。若没有付清，或付清后已知的剩余小矩阵仍有非零系数，入口判失败，不预填完整性。实际第一个指数层的秩还须等于旧 full 第一连接已付的四。

## 5. 原十三维 formal kernel mapper

小 Schur 消去保留每个实际主元的原 $1848$ 行标签和原二十七列标签。设最终实际选出的十四行、十四列为 $R,C$，剩余十三列为 $F$。保存常项 graph $N_0$，实际核 $N_0[F,:]=I_{13}$。

完整形式 mapper 为

$$
N(u)=\iota_F-\iota_C S(u)[R,C]^{-1}S(u)[R,F],
\qquad
K(u)=L(u)N(u).
$$

这不是直接假定带 $u$ 分母的表达式正则：每次实际单位 Schur 的右 graph 是幂级数且自由块为单位，其合成正是 $N(u)$，所以该表达式属于 $\mathbb F_{31}[[u]]$。实际十四主元子式非零，加上已付函数域上界十四，迫其余完整形式 Schur 为零，故

$$
A(u)^TK(u)=0,\qquad
K(u)[F_0[F],:]=I_{13}.
$$

wrapper 另将 $K_0=L_0N_0$ 落回全部 $4367$ 个原输出坐标，实际乘原 $A_0^T$，核 $6188\times13=80444$ 个坐标为零，核其十三个原自由坐标为单位阵。完整原字典、实际十四行列子式、$N_0$、原 $K_0$ 和形式 mapper 公式均临时保存。

这里的全形式身份由真实单位 Schur 与已付泛秩定理证明；回执明确将“更高 kernel 系数已全部数值乘回”设为否。已有 $L_0,\ldots,L_{21}$ 的全部原 residual 则确由本轮逐阶计算。二者不混为同一种数值验证，也不称已经生成十三条新的特征零有理函数核。

## 6. 检查点、预算和 CLI

native：
[full dual Schur C++](2026-11-15-r150-full-infinity-natural-dual-schur-789f.cpp)，
$20205$ B，SHA256

$$
\mathtt{33b6d1edd33d152f862fc123dc3e9baf6a7b75098bdf0c297b2759e0ca8ff675}.
$$

runner：
[full dual Schur runner](2026-11-15-r150-full-infinity-natural-dual-schur-runner-789f.py)，
$26503$ B，SHA256

$$
\mathtt{557db708b6f9e568374bcc46ffe81d437b0ac5b7af8392041960065facbc13fc}.
$$

native 只依赖已经冻结的 common 与 bitplane 两个头，不需要安装 FLINT 开发头；小 Smith 使用 Python-flint。编译限 $30$ 秒，初始共享数学预算 $180$ 秒、内存 $1024$ MiB。若时间到，最后完整阶保留，可同 out 同源续接。

每一阶将原 cochain、全部原 residual 与小 Schur 分别写完整临时文件，核 SHA256 后才原子提交 ledger。恢复时核同语义 binding、每个完整文件的 SHA、尺寸、原自由坐标和连续阶数。binding 不含恢复目录、请求预算或截止度数。小 Smith 也保完整中间矩阵与 mapper；扩展 native 精度时只重新执行受扩展系数影响的小 Schur，不重复已完成原 jet。

建议命令：

~~~text
python {scripts}/2026-11-15-r150-full-infinity-natural-dual-schur-runner-789f.py
  --native-model {native_model}
  --forward {forward}
  --backward {backward}
  --full-operations {full_operations}
  --paid-full-receipt {full_receipt}
  --primitive-equations {primitive}
  --paid-selected-summary {scripts}/43702348535-selected-natural-u-minimal-rebuild32.json
  --generic-rank-proof {scripts}/R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md
  --native-source {scripts}/2026-11-15-r150-full-infinity-natural-dual-schur-789f.cpp
  --out {work}/full-infinity-natural-dual-schur
  --seconds 180 --memory-mib 1024 --compile-seconds 30 --maximum-degree 21
~~~

头文件与 native 放同一 scripts 目录：

- common：$11284$ B，SHA256 $\mathtt{f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1}$；
- bitplane：$3030$ B，SHA256 $\mathtt{73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec}$。

主回执为 `full-infinity-natural-dual-schur-receipt.json`。完成 outcome 为 `complete-full-original-infinity-field-smith`；正常时间前缀为 `checkpointed-full-original-dual-jets`。只有真实十四指数、小余量、十三 mapper 和全部原门槛均通过才置 `completeFullInfinitySmithLengthComputed=true`。

所有大数据只在当前 job 临时存在。Git 仅保存源码、参数、真实 run、小回执和 SHA。此次 F31 完整 Smith 即使成功，也不会自动设置特征零 Smith 已完成或 selected leading coefficient 为 $31$ 单位。
