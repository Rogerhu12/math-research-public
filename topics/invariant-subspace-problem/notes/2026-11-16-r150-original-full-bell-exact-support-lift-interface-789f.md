# 完整原 Bell 非零理想：实际有限域来源的特征零支撑提升

作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

本消费者接在完整原 Bell 齐次次数入口之后，保留全部六个均值变量和十一个 Hankel 变量。它只读取同一临时 job 中已实际保存的原模型和有限域正来源。当前仅完成源码静态复核；共享执行环境离线，尚未实际 AST 或数学运行。有限域正来源尚未出现时，本程序明确返回“没有可消费的正来源”前缀，不产生特征零结论。

## 1. 原环、完整来源和本次目标

沿用未改动的原物理模型 helper，固定
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336).
$$
令 $x=(y_0,\ldots,y_5,H_0,\ldots,H_{10})$。原十七条梯度记为 $F_1,\ldots,F_{17}$，原 matched Bell 多项式记为 $b$。消费的是
$$
(F_1,\ldots,F_{17},b-1)\subset E[x]
$$
的完整十八标签来源。系数域的 $127,d=100$ place 仅用于挑选有限的 source monomial 支撑和一个非零 $E$ 子式；不会取值任何 $y,H$，不会把有限域 $1$ 身份直接提升为特征零。

父入口必须是本文锁定版本，包含独立 $(x^2-\tau^2,x\tau)$ 的二阶前缀、原来源续接三阶和非平凡 $\tau^3$ 乘回门。消费者重新核父语义 binding、原模型与正来源的压缩及逻辑 SHA，使用原模型中保存的全部 $E$ 系数。

## 2. 有限支撑与全部原单项式行

假设父入口实际付过
$$
1=\sum_{i=1}^{18}\bar A_i\bar F_i
$$
在 $\mathbb F_{127}[x]$ 中成立，其中 $\bar F_{18}=\bar b-1$。对每个 $\bar A_i$ 中的每个非零 monomial $m$ 设置一个未知 $a_{i,m}\in E$。这只是一个候选来源空间；不声称它包含原理想的所有来源。

程序从完整原 $E$ 生成元构建每个 $mF_i$，取全部出现的十七变量 monomial 行及常数行，得到
$$
A_E a=e_1.
$$
即使某个原 $E$ 行在 place 约化后恰好为零，该行也保留。原十八标签、单项式指数和来源权界逐项核验。程序先核父有限域来源向量在这份补全原行后的系统中仍满足 $\bar A\bar a=e_1$。

对 $\bar A$ 做精确有限域 RREF，只选择 $r$ 个独立原来源列和 $r$ 个原输出行，得到非零子式 $\bar U$；同时实际核所选列的完整有限域来源仍给全部行的 $e_1$。因此对应的原 $E$ 方块 $U$ 可逆。该事实不给 $A_E$ 的秩上界；后续绝不据此删除未选原输出行。

完整原 support profile 先保存。默认门为来源项数不超过 2048、完整矩阵项数不超过 20000000、原 $E$ 单位阶数不超过 512。超过资源门只保留准确前缀，允许同源同 out 提高资源门后继续；不称来源不存在。

## 3. 原 $E$ 单位与完整解先存

将 $E$ 按基 $(1,d,d^2)$ 作正规表示，$r\times r$ 单位系统化为原有理 $3r\times3r$ 系统。定义三次式逐项使用原整数系数除以 3725，乘法矩阵逐项按 $d^3$ 关系约化。

单位阶段在独立子进程中调用 python-flint 的精确 Dixon solve。全部 $3r$ 个有理解坐标先原样保存，然后才乘回全部正规表示单位行。父进程在数学预算到达时终止该子进程；若完整解已落盘，后续读取它继续，不再求同一单位。若还没有完整解，单位内部进度不可恢复，不能把此阶段描述为逐位 Dixon checkpoint。

保存的解绑定完整原单位输入 SHA。即使单位小回执未完成，父消费者仍可使用已完整保存的候选，但必须通过下一节全部原多项式乘回；不会把候选文件存在或单位行成立当作正结论。

## 4. 唯一特征零正结论门

把所选列解回填到原十八来源多项式，其余候选来源坐标设为零。保留全部
$$
A_i=A_{i,0}+dA_{i,1}+d^2A_{i,2}.
$$
以原十七条 $F_i$ 和原三个 Bell 系数分量，实际计算
$$
\sum_{i=1}^{17}A_iF_i+A_{18}(b-1)-1
$$
在 $E[x]$ 的三个完整有理多项式分量。每个分量都保留全部十七变量及全部单项式；没有选行、点值或截断。只有三个多项式逐项全零，才写入
~~~
characteristicZeroOriginalIdentityVerified = true
~~~
并保存完整十八项原 $E$ 来源。

三个分量各自完成后保存准确通过标志，下一调用复用先前已验证的完整分量。如果某分量非零，保存其完整原剩余多项式和 SHA，结论仅为“当前所选有限域来源截面没有升起”。不由此推断原理想非成员，不否定同支撑内其他截面或更大支撑的可能来源。

这一步若成功，则在原 $E[x]$ 中严格有 $1\in(F_1,\ldots,F_{17},b-1)$。所有参数分母均为零；解的分母只是固定数域 $E$ 中的常数。原 $Z$ Schur 消去和原全 33 梯度的双向来源沿用原模型已付恒等式，不另作参数点或秩分支假设。

## 5. 同一真身份产生原 Bell 幂来源

设父齐次正列为 $\tau^k$；实际候选支撑的每项都满足
$$
\operatorname{wt}(A_i)\le k-w_i,\qquad
\operatorname{wt}(A_{18})\le k-3,
$$
其中原权是 $\operatorname{wt}y=1,\operatorname{wt}H=2$，$w_i$ 为相应原梯度权。完整特征零身份通过后，将其齐次化：
$$
\tau^k=\sum_{i=1}^{17}F_i A_i^h+
(b-\tau^3)A_{18}^h.
$$
置 $n=\lceil k/3\rceil$，再乘 $\tau^{3n-k}$。环
$$
E[x][\tau]/(\tau^3-b)
$$
在 $E[x]$ 上有自由基 $1,\tau,\tau^2$。取常项严格给出
$$
b^n=\sum_{i=1}^{17}F_i S_i.
$$
若 $c\,m$ 是 $A_i$ 的一项，只有
$$
3n-w_i-\operatorname{wt}(m)\equiv0\pmod3
$$
时贡献 $S_i$，贡献恰为
$$
c\,m\,b^{(3n-w_i-\operatorname{wt}(m))/3}.
$$
这些非负整数幂和完整 $E$ 系数逐项保存为来源直线程序。该推论由已完整验证的原身份和单首项多项式除法推出，不需要把巨大的 $b^n$ 另外展开。输出明确记录 expandedBellPowerProductSeparatelyComputed=false；不把代数推导冒称第二次大多项式乘回。

因此实际正结果同时支付原归一理想的 $1$ 来源，以及原梯度理想中的明确 Bell 幂来源。若前三个完整原乘回尚未成功，本节不产生结果。

## 6. 源码与 inputs

| 项 | 完整 blob | 字节 | SHA256 |
|---|---|---:|---|
| 新 $E$ consumer | 6aa939b35d07aa9599635089152f5339cf49bff9 | 26209 | c9ea32d71c00a874d79bef49fd6c3b27236e68d7afe70d94289746a9c5ceed25 |
| 冻结 field driver | c5e81e3e97d0123df214a994667c5b046171ec82 | 31156 | da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d |
| 原 physical helper | 7e5244c7c9177d483bb2dbe2a1dc7a2dc86904a3 | 16964 | 31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10 |
| 本 inputs | ba6fe0f41a69f7f2d702cec66d78fad85303b261 | 3714 | 07cbfe944a25eeda2c089658f411dd0693143b67aa65b2fef1009aafe973a582 |

源路径分别为：

- notes/2026-11-16-r150-original-full-bell-exact-support-lift-789f.py；
- notes/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py；
- notes/2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py。

本 inputs 路径为 notes/2026-11-16-r150-original-full-bell-exact-support-lift-inputs-789f.json。historicalInputs=[]；三个小源码之外只消费同 job 当前生成的原 field 模型及候选，不恢复旧大数组。

## 7. 同 job 级次、CLI 与预算

先用冻结 field driver 运行实际双 degree 自测和完整原权 5 至 9。建议该阶段 600 秒、4 GiB、外墙 660 秒；这是预算参数调整，不改变父语义 binding。然后无论是否出现正列，都可运行以下 $E$ 消费者；没有候选时它准确返回 completed-prefix。

~~~
python {scripts}/2026-11-16-r150-original-full-bell-exact-support-lift-789f.py \
  --field-driver {scripts}/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py \
  --helper {scripts}/2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py \
  --field-out {work}/original-full-bell-homogeneous-source-prefix \
  --out {work}/original-full-bell-exact-support-lift \
  --seconds 600 --memory-mib 4096 \
  --max-unit-rank 512 --max-support 2048 --max-profile-elements 20000000
~~~

$E$ 阶段首轮建议 600 秒、4 GiB、外墙 660 秒。同 job 首轮 field 加 $E$ 合计预留 24 分钟（另加安装/原模型和工作流余量）；不得把不同 job 的旧 tmp 视为存活。预算可续时，同源码、同 out、同 binding 复用原已成 profile/单位输入/完整解/原分量验证。提高资源门不变数学输入；源码改动须换 out。

代码不调用 Singular，不安装依赖；依赖 Python 3 和 python-flint 0.9.0。精确 API 参照 [python-flint 有理矩阵文档](https://python-flint.readthedocs.io/en/latest/fmpq_mat.html) 的 solve 与 [有限域矩阵文档](https://python-flint.readthedocs.io/en/latest/nmod_mat.html) 的 rref/solve；实际仍由所有原门验证。

## 8. 失败、输出与存储范围

数学预算中断为 exit75，记录 parameters.error 和原诊断。单位候选没完成、完整支撑过大、profile 或单位阶超过当前资源门都不称数学否定。完整候选提升失败是一个已验证非零剩余结果，不再在同源续接时重复单位解和同一原乘回。

临时输出包括完整 support profile、原 $E$ 单位、全有理解、已验证分量、可能的完整非零剩余，或真原十八来源与 Bell 幂 SLP。每件有压缩/逻辑双 SHA；小回执保存真实时长、父/子峰值 RSS、原输入 binding 和完成范围。这里没有新永久数学数组：仓库只收源码、参数、证明、执行身份及输出 SHA，遵守根规则15。
