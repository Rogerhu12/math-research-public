# 正确 Phi：第二 NV 头上的原幂等元极化与低分母完整三次式

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**状态：完整原身份的纸面推导，无新执行。** 本文处理
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0
\tag{1}
$$
这一整个原支。通过同一个真实 Gram 代数中幂等元的极化，直接给出完整原 $N_4$ 的小三次表达式。其最后清分母只需旧单位 $Q$、$u-1$、$Q+4(u-1)$，不含 $M$ 的逆。这是完整原值的恒等改写；没有排除此支，没有反演新首项，也没有删除物理 $t$ 或任何其它同点原方程。

依赖为[第二 NV 头原二矩与四列呈示](R150-appendix-unit211-Phi-zero-corrected-second-NV-t-head-original-monic-sigma-and-four-columns.md)、[正确全 t 原坐标](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)与[一般完整缩放 N4 三短式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)。下面从原乘法直接推导，不调用第二头已成二十列、八条新奇部列或任何已冻结 gcd 门。

## 1. 原代数、原向量与误差的约定

置
$$
s=u-1,\quad \delta=1-Q,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell,
$$
$$
a_0=1-\ell,\qquad g=2\ell-1,\qquad
K_w=Q+4s,\qquad T_0=-K_w,
$$
$$
J=2u(1-u)+\ell Q,\qquad
J-Q=-4s^2,\qquad P_{02}=2sL.
\tag{2}
$$
仍在当前正确 Phi 的原权图工作；上述恒等式不恢复被撤回的旧 compact 均值链。

在二次权扩张 $\rho^2=\delta$ 中，
$$
b+c=\ell,\quad bp+cq=u,\quad
p=1+\rho,\quad q=1-\rho,\quad pq=Q.
$$
原代数乘法和迹固定为
$$
(v_0,v_1,v_B,v_C)(w_0,w_1,w_B,w_C)
=(v_0w_0,\ v_0w_1+v_1w_0,\ v_Bw_B,\ v_Cw_C),
$$
$$
\tau(v)=a_0v_0+v_1+bv_B+cv_C .
\tag{3}
$$
取
$$
\mathbf1=(1,0,1,1),\quad
\iota=(1,0,0,0),\quad
e_1=(0,1,0,0),\quad
g_0=(0,0,p,q).
$$
这里 $\iota^2=\iota$，$e_1^2=0$，$\iota e_1=e_1$；尤其不能把原 germ 分量当成独立 simple 分量。

原 Gram 为
$$
(0,0,p,q),\quad (0,A_1,r,r'),\quad
(p,r,0,t),\quad(q,r',t,0).
$$
设
$$
X=a_0p+r+ct,\qquad
Y=a_0q+r'+bt,\qquad
V=bX+cY,\qquad W_1=bpX+cqY,
$$
$$
A_1=2f-2V+2bc\,t,\qquad
E=f-V+bc\,t=A_1/2.
\tag{4}
$$
定义 $\mathcal K v=(\tau(\mathrm{row}_i v))_i$。于是
$$
d=\mathcal K\mathbf1=(u,d_1,X,Y),\qquad
d_1=2f-V-a_0u,\qquad \tau(d)=2f.
$$
完整原二次型为
$$
N_4(v)=2\tau(dv^2)-2f\tau(v^2)
 -4\tau(v)\tau(dv)+4f\tau(v)^2+\tau(v\mathcal K v).
\tag{5}
$$
最后一项始终完整保留。

为避免把原条件暗中设为零，先记
$$
E_0=2W_1-T_0-4uf,\qquad
n_0=N_4(g_0)-2\lambda P_{02}.
\tag{6}
$$
后面的原恢复图才有 $E_0=n_0=0$。以下极化在此之前就是普通原身份。

## 2. 原幂等元的完整极化表

记
$$
\mathcal B(v,w)=N_4(v+w)-N_4(v)-N_4(w).
$$
逐项展开 (5) 得
$$
\begin{aligned}
N_4(\mathbf1)&=0,\\
N_4(e_1)&=4(f-u),\\
N_4(g_0)&=2\lambda P_{02}+n_0,\\
N_4(\iota)&=2\ell(1+2\ell)f-4\ell V+2bc\,t,
\end{aligned}
\tag{7}
$$
以及全部六个交叉项
$$
\begin{aligned}
\mathcal B(\mathbf1,e_1)&=2(u-2f),\\
\mathcal B(\mathbf1,g_0)&=T_0+E_0,\\
\mathcal B(\mathbf1,\iota)&=4\ell f-2V,\\
\mathcal B(g_0,e_1)&=-2E_0,\\
\mathcal B(\iota,e_1)&=
 4\{\ell u+V-(1+2\ell)f\},\\
\mathcal B(\iota,g_0)&=
 g(T_0+E_0)+4u(V-f)-4bc\,t.
\end{aligned}
\tag{8}
$$

这些式子的来源可以直接核定。原迹对称性给
$$
\mathcal B(\mathbf1,v)=2\tau(dv)-4f\tau(v).
$$
同时
$$
\mathcal K e_1=g_0,\qquad
\mathcal K\iota=(0,A_1,X-ct,Y-bt),
$$
$$
\tau(d\iota)=2f-V,\qquad
\tau(g_0\mathcal K\iota)
=\tau(\iota\mathcal K g_0)=W_1-2bc\,t.
\tag{9}
$$
因此 (8) 的最后一式来自
$(2-4a_0)W_1-8\ell uf+4uV-4bc\,t$，再用 (6) 化简。式
$\mathcal B(g_0,e_1)=-2E_0$ 则用
$\tau(g_0^2)=2u-\ell Q$ 直接得到。这里没有调用错误的旧 $d_1^2$ 均值式。

## 3. 整个第二头上的完整 NV 小式

沿同一个原 sigma 恢复，
$$
h=1+\frac{T+m\sigma}{\ell}-\rho\sigma,\qquad
k=1+\frac{T+m\sigma}{\ell}+\rho\sigma,\qquad
w=\lambda-1-T.
$$
令
$$
\beta=-\frac{T+u\sigma}{\ell},\qquad
\alpha=1-\beta .
$$
完整物理向量有准确分解
$$
\mathbf V=(1,w,h,k)
=\alpha\mathbf1+\beta\iota+w e_1-\sigma g_0 .
\tag{10}
$$
在 (1) 上，
$$
\boxed{
\beta=\frac32-\lambda-\sigma,\qquad
T=-\ell\beta-u\sigma,\qquad
2w=1-2a_0\beta+2s\sigma .
}
\tag{11}
$$
没有倒 sigma、m 或任何新头。

定义两个普通二次多项式
$$
C_f=-1+2a_0\beta^2-4s\beta\sigma+4s^2\sigma^2,
$$
$$
C_u=(1-2a_0\beta+2s\sigma)(\beta-2s\sigma).
\tag{12}
$$
则完整原值满足
$$
\boxed{
\begin{aligned}
N_4(\mathbf V)
={}&P+\sigma^2(n_0+2sE_0),\\
P={}&fC_f+uC_u+2E\beta(\beta+2\sigma)\\
&-T_0\sigma(1-2a_0\beta)
 +2\lambda P_{02}\sigma^2.
\end{aligned}}
\tag{13}
$$
式 (13) 保留完整原 $N_4$，不是其最高项、奇部、范数或某个分量。

证明从 (7)–(10) 的十项二次展开开始：
$$
\begin{aligned}
N_4(\mathbf V)
={}&\beta^2N_4(\iota)+w^2N_4(e_1)+\sigma^2N_4(g_0)\\
&+\alpha\beta\mathcal B(\mathbf1,\iota)
 +\alpha w\mathcal B(\mathbf1,e_1)
 -\alpha\sigma\mathcal B(\mathbf1,g_0)\\
&+\beta w\mathcal B(\iota,e_1)
 -\beta\sigma\mathcal B(\iota,g_0)
 -w\sigma\mathcal B(g_0,e_1).
\end{aligned}
\tag{14}
$$
由 (11)，$E_0$ 的系数正好为
$$
\sigma(2w-\alpha-g\beta)=2s\sigma^2.
$$
把 $V=f+bc\,t-E$ 代入剩余项后，全部 t 系数是
$$
bc\,\beta\{4a_0\beta+4w-2-4s\sigma\}=0.
\tag{15}
$$
此处只消去完整多项式的 t 系数，没有施加 $t=0$。

其余 E 系数为 $2\beta(\beta+2\sigma)$，f 系数为
$$
4w^2-4w(1+g\beta)+2g\beta(1-a_0\beta)=C_f,
$$
u 系数为
$$
-4w^2+2w(1+g\beta)=2w(\beta-2s\sigma)=C_u.
$$
这给出 (13) 的全部系数，并且说明 t 消失与完整原迹、germ 交叉项同时相容。

## 4. 只含三个旧分母支持的普通多项式定义

现在使用已经付清的原 $E_0,N_0,P_1$ 恢复：
$$
E=\frac{P_{02}(T+\ell)}{T_0},\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q}.
\tag{16}
$$
在此坐标图 $E_0=n_0=0$，因此 (13) 是
$N_4(\mathbf V)=P$ 的普通恒等式，并非只在第二矩或第三矩理想中成立。

置
$$
e=L(1-\beta)-uQ\sigma,\qquad
D_0=(J-Q)T_0=4s^2K_w,
$$
$$
F=P_{02}T_0\lambda-P_{02}e+sT_0^2.
\tag{17}
$$
于是
$$
E=\frac{P_{02}e}{QT_0},\qquad f=\frac F{D_0}.
$$
再定义
$$
\begin{aligned}
\widehat C_f&=-Q+2(Q-L)\beta^2
              -4sQ\beta\sigma+4s^2Q\sigma^2,\\
\widehat C_u&=\{Q-2(Q-L)\beta+2sQ\sigma\}
                  (\beta-2s\sigma).
\end{aligned}
\tag{18}
$$
下列未展开的短式已经是一个确定的
$\mathbb Q[u,Q,\lambda,\sigma]$ 多项式：
$$
\boxed{
\begin{aligned}
C_{\mathrm{NV},2}={}&F\widehat C_f+D_0u\widehat C_u\\
&+2(J-Q)P_{02}e\,\beta(\beta+2\sigma)\\
&-D_0T_0\sigma\{Q-2(Q-L)\beta\}\\
&+2D_0Q\lambda P_{02}\sigma^2.
\end{aligned}}
\tag{19}
$$
这里 $\beta=3/2-\lambda-\sigma$，而 (2)、(17)–(18) 的全部量都是所列变量的普通多项式。因此
$$
\boxed{
C_{\mathrm{NV},2}=QD_0\,N_4(\mathbf V)
=4Q s^2K_w\,N_4(\mathbf V).
}
\tag{20}
$$
清分母乘子完整且只含旧支持。没有除去或反演
$M$、$m$、$2\ell-1$、任何新的 lambda/sigma 首项、D 或其它完整值。

式 (20) 适用于当前原恢复图，并不藉此把原 Gram 的定义推广到未付 $M=0$ 图。它的意义是：在原图内，完整 NV 可以用 (19) 这个没有 M 分母的短原多项式输入。原多项式的几何总次数满足
$$
\deg_{(\lambda,\sigma)} C_{\mathrm{NV},2}\le3.
\tag{21}
$$
这是由显示公式给出的次数上界；本文没有执行展开、因式、gcd 或 profile 计算。

## 5. 同点二矩仍完整保留

令
$$
V_2=2u-\ell Q=2s^2+2-Q,\qquad
V_3=2V_2-uQ,
$$
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1 .
$$
因为 $h-1=-\beta-p\sigma$、$k-1=-\beta-q\sigma$，同一点的完整二矩误差可直接写为
$$
E_2=\ell\beta^2+2u\beta\sigma+V_2\sigma^2-A_\lambda,
$$
$$
E_3=-\ell\beta^3-3u\beta^2\sigma
 -3V_2\beta\sigma^2-V_3\sigma^3-B_\lambda.
\tag{22}
$$
例如把 $\lambda=3/2-\beta-\sigma$ 代入第一式，得到准确二次
$$
E_2=(\ell-2)\beta^2+2(u-2)\beta\sigma
 +(2s^2-Q)\sigma^2+4\beta+4\sigma-\frac52.
\tag{23}
$$
(19)、(22) 给三个低次数、同一点的原必要条件，保全部复根及重数。由于 (20) 的乘子是旧单位，在当前图上
$$
(E_2,E_3,N_4(\mathbf V))
=(E_2,E_3,C_{\mathrm{NV},2}).
\tag{24}
$$
这只是这三个完整条件的准确改写；没有把它们称为全原系统的充分条件。

物理 t 仍出现在原均值、N1、完整个别 N/P 等其它同点方程中，不能因 (13) 而删除。本文没有计算这三个多项式的共同理想，没有支付任何新头，也没有把已成两个六次 lambda 必要式的首项当成单位。第一头被冻结的三标量 gcd 目标、第二头已成二十列和八条新奇部列的执行身份全部保持不变；本条没有重新执行它们。
