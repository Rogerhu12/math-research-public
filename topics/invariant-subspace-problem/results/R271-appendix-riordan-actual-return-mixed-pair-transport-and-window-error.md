# R271 附录：Riordan 对实际返回混合配对的运输与同窗误差

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文把已经付费的相对孔 Riordan 映射用于同一个实际来源的返回配对。运输只需完整右域与裸商，不需要运输或比较整个左 Gram。产生的误差由原裸费和同一实际未来能量支付，常数与头宽及窗口无关。运输后的测试仍明确保留逆伴随与真实返回投影；本文没有支付其余的返回主项。

依赖：

- [完整返回的物理有限系统](R271-appendix-complete-return-orthogonal-decomposition-driven-system-and-unique-lift.md)；
- [强位同一顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)；
- [强 gauge 的同一未来与返回主项](R271-appendix-strong-gauge-true-left-feedback-driven-return-and-ordinary-endpoint.md)；
- [相对孔 Riordan 的完整右域、裸商及统一费用](R271-appendix-relative-hole-riordan-conjugacy-full-bare-source-transport-and-uniform-budget.md)。

## 1. 完整物理域及映射

固定原强联块
$$
C=A_m+D_<,\qquad C^h=0,\qquad D=D_>,\qquad \delta=\|D\|.
$$
在远孔切口 $n$ 上，用前稿的真实右环境 $\mathscr W$、完整右链空间 $\mathcal Y_f$ 和裸链空间 $\mathcal Y_b$。裸链以其物理低旗代表嵌入 $\mathscr W$。同源最小列、完整零源与裸零源记为
$$
J_f,\quad J_b,\quad Z_f,\quad Z_b.
$$
置
$$
\mathscr E=\mathscr W^{\rm hi}\oplus^\perp Z_b,\qquad
\mathscr E_0=\mathscr E\ominus Z_f,\qquad
\mathcal R=J_f-J_b.
\tag{1.1}
$$
则 $\mathcal Rr\in\mathscr E_0$，且
$$
\mathscr E_0\perp Z_f,\qquad
\mathscr E_0\perp\operatorname{Ran}J_b,\qquad
\mathcal R^*\mathcal R=H-B.
\tag{1.2}
$$
这里 $B=J_b^*J_b$ 是完整裸链费用，不是普通完整右费用 $H=J_f^*J_f$。

令
$$
\phi(z)=-\frac{\psi_m(-z)}{d_0},\qquad
g(z)=\frac{\psi_m(z)}{d_0z},\qquad
\widehat C=\frac{\psi_m(C)}{d_0}=Cg(C).
\tag{1.3}
$$
所有函数都保到真实 $h-1$ 阶。帽号表示这个新头、同一远尾 $D$、同一切口的物理右系统。

已证明的 Riordan 算子 $K:\mathscr W\to\widehat{\mathscr W}$ 及其裸商映射 $K_b$ 满足
$$
K\mathcal Y_f=\widehat{\mathcal Y}_f,\quad
KZ_f=\widehat Z_f,\quad
K_b\mathcal Y_b=\widehat{\mathcal Y}_b,\quad
K_bZ_b=\widehat Z_b.
\tag{1.4}
$$
来源准确变为 $r\mapsto g(C_{\rm s})r$；以下简记 $gr$。高旗由 $K$ 双向保持，所以同时有
$$
K\mathscr E=\widehat{\mathscr E}.
\tag{1.5}
$$
选前稿的 $\tau_{14}$、$R=\lceil4e^{\tau_{14}}\rceil$、$h=d+R$，则存在明确但很大的绝对常数
$$
M_0=16(1+e^{1070}),\qquad \mathcal C_0=e^{2M_0}
$$
使
$$
\|K\|,\ \|K^{-1}\|,\ \|K_b\|,\ \|K_b^{-1}\|
\le\mathcal C_0.
\tag{1.6}
$$
这个常数不随 $m,n,R$ 或窗口增长。下文也适用于任意满足 (1.4)--(1.6) 的实际双向右映射。

本文在已证明的闭右空间及自然源形式域上使用最小列。对于由 $u_Q$ 产生的实际来源，两种右最小列及下面的配对均存在。一般来源可先在共同有限形式域证明，再按这些有界映射及相应最小范数完备化；本文不把潜在无界的环境 $D^\dagger$ 引入估计。

## 2. 返回测试的正确运输

对任意 $e\in\mathscr E_0$，定义
$$
\boxed{
\widehat e=P_{\widehat{\mathscr E}}K^{-*}e.
}
\tag{2.1}
$$
这里必须保留逆伴随及真实投影。

由 $KZ_f=\widehat Z_f$，
$K^{-*}e\perp\widehat Z_f$。又
$\widehat Z_f\subseteq\widehat{\mathscr E}$，所以
$$
\widehat e\in\widehat{\mathscr E}_0,\qquad
\|\widehat e\|\le\mathcal C_0\|e\|.
\tag{2.2}
$$
这一步没有声称 $K$ 为酉，也没有把 $K^{-*}$ 换成 $K$。

因为 $\widehat J_f(gr)$ 是帽系统的完整最小列，(1.4) 给
$$
K^{-1}\widehat J_f(gr)-J_fr\in Z_f.
\tag{2.3}
$$
并且 $\widehat{\mathcal R}(gr)\in\widehat{\mathscr E}_0$。因此投影 (2.1) 不改变它的配对。利用 $e\perp Z_f$ 及 $e\perp J_br$，严格得到
$$
\boxed{
\left\langle\widehat{\mathcal R}(gr),\widehat e\right\rangle
=
\left\langle\mathcal Rr,e\right\rangle
-
\left\langle K^{-1}\widehat J_b(gr),e\right\rangle.
}
\tag{2.4}
$$
这是完整最小化之后的恒等式。它没有把 $\widehat J_f(gr)$ 认作 $KJ_fr$，也没有把 $\widehat J_b(gr)$ 认作 $K_bJ_br$。

后一个裸列有可行上界
$$
\|\widehat J_b(gr)\|
\le\|K_bJ_br\|
\le\mathcal C_0\alpha(r).
$$
故 (2.4) 的误差满足
$$
\boxed{
\left|
\left\langle\widehat{\mathcal R}(gr),\widehat e\right\rangle
-\left\langle\mathcal Rr,e\right\rangle
\right|
\le\mathcal C_0^2\alpha(r)\|e\|.
}
\tag{2.5}
$$
右端只含原裸费和被运输的同一个测试；没有完整返回范数或环境相似条件数。

## 3. 原同一顶部的正主配对

取原实际
$$
u=u_Q,\qquad r=r_n^C=Cu_n,\qquad
Y_n=(u_{n+1},\ldots,u_{n+h}),
\qquad n+h+R<Q.
$$
前稿准确给出
$$
e_n=P_{\mathscr W}Y_n+J_br\in\mathscr E_0,
$$
$$
\|e_n\|^2
=\|P_{\mathscr W}Y_n\|^2-\alpha(r)^2
\le\|Y_n\|^2-\alpha(r)^2,
\qquad
\mathcal R^*e_n=(L+B)r.
\tag{3.1}
$$
因此令 $\widehat e_n$ 按 (2.1) 取值，便有
$$
\boxed{
\begin{aligned}
\mu(r)^2+\alpha(r)^2
={}&\operatorname{Re}
\left\langle\widehat{\mathcal R}(gr),\widehat e_n\right\rangle
+\epsilon_n,\\
|\epsilon_n|
\le{}&\mathcal C_0^2\alpha(r)\|e_n\|
\le\frac{\mathcal C_0^2}{2}\|Y_n\|^2.
\end{aligned}
}
\tag{3.2}
$$
最后一步使用
$\alpha(r)^2+\|e_n\|^2\le\|Y_n\|^2$，保两项的联合预算。

帽号来源与原来源之间也已有同一真实源度量的比较：
$$
\|g(C_{\rm s})-I\|_{L+B}\le\frac{2M_0}{h}.
\tag{3.3}
$$
故在原左最小图中 $U(gr-r)$ 的范数不超过
$(2M_0/h)\|r\|_{L+B}$。这只是原系统中的来源接近；本文并未由 (3.3) 推出帽系统的左 Gram 与 $L$ 可比。

若 $n$ 遍历任一合法切口集合 $\mathcal I$，每个实际远孔分量至多被 $h$ 个 $Y_n$ 读取。因此
$$
\boxed{
\sum_{n\in\mathcal I}|\epsilon_n|
\le\frac{\mathcal C_0^2h}{2}
\|P_{\mathcal N_> >\min\mathcal I}u\|^2.
}
\tag{3.4}
$$
在间距至少 $h$ 的网格上，右端的 $h$ 可去掉。并且
$$
\sum_{n\in\mathcal I}\|\widehat e_n\|^2
\le\mathcal C_0^2h
\|P_{\mathcal N_> >\min\mathcal I}u\|^2.
\tag{3.5}
$$
这些是同一 $u_Q$ 的物理平方和，未改换一个独立测试族。

在原带权母窗口中 $\|u_Q\|\le\|w\|$，合法切口数与 $Q$ 同阶。故平均误差至多
$O(\mathcal C_0^2h/Q)\|w\|^2$。由于 $\mathcal C_0$ 为固定常数，而已有 $h^2/Q\to0$，这个误差随 $m\to\infty$ 趋零。这里不需要假定 $w$ 的物理尾有任何给定衰减率。

## 4. 仍带原 gauge 的未付主项

原强 gauge 余项留下的实际测试是
$$
e_n^{\,q}=q_h(-T_0)^*e_n\in\mathscr E_0.
$$
因为 $T_0$ 是 $\mathscr E_0$ 上的真实压缩算子，这个取值仍在同一返回空间。设
$$
A_0=\sum_{k<h}|q_k|\delta^k;
$$
则 $\|e_n^{\,q}\|\le A_0\|e_n\|$。在 (2.1) 中使用此测试，得到
$$
\widehat e_n^{\,q}
=P_{\widehat{\mathscr E}}K^{-*}q_h(-T_0)^*e_n
\in\widehat{\mathscr E}_0,
$$
以及
$$
\boxed{
\begin{aligned}
&\left|
\left\langle\mathcal Rr_n^C,q_h(-T_0)^*e_n\right\rangle
-
\left\langle\widehat{\mathcal R}(gr_n^C),
\widehat e_n^{\,q}\right\rangle
\right|\\
&\qquad\le
\mathcal C_0^2A_0\alpha(r_n^C)\|e_n\|
\le\frac{\mathcal C_0^2A_0}{2}\|Y_n\|^2.
\end{aligned}
}
\tag{4.1}
$$
原 divided-difference 已付的
$A_{\rm drv}\alpha(r_n^C)\|e_n\|$
可以与 (4.1) 同窗相加。两项都没有要求 $H-B$ 的独立范数上界。

(4.1) 准确运输了原尚未付的主配对，而不是一个任意模型中的自由返回测试。

## 5. 仍未完成的比较

本文真正新增的预算是 (2.5)、(3.2)--(3.5) 与 (4.1)：原正主配对可转到 $\widehat C=\psi_m(C)/d_0$ 的完整返回系统，且转换误差由同一实际未来平方和支付。整个左前缀没有经过大范数相似。

剩下的量仍是
$$
\left\langle\widehat{\mathcal R}(gr_n^C),
P_{\widehat{\mathscr E}}K^{-*}q_h(-T_0)^*e_n\right\rangle.
$$
若随后接[保强孔的规约](R271-appendix-strong-hole-diagonal-linearization-vacuum-forcing-and-full-green-schur.md)，必须区分两个完整算子身份：纯头孔数变换 $W=\omega(B_m)^{N_s}$ 给的是 $C=W L\omega(B_m)W^{-1}$；对于本稿的 $\widehat C$，准确相似为 $\widehat C=V_0LV_0^{-1}$，其中 $V_0$ 是该稿第5节的完整 Artin 变换。$V_0$ 与 $W$ 只在 $\ker L$ 上相等，不能在全部返回链中互换。无论使用哪一个身份，都必须保留其完整物理度量、真实单位因子和本稿的逆伴随测试。不能把它替换成任意小的真空列，也不能由原右域运输常数推出高孔幂预算。

普通右封口、这个返回主配对及原 $N=M$ 仍未完成。
