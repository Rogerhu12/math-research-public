# R236 附录：更快多项式排序行的全部重数循环性

日期：2026-11-13（UTC）。独占作者：central_next；AI-assisted，GPT-6 Astra Pro。
状态：已证明；根会话已独立全文核验实阶乘预算、实际正锥、保重数逆及有界全域反射配对。
本稿使用原实际 Haar 模型；继承 [R260](../results/R260-arbitrary-span-derivation-budgets-and-sorted-bell-kernels.md) 的任意跨度真实反射误差，
并重付实指数阶乘幂界、保重数 Bézout 逆和局部实际 A 因子。
没有对未知不变子空间实施坐标重排，不把本结论当作普通 ISP 完成。

## 1. 定理、实际算子及本范围内的完整自然域

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a_*\in\mathbb C,
$$
并令非零幅度的非增重排为 $\rho_k$，$k\ge1$。
假设存在一个固定实数 $\sigma>1$，满足
$$
\boxed{
0<\limsup_{k\to\infty}k^\sigma\rho_k
\le B:=\sup_{k\ge1}k^\sigma\rho_k<\infty.
}
\tag{1.1}
$$
各 $a_j$ 的复相位与原物理排列任意。
固定任意复 first 指数权
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2,\qquad
t_j=e^{-2b_j},\qquad
R_j=V(t_jN_j),\qquad V(z)=\frac{I-z}{I+z}.
$$
记
$$
L=\max(1,\sup_j|t_j|,\sup_j|t_j|^{-1})<\infty.
$$
有限个低位使用实际准幂零预解式，高位使用
$N_j^2=\eta_jN_{j+1}$，给
$\sup_{j,\epsilon=\pm1}\|(I+\epsilon t_jN_j)^{-1}\|<\infty$。
因此 $\sup_j\|R_j\|<\infty$。

本范围有一个应明确使用的简化：
$$
\sum_j|a_j|=\sum_{k\ge1}\rho_k\le B\zeta(\sigma)<\infty.
\tag{1.2}
$$
所以真实倾斜 first 是按算子范数收敛的实际算子
$$
X=X_b=a_*I+\sum_ja_jR_j\in\mathcal A\subset B(H),
\qquad H=L^2(\mathbb Z_2).
\tag{1.3}
$$
这里 $\mathcal A=\overline{\mathbb C[A]}^{\|\cdot\|}$。
(1.3) 先在 R125/R176 的真实柱图核心上与原定义相等；
右端为全域有界算子，图闭包遂给完整等式。
没有通过改变 first 的求和排列定义一个新算子。

对 $n\ge2$，令
$$
L_n(v)=\left.\frac{d^n}{ds^n}
\log(\cosh s+v\sinh s)\right|_{s=0},\qquad
G_n=\sum_ja_j^nL_n(R_j)\in\mathcal A.
\tag{1.4}
$$
这些级数按范数绝对收敛。
给定非零标量多项式 $q$，除去非零首系数后设其首一、次数为 $p\ge2$，
定义
$$
\mathcal P(z;\kappa)=
\exp\left(\sum_{n=2}^p\frac{\kappa_n}{n!}\partial_z^n\right)q(z),
\qquad T=\mathcal P(X;G).
\tag{1.5}
$$
指数在有限多项式空间上是有限和。
本范围的 $X,T$ 全部有界，所有自然幂域都是 $H$；
下文没有未支付的无界乘积域。
R176 的完整 $C$ 自伴性和循环像公式仍适用。

**定理。** 在 (1.1) 下，对任意上述 $q,w$，
$$
\boxed{\ker T=0,\qquad q(u)e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.6}
$$
$q$ 的根可有任意有限重数。
次数为零、一次的情形已由 R16/R147 包含。
本稿以下证明 $p\ge2$；常数允许依赖固定的
$\sigma,B,a_*,b,p,q$ 和原模型，不依赖所选高位集合的最大物理位。

## 2. 任意正实指数的阶乘级数界

后面的阶乘指数通常不是整数，先给一个独立估计。

**引理。** 对任意固定实数 $s>0$，存在 $K_s<\infty$，使
$$
\boxed{
\sum_{k=0}^{\infty}\frac{x^k}{(k!)^s}
\le K_s\exp\big((s+1)x^{1/s}\big)
\qquad(x\ge0).
}
\tag{2.1}
$$

**证明。**
$x=0$ 显然。设 $y=x^{1/s}>0$，
$m=\max(1,\lceil2ey\rceil)$。
由 $\log(k!)\ge k\log k-k$，对 $k\ge1$，
$$
\frac{x^k}{(k!)^s}
\le\left(\frac{ey}{k}\right)^{sk}
\le e^{sy},
$$
最后一步用函数 $v\log(e/v)\le1$。
$k=0$ 也服从 $e^{sy}$ 界。
故 $k<m$ 的项和至多 $(1+2ey)e^{sy}$。
当 $k\ge m$ 时 $ey/k\le1/2$，尾和不超过
$(1-2^{-s})^{-1}$。
利用 $1+2ey\le(1+2e)e^y$，可取
$$
K_s=1+2e+(1-2^{-s})^{-1}.
$$
这证明 (2.1)，没有使用只对整数 $s$ 成立的多重对角展开。

## 3. 原正锥主控：实衰减指数只进入标量乘积

原 $A$ 和 $N_j=A^{2^j}/d_j$ 保持函数的逐点非负锥。
这里的正性不是 Hilbert 自伴正性。
真实关系为
$$
N_j^2=\eta_jN_{j+1},\qquad \|N_j\|=1,\qquad
0<\eta_j\le\bar\eta_j:=e^{-770\,16^j}.
\tag{3.1}
$$

写
$$
L_n(1+x)=\sum_{\ell=1}^nc_{n,\ell}x^\ell,\qquad
W_n(z)=\sum_{\ell=1}^n|c_{n,\ell}|
       \left(\frac{2Lz}{1-Lz}\right)^\ell.
\tag{3.2}
$$
$W_n(0)=0$，全部 Taylor 系数非负。
$N_j$ 准幂零，故这些实际有理函数的 Taylor 级数按范数绝对收敛。
令
$$
W_n(z)=zW_{n,1}(z)=w_{n,1}z+z^2W_{n,2}(z).
$$
由高位恒等式
$$
(I-LN_j)^{-1}=(I+LN_j)(I-L^2\eta_jN_{j+1})^{-1}
$$
及有限低位真实预解式，有
$$
\sup_j\|(I-LN_j)^{-1}\|<\infty,\qquad
B_{n,i}:=\sup_j\|W_{n,i}(N_j)\|<\infty\quad(i=1,2).
\tag{3.3}
$$
没有把范数为 1 的 $N_j$ 直接代入一个半径可能小于 1 的标量收敛界。

由 $R_j-I=-2t_jN_j(I+t_jN_j)^{-1}$ 的实际级数，
$$
|L_n(R_j)f|\le W_n(N_j)|f|.
$$
于是实际正主控
$$
M_n=\sum_j|a_j|^nW_n(N_j)
\tag{3.4}
$$
按范数收敛，并满足
$$
|G_n^kf|\le M_n^k|f|,\qquad \|G_n^k\|\le\|M_n^k\|.
\tag{3.5}
$$
收敛与逐次正锥主控使用
$\sum_j|a_j|^n\le B^n\zeta(n\sigma)$。

把 $N_j$ 的偶、奇幂分开，实际平方关系给
$$
\|e^{zN_j}\|\le(1+|z|)e^{|z|\sqrt{\eta_j}}.
$$
再用
$\|W_n(N_j)-w_{n,1}N_j\|\le B_{n,2}\eta_j$
以及这两个项交换，得到对 $v\ge0$、$t=|z|$，
$$
\|e^{zvW_n(N_j)}\|
\le(1+w_{n,1}tv)\exp(C_ntv\sqrt{\eta_j}).
\tag{3.6}
$$
这是包含全部实际进位的指数界。

按原物理位取最小 $h=h(t)\ge1$，使
$$
385\,16^h\ge2\log(2+t).
\tag{3.7}
$$
真实尾的乘积估计由有限乘积再取范数极限得到。
令 $\nu=n\sigma>1$，仅在非负标量乘积中使用排序：
$$
\begin{aligned}
\sum_{j\ge h}\log(1+w_{n,1}t|a_j|^n)
&\le\sum_{k\ge1}\log(1+w_{n,1}B^nt/k^\nu)\\
&\le I_\nu(w_{n,1}B^nt)^{1/\nu},
\end{aligned}
\tag{3.8}
$$
其中
$$
I_\nu=\int_0^\infty\log(1+x^{-\nu})\,dx<\infty.
$$
第二步是单调积分比较。
原物理尾进位则直接满足
$$
\sum_{j\ge h}|a_j|^n\sqrt{\eta_j}
\le2B^ne^{-385\,16^h}\le2B^n(2+t)^{-2}.
\tag{3.9}
$$
故
$$
\|e^{zM_{n,\ge h}}\|\le K_ne^{C_nt^{1/\nu}}.
\tag{3.10}
$$
排序后的第 $k$ 项没有被当作原物理第 $k$ 位。

有限物理头有真实 $A$ 因子
$$
M_{n,<h}=A U_{n,h},\qquad
U_{n,h}=\sum_{j<h}|a_j|^n d_j^{-1}
 A^{2^j-1}W_{n,1}(N_j)\in\mathcal A.
\tag{3.11}
$$
由原模型
$$
d_j=e^{-\Lambda_j},\qquad
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j
\le125\,16^j
$$
及 $\|A\|<1$，
$$
\|U_{n,h}\|\le
B_{n,1}B^n\zeta(n\sigma)e^{125\,16^{h-1}}.
\tag{3.12}
$$
(3.7) 的最小性给
$16^{h-1}\le1+2\log(2+t)/385$，从而
$$
\log(2+t\|U_{n,h}\|)\le C_n+2\log(2+t).
\tag{3.13}
$$

[R109](../results/R109-invariant-restriction-exact-quartic-type.md) 的真实四次幂界蕴含固定 $K_A,c_A>0$ 下
$\|A^k\|\le K_Ae^{-c_Ak^4}$。
$A$ 与 $U_{n,h}$ 交换，因此
$$
\|e^{zAU_{n,h}}\|
\le K_A\sum_{k\ge0}e^{-c_Ak^4}
            \frac{(t\|U_{n,h}\|)^k}{k!}.
$$
若 $\ell=\log(2+t\|U_{n,h}\|)$，优化给
$-c_Ak^4+k\ell\le-c_Ak^4/2+C_A\ell^{4/3}$。
舍去 $1/k!\le1$ 后求和，并用 (3.13)，得到
$$
\|e^{zM_{n,<h}}\|
\le K_n\exp\big(C_n(1+\log(2+t))^{4/3}\big)
\le K_n'e^{C_n't^{1/\nu}}.
\tag{3.14}
$$
最后一步只需要固定有限的实数 $\nu$。
头尾实际交换，故
$$
\boxed{
\|e^{zM_n}\|\le K_ne^{C_n|z|^{1/(n\sigma)}}
\qquad(z\in\mathbb C).
\tag{3.15}
$$
有限头的常数随参数增长已由 (3.12)--(3.14) 明确支付。

## 4. 分阶实阶乘幂与一次联合预解成本

令 $\nu=n\sigma$。
对 (3.15) 作 Cauchy 系数估计，
整数 $k\ge1$ 时取半径 $R=(\nu k/C_n)^\nu$，得到
$$
\|M_n^k\|
\le K_n k!e^{\nu k}\left(\frac{C_n}{\nu k}\right)^{\nu k}.
$$
由 $(k!)^\nu\le k^{\nu k}$ 及 (3.5)，
$$
\boxed{
\|G_n^k\|\le K_n\frac{D_n^k}{(k!)^{n\sigma-1}},
\qquad D_n=(eC_n/\nu)^\nu,\qquad k\ge0.
}
\tag{4.1}
$$
$k=0$ 吸入 $K_n\ge1$。

对任意 $z\ne0$，级数
$\sum_{k\ge0}z^{-k-1}G_n^k$ 绝对收敛。
左右乘 $z-G_n$ 都望远镜为 $I$，所以它是真正的有界预解式。
应用 §2，取 $s_n=n\sigma-1>0$，
$$
\boxed{
\|(z-G_n)^{-1}\|
\le\frac{\widetilde K_n}{|z|}
       \exp\big(\widetilde C_n|z|^{-1/(n\sigma-1)}\big).
}
\tag{4.2}
$$
这也明确证明每个实际坐标谱都只有零。

固定 $p$、$\varepsilon>0$，取 $0<\tau\le1$。
若 $F$ 在闭多圆盘
$|\kappa_n|\le\varepsilon\tau^n$ 的某邻域全纯，
且在其边界多圆周上 $|F|\le M_F$，
共同 Cauchy 公式给
$$
F(G)=\frac1{(2\pi i)^{p-1}}
\int_{\prod_{n=2}^p\{|z_n|=\varepsilon\tau^n\}}
F(z)\prod_{n=2}^p(z_n-G_n)^{-1}\,dz.
$$
这些实际预解式都属于同一个交换代数。
圆周长度消去 (4.2) 的 $|z_n|^{-1}$。
函数 $n\mapsto n/(n\sigma-1)$ 严格递减，故
$$
\boxed{
\|F(G)\|\le K M_F
 \exp\big(C_\varepsilon\tau^{-\beta}\big),\qquad
\beta=\frac2{2\sigma-1}.
}
\tag{4.3}
$$
$K,C_\varepsilon$ 与 $\tau,F$ 无关。
这是对整个系数函数的一次共同求值，不能对每个位的逆重复支付它。

## 5. 同幅高位桶与固定非零平均极限

由 (1.1)，选固定 $c_0>0$ 和 $N\to\infty$ 的子序列，
使 $N^\sigma\rho_N\ge c_0$。
从幅度最大的 $N$ 个实际指标中，
删去排序最前 $\lfloor N/4\rfloor$ 项，
再删去物理位置 $j<\lfloor N/4\rfloor$ 的项。
至少剩 $N/2$ 项，且
$$
j\ge h_N:=\lfloor N/4\rfloor,\qquad
c_0N^{-\sigma}\le|a_j|\le4^\sigma B N^{-\sigma}.
\tag{5.1}
$$
第二个上界来自剩余排序秩大于 $N/4$。

令
$$
J=\left\lceil\log_2(4^\sigma B/c_0)\right\rceil+1,\qquad
\kappa=\frac1{4J},\qquad Q_N=\lfloor\kappa N\rfloor.
$$
按二进幅度分桶，至少一桶含 $N/(2J)$ 项。
从其中取恰有 $Q_N$ 个实际指标组成 $I_N$；
记桶左端为 $\tau_N$。于是
$$
\boxed{
\min I_N\ge h_N,\quad
\tau_N\le|a_j|<2\tau_N\ (j\in I_N),\quad
c_0N^{-\sigma}\le\tau_N\le4^\sigma B N^{-\sigma}.
}
\tag{5.2}
$$
完全不限制 $\max I_N$。

置
$$
r=r_N=\lfloor\sqrt{Q_N}\rfloor.
\tag{5.3}
$$
则 $Q_N/r^2\to1$，$r=O(\sqrt N)$，
$r\tau_N\to0$，充分大 $N$ 时 $r\le Q_N$。
以后 $F\subset I_N$、$|F|=r$。
与临界 $\sigma=1$ 情形不同，这里不需要另选一个很小的平均参数。

## 6. 保重数的真实 Bézout 逆

Bell 恒等式给
$$
4L_n'(1)=-2(-2)^n,\qquad
\partial_{\kappa_n}\mathcal P=\frac1{n!}\partial_z^n\mathcal P.
$$
故每个位的一次系数准确为
$$
\boxed{
\mathscr L_a(z;\kappa)
=4a\partial_z\mathcal P+
 \sum_{n=2}^p4L_n'(1)a^n\partial_{\kappa_n}\mathcal P
=-2[\mathcal P(z-2a;\kappa)-\mathcal P(z;\kappa)].
}
\tag{6.1}
$$

令 $q$ 的不同根为 $\lambda_\nu$、重数为 $\mu_\nu$。
存在固定 $\varepsilon,\tau_0>0$，
使 $0<\tau\le\tau_0$、
$|\kappa_n|\le2\varepsilon\tau^n$ 时，
$\mathcal P$ 的每个根团都在
$|z-\lambda_\nu|<\tau/4$ 中，并保留 $\mu_\nu$ 个根（按重数计）。
理由是 Bell 的权为 $n$：
$\mathcal P-q=\sum_{k=2}^p\beta_k(\kappa)q^{(k)}$，
且 $|\beta_k|\le C_q\varepsilon\tau^k$。
在上述圆周上，$|q|\ge c_q\tau^{\mu_\nu}$；
所有微分扰动之和至多
$C_q\varepsilon\tau^{\mu_\nu}$。
取 $\varepsilon$ 足够小后，Rouché 同时给根计数和圆周上的同阶下界。

当 $\tau\le|a_j|<2\tau$ 时，
对原团的整个闭圆盘，平移 $2a_j$ 后与该团及其它根团分离。
同团的距离至少 $3\tau/2$，其它团用 $q$ 的固定根距控制。
因此
$$
|\mathcal P(z-2a_j;\kappa)|\ge c_q\tau^{\mu_\nu}
\ge c_q\tau^p
\quad\text{当 }|z-\lambda_\nu|\le\tau/4.
\tag{6.2}
$$
此处允许 $a_j$ 有任意复相位。

置
$$
H_F(z;\kappa)=\prod_{j\in F}[-2\mathcal P(z-2a_j;\kappa)],
\qquad h_F=H_F^{-1}
$$
（$h_F$ 在上述根团圆盘的邻域全纯），并在
$\Gamma_\nu=\{|\zeta-\lambda_\nu|=\tau/4\}$ 上定义
$$
\mathcal R_F(z;\kappa)=
\frac1{2\pi i}\sum_\nu\int_{\Gamma_\nu}
h_F(\zeta;\kappa)
\frac{\mathcal P(\zeta;\kappa)-\mathcal P(z;\kappa)}
 {(\zeta-z)\mathcal P(\zeta;\kappa)}\,d\zeta.
\tag{6.3}
$$
它对 $z$ 的次数小于 $p$，系数在
$|\kappa_n|\le\varepsilon\tau^n$ 的邻域全纯，并有
$$
|[z^k]\mathcal R_F|\le C_q^{r+1}\tau^{-pr-p+1}.
\tag{6.4}
$$
这是 (6.2)、圆周上 $\mathcal P$ 的下界、长度 $O(\tau)$
以及有界的多项式差商系数的乘积。

Cauchy 公式说明 $h_F-\mathcal R_F$ 在各根团内
被 $\mathcal P$ 全纯整除，因此保留全部根的全部重数。
由 (6.1)，在解析系数的多项式环中有
$$
\boxed{
\mathcal R_F\prod_{j\in F}\mathscr L_{a_j}
=1+\mathcal P\,\mathcal S_F.
}
\tag{6.5}
$$
这里可以对首一 $\mathcal P$ 作多项式除法；
商的系数仍全纯。没有只在根值上插值。

取 $\tau=\tau_N$，对 $\mathcal R_F$ 的每个系数
一次使用 (4.3)，再在实际有界 $X$ 上求值，得到
$$
\mathfrak R_F:=\mathcal R_F(X;G)\in\mathcal A.
$$
若 $M=\ker T$，则 $\mathfrak R_F$ 保持 $M$，且
$$
\boxed{
L_F\mathfrak R_F f=f\quad(f\in M),\qquad
L_F=\prod_{j\in F}\mathscr L_{a_j}(X;G).
}
\tag{6.6}
$$
注意在本有界范围内 $\mathfrak R_F$ 本身就是全 $H$ 的有界算子。
由 (5.2)，存在固定 $K$ 使
$$
\boxed{
\|\mathfrak R_F\|
\le\exp\big(KN^\theta+Kr\log(N+2)+K\big),\qquad
\theta=\sigma\beta=\frac{2\sigma}{2\sigma-1}<2.
}
\tag{6.7}
$$
未知核 $M$ 没有进入这个常数。

## 7. 任意物理跨度的有界反射误差及真实幂

令 $\mathsf J_F=\prod_{j\in F}M_{\chi_j}$，
$\gamma_F(B)=\mathsf J_FB\mathsf J_F$。
使用 R260 §§2--4 在 $Y=0$、导数阶数为零时的真实壳估计：
$$
\widehat X_F=X+\sum_{j\in F}a_j[V(-t_jN_j)-R_j],
$$
$$
\widehat G_{n,F}
=G_n+\sum_{j\in F}a_j^n
 [L_n(V(-t_jN_j))-L_n(R_j)],
$$
$$
\boxed{
\|\gamma_F(X)-\widehat X_F\|
+\sum_{n=2}^p\|\gamma_F(G_n)-\widehat G_{n,F}\|
\le\epsilon_N,\qquad
\epsilon_N\le C e^{-385\,16^{h_N-1}}.
}
\tag{7.1}
$$
常数不含 $\max I_N$。
这里 $\widehat X_F,\widehat G_F\in\mathcal A$，
而真正的反射误差一般不在这个交换代数中。

由 (5.2)，替身相对原变量的差满足
$$
\|\widehat X_F-X\|\le Cr\tau_N,\qquad
\|\widehat G_{n,F}-G_n\|\le C_nr\tau_N^n.
$$
所以这些变量全部一致有界。
有限多项式逐因子相减给
$$
\widehat T_F=\mathcal P(\widehat X_F;\widehat G_F),\quad
A_F=\widehat T_F-T,\quad
E_F=\gamma_F(T)-\widehat T_F,\qquad
\|E_F\|\le C\epsilon_N.
\tag{7.2}
$$
$T,\widehat T_F,A_F$ 在 $\mathcal A$ 中交换；
不假定 $E_F$ 与它们交换。
取一个固定常数 $C_T\ge1$ 同时控制其范数及
$\|\gamma_F(T)\|=\|T\|$。

令 $f_F=\mathfrak R_Ff$、$v_F=\mathsf J_Ff_F$，$f\in M$。
则 $\gamma_F(T)v_F=0$。
对 $k\ge1$，真实非交换幂差恒等式给
$$
\|\widehat T_F^k v_F\|
=\|(\widehat T_F^k-\gamma_F(T)^k)v_F\|
\le C\epsilon_N k C_T^{k-1}\|f_F\|.
$$
又 $T=\widehat T_F-A_F$ 的两项交换，所以二项式求和给
$$
\boxed{
\|T^rv_F-(-A_F)^rv_F\|
\le C\epsilon_N r(2C_T)^{r-1}\|f_F\|.
}
\tag{7.3}
$$
这一步没有把非交换的真实反射误差当作交换系数。
所有算子在本范围都全域有界，故 (7.3) 是真实自然幂等式的估计。

## 8. Boolean 主项与移过反射：每个重复位都付实际进位

用真实 $N_j^2=\eta_jN_{j+1}$，
带符号的有理式可在抽出明确二次余项后写成
$$
\widetilde A_F=
\mathcal P\left(
X+4\sum_{j\in F}a_jt_jN_j;\
G_n+4L_n'(1)\sum_{j\in F}a_j^nt_jN_j
\right)-\mathcal P(X;G).
\tag{8.1}
$$
统一真实分母界、$\sum_{j\in F}|a_j|\le2r\tau_N$ 给
$$
\|A_F-\widetilde A_F\|\le C\bar\eta_{h_N}.
\tag{8.2}
$$
例如
$V(-tN)-V(tN)=4tN(I-t^2N^2)^{-1}$；
减去 $4tN$ 的余项真含 $N^2$。
其它固定次数多项式的余项同样如此。

在交换形式变量 $x_j$ 中，(8.1) 没有常数项，
其一次部分恰为
$$
\sum_{j\in F}t_jx_j\mathscr L_{a_j}(X;G).
$$
系数环可以包含原实际 $N_j$；不假定这些实际算子代数独立。
这个形式多项式的系数范数绝对和统一有界，
因为 $p$ 固定、$X,G$ 有界、$r\tau_N\to0$。
$r$ 个正次数因子相乘而变量只有 $r$ 个，故平方自由部分恰为
$$
\widetilde A_F^r\equiv r!t_FN_FL_F
\pmod{(N_j^2:j\in F)},\qquad
t_F=\prod_{j\in F}t_j,\quad N_F=\prod_{j\in F}N_j.
\tag{8.3}
$$
每个弃项真含一个重复位，
代入实际算子后由 (3.1) 多出 $\bar\eta_{h_N}$。
系数绝对和至多 $C^r$。
结合 (8.2) 的幂差，
$$
\|A_F^r-r!t_FN_FL_F\|
\le\bar\eta_{h_N}\exp(Cr\log(r+2)).
\tag{8.4}
$$

还需把 $L_F$ 移过 $\mathsf J_F$。
令 $\widehat L_F$ 为把 $L_F$ 中的 $X,G$
替换为 $\widehat X_F,\widehat G_F$ 的交换替身。
由 (7.1) 的逐因子差，
$$
\|\gamma_F(L_F)-\widehat L_F\|
\le\epsilon_N rC^r.
$$
另一方面，$\widehat L_F-L_F$ 的每个形式差项含一个选中 $N_j$，
其余系数范数的绝对和至多 $C^r$。
左乘 $N_F$ 后就真含重复位，所以
$$
\|N_F(\widehat L_F-L_F)\|
\le\bar\eta_{h_N}C^r.
$$
准确使用
$$
L_F\mathsf J_F-\mathsf J_FL_F
=(L_F-\gamma_F(L_F))\mathsf J_F
$$
并乘上 $r!t_F$，该移动的全部成本仍至多
$\epsilon_N\exp(Cr\log(r+2))$；
较小的 $\bar\eta_{h_N}$ 已吸入 $\epsilon_N$。
没有假定 $L_F$ 与反射交换。

最后由 (6.6) 的真实 Bézout 逆消去 $L_Ff_F$，
合并 (7.3)、(8.4)，得到
$$
\boxed{
\|T^r\mathsf J_F\mathfrak R_Ff
-(-1)^rr!t_FN_F\mathsf J_Ff\|
\le\epsilon_N e^{Cr\log(r+2)}
 \|\mathfrak R_F\|\,\|f\|,\qquad f\in M.
}
\tag{8.5}
$$
整个估计只依赖所选位的最小物理位，不依赖跨度。

## 9. 对称平均与真实非零弱极限

定义
$$
\mathcal V_N=
(-1)^r\left(\frac2{Q_N}\right)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
 t_F^{-1}\mathsf J_F\mathfrak R_F.
\tag{9.1}
$$
它是实际有界算子，且
$$
\|\mathcal V_N\|\le A_N:=
\frac{(2L)^r}{r!}\sup_F\|\mathfrak R_F\|
\le\exp\big(KN^\theta+Kr\log(N+2)+K\big).
\tag{9.2}
$$

不同物理位的 $E_j$ 交换，$E_j^2=0$，
$E_j\mathsf J_j=E_j$，且 $\|N_j-E_j\|\le\bar\eta_j$。
故
$\|N_F\mathsf J_F-\prod_{j\in F}E_j\|\le r\bar\eta_{h_N}$。
将 (8.5) 求和得到
$$
\boxed{
\|T^r\mathcal V_Nf-C_{I_N}^rf\|\longrightarrow0
\quad(f\in M),\qquad
C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j.
}
\tag{9.3}
$$
一个明确的总误差上界为固定常数乘
$$
\epsilon_N
\exp\big(KN^\theta+Kr\log(N+2)+Cr\log(r+2)+K\big)
+2^rr\bar\eta_{h_N},
$$
它因 $h_N\asymp N$、$r=O(\sqrt N)$ 而趋零。

有限位提升矩阵在每个占据数层的行列和给
$\|\sum_{j\in I_N}E_j\|\le(Q_N+1)/2$，
从而
$$
\|C_{I_N}^r\|\le(1+1/Q_N)^r\longrightarrow1.
$$
对固定有限柱 $v,z$，充分大 $N$ 时它们的物理支撑低于 $\min I_N$，
准确有
$$
\langle C_{I_N}^rv,z\rangle
=\frac{(Q_N)_r}{Q_N^r}\langle v,z\rangle
\longrightarrow e^{-1/2}\langle v,z\rangle.
$$
这是 $r^2/Q_N\to1$、
$r^3/Q_N^2\to0$ 下的有限下降阶乘极限。
一致范数界把它扩展到全 $H$：
$$
\boxed{
C_{I_N}^r\rightharpoonup e^{-1/2}I,\qquad
T^r\mathcal V_N f\rightharpoonup e^{-1/2}f\quad(f\in M).
}
\tag{9.4}
$$
这里只使用已知实际局部矩阵，未搬运未知子空间；
也没有声称强趋于恒等。

## 10. 固定局部矩阵的真实 A 因子与四次衰减

固定任意有限局部矩阵 $D$，其物理支撑小于 $h$。
置
$$
Z_h=X-a_*I-\sum_{j<h}a_jR_j,\qquad
s_h=a_*+\sum_{j<h}a_j,\qquad
G_{n,\ge h}=\sum_{j\ge h}a_j^nL_n(R_j).
$$
这里所有和都是实际范数收敛的有界算子；
$D$ 与 $Z_h$、全部 $G_{n,\ge h}$ 交换，
因为实际 $N_j$ 只作用于物理位 $j$ 及更高位。

有限低头具有明确除法
$$
X-(Z_h+s_h)=A U_{1,h},\qquad
G_n-G_{n,\ge h}=A U_{n,h},
$$
其中
$$
U_{1,h}=-2\sum_{j<h}
 \frac{a_jt_j}{d_j}A^{2^j-1}(I+t_jN_j)^{-1},
$$
$$
U_{n,h}=-2\sum_{j<h}
 \frac{a_j^nt_j}{d_j}A^{2^j-1}
 (I+t_jN_j)^{-1}\widetilde L_n(R_j),
\qquad L_n(v)=(v-1)\widetilde L_n(v).
\tag{10.1}
$$
这些是固定 $h$ 的实际有界 $\mathcal A$ 元素。

有限多项式逐项相减给
$$
T=T_{\rm tail}+A U_h,\qquad
T_{\rm tail}=\mathcal P(Z_h+s_h;G_{\ge h}),\qquad
U_h\in\mathcal A\subset B(H).
\tag{10.2}
$$
$T_{\rm tail}$ 与 $D$ 交换，
并与 $A U_h$ 交换。
于是全 $H$ 上准确有
$$
\operatorname{ad}_T^rD
=\sum_{s=0}^r(-1)^s\binom rs
 (A U_h)^{r-s}D(A U_h)^s.
\tag{10.3}
$$
每一项真含左右合计 $r$ 个 $A$；
没有把 $A$ 移过 $D$。

R109 给
$$
\|A^{r-s}\|\,\|A^s\|
\le\exp\left(-\frac56r^4+105r^3\right)
\qquad(0\le s\le r).
\tag{10.4}
$$
因此
$$
\boxed{
\|(\operatorname{ad}_T^rD)\mathcal V_Nf\|
\le\|D\|\,[2\|U_h\|]^r A_N
 \exp\left(-\frac56r^4+105r^3\right)\|f\|.
}
\tag{10.5}
$$
$U_h=0$ 时该式按其直接零值解释。
因为 $r^4\asymp N^2$、$\theta<2$，
(9.2)--(10.5) 的对数上界为
$$
-\frac56r^4+105r^3+KN^\theta
+O(r\log(N+2)+r)\longrightarrow-\infty.
\tag{10.6}
$$
这正是 $\sigma>1$ 带来的严格指数余量。
任意固定局部 $D$ 的常数只进入 $O(r)$ 项。

## 11. 完整双线性配对与循环性

令 $B(f,g)=\langle f,Cg\rangle$。
实际 $T$ 为有界 $C$ 自伴算子，所以
$B(Tf,g)=B(f,Tg)$ 对所有 $f,g\in H$ 成立。
取 $f,g\in M=\ker T$。
(10.3) 的真实 Leibniz 展开中，所有左侧含正次 $T$ 的项
与 $g$ 配对为零，因此
$$
B(DT^r\mathcal V_Nf,g)
=(-1)^rB((\operatorname{ad}_T^rD)\mathcal V_Nf,g).
\tag{11.1}
$$
右侧由 (10.6) 趋零；
左侧由 (9.3)--(9.4) 趋于 $e^{-1/2}B(Df,g)$。
故
$$
B(Df,g)=0
\qquad(f,g\in M,\ D\text{ 任意固定有限局部矩阵}).
\tag{11.2}
$$

原 Haar 局部全矩阵 $*$-代数不可约，
任意非零 $f$ 的局部轨道稠密。
若 $0\ne f\in M$，在 (11.2) 取 $g=f$，
则稠密局部轨道都与 $Cf$ 正交，迫 $Cf=0$，矛盾。
所以 $\ker T=0$。

R176 的实际向量 $\xi_w=e^w$ 循环，且
$$
T\xi_w=q(u)e^w,\qquad
[q(u)e^w]_A=\overline{\operatorname{Ran}T}.
$$
$T$ 的完整 $C$ 自伴性使
$\ker T^*=C\ker T=0$，
所以 $\operatorname{Ran}T$ 稠密，证明 (1.6)。

## 12. 新关闭的范围与不能推出的结论

本稿覆盖任意固定实 $\sigma>1$，
幅度满足 (1.1) 的所有复系数行、
任意物理排列、任意有限低头与 $a_*$、
任意复 $\ell^2$ first 指数权，以及任意有限重数标量多项式。
例如幅度 $k^{-2}$ 的任意物理排列与任意复相位，
现在所有 $q(u)e^w$ 都循环，包括同字符的混合重根情形。

这类行满足 $k\rho_k\to0$，
所以并未被临界弱 $\ell^1$ 的正下限上极限条件直接覆盖。
这里真正的新预算是实阶乘指数 $n\sigma-1$，
以及联合 Bell 圈的成本
$\exp(C\tau^{-2/(2\sigma-1)})$；
它使一次 Bézout 输入只付 $\exp(O(N^\theta))$，$\theta<2$。
不能用较粗的弱 $\ell^1$ 预解界替代这个步骤。

没有证明只假设 $k\rho_k\to0$ 的所有行，
没有覆盖所有不满足任何固定幂次正上极限条件的幅度谱（例如几何衰减谱），
也没有由本稿覆盖 $1/2<\sigma<1$ 的全部重数。
后一个区间的同样计算会产生 $\theta>2$，
本稿的四次局部预算不足以吸收它。

多模式多项式、一般有限 chaos、正常湮灭者、
边界 $N=M$ 和完整普通 Hilbert ISP 均未由本稿关闭。
