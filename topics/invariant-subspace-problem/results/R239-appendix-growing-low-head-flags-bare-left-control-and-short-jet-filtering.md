# R239 附录：增长低头完整源旗的裸费左界、全首头合并与 short jets 定位

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。
状态：本文的实际低头源旗、全原窗口裸费左上界、首头合并常数及 short jets 谱定位均已证明。没有将剩余源图换成物理补空间；一般中间带和高头余项的温和上界仍未证明。

依赖：[真实无缩放 Jordan 成本](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)、[完整源坐标](R239-appendix-complete-source-schur-coordinates-and-growing-head-observation.md)、[首头度量分裂](R239-appendix-first-source-head-metric-splitting-and-middle-band-schur-amplification.md)及[两费用中的首头消元与保全左交叉项的正过滤测试](R239-appendix-paid-head-elimination-and-filtered-left-cross-tests.md)。本文只对较小的真实头使用一次已付的条件数，不以整个 $A_m$ 的巨大逆代替分段预算。

## 1. 真实低头、一次相似与反向链

固定原两个模型之一，$m\ge5,d=2^m$，以及全部原合法整数
$$
4d\le q\le e^{d^3/4}.
$$
写 $A=A_m,D=D_m$，$\nu=\|D_m\|$。原系数 $b_j=(j+1)^{-2}$ 给
$$
0<\nu\le\sum_{j\ge m}(j+1)^{-2}\le1/m<1.
\tag{1.1}
$$

取 $3\le\ell\le m$，记小头维数为 $H=2^\ell$。原矩阵的低头旗
$$
\mathcal H_H=\operatorname{span}\{e_0,\ldots,e_{H-1}\}
$$
在 $A_m$ 下不变，而且
$$
\boxed{A_m|_{\mathcal H_H}=A_\ell.}
\tag{1.2}
$$
这是实际权的相同低段，不是近似：所有 $i\ge\ell$ 的 $N_i$ 或 $Y_i$ 都杀掉这个旗；其余真实有限矩阵的限制与 $A_\ell$ 相同。

沿所引 Jordan 稿取
$$
K_\ell e_j=(A_\ell^*)^j e_0,\qquad V_\ell=K_\ell^{-*}.
$$
于是
$$
A_\ell=V_\ell J_HV_\ell^{-1},\qquad
\kappa_\ell:=\|V_\ell\|\,\|V_\ell^{-1}\|
\le e^{221\,16^{\ell-1}}.
\tag{1.3}
$$
这是无缩放的 $J_H$，故下面没有漏付 Jordan 标量的负幂。$K_\ell$ 下三角，$V_\ell$ 和其逆都上三角，所以它们保持每个原物理低头旗。且 $K_\ell$ 的第零行、列均为 $e_0$，故
$$
V_\ell e_0=V_\ell^{-1}e_0=e_0,\qquad
V_\ell=1\oplus V_{\ell,+}.
\tag{1.4}
$$

定义有限反向链算子
$$
R_\ell=V_\ell J_H^*V_\ell^{-1}.
\tag{1.5}
$$
对 $x$ 支持在原头 $0,\ldots,H-2$，准确有
$$
A_\ell R_\ell x=x.
\tag{1.6}
$$
更一般，若 $x$ 支持到头 $H-j-2$，则
$$
\boxed{A_\ell R_\ell^{j+1}x=R_\ell^jx,\qquad
\operatorname{supp}_{\rm head}(R_\ell^{j+1}x)
\subseteq\{0,\ldots,H-1\}.}
\tag{1.7}
$$
证明是逐次使用保持低旗以及 $J_HJ_H^*=I-P_{\mathbb Ce_{H-1}}$。

关键预算是
$$
\boxed{\|R_\ell^j\|
=\|V_\ell(J_H^*)^jV_\ell^{-1}\|
\le\kappa_\ell\qquad(1\le j<H).}
\tag{1.8}
$$
这里所有反向阶只支付同一次相似，绝不把它估成 $\kappa_\ell^j$。

## 2. 整个增长低头联合源旗

定义原完整源空间内的闭子空间
$$
\boxed{
\mathscr R_q^{[H]}
=\bigoplus_{i=0}^{H-2}e_i
\left(\ker D^{H-i-1}\cap\mathcal H_q\right).}
\tag{2.1}
$$
它保留全部连续尾及每个实际尾短核阶，不要求源 primitive。因为 $H\le d$，(2.1) 是原 $\mathscr R_q$ 的真实子空间。

给定 $r\in\mathscr R_q^{[H]}$，定义只有以下孔层非零的左链
$$
\boxed{
v_{q-j}=(-1)^jR_\ell^{j+1}D^jr
\quad(0\le j\le H-2).}
\tag{2.2}
$$
全部头算子默认张量尾单位。原 $q\ge4d$ 保证这些孔层均非负。

逐项核对合法性。由于第 $i$ 源头属于 $\ker D^{H-i-1}$，
$$
D^jr\ \text{只支持到头}\ H-j-2.
\tag{2.3}
$$
所以 (1.7) 每次都在真实允许旗内适用。顶端有
$$
Av_q=AR_\ell r=r.
$$
相邻左输出为
$$
Av_{q-j}+Dv_{q-j+1}
=(-1)^jR_\ell^jD^jr
+(-1)^{j-1}R_\ell^jD^jr=0.
$$
最低端也没有漏项，因为 $D^{H-1}r=0$。因此 (2.2) 确属原完整 $\mathscr V_q$，且 $E_qv=r$。

不同 $j$ 的输出孔层正交，所以没有对左链使用错误的逐项同层求和。由 (1.8)，
$$
\|v\|^2
=\sum_{j=0}^{H-2}\|R_\ell^{j+1}D^jr\|^2
\le\kappa_\ell^2\sum_{j=0}^{H-2}\nu^{2j}\|r\|^2
\le\frac{\kappa_\ell^2}{1-\nu^2}\|r\|^2.
\tag{2.4}
$$
真正左最小者的费用不超过此候选。另一方面，原裸链首段必须满足 $Da_1=r$，故
$$
\alpha_q(r)\ge\|r\|/\nu.
$$
于是得到全原整数窗的裸费左界
$$
\boxed{
\mu_q(r)^2\le C_{\ell,m}\alpha_q(r)^2
\quad(r\in\mathscr R_q^{[H]}),\qquad
C_{\ell,m}:=\frac{\nu^2}{1-\nu^2}\kappa_\ell^2
\le\frac{e^{442\,16^{\ell-1}}}{m^2-1}.}
\tag{2.5}
$$
常数不含 $q$。没有使用纯尾右逆的 $q$ 次幂，也没有改变裸费定义。

## 3. 完整源坐标中正是低头三角

沿完整源坐标稿，$\Gamma_q$ 把原源同构到
$$
\mathscr U_q=\bigoplus_{t=0}^{d-2}
\left(H_{\ge t+1}\otimes K_{q-t}\right).
$$
在这个真实坐标中，
$$
\boxed{
\Gamma_q\mathscr R_q^{[H]}
=
\mathscr U_q^{[H]}
:=
\bigoplus_{t=0}^{H-2}
\left(\operatorname{span}\{e_{t+1},\ldots,e_{H-1}\}
\otimes K_{q-t}\right).}
\tag{3.1}
$$
证明：对 (2.1) 的源，$P_0D^tr$ 只支持到头 $H-t-2$，并在 $t\ge H-1$ 时为零。实际三角同构
$$
A^{t+1}:H_{\ge t+1}\longrightarrow H_{\le d-t-2}
$$
的逆，把这个低头子旗准确送到
$\operatorname{span}\{e_{t+1},\ldots,e_{H-1}\}$；该断言由原非零第一上对角权的逐行回代得到。

反过来，(3.1) 的坐标经
$$
B_Ua=\sum_t(-1)^tA^{t+1}Q_ta_t
$$
所得第 $i$ 源头只可能来自 $t\le H-i-2$，而 $Q_tK_{q-t}\subseteq\ker D^{t+1}$。因此其尾核阶不超过 $H-i-1$，正是 (2.1)。

若 $\mathcal G_q$ 是完整左 Schur 度量，$\mathcal F_q$ 是原裸度量，则 (2.5) 准确等价于受限二次型
$$
\boxed{
\langle\mathcal G_qa,a\rangle
\le C_{\ell,m}\langle\mathcal F_qa,a\rangle
\qquad(a\in\mathscr U_q^{[H]}).}
\tag{3.2}
$$
它已经对这些源消去所有原零源自由坐标，不是对某个未最小化左链重新定义费用。

## 4. 与原两形式求和门槛相容的增长尺度

当 $m\ge7$，取
$$
\ell_m=\lfloor3m/4\rfloor-2,\qquad H_m=2^{\ell_m}.
\tag{4.1}
$$
于是 $\ell_m\ge3$，并且
$$
\frac18d^{3/4}<H_m\le\frac14d^{3/4}.
$$
由 $16^{\ell_m-1}=H_m^4/16$，
$$
442\,16^{\ell_m-1}
=\frac{221}{8}H_m^4
\le\frac{221}{2048}d^3<\frac18d^3.
$$
故对 (3.1) 的整个增长三角及全部原 $q$，
$$
\boxed{
C_{\ell_m,m}
\le\frac{\exp(221d^3/2048)}{m^2-1}.}
\tag{4.2}
$$
与原目标量级 $e^{d^3/4}/d$ 相比，准确比值上界为
$$
\boxed{
\frac{C_{\ell_m,m}}{e^{d^3/4}/d}
\le\frac{d}{m^2-1}
\exp\!\left(-\frac{291}{2048}d^3\right)
\longrightarrow0.}
\tag{4.3}
$$
因此这段源方向的实际裸费常数在原求和预算内。未由此声称剩余源也在该三角内，或与其物理正交。

## 5. 整条首源头与低三角合并时的准确常数

仍令 $P$ 为物理首源头投影，$Q=I-P$。定义更大的闭源空间
$$
\boxed{
\mathscr X_q^{[H]}
=P\mathscr R_q+\mathscr R_q^{[H]}
=e_0E_{d-1,q}\oplus
\bigoplus_{i=1}^{H-2}e_iE_{H-i-1,q}.}
\tag{5.1}
$$
其坐标像准确为
$$
\boxed{
\Gamma_q\mathscr X_q^{[H]}
=\mathscr D_q+\mathscr U_q^{[H]},
\qquad
\mathscr D_q=\bigoplus_{t=0}^{d-2}
\mathbb Ce_{t+1}\otimes K_{q-t}.}
\tag{5.2}
$$
所以这里同时包括所有深度的最小头对角，不只含浅 jets。

取 $r\in\mathscr X_q^{[H]}$，$r_0=Pr,r_1=Qr$，记
$$
a_0=\alpha(r_0),\quad a_1=\alpha(r_1),\quad
\lambda_0=\|G_q^{1/2}PJ_q^{-1}r\|,\quad
\lambda=\lambda_{\rm flat}(r),\quad \mu=\mu(r).
$$
首头约化给 $a_0^2+a_1^2=\alpha(r)^2$、$\lambda_0\le\lambda$。
对同一个真实 $r$，完整能量配对为
$$
\mu^2
=\langle r_0,PJ_q^{-1}r\rangle+\langle r_1,J_q^{-1}r\rangle.
$$
第一项由既有首头同源配对至多 $a_0\lambda_0$。第二项等于两个实际左最小原像的内积；因为 $r_1\in\mathscr R_q^{[H]}$，(2.5) 给其绝对值至多 $\sqrt{C_{\ell,m}}\,a_1\mu$。因此
$$
\boxed{\mu^2\le a_0\lambda_0+\sqrt{C_{\ell,m}}\,a_1\mu.}
\tag{5.3}
$$
没有将 $PJ_q^{-1}r$ 改成 $J_q^{-1}Pr$。

**标量常数。** 定义
$$
c(C)=
\begin{cases}
(2-C)^{-1},&0\le C\le1,\\
C,&C\ge1.
\end{cases}
\tag{5.4}
$$
则 (5.3) 准确推出
$$
\boxed{
\mu_q(r)^2\le c(C_{\ell,m})
\left[\alpha_q(r)^2+\lambda_{\rm flat}(r)^2\right]
\qquad(r\in\mathscr X_q^{[H]}).}
\tag{5.5}
$$

证明常数。$\mu=0$ 时结论显然，否则按 $\mu$ 归一使 $\mu=1$，并记 $u=a_1$。从 (5.3) 得
$$
a_0\lambda_0\ge\max(1-\sqrt C\,u,0).
$$
因此
$$
\alpha^2+\lambda^2
\ge u^2+2\max(1-\sqrt C\,u,0).
$$
当 $0<C\le1$ 时，该函数最小值为 $2-C$，在 $u=\sqrt C$ 取得；当 $C\ge1$ 时最小值为 $1/C$，在 $u=1/\sqrt C$ 取得。$C=0$ 时最小值为 $2$。这正是 (5.4)--(5.5)。

特别，当低旗常数至少一时，把整条首头深对角加进来不增加这个常数。一般总有 $c(C)\le\max(1,C)$，故 (4.2)--(4.3) 的原渐近预算保持有效。

## 6. 可一次消去这个合并空间，保留真实源图

令 $L=J_q^{-1}$，$B=J_{b,q}^{-1}$，$M=B+L G_qL$，仍令 $\chi(r)^2=\langle Mr,r\rangle$。以 $\Pi_X^M$ 表示 $M$ 内积中到 (5.1) 的真正正交投影。它存在，因为 $M$ 有界严格正，而该物理源子空间闭。

对任意原源，定义
$$
s_X=\Pi_X^Mr,\qquad r_X=r-s_X.
$$
由 (5.5)，
$$
\boxed{
\chi(r)^2=\chi(s_X)^2+\chi(r_X)^2,\qquad
\mu(s_X)^2\le c(C_{\ell,m})\chi(s_X)^2.}
\tag{6.1}
$$
因而剩余源的两费用平方和不增。若在这个真实 $M$ 正交图上有常数 $K_m$ 的三 Gram 估计，则左最小原像的三角不等式和两项实数 Cauchy 给原全源常数
$$
\boxed{K_m+c(C_{\ell,m}).}
\tag{6.2}
$$
这不要求首头投影和低旗投影交换。图上的左度量仍须按前稿的四项 $R^*LR$ 公式保留；不能用物理补块的压缩替换。

对实际来源 $r_m$，若
$$
c(C_{\ell_m,m})\chi(r_m)^2\to0
$$
且 $E_{q_m}^\dagger r_m\to w$，则 (6.1) 给
$E_{q_m}^\dagger r_{X,m}\to w$。增长 $\ell_m$ 时，这个定量条件须用原已付求和预算核验；不能仅从无速率的 $\chi(r_m)\to0$ 推出。固定 $\ell$ 时，$C_{\ell,m}\to0$、$c(C_{\ell,m})\to1/2$，所以原 $\chi(r_m)\to0$ 已足够。

## 7. 首头 short jets 的更精确左范数

下面令 $1\le s\le H-1$，并只取首头源 $e_0h$，$h\in E_{s,q}$。
记
$$
u_j=V_\ell e_j\quad(0\le j\le s).
$$
由 (1.3)--(1.4)，
$$
u_0=e_0,\quad u_1=e_1,\quad
Au_j=u_{j-1},\quad u_j\perp e_0\ (j\ge1).
$$
这些低头向量由实际反向链唯一确定；固定 $s$ 后，它们不随较大的 $m$ 改变。由 $V_\ell^{-1}e_0=e_0$，有 $R_\ell^je_0=u_j$。

(2.2) 此时给
$$
\mu_q(e_0h)^2
\le\sum_{j=0}^{s-1}\|u_{j+1}\|^2\|D^jh\|^2
\le g_{\ell,s,m}\|h\|^2,
$$
其中
$$
g_{\ell,s,m}
:=1+\sum_{j=1}^{s-1}\|u_{j+1}\|^2\nu^{2j}
\le\frac{\kappa_\ell^2}{1-\nu^2}.
\tag{7.1}
$$
另一方面，任何合法左原像的顶层满足 $Av_q=e_0h$。原严格三角头的第一上对角非零、且 $Ae_1=e_0$；逐行回代给 $v_q=e_1h+e_0k$。故
$$
\boxed{
\|h\|^2\le\mu_q(e_0h)^2\le g_{\ell,s,m}\|h\|^2.}
\tag{7.2}
$$
固定 $s,\ell$，随 $m\to\infty$ 有 $g_{\ell,s,m}\to1$。因此 (7.2) 对全部原 $q$ 以及可随参数变化的所有单位 $h\in E_{s,q}$ 一致逼近单位左费用；这不是只对一个固定 primitive 向量取极限。

## 8. 与首头过滤算子 H0 的准确接合

沿前一稿，令
$$
K=(D_{q+1}^\dagger|_{E_{d-1,q}})^*
(D_{q+1}^\dagger|_{E_{d-1,q}}),\qquad
H_0=K^{-1/2}\iota_0^*J_q^{-1}\iota_0K^{-1/2}.
$$
定义闭子空间
$$
\mathscr Z_{s,q}=K^{1/2}E_{s,q},
$$
并令 $P_s$ 为其在同一个首头归一化 Hilbert 空间中的正交投影。它通常不是原物理 $E_{s,q}$ 投影。由 $\|h\|\le\nu\|K^{1/2}h\|$ 及 (7.1)，
$$
\boxed{
P_sH_0P_s\preceq\zeta_{\ell,s,m}P_s,
\qquad
\zeta_{\ell,s,m}:=\nu^2g_{\ell,s,m}
\le C_{\ell,m}.}
\tag{8.1}
$$
这里只证明压缩二次型，不假定 $P_s$ 与 $H_0$ 交换。

仍取 $T_\tau=\tau(H_0+\tau I)^{-1}$。由逐谱不等式
$$
\left(\frac{h}{h+\tau}\right)^2\le\frac{h}{4\tau},
$$
(8.1) 给
$$
\boxed{
\|(I-T_\tau)P_s\|
\le\frac{\sqrt{\zeta_{\ell,s,m}}}{2\sqrt\tau}.}
\tag{8.2}
$$
并且对任意 $\Lambda>0$，
$$
\boxed{
\|\mathbf1_{[\Lambda,\infty)}(H_0)P_s\|
\le\min\!\left(1,\sqrt{\zeta_{\ell,s,m}/\Lambda}\right).}
\tag{8.3}
$$
这把真正 short jets 放进首头左压缩的低谱区域，代价来自原低头旗而非整个 $A_m$ 逆。它是定量谱泄漏界，不是严格谱支持或可交换性。

还有一个无需过滤的真实测试分裂。令 $U_0h=k_{K^{-1/2}h}$ 为前稿首头右链等距嵌入。则 $U_0P_sU_0^*$ 是到
$$
\mathscr K_s=\{k_h:h\in E_{s,q}\}
$$
的物理正交投影。对任一原增长头测试 $c$，$\|c\|\le\varepsilon$，取
$$
c_s=U_0P_sU_0^*c,\qquad c_{\rm rest}=c-c_s.
$$
两链在原完整右旗内，值域正交。其源 $f_s=F_{\rm flag}c_s$ 属于 $e_0E_{s,q}$，而
$$
\boxed{
\|E_q^\dagger f_s\|
\le\sqrt{\zeta_{\ell,s,m}}\,\varepsilon,\qquad
\|E_q^\dagger F_{\rm flag}c_{\rm rest}\|
\le1+\varepsilon+\sqrt{\zeta_{\ell,s,m}}\,\varepsilon.}
\tag{8.4}
$$
两测试仍有前稿同一个 $c^\flat$ 的联合平方观测上界
$\varepsilon^2\lambda_{\rm flat}^2$。$\Gamma_q f_s$ 的像准确落在最小头对角的前 $s$ 个 jet 层。

增长尺度 (4.1) 下，若增长头稿采用 $\varepsilon\le e^{-d^4/20}$，则
$$
\sqrt{\zeta_{\ell_m,s,m}}\,\varepsilon
\le\frac1{\sqrt{m^2-1}}
\exp\!\left(-\frac{d^4}{20}+\frac{221d^3}{4096}\right),
$$
仍为明确指数小量。没有把这个结论外推到全部深首头源或全部高头补空间。

## 9. 当前精确剩余范围

本文已把全原窗口中的增长低头强制三角与全部最小头对角纳入原两费用的可承受比较，并付清 short jets 与真实首头左谱过滤之间的联系。其余源在执行 (6.1) 后属于由完整 $M$ 定义的图空间；物理高头、深度和该图参数不能直接互换。

下一步若以 dyadic 头块继续，必须保留原 $A_m$ 的高位 carry、各块的真实尾短核旗、跨块左交叉及同一个平坦源费用。R271 深 jets 的 Schur 消元和前稿远低 primitive 带局部化仍是不同缩减，不因 (3.2) 自动拼成全部中间带上界。无权 $N=M$ 和普通复 Hilbert ISP 仍开放。
