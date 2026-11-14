# dyadic 平凡向量的准确相位，以及 E0 的固定 theta 截面

日期：2026-11-12。状态：以下局部向量、$L=34$ 的选择和参考曲线的
theta 平方公式均已证明。

本篇直接核对 $2$ 处的 Weil 表示，不把只对奇剩余特征证明的
lattice 公式外推到 $2$。它允许 R46 的固定整数明确取为
$L=34$，并给出参考曲线 $E_0:y^2=x^3-x$ 的具体截面。

## 1. 规范与外部输入

令

$$
 K=\mathbb Q(i),\quad \lambda=1+i,\quad
 E_0:y^2=x^3-x,\quad
 \chi_0=\psi_0\mathrm N^{-1/2}.
$$

$\psi_0$ 的导子为 $\lambda^3$。这一导子及
$K(E_0[\lambda^3])=K$ 可直接见 Coates–Liang–Sujatha（2009），
*The Tate-Shafarevich group for elliptic curves with complex multiplication*，
Lemmas 3.1–3.2 和 (44)：

<https://arxiv.org/pdf/0901.3832>。

采用全局标准加法特征；在无穷处是 $e^{2\pi_{\mathbb C}ix}$，
在 $\mathbb Q_2$ 上是

$$
 \psi_2(x)=e^{-2\pi_{\mathbb C}i\{x\}_2}.
$$

自对偶 Haar 测度满足 $\operatorname{vol}(\mathbb Z_2)=1$。
置 $\zeta_8=e^{\pi_{\mathbb C}i/4}$。

使用 Yang 1999，*Nonvanishing of central Hecke L-values and rank of
certain elliptic curves*，Appendix (A1)–(A3) 的标准 splitting：

<https://www.cambridge.org/core/services/aop-cambridge-core/content/view/915B51D40C0BD146C3DBC94DE4041BDD/S0010437X99000433a.pdf/nonvanishing_of_central_hecke_lvalues_and_rank_of_certain_elliptic_curves.pdf>。

这些是 Rao/Kudla 的一般特征零公式；以下并不使用该文后续的
奇剩余特征特征函数公式。
取 $\delta=i,\alpha=1$，则对 $g=x+iy\in K_2^1$，

$$
 \iota(g)=\begin{pmatrix}x&y\\-y&x\end{pmatrix},\qquad
 \omega(g)=\mu(g)r_S(\iota(g)),
                                                               \tag{1}
$$

$$
 \mu(g)=\chi_{0,2}(i(g-1))\,
        \gamma_2(y(1-x)\psi_2)\,
        (-1,-2y(1-x))_2 .                                    \tag{2}
$$

其中 $r_S$ 是 Rao 的标准截面。对本篇出现的非零下左项 $C$，
其核采用与 Yang 1997 (2.28) 一致的规范：

$$
 (r_S(A)\phi)(u)=|C|_2^{-1/2}
      \int_{\mathbb Q_2}
        \psi_2\!\left(\frac{A_{11}u^2+2uv+A_{22}v^2}{2C}\right)
        \phi(v)\,dv .                                        \tag{3}
$$

## 2. 实际局部 Hecke 特征

对任意 $u\in\mathcal O_{K_2}^\times$，存在唯一
$\epsilon\in\mu_4$ 使 $u\equiv\epsilon\pmod{\lambda^3}$，且

$$
 \chi_{0,2}(u)=\epsilon,\qquad
 \chi_{0,2}(\lambda)=\zeta_8 .                               \tag{4}
$$

第一式来自 $\psi_0$ 的 primary-generator 规范：
若 $u\equiv\epsilon$，则 $\epsilon^{-1}u$ 是 primary，
有限特征为 $\epsilon^{-1}$；idelic 局部分量取其逆。
第二式也可不依赖记号约定而由全局主 idèle 关系核对：
$\lambda$ 在所有奇有限位是单位，
$\chi_{0,\infty}(\lambda)=\zeta_8^{-1}$，故 $2$ 处分量必须为
$\zeta_8$。特别地 $\chi_{0,2}(2)=1$。

对 E17 来说局部分量相同。
确实 $17\in1+16\mathbb Z_2=(\mathbb Z_2^\times)^4$，
取 $a\in\mathbb Z_2^\times$、$a^4=17$ 后，
$(x,y)\mapsto(a^2x,a^3y)$ 给与 CM 作用交换的
$E_0\simeq E_{17}$。所以它们在 $K_2$ 上的 Tate 表示及 Hecke
局部分量一致。

## 3. 两个元素生成整个 dyadic norm-one 群

置

$$
 G_2=K_2^1,\qquad
 g_*=\frac{-3+4i}{5}=\frac{1+2i}{1-2i}.
$$

若 $x^2+y^2=1$，则 $x,y\in\mathbb Z_2$，且恰有一个为奇数。
若 $x$ 为奇数，则模 $8$ 可见 $4\mid y$，而模 $16$ 可见
$x\equiv\pm1\pmod8$。乘一个 $\mu_4$ 元后可令
$x\equiv1\pmod8,\ y\in4\mathbb Z_2$。因此

$$
 G_2=\mu_4\times U,\qquad
 U=G_2\cap(1+4\mathcal O_{K_2}).
                                                               \tag{5}
$$

$2$-进对数与指数给

$$
 \log:U\xrightarrow{\sim}4i\mathbb Z_2 .
                                                               \tag{6}
$$

这是因为对数的迹是范数的对数，norm-one 条件恰要求迹零；
反向由指数成立。又
$g_*-1=4(-2+i)/5$，故
$\log g_*\in4i\mathbb Z_2^\times$。所以 $g_*$ 拓扑生成 $U$，
$i,g_*$ 拓扑生成 $G_2$。

## 4. $\mathbf1_{\mathbb Z_2}$ 的两个准确特征值

记 $\phi=\mathbf1_{\mathbb Z_2}$。

### 4.1 元素 $i$

此时 $x=0,y=1$，

$$
 i(i-1)=-\lambda,\quad
 \chi_{0,2}(-\lambda)=-\zeta_8,\quad
 \gamma_2(\psi_2)=\zeta_8^{-1},\quad
 (-1,-2)_2=-1.
$$

所以 $\mu(i)=1$。$r_S(\iota(i))$ 是标准 Fourier 变换，
自对偶性给 $r_S(\iota(i))\phi=\phi$。因此

$$
                            \omega(i)\phi=\phi .             \tag{7}
$$

### 4.2 元素 $g_*$

这里 $x=-3/5,y=4/5$。首先

$$
 i(g_*-1)=-\frac45(1+2i).
$$

$-1/5$ 与 $1+2i$ 在 (4) 下的值都为 $-1$，所以
$\chi_{0,2}(i(g_*-1))=1$。其次

$$
 y(1-x)=\frac{32}{25},\qquad
 \gamma_2\!\left(\frac{32}{25}\psi_2\right)=\zeta_8^{-1},
 \qquad
 (-1,-64/25)_2=-1.
$$

所用两个 Weil index 均可直接由
$\psi_2$ 的有限二次 Gauss 和计算；
$32/25$ 的平方类为 $2$，其 unit part 为 $1$ 模 $8$。
于是

$$
                            \mu(g_*)=-\zeta_8^{-1}.           \tag{8}
$$

不能在这里忽略 Rao 核的相位。
由 $C=-4/5$，式 (3) 给

$$
 (r_S(\iota(g_*))\phi)(u)
   =2\int_{\mathbb Z_2}
        \psi_2\!\left(\frac{3u^2-10uv+3v^2}{8}\right)dv .
                                                               \tag{9}
$$

当 $u\in\mathbb Z_2$ 时，

$$
 \frac{3u^2-10uv+3v^2}{8}
  =\frac38\left(v-\frac53u\right)^2-\frac23u^2.
$$

最后一项整，平移也保持 $\mathbb Z_2$，所以 (9) 等于

$$
 2\int_{\mathbb Z_2}\psi_2(3v^2/8)\,dv
  =\frac28\sum_{v\bmod8}\zeta_8^{-3v^2}
  =\zeta_8^{-3}.                                             \tag{10}
$$

当 $u\notin\mathbb Z_2$ 时，(9) 为零：
函数 $\psi_2(3v^2/8)\mathbf1_{\mathbb Z_2}(v)$
在平移 $4\mathbb Z_2$ 下不变，其 Fourier 变换支撑在
$\tfrac14\mathbb Z_2$；频率 $-5u/4$ 不在该群中。
因此

$$
 r_S(\iota(g_*))\phi=\zeta_8^{-3}\phi,\qquad
 \omega(g_*)\phi=(-\zeta_8^{-1})\zeta_8^{-3}\phi=\phi .
                                                               \tag{11}
$$

结合 (5)–(7)、(11) 与表示的连续性，证明

$$
 \boxed{\quad
 \omega(g)\mathbf1_{\mathbb Z_2}
       =\mathbf1_{\mathbb Z_2}\quad(g\in G_2).
 \quad}                                                       \tag{12}
$$

该向量的范数为一。Yang 1997 Corollary 2.4 的局部重数一表明，
它正是 R46 所需的平凡角色线；原来的单位范数向量至多相差一个
固定代数相位。

## 5. 对 E17，可明确取 $L=34$

在 $2$ 处，(12) 的向量支撑在 $\mathbb Z_2$，
并在平移 $\mathbb Z_2$ 下不变。
实结构笔记已直接计算 $17$ 处的紧平均向量：
其支撑在 $17^{-1}\mathbb Z_{17}$，
并在平移 $17\mathbb Z_{17}$ 下不变。
其他有限位取 $\mathbf1_{\mathbb Z_\ell}$。

因此全局有限向量支撑在 $34^{-1}\widehat{\mathbb Z}$，
并在平移 $34\widehat{\mathbb Z}$ 下不变。R46 的偶整数可取

$$
                       \boxed{L=34,\qquad d=1156.}           \tag{13}
$$

本篇证明的是这个可用的具体值，不声称它在所有 theta 规范中最小。

## 6. E0 的 theta 截面完全显式

对 E0，所有有限位现在都可取 $\mathbf1_{\mathbb Z_\ell}$。
故固定 Hermite 生成函数为

$$
 B(t)=e^{-t^2}
       \sum_{n\in\mathbb Z}e^{-\pi_{\mathbb C}n^2+
                                         2\sqrt{2\pi_{\mathbb C}}nt}.
                                                               \tag{14}
$$

令 $\Omega_0>0$ 为 E0 的最小正实周期，
$c_0=\sqrt{2\pi_{\mathbb C}}/\Omega_0$。
这对应 $L_0=2,d_0^{\rm sec}=4$。
$B(c_0z)$ 与 $\sigma_0(z)^4$ 有相同自动因子；
其比值是椭圆函数，在 $O$ 的极点阶至多为四。

由 Jacobi $\theta_3$ 的零点，
$B(c_0z)$ 的四个零点恰为

$$
 z\equiv\frac{-1+i}{4}\Omega_0
            \pmod{\tfrac12\Omega_0\mathbb Z[i]}.
$$

它们正是 $[2]Q=(0,0)$ 的四个解。
E0 的 duplication 公式

$$
 x([2]Q)=\frac{(x(Q)^2+1)^2}{4x(Q)(x(Q)^2-1)}
$$

说明 $x^2+1$ 的四个零点也是这些点。
比较除子，再在 $O$ 比较常数项，得到精确恒等式

$$
 \boxed{\quad
 \frac{B(c_0z)}{B(0)}
      =(x(z)^2+1)\sigma_0(z)^4
      =:S_0(z)=\sum_{m\ge0}s_m^{(0)}z^m .
 \quad}                                                       \tag{15}
$$

因此 $S_0(0)=1$，全部系数有理，只有 $4\mid m$ 的系数可能非零。
特别地

$$
                         s_4^{(0)}=\frac43 .                 \tag{16}
$$

## 7. 参考中央平方的常数是 $1/4$

在 $4\mid m$ 的权族上，E0 的有限导子始终为 $f_0$。
用同一有限向量及 Yang 的范数公式，重复 R46 中已逐式证明的
Hermite--sigma 换元，所有不随 $m$ 变化的常数可由 $m=0$ 固定。
本篇 (15) 令 $s_0^{(0)}=1$，而
[参考中央值笔记](2026-11-12-rank-zero-reference-central-inert-value.md)
的 duplication 计算给
$d_0^{(0)}/f_0=1/4$。
因为 $Nf_0=8$、截面次数为 $4$，准确公式为

$$
 \boxed{\quad
 e_m^{(0)}:=\frac{d_m^{(0)}}{f_0^{2m+1}}
       =\frac14\,32^{-m}(s_m^{(0)})^2
          \qquad(4\mid m).
 \quad}                                                       \tag{17}
$$

这是 E0 的参考公式，不把 E17 的有限四次特征改成平凡特征。

作为独立的规范核验，直接在有限代数微分公式中取 $m=4$，
$U=(1+i)/2,X=i,Y=1-i$，得到

$$
 d_4^{(0)}=\frac{1+i}{288},\qquad
 e_4^{(0)}=\frac1{2359296}
         =\frac14\,32^{-4}\left(\frac43\right)^2 .
$$

这个精确有理数核验同时保留了中央系数、阶乘和 sigma 的规范。
参考惰性首坏项的赋值已由前一笔记独立证明，不依赖此核验。
