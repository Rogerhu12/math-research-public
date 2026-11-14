# R150 附录：真实循环块根、全柱任意二元多项式与唯一线性中心

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。

状态：完整证明；根代理与 kernel_resume_1cf 已全文独立核查。

范围扣除：[原中心谱稿](R150-appendix-linear-slope-center-ratios-and-equal-weight-bell-cyclicity.md)已付等权首一多项式及有限谱 $YL$ 部分的唯一中心；[通用 Newton 多边稿 §§2、7—8、11](R150-appendix-superlinear-newton-polygon-zero-cluster-descent-and-all-powers.md)已付全部严格超线性边和非首一首系数。本稿在真实全柱分支合并两者并停止于权一，取消原标量 $F$ 的首一、总次数和最高纯 $x$ 限制。一般原空谱 first 只需要其已知有界逆；不另假定最大增生或存在原空间上的分数根。

## 1. 原两行及完整结论

保持原模型的复 first
$$
u=u_*+\sum_j\zeta_j\chi_j,\qquad
v=v_*+\sum_j\nu_j\chi_j,\qquad \zeta,\nu\in\ell^2(\mathbb C),
$$
以及
$$
Z=X_u,\qquad Y=X_v,\qquad
\sigma(Z)=\varnothing,\qquad L=Z^{-1}\in\mathfrak C=A'.
$$
$L$ 有界、单射、稠密像、拟幂零。

取递增穷尽的有限物理位集 $F_n$，记
$$
d_n=|F_n|,\quad
\sigma_n=u_*+\sum_{F_n}\zeta_j,\quad
\tau_n=v_*+\sum_{F_n}\nu_j,\quad
g_n=\|\zeta_{F_n^c}\|_2+\|\nu_{F_n^c}\|_2.
$$
假设
$$
\boxed{
|\sigma_n|\to\infty,\qquad
\frac{\sum_{F_n}(|\zeta_j|+|\nu_j|)}{|\sigma_n|}\le C,\qquad
\frac{\sqrt{d_n}\,g_n}{|\sigma_n|}\to0.
}
\tag{1.1}
$$
允许先取一条满足这些条件的递增子列再重新编号。于是
$$
\beta_n=\tau_n/\sigma_n
\tag{1.2}
$$
有界。

对任意非恒定标量多项式 $F(x,y)$，令 $d=\deg_{\rm tot}F\ge1$，$F_d$ 为其最高普通齐次部分，并记非零标量多项式
$$
H_F(s)=F_d(1,s).
$$

**定理 1。** 对固定任意 $\lambda\in\mathbb C$、整数 $r\ge1$ 和原复 $\ell^2$ first 指数权 $w$，若原向量
$$
[F(u,v)-\lambda]^r e^w
$$
不循环，则必有
$$
\boxed{
\beta_n\longrightarrow\beta,\qquad H_F(\beta)=0.
}
\tag{1.3}
$$

因而：

1. 若 $\beta_n$ 不收敛，则每个非恒定 $F\in\mathbb C[x,y]$ 的全部常数移位、普通点态幂和这些复指数权均循环。
2. 只要 $\beta_n$ 有一个聚点 $\beta$ 满足 $H_F(\beta)\ne0$，同样得到该 $F$ 的全 $\lambda,r,w$ 循环性。
3. 若 $\beta_n\to\beta$，最高符号条件 $H_F(\beta)\ne0$ 足够；没有把 $H_F(\beta)=0$ 宣称为非循环的充分条件。

结论不要求 $F$ 关于任一变量首一，也允许其最高普通齐次部分含任意多个单项式。证明中没有对原无界最高系数 $f_M(Z)$ 求逆。

## 2. 原完整 Bell 与直接的非零中心检验

固定 $F,\lambda,r,w$。先按原 $u,v,w$ 构造 $[F(x,y)-\lambda]^r$ 的全部 Bell 系数，记原规范最大实现为 $\mathcal P$、其共同深域上的有限核心为 $P(Z,Y)$。

指数倾斜只给原 $Z,Y$ 的有界 $\mathfrak C$ 平移；正阶 Bell 微分严格降低普通总次数。令 $D_0=rd$，则
$$
P_{D_0}(x,y)=F_d(x,y)^rI.
\tag{2.1}
$$
全部其余系数有界、属于 $\mathfrak C$，总次数小于 $D_0$。原 $F-\lambda$、普通点态幂和原 cumulant 均保持，没有先改换行再重新计算 Bell。

这里先给定理1的第2项一个直接证明。设 $\beta_n\to\beta$ 沿某子列且 $H_F(\beta)\ne0$，并反设 $\ker\mathcal P\ne0$。令 $\Pi$ 为该闭核的正交投影。对原通常伴随的共同深词域，原形式伴随多项式 $P^*$ 与 $\mathcal P^*$ 一致，因此
$$
\Pi P^*=0.
\tag{2.2}
$$
写
$$
Z^*/\overline{\sigma_n}=I+A_n+T_n,\qquad
Y^*/\overline{\sigma_n}=\overline{\beta_n}I+B_n+U_n,
$$
其中 $A_n,B_n$ 为真实有限头，$T_n,U_n$ 为对应尾。

考虑
$$
\mathscr T_n
=I-\frac{P^*}
{\overline{\sigma_n}^{\,D_0}\,\overline{H_F(\beta)^r}}.
\tag{2.3}
$$
由 (2.1)，其在 $A_n,B_n,T_n,U_n$ 中的常数系数是
$$
\delta_n
=\left[1-\frac{\overline{H_F(\beta_n)^r}}
{\overline{H_F(\beta)^r}}\right]I+O(|\sigma_n|^{-1})
\longrightarrow0
\quad\text{按算子范数}.
\tag{2.4}
$$
误差来自原低次有界系数；其余单项式次数在 $1$ 到 $D_0$ 之间，系数一致有界。它们属于真实伴随交换代数并保持所需全部词域。

选整数 $p_n$ 使
$$
p_n/d_n\to\infty,\qquad
g_n\sqrt{p_n}/|\sigma_n|\to0.
\tag{2.5}
$$
R251 的任意位集头四次进位、补集混合尾预算及[全柱多项式稿 §§2—3](R150-appendix-polynomial-column-tests-and-invertible-normalized-parts.md)的三组展开，给
$$
\boxed{\|\mathscr T_n^{p_n}Q_{F_n}\|^{1/p_n}\to0.}
\tag{2.6}
$$
具体地，展开中若常数因子数至少 $p_n/3$，由 $\|\delta_n\|^{p_n/3}$ 控制；否则头总次数或尾总次数至少 $p_n/3$。前者最终超过 $2d_n$，由 $e^{-c p_n^4}$ 控制；后者由
$(C g_n\sqrt{D_0p_n}/|\sigma_n|)^{p_n/3}$ 控制。固定次数带来的所有系数和只增一个 $C_{D_0}^{p_n}$ 因子，故 (2.6) 成立。

R251 已付 $Q_{F_n}H$ 的任意固定深真实伴随词域；所有有限迭代均合法。(2.2) 逐次给
$$
\Pi Q_{F_n}=\Pi\mathscr T_n^{p_n}Q_{F_n}\to0.
$$
由 $Q_{F_n}\to I$ 强，得 $\Pi=0$，矛盾。

这直接证明任一非零最高中心都可排核。余下 §§3—7 支付更强的“失败迫整个比序列收敛”，包括所有聚点都落入最高符号零集而比序列仍不收敛的情况。

## 3. 一般原空谱 first 的真实有界循环块根

固定任意正整数 $Q$，在 $H^Q$ 上定义
$$
\boxed{
\mathbb B(h_0,\ldots,h_{Q-1})
=(Lh_{Q-1},h_0,\ldots,h_{Q-2}).
}
\tag{3.1}
$$
$Q=1$ 时就是 $L$。直接相乘给
$$
\boxed{\mathbb B^Q=\Delta_Q L.}
\tag{3.2}
$$
这里 $\Delta_Q$ 表示同一算子的 $Q$ 份对角放大。

由 (3.2)，$\mathbb B$ 单射，像稠密，并且
$r(\mathbb B)^Q=r(\Delta_Q L)=0$，所以它拟幂零。其矩阵条目为 $I,L,0$，保持每个原 first 的全部自然域和有限共同词域，并在这些域上与 $\Delta_Q Z,\Delta_Q Y$ 交换。

使用的系数代数是
$$
\boxed{
\mathfrak D_Q=
\overline{\operatorname{alg}}^{\|\cdot\|}
\bigl(\Delta_Q\mathfrak C,\mathbb B\bigr).
}
\tag{3.3}
$$
生成元彼此交换，故这是一个交换闭 Banach 代数。并未把整个
$M_Q(\mathfrak C)$ 称为交换代数。$\mathfrak D_Q\subseteq M_Q(\mathfrak C)$，所以全部元素仍保持原对角 first 的所需词域。

若 $A(t)=\sum_{n\ge0}A_nt^n$ 是原 $\mathfrak C$ 系数的局部解析函数，定义
$$
A[\mathbb B]=\sum_{n\ge0}(\Delta_Q A_n)\mathbb B^n.
\tag{3.4}
$$
原系数至多按固定指数增长，而 $\mathbb B$ 拟幂零，故级数按算子范数收敛，属于 $\mathfrak D_Q$。它保持加乘恒等式及全部上述域。以后关于无界算子的运算始终只有有限多项式，解析级数仅在这个实际有界块根上代入。

### 3.1 未知子图中的准确自然根域

设 $\mathcal M$ 为某固定有限进一步放大中的非零闭空间，被全部对角 $\mathfrak C$ 以及相应的 $\mathbb B$ 保持。记
$$
L_\mathcal M=(\Delta L)|_\mathcal M,\qquad
B_\mathcal M=\mathbb B|_\mathcal M.
$$
R186 同一正则族给 $Z^jR(t)^N\in\mathfrak C$ 全域有界；因此真实 $Z$ 部分的域在 $\mathcal M$ 中稠密，而该域正是
$\operatorname{Ran}L_\mathcal M$。这一步对一般非最大增生 $Z$ 已在全柱多项式稿 §4 支付。

于是 $B_\mathcal M$ 单射、像稠密，因为
$$
B_\mathcal M^Q=L_\mathcal M,\qquad
\operatorname{Ran}L_\mathcal M\subseteq\operatorname{Ran}B_\mathcal M.
$$
令 $X_\mathcal M=B_\mathcal M^{-1}$，则在完整自然域上
$$
\boxed{
\operatorname{Dom}X_\mathcal M^Q
=\operatorname{Ran}B_\mathcal M^Q
=\operatorname{Dom}Z_\mathcal M,\qquad
X_\mathcal M^Q=Z_\mathcal M.
}
\tag{3.5}
$$
没有赋予 $X_\mathcal M$ 或 $Z_\mathcal M$ 未证明的增生性质。

## 4. 块根上的全部超线性完整单位部分由原柱预算排除

对整数 $p>Q$ 定义自然闭算子
$$
S_p=(\Delta_Q Y)\mathbb B^p.
\tag{4.1}
$$
闭性来自原 $Y$ 闭和 $\mathbb B^p$ 有界；原共同正则器支付稠密域。

**引理 4.1。** 不存在非零闭 $\mathcal M$，同时满足全部对角 $\mathfrak C$ 不变、$\mathbb B$ 不变、
$$
\mathcal M\subseteq\operatorname{Dom}S_p,\qquad
S_p\mathcal M\subseteq\mathcal M,
$$
而完整部分 $J=S_p|_\mathcal M$ 有界可逆。

证明：$J$ 与 $B_\mathcal M$ 交换。对
$x\in\operatorname{Dom}X_\mathcal M^p=\operatorname{Ran}B_\mathcal M^p$，
写 $x=B_\mathcal M^p y$，就有准确的
$$
Yx=S_py=Jy=JX_\mathcal M^p x.
\tag{4.2}
$$
这也直接支付了该完整域上的 $Y$ 输入域。$J$ 保持 $X_\mathcal M$ 全部自然幂域并与之交换；逐次在
$\operatorname{Dom}X_\mathcal M^{pQ}$ 上应用 (4.2)，得到
$$
\boxed{
Y^Q=J^QX_\mathcal M^{pQ}=J^QZ_\mathcal M^p
\quad\text{于全部 }\operatorname{Dom}Z_\mathcal M^p.
}
\tag{4.3}
$$
没有把一个形式分数幂域代入原伴随。

取到 $\mathcal M$ 的正交投影 $\Pi$。对任意 $h\in\mathcal M$，先用同一个 $R(t)^N h$ 进入全部所需原 $Z,Y$ 词域。由于 $J$ 与正则器和 $Z_\mathcal M$ 交换，真实双配对 (4.3) 后令 $t\to0$，得到
$$
\boxed{
\Pi(Y^*)^Q=(J^*)^Q\Pi(Z^*)^p
}
\tag{4.4}
$$
于原共同伴随深域。

考虑全柱测试
$$
\mathscr P_n(z)
=I-\left(\frac{Z^*}{\overline{\sigma_n}}\right)^p
+z\,\frac{(Y^*)^Q}{\overline{\sigma_n}^{\,p}}.
\tag{4.5}
$$
按原有限头/尾展开，其常数项为
$$
z\,\overline{\sigma_n}^{\,Q-p}\overline{\beta_n}^{\,Q}\to0
$$
（在每个固定 $|z|\le R$ 上一致），其余次数不超过 $p$，系数一致有界。
所以 (1.1)、R251 及同一三组展开给
$$
\sup_{|z|\le R}
\|\mathscr P_n(z)^{m_n}Q_{F_n}\|^{1/m_n}\to0
\tag{4.6}
$$
其中 $m_n/d_n\to\infty$ 且 $g_n\sqrt{m_n}/|\sigma_n|\to0$。
这里的 $Q_{F_n}$ 按固定有限放大解释，其算子范数预算不改变。

(4.4) 给
$$
\Pi=\Pi\!\left[I-(Z^*/\overline{\sigma_n})^p\right]
+(J^*)^{-Q}\Pi\frac{(Y^*)^Q}{\overline{\sigma_n}^{\,p}}.
$$
逐次回传后用有限 Cauchy 系数公式，取
$R>\|J^{-Q}\|$，得
$$
\|\Pi Q_{F_n}\|
\le\frac{\sup_{|z|=R}\|\mathscr P_n(z)^{m_n}Q_{F_n}\|}
{1-\|J^{-Q}\|/R}\to0.
$$
与 $Q_{F_n}\to I$ 强矛盾。证毕。

额外的 $\mathbb B$ 不变是本引理明确的前提；下面每个实际核相伴图都会直接满足它。

## 5. 任意原多项式的 Newton 下降只运行到权一

若 $F$ 只依赖 $x$，则 $H_F$ 为非零常数，§2 已排核。以下设
$$
F(x,y)=\sum_{j=0}^{M}f_j(x)y^j,\qquad M\ge1,\quad f_M\ne0,
$$
允许 $f_0=0$。记 $d_j=\deg f_j$，零多项式次数为 $-\infty$，以及
$$
m(\tau)=\max_j(d_j+\tau j).
$$

从 $\tau=+\infty$ 下降到 $1$，列出全部真正转折
$\tau_1>\cdots>\tau_s>1$，最后加入终点
$$
\tau_{s+1}=1.
$$
若没有严格大于1的转折，就只有这个终点。终点可以是原包络的一个转折，也可以处于原两个转折之间。

选固定正整数 $Q$，使全部
$p_i=Q\tau_i$ 为整数，特别 $p_{s+1}=Q$。
置
$$
\mu_i=Qm(\tau_i),\quad
I_i=\{j:Qd_j+p_i j=\mu_i\},\quad
h_i=\max I_i,\quad \ell_i=\min I_i.
$$
首层 $h_1=M$。相邻两个所列参数之间唯一活动指标为 $\ell_i$，所以
$$
\boxed{
h_{i+1}=\ell_i,\qquad
\mu_i-\mu_{i+1}=(p_i-p_{i+1})\ell_i
\quad (i\le s).
}
\tag{5.1}
$$
若终点不是转折，$I_{s+1}$ 只有一个指标；该公式仍成立。终点没有“必须到零指标”的要求。

令 $c_j$ 为 $f_j$ 的最高 $x$ 系数，定义
$$
H_i(s)=\sum_{j\in I_i}c_js^j.
$$
终点准确为
$$
\boxed{H_{s+1}(s)=F_d(1,s)=H_F(s).}
\tag{5.2}
$$

固定 §2 的原完整 Bell $P$。置
$$
D=rM,\quad M_i=r\mu_i,\quad
D_i=rh_i,\quad E_i=r\ell_i.
$$
原正阶 Bell 微分及原有界倾斜平移严格降低每一个权 $(Q,p_i)$，包含终点的等权情形。因此
$$
\boxed{
\widehat P_i(t,s)=t^{M_i}P(t^{-Q},t^{-p_i}s)
\in\mathfrak C[t,s],\qquad
\widehat P_i(0,s)=H_i(s)^rI.
}
\tag{5.3}
$$
所有归一指数非负。由 (5.1)，完整有限式有
$$
\widehat P_i(t,t^{q_i}s)
=t^{q_iE_i}\widehat P_{i+1}(t,s),
\qquad q_i=p_i-p_{i+1}>0.
\tag{5.4}
$$

### 5.1 非首一首层只取消一个有界单位

若 $c_M=[x^{d_M}]f_M$，原 $Y^D$ 系数为
$$
A(Z)=c_M^rZ^{rd_M}+\sum_{\ell<rd_M}A_\ell Z^\ell,
\qquad A_\ell\in\mathfrak C.
$$
正阶 $y$ 微分降低 $y$ 次数，其他微分和平移只降低相应 $x$ 次数，故这个首项准确。

首层 $M_1=rQd_M+p_1D$。令
$$
a(t)=t^{Qrd_M}A(t^{-Q})
=c_M^rI+\sum_{\ell<rd_M}A_\ell t^{Q(rd_M-\ell)}.
\tag{5.5}
$$
它在0附近有解析逆；在真实块根上
$$
a[\mathbb B]=c_M^rI+\mathbb B^Q C[\mathbb B]
$$
为有界单位，因为第二项拟幂零。故可取
$$
U_1(t,s)=a(t),\qquad
Q_1(t,s)=a(t)^{-1}\widehat P_1(t,s).
\tag{5.6}
$$
$Q_1$ 关于 $s$ 首一、次数 $D$。这是通用多边稿 §11 的有界首系数归一；此处代入 §3 的实际块根仍逐项合法。

## 6. 真实零簇整除、原向量不变与严格超线性层排除

反设原 $\ker\mathcal P$ 含 $f\ne0$。原所有倾斜 first、$Z,Y$ 纳入同一个 R186 正则族，固定其单射正则器 $\mathcal R$，取一次
$$
N\ge rd+3D+2,\qquad
g=(\mathcal R^Nf,0,\ldots,0)\in H^Q.
\tag{6.1}
$$
于是 $g\ne0$，在全部所需原对角词域中，并有
$$
P(\Delta_Q Z,\Delta_Q Y)g=0.
$$
设 $S_i=(\Delta_QY)\mathbb B^{p_i}$。原项 $Z^aY^b$ 的归一系数为
$\mathbb B^{M_1-Qa-p_1b}$，指数非负；用 $\mathbb B^Q=\Delta_Q L$ 得
$$
\widehat P_1[\mathbb B](S_1)g
=\mathbb B^{M_1}P(\Delta_Q Z,\Delta_Q Y)g=0.
$$
由 $a[\mathbb B]$ 的真实有界逆，
$$
Q_1[\mathbb B](S_1)g=0.
\tag{6.2}
$$

对每个严格超线性层 $i\le s$，按通用多边稿 §§5、7 的有限 Banach Hensel 分解，维持
$$
\widehat P_i=U_iQ_i,\qquad
Q_i\text{ 首一、次数 }D_i,\qquad
U_i(0,s)=c_iI,\quad c_i\ne0,
$$
$$
Q_i(0,s)=c_i^{-1}H_i(s)^rI.
\tag{6.3}
$$
按不同非零根分簇，
$$
Q_i(t,s)=R_i(t,s)\prod_{\kappa\ne0}P_{i,\kappa}(t,s),
$$
$$
R_i(0,s)=s^{E_i},\qquad
P_{i,\kappa}(0,s)=(s-\kappa)^{d_{i,\kappa}}.
\tag{6.4}
$$
因子首一且系数局部解析；有限 CRT 给次数小于 $D_i$ 的投影多项式和恒等式
$\sum_\nu E_{i,\nu}(t,s)=1$。

令 $g_{i,\nu}=E_{i,\nu}[\mathbb B](S_i)g$，则
$$
g=\sum_\nu g_{i,\nu},\qquad
P_{i,\nu}[\mathbb B](S_i)g_{i,\nu}=0.
\tag{6.5}
$$
CRT 后再施加一个因子的总 $Y$ 次数小于 $2D$，所以 (6.1) 同时支付全部域。

若某个 $\kappa\ne0$ 的 $g_{i,\kappa}$ 非零，取该自然首一核的真实相伴图
$$
\Gamma=\{(h,S_ih,\ldots,S_i^{d_\kappa-1}h):
h\in\operatorname{Dom}S_i^{d_\kappa},\
P_{i,\kappa}[\mathbb B](S_i)h=0\}.
$$
$S_i$ 闭、最高关系首一，使 $\Gamma$ 闭，并使核向量逐次再入更深自然幂域。对角 $S_i$ 的完整部分 $J$ 是有界相伴矩阵。

所有系数属于 $\mathfrak D_Q$，与 $\mathbb B$ 及对角 $\mathfrak C$ 交换并保持自然域。所以 $\Gamma$ 同时被全部对角 $\mathfrak C$ 和 $\mathbb B$ 保持。又由
$$
P_{i,\kappa}(t,s)=(s-\kappa)^{d_\kappa}I+tV(t,s)
$$
得
$$
(J-\kappa I)^{d_\kappa}
=-B_\Gamma V[B_\Gamma](J).
$$
右侧拟幂零，故 $\sigma(J)=\{\kappa\}$，$J$ 为单位。由于 $p_i>Q$，引理4.1排除这个非零图。因此每个非零簇分量为零。

若 $E_i=0$，(6.5) 已给 $g=0$，直接矛盾。若 $E_i>0$，零簇分量严格等于原 $g$，并且
$$
R_i[\mathbb B](S_i)g=0.
\tag{6.6}
$$
因此每一层剩下的仍是同一个 (6.1) 原深域向量；词深度不随层数累积损失。

为从这层转到下一参数，令
$$
A_i(t,s)=U_i(t,t^{q_i}s)
\prod_{\kappa\ne0}P_{i,\kappa}(t,t^{q_i}s).
$$
其 $t=0$ 值是与 $s$ 无关的非零标量单位。由 (5.4)，
$$
A_i(t,s)R_i(t,t^{q_i}s)
=t^{q_iE_i}\widehat P_{i+1}(t,s).
$$
有限 Taylor 系数逐项比较强迫
$R_i(t,t^{q_i}s)$ 的全部低于 $q_iE_i$ 的 $t$ 次数消失。故
$$
Q_{i+1}(t,s)=t^{-q_iE_i}R_i(t,t^{q_i}s),\qquad
U_{i+1}(t,s)=A_i(t,s)
\tag{6.7}
$$
仍有解析系数，$Q_{i+1}$ 首一、次数 $E_i=D_{i+1}$，并满足 (6.3)。

在实际深域上 $S_i=\mathbb B^{q_i}S_{i+1}$，所以
$$
0=R_i[\mathbb B](S_i)g
=\mathbb B^{q_iE_i}Q_{i+1}[\mathbb B](S_{i+1})g.
$$
只取消已知单射的有界 $\mathbb B$ 幂，得到下一层的真实核等式。

这里的局部 $A_i^{-1}$ 仅用于证明 Taylor 整除；没有在未知图上对
$U_i[\mathbb B](S_i)$ 求逆，也没有使用无界解析因子。

## 7. 在权一终点应用实际唯一中心谱

经过有限多个严格超线性层，若尚未矛盾，则同一非零 $g$ 满足
$$
Q_{s+1}[\mathbb B](S_{s+1})g=0.
$$
此时 $p_{s+1}=Q$，所以准确地
$$
\boxed{
S_{s+1}=(\Delta_QY)\mathbb B^Q
=\Delta_Q(YL)
}
\tag{7.1}
$$
作为完整自然闭算子相等，域也是同一个有限直和域。

由 (5.2)、(6.3)，
$$
Q_{s+1}(t,s)
=c_{s+1}^{-1}H_F(s)^rI+tV(t,s).
\tag{7.2}
$$
若其 $s$ 次数为零，首一性直接给 $Q_{s+1}=1$，与 $g\ne0$ 矛盾。否则取该自然首一核的非零闭相伴图 $\Gamma$。

如 §6，$\Gamma$ 被全部对角 $\mathfrak C$ 与 $\mathbb B$ 保持，完整部分
$$
J=\Delta(YL)|_\Gamma
$$
有界。由 (7.2)，
$$
c_{s+1}^{-1}H_F(J)^r=-B_\Gamma V[B_\Gamma](J),
$$
右侧拟幂零，谱映射给
$$
\boxed{\sigma(J)\subseteq H_F^{-1}(0).}
\tag{7.3}
$$
这是一个有限非空谱集。

现在应用原中心谱稿定理1：对同一原 $Z,Y,F_n,\sigma_n,\tau_n$，任何非零有限谱完整 $YL$ 部分都迫
$$
\beta_n\to\beta,\qquad \sigma(J)=\{\beta\}.
$$
(7.3) 同时给 $H_F(\beta)=0$。

这证明原规范核非零必满足 (1.3)。原 $C$ 自伴性和原指数的循环图核心将规范核消失准确传成原点态向量循环，完成定理1。

本过程只经过有限多个 $\tau>1$ 层，再一次使用真实 $\tau=1$ 的整个有限谱图。它不需要进入斜率小于1的 Puiseux 层：这些可能的低斜率分支已经包含在终点的零根簇中，而中心谱论证同样适用于谱值零。

## 8. 全部原 weighted 行的具体范围

原中心谱稿 §§5—6 已支付以下完整原行的 (1.1)：
$$
u=u_*+\sum_j(a_j+d_j^0+e_j^0)\chi_j,\qquad
v=v_*+\sum_j(c_j+\gamma a_j+d_j^1+e_j^1)\chi_j,
$$
其中
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\quad
|c_j|\le C_0a_j,\quad
\sum_{a_j>0}|d_j^\nu|^2/a_j<\infty,\quad
d_j^\nu=0\ (a_j=0),\quad e^\nu\in\ell^1(\mathbb C).
$$
对 $a$ 的下降重排 $r_j=a_{\iota(j)}$，置
$$
S_n=\sum_{j\le n}r_j,\qquad G_n^2=\sum_{j>n}r_j^2.
$$
沿任何
$$
nG_n^2/S_n^2\to0
$$
的递增子列，取最大 $n$ 个 $a,|e^0|,|e^1|$ 位与前 $n$ 物理位之并。
原全部 weighted 和可和尾已由该稿逐项支付，且原中心比准确为
$$
\beta_n=\gamma+b_n+o(1),\qquad
b_n=\frac{\sum_{j\le n}c_{\iota(j)}}{S_n}.
$$

所以这里对任意非恒定 $F\in\mathbb C[x,y]$：

- 若 $b_n$ 在该全柱好子列不收敛，则全部 $[F(u,v)-\lambda]^r e^w$ 循环。
- 若 $b$ 为其中任意聚点，且 $F_d(1,\gamma+b)\ne0$，也有该 $F$ 的全部循环结论。
- 真正的非循环候选只可能使该平均收敛，并使其极限落在原普通最高齐次符号的对应零点。

其中 $c$ 可任意复，不需要固定复直线骨架。本稿仍明确需要这条全柱子列预算；没有把正行的另一支好时间条件免费当作一般复辅助预算。

如果某个原核实际存在，上面终点构造的同一个非零 $\Gamma$ 与具体列集无关。因此对任何另一组满足 (1.1) 的原列集，再应用中心谱稿都得到同一个单点 $\sigma(J)$。两组合法列集若迫不同中心极限，也足以排除该原核，无需把两个不可比的位集序列强行说成一个递增序列。

## 9. 例子、扣除及准确剩余项

以原中心谱稿的调和块例为例：
$a_j=1/(j+1)$，在依次支配此前总调和质量的块上交替取
$c_j=a_j$、$c_j=-a_j$，首个未覆盖位取 $c_0=0$。
全柱预算成立，块末平均分别趋于 $+1,-1$。定理1现在给
$$
\boxed{
[F(u,v)-\lambda]^r e^w\text{ 循环}
\quad\text{对每个非恒定 }F\in\mathbb C[x,y]
\text{ 及全部 }\lambda,r,w.
}
$$
不再限于原中心谱稿的等权首一类。

例如允许非首一的
$$
F(x,y)=x\,y^2-y+x^2,
$$
以及最高符号同时含多个线性根的
$$
F(x,y)=(y^2-x^2)^m+x^{2m-1},\qquad m\ge2.
$$
这些只是同一全多项式结论的具体输入，不另计独立结论。

旧单 first、固定超线性 Newton、等权首一、快速模和其他已付共同子类按各原来源扣除。本稿新增的是：一般原空谱 first 的显式有限放大块根、其真实柱单位部分排除，以及全部原二元多项式的唯一线性中心必要条件。

若唯一合法中心极限恰使 $F_d(1,\beta)=0$，结论仍保留这个候选；例如 $v=u+\chi_0$ 时 $(v-u)^2-1=0$，不能排除所有这样的持久线性分支。没有全柱预算的一般复辅助、真实正常见证的专属聚合源上界及普通复 Hilbert ISP 继续开放。
