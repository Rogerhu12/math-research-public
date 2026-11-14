# R53. 同一惰性首中央系数的十七点与整模形式实现

日期：2026-11-12。**状态：两个准确实现均已证明；其无穷非零仍开。**

R51 的实际 $E_{17}$ 截面记作 $A_{17}=\sum b_mz^m$。
将它单位缩放到 $E_1:y^2=x^3-x$，记
$$
A_1=\vartheta_T^{17}P(x^{-2})=\sum\beta_mz^m,\qquad
P(v)=v+3v^2/5-v^3/5+v^4/5.
$$
于是 $b_{4n}=17^{n-1}\beta_{4n}$。
以下两种公式都保留了在惰性 $p\ge7$ 处必须除去的一个 $p$；
不是只用模 $p$ 的先导相消认定目标非零。

## 1. 固定十七个挠点上的准确除 $p$ 公式

置 $\alpha=4-i$、$T=(0,0)$，对 $S\in E_1[\bar\alpha]$ 令
$$
R_S=T+S,\qquad
(U_S,X_S,Y_S)=\bigl(E_1^*(R_S),x(R_S),y(R_S)\bigr).
$$
这些数均在固定数域 $L=\mathbb Q(i,E_1[17])$ 中。
记 $\mathcal A=\Omega_1^2/\pi$，取实际 theta germs
$$
f_S(z)=e^{-\alpha\bar S z/\mathcal A}
             \frac{\vartheta_T(\alpha z+S)}{\vartheta_T(S)}.
\tag{1}
$$
它们是同一次数十七线丛的完整基，且 $f_S(0)=1$。
因而唯一存在固定代数系数 $a_S$，使
$$
A_1=\sum_Sa_Sf_S,\qquad \sum_Sa_S=0.
\tag{2}
$$

这些系数有完整的有限代数公式。令
$$
u_\alpha(v)=1+(12-20i)v+(-10+28i)v^2
                       +(-20-12i)v^3+(1+4i)v^4.
$$
则 $\vartheta_T(\alpha z)/\vartheta_T(z)^{17}=u_\alpha(x^{-2})$，并且
$$
a_S=\frac1{17}\sum_{Q\in E_1[\alpha]}
 e_\alpha(Q,S)^{-1}
 \frac{P(x(Q)^{-2})}{u_\alpha(x(Q)^{-2})}.
\tag{3}
$$
$Q=O$ 的项取零。$e_\alpha$ 是两个同源核之间的完美 Weil 配对。
对全部目标惰性素数，$a_S,U_S,X_S,Y_S$ 均整。

使用固定 Bell 递推
$$
\mathcal DU=-X,\quad\mathcal DX=2Y,\quad
\mathcal DY=3X^2-1,\qquad C_n=(\mathcal D+U)^n1.
$$
对 $p=4r-1$，取特征零提升
$$
\kappa_p=-\tfrac12(-1)^r\binom{2r}{r}.
$$
实际挠点满足 $C_{p+1}(U_S,X_S,Y_S)\equiv-\kappa_p\pmod p$。
因此
$$
Z_{S,p}:=\frac{C_{p+1}(U_S,X_S,Y_S)+\kappa_p}{p}
            \in\mathcal O_{L,p},
$$
而准确目标为
$$
\boxed{\quad
\beta_{p+1}\equiv-17\sum_Sa_SZ_{S,p}\pmod p,\qquad
b_{p+1}\equiv-17^r\sum_Sa_SZ_{S,p}\pmod p.
\quad}
\tag{4}
$$

### 证明

theta 自动因子表明 (1) 属于同一线丛。对 $Q\in\ker\alpha$，
$f_S(Q)/f_0(Q)=e_\alpha(Q,S)$，所以评价矩阵是可逆的十七阶
Fourier 矩阵。Riemann–Roch 的维数为十七，证明基的断言及 (3)。
比值 $\vartheta_T(\alpha z)/\vartheta_T(z)^{17}$ 是 $i$ 不变椭圆函数，
只在 $T$ 有至多十六阶极点，故是 $x^{-2}$ 的四次多项式；
到 $z^{16}$ 的有理 Taylor 计算确定上列五个高斯整数，根端已复算。
这使用有限极点空间，未以有限 Taylor 吻合代替一般函数恒等式。

在好惰性位，$2,5,17$ 都可逆，两个同源核以及 $T$ 的逆像约化后
仍不交，所以 (3) 的所有分母都是单位。还可只用低次数 CM division：
$$
\bar\alpha R_S=T,\qquad
U_S=-\delta\log\Psi_{\bar\alpha}(R_S)/17.
$$
其除法函数在这些点是单位，证明 $U_S$ 的整性。

惰性处 $\delta^p=0$、$\mathcal D^p=-\kappa_p\partial_U$。
写 $B=U^p-\delta^{p-2}X$，Bell–Jacobson 恒等式给
$$
(\mathcal D+U)^p=-\kappa_p\partial_U+B,\qquad
C_{p+1}=-\kappa_p+BU\pmod p.
$$
对上述 CM division 求 $p-1$ 次导数，利用
$\zeta(T+w)-\zeta(T)$ 为奇函数，以及有理对数导数 $h$ 满足
$\delta^{p-1}h=-h^p$，得到 $B(R_S)=0$。
另一方面 (1) 的 Taylor 系数准确是
$\alpha^nC_n(U_S,X_S,Y_S)/n!$，故
$$
\beta_{p+1}=\frac{\alpha^{p+1}}{(p+1)!}\sum_Sa_SC_{p+1}(R_S).
$$
使用 $\sum a_S=0$、$\alpha^{p+1}\equiv17$ 和
$(p+1)!/p\equiv-1\pmod p$，即得 (4)。
全文及所有自动因子见
[十七维基与 divided jet](../notes/2026-11-12-inert-seventeen-theta-basis-and-divided-jet.md)。

## 2. 同一个系数是真正整的半整数权模形式值

取模十七四次特征 $\lambda(3)=-i$，令
$$
a_n=\lambda(n)e^{2\pi i19n^2/289}\ (17\nmid n),\qquad a_n=0\ (17\mid n),
$$
以及固定的权 $1/2$ theta 模形式
$$
F(\tau)=\sum_{n\in\mathbb Z}a_nq^{n^2/(2\cdot17^2)},\qquad q=e^{2\pi i\tau}.
$$
其固定 metaplectic level 只含 $2,17$。这里 $a_n$ 与 (2) 的 $a_S$
是不同的系数。置
$$
D=(2\pi i)^{-1}\partial_\tau,\quad
\partial_k=D-\frac{k}{4\pi\operatorname{Im}\tau},\quad
k=\tfrac12,\quad N=(p+1)/2,\quad \epsilon_p=(2/p).
$$
设 $\vartheta_k=D-kE_2/12$，定义整的 holomorphic forms
$$
R_0=F,\quad R_1=\vartheta_kF,\qquad
R_{n+1}=\vartheta_{k+2n}R_n-\frac{n(k+n-1)}{144}E_4R_{n-1}.
\tag{5}
$$
它们的权分别为 $k+2n$。再令
$$
\mathcal K_p=E_{p-1}R_1+E_{p+1}F/24,\qquad
\boxed{\quad V_p=(R_N-\epsilon_p\mathcal K_p)/p.\quad}
\tag{6}
$$
$V_p$ 是同一固定群上的 $p$ 整 holomorphic modular form，权为 $p+3/2$。

令 $h=\sqrt{\pi/2}\,17/(\Omega_E\alpha)$。准确的有理数归一是
$$
\boxed{\quad
\mathscr V_p:=
24(16\pi h^2)^{N-2}\frac{V_p(i)}{\partial_{1/2}^2F(i)}
=\frac{(p+1)!}{p}\,b_{p+1}\in\mathbb Q.
\quad}
\tag{7}
$$
所以 $v_p\mathscr V_p=v_pb_{p+1}$，
$\mathscr V_p\not\equiv0\pmod p$ 足以给 R50 的初级有限性。
未归一的复值 $V_p(i)$ 本身没有被直接赋予 $p$ 进赋值。

### 证明

Hermite 与 Maass–Shimura 展开逐项比较给
$$
[t^{2N}]B(t)=\frac{(16\pi)^N}{(2N)!}\partial_{1/2}^NF(i),
$$
其中 $B$ 是 R51 的实际 Gaussian 生成函数。$A$ 从 $z^4$ 开始，
故 $F(i)=DF(i)=0$、$\partial_{1/2}^2F(i)\ne0$。

对 $Y=E_2^*/12$，Ramanujan 恒等式及 (5) 归纳给
$$
\partial_k^NF=\sum_{j=0}^N\binom Nj(k+N-j)_jY^jR_{N-j}.
$$
换 $Y$ 为 $E_2/12$ 时左端为 $D^NF$。临界 $N$ 下，每个 $j\ge1$
的上升阶乘含 $k+N-1=p/2$，其他分母为 $p$ 单位。
故 $R_N\equiv D^NF\pmod p$。
平方 Fourier 支撑给 $D^NF\equiv\epsilon_pDF$；而
$E_{p-1}\equiv1$、$E_{p+1}\equiv E_2$ 给 $\mathcal K_p\equiv DF$。
两项的权相同，且 level 与 $p$ 互素，$q$-expansion principle
证明 (6) 的整性。

在 $i$，$E_2^*=0$、$E_{p-1}=0$、$F=0$，所以
$\partial_{1/2}^NF(i)=pV_p(i)$。代回真实 Hermite 归一即得 (7)，
尤其没有漏掉 $(p+1)!$ 的那个 $p$。
完整推导、Fermat 商和全部 Eisenstein 修正见
[临界热导数全文](../notes/2026-11-12-inert-critical-heat-derivative.md)。

## 3. 当前保留的信息与未完成的步骤

十七个点的坐标代数是有限 étale 代数，其基域线性导数恒零，
但实际 $\delta x=2y$ 在这些点不恒零。故曲线导数不能先降到这个
有限点集再迭代；(4) 必须保留模 $p^2$ 的邻域 jet。

同样，(6) 的除 $p$ 后 Fourier 系数含
$$
\sum_{p\nmid n}a_n(n/17)^2
 \frac{(n/17)^{p-1}-1}{p}\,q^{n^2/(2\cdot17^2)}
$$
及完整的 Serre/Eisenstein 修正。全局模形式非零、固定 level，
或模 $p$ Frobenius 置换都没有单独证明 (7) 的指定 CM 值非零。
下一步仍是构造可控制这个实际值的算术比较，并证明无穷性。
