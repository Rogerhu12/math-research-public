# 十七条原自然三阶左来源及法次数至多四的精确范围

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。

## 1. 原式结果与范围

固定同一原来源集合 $J$、原输出集合 $I$ 和自然参数 $u=1/s$，
$$
B(u)=A^h(u)[I,J]=\sum_{\nu\ge0}u^\nu B_\nu,
\qquad |I|=|J|=4354.
$$
左向量按原 $4367$ 输出坐标保存，在 $I$ 外置零；乘回使用全部 $4354$ 个原来源。这里没有换为共动矩阵。

本次实际构造 **17 条头独立的整数四项来源**
$$
\lambda^{(a)}(u)=\lambda_0^{(a)}+
 u\lambda_1^{(a)}+u^2\lambda_2^{(a)}+u^3\lambda_3^{(a)}
$$
并逐原坐标验证
$$
\sum_{\nu=0}^k B_\nu^T\lambda_{k-\nu}^{(a)}=0,
\quad k=0,1,2,3,\quad 1\le a\le17.
\tag{1.1}
$$
总计 $17\cdot4\cdot4354=296072$ 个原整数产品全零。17 个头在已付的 33 维第一可延头坐标中独立；最大实际整数系数 5460 bit。最后校正 $\lambda_3$ 的法次数至多四。法变量仍为原 $m_0,\ldots,m_8$，纯切向变量为 $d=m_9,c=m_{10}$。

**完整第三可延头空间仍为已证的 21 维。** 本次没有将其降为 17；本次付清了其中用法次数至多四的最后校正可表示的 17 维空间。其余四个头仍有完整第三左来源的存在性，但最后校正尚未显式恢复。

完整第三连接等于 3 及完整 21 维头空间见
[R150-appendix-selected-natural-third-connection-exact-three-twentyone-heads-and-cost8601.md](R150-appendix-selected-natural-third-connection-exact-three-twentyone-heads-and-cost8601.md)。

## 2. 实际执行身份

| 项目 | 实际值 |
|---|---|
| run | 43702348535 |
| step | third21-normal-four-original-consumer |
| 执行源提交 | b383dc5220eb147ff4b37dccb2234878589ceeff |
| 程序字节数 | 32637 |
| 程序 SHA256 | 89a1e354928c70a9ff9aac28e1935d78739ea760ce39bb8b58dc2f7cf378c854 |
| 数学时间 | 22.819771111999216 秒 |
| 墙钟时间 | 22.90399264699954 秒 |
| 原残差阶段 | 11.1890478360001 秒 |
| 原四层来源及乘回阶段 | 11.539315707999776 秒 |
| 原完整回执 | 12713 字节 |
| 原回执 SHA256 | e595023947414b81e34df4f03a6b09047c5d1f3c52b1bbd9f31da4b53c0261a1 |
| 输入绑定 | 68b83b621a2219162ca36499757ab327cac7431f669e2fcc83e1de232affef50 |

实际小回执为
[43702348535-third21-normal-four-original-consumer.json](../notes/r150-infinity-remote-session-789f/43702348535-third21-normal-four-original-consumer.json)。
它同时记录 actualExplicitThirdHeadDimension=17、completeGlobalThirdHeadDimension=21、all21CompleteThirdHeadsExplicit=false、allOriginalFourLayerProductsZero=true、allActualHeadCoordinatesIndependent=true、fourthForcingComputed=false，outcome 为 restricted-normal-four-third-cochains-only。

所有大数组只在本次 job 临时目录中保存；长期记录源码、参数、实际运行和完整散列，不将可重算数据提交 Git 或 Release。

## 3. 完整原残差系统

令 $M_0=B_0^TE_{\mathrm{new}}$ 是满列秩的 $4354\times1546$ 原整数矩阵。旧第一校正使用 $E_{\mathrm{old}}$，本次始终分别保留两个实际嵌入。

原 36 个右端 $[H_F,T]$ 包含 3 个第一失败方向和 33 个第一可延方向，另有已完成的 130 个法四高核方向。每个真实单位解 $N_r/D_r$，$D_r>0$，给全部原行上的残差
$$
S_r=M_0N_r+D_rF_r,\qquad 1\le r\le166.
\tag{3.1}
$$
这些 166 个残差的完整有理秩已经付为 144。本次核对全部旧来源文件身份，没有重解旧 36 或 130 个右端。

由完整 21 维第三头投影形成新的 21 个真实右端 $q_j$，保留其实际整数化因子。新单位解 $n_j/d_j$ 给
$$
v_j=M_0n_j+d_jq_j,\qquad d_j>0.
\tag{3.2}
$$
单位解只先付 1546 个选定行；本次随后计算了全部 $4354$ 行的 $v_j$。当前 $M_0$ 的空行为 1922 个，旧高零行清单只是其中 1736 行，额外 186 行均保留在完整余量和最终乘回中。

取 $S_r$ 的真实 144 列基。令其原列 content 为 $c_r$，令 $v_j$ 的 content 为 $t_j$。在原行选择真正非零的 144 阶子式后，先保存完整有理解，再算
$$
R_j=D_j^{\mathrm{span}}\frac{v_j}{t_j}
 +\sum_{r=1}^{144}
 N_{rj}^{\mathrm{span}}\frac{S_{p_r}}{c_r}.
\tag{3.3}
$$
小素数只用于选择这个有理单位子式，不作为新的原大矩阵秩结论。所有原行参与 (3.3)，没有只检查选定行。

实际完整余残差秩为四；完整核为 17 维。每个核系数 $\kappa$ 都逐原行核清
$$
\sum_jR_j\kappa_j=0.
\tag{3.4}
$$
这一步实际生成并验证了完整核，不是只按 $21-4$ 填入维数。

| 临时对象 | 字节数 | SHA256 |
|---|---:|---|
| 原残差 144 阶单位 profile | 66597 | 9b4815f10fc1fef3194f2ec24c95be2c7868a08b72570390ba6c5effd8ae1417 |
| 144×21 完整有理解 | 98953 | d81da8a51c570556ad98eabea5bb131d3cf9b91825a19ad6c93f3992b36316af |
| 全原行 21 条余残差 | 65222 | 7835f183e25640397796706042038d94fe46725b59a1918349747addc3c56e05 |
| 完整 17 维头组合 | 2138 | 4a27a932d31814078ee0b70c0e55878aade1f1c37772f5c41025bf69b1d8a322 |
| 原残差阶段回执 | 5540 | 2f344be6e73add1fd49b23b28bd00beec6061e48a74f55e6e8dde4f23c6522a5 |
| 原四层乘回回执 | 10890 | 8a147b79e6f7a502aacc58fc07605c6754addf5d550295e838929955f5d1055f |

## 4. 列比例与完整四层回接

由 (3.4) 取
$$
\beta_j=\frac{D_j^{\mathrm{span}}\kappa_j}{t_j},
\qquad
\gamma_{p_r}=
 \frac{\sum_jN_{rj}^{\mathrm{span}}\kappa_j}{c_r},
$$
其余 $\gamma_r=0$，得到未缩放原列的恒等式
$$
M_0\left(\sum_j\beta_jn_j+\sum_r\gamma_rN_r\right)
 +\sum_j\beta_jd_jq_j+\sum_r\gamma_rD_rF_r=0.
\tag{4.1}
$$
新 21 个右端的整数化因子、旧 22 条二阶来源的 primitive 因子都同步运输；同一比例必须作用于整个低阶来源，不能只作用于右端。

记组合后的旧来源为 $(L_0,L_1,L_2)$，完整第一头矩阵为 $\Lambda C$，第一失败方向为 $\Lambda F$，且
$$
B_0^TE_{\mathrm{old}}X+B_1^T\Lambda C=0.
$$
真实旧残差补偿给 $a,y$ 和法四高核系数 $\eta_4$。原来源按
$$
\begin{aligned}
\lambda_0&=L_0,\\
\lambda_1&=L_1+\Lambda Cy,\\
\lambda_2&=L_2+\Lambda Fa+E_{\mathrm{old}}Xy,\\
\lambda_3&=E_{\mathrm{new}}x_3+E_4\eta_4
\end{aligned}
\tag{4.2}
$$
回接。加号与 (4.1) 一致，且 $E_{\mathrm{old}}Xy$ 没有被换成 $E_{\mathrm{new}}Xy$。

每列统一清四层来源的分母、取 primitive 整数代表并先保存完整候选，然后对原 $B_0,\ldots,B_3$ 做 (1.1) 的全部 17416 个整数产品。只有全零才保存该列 verified 回执。本次 17 列全部完成。

法次数至多四范围内的完整性来自以下源级事实。全部 21 个第三头已经属于旧 22 个二阶头空间。固定头的两种二阶 lift 之差由完整 33 个第一可延方向及 36 个常左核方向表示，已经由 $T,H_F$ 和常核自由度运输。最后校正可模常左核规范为 $E_{\mathrm{new}}\oplus E_4$；高 1736 行迫其法四部分落在已完整求出的 130 维高核。随后 (3.1)–(3.4) 核验全部原行。因此本次没有漏掉该支撑范围内的合法最后校正，恰为 17 维。

上述结论不排法次数五的最后校正。它也不撤销完整 21 维第三头的存在性。

## 5. 第四页的准确受限接口

设 $E=\operatorname{coker}B_0^T$。29 个真原来源核给映射 $\pi:E\to K_{29}^*$，已付 $\ker\pi\subset W_{12}$。已知
$$
W_{13}=W_{12}+\operatorname{im}R_3(\text{旧22头})
$$
维数 13，因此
$$
E/W_{13}\simeq K_{29}^*/\pi(W_{13}).
\tag{5.1}
$$
完整第三低阶像 $W_3$ 为 15 维；缺少的两个来项仍须保留。

对本次 17 条实际来源可新算
$$
R_4=B_1^T\lambda_3+B_2^T\lambda_2+
 B_3^T\lambda_1+B_4^T\lambda_0.
\tag{5.2}
$$
设其在已知商 $E/W_{13}$ 中的真实秩为 $r$。本次尚未计算 $r$，不能预填。

完整第三域 21 维比本次实际域多四维；进一步商掉尚缺的两个低阶像方向至多降秩二。所以
$$
\boxed{\max(3,r-2)\le\operatorname{rank}_{\mathbb Q}\beta_4
 \le r+4.}
\tag{5.3}
$$
下界 3 仅在同一原单位 Schur 前三页已证 $\mathbb Q/\mathbb F_{31}$ 秩均为 $3,9,3$ 后使用。式 (5.1) 还使已知商核的 $17-r$ 个方向给出真实第四可延头的存在性，但并未自动构造 $\lambda_4$。

域只有 17 维时，不能套用完整 21 维域下的“$r=3$ 即闭第四秩为 3”。在本次受限域上 $r=0$ 也非先验矛盾，它只给完整第四秩区间 $[3,4]$。

## 6. 缺四头的最小后继

式 (3.3) 的 21 条完整余残差已经保存且秩四。因此只需选择四个真正商代表作为新增非齐次右端，已成的 17 条来源无需重解。

法五恢复必须保留
$$
H_4\eta_4+H_5\eta_5=0
$$
的完整联动，不能将 $H_5$ 注入性当作任意高行可补，也不能沿用法次数至多四时法四分量为零的特殊结论。已有法五精确消元保存了 786 个完整 pivot 和反代 DAG；接续应从这些真实状态开始，保全部剩余法四/法五列和未选高行。

即使只新增四个非齐次右端，也须保高块的齐次核。如果高系统给 $z=T_Hc+N_Ha$，则低行仍须解
$$
\pi_{\mathrm{paid}}\bigl(R_{\mathrm{low}}+L T_H\bigr)c
 +\pi_{\mathrm{paid}}L N_Ha=0.
$$
这里 $\pi_{\mathrm{paid}}$ 商去已付 $M_0$/166 列像；$N_H$ 超出旧法四高核的方向不能删掉。未经实际验证，不预设联合高块秩 1736 或某个最终 Schur 尺寸。

本次未计算第四页，未证明参数首项是 31 单位，也未证明原九目标的特征零多项式成员性。此前完整第三头给出的指定子式阶数 $114/110/110$ 继续有效。
