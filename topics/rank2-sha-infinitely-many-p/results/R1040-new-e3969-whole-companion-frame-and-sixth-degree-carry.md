# R1040 — E3969 真六轴的完整小伴随框架与单项六次 carry

日期：2026-11-27。**状态：以下整框架、完整 H/J 纤维分解、单项六次返回、两个实际 whole 核、四输出 carry 及完整 K 主型三输出返回均已证明。** 来源是 R1038 §§10–14 已完全识别的固定 rank2 曲线 E3969。先保留另外三个伴随输出，再准确分离 K 主型；其余 mixed 条件及全部单位补域保持；本篇不宣称主问题已完成。

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
$
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


## 依赖

- R1038 §§10–14：E3969 的完整有限来源、通常全 Sha 桥、原126完整回乘、确切六 sigma 及 rank2 锚。
- [R522](R522-common-degree3-even-factor-and-same-st-positive-test.md)：原 odd degree3 完整偶纤维与普通周期规范。
- [R551](R551-original-norm5-two-state-core-and-complete-unit-inverse.md)：whole odd degree5 的真实 $\chi_{65}$ 和完整深限制。
- [R968](R968-original-common-degree10-carry-and-positive-eighth-order-difference.md)：原普通 ray、whole even degree10 的绝对 $\chi_{10}$ 及保全输出的 carry 规则。

本篇未运行新的数学数值计算。所有新显示恒等式均由原完整 sigma、有限维 theta 空间与已付 whole 核逐式证明；没有加入新的中央零或删除完整 mixed 补域。
