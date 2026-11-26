# R1049：原 $f_N$ 的完整 theta 一阶方向矩

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明的恒等式；未证明所示一阶矩非零。** 本文保留原 $F=x\sigma^6$、实际 theta 刚化、全部模六相位和原 $f_N$。它将原端点写成一个完整方向和，不丢 first-$p$ 项，也不把方向处处非零误作指定 Fourier 系数非零。本文尚未取得原 primitive/Legendre 同标签读数。

## 1. 同一来源与结论

沿 R1016、R1020、R1025、R1027，设
$$
p=6N+5\ge41,\qquad E:y^2=x^3-1,\qquad \sigma'(0)=1,
$$
$$
F=x\sigma^6=z^4\sum_{i\ge0}f_i z^{6i},\qquad
R_-=(x^3-4)\sigma^6=\sum_{j\ge0}r_jz^{6j},\qquad r_0=1.
\tag{1049.1}
$$
这里的 $f_N$ 就是原题的端点，所用系数都在已付清的首 $p$ 系数范围内。记
$$
P_{FR}(v)=\sum_{i+j=N}f_i r_jv^i.
\tag{1049.2}
$$
对原 Eisenstein norm-$p$ 表示
$$
A=\begin{pmatrix}\alpha&-\bar\beta\\\beta&\bar\alpha\end{pmatrix},
\qquad N\alpha+N\beta=p,
$$
仍取
$$
\gamma=-\bar\alpha/\beta,\qquad
\eta=\gamma^{-1},\qquad
T^- =\{\eta\in\mathbf F_{p^2}^{\times}:\eta^{p+1}=-1\}.
$$
原 R1012 的完整 norm-sphere 计数保证每个 $\eta\in T^-$ 都由恰十二个这种表示给出。

写 $s=\zeta-\zeta^2$，在 $\mathcal O/(3)$ 中取
$$
\alpha=a+a's,\qquad\beta=b+b's,
\qquad a,b\in\{1,-1\},\quad a',b'\in\mathbf F_3,
$$
$$
d_A^{(3)}=aa'+bb'\in\mathbf F_3,\qquad
e_A=\begin{cases}1,&\alpha\not\equiv0\pmod2,\\-1,&\beta\not\equiv0\pmod2.\end{cases}
\tag{1049.3}
$$
恰有一个模二分量非零；两者模 $s$ 都非零，均为原 norm 方程的直接后果。不要把 $d_A^{(3)}$ 和 R1025 的 index-one 标量 $d_A$ 混同。定义
$$
\phi_A=e_Aab\,\zeta^{d_A^{(3)}}\in\mu_6.
\tag{1049.4}
$$
令 $t^3=4$ 为原 $t\in\mathbf F_p$，并保留 R1027 已付清但未任意择号的 $\delta'_p\in\{1,-1\}$。

则准确有
$$
\boxed{\quad
\eta^5P_{FR}(\eta^6)=\frac{t^2\delta'_p}{12}\phi_A,
\qquad \eta\in T^-.
\quad}
\tag{1049.5}
$$
右端由 $\eta$ 唯一确定，详见下文的十二代表核对。尤其此完整卷积在所有方向都为单位，但指定的顶 Fourier 系数仍须另算。

原端点因此为
$$
\boxed{\quad
f_N=-\frac{t^2\delta'_p}{12(p+1)}
\sum_{\eta\in T^-}\eta\,\phi_A.
\quad}
\tag{1049.6}
$$
式中 $p+1$ 是有限域中的单位；写出它是为了保留实际正交投影的归一。

## 2. 实际三-primary 运输给完整输入截面

保留 R1020 的原截面
$$
U=x^2\sigma^6,\qquad R_+=(x^3+2)\sigma^6,\qquad Y_6=y\sigma^6.
$$
原实际三挠点、canonical lifts 和基为 R1020 (1020.13)–(1020.18)。特别
$$
F=A_F(\delta_1^-+\delta_{-1}^-),\qquad
R_-=\delta_0^-,\qquad A_F=\frac1{3t^2},
$$
$$
\delta_a^+=k_+(R_+-6aY_6/\sqrt3),\qquad
k_+=t^2/12,\quad a\in\{1,-1\}.
\tag{1049.7}
$$
平方根、$\zeta$、原三挠点顺序和 commutator 完全使用 R1020 的选择；不重新作相位归一。

令
$$
A_0=\begin{pmatrix}a&-b\\b&a\end{pmatrix},\qquad
S=\begin{pmatrix}d_A^{(3)}&ab'-ba'\\ab'-ba'&-d_A^{(3)}\end{pmatrix}.
$$
R1020 (1020.18) 给实际下降逆映射
$$
\mathcal K_{A,6}\Delta_\nu^-
=-36c_A\,\zeta^{-\nu^{\mathsf T}S\nu/2}\Delta_{A_0\nu}^+.
\tag{1049.8}
$$
在原输入 $F^p\boxtimes R_-^p$ 中只有 $\nu=(1,0),(-1,0)$。二者的相位均为 $\zeta^{d_A^{(3)}}$，因为 $-1/2=1$ 在 $\mathbf F_3$ 中成立；输出标签为 $(a,b)$、$(-a,-b)$。故其和准确为
$$
2k_+^2\left(R_+\boxtimes R_++12abY_6\boxtimes Y_6\right).
$$
由于 $A_F\in\mathbf F_p$，全部 scalar 的乘积是
$$
A_F^p(-36c_A)\,2k_+^2=-\frac{t^2}{6}c_A.
$$
于是
$$
\boxed{\quad
\mathcal K_{A,6}(F^p\boxtimes R_-^p)
=-\frac{t^2}{6}\zeta^{d_A^{(3)}}c_A
 \left(R_+\boxtimes R_++12abY_6\boxtimes Y_6\right).
\quad}
\tag{1049.9}
$$
这是原截面的完整等式。没有使用“任意 theta intertwiner 保乘法”，也没有仅由 CM 角色相同来认同两个不同来源。

## 3. 原零阶 jet 与完整卷积

原 $R_+(0)=1$，$Y_6(0)=0$。实际刚化 pullback 的原点值为一，因此 (1049.9) 右端的实际零阶读数是
$$
-\frac{t^2}{6}\zeta^{d_A^{(3)}}c_A.
\tag{1049.10}
$$
另一方面，对 $\Omega_{\gamma,6}(F^p\boxtimes R_-^p)$ 使用 R1016 (1016.11)。只有
$$
r=6i+4,\qquad s=6j,\qquad r+s=p-1,
$$
进入零阶读数，故 $i+j=N$。这里 $r,s$ 均为偶数，Wilson 给 $r!s!=-1$；原分布的 $(-6B)^{p-1}=1$。保留原 $\gamma^{-1}=\eta$，得到
$$
J_{00}\bigl(\Omega_{\gamma,6}(F^p\boxtimes R_-^p)\bigr)
=-\eta^4\sum_{i+j=N}f_i r_j\eta^{6i}
=-\eta^4P_{FR}(\eta^6).
\tag{1049.11}
$$
所有阶乘严格小于 $p$；实际 Frobenius 截面与解析截断的比较正是 R1016 已付的首 $p$ 矩形。没有除以一个未证整的 first-$p$ carry。

实际下降关系将 (1049.10)、(1049.11) 相等。再用原
$$
c_A=-\eta^2\mathcal C_N(\eta),\qquad
\eta^3\mathcal C_N(\eta)=-\delta'_p e_Aab/2
$$
即得到 (1049.5)。这是 R1025、R1027 的完整 scalar，不把共同符号改成一。

## 4. 十二个表示的实际相位不变性

固定方向的十二个表示由以下真实 norm-preserving 操作生成：
$$
(\alpha,\beta)\longmapsto(u\alpha,\bar u\beta),\quad u\in\mu_6,
\qquad
(\alpha,\beta)\longmapsto(-\beta,\alpha).
\tag{1049.12}
$$
第一个操作保持 $\gamma$。写 $u=u_0+u_1s\bmod3$，则 $u_0=\pm1$；$ab$ 不变，而且
$$
d_A^{(3)}\longmapsto d_A^{(3)}+u_0u_1(a^2-b^2)=d_A^{(3)}.
$$
模二的非零位置也不变，所以 $e_A$ 不变。

第二个操作把 $\gamma$ 送到 $\bar\beta/\alpha$，模 $p$ 由 $N\beta=-N\alpha$ 这仍是原 $\gamma$。它将 $ab$、$e_A$ 同时变号，且保持 $d_A^{(3)}$。因此两类操作均保持 $\phi_A$。结合完整十二计数，(1049.4) 是原方向上的确切值函数。

## 5. 原端点的正交抽取及范围

在 $T^-$ 上，只有总指数为 $p+1$ 的倍数时字符和才可能非零。因为 $0\le i\le N$，且 $6N=p-5<p+1$，
$$
f_Nr_0=\frac1{p+1}\sum_{\eta\in T^-}
 \eta^{-6N}P_{FR}(\eta^6).
$$
而 $r_0=1$，且
$$
\eta^{-6N-5}=\eta^{-p}=-\eta
$$
由 $\eta^{p+1}=-1$ 成立，代 (1049.5) 即得 (1049.6)。

此证明把原端点交给一个明确的一阶带相位方向矩。它没有证明该矩非零；也没有由每个加数非零推出其和非零。更没有删除原同 $h$ 问题的 primitive/Legendre mask。后续如使用 norm sphere、theta 级数或 character sum，必须保留 (1049.4) 的完整相位与 (1049.6) 的一次权重。

## 6. 同一个固定 theta 级数与积分乘积

上面的一阶方向矩还可以完全改写为固定输入的第 $p$ 个系数。
这一步保留全部实际相位，不把另一条同 CM 来源的级数代入。

令 $\mathcal O=\mathbf Z[\zeta]$，称
$\alpha_0\in\mathcal O$ 为 primary 当且仅当 $\alpha_0\equiv1\bmod3$。
单位约化 $\mu_6\longrightarrow(\mathcal O/3)^\times$ 是双射：
两边都有六个元素，$\pm1,\pm\zeta,\pm\zeta^2$ 的约化互异。
记其逆映射为 $\rho$。对 (1049.3) 的原表示，
$
\alpha\beta=ab(1+d_A^{(3)}s)
          =ab\zeta^{-d_A^{(3)}}\pmod3.
$
所以原相位准确为
$
\phi_A=e_A\,\overline{\rho(\alpha\beta)}.
\tag{1049.13}
$
置 $\alpha_0=\alpha/\rho(\alpha)$、
$\beta_0=\beta/\rho(\beta)$，则它们是唯一的 primary 代表。
由 $N\alpha+N\beta=p$，在模 $p$ 中
$\eta=\alpha/\bar\beta$，故
$
\eta\phi_A=e_A\,\frac{\alpha_0}{\bar\beta_0}.
\tag{1049.14}
$
全部分母在 $p$ 处为单位，因为 $0<N\alpha,N\beta<p$；
$p$ 在 $\mathcal O$ 惰性，范数为 $p$ 的单个元素不存在。

每个 primary 有序对有 $36$ 个独立单位代表，而每个原方向有
$12$ 个 norm-$p$ 表示。因此
$
\sum_{\eta\in T^-}\eta\phi_A
=3\sum_{\substack{\alpha_0,\beta_0\ {\rm primary}\\
                 N\alpha_0+N\beta_0=p}}
 e_A\frac{\alpha_0}{\bar\beta_0}.
\tag{1049.15}
$
$2$ 在 $\mathcal O$ 惰性，范数奇偶说明两分量恰有一个能被 $2$ 整除。
交换两个 primary 分量使 $e_A$ 变号，且
$
\frac{\beta_0}{\bar\alpha_0}
=-\frac{\alpha_0}{\bar\beta_0}\pmod p.
$
所以两个奇偶方向贡献相同，只取 $\alpha_0$ 奇、$\beta_0$ 偶并乘二。
唯一写 $\beta_0=-2\gamma_0$，其中 $\gamma_0$ 仍 primary，得到
$
\sum_{\eta\in T^-}\eta\phi_A
=-3\sum_{\substack{\alpha_0,\gamma_0\ {\rm primary}\\
                  N\alpha_0+4N\gamma_0=p}}
       \frac{\alpha_0}{\bar\gamma_0}.
\tag{1049.16}
$

定义两个与 $p$ 无关的确切级数
$
\Theta(q)=\sum_{\alpha_0\ {\rm primary}}\alpha_0q^{N\alpha_0}
         =\sum_{n\ge1}a_nq^n,\qquad
\mathcal E_\Theta(q)=\sum_{n\ge1}\frac{a_n}{n}q^n.
\tag{1049.17}
$
共轭保持 primary 条件，故 $a_n\in\mathbf Z$。
第二个级数的常数项取零，且
$q\,d\mathcal E_\Theta/dq=\Theta$。
式 (1049.16) 的最后一个和准确等于
$[q^p]\Theta(q)\mathcal E_\Theta(q^4)$，
因为 $\alpha_0/\bar\gamma_0=\alpha_0\gamma_0/N\gamma_0$。
每个所用 $N\gamma_0<p$，归约模 $p$ 合法。

结合 (1049.6)，得到固定输入公式
$
\boxed{\quad
f_N=\frac{t^2\delta'_p}{4(p+1)}
 [q^p]\Theta(q)\mathcal E_\Theta(q^4)\pmod p .
\quad}
\tag{1049.18}
$
所有 $36/12$、交换因子二、$\beta_0=-2\gamma_0$ 的负号和原
$\delta'_p$ 均保留。此恒等式不需要另认同一个 eta-product，
也不以仅仅相同的 CM 角色认同另一个 theta 或 Eichler 截面。
它没有证明该指定第 $p$ 项为单位，原同 $h$ 问题亦仍须继续。

## 来源

- [R1012](R1012-original-p-similitude-divided-high-coordinates-and-critical-bridge.md)，原 $\mathcal O\oplus\mathcal O j$ 的 norm-$p$ 向量、每方向十二个真实表示。
- [R1016](R1016-original-small-index-theta-and-complete-convolution-units.md)，*Original small-index theta and complete convolution units*，(1016.11) 的实际首 $p$ 分布及刚化 frame。
- [R1020](R1020-original-critical-convolution-complete-theta-scalar-bridge.md)，*Original critical convolution complete theta scalar bridge*，(1020.13)–(1020.18) 的真实三挠点、基常数、Weyl lifts 和完整相位。
- [R1025](R1025-original-theta-exact-mod-six-direction-phases.md)，*Original theta exact mod-six direction phases*，(1025.1)–(1025.2)。
- [R1027](R1027-original-level-p-squared-theta-distribution-and-constant-one.md)，*Original level-p-squared theta distribution and constant one*，原 $D_p=1$ 与 $\delta'_p\in\{\pm1\}$。

全部推导为纸面有限代数；root 已独立核对实际零阶分布、十二代表相位及正交抽取。未执行数学程序、未重算任何旧窗口。Serre 主目标仍 OPEN。
