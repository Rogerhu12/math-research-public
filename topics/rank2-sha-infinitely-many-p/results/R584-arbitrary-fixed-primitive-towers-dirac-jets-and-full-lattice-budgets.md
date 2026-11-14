# R584 — 任意固定长度原函数塔、全部 Dirac jets 与同一全次数成本

日期：2026-11-14。**状态：已证明。**

R575 的七个积分并不是代数独立性所允许的最大塔。
对两个原 $f_4=x\sigma^6$、$f_1=-xy\sigma^6$，任意预先固定的有限长度
都可用正幂规整到同一个 $w=z^6$；完整代数独立性、所有普通
Dirac jet 缺陷，以及同一多项式格上的普通和惰性成本均可直接证明。

当塔变长时，不能继续只减一个原点质量。
本文减去全部实际 Taylor jets，显示新增的每一条原负矩，
并给出固定有理线性组合，在不假设这些负矩为零的情况下
消掉全部局部 Dirac 缺陷。这些组合依然不是有界测度。
全部结论保持原来源，不把新增函数的核心自动当作原中央条件。

## 1. 任意固定塔及正幂规整

固定非负整数 $m_4,m_1$，置
$$
R_4=2+6m_4,\qquad R_1=5+6m_1,\qquad
d_4=4,\quad d_1=1,\qquad
q_\ell=(R_\ell+d_\ell)/6.
\tag{1}
$$
所有这些整数在研究素数 $p$、次数 $D$ 和 jet 阶 $k$ 之前固定。

在原 $b=17$ 的 sigma frame 上定义
$$
U_{\ell,r}(z)=\frac1{(r-1)!}\int_0^z(z-t)^{r-1}f_\ell(t)\,dt,
\qquad 1\le r\le R_\ell,
$$
$$
V_{\ell,r}(z)=z^{R_\ell-r}U_{\ell,r}(z).
\tag{2}
$$
每个积分取固定零初值。
$f_\ell$ 的 tame 型为 $d_\ell$、首阶为 $z^{d_\ell}$，所以
$V_{\ell,r}$ 的型是零，首阶为 $z^{R_\ell+d_\ell}=w^{q_\ell}$。
全部 $V$ 是整个 $w$ 平面上的有理系数整函数；没有除以 $z$。

加上同一个原 $S,T$，得到
$$
\mathbf G_R=(S,T,(V_{4,r})_{r=1}^{R_4},(V_{1,r})_{r=1}^{R_1}),
\qquad N=2+R_4+R_1=9+6(m_4+m_1).
\tag{3}
$$
这里 $N$ 是坐标数，源格的秩稍后另记为 $n_D$。

每个固定原 theta 来源满足 $\exp(O(|z|^2))$ 的完整准周期上界。
(2) 沿直线积分只增加一个固定次数多项式因子；
再乘一个固定正幂也不改变有限型二阶上界。
所以存在仅依赖固定塔的 $C_R$，对全部 $A\ge1$，
$$
\boxed{
\sup_{|w|\le A}\log\max(1,|\mathbf G_R(w)|)
\le C_R(1+A^{1/3}).
}
\tag{4}
$$
不声称 $C_R$ 对无限增长的塔长一致。

## 2. 任意有限塔的完整代数独立性

保持 R575 的实际微分域
$$
K_0=\mathbf C(z,x,y),\quad K_1=K_0(g),\quad
K=K_1(\sigma),\quad g=\sigma'/\sigma,\quad Dg=-x.
$$
[R575 第2–3节](R575-fixed-primitive-towers-and-complete-ordinary-dirac-defects.md)
证明的是对**任意**非零 $F\in K_0$，
$$
Dv=F\sigma^6
\quad\text{在 }K\text{ 或其任何有限代数扩张中无解}.
\tag{5}
$$
这个量词不限制 $F$ 的 $z$ 次数：
有限 $z$ 极点迫椭圆函数有常数原函数；
有限 $g$ 极点迫 $x$ 有有理原函数；
最后 $(D+6g)P=F$ 的最高 $g$ 次数排除全部多项式解。
有限非零 $\sigma$ 极点亦被对数导数排除。
因此 (5) 直接适用于下面任意固定的有限集合。

令
$$
J_{\ell,j}=\int_0^z t^j f_\ell(t)\,dt,
\qquad 0\le j<R_\ell .
$$
任何非零常数线性组合的被积函数都是
$$
x\{A(z)-yB(z)\}\sigma^6\ne0,
\qquad A,B\in\mathbf C[z].
$$
非零性因为 $z$ 在 $\mathbf C(E)$ 上超越，而 $y$ 非常数。
由 (5)，这个组合没有 $K$ 中的原函数。

R575 第4节已完整证明的加性积分引理遂给所有这些 $J$
在 $K$ 上代数独立。它的原三角变换为
$$
U_{\ell,r}
=\frac1{(r-1)!}\sum_{j=0}^{r-1}
 (-1)^j\binom{r-1}{j}z^{r-1-j}J_{\ell,j},
\tag{6}
$$
对角 $(-1)^{r-1}/(r-1)!$ 非零，任意有限长度均可逆。
再乘 (2) 的非零 $K$ 元素，故全部 $R_4+R_1$ 个 $V$
仍在 $K$ 上代数独立。

原 $S,T\in K$，二者已由 R418 证明代数独立。因此
$$
\boxed{\operatorname{trdeg}_{\mathbf C}\mathbf C(\mathbf G_R)=N.}
\tag{7}
$$
这是固定实际整函数的独立性，不是增加形式标签所得的维数。

## 3. 普通地点必须减去全部真实 jets

在任意好普通地点使用 R540/R579 的原实际规范
$$
\mu_f|_{p\mathbf Z_p}=\beta_p[\kappa_p]_*\mu_f,\qquad
|\beta_p|_p=1,\quad v_p(\kappa_p)=1,\quad \|\mu_f\|\le1,
$$
$$
\mathcal A_{\mu_f}(Z)=f(\Omega_p\log(1+Z)),\qquad |\Omega_p|_p=1.
\tag{8}
$$
全部普通 $p$ 均在此范围，非仅固定射线。
简写 $\beta,\kappa,\Omega$。

对 $r\ge1$ 定义原单位测度和其完整矩
$$
\tau_{\ell,r}=1_{\mathbf Z_p^\times}(t)t^{-r}\mu_f,
\qquad M_{\ell,r,j}=\tau_{\ell,r}(t^j),\quad 0\le j\le r.
$$
使用归一 jet 泛函
$$
\delta^{[j]}(\varphi)=\frac{\varphi^{(j)}(0)}{j!}
=\varphi^{[j]}(0,\ldots,0).
\tag{9}
$$
它不是 $j>0$ 时的有界测度。
定义真正的 jet 多项式分布及其余项
$$
Q_{\ell,r}=\sum_{j=0}^r M_{\ell,r,j}\delta^{[j]},
\qquad B_{\ell,r}=\tau_{\ell,r}-Q_{\ell,r}.
\tag{10}
$$
于是 $B_{\ell,r}(t^j)=0$ 对 $0\le j\le r$ 全部成立，
不需要任何负矩消失假设。

原函数的准确分布是
$$
\boxed{
\rho_{\ell,r}
=\sum_{n\ge0}\beta^n\kappa^{-rn}[\kappa^n]_*B_{\ell,r}.
}
\tag{11}
$$
对 R579 的整个连续差商范数
$$
\|\varphi\|_{r,p}
=\max_{0\le j\le r}\sup_{\mathbf Z_p^{j+1}}
 |\varphi^{[j]}(t_0,\ldots,t_j)|_p,
$$
(11) 第 $n$ 项在测试 $\varphi$ 上准确等于
$$
\beta^n\int t^r
 \left\{\varphi^{[r]}(\kappa^nt,0,\ldots,0)
              -\varphi^{[r]}(0,\ldots,0)\right\}\,d\tau_{\ell,r}(t).
\tag{12}
$$
这是完整 Newton 余项，已经减去所有次数至 $r$ 的原 Taylor 项。
其范数至多 $\|\varphi\|_{r,p}$，且因连续性在 $n\to\infty$ 时趋零。
故 (11) 对每个 $C^r$ 测试收敛，且
$$
\boxed{|\rho_{\ell,r}(\varphi)|_p\le\|\varphi\|_{r,p}.}
\tag{13}
$$
不声称各项在算子范数内趋零。

对于 $m\le r$，其 $m$ 次矩为零；对于 $m>r$，
(8) 和原几何级数给
$$
\rho_{\ell,r}(t^m)
=\frac{\mu_f(1_{\mathbf Z_p^\times}t^{m-r})}
 {1-\beta\kappa^{m-r}}
=\mu_f(t^{m-r}).
$$
所以保全部零初值，准确有
$$
\boxed{\mathcal A_{\rho_{\ell,r}}(Z)
=\Omega^{-r}U_{\ell,r}(\Omega\log(1+Z)).}
\tag{14}
$$
因此 (11) 呈示的是 (2) 中同一个固定原函数，没有另选原点常数。

## 4. 全部深度、全部缺陷与新增负矩

由于 $\tau_{\ell,r}$ 支持于单位，而每个 $\delta^{[j]}$ 支持于原点，
对 (11) 先逐有限和作真实限制，再取极限，得到
$$
\rho_{\ell,r}|_{p\mathbf Z_p}
=\beta\kappa^{-r}[\kappa]_*\rho_{\ell,r}-Q_{\ell,r}.
$$
并且 $[\kappa]_* \delta^{[j]}=\kappa^j\delta^{[j]}$，故所有 $m\ge1$ 有
$$
\boxed{
\rho_{\ell,r}|_{p^m\mathbf Z_p}
=\beta^m\kappa^{-rm}[\kappa^m]_*\rho_{\ell,r}
-\sum_{j=0}^r M_{\ell,r,j}
  \sum_{h=0}^{m-1}(\beta\kappa^{j-r})^h\delta^{[j]}.
}
\tag{15}
$$

令 $\mathcal D=-\partial_t$，即 $\mathcal D L(\varphi)=L(\varphi')$。
对 $a=R_\ell-r$ 置 $\widetilde\rho_{\ell,r}=\mathcal D^a\rho_{\ell,r}$。
R579 的完整差商导数恒等式给其 $C^{R_\ell}$ 范数仍至多一，
且
$$
\mathcal A_{\widetilde\rho_{\ell,r}}(Z)
=\Omega^{-R_\ell}V_{\ell,r}(\Omega\log(1+Z)).
\tag{16}
$$
准确恒等式
$\mathcal D^a\delta^{[j]}=(j+a)!/j!\,\delta^{[j+a]}$
保留所有阶乘。

定义所有实际负矩
$$
I_{\ell,d}=\int_{\mathbf Z_p^\times}t^{-d}\,d\mu_{f_\ell}(t),\qquad d\ge1.
\tag{17}
$$
$M_{\ell,r,r}=0$，因为 $f_\ell(0)=0$ 且 (8) 给单位质量也为零。
其余 $M_{\ell,r,j}=I_{\ell,r-j}$。
tame 型只给
$$
I_{\ell,d}=0\quad\text{除非 }d+d_\ell\equiv0\pmod6.
$$
因此设
$$
\mathcal D_4=\{2,8,\ldots,R_4\},\qquad
\mathcal D_1=\{5,11,\ldots,R_1\}.
$$
(15) 的完整正幂版本为
$$
\boxed{
\begin{aligned}
\widetilde\rho_{\ell,r}|_{p^m\mathbf Z_p}
={}&\beta^m\kappa^{-R_\ell m}[\kappa^m]_*\widetilde\rho_{\ell,r}\\
&-\sum_{\substack{d\in\mathcal D_\ell\\d\le r}}
 I_{\ell,d}\frac{(R_\ell-d)!}{(r-d)!}
 \left\{\sum_{h=0}^{m-1}(\beta\kappa^{-d})^h\right\}
 \delta^{[R_\ell-d]} .
\end{aligned}}
\tag{18}
$$
例如基本塔 $R_4=2,R_1=5$ 恰退回 R575 的两个 Dirac 质量。
更长塔确实出现 $I_{4,8},I_{1,11}$ 等新值；
它们没有由原 $I_{4,2},I_{1,5}$ 或原中央条件自动控制。
(18) 保留了每个新值、每个 jet 阶及全部深度因子。

## 5. 无条件消掉缺陷的固定子空间

固定一个 $\ell$，令 $R=R_\ell$、$\mathcal D=\mathcal D_\ell$，
$s_\ell=|\mathcal D|=m_\ell+1$。
考虑仅由固定有理数构成的矩阵
$$
A_{r,d}=
\begin{cases}
(R-d)!/(r-d)!,&r\ge d,\\
0,&r<d,
\end{cases}
\quad 1\le r\le R,\quad d\in\mathcal D .
\tag{19}
$$
取行 $r=d\in\mathcal D$ 得一个下三角方阵，
对角 $(R-d)!$ 全非零。因此 $A$ 在 $\mathbf Q$ 上秩为 $s_\ell$，
在全部 $p>R$ 处也有同一单位三角子式。

固定选择
$$
(c_1,\ldots,c_R)\in
\left\{c\in\mathbf Q^R:\sum_r c_r A_{r,d}=0
                       \text{ 对全部 }d\in\mathcal D\right\}.
\tag{20}
$$
这个空间的维数准确为 $R-s_\ell$。
以非 pivot 行为自由变量，逐次解上述固定三角方阵，
可选一组基，其全部分母只含不超过 $R$ 的素数。
定义实际整坐标
$$
H_{\ell,c}(w)=\sum_{r=1}^R c_r V_{\ell,r}(w).
\tag{21}
$$
同族坐标的周期乘数都是同一个 $\Omega^R$，所以 (20) 在
(18) 中对每个实际 $I_{\ell,d}$ 分别消去，无须其值为零。
于是每个这些固定组合均有完整普通身份
$$
\boxed{
\widetilde\rho_{\ell,c}|_{p^m\mathbf Z_p}
=\beta^m\kappa^{-Rm}[\kappa^m]_*\widetilde\rho_{\ell,c},
\qquad m\ge1 .
}
\tag{22}
$$
该结论对任意好普通位成立，并非仅一个固定射线。

任意选择的基与 $S,T$ 合起来仍代数独立，
因为它只是全部独立 $V$ 的一个固定满秩线性投影。
坐标数为
$$
\boxed{
N_{\rm free}
=2+(R_4-m_4-1)+(R_1-m_1-1)
=7+5(m_4+m_1).
}
\tag{23}
$$
这里 “free” 仅指原点 jet 缺陷为零，不赋新的算术中央身份。

这些新组合仍不是有界测度。
因为 $R\in\mathcal D$，(20) 的最后一列迫使 $c_R=0$。
所以 (21) 的每个分布项都含至少一次真实分布导数，
杀掉全部局部常数测试；但非零坐标 (21) 有一个非零多项式矩。
如果它是有界测度，局部常数在连续函数中的稠密性会迫它为零，
矛盾。
未规整的 $\rho_{\ell,r}$ 也非有界：在某个固定单位紧开集 $B$
上 $\tau_{\ell,r}(B)\ne0$，而
$$
\rho_{\ell,r}(\kappa^nB)
=\beta^n\kappa^{-rn}\tau_{\ell,r}(B)
$$
无统一界。
因此 (22) 不能代替有界测度所需的普通全乘积论证。

## 6. 同一个真实多项式格的全普通成本

对全部坐标 (3)，固定
$$
E_{D,R}=\bigoplus_{|\mathbf a|\le D}\mathbf Z\mathbf X^{\mathbf a},
\quad n_D=\binom{D+N}{N},\quad
r_k(P)=[w^k]P(\mathbf G_R(w)),
$$
$$
K_{D,k,R}=\ker_{\mathbf Q}(r_0,\ldots,r_{k-1})\cap E_{D,R},
\qquad \varphi_{D,R}^k=r_k|_{K_{D,k,R}\otimes\mathbf Q}.
\tag{24}
$$
保持原最大系数范数和实 Euclidean 范数。
对子空间 (21) 也独立取其固定坐标的同一定义，不把两个源格混写。

(13)、(16) 给每个 $V_{\ell,r}$ 的实际 $C^{R_\ell}$ 范数至多一。
R579 的完整 lattice-path 卷积论证于是给次数至多 $D$
的实际分布阶至多 $R_*D$，其中 $R_*=\max(R_4,R_1)$。
全部坐标至少从 $w$ 起，删去次数大于 $k$ 的列不改变整个前缀及当前行，
所以可用 $R_*\min(D,k)$。

同一真实前缀杀掉全部次数小于 $6k$ 的矩。
对 monic 下降阶乘应用 R579 的全节点差商估值，准确约去 $(6k)!$，得
$$
\boxed{
\log\|\varphi_{D,R}^k\|_p
\le \Lambda_p(6k,R_*\min(D,k))\log p,\qquad
\Lambda_p(n,L)=\sum_{a\ge1}\min(L,\lfloor n/p^a\rfloor).
}
\tag{25}
$$
当 $L\ge n$ 时仍成立：高于 $n$ 的差商为零，低阶估值的最弱界为一。
这里没有因 $R_*>6$ 而删去某些节点或评价层。

对所有普通位求和，一次素数幂用
$\min(L,n)$ 在 $p=n/\min(L,n)$ 处分开；全部高幂为 $O(n)$。
由于 $\min(L,n)\le R_*D$，得到
$$
\boxed{
\sum_{p\ {\rm ordinary}}\log\|\varphi_{D,R}^k\|_p
\le3k\log D+O_R(k+D).
}
\tag{26}
$$
固定有限坏集由共同正收敛半径支付。
(21) 的固定线性组合在全部好位有单位系数，故同一证明也给其
独立源格的 (25)–(26)，所用差商阶仍为 $R_*\min(D,k)$。
没有对乘积直接宣称 (22) 仍是其一变量限制公式。

回到 $b=17$ 的固定同构时，每族真实式是
$$
V_{\ell,r,17}(w)=17^{-q_\ell}V_{\ell,r,0}(17w).
\tag{27}
$$
所以全部列乘固定 $17$ 单位幂、评价行乘 $17^k$，在 $p\ne17$
保持整格和真实饱和前缀；$17$ 包含在固定坏集中。

## 7. 同一任意塔的全部惰性成本

取好惰性 $p>\max(71,R_4,R_1)$，令 $c_p=p/(p^2-1)$。
原 $f_\ell=\sum a_{\ell,m}z^m$ 仍有 R574 的真实界
$$
v_p(a_{\ell,m})\ge-\lfloor(m-d_\ell)c_p\rfloor.
$$
对 $n=6j$，(2) 的准确系数是
$$
[w^j]V_{\ell,r}
=\frac{a_{\ell,n-R_\ell}}
 {\prod_{i=1}^r(n-R_\ell+i)}.
\tag{28}
$$
非零项必有 $n\ge M_\ell:=R_\ell+d_\ell$。
短段中的每个因子是 $n-h$，其中 $0\le h\le R_\ell-1$；
因 $p>R_\ell$，每个 $p^a$ 至多出现一个倍数。

若某个一次 $p$ 分母出现，写 $n=mp+h$。
当 $n<2p^2$ 时 $m<2p$，而
$M_\ell-h\ge d_\ell+1\ge2$，所以
$$
(n-M_\ell)c_p
=m+\frac{m+(h-M_\ell)p}{p^2-1}<m,\qquad
nc_p\ge m.
$$
因此完整一次吸收为
$$
\boxed{
\lfloor(n-M_\ell)c_p\rfloor+1\le\lfloor nc_p\rfloor
\quad(n<2p^2).
}
\tag{29}
$$
这保原被积函数的 $M_\ell$ 阶余量，不假设分子被 $p$ 整除。

[R583](R583-nine-coordinate-inert-resonance-absorption-and-sharp-envelope.md)
的逐因子累计现在对任意这些固定短段逐字适用：
未吸收的一次分母每个耗至少 $2p^2$ 的正次数；
高 $p^a$ 倍数的总数不超过 $\min(D,k)$ 及 $\lfloor6k/p^a\rfloor$。
故同一 (24) 的全部 $D,k$ 有
$$
\boxed{
\log\|\varphi_{D,R}^k\|_p
\le\left\{
\left\lfloor\frac{6kp}{p^2-1}\right\rfloor
+\left\lfloor\frac{6k}{2p^2}\right\rfloor
+\sum_{a\ge2}\min\!\left(\min(D,k),\left\lfloor\frac{6k}{p^a}\right\rfloor\right)
\right\}\log p.
}
\tag{30}
$$
先估计所有原列，再限制真实前缀，没有遗漏来源乘积。
固定线性组合 (21) 的多项式代入不增加次数，且系数在好位整，
所以其独立源格也满足 (30)。

所有余项全素数和为 $O(k)$，Gaussian 惰性和为
$3k\log k+O(k)$。固定坏位有正收敛半径，成本 $O_R(k+D)$。
因此对全部原塔及无缺陷子空间两种真实格，分别得到
$$
\boxed{
\sum_{p\ {\rm inert}}\log\|\varphi_D^k\|_p
\le3k\log k+O_R(k+D).
}
\tag{31}
$$
塔长增加不增加这个主系数，但常数与固定坏集允许随预先固定的塔改变。

## 8. 真实维数的作用及剩余算术要求

对于 (24) 的 $N$ 个坐标，
(4)、(7)、(26) 和 R159 的完整旗标给以下严格门：
若在同一格全部非零层上有实际改善
$$
\sum_{p\ {\rm inert}}\log\|\varphi_D^k\|_p
\le a_I k\log D+b_I k\log k+O_R(k+D),\quad b_I<3,
$$
则必有
$$
N\le\frac{a_I+6}{3-b_I}.
$$
所以充分严格条件为
$$
\boxed{a_I+Nb_I<3N-6.}
\tag{32}
$$
无缺陷的独立子格以其真实维数 $N_{\rm free}$ 代入同一式。
当前无条件 (31) 是 $(a_I,b_I)=(0,3)$，两种格均未达到严格门。

若保持 $a_I=0$，较长固定塔所需的是 $b_I<3-6/N$。
这说明任何真正统一到所选全部坐标的正比例 Gaussian 改善，
都可以与一个足够长的固定塔比较。
它不说明在九格已付的改善会自动扩展到新格，
更不从原两个中央失败赋新增全部负矩为零。

同样，若某个论证对同一全部饱和层给
$p>CD^\vartheta$ 的惰性整性，(30) 只在 $p\le CD^\vartheta$ 求和
就有 $a_I=3\vartheta,b_I=0$，故严格阈值为
$$
\vartheta<N-2
\quad\text{（无缺陷子格则为 }\vartheta<N_{\rm free}-2\text{）}.
\tag{33}
$$
按 R159/R581 的同一全旗标反读，
对每个固定低于该阈值的 $\vartheta$ 和 $C>0$，
每个充分大 $D$ 都必须出现一个好惰性 $p>CD^\vartheta$
及真实非整饱和层；由 (30) 仍有 $k\ge(p+1)/6$。
这只是在固定原函数格中强制非整，不是原曲线中央非零证书。

原 $J'_S,J'_T$ 的完整算术身份、原 $q_n\ell$ 的混合域及所有补项
均未改变。(18) 明确显示更多塔会带来哪些新增负矩；
(20)–(23) 明确消除了局部缺陷，同时保其非有界性质。
原算术假设到所选完整源格的实际改善或 cutoff 桥仍须支付，
主目标继续保持未完成。
