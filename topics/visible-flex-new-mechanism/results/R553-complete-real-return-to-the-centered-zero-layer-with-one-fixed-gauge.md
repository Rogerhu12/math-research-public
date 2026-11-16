# R553：同一固定规范下到达完整返回层的有限真实路径

日期：2026-11-16。**完整原式纸面证明；没有执行数值、符号、profile、秩或新的科学任务。**

本稿将 R551 的小反向入段推进到一个准确的实际端口：在其从起点细选的小正高度子族中，同一个33行母、同一个 $\chi$ 和同一个原零历史起点，先沿 R540 到达 $k>2$，再通过有限次真实矩脉冲和负 $\delta$ 段，准确到达
$$
d_c=h(\omega-\omega_c)-k=0.
$$
原累计 $p_1^{\omega_c}$ 仍严格为负。没有重置第二或第三历史，没有切换母或 Gram，也没有使用无 ruling 桥。

这支付了 R547 所要求的整个薄层返回，而非仅一个小增量。它不支付慢 $t_1$ 恢复。实际末端的 $k$ 降回小量，速度平方仍产生真实的负 $t_1$ 费用；全八矩、末常态 germ、第三 period、pose 及主机制仍未完成。

来源：
[R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md)、
[R533](R533-complete-velocity-quadratic-form-and-all-history-regular-ruling-coordinates.md)、
[R536](R536-real-negative-total-matrix-density-from-a-complete-fast-height-loop.md)、
[R540](R540-same-positive-null-branch-and-real-large-curvature-with-negative-total-matrix-density.md)、
[R546](R546-real-quadratic-matrix-pulses-and-an-exact-same-gauge-zero-coordinate.md)、
[R547](R547-complete-joint-matrix-cost-and-the-real-return-layer-after-large-curvature.md)、
[R551](R551-real-negative-delta-entry-on-the-same-thirty-three-mother-and-fixed-gauge.md)。

## 1. 结论及一次冻结的选择顺序

固定原物理窗口 $I$ 和一个 $\omega_c>0$，使
$$
z_0:=\min_{x\in I}(x+\omega_c)>0 .
\tag{1}
$$
原二十目标、四自然约束、共同 cap、同宽复制、种子、右锚及完整
$\mathcal F_{\rm path}$ 都使用 R533 的同一类。

取一个充分小但有限的 $\epsilon>0$，并在母选择前固定
$$
h_c=\epsilon^{5/2}.
\tag{2}
$$
接着依下文的有限几何界，先固定包含整个正向参考弧和反向参考弧的合法 scalar 紧盒。最后选择原小 $L$、$\Lambda=L^{-6}$、有限正幅根与有限集中频率，使 R533、R536、R551 的全部要求同时成立，并另有
$$
\sqrt L\ll\epsilon^3,\qquad L^3\ll\epsilon^4 .
\tag{3}
$$
一次固定的 $\chi$ 仍由这份母和 R536 的原三个 Gram 条件确定。以后不改它。

存在一条有限光滑真实路径，整个段上
$$
\mathscr K(s,\theta)=0
$$
对全部相位成立，并有：

1. 在同一路径的一个内部时刻 $k>2$；
2. 最终准确 $d_c=0$，且
$$
|h_{\rm out}-h_c|\le C\epsilon^3,\qquad
|\omega_{\rm out}-\omega_c|\le C\epsilon^{1/2},\qquad
|k_{\rm out}|\le C\epsilon^3;
\tag{4}
$$
3. 从原起点累计的
$$
\Pi_{\rm out}:=m_{p_1}-2\omega_c m_{p_2}<0.
\tag{5}
$$

常数先由原有限母图册及固定 $\omega_c,I$ 给出，随后取
$\epsilon$ 小。与 $L,\Lambda$ 有关的低阶误差在相应有限盒上再压入下述明确余量。没有使用一条适用于无界几何或无界历史的完备流。

## 2. 一个包含全部原余项的负速度比较

沿用
$$
\eta=\omega-\omega_c,\quad d_c=h\eta-k,\quad
\gamma=h_s,\quad \delta=k_s/2-\eta\gamma .
$$
R533 的完整式为
$$
F=z^{\mathsf T}Hz+l(S,m)^{\mathsf T}z+q_S(m)+c_{\nu,0}(S).
\tag{6}
$$
记其关于 $(m,z)$ 的完整二次齐次部分为
$$
F_2(S,m,z)=z^{\mathsf T}Hz+l(S,m)^{\mathsf T}z+q_S(m).
\tag{7}
$$
这里只分次数，不删任何 local、Green、primitive 或左尾。

本节研究一个先固定的薄几何带
$$
0<h\le\bar h,\qquad |d_c|\le D h
\tag{8}
$$
内的状态；$D$ 为固定有限常数。实际高度始终另有正下界，完整
$k,\omega$ 在预选盒内有界。

令 $y=x+\omega_c$、$y_*=\omega_c/2$。完整正 null 向量为
$n_+=(b,1)$，并取它的真实速度二次矩
$$
N_+(S)=N(S,n_+(S)).
$$
R546 的完整因子及 R551(8)给
$$
\frac{\alpha_{N_+}}2=W(S,x)(bL_c+r),
$$
$$
W(S,x)=
\frac{b(1+d_c^2-h^2y^2)+2h(hy+d_c)}{8h^4}.
\tag{9}
$$
定义
$$
Q=1+(hy+d_c)^2,\qquad Q_*=Q(\xi_*),\qquad
\sigma(S)=\frac{8h^3W(S,\xi_*)}{Q_*}>0 .
\tag{10}
$$
小高度带中的严格正号由 R551 已付，且
$\sigma\asymp h^{-1}$。

在(8)写 $d_c=h d_1$，$|d_1|\le D$。于是
$$
Q=1+h^2(y+d_1)^2,
$$
$$
8h^4W=b\{1+h^2(d_1^2-y^2)\}+2h^2(y+d_1).
$$
全部 $x$ 仍在固定物理窗口中。因此
$$
\boxed{
W(S,x)=\frac{Q(S,x)}{8h^3}\sigma(S)+E_W(S,x),
\qquad |E_W|\le C h^{-2}.
}
\tag{11}
$$
相对于 $W\asymp h^{-4}$，误差为 $O(h^2)$。这不是把 $W$ 置换成常数；完整误差将进入原平方。

R520 的完整 principal 给
$$
F_2(S,N_+,z)
=\sum_i\lambda_i\int\frac Qh
\left\{W(bL_c+r)+
\frac{Q(\gamma L_c+\delta r)}{8h^3}\right\}^2t_i^2
+\mathcal L_2 ,
\tag{12}
$$
$\mathcal L_2$ 保全部 $C^2$ 二次余项。由(11)，大括号为
$$
\frac Q{8h^3}\bigl\{(z+\sigma n_+)\cdot(L_c,r)\bigr\}
+E_W(bL_c+r).
$$
所以(12)与完整 $H$ 平移平方的差满足以下准确估计，而非声称两者相等。

在 $\widehat z=(\widehat\gamma,-\theta)$、
$|\widehat\gamma|\le C_0$、固定 $0<\theta<1$ 上，令
$$
\mathcal D(S)=\frac{\Lambda\sigma(S)^2}{64h^7}.
$$
则
$$
\boxed{
\frac{
F_2(S,N_+,\sigma\widehat z)
-\sigma^2(\widehat z+n_+)^{\mathsf T}H(\widehat z+n_+)}
{\mathcal D(S)}
=O(h^2)+o_\Lambda(1)
}
\tag{13}
$$
连同对 $\widehat\gamma$ 的一次导数成立。

核(13)必须分两类。由(11)、$C^2$ jets 的统一界及 R533 的真实
$\sum\|u_i'''\|_2^2=O(\Lambda)$，交叉项的绝对值至多
$C\Lambda h^{-7}$，余平方项至多 $C\Lambda h^{-5}$；除以
$\mathcal D\asymp\Lambda h^{-9}$ 即为 $O(h^2)$、$O(h^4)$。
另一类是 $\mathcal L_2$ 与 $H$ 中完整低阶二次项的差。它们在固定正高度下界及有限 scalar 盒内，是统一有界的 $C^2$ 系数，乘有限的
$N_+$、$\sigma\widehat z$ 多项式。故归一后是
$o_\Lambda(1)$，亦有同样的速度一次导数界。选择顺序允许在该有限盒上把它压到最小高度平方以内。

这一估计没有把单独的 second square 当成完整 source，也没有把
$q_S(N_+)$ 因矩阵 $N_+^2=0$ 而删除。原 profile 算子平方、真实第三项和全部尾仍在(12)(13)中。

## 3. 同一正则根上的反向速度比

以下固定 $\theta=1/4$。在
$$
\widehat z_0=-\theta n_+
$$
处，(13)中的平移主项准确为零，因为 $n_+$ 是**完整** $H$ 的 null 向量。其对 $\widehat\gamma$ 的导数为
$$
\frac{2(1-\theta)(H_{11}b+H_{12})}{\Lambda/(64h^7)}
=-2(1-\theta)Q_*^3+o_\Lambda(1).
\tag{14}
$$
它有统一严格负下界。

故在整个预选薄带内，普通 IFT 给同一个小根
$$
F_2\{S,N_+(S),\sigma(S)(v(S),-\theta)\}=0,
$$
$$
\boxed{
v(S)=-\theta b(S)+O(h^2),
\qquad
\frac{v(S)}{-\theta}=b(S)+O(h^2).
}
\tag{15}
$$
这里已将(13)的低阶误差压入 $O(h^2)$。$v$ 是一个确定的完整源根，不是自由选出的连续函数。

它与 R551 的实际正 $X$ 分支相同。事实上从很大的正
$\delta$ 入速出发，$F_\gamma$ 的号是负；R551 的右投影区内该号不能变。式(14)给的有限根也具有同一个严格负号，且
$$
X/\tau=(1-\theta)\sigma+o(1)>0
\tag{16}
$$
在对应的真实大历史实现中成立。因此没有通过换 conic 连通分支取得(15)。

## 4. 一条有界的反向参考场

把 $r_{\rm ret}=d_c-d_{c,\rm in}$ 用作返回参数。由原水平关系，
无论实际 history 如何，只要 $\delta<0$，
$$
\frac{d(\eta/h)}{d d_c}=-\frac1{h^2}.
\tag{17}
$$
式(15)定义的参考场为
$$
\boxed{
\frac{dh}{d d_c}=-b(S)+E_h(S),\qquad
\frac{d(\eta/h)}{d d_c}=-\frac1{h^2},\qquad
|E_h(S)|\le Ch^2.
}
\tag{18}
$$
它只是后文要 shadow 的有限 scalar 场，尚未把理想状态
$m/\tau=N_+(S)$ 当成实际恒等式。

为比较正反两弧，定义只依赖 $h,d_c$ 的 principal 斜率
$$
b_0(h,d_c)=\frac{\mathsf C[Q^3]}{2\Lambda Q_*^3}.
\tag{19}
$$
在(8)由 R551 的统一矩界及
$\mathsf C_0=2\Lambda/\omega_c+O(1)$，
$$
b_0=\frac1{\omega_c}+O(h^2)+O(\Lambda^{-1}),
$$
且其 $(h,d_c)$ 一次导数在小带内有统一界。完整 $b$ 与
$b_0$ 的差可在先固定的有限盒上随 $\Lambda$ 压到任意指定小量。这一步不要求低阶余项独立于 $k,\omega$；它们只需在那个有限盒中有界。

因而正向 R540 场与反向(18)可以共同写为
$$
h_\tau=b_0(h,d_{c,a}-\tau)+e_+(S),\qquad |e_+|\le\varepsilon_\Lambda,
$$
$$
h_{d_c}=-b_0(h,d_c)+e_-(S),\qquad
|e_-|\le Ch^2+\varepsilon_\Lambda,
\tag{20}
$$
其中可取 $\varepsilon_\Lambda\le h_c^2$。

## 5. 正向到大曲率，反向不碰高度零

R536/R540 的实际选择腿末记为 $S_a$。在(3)下
$$
h_a=h_c-\sqrt L+O(L)\asymp h_c,\quad
d_{c,a}=O(L^3),\quad
k_a,\eta_a=O(L^3),\quad \eta_a>0.
\tag{21}
$$
令正向参考长度为 $\epsilon$。由 R551 的原估计，
$$
h_a+b_-\tau\le h_{\rm f}(\tau)\le h_a+b_+\tau,
\qquad 0\le\tau\le\epsilon ,
$$
$$
h_{\rm f}(\epsilon)\eta_{\rm f}(\epsilon)
\ge
\frac{(h_a+b_-\epsilon)^2\epsilon}
{h_a(h_a+b_+\epsilon)}.
\tag{22}
$$
这里 $b_\pm>0$ 固定。代 $h_a\asymp\epsilon^{5/2}$，末式为
$c\epsilon^{-1/2}$ 的下界。因此 $\epsilon$ 足够小时正向末端
$k>3$。R540 的有限真实 shadow 再将它实际化为 $k>2$，同时保原负累计。

在反向参考弧上令
$$
t=d_{c,a}-d_c,
$$
所以它从 $t=\epsilon$ 向 $t=0$ 走。以正向末态为真实相同的参考初值，记反向高度 $h_{\rm b}(t)$。由(20)的同图比较与普通 Gronwall，
$$
\boxed{
|h_{\rm b}(t)-h_{\rm f}(t)|
\le C\int_t^\epsilon(h_c+v)^2\,dv
+C\varepsilon_\Lambda\epsilon
\le C\epsilon^3 .
}
\tag{23}
$$
该证明只用 $b_0$ 在薄带内的统一 Lipschitz 界。先在
$|h_{\rm b}-h_{\rm f}|\le h_c/2$ 的暂定管内作估计，再由
$\epsilon^3=o(h_c)$ 闭合 continuation。于是整个参考返回满足
$$
h_{\rm b}(t)\ge c(h_c+t)>0.
\tag{24}
$$
这是真正排除了高度退化，不能只由局部速度图光滑代替。

同时 $d_c=d_{c,a}-t$ 给
$|d_c|\le D h_{\rm b}$，只需先取固定足够大的 $D$。因此(8)的假设沿整弧自行保持，(15)(18)始终是同一个已定义的完整根。

## 6. 原物理窗口的保持及真实小末态

令 $w=\eta/h$。原水平关系在正、反两弧上均给
$$
\frac{dw}{dt}=\frac1{h^2}.
$$
两弧在 $t=\epsilon$ 的 $w$ 相同。因此由(23)(24)，
$$
\left|w_{\rm b}(t)-w_{\rm f}(t)\right|
\le C\int_t^\epsilon
\frac{|h_{\rm b}(v)-h_{\rm f}(v)|}{(h_c+v)^3}\,dv
\le\frac{C\epsilon^3}{(h_c+t)^2}.
\tag{25}
$$
正向 $\eta_{\rm f}\ge0$，故
$$
\boxed{
\eta_{\rm b}(t)\ge
-\frac{C\epsilon^3}{h_c+t}
\ge-C\epsilon^{1/2}.
}
\tag{26}
$$
先取 $\epsilon$ 小到 $C\sqrt\epsilon<z_0/4$，就有整个真实参考弧的
$x+\omega_c+\eta>3z_0/4$。没有用 $\eta$ 必须始终正的假设，也没有把两参考弧的 $\eta$ 当成相同。

在 $d_c=0$ 即 $t=d_{c,a}$ 处，(21)–(26)给
$$
|h-h_c|\le C\epsilon^3,\qquad
|\eta|\le C\epsilon^{1/2},\qquad
|k|=|h\eta|\le C\epsilon^3.
\tag{27}
$$
这里 $L$ 已按(3)再取小，以吸收起点小项。参考场可在
$d_c=0$ 两侧再延续一个固定有限的小缓冲量，例如
$O(\epsilon^4)$，仍保持(24)(26)的严格裕量。

整个参考 arc 的 $k,\eta$ 虽在中途可以很大，仍有事前有限界。
例如由 $h\ge c h_c$、总参数长度 $O(\epsilon)$ 和(17)即可取粗界
$|w|\le C(1+\epsilon/h_c^2)$，再给 $h,k,\eta$ 的有限盒。
先固定这个盒，后选最终 $\Lambda$，所以(13)(19)(20)的低阶界没有量词循环。

## 7. 参考返回由有限次原矩脉冲实际实现

现在固定全部有限参数、母、$\chi$ 和上面的紧参考 arc。
只使用已经实际存在的正 $X$ 入端。下文的“归一”只用于估计，不改变真实矩阵。

在某个实际分点 $S_j,m_j,T_j$，先用 R546/R551 的正 $X$ 脉冲，取一个有限大 $\tau_j$，再取更大的有限平台幅 $B_j$ 和短 ramp，得到
$$
S_j^{\rm new}=S_j+o(1),\qquad
m_j^{\rm new}/\tau_j=N_+(S_j)+o(1).
\tag{28}
$$
$m_j$ 没有被删去：先使 $|m_j|/\tau_j$ 小，再使有限平台的真实误差小。每次输入都与原已有 germ smooth 相接，全部第三入值继承。

随后按 R551 指定
$$
\delta=-\theta\sigma(S_j)\tau_j
$$
并在同一负 $F_\gamma$ 根上解 $\gamma$。用 $u=\tau_j s$、
$n=m/\tau_j$，完整方程是
$$
F_2\{S,n,(\gamma/\tau_j,-\theta\sigma(S_j))\}
+\tau_j^{-2}c_{\nu,0}(S)=0,
$$
$$
n_u=N(S,\gamma/\tau_j,-\theta\sigma(S_j))
+\tau_j^{-2}M_0(S).
\tag{29}
$$
在每个足够小的返回参数步长 $\Delta d_c$ 内，(28)(29)的实际 scalar 增量为(18)的 Euler 增量加
$$
O((\Delta d_c)^2)+o_{\tau_j,B_j,\mathrm{ramp}}(1).
\tag{30}
$$
所有常数在先固定的参考紧管上共同取得。$n$ 在步内照(29)真实变化；没有假设它沿整个步仍等于 $N_+(S)$。

式(16)在小步内保持，故末态仍有真实 $X>0$。于是可以接下一次正
$X$ 脉冲，再归一到下一点的 $N_+$。这给一个有限递推，而不是把非实际的状态重置当作操作。

具体选择顺序是：先定一个足够细的**有限**分割以控制(30)的平方误差；然后对每一步，在前一步的实际有限输出已确定后，依次选择有限
$\tau_j$、有限 $B_j$、有限 smooth ramp 长度，使全部新增误差之和小于预先给定的 scalar 容差。历史可能逐步很大，但步数有限，每一步都在其自身原状态上操作，没有要求一个固定幅度支配全部无界历史。

标准有限 Euler 误差估计遂使整条实际 scalar 路径任意接近(18)的参考返回，且原高度、物理窗口和速度根裕量同时保持。所有完整 source 都由(29)准确为零，近似仅用于证明端点在哪里。

## 8. 准确到达 $d_c=0$，而不是只趋近

用第6节在 $d_c=0$ 两侧的缓冲，先将最后一个负输入步安排为其理想末值严格超过零。把全部 shadow 误差取得更小，则该步实际开始时 $d_c<0$、结束时 $d_c>0$。

在这一个实际步内，
$$
(d_c)_s=\theta\sigma(S_j)\tau_j>0
$$
准确为常正值。因此存在唯一的有限停止时刻，准确满足
$$
\boxed{d_c(s_{\rm stop})=0.}
\tag{31}
$$
它不是用极限端点替代实际根。该时刻仍在同一个 regular 开 germ 内，原 source 与全部相位关系保持；没有在停止点强改成常态速度。

选择 scalar shadow 容差小于 $\epsilon^4$ 等固定正裕量，即得(4)。
本稿没有清零 $h-h_c$、$\eta$ 或 $k$ 的真实小误差，也不将其末 pose 视为原 pose。

## 9. 原三个 $p$ 矩可以保预算，另外五矩与第三不可省

从 R536 的原起点开始，记已有严格负累计为
$-\varepsilon_P<0$。R540 正向高曲率段按原证明使其三个 $p$ 矩追加费用足够小。对第7节的有限个新段，原 $p_0,p_1,p_2$ 都只是当前 scalar 的连续函数，在预先固定的有限盒上有界，不含速度平方。

每个矩脉冲的真实时长是 $\tau_j/B_j^2$，每个负输入返回步的真实时长为
$\Delta d_c/\{\theta\sigma(S_j)\tau_j\}$，smooth ramp 也可在有限幅固定后再缩短。因此在不改变(28)–(31)的情况下，可以使全部新段的真实三个 $p$ 矩累计范数小于任意预定正数。取其对 $\Pi$ 的费用小于原可用负余量的一半，就得到(5)。

这个估计绝不适用于 $r,s,t$ 五类矩。尤其原
$$
t_1=\frac{k^2+2k d_c+2h\omega_c k-1}{8}
-\frac{\gamma^2}{8h^2}
\tag{32}
$$
始终保留。在每个有限归一返回段上，它的速度费用为
$$
-\frac{\tau_j}{8}\int
\frac{(\gamma/\tau_j)^2}{h^2}\,du ,
\tag{33}
$$
还须加全部正 $X$ 预脉冲与切换的真实费用。一般这些负项很大。
原静态部分虽可因真时长短而小，不能抵销或删除(33)。若原入端的总 $t_1$ 为负，还可把全部新段静态正增取得小于该负余量的一半，因而本次返回后总 $t_1$ 仍严格为负；没有把它误记为已支付的矩。

第三历史仍准确积分
$$
T_s=-M_{\rm raw}\circ\Phi_m+C(S,j^2S),
\tag{34}
$$
其中真实输入的加速度和全部前缀都在内。每个参数、每个幅和每个步数最终有限，所以它是有限 smooth 路径的真实输出；没有声称
$T$ 小、为零或可以从下一步重新累计。frame、位置与第四成本亦保真实输出。

## 10. 同一条真实后继还可以改变 $k$ 的号

上述准确返回端并不是必须停止的位置。在参考返回场上，
$
\frac{dk}{d d_c}
=-2\left(1+\eta\,\frac{\gamma}{\delta}\right).
\tag{35}
$
由(15)(27)，在 $d_c=0$ 附近有
$|\eta|\le C\sqrt\epsilon$、$|\gamma/\delta|\le C$。取 $\epsilon$ 更小，得到
$
\frac{dk}{d d_c}<-1.
\tag{36}
$
若(27)中的端点界记为 $|k|\le C_k\epsilon^3$，就将同一个参考场再延续一个
$(2C_k+2)\epsilon^3$ 的 $d_c$ 增量。这段高度变化为
$O(\epsilon^3)=o(h_c)$；由(17)，$\eta$ 的变化为
$O(\epsilon^3/h_c)=O(\sqrt\epsilon)$，所以同一个合法域与(36)继续保持。

在这个额外的固定有限紧弧上，仍使用第7节的有限真实脉冲细分。它不是将某一份理想 $n=N_+$ 沿整段冻结。将实际 shadow 误差取得小于
$\epsilon^3/2$，并用相同严格单调事件固定最终的 $d_c$，便得到
$
\boxed{
d_{c,\rm out}>0,\qquad k_{\rm out}<-c\epsilon^3<0,
\qquad \Pi_{\rm out}<0 .
}
\tag{37}
$
全部三个 $p$ 矩的额外费用仍能按第9节压小，母、$\chi$ 与全部真实入值均不变。

因此原
$
p_2(S_{\rm out})=-k_{\rm out}h_{\rm out}/2>0
\tag{38}
$
确实有一个实际正密度入端。它不是正的总 $p_2$ 收据：目前的实际停留很短，先前累计、其它矩和 $t_1$ 的负费用仍在。式(37)只进一步说明，R547 所要求的 $k$ 换号也能由本条同规范真实后继实现，不能由此预支慢控制或总矩返回。

## 11. 整个返回层已付，慢恢复没有预支

R547 说明，保净负 $\Pi$ 而补原 $t_1$，不能永远留在
$k\ge0,d_c\le-d_*<0$ 区。本稿在同一33母与固定 $\chi$ 上实际完成其中一条所需动作：从真实 $k>2$ 高曲率点返回到准确 $d_c=0$，没有丢掉前缀或更换 Gram。

但末端由(4)有
$$
|\zeta|=|k+2d_c|=|k|=O(\epsilon^3)<1.
$$
因此这里并没有同时进入已可长期支付正 $t_1$ 的区域。R547 的联合恒等仍适用，新增速度负费用也仍在(33)中。要完成全矩，下一段必须再次改变真正的慢变量并支付全部新欠账；不能把本稿的有限快速返回称为一个已闭的慢恢复环。

本文已闭的是“整个返回层是否能由同一实际 source 到达”这一具体问题。仍欠原总八矩、末 scalar/germ、第三返回、pose 和完整主机制。上述范围不借 R521/R544 的另一母或另一份 $\chi$，也不把局部正则图本身当成完备流。


窄核说明：literature仅核了(25)–(27)所用的几何积分估计与
$h_c=\epsilon^{5/2}$ 的阶数，在共同高度下界和(23)前提下通过；
(12)–(16)的完整源比较、同支识别及第7–8节的有限实际刷新由本文证明。
全部为纸面推导，没有新增科学执行。
