# R150：W/b0 正 e、k 趋负二、ell 单位的全部 mu 极点原排除

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**结论。** 当前 W/b0 原图中，若 $v(e)>0$、$\bar k=-2$ 且 $\ell$ 是赋值环单位，则 $\mu=2\lambda-3$ 不可能有极点。本篇完整处理全部 ell 剩余值，并以唯一首次的两个原局部返回排除最后两个中心。

结合已成有限 mu 结论，该 ell 单位图只剩
$\bar\ell=3/5,\bar\mu=-2$ 的有限中心；本篇不预记该中心或整个射线被排除。

## 1. 完整原范围与 mu 极点为何只能有 ell 剩余一

令 $r=e$、$v(r)=a>0$。既有原估值范围给 $Z=(k+2)/e$ 整。在本篇 $\bar Z\ne2$，
$$
L=\bar\ell=\frac2{2-\bar Z}\ne0.
$$
原权式直接给
$$
A_*/r\to2(L-3),\quad uQ\ell/r\to-2L,\quad
m\to1-L,\quad M\to2L-1.
\tag{1}
$$
全程使用原
$$
A_*T=uQ\ell\mu,\quad
q_2=2C_*A_2+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2,
$$
$$
R_6=MK^2-4m^2D^3,\quad
D=\ell A_2-T^2,\quad K=\ell^2B_3-3\ell A_2T+2T^3,
$$
$$
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2.
$$

假设 mu 有极点。若 $L=3$，(1) 和 b0 迫 $v(T)<v(\mu)<0$；q2 中 T² 系数除 r 后为单位，其余项的 mu 次数至多二，所以 T² 唯一最低，矛盾。没有倒 $A_*/r$。

取 $H=3-L\ne0$，有 $T/\mu\to L/H$。完整 q2 最高式为
$$
(L-1)C_3(L)=0,\qquad C_3=2L^3-15L^2+18L-9.
$$
完整 R6 除以 $\mu^6$ 的余值为
$$
\frac{27(L-1)^2L^3}{4H^6}R_5(L),\quad
R_5=L^5-14L^4+69L^3-146L^2+144L-54.
$$
这些表达式保留 M、D、K 最高项为零的可能，不除它们。

若 $L\ne1$，两式给 $C_3=R_5=0$。直接整式身份
$$
8R_5=(4L^2-26L+45)C_3+B_2,\quad B_2=11L^2+108L-27,
$$
$$
121C_3=(22L-381)B_2+144(305L-79)
$$
迫 $L=79/305$，但
$$
305^2B_2(79/305)=159236\equiv823\pmod{1009}.
$$
故全部 mu 极点只能有 $L=1$。上述纸面来源原 blob 为
58ebb5c9b87163348069bc1ef32ae939bda181a9，本篇已完整纳入，不借一次数值试点。

## 2. L=1 的两个完整局部中心

令
$$
x=1/\mu\in\mathfrak m,\qquad d=\ell-1.
$$
原 q2 的正则归一
$$
F_q=x^2\frac{q_2}{2uQ\ell}
=x^2\left[4\delta D-M\left\{
\frac{A_2}{\kappa}+\frac{2\mu+3}{u}\right\}\right],
\qquad \kappa=\frac{uQ\ell}{A_*},
$$
对 d 的一次头为 $-3/2$。因此
$$
d=(r+4x)/3+O((r,x)^2).
$$
在该原 q2 的局部商中，
$$
F_R=x^6R_6
=-r^2/48+rx/6-x^3/2
 +O(r^3,r^2x,rx^2,x^4).
\tag{2}
$$
这是整正则展开，非将有限域解任意提升到 QQ。

设 $b=v(x)>0$。若 $b>a$，(2) 的 r² 唯一最低；若 $b<a$，rx 与 x³ 只有 $a=2b$ 才可相消；若 $b=a$，前两二次项必须相消。因此全部可能只有
$$
\mathrm A:\quad r/x^2\to3,\quad b=a/2;
\qquad
\mathrm B:\quad r/x\to8,\quad b=a.
\tag{3}
$$
原权关系给 $d=r+Z/2+O((r,Z)^2)$。写 $Z=xY$，两个中心准确成为
$$
\mathrm A:\quad r=x^2R,\quad (R,Y)\to(3,8/3);
$$
$$
\mathrm B:\quad r=xR,\quad (R,Y)\to(8,-8).
\tag{4}
$$
这包括所有不相等的正估值和全部首次相消，不预先指定 x 的平方根或剥未知头。

## 3. 同一原 q2/R6 的两个单位 Jacobian

A 图取 $(F_q/x,F_R/x^3)$，B 图取 $(F_q/x,F_R/x^2)$。它们在当前局部环正则，其 x=0 完整式是
$$
\mathrm A:\quad
2-\frac34Y,\quad
\frac{Y(27Y^2-144Y+144+16R)}{256};
$$
$$
\mathrm B:\quad
2-R-\frac34Y,\quad \frac{R(R+Y)}{16}.
$$
按 $(R,Y)$ 次序，在 (4) 得
$$
J_A=\begin{pmatrix}0&-3/4\\1/6&0\end{pmatrix},
\qquad
J_B=\begin{pmatrix}-1&-3/4\\1/2&1/2\end{pmatrix},
$$
行列式为 $1/8,-1/8$，都是 1009 进单位。

原权分母先提取明确 x 幂后，常数只涉及
$k=-2$、$M=1$、$A_*/r=-4$、$\Phi/r=2$、$Q/r=-2$、
$R=3$ 或 8。由整隐函数定理，两个图各有唯一
$$
R(x),Y(x)\in\mathbb Z_{1009}[[x]]
$$
通过该中心并满足同点原 q2/R6。任何假想原赋值解都必须取这两个确定隐函数之一。

唯一首次运行在 QQ 上构造其 12 阶 jet。每阶只解对应的同一常数 Jacobian；全部 48 个新系数和实际读取的系数分母均检查为 1009 进整。最终 q2/R6 的全部系数直到 12 阶精确返回零。Laurent 运算逐次传播已知精度，没有把未计算尾项当成零。

## 4. 完整原 N5 的首次非零项

本次使用完整原定义
$$
T_0=2u-\ell Q-2u^2,\quad \Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3,\quad
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,
$$
$$
t_s=-P_c/(bcQ\Phi),\quad V_s=-G/Q-P_c/(Q\Phi),
\quad W_s=T_0/2,\quad y_s=(\ell W_s-uV_s)/M,
$$
$$
w=\lambda-1-T,\quad c_\lambda=-\mu,
$$
$$
z_1=-2(\ell c_\lambda+2T)y_s-2\ell w+mTt_s/\delta,
\quad z_2=-2G/Q-4my_s,
$$
$$
Z_0=2(\ell c_\lambda+T)(\ell uw+V_sT)+2bc\,t_sT^2,
$$
$$
N_5=2mD(Z_0+Dz_2)+MKz_1.
\tag{5}
$$
这些仍是原 f 常数系数，未施加物理 f=0。原完整 NV 身份将 (5) 与同点值条件相连，当前 b0/q2 下 N5 必须为零。

$T_0,P_{02},G$ 各有 r 因子，$P_c$ 有 r² 因子；它们在 t_s、V_s 中的 r 极点精确抵消。N5 对 mu 次数至多五，所以
$$
F_N=x^5N_5
$$
在两个局部环都正则。代入唯一隐函数的 12 阶 jet，只改变其 13 阶及以后项。

本次首次实际返回：
$$
\boxed{\quad
\mathrm A:\ x^5N_5=-\frac23x^4+O(x^5),\qquad
\mathrm B:\ x^5N_5=38x^3+O(x^4).
\quad}
\tag{6}
$$
A 的 0 至 3 阶和 B 的 0 至 2 阶都在 QQ 中精确为零，未跳过任何首个非零系数。两个显示系数都是 1009 进单位，模 1009 分别为 672、38。

实际源只打印系数字节数与 SHA：A 为 4 字节、
527a7f0844472f3cc7360c10db36011507264f496f7e8f147317b11256624805；
B 为 2 字节、
aea92132c4cbeb263e6ac2bf6c183b5d81737f179f21efdc5863739672f0f470。
规范字符串“-2/3”和“38”分别精确匹配上述 SHA；此小参数身份不重算任何 jet。

因为 $v(x)>0$，(6) 中首项的估值严格低于后面所有项，不可能为零。两个中心都被完整原 N5 排除。结合第1–2节，整个当前 ell 单位图的 mu 极点被排除。

## 5. 唯一实际执行与边界

[唯一首次源](../notes/2026-11-29-unit211-W-b0-positive-e-k-minus-two-ell-one-pole-two-local-original-jets-8542.py)，blob **166f357160ae13e942e1eed327e58d32e83bc26d**，SHA256 **8c647dc4a32e70a6b3f88033c83bc7a53f4c1e53094d7bbeb563fbfa7441826b**。

原输入 blob 5e20e95b2bcaf2a7d7b5a49ebbc6019b54351705。run **46173434775**、job **141066781704** 的真实记录：

- 内层退出码 0，elapsed **0.6626197880000007 秒**，max RSS **39164 KiB**；
- 最后数学阶段 **0.6148924720000011 秒**；
- source commit **255eb5e112652e6b8822d745a8c274b33206d411**；
- 原实际 pull 于 2026-11-28 18:00:19.564260 UTC 至 **d5471187b68b61cf78dbeaa71b8beec46c21cd09**，两份规则未变；
- 64 个完整 series 坐标检查、48 个 implicit 系数、132 个整性检查、两个完整原 N5 jet；
- stdout 3100 字节，SHA256 **4ed4ff15454295bb7653d913641ae20bf9977042f8ebfdcee8833a4f0196c392**。

小回执：[两个完整原局部返回](../notes/2026-11-29-unit211-W-b0-positive-e-k-minus-two-ell-one-pole-two-local-original-jets-receipt-8542.json)。

本篇不重跑任何旧门；没有从模 D 幂零或裸模空性推 QQ。唯一有限中心
$L=3/5,\mu=-2$ 仍开放，另有独立新原输入；不由本篇宣整个 W 排空。
