# R230 附录：任意收缩有限块的完整 Gram 与逆源障碍

日期：2026-11-13（UTC）。状态：已证明；普通 Hilbert ISP、一般正正常湮灭者及边界无权核心仍未解决。

完整证明见[任意有限交换块](../notes/2026-11-13-arbitrary-contractive-block-complete-gram-and-source-obstruction-normal-complex.md)；[任意标量 Schur 块](../notes/2026-11-13-all-schur-block-inverse-sources-and-universal-large-column-obstruction-normal-complex.md)保留独立的显式次数列证明。本文保持 R244 的原实际提升、原源、原最小逆和全部有限列量词。

## 1. 准确前提与结论

纯块上
$$
E=|1\rangle\langle0|,\quad D=I-2E,\quad
\Omega=2^{-q/2}(|0\rangle+|1\rangle)^{\otimes q},\quad
\chi_F=D_F\Omega .
$$
令
$$
\mathcal A_q^0=\operatorname{span}\{E_F:F\subseteq B\}
=\operatorname{span}\{D_F:F\subseteq B\}.
$$
真空是循环分离向量，故每个块向量 $u$ 唯一确定
$X_u^0\in\mathcal A_q^0$，满足 $X_u^0\Omega=u$。

固定同一物理分块 $|B_i|=q_i=16^i$ 与同一连续正、$C$ 实且**非湮灭**的向量
$$
f=1+\sum_{i\ge1}c_i\chi_{B_i},\qquad
c_i=2^{-i-2}=\frac1{4q_i^{1/4}},\qquad
\lambda=\|f\|^2=\frac{49}{48}.
$$
允许任意可逆收缩
$$
R_i\in\mathcal A_{q_i}^0,\quad \|R_i\|\le1,\quad
U_i=R_i^{-1}=X_{g_i}^0,\quad g_i=U_i\Omega,\quad n_i=\|g_i\|\ge1.
$$
不要求位对称、单变量函数表示或原标量函数为 Schur。

实际列使用 $V_j1=\chi_j$、$\|V_j-D_j\|\le8\eta_j$。
保留原准确逆块及预算
$$
\widetilde U_i=\frac{X_{g_i}}{1-\varepsilon_i},\quad
0\le\varepsilon_i<\frac12,\quad
16q_i5^{q_i}n_i\eta_{\min B_i}\le\varepsilon_i.
\tag{1.1}
$$
假设真实互不交源乘积
$$
g^{(m)}=\prod_{i\le m}\frac{g_i}{1-\varepsilon_i}\longrightarrow g
\quad\text{于原 }H,
\tag{1.2}
$$
并保 R244 所需的 $P$、$Pg=1$ 和同一组一致有界强单位。
于是原最小逆 $G=P^{-1}=X_g$ 在所有有限列上满足 $Gu=X_ug$。

**定理。** 存在同一各块上的实际有限 Walsh 列 $u_i$，$\|u_i\|\le1$，使
$$
\|Gu_i\|\longrightarrow\|g\|>0,\qquad
\boxed{\ 
\lim_i\frac1{q_i}
\log\frac{|\langle X_{u_i}f,f\rangle|}{\|Gu_i\|}
=\frac{\log5}{2}\ }.
\tag{1.3}
$$
因此整个纯有限交换块代数中这类收敛逆源均不能为该固定态提供 R244 的全列聚合界。

## 2. 从原矩阵构造协变符号

源收敛与 $n_i\ge1$ 直接给
$$
g_i\to\Omega,\quad n_i\to1,\quad
\|R_i\Omega-\Omega\|\le\|g_i-\Omega\|\to0.
\tag{2.1}
$$
对 $R=\sum_Fr_FE_F$ 定义
$$
b_R(z)=\sum_Fr_F(z/2)^{|F|},\qquad
\Omega_t=\frac{(|0\rangle+t|1\rangle)^{\otimes q}}
{(1+|t|^2)^{q/2}}.
$$
逐位计算得到
$$
\langle R\Omega_t,\Omega_s\rangle
=\frac{(1+t\bar s)^q}{(1+|t|^2)^{q/2}(1+|s|^2)^{q/2}}\,
 b_R\!\left(\frac{2\bar s}{1+t\bar s}\right).
\tag{2.2}
$$
取 $s=t$，映射 $2\bar t/(1+|t|^2)$ 覆盖闭单位盘，故
$\|R\|\le1$ 严格推出 $|b_R|\le1$。
这证明的是新协变符号的 Schur 性，没有把原 $R$ 替换成 $b_R(T_q)$。

取 $h=q^{-1/2}$、$t=1$、$s=(1-h)/(1+h)$，对 $R-I$ 应用 (2.2)：
$$
|b_R(1-h)-1|\le e^{1/2}\|R\Omega-\Omega\|.
\tag{2.3}
$$
因此逐块 $\ell_i=-\log|b_{R_i}(1-h_i)|\to0$。

## 3. 内部小圆与相干方向下界

将非零 Schur 多项式分解为 $b=IF$，其中 $I$ 包含全部盘内零点、$F$ 零点自由且 Schur。在 $x=1-h$，
$$
\sum_{\alpha}(1-|\alpha|)\le8\ell/h,\qquad
r:=\#\{|\alpha|\le3/4\}\le32\ell/h.
$$
Harnack 比较及其余 Blaschke 因子的显式逆界给
$$
|b(z)|\ge e^{-A}|I_{\rm in}(z)|\quad(|z|\le8/11),\qquad
A=\frac{1862}{3}\ell/h.
\tag{3.1}
$$
常数来自零点自由部分 $38\ell/(3h)$ 和外圈零点部分 $608\ell/h$；完整推导保于源稿。

取 $z_0=-3/5$、$\rho=q^{-1/4}$。
圆平均
$$
\frac1{2\pi}\int\log|z_0+\rho e^{it}-\alpha|\,dt
=\log\max(\rho,|z_0-\alpha|)
$$
保证该小圆上存在一点 $z$，使
$$
|b(z)|\ge \exp[-A-r\log(2/\rho)].
$$
在 (2.2) 取 $t=-3$、$\bar s=z/(2+3z)$。极化核的绝对平方准确为
$$
\frac{|1-3\bar s|^2}{10(1+|s|^2)}
=\frac1{1+25|z+3/5|^2}.
$$
故
$$
\|R_i\Omega_{-3}\|\ge e^{-\Gamma_i},\quad
\Gamma_i=\frac{1862}{3}\ell_i\sqrt{q_i}
+r_i\log(2q_i^{1/4})+\frac{25}{2}\sqrt{q_i}=o(q_i).
\tag{3.2}
$$
上界为1，所以 $q_i^{-1}\log\|R_i\Omega_{-3}\|\to0$。
任意多变量、不对称块都使用原矩阵的此下界。

## 4. 准确完整 Gram 与最优列

对所有 $2^{q_i}$ 个纯列，矩向量准确为
$$
m_i=(\lambda-c_i^2)\Omega+2c_i\chi_{B_i}
+c_i^2D_{B_i}^*\chi_{B_i},\qquad
\langle X_u^0f,f\rangle=\langle u,m_i\rangle.
\tag{4.1}
$$
纯反射满足 $CR_i^*C=R_i$；$q_i$ 偶数保证
$C\chi_{B_i}=\chi_{B_i}$。逐坐标
$D\chi=\sqrt5\,\Omega_{-3}^{(1)}$，因而
$$
\|R_i^*D_{B_i}^*\chi_{B_i}\|
=5^{q_i/2}\|R_i\Omega_{-3}\|.
$$
置 $a_i=\|R_i^*m_i\|$，则
$$
c_i^2 5^{q_i/2}e^{-\Gamma_i}-(\lambda+2c_i)
\le a_i\le c_i^2 5^{q_i/2}+\lambda+2c_i.
$$
因此 $\log a_i/q_i\to(\log5)/2$。

完整 Gram 的对偶范数以及最优列分别为
$$
\sup_{u\ne0}\frac{|\langle X_u^0f,f\rangle|}{\|U_iu\|}
=\|R_i^*m_i\|,\quad
w_i=\frac{R_i^*m_i}{a_i},\quad u_i=R_iw_i.
\tag{4.2}
$$
于是 $\|u_i\|\le1$、$U_iu_i=w_i$、$\|w_i\|=1$，
且纯矩准确等于 $a_i$。这里没有次数截断或对角 Gram 代替。

## 5. 原实际提升与有限源组合

完整列的系数 $\ell^1$ 范数至多 $2^{q_i/2}$。
逐位 telescoping 及 (1.1) 给
$$
\Delta_i:=\|X_{u_i}-X_{u_i}^0\|
\le8q_i(3\sqrt2)^{q_i}\eta_{\min B_i}
\le\frac{\varepsilon_i}{2n_i}
 \left(\frac{3\sqrt2}{5}\right)^{q_i}\to0.
\tag{5.1}
$$
准确源张量分解给
$$
\|X_{u_i}^0g\|=\frac{\|g\|}{n_i}.
$$
正缩放在块内外的范数比中抵消。
因此 $|\|Gu_i\|-\|g\|/n_i|\le\Delta_i\|g\|$，
实际矩误差至多 $\lambda\Delta_i$，证明 (1.3)。

还可取同一分块上有限个完整成功源 $g^{(\nu)}$ 的线性组合，
条件是该组合确为合格 $P$ 的真空原像。
令 $S_i=\prod_{\nu=1}^K R_{i,\nu}$。
它仍为原代数中的收缩，且
$$
\|S_i\Omega-\Omega\|\le
\sum_{\nu=1}^K\|R_{i,\nu}\Omega-\Omega\|\to0.
$$
对 $S_i$ 取 (4.2) 的最优列，纯矩指数仍为 $(\log5)/2$，
而每支
$$
U_{i,\nu}u_i=\prod_{\mu\ne\nu}R_{i,\mu}w_i,\qquad
\|U_{i,\nu}u_i\|\le1.
$$
所以同一组合的 $\|Gu_i\|$ 一致有界，实际比值的指数下极限至少 $(\log5)/2$。
不要求共同逆源乘积收敛，也不把正则器之和的逆当作逆源之和。

## 6. 范围与继续研究的对象

上述结论包含所有可逆收缩的纯有限交换块，包括全部标量 Schur 因子、
全部圆周弧、任意单变量收缩多项式及不对称多变量块。
独立 Schur 稿另给 $k=\lfloor q/3\rfloor$ 的显式列与指数差
$$
\frac{\log2}{3}+\frac{\log3}{6}-\log(11/8)>1/16;
$$
其径向化保原 $g,G$，并处理只在开盘解析的函数。

[负实粗源](R230-appendix-negative-real-rough-sources-and-large-column-obstructions.md)
仍说明合格源不必属于 $\mathcal H_{\sqrt3}$。
本文不依赖该加权正则性。

当前固定 $f$ 不是湮灭者，不能把其特定
$c_i^2D_{B_i}^*\chi_{B_i}$ 分量移到任意正常见证。
真正未闭的是由全湮灭关系选出的矩向量、不同分块或非块正则器、
以及没有真空原像的前向构造。
