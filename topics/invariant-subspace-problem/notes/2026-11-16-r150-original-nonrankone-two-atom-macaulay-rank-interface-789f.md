# 非秩一两原子原全 Macaulay 矩阵的有界秩入口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。  
日期：2026-11-16 UTC。

本入口接续 [真十七梯度小门](2026-11-16-r150-original-nonrankone-two-atom-gradient-interface-789f.md)。保全部原来源、原单项式与常数行比例；没有复用秩一 normal-form 字典。源码不预填秩，满秩与未满秩有不同的明确完成门。

冻结代码已经本地真实 AST、编译及有界运行。具体数学结论另见正式结果稿与执行身份；本文说明可重现协议及其量词。

## 1. 原模型必须重新核到同一逻辑 SHA

旧小 job 结束后不假定临时数组仍在。wrapper import 同一个已冻结生成器，重新运行全部原有理身份，并核完整 173045 B 逻辑模型：

~~~text
1f93dcd7db76f433df57536d4bd0b51417ae2a12137e08136141b4a9689a8d8d
~~~

包括十七个原偏导、11×11 真 minor、全部 N/Gamma 系数运输、56×11 原第三矩图及仿射来源表示。这个模型的原 paid binding 是

~~~text
2343a3e3f632236b0a5dc425f30a5f1ce27bfd10ff4add1d4c30c75ae692bcf9
~~~

同 out 续接时可以复用完全同逻辑 SHA 的临时模型。gzip 头可能随 Python 版本变化，故完成门核解压后的全部逻辑字节，不将不同压缩头冒充数学改变，也不假造旧压缩文件身份。

设原式与 primitive 整数式关系为

$$
F_i=\rho_i\widetilde F_i,\qquad i=0,\ldots,16.
$$

wrapper 再逐全部 1309 个非恒定坐标核这条有理身份，并逐 1309 个坐标核原式在 $127$ 的运输。每个 $\rho_i$ 的分子、分母均须为 $127$ 单位。不能先除去一个 $127$ 因子再称其为原同纤维矩阵。

## 2. 完整源与目标字典

固定十一个原平移变量 $m_0,\ldots,m_{10}$。来源是

$$
m^\alpha\widetilde F_i,\qquad |\alpha|\le3,\quad 0\le i\le16.
$$

乘子数为

$$
1+11+66+286=364,
$$

因此保全部 $17\cdot364=6188$ 行。顺序为乘子总次数、普通变量元组字典序，再依原方程 $i=0,\ldots,16$。

目标保全部次数一至五的普通单项式，数目

$$
11+66+286+1001+3003=4367.
$$

不含常数，因为小模型已经逐原式核其常项严格零。所有乘积的最高次数为五，没有被截断的原项。

native 输入只含同十七式的全部 $17\times77$ 个一、二次系数位置。native 自己生成全部乘子与目标字典；每个原乘积都必须落在完整目标表内。它不会接受已筛掉“零来源”的旧 2195 或 3333 列集合。

native 计算其 $6188\times4367$ 行表示；等价的来源线性映射具有 $4367$ 个目标行、$6188$ 个原来源列。

## 3. 原有限域秩与合法的特征零结论

固定素数为 $127$。使用已付七位面加乘实现，先执行全部独立标量算术检查，再实际核原 primitive 线性矩阵的模 $127$ 秩为十一。

每一原来源行从零重建，按最小非零原目标位置消元。新主元规范为一；每次消去后，首位置必须严格后移。完整尾部及全部 padding 位都保留。所选原来源编号、原目标主元、规范前主元值都存入临时完整 profile。

若最终秩为 $r$，这给同原有理有限矩阵的下界

$$
\operatorname{rank}_{\mathbb Q}\mathcal M\ge r.
$$

程序不由模 $127$ 未满秩推断特征零未满秩。

若且仅若实际 $r=4367$，选到一个真实原方块，其模 $127$ 行列式非零。因为全部原常数行比例都为单位，该方块给特征零满目标秩。于是每个 $m_j$ 已有原十七式的来源，来源乘子次数至多三：

$$
m_j=\sum_{i=0}^{16}a_{ij}(M)F_i(M),
\qquad \deg_Ma_{ij}\le3.
$$

所有 $F_i$ 的常项零，故固定均值下原理想准确等于 $(M)$。这是完整固定均值结论，强于先前仅在 $\det C(M)\ne0$ 的局部结论。

在原两原子参数图上使用同一原来源标签、同一目标表及固定常数 $\rho_i$，所选 minor 是一个仅依赖 $a,b,s,t$ 的非零多项式。局部化它后仍有上述有界来源，不再需要依赖 $M$ 的分母。这个参数 minor 仍不能被当作已付实际算子逆，或从一个非空参数开集推广到整个 Cat 秩二、三部分。

## 4. 未满秩时保留的是真有限矩阵余空间

若 $r<4367$，程序不会把它当作存在额外临界点的证明。它从完整规范行基按原目标次序反代完整 free-I 右核

$$
K\in\mathbb F_{127}^{4367\times(4367-r)}.
$$

必须核全部自由坐标单位矩阵及

$$
\mathcal M_{\rm rows}K=0
$$

的全部 $6188(4367-r)$ 个原坐标，才报告完整有限域余空间。

这只是当前完整次数五 Macaulay 矩阵的余空间；不是多项式理想全余模，也没有证明对更高参数乘法闭合。若要由此推全理想或真有理余空间，须有下一实际来源/闭包证书。

## 5. 真正可续的完整 checkpoint

三个阶段分别是：

1. 全部原来源行消元；
2. 完整 free-I 核反代；
3. 全部原来源乘回。

只在一整条原行、一个完整反代行或一条完整乘回行的安全边界提交。两个状态槽保存整个已规范行基、真实来源编号与主元值、阶段和 cursor；若已进入核阶段，同时保存全部核数组与已完成位置。原子 index 最后切换，指向完整槽。

绑定包含 wrapper、native、七位面 header、原模型 producer 的 SHA，完整 paid 模型 SHA，真实 native 输入 SHA，全部来源/目标字典 SHA 及协议版本。预算变化不改变数学绑定；源码或输入变化不能冒充同一 continuation。

恢复时重新核完整 basis 的首位置、规范主元、来源编号唯一性、全部自由坐标身份及准确 EOF。它不重新消已经完成的原行。

exit 75 只表示预算下的真前缀。不能要求下一任务依赖一个 exit 75 步骤“成功”；续接任务应只依赖原已成功输入，然后直接复用同 out、同源码与同 binding。

## 6. 预算、内存和输出

建议：

~~~text
--seconds 180 --memory-mib 2048 --compile-seconds 30
~~~

外墙 240 秒。七位面九个 coset 缓存的最坏基数组约 144 MiB；完整核即使按最大可能尺寸也约 19 MiB。这是按结构的上界估计，不冒充实测 RSS。不会分配旧多项式 NF 的多 GB 状态。

完整 CLI：

~~~text
python3 {scripts}/2026-11-16-r150-original-nonrankone-two-atom-macaulay-rank-789f.py
  --producer {scripts}/2026-11-16-r150-original-nonrankone-two-atom-gradient-789f.py
  --native-source {scripts}/2026-11-16-r150-original-nonrankone-two-atom-macaulay-rank-native-789f.cpp
  --header {scripts}/2026-11-15-r150-original-f127-bitplane-789f.hpp
  --out {work}/original-nonrankone-two-atom-macaulay-rank
  --seconds 180
  --memory-mib 2048
  --compile-seconds 30
~~~

完整参数与四个源 pin 见同名 inputs 文件。全 profile、kernel、两槽状态及原矩阵数据都只留临时目录。仓库按规则15只保存源码、参数、执行身份、输出 SHA 与正式证明。

异常既写入 parameters.error，也保实际 native 小回执和末个完整 checkpoint；不能将预算或进程失败写成数学负结论。本地执行与 Actions 执行在 manifest 中明确区分，不能给本地数学附一个不存在的 GitHub run。
