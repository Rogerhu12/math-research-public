# R271 附录：同一实际右逆伴随的临界物理来源域与精确值域

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 状态：下面的真实伴随域、临界主指数预算及实际值域身份已证明；真实 $W$ 自动满足此来源条件尚未证明。

本稿始终使用原 $T_N$ 或原完整 $T_Y$。
固定一次[全尺度实际右逆](R271-appendix-single-actual-right-inverse-on-all-physical-exponential-scales.md)的构造：
$\lambda_*>\kappa_0=2+2\log(3/2)$，相应整数 $Q\ge64$，
以及原 $R_q,R,E,U,\mathcal G=\mathcal G_{\lambda_*}$。
不随新的输出指数重新选择右逆。
沿用[平滑修正及真实有限孔行](R271-appendix-same-right-inverse-smoothing-correction-and-actual-kernel-cut-flux.md)
的 $C=\mathcal G E$，于是 $\mathcal G=R-C$。

这里 $\mathcal G^*$ 是稠密定义 Hilbert 算子 $\mathcal G$ 的真实伴随，
也等于其图闭包的伴随。
它不是原形式除法算子 $G_0^*$，不能混用这两个符号。

## 1. 临界主指数的完整来源域

物理孔层为 $\mathsf P_p$，并记
$$
X_\kappa=\left\{\xi:
\|\xi\|_\kappa=\sum_{p\ge0}e^{\kappa p}\|\mathsf P_p\xi\|<\infty\right\}.
$$
定义同一个固定 $Q$ 上的实际来源空间
$$
\mathcal Z_{\kappa,Q}=
\left\{\xi:
\|\xi\|_{\mathcal Z_{\kappa,Q}}:=
\sum_{p\ge0}
\exp\left((\kappa+\kappa_0)p+
 (36+\kappa)\sqrt{p+Q}\log(p+Q)\right)
\|\mathsf P_p\xi\|<\infty
\right\}.
\tag{1.1}
$$

**定理 1。** 对每个 $\kappa\ge0$，上述同一个实际伴随满足
$$
\boxed{
\mathcal Z_{\kappa,Q}\subset D(R^*)=D(\mathcal G^*),\qquad
\|R^*\xi\|_\kappa\le\|\xi\|_{\mathcal Z_{\kappa,Q}}.
}
\tag{1.2}
$$
还有有限常数 $K_{\lambda_*,\kappa}$，使
$$
\boxed{
\|\mathcal G^*\xi\|_\kappa
\le\|\xi\|_{\mathcal Z_{\kappa,Q}}
 +K_{\lambda_*,\kappa}\|\xi\|.
}
\tag{1.3}
$$
域等号在 (1.2) 中来自减去同一个全 $H$ 有界的 $C$，
不是声称这些域本身等于 $\mathcal Z_{\kappa,Q}$。

因此，对于每个 $\rho>\kappa_0$，同一个 $\mathcal G^*$ 连续作用为
$$
\boxed{
\mathcal G^*:X_{\kappa+\rho}\longrightarrow X_\kappa
\qquad(\kappa\ge0).
}
\tag{1.4}
$$
新的 $\rho$ 可以小于原构造使用的 $\lambda_*$；
此处始终是原同一个 Hilbert 伴随，没有另选形式逆。

(1.1) 保留主指数恰为 $\kappa_0$，
另付显示的次线性费用。
它比仅给所有严格大于 $\kappa_0$ 的指数来源更宽，
但不声称 $X_{\kappa+\kappa_0}$ 本身已经入域。

## 2. 两侧原孔壳给出完整伴随列和

令
$$
x=q+Q,\qquad m(q)=\left\lceil\tfrac12\log_2 x\right\rceil,
\qquad d(q)=2^{m(q)}.
$$
旧实际构造在放宽为固定指数之前已经给出
$$
\log\|R_q\|\le\kappa_0q+20\sqrt{x}\log x,
\tag{2.1}
$$
以及双侧真实支撑
$$
R_qH_q\subset
H_{[\max(0,q-m(q)+1),\,q+d(q)+m(q)]}.
\tag{2.2}
$$
(2.1)--(2.2) 包含全部实际头 carry，$Y$ 型也保完整 Cayley 逆。

固定输入孔数 $p$，只有满足
$$
p\ge q-m(q)+1
\tag{2.3}
$$
的 $q$ 才可能贡献 $R_q^*\mathsf P_p$。
旧有限孔行的同一估计给
$$
q\le\max(Q,2p).
\tag{2.4}
$$
直接核验：若 $q\ge Q$，则
$m(q)\le1+\tfrac12\log_2(2q)\le q/2$；
结合 (2.3) 即得 $q<2p$。较小 $q$ 由 $Q$ 覆盖。

置 $y=p+Q\ge64$。从 (2.3)--(2.4) 得
$$
q+Q\le2y,\qquad
q-p\le m(q)-1\le\frac{\log(2y)}{2\log2},
$$
而所有可能的非负整数 $q$ 至多 $2y$ 个。
因此
$$
\begin{aligned}
\sum_{q:\,(2.3)}e^{\kappa q}\|R_q\|
\le {}&
2y\exp\left((\kappa+\kappa_0)p
+\frac{\kappa+\kappa_0}{2\log2}\log(2y)\right.\\
&\left.\hspace{32mm}+20\sqrt{2y}\log(2y)\right).
\end{aligned}
\tag{2.5}
$$
这是对同一个实际输出壳的完整求和，没有把每行的界当作整算子界。

对 $y\ge64$，使用
$\log(2y)\le(7/6)\log y$、$\sqrt2<3/2$、
$\log2>2/3$ 及 $\kappa_0<3$，有
$$
20\sqrt{2y}\log(2y)\le35\sqrt y\log y,
$$
$$
\log(2y)+\frac{\kappa+\kappa_0}{2\log2}\log(2y)
\le\left(\frac{91}{24}+\frac{7\kappa}{8}\right)\log y
<(1+\kappa)\sqrt y\log y.
$$
所以 (2.5) 不超过
$$
\exp\left((\kappa+\kappa_0)p+
 (36+\kappa)\sqrt{p+Q}\log(p+Q)\right).
\tag{2.6}
$$

先对有限孔输入求和，由 (2.2)、三角不等式和 (2.6) 得
$$
\sum_qe^{\kappa q}\|R_q^*\xi\|
\le\sum_p\|\mathsf P_p\xi\|
       \sum_{q:\,(2.3)}e^{\kappa q}\|R_q\|
\le\|\xi\|_{\mathcal Z_{\kappa,Q}}.
\tag{2.7}
$$
对一般 $\xi\in\mathcal Z_{\kappa,Q}$，右端保证整个列和在 $X_\kappa$ 中绝对收敛。
对每个有限孔测试 $v$，它与 $Rv$ 的 Hilbert 配对恰相等；
再以原 $X_{\lambda_*}$ 的孔截断同时逼近 $v$ 和 $Rv$，
可把配对延至 $\mathcal G,R$ 的整个原定义域。
因此该列和是实际 $R^*\xi$，不是只有有限坐标成立的转置。
这证明 (1.2) 的包含和范数界。
$p=0,q=0$ 始终包含在 (2.3)--(2.7) 中，没有另丢真空行。

## 3. 同一平滑修正与全部指数尺度

旧稿给某个有限 $A_{\lambda_*,0}$：
$$
\|\mathsf P_qC^*\xi\|
\le A_{\lambda_*,0}e^{-28(q+Q)^2}\|\xi\|.
$$
由 $\kappa q\le14q^2+\kappa^2/56$，
$$
\boxed{
\|C^*\xi\|_\kappa
\le
\frac{A_{\lambda_*,0}
 \exp(-28Q^2+\kappa^2/56)}
 {1-e^{-56Q}}\|\xi\|.
}
\tag{3.1}
$$
故可把右端系数取为 (1.3) 的 $K_{\lambda_*,\kappa}$。
在 $\kappa=0$ 仅需普通输出范数时，也可直接使用
$\|C^*\|=\|C\|$。

因为 $\mathcal G=R-C$ 且 $C\in B(H)$，
稠密定义算子的伴随确切满足
$$
D(\mathcal G^*)=D(R^*),\qquad
\mathcal G^*=R^*-C^*.
\tag{3.2}
$$
这证明 (1.3)。

若 $\rho>\kappa_0$，有限常数
$$
L_{\rho,\kappa,Q}
=\sup_{p\ge0}
\exp\left(-(\rho-\kappa_0)p+
 (36+\kappa)\sqrt{p+Q}\log(p+Q)\right)
<\infty
$$
给
$$
\|\xi\|_{\mathcal Z_{\kappa,Q}}
\le L_{\rho,\kappa,Q}\|\xi\|_{\kappa+\rho}.
$$
合 (1.3) 得 (1.4)。特别
$$
\mathcal G^*:\mathscr E_\infty\longrightarrow\mathscr E_\infty
$$
连续，其中 $\mathscr E_\infty=\bigcap_{\kappa\ge0}X_\kappa$。

为了明确临界域确为更宽的输入，可在每个 $H_p$ 取一个单位向量，
使其系数为
$$
\exp\left(-(\kappa+\kappa_0)p-
 (37+\kappa)\sqrt{p+Q}\log(p+Q)\right).
$$
所得向量属于 $\mathcal Z_{\kappa,Q}$，
却不属于任何 $X_{\kappa+\rho}$、$\rho>\kappa_0$。
这里只证明来源域的严格扩张，不声称这个例子属于真实 $N^\perp$ 或 $W$。

## 4. 真实 N 垂直来源的精确 Hilbert 值域

记
$$
M=\ker T,\qquad N=\overline{BM},\qquad
I=M^\perp=\overline{\operatorname{Ran}T^*}.
$$
**定理 2。** 同一个固定右逆的实际伴随有
$$
\boxed{
D(\mathcal G^*)\cap N^\perp=\operatorname{Ran}T^*,
\qquad
T^*\mathcal G^*w=w
\quad(w\in D(\mathcal G^*)\cap N^\perp).
}
\tag{4.1}
$$
而且
$$
\boxed{
T^*H\subset D(\mathcal G^*),\qquad
\mathcal G^*T^*v=v\quad(v\in H).
}
\tag{4.2}
$$
这些是实际值域等式，不能把 (4.1) 的右侧改为其闭包 $I$。

证明 (4.2)，对每个 $f\in X_{\lambda_*}$ 使用原准确恒等式
$T\mathcal Gf=f$。因此
$$
\langle T^*v,\mathcal Gf\rangle=\langle v,f\rangle,
$$
给出真实 Hilbert 伴随域及 (4.2)。
特别 $T^*$ 单射，且 $T^*H\subset I\subset N^\perp$。

反过来，取 $w\in N^\perp\cap D(\mathcal G^*)$。
旧同一右逆稿 §6 已在有限整数支撑 $f$ 上证明
$$
\langle w,\mathcal Gf\rangle
=\langle h(w),f\rangle,
$$
其中 $h(w)$ 是原唯一规范形式解 $T^*h(w)=w$。
同一证明使用 $\mathcal Gf-Jf\in M\cap\mathscr E_\infty\subset N$，
没有任意更换来源。
由当前的真实伴随域，$h(w)$ 的所有坐标准确等于 $\mathcal G^*w\in H$。
原 $T^*$ 有界，故其形式方程即为实际 Hilbert 等式
$T^*\mathcal G^*w=w$。这证明 (4.1)。

定理 1 因而给新的可支付来源：
$$
\boxed{
w\in N^\perp\cap\mathcal Z_{\kappa,Q}
\ \Longrightarrow\
h(w)=\mathcal G^*w\in X_\kappa,\qquad T^*h(w)=w .
}
\tag{4.3}
$$
例如
$$
\|h(w)\|
\le(1+\|C\|)\|w\|_{\mathcal Z_{0,Q}}.
\tag{4.4}
$$
同一个 $w$ 和原 N/Y 算子均未替换。
若已知 $w=T^*v$，(4.2)--(4.3) 还说明：
$w\in\mathcal Z_{\kappa,Q}$ 会迫这个唯一实际 $v$ 属于 $X_\kappa$，
并支付同一范数界。

## 5. 光滑像的准确同一性与不能免费取得的密度

原 $T^*$ 保每个 $X_\kappa$。这里补齐所需实际理由：
固定任一低头 $m_0$，
$$
T^*=(T^{[m_0]})^*+\sum_{L\ge m_0}K_L^* .
$$
有限头项只改变有限个物理孔，
纯尾创建准确加一个孔。
每个 $K_L^*$ 仅作用于前 $L+1$ 位，故在 $X_\kappa$ 上的范数至多
$$
\sqrt{2L+3}\,e^{\kappa(L+1)}\|K_L\|.
$$
原完整 carry 界
$\|K_L\|\le52e^{-770\,16^{L-1}}$
使全部局部壳绝对求和。它同时保 $Y$ 型完整逆。
于是 $T^*\mathscr E_\infty\subset\mathscr E_\infty$。

由 (1.4)、(4.1) 得准确同一性
$$
\boxed{
T^*\mathscr E_\infty
=N^\perp\cap\mathscr E_\infty
=I\cap\mathscr E_\infty .
}
\tag{5.1}
$$
$T^*$ 在 $\mathscr E_\infty$ 与这个闭 Fréchet 子空间之间是线性拓扑同构，
逆为同一个 $\mathcal G^*$。
因为 $\mathscr E_\infty$ 在 $H$ 稠密且 $T^*$ 有界，
$$
\boxed{
\overline{N^\perp\cap\mathscr E_\infty}
=\overline{D(\mathcal G^*)\cap N^\perp}
=I.
}
\tag{5.2}
$$
所有闭包在原 Hilbert 范数中取。

所以即使 $D(\mathcal G^*)$ 自身在 $H$ 稠密，
也不能据此把其与 $N^\perp$ 的交宣布在 $N^\perp$ 稠密。
式 (5.2) 已准确识别这个交的闭包；若存在非零
$W=M\ominus N$，它恰处在尚未填补的正交方向。
特别
$$
W\cap D(\mathcal G^*)=\{0\},\qquad
W\cap\mathcal Z_{0,Q}=\{0\}.
$$
本文没有证明真实 $W$ 自动进入这些域，
没有给原 $RT P_{\le n}w$ 的有界子列，
也没有以这个实际来源准则代替 $N=M$ 或普通 ISP。
