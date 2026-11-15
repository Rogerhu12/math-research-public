# R119 续篇：参考窄源图中的有限正则 Nash 归纳与完整端口条件

2026-11-15，visible-exact / tail_connector。

**状态：解析证明，已完成独立核对。** 本篇将 E 的真实图平滑、A 的 graph近似右逆、J 的有源缺陷接成一条具体的无限迭代。只用有限角阶：初始状态6396阶、最高平滑背景8192阶、source8130阶。第一参数每步取同一真实值图，第二参数不变；所有均值由原 holonomy图重建。

先给一个有明确初始门的完整 body residual收敛定理，再列出使它成为全 BVP 定理必须满足的准确端口条件。本文不把 body residual为0误作 cap/long/height/$\nu$ 已全部匹配，也不把旧94步候选的非零端残差设为0。

## 1. 固定尺度和唯一实际重建

使用已证明的：

* [E：固定参考图及角向平滑](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md)；
* [A：graph近似右逆与准确端口缺陷](R119-supplement-reference-graph-approximate-right-inverse-and-exact-port-defects.md)；
* [N：二层完整网络](R119-supplement-two-level-full-network-tame-inverse-and-complete-sources.md)；
* [J：三径源与四径状态](R119-supplement-three-radial-source-jets-four-state-jets-and-1734-loss.md)。

记 $\|u\|_s=\|u\|_{E_s}$、$|g|_s=Z_s^{[3]}(g)$，均保持原 finite connector和无限胞元的不同 source单位。$u$ 是固定物理角的普通非mean高度，实际场由 E.11--E.14 的同一 $\gamma_1^*(u)$、mean小根和有向高度积分重建。写
$$
 f(u)=P_\perp{\mathfrak F}(u)=\mathcal L_0u+\mathcal Q(u).
 \tag{B.1}
$$
独立全局高度常数 $\lambda$ 先只规范一次。general charged方向不在这个 holonomy-one值图内。

固定参数
$$
 a=1856,\quad b=6396,\quad d=b-a=4540,\quad
 \mu=1734,\quad \nu=1796,\quad \kappa=5/4 .
 \tag{B.2}
$$
这里 $\kappa$ 仅表示迭代增长指数，不是 holonomy mean小根。
因此
$$
                   b+\mu=8130,\qquad b+\nu=8192 .
 \tag{B.3}
$$
不使用旧 $s\le64$ 结果来冒称整个尺度，也不额外增加未付的四个背景导数。

保持 A/N 的同一个真实 linear outer。若另外更新外背景，N.2 两个独立门必须对所有被调用的背景成立。本篇不由小 $E_a$ 推任意新 cap图的全传播小量。

## 2. 真正使用的三条估计

令 $S_T$ 是 E.7 的同一个角 Fourier投影。它与 $\mathcal L_0$、径向导数及 E中已经声明的线性 traces准确交换。对 $20\le s\le b$，
$$
 \|S_Tu\|_{s+\nu}\le T^\nu\|u\|_s,\qquad
 \|(I-S_T)u\|_s\le T^{s-b}\|u\|_b .
 \tag{B.4}
$$
当 $s+\nu\le b$ 时还可用 E.9 的插值，不能每次都用第一式粗收1796阶。

在低球 $\|v\|_a\le\rho_E/2$、$\rho_E=2^{-8192016}$ 上，A给
$$
 \|{\cal R}_v(g,0)\|_{20}+X_{20}(H)
                       \le C_p|g|_{1794},
$$
$$
 \|{\cal R}_v(g,0)\|_s+X_s(H)
       \le C_p|g|_{s+\mu}
       +C_h\{1+\|v\|_{s+\nu}
              +\mathcal A_{s+1748}
              +\epsilon_L\mathcal D_{s+1748}\}|g|_{1794},
 \tag{B.5}
$$
其中 $64\le s\le b$、$C_p=2^{10485768}$、$C_h=2^{41943040}$，
$H$ 是同一次完整 proxy解，$\mathcal R_v(g,0)=P_\perp H$。
第一式控制 graph norm，包含 $\mathcal L_0{\cal R}_v g$；不是仅控制状态。

其准确缺陷为
$$
 Df(v){\cal R}_v(g,0)=g-P_\perp{\cal E}_v[H],
 \tag{B.6}
$$
并保 J.23/A.17 的
$$
 \begin{split}
 |P_\perp{\cal E}_v[H]|_s\le C_J\{&
 |{\mathfrak F}(v)|_{s+1}X_{16}(H)
  +|{\mathfrak F}(v)|_{17}X_s(H)\\
 &+(1+\mathscr R_{s+8}(v))
                 |{\mathfrak F}(v)|_{17}X_{16}(H)\},
 \quad C_J=2^{1572864}.
 \end{split}                                             \tag{B.7}
$$
ordinary mean仍由 $\Pi_{A_v}$ 保留。A.4--5使完整
$|{\mathfrak F}(v)|_s$ 可用 $4|f(v)|_s$ 控制，含三径导。

非线性差及 Taylor余项用 E.25/A.18。只在 nonlinear代数的低20阶域进行 Taylor probe，不在probe处调用 N inverse、第二相位门或未付高阶小球。

## 3. 固定常数与可检查的初始入口

外行固定时令
$$
 B_*=\sup_{0\le q\le8144}
       (1+\mathcal A_q+\epsilon_L\mathcal D_q)<\infty .
 \tag{B.8}
$$
只需有限集合的整数/相邻半阶上界。若原固定外行不用该记号，取其已付同阶 source/Poisson有限上界。$B_*$ 不进入网络 small gate；只进入以下一次性的迭代预算：
$$
                    C_*=2^{134217728}(1+B_*)^8 .          \tag{B.9}
$$
这是一个明确宽常数。以下所有单步估计先按 $C_p,C_h,K_E,C_J$ 保留各真实因子，最后统一放入 $C_*$；不能把已经统一的 $C_*$ 在每一行再反复相乘。最多两个校正因子、一次 E/A remainder和一次 graph读出，bits小于
$2\cdot41943040+2\cdot2097152+2\cdot1572864+10485768+32
<134217728$。
固定外高因子至多四份，八次方留下余量。

设初始 $u_0\in E_b$，所有 E要求的真实线性 matching/traces成立，且
$$
                         \|u_0\|_a\le\rho_E/8 .
 \tag{B.10}
$$
先选择实数 $T_0\ge16$，满足
$$
 T_0\ge1+\|u_0\|_b+|f(u_0)|_b,\qquad
 T_0^{126}\ge16C_*,\qquad
 T_0^{1266}\ge16C_*/\rho_E .                              \tag{B.11}
$$
再要求实际源入口
$$
                         |f(u_0)|_a\le T_0^{-3000}.
 \tag{B.12}
$$
这里 (B.12)是独立的、真实需要验证的门，不能由 $\|u_0\|_a$ 小推出，更不能由每个旧局部成员都在片内满足 $N=0$ 推出全体 matching残差小。$T_0$ 可以取更大的 dyadic实数；它不是改变已付网络 cutoff或几何的参数。

## 4. 确切迭代，不对校正再作截断

定义
$$
 T_n=T_0^{(5/4)^n},\quad
 v_n=S_{T_n}u_n,\quad f_n=f(u_n),\quad
 w_n=-{\cal R}_{v_n}(S_{T_n}f_n,0),\quad
 u_{n+1}=u_n+w_n .                                       \tag{B.13}
$$
每次 $v_n$ 都重新计算真实第一参数、holonomy mean和高度；不是先截一个已经补好的 mean。$\lambda$ 的全局规范不逐胞重置。

(B.13)没有在 $w_n$ 外再加一个 $S_{T_n}$。若这样做，会额外产生
$Df(v_n)(I-S_{T_n}){\cal R}_{v_n}S_{T_n}f_n$，
它不由现有1734损失门自动变小。本篇使用 (B.13) 的实际输出。

虽然 $u_n$ 只要求 $E_b$，$v_n$ 在 $E_{8192}$ 有限，故可调用 A。最高调用恰为 (B.3)。$f$ 和其一次 derivative在有限 $E_b$ 上使用 A.18的低代数域扩展，不假设 $u_n$ 有8192阶小量。

## 5. 三个归纳量

置 $T_{-1}=T_0^{4/5}$。同时证明
$$
 |f_n|_a\le T_n^{-3000},\qquad
 \|u_n\|_b\le T_{n-1}^{3500},\qquad
 |f_n|_b\le T_{n-1}^{400},
 \qquad \|u_n\|_a\le\rho_E/4 .
 \tag{B.14}
$$
初始前三式由 (B.11)--(B.12)成立，因为3500和400都大于1；低球将在第9节由校正可和给出。

为便于逐项核幂，令 $T=T_n$。则
$$
 \|u_n\|_b\le T^{2800},\qquad
 |f_n|_b\le T^{320},\qquad
 |f_n|_a\le T^{-3000}.                                   \tag{B.15}
$$
两个指数分别准确来自 $3500/(5/4)=2800$ 和 $400/(5/4)=320$。

## 6. 校正的真实低、高界

(B.5)的低读出用 $1794<a$，所以
$$
                    \|w_n\|_{20}+X_{20}(H_n)
                          \le C_*T^{-3000}.              \tag{B.16}
$$
$H_n$ 表示负源 $-\Pi_{A_{v_n}}S_Tf_n$ 的实际 proxy解，$w_n=P_\perp H_n$。
本式没有 $T^\mu$。

在 $s=a$，pure源给 $T^{\mu-3000}=T^{-1266}$。
高背景先插值：
$\nu/d=1796/4540<2/5$，由 (B.10)、(B.14)给
$\|u_n\|_{a+\nu}\le T^{1120}$；
固定 $B_*$ 由 (B.9)单独支付。因此
$$
                    \|w_n\|_a+X_a(H_n)
                          \le C_*T^{-1266}.              \tag{B.17}
$$
没有先粗取 $T^{1796}$ 再称这一项可吸收。

在 $s=b$，pure源给
$$
 T^{b+\mu-a-3000}=T^{4540+1734-3000}=T^{3274}.
$$
背景项至多 $T^{\nu+2800-3000}=T^{1596}$，所以
$$
                    \|w_n\|_b+X_b(H_n)
                          \le C_*T^{3274}.               \tag{B.18}
$$
保留3274再用226幂余量；不能先写 $C_*T^{3500}$ 后把常数删掉。
由 (B.11)，
$\|u_{n+1}\|_b\le T^{2800}+C_*T^{3274}\le T^{3500}$。
两项分别有700幂和226幂余量，均受 $T_0^{126}\ge16C_*$ 控制。

## 7. 平滑背景的 residual不是简单截原 residual

E.23给准确身份
$$
 f(v_n)=S_Tf_n+\mathcal Q(S_Tu_n)-S_T\mathcal Q(u_n).
 \tag{B.19}
$$
线性大项 $\mathcal L_0$ 因准确交换而消去。E.24于是给
$$
 |{\mathfrak F}(v_n)|_{17}\le C_*T^{-3000},\qquad
 |{\mathfrak F}(v_n)|_{a+1}\le C_*T^{-1739}.              \tag{B.20}
$$
第一式的 graph交换误差在20阶至多
$T^{20-b+2800}=T^{-3576}$。
第二式的主交换误差为
$T^{a+1-b+2800}=T^{-1739}$；
$S_Tf_n$ 的该阶部分是 $T^{-2999}$。
E.24第二项用 $a+1$ 对 $a,b$ 的插值，放宽至
$T^{-3575}$，仍更小。
完整 mean由当前 $\Pi_{A_{v_n}}$ 恢复，不把两个不同权投影互换。

最高窗不对不存在的 $u_n$ 的 $b+1$ 阶作估计。直接用 E.21：
$$
 |{\mathfrak F}(v_n)|_{b+1}
 \le C_*T\{|f_n|_b+\rho_E\|u_n\|_b\}
 \le C_*T^{2801}.                                       \tag{B.21}
$$
其中 $Q(v_n)$ 用 $\|S_Tu_n\|_{b+1}\le T\|u_n\|_b$，
$S_TQ(u_n)$ 同理。$\mathscr R_{b+8}(v_n)$ 可用
$C_*T^{2808}$，而低窗 $\mathscr R_{a+8}(v_n)$ 由插值小于
$C_*T^6$，因为 $2800\cdot8/4540<5$。
这些高量均只乘低 source或低方向。

## 8. 准确 residual递推和所有误差项

置
$$
 \delta_n=-P_\perp{\cal E}_{v_n}[H_n],\qquad
 {\cal T}_n=f(u_n+w_n)-f(u_n)-Df(u_n)w_n .
$$
(A.8) 的号数给
$$
 f_{n+1}=(I-S_T)f_n
       +(Df(u_n)-Df(v_n))w_n+\delta_n+{\cal T}_n .
 \tag{B.22}
$$
这是实际 $f(u_{n+1})$ 的等式。没有遗漏 $D\Pi_A$：完整 residual每步由 holonomy重建，其 mean另按 E.26/A.9；(B.22)仅选取普通非mean source坐标。

先逐项用原常数，再统一以 (B.9)支付。低 $a$ 阶最坏幂分别为
$$
\begin{array}{c|c}
\text{来源}&\text{幂}\\ \hline
(I-S_T)f_n&-4540+320=-4220\\
{\cal T}_n&-3000-1266=-4266\\
\|u_n-v_n\|_a\,\|w_n\|_{20}&-4540+2800-3000=-4740\\
\|u_n-v_n\|_{20}\,\|w_n\|_a&-6376+2800-1266=-4842\\
|{\mathfrak F}(v_n)|_{a+1}X_{16}(H_n)&-1739-3000=-4739\\
|{\mathfrak F}(v_n)|_{17}X_a(H_n)&-3000-1266=-4266 .
\end{array}                                             \tag{B.23}
$$
Taylor项另外的 $(1+\|u_n\|_a)\|w_n\|_{20}^2$ 更小。
A.18的第三项以及 (B.7)含 $\mathscr R_{a+8}$ 的项，分别不超过
$C_*T^{-6576}$ 和 $C_*T^{-5994}$。因此
$$
                     |f_{n+1}|_a\le C_*T^{-4220}
                               \le T^{-3750}
                               =T_{n+1}^{-3000}.         \tag{B.24}
$$
最小470幂余量由 $T_0^{126}\ge16C_*$ 覆盖；quadratic自身仍有516幂余量。

在高 $b$ 阶，投影尾准确只有系数1：
$|(I-S_T)f_n|_b\le|f_n|_b\le T^{320}$。
新非线性项中，Taylor最坏是
$T^{-3000+3274}=T^{274}$。
背景差的两项分别为
$T^{2800-3000}=T^{-200}$ 和
$T^{-3576+3274}=T^{-302}$。
(B.21)乘低方向是 $T^{-199}$；
(B.20)的低 source乘 $X_b(H_n)$ 至多 $T^{274}$。
含 $\mathscr R_{b+8}$ 的项至多 $T^{2808-6000}=T^{-3192}$；
Taylor的 high背景乘低方向平方至多 $T^{-3200}$。
于是保留两种不同系数，得到
$$
                      |f_{n+1}|_b
                          \le T^{320}+C_*T^{274}
                          \le T^{400}.                  \tag{B.25}
$$
第一项有80幂余量而不带 $C_*$，由 $T_0\ge16$ 控制；
第二项有126幂余量，正是 (B.11) 的强常数门。
若先粗放成 $C_*T^{320}$ 就不能再用126幂的入口，本篇不作该放宽。
high状态仍可增长，不进入 small gate。

## 9. 收敛、完整 mean和物理读出

$T_n$ 的超几何增长使
$$
 \sum_n\|w_n\|_a
       \le2C_*T_0^{-1266}\le\rho_E/8,\qquad
 \sum_n\|w_n\|_{20}\le2C_*T_0^{-3000}.                    \tag{B.26}
$$
因此所有 $u_n,v_n$ 保 $\|\,\cdot\,\|_a\le\rho_E/4$；
(A.2)及真实第一/第二相位低门在每次 inverse前成立。
$u_n$ 在 $E_a$ 收敛到 $u_\infty$。
$E$ 的 closed graph、(B.1)的 tame连续性和 (B.24)给
$$
           f(u_\infty)=0,\qquad
           {\mathfrak F}(u_\infty)=\Pi_{A_{u_\infty}}0=0 .
 \tag{B.27}
$$
后一式包含 ordinary even mean。holonomy-one 是每步准确重建，
并非在极限用一个未证明的平均兼容性补上。

第一参数是同一低值图的连续极限；第二参数保持原固定值，
没有每步重抽五盒或重选 scalar gap。
无限深径向权仍是原 $C_j,\zeta_j$；E/J状态包含四个 broken径向 jets。
非mean高度读出仍为
$u_\theta=a_{\rm ph}wP$、
$u_t=a_{\rm ph}wK_\perp$、
$u_{tt}=a_{\rm ph}w\{(K_\perp)_t+(A+1)K_\perp\}$。
总物理高度则保
$z_t=a_{\rm ph}w(1+K)$、
$z_{tt}=a_{\rm ph}w\{K_t+(A+1)(1+K)\}$；
mean高度和 metric reference积分按 M/G 保留。
R的原深层 $\zeta_{131}$ 读出与 G.28 的净正幂控制累积平端，
而不是由1856个角导直接冒称物理径向正则。

在原真实线性 traces确实要求连续的截面，closed graph保这些迹；
$F=0$ 后两行给相应实际一侧低径 jets的识别。
本文没有删掉一个本来独立给定的 source原子或宣称一般 broken四阶自动全局连续。最终能授的物理 $C^2$仍按原 R/M/G 的单位和这些真实 traces读出，不授 analytic224、$C^\infty$ 或最高 $E_b$ 极限有界。

## 10. 当前定理究竟关闭了哪些行

(B.27)是完整 body residual定理，所有频率、两行和 holonomy mean均在其中。迭代中的 (A.6)采用原给定 linear端口，但实际 nonlinear重建的端值是
$$
 \dot z=H_n+H_{p,n}+\dot\lambda,\qquad
 \dot{\mathscr C}=b+\mathcal P_{v_n}(w_n)
                   +\hbox{原独立参数/source列}.
 \tag{B.28}
$$
这些不是 (B.22)中的 body缺陷。若在 (B.13)取 $b=0$，
不能因此宣称 $\mathcal P_{v_n}(w_n)=0$。

特别 $H_p$ 是同一个全区有向积分。共同物理截面上的高度差可以准确抵消其共同常数；两不同外端仍有
$H_p(t_R)-H_p(t_L)$。只可用一个 global $\lambda$ 固定一个高度规范。
实际 cap 的非零 Fourier $C$ 输入、两个 mean输出、物理固定 $f_B$、
独立 inner height/moving读出、true returned条件及 $\nu$
均按 A.19--24保为完整行。局部帽定理没有自动确定全局最终端点选择。

(B.26)和 M/G 的低连续性使这些真实端值有极限；这不意味着它们在极限为所需值。初值若仅是旧局部解拼接，(B.12)还必须对其真正 ordinary 源与界面原子核验，端口残差则须按下一节一同迭代。

## 11. 将同一归纳用于全匹配的最小完整条件

为避免一个不具可核内容的“以后作 Schur”，把必要输入明确列出。
设 $\mathcal P_s$ 是 A.3/N.4 的真实外源空间，所有 physical系数、
mean/height、density/scalar、原子及剩余参数单位原样保留。
在完整 source norm 中使用
$$
             |(f,b)|_s=Z_s^{[3]}(f)+\mathfrak B_{s-2}^{[3]}(b)
                   \quad(s\ge2).                        \tag{B.29}
$$
于是 A的 source $s+1734$ 和 low1794准确包含外源
$s+1732$、1792，不再暗加导数。

若给定一个真实 augmented nonlinear map
$\mathscr F_{\rm aug}=(f,\mathscr C,\text{原独立 scalar rows})$，
要套用本篇全部归纳，须验证以下同一域条件：

1. 实际可变外行及其 source有 N.2 的完整两门，包含 adjoint、
   mean、Poisson与全传播；固定给定行本身不支付未知端图。
2. 已核真实 $\mathcal P_u$ 和独立 height/flux/$\nu$/参数列，
   并在一个 global高度规范后的相容端口空间闭合其 Schur。
   对 N的 body/端源块 $\mathcal R_u^{\rm bod},\mathcal R_u^{\rm ext}$，
   仅在相应真列适用时该块准确为
   $I+\mathcal P_u\mathcal R_u^{\rm ext}$，
   右端为 $b-\mathcal P_u\mathcal R_u^{\rm bod}f$。
   其余独立参数列须置于同一个 augmented矩阵，不把非方阵当作这个 $I$。
   必须有真正 onto及 inverse，并保 low读出与相同1734/high1796窗。
3. 在 (B.29) 的完整范数中，真实 nonlinear端行有 E.25/A.18型
   one-high差与余项，且 smoothing commutator有 E.24型界或一个
   已明确更小的界。角 cutoff不自动与非径向 fixed端行交换，
   不能把 body的 $\mathcal L_0S_T=S_T\mathcal L_0$ 当作外行证明。
4. 完整近似逆的残余具有 (B.7)型 residual因子；
   还没有消去的真实端口列不能放进一个不带 residual因子的
   “误差”后沿用 (B.23)。general charges需要其真值图或独立
   affine principal列，不由 $\Pi_A$ 免费变成 holonomy-one切向。
5. 实际初始 augmented residual在 (B.29)满足 (B.11)--(B.12)，
   high有限与 low小均使用真实源单位。旧94步 finite chain、
   已有正/负 cap证书或局部 $N=0$ 不能单独代替此门。

若这五项在共同域内给出，取 $S_T$ 在每个真实 Fourier源分量上作用、
在独立 scalar上为恒等，并以 augmented近似逆替换 (B.13)，
(B.14)--(B.27)逐项成立。所有已付端口常数只需计入一个确定
更大的 $C_*$，再用同一显式初始门；不得更改指数后悄然沿用
旧入口。此条件化结论不预称上述五项已经为原全 BVP 验证完。

## 12. 当前实际进展与保留门

本篇已经支付：有限正则 graph近似逆进入实际 Nash递推，
low source1794的无 $T$ 读出，1734损失与1796背景的全部指数，
三径 source与四径状态、真正 mean重建及固定原第一参数。
没有使用一个尚未证明的无限高阶 tame定理，没有用
$H^{2048}$ 冒充原解析标签，也没有为高背景改变几何或网络 cutoff。

尚须结合实际任务验证的是第11节的全端口 Schur/非线性行以及初始
augmented residual入口。两条帽/尾工作线的已成结果可分别消费
这些准确列；在它们联立以前，本文只登记 (B.27) 的声明域内
body存在性和第11节的完整条件化归纳，不登记全局匹配或最终
$\nu$ 非线性闭合。

## 13. 与旧94步残差的准确比较，不作对象转授

原 [共同 KAM/94步链](R119-supplement-joint-KAM-incoming-and-actual-full-Newton-chain.md)
的全文 Git blob 为
078ce582f9b0b46115167de3b6938a6a2df3186c，J.26--J.29给
$\beta_{94}=66624$、$s_\beta=\beta-88823/400$，
以及真实非零上界
$$
 \|k(a_{94})-K_{B,\perp}(f(a_{94}),\Phi(c,f(a_{94})))\|
       _{\dot A^1_{s_{66624}}}<2^{-5760041760}.           \tag{B.30}
$$
它是该旧共同 KAM、第四重停及真实帽反馈下的**一条外切口非mean斜率残差**。
原篇第7节保留其两个 holonomy mean缺口和有向高度积分；
它不是本篇所有普通体源/全部端荷已经为0的结论。

对同一个旧外量，$\dot A^1_{s_{66624}}$ 确能控制任意
$H^q$、$q\le8130$，且无需大常数：对 $M\ge4$，
$\langle M\rangle^qM^{-1}e^{-s_{66624}M}<1$。
例如此表达式的 log导数小于 $q/M-s_{66624}<0$，
首频值由 $5^{8130}e^{-4s_{66624}}<1$ 核定。
这只把原残差改为同一个端口的有限Sob norm，
不将它改名为内部 $\zeta_j\delta_j^{16}$ 单位的 $Z_q^{[3]}$。

本篇入口与 (B.30) 的差异如下：

| 项目 | 旧 J.29 | 当前 (B.10)--(B.12) |
|---|---|---|
| 几何/参数 | 该篇共同 KAM 与第四重停原对象 | 当前 fixed-stop simple-root、L 的第一参数值图 |
| 未解量 | $B$ 处完整 nonlinear非mean斜率差 | 全 ordinary三径源，及第11节联立时的全部真实端残差 |
| 角空间 | $\dot A^1_{s_{66624}}$ | $Z^{[3]}_{1856}$ 与实际外源 $\mathfrak B_{1854}$ |
| 原始函数 | 两侧各自已有的局部真解 | 满足 E真实线性 traces的一个全区 graph成员 |
| mean/height | 原真小根及另一端高度输出仍保 | 同一个 holonomy重建、唯一 global规范及所有返回行 |

所以必须先做同对象身份或转移、界面 lifting及真实 source单位的收费，
才能把 (B.30) 用于当前初始门。
例如把斜率跳用有限 buffer改为连续场，会产生真实 ordinary源；
其 cutoff导数、三径 jets、两mean与实际端迹均须另外计量。
本文不假定这一步已经完成。

优化到3500/400的意义只是使数值预算不先排斥这个量级。
例如**如果另已验证** $B_*\le2^{6000000}$、
$1+\|u_0\|_b+|f_0|_b\le2^{1500000}$，
取 $T_0=2^{1500000}$ 就满足 (B.11)：
$126\cdot1500000=189000000$，
而 $\log_2(16C_*)<134217728+8\cdot6000001+4<189000000$；
$1266\cdot1500000$ 也大于该数加8192016。
此时真实 low入口为 $|f_0|_a\le2^{-4500000000}$。
(B.30) 与此仅在指数上留1260041760 bits，
该差不能替代上表尚未完成的 identity/source/port证明。
