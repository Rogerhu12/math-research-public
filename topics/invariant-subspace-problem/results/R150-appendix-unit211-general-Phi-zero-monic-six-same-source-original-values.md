# R150 附录：整 $\Phi=0$ 面的同源值恢复与八条首一六次商内原式

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 范围与结论

本文限于一般 unit211 的原 LS 剩余图及整 $\Phi=0$ 权面。此前完成的原权面排除继续有效，尤其 $u,Q,1-Q,\ell,u-\ell,T_0,J-Q$ 非零；原物理输入还给出 $bcP_{02}\lambda D\ne0$。已闭的 $S=0$、$L=0$ 整支使本图 $S\zeta\ne0$。这些单位只用于其原结论覆盖的范围。

本次新增输入先用原矩关系、原 $P_1$、原 $N(V)$ 恢复同一个 $f,t$，再恢复同一张完整原 Gram 矩阵。由这张矩阵的三条均值、原 $N_1$ 及两 singleton 的个别 $N/P$ 方程得到八条必要式。其分子均在同一个首一六次矩关系下逐次约化至 $T$ 次数不超过 $5$，而几何分母保留为原单位 $D$ 与 $P=S_nZ$ 的分别幂。

没有证明整 $\Phi=0$ 面为空，没有把六次商中的降次误称为全解判空；也没有倒置 $D$ 或 $P$ 在六次商中的代数范数。

## 2. 原权参数与单首一矩关系

记
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad
\Phi=T_0+4u-4+Q,\quad P_f=T_0(J-Q).
$$
整 $\Phi=0$ 面精确参数化为
$$
\ell=1-\frac{2(u-1)(u-2)}Q,
$$
只除原单位 $Q$。在此面，
$$
T_0=-Q-4(u-1),\quad J-Q=-4(u-1)^2,\quad
P_{02}=2(u-1)\ell Q.
$$
设
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,\quad
m=u-\ell,\quad M=\ell V_2-u^2.
$$
原值中心取
$$
D=\ell A_2-T^2,\quad s_n=\ell B_3-A_2T,\quad z_n=TB_3-A_2^2,
$$
$$
K=\ell^2B_3-3\ell TA_2+2T^3,\quad
Z=u s_n-2TD,\quad S_n=s_n+(3-2\lambda)D.
$$
原矩方程给出
$$
F_6=M K^2-4m^2D^3=0. \tag{2.1}
$$
其 $T^6$ 系数精确为
$$
4(M+m^2)=4\ell^2(1-Q), \tag{2.2}
$$
是已付权单位。因此可以化成首一六次关系，随后每次乘法立即约化 $T^6,\ldots,T^{10}$。程序每一次均核完整系数身份
$$
\text{原卷积}=\text{余式}+\text{商}\cdot\text{首一 }F_6,
$$
没有用数值代点代替。

## 3. 原矩关系恢复同一组值

在本图定义
$$
\zeta=\frac Z{2mD},\quad v_0=\frac{s_n}{2D},\quad
v_1=-\frac K{2mD},\quad S=\frac{S_n}D,\quad z=\frac{z_n}D. \tag{3.1}
$$
原始矩关系为
$$
H_A=\ell M\zeta^2-2TM\zeta+V_2T^2-u^2A_2,
$$
$$
H_B=u^2\{B_3-2v_0A_2+(v_0^2-(1-Q)v_1^2)T\}.
$$
由
$$
K+2TD=\ell s_n,\quad \ell Z=2mTD+uK,\quad m s_n-Z+K=0
$$
直接得到
$$
v_1=v_0-\zeta,\quad
H_A=\frac{u^2F_6}{4\ell m^2D^2},\quad H_B=-\frac{T H_A}{\ell},
$$
$$
v_0^2-(1-Q)v_1^2-\frac{z_n}D
=-\frac{F_6}{4\ell^2m^2D^2}.
$$
故 (2.1)、(3.1) 支付完整原矩来源。

选定原有序平方根 $\rho^2=1-Q$，令
$$
b=\frac\ell2+\frac{m\rho}{2(1-Q)},\quad
c=\frac\ell2-\frac{m\rho}{2(1-Q)},\quad p=1+\rho,\quad q=1-\rho.
$$
于是 $bc=M/[4(1-Q)]$，实际值为
$$
h=1+v_0+v_1\rho,\quad k=1+v_0-v_1\rho,\quad
w=\lambda-1-T,\quad V=(1,w,h,k).
$$
程序核回原二、三矩、$L=-2\rho\zeta$ 与 $D=bc(h-k)^2$。特别
$$
P=S_nZ=2mD^2S\zeta
$$
为原单位。这不是范数非零假设。

## 4. 原 $P_1$ 与原 $N(V)$ 唯一恢复 $f,t$

置
$$
G=\lambda P_{02}-(1-u)T_0,\qquad
P_c=QP_{02}(\ell+T)-GT_0.
$$
一般原 $P_1$ 为 $P_ff+bcQ\Phi t+P_c=0$。在本面，
$$
f=-P_c/P_f. \tag{4.1}
$$
完整原 $N(V)$ 线的紧凑分子是
$$
N_{F4}=4m\{(3-4\lambda)QD^2-Jz_nD\}
+2S_n(-2uQK+JZ),
$$
$$
\begin{aligned}
N_{C4}={}&4mGz_nD-2GS_nZ-QT_0S_nK\\
&+4mQwu(3-2\lambda)D^2+2mQwu s_nD
-2Qw(u-\ell Q)KD.
\end{aligned}
$$
有 $N_{F4}=4mD^2N_F$、$N_{C4}=4mD^2N_C$，且原 $t$ 系数乘相同尺度后为 $2bcQS_nZ$。所以
$$
t=-\frac{N_{F4}f+N_{C4}}{2bcQP}. \tag{4.2}
$$
$f$ 只有权分母，$t$ 的几何分母只有 $P$。

[完整原值 atlas](../notes/2026-11-27-unit211-generic-LS-Delta-zero-global-monic-value-quadratic-original-return-8542.py)
已经逐项支付原始恒等式
$$
\frac Q2N(V)=N_Ff+N_Tt+N_C-\frac{Qf}{u^2}H_A.
$$
本次在同一个商、同一个 $f,t$ 上核得 $H_A=0$ 和完整第二原线为零，因此确实得到原 $N(V)=0$。未把已付的整个 atlas 再展开设为额外登记门槛。

## 5. 同一张原 Gram 与八条必要式

令
$$
W_1=T_0/2+2uf,\quad
W_2=uT_0+\lambda P_{02}+(V_2+2u^2)f-bcQt.
$$
原 $E_0,N_0$ 唯一恢复
$$
X=\frac{qW_1-W_2}{bp(q-p)},\quad
Y=\frac{W_2-pW_1}{cq(q-p)}.
$$
所有分母均为原单位。置 $a=1-\ell$，
$$
r_G=X-ap-ct,\quad s_G=Y-aq-bt,\quad
A_G=2f-2bX-2cY+2bct.
$$
完整 Gram 行为
$$
R_0=(0,0,p,q),\quad R_1=(0,A_G,r_G,s_G),\quad
R_B=(p,r_G,0,t),\quad R_C=(q,s_G,t,0).
$$

在原代数 $\mathbb C[\varepsilon]/(\varepsilon^2)\oplus\mathbb C^2$ 中，
$$
xy=(x_0y_0,x_0y_1+x_1y_0,x_2y_2,x_3y_3),\quad
\tau(x)=ax_0+x_1+bx_2+cx_3.
$$
令 $\mathbf1=(1,0,1,1)$，
$$
\mathcal Kx=(\tau(R_ix))_i,\quad d=\mathcal K\mathbf1,\quad F_2=\tau(d)=2f.
$$
使用完整原式
$$
N_4(x)=2\tau(dx^2)-F_2\tau(x^2)-4\tau(x)\tau(dx)
+2F_2\tau(x)^2+\tau(x\mathcal Kx),
$$
$$
P_2(x)=\tau((x-\tau(x)\mathbf1)^3).
$$
三条原均值使用 dual 的原极化项与 singleton 的平方项；原 $N_1$ 使用 $N_4$ 的完整极化与原 $P_j$。程序直接从这些原定义形成八条记录：
$$
E_1,\ E_{B,\mathrm{even}},\ E_{B,\mathrm{odd}},\ N_1,
$$
$$
(N_4(R_B)-2\lambda P_{02}h^2)_{\mathrm{even,odd}},\quad
(P_2(R_B)-P_{02}h^3)_{\mathrm{even,odd}}.
$$
even/odd 是相对于原 $\rho^2=1-Q$ 的两系数。程序还构造 $C$ 行并核回两组共轭身份，故全部个别 singleton 方程都保留，未只取 weighted NS/PS 投影。

## 6. 实际返回与限制

本次首次实际执行：

- [原源](../notes/2026-11-27-unit211-general-Phi-zero-monic-six-actual-value-return-8542.py) SHA256：1218c370659ea487450279925224b57b2c729453d623fd6f086a962d3281963e。
- run 45985974447，job 140461582032，内部退出码 0。
- 驱动时间 69.226597096 秒，最大子进程 RSS 180608 KiB。
- stdout 8665 字节，SHA256：509a5900d6aae64a6dd083d43c1c664f95eed1ef51a8513b3604e4325ba2e392。
- 原源及真实 pull 提交均为 e4f22fb07d4f0c4ef5606fc82961976c2d4f9251；10:54:23.602775 UTC 两份 README blob 无变。

只剥原已付权因子后，变量顺序 $(u,Q,\lambda,T)$：

| 原式 | 分子次数 | 项数 | 几何分母幂 $(D,P)$ |
|---|---|---:|---|
| $E_1$ | $(23,13,14,5)$ | 12424 | $(0,2)$ |
| $E_B$ even | $(25,15,14,5)$ | 15393 | $(0,2)$ |
| $E_B$ odd | $(25,14,14,5)$ | 14424 | $(0,2)$ |
| $N_1$ | $(22,12,14,5)$ | 11437 | $(0,2)$ |
| $N_B$ even | $(40,23,25,5)$ | 74812 | $(2,3)$ |
| $N_B$ odd | $(39,22,25,5)$ | 71932 | $(2,3)$ |
| $P_B$ even | $(42,25,27,5)$ | 94451 | $(3,3)$ |
| $P_B$ odd | $(41,24,27,5)$ | 91124 | $(3,3)$ |

回执保留每一分子的 SHA256、原分母及剥因子记录。六次商执行 3646 次完整原差约化，核查 23388 个系数身份。几何逆只来自显名原单位，参数逆均有已付权因子的除法回乘审计。

分子次数受控不表示几何局部化后仍是六个基元的自由模，也不表示任一必要式的 $T$ 首项可倒置。本文保留全部此类零纤维；它完成新的同源必要值输入，原解存在性仍须由这些原式进一步决定。
