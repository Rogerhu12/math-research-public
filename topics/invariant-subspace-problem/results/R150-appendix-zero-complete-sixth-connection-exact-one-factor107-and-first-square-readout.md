# R150：零点完整第六连接恰一、公共因子 $K_{107}$ 与首次非零平方读数

2026-11-15；Astra-ISP-789f / literature_audit；AI 辅助：GPT-6 Astra Pro。

## 1. 新结论与准确范围

在原自然参数 $s=0$、原十七式以及全部 $6188$ 个原次数不超过三的来源上，本次实际有理运算证明

$$
\operatorname{rank}_{\mathbb Q}\beta_{6,0}=1,\qquad
\dim K_6=17.
\tag{1.1}
$$

这里 $K_6$ 是完整第六左头空间。全部较低阶连接像及其实际 cochain 修正均被保留。完整前六级连接秩现在为

$$
(4,0,1,3,1,1).
\tag{1.2}
$$

结合已付第七、八页的真实左 jet，得到

$$
\delta_{4354,0}\ge61,\qquad
\delta_{4353,0}\ge52,\qquad
9\le a_{\max,0}\le14.
\tag{1.3}
$$

因此原仿射公共因子提高为 $K_{107}$。结合当前同选定子式的无穷远阶 $130/125/125$，条件来源费用为 $8582$，目标分支费用仍为 $172$。

本次另出现新的真实目标信息：$\lambda_0,\ldots,\lambda_5$ 的九平方读数全零，但 $\lambda_6$ 有非零读数。它给未乘 $h_0$ 的相应目标在本有限来源模块中的局部障碍；由于原 $h_0$ 在零点有三阶零点，当前第六左 jet 尚不足以否定 $h_0t_j$ 的成员性。第七节给出精确坐标和值。

主要来源：

- [完整第五连接、$K_{105}$ 与费用 $8584$](R150-appendix-zero-complete-fifth-connection-exact-one-factor105-and-cost8584.md)；
- [通用完整高阶源码](../notes/2026-11-15-r150-zero-complete-higher-full-incoming-789f.py)；
- [本次完整第六实际回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-complete-sixth-full-incoming.json)；
- [同选定子式无穷远阶 $130/125/125$](R150-appendix-seventeen-source-fourth-pairing-rank-one-sixteen-heads-and-cost8585.md)；
- [既有第八页真实左 jet 与公共阶](R150-appendix-zero-fourteen-eighth-left-jets-factor104-and-cost8600.md)。

## 2. 完整第六页的旧像

沿前稿的原共动坐标，写

$$
M(s)=A_{\mathrm{new}}(s)^{\mathsf T}
=\sum_{j\ge0}s^jM_j.
\tag{2.1}
$$

全部原目标与来源变换保留；回到原目标左泛函时使用目标变换的转置。若 $T_k(v)=\sum_{\ell=0}^ks^\ell\lambda_\ell(v)$ 是真实 $k$ 阶 cochain，则

$$
M(s)T_k(v)=O(s^{k+1}).
\tag{2.2}
$$

令 $R_j$ 为真实 $T_{j-1}$ 的第 $j$ 阶 forcing。对同一第五头，任意两个第五 cochain 之差可逐阶表示为

$$
sT_4(K_4)+s^2T_3(K_3)+s^3T_2(K_2)
+s^4T_1(K_1)+s^5K_0
\pmod{s^6}.
\tag{2.3}
$$

已付完整 $\beta_{2,0}=0$，所以 $R_2(K_1)$ 被
$\operatorname{im}M_0+M_1K_0$ 吸收。完整第六连接所需的全部低页像为

$$
W_5=\operatorname{im}M_0+M_1K_0+
R_3(K_2)+R_4(K_3)+R_5(K_4).
\tag{2.4}
$$

因此只保最后的 $M_1Q$ 或只保第五 forcing 的商秩，均不能替代 (2.4)。本次计算保留每组真实来源列，并将其参数回填到全部相应阶数。

## 3. 原全来源消元与精确秩

全部来源仍按 normal 次数分成

$$
170+918+2295+2805=6188.
\tag{3.1}
$$

已付高齐次核

$$
N_{\mathrm h}:\mathbb Q^2\longrightarrow\mathbb Q^{3762}
\tag{3.2}
$$

参数化全部使 $5100$ 个高来源行为零的非纯高校正。全部非纯目标校正共 $4347=585+3762$ 个，未删高层的相互抵消。

令

$$
B=[J_0,M_1Q]\in\mathbb Q^{1088\times592},\qquad
C_{\mathrm h}=(M_0N_{\mathrm h})_{\mathrm{low}}.
\tag{3.3}
$$

已付 $\operatorname{rank}B=582$。完整第五十八头中，十个纯头对所有参数精确为零 cochain，余八头的实际第六 forcing 为

$$
R_6=\sum_{j=1}^6M_j\lambda_{6-j}
\in\mathbb Q^{6188\times8}.
\tag{3.4}
$$

其 $5100$ 个高来源行在本次实际逐项核验中全部为零，故高校正仍恰由 (3.2) 给出。完整低矩阵为

$$
\mathcal M_6=
[B,C_{\mathrm h},R_{3,\mathrm{low}},
 R_{4,\mathrm{low}},R_{5,\mathrm{low}},R_{6,\mathrm{low}}]
\in\mathbb Q^{1088\times636}.
\tag{3.5}
$$

其列数为 $592+2+13+12+9+8=636$。完整旧像在低行上的秩为 $589$；本次实际核验给出

$$
\operatorname{rank}\mathcal M_6=590,\qquad
\dim\ker\mathcal M_6=636-590=46.
\tag{3.6}
$$

核向最后八个新 leading 参数的投影维数为 $7$，归一化零 leading 纤维维数为

$$
46-7=39=628-589.
\tag{3.7}
$$

因此

$$
\operatorname{rank}\beta_{6,0}
=590-589=8-7=1,\qquad
\dim K_6=10+7=17.
\tag{3.8}
$$

完整旧像 (2.4)、完整高校正 (3.2) 和完整第五头共同保证这是精确连接秩，而非固定代表包络的秩。

计算复用同一 $582$ 阶单位块及三十六个旧实际 RHS 解，只新增八个单列 Dixon 求解。全部 $1088$ 个原低行 Schur 均被核验，没有重复旧大消元或构造完整逆。

## 4. 全部低阶系数回填与原式验证

设新 leading 参数为 $z$，旧 $R_3,R_4,R_5$ 的参数分别为 $y_3,y_4,y_5$。必须在原第五 cochain 的 $z$ 组合上同时加入

$$
s^3T_2y_3+s^2T_3y_4+sT_4y_5.
\tag{4.1}
$$

这三个完整多项式分别产生 (2.4) 中的 $R_3y_3,R_4y_4,R_5y_5$。最后还加入 $\lambda_5$ 的 $Qb$ 校正，并取

$$
\lambda_6=(x,N_{\mathrm h}a).
\tag{4.2}
$$

各组纯切向分量及所有较低阶系数均实际保留。输出十七条 cochain 的完整临时矩阵尺寸为 $18323\times17$，随后逐阶核验原零至六阶方程，核验坐标总数为

$$
7\cdot6188\cdot17=736372.
\tag{4.3}
$$

## 5. Smith 指数与 $K_{107}$

记原零点十四个正 Smith 指数为 $a_i$，$c_j=\#\{i:a_i\le j\}$。由 (1.2)，

$$
(c_1,\ldots,c_6)=(4,4,5,8,9,10).
\tag{5.1}
$$

此前真实第七、八页仍给 $c_7\le12,c_8\le13$。所以

$$
\begin{aligned}
\delta_{4354,0}
&=\sum_{j\ge0}(14-c_j)\\
&\ge14+10+10+9+6+5+4+2+1=61,
\end{aligned}
\tag{5.2}
$$

而

$$
\begin{aligned}
\delta_{4353,0}
&=\sum_{j\ge0}\max(13-c_j,0)\\
&\ge13+9+9+8+5+4+3+1=52.
\end{aligned}
\tag{5.3}
$$

[完整模 $31$ 仿射公因子结论](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md) 给特征零总阶上界 $66$。由最大与次大 determinantal 阶之差，

$$
a_{\max,0}\le66-52=14.
\tag{5.4}
$$

此前真实第八头仍给 $a_{\max,0}\ge9$。此处没有把模 $31$ 的最大指数 $11$ 当作特征零上界。

保留其他有限点的既有因子，得到

$$
\begin{aligned}
K_{107}
&=s^2K_{105}=s^{47}K_{60}\\
&=s^{61}(s-2)^9(s+6)^9F_+(s)^2F_-(s)^2E_8(s)^2.
\end{aligned}
\tag{5.5}
$$

其次数为 $107$，首项系数仍为 $5^6$。

## 6. 当前同选定子式的条件费用

保持无穷远阶 $130/125/125$，令 $q=D/K_{107}$。由完整所选模 $31$ 子式次数 $8527$ 及原齐次上界 $8770$，

$$
8420=8527-107\le\deg q
\le8770-130-107=8533.
\tag{6.1}
$$

原完整来源降度构造的三支费用为

$$
\begin{aligned}
\text{非基来源}&\le8533-1+45=8577,\\
\text{基来源转移}&\le8770+55-125-107-11=8582,\\
\text{目标分支}&\le8770+64-125-107-10-8420=172.
\end{aligned}
\tag{6.2}
$$

所以在原目标 $h_0t_\nu$ 属于原十七式 $\mathbb Q[s]$ 像的前提下，完整来源费用可取 $8582$。该成员性仍是前提，本次并未提供新的全局目标来源。

## 7. 首次非零平方读数及其局部含义

原目标

$$
t_j(s,m)=
\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2
\tag{7.1}
$$

在真实共动坐标中为 $n_j^2$，$j=2,\ldots,10$。本次所有十七条输出中，$\lambda_0,\ldots,\lambda_5$ 的九行平方读数仍逐项为零；但 $\lambda_6$ 的读数不再全零。

实际回执的首个非零项为目标 $j=2$、零基 headColumn $3$：

$$
c=
-\frac{
111154350080767296248270240401288879899521541562317992253647443265275919531
}{
13662588162871007048638920213136151690096801820082359115211341824000
}
\ne0.
\tag{7.2}
$$

对应真实 cochain 满足

$$
M(s)\lambda(s)=O(s^7),\qquad
\langle\lambda(s),t_2(s)\rangle=c\,s^6+O(s^7).
\tag{7.3}
$$

因此未乘 $h_0$ 的 $t_2$ 不属于本原有限 Macaulay 来源模块在 $\mathbb Q[[s]]$ 上的像：若存在该模块中的形式来源，则 (7.3) 的右侧必须被 $s^7$ 整除。

原待检目标还含

$$
h_0=s^3(s-2)F_+^2F_-^2E_8,\qquad
[s^3]h_0=-917294284800\ne0.
\tag{7.4}
$$

[原整数模型源码](../notes/2026-11-14-r150-ninth-first-integer-model-789f.py)给 $F_+(0)=-8,F_-(0)=864,E_8(0)=9600$，故 $[s^3]h_0=(-2)(-8)^2\cdot864^2\cdot9600=-917294284800$。

故同一配对对 $h_0t_2$ 的首个已知非零项在 $s^9$，系数为 $-917294284800\,c$。当前只已证明左残差为 $O(s^7)$，所以这不构成 $h_0t_2$ 的成员性障碍。后续若将同头延拓到足够阶数，还必须保全部旧像引起的系数改变，并重新读取原目标配对；不能把 (7.2) 未经运输地固定到新的代表。

本段只涉及原 R150 有限来源构造，不给原无限维不变子空间问题的结论。

## 8. 实际运行与可恢复身份

实际运行：

- run：43702348535；job：132776011109；
- step：zero-complete-sixth-full-incoming；
- 执行来源提交：b2dacea985a0eec5f7d16193d4ecd826efbd6d7e；
- 数学耗时：约 $22.7365$ 秒；
- 通用源码 SHA256：9bf405d3aa65d40a8ebeb3fc87f3e8bd686814db371657abe9794f92e59099b8；
- 原始小回执：$56301$ 字节，SHA256 为 767de0208f98dd6f899af8fa85fca84be98c5820a4c10dafaf50f24b9d09f698；
- 主线外回执：$63216$ 字节，SHA256 为 f034a67070f31d23288e606d444ad59f9f97f4e33a85f2f2fde85d501001823e。

| 对象 | 尺寸 | 逻辑 SHA256 |
|---|---:|---|
| 全部新原第六 forcing | $6188\times8$ | c865da51719e6a5b4b2e0c20103617920fe4c47871e4f2f6d03f2b08db68c3c2 |
| 全原低行 Schur | $1088\times44$ | ea23f6000fe5987d47a7104e9bd25366e2567fae31f1fd087d5aa527b7088d4c |
| 完整低核 | $636\times46$ | 683e0f5a0f1d0ba6c81bb56baf44e59dcdaad8e9aafe822f3c03276d438cb1dd |
| 全部十七条第六 cochain | $18323\times17$ | 7d38e1062c21fdcc4e01bf263a1fb4386091f552f7e9505e176a1b6c33912d68 |
| 第六系数九平方读数 | $9\times17$ | 8c9c2c45e5520aad475980368abb760a032b3d25d0d0fe17114eae764f2a2f69 |

临时检查点 binding 为 c278a4da4cff21dd01533794e03cf8cb4190daa60efa5d485a2cf3eb706688d0；manifest 为 $23671$ 字节，SHA256 为 f3ef0821156151cee429a2556641c3170b12a09bcd1746eda7b345ac7e54bd35。完整数组只保存在同 job 临时工作区；Git 保存源码、参数、运行身份与小回执。

下一完整第七页保留 $W_6=W_5+R_6(K_5)$。它复用四十四个旧实际 RHS，只需对当前完整十七头中的七个非 exact 头构造新的 forcing；低矩阵列数为 $643$，旧 incoming 秩为 $590$，其零 leading 参数纤维维数为 $636-590=46$。所有新高行与原七阶产品仍须实际核验后才能报告下一连接秩。
