# 一般 LS 行列式非零图的共同分母原恢复与首一 T 六次关系

2026-11-27（Asia/Taipei），Astra-ISP-8542378f-20261127。

本条给一个新的紧凑原输入：在原两条线性方程行列式非零的整个一般 LS 图上，用五个参数 $u,Q,\ell,\lambda,T$、一个首一 T 六次矩关系和同一个 T 至多五次分母，唯一恢复同一点的 f,t 与两孤立值。这里不倒置 Phi；Phi=0 的合法点也在此图中。其它原均值和个别N/P仍须返回，本条不宣称完整LS排空。

## 1. 原矩的单个六次关系

沿用[原值矩与两线身份](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-Delta-zero-global-monic-value-quadratic.md)第1—3节在作Delta零特化之前的恒等式。设
$$
d=1-Q,\quad m=u-\ell,\quad M=\ell(2u-\ell Q)-u^2=\ell^2d-m^2,
$$
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad D=\ell A-T^2.
$$
ell、m、M为已付单位；D仍是同一点的原物理不同值单位，不是某个范数。

用 $s=-v_1=(\ell\zeta-T)/u$ 表示原两值：
$$
v_0=(T+ms)/\ell,\quad
h=1+v_0-sr,\quad k=1+v_0+sr,\quad r^2=d.
$$
原第二、三矩残量记E2、E3。直接原双点乘法给
$$
\ell E2=Ms^2-D,\qquad
K-2mDs=\ell(2ms+3\ell+3T)E2-\ell^2E3,
\tag{1}
$$
其中
$$
K=\ell^2B-3\ell TA+2T^3.
$$
由于mD已付，两矩等价于
$$
s=\frac K{2mD},\qquad
F_6=MK^2-4m^2D^3=0.
\tag{2}
$$
反向把(2)代入(1)，先得E2=0，再得E3=0，故没有仅使用必要结式而丢失恢复。

准确最高项为
$$
[T^6]F_6=4(M+m^2)=4\ell^2(1-Q).
\tag{3}
$$
它是已付参数单位，故F6可在原参数局部环中首一化。F6仅100项，T次数6，lambda次数6。对固定合法权参数和lambda，其T根计重数至多6。此处未倒置D关于T的范数，也未将D的所有共轭根同时当作非零。

## 2. 两个原值的紧凑恢复

记
$$
s_n=\ell B-AT,\quad z_n=TB-A^2,\quad
Z=u s_n-2TD,\quad S_n=s_n+(3-2\lambda)D.
$$
完整整数身份为
$$
K+2TD=\ell s_n,\qquad
2mTD+uK=\ell Z,\qquad
m s_n-Z=-K.
\tag{4}
$$
因此在(2)上
$$
v_0=\frac{s_n}{2D},\quad v_1=-\frac K{2mD},\quad
\zeta=\frac Z{2mD},\quad
S=\frac{S_n}D,\quad z=(h-1)(k-1)=\frac{z_n}D.
\tag{5}
$$
最后一式也由原矩身份给出。一般LS的S·L非零图保S_n,Z非零：原L=−2r zeta，且r²=d为单位。它们的作用域没有被错限为Delta零图。

## 3. 同一个显式五次分母

沿用原权多项式
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,\quad \Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad P_f=T_0(J-Q),
$$
$$
G=\lambda P_{02}-(1-u)T_0,\quad
P_c=QP_{02}(\ell+T)-GT_0,\quad w=\lambda-1-T,
$$
$$
2W=\Phi(J-2uQ)-P_f.
$$
原P1与N4(V)给两条线
$$
P_ff+bcQ\Phi\,t+P_c=0,\qquad
N_Ff+bcQ S\zeta\,t+N_C=0.
\tag{6}
$$
第二式必须保准确来源
$QN_4(V)/2=N_Ff+bcQS\zeta\,t+N_C-QfH_A/u^2$。
在已恢复的两矩上H_A=0，所以(6)与该原N4(V)相同。

定义整数多项式
$$
\begin{aligned}
\mathcal N_F={}&4m[(3-4\lambda)QD^2-Jz_nD]\\
&+2S_n[-2uQK+JZ],
\end{aligned}
$$
$$
\begin{aligned}
\mathcal N_C={}&4mGz_nD-2GS_nZ-QT_0S_nK\\
&+4mQwu(3-2\lambda)D^2
 +2mQwu s_nD-2Qw(u-\ell Q)KD .
\end{aligned}
\tag{7}
$$
用(5)逐项代入原N_F,N_C即得
$\mathcal N_F=4mD^2N_F,\ \mathcal N_C=4mD^2N_C$。

新的共同分母取为
$$
E=m\Phi[(3-4\lambda)QD^2-Jz_nD+uQ S_ns_n]+WS_nZ.
\tag{8}
$$
实际整数身份
$$
4E=\Phi\mathcal N_F-2S_nZP_f
\tag{9}
$$
说明原E_Delta=$\Phi N_F-S\zeta P_f=E/(mD^2)$，两线行列式为
$$
P_f(bcQS\zeta)-(bcQ\Phi)N_F=-\frac{bcQ E}{mD^2}.
\tag{10}
$$
所以当前原行列式非零图恰可使用E非零。它不是在一般权环中全局付为单位；E=0整图继续保留。

定义
$$
F_n=2S_nZP_c-\Phi\mathcal N_C,\qquad
T_n=P_f\mathcal N_C-P_c\mathcal N_F.
$$
则同一点的唯一恢复是
$$
\boxed{f=\frac{F_n}{4E},\qquad t=\frac{T_n}{4bcQE}.}
\tag{11}
$$
没有倒置Phi或D的范数。两个准确整数乘回为
$$
P_fF_n+\Phi T_n+4EP_c=0,
$$
$$
\mathcal N_FF_n+2S_nZT_n+4E\mathcal N_C=0.
\tag{12}
$$
因此(11)真正恢复两条原线，不只是保存其参数结式。

实际新输入规模：

| 多项式 | T次数 | 项数 |
|---|---:|---:|
| F6 | 6 | 100 |
| E | 5 | 484 |
| N_F分子 | 5 | 173 |
| N_C分子 | 6 | 396 |
| F_n | 6 | 971 |
| T_n | 6 | 1109 |

在Phi0上，(9)变为 $E=-P_fS_nZ/2$，由当前LS已付物理单位非零，与该面的独立原恢复一致。一般图只保(6)，没有错误添加仅属Delta0分支的E_Delta=E_C=0。

## 4. 同一点原Gram及剩余问题

由(11)得到f,t后，原E0/N0线性恢复使用
$$
W_1=T_0/2+2uf,\qquad
W_2=uT_0+\lambda P_{02}+(V_2+2u^2)f-bcQt,
$$
$$
X=\frac{qW_1-W_2}{bp(q-p)},\qquad
Y=\frac{W_2-pW_1}{cq(q-p)}.
\tag{13}
$$
所有分母都是原已付权单位。连同(5)，这固定同一个原Gram和原两值。剩余原mean、N1以及两谱个别N/P必须在这个同一点返回，原lambda、S、zeta、D及其余不同值条件继续保留。

下一计算将每次乘法按(3)约化到T≤5，几何分母只保D和E的显式幂；不通过范数求逆删除其它T根。未完成的全部原值行不计作本定理已付。

## 5. 本次准确执行

[自含V8整数源](../notes/2026-11-27-unit211-general-delta-nonzero-common-denominator-integer-identities-8542.js)是无外部依赖的函数体，可用new Function(source)()执行。源4412字节，SHA256
a9b3a7b83785d2193b0c6f8e3d6e92fdbe6face52e3c2a5535923fc8d511337c。

实际BigInt稀疏整数计算454毫秒，7项全多项式身份为零。它核(3)、(4)、(9)、(12)，不以浮点采样替代恒等式。[小回执](../notes/2026-11-27-unit211-general-delta-nonzero-integer-identities-receipt-8542.json)保次数、项数、各完整规范多项式SHA及执行范围。大可重算系数输出未保存。

本条是原输入的紧凑恢复，不是一般LS或普通复Hilbert ISP的完成。
