# R266：任意重排指数幅度行的全部重数循环性与对数型联合预解预算

日期：2026-11-13（UTC）。作者：kernel。
状态：已证明；root和boundary已全文核验；这是原 Haar 模型的中间结论，普通 Hilbert ISP 未完成。

本文接 R236 的保重数 Hermite 余式、R260 的真实任意跨度壳、R264 的平方窗口弱平均。新增范围是 little-weak-$\ell^1$ 中任意物理排列的指数及伸缩指数幅度行；新增估计是实际累积量的对数型整增长与联合预解成本。临界弱 $\ell^1$ 的全重数已由 R236 的独立附录覆盖，不在本文重复登记。

## 1. 定理与原算子不变

令
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a_*\in\mathbb C,
$$
并设非零幅度的非增重排 $\rho_k$ 满足：存在固定
$$
0<\alpha\le1,\qquad c,C,\beta_-,\beta_+>0
$$
使充分大 $k$ 有
$$
\boxed{
c e^{-\beta_+k^\alpha}\le\rho_k\le
C e^{-\beta_-k^\alpha}.
}
\tag{1.1}
$$
增大 $C$、缩小 $c$ 后可令所有 $k\ge1$ 成立。允许上下指数率不同、任意复相位、任意物理排列及任意多个零系数。

固定任意复 first 指数权
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2(\mathbb C).
$$

**定理（已证明）。** 对每个非零标量多项式 $q$，
$$
\boxed{q(u)e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.2}
$$
$q$ 的根允许任意有限重数。特别包括任意重排的几何幅度和 $e^{-\beta k^\alpha}$、$0<\alpha<1$ 的全部重根。

(1.1) 给 $a\in\ell^1$。下面的 first 和 Bell 多项式因此都是全域有界算子；这项实际性质允许简化高阶词域，不需要借用未经证明的闭自然幂等式。所有排序只用于标量估计和挑选有限实际位，不实施一个把排序变成原算子交织的坐标置换，也不改动 $a_*$。

## 2. 实际模型与有界 Bell 多项式

保留 R109/R176 的原模型
$$
Af(y)=w_0(y)f(y-1),\qquad w_0\ge0,\qquad \|A\|=e^{-20},
$$
$$
N_j=A^{2^j}/d_j,\quad \|N_j\|=1,\quad
N_j^2=\eta_jN_{j+1},\quad
0<\eta_j\le e^{-770\,16^j},
$$
$$
d_j=e^{-\Lambda_j},\qquad
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j
\le125\,16^j.
\tag{2.1}
$$
原四次幂界为
$$
\|A^k\|\le
\exp\!\left[-\frac{100}{15}k^4+105k^3\right].
\tag{2.2}
$$
特别存在固定 $K_A,c_A>0$ 使 $\|A^k\|\le K_Ae^{-c_Ak^4}$。

置
$$
t_j=e^{-2b_j},\quad
R_j=V(t_jN_j),\quad V(z)=(I-z)(I+z)^{-1},
$$
$$
X=a_*I+\sum_ja_jR_j,\qquad
G_n=\sum_ja_j^nL_n(R_j),\quad n\ge2,
$$
$$
L_n(v)=
\left.\frac{d^n}{ds^n}\log(\cosh s+v\sinh s)\right|_{s=0}.
\tag{2.3}
$$
固定 $b$ 时，$\sup_j\|(I\pm t_jN_j)^{-1}\|<\infty$。
大 $j$ 用实际平方关系和
$(I\pm tN)^{-1}=(I\mp tN)(I-t^2N^2)^{-1}$；
有限个小 $j$ 用各自真正的准幂零预解式。故 $R_j$ 一致有界。
因为 $a\in\ell^1$，(2.3) 中全部和在算子范数绝对收敛，属于同一个交换代数 $\mathcal A$。

非零常数 $q$ 的结论已由 $e^w$ 的循环性得到。下面将 $q$ 除以首系数，设它首一、次数 $p\ge1$，并定义
$$
\mathcal P(z;\kappa)
=\exp\!\left(\sum_{n=2}^p
\frac{\kappa_n}{n!}\partial_z^n\right)q(z),\qquad
T=\mathcal P(X;G_2,\ldots,G_p).
\tag{2.4}
$$
指数在有限维多项式空间上是有限和；$p=1$ 时取空元组。
$T\in\mathcal A$ 有界，并且对原固定共轭 $C_0$ 有
$$
T=C_0T^*C_0,\qquad T e^w=q(u)e^w.
\tag{2.5}
$$
这是 R176 的真实加权 Bell 恒等式在 $a\in\ell^1$ 时的全域形式。
令 $M=\ker T$。全部 $\mathcal A$ 元素保持 $M$。

## 3. 保留全部 carry 的对数型整增长

记
$$
\gamma=1+\frac1\alpha\ge2.
$$

**引理。** 对每个固定 $n\ge2$，存在 $K_n,C_n>0$ 使
$$
\boxed{
\|e^{zG_n}\|
\le K_n\exp\!\left[
C_n(1+\log(2+|z|))^\gamma
\right]\quad(z\in\mathbb C).
}
\tag{3.1}
$$
常数不依赖系数的物理位置；更准确地说，证明只用固定上界 (1.1)、固定 $b$ 和原模型。

### 3.1 实际函数非负锥的主控

令 $L=\max(1,\sup_j|t_j|)$，并写
$$
L_n(1+x)=\sum_{\ell=1}^n c_{n,\ell}x^\ell,\qquad
W_n(z)=\sum_{\ell=1}^n|c_{n,\ell}|
\left(\frac{2Lz}{1-Lz}\right)^\ell.
$$
$W_n$ 的 Taylor 系数非负且 $W_n(0)=0$。
$A,N_j$ 保持原 $L^2$ 函数的逐点非负锥，这不是 Hilbert 自伴正性。
R236 分阶预算的准确有理式给
$$
|L_n(R_j)f|\le W_n(N_j)|f|.
$$
令
$$
M_n=\sum_j|a_j|^nW_n(N_j).
$$
其和按范数收敛，并有
$$
|G_n^kf|\le M_n^k|f|,\qquad
|e^{zG_n}f|\le e^{|z|M_n}|f|.
\tag{3.2}
$$

为明确统一逆的预算，实际平方关系给
$\sup_j\|(I-LN_j)^{-1}\|<\infty$，有限低位照 §2 单独支付。
若
$$
W_n(z)=zW_{n,1}(z)=w_{n,1}z+z^2W_{n,2}(z),
$$
则
$$
B_{n,i}:=\sup_j\|W_{n,i}(N_j)\|<\infty,\quad i=1,2.
$$
由偶奇幂分拆，
$$
\|e^{\zeta N_j}\|
\le(1+|\zeta|)e^{|\zeta|\sqrt{\eta_j}}.
$$
故对 $v\ge0$、$t=|z|$，
$$
\boxed{
\|e^{zvW_n(N_j)}\|
\le(1+w_{n,1}tv)
\exp(C_n^{(0)}tv\sqrt{\eta_j}).
}
\tag{3.3}
$$

### 3.2 排序只发生在标量乘积内

由 (1.1)，对 $t\ge0$，
$$
\sum_j\log(1+w_{n,1}t|a_j|^n)
\le\sum_{k\ge1}
\log(1+D_nt e^{-n\beta_-k^\alpha})
\le C_n^{(1)}(1+\log(2+t))^\gamma.
\tag{3.4}
$$
最后一步可直接积分验证。
递减性使求和不超过从零开始的积分；置
$v=n\beta_-x^\alpha$ 后，积分是固定常数乘
$$
\int_0^\infty
\log(1+D_nt e^{-v})v^{1/\alpha-1}\,dv.
$$
令 $\ell=\log(2+D_nt)$。在 $v\le2\ell$ 上用
$\log(1+D_nt e^{-v})\le\ell$，得 $C\ell^{1+1/\alpha}$；
在 $v\ge2\ell$ 上用 $D_nt e^{-v}\le e^{\ell-v}$，
剩余积分被固定常数乘
$e^{-\ell}(1+\ell^{1/\alpha-1})$ 控制。
这证明 (3.4)。

### 3.3 随参数选实际物理头

取最小整数 $h\ge1$ 使
$$
385\,16^h\ge2\log(2+t).
\tag{3.5}
$$
对实际尾 $M_{n,\ge h}$，各项交换，先用 (3.3) 对有限乘积估计，再取范数极限。
进位因子满足
$$
t\sum_{j\ge h}|a_j|^n\sqrt{\eta_j}
\le 2t(\sup_j|a_j|)^n e^{-385\,16^h}\le C_n.
$$
纯标量乘积由 (3.4) 控制。因此
$$
\|e^{zM_{n,\ge h}}\|
\le K\exp[C(1+\log(2+t))^\gamma].
\tag{3.6}
$$

有限物理头具有真实因子
$$
M_{n,<h}=A U_{n,h},\qquad
U_{n,h}=\sum_{j<h}
|a_j|^n d_j^{-1}A^{2^j-1}W_{n,1}(N_j)\in\mathcal A.
$$
由于 $\sum_j|a_j|^n<\infty$，
$$
\|U_{n,h}\|\le C_n e^{125\,16^{h-1}}.
$$
(3.5) 的最小性给
$16^{h-1}\le1+(2/385)\log(2+t)$，从而
$$
\log(2+t\|U_{n,h}\|)\le C_n+2\log(2+t).
$$
原 (2.2) 及 $A$ 与 $U_{n,h}$ 的交换性给
$$
\|e^{zAU_{n,h}}\|
\le K_A\sum_{k\ge0}
e^{-c_Ak^4}\frac{(t\|U_{n,h}\|)^k}{k!}
\le K\exp[C(1+\log(2+t))^{4/3}].
\tag{3.7}
$$
最后一步用
$-c_Ak^4+k\ell\le-(c_A/2)k^4+C_A\ell^{4/3}$ 后求和。
$\gamma\ge2$ 吸收 (3.7)。
头尾交换，结合 (3.2)、(3.6) 即证 (3.1)。
有限低头与高尾真实 carry 均已支付，没有把 $M_n$ 换成纯平方零和。

## 4. 全方向实际预解与一次联合求值

(3.1) 的对数增长小于任何正线性增长。
对 $\lambda\ne0$ 定义真正的 Bochner 积分
$$
J_\lambda=\int_0^\infty e^{-s}e^{sG_n/\lambda}\,ds.
$$
它按算子范数绝对收敛。
对积分前的有界算子指数求导并在有限区间积分，再令端点趋无穷，
边界项 $e^{-s}e^{sG_n/\lambda}\to0$，得到
$$
(I-G_n/\lambda)J_\lambda
=J_\lambda(I-G_n/\lambda)=I.
$$
所以 $J_\lambda=\lambda(\lambda-G_n)^{-1}$；这不是只在大 $\lambda$ 区域成立的形式级数。

置 $\ell_\lambda=1+\log^+|\lambda|^{-1}$。
有
$$
1+\log(2+s/|\lambda|)
\le\ell_\lambda+\log(2+s).
$$
用 $(x+y)^\gamma\le2^{\gamma-1}(x^\gamma+y^\gamma)$ 得
$$
\|J_\lambda\|
\le K e^{C'\ell_\lambda^\gamma}
\int_0^\infty
e^{-s+C'(\log(2+s))^\gamma}\,ds.
$$
最后的积分是固定有限数。因此
$$
\boxed{
\|\lambda(\lambda-G_n)^{-1}\|
\le K_n'\exp[C_n'(1+\log^+|\lambda|^{-1})^\gamma].
}
\tag{4.1}
$$
此式也给各 $G_n$ 的谱为 $\{0\}$，且所有复方向统一。

固定 $p,\varepsilon>0$，令 $0<\delta\le1$。
若 $F$ 在闭多圆盘
$|\kappa_n|\le\varepsilon\delta^n$ 的邻域全纯，
边界多圆周上 $|F|\le M_F$，
则真实联合 Cauchy 演算及 (4.1) 给
$$
\boxed{
\|F(G_2,\ldots,G_p)\|
\le K M_F
\exp[C_\varepsilon(1+\log(1/\delta))^\gamma].
}
\tag{4.2}
$$
圆周长度的每个半径正好消去相应预解式的 $|\lambda|^{-1}$。
常数不依赖 $\delta,F$，允许 $F$ 随反射次数与选位变化。
$p=1$ 时没有联合积分，按通常标量值解释。

## 5. 不要求同幅的保重数 Hermite 逆

本节推广 R236 余式使用的幅度区间：不要求
$\delta\le|a_j|\le2\delta$，只需
$$
\delta\le|a_j|\le a_0,\qquad j\in F,
\tag{5.1}
$$
其中 $a_0>0$ 是依赖固定 $q$ 的足够小常数。

设 $q$ 的不同根为 $\lambda_\nu$，重数为 $\mu_\nu$。
存在固定 $\varepsilon,\delta_0,a_0>0$，使当
$$
0<\delta\le\delta_0,\qquad
|\kappa_n|\le2\varepsilon\delta^n
\tag{5.2}
$$
时，$\mathcal P(z;\kappa)$ 的每个根团在
$|z-\lambda_\nu|<\delta/8$ 内并保持总重数 $\mu_\nu$。

证明这项定量 Rouché 断言：
展开有限指数，得到
$\mathcal P-q=\sum_{d=2}^p C_d(\kappa)q^{(d)}$，
其中 $C_d$ 按权 $\deg\kappa_n=n$ 齐次，且
$|C_d|\le C_p\varepsilon\delta^d$。
在 $|z-\lambda_\nu|=\delta/8$ 上，
$d\le\mu_\nu$ 的项由
$q^{(d)}=O(\delta^{\mu_\nu-d})$ 控制，
$d>\mu_\nu$ 的项则用有界导数及 $\delta^d\le\delta^{\mu_\nu}$。
故扰动不超过 $C_q\varepsilon\delta^{\mu_\nu}$。
取 $\varepsilon$ 小于固定的 Rouché 常数，便小于
$|q(z)|\ge c_q8^{-\mu_\nu}\delta^{\mu_\nu}$。
团外无余根，因为总重数为 $p$。

取圈
$$
\Gamma_\nu=\{|z-\lambda_\nu|=\delta/4\}.
$$
令
$$
\mathscr L_a(z;\kappa)
=-2[\mathcal P(z-2a;\kappa)-\mathcal P(z;\kappa)],
$$
$$
H_F(z;\kappa)
=\prod_{j\in F}[-2\mathcal P(z-2a_j;\kappa)].
$$
若 $|F|=r$ 且 (5.1) 成立，取 $a_0$ 小于不同根间距的固定小倍数。
同一根团经 $2a_j$ 平移后距原团至少 $2|a_j|$；
在原 $\Gamma_\nu$ 及其内部，它与原团之间的余距至少固定常数乘 $|a_j|$。
不同根团间距仍有固定正下界。
于是 $H_F^{-1}$ 在各圈内部及邻域全纯，且
$$
|H_F^{-1}|\le C_q^r\delta^{-pr},\qquad
|\mathcal P(\zeta;\kappa)|\ge c_q\delta^p
\quad(\zeta\in\cup_\nu\Gamma_\nu).
\tag{5.3}
$$
只用最小幅度 $\delta$；不出现最大与最小幅度之比。
复相位不影响以上距离下界。

定义次数小于 $p$ 的真正 Hermite 余式
$$
\mathcal R_F(z;\kappa)
=\frac1{2\pi i}\sum_\nu\int_{\Gamma_\nu}
\frac1{H_F(\zeta;\kappa)}
\frac{\mathcal P(\zeta;\kappa)-\mathcal P(z;\kappa)}
{(\zeta-z)\mathcal P(\zeta;\kappa)}\,d\zeta.
\tag{5.4}
$$
系数在 (5.2) 的多圆盘内部全纯。
分子差商的系数一致有界，圈长为 $O(\delta)$，所以
$$
|[z^k]\mathcal R_F|
\le C_q^{r+1}\delta^{-pr-p+1},\qquad 0\le k<p.
\tag{5.5}
$$
Cauchy 公式给 $H_F^{-1}-\mathcal R_F$ 在每个根团内被 $\mathcal P$ 全纯整除；
因而保留全部重数。再用
$\mathscr L_a\equiv-2\mathcal P(z-2a)\pmod{\mathcal P}$，得到多项式恒等式
$$
\boxed{
\mathcal R_F\prod_{j\in F}\mathscr L_{a_j}
=1+\mathcal P\mathcal S_F.
}
\tag{5.6}
$$
这不是仅在不同根的数值上插值。

对 (5.4) 的系数一次使用 (4.2)，再在有界 $X$ 上代入，令
$$
\mathfrak R_F=\mathcal R_F(X;G)\in\mathcal A.
$$
在 $M$ 上有
$$
\left(\prod_{j\in F}\mathscr L_{a_j}(X;G)\right)
\mathfrak R_Ff=f,\qquad f\in M,
\tag{5.7}
$$
而
$$
\boxed{
\|\mathfrak R_F\|
\le\exp[C_1\ell^\gamma+C_2r\ell+C_3r+C_4],
\qquad \ell=1+\log(1/\delta).
}
\tag{5.8}
$$
常数只依赖原固定行、$b,q$；特别不依赖 $F,r$ 的物理跨度。
一次联合求值不重复支付 $r$ 次预解成本。

## 6. 平方窗口与物理前缀删除

取固定 $\kappa>0$，其值在 §9 决定。
对趋于无穷的整数 $r$ 置
$$
Q_r=\lceil\kappa r^2\rceil,\qquad
h_r=\lceil3\log_2(r+1)\rceil,\qquad
K_r=Q_r+h_r.
$$
取幅度最大的 $K_r$ 个实际非零系数，删去所有物理位置 $j<h_r$。
至多删掉 $h_r$ 项，故可从余项取恰有 $Q_r$ 个指标的集合 $I_r$。
它满足
$$
\min I_r\ge h_r,\qquad
|a_j|\ge\delta_r:=\rho_{K_r}\quad(j\in I_r).
\tag{6.1}
$$
最大物理位没有上界要求。
因为 $h_r\to\infty$ 且原 $a_j\to0$，
$\max_{j\in I_r}|a_j|\to0$，所以最终满足 §5 的固定上界 $a_0$。
这一步不需要其收敛速率。

(1.1) 给
$$
\ell_r:=1+\log(1/\delta_r)
\le C_0+\beta_+K_r^\alpha.
\tag{6.2}
$$
(5.8) 因而给所有 $F\subset I_r$、$|F|=r$ 的统一界
$$
\boxed{
\log\|\mathfrak R_F\|
\le C_5K_r^{\alpha+1}
+C_6rK_r^\alpha+C_7r+C_8.
}
\tag{6.3}
$$
这里 $\alpha\gamma=\alpha+1$。
所有 $C_i$ 均在选择 $\kappa$ 之前固定。

## 7. 实际反射、Boolean 余式与先消逆再反射

记
$$
J_F=\prod_{j\in F}M_{\chi_j},\qquad
\gamma_F(B)=J_FBJ_F.
$$
R260 的真实局部壳给
$$
\widehat X_F=X+\sum_{j\in F}a_j[V(-t_jN_j)-R_j],
$$
$$
\widehat G_{n,F}
=G_n+\sum_{j\in F}a_j^n
[L_n(V(-t_jN_j))-L_n(R_j)]
$$
以及
$$
\|\gamma_F(X)-\widehat X_F\|
+\sum_{n=2}^p
\|\gamma_F(G_n)-\widehat G_{n,F}\|
\le\epsilon_h,\qquad
\epsilon_h\le C e^{-c\,16^{h-1}},\quad h=\min F.
\tag{7.1}
$$

为明确不依赖最大位的原因：第 $\ell$ 个差壳只含 $j<\ell$；
若 $F\cap(j,\ell]=\varnothing$，整壳准确为零。
有界 Cayley 逆差给其范数至多
$C\sum_{j<\ell}|a_j|\alpha_\ell/\alpha_j
\le C\|a\|_2\eta_{\ell-1}$。
固定 $L_n$ 的壳同理，把 $a$ 换成 $a^n$。
求和从 $\ell\ge h$ 开始，给 (7.1)。
同位纯项已被符号反转完全吸收，故没有一个大小为1的第 $j=\ell$ 项。

置
$$
\widehat T_F=\mathcal P(\widehat X_F;\widehat G_F),\qquad
A_F=\widehat T_F-T.
$$
所有带帽算子仍在同一交换代数 $\mathcal A$。
由于 $\sum|a_j|<\infty$，$\widehat X_F,\widehat G_F,\widehat T_F$ 及 $A_F$ 的范数对全部有限 $F$ 一致有界。
固定有限多项式的幂差和 (7.1) 给
$$
\|\gamma_F(T)-\widehat T_F\|\le C_p\epsilon_h,\qquad
\|(\gamma_FT)^r-\widehat T_F^r\|
\le r C_p^r\epsilon_h.
\tag{7.2}
$$
这些是全域有界等式，没有剩余自然域问题。

由真实有理差及 $N_j^2=\eta_jN_{j+1}$，
可以将 $A_F$ 替换为
$$
\widetilde A_F=
\mathcal P\left(
X+4\sum_{j\in F}a_jt_jN_j;\
G_n+4L_n'(1)\sum_{j\in F}a_j^nt_jN_j
\right)-\mathcal P(X;G)
\tag{7.3}
$$
且
$$
\|A_F-\widetilde A_F\|\le C_p\eta_h.
$$
例如 $V(-tN)-V(tN)=4tN(I-t^2N^2)^{-1}$，
减去 $4tN$ 后明确含 $N^2$；对固定 $L_n$ 同样逐项提取 $N^2$。
全部逆的一致界已经在 §2 支付。

现把 (7.3) 看作交换形式变量 $x_j$ 的多项式。
它没有零次项，一次部分准确为
$$
\sum_{j\in F}t_jx_j\mathscr L_{a_j}(X;G).
\tag{7.4}
$$
这里使用精确有限差恒等式
$$
4L_n'(1)=-2(-2)^n,\qquad
\partial_{\kappa_n}\mathcal P=\partial_z^n\mathcal P/n!.
$$
$r$ 个正次因子相乘而变量只有 $r$ 个，故
$$
\widetilde A_F^r
\equiv r!t_FN_F\prod_{j\in F}\mathscr L_{a_j}(X;G)
\pmod{(N_j^2:j\in F)},
$$
$$
t_F=\prod_{j\in F}t_j,\qquad N_F=\prod_{j\in F}N_j.
\tag{7.5}
$$
每个弃项真含重复位，实际求值后获得至少一个 $\eta_h$。
系数算子范数的绝对和至多 $C_p^r$：
对 (7.3) 取系数绝对值，用 $\sum_{j\in F}|a_j|\le\|a\|_1$、
固定 $G_n,X$ 范数及 $\sup|t_j|$ 即可。
因而 (7.5) 的实际余项范数不超过 $C_p^r\eta_h$。
这不要求同幅，也不付 $(\max|a_j|/\min|a_j|)^r$。

对 $f\in M$ 取 $f_F=\mathfrak R_Ff\in M$。
采用左反射恒等式
$$
T^rJ_Ff_F=J_F(\gamma_FT)^rf_F.
$$
因为 $\widehat T_F=T+A_F$ 与 $T$ 交换，且 $Tf_F=0$，
$\widehat T_F^rf_F=A_F^rf_F$。
先在同一个 $M$ 内用 (5.7) 消去整个有限差乘积，再在左边作用 $J_F$。
结合 (7.2)--(7.5)，
$$
T^rJ_F\mathfrak R_Ff
=r!t_FJ_FN_Ff+\mathcal E_Ff,
$$
$$
\boxed{
\|\mathcal E_Ff\|
\le r C_p^r\epsilon_h
\|\mathfrak R_F\|\|f\|.
}
\tag{7.6}
$$
已将更小的 $\eta_h$ 吸入 $\epsilon_h$。
这一步没有把有限差多项式无证移过物理反射。

令 $E_j$ 为原纯位平方零矩阵。
$J_jE_j=-E_j$，且
$\|N_F-\prod_{j\in F}E_j\|\le r\eta_h$，
所以主项进一步为
$$
(-1)^r r!t_F\prod_{j\in F}E_jf
$$
加上范数至多 $r!|t_F|r\eta_h\|f\|$ 的真实误差。

## 8. 平方窗口的非零全空间弱极限

定义 $M\to H$ 的有界输入
$$
\mathcal V_r=
(-1)^r\left(\frac2{Q_r}\right)^r
\sum_{\substack{F\subset I_r\\|F|=r}}
t_F^{-1}J_F\mathfrak R_F.
\tag{8.1}
$$
令 $L=\max(1,\sup_j|t_j|^{-1})$。
因
$\binom{Q_r}r(2/Q_r)^r\le2^r/r!$，
有
$$
\|\mathcal V_r\|
\le\frac{(2L)^r}{r!}\sup_F\|\mathfrak R_F\|,
$$
从而扩大固定常数后
$$
\boxed{
\log^+\|\mathcal V_r\|
\le C_5K_r^{\alpha+1}
+C_6rK_r^\alpha+C_9r+C_{10}.
}
\tag{8.2}
$$

置
$$
C_{I_r}=\frac2{Q_r}\sum_{j\in I_r}E_j.
$$
不同位的 $E_j$ 交换且平方为零。(7.6) 求和因此给
$$
\|T^r\mathcal V_rf-C_{I_r}^rf\|
\le
\left[
\frac{(2L)^r}{r!}r C_p^r\epsilon_{h_r}
\sup_F\|\mathfrak R_F\|
+2^rr\eta_{h_r}
\right]\|f\|.
\tag{8.3}
$$
$16^{h_r}\ge(r+1)^{12}$，所以 $\epsilon_{h_r}\le C e^{-c'(r+1)^{12}}$。
(6.3) 的增长至多 $e^{O(r^4)}$；(8.3) 的方括号趋零。

R264 的有限位提升矩阵估计给
$$
\|C_{I_r}^r\|\le(1+1/Q_r)^r\longrightarrow1.
$$
对任意两个固定有限柱 $f,g$，充分大 $r$ 时所有选中位都在它们支撑之后，准确有
$$
\langle C_{I_r}^rf,g\rangle
=\frac{(Q_r)_r}{Q_r^r}\langle f,g\rangle
\longrightarrow e^{-1/(2\kappa)}\langle f,g\rangle.
$$
利用有限柱稠密及一致范数界，得到整个原 $H$ 上的弱算子极限
$$
\boxed{
C_{I_r}^r\rightharpoonup
\alpha_\kappa I,\qquad
\alpha_\kappa=e^{-1/(2\kappa)}>0.
}
\tag{8.4}
$$
所以对每个 $f\in M$，
$$
T^r\mathcal V_rf\rightharpoonup\alpha_\kappa f.
\tag{8.5}
$$
$\kappa$ 始终固定；没有令它随 $r$ 趋零，也没有将此弱极限写成强极限。

## 9. 固定局部交换子与四次成本

取任意固定局部矩阵 $D$，支撑在前 $h$ 位。
记
$$
Z_h=\sum_{j\ge h}a_jR_j,\qquad
s_h=a_*+\sum_{j<h}a_j,\qquad
G_{n,\ge h}=\sum_{j\ge h}a_j^nL_n(R_j).
$$
$D$ 与所有这些实际尾算子交换。

有限低头有明确有界 $A$ 因子：
$$
X-(s_hI+Z_h)=A U_{1,h},\qquad
G_n-G_{n,\ge h}=A U_{n,h}.
$$
例如
$$
U_{1,h}
=-2\sum_{j<h}a_jt_jd_j^{-1}
A^{2^j-1}(I+t_jN_j)^{-1}.
$$
$L_n(1)=0$ 给 $U_{n,h}$ 的同类有限表达。
固定有限多项式的差遂给
$$
T=T_{\rm tail}+A U_h,\qquad
T_{\rm tail}=\mathcal P(s_hI+Z_h;G_{\ge h}),\qquad
U_h\in\mathcal A.
\tag{9.1}
$$
这里 $U_h$ 真正有界，因为 $X,Z_h$ 均有界；
不是将一般零字符元直接除以 $A$。
全部项交换，$D$ 与 $T_{\rm tail}$ 交换，故
$$
\operatorname{ad}_T^rD
=\sum_{s=0}^r(-1)^s\binom rs
A^{r-s}U_h^{r-s}D A^sU_h^s.
$$
不把 $A$ 移过 $D$。由 (2.2)，
$$
\boxed{
\|\operatorname{ad}_T^rD\|
\le\|D\|(2\|U_h\|)^r
\exp[-(5/6)r^4+105r^3].
}
\tag{9.2}
$$

当 $0<\alpha<1$，(8.2) 给
$$
\log^+\|\mathcal V_r\|=o(r^4),
$$
所以可取任意固定 $\kappa>0$。
当 $\alpha=1$，因 $K_r/r^2\to\kappa$，
$$
\limsup_{r\to\infty}r^{-4}\log^+\|\mathcal V_r\|
\le C_5\kappa^2.
$$
此时选择一个固定 $\kappa>0$ 使
$C_5\kappa^2<1/4$。
$C_5$ 不依赖局部测试 $D,h$，故同一个 $\kappa$ 可用于全部固定局部矩阵。
于是两种情形都有
$$
\|(\operatorname{ad}_T^rD)\mathcal V_rf\|\longrightarrow0
\qquad(f\in M).
\tag{9.3}
$$

令 $\mathcal B(x,y)=\langle x,C_0y\rangle$。
$T$ 的真正 $C_0$ 自伴性、$Tg=0$ 及有限 Leibniz 展开给
$$
\mathcal B(DT^r\mathcal V_rf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD)\mathcal V_rf,g)
\quad(f,g\in M).
$$
右侧由 (9.3) 趋零，左侧由 (8.5) 趋于
$\alpha_\kappa\mathcal B(Df,g)$。
因此
$$
\mathcal B(Df,g)=0
\quad(f,g\in M,\ D\text{ 任意固定局部矩阵}).
$$
原 Haar 局部全矩阵代数不可约，任意非零 $f$ 的局部轨道稠密。
取 $g=f\ne0$ 就迫 $C_0f=0$，矛盾。
所以
$$
\boxed{\ker T=0.}
\tag{9.4}
$$

## 10. 循环性与范围

由 (2.5)，$\ker T^*=C_0\ker T=0$，故 $T$ 的像稠密。
$T$ 有界且交换 $A$，而 $e^w$ 是 R176 已证的真实循环向量。
因此
$$
[q(u)e^w]_A
=[Te^w]_A=\overline{\operatorname{Ran}T}=H.
$$
这证明 (1.2)，不取简单根多项式的极限。

本稿新增的是：

- 对 $0<\alpha\le1$ 的排序指数上界，保全部实际 carry 的累积量对数型整增长；
- 全复方向预解及 Bell 权小多圆周的一次对数型联合预算；
- 只要求最小幅度与趋零最大幅度、无需同幅比的保全部重数 Hermite 逆；
- 任意物理重排的指数与伸缩指数行上，全部加权多项式的循环性。

R265 已给更快 $1<\alpha\le3/2$ 行的解析 Bell 分支及简单根循环性。
本文的联合逆成本在该区间可能超过四次预算，所以没有把全部重数扩到该区间。
一般 little-weak-$\ell^1$、无弱上界行的全部重数、多模式点态多项式、正常湮灭者、边界 $N=M$ 与普通 ISP 仍需各自证明。

## 依赖正文

- R109：原 $A^k$ 的四次范数界。
- R176：复 first 指数的循环性、实际 Bell 恒等式与固定共轭。
- R236《实际累积量的分阶阶乘幂界与联合预解预算》：正锥主控与局部实际指数预算；本文重新支付排序指数类的整增长。
- R236《规范加权多项式的全部重数循环性》：Hermite 余式的保重数机制；本文 §5 放宽同幅条件并给完整量化。
- R260：任意物理跨度的真实壳消失及最小位 carry 界。
- R264：平方窗口的全 $H$ 非零弱平均；本文 §8 保留准确量词。
