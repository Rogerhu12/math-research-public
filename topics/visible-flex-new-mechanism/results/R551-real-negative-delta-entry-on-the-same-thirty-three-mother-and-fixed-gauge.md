# R551：同一三十三行母与固定规范上的真实反向入段

日期：2026-11-16。**完整原式纸面证明；没有执行数值、符号、profile、秩或新的科学任务。**

本稿继续 R540/R546/R547 的同一可变母机制。它支付一个此前没有的实际动作：用原完整八矩脉冲改变速度二次曲线的真实中心，再沿同一个正则连通支从正 $\delta$ 接到负 $\delta$，产生一个非零的 $d_c$ 返回增量。全过程保原第二、第三历史、初端势与一次固定的 $\chi$；没有把累计矩阵当成额外控制。

结论有两个明确层次。第一，对一个已经实际到达、满足下述 $W_*>0$ 的入端，给完整可接入定理。第二，在原33行初选中，只细选一个小正参考高度及 R540 原弧的停止时刻，可以实际产生这种入端，同时已有 $k>2$ 和净负 $p_1^{\omega_c}$。第二层是从起点的同一母选择，不是说任意已冻结的 $d_c\approx-2$ 末态都具有该符号。

新段只给一个严格正的返回长度；它没有支付 R547 要求的整个薄层、慢 $t_1$ 恢复、全八矩、末 germ 或 pose。特别，新增速度平方通常继续增加负 $t_1$，该成本下文明确保留。

来源：
[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、
[R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md)、
[R533](R533-complete-velocity-quadratic-form-and-all-history-regular-ruling-coordinates.md)、
[R536](R536-real-negative-total-matrix-density-from-a-complete-fast-height-loop.md)、
[R540](R540-same-positive-null-branch-and-real-large-curvature-with-negative-total-matrix-density.md)、
[R546](R546-real-quadratic-matrix-pulses-and-an-exact-same-gauge-zero-coordinate.md)、
[R547](R547-complete-joint-matrix-cost-and-the-real-return-layer-after-large-curvature.md)。

## 1. 同一个实际状态与原允许域

固定 R533 的真实物理窗口 $I$、右锚、全包名单、原二十目标、四自然约束和共同 $\mathcal F_{\rm path}$。取 $\omega_c>0$，使
$$
x+\omega_c>0\qquad(x\in I).
\tag{1}
$$
使用原速度坐标
$$
\eta=\omega-\omega_c,\quad d_c=h\eta-k,\quad
\gamma=h_s,\quad \delta=k_s/2-\eta\gamma .
$$
原水平关系准确为
$$
h_s=\gamma,\qquad
k_s=2(\delta+\eta\gamma),\qquad
\eta_s=\frac{\delta+\eta\gamma}{h},\qquad
(d_c)_s=-\delta .
\tag{2}
$$
原矩阵仍满足
$$
m_s=M_0(S)+N(S,\gamma,\delta).
\tag{3}
$$
第三、frame 和位置按原恢复积分，不重置任何入值。

本文沿用 R520(4)、R533(1)–(3)的实际定义域：
$$
h>0,\qquad x+\omega>0\quad(x\in I).
\tag{4}
$$
完整原配对中 $Q=1+\{h(x+\omega)-k\}^2>0$。本支没有另加
$h_c(x+\omega_c)>1$。后一类强不等式用于另一母库中两加速度系数的符号，不能移作本稿的原定义域。以下每条真实路径都留在一个预先选定的有限合法盒内；没有令真实高度等于零。

固定原母与 $\chi$ 后，R533 的完整 ruling 是
$$
F(S,m,z)=z^{\mathsf T}H(S)z+l(S,m)^{\mathsf T}z+c_\nu(S,m)=0,
\qquad z=(\gamma,\delta).
\tag{5}
$$
其中 $l$ 对 $m$ 线性，
$$
c_\nu(S,m)=q_S(m)+c_{\nu,0}(S)
$$
保完整二次历史与固定初端势。$H$ 独立于 $m,\chi$。在原合法紧盒内
$$
H_{11}=O(1),\quad
H_{12}=-\Lambda\,\frac{Q_*^3}{64h^7}+O(1),\quad
H_{22}=O(\Lambda),\quad
-\det H\ge c_{\det}\Lambda^2,
\tag{6}
$$
$$
\xi_*=-\omega_c/2,\qquad Q_*=Q(S,\xi_*)>0.
$$
$\xi_*$ 仍仅是多项式读出，不是物理支持点。

## 2. 完整一次历史项中决定反向中心的原坐标

保 R546 的矩阵多项式
$$
\mathcal R_m(x)=m_{r_1}+m_{s_1}x+m_{t_1}x^2,
$$
$$
\mathcal P_m(x)=m_{r_0}+m_{s_0}x+m_{t_0}x^2,\qquad
\mathcal J_m=\mathcal P_m-\omega_c\mathcal R_m,
$$
$$
p_m(x)=m_{p_0}+m_{p_1}x+m_{p_2}x^2,\qquad
m_{t_0}=m_{p_0}/4+m_{s_1}/2.
\tag{7}
$$
对单包写
$$
p=u',\quad r=u'',\quad t=u''',\quad
L_c=p-(x+\omega_c)r,\quad
C=u-xp+x^2r/2.
$$
原 E8 二阶式的局部系数为
$$
A_1=p_m,\qquad A_2=\mathcal R_m-xp_m/2,\qquad
C_{\rm tail}=\mathcal P_m+x\mathcal R_m-x^2p_m/4 .
$$
因此它的完整三导系数满足
$$
\boxed{
\frac{\alpha_m}{2}
=\mathcal R_mL_c-\mathcal J_mr+\frac{p_m}{2}C.
}
\tag{8}
$$
这是原局部系数提取；没有删除右 primitive 或其左值。

令
$$
\mathsf {CL}[P]=\sum_i\lambda_i\int P(x)C_iL_{c,i}t_i^2\,dx.
$$
R533 的完整 principal 是
$$
\sum_i\lambda_i\int\frac Qh
\left\{\frac{\alpha_m}{2}
+\frac{Q(\gamma L_c+\delta r)}{8h^3}\right\}^2t_i^2\,dx.
$$
对 $\gamma$ 取一次项，由(8)准确得到
$$
\boxed{
l_\gamma=
\frac{\mathsf A[Q^2\mathcal R_m]
-\mathsf B[Q^2\mathcal J_m]
+\mathsf {CL}[Q^2p_m]/2}{4h^4}
+l_{\gamma,\rm low}.
}
\tag{9}
$$
这里 $l_{\gamma,\rm low}$ 是完整 $C^2$ 一次历史余项。R520 的共同低阶邻域和 R533 的三导能量给
$$
|l_{\gamma,\rm low}|\le C|m|,\qquad
|\mathsf {CL}[Q^2p_m]|\le C\Lambda |m_p|.
$$
所有相乘多项式次数均不超过6。于是由原
$\mathsf A[P]=O(1)$、$\mathsf B[P]=-\Lambda P(\xi_*)+O(1)$，
$$
\boxed{
l_\gamma
=\frac{\Lambda Q_*^2}{4h^4}\mathcal J_m(\xi_*)
+O(|m|)+O(\Lambda|m_p|).
}
\tag{10}
$$
不能删去最后的 $p_m$ 项；稍后是实际脉冲的 $p_N=0$ 使其在相应归一极限中消失。

同一完整源还给
$$
|l(S,m)|\le C\Lambda |m|,\qquad
|q_S(m)|\le C\Lambda |m|^2.
\tag{11}
$$
这些界由有限完整系数与原能量得到，常数可依先固定的合法盒。固定 $\nu$ 的值留在 $c_{\nu,0}$，不藏进一个对 $\nu$ 一致的界。

## 3. 两个真实矩方向与中心移动的符号

用 R540/R546 的同一个光滑 null frame：
$$
s_H=\sqrt{H_{12}^2-H_{11}H_{22}},\quad D_H=-H_{12}+s_H>0,
$$
$$
b=H_{22}/D_H,\quad \beta=H_{11}/D_H,\quad
n_+=(b,1),\quad n_-=(1,\beta).
$$
其混配为
$$
\kappa_N=n_+^{\mathsf T}Hn_-=-2s_H^2/D_H<0.
$$
完成平方：
$$
z_c=-\frac12H^{-1}l,\qquad
\Delta=\frac14l^{\mathsf T}H^{-1}l-c_\nu,
$$
$$
z=z_c+Xn_++Yn_-,\qquad
F=2\kappa_NXY-\Delta .
\tag{12}
$$
原 $X>0$ 图一直保留全部 $m,\nu$：
$Y=\Delta/(2\kappa_NX)$。

在一个**已经实际到达**的入端 $S_*,m_*,T_*$，取
$$
N_*=N(S_*,n_+(S_*)).
$$
R546 的完整八坐标因子式给
$$
p_j(N_*)=0,\quad
\mathcal J_{N_*}(\xi_*)=-W_*,
$$
$$
\boxed{
W_*=
\frac{b_*(1+d_{c,*}^2-h_*^2\omega_c^2/4)
+2h_*(h_*\omega_c/2+d_{c,*})}{8h_*^4}.
}
\tag{13}
$$
本节的关键入端假设是
$$
\boxed{W_*>0.}
\tag{14}
$$
它不是由 $H$ 不定自动推出的。第7–8节另付一种实际到达它的原初选方式。

沿固定 $S_*$ 的有限矩射线
$$
m=m_*+\tau N_*,\qquad \tau\to+\infty,
$$
将(10)除以 $\tau$，用 $p(N_*)=0$ 得
$$
\frac{l_\gamma}{\tau}
=-\frac{\Lambda Q_*^2W_*}{4h_*^4}+O(1)+o_\tau(1).
\tag{15}
$$
由完整逆矩阵，
$$
(z_c)_\delta=\frac{H_{12}l_\gamma-H_{11}l_\delta}{2\det H}.
$$
结合(6)(11)(15)，
$$
\boxed{
\frac{(z_c)_\delta}{\tau}
=-\sigma_*+O(\Lambda^{-1})+o_\tau(1),\qquad
\sigma_*=\frac{8h_*^3W_*}{Q_*}>0.
}
\tag{16}
$$
该负号来自原 $\mathcal J_N=-W$ 与完整逆矩阵；不是另选一个相反速度或倒走原时间。

## 4. 原二次曲线的投影缺口与同支接入

在固定当前 $S,m$，令 $w_\delta=\delta-(z_c)_\delta$。
把(5)看成关于 $\gamma$ 的二次式，其判别式是
$$
4\{(-\det H)w_\delta^2+H_{11}\Delta\}.
\tag{17}
$$
定义
$$
r_\delta=
\sqrt{\frac{(-H_{11}\Delta)_+}{-\det H}}.
\tag{18}
$$
当 $H_{11}\Delta<0$，实曲线的 $\delta$ 投影是
$|w_\delta|\ge r_\delta$；其它情形不产生投影开缺口。无论
$H_{11}$ 是否为零，区域
$$
\delta>(z_c)_\delta+r_\delta
\tag{19}
$$
内均可从任一实际根沿固定符号的 $F_\gamma\ne0$ 分支继续。
$H_{11}=0$ 时按原线性式处理，不除以它。

由(6)(11)，在上述射线上
$$
\frac{r_\delta}{\tau}
\le \frac{C}{\sqrt\Lambda}+o_\tau(1).
\tag{20}
$$
先在共同初选中取一个充分大但有限的 $\Lambda$，再选有限大
$\tau$，可使
$$
(z_c)_\delta/\tau<-3\sigma_*/4,\qquad
r_\delta/\tau<\sigma_*/4.
\tag{21}
$$
故真实负数
$$
\delta_{\rm new}=-\sigma_*\tau/4
\tag{22}
$$
严格位于(19)，并且到投影边缘有固定的 $O(\tau)$ 正距离。

如果入端速度具有很大的正 $\delta$，则它也位于(19)。沿
$\delta$ 从此正值降到(22)的有限闭区间，取通过该实际速度的同一根，原 $F_\gamma$ 始终非零。这是一条真实二次曲线上的紧正则弧，不是把两份不相接的解拼在一起。即使 $\Delta=0$，该弧也不经过顶点，因为整个弧的 $w_\delta$ 严格为正。

## 5. 矩射线由原正 $X$ 脉冲实际实现

不能把第3节的矩射线当成可自由指定的状态。现使用 R546 的已经付清的真实脉冲。

先固定本次有限 $\tau$。从实际 $X>0$ 入 germ 接到有限大平台
$X=B$，保同一 $\chi$。其平台真时长取 $\tau/B^2$。在
$\upsilon=B^2(s-s_{\rm in})$ 时钟下，完整约化系统是
$$
S_\upsilon=B^{-1}\mathcal B(S)(z/B),\qquad
m_\upsilon=B^{-2}M_0(S)+N(S,z/B),
$$
$$
z/B=n_+(S)+O(B^{-1})
$$
于先固定的有限矩管内。R546 给完整端点收敛
$$
S_B\longrightarrow S_*,\qquad
m_B\longrightarrow m_*+\tau N_* .
\tag{23}
$$
平台末实际 $\delta_B=B+O(1+|m_B|)+O((1+|m_B|^2)/B)$，所以
先固定 $\tau$、再取有限大 $B$，末速度确为正且落在第4节的同一右投影区。

平台前的 ramp 先定有限幅，再取充分短时长；其真实二次矩变化随时长趋零，一同计入(23)。原静态项未删，完整第三项也按真实 smooth 输入恢复。$T$ 可以很大，但有限；不从(23)给它附加不成立的同阶误差界。

严格(21)对小的实际 $(S,m)$ 误差稳定。因此对一个有限的 $B$，
(21)(22)在平台的**真实末态**继续成立。必要时将 $\sigma_*$ 的固定裕量略收小；不重新读取一个未知目标值作为新控制。

然后沿原平台真解短延续，记其实际
$\delta_{\rm old}(s)$。取左开集为1、右开集为0的 smooth cutoff
$\chi_{\rm sw}(s)$，指定
$$
\delta_{\rm in}(s)
=\chi_{\rm sw}(s)\delta_{\rm old}(s)
+(1-\chi_{\rm sw}(s))\delta_{\rm new}.
\tag{24}
$$
这里 $\chi_{\rm sw}$ 只是控制切换函数，绝不是重新选择第三规范
$\chi_\theta$。

利用第4节通过原速度的正则根，解出 $\gamma$，同时积分原
$(S,m)$。在固定有限幅下，把切换长度取足够短，实际状态保持在该紧正则弧的统一邻域，故全程存在且仍满足 $F=0$。左开集与原解完全相同，右开集准确为常输入(22)。因此全部原 germ 平滑接上，没有只匹配速度值而遗漏加速度的拼接问题。

这已在同一个真实前缀上支付了从正 $\delta$ 到负 $\delta$ 的实际过渡。原 $m,T$ 不是射线的理想值，而是(23)(24)产生的真实值。

## 6. 一个非零实际返回增量，及其完整费用

进一步把上述有限选择做成 $\tau\to\infty$ 的族，仅用于证明存在一个统一正的返回长度；最后仍取单个有限 $\tau$。母与 $\chi$ 全程不变。选 $B=B(\tau)$ 足够快增大，ramp 足够短，使新负输入段的实际入值满足
$$
S_{\tau,0}\longrightarrow S_*,
\qquad n_{\tau,0}:=m_{\tau,0}/\tau\longrightarrow N_*.
\tag{25}
$$
这些选择都在(23)的有限参数范围逐次完成，没有让一条实际路径使用无限幅。

置
$$
u=\tau(s-s_{\rm neg}),\qquad n=m/\tau,\qquad
\gamma=\tau v,\qquad \delta=-c\tau,\quad c=\sigma_*/4>0.
$$
因为(5)的次数是完整准确的，除以 $\tau^2$ 后正是
$$
v_z^{\mathsf T}Hv_z+l(S,n)^{\mathsf T}v_z+q_S(n)
+\tau^{-2}c_{\nu,0}(S)=0,
\qquad v_z=(v,-c).
\tag{26}
$$
其关于 $v$ 的导数在(25)的极限点严格非零；这正是第4节的同一投影裕量，未改成一条省略历史的方程。

在该同一分支上解 $v=\mathcal V(S,n,\tau^{-2})$，完整系统成为
$$
S_u=\mathcal B(S)\{\mathcal V,-c\},\qquad
n_u=N(S,\mathcal V,-c)+\tau^{-2}M_0(S).
\tag{27}
$$
在一个先固定的小闭管内，(26)(27)对 $\tau^{-2}$ 光滑且有统一局部界。普通 ODE 连续依赖给一个 $u_0>0$，使所有充分大但有限的
$\tau$ 的实际解存在于 $0\le u\le u_0$。缩小 $u_0$ 可保原合法性、
$k>2$ 及其它原 strict scalar 条件。

由原(2)，在这整个新段上准确有
$$
\boxed{(d_c)_u=c,\qquad
d_{c,\rm out}-d_{c,\rm neg}=cu_0>0.}
\tag{28}
$$
这个增量不随最后选取的充分大 $\tau$ 趋零。它是从实际负输入段的真实入值计起，不把切换中的费用抹去。切换引起的 $d_c$ 变化可再取小于 $cu_0/4$，故整个新后继也有严格正的净返回增量。

原三个 $p$ 列只依赖当前 scalar。在上述固定管内，其新增累计为
$$
\left\|\Delta(m_{p_0},m_{p_1},m_{p_2})\right\|
=O(\tau^{-1})+o_{\rm ramp}(1).
\tag{29}
$$
正 $X$ 预脉冲的相应费用亦可任意小。因此从一个净负
$p_1^{\omega_c}$ 的实际入端开始，可取有限参数使整个新后继仍保
$$
\boxed{\Pi_{\rm out}<0,\qquad k_{\rm out}>2.}
\tag{30}
$$

但原二次矩和 $t_1$ 绝不享(29)：
$$
\Delta m
=\tau\int_0^{u_0}N(S,\mathcal V,-c)\,du+O(\tau^{-1}),
$$
$$
\boxed{
\Delta t_1
=-\tau\int_0^{u_0}\frac{\mathcal V^2}{8h^2}\,du
+O(\tau^{-1}),
}
\tag{31}
$$
并须再加预脉冲和切换的真实费用。该主项非正。第三恢复中
$-M_{\rm raw}\circ A$ 可以产生更大的有限量；它始终按原式积分，本文没有将其归零或与 scalar 小误差混同。

## 7. $W_*>0$ 的同库从起点子类：只在 profile 目标上取辅助极限

现在支付(14)的一种实际来源。不对任意已冻结旧末态宣称它成立。

固定 $\omega_c>0$ 和原物理窗口。把 R533 的三个完整零目标乘以
$64h_c^4$：
$$
\boxed{
64h_c^4q_j(A_c)
=q_j(R_y+h_c^2T_y)=0,\qquad j=0,1,2.
}
\tag{32}
$$
$q_j$ 对其 E8 算子齐次二次，所以(32)是完整恒等，包括原有序尾。
右边在辅助参数 $h_c=0$ 有有限定义；其 principal 是
$4\mathsf A_j$。这里的 $h_c=0$ 仅用来选择有限 profile 目标和有限列，不是几何状态或真实路径。

R533 §4–7 的33维 principal、有限正核与低阶纠正可在这个辅助极限一起选择。理由如下：

- 原二十行及其数值不依赖这个辅助高度；其 $W^2,xW^2$ 两低行也不变。
- (32)在 $h_c=0$ 恰替换为三条非退化的低 $\mathsf A$ 主行，故同一个33阶主 minor 非零。
- 完整低阶余项是同三条 $q_j$ 目标中关于 $h_c^2$ 的有限多项式 $C^2$ 系数，在原共同 $C^2$ 邻域内统一有界。它们仍作为实际目标的完整余项进入有限 IFT，既不删去，也不另假逐母相等；不存在 $h_c^{-1}$ 的新增奇异观察。
- 在该有限列矩阵的一个小闭参数区间上，右逆和严格正核连续保持。原有限 IFT 的正幅盒以及三导能量常数因此可共同选。

于是对某个 $\bar h_c>0$，可以在
$0<h_c\le\bar h_c$ 内分别取实际母，使原20的全部固定值、四约束和共同 cap 保持，且
$$
|\mathsf A_j|\le C,\qquad
\mathsf B_j=-\Lambda\xi_*^j+O(1),\qquad
|\mathsf C_j|\le C(1+\Lambda)
\tag{33}
$$
具有不依赖小 $h_c$ 的 profile 常数。选择顺序仍为一个有限
$h_c$、有限 $\Lambda$、有限正幅盒，最后有限集中频率。没有要求一个固定高频根适用于无界参数。

还用原偶性 $\int prt^2=0$，有
$$
\mathsf A_0=\mathsf W_0-2\omega_c\mathsf D_0+\omega_c^2\mathsf C_0,
\qquad
\mathsf B_0=\mathsf D_0-\omega_c\mathsf C_0,
$$
其中 $\mathsf D_0=\sum_i\lambda_i\int Wr t_i^2$。
消去 $\mathsf D_0$，结合原
$\mathsf W_0,\mathsf A_0=O(1)$、$\mathsf B_0=-\Lambda$，准确得
$$
\boxed{\mathsf C_0=2\Lambda/\omega_c+O(1).}
\tag{34}
$$
此处 $\mathsf D_0=-\sum\lambda_i\int x r_i^2t_i^2$ 也可直接由偶性识别；没有把所有 $\mathsf C_j$ 设成点质量矩。

## 8. 小正高度域中的实际高曲率入端

先选一个固定有限 $d_c$ 区间，例如 $|d_c|\le1$。
在该区间与 $0<h\le\bar h$ 上，真实多项式
$$
Q(S,x)^3=(1+d_c^2)^3+O(h)
$$
对 $x\in I$ 一致成立。由(33)(34)，
$$
\mathsf C[Q^3]
=(1+d_c^2)^3\,\frac{2\Lambda}{\omega_c}+O(h\Lambda)+O(1),
$$
$$
-\mathsf B[Q^3]=\Lambda Q_*^3+O(1).
$$
对每个先固定的正高度下界和有限 scalar 盒，再取 $\Lambda$ 足够大，完整低阶 $H$ 余项也被准确控制。由原 null 斜率公式得
$$
\boxed{
b(S)=\frac1{\omega_c}+O(h)+o_{\Lambda}(1).
}
\tag{35}
$$
$O(h)$ 的常数由(33)统一；$o_\Lambda(1)$ 在所选有限合法盒上一致。先取小的 $\bar h>0$，再取有限大 $\Lambda$，可以保证
$$
0<b_-:=\frac{3}{4\omega_c}\le b(S)
\le b_+:=\frac{5}{4\omega_c},
\tag{36}
$$
以及
$$
b(S)(1+d_c^2-h^2\omega_c^2/4)
+2h(h\omega_c/2+d_c)>0.
\tag{37}
$$
所以整个这个小高度带都有 $W_+(\omega_c/2)>0$。

选择固定小 $\tau_0>0$，使
$b_+\tau_0<\bar h/4$、$\tau_0<1/4$。再选一个充分小的**正**
$h_c$。R536/R540 的真实选择腿在
$L\ll h_c^2$ 后有
$$
h_a=h_c-\sqrt L+O(L)>h_c/2,\quad
d_{c,a}=O(L^3),\quad \eta_a>0,\quad X_a>0.
$$
R540 原 $n_+$ 参考弧满足
$$
h_\tau=b,\qquad (d_c)_\tau=-1,\qquad
(\eta/h)_\tau=1/h^2 .
\tag{38}
$$
故 $0\le\tau\le\tau_0$ 上
$$
h_a+b_-\tau\le h(\tau)\le h_a+b_+\tau,
$$
$$
h(\tau)\eta(\tau)\ge
\frac{(h_a+b_-\tau)^2\,\tau}
{h_a(h_a+b_+\tau)}.
\tag{39}
$$
固定 $\tau_0$ 而使正 $h_c$ 足够小时，右边在 $\tau_0$ 趋于无穷。
于是可以先固定这些有限参数，使
$$
k(\tau_0)=h(\tau_0)\eta(\tau_0)-d_c(\tau_0)>3,
$$
$$
0<h(\tau_0)<\bar h,\qquad
-\frac12<d_c(\tau_0)<0,\qquad W_+(\omega_c/2)>0.
\tag{40}
$$
$\eta$ 的上界虽然可很大，但有限。先用(36)(38)的粗界选一个包含整个参考弧的有限合法盒，随后才在 R533 中选最终 $\Lambda$ 和母。由于 $\eta/h$ 增加且起点 $\eta>0$，全弧的
$x+\omega_c+\eta>0$；没有用改变 $\omega_c\sim h_c^{-1}$ 偷换(39)。

R540 的真实有限正 $X$ shadow 适用于这个先固定的参考弧。其全部原矩阵按真实方程走出，scalar 误差与原三个 $p$ 矩的追加费用可以共同压小。因此在同一个固定母、同一个固定 $\chi$、同一个原起点上，确有一个实际入端满足
$$
\boxed{
k_*>2,\quad \Pi_*<0,\quad X_*>0,\quad W_*>0.
}
\tag{41}
$$
本稿直接使用(41)这个实际入端，并不先假设 R546 的任意单矩归零后仍有 $X>0$：那份脉冲可以大改 $m$，所以 $X$ 的号不能由 scalar 小误差推断。若先支付了该单矩，必须在其真实输出重新核本稿的实际入端条件。下述后继也不保证那个单矩零值继续不变。

(41)是 R540 原允许初选及原弧停止时刻的细选。它一般不等于
R547 为叙述薄层费用而取的 $d_c\approx-2$ 末态，也不赋予一个任意既有末态(14)。选完以后不再改母、不改原20数值、不改 $\chi$。

## 9. 另一份已经实际为负的 $X$ 入端

还有一个不需要(14)的窄实际情形，应与前面区分。若某个同母、同 $\chi$ 的真实 regular 入端已满足 $X_{\rm in}<0$，就可在同一个 $X$ 图内接到 $X=-B$，不跨 $X=0$。

取 $u=B(s-s_{\rm in})$、$n=m/B$。完整速度式给
$
z/B=-n_+(S)+O(|n|)+O(|n|^2)+O(B^{-1})
$
于一个固定的小 $(S,n)$ 管内；初值 $n_{\rm in}=m_{\rm in}/B\to0$。完整系统仍保
$
S_u=\mathcal B(S)(z/B),\qquad
n_u=N(S,z/B)+B^{-2}M_0(S).
$
故在一个统一的小正 $u$ 区间内有 $\delta/B<-1/2$，于是
$d_c$ 有严格正增量。接入 ramp 先定有限幅、后定短时长，原 germ 与全部 history 均保留。原三个 $p$ 矩费用仍为 $O(B^{-1})$，而 $t_1$ 的速度平方费用仍为非正的 $O(B)$。

这一观察只消费一个已经实际存在的负 $X$ 入端。它不说 R540 的正 $X$ 路径可以无费用换号，也不说 R546 的任意目标末态必在这一支上。它使两个真实情形的范围清楚：已有 $X<0$ 时直接小回退；仍在 $X>0$ 且有(14)时，必须使用第2–6节的完整历史中心移动。

## 10. 已闭事实与真正仍欠的返回长度

对(41)这个完整真实入端，第3–6节构造了同一规范的有限光滑后继，使 $\delta$ 真正变负、$d_c$ 有一个非零正增量，同时保净负
$p_1^{\omega_c}$、$k>2$ 和合法几何。每一个矩阵脉冲、切换和负输入段都有原完整方程，不靠 formal 矩方向或未到达的 conic 根。

这是 R547 必要返回动作的实际局部入口，但仍不等于整个返回。统一小管给出的 $cu_0$ 未被证明大于原负 $d_c$ 到 $O(L^9)$ 层的距离，也未证明能无退化地重复到该层。尤其(31)通常继续增加负 $t_1$，所以不能把这一快返回段当成所需的慢正费用区。

下一真正问题是：沿这同一个实际 history 继续控制，使反向增量到达有利的慢区域，并支付新增的全部负矩账。若要跨多个局部管，须逐步保原 $W$ 号、完整投影裕量、合法盒及历史界；本稿不将局部存在自动拼成全局返回。全八矩、第三 period、末 scalar/germ、pose 与最终同一规范仍未完成。

窄核范围：literature只按两原槽核过(9)的系数以及(15)由
$\mathcal J_N=-W$ 得到的符号；完整逆矩阵、投影、真实脉冲接入、辅助高度族与后继范围由本文逐式证明。没有科学执行。
