# R317：弱单 hook 曲段的完整混合修正与非负分支点第四障碍

日期：2026-11-15。**完整纸面原式推导。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R308](R308-genuine-derivative-rank-two-circles-with-one-hook-and-complete-third-range.md) 已经构造了真正导数 rank-two 的弱单 hook 圆，并支付同一真实几何上的完整三阶 range。本稿回到第四原式，算出离开导数 rank-one 后出现的准确新项。它不是任意可调的自由常数。

对 R308 中真实曲段
$$
f(x)=A_\nu(x-\beta_\nu)^{5/2},
\qquad g(x)=w_\nu(x),\quad
w_\nu\in C_c^\infty(J_\nu),\quad
\overline J_\nu\subset(\beta_\nu,\infty),
\tag{1}
$$
若全部物理分支点 $\beta_\nu\ge0$，则在原小共振偶端芽上，完成此前必要面积及三个 directed 行以后，新的完整一层仍严格为正。因此这一自然 R308 子族虽然通过了三阶，仍不能通过完整第四 ruling。

$\beta_\nu$ 是 profile 幂段的分支位置，**不是**几何端芽的 $\omega-k/h$ 常数。所有计算均在固定的真实物理坐标 $x$ 中进行；没有把一般负 $\beta_\nu$ 平移成零再沿用原算子。负分支点的实际符号和联合约束留待另证。

主要来源：[R250 完整三槽面积及弱 hook](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R259 真实 cubic 变分和尾项](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R300 完整一层](R300-one-history-tail-compensation-and-thirty-eight-dimensional-principal-space.md)、[R304 原小共振正余量](R304-positive-one-history-remainder-excludes-disjoint-real-rank-one-circles.md)、[R306 一般 mixed 四行](R306-derivative-rank-classification-and-overlapping-profile-Gaussian-obstruction.md)及 R308。

## 1. 同一实际几何、弱条件与真实曲段范围

保持 R308 已固定的真实闭 hook：
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0,
$$
并在所考察端口取 R304 的原小共振芽
$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=\kappa(1-2\varepsilon\sigma^2),\qquad
\omega=\kappa/h,\qquad
\varepsilon=\kappa^2/4,\quad
0<t:=\kappa^2<1/100.
\tag{2}
$$
$h_e>0$，$\kappa$ 可以为正或负。profile 活动区间仍在正物理轴上。

最终 $f,g$ 为实紧光滑函数，满足原三矩圆条件，且
$$
\mathfrak H(g;f,f)=0,\qquad
\mathcal W(f,g):=g'f''-f'g''\not\equiv0.
\tag{3}
$$
不添加第二个 hook。对 $u=\phi_\theta=f\cos\theta+g\sin\theta$，
$$
\mathfrak H(u;f\odot f-u\odot u)=0
\tag{4}
$$
由 R308 的完整相位恒等成立。

本稿的全局分部积分仅要求：$\mathcal W(f,g)$ 的支撑包含于有限个严格内部曲段 $J_\nu$，在其邻域 $f'\ne0$ 且 $A_f=0$；在其余位置 $\mathcal W=0$。R308 原曲段、三左补包与八个完整副本准确满足这一假设。在最后取 $\theta=\pi/2$ 时，各曲段还有 (1)的明确形式。原 cutoff 过渡区上 $g=0$；新增矩补包内 $f,g$ 比例相同；这些区域虽可有真实原函数尾，却没有 $\mathcal W$ 项。

共同右锚始终固定。原三矩只在完整 $D=f\odot f-u\odot u$ 上使用；不宣称单个 $w_\nu$ 或单个补包独立满足它们。

## 2. 先保留一般 mixed 积分

对固定相位记
$$
p=f',\quad q=f'',\quad q'=f''',\qquad
v=u',\quad r=u'',\quad r'=u''',
$$
$$
F=q^2,\quad R=r^2,\quad d_0=F-R,\qquad A=Jd_0.
$$
$A=PD$ 是完整原算子槽，三矩使它以及下述 $XD$ 真紧。另定义
$$
C=\int R(F-R),\qquad D_4=\int(F-R)^2,
$$
$$
Y=\int vr\,d_0',\qquad
Z=\int xR\,d_0',\qquad
B=\int pq\,d_0',
$$
$$
X_2=\int x^2F'd_0',\qquad
T_1=\int xpq'd_0'.
\tag{5}
$$
这些都是整个 profiles 的真实积分。一般弱 hook 下不能沿用 R306 的 $C=0$ 或 $Y=Z=0$。

设
$$
W=vq-pr,\qquad
\mathcal J=\int W r q',\qquad
\mathcal J_x=\int xWq'r'.
\tag{6}
$$
$\mathcal J_x$ 是另一个已定义积分，不是对 $\mathcal J$ 求导。$W=\sin\theta\,\mathcal W(f,g)$，因此它只支撑在上述曲段内，所有涉及 $1/p$ 的计算都在 $p$ 与零有正距离的紧子区间内进行。

## 3. 弱通量给两个准确修正；原右尾没有被删除

由 $W'=vq'-pr'$，
$$
p(rq'-qr')=qW'-q'W.
$$
所以在完整区间分部积分，曲段端的 $W$ 与所有 jets 均为零，得到
$$
\begin{aligned}
\int W(rq'-qr')
&=\int\frac qp WW'-\int\frac{q'}pW^2\\
&=-\frac14\int
\frac{6pq'-2q^2}{p^2}\,W^2=0.
\end{aligned}
\tag{7}
$$
最后一步使用真实弱通量 $A_fW=0$。这不是把 $A_f=0$ 外推到 cutoff 或补包上。

因而
$$
\int Wrq'=\int Wqr'=\mathcal J.
\tag{8}
$$
对 $pqr^2$ 的全区导数积分，再用原 profiles 的零 collar，可得
$$
\int vrqq'=-\frac13\int FR-\mathcal J.
$$
结合 $\int vr^2r'=-\int r^4/3$，得到
$$
\boxed{
Y=-\frac23C-2\mathcal J,\qquad
B=-\frac23(D_4+C)-2\mathcal J.
}
\tag{9}
$$
它们准确替代 rank-one 情形的两条恒等。新增的 $\mathcal J$ 不能由旧 $C^2$ self 观察或“已付三阶”删去。

还需要一条带物理 $x$ 的恒等。直接由 (5)有
$$
Z+\frac C2
=\frac12\int x(RF'-FR')
=\int xqr(rq'-qr').
$$
在 $W$ 支撑内，$A_f=0$ 给 $q^2/p=3q'$ 及
$$
(q^2/p)'=-qq'/p.
$$
代入上式并对 $W'$ 分部积分，得到
$$
\boxed{
Z+\frac C2=-3(\mathcal J+\mathcal J_x).
}
\tag{10}
$$
这些步骤只操作已经存在的真实 local 密度；Volterra 尾是在下一节的完整原面积中保留，而非逐曲段假设紧性。

## 4. 完整面积现在迫 $Z=C$，不再迫 $C=0$

沿 R304/R306 使用原五算子
$$
P=\Phi_{r_0},\quad R_0=\Phi_{r_1},\quad
S_0=\Phi_{s_0},\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},
$$
及
$$
W_*=aR_0+bS_0,\qquad
Z_*=d_*L+e_*U,\qquad B_{-3}=c_PP,
$$
$$
\begin{aligned}
a&=-\frac{51t^2+2t+8}{64h_e^2},&
b&=-\frac{17t^2+4t}{32h_e^2},\\
d_*&=\frac{6\kappa^3}{h_e},&
e_*&=-\frac{\kappa(15t+1)}{4h_e},&
c_P&=-\frac{\kappa(41t^2+27)}{216h_e^3}.
\end{aligned}
\tag{11}
$$
这里 $b$ 是 Gaussian 方向的常数，与 profile 分支点 $\beta_\nu$ 无关。

R250 的完整三槽原式是
$$
[W_*,P](u;D)=
\frac13\{(a+3b)J(rd_0)+a\mathfrak H(u;D)\}.
$$
后项由弱 (4)准确为零。保留 $J(rd_0)$ 的真实左尾，直接分部积分给
$$
I_1\{u,J(rd_0)\}
=\frac12\int RF-\frac34\int R^2-\frac12\int xRF'
=\frac{C-Z}{2}.
$$
由于 $a+3b\ne0$，完整 $A_{-2,-3}$ 的这一外矩为零迫
$$
\boxed{Z=C.}
\tag{12}
$$
结合 (10)，又得到
$$
\boxed{C=-2(\mathcal J+\mathcal J_x).}
\tag{13}
$$
(12)–(13)均是对完整 profiles 的条件，不是要求每个曲段各自通过一个非合法单包面积。

## 5. 原四行与完整 local 合成，不只算一个候选项

定义真正 directed 行
$$
H_j^X=-I_j(XD,PD)+2I_j\{u,X(u,PD)\}.
$$
假设完整第四 ruling 可行。原 Gaussian 词独立性、相应对称二层与面积便给必要条件
$$
H_2^P=0,\qquad
aH_1^{R_0}+bH_1^{S_0}=0,\qquad
d_*H_0^L+e_*H_0^U=0.
\tag{14}
$$
不能只从某个对称行推出一个 directed 行；这里保留了原两部分一起为零的前提。

R306(28) 已从原 cubic 及真实 inner 槽得到的一般 mixed 四式在此原样使用：
$$
\begin{aligned}
H_2^P&=-X_2-4Z+4Y-2D_4,\\
H_1^{R_0}&=-X_2+2T_1-Z+2Y+C,\\
H_1^{S_0}&=-X_2-2Z+\tfrac12D_4,\\
H_0^U&=-\tfrac32X_2+2T_1-2Y+Z+2B+D_4-C.
\end{aligned}
\tag{15}
$$
这些式子本身不要求 $W=0$。其变分保留了
$-I_j(A,X(f,f))$，所以没有把可能非紧的 $X(f,f)$ 改成紧函数。

先用 (12)、(14) 消去 $X_2,T_1$，再代入 (9)，准确得到
$$
H_0^U=
\left(\frac23-\frac{5b}{2a}\right)D_4
+\frac{14}{3}\left(1-\frac ba\right)C
+8\left(1-\frac ba\right)\mathcal J .
\tag{16}
$$
原 R221(17) local 项并不随弱核简化而消失。其完整独立系数仍为
$$
[\sigma h^{-2}j^0]
\{2\mathcal T(A;D)-4\mathcal T(u;u,A)\}
=-\frac{\kappa^3}{8}X_2+\frac{\kappa^3}{16}D_4
-\frac{\kappa^3}{4}Z .
\tag{17}
$$
由 (9)、(12)、(14)，它化为
$$
\kappa^3\left(\frac{5D_4}{16}+\frac{7C}{12}
+\mathcal J\right).
\tag{18}
$$
原 elementary history 三常数是
$$
\ell_0=-\kappa/2-6\kappa^3,\qquad
m_0=\kappa(15t+1)/4,\qquad p_0=41\kappa^5/216.
$$
因此去掉非零 $c_P$ 的完整一层行为
$$
\mathscr O_\theta
=\frac{\ell_0}{2}H_0^L+
\frac{m_0}{2}H_0^U+
\frac{p_0}{2}H_2^P+\text{(17)}.
$$
第三条 (14)给
$$
K_\kappa:=\frac12(m_0-\ell_0e_*/d_*)
=-\frac{1+15t}{96\kappa}.
$$
完整合成 (16)、(18)，得到本稿的主要混合身份：
$$
\boxed{
\mathscr O_\theta
=-D_\kappa D_4+
\Gamma_\kappa\left(\mathcal J+\frac{7C}{12}\right),
}
\tag{19}
$$
$$
D_\kappa=
\frac{16+184t-1713t^2-2475t^3-4590t^4}
{288\kappa(51t^2+2t+8)},
$$
$$
\Gamma_\kappa=
8K_\kappa(1-b/a)+\kappa^3
=-\frac{8+114t-169t^2+231t^3-612t^4}
{12\kappa(51t^2+2t+8)} .
\tag{20}
$$
这包含真实 local、chain 和 elementary history，且没有舍去 $C^2$ 余项。令 $\mathcal J=C=0$ 才回到 R306 的旧值；弱 hook 本身不允许这样令零。

## 6. 在 R308 的真实曲段上把修正完全算出

现在只取真实相位 $\theta=\pi/2$，故 $u=g$。在一个曲段内设
$$
f=A_\nu(x-\beta_\nu)^{5/2},\qquad
g=w_\nu\in C_c^\infty(J_\nu).
$$
所有求导与积分仍在最终物理位置；不会在最后平移后继续使用旧的 $x$ 权系数。

记
$$
\lambda_\nu=\frac{75A_\nu^2}{16}>0.
$$
原幂式准确给
$$
qq'=\frac32\lambda_\nu,\qquad
pq'=\lambda_\nu(x-\beta_\nu).
$$
因 $w_\nu',w_\nu''$ 在曲段两端都为零，
$$
\begin{aligned}
\mathcal J_\nu
&=\int q'w_\nu''(w_\nu'q-pw_\nu'')
=-\lambda_\nu\int(x-\beta_\nu)(w_\nu'')^2,\\
(\mathcal J_x)_\nu
&=\int xq'w_\nu'''(w_\nu'q-pw_\nu'')
=-\frac{\lambda_\nu}{2}\int(x+\beta_\nu)(w_\nu'')^2.
\end{aligned}
\tag{21}
$$
例如第二式保留两项：
$$
\int xw_\nu'w_\nu'''=-\int x(w_\nu'')^2,\qquad
-\int x(x-\beta_\nu)w_\nu''w_\nu'''
=\frac12\int(2x-\beta_\nu)(w_\nu'')^2.
$$
这些是原紧 $w_\nu$ 的合法分部积分，不对 $f$ 的幂段单独施加虚假的零边界。

在所有其他区域 $W=0$，故 (21)可以对曲段求和。由全局必要式 (13)才有
$$
C=\sum_\nu\lambda_\nu
\int(3x-\beta_\nu)(w_\nu'')^2.
$$
最终新修正准确为
$$
\boxed{
\mathcal E_{\rm weak}:=
\mathcal J+\frac{7C}{12}
=\sum_\nu\frac{\lambda_\nu}{12}
\int(9x+5\beta_\nu)(w_\nu'')^2.
}
\tag{22}
$$
这里未把完整 $C$ 的补包贡献直接丢弃：它们已包含在 (13)的全局等式中。(22)是在假设原面积门被支付后的准确后果。

八副本的实幅度可以为负；其 $A_\nu^2$ 和 $(w_\nu'')^2$ 合起来仍是原四次幅度权。补偿包、cutoff 和真实左尾没有被误认为分别无成本。

## 7. 非负物理分支点给严格第四障碍

置
$$
N(t)=16+184t-1713t^2-2475t^3-4590t^4,
$$
$$
P(t)=8+114t-169t^2+231t^3-612t^4,\qquad
A(t)=51t^2+2t+8 .
$$
乘回 (11)中的原 $c_P$，(19)成为
$$
\boxed{
[\sigma h^{-2}j^0]\mathscr R_{-3,\pi/2}
=
\frac{(41t^2+27)N(t)}{62208h_e^3A(t)}D_4
+
\frac{(41t^2+27)P(t)}{2592h_e^3A(t)}
\mathcal E_{\rm weak}.
}
\tag{23}
$$
$0<t<1/100$ 时 $N(t)>15$，且
$P(t)>8-169/10^4-612/10^8>7.98$。两个系数都严格为正，与 $\kappa$ 的正负无关。

在当前正物理区间上，若每个 $\beta_\nu\ge0$，则
$$
9x+5\beta_\nu>0.
$$
至少一个 $w_\nu$ 非零；紧支撑非零函数不可能二阶导数恒零。因此
$$
\mathcal E_{\rm weak}>0,\qquad D_4\ge0.
$$
于是 (23)严格为正。

**定理。** R308 的真实弱单 hook、导数 rank-two 圆，若在最终物理坐标中的所有幂段分支点非负，则在 (2)的同一小共振偶端芽上不能满足完整第四 ruling。若它已违反 (12)或(14)，自然已失败；若这些原必要门全部被付，(23)仍给严格非零余量。

这不是仅算一个候选 local 项。R304/R300 的同锚 Gaussian 词独立性与完整 gauge 偶部商使 (23)成为不能由其他 history、真实中心初值或 $\mathcal W_e$ 项抵消的准确系数。使用的范围与原 R304 相同，新增的只有合法 weak mixed profiles 及其完整修正。

非负分支子族确实能在 R308 的任意给定正活动区间内构造：先在该区间选一个正 $\beta$，在其右侧放严格内部幂段及 cutoff，在其左侧留三补包；先固定缩放和完整副本位置，再作原七次差分。无需改变已冻结的几何或扩大物理区间。

## 8. 本稿没有排除的一条实际分叉

一般负 $\beta_\nu$ 下，(22)可以出现负项。不能由此宣布第四可解：同一个 profiles 仍须同时通过真实全角面积、(14)、其余对称与一层系数、完整第四周期和平台条件。

尤其不能独立指定 $\mathcal E_{\rm weak}$、$D_4$ 或补包的四次矩；(13)、原三矩以及原补偿平方根把它们约束在同一个真实圆上。下一问题是检查负分支点能否在这些联立条件下让 (23)准确为零，而非只观察 $9x+5\beta_\nu$ 变号。

R308 的完整三阶结论保持。新增完成的是 (19)的精确弱核 mixed 修正、(22)对真实幂段与完整副本的准确值，以及非负物理分支子族的严格第四否定。
