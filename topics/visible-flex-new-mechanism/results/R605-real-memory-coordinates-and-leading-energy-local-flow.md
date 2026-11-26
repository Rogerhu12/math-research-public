# R605：真实二维记忆坐标与最高能量层的正则局部流

日期：2026-11-26。**已证明：下述可逆运动学、真实记忆增量、全程正m输入及首层内部局部流。** 原式纸证；没有新科学执行。
本文接 R603 已付的真实首 mass 终态：局部中心准备没有使全程能量、原历史或几何预算闭合。
新步骤是把全程运动学、真正的记忆环以及两条最高能量方程放在同一组可逆坐标中。
本文不把记忆环的可达性称作完整 ruling 环，也没有证明八矩根或宏观完成。

## 1. 原运动学的全程可逆坐标

从同一个原几何
$$
h>0,\qquad d=h\eta-k,\qquad \eta_s=k_s/(2h)
$$
定义
$$
\theta=\arctan d,\qquad
R=h\cos\theta=\frac h{\sqrt{1+d^2}},\qquad I=-\frac\eta h .
\tag{1}
$$
取唯一 $\theta\in(-\pi/2,\pi/2)$，则 $R>0$，而准确逆是
$$
\boxed{h=R\sec\theta,\qquad
\eta=-R\sec\theta\,I,\qquad
k=-\tan\theta-R^2\sec^2\theta\,I.}
\tag{2}
$$
所以没有释放额外几何自由度或另取一份 $\eta$。

原运动学与一个一阶记忆式准确等价：
$$
\boxed{I_s=\frac{\theta_s}{R^2}.}
\tag{3}
$$
证明直接由
$$
d_s=h_s\eta-k_s/2,\qquad
I_s=-\eta_s/h+\eta h_s/h^2=d_s/h^2
$$
及 $d_s=\sec^2\theta\,\theta_s$ 得到。
反过来，微分(2)并使用(3)立即恢复 $\eta_s=k_s/(2h)$。

固定实际中心 $h(0)=H,\ k(0)=\eta(0)=0$ 时，
$R(0)=H,\theta(0)=I(0)=0$。
任何给定的两条光滑函数 $R,\theta$ 所确定的真记忆都是
$$
I(s)=\int_0^s\frac{\theta_t(t)}{R(t)^2}\,dt.
\tag{4}
$$
不能在回路结束后把这个积分重新置零。

## 2. 原真实加速度与两条完整 ruling 不变

记 $q_g=1+d^2=\sec^2\theta$，
$a_R=R_s/R,\ \omega=\theta_s$。
则
$$
\gamma=h_s=h(a_R+d\omega),\qquad
\upsilon=k_s=-2q_g\omega-2h\gamma I,
\tag{5}
$$
$$
e_s=\gamma y+d_s=h y\,a_R+(hdy+q_g)\omega .
\tag{6}
$$
给 $R_{ss},\theta_{ss}=\omega_s$，原两加速度准确为
$$
a=h\left\{\frac{R_{ss}}R+2a_Rd\omega
 +(1+2d^2)\omega^2+d\omega_s\right\},
\tag{7}
$$
$$
b=-4dq_g\omega^2-2q_g\omega_s
 -2(\gamma^2+ha)I-\frac{2h\gamma\omega}{R^2}.
\tag{8}
$$
这两个式子保留全部真实二阶项。

它们对 $(R_{ss},\theta_{ss})$ 的 Jacobian 为
$$
\begin{pmatrix}
h/R&hd\\
-2hI(h/R)&-2hI(hd)-2q_g
\end{pmatrix},
$$
其行列式
$$
\boxed{-2(h/R)q_g=-2q_g^{3/2}\ne0.}
\tag{9}
$$
在 R598 已证明 $C_hC_k\ne0$ 的同一原合法盒内，R530 两条 $C_h/C_k$ ruling 在新坐标中仍是对两真实加速度非退化的同一系统；
没有因为改坐标得到新的逐点控制。
原八维 $A_s=M$、六个 R590 rho 更新、一个固定 $\chi$
和整个负侧反号仍须同时解。

这给一个十九态的等价几何坐标选择
$(R,\theta,I,R_s,\theta_s,A,\rho_+,\rho_-)$，
但坐标 Jacobian 非零不授原末图 rank 或根。

## 3. 真正二维回路的非零记忆与完整费用边界

在 $(R,\theta)$ 平面上作四条边：
$$
(R_0,\theta_0)\to(R_0,\theta_1)\to
(R_1,\theta_1)\to(R_1,\theta_0)\to(R_0,\theta_0).
$$
由(3)准确有
$$
\boxed{\Delta I=(\theta_1-\theta_0)
 \left(R_0^{-2}-R_1^{-2}\right).}
\tag{10}
$$
每条边可用端点全平的光滑时间函数参数化；
四角所有速度与更高jets为零，所以拼接光滑，
并且各边的积分仍准确等于上述值。
改变行走方向可改变真记忆的号。

若 $H<R_0<R_1$，整个回路保持
$$
m=h^2-H^2(1+d^2)=q_g(R^2-H^2)>0.
\tag{11}
$$
任意一个满足 $R>H$ 且 $(h,k,\eta)$ 处于原严格合法盒内部的几何状态，都可取足够小矩形，
使整条运动学回路仍留在该盒，并产生非零 $\Delta I$。
这是真实的三维运动学可达方向，不是把 $\eta$ 当作独立按钮。

但(10)没有使 $k,\eta$ 回到起值：
回到同一 $R,\theta$ 后，它们按(2)记录新的 I。
也没有结算真实 $A,\rho$、两条完整 ruling 或 frame/位置。
把回路放慢可以降低速度，却会增长物理时间和原位置积分成本；
本文不把这个操作称作宏观无代价。

### 单叶为什么不提供所需负矩

若从 $\theta=I=0$ 出发，始终有一个正单值函数 $R=\mathcal R(\theta)$，则
$$
I=\int_0^\theta \mathcal R(t)^{-2}\,dt
$$
与非零 $\theta$ 同号。由(2)，$k$ 与 $\theta$ 反号，
$d=\tan\theta$ 与 $\theta$ 同号，所以
$$
-kd>0\quad(\theta\ne0).
\tag{12}
$$
这正是原 $p_1$ 密度。只沿这样的单叶往返不能把它清零。
二维 R/θ 记忆回路能改变 I 与当前 θ 的相对号，
才提供这条点态正号之外的真实入口。
此处不是另发一个“所有路径不可行”命题。

## 4. 一个全程保持 m>0 的有限强准备族

令 $s=Lx,\ \vartheta=\pi x/2$，取
$$
q(x)=\sin\vartheta\,
       \exp\left(\sum_{j=0}^{p} a_j\cos j\pi x\right),\qquad
R(x)=H\left(1+\frac{q(x)^4}{1+q(x)^4}\right).
\tag{13}
$$
于是 $H<R(x)<2H$ 对每个 $x>0$ 成立，
$R-H=O(s^4)$，且 $R_s(1)=0$。
选择固定 $\theta_c=3/5$，并置
$$
\theta(x)=\theta_c\tanh\left(c_1\sin\vartheta+
         \sum_{j=1}^{q} b_j\sin((2j+1)\vartheta)\right),
$$
$$
c_1=-\frac{2L}{\pi\theta_c}
       -\sum_{j=1}^{q}(2j+1)b_j.
\tag{14}
$$
这准确给
$$
\theta(0)=0,\qquad \theta_s(0)=-1,\qquad
\theta_{ss}(0)=0,\qquad \theta_s(1)=0.
$$
由(2)–(8)，以(4)的真 I 定义几何，
$$
h(0)=H,\quad h_s(0)=0,\quad h_{ss}(0)=H,\quad
k(0)=\eta(0)=0,\quad k_s(0)=2,\quad k_{ss}(0)=0.
\tag{15}
$$
原末 $h_s(1)=k_s(1)=0$ 也保持。

这是**整个路径**的运动学输入，不只一个中心jet。
其 m 由(11)(13)在全部 $x>0$ 准确为正。
取 $.9\le H\le1.2$ 时，利用
$\cos(3/5)\ge1-\tfrac12(3/5)^2=41/50$，
$$
.9\le h(x)<\frac{12/5}{41/50}=\frac{120}{41}<3.
\tag{16}
$$
因此高度范围无需采样保证。

$I,k,\eta$ 和速度仍由同一真实积分、(2)(5)决定；
(16)不保证它们自动进入原盒。
这些必须作为完整路径的独立约束，不能省掉。
当前族也不自动使末 $p_2=0$；
若采用此输入，必须把它与另外七个原矩一起支付，
而不是把旧单调 c 的 p2 结论搬到新族。

## 5. 两侧最高能量层的准确方程

用 R603 的六参考节点 $c_i>0$ 与正权 $w_i$，并记
$$
Q(y)=1+(hy+d)^2,\qquad
C_A(y)=r_0+(r_1+s_0)y+\frac32s_1y^2
 +(t_1-p_1/4)y^3-\frac14p_2y^4,
$$
$$
V_2(y)=-2C_A(y)-\frac{Q(y)}{4h^3}
  \{hy\,a_R+(hdy+q_g)\omega\}.
\tag{17}
$$
所有 A 都是同一真 $A_s=M$，不是每个节点另配系数。

原负侧是 $(h,-k,-\eta,-\gamma,\upsilon)$、$JA$；按 $(p_0,p_1,p_2,t_1,r_1,s_1,s_0,r_0)$ 的次序，$J=\operatorname{diag}(1,-1,1,-1,-1,1,-1,1)$。因此 $d_-=-d$、$(d_s)_-=d_s$，从而 $(e_s)_-(y)=(e_s)_+(-y)$。逐项对原八坐标与(6)可核
$$
Q_-(y)=Q_+(-y),\qquad C_{JA}(y)=C_A(-y),\qquad
(V_2)_-(y)=(V_2)_+(-y).
\tag{18}
$$
这只是在原多项式读出中的 $y\mapsto-y$ 身份；
实际母仍位于原正窗口，不搬动副本或重设右锚。

定义
$$
B_+=\sum_iw_iQ(c_i)V_2(c_i)^2,\qquad
B_-=\sum_iw_iQ(-c_i)V_2(-c_i)^2 .
$$
在 R603 的同一个有界缩微极限及 P1=0 结论下，
正支 $P_2>0,m>0$ 的完整首层准确为
$$
\boxed{B_+=\lambda m,\qquad B_-=\lambda m,\qquad
\lambda=P_2/(4c_*)>0,}
\tag{19}
$$
其中 $\lambda$ 是**整条路径上的一个常数**。
$m>0$ 只支付必要符号；还必须同时支付两式及常值比率。
将(19)按每点分别配 λ 会改变原固定规范，本文不这样做。

## 6. 首层确有正则局部流：两椭圆的真实交点

不能仅画两椭圆就宣称它们相交。
这里给一个准确可计算的内部正则点。

取 $h>H>0,\ d=0,\ A=0$，并选合法 I（例如 I=0，则 k=η=0）。
此时 R=h，$m=h^2-H^2>0$，$Q_i=1+h^2c_i^2$。
式(17)给
$$
B_\pm=\mathsf A a_R^2\pm2\mathsf B a_R\omega+
       \mathsf C\omega^2,
$$
$$
\mathsf A=\frac1{16h^4}\sum_iw_iQ_i^3c_i^2,\quad
\mathsf B=\frac1{16h^5}\sum_iw_iQ_i^3c_i,\quad
\mathsf C=\frac1{16h^6}\sum_iw_iQ_i^3.
\tag{20}
$$
三个数严格正。
对任意固定 $\lambda>0$，取
$$
a_R=0,\qquad
\omega_*=\pm\sqrt{\lambda(h^2-H^2)/\mathsf C}\ne0 .
$$
这正好同时满足(19)，不是近似交点。
两方程对 $(a_R,\omega)$ 的真实 Jacobian 为
$$
\begin{pmatrix}
2\mathsf B\omega_*&2\mathsf C\omega_*\\
-2\mathsf B\omega_*&2\mathsf C\omega_*
\end{pmatrix},
\quad
\boxed{\det=8\mathsf B\mathsf C\omega_*^2>0.}
\tag{21}
$$
所以隐函数定理在该点附近把 $(a_R,\omega)$ 唯一解为
$(R,\theta,I,A)$ 的光滑函数，保同一固定 λ 与同一支号。
与
$$
R_s=Ra_R,\quad\theta_s=\omega,\quad I_s=\omega/R^2,\quad A_s=M
\tag{22}
$$
结合，标准局部存在唯一性给出**真正满足两条首层能量方程且保真 M/记忆的局部流**。

这个局部结论不支付 prepared 中心到该点的前缀。
它也不授八末矩、原有限ε的C²余项或rho方程。
prepared 中心 $m=B_\pm=0$ 是退化点；
把(21)从内部点直接延伸过去会漏掉一个必须支付的问题。
R601/R603 的精确中心条件只是与该退化起点相容的启动资料。

## 7. 与原有限ε问题的接口及下一实际输入

任何下一份源都必须分开以下三种读数：

1. (13)(14)(4)的实际运动学 guide及全部八矩；
2. (19)用一个固定 λ 的**全程首层**缺陷，而非只核 m 的号；
3. 同一实际母、同一新全history下的两条完整 R590/R530 ruling，
   包括全部C²余项、非负正平方、原rho、一个固定χ和原末条件。

先以真实 M 计算 A，再拟合一个全程 λ，可以构造有理由的首层初猜；
这不删除原问题的有限ε项。
原 full mass 必须接着使用完整真实种子，并保原单位缺陷与整条几何预算。
本轮已付九族不纯加迭代；新的输入应在全程 R/θ 记忆与能量兼容上改变。

若采用原29条BC的准确变量消元，也只能改变方程组织：
初端19态由同一真实中心十参数恢复，末八A与两个速度固定为原目标，
其余质量方程通过原链式Jacobian拉回。
不能把错误的独立中心势或不满足M的guide端值当作已经付清的history。

本文已经证明的是可逆全程坐标、可控的真记忆增量、
m正支的明确有限输入和首层内部正则局部流。
prepared起点可达、全程首层返回、全部八矩、有限ε原根、
原第三/第四period、pose及题目的reach/holding仍未支付；
后继实际求解必须逐项保留这些条件。

