# R601 Prepared 中心的真实一阶 jet、固定规范选择与最高能量延后

日期：2026-11-26。**原方程纸证；没有新科学执行。**
本稿接 R590/R598，给下一真实初猜一条准确可施加的中心条件，
不改变当前已经发布的 R598 首跑，不宣全程 slow manifold、
八矩根或宏观几何完成。

## 1. 同一个真实中心与固定母

全程使用同一实际母、右锚、完整 $A_s=M$ 和 R590 状态。
记原矩顺序
$$
A=(p_0,p_1,p_2,t_1,r_1,s_1,s_0,r_0),
$$
并写
$$
d=h\eta-k,\quad d_s=\gamma\eta-\upsilon/2,\quad
Q=1+(hy+d)^2,\quad e_s=\gamma y+d_s .
\tag{1}
$$
此处 $d_s$ 表示这个真实导数，后文需要再求它的时间导数，
不把它释放为独立变量。

固定中心 $s=0$ 的 prepared 数据
$$
(h,k,\eta,\gamma,\upsilon)=(H,0,0,0,v),\qquad H>0,
$$
$$
A_c^{\rm odd}
=\left(\frac v{12H},0,\frac v{16H^3},\frac v{24H}\right),
\qquad A_c^{\rm even}=0,\qquad \rho_+=\rho_-=0 .
\tag{2}
$$
odd 顺序是 $(p_0,p_2,r_0,s_1)$。
$H,v$ 是同一真实中心参数；不把旧母的 $\nu,\rho,E_c$ 搬来。

令 $a=h_{ss}(0),b=k_{ss}(0)$。
这两个数在真实路径上必须满足原两条 ruling；第4节准确结算。
当 $b=0$ 时，本文给出全 first-time-jet 的明确身份。

## 2. 原正平方的三个 profile 系数

对一微包的固定 jets $u,p=u',r=u''$，R590 写
$$
V:=H_A+2F_0=V_0(y)u+V_1(y)p+V_2(y)r.
\tag{3}
$$
由原 E8 六项式，
$$
V_0=p_0+p_1y+p_2y^2,
$$
$$
V_1=2r_1+2(s_1-p_0/2)y+2(t_1-p_1/2)y^2-p_2y^3
+\frac{\gamma Q}{4h^3},
$$
$$
V_2=-2C_A-\frac{Qe_s}{4h^3},
$$
$$
C_A=r_0+(r_1+s_0)y+\frac32s_1y^2+
(t_1-p_1/4)y^3-\frac14p_2y^4.
\tag{4}
$$
全部 $A$ 是真实历史，不是另配多项式系数。

代(2)直接给
$$
V_0(0,y)=\frac v{12H},\qquad V_1(0,y)=V_2(0,y)=0,
$$
$$
V(0,y)=\frac v{12H}u.
\tag{5}
$$
所以 prepared 中心的正能量一般非零；它只是没有 $p,r$ 高导项。

## 3. 从真 $M$ 逐项求第一时间导数

原 R530/R584 密度在(2)处为
$$
(p_0,p_1,p_2)_s=(0,0,0),\qquad
(t_1)_s=-\frac18,
$$
$$
(r_1)_s=-\frac1{8H^2},\qquad
(s_1)_s=(r_0)_s=0,\qquad
(s_0)_s=-\frac{v^2}{16H^2}.
\tag{6}
$$
这里特别保留了原 $s_0$ 中的 $\upsilon^2$ 项。
运动学又给
$$
h_s=0,\quad d=0,\quad d_s=-v/2,\quad
Q_c=1+H^2y^2,\quad Q_s=-Hvy .
\tag{7}
$$
当 $b=0$，$e_{ss}=ay$，故
$$
(Qe_s)_s=\frac{Hv^2y}{2}+aQ_cy.
\tag{8}
$$

先由(4)(6)求
$$
(V_0)_s(0,y)=0,
$$
$$
(V_1)_s(0,y)
=-\frac1{4H^2}-\frac{y^2}4+\frac{aQ_c}{4H^3}
=\boxed{\frac{a-H}{4H^3}Q_c}.
\tag{9}
$$
再有
$$
(C_A)_s(0,y)
=-\left(\frac1{8H^2}+\frac{v^2}{16H^2}\right)y-\frac{y^3}8 .
$$
与(8)结合，
$$
\begin{aligned}
(V_2)_s(0,y)
&=\left(\frac1{4H^2}+\frac{v^2}{8H^2}\right)y
+\frac{y^3}4-\frac{v^2y}{8H^2}-\frac{aQ_cy}{4H^3}\\
&=\boxed{\frac{H-a}{4H^3}yQ_c}.
\end{aligned}
\tag{10}
$$
$\,v^2$ 两项确由原 $s_0$ 和真实 $Qe_s$ 的导数相消，
不是在高频近似里丢掉。

因此完整微包多项式有准确恒等式
$$
\boxed{V_s(0,y)=\frac{a-H}{4H^3}Q_c(p-yr).}
\tag{11}
$$
它是原完整 $A_s=M$ 与真实几何导数的结论，
没有冻结 $Q$、$A$ 或 incoming。

特别可选
$$
\boxed{a=H,\qquad b=0,}
\tag{12}
$$
使 $V_s(0,y)=0$，包括 $p$ 与 $r$ 的一阶生成都同时消去。

### 3.1 没有把整个正平方置零

令 $\mathcal I$ 表示 R590/R598 同一正权完整积分；
其 $D_0^2(u''')^2$ 因子保持原样。
原真实正能量是
$$
\mathcal E(s)=\mathcal I\left[
\frac{Q}{64h}D_0^2(u''')^2V^2\right].
\tag{13}
$$
在(2)(12)下，
$$
\mathcal E(0)
=\frac{v^2}{9216H^3}
\mathcal I[D_0^2(u''')^2Q_cu^2],
$$
$$
\mathcal E_s(0)
=-\frac{v^3}{9216H^2}
\mathcal I[D_0^2(u''')^2y\,u^2].
\tag{14}
$$
后一式来自仍然变化的正权 $Q/h$。
因此即使 $V_s=0$，也一般不使 $\mathcal E_s=0$。
$v\ne0$ 时 $\mathcal E(0)>0$，没有删除能量。

对固定光滑真实轨道，(12)使 $V_1,V_2=O(s^2)$，
相较通常 $O(s)$ 延后一阶。用 R598 幅
$\varepsilon^{7/4}/256$ 计，最高 $r^2(u''')^2$ 项于是从
$O(\varepsilon^{-2}s^2)$ 延后为
$O(\varepsilon^{-2}s^4)$。
这个陈述的常数依赖该真实轨道的高阶 jets；
它不授跨 $\varepsilon$ 的统一存在区间或全程能量上界。
正平方中的交叉项和其它阶项在(13)仍完整存在。

还可准确看到这不是全程零流形：
$$
(p_2)_{ss}(0)=-\frac{Hv}{2},
\qquad [y^4](V_2)_{ss}(0)=-\frac{Hv}{4}.
\tag{15}
$$
因为原 $(p_2)_s=-kh/2$，而 $V_2$ 的唯一四次系数为 $p_2/2$。
若 $v\ne0$，不论怎样选择其它更高几何 jet，
$V_2$ 的二阶生成都不能全部为零。
(12)是一个准确较好启动条件，不是偷换成任意长的 prepared 路径。

## 4. 同一固定 $\chi$ 如何真支付 $a=H,b=0$

在 R590 的中心化、去势坐标，
$$
K_\pm=R_\pm^0-4w_\pm\rho_\pm
-4w_\pm(E_\pm-E_c)-2w_\pm\bar\nu .
$$
用原中心零配对坐标
$$
\bar\nu=(\zeta_0-H^2\zeta_2,\zeta_1,\zeta_2).
\tag{16}
$$
在(2)处两侧实际几何和 $JA=A$ 相同，
$\rho_\pm=0$、$E_\pm=E_c$，且
$$
w_c=(1/(4H),0,H/4),\qquad
w_c\bar\nu=\zeta_0/(4H).
$$
故两条完整 ruling 准确变为
$$
R_c^0-\frac{\zeta_0}{2H}+C_{h,c}a+C_{k,c}b=0,
$$
$$
R_c^0-\frac{\zeta_0}{2H}+C_{h,c}a-C_{k,c}b=0.
\tag{17}
$$
R598 真实域中 $C_{k,c}>0$，相减给 **真实** $b=0$。
$C_{h,c}<0$，再选择一次固定
$$
\boxed{\zeta_0=2H\{R_c^0+C_{h,c}H\}}
\tag{18}
$$
即使两式同时给 $a=H$。
$\zeta_1,\zeta_2$ 在中心配对仍为零，可保持原全程常数自由度；
不能把它们或 $\zeta_0$ 沿路径重新拟合。

(18)中的 $R_c^0,C_{h,c}$ 必须在这份母、这份真实中心完整计算，
不是换用旧母的数值。选择 $\zeta_0$ 后仍按 R590 还原
$\widehat\nu=\bar\nu-2E_c$、$\nu=\bar\nu-2r_c$，
并使用 R521 的同一个固定 Gram 右逆得到 $\chi_\theta$。
因此这是在原规范内支付一个中心加速度，没有增加逐点控制或删掉能量。

## 5. 可直接实施的十参数新 guide

R598 已跑 guide 写成
$$
h(x)=1.9+\tanh\left(\sum_{j=0}^4\alpha_j\cos j\pi x\right),
\qquad s=Lx.
$$
定义 $S=\sum\alpha_j$，则
$$
H=1.9+\tanh S,\qquad
h_{ss}(0)=-\frac{\pi^2(1-\tanh^2S)}{L^2}
\sum_{j=1}^4j^2\alpha_j.
\tag{19}
$$
故可用 $(H,\alpha_1,\alpha_2,\alpha_3,L)$ 直接定义
$$
B_*=-\frac{HL^2}{\pi^2[1-(H-1.9)^2]},
$$
$$
\alpha_4=\frac{B_*-\alpha_1-4\alpha_2-9\alpha_3}{16},\quad
\alpha_0=\operatorname{atanh}(H-1.9)-\sum_{j=1}^4\alpha_j.
\tag{20}
$$
只要 $.9<H<2.9$，所有量有限，
高度全域仍在 $(.9,2.9)$，且(19)准确等于 $H$。
原奇半波的 $k$ 给 $k_{ss}(0)=0$；
原单调标量 $c$ 继续处理 $\int hk=0$。

这样原11参数 guide 变为10参数；
在(2)与(20)已支付的真实条件下，
仍将其余七个原末矩联合拟合。
不能因“有3个剩余参数”宣称满秩、根或空间预算必可达。

新运行应从 run45828239888 已付11参数读取
$H=1.9+\tanh(\sum\alpha_j)$、$\alpha_{1,2,3}$、五个曲率系数与 $L$，
再按(20)形成真正新输入，不从旧初猜重跑400nfev。
数值 $H$ 的转换与后续新求积/优化都只能在公开 Actions 中执行。
该初猜会改变中间高度形状；其 $\eta$、完整八矩、所有 history、
$\zeta$ 与原 frame/空间预算必须共同重算，不能保留旧数组。

进入完整 BVP 后可以仍释放全部原10个中心参数；
(20)(18)只是有根据的新种子，不强行把完整解限制成 prepared 全程。
这条新中心身份未解决七剩余矩、原 ruling 轨道、pose/period、
以及 R598 首 guide 已暴露的 reach/diameter 必要预算。

