# R432 — 原平衡两深度非零来源与保输出的三条真实 Hadamard 管

日期：2026-11-14。**状态：已证明。** 同时展开原 $G_{16}$ 的两条
sigma，可以让剩余两个 sigma 的尺度完全相同，并仍证明只有两个
独立深度的原输入域必有中央非零。这个平衡表示使 R337 的真实
Hadamard 矩阵 $B$ 严格固定原相加输出。

本篇还把该非零域完整接到原 $\mathcal K$ 的确定 $\Sigma$ 输入
表示。使用 R435 已付的完整 $K_{16}^4=I$，可取 $n\in4\mathbf Z$
并对 $\mathcal R$ 的两个输出同时施加真正的 $p^n$ 限制。
原 $\mathcal R$ 两输出始终保留。该实际隐藏域的完整第一边际与
原非零域恰相差常数 $-2/3$。
在这个**原联合**上，一条恰一单位管及其两个 Hadamard 像组成
三条两两不交的真实管；全部相加输出、第二输出与剩余补支均明确。

这给出原小核中的实际隐藏非零域，并不将其中央值赋为零。
原 $X$ 条件、内层 $\mathcal R$ 深条件与三管补域仍须准确运输。
主目标尚未完成。

## 1. 平衡展开后还是同一个原 S

保持 R339、R424、R429、R430 的同一曲线、周期和来源：
$$
b=17,\quad\delta^2=-3,\quad\gamma=(5+\delta)/2,\quad
S=-\frac1{84}\sigma\,\sigma(2\cdot)\sigma(\delta\cdot)
                   \sigma(2\delta\cdot)\sigma(\gamma\cdot)\sigma(\bar\gamma\cdot).
$$
写 $p>19$ 为同一普通好素数，$K=(p-7)/6$、$d=p-1$。
sigma 的原 full core 单独记为
$$
\nu_\sigma|_p=\lambda_\sigma[\kappa]_*\nu_\sigma,\qquad
v_p(\kappa)=1,\quad \lambda_\sigma\in\mathcal O^\times.
\tag{1}
$$
它不与 R430 的目标标量 $\lambda$ 混用。

取任意 $m\ge0$，令
$$
q=2\delta^{-m},\quad q_h=2\delta^{-h},\qquad
\mathcal E_m(z)=\prod_{h=1}^m\Theta(q_hz),\qquad
\mathcal B_m(z)=\Theta(2z)\mathcal E_m(z)^2.
$$
对原 $\sigma(2z)$ 展开 $m$ 次，对原 $\sigma(2\delta z)$ 展开
$m+1$ 次，准确得到
$$
\boxed{\sigma(2z)\sigma(2\delta z)
 =\delta^{2m+1}\sigma(qz)^2\mathcal B_m(z),}
\qquad
\boxed{G_{16}(z)=\frac{\delta^{2m}}4\sigma(qz)^2\mathcal B_m(z).}
\tag{2}
$$
没有改变原曲线，也没有只比较 Taylor 首项。
这里 $\mathcal B_m$ 中共有 $M=2m+1$ 个原 Theta 因子，其尺度列为
$$
(2,q_1,q_1,q_2,q_2,\ldots,q_m,q_m).
\tag{3}
$$
每个 Theta 始终使用 R339 的两 sigma 二次权表示。

在原 $S$ 的此表示中，指定尺度一的 sigma 输入 $x_0$ 为单位。
五个无权深 sigma 输入的尺度为
$$
(\delta,\gamma,\bar\gamma,q,q),\qquad
\widetilde C_m=-\delta^{2m+1}/84.
\tag{4}
$$
令每一对 Theta 的两个原 sigma 输入也保留。定义真正的原输入域
$$
\boxed{\mathcal D^{\mathrm{bal}}_{m;n,r}
=\{x_0\in\mathbf Z_p^\times,\quad
\text{五个 (4) 输入均在 }p^n,\quad
\text{全部 }2M\text{ 个 Theta sigma 输入均在 }p^r\}.}
\tag{5}
$$
各对的原权仍为
$\Omega^{-2}(XY-(X^2+Y^2)/2)$，总权是这些原权的乘积。
原输出为单位，且域的质量为零。记此原受限输出测度为
$\nu^{\mathrm{bal}}_{m;n,r}$、principal 函数为
$J^{\mathrm{bal}}_{m;n,r}(u)$。

## 2. 平衡后的完整聚合系数仍严格非零

写 R429 的同一个
$$
\sigma(z)=zA_b(z^6),\qquad a_m=(-27)^{-m}.
$$
由 $\Theta(z)=\sigma(\delta z)/(\delta\sigma(z))$ 和 R429 的
准确 telescope，
$$
\boxed{\mathcal B_m(z)
 =\frac{A_b(-27(2z)^6)A_b((2z)^6)}
             {A_b(a_m(2z)^6)^2}.}
\tag{6}
$$
定义
$$
Q_K(a)=[w^K]\frac{A_b(-27w)A_b(w)}{A_b(aw)^2}.
\tag{7}
$$
R429 已由原 $x''=6x^2$ 完整证明
$$
\log\frac1{A_b(-w)}
 =\sum_{j\ge1}\frac{b^ju_j}{6j(6j-1)}w^j,\qquad u_j>0.
$$
将右端乘二后取形式指数，得到
$$
(-1)^j[w^j]A_b(w)^{-2}
 \ge\frac{(b/105)^j}{j!}>0\qquad(j\ge1).
\tag{8}
$$
(7) 最高 $a$ 次项的系数正是 $[w^K]A_b(w)^{-2}$，因此
$\deg Q_K=K$。所以任意 $K+1$ 个不同的非负整数 $m$ 中，
都至少有一个使 $Q_K(a_m)\ne0$。可取 $0\le m\le K$；
也可取 $m\in\{0,3,\ldots,3K\}$。

完整 Theta 聚合的指定系数于是为
$$
\boxed{[z^{6K}]\mathcal B_m=2^{6K}Q_K(a_m)\ne0.}
\tag{9}
$$
所有相同深度造成的指数碰撞都已包含在 (6) 中。
这里只证明非零，不预付普通处单位性或统一赋值界。

令 $\mathcal H_m^{\mathrm{bal}}(T,U)$ 为把 (5) 的五个无权
深输入全部缩放 $T$、全部 Theta 对全部缩放 $U$ 后，测试
$d\log_p\langle Y\rangle$ 得到的解析函数；保留原权因子 $U^{2M}$。
和 R427、R429 一样，完整原 core 给
$$
(J^{\mathrm{bal}}_{m;n,r})'(0)
=\lambda_\sigma^{5n+2Mr}
                \mathcal H_m^{\mathrm{bal}}(\kappa^n,\kappa^r).
\tag{10}
$$
其 log 展开在 $(p\mathcal O)^2$ 上收敛；五个零质量 sigma
杀掉常数项。

五个 sigma 的一次正矩给
$$
\widetilde C_m\,\delta\gamma\bar\gamma q^2
=\left(-\frac{\delta^{2m+1}}{84}\right)
   \left(28\delta^{1-2m}\right)=1.
$$
因此完整指定系数准确是
$$
\boxed{
[T^5U^{2M+6K}]\mathcal H_m^{\mathrm{bal}}
=d(p-3)!\,I_{-(p-2)}\,\Omega^{p-2}\,2^{6K}Q_K(a_m)\ne0.}
\tag{11}
$$
这里是同一个原 $I_{-(p-2)}$；
R339 的 $I_{-(p-2)}\equiv(1-\lambda_\sigma\kappa)\Omega\pmod p$
已付其单位性。总 log 指数为 $5+6K=p-2$，没有另用固定负五次矩。

由二变量解析恒等定理，任意 $n_0\ge1$ 都有 $n,r\ge n_0$ 使
$(J^{\mathrm{bal}}_{m;n,r})'(0)\ne0$。
同 R429 的固定一轴再取极限论证，还可预先要求 $r\ge n+D$
或 $n\ge r+D$。也可把 $n$ 限制为任意固定正整数的倍数：
对 $r\ge n+D$，先固定允许的 $n$ 并令 $r\to\infty$，
再让 $n$ 遍历这些倍数；对 $n\ge r+D$ 则先固定 $r$。
每次使用的无限子列都趋于盘内零点，证明仍成立。
下面使用 $n\in4\mathbf Z_{\ge1}$、$r\ge n$。
输入数随 $p$ 变化，原目标始终是固定 $S$。

## 3. 将此非零域接到一个完整、明确的 Sigma 联合

保持 R424 的同一对称整核
$$
\mathcal R\in\mathcal S_{16}\boxtimes\mathcal S_{16},\qquad
\mathcal R(y,0)=-\frac23P_{16}(y),
$$
$$
P_{16}(y)=\frac{F_{18}(y)}{\sigma(y)^2}
=\frac{\Theta(y)\sigma(\gamma y)\sigma(\bar\gamma y)}7,
\qquad
F_{18}=\sigma^2P_{16}.
\tag{12}
$$
R430 的真实小核为
$$
\mathcal K(y,v)=G_{16}(y)\sigma(y-v)\sigma(y+v)\mathcal R(y,v).
\tag{13}
$$

为准确记录所需来源，定义
$$
\nu_{\mathcal R}^{(n)}=(\kappa^n r_0,s_0)_*\nu_{\mathcal R}(r_0,s_0).
\tag{14}
$$
这是完整联合的实际有界推前，第二输出 $s_0$ 没有改变；
**(14) 不是对 $\nu_{\mathcal R}$ 的第一输入施加 $p^n$ 限制。**
本篇不预设它与那种限制的关系。

使用 (2) 中的全部 $M$ 对 Theta 原 sigma 输入，设其带尺度的
相加输出为 $\tau$、完整二次权为 $Q^{\Theta}_m$。
再取四个独立原 sigma 输入 $a,b,c,e$，定义
$$
\boxed{
Y=\kappa^n r_0+\tau+q(a+b)+c+e,\qquad
X=s_0-c+e.}
\tag{15}
$$
底层带权联合始终是
$$
\frac{\delta^{2m}}4
 \left(\nu_{\mathcal R}(r_0,s_0)\otimes
 Q^{\Theta}_m\nu_\sigma^{\otimes2M}
                       \otimes\nu_\sigma(a)\nu_\sigma(b)\nu_\sigma(c)\nu_\sigma(e)\right).
\tag{16}
$$
在它上面只施加
$$
a,b,e\in p^n,\qquad c\in\mathbf Z_p^\times,\qquad
\text{全部 Theta 原 sigma 输入}\in p^r.
\tag{17}
$$
令 (15) 的完整联合推前为 $\mathfrak M_{m;n,r}$。
它含 (14) 的第一轴缩放、原 $\mathcal R$ 两输出、全部 Theta 权
和每一个显示的 sigma 输入。由于 $\kappa^nr_0\in p^n$、$r\ge1$，
(17) 上 $Y$ 自动为单位。

**完整边际恒等式。**
$$
\boxed{Y_*\mathfrak M_{m;n,r}
=-\frac23\lambda_\sigma^{-2n}\,
                         \nu^{\mathrm{bal}}_{m;n,r}.}
\tag{18}
$$

证明：这是一条完整 Amice 身份，不只是若干矩相等。
记 $\sigma^\times$ 为原单位 sigma 测度的变换。
(5) 先对三个 $\delta,\gamma,\bar\gamma$ 输入及两个 $q$ 输入使用
同一 sigma core，再用原 norm-three 身份，得到
$$
\begin{aligned}
\widehat{\nu^{\mathrm{bal}}_{m;n,r}}(z)
={}&\widetilde C_m\lambda_\sigma^{5n+2Mr}\kappa^{2Mr}
 \sigma^\times(z)\sigma(\delta\kappa^nz)
 \sigma(\gamma\kappa^nz)\sigma(\bar\gamma\kappa^nz)
 \sigma(q\kappa^nz)^2\mathcal B_m(\kappa^rz)\\
={}&\frac{\delta^{2m}}4\lambda_\sigma^{5n+2Mr}\kappa^{2Mr}
 \sigma^\times(z)\sigma(\kappa^nz)P_{16}(\kappa^nz)
 \sigma(q\kappa^nz)^2\mathcal B_m(\kappa^rz).
\end{aligned}
\tag{19}
$$
第二行使用
$\sigma(\delta z)\sigma(\gamma z)\sigma(\bar\gamma z)
=7\delta\,\sigma(z)P_{16}(z)$ 和
$7\delta\widetilde C_m=\delta^{2m}/4$。

另一方面，(16)、(17) 中只有 $a,b,e$ 三个无权 sigma 输入施加
深度 $n$，而 (14) 的第一边际由 (12) 准确给
$-2P_{16}(\kappa^nz)/3$。所以其第一边际的变换是
$$
-\frac23\frac{\delta^{2m}}4
 \lambda_\sigma^{3n+2Mr}\kappa^{2Mr}
 \sigma^\times(z)\sigma(\kappa^nz)P_{16}(\kappa^nz)
 \sigma(q\kappa^nz)^2\mathcal B_m(\kappa^rz).
$$
与 (19) 比较即 (18)。所有 $\Omega^{-2M}$ 已在原 Theta
变换中保留，原权的 $\kappa^{2Mr}$ 也没有丢失。证毕。

因此第2节选择的 $m$ 以及某些任意深的 $r\ge n$ 给出
$$
\boxed{\int d\log_p\langle Y\rangle\,d\mathfrak M_{m;n,r}
=-\frac23\lambda_\sigma^{-2n}
       (J^{\mathrm{bal}}_{m;n,r})'(0)\ne0.}
\tag{20}
$$
这是一个确定的 $\Sigma$ 表示中的真正非零联合。
它不是把 $F_{18},G_{18}$ 分离张量中的一个事件直接搬到
$\Sigma\mathcal R$ 输入表示。

### 3.1 四的倍数深度使此来源成为原 K 的真实隐藏限制

R435 在同一 ray、同一个原整 theta 格上已付
$K_{16}^4=I$，其外部测度标量是
$\lambda=-1/\bar\pi_0$。完整公式为
$$
\nu_{\mathcal R}|_{r_0\in p^n}
=\lambda^n(\kappa^nr_0,s_0)_*
                \nu_{(K_{16}^n\otimes I)\mathcal R}.
$$
因而对 $n\in4\mathbf Z_{\ge1}$，
$$
\boxed{\nu_{\mathcal R}|_{r_0\in p^n}
=\lambda^n\nu_{\mathcal R}^{(n)}.}
\tag{20a}
$$
这里使用的是全 $\mathcal S_{16}$ 上的真实算子，不是只在
$P_{16}$ 边际上猜测本征性。

现在回到原 (13) 的平衡输入表示 (2)，定义
$\mathfrak N_{m;n,r}$ 为完整 (16) 上真正的隐藏域
$$
\boxed{r_0\in p^n,\quad a,b,e\in p^n,\quad c\text{单位},
\quad\text{全部 Theta 原 sigma 输入}\in p^r,}
\tag{20b}
$$
其输出取原坐标
$$
\boxed{Y=r_0+\tau+q(a+b)+c+e,\qquad X=s_0-c+e.}
\tag{20c}
$$
$s_0$ 不附加任何条件。这确是固定原 $\mathcal K$ 的同一
$\Sigma\mathcal R$ 卷积表示中的限制；没有改变来源。
由 (18)、(20a)，得到完整测度身份
$$
\boxed{Y_*\mathfrak N_{m;n,r}
=-\frac23\lambda^n\lambda_\sigma^{-2n}
                       \nu^{\mathrm{bal}}_{m;n,r}.}
\tag{20d}
$$
所以第2节的非零选择可以同时满足 $n\in4\mathbf Z$、$r\ge n$，
并使 $\mathfrak N_{m;n,r}$ 的第一 principal 中央严格非零。
两种 core 标量分别保留；它们在当前 ray 上满足
$\lambda_\sigma=1/\bar\pi_0=-\lambda$，显示的比例仍为单位。

### 3.2 偶深交换保留真实第二深条件及 inverse 尺度

R435 同时证明 $\mathcal R$ 的对角二挠不变性及
$(K_{16}^2\otimes I)\mathcal R=(I\otimes K_{16}^2)\mathcal R$。
所以对本节的 $n$，完整有
$$
\boxed{\nu_{\mathcal R}|_{r_0\in p^n}
=(\kappa^nr_0,\kappa^{-n}s_0)_*
                   (\nu_{\mathcal R}|_{s_0\in p^n}).}
\tag{20e}
$$
在 (20b) 中应用它后，$a,b,c,e$ 和全部 Theta 隐藏条件原样保留，
输出准确变为
$$
Y'=\kappa^nr_0+\tau+q(a+b)+c+e,\qquad
X'=\kappa^{-n}s_0-c+e,\qquad s_0\in p^n.
\tag{20f}
$$
inverse 尺度仅作用于所示深输入，所以仍是整坐标。
不能删去 $s_0\in p^n$，也不能把 $X'$ 改回 $s_0-c+e$。
该完整返回没有说 $\mathcal R$ 的第二输入是与第一输入独立的附加
来源，因此没有免费进入 R430 的独立第二轴测试结论。

### 3.3 两个 R 输出可以同时深，且完整边际比例恰为 −2/3

更强地，给定任意 $j\in4\mathbf Z_{\ge0}$，在 (20b) 中再加
$s_0\in p^j$，记这个原实际限制为 $\mathfrak N^{(j)}_{m;n,r}$。
R435 的第二轴完整公式给
$$
\nu_{\mathcal R}|_{\{r_0\in p^n,s_0\in p^j\}}
=\lambda^j[1,\kappa^j]_*
                       (\nu_{\mathcal R}|_{r_0\in p^n}).
$$
原 $Y$ 输出不含 $s_0$；所有其它隐藏条件也不含 $s_0$。
所以对完整第一边际准确有
$$
\boxed{Y_*\mathfrak N^{(j)}_{m;n,r}
=\lambda^jY_*\mathfrak N_{m;n,r}
=-\frac23\lambda^{n+j}\lambda_\sigma^{-2n}
                        \nu^{\mathrm{bal}}_{m;n,r}.}
\tag{20g}
$$
这证明任意额外四倍深的第二限制仍保该第一中央非零。
没有要求两个 $\mathcal R$ 输入独立。

尤其可取 $j=n$。因 $\lambda=-\lambda_\sigma$，
$\lambda^{2n}\lambda_\sigma^{-2n}=1$，得到
$$
\boxed{Y_*\mathfrak N^{(n)}_{m;n,r}
=-\frac23\nu^{\mathrm{bal}}_{m;n,r}.}
\tag{20h}
$$
这时 (20b) 同时有 $r_0,s_0,a,b,e\in p^n$、$c$ 单位及全部
Theta 输入在 $p^r$；实际 $Y,X$ 两输出都为单位。
而且原总和、差输出准确满足
$$
W=Y+X=r_0+s_0+\tau+q(a+b)+2e\in p^n,\qquad
V=X-Y\equiv-2c\pmod p,
\tag{20h'}
$$
所以 $V$ 为单位。这条实际非零域位于原反对角深管中。
所以这条非零域完全位于原 $\mathcal K$ 的 $Y/X$ 双单位输出格内，
但它仍带显示的隐藏条件，不能把整个输出格的中央零分给它。

在 (20e) 上正确拉回第二深条件，还得到
$$
\boxed{\nu_{\mathcal R}|_{\{r_0\in p^n,s_0\in p^j\}}
=[\kappa^n,\kappa^{-n}]_*
                     (\nu_{\mathcal R}|_{s_0\in p^{n+j}}).}
\tag{20i}
$$
若 $j=n$，变换后的第二 R 输出 $\kappa^{-n}s_0$ 仍在 $p^n$，
而不是一个任意单位。这里完整保留的是 $s_0\in p^{2n}$；
两个来源式 (20h)、(20i) 都可放进下面的相同三管恒等式。

## 4. 平衡后真正保输出的 B、C 及三条完整管

令 $u=(a,b,c,e)^t$，使用 R337 已付的原四 sigma 身份
$\nu_\sigma^{\otimes4}=B_*\nu_\sigma^{\otimes4}
+C_*\nu_\sigma^{\otimes4}$，其中
$$
B=\frac12\begin{pmatrix}
1&1&1&-1\\1&1&-1&1\\1&-1&1&1\\-1&1&1&1
\end{pmatrix},\qquad
C=\frac12\begin{pmatrix}
1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1
\end{pmatrix}.
\tag{21}
$$
它们只作用这四个 sigma 输入，不作用 $(r_0,s_0)$ 或任何 Theta
输入，所以 (16) 的全部二次权和剩余联合保持原样。

以下使用 (20b)、(20c) 的原联合，置 $A=r_0+\tau$。
在同一个输入空间上定义
$$
Y_B=Y,\quad X_B=s_0-a+b,\qquad
Y_C=A+(q+1)a+(q-1)b,\quad X_C=X.
\tag{22}
$$
直接矩阵计算给
$$
(q,q,1,1)B=(q,q,1,1),\qquad
(0,0,-1,1)B=(-1,1,0,0),
$$
$$
(q,q,1,1)C=(q+1,q-1,0,0),\qquad
(0,0,-1,1)C=(0,0,-1,1).
\tag{23}
$$
这是平衡 (2) 带来的保原输出身份；未平衡的
$(2,2\delta,1,1)$ 行不满足第一式。

定义三条实际管
$$
\mathcal T_0=\{a,b,e\in p^n,\ c\in\mathbf Z_p^\times\},
\qquad\mathcal T_B=B\mathcal T_0,\qquad
\mathcal T_C=C\mathcal T_0.
\tag{24}
$$
每条管都由一个原单位参数 $h$ 及全体 $p^n\mathbf Z_p^4$ 组成：
$$
\begin{array}{c|c}
\text{管}&(a,b,c,e)\pmod{p^n}\\ \hline
\mathcal T_0&(0,0,h,0)\\
\mathcal T_B&(h/2,-h/2,h/2,h/2)\\
\mathcal T_C&(h/2,-h/2,h/2,-h/2).
\end{array}
\tag{25}
$$
三条管两两不交：第一条只有一个单位坐标，后两条有四个；
后两条若同线，第一坐标使比例为一，第四坐标则要求 $2=0$。
$B,C\in\mathrm{GL}_4(\mathbf Z_p)$ 保持完整 $p^n$ 邻域，所以
这不只是模 $p$ 点数计算。

同时 $B^2=C^2=I,(BC)^3=I$，并且
$$
B:\mathcal T_0\leftrightarrow\mathcal T_B,\quad
 B\mathcal T_C=\mathcal T_C;\qquad
C:\mathcal T_0\leftrightarrow\mathcal T_C,\quad
 C\mathcal T_B=\mathcal T_B.
\tag{26}
$$
所以这三条真实管的并对两个 Hadamard 变换都不变。

## 5. 保 R 两输出的精确交叠与补支

现在使用第2节允许的 $r\ge n$。全部 Theta 输入深度至少 $n$，
又保留真实 $r_0\in p^n$，故 $A=r_0+\tau\in p^n$。
由 (22)、(25)，得到完整输出余类表
$$
\boxed{
\begin{array}{c|cccc}
&Y&X&X_B&Y_C\\ \hline
\mathcal T_0&h&s_0-h&s_0&0\\
\mathcal T_B&h&s_0&s_0-h&h\\
\mathcal T_C&0&s_0-h&s_0-h&h
\end{array}
\pmod{p^n}.}
\tag{27}
$$
第二输出 $s_0$ 没有被抹成零。尤其准确有
$$
\mathcal T_B\cap\{X\in p^n\}
   =\mathcal T_B\cap\{s_0\in p^n\},
$$
$$
\mathcal T_0\cap\{X\in p^n\}
   =\mathcal T_0\cap\{s_0-c\in p^n\},\qquad
\mathcal T_C\cap\{X\in p^n\}
   =\mathcal T_C\cap\{s_0-2c\in p^n\}.
\tag{28}
$$
因此在 $s_0\in p^n$ 的那一部分，$\mathcal T_B$ 确实落入
原 $Y$ 单位、$X$ 深的输出域，而 $\mathcal T_0$ 的原 $X$ 为单位。
若 $s_0$ 为单位，交叠条件会改变，不能把 (28) 第一行推广到其他两管。

令 $\eta_{m;n,r}$ 表示 (16) 已对全部 Theta 输入施加 $p^r$
限制，并保留 $r_0\in p^n$，但四 sigma 尚未施加 (24) 的带权测度。
对任意连续完整测试 $f(y,x)$，原四 sigma 身份给
$$
\boxed{
\int_{\mathcal T_0}f(Y,X)\,d\eta_{m;n,r}
=\int_{\mathcal T_B}f(Y,X_B)\,d\eta_{m;n,r}
 +\int_{\mathcal T_C}f(Y_C,X)\,d\eta_{m;n,r}.}
\tag{29}
$$
还可在三项同时保留任意 $(r_0,s_0)$ 和全部 Theta 隐藏输入的测试，
因为两矩阵不作用这些输入。证明只需将左侧的
$\mathbf1_{\mathcal T_0}f(Y,X)$ 正确拉回 $B,C$；
两矩阵是对合，故域恰是 (24)，输出恰是 (22)。

取 $f(y,x)=\mathbf1_{y\text{单位}}d\log_p\langle y\rangle$，
第3节的某个任意深选择使 (29) 左边非零。
还可在 (29) 全部三项保留 $s_0\in p^n$；(20h) 保证此时左边
仍非零。这给三条分支的准确原输出格
$$
\mathcal T_0:\ (Y,X)\text{ 双单位},\qquad
\mathcal T_B:\ Y\text{ 单位},\ X\in p^n,\qquad
\mathcal T_C:\ Y\in p^n,\ X\text{ 单位}.
\tag{29a}
$$
原深总和也必须随分支运输：第一支用 $Y+X_B\in p^n$，
第二支用 $Y_C+X\in p^n$。两支各自的原 $Y+X$ 反而为单位，
如 (27) 直接所示。不能把 R431 对原 $Y+X$ 的核免费当作
已运输总和的核。
右边两个
**准确显示的**实际分支至少一个非零。
$\mathcal T_C$ 上原 $Y$ 在 $p^n$，但被测的 $Y_C$ 是单位；
不能据原 $Y$ 非单位删去这条补支。
若还测试 $X$，第一支必须用 $X_B$，不能写回 $X$。

完整输出域 $\{Y\text{单位},X\in p^n\}$ 也不等于
$\mathcal T_B$ 的受控部分。即使 $A,s_0\in p^n$，例如四 sigma 的
一个单位管邻域
$$
(a,b,c,e)\equiv(1,0,0,0)\pmod{p^n}
$$
给 $Y\equiv q$ 为单位、$X\equiv0$，却不在三管并中。
它是实际非空开闭补域；本篇不把集合非空自动认作其有符号测度非零。
这些补域及 (29) 的第二分支均须保留。

## 6. 与已付条件中央的准确接点

R430 已控制原 $\mathcal K$ 的完整第一 principal 中央和任意
第二输出测试；独立附加在第二轴的原输入也可完整保留。
本篇新增的是：

1. 同一原 $S$ 的真正两深度非零域可以选择一个 $B$ 保输出的
   平衡 sigma 表示，且有完整非零系数 (11)。
2. (20a)–(20d) 将该非零域完整送到原 $\mathcal K$ 的指定
   $\Sigma\mathcal R$ 隐藏域。$n\in4\mathbf Z$ 的真实全 core
   支付了第一轴缩放，第二输出和实际第一深条件都没有隐去。
3. (20g)–(20i) 允许两个内层输出同时深，且同深时第一边际恰
   为 $-2/3$ 倍原受限来源。偶深交换保真实 $p^{2n}$ 条件。
4. (27)–(29a) 支付了真实三管在 $Y/X$ 深度域中的交叠、保输出
   分支、改变输出的补支和真实输出域外余下的开闭部分。

仍待支付的接口具体是：由原 $J'_S(0)=0$ 合法控制 (20b) 这种
内层 $\mathcal R$ 与共享 sigma 的隐藏域；并处理 (29) 的
$Y_C$ 补支和 (28) 未覆盖的实际部分。
这里的内层完整 core 已由 R435 另行付清，不能仅从原
$\mathcal K$ 第一输出 core 拆出来；更不能从 core 恒等式本身
赋这条实际非零域以中央零。(20e)、(20f) 的偶深运输保留着
第二深条件、inverse 尺度和混合输出。

- [R429：倒 sigma 严格符号、真实两深度网格](R429-original-two-depth-grid-and-reciprocal-sigma-nonvanishing.md)。
- [R424：原 Bezout 核及完整 R16 边界](R424-original-half-period-bezout-kernel-and-complete-central-disintegration.md)。
- [R430：整反卷积后的原小核与准确条件中央](R430-original-integral-second-output-division-and-degree18-mixed-rows.md)。
- [R337：原四 sigma Hadamard 有界测度身份](R337-original-hadamard-domain-transport-and-depth-zero-propagation.md)。
- [R435：同一原 degree16 全 core、对角二挠不变性与完整偶深交换](R435-original-degree16-square-core-and-exact-two-axis-depth-transfer.md)。

