# R468 — 第三原中央行、三高轴 Hensel 与六条真实 carry

日期：2026-11-14。**状态：已证明。** 对 R466/R469 的固定 $E_{2312}$ 来源，本篇在原共同 $E_1$ 模型中给出准确角多项式、第三条完整中央聚合、三高轴的单位 Jacobian、实际固定高轴坐标，以及同一原 $M$ 上的六条首次提升末行。相对三块在 $\ell=1$ 时出现一个明确二乘二 Schur 矩阵，$\ell=2$ 时是一条，$\ell\ge3$ 时这些首位参数仍可由整行变换吸收。

第三来源增加的是一条真实角中央条件；其 Gaussian charge 四已经是原次数体系中的 charge，不增加全局代数维数。原 $\bar M$ 对这三个高轴仍不变；参考相对 $J$ 可逆时，原 Miller 修正依旧被完整首像吸收。本文保全部 $P_{134}/U_0$、两条十三行边界、第二/第三中央权与高换参尾，未由三个 Jacobian 行推出全次数预算改善。

## 1. 同一固定 theta 上的第三来源

取 R403 的共同 $E_1:y^2=x^3+1$、
$$
w=z^6,\qquad t=-1/x^3,\qquad \Theta=x\sigma^2,
\qquad d=1+8t,\qquad h_7=7+4t+16t^2.
$$
仍令
$$
S=\Theta^{17}f,\qquad T=\Theta^{36}fV,
\quad f=t(t-1)h_7d/7,
$$
$$
V=(1-4t)(1-20t-8t^2)(1+96t+48t^2-64t^3).
$$
第三条准确来源记为 $U$，避免把它与原公共单位 $U_0$ 混同：
$$
\boxed{U=\sigma^{136}x^2P_{21}(x^3)=\Theta^{68}f_U(t),
\qquad f_U(t)=t^{22}P_{21}(-1/t).}
\tag{1}
$$
这里
$$
\begin{aligned}
91P_{21}(X)={}&(X+1)(X^2+20X-8)(7X^2-4X+16)\\
&\cdot(X^4+40X^3+2112X^2+3136X+1792)\\
&\cdot(13X^4+52X^3+1536X^2+1024X+256)\\
&\cdot(X^8+1232X^7-58688X^6-49408X^5-439040X^4\\
&\hspace{18mm}-2111488X^3-1949696X^2-851968X-32768).
\end{aligned}
\tag{2}
$$
因此 $\deg f_U=22$、$f_U=-t+\cdots$，且 $U=w+\cdots$。R466 支付它的完整局部 Schwartz/谱身份；R469 支付同一来源与 $E_{2312}:y^2=x^3+2312$ 的普通及惰性通常 Selmer、完整 Sha 商和周期比较，并给精确 rank 二。于是反证中可以合法同时假定三个原完整中央导数为零；无穷性仍须另外证明。

本篇固定 $p=6s-1>83$，使用原完整模型
$$
\kappa=34[z^{p+1}]\log(\sigma/z)+\Delta,\quad
\Delta\in\mathcal O,\quad a=p\kappa\in\mathcal O^\times,
\quad\alpha=36/17.
$$
三个相对 charge 为
$$
\boxed{q_S=1,\qquad q_T=\alpha,\qquad q_U=4.}
\tag{3}
$$
第三 Gaussian 为 $4\kappa$，与 R469 的 $136c$ 只差 $4\Delta\in\mathcal O$。R342 的完整 Newton 重标适用，且第三来源质量零，所以其完整中央导数不变。

令 $g=d\Theta^{17}e^{-\kappa w^s}$，则三个完整 regularized 来源是
$$
\widehat S=(g/d)f,\qquad
\widehat T=(g/d)^\alpha fV,\qquad
\boxed{\widehat U=(g/d)^4f_U.}
\tag{4}
$$
这些是同一原 $g$ 的三个角测试，不是三个可独立选择的径向函数。

## 2. 新角条件的真实来源成本

$f_U$ 含 $t(t-1)h_7$，但不含 $d$；事实上
$$
P_{21}(8)=-509354311036569656601083904/91\ne0.
$$
故 $U=\mathscr R^4f_U/d^4$ 不能直接认作旧 $n=4$ canonical 列，其在 $d=0$ 的极比 $q_4=t(t-1)h_7/d^2$ 深二。

有两条完整而有成本的有限返回：
$$
\boxed{d^2U=\mathscr R^4q_4\frac{f_U}{t(t-1)h_7}\in\mathcal W_{4,0},}
\tag{5}
$$
因为最后的多项式次数十八不超过 $e_5=20$；以及使用 R453 的固定次数二乘子
$$
W_2=\mathscr R^2t(t-1)^2d h_7^2,
\qquad
\boxed{W_2U=\mathscr R^6q_6\,h_7 f_U\in\mathcal W_{6,0}.}
\tag{6}
$$
此处 $q_6=t(t-1)^2h_7/d^3$，$\deg(h_7f_U)=24\le e_7=29$。
$W_2$ 物理首阶一，故同一整目标的返回仍增加一条物理行和两条 carry；返回到原 $M$ 时使用它的完整单位部分，不能删除 $P_{134}$ 或总 charge 四十。

(5) 的 $d^2$ 在原点为单位，但中央泛函不是角多项式线性的乘法泛函；不能把 $J'_U=0$ 改写成 $J'_{d^2U}=0$。同样，(6) 证明来源成员性，不给 $W_2U$ 或任意幂新的中央零。

## 3. 第三条完整三权聚合

对 $\nu=S,T,U$ 记 $q=q_\nu$，
$$
c_{\nu,j}=[w^{js}]\widehat\nu.
$$
R469 的完整惰性圆盘界与 R403 的整高轴证明给：$j\le5$ 时这些系数整，$j=6$ 时至多有一个 $p$ 分母；所有 $j\ge7$ 的完整 Newton 导数尾属于 $p^4\mathcal O$。所以三条实际导数都准确满足
$$
J'_\nu(0)\equiv\frac p{qa}c_{\nu,1}
-\frac{p^2}{q^2a^2}c_{\nu,2}
+\frac{2p^3}{q^3a^3}c_{\nu,3}\pmod{p^4}.
\tag{7}
$$
于是合法的第三完整失败必要条件是
$$
\boxed{\mathfrak C_U=16a^2c_{U,1}-4pa c_{U,2}
+2p^2c_{U,3}=0\pmod{p^3}.}
\tag{8}
$$
它与原 $S,T$ 的两条聚合并列；没有把三个权分别置零。以下采用统一单位归一
$$
\boxed{F_\nu=\frac{c_{\nu,1}}q-\frac p{q^2a}c_{\nu,2}
+\frac{2p^2}{q^3a^2}c_{\nu,3}.}
\tag{9}
$$
原三个完整导数都为零，严格推出三个 $F_\nu=0\bmod p^3$；反向不把三权精度冒充整个中央函数。

## 4. 三个原高轴与固定实际参数

继续 R434 的原角系数
$$
\log\Theta^{17}=\sum_{n\ge1}\ell_nt^n,\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n},\quad
A_p=p\ell_s,\quad e=(-1)^s.
$$
三个确定的实际角系数为
$$
U_* =\ell_{s-3}+e\frac{8^{s-3}}{s-3},\quad
V_* =\ell_{s-2}-e\frac{8^{s-2}}{s-2},\quad
W_* =\ell_{s-1}+e\frac{8^{s-1}}{s-1}.
\tag{10}
$$
从同一原 $\log g$ 删除这三项，定义唯一参考 $g_\circ$。对计算参数 $(U,V,W)$ 置
$$
h=Ut^{s-3}+Vt^{s-2}+Wt^{s-1},\qquad
g_{U,V,W}=g_\circ e^h.
\tag{11}
$$
只有 (10) 恢复原固定算术对象。其它点仅用于同一个有限评价的坐标恒等式。

原换参 $t=-w-3w^2/7-75w^3/637+\cdots$ 给
$$
h=w^{s-3}(u+vw+xw^2)+w^sH_{u,v,x}(w),
\tag{12}
$$
其中 $H$ 为确定的整级数、线性依赖三个参数，并且
$$
\boxed{u=-eU,\quad
v=\frac{3(s-3)}7u+eV,\quad
x=\frac{3(s-2)}7v+(s-3)\left(\frac{75}{637}-\frac{9s}{98}\right)u-eW.}
\tag{13}
$$
这个三角变换的行列式为 $e\in\{\pm1\}$。$H$ 定义为 (11) 减去前三项后除 $w^s$；全部高尾保留，未用三个纯 $w$ 单项式代替实际角变形。

设 $\chi=(2/p)$。R434 的反向递推给
$$
\frac{\ell_{s-3}}{A_p}
=r_3(p):=\frac{(p+1)(p-6)(p-12)}{(p-3)(p-9)(p-17)(p-15)},
\quad r_3(0)=8/765.
\tag{14}
$$
故实际纯 $w$ 坐标准确满足
$$
\boxed{\begin{aligned}
\bar u_*&=-8\bar a/765+3\chi/2176,\\
\bar v_*&=38\bar a/1155+303\chi/19712,\\
\bar x_*&=-57\bar a/637+937737\chi/3261440.
\end{aligned}}
\tag{15}
$$
所有分母在本范围内均为单位。模 $p^3$ 也有完整固定式：取
$$
\beta_p=eA_p=a+epd_p,\quad B_p=8^s,
$$
以及 R434 的 $r_1,r_2$，先置
$$
u_*=-\beta_pr_3(p)-\frac{B_p}{512(s-3)},\qquad
v_* =\frac{3(s-3)}7u_*+\beta_pr_2(p)-\frac{B_p}{64(s-2)},
$$
$$
x_* =\frac{3(s-2)}7v_*+(s-3)\left(\frac{75}{637}-\frac{9s}{98}\right)u_*
-\beta_pr_1(p)-\frac{B_p}{8(s-1)}.
\tag{16}
$$
这仍是特征零等式；$d_p$ 与 $q_p(2)$ 的准确约化按 R434 读取。三个量都不是自由的 Gaussian 参数。

## 5. 三个完整基准的单位 Hensel 系统

令 $A_\nu$ 是 $g_\circ$ 给出的三个参考 regularized 来源。对 $k=1,2,3$ 定义
$$
C_{\nu,k}(u,v,x)=[w^{ks}]A_\nu
\sum_{m=0}^k\frac{q_\nu^m h^m}{m!},
\tag{17}
$$
其中 $h$ 是 (12) 的整个级数。因 $s\ge15$、$A_\nu$ 从 $w$ 起，$m>k$ 的项不进入所读权；(17) 精确保所有原换参高尾与卷积 carry。将 $C_{\nu,k}$ 代入 (9) 即得三条完整参数多项式。

原前三个低系数为
$$
\begin{array}{c|ccc}
\nu &[w]\nu &[w^2]\nu &[w^3]\nu\\\hline
S&1&-988/105&16594771/1576575\\
T&1&-2938/35&-230804229/175175\\
U&1&135218/105&21083507491/1576575
\end{array}
\tag{18}
$$
这些也等于参考的低系数，因为 $h$ 的首阶至少十二。模 $p$ 的 Jacobian 对全部参数恒为
$$
B_3=\begin{pmatrix}A_{S,3}&A_{S,2}&1\\A_{T,3}&A_{T,2}&1\\A_{U,3}&A_{U,2}&1\end{pmatrix},
\quad
\boxed{\det B_3=-2998254112/4125
=-\frac{2^5\cdot7\cdot19\cdot704477}{3\cdot5^3\cdot11}.}
\tag{19}
$$
因此对 $p>83,p\ne704477$，有唯一
$z^\dagger=(u^\dagger,v^\dagger,x^\dagger)\bmod p^3$ 使三个完整 $F_\nu$ 均为零。具体为先解模 $p$ 的仿射系统，再逐位使用
$$
z_{r+1}=z_r-p^rB_3^{-1}
\begin{pmatrix}F_S(z_r)/p^r\\F_T(z_r)/p^r\\F_U(z_r)/p^r\end{pmatrix}
\pmod{p^{r+1}},\qquad r=1,2.
\tag{20}
$$
原三个完整中央同时失败，必迫实际 (16) 等于这个唯一解模 $p^3$。每一步必须使用完整 (17)，不能只读第一权或删除原三个基准。

第三条低角行的独立性并不在 $704477$ 消失。改用第一列 $A_{\nu,4}$ 时，
$$
\det B_{4,2,1}=100202962632448/3155625,
\quad\gcd(2998254112,100202962632448)=32.
\tag{21}
$$
两式所有分母的素因子都小于 $84$。所以三个来源在前四个实际系数中对全部 $p>83$ 秩三；在这个单一异常素数可改用 $t^{s-4},t^{s-2},t^{s-1}$ 三轴。以下为保最短六行窗口，使用 (19) 的主选择并删除这一个固定素数，不把它当成未知无限坏集。

这一独立性是相对于显示的三个完整角测试。charge 四也出现在已付 $S(2z)$；原分布关系仍约束实际 $g$，不能把 (20) 的计算参数认成三份独立算术选择。

## 6. 原整个 M 的准确参数式与六条首次提升末行

保持原目标
$$
\Gamma_{L+13}=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^{\ell+13}\epsilon^2),\quad
L=2s+\ell,\quad1\le\ell<s-13,
$$
以及同一个完整评价
$$
M_\circ^{\rm orig}=c_*U_{0,\circ}m_{13}J_\circ.
$$
来源可以是原有限 $\mathcal W_{D,J}$，也可以明确添入 (1) 的实际单列；不得省略其 (5)–(6) 的返回成本。每列相对 charge 为原 $n+\alpha j$，第三单列为四；总 charge 始终再加四十，记 $\mathcal E_{\rm tot}$。

令 $P_2(w)=u+vw+xw^2$。在整个目标中，准确有
$$
\begin{aligned}
M_h^{\rm orig}=c_*U_{0,\circ}\{&m_{13}J_\circ
+p\epsilon(w^{10}P_2+w^{13}H)J_\circ\mathcal E_{\rm tot}\\
&+\frac{p^2\epsilon^2}{2}
(w^7P_2^2+2w^{10}P_2H+w^{13}H^2)
J_\circ\mathcal E_{\rm tot}^2\}\pmod{p^3}.
\end{aligned}
\tag{22}
$$
证明是逐列乘 $e^{Qh}$，并准确使用 $w^s=p\epsilon$。
三次项首阶至少 $13+3(s-3)=3s+4$，超出完整目标，故没有省略未付的三阶项。式中 $H$ 的全部一次、二次及交叉项保留。

特别，
$$
\boxed{\bar M_h^{\rm orig}=\bar M_\circ^{\rm orig}.}
\tag{23}
$$
对相同真实首核向量 $P$，按 R425 将完整参考列记为
$w^{13}A_\Phi(w)e_2(Q_\Phi a\epsilon)$，并置
$$
W_i(P)=\sum_\Phi P_\Phi Q_\Phi^i A_\Phi(w).
$$
这里保留 $P_{134}/U_0$ 和总 charge 四十。真实 $K_1(M)$ 给
$$
W_0,W_1\in w^{s-13}k[[w]],\qquad W_2\in w^\ell k[[w]].
\tag{24}
$$
令 $d_{1,i}=[w^{s-13+i}]W_1$、$d_{2,i}=[w^{\ell+i}]W_2$，$i=0,1,2$，负下标取零。则完整首次提升变化为
$$
\boxed{\begin{aligned}
(\beta_1^h-\beta_1^\circ)(P)=\Big[&
\sum_{i=0}^2(u d_{1,i}+v d_{1,i-1}+x d_{1,i-2})
\epsilon w^{s-3+i}\\
&+a\sum_{i=0}^2(u d_{2,i}+v d_{2,i-1}+x d_{2,i-2})
\epsilon^2w^{\ell+10+i}\Big].
\end{aligned}}
\tag{25}
$$
方括号仍商去同一个完整首像。式 (22) 除 $p$ 后，$H$ 部分是
$\epsilon w^{13}HW_1+a\epsilon^2w^{13}HW_2$；由 (24) 恰在两块端点消失。所以不是先删掉高尾再猜 (25)。六个目标行准确为
$$
\boxed{2s-3,\ 2s-2,\ 2s-1,\ L+10,\ L+11,\ L+12.}
\tag{26}
$$
第二次提升仍使用整个 (22)、三个完整第三权及原 Hensel 第三位；(25) 没有替代它们。

## 7. 同一相对 J 的全部剩余首位 Schur 项

本节只对相对 $J$ 作整行变换，不把它与原 $M$ 的 carry 商混同。对源 $P$ 记
$V_i(P)=\{\mathcal E_{\rm rel}^iP\}_{\rm reg,\circ}$。模 $p$ 的三个块是
$$
(V_0+hV_1)_{<s},\quad
a(V_1+hV_2)_{<s},\quad (a^2/2)(V_2)_{<\ell}.
\tag{27}
$$
$h^2$ 在前两块已经超窗，$h$ 在第三块超窗。先以第二块消第一块的 $hV_1$，再以第三块已有的 $V_2$ 系数消第二块。两次都是对角一的整行变换。置
$$
\vartheta_1(P)=a[w]V_2(P),\qquad
\vartheta_2(P)=a[w^2]V_2(P).
$$
其准确剩余为
$$
\boxed{\bar J_h\sim\begin{cases}
\bar J_\circ,&\ell\ge3,\\
\bar J_\circ+u e_{2s-1}\vartheta_2,&\ell=2,\\
\bar J_\circ+u e_{2s-2}\vartheta_1
+e_{2s-1}(u\vartheta_2+v\vartheta_1),&\ell=1.
\end{cases}}
\tag{28}
$$
三个参数中的 $x$ 在首位均被已存在的第三块常数行消掉；不能把它另计为独立首位缺陷。

若 $N=L$ 且参考 $\bar J_\circ$ 可逆，$\ell=2$ 的行列式比为
$1+u\vartheta_2\bar J_\circ^{-1}e_{2s-1}$。对 $\ell=1$ 置
$$
B=\begin{pmatrix}\vartheta_1\\\vartheta_2\end{pmatrix}
\bar J_\circ^{-1}\begin{pmatrix}e_{2s-2}&e_{2s-1}\end{pmatrix}.
$$
则真正的二乘二 Schur 比为
$$
\boxed{\frac{\det\bar J_h}{\det\bar J_\circ}
=\det\left(I_2+\begin{pmatrix}u&0\\v&u\end{pmatrix}B\right)
=1+u\operatorname{tr}B+vB_{12}+u^2\det B.}
\tag{29}
$$
实际参数必须代 (15)；只有三个完整中央失败时，它们也等于 (20) 的中央条件解。参考矩阵若不单位，应保无分母行更新或完整 (25)，不使用这个逆。

完整 $t$ 高尾在模 $p^2$ 相对矩阵上仍是 R434 的左单位
$$
J_t\equiv\left(I+\frac p a\bar H E_\epsilon\right)J_w\pmod{p^2}.
\tag{30}
$$
因此真方阵的行列式只多乘
$1+(p/a)(s+2\ell)H(0)$。在余秩一掉秩线上，除 $p$ 的下一位不受该额外单位改变；若二乘二矩阵的余秩更大，则保完整首次提升矩阵，不能再以单一 $\eta$ 替代。

## 8. 真原像与全局预算的准确结论

首先，(23) 使原整个首像和 $\gamma=\dim(I_{13}/\operatorname{im}\bar M)$ 对三个高轴完全不变。特别，参考 $J_\circ$ 为整单位时，原首像已是整个 $I_{13}$，所以 $\gamma=0$；即使 (29) 后来掉秩，R444 的实际 $p^2A_0$ Miller 修正仍通过同一原首像全部吸收。新的二乘二相对 Schur 不自动成为原可见第二障碍。原比较继续是 R449 的
$$
K_2^{\rm red}(M)=\ker(\pi\beta_J)\subset\ker\bar J,
\qquad G_2=C_2(J)/\overline H,
$$
两条十三行 carry 和第三位均不可省略。

其次，三个全局来源仍只有代数维数二。R418 已证 $t,\Theta$ 的代数独立以及 $t,\Theta$ 对 $\mathbf C(S,T)$ 代数；而 (1) 直接给
$$
\boxed{U/S^4=f_U/f^4\in\mathbf Q(t).}
\tag{31}
$$
故 $\operatorname{trdeg}\mathbf C(S,T,U)=2$。三条来源在 $w$ 平面仍有有限型增长阶至多 $1/3$；多项式来源次数增加时，完整 theta charge 最高包含 $136\deg_U$，必须计入型常数。

R469 的普通整测度与同一单位周期给真实乘积的普通前缀阶乘抵消；惰性处三个来源都由同一个原 Gaussian 半径控制，第三来源 (1) 的固定角多项式仍有无条件包络 $3k\log k+O(k+D)$。三个形式变量生成的真实代数只有二次的 Hilbert 秩增长，不能按三个代数独立坐标计算；若另选三生成元的商格，还必须支付它与所选整数/实范数格的完整比较。

本篇沿用 R418 的同一个真正 $(S,T)$ 平面源格及其全部饱和前缀，增加的是合法的第三完整中央假设。因此若用三个完整失败去改善该格的全次数范数，原严格门仍是
$$
\boxed{a_I+2b_I<3.}
\tag{32}
$$
本篇支付了一个真实第三角约束、其全部三权基准与有限原矩阵接口，没有仅凭三行独立就证明 (32)。下一项必须使用这些实际固定参数、三个完整基准和同一个真实来源格，证明可见像缺口或全次数范数改善；不把新增固定来源条数当作已经支付的主阶收益。

## 核验与依赖

伴随脚本 `scripts/check-r468-third-central-six-carry.py` 从 (2) 重建真实第三来源，核低四项、两个精确 Jacobian 小式、实际三角高轴递推、原 $P_{134}$ 下全部六行首提升变化及三个完整权的 Hensel 解。它只核公式，不对目标素数作宽扫描。

- R466/R469/R470：第三固定来源的真实谱、局部身份、完整 Selmer/Sha 桥及原 degree136 返回。
- R403/R425/R434：共同原 Gaussian、完整三权、高尾及固定角坐标。
- R444/R449：完整首像吸收与原第二余核精确序列。
- R453/R418：准确固定来源返回及全次数复/算术预算。
