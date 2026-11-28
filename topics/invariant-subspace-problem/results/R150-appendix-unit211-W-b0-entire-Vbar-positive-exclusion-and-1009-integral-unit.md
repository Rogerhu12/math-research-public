# R150 补充：W/b0 整个 Vbar 正阶边界排除及1009整单位性

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127。日期：2026-11-29（Asia/Taipei）。

## 1. 完整结论与先行覆盖

对当前正确 W、完整 b0=0 与既有物理非零图的任一原代数点，在任意1009位置都有
$$
\boxed{v(V_{\rm bar})=0,\qquad V_{\rm bar}=uk+2.}
\tag{1}
$$
这是一条整个原分母边界的排除，不只是某个剩余开图；也不等于整个 W 空性。

先行[全部 e、k、u 的整单位性](R150-appendix-unit211-W-b0-entire-positive-e-ray-exclusion-and-e-k-u-integral-units.md)使 Vbar 整。因此只需反证 Vbar 正阶。此前的完整原覆盖如下：

| 原估值范围 | 已证明的准确来源 |
|---|---|
| 任意 ell 极点 | [统一原 q2/R6 极点排除](R150-appendix-unit211-W-b0-global-ell-integrality-and-Vbar-positive-finite-weight-chart.md)，不要求 delta 单位 |
| Vbar 正阶、u剩余不等于1/2 | 原 ell 分子剩余非零，迫 ell 极点，矛盾 |
| u剩余1/2、k剩余−4 | 上述同稿以 r=Vbar、s=2u−1、z=s/r 整，给全部有限 L=ell剩余=3/4+z剩余 |
| L=0、1/4、1/2、7/4 | 上述同稿分别以完整原 q2/R6 排 ell 深、Phi 深、m 深、Astar 深，保所有 mu 阶 |
| M 剩余为零，允许任意深度 | [整个 M 深中心及 mu 整性](R150-appendix-unit211-W-b0-Vbar-positive-entire-M-zero-exclusion-and-mu-integrality.md)，原 D/K/F 完整返回1 |
| M 单位、mu 任意极点 | 同稿完整 q/R/N5 最高头返回1 |
| 剩余一般有限 mu | 本稿新的完整 q2/R6/N5 原单位返回 |

前六行均为已登记完整结论，本次未重新执行它们。余下所有原点必须处于
$$
u=1/2,\quad Q=2,\quad \delta=-1,\quad \ell=L,\quad
m=1/2-L,\quad M=-(8L^2-4L+1)/4
\tag{2}
$$
的剩余图，且 mu 整、下列纯 L 多项式为单位：
$$
U(L)=L(2L-1)(4L-1)(7-4L)(8L^2-4L+1).
\tag{3}
$$

## 2. 三个完整原必要式

在 (2) 中，
$$
\begin{gathered}
J=1/2+2L,\quad A_*=(7-4L)/2,\quad
T_0=\Phi=1/2-2L,\quad P_{02}=-1/4-L,\\
\lambda=(\mu+3)/2,\quad T=2L\mu/(7-4L),\\
A_2=(\mu^2+4\mu+5)/2,\quad B_3=(\mu^3+6\mu^2+12\mu+7)/2,\\
D=LA_2-T^2,\quad K=L^2B_3-3LA_2T+2T^3,\quad
C_*=A_*m^2+J\delta L^2.
\end{gathered}
$$
完整原 q2、R6 是
$$
q_2=2C_*A_2+2MLQ(3-4\lambda)-8uQ\delta LT^2,
\qquad R_6=MK^2-4m^2D^3.
\tag{4}
$$
完整 N5 用同点已证 f 常数表达：
$$
\begin{gathered}
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(L+T)-GT_0,\quad bc=M/(4\delta),\\
t_s=-P_c/(bcQ\Phi),\quad V_s=-G/Q-P_c/(Q\Phi),\\
y_s=(LT_0/2-uV_s)/M,\quad w=\lambda-1-T,\\
z_1=-2(-L\mu+2T)y_s-2Lw+mTt_s/\delta,\quad z_2=-2G/Q-4my_s,\\
Z_0=2(T-L\mu)(Luw+V_sT)+2bc\,t_sT^2,\\
N_5=2mD(Z_0+Dz_2)+MKz_1.
\end{gathered}
\tag{5}
$$
(5) 不把原物理 f 设为零。其原来源仍为
$$
N_5=2mD\ell^2NV+Mz_{1,\mathrm{full}}H_{\mathrm{val}}
 -2mDz_{2,\mathrm{full}}q-\frac{2f}{MQ}C_4,
$$
在当前同点 b0、q2 下 C4=0。没有 D 逆或不完整奇部替换。

mu 已整，全部恢复系数的分母只有 (3) 支持，故任何尚存原点在同一个剩余 mu 上必须满足
$$
q_2=R_6=N_5=0
\quad\text{于 }\mathbb F_{1009}[L,\mu,U^{-1}].
\tag{6}
$$
lambda 的零剩余、mu=0和任意有限剩余全部保留。

## 3. 两个完整固定伴随与第三个伪余式来源

先只清原分母和 (3) 支持，保实际尺度
$$
p_i=s_iF_i\in\mathbb Q[L,\mu],\quad
(F_0,F_1,F_2)=(q_2,R_6,N_5).
$$
实际三个 mu 次数为2、6、5，L次数为5、9、11；每个 s_i 已完整回乘，全部分母1009整且仅有 U 支持。

第一个固定容量(2,6)矩阵用八列
$$
p_0,\mu p_0,\ldots,\mu^5p_0,\ p_1,\mu p_1;
$$
第二个固定容量(2,5)用七列
$$
p_0,\mu p_0,\ldots,\mu^4p_0,\ p_2,\mu p_2.
$$
两个都只取第零坐标伴随，全部15个坐标及原乘子实际返回。其原行列式 L 次数47、46，仅删除已付 U 支持的18、17次因子后，得到两个 L 次数29的必要标量。

第三个固定来源不倒 q2 的 mu 头。设 h 为 p0 的二次头，分别从 p1、p2 开始同步运输完整三原tag，用
$$
R\mapsto hR-\operatorname{lc}_\mu(R)
 \mu^{\deg_\mu R-2}p_0
$$
作九步精确伪除法，得到完整一次余式
$$
R_{\rm lin}=r_1\mu+r_0,\qquad
N_{\rm lin}=n_1\mu+n_0.
$$
固定组合
$$
C_3=r_1N_{\rm lin}-n_1R_{\rm lin}
$$
是纯 L 标量；全部三原tag同步返回。仅去 U 支持后，其实际 L 次数48。

所以三条新标量均有完整原身份
$$
C_j=\Omega_{j0}q_2+\Omega_{j1}R_6+\Omega_{j2}N_5
\quad(j=1,2,3)
\tag{7}
$$
于 $\mathbb Q[L,\mu,U^{-1}]$。没有反演任何新的 L 头；mu 首项退化、重根、线性余式头同时为零等纤维均由普通身份保留。

## 4. 实际联合原单位与整边界矛盾

对 (7) 的三个新权标量做一次首次 $\mathbb F_{1009}[L]$ 联合 Bézout，实际公共多项式为首一常数1。将它的全部乘子和 (7) 合成后，源码逐项返回
$$
\boxed{
1=\omega_0q_2+\omega_1R_6+\omega_2N_5
\quad\text{于 }\mathbb F_{1009}[L,\mu,U^{-1}].
}
\tag{8}
$$
三条实际终端原乘子均非零，其 mu 次数分别为5、1、1；所有多项式分母只在 U 支持内，有理数分母对1009为单位。实际无需增加 U 正幂，paidSupportPower=0。

这是完整原多项式回乘，不是只在 q2 二次余类中返1，也不是由两个独立结果式的根被错误拼为共同原点。即使三个必要标量共同为零并不充分给原点，(8) 作为必要矛盾仍足以排除每个原点。

(8) 与 (6) 冲突，故余下全部有限 mu 图为空。结合第1节覆盖表，Vbar 正阶已没有任何原点。Vbar 本来整，所以得到 (1)。任意剩余域扩张和分歧位置都同样覆盖，不由单个有限域数值点外推一般 QQ 空性。

## 5. 唯一实际执行与可再生定义

- [冻结源码](../notes/2026-11-29-unit211-W-Vbar-positive-finite-mu-three-full-original-scalars-8542.py)
- [执行前完整输入](../notes/2026-11-29-unit211-W-Vbar-positive-finite-mu-three-full-original-scalars-8542-input.md)
- [小执行回执](../notes/2026-11-29-unit211-W-Vbar-positive-finite-mu-three-full-original-scalars-8542-execution.json)

源 blob **fbf84e2883eb8c43a6b30a3c1b013d2997ecae70**，13590 B，
SHA256 **5b7d8966461d65fecb0a79387a065251a87eea24a8fbf0a4ed33a82d35303681**。

固定120秒/1GiB、外135秒，零执行依赖。唯一
[run46180592399](https://github.com/Rogerhu12/math-research-public/actions/runs/46180592399)，
job **141089034950**、attempt1，实际
**0.16042831600000085秒 / 39836KiB / exit0**；数学末记录0.08874397199999606秒。

源提交 **0465476f3dbeb52b217ed78fc61d41a58349a761**；
真实pull **7b1720935556f0e3d204ec1d735b682a9b5a153c**，
于 **2026-11-28 19:20:04.682125 UTC** 检查两README，无变。
全文核读六条数学记录并按原行重组 stdout：**12265B**，
SHA256 **fb811cad3dd0f3bd1813dd5c60ee40595ca8ccb289b5b4333f6e9f21b35d824f**，
与实际driver匹配。

| 新必要标量 | L次数 | 规范SHA256 |
|---|---:|---|
| 固定q2/R6伴随 | 29 | 577d6599b9c4f9b7342723a8ffac3d52093b058225cf2cf509d3f1beffcda96b |
| 固定q2/N5伴随 | 29 | 72c6c1f6477b019b9f8a5d47e3d063c71049d2db399ccddd1db4a8da62d1b495 |
| 完整伪余式线性楔积 | 48 | 949b8abb7c88b7d2dfc4e6fef8b5c1aee84f9985e31ce7f8be6d62326db9e991 |
| 最终原目标 | 1 | 080a9ed428559ef602668b4c00f114f1a11c3f6b02a435f0bdc154578e4d7f22 |

实际完成15个伴随坐标、19次完整原回乘、九步伪除法、464次精确整除、34次p整检查、34次有限域除法及四次Bézout返回。乘子由冻结源码的固定列、伪除法和合成规则定义；只保源、参数、run/SHA和小profiles，不保存可重算的系数载荷。

本次未运行前源7fe1的M零或pole门，也未重跑旧射线、全权投影或任何冻结资源门。整个 Vbar 边界现已关闭；其余内部 ell、m、M、Astar 等原分母仍需各自证明，不能直接据本稿使用未经支付的完整整模型。
