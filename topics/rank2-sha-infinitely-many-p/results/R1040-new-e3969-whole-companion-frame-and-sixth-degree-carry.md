# R1040 — E3969 真六轴的完整小伴随框架与单项六次 carry

日期：2026-11-27。**状态：以下整框架、完整 H/J 纤维分解、单项六次返回、两个实际 whole 核、四输出 carry、完整 K 主型返回及五伴随主型乘积均已证明。** 来源是 R1038 §§10–14 已完全识别的固定 rank2 曲线 E3969。先保留另外三个伴随输出，再准确分离 K 主型；其余 mixed 条件及全部单位补域保持；本篇不宣称主问题已完成。

本篇使用原普通 ray。其 $\lambda,\kappa$ 不是惰性模型中同名的参数。新的 $C,F$ 也不是 R968 的旧共同平面；下文每个推前都明确保新的四个实际输出。

## 1. 原模型、整周期及真正的算术边际

沿 R968 固定
$$
\omega^2+\omega+1=0,\qquad \delta=1+2\omega,\qquad
\pi=(7+\delta)/2=4+\omega,\qquad N\pi=13,
$$
$$
b=17,\qquad y^2=x^3+b,\qquad Dx=2y,\qquad
\lambda=-\bar\pi_0^{-1},\quad
\kappa=p\lambda^2\in p\mathcal O^\times,\quad d=p-1,
\qquad
\rho=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
$p>211$ 在原无限普通 ray 上；$\Omega$ 是原普通单位周期。
所有原输入及以下固定整自同构都使用同一个 $\Omega$。
$\pi$ 是固定 norm13 元，而 $\pi_0$ 是当前普通素数的原生成元，二者不混用。

R1038(76) 已对同一实际 E3969 来源证明
$$
\Phi_{126,b}(z)=
\frac{\sigma_b(7z)\sigma_b(\pi z)\sigma_b(\bar\pi z)
      \sigma_b(3\delta z)\sigma_b(2\delta z)^2}{-3276\delta}.
\tag{2}
$$
它的首项为 $z^6$。这里保从该篇 $b=1$ frame 返回 (1) 的整周期账本：
取 $t^6=17$、$\Omega_1=t\Omega$，则
$$
\Phi_{126,17}(z)=t^{-6}\Phi_{126,1}(tz),\qquad
\Phi_{126,17}\bigl(\Omega\log(1+T)\bigr)
=t^{-6}\Phi_{126,1}\bigl(\Omega_1\log(1+T)\bigr).
\tag{3}
$$
因此原物理单位域不变，
$J_{126,17}=17^{-1}J_{126,1}$。
这是同一 $\psi_{E3969}$ 来源的微分/frame 返回，不将它改贴成 E17 的 Hecke 字符。
也不把可能不属于 $\mathbb Q_p$ 的 $t$ 偷当成 $\mathbb Z_p$ 的自映射。

令
$$
a=(7,\pi,\bar\pi,3\delta,2\delta,2\delta),\qquad Y=a\xi.
$$
由 $\prod_i a_i=-3276\delta$ 及 (1) 的原符号，
$$
\boxed{Y_*\rho=39\delta\,\nu_{\Phi_{126,17}}.}
\tag{4}
$$
R1038 已付全有限角色、Schwartz、Gaussian、通常 Selmer/全 Sha 桥及固定 rank2 锚。
故在该曲线的坏中央假设下，本篇可用的真实条件是
$J'_{126,17}(0)=0$，不是把六个 sigma 因子各自赋零。

## 2. 六行完整正交框架

定义五个原六输入行
$$
\begin{aligned}
H&=(1,-1,-1,0,0,0),\\
K&=(-1,\omega,\omega^2,\delta,0,0),\\
L&=(1,3+5\omega,-2-5\omega,-2\delta,0,0),\\
J&=(0,0,0,0,1,-1),\\
M&=(14,2\pi,2\bar\pi,6\delta,-17\delta,-17\delta).
\end{aligned}
\tag{5}
$$
行与观察使用同一字母。它们与 $a$ 的完整 Hermitian Gram 是
$$
\boxed{
\operatorname{Gram}(a,H,K,L,J,M)
=\operatorname{diag}(126,3,6,51,2,2142).}
\tag{6}
$$
例如 $\pi+\bar\pi=7$ 给 $a\perp H$；
$\pi+3\delta=-7\omega^2$、
$\bar\pi-3\delta=-7\omega$ 给 $a\perp K,L$。
$N(3+5\omega)=N(-2-5\omega)=19$，所以
$NL=1+19+19+12=51$。
前四个 $a$ 系数的范数和为102，而 $M$ 在前四项为 $2a$、
后两项为 $-17\delta$，故
$a\bar M^{\,t}=204-204=0$、
$NM=4\cdot102+2\cdot17^2\cdot3=2142$。
其余内积将 (5) 代入即为零；这里保全部六行，未只核第一边际。

令 $\mathcal F$ 按 $(a,H,K,L,J,M)$ 的次序排列。
其前四列、前四行的行列式为306。
对最后一行作 $M\leftarrow M-2a$ 后，最后二乘二块为
$\left(\begin{smallmatrix}1&-1\\-21\delta&-21\delta\end{smallmatrix}\right)$。
于是
$$
\boxed{
\det\mathcal F=-12852\delta,\qquad
N(\det\mathcal F)=2^4\,3^7\,7^2\,17^2.}
\tag{7}
$$
所以 (5)–(7) 在当前好普通位给原六输入的整自同构。
没有丢掉任何隐藏输入。

各方向的整个标准半特征也由原系数确定：

| 方向 | degree | 原标准半特征 |
|---|---:|---|
| $Y$ | 126 | even |
| $H$ | 3 | odd |
| $K$ | 6 | even |
| $L$ | 51 | odd |
| $J$ | 2 | even |
| $M$ | 2142 | even |

证明是逐个检查模2非零的 CM 系数数目，依次为4、3、4、3、2、2。
Hermitian 交叉为零，使各方向的周期变换没有其余生成变量的隐藏线性项。
特别，$L$ 的 norm51 不把它识别成某条已知 canonical 来源；
$M$ 的 degree2142 也不单凭数值认成 degree34 的旧来源。

## 3. 两个低维方向的完整联合分解

以后记
$$
C=H,\qquad F=J,\qquad
\mathcal A=(Y,K,L,M),\qquad \eta=\mathcal A_*\rho.
\tag{8}
$$
令 $\mathcal B(y,c,k,l,f,m)$ 为 $\mathcal F_*\rho$ 的整个生成来源。

$C$ 方向属于整个标准 odd $\mathcal S_3$。
完整基为
$\sigma^3,x\sigma^3,-y\sigma^3$，其中前两项奇、末项偶。
其唯一偶线为
$$
B_3(z)=-y(z)\sigma(z)^3
      =\frac{\sigma(2z)}{2\sigma(z)},\qquad B_3(0)=1.
\tag{9}
$$
这是 R522 的完整纤维论证在本篇实际行 (5) 上的直接应用。
也可在原三个 sigma 中直接看出：其余所有行均满足
$u_1=u_2+u_3$，而 $C$ 的三个系数为 $(1,-1,-1)$；
所以没有未付的移动半特征。

$F$ 方向属于整个标准 even $\mathcal S_2$，基为
$\sigma^2,x\sigma^2$，二者都是偶函数；
其 principal $\mu_6$ 线恰为
$$
\Theta(z)=x(z)\sigma(z)^2,\qquad \Theta(0)=1.
\tag{10}
$$
事实上其余五行在最后两个位置的系数相等。
原最后两因子就是 $\sigma(u+f)\sigma(u-f)$，
而准确 sigma 加法式为
$$
\sigma(u+f)\sigma(u-f)
=\sigma(u)^2\{\Theta(f)-x(u)\sigma(f)^2\}.
\tag{11}
$$
因此 (10) 的绝对系数也已支付。

令 $\Pi_{C,+}$ 是 $C\mapsto-C$ 的偶平均，
$\Pi_{F,0}$ 是完整 $F\mapsto\zeta F$、$\zeta\in\mu_6$ 的 principal 平均。
两个物理算子分别为
$I-2\bar C^{\,t}C/3$ 及
$I+(\zeta-1)\bar F^{\,t}F/2$。
它们交换，固定 (8) 的全部四输出。
由 (9)–(11) 的完整空间而非有限 jet，严格有
$$
\boxed{
\Pi_{C,+}\Pi_{F,0}\mathcal B
=B_3(c)\Theta(f)\mathcal B(y,0,k,l,0,m).}
\tag{12}
$$
等价地，在 $(C,F;\mathcal A)$ 坐标上是完整测度身份
$$
\boxed{
\Pi_{C,+}\Pi_{F,0}(\mathcal F_*\rho)
=\nu_{B_3}\otimes\nu_\Theta\otimes\eta.}
\tag{13}
$$
(13) 对全部连续测试成立，$\eta$ 的 $Y,K,L,M$ 之间所有 mixed 条件均保。
但 $\eta$ 本身没有被断言为四个一维测度的张量。

例如 $\varphi(C,F)$ 对 $C$ 偶、对 $F$ principal，
且 $g$ 是四输出的任意连续函数，则
$$
\int \varphi(C,F)g(\mathcal A)\,d\rho
=(\nu_{B_3}\otimes\nu_\Theta)(\varphi)\,\eta(g).
\tag{14}
$$
若 $g$ 再含未运输的 $C,F$ 条件，(14) 不能这样拆分。
若 $g$ 含 $K,L,M$，其中央也不由 (4) 免费变成已知零。

## 4. 完整六次条件矩及单项返回

同一原方程给
$$
x=z^{-2}-\frac b7z^4+O(z^{10}),\qquad
\sigma=z+\frac b{210}z^7+O(z^{13}),
$$
故
$$
B_3=1+\frac{3b}{10}z^6+O(z^{12}),\qquad
\Theta=1-\frac{2b}{15}z^6+O(z^{12}).
\tag{15}
$$
由完整纤维 (12)，不是只对裸边际，
$$
\begin{aligned}
(\mathrm{forget}\ C)_*(C^6\rho)
 &=216b\Omega^6(\mathrm{forget}\ C)_*\rho,\\
(\mathrm{forget}\ C)_*(C^2\rho)
 &=(\mathrm{forget}\ C)_*(C^4\rho)=0,\\
(\mathrm{forget}\ F)_*(F^6\rho)
 &=-96b\Omega^6(\mathrm{forget}\ F)_*\rho.
\end{aligned}
\tag{16}
$$
最后一式也直接由整个 $\mathcal S_2$ 两个基的第六系数得到。
整个 $F$ 方向均为偶函数，所以任意奇 $F$ 矩在保其余全部五输出时为零。

因此对 $1\le j\le5$，
$$
\boxed{\mathcal A_*(C^jF^{6-j}\rho)=0.}
\tag{17}
$$
$j$ 奇时 $6-j$ 奇，使用完整 $F$ 奇矩零；
$j=2,4$ 时使用 (16) 的完整 $C$ 条件矩。
这没有把来源乘积的中央当成乘积泛函。

置
$$
r=\frac23,\qquad D=F-C,\qquad E=F+rC.
\tag{18}
$$
则 $D\perp E$，$ND=5$、$NE=10/3$，准确反解为
$$
C=\frac35(E-D),\qquad F=\frac35(E+rD).
\tag{19}
$$
$DE^5$ 中纯 $C^6$ 的系数是 $-r^5=-32/243$，
纯 $F^6$ 的系数是1。
全部其他项由 (17) 消去。因此
$$
\boxed{
\mathcal A_*(DE^5\rho)
=-\frac{1120}{9}b\Omega^6\,\eta,}
\qquad
216\left(-\frac{32}{243}\right)-96=-\frac{1120}{9}.
\tag{20}
$$
即完全固定的单项六次权
$$
\boxed{Q(C,F)=-\frac9{1120b\Omega^6}\,DE^5}
\tag{21}
$$
在完整四输出上返回1。
不需要保一串高次项，也没有以删掉某个未知矩来得到 (20)。

## 5. 两个不同的 whole 核及绝对符号

实际整行是
$$
\boxed{
D=(-1,1,1,0,1,-1),\qquad
3E=(2,-2,-2,0,3,-3).}
\tag{22}
$$
前者整个标准 odd degree5，后者整个标准 even degree30。
它们与所有 $\mathcal A$ 输出的 Gaussian 交叉均严格为零。

R551(7) 支付整个 odd $\mathcal S_5$ 的原绝对 core。
记
$$
u_D=\chi_{65}\lambda,\qquad \chi_{65}^2=1.
\tag{23}
$$
对 degree30，R968 的同一原 ratio 满足
$g_\pi=\pi_0/\bar\pi_0\equiv1\bmod15$、
$g_\pi\equiv3\bmod4$，因而
$$
g_\pi\equiv31=1+30\pmod{60}.
\tag{24}
$$
如 R968 §2，标准 even $\mathcal S_{30}$ 的两个完整 canonical
Heisenberg 生成元及中心均被保持：
$31^2\equiv1\bmod60$。
Schur 引理使原归一 core 在整个空间上为 scalar，未只在 projective 商上为 scalar。

绝对锚使用固定非零整 CM 拉回
$$
[\delta]^*\mathcal S_{10}^{\rm even}\subset
\mathcal S_{30}^{\rm even}.
\tag{25}
$$
它保持标准 even 半特征，并与原普通深限制交换。
R968(9) 已付 $\mathcal S_{10}$ 的实际符号 $\chi_{10}^2=1$，
故 degree30 的符号准确也是 $\chi_{10}$。
以后记
$$
\boxed{u_E=\chi_{10}\lambda.}
\tag{26}
$$
这里不认 $\chi_{65}=\chi_{10}$，也不选取其中某个号。
固定 $3$ 的物理单位覆盖将 $3E$ 返回 $E$，没有新 scalar。

令
$$
P_{R,t}=I+(t-1)\bar R^{\,t}R/NR,\qquad R=D,E.
$$
完整来源身份为
$$
\boxed{
\rho|_{\{D\in p^n\}}=u_D^n(P_{D,\kappa^n})_*\rho,\qquad
\rho|_{\{E\in p^n\}}=u_E^n(P_{E,\kappa^n})_*\rho.}
\tag{27}
$$
各式保其余五输出；特别 $D,E$ 正交使它们可按原域顺序联用。
这是整个 (22) 来源的 whole 核，不从 (4) 的单个 canonical 边际反推。

## 6. 保四输出的完整剪裁 carry

定义真正的正交投影
$$
\Pi_{\rm new}
=I-\frac13\bar C^{\,t}C-\frac12\bar F^{\,t}F.
\tag{28}
$$
其像是秩四整直和项，由 $Y,K,L,M$ 完整识别。
下式既可写成 $\Pi_{\rm new,*}$，也可写成 $\mathcal A_*$。

对 $n\ge1$，真实域
$$
\Gamma_n=\{D\in p^n,\ E\in\mathcal O^\times\}
=\{C,F\in\mathcal O^\times,\ F-C\in p^n\}.
\tag{29}
$$
等价性由 (19) 及 $5/3$ 为单位逐点得到。
在此域定义
$$
\boxed{
\widehat Q_{n,p}
=-\frac9{1120b\Omega^6}\,
  \frac{(D/\kappa^n)E^5}{1-u_E\kappa^5},}
\tag{30}
$$
域外延为零。
$D/\kappa^n$ 在原域整；新增分母模 $p$ 为1，因此整个权整且有界。
尤其不需要对 $1-u_E$ 作任何额外除法。

先用 (27) 的 $D$ 核归一 $D/\kappa^n$。
该缩放固定 $E$ 及整个 $\Pi_{\rm new}$，所以真实 $E$ 单位域不动。
再用 $E$ 核计算 $E^5$ 的单位部分，准确产生
$1-u_E\kappa^5$。
最后代入 (20)，严格得到
$$
\boxed{
\mathcal A_*({\bf1}_{\Gamma_n}\widehat Q_{n,p}\rho)
=u_D^n\eta,}
\tag{31}
$$
等价于
$$
\Pi_{\rm new,*}({\bf1}_{\Gamma_n}\widehat Q_{n,p}\rho)
=u_D^n\Pi_{\rm new,*}\rho.
$$
(31) 对四输出的任意完整连续测试成立，包括所有真正 mixed 紧开域。
没有把六变量恒等误称为删去 $C,F$ 之前的恒等。

### 6.1 三支与六次对称

对 $\zeta\in\mu_3$，置
$$
D_\zeta=F-\zeta C,\qquad
E_\zeta=F+r\zeta C,\qquad
\Gamma_{n,\zeta}=\{D_\zeta\in p^n,\ E_\zeta\ {\rm unit}\}.
\tag{32}
$$
$D_\zeta$ 仍有五个模2非零系数，$3E_\zeta$ 仍只有末两系数模2非零；
所以两个 whole 核分别仍是同一个 $u_D,u_E$。
$D_\zeta E_\zeta^5$ 的纯 $C^6$ 系数是 $-r^5\zeta^6=-r^5$，
(17) 仍逐项适用。于是 (30)–(31) 对每支都成立。

定义
$$
\mathfrak q_{n,p}
=\frac13\sum_{\zeta\in\mu_3}
{\bf1}_{\Gamma_{n,\zeta}}
\left\{-\frac9{1120b\Omega^6}
\frac{(D_\zeta/\kappa^n)E_\zeta^5}{1-u_E\kappa^5}\right\}.
\tag{33}
$$
三支互不相交，并集准确为
$$
\Gamma_n^{(3)}
=\{C,F\ {\rm unit},\ F^3-C^3\in p^n\}.
$$
完整返回是
$$
\boxed{\mathcal A_*(\mathfrak q_{n,p}\rho)=u_D^n\eta.}
\tag{34}
$$
此权在 $C\mapsto\omega C$ 下仅循环三支，在全部六输入同时乘
$\mu_6$ 下也不变。这里的 $C$ 旋转是 (28) 对应的新物理旋转；
没有将它冒认成 R968 的旧几何算子或断言原 $\rho$ 被它固定。

## 7. 真正的中央行、全部补域及尚未消掉的 mixed 项

由 (4)、(34)，同一个真实单位 cut 上完整 Mellin 身份是
$$
\boxed{
\int_{Y\ {\rm unit}}\langle Y\rangle^{dv}
       \mathfrak q_{n,p}\,d\rho
=39\delta\,u_D^nJ_{126,17}(v).}
\tag{35}
$$
在已付坏中央假设 $J'_{126,17}(0)=0$ 下，(35) 的导数确为零。
每个单支 (31) 也分别给同一结论。

但对任意涉及 $K,L,M$ 的连续权 $g$，真实式只有
$$
\int {\bf1}_{Y\ {\rm unit}}\log\langle Y\rangle\,
 g(Y,K,L,M)\mathfrak q_{n,p}\,d\rho
=u_D^n
\int {\bf1}_{Y\ {\rm unit}}\log\langle Y\rangle\,g\,d\eta.
\tag{36}
$$
右边通常仍是未知的完整 mixed 中央，不能由 (4) 赋零。
同样，$\log\langle aY+bC\rangle$ 及其实际单位域不能穿过 (13) 改成
$\log\langle Y\rangle$。

为把非零子管与全域区别写成同一式，任取实际紧开
$\mathcal U\subset\Gamma_n^{(3)}\cap\{Y\ {\rm unit}\}$，则坏中央假设准确给
$$
\boxed{
0=
\int_{\mathcal U}d\log\langle Y\rangle\,
           \mathfrak q_{n,p}\,d\rho+
\int_{(\Gamma_n^{(3)}\cap\{Y\ {\rm unit}\})\setminus\mathcal U}
d\log\langle Y\rangle\,\mathfrak q_{n,p}\,d\rho.}
\tag{37}
$$
这两个项使用完全相同的来源、权及原单位 cut。
本篇没有宣称第二项消失。

特别，(22) 的 $D$ 和 $E$ 同时不读第四个原输入，
而任何其他单个原坐标单独为单位时均不能使 $D$ 深、$E$ 单位。
所以 R968 的旧“五深一单位”非零网格不能直接搬到 (29)；
若使用两单位配对网格，两个单位输入的完整相关域及其余补域必须一起保留。
也没有把旧 $S/T/W^\pm/Z$ 的原观察认作 (28) 的四输出。

本篇新增的是：(7) 的小整框架、(12)–(17) 的完整条件矩、
(20) 的单项返回、(27) 中各自保号的两个 whole 核，以及
(31)/(34)/(35) 的真实四输出 carry 和算术必要行。
$L$ 的 odd degree51、$M$ 的 even degree2142 以及 (37) 的单位补域继续作为实际来源保留。
把它们识别成其他算术线、或证明同一读者的剩余量非零，仍须付完整来源和投影，不能只凭范数相等。



## 8. 原 K 方向的完整一维主型及真实 norm17 混合

本节在原来源上再消去一个实际伴随，未把整个 $\mathcal S_6$ 误认成一维。

### 8.1 三个 norm3 行与准确的17矩阵

在前四个原坐标中置
$$
R=(1,-\omega,-\omega^2,0),\qquad
V=(1,-\omega^2,-\omega,0),\qquad
U=R+\delta e_4,\qquad K=-R+\delta e_4.
\tag{38}
$$
$H,R,V$ 是整个三坐标 Fourier 框架，彼此正交且范数均为3。
$U,K,V$ 彼此正交，范数分别为6、6、3。
若
$$
P=(7,\pi,\bar\pi,3\delta,0,0),\qquad
Q=(0,0,0,0,\delta,\delta),
$$
则原行完整等于
$$
\boxed{
P=3U+4V,\qquad L=-2U+3V,\qquad
Y=P+2Q,\qquad M=2P-17Q.}
\tag{39}
$$
前两个等式的实际矩阵是
$\left(\begin{smallmatrix}3&4\\-2&3\end{smallmatrix}\right)$，
行列式为17。它确切解释 $NP=102=6\cdot17$、$NL=51=3\cdot17$。
这仍不把 $L$ 或 $P/\delta$ 直接认成 E17 的 canonical 行。

### 8.2 两个小 theta 恒等式决定全部 K 主型

写 $X(z)=x(z)^3$，并置
$$
T(z)=\sigma(z)^3,\qquad A(z)=x(z)\sigma(z)^3,\qquad
B(z)=B_3(z),\qquad
F_6^-(z)=\sigma(z)^6\bigl(X(z)-2b\bigr).
\tag{40}
$$
整个 odd $\mathcal S_3$ 基 $T,A,B$ 的 $\mu_6$ 型分别是3、1、0。
两个正交 norm3 方向因而给完整三 sigma 恒等式
$$
\boxed{
\prod_{j=0}^{2}\sigma(r+\omega^j v)
=T(r)B(v)+B(r)T(v).}
\tag{41}
$$
证明：左边在 $r,v$ 上都属于标准 odd $\mathcal S_3$，
整体型为3；全部可能的张量只有 $T\otimes B$、$B\otimes T$。
分别令 $r=0$、$v=0$，由 $B(0)=1$ 确定两个系数都为1。
因此 (41) 是全函数身份，不是仅由首项推断。

令 $\Pi_{0,k}$ 作用于完整 $k$ 变量。
以下两个准确恒等式是
$$
\boxed{
\begin{aligned}
\Pi_{0,k}\{T(u-k)A(u+k)\}
 &=x(u)\sigma(u)^6F_6^-(k),\\
\Pi_{0,k}\{B(u-k)A(u+k)\}
 &=-x(u)y(u)\sigma(u)^6F_6^-(k).
\end{aligned}}
\tag{42}
$$
为完整证明 (42)，两个 $u,k$ 空间均为标准 even $\mathcal S_6$，
交叉 Gaussian 为零。
其 principal 子空间的完整基是
$\sigma^6X,\sigma^6$；
其 type4、type1 子空间分别只有
$x\sigma^6$、$-xy\sigma^6$。
所以每一式的右侧必为所示 $u$ 因子乘
$\sigma(k)^6(X(k)+c b)$，只需支付真正的 $c$。

使用准确展开
$$
T=z^3+\frac b{70}z^9+\cdots,\qquad
A=z-\frac{9b}{70}z^7+\cdots,\qquad
B=1+\frac{3b}{10}z^6+\cdots,
$$
第一式左边的 $u^4k^6$ 系数为
$$
\frac b{70}
\{(84-126)-9(-35+105-63+7)\}
=-\frac{12b}{5}.
$$
第二式的 $uk^6$ 系数为
$(3b/10)(1-6)-(9b/70)7=-12b/5$。
另一方面
$\sigma^6(X+cb)=1+(c-2/5)b\,k^6+\cdots$，
故两式都给 $c=-2$。
这是完整有限维空间中的全部系数证明，没有省略第二条 principal 线。

### 8.3 原六 sigma 的全部三输出返回

使用 $(y,h,k,l,j,m)$ 为 (5) 的实际 Fourier 变量，定义
$$
p_0=y+2m,\qquad q_0=2y-17m,\qquad
u=3p_0-2l,\qquad v=4p_0+3l.
\tag{43}
$$
先不作 $K$ 投影。原前三个 sigma 在 $(H,R,V)$ 生成变量中为
$$
\prod_{a=0}^{2}\sigma\bigl(h+\omega^a(u-k)+\omega^{-a}v\bigr).
$$
原来第二、第三个输入各有一个负号，两个 sigma 负号正好相消。
取完整 $H$ 偶部分后，它准确变为
$$
B(h)\{T(u-k)B(v)+B(u-k)T(v)\}.
$$
第四个原 sigma 是 $\sigma(\delta(u+k))=\delta A(u+k)$。
最后两个原 sigma 的 $J$ 主型由 (11) 准确给
$\Theta(j)\sigma(\delta q_0)^2$。
代入 (42)，再用 (41)，得到整个来源恒等式
$$
\boxed{
\Pi_{C,+}\Pi_{K,0}\Pi_{F,0}\mathcal B
=B_3(h)F_6^-(k)\Theta(j)\,\mathcal B_3(y,l,m),}
\tag{44}
$$
其中绝对规范未变，
$$
\boxed{
\mathcal B_3(y,l,m)
=-\frac1{84}\,
\sigma(\delta u)
\prod_{a=0}^{2}\sigma(u+\omega^a v)\,
\sigma(\delta q_0)^2.}
\tag{45}
$$
$\mathcal B_3$ 正是 $(Y,L,M)_*\rho$ 的完整生成来源。
例如 $l=m=0$ 时，$u=3y,v=4y,q_0=2y$；
$3+4\omega=-\omega^2\pi$、
$3+4\omega^2=-\omega\bar\pi$，
两个单位的乘积为1，所以 (45) 严格回到 (4)，没有新增 phase。

(44) 等价于完整测度身份
$$
\boxed{
\Pi_{C,+}\Pi_{K,0}\Pi_{F,0}(\mathcal F_*\rho)
=\nu_{B_3}\otimes\nu_{F_6^-}\otimes\nu_\Theta
 \otimes (Y,L,M)_*\rho.}
\tag{46}
$$
三个因子都质量1。
$\nu_{F_6^-}$ 的有界整性也由原整个来源得到：
对 (46) 取原 $Y^6$ 条件矩，其系数为
$39\delta\,6!\Omega^6$，在当前好位是单位；
所以可从原整测度及有限主型投影直接提取该因子。
不必另猜一个 p-adic 函数是否属于测度格。

由 $F_6^-=1-(12b/5)z^6+\cdots$，另有准确条件矩
$$
\boxed{
(Y,L,M)_*(K^6\rho)
=-1728b\Omega^6\,(Y,L,M)_*\rho.}
\tag{47}
$$
这里已经忘去 $C,F$；若要保它们，使用的是 (46) 的实际投影，
不是未经投影的六变量身份。

### 8.4 对新 carry 的真正中央消费范围

$K\perp C,F$，所以其 $\mu_6$ 物理旋转逐点保持 $D_\zeta,E_\zeta$ 和全部 $\Gamma_{n,\zeta}$。但 $H$ 偶平均与 $J$ 主型一般不保持这些 cut。以下正确顺序是先用(34)忘去 $C,F$、保完整 $Y,K,L,M$，再在该四输出上用(46)的 $K$ 因子；不让 $H/J$ 平均提前穿过原 cut。

由于 (34) 保完整 $Y,K,L,M$，对任意 principal 连续权 $\varphi(K)$
和 $(Y,L,M)$ 上的完整连续 $g$，可合法联用 (34)、(46)，得到
$$
\boxed{
\int \varphi(K)g(Y,L,M)\mathfrak q_{n,p}\,d\rho
=u_D^n\,\nu_{F_6^-}(\varphi)
       \int g(Y,L,M)\,d\rho.}
\tag{48}
$$
因此当 $g={\bf1}_{Y\ {\rm unit}}\langle Y\rangle^{dv}$ 时，
右边是 $39\delta\,u_D^n\nu_{F_6^-}(\varphi)J_{126,17}(v)$。
坏中央假设确使这些完整行的导数为零。
$\varphi$ 可以包含 $K$ 的真实单位或深条件；它没有被换成任意 mixed 的 $Y/K$ 条件。

(45) 的 $Y,L,M$ 仍是一个完整三变量来源。
特别不能从17矩阵 (39) 或新条件矩 (47)
给 $L$、$M$、$\log\langle aY+bL+cM\rangle$ 赋中央零。
后继剩余现在由这个固定三变量式及原单位补域明确控制。


## 9. 剩余 L/M 的完整三处 gluing 与 M→S34 提取恒零

本节支付原绝对三挠字符，证明结论在整个三变量来源上成立。
它不是只检查 M 的第一边际或质量。
因此此前拟作的 M2142→S34 数值提取已由整函数证明解决，无需执行。

### 9.1 odd 目标必须保留的原字符

取原 CM 周期 $\lambda_0$，使 $\chi_\sigma(\lambda_0)=-1$，
令 $u_0=\lambda_0/\delta$。
$\ker\delta$ 使用代表 $0,u_0,-u_0$，置
$$
\epsilon(u)=\chi_\sigma(\delta u),\qquad
\epsilon(0)=1,\quad\epsilon(\pm u_0)=-1.
\tag{49}
$$
所有 $\mathsf T_{R,u}$ 都是原 canonical Weyl lift；
对一个 norm $3m$ 的标准 sigma theta 方向，
真正 $[\delta]^*\mathcal S_m$ 的 kernel 特征是 $\epsilon(u)^m$。
这是将原准周期式直接代入 $g(\delta(z+u))$ 后得到的；
不把 odd 目标的 kernel lift 冒认成无相位。

因此其准确 old projector 为
$$
\boxed{
P_{\delta,R}=\frac13\sum_{u\in\ker\delta}
       \epsilon(u)^{-m}\mathsf T_{R,u},\qquad m=NR/3.}
\tag{50}
$$
重相位后的三个 kernel 算子组成真正的有限群作用，
所以 (50) 是 projector，像恰为原 $[\delta]^*\mathcal S_m$。

对 $H$，$m=1$，其 old 像为
$[\delta]^*\mathcal S_1=\mathbb C\,\sigma(\delta h)$，是奇线。
$P_{\delta,H}$ 与 $h\mapsto-h$ 交换，因 (49) 对 $u,-u$ 对称。
于是
$$
\boxed{P_{\delta,H}\Pi_{C,+}\mathcal B=0,}
\tag{51}
$$
也可由 (9) 的唯一偶线 $B_3$ 直接看出。
注意这里是 $I-\mathsf T_{H,u_0}-\mathsf T_{H,-u_0}$ 杀掉 $B_3$，
不是未加权的三项和。

### 9.2 原六 sigma 的实际周期关系

以下均是原六输入整行，末尾未写的零坐标也保留：
$$
\begin{array}{c|c|c|c}
R&R+sH=\delta G_R&G_R&NG_R\\ \hline
Y&Y-H&
(-2\delta,-1-3\omega,-2-3\omega,3,2,2)&43\\
K&K+H&(0,-\omega^2,\omega,1,0,0)&3\\
L&L-H&(0,\bar\gamma,-\gamma,-2,0,0)&18\\
M&M+H&(-5\delta,1-2\delta,-1-2\delta,6,-17,-17)&715
\end{array}
\tag{52}
$$
这里 $\gamma=(5+\delta)/2=3+\omega$。
每一式由 (5)、(38) 逐坐标得到。
因为 $R\perp H$、$NH=3$，
$NG_R=NR/3+1=m+1$。

对 $u\in\ker\delta$，$(R_i+sH_i)u=G_{R,i}\delta u$ 是每个原 sigma 的整周期。
两个正交 Weyl 指数与这些原准周期指数准确抵消：
线性项只为 $NR\,z_R+NH\,z_H$，
二次项只为 $(NR+NH)u/2$，其余全部生成变量的交叉为零。
剩下的真实符号为
$\prod_i\chi_\sigma(G_{R,i}\delta u)$。
在 $\mathcal O_K/2=\mathbb F_4$ 中，每个非零系数都保原奇符号，
而非零系数数目的奇偶性正是 $NG_R=m+1$ 的奇偶性。
所以在原整个来源上有
$$
\boxed{
\mathsf T_{R,u}\mathsf T_{H,su}\mathcal B
=\epsilon(u)^{m+1}\mathcal B.}
\tag{53}
$$
这支付了所有 six-sigma phase，而不是仅由同一个抽象 Heisenberg 交换子猜符号。

将 (53) 乘 (50) 的权并对三个 $u$ 求和，得到
$$
P_{\delta,R}\mathcal B
=\frac13\sum_u\epsilon(u)\mathsf T_{H,-su}\mathcal B
=P_{\delta,H}\mathcal B.
$$
$P_{\delta,R}$ 与 $H$ 偶投影交换，右侧完整加权和也与该投影交换。
由 (51)，准确推出
$$
\boxed{
P_{\delta,R}\Pi_{C,+}\mathcal B=0
\qquad(R=Y,K,L,M).}
\tag{54}
$$
这里从未将单个 $\mathsf T_{H,u}$ 穿过 $H$ 偶投影。
只有完整加权和可交换；各个单独 translate 不能因此被赋予一个标量。

### 9.3 整个三变量来源的准确三挠关系

$K,J$ 的投影与 $Y,L,M$ 的实际 kernel 算子交换，
因为各方向在 (6) 中正交。
因此 (54) 对 (45) 的整个 $\mathcal B_3(y,l,m)$ 仍成立：
$$
\boxed{
\begin{aligned}
(I+\mathsf T_{Y,u_0}+\mathsf T_{Y,-u_0})\mathcal B_3&=0,\\
(I-\mathsf T_{L,u_0}-\mathsf T_{L,-u_0})\mathcal B_3&=0,\\
(I+\mathsf T_{M,u_0}+\mathsf T_{M,-u_0})\mathcal B_3&=0.
\end{aligned}}
\tag{55}
$$
$Y/3$、$M/3$ 的 theta degree 分别为42、714，均 even；
$L/3$ 的目标 degree 为17，odd，故中间一式必须带负号。
等价地，未加权的 L 三项和为 $2\mathcal B_3$，不能误写为零。
这些式保全部 Y/L/M 系数，不只在原点成立。

令 $\alpha_+=3\gamma$、$\alpha_-=3\bar\gamma$，均 norm63。
它们都被 $\delta$ 整除。
M 方向的实际 old 子空间
$[\alpha_\pm]^*\mathcal S_{34}$ 包含于
$[\delta]^*\mathcal S_{714}$，因为
$\alpha_\pm/\delta=-\delta\gamma_\pm$。
(55) 的最后一式因此立即给出
$$
\boxed{
\mathcal T_{\alpha_+}^{(M)}\mathcal B_3
=\mathcal T_{\alpha_-}^{(M)}\mathcal B_3=0.}
\tag{56}
$$
$\mathcal T$ 是未平均的完整 CM trace，保其他两个实际输出；
$34$ 和 $714$ 都是 even，所以这里没有隐藏的 odd-target rephase。

特别，M 第一边际的两个完整63纤维返回均为零，
原 $\mathcal S_{34}$ 的全部六坐标都为零，
随后 R297 的 E17 projector 也必为零。
这不是只知道其质量列为零，也没有留下待数值决定的投影系数。
$NM=63\cdot34$ 虽与旧 E17 pull 的 degree 相同，
真实来源却已被 (56) 完整排除在该 old 像外。

### 9.4 同一结论的完整 module-linearity 返回

另可直接沿 R1038 的实际原边际核查 (56)。
令
$$
F_0=\sigma(7z)\sigma(\pi z)\sigma(\bar\pi z)\sigma(3\delta z),
\qquad \deg F_0=102\quad\hbox{standard even}.
$$
原算术来源是
$$
\Phi_{126}
=\frac{F_0\,[\delta]^*(\sigma(2z)^2)}{-3276\delta}.
\tag{57}
$$
R1037 §4(18)–(22) 的完整 trace/pull
$T_M E_M=3I$、§9 实际层 $[0,1,0,0]$，
与 R1038 §11(53)
$\Phi_{378}=-E_{126}\Phi_{126}/27$，
已经严格给出完整 $T_{42}\Phi_{126}=0$。

kernel trace 对真正 pullback 因子满足原 module-linearity；
它由 $\mathsf T^{N_1+N_2}(fg)
=(\mathsf T^{N_1}f)(\mathsf T^{N_2}g)$ 逐项证明。
在 (57) 中，目标 degrees34、8、42 全是 even，
所以原未加权的 trace 正确。
可提出 $[\delta]^*(\sigma(2z)^2)$；
它不是零函数，于是完整 $\delta$ trace 的 $F_0$ 因子必为零。

而 M 的原六 sigma 正是
$$
\boxed{
\prod_i\sigma(M_i z)
=F_0(2z)\,[\delta]^*(\sigma(17z)^2).}
\tag{58}
$$
$[2]$ 与 $\delta$ 互素，它们的完整 Weyl pull/trace 交换，
故 $F_0(2z)$ 仍为 $\delta$-new。
(58) 的目标 degrees136、578、714 仍全是 even。
再次用完整 module-linearity，M 的整个 $\delta$ trace 为零；
随后沿 $\alpha_\pm/\delta$ 的完整 trace 给 (56) 的第一边际版本。

这里用的是 kernel trace 对已指明 pullback 因子的线性性质，
没有传播中央泛函的乘积零。
整个三变量版本则由 (52)–(55) 已另外支付。
L/M 的其他真正 $\delta$-new 分量、三变量 mixed 单位域及 (37) 的补域继续保留；
(55) 的有限 theta 翻译也不等于将物理 logarithm 的输入简单相加一个 torsion 常数。


### 9.5 三个方向的原字必须联动

(53) 的 Y/M 两式还给更强的整个来源作用：
$$
\boxed{
\mathsf T_{Y,u}\mathsf T_{M,u}\mathcal B_3=\mathcal B_3,\qquad
\mathsf T_{Y,u}\mathsf T_{L,-u}\mathcal B_3
=\epsilon(u)\mathcal B_3.}
\tag{59}
$$
证明可在原 $\mathcal B$ 上先用
$\mathsf T_{Y,u}\mathsf T_{H,-u}=\epsilon(u)$、
$\mathsf T_{M,u}\mathsf T_{H,u}=\epsilon(u)$、
$\mathsf T_{L,u}\mathsf T_{H,-u}=1$；
各正交方向的实际 Weyl 算子交换，
$\mathsf T_{H,-u}\mathsf T_{H,u}=I$，
故不留下未定中心相位。
所得联合算子与 H/K/J 投影交换，遂给 (59)。
也可直接核
$Y+M=3(7,\pi,\bar\pi,3\delta,-5\delta,-5\delta)$，
其除 $\delta$ 后范数756为偶；
$Y-L$ 除 $\delta$ 后范数59为奇，分别给 (59) 的两个符号。

令
$$
\tau_Y(u)=\mathsf T_{Y,u},\qquad
\tau_M(u)=\mathsf T_{M,u},\qquad
\tau_L(u)=\epsilon(u)^{-1}\mathsf T_{L,u}.
$$
这三套都是保原目标半特征后真正的 $\ker\delta$ 群作用。
(55)、(59) 准确说明：整个 $\mathcal B_3$ 只有两个非平凡联合字。
对 $\lambda\in\{\omega,\omega^2\}$，设
$$
\mathcal B_{3,\lambda}
=\frac13\sum_{j=0}^2\lambda^{-j}
       \tau_Y(ju_0)\mathcal B_3.
$$
这里 $\tau$ 使用重相位后的真实群作用，不把 $2u_0$ 与 $-u_0$ 的
原 odd lift 无证认同。
完整分解及三个同时特征为
$$
\boxed{
\mathcal B_3=\mathcal B_{3,\omega}+\mathcal B_{3,\omega^2},
\qquad
(\tau_Y(u_0),\tau_L(u_0),\tau_M(u_0))
 \mathcal B_{3,\lambda}
=(\lambda,\lambda,\lambda^{-1})\mathcal B_{3,\lambda}.}
\tag{60}
$$
所以后继必须保这两个相关字，不能把三轴各自的两个非平凡字
视作八个独立组合，或把 δ-old 零当成某个单字零。

对任何原连续 mixed 测试 $f$，(59) 对应的严格读者身份是
$$
\boxed{
\langle\eta_3,f\rangle
=\langle\eta_3,(\tau_Y(u)\tau_M(u))^\dagger f\rangle,\qquad
\eta_3=(Y,L,M)_*\rho.}
\tag{61}
$$
转置按 R985 的整个有限 theta 测度公式执行，保原单位域、
质量和全部 logarithm；它不是物理变量替换 $Y\mapsto Y+u$、
$M\mapsto M+u$。
(60) 的两个实际字给出同一个完整来源的精确联动，
没有额外赋予其中任何一个 mixed 中央零。


## 依赖

- R1038 §§10–14：E3969 的完整有限来源、通常全 Sha 桥、原126完整回乘、确切六 sigma 及 rank2 锚。
- [R522](R522-common-degree3-even-factor-and-same-st-positive-test.md)：原 odd degree3 完整偶纤维与普通周期规范。
- [R551](R551-original-norm5-two-state-core-and-complete-unit-inverse.md)：whole odd degree5 的真实 $\chi_{65}$ 和完整深限制。
- [R968](R968-original-common-degree10-carry-and-positive-eighth-order-difference.md)：原普通 ray、whole even degree10 的绝对 $\chi_{10}$ 及保全输出的 carry 规则。

本篇未运行新的数学数值计算。所有新显示恒等式均由原完整 sigma、有限维 theta 空间与已付 whole 核逐式证明；没有加入新的中央零或删除完整 mixed 补域。

## 10. 真实 norm9/norm14 框架及五个伴随的完整乘积

本节不再沿 M2142 提取已经为零的 old 来源。
用原整数行改写 L/M 后，全部五个伴随的主型部分均可直接确定。
所得是原六 sigma 的完整有限投影身份，不增加第一轴 Hecke projector。

### 10.1 17 完全消失的原正交框架

沿 §8 的 $U,V,Q$ 定义
$$
\boxed{
\begin{aligned}
A_9&=\frac{M+3L}{17}=V-Q
 =(1,-\omega^2,-\omega,0,-\delta,-\delta),\\
N_{14}&=\frac{M-14L}{17\delta}
 =\frac{2U-2V-Q}{\delta}
 =(0,-2,2,2,-1,-1).
\end{aligned}}
\tag{62}
$$
特别这两个都是原六输入的整数行；不是仅在形式分式域换坐标。
完整反解是
$$
\boxed{L=A_9-\delta N_{14},\qquad M=14A_9+3\delta N_{14}.}
\tag{63}
$$
由 $NU=6,NV=3,NQ=6$ 及三者正交，
$$
NA_9=9,\quad NN_{14}=14,\quad A_9\perp N_{14}.
$$
它们也与 $Y,H,K,J$ 全部正交。因此按顺序
$(Y,H,K,J,A_9,N_{14})$ 的完整 Gram 和 determinant 为
$$
\boxed{
\operatorname{Gram}=\operatorname{diag}(126,3,6,2,9,14),\qquad
\det=756,\qquad N\det=2^4 3^6 7^2.}
\tag{64}
$$
可从 (6) 的 determinant 先以 (62) 替换 L/M，
再交换 A/J 两行直接核得其正号。
所以新框架的真实整逆只删 $2,3,7$，没有17费用。

$A_9$ 的模二非零原系数有五个，半特征是 standard odd；
$N_{14}$ 只有最后两个模二非零，半特征是 standard even。
两者都保全部原 Gaussian；正交性消掉的是确切交叉，而非只在原点的项。

### 10.2 norm9 的整个主型 δ-new 线

原逐坐标身份是
$$
\boxed{A_9-H=\delta(0,-\omega,\omega^2,0,-1,-1).}
\tag{65}
$$
右侧除 $\delta$ 后范数为4，是 even。
沿 (49) 的同一 $\epsilon$，
$$
\mathsf T_{A_9,u}\mathsf T_{H,-u}\mathcal B=\mathcal B
\qquad(u\in\ker\delta).
$$
$A_9$ 的 $\delta$-下降目标 degree 为3，仍是 odd。
故其真正 old projector 是
$\frac13\sum_u\epsilon(u)^{-3}\mathsf T_{A_9,u}$。
与 (51) 完全相同的完整加权和论证给
$$
\boxed{P_{\delta,A_9}\Pi_{H,+}\mathcal B=0.}
\tag{66}
$$
后续 K/J/N 的正交投影都与此式交换。

standard odd $\mathcal S_9$ 的主型空间准确为
$$
\sigma(z)^9y(z)\langle1,X(z)\rangle,\qquad X=x^3.
$$
其 old 主型线由
$B_3(\delta z)=-y(z)\sigma(z)^9(X(z)-8b)$ 张成。
真实 new 主型线则是
$$
\boxed{\Theta_9(z)=-y(z)\sigma(z)^9(X(z)+4b),\qquad \Theta_9(0)=1.}
\tag{67}
$$

这里可直接支付其完整 weighted trace，不只检查有限几个矩。
原 division 身份给
$$
\sigma(3z)=3x(z)(X(z)+4b)\sigma(z)^9,\qquad
\Theta_9=-\frac{y}{3x}\sigma(3z).
$$
又
$\sigma(3z)=[\delta]^*(-\sigma(\delta z))$；
目标 degree3 为 odd，故恰带 (66) 的原 $\epsilon$。
若 $S=(0,\sqrt b)$，则 $\ker\delta=\{O,S,-S\}$，原加法公式给
$$
x(P+S)=-\frac{2\sqrt b\,x(P)}{y(P)+\sqrt b},\qquad
x(P-S)=\frac{2\sqrt b\,x(P)}{y(P)-\sqrt b},
$$
$$
x(P)x(P+S)x(P-S)=-4b.
$$
对最后一式取原 $D=d/dz$ 的 logarithmic derivative，得到
$\sum_{u\in\ker\delta}y(P+u)/x(P+u)=0$。
将真正 pullback $\sigma(3z)$ 提出完整 weighted trace，
即证 (67) 的整个 trace 为零。
与 old 线独立，加上主型空间二维，严格得到 (67) 的单重性。
$\Theta_9$ 本身无极；表示中的 $1/x$ 没有被当成任意来源上的无极算子。

### 10.3 norm14 的真实二挠作用与唯一主型线

两个原整数式为
$$
\boxed{
N_{14}+J=2(0,-1,1,1,0,-1),\qquad
N_{14}-J=2(0,-1,1,1,-1,0).}
\tag{68}
$$
右侧两个 quotient 的范数都为4，是 even。
因此对每个 $0\ne t\in E[2]$，完整六 sigma 原 lift 满足
$$
\mathsf T_{N_{14},t}\mathsf T_{J,t}\mathcal B=\mathcal B.
$$
$J$ 的 degree2 为 even，所以 $\mathsf T_{J,t}^{-1}=\mathsf T_{J,t}$。
令 $\mathscr S_R=\sum_{0\ne t\in E[2]}\mathsf T_{R,t}$。
这个完整三项和与对应的主型投影交换，不能将单独的 translate 这样交换。

原 $E_b$ 的二挠点记为 $(e,0)$，$e^3=-b$。
沿 R1021 §13 的实际 Weyl 规范，
$$
q_e^2=\frac{e^2(x-e)}{b\sqrt3},\qquad
x(P+(e,0))=\frac{e(x+2e)}{x-e},
$$
其中 $\sqrt3>0$ 固定原复规范。
于是
$$
\mathsf T_{J,e}(x\sigma^2)
=-\frac{x+2e}{\sqrt3}\sigma^2,\qquad
\boxed{\mathscr S_J\Theta=-\sqrt3\,\Theta.}
\tag{69}
$$
这是整个原 degree2 空间中的实际主型特征，不只按二进维数择号。

由 (68)、正交交换和完整三项和，得到
$$
\boxed{\mathscr S_{N_{14}}\Pi_{J,0}\mathcal B
=-\sqrt3\,\Pi_{J,0}\mathcal B.}
\tag{70}
$$
H/K/A 的投影仍与这条 N 方向的身份交换。

$N_{14}$ 的主型空间准确为
$\sigma^{14}\langle b^2x,bx^4,x^7\rangle$。
在这个完整三列基中，原三项和的矩阵为
$$
\boxed{
\mathscr S_{14}=\frac1{9\sqrt3}
\begin{pmatrix}
11&16&-448\\
10&17&280\\
-1&1&-1
\end{pmatrix}.}
\tag{71}
$$
这也可逐项手证，无需新数值运行：
对 $j=0,1,2$，
将
$(1-t)^{6-3j}(1+2t)^{1+3j}$
的 $t^0,t^3,t^6$ 三个系数分别记为 $1,a_j,b_j$。
三组为
$(1,10,-11),(1,-17,16),(1,280,448)$。
在 $e^3=-b$ 上求三个 e 的和，仅这三槽存留；
连同 $q_e^{14}$ 的准确符号即给 (71)。
该矩阵的平方为 $3I$、迹为 $\sqrt3$，
$-\sqrt3$ 特征线只有一维，向量恰为 $(16,-10,1)$。
因此
$$
\boxed{
\Theta_{14}(z)=\sigma(z)^{14}x(z)(X(z)-2b)(X(z)-8b),
\qquad\Theta_{14}(0)=1}
\tag{72}
$$
是 (70) 保留下来的唯一主型来源。
没有从相同 theta degree 猜曲线，也没有给它新增算术中央零。

### 10.4 整五个伴随的完整因子化

对实际行 R 写 $\Pi_{R,0}$ 为其 $\mu_6$ 主型投影。
在 H 上它等于已用的偶投影，因为 degree3 的整个偶子空间就是主型 $B_3$。
全部五方向正交，故这些投影彼此交换。

先用 (45) 的完整 H/K/J 因子；
再用 (66)–(67) 的 A 主型单重性和
(70)–(72) 的 N 主型单重性。
每一步都对其余所有生成变量逐系数成立。
五个因子在原点均为1，因此剩下的 Y 函数准确是原第一边际，
没有留下待定的共同尺度：
$$
\boxed{
\begin{aligned}
&\Pi_{H,0}\Pi_{K,0}\Pi_{J,0}\Pi_{A_9,0}\Pi_{N_{14},0}
 \mathcal B(y,h,k,j,a,n)\\
&\quad =
39\delta\,\Phi_{126,b}(y)\,
 B_3(h)F_6^-(k)\Theta(j)\Theta_9(a)\Theta_{14}(n).
\end{aligned}}
\tag{73}
$$
这里 $F_6^-=(X-2b)\sigma^6$、$\Theta=x\sigma^2$，
$\mathcal B$ 是原 $-\prod_{i=1}^6\sigma/84$ 在 (64) 的完整六变量返回。
特别 (73) 没有在 Y 上另施一个算术 Hecke projector。
第一轴仍是 R1038 的同一 E3969 来源及其同一 $\Omega_b$。

记 $\mathcal F=(Y,H,K,J,A_9,N_{14})$ 为这个真实整框架。
作为整个有界测度等式，(73) 准确为
$$
\boxed{
\mathcal F_*\mathscr P\rho
=39\delta\,\nu_{\Phi_{126,b}}\otimes
\nu_{B_3}\otimes\nu_{F_6^-}\otimes\nu_\Theta
 \otimes\nu_{\Theta_9}\otimes\nu_{\Theta_{14}}.}
\tag{74}
$$
所有伴随都用同一个原普通单位周期 $\Omega$。
新两个因子的有界整性亦沿 §8.3 直接提取：在完整投影式中对 Y 取第六矩，
系数为 $39\delta\,6!\Omega^6$，在当前好位为单位；再对其余伴随取质量，
分别得到 $\nu_{\Theta_9}$、$\nu_{\Theta_{14}}$。
所以这里使用真实原整测度格，而不是仅由复 theta 身份猜测有界性。
它是一个真实有限投影后的乘积；不是将中央泛函的乘积零当作规则。

新两个因子的首项和完整六阶矩也可直接记录：
$$
\Theta_9=1+\frac{39b}{10}z^6+O(z^{12}),\qquad
\Theta_{14}=1-\frac{164b}{15}z^6+O(z^{12}).
$$
所以五个伴随的实际六阶矩依次为
$$
\boxed{
(216,-1728,-96,2808,-7872)\,b\Omega^6
\quad\text{对应 }(H,K,J,A_9,N_{14}).}
\tag{75}
$$
此处每个数字都包含 $6!$，没有将 Taylor 系数当成测度矩。
这些常数的全部素因子小于211。

### 10.5 可直接使用的原 mixed 测试范围

(74) 的有限投影可完全写回原六输入，保单位域。
对每个伴随行 R 及 $\zeta\in\mu_6$，令
$$
P_{R,\zeta}=I+(\zeta-1)\frac{\bar R^{\,t}R}{NR}.
$$
在当前所有好位它是原局部整自同构，
准确将 R 输出乘 $\zeta$，固定 Y 和其他四伴随。
因此
$$
\mathscr P^\dagger f(\xi)
=\frac1{6^5}\sum_{\zeta_H,\zeta_K,\zeta_J,\zeta_A,\zeta_N\in\mu_6}
 f(P_{H,\zeta_H}P_{K,\zeta_K}P_{J,\zeta_J}
   P_{A_9,\zeta_A}P_{N_{14},\zeta_N}\xi).
\tag{76}
$$
这是原物理线性变换的完整有限平均，不是 torsion 的物理加法替换。

令 $\mathbf c=(H,K,J,A_9,N_{14})$，h 为其任意完整连续有界测试，
可包含这些伴随之间任意 mixed 单位/depth 条件。
记 $\mathscr A h$ 为 (76) 的准确平均，并置
$$
\Lambda_p(h)=
\int h\,d(\nu_{B_3}\otimes\nu_{F_6^-}\otimes\nu_\Theta
                   \otimes\nu_{\Theta_9}\otimes\nu_{\Theta_{14}}).
$$
由 (74)，整个原 Mellin 身份是
$$
\boxed{
\int_{Y\ {\rm unit}}\langle Y\rangle^{dv}
       \mathscr A h(\mathbf c)\,d\rho
=39\delta\,J_{126,b}(v)\,\Lambda_p(h).}
\tag{77}
$$
特别，若 h 本身对五个伴随分别乘 $\mu_6$ 不变，
可以在 (77) 中直接用 h；不必再次平均。
原质量 $J_{126,b}(0)=0$，所以固定归一 $Y/7$ 也不产生额外首导数项。
原 E3969 的坏 Sha 假设因而真正迫使 (77) 的中央首导数为零，
对这里每一个实际完整 h 都成立。

R1042 的共同平面在新框架中的准确位置是
$$
\boxed{
C=2\omega H,\qquad
F=2K-\frac{5+\omega}{2}J
 +2(1+\omega)A_9+\frac{1-\omega}{2}N_{14}.}
\tag{78}
$$
各项的 Hermitian 范数依次为
$24,21/2,36,21/2$，总数81，交叉全部为零。
因此 R1042 的原 $\Gamma_n,Q_{n,p}$ 确只读这五个伴随，
其 (76) 平均是明确的另一套完整测试，所有旋转后的单位域随同保留。
(77) 支付这套平均的整个中央行；
它不把未平均的原 cut 预认成相同。

仍须准确保留剩余范围：
原五深网格在这个框架中一般含 Y 与伴随的混合条件，
它不能只因 (74) 被改成一个与 Y 无关的 h。
R1042 的 $Y_S,Y_T$ 也读这些伴随，不能将它们的 logarithm
替换为 $\log Y$ 后应用 (77)。
后继可用的是 (74)、(76)–(78) 的完整测试转换与明确的五个实际因子，
不是任意 mixed 中央零。

## 11. 五角平均与原三观察共同正交的准确交

本节确定哪些 §10 的真实伴随旋转仍能作为 R1042 的同一个三观察 carry。
它只用原行的完整系数，不将一个方向的合法中央行扩成另外两个方向的中央零。

### 11.1 两个原观察在小框架中的全部系数

按 $(Y,K,J,A_9,N_{14})$ 的次序，两个原观察准确为

| 原观察 | $Y$ | $K$ | $J$ | $A_9$ | $N_{14}$ |
|---|---|---|---|---|---|
| $Y_S$ | $(21-\delta)/63$ | $-\delta/3$ | $-1/2$ | $(3+5\delta)/18$ | $(-8+7\delta)/14$ |
| $Y_T$ | $(30-2\delta)/63$ | $-\delta/3$ | $(3\delta-4)/2$ | $(-15+7\delta)/18$ | $(-9+4\delta)/14$ |

两者的 H 系数都是零。这张表由每个原内积除以
(64) 的对应范数逐项得到，保原六输入。
例如
$\langle Y_S,Y\rangle=42-2\delta$、
$\langle Y_S,K\rangle=-2\delta$、
$\langle Y_S,A_9\rangle=(3+5\delta)/2$、
$\langle Y_S,N_{14}\rangle=-8+7\delta$。
按 (64) 回算，两行范数分别严格为34、72。
其差的伴随系数为
$$
\boxed{
(\Delta_K,\Delta_J,\Delta_A,\Delta_N)
=\left(0,\frac{3\delta-3}{2},
              \frac{-9+\delta}{9},\frac{-1-3\delta}{14}\right),
\quad \Delta=Y_T-Y_S.}
\tag{79}
$$

### 11.2 同时保三观察的旋转只有共同相位

在 (78) 中令四个真实相位独立变化：
$$
F_{\boldsymbol\zeta}
=2\zeta_K K-\frac{5+\omega}{2}\zeta_JJ
 +2(1+\omega)\zeta_AA_9
 +\frac{1-\omega}{2}\zeta_NN_{14},
\qquad \zeta_R\in\mu_6.
\tag{80}
$$
所有这些行都与 Y、H 正交，范数仍为81。
但是与两个旧观察正交是另一个必须实际满足的条件。
由 (79) 的全部项，准确有
$$
\boxed{
\langle F_{\boldsymbol\zeta},Y_T-Y_S\rangle
=\frac{3+5\delta}{2}
       (3\zeta_J-4\zeta_A+\zeta_N).}
\tag{81}
$$
系数 $3+5\delta$ 非零。若 (81) 为零，
则复嵌入下
$$
4=|4\zeta_A|=|3\zeta_J+\zeta_N|\le3+1=4.
$$
三角不等式的等号迫两个非零复数同向，故
$$
\zeta_J=\zeta_N=\zeta_A=:\zeta.
$$
此时 (80) 等于
$\zeta F+2(\zeta_K-\zeta)K$。
原 $F\perp Y_S$，而
$\langle K,Y_S\rangle=2\delta$，所以
$$
\boxed{
\langle F_{\boldsymbol\zeta},Y_S\rangle
=4\delta(\zeta_K-\zeta).}
\tag{82}
$$
因此有准确的充要条件
$$
\boxed{
F_{\boldsymbol\zeta}\perp Y_S,Y_T,Y
\quad\Longleftrightarrow\quad
\zeta_K=\zeta_J=\zeta_A=\zeta_N.}
\tag{83}
$$
充分性由原 $F\perp Y_S,Y_T,Y$ 直接给出。
这是固定 CM 系数上的完整结论，未用有限素数扫描；
当前好位均可使用其特征零整关系。

若再让 H 旋转，它只是给原 $C=2\omega H$ 加一个独立相位；
同时保三观察的平面仍然是原 $C,F$ 平面。
除去共同相位后，只有原相对六次相位的分支，
没有产生1296个新的共同三观察 carry。

### 11.3 对全部测试的实际限制

§10(77) 对第一轴 Y 及任意完整伴随测试的有限平均仍完全成立。
(83) 不削弱该身份。
它排除的是另一种未经证明的使用方式：
将 (76) 的1296个相对旋转分支逐一当成保
$Y_S,Y_T,Y$ 的 R1042 原 carry，并分别赋三个 canonical 中央零。

非共同相位的分支必须携带真实改变后的
$Y_S,Y_T$、原 unit cut、logarithm 和余权。
只有原来源上的完整转置，或对这些实际新观察另付完整算术来源，
才能消费它们；范数仍为81本身不完成这一步。

## 12. 未投影 K/A 的完整两态与非零质量参考源

本节只在 H/J/N 三个方向作已经支付的主型投影，
保留 K 与 $A_9$ 的全部实际混合项。
在第一轴使用主型读者时，原整个来源准确只剩两个固定的 K/A 张量。
第二个张量的系数来源具有单位质量；它不能被赋予算术中央零。
这个两态结论给出一个完整的条件测度关系，及两个真正的六阶返回权。

### 12.1 三个伴随投影后的原完整函数

以下简记 $A=A_9$、$N=N_{14}$，生成变量分别写为
$(z,h,k,j,a,n)$，与物理输出 $(Y,H,K,J,A,N)$ 对应。
置
$$
\mathscr P_3=\Pi_{H,0}\Pi_{J,0}\Pi_{N,0}.
$$
N 的单重性只用 J 的投影，见 (68)–(72)，并不需要先投影 K/A。
故沿 §8 的原 U/V/Q 加法身份，整个返回准确为
$$
\boxed{
\mathscr P_3\mathcal B
=B_3(h)\Theta(j)\Theta_{14}(n)\,\mathcal C(z,k,a),}
\tag{84}
$$
其中
$$
\boxed{
\begin{aligned}
\mathcal C(z,k,a)=-\frac1{84}\,
 &\sigma\bigl(\delta(3z+k)\bigr)
 \sigma\bigl(\delta(2z-a)\bigr)^2\\
 {}\cdot\bigl\{&
 \sigma(3z-k)^3 B_3(4z+a)
 +B_3(3z-k)\sigma(4z+a)^3\bigr\}.
\end{aligned}}
\tag{85}
$$
这里 $\sigma(w)^3$ 始终是原 sigma 的三次幂，
不是 $\sigma(3w)$。所有系数使用原 $\rho=-\nu_\sigma^{\otimes6}/84$；
没有为 (85) 重新归一化测度。

为核 (85)，在 §8 的 U/V/Q 对偶变量中代入
$$
u=3z+2n/\delta,\qquad
v=4z+a-2n/\delta,\qquad
q=2z-a-n/\delta.
$$
先保 H/J 的完整两个加法项，再用 N 的质量一单重因子，
置 $n=0$ 即得 (85)。
所以此处置 $n=0$ 是已经付清的整因子提取，而不是删除 N 的 mixed 条件。

(54)、(66) 给出的 Y/K/A 三个完整 $\delta$-new 身份仍成立。
此外有一个实际原整数 gluing：
$$
\boxed{
K+A=\delta(0,1,-1,1,-1,-1),\qquad
\mathsf T_{K,u}\mathsf T_{A,u}\mathcal C
=\epsilon(u)\mathcal C\quad(u\in\ker\delta).}
\tag{86}
$$
右侧 quotient 范数为5，是 odd；$\epsilon$ 正是 (49) 的原符号。
将原六 sigma 准周期式逐坐标代入，和 (53) 完全相同地消掉
Weyl 指数，余下五个非零模二系数给 (86)。
不能将此式的 $\epsilon$ 改成1。

### 12.2 全标准空间中的四个候选张量

现在只在 Y 上取 $\mu_6$ 主型：
$$
\mathcal C_0=\Pi_{Y,0}\mathcal C.
$$
原 $\mathcal C$ 对三个变量同时乘 $\mu_6$ 为主型，
所以 $\mathcal C_0$ 在 K/A 上的总型也为0。
这不等于对 K 与 A 分别取主型。

standard even $\mathcal S_6$ 的完整基为
$\sigma^6\langle1,x,y,x^2,xy,X\rangle$。
其 $\delta$-old 像是
$\sigma(\delta k)^2$ 与 $\Theta(\delta k)$ 两条，类型为2和0。
因此 K 的完整 new 部分及其类型准确是
$$
\begin{array}{c|cccc}
\text{型}&0&1&3&4\\ \hline
\text{来源}&F_6^-&xy\sigma^6&y\sigma^6&x\sigma^6 .
\end{array}
\tag{87}
$$
这里 $F_6^-=(X-2b)\sigma^6$ 的完整 new 身份已在 §8 支付。

standard odd $\mathcal S_9$ 的完整 $\delta$-new 部分每种
$\mu_6$ 类型各一维。与 (87) 配成总型0的四条分别是
$$
\begin{array}{c|cccc}
\text{型}&0&5&3&2\\ \hline
\text{来源}&\Theta_9&x^2\sigma^9&(X+4b)\sigma^9&x^2y\sigma^9 .
\end{array}
\tag{88}
$$
类型2、5在 old 空间没有竞争列。
类型0由 (67) 给出。
类型3的 old 列为 $\sigma(\delta a)^3=-3\delta X\sigma^9$；
原加法公式还给
$$
\sum_{u\in\ker\delta}\frac1{X(P+u)}=-\frac3{4b}.
$$
将真正 old 因子 $\sigma(\delta a)^3$ 提出加权 trace，
即证 $(X+4b)\sigma^9$ 为 new。它与 old 列独立，
所以 (88) 并未留下未检查的额外类型3分量。

依次定义整个双变量来源
$$
\begin{aligned}
E_0(k,a)&=F_6^-(k)\Theta_9(a),\\
E_1(k,a)&=(xy\sigma^6)(k)(x^2\sigma^9)(a),\\
E_3(k,a)&=(y\sigma^6)(k)((X+4b)\sigma^9)(a),\\
E_4(k,a)&=(x\sigma^6)(k)(x^2y\sigma^9)(a).
\end{aligned}
\tag{89}
$$
(87)–(88) 说明 $\mathcal C_0$ 的每个 Y 系数都落在这四个张量的全空间；
不是只由四个首阶猜测张成。

### 12.3 原 joint gluing 恰好只留下两态

写一个一般元素为
$c_0E_0+c_1E_1+c_3E_3+c_4E_4$。
它除以真正 old 因子
$$
O(k,a)=\sigma(\delta k)^2\sigma(\delta a)^3
=9\delta\,x_k^2X_a\,\sigma(k)^6\sigma(a)^9
$$
后，(86) 等价于对 $(k,a)\mapsto(k+S,a+S)$ 的不变性，
其中 $S=(0,\sqrt b)$。
这是因为 O 的目标 degree 为 $2+3=5$，恰有同一个 $\epsilon$；
没有在取商时丢掉半特征。

去掉共同 $9\delta$ 后，这个实际有理函数为
$$
\frac{X_a+4b}{x_k^2X_a}
 \{-c_0(X_k-2b)y_a+c_3y_k\}
+\frac{c_1y_k+c_4y_a}{x_kx_a}.
\tag{90}
$$
用 (67) 的原加法公式，连同
$$
y(P+S)=\sqrt b\,\frac{y(P)-3\sqrt b}{y(P)+\sqrt b},
$$
先比较 $a=O$ 处的 $a^{-3}$ 项，得 $c_3=6bc_0$；
再比较 $k=O$ 处的 $k^{-1}$ 项，得 $c_4=-c_1$。
后一次比较中 (90) 第一项只有 $k^{-2}$ 后接 $k^1$，
没有可吸收该条件的 $k^{-1}$ 项。

这两个条件也充分。对 $E_1-E_4$，
相应有理因子为 $(y_k-y_a)/(x_kx_a)$，
直接代入两个加法式即保持不变。
对 $E_0+6bE_3$，置 $r=y_k/\sqrt b$、$t=y_a/\sqrt b$。
除固定常数外，其因子为
$$
\frac1{x_k^2}\frac{t^2+3}{t^2-1}
       \{-(r^2-3)t+6r\}.
$$
同时作 $r\mapsto(r-3)/(r+1)$、$t\mapsto(t-3)/(t+1)$ 时，
三个因子的倍率依次为
$(r+1)^2/4$、$-(t+1)/2$、
$-8/((r+1)^2(t+1))$，乘积恰为1。
因此完整允许空间准确为
$$
\boxed{
\Xi_0=E_0+6bE_3,\qquad
\Xi_1=E_1-E_4.}
\tag{91}
$$
特别
$$
\Xi_0(0,0)=1,\qquad \Xi_1(0,0)=0,\qquad
\Xi_1=-ka^5+k^4a^2+\text{更高总次数}.
$$

### 12.4 固定第二来源的绝对质量与整周期

(91) 对每个 Y 系数成立。
在 $k=a=0$ 取完整边际，原 R1038 来源给第一系数
$39\delta\Phi_{126,b}$。
故存在唯一固定来源 $G_{126,b}$ 使
$$
\boxed{
\mathcal C_0(z,k,a)=
39\delta\,\Phi_{126,b}(z)\Xi_0(k,a)
+G_{126,b}(z)\Xi_1(k,a).}
\tag{92}
$$
它是原 standard even、主型、$\delta$-new 的 degree126 整 theta 来源；
此处不为它指定椭圆曲线或新的算术零。

其绝对规范无需数值提取。
由 (85)，
$$
\mathcal C(0,k,a)
=-\frac1{84}\sigma(\delta k)
 \{-\sigma(k)^3B_3(a)+B_3(k)\sigma(a)^3\}
 \sigma(\delta a)^2.
$$
总次数6的原首项准确为
$\delta(ka^5-k^4a^2)/28$。
结合 (91) 得
$$
\boxed{G_{126,b}(0)=-\frac{\delta}{28}.}
\tag{93}
$$
这个质量在所有当前好位均为单位。

所有来源使用同一个原普通单位周期 $\Omega$。
更具体地，G 的整个测度可在原输入上直接定义为
$$
\boxed{
\nu_G=-\frac1{120\Omega^6}\,
Y_*\bigl(KA^5\,\mathscr P_3\rho\bigr).}
\tag{94}
$$
因为 $KA^5$ 的总次数为6，原 simultaneous 主型已经使
这个 Y 返回为主型；在 (94) 再写 $\Pi_{Y,0}$ 也不改变它。
$120\Omega^6$ 在 $p>211$ 为单位，
所以 (94) 支付固定 p-adic 整格与有界性，并未任取一个复周期。

(89) 的各个双变量因子也是真有界来源。
例如
$$
xy\sigma^6=-\Theta B_3\sigma,\quad
y\sigma^6=-B_3\sigma^3,\quad
x\sigma^6=\Theta\sigma^4,\quad
x^2\sigma^9=\Theta^2\sigma^5,
$$
$$
(X+4b)\sigma^9=\Theta(\delta z)\sigma^3,\qquad
x^2y\sigma^9=-\Theta^2B_3\sigma^2.
$$
这些都是已付原有界测度的完整卷积；
其用途仅是给 (91) 的张量测度与整周期，不传播中央乘积零。

### 12.5 原 ray 上 G 的整个 ordinary 核与单位质量

这里需要支付 degree126 的完整核心，不能只由 (93) 推单位部分非零。
原 R531(13) 已明确固定
$$
g_\pi\equiv27+8\omega\pmod{64},\qquad
g_\pi\equiv1\pmod{27\cdot7\cdot13}.
$$
特别原 ray 确实含模7条件。
由模4为3、模63为1，CRT 准确给
$$
\boxed{g_\pi\equiv127=1+126\pmod{252}.}
\tag{95}
$$
所以无需偷偷增加一个尚未支付相容性的射线条件。

R471 与 R531 §2 已付原 $\Theta=x\sigma^2$ 的 whole 核
$\beta=-\lambda$，不是由解析奇偶猜其正负。
用原 CM 拉回
$\Theta(3\gamma z)$，其 degree 准确为
$2N(3\gamma)=2\cdot63=126$，半特征为 standard even。
这个非零锚与原 ordinary 核交换。
(95) 的完整 Heisenberg scalar 条件因而将原 standard even
$\mathcal S_{126}$ 的核心锁定为同一个 $\beta$。
G 的全部有限系数属于这个空间，遂有
$$
\nu_G|_{p\mathcal O}
=\beta[\kappa]_*\nu_G,\qquad
\boxed{
J_G(0)=(1-\beta)G(0)
=-\frac{\delta(1+\lambda)}{28}\in\mathcal O^\times.}
\tag{96}
$$
$1+\lambda$ 的单位性沿原 R410 保持。
这里的 $\kappa=p\lambda^2$、$\Omega$、单位域都未更换。

若采用原归一化观察 $Y/7$，
$$
J_{G,7}(v)=\langle7\rangle^{-dv}J_G(v),\qquad
\boxed{
j_{G,7}=J'_G(0)-d\log\langle7\rangle J_G(0).}
\tag{97}
$$
G 的质量非零，(97) 的第二项必须保留；
不能沿 $\Phi_{126}$ 的质量零结论删掉它。

### 12.6 对完整 companion-only mixed 域的真实两态读者

令 $\mathbf c=(H,J,N,K,A)$。
对其任意连续有界测试 h，令 $\mathscr A_3h$ 为 H/J/N
三个原物理主型平均，其矩阵仍是 (76) 的相应三因子。
定义
$$
\Lambda_i(h)=
\int h\,d\bigl(\nu_{B_3}\otimes\nu_\Theta\otimes\nu_{\Theta_{14}}
                   \otimes\nu_{\Xi_i}\bigr),\qquad i=0,1.
$$
这些测试可含全部五伴随之间的任意 unit/depth 条件；
K/A 不必分别主型，也不必独立。
由于 $d=p-1$ 是6的倍数，
$1_{Y\ {\rm unit}}\langle Y\rangle^{dv}$ 本身为 Y 主型。
只动 Y 的 $\Pi_{Y,0}$ 固定全部伴随，故可准确应用 (92)，得到
$$
\boxed{
\int_{Y\ {\rm unit}}\langle Y\rangle^{dv}
       \mathscr A_3h(\mathbf c)\,d\rho
=39\delta J_{126,b}(v)\Lambda_0(h)+J_G(v)\Lambda_1(h).}
\tag{98}
$$
若 h 已分别对 H/J/N 的 $\mu_6$ 不变，则无需再平均。
这说明 Y 主型投影的合法顺序；它不要求将 K/A 的混合测试
偷换成两个分别主型测试。

设原 E3969 坏 Sha 假设给已付的 $J'_{126,b}(0)=0$。
又 $J_{126,b}(0)=0$，所以 (98) 的整个条件质量和中央测度满足
$$
\boxed{
\begin{aligned}
\mathcal M(h)&=J_G(0)\Lambda_1(h),\\
\mathcal L(h)&=J'_G(0)\Lambda_1(h),\\
\mathcal L(h)&=\frac{J'_G(0)}{J_G(0)}\mathcal M(h).
\end{aligned}}
\tag{99}
$$
采用 $Y/7$ 时，最后的比例准确改成
$J'_G(0)/J_G(0)-d\log\langle7\rangle$。
这是整个实际 companion 条件测度的线性约束，
不是把未识别的 $J'_G(0)$ 设成零。

(98)–(99) 不把含 Y 的原五深网格认作 companion-only 条件，
也不把 $Y_S,Y_T$ 的真实 logarithm 改成 $\log Y$。
这些额外域必须按原整框架另外运输。
但对确在本节范围内的任意两个测试，
它已经给出准确的交叉关系
$\mathcal L(h_1)\mathcal M(h_2)-\mathcal L(h_2)\mathcal M(h_1)=0$，
无需预知参考中央的数值。

### 12.7 两个真正的六阶交叉返回权

从 (91) 的各自型和首项，整系数准确为
$$
[ka^5]\Xi_1=-1,\qquad [k^4a^2]\Xi_1=1,\qquad
[k^3a^3]\Xi_0=-6b,
$$
其他对应态的这些系数为零。
令 $\pi_4=(Y,H,J,N)$，并记
$\nu_{\rm comp}=\nu_{B_3}\otimes\nu_\Theta\otimes\nu_{\Theta_{14}}$。
包含全部 factorial 和原 $\Omega$ 后，真正四输出测度身份为
$$
\boxed{
\begin{aligned}
(\pi_4)_*(KA^5\,\mathscr P_3\rho)
 &=-120\Omega^6\,\nu_G\otimes\nu_{\rm comp},\\
(\pi_4)_*(K^4A^2\,\mathscr P_3\rho)
 &=48\Omega^6\,\nu_G\otimes\nu_{\rm comp},\\
(\pi_4)_*(K^3A^3\,\mathscr P_3\rho)
 &=-216b\Omega^6\cdot39\delta\,
                  \nu_{\Phi_{126,b}}\otimes\nu_{\rm comp}.
\end{aligned}}
\tag{100}
$$
所以原正次数测试
$$
\boxed{
(\pi_4)_*\bigl((2KA^5+5K^4A^2)\mathscr P_3\rho\bigr)=0}
\tag{101}
$$
是一个完整来源零核，不用任何算术坏假设；
$K^3A^3$ 则是准确返回原 canonical 来源的交叉权。
(100)–(101) 保任意真正四输出条件，
没有将 K/A 自身的其他 cut 免费留在忘去 K/A 的等式里。
这些实际权及 (99) 的单位质量比例，是本节给后续 mixed 补域的新增输入。

## 13. norm5/norm90 的两条完整伴随管及精确质量消组合

本节把 (100) 的有限矩推进为带完整 unit/depth 域的来源返回。
所用域只读真正伴随；不把 R1042 §9 中还含 Y 的两单位管改成这里的域。
所有等式保原四个输出 $(Y,H,J,N)$。

### 13.1 原整数正交二轴与两个实际 whole 核

在 K/A 平面置
$$
\boxed{
\begin{aligned}
D&=(K+A)/\delta=(0,1,-1,1,-1,-1),\\
E&=3K-2A=(-5,\omega-2,-3-\omega,3\delta,2\delta,2\delta),\\
K&=(E+2\delta D)/5,\qquad A=(3\delta D-E)/5 .
\end{aligned}}
\tag{102}
$$
它们的 Hermitian 范数为5、90，内积为零；也分别正交于 Y/H/J/N。
变换 determinant 为 $-5/\delta$，所以在当前好位是整自同构。
D 的五个非零模二系数给 standard odd；
E 的四个非零模二系数给 standard even，均保原 Gaussian。

R551(7) 的整个 odd $\mathcal S_5$ 核已经准确锁定为
$u_5=\chi_{65}\lambda$，不是只沿其中一条主型线。
原 ray 的 $g_\pi\equiv1\bmod(27\cdot5)$、
$g_\pi\equiv3\bmod4$ 给 $g_\pi\equiv91\bmod180$，
所以 standard even $\mathcal S_{90}$ 的 whole 交织为 scalar。
用 R968 已付 even $\mathcal S_{10}$ 的非零 $[3]$ 拉回作绝对锚，
得其实际标量为 $u_{90}=\chi_{10}\lambda$。这里两个 $\chi$ 均保留，
没有假定它们相等。因此在原完整六变量来源上
$$
\boxed{
\rho|_{D\in p^n\mathcal O}
=u_5^n(P_{D,\kappa^n})_*\rho,\qquad
\rho|_{E\in p\mathcal O}
=u_{90}(P_{E,\kappa})_*\rho.}
\tag{103}
$$
两个原物理缩放都保 Y/H/J/N，并相互交换；
它们也与 $\mathscr P_3$ 交换。
这是将 whole theta 核作用于完整系数空间，不是把 D/E 当作独立边际。

### 13.2 两态的完整六阶返回系数

若 d/e 是 D/E 的生成变量，则原 K/A 变量准确为
$k=d/\delta+3e,\ a=d/\delta-2e$。
令 $q=d/\delta$。由 (89)–(91)，两态总六阶部分为
$$
\boxed{
\begin{aligned}
[\Xi_0]_6
 &=b\left\{-\frac{12}{5}k^6+\frac{39}{10}a^6-6k^3a^3\right\},\\
[\Xi_1]_6
 &=k^4a^2-ka^5\\
 &=15q^5e-100q^3e^3+25q^2e^4-100qe^5+420e^6 .
\end{aligned}}
\tag{104}
$$
第一式各项分别来自 $F_6^-$、$\Theta_9$ 及 $6bE_3$；
第二式直接由两个不同类型的原首项相减。
包含每个变量的 factorial 后，全部七个六阶矩是
$$
\boxed{
\begin{array}{c|rr}
\text{权}&\Xi_0\text{ 的矩}/\Omega^6&
             \Xi_1\text{ 的矩}/\Omega^6\\ \hline
D^6&120b&0\\
D^5E&480\delta b&-200\delta/3\\
D^4E^2&0&0\\
D^3E^3&-6840\delta b&-400\delta\\
D^2E^4&40320b&-400\\
DE^5&195840\delta b&4000\delta\\
E^6&-146880b&302400
\end{array}}
\tag{105}
$$
这些是原整个两态的矩；没有遗漏高阶函数对该固定矩的贡献，
因为一个六阶 Taylor 系数只读 (104)。
尤其 $D^4$ 型在整个 odd $\mathcal S_5$ 中缺席，与表中两零相合。

### 13.3 两个完整管测试的实际返回

对 $n\ge1$，取真正紧开域
$$
\Gamma_n^{5,90}=\{D\in p^n\mathcal O,\ E\in\mathcal O^\times\}.
$$
在域外将下列函数延为零：
$$
\boxed{
\begin{aligned}
t_{1,n}&=\frac{{\bf1}_{\Gamma_n^{5,90}}}{\Omega^6}
       \frac{(D/\kappa^n)E^5}{1-u_{90}\kappa^5},\\
t_{2,n}&=\frac{{\bf1}_{\Gamma_n^{5,90}}}{\Omega^6}
       \frac{(D/\kappa^n)^2E^4}{1-u_{90}\kappa^4}.
\end{aligned}}
\tag{106}
$$
在此域 $D/\kappa^n$ 整，两个分母模 p 都为1，故都是实际整有界测试。
先用 (103) 的 D 核，再减去 E 的深部分，
恰分别产生 $u_5^n(1-u_{90}\kappa^5)$、
$u_5^n(1-u_{90}\kappa^4)$。这些正是 (106) 已保留的分母。
令 $\pi_4=(Y,H,J,N)$，并沿 (100) 记 $\nu_{\rm comp}$，于是
$$
\boxed{
\begin{aligned}
(\pi_4)_*(t_{1,n}\mathscr P_3\rho)
 &=u_5^n\{195840\delta b\cdot39\delta\,\nu_\Phi
                       +4000\delta\,\nu_G\}\otimes\nu_{\rm comp},\\
(\pi_4)_*(t_{2,n}\mathscr P_3\rho)
 &=u_5^n\{40320b\cdot39\delta\,\nu_\Phi
                       -400\,\nu_G\}\otimes\nu_{\rm comp}.
\end{aligned}}
\tag{107}
$$
这是整个四输出测度身份，因而可保任意真正四输出 mixed 测试。
D/E 的域已被完整消费，不能再在右侧免费保一个额外 D/E 条件。

这里不用额外投影 Y：两权的总次数为6，域在 D/E 同时乘
$\mu_6$ 下不变；H/J/N 已主型，故返回的 Y 来源本身主型。
因此 (92) 的两态分解准确覆盖整个 (107)，不只覆盖一类测试的积分。

### 13.4 单位行列式、canonical 纯返回与参考纯返回

两行的系数行列式准确是
$-239616000\delta b=-400\cdot599040\delta b$。
其中 $599040=2^{10}3^2\cdot5\cdot13$，
故在当前好位连同 $b=17$ 均为单位。定义
$$
\boxed{
\begin{aligned}
h_{\Phi,n}&=\frac{t_{1,n}+10\delta t_{2,n}}
                         {599040\delta b},\\
h_{G,n}&=\frac{40320t_{1,n}-195840\delta t_{2,n}}
                         {239616000\delta}.
\end{aligned}}
\tag{108}
$$
完整消去 (107) 的另一态，得到
$$
\boxed{
\begin{aligned}
(\pi_4)_*(h_{\Phi,n}\mathscr P_3\rho)
 &=39\delta\,u_5^n\,\nu_\Phi\otimes\nu_{\rm comp},\\
(\pi_4)_*(h_{G,n}\mathscr P_3\rho)
 &=u_5^n\,\nu_G\otimes\nu_{\rm comp}.
\end{aligned}}
\tag{109}
$$
所以这里的质量消组合是在一条完整管上逐测度成立，
不是仅抵消两条五深网格的首项。

若只读 Y 中央，可将 $\mathscr P_3$ 移到测试端：
D/E 全正交于 H/J/N，故 (106)–(108) 的域和权被这三个平均固定。
于是 (109) 给原未投影 $\rho$ 上的合法整测试。
特别在原 E3969 坏中央假设下，
$$
\boxed{
\begin{aligned}
\int_{Y\ {\rm unit}}d\log\langle Y\rangle\,h_{\Phi,n}\,d\rho&=0,\\
\int_{Y\ {\rm unit}}h_{G,n}\,d\rho&=u_5^nJ_G(0),\\
\int_{Y\ {\rm unit}}d\log\langle Y\rangle\,h_{G,n}\,d\rho&=u_5^nJ'_G(0).
\end{aligned}}
\tag{110}
$$
采用 Y/7 时，最后一式仍须减去 (97) 的准确质量费用。
这些是所有 n 的完整返回；共同因子 $u_5^n$ 本身不产生新的
关于 n 的不相容条件。其真正用途是给 (99) 两个可明确控制、
覆盖完整 companion-only 域的独立整测试，并将 canonical 与
非零质量参考逐项分开。原 S/T mixed logarithm 及含 Y 的补管
仍按它们的真实域消费，没有在本节被赋予额外中央零。
