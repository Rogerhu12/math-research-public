# 缺四个第三来源：真实高块 profile、29 源支撑交及四个原商代表

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

## 1. 状态与用途

代码 2026-11-15-r150-third-missing-four-high-profile-789f.py，17548 字节，SHA256 为 831fee03bebcc30c05d3d9b9dd4415db1862c6586a26df37bb28537f1313fdf3。已对这组字节实际 ast.parse 成功；未执行数学。

该阶段为接续缺少的四条真实第三来源确定必要的小线性代数入口。它复用已经保存的原 $H_5/H_4$ 配对矩阵，不重 786 个精确 pivot；复用 29 条原来源，不重有理核恢复；复用已付 17 维核和全部 21 条原余残差，不重 21 单位解。

唯一新增工作是：

1. 从完整 17 维余残差核中选择四个真正商代表；
2. 对原 $1736\times2772$ 高矩阵 $H=[H_5,H_4]$ 计算一次完整模 31 profile，实际核其选定单位子式；
3. 求 29 个已付真来源在这 1736 个高来源行上的精确支撑交，并将这些真正高行左关系乘回全部 2772 列；
4. 只有实际模 31 下界和真有理上界相等时，才报告 $H$ 的精确有理秩。

本阶段不恢复完整高核、不计算新大单位逆，也不产生新的 $\lambda_3$。它的输出决定下一四个非齐次右端的确切尺寸；保全部高齐次自由。

## 2. CLI

    python -B {scripts}/2026-11-15-r150-third-missing-four-high-profile-789f.py
      --normal5-out {work}/selected-natural-second-left-normal-five-high-elimination
      --pairing-out {work}/same-source-koszul29-second-pairing
      --second-out {work}/selected-natural-second-left-regauged
      --consumer-out {work}/third21-normal-four-original-consumer
      --out {work}/third-missing-four-high-profile
      --seconds 60
      --memory-mib 2048

normal5-out 必须指原 step21 的实际输出目录，包含 prepared/complete-original-high-normal-five-and-four.json.gz 与 prepared/original-h5-field-unit-profile.json.gz。本 CLI 已与当前请求中原 step21 的实际输出路径核对，不改数学文件或 binding。

主回执：third-missing-four-high-profile-receipt.json。

完成返回 0、status=completed。数学时间到边界返回 75、status=completed-prefix，保存已成四商代表、原高 profile 或真实支撑关系。失败返回 1 并保异常日志。共享数学 60 秒、每进程 2 GiB；各完整 stage 可按同一输入/程序绑定复用。所有完整数组仅临时保存。

## 3. 固定输入

| 键 | 字节数 | SHA256 |
|---|---:|---|
| old_unit | 9008513 | c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe |
| high_pair | 1019818 | d2ae353a064704e8d721d1663a6e838f93195438d004d2662386a8d34dd56024 |
| old_h5_profile | 5489 | c4e504e9ad006aa6b44572c888d26602662f9efde7a040dd43c0a9e446c878f1 |
| source_receipt | 15304 | 11b0f10e9c0750b73644c425f91b48a249e5829a8dc7960e68e7713ef545f289 |
| head_kernel | 2138 | 4a27a932d31814078ee0b70c0e55878aade1f1c37772f5c41025bf69b1d8a322 |
| residual | 65222 | 7835f183e25640397796706042038d94fe46725b59a1918349747addc3c56e05 |
| span_profile | 66597 | 9b4815f10fc1fef3194f2ec24c95be2c7868a08b72570390ba6c5effd8ae1417 |
| span_solution | 98953 | d81da8a51c570556ad98eabea5bb131d3cf9b91825a19ad6c93f3992b36316af |

29 个实际来源证书的字节身份由已付 source_receipt 清单继承，消费前逐文件核验。所有原 $6188$ 来源、所选 $J$ 支撑和全部 $4367$ 原乘回的已付身份均保留；不将模 31 核替作有理核。

## 4. 四个商代表与尺度

已付 21 条原余残差 $R_j$ 的核为 17 维。对这 17 条完整核系数作小 RREF，取四个非主元坐标 $j_1,\ldots,j_4$，则对应标准单位向量给该核的一个补空间。程序还在原 $4354$ 坐标中核
$$
\operatorname{rank}_{\mathbb Q}[R_{j_1},\ldots,R_{j_4}]=4
$$
以及全部 1736 高行余量为零。

代表的来源不是任意重新挑选的二阶初值。它们正是已付 consumer 中 $\kappa=e_{j_a}$ 的四个方向，保
$$
\beta_j=D_j^{\mathrm{span}}/t_j,\qquad
\gamma_{p_r}=N_{rj}^{\mathrm{span}}/c_r.
$$
这些比例连同原残差列全部保存。后继通过已付 consumer 的同一公式恢复其原低层 cochain；不丢 $d_j/g_j$ 或旧 primitive 因子。

输出 four-genuine-third-head-quotient-representatives.json.gz，包含四个原索引、完整原残差、全部 166 补偿比例，以及不重算旧 17 来源的明确标志。

## 5. 高矩阵的两个真实界

原高矩阵有 1736 行，列为全部 1287 个法五输出和全部 1485 个法四输出。程序只从已付原 pair 读取，保其原来源行标签；没有用已经放大的消元系数冒充原矩阵。

模 31 得 $r$ 后，实际选行、列并核 $r$ 阶子式非零，故
$$
\operatorname{rank}_{\mathbb Q}H\ge r.
$$

记 $K$ 为同一原 $J$ 上的 $4354\times29$ 真有理来源矩阵，$L$ 为高行集的补集。完整求
$$
C=\ker_{\mathbb Q}K_L,\qquad d=\dim C.
$$
只对这些真正满足 $K_Lc=0$ 的组合取高行部分。由完整原来源恒等式，
$$
(K_{\mathrm{high}}c)^T H=0.
$$
程序逐坐标核 $K_Lc=0$，再乘回全部 2772 个原高列，并核这些左关系独立。因此
$$
\operatorname{rank}_{\mathbb Q}H\le1736-d.
$$
不得直接截断不支撑于高行的任意旧来源作为左关系。

只有 $r=1736-d$ 时，回执才写 actualH45RankOverQExactlyKnown=true。否则只保真实区间。高核维数在
$$
2772-(1736-d)\le \dim\ker H\le2772-r
$$
之内；再商已付 130 维法四高核仅减去 130。没有预填联合高秩 1736，也没有预填恰好 906 个新高方向。

## 6. 完整常数纠偏的规范与可选解法

现有 $E_{\mathrm{new}}$ 有 1546 列，$E_4$ 有 1485 列，$E_5$ 有 1287 列，总数 4318。该原规范的满列秩可从已付事实证明，无需额外大有理消元：

- 原完整常左核全部支撑在法次数至多二；
- 若支撑 $E_{\mathrm{new}}\oplus E_4\oplus E_5$ 的向量落入常左核，它的 $E_4,E_5$ 分量必先为零；
- 余下 $E_{\mathrm{new}}$ 分量由已付 $M_0=B_0^TE_{\mathrm{new}}$ 满列秩迫为零。

因此
$$
B_0^T[E_{\mathrm{new}},E_4,E_5]
$$
恰是完整原像的 4318 列基。再加入 $H_F,T$ 的完整 12 维商像，增广映射秩为 4330。这是一条源级规范结论，不等于已经拥有其有理单位逆或低成本分解。

直接 4330 阶解是可选架构，但不应把巨大 $H_F,T$ 清分母列混入原矩阵后盲目重启大 dense 消元；同一组它们作为少量右端、原单位块及真实小 Schur 的组织方式应按实际高度/稀疏结构决定。

## 7. 后继必须保的齐次自由

四个原商代表只减少非齐次右端数，不能删除未知高齐次核。完整高/低系统是
$$
Hz=0,\qquad
\pi_{\mathrm{paid}}\bigl(Rc+Lz\bigr)=0.
$$
若实际高消元得到 $z=T_Hc+N_Ha$，则低系统必须保
$$
\pi_{\mathrm{paid}}(R+LT_H)c+\pi_{\mathrm{paid}}LN_Ha=0.
$$
旧 786 个完整 pivot/DAG 可以继续使用；剩余所有法四、法五列和未选高行仍须保留。

新的第三来源须完整原四层乘回且头独立之后才计入。当前第四像在已知商秩为 1；若后来新增两条独立第三来源而新已知商像仍秩 1，完整第四秩即可由上界 $1+(21-19)=3$ 与已付下界 3 夹定。这只是可能的实际停止准则，不预报新方向可成。
