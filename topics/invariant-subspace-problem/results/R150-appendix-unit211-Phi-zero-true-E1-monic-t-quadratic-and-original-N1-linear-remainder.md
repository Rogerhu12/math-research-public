# R150：正确 Phi 的真 E1 首一 t 二次与完整 N1 一次余式

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**新增原结构。** 在当前正确 Phi 规范中，将 $\lambda,T$ 固定为系数变量，真实 dual-germ 均值 $E_1$ 本身就有已付纯权 $t^2$ 头：
$$
\boxed{[t^2]E_1=-\frac{bc\,\ell Q}{2\delta}.}
\tag{1}
$$
完整原第一 jet 的 $t^2$ 头准确为其 $2(u-1)$ 倍。因此
$$
\boxed{\mathcal L_N:=N_1-2(u-1)E_1
       \quad\text{是关于 }t\text{ 的至多一次式}.}
\tag{2}
$$
下面给出它的实际一次系数及完整原定义。此结论不需要第二 NV 头，不反演 $m,D,3-2\ell$ 或任何新的几何首项；它仅使用 Phi 恢复中的 $f_t=(A_1)_t=0$。一般 W 的恢复有额外 Phi 项，不能把本稿直接移到 W。

已有的[全 Phi 首一 t 二次呈示](R150-appendix-unit211-Phi-zero-corrected-whole-monic-t-quadratic-exact-ten-columns-and-four-generator-NV-head.md)继续正确。本稿的新量是可以直接选真 $E_1$ 为首一源，以及 (2) 的完整 jet 消项和显示一次系数；没有重跑其旧列、cofactor 或任何 gcd。

## 1. 同点恢复与真实 t 方向

使用正确原规范
$$
s=u-1,\quad \delta=1-Q,\quad p=1+\rho,\quad q=1-\rho,
\quad \rho^2=\delta,\quad p+q=2,\quad pq=Q,
$$
$$
b+c=\ell,\quad bp+cq=u,\quad m=u-\ell,\quad
M=4bc\delta=\ell^2\delta-m^2,\quad \theta=u-\ell Q.
$$
在 Phi 图，
$$
L=Q-2s(u-2),\quad \ell=L/Q,\quad
T_0=-Q-4s,\quad J=Q-4s^2,\quad P_{02}=2sL.
$$
保留原 $E_0,N_0,P_1$ 的准确仿射恢复：
$$
E=\frac{A_1}{2}=\frac{P_{02}(T+\ell)}{T_0},
\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},
$$
$$
V=f-E+bc\,t,\qquad W_1=\frac{T_0}{2}+2uf .
\tag{3}
$$
这些恒等式来自真正 Gram，未借用已撤回的错误 compact $R$。这里 $E,f,W_1$ 关于 $t$ 均为常数。

置 $V_0=f-E$，并定义
$$
x_0=\frac{\theta V_0-mW_1}{M},\qquad
y_0=\frac{\ell W_1-uV_0}{M},
\qquad X_0=x_0+\rho y_0,\quad Y_0=x_0-\rho y_0 .
$$
完整同点原均值为
$$
X=\frac{W_1-qV}{b(p-q)},\qquad
Y=\frac{pV-W_1}{c(p-q)}.
$$
于是
$$
X=X_0-\frac{cq}{2\rho}t,\qquad
Y=Y_0+\frac{bp}{2\rho}t,
$$
$$
r=X-(1-\ell)p-ct,\qquad
r_C=Y-(1-\ell)q-bt,
\tag{4}
$$
所以
$$
X_t=-\frac{cq}{2\rho},\quad
Y_t=\frac{bp}{2\rho},\quad
r_t=-\frac{cp}{2\rho},\quad
(r_C)_t=\frac{bq}{2\rho}.
\tag{5}
$$
所有分母均是旧原权单位。也可完全不取 $\rho$ 写
$$
x=x_0+\frac{\theta}{4\delta}t,\qquad
y=y_0-\frac{u}{4\delta}t.
$$
这保留两个谱标签及其共轭；没有选一个物理根或反演 $m$。

## 2. 真 dual-germ 原定义

置 $a_0=1-\ell$。四行 Gram 为
$$
g_0=(0,0,p,q),\quad
g_1=(0,A_1,r,r_C),\quad
g_B=(p,r,0,t),\quad
g_C=(q,r_C,t,0).
$$
迹与乘法必须取
$$
\tau(v)=a_0v_0+v_1+bv_B+cv_C,
$$
$$
(vz)_0=v_0z_0,\quad
(vz)_1=v_0z_1+v_1z_0,\quad
(vz)_B=v_Bz_B,\quad
(vz)_C=v_Cz_C.
$$
令 $\mathbf1=(1,0,1,1)$，
$$
(\mathcal Kv)_i=\tau(g_iv),\qquad
d=\mathcal K\mathbf1=(u,d_1,X,Y),\qquad F_2=\tau(d)=2f.
$$
这里
$$
d_1=2f-V-a_0u,\qquad (d^2)_1=2ud_1.
\tag{6}
$$
真实 $E_1$ 的第一项也是 dual 系数：
$$
E_1=2\tau(g_0g_1)-2(\mathcal Kd)_1-4ud_1+4fd_1 .
\tag{7}
$$
不能将 $2ud_1$ 替换成 $d_1^2$。

记
$$
V_2=bp^2+cq^2=2u-\ell Q,\quad
W_r=bpr+cqr_C,\quad
S_1=bXr+cYr_C,\quad
S_2=bpXr+cqYr_C.
$$
真实乘法给
$$
W_r=W_1-a_0V_2-2bc\,t,\qquad
(\mathcal Kd)_1=uA_1+S_1.
$$
因此完整 (7) 为
$$
\boxed{E_1=2W_r-2uA_1-2S_1+4(f-u)d_1.}
\tag{8}
$$

## 3. 直接显示 E1 的全部 t 系数

从 (4)–(5)，
$$
[t^2]S_1=bX_tr_t+cY_t(r_C)_t
       =\frac{bc\,\ell Q}{4\delta},\qquad
[t]S_1=-2bc\,y_0,
$$
$$
[t]W_r=-2bc,\qquad [t]d_1=-bc.
\tag{9}
$$
令
$$
d_{10}=f+E-a_0u,\qquad
S_{10}=bX_0(X_0-a_0p)+cY_0(Y_0-a_0q),
$$
$$
c_E=2(W_1-a_0V_2)-4uE-2S_{10}
                  +4(f-u)d_{10}.
$$
(8) 逐项得到
$$
\boxed{
E_1=-\frac{bc\,\ell Q}{2\delta}t^2
 +4bc(y_0-f+s)t+c_E.}
\tag{10}
$$
其中 $c_E$ 对 $(\lambda,T)$ 总次数至多二。由于 $bc,\ell,Q,\delta$ 都是当前原权单位，
$$
\boxed{
q_E=-\frac{2\delta}{bc\,\ell Q}E_1
=t^2-\frac{8\delta}{\ell Q}(y_0-f+s)t
       -\frac{2\delta}{bc\,\ell Q}c_E}
\tag{11}
$$
是在完整当前权图成立的首一 $t^2$。其一次系数总 $(\lambda,T)$ 次数至多一，常数系数至多二。支付 (11) 不需要 $2u-3$、$3-2\ell$、$T$ 或 $\lambda$ 的逆。

## 4. 完整 N1 的极化，不只保一个最高项

定义完整
$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)
       -4\tau(v)\tau(dv)+2F_2\tau(v)^2+\tau(v\mathcal Kv).
$$
原第一 jet 为
$$
N_1=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)-4\lambda wP_{02}.
\tag{12}
$$
用真正 dual 乘法逐项极化：
$$
\tau(g_0)=u,\quad \tau(g_1)=d_1,\quad
\tau(dg_0)=W_1,\quad \tau(dg_1)=uA_1+S_1,
$$
$$
\tau\!\left(g_0\mathcal Kg_1+g_1\mathcal Kg_0\right)
=2A_1V_2+2bc\,t(pr_C+qr).
$$
因此完整原式为
$$
\boxed{\begin{aligned}
N_1={}&4S_2-4fW_r-4u(uA_1+S_1)-4d_1W_1
       +8fu d_1\\
 &+2A_1V_2+2bc\,t(pr_C+qr)-4\lambda wP_{02}.
\end{aligned}}
\tag{13}
$$
(13) 包含全部 Gram 与 jet 项，并非仅在均值理想中相等。

由 (5)，
$$
[t^2]S_2=\frac{bcQ(2\ell-u)}{4\delta},\qquad
[t](pr_C+qr)=\frac{Qm}{2\delta}.
$$
所以
$$
\begin{aligned}
[t^2]N_1
&=\frac{bcQ}{\delta}
  \left[(2\ell-u)-u\ell+m\right]\\
&=-\frac{bc\,\ell Q(u-1)}{\delta}
 =2(u-1)[t^2]E_1 .
\end{aligned}
\tag{14}
$$
这里 $m=u-\ell$ 只作为恒等式使用，没有反演。其他项至多一次于 $t$，因为 $A_1,f,W_1,\lambda,w$ 都与 $t$ 无关。

## 5. 一次余式的实际完整系数

由 (8)、(13)，原式的精确差为
$$
\begin{aligned}
\mathcal L_N={}&4(S_2-S_1)-4(f+s)W_r
 +(-4W_1+8f+8su)d_1\\
 &-2\ell Q A_1+2bc\,t(pr_C+qr)-4\lambda wP_{02}.
\end{aligned}
\tag{15}
$$
在 $t=0$ 处记
$$
S_{20}=bpX_0(X_0-a_0p)+cqY_0(Y_0-a_0q).
$$
令
$$
\begin{aligned}
a_N={}&4(S_{20}-S_{10})-4(f+s)(W_1-a_0V_2)\\
 &+(-4W_1+8f+8su)d_{10}
 -4\ell Q E-4\lambda wP_{02}.
\end{aligned}
$$
再由 (4) 得
$$
[t](S_2-S_1)=-2bc\,x_0+a_0bcQ,\qquad
(pr_C+qr)|_{t=0}=2x_0-2\delta y_0-2a_0Q .
$$
代入 (15)，所有显示项给
$$
\boxed{
\mathcal L_N=a_N+b_Nt,\qquad
b_N=4bc\left(W_1-x_0-\delta y_0-2s^2\right).}
\tag{16}
$$
$a_N$ 对 $(\lambda,T)$ 总次数至多二，$b_N$ 至多一。没有把 $b_N$ 宣布为单位；其整零面必须保留。

(10)、(16) 都是普通原多项式身份。它们给精确双向理想等式
$$
(E_1,N_1)=(q_E,\mathcal L_N)
\quad\text{于当前原已付系数环的 }A[\lambda,T,t].
\tag{17}
$$
右向用 (11)、(2)，左向用
$E_1=-(bc\ell Q/(2\delta))q_E$ 与
$N_1=\mathcal L_N+2sE_1$。没有除 $b_N$，所以 (17) 包含一次余式降头或恒零的全部纤维。

## 6. 对后继原值模型的准确用途

完整 $E_B,E_C$ 也都是总 $(\lambda,T,t)$ 次数至多二。用 (11) 一次短除后，其 $t$ 余式至多一次。故四个原条件
$$
E_1,\ E_B,\ E_C,\ N_1
$$
可以先用真正的 $q_E$ 作首一二次环境，再保三条原一次余式及各自的 $t$ 倍。这是已知两生成呈示原理的一种新的显示原源选择；没有实际重建或重算此前六列/十列门。

在第二 NV 头上，再代 $T=\ell(\lambda-3/2)-m\sigma$，(10)–(17) 全部成立。前篇完整 $E_2,E_3,NV$ 的五生成必要代数因而可以直接添这个首一二次，得到至多十个权模生成元。所有原均值、jet、两个 singleton 的完整 N/P 仍须在同一点施加；这些必要结构没有支付充分性或第二头空性。

物理 $D$ 的后续局部化只取开集，不能免费宣称局部化后的全权模仍有限或自由。本稿也没有对 $\rho$ 或原 $U_0$ 尺度作点数/长度声明。

## 7. 来源与执行边界

原恢复与真 dual 乘法来自已纠正的 Phi 定义；本稿显示 (7) 中完整 $(d^2)_1=2ud_1$，不沿错误 compact $R$ 链。原仿射恢复可对照首部已引的正确全 Phi 首一二次稿；本稿 (3)、(7)、(12) 另给全部所需的准确同点定义，不需要再读旧系数载荷或运行旧源。

这是新的完整纸面恒等式稿，没有新脚本、数值验算或 Actions 运行。全部系数由 (4)–(5) 的原斜率和 (8)、(13) 的完整原式逐项得到；同组已独立复算两个二次头。未把这个纸面推导写成机器实际回执，也没有重跑任何已成或冻结目标。
