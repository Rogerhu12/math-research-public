# 原 Bell 归一临界商的五十六个完整七生成元图册

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。2026-11-16。

## 1. 覆盖的是全体 Bell 非零归一支路

使用[完整十生成元有限表示](R150-appendix-complete-original-ten-generator-finite-critical-presentation.md)的原57列子集，以及[三阶子式理想等式](R150-appendix-original-mean-three-minor-ideal-is-the-cube-of-the-mean-ideal.md)。系数环
$$
B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad S=B[u_0,\ldots,u_4]
$$
与原匹配三次域 $E$ 保持不变。原归一条件为 $b=y\cdot w=1$。

六条原均值关系的四个二次生成元系数为
$$
M(y)=[T_1y,T_2y,T_3y,T_4y]\in E[y]^{6\times4}.
$$
先前实际80个原3×3子式中，完整三次系数方块选出了56个原子式
$\delta_1,\ldots,\delta_{56}$，它们的56×56系数矩阵是 $E$ 单位。因此这**选中的56个原子式本身**已经满足
$$
(\delta_1,\ldots,\delta_{56})=(y_0,\ldots,y_5)^3.
\tag{1}
$$
本文没有把“选中的56个”写成“全部80个”。

在 $B/(b-1)$ 中，$1=\sum_iw_iy_i$，故 $(y)^3$ 为单位理想；(1)说明这56个原子式开集覆盖全部 Bell=1 参数。没有只保泛点，也没有排除 $M(y)$ 的真实 rank3支路。

本次实际为每个开集构造一个完整7×54矩阵及全部原来源。对每个 $\delta_\alpha$，
$$
\operatorname{coker}_{S[\delta_\alpha^{-1}]}\mathcal P_\alpha
\cong (S/I)[\delta_\alpha^{-1}],
\tag{2}
$$
其中 $I$ 是原十七梯度与 $b-1$ 生成的理想。每个 $\mathcal P_\alpha$ 的条目对五个 $u$ 至多一次。完整原临界问题因此等价于这些真覆盖图册上的问题，尚未据此证明任一图册或全部图册为空。

## 2. 原行列标签与真正的源 Schur

从实际10×68母输出中取已证明等价的57列：
零起始编号 $0,\ldots,49,61,\ldots,67$。对选中子式的原 mean 行
$R=(r_0,r_1,r_2)$、原二次列 $C=(c_0,c_1,c_2)$：

- 消去的原模生成元行是 $6+c_0,6+c_1,6+c_2$；
- 三个原关系列是 $61+r_0,61+r_1,61+r_2$；
- 其余七个模生成元及54个原关系列全保留，顺序不变。

按此原标签分块，母矩阵为
$$
\mathcal P_{57}=
\begin{pmatrix}A&B_0\\C_0&D_0\end{pmatrix},
\qquad A=M[R,C]^{\mathsf T}.
$$
故 $\det A=\delta_\alpha$，没有额外符号或参数比例。实际保存的是不含分母的矩阵
$$
\mathcal P_\alpha=\delta_\alpha D_0-C_0\operatorname{adj}(A)B_0.
\tag{3}
$$
在原子式开集上，(3)与通常 Schur 补仅差可逆的列比例 $\delta_\alpha$，所以给(2)。

这里 $A$ 全部为真实 $y$ 线性式，$C_0$ 与各均值参数系数完整保留。母57列对 $u$ 至多一次，而 $A,\operatorname{adj}(A),C_0$ 不含 $u$，故(3)仍对 $u$ 至多一次。这不是在某个参数数值上计算的 Schur 补。

每个图册都保持七个原单项式：
$$
1,u_0,\ldots,u_4,\quad\text{四个原 }v_l\text{ 中未消去的一个}.
$$
没有声称这七个生成元线性无关、自由或在不同图册自动构成同一全局七元基。

## 3. 全部原来源和双向图映射

把原完整18个生成元排成行
$$
\mathcal G=(F_5,W_6,Y_6,b-1).
$$
母表示的三主列与其余54列原来源分别记为 $S_P,S_R$。实际原身份为
$$
m_EA+m_KC_0=\mathcal G S_P,\qquad
m_EB_0+m_KD_0=\mathcal G S_R.
$$
这里 $E,K$ 是被消去与保留的原模行，完全对应§2标签。先右乘伴随矩阵，得到三条完整图身份
$$
\delta_\alpha m_E+m_KC_0\operatorname{adj}(A)
=\mathcal G S_P\operatorname{adj}(A).
\tag{4}
$$
再从第二式乘 $\delta_\alpha$ 的结果减去(4)右乘 $B_0$，得
$$
m_K\mathcal P_\alpha
=\mathcal G\bigl(\delta_\alpha S_R-S_P\operatorname{adj}(A)B_0\bigr).
\tag{5}
$$
本次每个图册同时保存(3)的全部7×54坐标、(5)的全部18×54原来源，以及(4)的全部18×3原来源。原 $F,W,Y$ 仍通过已付完整 Jacobian 运输回原17变量梯度；没有停在来源未知的新关系中。

在 $\delta_\alpha$ 可逆时，保留生成元从子表示映入母表示；被消去生成元反向按
$$
m_E=-m_KC_0\operatorname{adj}(A)/\delta_\alpha
$$
运输。由(4)、(5)及原三主列关系，两映射互逆。这给(2)的完整来源证明，而不是只证明某个必要残差为零。

固定3×3伴随矩阵的左右18个恒等式在九个独立整变量上逐项验证。所有图册都按同一原符号与转置约定代入；该通用验证不使用有限域来替代 $E$ 上的伴随恒等式。

## 4. 实际原子式核对

消费者重新读取原六 mean 模型与四个 $T_l$ 的完整文件 SHA。全部432个有理分量在实际 $(127,d=100)$ 的约化均合法，并重建原144个矩阵条目，逐项匹配原子式证书。

随后重新核：

- 原56×56系数单位的全部6272个左右乘回坐标；
- 56个选中原子式各自全部56个三次系数，共3136个系数；
- 每个原子式的原 rows/columns、原 degree3来源标签及零乘子；
- 每个图册的七个原保留行、三主列、全部54余列、原18来源顺序；
- 每个新表达式的后向引用与 $u$ 次数界。

其中有限域核验用于识别实际选中的**原常数系数单位**，从而严格证明该原 $E$ 方块非零；没有把任意有限域商矩阵当作特征零基。全参数 Schur 与来源恒等式由(3)–(5)精确给出。

## 5. 实际执行身份

首版实际在0.3713665800023591秒触发输入标签断言：旧系数证书记录的是
minorIndex与全零 multiplier，原 rows/columns 另在完整80字典中。该次没有进入完整图册构造，exit1保持。v2修为严格核 degree3、全零 multiplier，再映回全部原 rows/columns，未删除校验、未重选来源。

v2实际 exit0，7.132909848005511秒，最大常驻72944 KiB。全部56图册完成。构造并保留：

- 21168个子矩阵坐标，即 $56\cdot7\cdot54$；
- 54432个原来源坐标，即 $56\cdot18\cdot54$；
- 168条消去生成元的完整图身份；
- 每个图册至多5290个新节点，共用原105774节点而不复制母图。

这些是完整表示与来源的坐标数，不冒称对巨大参数多项式进行了展开式重乘。原参数身份的证明是精确通用伴随及(4)、(5)，其全部实际输入与索引均已核。

binding：
~~~text
ad9efd97def71be282ace34d218e8c78c50c2d362fb9fef0a753025fd9891247
~~~

| 对象 | 字节数 | SHA256 |
|---|---:|---|
| v2实际小回执 | 1472 | f5a8a0dbb84474ffc74e5e732983403c94311b94d700df90c10427d631e43145 |
| 完整56图册索引 gzip | 6452 | 8bc2901b3ee9631ea3f53fdb03fe62051cae0b3b83532ed07ba6ce7acd48a707 |
| 完整56图册索引逻辑内容 | 16181 | b9ec3af3d8196524d30ec94a9dc2daca0ce790d0578e7c96d9c42b7089bc355d |
| 首版失败回执 | 509 | 170f0466d3e0d153318c6af6dc0f92ff7903cbd6dc7bfd0b932aee05c7863757 |

小可重现入口：

- [最终图册消费者](../notes/2026-11-16-r150-original-complete-fifty-six-seven-generator-charts-v2-789f.py)；
- [输入与祖先 pins](../notes/2026-11-16-r150-original-fifty-six-seven-generator-charts-inputs-v2-789f.json)；
- [精确局部化与源运输接口](../notes/2026-11-16-r150-original-fifty-six-seven-generator-charts-interface-v2-789f.md)；
- [执行身份](../notes/r150-nonrankone-execution-789f/20261116-local-original-fifty-six-seven-generator-charts-v2.json)。

原大数据与图册数组不入库。后继判空仍须使用这些完整来源及覆盖条件，不能用单一泛点、任取一个子式开集、未经证实的 rank4，或“局部七生成”代替原全参数临界理想结论。
