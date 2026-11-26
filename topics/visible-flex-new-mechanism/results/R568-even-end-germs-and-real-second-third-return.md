# R568：八矩词的真实偶 germs 与同规范第二、第三返回

日期：2026-11-26。承接已证明的 R567；root 已全文读取，
对照 R523/R526 的完整反射式与 R559/R564 的原四末控和费用。
原式纸证，没有执行科学数值或符号计算。

新增命题不是“零速度自动给偶 germ”，而是在原加速度控制中把末开区间
真正改成恒高度，再在同一个八矩共同零上使用原系统的反射唯一性。
这支付 R526 中此前独立悬着的 scalar germ 条件。

## 1. 固定第三规范不破坏原反射

保 R521 的同一母、真右锚、$w=0$ 和一个固定 $\chi_\theta$。
完整状态写成
$$
X=(S,\gamma,\upsilon,A,T),\qquad
S=(h,k,\omega),\quad \gamma=h_s,\quad\upsilon=k_s.
$$
$T$ 是未删去势或原函数的完整第三算子。控制是原 $a=h_{ss}$，
$k_{ss}$ 由完整第四 ruling 与 $C_k>0$ 唯一解出。

R523 §2 已从原 R56/R73 逐项证明
$$
M(S,-\gamma,-\upsilon)=M(S,\gamma,\upsilon),
\qquad \mathcal C^{\rm rev}=-\mathcal C,
$$
其中原 history 方程是
$$
A_s=\Phi_M,
\qquad T_s=-\Phi_M\circ A+\mathcal C_s.
\tag{1}
$$
令
$$
\mathcal I(S,\gamma,\upsilon,A,T)
=(S,-\gamma,-\upsilon,-A,T).
\tag{2}
$$
R523 §3 对零 $\chi$ 写出的 ruling 偶性也适用于任意本次已固定的
$\chi$：原完整公式
$$
q_\theta=AD_\theta,
\qquad b_\theta=-2T(\phi_\theta;D_\theta)-\chi_\theta
$$
在(2)下给 $q\mapsto-q$、$b\mapsto b$。
局部第四项偶，线性 $\mathcal L_s(q)$ 的速度与 $q$ 同时变号，
$q$ 的能量平方偶，$\mathcal E(\phi,b)$ 偶。
固定的 $\chi$ 没有新的速度或时间导数，因此完整 ruling 保持。
原 $C_h,C_k$ 只依赖 scalar，亦保持。
故原 $k_{ss}$ 输出满足
$$
k_{ss}(\mathcal I X,a)=k_{ss}(X,a).
\tag{3}
$$
完整 ODE 于是具有可逆性
$$
F(\mathcal I X,a)=-D\mathcal I\,F(X,a).
\tag{4}
$$
第三方程的号可直接核：反射后的右边是
$-M\circ(-A)-\mathcal C=M\circ A-\mathcal C$，恰为原导数的负值。
这里不要求 $T=0$，也不要求 $T$ 在某个 outer 核内。

## 2. 一个真正可用的偶 germ 判据

设在某端点 $s=s_*$ 有
$$
\gamma(s_*)=\upsilon(s_*)=0,\qquad A(s_*)=0.
\tag{5}
$$
设原高度加速度控制在该点一个开放邻域内为一个偶函数。
特别，$a=0$ 是允许的明确选择。
将真实解按 $s-s_*\mapsto-(s-s_*)$ 和(2)反射，
由(4)得到同一控制、同一完整初值的解；$T(s_*)$ 保原真实值。
原正规 ODE 唯一性给
$$
S(s_*+t)=S(s_*-t),
\quad(\gamma,\upsilon)(s_*+t)=-(\gamma,\upsilon)(s_*-t),
$$
$$
A(s_*+t)=-A(s_*-t),\qquad T(s_*+t)=T(s_*-t).
\tag{6}
$$
因此 $h,k,\omega$ 的全部奇阶 jets 在该端准确为零。
只给 $\gamma=\upsilon=0$ 或仅落在反馈慢支上都不足以使用此判据；
控制本身的偶 germ 与 $A=0$ 是实际假设。

## 3. 用原四末控支付恒高度开段

R567 的末段是 R564 的负耦合长快回路。
取原快时钟 $\tau=(s-s_{\rm in})/\delta$，保
$$
H_->0,\quad C_k(H_-,0)>0,\quad \beta_-\ne0,
\quad \omega_-^2=c/C_k(H_-,0)>0.
$$
在该回路后留一个固定有限快窗，其内四个紧支撑原高度加速度控制
与 R559/R564 相同。修改的只是这个快窗最后的开放控制：
将原耗散反馈加速度平坦切换到
$$
h_{\tau\tau}=0
\tag{7}
$$
并在结束点前后保一个固定正长度的开放区间。

四个终端目标仍可取
$$
h=H_-,\quad h_\tau=0,\quad
d=q_{\Gamma_{\rm out}}(H_-),\quad d_\tau=0.
\tag{8}
$$
其中 $\Gamma_{\rm out}$ 是这条修改后实际词的真实完整 history；
不固定它、不将第三 incoming 归零。
由(7)和终端 $h_\tau=0$，整个末开区间上 $h$ 逐函数等于 $H_-$。
原水平式 $k_\tau=2\eta h_\tau-2d_\tau$ 在端点给 $k_s=0$。
不要求 $k$ 在开区间恒定，也不要求 $k_{ss}(s_*)=0$。

### 3.1 为何真实四维 rank 保留

在 $\delta=0$、small-state 极限，零速度且
$d=q_\Gamma(H_-)$ 的末端为恒高度的平衡。
线性几何系统仍为
$$
f''=a_\tau,\qquad D''+\omega_-^2D=-\beta_-f''.
\tag{9}
$$
原四个高度加速度内控的读出核由
$1,\tau,\sin(\omega_-\tau),\cos(\omega_-\tau)$ 生成。
$\omega_->0$、$\beta_-\ne0$ 保四维可控性。
在内控后再加一段固定恒高度自由流，只把该四维读出乘一个可逆
有限时基本矩阵，所以极限 rank 不变。
平坦切换的基解同样是可逆有限时流。

实际系统保完整 history：在极限零速基态上，$M_2$ 和原三次/面积项
的历史增量对几何扰动从二次起，且本段 incoming 的
$\mathsf A=O(M/R^{3/2}),\mathsf Z=O(M/R^2)$ 趋零。
所以实际四目标（含 $q_{\Gamma_{\rm out}}$ 的导数）的 Jacobian
是上述可逆矩阵的 $o^1_R(1)+o^1_\delta(1)$ 扰动。
这里没有把第三有序项或 $\partial\Gamma_{\rm out}$ 删掉，
而是用 R559(22)(23) 的原导数界估它们。

### 3.2 残差和费用

R559/R564 长回路末残差为
$O(\mu_R/L)+o^1_\delta(1)$，其中对于 R567 的 $L\asymp\sqrt R$，
$$
\sigma=O(R^{-1/2}),\qquad
\kappa_R=O(R^{-1/2}+M/R),\qquad
\mu_R=O(\kappa_R\sigma/L^2).
$$
在 $\delta=0$ 的精确末平衡上切换(7)不产生新非零残差。
有限正 $\delta$ 的原 $\delta^2M_0$、$\delta^2\mathcal C^{[1]}$
及其它被保留项只给固定 $R$ 后的 $o^1_\delta(1)$。
故实际四末控修正仍为
$O(\mu_R/L)+o^1_\delta(1)$。
其速度平方费用仍是
$O((\mu_R/L)^2)/\delta+o^1_\delta(1/\delta)$；
如 R559(39)，相对于长回路最细 $S_0$ 费用的比值为
$O(\kappa_R^2/L)\to0$。
静态与原第三费用在固定快窗上由同一最后 $\delta$ 选择支付。

所以修改后 R567 的七维归一端图仍在同一个正参数盒上
$C^1$ 收敛到原 $4+1+2$ 简单零映射。
原 $P_2$ 停止图也同样保留。
在这一修改后的真正全词上重解八矩，而不是取旧八矩根后接一段未结账尾巴。
由同一个 IFT，全部八矩准确为零且(8)同时准确成立。

## 4. 两端确有反射匹配 germs

末端：修改后共同根上 $A=0$，(8)给 $\gamma=\upsilon=0$，
(7)在开邻域给偶控制。因此 §2 直接授予全部 scalar 偶 jets。
$T_*$ 可以是原完整大第三输出，不影响该唯一性论证。

初端：原 R544 §5 从 $S=(H,0,\Omega)$、零速度、$A=T=0$ 开始，
四个高度加速度控制紧支撑在初始固定快窗的内部。
可明确保留它们以前的一个开放 $h_{\tau\tau}=0$ 区间。
这与原初值和控制设计兼容；若固定窗布局需要扩长，只增加一个
固定快长度并在原四控制构造中一并选择，初始快费用类型不变。
因此初端也由 §2 有全部 scalar 偶 jets。
不要求两个端点的 scalar 值相同。

## 5. 真实正长度倒行完成第二、第三与 scalar 返回

令上述八矩、双偶端段为 $P$，长度为有限 $L_P>0$。
实际接上 $P^R$，其 scalar 函数是
$S_R(t)=S_P(L_P-t)$，frame/位置仍按原 ODE 正向恢复。
两端偶 germs 保接点和最后再次拼接处全部光滑。
原合法窗口只重排已发生的 scalar 值，因此保持。

第一段末 $A_*=0$，第三末值保为 $T_*$。
R526(12)–(15)在真实 incoming 下给
$$
A_{PP^R}(L_P+t)=-A_P(L_P-t),\qquad
T_{PP^R}(L_P+t)=T_P(L_P-t).
\tag{10}
$$
没有让倒行从新的零第三历史开始。
同一 $w=0,\chi$ 下 $q$ 反号、$b$ 不变，故原完整第四 ruling
沿两段仍恒为零。终端准确有
$$
\boxed{S_{PP^R}=S_{
m initial},\qquad
\mathsf m_{PP^R}=0,\quad A_{PP^R}=0,\quad T_{PP^R}=0.}
\tag{11}
$$
其中原密度 $M_{\rm raw}$ 在倒行中为偶，故更直接有
$\mathsf m_{PP^R}=2\mathsf m_P=0$，不需要从 $A=0$ 反推坐标。
这一次可使用的是原全算子身份，不仅是有限个配对或外层核。

## 6. 下一真实端口仍须继续

令第一段的实际 pose 为 $(G,v)$，
$D_F=\operatorname{diag}(-1,1,-1)$。
R526 给反射双词的真实 pose
$$
\left(GD_FG^{-1}D_F,\ (I-GD_FG^{-1})v\right).
\tag{12}
$$
它成为单位 pose 当且仅当
$GD_F=D_FG$ 且 $(I-D_F)v=0$。
本稿不从八矩零或反射偶性推这两个尚未支付的条件。
完整第四 characteristic 累计仍是 $2V_P(x,\theta)$，
不是零；也不能只看它的若干外配对便称整个 period 返回。

本稿推进到一个可真实正向重复的同规范 scalar/第二/第三返回块。
其 pose、第四 period、同十三规范和有限等距几何仍须在后继继续控制。
