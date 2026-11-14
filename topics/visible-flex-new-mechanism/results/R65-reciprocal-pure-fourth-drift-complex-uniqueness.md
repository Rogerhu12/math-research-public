# R65：理想互反两常态的纯第四漂移与复 profile 障碍

日期：2026-11-14。状态：已完成的准确条件结论。root 全文核对右锚、纯谐波归约及复 Volterra/Gronwall 证明；repo_sources 独立核对两态 normal 差、纯通道 jet 恒等式及平方分解。使用纸面推导与小型符号身份核对，没有求值真实 profile 积分、研究几何或运行完整第四目标。

本稿处理 R62 的**理想、无连接桥** $k=+1,-1$ 两常态。它回答的是二、三历史准确返回后，余下纯第四漂移能否也恒零。结论不能用于删除真实桥，更没有排除带真实连接、有限 N 修正或其他状态的整个闭几何。

## 1. 归一坐标、唯一右锚与纯通道

保持 R62 的同一 $h>0,d=h\omega-k$，令 $x=h\xi+d$。本稿固定紧区间

$$I=[l,r]\Subset(1,\infty).$$

因此两状态的 $u_k=h^2/(x+k)$ 都为正且没有分母零点。把原 profile 写成 $q(x)=\phi((x-d)/h)$ 后，$Y,r,\eta_*,G_*$ 各为 $h^2$ 倍的 $h=1,d=0$ 对应量，而 $\mathscr R_k$ 与 $\mathcal J_k$ 不变。因此只须在 $h=1,d=0$ 推导，再作同一仿射拉回；不能把两个状态的 $u$ 强设为相同。

以下 $q$ 可为复值，所有点积和平方先按**普通双线性**定义。令

$$Q=1+x^2,\qquad L=x^2-1,\qquad
V_q=\left(-\frac{q'}2,\ q-\frac{xq'}2\right),$$

$$A(a,b)(x)=\frac12\int_x^r V_a'(\eta)\cdot V_b'(\eta)\,d\eta,
\qquad A_q=A(q,q).\tag{1}$$

这是从同一个右 collar 取的真实尾积分，不含自由积分常数。对 $q\in C^2(I;\mathbb C)$，(1) 已有意义且

$$A_q'=-\frac12V_q'\cdot V_q'.\tag{2}$$

对光滑且右 collar 为零的 $q$，取 R62 中目标 profile 为零、第一 profile 为 $q$，定义纯第四漂移

$$\mathcal P[q](x)=\mathcal J_{+1}(0,q)(x)+\mathcal J_{-1}(0,q)(x).\tag{3}$$

这里两个 $\mathcal J$ 均在自己的真实 $u_k=1/(x+k)$ 上恢复，最后才在共同 $x$ 上相加。

## 2. 完整纯漂移的两个二次因子

定义

$$\begin{aligned}
P_1[q]={}&16xA_q+4\left(q-\frac{xq'}2\right)^2
+(xq'-Lq'')^2+2L(q'')^2,\tag{4}
\end{aligned}$$

以及

$$P_2[q]=16A_q+
\begin{pmatrix}q&q'&q''\end{pmatrix}
\mathsf M(x)
\begin{pmatrix}q\\q'\\q''\end{pmatrix},\tag{5}$$

其中

$$\mathsf M(x)=
\begin{pmatrix}
4x&-2(2x^2-1)&2xL\\
-2(2x^2-1)&2x(2x^2-1)&-L(2x^2+1)\\
2xL&-L(2x^2+1)&xLQ
\end{pmatrix}.$$

**准确恒等式为**

$$\boxed{\left(\frac{\mathcal P[q]}{L}\right)'
=\frac{P_1[q]P_2[q]}{64L^2}.}\tag{6}$$

右 collar 中所有 profile jet 和尾积分为零，故该原函数没有剩余常数：

$$\boxed{\mathcal P[q](x)
=-\frac{L(x)}{64}\int_x^r
\frac{P_1[q](\eta)P_2[q](\eta)}{L(\eta)^2}\,d\eta.}\tag{7}$$

式 (7) 只需 $q\in C^2(I;\mathbb C)$ 即定义连续函数。对光滑右零 profile，它准确等于 R62 的完整 pure drift；下文的低正则唯一性直接针对 (7)，不冒称未经定义的低正则第三/第四向量场。

### 2.1 从完整 diagonal 恢复核对 (6)

以下给出可直接复核的消元中间式，保留混合尾直到它真正消掉。设

$$m=V_q\cdot V_q,\quad n=-qq'+\frac x2(q')^2,
\quad b=-\left\{LA_q+\frac{xm+n}{2}\right\}.$$

由 R62 的 $\mathcal B$ 分解，纯通道正是 $d_k=kb$。记 $p=x+k$，则

$$r_k=-A_q-\frac m{2p},\quad t_k=\frac q p-\frac{q'}2,
\quad Y_{d_k}=\frac{kV_b}{p},\quad
r_k(q,d_k)=k\left\{A(q,b)+\frac{V_q\cdot V_b}{2p}\right\}.\tag{8}$$

真实物理微分是 $\partial_u=-p^2\partial_x$。因此逐态取

$$\eta_k=-\frac12t_k(r_k)_u+\frac12r_k(t_k)_u
+\frac12Y_{d_k}\cdot(Y_q)_u-r_k(q,d_k),$$

$$ (Y_q)_u=V_q-pV_q',\qquad
(G_k)_u=(\eta_k-p\eta_k')(1,x)-p\eta_k(0,1),\tag{9}$$

$$D_{ss,k}=-|r_k(k,1)+Y_{d_k}|^2
-2t_k\{2r_k(q,d_k)+\eta_k\},$$

$$D_{uu,k}=-(r_k)_u^2-2(Y_q)_u\cdot(G_k)_u.\tag{10}$$

在复值延拓中，(10) 的 $|\ |^2$ 仅是两分量平方之和的简写，不能改成 Hermitian 模平方。用 $K_{0,k}=kL$ 得

$$\frac{\mathcal P}{L}
=\frac{(x+1)^2D_{ss,+}+(x-1)^2D_{ss,-}}{2L}
+\rho_+-\rho_-,\qquad
\rho_k'=-\frac{D_{uu,k}}{2(x+k)^2}.\tag{11}$$

为缩短展开，置 $A_r=-A_q,m_r=-m,C=A(q,b)$，并定义

$$\begin{aligned}
E_0&=\frac{A_rq}{2}+\frac{qm_r'}4-\frac{m_rq'}8,\\
E_1&=\frac{qA_r'}2-\frac{A_rq'}2-\frac{q'm_r'}8+\frac{m_rq''}8,\\
E_2&=\frac{A_rq''-q'A_r'}4,\\
E&=E_0+xE_1+QE_2,\\
O&=E_1+2xE_2-C-\frac12V_b\cdot V_q'.
\end{aligned}\tag{12}$$

式 (9) 准确给 $\eta_k=E+kO$，没有丢弃 $Y_{W_s}$ 或 $\rho_{3,s}$。另令

$$\begin{aligned}
U&=-\left(QA_r'+\frac x2m_r'-\frac12m_r\right),
&V&=-\left(2xA_r'+\frac12m_r'\right),\\
s_0&=xA_r+\frac{m_r}{2},
&q_0&=xq-\frac Q2q',\\
q_1&=q-xq',
&z_0&=-q_1-\frac L2q''.
\end{aligned}$$

于是 $(r_k)_u=U+kV$。两态直接 ss 贡献之和是

$$\begin{aligned}
D_0={}&-2\left\{s_0^2+A_r^2+s_0(V_b)_T
+A_r(V_b)_B+\frac12V_b\cdot V_b\right\}\\
&-4q_1C+q'(V_q\cdot V_b)-2(q_0E+q_1O).
\end{aligned}\tag{13}$$

其中 $D_0=((x+1)^2D_{ss,+}+(x-1)^2D_{ss,-})/2$。真实 normal 差的导数为

$$\begin{aligned}
(\rho_+-\rho_-)'={}&
-\frac{2(xU-V)(U-xV)}{L^2}
+\frac{2z_0(QE-2xO)}{L^2}\\
&+\frac{2q_0E'+2(Qz_0+q_1)O'}{L}.\tag{14}
\end{aligned}$$

第一项来自两个不同 $du_k$ 权重下的 $-(r_k)_u^2$，并不是把两个负平方按同一测度直接相加。余下三项完整来自 (9) 的 $G_k$。

将 (13)、(14) 代入 $(D_0/L)'+(\rho_+-\rho_-)'$，只用

$$A_q'=-\frac12V_q'\cdot V_q',\qquad
C'=-\frac12V_q'\cdot V_b'$$

以及 $b$ 的显示式展开，所有 $C$、$q'''$ 和更高 jet 都消掉，余式恰为 (4)、(5) 的乘积除以 $64L^2$。这同时说明 (6) 没有借用低阶矩为零或抹掉某个左尾。

独立小证书 [小型准确代数证书](../scripts/literature_reciprocal_pure_drift_certificate.py) 从 (8)–(11) 的原始向量式建立 formal jet 微分，准确检查该因子式；它不使用 (12)–(14) 作为待证式的替代输入。source 另从 (13)、(14) 路径核对同一恒等式，给出两个独立的消元入口。

## 3. 实 profile 的符号

对实 $q$，有 $A_q\geq0$，(4) 在 $x>1$ 是非负平方和。令 $H=2x^2-1$，(5) 还有准确分解

$$\begin{aligned}
P_2[q]={}&16A_q
+4x\left(q-\frac{Hq'}{2x}+\frac{Lq''}{2}\right)^2\\
&+\frac Hx\left(q'-\frac{2xLq''}{H}\right)^2
+\frac{2xL}{H}(q'')^2.\tag{15}
\end{aligned}$$

矩阵 $\mathsf M$ 的顺序主子式为

$$4x,\qquad4(2x^2-1),\qquad8x(x^2-1),$$

在 $I$ 上均严格正。非零紧支撑实 profile 存在 $V_q'\ne0$ 的子区间；在该子区间的左方 $A_q>0$，于是 $P_1P_2>0$。由 (7)，$\mathcal P[q]$ 在相应左侧严格负，特别在整个支撑左侧 collar 严格负；它在右 collar 仍为零。

这证明实 pure drift 一般不相消。不过取零目标和非零实第一 profile 本身没有支付第二 ruling，所以此符号事实单独不是一个完整闭带弯曲的反证。

## 4. 复 profile 的零集唯一性，不使用复正性

**定理。** 设 $I=[l,r]\Subset(1,\infty)$，$q\in C^2(I;\mathbb C)$，$q(r)=q'(r)=0$，$A_q$ 按 (1) 唯一右锚定义。若

$$P_1[q](x)P_2[q](x)=0\qquad(x\in I),\tag{16}$$

则 $q\equiv0$。因此对光滑右 collar 为零的 profile，$\mathcal P[q]\equiv0$ 当且仅当 $q\equiv0$。

**证明。** 在 $P_1$、$P_2$ 中，$(q'')^2$ 的系数分别是

$$LQ,\qquad xLQ.$$

它们在整个紧区间 $I$ 上有统一正下界。其他含 $q''$ 的项至多为一个有界系数乘 $qq''$ 或 $q'q''$，其余项由 $q^2,qq',(q')^2,A_q$ 组成。

对任一个等式 $P_j[q]=0$，使用普通复乘法的准确事实

$$|(q'')^2|=|q''|^2$$

和 Young 不等式吸收混合项，可选同一个只依赖 $I$ 的常数 $C_I$，使

$$|q''(x)|^2\leq C_I\{|q(x)|^2+|q'(x)|^2+|A_q(x)|\}.\tag{17}$$

条件 (16) 只要求每一点至少一个因子为零；两个因子都给同一 (17)，所以不需要选择一个连续分支，也不需要证明切换点有限。

令 $t=r-x$，$T=r-l$，并置

$$E(t)=\int_{r-t}^r|q''(\eta)|^2\,d\eta,\qquad0\leq t\leq T.$$

由右端两个零值及 Cauchy–Schwarz，

$$|q'(r-t)|^2\leq tE(t),\qquad
|q(r-t)|^2\leq\frac{t^3}{3}E(t).\tag{18}$$

虽然 $A_q$ 不必实或非负，(1) 仍给

$$|A_q(r-t)|\leq C_I\int_{r-t}^r
\{|q''|^2+|q'|^2\}\,d\eta
\leq C_I(1+t^2/2)E(t).\tag{19}$$

这里用了 $E$ 单调以及对每个较短尾的 (18)。将 (18)、(19) 代入 (17)，在整个 $[0,T]$ 上得到

$$E'(t)\leq C_I' E(t),\qquad E(0)=0.$$

Gronwall 不等式给 $E\equiv0$，再由两个端值推出 $q\equiv0$。证明没有把普通复平方当成正模平方。证毕。

## 5. 对理想两态完整相位的含义

固定任意与相位无关的目标 profile $f$，令 $a,b$ 是同一 $I$ 内实光滑紧支撑 profile，取第一 profile 圆

$$\phi_\theta=a\cos\theta+b\sin\theta,
\qquad q=a+ib,\qquad \zeta=e^{-i\theta}.$$

于是 $\phi_\theta=(\zeta q+\zeta^{-1}\overline q)/2$。R62 的 $\mathcal J_k(f,\phi)$ 由目标四次、目标二次乘 $\phi$ 二次以及 $\phi$ 纯四次组成。因此它的 $\zeta^4$ 系数准确为

$$[\zeta^4]\{\mathcal J_+(f,\phi_\theta)+\mathcal J_-(f,\phi_\theta)\}
=\frac1{16}\mathcal P[q].\tag{20}$$

这也与完整第四编译中的纯通道 $-H(B,B)/16-H(A,U)/4$ 一致：零目标、第一场为 $Y_q$ 时，第二场是 $-B$、第三场是 $2U$，第四强迫为 $-H(B,B)-4H(A,U)$。

在 R62 的理想无桥模型中，两常态等长 $T_0$，相反三角历史向量场对任意共同右零入值准确互逆。完整第四净漂移的 $\zeta^4$ 模式于是为 $T_0\mathcal P[q]/16$。第 4 节说明，只要 $q\ne0$，该函数就不能恒零。

所以，同一物理正侧区间中，**一个理想无桥 $\pm1$ 对不能仅靠改变非零复 profile 或消掉二、三历史而支付整个第四周期函数**。这包括有真实重叠的 profile 平面；结论不依赖把它旋转成不交支撑。允许共同入值中的合法全局历史 gauge 也不改变 R62 的局部漂移，但在两态接缝另行重锚不属于这个模型。

## 6. 与 R49 及真实连接的界限

R49 处理常段第四 **ruling** 的最高 $s^2$ 系数；本稿处理理想逆流已经取消那些历史后仍留下的第四 **period** 的纯谐波局部漂移。它们属于两个不同的完整 range 条件，不能用本稿的符号替代 R49 的系数，也不能因为历史的最高次数相消就删除 (7)。

本稿尤其没有证明整个 R45 真正闭几何的纯第四周期非零。真实桥改变 $k,h,\omega$，接收并传播第二、第三历史，也贡献自己的第四函数；其高阶作用不由二阶矩阵成本 O(1) 控制。有限 N 零算子修正还会使 bulk 离开准确 $k=\pm1$。这些贡献有可能补偿 (7)，必须在共同锚下实算或准确设计。

本次完整第四实际输出中 −4 模式随两档加密大幅变化，不能由本稿断言其准确全几何值，也不能倒过来从该数值现象猜定 (7) 为零。本稿给出的是一个可复核的具体漂移算子和范围清楚的无桥模型障碍。下一控制设计必须把真实连接当成可能承担必要第四补偿的组成部分，不能再把互反 bulk 当成全阶逆片。
