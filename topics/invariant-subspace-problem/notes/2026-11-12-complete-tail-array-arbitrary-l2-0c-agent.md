# R104 附注：任意固定次数的完整高尾数组近标量

日期：2026-11-12
作者：Astra-ISP-0c017065 / l2_moments
状态：已证明。作为 R104 的补充来源，不另占正式结果编号；不修改已交付的 R104 主稿。

## 1. 完整尾数组必须包含空集

固定 $0\ne g\in H$ 与有限整数 $p\ge0$。由常向量循环性，选 $n_0\ge0$ 使
$$
\beta=B(A^{n_0}1,g)\ne0.
$$
令
$$
\mathcal T_{p,m}
=\overline{\operatorname{span}}
\{\chi_J:J\subseteq[m,\infty),\ |J|\le p\}.
\tag{1.1}
$$
这个尾空间包含常数，对应 $J=\varnothing$。
记 $U_{p,m}$ 为它到
$\ell^2(\{J\subseteq[m,\infty):|J|\le p\})$
的 Walsh 系数等距映射。

对整个 $H_{\le p}$，定义
$$
\Phi^{(p)}_{g,m}f
=\left(B(A^{n_0}T_Jf,g)\right)_{
J\subseteq[m,\infty),\ |J|\le p},
\qquad T_J=\prod_{j\in J}(2N_j-I).
\tag{1.2}
$$
约定 $T_\varnothing=I$。因此空集分量正是普通矩
$B(A^{n_0}f,g)$，不能遗漏。

**定理。** 该数组在 $H_{\le p}$ 上有界，并且
$$
\boxed{
\left\|\Phi^{(p)}_{g,m}|_{\mathcal T_{p,m}}
-\beta U_{p,m}\right\|\longrightarrow0.
}
\tag{1.3}
$$
故对充分大的 $m$，
$$
\boxed{
\|\Phi^{(p)}_{g,m}f\|_{\ell^2}
\ge\frac{|\beta|}{2}\|f\|_2
\qquad(f\in\mathcal T_{p,m}).
}
\tag{1.4}
$$
测试端 $g$ 完全任意，不要求有限次数。

## 2. 合成、模型恒等式与真实误差

对每个 $0\le r\le p$，用 R84 的常数 $C_{p,r},D_{p,r}$，其中可取
$C_{p,0}=1,D_{p,0}=0$。设
$$
C_p=\left(\sum_{r=0}^p C_{p,r}^2\right)^{1/2},
\qquad
D_p=\left(\sum_{r=0}^p D_{p,r}^2\right)^{1/2}.
$$
对有限数组 $(c_J)$，分别按 $|J|$ 合成并作有限次 Cauchy--Schwarz，得到
$$
\left\|\sum_Jc_JS_Jf\right\|_2
\le C_p\|c\|_{\ell^2}\|f\|_2,
\tag{2.1}
$$
$$
\left\|\sum_Jc_J(T_J-S_J)f\right\|_2
\le D_p\eta_m\|c\|_{\ell^2}\|f\|_2
\quad(f\in H_{\le p}).
\tag{2.2}
$$
这里所有 $J$ 都在高尾中，包含空集。对任意 $g\in H$ 作双线性对偶，
$$
\|\Phi^{(p)}_{g,m}\|
\le W_{n_0}(C_p+D_p\eta_m)\|g\|_2.
\tag{2.3}
$$

令 $g_m=\mathbb E_mg$ 是低 $m$ 位条件期望，
$$
\beta_m=B(A_m^{n_0}1,g_m)=B(A_m^{n_0}1,g).
$$
于是
$$
|\beta_m-\beta|
\le n_0\alpha_m^{\rm op}\|g\|_2.
\tag{2.4}
$$
若 $f\in\mathcal T_{p,m}$，则对任意两个高尾有限集 $J,S$，
$$
\int S_J\chi_S\,d\mu_{\rm tail}
=\mathbf1_{\{J=S\}}.
\tag{2.5}
$$
若 $S\setminus J$ 非空，其余 Walsh 因子均值为零；
若 $J\setminus S$ 非空，相应的 $S_j1=-\chi_j$ 均值为零；
而 $J=S$ 时各位 $S_j\chi_j=1-2\chi_j$ 的常数项为 $1$。
这也涵盖 $J=S=\varnothing$。

纯头与纯尾张量分离因此给
$$
\boxed{
\left(B(A_m^{n_0}S_Jf,g_m)\right)_J
=\beta_m U_{p,m}f.
}
\tag{2.6}
$$
模型恒等式对整个尾次数 $\le p$ 空间成立，不只对最高齐次层成立。

真实差分仍按 R104 的正确次序：
$$
\begin{aligned}
&B\!\left(A^{n_0}\sum_Jc_J(T_J-S_J)f,g\right)\\
&\quad+
B\!\left((A^{n_0}-A_m^{n_0})\sum_Jc_JS_Jf,g\right)\\
&\quad+
B\!\left(A_m^{n_0}\sum_Jc_JS_Jf,g-g_m\right).
\end{aligned}
$$
所有合成都先作用于原 $f\in H_{\le p}$；实际进位及实际幂均在合成之后估计。
由 (2.1)—(2.4)，
$$
\boxed{
\left\|\Phi^{(p)}_{g,m}|_{\mathcal T_{p,m}}-\beta U_{p,m}\right\|
\le
W_{n_0}D_p\eta_m\|g\|_2
+(C_p+1)n_0\alpha_m^{\rm op}\|g\|_2
+C_p\|A_m^{n_0}\|\,\|g-\mathbb E_mg\|_2.
}
\tag{2.7}
$$
右端趋于零，证明 (1.3)—(1.4)。

## 3. 零矩空间的有限头导数控制

记
$$
\mathcal Z_g^{(p)}
=\{f\in H_{\le p}:B(A^nf,g)=0\text{ 对全部 }n\ge0\}.
$$
令 $Q_m$ 是对低 $m$ 位取均值、仅保留高尾变量的正交投影。
在 $H_{\le p}$ 上，
$$
\operatorname{Ran}Q_m=\mathcal T_{p,m}.
$$
因为 (1.2) 中每一测试都是 $A$ 的多项式，零矩给
$\Phi^{(p)}_{g,m}f=0$。对满足 (1.4) 的 $m$，
$$
\frac{|\beta|}{2}\|Q_mf\|_2
\le\|\Phi^{(p)}_{g,m}(I-Q_m)f\|_{\ell^2}.
$$
设 $M=\|\Phi^{(p)}_{g,m}\|$，则
$$
\boxed{
\|f\|_2
\le C_{g,p,m}\|(I-Q_m)f\|_2,\qquad
C_{g,p,m}
=\left[1+\left(\frac{2M}{|\beta|}\right)^2\right]^{1/2},
\quad f\in\mathcal Z_g^{(p)}.
}
\tag{3.1}
$$
所以该零矩空间是“至少含一个低位的 Walsh 系数空间”某个子空间上的有界线性图。
它不只是说每个向量各自有某个低位系数；同一个有限 $m$ 和同一个常数同时控制所有可能的零矩向量。

用 Walsh 删除算子
$$
D_j\chi_S=\mathbf1_{\{j\in S\}}\chi_{S\setminus\{j\}}
$$
还得到
$$
\|(I-Q_m)f\|_2^2
=\sum_{S:S\cap[0,m)\ne\varnothing}|\widehat f(S)|^2
\le\sum_{j<m}\|D_jf\|_2^2.
$$
因此
$$
\boxed{
\|f\|_2
\le C_{g,p,m}
\left(\sum_{j<m}\|D_jf\|_2^2\right)^{1/2}
\qquad(f\in\mathcal Z_g^{(p)}).
}
\tag{3.2}
$$
这是有限组低位导数的统一控制；没有断言这些导数本身仍属于某个已知零矩空间。

## 4. 一阶维数界的改进及高阶边界

当 $p=1$，
$$
(I-Q_m)H_{\le1}
=\operatorname{span}\{\chi_0,\ldots,\chi_{m-1}\},
$$
其维数是 $m$。常数已经被含空集的尾数组控制。因此 (3.1) 将 R104 主稿的安全界改进为
$$
\boxed{\dim\mathcal Z_g\le m.}
\tag{4.1}
$$
这里的 $m$ 是 (1.4) 成立的某个充分大整数，未声称存在与 $g$ 无关的统一维数上界。

当 $p\ge2$，$(I-Q_m)H_{\le p}$ 仍是无限维。例如固定 $j<m$ 后，所有
$\chi_j\chi_k$、$k\ge m$ 都属于这个空间。
(3.1)—(3.2) 因而不直接证明高阶零矩空间有限维。
删除算子 $D_j$ 也不与实际 $A$ 自动交换，不能把 (3.2) 当作已经完成的次数归纳。

本附注保留了真正一般的测试端 $g\in H$，但尚未由这些结构排除所有非零零矩向量。
