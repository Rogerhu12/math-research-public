# R150：W/b0 内部 m 正阶、k=-2 整支的原均值单位排除

日期：2026-11-29（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

**定理。** 在当前正确 W、完整 $b_0=0$ 物理图的任意 1009 赋值位置，不存在
$
v(m)>0,\qquad \bar k=-2.
$
原 $q_2/R_6$ 先把该整支压到唯一有理剩余中心；独立真 $E_1$ 二次头支付 $f$ 整性；唯一首次执行在完整四维 $f/\sigma$ 环境内实际返回普通原多项式恒等式 $1$。最终只用真 $E_1$ 和完整 $E_B$ 两个非零乘子，所有谱根及重数都在原环境内保留。另一 $\bar Q=2$ 的 $m$ 正阶图不由本定理关闭。

## 1. 原范围与实际目标

始终取当前正确真 dual-germ 的 W、完整 b0=0 物理图，剩余特征为 1009。赋值可以在任意有限扩张中取值，不假定离散阶已经归一为整数。本输入只处理
$$
v(m)>0,\qquad \overline k=-2.
$$
已经独立完成的原估值定理给出 e、k、u=e+1、delta=1-Q、Vbar=uk+2 均为赋值单位，ell 整。本输入不重算这些结论，不使用物理 m 非零来断言 m 是赋值单位。

这里和以下公式统一以 $\delta$ 表示 delta。原权为
$$
Q=ek,\quad
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)},\quad
m=u-\ell=\frac{u(k+2)(Q-2)}{k(uk+2)},\quad
M=\ell^2\delta-m^2.
$$
因此整个 $v(m)>0$ 边界分为 $\bar k=-2$ 与 $\bar Q=2$ 两图；两者交点会迫 $\bar u=0$，已经排除。本次唯一计算只针对第一图。另一图的全部有限 $\mu$、原权首项和原值仍保留。

实际完成的目标是在完整四维 $\mathbb F_{1009}$ 代数中，以全部真实原行返回 1，并最终在未取商的 $\mathbb F_{1009}[f,\sigma]$ 中返回完整十源恒等式。这里没有从有限域空性向未经识别的有理数一般纤维提升的步骤：它直接检验一个已由原估值式强制得到的剩余中心。

引用的先行范围：

- [e、k、u 全部整单位](../results/R150-appendix-unit211-W-b0-entire-positive-e-ray-exclusion-and-e-k-u-integral-units.md)；
- [全 ell 整与 Vbar 有限权图](../results/R150-appendix-unit211-W-b0-global-ell-integrality-and-Vbar-positive-finite-weight-chart.md)；
- [整个 delta 正阶排除](../results/R150-appendix-unit211-W-b0-entire-delta-positive-exclusion-and-1009-integral-unit.md)；
- 原 Vbar 正阶整支排除沿 parent 已完成、单独发表的原三式单位返回。本小图实际上已有 $Vbar=-2(u-1)$ 的非零首值，故不需要借用该整支的其他坐标图。

## 2. 两个原必要式强迫唯一有理剩余中心

令
$$
\mu=2\lambda-3,\quad
A_2=\frac{\mu^2+4\mu+5}{2},\quad
B_3=\frac{\mu^3+6\mu^2+12\mu+7}{2},
$$
$$
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2,
$$
$$
A_*T=uQ\ell\mu,\quad
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell A_2T+2T^3.
$$
保留完整原必要式
$$
q_2=2C_*A_2+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2=0,
\qquad
R_6=MK^2-4m^2D^3=0. \tag{1}
$$

置 $U=\bar u$。在 $\bar k=-2$ 且 $v(m)>0$ 上，
$$
\bar Q=2(1-U),\quad \bar\delta=2U-1,\quad
\bar\ell=U,\quad \bar M=U^2(2U-1),
$$
$$
\bar J=\bar A_*=-4U(U-1),\qquad
\bar T=U\bar\mu/2
$$
（最后一式在 $\mu$ 整后取剩余；在整性论证中使用相应单位系数的完整仿射式）。

完整 $q_2$ 的 $\mu^2$ 头在该局部环中为单位，因为其剩余多项式为
$$
4U^3(U-1)(2U-1)
 \big[(U-1)\mu^2-2\mu-2\big]. \tag{2}
$$
前置各因子均非零，故 $\mu$ 整、$\lambda,T,D,K$ 皆整。由 $R_6$、$M$ 单位和 $v(m)>0$，有 $\bar K=0$。剩余式为
$$
(U-1)\mu^2-2\mu-2=0,\qquad
(U-1)\mu^3+9\mu+14=0. \tag{3}
$$
第二式减去 $\mu$ 倍第一式恰得
$$
2\mu^2+11\mu+14=(\mu+2)(2\mu+7)=0. \tag{4}
$$
若 $\bar\mu=-2$，第一式迫 $U=1/2$，与 $\bar\delta\ne0$ 冲突。因此唯一剩余中心是
$$
U=\frac{29}{49},\quad
\bar\mu=-\frac72,\quad
\bar\lambda=-\frac14,\quad
\bar T=-\frac{29}{28}. \tag{5}
$$
其余参数准确为
$$
\bar e=-\frac{20}{49},\quad \bar k=-2,\quad
\bar Q=\frac{40}{49},\quad \bar\delta=\frac9{49},\quad
\bar\ell=\frac{29}{49},\quad \bar m=0,
$$
$$
\bar D=-\frac{87}{784},\quad
\bar K=0,\quad
\bar M=\bar\ell^2\bar\delta,\quad
\bar w=\bar\lambda-1-\bar T=-\frac3{14}. \tag{6}
$$
上述有理数分母均为 1009 单位；没有按新的原理想秩选择素数或剩余点。

## 3. 同一点的原仿射恢复不倒 m 或 Pf

以下是正确原 Gram 的定义，先在原局部系数环中理解，再在 (5) 取剩余。写
$$
a=1-\ell,\quad p=1+\rho,\quad q=1-\rho,\quad
\rho^2=\delta,\quad
b=\frac{\ell+m/\rho}{2},\quad c=\frac{\ell-m/\rho}{2},
\quad bc=\frac{M}{4\delta}.
$$
并定义
$$
T_0=2u-\ell Q-2u^2,\quad
\Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,\quad
G=\lambda P_{02}-(1-u)T_0,
$$
$$
P_f=T_0(J-Q),\quad
P_c=QP_{02}(\ell+T)-GT_0.
$$
使用原 P1 仿射式
$$
t=-\frac{P_ff+P_c}{bcQ\Phi},\qquad
V=\frac{Jf+bcQt-G}{Q},\qquad
W_1=2uf+\frac{T_0}{2}, \tag{7}
$$
$$
X=\frac{W_1-qV}{b(p-q)},\quad
Y=\frac{pV-W_1}{c(p-q)},\quad
A_1=2f-2V+2bct,\quad
r=X-ap-ct,\quad s=Y-aq-bt. \tag{8}
$$
在 (5)，$T_0=0$ 而
$$
\Phi=-\frac{40}{49},\qquad
b=c=\frac{29}{98},\qquad \rho=\frac37
$$
均为单位。因此 (7) 从不倒退化的 $P_f$；只倒 $bcQ\Phi$ 等真实赋值单位。另一 $\rho=-3/7$ 将两个完整 singleton 标签同时交换，保留下面的全体原行，故选择 $\rho=3/7$ 不丢原点。

在本中心，完整 (7)–(8) 给出
$$
t=-\frac{27}{49},\qquad
V_f=2U,\qquad X_f=Y_f=2, \tag{9}
$$
其中下标 $f$ 表示普通多项式系数，绝非把物理 $f$ 设为 0。

## 4. 真 E1 的单位二次头支付 f 整

四维 dual algebra 的乘法和迹必须使用
$$
(vz)_0=v_0z_0,\quad
(vz)_1=v_0z_1+v_1z_0,\quad
(vz)_B=v_Bz_B,\quad(vz)_C=v_Cz_C,
$$
$$
\tau(v)=av_0+v_1+bv_B+cv_C.
$$
原 Gram 行为
$$
R_0=(0,0,p,q),\quad R_1=(0,A_1,r,s),\quad
R_B=(p,r,0,t),\quad R_C=(q,s,t,0).
$$
置 $\mathbf1=(1,0,1,1)$，
$$
(\mathcal Kv)_j=\tau(R_jv),\qquad d=\mathcal K\mathbf1,\quad F_2=\tau(d)=2f.
$$
真实均值是
$$
E_j=\tau(R_j^2)-2(\mathcal Kd)_j-2(d^2)_j+2F_2d_j,
$$
其中 dual 系数 $j=1$ 的第一项为 $2\tau(R_0R_1)$，而
$(d^2)_1=2d_0d_1$，不可替成 $d_1^2$。

由 (9)，$d_1$ 的 $f$ 系数为 $2-2U$，
$(\mathcal Kd)_1$ 的 $f^2$ 系数为 $4U$。故
$$
[f^2]E_1=-8U+4(2-2U)=8-16U=-8\bar\delta. \tag{10}
$$
它是单位。相比之下，在该中心 $[f^2]E_B=[f^2]E_C=0$，所以本输入确实使用独立的真 $E_1$，没有把它与加权均值偷换。

原 $E_1$ 各系数在此赋值环中整，二次头是单位；原点满足 $E_1=0$，从而 $f$ 整。于是 (7)–(8) 的全部 Gram 坐标整，能够合法同时取剩余。

## 5. 保全部谱根与全部重数的四维环境

在剩余中心，完整谱为
$$
v=(1,w,h,k_v),\qquad
h=1+T/\ell+\rho\sigma,\quad
k_v=1+T/\ell-\rho\sigma.
$$
这里 $k_v$ 是原 singleton 值，与权参数 $k$ 区分。第二矩为
$$
E_2=b(h-1)^2+c(k_v-1)^2-A_2
    =\frac M\ell\left(\sigma^2-\frac D M\right). \tag{11}
$$
$M$ 单位且 $D$ 整，因此 $\sigma$ 整。本中心第三矩满足准确恒等式
$$
E_3=b(h-1)^3+c(k_v-1)^3-B_3
     =3T\delta\left(\sigma^2-\frac DM\right), \tag{12}
$$
它没有遗留新的值根选择。

于是
$$
q_f=\frac{E_1}{-8\delta},\qquad
q_\sigma=\sigma^2-\frac DM=\frac\ell M E_2
$$
给出两个独立的首一二次，环境
$$
B=\mathbb F_{1009}[f,\sigma]/(q_f,q_\sigma)
$$
以 $1,f,\sigma,f\sigma$ 为自由四维基。这里的自由性只来自这两个显示首一关系，不是对原商擅加的假设；任何重根和幂零结构全部保留。

新原值定义为
$$
\mathcal N(v)=
2\tau(dv^2)-F_2\tau(v^2)-4\tau(v)\tau(dv)
 +2F_2\tau(v)^2+\tau(v\mathcal Kv),
$$
$$
\mathcal P(v)=\tau\big((v-\tau(v)\mathbf1)^3\big).
$$
完整十源依次是
$$
E_2,E_1,E_B,E_C,N_1,N_B,N_C,P_B,P_C,NV,
$$
其中
$$
N_1=\mathcal N(R_0+R_1)-\mathcal N(R_0)-\mathcal N(R_1)
          -4\lambda wP_{02},
$$
$$
N_B=\mathcal N(R_B)-2\lambda P_{02}h^2,\quad
N_C=\mathcal N(R_C)-2\lambda P_{02}k_v^2,
$$
$$
P_B=\mathcal P(R_B)-P_{02}h^3,\quad
P_C=\mathcal P(R_C)-P_{02}k_v^3,\quad NV=\mathcal N(v).
$$
源码还直接返回 $E_0=0$、$F_2=2f$、原 N0/P1、(11)–(12)，核定全部原式确在同一点。

## 6. 完整四维原返回及整个命名支的关闭

每个十源乘四个基元后，用两个首一关系作准确普通多项式短除；每一列都保留完整十个原乘子，因此得到真实 $4\times40$ 原列矩阵。有限域 Gaussian 只组合这些已返回的原列。

唯一预定目标是 $1$，此次已真实完成。先逐四坐标乘回，再合并全部列的实际原乘子，最后在未取商的普通环中实际检查
$$
\sum_{i=1}^{10}\Omega_iF_i=1
       \quad\text{于 }\mathbb F_{1009}[f,\sigma]. \tag{13}
$$
不以矩阵秩摘要代替 (13)，也不以 $D$、$m$、$f$ 或 $\sigma$ 的正幂冒充单位目标。

实际 Gaussian rank 为 4，40 个原列、40 次首一短除和最后完整十源返回都成功。更具体地，非零最终乘子只有 $E_1$ 的常数乘子和 $E_B$ 的一次 $f$ 乘子，故实际身份还具有
$$
1=cE_1+(a_1f+a_0)E_B,\qquad c,a_0,a_1\in\mathbb F_{1009}. \tag{14}
$$
此处系数由唯一原源的准确列运算定义，未另存可重算系数；完整源在普通多项式环中已经把 (14) 乘回。两个非零乘子的 canonical profile SHA 分别为
`3b023596ea2e4d7ac8aa2a3dd0d2f85df5712524c04b9e92adfb3eae4151ca39`、
`9c05ca4098ff00be38a4a89311365ed5da28f8361eba12a293186b97e6e54523`。

任何假设原点在 (5) 处都已证明 $f,\sigma$ 和全部原系数整，其剩余必同时满足这两条真实原均值；(14) 矛盾。因此整个 $v(m)>0,\bar k=-2$ 命名支排除，不只是某一数值谱根。任意剩余域扩张仍保持 (13)–(14)。

本结论没有把模 $D$ 幂零提升为有理数结论，不需要新 Hensel 选择，也不从一个任意良好模点推一般权域空性。被检验的中心是完整原估值式唯一强制的中心，且原变量整性已经独立支付。

## 7. 唯一实际执行与来源

源：[完整四维原返回](../notes/2026-11-29-unit211-W-b0-internal-m-positive-k-minus-two-whole-four-original-return-8542.py)；派发前输入：[完整范围及整性证明](../notes/2026-11-29-unit211-W-b0-internal-m-positive-k-minus-two-whole-four-original-return-8542-input.md)；小回执：[完整实际记录](../notes/2026-11-29-unit211-W-b0-internal-m-positive-k-minus-two-whole-four-original-return-receipt-8542.json)。

源 blob `e9ceaf177097ac19454bad1d3e5bae84310b5e7c`，10015 字节，SHA-256
`4cd24055fb922e2dd041ec37d6a9c0a4f57f0cc17ff5a382a5a61b487de4f1f3`。
源在第一次执行前全文静审，未作数学重跑。

唯一 [run 46182562376 / job 141095189005](https://github.com/Rogerhu12/math-research-public/actions/runs/46182562376/job/141095189005) 实际为：

| 项目 | 实际记录 |
|---|---|
| driver elapsed | 0.03303533100000067 秒 |
| 数学最后完整 stage | 0.01091920899999721 秒 |
| 峰值子进程 RSS | 34160 KiB |
| 内层退出 | 0 |
| 资源预算 | 原固定 30 秒 / 256 MiB；外层 45 秒 |
| 环境维数 / 原列 | 4 / 40 |
| 实际 rank / 原目标 | 4 / 1 |
| 完整普通十源返回 | 已完成 |
| 原定义 / 首一原关系 | 15 / 2 |
| 原短除 / 列返回 | 40 / 40 |
| stdout | 4584 字节 |

stdout SHA-256：
`50a4415b46259c9084ac5d98f99aced8128cdfff28a69cab2a941495e6e519b8`。

source commit 与实际 pull 后 commit 均为
`4cb9c03e90a3f2dcec519f80ad0c66d6c885664c`，
真实 pull 时间 2026-11-28T19:42:36.598954Z。两 README blob 分别为
`99c5ad8d06e939e6cfbbab1afdeffa5463f15f18`、
`5fbd905291dd044c88d35bd9c07ac0e586ff795a`，实际记录显示规则无变。

原日志字段 `noMInverse=true` 的命名指 **小写 $m$ 未被反演**。源确实且合法地反演大写 $M=\ell^2\delta$，它在本中心是已证明的赋值单位；这里保留原运行字节和原字段，并明确其语义，不改写实际历史。

本文只关闭这张内部 $m$ 正阶图。其余 $\bar Q=2$ 图、尚未排除的内部权边界和全部剩余原值均保持各自原范围。没有新全 W 空性或有限点数外推。
