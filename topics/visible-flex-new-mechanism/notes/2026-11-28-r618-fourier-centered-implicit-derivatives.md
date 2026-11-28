# R618：固定度量隐式导数中的准确 Fourier 背景消去

2026-11-28。**下述代数恒等式已证明；尚未运行的新数值实现不等于误差证书。**
接[原持久分拆终态](2026-11-28-r618-split-first-complete-state-terminal.md)，
不改变R618的目标度量、真实高度、角模、核心端式或求解行。

## 1. 真正可消去的量

当前响应高度的每个参数方向$H$都是正偶频率的有限余弦和，
包括完整非线性核心映射的参数导数，最高从属频率96。
这是原`height_direction`和`one_height_direction`的实际公式；
原基场的tanh部分被冻结，不在这些方向中重新展开成有限tanh导数。
因此准确有

$$
\langle H_r\rangle=\langle H_{rr}\rangle=
\langle H_\theta\rangle=\langle H_{\theta\theta}\rangle=
\langle H_{r\theta}\rangle=0. \tag{1}
$$

固定512点等距角泛函对这些有限频率也准确为零；浮点三角值与求和则
不必为机器零。(1)来自函数定义，不能将任意有非零均值的未来方向塞进此接口。
下面只在角平均内消去乘在(1)前的常数；点值导数仍保全部背景项。

## 2. 均值根的一阶方向

沿用R618完整状态，令$p=-W+s+f_r$、$q=f_\theta$、$t=f_{\theta\theta}$，
$b,u,N,C,\omega$与原文相同，$c_0=\langle\omega C\rangle\ne0$。
度量$E,E_r$保持固定。设$a=N/u$，直接微分得

$$
A=\partial_p a=\omega C,
$$
$$
B=\partial_q a=
\frac{rq}{ub^3}+\frac{3r^2ptq}{ub^5}
+\frac{Nr^2p^2q}{u^3b^4},
\qquad T=\partial_t a=\frac{r^2p}{ub^3}. \tag{2}
$$

其中第一式由
$\partial_pN=r^2t/b^3$、$\partial_pu=-r^2p/(ub^2)$，并用
$u^2+r^2p^2/b^2=E$合并即可。其余两式逐项微分得到。
固定turning均值后

$$
\delta s=-\frac{\langle AH_r+BH_\theta+TH_{\theta\theta}\rangle}{c_0}
=-\frac{\langle(A+W)H_r+BH_\theta+(T+W/r)H_{\theta\theta}\rangle}{c_0}. \tag{3}
$$

第二等号准确使用(1)，没有改变方程或删角模。参考轴对称状态中
$A=-W$、$T=-W/r$；在接近平帽的地方，先以持久分拆的Decimal状态
形成$A+W,T+W/r$，避免先把这两个小差量丢到binary64再作背景求和。
这个代数变形并不保证当前全部系数条件良好；实际attainer必须另报。

## 3. 完整离解连接导数

记$w=\omega$、$B_0=f_{r\theta}-q/r$，沿用原分拆

$$
K=(e+Wd)t+r d-Wq^2/r,\quad d=s+f_r,
$$
$$
Q=EB_0^2+W'K+e_rM/2-Cf_{rr},\qquad
D=C s_r-Q,\qquad R=wD. \tag{4}
$$

令$\delta p=H_r+\delta s$。
由$\delta w/w=-3(\delta u/u+\delta b/b)$，

$$
\frac{\delta u}{u}+\frac{\delta b}{b}
=-\frac{r^2p}{u^2b^2}\delta p
-\left(\frac{r^2p^2q}{u^2b^4}+\frac q{b^2}\right)H_\theta. \tag{5}
$$

把$\delta Q-s_r\delta C$按五个方向jet收集，定义

$$
\begin{aligned}
L_p={}&w\left[W'(Wt+r)+\frac{e_rt}{2}-r(s_r+f_{rr})
-\frac{3Dr^2p}{u^2b^2}\right],\\
L_q={}&w\left[-\frac{2EB_0}{r}-\frac{2W'Wq}{r}-\frac{e_rq}{r}
-3D\left(\frac{r^2p^2q}{u^2b^4}+\frac q{b^2}\right)\right],\\
L_t={}&w\left[W'(e+Wd)+\frac{e_rp}{2}-E(s_r+f_{rr})\right],\\
L_{rt}={}&2wEB_0,\qquad L_{rr}=-wC=-A.
\end{aligned} \tag{6}
$$

这些含$D$的项是离解权重项，不能删除。
逐项代入(4)--(5)给完整恒等式

$$
\delta R=A\delta s_r-L_p(H_r+\delta s)-L_qH_\theta
-L_tH_{\theta\theta}-L_{rt}H_{r\theta}-L_{rr}H_{rr}. \tag{7}
$$

同一mean连接要求$\langle\delta R\rangle=0$，所以由(1)

$$
\delta s_r=\frac1{c_0}\left[
\left\langle(L_p-W')H_r+L_qH_\theta+
(L_t-W'/r)H_{\theta\theta}+L_{rt}H_{r\theta}
+(L_{rr}-W)H_{rr}\right\rangle
+\langle L_p\rangle\delta s\right]. \tag{8}
$$

这里用到的$W',W'/r,W$确为与角无关的标量。
轴对称背景中$L_p=W'$、$L_t=W'/r$、$L_{rr}=W$。
这也解释了为何原式
$[\langle\delta wQ+w\delta Q\rangle-s_r\delta c_0]/c_0$
可以先用$Q-s_r C=-D$合并，再作(8)，而无须两个大均值相减。
(2)、(6)的系数从同一完整Decimal状态求出，(3)、(8)用longdouble
收缩，最后才进入原binary64全行QR/SVD。没有删奇异方向，也没有改行权。

## 4. 点值导数全部加回背景

输出角网不应用“均值为零”来删除点值。新实现用与(7)相同的分拆：

$$
\begin{aligned}
\delta a={}&-W\delta p-(W/r)H_{\theta\theta}
+(A+W)\delta p+BH_\theta+(T+W/r)H_{\theta\theta},\\
\delta R={}&-W(\delta s_r+H_{rr})-W'\delta p-(W'/r)H_{\theta\theta}\\
&+(A+W)(\delta s_r+H_{rr})-(L_p-W')\delta p-L_qH_\theta\\
&-(L_t-W'/r)H_{\theta\theta}-L_{rt}H_{r\theta}.
\end{aligned} \tag{9}
$$

展开(9)立刻恢复(2)、(7)。两次primitive以及完整离解相位项仍用原公式。
完整1473列Jacobian、完整组合试方向和mean-height参数查询都显式接入新链，
不会出现值走新链而步长或Jacobian继续用旧消减公式的情况。

## 5. 标量根的实际进度

原已付日志显示trial mean经常用约43次纯二分达到$10^{-13}$的绝对小坐标宽度。
新算法仍保存实际符号括号；偶数次允许区间内的Newton候选，奇数次必作二分。
因此任何两次未终止更新至少包含一次二分，保持进度保障。
当当前残差相对导数很小时，仅提议$x\pm\mathrm{tol}/4$小盒，
必须实际评价两端并符合原符号条件才接受；小残差本身不产生根资格。
参考与trial的绝对坐标预算、原same-sign box和全部分拆身份不变。

这些仍是数值观察，既有七类源误差、角求积、径向和舍入误差没有因此变成0。
此算法应先实际求出有分辨率的非零下降；宏观幅度、完整同g精化、嵌入性
和全时reach仍必须按原README另行满足。
