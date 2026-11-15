# 已付二十九条原 Koszul 曲线的一阶外来源：精确有理小入口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15。

状态：代码已在恢复的本地执行环境完成 Python AST 语法检查；未运行本次数学。下面的 $r$、$t_2$ 必须由实际新回执确定，不能预填成秩或新增阶。

## 1. 固定曲线与原来源身份

保持原自然齐次化的十七个 primitive 多项式 $F_i^h(u,m)$、原 $6188$ 个来源坐标与原选列 $J$。对于每一对 $i<j$ 以及 $h\in\{1,m_0,\ldots,m_{10}\}$，取真实来源曲线

$$
\phi_{ijh}(u)=h\bigl(F_j^h(u,m)e_i-F_i^h(u,m)e_j\bigr).
$$

按 $i<j$ 的字典序、每对依次 $1,m_0,\ldots,m_{10}$，这些列组成

$$
\Phi(u)\in\mathbb Z[u]^{6188\times1632},\qquad
A^h(u)\Phi(u)=0
$$

的精确原式恒等式。来源乘子次数至多三，没有新分母或负 $u$ 幂。

既有 exact-support 计算已经给出二十九条 $1632$ 维 primitive 整数列，组成 $X$，满足

$$
(\Phi_0X)_{J^c}=0,\qquad
\operatorname{rank}_{\mathbb Q}\Phi_0X=29.
$$

这里使用真实整数来源系数文件 exact-koszul-source-coefficient-basis.json.gz，没有把当时模 $31$ 的来源图当成有理图。原二十九列的完整 $6188$ 坐标 SHA、全部 $4367$ 原整数产品及三十六个自由坐标的秩，均已实际付清。

## 2. 唯一新的矩阵

展开 $\Phi(u)=\Phi_0+u\Phi_1+\cdots$。只计算

$$
M=(\Phi_1X)_{J^c}\in\mathbb Z^{1834\times29}.
\tag{2.1}
$$

$F_0,F_1$ 直接取本次已完成的自然参数第一连接输入：$N$ 的 $L_{10},L_9$，$\Gamma$ 的 $\Gamma_5,\Gamma_4$，所有 primitive 常数与原参数字段已核。没有用共动的 $P_1$ 替换自然导数。

入口实际完成下述来源检验后，才计算 (2.1) 的有理核：

- 重建全部 $\Phi_0$，与旧原模型的每个非零来源系数逐项相等；
- 重新组合 $\Phi_0X$，按列核对全部 $6188$ 坐标的旧已付 SHA；
- 全部 $1834$ 个常数外来源为零，全部三十六个自由来源与已付独立像逐项相等；
- 新构造 $\Phi_1X$ 后，实际核全部原输出恒等式
  $A_0\Phi_1X+A_1\Phi_0X=0_{4367\times29}$。

这些是对新自然来源曲线的完整接线，不重做原 $1603$ 方块的有理解、旧大正常形或 Dixon 数字。

## 3. 精确核给出二阶支撑的足够子空间

若实际有理秩为

$$
r=\operatorname{rank}_{\mathbb Q}M,\qquad t_2=29-r,
$$

取完整核 $H\in\mathbb Z^{29\times t_2}$，各列只作非零有理归一并清分母。入口要求

$$
MH=0
$$

在原全部 $1834$ 行上准确成立，并保存其非零对角自由坐标块，支付列独立性。

因此曲线 $\Phi(u)XH$ 是精确原核，常项仍有秩 $t_2$，且

$$
(\Phi(u)XH)_{J^c}=O(u^2).
$$

其他已付曲线的外来源至少为 $O(u)$。故本次实际值若完成，将给出固定二十九维曲线空间中的滤过

$$
\dim F_1=29,\qquad \dim F_2=t_2.
$$

**范围：**这是固定常系数组合 $XH$ 的完整核。没有允许额外加入 $u\Phi(u)Y$ 去校正外一阶项，也没有计算整个原核模的最大二阶支撑。因此 maximumSecondOrderSourceSpaceComputed=false 始终保留。

## 4. 可接到原子式的来源因子

在完整 Smith 分解的 active 来源矩阵 $E(u)$ 中，每条真实原核曲线满足

$$
E_J(u)\kappa_J(u)=-E_{J^c}(u)\kappa_{J^c}(u).
$$

二十九个常项在原 $J$ 中独立，故将这二十九条 $J$ 内来源补成一个解析可逆列基后，$t_2$ 列的 active 产品被 $u^2$ 整除，其余 $29-t_2$ 列被 $u$ 整除。总来源因子阶至少

$$
g=29+t_2.
$$

任意少一列的 minor 由外积或 Cauchy–Binet 展开得到至少

$$
g-\ell_{\max},\qquad
\ell_{\max}=
\begin{cases}
1,&t_2=0,\\
2,&t_2>0.
\end{cases}
$$

这个论证支付了删除一个来源时可能同时影响常数和一阶的情况，不把两项来源约束免费合并成一项。若另有已付完整矩阵 Smith 下界 $\delta_n,\delta_{n-1}$，才能进一步加上它们得到同选原子式、原来源单列替换及 cofactor 的阶。本程序只记录 $g$ 和 $g-\ell_{\max}$，不在代码里假定后来可能更新的完整 Smith 值。

## 5. 具体入口与六个已成输入

~~~
python -B {scripts}/2026-11-15-r150-koszul-curve-first-outside-789f.py
  --support-dir {work}/koszul-exact-rational-support
  --source-model {work}/koszul-exact-sparse-preparation/exact-original-koszul-outside-model.json.gz
  --first-dir {work}/selected-natural-first-connection-f31
  --out {work}/koszul-curve-first-outside
  --seconds 30
  --memory-mib 512
~~~

仅用标准 Python 与已安装 python-flint，没有编译、新库、网络下载或新参数素数。

输入六文件的完整 bytes/SHA 固定在源码：

| 文件 | 字节数 |
| --- | ---: |
| 原 Koszul 来源模型 | 814572 |
| 二十九列真实整数系数基 | 1670175 |
| 已付三十六自由像 | 29488 |
| exact-support 原完整回执 | 18271 |
| 已付自然 $F_0,F_1$ 整系数缓存 | 20582 |
| 本次自然第一连接原完整回执 | 15594 |

真实绑定分别为旧支持构造的 10890e55…48cc6a4 和自然一阶实绩的 479d3295…f5dac31；源码中保存全长，不用摘要值代校验。

## 6. 有界求解和可恢复实际边界

主进程共享三十秒预算、每进程 $512$ MiB。先构造并保存全部原 $M$ 及来源检验回执，再启动独立有界 worker 计算只有二十九列的精确有理 RREF。worker 逐行 content 缩放只作非零有理标量，结果最终仍乘回未缩放的原全部 $1834$ 行。

worker 在完整原乘回之前先保存精确核系数。如果小核阶段达到预算，下一次直接复用已完成的 $M$ 与来源身份；若 exact 核已经保存但原乘回未完，则仅续该原乘回，不重新做 RREF。所有实际中断状态均为 budget-exhausted，不会当成秩否定。

主小回执：

~~~
koszul-curve-first-outside-receipt.json
~~~

完成字段为：

- outsideFirstRankOverQ；
- fixedConstantCombinationSecondOrderDimension；
- all29PaidConstantSourcesMatched；
- all4367ExactFirstSyzygyProductsZero；
- all1834ExactOutsideKernelProductsZero；
- completeKernelOfThisFixedOutsideMatrixComputed；
- allSecondOrderConstantHeadsIndependent。

来源矩阵、完整小核及中断工作文件均只留 job 临时目录。长期只保存源码、参数、真实小回执与完整 SHA；不上传可重算的大结果。
