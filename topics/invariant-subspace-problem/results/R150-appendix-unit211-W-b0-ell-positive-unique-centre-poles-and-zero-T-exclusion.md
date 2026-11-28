# R150 后续：W/b0 的 ell 正阶唯一中心、全极点排除与完整 N5 二阶归一

日期：2026-11-29（Asia/Taipei）。作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。

**已证明：** 在当前正确 W/b0 图的任意 1009 位置，若 $v(\ell)>0$，则权剩余必为 $u=-5/4,k=-1/2,Q=9/8$；$\mu=2\lambda-3$ 整，$T$、$\mu$、$\mu^2+4\mu+5$ 均为单位。完整原 $N_5$ 可准确除出 $2\ell^2$，余项在该中心正则。末节只定义首次有限图输入，不预报其空性或执行结果。

## 1. 已付原范围和必要式

沿用
$$
e=u-1,\quad Q=ek,\quad V_{\rm bar}=uk+2,\quad\delta=1-Q,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV_{\rm bar}},\quad
m=u-\ell,\quad M=\delta\ell^2-m^2.
$$
先行[全 e/k/u 单位](R150-appendix-unit211-W-b0-entire-positive-e-ray-exclusion-and-e-k-u-integral-units.md)、
[全 ell 整](R150-appendix-unit211-W-b0-global-ell-integrality-and-Vbar-positive-finite-weight-chart.md)、
[全 Vbar 单位](R150-appendix-unit211-W-b0-entire-Vbar-positive-exclusion-and-1009-integral-unit.md)、
[全 delta 单位](R150-appendix-unit211-W-b0-entire-delta-positive-exclusion-and-1009-integral-unit.md)给
$$
v(e)=v(k)=v(u)=v(Q)=v(\delta)=v(V_{\rm bar})=0,\qquad v(\ell)\ge0.
$$
$v$ 可来自任意有限扩张，以下只比较阶，不假定最小正阶为 1；约定 $v(0)=+\infty$。物理 ell 零支已排，故 $\ell\ne0$。

记
$$
A=\frac{\mu^2+4\mu+5}{2},\quad
B_3=\frac{\mu^3+6\mu^2+12\mu+7}{2}=(\mu+2)A-\lambda,\quad
\lambda=\frac{\mu+3}{2},
$$
$$
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2,\quad
A_*T=uQ\ell\mu,
$$
$$
D=\ell A-T^2,\quad K=\ell^2B_3-3\ell AT+2T^3.
$$
完整原必要式为
$$
q_2=2C_*A+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2=0,\qquad
R_6=MK^2-4m^2D^3=0. \tag{1}
$$
另置
$$
T_0=2u-\ell Q-2u^2,\quad \Phi=T_0+4u-4+Q,\quad
P_{02}=(2-3u)(2u-\ell Q)-Qu+2u^3.
$$
§4 重列完整原 $N_5$。其原理想必要性沿用
[完整 N5 定义源](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)；它不是物理 $f=0$ 的特化。本稿不倒 $D$，也不假定 $A_*$ 为单位。

## 2. Astar 单位的整个 ell 正阶图排除

设 $a=v(\ell)>0$，于是 $m,M$ 为单位，剩余为 $u,-u^2$。
若 $v(A_*)=0$，原线性式给 $T=\ell\beta\mu$，其中 $\beta=uQ/A_*$ 为单位。

若 $s=v(\mu)<0$，则
$$
v(D)=a+2s,\qquad v(K)\ge2a+3s.
$$
$MK^2$ 的阶至少 $4a+6s$，而 $4m^2D^3$ 准确为 $3a+6s$，不能相消。

若 $\mu$ 整，则 $v(T)\ge a$，$C_*$ 为单位。由 $q_2$ 得 $v(A)\ge a$。
在 $\bar A=0$ 时 $\bar B_3=-\bar\lambda\ne0$，因为 $\lambda=0$ 给 $A(-3)=1$。
故 $v(D)\ge2a,v(K)=2a$，$R_6$ 两项阶为 $4a$ 和至少 $6a$，矛盾。
这也覆盖 $\mu=T=0$，其 $A$ 常数已直接矛盾。因此必有 $v(A_*)>0$，允许 $A_*=0$。

## 3. 唯一中心和全部 mu/T 极点排除

在 $\bar\ell=0$ 上，
$$
\bar A_*=2\bar u(2\bar Q+\bar u-1)=2\bar u\bar e(2\bar k+1).
$$
所以 $\bar k=-1/2$。原 ell 分子在该 k 的剩余为 $u+5/4$，故
$$
\boxed{\bar u=-5/4,\quad\bar e=-9/4,\quad\bar k=-1/2,\quad
\bar Q=9/8,\quad\bar\delta=-1/8,\quad\overline{V_{\rm bar}}=21/8.} \tag{2}
$$
并有
$$
\bar m=-5/4,\quad\bar M=-25/16,\quad\bar J=-45/8,\quad
\bar A_*=0,\quad\bar T_0=45/8,\quad\bar\Phi=-9/4,\quad
\bar P_{02}=-135/8. \tag{3}
$$
这里 $M,Q,\Phi$ 都已付为真正赋值单位。

由 $C_*=4uQ\delta\ell^2-MA_*$，定义
$$
\widetilde q=4u\delta DT-M\{u\mu A+(3+2\mu)T\},
$$
便有完整身份
$$
Q\ell\widetilde q-\frac T2q_2-MA(A_*T-uQ\ell\mu)=0. \tag{4}
$$
物理原点满足 $\widetilde q=0$；右式不含 ell 或 $A_*$ 的逆。

还有
$$
K^2+4D^3=\ell^2C_3,\qquad
C_3=4B_3T^3-3A^2T^2-6\ell AB_3T+\ell^2B_3^2+4\ell A^3,
$$
$$
R_6/\ell^2=\delta K^2-m^2C_3. \tag{5}
$$
这是原因子的准确约去，其正则性由右式支付，并未把 ell 称为单位。

设 $s=v(\mu)<0,t=v(T)$。(4) 的四项阶为
$a+2s+t,3t,3s,s+t$。若 $t<s$，$T^3$ 唯一最低；若 $t>s$，$\mu A$ 唯一最低。故 $t=s$，原线性式还给 $v(A_*)=a$。
置 $\alpha=\overline{T/\mu}$，(4)、(5) 最低项给
$$
\alpha^3=\bar u^2/(8\bar\delta)=-25/16,\qquad
4\bar\delta\alpha^4-2\bar u^2\alpha+3\bar u^2/4=0.
$$
代入第一式，第二式迫 $\alpha=1/2$，两个立方值却相差 $27/16\ne0$。
所以 $\mu$ 整。若此时 $T$ 有极点，(4) 又只有 $T^3$ 最低，故
$$
\boxed{v(\mu)\ge0,\quad v(T)\ge0.} \tag{6}
$$
$A_*=0$ 的精确情形由原线性式给 $\mu=0$，同一 $T^3$ 比较仍适用，无需假定 $v(A_*)$ 有限。

## 4. 完整 N5 的显式 ell² 归一及证明

以下对完整参数和自由 $T,\mu$ 恒成立，不先使用 W、$q_2$ 或原线性式。简写 $l=\ell$，置
$$
G=\lambda P_{02}+(u-1)T_0,\quad P_c=QP_{02}(l+T)-GT_0,\quad
B=P_c/(Q\Phi),\quad V_s=-G/Q-B,
$$
$$
y=(lT_0/2-uV_s)/M,\quad w=\lambda-1-T,\quad\theta=u-lQ.
$$
完整原定义为
$$
z_1=2(l\mu-2T)y-2lw-4mTB/M,\qquad z_2=2V_s+2B-4my,
$$
$$
Z_0=2(T-l\mu)(luw+V_sT)-2BT^2,\qquad
N_5=2mD(Z_0+Dz_2)+MKz_1. \tag{7}
$$
只有 (3) 已付的 $M,Q,\Phi$ 出现在分母。准确地，
$$
\boxed{N_5=2l^2H,} \tag{8}
$$
$$
\begin{aligned}
H={}&\frac{2m}{M}(A-\mu T)
 [(\tfrac12mT_0-\theta V_s)T^2+MAV_s]\\
&+y[\delta K(l\mu-2T)-m^2(4A^2-2B_3T-3\mu AT+l\mu B_3)]\\
&+w[m\{-2T^3+(2u-3m)AT+2u\mu T^2\}
 +l\{-2muA\mu+m^2B_3-\delta K\}]\\
&+2mB(A^2-B_3T).
\end{aligned} \tag{9}
$$
给出直接展开证明。收集 (7) 的 $y,w,V_s,B$ 项得
$$
N_5/2=yY+lwW+2mlD(A-\mu T)V_s+2ml^2B(A^2-B_3T),
$$
其中 $Y=MK(l\mu-2T)-4m^2D^2$、$W=2muD(T-l\mu)-MK$。
利用 $M=\delta l^2-m^2,u-m=l$，逐项展开为
$$
Y=2m^2lT^2(A-\mu T)
+l^2[\delta K(l\mu-2T)-m^2(4A^2-2B_3T-3\mu AT+l\mu B_3)],
$$
$$
W=lm[-2T^3+(2u-3m)AT+2u\mu T^2]
+l^2[-2muA\mu+m^2B_3-\delta K].
$$
又 $M+mu=l\theta$ 给
$$
mT^2y+DV_s=\frac lM[(mT_0/2-\theta V_s)T^2+MAV_s].
$$
代回便是 (8)–(9)。没有倒 $l,A_*,D,T$，也没有以最高头代替完整 N5。

## 5. T 剩余为零的全部情形

由 (4)、(6)，$\bar T=0$ 迫 $\bar\mu\bar A=0$。
设 $U=-5/4,Q_0=9/8,\Delta=-1/8$，以下 $A,B_3,\mu,T$ 为剩余变量。
令
$$
G_0=-135(2\mu+9)/32,\quad
B_0=\frac{(-135/8)T-G_0(45/8)/Q_0}{-9/4},\quad
V_0=-G_0/Q_0-B_0.
$$
(9) 在 (2) 的完整剩余为
$$
\begin{aligned}
H_0={}&-2(A-\mu T)[(45/16-V_0)T^2-UAV_0]\\
&+(V_0/U)[-4\Delta T^4-U^2(4A^2-2B_3T-3\mu AT)]\\
&+Uw[-2T^3-UAT+2U\mu T^2]+2UB_0(A^2-B_3T).
\end{aligned} \tag{10}
$$
当 $T=0$，
$$
H_0=(225/4)(2\mu+9)A^2. \tag{11}
$$
若 $\bar\mu=0$，(11) 非零，矛盾。

若 $\bar A=0$，则 $\bar\mu,3+2\bar\mu,\bar B_3=-\bar\lambda,\bar G_0$ 全非零：
$A(-3/2)=5/8,A(-3)=1,A(-9/2)=29/8$。
设 $t=v(T)>0$。原线性式给 $b=v(A_*)=a-t$，所以 $0<b<a$、$v(C_*)=b$。
$q_2$ 第二项阶准确为 $a$，末项阶高于 $a$，因而
$$
v(A)=a-b=t. \tag{12}
$$
在完整 (9) 中，除 $2uB_3(V_s-B)T$ 外全部项阶严格高于 $t$：
含 $A^2,AT,T^2$ 的项至少 $2t$；显式 ell 低项至少 $a>t$；$K$ 项也更高。
而在本中心 $l=T=0$，
$V_0-B_0=-6G_0/Q_0$，故
$$
\overline{H/T}=-12U\bar B_3G_0/Q_0\ne0,
$$
与 $H=0$ 矛盾。若 $T=0$ 精确成立，原线性式直接迫 $\mu=0$，已排。
因此
$$
\boxed{v(T)=0.} \tag{13}
$$

## 6. 剩余三式及真正已付的 mu 支持

(4)、(5) 在 (2) 精确给
$$
\bar{\widetilde q}=(5/64)\widehat Q,\qquad
\overline{R_6/\ell^2}=(T^2/16)\widehat R,
$$
$$
\widehat Q=-8T^3-25\mu A+20(3+2\mu)T,\qquad
\widehat R=-8T^4-100B_3T+75A^2. \tag{14}
$$
第三式是完整 $H_0$。因此可使用三条完整必要式
$$
\bar{\widetilde q},\qquad
\overline{R_6/\ell^2}/T^2,\qquad H_0. \tag{15}
$$
此处除 $T^2$ 仅使用已经独立证明的 (13)。

若 $\bar\mu=0$，(14) 给 $T^2=15/2$ 和 $75/4-350T=0$，后者即 $T=3/56$。
两者要求 $23511=0$，而 $23511\equiv304\pmod{1009}$。

若 $\bar A=0$，则 $B_3=-(\mu+3)/2$、$2\mu+3\ne0$。由 (14)，
$$
T^2=(5/2)(2\mu+3),\quad T^3=-25B_3/2,\quad
T=\frac{5(\mu+3)}{2(2\mu+3)}.
$$
故 $5(\mu+3)^2=2(2\mu+3)^3$。模 $\mu^2+4\mu+5$ 化简为 $7\mu+3=0$，
而该二次在 $-3/7$ 的值为 $170/49\ne0$。于是
$$
\boxed{v(\mu)=v(\mu^2+4\mu+5)=0.} \tag{16}
$$
这些单位仅在当前 T 单位图使用，未外推至一般原图。

## 7. 首次有限图输入，不预记执行结果

新自含源 **2026-11-29-unit211-W-b0-ell-positive-unique-centre-three-original-scalars-8542.py**；
Git blob **57f37a7f16fc48cabb61ad9497ec953970476855**；
SHA-256 **16404dd1f2da2c7406d86bc5a4cb5cad4c14a8634cde4b2b68077fe427de1aef**；
13898 字节。固定 120 秒 / 1 GiB，外层 135 秒，无历史执行依赖。

源码保 ell 为普通变量，以完整 (7) 精确除出 $2\ell^2$，返回 (8)–(10)。
再对 (15) 使用 T 容量 $(3,4)$、$(3,5)$ 的两个固定完整 Sylvester 方阵；
全部 cofactor 坐标和全部三个原乘子均回乘，不以一个行列式摘要代替来源。

只在这两个新纯 mu scalar 完成后，首次作同一 $\mathbb F_{1009}[\mu]$ Bézout。
只准去除 (16) 的支持 $\mu(\mu^2+4\mu+5)$；末组合须完整返回三条 (15)。
若剩余必要多项式不是常数，保留其全部根；非零多项式不冒称单位。

本输入不选 T 或 mu 根，不倒未付头，不复算任何旧 ray/边界门，不换素数或提高预算。
纸面已排全部极点及 T 零支；(15) 的有限图是否为空，仍以该唯一真实执行的原返回为准。
