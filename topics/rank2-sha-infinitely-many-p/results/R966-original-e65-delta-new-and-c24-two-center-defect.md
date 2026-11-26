# R966 — 原 E65 的准确 δ-new 来源、三个受迫中央与 C24 两中心差

日期：2026-11-26。**状态：已证明。**

本篇从 R959 已识别的同一个 degree390 Fourier 来源证明它在
R877 的标准三点 theta 投影下为 new。这个事实并不靠“even
δ² 型”这一名称猜定。原 Gaussian、三点 lift 及其中心在第1节逐项
核定。

由此得到两个可直接使用的结论。第一，原 E65 中央导数为零时，
其三个指定 δ-torsion 译像的中央导数都确实为零。第二，R964 的
实际乘法来源 SZ 准确等于两个非零中心的完整伙伴差：
$$
 SZ=\frac19\sum_{j=1,2}C_j(J-J_j).
$$
这里没有把一个因子的投影移过另一个因子，也没有将这个差的中央
赋零。第6节把它写成卷积以后才切单位域的完整 Mellin 积分。

## 1. 同一标准格、Gaussian 和三个 canonical lifts

保持
$$
 \delta=1+2\omega,\quad \delta^2=-3,\quad
 \tau=(1-\omega)^{-1},\quad
 \Lambda=\mathbf Z+\tau\mathbf Z.
\tag{1}
$$
这一节用 $u$ 表示复统一化参数，避免与下面的来源 $Z$ 混名。
$\delta\tau=\omega$，且
$$
 \delta^{-1}=1-2\tau,\qquad
 \delta^{-1}\tau=\frac23-\tau.
$$
因此 $\Lambda$ 对 $\delta$ 稳定，完整三点核为
$$
 E[\delta]=\{T_0,T_1,T_2\},\qquad T_j=j/3\bmod\Lambda.
\tag{2}
$$
这里 $\delta T_j=-j+2j\tau$ 是实际周期；三点不由任意三等分点替代。

令 $\Sigma$ 为这个格的标准 Weierstrass sigma，
$\Sigma(u)=u+\cdots$。格的面积为 $\sqrt3/6$。
其准周期准确为
$$
 \eta_\lambda=2\sqrt3\pi\,\overline\lambda,\qquad
 \Sigma(u+\lambda)=\chi(\lambda)
       e^{\eta_\lambda(u+\lambda/2)}\Sigma(u).
\tag{3}
$$
这里 $\chi$ 是标准 sigma 半特征。为核定 (3)，准周期映射可写成
$A\lambda+B\bar\lambda$；CM 关系
$\eta_{\omega\lambda}=\omega^{-1}\eta_\lambda$ 迫 $A=0$，
Legendre 关系再给 $B=\pi/\operatorname{area}(\Lambda)=2\sqrt3\pi$。
没有另加一个二次 exponential 改动 sigma。

对本篇出现的 degree $3m$，其中 $m=8,122,130$ 都为偶数，
R877 的原 deck lift 是
$$
 \mathcal T_j^{(3m)}A(u)=
 \Sigma(\delta u)^m
 \frac{A(u+T_j)}{\Sigma(\delta(u+T_j))^m}.
\tag{4}
$$
分母的零点按完整 quotient 解释；这是原线丛的 lift，不是一个
带待定 scalar 的普通物理平移。
由于 $A/\Sigma(\delta u)^m$ 是椭圆函数，(4) 不依赖周期代表，
满足三点群律，而且随 degree 的乘法相容。

准确比较 R959 的 Gaussian。若
$$
 A(u)=e^{3m\sqrt3\pi u^2}F(u),
$$
由 $\lambda=\delta T_j=\delta j/3$ 得
$$
 \eta_\lambda\delta=2j\sqrt3\pi,\qquad
 \frac12\eta_\lambda\lambda=\frac{j^2\sqrt3\pi}{3}.
$$
$\chi(\lambda)^m=1$ 因 $m$ 偶。故
$$
 \frac{\Sigma(\delta(u+j/3))^m}{\Sigma(\delta u)^m}
 =\exp\!\left(2mj\sqrt3\pi u+
                    \frac{mj^2\sqrt3\pi}{3}\right)
 =\exp\!\left(3m\sqrt3\pi\{(u+j/3)^2-u^2\}\right).
\tag{5}
$$
所以同一原 frame 中确切有
$$
 \boxed{\mathcal T_j^{(3m)}A(u)
       =e^{3m\sqrt3\pi u^2}F(u+j/3).}
\tag{6}
$$
所有半特征和 Gaussian 在 (5) 相消；不能在一般别的 lift 下
直接照抄 (6)。

将这个复模型经固定周期同构认回 $E_1:y^2=x^3+1$ 时，
(4) 恰为 R877 的代数 lift。若 $A=\sigma^{3m}R$，它也可完全
代数地写成
$$
 \mathcal T_j^{(3m)}A
  =\sigma^{3m}(\delta x)^m
       \left(\frac{R}{(\delta x)^m}\right)\!\circ\tau_{T_j}.
\tag{7}
$$
这使用同一个准确除法函数
$\sigma(\delta z)=\delta x\sigma^3$。
非零两点在代数模型中是 $x=0,\ y=\pm1$，次序由 (2) 固定。
(7) 同时证明后文的译像都是代数 whole 截面，不以复 Gaussian
表达式猜测其整性。

## 2. 原 E65 来源的完整 δ-new 恒等式

记 $Z=F_{65,1}$，是 R959/R961 的同一个原来源：
$$
 Z=\sigma^{390}P_Z(X),\quad X=x^3,\quad
 \deg P_Z=64,\quad [X^{64}]P_Z=1.
\tag{8}
$$
原实际最小分母为175；来源从 $z^6$ 起。
R959(32)–(34) 在 (1) 的格上已将它识别为一个非零固定 scalar
倍的
$$
 A_{65}(u)=e^{390\sqrt3\pi u^2}
 \sum_{n\in\mathbf Z}a_n
    \exp\!\left(\frac{\pi i\delta n^2}{2340}+2\pi inu\right),
\tag{9}
$$
并准确证明
$$
 a_{-n}=a_n,\qquad
 a_n=v_2(n\bmod4)v_3(n\bmod3)
               f_5(2n\bmod5)f_{13}(-n\bmod13),
 \quad v_3=(0,1,1).
\tag{10}
$$
本篇保留全部五、十三处系数，没有把 $a_n$ 换成一条任意三处向量。

令
$$
 \Pi_\delta^{(390)}
   =\frac13\sum_{j=0}^2\mathcal T_j^{(390)}.
$$
由 (6)，它对 (9) 的第 $n$ 项的乘子是
$$
 \frac13\sum_{j=0}^2 e^{2\pi i nj/3}
 =\begin{cases}1&3\mid n,\\0&3\nmid n.\end{cases}
$$
(10) 使 $3\mid n$ 的完整系数也为零。该 Fourier 级数局部一致
收敛，故可以作这三个有限平移和；于是得到整个截面恒等式
$$
 \boxed{\Pi_\delta^{(390)}Z=0,\qquad
        Z_0+Z_1+Z_2=0,\quad
        Z_j=\mathcal T_j^{(390)}Z.}
\tag{11}
$$
这是由已识别原 Fourier 来源取得的绝对标准 trace-zero，
没有从 degree、CM7/19 谱维数或导子名称反推。

另外 $Z(-z)=Z(z)$。对 (4) 作反射，因这里的 $m$ 偶，
$$
 \iota\mathcal T_j^{(3m)}
  =\mathcal T_{-j}^{(3m)}\iota,\qquad
  (\iota A)(z)=A(-z).
\tag{12}
$$
所以
$$
 \boxed{Z_1(-z)=Z_2(z).}
\tag{13}
$$
在 $z=0$ 结合 $Z_0(0)=0$、(11)，还得到
$Z_1(0)=Z_2(0)=0$。
这是真正的中心值零，不只是模 $p$ 的零。

## 3. C24、真实奇伙伴及完整两中心差

保持全部原符号
$$
 Q_2(X)=7X^2-4X+16,\qquad
 C=-\frac{\sigma^{24}x^2yQ_2(X)}7,\qquad
 S=\frac{X(X-8)}{Q_2(X)}.
\tag{14}
$$
此处 $S$ 仅指式(14)的有理乘子，与原权17算术来源的同名字母区分。
R959/R960 原实际角因子给
$$
 P_Z=X(X+1)Q_2R_{60},\qquad
 J=J_Z=-7\sigma^{366}xyR_{60},\qquad Z=CJ.
\tag{15}
$$
所有65个原系数仍由原完整 CM 来源固定；没有重新选择 $R_{60}$。
$R_{60}$ 的最高系数为 $1/7$，所以 $J=z+\cdots$，degree366。
式 (15) 是 whole 伙伴，无未消的 $Q_2$ 极。

置
$$
 C_j=\mathcal T_j^{(24)}C,\qquad
 J_j=\mathcal T_j^{(366)}J.
\tag{16}
$$
由 (4) 或 (7) 的准确张量兼容，
$$
 C_jJ_j=Z_j.
\tag{17}
$$
特别第2节的真实新型条件在这个因式分解中准确是
$$
 \boxed{\frac13\sum_{j=0}^2 C_jJ_j=0.}
\tag{18}
$$
不能将 (18) 拆为 $J_j=J$、$\Pi_\delta J=0$，或一个因子的
独立消失。

R877(19) 已在完全相同的 lift 下证明
$$
 \Pi_\delta^{(24)}C
   =\frac37(E_0-8E_1)=3SC,\qquad
 E_j=-\sigma^{24}x^{8-3j}y.
\tag{19}
$$
因此 $\sum_jC_j=9SC$。先乘原未平移的 $J$，再减去 (18)，
得到准确的整个来源身份
$$
 \boxed{
 SZ=\frac19\sum_{j=0}^2C_jJ
    =\frac19\sum_{j=0}^2C_j(J-J_j)
    =\frac19\sum_{j=1,2}C_j(J-J_j).}
\tag{20}
$$
第零项确为零；另外两项保持各自完整中心和伙伴。

若 $D_j=C_j(J-J_j)$，原 $C,J$ 都为奇来源，故 (12) 给
$$
 D_1(-z)=D_2(z),\qquad
 (C_1J)(-z)=C_2J.
\tag{21}
$$
这只将两个中心在偶读数中配对，不令其中任何一个为零。

(20) 的精确 C24 坐标也必须保留：
$$
 SZ=\frac{E_0J-8E_1J}{7},\qquad
 RZ=\frac{E_0J+44E_1J+16E_2J}{7},\qquad R=1-6S.
\tag{22}
$$
这里的 $1/7$ 不能只因讨论方向而丢弃。

### 3.1 三点轨道中真正的型三奇来源

令 $c_1=[X]P_Z$。R960 的真实角 profile
$\deg f_Z=64$，结合
$f_Z(t)=\sum_{j=0}^{64}c_j(-t)^{65-j}$，准确给
$c_0=0,\ c_1\ne0$。这仍是同一个原多项式的系数，不另造输入。

置
$$
 Y_3=\frac{Z_1-Z_2}{2},\qquad
 Z_1=-\frac Z2+Y_3,\quad Z_2=-\frac Z2-Y_3.
\tag{22a}
$$
它是一个明确的 whole degree390 奇来源。
还可直接读出其非零首项。设 $T_1=(0,\epsilon)$，
$\epsilon=y(T_1)\in\{1,-1\}$，顺序仍由 (2) 固定。
在 $z=0$ 有
$$
 x(z+T_1)=2\epsilon z+\cdots,\qquad
 \mathcal T_{1}^{(390)}Z
 =\sigma(z)^{390}
     \left(\frac{x(z)}{x(z+T_1)}\right)^{130}
                      P_Z(x(z+T_1)^3).
$$
后一式由 (7) 中全部 $\delta^{130}$ 准确消去得到。
$\sigma^{390}x^{130}=z^{130}+\cdots$，故
$$
 \boxed{Y_3(z)=\frac{\epsilon c_1}{2^{127}}z^3+\cdots\ne0.}
\tag{22b}
$$
在固定 $c_1$ 的分子所含有限素集之外，这也是整单位首项；
不能仅由 $p>211$ 预先删除这一有限集。

两个非零 $\delta$ 点固定于 $[\omega]$。
在上式中 $x(\omega z)=\omega x(z)$，平移后同样成立，
$P_Z$ 只读 $x^3$，且 $\sigma^{390}(\omega z)=\sigma^{390}(z)$。
所以 $Z_j(\omega z)=Z_j(z)$。结合奇性，$Y_3$ 的准确
$\mu_6$ 型为三。它不是一个新算术中央；原 principal 读者因
型及反射而不读它，但一般混合测试会读到这个指定的实际来源。

## 4. 整格、精确中心零与原 b=17 返回

全部等式先在原代数 theta 格成立。对 $p>211$，固定原好位环上
$2,3,5,7,13,17,65,175$ 都为单位。
三点 $\delta$-核是有限 étale；R877 的标准 descent lift (7)
在相应好整模型上作用于 whole 截面格，只有已显示的固定单位分母。
因此 $C_j,J_j,Z_j,D_j,C_jJ$ 都是同一模型的整 whole 来源。
这里可先清原固定系数分母，再取三点算子；没有依赖大阶 Taylor
系数的非整除法。

还须检查除 $p$ 行要求的准确中心核。非零 $T_j$ 处 $x=0$。
(14) 给 $C$ 在这两点至少二阶零，(15) 给 $J$ 至少一阶零；
(4) 的实际局部 multiplier 是非零单位。所以
$$
 C_j(0)=J_j(0)=0 \quad(j=1,2).
$$
连同 $C(0)=J(0)=0$，得到
$$
 D_j(0)=C_jJ(0)=Z_j(0)=0 .
\tag{23}
$$
这些是 whole degree390 的准确中心零来源。
若需要 principal 型及原六阶开始的窗，可以对每个来源施加原
$\mu_6$ 投影 $\Pi_0$。它整、分母为6，保持 (20)，并将 (23)
后的首个可能阶准确置于6；所有被读取的 $h(p+1)$ 次系数不变。

一般单位 $b$ 令 $\theta_b^6=b$，同一规范为
$$
 C_b(z)=\theta_b^{-5}C(\theta_bz),\quad
 J_b(z)=\theta_b^{-1}J(\theta_bz),\quad
 Z_b(z)=\theta_b^{-6}Z(\theta_bz),\quad
 S_b(z)=S(\theta_bz).
\tag{24}
$$
把点同时送到 $T_{j,b}=\theta_b^{-1}T_{j,1}$ 后，(4) 或 (7)
给译像具有完全相同的齐次式。
故 (18)–(22) 在 $b=17$ 上所有系数仍分别是
$1/3,1/9,1/7$，没有额外 period scalar。
$\theta_b$ 及这些点在当前好位的相应有限 étale 扩张中都是单位
输入；不要求它们都预先属于基剩余域。

物理 $E_{65}$ 与共同 $E_{17}$ 的实际周期用 R959(55)：
若 $u^6=65/17$，取
$\Omega_{p,65}=u^{-1}\Omega_{p,17}$，则
$$
 \nu_{65,p}=\frac{17}{65}\nu_{Z_{17},p}
\tag{25}
$$
（若采用整数来源 $175Z$，两边同时乘175）。
(24) 同样运输这里的每个 degree390 项，因此 (25) 的同一个单位
因子适用于整条身份。没有从其它曲线为平移或乘积赋予新的
Schwartz、Euler 或 Selmer 身份；算术授权仍只是 R959 的 $Z$。

## 5. 三个真的受迫中央：普通与惰性分别说明

### 5.1 普通的原 principal 单位 Mellin

设 $p\equiv1\bmod3$。全部来源用同一个共同 $E_{17}$ 普通整周期。
令
$$
 \mathcal L_p(A)=
 \left.\frac{d}{dv}\int_{\mathbf Z_p^\times}
          \langle x\rangle^{(p-1)v}\,d\nu_A(x)\right|_{v=0}.
\tag{26}
$$
这与 R959 的 $G'_A(0)$ 差同一个准确非零因子
$(p-1)\log_p(1+p)$，因此零条件相同。
这里只用原 principal 分支，不把任意 Teichmüller 型混进 (26)。

反射的 Amice 公式是
$\nu_{\iota A}=[-1]_*\nu_A$。
原单位域和权在 $x\mapsto-x$ 下不变，故
$\mathcal L_p(\iota A)=\mathcal L_p(A)$。
对 (11)、(13) 应用同一真实线性泛函，得到
$$
 \boxed{\mathcal L_p(Z_1)=\mathcal L_p(Z_2)
                =-\frac12\mathcal L_p(Z).}
\tag{27}
$$
所以 **原 E65 坏中央确实强迫这三个指定 translated 来源的
中央全零**。这里不是把 tame torsion 解释为
$\mathbf Z_p$ 上的字符或加法平移；它们各自有 (7) 固定的完整
生成截面和整测度。

### 5.2 惰性的整个原 Newton 读者

设 $p=6s-1>211,\ d=p+1$。在同一模型上用原
$c_b=[z^d]\log(\sigma_b/z)$，$v_p(c_b)=-1$。
对本篇 degree390 来源定义
$$
 \mathcal J_{A,p}(v)=
 \sum_{h\ge0}(390c_b)^{-h}
       [z^{dh}]\{A(z)e^{-390c_bz^d}\}\,(v)_h.
\tag{28}
$$
若已采用 R943 的共同 $\kappa=34c_b+\Delta$，则使用
$q_Z\kappa,\ q_Z=195/17$；这里
$p\kappa$ 是单位，不能当作额外一层 $p$。
R342 的完整整 Gaussian 重标在准确中心零格上保持中央导数，
故下述身份与原读者一致。

先施加 $\Pi_0$ 后，各输入为 degree390、至少六阶的整 whole
来源；R959(57)–(58) 的逐基圆盘估计原样适用。因此 (28) 是整个
收敛的原 Newton 函数，线性身份不只限于一个截断层。
$d$ 偶，Gaussian 也偶，所以
$\mathcal J_{\iota A,p}=\mathcal J_{A,p}$。
由 (11)、(13) 得更强的整函数身份
$$
 \boxed{\mathcal J_{Z_1,p}
       =\mathcal J_{Z_2,p}
       =-\frac12\mathcal J_{Z,p}.}
\tag{29}
$$
它特别给中央导数的同一受迫关系。

(24) 与 $c_b=\theta_b^dc_1$ 同时运输后，每一项都只带
$\theta_b^{-6}=b^{-1}$；物理 $E_{65}$ 与共同 $E_{17}$ 的
比例仍为 $17/65$。原 Gaussian 的第 $h$ 次幂和
$z^{dh}$ 缩放完全相消，不能只运输其中一项。

### 5.3 真正的首除 p 行及其提升范围

本篇的 (23) 允许应用 R855/R856 的
$$
 \mathfrak B_{390,p}(\bar A)
       =j_{p+1}(A)/p\bmod p
\tag{30}
$$
于同一个准确中心零整格；所有提升仍固定原曲线和完整来源。
不将其扩成“中心值仅模 $p$ 为零”的任意提升。

若沿用 R855 的整窗口证明，所需宽度是 $p+1+390$，而
$(p^2-1)/6>p+1+390$ 在当前 $p>211$ 已成立，
且 $p\nmid390$。因此这里没有因新增 degree390 暗用一个不足的
旧小-degree 窗。
由全来源等式直接得到
$$
 \boxed{
 \mathfrak B(SZ)
 =\frac19\sum_{j=1,2}\mathfrak B(D_j)
 =\frac29\mathfrak B(D_1),\qquad
 \mathfrak B(Z_1)=\mathfrak B(Z_2)=-\frac12\mathfrak B(Z).}
\tag{31}
$$
这没有把 $\mathfrak B$ 与任何 trace 或乘法算子自由交换。
若用 R855 的热递推读取每一项，仍须保全部参数至模 $p^2$，
最后作原点特化和真除 $p$。

## 6. 第三列中央的完整两中心 cut

普通情形把同一原 degree390 乘积先化为测度卷积：
$$
 \nu_{C_jJ}=\nu_{C_j}*\nu_J,\qquad
 \nu_{C_jJ_j}=\nu_{C_j}*\nu_{J_j}.
$$
于是 (20) 给没有少域的准确式
$$
 \boxed{
 \mathcal L_p(SZ)
 =\frac{p-1}{9}\sum_{j=1,2}
  \iint_{\;x+y\in\mathbf Z_p^\times}
     \log_p\langle x+y\rangle\,
       d\nu_{C_j}(x)\,d(\nu_J-\nu_{J_j})(y).}
\tag{32}
$$
每个因子使用第4节的同一普通周期和完整 canonical 中心。
域是 $x+y$ 为单位，不是分别令 $x$ 和 $y$ 为单位；
非单位输入与相消到非单位的单位对都由该域准确处理。

若原 $\mathcal L_p(Z)=0$，(27) 使三个**对角乘积**
$C_jJ_j=Z_j$ 的中央确实为零。
再由 (21) 合并两个非零中心，可准确化为
$$
 \boxed{
 \mathcal L_p(SZ)=\frac29\mathcal L_p(C_1J)
 =\frac{2(p-1)}9
  \iint_{\;x+y\in\mathbf Z_p^\times}
       \log_p\langle x+y\rangle\,
             d\nu_{C_1}(x)d\nu_J(y).}
\tag{33}
$$
这留下一个明确的**交叉乘积**，没有将它赋零。

惰性处相同的线性、反射及 (29) 给
$$
 \mathcal J'_{SZ,p}(0)=\frac29\mathcal J'_{D_1,p}(0);
 \qquad
 \mathcal J'_{Z,p}(0)=0
 \Longrightarrow
 \mathcal J'_{SZ,p}(0)=\frac29\mathcal J'_{C_1J,p}(0).
\tag{34}
$$
这里不引入惰性普通测度；右侧仍为 (28) 的完整 Newton 读者。
(32) 的普通积分式不会移用于惰性素数。

## 7. 与原完整投影和二挠伴随的合法合流范围

R963/R965 已在同一真实六变量框架中给
$$
 \mathcal P_{65}\Phi_\rho=Z\otimes\Lambda_\rho,
 \qquad \mathcal P_{65}\Phi_h=Z\otimes\Lambda_h.
\tag{35}
$$
对**已经投影后的**第一因子施加本篇三点 lift，准确得到
$$
 (\mathcal T_{j,Y}\mathcal P_{65})\Phi_\rho
       =Z_j\otimes\Lambda_\rho,\qquad
 (\mathcal T_{j,Y}\mathcal P_{65})\Phi_h
       =Z_j\otimes\Lambda_h.
\tag{36}
$$
原坏 $Z$ 条件由 (27) 使 (36) 在原第一单位 Mellin 权乘
任意独立五伴随测试上都为零。
这是三个完整已指定来源的真正受迫族。

对任意真实混合测试 $F(Y,\mathbf Z)$，记
$F^\pm=(F(Y,\mathbf Z)\pm F(-Y,\mathbf Z))/2$。
(22a) 在同一完整张量中还给
$$
 \boxed{
 (Z_1\otimes\Lambda)(F)
   =-\tfrac12(Z\otimes\Lambda)(F^+)
                      +(Y_3\otimes\Lambda)(F^-),\qquad
 (Z_2\otimes\Lambda)(F)
   =-\tfrac12(Z\otimes\Lambda)(F^+)
                      -(Y_3\otimes\Lambda)(F^-).}
\tag{37}
$$
这里 $\Lambda$ 可以取 (35) 的任一实际伴随；
测试中的全部 cut 和 logarithm 同时进入 $F^\pm$。
这显示一般 mixed cut 中必须保留的准确型三项及其 (22b) 的
非零首项，而不是将两个平移来源统称为原 $Z$ 的 scalar 倍。

R965 的二幂算子 $\widehat{\mathscr D}$ 只动伴随，故它与
(36) 的第一因子 $\mathcal T_{j,Y}$ 严格交换。
这给合法的二、三处有限中心联用，但没有交换
$\mathcal T_{j,Y}$ 与 $\mathcal P_{65}$ 的顺序，
也没有把尚未投影的原第一 sigma 因子认作 $Z$。

尤其 (20) 是单变量 whole 来源恒等式，(32) 是其真实二因子
卷积身份；它们不是任意六变量伴随系数的逐项整除或逐项 trace
恒等式。原 R548(41)/R965(34) 的混合测试仍须保持
$P_1,R_c,L_h^{-1}$ 的顺序、全部 CM 分支和所有单位条件。
本篇的新受迫族不自动杀掉该混合测试，也不消去 (33) 的交叉项。

### 7.1 原全局偶 mixed 测试上的真实压缩

原 $\Phi_\rho,\Phi_h$ 在全部六变量同时取负时为偶：
原六个奇 sigma 的乘积为偶，所有原线性框架和 $H$ 保持这个反射。
第一角和原完整 CM trace/pull 算子也与该反射交换（在每个完整
有限纤维上同时把 torsion 中心取负），故 (35) 的投影来源仍为偶。
$Z$ 为偶且非零，约消这个第一因子得到
$$
 \Lambda_\rho(-\mathbf z)=\Lambda_\rho(\mathbf z),\qquad
 \Lambda_h(-\mathbf z)=\Lambda_h(\mathbf z).
\tag{38}
$$
所以 $Y_3\otimes\Lambda$ 在全部六变量同时反射下为奇。

若实际连续 mixed 测试满足
$$
 F(-Y,-\mathbf Z)=F(Y,\mathbf Z),
\tag{39}
$$
则无论它的 cut 是否混合第一轴、是否为分离变量，
$$
 (Y_3\otimes\Lambda)(F)=0.
$$
将 (22a) 作用于这个**完整测试类**，得到
$$
 \boxed{
 (\mathcal T_{1,Y}\mathcal P_{65}\Phi)(F)
 =(\mathcal T_{2,Y}\mathcal P_{65}\Phi)(F)
 =-\frac12(\mathcal P_{65}\Phi)(F),
 \quad \Phi=\Phi_\rho,\Phi_h.}
\tag{40}
$$
这里不需要坏中央假设；它是全局偶 mixed 测试上真正的有限中心
压缩，而不只是对独立伴随的 Mellin 测试成立。

使用 (40) 前，来源和测试的范围仍须逐项保持。原全局偶来源可把
任意原测试准确换为
$$
 F^{\mathrm{ev}}(v)=\frac{F(v)+F(-v)}2
\tag{41}
$$
而不改其积分。所有实际线性拉回 $P_1,R_c,L_h^{-1}$ 都与同时
取负交换，所以可以对包含全部 cut、$q$ 及 logarithm 的原测试
整体作 (41)，没有只偶化其中一个因子。

R965 三个码来源也具有所需的全局偶性。原 Weyl lift 对同时反射
满足 $\iota_6U_r\iota_6^{-1}=U_r^{-1}$、
$\iota_6V_s\iota_6^{-1}=V_s^{-1}$。
在 R965 的完整四码空间中 $U_r^2=V_s^2=I$，而
$\Phi_\rho$ 为偶，所以 $e_r=U_r\Phi_\rho$ 以及
$U_rV_{\omega r}\Phi_\rho$ 均为偶。
保中心的奇次幂代表在这些来源上作用相同，故三个真实有限
torsion 来源都允许 (41)。若再施加 $\mathcal P_{65}$，其偶性
继续保持，(38) 对相应真实伴随同样成立。

相反，一个尚未与其负中心配对的单独 CM/torsion 分支未必是偶；
不能在有限纤维求和之前就对每支任意作 (41)。
也不能把一般 $\mathcal T_{j,Y}\mathcal P_{65}\Phi$ 本身称为全局偶，
因为它含 (22a) 的奇项。(40) 正确要求测试已满足 (39)。

最后，(40) 并不使 $(\mathcal P_{65}\Phi)(F)$ 在一般 mixed cut
上为零。坏中央只直接控制 §5 的原 Mellin 分离测试；
(40) 给原 mixed 读数的准确共同倍率，没有消去该读数本身，
也不删除 (33) 的交叉乘积。


### 7.2 原指定 carry 测试已经全局偶

本节只用 R536、R544、R548 的原测试，不改其系数或域。
此处的普通参数始终是
$\lambda=-\bar\pi_0^{-1},\ \kappa=p\lambda^2$；
它与惰性 Gaussian 的同名参数不同。

R536(7)–(8) 的十个 $\phi_j$ 及 $\phi_*=-C^6/8$ 都是原六输入
的齐次六次多项式。该文 (10) 的线性换元不改次数，
(11) 的 $\mathcal R_p$ 只对每个 $E$ 次数乘以准确系数
$(1+\lambda\kappa^j)^{-1}$，所以整个 $\mathcal R_pP_p$ 仍齐次六次。
原 (24) 选择的实际系数 $x_p$ 依赖 $\lambda,\kappa$，但不依赖
被反射的六个积分变量。因此 (25) 及 (40)–(43) 中
$
 q_{n,p}^{(j)}
 =\frac1{b\Omega^6}
   (\mathcal R_pP_p)(D_j/\kappa^n,E_j,G)
$
在所有六输入同时取负时不变。
每个 $\Gamma_{n,j}=\{C,F\ {\rm unit},D_j\in p^n\}$ 也在同一
反射下稳定，因为显示的三个观察都是线性形式。
保完整三分支及其 $1/3$ 后，准确得到
$
 \boxed{\mathfrak q_{n,p}(-\xi)=\mathfrak q_{n,p}(\xi).}
\tag{42}
$

R544(22)，等价的 R548(37)，使用这个同一个
$q=\mathfrak q_{n,p}$：
$
 f=1_{L_{\rm mix}\ {\rm unit}}q
  \bigl(1_{Y_s\ {\rm unit}}d\log\langle Y_s\rangle
        -1_{W\ {\rm unit}}d\log\langle W\rangle\bigr).
$
三个 unit 条件在取负下不变；原 principal 权满足
$\langle-x\rangle=\langle x\rangle$。
故 $f(-\xi)=f(\xi)$ 是原完整测试的恒等式。
所有实际 $R_c,P_1,L_h^{-1}$ 都是线性映射，于是 R548(41) 与
R965(33) 的指定剩余测试已经满足
$
 \boxed{
 F_{\rm rem}
 =\bigl((f-f\circ R_c)\circ P_1\bigr)\circ L_h^{-1},
 \qquad F_{\rm rem}(-Y,-\mathbf Z)=F_{\rm rem}(Y,\mathbf Z).}
\tag{43}
$
全部 $\kappa^{-n}$、$q$ 系数、cubic carry、unit/deep 条件和
logarithm 都保持原值；没有只偶化一个局部因子。

所以 (40) 可以直接应用于 (43) 及 §7.1 所列完整已投影来源，
无需先修改测试。仍只得到两个 $\delta$ 中心的准确倍率
$-1/2$；原 $(\mathcal P_{65}\Phi)(F_{\rm rem})$ 本身是否为零
须由同一实际四态、全部 CM 分支和其余算术行继续支付。

本节的原编号依据：
[R536(7)–(11),(24)–(25),(40)–(43)](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)；
[R544(22)](R544-original-s3-and-exact-mixed-unit-complement.md)；
[R548(37),(41)](R548-original-whole-third-source-cm-reflection-and-complete-positive-spectrum.md)。

## 已付输入与剩余实际门

本篇已付原 E65 的标准三点 new 性、完整 Gaussian/lift 比较、
三个合法中央零的运输、实际 $SZ$ 的两中心伙伴差，
以及同一个 unit-cut 上的准确交叉读数。
没有新数学数值执行或目标素数样本；使用的是 R959 已登记的
完整 Fourier/CM 身份和 R877 已证明的真实投影。

六条算术坏中央尚未给出 (33) 的交叉乘积零或非零；
它不能由伙伴质量、有限谱或一个自由乘法传播替代。
本篇也没有完成同一个原中央导数的无穷素数非零门。

## 依赖

- [R959：原 E65 全部 Schwartz、实际 degree390 和完整中央桥](R959-original-e65-two-independent-points.md)。
- [R960：六原来源的实际完整角格](R960-original-e65-six-source-normalization-and-integral-grid.md)。
- [R877：同一标准 δ 三点迹与原 C24 的完整投影](R877-original-norm-three-common-source-and-h22-partner.md)。
- [R963：原 h 与 E65 的完整投影](R963-original-h-e65-full-cm-projection.md)。
- [R964：实际 $d/h_7$ 来源和完整交换子](R964-original-e65-rational-off-target-unit-commutator.md)。
- [R965：原两态的完整二挠伴随单位逆](R965-original-e65-full-joint-dyadic-companion-unit-inverse.md)。
- [R855：whole 原格与准确中心零除 p 行](R855-original-full-heat-connection-and-canonical-divided-jet.md)。
- [R856：原 whole Hurwitz 与 Frobenius 递推](R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)。
