# 固定 theta 截面的十七次同源下降

日期：2026-11-12。状态：以下一般下降、准确次数 $68$、带半特征的次数 $17$ 下降及各自整条 Mellin 比较均已证明。无穷多个素数处的中心简单零点仍未证明。

## 1. 输入和结论

沿用 [R46](../results/R46-fixed-sigma-section-and-central-mellin-factors.md)
与[已证明的实结构](2026-11-12-theta-real-structure-and-mellin-square.md)。
固定

$$
 E:y^2=x^3-17x,\qquad \Gamma=\Omega_E\mathbb Z[i],
 \qquad A=\Omega_E^2/\pi_{\mathbb C},
 \qquad f=34(1+i).
$$

[dyadic 向量的准确计算](2026-11-12-dyadic-vector-and-reference-theta.md)
已证明 R46 的同一平凡等型线可用 $\mathbf1_{\mathbb Z_2}$，因而可取
$L=34$。第 2–5 节先给对任意 $34\mid L$ 都成立的下降。
记

$$
 d=L^2,\qquad n=d/17.
$$

特别地，$4\mid n$。实结构给固定 $N\varpi=17$ 的 Gaussian prime，
$q=\varpi/\bar\varpi$，以及非零整函数

$$
 S(z)=P(x(z)^2)\sigma_E(z)^d=\sum_m s_mz^m,
 \qquad \bar S(z)=S(q^{-1}z),\qquad S(0)=0.
 \tag{1}
$$

上横线仅共轭代数系数。下面证明

$$
 \boxed{
 A_0(z):=S(z/\varpi)
   =R_0(x(z)^2)\sigma_E(z)^n,\qquad
 R_0\in(\overline{\mathbb Q}\cap\mathbb R)[X],
 \quad \deg R_0\le n/4-1 .
 }
 \tag{2}
$$

这比“$A_0$ 的 Taylor 系数为实代数数”更强：
$A_0$ 是原来同一椭圆曲线上次数从 $d$ 减到 $d/17$ 的代数 theta 截面。

使用已证明的 $L=34$，(2) 具体成为

$$
 A_0(z)=R_0(x(z)^2)\sigma_E(z)^{68},
 \qquad \deg R_0\le16.
 \tag{3}
$$

第 7 节还保留奇数 $L=17$ 的半特征，进一步得到仅含四个固定
实代数参数的次数 $17$ 截面。

## 2. 两份准周期律

方格情形的 Eisenstein 常数为零，因此

$$
 \sigma_E(z+\lambda)=\epsilon(\lambda)
       \exp\!\left(\frac{\bar\lambda}{A}
                        (z+\lambda/2)\right)\sigma_E(z),
 \qquad \lambda\in\Gamma,
 \tag{4}
$$

其中 $\epsilon(\lambda)\in\{\pm1\}$ 是标准 sigma 半特征。
因为 $d$ 为偶数，(1) 的 $S$ 满足

$$
 S(z+\lambda)=J_\lambda(z)S(z),\qquad
 J_\lambda(z)=
 \exp\!\left(\frac dA\bar\lambda(z+\lambda/2)\right),
 \quad\lambda\in\Gamma.
 \tag{5}
$$

$\bar S=\bar P(x^2)\sigma_E^d$ 满足同一条 (5)，因为 $\sigma_E,x$ 的
Taylor 系数为有理数。把 $\bar S(z)=S(q^{-1}z)$ 代入这条准周期律，
再令 $\mu=q^{-1}\lambda$，得到

$$
 S(w+\mu)=J_\mu(w)S(w),\qquad \mu\in q^{-1}\Gamma.
 \tag{6}
$$

这里使用 $q\bar q=1$：
$\bar\mu=q\bar\lambda$，所以变换后的指数正好仍为 (5) 的形式。

## 3. 交叉相位及扩大的周期格

Gaussian ideals $(\varpi)$ 与 $(\bar\varpi)$ 互素，故

$$
 \Gamma'=\Gamma+q^{-1}\Gamma
       =\varpi^{-1}(\varpi\Gamma+\bar\varpi\Gamma)
       =\varpi^{-1}\Gamma.
 \tag{7}
$$

不能仅凭 (7) 就把两份准周期律相加；须检查乘子相容性。
直接计算，对任意 $\lambda,\mu\in\Gamma'$，

$$
 \frac{J_\mu(z+\lambda)J_\lambda(z)}{J_{\lambda+\mu}(z)}
   =\exp\!\left(
       \frac d{2A}(\bar\mu\lambda-\bar\lambda\mu)
      \right).
 \tag{8}
$$

$\Gamma'$ 的基本面积是 $\Omega_E^2/17=\pi_{\mathbb C}A/17$。
所以存在整数 $h$ 使

$$
 \frac{\bar\mu\lambda-\bar\lambda\mu}{2A}
       =\frac{\pi_{\mathbb C}i}{17}h.
$$

(8) 因而是 $(-1)^{nh}=1$，这里恰好使用 $n=d/17$ 为偶数。
两条已有准周期律可以任意相加或取负，得到

$$
 S(z+\lambda')=J_{\lambda'}(z)S(z)
               \quad(\lambda'\in\Gamma').
 \tag{9}
$$

这一步也排除了潜在的非平凡二次半特征；无需另乘指数二次项。

## 4. 回到原曲线并得到实代数多项式

对 $\lambda\in\Gamma$，在 (9) 中取 $\lambda'=\lambda/\varpi$。
由 $N\varpi=17$，

$$
 \begin{aligned}
 A_0(z+\lambda)
 &=\exp\!\left(
      \frac dA\frac{\bar\lambda}{\bar\varpi}
        \left(\frac z\varpi+\frac{\lambda}{2\varpi}\right)
       \right)A_0(z)\\
 &=\exp\!\left(\frac nA\bar\lambda(z+\lambda/2)\right)A_0(z).
 \end{aligned}
 \tag{10}
$$

$n$ 为偶数，因此 $\sigma_E^n$ 也满足 (10)。
于是 $R=A_0/\sigma_E^n$ 是 $\Gamma$-椭圆函数，
仅可能在 $O$ 有至多 $n$ 阶的极点。

$S(iz)=S(z)$，所以 $A_0(iz)=A_0(z)$；又因 $4\mid n$，
$\sigma_E(iz)^n=\sigma_E(z)^n$。故 $R$ 在 $[i]$ 下不变。
固定子域为 $\mathbb C(x^2)$，而除 $O$ 外无极点，
所以 $R=R_0(x^2)$ 是多项式。
$x^2$ 在 $O$ 的极点阶为四，先给 $\deg R_0\le n/4$。

由 $S(0)=0$ 和非零性，$A_0$ 在 $O$ 有正零阶。
该零阶是四的倍数，因此最高的次数 $n/4$ 项不存在，
即 $\deg R_0\le n/4-1$。

$A_0(z)$ 的 Taylor 系数为 $s_m/\varpi^m$，都是代数数。
$\sigma_E$ 及 $x$ 的展开有理；依次消去 Laurent 展开的最高负幂，
可逐项解出 $R_0$ 的全部系数为代数数。
此外，由 (1)，

$$
 \overline{s_m/\varpi^m}
   =q^{-m}\bar\varpi^{-m}s_m
   =s_m/\varpi^m .
 \tag{11}
$$

因此 $A_0$ 的系数实，$\sigma_E,x$ 的系数也实，
唯一性迫使 $R_0$ 的全部系数实。这完成 (2)。

## 5. 同一个 Mellin 因子的准确改写

记 $A_0(z)=\sum_m a_mz^m$。由于 $s_m=\varpi^m a_m$，
(11) 给

$$
 s_m\bar s_m=17^m a_m^2.
$$

因此 R46 的复平方范数公式准确降为

$$
 \boxed{
 e_m=\kappa(Nf\,n)^{-m}a_m^2\qquad(4\mid m).
 }
 \tag{12}
$$

$\kappa$ 没有变化。对每个目标普通 $p\ne17$，
$\varpi\in\mathbb Z_p^\times$。
令 $\mu_p$ 为固定截面 $A_0$ 的有界测度，

$$
 \int x^m\,d\mu_p=\Omega_p^m m!a_m,
$$

并令 $J_p(T)$ 为其单位区间的 principal Mellin 变换。
全部矩给出实际测度关系

$$
 \nu_p=[\varpi]_*\mu_p,\qquad
 G_p(T)=(1+T)^{\,\log_p\langle\varpi\rangle/\log_p(1+p)}J_p(T).
 \tag{13}
$$

这是乘 $p$ 单位的推前，因此对所有这些 $p$ 有效，
不用为了零阶结论先删去测度的有限分母。

代入已证明的整条平方恒等式，使用 $d=17n$ 及
$q=\varpi/\bar\varpi$，得到

$$
 \boxed{
 F_p^{\Theta,-}(T)
   =\kappa f\Omega_p
      (1+T)^{\,\log_p\langle f^2/n\rangle/\log_p(1+p)}
         J_p(T)^2 .
 }
 \tag{14}
$$

所以

$$
 J_p(0)=0,\qquad
 \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
       \iff J_p'(0)\ne0.
 \tag{15}
$$

取 $n=68$，则 $f^2/n=34i$。
由于 $i$ 为目标普通 $p$ 的 Teichmüller 单位，
(14) 的指数便是 $\log_p\langle34\rangle/\log_p(1+p)$。

本下降降低的是同一个实际 theta 截面的线丛次数与有限多项式的大小，
并没有把 $J_p'(0)$ 变成某个已知非零的有限代数对数。
固定截面的次数小与无穷多个变化 $p$ 的中心简单零点之间，
仍需新的证明。

## 6. 实际 $L=34$ 及奇数 $17$ 的有限模型

$17$ 处已有显式公式
$\rho v(t/17)\propto\lambda(ct)\psi(ct^2/(2\cdot17^2))$，
支撑为 $v_{17}(x)=-1$。
直接平移可见它在 $17\mathbb Z_{17}$ 下不变，
所以该处确实只需 $v_{17}(L)=1$。

dyadic 笔记逐项计算同一 Hecke splitting 在
$i$ 与 $(-3+4i)/5$ 上的 Rao 相位，证明
$\phi_2=\mathbf1_{\mathbb Z_2}$ 被整个 norm-one torus 固定。
该处支撑与平移模数都是 $\mathbb Z_2$；故有限向量同时允许
$L=34$ 与 $L=17$。

用 R46 的记号，$L=34$ 时 $a_n$ 只有偶数 $n$ 可能非零，
而 $a_{2k}=\phi_f^{\rm av}(k/17)$。
因此两种 lattice 枚举给完全同一个 Hermite 生成函数 $B(t)$，
并且其尺度满足 $c_{34}=2c_{17}$。
若 $S_{34}$ 为本文原来已证明代数性的截面，定义

$$
 S_{17}(z)=S_{34}(z/2).
 \tag{16}
$$

这保留固定共同标量 $C$：
$B(c_{17}z)=C S_{17}(z)$。
所以 $S_{17}$ 的 Taylor 系数已经代数，不必重新证明一份
奇数次数 theta 基的代数性。它仍满足
$\bar S_{17}(z)=S_{17}(q^{-1}z)$ 及 $S_{17}(iz)=S_{17}(z)$。

## 7. 保留半特征后的次数十七下降

### 7.1 归一化的半周期 theta

置

$$
 T_0=\frac{1+i}{2}\Omega_E,\qquad
 \vartheta(z)=
    e^{-\zeta_E(T_0)z}\frac{\sigma_E(z+T_0)}{\sigma_E(T_0)}.
 \tag{17}
$$

$T_0$ 对应 $E$ 的 $2$-挠点 $(0,0)$。
由 sigma 加法公式，以及
$2\zeta_E(T_0)=\eta_{\Omega_E+i\Omega_E}$，
准确得到

$$
 \boxed{\vartheta(z)^2=x(z)\sigma_E(z)^2,\qquad
        \vartheta(0)=1.}
 \tag{18}
$$

例如，加法公式先给
$\sigma(z+T_0)\sigma(z-T_0)=-x(z)\sigma(z)^2\sigma(T_0)^2$；
准周期律又给
$\sigma(z-T_0)=-e^{-2\zeta(T_0)z}\sigma(z+T_0)$，
两个负号恰消去。

右边的 Taylor 系数有理、常数项为一，故其取常数项一的形式平方根
有理。因而 $\vartheta$ 的全部系数为有理数。
右边在 $z\mapsto iz$ 下不变，常数项排除负号，于是

$$
 \vartheta(iz)=\vartheta(z).
 \tag{19}
$$

其零点恰为 $T_0+\Gamma$，都是一阶。
写 $\lambda=\Omega_E(r+si)$，直接代入 (4) 得

$$
 \vartheta(z+\lambda)
   =\chi_T(\lambda)
      \exp\!\left(\frac{\bar\lambda}{A}(z+\lambda/2)\right)
       \vartheta(z),\qquad
 \chi_T(\lambda)=(-1)^{rs}.
 \tag{20}
$$

特别地两生成元 $\Omega_E,i\Omega_E$ 的半特征均为 $+1$；
对一般周期不能把 $\chi_T$ 省掉。

### 7.2 奇数次数截面及交叉符号

$L=17$ 的 $B$ 准周期式在两生成元上的符号均为正，
所以 $S_{17}$ 与 $\vartheta^{17^2}$ 有相同的完整乘子：

$$
 S_{17}(z+\lambda)
   =\chi_T(\lambda)
       \exp\!\left(\frac{17^2}{A}
                         \bar\lambda(z+\lambda/2)\right)
          S_{17}(z),\qquad\lambda\in\Gamma.
 \tag{21}
$$

这里 $17^2$ 为奇数，(21) 正是两生成元的准周期律按 cocycle
延伸的结果。$\bar S_{17}$ 满足同一式。
实结构于是给 $q^{-1}\lambda$ 处的对应乘子，其半特征为
$\chi_T(\lambda)$。

与第 3 节不同，现在不能声称所有交叉相位都为一。
在 $\Gamma'=\varpi^{-1}\Gamma$ 上定义候选完整乘子

$$
 \widetilde J_{\lambda'}(z)
   =\chi_T(\varpi\lambda')
      \exp\!\left(\frac{17^2}{A}
                  \bar\lambda'(z+\lambda'/2)\right).
 \tag{22}
$$

这是真正的 theta cocycle：把 $\lambda'=\lambda/\varpi$、
$z=w/\varpi$ 代入，指数变为
$17\bar\lambda(w+\lambda/2)/A$，
而 $\chi_T^{17}=\chi_T$，恰为 $\vartheta(w)^{17}$ 的乘子。

对本题的 $\varpi=4-i$，
$\varpi\equiv\bar\varpi\equiv i\pmod{2\mathbb Z[i]}$，
只交换 $r,s$ 的奇偶性。因此

$$
 \chi_T(\varpi\lambda)
   =\chi_T(\bar\varpi\lambda)=\chi_T(\lambda).
 \tag{23}
$$

(22) 在 $\Gamma$ 上与 (21) 一致；
在 $q^{-1}\Gamma$ 上则因
$\varpi q^{-1}\lambda=\bar\varpi\lambda$ 也与实结构给出的乘子一致。
这两子格生成 $\Gamma'$，且 (22) 满足 cocycle，
所以它在整个 $\Gamma'$ 上都是 $S_{17}$ 的准确乘子。
这核对了全部交叉相位，没有默选一个额外半特征或二次指数项。

### 7.3 四个代数参数

定义

$$
 A_{17}(z)=S_{17}(z/\varpi)
          =S_{34}(z/(2\varpi))=A_0(z/2).
 \tag{24}
$$

由 (22)，$A_{17}$ 与 $\vartheta^{17}$ 有相同乘子。
$A_{17}$ 的 Taylor 系数为实代数数，仍在 $[i]$ 下不变。
故 $A_{17}/\vartheta^{17}$ 是 $[i]$-不变椭圆函数，
仅可能在 $T_0$ 有至多十七阶极点。

$x$ 在 $T_0$ 有二阶零点，所以 $1/x^2$ 在该处有四阶极点；
它在商曲线 $E/\mu_4\simeq\mathbb P^1$ 上是以 $T_0$ 为唯一极点的坐标。
因此

$$
 \boxed{
 A_{17}(z)=\vartheta(z)^{17}Q(x(z)^{-2}),\qquad
 Q\in(\overline{\mathbb Q}\cap\mathbb R)[X],\quad\deg Q\le4 .
 }
 \tag{25}
$$

由 $\vartheta(0)=1$、$x(z)^{-2}\to0$ 及 $A_{17}(0)=0$，
还有 $Q(0)=0$。
系数的实代数性可由 $z=0$ 处逐项比较直接得到。
利用 (18)，亦可把整个函数写成

$$
 \boxed{
 A_{17}(z)
   =\vartheta(z)\sigma_E(z)^{16}
         \bigl(c_1x(z)^6+c_2x(z)^4+c_3x(z)^2+c_4\bigr),
 \quad c_j\in\overline{\mathbb Q}\cap\mathbb R .
 }
 \tag{26}
$$

这四个参数固定一次，对所有素数与所有权重使用。
非零性保证它们不全为零。

### 7.4 同一分支在次数十七对象上的形式

写 $A_{17}(z)=\sum_m b_mz^m$。
因为 (24) 给 $a_m=2^m b_m$，(12) 准确变为

$$
 e_m=\kappa(17\,Nf)^{-m}b_m^2\qquad(4\mid m).
 \tag{27}
$$

对目标普通 $p$，乘 $2$ 是单位，故其有界测度及 Mellin 因子仍由
实际推前对应。记新 Mellin 因子为 $J_{17,p}$，则

$$
 \boxed{
 F_p^{\Theta,-}(T)
   =\kappa f\Omega_p
      (1+T)^{\,\log_p\langle136\rangle/\log_p(1+p)}
         J_{17,p}(T)^2 .
 }
 \tag{28}
$$

这里 $f^2/17=136i$，$i$ 在 principal-unit 投影中消失。
因此

$$
 J_{17,p}(0)=0,\qquad
 \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
         \iff J_{17,p}'(0)\ne0.
 \tag{29}
$$

原 Mellin 因子与 $J_{17,p}$ 只差已明确的单位伸缩因子，
并没有更换本题需要控制的零阶。
次数 $17$ 的形式把输入压缩到四个代数参数；
它尚未给出无穷多个 $p$ 上 (29) 右边成立的证明。

### 依赖

- [R46](../results/R46-fixed-sigma-section-and-central-mellin-factors.md)：
  固定截面、代数性、完整 Mellin 比较及普通处有界性。
- [实结构与 Mellin 平方](2026-11-12-theta-real-structure-and-mellin-square.md)：
  $\bar S(z)=S(q^{-1}z)$ 及准确零阶判据。
- [dyadic 向量与参考 theta](2026-11-12-dyadic-vector-and-reference-theta.md)：
  同一平凡线的准确向量 $\mathbf1_{\mathbb Z_2}$，从而允许 $L=34$ 和 $L=17$。
- sigma 准周期律采用同一方格规范，见 Bannai–Kobayashi 2010，
  *Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*，
  Example 1.9；
  [作者预印本](https://arxiv.org/abs/math/0610163)。
  第 2–5 节的交叉相位、下降及新指数均在本文直接证明。
