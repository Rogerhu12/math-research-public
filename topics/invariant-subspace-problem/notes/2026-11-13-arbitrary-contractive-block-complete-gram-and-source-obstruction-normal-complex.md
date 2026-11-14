# 任意纯有限块收缩逆的完整 Gram 障碍

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065。

**状态：已证明的中间结论。** 本稿关闭的不只是单变量 Schur 函数演算。
允许每个纯块的前向算子为整个有限交换 Walsh 代数中的任意可逆收缩，
无需它是 $T_q$ 的多项式，更无需该多项式具有标量 Schur 延拓。
若它们经原准确实际提升和正缩放得到的逆真空源乘积确实收敛，
则对既有同一固定正常态，完整有限块 Gram 的最优配对范数
具有准确指数 $(\log5)/2$。
相应实际有限列的逆像范数收敛到 $\|g\|$，
所以 R244 全列聚合界仍然失败。

关键不是把任意收缩矩阵当作 Schur 函数：
从真实矩阵的物理相干态期望，严格构造一个新的 Schur 协变符号。
其极化恒等式把标量预算准确转回原矩阵；
原前向、原逆源、原 $G$ 从未被替换。

本固定 $f$ 是已知非湮灭正常态。
真正湮灭者专属 Gram、非块正则器和无真空原像的路线仍开放，
普通 Hilbert ISP 未完成。

## 1. 整个有限交换块代数与准确实际前提

在每个物理位上记
$$
E=|1\rangle\langle0|,\qquad
\Omega_+=\frac{|0\rangle+|1\rangle}{\sqrt2},\qquad
\chi=\frac{|0\rangle-|1\rangle}{\sqrt2},\qquad
D=I-2E.
$$
$\Omega=\Omega_+^{\otimes q}$，
$\chi_F=D_F\Omega$ 是块内 Walsh 正交基。
纯有限代数为
$$
\mathcal A_q^0
=\operatorname{span}\{E_F:F\subseteq B\}
=\operatorname{span}\{D_F:F\subseteq B\}.
\tag{1.1}
$$
它是交换代数。$\Omega$ 为循环分离向量：
$$
X_u^0=\sum_Fu_FD_F,\qquad X_u^0\Omega=u
$$
给 $\mathcal A_q^0$ 与整个块 Hilbert 空间的一一对应。
任何可逆 $R\in\mathcal A_q^0$ 的逆也在该代数中，
因为去掉常数项后是幂零理想，有限 Neumann 展开准确给逆。

第 $i$ 块现在允许任意
$$
R_i\in\mathcal A_{q_i}^0,\qquad
R_i\text{ 可逆},\quad \|R_i\|\le1.
$$
令
$$
U_i=R_i^{-1},\qquad
g_i=U_i\Omega,\qquad n_i=\|g_i\|\ge1.
\tag{1.2}
$$
因此 $U_i=X_{g_i}^0$。

实际生成元保留原完整估计
$$
V_j1=\chi_j,\qquad
\|V_j-D_j\|\le8\eta_j,\qquad
\eta_j\le e^{-770\,16^j},\qquad
\|V_j\|,\|D_j\|<3.
\tag{1.3}
$$
实际列 $X_u=\sum_Fu_FV_F$ 满足 $X_u1=u$。

仍假设准确实际逆块和真空列为
$$
\widetilde U_i=\frac{X_{g_i}}{1-\varepsilon_i},\qquad
\widetilde g_i=\frac{g_i}{1-\varepsilon_i},
\qquad 0\le\varepsilon_i<1/2,
\tag{1.4}
$$
支付原预算
$$
16q_i5^{q_i}\max(1,n_i)\eta_{\min B_i}\le\varepsilon_i,
\tag{1.5}
$$
并且其互不交源乘积在原 $H$ 中收敛：
$$
g^{(m)}=\prod_{i\le m}\widetilde g_i\longrightarrow g.
\tag{1.6}
$$
使用 R244 时还保持构造所得 $P$、$Pg=1$、
同一组一致有界强单位等原前提，所以
$$
G=P^{-1}=X_g,\qquad Gu=X_ug
\tag{1.7}
$$
在所有有限 Walsh 列上准确成立。

固定
$$
q_i=|B_i|=16^i,\qquad
c_i=2^{-i-2}=\frac1{4q_i^{1/4}},
$$
$$
f=1+\sum_{i\ge1}c_i\chi_{B_i},\qquad
\lambda=\|f\|^2=\frac{49}{48},\qquad
\phi_f(Y)=\langle Yf,f\rangle.
\tag{1.8}
$$
所有 $q_i$ 为偶数；同一个 $f$ 和同一物理分块贯穿全文。

源收敛有一个直接后果。准确张量恒等式给
$$
\|g^{(i)}-g^{(i-1)}\|
=\|g^{(i-1)}\|\,
 \|g_i/(1-\varepsilon_i)-\Omega\|.
$$
前面范数至少 $1$，所以
$g_i/(1-\varepsilon_i)\to\Omega$。
由 $n_i\ge1$ 得 $\varepsilon_i\to0$，
从而
$$
\boxed{
g_i\to\Omega,\qquad n_i\to1,\qquad
\|R_i\Omega-\Omega\|\le\|g_i-\Omega\|\longrightarrow0.
}
\tag{1.9}
$$
下面的纯 Gram 引理只用 $R_i$ 收缩及 (1.9) 最后一项。

## 2. 任意真实收缩块的 Schur 协变符号

对复参数 $t$ 定义归一化物理相干态
$$
\Omega_t=
\frac{(|0\rangle+t|1\rangle)^{\otimes q}}
 {(1+|t|^2)^{q/2}},
\qquad \Omega_1=\Omega.
\tag{2.1}
$$
将任意 $R\in\mathcal A_q^0$ 写成
$$
R=\sum_{F\subseteq B}r_FE_F.
$$
定义新的标量多项式
$$
\boxed{
b_R(z)=\sum_{F\subseteq B}r_F(z/2)^{|F|}.
}
\tag{2.2}
$$
它不是把某个未经验证的原多项式当成 Schur 函数。

逐坐标计算给
$$
\langle R\Omega_t,\Omega_t\rangle
=b_R\left(\frac{2\overline t}{1+|t|^2}\right).
\tag{2.3}
$$
$t\mapsto2\overline t/(1+|t|^2)$ 覆盖整个闭单位圆盘：
固定相位后，模是 $2r/(1+r^2)$，取遍 $[0,1]$。
因此真实算子范数界 $\|R\|\le1$ 严格推出
$$
\boxed{|b_R(z)|\le1\quad(|z|\le1).}
\tag{2.4}
$$
所以 $b_R$ 确实是 Schur 多项式，无须 $R$ 有单变量 Schur 延拓。

更强的极化恒等式是
$$
\boxed{
\langle R\Omega_t,\Omega_s\rangle
=
\frac{(1+t\overline s)^q}
 {(1+|t|^2)^{q/2}(1+|s|^2)^{q/2}}\,
 b_R\left(\frac{2\overline s}{1+t\overline s}\right).
}
\tag{2.5}
$$
分母 $1+t\overline s$ 非零时按此式理解，其他点可按多项式连续延拓。
其证明是：每个 $E_F$ 的矩阵元为
$\overline s^{|F|}(1+t\overline s)^{q-|F|}$
除以相同归一化分母；相加即得。

作为与前稿的联系，若
$R=p(T_q)$、$T_q=2(q+2)^{-1}\sum_jE_j$，则
$$
b_R(z)=\sum_{n=0}^q
 p_n\frac{(q)_n}{(q+2)^n}z^n.
$$
(2.4) 只断言这个准确协变符号为 Schur，
没有断言原 $p$ 本身为 Schur。

## 3. 真空接近直接控制符号的径向值

令 $h=q^{-1/2}$，取实数
$$
s=\frac{1-h}{1+h}.
$$
在 (2.5) 中令 $t=1$。此时
$$
\frac{2s}{1+s}=1-h,\qquad
\frac{1+s}{\sqrt2\sqrt{1+s^2}}
=\frac1{\sqrt{1+h^2}}.
$$
将 $R$ 换成 $R-I$，得到准确关系
$$
\langle(R-I)\Omega,\Omega_s\rangle
=(1+h^2)^{-q/2}[b_R(1-h)-1].
$$
所以
$$
\boxed{
|b_R(1-q^{-1/2})-1|
\le e^{1/2}\|R\Omega-\Omega\|.
}
\tag{3.1}
$$
这是原矩阵的极化式，不使用对原多项式的 Poisson 表示。

对序列 $R_i$，由 (1.9)，
$$
b_i(1-h_i)\longrightarrow1,\qquad
b_i:=b_{R_i},\quad h_i=q_i^{-1/2}.
$$
略去有限初块后定义
$$
\ell_i=-\log|b_i(1-h_i)|\ge0,\qquad
\ell_i\longrightarrow0.
\tag{3.2}
$$

## 4. 符号在一个内部小圆周上的严格下界

本节的所有标量论证只用于已经由 (2.4) 证明为 Schur 的 $b_i$。
为完整可重做，重列所需的有限零点与调和预算。

固定 $b=b_i$、$q=q_i$、$h=q^{-1/2}$、$x=1-h$、$\ell=-\log|b(x)|$。
将全部开单位圆盘内零点按重数记为 $\alpha_\nu$，分解
$$
b(z)=I(z)F(z),\qquad
I(z)=\prod_\nu\frac{z-\alpha_\nu}{1-\overline{\alpha_\nu}z}.
\tag{4.1}
$$
$b$ 是非零多项式，所以零点有限。
$F$ 在单位圆盘解析、无零点且 $|F|\le1$；
最后一点由圆周上 $|I|=1$ 与最大值原理得到。
圆周上的零点可以留在 $F$ 中。

对每个 $p=|\alpha|<1$，
$$
1-\left|\frac{x-\alpha}{1-\overline\alpha x}\right|^2
=\frac{(1-x^2)(1-p^2)}{|1-\overline\alpha x|^2}
\ge\frac{h(1-p)}4.
$$
因此
$$
\boxed{
\sum_\nu(1-|\alpha_\nu|)\le8\ell/h.
}
\tag{4.2}
$$
令 $r$ 为 $|\alpha_\nu|\le3/4$ 的紧内零点数，则
$$
\boxed{r\le32\ell/h.}
\tag{4.3}
$$

令 $v=-\log|F|$。它在整个开圆盘上非负调和，
且 $v(x)\le\ell$。
Poisson 核最大最小值给 Harnack 界：
$$
\sup_{|z|\le8/11}v(z)
\le\frac{38}{3}\frac{\ell}{h}.
\tag{4.4}
$$
这里先比较 $v(0)\le2\ell/h$，
再用 $(1+8/11)/(1-8/11)=19/3$。

对其余 $p>3/4$ 的零点，
在 $|z|\le8/11$ 有
$$
\left|\frac{1-\overline\alpha z}{z-\alpha}\right|
\le\frac{1-8p/11}{p-8/11}
\le1+76(1-p).
$$
第一步可将 $\alpha$ 旋转到正轴，
检查固定 $|z|$ 的平方比值随夹角余弦递增；
第二步用 $p-8/11\ge1/44$。
结合 (4.2)，外圈逆积的对数至多 $608\ell/h$。
若 $I_{\rm in}$ 为紧内零点积，
于是得到
$$
\boxed{
|b(z)|\ge e^{-A}|I_{\rm in}(z)|
\quad(|z|\le8/11),\qquad
A=\frac{1862}{3}\frac{\ell}{h}.
}
\tag{4.5}
$$
在紧内零点处两边都为零，仍成立。

现在固定
$$
z_0=-\frac35,\qquad \rho=q^{-1/4}.
$$
充分大 $q$ 有 $\rho\le1/20$，
所以圆 $|z-z_0|=\rho$ 包含在 $|z|\le13/20<8/11$ 内。

对任意复 $\alpha$，基本圆平均公式给
$$
\frac1{2\pi}\int_0^{2\pi}
 \log|z_0+\rho e^{it}-\alpha|\,dt
=\log\max(\rho,|z_0-\alpha|)\ge\log\rho.
$$
此式由圆内、圆外分别展开 $\log(1-w)$ 并取实部平均得到；
零点落在圆上时按可积极限成立。
紧内 Blaschke 因子的分母模不超过 $2$。
因此圆平均给
$$
\frac1{2\pi}\int_0^{2\pi}
 \log|I_{\rm in}(z_0+\rho e^{it})|\,dt
\ge-r\log(2/\rho).
$$
于是至少有一点 $z$ 在该圆上满足
$$
\boxed{
|b(z)|\ge\exp[-A-r\log(2/\rho)].
}
\tag{4.6}
$$
这一步保留了全部紧内零点，不要求某个预选点恰好避开它们。

对逐块序列，$A_i=o(\sqrt{q_i})$、
$r_i=o(\sqrt{q_i})$。
故 (4.6) 的负对数是 $o(q_i)$，
即使紧内零点非常靠近 $z_0$ 也成立。

## 5. 标量下界准确返回原收缩矩阵

仍取第4节找到的 $z$。令
$$
\overline s=\frac{z}{2+3z}.
$$
因为 $|z+3/5|\le1/20<1/15$，分母不为零。
在极化公式 (2.5) 中取 $t=-3$，
则
$$
\frac{2\overline s}{1-3\overline s}=z.
$$
其归一化核的绝对平方准确为
$$
\begin{aligned}
\frac{|1-3\overline s|^2}{10(1+|s|^2)}
&=\frac4{10(|2+3z|^2+|z|^2)}\\
&=\frac1{1+25|z+3/5|^2}
=\frac1{1+25\rho^2}.
\end{aligned}
\tag{5.1}
$$
于是由 (2.5)、(4.6) 和 $\|\Omega_s\|=1$，
$$
\begin{aligned}
\|R\Omega_{-3}\|
&\ge|\langle R\Omega_{-3},\Omega_s\rangle|\\
&\ge(1+25\rho^2)^{-q/2}
 \exp[-A-r\log(2/\rho)].
\end{aligned}
$$
取 $\rho=q^{-1/4}$、用 $\log(1+y)\le y$，得到明确下界
$$
\boxed{
\|R_i\Omega_{-3}\|
\ge e^{-\Gamma_i},
}
\tag{5.2}
$$
$$
\Gamma_i=
\frac{1862}{3}\ell_i\sqrt{q_i}
+r_i\log(2q_i^{1/4})
+\frac{25}{2}\sqrt{q_i}
=o(q_i).
\tag{5.3}
$$
上界为 $\|R_i\|\le1$，因此
$$
\boxed{
\frac1{q_i}\log\|R_i\Omega_{-3}\|\longrightarrow0.
}
\tag{5.4}
$$
这是原真实矩阵 $R_i$ 的结论。
没有用 $b_i(T_i)$ 代替它，
也没有要求 $R_i$ 关于位排列对称。

## 6. 固定正常态的完整有限 Gram

当测试列 $u$ 只支持于 $B_i$，纯矩是一个完整块线性泛函。
对任意 $F\subseteq B_i$，
$$
\langle D_F\chi_{B_i},\chi_{B_i}\rangle=2^{|F|}.
$$
真空与完整块的交叉项只有 $F=B_i$ 时非零，
而 $q_i$ 为偶数，所以两个交叉项均为 $1$。
因此其完整矩向量准确为
$$
\boxed{
m_i=(\lambda-c_i^2)\Omega
 +2c_i\chi_{B_i}
 +c_i^2D_{B_i}^*\chi_{B_i},
\qquad
\phi_f(X_u^0)=\langle u,m_i\rangle.
}
\tag{6.1}
$$
这包含所有 $2^{q_i}$ 个列，不只对角元或固定次数截断。
例如空列的系数是
$(\lambda-c_i^2)+c_i^2=\lambda$，符合 $\phi_f(I)=\lambda$。

令 $C$ 为纯反射共轭，
$$
C\Omega=\Omega,\qquad C\chi_F=(-1)^{|F|}\chi_F
$$
并对系数共轭。
每个 $E_j$ 满足 $CE_j^*C=E_j$；
交换性给整个 $\mathcal A_q^0$ 的 $C$ 对称：
$$
CR^*C=R.
\tag{6.2}
$$
由于 $q_i$ 偶数，
$C\chi_{B_i}=\chi_{B_i}$，
所以
$$
\|R_i^*D_{B_i}^*\chi_{B_i}\|
=\|R_iD_{B_i}\chi_{B_i}\|.
$$
而逐坐标
$$
D\chi=2\chi-\Omega_+
=\frac{|0\rangle-3|1\rangle}{\sqrt2}
=\sqrt5\,
 \frac{|0\rangle-3|1\rangle}{\sqrt{10}}.
$$
因此
$$
\boxed{
\|R_i^*D_{B_i}^*\chi_{B_i}\|
=5^{q_i/2}\|R_i\Omega_{-3}\|.
}
\tag{6.3}
$$

记
$$
a_i=\|R_i^*m_i\|.
$$
由 $\|R_i^*\|\le1$、(5.2) 和 (6.1)，
$$
c_i^2\,5^{q_i/2}e^{-\Gamma_i}-(\lambda+2c_i)
\le a_i
\le c_i^2\,5^{q_i/2}+\lambda+2c_i.
\tag{6.4}
$$
$c_i^2=1/(16\sqrt{q_i})$、$\Gamma_i=o(q_i)$，
所以
$$
\boxed{
\lim_{i\to\infty}\frac{\log a_i}{q_i}
=\frac{\log5}{2}.
}
\tag{6.5}
$$

这里 $a_i$ 就是整个纯有限 Gram 的准确对偶范数：
$$
\boxed{
\sup_{u\ne0}
 \frac{|\phi_f(X_u^0)|}{\|U_iu\|}
=\|R_i^*m_i\|=a_i.
}
\tag{6.6}
$$
证明只需令 $u=R_iw$，
则 $\|U_iu\|=\|w\|$，
而 $\langle u,m_i\rangle=\langle w,R_i^*m_i\rangle$，
再用 Hilbert 空间的 Riesz 对偶。

对充分大 $i$，$a_i>0$。
取准确最优列
$$
\boxed{
w_i=\frac{R_i^*m_i}{a_i},\qquad
u_i=R_iw_i.
}
\tag{6.7}
$$
于是
$$
\|w_i\|=1,\qquad
\|u_i\|\le1,\qquad
U_iu_i=w_i,\qquad
\phi_f(X_{u_i}^0)=a_i>0.
\tag{6.8}
$$
这些是完整块中实际存在的有限 Walsh 向量。
$u_i$ 可以使用所有次数，不要求对称层或分母消去。

## 7. 完整实际 carry 与同一个最小逆

因为 $\|u_i\|\le1$，
全部 Walsh 系数满足
$$
\sum_{F\subseteq B_i}|(u_i)_F|\le2^{q_i/2}.
$$
在每一 $F$ 上使用 (1.3) 的完整 telescoping，
得到
$$
\boxed{
\Delta_i:=\|X_{u_i}-X_{u_i}^0\|
\le8q_i(3\sqrt2)^{q_i}\eta_{\min B_i}
\le\frac{\varepsilon_i}{2n_i}
 \left(\frac{3\sqrt2}{5}\right)^{q_i}\longrightarrow0.
}
\tag{7.1}
$$
因此完整块高次数成本确由原 (1.5) 支付。

纯块代数交换，且 $U_i=X_{g_i}^0$，所以
$$
X_{u_i}^0g_i=U_iu_i=w_i.
$$
准确源张量分解因而给
$$
\boxed{
\|X_{u_i}^0g\|=\frac{\|g\|}{n_i}.
}
\tag{7.2}
$$
这里正缩放 $1-\varepsilon_i$ 在块内与块外范数比中准确抵消；
没有把实际源列改为未缩放的纯乘积。

由 (1.7)、(7.1)--(7.2)，
$$
\left|\|Gu_i\|-\frac{\|g\|}{n_i}\right|
\le\Delta_i\|g\|.
$$
$n_i\to1$，于是
$$
\boxed{\|Gu_i\|\longrightarrow\|g\|>0.}
\tag{7.3}
$$
实际矩同样满足
$$
|\phi_f(X_{u_i})-a_i|\le\lambda\Delta_i\longrightarrow0.
$$
结合 (6.5)，得到本稿最终实际结论
$$
\boxed{
\lim_{i\to\infty}\frac1{q_i}
 \log\frac{|\phi_f(X_{u_i})|}{\|Gu_i\|}
=\frac{\log5}{2}>0.
}
\tag{7.4}
$$
同一个 $P$、同一个 $g$、同一个 $G$、
同一个 $f$ 和同一分块完成了全部配对。
没有为不同列更换正则器。

## 8. 有限个完整逆源组合：用共同前向积

上述结论还覆盖同一分块上有限个完整成功源
$g^{(\nu)}$，$\nu=1,\ldots,K$。
每支允许任意纯收缩
$R_{i,\nu}\in\mathcal A_{q_i}^0$。
假设
$$
g=\sum_{\nu=1}^K z_\nu g^{(\nu)}
$$
确为某个合格 $P$ 的 $P^{-1}1$。

不要求这些分支的共同逆源另行收敛。
直接取共同前向积
$$
S_i=\prod_{\nu=1}^K R_{i,\nu}.
$$
它为可逆收缩，仍在同一个纯交换块代数中。
每支源收敛给 $R_{i,\nu}\Omega\to\Omega$；
望远镜和收缩性给
$$
\|S_i\Omega-\Omega\|
\le\sum_{\nu=1}^K\|R_{i,\nu}\Omega-\Omega\|\longrightarrow0.
$$
所以第2至6节的纯 Gram 结论适用于 $S_i$：
$$
\frac1{q_i}\log\|S_i^*m_i\|\longrightarrow\frac{\log5}{2}.
$$

取
$$
w_i=\frac{S_i^*m_i}{\|S_i^*m_i\|},\qquad u_i=S_iw_i.
$$
$\|u_i\|\le1$，纯矩准确为 $\|S_i^*m_i\|$。
对每一支，由交换性，
$$
U_{i,\nu}u_i
=\prod_{\mu\ne\nu}R_{i,\mu}w_i,
\qquad \|U_{i,\nu}u_i\|\le1.
$$
准确块源分解和有限三角和因而给
$$
\|X_{u_i}^0g\|
\le\sum_{\nu=1}^K|z_\nu|\|g^{(\nu)}\|.
$$
实际 carry 仍由 (7.1) 支付。
所以 $\|Gu_i\|$ 一致有界，而实际矩具有指数 $(\log5)/2$。
至少有
$$
\liminf_i\frac1{q_i}
 \log\frac{|\phi_f(X_{u_i})|}{\|Gu_i\|}
\ge\frac{\log5}{2}.
$$

这里组合完整逆源；共同的是前向收缩积，
并未声称正则器之和的逆等于逆源之和。

## 9. 新边界与真正湮灭矩剩余问题

本稿的范围是整个纯有限交换块代数，
已经包含：

- 任意单变量 $p(T_q)$ 收缩，无论原 $p$ 是否有 Schur 延拓；
- 任意非对称多变量块多项式及其纯逆，只要前向为收缩；
- 任意逐块因子化、因子数和相位；
- 同一分块上有限个完整成功逆源的线性组合。

所需的实际前提仍是 (1.4)--(1.7)。
没有真空原像或没有这类 disjoint 有限块逆源结构的前向族不在结论中。
更一般的非块正则器也未被自动包含。

固定测试态 $f$ 已经被正锥结论排除为湮灭者。
(7.4) 因而是整个块逆源构造的适用边界，
并不排除真正湮灭正常态。
真正的后续问题是：
对湮灭关系选出的实际完整矩向量，
是否能构造专属 $P$ 使全部有限 Gram 的对偶范数一致有界；
或者找到其不可避免的类似相干方向下界。
不能把本稿非湮灭态的特定 $D_B^*\chi_B$ 分量凭空加到未知见证中。

完整依赖：

- [R244 聚合逆图和完整有限列核心](../results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)；
- [任意 Schur 块的径向、零点和调和预算](2026-11-13-all-schur-block-inverse-sources-and-universal-large-column-obstruction-normal-complex.md)（本稿第4节已完整重列所用部分）；
- [负实边界准确 Gram 与实际全块 carry](2026-11-13-signed-real-and-complex-sector-blaschke-large-column-obstruction-normal-complex.md)。

本稿第2、3、5节专门证明协变符号与原矩阵之间的两个方向，
避免把“有限矩阵收缩”误当成“原标量函数为 Schur”。
