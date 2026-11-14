# R119 续篇：精确两相位曲线上的完整高振荡两态正型

2026-11-14，visible-exact / tail_connector。

**状态：已证明的径向两端口结论。** 本篇把
[第三相位与局部曲线](R119-supplement-exact-third-phase-kernel-and-local-two-phase-curve.md)
的正系数接到真实有限频率方程，而非把形式渐近系数当成正定矩阵。
同一条实际曲线对全部
$$
 \kappa=M^2/B,\qquad \sqrt\kappa\ge 2^{1600}\rho^{-10},
 \qquad \rho=2^{-40}J^{-2}
 \tag{O.1}
$$
给完整两个状态的正型。阈值是
$\kappa\ge2^{4000}J^{40}$，没有新增 $B$ 或 $\delta^{-1}$ 的幂。
负窗的真实径向两端口、全部径向 Fourier 混合及原单位有限参数
半径都在结论内。实际非径向近核的端角响应、两列 $\Gamma^*$
和三段外反馈仍须另付，本文末节明确保留。

本文使用第三相位篇已经勘误的单位：
$\mathsf C_2=(\beta_\Xi-\beta_0)/\sqrt B$。
物理 $M$ 第一相位的改变量是
$4\sqrt B\,\mathsf C_2/M=4\mathsf C_2/\sqrt\kappa$。
所有以下展开均使用 $k=\sqrt\kappa$。

## 1. 原同一曲线和三个准确积分

保持第三相位篇 (T.1)--(T.37) 的全部对象。为避免混淆，
物理径向坐标记作 $t_{\rm ph}$，曲线参数记作 $\alpha$：
$$
 \Xi_\alpha=\alpha\psi+z_-(\alpha)\eta_-+z_+(\alpha)\eta_+,
 \quad |\alpha|\le r_0,\quad
 r_0=2^{-1000}\rho^{13},
 \quad \mathsf C(\Xi_\alpha)=0 .
 \tag{O.2}
$$
这是同一原 $C_x^4$ 曲线，未放大其实际参数盒。
$\psi$ 支持于 $[c-\rho,c+\rho]$，两补偿列支持于
$c\pm4\rho$ 的半径 $\rho$ 区间。置
$$
 x_L=c-6\rho,\quad x_R=c+6\rho,\quad
 F_\alpha=f+7e-\tau\Xi_\alpha',\quad
 e=B^{-1},\quad \tau=\Delta^{-1},\quad
 dt_{\rm ph}=(\Delta/B)\,dx .
 \tag{O.3}
$$
实际 $e>0$、$80<\Delta<3J$ 均保留。记
$$
 V_\alpha(x)=
 -\frac{(F_\alpha+e)^2}{4F_\alpha}
 +\frac{\tau F_\alpha'}{2F_\alpha}
 -\frac{\tau^2F_\alpha''}{4F_\alpha^2}
 +\frac{5\tau^2(F_\alpha')^2}{16F_\alpha^3}.
 \tag{O.4}
$$

光学坐标及端长度是
$$
 s_\alpha(x)=\Delta\int_{x_L}^{x}\sqrt{F_\alpha(y)}\,dy,
 \qquad S_\alpha=s_\alpha(x_R).
 \tag{O.5}
$$
由第54束 (H.7)，完整相位差准确为
$$
 \mathsf C_1(\Xi_\alpha)=-2(S_\alpha-S_0),\qquad
 \mathsf C_2(\Xi_\alpha)
 =-\frac14\left(\int_0^{S_\alpha}\overline V_\alpha\,ds
                         -\int_0^{S_0}\overline V_0\,ds\right),
 \tag{O.6}
$$
其中 $\overline V_\alpha(s)=V_\alpha(x_\alpha(s))$。
第二式不是一次渐近近似：把 (O.4) 乘 $\sqrt F$ 积分，
$F'/\sqrt F$ 是端项，另用
$$
 \int F''F^{-3/2}\,dx
   =[F'F^{-3/2}]+\frac32\int(F')^2F^{-5/2}\,dx .
$$
所有端项在 $\alpha$ 差分中准确相消，得到的正是
$\Delta F_e(F)/16+(F')^2F^{-5/2}/(64\Delta)$。

因此 $S_\alpha=S$ 固定，且
$$
 \int_0^S\dot{\overline V}_\alpha\,ds=0,\qquad
 \frac12\int_0^S\overline V_\alpha\dot{\overline V}_\alpha\,ds
                  =\frac{d}{d\alpha}\mathcal C_3(\Xi_\alpha)>d/2,
 \quad d=2^{-789}\rho^7 .
 \tag{O.7}
$$
点号在固定 $s$ 上取 $\alpha$ 导数。
因三个支集远离 $x_L,x_R$，$F_\alpha$ 及所有所需 jets
在两端邻域不变。$S_\alpha$ 的准确恒定进一步说明
$x_\alpha(s)$ 在两个端邻域都不变。因此
$\dot{\overline V}_\alpha$ 在固定区间 $(0,S)$ 内紧支，
其下文所有分部端项均为零。

## 2. 全部实际高阶 jet 费用

这一节仅延长同一显式紧支函数的有限 jets，不对真实解
假定复径向延拓。原第67束 (F.15) 的证明给相位算子系数
$$
 |b_\nu^{(l)}|\le l!\,2^{82l+97},\qquad \nu=0,1.
 \tag{O.8}
$$
该式来自已付半径 $2^{-82}$ 的明确多项式商，故也适用于
$l=6,7,8$。两系数在 $0\le l\le8$ 的和小于 $2^{770}$。
对 $P(y)=(1-y^2)^{14}$，其系数绝对和是 $2^{14}$、次数28，
故 $0\le l\le9$ 有
$$
 \sup_{|y|\le1}|P^{(l)}(y)|
       \le2^{14}28^l<2^{64}.
 \tag{O.9}
$$
原 $F^{9/2}$ 在各实点半径 $2^{-8}$ 的复盘上可取
$1<|F|<3$，由 quartic 的四个原导数界直接验证；
其 $0$--$7$ 阶实 jet 均小于 $2^{80}$。
对
$\psi=2^{-700}F^{9/2}\{f_\rho''-b_1f_\rho'
 +(b_0-b_1')f_\rho\}$ 逐项用 Leibniz，
至多四个有限和及其组合系数小于 $2^{12}$。
保留每一项的 $\rho$ 幂，得到
$$
 |\psi^{(l)}|<2^{256}\rho^{4-l},\qquad
 |\eta_\pm^{(l)}|<2^{-16}\rho^{4-l},
                          \quad 0\le l\le7 .
 \tag{O.10}
$$
例如最宽的 bits 是 $-700+80+770+64+12=226<256$；
较低阶项多出的正 $\rho$ 幂只会改善此界。
原多项式在端点的14阶零也保证这些延零 jets 连续。

由原 $|z'|\le H_0|\alpha|$、
$|z|\le H_0\alpha^2$ 和 $H_0r_0=2^{-872}\rho^7<1$，
$$
 |\partial_x^l\dot\Xi_\alpha|
       <2^{257}\rho^{4-l},\qquad
 |\partial_x^l\Xi_\alpha|
       <2^{257}r_0\rho^{4-l}
        =2^{-743}\rho^{17-l},\quad 0\le l\le7 .
 \tag{O.11}
$$
于是整个实曲线满足
$$
 3/2<F_\alpha<2,\qquad
 \max_{0\le l\le6}|\partial_x^lF_\alpha|<2^{10},
 \qquad S<2^7J\rho<1 .
 \tag{O.12}
$$
这里 $7/4<f+7e<31/16$ 留有真实余量；原四阶最大值720，
五、六阶仅来自 (O.11)。

以下给宽但明确的链式费用，供独立消费。把每点的六阶 Taylor
jet 当成多项式，在 $|z|\le2^{-14}$ 上其非恒定部分小于 $1/8$。
对指数
$-4,-3,-2,-1,-1/2,1/2,1/4$，正实分支的模小于 $2^8$，
因此在 $l\le6$ 范围
$$
 |\partial_x^l F_\alpha^a|<l!\,2^{14l+8}.
 \tag{O.13}
$$
这是有限链式法则的证明，不是对仅有有限正则性的曲线
作解析延拓断言。展开 (O.4) 为
$$
 -\tfrac14(F+2e+e^2/F)
   +\tfrac{\tau}{2}F'/F
   -\tfrac{\tau^2}{4}F''/F^2
   +\tfrac{5\tau^2}{16}(F')^2/F^3 .
$$
其 $0$--$3$ 阶 $x$ jets 小于 $2^{80}$，$0$--$4$ 阶小于
$2^{100}$：最后一项最宽的 bits 分别小于
$5+20+53=78$ 和 $7+20+69=96$，其余项和仍有余量。

令 $a_s=\tau F^{-1/2}$，则
$|a_s|<1$、$|a_s'|<2^{10}$、$|a_s''|<2^{22}$。
把 $(a_s\partial_x)^l$ 展开到 $l=3$，系数和小于 $2^{24}$，
故
$$
 1+\|\overline V_\alpha\|_{W^{3,\infty}(0,S)}
                                  < A:=2^{128}.
 \tag{O.14}
$$
这里各阶范数取和；常数仍覆盖四项之和。

还须支付固定光学坐标的参数导数，不能只取固定 $x$ 导数。
令 $\Psi=\dot\Xi_\alpha$，则
$$
 \dot F=-\tau\Psi',\quad
 \dot s(x)=-\frac12\int_{x_L}^xF^{-1/2}\Psi'\,dy,\quad
 \dot x(s)=-\tau F^{-1/2}\dot s(x).
 \tag{O.15}
$$
(O.10)--(O.13) 给
$|\partial_x^l\dot s|<2^{304}\rho^{4-l}$、
$|\partial_x^l\dot x|<2^{360}\tau\rho^{4-l}$，
$0\le l\le3$。第一个 $l=0$ 界使用完整长度 $12\rho$；
其它界为明确积分的一至三次微分。
直接变分 (O.4)，七个乘积项分别包含一个 $\dot F,\dot F'$
或 $\dot F''$；再取最多三次 $x$ 导数时，
(O.11) 给的最差项是 $2^{257}\rho^{-2}$。
乘积的组合系数不超过 $4^3$，
另外最多两项 $F'$ 因子和一个倒数 jet，故
$$
 \max_{l\le3}|\partial_x^l(\dot V|_x)|
                                      <2^{352}\rho^{-2}.
$$
固定 $s$ 上的准确导数为
$\dot{\overline V}=(\dot V|_x)+V_x\dot x$。
用 $V$ 的四阶界及 (O.15)，其三阶 $x$ jets 小于
$2^{465}\rho^{-2}$；再用同一个 $a_s\partial_x$ 展开，
全部三阶 $s$ jets 小于 $2^{490}\rho^{-2}$。
最后由 $S<1$ 得
$$
 \|\dot{\overline V}_\alpha\|_{W^{3,1}(0,S)}
                          < H:=2^{512}\rho^{-3}.
 \tag{O.16}
$$
所有 $\Delta$ 因子已在 (O.15) 抵消或留下有利的 $\tau$。
(O.14)--(O.16) 均无隐藏 $B$ 或频率常数。

## 3. 一个完整两行的有限频率引理

本节证明实际使用的初等估计。设 $0<S\le1$，
$V$ 为实 $W^{3,\infty}$ 函数，$v=\dot V$ 紧支且
$W^{3,1}$，并有
$$
 1+\|V\|_{W^{3,\infty}}\le A,\quad
 \|v\|_{W^{3,1}}\le H,\quad
 \int v=0,\quad \frac12\int Vv>D/2 .
 \tag{O.17}
$$
对 $k\ge2\sqrt A$ 置
$$
 p=(k^2+V)^{1/2},\quad f=p^{-1/2},\quad
 \vartheta(s)=\int_0^sp,\qquad
 \mathcal F=
 \begin{pmatrix}
 f\cos\vartheta&f\sin\vartheta\\
 f'\cos\vartheta-fp\sin\vartheta&
 f'\sin\vartheta+fp\cos\vartheta
 \end{pmatrix}.
 \tag{O.18}
$$
$\det\mathcal F=f^2p=1$ 准确成立。
两列的方程余项是
$$
 y''+(k^2+V)y=E y,\qquad
 E=\frac{f''}{f}
   =-\frac{V''}{4p^2}+\frac{5(V')^2}{16p^4}.
 \tag{O.19}
$$
由 $p^2\ge3k^2/4$（下文只用 $p\ge k/\sqrt2$）、
$A/k^2\le1/4$，有 $|E|<A/k^2$。

令准确齐次基本阵为 $\mathcal Y=\mathcal F W$、
$W(0)=I$。代入方程得到
$$
 W'=-E\,\mathcal F^{-1}e_2e_1^T\mathcal F\,W,\qquad
 \|\mathcal F^{-1}e_2e_1^T\mathcal F\|=f^2=1/p .
 \tag{O.20}
$$
因此完整 interaction 满足
$$
 \gamma=\int|E|/p<2A/k^3\le1/4,\qquad
 \|W\|,\|W^{-1}\|<2,\qquad
 \|W-I\|<4A/k^3 .
 \tag{O.21}
$$
这些是两行全矩阵估计；未选择一个 traveling branch。

真实 crossing 在固定左端 $\mathcal F(0)$ 的系数 $c\in\mathbb C^2$
上是 Hermitian 矩阵
$$
 \mathcal L=-\int_0^S v(s)\,
              \mathcal Y(s)^*e_1e_1^T\mathcal Y(s)\,ds .
 \tag{O.22}
$$
先令 $W=I$。$cc^T$ 的三角恒等式说明相应矩阵
$\mathcal L_{\rm app}$ 的标量部分及非标量部分为
$$
 D_k=-\frac12\int v/p,\qquad
 \|\mathcal L_{\rm app}-D_kI\|
       =\frac12\left|\int(v/p)e^{2i\vartheta}\,ds\right|.
 \tag{O.23}
$$
在 $|V|/k^2\le1/4$ 上，
$|(1+z)^{-1/2}-1+z/2|\le2z^2$，所以
$$
 \left|D_k-\frac1{4k^3}\int Vv\right|
                                      \le A^2H/k^5 .
 \tag{O.24}
$$
$\int v=0$ 在这里准确消去第一项。

置 $q=1/p$。直接三次微分给
$\max_{0\le l\le3}|q^{(l)}|\le2/k$；
例如最宽的三阶和由
$22(A/k^2)^3+13(A/k^2)^2+2(A/k^2)<2$
控制。三次分部积分没有端项，并给
$$
 \int qv\,e^{2i\vartheta}
   =\left(-\frac1{2i}\right)^3
       \int \partial_s\{q\partial_s[q\partial_s(q^2v)]\}
                                      e^{2i\vartheta}\,ds .
 \tag{O.25}
$$
展开式最多 $5^3=125$ 个项，每项含四个 $q$ 的有限 jets，
以及 $v$ 的一个至多三阶 jet。因此
$$
 \left|\int qv\,e^{2i\vartheta}\right|
                                  <2^8H/k^4 .
 \tag{O.26}
$$
这明确控制了完整非标量的两个实分量。

再恢复准确 $W$。由 (O.21)，
$\|W^*cc^TW-cc^T\|\le12A/k^3$（这里 $c=(\cos\vartheta,\sin\vartheta)$
是实单位向量），故
$$
 \|\mathcal L-\mathcal L_{\rm app}\|
                                      <24AH/k^4 .
 \tag{O.27}
$$
合并 (O.23)--(O.27)，安全地
$$
 \left\|\mathcal L-
       \frac1{4k^3}\left(\int Vv\right)I\right\|
                              <2^8A^2H/k^4 .
 \tag{O.28}
$$
若
$$
                  k\ge2^{12}A^2H/D ,
 \tag{O.29}
$$
则由 (O.17)
$$
                       \boxed{\mathcal L>D/(8k^3)\,I_2.}
 \tag{O.30}
$$
这是任意复两状态的矩阵正定性，包含两个方向的交叉项。

## 4. 应用于整条有限曲线，及物理 B 因子的准确归属

应用 (O.17) 时取 $D=d$，$V=\overline V_\alpha$、
$v=\dot{\overline V}_\alpha$。由 (O.14)、(O.16)，
$$
 2^{12}A^2H/d
  =2^{1569}\rho^{-10}<2^{1600}\rho^{-10}.
 \tag{O.31}
$$
因此 (O.1) 在全部 $|\alpha|\le r_0$ 同时给 (O.30)。

还须回到原物理单位。径向方程准确为
$$
 (\mu h_{t_{\rm ph}})_{t_{\rm ph}}+M^2\mu Qh=0,\qquad
 \mu_{t_{\rm ph}}/\mu=-1-Q .
$$
令 $u=\sqrt\mu\,h$、
$v_{\rm Sch}=F_\alpha^{1/4}u$。它化为
$v_{{\rm Sch},ss}+(k^2+\overline V_\alpha)v_{\rm Sch}=0$。
原物理作用量和光学作用量之间的系数是 $B$：
$$
 \int\mu(|h_{t_{\rm ph}}|^2-M^2Q|h|^2)\,dt_{\rm ph}
 =B\int(|v_{{\rm Sch},s}|^2
                   -(k^2+\overline V_\alpha)|v_{\rm Sch}|^2)\,ds
                              +\text{固定端项}.
 \tag{O.32}
$$
这可直接以 $dt_{\rm ph}=\Delta\,dx/B$ 验证。
对齐次真实解取参数变分时，内部的解变分项由方程消去，
两个端项因 compact 支集和 (O.6) 而不变。故原完整 profile 核为
$$
 \int\Psi\,\mathcal K_{\rm rad}\,dt_{\rm ph}
    =-B\int\dot{\overline V}_\alpha |v_{\rm Sch}|^2\,ds,
 \quad
 \mathcal K_{\rm rad}
   =\mu\{|h_{t_{\rm ph}}|^2
       -2M^2\operatorname{Re}(\bar h h_{t_{\rm ph}})
       +M^2|h|^2\}.
 \tag{O.33}
$$
$\Psi=\dot\Xi_\alpha$；原两个径向 $\bar\Gamma$ 导数在整条
曲线上准确为零，不另添远端补偿项。

取
$$
 \binom{v_{\rm Sch}}{v_{{\rm Sch},s}}
           =B^{-1/2}\mathcal Y_\alpha(s)c .
 \tag{O.34}
$$
该物理两解的 Wronskian 是1，因为
$\operatorname{Wr}_{t_{\rm ph}}(u_1,u_2)
 =B\operatorname{Wr}_s(v_1,v_2)$。
(O.33) 的 $B$ 与 (O.34) 的 $B^{-1}$ 准确抵消。
用真实盒坐标 $\theta=\alpha/r_0$，得到
$$
 \boxed{\quad
 \mathfrak L_{\theta,M}(c)
       >\frac{r_0d}{8k^3}|c|^2
       =2^{-1792}\rho^{20}\kappa^{-3/2}|c|^2 .
 \quad}
 \tag{O.35}
$$
未把单位形状导数当成有限坐标导数，也未漏掉物理 measure。

## 5. 固定两端口、原中心 wave 与整负窗

在 $x_L,x_R$ 取 (O.18) 的零相位 frame
$$
 F_e^0=\begin{pmatrix}p_e^{-1/2}&0\\
             (p^{-1/2})'_e&p_e^{1/2}\end{pmatrix}.
$$
它们的全部系数对 $\alpha$ 固定。真实 transfer 在这两个
canonical frames 中是 $R_{\vartheta(S)}W(S)$，
所以 norm 及逆 norm 都小于2。
令每端 $\xi_\pm=(q\pm ip)/\sqrt2$，
incoming 为 $(\xi_{L,+},\xi_{R,-})$，
outgoing 为 $(\xi_{L,-},\xi_{R,+})$。
完整两端 scattering $\mathcal S_M$ 是酉矩阵；守恒 Green 型给
$$
 a^*(-i\mathcal S_M^*\partial_\theta\mathcal S_M)a
                              =\mathfrak L_{\theta,M}(c).
 \tag{O.36}
$$
两端的总平方范数是 $2|a|^2$，另一方面不超过
$|c|^2+|Tc|^2<5|c|^2$。因此局部两端口上
$$
                 -i\mathcal S_M^*\partial_\theta\mathcal S_M
                     >\frac{r_0d}{32k^3}I_2 .
 \tag{O.37}
$$
(O.36) 是完整 incoming/outgoing 规范；没有只选一个 Robin
线或把双端解空间压成一个标量。

为接回旧真实中心 wave，在 $x_L$ 置
$$
 Z=(\sqrt{k_c}\,u,u_{t_{\rm ph}}/\sqrt{k_c}),
 \qquad k_c=\sqrt{7M^2-16},\quad 2M<k_c<3M.
$$
由 (O.18)、(O.34) 直接有
$$
 c=\begin{pmatrix}1&0\\a_*&1\end{pmatrix}
           \begin{pmatrix}b_*&0\\0&b_*^{-1}\end{pmatrix}Z,
 \quad
 b_*^2=\frac{Bp\sqrt F}{k_c},\quad
 a_*=\frac{\tau F'}{4F^{3/2}p}+\frac{p'}{2p^2}.
 \tag{O.38}
$$
(O.1)、(O.12)、(O.14) 给
$\sqrt B/(3\sqrt2)<b_*^2<\sqrt B$ 和 $|a_*|<1$。
所以
$$
                  |c|^2>\frac1{4\sqrt B}|Z|^2,\qquad
 \mathfrak L_{\theta,M}
                   >\frac{r_0d B}{32M^3}|Z(x_L)|^2 .
 \tag{O.39}
$$
这里明确付了与原 wave 的 $B^{1/4}$ 条件数，没有把
光学 canonical 单位直接称为原物理中心单位。

第53/54束对整个原 $C^4$ 球重新支付的真实正反向 Cauchy 界是
$$
 K_j=2^{6000}J^8\delta_j^{-16}.
$$
第54束 (H.18)--(H.21) 明确覆盖全部实内部子区间；
本曲线由第三相位篇第8节已逐项重新接入同一球。
从任一内部 $Z$ 到旧两个固定 $Q=7$ wave 端口使用同一个
$K_j$。第67束完整 Green/Cayley 识别因而把
$L\ge d_{\rm loc}|Z|^2$ 送到
$-iS_M^*DS_M\ge d_{\rm loc}/(8K_j^2)$。
此比较只用两端真实迹之和及 Cauchy norm，不需要单侧质量下界。
代入 (O.39) 并安全放宽得整个真实径向负窗
$$
 \boxed{\quad
 -iS_M^*\partial_\theta S_M
       >2^{-1800}\rho^{20}B K_j^{-2}M^{-3}I_2 .
 \quad}
 \tag{O.40}
$$
原常数 $K_j$ 若用于其它端规范，须先保留原准确转换，
不能直接把 (O.40) 声称为任何未经消费的全网归一。

## 6. 同一方向的径向混频结论与全部源

(O.2) 不依赖 $M$。对任何有限频带
$$
 U/2\le |m|\le U,\qquad (U/2)^2/B\ge2^{4000}J^{40},
$$
径向 Fourier 正交性使 (O.40) 对完整两锥、多模两态同时成立：
$$
 \sum_m a_m^*(-iS_m^*\partial_\theta S_m)a_m
      >2^{-1800}\rho^{20}B K_j^{-2}U^{-3}
                                  \sum_m|a_m|^2 .
 \tag{O.41}
$$
更一般的无限和在右侧 $|m|^{-3}$ 加权形式域内成立。
这里没有每模式参数、没有除以 band 模数；一个真实有限参数
沿整条曲线共同控制所有这些径向频率。
这仍是径向正交分解，未删除实际非径向交叉项后给它改名。

源保持完整。为明确原物理与光学两行的关系，令
$Y=(h,\pi)$ 是总 conormal 状态，并置
$$
 u=\sqrt\mu h,\qquad
 p_u=\pi/\sqrt\mu-(1+Q)u/2,
$$
$$
 X=T_\alpha Y=
 \binom{\sqrt B\,F^{1/4}u}
 {B^{-1/2}F^{-1/4}p_u+
                    \sqrt B\,\tau F' u/(4F^{5/4})}.
 \tag{O.42}
$$
$\det T_\alpha=1$，且对齐次解 $X=(\sqrt B\,v_{\rm Sch},
\sqrt B\,v_{{\rm Sch},s})$。
若原材料坐标中 $Y_{t_{\rm ph}}=A_{\rm ph}Y+\mathbf s$，
则准确的全仿射系统是
$$
 X_s=\begin{pmatrix}0&1\\-(k^2+\overline V_\alpha)&0\end{pmatrix}X
             +\sigma,\qquad
 \sigma=(B\sqrt F)^{-1}T_\alpha\mathbf s .
 \tag{O.43}
$$
原普通/weak 源两行
$\mathbf s=(-\mu^{-1}F^t,\ g-\partial_\theta F^\theta)$
均被这一个完整矩阵作用，特别第一 weak 源不被误当成
只出现在 Schr 方程右侧的普通函数。
准确解含全部有序 Duhamel 项
$\int U(s,\zeta)\sigma(\zeta)\,d\zeta$；
本文的齐次正定性没有删掉这个仿射列。

参数导数和粗 weak 数据仍在原材料坐标中按第61束
$\widehat{\mathbf s}=\dot{\mathbf s}-\Psi\mathsf B\mathbf s$
及完整 Piola/normal-shear 公式消费。
不能为了固定 $s$ 而对一个粗 $F^t$ 擅自取径向导数；
(O.43) 是合法 pullback，若用分布源则保持其弱式。
裸通量的 $F^t$ 端迹仍由原输入空间提供。

$M=0$ 不在 (O.1) 内，不能把它代入 $k^{-1}$ frame。
独立 mean 仍满足
$(\pi_0)_{t_{\rm ph}}=g_0$、
$(h_0)_{t_{\rm ph}}=\mu^{-1}(\pi_0-F_0^t)$。
物理常高度是准确 null；flux mean 的真实响应没有被赋予
(O.40) 的高频下界，也未从全网源空间移除。

## 7. 消费范围与真正剩余量词

本篇关闭的是高 $\kappa$ 的有限频率两态余项：
第三系数给出的正方向，经过真实 fixed-length 方程、全部
振荡非标量项及全 interaction 后，仍在整个实际参数盒
给 (O.40)。剩余区间
$$
                         1/4\le\kappa<2^{4000}J^{40}
$$
只随 $J$ 增长；不能用低锥定理跨过已经证实的
$\kappa\in[3/4,1]$ 反例。它需用真实五函数可观测性或另一个
实际方向处理，并重付其有限盒。

在非径向对象上，$\Gamma^*(a,\Omega)$ 的两个参数导数并非零。
径向 $\bar\Gamma$ 的零导数只意味着 joint 方程的径向参考列
准确为零；实际响应仍应由完整 joint 方程求解。
端角图的参数导数、三个相邻区间的背景响应和 source-to-label
权也尚未由 (O.40) 支付。

特别若把完整酉 return $U$ 改写成
$\widetilde U=V^*UV$，令 $A=-iV^*V'$，则
$$
 -i\widetilde U^*\widetilde U'
   =V^*(-iU^*U')V+A-\widetilde U^*A\widetilde U .
$$
对 $r=(I-\widetilde U)x$，附加配对准确为
$2\operatorname{Re}\langle r,Ax\rangle-\langle r,Ar\rangle$。
这是后续 near-kernel 的可用消项；使用时仍须付真实 domain
和全残差，不能把端图导数直接设成零。
非酉 physical symplectic ports 则应使用原 Green 边界恒等式。

所有以上是显式解析证明；本篇没有运行新数值实验，
也没有把任何未运行的整数门标记为已通过。
