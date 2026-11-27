# R1042 — E17、E24 与 E3969 的同一六 sigma 伴随、共同 carry 和真实五深单位差

日期：2026-11-27 UTC。**已证明：原 S34、T72 和 R1038 的完整 Φ126 可以放在同一个原六 sigma 张量中，并有共同的 norm3 / norm81 正交伴随平面。该平面的一套真实 degree93 / 2511 框架给同一个四输出 carry；它包含一个原五深、一单位网格。固定六次测试取消全部常数项后，三条正确归一 logarithm 的每一对在该网格上的差都有准确赋值 n。**

本篇保完整四输出、全部半特征、绝对普通 core、原单位 cut、质量多项式和全部补域。另一套 degree90 / 810 框架也在同一平面内。两套 whole 返回均不把局部非零替代完整中央非零；后继使用的是这里同源、同域的三条真实算术行。

## 1. 三条实际观察及一个低范数共同平面

仍用 R968 的普通规范
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
\gamma=3+\omega,\quad \bar\gamma=2-\omega,\quad
\pi=4+\omega,\quad\bar\pi=3-\omega,
$$
$$
b=17,\quad \lambda=-\bar\pi_0^{-1},\quad
\beta=-\lambda,\quad \kappa=p\lambda^2,\quad d=p-1,\qquad
\rho=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
所有六个输入属于同一个原 $E_b$、原微分和同一个普通单位 period $\Omega$。
这里只把 R968 的前四输入重排，未改变六 sigma 测度。

对 $\xi=(\xi_1,\ldots,\xi_6)^t$ 定义三条完整观察
$$
\begin{aligned}
Y_S&=(\gamma,\bar\gamma,\delta,2\delta,1,2)\xi,\\
Y_T&=(\gamma,\bar\gamma,\delta,2\delta,3\delta,4)\xi,\\
Y_A&=(7,\pi,\bar\pi,3\delta,2\delta,2\delta)\xi .
\end{aligned}
\tag{2}
$$
由 R297/R398 和 R1038(76)，准确边际为
$$
\boxed{(Y_S)_*\rho=\nu_S,\qquad
(Y_T)_*\rho=6\delta\,\nu_T,\qquad
(Y_A)_*\rho=39\delta\,\nu_{\Phi_{126,b}}.}
\tag{3}
$$
最后的常数来自 $-3276\delta/(-84)=39\delta$，不是重新选择源的标量。

这里 $\Phi_{126,b}(z)=t^{-6}\Phi_{126,1}(tz)$，$t^6=b$，
是 R1038 的**同一个 E3969 Hecke 来源**在共同模型中的返回。
若同时取 $\Omega_b=\Omega_1/t$，完整 Amice 身份为
$$
\Phi_{126,b}(\Omega_b\log(1+T))
=t^{-6}\Phi_{126,1}(\Omega_1\log(1+T)).
\tag{4}
$$
因此单位域原样保持；不要求 $t\in\mathbf Q_p$，
也不把 $t$ 在一般基变后冒作 $\mathbf Z_p$ 的自映射。
R1038 的全平方和通常全群桥已经包含这一固定 homothety。
物理曲线仍是 E3969。

新共同整行为
$$
\boxed{
H=(1,-1,-1,0,0,0),\quad
F=(2\omega,-1+5\omega,1-3\omega,3+3\omega,-\delta,4-\omega).
}
\tag{5}
$$
逐项 Hermitian 内积给
$$
H\perp F,\qquad NH=3,\quad NF=81,\qquad
H,F\perp Y_S,Y_T,Y_A.
\tag{6}
$$
例如 $NF=4+31+13+9+3+21=81$；
把 (2) 共轭后与 (5) 相乘，三个内积均准确为零。
三条观察彼此独立：$Y_T-Y_S$ 仅读最后两输入，
而 $Y_A$ 的前四系数不与 $Y_S$ 成比例。

不需要任选第四个观察。保整个正交投影
$$
\boxed{\Pi=I-\frac{\bar H^{\,t}H}{3}
             -\frac{\bar F^{\,t}F}{81}.}
\tag{7}
$$
它在当前好位是秩四的整幂等，且 $Y_i\Pi=Y_i$。
下文的 $\Pi_*$ 始终保这整个四输出，包括它上的任意 mixed 条件。

## 2. 可含原五深网格的 degree93 / 2511 框架

取
$$
C=2\omega H,\qquad NC=12,\qquad r=\frac{27}{4},\qquad
D=F-C,\quad E=F+rC,\quad h=1+r=\frac{31}{4}.
\tag{8}
$$
准确有
$$
C\perp F,\quad D\perp E,\quad ND=93,\quad N(2E)=2511=81\cdot31,
$$
$$
C=\frac{E-D}{h},\qquad F=\frac{E+rD}{h}.
\tag{9}
$$
两个实际整行是
$$
\boxed{
D=(0,-1+7\omega,1-\omega,3+3\omega,-\delta,4-\omega),
}
$$
$$
\boxed{
2E=(31\omega,-2-17\omega,2-33\omega,
                         6+6\omega,-2\delta,8-2\omega).
}
\tag{10}
$$
$D$ 模二有五个非零系数，$2E$ 有三个。
在原 $\mathcal O_K/2=\mathbf F_4$ 上，每个非零 CM 系数均保原 sigma
奇半特征，所以两行的**整个**半特征都是 standard odd。
没有把 $NE=2511/4$ 当成一个整数 theta degree；
$E$ 使用 (10) 的真正单位二覆盖。

### 2.1 同一个无限普通 ray 的相容细化

在 R410/R531/R968 原 ray 上保所有既有条件，另要求
$$
\boxed{g_\pi=\pi_0/\bar\pi_0\equiv1\pmod{81\cdot31}.}
\tag{11}
$$
这是相容的固定细化。原三处已有 $g_\pi\equiv1\bmod27$。
写 $\pi_0=A+B\omega$，因 $\bar\pi_0$ 是三处单位，
$B\delta\equiv0\bmod27$；$B$ 为有理整数，故 $27\mid B$。
所以旧 $\pi_0\bmod27$ 是一个有理单位类，可在不改变它的条件下
选择同一个有理单位类的 $\bmod81$ 提升。这里不要求旧类为1。
三十一处与旧模数互素，可取 $\pi_0\equiv1\bmod31$。
其余处，包括原 $\bmod64$、五、七、十三、十七、十九的所有条件
保持原样。CRT 给互素的固定 ray 类，同一个 ray-class 素理想定理
仍给无穷普通有理素数。这里只删除原固定坏集，以下取 $p>211$。

因为原 $g_\pi\equiv1\bmod2$，(11) 给
$$
g_\pi\equiv1\pmod{186},\qquad
g_\pi\equiv1\pmod{5022}.
\tag{12}
$$
这正是 degree93 和 degree2511 的完整 odd Heisenberg 模数 $2N$，
并非只保 projective 作用。

令 $\gamma_{31}=6+\omega$，$N\gamma_{31}=31$。
两条非零绝对锚分别为
$$
\sigma(\delta\gamma_{31}z),\qquad \sigma(9\gamma_{31}z).
\tag{13}
$$
其 degree 恰为93、2511，且其 standard odd 半特征与 (10) 相同。
原 sigma 的普通核心是 $\beta=-\lambda$；
prime-to-$p$ 的实际 CM pull 与深限制交换。
Schur 引理及 (13) 因而同时支付两条**整个空间**的绝对核心 $\beta$。

所以对 $L=D,E$、$n\ge0$，有完整六变量测度身份
$$
\boxed{
\rho|_{L\in p^n\mathcal O}
=\beta^n(P_{L,\kappa^n})_*\rho,\qquad
P_{L,t}=I+(t-1)\frac{\bar L^{\,t}L}{NL}.}
\tag{14}
$$
它保正交的其余五输出，特别保整个 (7)。
这里不需要为整个 degree12 的 $C$ 空间另猜 scalar；
下一节只用其已付 norm3 原纤维。

## 3. 完整 norm3 低矩与唯一固定六次测试

$H$ 是 R522 原 norm3 方向在 (2) 重排后的相反数。
整个 odd degree3 空间的偶部分一维，准确由
$$
B_3=-y\sigma^3=\frac{\sigma(2z)}{2\sigma(z)}
=1+\frac{3b}{10}z^6+O(z^{12})
\tag{15}
$$
张成。对其余五变量逐系数成立，不只是第一边际。
因为 $C=2\omega H$，
$$
B_3(2\omega z)=1+\frac{96b}{5}z^6+O(z^{12}).
$$
故完整低矩为
$$
\boxed{
(\operatorname{forget}C)_*(C^6\rho)
=13824\,b\Omega^6(\operatorname{forget}C)_*\rho,\qquad
(\operatorname{forget}C)_*(C^2\rho)=0.
}
\tag{16}
$$
同理 $C^4$ 的完整返回为零。$13824=2^9 3^3$；
它包括实际六阶 factorial，未把 Fourier 系数直接当矩。

取
$$
\boxed{
Q(C,F)=\frac{C^6}{2^9 3^3}
       -\frac{C^2F^4}{2\cdot3^{11}\cdot19}.}
\tag{17}
$$
$F$ 与 $C$ 正交，第二项由 (16) 逐个完整 $F$ 系数消失。
因此
$$
\boxed{\Pi_*\left(\frac{Q}{b\Omega^6}\rho\right)=\Pi_*\rho.}
\tag{18}
$$
展开为
$$
Q=h^{-6}\sum_{k=0}^6q_kD^kE^{6-k},
$$
$$
\boxed{
(q_0,\ldots,q_6)=
\frac{(124403,-754354,1813469,-2675052,1898316,0,-406782)}
     {2^9 3^{11}\cdot19}.}
\tag{19}
$$
可直接由
$(E-D)^6/(2^9 3^3)
 -(E-D)^2(E+rD)^4/(2\cdot3^{11}\cdot19)$
核全部七项。特别
$$
\boxed{q_5=0,\qquad
q_4=\frac{7\cdot31}{2^7 3^4\cdot19}.}
\tag{20}
$$
取消第五项是特征零身份，未选取 $p$ 后调系数。

## 4. 同一四输出 carry 的全部精度返回

定义
$$
\Gamma_n=\{D\in p^n\mathcal O,\ E\ {\rm unit}\}
=\{C,F\ {\rm unit},\ F-C\in p^n\mathcal O\}.
\tag{21}
$$
等价性由 (9) 逐点成立。置
$$
\boxed{
\widehat Q_{n,p}
=\frac1{h^6 b\Omega^6}
 \sum_{k=0}^6
 \frac{q_k(D/\kappa^n)^kE^{6-k}}
      {1+\lambda\kappa^{6-k}}
\quad\text{于 }\Gamma_n,}
\tag{22}
$$
在域外延为零。所有系数整；正次数分母模 $p$ 为一，
常数分母 $1+\lambda$ 由 R410 是单位。
所以 (22) 是原空间上真正连续有界的紧开测试。

先用 (14) 的 $D$ 核返回 $D/\kappa^n$，保 $E,\Pi$；
再用完整 $E$ 核读其单位域，
逐次数产生 $1-\beta\kappa^{6-k}=1+\lambda\kappa^{6-k}$。
消掉这些准确分母，再用 (18)，得到
$$
\boxed{\Pi_*({\bf1}_{\Gamma_n}\widehat Q_{n,p}\rho)
       =\beta^n\Pi_*\rho.}
\tag{23}
$$
对 (7) 上任意完整连续测试成立。
实际 $D$ 缩放在 $(C,F)$ 坐标中为
$$
\binom{C'}{F'}
=\frac1{31}
\begin{pmatrix}
27+4t&4(1-t)\\
27(1-t)&4+27t
\end{pmatrix}
\binom C F,\qquad t=\kappa^n .
\tag{24}
$$
它保 $E$ 和全部 $Y_S,Y_T,Y_A$，故没有移动第一权后仍使用旧 cut。

令 $a_S=a_T=\gamma,\ a_A=7$。原实际 Mellin 函数满足
$$
\begin{aligned}
\int_{\Gamma_n,Y_S\ {\rm unit}}\!
 \langle Y_S/a_S\rangle^{du}\widehat Q_{n,p}\,d\rho
 &=\beta^n\langle\gamma\rangle^{-du}J_S(u),\\
\int_{\Gamma_n,Y_T\ {\rm unit}}\!
 \langle Y_T/a_T\rangle^{du}\widehat Q_{n,p}\,d\rho
 &=6\delta\,\beta^n\langle\gamma\rangle^{-du}J_T(u),\\
\int_{\Gamma_n,Y_A\ {\rm unit}}\!
 \langle Y_A/a_A\rangle^{du}\widehat Q_{n,p}\,d\rho
 &=39\delta\,\beta^n\langle7\rangle^{-du}J_{126,b}(u).
\end{aligned}
\tag{25}
$$
三条是同一个原来源、同一个 carry、同一个测试；
每条自己的单位条件仍写在式中。

三个 canonical 的质量在其真实中央均为零。
因此 (25) 的固定尺度乘子不会改变其首导数，除去显示的常数因子。
若三条首导数同时为零，(25) 的三个完整中央积分同时为零。
这里没有给任意 $\Pi$-依赖的乘子赋中央零。

## 5. 一个真正包含的原五深网格

取
$$
\mathcal D_n=
\{\xi_2,\xi_3,\xi_4,\xi_5,\xi_6\in p^n\mathcal O,\
x:=\xi_1\ {\rm unit}\}.
\tag{26}
$$
由 (10) 的首坐标为零，
$$
C\equiv F\equiv2\omega x,\quad
E\equiv e_0x,\quad e_0=\frac{31\omega}{2}\pmod{p^n}.
$$
于是 $\mathcal D_n\subset\Gamma_n$，
三个 $Y_i$ 也都为单位，原自由系数分别就是 $\gamma,\gamma,7$。

令五个深输入共同缩放为 $T$。记
$$
D=T D_f,\quad E=e_0x+T E_f,\quad Y_i=a_ix+T Z_i,
$$
其中按 $(\xi_2,\xi_3,\xi_4,\xi_5,\xi_6)$ 的顺序，
$$
\begin{aligned}
D_f&=(-1+7\omega,1-\omega,3+3\omega,-\delta,4-\omega),\\
E_f&=(-1-17\omega/2,1-33\omega/2,3+3\omega,-\delta,4-\omega),\\
Z_S&=(\bar\gamma,\delta,2\delta,1,2),\\
Z_T&=(\bar\gamma,\delta,2\delta,3\delta,4),\\
Z_A&=(\pi,\bar\pi,3\delta,2\delta,2\delta).
\end{aligned}
\tag{27}
$$
这些行在本节与对应的五输入作点积。

定义完整解析函数
$$
\mathcal A_i(T)=
\frac d{h^6 b\Omega^6}
\int_{x\ {\rm unit}}\int
\log\langle x+T Z_i/a_i\rangle
\sum_{k=0}^6
\frac{q_kD_f^k(e_0x+T E_f)^{6-k}}
     {1+\lambda\kappa^{6-k}}\,d\rho .
\tag{28}
$$
$\rho$ 内五个深坐标在这里已经取回完整测度，$x$ 仍只取单位；
所有 $\lambda,\kappa$ 分母对固定 $p$ 保持不动。
五个原 sigma 核给准确返回
$$
\boxed{
\int_{\mathcal D_n}d\log\langle Y_i/a_i\rangle
                 \widehat Q_{n,p}\,d\rho
=\beta^{5n}\mathcal A_i(\kappa^n).}
\tag{29}
$$

### 5.1 全部常数、质量和首项

原 sigma 的矩仅在 $1\bmod6$ 次数可能非零。
五个独立输入首次需总次数五。
在 $T=0$ 唯一可能是 $k=5$，已被 (20) 严格取消；
$k=6$ 的角型不符。因此
$$
\boxed{\mathcal A_i(0)=0.}
\tag{30}
$$
这包含常数 log 和整个原质量，不只是模 $p$ 消失。

第一阶只用 $k=4$。完整五混合系数准确为
$$
\begin{array}{c|r}
L&[\xi_2\xi_3\xi_4\xi_5\xi_6]D_f^4L\\ \hline
Z_S&-9072+6912\delta\\
Z_T&-16848-3456\delta\\
Z_A&-5832+8424\delta\\
E_f&71280+27864\delta .
\end{array}
\tag{31}
$$
可不依赖计算程序逐项核：$\prod d_j=27(13+11\delta)/2$，
混合系数为 $24\prod d_j\sum L_j/d_j$；
四个比值和分别是
$$
\frac{255+439\delta}{399},\quad
\frac{-771+325\delta}{399},\quad
\frac{156+134\delta}{133},\quad
\frac{407-93\delta}{38}.
$$

保
$$
I_1=(1+\lambda\kappa)\Omega,\qquad
I_{1,\log}=\int_{x\ {\rm unit}}x\log\langle x\rangle\,d\nu_\sigma
\in p\Omega\mathcal O .
$$
于是全第一项是
$$
\boxed{
[T]\mathcal A_i=
\frac d{b(1+\lambda\kappa^2)}
 \left(\alpha_i\frac{I_1}{\Omega}
                +m_1\frac{I_{1,\log}}{\Omega}\right),}
\tag{32}
$$
其中
$$
\boxed{
(\alpha_S,\alpha_T,\alpha_A)=
\frac{16\omega^2}{9\cdot7\cdot19\cdot31^3}
 (57-101\delta,\ 219+\delta,\ 27-39\delta),}
$$
$$
\boxed{m_1=-\frac{64\omega(110+43\delta)}
                       {3\cdot19\cdot31^4}.}
\tag{33}
$$
$m_1$ 是测试多项式本身的线性项，未删掉。
对 (32)，直接代入
$\alpha_i=-q_4e_0^2 B_i/(84h^6a_i)$、
$m_1=-2q_4e_0 B_E/(84h^6)$ 即得。

全部质量也有固定完整式。置
$$
B_k=[\xi_2\xi_3\xi_4\xi_5\xi_6]D_f^kE_f^{5-k},\quad
m_{5-k}=-\frac{(6-k)e_0q_kB_k}{84h^6}\quad(0\le k\le4).
$$
则删掉 (28) 中 $d\log$ 后，质量多项式准确为
$$
\boxed{
\mathcal M(T)=\frac{1+\lambda\kappa}{b}
   \sum_{r=1}^5\frac{m_rT^r}{1+\lambda\kappa^{r+1}}.}
\tag{34}
$$
这指定全部五个系数，没有其它项。
若需直接展开，$B_k=k!(5-k)![v^k]R(v)$，完整固定多项式为
$$
R(v)=(1+v)^3\left[
\frac{-25101-4113\delta}{8}
+\frac{4887+1431\delta}{2}v
+\frac{351+297\delta}{2}v^2\right].
\tag{35}
$$

### 5.2 每一对真实差都只读正第一单位矩

(28) 先按 $Y_i/a_i$ 归一自由系数，
所以相减后整个 $\log\langle x\rangle$ 质量项严格相消，
不是只因它多含一个 $p$ 而略去。特别
$$
[T](\mathcal A_i-\mathcal A_j)=
\frac db(\alpha_i-\alpha_j)
\frac{1+\lambda\kappa}{1+\lambda\kappa^2}.
\tag{36}
$$
设 $c_*={16\omega^2}/({9\cdot7\cdot19\cdot31^3})$，则
$$
\alpha_T-\alpha_S=6c_*(27+17\delta),\quad
\alpha_A-\alpha_S=2c_*(-15+31\delta),\quad
\alpha_A-\alpha_T=-8c_*(24+5\delta).
\tag{37}
$$
三个括号的范数分别为
$$
1596=4\cdot3\cdot7\cdot19,\quad
3108=4\cdot3\cdot7\cdot37,\quad
651=3\cdot7\cdot31.
$$
故 (36) 在当前全部 $p>211$ 是单位，没有新增大坏素数。

完整 log 展开只带次数分母；
(19)、(27) 的固定分母在当前好位都整，故
$$
v_p([T^j](\mathcal A_i-\mathcal A_j))
\ge-\lfloor\log_p j\rfloor\quad(j\ge1).
$$
对 $j>1,n\ge1$，$jn-\lfloor\log_pj\rfloor>n$。
结合 (29)、(30)、(36)，准确得到
$$
\boxed{
v_p\left(
\int_{\mathcal D_n}d\left[
\log\langle Y_i/a_i\rangle-\log\langle Y_j/a_j\rangle\right]
\widehat Q_{n,p}\,d\rho\right)=n
\quad(i\ne j).}
\tag{38}
$$
这是包含新增 E3969 的同一个原网格、同一个完整测试上的非零；
没有使用负矩或未识别的 $p$-依赖系数。

## 6. 同一平面的另一套完整 degree90 / 810 carry

还可在同一个 (7) 内取
$$
C_0=\delta H,\quad D_0=F-C_0,\quad E_0=F+9C_0,
\quad NC_0=9,\ ND_0=90,\ NE_0=810.
\tag{39}
$$
完整整行是
$$
D_0=(-1,7\omega,2-\omega,3+3\omega,-\delta,4-\omega),
$$
$$
E_0=(9+20\omega,-10-13\omega,-8-21\omega,
                                     3+3\omega,-\delta,4-\omega).
$$
二者模二各有六个非零系数，故 standard even。
由旧 $g_\pi\bmod4=3$、五处为一及 (11)，
$$
g_\pi\equiv91\pmod{180},\qquad
g_\pi\equiv811\pmod{1620}.
$$
R968 whole $\mathcal S_{10}$ 的绝对锚经 $[3]$、$[9]$ 拉回，
分别进入完整 $\mathcal S_{90}$、$\mathcal S_{810}$。
所以它们共同的实际核心准确为
$\upsilon_p=\chi_{10}\lambda$，$\chi_{10}^2=1$，不择符号。

原 norm3 偶纤维现在是 $B_3(\delta z)$，
完整六次矩为 $-5832b\Omega^6$。
因此取 $Q_0=-C_0^6/5832$，
按 $C_0=(E_0-D_0)/10$ 展开并逐次数除
$1-\upsilon_p\kappa^{6-k}$，得到完整测试
$\widehat Q^{(0)}_{n,p}$，满足
$$
\boxed{
\Pi_*({\bf1}_{\Gamma^{(0)}_n}\widehat Q^{(0)}_{n,p}\rho)
=\upsilon_p^n\Pi_*\rho,\quad
\Gamma^{(0)}_n=\{D_0\in p^n,E_0\ {\rm unit}\}.}
\tag{40}
$$
其七个系数准确为
$-(-1)^k\binom6k/(5832\cdot10^6)$。
全部常数分母仍由 R410 付清。

两套框架因而给一个真正的 whole 零核
$$
\boxed{
\Pi_*\left[
\upsilon_p^{-n}{\bf1}_{\Gamma^{(0)}_n}\widehat Q^{(0)}_{n,p}\rho
-\beta^{-n}{\bf1}_{\Gamma_n}\widehat Q_{n,p}\rho
\right]=0.}
\tag{41}
$$
它保全部三条观察和第四输出。值得区分：
$\mathcal D_n\cap\Gamma^{(0)}_n=\varnothing$，
因为 $D_0\equiv-x$ 在 (26) 为单位。
所以不能把两套 carry 的真实域提前认同。

## 7. 新三条条件给出的准确全补域方程

置
$$
L_i={\bf1}_{Y_i\ {\rm unit}}\,d\log\langle Y_i/a_i\rangle.
$$
若三条真实 canonical 中央首导数全为零，(25) 给
$$
\int_{\Gamma_n}L_i\widehat Q_{n,p}\,d\rho=0
\quad(i=S,T,A).
\tag{42}
$$
于是任意两条的实际分解是
$$
\boxed{
0=\int_{\mathcal D_n}(L_i-L_j)\widehat Q_{n,p}\,d\rho
+\int_{\Gamma_n\setminus\mathcal D_n}
              (L_i-L_j)\widehat Q_{n,p}\,d\rho.}
\tag{43}
$$
第一项由 (38) 的准确赋值 $n$ 已证非零；
第二项保它自己的两个不同单位条件及全部四输出。
(41) 可以在这些真实 mixed 条件上使用，
但没有删去 (43) 的补域，也没有把任意 $\Pi$-乘子传播成中央零。

本篇新增并付清的是 **三条原算术来源第一次同时处于这个实际
norm3/norm81 平面、两套 whole 核、同一个正矩测试及 (38) 的全深度非零**。
后继继续消费 (41)–(43) 及三条观察之间的真实来源作用，
不把阶段性的局部非零当作无穷素数完成标准。

## 依赖与执行边界

- R297、R398：原 S34/T72、完整六 sigma 及同源缩放。
- R1038 §§10–14：E3969 的同一实际126来源、全平方/通常全群桥和规范；
  本篇不重做其 $p=5$ 已完锚。
- R522、R531：原 norm3 整个偶纤维、普通 full-core 返回和完整质量处理。
- R410：同一原无限 ray、$1\pm\lambda$ 的单位性。
- R968：标准 even $\mathcal S_{10}$ 的真实 $\chi_{10}$ 和 whole 带中心规范。

全文使用显示的固定线性代数、theta 纤维、矩和原有界测度恒等式；
没有新增数学运行、素数扫描或缓存矩阵输入。
