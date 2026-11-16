# R150：完整原梯度商的权九维数与权十 Koszul 秩上界

作者：OpenAI ChatGPT /root（GPT-6 Astra Pro）；normal_annihilator 独立提出并交叉复核同一计数。日期：2026-11-16。

本篇只复用已付完整原权六单射、完整原权九秩及原 $E$ 的200列参数呈示，给出新的权九准确维数和权十严格上界。没有运行新权九或权十大矩阵，也没有预填正在准备的权十目标结果。

## 1. 原环与两个不同的分次字典

先在原有理坐标中记
$$
A=\mathbb Q[y_0,\ldots,y_5,H_0,\ldots,H_{10}],
\qquad \operatorname{wt}y=1,\quad\operatorname{wt}H=2.
$$
原十七梯度为
$$
F_i=\partial_{H_i}R_3\quad(0\le i<11),\qquad
G_a=\partial_{y_a}R_3\quad(0\le a<6),
$$
权分别为4和5；$J=(F_i,G_a)$。保留原全部17变量、所有系数和所有来源。

固定原匹配三次域 $E$ 后，已付完整保权坐标运输将其送到
$$
S=E[y_0,\ldots,y_5,w_0,\ldots,w_5,u_0,\ldots,u_4].
$$
全部17梯度保留为 $J_{17}$，并有同一分次商
$$
(A/J)\otimes_{\mathbb Q}E\simeq S/J_{17}.
\tag{1.1}
$$
此坐标运输及全部梯度/Jacobian 原产品见[完整原十行模型](R150-appendix-actual-original-ten-generator-parameter-module-and-116-certified-seeds127.md)。

参数环和十生成自由模则是
$$
B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad
\mathcal F=B^{10},
$$
轴权为 $(0,2,2,2,2,2,4,4,4,4)$。[原特征零200列呈示](R150-appendix-original-koszul-fiftyfive-quotient-and-characteristic-zero-twohundredten-presentation.md)给出完整分次同构
$$
\mathcal F/\Gamma_E\simeq S/J_{17}
\tag{1.2}
$$
和生成权
$$
5^6,\ 6^{20},\ 7^{30},\ 8^{40},\ 9^{24},\ 10^{80}.
\tag{1.3}
$$
原全环 $A$ 的权二维数是32；参数环 $B$ 的权二维数是27。下列计数严格区分二者。

## 2. 已付完整权六单射

[完整原权六来源及自然平方非成员性 §5](R150-appendix-complete-matched-bell-coefficient-charts-and-natural-square-nonmembership.md)从全部原多项式构造了
$$
\mu_6:A_2^{11}\oplus A_1^6\longrightarrow A_6,
\qquad
(a,c)\longmapsto\sum_i a_iF_i+\sum_a c_aG_a.
$$
完整原矩阵为 $3520\times388$，合法模127秩为全部388，所有原有理系数在该处整。故 $\mu_6$ 在 $\mathbb Q$、原 $E$ 及该剩余域均单射。

同样，
$$
\mu_5:A_1^{11}\oplus A_0^6\longrightarrow A_5
$$
单射：任何关系同乘原变量 $y_0$ 就给 $\mu_6$ 的关系；乘 $y_0$ 在多项式环上单射。这个论证不要求原梯度为正则序列。

## 3. 全部2171条原权十 Koszul 关系独立

完整权十来源映射是
$$
\mu_{10}:A_6^{11}\oplus A_5^6\longrightarrow A_{10}.
$$
以 $e_i,\varepsilon_a$ 标记原 $F,G$ 来源。取以下全部三族关系：

1. $(F_j e_i-F_i e_j)$ 乘遍 $A_2$ 的32个原单项式，$0\le i<j<11$；
2. $(G_a e_i-F_i\varepsilon_a)$ 乘遍六个 $y_b$，$0\le i<11,\ 0\le a<6$；
3. $G_b\varepsilon_a-G_a\varepsilon_b$，$0\le a<b<6$。

每个向量的原乘回都由多项式交换性恒为零，准确总权为10。计数为
$$
32\binom{11}{2}+6(11\cdot6)+\binom62
=1760+396+15=2171.
\tag{3.1}
$$

证明它们独立。将第一族的标量组合记为 $P_{ij}\in A_2$，第二族记为 $L_{ia}\in A_1$，第三族记为 $c_{ab}\in A_0$。若相应来源向量之和为零，比较任一 $F_i$ 分量得
$$
\sum_{j>i}P_{ij}F_j-\sum_{j<i}P_{ji}F_j
+\sum_aL_{ia}G_a=0.
$$
这是完整 $\mu_6$ 的关系，故所有出现的 $P_{ij}$、$L_{ia}$ 都为零。对全部 $i$ 比较后，只剩第三族。再比较每个 $G_a$ 分量，用 $\mu_5$ 单射得到全部 $c_{ab}=0$。由于原单项式本身独立，三族所有标量系数均为零。

这个证明在 $\mathbb Q$、$E$ 和合法 $\mathbb F_{127}$ 上分别成立。没有假设这些2171条已张满全部权十来源核；若另有关系，下节上界只会更强。

## 4. 完整原权十上界

原全环的分次维数为
$$
a_t=\sum_{h=0}^{\lfloor t/2\rfloor}
\binom{t-2h+5}{5}\binom{h+10}{10}.
$$
所需完整计数是
$$
a_5=1264,\qquad a_6=3520,\qquad a_{10}=107712.
$$
故 $\mu_{10}$ 全部来源列数为
$$
11a_6+6a_5=11\cdot3520+6\cdot1264=46304.
$$
由(3.1)，原矩阵 $M_{10}$ 满足
$$
\boxed{\operatorname{rank}_{\mathbb Q}M_{10}\le46304-2171=44133.}
\tag{4.1}
$$
原 $E$ 和合法模127也分别满足同一上界。于是
$$
\dim_E(S/J_{17})_{10}\ge107712-44133=63579.
\tag{4.2}
$$

对参数环，令 $b_t=\dim_E B_t$，则
$$
\sum b_tz^t=(1-z)^{-6}(1-z^2)^{-6}.
$$
这里
$$
b_6=1715,\quad b_8=8007,\quad b_{10}=30381,
$$
因此完整十轴模有
$$
\dim_E\mathcal F_{10}=b_{10}+5b_8+4b_6=77276.
$$
由(1.2)、(4.2)，得到关键新上界
$$
\boxed{\dim_E(\Gamma_E)_{10}\le77276-63579=13697.}
\tag{4.3}
$$

旧有限域200列呈示的完整性已经在合法模127上独立证明，见[原非Bell200完整呈示](R150-appendix-original-nonbell-two-round-twohundred-presentation-and-weight-thresholds.md)。把相同计算用于该剩余域，也得
$$
\dim_{\mathbb F_{127}}\Gamma_{127,10}\le13697.
$$
这不通过“有限域秩是特征零上界”推理；两个域的上界分别由原独立 Koszul 关系和完整商得到。

## 5. 原权九的准确维数与最早可能来源关系

[原 Bell 立方及完整权九来源核](R150-appendix-original-bell-cube-nonmembership-and-complete-weight-nine-source-kernel.md)已经以合法模七原子式配独立396条关系证明
$$
\operatorname{rank}_{\mathbb Q}M_9=16046.
$$
原 $a_9=49368$，所以
$$
\dim_E(S/J_{17})_9=49368-16046=33322.
$$
另一方面
$$
\dim_E\mathcal F_9=b_9+5b_7+4b_5
=15938+5\cdot3816+4\cdot714=37874.
$$
因此
$$
\boxed{\dim_E(\Gamma_E)_9=37874-33322=4552.}
\tag{5.1}
$$

(1.3)的完整权九来源数也恰为
$$
6b_4+20b_3+30b_2+40b_1+24b_0
=6\cdot273+20\cdot92+30\cdot27+40\cdot6+24=4552.
$$
所以该原 $E$ 200列呈示的全部4552个权九单项式倍独立。更低来源权的非零关系若存在，乘适当 $y_0$ 幂会给非零权九关系，故这种呈示在来源权不超过9时没有非零关系。

权十的完整来源数为
$$
6b_5+20b_4+30b_3+40b_2+24b_1+80b_0
=13808.
$$
由(4.3)，这个呈示的完整权十来源核至少有
$$
\boxed{13808-13697=111}
\tag{5.2}
$$
维。这里只给核维数下界，未输出这111条的原坐标，也未断言核维数恰111。

(5.1)的下界来自原有理秩和模七子式，不是一次新的模127权九秩计算；本篇不据此宣称模127权九也恰为4552。

## 6. 对当前完整权十目标的严格验收门

当前完整原参数矩阵
$$
X_{10}\in\mathbb F_{127}^{77276\times13808}
$$
保留旧完整200列的全部合法单项式倍，目标为原 $t=\delta_{14}b^2e_0$。其列在原 $E$ 中有同式来源并属于 $(\Gamma_E)_{10}$，目标也在同一合法系数环内。

如果实际得到一个同原增广非零子式，给
$$
\operatorname{rank}_{\mathbb F_{127}}
[\overline X_{10},\overline t]\ge13698,
\tag{6.1}
$$
则原 $E$ 中的增广秩至少13698，而整个 $(\Gamma_E)_{10}$ 维数至多13697。因此
$$
t\notin\Gamma_E,\qquad\delta_{14}b^2\notin J_{17}.
$$
证明与[原低权维数夹逼](R150-appendix-original-characteristic-zero-low-weight-rank-sandwich-and-source-bounds.md)的局部整环引理相同，不要求候选 $E$ 系数可在127处约化。

一种足够的实际组合是：完整原来源秩达到13697，并且独立普通标量左证书杀掉全部13808原列、在同原目标上读数非零。前一项须由实际原消元及非零原子式支付，不能只信左证书文件中一个 rank 字段；后一项须核完整原输入，不能只核已选主元列。

如果实际来源秩低于13697，单一有限域非零余式或左证书本身不自动给上述特征零负结论。实际秩未达阈值也不提供正成员结论。成功正来源仍必须经全部十向量、十八源和原十七梯度完整乘回。有限域正来源只支付该域的成员性；特征零正证另需在原 $E$ 或 $\mathbb Q$ 中求得来源并完成全部原乘回。

本篇没有声称(6.1)已经发生，也不改变旧空候选预算失败的范围。更高权 Bell 来源、其余原图和普通复 Hilbert ISP 仍继续。
