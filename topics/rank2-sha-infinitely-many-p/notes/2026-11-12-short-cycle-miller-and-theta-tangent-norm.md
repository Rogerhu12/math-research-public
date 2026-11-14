# 短 Frobenius 周期中的固定 Miller 单位、全 jet 与 theta 切向范数

日期：2026-11-12。状态：本文各恒等式、局部范数及精度结论均已证明。
它们保留实际十七次截面，但尚未把其中央导数识别成一个已知非零的
固定代数单位对数。特别区分代数 theta 平移和局部收敛的单位范数。

## 1. 固定对象与短周期素数

使用[实际纯对数分解](2026-11-12-actual-rational-reference-pure-logarithmic-form.md)
已经完整证明的规范：

$$
E_0:y^2=x^3-x,\quad \omega=dx/(2y),\quad D=d/\omega,
\quad T=(0,0),\quad \alpha=4-i,\quad N=17.
$$

令 $\theta=\theta_T$、$\theta(0)=1$，并置

$$
f_0(z)=\theta(\alpha z),\qquad A(z)=f_0(z)R(z),
\qquad R=\frac{q(x^{-2})}{u_\alpha(x^{-2})}.
\tag{1.1}
$$

这里 $q(V)=V+3V^2/5-V^3/5+V^4/5$，$u_\alpha$ 是前文的固定
四次多项式。$R$ 在 $O$ 为 $z^4+O(z^8)$，只在

$$
\mathcal D^\circ=\{P=T+S:0\ne S\in E_0[\alpha]\}
\tag{1.2}
$$

有十六个简单极点。记其留数为 $\rho_P$。已证

$$
\sum_P\rho_P=0,\qquad \rho_{iP}=i\rho_P,
\qquad \rho_{-P}=-\rho_P,
$$

$$
R\omega=\frac1{17}\sum_P\rho_P\,d\log g_P,
\quad \operatorname{div}g_P=17(P)-17(T),\quad g_P(O)=1.
\tag{1.3}
$$

尤其 (1.3) 中没有未定的 $\omega$ 项：其可能系数准确等于
$17^{-1}\sum_{Q\in E[\alpha]}R(Q)$，前文的四维商代数证书证明它为零。
规范还给 $g_{-P}(Z)=g_P(-Z)$。

以下限制到

$$
p\equiv35\ \text{或}\ 67\pmod {68},\qquad
s_p=\begin{cases}1,&p\equiv1\pmod {17},\\
-1,&p\equiv-1\pmod {17}.
\end{cases}
\tag{1.4}
$$

这些都是惰性好素数，且对每个 $P\in\mathcal D^\circ$，
$[p]P=s_pP$、$[p]T=T$。所有下述固定函数定义在
$L=\mathbb Q(i,E_0[17])$，不随 $p$ 改变。

## 2. Miller 范数及其真正的固定单位常数

对奇整数 $m$，采用 sigma 规范

$$
\Psi_m(z)=\sigma(mz)/\sigma(z)^{m^2}.
$$

它的除子是 $\sum_{Q\in E[m]\setminus\{O\}}(Q)-(m^2-1)(O)$。
固定 $p,P$，比较除子与 $Z=O$ 处的值，得到

$$
\prod_{Q\in E[p]}g_P(Z+Q)
   =C_{p,P}\,g_{[p]P}([p]Z),
\qquad C_{p,P}=\prod_{Q\in E[p]}g_P(Q).
\tag{2.1}
$$

所有取值都避开 $P,T$。Weil 互反律应用于 $g_P,\Psi_p$，由于两者
除子的支撑不交，且 $g_P(O)=1$，给出准确常数

$$
\boxed{\quad C_{p,P}=
   \left(\frac{\Psi_p(P)}{\Psi_p(T)}\right)^{17}.\quad}
\tag{2.2}
$$

这不是只确定到根单位的式子：两边在 (2.1) 中的常数规范已经固定。

取固定辅助整数 $b=69\equiv1\pmod {34}$，并置

$$
v_P=\Psi_b(P)/\Psi_b(T)\in L^\times.
\tag{2.3}
$$

sigma 除法的定义直接给交换恒等式

$$
\Psi_b([p]Z)\Psi_p(Z)^{b^2}
 =\Psi_p([b]Z)\Psi_b(Z)^{p^2}.
\tag{2.4}
$$

因为 $[b]P=P$、$[p]P=s_pP$，而奇数 $b$ 的 $\Psi_b$ 是偶函数，
在 $P,T$ 各取值并相除后得到

$$
\boxed{\quad C_{p,P}^{b^2-1}=v_P^{17(p^2-1)}.\quad}
\tag{2.5}
$$

此处 $p\nmid b(b^2-1)$：$b=3\cdot23$，
$b^2-1=4760=2^3\cdot5\cdot7\cdot17$，这些素数均不在 (1.4)。
$P,T$ 在好模型中有不同于 $O$ 的非零约化，$[b]$ 可分且仍固定它们；
因此 $\Psi_b(P)$、$\Psi_b(T)$ 都是 $p$ 进单位。
所以 (2.3) 是一组真正固定的代数单位，且任一 $p$ 进对数分支给

$$
\log_p C_{p,P}
 =\frac{17(p^2-1)}{b^2-1}\log_p v_P.
\tag{2.6}
$$

然而实际留数加权不能省略。由
$\Psi_b(iZ)=i^{1-b^2}\Psi_b(Z)=\Psi_b(Z)$，有
$v_{iP}=v_P$；故每个四点轨道内相消，准确得到

$$
\boxed{\quad
 \sum_P\rho_P\log_p v_P=0,
 \qquad \sum_P\rho_P\log_p C_{p,P}=0.
\quad}
\tag{2.7}
$$

因此 (2.6) 本身没有给实际中央导数的非零值。

## 3. 保留全部 jet 的交换式

令

$$
h_{m,P}(z)=\Psi_m(P+z)/\Psi_m(P),\qquad h_{m,P}(0)=1.
$$

(2.4) 除以常数项后，不丢弃任何 Taylor 项，得到

$$
\frac{h_{p,P}(bz)}{h_{p,P}(z)^{b^2}}
 =\frac{h_{b,P}(s_ppz)}{h_{b,P}(z)^{p^2}}.
\tag{3.1}
$$

这里使用了 $h_{b,s_pP}(pz)=h_{b,P}(s_ppz)$，其中的符号来自
$\Psi_b$ 的偶性。取常数项零的正式对数，$n\ne2$ 时有

$$
\boxed{\quad
[z^n]\log h_{p,P}
 =\frac{(s_pp)^n-p^2}{b^n-b^2}[z^n]\log h_{b,P}.
\quad}
\tag{3.2}
$$

$n=2$ 的分母为零，但不是漏掉一个任意二次项。直接求导得

$$
D^2\log\Psi_m(P)=-m^2x([m]P)+m^2x(P)=0
\quad(m=p,b).
\tag{3.3}
$$

还须说明 (3.2) 不自动产生新的固定底数非 Wieferich 条件。
设

$$
\zeta_P^{(0)}=\zeta(P)-\bar P/\mathcal A,
\qquad \zeta_P^{(j)}=D^j\zeta(P)\quad(j\ge1).
$$

这些均为代数数，且 $j\ge1$ 时可由 $x,y$ 的整数微分多项式计算。
用准周期公式逐式展开 (3.1)，有

$$
[z^n]\log h_{b,P}
   =(b^n-b^2)\zeta_P^{(n-1)}/n!,
$$

$$
[z^n]\log h_{p,P}
   =((s_pp)^n-p^2)\zeta_P^{(n-1)}/n!.
\tag{3.4}
$$

在 $n=1$，这里用约化的 $\zeta_P^{(0)}$，准周期项准确被吸收；
在 $n\ge2$，直接微分 sigma 除法式即可。
所以 $b^n-b^2$ 本来就是固定 $h_b$ 第 $n$ 个对数系数的已知因子。
在临界 $n=p+1$ 把它单独写成 Fermat 商后忘记这个共同因子，会产生
虚假的额外算术输入。(3.2) 的正确作用是恢复全部 zeta/Bell jet。

## 4. 实际有理函数的完整 trace 分布

对 (2.1) 取 $D\log$，再乘 $\rho_P/17$ 并求和。
利用 (1.3) 与 $\rho_{s_pP}=s_p\rho_P$，得到原曲线上的准确有理函数式

$$
\boxed{\quad
\sum_{Q\in E[p]}R(Z+Q)=s_pp\,R([p]Z).
\quad}
\tag{4.1}
$$

这保留全部 jet，并非只在模 $p$ 或模 holomorphic 微分后成立。
如果 (1.3) 右边还含 $c\omega$，同样计算会多出
$p(p-s_p)c$；实际零迹正是去掉这一项的必要输入。

定义在 $O$ 正式盘上的真实对数原函数

$$
H(Z)=\frac1{17}\sum_P\rho_P\log_p g_P(Z),\qquad H(O)=0.
\tag{4.2}
$$

由于 $g_P\in1+t\mathcal O[[t]]$，这个式子在整个 $|t|<1$ 上收敛，
且 $dH=R\omega$。惰性时全部 $p$ 挠点都在此正式盘内；
所以 (2.1)、(2.7) 的对数现在可作实际收敛函数比较，得

$$
\boxed{\quad
\sum_{Q\in E[p]}H(Z+Q)=s_pH([p]Z).
\quad}
\tag{4.3}
$$

这是一条真实的对数分布式。它的导数是 (4.1)，而不是已经证明了
$H$ 在某个固定点的值等于 $J_{A,p}'(0)$。

## 5. 保留 theta 参考的规范化一阶范数

先在复 uniformization 上取 $E[p]$ 的平衡代表 $q_Q$，满足
$q_{-Q}=-q_Q$，因而 $\sum_Qq_Q=0$。定义代数规范平移

$$
\mathcal T_Qf_0(z)=
 \frac{f_0(z+q_Q)}{f_0(q_Q)}
 \exp\!\left(-\frac{N\bar q_Qz}{\mathcal A}\right).
\tag{5.1}
$$

它常数项为 $1$。这里 $f_0(q_Q)\ne0$，因为 $p$ 挠点不能落在
$[\alpha]^{-1}T$。规范平移的正式展开由 Mumford 挠点平移定义，
其系数为代数数；参见 Bannai–Kobayashi，
*Algebraic theta functions and $p$-adic interpolation of
Eisenstein–Kronecker numbers*，Duke Math. J. 153 (2010)，229–295，
[作者版 Theorem 2.9](https://arxiv.org/html/math/0610163v4)。
本文只使用该代数性结论，不使用作者版中另需普通性的整性命题。

由 $\alpha$ 双射置换 $E[p]$，乘积 $\prod_Qf_0(z+q_Q)$ 和
$f_0(pz)$ 有相同零点。二者自动因子也相同：平衡条件消去线性指数，
$\theta_T$ 的二挠半特征在奇数 $p$ 下不变。其比是无零极点的椭圆函数，
故为常数。再比较 $z=0$，得到

$$
\boxed{\quad \prod_{Q\in E[p]}\mathcal T_Qf_0(z)=f_0(pz).\quad}
\tag{5.2}
$$

若不用常数项一的规范，则右边应乘
$C_p^\theta=\prod_Qf_0(q_Q)$；不能混用这两种规范。

现在在双数环 $L[\tau]/(\tau^2)$ 中取

$$
f_\tau=f_0(1+\tau R)=f_0+\tau A.
$$

对每个平移用与 (5.1) 相同的线丛因子，并仍除以该平移的常数项。
由 (4.1) 及 $R(O)=0$，准确得到

$$
\begin{aligned}
\prod_Q\mathcal T_Qf_\tau(z)
 &=f_0(pz)\left(1+\tau
       \sum_Q\{R(z+Q)-R(Q)\}\right)\\
 &=f_0(pz)+\tau s_pp\,A(pz).
\end{aligned}
\tag{5.3}
$$

其中 $\sum_QR(Q)=0$ 是 (4.1) 在 $Z=O$ 的值。
因此这是保留真实 reference 的线性化范数；它没有以裸 $d\log$
替代原来的 theta 截面。

几何上，$f_\tau$ 在原简单零点 $P$ 附近的零点是
$P-\tau\rho_P$（用 $z$ 作为切向坐标）。其零点之和的一阶变化为
$-\tau\sum\rho_P=0$，故仍在同一个十七次线性系统内。
$[p]$ 把此零点送到 $s_pP-\tau p\rho_P$；
因为 $\rho_{s_pP}=s_p\rho_P$，这正是右边的方向 $s_pp\tau$。
这给 (5.3) 的独立除子解释。

## 6. 哪部分是真的局部单位范数

(5.1)–(5.3) 首先是代数 theta／复正式恒等式。
在惰性处，$f_0(t)$ 自身的 Taylor 收敛半径小于非零 $p$ 挠点的半径；
因而 $f_0(q_Q)$ **不能**解释为把 $t(Q)$ 直接代入这个 Taylor 级数。
这里的值与平移是由上述代数线丛规范定义，再送入 $p$ 进系数域。
没有由 (5.2) 宣称 $f_0$ 是整个开正式盘上的 Coleman 单位。

与此不同，$R(t)\in t^4\mathcal O[[t^4]]$，所以
$1+\tau R(t)$ 在 $|t|<1$ 是真正的双数整单位。
对正式群的有限平坦 $[p]$ 定义局部范数算子 $\mathcal N_p$，规范为

$$
(\mathcal N_p u)([p]t)=\prod_{Q\in E[p]}u(t+_EQ).
$$

于是 (4.1) 直接给实际整级数等式

$$
\boxed{\quad
\mathcal N_p(1+\tau R(t))=1+\tau s_ppR(t).
\quad}
\tag{6.1}
$$

因此 $R$ 是该切向 trace 算子的 $s_pp$ 本征方向。
但这一条固定一维方向本身不给一个非零整的范数相容逆系统。
确实，若各层都取 $1+\tau a_nR$、$a_n\in\mathcal O$，相容性要求
$a_n=s_pp a_{n+1}$；故 $a_0\in\bigcap_{n\ge0}p^n\mathcal O=0$。
若改用 $a_n=(s_pp)^{-n}a_0$，虽然在分式系数中相容，却引入逐层分母。
这只讨论这个固定本征方向，不否定其他整 Coleman 单位或 signed 格的存在。

## 7. 临界低 jet 中的精度损失

令 $d=p+1$。超奇异正式群满足
$[p]t\bmod p$ 的首项次数为 $p^2$。因此在截断次数 $\le d<p^2$ 时，
$[p]t$ 的每个系数都被 $p$ 整除。又 $R\in t^4\mathcal O[[t]]$，故

$$
\sum_{Q\in E[p]}R(t+_EQ)
  =s_ppR([p]t)\in p^5\mathcal O[[t]]+(t^{d+1}).
\tag{7.1}
$$

只把这条相对单位范数除以一次 $p$，再看临界低 jet，会得到零；
它不能直接等同于实际已知的除 $p$ Bell 行。

保留 (5.3) 的完整 theta 参考后，若
$A(z)=\sum\beta_mz^m$，则更准确地

$$
[\tau z^d]\prod_Q\mathcal T_Qf_\tau(z)
       =s_pp^{d+1}\beta_d=s_pp^{p+2}\beta_{p+1}.
\tag{7.2}
$$

所以从该范数的临界项提取 $\beta_{p+1}$ 需要保留 $p+2$ 层的规范化。
例如短周期中的 $p=67$，已有
[双算法脚本](../scripts/check-inert-theta-prime-diagonal.py) 的两条有限递推
均给 $\beta_{68}\equiv57\pmod {67}$；右边临界系数恰有赋值 $69$。
这不是零，而是高斜率归一化会抹掉低精度信息的明确计算。

原实际解析行仍由 R54/R59 定义：

$$
\ell_p(R)=\left.\frac d{du}\frac{J_{f_0R,p}(u)}{J_{f_0,p}(u)}\right|_{u=0},
\qquad J_{A,p}'(0)=\ell_p(R),
$$

$$
\frac{J_{A,p}'(0)}p\equiv\frac{\beta_{p+1}}{17pc}\pmod p.
\tag{7.3}
$$

这里 $c$ 为 R54 的共同首坏 sigma 系数，$v_p(c)=-1$。
(3.2)、(4.1)、(5.3) 与 (7.2) 给出彼此一致的全 jet／范数接口；
它们没有把 (7.3) 的非零性化成 (2.6) 的非零性，后者在真实权重下
已经由 (2.7) 相消。仍需一个保留正次数 theta 参考及高斜率归一化的
实际周期比较，才能把这些固定单位接到所需中央导数。
