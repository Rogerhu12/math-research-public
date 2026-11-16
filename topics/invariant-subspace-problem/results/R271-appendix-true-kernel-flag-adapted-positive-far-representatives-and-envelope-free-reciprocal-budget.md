# R271 附录：真实核旗适配的正远孔代表与无费用包络的同源倒数门

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：以下代表、完整费用公式和同一原 $w$ 的必要倒数条件均已证明。** 本稿把实际首头返回源的第 $r+1$ 个正交核旗分量放到第 $r$ 个远孔层。各层使用整个原强头空间中的真正 MP 最小原像，未把低旗来源误当成低旗解。所得代表仍对应原同一个 $f_1=e_1\otimes\Omega$、全部 $h$ 段和真正帽来源。

新代表不需要先有统一范数包络：同 $Q$ 投影误差可在除以代表范数之后吸收。因此，任意这样的代表若能取得一个倒数不可和的实际费用上界，即可排除相应非零锚。**本稿尚未证明这个费用上界。**

内积对第一变量线性。

依据：

- [完整低旗来源与跨头核 Schur](R271-appendix-complete-low-flag-return-source-and-cross-head-schur-energy-summability.md)，§§3–4、7；
- [原物理尾的核参数自由度](R271-appendix-physical-tail-kernel-parameter-freedom-and-complete-two-hole-positive-pencil.md)，§§1–3；
- [移动头全高度 coherent Bessel](R271-appendix-cross-head-all-height-coherent-bessel-and-same-w-full-energy-summability.md)，§§1–4；
- [原顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)，§2；
- [matched 平均首反馈](R271-appendix-matched-full-resolvent-first-far-hole-and-native-mean-feedback.md) 中的完整 $U_n$、$H-B$ 配对和帽来源。最后一条只用于保持已付接口；下文的代表和必要条件不依赖任何未付的右费。

## 1. 原空间与真正旗分量

固定原 N/Y 头，取 $m\ge10$、$d=2^m$，以及原偶强段 $R\ge d$。记
$$
x=m+R,\qquad h=d+R,\qquad
C=A_m+D_{[m,x)},\qquad C^h=0,
$$
$$
D=D_{[x,\infty)},\qquad L=C+D,\qquad
b_i=(i+1)^{-2},\qquad
S=S_x=\sum_{i\ge x}b_i^2.
\tag{1.1}
$$
原强头是有限维物理空间。令
$$
\mathcal F_j=\ker C^j,\qquad
P_j=P_{\mathcal F_j},\qquad
K=\mathcal F_1,\qquad
E_j=P_j-P_{j-1}.
\tag{1.2}
$$
这里 $E_j$ 是正交核旗差，不是原逐位删除算子。

原偶强段结论给 $K\subset\operatorname{Ran}C$。在完整强头度量中定义
$$
G=(CC^*)^\dagger,\qquad
\Gamma=P_KG|_K,\qquad
Ce_1=e_0,\quad Ce_0=0,\quad \|e_0\|=\|e_1\|=1.
\tag{1.3}
$$
$\Gamma>0$ 于 $K$。所有以下 MP 都是有限维完整 MP；不先压到某个 $\mathcal F_j$。

对任意 $v\in K$，置
$$
\mathfrak h_v=C^\dagger v-C^*\Gamma v.
\tag{1.4}
$$
由 $C:\mathcal F_2\ominus K\to K$ 的真正逆为 $C^\dagger|_K$，
$$
P_{\mathcal F_2}C^*\Gamma v=C^\dagger v,
\qquad
\mathfrak h_v\perp\mathcal F_2.
\tag{1.5}
$$

原 $D_{[m,x)}$ 满足
$\operatorname{ad}_{D_{[m,x)}}^3(D_{[m,x)}^*)=0$；
$A_m^d=0$ 给
$\operatorname{ad}_{A_m}^{2d-1}(A_m^*)=0$。两部分及其交叉伴随对易，故
$$
\operatorname{ad}_C^{2d-1}(C^*)=0.
$$
因 $\Gamma v\in\ker C$，有
$C^kC^*\Gamma v=\operatorname{ad}_C^k(C^*)\Gamma v$。
又 $C^\dagger v\in\mathcal F_2$，所以准确有
$$
\boxed{\mathfrak h_v\in\mathcal F_{2d-1}\ominus\mathcal F_2.}
\tag{1.6}
$$
此处没有给原 $A_m$ 加上不存在的单降阶物理 grading。

写 $p=2d-2<h$。于是
$$
\mathfrak h_v=\sum_{r=2}^{p}E_{r+1}\mathfrak h_v.
\tag{1.7}
$$
由于
$E_{r+1}\mathfrak h_v\in(\ker C^r)^\perp
=\operatorname{Ran}(C^*)^r$，可以定义
$$
\boxed{
q_r(v)=\big((C^*)^r\big)^\dagger E_{r+1}\mathfrak h_v
\in\operatorname{Ran}C^r,\qquad
(C^*)^r q_r(v)=E_{r+1}\mathfrak h_v .
}
\tag{1.8}
$$
这既说明可解性，也钉住最小范数规范。虽然右端只在第 $r+1$ 旗，(1.8) 的解仍在整个原强头空间中取值。

## 2. 同一来源的完整正远孔代表

令
$$
\omega_j=(D^*)^j\Omega,\qquad
\sigma_j^2=\|\omega_j\|^2
=(j!)^2e_j\big((b_i^2)_{i\ge x}\big),\qquad \sigma_1^2=S.
\tag{2.1}
$$
每个有限 $j$ 的 $\omega_j$ 都属于真正物理 Hilbert 空间。
准确有 $D^*\omega_j=\omega_{j+1}$；不假设 $D\omega_{j+1}$ 与 $\omega_j$ 成比例。

置
$$
t_v=\frac{e_0-v}{S}-\Gamma v,\qquad
k(v)=(e_1-C^\dagger v)\otimes\Omega
-\frac{e_0-v}{S}\otimes\omega_1 .
\tag{2.2}
$$
逐层使用 $CC^\dagger v=v$、$C(e_0-v)=0$ 和
$D\omega_1=S\Omega$，得到 $Lk(v)=0$。并且
$$
\boxed{
f_1-\big(\mathfrak h_v\otimes\Omega+t_v\otimes\omega_1\big)
=k(v)+L^*(\Gamma v\otimes\Omega).
}
\tag{2.3}
$$
这是同一个 $v$ 的精确恒等式；不是将两个不同最小来源的上界相减。

对每个 $r=2,\ldots,p$，定义有限列
$$
\Psi_r(v)=\sum_{j=0}^{r-1}(-1)^j
 (C^*)^{r-1-j}q_r(v)\otimes\omega_j .
$$
因为 $C^*$ 与 $D^*$ 作用于独立因子，相邻项逐一抵消：
$$
\boxed{
L^*\Psi_r(v)
=E_{r+1}\mathfrak h_v\otimes\Omega
-(-1)^r q_r(v)\otimes\omega_r.
}
\tag{2.4}
$$
因此
$$
\begin{aligned}
F_{\rm fl}(v)
&=t_v\otimes\omega_1+
  \sum_{r=2}^{p}(-1)^r q_r(v)\otimes\omega_r,\\
\Psi_{\rm fl}(v)
&=\Gamma v\otimes\Omega+\sum_{r=2}^{p}\Psi_r(v)
\end{aligned}
\tag{2.5}
$$
满足
$$
\boxed{f_1-F_{\rm fl}(v)=k(v)+L^*\Psi_{\rm fl}(v).}
\tag{2.6}
$$

所有项均有限远孔。$k(v)$ 至多一远孔，
$\Psi_{\rm fl}(v)$ 至多 $p-1$ 远孔，
$F_{\rm fl}(v)$ 仅有第 $1,\ldots,p$ 远孔。
换回原 $m$ 后物理孔计数，三者的上界分别为 $R+1$、$R+p-1$、$R+p$。
原 $b\in\ell^1$，所以 $L,L^*$ 全空间有界；
(2.6) 没有形式无穷列或未说明的闭像假设。

## 3. 真正费用与同一强头正最小化

不同远孔层正交，故
$$
\boxed{
\kappa_{\rm fl}(v)^2:=\|F_{\rm fl}(v)\|^2
=\frac1S\|e_0-(I+S\Gamma)v\|^2
+\sum_{r=2}^{p}\sigma_r^2\|q_r(v)\|^2.
}
\tag{3.1}
$$
这是原物理范数。每个较高核旗使用它自己的 $\sigma_r^2$，而非把全部 $\mathfrak h_v$ 都压到二远孔。

(3.1) 亦给一个完整有限维正最小化。令 $Q_r:K\to\operatorname{Ran}C^r$ 为 (1.8) 的实际线性映射，定义
$$
X_{\rm fl}=\sum_{r=2}^{p}\sigma_r^2 Q_r^*Q_r,\qquad
A=I+S\Gamma,\qquad
T_{\rm fl}=A^{-1}X_{\rm fl}A^{-1}\succeq0 .
$$
以 $u=Av$ 改写 (3.1)，唯一极小者和极小值为
$$
\begin{aligned}
v_{\rm fl,opt}
 &=A^{-1}(I+S T_{\rm fl})^{-1}e_0,\\
\kappa_{\rm fl,opt}^2
 &=\frac1S\left[1-
 \left\langle e_0,(I+S T_{\rm fl})^{-1}e_0\right\rangle\right]
 \le \frac1S .
\end{aligned}
\tag{3.2}
$$
没有对 $T_{\rm fl}$ 求逆。这个上界本身仍可能随 $x$ 很大，不能作为最终费用预算。

特别，可以保此前固定的
$v_S=(I+S\Gamma)^{-1}e_0$；此时 $t_{v_S}=0$，
所有费用都在第 $2,\ldots,p$ 远孔。也可以使用 (3.2) 的完整极小者。
下节必要条件对任意预先选择的 $v_m\in K_m$ 都成立。

## 4. 原同 Q 投影、全部 h 段和帽来源

记原
$$
P_{\mathscr U_Q}=P_{V_Q}-P_{K_Q}.
$$
若 $Q\ge R+p$，则 $k(v)\in K_Q$；
$\Psi_{\rm fl}(v)$ 的原孔支撑至多 $Q-1$，由真正低行方程
$P_{V_Q}L^*\Psi_{\rm fl}(v)=0$。
于是 (2.6) 给
$$
\boxed{P_{\mathscr U_Q}F_{\rm fl}(v)
=P_{\mathscr U_Q}f_1.}
\tag{4.1}
$$
这不是依靠 $P_{\mathscr U_Q}$ 与 $C$、$C^*$ 或 MP 交换。

对强块来源的真实最小 left 列 $U_n$，若 $n\ge p$，
$k(v)$ 属于其完整零源核，而 $\Psi_{\rm fl}(v)$ 的远孔支撑至多 $n-1$。
因此同样准确有
$$
\boxed{U_n^*F_{\rm fl}(v)=U_n^*f_1.}
\tag{4.2}
$$
所以 matched 来源
$(L_n+H_n)^{-1}U_n^*f_1$ 完全不变，
主项 $(H_n-B_n)(r_w,s_f)$ 也保持同一 $r_w,s_f$。
这里 $L_n,H_n,B_n$ 是原来源度量；算子 $L=C+D$ 与 $L_n$ 不混用。

全部 right 仍有原 $h$ 段，不以 $p$ 替代它。
若进一步进入原真正帽逆伴随和外部投影，仍要求
$$
n+2h+R<Q.
\tag{4.3}
$$
其作用对象仍是完整
$P_{\widehat{\mathscr E}}K_{\rm amb}^{-*}\mathcal R s_f$；
(4.2) 只说这个实际 $s_f$ 相同，不把上述算子换成环境相似。

原 $\tau_{14}$ 序列满足
$$
e^{(25/2)d_m^3}\le x_m\le e^{13d_m^3},\qquad
h_m\le2x_m,\qquad Q_m=d_m^2h_m<e^{14d_m^3}.
\tag{4.4}
$$
故 $Q_m\ge R_m+p_m$，而
$Q_m/2\le n\le Q_m-R_m-2h_m-1$ 内所有整数 cut
同时满足 $n\ge p_m$ 和 (4.3)。所有来源均先选定，再用于这个整窗。

## 5. 无需范数包络的同一 w 倒数必要条件

固定原 $w\in W$，记 $W_0=\|w\|$、$\alpha=\langle w,f_1\rangle$。
沿 (4.4) 取任意 $v_m\in K_m$，写
$F_m=F_{{\rm fl},m}(v_m)$、$\kappa_m=\|F_m\|$。
原同窗物理投影定理给
$$
u_m=P_{\mathscr U_{Q_m}}w,\qquad
\|u_m-P_{\mathcal N_m\le Q_m}w\|
\le2\eta_m W_0,\qquad \eta_m=e^{-6d_m^4}.
\tag{5.1}
$$
$F_m,f_1$ 都支撑于原 $Q_m$ 以下，且 (4.1) 给
$\langle u_m,F_m-f_1\rangle=0$。又 $F_m$ 全在正远孔，与 $f_1$ 正交，故
$$
\boxed{
|\langle w,F_m\rangle-\alpha|
\le\varepsilon_m\sqrt{1+\kappa_m^2},
\qquad \varepsilon_m=2\eta_m W_0.
}
\tag{5.2}
$$

对真实归一 coherent 读出
$$
\beta_{m,r}
=\frac{D_{x_m}^{\,r}P_{N_{\ge x_m}=r}}{\sigma_{m,r}},
$$
已付全高度 Bessel 是
$$
\sum_m\sum_{r=1}^{h_m-1}\|\beta_{m,r}w\|^2
\le2W_0^2.
\tag{5.3}
$$
(2.5) 的系数行只有 $r\le p_m<h_m$，范数正是 $\kappa_m$。
因此当 $\kappa_m>0$，
$$
a_m:=\frac{|\langle w,F_m\rangle|}{\kappa_m},
\qquad
\sum_{\kappa_m>0}a_m^2\le2W_0^2.
\tag{5.4}
$$
这里各 $m$ 可以使用不同的整个强头列；(5.3) 已是算子行 Bessel，不是逐列弱收敛。

假设 $\alpha\ne0$。充分大 $m$ 时 $\varepsilon_m\le|\alpha|/2$。
此时 $\kappa_m=0$ 会由 (5.2) 推出
$|\alpha|\le\varepsilon_m$，不可能。
令 $x_m'=\kappa_m^{-1}$，由 (5.2)
$$
|\alpha|x_m'
\le a_m+\varepsilon_m\sqrt{1+(x_m')^2}
\le a_m+\varepsilon_m+\varepsilon_m x_m' .
$$
吸收最后一项得到
$$
x_m'\le\frac2{|\alpha|}(a_m+\varepsilon_m).
$$
所以
$$
\boxed{
\sum_{m\ge m_1}\kappa_m^{-2}
\le\frac8{|\alpha|^2}
 \left(2W_0^2+\sum_{m\ge m_1}\varepsilon_m^2\right)
<\infty.
}
\tag{5.5}
$$

证明从未要求 $\eta_m\kappa_m\to0$、
$\kappa_m\le S_m^{-1/2}$ 或任何其他事先费用包络。
因此即使使用未优化的 $v_S$ 以及完整 (1.8) 的最小列，(5.5) 仍成立。

一个准确的充分门是：若在某无限指标集 $\mathcal J$ 上证明
$$
\kappa_m^2\le c_m,\qquad
\sum_{m\in\mathcal J}\frac1{c_m}=\infty,
\tag{5.6}
$$
则 $\alpha=0$。例如若对全部充分大的 $m$ 有
$c_m=O(m\log(m+1))$，条件足够；不把这个例子套到任意稀疏子列。

## 6. 剩余的真实费用门

(1.8)、(3.1) 保留了全部高旗 nuisance。
虽然 $\mathfrak h_v$ 只在 $\mathcal F_{2d-1}$，没有把
$\big((C^*)^r\big)^\dagger$ 换成该低旗压缩的逆。
原已付低旗核 Schur 能量也不能直接成为 (3.1) 的上界。

本稿新增的可检验目标是同一实际来源的
$$
\frac1S\|e_0-(I+S\Gamma)v\|^2
+\sum_{r=2}^{2d-2}
 (r!)^2 e_r\big((b_i^2)_{i\ge x}\big)
 \left\|\big((C^*)^r\big)^\dagger E_{r+1}\mathfrak h_v\right\|^2 .
\tag{6.1}
$$
较高真实核旗由较高远孔权支付，且任何实际费用证明都可直接使用
(5.5)–(5.6)，无需另付代表范数包络。
仍须证明 (6.1) 在原 N/Y、连续尾和同一来源下的有效上界；
没有据本稿宣称 $N=M$ 或普通 ISP 已闭。
