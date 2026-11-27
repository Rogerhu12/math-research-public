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


## 8. 五主型投影后的真实 F81 cut：72 支、全五矩及单输入扇区

本节使用 R1040 §10 的实际五伴随乘积和物理平均。
所有测试仍在原六输入上，特别不把原 $\Gamma_n$ 预认成平均后的同一个域。
记新伴随为 $H,K,J,A,N$，其范数为 $3,6,2,9,14$。
原 C/F 的准确位置为
$$
C=2\omega H,\qquad
F=2K-\frac{5+\omega}{2}J+
 2(1+\omega)A+\frac{1-\omega}{2}N.
\tag{44}
$$

### 8.1 全部实际旋转与原单位域

令 $h_n={\bf1}_{\Gamma_n}\widehat Q_{n,p}$。
它满足 $h_n(\zeta C,\zeta F)=h_n(C,F)$，$\zeta\in\mu_6$：
深度/单位条件不变，而原多项式的总次数为六。
因此五个角平均的真正 transpose 准确缩为
$$
\boxed{
\overline h_n=\frac1{6^4}
 \sum_{\zeta_K,\zeta_J,\zeta_A,\zeta_N\in\mu_6}
 h_n(C,F_{\boldsymbol\zeta}),}
\tag{45}
$$
$$
F_{\boldsymbol\zeta}=
2\zeta_KK-\frac{5+\omega}{2}\zeta_JJ+
2(1+\omega)\zeta_AA+\frac{1-\omega}{2}\zeta_NN.
$$
每项仍使用自己的整个
$$
D_{\boldsymbol\zeta}=F_{\boldsymbol\zeta}-C,\quad
E_{\boldsymbol\zeta}=F_{\boldsymbol\zeta}+rC,\quad
\Gamma_{n,\boldsymbol\zeta}
=\{D_{\boldsymbol\zeta}\in p^n,\ E_{\boldsymbol\zeta}\ {\rm unit}\}.
\tag{46}
$$
(22) 的全部七项、$\kappa^{-nk}$ 和准确 Euler 分母不变。

### 8.2 原五深网格上准确只有72支

在原 $\mathcal D_n$ 上，
$$
(H,K,J,A,N)\equiv(x,-x,0,x,0)\pmod{p^n}.
$$
所以某项 (46) 相交，当且仅当
$$
-\zeta_K+(1+\omega)\zeta_A=\omega.
$$
这是三个六次根的和为零；其完整解恰为
$$
\boxed{(\zeta_K,\zeta_A)=(1,1),\quad(\omega^2,\omega).}
\tag{47}
$$
$\zeta_J,\zeta_N$ 各自的六种值全部保留。
非零差的复绝对值至多3，范数至多9，故 $p>211$ 时不会有新增约化解。
于是1296项中准确72项包含整个 $\mathcal D_n$，其余均不相交。
这不是将72项改成一个相同 cut：只在当前完整网格上使用 (47)。

对任何总次数五的原混合系数，$\zeta_J,\zeta_N$ 的平均可逐项完成：
次数小于六的非恒定字符之和为零。
两支留下的 D 行（包含首坐标）准确为
$$
\begin{aligned}
d^{(0)}&=(0,6\omega,0,2\delta,2(1-\omega),2(1-\omega)),\\
d^{(1)}&=(0,0,6\omega,2\omega^2\delta,2\delta,2\delta).
\end{aligned}
\tag{48}
$$
这一步只用于完整多项式系数；在后面的剩余深度 cut 内，
不能提前删除 J/N 的实际相位。

设 $e^{(a)}=d^{(a)}+hC$。
按原五个深输入的顺序，完整生成多项式准确为
$$
\boxed{
\overline R(v)
=\frac1{36}\sum_{a=0}^1
 \prod_{j=2}^6(e_j^{(a)}+v d_j^{(a)})
=\frac{31(\omega-1)}6(1+v)^3(12v-19).}
\tag{49}
$$
例如第一支的乘积为
$48h\delta(1+v)^3\{6(1+v)-2h\}$，
第二支为其 $\omega$ 倍；这直接给 (49) 的全部系数。

因此 (34) 的平均网格质量仍是一整个准确五次多项式：
只须用
$$
\overline B_k=k!(5-k)![v^k]\overline R(v)
$$
替换该式的 $B_k$，保全部 $q_k$ 和 Euler 分母。
并无未写出的更高质量项。

### 8.3 原 Y_A 平均中央行的实际网格首项

同样逐项读得
$$
\begin{aligned}
\overline{[\,\xi_2\xi_3\xi_4\xi_5\xi_6\,]D_f^4Z_A}
 &=-96(3+\delta),\\
\overline{[\,\xi_2\xi_3\xi_4\xi_5\xi_6\,]D_f^4E_f}
 &=1488(\omega-1).
\end{aligned}
\tag{50}
$$
更一般，对一个固定的 L，
该平均五混合系数是
$-96\delta(L_2+\omega^2L_3)$。
于是原 (28)–(32) 的同一完整展开给
$$
[T]\overline{\mathcal A}_A
=\frac d{b(1+\lambda\kappa^2)}
\left(\overline\alpha_A\frac{I_1}{\Omega}
      +\overline m_1\frac{I_{1,\log}}{\Omega}\right),
\tag{51}
$$
$$
\overline\alpha_A=
-\frac{q_4e_0^2}{84h^6\cdot7}\{-96(3+\delta)\},\qquad
\overline m_1=
-\frac{2q_4e_0}{84h^6}\,1488(\omega-1).
$$
$\overline\alpha_A$ 在全部当前 $p>211$ 为单位；
$I_{1,\log}/\Omega\in p\mathcal O$，
故 (51) 本身为单位。
常数项仍严格为零；完整 log 尾仍满足原
$-\lfloor\log_pj\rfloor$ 的系数下界。因此
$$
\boxed{
v_p\left(
 \int_{\mathcal D_n}d\log\langle Y_A/7\rangle\,
                    \overline h_n\,d\rho\right)=n.}
\tag{52}
$$

这里原 $Y_A$ 不被五个伴随的物理旋转移动。
R1040(77) 因而确实支付整个平均行
$$
\int_{Y_A\ {\rm unit}}d\log\langle Y_A/7\rangle
          \overline h_n\,d\rho
=39\delta\,j_{126,b}\,\Lambda_p(h_n).
\tag{53}
$$
其在坏 canonical 假设下为零是合法结论。
(52) 只支付其中的明确网格，尚未删去 (53) 的真实补域。

若固定不旋转的 $Y_S,Y_T$ 也放入同一网格计算，
则两者的 (50) 都是 $-96(3+4\delta)$；
其与 A 的归一系数差为
$$
\frac{-96(3+\delta)}7-
 \frac{-96(3+4\delta)}{\gamma}
=\frac{144(7+5\delta)}7.
\tag{54}
$$
该差为当前好位单位。
但 (53) 不自动支付这些未旋转 S/T 的平均中央零。
R1040 的真实正交条件迫使同时保 S、T 的四个相位完全相同；
不能把1296个新 cut 逐支当成原三条 canonical carry。

### 8.4 完整原输入分层与不可省略的中间环

按模 p 的原六输入 unit pattern 分层。
若唯一 unit 是 $\xi_4,\xi_5,\xi_6$ 之一，则 H 深，所有平均 cut 均为空。
若唯一 unit 是 $\xi_2$，其必要条件为
$$
2\omega(\zeta_K+\zeta_A+1)=(1-\omega)\zeta_N.
$$
左边在 $2\mathcal O_K$，右边不在，故特征零无解。
$\xi_3$ 的式同样左边可被2整除、右边不可。
这些非零差的范数小于60，所以 $p>211$ 也没有约化解。
全深输入同样被 C 的单位条件排除。

因此模 p 只有 $\xi_1$ 单 unit 的扇区可能相交。
对 $n>1$，这不等于 $\mathcal D_n$。
完整余部必须保
$$
(\mathcal D_1\setminus\mathcal D_n)
 \cap\bigcup_{\boldsymbol\zeta}\Gamma_{n,\boldsymbol\zeta}
\quad\text{和至少两个原输入为 unit 的部分。}
\tag{55}
$$

第一项有一个准确的原五核递归，不能将它称为空。
对 $1\le m<n$，在 $\mathcal D_m$ 上先取回五个原深输入，
令 $T_m=\kappa^m$。
所有72支准确变成
$$
D_{\boldsymbol\zeta}=T_m d_{\boldsymbol\zeta},\quad
E_{\boldsymbol\zeta}=e_0x+T_m e_{\boldsymbol\zeta},\quad
Y_A=7x+T_mZ_A ,
$$
测度带 $\beta^{5m}$，剩余实际条件为
$$
d_{\boldsymbol\zeta}\in p^{\,n-m}\mathcal O.
\tag{56}
$$
原测试中的 D 项准确成为
$(d_{\boldsymbol\zeta}/\kappa^{n-m})^k$；
E 项、log 和所有分母仍如上保留。
这里的72个 $d_{\boldsymbol\zeta}$ 仍含 J/N 的全部相位，
不可在 (56) 内改用仅两个多项式行 (48)。
相邻 m 的准确返回相减，才是
$\mathcal D_m\setminus\mathcal D_{m+1}$ 的完整积分。

### 8.5 一个真实的两 unit 厚管

余部中有下列明确且不能从集合上排掉的支。
取 $\zeta_A=-1$，$\zeta_K=\zeta_J=\zeta_N=1$，则
$$
F^*=F-4(1+\omega)A,\qquad
D^*_1=4\omega^2,\quad D^*_4=-3\omega^2 .
$$
所以
$$
\boxed{
\mathcal U_n=
\{\xi_1=x\ {\rm unit},\
 \xi_4-4x/3\in p^n,\
 \xi_2,\xi_3,\xi_5,\xi_6\in p^n\}
\subset\Gamma_{n,*}.}
\tag{57}
$$
在这个完整管上，
$$
\begin{aligned}
C&\equiv2\omega x,\qquad E^*\equiv h\,2\omega x,\\
Y_A&\equiv(7+4\delta)x,\\
Y_S=Y_T&\equiv(15+19\delta)x/6\pmod{p^n}.
\end{aligned}
\tag{58}
$$
后二者的范数分别为97及 $109/3$，故原三个观察在当前好位均为单位。
管中恰有两个原输入为 unit，不属于 (52) 的五深网格。

该两坐标的原正交行是
$$
d=-4\xi_1+3\xi_4,\qquad e=3\xi_1+4\xi_4,
\quad Nd=Ne=25.
\tag{59}
$$
两个完整半特征均为 standard odd。
其原联合来源为
$\sigma(-4z_d+3z_e)\sigma(3z_d+4z_e)$。
(59) 给出了继续消费 (57) 的真实 norm25 输入，
而不是仅因出现 degree25 就将它等同于另一套
$\mathcal C_\pm$ 或先宣称其积分更深。
它的完整 unit cut、四个其他深输入、普通 ray 的 $5^2$ 相容细化
及全幂核仍须一同使用。


## 9. 原两 unit 管的完整 norm25 返回与实际常数项

本节继续 (57)，计算的是同一个平均 $\overline h_n$ 在原
$\mathcal U_n$ 上的真实积分。它说明该补域并不因四个原输入深而自动
比 (52) 的五深网格更深；后续必须消费其完整项。

### 9.1 同一 ray 的 norm25 whole 核

在原射线保全部条件，再将原 $\pi_0\equiv2\bmod5$ 提升为
$\pi_0\equiv2\bmod25$。其它模数与此提升相容，
固定 ray-class 素理想定理仍给无穷普通素数。
于是 $g_\pi=\pi_0/\bar\pi_0\equiv1\bmod50$。
两条 (59) 的半特征都是 standard odd；
原完整 degree25 Heisenberg 模因此有 scalar 核。
以非零实际锚 $\sigma(5z)$ 及原 sigma 的 prime-to-p pull
锁定其绝对 scalar，两个方向的深核均为 $\beta=-\lambda$。
这与第2节的 whole-space 论证相同，不将一个未识别的子空间代替全25维。

使用完整原联合来源
$$
\mathcal R(z_d,z_e)
=\sigma(-4z_d+3z_e)\sigma(3z_d+4z_e).
\tag{60}
$$
其 Gram 为 $(25,25)$、交叉为零、两半特征如上。
原 $\mathcal U_n$ 准确等于
$d\in p^n,\ e$ unit、以及 $\xi_2,\xi_3,\xi_5,\xi_6\in p^n$。
故其五个深方向可同时返回：
一个 whole degree25 核与四个原 sigma 核产生 $\beta^{5n}$。
取回后的输入准确为
$$
\boxed{
\xi(T)=\left(
 \frac{3e-4Td}{25},\,Tu_2,\,Tu_3,\,
 \frac{4e+3Td}{25},\,Tu_5,\,Tu_6\right),\qquad T=\kappa^n,
}
\tag{61}
$$
其中 e 仍只取 unit；测度是
$-\nu_{\mathcal R}(d,e)\otimes\nu_\sigma^{\otimes4}/84$。
这里没有 Haar Jacobian，也没有删除联合来源中的 d/e 耦合。

### 9.2 这个管上的全部平均支

为给统一且不依赖扫描的有限坏界，以下只将素数下界提高为
$p>1296$。这是固定有限删集。

在 (57) 的原管上，某一旋转能进入 cut 的充分必要条件为
$$
(-6+8\delta)\zeta_K+6(1+\omega)\zeta_A
       +4(1-\omega)\zeta_N=6\omega .
\tag{62}
$$
$\zeta_J$ 任意。该式的完整解是
$$
\boxed{
(\zeta_K,\zeta_A,\zeta_N)
=(1,-1,1),\quad(-\omega^2,-\omega,-\omega^2).}
\tag{63}
$$
简短手证如下。
对六个 $\zeta_K$，将第一项移到右侧所得的范数依次为
$84,444,336,192,372,156$，顺序为
$1,-1,\omega,-\omega,\omega^2,-\omega^2$。
左边另两项的和范数至多 $(6+4\sqrt3)^2<168$，
所以只余第一和最后。
又
$6(1+\omega)/(4(1-\omega))=\delta/2$。
范数84的情况迫 $\zeta_A/\zeta_N=\pm1$，
范数156的情况迫该比为 $-\omega$ 或 $\omega^2$；
逐个代入便得 (63)。
任何非零 (62) 差的绝对值小于36，故范数小于1296，
当前没有额外模 p 解。

所以1296项中恰12项包含整个 $\mathcal U_n$，其余不相交。
每支仍保整个 (46) 的 unit/depth 域；
在当前管内它们的 E 自由系数全为
$$
e_*=\frac{93\omega}{50},
\qquad
a_A'=\frac{21+12\delta}{25},\qquad
a_S'=a_T'=\frac{15+19\delta}{50}.
\tag{64}
$$
将各原行直接代入 (61)，定义实际线性式
$$
D_\zeta(\xi(T))=T L_\zeta,\quad
E_\zeta(\xi(T))=e_*e+T M_\zeta,\quad
Y_i(\xi(T))=a_i'e+T Z_i'.
$$
这些定义保全部四个其它深输入，唯一的 source 是 (60)；
不将 (63) 的两个管内源重新识别为别的 arithmetic line。

### 9.3 完整质量首项：Euler 因子准确消掉

令 $\mathcal M_{\mathcal U}(T)$ 为
$\overline h_n$ 取回 (61) 后的质量函数，包含 $1/1296$ 的实际平均，
但不含外面的 $\beta^{5n}$。
因此
$$
\int_{\mathcal U_n}\overline h_n\,d\rho
=\beta^{5n}\mathcal M_{\mathcal U}(\kappa^n).
\tag{65}
$$
在 T=0，四个原 sigma 输入各自至少需要一次。
$k=5$ 已被原 $q_5=0$ 杀掉，只余 k=4、k=6，
对应 d 的次数0、2。
原 (60) 的完整二次项是
$$
\mathcal R=-12z_d^2-7z_dz_e+12z_e^2+O((z_d,z_e)^8).
$$
故两个真实联合矩是
$m_{0,2}=24\Omega^2$、$m_{2,0}=-24\Omega^2$。
对 e 的 whole unit 核，
它们分别乘 $1+\lambda\kappa^2$、$1+\lambda$，
正好消掉 (22) 的两个原分母。
这里未将 Taylor 系数当作未乘阶乘的矩。

在 (63) 两支中，d 在 $L_\zeta$ 的系数分别是
$-\omega^2,\omega$。
$\zeta_J$ 的六值平均后，四个其它深输入系数的乘积准确为
$$
\boxed{
P_0=-\frac{375+825\omega}{4},\qquad
P_1=-\frac{252+819\omega}{4}.}
\tag{66}
$$
例如第一支的前两个系数为 $-1+3\omega,-3-\omega$；
后两项的 J-平均乘积为
$\{5(\omega-1)/2\}^2$。
第二支相应为
$-2+3\omega,2-\omega$ 和
$\{-3(2+3\omega)/2\}^2$。
这给 (66) 的全部四深混合系数，不是只读一条首坐标。

由原 $q_6/q_4=-3/14$，逐项回乘所得常数为
$$
\boxed{
M_*:=\mathcal M_{\mathcal U}(0)
=-\frac{2q_4}{63h^6b}
 \left\{
 e_*^2(P_0+P_1)
 +\frac{45}{14}(\omega P_0+\omega^2P_1)
 \right\}\ne0.}
\tag{67}
$$
系数含 $-1/84$ 的原六 sigma 规范。
确切地，括号等于
$$
-\frac{25947}{10000}(339-209\omega)
+\frac{135}{28}(43+117\omega).
$$
其 $\omega$ 系数严格为正，故在 K 中非零。
所有数都是固定有理代数数；未用数值近似或有限素数扫描。
若某个目标 p 除该固定分子的范数，只保其真实有限估值，
不将 (67) 一概称作 p 单位。

### 9.4 归一中央差的真实常数与全尾

令 $\mathcal A_{i,\mathcal U}(T)$ 为 (65) 同一返回中再乘
$d\log\langle Y_i/a_i\rangle$ 的完整函数。
在 T=0，各支相同的 $\log\langle e\rangle$ 严格相消。
于是
$$
\boxed{
(\mathcal A_{A,\mathcal U}
 -\mathcal A_{S,\mathcal U})(0)
=d\,M_*\log\langle r_*\rangle,\qquad
r_*=\frac{3(23+27\delta)}{7(15+19\delta)}.}
\tag{68}
$$
其范数为
$$
Nr_*=\frac{3\cdot97}{7\cdot109}=\frac{291}{763}\ne1.
$$
当前所有地点 $r_*$ 是 unit，且不是根一；
故 $\log\langle r_*\rangle\ne0$。
这里使用的是原两个实际观察的自由系数 (64)，
不是任选一个用于制造非零的常数。
S 与 T 的自由系数相同，故其归一差没有这个常数项。

完整函数由 (61) 直接定义：
e 保 unit，d 和四个其它变量保全，
使用 (22) 的全部项
$L_\zeta^k(e_*e+TM_\zeta)^{6-k}$ 和真实原分母，
对 (63) 及全部 $\zeta_J$ 求原平均。
因此其正次数系数满足
$$
v_p([T^j](\mathcal A_{A,\mathcal U}
          -\mathcal A_{S,\mathcal U}))
\ge-\lfloor\log_pj\rfloor.
$$
设
$\ell_p=v_p(d M_*\log\langle r_*\rangle)<\infty$。
对每个 $n>\ell_p$，真实积分准确满足
$$
\boxed{
v_p\left(
 \int_{\mathcal U_n}d[
 \log\langle Y_A/7\rangle-\log\langle Y_S/\gamma\rangle]
 \overline h_n\,d\rho\right)=\ell_p .}
\tag{69}
$$
外面的 $\beta^{5n}$ 是单位，不能将它当成额外 p 深度。
这支付了一个完整补域管的实际全尾；
(69) 的深度固定，绝非随 n 自动高于 (52) 的 n。

### 9.5 与新两态比例保持同一实际域

管的全部新坐标可以不借抽象存在写出。
置 $x=\xi_1$、$s=\xi_4-4x/3$，其余四深变量仍记
$u_2,u_3,u_5,u_6$，则
$$
\begin{aligned}
H&=x-u_2-u_3,\\
K&=(-1+4\delta/3)x+\delta s+\omega u_2+\omega^2u_3,\\
J&=u_5-u_6,\\
A&=x-\omega^2u_2-\omega u_3-\delta u_5-\delta u_6,\\
N&=8x/3+2s-2u_2+2u_3-u_5-u_6,\\
Y_A&=(7+4\delta)x+3\delta s+
        \pi u_2+\bar\pi u_3+2\delta u_5+2\delta u_6 .
\end{aligned}
\tag{70}
$$
所以 (57) 等价于 H unit，以及
$$
J,\quad A-H,\quad N-8H/3,\quad
K-(-1+4\delta/3)H,\quad
Y_A-(7+4\delta)H\in p^n .
\tag{71}
$$
前四个条件只读伴随，最后一个是真正的 Y-伴随 mixed cut。
若使用 R1040 的两态比例，必须保持这个差别。
(67)–(69) 不把某个局部常数改称整个补域，不给未平均 S/T 行赋零，
也不把正的局部首项充作主目标的完成。
现在需要消费的是 (65)–(71) 这些明确的实际补偿项。

## 依赖与执行边界

- R297、R398：原 S34/T72、完整六 sigma 及同源缩放。
- R1038 §§10–14：E3969 的同一实际126来源、全平方/通常全群桥和规范；
  本篇不重做其 $p=5$ 已完锚。
- R522、R531：原 norm3 整个偶纤维、普通 full-core 返回和完整质量处理。
- R410：同一原无限 ray、$1\pm\lambda$ 的单位性。
- R968：标准 even $\mathcal S_{10}$ 的真实 $\chi_{10}$ 和 whole 带中心规范。

全文使用显示的固定线性代数、theta 纤维、矩和原有界测度恒等式；
没有新增数学运行、素数扫描或缓存矩阵输入。


## 10. 同一两 unit 管的完整一次项和真实 degree25 型五来源

本节仍使用 §9 的原 $\mathcal R$、12个实际平均支和同一 unit 域。
没有把管外部分、$D_1\setminus D_n$ 或其它 unit 扇区删除。
新增的是 (68) 中 S/T 差的完整一次系数。

### 10.1 原双 sigma 的三阶条件矩

置
$$
H_m(z)=
 \left.\partial_w^m\{\sigma(3z-4w)\sigma(4z+3w)\}\right|_{w=0}.
$$
这正是 (60) 的 d 条件矩，变量顺序未交换。
令 $X=x^3$。同一个原 $E_b$ 上有整来源身份
$$
\boxed{
H_3=432b\,\sigma^{25}x
       (-35X^3+84bX^2+84b^2X+208b^3),
\qquad H_3=-15120b\,z^5+O(z^{11}).}
\tag{72}
$$
它是 standard odd degree25 空间的实际型五向量。
(72) 不把它认成 F0 的 $\mathcal C_\pm$ 或原 degree34 型五线。

以下给出不依赖新执行的完整证明。先取 b=1。
两条整数行 $(3,4),(-4,3)$ 正交，交叉准周期指数准确消失，
故 $\partial_w^3$ 保整个 degree25 线束。
反演及 $\mu_6$ 类型使其唯一形状为
$\sigma^{25}xP_3(X)$，$\deg P_3\le3$。
原 $\sigma(z)=z+z^7/210+\cdots$ 给
$[z^5]H_3=-15120$，固定三次项。

令
$c_P(u)=e^{-\zeta(P)u}\sigma(P+u)/\sigma(P)$。
在三种真实挠点使用
$Dx=2y,\ Dy=3x^2$，
$$
c_{(e,0)}(u)=1-\tfrac e2u^2+\cdots,\qquad
c_{(0,1)}(u)=1-\tfrac13u^3+\cdots .
$$
三个完整规范值为
$$
\boxed{
P_3(-1)=104976,\qquad P_3(0)=89856,\qquad
P_3(8)=-5038848.}
\tag{73}
$$
其常数可直接核：

* 在 $T=(e,0)$，$e^3=-1$，
  $\mathcal R(z,0)/\sigma(z)^{25}$ 在 $T+u$ 首项为 $-2916u$。
  整个局部双函数为固定常数乘
  $c_T(3u-4w)\sigma(4u+3w)$；常数除 $\sigma(T)^{25}$ 为−729。
  在 u=0，三阶 w 导数为 $-144e$，故得第一值。
* 在 $S=(0,1)$，同一首项为 $768u$，局部常数为256。
  $[(3u-4w)(-(4u+3w)^3/3)]_{uw^3}=117$，
  三阶导数为 $702u$；除 $x(S+u)=2u+\cdots$ 得第二值。
* 在 $P=(2,3)$，$3P=(-1,0)$、$4P=(0,-1)$。
  原交叉准周期仍消失；
  $c_{3P}(-4w)c_{4P}(3w)$ 的三阶 w 导数为54。
  $\sigma(3P)\sigma(4P)/\sigma(P)^{25}
    =72\cdot(-2592)$；
  再除 x(P)=2，得到第三值。

四个条件恰确定
$P_3=-15120X^3+36288X^2+36288X+89856$，
即 (72) 的 b=1 形式。
一般 b 由 $t^6=b$、
$\sigma_b(z)=t^{-1}\sigma_1(tz)$ 返回；
第三 w 导数的全尺度为 t，
因此 (72) 外面的 b 因子必须保留。

在同一个原普通周期 $\Omega$ 上，
条件矩的测度身份是
$$
\boxed{
(\operatorname{forget}d)_*(d^m\nu_{\mathcal R})
       =\Omega^m\nu_{H_m}.}
\tag{74}
$$
定义真正 e-unit 负一读数
$\mathcal I_{3,p}=\int_{e\ {\rm unit}}e^{-1}\,d\nu_{H_3}(e)$。
(74) 中不存在额外 m!；
它已在 $H_m=\partial_w^m\mathcal R$ 内。

### 10.2 十二支的完整有限系数

保持 (64) 的
$$
a'=\frac{15+19\delta}{50},\qquad
e_*=\frac{93\omega}{50}.
$$
两支 (63) 的 d 系数为
$\ell_0=-\omega^2,\ \ell_1=\omega$。
记 $l_2,l_3,l_5,l_6$ 为 $L_\zeta$ 中四个其它深变量的系数。
$Y_T-Y_S$ 的准确深部分为
$$
\Delta Z=(3\delta-1)u_5+2u_6 .
$$
在每组六个 $\zeta_J$ 上取实际平均，定义
$$
R_j=\operatorname{avg}_{\zeta_J}
        l_2l_3\{(3\delta-1)l_6+2l_5\}.
$$
由 (66) 已显示的全部 l 值，准确得到
$$
\boxed{
R_0=-250-95\omega,\qquad R_1=84+273\omega,}
\qquad
\boxed{\begin{aligned}
S_0&=R_0+R_1=-166+178\omega,\\
S_1&=\ell_0R_0+\ell_1R_1=-428-439\omega,\\
S_3&=\ell_0^3R_0+\ell_1^3R_1=334+368\omega.
\end{aligned}}
\tag{75}
$$
例如第一支 $l_2l_3=6-5\omega$，$l_5,l_6$ 的均值都是
$5(\omega-1)/2$；
第二支对应 $-1+11\omega$ 和 $-3(2+3\omega)/2$。
所以 (75) 包括所有 J 支，不是选一条代表。

因为 S/T 在 T=0 的自由系数完全相同，
原归一 logarithm 差在 T=0 整体为零。
因此一次项只由
$d\,\Delta Z/(a'e)$ 产生；
测试质量的 T 导数乘的是零，没有另一个隐藏项。

四个原 sigma 各自最低矩为一次，下一次为七次。
总次数 $k+1\le7$ 时，它们只能各取一次。
这使 k=0,1,2 全零；k=5 仍被原 $q_5=0$ 杀掉。
剩下的完整混合系数准确为
$$
[u_2u_3u_5u_6]L_\zeta^k\Delta Z
 =\frac{k!}{(k-3)!}\ell_j^{\,k-3}d^{k-3}
             l_2l_3\{(3\delta-1)l_6+2l_5\},
\quad k=3,4,6 .
\tag{76}
$$

### 10.3 实际一次读者，保每一个 Euler 因子

原联合二次矩和 e 的 whole unit 核给
$$
\begin{aligned}
\int_{e\ {\rm unit}}e^2\,d\nu_{\mathcal R}
 &=24\Omega^2(1+\lambda\kappa^2),\\
\int_{e\ {\rm unit}}de\,d\nu_{\mathcal R}
 &=-7\Omega^2(1+\lambda\kappa),\\
\int_{e\ {\rm unit}}d^3e^{-1}\,d\nu_{\mathcal R}
 &=\Omega^3\mathcal I_{3,p}.
\end{aligned}
$$
最后一行使用完整负一泛函，未把一个形式负次数 Euler 因子
代进去。于是 (22)、(63)、(74)–(76) 给
$$
\boxed{\begin{split}
[T](\mathcal A_{T,\mathcal U}-\mathcal A_{S,\mathcal U})
=-\frac{d}{18144h^6ba'}\bigg\{&
144q_3e_*^3S_0\frac{1+\lambda\kappa^2}{1+\lambda\kappa^3}\\
&-168q_4e_*^2S_1\frac{1+\lambda\kappa}{1+\lambda\kappa^2}\\
&+\frac{120q_6S_3}{1+\lambda}\,
                    \Omega\mathcal I_{3,p}\bigg\}.
\end{split}}
\tag{77}
$$
$18144=84\cdot216$，
其中216来自原1296平均内每支的六个 J 值。
四个深 sigma 的 $\Omega^4$、
联合矩的实际 factorial、原 $-1/84$ 及 $b\Omega^6$
全部已在 (77) 中返回。

### 10.4 代数部分严格非零；负一项的范围保持

记 (77) 大括号的前两项为 $A_p$，最后一项为
$B_p\Omega\mathcal I_{3,p}$。
两者的系数均为代数数，
$B_p=120q_6S_3/(1+\lambda)\ne0$。
原 (19) 还给
$$
q_3/q_4=-799/567.
\tag{78}
$$
而且对当前 $p>1296$，有严格的新结论
$$
\boxed{A_p\ne0.}
\tag{79}
$$
这是完整代数数的非零，不只是一个 mod p 首项。
若 $A_p=0$，则在原复嵌入中
$$
\left|
\frac{(1+\lambda\kappa^2)^2}
     {(1+\lambda\kappa^3)(1+\lambda\kappa)}
\right|
=\left|\frac{7S_1}{6(q_3/q_4)e_*S_0}\right|<\frac34 .
$$
右侧的严格界可只用
$|S_1|<434,\ |S_0|>297,\ |q_3/q_4|>7/5,\ |e_*|>9/5$。
左侧则因 $|\kappa|=1,\ |\lambda|=p^{-1/2}<1/36$，
严格大于 $(35/37)^2>3/4$，矛盾。
没有把 $\lambda$ 的 p-adic 单位性误当作其复绝对值。

(79) 尚不单独排除
$A_p+B_p\Omega\mathcal I_{3,p}=0$。
要使用 R749 的点对数分离，须先为 (72) 的**整个**
degree25 来源支付实际有限5角色、点域和共同周期，
不能把它换成先前 degree34 的三条九阶线或 E21609 的负一值。
本篇到这里不预授该点桥。

### 10.5 原全尾与完整补域

S/T 的本管常数项为零。
与 §9.4 同一完整有界测度和同一单位条件给
$$
v_p([T^j](\mathcal A_{T,\mathcal U}
                 -\mathcal A_{S,\mathcal U}))
\ge-\lfloor\log_pj\rfloor\qquad(j\ge1).
\tag{80}
$$
若后续证明 (77) 非零，记其估值为 $\ell_p$；
则由同一个全尾，对 $n>\ell_p$ 有本管积分的准确深度
$n+\ell_p$。这是一条管内结论。

全原平均积分仍必须写为
$$
\boxed{
\int (L_T-L_S)\overline h_n\,d\rho
 =
\int_{\mathcal U_n}(L_T-L_S)\overline h_n\,d\rho
+\int_{\operatorname{supp}\overline h_n\setminus\mathcal U_n}
       (L_T-L_S)\overline h_n\,d\rho .}
\tag{81}
$$
右边第二项包含全部其它 unit 扇区和
$(D_1\setminus D_n)$ 的原中间环；
它没有因本节取一个有限 Taylor 系数而消失。
原坏条件也没有给未授权的 S/T 平均零行。
本节新支付的是 (72) 的真实来源及 (77) 的完整有限首项，
可以在有限点载体上继续接线，不将其冒作无穷 logarithm 的点投影。


## 11. 中间环的完整 dyadic 核：精确两态返回和原一 unit 扇区

本节支付 (55)–(56) 中的整个中间环。所有等式使用原六输入上的
测度限制与推前，不以某个局部网格的首项替代其补域。
原未旋转的三个观察还给一个更强的准确结论：整个
$\mathcal D_1$ 的两中央差赋值为一，与 carry 深度 $n$ 无关。

### 11.1 72 支的完整 degree372 核

令 $\mathscr Z$ 为 (47) 的全部72个四元组。
各支原行仍为 (45)–(46)，有
$$
D_\zeta{}_1=0,\quad ND_\zeta=93,\quad
D_\zeta\overline E_\zeta^{\,t}
=D_\zeta\overline Y_A^{\,t}=0 .
\tag{82}
$$
这里后两个正交是完整行的身份。$Y_A$ 正交于全部五伴随；
而 $F_\zeta\perp C$、$NF_\zeta=81$、$NC=12$ 和
$r=81/12$ 给第一项。不能将 $D_\zeta$ 换成 (48) 的两个平均多项式行。

各 $D_\zeta$ 的第2、3、4坐标在 $\mathcal O_K$，最后两个为
$$
\begin{aligned}
d_5&=-\frac{5+\omega}{2}\zeta_J
       -2(1+\omega)\delta\zeta_A-\frac{1-\omega}{2}\zeta_N,\\
d_6&=\frac{5+\omega}{2}\zeta_J
       -2(1+\omega)\delta\zeta_A-\frac{1-\omega}{2}\zeta_N .
\end{aligned}
$$
所以 $D_\zeta$ 整当且仅当 $\zeta_J/\zeta_N=\pm1$；
准确24支整、48支只有分母二。
若记 $a_j=2d_j$，后48支中
$$
a_2,a_3,a_4\equiv0\pmod2,\qquad
a_5\equiv a_6\equiv\omega^2(\zeta_J+\zeta_N)\ne0\pmod2.
\tag{83}
$$
于是整支的第一轴为 standard odd degree93；
对所有支共同沿第一生成变量作 $[2]$ 覆盖后，则为 standard even
degree372，另一切输出全部保留。该覆盖在当前普通处为单位倍点，
不改变深度或单位条件。

原 ray 已有 $g_\pi\equiv3\bmod8$、$g_\pi\equiv1\bmod93$，故
$g_\pi\equiv187\bmod744$。在完整 $\mathcal S_{372}$ 的 canonical
Schrödinger 基 $e_j,\ j\in\mathbf Z/372$，原含中心二挠 lift 为
$$
\mathcal T_{(s+r\omega)/2}^{372}e_j
=(-1)^{s(j+93r)}e_{j+186r}.
$$
置 $\epsilon(0)=1$、$\epsilon(t)=-1$ 对非零二挠，并定义
$$
P_\epsilon=\frac14\sum_{t\in E[2]}\epsilon(t)\mathcal T_t^{372},
\qquad
\mathsf B=2P_\epsilon-I.
$$
与 R551 §2 的全 Heisenberg 证明完全同一，直接得到
$$
\boxed{
P_\epsilon=\frac14(I-\mathsf D)(I-\mathsf X),\quad
\mathsf B e_j=-e_{187j},\quad
\mathsf B^2=I .}
\tag{84}
$$
这里 $\mathsf D e_j=(-1)^je_j$、$\mathsf X e_j=e_{j+186}$。
$187^2\equiv1\bmod744$，所以该排列实现原 core 的完整 Heisenberg
交织，中心相位也一致。$P_\epsilon$ 的像恰为
$[2]^*\mathcal S_{93}^{\rm odd}$，维数93，$\mathsf B$ 在该像上为一。

odd degree93 的 whole 核已由第2节的
$\sigma(\delta\gamma_{31}z)$ 真实锚锁为 $\beta$。
它与单位倍点 $[2]$ 交换，因而锁定整个 degree372 的
**实际深核为 $\beta\mathsf B$**。
若把外部 $\lambda$ 剥掉，原 core 是 $-\mathsf B$；
不能漏掉这个负号。

将 (84) 放回每个实际第一轴，记其完整联合算子为
$\mathsf B_\zeta$。设
$$
P_{\zeta,t}
=I+(t-1)\overline D_\zeta^{\,t}D_\zeta/93 .
$$
于是全部伴随保留的测度等式为
$$
\boxed{
\rho|_{\{D_\zeta\in p^r\}}
=\beta^r(P_{\zeta,\kappa^r})_*
       \mathsf B_\zeta^r\rho,\qquad r\ge0.}
\tag{85}
$$
对于24个整支，$\mathsf B_\zeta\rho=\rho$，可直接用原 odd93 核。
其余48支不将 $\mathsf B_\zeta\rho$ 擅自认成 $\rho$。

这些新来源是有界整测度，而非只在复 theta 空间中的符号。
确切地，(85) 在 $r=1$ 给
$\mathsf B_\zeta\rho
=\beta^{-1}(P_{\zeta,\kappa^{-1}})_*
(\rho|_{D_\zeta\in p})$。
该逆只在所写深域使用，并将其送回原整格；
$93$ 和 $\beta$ 是单位，所以测度范数不增。
再用 (84) 得到整个两态 $(\rho,\mathsf B_\zeta\rho)$ 的返回。
不需要新增数学运行或选择另一半周期相位。

### 11.2 所有原中间环的准确返回

在 (56) 中写
$$
D_\zeta=T_m d_\zeta,\quad
E_\zeta=e_0x+T_m e_\zeta,\quad
Y_A=7x+T_m Z_A,\qquad T_m=\kappa^m.
$$
$d_\zeta,e_\zeta,Z_A$ 仍是原五个深坐标的完整线性式。
由 (82)，$x$、$e_\zeta$、$Z_A$ 被 $P_{\zeta,t}$ 逐个固定。
因此剩余 $d_\zeta\in p^{n-m}$ 可用 (85) 取回，
不会移动实际 Mellin 权或 E 的单位域。

对 $\varepsilon=0,1$，定义一个真正的固定解析函数
$$
\mathcal A_{\zeta,\varepsilon}(T)
=\frac d{h^6b\Omega^6}
 \int_{x\ {\rm unit}}
 \log\langle x+TZ_A/7\rangle
 \sum_{k=0}^6
 \frac{q_kd_\zeta^k(e_0x+Te_\zeta)^{6-k}}
      {1+\lambda\kappa^{6-k}}\,
 d(\mathsf B_\zeta^\varepsilon\rho).
\tag{86}
$$
它在 $T\in p\mathcal O$ 解析；$p>1296$ 时所有自由系数是单位。
原 period、Euler 分母和全部 J/N 相位一项未删。
因来源有界，其 log 尾有与原 (28) 相同的次数分母界。
但不假设 $\varepsilon=1$ 时的质量或常数项为零。

令
$I_{\zeta,m}^{(n)}=\int_{\mathcal D_m}L_Ah_n(C,F_\zeta)\,d\rho$。
先取回原五个深输入，再用 (85)，得到
$$
\boxed{
I_{\zeta,m}^{(n)}
=\beta^{n+4m}
 \mathcal A_{\zeta,\,(n-m\bmod2)}(\kappa^m),
\qquad 1\le m\le n.}
\tag{87}
$$
在 $m=n$ 时没有额外第一轴限制，正是原网格
$\beta^{5n}\mathcal A_{\zeta,0}(\kappa^n)$。
(87) 中的 $4m$ 来自 $5m+(n-m)$，不能把五个原深核与
新的第一轴深核重复计数。

因此全部相邻环带是
$$
\begin{aligned}
\int_{\mathcal D_m\setminus\mathcal D_{m+1}}
 L_Ah_n(C,F_\zeta)\,d\rho
={}&\beta^{n+4m}
 \mathcal A_{\zeta,n-m\bmod2}(\kappa^m)\\
&-\beta^{n+4m+4}
 \mathcal A_{\zeta,n-m-1\bmod2}(\kappa^{m+1}).
\end{aligned}
\tag{88}
$$
求这个有限和，整个中间环的返回准确为
$$
\boxed{
\int_{\mathcal D_1\setminus\mathcal D_n}
 L_A\overline h_n\,d\rho
=\frac1{1296}\sum_{\zeta\in\mathscr Z}
 \left\{
 \beta^{n+4}\mathcal A_{\zeta,n-1\bmod2}(\kappa)
 -\beta^{5n}\mathcal A_{\zeta,0}(\kappa^n)
 \right\}.}
\tag{89}
$$
整个 $\mathcal D_1$ 的贡献因而只含 $n$ 的奇偶来源和外部 $\beta^n$；
无需把无限多个中间深度当作独立输入。
这不是“中间环更深”的估计：第二项与 (52) 的原网格项
**精确相消后**才得到完整单 unit 扇区。
至少两个原输入为 unit 的真正余域仍存在。

### 11.3 未旋转三观察：整个单 unit 扇区恰有一位

对于原未旋转的 $D=F-C$，来源在 odd93 上，
故 $\mathsf B\rho=\rho$。而 $D$ 还同时正交于 $Y_S,Y_T$。
因此 (87) 对原 (28) 的三函数本身成立：
$$
\boxed{
\int_{\mathcal D_m}L_i\widehat Q_{n,p}\,d\rho
=\beta^{n+4m}\mathcal A_i(\kappa^m),
\quad i=S,T,A,\quad 1\le m\le n .}
\tag{90}
$$
限制与测试始终包括原 $\Gamma_n$；在该式左端用第4节的
域外延零约定。

(30)、(36) 和原完整 log 尾界给
$v_p(\mathcal A_i(\kappa)-\mathcal A_j(\kappa))=1$。
所以对所有 $n\ge1$，
$$
\boxed{
v_p\!\left(\int_{\mathcal D_1}
 (L_i-L_j)h_n\,d\rho\right)=1,\qquad i\ne j .}
\tag{91}
$$
对 $n>1$，同一个中间环的未旋转差也恰有一位：
其两个精确项分别有赋值 $1$、$n$，不可能相消。
这是原 (38) 的真正补域消费，不是再次证明同一网格赋值。

如果三条 canonical 中央同时为零，(42) 因而强迫整个
$\Gamma_n\setminus\mathcal D_1$ 的相应差也具有准确赋值一，
并等于 (90) 在 $m=1$ 的负数。
该域包含全部其它 unit pattern 和真实相加 cut；
本节没有由 (91) 给它赋零。
第9–10节的两 unit 厚管只占其中一个部分，仍须与它们之外的
完整余域联立。


## 12. 整个至少双 unit 余域的首位：原真除 p 与无周期有限公式

本节只处理原未旋转 $h_n={\bf1}_{\Gamma_n}\widehat Q_{n,p}$，
保三条原观察及各自 unit cut。
它给 $\Gamma_n\setminus\mathcal D_1$ 的完整首位，
不是把第9–10节指定的 $\mathcal U_n$ 当作这个余域。
平均后的 $\overline h_n$ 仍按 (89) 保全部72个来源状态。

置 $d=p-1$。令 $\mathcal F_i$ 是原整个边际 $(Y_i)_*\rho$ 的生成函数：
$$
\begin{aligned}
\mathcal F_S&=S_{34},&
\mathcal F_T&=6\delta T_{72},&
\mathcal F_A&=39\delta\Phi_{126,b},\\
a_{i,d}&=[z^d]\mathcal F_i(z).&&&
\end{aligned}
\tag{92}
$$
这里 $S_{34},T_{72},\Phi_{126,b}$ 均取首项 $z^6$ 的旧准确规范。
特别 T 和 A 的两个原常数没有消掉。

### 12.1 在原完整单位域上先付除 p

原 $\Omega$ 是 E17 普通形式群与乘法形式群之间的单位周期，
所以 $v_p(\Omega)=0$。$\nu_\sigma$ 为原整 Amice 测度；
$p>1296$ 时 $\rho$ 的 $84$ 及本篇 frame/carry 固定分母均为单位。
于是各 $(Y_i)_*\rho$ 是整测度。原三 canonical 的完整 unit 质量
在第4节已付为零：
$$
\int_{Y_i\ {\rm unit}}d\rho=0.
$$
此式只在所写的完整 unit 域上使用。

对任意 $y\in\mathbf Z_p^\times$，
$d\log\langle y\rangle=\log(y^d)$，且 $y^d-1\in p\mathbf Z_p$，
故
$$
d\log\langle y\rangle\equiv y^d-1\pmod{p^2}.
$$
非 unit 部分的 $y^d$ 积分则属于 $p^d\mathcal O\subset p^2\mathcal O$。
用上一条完整质量零，及原 Amice 矩的准确阶乘归一，得到
$$
\boxed{
J_{\mathcal F_i}'(0)
 \equiv \int y^d\,d\nu_{\mathcal F_i}
 =\Omega^d d!\,a_{i,d}\pmod{p^2},\qquad
a_{i,d}\in p\mathcal O .}
\tag{93}
$$
右端的可除 p 是证明所得，不是把模 p 系数形式除 p。
由于 $d!$ 与 $\Omega$ 都是单位，它也给 $a_{i,d}/p$ 的真实整性。

全域上用 $Y_i/a_i$ 代替 $Y_i$ 只增加
$-d\log\langle a_i\rangle$ 乘完整 unit 质量，所以在 (93) 中准确消去。
在 $\mathcal D_1$、$\mathcal U_n$ 或其它局部扇区中，
不能据此删掉对应质量项；本节下式使用的是 (28) 已保质量的原归一函数。

### 12.2 保全部余域的第一 Schur 读数

由 (25)、(90) 的完整来源身份，
$$
\begin{split}
\beta^{-n}\int_{\Gamma_n\setminus\mathcal D_1}
 (L_i-L_j)h_n\,d\rho
={}&J_{\mathcal F_i}'(0)-J_{\mathcal F_j}'(0)\\
&-\beta^4\{\mathcal A_i(\kappa)-\mathcal A_j(\kappa)\}.
\end{split}
$$
原 (36) 及其全尾保证
$\mathcal A_i(\kappa)-\mathcal A_j(\kappa)
\equiv\kappa(d/b)(\alpha_i-\alpha_j)\bmod p^2$。
因此对每个 $n\ge1$，整个至少双 unit 余域的准确首位为
$$
\boxed{
\frac{\beta^{-n}}p
 \int_{\Gamma_n\setminus\mathcal D_1}(L_i-L_j)h_n\,d\rho
\equiv
\Omega^d d!\,\frac{a_{i,d}-a_{j,d}}p
-\lambda^6\frac d b(\alpha_i-\alpha_j)\pmod p .}
\tag{94}
$$
左端为整：每个原 $L_i$ 在其 unit 域上都属于 $p\mathcal O$，
而 $h_n$ 有界整。全部不同的 $Y_i$-unit 条件仍留在实际积分中；
(94) 并未用“各输入为 unit”替代“原和变量为 unit”。

### 12.3 用原形式群精确消掉周期

写 $p=6s+1$，并置
$$
\mathfrak h_p=\binom{3s}{2s}\pmod p,\qquad
\mathcal H_{b,p}=b^s\mathfrak h_p .
$$
$\mathcal H_{b,p}$ 是 $y^2=x^3+b$、微分 $dx/(2y)$ 的 Hasse invariant：
它就是 $(x^3+b)^{(p-1)/2}$ 中 $x^{p-1}$ 的系数。
其全部阶乘都小于 p，故当前普通处为单位。

为核绝对周期规范，取原整参数 $u=-x/y=z+\cdots$。
原 height-one 形式群的 $[p]$ 在特征 p 中首项为
$\mathcal H_{b,p}u^p$。
原同构 $u(\Omega\log(1+T))$ 的首系数是 $\Omega$；
与乘法形式群 $[p](T)\equiv T^p$ 比较首项，准确得到
$$
\Omega^{p-1}\equiv\mathcal H_{b,p}^{-1}\pmod p.
$$
同时 $\pi_0$ 与 E0 的真正 Frobenius 至多差 $\mu_6$，
$\bar\pi_0^6\equiv\mathfrak h_p^6\bmod p$。
由 $\lambda=-\bar\pi_0^{-1}$、$b^{p-1}\equiv1$ 和 Wilson 得
$$
\boxed{
\Omega^d d!\equiv-\mathcal H_{b,p}^{-1},\qquad
\lambda^6\equiv\mathfrak h_p^{-6}
                  =\mathcal H_{b,p}^{-6}\pmod p .}
\tag{95}
$$
这里只取六次幂，故没有在实际 CM unit phase 上擅选 Frobenius 号。

### 12.4 三条原六 sigma 的有限低卷积

下面的公式给 (94) 的全部剩余算术输入，
只需固定三个六元组和低于第一个普通共振的有限系数。
在 $b=1$ 取
$$
W(w)=z^2x_1(z)=\sum_{r\ge0}w_rw^r,\qquad
f(w)=\sigma_1(z)/z,\qquad w=z^6.
$$
由 $x''=6x^2$、$(x')^2=4(x^3+1)$ 及
$(\log\sigma)''=-x$，准确递推为
$$
\begin{split}
&w_0=1,\qquad w_1=-1/7,\\
&w_r=\frac{\sum_{j=1}^{r-1}w_jw_{r-j}}
              {(r-1)(6r+1)}\quad(r\ge2),\\
&\log f(w)=-\sum_{r\ge1}
          \frac{w_r}{6r(6r-1)}w^r .
\end{split}
\tag{96}
$$
保原固定 CM 行
$$
\begin{split}
\boldsymbol a_S&=(\gamma,\bar\gamma,\delta,2\delta,1,2),\\
\boldsymbol a_T&=(\gamma,\bar\gamma,\delta,2\delta,3\delta,4),\\
\boldsymbol a_A&=(7,\pi_{13},\bar\pi_{13},3\delta,2\delta,2\delta),
\end{split}
$$
其中 $\gamma=3+\omega$、$\pi_{13}=4+\omega$。
令 $\gamma_S=1,\gamma_T=6\delta,\gamma_A=39\delta$，定义
$$
\boxed{
c_{i,p}=\gamma_i[w^{s-1}]
 \exp\left\{-\sum_{r=1}^{s-1}
 \frac{w_r}{6r(6r-1)}
       \left(\sum_{\ell=1}^6 a_{i,\ell}^{6r}\right)w^r\right\}.}
\tag{97}
$$
三个 $\gamma_i$ 正是 $-\prod_\ell a_{i,\ell}/84$。
故 (97) 是六个原 sigma **完整乘回后的系数**，
没有将六个因子分别赋中央零。

在 $r\le s-1$，(96) 的 $(r-1)$、$6r+1$、
$6r$、$6r-1$ 及指数展开需要的阶乘都为 p 单位。
所以 (97) 可在 $\mathcal O_K/p^2$ 中用固定递推直接读取，
没有隐藏的先除 p 步骤，也不需上一个已失真的 Gaussian 高项。
最后由 (93) 付真正一次除 p。

真实六 sigma homothety
$\sigma_b(z)=t^{-1}\sigma_1(tz)$、$t^6=b$ 给
$$
\boxed{a_{i,d}=b^{s-1}c_{i,p},\qquad c_{i,p}\in p\mathcal O.}
\tag{98}
$$
把 (95)、(98) 代回 (94)，得到完全无 period 的有限函数
$$
\boxed{
\frac{\beta^{-n}}p
 \int_{\Gamma_n\setminus\mathcal D_1}(L_i-L_j)h_n\,d\rho
\equiv
\frac1b\left\{
-\mathfrak h_p^{-1}\frac{c_{i,p}-c_{j,p}}p
+\mathfrak h_p^{-6}(\alpha_i-\alpha_j)
\right\}\pmod p .}
\tag{99}
$$
所有符号在原普通嵌入约化；$1/b$、$\mathfrak h_p$ 均是单位。
这给整个余域而不只是某一 unit pattern 的跨 p 算术公式。

坏三 canonical 条件在此首位严格要求
$$
\boxed{c_{S,p}/p=c_{T,p}/p=c_{A,p}/p=0\pmod p .}
\tag{100}
$$
于是 (99) 回到 (91) 的相反固定单位项。
目前 (96)–(100) 并未证明三项不可同时为零：
后续需要在这个**同一个有限低卷积**上取得真正非零或全精度消元，
不能把 (99) 所计算的实际补偿再宣布为零。
