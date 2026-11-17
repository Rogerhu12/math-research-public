# R5：退化负曲率入口的圆弧保持与加权能量

2026-11-17，Astra-held10-f00f08c9-20261117 / root、new_construction。

这是一个**条件定理的完整经典证明**：假定一个具有指定 Cauchy 数据、指定旋转度量的 $C^3$ 浸入已经存在，则其精确圆弧数据必在下述特征区域内保持为显式局部旋转片。定理不构造完整闭曲面，不证明 true-prefix 边值问题有解，也不将任意 $C^2$ 浸入自动提升为 $C^3$。

## 1. 定理及正则性

令 $a\in C^3([0,S])$，满足

$$
a(0)=1,\quad a'(0)=a''(0)=0,\quad a(s)>0.
$$

假设存在 $0<L<S$，使

$$
a''(s)>0\quad(0<s<L),\qquad
 a''(s)=0\quad(L\le s\le S),
$$

且在某个初始区间 $[0,\tau_0]$ 上 $a''$ 非减。令 $k>\sup_{[0,S]}|a'|$。给定一个 $C^3$ 浸入

$$
X:[0,S]\times\mathbb S^1\longrightarrow\mathbb R^3,
\qquad X^*g_{\rm Euc}=ds^2+a(s)^2du^2.
$$

假定整个初始闭曲线 $\Gamma(u)=X(0,u)$ 位于水平面内、按单位弧长参数化、严格凸，并且

$$
X_s(0,u)=e_z\quad\text{对全部 }u.
$$

这里“严格凸”具体要求其有向曲率在紧的初始圆周上具有正下界。假定在一个开材料区间 $I=(u_-,u_+)$ 上，它精确为半径 $1/k$ 的圆弧：

$$
\Gamma(u)=c+\frac1k e(ku+\phi_0).
$$

定义

$$
Z(s)=\int_0^s\sqrt{1-a'(r)^2/k^2}\,dr,
\qquad
X_0(s,u)=c+\frac{a(s)}k e(ku+\phi_0)+Z(s)e_z,
$$

以及

$$
c_0(s)=\sqrt{\frac{a''(s)}{a(s)(k^2-a'(s)^2)}},\quad
\chi(s)=\int_0^s c_0(r)\,dr\qquad(0\le s\le L).
$$

则只要相应区间非空，

$$
X(s,u)=X_0(s,u)\quad\text{当 }0\le s\le L,
\quad u_-+\chi(s)<u<u_+-\chi(s). \tag{T1}
$$

在其后的零曲率 coast 上无需再缩小角区间：

$$
X(s,u)=X_0(s,u)\quad\text{当 }L\le s\le S,
\quad u_-+\chi(L)<u<u_+-\chi(L). \tag{T2}
$$

假设 $X\in C^3$ 保证第二基本形式为 $C^1$，从而下面的 Codazzi 方程、系数微分、特征 ODE 与能量分部积分均为经典意义。证明真正使用的是这些具体正则性，**不声称只给 $C^2$ 就已足够**。同样，定理不越过下一段 $a''<0$ 的椭圆区；coast 终点以后没有在此得到有限传播结论。

## 2. Gauss–Codazzi 系统与一个必要的非线性项

取单位法向

$$
n=\frac{X_u\times X_s}{a},
$$

令

$$
\ell=\langle X_{ss},n\rangle,\quad
M=\langle X_{su},n\rangle,\quad
N=\langle X_{uu},n\rangle.
$$

Gauss 方程和两条 Codazzi 方程是

$$
\ell N-M^2=-aa'',\qquad
M_s=\ell_u-\frac{a'}aM,
\qquad
N_s=M_u+aa'\ell+\frac{a'}aN. \tag{8}
$$

初始法向为平面曲线的外法向，因此 $N(0,u)=-\kappa_\Gamma(u)$ 有统一负上界，且 $M(0,u)=0$ 在整个初始圆周成立。由连续性，在某个完整初始圆柱上 $|N|$ 具有正下界。后续只在 $N\ne0$ 的区域使用消元；第 6 节的延拓会保证局部相等区域中的这一条件。

记

$$
q=aa'',\quad
N_0=-a\sqrt{k^2-a'^2},\quad V=N-N_0.
$$

显式片满足 $M_0=0$。由 $\ell=(M^2-q)/N$ 可得**精确**差分系统

$$
\begin{aligned}
M_s={}&\frac{2M}{N}M_u+\frac{q}{N^2}V_u
-\left(\frac{a'}a+\frac{M N_u}{N^2}\right)M,\\
V_s={}&M_u+\frac{aa'M}{N}M
+\left(\frac{a'}a+\frac{a^2a'a''}{NN_0}\right)V.
\end{aligned} \tag{9}
$$

首式中的 $-M^2N_u/N^2$ 不能直接删去。式 (9) 将它作为一个系数有界的低阶乘积写入括号。这种重排对一个已给定的 $C^3$ 解是合法的；它不是把非线性方程换成另一个方程。

写 $Y=(M,V)^T$，则 $Y_s=A Y_u+B Y$，其中

$$
A=\begin{pmatrix}2M/N&q/N^2\\1&0\end{pmatrix},
\quad
B=\begin{pmatrix}
-a'/a-MN_u/N^2&0\\
aa'M/N&a'/a+a^2a'a''/(NN_0)
\end{pmatrix}. \tag{10}
$$

## 3. 整个初始圆周上的 $M=O(a')$

在完整初始圆柱上，$M,N,N_u$ 有界，$|N|$ 远离 0。把第一条方程沿速度 $-2M/N$ 的材料角特征积分，有

$$
\frac{dM}{ds}
=\frac{q}{N^2}N_u-
\left(\frac{a'}a+\frac{MN_u}{N^2}\right)M.
$$

特征在圆周上没有侧边界。初值 $M(0,\cdot)=0$，Gronwall 不等式给出统一界

$$
\sup_u|M(s,u)|\le C\int_0^s q(r)\,dr
\le C\max_{[0,s]}a\int_0^s a''(r)\,dr
\le C_1 a'(s). \tag{11}
$$

在初始单调段，$a''\ge0$ 且非减，所以

$$
0\le a'(s)=\int_0^s a''(r)\,dr\le s a''(s).
$$

因而

$$
\frac{a'(s)^2}{a''(s)}\le s^2a''(s)\longrightarrow0,
\qquad
\frac{M(s,u)}{\sqrt{q(s)}}\longrightarrow0
\quad\text{一致于 }u. \tag{12}
$$

## 4. 初始段的加权能量及无损入端极限

对 $s>0$ 令

$$
S=\operatorname{diag}\left(\frac{N^2}{q},1\right).
$$

则

$$
SA=\begin{pmatrix}2MN/q&1\\1&0\end{pmatrix}
$$

对称。在一个随时间缩小的角区间 $J_s$ 上考虑

$$
E(s)=\int_{J_s}Y^TSY\,du
=\int_{J_s}\left(\frac{N^2M^2}{q}+V^2\right)du. \tag{13}
$$

分部积分给出内部项

$$
\int_{J_s}Y^T\big[S_s-(SA)_u+SB+B^TS\big]Y\,du. \tag{14}
$$

在初始单调段，$q'=a'a''+aa'''\ge0$。因此

$$
(S_{11})_s=\frac{N^2}{q}\frac{2N_s}{N}
-\frac{N^2q'}{q^2}
\le C S_{11};
$$

奇异项 $-N^2q'/q^2$ 的符号有利，无需用 $|q'/q|$ 上界它。

另一方面，$(SA)_u$ 仅有 $(1,1)$ 元非零，而且

$$
\frac{((SA)_u)_{11}}{S_{11}}
=\frac{2M_u}{N}+\frac{2MN_u}{N^2},
$$

该比值有界。矩阵 $B$ 的对角元有界，其非对角项对能量的贡献为 $2B_{21}MV$。由

$$
2|MV|\le\frac1{\sqrt{S_{11}}}\,(S_{11}M^2+V^2)
$$

以及 $1/\sqrt{S_{11}}=\sqrt q/|N|$ 有界，得到一个**不依赖下端截断 $\epsilon$** 的常数 $C$，使内部项不超过 $CE(s)$。

## 5. 出流边界与入口唯一性

先固定任意闭区间 $J\Subset I$ 及任意 $\eta>0$。令

$$
J_s=\big[j_-+(1+\eta)\chi(s),\;
 j_+-(1+\eta)\chi(s)\big].
$$

只考虑此区间尚非空的时间。对式 (10) 使用的主矩阵 $A$，两个特征值为

$$
\lambda_\pm=\frac{M}{N}\pm\frac{\sqrt{M^2+q}}{|N|}.
$$

注意这与把 $-M^2N_u/N^2$ 保留在主部的原始拟线性矩阵的特征值写法不同；本能量计算必须使用上面这个 $A$ 的谱。

由于初始圆弧上 $N(0,u)=N_0(0)=-k$，由连续性及式 (12)，一致于 $u\in J$ 有

$$
\frac{\max(|\lambda_+|,|\lambda_-|)}{c_0(s)}
=\frac{|N_0|}{|N|}
\left(\frac{|M|}{\sqrt q}+\sqrt{1+\frac{M^2}{q}}\right)
\longrightarrow1. \tag{15}
$$

所以在一个足够短的初始区间上，两侧边界向内速度 $(1+\eta)c_0$ 严格大于所有谱速的绝对值。

具体地，上边界能量项为

$$
Y^TSA Y-(1+\eta)c_0Y^TSY\le0,
$$

下边界项为

$$
-Y^TSA Y-(1+\eta)c_0Y^TSY\le0.
$$

这是因为 $S^{1/2}AS^{-1/2}$ 为对称矩阵，其特征值即 $\lambda_\pm$。结合第 4 节，

$$
E'(s)\le CE(s)\qquad(0<s\le\tau).
$$

在 $s=\epsilon$ 处，式 (11)–(12) 及 $V\to0$ 在 $J$ 上的一致连续性给出

$$
E(\epsilon)
\le C\frac{a'(\epsilon)^2}{a''(\epsilon)}
+|J|\sup_{u\in J}|V(\epsilon,u)|^2\longrightarrow0.
$$

因此对固定 $0<s\le\tau$，

$$
0\le E(s)\le e^{C(s-\epsilon)}E(\epsilon)
\longrightarrow0.
$$

从而 $M=0,V=0$ 在此初始收缩区域内成立。入口退化在这里已经通过加权能量的入端极限处理，而不是直接引用一个要求统一严格双曲性的标准定理。

## 6. 严格双曲部分的继续、尖锐宽度与末端退化

继续使用固定 $J\Subset I$ 和固定 $\eta>0$。若相等性已保持至某个 $s_*>0$，且 $s_*<L$、$J_{s_*}$ 非空，那么在闭区间 $J_{s_*}$ 上

$$
M=0,\quad N=N_0\ne0,\quad
\max|\lambda_\pm|=c_0(s_*).
$$

由于 $c_0(s_*)>0$，边界速度有严格的 $\eta c_0(s_*)$ 余量。系数连续性保证其后一个短时间区间中 $N$ 仍远离 0，边界仍出流。在这个短区间，$q$ 有正下界，所以全部能量系数有通常的有限上界；从 $E(s_*)=0$ 再次得到 $E=0$。

这样相等性在每个固定的 $T<L$ 上通过开闭延拓成立。这里不要求 $q$ 在靠近 $L$ 时有统一正下界，也不要求把初始段的同一个常数 $C$ 使用到 $L$。对任意严格位于尖锐区间

$$
u_-+\chi(s)<u<u_+-\chi(s)
$$

的点，先选 $J\Subset I$ 足够大，再选 $\eta>0$ 足够小，即可包含该点。因此获得没有 $1+\eta$ 损耗的结论。最后由 $X,M,N$ 的连续性令 $s\uparrow L$，得到 $s=L$ 处所有严格内点的相等性。

## 7. 零曲率 coast 不再损耗角宽

在 $q=0$ 的 coast 上，式 (9) 的第一式是

$$
M_s-\frac{2M}{N}M_u
=-\left(\frac{a'}a+\frac{MN_u}{N^2}\right)M.
$$

在一个初始值 $M(L,u)=0$ 的内部材料点处，沿这个 $C^1$ 特征场的 ODE 唯一性给出 $M=0$；其角速度也因此为 0，故该特征就是固定的竖线 $u=\text{常数}$。这同时证明没有由侧边界进入该区间的非零值。

因为 $M$ 在所述开角区间内恒为 0，$M_u=0$。第二条方程化为

$$
N_s=\frac{a'}aN.
$$

此时 $a'$ 为常数，故

$$
N(s,u)=N(L,u)\frac{a(s)}{a(L)}
=-a(s)\sqrt{k^2-a'^2}=N_0(s).
$$

这一相等性保证 $N\ne0$，通过连续性可延续至整个 coast。无需再次缩小角区间。

## 8. 从第二基本形式相等恢复位置相等

在已经得到 $M=0,N=N_0$ 的区域，Gauss 方程给出 $\ell=\ell_0$。令

$$
e_1=X_s,\quad e_2=X_u/a.
$$

Gauss–Weingarten 方程沿每条固定 $u$ 的竖线为

$$
X_s=e_1,\quad
(e_1)_s=\ell n,\quad
(e_2)_s=(M/a)n,\quad
n_s=-\ell e_1-(M/a)e_2. \tag{16}
$$

实际浸入与显式片具有相同的系数 $\ell,M/a$，并在初始圆弧上具有相同的位置、两个单位切向和单位法向。线性框架 ODE 的唯一性给出 $X=X_0$。由于 $\chi$ 非减，任意终点处于收缩区间的竖线在之前的所有时间也位于相等区域内，所以这一步的积分路径没有越出已证明区域。

这完成 (T1)–(T2) 的证明。下半段若具有相应反射的初值，可用相同论证在反射坐标上处理；不能仅凭上半段的计算就无条件声称另一半满足这些初值。

## 9. 对当前候选的准确用途

精确圆弧 provider 的 $C^2$ 曲率半径产生足够正则的平面初始曲线；源 v17/v18 flat ramp 在最初小段有 $a''$ 非减，首次负曲率 ramp 后有一段 $a''=0$ 的 coast。因此**如果**某个实际完成的 true-prefix 解满足本定理的 $C^3$ 正则性、精确旋转度量和完整 Cauchy 数据，本定理可支付 R4 预算中“局部精确旋转片保持”的缺口。

仍未支付的项目包括：完整 prefix 解存在、非线性尾端闭合、同一固定参数／固定度量的真正加密或精确构造、全局 C2 拼接和 reach、以及 $\delta_E>0$。浮点 BVP、近似圆弧的 Fourier 投影或有限点的度量小残差均不满足本定理的精确前提。
