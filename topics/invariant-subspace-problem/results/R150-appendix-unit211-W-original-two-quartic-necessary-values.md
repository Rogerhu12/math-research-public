# R150：W 原 Delta 与两个原矩给出的同值双四次必要式

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。
AI-assisted GPT-6 Astra Pro。

**状态：完整原理想恒等式与新的低次必要输入。** 在已发表的原 Delta=0、W=0 权局部化中，从同一个原值中心 s 构造两条仅对 lambda、T 为四次的必要式。两条都有明确的原理想组合，不倒置物理 D、一次值系数或其范数。本文不声称原 W 已空，也不声称下述新 50×35 矩阵已经执行。

## 1. 作用域与原式来源

沿用[完整原值十行及四生成返回](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-native-full-value-four-generator-system.md)的同点 x,y,t、lambda,T，以及[原值身份和首一四生成塔](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-original-value-identities-and-monic-four-generator-tower.md)第 1、3 节。这里 ell、M、Phi 是该已限定图上的已付权单位；不把此前以物理 D 非零为前提的权排除外推到一般 hU=kU 碰撞。

置

$$m=u-\ell,\quad d=1-Q,\quad
s=(\ell\zeta-T)/u=-v_1,\quad v_0=(T+ms)/\ell,$$

$$A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,$$

$$D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell T A_\lambda+2T^3.$$

原向量 Vval=(1,lambda−1−T,hU,kU) 的两个矩为

$$E_2=\tau(V_{\rm val}^2)-2\lambda^2,\qquad
E_3=\tau(V_{\rm val}^3)-4\lambda^3.$$

已发表的完整原身份给

$$q:=Ms^2-D=\ell E_2,\tag{1}$$

$$H:=K-2mDs
=\ell(2ms+3\ell+3T)E_2-\ell^2E_3.\tag{2}$$

仍取原两线的 Delta 分子

$$E_\Delta=\Phi N_f-S\zeta P_f,\quad
S=2v_0+3-2\lambda,\quad z=v_0^2-ds^2.$$

W 的已发表权身份准确给

$$E_\Delta=\Phi\{Q(3-4\lambda)-Jz+2uQS v_0\}.\tag{3}$$

这是原 EDelta 本身，不是把一般原 N4(Vval) 的 Phi 倍数随意拆成两条零式。本图本来要求 EDelta=0，原相容条件 EC=0 与两谱个别 N/P 继续保留。

## 2. 同一个 s 上的原一次式

定义只涉及权及 lambda、T 的系数

$$c=3-2\lambda,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+Jd\ell^2,$$

$$
\begin{aligned}
a_\Delta={}&M\ell^2Q(3-4\lambda)+MA_*T^2
 +2MuQc\ell T+C_*D,\\
b_\Delta={}&2Mm(A_*T+uQc\ell).
\end{aligned}\tag{4}
$$

特别地，aDelta 对 lambda、T 的总次数不超过 2，bDelta 不超过 1。

令

$$Z_\Delta=\ell^2E_\Delta/\Phi.$$

由 (3) 直接展开可得完整式

$$
Z_\Delta=
\ell^2Q(3-4\lambda)+A_*(T+ms)^2
+2uQc\ell(T+ms)+Jd\ell^2s^2.\tag{5}
$$

因此，不经过根选择或数值代入，就有

$$MZ_\Delta-C_*q=a_\Delta+b_\Delta s.\tag{6}$$

(6) 的 s² 系数准确相消；常数、s 系数分别恰为 (4)。Phi 的唯一使用是已付权单位，且下面均给出不含 1/Phi 的完整交叉乘法身份。

## 3. 两个四次式与完整原组合

定义

$$\mathcal R_4=M a_\Delta^2-D b_\Delta^2,\qquad
\mathcal C_4=2mD a_\Delta+K b_\Delta.\tag{7}$$

它们都不含 s，对 lambda、T 的总次数均不超过 4。

第一条的完整原组合为

$$
\begin{aligned}
\Phi\mathcal R_4
={}&M^2\ell^2(a_\Delta-b_\Delta s)E_\Delta\\
&+\Phi\{b_\Delta^2-MC_*(a_\Delta-b_\Delta s)\}q.
\end{aligned}\tag{8}
$$

证明只需将 (6) 代入

$$\mathcal R_4
=M(a_\Delta-b_\Delta s)(a_\Delta+b_\Delta s)+b_\Delta^2q.$$

第二条的完整原组合为

$$
\Phi\mathcal C_4
=2mDM\ell^2E_\Delta-2mDC_*\Phi q+b_\Delta\Phi H.\tag{9}
$$

这是把同一个 s 上的两条一次式联立消元：

$$\mathcal C_4=2mD(a_\Delta+b_\Delta s)+b_\Delta(K-2mDs).$$

由 (1)、(2)，(8)、(9) 都是原 E2、E3、EDelta 的明确组合。因此每个原 Delta0/W0 点必须满足

$$\mathcal R_4=\mathcal C_4=0.\tag{10}$$

整个推导没有倒置 D、aDelta、bDelta、K、Cstar，也没有删掉其中任一零纤维。原理想来源来自等式本身；不使用多变量 gcd=1、模采样或一般矩阵秩判断原解集。

## 4. 同值六次式及未付一次首项

同时保留三阶矩的同值必要式

$$\mathcal R_6=MK^2-4m^2D^3.$$

其完整原组合为

$$\mathcal R_6=M(K+2mDs)H+4m^2D^2q.\tag{11}$$

三个 s 消元式还满足不含任何分母的身份

$$
b_\Delta^2\mathcal R_6
=M\mathcal C_4(b_\Delta K-2mD a_\Delta)
 +4m^2D^2\mathcal R_4.\tag{12}
$$

(12) 说明不能在 bDelta 尚未支付时，把两条四次式当作全部原矩的等价替代。bDelta=0 的整纤维仍在输入中；原 H、q、EDelta、EC 与个别 N/P 仍随原问题保留。本文只用 (7) 增加原系统的必要行，并不引入独立的第二个值参数。

## 5. 新 50×35 原必要矩阵

原 E0、N0、P1 给出的 lambda、T 对同一个 x,y,t 均为仿射一次式，分母为已付权单位。故将这些原式代入 (7) 后，R4、C4 对 x,y,t 仍为总次数至多 4 的原必要多项式。

令列为 x,y,t 的全部总次数不超过 4 的单项式，共 35 列。原四条二次

$$E_1,\ E_{B,e},\ E_{B,o},\ N_1$$

各乘全部次数不超过 2 的单项式，共 40 行；原两个三次 NS、PS 各乘全部次数不超过 1 的单项式，共 8 行。再加 (7) 两条四次原行，得到一个准确的 50×35 输入。

这与原 48×35 只差两条新的原值信息，没有提高旧资源限制或只更换变量顺序。若后续在某个完整有限常数代数上实际返回此矩阵对常数 1 的全 35 列组合，则该有限纤维可按真实证书继续处理。本文尚未运行该矩阵，不将此前 48×35 的秩 33 冒称它的秩或排除结论；已成功的旧纤维不因这个新输入重跑。

## 6. 实际精确恒等式回执

配套 JavaScript 源用十个独立形式变量

$$\ell,u,m,Q,J,d,M,\lambda,T,s$$

上的 BigInt 整系数多项式运算，实际逐系数检查 (6)、(8) 去 Phi 后的形式、(9) 去 Phi 后的形式、(11)、(12)，五条全为零多项式。检查甚至不需要把 m=u−ell 或 M 的权定义代入，因此这些组合身份不来自特定权值采样。

实际运行 24 毫秒，未调用外部计算进程，不报告不存在的 POSIX exit 或 RSS。零次特化、零次数值样本。源码 6395 字节，SHA256：

3d71f3f1c88e0b582123bd6f00f932c882dd8ee1e50f2567c37fdaa330757189

在上述十变量自由整系数环中，R4、C4、R6 分别为 138、54、42 项，对 lambda、T 次数分别为 4、4、6。这些项数不是代入 e,k 权公式后的项数，也不是有限纤维矩阵的执行结果。

原来源保持为已刊 f9409e5f 完整十行回执及 7681be8c 已实际完成的原身份段；旧 180 秒环境大展开没有重放。新矩阵的首次实际有限返回应独立保存回执，只续真实未闭纤维。
