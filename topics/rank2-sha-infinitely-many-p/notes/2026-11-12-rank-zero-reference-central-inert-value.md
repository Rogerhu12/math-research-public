# 秩零参考曲线的中央首坏项：每个惰性素数的精确赋值

日期：2026-11-12。状态：本篇的参考值及其赋值已证明；它本身不推出 E17 的 Sha 有限性。

考虑固定参考曲线

$$
 E_0:y^2=x^3-x,\qquad \omega_0=\frac{dx}{2y},\qquad
 K=\mathbb Q(i),\qquad f_0=2(1+i).
$$

其 CM Hecke 特征的导子为 $(f_0)$。
对应射线类域是 $K$：类数为一，
$(\mathcal O_K/(1+i)^3)^\times$ 有四个元素，
且 $\mu_4$ 到该群是双射。
因此标准导子迹在这里只有一个点。

取精确 $f_0$-阶点

$$
 S=(i,1-i),\qquad [2]S=(0,0)=T .
$$

标准正实周期所给的导子点与此点至多相差一个 $\mu_4$ 作用。
这对以下任何 $p$-进赋值都只乘单位；本篇使用上述明确的点来固定公式。

设 $d_m^{(0)}$ 是这个单点 Kronecker theta 的中央系数：

$$
 d_m^{(0)}=[z^mw^m]\left(\Theta_{S,0}(z,w)-\frac1w\right).
                                                               \tag{1}
$$

**结论。** 对每个 $p\ge7$、$p\equiv3\pmod4$，

$$
 \boxed{\quad
 v_p(d_{p+1}^{(0)})=-2 .
 \quad}                                                       \tag{2}
$$

更精确地，置

$$
 r=\frac{p+1}{4},\qquad
 \kappa_{0,p}
   =-\frac12(-1)^r\binom{2r}{r}\in\mathbb F_p^\times .
$$

则

$$
 \boxed{\quad
 p^2d_{p+1}^{(0)}
       \equiv\kappa_{0,p}^{\,2}\frac{1+i}{2}\pmod p .
 \quad}                                                       \tag{3}
$$

左边在取模前确实是整的。由于 $p$ 惰性，右边在
$\mathbb F_{p^2}$ 中非零。

## 1. 初值来自 sigma duplication，不使用 BSD

令 $U(Z)=E_1^*(Z)$，采用前述中央 theta 笔记的 reduced-theta 规范。
在方格晶格上，$U$ 是完成后的 zeta 函数。
二挠点处由奇性与周期性有 $U(T)=0$。

不变微分规范下，sigma duplication 精确为

$$
 \sigma_0(2z)=\sigma_0(z)^4(-2y(z)).
                                                               \tag{4}
$$

负号由 $y(z)=-z^{-3}+\cdots$ 与左边首项 $2z$ 固定；
对数导数不受这个常数负号影响。
对 (4) 求导并加入完成项，得到

$$
 U(2S)=2U(S)+\frac12\,\delta\log(-2y)(S),\qquad
 \delta=2y\frac d{dx}.
$$

因为

$$
 \delta\log(-2y)=\frac{3x^2-1}{y},
$$

所以

$$
 U(S)=-\frac{3i^2-1}{4(1-i)}
          =\frac{1+i}{2}.
                                                               \tag{5}
$$

Kronecker 展开给 $d_0^{(0)}=U(S)$。在这一点和生成元规范下，

$$
 \frac{d_0^{(0)}}{f_0}=\frac14 .
                                                               \tag{6}
$$

特别是初值对所有奇素数都是单位。这是有限的 sigma 与 torsion
计算，没有使用参考曲线的 BSD 公式。

## 2. 惰性处的代数微分系统

在

$$
 \mathcal R_0=\mathcal O_{K,(p)}[U,X,Y]/(Y^2-X^3+X)
$$

上定义

$$
 \mathcal DU=-X,\quad
 \mathcal DX=2Y,\quad
 \mathcal DY=3X^2-1,\quad
 \mathcal L=\mathcal D+U,\quad C_n=\mathcal L^n1.
                                                               \tag{7}
$$

曲线导子 $\delta=\mathcal D|_{\mathcal O[X,Y]}$ 在惰性处满足
$\delta^p=0$ 模 $p$。于是

$$
 \kappa=\delta^{p-1}X\in\mathbb F_p,\qquad
 \mathcal D^p=-\kappa\partial_U,\qquad
 \partial_UC_n=nC_{n-1}.
                                                               \tag{8}
$$

Bell/Jacobson 恒等式给

$$
 B=C_p=U^p-\delta^{p-2}X,\qquad
 \mathcal DB=-\kappa,\qquad
 C_{p+n}=-\kappa nC_{n-1}+BC_n\pmod p .
                                                               \tag{9}
$$

这些恒等式与
[中央惰性平移笔记](2026-11-12-central-diagonal-inert-shift.md)
§1 相同，只把曲线参数 $17$ 换成 $1$。

这里 $\kappa$ 的精确式及后文 sigma 分母界可以从该笔记严格转移。
在最大未分歧扩张中取单位 $a$ 满足 $a^4=17$，则

$$
 E_0\longrightarrow E_{17},\quad
 (X,Y)\longmapsto(a^2X,a^3Y),\qquad
 \delta_{17}=a\,\delta_0 .
$$

因此

$$
 \kappa_{17,p}=a^{p+1}\kappa_{0,p}=17^r\kappa_{0,p}.
$$

惰性平移笔记的已证公式
$\kappa_{17,p}=-\tfrac12(-1)^r\binom{2r}{r}17^r$
即给本篇的 $\kappa_{0,p}$。由于 $2r<p$，它非零。
这里只对曲线微分系统作单位换元，不把不同全局 Hecke 特征等同。

## 3. 真实参考导子点满足 $B(S)=0$

必须保留实际初值，而不是在任意 $U$ 上假设这一等式。
对 $S$ 取 (4) 的平移版本。若

$$
 F_S(z)=e^{-z\bar z_S/A}
                   \frac{\sigma_0(z_S+z)}{\sigma_0(z_S)},
$$

则

$$
 F_T(2z)=F_S(z)^4
                    \frac{(-2y)(S+z)}{(-2y)(S)}.             \tag{10}
$$

$(-2y)(S)=-2(1-i)$ 是当前位的单位。
$T$ 是二挠点，所以 $d\log F_T(z)/dz$ 为奇函数；
它的第 $0$ 和第 $p-1$ 阶导数在零处均为零。

令 $h=\delta\log(-2y)$。对 (10) 的对数取一次和 $p$ 次导数，得

$$
 h(S)=-4U(S),\qquad
 (\delta^{p-1}h)(S)=-4(\mathcal D^{p-1}U)(S).
                                                               \tag{11}
$$

由 $\delta^p=0$ 和
$\delta+h=(-2y)^{-1}\delta(-2y)$，
Bell/Jacobson 给 $\delta^{p-1}h=-h^p$。
代入 (11)，使用 $4^p=4$ 模 $p$，可得

$$
 (\mathcal D^{p-1}U)(S)=-U(S)^p,\qquad B(S)=0\pmod p .
                                                               \tag{12}
$$

这一证明使用乘子 $2$，故不引入额外的惰性坏素数。

## 4. 只需两项的中央系数计算

令

$$
 q_j^{(0)}=[w^j]\frac{w}{\sigma_0(w)}.
$$

在次数 $j<2p$ 的范围内，
惰性平移笔记 §3 及上面的单位缩放给

$$
 q_j^{(0)}\in\mathcal O\quad(j<p+1),\qquad
 v_p(q_j^{(0)})\ge-1\quad(j<2p),\qquad
 pq_{p+1}^{(0)}\equiv-\kappa\pmod p.
                                                               \tag{13}
$$

单位缩放的方向是
$\sigma_{17}(w)=a^{-1}\sigma_0(aw)$，因此
$q_j^{(17)}=a^j q_j^{(0)}$，并无额外周期分母。
此外方格对称给 $q_j^{(0)}=0$，除非 $4\mid j$。

固定中央 theta 的完整有限公式是

$$
 d_m^{(0)}=
 \frac1{m!}\sum_{j=0}^{m+1}
       \frac{q_j^{(0)}}{(m+1-j)!}
                  (\mathcal D^m C_{m+1-j})(S).              \tag{14}
$$

取 $m=p+1$。外面的 $(p+1)!$ 恰有一个 $p$ 因子；
内层由 (13) 至多再有一个。因此 $p^2d_{p+1}^{(0)}$ 整。
乘 $p^2$ 后模 $p$，只有 $j=0$ 与 $j=p+1$ 可能保留：

* 内层阶乘含 $p$ 时，必须 $j\le2$，而 $q_1=q_2=0$；
* $q_j$ 含 $p^{-1}$ 时，只有 $j=p+1$，因为 $q_{p+2}=0$。

第二项实际为零，因为

$$
 \mathcal D^{p+1}C_1
       =\mathcal D^p(-X)=0\pmod p.                           \tag{15}
$$

第一项的分子由 (8)、(9)、(12) 给

$$
 \begin{aligned}
 (\mathcal D^{p+1}C_{p+2})(S)
   &=-\kappa(p+2)(\mathcal DC_{p+1})(S)\\
   &=-2\kappa\,\mathcal D(-\kappa+BU)(S)\\
   &=2\kappa^2U(S)\pmod p .
 \end{aligned}                                                \tag{16}
$$

Wilson 定理则给

$$
 \frac p{(p+1)!}\equiv-1,\qquad
 \frac p{(p+2)!}\equiv-\frac12\pmod p .
$$

故 (14) 恰化为

$$
 p^2d_{p+1}^{(0)}
      \equiv\frac12(2\kappa^2U(S))
      =\kappa^2U(S)\pmod p .
$$

与 (5) 合并即为 (3)，也证明 (2)。

## 5. 用作参考值时的范围

若记 $e_m^{(0)}=d_m^{(0)}/f_0^{2m+1}$，则所有奇素数处
$v_p(e_m^{(0)})=v_p(d_m^{(0)})$。
所以参考中央权 $m=p+1$ 的归一化分母恰为 $p^2$。

本篇只提供这个精确算术输入。把它同 E17 的 Kato 或 signed
Coleman 元比较，还必须核对两者所用的全局特征、局部 Tate 与
de Rham 基，以及插值式里的阶乘和 Euler 因子；局部曲线同构本身
不会自动识别全局 Euler-system 元。
