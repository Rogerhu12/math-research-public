# R119：实际末端 connector 上的全标签精确延拓和完整两迹

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇把 R115 的同一个全标签精确无限尾，向外延到 R69
已经安装的**整个末端组**：从放大段的 $q=2$ 末端开始，依次经过
$2\to-1$ 短过渡、真实停止的 $q=-1$ 主段和 $-1\to-8$ 末端短过渡。
没有添加一个未安装的 cut128 平台，没有改变该处目标度量，也没有只传有限
低模。全部高标签、全部高输出、mean 和 holonomy 均保留。

这里得到的是精确尾及该有限组的全频两迹参数化。**尚未得到**前方整个
$q=2$ 放大段、两个 bump、长径向段直至 $r=25/8$ 的非线性高输入图逆；
也不将本篇的前向延拓当成 regular 端口的同宽 Robin 微扰定理。

## 1. 同一实际几何，准确时间和角宽

使用 [R69 §§4–5](R69-actual-closed-approximate-exterior-and-two-held-disks.md)、
[R11 §5](R11-matched-mode-four-physical-tail-connector.md) 和
[R115](R115-actual-tail-holomorphic-neighborhood-and-strong-extension.md)。
完整尾来源仍为 quantitative-newton-twist-flex 的
[R72](../../quantitative-newton-twist-flex/results/R72-large-width-inner-tail-to-cut128.md)
及 [R25](../../quantitative-newton-twist-flex/results/R25-relative-material-ball-and-early-gates.md)；
所用源 blob 与 R115 §1 相同。

记真实末端物理半径为 $a_e=\rho_*b$，$1<b<2$，并令
$$
 \delta=\frac2{25}2^{-128}<2^{-131},\qquad
 w_c=\epsilon\delta^6/b^7,\qquad
 \zeta=\epsilon\delta^{39/4},\qquad
 s_*:=\frac{\zeta}{w_c}=b^7\delta^{15/4}<2^{-484}.
 \tag{119.1}
$$
$\rho_*,\epsilon$ 是 R69 的真实缩放，不改变它们。
本篇参考半径为 $r=a/\rho_*$，向外回走的时间为
$$
 t=\log(r/b)=v_e-v.
 \tag{119.2}
$$
R69 的原顺向坐标 $v=\log h$ 在这里反向。令 $\eta=2^{-24}$，
$S(x)=10x^3-15x^4+6x^5$。最靠 cut128 的那一段准确定义为
$$
 q(t)=-8+7S(t/\eta),\qquad 0\le t\le\eta .
 \tag{119.3}
$$
这是原 $-1\to-8$ quintic 的反向，利用了 $S(1-x)=1-S(x)$。
再向外是同一个、由 R11 真横截根定义的 $q=-1$ 主段，最后是原
$2\to-1$ quintic 的反向。其终端记为 $t=L$。R11 (5.2)–(5.5) 给
$$
 0<L<\log(9/8)+2\eta<\frac18,
 \qquad -8\le q\le2 .
 \tag{119.4}
$$
最后一个有理界可用
$\log(9/8)<1/8-1/128+1/1536$ 后直接核验。
在这条**已安装**背景上，
$$
 r=be^t,\qquad A(t):=r w_r/w=q(t)+1,\qquad w_t=Aw,
 \tag{119.5}
$$
故
$$
 1<r<3,\qquad |A|\le7,\qquad |A+1|\le6,
 \qquad \frac13<w/w_c<3,
 \qquad 0<w<1.
 \tag{119.6}
$$
这里 $w$ 是物理高度斜率，亦等于等比缩放前参考高度的斜率。
初值 $w_c$ 和 (119.5) 唯一确定的 $w$ 正是 R69 的轮廓；没有另选
一个相近的 profile。该组的某些段是负曲率或零曲率，本篇不用正帽能量。

所有角宽都是**原物理角 $\theta$** 的 Wiener 宽度，频率为 $4\mathbb Z$。
准确预算如下：

| 用途 | 角宽 |
|---|---:|
| R72/R115 原 cut128 状态 | $\tau=5177/400=12.9425$ |
| 转相对一阶状态后的起始宽度 | $\sigma_0=\tau-9/1600=12.936875$ |
| 整个末端组上的能源宽度 | $\sigma_1(t)=\sigma_0-16t>\tau-2-9/1600$ |
| 二次余项的工作宽度 | $\sigma_2(t)=\sigma_1(t)-1/4$ |
| 完整 raw 两迹输出 | $\sigma_{out}=\tau-3=9.9425$ |
| 完整 grounded 两迹输出 | $\sigma_g=\tau-4=8.9425$ |

特别 $\sigma_2(L)-\sigma_{out}>1/2$。这些宽度均小于已有输入宽度，
没有重调 R72 的绝对角宽或调用一个更宽标签球。后续若转入有限正帽的
物理 $1/512$ 条带，可以直接限制到它；真正跨过本篇外端之后的有限
传播仍须另付，不能用这个限制代替。

## 2. 实际完整相对方程

先以正参考高度 $z=h+u$ 写方程，$h_r=w$；北帽的真实高度是
$Z=Z_0-\rho_*u$。记
$$
 P=\frac{u_\theta}{rw},\qquad K=\frac{u_r}{w},\qquad
 U=P_\theta,\quad V=K_\theta,
 \qquad E=1+w^2 .
 \tag{119.7}
$$
由源 R72 (2.4)，准确的全频方程是
$$
 \begin{split}
 P_t&=V-(A+1)P,\\
 K_t&=F_t(P,K,U,V),
 \end{split}
 \tag{119.8}
$$
其中
$$
 F_t=
 \frac{-A(2K+U+K^2+KU+w^2P^2)+E(V-P)^2}
      {1+K+EU}.
 \tag{119.9}
$$
导出时先代 $p=wP,\ \kappa=wK$，并同时微分 $w_t=Aw$；遗漏这项会
把线性式 $-A(2K+U)$ 错写为 $-A(K+U)$。完整差额恰为
$$
 F_t+A(2K+U)=
 \frac{E(V-P)^2+A\{K^2+2EKU+EU^2-w^2P^2\}}
      {1+K+EU}.
 \tag{119.10}
$$
相邻程序以独立整数多项式相减核这两个恒等式。

对四分量使用和范数
$$
 N_\sigma=\|P\|_\sigma+\|K\|_\sigma+
                 \|U\|_\sigma+\|V\|_\sigma,
 \qquad \|f\|_\sigma=\sum_{m\in4\mathbb Z}e^{\sigma|m|}|f_m|.
 \tag{119.11}
$$
mean 包括在 $K$ 中。若 $N_\sigma\le1/64$，则分母的逆 norm 不超过
$32/31$。逐项使用 Banach 代数和正系数逆级数，得到
$$
 \|F_t\|_\sigma\le15N_\sigma,
 \quad \|F_P\|_\sigma\le19N_\sigma,
 \quad \|F_K\|_\sigma<15,
 \quad \|F_U\|_\sigma<8,
 \quad \|F_V\|_\sigma\le5N_\sigma .
 \tag{119.12}
$$
例如在 $n=1/64$，这五个估计依次由
$$
 \frac{14+9n}{1-2n}<15,\quad
 \frac{18}{1-2n}<19,\quad
 \frac{14+14n+15n}{1-2n}<15,
 \quad \frac{7(1+n)+30n}{1-2n}<8,
 \quad \frac4{1-2n}<5
 \tag{119.13}
$$
给出。式中 $F_K,F_U$ 的分式已包含微分分母的项。
由于
$$
 U_t=V_\theta-(A+1)U,
 \qquad
 V_t=F_PU+F_KV+F_UU_\theta+F_VV_\theta,
 \tag{119.14}
$$
有移动角宽能源不等式
$$
 \frac{d^+}{dt}N_{\sigma(t)}
 \le32N_{\sigma(t)}+
       (8+\sigma'(t))\sum_m |m|e^{\sigma(t)|m|}
          (|P_m|+|K_m|+|U_m|+|V_m|).
 \tag{119.15}
$$
零阶项逐列总系数可取 $21,15,21+19/64,31$，均小于32；角导项
只有 $8\|D U\|+(1+5/64)\|D V\|$，被 $8\|D(P,K,U,V)\|$ 控制。
这说明16是一个明确充分的角宽下降速率，不是未给出的 CK 常数。

### 全频存在和唯一性

先将 (119.8) 的右侧作 Fourier 投影，初始数据也投影，令
$U=P_\theta,V=K_\theta$。这只是全方程的逼近方案；**不声称**该有限
方案逐项保存 holonomy，也不把它的逐点逆说成源 R72 的压缩逆。
有限 ODE 的复解析右侧在 $N<1/64$ 合法，且 (119.15) 与截断无关。
在 $\sigma_1(t)=\sigma_0-16t$ 上，
$$
 N_{\sigma_1(t)}\le e^{32t}N_{\sigma_0}(0)<64N_{\sigma_0}(0).
 \tag{119.16}
$$
在任何严格较窄条带，统一 Fourier 尾和全部所需角导由一个正宽度差
给出；右侧与时间导数也一致有界。有限 ODE 因而在较窄条带有局部一致
收敛子列，极限解完整 (119.8)。初始 $U=P_\theta,V=K_\theta$ 的关系
由极限保持。对两解相减，在再缩窄的固定条带，系数差乘背景角导是
有界零阶项，主角导项仍可由同一个负宽度导数吸收；Gronwall 给唯一性。
于是所有截断收敛至同一解。逼近残差在严格较窄条带有一致指数尾，
同样的差分估计给标签复球上的局部一致收敛，所以解对标签全纯。
这一论证只使用实际连续 $A(t),w(t)$，不要求跨 quintic 接缝的径向解析性。

## 3. 原全标签球真实进入这个存在域

保留 R115 的整个复标签球 $\|a\|<1/4$。其真实强状态满足
$$
 \|X(a)\|_{\mathcal X}<\frac{13}{4}\|a\|<1,
 \qquad
 \|X(a)-\mathcal H a\|\le\kappa\|X(a)\|^2,
 \qquad \kappa<2^{-60}.
 \tag{119.17}
$$
这来自同一固定点，而不是把 $1/12$ 球任意延长。

置 $d=9/400$。源 R72 (11.9) 的推导只使用完整 cut128 状态，故对
所有内部标签而非仅最低模有
$$
 \mathcal R_0
 \le12b^{10}\delta^{15/4}(e,d/4)^{-1}\|X(a)\|
 <2^{14}s_*\|X(a)\|.
 \tag{119.18}
$$
这里 $12b^3(e,d/4)^{-1}<96(800/9)<2^{14}$。
$\mathcal R_0$ 是源 R25 (2.1) 的五项非mean相对和。完整 mean 小根
$|K_0|\le12\mathcal R_0^2$ 已包含；因此
$$
 N_{\sigma_0}(0)\le2\mathcal R_0+12\mathcal R_0^2
 <2^{16}s_*\|X(a)\|.
 \tag{119.19}
$$
由于 $V=(K_\theta-P)+P$，这一步没有遗漏 $K_\theta$。
结合 (119.16)，在整个真实组上
$$
 \boxed{\quad
 N_{\sigma_1(t)}(t)<2^{22}s_*\|X(a)\|<2^{-462}.
 \quad}                                                     \tag{119.20}
$$
它严格留在复 $1/64$ 球，完成了存在域的自洽检验。
所有高标签与所有高输出都在这个同一和范数中。

## 4. 完整 mean、水平重建及与原尾的 $C^2$ 接合

在 cut128 先以一个整体高度平移规范 $u_0$ 的角平均为0，平盘的高度
则是输出；另保留独立的物理平移参数 $\lambda$。
令
$$
 u(t,\theta)=u(0,\theta)+\int_0^t r(s)w(s)K(s,\theta)\,ds.
 \tag{119.21}
$$
由 (119.8) 有 $(rwP)_t=rwK_\theta$，所以原始关系
$u_\theta=rwP$ 在全过程保持，角平均未被重置。

仍记 $k=w(1+K),\ p=wP,\ D=E-k^2-Ep^2,\ \mathsf t=1-p^2$。
准确连接为
$$
 G=\alpha_\theta=
 \frac{1+kp_\theta/\mathsf t}{\sqrt D},\qquad
 M=\langle G\rangle.
 \tag{119.22}
$$
源 R72 (2.6) 是全频恒等式；(119.8) 的零 residual 给 $M_t=0$。
因此 $M\equiv1$，其 mean 径向迹始终是同一个 holonomy-one 小根。
对真实标签，正性余量由 (119.20) 给
$$
 D>1-2^{-460},\quad \mathsf t>1-2^{-920},\quad
 k+Ep_\theta=w(1+K+EU)>\tfrac12w.
 \tag{119.23}
$$
不会在本段遇到改变小根分支的问题。

采用 R115 (115.16)–(115.19) 的同一水平重建：
$$
 l=r\sqrt{\mathsf t},\quad a_1=-kp/\sqrt{\mathsf t},\quad
 b_1=\sqrt{D/\mathsf t},\quad
 \gamma=\partial_\theta^{-1}(G-1),
$$
$$
 (\partial_\theta+i)R_h=i l e^{i\gamma},\qquad
 (R_h)_r=e^{i\gamma}(b_1+i a_1).
 \tag{119.24}
$$
$R_h$ 是旋转基中的水平坐标。实反射和四重旋转由唯一性保持；
$\partial_\theta^{-1}$ 的零平均规范与原尾相同，四重旋转使水平平移
周期准确为0。完整 Darboux 方程保证该 coframe 的径向与角向导数相容。
故所得 $F_a$ 在本组上**精确**诱导原旋转度量
$(1+w^2)dr^2+r^2d\theta^2$，并与原 tail chart 的完整向量及一阶迹相同。

接缝处 $w,w_r$ 是同一真实背景；(119.9) 的分母不为0，故二阶高度
也相同。式 (119.24) 的一次微分只用高度二阶和背景一阶，给完整向量
二阶 jet 匹配。这样接上的是真 $C^2$ 精确面，不只是匹配一条线性方向。

若只改变 $\lambda$，完整变化在所有这些地方均准确为 $e_z$；平帽上
其余全部标签方向仍 $C^2$ 为零。上下两份可按 R69 原腰反射安装，
而不是分别选择两个不相关的 mean。

## 5. 完整 raw 两迹，明确二次余项

在 $t=L$，以北帽参考高度扰动 $C_a=-u_a$ 定义输出。
记 $r_L=be^L$，$\nu_m=m^2(m^2-1)/12$。输出 norm 为
$$
 \begin{split}
 \|\mathcal B(a)\|={}&
 \sum_{m\ne0}e^{\sigma_{out}|m|}
 \left(\left|\frac{\nu_m C_{a,m}}{r_L^4\zeta}\right|
 +\left|\frac{C_{a,r,m}/r_L^3-m^2C_{a,m}/r_L^4}
                    {\sqrt{12}\zeta}\right|\right)\\
 &+|C_{a,0}|/\zeta+|C_{a,r,0}|/\zeta.
 \end{split}                                                \tag{119.25}
$$
它保留全部高输出及 mean 两行。改变整体高度常数的独立列另列，不把
它乘以非零模的 $\nu_m$。

由初始 $\nu_m\ge20$、$b^4<16$，
$\|u(0)\|_{\sigma_0}<\zeta\|X\|$。
(119.20)–(119.21)、$r<3,w<3w_c,L<1/8$ 给
$$
 \|u(t)\|_{\sigma_1(t)},\quad
 \|u_r(t)\|_{\sigma_1(t)}<2^{24}\zeta\|X\|.
 \tag{119.26}
$$
在超过 $1/2$ 的余宽上，$\|D^4f\|\le2^8\|f\|$、
$\|D^2f\|\le4\|f\|$。因此
$$
 \|\mathcal B(a)\|<2^{35}\|a\|.
 \tag{119.27}
$$
粗常数不要求切口的任何高度模非零，故没有在高模除以未知高度。

现在令 $\mathcal L a=D\mathcal B(0)a$，即真实线性尾 $\mathcal H a$
经同一已安装末端组传播的完整两迹。则
$$
 \boxed{\quad
 \|\mathcal B(a)-\mathcal L a\|
 <2^{-22}\|a\|^2,\qquad \|a\|<1/4.
 \quad}                                                     \tag{119.28}
$$
下面给完整余项账。由 (119.10)，
$\|F_t+A(2K+U)\|_{\sigma_1}\le32N_{\sigma_1}^2$。
降宽 $1/4$ 后连同其角导的四状态源 norm 小于 $2^7N_{\sigma_1}^2$。
线性四状态传播在同一移动宽度上 norm 至多64，因此 Duhamel 非线性
响应至多 $2^{54}s_*^2\|X\|^2$。

初始非mean余项由 (119.17) 与线性切口换算至多
$2^{16}\kappa s_*\|X\|^2$。完整 mean 初始值至多
$12(2^{14}s_*\|X\|)^2<2^{32}s_*^2\|X\|^2$，没有删掉。
传播后与 Duhamel 相加，在 $\sigma_2(t)$ 得
$$
 \|(P,K,U,V)-(P,K,U,V)^{\rm lin}\|_{\sigma_2(t)}
 <\{2^{22}\kappa s_*+2^{55}s_*^2\}\|X\|^2
 <2^{-37}s_*\|X\|^2.
 \tag{119.29}
$$
初始高度余项小于 $\kappa\zeta\|X\|^2$。再次积分 (119.21) 后，
高度及径向导余项都小于 $2^{-35}\zeta\|X\|^2$。
取 (119.25) 两迹及 mean，支付刚才的四阶角费用，合计小于
$2^{-26}\|X\|^2<2^{-22}\|a\|^2$。这就是 (119.28)，未把线性尾的
已知极小差额误当成全段的非线性余项。

在 $\|a\|\le1/12$ 上，完整全纯输出因而还满足
$$
 \|D\mathcal B(a)-\mathcal L\|<2^{-20}\|a\|,
 \qquad \|D^2\mathcal B(a)\|<2^{-18}.
 \tag{119.30}
$$
第一式用半径 $\|a\|$ 的方向圆盘；第二式用两个半径 $1/24$ 的圆盘，
其总输入仍在 $1/6<1/4$ 球内。每个估计对**所有**标签方向成立。

## 6. 实际 normal/grounded 动量，全部高模和 mean

下面只处理真实 Jacobi 方向 $\dot F=D_aF[b]$；不用基态公式替代更新后
几何。在参考半径 $r_L$，记其北帽参考高度两迹为 $C,C_r$，并令
$\dot k=-C_r,\ \dot p=-C_\theta/r$。准确变分为
$$
 \dot l=-rp\dot p/\sqrt{\mathsf t},\quad
 \dot a_1=-p\dot k/\sqrt{\mathsf t}-k\dot p/\mathsf t^{3/2},\quad
 \dot b_1=-k\dot k/(b_1\mathsf t)-k^2p\dot p/(b_1\mathsf t^2),
 \tag{119.31}
$$
$$
 \begin{split}
 \dot G={}&D^{-1/2}
 \left[\frac{\dot k p_\theta+k\dot p_\theta}{\mathsf t}
       +\frac{2kp_\theta p\dot p}{\mathsf t^2}\right]\\
 &+(1+kp_\theta/\mathsf t)D^{-3/2}(k\dot k+Ep\dot p).
 \end{split}                                                \tag{119.32}
$$
$\langle\dot G\rangle=0$ 是对 $M\equiv1$ 微分的结果；它保留真实 mean
径向迹。取 $\dot\gamma=\partial_\theta^{-1}\dot G$，则
$$
 (\partial_\theta+i)V_h=e^{i\gamma}(i\dot l-l\dot\gamma),\qquad
 (V_h)_r=e^{i\gamma}
    [\dot b_1+i\dot a_1+i(b_1+i a_1)\dot\gamma].
 \tag{119.33}
$$
$V_h$ 是物理水平变化除以 $\rho_*$，旋转基导数已计入。

令 $\mathsf S=F\cdot\nu$、$c=Z^2/\mathsf S^2$、
$c_v=C+(\rho_*/Z)R_h\cdot V_h$。同一 grounded 高度及沿正物理半径的
conormal 准确为
$$
 \boxed{\quad
 \frac{v}{\rho_*}=c_v,\qquad
 \frac{p_{n}}w=
 \frac{c}{\sqrt D}
 \left[\frac{k+Ep_\theta}{Ew}(c_v)_r
       -\frac{\kappa_\theta-p}{rw}(c_v)_\theta\right].
 \quad}                                                     \tag{119.34}
$$
这里 $v=F\cdot\dot F/Z$，$p_{n}$ 是 $Y_z^2\mathsf A\nabla v$ 的真实
密度通量；$\mathsf A=-\operatorname{cof}II/(\zeta_F^2\sqrt{\det g_0})$。
相邻外域的 outward 方向相反，matching 时须翻号。
式 (119.34) 与 R115 补篇 (L.8) 一致，$w$ 取当前切口值而非误用 $w_c$。
$(c_v)_r$ 中保留 $Z_r=-\rho_*k$、$(R_h)_r$ 和 $(V_h)_r$。

这也给一个可直接消费的粗小量门。取
$\|f\|_{\sigma,j}=\sum_m e^{\sigma|m|}(1+|m|)^j|f_m|$。
从 $\sigma_1(L)$ 到 $\sigma_g$ 尚余大于 $1/2$ 的角宽；至八阶的统一
乘数 $17^8<2^{40}$。因而五个背景相对量的加权范数可用
$$
 R_d<2^{-420},\qquad
 I:=\bigl(\|C/\zeta\|_{\sigma_g,8}
          +\|C_r/\zeta\|_{\sigma_g,8}\bigr)<2^{68}\|b\|,
 \qquad
 \eta_g:=\frac{\rho_*rw}{Z}<2^{-782}
 \tag{119.35}
$$
控制。$I$ 用 (119.26) 在标签复球的 Cauchy 导数，$Z>17/20$ 由 R69
及下一节的实际修正界保持；可保留 $|\lambda|\le1/20$。

为明示有限代数费用，在同一加权 Wiener 代数里，(119.31)–(119.34)
给下表；两个旋转分量均计算，点积按真实双线性式。

| 量 | 所列尺度除去后的上界 |
|---|---:|
| $\dot G/(w\zeta I)$、$\dot\gamma/(w\zeta I)$ | $32,64$ |
| $\dot l/(w\zeta I)$ | $4R_d$ |
| $\dot a_1/(w\zeta I)$、$\dot b_1/(w\zeta I)$ | 各 $8$ |
| $V_h/(w\zeta I)$、$(V_h)_r/(w\zeta I)$ | $2^{10},2^{12}$ |
| $(c_v-C)/(\zeta I)$ | $2^{13}\eta_g$ |
| $((c_v)_r-C_r)/(\zeta I)$ | $2^{20}\eta_g$ |
| $(p_{n}/w-C_r)/(\zeta I)$ | $2^{24}(R_d+\eta_g)$ |

例如 $\mathsf S/Z=\sqrt{D/E}(1+\chi)$ 且 $\|\chi\|_{\sigma_g,6}<8\eta_g$。
式 (119.34) 的两个系数分别距 $1,0$ 不超过
$32(R_d+\eta_g),8R_d$。与上表相乘，随后取 (119.25) 的全部角多项式
及 mean 两行，总费小于 $2^{32}(R_d+\eta_g)I$。各项所需角导至多8，
已经在 (119.35) 中，不再隐含一个同宽微分算子。

用 (119.25) 的规范对 grounded 输出 $(v/\rho_*,p_{n}/w)$ 取 norm，
得到全标签 Jacobi 算子 $\mathcal C_a$，有
$$
 \boxed{\quad
 \|\mathcal C_a-D\mathcal B(a)\|
       _{\ell^1\to\mathfrak C_{\sigma_g}\oplus\mathbb C^2}
 <2^{-310},\qquad \|a\|\le1/12.
 \quad}                                                     \tag{119.36}
$$
这里 $D\mathcal B(a)$ 自然限制到 $\sigma_g$。全部高输出和 mean 通量
在同一个 norm 内；没有仅比较低172行。
整体物理竖直平移的准确列仍是 $v=\lambda,p_{n}=0$。
若先减去当前 $C_0$ 再用上表，须在高度行加回同一个平移；不能同时把
cut mean 与 flat mean 都设为0。

## 7. 实际物理 $C^2$ 费用与剩余问题

在参考坐标上，(119.8) 直接给
$$
 u_{rr}=\frac wr(AK+F_t),\quad
 u_{r\theta}=wV,\quad u_{\theta\theta}=rwU.
 \tag{119.37}
$$
用 (119.20)、(119.26) 和 $r<3,w<3w_c$，完整高度二阶 norm
小于 $2^{30}\zeta\|X\|$。
(119.24) 的一次微分重建完整水平二阶数据；在 $1<r<3$、
$|w|,|w_r|<1$ 及 (119.23) 的实际球内，coframe、connection 和两个角
原函数的总费用可宽松取 $2^{20}$。径向角规范使用准确恒等式
$\gamma_r=(a_1G-(b_1)_\theta)/l$，不通过微分 $G$ 引入高度三阶。这可由 (119.31)–(119.33) 的同一
逆/平方根界或 R115 (115.20) 逐项放宽得到，**不需高度三阶**。
加上柱坐标到物理 Cartesian jets 的费用 $2^6$，再作实际等比缩放，
有
$$
 \|F_a-F_0-\lambda e_z\|_{C^2({\rm final\ group})}
 <2^{56}\frac\zeta{\rho_*}\|X\|
 <2^{-778}\|a\|.
 \tag{119.38}
$$
最后一步用了 R115 的真实 $\epsilon/\rho_*<2^{440}$、
$\delta<2^{-131}$ 及 $\|X\|<(13/4)\|a\|$；
$56+440+2-131(39/4)=-779.25<-778$。
这包含对极小物理半径的二阶缩放，不将 $1/\rho_*$ 丢掉。
完整 tail 上的旧 $C^2$ 费用仍用 R115；(119.38) 只增加此实际有限组。

本篇因而提供了一个真正可与主体联立的外端：其完整 metric germ、
全部 raw 两迹、normal/ground-state 换元、mean 及有限二次费用均明确。
外端现在是**原 $q=2$ 放大段的末端**。从这里到 regular $r=25/8$
还要经过该放大段、准备组、两个 bump 和长径向段；高标签到那个切口
的统一逆不由 (119.28) 或 (119.36) 自动得到。尤其不能把角宽下降后的
前向小余项作为同宽 Neumann 逆使用。

相邻 [有理核验程序](../scripts/fourfold_installed_final_connector_20261113.py)
实际核验上面的角宽、有限常数、缩放指数及多项式恒等式；
[完整小报告](../notes/2026-11-13-R119-installed-final-connector-budget.json)
保存每个门。无限标签和实际 PDE 的结论来自本篇证明，而不是有限门的
数目；本次未冒充重跑 R72 无限尾或未保存的原生大矩阵。
