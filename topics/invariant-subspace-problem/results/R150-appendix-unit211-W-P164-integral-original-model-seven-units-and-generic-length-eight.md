# R150：P164 完整原整模型的七个单位块、两个保留主分量与泛型八维上界

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

唯一实际 run46094057077 / job140821285456 已完整执行：11.524541746 秒、峰值 RSS 125440 KiB、内层退出码 0。完整 97 维权模型、同点 lambda 六次和 z 二次、全部 132 原列均成功；九个有限域 primary 中七个实际返回原单位 1，另外两个完整二重一次主分量均只有模其剩余域秩 10，未返回单位。

**严格新结论。** 完整原 I11 的局部有限 A 模由至多 8 个元素生成，故其 QQ(k) 泛型商维数至多 8。没有得到全局单位或 QQ(k) 泛型空，也没有得到全 W 零维。两个未决主分量和全部重数保留；本次并无资源失败。

## 1. 两项已成前提，及真正的新目标

已完成 [P164 的完整整特化与无竖直分量定理](R150-appendix-unit211-W-native-P164-integral-specialization-no-vertical-component-and-local-weight-model.md) 给出：

$$
A=\mathbf Z_{(1009)}[k]_{(1009,k-3)},\qquad
B=A[e]/(\widehat P),\qquad \deg_e\widehat P=97,
\tag{1}
$$

其中 $\widehat P$ 首一，B 在 A 上有限自由，秩 97。整个模极大理想的 P 定义精确已返回，首一模式 SHA-256 为 ebe334f55739f723b57d093e4b990bdf53e2be2b05758edce7324d98ab5c7b93，包含全部重数。真 P 没有 QQ[k] 非恒定内容。原 native 身份为 $\det M=cUP$，U 在当前原权图已付；由真实值列首坐标为 1，adjugate 直接给出 $\det M\in I_6$，因而 $P\in I_6$。所以 (1) 没有加入一个缺少原理想来源的额外曲线。

本次未重算旧 QQ 二参数 determinant、三条 QQ 竖直切片、完整 QQ 特征多项式或先前大 cofactor。仅从原必要前缀重建 (1) 的模多项式及原坐标定义，再将完整原 I11 同态代入。这个新模型已实际完整构成，原单位目标只在下述七个 primary 中完成。

本次故意不以模 D 幂为目标。模 p 下 D 为零或幂零不能单独推出 QQ 下 D 为零；若未返 1，一律保留未决支。

## 2. 所有系数必须在 B 上真实有定义

由 (1) 可得

$$
\overline B=B/(1009,k-3)B
=\mathbf F_{1009}[e]/(\overline P_{97}).
\tag{2}
$$

对每一个出现的原 QQ 有理多项式 n/d，源码仅把分子、分母同时乘一个非零 QQ 常数，使 d 的 p 内容为零。随后实际检查完整分子和分母的每个系数 p 整；完整分母在 (2) 中必须返回真实乘法逆：

$$
s\bar d+t\overline P=1,\qquad \bar d\,s=1\ \text{in }\overline B.
\tag{3}
$$

所有式 (3) 都在整个 97 维代数中，不是只选一个好因子。由 B 在 A 上有限自由，乘 d 的 cokernel 是有限 A 模。式 (3) 令其模极大理想为零，Nakayama 引理给出该 cokernel 为零；所以 d 本身在 B 中是单位。这个论证保留全部重数。

若任何分母或 p 整性条件失败，源准确报告阻碍及真实 gcd，整个阻碍支持保留，不把“当前物理分母非零”误当它在整模型中自动可逆。没有几何 D、lambda 首项或未付范数逆。

## 3. 同一个原 lambda 的首一六次环境

原 native 六生成元为

$$
v=(1,x,y,t,y^2,yt)^T.
$$

旧原三轴乘法关系给出 $x_iv=M_iv+E_iF_4$。原 lambda 是这三轴的已付仿射式

$$
\lambda=\alpha_0+\alpha_1x+\alpha_2y+\alpha_3t.
$$

因此

$$
M_\lambda=\alpha_0I+\sum_{i=1}^3\alpha_iM_i,\qquad
E_\lambda=\sum_{i=1}^3\alpha_iE_i,
$$

$$
(\lambda I-M_\lambda)v=E_\lambda F_4.
\tag{4}
$$

源实际返回 (4) 的六个完整原多项式身份及全部权分母。对这个单一矩阵的通用 adjugate 身份给出已刊原关系

$$
\chi(\lambda)=\det(\lambda I-M_\lambda)\in I_4,\qquad\deg_\lambda\chi=6,
\tag{5}
$$

首项为 1，不假设 v 是自由基。由第 2 节，$M_\lambda$ 的系数在 B 上有定义，所以 $\chi\in B[\lambda]$。本次只在 (2) 的整个代数中按同一通用 Faddeev 公式构造 (5) 的准确模像，实际返回六步及最终 B6=0。整数 1 至 6 均为 p 单位。没有重跑旧 QQ 特征系数或剥 lambda、lambda−3/2。

于是

$$
B_\lambda=B[\lambda]/(\chi)
\tag{6}
$$

在 A 上有限自由，秩 582。

## 4. 保留整 H198 支范围的首一二次及完整原坐标

在此前 H198 非零补图，

$$
n=p_0+p_1x+p_2y,\quad
p_1=a\lambda+b,\quad p_2=c\lambda+d,\quad
\Delta_N=ad-bc,\quad z=ax+cy.
$$

当前模型要求 $\Delta_N$ 也由第 2 节在完整 (2) 中实际返单位，才可使用

$$
x=(p_2z+cp_0)/\Delta_N,\qquad
y=(-p_1z-ap_0)/\Delta_N.
\tag{7}
$$

这只是使当前补图在整模型中有定义；没有把 H198=0 当成全 W 单位。

已完成的原关系是

$$
q_z=z^2+\beta_1(\lambda)z+\beta_0(\lambda)\in I_4.
\tag{8}
$$

两系数的分母同样受第 2 节检查。定义明确自由环境

$$
C=B_\lambda[z]/(q_z).
\tag{9}
$$

C 的 A 秩为 $97\cdot6\cdot2=1164$，其 B 基为 $\lambda^jz^\epsilon$，$0\le j<6,0\le\epsilon<2$。这只说环境自由，绝不说原方程商自由。两个首一关系的所有根和重数都保留。

模模型中，源码实际核 (7) 的 n=0、z=ax+cy、首一 qz=0，并恢复原 t。还实际检查原 old-lambda 在同一点的值等于模型中的 lambda；不是将两个独立值变量混同。原 N1 及 qz 对三条均值的真实组合在这个模型中再次乘回。

## 5. 全部原 I11 的直接同态像

完整理想的定义沿 [原 I11 精确二十行二列定理](R150-appendix-unit211-W-H198-complement-exact-twenty-two-full-original-values-and-two-scalars.md)：

$$
I_{11}=(E_1,E_{B,e},E_{B,o},N_1,N_S,P_S,
q_{T,4},R_6,N_{\rm low},P_{\rm low},V_{\rm low}).
\tag{10}
$$

本次直接将完整原多项式同态映入 (9)，不再展开旧二十行系数或任何 QQ 大 cofactor。前三均值、N1、NS、PS 保留全部原表达式；新五个值仍完整保持

$$
\begin{gathered}
m=u-\ell,\quad \delta=1-Q,\quad M=4bc\delta,\\
A_2=2\lambda^2-2\lambda+1,\quad B_3=4\lambda^3-6\lambda^2+3\lambda-1,\\
D=\ell A_2-T^2,\quad K=\ell^2B_3-3\ell TA_2+2T^3,\\
R_6=MK^2-4m^2D^3.
\end{gathered}
\tag{11}
$$

qT4 为此前完整 C4 除已付纯权首项；Nlow、Plow 保原 $N_4(\mathrm{row}_B)$、$P_2(\mathrm{row}_B)$ 的完整 rho 奇部；Vlow 保整个 $N_4(V)$，没有换成 Phi 倍数。源码从原 Gram 定义这些基量，并实际核 V0/V1 三个二次型系数的 rho 奇部全零。所有公式与已经实际成功的 I11 源逐项相同，只将算术环境换成 (9)。没有除 D 或从模 D0 外推物理排空。

令 $g_1,\ldots,g_{11}$ 为 (10) 的完整像。因为 (9) 有上述十二个 B 基元，理想 J 的 B 模像精确由

$$
\{g_i\lambda^jz^\epsilon:1\le i\le11,\ 0\le j<6,\ 0\le\epsilon<2\}
\tag{12}
$$

生成。故新原矩阵恰为 12 行、132 列；这是完整理想的有限模呈示，不是只挑若干必要交换子。lambda 与 z 的乘法来自真正的两个首一商，所以没有裸矩阵交换或结合性的假设。

## 6. 全部主分量、真原乘回与 CRT

源码完整因式分解准确 $\overline P$，实际核出乘积含每个原重数。每个有限域因子的不可约性由完整 Rabin 条件再明确检查，不把该因子当成 QQ 因子。

在每个完整 primary 代数

$$
\mathbf F_{1009}[e]/(f_i^{m_i})
$$

内，从 (12) 的原列尝试选出十二列。所有主元均以真实扩展 Euclid 求逆、实际返回 1；选列成功后，源码实际核十二个目标基向量的全部 144 个原矩阵乘积。若某主分量不能满射，完整该分量保留，不扩大资源、换素数或换顺序重跑。

若全部主分量都成功，再实际构造 CRT 幂等元：逐个核幂等、交叉乘积为零、总和为 1。将各块常数目标的原组合提升回整个 (2)，最终再返回十二个坐标：

$$
\sum_{j=1}^{132}c_j\,\operatorname{column}_j=(1,0,\ldots,0).
\tag{13}
$$

只有 (13) 真正完成才报告整体原单位返回。矩阵、乘子的大系数只留定义与 SHA，不保存或传送载荷。

## 7. 真实完成的主分量返回与未完成的全单位目标

整个模型实际有 67 个权逆，均在完整 $\overline B$ 中返回 1；30189 个有理系数完成 p 整性检查。真同点 $\chi$ 的六步 Faddeev 和 B6=0 完成，其准确模定义为 2296 字节、SHA-256 03a5a5dad07464f05d9208f2e7f84b545a64b426a0e9616a8ee239c324f70b32。完整 12×132 原列于 11.317778404 秒完成，599448 字节定义的 SHA 为 5b3c4d986b673f6a6a30733145793233861a9b305eba6d25b82ad5fd4b1340d7。

完整分解、Rabin 条件和含重数乘积均实际返回：

| primary index | 不可约次数 | 原重数 | primary 的 Fp 维数 | 矩阵模剩余域秩 | 完整 primary 原单位 |
|---|---:|---:|---:|---:|---|
| 0 | 1 | 1 | 1 | 12 | 已返回 |
| 1 | 1 | 1 | 1 | 12 | 已返回 |
| 2 | 1 | 2 | 2 | 10 | 未返回，整支保留 |
| 3 | 1 | 2 | 2 | 10 | 未返回，整支保留 |
| 4 | 1 | 1 | 1 | 12 | 已返回 |
| 5 | 5 | 1 | 5 | 12 | 已返回 |
| 6 | 7 | 1 | 7 | 12 | 已返回 |
| 7 | 23 | 1 | 23 | 12 | 已返回 |
| 8 | 55 | 1 | 55 | 12 | 已返回 |

各维数之和为 97。七个满秩块均仅由原 E1 的十二个真实基倍就已选出完整原列，全部 144 个矩阵乘积实际返回；不是只看一个 determinant 非零。两块 rank10 都完整遍历了全部 132 列才结束。它们仅在模其最大理想的剩余域上秩为 10；不能把这句话改成整个二重 primary 的 cokernel 维数已经恰为 2 或 4。

两个未决一次因子的定义 SHA 分别为

- index2：0e2ca59eb1ba5cd7c67221120200547afbaa9f137206e2940fcfe4b608d30dbe；
- index3：7991d9aecc5b33c423608ce58f4809610c92e69b2cdbd3cf9cc9334991f2fe41。

这两个是 Fp[e] 因子，不是 QQ 曲线因子。因为未全部返回单位，源码没有执行第 6 节最后的整体 CRT 单位断言，也没有报告 QQ(k) 泛型空。没有换素数、k、顺序或预算重跑。

## 8. 已经成立的局部八生成与 QQ(k) 上界

记

$$
\mathcal M=C/J,
$$

其中 C 是 (9) 的有限自由 A 环境，J 由完整 (10) 生成。$\mathcal M$ 是有限 A 模，不要求自由。

在 $\overline B$ 的七个已单位 primary 上，$\overline{\mathcal M}$ 为零。两个剩余 primary 分别为

$$
B_i=\mathbf F_{1009}[e]/(f_i^2),\qquad\deg f_i=1,\quad i=2,3.
$$

每个矩阵在 $B_i/(f_i)$ 上的秩为 10，所以对应 cokernel 模最大理想的维数是 2。对有限局部 Artin 环 $B_i$ 使用 Nakayama，这个 cokernel 由至多两个 $B_i$ 元素生成。因为 $B_i$ 的 Fp 维数是 2，它的整个 cokernel 的 Fp 维数至多 4；这一步完整保留平方幂，没有假定它自由。

因此

$$
\dim_{\mathbf F_{1009}}
\bigl(\mathcal M/(1009,k-3)\mathcal M\bigr)\le4+4=8.
\tag{14}
$$

在 A 的剩余域中取至多八个生成元并任意提升到 $\mathcal M$，再次使用有限模块 Nakayama，得到

$$
\mathcal M\ \text{在 A 上由至多八个元素生成}.
\tag{15}
$$

令 $K=\operatorname{Frac}(A)=\mathbb Q(k)$，由 (15) 可严格推出

$$
\boxed{\dim_K(\mathcal M\otimes_AK)\le8.}
\tag{16}
$$

这是特征零的真实泛型上界，不是将两个模线性因子当成 QQ 因子。它仍允许正维权曲线、有限 k 纤维的跳跃，以及任何未完成的原几何条件。

若进一步只看当前物理 D 非零的固定规范原点，$x,y,t$ 由 (7) 和原 lambda 线性式恢复；加 $\rho^2=1-Q$ 至多再乘 2，而完整两矩条件在已付 $m,\ell,D$ 上唯一恢复

$$
\zeta=\frac{T+uK_{\rm moment}/(2mD)}{\ell},
\qquad K_{\rm moment}=\ell^2B_3-3\ell TA_2+2T^3.
$$

(16) 的 K 代数是有限维 Artin 代数；后续原权或几何局部化只删除分量，取额外原条件的商也不增维。因此该固定规范完整原坐标在 QQ(k) 上有至多 16 维的泛型环境。这仍是泛型 k 结论，不能当作全 W 有限点界。整 H198=0 已有独立有限交结论，不贡献 QQ(k) 泛型点；它在具体有限 k 的原点仍全部保留。

## 9. 新几何线索的准确限度

把已知 W 权式写为

$$
u=e+1,\quad V=(e+1)k+2,\quad
\ell=\frac{(e+1)((k+2)^2-2ek)}{kV}.
$$

直接展开给出

$$
2\ell-1=-\frac{L_{1/2}}{kV},\qquad
L_{1/2}=4ke^2-(k^2+4k+8)e-(k^2+6k+8).
\tag{17}
$$

在固定 k=3、p=1009 下，$L_{1/2}=12e^2-29e-35$，且

$$
12e^2-29e-35=12(e-235)(e-356)\pmod{1009}.
\tag{18}
$$

两个首一因子分别为升序系数 $(774,1)$、$(653,1)$，其 SHA 正好等于第 7 节的 index3、index2。式 (18) 是完整二次因式身份；只说明实际残余权模支持与 $\ell=1/2$ 相符，**不证明**原 QQ 曲线是 $\ell=1/2$，不证明 $L_{1/2}^2$ 在真 P 中整除，更不支付这条权线。

后续须从这两个完整残余 primary 的真实商作用及 QQ(k) 原几何族证明相应归属。模 D0、模 lambda=1/2 或模 D 幂都不能单独外推 QQ。本次不以这些尚未完成的身份作数学输入。

## 10. 实际执行与来源

冻结源：

[2026-11-28-unit211-W-P164-complete-original-local-1164-model-8542.py](../notes/2026-11-28-unit211-W-P164-complete-original-local-1164-model-8542.py)

blob 18acba8c45b2cdb41c5d7f93a4118082a585c952；20952 字节，SHA-256 1dc4ded9c09f191ec06b3844bd8ad021660a90e3c6d966ffc7b6cdb6c0140c8b。固定 180 秒 / 4 GiB，全部定时器受同一初始截止约束。

唯一实际 run46094057077 / job140821285456，source commit 0e037f0f75fef919a6c5b7754814b51be6d2cb42。源最后标记 11.452289236 秒，驱动 11.524541746 秒、RSS 125440 KiB、内层退出码 0。它是完整返回了部分数学目标，不是超时、内存失败或实现异常。

2026-11-28 01:37:57.180913 UTC 真实 pull 后仍为同一 commit。两 README 的 blob 分别为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、5fbd905291dd044c88d35bd9c07ac0e586ff795a，均无差异。

stdout 10224 字节，SHA-256 9235cbde4446061e261c57586c1f2c6c6d1be7447ed67b1d11684dfca048664f。附 [实际小回执](../notes/2026-11-28-unit211-W-P164-original-local1164-seven-units-two-residuals-actual-receipt-8542.json)。没有保存、编码或分片传送矩阵或大系数。既成七个单位块不再重跑；两个未决主分量转入新的原几何返回。

普通无限维 ISP 与整个 W 均未完成。
