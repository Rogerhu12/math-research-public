# R150：H198 补图完整原 I11 的精确二十行二列表示及两条个别值必要式

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

唯一实际运行 run46090310802 / job140809432890 已完整成功：驱动 128.939929339 秒、峰值 RSS 711164 KiB、内层退出码 0。以下证明同时保留完整原方程来源和真实运行范围。

**结论。** 在现有 W 余权图的 H198 非零补图，完整原均值与加权值理想 I6 有精确十行二列表示；加入下列五个完整原值条件后，I11 有精确二十行二列表示。两对新的原值行实际给出同一个 lambda 上的必要多项式 C11、C10，其 lambda 次数分别为 11、10。此结论不把它们称为首一或本原，不支付其任何首项或完整内容。H198=0 保持为完整例外支；整个 W 尚未排空。

权环沿 [N1 的 H198 坐标定理](R150-appendix-unit211-W-N1-H198-weight-curve-and-two-generator-monic-square.md) 与 [此前完整十五行二列定理](R150-appendix-unit211-W-H198-complement-exact-fifteen-two-columns-and-two-primitive-sextics.md)。所有权单位均沿当前已经发表的同一原 W 图；下文与完整个别原值的等价性只用于原物理 D 非零的互异单值图，不外推 D=0 碰撞图。

## 1. 更小的精确 I6 表示

沿已完成的 N1 斜率坐标和 H198 非零补图，置 $R=A_W[H198^{-1}][\lambda]$。坐标为

$$
n=p_0+p_1x+p_2y,\quad z=ax+cy,\quad
\Delta_N=ap_2-cp_1,\quad
\hat x=(p_2z+cp_0)/\Delta_N,\quad
\hat y=(-p_1z-ap_0)/\Delta_N.
\tag{1}
$$

$\Delta_N$ 是图内纯权单位，$p_1=a\lambda+b,p_2=c\lambda+d$；$n=N_1+\sum_{i=1}^3\nu_iF_i$，$F_i$ 为三条原均值。此前原源已实际返回 $z$ 的首一平方

$$
q_z=z^2+\beta_1(\lambda)z+\beta_0(\lambda)\in(F_1,F_2,F_3,N_1).
\tag{2}
$$

换基可逆，消去 n 后将三个均值代入 (1) 得到

$$
\widetilde F_i=A_i z^2+B_i z+C_i.
$$

由此前 z 平方的真实均值迹，源码实际检查

$$
q_z=-\sum_i\theta_i\widetilde F_i,\qquad
N_1(\hat x,\hat y)=-\sum_i\nu_i\widetilde F_i.
\tag{3}
$$

这里 $\theta_i$ 是此前真实 $z^2$ 均值约化乘子，没有新增单位。定义

$$
\ell_i=\widetilde F_i-A_iq_z.
$$

它们对 z 至多一次；(3) 与反向 $\widetilde F_i=\ell_i+A_iq_z$ 给出完整理想等式

$$
(\widetilde F_1,\widetilde F_2,\widetilde F_3)
=(q_z,\ell_1,\ell_2,\ell_3).
\tag{4}
$$

令明确自由二次环境 $S=R[z]/(q_z)$。其内任意由若干线性元素 $r_j$ 生成的理想，作为 R 模精确由 $r_j,zr_j$ 生成，因为 S 由 $1,z$ 生成。故完整 I4 商由三条 $\ell_i$ 及各自 z 倍给出精确六行二列。这里 $a,b,c,d$ 只在坐标式 (1) 及换基公式中表示 N1 的四个斜率系数，不是物理权；物理权 $b,c$ 仅用于式 (5) 及原 Gram 的定义。

对同一点原 $N_S,P_S$，先按三条均值降到 $(1,x,y)$，再用 (1) 变为线性余式 $r_S,r_P$。其与原 NS/PS 的差属于 I4。因此加入 $r_S,zr_S,r_P,zr_P$ 后，完整

$$
I_6=(F_1,F_2,F_3,N_1,N_S,P_S)
$$

给出精确十行二列表示。这不是删掉旧十五行中的某些必要交换子；是通过 (3)–(4) 直接给出整个原理想的双向表示。原 I6 商仍不要求自由。此前已完成十五行二列及两条本原六次式的结果保持成立，本次不重跑那两个 cofactor。

## 2. 五个完整原值条件

在相同原变量与权量中记

$$
\begin{gathered}
m=u-\ell,\quad \delta=1-Q,\quad M=4bc\delta,\\
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\\
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell T A_2+2T^3.
\end{gathered}
\tag{5}
$$

以下全部式保持原同一点的值，未倒置 D 或任何 D 范数。第一条是已刊原 C4 的首一 T 四次式。定义

$$
A_*=4uQ-J,\quad C_*=A_*m^2+J\delta\ell^2,\quad c_\lambda=3-2\lambda,
$$

$$
a_\Delta=M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQc_\lambda\ell T+C_*D,\quad
b_\Delta=2Mm(A_*T+uQc_\lambda\ell),
$$

$$
q_{T,4}=\frac{2mD a_\Delta+K b_\Delta}
 {8muQ\ell^2\delta}.
\tag{6}
$$

分母仅为当前已付权量。第二条保完整两矩条件：

$$
R_6=MK^2-4m^2D^3.
\tag{7}
$$

设 $n_b,p_b$ 分别为原 $N_4(\mathrm{row}_B)$、$P_2(\mathrm{row}_B)$ 在 $\rho^2=\delta$ 中的完整 $\rho$ 奇部系数，$A_0=1+T/\ell$。第三、四条是此前已刊 D 降幂后的个别原式：

$$
N_{\rm low}=Dn_b+\frac{2\lambda P_{02}}mKA_0
 +\frac{4\lambda P_{02}m}{\ell M}D^2,
\tag{8}
$$

$$
P_{\rm low}=Dp_b+\frac{3P_{02}}{2m}KA_0^2
 +\frac{P_{02}(3m^2/\ell^2+\delta)}{2mM}KD
 +\frac{6P_{02}m}{\ell M}A_0D^2.
\tag{9}
$$

最后一条保整个原 $N_4(V)$，没有换成某个 $\Phi$ 倍数。原二次型以

$$
V_0=(1,\lambda-1-T,1+T/\ell,1+T/\ell),\quad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho)
$$

定义

$$
Z_0=N_4(V_0),\quad Z_2=N_4(V_1),\quad
Z_1=N_4(V_0+V_1)-Z_0-Z_2.
$$

三个量均为 rho 偶部；源码实际核出奇部为零。使用

$$
V_{\rm low}=DZ_0+\frac{KZ_1}{2m}+\frac{D^2Z_2}{M}.
\tag{10}
$$

式 (6) 沿已发表的原 C4/E2/E3/两线恒等式。式 (7)–(10) 的定义与已刊原 D 降幂源 [2026-11-27-unit211-W-global-monic-T3-D-linear-eleven-by-six-original-return-8542.py](../notes/2026-11-27-unit211-W-global-monic-T3-D-linear-eleven-by-six-original-return-8542.py) 完全一致；本次不运行该旧门。

这些条件的原值意义也可直接核明。置 $s=(\ell\zeta-T)/u$；完整两个矩条件给

$$
Ms^2=D,\qquad 2mDs=K.
$$

因此原单值为 $h=A_0+ms/\ell-\rho s$、$k=A_0+ms/\ell+\rho s$。原个别 N 残式的 rho 奇部是

$$
n_b+4\lambda P_{02}(A_0s+ms^2/\ell),
$$

P 残式的 rho 奇部是

$$
p_b+P_{02}\bigl(3A_0^2s+6A_0ms^2/\ell
 +(3m^2/\ell^2+\delta)s^3\bigr).
$$

分别乘 D 并用两个矩身份，恰得到 (8)、(9)。整个 $N_4(V_0+sV_1)$ 乘 D 后同理恰为 (10)。这是完整原奇部与完整原二次型，未用某个选择性的 trace 代替。

在原 $D\ne0$ 图，$s=K/(2mD)$ 唯一；(7) 迫 $Ms^2=D$。原 NS/PS 的加权残式分别为 $\ell$ 倍偶部加 m 倍奇部，所以 (8)、(9) 连同 NS/PS=0 和已付 $\ell\ne0$ 恢复两对个别原 N/P。这里的 D 非零只用于等价范围；新代数构造没有倒置 D 或其范数。

为避免任何命名歧义，本稿所构造的确切理想始终显式定义为

$$
I_{11}=I_6+(q_{T,4},R_6,N_{\rm low},P_{\rm low},V_{\rm low}).
\tag{11}
$$

新精确模表示首先是 (11) 的表示，不把必要式擅自外推一般碰撞图。

## 3. 先原均值降次，再一次换坐标

若直接在 (2) 中堆叠 T 六次，可能重复引入 H198 高次分母。本次每个新值先在已实际返回的原三生成元 $(1,x,y)$ 中构造。设原真实矩阵满足

$$
xv=M_xv+E_xF_{\rm mean},\qquad
yv=M_yv+E_yF_{\rm mean}.
$$

对两个已具有原均值来源的线性余式 $a v,b v$，固定乘法取

$$
c=a\,(b_0I+b_1M_x+b_2M_y).
\tag{12}
$$

原线性多项式乘积与 $cv$ 的差恰为

$$
\sum_i a_i(b_1(E_x)_i+b_2(E_y)_i)F_{\rm mean}.
\tag{13}
$$

将两输入已有来源一起组合即得完整乘法 DAG。无需假设 $M_x,M_y$ 在自由三维空间交换，亦不假设余式唯一或三生成元自由。相同固定表达式的归纳已经足够。实际已返回的矩阵误差行与每个输入的原来源，经固定有向无环运算图逐项组合，给出该节点的完整原理想身份；这里不声称另外展开了所有巨大最终乘子。

新原 Gram 基础输入 $T,n_b,p_b,Z_0,Z_1,Z_2$ 先经过同一物理 lambda 可逆代入，再实际逐项核回原三均值约化。式 (6)–(10) 的每个加法、乘法和已付权除法继承 (12)–(13) 的原来源。所有这些计算只用原三规则，尚未倒置 H198。

每个完整新值最后只作一次 (1) 换基。若三行是 $r=(r_0,r_1,r_2)$，令

$$
s_0=r_0+(cr_1-ar_2)p_0/\Delta_N,\quad
s_1=(p_2r_1-p_1r_2)/\Delta_N,\quad
\kappa=(-cr_1+ar_2)/\Delta_N.
$$

源实际核回三个系数，故该新值与 $s_0+s_1z$ 的差位于 I4。每条加入这个线性行及其 z 倍

$$
z(s_0+s_1z)\equiv-\beta_0s_1+(s_0-\beta_1s_1)z\pmod{q_z}.
\tag{14}
$$

式 (14) 与 $s_1q_z$ 的精确乘回均实际检查。结合第一节的十行，即得 (11) 的精确二十行二列表示。没有把 I11 商称为自由二维模。

## 4. 精确原商与实际已返回的二十条关系

以 $F_1,F_2,F_3,N_1,N_S,P_S$ 及式 (6)–(10) 定义 I11。由 (1) 的可逆坐标、(3)–(4) 的理想等式、每个新值的原均值运算身份及 (14)，有 R 模同构

$$
\boxed{R[x,y]/I_{11}\ \simeq\
R^2/\langle r_j,zr_j:1\le j\le10\rangle_R.}
\tag{15}
$$

这里十个 $r_j$ 依次是三个 $\ell_i$、NS、PS、$q_{T,4},R_6,N_{\rm low},P_{\rm low},V_{\rm low}$ 的实际线性余式。式 (15) 的右边用首一 qz 约化 z 乘法，并保留全部十个乘积。理想包含于所列模的方向来自这些原理想身份；反方向来自 qz、每个原生成元与其余式的差在 I4，以及每个 S 元素均唯一写成 $a+bz$。这证明完整商表示，无需另设迭代闭包条件。

实际源在 61.699310709 秒返回完整 I6 十行；111.777074914 秒返回完整 I11 二十行。全部三条代入均值、N1 代入、qz 的三均值组合、所有原 Gram 基础输入、最终换基三个系数以及十个 z 乘积均真实乘回。五个值的来源图共 82 个节点；没有逆 D 或 D 的范数，也没有把三维原商或二维原商假设为自由代数。

| 新增原值 | 原余式常数列的 lambda 次数 | 原余式 z 列的 lambda 次数 |
|---|---:|---:|
| $q_{T,4}$ | 5 | 4 |
| $R_6$ | 7 | 6 |
| $N_{\rm low}$ | 6 | 5 |
| $P_{\rm low}$ | 6 | 5 |
| $V_{\rm low}$ | 6 | 5 |

这些是本次实际 z 坐标下的次数。无新逆的中心平移可降低各列次数界，但原二行 determinant 不变；本次未以该平移重跑任何旧目标。

## 5. 两对完整原值行的 cofactor 与内容零支

在二十行全部完成后，只取如下两对：

$$
(A,B)=(R_6,V_{\rm low}),\qquad
(A,B)=(N_{\rm low},P_{\rm low}).
\tag{16}
$$

式中 A、B 是经过已付图内权量清分母的二列多项式行。对任意这一对，设

$$
\omega=(B_1,-A_1),\qquad h=\gcd(B_1,-A_1).
$$

两对实际 h 恰有同一规范定义：双次数 $(8,12)$、总次数 16、69 项，定义字节数 1925，SHA-256 为

0c675b3d0f732e60114a3a1bab0807f59d525e0df253fe0a800e62a56a27270b。

源码分别实际核出两个整除及两个坐标：

$$
h\,(\omega/h)=\omega,\qquad
(\omega/h)
\begin{pmatrix}A_0&A_1\\B_0&B_1\end{pmatrix}
=(C^*,0),\qquad
hC^*=A_0B_1-A_1B_0.
\tag{17}
$$

因此 Cstar 已有原 I11 组合。整个 h=0 纤维仍满足 (17)：这里只约掉两个真实乘子的共同内容，没有把原方程除以未付因子。

随后仅从 Cstar 剥去已付纯权因子及本节明确局部化的 H198 因子。记实际剥除乘子为 U，则源码实际返回

$$
UC=C^*,\qquad
\frac{\omega}{hU}
\begin{pmatrix}A_0&A_1\\B_0&B_1\end{pmatrix}
=(C,0).
\tag{18}
$$

U 在 R 中为单位；这给两条同一点的必要条件 $C_{11}=C_{10}=0$。本次没有计算它们的完整 lambda 内容，不能把 (17) 的乘子内容取消误写成“标量多项式本原”。所有未付 lambda 首项、未付标量内容以及全部 H198=0 原支均保留。

## 6. 实际两条新必要多项式

固定的源码定义给出：

| 原值行对 | $(\deg_e,\deg_k,\deg_\lambda)$ | 总次数 | 项数 | 定义字节数 |
|---|---:|---:|---:|---:|
| $R_6,V_{\rm low}$：$C_{11}$ | $(76,106,11)$ | 149 | 61868 | 4345967 |
| $N_{\rm low},P_{\rm low}$：$C_{10}$ | $(80,110,10)$ | 153 | 61601 | 4328706 |

准确定义的 SHA-256：

- C11：8ac3f173169d4ee706e2bc6fbd174b9c48f472c8288e27b2751bc7c612a98dee。
- C10：282b8fe234b82b5070d9af85c0020eb6e8489c4a025fc080fa27b72aa3475a3f。

剥除前的 Cstar 参数分别为 $(96,131,11)$、总次数 184，以及 $(107,143,10)$、总次数 199；实际定义 SHA 分别为 b63157207e01999e3c62ab5fc9df1449732ee6e17fc82b03d7585d6876bbd9df 与 0f68ba641a78d8f391f5f46e27cea919bdd06babfa7507cd6b0dc753efd718e7。

C11 于 118.783901409 秒完成最后两列乘回；C10 于 128.823633392 秒完成。没有运行这两条式的结果式、范数、共同因式或任何有限纤维排除。它们是完整 I11 的新原组合输入，不是整 W 排空或权参数有限性的证明。

## 7. 实际运行、来源与保留边界

冻结源：

[2026-11-28-unit211-W-H198-full-original-values-first-mean-reduction-twenty-two-model-8542.py](../notes/2026-11-28-unit211-W-H198-full-original-values-first-mean-reduction-twenty-two-model-8542.py)

blob 为 cea5061e1c944129af4c14f6cb53089ecdbebee1；14921 字节，SHA-256 为

f6f07b2f3fdb50f59565ef6501cbc2121d5882ce7cb32f7d17a4a1d2d139b6a1。

唯一实际 run46090310802 / job140809432890，source commit 为 cf8f664bb19a76713f0c946fcb78973861961015。固定 180 秒 / 4 GiB；alarm 与 setitimer 同时受初始绝对截止约束。源最终数学标记于 128.823879294 秒返回，驱动 128.939929339 秒、峰值 RSS 711164 KiB、内层退出码 0。只执行四个已冻结依赖的必要构造前缀；旧十五行 cofactor、十二阶结果式、十八行 module、六维 Norm 及原二参数六阶 determinant 均未执行。

2026-11-28 00:53:54.742954 UTC 真实 pull 从 cf8f664bb19a76713f0c946fcb78973861961015 到 353c9bf9cb7f7ea8009438779453e6e8227b2399。根 README 与课题 README 的 blob 分别仍为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、5fbd905291dd044c88d35bd9c07ac0e586ff795a，差异为空。

stdout 23563 字节，SHA-256 为 c7f8ebfdf4f6fa7384e9b57cb7c0ee28b5be57be37df5a355aa057c2cd38547f。附 [小回执](../notes/2026-11-28-unit211-W-H198-full-original-values-twenty-two-actual-receipt-8542.json)。仅保存源、定义、运行身份及小回执；上表的可重算大系数没有保存、编码或分片传送。

H198=0 的完整原支已有独立有限交结论，但并未因此成为本模型的单位；本补图所有未付 lambda 头与标量内容也继续保留。普通无限维 ISP、整个 W 及其剩余原参数纤维均未由本结果完成。
