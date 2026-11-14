# 伸展指数至几何衰减排序行的全部重数：不同幅高位与对数预解预算

日期：2026-11-13（UTC）。独占作者：central_next；AI-assisted，GPT-6 Astra Pro。
状态：已证明；这是原实际 Haar 模型的中间结论，普通 Hilbert ISP 未完成。
固定原实际 Haar 模型。本文证明标量多项式的全部有限重数，
不将既有解析分支或无重根结果重复计为新结论。

并行主线 [R266](../results/R266-all-multiplicities-for-rearranged-exponential-rows-and-logarithmic-resolvents.md) 已证明所有充分大排序秩均有双侧指数界时的全部重数。本文保留独立的完整推导，其严格扩展是下界只需沿无穷子序列成立，并显式给出真实累积量的 $\exp(-d_nk^{1+\alpha})$ 幂界。两稿重叠的双侧类不重复计为新范围。

## 1. 精确范围与全域有界模型

令 $\rho_k$ 是非零复系数 $a_j$ 幅度的非增重排。
假设存在固定参数
$$
0<\alpha\le1,\qquad 0<\beta_-\le\beta_+,\qquad B,c_0>0
$$
以及趋于无穷的整数子序列 $N$，使
$$
\boxed{
\rho_k\le B e^{-\beta_- k^\alpha}\quad(k\ge1),\qquad
\rho_N\ge c_0e^{-\beta_+N^\alpha}\quad\text{沿该子序列}.
}
\tag{1.1}
$$
下界只需沿子序列，不要求对全部排序秩成立。
原物理排列、复相位、有限低头及 $a_*\in\mathbb C$ 任意。
取
$$
u=a_*+\sum_ja_j\chi_j,\qquad
w=c_*+\sum_jb_j\chi_j,\quad b\in\ell^2,\qquad
t_j=e^{-2b_j},\quad R_j=V(t_jN_j).
$$
令
$L=\max(1,\sup_j|t_j|,\sup_j|t_j|^{-1})<\infty$。
有限低位的实际准幂零预解式及高位真实平方关系给
$\sup_{j,\epsilon=\pm1}\|(I+\epsilon t_jN_j)^{-1}\|<\infty$。

(1.1) 给 $\sum_j|a_j|<\infty$，所以
$$
X=X_b=a_*I+\sum_ja_jR_j\in\mathcal A,\qquad
\mathcal A=\overline{\mathbb C[A]}^{\|\cdot\|},
\tag{1.2}
$$
级数按原物理次序范数绝对收敛。
它在真实柱图核心上等于 R125/R176 的倾斜 first，
故全图闭包与 (1.2) 相等，定义域就是 $H=L^2(\mathbb Z_2)$。

固定首一标量多项式 $q$，次数 $p\ge2$。
设
$$
L_n(v)=\left.\frac{d^n}{ds^n}
\log(\cosh s+v\sinh s)\right|_{s=0},\qquad
G_n=\sum_ja_j^nL_n(R_j)\in\mathcal A,
$$
$$
\mathcal P(z;\kappa)=
\exp\left(\sum_{n=2}^p\frac{\kappa_n}{n!}\partial_z^n\right)q(z),
\qquad T=\mathcal P(X;G)\in\mathcal A.
\tag{1.3}
$$
指数在次数不超过 $p$ 的多项式空间上是有限和。
所有算子和自然幂均全域有界。
R176 给完整 $C$ 自伴性及实际循环像公式。

**定理。**
$$
\boxed{
\ker T=0,\qquad q(u)e^w\text{ 对实际 }A\text{ 循环}.
}
\tag{1.4}
$$
根的重数任意。
非零常数和一次多项式由既有 R16/R147 处理。
下面所有常数均可依赖固定的行、指数权、$\alpha,\beta_\pm,p,q$，
但不得依赖高位集合的最大物理位。

## 2. 原正锥主控与标量伸展指数乘积

原模型满足
$$
N_j^2=\eta_jN_{j+1},\qquad
\|N_j\|=1,\qquad
0<\eta_j\le\bar\eta_j=e^{-770\,16^j}.
\tag{2.1}
$$
$A$ 和 $N_j$ 保持逐点函数非负锥；
以下的正性不是 Hilbert 自伴正性。

写
$$
L_n(1+x)=\sum_{\ell=1}^nc_{n,\ell}x^\ell,\qquad
W_n(z)=\sum_{\ell=1}^n|c_{n,\ell}|
       \left(\frac{2Lz}{1-Lz}\right)^\ell
       =zW_{n,1}(z)=w_{n,1}z+z^2W_{n,2}(z).
\tag{2.2}
$$
$W_n(0)=0$，全部 Taylor 系数非负。
实际准幂零演算与高位
$$
(I-LN_j)^{-1}=(I+LN_j)(I-L^2\eta_jN_{j+1})^{-1}
$$
给
$$
\sup_j\|W_{n,1}(N_j)\|<\infty,\qquad
\sup_j\|W_{n,2}(N_j)\|<\infty.
\tag{2.3}
$$
有限低位分别使用实际预解式后取最大值。

定义范数收敛的实际正主控
$$
M_n=\sum_j|a_j|^nW_n(N_j).
$$
由 $R_j-I=-2t_jN_j(I+t_jN_j)^{-1}$ 的绝对范数收敛级数，
$$
|G_n^kf|\le M_n^k|f|,\qquad \|G_n^k\|\le\|M_n^k\|.
\tag{2.4}
$$
逐次使用的是函数非负锥保持性。

偶、奇幂与 (2.1) 给
$\|e^{zN_j}\|\le(1+|z|)e^{|z|\sqrt{\eta_j}}$。
因此对 $v\ge0$、$t=|z|$，
$$
\|e^{zvW_n(N_j)}\|
\le(1+w_{n,1}tv)\exp(C_ntv\sqrt{\eta_j}).
\tag{2.5}
$$
这是实际完整进位估计。

记
$$
\gamma=1+\frac1\alpha\ge2.
$$
对任意固定 $\lambda>0$、$A\ge0$，
$$
\boxed{
\sum_{k\ge1}\log(1+A e^{-\lambda k^\alpha})
\le C_{\alpha,\lambda}
 \big(1+[\log(2+A)]^\gamma\big).
}
\tag{2.6}
$$
为证明它，设 $U=\log(2+A)$，
$m=\max(1,\lceil(2U/\lambda)^{1/\alpha}\rceil)$。
前 $m$ 项之和至多
$m\log(1+A)\le C(1+U^\gamma)$。
对 $k>m$，有
$A e^{-\lambda k^\alpha}\le e^{-\lambda k^\alpha/2}$，
再用 $\log(1+x)\le x$ 和收敛级数
$\sum_ke^{-\lambda k^\alpha/2}$ 即得。
这一步只处理非负标量数列，不实施 Hilbert 空间坐标置换。

## 3. 全部物理进位下的对数指数增长

给定 $t\ge0$，按原物理位选最小整数 $h(t)\ge1$，使
$$
385\,16^h\ge2\log(2+t).
\tag{3.1}
$$
将 $M_n$ 分成原物理头和尾，两部分在 $\mathcal A$ 中交换。
对尾部先取有限乘积，再由范数连续性取极限，
用 (2.5)、排序上界及 (2.6)：
$$
\begin{aligned}
\sum_{j\ge h}\log(1+w_{n,1}t|a_j|^n)
&\le\sum_{k\ge1}
 \log(1+w_{n,1}B^nt e^{-n\beta_-k^\alpha})\\
&\le C_n\big(1+[\log(2+t)]^\gamma\big).
\end{aligned}
\tag{3.2}
$$
物理尾进位不排序，直接估计
$$
\sum_{j\ge h}|a_j|^n\sqrt{\eta_j}
\le2B^n e^{-385\,16^h}\le2B^n(2+t)^{-2}.
\tag{3.3}
$$
故尾指数有
$K_n\exp(C_n[\log(2+t)]^\gamma)$ 界。

有限物理头仍有明确的实际因子
$$
M_{n,<h}=A U_{n,h},\qquad
U_{n,h}=\sum_{j<h}|a_j|^n d_j^{-1}
 A^{2^j-1}W_{n,1}(N_j).
\tag{3.4}
$$
由
$$
d_j^{-1}\le e^{125\,16^j},\qquad
\sum_j|a_j|^n\le B^n\sum_{k\ge1}e^{-n\beta_-k^\alpha}<\infty,
$$
得到 $\|U_{n,h}\|\le C_ne^{125\,16^{h-1}}$。
(3.1) 的最小性给
$$
\log(2+t\|U_{n,h}\|)\le C_n+2\log(2+t).
\tag{3.5}
$$
R109 的真实四次幂界蕴含固定 $K_A,c_A>0$ 下
$\|A^k\|\le K_Ae^{-c_Ak^4}$。
因此
$$
\|e^{zAU_{n,h}}\|
\le K_A\sum_{k\ge0}e^{-c_Ak^4}
       \frac{(t\|U_{n,h}\|)^k}{k!}
\le K_n\exp(C_n(1+\log(2+t))^{4/3}).
\tag{3.6}
$$
最后一步来自
$-c_Ak^4+k\ell\le-c_Ak^4/2+C_A\ell^{4/3}$，
$\ell=\log(2+t\|U_{n,h}\|)$。
因为 $\gamma\ge2>4/3$，
该低头成本可吸入 (3.2) 的对数幂。
于是
$$
\boxed{
\|e^{zM_n}\|\le K_n
 \exp\big(C_n[\log(2+|z|)]^\gamma\big)
\qquad(z\in\mathbb C).
}
\tag{3.7}
$$
所有低头常数对参数的增长都已由 (3.4)--(3.6) 支付；
没有只固定一个物理截断后忽略其随参数增长。

## 4. 超阶乘幂界、实际 Neumann 级数与联合小圈

对 (3.7) 作 Cauchy 系数估计。
取半径 $R=e^{\lambda k^\alpha}$，其中固定 $\lambda>0$ 稍后选小。
由
$$
\log(2+R)\le\log3+\lambda k^\alpha,\qquad
(\log3+\lambda k^\alpha)^\gamma
\le2^{\gamma-1}\big((\log3)^\gamma+
                 \lambda^\gamma k^{1+\alpha}\big),
$$
得到
$$
\|M_n^k\|
\le K_n' k!
 \exp\big((C_n'\lambda^\gamma-\lambda)k^{1+\alpha}\big).
$$
选 $\lambda$ 使 $C_n'\lambda^{\gamma-1}\le1/2$。
由于
$\log(k!)\le k\log(k+1)=o(k^{1+\alpha})$，
再缩小负系数并吸收有限个 $k$，有
$$
\boxed{
\|G_n^k\|\le\|M_n^k\|
\le K_n''e^{-d_n k^{1+\alpha}}\qquad(k\ge0)
}
\tag{4.1}
$$
对某个固定 $d_n>0$ 成立。
这里的 $k!$ 已实际支付，不只是把它写入一个未控制的误差项。

对所有 $z\ne0$，
$\sum_{k\ge0}z^{-k-1}G_n^k$ 按范数绝对收敛，
左右乘 $z-G_n$ 都等于 $I$。
令 $\ell=\log^+(1/|z|)$。
实变量优化给
$$
-d_n k^{1+\alpha}+k\ell
\le-\frac{d_n}{2}k^{1+\alpha}+C_n\ell^\gamma.
$$
求和收敛的第一项，得到真正的全域预解界
$$
\boxed{
\|(z-G_n)^{-1}\|
\le\frac{\widetilde K_n}{|z|}
 \exp\big(\widetilde C_n[\log^+(1/|z|)]^\gamma\big).
}
\tag{4.2}
$$
特别，每个实际 $G_n$ 的谱都是 $\{0\}$。

固定 $\varepsilon>0$。
若 $0<\delta\le1$，而 $F$ 在
$|\kappa_n|\le\varepsilon\delta^n$ 的邻域全纯，
边界多圆周上 $|F|\le M_F$，
共同的实际多圆周 Cauchy 演算和 (4.2) 给
$$
\boxed{
\|F(G)\|\le K M_F
 \exp\big(C_\varepsilon[1+\log(1/\delta)]^\gamma\big).
}
\tag{4.3}
$$
圆周长度逐个消去 $|z_n|^{-1}$；
有限个
$\log^+(1/(\varepsilon\delta^n))$
都被常数乘 $1+\log(1/\delta)$ 控制。
$K,C_\varepsilon$ 与 $F,\delta$ 无关。
整个逆系数一次共同求值，只支付一次 (4.3)。

## 5. 不同幅度的高位选择：保留线性数量的位

沿 (1.1) 的子序列 $N$，
从幅度最大的 $N$ 个实际指标中，
删去排序最前 $\lfloor N/4\rfloor$ 项，
再删去物理位 $j<\lfloor N/4\rfloor$ 的项。
至少剩 $N/2$ 项。
任取其中
$$
Q_N=\lfloor N/4\rfloor
$$
项，组成 $I_N$。
令
$$
h_N=\lfloor N/4\rfloor,\qquad
\delta_N=c_0e^{-\beta_+N^\alpha},\qquad
u_N=B e^{-\beta_-(N/4)^\alpha}.
$$
准确有
$$
\boxed{
\min I_N\ge h_N,\qquad
\delta_N\le|a_j|\le u_N\quad(j\in I_N),\qquad
u_N\longrightarrow0.
}
\tag{5.1}
$$
$\max I_N$ 无上界。
没有为了同幅度而把 $Q_N$ 缩减到次线性规模。

固定 $c>0$，在临界 $\alpha=1$ 时稍后选小；
在 $0<\alpha<1$ 时可直接取 $c=1$。
定义
$$
r=r_N=\left\lfloor\sqrt{Q_N/c}\right\rfloor.
\tag{5.2}
$$
则
$$
Q_N/r^2\to c,\qquad N/r^2\to4c,\qquad
r u_N\to0.
\tag{5.3}
$$
充分大 $N$ 时 $r\le Q_N$。
下面 $F\subset I_N$、$|F|=r$。
同一个 $F$ 内的幅度比例可以趋于无穷；
下一节明确支付这一变化。

## 6. 不需同幅带的保重数 Bézout 余式

精确 Bell 有限差恒等式仍为
$$
\mathscr L_a(z;\kappa)
=4a\partial_z\mathcal P+
 \sum_{n=2}^p4L_n'(1)a^n\partial_{\kappa_n}\mathcal P
=-2[\mathcal P(z-2a;\kappa)-\mathcal P(z;\kappa)].
\tag{6.1}
$$
其中使用
$4L_n'(1)=-2(-2)^n$、
$\partial_{\kappa_n}\mathcal P=\partial_z^n\mathcal P/n!$。

令 $q$ 的不同根为 $\lambda_\nu$、重数为 $\mu_\nu$。
存在固定 $\varepsilon,\delta_0>0$，
使 $|\kappa_n|\le2\varepsilon\delta^n$、
$0<\delta\le\delta_0$ 时，
$\mathcal P$ 的每个根团都在
$|z-\lambda_\nu|<\delta/4$ 中，保留重数 $\mu_\nu$；
在圆周 $\Gamma_\nu$ 上有
$|\mathcal P|\ge c_q\delta^{\mu_\nu}$。
证明由 Bell 权重系数
$|\beta_k(\kappa)|\le C_q\varepsilon\delta^k$
和 Rouché 给出：每项
$\beta_kq^{(k)}$ 在该圆周都是
$O(\varepsilon\delta^{\mu_\nu})$。

选一个固定 $a_0>0$，使 $2a_0$ 小于不同标量根之间最小距离的四分之一；
若只有一个不同根，则任取充分小的 $a_0$。
现只假设
$$
\delta\le|a_j|\le a_0.
\tag{6.2}
$$
对 $|z-\lambda_\nu|\le\delta/4$，
$z-2a_j$ 与同团任一根的距离至少
$$
2|a_j|-\delta/2\ge3|a_j|/2\ge3\delta/2.
$$
与其它团的距离则有固定正下界。
所以
$$
\boxed{
|\mathcal P(z-2a_j;\kappa)|
\ge c_q|a_j|^{\mu_\nu}
\ge c_q\delta^{\mu_\nu}
\ge c_q\delta^p.
}
\tag{6.3}
$$
不需要 $|a_j|\le2\delta$，也不要求任何共同相位。
由 (5.1)，(6.2) 对全部所选位最终成立。

定义
$$
H_F(z;\kappa)=\prod_{j\in F}[-2\mathcal P(z-2a_j;\kappa)],
\qquad h_F=H_F^{-1}
$$
于根团圆盘的邻域，并置
$$
\mathcal R_F(z;\kappa)=
\frac1{2\pi i}\sum_\nu\int_{\Gamma_\nu}
h_F(\zeta;\kappa)
\frac{\mathcal P(\zeta;\kappa)-\mathcal P(z;\kappa)}
 {(\zeta-z)\mathcal P(\zeta;\kappa)}\,d\zeta.
\tag{6.4}
$$
它对 $z$ 的次数小于 $p$，系数在闭多圆盘
$|\kappa_n|\le\varepsilon\delta^n$ 的邻域全纯，并满足
$$
|[z^k]\mathcal R_F|\le C_q^{r+1}\delta^{-pr-p+1}.
\tag{6.5}
$$
常数与 $u_N/\delta_N$ 无关：
分母只使用 (6.3) 的下界，
而差商的系数只依赖固定 $q$、有界根团和小 $\kappa$。

Cauchy 公式使 $h_F-\mathcal R_F$ 被 $\mathcal P$
局部全纯整除，因而保留全部根的全部重数。
在解析系数多项式环中，
$$
\boxed{
\mathcal R_F\prod_{j\in F}\mathscr L_{a_j}
=1+\mathcal P\,\mathcal S_F.
}
\tag{6.6}
$$
商的系数由首一多项式除法保持全纯。
没有用简单根逼近或只在根值上插值。

以 $\delta=\delta_N$，
对整个余式系数一次使用 (4.3)，在实际有界 $X$ 上求值：
$$
\mathfrak R_F=\mathcal R_F(X;G)\in\mathcal A.
$$
若 $M=\ker T$，则 $\mathfrak R_FM\subset M$，并且
$$
L_F\mathfrak R_Ff=f\quad(f\in M),\qquad
L_F=\prod_{j\in F}\mathscr L_{a_j}(X;G).
\tag{6.7}
$$
因为
$1+\log(1/\delta_N)\le C N^\alpha$、
$\alpha\gamma=1+\alpha$，
存在不依赖 $c,N,F$ 的固定 $K$，使
$$
\boxed{
\|\mathfrak R_F\|
\le\exp\big(KN^{1+\alpha}+KrN^\alpha+Kr+K\big).
}
\tag{6.8}
$$
$c$ 只通过 $r$ 出现，常数 $K$ 在选小 $c$ 之前已经固定。

## 7. 实际有界反射幂与不同幅度下的 Boolean 主项

令
$\mathsf J_F=\prod_{j\in F}M_{\chi_j}$、
$\gamma_F(B)=\mathsf J_FB\mathsf J_F$。
R260 的任意跨度真实壳在导数阶数零给
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
该界不含最大物理位。
同时
$$
\|\widehat X_F-X\|\le Cr u_N\to0,\qquad
\|\widehat G_{n,F}-G_n\|\le C_nr u_N^n\to0.
$$

设
$$
\widehat T_F=\mathcal P(\widehat X_F;\widehat G_F),\quad
A_F=\widehat T_F-T,\quad E_F=\gamma_F(T)-\widehat T_F.
$$
有限有界多项式的逐因子差给 $\|E_F\|\le C\epsilon_N$；
$T,\widehat T_F,A_F$ 交换，但不假定 $E_F$ 与它们交换。
若 $f_F=\mathfrak R_F f$、$v_F=\mathsf J_Ff_F$、$f\in M$，
则 $\gamma_F(T)v_F=0$。
真实非交换幂差给
$$
\|\widehat T_F^k v_F\|\le C\epsilon_N k C_T^{k-1}\|f_F\|.
$$
再用 $T=\widehat T_F-A_F$ 的交换二项式，
$$
\|T^rv_F-(-A_F)^rv_F\|
\le C\epsilon_N r(2C_T)^{r-1}\|f_F\|.
\tag{7.2}
$$
$C_T$ 只控制固定有界变量，不涉及任何初段最大位范数。

真实平方关系允许写
$$
\widetilde A_F=
\mathcal P\left(
X+4\sum_{j\in F}a_jt_jN_j;\
G_n+4L_n'(1)\sum_{j\in F}a_j^nt_jN_j
\right)-\mathcal P(X;G),
$$
$$
\|A_F-\widetilde A_F\|\le C\bar\eta_{h_N}.
\tag{7.3}
$$
有理式的余项明确含 $N_j^2$；
其系数绝对和由 $\sum_F|a_j|\le r u_N\to0$ 控制。
这一步同样不需要幅度彼此可比。

在形式变量 $x_j$ 中，$\widetilde A_F$ 无常数项，
一次部分为
$\sum_{j\in F}t_jx_j\mathscr L_{a_j}(X;G)$。
系数环允许包含原实际 $N_j$，不假定代数独立。
$r$ 个正次因子、$r$ 个选中变量给
$$
\widetilde A_F^r\equiv r!t_FN_FL_F
\pmod{(N_j^2:j\in F)},\qquad
t_F=\prod_{j\in F}t_j,\quad N_F=\prod_{j\in F}N_j.
\tag{7.4}
$$
每个弃项真含重复位，实际范数多出 $\bar\eta_{h_N}$；
总系数范数至多 $C^r$。
所以
$$
\|A_F^r-r!t_FN_FL_F\|
\le\bar\eta_{h_N}e^{Cr\log(r+2)}.
\tag{7.5}
$$

令 $\widehat L_F$ 是 $L_F$ 的交换反射替身。
由 (7.1) 逐因子相减，
$\|\gamma_F(L_F)-\widehat L_F\|\le\epsilon_N rC^r$。
$\widehat L_F-L_F$ 的每个项含选中 $N_j$，
左乘 $N_F$ 后含真正重复位，故
$\|N_F(\widehat L_F-L_F)\|\le\bar\eta_{h_N}C^r$。
使用准确恒等式
$$
L_F\mathsf J_F-\mathsf J_FL_F
=(L_F-\gamma_F(L_F))\mathsf J_F
$$
而非假定交换，全部移动成本乘上 $r!t_F$ 后
仍不超过 $\epsilon_Ne^{Cr\log(r+2)}$。

最后由 (6.7) 消去 $L_Ff_F$，得到
$$
\boxed{
\|T^r\mathsf J_F\mathfrak R_Ff
-(-1)^rr!t_FN_F\mathsf J_Ff\|
\le\epsilon_Ne^{Cr\log(r+2)}
 \|\mathfrak R_F\|\,\|f\|\qquad(f\in M).
}
\tag{7.6}
$$
这是全部实际算子的全域有界证明；
没有遗留形式乘积域或未定义的非交换函数演算。

## 8. 对称平均及非零弱极限

置
$$
\mathcal V_N=
(-1)^r\left(\frac2{Q_N}\right)^r
\sum_{\substack{F\subset I_N\\|F|=r}}
 t_F^{-1}\mathsf J_F\mathfrak R_F.
$$
其范数满足
$$
\|\mathcal V_N\|\le A_N:=
\frac{(2L)^r}{r!}\sup_F\|\mathfrak R_F\|
\le\exp\big(KN^{1+\alpha}+KrN^\alpha+Kr+K\big).
\tag{8.1}
$$

实际 $\|N_j-E_j\|\le\bar\eta_j$、
$E_j^2=0$、
$E_j\mathsf J_j=E_j$ 给
$\|N_F\mathsf J_F-\prod_FE_j\|\le r\bar\eta_{h_N}$。
所以 (7.6) 求和后
$$
\boxed{
\|T^r\mathcal V_Nf-C_{I_N}^rf\|\to0,\qquad
C_{I_N}=\frac2{Q_N}\sum_{j\in I_N}E_j,\quad f\in M.
}
\tag{8.2}
$$
总误差可用固定常数乘
$$
\epsilon_N
 \exp\big(KN^{1+\alpha}+KrN^\alpha+Kr+Cr\log(r+2)+K\big)
+2^rr\bar\eta_{h_N}
$$
控制，由 $h_N\asymp N$ 的真实超快进位衰减而趋零。

已知有限局部矩阵的占据数分层给
$\|C_{I_N}^r\|\le(1+1/Q_N)^r\to1$。
对固定有限柱 $v,z$，当所选位都高于其支撑时，
$$
\langle C_{I_N}^rv,z\rangle
=\frac{(Q_N)_r}{Q_N^r}\langle v,z\rangle
\longrightarrow e^{-1/(2c)}\langle v,z\rangle.
$$
由一致范数界，
$$
\boxed{
C_{I_N}^r\rightharpoonup\alpha_c I,\quad
T^r\mathcal V_Nf\rightharpoonup\alpha_c f\ (f\in M),\qquad
\alpha_c=e^{-1/(2c)}>0.
}
\tag{8.3}
$$
无需未知核向量的任何物理尾速率。

## 9. 真正的局部 A 因子与临界几何端点

固定任意有限局部矩阵 $D$，支撑小于物理位 $h$。
令
$$
Z_h=X-a_*I-\sum_{j<h}a_jR_j,\qquad
s_h=a_*+\sum_{j<h}a_j,\qquad
G_{n,\ge h}=\sum_{j\ge h}a_j^nL_n(R_j).
$$
这些是范数收敛的真实尾，$D$ 与它们全部交换。
有限低头差明确被 $A$ 整除：
$$
X-(Z_h+s_h)=A U_{1,h},\qquad
G_n-G_{n,\ge h}=A U_{n,h},
$$
$$
U_{1,h}=-2\sum_{j<h}\frac{a_jt_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-1},
$$
$$
U_{n,h}=-2\sum_{j<h}\frac{a_j^nt_j}{d_j}
 A^{2^j-1}(I+t_jN_j)^{-1}\widetilde L_n(R_j),
\quad L_n(v)=(v-1)\widetilde L_n(v).
\tag{9.1}
$$
所有 $U_{n,h}\in\mathcal A$ 真正有界，$h$ 固定。

因此有限多项式相减给
$$
T=T_{\rm tail}+A U_h,\qquad
T_{\rm tail}=\mathcal P(Z_h+s_h;G_{\ge h}),\qquad U_h\in\mathcal A.
$$
$T_{\rm tail}$ 与 $D$、$A U_h$ 都交换，故
$$
\operatorname{ad}_T^rD
=\sum_{s=0}^r(-1)^s\binom rs
 (A U_h)^{r-s}D(A U_h)^s.
\tag{9.2}
$$
每项真含左右合计 $r$ 个 $A$，
没有将 $A$ 移过未知局部矩阵。

由 R109，
$$
\|A^{r-s}\|\,\|A^s\|
\le e^{-(5/6)r^4+105r^3}.
$$
所以
$$
\|(\operatorname{ad}_T^rD)\mathcal V_Nf\|
\le\|D\|\,[2\|U_h\|]^r A_N
 e^{-(5/6)r^4+105r^3}\|f\|.
\tag{9.3}
$$
$U_h=0$ 的情形直接为零。
其对数主预算是
$$
-\frac56r^4+105r^3+KN^{1+\alpha}
+KrN^\alpha+O(r+1).
\tag{9.4}
$$

若 $0<\alpha<1$，取 $c=1$，
则 $r^4\asymp N^2$，其它项都是 $o(N^2)$，
所以 (9.3) 趋零。

若 $\alpha=1$，先固定 (6.8)、(8.1) 的常数 $K$，
再选择
$$
\boxed{
0<c<\min\left(1,\frac14\sqrt{\frac5{48K}}\right).
}
\tag{9.5}
$$
由 $N/r^2\to4c$，
$$
\frac{KN^2}{r^4}\longrightarrow16Kc^2<\frac5{48}.
$$
其余 $r^3,rN,r$ 项都为 $o(r^4)$，
所以负的 $-(5/6)r^4$ 仍有固定余量。
这支付了几何衰减端点，没有把临界情形误当作严格小阶。
$\alpha_c=e^{-1/(2c)}$ 虽可能很小，但固定且非零。

## 10. 完整配对、排核与循环性

令 $B(f,g)=\langle f,Cg\rangle$。
$T$ 全域有界且完整 $C$ 自伴。
对 $f,g\in M=\ker T$，
Leibniz 展开中所有左侧含正次 $T$ 的项
与 $g$ 配对为零，准确有
$$
B(DT^r\mathcal V_Nf,g)
=(-1)^rB((\operatorname{ad}_T^rD)\mathcal V_Nf,g).
\tag{10.1}
$$
右侧由 §9 趋零，左侧由 (8.2)--(8.3)
趋于 $\alpha_c B(Df,g)$。
故
$$
B(Df,g)=0\qquad(f,g\in M,\ D\text{ 任意固定有限局部矩阵}).
$$
原 Haar 局部全矩阵 $*$-代数不可约。
若 $0\ne f\in M$，其局部轨道稠密；
取 $g=f$ 就迫 $Cf=0$，矛盾。
所以 $\ker T=0$。

R176 的真实 $\xi_w=e^w$ 循环，且
$$
T\xi_w=q(u)e^w,\qquad
[q(u)e^w]_A=\overline{\operatorname{Ran}T}.
$$
由 $T^*=CTC$，
$\ker T^*=C\ker T=0$，因此 $T$ 像稠密。
这证明 (1.4)，包括全部混合重根。

## 11. 已关闭的准确范围与剩余接口

本稿对 (1.1) 的所有原物理排列和复相位有效。
特别，$\rho_k$ 与 $e^{-\beta k^\alpha}$ 可比时，
所有 $0<\alpha\le1$ 的
$q(u)e^w$ 都循环，无论 $q$ 有怎样的有限根重数。
事实上允许上下两个不同的固定指数常数，
且下界只需沿子序列。

本稿的新要点有两个。
一是保重数 Bézout 只需最小幅度 $\delta_N$ 和最大幅度趋零，
因此高位集合可以保留 $Q_N\asymp N$；
不能强加同幅桶后损失这一规模。
二是真实正锥给联合小圈的对数预解成本
$O((\log(1/\delta_N))^{1+1/\alpha})=O(N^{1+\alpha})$，
使全部重数的逆输入在 $\alpha\le1$ 仍能由局部四次幂预算吸收。

本稿没有证明 $\alpha>1$ 的全部重数。
现有解析分支或简单根结论即使覆盖更大的 $\alpha$ 区间，
也不能免费通过本稿的 Bézout 输入预算推广。
对 $\alpha>1$，(9.4) 中 $N^{1+\alpha}$ 超过 $N^2$，
上述固定弱平均尺度不再关闭估计。

也没有覆盖任意衰减形状的全部同字符行，
更没有解决多模式多项式、一般有限 chaos、
正常湮灭者、边界 $N=M$ 或普通 Hilbert ISP。
