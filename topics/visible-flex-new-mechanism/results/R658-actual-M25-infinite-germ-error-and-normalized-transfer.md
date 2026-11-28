# R658　固定 86da 源的真实 M=25 截断余项及其归一传递

R643 使用 11 个原齐次模 $j=2,4,\ldots,22$，相位零，$r_c=11/50,\ell=1/5,A=4/5$。原算式在 $n=17$ 规定 $y(\alpha_{17})=1$，在 $n=26$ 规定有限端 $y(\alpha_{26})=0$。无穷模型取 R600 的唯一全平支。本条把两者作为**准确方程的两个不同边值问题**比较。固定 $M$ 的实际浮点 Cauchy 值、稠密积分及归一误差仍有各自的账。R643 终态的真实源合同 SHA-256 为 `56ec2a5f44fc05c844390d54395a890fd32e84fef60364483ef8532ea830cbfb`，目标为 `86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5`。以下估计不重复 Riccati 或 ODE 求解。

## 1　实际峰间的收缩

沿用 R569、R583 和 R600 的精确 Dirichlet-to-Neumann 矩阵 $D$。写 $a=\alpha_n,b=\alpha_{n+1},\mu=j^2\le484$，$r=r_c+\ell/u$，
$$
p=4u^2r^{2\mu}e^{-u(2-\sin u)},\qquad
\epsilon=\mu(\mu-1)\ell^2/(r^2u^4),\qquad (py_u)_u=-\epsilon py .
$$
对 $n\ge17$，$0<\pi/2+2\pi n-a<.04$、$6<b-a<7$、$a>100$。用本 cell 的 $C_a=4a^2r(a)^{2\mu}$，则
$$
 e^{-1}C_a <4u^2r(u)^{2\mu}< (6/5)C_a .
$$
下界用 $2\mu\int_a^{a+7}\ell/(r u^2)\,du<1$。两端各长 $1/5$ 的窗有 $\sin u>\cos(.24)>.97$（端点上的弱等号也足够），从而 $p\ge C_a e^{-9}e^{-1.03a}$。在谷中心 $3\pi/2+2\pi n$ 的左右各 $1/5$，$\sin u\le-\cos(.2)<-.98$，故 $K=(\int_a^bp^{-1})^{-1}\le3C_a e^{-2.98a}$。端窗的电阻比例不超过 $(3/5)e^9e^{-1.95a}<1/2$。

设 $H_i$ 是对应零势端插值。端窗上 $H_i\ge1/2$。R569 的单谷 Green 正性、$\epsilon\ge a^{-4}$ 及 R600 的 Green 小量 $<1/4$ 给出 $-D_{LR}\le2K$、$D_{ii}\le K-\epsilon_{\min}\int pH_i^2$。因此，两端分别有
$$
 -D_{ii}\ge C_a e^{-9}a^{-4}e^{-1.03a}/40,\qquad
 \frac{-D_{LR}}{-D_{ii}}\le T(a):=240e^9a^4e^{-1.95a}.              \tag{1}
$$
吸收 $K$ 用 $120e^9a^4e^{-1.95a}<1$，其左侧在 $a\ge100$ 递减。使用同一 cell 的端对角，避免在相邻不同归一的 $C_a$ 之间放大。

令 $k_n=-D_{n,LR}$、$V_n=-D_{n-1,RR}-D_{n,LL}$，$\rho_n=|y_n/y_{n-1}|$。对 $\rho\in[0,1/32]$，精确映射 $P_n(\rho)=k_{n-1}/(V_n-k_n\rho)$ 满足
$$
0\le P_n(\rho)\le U_n:=2T(a_{n-1}),\qquad
 |P'_n|\le L_n:=2T(a_{n-1})T(a_n).
$$
这里 $k_{n-1}/V_n$ 以左 cell 界，$k_n/V_n$ 以右 cell 界。有限端 $\rho_{26}^{25}=0$，真端 $\rho_{26}^{\infty}\le U_{26}$。这给
$$
 d_m:=|\rho_m^\infty-\rho_m^{25}|\le U_{26}\prod_{n=m}^{25}L_n
 \quad(18\le m\le26).                                                \tag{2}
$$
$17\le n\le26$ 时 $a_n>6.28n+1.53$、$a_n<166$、$\log T(a_n)<35-1.95a_n$。这些粗数只用 $3.14<\pi<22/7$、$\log 240<5.5$、$\log166<5.12$。特别
$$
 \log d_{18}<9\log2+17(35)-1.95(6.28\cdot361+17\cdot1.53)<-3860.      \tag{3}
$$
索引和为 $(17+\cdots+24)+(18+\cdots+25)+25=361$。

## 2　共同口至外口的完整路径

首 cell 的两个解左值同为 1，右值之差绝对值为 $d_{18}$。端通量的准确差为 $k_{17}d_{18}$。采用源中的平衡向量 $X=(y,y_u/\sqrt\epsilon)$，则
$$
 |\Delta X(a_{17})|\le6a_{17}^2e^{-1.979a_{17}}d_{18}<e^{-4060}.
$$
这里 $p(a_{17})\ge C_a e^{-1.001a}$、$\epsilon(a)\ge a^{-4}$。源码保存的 $z=y_u/\epsilon$ 对应 $|\Delta z|=|\Delta X_2|/\sqrt\epsilon$。相同 $y(a_{17})$ 已包括完整幅度规范。

令 $g=(\log p)'$。按 $u$ 减小方向写 ODE，其两非对角元为 $-\sqrt\epsilon,+\sqrt\epsilon$，对称部只有第二对角元
$$
 g+\tfrac12(\log\epsilon)'=
 u\cos u-(2-\sin u)-(2\mu-1)\ell/(ru^2).
$$
因而能量范数的对数增长至多 $u(\cos u)_+$。整个 $u\in[5/2,a_{17}]$ 上，增长指数小于
$$
 \int_0^{\pi/2+34\pi}u(\cos u)_+du
 =\pi/2-1+4\pi\sum_{k=1}^{17}k<1924.
$$
向内从 $a_{17}$ 到 109 的短延伸则至多增长 $e^{113}$，此时取上式负号的正部。由此
$$
 \sup_{5/2\le u\le109}|\Delta X(u)| < e^{-2130}.                    \tag{4}
$$
这是未作 display 缩放的准确有限端与真无穷端的差。它包含原数值口略微穿过本模 $a_{17}$ 的情况。

## 3　全部内 cell 与真正的缺失尾

对 $18\le i\le26$ 有 $L_i\le U_i$（只在 (2) 所需的 $i\le25$ 用到 $L_i$）。令 $P_* =\prod_{i=18}^{26}U_i$，则 $\log P_* <9(36)-1.95(6.28\cdot189+9\cdot1.53)<-2010$。把真实和准确有限的 $Y_n=\prod_{i=18}^n\rho_i$ 逐因子相减，(2) 给 $|\Delta Y_n|\le9P_*$。每一项在差因子的左侧含全部较早 $U_i$，该差因子含所有后续 $U_i$，其余因子至多 1。$Y_{26}^{\infty}\le P_*$。

在 $17\le n\le25$ 的整 cell，取 $D=9P_*$；在 $n\ge26$ 取 $D=P_*\prod_{i=27}^{n}U_i$。前段比较两准确解，后段只包围真尾本身。各 cell 两个端值绝对值都至多 $D$，Green 逆给 $\|y\|_\infty\le2D$。按中值定理和 $(py_u)'=-\epsilon py$，
$$
 |y_u|\le e^{2a+23}D(1/3+14\epsilon_{\max})\le e^{2a+23}D ,
$$
其中 $p_{\max}/p_{\min}<e^{2a+23}$，$\epsilon_{\max}\le870000a^{-4}$。

设 $f=r^\mu y,Q=f_r-\mu f/r$、$l=(\log W)_r$，此处 $W=(4/5)e^{-u(2-\sin u)}$。有 $Q=-r^\mu u^2y_u/\ell$、$f_{rr}=-lQ$ 和
$$
 f_{rrr}=(l^2+\mu l/r-l_r)Q+\mu(\mu-1)lf/r^2.
$$
$V=a+7$，$|l|\le6V^3, |l_r|\le27V^5$、$\mu/r<2201$。代入上式（$r^\mu\le1$）给零至三阶统一界 $10^8V^8e^{2a+23}D$。以 $1/W\le(5/4)e^{3(a+7)}$ 除得
$$
 \max_{k\le3}|\partial_r^kf|/W \le e^{64}(a+7)^8e^{5a}D .
$$
对于 $17\le n\le26$，右侧 $<e^{-1000}$。对于 $n\ge26$，相邻界的比小于 $e^{35+56/(a+7)}2T(a)<1$，覆盖无穷多 cell。共同口 $108\le u\le a_{17}$ 上由 (4) 和相同径向公式直接得更强的界。故
$$
 \boxed{\begin{aligned}
 \max_{k\le3}|\partial_r^k(f_\infty-f_{25})|/W &<e^{-1000},
       &&108\le u\le\alpha_{26},\\
 \max_{k\le3}|\partial_r^k f_\infty|/W &<e^{-1000},
       &&u\ge\alpha_{26}.
 \end{aligned}}                                                     \tag{5}
$$
第二行给出的是真幅值余项。$y_{25}(\alpha_{26})=0$ 不规定其斜率，不能把两段拼作一条光滑的有限解。角向 $b$ 阶导数再乘实际 $j^b$。这里没有重写 R648/R650 的几何连接或曲率公式。

## 4　同一原连接头和核心归一

R576 的实际正函数是 $W=B+G+C$，$B=w e^{-6d}$ 是原尾乘抑制阶跃，$G=H s_+s_-$ 为一个先升后降的峰，$C$ 为单调非负的光滑 core 项。原模、冻结 force 背景及 86da 参考所用的各自 $0<H<1$ 只在估计中同界；实际输入仍分别取各自源值。$r\in[.30,.85)$ 有 $B\ge m=(4/5)e^{-7.5-6}>e^{-14}$。负变差满足
$$
 \int[-W'/W]_+ dr
 \le\int |(\log w)'|dr+6+\log(1+H/m)<34 .
$$
尾项按 $u\in(0,5/2]$ 取 $|\partial_u\log w|\le u+3$，积分 $<11$。增益负导数只出现在下降半支，积分 $(-G')/(m+G)$；单调 core 项无需上界其无界末斜率。再由 $0\le C\le(1/2)(1-t)^{-\alpha}$、$t=(r-.55)/(.85-.55)$、$\alpha=.55$，有 $\int_{.30}^{.85} W dr<2$。

设置 $v=ry_r/\sqrt{\mu(\mu-1)}$、$t_0=\log r$。$(y,v)$ 的非对角元为 $\pm\sqrt{\mu(\mu-1)}$，第二对角 $-(2\mu-1)-rW'/W$。在 $.30$ 两种平衡状态只差第二分量的符号。因此整连接直到 rim 均有 $\|(\Delta y,\Delta v)\|<e^{-2090}$。写 $C_h=r^\mu y$ 为未缩放原高度列，
$$
 A_h=-\frac{Wr^\mu\sqrt{\mu(\mu-1)}}{\mu-1}v,\qquad
 (r^{\mu-1}A_h)'=\mu r^{\mu-2}W C_h .
$$
先在 $.30$ 用第一式，随后用第二式积分，得到
$$
 \|\Delta C_h\|_\infty<e^{-2090},\quad
 \|\Delta A_h\|_\infty
 \le |\Delta A_h(.30)|+(\mu/.30)\|\Delta C_h\|_\infty\int W < e^{-2080}.       \tag{6}
$$
(6) 包括 $r\uparrow R$ 的实际 $A_{\rm core}$，不把 $W(R)$ 塞入有限分母。在原紧致 body 区间，
$C_h'=\mu C_h/r-(\mu-1)A_h/(rW)$、$C_h''=(\mu-1)W'A_h/(rW^2)$；由此逐项传入一、二阶，三阶用原 ODE 微分。正图转接处按实际 regular $x$ 系数求导。

原齐次列先除 display，再除对应 $A_{\rm core}$；两次缩放合起来正是未缩放的 $G/A_h(R)$，包括体部和原尾。给任一线性高度或导数泛函 $L$，令 $m_A$ 是准确 **有限 M** 的 $|A_{25}(R)|$ 下界、$m_A>d_A=e^{-2080}$，取 $d_L\ge|L(G_\infty-G_{25})|$ 及 $B_L\ge|L(G_{25})|$。则
$$
 | L(G_\infty/A_\infty-G_{25}/A_{25})|
 \le \frac{d_L+B_Ld_A/m_A}{m_A-d_A}.                                 \tag{7}
$$
$u\ge\alpha_{26}$ 时直接用 (5) 第二行除以 $m_A-d_A$ 包围真归一尾，不给有限柱补一个光滑值。实际区间如输入 display 量 $D_{25}$ 和已缩放 $c_{25}$，须先用 $|A_{25}|=e^{D_{25}}|c_{25}|$；大指数可保留成对数。原未验证浮点收据中 $(D,c)$ 的包围只包括打印浮点值，不能直接成为 (7) 的准确 $m_A$。原齐次 admissible 修正中，$r\ge.65$ 恒取同一 core pair 的第一列，此处齐次截断差严格为 0。$.55<r<.65$ 对原差乘 $1-\chi$，对一、二阶用完整 Leibniz 项；其余误差不随这一消去而消失。

## 5　真实 forced j4 和合同入口

强迫列使用原 j2 admissible 列 $F$、原 264q 的 gain、原 source taper 与原零口特解。令 $a=rF'-4(1+W^2)F$、$b=F'-F/r$。源码二次源为
$$
 2S=\chi\{aF''+4WW'FF'+4(1+W^2)b^2-4WW'F^2/r\}.
$$
在 $[.30,.65]$ 按 $|\Delta(xy)|\le B_xd_y+B_yd_x+d_xd_y$ 逐项支付 (7) 的 j2 三个高度 jets 和原 cutoff 导数。$r\le.30$ 原源恒零；$r\ge.65$ 两个精确的 j2 admissible 强迫输入同取第一 core pair，故该**截断分量**的 $\Delta S=0$。

设 $P$ 是零口的 j4 特解，$h$ 是该 force 背景上的未缩放 j4 齐次解，$\mu=16$。从真实 $A,D$ 方程得到 $(W P')'-\mu W'P/r=S/r$。平衡 $(y,v)$ 的第二式新增 $r^{1-\mu}S/(W\sqrt{\mu(\mu-1)})$。因此在同一连接上，若 $B_S\ge\sup|\Delta S|$，则
$$
 d_{C_P}\le e^{34}\frac{(.30)^{1-\mu} B_S}{m\sqrt{\mu(\mu-1)}}\log(.65/.30),
 \quad d_{A_P}\le (\mu/.30)d_{C_P}\!\int W+(.65-.30)B_S/(\mu-1).
$$
核心结边的真实组合是 $P-t h$，$t=C_P(R)/C_h(R)$。这里 **display 再次抵消**，原有 forced 归一常数最后仍须单独除。$|C_{h,25}(R)|\ge m_h>d_{C_h}$ 时，
$$
 d_t\le[d_{C_P}+B_{C_P}d_{C_h}/m_h]/(m_h-d_{C_h}).
$$
组合误差为 $d_P+B_h d_t+|t_{25}|d_h+d_t d_h$，其各 jets 用原 AC 公式，$C''$ 保留新增的 $S/(rW)$。实际 core-back 初值是 $(A_P(R)-t A_h(R),0)$。在 $.65$ 外强迫源的差为零，仍需把该第一分量之差乘实际 core-pair 第一列。在过渡区保留原 $\chi,\chi',\chi''$ 及其乘积。原固定数 $16533.1541790287$、各个有限系数的实现、浮点归一对象同数学参数之差均保持原合同身份。

(1)–(6) 的有限截断分量不依赖任何数值积分。要把 (7) 与强迫商式接入整份 R643 读数，需同一准确有限源的分母正下界和范数上界，或来自其已验证的数值误差界。原合同还没有这些证据；另六类误差及实际角均值、位置和固定度量误差均不能由此消去。应用时保留真实七行合同，在该行附加截断分量、适用坐标及未闭合的归一依赖，不能将原行直接替换成零。

[原 R600](R600-same-mild-tail-flat-kernels-through-thirty-two.md) · [固定 86da 数学定义](../computations/r618-actual397-frozen-field-definition-20261127.json) · [实际 R643 尾源](../scripts/r643_complete_mean_tail_bounds_20261128.py) · [R643 终态](../notes/2026-11-28-r643-1566-0d9a-rule-terminal.md)
