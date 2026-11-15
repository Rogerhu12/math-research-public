# R768 增补：完整零纤维数据与唯一普通二阶消极

**2026-11-15 范围更正：本篇选定的 r=ell=1、k=0、b0≥3 在原来源中为空。原首层帽强制 3b0+deg Q(0,Y)≤4r+2；r=1时b0≤2。下列条件公式不得记作实际可用窗口；详见[原次数门更正](2026-11-15-r768-original-fiber-degree-feasibility.md)。后续改从未被此门排除的r≥2重做。**

日期：2026-11-15。**状态：本文的实际二维商、指定主部、同来源两输出矩阵和对偶铅笔的最高极消去已证明；指定全球延拓仍未解决。**

本文继续 R768 的同一个实际来源，专取
$$
r=\ell=1,\qquad k=0,\qquad s=2h+1,\qquad
N_0=s-13,\quad T=N_0-1.
\tag{1}
$$
保 R750 的原强接触范围、$p>101$、$f_D<p$、
$P^{\rm fact}=qtF^3$、$q=d^{-C_D}Q$、$d=1+8t$ 和全部十九角。
$P=(0,1)$ 光滑、$e=(\mathcal EF)|_C$、$q_0=q|_C$ 在 $P$ 为单位。
另保 R768 的有限纤维门
$$
b_0=\deg_YF(0,Y)\ge3.
\tag{2}
$$
本篇不另把 R459 已付的 $-2,5,-6$ 首项登记为新结论。

记
$$
\boxed{B=\frac{b_s(0)q_0(0)e(0)^3u(0)^2}{a}\in k^\times,}
\qquad
\eta_0=t^hu,\quad t^s=p\epsilon b_s,\quad a\in\mathcal O^\times.
\tag{3}
$$
这是原固定数据，不是新的自由参数。

## 1. 整个有限零纤维的实际二维商

沿用 R750/R766 的准确序列
$$
0\longrightarrow H^0(C,\mathcal N^3)
\longrightarrow\mathcal U_D
\longrightarrow\mathcal V_{E'}\longrightarrow0,
\qquad
\mathcal N=\mathcal O_C(C).
\tag{4}
$$
实际 $u\in\mathcal U_D$ 以同一个
$$
u=R|_C/(q_0t),\qquad R\in\overline{\mathcal W}_D,\quad R(P)=0
\tag{5}
$$
表示；低值右逆的完整高尾仍按 R766 处理。

设 $Z_0$ 为 $t=0$ 中全部有限 $Y$、除 $P$ 外的 Cartier 纤维部分。
其长度为 $b_0-1$，并且 $Z_0\le E'$。
它包括全部非约化交点；不要求其它根简单。
在这个有限开集，$E'$ 的局部方程是同一个 $q_0t$。
因此原主部空间有准确的最高 $t$ 极层
$$
\mathcal P_{E'}\longrightarrow
\mathcal P_{E'}/\mathcal P_{E'-Z_0}
\simeq\mathcal N^3(E')|_{Z_0},
\quad
\mathcal P_A=\mathcal N^3(A)/\mathcal N^3 .
\tag{6}
$$
使用原仿射框乘 $q_0t$，(6) 读取的正是 $R\bmod t$。
这里不把 $q_0$ 当函数单位：即使它在其它点有零，
$1/(q_0t)$ 仍是相应扭曲线束的合法局部框。

写
$$
F_0(Y)=F(0,Y)=c_0(Y-1)V_0(Y),
\qquad V_0(1)\ne0.
$$
在该框下，$Z_0$ 的坐标代数是 $k[Y]/V_0$。
原 $A_n=\lfloor(n+1)/4\rfloor$ 使每个原来源准确满足
$$
R(0,Y)\in k[Y]_{\le2}.
\tag{7}
$$
(5) 又给 $R(0,1)=0$。
定义
$$
\mathcal L_2=\{A(Y-1)+C(Y-1)^2:A,C\in k\}.
$$
因 $\deg F_0\ge3$，$\mathcal L_2\to k[Y]/V_0$ 单射：
一个核多项式既被 $V_0$ 整除又在 $Y=1$ 为零，
便被次数至少三的 $F_0$ 整除，只能为零。

令
$$
\mathcal W_D^{[t]}
=\overline{\mathcal W}_D\cap t\,k[t,Y,d^{-1}],
\qquad
\mathcal V_t=
\operatorname{pp}_{E'}\!
\left\{\frac{R|_C}{q_0t}:R\in\mathcal W_D^{[t]}\right\}.
\tag{8}
$$
这是原全来源中的实际子空间，不是环境主部的核。

**定理 1。** 最高 $t$ 极层给准确短正合列
$$
\boxed{
0\longrightarrow\mathcal V_t
\longrightarrow\mathcal V_{E'}
\xrightarrow{\ \pi_0\ }\mathcal L_2
\longrightarrow0.
}
\tag{9}
$$

证明如下。若实际主部的 (6) 为零，则 $R(0,Y)$ 在 $V_0$ 上为零；
由 (7) 和 $R(0,1)=0$，上述单射迫 $R(0,Y)=0$，
即同一个 $R$ 属于 $\mathcal W_D^{[t]}$。
反向显然。
增加 (4) 的三倍截面，可用原 $qtH_3$ 作代表，仍被 $t$ 整除；
因此这个核不依赖代表。
而原实际两列组合
$$
R_{\rm lin}=Y-1,\qquad
R_{\rm quad}=1-2Y-Y^2q_2(t),\qquad
q_2=(t-1)/d
\tag{10}
$$
分别给 $Y-1$ 和 $(Y-1)^2$。
$n=0,1,2$ 的原帽支付 (10)，故 (9) 满射。
这也证明两个方向都是真实方向，不能被一个任意环境补列替代。

特别，$\dim\mathcal V_{E'}\ge2$。
这个比 R766 的单个单位更强的结论来自真实原列，而非维数猜测。

## 2. 完整首次修正指定整个二维投影

在值已消到 $r=1$ 的来源上，两个常数 normal 泛函为
$$
d_1(\operatorname{pp}u)=(\mathcal ER)(P),\qquad
d_2(\operatorname{pp}u)=(\mathcal E^2R)(P).
\tag{11}
$$
由 (9)，它们定义良好，并且
$$
\pi_0(v)=A(Y-1)+C(Y-1)^2
\quad\Longrightarrow\quad
d_1(v)=A,\quad d_2(v)=A+2C .
\tag{12}
$$
它们都杀 $\mathcal V_t$，联合秩准确为二。

若同一个实际 $R$ 使
$$
M(P^{\rm fact}+pR)\in p^2
\tag{13}
$$
成立，剥去整个原 $c_*U_0$、仍保 $w^{13}$ 后：
第一 normal 常数 forcing 为零；
第三块第 $13$ 行的 forcing 为 $3a^2B$。
因此同一个 $R$ 必须满足
$$
d_1=0,\qquad (a^2/2)d_2=-3a^2B.
$$
结合 (12) 得
$$
\boxed{\pi_0(\operatorname{pp}u_R)=-3B(Y-1)^2,}
\tag{14}
$$
以及更强的原多项式等式
$$
\boxed{R(0,Y)=-3B(Y-1)^2.}
\tag{15}
$$
这里仅用完整 $M$ 的首次 $p^2$ 条件；
不需要将其误升成相对 $J$ 的 $p^2$ 条件。

对 $Z_0$ 上任一几何点，$Y-1$ 为单位。
故 (15) 还强迫 $R|_C$ 在该处为单位。
在正规化的每个相应支 $Q$ 上，准确有
$$
\boxed{\operatorname{pole}_Q(u_R)=v_Q(q_0)+v_Q(t).}
\tag{16}
$$
这个等式包括 ramified 纤维和奇点支。
若 $q_0$ 在整个 $Z_0$ 为单位，则 (14) 指定那里的**全部**主部；
一般情形指定 (6) 的完整最高 $t$ 极层，并强迫 (16) 的满极阶，
但 $q_0$ 自身较低的主部仍可变化。

## 3. 唯一固定列的全部高尾及原核

记 $v_{\rm quad}$ 为 (10) 的真实主部。
因 $q_2+1=9t/d$，其完整归一值为
$$
\boxed{
u_{\rm quad}
=\frac{( \psi-1)^2}{q_0t}
-\frac{9\psi^2}{q_0d},
\qquad u_{\rm quad}(P)=-9/q_0(P).
}
\tag{17}
$$
第一 normal 的完整曲线值为
$$
\boxed{
(\mathcal ER_{\rm quad})|_C
=2\psi(\psi-1)-18t\psi^2/d.
}
\tag{18}
$$
这些高尾均保原 $\psi,q_0,d$，不能只用零纤维二次式代替。

(15) 准确等价于
$$
\boxed{R=-3B R_{\rm quad}+R_t,\qquad
R_t\in\mathcal W_D^{[t]}.}
\tag{19}
$$
因此 R766 的值加**两条**常数 normal 条件可解，当且仅当
$$
\boxed{
\mathcal O_T(v_{\rm quad})\in
\mathcal O_T(\mathcal V_t).
}
\tag{20}
$$
这是一个比只用 $\ker d_2$ 更窄的实际成员性问题。
从 (20) 回到来源时，仍只减原 $qtH_3$；
它在 $\mathcal W_D^{[t]}$ 中，不改变 (14)。
故 (20) 的充分性也保持同一个实际来源。

还有完全显示的全 first-normal 后续矩阵。
令 $\mathcal S_D=t^{-1}\mathcal W_D^{[t]}$，这只是 (19) 的实际商，
**不是**声称可免费对整个 $\mathcal W_D$ 除 $t$。
其完整整基为
$$
\boxed{
\begin{cases}
Y^nq_n\,\mathcal O[t]_{\le e_{n+1}-1},&n=0,1,2,\\
Y^n(q_n/t)\,\mathcal O[t]_{\le e_{n+1}},&n\ge3 .
\end{cases}}
\tag{21}
$$
$d$ 分母、全部角和每个上帽都由这一个等式保留。

对 $\beta=M(P^{\rm fact})/p\bmod p$，在原短三块中写其读数为
$(0,\beta_1,\beta_2)$，其中 $\beta_2=3a^2B$。
原 $P^{\rm fact}\in\ker\bar J$ 保证 $\beta$ 在两条十三行 carry 位置为零；
这不是另删掉两个条件。
代入 $R_t=tS$，整个原 first-lift 方程准确化为
$$
\boxed{
\begin{aligned}
S(t,g)_{<N_0-1}
&=\left[\frac{3B R_{\rm quad}(t,g)}t\right]_{<N_0-1},\\
(\mathcal ES)(t,g)_{<N_0-1}
&=\left[
\frac{3B(\mathcal ER_{\rm quad})(t,g)}t
-\frac{\beta_1}{a t}
\right]_{<N_0-1},
\qquad S\in\overline{\mathcal S}_D .
\end{aligned}}
\tag{22}
$$
三个已消的常数行都在 (15) 中支付。
(22) 的两个右端确实整：$R_{\rm quad}(0,1)=
(\mathcal ER_{\rm quad})(0,1)=0$，而 $\operatorname{ord}\beta_1\ge h>0$。
仍使用原 $t=t(w)$ 的完整单位变换。
$\beta_1$ 的 native $\xi$ 与原 carry 高尾全部保留。

(22) 是对原同一个 $R$ 的全部剩余模 $p$ 方程，
没有给两个输出分别选不同来源。
它没有被证明满射或不含所示右端。
进入下一位时仍须使用 (19) 的原整 $R$，
恢复完整 $J$、两条十三行和同一个 $d_2$；
本篇不把模 $p$ 的除 $t$ 行消元当成整目标上的自由共轭。

## 4. 全球对偶不必固定为单个 d₂

由 (9)，$\mathcal V_t^\perp=\operatorname{span}\{d_1,d_2\}$。
有限维对偶给：
(20) 失败，当且仅当存在
$$
\omega\in\mathcal D_T
=H^0(C,\omega_C\mathcal N^{-3}(TP))
$$
使
$$
\boxed{
\mathcal O_T^*\omega=d_2+\lambda d_1
\quad\text{对某个 }\lambda\in k.
}
\tag{23}
$$
证明是对 $\mathcal O_T(\mathcal V_t)$ 的 annihilator 配对：
其在 $v_{\rm quad}$ 上非零恰等价于 $d_2$ 的系数非零，
再按这个系数归一化。
因 $d_1(v_{\rm quad})=0,d_2(v_{\rm quad})=2$，
所用归一始终合法。

一旦 (23) 成立，R766 同一个低值右逆给真正的全 $M$ 左行。
它对原 forcing 的值为 $6B\ne0$，
因为第一 normal 常数 forcing 为零，第二为 $6B$。
因此 (23) 的任一实际解都给完整首次 Bockstein 非零。
本篇未证明它有解。

## 5. 对偶铅笔中唯一可付的最高 Y 极消去

现在把 (23) 的局部数据写成实际微分。
用 R768 的 monic
$$
W_0(Y)=F_0(Y)/c_0,\qquad
L(Z,Y)=\frac{W_0(Z)-W_0(Y)}{Z-Y},
$$
定义
$$
K_1(Y)=\left.Z\partial_ZL\right|_{Z=1},
\qquad
K_2(Y)=\left.(Z\partial_Z)^2L\right|_{Z=1}.
$$
它们分别表示 (11) 的两个真实有限纤维泛函。
两者的最高 $Y^{b_0-2}$ 系数都准确为一。
因此
$$
\boxed{
\deg(K_2+\lambda K_1)\le b_0-3
\quad\Longleftrightarrow\quad \lambda=-1.
}
\tag{24}
$$
在这个唯一值，
$$
\boxed{
K_{\rm ord}=K_2-K_1
=\left.\partial_Z^2L\right|_{Z=1},
\quad
\deg_YK_{\rm ord}=b_0-3,
\quad [Y^{b_0-3}]K_{\rm ord}=2.
}
\tag{25}
$$
$p>101$ 保这个顶系数为单位；
$b_0=3$ 时它就是非零常数。
这就是原 $E^2-E=\partial_Y^2$ 在 $Y=1$ 的普通二阶行。
没有加入新观测；只使用同一个原 first-normal 常数行，其 forcing 为零。

同 frame 的局部代表为
$$
\boxed{
\omega_{\rm ord}
=q\,c_0K_{\rm ord}(Y)\frac{dt}{F_Y}.
}
\tag{26}
$$
它在 $P$ 正则，在其它有限零纤维按完整相对留数读取。
原普通二阶 forcing 仍为单位 $6B$。

对任一原正规化边界支 $Q$，若 $v_Q(Y)<0$，
因为 (25) 的全部系数为常数、顶系数非零，
相比单独 $K_2$ 的代表准确有
$$
\boxed{
v_Q(\omega_{\rm ord})-v_Q(\omega_2)=-v_Q(Y)>0
}
\tag{27}
$$
（同一线束框、同一个 $q,F_Y,dt$）。
所以这一步在每个 $Y$ 有极的原边界支确实少了一份 $Y$ 极阶，
不是仅作 formal degree 计数。

其它原角以及 $Y$ 无极的无穷远支不能据 (27) 自动改善。
其完整极除子仍须按 R768 的
$$
\operatorname{div}(e^3\omega_{\rm ord})+\Delta_C-3\pi^*D_e
\tag{28}
$$
逐支读取，保原十九角和 conductor。
(24) 还说明：在这两条既有常数 normal 行的铅笔内，
最高次再降低一阶已不可能；
不得额外使用一个并未杀掉 forcing 的新行。

(26) 本身仍不等于一个 $\mathcal D_T$ 截面。
全球问题继续是 (23) 的实际限制像；
$\lambda=-1$ 是已经支付一份边界消极的候选，
不是说它必定是全球可延拓的参数。

本增补把原其它 normal 的一个完整条件纳入，
指定全部有限零纤维最高主部，并保留 (22) 的同来源全高尾。
剩余全球延拓、(22) 指定两输出的实际像，以及下一位同 $R$ 均未关闭。

依赖：[R768](../results/R768-finite-fiber-normal-residue-and-original-global-pole-divisor.md)；
[R766](../results/R766-actual-principal-part-normal-functional-and-specified-small-obstruction.md)；
[R750](../results/R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R459](../results/R459-actual-angular-content-and-padded-cubic-first-lift.md)。
