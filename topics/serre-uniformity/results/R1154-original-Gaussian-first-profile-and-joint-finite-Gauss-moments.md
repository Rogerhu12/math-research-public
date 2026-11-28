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
