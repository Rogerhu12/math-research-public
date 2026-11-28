# R150：P164 上完整原 I11 的 1164 维局部整模型首次输入

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。源尚未执行。

## 1. 两项已成前提，及真正的新目标

已完成 [P164 的完整整特化与无竖直分量定理](../results/R150-appendix-unit211-W-native-P164-integral-specialization-no-vertical-component-and-local-weight-model.md) 给出：

$$
A=\mathbf Z_{(1009)}[k]_{(1009,k-3)},\qquad
B=A[e]/(\widehat P),\qquad \deg_e\widehat P=97,
\tag{1}
$$

其中 $\widehat P$ 首一，B 在 A 上有限自由，秩 97。整个模极大理想的 P 定义精确已返回，首一模式 SHA-256 为 ebe334f55739f723b57d093e4b990bdf53e2be2b05758edce7324d98ab5c7b93，包含全部重数。真 P 没有 QQ[k] 非恒定内容。原 native 身份为 $\det M=cUP$，U 在当前原权图已付；由真实值列首坐标为 1，adjugate 直接给出 $\det M\in I_6$，因而 $P\in I_6$。所以 (1) 没有加入一个缺少原理想来源的额外曲线。

本次不重算旧 QQ 二参数 determinant、三条 QQ 竖直切片、完整 QQ 特征多项式或先前大 cofactor。仅从原必要前缀重建 (1) 的模多项式及原坐标定义，构造一个新的整模型：旧真首一 lambda 六次关系，再加旧真首一 z 二次关系，然后把完整原 I11 直接同态代入。目标仅为在这个完整有限模型中实际返回原单位 1。

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

完整理想的定义沿 [原 I11 精确二十行二列定理](../results/R150-appendix-unit211-W-H198-complement-exact-twenty-two-full-original-values-and-two-scalars.md)：

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

内，从 (12) 的原列选出十二列。所有主元均以真实扩展 Euclid 求逆、实际返回 1；选列成功后，源码实际核十二个目标基向量的全部 144 个原矩阵乘积。若某主分量不能满射，完整该分量保留，不扩大资源、换素数或换顺序重跑。

若全部主分量都成功，再实际构造 CRT 幂等元：逐个核幂等、交叉乘积为零、总和为 1。将各块常数目标的原组合提升回整个 (2)，最终再返回十二个坐标：

$$
\sum_{j=1}^{132}c_j\,\operatorname{column}_j=(1,0,\ldots,0).
\tag{13}
$$

只有 (13) 真正完成才报告整体原单位返回。矩阵、乘子的大系数只留定义与 SHA，不保存或传送载荷。

## 7. 若真返 1，允许的 QQ 推论

设 (13) 真完成且全部系数、分母检查通过。令 $C/J$ 为 (9) 中加入 (10) 后的商。它是有限 A 模；(13) 表示其模 A 极大理想为零。Nakayama 引理直接给出

$$
C/J=0.
\tag{14}
$$

因此在 A 的分式域 QQ(k) 上，真 P164 的完整原系统没有泛型解。这里使用的是已证明首一 e97、lambda6、z2 的有限自由多项式环境；不是从某个任意多元模空性推 QQ 空性。即使 C/J 不自由，有限模块论证仍成立。

P 无纯 k 内容的已成结论排除了整个竖直 P 曲线。其他正维权分量必支配 k，和 (14) 矛盾。因此该补图剩余原权支持零维；整 H198=0 已有独立有限交结论，合起来才可得全当前 W 的原权支持零维。仍可能存在有限权点及原几何点，必须继续同点返回；本门不声称整 W 为空，也没有凭空提供显式 QQ 单位乘子或有限 k 覆盖多项式。

若只得到余秩、坏权分母或模 D 幂，上述提升完全不适用，源明确不作 (14) 或零维结论。

## 8. 冻结源与准确资源

文件：

2026-11-28-unit211-W-P164-complete-original-local-1164-model-8542.py

源 SHA-256：

1dc4ded9c09f191ec06b3844bd8ad021660a90e3c6d966ffc7b6cdb6c0140c8b

固定 180 秒 / 4 GiB。所有必要前缀的 alarm、setitimer 都钳到同一初始绝对截止。只取已刊 P 模定义前缀与 N1 坐标前缀，跳过所有旧完成/冻结运算尾段。固定七件依赖：P164 整模型源、native 原六行源、原 C9 六规则源、I11 完整源、N1 slope 源、三均值源、physical-lambda 源。

本稿仅冻结数学输入及其条件推论。实际内层退出与完整原单位返回以唯一首次运行回执为准。
