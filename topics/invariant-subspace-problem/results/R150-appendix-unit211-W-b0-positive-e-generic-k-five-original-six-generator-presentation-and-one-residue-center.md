# R150 补充：正 e 一般 k 的完整五原六元呈示及唯一剩余权中心

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127。日期：2026-11-29（Asia/Taipei）。

## 1. 完成结论及未完成范围

在正确 W/b0、剩余特征1009的
$$
v(e)>0,\quad v(k)=0,\quad\bar k\notin\{-2,-4,4\}
\tag{1}
$$
图上，本次唯一新联合原输入完成六元环境的准确十八列呈示、三个固定六阶 cofactor、以及完整五原方程的联合 Bézout。整个(1)的原解必须满足
$$
\boxed{\bar L=3/4,\qquad\bar\mu=-2,\qquad
\bar\lambda=1/2,\qquad\bar k=-8.}
\tag{2}
$$
这里 $L=(k+2)/k,\mu=2\lambda-3$。这是整个一般k原赋值图的剩余中心限制，尚不是该中心或整个正e射线的排空；物理f继续自由并须满足完整singleton条件。

前置的[物理f及全部Gram整性](R150-appendix-unit211-W-b0-positive-e-generic-unit-k-physical-f-integrality-and-singleton-model.md)、[正负四中心排除](R150-appendix-unit211-W-b0-positive-e-unit-k-exact-residual-quadratic-and-k-plus-minus-four-exclusion.md)、[完整首阶及六元纸呈示](R150-appendix-unit211-W-b0-positive-e-generic-k-complete-singleton-first-jets-and-six-generator-presentation.md)均已付清。本次没有重跑其旧门。

## 2. 同一点五个完整原条件

令
$$
A=\mathbb Z_{(1009)}[L,U^{-1}],\qquad U=L(L-1)(2L-1)(2L-3).
$$
(1)及已成边界证明保证这些因子的剩余均非零。原五条件次序固定为
$$
G=(q_{\rm raw},P_0,P_1,R,N),
\tag{3}
$$
其中
$$
q_{\rm raw}=\frac{h^3}{9}\mu^2-4h(L-1)\mu+2h^2-3,\quad h=3-2L,
$$
$$
P_0=[P_B]_0,\qquad P_1=[(N_B-P_B)/e]_0.
$$
后两式来自真实singleton原Gram，因原P02值项至少二阶且物理坐标整，均是同一点的必要式。

R和N始终为完整R6及完整N5的正则剩余。明确地，取
$$
M_0=2L-1,\quad m_0=1-L,\quad T=L\mu/3,
$$
$$
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2,
$$
$$
D=L A_2-T^2,\quad
K=L^2B_3-3L A_2T+2T^3,\quad
R=M_0K^2-4m_0^2D^3.
$$
从同一真实仿射恢复取 $V_0=[V_s]_0,t_0=[t_s]_0$，并置
$$
y_0=-V_0/M_0,\quad w=(\mu+3)/2-1-T,
$$
$$
z_1=-2(-L\mu+2T)y_0-2Lw+m_0Tt_0,\qquad z_2=-4m_0y_0,
$$
$$
Z_0=2(T-L\mu)(Lw+V_0T)+M_0t_0T^2/2,\qquad
N=2m_0D(Z_0+Dz_2)+M_0Kz_1.
\tag{4}
$$
$[G/Q]_0=[W_s]_0=0$ 已用于(4)的准确剩余；并未设物理f=0。没有D逆、新几何头逆或分别选择范数根。

实际原分子 profile：

| 原式 | L次 | mu次 | f次 | 总次 | 项数 |
|---|---:|---:|---:|---:|---:|
| qraw | 3 | 2 | 0 | 5 | 10 |
| P0 | 9 | 3 | 3 | 12 | 97 |
| P1 | 11 | 3 | 3 | 14 | 117 |
| R | 8 | 6 | 0 | 14 | 30 |
| N | 9 | 5 | 0 | 14 | 43 |

全部实际分母1009整，支持只在U。

## 3. 双首一规则和准确六行十八列

已付单位
$$
c_\mu=h^3/9,\qquad
c_f=16(2L-2)(2L-3)/(2L-1)^2
$$
给
$$
q_\mu=q_{\rm raw}/c_\mu,\qquad
P_0/c_f=\widetilde P_0+Wq_\mu,\quad\deg_\mu\widetilde P_0<2.
$$
$q_\mu$对mu首一二次，$\widetilde P_0$对f首一三次。所以
$$
B=A[\mu,f]/(q_\mu,\widetilde P_0)
$$
是真自由六元代数，基按
$$
(1,\mu,f,\mu f,f^2,\mu f^2)
\tag{5}
$$
排列。实际首一f式的分子次数为(L14,mu1,f3)、总16、102项，分母L13；其首一性及普通除法均返回。

每个G先除f后除mu，实际核
$$
G=r+\frac{Q_f}{c_f}P_0+
 \frac{Q_\mu-Q_fW}{c_\mu}q_{\rm raw}.
\tag{6}
$$
按种子 $P_1,R,N$ 各乘(5)，得到准确模呈示
$$
A[\mu,f]/(q_{\rm raw},P_0,P_1,R,N)
\simeq\operatorname{coker}(A^{18}\longrightarrow A^6).
\tag{7}
$$
其十八列、108个坐标和全部五原反传已在本次唯一运行中完成。自由性仅用于B；没有称(7)的真实商自由，也没有损失重根或幂零结构。

## 4. 三个固定原 cofactor

事前固定的零起始列组是
$$
[0,1,2,3,6,7],\quad
[0,1,2,3,12,13],\quad
[0,1,6,7,14,15].
\tag{8}
$$
对每组清全部实际旧分母，用整除Bareiss和反代返回全部六个伴随坐标；再经(6)合并五个完整原来源。只有U的旧支持从标量剥除，并同步运输到全部乘子。实际得到
$$
C_j(L)=\sum_{i=0}^4\Omega_{ji}G_i.
\tag{9}
$$
这些是普通完整原身份；不把矩阵主元或新权头当单位。三个固定矩阵本次全部非奇异。

| j | 清分母原det的L次 | 剥除旧U支持次数 | 最终Cj的L次 | 项数 |
|---|---:|---:|---:|---:|
| 0 | 150 | 94 | 56 | 57 |
| 1 | 149 | 90 | 59 | 60 |
| 2 | 145 | 103 | 42 | 43 |

最终普通QQ标量的规范SHA-256依次为：

- da83a10effcd818eed98fc72f587fb830759279cd40d5ceea328292ae5e07d12；
- 91f2be2249c2d748f35d85327e9fd8746ee4ef4dfb9a58e7584722ce3c9b0e63；
- 7b6907419e1368acddc59c682387e9c41c0ea5edbc1ae78ea2690f376f99b63e。

实际(9)中P0、P1的最终乘子恰为零。记录这一点以明确本次三个选定标量尚未检验剩余中心的f条件；它不损害完整(7)的准确性，也不允许据此删除原singleton方程。

## 5. 第一次联合 Bézout 及唯一剩余中心

只对本次(9)的新标量执行事前固定的 $\mathbb F_{1009}[L]$ 联合Bézout。实际完整返回
$$
\sum_j b_j(L)\bar C_j(L)=g(L),
$$
其中没有剩余U因子需要剥除，且
$$
\boxed{g(L)=L+756=L-\frac34\quad\hbox{于 }\mathbb F_{1009}[L].}
\tag{10}
$$
该首一线性式的规范短系数串为[756,1]，7字节SHA
**1cbb585123b5558ee2312aef2673b3023806b2a7ff22184ada18c63d3d9918cd**。
用实际已经返回的长度和摘要识别这个单一小标量；没有重启源码或重新计算任何门。

把b_j的普通提升合并(9)，程序对全部五个原有理多项式逐系数返回
$$
\sum_{i=0}^4\Theta_iG_i=L-\frac34\pmod {1009}.
\tag{11}
$$
所有最终乘子分母只含原U支持且系数1009整，故(11)对(1)的任意原剩余点合法。实际q、R、N三乘子非零，P0/P1乘子零；全部五源都按固定次序检查，没有只凭gcd次数宣称单位。

因此 $L=3/4$。此时原qraw准确化为
$$
q_{\rm raw}|_{L=3/4}=\frac38(\mu+2)^2,
$$
剩余域是域，特征不为2或3，故mu=-2。再由原坐标得lambda=1/2、k=-8，即(2)。

这个推理仅确定原赋值的剩余域点，没有把含平方的理想替换为约化理想或从裸模空性提升QQ空性。该中心是否与P0/P1相容仍是下一不同原输入。

## 6. 唯一实际执行

[新五原联合源码](../notes/2026-11-29-unit211-W-positive-e-generic-k-five-original-six-generator-joint-input-8542.py)，
blob **8600631e1ed0289e4c2eb97fbd6883b99778b4b0**，
SHA **7b71964b8ab38500656d728002dc0dbc74c4a332f53bd5e2eea42538c36a8ada**。

[事前固定输入](../notes/2026-11-29-unit211-W-positive-e-generic-k-five-original-six-generator-joint-input-8542-input.md)保全部尺度、原来源和预算。

唯一[run46176848261](https://github.com/Rogerhu12/math-research-public/actions/runs/46176848261)，job141077382113：

- 固定120秒/1GiB、外135秒；实际 **0.43085872000000336秒 / 40908KiB / exit0**。
- 全部七条数学记录亲读；最后数学阶段0.3819493249999937秒。
- 37次首一除法、19次原模身份、108列坐标、18个cofactor坐标、25次五原返回、139次p整检查、60次有限域商余和5次Bézout返回全部成。
- stdout **18579B**，SHA **3652c07ee08dcb6fea8bc34f05e1197415f4f34b10def44ef5f397eed27ef9b0**；重组日志原数学行与driver的长度/摘要完全匹配。
- source commit **4c463f2f670730345fa93a36ba726cb189bbf707**；实际pull到 **0212de454a8c91a07c54f052e71d19a205f6a1d6**，UTC **2026-11-28 18:37:32.764848**，两README无变。

唯一依赖2f951只读取4750B必要Gram定义前缀，SHA
ce658823d68f6afba617d80088f5073fcccb79a3550509bce4b220f7a8d8f3b8。
AST排除旧顶层断言、计时器和后续证明循环；没有再执行旧四首阶的f结式、83e六射线门或任一冻结目标。

[小回执](../notes/2026-11-29-unit211-W-positive-e-generic-k-five-original-six-generator-joint-input-8542-execution.json)保存实际七记录的profiles/来源统计及driver身份，不保存系数载荷。本次只完成(2)的整图必要限制；其中心、其它内部DVR和普通ISP继续。
