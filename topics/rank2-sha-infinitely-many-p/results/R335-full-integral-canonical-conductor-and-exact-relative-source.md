# R335：整个导子的完整整数典范基与准确相对来源

日期：2026-11-13。**状态：以下整个原导子在每个次数的准确整数基、相对于一个固定导子乘子的自由余源、全部原点阶及同一有限目标的完整运输均已证明。它给出整个可用导子来源，不再仅使用五个首生成元或三条修正。所有新增列已证明属于原幂格；没有给它们附加中央零条件，也未将来源完善当作目标深关系的非零定理。**

## 1. 固定原环与一个实际134次多项式

保留 R322、R325、R326 的
$$
R=\mathbf Z[1/(42b)],\quad b=17,\quad
A=7bS,\quad B=7bS(\delta z),\quad C=7bS(2z),
$$
原权为 $(1,3,4)$，原环及其归一化为 $\mathcal T_R\subset\mathcal N_R$。
仍取
$$t=-b/x^3,\quad h_7=16t^2+4t+7,\quad a=t(t-1)h_7,\quad A=\rho a.$$
记
$$
u_n=\lfloor3n/4\rfloor,\quad v_n=\lfloor n/2\rfloor,
\quad c_n=\lfloor2n/3\rfloor,
$$
$$
T_n=t^{u_n}(t-1)^{c_n}(1+8t)^{v_n}h_7^{u_n},
\qquad d_n=3u_n+2v_n+c_n.
\tag{1}
$$
已付的实际整数归一化是
$$\mathcal N_{R,n}=\frac{A^n}{T_n}R[t]_{\le d_n}.$$

R326 的 primitive 导子分子 $N\in\mathbf Z[t]$ 有完整准确分解
$$
\boxed{N=t^3(t-1)(1+8t)^3h_7^3P_{134},}
\tag{2}
$$
其中
$$
\boxed{\deg P_{134}=134,\quad \operatorname{cont}(P_{134})=1,
\quad P_{134}(0)=-3^4\cdot3159421.}
\tag{3}
$$
这里 $P_{134}$ 由已发表的 $N$ 作 (2) 的四个固定整多项式除法定义；
所附新证书保存它的全部135个整数系数并直接核 (2)、(3)，没有重跑旧1154条返回证书。

把 R325 的残数系数按 R326 的同一标量正规化，记为 $\kappa_*$。
该正规化标量为
$$\frac1{541653102231552}=2^{-22}3^{-17}\in R^\times.$$
由于 $G_0=A^{40}N/T_{40}$ 对应 $dt/Q_1$，(2) 给出
$$
\boxed{\kappa_*=
\frac{P_{134}}{t^{26}(t-1)^{24}(1+8t)^{16}h_7^{26}}.}
\tag{4}
$$
所以整个典范模的同一残数系数已经是一个固定明确分式，未留下不确定的有理倍数。

## 2. 每个次数的完整整数基

对 $m\ge1$ 置
$$
\alpha_m=\lceil3m/4\rceil,\quad
\beta_m=\lceil m/2\rceil,\quad
\gamma_m=\lceil2m/3\rceil,
$$
$$
Q_m=t^{\alpha_m}(t-1)^{\gamma_m}
                    (1+8t)^{\beta_m}h_7^{\alpha_m},
\quad e_m=3\alpha_m+2\beta_m+\gamma_m-2.
\tag{5}
$$
定义实际齐次分式
$$
\boxed{C_{m,j}=A^{m+39}\kappa_*\frac{t^j}{Q_m},
\qquad 0\le j\le e_m.}
\tag{6}
$$
原权始终是 $m+39$，不是 $m$。

**定理1（全部好素数、全部次数的准确整基）。**
令 $\mathfrak c_R=(\mathcal T_R:\mathcal N_R)$。则
$$
\boxed{(\mathfrak c_R)_n=0\quad(n<40),\qquad
(\mathfrak c_R)_{m+39}=\bigoplus_{j=0}^{e_m}R C_{m,j}\quad(m\ge1).}
\tag{7}
$$
没有新增5、13或其他随次数变化的坏素数。

**证明。** R325 的准确典范比较给
$$
(\mathfrak c_{\mathbf Q})_{m+39}
 =A^{m+39}\kappa_*H^0\!\left(\mathbf P^1,
                    \omega_{\mathbf P^1}(\lceil mD\rceil)\right),
$$
其中 $D$ 在 $0,r_+,r_-$ 的系数为 $3/4$，在无穷和 $-1/8$ 为 $1/2$，
在1为 $2/3$。有限极点分母正是 $Q_m$。
若微分写成 $f(t)dt/Q_m$，无穷处的条件恰为
$\deg f\le\deg Q_m+\beta_m-2=e_m$。
因此 (6) 已是整个有理导子的基。

须付准确的整数交集。令 $n=m+39$。相对于 (1)，(6) 的 numerator 是
$$
\boxed{P_{134}\,t^{E_m+j}(t-1)^{F_m}(1+8t)^3h_7^{E_m},}
\tag{8}
$$
其中
$$
E_m=\begin{cases}3,&m\equiv0,1\pmod4,\\2,&m\equiv2,3\pmod4,\end{cases}
\qquad
F_m=\begin{cases}2,&m\equiv0\pmod3,\\1,&m\not\equiv0\pmod3.\end{cases}
\tag{9}
$$
这些式子直接由
$$u_n-26-\alpha_m=E_m,\quad
c_n-24-\gamma_m=F_m,\quad v_n-16-\beta_m=3$$
得到。并且准确有
$$
\boxed{d_n-\deg\!\left(P_{134}t^{E_m}(t-1)^{F_m}(1+8t)^3h_7^{E_m}\right)-e_m=5.}
\tag{10}
$$
所以每个 (6) 都属于 $\mathcal N_R$。R322 已付
$\mathfrak c_R=\mathcal N_R\cap\mathfrak c_{\mathbf Q}$，遂证明这些列全是原整数导子。

反过来，任一有理典范元素的 (8) 分子是一个固定 primitive 整多项式乘
$f\in\mathbf Q[t]_{\le e_m}$。固定乘子在每个未倒置素数模下都非零。
若 $f$ 的系数有某个这样的素数分母，取最小公分母后模该素数，
两个非零多项式的乘积仍非零，不可能得到整分子。
这就是逐素数的 Gauss content 引理；故整交集强迫 $f\in R[t]$。
于是 (7) 是等式。$n<40$ 的零结论由同一有理典范公式及无挠性得到。$\square$

特别 $C_{1,j}=G_j$，$0\le j\le4$，正是原首40次五个整导子。
定理1给的是全部次数的准确整基，比仅知道某个导子乘归一化的返回更强。

## 3. 相对一个固定乘子的余源完全自由且显式

令 $n\ge0$、$m=n+1$。在 (6) 的 canonical 多项式坐标中，乘 $G_0$ 的原归一化像是
$$
\boxed{G_0\mathcal N_{R,n}
 = C_{m,0}\,R_n(t)R[t]_{\le d_n},}
\tag{11}
$$
其中
$$
\boxed{R_n(t)=(t h_7)^{\varepsilon_n}(t-1)^{\eta_n},\quad
\varepsilon_n=\mathbf1_{n\equiv1,2\ (4)},\quad
\eta_n=\mathbf1_{n\equiv1\ (3)}.}
\tag{12}
$$
这里 $R_n$ 的符号不表示系数环。证明只需准确除式
$$\frac{Q_{n+1}}{Q_1T_n}=R_n(t).$$
$1+8t$ 的指数在这个商中恒为零，不能额外保留或删除一个该点条件。

记 $r_n^{\rm rel}=\deg R_n=3\varepsilon_n+\eta_n$。有
$$\boxed{e_{n+1}=d_n+r_n^{\rm rel}+4.}\tag{13}$$
所以
$$
\boxed{\frac{(\mathfrak c_R)_{n+40}}{G_0\mathcal N_{R,n}}
\text{ 是自由 }R\text{ 模，秩 }4+3\varepsilon_n+\eta_n.}
\tag{14}
$$
一组明确的余基由以下原列给出：
$$
\boxed{C_{n+1,j},\quad
0\le j<r_n^{\rm rel}\quad\text{或}\quad
e_{n+1}-3\le j\le e_{n+1}.}
\tag{15}
$$
若 $r_n^{\rm rel}=0$，第一组为空。

**证明。** 在 $R[t]_{\le e_{n+1}}$ 中先减去最上面四个单项式，
再对 $R_n$ 作 Euclidean 除法。其首系数 $16^{\varepsilon_n}$ 在 $R$ 中可逆，
商的次数至多 $d_n$，余数次数小于 $r_n^{\rm rel}$，故 (15) 张成。
若一个 (15) 组合落在 $R_nR[t]_{\le d_n}$，最高四项先由次数比较为零，
余下低于 $\deg R_n$ 的余数又只能为零。这同时证明自由性和独立性。$\square$

每次相对缺口准确为4、5、7或8维，按模十二周期变化。
前四个方向是无穷处余量；低余数来自 $0$、两条CM7角点及1处的指定条件。
总的相对秩为 $35D/6+O(1)$，没有把它计成 $D^2$ 的新自由来源。
但 (15) 的每一列现在都有原幂格成员性、整系数及准确次数，均可实际用于有限目标修正。

## 4. 全部真实原点阶与最小的两条修正

令 $w=z^6$。由 (4)–(6) 得
$$
\boxed{\operatorname{ord}_w C_{m,j}=13+\lfloor m/4\rfloor+j.}
\tag{16}
$$
这是准确等式，因 $P_{134}(0)\ne0$；并非仅有消失阶下界。
首系数为
$$
P_{134}(0)(-b)^{13+\lfloor m/4\rfloor+j}
       (-1)^{15+\lfloor m/3\rfloor}7^{13+\lfloor m/4\rfloor}.
\tag{17}
$$
对本题惰性 $p>7,p\ne17$，它是单位：3159421为分裂素数，已由 R328 支付。
这证明在每个次数，(6) 不仅是整基，还是物理原点消失旗标的整适配基。

相对于 $G_0=C_{1,0}$，有尤其简单的全函数式
$$
\boxed{\frac{C_{n+1,j}}{G_0}
 =\rho^n\frac{
 t^{\lfloor(n+1)/4\rfloor+j}
 (t-1)^{\lfloor(n+1)/3\rfloor}
 h_7^{\lfloor(n+1)/4\rfloor}}
 {(1+8t)^{\lfloor n/2\rfloor}}.}
\tag{18}
$$
它来自 $A^nQ_1/Q_{n+1}$ 的准确指数抵消。
右端在原点整，其首系数在同一惰性素数处为单位。
特别
$$
\boxed{C_{2,0}=G_0\rho,\qquad
C_{3,0}=G_0\rho^2\frac{t-1}{1+8t}.}
\tag{19}
$$
两者的原权为41、42，物理首阶仍十三。
$\rho$ 或 $\rho^2$ 本身没有因此成为新的中央零来源；(19) 的合法性是左端已经属于原导子。

R331 用三个额外 $K_i$ 支付径向常数。现在 (19) 给更小的明确选择：
保留 $G_0$，只加 $C_{2,0},C_{3,0}$ 两列即可。
在相对 $G_0$ 的三径向常数上，模 $p$ 的矩阵为
$$
\boxed{\begin{pmatrix}
1&1&-1\\
0&a_p&-2a_p\\
0&a_p^2/2&-2a_p^2
\end{pmatrix},\qquad\det=-a_p^3\in\mathcal O^\times.}
\tag{20}
$$
这两列在 (14) 中是低余数列，因此相对于 $G_0\mathcal N$ 独立且 primitive。
当 $D\ge2$ 时已在原 $D+40$ 预算中。
原归一化像没有两条非零径向常数，所以少于两个新增列不可能补齐它们；
在这个准确意义下，(19) 是最小的原修正。

## 5. 整个导子在同一有限目标中的全深返回

这里保留 R328、R331 的条件
$$p=6s-1,\quad s>13,\quad 1\le\ell<s-13,\quad L=2s+\ell.$$
令 $g=e^{-\kappa w^s}\rho$、$a_p=p\kappa\in\mathcal O^\times$。
在原 $\Gamma_L$ 中，对每个 (18) 置
$$
\boxed{\mathcal Y_{n,j}=
g^n\frac{
 t^{\lfloor(n+1)/4\rfloor+j}
 (t-1)^{\lfloor(n+1)/3\rfloor}
 h_7^{\lfloor(n+1)/4\rfloor}}
 {(1+8t)^{\lfloor n/2\rfloor}}
 e_2(na_p\epsilon),\quad0\le j\le e_{n+1}.}
\tag{21}
$$
所有原高轴和 $w^s=p\epsilon$ 进位都按 R322 使用。
这是一份直接可用的完整有限矩阵，不需要解47次隐式关系，也不需要按列另付有理返回。

以 (21) 为列的矩阵记为 $\mathcal J_{\rm can,D}$，$0\le n\le D$。
同一 $G_0$ 给
$$
\boxed{\mathcal J_{L+13}|_{(\mathfrak c_{\mathcal O})_{\le D+40}}
       =c_*\mathcal U\,m_{13}\circ\mathcal J_{\rm can,D}.}
\tag{22}
$$
这里左右来源按定理1的实际整基认同；右边的相对次数 $n$ 与左边的原权 $n+40$ 始终区别。
普通级数先乘到 $w^{13}$ 后再截断的论证与 R328 完全相同。
所有 (18) 都在原点整，故未读高行不进入长度 $L+13$。

此外，$(\mathfrak c_{\mathcal O})_{\le D+40}$ 在
$\mathcal T_{\mathcal O,\le D+40}$ 中 primitive。
若 $px$ 属于该导子且 $x\in\mathcal T$，则 $x\in\mathfrak c_{\mathbf Q}$，
又 $x\in\mathcal N_{\mathcal O}$；R322 的整交集立即给 $x\in\mathfrak c_{\mathcal O}$。
于是对所有 $N\ge1$，
$$
\boxed{0\le
K_N(\mathcal J_{L+13}|_{\mathfrak c_{\le D+40}})
       -K_N(\mathcal J_{\rm can,D})\le26,}
\tag{23}
$$
且这些核 primitive 嵌入整个原幂格的相应模 $p^N$ 核。
因此整个导子中的任意深关系仍只用一次固定charge40和原十三行成本。
这没有把26条跨界带删去，也没有声称 (21) 的未知 Smith 尾已经算完。

R331 的联合三列像是 (21) 的真子像；(14)、(15) 给出从单一 $G_0\mathcal N$
补到整个 (21) 的所有实际原列。提升类现在可以在这个完整的、已付原来源像中求解。
若仍有类不在像中，那才是这一整套导子修正之后的真实有限目标障碍。

## 6. 五径向块也有完整支付的原单位矩阵

本节给 R324 五块一个直接可用的原来源，不以三块结果冒充五块。
利用已经支付的 $G_j=C_{1,j}=t^jG_0$，取
$$
\boxed{H_j=G_jA^{4-j},\qquad0\le j\le4.}
\tag{24}
$$
它们全属于原 $\mathcal T$，权数为 $44-j$，物理首阶全为十七。
除去共同的 $G_0w^4$ 后，五个首系数为
$(-b)^j(7b)^{4-j}$，相对 charge 为 $4-j$。
所以五径向常数的实际矩阵模 $p$ 的行列式是
$$
\boxed{7^{10}b^{20}a_p^{10}\in\mathcal O^\times.}
\tag{25}
$$
证明与 R331 的连续 charge Vandermonde 完全一样：
五个连续整数的 Vandermonde 与 $0!1!2!3!4!$ 准确抵消，
反向排列的符号为 $(-1)^{10}=1$。

为付全部物理范围，取 $s>18$，源长度为 $5s$，目标长度为 $5s+17<p$。
R324 的实际删首 Gaussian 整性覆盖这个完整范围；所需指数展开只到
$\epsilon^5$，其阶乘在当前素数为单位。
先乘 $w^{17}$ 的运输在每条源行上准确乘
$$p^{\lfloor(r+17)/s\rfloor-\lfloor r/s\rfloor},\qquad0\le r<5s.$$
它有五条各十七行的跨界带，总指数为85。
因此这个五块原修正保留完整目标后的全部精度核长度差在0与85之间。

特别，R324 的原强迫行 $w^{5s-1}$ 被送到 $w^{5s+16}$，
恰好仍在所付的新目标内，并在这一次跨界中再付一个 $p$。
不能因为只看旧五块便把它说成消失，也不能用 (25) 的常数单位 minor
替代这条完整高行的处理。

## 7. 证书及继续的实际对象

[check-jzero-full-canonical-conductor-basis.py](../scripts/check-jzero-full-canonical-conductor-basis.py)
及其 JSON 精确验证固定 primitive 分子 (2)–(4)、其全部整数系数，
以及 (8)–(13) 的十二个剩余类。
增加十二使相关 floor/ceil 指数分别增加9、6、8，次数增加47，
所以这十二类与正文证明覆盖全部次数，不是有限次数经验外推。
原全次数饱和、典范模和所有精度运输分别由既有完整证明与上文给出。

后继的指定对象是 (21) 的完整像、它的真实整 Schur 余块及其 Bockstein 类。
R334 所研究的原首中央参数和确定 harmonic carry，必须投影到这个已经支付的原像中；
本篇没有令任何新增 $C_{m,j}$ 的中央导数为零。

依赖：[R322](R322-three-true-zero-weighted-saturation-and-original-q2-kernel.md)、
[R324](R324-original-u-connection-first-forced-row-and-five-block-smith.md)、
[R325](R325-three-true-zero-weighted-normalization-and-conductor.md)、
[R326](R326-original-weighted-conductor-integral-generators-and-uniform-return.md)、
[R328](R328-original-conductor-thirteen-shift-and-normal-image-obstruction.md)、
[R329](R329-fourteen-generator-normalization-and-full-conductor-matrix.md)、
[R331](R331-three-original-conductor-corrections-and-paid-unit-schur.md)。
