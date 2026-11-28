# R1154：原 Gaussian 首标签与指定 minor 的同源有限 Gauss 约束

日期：2026-11-28（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

**已证明，纯纸面。** 本篇继续
[R1135 §§16–17](R1135-original-Gaussian-low-row-fiber-constraint.md)
的同一个原 Gaussian 点、Hasse 参数和有限 Gauss 对。
新支付三件事：原首个 affine 标签的 $\mathcal H_p$ 也由这一对读取；
原 Hasse 六次列反序后，两种 $p\bmod12$ 分支具有同一个准确的
模 $x^p$ 超几何来源；指定 minor 的两条共同边界项严格相消。
所得是原 $\mathcal H_p$ 与 $\Delta_{\rm low}$ 的联合约束，
并非它们不能同时为零的结论。

实际标签的 Bernoulli mask、两 twist 在同一 coarse component 内的
统一、以及 $S=0,P=0$ 边界仍按 R1135 原式保留。
本篇不以一个非零端点、零带或非零多项式替代指定 moment 非零。

## 1. 同一原曲线与有限输入

设 $p=4k+3\ge41$，原 Gaussian 曲线为
$y^2=x^3+a_{\rm G}x$，$a_{\rm G}\in\mathbf F_p^\times$。
在 R1135 的固定判别式曲线上，写
$$
\begin{gathered}
r=-\frac43a_{\rm G},\qquad
Y^2=X^3-r^3,\qquad T_{\rm G}=(r,0),\\
D X=2Y,\quad D Y=3X^2,\quad
\omega_\Delta=\frac{dX}{2Y}=\frac{dY}{3X^2},\\
u=\mathsf A=E_{p-1}\bmod p,\qquad
\beta(u)=D\mathsf A,\qquad
\beta_{\rm G}=\beta(T_{\rm G})=-\delta\ne0.
\end{gathered}
\tag{1154.1}
$$
这里 $u$ 是 Hasse 局部参数，$\beta_{\rm G}$ 不是 torsion-root；
$D=6b\partial_a-4a^2\partial_b/3$ 始终是原 Serre 向量场。
令 $\ell$ 是 (1135.82) 的有限偶伴随解，
$\ell(0)=1$，并置
$$
x=-\frac{Y^2}{r^3},\qquad
X=r(1-x)^{1/3},\qquad
\kappa=\frac{\beta_{\rm G}}{3r^2}.
$$
本篇的 $x$ 是这个局部变量，不是原曲线的 $x$ 坐标。

写
$$
(p,\epsilon)=(12n+7,0)\ \hbox{或}\ (12n+11,1),
\qquad N=\frac{p-7}{2}=6n+2\epsilon.
$$
$N$ 为偶数。原安全解及 Hasse 列为
$$
\begin{aligned}
L(x)&={}_2F_1(1/12,1/12;1/2;x),\\
Q(x)&={}_2F_1(7/12,7/12;3/2;x),\\
P_n(x)&={}_2F_1(-n,-n;3/2;x),\\
L_n(x)&={}_2F_1(-n-1/2,-n-1/2;1/2;x),
\end{aligned}
$$
$$
\boxed{\quad
\ell(u(Y))=L(x),\quad
u=\kappa YQ(x),\quad
Q=(1-x)^{\epsilon/3}P_n,\quad
L=(1-x)^{\epsilon/3}L_n.
\quad}
\tag{1154.2}
$$
含 $L$ 的式子只使用至 $x^{N+1}$ 的安全前缀；
含 $Q$ 的第二、第三式是已由原 Hasse 次数支付的代数式。
所有分数幂取常数项一。记
$$
\boxed{\quad
T(x)=Q^6=(1-x)^{2\epsilon}P_n^6,\quad
\deg T=N,\quad
t_N=[x^N]T=
 \left(\frac{n!}{(3/2)_n}\right)^6\ne0.
\quad}
\tag{1154.3}
$$
同时保留 R1135 的三个有限系数
$$
\begin{aligned}
b_N&=[x^{N+1}]Q^4L^2,\\
c_N&=[x^N](1-x)^{2/3}Q^6L(Q+2xQ'),\\
d_N&=[x^{N+1}](1-x)^{2/3}Q^4L^3(Q+2xQ').
\end{aligned}
\tag{1154.4}
$$
它们不是原 Kronecker 的 $c_s,d_s$。
已经支付的实际尺度是
$$
\Delta_{\rm low}
=\frac{8}{4455\,r\beta_{\rm G}^2}
       (3b_Nc_N-t_Nd_N).
\tag{1154.5}
$$

## 2. 首个 affine 标签也由同一个 forcing 读取

原
[R1082 (1082.21)](R1082-original-Gaussian-high-Hurwitz-and-complete-short-convolution.md)
给
$$
\mathcal H_p=\frac25(DG_{p-5})(T_{\rm G}).
\tag{1154.6}
$$
这是先在通用模参数上求热导数、再特化的身份。
不对仅在 Hasse 零集上成立的反射值式求导。

这里把 R1135 的原 forcing 论证准确延至 $r=5$。
固定同一 Eisenstein 规范
$$
\mathcal E_j=-\frac{B_j}{2j}+\sum_{m\ge1}\sigma_{j-1}(m)q^m,
\qquad G_j=\frac{2\mathcal E_j}{(j-1)!},
\qquad
\mathcal E_6=-\frac{12b}{7}=\frac{3Y}{7}.
$$
逐 Fourier 系数的
$m^5\sigma_{-5}(m)=\sigma_5(m)$（$p\nmid m$）
及完整 $p$-depletion 给
$$
\theta^5G_{p-5}
=\frac{2}{(p-6)!}
       \bigl(\mathsf A^6\mathcal E_6-\mathcal E_6^p\bigr).
$$
两边权都是 $6p$，常数是 $c-c^p=0$。
原 $U_p=1$ 还给
$\Pi_0(G_{p-5}/\mathsf A^5)=(G_{p-5}/\mathsf A)^p$。
因此与 (1135.76) 完全同源的无分母式为
$$
u^{2p-5}G_{p-5}-u^pG_{p-5}^p
=\frac{2}{(p-6)!}\,
       \mathcal B^{p-6}(u^6\mathcal E_6),
\qquad \mathcal B=u^2D.
\tag{1154.7}
$$
没有另选 Frobenius 常数。

置 $\xi=u/\ell(u)$。
由原
$\mathcal B=\beta_{\rm G}\xi^2d/d\xi+
O(\xi^{p+3})d/d\xi$，
(1154.7) 中一次误差的最低总次数为 $2p+1$。
读取 $\xi^{2p-4}$，Frobenius 那项没有贡献。
同 (1135.87) 的 Wilson/Lagrange 计算给
$$
\begin{gathered}
J_{5,1}=[u^{p-4}]
          \frac{\mathcal E_6(u)}{\beta(u)}\ell(u),\\
[\xi]\left(\frac{\xi}{u}\right)^5G_{p-5}
=-10\beta_{\rm G}^{-4}J_{5,1}.
\end{gathered}
\tag{1154.8}
$$
由于 $G_{p-5}$ 为奇、$\ell$ 为偶，左边正是
$[u]G_{p-5}$；于是
$$
\boxed{\quad
\mathcal H_p=-4\beta_{\rm G}^{-3}J_{5,1}.
\quad}
\tag{1154.9}
$$
所需最高的 $\ell$ 次数是 $p-5$。
这一步没有越过 §1 的安全前缀。

定义同一 Gauss 对的系数
$$
E_H=[x^{N+1}](1-x)^{-2/3}Q^3L.
\tag{1154.10}
$$
用 $\mathcal E_6\omega_\Delta=Y\,dY/(7X^2)$，
(1154.8) 的实际 residue 变成
$$
\frac{\kappa^2}{7r^2}\,
Y^{4-p}(1-x)^{-2/3}Q^3L\,dY.
$$
这里 $\kappa^{3-p}=\kappa^2$；
$Q^{-p}$ 在本次低于 $p$ 的系数中只有常数一。
因为 $p-5=2(N+1)$、$N+1$ 为奇，准确得到
$$
J_{5,1}
=-\frac{\kappa^2}{7r^{3N+5}}E_H.
$$
令 $\varepsilon_r=r^{(p-1)/2}\in\{1,-1\}$。
由 $3N+9=3(p-1)/2$，最终尺度是
$$
\boxed{\quad
\mathcal H_p
=\frac{4}{63\,\beta_{\rm G}\,r^{3N+9}}E_H
=\frac{4\varepsilon_r}{63\beta_{\rm G}}E_H .
\quad}
\tag{1154.11}
$$
全过程仍在 $Y$ 中读取 residue。
由 $Y^2$ 换到 $x$ 时只换系数，没有多除一个二。

## 3. 同一 Wronskian 将首标签变为准确的二次 moment

置
$$
R_0(x)=\frac{L(x)}{Q(x)},\qquad
S_0(x)=R_0(x)^2.
$$
$Q(0)=1$，所以这两个商在全部所需范围内有唯一安全前缀。
(1135.99) 直接给
$$
\boxed{\quad
R_0-2xR_0'=(1-x)^{-2/3}Q^{-2}.
\quad}
\tag{1154.12}
$$
因此 (1154.10) 具有两个完全相等的读法：
$$
\boxed{\begin{aligned}
E_H
&=[x^{N+1}]T(S_0-xS_0')\\
&=[x^{N+1}](xT'-NT)S_0.
\end{aligned}}
\tag{1154.13}
$$
第二式是有限系数分部积分：
$[x^{N+1}](xTS_0)'=(N+2)[x^{N+1}]TS_0$；
等价地
$[x^{N+1}]x(TS_0)'=(N+1)[x^{N+1}]TS_0$。
保留 $xT'$ 项后即得所示 $-N$，没有以普通求导杀掉整个乘积。

这使原 $\mathcal H_p=0$ 成为与 (1154.5) 同源的确切约束；
它不是从四个有限数中另定义一个替代标签。

## 4. 反序 Hasse 列的共同 Gauss 来源及完整零带

令
$$
q_n=[x^n]P_n=\frac{n!}{(3/2)_n},\qquad
\widehat P_n(y)=q_n^{-1}y^nP_n(1/y).
$$
直接比较第 $n-j$ 项与最高项，有
$$
\frac{[x^{n-j}]P_n}{q_n}
=\frac{(-n)_j(-n-1/2)_j}{(j!)^2}
\quad(0\le j\le n).
$$
故这是一个精确的终止多项式身份：
$$
\boxed{\quad
\widehat P_n(y)
={}_2F_1(-n,-n-1/2;1;y).
\quad}
\tag{1154.14}
$$
相应地，令
$$
\widehat T(y)=t_N^{-1}y^NT(1/y)
=(1-y)^{2\epsilon}\widehat P_n(y)^6.
$$

定义只消费 $0\le j<p$ 系数的
$$
\mathfrak G(y)={}_2F_1(1/12,7/12;1;y).
$$
这些系数的分母是 $(j!)^2$ 及 $12$ 的幂，全部为单位。
当 $p=12n+7$，(1154.14) 的两个上参数正同余于
$7/12,1/12$，所以 $\widehat P_n=\mathfrak G\bmod y^p$。
当 $p=12n+11$，上参数同余于 $11/12,5/12$；
Euler 的原有理级数恒等式在这个安全范围准确给
$$
{}_2F_1(11/12,5/12;1;y)
=(1-y)^{-1/3}\mathfrak G(y).
$$
取六次幂后，前面的 $(1-y)^2$ 正好抵消。
所以两种分支统一为
$$
\boxed{\quad
\widehat T(y)\equiv\mathfrak G(y)^6\pmod{y^p}.
\quad}
\tag{1154.15}
$$
这里只声明模 $y^p$ 的恒等式。
没有将含 $p!$ 的更高 Gauss 系数约化，也没有把原伴随解宣为无限整级数。

由于 $\widehat T$ 是次数恰为 $N$ 的多项式，
(1154.15) 还支付完整零带
$$
\boxed{\quad
[y^j]\mathfrak G(y)^6=0
\qquad (N<j<p).
\quad}
\tag{1154.16}
$$
这是原 Hasse 次数给出的具体恒等式，而非任意超几何截断规则。
其第一个非恒定系数是
$$
\widehat T_1=[y]\mathfrak G^6
=6\cdot\frac7{144}=\frac7{24}\ne0.
$$
由此
$$
\boxed{\quad
\deg(xT'-NT)=N-1,\qquad
[x^{N-1}](xT'-NT)=-\frac7{24}t_N\ne0.
\quad}
\tag{1154.17}
$$
$N=(p-7)/2<p$，最高项的消去与下一项的非消去都准确，
不把这个多项式的非零性误作 (1154.13) 的 moment 非零。

写 $S_0(x)=\sum s_jx^j$、$\widehat T(y)=\sum_{j=0}^N\widehat t_jy^j$。
同一实际两个系数因而可写成
$$
\boxed{\begin{aligned}
b_N&=t_N\sum_{j=0}^{N}\widehat t_j\,s_{j+1},\\
E_H&=-t_N\sum_{j=1}^{N}j\,\widehat t_j\,s_{j+1},
\qquad
\widehat t_j=[y^j]\mathfrak G(y)^6.
\end{aligned}}
\tag{1154.18}
$$
右边的 $s_j$ 始终来自 §1 的指定 $L/Q$；
它们不是可以任意选择的测试向量。
所有指标至多 $N+1=(p-5)/2$，仍在安全范围。

## 5. 原 minor 的两条共同边界准确抵消

再定义两个同源有限系数
$$
\begin{aligned}
e_N^\dagger&=[x^{N-1}](1-x)^{-1/3}Q^7L,\\
f_N^\dagger&=[x^N](1-x)^{-1/3}Q^5L^3.
\end{aligned}
\tag{1154.19}
$$
这里的 $e_N^\dagger,f_N^\dagger$ 不表示 j0 路线的 $e,f_N$。

令 $A_0(Y)=YQ(x)$、$\ell_0(Y)=L(x)$，prime 仅在本段表示 $d/dY$。
(1154.12) 给
$$
X^2(A_0'\ell_0-A_0\ell_0')=r^2
$$
在所需前缀中成立。两次直接乘积求导得到
$$
\begin{aligned}
8X^2A_0^6\ell_0A_0'
 &=X^2(A_0^7\ell_0)'+r^2A_0^6,\\
8X^2A_0^4\ell_0^3A_0'
 &=X^2(A_0^5\ell_0^3)'+3r^2A_0^4\ell_0^2.
\end{aligned}
\tag{1154.20}
$$
读取 $Y^{p-1}$。
对任意本次有限 jet $V(Y)$，
$$
[Y^{p-1}](X^2V)'=p[Y^p](X^2V)=0,
\qquad
(X^2)'=\frac{4Y}{3X}.
$$
所以第一式的导数项转为
$-\frac43[Y^{p-1}]Y A_0^7\ell_0/X$，
第二式转为
$-\frac43[Y^{p-1}]Y A_0^5\ell_0^3/X$。
这个求导恒等式不读取未知的 $[Y^p]V$ 数值；
它的系数乘 $p$，准确为零。

在 (1154.20) 第二式中，Wronskian 的最低外乘阶为四；
因此只需它至 $Y^{p-5}$，恰在 §1 已付范围内。
所有乘积中 $\ell_0$ 的所需次数也至多 $p-5$。
再用 $N$ 偶、$N-1,N+1$ 奇的实际 $Y$ 系数换算，得到
$$
\boxed{\quad
c_N=\frac{t_N}{8}+\frac{e_N^\dagger}{6},
\qquad
d_N=\frac{3b_N}{8}+\frac{f_N^\dagger}{6}.
\quad}
\tag{1154.21}
$$
例如第一式中
$[Y^{p-1}]X^2A_0^6\ell_0A_0'
=r^{2-3N}c_N$，
而
$[Y^{p-1}]Y A_0^7\ell_0/X
=-r^{2-3N}e_N^\dagger$，
准确给 $+e_N^\dagger/6$。
第二式的共同尺度是 $-r^{-3N-1}$，同样给
$+f_N^\dagger/6$。

因此两条边界项 $3b_Nt_N/8$ 完整抵消，留下
$$
\boxed{\begin{aligned}
3b_Nc_N-t_Nd_N
 &=\frac{3b_Ne_N^\dagger-t_Nf_N^\dagger}{6},\\
\Delta_{\rm low}
 &=\frac{4}{13365\,r\beta_{\rm G}^2}
       (3b_Ne_N^\dagger-t_Nf_N^\dagger).
\end{aligned}}
\tag{1154.22}
$$
$13365=3^5\cdot5\cdot11$ 在本范围为单位。
这是真正的同一乘积边界消去，
仍保留 $e_N^\dagger,f_N^\dagger$ 全项。

## 6. 原 actual good mask 下的联合结论

所有恒等式均来自原 Gaussian 输入，不需要先假设某个 Bernoulli 数为单位。
但将它们用于标签分离时，仍按实际出现条件取行。

若 $p\mid B_{p-3}$，
[R1127](R1127-original-Gaussian-irregular-complement-and-affine-cuspidal-label.md)
的原 $\omega^2$ 补支已经有 affine 单位行。
若 $p\nmid B_{p-3}$，原高角色 $R=p-3$ 是 good，
且 R1082 的准确斜率给：
同一原 Gaussian coarse component 内的一个非对角共同纤维
必须满足 $\mathcal H_p=0$。
由 (1154.11)、(1154.18)，这准确强迫
$$
\sum_{j=1}^{N}j\,\widehat t_j\,s_{j+1}=0.
\tag{1154.23}
$$

进一步，在 R1135 §3 的分支
$p\mid B_{p-7}$、$p\nmid B_{p-5}$，
两条实际 good 行 $R=4,p-5$ 的 degree-one 组合斜率
是单位尺度乘 $\Delta_{\rm low}$。
所以同一个非对角共同纤维还必须满足
$$
\boxed{\quad
\sum_{j=1}^{N}j\,\widehat t_j\,s_{j+1}=0,
\qquad
f_N^\dagger
=3e_N^\dagger\sum_{j=0}^{N}\widehat t_j\,s_{j+1}.
\quad}
\tag{1154.24}
$$
这里准确约去了已证明的 $t_N\ne0$，
没有约去 $e_N^\dagger$、$b_N$ 或任一尚未证明为单位的数。

在 $p\mid B_{p-5}$ 时，不把不存在的 $R=p-5$ 行补进 mask；
(1154.22) 仍是原函数身份，但不自动提供这个标签约束。
R1135 的其他实际行与唯一候选点对仍完整保留。
本篇没有证明 (1154.24) 不可能，也没有从行数或反序零带
推出实际 good 子代数已是 $\mathbf F_p[z]$。

新增的已闭来源是：
原 $\mathcal H_p$ 与指定 minor 使用同一个有限 Gauss 对；
原 Hasse 反序列有 (1154.15)–(1154.17) 的统一精确前缀和零带；
原 minor 有 (1154.20)–(1154.22) 的完整边界抵消。
后续仍须控制这同一指定输入的联合 moment，
或给出另一条确实出现的 good 行来分离原余对。
全篇没有数学程序执行或 prime 窗口重扫。


## 7. 同一 Gauss 对的 Legendre 多项式与有限对数

本节继续 (1154.2) 的同一局部解，不新增同源或参考点。
只在形式换元时加入 $v$，满足 $v^2=r$，并取
$$
w=\frac{Y}{X^{3/2}},\qquad
X=r(1-w^2)^{-1/3},\qquad
Y=rv\,w(1-w^2)^{-1/2}.
$$
$X^{3/2}$ 的常数项取 $rv$。于是
$$
x=-\frac{w^2}{1-w^2},\qquad
\omega_\Delta=\frac1{3v}(1-w^2)^{-5/6}\,dw.
\tag{1154.25}
$$
这个 $w$ 不是原 Gaussian profile 的 gauge 参数。
最后的标量全下降到 $\mathbf F_p$；换 $v$ 的符号只把 $w$ 换为 $-w$，
不会改变下面的偶系数。

令
$$
\nu=2n+1=
\begin{cases}
(p-1)/6,&\epsilon=0,\\
(p-5)/6,&\epsilon=1.
\end{cases}
$$
它是小于 $p$ 的奇整数，且
$\nu(\nu+1)=-5/36\bmod p$。
用标准 Legendre 递推定义多项式 $\mathsf P_d$：
$$
\mathsf P_0=1,\quad \mathsf P_1=w,\qquad
(d+1)\mathsf P_{d+1}
=(2d+1)w\mathsf P_d-d\mathsf P_{d-1}.
$$
本篇只需 $0\le d\le\nu$；这些分母均为单位。
其原规范是 $\mathsf P_d(1)=1$。
置
$$
a_\nu=\mathsf P_\nu'(0)
=(-1)^n\frac{(3/2)_n}{n!}\ne0,\qquad
\mathsf o(w)=\frac{\mathsf P_\nu(w)}{a_\nu},
$$
$$
\mathsf W_{\nu-1}(w)=
\sum_{j=1}^{\nu}\frac{\mathsf P_{j-1}(w)\mathsf P_{\nu-j}(w)}j,
\qquad
\mathcal L_p(w)=
\sum_{j=0}^{(p-3)/2}\frac{w^{2j+1}}{2j+1}.
$$
所有 $\mathcal L_p$ 的分母也严格小于 $p$。
定义
$$
\boxed{\quad
\mathsf e(w)=
a_\nu\mathsf W_{\nu-1}(w)
-a_\nu\mathsf P_\nu(w)\mathcal L_p(w).
\quad}
\tag{1154.26}
$$
$\mathsf o$ 为奇、首项 $w$；
$\mathsf e$ 为偶、常数项一。
(1154.26) 只作为原偶解的安全有限前缀使用，
不把右边的高次多项式项称为原无限伴随解。

这里的 Legendre companion 公式可自足证明。
在 characteristic zero 中先用
$\operatorname{atanh}w=\sum w^{2j+1}/(2j+1)$。
由 $\sum_{d\ge0}\mathsf P_d t^d=(1-2wt+t^2)^{-1/2}$，
上面 $\mathsf W$ 的生成函数是
$$
\sum_{d\ge1}\mathsf W_{d-1}t^d
=(1-2wt+t^2)^{-1/2}
  \int_0^t(1-2ws+s^2)^{-1/2}\,ds.
$$
对 $t$ 求导给与 $\mathsf P_d$ 相同的三项递推（递推指标 $d\ge1$），
初值为 $\mathsf W_{-1}=0,\mathsf W_0=1$。
因此
$\mathsf Q_d=\mathsf P_d\operatorname{atanh}w-\mathsf W_{d-1}$
具有初值
$\mathsf Q_0=\operatorname{atanh}w$、
$\mathsf Q_1=w\operatorname{atanh}w-1$，
并满足同一 Legendre 方程
$$
(1-w^2)h''-2wh'+d(d+1)h=0.
$$
这也可由三项递推及
$(1-w^2)\mathsf Q_d'=d(\mathsf Q_{d-1}-w\mathsf Q_d)$
直接归纳；$d=1$ 的式子由所列初值核定。

Wronskian 是常数除以 $1-w^2$。
把对数项相消后在 $w=1$ 读取，因 $\mathsf P_\nu(1)=1$，
该常数准确为 $-1$：
$$
(1-w^2)(\mathsf P_\nu'\mathsf Q_\nu
                     -\mathsf P_\nu\mathsf Q_\nu')=-1.
$$
在 $w=0$ 读取又得
$\mathsf W_{\nu-1}(0)=a_\nu^{-1}$。
因此在未截断的安全前缀中，
$-a_\nu\mathsf Q_\nu$ 正是所需偶初值解。
对已经定义的有限 $\mathsf e$，保留
$\mathcal L_p'=(1-w^{p-1})/(1-w^2)$ 后，完整式是
$$
\boxed{\quad
(1-w^2)(\mathsf o'\mathsf e-\mathsf o\mathsf e')
=1-w^{p-1}\mathsf P_\nu(w)^2
\equiv1\pmod{w^{p+1}}.
\quad}
\tag{1154.27}
$$
所以只约化至所用的 $w^{p-5}$，把 $\operatorname{atanh}$ 换成
$\mathcal L_p$ 完全合法；首个被排除的对数分母在 $w^p$，
乘奇 $\mathsf P_\nu$ 后还更高。
上式仍显示完整 finite-log carry，不将有限多项式的
Wronskian 在全部次数上误写成常数。

令
$$
c=\frac{\beta_{\rm G}}{3v},\qquad
\Lambda(w)=(1-w^2)^{-(p-1)/12}.
$$
对 (1154.2) 的 $P_n,L_n$ 作 Pfaff 变换，准确得到
$$
\boxed{\quad
u=c\Lambda(w)\mathsf o(w),\qquad
\ell(u(w))=\Lambda(w)\mathsf e(w),
\qquad c^p=\varepsilon_r c.
\quad}
\tag{1154.28}
$$
例如 $P_n$ 变成
$(1-w^2)^{-n}{}_2F_1(-n,n+3/2;3/2;w^2)$；
再乘 $Y$ 和 $(1-x)^{\epsilon/3}$ 后，
共同指数为 $-n-1/2-\epsilon/3=-(p-1)/12$。
偶解同样变成
$\,{}_2F_1(-n-1/2,n+1;1/2;w^2)$。
它们正是上述奇、偶 Legendre 初值解。
$u$ 一列仍来自原 Hasse；$\ell$ 一列只使用安全前缀。
$v^p=\varepsilon_r v$ 给最后一个准确相位，不把 $v$ 强行放入 $\mathbf F_p$。

## 8. 五个 Legendre moments 的完整原尺度

为避免与 §1 的 $t_N,b_N$ 混同，用不同字体定义
$$
\begin{aligned}
\mathsf t&=[w^{p-1}]\frac{\mathsf o^6}{1-w^2},&
\mathsf b&=[w^{p-1}]\frac{\mathsf o^4\mathsf e^2}{1-w^2},\\
\mathsf u&=[w^{p-1}]\frac{w\mathsf o^7\mathsf e}{1-w^2},&
\mathsf v&=[w^{p-1}]\frac{w\mathsf o^5\mathsf e^3}{1-w^2},\\
\mathsf h&=[w^{p-1}]\frac{w\mathsf o^3\mathsf e}{1-w^2}.&&
\end{aligned}
\tag{1154.29}
$$
$\mathsf e$ 实际所需的最高次数仍是 $p-5$。
此外
$$
\deg\mathsf o^6=6\nu=p-1-4\epsilon.
$$
$\mathsf o^6$ 为偶多项式，故这次有限求和准确给
$$
\boxed{\quad
\mathsf t=\mathsf o(1)^6=a_\nu^{-6}\ne0.
\quad}
\tag{1154.30}
$$
这是原已知单位端点的 Legendre 读法，不是新的 minor 单位断言。

全部原 residue 可直接在 (1154.28) 中换元。
有
$$
\mathcal E_6=\frac{3rv}{7}\,w(1-w^2)^{-1/2},
\qquad
\mathcal E_8=\frac{27r^2}{10}(1-w^2)^{-2/3}.
$$
例如 $J_{7,0}$ 的 integrand 除常数外为
$$
(1-w^2)^{p(p-7)/12-1}
   \mathsf o^{\,6-p}\,dw.
$$
$\mathsf o/w$ 是偶单位级数。
所以在读取 $w^{p-1}$ 时，两个完整 Frobenius 因子
$(\mathsf o/w)^{-p}$ 和 $(1-w^2)^{p(p-7)/12}$
都只有常数一；没有跨过 $p$ 后作普通微分。
这给 $\mathsf t$，其常数是
$(9r^2/(10v))c^{6-p}
=\varepsilon_r\beta_{\rm G}^5/(270r)$。
另外两种 $J$ 完全同理，得到
$$
\boxed{\begin{aligned}
J_{5,1}&=\frac{\varepsilon_r\beta_{\rm G}^2}{63}\,\mathsf h,\\
J_{7,0}&=\frac{\varepsilon_r\beta_{\rm G}^5}{270r}\,\mathsf t,\\
J_{7,2}&=\frac{\varepsilon_r\beta_{\rm G}^3}{30}\,\mathsf b.
\end{aligned}}
\tag{1154.31}
$$

对 $\mathcal M_1,\mathcal M_3$，实际 $du$ 多出
$$
c\Lambda
\left(\mathsf o'
-\frac{w\mathsf o}{6(1-w^2)}\right)dw
\quad\bmod p
$$
而非单独的 $c\Lambda\mathsf o'\,dw$。
完整余下共同幂是 $(1-w^2)^{p(p-9)/12}$，
仍只贡献常数一。由 (1154.27) 与
$[w^{p-1}]V'=p[w^p]V=0$，有
$$
8[w^{p-1}]\mathsf o^6\mathsf e\,\mathsf o'=\mathsf t,
\qquad
8[w^{p-1}]\mathsf o^4\mathsf e^3\mathsf o'=3\mathsf b.
$$
因此原两条 $\mathcal E_8$ moments 准确为
$$
\boxed{\begin{aligned}
\mathcal M_1
&=\frac{\varepsilon_r\beta_{\rm G}^6}{270r}
      \left(\frac{\mathsf t}{8}-\frac{\mathsf u}{6}\right),\\
\mathcal M_3
&=\frac{\varepsilon_r\beta_{\rm G}^4}{30}
      \left(\frac{3\mathsf b}{8}-\frac{\mathsf v}{6}\right).
\end{aligned}}
\tag{1154.32}
$$
(1154.27) 的额外 carry 在这两次读取前分别至少乘上
$\mathsf o^6$、$\mathsf o^4$，总次数都严格大于 $p-1$，
故此次消失有准确次数界。所有原边界项均保留。
结合 (1135.90)、(1154.9)，最后得到
$$
\boxed{\quad
\mathcal H_p=-\frac{4\varepsilon_r}{63\beta_{\rm G}}\mathsf h,
\qquad
\Delta_{\rm low}
=\frac{4}{13365\,r\beta_{\rm G}^2}
       (3\mathsf b\mathsf u-\mathsf t\mathsf v).
\quad}
\tag{1154.33}
$$
这和 (1154.11)、(1154.22) 是同一原值的另一个完全定标读法。
负号由 (1154.25) 的真实换元决定，未把该二次扩域相位省略。

## 9. 原首标签的明确有限 harmonic 等式

记
$$
H_j=\sum_{i=1}^j\frac1i,\quad H_0=0,\qquad
h_{\rm odd}=\sum_{i=0}^{(p-3)/2}\frac1{2i+1},
\qquad
\mathsf P_\nu(w)^4=\sum_{s=0}^{2\nu}C_s w^{2s}.
\tag{1154.34}
$$
$2\nu<(p-1)/2$，所以所有这里的分母均为单位；
$\sum C_s=\mathsf P_\nu(1)^4=1$。

令
$$
\mathscr R(P)=[w^{p-1}]\frac{P(w)}{1-w^2},
\qquad
V_\nu(w)=\mathsf W_{\nu-1}(w)-\mathsf P_\nu(w)\mathcal L_p(w).
$$
由 (1154.26)，
$$
a_\nu^2\mathsf h
=\mathscr R\!\left(w\mathsf P_\nu^3V_\nu\right).
$$
其不含对数的部分 $w\mathsf P_\nu^3\mathsf W_{\nu-1}$
是次数至多 $4\nu<p-1$ 的偶多项式。因此该部分的读数正是
$\mathsf W_{\nu-1}(1)=H_\nu$。

对含对数部分，直接逐奇数系数求和给
$$
[w^{p-2-2s}]\frac{\mathcal L_p(w)}{1-w^2}
=h_{\rm odd}+\frac12H_s
\qquad(0\le s\le2\nu).
$$
确实，右边补回的高端奇数
$p-2s,p-2s+2,\ldots,p-2$ 的倒数和为 $-H_s/2$。
所以
$$
\boxed{\quad
a_\nu^2\mathsf h
=H_\nu-h_{\rm odd}-\frac12\sum_{s=0}^{2\nu}C_sH_s.
\quad}
\tag{1154.35}
$$
这是原 $\mathcal H_p$ 的实际同源 harmonic 表达，
不含一个未定的 companion 常数。

还可把 $h_{\rm odd}$ 写成原整数 Fermat quotient：
$$
q_p(2)=\frac{2^{p-1}-1}{p}\in\mathbf Z,\qquad
h_{\rm odd}=q_p(2)\pmod p.
$$
这里的除以 $p$ 先在整数中完成。
自足证明是将
$\binom pj/p\equiv(-1)^{j-1}/j$
对 $1\le j\le p-1$ 求和；
左边为 $2q_p(2)$，右边由
$\sum_{j=1}^{p-1}1/j=0$ 准确等于 $2h_{\rm odd}$。
结合 (1154.33)，得到
$$
\boxed{\begin{aligned}
\mathcal H_p
&=\frac{4\varepsilon_r}{63\beta_{\rm G}a_\nu^2}
 \left(q_p(2)-H_\nu
        +\frac12\sum_{s=0}^{2\nu}C_sH_s\right),\\
\mathcal H_p=0
&\Longleftrightarrow
q_p(2)=H_\nu-\frac12\sum_{s=0}^{2\nu}C_sH_s
\quad\bmod p.
\end{aligned}}
\tag{1154.36}
$$
这个条件不声称 $q_p(2)$ 为单位，也不把它换成某个未核的
Bernoulli 同余；它只使用同一 Legendre 多项式的实际 coefficients。

## 10. 同一 finite logarithm 给指定 minor 的完整三次式

为了使第二条联合条件也完全显式，置
$$
\begin{aligned}
\mathbf B_\nu&=\mathscr R(\mathsf P_\nu^4V_\nu^2),\\
\mathbf U_\nu&=\mathscr R(w\mathsf P_\nu^7V_\nu),\\
\mathbf V_\nu&=\mathscr R(w\mathsf P_\nu^5V_\nu^3).
\end{aligned}
$$
由 $\mathsf o=\mathsf P_\nu/a_\nu$、$\mathsf e=a_\nu V_\nu$，
原五个 moments 的各个幂因子直接给
$$
\mathsf b=a_\nu^{-2}\mathbf B_\nu,\quad
\mathsf u=a_\nu^{-6}\mathbf U_\nu,\quad
\mathsf v=a_\nu^{-2}\mathbf V_\nu,\quad
\mathsf t=a_\nu^{-6}.
$$
故
$$
\boxed{\quad
\Delta_{\rm low}
=\frac{4}{13365\,r\beta_{\rm G}^2a_\nu^8}
       (3\mathbf B_\nu\mathbf U_\nu-\mathbf V_\nu).
\quad}
\tag{1154.37}
$$
右边只含一个明确的 Legendre 多项式、
有限和 $\mathsf W_{\nu-1}$、以及同一个有限 $\mathcal L_p$；
对数的最高幂为三。
不需要再定义一个无限 Gauss 解，也不读取对数的首个 $p$ 分母。

特别，在 §6 已说明的 actual-good 分支中，
同一非对角共同纤维必须满足这两条完整关系：
$$
\boxed{\quad
q_p(2)=H_\nu-\frac12\sum_{s=0}^{2\nu}C_sH_s,\qquad
3\mathbf B_\nu\mathbf U_\nu-\mathbf V_\nu=0.
\quad}
\tag{1154.38}
$$
第一式和第二式使用同一 $V_\nu$；
没有将第二式的全部较低对数乘积删去。
目前还没有证明 (1154.38) 不可能。

R1152 的真实有限 harmonic 中央读数是另一个已固定来源。
(1154.36)–(1154.38) 不把这里的加权有限和认成
$\operatorname{Har}_p(1,3,4)$，也没有计算原 $F_0$ 的 $z_{12}$。
若要联立，仍须给出两种原来源间的准确 cochain、period 或 Frobenius 比较；
仅因两者都可写成有限 harmonic 和不足以识别。
本节全部是同一原 forcing 的纸面变换，无数学程序执行。


## 11. 完整 finite-log 移位与原 Bernoulli 条件

本节把 (1154.37) 中三次 finite logarithm 的全权重保留。
新增的无权端点是原 $\mathrm B_{p-3}$，不是一个另行选取的单位；
随后给出它在指定 minor 中的准确权重及全部剩余项。
这里 $\mathrm B_j$ 专指普通 Bernoulli 数，避免与
$\mathbf B_\nu$ 混同。

置
$$
M=\frac{p-1}{2},\qquad q=q_p(2),\qquad L=\mathcal L_p.
$$
以下所有等式先在 $\mathbf F_p$ 中读取；$q$ 仍由 (1154.36)
规定，不能作为自由参数选择。

### 11.1. 三次有限对数的完整端点

先有
$$
\boxed{\quad
\mathscr R(L^2)=0,\qquad
[w^{p-2}]\frac{L^3}{1-w^2}=\frac38\mathrm B_{p-3}.
\quad}
\tag{1154.39}
$$
第一式由
$(L^3)'=3L^2(1-w^{p-1})/(1-w^2)$
读取 $w^{p-1}$ 得到。左边该项为零；
右边多出的项至少从 $w^{p+1}$ 开始。

为自足证明第二式，定义有限的参数多项式
$$
E(T)=[w^{p-1}]
 \sum_{j=0}^{p-1}\frac{(2TL(w))^j}{j!}.
$$
这次所有阶乘都是单位。对 $1\le a\le p-1$，
在严格低于 $w^p$ 的前缀中，有
$$
E(a)=[w^{p-1}](1+w)^a(1-w)^{-a}
    =[w^{p-1}](1+w)^a(1-w)^{p-a}
    =2a(-1)^{a+1}.
$$
最后一个等式读取次数 $p$ 多项式的次高项；
未把模 $p$ 的指数参数当成一个无限特征零指数。
因为 $\deg E\le p-1$，有限域幂和准确给
$$
[T^4]E=-2\sum_{a=1}^{p-1}(-1)^{a+1}a^{p-4}
       =\frac12\sum_{b=1}^M b^{p-4}.
$$
令 $n=p-3$。Bernoulli 多项式的有限幂和与倍分式给
$$
\sum_{b=1}^M b^{p-4}
 =\frac{\mathrm B_n(1/2)-\mathrm B_n}{n}
 =\frac{(2^{1-n}-2)\mathrm B_n}{n}
 =-2\mathrm B_{p-3}\pmod p.
$$
这里 $n<p-1$，全部有关 Bernoulli 系数及分母在 $p$ 处整。
因此 $[T^4]E=-\mathrm B_{p-3}$。
另一方面，
$$
[T^4]E=\frac23[w^{p-1}]L^4,\qquad
[w^{p-2}]\frac{L^3}{1-w^2}
 =-\frac14[w^{p-1}]L^4.
$$
第二式来自 $(L^4)'$；此处 finite-log carry 还未到所读次数。
两式合并即 (1154.39)。

### 11.2. 每个实际移位的三个核

对 $0\le s\le M$，定义
$$
\begin{aligned}
o_s&=\sum_{i=0}^{s-1}\frac1{2i+1},&
K_s&=\sum_{i=0}^{s-1}\frac{H_i}{2i+1},\\
A_s&=\sum_{i=1}^{s}\frac{o_i}{i},&
J_s&=\sum_{i=1}^{s}\frac{K_i}{i}.
\end{aligned}
$$
空和为零。所有分母严格小于 $p$。
直接保留每个 coefficient 的真实范围，有
$$
\boxed{\begin{aligned}
\mathscr R(w^{2s+1}L)
 &=q+\frac{H_s}{2}
 &&(0\le s\le M-1),\\
\mathscr R(w^{2s}L^2)
 &=2q\,o_s+K_s
 &&(0\le s\le M-1),\\
\mathscr R(w^{2s+1}L^3)
 &=\frac38\mathrm B_{p-3}
      +3qA_s+\frac32J_s
 &&(0\le s\le M-2).
\end{aligned}}
\tag{1154.40}
$$
在各自上界以外，左边严格为零。
下面的加权和一律按这些界截断，不把右边未经说明地继续使用。

第一行就是 (1154.35) 的逐系数证明。
第二行可由完整端点 $\mathscr R(L^2)=0$ 倒读：
$$
[w^{2i}]L^2=\frac{o_i}{i}\qquad(1\le i\le M).
$$
去掉最后 $s$ 项时，写 $i=M-j$；
有 $o_{M-j}=q+H_j/2$、$1/(M-j)=-2/(2j+1)$。
所以被去掉的尾项为
$-(2q+H_j)/(2j+1)$，给第二行的两个正号。

第三行使用
$$
[w^{2i-1}]L^3=\frac{3A_{i-1}}{2i-1}.
$$
在最后 $s$ 项中写 $i=M-j$；
第二行已经给
$A_{M-j-1}=2q\,o_{j+1}+K_{j+1}$，
而 $2i-1=-2(j+1)$。
从 (1154.39) 减去这段尾项，准确得到第三行。
上述证明也说明：无权端点的 $\mathrm B_{p-3}$ 不可直接代替
一个有 $w^{2s+1}$ 的实际读取。

### 11.3. 保全部 $P_\nu$ 权的原 minor

为使展开可以逐项消费，对任意偶多项式
$A(w)=\sum a_s w^{2s}$ 定义以下有限线性泛函：
$$
\begin{aligned}
\mathfrak t(A)&=\sum_{s=0}^{M}a_s,&
\mathfrak d_i(A)&=\sum_{s=0}^{M-i}a_s\quad(i=1,2),\\
\mathfrak h_1(A)&=\sum_{s=0}^{M-1}a_sH_s,&
\mathfrak o_1(A)&=\sum_{s=0}^{M-1}a_so_s,\\
\mathfrak k_1(A)&=\sum_{s=0}^{M-1}a_sK_s,&
\mathfrak a_2(A)&=\sum_{s=0}^{M-2}a_sA_s,\\
\mathfrak j_2(A)&=\sum_{s=0}^{M-2}a_sJ_s.&&
\end{aligned}
\tag{1154.41}
$$
缺少的多项式系数按零处理；尤其高于所列界的
$P_\nu^8$ 项没有被改成在 $w=1$ 的值。

本小节简写
$$
P=\mathsf P_\nu,\qquad W=\mathsf W_{\nu-1},
\qquad V=W-PL.
$$
$P^5W/w$ 是真实偶多项式，因为 $w\mid P$。
定义完全固定的数
$$
\begin{aligned}
B_0&=H_\nu^2-\mathfrak h_1(P^5W/w)+\mathfrak k_1(P^6),\\
B_1&=-2H_\nu+2\mathfrak o_1(P^6),\\
U_0&=\mathfrak t(wP^7W)-\frac12\mathfrak h_1(P^8),\\
D_1&=\mathfrak d_1(P^8),\qquad D_2=\mathfrak d_2(P^8),\\
V_0&=\mathfrak t(wP^5W^3)-\frac32\mathfrak h_1(P^6W^2)
       +3\mathfrak k_1(wP^7W)-\frac32\mathfrak j_2(P^8),\\
V_1&=-3\mathfrak d_1(P^6W^2)
       +6\mathfrak o_1(wP^7W)-3\mathfrak a_2(P^8).
\end{aligned}
\tag{1154.42}
$$
这些是有限 Legendre 与 harmonic 数据；定义本身不宣称任何一项为单位。

完整乘积展开及 (1154.40) 给
$$
\boxed{\begin{aligned}
\mathbf B_\nu&=B_0+B_1q,\\
\mathbf U_\nu&=U_0-D_1q,\\
\mathbf V_\nu&=V_0+V_1q-\frac38\mathrm B_{p-3}D_2.
\end{aligned}}
\tag{1154.43}
$$
例如最后一式逐项使用
$$
wP^5V^3
=wP^5W^3-3wP^6W^2L
 +3wP^7WL^2-wP^8L^3.
$$
后三项正对应 (1154.40) 的三个不同范围。
第一式还用到
$\deg(P^4W^2)\le6\nu-2\le p-3$、
$\deg(P^5W/w)\le p-3$，所以它们没有高端截断：
$$
\mathfrak t(P^4W^2)=H_\nu^2,\qquad
\mathfrak d_1(P^5W/w)=H_\nu.
$$
与此相反，$P^8$ 的次数通常超过 $p-1$，
因而 $D_1,D_2$ 必须保持所定义的部分和。

### 11.4. 首标签为零后的真正 Bernoulli 方程

置
$$
Q_\nu=H_\nu-\frac12\mathfrak h_1(P^4),\qquad
\mathfrak C_\nu(T)
=3(B_0+B_1T)(U_0-D_1T)-V_0-V_1T.
$$
因为 $2\nu<M$，$Q_\nu$ 恰是 (1154.36) 中的完整加权和，
而 $\mathfrak C_\nu$ 的次数至多二。
(1154.37)、(1154.43) 准确成为
$$
\boxed{\quad
\Delta_{\rm low}
=\frac{4}{13365\,r\beta_{\rm G}^2a_\nu^8}
 \left(\mathfrak C_\nu(q)
       +\frac38\mathrm B_{p-3}D_2\right).
\quad}
\tag{1154.44}
$$
因此在 §6 指定的实际 good-row 分支中，
原非对角共同纤维同时满足
$$
\boxed{\quad
q_p(2)=Q_\nu,\qquad
\mathfrak C_\nu(Q_\nu)
       +\frac38\mathrm B_{p-3}D_2=0.
\quad}
\tag{1154.45}
$$
这是与原 $\mathrm B_{p-3}$ mask 的真实同源联系；
它没有用 R1152 的另一个 harmonic 来源替换任何标量。
在正在考虑的余支，$\mathrm B_{p-3}$ 本身是单位，
但 (1154.45) 仍保留整个 $\mathfrak C_\nu(Q_\nu)$ 和 $D_2$。
目前没有证明前者为零或后者为单位。
若 $D_2=0$，第二式就是 $\mathfrak C_\nu(Q_\nu)=0$；
若 $D_2\ne0$，才可除以这个真实部分和。
本篇不以无权的 (1154.39) 声称已经排除原余对。


## 12. 原 Newton 余对的 finite-log 算子与准确缺项

本节把 §11 的同一个 $E(T)$ 接到
[原有限重建笔记 (F.20)–(F.25)](../notes/2026-11-28-original-Gaussian-finite-contiguity-and-spectral-reconstruction.md)
的实际 Newton 余核。它不使用另一个横向权重行，
也不把有限多项式的非零值当成原共同纤维已被排除。

### 12.1. 同一个 $E$ 的完整 Bernoulli 系数与差分

(1154.39) 证明中的 $E$ 为偶多项式，$E(0)=0$，且
$\deg E=p-1$。写 $E(T)=\sum e_sT^s$，则
$$
\boxed{\begin{aligned}
e_2&=-4q_p(2),\\
e_s&=\frac{4(1-2^{2-s})}{1-s}\,
           \mathrm B_{p+1-s}
       &&(4\le s\le p-1,\ s\ {\rm even}),\\
e_{p-1}&=-1.
\end{aligned}}
\tag{1154.46}
$$
第一式也可用
$[w^{p-1}]L^2=o_M/M=-2q_p(2)$ 直接核准。
对其余偶 $s$，同一有限插值给
$$
e_s=-2\sum_{a=1}^{p-1}(-1)^{a+1}a^{p-s}
    =2^{3-s}\sum_{b=1}^M b^{p-s}.
$$
置 $n=p+1-s$，则 $2\le n\le p-3$。
沿 (1154.39) 的 Bernoulli 多项式证明，最后一个幂和为
$(2^{1-n}-2)\mathrm B_n/n$，正好得到 (1154.46)。
特别最末项也等于 $-6\mathrm B_2=-1$；
这与指数展开的 $(p-1)!$ 读取相同。

原始整数代表 $1\le a\le p-1$ 仍满足
$$
E(a)=2a(-1)^{a+1}\ne0.
$$
这是 $E$ 的有限域取值，不是关于原 Gaussian 参数的标签注入。
它还给一个完全精确的差分恒等式
$$
\boxed{\quad
T E(T+1)+(T+1)E(T)=-2(T^p-T).
\quad}
\tag{1154.47}
$$
左边在全部 $a\in\mathbf F_p$ 为零，包含 $a=0,-1$；
其次数至多 $p$，最高系数为 $-2$，
所以准确等于所示倍数的 $T^p-T$。
没有将 $T^p=T$ 当作 $\mathbf F_p[T]$ 中的恒等式。

### 12.2. 原差商到 $E$ 的实际算子

取同一个原 coarse component 内两个不同参数，
用 R1135 §10 已支付的两 twist 规范写
$$
Z=\gamma^2z,\quad Z'=\gamma^2z',\quad
S=Z+Z',\quad P=ZZ',\qquad
b_0=1,\ b_1=S,\ b_{h+2}=Sb_{h+1}-Pb_h.
$$
这里的 $P$ 是两点的乘积，不再是 §11 的 Legendre 简写；
本小节不混用两者。
保留 $S^2-4P\ne0$，并允许 $S=0$ 或 $P=0$。

令
$$
m=\frac{p-1}{2},\qquad
Q_{\rm grid}(Y)=\frac{Y^m-1}{(Y-1)(Y-1/4)}
$$
及
$$
D_{S,P}(Y)=
\sum_{h=1}^k\frac{b_{h-1}}{(2h)!}
 \overline{\mathsf B}_h(Y)
\quad\bmod Q_{\rm grid}(Y),
\qquad
\deg D_{S,P}<m-2.
$$
这是 (F.24) 的指定次数代表，不是任意另选的多项式。
在全部原 ambient 行，除了被排除的中间角色外，有
$$
\frac{\mathcal A_R(Z)-\mathcal A_R(Z')}{Z-Z'}
 =R(R^2-1)D_{S,P}(R^2),\qquad
D_{S,P}(4)=-\frac{G_{p-3}}{12}.
\tag{1154.48}
$$
这里 $\mathcal A_R$ 是去掉原单位 $N_R$ 后的完整行。
原实际观测仍只包含原 $\mathcal G_p$；(1154.48)
没有把 ambient 行加进观测。

置 $\vartheta=T\,d/dT$，定义
$$
\boxed{\quad
\mathscr Z_{S,P}(T)=
(1-\vartheta)
 \big((1-\vartheta)^2-1\big)
 \big((1-\vartheta)^2-\tfrac14\big)
 D_{S,P}\big((1-\vartheta)^2\big)\,E(T).
\quad}
\tag{1154.49}
$$
这是作用在原有限多项式上的真实算子。
作为 $\vartheta$ 的多项式，其次数至多 $p-2$；
不涉及对一个同值点对作横向微分。

对偶数 $s$ 令 $R=p+1-s$，则 $R=1-s$ 于 $\mathbf F_p$。
在 (1154.48) 的范围中直接按 $\vartheta T^s=sT^s$ 读取，
$$
\boxed{\quad
[T^s]\mathscr Z_{S,P}
=e_s\left(R^2-\frac14\right)
 \frac{\mathcal A_R(Z)-\mathcal A_R(Z')}{Z-Z'}.
\quad}
\tag{1154.50}
$$
特别，对 forced $R=p-1-2j$，$1\le j\le k-1$，
其对应项是 $s=2j+2$，并且
$$
e_s=\frac{4(1-2^R)\mathrm B_R}{R}.
$$
所以真实 primitive 因子 $1-2^R$ 继续保留；
不能将一个为零的 primitive 因子反除，也不能反向把
$e_s=0$ 一概读成 $\mathrm B_R=0$。

### 12.3. 全 actual-good 相等强迫的缺项与非零端点

假设这两点的全部原 actual-good 标签相等。
每个 forced $R=p-1-2j$ 都按以下真实二分处理：
若 $\mathrm B_R$ 为单位，该角色是已付的实际 good 行，
所以 (1154.50) 的差商为零；
若 $\mathrm B_R=0\bmod p$，则 $e_s=0$。
因此 $s=4,6,\ldots,2k$ 的全部系数为零。

另外，$s=0,2$ 分别由零常数或
$R(R^2-1)$ 消去；实际缺席的中间角色
$R=(p+1)/2$ 对应 $s=2k+2$，
由显示的 $R^2-1/4$ 因子消去。
奇次系数始终为零。准确得到
$$
\boxed{\quad
\mathscr Z_{S,P}(T)\in
T^{2k+4}\mathbf F_p[T],\qquad
\deg\mathscr Z_{S,P}=p-1,\qquad
[T^{p-1}]\mathscr Z_{S,P}
=\frac{15}{8}G_{p-3}\ne0.
\quad}
\tag{1154.51}
$$
最高系数逐项是
$(-1)\cdot2(4-1)(4-1/4)D_{S,P}(4)$；
所以它与 $S,P$ 无关，全部常数已有原尺度。

(1154.51) 不是矛盾：这样的有限多项式可以存在。
较高的 $s$ 仍对应原低角色的真实 mask，
本文没有把那些未出现的角色补成观测。
若 $R=2$ 实际 good，(1154.50) 与最高系数确会矛盾，
准确恢复已成的 R1127 分支；正在考虑的余支中，
不能擅自加入这条行。

### 12.4. 缺项的前两层就是原联合 moment

这个算子并未引入一个与原 $\mathcal H_p,\Delta_{\rm low}$
无关的辅助检测。由原 Kronecker 展开
$$
[U]\mathscr K(T,U)=\frac12C_2(T)
$$
可知 $c_1=\mathcal H_p/2$，
所以完整行 $\mathcal A_{p-3}(Z)=\mathcal H_p Z/4$。
代 $e_4=-\mathrm B_{p-3}$ 得
$$
\boxed{\quad
[T^4]\mathscr Z_{S,P}
=-\frac{35}{16}\mathrm B_{p-3}\mathcal H_p.
\quad}
\tag{1154.52}
$$
若 $R=4$ 的实际行也在两点相等，
R1135 的同一个单位 $F=G_{p-7}$ 给
$S=12c_2/F$。这时完整 $R=p-5$ 行的差商为
$$
\frac{c_3}{2}+\frac{d_1S}{24}
=\frac{\Delta_{\rm low}}{2F}.
$$
再代 $e_6=-3\mathrm B_{p-5}/4$，准确有
$$
\boxed{\quad
[T^6]\mathscr Z_{S,P}
=-\frac{297}{32G_{p-7}}\,
       \mathrm B_{p-5}\Delta_{\rm low}.
\quad}
\tag{1154.53}
$$
因此在 §6 的实际 Bernoulli 分支中，前两层恰是
(1154.45) 所处理的同一联合约束，而非另一个参数导数。
更高系数仍须用原 good 行、(1154.47) 和实际
$D_{S,P}$ 的二根递推来处理；
目前没有证明 (1154.51) 的缺项对这种指定 $D_{S,P}$ 不可能。
本节为纯纸面证明，没有数学程序执行。


## 13. 原 Jacobi 参数的完整有限 Green 核与 Newton 端点

本节把 §7 的同一个 Legendre 对、§12 的同一个 $E(T)$
放入一个有限系数空间，保留首次 $p$ 边界。
得到的是带原权重的明确读取公式，以及原 Newton 基的
Jacobi 端点身份。没有将无权配对、共同谱或其非退化性
当作指定 $\mathcal H_p,\Delta_{\rm low}$ 的非零证明。

### 13.1. 同一 companion 的参数来源

置 $\mathcal A=\mathbf F_p[w]/(w^p)$，并记
$$
q=1-w^2,\qquad
\mathcal D=q\,\frac d{dw},\qquad
\langle f,g\rangle=[w^{p-1}]\frac{fg}{q}.
$$
这里 $q$ 是一个多项式，不是 Fermat quotient。
$\mathcal D$ 在 $\mathcal A$ 上有定义，
而且 $\langle\mathcal Df,g\rangle=-\langle f,\mathcal Dg\rangle$；
这只用 $[w^{p-1}](fg)'=p[w^p](fg)=0$。
此配对非退化，因为在单项式基上的反对角系数为一。

对形式参数 $\tau$，用安全有限式定义
$$
A_\tau(w)=
\sum_{j=0}^{p-1}\frac{\tau^j\mathcal L_p(w)^j}{j!}
       \pmod{w^p},
$$
$$
J_{d,\tau}(w)=2^{-d}\sum_{j=0}^d
 \binom{d-\tau}{d-j}\binom{d+\tau}{j}
 (w-1)^j(w+1)^{d-j},
\qquad
F_{d,\tau}=A_\tau J_{d,\tau}\pmod{w^p}.
\tag{1154.54}
$$
本节只取 $0\le d\le m-1$，其中 $m=(p-1)/2$。
这些广义二项式仅除以小于 $p$ 的阶乘。
$J_{d,\tau}=P_d^{(-\tau,\tau)}$ 是一个实际多项式，
不是在可能有参数分母的超几何式中作形式相除。

特别，固定原 $\nu=\lfloor p/6\rfloor$，有
$$
F_{\nu,0}=\mathsf P_\nu,\qquad
\left.\partial_\tau F_{\nu,\tau}\right|_{\tau=0}
=-V_\nu.
\tag{1154.55}
$$
确实 $J_{0,\tau}=1,J_{1,\tau}=w-\tau$，且对 $d\ge1$，
$$
(d+1)J_{d+1,\tau}
=(2d+1)wJ_{d,\tau}
-\frac{d^2-\tau^2}{d}J_{d-1,\tau}.
$$
在 $\tau=0$ 微分后，
$\partial_\tau J_{d,\tau}|_0=-\mathsf W_{d-1}$，
由同一三项递推和初值逐步确定。
再用 $\partial_\tau A_\tau|_0=\mathcal L_p$ 就是 (1154.55)。
因此下文的一阶参数列准确是原 $V_\nu$，没有另选 companion。

### 13.2. 保留形式参数的两个边界项

记
$$
j_\tau=F_{\nu,\tau}(0),\qquad
k_\tau=F_{\nu,\tau}'(0),\qquad
\mathcal L_\nu=\mathcal D^2+\nu(\nu+1)q.
$$
$\nu$ 为奇数。由 (1154.54) 的 Rodrigues 等价式在 $w=0$
读取，或按上面的递推归纳，准确有
$$
j_\tau=-\frac{\tau}{\nu!}
 \prod_{a=1}^{(\nu-1)/2}(\tau^2-4a^2),
\qquad
k_\tau=-\frac1{\nu!}
 \prod_{a=0}^{(\nu-1)/2}
       \bigl(\tau^2-(2a+1)^2\bigr).
\tag{1154.56}
$$
第二式包含 $A_\tau$ 的一次导数：
$k_\tau=J_{\nu,\tau}'(0)+\tau J_{\nu,\tau}(0)$。
特别 $j_0=0,k_0=a_\nu$。

在 $\mathcal A[\tau]$ 中，完整方程是
$$
\boxed{\quad
(\mathcal L_\nu-\tau^2)F_{\nu,\tau}
=(\tau-\tau^p)
 \bigl(j_\tau w^{p-2}-k_\tau w^{p-1}\bigr).
\quad}
\tag{1154.57}
$$
以下直接支付首次边界，而不把 $\tau^p=\tau$
用于形式参数。先在特征零中写
$\mathcal F_\tau=e^{\tau\operatorname{atanh}w}J_{\nu,\tau}$。
Jacobi 方程给
$(\mathcal L_\nu-\tau^2)\mathcal F_\tau=0$。
若 $a_j=[w^j]e^{\tau\operatorname{atanh}w}$，
则到次数 $p$ 的唯一非整来源是
$\tau w^p/p$ 与 $(\tau w)^p/p!$，所以
$$
pa_p\equiv\tau-\tau^p,\qquad
pa_{p+1}\equiv\tau(\tau-\tau^p)\pmod p.
$$
后一式也由
$(1-w^2)(e^{\tau\operatorname{atanh}w})'
=\tau e^{\tau\operatorname{atanh}w}$
在次数 $p$ 直接得到。
于是
$$
p[w^p]\mathcal F_\tau=(\tau-\tau^p)j_\tau,\qquad
p[w^{p+1}]\mathcal F_\tau=(\tau-\tau^p)k_\tau.
$$
$\mathcal D^2w^p$ 的最低项是 $p(p-1)w^{p-2}$，
$\mathcal D^2w^{p+1}$ 的最低项是 $p(p+1)w^{p-1}$。
从完整解减去这两个被截掉的系数，恰给 (1154.57)；
更高次数不可能落入 $\mathcal A$。
这是有限多项式的恒等式，不需要约化整个非整无限解。

因为 $\mathcal L_\nu$ 关于上述配对自伴，
将 (1154.57) 的两参数版本相减，得到
$$
(\tau^2-\sigma^2)
 \langle F_{\nu,\tau},F_{\nu,\sigma}\rangle
=\bigl(\tau+\sigma-(\tau+\sigma)^p\bigr)
 (k_\tau j_\sigma-j_\tau k_\sigma).
$$
分子 $k_\tau j_\sigma-j_\tau k_\sigma$ 被 $\tau-\sigma$
整除。在多项式环中消去共同因子后，有
$$
\boxed{\quad
\langle F_{\nu,\tau},F_{\nu,\sigma}\rangle
=\bigl(1-(\tau+\sigma)^{p-1}\bigr)
 \frac{k_\tau j_\sigma-j_\tau k_\sigma}{\tau-\sigma}.
\quad}
\tag{1154.58}
$$
右边的商是真正的多项式，所以对角与反对角也包含在内。
例如 $\sigma=-\tau$ 时它准确是
$\prod_{a=1}^{\nu}(1-\tau^2/a^2)$。
对 (1154.57) 在 $\tau=0$ 微分，还得到原伴随列的完整式
$$
\boxed{\quad
\mathcal L_\nu V_\nu=a_\nu w^{p-1}.
\quad}
\tag{1154.59}
$$
不能以 $\tau\in\mathbf F_p$ 逐点时右边消失为理由，
在参数微分前删掉 $\tau-\tau^p$。

### 13.3. 全部原权重都由同一个 $E$ 读取

只使用 (1154.58) 的无权配对还不包含原 minor 的权重。
这里给出保留这些权重的有限公式。

定义
$$
M_j(\eta)=\langle w^j,A_\eta\rangle
\quad(0\le j\le p),\qquad M_p=0.
$$
原 $A_\eta$ 的完整一阶边界是
$\mathcal DA_\eta-\eta A_\eta
=-(\eta-\eta^p)w^{p-1}$。
对它以及 $\mathcal D(w^jA_\eta)$ 使用配对，
直接得到
$$
\boxed{\begin{aligned}
M_0&=1-\eta^{p-1},&
M_1&=-\frac{E(\eta/2)}{\eta},\\
M_{j+1}&=M_{j-1}+\frac{\eta}{j}M_j
 &&(1\le j\le p-1).
\end{aligned}}
\tag{1154.60}
$$
$E(0)=0$，所以这里的商也是多项式。
$M_1$ 的式子来自
$0=\langle1,\mathcal D(wA_\eta)\rangle
=[w^{p-1}]A_\eta+\eta M_1$，
其中 $[w^{p-1}]A_\eta=E(\eta/2)$。
所有递推除数均为单位。

这也给一个完全固定的有限端点模型。
令 $\mathfrak a_0=1,\mathfrak a_1=0$、
$\mathfrak b_0=0,\mathfrak b_1=1$，两列按
(1154.60) 的同一递推定义至指标 $p$。则
$$
\boxed{\quad
\mathfrak b_p=1-\eta^{p-1},\qquad
\mathfrak a_p=\frac{E(\eta/2)}{\eta},\qquad
M_j=\mathfrak a_j\mathfrak b_p-\mathfrak b_j\mathfrak a_p.
\quad}
\tag{1154.61}
$$
证明不假设任何 Bernoulli 数为单位。
先由递推得 $M_j=\mathfrak a_jM_0+\mathfrak b_jM_1$。
$\mathfrak b_p$ 的次数为 $p-1$、首系数为
$1/(p-1)!=-1$、常数为一。
对每个 $\eta\in\mathbf F_p^\times$，
(1154.47) 前的准确值保证 $E(\eta/2)\ne0$；
故 $M_p=0$ 强迫 $\mathfrak b_p(\eta)=0$。
于是 $\mathfrak b_p=1-\eta^{p-1}$，再在多项式环中消去
这个非零因子，得到 $\mathfrak a_p=-M_1$。
特别由原定义，$M_{p-1}=1,M_{p-2}=\eta$。
这些端点保留了 §11 的真实高端 cutoff。

对任何多项式 $H(w)=\sum h_jw^j$，定义
$$
\mathscr T_\eta(H)=\sum_{j=0}^{p-1}h_jM_j(\eta).
$$
先在 $w$ 方向模 $w^p$，再作此读取。
有限指数的乘法律给
$$
\left\langle 1,\,
 H(w)\prod_{i=1}^sF_{d_i,\tau_i}(w)\right\rangle
=\mathscr T_{\tau_1+\cdots+\tau_s}
 \left(H(w)\prod_{i=1}^sJ_{d_i,\tau_i}(w)\right).
\tag{1154.62}
$$
因此这不是用无权核替代原 moments。
写 $P=\mathsf P_\nu$，则 (1154.55) 准确给
$$
\boxed{\begin{aligned}
a_\nu^2\mathsf h
&=-\left.\partial_\tau
 \mathscr T_\tau(wP^3J_{\nu,\tau})\right|_0,\\
\mathbf B_\nu
&=\left.\partial_\tau\partial_\sigma
 \mathscr T_{\tau+\sigma}
 (P^4J_{\nu,\tau}J_{\nu,\sigma})\right|_0,\\
\mathbf U_\nu
&=-\left.\partial_\tau
 \mathscr T_\tau(wP^7J_{\nu,\tau})\right|_0,\\
\mathbf V_\nu
&=-\left.\partial_\tau\partial_\sigma\partial_\rho
 \mathscr T_{\tau+\sigma+\rho}
 (wP^5J_{\nu,\tau}J_{\nu,\sigma}J_{\nu,\rho})\right|_0.
\end{aligned}}
\tag{1154.63}
$$
这些参数微分仅到三阶；它们作用于已经定义的有限多项式。
$P^8$ 的高次项没有被改成端点一：
次数至少 $p$ 的 $w$ 项确实不参与原系数读取。
尤其 $M_{p-2}=\eta$ 的三次系数为零，
所以最末奇位不能套用 §11.2 的内部三次核；
这正是原 $D_2$ 而非 $D_1$ 的 cutoff。
(1154.63) 继续保留 $\mathfrak C_\nu(Q_\nu)$ 的全部剩余项。

### 13.4. 原 Newton 基的准确 Jacobi 端点

还有一条将 §12 的原差商接回同一有限配对的精确身份。
对每个 $2\le r\le m$，取 (1154.54) 中的 $d=r-1$。
有限指数相消，而 $J_{d,\tau}J_{d,-\tau}$ 为偶多项式，
次数 $2d\le p-3$。所以
$$
\langle F_{r-1,\tau},F_{r-1,-\tau}\rangle
=J_{r-1,\tau}(1)J_{r-1,-\tau}(1)
=\prod_{a=1}^{r-1}\left(1-\frac{\tau^2}{a^2}\right).
$$
由此得到原 (F.20) 的完整尺度
$$
\boxed{\quad
q_r(R)=
-\frac{R((r-1)!)^2}{(2r-1)!}
 \langle F_{r-1,R},F_{r-1,-R}\rangle.
\quad}
\tag{1154.64}
$$
特别，原实际点对
$\mathsf F_{Z,Z'}=\sum_{r=2}^m c_rE_r$
的全 Newton 读取，是 (1154.64) 的同一 $c_r$ 线性组合；
没有换成另一组可自由选择的 moments。
$r=m$ 的端点在非零 $R\in\mathbf F_p$ 上只可能于
$R=\pm m=\pm1/2$ 非零，
故再乘 $R^2-1/4$ 后消失。这与
spectral note (F.35)–(F.38) 的完整
$C_{\rm pr}$ 和 $-(R^p-R)$ 边界一致，
不把 $C_{\rm pr}$ 或其中某个低卷积改成零。

这里仍有两个明确不同的指标：
(1154.55)–(1154.63) 的 $\nu$ 固定为原 $\lfloor p/6\rfloor$；
(1154.64) 的 Jacobi 次数是变化的 $r-1$。
端点身份本身没有把这个变化次数族与指定
$P_\nu^4,wP_\nu^6$ 权重作算子等同，
也没有构造一个保原二根递推的 intertwiner。
因此 actual-good mask、两点真实范围及 (1154.45)/(1154.51)
仍保持原有条件，未由本节排除共同纤维。
新增可消费的来源是 (1154.57) 的两个完整边界、
(1154.60)–(1154.63) 保全部权重的同一个 $E$ 读取，
以及 (1154.64) 的原 Newton 端点尺度。
全节为纸面证明，没有数学程序执行。

root 全文逐式核准形式参数的p/p+1边界、Green相减号、M_j递推至真实j=p端点、所有原Pν权重与Newton尺度。特别未在参数微分前使用τ^p=τ，也未把固定ν与变化r−1等同；o1独核完整Green核。无数学程序执行。


## 14. Darboux 运输的完整最高 jet 与固定次数的阶数递推

本节继续 §13 的同一个有限代数、配对和形式参数。
将 Jacobi 族写成 Darboux 运输时，截掉次数 $p$ 以上的项并不与微分算子交换。
下面计算这个差，而不是只在 $\tau\in\mathbf F_p$ 上比较后再求参数导数。

### 14.1. 一个明确的 $\nu$ 阶边界

仍记 $q=1-w^2$、$\mathcal D=q\,d/dw$，并置
$$
A_j=\mathcal D-jw,\qquad B_j=\mathcal D+jw,\qquad
\mathcal T_\nu=A_\nu A_{\nu-1}\cdots A_1 .
$$
算子的乘积从右向左作用；相对于 (1154.54) 前的配对，
$A_j^*=-B_j$。
在特征零的安全有理系数环中，Jacobi 的有限二项式式给
$$
(\mathcal D+\tau-jw)J_{j-1,\tau}=-jJ_{j,\tau}.
$$
所以逐步作用，得到完整恒等式
$$
\mathcal T_\nu e^{\tau\operatorname{atanh}w}
=(-1)^\nu\nu!\,
 e^{\tau\operatorname{atanh}w}J_{\nu,\tau}.
\tag{1154.65}
$$
这里不先约化无限指数级数。

先在 $\mathbf Z_{(p)}[w,d/dw]$ 定义，再约化
$$
\mathfrak E_\nu=
\frac{[\mathcal T_\nu,w^p]}p
\pmod{(p,w^p)}.
\tag{1154.66}
$$
这是实际整微分算子：$\nu<p$，而
$d^a(w^p)/dw^a$ 对 $1\le a\le\nu$ 都被 $p$ 整除。
它在 $\mathcal A=\mathbf F_p[w]/(w^p)$ 上有定义。
对单项式的最低项准确为
$$
\boxed{
\begin{aligned}
\mathfrak E_\nu(w^i)
&=(-1)^{\nu-i-1}i!(\nu-i-1)!
  w^{p-\nu+i}
  +\text{更高次项},
&&0\le i<\nu,\\
\mathfrak E_\nu(w^i)&=0,
&&\nu\le i<p.
\end{aligned}}
\tag{1154.67}
$$
确实 $\mathcal T_\nu$ 的最高导数项为 $q^\nu(d/dw)^\nu$；
只有它能给显示的最低次数，其系数是
$(p+i)(p+i-1)\cdots(p+i-\nu+1)/p$ 的约化。
其它项只能提高次数。
因此
$$
\ker\mathfrak E_\nu=(w^\nu),\qquad
\operatorname{im}\mathfrak E_\nu=w^{p-\nu}\mathcal A,
\qquad \operatorname{rank}\mathfrak E_\nu=\nu.
$$
这是前 $\nu$ 个 jet 到最高 $\nu$ 个 jet 的同构，不能把它整体删去。
特别 $\nu$ 为奇数时，
$\mathfrak E_\nu(1)=(\nu-1)!w^{p-\nu}+\cdots$，
显示首项为单位。

### 14.2. 原 companion 的全部修正

若 $a_j=[w^j]e^{\tau\operatorname{atanh}w}$，则 §13 的首次边界还给
$$
pa_{p+j}\equiv(\tau-\tau^p)a_j\pmod p
\qquad(0\le j<\nu).
$$
由 $pa_p=\tau-\tau^p$ 和原一阶方程，
对 $j$ 归纳即可；所有递推除数 $1,\ldots,\nu-1$ 都是单位。
在这些次数内只有一次 $p$ 分母。
次数至少 $p+\nu$ 的项不可能经 $\mathcal T_\nu$ 落到 $w^p$ 以下。

于是 (1154.65) 约化后的完整式是
$$
\boxed{
\mathcal T_\nu A_\tau
=(-1)^\nu\nu!F_{\nu,\tau}
-(\tau-\tau^p)\mathfrak E_\nu(A_\tau).}
\tag{1154.68}
$$
这里 $\mathfrak E_\nu(A_\tau)$ 只需要 $A_\tau$ 的前 $\nu$ 个系数，
所以是定义明确的有限多项式。
对形式参数在零处微分，利用 $\nu$ 为奇数与 (1154.55)，得到
$$
\boxed{\qquad
\nu!V_\nu=\mathcal T_\nu\mathcal L_p+\mathfrak E_\nu(1).
\qquad}
\tag{1154.69}
$$
逐点的 $\tau^p=\tau$ 不能消掉本式最后一项。

边界还有无需重建高次多项式的双权读取。
对任意 $f,g\in\mathcal A$，
$$
\boxed{
\langle f,\mathfrak E_\nu g\rangle
=\sum_{j=1}^{\nu}
 \bigl(A_{j+1}^*\cdots A_\nu^*f\bigr)(0)\,
 \bigl(A_{j-1}\cdots A_1g\bigr)(0).}
\tag{1154.70}
$$
空乘积为恒等。
证明可在 Laurent 算子中直接进行：
$$
w^{-p}\mathcal T_\nu w^p
=\prod_{j=\nu,\ldots,1}(A_j+p q/w).
$$
减去 $\mathcal T_\nu$、除以 $p$ 后，只保一次插入 $q/w$。
在留数配对中把其左侧算子逐个移到 $f$ 上，
而 $(q/w)\,dw/q=dw/w$；最后只读两正规函数的常数项。
这同时保留了所有符号与两端 jet。

记 $e_\nu=\mathfrak E_\nu(1)$，
并令 $\operatorname{bd}_\nu(f)=\langle f,e_\nu\rangle$。
因为
$A_{j-1}\cdots A_1(1)=(-1)^{j-1}(j-1)!\mathsf P_{j-1}$，
且 $\nu$ 为奇数，(1154.70) 化为
$$
\operatorname{bd}_\nu(f)=
\sum_{\substack{1\le j\le\nu\\j\ {\rm odd}}}
 (j-1)!\mathsf P_{j-1}(0)\,
 (B_{j+1}\cdots B_\nu f)(0).
$$
它只读 $f$ 的前 $\nu$ 个 jet；
没有以这个有限和的存在断言其值为单位。

### 14.3. 原四个 weighted 读取中的一次边界

仅在本小节置 $\mathsf K_\nu=\mathcal T_\nu\mathcal L_p$，
并仍写 $P=\mathsf P_\nu$。
由于 $2(p-\nu)\ge p$，在 $\mathcal A$ 中有 $e_\nu^2=0$。
因此 (1154.69) 代入原四个 moments，恰给
$$
\boxed{\begin{aligned}
a_\nu^2\mathsf h
&=\frac{\langle wP^3,\mathsf K_\nu\rangle+
               \operatorname{bd}_\nu(wP^3)}{\nu!},\\
\mathbf B_\nu
&=\frac{\langle P^4,\mathsf K_\nu^2\rangle+
               2\operatorname{bd}_\nu(P^4\mathsf K_\nu)}
              {(\nu!)^2},\\
\mathbf U_\nu
&=\frac{\langle wP^7,\mathsf K_\nu\rangle+
               \operatorname{bd}_\nu(wP^7)}{\nu!},\\
\mathbf V_\nu
&=\frac{\langle wP^5,\mathsf K_\nu^3\rangle+
               3\operatorname{bd}_\nu(wP^5\mathsf K_\nu^2)}
              {(\nu!)^3}.
\end{aligned}}
\tag{1154.71}
$$
这些仍是 §10 的同一 $\mathbf B_\nu,\mathbf U_\nu,\mathbf V_\nu$，
没有将 $P^4$、$wP^6$ 或高端 cutoff 换成无权端点。

例如记上面三个分子的非边界部分为
$B^\circ,U^\circ,V^\circ$，相应一次读取为
$b^\partial=\operatorname{bd}_\nu(P^4\mathsf K_\nu)$、
$u^\partial=\operatorname{bd}_\nu(wP^7)$、
$v^\partial=\operatorname{bd}_\nu(wP^5\mathsf K_\nu^2)$，则实际 minor 的完整分子是
$$
(\nu!)^3(3\mathbf B_\nu\mathbf U_\nu-\mathbf V_\nu)
=3(B^\circ+2b^\partial)(U^\circ+u^\partial)
  -V^\circ-3v^\partial .
$$
其中 $6b^\partial u^\partial$ 是两个已读取标量的乘积，
不能由函数恒等式 $e_\nu^2=0$ 删掉。
本节固定了真正的边界计算，没有证明右边非零。

### 14.4. 固定 $\nu$ 的阶数递推与它的边界

同一个有限二项式定义还直接给
$$
\begin{aligned}
(\nu-\tau)J_{\nu,\tau+1}
 &=-(1-w)J_{\nu,\tau}'-\tau J_{\nu,\tau},\\
(\nu+\tau)J_{\nu,\tau-1}
 &=(1+w)J_{\nu,\tau}'+\tau J_{\nu,\tau}.
\end{aligned}
$$
可逐项用 Pascal 恒等式核准；这里的次数一直是固定的 $\nu$。
若把它写成对有限 $F_{\nu,\tau}$ 的微分作用，
(1154.60) 前的一阶边界必须保留：
$$
\boxed{\begin{aligned}
(\nu-\tau)\sqrt q\,F_{\nu,\tau+1}
 &=-(\mathcal D+\tau w)F_{\nu,\tau}
   -(\tau-\tau^p)j_\tau w^{p-1},\\
(\nu+\tau)\sqrt q\,F_{\nu,\tau-1}
 &=(\mathcal D-\tau w)F_{\nu,\tau}
   +(\tau-\tau^p)j_\tau w^{p-1}.
\end{aligned}}
\tag{1154.72}
$$
$\sqrt q$ 始终取常数一的有限平方根。
两式相加时上述边界确实相消。
令 $X=w/\sqrt q$，得到
$$
(\nu-\tau)F_{\nu,\tau+1}
 +2\tau X F_{\nu,\tau}
 +(\nu+\tau)F_{\nu,\tau-1}=0.
$$
再次使用这条式子，并先清分母，有
$$
\boxed{\begin{aligned}
4\tau(\tau^2-1)X^2 F_{\nu,\tau}
={}&(\tau-1)(\nu-\tau)(\nu-\tau-1)F_{\nu,\tau+2}\\
 &+2\tau\{\nu(\nu+1)+1-\tau^2\}F_{\nu,\tau}\\
 &+(\tau+1)(\nu+\tau)(\nu+\tau-1)F_{\nu,\tau-2}.
\end{aligned}}
\tag{1154.73}
$$
它在 $\mathcal A[\tau]$ 中成立，因而也保留
$\tau=0,\pm1,\pm\nu$ 的退化边界；
不得在这些位置反除显示的因子。
同时 $X^2=w^2/(1-w^2)=-x$，
正是 §7 的同一有限 Gauss 变量，并非新引入的自由坐标。

(1154.73) 支付原固定次数族中 $X^2$ 乘法的三项运输。
它仍不表示原 Bernoulli good-mask 在 $\tau\mapsto\tau\pm2$ 下封闭，
也没有把 (1154.64) 中变化的次数 $r-1$ 认成 $\nu$。
后续要由此排除两个实际 coarse 点，仍须证明运输保留原二根系数和实际可用行。
本节新增的可用来源是 (1154.67) 的精确边界同构、
(1154.70)–(1154.71) 的原 weighted 读取和
(1154.72)–(1154.73) 保退化项的阶数递推。
全节为纸面证明，无数学程序执行。
