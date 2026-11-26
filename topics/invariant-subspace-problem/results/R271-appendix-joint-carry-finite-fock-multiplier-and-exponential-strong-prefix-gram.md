# R271 附录：联合 carry 的有限 Fock 乘子与指数强前缀完整 Gram

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下相对 Gram、同源列与同一真子空间上的残余配对界已证明。**
本稿使用原 c26 联合 carry 预算，把原强头
$C=A_m+D_{[m,x)}$ 与同一完整物理坐标上的真实头 $A_x$
作相对比较。有限 Fock 截断中的准确乘子使费用只依赖
$\sqrt{J/s}$，不出现此前绝对扰动界的 $e^{M^2/s}$。
原允许的高度与 $x\le e^{13d^3}$ 都落入新范围；甚至整个
$C$ 塔的有限高度 $J\le d+x-m-1$，也可在明确的
$x+1\le e^{26d^3}/4$ 范围内比较。

每次压缩均保同一个完整子空间 $F$。特别可保全部已经指定的
真交旗，不能用本稿把 $F$ 改成另一个算子的自然核。
本稿没有得到 $\gamma<1/16$ 的物理孔加权
$\mathcal Z_\gamma$，也没有把末尾的能量对偶残余界改成无权残余界。

依赖：

- [原联合 carry 与 c26 窗口](../notes/2026-11-14-joint-positive-carry-budget-and-twenty-six-window-actual-sources-789f-next.md)，尤其 (5.1)、(5.4)；
- [原强头与真实大头的完整 Gram 比较](R271-appendix-actual-strong-head-gram-comparison-and-true-far-variance-source-limit.md)，尤其其准确压缩 (1.5) 与原远尾方差 (3.1)。

## 1. 原完整误差及同一有限物理头

取原 N 或 Y 模型，$m\ge10$、$d=2^m$，令
$$
 L_m=A_m+D_m,\qquad \mathcal E=L_m-T,\qquad
 \mathscr R_m=\exp\!\left(\frac{417}{8}d^3\right).
$$
已有完整联合预算为
$$
 \mathcal J_m(\mathscr R_m)
 :=\mathscr R_m\sum_{\substack{j,k<d\\a\ge0}}
 \frac{\mathscr R_m^{j+k+a}}{(j+1)!k!a!}
 \|A_m^j(\operatorname{ad}_{D_m}^{a}\mathcal E)A_m^k\|
 \le2e^{-15d^4/8}.
 \tag{1.1}
$$
这已经保留全部实际 carry；以下不再独立估计两个头幂。

取整数 $x\ge m$，$R=x-m$。在原前 $x$ 位的完整物理空间上记
$$
 D_< =D_{[m,x)},\quad C=A_m+D_<,\quad A=A_x,\quad E=C-A.
 \tag{1.2}
$$
前 $x$ 位真空嵌入的像同时被 $A_m,D_m,L_m,T,\mathcal E$
保持。因此限制与乘积、交换子相容，准确有
$$
 E=\mathcal E|_{\mathcal H_{<x}},\qquad
 A_m^j(\operatorname{ad}_{D_<}^{a}E)A_m^k
 =\left.A_m^j(\operatorname{ad}_{D_m}^{a}\mathcal E)A_m^k
 \right|_{\mathcal H_{<x}}.
 \tag{1.3}
$$
这里 $\mathcal H_{<x}$ 是全部 $2^x$ 维头，强位没有删状态。

对 $0\le b\le\mathscr R_m$ 定义
$$
 \Lambda_x(b)=
 \sum_{\substack{j,k<d\\a\ge0}}
 \frac{b^{j+k+a+1}}{(j+1)!k!a!}
 \|A_m^j(\operatorname{ad}_{D_<}^{a}E)A_m^k\|.
 \tag{1.4}
$$
所有项非负，故由 (1.1)--(1.3)
$$
 \boxed{\Lambda_x(b)
 \le\frac b{\mathscr R_m}\mathcal J_m(\mathscr R_m)
 \le2\frac b{\mathscr R_m}e^{-15d^4/8}.}
 \tag{1.5}
$$
$b=0$ 时按零理解。对正 $b$，式 (1.5) 同时支付后面使用的绝对收敛。

## 2. 准确指数乘子及一个保联合 factorial 的积分

定义整个矩阵函数
$$
 U(z)=e^{zA}e^{-zC},\qquad
 V(z)=U(z)^{-1}=e^{zC}e^{-zA},\qquad
 B(z)=e^{zC}Ee^{-zC}.
 \tag{2.1}
$$
因 $A=C-E$，逐项微分给
$$
 U'(z)=-U(z)B(z),\qquad V'(z)=B(z)V(z),\qquad U(0)=V(0)=I.
 \tag{2.2}
$$
$A_m^d=0$ 且 $[A_m,D_<]=0$。于是
$$
 B(z)=\sum_{j,k<d}\sum_{a\ge0}
 \frac{(-1)^kz^{j+k+a}}{j!k!a!}
 A_m^j(\operatorname{ad}_{D_<}^{a}E)A_m^k.
 \tag{2.3}
$$
若 $B(z)=\sum_{\ell\ge0}B_\ell z^\ell$，则
$$
 \begin{aligned}
 \sum_{\ell\ge0}\frac{b^{\ell+1}}{\ell+1}\|B_\ell\|
 &\le\sum_{j,k<d,a\ge0}
 \frac{b^{j+k+a+1}}{(j+k+a+1)j!k!a!}
 \|A_m^j(\operatorname{ad}_{D_<}^{a}E)A_m^k\|\\
 &\le\Lambda_x(b).
 \end{aligned}
 \tag{2.4}
$$
最后一步恰用
$(j+1)/(j+k+a+1)\le1$。所以不必把 $(j+1)!$
改成 $j!$ 再付额外 $d$，也不必分别估计 $e^{zC}$ 的范数。

## 3. 有限 Fock 中的非交换乘子估计

固定 $J\ge1$、$s>0$。在正交基 $e_0,\ldots,e_J$ 上令
$$
 Z_Je_k=\sqrt{k+1}\,e_{k+1}\quad(k<J),\qquad Z_Je_J=0.
$$
则 $Z_J^{J+1}=0$、$\|Z_J\|=\sqrt J$。设
$$
 N=Z_J/\sqrt s,\qquad b=\|N\|=\sqrt{J/s}.
 \tag{3.1}
$$
对任何矩阵系数解析芽 $W(z)=\sum W_\ell z^\ell$，定义
$$
 \mathcal M_W=\sum_{\ell=0}^{J}W_\ell\otimes N^\ell.
 \tag{3.2}
$$
头系数与辅助因子 $N$ 交换，故 (3.2) 保乘法；头系数彼此不需要交换。
特别 $\mathcal M_U\mathcal M_V=\mathcal M_V\mathcal M_U=I$。

为直接估计它们，令
$$
 \mathcal U(t)=\sum_{\ell=0}^{J}U_\ell\otimes(tN)^\ell,
 \qquad
 \mathcal V(t)=\sum_{\ell=0}^{J}V_\ell\otimes(tN)^\ell,
 \quad0\le t\le1.
$$
把 (2.2) 送入同一个有限商代数，准确得到
$$
 \mathcal U'=-\mathcal U\mathcal B(t),\qquad
 \mathcal V'=\mathcal B(t)\mathcal V,
 \quad
 \mathcal B(t)=\sum_{\ell=0}^{J-1}B_\ell\otimes t^\ell N^{\ell+1}.
 \tag{3.3}
$$
有限截断不会留下边界项，因为所有次数 $>J$ 的 $N$ 幂为零。
由 (2.4)
$$
 \int_0^1\|\mathcal B(t)\|\,dt
 \le\sum_{\ell=0}^{J-1}\frac{b^{\ell+1}}{\ell+1}\|B_\ell\|
 \le\Lambda_x(b).
 \tag{3.4}
$$
记 $\Lambda=\Lambda_x(b)$，Gronwall 以及对 (3.3) 的积分给
$$
 \boxed{
 \|\mathcal M_U\|,\ \|\mathcal M_U^{-1}\|\le e^\Lambda,
 \qquad
 \|\mathcal M_U-I\|,\ \|\mathcal M_U^{-1}-I\|
 \le e^\Lambda-1.
 }
 \tag{3.5}
$$
这在 $b\le\mathscr R_m$ 时成立，端点也合法；没有使用小于一的 Cauchy 比率。
$J=0$ 时直接取 $N=0$、$\Lambda=0$，所有式子仍成立。

## 4. 同一个完整 Gram 的相对比较

对 $X=A,C$ 定义完整有限列及其 Gram
$$
 \mathcal R_{X,J}(s)v
 =\sum_{j=0}^{J}\frac{X^jv}{\sqrt{j!s^j}}\otimes e_j,
 \qquad
 H_{X,J}(s)=\mathcal R_{X,J}(s)^*\mathcal R_{X,J}(s)
 =\sum_{j=0}^{J}\frac{(X^*)^jX^j}{j!s^j}.
 \tag{4.1}
$$
辅助符号若原塔使用 $(-X)^j$，只需把 $N$ 换成 $-N$，所有范数和 Gram 不变。

从 $e^{zA}=U(z)e^{zC}$ 逐系数比较，可得
$$
 \boxed{\mathcal R_{A,J}(s)=\mathcal M_U\mathcal R_{C,J}(s).}
 \tag{4.2}
$$
其中 $N^\ell e_{j-\ell}=s^{-\ell/2}
\sqrt{j!/(j-\ell)!}\,e_j$，故 (4.2) 的全部 factorial 准确。
由 (3.5)
$$
 \boxed{
 e^{-2\Lambda}H_{C,J}(s)\preceq H_{A,J}(s)
 \preceq e^{2\Lambda}H_{C,J}(s),
 }
 \tag{4.3}
$$
$$
 \boxed{
 e^{-2\Lambda}H_{C,J}(s)^{-1}\preceq H_{A,J}(s)^{-1}
 \preceq e^{2\Lambda}H_{C,J}(s)^{-1}.
 }
 \tag{4.4}
$$
两边 $H\succeq I$，所有 inverse 都是完整空间中的有界正 inverse。

更一般地，令 $F$ 为同一物理头中任意指定的闭子空间，包含某个已选真实交旗的情形。
记 $i:F\hookrightarrow\mathcal H_{<x}$，并置
$$
 H_{X,F}=i^*H_{X,J}i.
$$
把 (4.2) 限制到同一个 $F$，即得 (4.3)--(4.4) 对
$H_{A,F},H_{C,F}$ 也成立。这里没有移动 $F$，也没有把
$i^*H_X^{-1}i$ 写成 $H_{X,F}^{-1}$。

## 5. 原同一个 forcing、完整能量列及环境残余配对

固定同一个 $f\in\mathcal H_{<x}$，包括原
$f_1=e_1\otimes\Omega$。在 §4 的同一个 $F$ 上定义
$$
 a_X=iH_{X,F}^{-1}i^*f,\qquad
 k_X=\mathcal R_{X,J}a_X,\qquad X=A,C.
 \tag{5.1}
$$
$k_X$ 正是 $(f,0,\ldots,0)$ 到完整列空间
$\mathcal R_{X,J}F$ 的正交投影。
因 $\mathcal M_U$ 是下三角且第零行是恒等，
$$
 \mathcal M_U^*(f\otimes e_0)=f\otimes e_0.
 \tag{5.2}
$$
因此 (5.1) 真的保留原 forcing；没有暗中改用一个反向列。

令 $E_C(f)=\|k_C\|^2=\langle H_{C,F}^{-1}i^*f,i^*f\rangle\le\|f\|^2$。
由 (4.3)，正矩阵
$H_{C,F}^{-1/2}H_{A,F}H_{C,F}^{-1/2}$
的谱在 $[e^{-2\Lambda},e^{2\Lambda}]$。故
$$
 \boxed{
 \|\mathcal R_{C,J}(a_A-a_C)\|
 \le(e^{2\Lambda}-1)E_C(f)^{1/2}.
 }
 \tag{5.3}
$$
再使用 (4.2)、(3.5)，得
$$
 \boxed{\|k_A-k_C\|
 \le(e^{3\Lambda}-1)E_C(f)^{1/2}
 \le(e^{3\Lambda}-1)\|f\|.}
 \tag{5.4}
$$
确切常数来自
$e^\Lambda(e^{2\Lambda}-1)+(e^\Lambda-1)=e^{3\Lambda}-1$。
交换两者也给以 $E_A(f)^{1/2}$ 为右端的同一界。

保完整环境残余
$$
 \xi_X=f-H_{X,J}a_X\in F^\perp.
$$
对任意环境测试 $v$，准确有
$$
 \begin{aligned}
 |\langle\xi_A-\xi_C,v\rangle|
 &\le
 \bigl(\|\mathcal M_U^*\mathcal M_U-I\|
       \|\mathcal R_{C,J}a_A\|
       +\|\mathcal R_{C,J}(a_A-a_C)\|\bigr)
       \|\mathcal R_{C,J}v\|\\
 &\le(e^{4\Lambda}-1)E_C(f)^{1/2}\,
       \|\mathcal R_{C,J}v\|.
 \end{aligned}
 \tag{5.5}
$$
这里使用 $\|\mathcal R_{C,J}a_A\|\le e^{2\Lambda}E_C(f)^{1/2}$。
所以也可写成完整能量对偶范数
$$
 \boxed{
 \|H_{C,J}^{-1/2}(\xi_A-\xi_C)\|
 \le(e^{4\Lambda}-1)E_C(f)^{1/2}.
 }
 \tag{5.6}
$$
最后一式不等于 $\|\xi_A-\xi_C\|$ 的同一上界；环境伴随费用没有被删除。

## 6. 实际 $S_x$、原高度窗及增长强前缀

原远尾方差满足
$$
 S_x=\sum_{i\ge x}(i+1)^{-4},\qquad
 \frac1{3(x+1)^3}\le S_x\le\frac1{3x^3}.
 \tag{6.1}
$$
对 $s\ge S_x$，以下一个明确条件足以应用全部前述结论：
$$
 \boxed{3J(x+1)^3\le\exp\!\left(\frac{417}{4}d^3\right).}
 \tag{6.2}
$$
在此范围 $\Lambda\le2e^{-15d^4/8}$，所以各相对误差趋零。
特别，(5.3)、(5.4) 的绝对源列误差，以及完整 inverse 的环境差范数，
均不超过 $e^{-d^4}\|f\|$（inverse 算子差省略 $\|f\|$）。
例如 $e^{3\Lambda}-1\le4\Lambda\le8e^{-15d^4/8}\le e^{-d^4}$。

### 6.1 原纯远高度窗

若
$$
 J=r-1\le\frac{\sqrt{x+1}}{8(m+1)},\qquad
 x+1\le e^{13d^3},
 \tag{6.3}
$$
则
$$
 \frac Js\le\frac{3(x+1)^{7/2}}{8(m+1)}
 \le\exp\!\left(\frac{91}{2}d^3\right)
 <\mathscr R_m^2.
$$
因此原全部允许的整数高度都满足 (6.2)，没有先固定 $r$ 再令 $x$ 增长。

### 6.2 整个强头有限塔

原 $C^{h}=0$，其中 $h=d+x-m$。若
$$
 m\ge10,\quad d\le x,\quad
 x+1\le\frac14e^{26d^3},\quad 0\le J\le h-1,
 \tag{6.4}
$$
则 $J\le2(x+1)$，因而
$$
 \frac Js\le6(x+1)^4
 \le\frac6{4^4}e^{104d^3}
 <e^{(417/4)d^3}=\mathscr R_m^2.
$$
这覆盖 $C$ 的整个有限塔。
若还需原母窗口支持，取 $Q\ge R+J$；在 (6.4) 中
$$
 R+J\le(x-m)+(d+x-m-1)<3(x+1)<e^{26d^3},
$$
故可同时选择原 c26 合法整数 $Q$。这里仍分别核了高度与母支持，未用 Gram 比较替代母窗口条件。

注意 $A_x$ 的幂零阶数可能远大于 $h$。本节比较的是相同有限高度 $J$ 的
$H_{A_x,J}$ 与 $H_{C,J}$，不把前者改成其无穷完整塔。

## 7. 乘子本身也保真正的物理孔权

以下固定 $\gamma=1/32$，在全部前 $x$ 位上令
$$
 \Gamma=\gamma^{-\mathcal N_{<x}}=32^{\mathcal N_{<x}}.
$$
这是真正物理孔数，未换成辅助 Jordan grade。它在辅助 Fock 因子上取恒等。

原 carry 分解在本头上准确为
$E=-\sum_{p=m}^{x-1}K_p$。每个 $K_p$ 只作用前 $p+1$ 位，
而 $D_m$ 中位于 $p$ 以后的项与它交换。
因此每个
$X_{jka,p}=A_m^j(\operatorname{ad}_{D_<}^{a}K_p)A_m^k$
也只作用前 $p+1$ 位。对两个方向均有
$$
 \|\Gamma X_{jka,p}\Gamma^{-1}\|,
 \quad\|\Gamma^{-1}X_{jka,p}\Gamma\|
 \le32^{p+1}\|X_{jka,p}\|.
 \tag{7.1}
$$
这里后 $x-p-1$ 位的孔权完全抵消，所以没有 $32^x$ 的费用。

c26 稿逐 $p$ 的 (0.2)、(5.2)--(5.3) 已经给
$$
 \mathscr R_m\sum_{j,k<d,a\ge0}
 \frac{\mathscr R_m^{j+k+a}}{(j+1)!k!a!}
 \|X_{jka,p}\|\le e^{-15\cdot16^p/8}.
 \tag{7.2}
$$
所以把 (1.4) 的每个项改成任一方向的真实孔权共轭后，得到
$$
 \begin{aligned}
 \Lambda_\gamma(b)
 &\le\frac b{\mathscr R_m}
       \sum_{p=m}^{x-1}32^{p+1}e^{-15\cdot16^p/8}\\
 &\le 2\frac b{\mathscr R_m}\,32^{m+1}e^{-15d^4/8}.
 \end{aligned}
 \tag{7.3}
$$
末一步由相邻项比
$32\exp[-(225/8)16^p]<1/2$ 得到，$m\ge10$ 时有充分余量。

§§2--3 的证明现在逐字适用于共轭后的头系数。
记 $\widehat\Gamma=\Gamma\otimes I_{\{0,\ldots,J\}}$，则
$$
 \boxed{
 \|\widehat\Gamma\mathcal M_U^{\pm1}\widehat\Gamma^{-1}\|,
 \quad
 \|\widehat\Gamma^{-1}\mathcal M_U^{\pm1}\widehat\Gamma\|
 \le e^{\Lambda_\gamma(b)},
 }
 \tag{7.4}
$$
四个算子与恒等的差范数均不超过
$e^{\Lambda_\gamma(b)}-1$。当 $b\le\mathscr R_m$ 时，这些差仍不超过
$e^{-d^4}$，因为 $(m+1)\log32+\log4\le7d^4/8$。

例如对同一个任意候选 $v$，确切有
$$
 \|\widehat\Gamma(\mathcal R_{A,J}v-\mathcal R_{C,J}v)\|
 \le(e^{\Lambda_\gamma}-1)
       \|\widehat\Gamma\mathcal R_{C,J}v\|.
 \tag{7.5}
$$
也可比较真正加权 Gram
$$
 H_{X,J}^{(\gamma)}
 :=\sum_{j=0}^{J}\frac{(X^*)^j\Gamma^2X^j}{j!s^j}:
 \quad
 e^{-2\Lambda_\gamma}H_{C,J}^{(\gamma)}
 \preceq H_{A,J}^{(\gamma)}
 \preceq e^{2\Lambda_\gamma}H_{C,J}^{(\gamma)}.
 \tag{7.6}
$$
任意同一 $F$ 的压缩仍保 (7.6)。

但是原最小者使用的是 $H_{X,F}$，并未改用
$H_{X,F}^{(\gamma)}$。因此 (7.4)--(7.6) 只免费运输已经付清的加权候选、测试和加权变分问题；
它们不把未知的 $\|\Gamma a_C\|$ 或
$\|\Gamma\xi_C\|$ 变成一个已知量。
特别不能将物理正交投影与 $\Gamma$ 交换。

## 8. 对当前最高 carry 缺口的准确用途

本稿直接扩大原同源完整 inverse 的强前缀范围，且可保任意给定的同一个 $F$。
若把基头从 $m$ 换成 $m-1$，同一证明也适用于
最高 carry 置零后的 $C_0=A_{m-1}+D_{[m-1,x)}$；预算中的
$d$ 必须相应换成 $2^{m-1}$，不能继续借用原 $m$ 的指数。

这没有比较 $F_0=\lim_{t\downarrow0}\ker C_t^r$
与 $\ker A_x^r$。在使用 (5.5)--(5.6) 控制
$\mathcal Z_\gamma$ 时，仍须支付高孔加权测试的
$\|\mathcal R_{C_0,J}v\|$，或直接证明原完整残余的加权衰减。
完整环境 inverse 与移动真核、原源能量与孔加权残余，是这里保留的两个不同接口。
