# R538：预给高度路径的完整四阶矩泛函与真实强准备

日期：2026-11-16。**完整原式与有限区间奇异 ODE 的纸面证明；没有执行数值、求积、符号、profile、秩或开发检查。**

本稿在 [R537](R537-prescribed-finite-height-paths-with-one-gauge-and-complete-history-energy-bounds.md) 的同一真实系统内，把原 $p_1$ 累计的 $O(\delta^4)$ 估计提升为一个准确的四阶系数。母库、全部 copy、右锚、第二规范 $w=0$、原 R534 一次选定的 $\chi^\delta$、实际入端及全部二、三阶历史都保持。这里不把某个局部输入任意当成可指定的矩密度。

关键是两点。第一，必须预给高度的四阶界，才能控制含完整慢历史的强迫项二阶时间导数；R537 仅为能量界使用的 $C^3$ 统一控制本身不够。第二，初值来自一个真正开放的固定 $d$ 解段，因而自动具有足够强的振子准备。由此，实际 $d/\delta^2$ 有统一极限，不再只知道一个量级。

所得单泛函仍含沿整条高度路径累计的 $A_h,T_h$。若它严格为负，就给原 R534 正前缀之后的**真实总 $p_1<0$**；本稿只证明这一准确判据，不把高度和泛函中的强迫量当成两个独立控制，也不预授某个具体负例。其余七矩、frame、位置、period 及全部端 germ 均仍是原联合问题。

## 1. 范围、入端及额外正则性

沿用 R537 的固定母库、有限时长 $T$、合法高度路径 $\bar h$ 和实际拼接高度 $h_\delta$。具体地，
$$
h_\delta(t)=\bar h(t)+\zeta(t)
\{h_\delta^{\rm old}(t)-h_*^{\rm old}(t)\},
\qquad 0\le t\le T,
\tag{1}
$$
其中 $\zeta=1$ 于一个固定初始开放区间，随后为0；$h_\delta^{\rm old}$ 是 R535 的同一真实固定 $d$ 解。$\bar h$ 在该初始区间等于极限解 $h_*^{\rm old}$。全部高度均位于预先固定的正紧区间，并保
$$
h_-\min_{x\in I}(x+\omega_c)>1
\tag{2}
$$
的严格余量。

本稿要求在已固定的有限区间上有
$$
\sup_{\delta}\|h_\delta\|_{C^4([0,T])}<\infty,
\qquad h_\delta\longrightarrow\bar h
\quad\text{于 }C^2([0,T]).
\tag{3}
$$
若使用有限维目标族，则这些界和收敛须在该紧参数盒上一致。原构造取固定 $C^\infty$ 目标及固定 cutoff，由 R535 的正规有限区间 ODE 依赖即可满足(3)。这只是说明原允许选择如何取得本稿所需条件，不把任意仅有 $C^3$ 界的序列升级为(3)。

记
$$
\gamma=h_\delta',\qquad a=h_\delta'',\qquad
\eta=\omega-\omega_c,\qquad d=h\eta-k,\qquad v=d_s.
$$
真实起点来自 R535：
$$
d(0)=d_0^\delta=O(\delta^5),\quad v(0)=0,\quad
j(0)=O(\delta^5),\quad A(0)=O(\delta),\quad T(0)=O(\delta^2).
\tag{4}
$$
在初始开放区间，$d(t)\equiv d_0^\delta$，而不是只在单点令 $v(0)=0$。

所有选择仍按 R537 的顺序：母库、有限高度路径、有限时长和有限导数界先固定，再取小 $\delta$。本稿没有统一控制依赖 $\delta$ 发散的高度、时长或高度导数。

## 2. 必须保留的完整快慢系统

R537 的几何变量
$$
j=\frac{\eta}{h}+\frac d{h^2}
$$
满足
$$
j_s=-\frac{2d\gamma}{h^3},\qquad
\eta=hj-\frac dh,\qquad k=h^2j-2d,
\qquad \upsilon=k_s=2\eta\gamma-2v.
\tag{5}
$$
完整 ruling 给
$$
d_{ss}+\delta^{-2}\alpha(t,d)d=G(t,d,v,Z),
\qquad \alpha(t,d)=\frac{c_k}{C_k(h_\delta(t),d)}>0,
\tag{6}
$$
其中 $c_k=C_k(H,0)>0$，并且
$$
\begin{aligned}
G={}&\frac{
\mathcal F(S,\gamma,2\eta\gamma-2v,A,T)
-\nu_0^\delta(1+d^2)/(2h)-B(h,d)h_\delta''
}{2C_k(h,d)}\\
&+\frac{\eta}{h}\gamma^2-\frac{\gamma v}{h}.
\end{aligned}
\tag{7}
$$
$C_h+2\eta C_k=-B(h,d)$ 是 R521/R535 的完整加速度恒等式。$\mathcal F$ 包含原
$$
R_0+R_2+L_{\rm vel}(AD)-E(AD,AD)-4E(\phi,T(\phi;D))
$$
的真实组合；这里没有删除有序第三项，也没有把累计 $A$ 换成瞬时系数。

R77 的原权三式允许准确定义
$$
\widetilde T=T-P_{\rm acc}(S,\gamma,\upsilon)
+\mathcal A(S)\gamma\upsilon,\qquad
Z=(j,A,\widetilde T).
\tag{8}
$$
原系统变为
$$
d_s=v,\qquad
v_s=-\delta^{-2}\alpha(t,d)d+G(t,d,v,Z),
\qquad Z_s=\mathcal H(t,d,v,Z),
\tag{9}
$$
其中 $G$ 已按(8)恢复真实 $T$。完整慢历史为
$$
\begin{aligned}
A_s={}&\Phi_{M_{\rm raw}},\\
\widetilde T_s={}&-\Phi_{M_{\rm raw}}\circ A+\mathcal C_s^{[1]}
+2\mathcal A h_\delta''\upsilon\\
&+\{(X\mathcal A)\gamma+(Y\mathcal A)\upsilon\}\gamma\upsilon
+\sum_{q=0}^3\mathcal B_q\gamma^{3-q}\upsilon^q .
\end{aligned}
\tag{10}
$$
特别，$\mathcal H$ 中没有 $v_s=d_{ss}$，没有 $k_{ss}$，也没有 $\delta^{-2}$。原 $T$ 的速度势及其两端值仍由(8)完整恢复。

R537 已在同一先固定的有限盒上证明
$$
d=O(\delta^2),\quad v=O(\delta),\quad v_s=O(1),
\quad \|Z\|+\|Z_s\|\le C.
\tag{11}
$$
其全部有限区间存在与顺次历史界可直接使用。本稿只研究这个已存在的真实解，不重建另一条有同名变量的路径。

## 3. 含全部历史的强迫二阶导数

定义
$$
\alpha_0(t)=\alpha(t,0),\qquad
f(t,Z)=G(t,0,0,Z),\qquad
D_\delta(t)=\frac{f(t,Z(t))}{\alpha_0(t)}.
\tag{12}
$$
$f$ 中仍含真实慢 $A,\widetilde T$；$D_\delta$ 也不是外加控制。

因为 $G,\mathcal H$ 的显式时间依赖只用预给 $h_\delta,h_\delta',h_\delta''$，(3)及慢盒使
$$
f,\ f_t,\ f_{tt},\ f_Z,\ f_{tZ},\ f_{ZZ},
\quad \mathcal H_t,\mathcal H_d,\mathcal H_v,\mathcal H_Z
$$
在实际轨道上有统一有限界。这里 $f_t$ 可含 $h_\delta'''$，$f_{tt}$ 可含 $h_\delta''''$；二者均已在(3)中支付。

沿实际解，准确地
$$
f_s=f_t+f_Z\mathcal H,
\tag{13}
$$
$$
\begin{aligned}
f_{ss}={}&f_{tt}+2f_{tZ}\mathcal H
+f_{ZZ}[\mathcal H,\mathcal H]\\
&+f_Z\{\mathcal H_t+\mathcal H_d v
+\mathcal H_v v_s+\mathcal H_Z\mathcal H\}.
\end{aligned}
\tag{14}
$$
(14)只需已经证明的 $v_s=O(1)$；不需 $v_{ss}$ 或任何未付的快高导数。故
$$
|D_\delta|+|D_\delta'|+|D_\delta''|\le C.
\tag{15}
$$
这也是 R537 的完整第三重写不能省略的地方：若直接把原 $T$ 当慢变量，原 $T_s$ 中的 $k_{ss}$ 会使上述证明失去其 stated 输入。

## 4. 强准备来自真实开放固定 $d$ 段

在初始开放区间，实际解具有
$$
d\equiv d_0^\delta,\qquad v\equiv0,\qquad v_s\equiv0.
$$
于是原(6)准确给
$$
G(t,d_0^\delta,0,Z(t))
=\delta^{-2}\alpha(t,d_0^\delta)d_0^\delta .
\tag{16}
$$
由同一盒的光滑性，
$$
G(t,d_0^\delta,0,Z)-f(t,Z)=O(d_0^\delta).
$$
两边乘 $\delta^2$ 并利用(12)，得到
$$
\delta^2D_\delta-d_0^\delta
=\frac{\{\alpha(t,d_0^\delta)-\alpha_0(t)\}d_0^\delta
-\delta^2\{G(t,d_0^\delta,0,Z)-f(t,Z)\}}
{\alpha_0(t)}
=O(\delta^7).
\tag{17}
$$
这里 $(d_0^\delta)^2=O(\delta^{10})$，
$\delta^2d_0^\delta=O(\delta^7)$，两项都保留。

对(17)在该真实开放段微分，$d_0^\delta$ 是常数。原固定 $d$ 支是 R535 中参数
$(d,c,\nu_0,d\nu_1)$ 的正规 ODE，故其有限时间导数一致有界。或者直接用(10)及预给高度界，差
$G(t,d_0^\delta,0,Z)-f(t,Z)$ 的时间导数仍为 $O(d_0^\delta)$，而
$\{\alpha(t,d_0^\delta)-\alpha_0(t)\}'=O(d_0^\delta)$。因此
$$
\delta^2D_\delta'=O(\delta^7)
\tag{18}
$$
于初始段。置
$$
e=d-\delta^2D_\delta,
$$
便得到真正的初始准备
$$
\boxed{e(0)=O(\delta^7),\qquad e_s(0)=O(\delta^7).}
\tag{19}
$$
这比仅指定 $d(0)=O(\delta^5),v(0)=0$ 强。若没有(16)这一真实开放段，不能免费使用(19)。

## 5. 修正振子及统一强收敛

令
$$
b(t)=G_v(t,0,0,Z(t)).
$$
按实际变量作 Taylor 展开，并用(11)，有
$$
G(t,d,v,Z)=f(t,Z)+b(t)v+O(d+v^2).
$$
同时
$$
\delta^{-2}\{\alpha(t,d)-\alpha_0(t)\}d=O(\delta^2).
$$
代入 $d=e+\delta^2D_\delta$，利用(15)，准确得到一个沿实际解成立的方程
$$
\boxed{
e_{ss}-b(t)e_s+\delta^{-2}\alpha_0(t)e
=\mathcal R_\delta(t),\qquad
|\mathcal R_\delta(t)|\le C\delta^2 .
}
\tag{20}
$$
余项包含 $\delta^2(bD_\delta'-D_\delta'')$；它并没有被略去。这里不要求对 $\mathcal R_\delta$ 的快时间导数作统一估计。

取能量
$$
\mathscr E_e=\frac12 e_s^2+
\frac{\alpha_0(t)}{2\delta^2}e^2.
\tag{21}
$$
$\alpha_0$ 有严格正下界，$b,\alpha_0'$ 有统一界，故
$$
\mathscr E_e'
=b e_s^2+\frac{\alpha_0'}{2\delta^2}e^2
+e_s\mathcal R_\delta
\le C\mathscr E_e+C\delta^2\sqrt{\mathscr E_e}.
\tag{22}
$$
用 $\sqrt{\mathscr E_e+\varepsilon}$ 后令 $\varepsilon\downarrow0$，或用等价积分比较，(19)给
$$
\sqrt{\mathscr E_e(t)}
\le C_T\{\sqrt{\mathscr E_e(0)}+\delta^2\}
=O(\delta^2).
$$
所以整个已固定区间上
$$
\boxed{
d=\delta^2D_\delta+O(\delta^3),\qquad
d_s=O(\delta^2),\qquad
e_s=O(\delta^2).
}
\tag{23}
$$
其中 $d_s=\delta^2D_\delta'+e_s$；没有把 $e_s/\delta^2$ 的振动误报为收敛。结论也不授 $d_{ss}=O(\delta^2)$ 或其更高导数小量。

## 6. 极限强迫是完整的单路径泛函

令 $Z_h$ 为(9)在 $d=v=j=0$、$h=\bar h$、
$\nu_0^\delta=\nu_0^0:=\lim_{\delta\to0}\nu_0^\delta$ 下的极限慢系统，取极限真实初值 $A_h(0)=T_h(0)=0$。这正是
$$
S_h=(\bar h,0,\omega_c),\qquad
\gamma_h=\bar h',\qquad \upsilon_h=0
$$
沿原 R73 方程的 canonical 历史：
$$
A_h'=\Phi_{M_{\rm raw}(S_h,\bar h',0)},\qquad
T_h'=-\Phi_{M_{\rm raw}}\circ A_h+\mathcal C(S_h,\bar h',0,\bar h'',0).
\tag{24}
$$
(24)只定义真实字段，不宣称该极限路径本身已经满足完整第四 ruling。$T_h$ 含原速度势。

实际慢系统的输入 $d,v$ 由(23)统一趋零，初始历史由(4)趋零，高度数据由(3)收敛。普通有限区间连续依赖给
$$
Z(t)\longrightarrow Z_h(t),\qquad D_\delta(t)\longrightarrow D_h(t)
\tag{25}
$$
一致成立。具体地，
$$
\boxed{
D_h=
\frac{
\mathcal F(S_h,\bar h',0,A_h,T_h)
-B(\bar h,0)\bar h''
-\nu_0^0/(2\bar h)
}{2c_k}.
}
\tag{26}
$$
这是沿整条 $\bar h$ 的完整 canonical ruling 缺额除以 $2c_k$。分母来自
$\alpha_0=c_k/C_k$，所以没有残留一个误放的 $C_k$。

由(23)(25)，
$$
\frac d{\delta^2}\longrightarrow D_h .
\tag{27}
$$
再把(5)的原积分式除以 $\delta^2$，利用 $j(0)=O(\delta^5)$，得到
$$
\boxed{
J_h(t):=\lim_{\delta\to0}\frac{j(t)}{\delta^2}
=-2\int_0^t\frac{D_h(s)\bar h'(s)}{\bar h(s)^3}\,ds.
}
\tag{28}
$$
因此
$$
\frac{k}{\delta^2}\longrightarrow
\bar h^2J_h-2D_h,\qquad
\frac{\eta}{\delta^2}\longrightarrow
\bar hJ_h-\frac{D_h}{\bar h}.
\tag{29}
$$
所有收敛均在 $[0,T]$ 上一致。$D_h$ 在原初始开放参考段上为0，与(17)的真实准备相容。

## 7. 原 $p_1$ 四阶累计的准确公式

在固定坐标 $y=x+\omega_c$ 中，原 R73/R524 给
$$
M_{p_1}=-kd.
$$
由(27)(29)，得到本稿的主要结论：
$$
\boxed{
\lim_{\delta\to0}\delta^{-4}
\int_0^T M_{p_1}(s)\,ds
=\mathcal P[\bar h]
:=\int_0^T
\{2D_h^2-\bar h^2J_hD_h\}\,ds .
}
\tag{30}
$$
把(28)代入，等价地
$$
\boxed{
\mathcal P[\bar h]
=2\int_0^T D_h(t)^2\,dt+
2\int_0^T\bar h(t)^2D_h(t)
\left\{\int_0^t
\frac{D_h(s)\bar h'(s)}{\bar h(s)^3}\,ds\right\}dt .
}
\tag{31}
$$
本式不作快速相位平均。它来自实际 $d,k$ 的统一强收敛；没有交换一个未证明的振子均值与有序历史。

R534 正前缀的 $p_1$ 为 $O(\delta^7)$，R535 的固定 $d$ 过渡及任意已固定有限入段没有新增 $\delta^4$ 基准。故包含此前同规范真实前缀的总累计也满足
$$
m_{p_1}^{\rm total}
=\delta^4\mathcal P[\bar h]+o(\delta^4).
\tag{32}
$$
特别，若对一条确实按(26)计算的允许高度路径证明
$\mathcal P[\bar h]<0$，则充分小正 $\delta$ 给
$m_{p_1}^{\rm total}<0$。这是一条真实可用的充分判据，而非一个 signed 成本或局部密度的替代。

反过来，只指定某个使(31)为负的抽象函数 $D$ 并不能使用(32)：它必须等于同一高度路径、同一入历史和同一 $\nu_0^0$ 通过(24)(26)产生的 $D_h$。

## 8. 直接可读的符号结构及其边界

若从初始点起高度恒定，则(28)给 $J_h=0$，因而
$\mathcal P=2\int D_h^2\ge0$。所以不能靠一段从零 $J_h$ 起算的常高度路径免费取得负累计。

若某个前段已产生非零 $J_h(t_0)$，随后高度恒为 $h_1$，则该后段上 $J_h$ 恒定，原 integrand 精确改写为
$$
\boxed{
2D_h^2-h_1^2J_hD_h
=2\left(D_h-\frac{h_1^2J_h}{4}\right)^2
-\frac{h_1^4J_h^2}{8}.
}
\tag{33}
$$
它给一个明确的负累计机制：应研究真正的 canonical 缺额
$D_h$ 是否能在同一固定规范下接近这条负密度中心。公式本身并未支付这个控制；$D_h$ 在常高度段仍受完整 $A_h,T_h$ 的有序演化约束。

另一个方便的充分非负条件可以直接由(31)读取。令
$$
(\mathcal V_hD)(t)=\bar h(t)^2
\int_0^t D(s)\frac{\bar h'(s)}{\bar h(s)^3}\,ds.
$$
若这一个固定高度的 $L^2\to L^2$ 算子范数小于1，则
$$
\mathcal P[\bar h]\ge
2(1-\|\mathcal V_h\|)\|D_h\|_{L^2}^2.
\tag{34}
$$
例如可用其 Hilbert–Schmidt 上界
$$
\|\mathcal V_h\|^2\le
\int_0^T\bar h(t)^4
\int_0^t\frac{\bar h'(s)^2}{\bar h(s)^6}\,ds\,dt.
$$
这只是给定高度的一个充分界，不能反推范数较大时存在负例。

## 9. 保留的完整义务

本稿的强收敛只用于原 $p_1=-kd$，没有给所有速度二次矩一个未经证明的四阶平均。真实 $A,T$ 始终按(10)(24)累计，不能因 $k,\eta$ 小便删掉它们。

R537 的另一原矩结论仍然成立：
$$
\int_0^T M_{t_1}\,ds
\longrightarrow
-\frac18\int_0^T
\{1+(\bar h'/\bar h)^2\}\,ds<0.
\tag{35}
$$
因此即便某条后继路径支付(32)的严格负 $p_1$，也没有因此支付 $M=0$。所有其它矩、scalar 末 germ、frame、位置、第四 period、原十三规范和可拼接边界仍须在同一真实词内处理。

本稿没有改已经冻结的母库，也没有在路径中途改 $\chi^\delta$。若后续要从起点另选其它有限 Gram 参数，必须重新说明其原 ruling 项、真实前缀及本稿所用统一界；不能仅把一个新参数填进(26)而沿用旧规范收据。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：原 $p_1$、八矩及完整有序第三累计；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)(2)：完整加速度势和速度三次项；
- [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md)：未消第三历史的完整第四 ruling；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：本稿唯一母库及完整 $C_h,C_k$；
- [R534](R534-real-zero-history-entry-into-negative-matrix-density-and-fixed-gauge-continuation.md)、[R535](R535-fixed-geometric-d-and-uniform-negative-matrix-increment-with-one-gauge.md)：真实开放固定 $d$ 入段、同一规范和实际前缀；
- [R537](R537-prescribed-finite-height-paths-with-one-gauge-and-complete-history-energy-bounds.md)：任意先固定有限高度路径的全段存在、完整慢状态与初步能量界。

全文只作原式纸推，没有新科学执行。
