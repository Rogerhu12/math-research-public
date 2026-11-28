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
