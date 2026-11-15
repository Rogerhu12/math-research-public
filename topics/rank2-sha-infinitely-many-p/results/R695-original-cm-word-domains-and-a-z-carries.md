# R695 — 原 CM 三态共同核心、真实词像格与 A/Z 双门比较

日期：2026-11-15。**状态：已证明。**

本篇保持 R679 的同一个 $q_N^\sharp$，不采用尚未构造的 W 适配测试。
把 R487 的完整奇阶平移论证用于 R692 的四轴三态，再加入 R488 的
原 A 两层核心，得到**投影之前的真实 CM 词域**。
它与 R692 先返回、再运输投影的式子相容，但两个域不能相互替代。

同时付清一个实际几何接点：原非零八角域位于
$A^2W$ 和 $WA^2$ 两个原词域的交中，两个返回观察的深度相差二；
第一 CM 的不同单位尺度把它们的 A 超深管送到两两不交的管。
原权在 A 端出现的十二次差、以及浅层两条互不相交的 H 门均完整保留。
这些式子给原三中央和参考行的确切返回，不将任何受限补域赋零。

## 1. 原三态、五个实际核心字母

沿用 R686、R692 的
$$
\lambda=-\bar\pi_0^{-1},\qquad \beta=-\lambda,\qquad
\kappa=p\lambda^2,\qquad d_p=p-1,
$$
$$
\gamma=\chi_{29,p}\chi_{7627,p}\in\{1,-1\},\qquad b=17.
\tag{1}
$$
在原六 sigma 联合上令
$$
Q=c+2d,\quad L=2c-d,\quad
Y=A+Q,\quad
W=A+b_QQ+b_LL,
$$
$$
b_Q=\frac{11+6\omega}{5},\quad b_L=\frac{2+12\omega}{5},\quad
b_Y=\frac{20+3\omega}{17},\quad Z=W-b_YY,
$$
$$
E=(5+6\omega)A-\frac{29(5+6\omega)}5Q+\frac{87\omega}5L,\qquad
V=36Y-(17-3\omega)W .
\tag{2}
$$
这里 $\operatorname{Gram}(A,Q,L)=\operatorname{diag}(29,5,5)$，
$\operatorname{Gram}(Y,17Z,E)=\operatorname{diag}(34,8942,7627)$。
原另三个伙伴逐个保留。

三态为 R692 的
$$
e_0=\mu_0,\qquad
e_1=K_{72,W}e_0,\qquad
e_2=-\frac14\sum_{t\in E[4]}\mathsf T_{W,t}^{72}e_0.
$$
包括原 C 角平均、所有 quarter flats 和 canonical 中心。
按列表示来源像，
$$
R=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix},
\qquad
K=\begin{pmatrix}0&1&-1\\1&0&-1\\0&0&-1\end{pmatrix}.
\tag{3}
$$
$R^2=K^2=(KR)^4=I$。从 $e_0$ 出发的来源轨道是
$e_0,e_1,e_2,-e_0-e_1-e_2$。

以 $P_{B,t}$ 表示沿原正交 B 轴乘 $t$、固定其正交补的物理映射。
下表是完整测度限制，不是边际等式：
$$
\begin{array}{c|c|c|c}
\text{字母}&\text{物理映射 }M_a&\text{来源 }S_a&
  \text{外标量 }c_a\\ \hline
Y&R_YP_{Y,\kappa}&R&\lambda\\
Z&R_YP_{Z,\kappa}&R&\gamma\lambda\\
W&P_{W,\kappa}&K&\lambda\\
V&P_{V,\kappa}&K&\gamma\lambda\\
A_2&P_{A,\kappa^2}&R&\lambda^2
\end{array}
\tag{4}
$$
前四行是 R692；最后一行是 R488 的同一个原 A 两层身份。
$A_2$ 是一个字母，所对应的真实深度为二。
$R_Y$ 不得从 Z 或 W 混管中删除。

对字 $\mathfrak w=(a_1,\ldots,a_r)$ 定义
$$
M_{\mathfrak w}=M_{a_1}\cdots M_{a_r},\quad
S_{\mathfrak w}=S_{a_r}\cdots S_{a_1},\quad
c_{\mathfrak w}=\prod_{\ell=1}^r c_{a_\ell}.
\tag{5}
$$
逐个在整像上取逆，得到
$$
e_i|_{M_{\mathfrak w}\mathcal O^6}
=c_{\mathfrak w}(M_{\mathfrak w})_*S_{\mathfrak w}e_i.
\tag{6}
$$
式 (6) 的像格包含全部后续转置条件；它不是各未运输轴深条件的交。
所有矩阵均对其实际整像可逆，未对任意受限测度定义 theta 投影。

## 2. 第一 CM 分支的两种等价写法

取
$$
\alpha=\gamma_{13}^j\gamma_{19}^{\,k},\quad
\gamma_{13}=4+\omega,\quad\gamma_{19}=5+2\omega,\quad
0\le j\le17,\quad k\in\{0,1\}.
$$
第一 theta 轴是原 $2Y$，次数 136。
在这一轴使用原 canonical lift
$$
\mathsf T_t^{(n)}F(z)=e^{-n\eta_t(z+t/2)}F(z+t),
$$
并定义保完整纤维的平移和
$$
\mathcal Q_\alpha F
=\sum_{t\in E[\alpha]}\mathsf T_{\bar\alpha t,\,2Y}^{136}F.
\tag{7}
$$
$F$ 的其余五个变量不变。(7) 不删除任何纤维或常数半相位。

R465(42) 的完整分支为
$$
G_{\alpha,t}(z,\mathbf z)
=(\mathsf T_{\bar\alpha t}^{136}F)(\bar\alpha z,\mathbf z),
\qquad
\nu_{N_{\alpha,Y}F}
=\alpha^{-1}[\alpha^{-1},I_5]_*\sum_t\nu_{G_{\alpha,t}}.
$$
现在仅把 $G$ 内的生成变量 $\bar\alpha z$ 拉回移到物理推前；
这给完全等价的式子
$$
\boxed{
\nu_{N_{\alpha,Y}F}
=\alpha^{-1}(D_{\bar\alpha/\alpha})_*\nu_{\mathcal Q_\alpha F},
\qquad
D_s:(Y,Z,E,\mathbf R)\mapsto(sY,Z,E,\mathbf R).
}
\tag{8}
$$
加入 principal 角分支 $\zeta\in\mu_6$ 后，令
$$
s=s_{\alpha,\zeta}=\zeta\bar\alpha/\alpha,\qquad
\sigma_{\alpha,\zeta,i}
=\alpha^{-1}(D_s)_*\nu_{\mathcal Q_\alpha e_i}.
\tag{9}
$$
因此本篇的 $s$ 与仍把 $\bar\alpha z$ 留在 G 内时的
$\zeta/\alpha$ 不同；两者不能交叉使用。
所有 $1/\alpha$、完整 torsion lift 和
$\log\langle s\rangle=\log\langle\bar\alpha\rangle-
\log\langle\alpha\rangle$ 都仍在 (8)–(9) 中。

## 3. 原固定奇覆盖上，五个核心都保同一个平移来源

使用 R487 已付的固定
$$
m=13^{17}19^5,\qquad
\pi_0\equiv2\pmod{13^{34}},\qquad
\pi_0\equiv1\pmod{19^{10}} .
\tag{10}
$$
这些条件与当前原 ray 相容，并已在 R487 付固定单位 CRT 与无穷性。
特别 $g_\pi=\pi_0/\bar\pi_0\equiv1\bmod m^2$。
这里不把模 13、19 的低阶条件误用到高次 trace。

先取原 quarter 来源及 (4) 各正交框架的一个共同偶覆盖，
再沿全部六轴作 $[m]$ 拉回。沿 R487 已付的 frame，再作 (2) 的新增变换，其新增分母只涉及
$2,3,5,17,29,263$；全部清分母与 m 互素；
(7) 的每个平移因而可在各框架中准确写成 $m^2$ 挠平移。
具体 lift 与 R487(23) 相同：清分母矩阵在模 $m^2$ 求逆，
而不是只模 m 求逆。其各轴次数是 $n_\ell m^2$，$n_\ell$ 偶。

完整 ordinary Egorov 身份在当前轴把平移参数送至 $g_\pi t$；
A 两层使用 $g_\pi^2t$。由 (10)，新旧参数相差整周期。
若 $t=u/m^2$、周期差为 v，则唯一可能的交叉相位为
$$
\exp\!\left\{\frac{n_\ell m^2}{2}
(\eta_vt-\eta_tv)\right\}
=\exp\{\pi i n_\ell E(v,u)\}=1.
\tag{11}
$$
标准周期半特征在该偶覆盖也为一。
所以这是完整中心的交换，不只是 projective 的交换。

由此每个 (4) 的真实核心与 (7) 的**每条完整平移来源**交换。
其绝对标量已经由 (4) 的原来源定标；$[m]$ 是普通单位推前，
不产生新的外部标量。故
$$
\boxed{
\nu_{\mathcal Q_\alpha e_i}|_{M_a\mathcal O^6}
=c_a(M_a)_*\nu_{\mathcal Q_\alpha S_ae_i}.
}
\tag{12}
$$
完整高阶词由同一式迭代。没有给整个高次数 theta 空间另猜 scalar。
这些平移在一个固定 prime-to-p 覆盖上整，$1/\alpha$ 为单位，
所以所有式子保持原有界整测度格。

原 $q_N^\sharp$ 只依赖 Y/Z 平面的四个共同伙伴。
它与 (7)、$D_s$ 及前四个物理映射交换；原 C-unit 和 H-deep 门也不动。
这可先在正交 Y 框架逐个变量检查，再以原 Gram 等式转回；
不是将隐藏权认作一个新的完整第一源。

## 4. 投影之前的真实 CM 词域与完整原算术行

置
$$
M_{\mathfrak w,s}=D_sM_{\mathfrak w}D_s^{-1}.
$$
由 (9)、(12) 逐项得到
$$
\boxed{
\sigma_{\alpha,\zeta,i}|_{M_{\mathfrak w,s}\mathcal O^6}
=c_{\mathfrak w}(M_{\mathfrak w,s})_*
 \sigma_{\alpha,\zeta,S_{\mathfrak w}i}.
}
\tag{13}
$$
下标 $S_{\mathfrak w}i$ 按线性组合解释。
(13) 是投影前各真实来源的式子，不是把投影穿过一个未运输的域。

三个第一轴投影写成
$$
P_\chi=\sum_{\alpha,\zeta}a_{\chi,\alpha,\zeta}
    R_{\zeta,Y}N_{\alpha,Y},
$$
其中
$$
a_{S,j,0,\zeta}=\frac{(-1)^j}{108},\qquad
a_{{\rm new},j,k,\zeta}=\frac{\omega^{2j}(-\omega)^k}{216},
\qquad
a_{H,j,k,\zeta}=\frac{(-\omega^2)^k}{216}.
\tag{14}
$$
第一行只取 k=0，其余两行取 k=0,1。
这就是 R483 的同一十八项/三十六项投影及六角平均。

记 $f_w(y)=1_{y\in\mathcal O^\times}\langle y\rangle^{d_pw}$。
在每一项中使用**实际返回权及观察**
$$
q_{\mathfrak w,s}=q_N^\sharp\circ M_{\mathfrak w,s}^{-1},
\qquad Y_{\mathfrak w,s}=Y\circ M_{\mathfrak w,s}^{-1}.
$$
完整加权行定义为
$$
\mathcal J_{\chi,i,\mathfrak w}(w)
=\sum_{\alpha,\zeta}a_{\chi,\alpha,\zeta}
 \int_{M_{\mathfrak w,s}\mathcal O^6}
 q_{\mathfrak w,s}f_w(Y_{\mathfrak w,s})\,
 d\sigma_{\alpha,\zeta,i}.
\tag{15}
$$
由 (13) 精确返回后，所有源重新组成同一个投影：
$$
\boxed{
\mathcal J_{\chi,i,\mathfrak w}
=c_{\mathfrak w}\int f_w(Y)\,dP_\chi(q_N^\sharp S_{\mathfrak w}e_i).
}
\tag{16}
$$
若词只含四个平面轴，$q_{\mathfrak w,s}=q_N^\sharp$；
含 $A_2$ 时不能这样简化。

R692 已付右边整个来源及尺度。具体写
$$
\begin{array}{c|rrrr}
v&e_0&e_1&e_2&-e_0-e_1-e_2\\ \hline
d_S(v)&1&\omega^2/2&\omega^2/2&\omega\\
d_{\rm new}(v)&0&52/3&-52/3&0\\
d_H(v)&0&c_H&-c_H&0
\end{array},
\qquad c_H=-\frac{1+\delta}{2016b}.
$$
于是 (16) 等于
$$
\boxed{
c_{\mathfrak w}\lambda^N
\begin{cases}
d_S(S_{\mathfrak w}e_i)J_S(w),&\chi=S,\\
d_{\rm new}(S_{\mathfrak w}e_i)
   \langle2\rangle^{-d_pw}J_{\rm new}(w),&\chi={\rm new},\\
d_H(S_{\mathfrak w}e_i)
   \langle2\rangle^{-d_pw}J_H(w),&\chi=H .
\end{cases}}
\tag{17}
$$
新线、参考的 $2^{-1}$ 是原物理 Y 与 theta 轴 $2Y$ 的准确尺度。
$J_H(0)=1+\lambda$，其未知导数没有被赋零。

因此三原中央失败合法控制 (17) 的秩二行，所有来源、权、域均可逐项复原。
它不控制将 (15) 中各 $M_{\mathfrak w,s}$ 改为同一个 $M_{\mathfrak w}$ 后的式子。

## 5. 四轴真切集及 CM 词的具体差

例如 W 字母在 $\sigma_{\alpha,\zeta,i}$ 上的实际深域是
$$
W_s:=W\circ D_s^{-1}=b_Ys^{-1}Y+Z\in p\mathcal O,
$$
V 字母的域为
$$
V_s:=\frac{263}{17}s^{-1}Y-(17-3\omega)Z\in p\mathcal O .
\tag{18}
$$
Y/Z 字母的深域不变。把 (18) 拉回未缩放的
$\nu_{\mathcal Q_\alpha e_i}$，原未共轭 W 门则是
$b_YsY+Z\in p\mathcal O$；这是 R692(31) 的同一切集，使用的是
本篇 (8) 的完整重写。

任意原测试 f 和 word 的两种先后次序，其域差准确是逐支
$$
1_{M_{\mathfrak w,s}\mathcal O^6}
 -1_{M_{\mathfrak w}\mathcal O^6},
\tag{19}
$$
同时还须保相应的两个逆观察与两个返回权。
只有指示函数相同的区域才允许删去 (19)；
不是只由来源矩阵 $S_{\mathfrak w}$ 相同就删去它。

## 6. 原八角域与所有第一 CM 超深管

(2) 的正交逆精确给
$$
\boxed{
\begin{aligned}
A&=\frac{29}{34}Y+\frac{87\omega}{526}Z
       -\frac{1+6\omega}{263}E,\\
Q&=\frac5{34}Y-\frac{87\omega}{526}Z
       +\frac{1+6\omega}{263}E,\\
L&=-\frac{17(5+6\omega)}{263}Z+\frac{3\omega^2}{263}E.
\end{aligned}}
\tag{20}
$$
特别 L 是 Y 的真正伙伴，第一 CM 分支逐个固定 L。
写
$$
A_s=A+\frac{29}{34}(s^{-1}-1)Y,\qquad
Q_s=Q+\frac5{34}(s^{-1}-1)Y .
\tag{21}
$$

保 R678 的真实角域
$$
\mathcal C_{r,k,n}
=\{A\in p^{2r},\ Q\in p^k\mathcal O^\times,\
                    L\in p^n\mathcal O^\times\},
\qquad k<n<2r.
\tag{22}
$$
在其上
$$
v_p(Y)=v_p(Z)=v_p(W)=v_p(E)=v_p(V)=k.
\tag{23}
$$
证明只需保 Q 的真实首项：
Z 的系数是 $87(1+\omega)/85$，W 的系数是 $b_Q$，
E 的系数是 $-29(5+6\omega)/5$，
V 的系数是 $-(25+87\omega)/5$。
最后一个范数为 $13\cdot463$；当前 $p\equiv7\bmod64$ 已不取 463，
也可统一将显示有限因子列入固定坏集。

完整 CM 像为
$$
\boxed{
D_s\mathcal C_{r,k,n}
=\{A_s\in p^{2r},\ Q_s\in p^k\mathcal O^\times,\
                       L\in p^n\mathcal O^\times\}.}
\tag{24}
$$
216 个 $s=\zeta\bar\alpha/\alpha$ 在 K 中两两不同：
13、19 两对共轭素理想的赋值先确定 j,k，随后确定 $\zeta$。
删去其两两差分子的范数的固定有限素因子；
这与 R487 的显示有限坏集等价，因为只是取逆/共轭斜率。
在余下同一无穷 ray 上，不同 s,t 的 (24) 两两不交。
确实
$$
A_s-A_t=\frac{29}{34}(s^{-1}-t^{-1})Y
$$
在 $v_p(Y)=k$ 上恰有赋值 k，而两个 A 管都要求赋值至少 $2r>k$。

这项分离只定位真正的补域。不同项含不同完整 CM 平移来源，
测度也不是正测度；因此两两不交并不排除其积分相消。
尤其 (22) 中的已付非零，只适用于其原来源及原测试，
没有被搬成 (24) 每条新来源的非零值。

## 7. 同一个 R：A 两层与 Z 一层的确切比较

由 (4) 对任意原态、任意完整返回测试 F 有
$$
\boxed{
\lambda^{-2}\int_{A\in p^2} F\circ P_{A,\kappa^{-2}}\,de_i
=(\gamma\lambda)^{-1}
 \int_{Z\in p}F\circ(R_YP_{Z,\kappa})^{-1}\,de_i
=\int F\,dRe_i .
}
\tag{25}
$$
在 CM 分支中将 A、$P_A$ 换成 (21) 的共轭，而 Z 映射完全不变；
因为 $D_s$ 与 $R_Y P_{Z,\kappa}$ 严格交换。
这正是 (15) 的 A 单字与 Z 单字的同来源比较。

下面付清 F 含原 q 时 A 端的全部差。
记
$$
e_A=5+6\omega,\quad
a_0=-e_A/29,\quad b_F=e_A/5,\quad\ell_0=-3\omega/5,\quad
g=3-2\omega.
$$
原门和权可准确写成
$$
H=D^*+a_0A+b_FQ+\ell_0L=D^*-E/29,
$$
$$
q_N^\sharp
=1_{C\ {\rm unit},\,H\in p^N}
 \mathcal P_N\bigl(H/\kappa^N,\ H+14C,\
                         13H_1+g(H+C)\bigr).
\tag{26}
$$
$\mathcal P_N$ 是 R679 已构造的实际混合六/十二次多项式，
包括各自的 $b,\Omega$ 规范；不是辅助有限域解。

置
$$
\Delta_A=a_0(\kappa^{-2}-1)A,\qquad
\partial_N=\kappa^{-N}\partial_1+\partial_2+g\partial_3 .
$$
A 端返回的实际权是
$$
\boxed{
q_A=1_{C\ {\rm unit},\,H+\Delta_A\in p^N}
 \mathcal P_N(\mathbf X+\Delta_A(\kappa^{-N},1,g)),
}
\tag{27}
$$
其中 $\mathbf X$ 是 (26) 的三个实参。
在 $A\in p^{N+2}$ 上，两个 H 门相同，且准确有限展开为
$$
\boxed{
q_A-q_N^\sharp
=1_{C\ {\rm unit},\,H\in p^N}
 \sum_{\ell=1}^{12}\frac{\Delta_A^\ell}{\ell!}
       \partial_N^\ell\mathcal P_N(\mathbf X).
}
\tag{28}
$$
当前 p 大于 12，所有 factorial 为单位。
若 $v_p(A)=j\ge N+2$，第 $\ell$ 项的下界是
$\ell(j-N-2)$，保实际系数的整性。

反之，对 $2\le j<N+2$，$\Delta_A$ 恰有赋值 $j-2<N$。
所以
$$
\{H\in p^N\}\cap\{H+\Delta_A\in p^N\}=\varnothing
\quad\text{在 }v_p(A)=j\text{ 上}.
\tag{29}
$$
这一部分的 $q_A-q_N^\sharp$ 是两条不交的完整权管之差，
不能用 (28) 或连续小误差代替。C-unit 仍在两项中。
CM 分支中所有式子只把 A 换成 $A_s$，H、C、$H_1$ 固定。

## 8. 两个原词在同一非零角域上的精确交叠

取
$$
M_+=P_{A,\kappa^2}P_{W,\kappa},\qquad
M_-=P_{W,\kappa}P_{A,\kappa^2},
$$
$$
d_A=\kappa^{-2}-1,\qquad d_W=\kappa^{-1}-1,\qquad
a_W=(17-3\omega)/36,\qquad c_A=29/72 .
$$
两个真实像格分别是
$$
\boxed{
\begin{aligned}
M_+\mathcal O^6&=\{A\in p^2,\ W+d_AA\in p\},\\
M_-\mathcal O^6&=\{W\in p,\ A+d_Wc_AW\in p^2\}.
\end{aligned}}
\tag{30}
$$
它们的来源分别为 $KR e_0=e_1$ 和 $RK e_0=e_2$，
外标量同为 $\lambda^3$。

两个返回的第一观察完整是
$$
\boxed{
\begin{aligned}
Y_+&=Y+d_Wa_WW+d_A(1+d_Wa_W)A,\\
Y_-&=Y+d_AA+d_W(a_W+d_Ac_A)W,\\
Y_+-Y_-&=d_Ad_W(a_WA-c_AW).
\end{aligned}}
\tag{31}
$$
返回权也不同：
$$
\boxed{
q_+=q\text{ 中 }H\text{ 及三个实参沿 (27) 移 }\Delta_+,
\quad \Delta_+=a_0d_AA,
}
$$
$$
\boxed{
q_-=q\text{ 中同样移 }\Delta_-,
\quad \Delta_-=a_0d_A(A+d_Wc_AW).
}
\tag{32}
$$
这保原 H 门，不是只保多项式。

若 $k\ge3$ 且 $2r-2>k$，(22) 同时位于 (30) 的两个域，
并且
$$
\boxed{v_p(Y_+)=k-1,\qquad v_p(Y_-)=k-3.}
\tag{33}
$$
(31) 中的最低项分别为 $d_Wa_WW$ 和 $d_Ad_Wc_AW$，
其它项赋值严格更大。两个乘数都是显示单位。
因此相同原点并没有相同返回环带。

在 R678 的 $k=r+m,\ n=r+M+j$、$m=0,1$、$j=0,\ldots,3$、
$M\ge2$、$r>M+3$ 且其实际较大 r 门下，以上条件均成立。
$A^2W$ 端的 H 移量赋值至少为 $2r-2$；
$WA^2$ 端的赋值为 $k-3$。
当 $k\ge N+3$ 时两者均可用 (28)，但其十二次项仍不同；
这没有把 R682 的原非零角域行认成 (31) 的另一个 Mellin 观察。

对 CM 标签 s，(30)–(32) 逐字变为 $A_s,W_s$，
观察变为 $sY_\pm\circ D_s^{-1}$，
完整权为 $q_\pm\circ D_s^{-1}$。
所有额外原 A/Q/L 条件、C 门和 H 门一起运输。

### 8.1 两词的准确齐次与非齐次算术比较

用 (15) 定义两词的完整 CM 加权环带行，
把 $f_w$ 换成 $1_{v_p(Y_\pm)=a}
\langle Y_\pm/p^a\rangle^{d_pw}$，记为
$\mathcal J_{\chi,\pm,a}$。
因为两词返回态是 $e_1,e_2$，新线、参考的符号相反。
例如参考行准确为
$$
\mathcal J_{H,+,a}
=\lambda^{N+3}c_H\beta^a
 \langle\lambda^2\rangle^{ad_pw}
 \langle2\rangle^{-d_pw}J_H(w),
$$
$$
\mathcal J_{H,-,b_0}
=-\lambda^{N+3}c_H\beta^{b_0}
 \langle\lambda^2\rangle^{b_0d_pw}
 \langle2\rangle^{-d_pw}J_H(w).
\tag{34}
$$
因此未知参考导数和固定尺度 log 在真实两词差中消去：
$$
\boxed{
\beta^{-a}\mathcal J_{H,+,a}'(0)
+\beta^{-b_0}\mathcal J_{H,-,b_0}'(0)
=\lambda^{N+3}c_H(a-b_0)d_p
 \log\langle\lambda^2\rangle(1+\lambda).
}
\tag{35}
$$
$a\ne b_0$ 时右边非零。
$\log\langle\lambda^2\rangle\ne0$ 仍由其全局 norm 为 $p^{-2}$、
从而不可能为根单位得到。
取 (33) 的 $a=k-1,b_0=k-3$，右边系数差恰为二。

新曲线对应的完整两行将 $c_HJ_H$ 换成 $(52/3)J_{\rm new}$；
其质量零，原 $J_{\rm new}'(0)=0$ 时两个中央均为零。
S 行按 R692 的正号系数 $\omega^2/2$ 返回同一原 $J_S$。
这些断言限于 (34) 的完整词域及全部 CM 分支。
把积分再限制到 (22) 或 (24) 后，余域仍必须保留。

## 9. 新接口及尚未消去的真实项

本文已把原第一 CM 投影与五种真实核心放在同一个固定覆盖、
完整三态和同一权上，给 (13)–(17) 的投影前算术词行。
特别 (25) 的同 R 比较及 (30)–(35) 的两词交叠，都包含原已付非零角域，
无需另造辅助来源或添加一条中央零。

尚未证明这些中央关系不相容。
必须继续处理的实际项是：

- 不同 s 的完整平移来源及 (18)、(24) 的不同管；
- (27)–(29) 的 A 端权差及浅层双 H 门；
- 同一角域上 (31) 的两种返回观察、(32) 的两种返回权；
- 从完整词域缩到角域时的全部补域和参考的非零质量。

这些项目全在本文的显示公式中，没有将一个源矩阵关系当作物理域关系，
也没有用一个局部非零或一个参考非齐次差替代主目标所需的全中央非零。

## 公开复现及依赖

只提交独立程序
[check-r695-cm-word-domains-and-a-z-carries.js](../scripts/check-r695-cm-word-domains-and-a-z-carries.js)。
运行参数为默认值；程序不读取任何旧证书，不依赖网络或第三方包。
命令：
$$
\texttt{node scripts/check-r695-cm-word-domains-and-a-z-carries.js}.
$$
按根规则 13，数值/精确检查交公开 Actions 运行；
本稿未在会话 V8 执行该程序。
运行号及暂态输出 SHA256 由主线程登记。
依根规则 15，不提交可重算 JSON、证书或 Actions 输出。

程序核 (20) 的全 CM 逆矩阵、各原投影、(27) 与 (31)–(32) 的
符号多项式、两词返回态、全部 216 CM 尺度的互异性和显示范数。
完整中心、整测度、所有域量词及算术返回由正文证明。

依赖：
[R487](R487-original-cm-mixed-tubes-and-common-core-reference-carry.md)；
[R488](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)；
[R483](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)；
[R465](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)；
[R679](R679-neutral-degree-twelve-three-s-and-exterior-return.md)；
[R678](R678-original-finite-word-corners-and-negative-one-return.md)；
[R682](R682-original-opposite-corners-and-uniform-unit-difference.md)；
[R686](R686-original-yz-core-and-same-source-st-unit-failures.md)；
[R692](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)。

## 已完成的公开脚本核对

公开 run [43684255990](https://github.com/Rogerhu12/math-research-public/actions/runs/43684255990)、job132721269948、source e335b329641fbc78c451bafa6285bf9be66a2ff1；本篇脚本默认参数退出0。脚本SHA256为832cd9145c575c322623195e18278a841faedb62850133c773a017bfe26cb939，stdout94170字节，SHA256为3c921df41731a29ac7a138e3d9cf2ffb881fdf8f88f35766e80b8a7a38cd3fab。只登记脚本/参数/run/hash，不保存可重算报告。首次run43683930350仅因stdout显示预算失败，本次完整hash核对成功；正文一般证明不依赖复跑门。
