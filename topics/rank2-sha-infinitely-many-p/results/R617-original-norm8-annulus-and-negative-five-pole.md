# R617 — 原 norm8 环带、同一 carry 差测试与负五极点行

日期：2026-11-14。**状态：已证明。**

本篇把 R613 的实际重叠支、独占支及其规范／native 测试差，
同时接到原 $R=(W-Y)/2$ 的完整偶深核。
没有再增加一个深轴。每个支的全部 $q$、$C/F$ 条件及两个
Mellin 单位指示都保留。

第一修正项可以完全计算：原两个 sigma 的 $R$ 一阶矩恰为
$6\Omega x^2y_\wp\sigma^8=-6\Omega\Theta f_1$。
所以该修正是同一个原来源的五变量简单极点行。
这条行的新真实矩形及原三 sigma 反射，准确消去未知负三矩，
返回原固定负五矩 $I_1$。两个实际 norm8 环带还可直接提取此
极点总行。最后的公式同时保原中央、两个完整 native 环带和
极点外域；没有把任何局部非零或固定系数单位移给原总中央。

## 1. 原来源、两个 norm8 轴及不变的真实 carry

保持 R590、R594、R611、R613 的全部规范：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times .
\tag{1}
$$
原射线、R594 固定坏集和 $p\ge71$ 不变。完整来源仍为
$$
\mu_0=\nu_{B_C}(C)\otimes\nu^\flat,\qquad
\nu^\flat=\frac1{42}
 (\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
  -\nu_{f_3}(Z)\otimes\nu_\Theta(Q))
 \otimes\nu_\sigma(r)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),
$$
$$
f_1=-xy_\wp\sigma^6,\quad f_3=-y_\wp\sigma^6,\quad
\Sigma=\sigma^2,\quad\Theta=x\sigma^2 .
\tag{2}
$$
$B_C$ 质量为一。写
$$
\alpha=1+3\omega,\quad\gamma_d=2+3\omega=-\bar\alpha,\qquad
R=\alpha c+d,\quad K=c+\gamma_d d .
\tag{3}
$$
这是 R539 的原两个 norm8 轴，行列式 $-8$，完整逆为
$$
c=(\bar\alpha R+K)/8,\qquad d=(R-\alpha K)/8,\qquad
N(R)=N(K)=8,\quad R\perp K .
\tag{4}
$$
置
$$
a_Z=(-2+\omega)/2,\quad a_Q=(4+3\omega)/2,\quad
a=-3\omega/8,\quad b_K=-(1+6\omega)/8,
$$
$$
\boxed{
V=a_ZZ+a_QQ+2\delta r+b_KK,\qquad
Y=V+aR,\qquad W=V+(a+2)R .
}
\tag{5}
$$
因此 $V\perp R$、$N(V)=263/8$。本篇不为 $V$ 另赋核心。

原三个 carry 行完全不含 $R$：
$$
F=\delta Z/6+(1-2\omega)Q/2+\omega^2r+K,
$$
$$
G=-\frac{32+31\omega}{6}Z+\frac{-14+\omega}{2}Q
 +(21-3\omega)r+(3-2\omega)K .
\tag{6}
$$
R613 的 $A,H,L$ 也与 $R$ 正交。故 $R$ 的物理缩放逐个保持
$C,F,G,A,H,L$，特别保持
$$
\Gamma_{+,n},\quad\Gamma_{-,n},\quad
\mathscr X_n=\{A,L\in p^n,H\ {\rm unit}\},\quad
\mathscr E_n=\Gamma_{+,n}\setminus\Gamma_{-,n},
$$
以及同一个 $q_{+,n}$ 的所有系数和条件。
这里 $q_{+,n}$ 始终指 R613(3) 的真实正支，不把六支平均在
含 $C$ 的域上逐点替换成它。

令
$$
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
             -1_{W\ {\rm unit}}\log\langle W\rangle\},\qquad
\mathcal T=\mu_0(\ell)=J'_S-6\delta J'_T .
\tag{7}
$$
仍各保 $Y,W$ 自己的单位指示。

## 2. 完整偶深核及任意原支的环带分解

R539 已在 entire $\mathcal S_8$ 上付清
$$
K_8=-B_8,\qquad B_8e_j=(-1)^je_{3j+4},\qquad K_8^2=I .
\tag{8}
$$
原 $B_C$ 投影只动前四 sigma，与 (3) 的两个原输入独立，
故 (8) 在 (2) 上保全部其余五坐标。
对 $m\ge0$，
$$
\boxed{\mu_0|_{\{R\in p^{2m}\}}
=\lambda^{2m}(P_{R,\kappa^{2m}})_*\mu_0 .}
\tag{9}
$$
此式也可附任意 $R$ 不变切集、任意 $R$ 不变连续权。
特别可同时附 $\mathscr X_n$、$\mathscr E_n$、$q_{+,n}$。
这只用整个 even-depth 返回，不给奇深第二态赋新的算术零。

记
$$
\mathscr A_m=\{R\notin p^{2m}\},\qquad
c_k=\frac{(-1)^{k+1}}{k}\{a^k-(a+2)^k\},\quad k\ge1 .
\tag{10}
$$
其中
$$
c_1=-2,\qquad c_2=2-3\omega/4 .
$$
对任何 $m\ge1$，在 (9) 的归一域中，
两个缩放观察均为单位当且仅当 $V$ 为单位。
于是是**整条测试恒等式**
$$
\boxed{
\ell\circ P_{R,\kappa^{2m}}
=d_p\,1_{V\ {\rm unit}}\sum_{k\ge1}
 c_k\kappa^{2mk}\frac{R^k}{V^k}.
}
\tag{11}
$$
若 $V$ 非单位，两项都为零。
若 $V$ 单位，两个 log 的共同 $\log\langle V\rangle$
准确相消，再用收敛的 $\log(1+t)$ 级数即得 (11)。
所以这里没有把旧 $Y/W$ 单位域免费换成 $V$ 单位域：
换域只发生在已经付清的真实 $R$ 深支。

若 $\mathscr D$ 和 $q$ 都在 $R$ 缩放下不变，完整分解为
$$
\boxed{
\begin{aligned}
\int_{\mathscr D}q\ell\,d\mu_0
={}&\int_{\mathscr D\cap\mathscr A_m}q\ell\,d\mu_0\\
&+d_p\lambda^{2m}\sum_{k\ge1}c_k\kappa^{2mk}
 \int_{\mathscr D\cap\{V\ {\rm unit}\}}
 q\,\frac{R^k}{V^k}\,d\mu_0 .
\end{aligned}}
\tag{12}
$$
实际 $q_{+,n}$ 在其支撑上整有界。对 $k\ge2$，
$2mk-v_p(k)\ge4m$；对 $k\ge3$，该下界为 $6m$。
因此 (12) 的全部高阶误差有直接一致赋值界，不依赖 $n$。

## 3. 第一 R 矩的完整五变量来源

原两个 sigma 的完整生成函数为
$$
F_0(s,t)=\sigma(\alpha s+t)\sigma(s+\gamma_dt)
       \in\mathcal S_8\otimes\mathcal S_8 .
\tag{13}
$$
用原 CM7 division 式
$$
\sigma(\gamma_dt)=\gamma_d\sigma(t)^7P(t),\qquad
P(t)=x(t)^3-r_7b,\qquad r_7=(-4-12\omega)/7 .
\tag{14}
$$
它与 R398/R426 的 $\gamma=3+\omega$ 公式相同，
因为 $\gamma_d=-\omega^2\gamma$，这是原固定 $\mu_6$ 单位。
$\alpha\gamma_d=-7$，故对 (13) 作实际一阶导数时
$$
\begin{aligned}
\partial_sF_0(0,t)
&=\alpha\sigma'(t)\sigma(\gamma_dt)
       +\sigma(t)\sigma'(\gamma_dt)\\
&=(\alpha\gamma_d+7)\sigma(t)^7\sigma'(t)P(t)
       +\sigma(t)^8P'(t)\\
&=\boxed{6\sigma(t)^8x(t)^2y_\wp(t)} .
\end{aligned}
\tag{15}
$$
所有 $\zeta$ 项以及 division 常数 $r_7$ 在第一式中严格消掉，
不是从形式导数删去它们。

令 $g_8=x^2y_\wp\sigma^8=-\Theta f_1$。
在原 Amice 规范中，完整第一 $R$ 矩
$$
\nu_1(\varphi):=\int R\,\varphi(C,Z,Q,r,K)\,d\mu_0
$$
准确为
$$
\boxed{
\nu_1=\frac{\Omega}{7}\nu_{B_C}\otimes
(\nu_{f_1}\otimes\nu_\Sigma-\nu_{f_3}\otimes\nu_\Theta)
\otimes\nu_\sigma\otimes\nu_{g_8}.
}
\tag{16}
$$
这是完整五变量身份，对任意实际 $C/F/G$ 条件和混合测试均成立。
如把 $g_8=-\Theta f_1$ 改写成卷积，测试仍作用于两输入的总和；
不额外删除它们的隐藏域。

还有完整二阶公式，可用于保下一项：
$$
\boxed{
\partial_s^2F_0(0,t)=\sigma(t)^8
 \{(2+6\omega)x(t)^4-(40+24\omega)b\,x(t)\}.
}
\tag{17}
$$
证明由
$P''=42x^4+24bx$ 和
$\gamma_d^2x(\gamma_dt)=7x-(\log P)''$
直接得到 $\sigma^8(P''-56xP)/\gamma_d$。
实际第二矩再乘 $\Omega^2$。
其他阶仍用真实 $\Omega^k\partial_s^kF_0(0,t)$，
不把其各自的 theta 分量删掉。

$g_8$ 是整个 $\mathcal S_8$ 的奇截面，且
$$
g_8(t)=-t+O(t^7),\qquad
\int K\,d\nu_{g_8}=-\Omega .
$$
(8) 在整个奇子空间上是 $-I$：
标准奇基 $e_j-e_{-j}$，$j=1,2,3$，逐列给 $B_8=+I$。
所以没有新的射线或未知标量，
$$
\boxed{\nu_{g_8}|_{p\mathbf Z_p}=\beta[\kappa]_*\nu_{g_8}.}
\tag{18}
$$
这不识别一条新 rank-two 曲线，也不赋它负矩非零。

## 4. 同一 cap/ex 的首修正及全部补项

定义实际第 $k$ 矩来源
$$
\nu_k(\varphi)=\int R^k\varphi(C,Z,Q,r,K)\,d\mu_0 .
$$
它们不是独立选来的辅助来源，全部由 (13) 同一完整联合给出。
对 R613 的 $\mathscr D=\mathscr X_n$ 或 $\mathscr E_n$，置
$$
\mathcal P_{n,k}^{\mathscr D}
=\nu_k\left(1_{\mathscr D}\,q_{+,n}
                  \frac{1_{V\ {\rm unit}}}{V^k}\right).
\tag{19}
$$
由于 $\mathscr D,q,V$ 都不含 $R$，(12) 给两个真实支各自的准确式
$$
\boxed{
Q_n^{\mathscr D}
=\int_{\mathscr D\cap\mathscr A_m}q_{+,n}\ell\,d\mu_0
+d_p\lambda^{2m}\sum_{k\ge1}c_k\kappa^{2mk}
 \mathcal P_{n,k}^{\mathscr D}.
}
\tag{20}
$$
尤其首项是
$$
Q_n^{\mathscr D}
=\int_{\mathscr D\cap\mathscr A_m}q_{+,n}\ell\,d\mu_0
-2d_p\lambda^{2m}\kappa^{2m}\mathcal P_{n,1}^{\mathscr D}
+p^{4m}\mathcal O .
\tag{21}
$$
$\mathcal P_{n,1}^{\mathscr D}$ 完全使用 (16)，仍保 $H$ 单位或
独占 carry 的全部条件。

只有把两个支完整相加后，才可使用原 $\pi_4$ 返回。
因为 $R,V$ 都在 $\langle Y,W\rangle$ 中，
$1_{V\ {\rm unit}}R^k/V^k$ 是合法的完整 $\pi_4$ 测试。
故令
$$
P_k=\mu_0\left(1_{V\ {\rm unit}}R^k/V^k\right),
$$
准确有
$$
\boxed{
\mathcal P_{n,k}^{\mathscr X_n}
+\mathcal P_{n,k}^{\mathscr E_n}=\beta^nP_k .
}
\tag{22}
$$
单个 cap 或 ex 没有这一删除 $q$ 的许可。
同样两个 native 环带之和恰为
$$
\int_{\Gamma_{+,n}\cap\mathscr A_m}q_{+,n}\ell\,d\mu_0
=\beta^n A_m,\qquad
A_m:=\int_{\mathscr A_m}\ell\,d\mu_0 .
\tag{23}
$$
因此 (20)–(23) 保整个原总行
$\beta^n\mathcal T=Q_n^\cap+Q_n^{\rm ex}$，
而不是只留下一个新子域。

## 5. R613 规范／native 差在同一环带上的实际首行

记 R613 的 $P_n=P_{A,\kappa^n}P_{L,\kappa^n}$，
$\mathscr R_H=(I-\lambda^2S_{H,\kappa^2})^{-1}$ 为该篇 (26)
已经证明的完整连续逆，包括其 $H=0$ 项。
对正偶数 $n$，在 $\mathscr X_n$ 上定义
$$
\begin{aligned}
\mathfrak D_n f={}&
 \beta^n\lambda^{-2n}(\mathscr R_Hf)\circ P_n^{-1}
 -q_{+,n}f\\
&+\beta^n1_{\mathscr X_{n+1}}\chi\lambda^{-2n-1}
 (\mathscr R_Hf)\circ P_{H,\kappa}P_{n+1}^{-1}.
\end{aligned}
\tag{24}
$$
逆幂只在各自真实深域中使用。
R613(36) 正是
$Q_n^{\rm ex}=\int_{\mathscr X_n}\mathfrak D_n\ell\,d\mu_0$。

所有 (24) 的缩放和条件都与 $P_R$ 交换。
且 $\ell|_{R=0}=0$，所以 $(\mathfrak D_n\ell)|_{R=0}=0$。
不存在可按总质量随意删掉的额外常数项。
置
$$
p_k=1_{V\ {\rm unit}}/V^k,\qquad
\Pi_{n,k}=\mathfrak D_np_k .
\tag{25}
$$
每个 $\Pi_{n,k}$ 完全不含 $R$。
将 (11) 逐项送过 (24)，得到**原差测试的完整恒等式**
$$
\boxed{
Q_n^{\rm ex}
=\int_{\mathscr X_n\cap\mathscr A_m}
             \mathfrak D_n\ell\,d\mu_0
+d_p\lambda^{2m}\sum_{k\ge1}c_k\kappa^{2mk}
 \nu_k(1_{\mathscr X_n}\Pi_{n,k}).
}
\tag{26}
$$
特别
$$
\boxed{
Q_n^{\rm ex}
=\int_{\mathscr X_n\cap\mathscr A_m}
             \mathfrak D_n\ell\,d\mu_0
-2d_p\lambda^{2m}\kappa^{2m}
 \nu_1(1_{\mathscr X_n}\Pi_{n,1})
+p^{4m}\mathcal O .
}
\tag{27}
$$
这里 $\nu_1$ 是显示的 (16)。
$\Pi_{n,1}$ 的原 $q$、$\lambda,\kappa$、
$A/L$ 归一、整个 $H$ 连续逆和所有原单位条件都由 (24)–(25)
明确决定。没有把规范测试当成 native 测试。

也可完全留在环带上：对这里的任意完整测试 $f$，
因为 $f|_{R=0}=0$，
$$
\mathscr R_Rf=\sum_{j\ge0}\lambda^{2j}
 f\circ P_{R,\kappa^{2j}}
$$
一致收敛，且
$$
\int_{\mathscr X_n}f\,d\mu_0
=\int_{\mathscr X_n\cap\mathscr A_1}\mathscr R_Rf\,d\mu_0 .
$$
对 $f=\mathfrak D_n\ell$，
$\mathscr R_Rf-f$ 的第一项准确为
$-2d_p\lambda^2\kappa^2
 R\Pi_{n,1}/(1-\lambda^2\kappa^2)$，余项在 $p^4\mathcal O$；
整条级数仍由 (26) 支付。
这只是同一原差测试的另一种完整写法。

## 6. 两个实际 native 环带提取第一极点总行

定义
$$
P=P_1=\nu_1(1_{V\ {\rm unit}}/V).
\tag{28}
$$
这是 (20)、(26) 中第一修正的完整总行。
由 (12) 的完整原来源式，
$$
\boxed{
\mathcal T-A_m
=d_p\lambda^{2m}\sum_{k\ge1}c_k\kappa^{2mk}P_k .
}
\tag{29}
$$
这条式子也可把 $A_m$ 换成 (23) 两个同一 $q$ 的 native 环带之和，
准确再乘 $\beta^{-n}$。
所以它不是为极点行另造没有原中央联系的测试。

令
$$
S_m=\lambda^{-2m}\kappa^{-2m}(\mathcal T-A_m).
$$
整个括号由 (29) 自动在 $p^{2m}\mathcal O$，
不能单独估计两项后删去其中一项。准确展开为
$$
S_m=-2d_pP+d_pc_2\kappa^{2m}P_2+p^{4m}\mathcal O .
\tag{30}
$$
相邻两环带的真正差消去第二矩：
$$
\boxed{
P_m^{\rm app}:=
-\frac{S_{m+1}-\kappa^2S_m}{2d_p(1-\kappa^2)}
=P+p^{4m+2}\mathcal O .
}
\tag{31}
$$
余项的更强 $4m+2$ 来自对 (29) 的整条级数逐项作差：
第 $k\ge3$ 项含
$\kappa^{2m(k-1)+2}(\kappa^{2k-4}-1)$；
$1-\kappa^2$ 是单位。
(31) 中原 $\mathcal T$ 和两个 native 环带都保留。

## 7. 同一极点来源上的真实矩形与原负五矩

现在只在 (16) 的完整矩来源中忘去质量一的 $C$。
记余下四变量来源为 $\bar\nu_1$。
定义新域
$$
\boxed{
\mathscr U_n=\{Z\ {\rm unit};\ Q,r,K\in p^n\},\qquad n\ge1 .
}
\tag{32}
$$
这是**本篇第一矩来源上的三深矩形**。
它不是 R594 的四深 $\mathscr R_n$，也不是原六 sigma 的
$\mathcal D_n$；那些域上的已知单位首项不移到 (32)。

$\Sigma,\Theta,\sigma,g_8$ 的所需完整核心分别都为 $\beta$，
最后一项由 (18) 自含支付。因此对整个 (32)
准确返回 $\beta^{3n}$，同时缩放 $Q,r,K$ 为 $\kappa^n$，
保 $Z$ 单位。
在此 $V$ 自动为单位，因为 $a_Z$ 为单位。

保持原两条负矩
$$
I_1=\int_{\mathbf Z_p^\times}Z^{-5}\,d\nu_{f_1},\qquad
I_3=\int_{\mathbf Z_p^\times}Z^{-3}\,d\nu_{f_3}.
\tag{33}
$$
$I_3$ 未被赋零。由
$\mu_2(\Sigma)=2\Omega^2$、
$\mu_0(\Theta)=1$、
$\mu_1(\sigma)=\Omega$、
$\mu_1(g_8)=-\Omega$，
实际倒数级数给
$$
\boxed{
\int_{\mathscr U_n}V^{-1}\,d\bar\nu_1
=\beta^{3n}
 \{e_3\Omega^3\kappa^{2n}I_3
       +e_5\Omega^5\kappa^{4n}I_1\}
 +p^{8n}\mathcal O ,
}
\tag{34}
$$
其中
$$
e_3=\frac{4\delta b_K}{7a_Z^3}
=\frac{-548-808\omega}{2401},\qquad
e_5=-\frac{48\delta b_Ka_Q^2}{7a_Z^5}
=\frac{-900624-433824\omega}{117649}.
\tag{35}
$$
具体地，负三分支只从 $rK$ 的两次项开始，
负五分支从 $Q^2rK$ 的四次项开始。
完整 $\mu_6$ 型使后续指数分别为 $2+6j$、$4+6j$。
倒数的几何级数没有 log 的 $1/k$ 分母，
所以剩余部分直接在 $p^{8n}\mathcal O$；
没有假设更高负矩消失。

## 8. 原反射在同一深度消去 I3，全部极点外域保留

R611 的 $\tau$ 固定 $R,K,r,C$，只在 $(Z,Q)$ 上作用。
因 $R$ 被保持，实际第一矩来源仍满足
$\tau_*\bar\nu_1=-\bar\nu_1$。
其作用在 $V$ 上是
$$
V_\tau=\bar a_ZZ+\bar a_QQ+2\delta r+b_KK .
$$
令
$$
c_\tau=(-323-360\omega)/343=(a_Z/\bar a_Z)^3 .
$$
原 $c_\tau$ 没有改变。
(34) 的两个对应系数为
$$
e_{3,\tau}=\frac{-332+488\omega}{2401}=c_\tau e_3,
\qquad
e_{5,\tau}=\frac{-862896-207456\omega}{117649}.
$$
于是
$$
\boxed{
\varepsilon_{\rm pole}:=e_{5,\tau}-c_\tau e_5
=\frac{-1255680-1105920\omega}{117649},
}
$$
$$
\boxed{
N(\varepsilon_{\rm pole})
=\frac{2^{16}3^4 5^2\,31}{7^9}.
}
\tag{36}
$$
当前 $p\equiv7\bmod64$ 排除 $31$，其他显示素数已在旧坏集中。
所以 (36) 对整个当前射线为单位，无新 CRT 条件。
这也是
$\varepsilon_{\rm pole}=(-6b_K/(2-12\delta))\varepsilon_\tau$
的原 R611 规范，不重选一个共轭周期。

在同一个 (32) 上，
$$
\boxed{
\int_{\mathscr U_n}(V_\tau^{-1}-c_\tau V^{-1})\,d\bar\nu_1
=\beta^{3n}\varepsilon_{\rm pole}\Omega^5\kappa^{4n}I_1
+p^{8n}\mathcal O .
}
\tag{37}
$$
为保全部真实补域，定义
$$
B_n^{\rm pole}:=
\int_{\mathscr U_n^c}
 \left\{\frac{1_{V_\tau\ {\rm unit}}}{V_\tau}
            -c_\tau\frac{1_{V\ {\rm unit}}}{V}\right\}\,d\bar\nu_1 .
\tag{38}
$$
这里外域的两个单位条件分别保留。
完整反射给总行 $-(1+c_\tau)P$，
故
$$
\boxed{
\frac{-(1+c_\tau)P-B_n^{\rm pole}}
 {\beta^{3n}\varepsilon_{\rm pole}\Omega^5\kappa^{4n}}
=I_1+p^{4n}\mathcal O .
}
\tag{39}
$$

将 (31) 取 $m=2n$ 代入，
得到只含原中央、原两个完整 native 环带及显示极点补域的式子：
$$
\boxed{
\frac{-(1+c_\tau)P_{2n}^{\rm app}-B_n^{\rm pole}}
 {\beta^{3n}\varepsilon_{\rm pole}\Omega^5\kappa^{4n}}
=I_1+p^{4n}\mathcal O .
}
\tag{40}
$$
$P_{2n}^{\rm app}$ 由 (30)–(31) 准确使用
$\mathcal T,A_{2n},A_{2n+1}$；
每个 $A$ 又可用 (23) 写成同一个原 $q$ 的 cap/ex 全部环带。
它们的真实 $R$ 切集分别是
$R\notin p^{4n}$、$R\notin p^{4n+2}$。
所有 $\lambda,\kappa,\beta$ 归一幂在显示公式中保留。

## 9. 准确范围与接续

(26)–(27) 已把 R613 的实际规范／native 测试差，
而非另一个任意测试，送入同一 norm8 环带与明确五变量首矩。
(34)–(40) 则把这个真实首修正接回原固定负五矩。
整个证明没有假定 $I_1$ 或 $I_3$ 为零、单位或非零。

若原 $J'_S=J'_T=0$，只允许在 (29)–(31) 中令
$\mathcal T=0$。两个 native 环带和 $B_n^{\rm pole}$ 仍完整存在。
若再有 $I_1=0$，(40) 仅迫其完整分子在 $p^{8n}\mathcal O$；
本篇没有证明该高阶补偿不可能。
固定的 $\varepsilon_{\rm pole}$ 是单位，不能据此把依赖 $p$ 的
原负矩当成固定 CM 多项式来应用密度引理。

R594 原非零管仍位于 R613 的独占支。
(20)、(26)、(40) 没有把该子管的赋值移给全部独占支、cap、
新矩形 (32) 或总中央。主目标仍待这些真实全补偿的进一步比较。

## 精确文件与依赖

- [check-r617-original-norm8-annulus-and-negative-five-pole.js](../scripts/check-r617-original-norm8-annulus-and-negative-five-pole.js)
- [check-r617-original-norm8-annulus-and-negative-five-pole.json](../scripts/check-r617-original-norm8-annulus-and-negative-five-pole.json)
- [R539：原 norm8 entire 核及完整两态](R539-original-degree8-mixed-st-core-and-amplified-central-domain.md)
- [R594：同一完整 q 与九乘二十整右逆](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)
- [R611：实际三 sigma 反射、原负五规范](R611-original-three-sigma-reflection-and-same-depth-negative-five.md)
- [R613：两个真实 carry 的交域及完整差测试](R613-original-reflected-carry-intersection-and-complete-two-state-return.md)
- [R426：原 CM7 division 规范](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)

BigInt 证书核定完整六坐标、两个 norm8 轴和全部旧 $C/F/G/Y/W$
行，整个奇 $\mathcal S_8$ 核、第一及第二条件矩的代数系数、
负三／负五和反射后的四个实际系数、固定单位范数及原 R611
尺度关系。无限深度、完整连续测试和全部补域的等式由正文支付；
未重算原 R594 右逆或以数值采样代替来源身份。
