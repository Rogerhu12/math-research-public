# R868 原 P0 准确 socle 与五个254次扭转模块：公开执行契约

日期：2026-11-16。数学依据为 [R868 完整证明](../results/R868-original-P0-pole-generators-and-degree254-RR-certificate.md)。所有新矩阵、有限域秩、整数提升、有理重构和 K 运算只在公开 Actions 的独立 core 中执行。标准库 wrapper 只负责字节、来源、状态恢复与结果字段；不导入 core 或 flint。

## 1. 固定出口及边界

脚本 `R868_original_P0_socle_and_RR_modules.py`，数学结果名 `R868-original-P0-socle-and-degree254-RR-modules`，FINAL 为 `p41-original-P0-socle-and-RR-module-certificate.json`。CLI 为

```text
--config <expanded-job.json> --out <output> --budget-minutes <minutes>
```

首次只做一个真实 K 线性核，然后输出原两图 $I_{P_0}^{-254}$ 和五个 $\mathscr L_j I_{P_0}^{-254}$ 的准确模块来源。不求五个128维 RR 基，不求634维差分空间、一般 $\Gamma$、$M_g$ 或高度。

原 W 的34组、P0 的272个两图值、原点理想、R849 的五个极理想图都是已完成输入。首次不重算原 W、原三个 V1 共轭、Fourier 行、P0 值或旧理想。

## 2. 原数学来源与活跃运输分离

数学来源分五组 `R805/R806/R849/R856/R860`。每组绑定原 result、run、source commit、core SHA、manifest SHA、原 certificate、完整原 configuration 的 fingerprint 和本次选择文件的 bytes/SHA。路径只出现在 expanded job，不进入数学 tag。

- R860 直接读成功输出中的 W 系数来源索引。原 R806 的45件及原 R805 的7件从 R860 已成61件载体取出；原 R853 另外9件仍逐成员核验，但不假称本次会重用其数学。
- R856 直接读真实成功输出中的原 P0 两图值、点理想及 meta。没有重新使用 R837 点值算法。
- R849 原 source 身份不变，但不访问已到期的旧下载地址。其已成小图、meta、原 inventory/receipt 从仍活跃的继承载体取回。若载体还包着旧395MB opaque 全局输入，只在流式运输中逐原 SHA 核验；首次不把它加入新数学输入或新的最小输出载体。新 scope 并不执行原 U.1、五极理想或完整 GP 图的内部算术。

R849 的 `eta_degree_zero_fractional_ideal` 才是本次五个 $\mathscr L_j=\mathcal O(-Z_j)$。同一记录中的 `real_descent_degree_zero_fractional_ideal` 是另一原比较对象，不能替换。新模块图明确保存原 R849 节点、父配置、全部旧图叶身份以及原 p/q/η 负类号。

运输 API 的父子标签不能直接改名为新 producer；carrier 内原文件字节及 configuration 都保持。wrapper 对 parent 的完整 manifest 和选入成员核 SHA；若只做 Range 选择，就明确不声称重哈希了整个 ZIP。新输出最小载体只含本次实际选择的数学源与原 metadata。

## 3. 一次点矩阵：清列分母但准确恢复原尺度

读 R856 的 $z_0,w_0$，以 $d_z z_0=Z_0+Z_1\zeta$、$d_w w_0=W_0+W_1\zeta$ 为整数对。原 W 的第 j 列由已成 `coordinate_numerators/column_denominators` 给出，分母为 $d_j>0$；690个 S 行到正规行及 z 次数只读 R860 的原映射。

由于 $\deg W_{ij}\le1+\epsilon_j-\epsilon_i\le3$，先清列因子 $d_jd_z^3d_w$，再除该列全部两K坐标的正整数 content，得到整数 K 矩阵 H 与准确正有理列尺度 $\Delta_j$：

$$
W(z_0)-w_0I=H\operatorname{diag}(\Delta_j^{-1}).
\tag{868M.1}
$$

该尺度不能被模中心化。每8列是一个完成阶段；同时用原 P0 左评价向量准确核该8列的零关系。34组全部结束后给完整整数矩阵索引，旧已成组直接回用。

## 4. 一个实际子式，两个固定模逆

有限素数顺序从1000000753起，取 $p\equiv1\pmod3$ 的素数。先排掉原点分母、左评价分母及列尺度不为单位的 p。选该 p 上两个实际 $\zeta$ 根，对 H 分别约化。

第一嵌入上做一次 RREF 选271个主列，再对其转置选271行。只有**同一原行列集**在另一嵌入也为单位，才接受。两份非零模行列式已经证明原 K 子式非零；原 P0 左评价给秩上界271，因此不再求一份巨大的特征零行列式。

失败素数保存实测原因，继续有限序列；不把坏约化或本轮候选耗尽解释为特征零秩失败。成功行列集各在两嵌入求一个271阶模逆，逐项核左右两个乘积。以后每位只消费这两个原模逆，不能再做消元。

## 5. 一条两K坐标 Dixon 与准确完整乘回

令 k 为唯一自由原列。先设整数系统的 $u_k=1$，解271阶选行系统。写 $H=H_0+\zeta H_1$，其有理展开矩阵为

$$
\begin{pmatrix}H_0&-H_1\\H_1&H_0-H_1\end{pmatrix}.
\tag{868M.2}
$$

不求该542阶大逆；在两嵌入上分别用上一节固定逆求校正，再以两个根的差还原两Q坐标。当前状态保存 $x\bmod p^d$、$p^d$ 与准确整数余数 r，始终满足

$$
b-Mx=p^d r.
\tag{868M.3}
$$

每步由 $Md\equiv r\pmod p$ 得 $x\leftarrow x+p^d d$、$r\leftarrow(r-Md)/p$，准确整除后原子写 current 和小 digit receipt。硬断若恰在 current 写完而 receipt 之前，读回原完整 current 后补同一小 receipt；不重该已完成位。

每8位尝试一次严格矩形有理重构，界 $B=\lfloor\sqrt{(p^d-1)/2}\rfloor$ 满足 $2B^2<p^d$。542个Q坐标全恢复后，还须先准确验证选行系统，再补入自由1，核**全部272个K方程**。仅有重构成功、原模匹配或所选行回代都不够。

最后恢复原 normal 坐标

$$
h_i=\Delta_i u_i/\Delta_k,\qquad h_k=1.
\tag{868M.4}
$$

输出完整准确 h、两K有理坐标、原尺度、成功位数及544个零残差。不得把原模核或未展开的 adjugate 当作此准确向量。

## 6. 两图结果及实际复用

准确 $h_\sigma=\operatorname{diag}(v_0^{-\epsilon_i})h$ 只由同一个 h 运输；所有272条对角等式和重叠的次数至多2的多项式恒等式都准确核对。每图输出常 normal 分子向量、一次分母，以及

$$
I_{P_0,c}^{-254}=(1,f_c^{254}),\qquad
M_{j,c}=\mathfrak L_{j,c}(1,f_c^{254}).
\tag{868M.5}
$$

原第147个 $H^0(H+P_0)$ 截面是实际恢复的 $f_c$。254次函数幂可以保 DAG，不要求没有消费者的完整 normal 乘法表。两生成元完整性用曲线 DVR 的准确阶，重叠的255个冗余幂可按已给三角二项式运输；不声称已求出这些幂到两个端点幂的所有 Bézout 系数。

每个新理想节点保原 R849 的正确 p/q、原 $\eta$ 类号和同一两图嵌入。具体 theta、Poincaré、非 p 项及刚性化既不删除，也不被这次理想计算宣称完成。

## 7. 断点、完整性和诚实退出

工作文件只在输出根目录，前缀 `R868-`、JSON gzip；原子临时文件不作为完成数据。完成阶段都带同一真实新 configuration 和 `complete=true`；`R868-Dixon-current.json.gz` 是 `complete=false`，在 FINAL 单列。

数学 tag 固定 core SHA、证明/方法 SHA、全部选择源、原索引顺序、列尺度规则、素数序列和重构策略。预算、最大素数试次数、最大 Dixon 位数及纯运输 route 不进数学 tag。续算可以提高控制上限，但不能改数学源或算法权重；所有旧完成组/子式/逆/位直接回用。

旧 `complete=false` FINAL 是历史终点，不能拿其旧 current SHA 约束后来已推进的 current。真成功 FINAL 则必须恢复全部所指完成阶段，并逐 manifest 的 bytes/SHA 检查。

首 scope 成功旗标分别为：点纤维秩271、准确 normal socle、两图完整点逆254次理想、五个完整254次数模块 DAG。`degree254_RR_basis_128_computed` 与 `original_connection_or_height_computed` 始终为 false。预算/位数停止时已经完成的子式保真，但未完成的准确 h 和截面不得填真。

新论文的 $\mathcal O^{128}\oplus\mathcal O(-1)^{144}$ 及128权0+144权1的完整性证书是下一 RR 消费的固定目标，不是本次输出维数的冒认。
