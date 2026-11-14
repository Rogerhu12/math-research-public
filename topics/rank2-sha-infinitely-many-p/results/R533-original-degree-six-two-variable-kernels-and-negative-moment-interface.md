# R533 — 原两变量六度完整核、固定负矩接口与非可迭代纤维

日期：2026-11-14。**状态：已证明。**

在 R529/R532 的同一个原来源内，保留 $U=2J,V=2K$ 两个输出时，
两条实际输入张量有完整的六度外积公式。它们保任意两变量紧开条件，
给两个固定负阶矩的准确双单位域接口。同时给出一个显示的联合余项：
其 $U$ 推前为零，乘 $K^3$ 后却有单位矩。因此已有的条件三次矩矩阵
不能直接迭代为六次矩矩阵。

本篇不赋这两个固定负矩以非零或单位值，也不把一个 CM 型单重线
当作完整有限 Schwartz 特征的算术识别。主目标未完成。

## 1. 原来源、规范与整基

沿用 [R529](R529-original-low-j-k-core-and-complete-st-carry.md)
及 [R532](R532-original-j-a5-full-frame-and-rank-two-source.md) 的普通射线、
原周期 $\Omega=\Omega_p\in\mathcal O^\times$ 与规范
$$
b=17,\quad \omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
a=2+\omega=-\omega\delta,\quad a^3=3\delta,\quad a^6=-27.
$$
这里 $\mathcal O$ 是所选普通嵌入的系数整数环。所有旧固定坏集保留。
$\sigma$ 是原 sigma，$x_\wp,y_\wp$ 是同一曲线
$y_\wp^2=x_\wp^3+b$ 的原均匀化坐标；不得与独立输入 $x$ 混淆。记
$$
B_3=-y_\wp\sigma^3,\qquad P_3=\sigma^3,\qquad
Q_1=x_\wp\sigma^3=\sigma(az)/a,\qquad \Theta=x_\wp\sigma^2.
\tag{1}
$$
这些均是已有的整测度来源。$F$ 对应测度记为 $\nu_F$；
归一为 $\int z^j\,d\nu_F=\Omega^j F^{(j)}(0)$。

标准 even degree $6$ 空间有以下完整六基：
$$
\begin{array}{c|c|c|c}
F&\text{函数}&\text{整卷积表达}&\mu_6\text{型}\\ \hline
h_0&x_\wp^3\sigma^6&\Theta^3&0\\
h_6&\sigma^6&P_3^2&0\\
f_1&-x_\wp y_\wp\sigma^6&B_3Q_1&1\\
f_2&x_\wp^2\sigma^6&\Theta^2\sigma^2&2\\
f_3&-y_\wp\sigma^6&B_3P_3&3\\
f_4&x_\wp\sigma^6&Q_1P_3&4.
\end{array}
\tag{2}
$$
除去共同 $\sigma^6$ 后，极点阶恰为 $6,0,5,4,3,2$，互异；
$h^0(6[0])=6$，所以这不是只截取低阶项的候选表。
整性由第三列的原测度卷积给出。型 $j$ 的含义是
$F(\zeta z)=\zeta^jF(z)$，$\zeta\in\mu_6$。
另记
$$
H=h_0-2b h_6=(x_\wp^3-2b)\sigma^6,\qquad H(0)=1.
\tag{3}
$$

在原 $(R,x)$ 两个输入上取
$$
\Sigma_B=\nu_{B_3}(R)\otimes\nu_\sigma(x),\qquad
\Sigma_P=\nu_{P_3}(R)\otimes\nu_\sigma(x),
$$
$$
U=R-ax=2J,\qquad V=R+ax=2K.
\tag{4}
$$
矩阵行列式 $2a$ 是当前处单位。两输出各自极化度数 $3+3=6$，
交叉项为 $3-N(a)=0$；其 even 半特征正是 R529 §2 支付的那个，
没有额外伴随 flat twist。两个完整生成函数为
$$
F_B(s,t)=B_3(s+t)\sigma(a(t-s)),\qquad
F_P(s,t)=\sigma(s+t)^3\sigma(a(t-s)).
\tag{5}
$$
对测度的指数生成函数须把 $(s,t)$ 同时代为 $(\Omega s,\Omega t)$。

## 2. 两个完整外积恒等式

写
$(F\wedge G)(s,t)=F(s)G(t)-G(s)F(t)$。则
$$
\boxed{F_B=a\{H\wedge f_1+6b\,f_3\wedge f_4\},}
\tag{6}
$$
$$
\boxed{F_P=a\{H\wedge f_4+2\,f_1\wedge f_3\}.}
\tag{7}
$$

**证明。** (5) 都在整个 $\mathcal S_6\otimes\mathcal S_6$ 中，
且交换 $s,t$ 时因 sigma 奇性变号。第一式总型为 $1$；
由 (2)，对应交替空间恰由
$$h_0\wedge f_1,\quad h_6\wedge f_1,\quad f_3\wedge f_4$$
张成。第二式总型为 $4$，对应空间恰由
$$h_0\wedge f_4,\quad h_6\wedge f_4,\quad f_1\wedge f_3$$
张成；可能的 $f_2\wedge f_2$ 恒为零。因此下述系数确定的是
整个函数，不是有限 jet 的猜测。

在 $t=0$，由 $\sigma(as)=aQ_1(s)$，(5) 分别为
$-af_1(s),-af_4(s)$。两式第一个外积的系数因而都为 $a$。
原微分方程给
$$
\sigma(z)=z+\frac b{210}z^7+O(z^{13}),\qquad
B_3(z)=1+\frac{3b}{10}z^6+O(z^{12}),
$$
$$
h_0=1-\frac{2b}{5}z^6+O(z^{12}),\quad
f_1=z+\frac{6b}{35}z^7+O(z^{13}),\quad
h_6=z^6+O(z^{12}),\quad f_3=z^3+O(z^9),\quad f_4=z^4+O(z^{10}).
\tag{8}
$$
第一生成函数的七次齐次部分，除以 $a$，为
$$
b\left\{\frac3{10}(s+t)^6(t-s)-\frac9{70}(t-s)^7\right\}.
$$
其 $s^6t$ 系数 $-12b/5$ 减去 $h_0\wedge f_1$ 的 $-2b/5$，
给 $h_6\wedge f_1$ 的系数 $-2b$；
$s^3t^4$ 系数恰为 $6b$，给第三项。得到 (6)。

第二函数的四次齐次部分除以 $a$ 为
$$(s+t)^3(t-s)=t^4-s^4+2st^3-2s^3t,$$
故 $f_1\wedge f_3$ 系数为 $2$。余系数写作 $cb\,h_6\wedge f_4$。
代 $t=\omega s$，使用 $a(\omega-1)=-3$、$1+\omega=-\omega^2$，
左边成为 $\sigma(s)^3\sigma(3s)$。R532 §6 的完整三倍恒等式
$$
\sigma(3s)=3x_\wp(s)(x_\wp(s)^3+4b)\sigma(s)^9
$$
使其等于 $3(x_\wp^4+4bx_\wp)\sigma^{12}$。右边等于
$$
a(\omega-1)\{x_\wp^4+cbx_\wp-2x_\wp y_\wp^2\}\sigma^{12}
=3\{x_\wp^4+(2-c)bx_\wp\}\sigma^{12}.
$$
因此 $c=-2$，得到 (7)。证毕。

以 $\eta\wedge\nu=\eta\otimes\nu-\nu\otimes\eta$ 记测度外积，
Amice 变换单射立即把 (6)–(7) 变为
$$
\begin{aligned}
(U,V)_*\Sigma_B&=a(\nu_H\wedge\nu_{f_1}+6b\,\nu_{f_3}\wedge\nu_{f_4}),\\
(U,V)_*\Sigma_P&=a(\nu_H\wedge\nu_{f_4}+2\,\nu_{f_1}\wedge\nu_{f_3}).
\end{aligned}
\tag{9}
$$
(9) 可施加任意真实两变量紧开测试。与 R535 的其他实际输入张量相乘时，
必须同时保其原系数及条件；(9) 不把那些条件当独立边际。

## 3. 整个空间的核心与双单位负矩

沿用
$$
\lambda=-\bar\pi^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1.
$$
当前射线的 $g_\pi\equiv7\pmod {12}$ 及实际锚 $\Theta(\delta z)$
已经在 R529 §2 把整个 even $\mathcal S_6$ 核定为 $\beta$。
因此 (2)–(3) 的每条实际整测度都满足
$$
\nu_F|_{p\mathcal O}=\beta[\kappa]_*\nu_F.
\tag{10}
$$
特别地，(9) 对 $U,V$ 两方向各有完整核心，任意两深度可独立运输；
这里使用的是整个六维空间，而非只靠各单重型猜核心。

对任意整数 $r$（包括负整数）定义
$$
J_F^{(r)}(u)=\int_{\mathcal O^\times}z^r\langle z\rangle^{du}\,d\nu_F(z),
\qquad u\in\mathbb Z_p.
\tag{11}
$$
单位域上负幂有界，故这是合法的原测度积分。由 $\mu_6$ 变换，
若 $r$ 与 $F$ 的型不同余，则 (11) 对所有 $u$ 恒为零。

记 $M_B^{r,s}(u,v)$ 为在原 $\Sigma_B$ 上、**同时限制 $U,V$ 为单位**的
$$U^rV^s\langle U\rangle^{du}\langle V\rangle^{dv}$$
积分；$M_P$ 同理。由 (9) 严格得到
$$
\begin{aligned}
M_B^{r,s}(u,v)=a\{&
J_H^{(r)}(u)J_{f_1}^{(s)}(v)-J_{f_1}^{(r)}(u)J_H^{(s)}(v)\\
&+6b[J_{f_3}^{(r)}(u)J_{f_4}^{(s)}(v)-J_{f_4}^{(r)}(u)J_{f_3}^{(s)}(v)]\},
\end{aligned}
\tag{12}
$$
$$
\begin{aligned}
M_P^{r,s}(u,v)=a\{&
J_H^{(r)}(u)J_{f_4}^{(s)}(v)-J_{f_4}^{(r)}(u)J_H^{(s)}(v)\\
&+2[J_{f_1}^{(r)}(u)J_{f_3}^{(s)}(v)-J_{f_3}^{(r)}(u)J_{f_1}^{(s)}(v)]\}.
\end{aligned}
\tag{13}
$$
这些是完整两个 Mellin 变量的恒等式。

置 $D_j=1+\lambda\kappa^j$。由 (8)、(10) 得
$$
J_H^{(0)}(0)=D_0,\quad J_{f_1}^{(1)}(0)=\Omega D_1,\quad
J_{f_3}^{(3)}(0)=6\Omega^3D_3.
\tag{14}
$$
$D_1,D_3$ 显然为单位。$D_0$ 也为单位：当前 $\pi$ 的整系数
给偶数迹 $t_\pi=\pi+\bar\pi$。若 $D_0\equiv0\pmod p$，则
$t_\pi\equiv1\pmod p$；而 $|t_\pi|\le2\sqrt p<p-1$，$p>19$，
故 $t_\pi=1$，与偶性矛盾。

定义实际固定负矩
$$
I_4=\int_{\mathcal O^\times}z^{-2}\,d\nu_{f_4},\qquad
I_1=\int_{\mathcal O^\times}z^{-5}\,d\nu_{f_1}.
\tag{15}
$$
型消去与 (12)–(14) 给
$$
\boxed{\begin{aligned}
M_P^{-2,0}(0,0)&=-aD_0 I_4,\\
M_B^{-5,0}(0,0)&=-aD_0 I_1,\\
M_B^{-2,3}(0,0)&=-36ab\Omega^3D_3 I_4,\\
M_P^{-5,3}(0,0)&=12a\Omega^3D_3 I_1.
\end{aligned}}
\tag{16}
$$
各显示乘数是当前处单位，故分别给固定负矩与相应真实双单位积分
非零/单位性的准确等价。没有证明等价两端已非零。

更一般地，$U\in p^n\mathcal O^\times,V\in p^m\mathcal O^\times$
时，把测试完整改成
$$(U/\kappa^n)^r(V/\kappa^m)^s
\langle U/\kappa^n\rangle^{du}\langle V/\kappa^m\rangle^{dv},$$
其积分准确为 $\beta^{n+m}M^{r,s}(u,v)$。
若另用 $p^n,p^m$ 归一，则必须保所有 $\lambda^{2n},\lambda^{2m}$
的幂与尺度对数。这里未作任何负矩的无限环带求和。

## 4. 条件三次矩的确切非可迭代余项

本节 $K=V/2$ 是原物理输出，不能误用 $V$。令
$$
\boldsymbol\Sigma=\begin{pmatrix}\Sigma_B\\\Sigma_P\end{pmatrix},
\qquad \Pi=U_*.
$$
对 (6)–(7) 取 $t^3$ 系数并乘 $3!\Omega^3/2^3$，
以及取 $t^6$ 系数并乘 $6!\Omega^6/2^6$，得到**整个 $U$ 测度**等式
$$
\Pi(K^3\boldsymbol\Sigma)=A\,\Pi\boldsymbol\Sigma,\qquad
A=\Omega^3\begin{pmatrix}0&9b/2\\-3/2&0\end{pmatrix},
\tag{17}
$$
$$
\Pi(K^6\boldsymbol\Sigma)=-27b\Omega^6\Pi\boldsymbol\Sigma.
\tag{18}
$$
细节是 $f_3^{(3)}(0)=6$，而由 (3)、(8)
$H^{(6)}(0)=-1728b$；其余项由型排除。
$U$ 边际为
$$
\Pi\Sigma_B=-a\nu_{f_1},\qquad \Pi\Sigma_P=-a\nu_{f_4}.
\tag{19}
$$

现在定义仍在真实 $(R,x)$ 来源上的联合测度
$$
\boldsymbol{\mathcal R}=K^3\boldsymbol\Sigma-A\boldsymbol\Sigma.
\tag{20}
$$
由 (17)，$\Pi\boldsymbol{\mathcal R}=0$。但
$$
A^2=-\frac{27b}{4}\Omega^6 I,\qquad
\boxed{\Pi(K^3\boldsymbol{\mathcal R})
=-\frac{81b}{4}\Omega^6\Pi\boldsymbol\Sigma.}
\tag{21}
$$
因此第一分量 $\mathcal R_B$ 满足
$$
\boxed{
\int_{\{U\in\mathcal O^\times\}}U K^3\,d\mathcal R_B
=\frac{81ab}{4}\Omega^7D_1\in\mathcal O^\times.
}
\tag{22}
$$
这里 $K$ 未额外限制为单位；它正是 (20) 的原联合多项式测试。
$p>19$、$b=17$ 及 (14) 证明最右端确为单位。

(20)–(22) 完整支付以下障碍：乘 $K^3$ 不保持 $\ker\Pi$，
所以 (17) 只是一次推前后的条件矩关系，并不定义一个可以在
边际空间上自由迭代的乘法算子。直接平方 $A$ 会把 (18) 的系数
错误缩小四倍；实际缺失量正是 (21) 的显示非零纤维。

## 5. 当前边界及接回原问题的要求

(6)–(9) 是原六度两变量来源的全恒等式，可以直接代入
[R535](R535-original-hesse-tensor-and-complete-mixed-kernel.md)
的完整 Hesse 五项；原旧 $W$ 的全部 $E/K$ 项及所有输入条件仍须同转置。
(12)–(16) 给固定负矩的准确接口，但未识别 $f_1,f_4$ 的全部
有限 Schwartz/Hecke 数据。仅有 $\mu_6$ 型和 whole 核，不足以
把其负阶矩换成另一个算术分支的已知正阶特殊值。
原 [R332](R332-fixed-negative-original-moments-actual-soule-classes-and-reflected-root-signs.md) 的
同 CM 型 Katz 对偶及普通地点约束仍须遵守；本篇不使用任何
未付的 $r\mapsto-1-r$ 反射。

继续需要的是同一原来源双单位域的实际比较，或完整补域与原
$J'_S,J'_T$ 的合法联立。单独的辅助单位矩 (22)、
原网格非零或有限个素数不满足课题完成标准。
