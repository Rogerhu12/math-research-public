# 原六均值的首层三十条乘法关系：完整权七来源接口

作者：Astra-ISP-789f / normal_annihilator，与 /root；AI-assisted GPT-6 Astra Pro。

## 1. 本步的实际对象与边界

本入口在已付合法固定系数映射 $E\to\mathbb F_{127}$、$d\mapsto100$ 上工作。全部十二个 $y,w$ 参数仍为多项式变量，原五个 $u$ 变量仍保留在来源系数中。它只构造、筛选三十条真正的原来源关系，不计算整个稳定闭包，不宣称 $1$ 属原理想，也不把有限域选元提升为特征零选元。

父模型是已付十生成元向量

$$m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4)^{\mathsf T},$$

以及五个完整参数矩阵 $N_i$、五个完整原来源矩阵 $S_i$、六条均值关系 $Y_j$。把原十八个生成元（五个 $u$ 梯度、六个 $w$ 梯度、六个 $y$ 梯度与 $b-1$）记为列 $A$。原已验证身份为

$$m^{\mathsf T}N_i=u_i m^{\mathsf T}-A^{\mathsf T}S_i,
\qquad m^{\mathsf T}Y_j=A^{\mathsf T}\sigma_j.$$

因此每个 $0\le i<5$、$0\le j<6$ 的新列

$$V_{ij}=N_iY_j,\qquad
\tau_{ij}=u_i\sigma_j-S_iY_j$$

都满足完整原来源身份

$$m^{\mathsf T}V_{ij}=A^{\mathsf T}\tau_{ij}.$$

本程序重新逐项核全部五十条原乘法列身份、二十六条所用父种子原来源、三十条新列的完整十八生成元乘回。已付原十七梯度的 Jacobian 运输保持在同一精确父模型中，没有另选常数或参数图。

## 2. 完整权七字典

参数权为 $\operatorname{wt}(y)=1$、$\operatorname{wt}(w)=2$，十个模生成元权为 $(0,2^5,4^4)$。六均值列权五，已付保留的二十条低权交换子列权六，所以全部三十个 $V_{ij}$ 恰为权七。

记 $B_d$ 为十二参数的完整权 $d$ 单项式集合。实际使用

$$|B_1|=6,\quad |B_2|=27,\quad |B_3|=92,
\quad |B_5|=714,\quad |B_7|=3816.$$

全部输出数为

$$3816+5\cdot714+4\cdot92=7754.$$

原输入按固定顺序为：

1. 六条均值各乘全部 $B_2$，共 162 列；
2. 已付实际二十条权六交换子各乘全部 $B_1$，共 120 列；
3. 按 $(i,j)$ 字典序排列的三十个 $V_{ij}$。

所以前缀为 282 列，完整矩阵为 $7754\times312$。每个输出指数、原种子编号、乘子单项式及新列标签全部保存在同一哈希字典；任何原非零单项式不落在该字典就失败。没有行采样、参数代入或高次数删项。

该前缀只作为一种保守的已知来源集合。它没有声称穷尽原五十列子模的权七部分；例如 Bell 列不用于这个齐次筛选。即使一条新列被保留，也不能据此称它在原完整五十列子模中独立。

## 3. 可复用的真实原行算术

直接复用已审核的 `original-parameter-seed-compression-rank127` native 及原七位面 F127 头文件，逐字不改。输入原协议记录完整 7754 输出、312 输入、原目标起点 282 和新的语义 binding；其既有范围上限 20000/2000 包含本步真实尺寸。

native 先做原完整 F127 算术检查及 25 个独立普通标量小矩阵产品，再按固定输入顺序消元。每个完成的依赖式保留原目标系数严格 1、只用较早原输入的完整 312 系数。每个预算退出保留完整已处理原行及其真实来源；未完成整行不计入结果。

消费者逐新列读取关系，实际验证完整十参数坐标相等，并将同一系数组合施于原十八来源，再做完整多项式乘回。只有这些门全部通过，才删除新列。

令 $L_0$ 是已付五十原列的参数子模，$K$ 是该次实际保留的新列集合。本步完全结束所能证明的等式恰为

$$L_0+\sum_{i,j}B\,N_iY_j
=L_0+\sum_{(i,j)\in K}B\,N_iY_j.$$

即使 $K=\varnothing$，也只说明本组三十列已有上述原来源表达，不说明五个 $N_i$ 对 $L_0$ 全部稳定。即使 $K\ne\varnothing$，也不声称左侧严格大于 $L_0$。后继若把保留列加入候选正门，仍须真实求得 $e_0$ 的参数来源并完成原十、十八、十七加 Bell 的乘回；本步不替代该正门。

## 4. 精确输入与来源身份

主源码：

~~~text
notes/2026-11-16-r150-original-mean-first-frontier127-789f.py
Git blob 049028bbcfa486e8335d589c203d7cf682c4d7ac
18470 bytes
SHA256 810904a2c797b08493ed377c069abd75018e0a0df8035cb700baad80616bea1e
~~~

所有 helper 的完整 path/blob/bytes/SHA、父 binding、原物理 manifest pin 和完整数学压缩 pin 记于同名 `inputs-789f.json`。父模型与压缩必须是当前可访问、真实完成的同源产物。先验证全部父文件及原来源，才能采用父已付关系；不能把过期临时目录当作仍存在。

必须使用 Python 3.12.14、python-flint 0.9.0，以保持已锁 gzip 物理字节；不能将 Python 3.14 的 header 差异通过放宽输入 SHA 规避。native 使用 `g++ -std=c++17 -O3`。本步不依赖 Singular。

完整 CLI：

~~~text
python notes/2026-11-16-r150-original-mean-first-frontier127-789f.py
  --model-source {scripts}/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py
  --model-out {work}/original-ten-parameter-module127-v2
  --compression-source {scripts}/2026-11-16-r150-original-parameter-seed-compression127-789f.py
  --compression-out {work}/original-parameter-seed-compression127
  --native-source {scripts}/2026-11-16-r150-original-parameter-seed-compression-rank127-789f.cpp
  --header {scripts}/2026-11-15-r150-original-f127-bitplane-789f.hpp
  --out {work}/original-mean-first-frontier127
  --through final --seconds 180 --memory-mib 768
~~~

外层预算 240 秒；`--through prepare` 只完成三十新来源和完整输入，不做 native 秩结论。相同源码、参数、父文件、输出目录和 binding 可继续真实完整阶段；各新列和来源验证分别事务保存。预算 exit 75 只说明已保存的整阶段前缀，任何算术或文件门失败按 exit 1 原样报告。

## 5. 原计算记录边界

本接口冻结时只完成源码语法检查，没有执行三十新列的数学计算。实际秩、保留数与耗时必须以后续真实回执为准。所有多项式数组、完整字典、native 状态和 raw 回执只留临时工作目录；仓库仅保存源码、参数、证明与实际运行身份/SHA。不得从本接口预填任何秩、独立性或全局判空结果。
