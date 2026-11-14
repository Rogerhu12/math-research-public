# R119 续篇：实际 canonical 根图到原径向切口的全频两迹传递

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在
[真实联合解析根](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
的同一非零标签背景上，把 $\xi_*=1/64$ 的 constant canonical
截面准确接回原先固定的物理径向截面。保留真实特征平移作端口
预条件后，这项接线在原根的同一 $H^s\oplus H^s$、$|s|\le4$
中有完整相对界
$$
 \|\mathcal P_e^{-1}\mathcal T_e-I\|
                  <2^{256}b_e^2n_e.                       \tag{G.1}
$$
此处 $\mathcal P_e$ 包含真正的两支密度 pullback、mean 高度及
所有实际 height/conormal 乘子；它不是恒等算子。
把它与前篇完整 root Cauchy 接合后，每个根的相对费用可取
$2^{4800}b_e^2n_e$。新尾实际满足 $\|X\|\le2^{-262144}$ 时，
全部四根/胞元的完整和小于 $2^{-97340}$。

ordinary 与 weak 源的完整 Piola、height 修正、mean 和法向
端点负荷都明确给出。一般原 $L^2_tH^s_\theta$ 体源没有被
免费当成径向—角混合图上的高窗源；本篇给可直接消费的真实
联合源 norm，并说明为什么实际标签及材料参数 Jacobi 列在这些
根 germ 内的体源恰为0。

## 1. 真正固定的原径向切口

沿用前篇 $x=\varsigma b(t-t_e)$、$\Psi=(\xi,\phi)$、
$\xi_0(x)$、$n=n_e$ 和 $b=b_e$。取
$$
 x_*:=\xi_0^{-1}(1/64),\qquad
 t_*:=t_e+\varsigma x_*/b.                                \tag{G.2}
$$
这是原材料径向 $t$ 的固定切口，非径向标签改变时不移动。
它满足 $Q(x_*)>1/128$，故确实在严格负型区。
两根分别使用自己的 $\varsigma$；不是把右根当成向外为正。

将 $t=t_*$ 在真实 canonical 图中写成
$$
 \phi=H(\theta):=\phi(x_*,\theta),\qquad
 \xi=g(\phi):=\xi(x_*,H^{-1}(\phi)),\qquad
 d(\phi)=g(\phi)-\xi_*.
 \tag{G.3}
$$
本篇的 $d$ 只记图的高度差，不是原 Jacobi principal drift。
前篇 (J.16)--(J.19) 的完整复逆给
$$
 \|d\|_{\operatorname{Im}\phi\le1}<D_e:=2^{13}n,
 \quad \|H-\mathrm{id}\|<2^{10}n/b,
 \quad |H'-1|<2^{11}n/b.                                 \tag{G.4}
$$
它们是完整解析函数界。$d$ 可以变号或为0；下文不会除以 $d$。
所有路径都位于 $1/128<\xi<1/32$ 的同一个已付联合解析 germ，
不穿过任一仅 $C^2$ 径向接缝。

先在明确的小球
$$
 b^2n\le2^{-512}                                         \tag{G.5}
$$
上证明接线。真实工作输入比它强得多：
$b^2<2^{32}(j+4)\delta_j^{-9/2}<(K_j^{\rm ref})^2$，
全标签篇 (U.25) 给 $b^2n<2^{-102142}$。
因此本篇没有为获得小常数改动原对象或重新选择 profile。

## 2. 三个局部特征态，保留完整 density potential

前篇的完整 canonical 方程是
$$
 u_{\xi\xi}-c(\xi)^2u_{\phi\phi}+Vu=f_c-\operatorname{div}F_c,
 \qquad c(\xi)=\sqrt\xi/b.
 \tag{G.6}
$$
在本严格小段令
$$
 w=\sqrt c\,u,\qquad
 \kappa=\frac{V+5/(16\xi^2)}c,
 \qquad F_d=c^{-1/2}F_c,
 \qquad f_d=c^{-1/2}\left(f_c-\frac{c'}{2c}F_c^\xi\right).
 \tag{G.7}
$$
这里 $w$ 是 Jacobi 密度高度，不是参考旋转曲面的 slope。
后者在第7节记为 $w_{\rm ref}$ 以免混淆。
准确完整方程成为
$$
 \operatorname{div}
   \left[\begin{pmatrix}1/c&0\\0&-c\end{pmatrix}\nabla w\right]
                 +\kappa w=f_d-\operatorname{div}F_d.
 \tag{G.8}
$$
$5/(16\xi^2)$ 来自 $(c^{-1/2})''/c^{-1/2}$，并未丢弃。

定义完整 total 动量和两个密度态
$$
 z=w_\phi,\qquad \zeta=w_\xi/c+F_d^\xi,
 \qquad y_\pm=(z\pm\zeta)/2.
 \tag{G.9}
$$
直接微分得到一个局部三态系统：
$$
 \begin{aligned}
 w_\xi&=c(y_+-y_-)+S_0,\\
 (y_\sigma)_\xi-\sigma c(y_\sigma)_\phi
                &=-\sigma\kappa w/2+S_\sigma,
                  \qquad\sigma=\pm1,\\
 S_0&=-cF_d^\xi,\\
 S_\sigma&=\tfrac12\left(\sigma f_d
                -c\partial_\phi F_d^\xi
                -\sigma\partial_\phi F_d^\phi\right).
 \end{aligned}                                             \tag{G.10}
$$
主速度为 $0,-c,+c$，所有剩余项都是局部乘法。
约束 $w_\phi=y_++y_-$ 由 (G.10) 准确保持。
因此并不需要在变时间图上把一个非局部 $\partial_\phi^{-1}$
误当成可与取迹交换的算子。

在前篇已付复域内，$|V|<17$。在本严格小段及其所用复邻域，
$|\xi|>1/128$、$|c|<1/b$、$|c|^{-1}<16b$，故
$$
 |\kappa|<2^{17}b,
 \qquad \|B(\xi,\phi)\|_\infty<2^{18}b,                 \tag{G.11}
$$
其中 $B$ 为 (G.10) 的完整三态零阶矩阵。
虽然这比精细高频估计粗，但 $bD_e$ 已由 (G.5) 支付。

## 3. 真图迹与不会遗漏 mean 的完整端口空间

先取 $F_d=0$。图上的真实密度态是
$$
 Y_\sigma(\phi)=
 [1+\sigma c(g(\phi))g'(\phi)]\,
                 y_\sigma(g(\phi),\phi),
 \qquad W(\phi)=w(g(\phi),\phi).
 \tag{G.12}
$$
准确有
$$
 W'=Y_++Y_-,\qquad
 p_{d,g}:=w_\xi/c+c g'w_\phi=Y_+-Y_-.
 \tag{G.13}
$$
所以图的第二行是完整 conormal 密度，不是裸 $w_\xi$。

对 $q=s-1/2\in[-9/2,7/2]$，定义完整端口
$$
 \mathcal E_q={(a,y_+,y_-):\langle y_++y_-\rangle=0\},
 \qquad \|(a,y_+,y_-)\|=|a|+\|y_+\|_{H^q}+\|y_-\|_{H^q}.
 \tag{G.14}
$$
这里 $a=\langle w\rangle$ 是独立 mean 高度；高度由
$$
 w=a+\partial_\phi^{-1}(y_++y_-)
 \tag{G.15}
$$
准确恢复，$\partial_\phi^{-1}$ 使用全部 $m\in4\mathbb Z\setminus0$。
它从 $H^q$ 到 $H^{q+1}$ 有界，且作为 $H^q$ 算子的 norm
至多 $1/4$。独立通量 mean 是 $\langle y_+-y_-\rangle$，
并没有再加条件把它置零。

定义两个准确的原点到图的 principal 特征标签
$$
 L_\sigma(\phi)=\phi+\sigma\int_{\xi_*}^{g(\phi)}c(\tau)d\tau,
 \qquad L_\sigma'=1+\sigma c(g)g'.                       \tag{G.16}
$$
与前篇 (J.10) 的原两支标记相比，准确对应是
$\epsilon=-\varsigma\sigma$：前篇
$S_\epsilon=\phi-\epsilon\varsigma\,2\xi^{3/2}/(3b)$，
而本支的标记是 $\phi+\sigma\,2\xi^{3/2}/(3b)$。
因此左右根的支交换明确保留，接回 strict 段时须使用此对应。
在 (G.5) 上它们是真实 degree-one 圆周微分同胚。
它们及逆的前6阶导数由 (G.4) 的同一复域控制。
对于 $|q|\le5$，真 density pullback
$D_L f=L'f\circ L$ 及其逆的 $H^q$ norm 均小于 $2^{20}$。
可先在整数 $0,\ldots,5$ 上用链式法则和 change of variables
证明：高阶导数的 Bell 系数和小于 $2^{16}$、Jacobian 在
$(1/2,2)$ 内；负整数由 $D_L^*=C_{L^{-1}}$，中间指数由
Hilbert 插值给出。这里没有估计 $D_L-I$ 的同空间 norm。

于是完整 principal 端口算子定义为
$$
 \mathcal P_g(a,y_+,y_-)
       =(a,D_{L_+}y_+,D_{L_-}y_-).
 \tag{G.17}
$$
两条 density pullback 各自保留积分，所以 (G.17) 确实把
$\mathcal E_q$ 映回自身，且有 onto 逆，双向 norm 小于 $2^{20}$。
输出高度通过 (G.15) 重建；不能把两支不同 pullback 后的高度
仍写成输入高度。独立 mean 行则准确按 (G.17) 定义保留。

## 4. 不除图高差的完整有序特征级数

对 (G.10) 先沿其三条真实主特征作 Duhamel。对图末端
$\xi=g(\phi)$，第 $k$ 项的有序径向变量统一写为
$$
 \xi_\ell=\xi_*+s_\ell d(\phi),\qquad
       0\le s_k\le\cdots\le s_1\le1.
 \tag{G.18}
$$
每个积分带完整因子 $d(\phi)^k$。
因此 $d$ 变号时保留原积分方向，$d=0$ 时所有非零阶项自然为0。
不存在需要另外选择符号域的退化坐标分母。

每条有序路径的末端输入角和各中间角均形如
$$
 \Phi(\phi)=\phi+
 d(\phi)\int_0^1\epsilon(s)
              c(\xi_*+s d(\phi))ds,
             \qquad |\epsilon(s)|\le1,                 \tag{G.19}
$$
在部分区间积分时将 $\epsilon$ 置0。
这给与 $k$ 无关的真解析微分同胚界：位移小于 $D_e/b$，
前6阶导数与恒等之差均小于 $2^{20}D_e/b$。
完整路径的符号可以任意切换，并未假定各段同支。

系数乘积在角宽 $1/8$ 的完整复域中有上界
$(2^{18}bD_e)^k$。在 $|q|\le5$，一个该宽解析函数的乘法
norm 至多 $2^{40}$ 倍其复域上确界：用
$e^{-1/2}<2/3$，逐项求和
$1+2\sum_{k\ge1}(1+4k)^5(2/3)^k<2^{40}$ 即可。
把整个系数乘积一次作为乘子估计，再用 (G.19) 的完整
$H^q$ pullback 界，不能按路径次数重复支付角宽。

包括全部三态路径计数、图密度的因子和 $1/k!$ 后，第 $k$
阶算子 norm 被
$$
 2^{64}\frac{(2^{20}bD_e)^k}{k!}
 \tag{G.20}
$$
控制。先在光滑 Fourier 数据上逐项推导；此可求和的同空间
上界给所有 $H^q$ 数据的唯一延拓。约束和完整 mean 由光滑
逼近保留，不是事后删除一个常数槽。

第0项在两个 density 行恰是 (G.17)，在高度 mean 行恰是
$a$。真实 $w$ 的函数值不等于 principal 重建高度，比较时只
在 (G.14) 的完整端口坐标中读它的 mean。由
$\|w\|_{H^q}+\|y_+\|_{H^q}+\|y_-\|_{H^q}<2\|\cdot\|_{\mathcal E_q}$，
以及 $2^{20}bD_e<1/2$，得到真实 graph 传递 $\mathcal T_g$
满足
$$
 \boxed{\quad
 \|\mathcal T_g-\mathcal P_g\|_{\mathcal E_q\to\mathcal E_q}
          <2^{112}bn,
 \qquad
 \|\mathcal P_g^{-1}\mathcal T_g-I\|<2^{132}bn.
 \quad}                                                     \tag{G.21}
$$
这是一条完整两迹加 mean 的算子结论。没有把仅一支 height
kernel、一个有限模图或小相位的点态界升级为全频 operator norm。

## 5. 转回前篇同一个 Airy 两态

在 $\xi=\xi_*$，$c_*=1/(8b)$、$c'_*/(2c_*)=16$。
前篇两态为 $Z=(s^{1/2}u,s^{-1/2}u_\xi)$，其中
$$
 s_m=(1+(|m|/b)^{4/3}+(|m|/b)^2/64)^{1/2}.
$$
从它到 (G.14) 的准确算子 $\mathcal A_*$ 是
$$
 a=\sqrt{c_*}\langle u\rangle,\qquad
 y_\sigma=\frac12\left[\sqrt{c_*}u_\phi
                +\sigma\frac{u_\xi+16u}{\sqrt{c_*}}\right].
 \tag{G.22}
$$
所有 mean 和 normal shear 都在此式中。
对 $m\ne0$ 使用
$s_m\ge\max(1,c_*|m|)$、
$s_m\le3(1+|m|/b)$、$|m|\ge4$，直接逐模得到
$$
 \|\mathcal A_*\|_{H^s\oplus H^s\to\mathcal E_{s-1/2}},
 \quad
 \|\mathcal A_*^{-1}\|_{\mathcal E_{s-1/2}\to H^s\oplus H^s}
                         <2^{20}\sqrt b.
 \tag{G.23}
$$
在 $m=0$，单独使用
$a=\sqrt{c_*}u_0$ 和
$y_{+,0}=-y_{-,0}=(u_{\xi,0}+16u_0)/(2\sqrt{c_*})$，
得到同一门。没有以 $1/m$ 处理零模。

因此 (G.21) 转回原两态后的相对费用小于
$2^{172}b^2n$，放宽为 (G.1)。这明确支付了真实频率平衡，
没有凭一个非频率平衡的三态估计免费授予 Airy 两行范数。

## 6. 两个真正物理端口及其所有 mean

令 $\alpha$ 为前篇 (J.22) 的完整 raw 密度，并置
$$
 k=\alpha c
       =\left[\frac{w_{\rm ref}}{a_{\rm phys}}
                    \frac{\sqrt Q}{D}\right]\circ\Psi^{-1},
 \qquad
 s_g=\frac{(\partial_\xi+c^2g'\partial_\phi)\log k}{2c}
                         \bigg|_{\xi=g(\phi)}.
 \tag{G.24}
$$
这是原 raw 判别式密度的准确不变量。
对无 weak 源的两迹，原固定 $t=t_*$ 的高度和向正 $t$ 通量
准确为
$$
 \boxed{\quad
 h(\theta)=\left[k^{-1/2}W\right](H(\theta)),\qquad
 p(\theta)=\varsigma H'(\theta)
       \left[\sqrt k\,(Y_+-Y_--s_gW)\right](H(\theta)).
 \quad}                                                     \tag{G.25}
$$
其中 $p=\mu(h_t-d_{\rm drift}h_\theta)$，不是裸径向导数。
证明是在 graph 上先取 $\alpha(h_\xi+c^2g'h_\phi)$，再使用
$h=k^{-1/2}w$；$H'$ 来自 density 端口，$\varsigma$ 来自
原 $t$ 与向内 $\xi$ 的方向。两者都不能删除。

这些公式定义 $\mathcal A_g$：从实际物理 $(h,p)$ 到
$(\langle W\rangle,Y_+,Y_-)$，其逆就是 (G.25)、(G.15)。
所以本篇算子是明确的
$$
 \mathcal T_e=\mathcal A_g^{-1}\mathcal T_g\mathcal A_*,
 \qquad
 \mathcal P_e=\mathcal A_g^{-1}\mathcal P_g\mathcal A_*.
 \tag{G.26}
$$
完整物理乘子与两端角图没有省略，只是在准确相对乘积中相消。
物理配对和 mean 行也明确为
$$
 \langle h\rangle_\theta=
   \left\langle (H^{-1})'k^{-1/2}W\right\rangle_\phi,
 \qquad
 \langle p\rangle_\theta=
   \varsigma\left\langle\sqrt k(Y_+-Y_--s_gW)\right\rangle_\phi.
 \tag{G.27}
$$
一般这两个表达式都不是对应 canonical 状态的裸零模。

在前篇另已列出的 $n\le2^{-4424}$ 域内（真实工作输入同时满足），
每个根现在可以同前篇 $\mathcal U(\xi_*,0)$ 接合，以
$\mathcal P_e\mathcal U_0(\xi_*,0)$ 为实际主相位预条件。
因参考正反 Cauchy norm 均小于 $2^{2184}$，完整相对差小于
$$
 2^{4800}b_e^2n_e.                                       \tag{G.28}
$$
原根点的物理两迹仍用前篇 (J.39)，本篇另一端则已是原固定
$t_*$ 的物理切口。四根求和和所有有限 prefix 费用给
$$
 \sum_e2^{4800}b_e^2n_e
 <2^{164804}\|X\|\le2^{-97340}.                          \tag{G.29}
$$
不同根的真实特征图没有在这个求和中被认作恒等；接下来的 strict
流和全 return 必须消费同一组准确 $\mathcal P_e$。

## 7. 实际 ordinary 和 weak 源空间

前篇的完整原源是 $\operatorname{div}(G\nabla h)=f-\operatorname{div}F$。
先按真 $\Psi$ 作 Piola，记
$\widetilde f=(f/\mathfrak J)\circ\Psi^{-1}$、
$\widetilde F=(D\Psi F/\mathfrak J)\circ\Psi^{-1}$。
两次 height 共轭可以准确合写为
$$
 F_d=k^{-1/2}\widetilde F,\qquad
 f_d=k^{-1/2}\left(\widetilde f-\tfrac12\nabla\log k\cdot\widetilde F\right).
 \tag{G.30}
$$
这保留 weak 源产生的 ordinary 修正。完整三态源就是 (G.10)。

一个可直接消费且不含假 norm 转授的 source 合同如下。假设这些
实际 $S_0,S_+,S_-$ 在
$|\xi-\xi_*|\le1/256,|\operatorname{Im}\phi|\le1/4$
的联合复域解析，定义
$$
 \mathfrak S_e=\sup
           (|S_0|+|S_+|+|S_-|).
 \tag{G.31}
$$
同一有序路径证明，包括所有源位置，给零初始 total 三态的
graph 输出。先在与 (G.14) 同 norm、但暂不加零平均约束的
环境三元空间 $\mathcal V_q$ 中读取 $(\langle W\rangle,Y_+,Y_-)$：
$$
 \|\mathrm{body\ source\ output}\|_{\mathcal V_q}
                        <2^{80}D_e\mathfrak S_e.
$$
把第8节明确的 weak 端点修正 $\mathcal B_g$ 减去后，输出
确实在 $\mathcal E_q$ 中，因而完整 total-flux 源列满足
$$
 \|\mathcal P_e^{-1}\mathrm{source\ port}_{phys}\|_{H^s\oplus H^s}
 <2^{120}\sqrt b D_e\mathfrak S_e
                      +2^{40}\sqrt b\|\mathcal B_g\|_{\mathcal V_q}.
 \tag{G.32}
$$
普通源的 $\mathcal B_g=0$。若改用 bare 输入/输出，还须加第8节
明确的两端 weak trace 列。若只要求较低正则，亦可直接使用
(G.18)--(G.20) 的实际
路径 source norm；本篇没有据此省略径向正则性。

对于普通 Darboux 源 $e$，无 weak 源时
$$
 f_d=\left[
  \frac{a_{\rm phys}^{1/2}w_{\rm ref}^{3/2}J}
       {Q^{1/4}D\mathfrak J}\,e\right]\circ\Psi^{-1}.
 \tag{G.33}
$$
令 $a_e=a_{\rm phys}(t_e)$、$w_e=w_{\rm ref}(t_e)$。
在实际物理联合域 $|x|\le1/8,|\operatorname{Im}\theta|\le1$
提供 $e$ 的解析上确界 $\|e\|_{\mathcal J_e}$ 时，所有路径和
真逆图均留在此域内，且
$$
 \mathfrak S_e<2^{12}a_e^{1/2}w_e^{3/2}b^{-1}\|e\|_{\mathcal J_e}.
$$
因而 (G.32) 的预条件源列小于
$$
 2^{160}n_e\sqrt{a_e/b_e}\,w_e^{3/2}\|e\|_{\mathcal J_e}.
 \tag{G.34}
$$
所有物理半径、slope、Jacobians 都在此式中。

一般原 $L^2_tH^s_\theta$ 输入不保证 (G.31) 或
$\|e\|_{\mathcal J_e}$ 有限。例如即使 $e$ 在角变量为常数，
只有有限径向正则性的原函数沿 $t=g(\theta)$ 读取也不自动有任意
高角正则。因此本篇没有把该联合源合同称作所有粗源的无损图迹
定理。这里的源范数是明确的实际输入条件，而非藏在常数里的假设。

对当前要反演的真实尾标签列，根 germ 的 ordinary 与 weak
体源准确为0：全标签尾的 Darboux residual 为0，固定 $\Gamma$
的标签导数是齐次 Jacobi 列。材料参数导数也在根内为齐次，
因为该 germ 中 $w_{\rm ref},A$ 在共同 $r$ 坐标不随任何
down-ramp 参数改变。若把它改写为固定物理半径的导数，则应
把已知的整体尺度/坐标变化列一并恢复，不能把
$\dot t=-\dot{\log\rho}$ 或 $\dot a_e=a_e\dot{\log\rho}$ 删除。
这些准确已知列与零体源的材料 Jacobi 列分开相加；不据此假定
任意外来 metric-source 也在根内为0。

## 8. Weak 法向迹、所有周期与平均源行

有 weak 源时仍使用 (G.12)，但完整 graph 关系变成
$$
 W'=Y_++Y_--c g'F_d^\xi|_g,
 \qquad
 p_{d,g}^{tot}=Y_+-Y_--g'F_d^\phi|_g.
 \tag{G.35}
$$
因此周期条件准确是
$\langle Y_++Y_--c g'F_d^\xi|_g\rangle=0$，不是删除
$\langle Y_++Y_-\rangle$。真正物理 total 通量为
$$
 (p+F^t)(\theta)=\varsigma H'(\theta)
 \left[\sqrt k
       (Y_+-Y_--g'F_d^\phi|_g-s_gW)\right](H(\theta)).
 \tag{G.36}
$$
明确地，定义两个实际端点列
$$
 \mathcal B_g^\pm=\tfrac12
       (c g'F_d^\xi|_g\pm g'F_d^\phi|_g),\qquad
 \mathcal B_g=(0,\mathcal B_g^+,\mathcal B_g^-).
$$
则按**齐次**物理端口公式 $\mathcal A_g$ 读取真实 total
$(h,p+F^t)$ 时，得到的恰是
$(\langle W\rangle,Y_+-\mathcal B_g^+,Y_--\mathcal B_g^-)$。
它的两 density 分量之和为 $W'$，故真实地属于 $\mathcal E_q$。
恢复 bare 物理 $p$ 时还须减去原 $F^t$ 的端点迹。
其在该端口空间中的附加列为
$$
 \mathcal B_t^\pm=
 \pm\frac{\varsigma}{2\sqrt k}
                \left(\frac{F^t}{H'}\right)\circ H^{-1}.
$$
所以 (G.32) 的 bare 输出再加
$2^{40}\sqrt b\|(0,\mathcal B_t^+,\mathcal B_t^-)\|$。
若初始输入给的是 bare $u_\xi$，而非 (G.9) 的 total 状态，
还须在平切口加入 $\mathcal B_*=(0,F_d^\xi/2,-F_d^\xi/2)|_{\xi_*}$。
它经完整传递的预条件费用小于 $2^{64}\sqrt b\|\mathcal B_*\|$。
源合同 (G.31) 本身不赋予 $F_d^\xi|_g,F_d^\phi|_g$ 或
$F^t|_{t_*}$ 的端点 norm；若没有从真实 producer 支付这些
trace，只得到 total-flux 合同。

每条密度 mean 和独立高度 mean 的准确有源表达式是
$$
 \langle Y_\sigma\rangle-\langle y_{\sigma,*}\rangle
 =\left\langle\int_{\xi_*}^{g(\phi)}
              [-\sigma\kappa w/2+S_\sigma]d\xi\right\rangle,
$$
$$
 \langle W\rangle-\langle w_*\rangle
 =\left\langle\int_{\xi_*}^{g(\phi)}
             [c(y_+-y_-)-cF_d^\xi]d\xi\right\rangle.
 \tag{G.37}
$$
第一式由完整散度在变上端图上的积分得到，其边界项正是
$1+\sigma c g'$。两式的积分均保留 $d$ 的方向，适用于图与
平切口相交的情形。它们与 (G.27)、(G.35)--(G.36) 一起保留
普通源的物理 mean 电荷、holonomy 和独立高度常数。

图、逆图、$H$、$g$、$k$ 和 $s_g$ 均在前篇的同一完整参数
复域全纯，所有端口微分按其 (J.41)--(J.42) 保留移动图和
Jacobian 项。弱源本身所需的参数导数/法向 trace 仍由其实际
producer 给出，不从一个形式链式法则虚授源正则性。

## 9. 该接线完成了什么

现在四个真实根都已接回原 $t$ 的严格负型切口，且 (G.25) 给
可直接交给 strict 原径向系统的完整高度和密度通量。相对比较
只在保留准确 $L_\pm$ 的主相位预条件后成立；没有把高频平移
当成一个同空间小扰动。完整 mean 与源法向负荷均可按上式读取。

下一步仍需消费原 $t$ 严格段的完整 density 流、在新公共度量上
重新联立实际 ray KAM，并将这些准确端图和正型完整两端 DN
组装成全 mixed high-input inverse。这里并没有由一个根块的
小余项宣布全 return 相位已相同，也没有证明外部非线性匹配。

脚本 `scripts/fourfold_actual_root_graph_two_port_20261113.py` 与
报告 `notes/2026-11-13-R119-actual-root-graph-two-port-budget.json`
核对完整三态、signed graph/weak mean 恒等式、全部有理范数门
以及实际四根/有限前缀求和。无限模算子结论来自上面的完整
特征级数，未采用有限谱替代。
