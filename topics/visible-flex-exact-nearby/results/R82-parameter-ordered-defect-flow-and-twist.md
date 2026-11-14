# R82：小缺陷流的参数有序展开、完整二阶余项与真实横截

2026-11-12，visible-exact-astra-f6a2。

**状态：以下定量命题及有限积分接口已证明；实际全前腿的有符号参数源尚须支付。**
本篇将 R68/R72 的小缺陷坐标直接用于同一个真实参数族的一、二阶变分。
粗模数支付高阶余项，保留符号的有限积分支付平均横截。两者不能互相代替。
本篇不宣布当前 δ₅ 返回已通过 R31，也不将圆周结论转授给完整等距 PDE。

## 1. 固定参考、真实参数与角坐标

固定同一个准确参考 $Y_j(u,x)$，$u\in[-1,1]$，$x\pmod{2\pi}$。
$Y$ 是物理角，满足 $Y(u,x+2\pi)=Y(u,x)+\pi/2$；标签 $x$ 是归一化角。
参数 $p$ 改变真实几何和真实特征场，**不改变**本篇的 $Y$、$q=Y_x$、
有限 $H$ 或局部物理时间 $\tau=\tau_{c,j}+h_j u$。
特别地，准确转折时刻仍是 $\tau=\pm\pi/2$，不能改成它们的 binary64 近似。
在全部真实参数区间 $I$，真实固定 $\tau$ 场记为 $f(\tau,\theta,p)$。
移动几何根 $r=t(p)\sin\tau$ 的全部链式项已经包含在 $f_p,f_{pp}$ 中。

假设 $q$ 在整条实时参考及整个标签带 $\mathcal S_S=\{|\Im x|<S\}$ 上非零。
每段定义

\[
 g_0=\frac{h_j f(\tau,Y,p)-Y_u}{q},\qquad
 g_1=\frac{h_j f_p(\tau,Y,p)}q,\qquad
 g_2=\frac{h_j f_{pp}(\tau,Y,p)}q.                 \tag{82.1}
\]

这些是准确的 $g_1=\partial_p g_0$、$g_2=\partial_p^2g_0$，没有额外因子 $4$。
因子 $4$ 只在最后输出归一化返回时出现。若某腿的 $h_j<0$，保留该符号，
局部积分仍从 $u=-1$ 到 $1$。按各段顺序连接的局部时间以下统一记为 $v$。

所有接缝必须是准确函数恒等式 $Y_{j+1}(-1,x)=Y_j(1,x)$，因而 $q$ 也准确匹配。
$Y_u$ 和 $g_i$ 可以有有限跳跃；小缺陷坐标 $X$ 连续通过接缝，不能重新置为 $x$。
若首端 $Y(a,x)=H(x)/4$，则

\[
 X_v=g_0(v,X,p),\quad X(a,x,p)=x,\qquad
 \Gamma_p(x)=4Y(b,X(b,x,p))=P_p(H(x)),              \tag{82.2}
\]

其中 $P_p$ 是准确归一化物理前腿提升。真实后腿等于前腿的结论只能在
[R77](R77-reflection-square-of-principal-return.md) 的显式对称对象上使用。

若已经支付整个实时带 $|q|\le Q$、$Y(v,\mathbb R)\subset\mathbb R$，则
$|\Im Y(v,x)|\le Q S$。所以将 R80 的物理角源带 $|\Im\theta|<S_\theta$
接入 (82.1) 的明确条件是 $Q S<S_\theta$，不是把两种角带宽写成同一个数。
所有 $f_p,f_{pp}$ 必须对应同一准确仿射几何族、同一根分支及同一参数区间。

## 2. 有符号近似源及完整输入误差

假设 $g_0(v,\cdot,p)$ 在 $\mathcal S_S$ 全纯、$2\pi$ 周期，关于 $v$ 分段连续，
关于真实 $p$ 为取值于该解析函数空间的 $C^2$ 族。
在整个 $I$ 给出可积非负函数 $M_i(v)$，并给选定的有限近似源 $\widehat g_i$，使

\[
 |g_i(v,x,p)|,\ |\widehat g_i(v,x)|\le M_i(v),\qquad
 |g_i(v,x,p_0)-\widehat g_i(v,x)|\le\eta_i(v),\quad i=0,1,2,
 \tag{82.3}
\]

在整个声明的复带上成立。近似源可以只在 $p_0$ 处计算，亦可逐参数提供同样的合同。
不要求所选 $\widehat g_1,\widehat g_2$ 在形式上等于 $\widehat g_0$ 的参数导数；
要求它们分别逼近 (82.1) 中真正的一、二阶源。
定义累计量

\[
 A(v)=\int_a^vM_0,\quad B_i(v)=\int_a^vM_i\ (i=1,2),\quad
 E_i(v)=\int_a^v\eta_i,\qquad A=A(b),\ B_i=B_i(b),\ E_i=E_i(b).
 \tag{82.4}
\]

全部无限 primitive、有限场重构、时间与标签截尾、节点球、样条换片 cap、
有限复合及算术误差都必须进入 $\eta_i$。只有实时间点值的误差不能代付 (82.3)。
若先有 $|\widehat g_i|\le\widehat M_i$，可取 $M_i=\widehat M_i+\eta_i$。
保留有限源的系数符号，不能仅保存 $M_1,M_2$ 后宣称平均横截非零。

选择 $0\le\sigma<S$，置

\[
 R=S-\sigma,\qquad 0<A<R/2,\qquad d=R-A.            \tag{82.5}
\]

$A=0$ 时可使用任意更大的正上界再取极限。以下公式在每个前缀也成立，
把总量换成其前缀值即可。

## 3. 准确有序积分及参数展开

令 $G_i(v,x)=\int_a^v g_i(w,x,p_0)\,dw$。定义

\[
\begin{aligned}
 V_0&=G_0+\int_a^b g_{0x}G_0\,dv,\\
 V_1&=G_1+\int_a^b(g_{1x}G_0+g_{0x}G_1)\,dv,\\
 V_2&=G_2+\int_a^b(g_{2x}G_0+2g_{1x}G_1+g_{0x}G_2)\,dv.
\end{aligned}                                                     \tag{82.6}
\]

右侧 $G_i$ 在积分内部取同一时刻 $v$，在积分外取 $b$。
由时间和参数微分交换，$V_1=\partial_p V_0$、$V_2=\partial_p^2V_0$。
用三个 $\widehat g_i$ 同样定义 $\widehat V_i$，不需要近似源之间有参数一致性。

令 $Z=\partial_pX$、$W=\partial_p^2X$。准确变分方程为

\[
 Z_v=g_{0x}(v,X)Z+g_1(v,X),\qquad
 W_v=g_{0x}(v,X)W+g_{0xx}(v,X)Z^2+2g_{1x}(v,X)Z+g_2(v,X),
 \tag{82.7}
\]

首值均为零。全部参数源都在同一个真实轨迹 $X$ 处取值。

### 3.1 零阶流余项

R68 给 $|X(v,x)-x|\le A(v)$。在轨迹与起点之间的线段上可用
$|g_{0x}|\le M_0/d$、$|g_{0xx}|\le2M_0/d^2$，而起点处
$|g_{0x}(v,x)|\le M_0/R$。
先积分得 $|X-x-G_0|\le A(v)^2/(2d)$，再作含积分余项的二阶 Taylor，
得到 R72 的完整界

\[
 |X(b,x)-x-V_0(x)|\le T_0:=\frac{A^3}{2d^2}.        \tag{82.8}
\]

### 3.2 用辅助复缩放支付一、二阶参数尾

只在证明中把真实小场改成 $\lambda g_0$，不把 $\lambda$ 视为几何参数。
置 $L=R/(2A)>1$。对 $|\lambda|\le L$，真实缩放流始终满足
$|X_\lambda-x|\le LA=R/2$，因此仍离原带边界至少 $d_L=R/2$。
流关于 $\lambda$ 全纯；关于 $p$ 的一、二阶微分由统一变分方程继承，
不要求存在任何复 $p$ 域。

写 $\alpha=|\lambda|$、$a(v)=A(v)$、$b_1(v)=B_1(v)$。
积分因子给

\[
 |Z_\lambda(v)|\le \alpha e^{\alpha a(v)/d_L}b_1(v).
 \tag{82.9}
\]

二阶方程的三个强迫项分别给

\[
\begin{aligned}
 |W_\lambda(b)|\le{}&\alpha e^{\alpha A/d_L}B_2
 +\frac{2\alpha^2e^{\alpha A/d_L}}{d_L}\int_a^bM_1(v)b_1(v)\,dv\\
 &+\frac{2\alpha^3e^{\alpha A/d_L}}{d_L^2}
       \int_a^bM_0(v)e^{\alpha a(v)/d_L}b_1(v)^2\,dv\\
 \le{}&\alpha e^{\alpha A/d_L}B_2+
 \frac{\alpha^2e^{\alpha A/d_L}(2e^{\alpha A/d_L}-1)}{d_L}B_1^2.
\end{aligned}                                                     \tag{82.10}
\]

这里第一项内的指数取上界；第二项用 $\int M_1b_1=B_1^2/2$；
第三项用 $b_1(v)\le B_1$ 与
$\int M_0e^{\alpha a/d_L}=d_L(e^{\alpha A/d_L}-1)/\alpha$。
因此在 $|\lambda|=L$，

\[
 |Z_\lambda|\le eLB_1,\qquad
 |W_\lambda|\le eLB_2+\frac{2e(2e-1)L^2}{R}B_1^2.  \tag{82.11}
\]

$X_\lambda-x$ 的 $\lambda$ 和 $\lambda^2$ 系数分别是
$G_0$ 与 (82.6) 的二次有序积分。微分后，$Z_\lambda$ 的前两项之和为
$V_1$，$W_\lambda$ 的前两项之和为 $V_2$。
对 $\lambda$ 使用 Cauchy 系数界，准确求和所有 $n\ge3$，得到

\[
 \boxed{|Z(b,x)-V_1(x)|\le
 T_1:=\frac{4e A^2B_1}{R^2(1-2A/R)}},              \tag{82.12}
\]

\[
 \boxed{|W(b,x)-V_2(x)|\le
 T_2:=\frac{4e A^2B_2+4e(2e-1)AB_1^2}{R^2(1-2A/R)}}.
 \tag{82.13}
\]

这支付真实非线性流的全部高阶时间有序项，包含二阶参数导数中的交叉项。
没有把形式展开截断当作真实解，也没有重新引入原始大场的变分指数。

### 3.3 近似源误差

在起点标签处，空间 Cauchy 给
$|g_{ix}-\widehat g_{ix}|\le\eta_i/R$。
准确展开 (82.6) 的积分之差，再使用
$\int(\eta_i A+M_0E_i)=AE_i$ 和
$\int(\eta_0B_i+M_iE_0)=B_iE_0$，得到

\[
\begin{aligned}
 |V_0-\widehat V_0|&\le E_0(1+A/R),\\
 |V_1-\widehat V_1|&\le E_1+(AE_1+B_1E_0)/R,\\
 |V_2-\widehat V_2|&\le E_2+(AE_2+2B_1E_1+B_2E_0)/R.
\end{aligned}                                                     \tag{82.14}
\]

第二阶中间项 $2g_{1x}G_1$ 的费用是 $2B_1E_1/R$，不能丢掉。
若实际保存的有限 $\widetilde V_i$ 相对准确 $\widehat V_i$ 另有完整连续带误差
$\varepsilon_i^{\rm int}$，定义

\[
\begin{aligned}
 b_0&=T_0+E_0(1+A/R)+\varepsilon_0^{\rm int},\\
 b_1&=T_1+E_1+(AE_1+B_1E_0)/R+\varepsilon_1^{\rm int},\\
 b_2&=T_2+E_2+(AE_2+2B_1E_1+B_2E_0)/R+\varepsilon_2^{\rm int}.
\end{aligned}                                                     \tag{82.15}
\]

则 $X-x-\widetilde V_0,Z-\widetilde V_1,W-\widetilde V_2$ 在整个
$\mathcal S_\sigma$ 分别有模上界 $b_0,b_1,b_2$。

## 4. 可直接实现的有限积分与跨段接口

每个叶段保存三个完整有限多项式
$\widehat g_i(u,x)=\sum_{n,k}c_{i,n,k}u^ne^{ikx}$；其标签频率是整数 $k$，
不是物理角频率 $4k$。令该段首积分末值为 $A_i^{(j)}(x)$，局部二阶积分为

\[
 J_0=\mathcal B(\widehat g_0,\widehat g_0),\quad
 J_1=\mathcal B(\widehat g_1,\widehat g_0)+\mathcal B(\widehat g_0,\widehat g_1),
\]
\[
 J_2=\mathcal B(\widehat g_2,\widehat g_0)+2\mathcal B(\widehat g_1,\widehat g_1)
                                  +\mathcal B(\widehat g_0,\widehat g_2),
 \quad \mathcal B(a,b)=\int_{-1}^1a_x(u)\int_{-1}^u b(v)\,dv\,du.
 \tag{82.16}
\]

设 $C_i$ 是之前全部段的首积分，$D_i$ 是之前全部段的对应二次积分。新段准确更新为

\[
\begin{aligned}
 D_0&\leftarrow D_0+(A_0^{(j)})'C_0+J_0,\\
 D_1&\leftarrow D_1+(A_1^{(j)})'C_0+(A_0^{(j)})'C_1+J_1,\\
 D_2&\leftarrow D_2+(A_2^{(j)})'C_0+2(A_1^{(j)})'C_1+(A_0^{(j)})'C_2+J_2,\\
 C_i&\leftarrow C_i+A_i^{(j)}\quad(i=0,1,2).
\end{aligned}                                                     \tag{82.17}
\]

前三行必须使用旧的 $C_i$。最终 $\widehat V_i=C_i+D_i$。
若 $a(u)=\sum_m a_mu^m$、$b(u)=\sum_n b_nu^n$，令
$j_\ell=0$（$\ell$ 奇）或 $2/(\ell+1)$（$\ell$ 偶），则

\[
 \mathcal B(a,b)=\sum_{m,n}w_{mn}a_m'b_n,
 \qquad w_{mn}=\frac{j_{m+n+1}-(-1)^{n+1}j_m}{n+1}. \tag{82.18}
\]

这些权重是准确有理数，已包含奇偶与时间先后关系。有限 Fourier 乘积保留
全部和频；如投影，全部被删项计入 $\varepsilon_i^{\rm int}$。
不能把 $J_i$ 置零，或把仅用于原场的 $A^2/R$ 无条件用于参数混合项。
若只界局部 $J_i$ 而不保系数，可由 (82.18) 的完整有限 Wiener 和支付其费用。
跨段项仍须累计，不能因一个短叶段的首积分很小而重新清零。

**数据接口。** 原生参数场模块输出同一对象的 $f_p,f_{pp}$ 及其无限尾；
参考模块输出准确 $Y,Y_u,q$；密度模块依 (82.1) 输出有符号的有限三源、
每个源的 $M_i,\eta_i$、完整时间和角带以及对象/参考身份。
积分模块只用 (82.16)–(82.18)，输出有限 $\widetilde V_i$ 和全部额外费用。
实时间参数快照可核对符号和规模，但没有连续时间/全角费用时不能充当这个接口。

## 5. 真实物理端点的一、二阶参数误差

置 $\widetilde X=x+\widetilde V_0$、$\widetilde Z=\widetilde V_1$、
$\widetilde W=\widetilde V_2$。记

\[
 U_*=A+\frac{A^2}{2R}+\varepsilon_0^{\rm int},\qquad
 Q_j\ge\sup_{\mathcal S_{\sigma+U_*}}|\partial_x^j q(b,\cdot)|\quad(j=0,1,2).
 \tag{82.19}
\]

必须实际保证 $\sigma+U_*$ 在参考端点的已付域内。由 R72，$X$、$\widetilde X$
及二者之间的整条线段都在此域内。
不经有序展开也可从 (82.7) 得到方便的粗真实上界

\[
 Z_*:=e^{A/d}B_1,\qquad
 W_*:=e^{A/d}B_2+\frac{e^{A/d}(2e^{A/d}-1)}dB_1^2,
 \tag{82.20}
\]

推导正是 (82.9)–(82.10) 的 $\lambda=1,d_L=d$ 版本。
也可用更小的已证有限值 $|\widetilde Z|+b_1$、$|\widetilde W|+b_2$。
令 $\widetilde Z_*\ge|\widetilde Z|$。准确端点微分为

\[
 \partial_p\Gamma_p=4q(b,X)Z,\qquad
 \partial_p^2\Gamma_p=4\{q_x(b,X)Z^2+q(b,X)W\}.    \tag{82.21}
\]

分别用 $\widetilde X,\widetilde Z,\widetilde W$ 组成对应近似函数。
它们与真实 $\Gamma,\Gamma_p,\Gamma_{pp}$ 的全带误差可取

\[
\begin{aligned}
 e_{\Gamma,0}&=4Q_0b_0,\\
 e_{\Gamma,1}&=4(Q_1b_0Z_*+Q_0b_1),\\
 e_{\Gamma,2}&=4\{Q_2b_0Z_*^2+Q_1b_1(Z_*+\widetilde Z_*)
                              +Q_1b_0W_*+Q_0b_2\}.
\end{aligned}                                                     \tag{82.22}
\]

证明只需分别在 $q,q_x$ 上用线段积分公式，并准确展开两个乘积之差。
若随后把这些近似复合函数改成有限 Fourier 对象，须再加全部连续复合/重构误差，
不能将单个节点误差当成全 Fourier 白噪声后省略放大。

特别地，若准确端点为 $Y(b,x)=x/4+U(x)$，$U$ 是完整有限 Fourier 函数，
写 $w_i=\widetilde V_i$。与零阶端点二次展开一致的三个有限输出是

\[
\begin{aligned}
 P_0&=x+4U+(1+4U')w_0+2U''w_0^2,\\
 P_1&=(1+4U'+4U''w_0)w_1,\\
 P_2&=(1+4U'+4U''w_0)w_2+4U''w_1^2.
\end{aligned}                                                     \tag{82.22a}
\]

这里 $P_i$ 分别近似真实参数的第 $i$ 阶输出，不要求保存的 $w_i$ 形式上是
某个选定有限族 $w_0(p)$ 的参数导数。置
$M_3=\|U'''\|_{\sigma+\|w_0\|_\sigma}$，完整保留所有有限乘积频率后，
相对 (82.21) 的近似复合，它们还须支付

\[
 \frac23M_3\|w_0\|_\sigma^3,\qquad
 2M_3\|w_0\|_\sigma^2\|w_1\|_\sigma,\qquad
 2M_3\|w_0\|_\sigma^2\|w_2\|_\sigma
       +4M_3\|w_0\|_\sigma\|w_1\|_\sigma^2              \tag{82.22b}
\]

的费用。这直接来自 $U$ 的二阶、$U'$ 的一阶和 $U''$ 的零阶 Taylor 积分余项。
它们加在 (82.22) 之后；选取 dyadic 系数造成的 $w_i$ 误差须先计入 $b_i$。

## 6. Wiener 带宽、固定 H 的局部逆与平均横截

取明确的带宽层次

\[
 0<s_0<s_*<s_+<\sigma<S,\qquad \Delta=s_+-s_*.
 \tag{82.23}
\]

在 $\mathcal S_\sigma$ 已付的周期端点误差，经 R63 的完整 Hardy 界变成

\[
 \epsilon_{\Gamma,i}^{A}\le
 e_{\Gamma,i}\sqrt{2\coth(\sigma-s_+)-1}
       +\text{额外有限复合的 }A_{s_+}\text{ 费用}.     \tag{82.24}
\]

常数模和负频率均已包含。平均横截所用的是有符号有限端点参数函数，
其范数与 (82.24) 相加才给真实范数。

令 $d_0$ 是准确选定的半返回目标角，并置
$\mathcal E_p=\Gamma_p-H(x+d_0)$。
在整个真实参数盒上支付 R63 的

\[
 \|(H')^{-1}\|_{s_+}\le\mathcal R_H,\quad
 \|H''\|_{s_++r_H}\le B_H,\quad
 \kappa=\mathcal R_HB_Hr_H\le\tfrac12,\quad
 \mathcal R_H\sup_p\|\mathcal E_p\|_{s_+}\le r_H/2. \tag{82.25}
\]

于是准确 $G_p=H^{-1}P_pH=x+d_0+u_p$ 存在，
$\|u_p\|_{s_+}\le2\mathcal R_H\|\mathcal E_p\|_{s_+}$，并且

\[
 \partial_pG_p=\frac{\partial_p\Gamma_p}{H'(G_p)},\qquad
 \partial_p^2G_p=
 \frac{\partial_p^2\Gamma_p-H''(G_p)(\partial_pG_p)^2}{H'(G_p)}.
 \tag{82.26}
\]

若在 $s_+$ 上真实端点参数范数为 $P_\Gamma,T_\Gamma$，可取

\[
 P_+=\frac{\mathcal R_H}{1-\kappa}P_\Gamma,\qquad
 T_+=\frac{\mathcal R_H}{1-\kappa}(T_\Gamma+B_HP_+^2).
 \tag{82.27}
\]

故供 R31 在映射域宽 $s_*$ 使用的四个统一常数可取

\[
 P=P_+,\qquad Q=\frac{P_+}{e\Delta},\qquad T=T_+,\qquad
 B=\frac{2\sup_p\|u_p\|_{s_+}}{\Delta^2}.          \tag{82.28}
\]

所有导数收缩都明确发生在 $s_+\to s_*$；随后 R31 的初始宽为 $s_0$，
初始共轭为恒等映射，必须继续支付它自己的迭代宽损失和域余量。

### 6.1 有符号有限平均真正支付 twist

在 $p_0$ 处令 $A_1^{\rm fin}$ 为保存的有限端点参数近似，
$\|\partial_p\Gamma-A_1^{\rm fin}\|_{s_+}\le\epsilon_{\Gamma,1}^{A}$。
选有限 $q_H^{\rm fin}$，并支付
$\|1/H'(x+d_0)-q_H^{\rm fin}\|_{s_+}\le\epsilon_H$。
其完整有限乘积的零频系数为

\[
 \tau_{\rm fin}=\langle A_1^{\rm fin}q_H^{\rm fin}\rangle.
 \tag{82.29}
\]

平移 $d_0$ 的指数和有限算术误差须在 $\epsilon_H$ 或另列的
$\epsilon_{\rm av}$ 中包含。R31 在恒等预共轭坐标的真实横截是
$\tau=\langle\partial_pG_{p_0}\rangle$。由 (82.26) 及 Neumann 逆之差，

\[
 \left\|\frac1{H'(G)}-\frac1{H'(x+d_0)}\right\|_{s_+}
 \le\frac{\mathcal R_H^2B_H}{1-\kappa}\|u_{p_0}\|_{s_+}.
 \tag{82.30}
\]

因此完整误差为

\[
 \boxed{|\tau-\tau_{\rm fin}|\le
 \mathcal R_H\epsilon_{\Gamma,1}^{A}
 +\|A_1^{\rm fin}\|_{s_+}\epsilon_H+\epsilon_{\rm av}
 +\frac{\mathcal R_H^2B_H}{1-\kappa}P_\Gamma\|u_{p_0}\|_{s_+}.}
 \tag{82.31}
\]

有限区间 $\tau_{\rm fin}$ 距零的距离减去右侧，若严格为正，才得到 R31 的
$\sigma_0$。不需要参数导数处处同号。直接在原 $H$ 使用 R31 时，其初始横截
是 $\langle\partial_p\Gamma/H'(x+d_0)\rangle$；换成恒等预共轭后才是 $\tau$。
两者之间的 (82.30) 费用不能省略。

### 6.2 一个明确的宽度配置示例

例如可选择

\[
 S=1/512,\quad \sigma=3/2048,\quad s_+=1/1024,
 \quad s_*=3/4096,\quad s_0=1/2048,\quad\delta_0=1/16384.
 \tag{82.32}
\]

于是流余项使用 $R=1/2048$，要求 $A<1/4096$；Hardy 宽差为 $1/2048$；
混合导数宽差为 $1/4096$；R31 的最终宽为 $s_0-4\delta_0=1/4096$。
其初始恒等共轭的域门还要求 $2L_H\varepsilon_0/\delta_0<s_*-s_0=1/4096$。
这只是明确的可选算术配置，没有宣称其误差、横截、$H$ 逆或 R31 小量门已经通过。
如果使用已付的实时参考界 $Q<1.05$，(82.1) 的物理像仅需
$QS<21/10240<1/64$；真实参数源仍须独立拥有该物理角域。

## 7. 真参数盒、半返回与相位平均 β

中心 $p_0$ 的小缺陷总量为 $A_0$，而整个 $|p-p_0|\le\eta$ 上的一阶源总界为 $B_1$。
则由实参数积分

\[
 \sup_{|p-p_0|\le\eta}\int|g_0(v,\cdot,p)|\,dv
 \le A_0+\eta B_1=:A_I.                              \tag{82.33}
\]

用 $A_I$ 检查 (82.5)，即给整个真实参数盒的复带流、(82.20) 和端点参数粗界。
继而可用
$\sup_p\|\mathcal E_p\|_{s_+}\le\|\mathcal E_{p_0}\|_{s_+}+\eta P_\Gamma$
支付 (82.25)。这里 $P_\Gamma$ 先从真实流与固定参考取得，不依赖尚待证明的局部逆，
所以没有循环。中心有符号积分支付 twist，整个盒的粗一、二阶界支付 R31 稳定性。

在 R77 的同一个显式偶/奇族上，真实全返回为 $P_p^2$。
若准确目标全旋转角为 $\alpha=2d_0$，且
$|e^{ik\alpha}-1|\ge1/(K|k|)$，则

\[
 |e^{ikd_0}-1|\ge\tfrac12|e^{ik\alpha}-1|
                   \ge1/(2K|k|).                    \tag{82.34}
\]

故可对真实半返回以常数 $2K$ 使用 R31；所得准确共轭平方后给全目标旋转。
必须先支付真实半返回误差并选定自然提升 $d_0$。不能从全返回近共轭自动推出
半返回近共轭，也不能把 $d_0+\pi$ 的另一平方根静默换入。

最后，R50/R52 中完整算子的相位平均记为 $\mathfrak b(p)=\langle\beta\rangle$，
它不是几何角相位 $\beta(r,p)$，也不是上述圆周 twist。
若另有同一真实参数族的有向证书
$\mathfrak b(p_0)\in[b_-,b_+]$、$|\mathfrak b'(p)|\le L_\beta$ 于整个参数盒，
则选参后仅可转授

\[
 \mathfrak b(p)\in[b_--L_\beta\eta,b_++L_\beta\eta]. \tag{82.35}
\]

所需非零或其它排除集合的余量必须由这个扩张后的区间实际检查。
该 β 证书的径向 collar、真实角解析带、有限部和无限尾仍须由原 β 计算支付；
本篇的标签带收缩不会免费支付或扩大它们。若后续完整算子还需要角函数的
Wiener 范数，应另外声明其物理/归一化角和所用宽度，不能由一个平均数推得。

至此，有限有符号参数源、完整时间有序积分、真实流变分、端点 Wiener 误差、
固定 $H$ 的平均横截及真实参数盒已有明确连接。实际输入仍在计算中；
完整 KAM 门、幅度/低阶传播、帽与外延、全频逆及精确等距族不由本篇代付。

实现接口为 `scripts/fourfold_parameter_ordered_defect.py`：
`parameter_coordinate_budget`、`endpoint_parameter_budget`、
`first_and_local_parameter_bounds`、`advance_parameter_integrals`。
局部二阶项可保完整系数，也可支付准确奇偶分解后的全部有限范数；
跨段项完整保留。`--closed-flow-check` 使用先平移、再作正弦流的闭式解
$\tan(X/2)=e^{2\lambda b}\tan((x+2\lambda a)/2)$，核对非交换二次项及其两阶
参数导数。此有限代数核对不代付任何真实场输入或全前腿计算。
