# R973 — 原 degree130 的完整算术谱与固定 E260 的秩二下界来源

日期：2026-11-26 UTC。**已证明：原22维空间的全部有限 Weil 类型及其全局 Hecke 角色；其中新固定曲线 $E_{260}:y^2=x^3+260$ 的有理秩至少二、全部局部 Schwartz、同一全权平方和通常全 Selmer 桥；同次原全390计算实际给 $\Pi_{260}\mathscr H_{130}=\Phi_{260}/81\ne0$。** 原 R971 六 sigma 候选在此新线上恰为零。四个真正非 $\mu _6$ 的二维块在 $\mathscr H_{130}$ 中也都非零，不能将完整余项统称为另一条有理 CM 椭圆曲线来源。本篇不声称无穷多个 $p$ 的中央导数已非零。

始终沿用 R970 的 $K=\mathbf Q(\omega)$、$\delta=1+2\omega$、$\operatorname {Im}\delta>0$，及其加性角色、极化和全部 sigma frame。为固定十二次根的方向，置
$$
 \zeta _6=-\omega,\qquad \zeta _{12}=e^{-\pi i/6};
 \quad\zeta _{12}^2=\zeta _6,\quad\zeta _{12}^4=\omega^2.
 \tag{1}
$$
这里尤其不能把最后一项改成 $\omega$。

## 1. 完整有限模型，而非两好位的角色猜测

标准主型空间为
$$
 V_{130}=\sigma^{130}x^2K[X]_{\le21},\qquad X=x^3,
 \qquad\dim_KV_{130}=22.
 \tag{2}
$$
第21次 $X$ 是质量列。它来自整个130维 theta 表示的几何 $\mu _6$ 不变部分；本节先处理完整有限表示，最后才读取这22列。

R970 的 CRT 与标准 Fourier 相位
$d_n=a_n\zeta _{520}^{-n^2}$ 给
$$
 H^0(\mathcal O(130O))\simeq W_2\otimes W_5\otimes W_{13},
 \qquad\dim(W_2,W_5,W_{13})=(2,5,13).
 \tag{3}
$$
二处以 $f_A=e_0-e_2,f_B=e_1+e_3$ 为基，R290(23) 的实际算子
$M_\omega$ 的两个特征向量是
$$
 v_\epsilon=(1,t_\epsilon,-1,t_\epsilon),\qquad
 t_0=(1+\sqrt3)/\sqrt2,\quad
 t_1=(1-\sqrt3)/\sqrt2,
 \quad M_\omega v_\epsilon=\omega^\epsilon v_\epsilon.
 \tag{4}
$$
二处的 $g_*$ 和 $-1$ 固定这两列，外支撑的相消是 R290 的完整生成元积分，不另换四陪集 frame。

五处取 $g_5=-\omega$ 为 $T_5=\mathbf F_{25}^1$ 的生成元。
十三处分裂参数仍为 $t=x+6y\in\mathbf F_{13}^{\times}$，以2为生成元。定义
$$
 \tau_a(g_5)=\zeta_6^a,\qquad
 \tau_b(2)=\zeta_{12}^b.
 \tag{5}
$$
对 R970(15),(20) 的全部实际矩阵求迹，非中央元的对角二次 Gauss 和给
$$
 \operatorname {Tr}W_5(g)=6\mathbf1_{g=1}-\tau_3(g),\qquad
 \operatorname {Tr}W_{13}(t)=12\mathbf1_{t=1}+\tau_6(t).
 \tag{6}
$$
例如中央 $-1$ 两边的迹都为1；在单位元处分别为5和13。非中央项直接将矩阵指数中的 $a=b$ 合并为 $2(x-1)a^2/y$，应用完整一维 Gauss 和，再用 $x^2+3y^2=1$ 化简，即给 (6)。因此五处仅缺 $a=3$，其余五个角色各一次；十三处十二个角色均出现，只有 $b=6$ 出现两次。

几何 $-1$ 在张量 (3) 上的值为 $(-1)^{a+b}$。几何 $\omega$ 用实际环面元 $\omega^2$，三个局部值依次为
$\omega^{2\epsilon},\omega^{2a},\omega^{2b}$；十三处用到了
$\omega^2\mapsto3=2^4$。所以全部合法标签恰为
$$
 \boxed{a\ne3,\quad a+b\equiv0\pmod2,\quad
 a+b+\epsilon\equiv0\pmod3,\quad
 \epsilon\in\{0,1\},\ a\bmod6,\ b\bmod12.}
 \tag{7}
$$
它们有20个，$(\epsilon,a,b)=(0,0,6),(1,2,6)$ 各多一次，合计22维。没有删除质量或先假定全谱只含六次根。

### 1.1 每个标签的完整全局角色

令 $\lambda_{13}:\mathbf F_{13}^{\times}\to\mu_{12}$ 满足
$\lambda_{13}(2)=\zeta_{12}$，固定
$\pi=4+\omega,\bar\pi=3-\omega$。对 (7) 的每个标签，单位化 Hecke 角色的无穷型及全部坏单位为
$$
\begin{array}{c|c}
v&\chi_v\text{ 在单位上的值}\\ \hline
\infty&(z/|z|)^{-1}\\
2&\operatorname {Teich}_{\mu_3}(u)^{1+\epsilon}\\
3&u\bmod\delta\in\{\pm1\}\\
5&(u\bmod5)^{4(a+3)}\\
\pi&\lambda_{13}(u\bmod\pi)^{6-b}\\
\bar\pi&\lambda_{13}(u\bmod\bar\pi)^{b-6}.
\end{array}
\tag{8}
$$
五处的 $a+3$ 是 Hilbert90 与 quadratic splitting 的差，十三处的 $6-b$ 也保留同一差；不能将有限 Weil 角色本身当成算术单位角色。

绝对 uniformizer 值是
$$
 \chi_2(2)=\chi_5(5)=-1,\qquad \chi_3(\delta)=-i,
 \tag{9}
$$
以及明确的主 idèle 公式
$$
 \chi_\pi(\pi)=\frac{\pi}{\sqrt{13}}
 \bigl(\chi_2(\pi)\chi_3(\pi)\chi_5(\pi)
             \chi_{\bar\pi}(\pi)\bigr)^{-1},
 \tag{10}
$$
另一支由同样的共轭公式给出。式 (8)–(10) 因而规定了非紧13参数，并非只规定紧环面。

说明这些数据确实粘成一个角色：在全局单位 $\omega$ 上，2、5和两13的乘积是
$\omega^{1+\epsilon+a+b}$，无穷分量是 $\omega^2$；第一项的指数用到了
$\lambda_{13}(9)^{6-b}\lambda_{13}(3)^{b-6}=\omega^b$。
它们的总乘积由 (7) 为1。全局 $-1$ 的乘积也由 (7) 为1。
类数一于是将 (8) 唯一延拓为全局角色，uniformizer 的 (9)–(10) 正是该延拓。
特别 $\chi_5(\delta)=-(-1)^a$，两13分量在 $\delta$ 上的乘积是 $(-1)^b$；主 $\delta$ 的积关系给 (9) 的 $-i$。

这些角色满足 $\chi|_{\mathbf A_{\mathbf Q}^{\times}}=\epsilon_{K/\mathbf Q}$。
其局部 epsilon 依次为
$$
 \epsilon_2=1,\quad\epsilon_3=-i,\quad
 \epsilon_5=(-1)^a,\quad
 \epsilon_{13}=(-1)^b,\quad\epsilon_\infty=i.
 \tag{11}
$$
五处的证明是：对任何非平凡而在 $\mathbf F_5^\times$ 上平凡的角色 $\vartheta$，按 $z=x+y\delta$ 的 $x$ 分纤维，完整负加性 Gauss 和等于 $5\vartheta(\delta)$；再乘 $\chi_5(5)=-1$。十三处两 split epsilon 的乘积为 $\chi_\pi(-1)=(-1)^b$。二处的两种非平凡三次剩余角色都有同一个 Gauss 和2，三处是 R290 的 $i\sqrt3$。式 (7) 给全局根数 $+1$。

epsilon 乘 $\chi_v(\delta)$ 后的 dichotomy 在 $2,3,5,13,\infty$ 上始终为
$(+,-,-,+,+)$，故所有这些类型用同一
$$
 \alpha=5/13,\qquad\kappa=15\sqrt3/13.
 \tag{12}
$$
若 $b\ne6$，导子恰为 $(130\delta)$。若 $b=6$，两个13角色均未分歧，primitive 导子是 $(10\delta)$；level130 中的重数二是同一全局角色的两个旧向量，绝非两个新 Hecke 角色。

### 1.2 完整 theta-group 交织确定好位算子

取 $\gamma_7=3+\omega,\gamma_{19}=4+\delta$ 及
$\mathscr N_\gamma=[\gamma]_*[\bar\gamma]^*/\gamma$。
这里用整个 Heisenberg 群，而非从一条候选来源推断其他列。若 $R(v)$ 是由标准 Fourier 相位 (3) 固定的 theta 平移提升，则原 sigma division 比
$r_\gamma=\sigma(\gamma z)/\sigma(z)^{N\gamma}$ 与完整纤维重排给
$$
 \mathscr N_\gamma R(v)\mathscr N_\gamma^{-1}
       =R((\gamma/\bar\gamma)v).
 \tag{13}
$$
具体地，在 $[\gamma]$ 的纤维中把 $y$ 换成
$y+\bar\gamma^{-1}v$，其像 $z$ 换成
$z+\gamma\bar\gamma^{-1}v$；$r_{\bar\gamma}/r_\gamma$ 的全部载体正好运输 theta 平移的双线性 cocycle。标准 $d_n=a_n\zeta_{520}^{-n^2}$ 已将二次 cocycle 固定，故等式在提升群本身成立，不只是对底层130挠点成立，也不留下一个未知挠平移。除数 $\gamma$ 两边相同。

(13) 与 (3) 的完整绝对不可约性说明算子与局部有限 Weil 张量只差一个共同标量。实际局部比值 $\gamma/\bar\gamma$ 在2、5、13处分别为
$$
 \gamma_7:\ (\omega,-1,2),\qquad
 \gamma_{19}:\ (1,\omega^2,8).
$$
R970 已从独立 Schwartz 全平方证明 $E_{65^3}$ 的真实值为 $(\omega,-1)$，其标签 $(0,0,0)$ 的三个有限 Weil 值均为1。这将两个共同标量固定，得到整个空间上的准确等式
$$
 \mathscr N_7=\omega M_\omega\otimes W_5(-1)\otimes W_{13}(2),
 \qquad
 \mathscr N_{19}=-I\otimes W_5(\omega^2)\otimes W_{13}(8).
 \tag{14}
$$
所以每个 (7) 的全部特征值为
$$
 \boxed{\lambda_7=\zeta_{12}^{\,8-4\epsilon-6a+b},\qquad
 \lambda_{19}=\zeta_{12}^{\,6+4a+3b}.}
 \tag{15}
$$
直接把 (8)–(10) 代入
$\psi((\gamma))/\gamma=\prod_{v\mid130\delta}\chi_v(\gamma)^{-1}$
也给 (15)。这里全局角色先由全部坏位规定，(15) 是其结果。

## 2. 全部有理 j=0 曲线类型及真正非六次块

当 $a,b$ 都为偶数，定义
$$
 r\equiv a+3\pmod6,\quad r\in\{1,3,5\},\qquad
 s\equiv3-b/2\pmod6,\quad0\le s\le5,
 \quad d=2^{2\epsilon}5^r13^s.
 \tag{16}
$$
(7) 等价于 $r+s+\epsilon\equiv0\pmod3$，从而 $d\equiv-1\pmod9$。
Silverman–Stange 的原六次剩余公式给 $E_d:y^2=x^3+d$ 的全部角色正是 (8)。五、十三处分别由 $v_5(d)=r,v_{13}(d)=s$ 的 tame 六次角色给出；二处奇单位部分为 $1\pmod4$，在未分歧二次域 $K_2$ 中为六次幂，而 $2^{2\epsilon}$ 给所示 Teich 指数。三处 $d/17\equiv1\pmod9$ 是 $\mathbf Q_3$ 中六次幂，故为同一导子一类。由类数一及全局单位相容，全部 uniformizer 也同 (9)–(10)，不是只核两个好位。

R976 的因子编号 $j=0,\ldots,5$ 指 $U-\zeta_6^j$。完整表为：

| $(\epsilon,a,b)$ | $(i_7,i_{19})$ | $d$ | $K$ 维数 | 算术范围 |
|---|---:|---:|---:|---|
| $(0,4,2)$ | $(5,2)$ | $845$ | 1 | primitive |
| $(0,4,8)$ | $(2,5)$ | $1856465$ | 1 | primitive |
| $(0,0,6)$ | $(1,0)$ | $125$ | 2 | 同一角色的13-old 两拷贝 |
| $(0,0,0)$ | $(4,3)$ | $274625=65^3$ | 1 | R970，秩恰二 |
| $(0,2,4)$ | $(0,1)$ | $40625$ | 1 | primitive |
| $(0,2,10)$ | $(3,4)$ | $89253125$ | 1 | primitive |
| $(1,4,4)$ | $(4,5)$ | $260$ | 1 | 本篇，秩至少二 |
| $(1,4,10)$ | $(1,2)$ | $571220$ | 1 | primitive |
| $(1,0,2)$ | $(3,0)$ | $84500$ | 1 | primitive |
| $(1,0,8)$ | $(0,3)$ | $185646500$ | 1 | primitive |
| $(1,2,6)$ | $(5,4)$ | $12500$ | 2 | 同一角色的13-old 两拷贝 |
| $(1,2,0)$ | $(2,1)$ | $27462500$ | 1 | primitive |

这里的二维是 theta 重数，不能写成 Mordell–Weil 秩。将 $d$ 换成 $-27d$ 只给同一 $K$ 同构类及有理三同源类，不另算一条新的算术来源。

其余八个标签的 $a,b$ 都为奇数。共轭 $b\leftrightarrow b+6$ 配成四个 $K$ 二维块；R976 的编号6、7、8分别是 $U^2+1,U^2+\omega,U^2+\omega^2$：

| 标签 | $(i_7,i_{19})$ | $K$ 维数 |
|---|---:|---:|
| $(0,1,5),(0,1,11)$ | $(7,7)$ | 2 |
| $(1,1,1),(1,1,7)$ | $(8,7)$ | 2 |
| $(0,5,1),(0,5,7)$ | $(6,8)$ | 2 |
| $(1,5,3),(1,5,9)$ | $(7,8)$ | 2 |

这些角色在13单位上的值真正含十二次根，且其 $\lambda_7\notin\mu_6$。对任何 $\mathbf Q$ 上的 j=0 曲线，六次剩余式必给
$\psi_d((\gamma))/\gamma\in\mu_6$；故上述四块不能是另一条有理 j=0 椭圆曲线的来源。这个排除使用了完整局部角色，(15) 的非六次值还给出一个独立必要性检查。

维数相加为 $14+8=22$。实际全81块运算与本表逐项一致，并给四个非六次块的 $\mathscr H_{130}$ 投影全部非零、原 $F_{130}$ 投影全部为零。因此
$\mathscr H_{130}$ 的余项不能只按本表的十二条有理曲线重命名。

两个13-old 块中，好位作用在同一算术角色的两拷贝上相同；即使再加任意多个好位，也不会区分它们。选择非紧13向量或给两条真实退化映射之前，不给其任意质量零向量套用一个新的 primitive 中央。

## 3. 新固定 E260 的两个独立有理点

固定
$$
 E_{260}:y^2=x^3+260,\qquad P=(4,18),\quad Q=(-4,14).
 \tag{17}
$$
它们确在原曲线上。用 $F=\mathbf Q(r),r^2=65,r>0$，定义
$\Delta(x,y)=[y+2r]\in F^\times/F^{\times3}$、$\Delta(O)=1$。
R959 §2 的同一原弦恒等式在这里是
$$
 \prod_{i=1}^3(y(R_i)+2r)=(n+2r)^3,\qquad
 (y+2r)(-y+2r)=-x^3;
 \tag{18}
$$
第一式对直线 $y=mx+n$ 的三个交点按重数成立。故 $\Delta$ 是杀掉 $3E$ 的群同态。

置 $A=18+2r,B=14+2r$，准确有
$$
 A/B=(1+r)/8,\qquad AB=64(8+r).
 \tag{19}
$$
8和64均为有理立方。R959 §§3–4 的完整实二次域证明给：在二的两个素理想上，$1+r$ 的赋值为 $(5,1)$；$\varepsilon=8+r$ 是范数 $-1$ 的根本单位，且不是立方。该根本性只需观察若 $1<u<\varepsilon$ 是单位，写 $u=(x+yr)/2$，则 $0<y<2$，迫 $y=1$，而 $x^2=61$ 或69不可能。因此 $[1+r],[8+r]$ 在 $F^\times/F^{\times3}$ 中独立。

(19) 的两行从 $[A],[B]$ 到这两个独立类的变换行列式为2，在 $\mathbf F_3$ 中可逆。故 $\Delta(P),\Delta(Q)$ 独立。
原三挠除法式是 $3x(x^3+1040)=0$；$x=0$ 需 $260$ 为有理平方，另一项在5处的赋值为一，不可能是有理立方。因此 $E_{260}(\mathbf Q)[3]=0$，于是
$$
 \boxed{\operatorname {rank}E_{260}(\mathbf Q)\ge2.}
 \tag{20}
$$
这是实际点的下降像下界，不使用秩表、BSD 或数值高度。

## 4. E260 全部局部数据与真实 Schwartz

其标签是 $(\epsilon,a,b)=(1,4,4)$。与一般表相比，全部费用明确为
$$
\begin{array}{c|c|c|c}
v&\chi_v\text{ 的单位值}&\text{uniformizer 值}&a(\chi_v)\\ \hline
2&\operatorname {Teich}_{\mu_3}(u)^{-1}&-1\text{ 在 }2&1\\
3&u\bmod\delta&-i\text{ 在 }\delta&1\\
5&u^4\in\mu_6&-1\text{ 在 }5&1\\
\pi&u^2\in\mu_6&-\omega\pi/\sqrt{13}&1\\
\bar\pi&u^2\in\mu_6&-\omega^2\bar\pi/\sqrt{13}&1.
\end{array}
\tag{21}
$$
13的两行中 $u^2$ 在各自剩余嵌入读取：$\omega\mapsto9,3$。核定第一支绝对值时，全局 $\pi$ 在2、3、5、另一13处的值依次是
$\omega^2,-1,-\omega^2,-\omega$，乘积 $-\omega^2$，给 (21)。

二处 $65$ 是 $\mathbf Q_2$ 六次幂，只有 $4$ 的 tame 三次扭曲；三处 $260/17\equiv1\pmod9$；五和十三的参数赋值一。故
$$
 \mathfrak f_{260}=(130\delta),\qquad
 N(E_{260})=152100,\qquad[K(\mathfrak f_{260}):K]=3456.
 \tag{22}
$$
根数、Hermitian 类和 $\kappa$ 均已由 (11)–(12) 核定。

### 4.1 二、三处

将 R290 原 $\chi_2$ 乘 Teich 的一次方时，其 splitting
$\mu(g)=\chi_2(\delta(g-1))\cdots$ 在 $g=\omega$ 处多 $\omega^2$，在 $g_*$ 和 $-1$ 处均多1。因此 (4) 的 $v_1$ 被新全部环面固定，不是原 $v_0$。其完整支撑和 Haar 为
$$
 \phi_2=f_A+t_1f_B,\qquad n_2=3-\sqrt3.
 \tag{23}
$$
三处同一导子一 splitting 给
$$
 \phi_3=\mathbf1_{\mathbf Z_3/3},\qquad n_3=3.
 \tag{24}
$$

### 4.2 五处

使用 R970(15) 的实际五维矩阵，取 $\tau(g)=g^4$。
由 $g=z^{-4}$，真实 $\chi_5(z)=z^4$ 给 $\eta(g)=g^{-1}$，故
$\tau=\eta_0\eta^{-1}=g^4$。完整正交投影
$\Pi_{5,4}=6^{-1}\sum_g\tau(g)^{-1}W_5(g)$ 给
$$
 \boxed{f_5(a)=3\sqrt5(\Pi_{5,4}e_0)(a)
 =\sqrt5\mathbf1_{a=0}
   +\omega^2\zeta_5^{2a^2}+\omega\zeta_5^{-2a^2}.}
 \tag{25}
$$
四个非中央元素是 $(x,y)=(\pm2,\pm2)$，两对指数为 $\pm2a^2$，$y$ 的 Legendre 符号均为负；所示两个权系数来自全部 $\tau^{-1}$，没有遗漏中心。
它实、偶且 $f_5(0)=\sqrt5-1\ne0$。正交投影或全 Gauss 和给
$$
 \phi_5=\sum_{a\bmod5}f_5(a)\mathbf1_{a/5+\mathbf Z_5},\qquad
 n_5=3(5-\sqrt5).
 \tag{26}
$$

### 4.3 十三处的两支和全部非紧费用

有限角色为 $\tau(2)=\zeta_{12}^4=\omega^2$，即 $b=4$。
用 R970(20) 的完整13维矩阵和
$\Pi_{13,4}=12^{-1}\sum_t\tau(t)^{-1}W_{13}(t)$，得到
$$
\boxed{\begin{aligned}
 f_{13}(a)&=6\sqrt{13}(\Pi_{13,4}e_0)(a)\\
 &=\sqrt{13}\mathbf1_{a=0}+1
 -\omega(\zeta_{13}^{-3a^2}+\zeta_{13}^{a^2})
 -\omega^2(\zeta_{13}^{-a^2}+\zeta_{13}^{3a^2}).
\end{aligned}}
\tag{27}
$$
为直接检查全投影，按 $t=2,3,4,5,6$ 模 $\pm1$ 取五对非中央元；其
$x/y$ 是 $(-3,1,-1,0,3)$，$(y/13)$ 是 $(-,-,-,+,-)$，
$\tau(t)^{-1}$ 是 $(\omega,\omega,\omega^2,1,\omega^2)$，正好给 (27)。它实、偶，$f_{13}(0)=\sqrt{13}+3\ne0$。

完整 isometry 仍是 R970(18)，$A=\delta_0^3\alpha$、$13A\equiv1\pmod{13}$。自然极化中的单位环带为
$\vartheta^{-1}\mathbf1_{\mathbf Z_{13}^{\times}}$，此时 $\vartheta(u)=u^2$ 在指定 split 支读取。它经该 isometry 落在 (27) 的同一非零、重数一有限线。非紧 uniformizer 仍移到不交环带，不声称整条非紧环面逐向量固定。

每个 $\mathbf1_{a+13\mathbf Z_{13}}$ 的范数平方是 $1/13$，故
$$
 \phi_{13}=\sum_{a\bmod13}f_{13}(a)\mathbf1_{a+13\mathbf Z_{13}},\qquad
 n_{13}=\frac{6(13+3\sqrt{13})}{13}.
 \tag{28}
$$
Yang 的单位范数单陪集经完整紧单位平均，范数平方是 $1/12$，theta 积分保持。归一后平方多十二，因此 split 因子仍为 $13/12$，不是 $13/144$。这一步保留 (21) 的两支和全部非紧参数。

## 5. 同一 degree130 全权平方及实际来源线

其余有限处取标准球。准确有理支撑为 $x=n/30$，定义
$$
 a_n=v_1(n\bmod4)f_5(n\bmod5)f_{13}(10n\bmod13).
 \tag{29}
$$
全部局部向量非零且 CRT 独立，所以这是非零系数系统。它实偶，且
$a_{n+260}=a_n,\ (-1)^na_{n+130}=-a_n$。因此
$$
 F(Z)=\sum_na_n e^{\pi i(\delta/3)n^2/260+2\pi inZ},\qquad
 S_{\rm raw}(Z)=e^{130\sqrt3\pi Z^2}F(Z)
 \tag{30}
$$
是标准 $\mathcal O(130O)$ 的非零截面：换指标给
$F(Z+s_0)=e^{-130\pi is_0-260\pi iZ}F(Z)$、$F(Z+1)=F(Z)$，
其中 $s_0=(1-\omega)^{-1}$。没有新的 flat twist。

令 $h=\sqrt\kappa/(60\pi i)$，沿用 R290 Hermite 规范，
$$
 b_m=\sum_na_nH_m(\sqrt\kappa n/30)e^{-\pi\kappa n^2/30^2},\qquad
 \sum_m b_mT^m/m!=S_{\rm raw}(hT),\qquad
 130\sqrt3\pi h^2=-1/(8\pi).
 \tag{31}
$$
全部有限不变性给 $b_m=0$ 若 $6\nmid m$，且每个 $b_m$ 实。
当 $6\mid m$ 时，(21) 的全部有限单位角色保持；13非紧参数虽随权变，单位环带的矩阵系数在非零赋值环带为零，故同一 Schwartz 及同一 split 费用适用于所有这些权。

置
$$
 c(0)=65/108,\qquad
 C_{260}=\frac2{6c(0)}\frac{\pi}{3\sqrt3}
       \frac{\sqrt{2\kappa}}{n_2n_3n_5n_{13}}>0.
$$
Yang 的原 theta 积分与全局体积计算于是准确给
$$
 \boxed{L(\psi_{260}^{2m+1},m+1)
       =C_{260}\frac{(4\pi)^m}{m!}b_m^2\qquad(6\mid m).}
 \tag{32}
$$
类数一的体积比仍为六，全部局部范数见 (23)–(28)。由 (20) 与 CM 解析秩零定理的逆否命题，$L(E_{260},1)=0$；故 $b_0=0$，真实来源至少六阶。

标准 Fourier 坐标 $a_n\zeta_{520}^{-n^2}$ 全代数；R959 §10 的两个真实130挠平移和绝对不可约 theta-group 交织，先给一条固定代数线。由 (8)、(15)，它的绝对 CM 特征值是
$$
 (\lambda_7,\lambda_{19})=(\omega,-\omega^2)
       =(\zeta_6^4,\zeta_6^5).
 \tag{33}
$$
本节独立的局部构造与 (32) 先于计算谱指定这条线。

### 5.1 同次原矩阵的实际完整回执

公开 run **45884058894**，job **140130269899**，源提交
`fbb1c31937b02426caa21e77d65bd22e080a32c9`，使用同次完整390矩阵与 R970 的全部22列整嵌入。R976 逐项核所有81联合投影、完整质量列、总和、两个十二次幂及全部 H/F 回乘，结果全部 PASS。本篇消费的准确结论为
$$
 \dim_K\operatorname {im}\Pi_{4,5}=1,\quad
 \Phi_{260,1}=\sigma_1^{130}x_1^2\sum_{j=0}^{20}u_jX_1^j,\quad
 u_j\in\mathbf Q,\quad u_{20}=1,
 \tag{34}
$$
$$
 \boxed{\Pi_{4,5}\mathscr H_{130}=\frac1{81}\Phi_{260,1},\qquad
        \Pi_{4,5}F_{130}=0.}
 \tag{35}
$$
源首阶准确为六，归一源 SHA256 为
`d27425cf5e8895ad6f054ef73d126608ab7dc5a38c22eb9acaa8cadea7e678b3`。
限制22矩阵摘要为
`aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113`；
全部81块及 H/F 分量摘要为
`10f135ee6b95817e9b4414e974d66a9d5129318f9059058072fc61b821f11313`。
生产器和消费者、完整390摘要及所有其他块的实际回执见 R976，不保存生成坐标表作下一次输入。

因 (34) 的完整共同核唯一，(29) 的先验非零来源就是该线。不是将任意一维核重新命名为 $E_{260}$。
两个十二阶投影在 $p>211$ 整，实际 $\mathscr H_{130}$ 的原除法来源也在该范围整；由 (35)，$\Phi_{260,1}=81\Pi_{4,5}\mathscr H_{130}$，故本归一不引入新的无界整格费用。也可固定一次清分母 $D_{260}$，下节保留其全部赋值。

本节还界定表中其他 primitive 曲线的范围：除 $65^3,260$ 外，表中八条 primitive 一维线的完整质量泛函均非零（R976 的实际22列回执）。对这些偶标签，(25)、(27) 换成各自完整偶角色投影；非 quadratic 投影线均非零，实际单位环带及 Yang 因子均非零。相同的 (32) 在 $m=0$ 因而给 $L(E_d,1)\ne0$，CM 秩零定理给这八条曲线的有理秩为零。这个判断不从 $\Pi\mathscr H$ 是否非零推导；它读取的是该整条源线的质量泛函。两个13-old块不在此结论中。

## 6. 真实模型、普通与惰性通常全 Selmer 桥

这部分应用 R970 §6、R959 §§13–16 已付的通用证明，逐项保留新输入的费用。令 $\widehat u_j=D_{260}u_j$ 整，$\widehat\Phi=D_{260}\Phi$。对任意非零 $b$，准确齐次式为
$$
 \Phi_{260,b}(z)=\sigma_b^{130}x_b^2
       \sum_{j=0}^{20}u_j b^{20-j}x_b^{3j}
       =b^{-1}\Phi_{260,1}(\theta_bz),\qquad\theta_b^6=b.
 \tag{36}
$$
物理曲线是 $b=260$，共同模型是 $b=17$。Hermitian 参数 $5/13$、degree130 和微分同构各自保留。
由同一周期 $\varpi_{260}=s_0\Omega_{260}$ 及 (31)–(32)，有固定非零代数数 $\widehat\kappa_{260}$，满足
$$
 \mathscr E_{260,m}=\frac{\widehat\kappa_{260}}{s_0}
                   130^{-m}\widehat s_m^2,\qquad
 \widehat\Phi_{260,260}(z)=\sum_m\widehat s_mz^m,\quad6\mid m.
 \tag{37}
$$
非零代数性可在第一个非零 Taylor 系数的临界值取得；不逐权选平方根。清分母使常数除以 $D_{260}^2$，其赋值不能丢弃。

### 6.1 普通素数

在固定有限坏集之外，$p>211,p\equiv1\pmod3$。真实 CM sigma 整性和 (36) 的每项阶 $126-6j\ge6$ 给有界整测度 $\widehat\nu_{260,p}$。取其原单位切域和实际相容单位周期，定义
$$
 \widehat G_{260,p}(T)=\int_{\mathbf Z_p^\times}
 (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}\,d\widehat\nu_{260,p}(x).
 \tag{38}
$$
两个真实 Katz Euler 因子同为
$1-\pi_p^m/\bar\pi_p^{m+1}$，$\pi_p=\psi_{260}(\mathfrak p)$；从 (37) 的全权平方作原单位矩极限，得到
$$
 \mathcal K_{260,p}(T)=\frac{\widehat\kappa_{260}}{s_0}\Omega_{p,260}
 (1+T)^{-\log_p\langle130\rangle/\log_p(1+p)}
 \widehat G_{260,p}(T)^2.
 \tag{39}
$$
由 $L(E_{260},1)=0$ 在同一 Katz 分支的插值，$\widehat G_{260,p}(0)=0$；这一单位质量零另由 (39) 支付，不从全质量零偷推。

Agboola–Howard 的通常单 CM Selmer 定理适用：最大整环 CM、正根数和好普通已证，射线次数3456与 $p$ 互素。辅助好惰性11的中心因子 $-132$ 为单位；primitive 的2、3、5、两个13参数不删。原惯性像、塔上挠点排除、基层控制和二次分解与 R970 相同。因此，若 $r=\operatorname {rank}E_{260}(\mathbf Q)$，$r_p=\operatorname {corank}_{\mathbf Z_p}\Sha(E_{260}/\mathbf Q)[p^\infty]$，
$$
 \boxed{r+r_p\le2\operatorname {ord}_0\widehat G_{260,p};\qquad
 \widehat G'_{260,p}(0)\ne0\Longrightarrow
 r=2, \Sha(E_{260}/\mathbf Q)[p^\infty]\text{ 有限}.}
 \tag{40}
$$
这里使用 (20) 的秩下界，而非假定秩恰二。

### 6.2 惰性素数与每权真实 period 比

令 $p=6s-1>211,d=p+1$。在同一 $E_1$ 上取
$f=\log(\sigma/z),c=[z^d]f$、$v_p(c)=-1$，定义完整 Gaussian/Newton
$$
 \widehat G_{130}=\widehat\Phi_{260,1}e^{-130cz^d},\qquad
 a_h=(130c)^{-h}[z^{dh}]\widehat G_{130},\qquad
 \widehat J_{260,p}(v)=\sum_{h\ge0}a_h(v)_h.
 \tag{41}
$$
R301 的同一严格圆盘估计逐项应用于 (34)，给
$$
 v_p(a_h)\ge\left\lceil\frac{h(p-1)+6}{2p}\right\rceil,\qquad
 \widehat J_{260,p}\in pv\mathcal O\langle v\rangle,\qquad
 \widehat J_{260,p}(k)=k!(130c)^{-k}[z^{dk}]\widehat\Phi_{260,1}.
 \tag{42}
$$
这里没有改变原参考 Gaussian。因 $260\in\mathbf F_p^\times\subset\mathbf F_{p^2}^{\times6}$，取单位 Hensel 根 $\theta^6=260$，原整同构
$$
 F_\theta:E_1\longrightarrow E_{260},\qquad
 (X,Y)\longmapsto(\theta^2X,\theta^3Y),\qquad
 F_\theta^*\omega_{260}=\theta^{-1}\omega_1
 \tag{43}
$$
将 Gaussian 同时运成 $\theta^dc$。Newton 系数中的 $\theta^{dh}$ 完全相消，故物理半因子是 $260^{-1}\widehat J_{260,p}$，共同模型是 $17^{-1}\widehat J_{260,p}$。

R303/R943/R959 的完整 BKO signed 格及标准椭圆单位类给
$0\ne\mathcal A_{260,p}\in\mathcal O[[T]]$。新费用为 primitive 导子 $130\delta$、ray 次数3456、(43) 的真实微分、与参考 $E_1$ 同阶的 Tate/Gamma 因子和阶乘。两边非单位的 $m!$ 及 $p$ 处 $1+1/p$ 只在比中消掉，未被单独声称为单位。

参考5处完整因子是 $6/5$，参考13处为
$$
 (1-\rho^{2m+1}/13^{m+1})(1-\bar\rho^{2m+1}/13^{m+1}),\qquad
 \rho=-\omega^2\pi,\quad\rho+\bar\rho=2.
 \tag{44}
$$
在 $d\mid m$ 的整条支上，它模 $p$ 为 $12/13$，故为单位；不是将整个权函数偷换成常数。辅助好惰性 $\ell\equiv1\pmod p$ 的原因子模 $p$ 为2。全部固定坏集仍有限。

所用混合权比较的准确范围是：Kato §15.8 的 CM 张量、Lemma15.11 分别定义的 étale/de Rham 与 Betti/复周期图，以及已证等式 (15.16.1)，将同一椭圆单位张量送到按该 Betti 像标记的 Kato 类；Theorem12.5(1) 的 $k=2m+2,r=m+1$ 再分别通过两个图拉回。任意共同秩一映射 $s$ 的标量消去。不需要 Kato 同页尚未证明的“两个图由同一 motivic 映射诱导”这一更强命题。详见本轮 mixed-weight period audit note 的实际图及原文页码。

故每个允许权分别有真实赋值身份
$$
 v_p\mathcal A_{260,p}(x_m)
 =v_p\mathscr E_{260,m}-v_p\mathscr E_{1,m},\qquad
 x_m=q_{\rm ac}^m-1,\quad v_p(q_{\rm ac}-1)=1.
$$
与原 $J_{0,p}\in1+p\mathcal O\langle v\rangle$ 比较，得到
$$
 \boxed{v_p\mathcal A_{260,p}(x_{dk})
 =v_p(\widehat\kappa_{260})+2v_p\widehat J_{260,p}(k).}
 \tag{45}
$$
不假设被约掉的剩余单位随权解析。沿 $k=p^n$ 比较 $n$ 的系数，得
$\operatorname {ord}_0\mathcal A_{260,p}=2\operatorname {ord}_0\widehat J_{260,p}$；非零 $\mathcal A$ 排除 $J\equiv0$。BKO Theorem6.2 的基层通常 Selmer 不等式包括通常全 Selmer，且平凡角色在正号格，没有相反符号的一维加项。因此
$$
 \boxed{r+r_p\le2\operatorname {ord}_0\widehat J_{260,p};\qquad
 \widehat J'_{260,p}(0)\ne0\Longrightarrow
 r=2, \Sha(E_{260}/\mathbf Q)[p^\infty]\text{ 有限}.}
 \tag{46}
$$
这不把 signed Selmer 的挠性本身当成通常全 Sha 的有限性。

同一完整有限证书为
$$
 L_H=\sum_{h=1}^H(-1)^{h-1}(h-1)!a_h,\qquad
 M_H=\left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!),
$$
$$
 \widehat J'_{260,p}(0)\ne0
 \quad\Longleftrightarrow\quad
 \exists H:\ v_p(L_H)<M_H.
 \tag{47}
$$
因为 (42) 给误差赋值至少 $M_H\to\infty$。这仍是完整导数证书；首位模 $p$ 为零不等于证书失败。

## 7. 新输入的准确作用域

式 (20)、(21)–(32)、(34)–(46) 使 $\Phi_{260}$ 成为一个真正不同的固定 rank≥2 曲线原中央，并且实际出现在原 $\mathscr H_{130}$ 的全谱中。它因此可以与旧固定曲线一起参与原共同 cut 上的联合非零问题。

式 (35) 同时明确原 R971 的 norm130 六 sigma 输入在此新线上为零，不能据旧 $F_{130}$ 构造一个假非零 companion 单位。需要另一个真实六 sigma 输入时，必须再次给实际完整投影回执；仅改 dyadic 标签、首项或轴的范数不支付该门。

完整 $\mathscr H_{130}$ 还含两个13-old块及四个非六次块。对这些余项，本篇已经识别其有限角色和全局来源范围，却没有把 $E_{260}$ 的中央零传播给它们，也没有跨越旧 mixed cut 交换投影次序。完成标准所要求的固定曲线、无穷多个不同素数的通常全 Sha 有限量词仍须继续证明。

## 依据

- R290：二处全部生成元积分、三处导子一向量、原 Hermite 与体积规范。
- R959：实二次域下降、代数 theta-group 比较、普通及 signed 的通常全 Selmer 通用桥。
- R970：本篇同一 $\alpha=5/13$ 的5/13有限矩阵、绝对 CM 锚、全22嵌入及新权费用的通用形式。
- R972、R976：同一次完整390限制与22维全谱；本篇的算术标签独立由 (8) 规定。
- Silverman–Stange，§6、Theorem19 证明的六次剩余式：<https://arxiv.org/pdf/0912.1831>。
- Yang，*Theta liftings and Hecke L-functions*，Theorems1.11、2.6、2.15及split局部Corollary2.13：<https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>；*Eigenfunctions of the Weil representation of unitary group of one variable*：<https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>；1999 原 splitting 和 Schrödinger 转模：<https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- Agboola–Howard，Theorems2.1.1、2.4.17(1)：<https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf>。
- Burungale–Kobayashi–Ota (2021)，Theorems2.1、6.1–6.2：<https://annals.math.princeton.edu/2021/194-3/p08>；BKO (2024) §2.2.1、Corollary4.11(i)、Proposition4.12：<https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf>。
- Kato，Theorem12.5(1)、§15.8、Lemma15.11、(15.16.1)：<https://www.numdam.org/article/AST_2004__295__117_0.pdf>；本轮逐图核查见 `notes/2026-11-27-mixed-weight-period-audit-and-height-difference-scope.md`。
