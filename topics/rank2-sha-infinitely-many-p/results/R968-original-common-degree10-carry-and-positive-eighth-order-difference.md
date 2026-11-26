# R968 — 同一全观察的 degree10/210 carry 与原正矩给出的八阶差

日期：2026-11-26。**状态：以下整个 theta 核、共同 carry、十二次完整纤维返回及原实际网格上的非零归一差均已证明。** 所用来源仍是原六 sigma；没有新增曲线、换普通射线或使用负矩非零假设。原补域保留，主目标尚未完成。

R536 的旧 carry 保 $(Y,W,W',G)$，并不同时保新 $W^\pm,Z$。这里改用纯前四的共同伴随，整 theta degree 为10、210；其完整核心带同一个真实符号 $\chi_{10}\in\{\pm1\}$，全程保留而不择号。一个十二次测试使危险的 $D^9E^3$ 系数准确为零，局部首差于是只读原 sigma 的正第一单位矩。

## 1. 原六输入、全部观察与新的共同平面

固定原普通 ray，沿 R410、R531 使用
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,\quad b=17,
$$
$$
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda,\qquad\kappa=p\lambda^2\in p\mathcal O^\times,\qquad d=p-1,
\quad \rho=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
这里是普通参数，绝不与 R943 惰性 $v_p(\kappa)=-1$ 的参数混用。
原输入为 $\xi=(\xi_1,\xi_2,\xi_3,x,c,d_0)^t$，置
$$
A=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma x.
$$
原观察为 $Y=A+c+2d_0$、$W=A+3\delta c+4d_0$；
R958/R961 的两条 $W^\pm$ 和 $Z$ 的真实轴也都属于
$A+a c+b'd_0$。其原尺度、投影和 period 仍按各篇，不因本式而改变。

沿 R522 的准确行取
$$
H_0=(1,0,-1,1,0,0),\qquad
H_1=(-1,2,\omega,1+\omega,0,0),
$$
$$
\boxed{
C=H_0/\delta,\qquad F=-\omega H_1/\delta,\qquad
r=7/3,\qquad D=F-C,\qquad E=F+rC.}
\tag{2}
$$
原 Gram 给
$$
C\perp F,\quad NC=1,\quad NF=r,\quad
D\perp E,\quad ND=10/3,\quad NE=70/9 .
\tag{3}
$$
$C,F$ 同时正交于所有 $A+a c+b'd_0$，也正交于 R522 的原 $W'$；
因为 $H_0,H_1$ 已同时正交于原 $Y,W,W'$，且不读 $c,d_0$。
因此这里确实保原 $S,T,W^\pm,Z$ 的实际观察和 $W'$。

可不用任意选取一个有理补基。令 $\pi$ 是完整正交投影
$$
\pi=I-\bar C^{\,t}C-\frac37\bar F^{\,t}F
\tag{4}
$$
到 $\ker C\cap\ker F$。在原好位它是整幂等，像为秩四自由直和项。
上述每条观察都满足 $L\pi=L$。
下文 $\pi_*$ 恒保这整个四输出，包括其任意 mixed 条件。

准确反解是
$$
C=\frac3{10}(E-D),\qquad
F=\frac3{10}(E+rD).
\tag{5}
$$
实际整行不是只看物理范数：
$$
\boxed{
\delta D=(\omega-1,-2\omega,1-\omega^2,0,0,0),}
$$
$$
\boxed{
3\delta E=(7+3\omega,-6\omega,-4+3\omega,10,0,0).}
\tag{6}
$$
它们的范数分别为10、210；各有恰两个模2非零的 CM 系数，
因此实际半特征都是标准 even。所有原伴随 Gaussian 交叉为零。
原 $C,F$ 则分别用整行 $H_0,-\omega H_1$ 的 odd degree3、7 覆盖。

## 2. 两个 whole 核及同一真实绝对符号

当前 ray 的准确 ratio 为 $g_\pi=\pi_0/\bar\pi_0$。
R410 的模5细化给 $g_\pi\equiv1\bmod5$；
R531(13) 给 $g_\pi\equiv27+8\omega\bmod64$ 及
$g_\pi\equiv1\bmod(27\cdot7\cdot13)$。于是
$$
g_\pi\equiv11\pmod{20},\qquad
g_\pi\equiv211\pmod{420}.
\tag{7}
$$
这不是把 $\pi_0$ 与 $g_\pi$ 混同。

标准 even $\mathcal S_N$ 的两个完整 canonical Heisenberg 生成元
的 $N$ 次幂均为一。$g_\pi\equiv1+N\bmod2N$、$N$ 偶时，
两生成元及其中心都保持：$(1+N)^2\equiv1\bmod2N$。
故 Schur 引理使原归一 core 在整个 $\mathcal S_{10}$、
$\mathcal S_{210}$ 上均为 scalar，不只在 projective 商中为 scalar。

必须支付绝对标量。R551(7) 已付整个 odd $\mathcal S_5$ 的实际
core 为 $\chi_{65}\lambda$，其中真实 $\chi_{65}^2=1$。
取任意非零 $f,g\in\mathcal S_5$，把完整双变量来源拉回为
$$
f(u+v)g(u-v)\in
\mathcal S_{10}^{\rm even}\otimes\mathcal S_{10}^{\rm even}.
\tag{8}
$$
两个 odd 半特征相消，Gram 为 $\operatorname{diag}(10,10)$，
交叉严格为零。$p\ne2$ 时 $(u,v)\mapsto(u+v,u-v)$ 是原局部整自同构，
所以两个变量同时深的真实域准确相同。
若 degree10 的归一 scalar 记为 $\chi_{10}$，比较同一非零完整来源
的两种双深计算，得
$$
\lambda^2\chi_{10}^2=\lambda^2\chi_{65}^2,\qquad
\boxed{\chi_{10}\in\{1,-1\}.}
\tag{9}
$$
这不是把单变量乘积的 core 当作两个 core 的乘积；(8) 始终使用两个
独立变量及同一个完整双深域。

令 $\alpha=\delta\gamma$，$N\alpha=21$。
非零固定拉回 $[\alpha]^*\mathcal S_{10}\subset\mathcal S_{210}$
保持标准 even 特征。原 prime-to-$p$ 完整 CM 拉回与普通深限制交换，
所以它作绝对锚给
$$
\chi_{210}=\chi_{10}.
\tag{10}
$$
不需要猜测该真实符号在全部素数上是否相同。
以下固定
$$
\upsilon_p=\chi_{10}\lambda .
\tag{11}
$$
下文始终使用这个普通 core scalar。

对 $L=D,E$，令 $P_{L,t}=I+(t-1)\bar L^{\,t}L/NL$。
(6) 的固定单位覆盖回到原物理输入后，完整身份为
$$
\boxed{\rho|_{L\in p^n}=\upsilon_p^n(P_{L,\kappa^n})_*\rho.}
\tag{12}
$$
任意其余五输出、半特征和中心均保留。
$C,F$ 的 whole core 仍是已付的 $\beta$，但下文只需它们的真实纤维矩。

同一论证适用于沿 $C,F$ 保持上述 whole 格的完整来源，特别是
第一观察属于 $\pi$ 的原完整 CM 投影。原 R544 的 $H$ 只动
$(c,d_0)$，也不改变前四输入的这些 whole 空间。
不能把后来的 R965 $\mathscr D_{156}$ 当成保持 $C,F$；
它影响原前四输入，须另付其实际测试和覆盖。

## 3. 十二次 whole 纤维恒等式

R522 的完整 odd degree3 方向偶子空间只有
$$
B_3(z)=-y(z)\sigma(z)^3=\frac{\sigma(2z)}{2\sigma(z)}.
$$
从同一原曲线方程 $y^2=x^3+b$、$x'=2y$ 得
$$
x=z^{-2}-\frac b7z^4+\frac{b^2}{637}z^{10}+\cdots,
\quad
\log(\sigma/z)=\frac b{210}z^6-\frac{b^2}{84084}z^{12}+\cdots .
$$
所以
$$
B_3=1+\frac{3b}{10}z^6-\frac{57b^2}{15400}z^{12}+\cdots.
\tag{13}
$$
这是整个一维偶子空间的准确系数；用其余全部五输出作系数仍成立。
$C=H_0/\delta$、$\delta^{12}=729$ 给
$$
\boxed{
(\mathrm{forget}\ C)_*(C^{12}\rho)
=-2432\,b^2\Omega^{12}(\mathrm{forget}\ C)_*\rho,\qquad
(\mathrm{forget}\ C)_*(C^2\rho)=0.}
\tag{14}
$$
其中 $2432=128\cdot19$；原 $\Omega$ 为同一个普通单位周期。

取完全固定的齐次十二次多项式
$$
\boxed{
Q(C,F)=-\frac{C^{12}}{128\cdot19}
 +\frac{11\cdot3^9}{2^{11}\cdot19\cdot7^7}C^2F^{10}.}
\tag{15}
$$
$F$ 与 $C$ 正交，故 (14) 逐个完整 $F$ 系数适用，得到
$$
\boxed{
\pi_*\left(\frac{Q}{b^2\Omega^{12}}\rho\right)=\pi_*\rho .}
\tag{16}
$$
没有仅证明第一边际或有限若干矩相合。

按 (5) 定义所有准确系数 $q_k$：
$$
Q=\sum_{k=0}^{12}q_kD^kE^{12-k}
=\left(\frac3{10}\right)^{12}
\left[
-\frac{(E-D)^{12}}{128\cdot19}
+\frac{11\cdot3^9}{2^{11}\cdot19\cdot7^7}
 (E-D)^2(E+rD)^{10}
\right].
\tag{17}
$$
这里保全十三个系数，不删除未写出的项。
两个关键值由整式二项展开准确为
$$
\boxed{q_9=0,\qquad
q_3=\frac{3^{12}\cdot11\cdot1069}{2^{19}\cdot5^9\cdot7^6}\ne0.}
\tag{18}
$$
例如 $D^9E^3$ 的括号系数为
$55/608+a\,10r^7(r^2-9r+12)=0$，
$D^3E^9$ 的为 $55/608+a\,9520/9$，
$a=11\cdot3^9/(2^{11}\cdot19\cdot7^7)$。
(18) 是特征零恒等，不是模某个试验素数的取消。

## 4. 同一个 carry 保全部实际观察

对 $n\ge1$ 定义真实域
$$
\Gamma_n=\{D\in p^n,\ E\ {\rm unit}\}
=\{C,F\ {\rm unit},\ F-C\in p^n\}.
\tag{19}
$$
等价性用 (5) 和 $10/3$ 为单位逐点成立。
置
$$
\widehat Q_{n,p}=
\frac1{b^2\Omega^{12}}\sum_{k=0}^{12}
 \frac{q_k(D/\kappa^n)^kE^{12-k}}
      {1-\upsilon_p\kappa^{12-k}}\quad\text{于 }\Gamma_n.
\tag{20}
$$
域外延为零。所有系数整且有界。
正次数分母模 $p$ 为一；常数分母 $1-\upsilon_p$ 是单位，因为
$\upsilon_p=\pm\lambda$ 且 R410 已付 $1\pm\lambda$ 的单位性。

先以 (12) 的 $D$ 核还原 $D/\kappa^n$，保完整 $E,\pi$；
再以同一 $E$ 核计算每个真实 $E^j$ 的单位部分，
准确产生 $1-\upsilon_p\kappa^j$。逐项消去 (20) 的分母，最后用 (16)，得
$$
\boxed{\pi_*({\bf1}_{\Gamma_n}\widehat Q_{n,p}\rho)
              =\upsilon_p^n\pi_*\rho .}
\tag{21}
$$
这对 $\pi$ 上任意完整连续测试成立，保所有真正 mixed 紧开条件。
原 $Y,W,W^\pm,Z,W'$ 观察均未移动。

为保原 R522 三阶几何 $\mathcal T$，置
$$
\zeta_j=\omega^{2j},\qquad
D_j=F-\zeta_jC,\quad E_j=F+r\zeta_jC,\quad
\Gamma_{n,j}=\{D_j\in p^n,\ E_j\ {\rm unit}\}.
$$
$\delta D_j,3\delta E_j$ 仍有范数10、210和标准 even 半特征：
模2的三个非零原系数为 $1,\omega,\omega^2$，减去 $\zeta_j$
恰消掉一个，留下两个。故 (12) 对全部三支用同一个 $\upsilon_p$。
令 $\widehat Q_{n,p}^{(j)}$ 为 (20) 的对应式，定义
$$
\boxed{
\mathfrak q_{n,p}^{\,\mathrm{new}}
=\frac13\sum_{j=0}^2
 {\bf1}_{\Gamma_{n,j}}\widehat Q_{n,p}^{(j)}.}
\tag{22}
$$
三支互不相交，其并集恰为
$\{C,F\ {\rm unit},\,F^3-C^3\in p^n\}$。
R522(8) 给 $C\mathcal T=\omega^2C,F\mathcal T=F$，
所以
$$
\boxed{
\mathfrak q_{n,p}^{\,\mathrm{new}}\circ\mathcal T
=\mathfrak q_{n,p}^{\,\mathrm{new}},\qquad
\pi_*(\mathfrak q_{n,p}^{\,\mathrm{new}}\rho)=\upsilon_p^n\pi_*\rho .}
\tag{23}
$$
十二次齐次也使它在六输入同时乘 $\mu_6$ 下不变。
它是新完整测试，不与 R536 的旧 $\mathfrak q$ 偷换。

## 5. 原五深一单位网格、零质量和完整首差

仍取原网格
$$
\mathcal D_n=
\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n,\ x\ {\rm unit}\}.
\tag{24}
$$
(6) 的 $D$ 不读 $x$，并且
$C\equiv F\equiv x/\delta$、$E\equiv10x/(3\delta)\bmod p^n$。
所以 $\mathcal D_n\subset\Gamma_{n,0}$，
另外两支在这里为空；$Y,W$ 为单位。
R522 的同一个 $W'$ 在此仍深。
在 (24) 上，(22) 准确为 $\widehat Q_{n,p}/3$。

测试及 carry 只读前四输入，$c,d_0$ 的两个深 sigma 质量各自为零。
因此整个加权质量、全部固定尺度 log 和 $\log\langle x\rangle$ 贡献
都严格为零，不能只说它们模 $p$ 为零。

令五个深输入共同缩放为 $T$，暂不包含 (22) 的 $1/3$。
写
$$
D=T D_f,\qquad E=e_0x+T E_f,\qquad
e_0=\frac{10}{3\delta},\qquad
A_T=\bar\gamma x+T(\delta\xi_1+2\delta\xi_2+\gamma\xi_3),
$$
$$
D_f=\frac{(\omega-1)\xi_1-2\omega\xi_2+(1-\omega^2)\xi_3}{\delta}.
\tag{25}
$$
当 $T=\kappa^n$，(20) 的 $D/\kappa^n$ 正是 $D_f$，并没有移动原 $x$。
定义整个真实解析函数
$$
\mathcal A(T)=\frac{d}{b^2\Omega^{12}}
 \int_{x\ {\rm unit}}\int
 \left\{\frac1{6\delta}\log\langle A_T+T(3\delta c+4d_0)\rangle
              -\log\langle A_T+T(c+2d_0)\rangle\right\}
 \sum_{k=0}^{12}
 \frac{q_kD_f^k(e_0x+TE_f)^{12-k}}
      {1-\upsilon_p\kappa^{12-k}}\,d\rho .
\tag{26}
$$
分母中的 $\lambda,\kappa,\upsilon_p$ 固定，不随 $T$ 变化。
所有实际输入域及原 $-1/84$ 都在 (26) 中。
原五个 sigma 的 core 于是给准确局部差
$$
\Delta_n:=
\int_{\mathcal D_n}
 d\left(\frac{\log\langle W\rangle}{6\delta}
               -\log\langle Y\rangle\right)
 \mathfrak q_{n,p}^{\,\mathrm{new}}\,d\rho
=\frac{\beta^{5n}}3\mathcal A(\kappa^n).
\tag{27}
$$

### 5.1 第八阶以前为何完整相消

原 sigma 只在 $1\bmod6$ 的次数有矩。
因此先固定所有前四输入，对最后两个独立 sigma 作积分，
总次数小于八时只可能读 $(c,d_0)$ 的 $(1,1)$ 矩。
它的系数正比于两个线性系数之积；
$W$ 的乘积为 $12\delta$，除 $6\delta$ 后恰为 $Y$ 的乘积2。
所以这部分作为 $A_T$ 的整个函数完全相消，所有
$[T^j]\mathcal A$、$j<8$ 都准确为零。
这包含测试自身的全部 $T$ 项，而非只比较裸 logarithm 的首项。

第八阶的新增矩只有 $(7,1)$、$(1,7)$。
$\nu_\sigma(x)=\Omega$、
$\nu_\sigma(x^7)=24b\Omega^7$，
故这两个原输入的归一差在 (26) 中准确给
$$
\frac{751296\,b\Omega^8}{(\bar\gamma x)^8}\,T^8 .
\tag{28}
$$
这里
$2\{(3\delta)^6+4^6-1-2^6\}=-31304$
和 logarithm 的负号都已保留。
第八阶用测试的 $T=0$ 项。

对其余三个深 sigma，$D_f^k$ 只在 $k\equiv3\bmod6$ 时可能非零。
$0\le k\le12$ 中只有3、9；(18) 把9准确杀掉，
因此没有引入原自由 $x$ 的负五次矩。
唯一剩余的是
$$
[\xi_1\xi_2\xi_3]D_f^3=-\frac{12\omega}{\delta},
\qquad
(e_0x)^9/(\bar\gamma x)^8
=\frac{e_0^9}{\bar\gamma^8}\,x .
\tag{29}
$$
故自由输入只读已付的**正第一单位矩**
$$
I_1=(1+\lambda\kappa)\Omega.
\tag{30}
$$
将 (18)、(28)–(30) 与原 $-1/84$ 全部代回，准确得到
$$
\boxed{
[T^8]\mathcal A
=-\frac db\,
 \frac{11\cdot13\cdot43\cdot1069\,\omega}
      {48\cdot7^6\bar\gamma^8}
 \frac{1+\lambda\kappa}{1-\upsilon_p\kappa^9}.}
\tag{31}
$$
所有 phase 和原 $b,\Omega$ 已回到 (1) 的规范。

### 5.2 全尾与每个深度的非零

在原好普通位 $p>211$、另删固定 $p\mid1069$ 后，(31) 是单位。
这里不把一个未知固定系数预认成单位；
新有限分子已完整显示。
原 ray 去掉有限素数仍无限。

(26) 的所有多项式系数和测度整，$x$ 是单位；
$A_T$ 在 $T\in p\mathcal O$ 为单位。
logarithm 第 $m$ 项只带通常分母 $m$，
故完整系数统一满足
$$
v_p([T^j]\mathcal A)\ge-\lfloor\log_p j\rfloor\quad(j\ge1).
\tag{32}
$$
对 $j>8,n\ge1,p>211$，
$jn-\lfloor\log_p j\rfloor>8n$。
于是 (27)、(31) 严格给
$$
\boxed{v_p(\Delta_n)=8n,\qquad \Delta_n\ne0
                    \quad\text{对每个 }n\ge1.}
\tag{33}
$$
既没有用负矩的模 $p$ 非零猜测，也没有只给某个有限 $n$ 的验证。

## 6. 进入原 h 的 W 深管，原测试保持不动

仅在本节记 $h_{\mathcal T}=\omega^2\mathcal T_*\rho$，
这是 R522 的原六维三阶来源，不与 R548 的另一个正两态名称混同。
置 $\mathcal E_n=\mathcal T\mathcal D_n$。
原 $Y\mathcal T=Y$、$W\mathcal T=W'$、
$W_2=W\mathcal T^2$、$\mathcal T^3=I$ 和 (23) 给
$$
\boxed{
\int_{\mathcal E_n}
 d\left(\frac{\log\langle W_2\rangle}{6\delta}
           -\log\langle Y\rangle\right)
 \mathfrak q_{n,p}^{\,\mathrm{new}}\,dh_{\mathcal T}
=\omega^2\Delta_n .}
\tag{34}
$$
在这个实际域中，$W\in p^n$、$Y,W_2$ 为单位；
全部原条件仍是 $(\mathcal T^{-1}\xi)_i\in p^n$（$i\ne x$）及
$(\mathcal T^{-1}\xi)_x$ 单位。来源、测试和完整域一起运输。
(34) 的赋值仍为 $8n$，质量仍严格为零。

原 $W$ 核的物理缩放固定 $C,F$，所以也固定这里的新测试。
它仍会移动 $Y,W_2$，这些实际权和其单位条件不能删除。

## 7. 原算术行、CM 投影与准确剩余域

由 (23)，同一新测试上的整个原 S/T 行是
$$
\int_{Y\ {\rm unit}}\langle Y\rangle^{du}
 \mathfrak q_{n,p}^{\,\mathrm{new}}d\rho=\upsilon_p^nJ_S(u),\qquad
\int_{W\ {\rm unit}}\langle W\rangle^{du}
 \mathfrak q_{n,p}^{\,\mathrm{new}}d\rho=6\delta \upsilon_p^nJ_T(u).
\tag{35}
$$
若原两中央同时为零，精确补域身份为
$$
0=\Delta_n+
\int_{\Gamma_n^{(3)}\setminus\mathcal D_n}
 d\left(\frac{{\bf1}_{W\ {\rm unit}}\log\langle W\rangle}{6\delta}
          -{\bf1}_{Y\ {\rm unit}}\log\langle Y\rangle\right)
 \mathfrak q_{n,p}^{\,\mathrm{new}}\,d\rho .
\tag{36}
$$
两种不同的单位条件和整个补域都在此，未由 (33) 被消去。

新 $W^\pm,Z$ 的原第一轴同样属于 $\pi$，因此其完整 CM trace/pull
及真实有限 torsion 纤维逐个保持 $C,F$。
它们的已投影 whole 来源继续满足 (21)、(23)；
可以在相同新测试上使用各自的真正算术中央及其原归一。
但三条原 CM source projection 并不因此相同。
未投影 raw 边际的外谱不能被删除，两个不同 projection 的 mixed
单位切域也不能免费合并。

同理，R965 的 $\mathscr D_{156}$ 虽保这些第一轴，
却不保本篇 $C,F$，所以不能令它与 $\mathfrak q^{\rm new}$ 自由交换。
原 R544 只动最后两输入的 $H,P_j,R_c$ 则确实保持本篇测试；
在这些来源上仍须保它们对 $Y,W$ 的真实移动。
本篇支付的是新的共同 whole 核、同一四输出 carry 和 (33) 的
实际正矩非零差。继续在 (36) 及各原 CM 来源的完整 mixed 域内联立，
不由局部非零宣称固定曲线的无穷素数结论。

## 依赖

- [R410](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)：原 ray、ratio 与全部 $1\pm\lambda$ 单位。
- [R522](R522-common-degree3-even-factor-and-same-st-positive-test.md)：原 $H_0,H_1$ whole 格、完整偶纤维及原 $\mathcal T$。
- [R531](R531-hidden-two-frame-native-central-carry.md)：原完整 ratio 同余及 scalar whole core 规范。
- [R551](R551-original-norm5-two-state-core-and-complete-unit-inverse.md)：整个 odd degree5 的真实 $\chi_{65}$，完整双变量来源及规范。
- [R958](R958-original-e89-common-six-sigma-cm-projection.md)、[R961](R961-original-e65-common-six-sigma-cm-projection.md)：新轴的原完整来源、CM 投影及实际尺度。
- [R965](R965-original-e65-full-joint-dyadic-companion-unit-inverse.md)：原共同第一轴与不能免费保持的伴随测试。

本篇没有新增数学数值执行；完整 proof 使用原已付 whole 来源和显示代数恒等式。
