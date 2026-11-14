# R466 — 固定二倍 division-log 的五条真实 sextic 来源与新秩至少二曲线

日期：2026-11-14。**状态：固定二倍来源的全纯性、完整 CM7/19
分解、五条原 2/3/17 Schwartz 身份、全权 Yang 平方、一个明确整
来源组合及新曲线的代数秩下界均已证明。新曲线是**
$$
\boxed{E_{\rm new}:y^2=x^3+2312,\qquad
       \operatorname{rank}E_{\rm new}(\mathbf Q)\ge2.}                 \tag{1}
$$
**它不是旧 $j=1728$ 池中的 $y^2=x^3-2312x$。**
本篇没有把零质量换成非零中央导数，也没有删除两个 division-log
来源的其余六个外谱。主课题的无穷素数结论仍未由本篇单独推出。

## 1. 固定二倍单位及两条完整全纯来源

采用 R307、R460、R463 的同一规范：
$$
E_b:y^2=x^3+b,\quad \delta^2=-3,\quad
\omega=(-1+\delta)/2,\quad X=x^3,\quad
x=z^{-2}+\cdots,\ y=-z^{-3}+\cdots,\ \sigma=z+\cdots .
                                                                    \tag{2}
$$
令 $C_{13},C_{15}$ 是 R460 的两条实际奇伴随，准确写成
$$
C_i=\sigma^{34}y\sum_{j=1}^{5}P_{i,j}b^{4-j}X^j,                     \tag{3}
$$
其中
$$
\begin{aligned}
(P_{13,1},\ldots,P_{13,5})
 &=\left({10880\over14847},-{13504\over14847},{6269\over9898},
          -{6523\over59388},-{37\over33936}\right),\\
(P_{15,1},\ldots,P_{15,5})
 &=\left({923\over1470},{107\over5880},{11399\over15680},
          -{15919\over94080},-{37\over53760}\right).
\end{aligned}                                                       \tag{4}
$$
这里保留 $j=5$ 的 $b^{-1}$，不改其原连接定标。

由真正的倍点与 $\delta$ 同源公式，
$$
r_2={\sigma(2z)\over\sigma(z)^4}=-2y,\qquad
u_2={r_2(\delta z)\over r_2(z)}
 ={X-8b\over\delta^3X},\qquad
R_2=\partial_z\log u_2={48by\over x(X-8b)}.                            \tag{5}
$$
固定来源为
$$
\boxed{W_i(z)=R_2(z)C_i(2z)\in\mathcal S_{136},\qquad i=13,15.}       \tag{6}
$$
本篇的 $W_i$ **没有**另除二。

设 $D$ 为非零 $\delta$-核的两个点之和。R463 的完整除子式给
$\operatorname{div}u_2=[2]^*D-4D$；也可直接由 (5) 读出。
$R_2$ 的全部极都是这些点上的简单极，而 $C_i$ 在 $D$
各有至少三阶零。因此 $C_i(2z)$ 支付了所有极，(6) 是全局
全纯截面。其 $\mu _6$ 类型为零。

用
$$
x(2z)={x(X-8b)\over4(X+b)},\qquad
y(2z)={X^2+20bX-8b^2\over8y^3}
$$
得到完整有理多项式
$$
\boxed{\begin{aligned}
{W_i\over\sigma^{136}x^2}
={}&3\,2^{35}b(X+b)(X^2+20bX-8b^2)\\
&\cdot\sum_{j=1}^{5}
 P_{i,j}b^{4-j}2^{-6j}
 (X+b)^{15-3j}X^{j-1}(X-8b)^{3j-1}.
\end{aligned}}                                                       \tag{7}
$$
右边总齐次权为二十一，次数恰二十一，故两个 $W_i(0)=0$。

还有一个完整来源迹，而不只是中央质量：
$$
\boxed{\frac14\sum_{t\in E[2]}T_t^{(136)}W_i=0.}                     \tag{8}
$$
事实上 canonical $E[2]$ 平移逐项固定 $C_i(2z)$；由
$(2,\delta)=1$ 的原单位范数，$\operatorname{Norm}_{[2]}u_2=1$，
所以 $\sum_{t\in E[2]}R_2(z+t)=0$。这也明确保留了四个真实
分支，没有把某一条 division-log 当成常数。

## 2. 完整有限 CM 块与被保留的外谱

记
$$
\gamma _7=3+\omega=(5+\delta)/2,\quad
\gamma _{13}=4+\omega,\quad \gamma _{19}=5+2\omega=4+\delta,\quad
N_\ell={[\gamma_\ell]_*[\bar\gamma_\ell]^*\over\gamma_\ell}.
                                                                    \tag{9}
$$
它们是实际 pull/trace，没有另外的 projective 定标。
整个 principal 空间是
$$
\mathcal H_{136}^{+}
 =\sigma^{136}x^2K[X]_{\le22},\qquad \dim=23.                         \tag{10}
$$
第 22 列正是原点质量，不能漏掉。

R464 的同一精确纤维方法在 (10) 给出完整 $23\times23$
$N_7$ 矩阵；数据见
[完整矩阵](../notes/2026-11-14-theta-degree136-cm7-exact.json)。
所有二十三列均由真实七点纤维、保留全部 sigma frame 的迹确定。
本篇在该特征零矩阵上核得
$$
N_7^{18}=I,\qquad N_7^9W_i=W_i,\qquad
\dim_K\langle W_i,N_7W_i,\ldots,N_7^8W_i\rangle=9.                   \tag{11}
$$
故每个 $W_i$ 的最小多项式恰为 $t^9-1$。

六条 $\mu _6$ 特征的完整空间维数为
$$
\begin{array}{c|rrrrrr}
\lambda&1&\omega&\omega^2&-1&-\omega&-\omega^2\\ \hline
\dim\ker(N_7-\lambda)&2&1&2&1&1&1 .
\end{array}                                                         \tag{12}
$$
对每个 $W_i$，后三条投影都是**整条来源零**，前三条都非零。
此外 $t^3-\omega$、$t^3-\omega^2$ 两个外部三次谱也全部出现，
各给三维循环块。旧三条负特征为零不等于没有新的算术来源。

全空间上的正 $\mu _3$ 投影可写作
$$
\mathcal P={1\over6}\sum_{j=0}^{5}N_7^{3j},\qquad
\dim\operatorname{im}\mathcal P=5.                                  \tag{13}
$$
在已付的 $N_7^9=1$ 块上，它才简化成
$$
P_+={I+N_7^3+N_7^6\over3}.                                         \tag{14}
$$
后文只对该块中的 $W_i$ 使用 (14)；不把 (14) 当成整个
二十三维空间上的投影。

### 2.1 第二个真实 CM 算子区分重数

在完整中心模 $2\cdot136=272$ 中，用 $a+b\omega$ 的数对记号，
$$
g_7=(40,195),\quad g_{13}=(43,147),\quad g_{19}=(87,144),
$$
$$
g_{13}=-g_7^{23},\qquad
g_{19}=33(-\omega)g_7^2.                                            \tag{15}
$$
数 $33$ 模十六为一、模十七为负一；它是独立的十七处反射。
取完整 theta 结构中的
$$
D_{33}e_j=e_{33j},\qquad 33^2\equiv1\pmod{272}.
$$
其在原 $[2]$ 拉回的基
$v_j=e_{2j}+e_{2j+68}$ 上送 $v_j$ 到 $v_{-j}$，所以
$D_{33}S(2z)=S(2z)$。

Heisenberg 协变和不可约性把 (15) 提升为相差共同标量的
真实算子。原 $S(2z)$ 给绝对锚：
$$
N_7S(2z)=-S(2z),\quad N_{13}S(2z)=-S(2z),\quad
N_{19}S(2z)=\omega S(2z).                                           \tag{16}
$$
最后一式既由原 Hecke 角色给出，也可用
$\#E_{17}(\mathbf F_{19})=27$ 及所选 $\gamma_{19}$ 校准：
唯一迹为负七的单位倍为 $\omega\gamma_{19}$。
因此在整个 principal 空间上
$$
\boxed{N_{13}=N_7^{23},\qquad
       N_{19}=\omega D_{33}N_7^2.}                                  \tag{17}
$$
这里 $N_{13}$ 的全空间式为 $R_{-1}N_7^{23}$；
principal 偶性才去掉 $R_{-1}$。

为独立核定 (17) 在本篇实际五维块的常数，证书还计算了
完整的五个十九点纤维。先从
$\sigma(\gamma_{19}z)/\sigma(z)^{19}$ 的真实除子，确定
$\gamma_{19}(x^9+c_1x^6+c_2x^3+c_3)$；四个 Laurent 系数
确定的是整个有限极空间中的函数。两个互素 CM pull/trace
对易，故 $N_{19}$ 保持 $\operatorname{im}\mathcal P$。
五个精确求值给该闭合五维块的完整矩阵，不是采样猜本征值。
计算得到 $N_{19}^6=I$，以及 (17) 给出的 $D_{33}^2=I$；
其正、负空间维数为三、二。

## 3. 五条候选的完整有限角色

现在独立构造真正的算术来源，随后才与 (13) 识别。令
$$
\boxed{D_k=8(-17)^k,\quad E_k:y^2=x^3+D_k,\quad 1\le k\le5.}          \tag{18}
$$
若 $\psi_k$ 为解析微分 CM type 的角色，Silverman–Stange
的六次剩余式给
$$
{\psi_k\over\psi_1^{\rm base}}
 =\left({2(-1)^k\over\cdot}\right)_2
  \left({17\over\cdot}\right)_6^{-k}.                                \tag{19}
$$
右边第一项是有理二次角色拉到 $K$；在本地 idèle 上是相应
有理角色与 $N_{K_v/\mathbf Q_v}$ 的复合。理想/单位方向沿用
R290，不能把十七处的单位幂改成负幂。

设 $\varepsilon_q$ 为 $\mathbf Q_2$ 的二次角色，$q=\pm2$。
完整坏点表为
$$
\begin{array}{c|c|c}
v&\chi_{k,v}\text{ 在单位上的值}&\text{uniformizer 值}\\ \hline
2&\operatorname{Teich}_{\mu _3}(u\bmod2)\,
      \varepsilon_{\,2(-1)^k}(N u)&\chi_{k,2}(2)=-1\\
3&u\bmod\delta\in\{\pm1\}&\chi_{k,3}(\delta)=-i\\
17&(u\bmod17)^{48k}&\chi_{k,17}(17)=-1 .
\end{array}                                                         \tag{20}
$$
理由包括：$17$ 是 $\mathbf Q_2$ 的六次幂；
$-17\in1+9\mathbf Z_3$ 是 $\mathbf Q_3$ 的六次幂，而 $8$
在三处给与原 $E_{17}$ 相同的未分歧二次扭曲；$2,-1$ 在
$\mathbf Q_{17}$ 都为平方，所以 (18) 的固定因子在十七处
不改变原 $k$ 次角色。主 idèle $17$ 的积关系给表中最后
一个负号。

因此
$$
\boxed{\mathfrak f_{\psi_k}=(8\delta\cdot17),\quad
       N\mathfrak f_{\psi_k}=55488,\quad N_{E_k}=166464.}              \tag{21}
$$
这里 $k=0$ 不在此表内：其十七处角色未分歧，不能混作第六条
同 conductor 来源。

### 3.1 Hermitian 类仍为十七

在 Yang 原负有限加性角色及 $\psi_K/2$ 下，二处 conductor
为三，Tate 公式可取 $c=4$。在
$\mathcal O_K/8=\{a+b\omega\}$ 上完整求和，得到
$$
\sum_{u\bmod8}^{\times}\chi_{k,2}(u)^{-1}
 e^{-2\pi i\operatorname{Tr}(u)/8}
 =\begin{cases}8,&k\text{ 奇},\\-8,&k\text{ 偶}.\end{cases}           \tag{22}
$$
同时 $\chi_{k,2}(\delta)=1,-1$ 分别对应奇、偶 $k$，故
二处 epsilon 乘该值始终为正一。

十七处角色和的零 trace 纤维为 $16(-1)^k$，其余每个纤维
为 $-(-1)^k$，所以 Gauss 和为 $17(-1)^k$。
乘 uniformizer 值负一及 $\chi_{k,17}(\delta)=(-1)^k$，
仍得负一。三处和原 R290 相同，得负一；无穷处为正一。
于是全部局部条件准确为
$$
(+1,-1,-1,+1)\quad\text{于 }(2,3,17,\infty),\qquad
\boxed{\alpha=17,\quad\kappa=51\sqrt3.}                              \tag{23}
$$

## 4. 二处整个 norm-one 群的真实偶、奇向量

不能把 R393 在偶函数上可改写的核直接套到奇函数。本节保留
完整交叉项。令
$$
g_*={1+2\delta\over1-2\delta},\qquad
\iota_{17}(x+y\delta)=
\begin{pmatrix}x&153y\\-y/51&x\end{pmatrix}.
$$
$-1,\omega,g_*$ 拓扑生成 $K_2^1$：其 principal 部分由
$\log g_*=4\delta$ 乘二进单位生成，其余为 $\mu _3$ 和负号。
Yang Appendix (A1)–(A3) 的实际 splitting 给两个二次扭曲共同的
$$
\mu(\omega)=-\omega^2\zeta_8,\quad
\mu(\omega^2)=-\omega\zeta_8^{-1},\quad
\mu(g_*)=\zeta_8.                                                    \tag{24}
$$
例如 $N(\delta(g_*-1))=144/13$，两种二次角色在此都为负一，
将原未扭曲的 $\zeta_8^{-3}$ 改成 $\zeta_8$。
比较 $-g_*$ 则必须保留
$$
W_{-1}=R\quad(q=-2),\qquad W_{-1}=-R\quad(q=2),\qquad
R\phi(u)=\phi(-u).                                                   \tag{25}
$$
因为 $N(\delta(-g_*-1))=12/13$，两种扭曲在这里取相反值。

设 $v(a)=\phi(a/4)$，保留整个实际八维条件
$$
\operatorname{supp}\phi\subset\tfrac14\mathbf Z_2,\quad
\phi\text{ 以 }4\mathbf Z_2\text{ 为周期},\quad
v(a+8)=(-1)^av(a).                                                   \tag{26}
$$
完整 Rao 核分别为
$$
{1\over\sqrt2}\int
 \psi_2\!\left({51\over2}(u^2+4uv+v^2)\right)\phi(v)\,dv,
$$
$$
2\int\psi_2\!\left({17\over8}
 (33u^2+78uv+33v^2)\right)\phi(v)\,dv .                               \tag{27}
$$
各式还乘 (24) 的相应 $\mu$。第一式的输出在
$\tfrac18\mathbf Z_2\setminus\tfrac14\mathbf Z_2$ 由 (26) 准确
相消，未遗漏更大的支撑。

在 $a,b=0,\ldots,7$ 的实际坐标中，
$$
(W_\omega)_{ab}={-\omega^2\zeta_8\over2\sqrt2}\,
 \zeta_{32}^{-51(a^2+b^2+4ab)}.                                     \tag{28}
$$
$W_{g_*}$ 固定四个奇指标，交换 $0,4$ 并取正号，交换
$2,6$ 并取负号。完整相位来自 (27)，不是只给出射影置换。

取
$$
h_+=\mathbf1_{\mathbf Z_2},\qquad
h_-=\mathbf1_{1/2+2\mathbf Z_2}
       -\mathbf1_{-1/2+2\mathbf Z_2},\qquad
\phi_\pm=(I+W_\omega+W_{\omega^2})h_\pm.                             \tag{29}
$$
两个 $h_\pm$ 都被 $W_{g_*}$ 固定；其普通奇偶性分别为正、
负。因此 (24)–(29) 支付了整个 $K_2^1$：
$\phi_+$ 是 $q=-2$ 的原不变向量，
$\phi_-$ 是 $q=2$ 的原不变向量。

为使全部十六陪集可直接复核，记
$\chi_4(a)=(-1)^{(a-1)/2}$（$a$ 奇），则
$$
v_+(a)=
\begin{cases}
1,&a\equiv0\pmod4,\\
0,&a\equiv2\pmod4,\\
(\omega^2\zeta_{32}^{a^2}+\omega\zeta_{32}^{-a^2})/\sqrt2,&a\text{ 奇},
\end{cases}                                                         \tag{30}
$$
$$
v_-(a)=
\begin{cases}
0,&a\equiv0\pmod4,\\
\chi_4(a/2),&a\equiv2\pmod4,\\
-{\chi_4(a)\over\sqrt2}
 (\omega^2\zeta_8^3\zeta_{32}^{a^2}
  +\omega\zeta_8^{-3}\zeta_{32}^{-a^2}),&a\text{ 奇}.
\end{cases}                                                         \tag{31}
$$
它们都是实函数，分别偶、奇，并均满足 (26)。
原自对偶测度 $\operatorname{vol}(\mathbf Z_2)=1$ 给
$$
\boxed{\|\phi_+\|^2=\|\phi_-\|^2=3.}                                 \tag{32}
$$
这也由 $h_\pm$ 的支撑分别与两个旋转项的支撑不相交、
再用酉性将两旋转项的内积化回 $\langle h_\pm,W_\omega h_\pm\rangle=0$
直接得到。
证书在 $\mathbf Q(\zeta_{96})$ 中逐项核 (22)、(28)–(32)，
包括 $W_\omega^3=I$ 和两个 torus 生成元对易。

## 5. 十七处五条原角色及三处原球

保持 R290 的同一有限 Weil 模型
$e_a=\mathbf1_{a/17+\mathbf Z_{17}}$，其原矩阵为
$$
W(x+y\delta)_{ab}
 =-{(y/17)\over\sqrt{17}}\,
 \zeta_{17}^{\,3\{x(a^2+b^2)-2ab\}/(2y)},\qquad y\ne0.               \tag{33}
$$
取 $g_0=2+4\delta$，阶为十八。必须保留原 splitting 的缺失
二次角色，所以真正的五条有限角色是
$$
\tau_k(g)=g^{9+3k},\qquad
\tau_k(g_0)=-(-\omega^2)^k,\qquad
\Pi_k={1\over18}\sum_{j=0}^{17}\tau_k(g_0)^{-j}W(g_0^j).              \tag{34}
$$
定义真实规范向量
$$
f_k=9\sqrt{17}\,\Pi_k e_0\quad(k\text{ 奇}),\qquad
f_k=9\sqrt{17}\,\Pi_k(e_1-e_{-1})\quad(k\text{ 偶}).                  \tag{35}
$$
原有限 Gauss 运算证明每条重数一、(35) 非零且实，奇偶性为
$(-1)^{k+1}$。尤其 $k=2,4$ 的两个奇向量并未被偶投影
错误地删掉。只有 $k=0$ 对应缺失的 $g^9$。

记 $n_k=\sum_a|f_k(a)|^2>0$；其精确代数值随证书保存。
对于奇 $k$，仍为 R306 的
$$
n_1=n_5=9(17-\sqrt{17}),\qquad n_3=9(17-4\sqrt{17}).
                                                                    \tag{36}
$$
偶 $k$ 的规范是 (35)，不把它们的范数换成 (36)。
三处则保持原 $\phi_3=\mathbf1_{3^{-1}\mathbf Z_3}$，范数三。
所有其余有限点为原标准球。

## 6. 实际全局 Hermite 来源、周期和全权平方

由 (29)、(35) 的支撑，整个原有理支撑恰为 $x=n/204$，
实际有限系数为
$$
\boxed{
a_{k,n}=v_{(-1)^{k+1}}(11n\bmod16)\,f_k(10n\bmod17).}                \tag{37}
$$
这里 $51^{-1}\equiv11\pmod{16}$、$12^{-1}\equiv10\pmod{17}$，
两个逆元均不能省去。真实系数非零，实且偶，并满足
$$
a_{k,n+272}=a_{k,n},\qquad
a_{k,n+136}=(-1)^n a_{k,n}.                                        \tag{38}
$$

用 Yang 的原 Hermite 规范
$\sum H_m(x)T^m/m!=e^{xT-T^2/(8\pi)}$，定义
$$
b_{k,m}=\sum_{n\in\mathbf Z}a_{k,n}
 H_m\!\left({\sqrt\kappa\,n\over204}\right)
 e^{-\pi\sqrt3 n^2/816},\qquad \kappa=51\sqrt3.                       \tag{39}
$$
整个有理 $\mu _6$ Weil 不变性给 $b_{k,m}=0$ 若 $6\nmid m$。
两处奇向量在偶 $k$ 时相乘为偶，这一步保留了原奇支的符号。

设 $\tau_0=\delta/3$、$s=(1+\tau_0)/2$、$\Lambda=\mathbf Z+s\mathbf Z$。
置
$$
F_k(Z)=\sum_n a_{k,n}e^{\pi i\tau_0 n^2/272+2\pi inZ},\qquad
h={\sqrt\kappa\over408\pi i}.
$$
由 (38) 完整重新编号得到
$$
F_k(Z+s)=e^{-136\pi i s-272\pi i Z}F_k(Z),\qquad F_k(Z+1)=F_k(Z).
$$
所以
$$
\boxed{\mathscr S_{k,\Lambda}(Z)=e^{136\sqrt3\pi Z^2}F_k(Z)
       \in H^0(\Lambda,\mathcal O(136O)),\qquad
       \mathcal B_k(T)=\mathscr S_{k,\Lambda}(hT).}                   \tag{40}
$$
因为 $136\sqrt3\pi h^2=-1/(8\pi)$，这是同一个真实 Gaussian，
没有指数补项或未指定的半特征。

全部合法权 $6\mid m$ 上，有限角色及原向量保持，完整范数为
$$
\mathcal N_{k,m}={9n_k\over\sqrt{102\sqrt3}}\,
                   {m!\over(4\pi)^m}.
                                                                    \tag{41}
$$
Yang 的 $S_1=\{2,17\}$、$S_2=\varnothing$，
$c(0)=17/27$，单位群和商体积同 R306。故
$$
\boxed{
L(\psi_k^{\,2m+1},m+1)
 =C_k{(4\pi)^m\over m!}b_{k,m}^{\,2},\qquad
C_k={\pi\sqrt{102\sqrt3}\over51\sqrt3\,n_k}>0,\quad 6\mid m .
}                                                                   \tag{42}
$$
本篇是从全部原向量支付 (42)，不从拟合到的多项式倒推
“一定存在”某条 Hecke 角色。

## 7. 完整局部数据识别五条实际代数线

现在把 (40) 放入 (10)。用原 $S(2z)$ 的绝对锚比较公共
Heisenberg 交织子，二处比值来自 (20)，十七处比值来自 (34)。
对 $g_\ell=\gamma_\ell/\bar\gamma_\ell$，
$$
N(\delta(g_7-1))=9/7,\qquad
N(\delta(g_{19}-1))=36/19,\qquad
g_7\bmod17=g_0,\quad g_{19}\bmod17=g_0^8.
                                                                    \tag{43}
$$
因此 $\varepsilon_{2(-1)^k}(7)=(-1)^k$、
$\varepsilon_{2(-1)^k}(19)=(-1)^{k+1}$，而三处公共向量不变。
逐项比较给
$$
\boxed{
N_7\mathscr S_k=\omega^{2k-2}\mathscr S_k,\quad
N_{19}\mathscr S_k=(-1)^{k+1}\omega^k\mathscr S_k,\quad
D_{33}\mathscr S_k=(-1)^{k+1}\mathscr S_k .
}                                                                   \tag{44}
$$
这是完整有限角色的推论；三处计点只用于 (16) 的共同绝对标量，
不承担曲线身份。

完整五维矩阵证明 (44) 的五个共同特征空间都恰一维。
故 (40) 的五条非零原 Schwartz 来源和 (13) 中的五条线一一
对应。具体如下；质量是投影 $W_i$ 的质量，在一般 $b$
还须将表中各数除以 $b$：
$$
\begin{array}{c|r|c|c|c|c}
k&D_k&N_7&N_{19}&(\Pi_kW_{13})(0)\ (b=1)&
                          (\Pi_kW_{15})(0)\ (b=1)\\ \hline
1&-136&1&\omega&-25/801738&-25/508032\\
2&2312&\omega^2&-\omega^2&0&0\\
3&-39304&\omega&1&109/1603476&109/1016064\\
4&668168&1&-\omega&37/133623&37/84672\\
5&-11358856&\omega^2&\omega^2&-29/1603476&-29/1016064
\end{array}                                                         \tag{45}
$$
表中所有十个完整投影都非零，包括质量为零的一行。
记号 $\Pi_k$ 在这里表示由 (44) 对应的**实际代数来源**
共同投影，区别于 (34) 的十七处单因子投影；两者经刚证明的
原来源识别相容。

由 (42) 的零权及 CM 非零中央值迫代数秩零的定理，表中其他
四条曲线确有秩零。这是四条已识别来源的非零质量结论；
它们的中央导数仍未知。

## 8. 一个明确整组合抽出新来源，保留全部六个外谱

四条非零质量线上的**整条函数**均满足
$$
101\Pi_kW_{13}=64\Pi_kW_{15}\quad(k=1,3,4,5).
                                                                    \tag{46}
$$
零质量线则有精确的非同比系数：
$$
\boxed{\Pi_2W_{13}=-{81328\over6363}S_{\rm new},\qquad
       \Pi_2W_{15}=-{20527\over2520}S_{\rm new}.}                     \tag{47}
$$
于是
$$
\boxed{
S_{\rm new}=-{5\over3848}\,
P_+(101W_{13}-64W_{15}),\qquad
S_{\rm new}(z)=z^6+O(z^{12}).}                                      \tag{48}
$$
系数 $-3848/5=-8\cdot13\cdot37/5$ 在本公式中准确保留。
$W_*=101W_{13}-64W_{15}$ 的完整循环维数为七；
$(I-P_+)W_*$ 的循环维数为六，质量虽为零而来源不为零。
(48) 没有把这些外谱丢弃为中央零。

首项一的来源有如下简洁完整因式；各块按 $X,b$ 齐次恢复：
$$
\boxed{\begin{aligned}
{S_{{\rm new},b}\over\sigma^{136}x^2}
={1\over91}&(X+b)(X^2+20bX-8b^2)(7X^2-4bX+16b^2)\\
&\cdot(X^4+40bX^3+2112b^2X^2+3136b^3X+1792b^4)\\
&\cdot(13X^4+52bX^3+1536b^2X^2+1024b^3X+256b^4)\\
&\cdot(X^8+1232bX^7-58688b^2X^6-49408b^3X^5\\
&\hspace{13mm}-439040b^4X^4-2111488b^5X^3
-1949696b^6X^2\\
&\hspace{13mm}-851968b^7X-32768b^8).
\end{aligned}}                                                       \tag{49}
$$
总次数二十一，最高系数 $7\cdot13/91=1$，所以首 $z^6$
确为一。公式由整个二十三列多项式恒等式核定，不由若干
Taylor 系数猜测。

## 9. 新曲线的两个有理点严格独立

在 (1) 上取
$$
P=(17,85),\qquad Q=(34,204),\qquad K'=\mathbf Q(r),\quad r^2=2.
$$
设 $\rho=5+2r$、$\bar\rho=5-2r$、$\epsilon=1+r$。
它们满足
$$
N\rho=17,\quad
\alpha(P):=85+34r=\rho^2\bar\rho,\quad
\alpha(Q):=204+34r=r^3\epsilon\rho\bar\rho^2,
$$
$$
\boxed{\alpha(P)\alpha(Q)=(17r)^3\epsilon.}                          \tag{50}
$$

这里 $\alpha(x,y)=y+34r$ 在 $K'^\times/K'^{\times3}$ 中是
真实的三同源 Kummer 同态。可不用引用下降程序直接核同态：
若直线 $y=mx+c$ 与曲线交于三点 $P_i$，其横坐标满足
$f(x)=x^3-(mx+c)^2+2312$；代入
$x=-(c+34r)/m$，得到
$$
\prod_{i=1}^{3}(y(P_i)+34r)=(c+34r)^3.
$$
同时
$\alpha(R)\alpha(-R)=-x(R)^3$ 是立方，故弦切群律给所称同态；
切线、垂线由同一式或极限处理。原有理点没有 $x=0$ 的例外。

$\rho,\bar\rho$ 是十七之上的两个不同素元。
若 $\alpha(P)^a\alpha(Q)^b$ 为立方，两个赋值给
$$
2a+b\equiv a+2b\equiv0\pmod3,
$$
所以 $a\equiv b\pmod3$。再由 (50)，必须
$\epsilon^a$ 是立方。可是 $\epsilon$ 不是 $K'$ 的立方：
若 $(A+Br)^3=1+r$，根的整性给 $A,B\in\mathbf Z$，
比较 $r$ 系数得 $B(3A^2+2B^2)=1$，不可能。
故 $a\equiv b\equiv0\pmod3$。

最后 $E_{\rm new}(\mathbf Q)[3]=0$。其三除法多项式为
$3x(x^3+9248)$：$x=0$ 要求 $2312$ 是平方，
另一项要求 $-9248=-2^5 17^2$ 是有理立方，均不成立。
若 $mP+nQ=0$，前述 Kummer 独立性先迫 $3\mid m,n$，
无有理三 torsion 再给除以三后的关系；无限下降迫 $m=n=0$。
因此 (1) 的秩下界完全不依赖 Sha、数值高度或解析秩猜测。

## 10. 同一现有 ray 上的完整 scalar core

沿 R454 已固定的 ray，完整 theta 群的中心仍按模 272 读取。
其实际 ordinary core 的 Heisenberg 元素为
$$
g_p=(203,136)=g_7^9.
$$
用 $S(2z)$ 的原锚
$K_{136}S(2z)=S(2z)$、$N_7^9S(2z)=-S(2z)$，
不可约性确定整个空间的绝对式
$$
\boxed{K_{136}=-N_7^9.}                                             \tag{51}
$$
因此 $W_{13},W_{15}$ 和五条 (44) 全部满足 $K_{136}=-1$。
在原 $b=17$ theta 测度的共同规范
$\lambda=-1/\bar\pi_0,\ \kappa=p/\bar\pi_0^2$ 中，
$$
\boxed{\nu_{S_{\rm new}}|_{p\mathbf Z_p}
       =-\lambda[\kappa]_*\nu_{S_{\rm new}}.}                        \tag{52}
$$
这是真正整条来源关系；没有从一个 principal 数字倒定 core。
把 (52) 改写为新曲线自己的 primitive Euler 因子时，仍须使用
其实际 $\psi_2$ 与 Frobenius，不可只因共用 theta 坐标而令
新 $\pi$ 等于旧 $\pi_0$。

## 11. 给后续算术桥的准确尺度与保留项

共同 $b=17$ 方程到 $E_{2312}$ 的正实尺度为
$$
u=136^{1/6},\qquad
\boxed{S_{{\rm new},2312}(z)=u^{-6}S_{{\rm new},17}(uz),\qquad
       \Omega_{2312}=\Omega_{17}/u.}                               \tag{53}
$$
(49) 的总权二十一直接证明首个式子；首 $z^6$ 归一保持。
原 Hermite 尺度为 (40) 的 $h$，不能误用旧 degree34 的
$\sqrt\kappa/(204\pi i)$。

若把原 $\mathscr S_{2,\Lambda}$ 与首项一物理来源相比，其
准确 raw scalar 可定义为
$$
\mathscr S_{2,\Lambda}(Z)
 =c_D\,S_{{\rm new},2312}(\Omega_{2312}Z),\qquad
c_D={b_{2,6}\over720h^6\Omega_{2312}^6}\ne0.                         \tag{54}
$$
式 (42)、(49) 保证该首项非零。需要一个固定代数平方常数时，
应对 $C_2c_D^2/\Omega_{2312}$ 作完整 CM period 代数归一；
不能单独无证把 raw $c_D$ 称为代数数。具体 Katz/Euler/全
Selmer 的返回由后续 R469 支付，本篇不重复或预支这些步骤。

本篇给主线新增的内容是：一条**已识别的固定秩至少二曲线**、
其完整正权 theta 来源、原 norm-two division-log 中实际可取
的整组合、以及同一 ray 上的真实 core。尚未证明其 p-adic
中央导数在无穷多个 $p$ 非零；四条秩零来源的中央导数和六个
外谱的中央量也全部保留。

## 证书与来源

- [check-r466-fixed-two-division-source.py](../scripts/check-r466-fixed-two-division-source.py)
  及同名 JSON：从 (7) 构造两源，核完整 CM7 谱、五个真实 CM19
  纤维及六个mu6投影；其完整五维矩阵给(44)–(47)的共同特征线。
  (48)–(49)的整组合/因式另由R470脚本在全部二十三坐标中保存。
  CM7 输入为已付二十三列的
  [特征零完整矩阵](../notes/2026-11-14-theta-degree136-cm7-exact.json)。
- [check-r466-original-dyadic-sextic-data.py](../scripts/check-r466-original-dyadic-sextic-data.py)
  及同名 JSON：六十八项精确检查，包括完整 dyadic Gauss、
  偶/奇 Rao 矩阵、两个范数三、五个原十七处投影、支撑逆元
  和新曲线的 Kummer 恒等式。
- R307、R460、R463 提供 (3) 的原连接身份和 division-log
  规范；R290、R306、R393 提供已付加性角色、Heisenberg
  结构与 Yang 全局测度。本篇对新增奇 dyadic 来源重新计算，
  没有只引用偶来源的核。
- J. H. Silverman and K. E. Stange, *Amicable Pairs and Aliquot
  Cycles for Elliptic Curves*, Experimental Math. **20** (2011),
  329–357，§6、Theorem 19 证明中的六次角色式；
  [作者全文](https://arxiv.org/pdf/0912.1831)。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of
  certain elliptic curves*, Compositio Math. **117** (1999), 337–359，
  Lemma 1.1、Proposition 1.2、Proposition 1.5、Appendix (A1)–(A3)；
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)。
  本篇已重新打开作者原文核 A1–A3，尤其保留奇函数的完整核。
- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew.
  Math. **485** (1997), 25–53，Theorem 1.11、Corollary 2.14；
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
- K. Rubin, *Elliptic curves with complex multiplication and the
  conjecture of Birch and Swinnerton-Dyer*, Invent. Math. **64**
  (1981), 455–470，Corollary 2.2。这里只用已识别 CM 曲线的
  非零复中央值迫代数秩零，不用其逆命题。
