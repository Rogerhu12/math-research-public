# 同一原 Koszul 外支撑矩阵的模 31 完整 Smith 长度 149

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。
日期：2026-11-15。

## 1. 本次已完成的结论

固定同一自然参数 $u=1/s$、原十七式的权齐次化、原输出集 $I$ 和原来源集 $J$。令

$$
A(u)\in\mathbf Z_{(31)}[u]^{4367\times6188},
\qquad B(u)=A(u)[I,J]\in\mathbf Z_{(31)}[u]^{4354\times4354}.
$$

令 $\Phi(u)$ 为 $136$ 个标准来源 $F_j e_i-F_i e_j$ 各乘
$1,m_0,\ldots,m_{10}$ 所得的 $1632$ 列，并令

$$
O(u)=\operatorname{pr}_{J^c}\Phi(u)
 \in\mathbf Z_{(31)}[u]^{1834\times1632}.
$$

这是固定的常数及一次乘子 Koszul 族；没有把它扩大为整个 Koszul 模。
原来源身份为 $A\Phi=0$，每个 $J^c$ 原来源坐标均保留。

本次实际计算在 $\mathbf F_{31}[[u]]$ 上给出

$$
\operatorname{rank}O(0)=1603
$$

以及全部 $29$ 个正 Smith 指数

$$
\boxed{
1^{\,2},\quad
2^{\,10},\quad
3^{\,3},\quad
4^{\,3},\quad
5,\quad
6,\quad
8^{\,2},\quad
9,\quad
10^{\,2},\quad
11,\quad
12,\quad
13,\quad
14.
}
\tag{1.1}
$$

指数记号中的上标表示重数。因此

$$
\boxed{
\sigma_{31}(O)=149,\qquad
a_{\max,31}(O)=14,\qquad
\operatorname{rank}
 \bigl(\operatorname{coker}O/\operatorname{tors}\bigr)=202.
}
\tag{1.2}
$$

这是完整谱，而非截至某一位的下界。没有未定正指数。

本次没有计算 $O_{\mathbf Q}$ 的完整 Smith 谱，也没有证明原所选多项式子式
$D(s)$ 的最高系数为 $31$ 单位。实际回执相应字段
characteristicZeroSmithComputed 与 leadingCoefficientUnitProved 均为 false。

## 2. 实际运行与原输入身份

实际运行是：

- Actions run：43731615668；
- step：koszul-outside-minimal-original-field-through21；
- execution source：e238d925a11a50a0098ffda39ce243c4afbfeda6；
- 数学耗时：$13.088630369999919$ 秒；
- step 墙钟：$13.202008035999938$ 秒；
- 请求预算：$180$ 秒、$1024$ MiB；
- 退出码：$0$；
- Python-flint：0.9.0；
- 原完整临时回执：$15832$ bytes，
  SHA256 eeddfe8782d06338d15d834bdf387de5cd2f85d8334415f59411d24bfca244a6。

实际小摘要见
[本次运行回执](../notes/r150-full-infinity-dual27-session-789f/43731615668-koszul-outside-minimal-original-field-through21.json)。
执行源码为
[最小原外支撑 Smith 程序](../notes/2026-11-15-r150-koszul-outside-minimal-field-smith-selector-789f.py)，
$24174$ bytes，SHA256
c4b92e5db24165f2d0e1f36f20759a9554239c2aaba84f73984e154604e7f161。

四个实际输入分别为：

| 输入 | bytes | SHA256 |
|---|---:|---|
| 原 native 模型 | 128145 | 291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6 |
| 原 primitive 整数方程 gzip | 65159 | 44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe |
| 同一所选原子式字典回执 | 75700 | 5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68 |
| 已完成的所选 $B$ 至 $32$ 次摘要 | 26242 | e57d4bc56bbd50e1d1700b819a3f5f6499c92b885788ec3fe55089b5a6755657 |

本次语义 binding 为
87f3d53e716c7aa48e29e8089a33944ef72a7a9b7f56ebd8f64ed10c89be3886。
同一原 $J$ 的字典 SHA256 为
130984d8bba68b633607c25a6610bb6bdb2cb6c8bc1d536d6ed31ab7b2dda4f9。
它逐项对应已付所选子式 binding
43124d7d621b24353e3686cb1db8932ee6259822f22c1dbb1f8e0cd1d7b54600。
因此这里的外支撑并非换了一组较方便的原来源列。

本次重新读取历史原模型和小摘要，未使用已经结束的旧 session 临时文件；
未重复旧 $1603$ 阶有理求解、旧 $4318$ 阶消元或原正常形计算。
所有可由源码和参数重建的大数组仅留在当次 job 临时目录，未提交 Git 或 Release。

## 3. 原来源层的完整核验

程序从原 primitive 系数和 native 模型构造自然 $u$ 系数，实际核验全部
$4433$ 个参数系数身份。随后直接形成 $\Phi$ 和 $O$，其原自然次数不超过 $10$。

在 $O(0)$ 中实际选取 $1603$ 个原行及 $1603$ 个族列，并核验对应方块的完整逆。
取其余 $29$ 个族坐标为自由块，构造规范常数核 $X_0$：

$$
O_0X_0=0,\qquad
(X_0)_{\mathrm{free}}=I_{29}.
\tag{3.1}
$$

实际验证包括：

1. 全部 $1834$ 个外来源行上的 (3.1)；
2. $\Phi_0X_0$ 的全部 $6188$ 个原来源坐标，以及 $J^c$ 上全零；
3. 在原 $36$ 个所选自由来源坐标上的秩为 $29$；
4. 原 $4367$ 个输出上的全部
   $4367\cdot29=126643$ 个乘积坐标为零。

这里第 4 项是完整原矩阵乘回，不是仅在 $I$ 中乘回，也不是仅以某个商坐标
为零代替原来源身份。回执中的 all126643OriginalConstantSourceProductsZero、
allOriginalSelectedSourceSupportVerified 和 all29OriginalConstantSourcesIndependent
均为真。

还可由这些实际数据直接核验 $\Phi_0$ 满列秩 $1632$：
若 $\Phi_0c=0$，则 $O_0c=0$，故 $c=X_0d$；
第 3 项再迫使 $d=0$。因此原 $1632$ 列族的常数独立性也在本次原字典中核对。

这一步付清的是有限域常数来源。它不重新解释旧有限域预基系数为有理数，
也不把有限域的 $29$ 列直接登记为新的特征零来源。

## 4. 真单位消去及全部外支撑系列

记本次选取的单位行集为 $R$，单位族列为 $C$，其余族列为 $F$。
设 $U_0=O_0[R,C]$。固定自由块为 $I_{29}$，对 $k\ge1$ 取

$$
(X_k)_F=0,\qquad
(X_k)_C=-U_0^{-1}
 \left(\sum_{i=1}^{\min(10,k)}O_iX_{k-i}\right)_R.
\tag{4.1}
$$

于是 $(O(u)X(u))_R=0$ 在实际计算的每一位成立。
所有其余原外来源行组成 $231\times29$ 真 Schur 系列

$$
S(u)=\bigl(O(u)X(u)\bigr)_{R^c}.
\tag{4.2}
$$

程序没有只取与旧目标有关的若干行。每一层均保存并绑定完整
$1632\times29$ 族来源、$1834\times29$ 外支撑残量和
$231\times29$ Schur 系数，并实际核验全部 $1603$ 个单位行消去为零及
全部 $29$ 个自由族坐标。

本次实际计算至 $u^{21}$，包含该次系数。原来源与残量的每层 SHA256
以及完整层账本 SHA256 均写入小回执；其中完整层账本为
$12725$ bytes，SHA256
7296eb2086bfd367824c120cb65ecf815affefb448516dea053d1e3b4a48e6f8。

逐次对真 Schur 系列的常数单位块消去、再除 $u$，得到下表：

| 正指数 | 本次付清的重数 |
|---:|---:|
| 1 | 2 |
| 2 | 10 |
| 3 | 3 |
| 4 | 3 |
| 5 | 1 |
| 6 | 1 |
| 7 | 0 |
| 8 | 2 |
| 9 | 1 |
| 10 | 2 |
| 11 | 1 |
| 12 | 1 |
| 13 | 1 |
| 14 | 1 |

至指数 $14$，全部 $29$ 个非单位列已付清。剩下的 $202$ 行给自由余核；
没有继续把它们当作待发现的正指数。

[原外支撑扭子模注入证明](R150-appendix-koszul-outside-torsion-embedding-and-selected-minor-test.md)
还给出本次预定截止的独立依据：
$\operatorname{tors}\operatorname{coker}O$ 注入同一 $B$ 的余核，
而已付 $B_{\mathbf F_{31}}$ 最大正指数为 $21$。
本次实际系列与单位乘回仍是结论的必要数据，不能用这个先验截止替代。

## 5. 特征零的准确推论

在 $\mathbf Q[[u]]$ 上，同一 $O_0$ 的秩 $1603$ 和 $\Phi_0$ 的秩 $1632$
已由原真有理来源证明；本稿不重复那些计算。因此 $O_{\mathbf Q}$ 同样恰有
$29$ 个正 Smith 指数，记其总和为 $\sigma_{\mathbf Q}$。

取实现 (1.2) 的某个原 $1632$ 阶子式。其 $u^{149}$ 系数模 $31$ 非零，
故这一同一整数子式在特征零中的消失阶至多 $149$。所以

$$
\boxed{29\le\sigma_{\mathbf Q}\le149.}
\tag{5.1}
$$

右边是总长度的上界。它不证明 $\sigma_{\mathbf Q}=149$，也不证明
$a_{\max,\mathbf Q}\le14$。一般而言，最大 Smith 指数是相邻两个
确定子式阶之差；分别拥有它们的上界不能直接对这个差取上界。

本次 (1.1) 不补付旧固定二十九条未校正曲线的一阶外支撑计算。
旧结论仅说明固定常数线性组合不能使其一阶外支撑为零；
本次则允许 (4.1) 中全部原族的高次系数纠偏。两者量词不同，结果相容。

## 6. 与完整原矩阵新有限域谱合读时的路线边界

独立的
[完整原矩阵无穷远双核回执](../notes/r150-full-infinity-dual27-session-789f/43731615668-full-infinity-original-dual27-v2-through21.json)
已经实际得到

$$
\delta_{4354}(A_{\mathbf F_{31}})=66.
$$

它是同一原自然参数、完整 $4367\times6188$ 矩阵的长度。
同一原子式首系数提升只给
$\delta_{4354}(A_{\mathbf Q})\le66$。结合 (5.1)，

$$
\delta_{4354}(A_{\mathbf Q})+\sigma_{\mathbf Q}\le215<243.
\tag{6.1}
$$

因此，只靠“完整原矩阵 torsion 长度加这个固定 Koszul 族的外支撑长度”
这一项下界，即使把两者的特征零谱都算准，也不足以达到同一所选 $B$
的有限域长度 $243$。原扭子模证明中的条件判据仍正确，但对这个固定族
仅用上述两项已不能满足其阈值。

(6.1) 不是 $v_u\det B_{\mathbf Q}\le215$ 的结论。
所选输出投影，以及完整原核中超出这 $1632$ 列族的自由商，仍可能贡献额外阶。
有限域中差额为

$$
243-66-149=28.
$$

定位这 $28$ 的来源是后继的具体小接口；不能把它略去，也不能从 (6.1)
断言原最高系数非单位。当前原特征零多项式目标成员性、最高系数单位性及其
完整来源证书，均保持各自尚待支付的范围。
