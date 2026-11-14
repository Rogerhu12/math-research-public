# R375：原倾斜 Jacobi 核的双 Frobenius、完整来源族及返回原中央

日期：2026-11-14。**状态：已证明。** 对 R367 的同一 $A,\mathcal E$
和原余三因子，构造真正的 $(Z,X)$ 联合。
在一个固定无穷普通素数族上，两个方向的真实完整 theta 空间分别为
$\mathcal S_{1728}$、$\mathcal S_{448}$，且都由同 degree 的单 sigma 锚
确定绝对 $p$-core。它们给出包含原来源 $T_1=S$ 的完整族，并有
$\nu_{T_\kappa}|_p=\lambda_\sigma[\kappa]_*\nu_S$。
倾斜变量的变换、原输出的变化、全部加法 carry 和 tame 均保留。
本篇不把新来源的 unit 部分或叶六支平均自动赋予原 $J'_S(0)$ 的零性。

## 1. 固定原对象及素数族

沿用 R367：
$$
E_b:y^2=x^3+b,\quad b=17,\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad\gamma=3+\omega,
$$
$$
A=\sigma(z)\sigma(2z)\sigma(\delta z),\qquad
B=\sigma(2\delta z)\sigma(\gamma z)\sigma(\bar\gamma z),
$$
$$
S=-AB/84,\qquad
\mathcal E(w)=\frac1{2\delta}[z^3]\,
                   \sigma(z-7w)\sigma(2(z+w))\sigma(\delta(z+w)).
\tag{1}
$$
$A,B,\mathcal E$ 的真实 degree 分别为 $8,26,56$；
型分别为 $3,3,0$，且
$$
A=2\delta z^3+\cdots,\quad
B=14\delta z^3+\cdots,\quad \mathcal E(0)=1,\quad S=z^6+\cdots.
\tag{2}
$$
所有测度都用原同一普通周期 $\Omega$：
$\int e^{zx/\Omega}d\nu_G(x)=G(z)$。

设
$$
\pi=\psi_{17}(\mathfrak p),\quad \pi\bar\pi=p,\quad
\varepsilon=\psi_0(\mathfrak p)/\psi_{17}(\mathfrak p),\quad
\kappa=p/\bar\pi^2,\quad \lambda=\lambda_\sigma=\varepsilon^3/\bar\pi.
\tag{3}
$$
$\nu_\sigma|_p=\lambda[\kappa]_*\nu_\sigma$ 已由 R316 付清。
本篇采用固定集合
$$
\boxed{
\mathcal P_J=\{p>7:\ p\equiv1\pmod3,\
                  \pi/\bar\pi\equiv1\pmod{24192\mathcal O_K}\},
\qquad 24192=2^7\cdot3^3\cdot7.
}
\tag{4}
$$
分母在该模数可逆。该集合包含有限 Galois 扩张
$K(E_{17}[24192])$ 的所有好全分裂有理素数，故由 Chebotarev
密度定理是无穷的固定普通素数集合。
全分裂使实际 Frobenius 对该挠点群为恒等，从而实际
$\pi,\bar\pi$ 都为一模该模数；这里没有任取范数 $p$ 的生成元。

## 2. 两个整个空间的绝对 core：真锚而非项目相位

记 $\mathcal S_N=\sigma^NL(NO)$。
R300 §§2–2.1 对偶 $N$ 给同一原测度的完整 trace
$$
T_p=\frac{\bar\pi}p\mathscr M_\pi,\qquad
T_p\nu=\bar\pi[\bar\pi^2]_*
      (x\mapsto x/p)_*(\nu|_p),
\tag{5}
$$
$$
\mathscr M_a(\sigma^Nf)
=\sigma^N\operatorname{Tr}_{[a]}
       [(r_{\bar a}/r_a)^N f\circ[\bar a]],\qquad
r_a=\sigma(az)/\sigma(z)^{Na}.
\tag{6}
$$
原 division、全部 Gaussian、根单位平均的 $1/p$、
半特征和对称 theta lift 的中心均包含于 (5)–(6)。
它们的证明对本节的偶数 $N$ 原样适用，不仅对 $N=34$。

若 $\pi/\bar\pi=1\bmod2N$，完整对称 lift 交织给
$\mathscr M_\pi$ 与全部 Heisenberg 生成元交换。
primitive 交换子使其 $N$ 维表示不可约，所以 $T_p$ 为标量。
这仍须在同 degree 的真实来源上确定标量。

本篇使用三个明确的 norm：
$$
64=N(8),\qquad448=N(8\gamma),\qquad1728=N(24\delta).
\tag{7}
$$
相应的原截面 $\sigma(8z),\sigma(8\gamma z),\sigma(24\delta z)$
分别属于这些完整空间。其尺度在本篇普通处均为单位。
因为原限制到 $p$ 与单位缩放交换，R316 的同一 sigma core 给
它们的 $T_p$ 标量全部为 $\varepsilon^3$。
(4) 又蕴含模 $128,896,3456$ 的完整交织相同。
因此准确得到
$$
\boxed{
\nu_G|_p=\lambda[\kappa]_*\nu_G
\quad\text{对整个 }\mathcal S_{64},\mathcal S_{448},\mathcal S_{1728}.
}
\tag{8}
$$
这包含所有型、所有质量列，不是仅某条有限本征线。
标量由非零截面身份锚定，没有除以未知 Mellin 值。

此外 (4) 在原 degree 七给完整标量：
R368 的奇 order 对称 lift 与同 degree $\sigma(\gamma z)$ 锚使
$$
\lambda_7=\lambda_{23}=\lambda.
\tag{9}
$$
结合 R367 的原关系，
$$
\boxed{\lambda_A\lambda_{\mathcal E}
       =\lambda_\sigma\lambda_{23}=\lambda^2.}
\tag{10}
$$
此处不需要分别把 $\lambda_A,\lambda_{\mathcal E}$ 认成 $\lambda$；
degree 八和五十六没有在本节被错误地用一个不存在的 sigma norm 锚替换。

## 3. 倾斜域的真实联合坐标

令 $y,r,s$ 分别是 $\nu_A,\nu_{\mathcal E},\nu_B$ 的原加性变量，
并保符号和归一
$$
d\mu=-\frac1{84}\,d\nu_A(y)d\nu_{\mathcal E}(r)d\nu_B(s).
$$
其原输出边际为 $Y=y+s$，因为 $\nu_{\mathcal E}$ 质量一，
故 $Y_*\mu=\nu_S$。更准确，R367 的完整联合表明，
$\mu$ 是原六输入在 $R$ 方向作 $\mu_6$ 投影、保留
$(Y_{123},R,Y_B)$ 后的同一联合；$Q_{23}$ 的质量一边际已被积分。
因此这里的辅助因子有原输入接口。

本篇的实际新变量是
$$
\boxed{
X=7y+r,\qquad Z=Y-X/8=s+(y-r)/8,\qquad Y=Z+X/8.
}
\tag{11}
$$
记 $\rho=(Z,X)_*\mu$。这是原有界测度的直接推前，
并非任取二维乘积。其联合变换为
$$
\boxed{
\mathcal H(z,w)
=-\frac1{84}A(z/8+7w)\mathcal E(w-z/8)B(z).
}
\tag{12}
$$
若原倾斜表达用 $w$ 写作
$-A(z+7w)\mathcal E(w)B(z)/84$，
则 $w'=w+z/8$ 后正是 (12) 的 $w'$ 表达。
因此 core 沿 $X$ 时保持的是 $Z$，不是原 $Y$ 或 $y$。

这里可直接核对自动因子，避免把倾斜域误换成直域。
对 $w\mapsto w+\lambda_0$，$A$ 的 $7\lambda_0$ 位移产生
关于 $z$ 的 $+7\eta_{\lambda_0}z$；
$\mathcal E$ 的位移产生 $-7\eta_{\lambda_0}z$。
二者准确相消，剩下
$$448\eta_{\lambda_0}(w+\lambda_0/2).$$
所以每个 $z$ 系数确实属于固定 $\mathcal S_{448}$。

再置 $z=8v$，则
$$
\mathcal H(8v,w)
=-A(v+7w)\mathcal E(w-v)B(8v)/84 .
\tag{13}
$$
$v$ 方向的 degree 为 $8+56+64\cdot26=1728$；
与 $w$ 的交叉项为 $8\cdot7-56=0$。
两个方向的半特征都是上述偶 degree 的原特征。
故它是真正
$\mathcal O(1728O)\boxtimes\mathcal O(448O)$ 的截面。

(8) 因而逐系数给**全二维测度**的两个 core：
$$
\boxed{
\rho|_{X\in p}=\lambda[\mathrm{id},\kappa]_*\rho,\qquad
\rho|_{Z\in p}=\lambda[\kappa,\mathrm{id}]_*\rho.
}
\tag{14}
$$
第二式先对 $8Z$ 用 $\mathcal S_{1728}$，再用八为单位换回 $Z$。
系数身份决定全部联合矩；有界测度的 Amice 唯一性给 (14)。
没有遗漏与 $z$ 有关的 theta-character：
它已经由 (12)–(13) 的原自动因子计算支付。

## 4. 平移球的完整来源族

对 $\xi\in\mathbf Z_p$ 定义实际有界来源族
$$
\boxed{
G_\xi(z)=
 A\left(\frac{1+7\xi}{8}z\right)
 \mathcal E\left(\frac{\xi-1}{8}z\right),\qquad
T_\xi(z)=-G_\xi(z)B(z)/84 .
}
\tag{15}
$$
这是同一原测度的线性推前：
$$
\nu_{T_\xi}=(Z+\xi X/8)_*\rho.
\tag{16}
$$
特别
$$
\boxed{G_1=A,\quad T_1=S,\quad
G_0=A(z/8)\mathcal E(z/8).}
\tag{17}
$$
最后用了 $\mathcal E$ 为型零，故为偶函数。

令
$$
\mathcal C_n=Y_*(1_{X\in p^n}\mu),\qquad n\ge0.
$$
由第一个 (14)，其完整原变换准确是
$$
\boxed{
\mathcal C_n=\lambda^n\nu_{T_{\kappa^n}}.
}
\tag{18}
$$
确实，保持 $Z$ 而将 $X$ 乘 $\kappa^n$，把原 $Y$ 变成
$$
Z+\kappa^nX/8
=\frac{1+7\kappa^n}{8}y
 +\frac{\kappa^n-1}{8}r+s.
\tag{19}
$$
这就是 (15)，而不是保持原 $y$ 的一个免费 core。

等价的平移球式是
$$
\boxed{
\int e^{zy/\Omega}\,
 \nu_{\mathcal E}(-7y+p^n)\,d\nu_A(y)
=\lambda^nG_{\kappa^n}(z).
}
\tag{20}
$$
这一部分式也可只用 $\mathcal S_{448}$ 证明，不需要原 $B$。
详细的 tilt 计算如下：
$H_z(w')=A(z/8+7w')\mathcal E(w'-z/8)$ 是固定
$\mathcal S_{448}$ 的形式 $z$ 族；
$A(z+7w)\mathcal E(w)=H_z(w+z/8)$。
若 $\eta_z$ 是 $H_z$ 的原测度，左边正是
$$
\int_{p^n}e^{zx/(8\Omega)}\,d\eta_z(x)
=\lambda^n\int e^{z\kappa^nx/(8\Omega)}\,d\eta_z(x)
=\lambda^nH_z(\kappa^nz/8).
$$
这明确保留了 tilt 的指数，且结果恰是 (20)。
所有身份也由实际有界联合 $\rho$ 给出，不需要对形式参数交换一个未收敛的无限和。

## 5. 真正总输出的 p-core 返回原 S

现在 $\xi\in p\mathbf Z_p$ 时，
$Z+\xi X/8$ 在 $p$ 中当且仅当 $Z$ 在 $p$ 中。
第二个 (14) 因而直接给
$$
\boxed{
\nu_{T_\xi}|_p
=\lambda[\kappa]_*\nu_{T_{\xi/\kappa}},
\qquad \xi\in p\mathbf Z_p.
}
\tag{21}
$$
这是同一总输出的测度式，全部相加 carry 都在 (11)–(14) 内。
尤其
$$
\boxed{
\nu_{T_\kappa}|_p=\lambda[\kappa]_*\nu_S,\qquad
\nu_{T_0}|_p=\lambda[\kappa]_*\nu_{T_0}.
}
\tag{22}
$$
不只是一个裸有限空间映射，也不是只比较首系数。

以下 $T_0^{\rm lim}$ 专指参数 $\xi=0$ 的来源；
$T_{\kappa^0}=T_1=S$ 则是深度零的来源，两者不混用。
对整数深度 $n\ge1$，(21) 迭代为
$$
\nu_{T_{\kappa^n}}|_{p^j}
=\lambda^j[\kappa^j]_*\nu_{T_{\kappa^{n-j}}},
\qquad 0\le j\le n.
\tag{23}
$$
超过第 $n$ 环带后，使用原 S 已付的
$\lambda_S=\bar\pi^{-1}$ core，故对 $j\ge n$
$$
\boxed{
\nu_{T_{\kappa^n}}|_{p^j}
=\lambda^n\lambda_S^{j-n}[\kappa^j]_*\nu_S.
}
\tag{24}
$$
这里的 $\lambda_S$ 与 $\lambda$ 没有被误合并。

(18) 还给原倾斜域的完整递推
$$
\boxed{
\mathcal C_n|_p=\lambda^2[\kappa]_*\mathcal C_{n-1},
\qquad n\ge1,\qquad \mathcal C_0=\nu_S.
}
\tag{25}
$$
(23)–(25) 指定其全部非单位输出，仍保留每一层真实 unit 余项。

## 6. 全 tame Mellin 与所保留的质量

置 $d=p-1$，记 $J_{\xi,\ell}(u)$ 为 $\nu_{T_\xi}$ 的单位 Mellin：
$$
J_{\xi,\ell}(u)=
 \int_{\mathbf Z_p^\times}
 \omega_p(x)^\ell\langle x\rangle^{du}\,d\nu_{T_\xi}(x).
$$
第 $j$ 环带先将变量除以 $p^j$ 归一。
对 $j\le n$，(23) 给准确式
$$
\boxed{
J_{\kappa^n,\ell}^{[j]}(u)
=\lambda^j\omega_p(\bar\pi)^{-2j\ell}
 \langle\bar\pi\rangle^{-2jdu}
 J_{\kappa^{n-j},\ell}(u).
}
\tag{26}
$$
当 $j=n$ 时，右边最后一项就是原 $J_{S,\ell}(u)$；
当 $j>n$ 时，标量改为
$\lambda^n\lambda_S^{j-n}$，最后一项仍为 $J_{S,\ell}$。
导数始终保留
$$
J'_{\kappa^{n-j},\ell}(0)
-2jd\log_p(\bar\pi)J_{\kappa^{n-j},\ell}(0).
\tag{27}
$$
principal 分支的质量在这里确为零：
$T_\xi(0)=0$，(21) 给 $\xi\in p\mathbf Z_p$ 的非单位质量零，
而 $\xi=1$ 是原 S 的已付质量零。
其他 tame 的质量项不凭此删除。

因此若原 $J'_S(0)=0$，(26) 真正控制的是这些已指定的非单位环带。
它没有同时令 $J'_{\kappa^n,0}(0)$ 的 unit 部分为零。

## 7. 原 y-unit 边界与六叶分支

(20) 的原 $y$ 非单位部分必须另付。
对 $n\ge1$，在 $7y+r\in p^n$ 内，$y$ 非单位必使 $r$ 也非单位。
使用两条实际 core，得到部分输出测度的非单位项
$$
\lambda_A\lambda_{\mathcal E}[\kappa]_*
 \left(\int \nu_{\mathcal E}(-7y+p^{n-1})\,d\nu_A(y)\right).
$$
在本篇类上 (10) 是 $\lambda^2$。故若 $B$ 仍按原变量保留，完整
$y$-unit 来源为
$$
\boxed{
\mathcal C_n^{\,y\times}
=\lambda^n\left(
 \nu_{T_{\kappa^n}}-\lambda\nu_{\widetilde T_{\kappa^{n-1}}}
\right),\qquad
\widetilde T_\xi(z)=-G_\xi(\kappa z)B(z)/84.
}
\tag{28}
$$
注意只有 $G_\xi$ 被缩放；$B(z)$ 没有变成 $B(\kappa z)$。
因此这不是 $\lambda[\kappa]_*\nu_{T_\xi}$，不能从 Mellin 中拉出一个
整体的 $\langle\kappa\rangle^{du}$。

R367 的原六个叶分支再有 $Q_{23}\in p^n$，
其实际参考质量为 $\lambda_7^n=\lambda^n$。
于是未除以六的真实并域在总输出上的测度正是
$$
\boxed{
\mathcal L_n^{(6)}
=6\lambda^{2n}\left(
 \nu_{T_{\kappa^n}}
 -\lambda\nu_{\widetilde T_{\kappa^{n-1}}}
\right).
}
\tag{29}
$$
每个符号、系数、原 partial-unit 条件和最终 output-unit 条件都保留。
右边可直接取全部 tame Mellin；它仍是六个真实分支的并，
不是原单一 unit 叶支。

若原第 $4,5,6$ 输入另有独立深度限制，则 $B$ 必须换成对应的受限卷积。
$\mathcal S_{1728}$ 的第 3 节证明针对本篇完整原 $B$；
不能未经证明把它应用到任意独立叶限制后的 $B$。
这是与 R339 全独立 grid 对接时的准确范围。

## 8. 完整极限及一个固定补偿行

$\xi=\kappa^n\to0$ 时，(15) 的系数是实际 unit 缩放，
其原有界测度弱收敛到 $\nu_{T_0^{\rm lim}}$。
更准确，对整值 1-Lipschitz 测试，差的赋值至少 $n$：
输出位移是 $\kappa^nX/8$，且原所有测度有统一整范数。
同样的估计适用于全部原 unit Mellin 在 $u\in\mathbf Z_p$ 的值
及中央导数；unit 指示是开闭的，log 在每个 unit 剩余类上有该估计。

因此 (18) 的规范化极限为
$$
\lambda^{-n}\mathcal C_n\ \longrightarrow\ \nu_{T_0^{\rm lim}},
$$
而 (29) 的规范化极限是
$$
\boxed{
(6\lambda^{2n})^{-1}\mathcal L_n^{(6)}
\ \longrightarrow\
\nu_{T_0^{\rm lim}}-\lambda\nu_{\widetilde T_0^{\rm lim}}.
}
\tag{30}
$$
第二式的误差在同样测试下至少为 $p^n$；
第二项的 $\kappa$ 缩放补偿了 $n-1$ 所损的一阶。
单位 $\lambda^n$ 没有被当作趋零的尾。

(30) 中固定的补偿并非免费的整体 depletion。
真实差写成
$$
\lambda\left([\kappa]_*\nu_{T_0^{\rm lim}}
                   -\nu_{\widetilde T_0^{\rm lim}}\right),
$$
其整个来源准确为
$$
-\frac{\lambda}{84}G_0(\kappa z)\bigl(B(\kappa z)-B(z)\bigr).
\tag{31}
$$
所有部分缩放和原相加边界仍可见。

还有一个完整、收敛的原中央表达，不将其固定负矩预设为非零。
因 $G_0$ 型三、质量零、首阶三，且 $\kappa$ 将其输入送入 $p$，
$\widetilde T_0$ 的最终输出是 unit 当且仅当原 $B$ 输入是 unit。
记
$$
M_m(G_0)=\int x^m\,d\nu_{G_0}(x),\qquad
I_{-m}(B)=\int_{\mathbf Z_p^\times}y^{-m}\,d\nu_B(y).
$$
对 principal 分支逐项展开原 $\log(1+\kappa x/y)$，得到
$$
\boxed{
J'_{\widetilde T_0,0}(0)
=-\frac d{84}\sum_{j\ge0}
 \frac{\kappa^{6j+3}}{6j+3}
 M_{6j+3}(G_0)I_{-(6j+3)}(B).
}
\tag{32}
$$
只有这些型匹配的权出现，且其 log 符号均为正后再乘原 $-1/84$。
每项赋值至少 $6j+3-v_p(6j+3)$，所以原全尾收敛。
$M_3(G_0)=3\delta\Omega^3/128$ 是单位；
首项准确为
$$
-\frac{d\delta\Omega^3}{10752}\kappa^3 I_{-3}(B).
\tag{33}
$$
没有用这个三阶矩或某个未证明的 $I_{-3}(B)\ne0$
代替目标完整中央导数。

## 9. ξ=1 与深圆盘之间仍须保留的实际输出域

用同一个 $\rho$，$J_{\xi,\ell}$ 的 unit 域是
$$
\mathcal U_\xi=\{Z+\xi X/8\in\mathbf Z_p^\times\}.
$$
当 $\xi\in p\mathbf Z_p$，它准确等于 $\{Z\ {\rm unit}\}$，
所以这一圆盘上的 $J_{\xi,\ell}(u)$ 是具有固定积分域的解析族。
在原点 $\xi=1$，域则为 $\{Z+X/8\ {\rm unit}\}$。
两者不可以靠形式 $\xi$-系数的解析性直接认作同一积分域。

例如 principal 中央差有完整分解
$$
\begin{aligned}
J'_S(0)-J'_{0,0}(0)=d\{&
\int_{\mathcal U_0\cap\mathcal U_1}
   [\log_p\langle Z+X/8\rangle-\log_p\langle Z\rangle]\,d\rho\\
&+\int_{\mathcal U_1\setminus\mathcal U_0}
             \log_p\langle Z+X/8\rangle\,d\rho\\
&-\int_{\mathcal U_0\setminus\mathcal U_1}
             \log_p\langle Z\rangle\,d\rho\}.
\end{aligned}
\tag{34}
$$
其中两个真实边界分别是
$$
Z\in p,\ X\ {\rm unit},
\qquad
Z\ {\rm unit},\ X\equiv-8Z\pmod p.
\tag{35}
$$
第一项还保 unit 交集上的整个 log 差。
(14) 支付原点深层，并没有自动把第二条 unit 平移边界删掉。

本篇取得的正向返回是 (21)–(26)：
在同一固定无穷素数族中，一个明确的原 tilted 来源的全 $p$-core
确切回到原 S，且其所有深度、tame、质量和额外叶补偿已完整写出。
后续必须用这个同一族控制 (28)、(32)、(34) 的实际剩余观察；
不能只由两个整个空间标量、某一层单位质量或一个新来源的非零矩收尾。

## 引用

- [R300：原完整 trace 与 Heisenberg 中心](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)，§§2–2.1。
- [R316：原 sigma 及实际周期的完整 core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)，§3。
- [R362：原共同二维 core 与部分输出](R362-original-triple-pair-core-and-six-branch-leaf-domain.md)。
- [R367：degree 七与五十六整个联合](R367-original-degree-seven-fifty-six-joint-and-translated-leaf-balls.md)，原 $A,B,\mathcal E$、全域与加权核。
- [R368：奇 degree 七的完整绝对作用](R368-original-degree-seven-absolute-core-and-fixed-prime-unit-tubes.md)，(9) 所用真正同 degree 锚。
- [R339：独立叶深度族](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)，其额外独立限制不能从本篇删除。
