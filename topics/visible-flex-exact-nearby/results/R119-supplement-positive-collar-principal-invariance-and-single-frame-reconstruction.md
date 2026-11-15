# R119/R133 续篇：正 collar 的 principal 不变性与完整 Cauchy 数据的单一 frame 重建

2026-11-15，visible-exact / tail_connector。

**准确几何接口，全文及真实 coframe/连接/残差号已独立核对。** 本篇将两个不同事实分开证明。
第一，B 端正型 collar 内的改动不改变任何真实 principal return，
因此在固定第二参数后保同一第一参数值图。第二，若最后的真实
Darboux residual已经为0，则完整 Cauchy高度数据在 B 的匹配给出
一个可以连续重建的共同 Euclidean frame。全过程保两 mean、
holonomy、唯一高度常数以及真实角连接。

非zero residual的 graph种子只有准确 Cauchy数据，不因这些数据
已经匹配就获得等距 immersion。也不将以下唯一重建当作对未知
帽内曲率、ν 或另外给定的 height/flux条件的 Schur反演。

## 1. Principal 值图只读取真实负分量

采用已发布的
[L：低范数第一参数图](R119-supplement-low-norm-principal-Gamma-map-and-tame-high-conjugacy.md)
及[新 B collar 种子](R119-supplement-new-94-B-collar-lift-and-actual-graph-seed.md) G。
冻结同一个 $\gamma_2^\flat$、五盒 profile、fixed stop和实际物理
$t,\theta$。对每个允许第一参数 $p$，记其径向 profile为 $w_p$。

L.10 的真实返回是
$$
 (F_\pm)_t=-d(t,F_\pm)\mp\sqrt{Q(t)}\,v(t,F_\pm),
 \qquad {\cal R}_i=F_-^{-1}\circ F_+ .
 \tag{T.1}
$$
它的两条有序路径只位于相应真实负分量 $Q>0$，连同两端原根。
外行 $i=(129,2)$ 使用其新 simple-root 分量，没有替换成自由旋转。
$P,K,U,V$ 及 $w_p$ 的完整 mean都参与 $d,v$，不是只读取非mean近似。

G 的改动支持在
$$
 0\le v_B=-t\le d_B=2^{-1024},\qquad
 Q=S(v_B/2^{-24})-1<-3/4 .
 \tag{T.2}
$$
所有允许 $p$ 的径向控制支持都与此 collar分离。
给定两个非mean高度 $u,\widetilde u$，若它们之差支持在这个 collar，
则对每个允许 $p$，两者在 (T.1) 的整个路径、根和邻域逐点相同。
各自以同一个 $w_p$ 解真实 holonomy小根后，完整 mean亦逐点相同。
因此准确有
$$
 f_i(p,\widetilde u)=f_i(p,u),\quad
 {\mathfrak T}_i(p,\widetilde u)
                     ={\mathfrak T}_i(p,u)\qquad\hbox{全部 }i,p .
 \tag{T.3}
$$
由 L.14--L.15 的同一低球上的唯一固定点，
$$
                     \gamma_1^*(\widetilde u)=\gamma_1^*(u).
 \tag{T.4}
$$
这是整个非线性值图相同，不只是沿某一个方向导数为0。
不需要在更高角 norm中重新选参，也不把第二参数值图扩到
一般有荷方向。第二参数始终是冻结的原实际数。

## 2. 准确高度、metric 和两个正分母

现在独立考虑一个真实连通 annular部分，使用物理半径 $a>0$。
原目标度量是
$$
            g=(1+w(a)^2)\,da^2+a^2d\theta^2 .
 \tag{T.5}
$$
令 $z$ 是 Darboux正高度，满足
$$
 z_a=w(1+K),\qquad z_\theta=awP,\qquad
 U=P_\theta,\quad V=K_\theta .
 \tag{T.6}
$$
$\langle P\rangle=0$ 源于同一个周期高度；
$K=K_\perp+\kappa$ 包含原真正 holonomy mean。
取 $t=\log a$，$q=w^2$、$A=(\log w)_t$、$Q=-A$，
运动学准确给
$$
                        P_t=V+(Q-1)P .
 \tag{T.7}
$$
全文保
$$
 B=1-qP^2>0,\qquad
 D=1-q\{2K+K^2+(1+q)P^2\}>0,\qquad
 J=1+K+(1+q)U>0 .
 \tag{T.8}
$$
这些是已付真实分支条件，不是 $Q$ 的符号条件；
所以根处 $Q=0$ 不造成这里的除零。

考虑 horizontal metric $g_h=g-dz\otimes dz$。
准确矩阵及其 determinant是
$$
 g_h=
 \begin{pmatrix}
 1-q(2K+K^2)&-a q(1+K)P\\
 -a q(1+K)P&a^2B
 \end{pmatrix},\qquad
                  \det g_h=a^2D .
 \tag{T.9}
$$
因此 (T.8) 保 $g_h$ 正定。
全部 mean 已在 $K,P$ 中；不以平均 metric代替 (T.9)。

## 3. 一个明确的 coframe 与真实角连接

选取原径向正定向的 orthonormal coframe
$$
 \omega_1=\frac{\sqrt D}{\sqrt B}\,da,\qquad
 \omega_2=-\frac{q(1+K)P}{\sqrt B}\,da
                         +a\sqrt B\,d\theta .
 \tag{T.10}
$$
有 $g_h=\omega_1^2+\omega_2^2$，
$\omega_1\wedge\omega_2=a\sqrt D\,da\wedge d\theta$。
定义唯一实连接一形式 $\Omega$，使
$$
 d\omega_1=\Omega\wedge\omega_2,\qquad
 d\omega_2=-\Omega\wedge\omega_1 .
 \tag{T.11}
$$
在径向参考上 $\Omega=d\theta$，与原 coframe方向一致。

写
$f=\sqrt D/\sqrt B$、
$g_1=-q(1+K)P/\sqrt B$、
$h=a\sqrt B$。
从 (T.11) 逐项得到
$$
 \Omega_\theta=\frac{h_a-(g_1)_\theta}{f},\qquad
 \Omega_a=\frac{-f_\theta+\Omega_\theta g_1}{h}.
 \tag{T.12}
$$
利用 (T.7)，其中第一式准确化为
$$
 \boxed{\quad
 \Omega_\theta=
 \frac{1+q(1+K)U/B}{\sqrt D}
                     =:{\cal H}_q(P,K,U).
 \quad}                                                   \tag{T.13}
$$
例如 $B_t=2q(P^2-PV)$，故 $B+B_t/2+qPV=1$；
余下两个 $U$ 项以 $B+qP^2=1$ 合成 (T.13)。
这一步没有使用 $K_t=F$。

(T.12) 的 $\Omega_a$ 只读取同一 slice的
$P,K,U,V$、径向 $a,w$ 和角导；它不靠把径向角常数重新设0定义。
全部径向 phase就是这个一形式的径向积分。
更具体地，利用 $D+q(1+K)^2=(1+q)B$ 消去所有剩余的 $PU$ 项，
第二式准确给
$$
 \Omega_t=a\Omega_a
       =\frac{q(1+K)(V-P)}{B\sqrt D}.
 \tag{T.12a}
$$
此式直接保留真实径向角连接，并显式表明其中没有 $K_t$。

## 4. Residual、flatness 和准确 holonomy

采用原完整商式
$$
 F=\frac{Q(2K+U+K^2+KU+qP^2)+(1+q)(V-P)^2}
                       {1+K+(1+q)U},\qquad
 \mathfrak r=K_t-F .
 \tag{T.14}
$$
直接微分 (T.12)，只用 (T.7)、$q_t=2Aq$ 及
$U=P_\theta,V=K_\theta$，得到
$$
 \boxed{\quad
 d\Omega=q\,JD^{-3/2}\mathfrak r\,dt\wedge d\theta .
 \quad}                                                   \tag{T.15}
$$
其 $\mathfrak r$ 系数也可直接核：
$\partial_K{\cal H}_q=qJD^{-3/2}$，而 $\Omega_t=a\Omega_a$
不含 $K_t$；把 $K_t$ 换为完整 (T.14) 后其余项全部消去。
这是 M.16 的未取 mean版本；取圆周平均便恢复
$\partial_t\langle{\cal H}_q\rangle=q\langle JD^{-3/2}\mathfrak r\rangle$。

真实 holonomy小根始终是
$$
                         \langle{\cal H}_q\rangle=1 .
 \tag{T.16}
$$
若 $\mathfrak r=0$，则 $d\Omega=0$。
若只有 (T.16) 而 $\mathfrak r$ 非zero，
只能得到其 weighted mean兼容，不得从中推 $d\Omega=0$。
所以 G 的 off-shell种子不能在这一步被称为已经重建成等距面。

## 5. 同一个 frame、一个位置和全部周期

现在假设真实 Darboux方程成立，因而 $d\Omega=0$。
在 universal cover上从一个固定点积分
$$
              d\alpha=\Omega,\qquad
              dX=e^{i\alpha}(\omega_1+i\omega_2).
 \tag{T.17}
$$
(T.11) 使第二式闭合：
$d(\omega_1+i\omega_2)=-i\Omega\wedge(\omega_1+i\omega_2)$。
因此 (T.17) 给真正的 $X:\widetilde I\times\mathbb R\to\mathbb C$。
只选择一次初始角 $\alpha_0$ 和一次初始水平位置 $X_0$。

由 (T.16)，$\alpha(a,\theta+2\pi)-\alpha(a,\theta)=2\pi$。
四重周期使更准确的 quarter差为 $\pi/2$。
(T.10) 的系数也为四重周期，因此
$$
                  X(a,\theta+\pi/2)=iX(a,\theta)+b_0
 \tag{T.18}
$$
中 $b_0$ 是整个连通区域的同一个常数：
微分左边减右边在 $a,\theta$ 两个方向都为0。
迭代四次，$1+i+i^2+i^3=0$ 给真正的水平位置周期。
没有每层独立的平移 period，也没有按半径改动旋转中心。

对正高度取空间浸入 $(\Re X,\Im X,z)$，
对北帽的实际约定取 $(\Re X,\Im X,Z_0-z)$。
由 (T.9)--(T.10) 其第一基本形式准确为 $g$。
$g_h$ 正定保证 immersion；整个证明不除以 $Q$。
初始 $X_0,\alpha_0$ 只改变一个共同的平面刚体动作，
不是每片一个新 unknown。

## 6. B 接口的准确 frame 接续

设 B 两侧都已是真实解，目标 metric、$a,w$ 的所需 jets相同，
且使用同一个物理角。若
$$
                  z_-(B,\theta)=z_+(B,\theta),\qquad
                  (z_a)_-(B,\theta)=(z_a)_+(B,\theta)
 \tag{T.19}
$$
包含完整 mean成立，则 $P,K,U,V$ 在 B相同。
(T.10)、(T.12)--(T.13) 的 coframe及连接在 B也相同。
将尾侧的唯一初始 frame/位置取为已经确定的 cap--long侧
在一个固定角上的真实值，(T.17) 沿整个 B圆的 ODE唯一性便使
完整 B曲线、两向切向量与 frame全部相同。

这是将尚待重建的一侧安装到同一个已经给定的 frame；
不是把两个已经各自规定的物理端 frame分别重新归零。
若两个端 frame都被外问题独立指定，它们仍需比较 (T.17) 的
实际 ordered输出，并保作真实 matching行。

最后由 (T.14) 和 $J>0$，同一个 Cauchy pair确定 B的
$K_t$，所以两侧所需二阶高度迹相同；
flat coframe的对应 derivatives亦匹配。
原单侧目标/profile正则只授原来的全局阶数，
更高 derivatives仍按已经记录的 broken jets保留。

## 7. 一个高度规范与未删除的 mean跨度

(T.6) 的 mean是
$$
                 \langle z\rangle_t=aw(1+\kappa).
 \tag{T.20}
$$
所以相同 $\kappa(B)$ 只匹配 mean slope，
还必须用一次真实积分对齐 mean高度：
$$
 \langle z(t)\rangle
  =\lambda+\int_{t_f}^t a(s)w(s)(1+\kappa(s))\,ds .
 \tag{T.21}
$$
G.22--G.24 正是对其修补后的真实费用；
long 的独立 mean-height跨度不乘 $\varepsilon_L$。
一个整体 $\lambda$ 可规范一个真实端的高度；
其余端值都是 (T.21) 的实际输出。

坐标 primitive 的 mean规范、Euclidean frame角 $\alpha$、
principal Γ反项以及空间位置常数是不同对象。
(T.17) 保留完整 $\Omega_a$；不会因为 moving坐标
$\langle\Theta-\mathrm{id}\rangle=0$ 而删除这个真实径向角积分。
物理 $B_0,C_0$ 亦没有由四重周期或 (T.16) 自动置零。
在实际共同反射子类中 $B_0=0$ 是原独立反射定理的结论，
而不是本篇作 frame接续的前提。

## 8. 对当前 fixed-Γ2/Nash 工作线的准确权限

G 构造的种子保同一 $\gamma_1^*$ 与冻结 $\gamma_2^\flat$，
因为 (T.3) 是所有候选 $p$ 上的准确恒等式。
后继 Nash校正一般作用于负分量，须按 E/L 重选同一第一参数值图；
本篇不使该重选消失，也不重授第二参数的值图。

如果后继 augmented迭代真正解出 body residual和 actual
cap--long返回，使 (T.19) 包含全 mean成立，则 (T.17)--(T.21)
给同一个连续且周期的几何重建，没有额外任意的逐层 phase/reset。
所有已有平盘 $C^2$ 极限按原真实物理 jet界接回；不从一个
finite-Sobolev norm独自推新的全层几何极限。

尚未解的帽内 $B(L),C_0(L)$、内height/frame、ν、独立 flux荷或
另外指定的两端位置，不由本定理删除。
它们若属于全局问题的给定条件，仍须在同一个 actual Schur中成立。
本篇只给 (T.19) 一旦成立时的准确、无新规范自由度的 frame接续。

本篇也不把固定第二参数、沿 $\gamma_1^*(u)$ 的设计迭代，
称为整个族保持同一个 metric。若最终要冻结得到的第一参数并构造
一个完整 $\nu$/flex 族，须另付冻结该第一参数后的增广逆和
非线性入口；现有 E/L/B 值图收敛与本 frame 接续不自动提供该结论。
