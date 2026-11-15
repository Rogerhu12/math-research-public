# R764 — 保原 Y 与最终权的六度轴、三个 CD 域和同域外部首行

日期：2026-11-15。**状态：已证明。**

本文在同一个原六 sigma 联合中给出一条 degree 6 的完整轴核。该轴同时固定原 $Y$ 和最终实际测试 $q_N^*$，不更换原五十列逆、两条核修正、六支 carry 或任何 $\lambda,\kappa,\kappa^N$ 系数。它使三个 $\mathcal T$-旋转的 CD 域在足够深处准确合并；浅层只在精确环带上互斥，未被删除。

对原外部 $\mathcal O_{j,n}$，本篇给出全部原变量、单位条件及归一 $W_j$ 观察的同域返回。共同域上的两个 $W_j$ 行之差首项是同一个实际条件负一行，后续幂按真实三阶来源关系消去。这个首行尚未被赋零或非零；原 E 浅项和全部外部补偿继续保留。

## 1. 来源、参数和原实际权

固定
$$
\omega^2+\omega+1=0,\qquad \delta=1+2\omega,\qquad b=17,
$$
$$
\lambda=-\bar\pi_0^{-1},\qquad \beta=-\lambda,\qquad
\kappa=p\lambda^2,\qquad N\in4\mathbf Z_{>0}.
\tag{1}
$$
所有素数、固定坏集和整逆条件均沿 R734；不新增射线。
物理输入及来源为
$$
(\xi_1,\xi_2,\xi_3,x,c,d),\qquad
e_0=-\nu_\sigma^{\boxtimes6}/84,\qquad
h_W=\omega^2\mathcal T_*e_0,\qquad h_+=h_W+\tfrac12e_0.
\tag{2}
$$
这里 $h_W=e_1+e_2$ 是原 W 二挠来源，不与其他分支中同名 h 混用。

原观察和 carry 行保持为
$$
\begin{aligned}
A&=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,\\
Y&=A+c+2d,\qquad W=A+3\delta c+4d,\\
C&=(\xi_1-\xi_3+x)/\delta,\\
H_1&=-\xi_1+2\xi_2+\omega\xi_3-\omega^2x,\\
D&=\xi_1+\omega^2\xi_2-2\omega\xi_3+c+(2+3\omega)d,\\
F&=D+C,\qquad G=13H_1+(3-2\omega)F.
\end{aligned}
\tag{3}
$$
$q=q_N^*$ 始终表示 R734 的最终有界整测试。前一条 T 不变性注已经逐项证明：它的全部所选列、两条核修正及六支次数逆都只使用 C、F、G，且
$$
q\circ\mathcal T=q,\qquad
Y_*(q e_0)=\beta^N\nu_S,\qquad
Y_*(q h_W)=\omega^2\beta^N\nu_S.
\tag{4}
$$
这不是对 cd 返回权 $\Phi_N$ 的不变性声明。

以下对 $\mu\in\operatorname{span}_{\mathcal O}\{e_0,h_W\}$ 写
$\rho_\mu=q\mu$。特别 $h_+$ 也在此范围内。

## 2. 整数正交框架和完整半特征

定义
$$
\begin{aligned}
\mathfrak r&=(\xi_1-\omega^2\xi_3+\omega x)/\delta,\\
\mathfrak s&=\mathfrak r+c,\qquad
\mathfrak t=\mathfrak r-c,\\
\mathfrak B&=-\xi_1+\omega\xi_3-\omega^2x=H_1-2\xi_2.
\end{aligned}
\tag{5}
$$
使用行内积 $\langle L,M\rangle=L\bar M^{\,t}$。
$\mathfrak r,C,\mathfrak B$ 两两正交，范数分别为 $1,1,3$；
$\mathfrak s,\mathfrak t$ 范数均为 2，并彼此正交且垂直于
$C,\mathfrak B,\xi_2,d$。

清掉 p-unit $\delta$ 后，完整整数框架为
$$
L=
\begin{pmatrix}
1&0&-\omega^2&\omega&-\delta&0\\
1&0&-\omega^2&\omega& \delta&0\\
1&0&-1&1&0&0\\
-1&0&\omega&-\omega^2&0&0\\
0&1&0&0&0&0\\
0&0&0&0&0&1
\end{pmatrix},
\quad
L\xi=(\delta\mathfrak t,\delta\mathfrak s,\delta C,\mathfrak B,\xi_2,d)^t.
\tag{6}
$$
直接消去前两行的 c 列，剩下的三阶行列式为 $-3\delta$，给出
$$
\boxed{\det L=-18,\qquad
L\bar L^{\,t}=\operatorname{diag}(6,6,3,3,1,1).}
\tag{7}
$$
故这是当前 p 处的完整可逆格变换，未忘任何输入。

原 sigma 的 odd 半特征在 $O_K/2\simeq\mathbf F_4$ 的三个非零类上相同；CM 单位乘法保持该半特征。因此，第一、第二行各有四个非零模二系数，给标准 even 半特征；第三、第四行各有三个，给原 odd 半特征；最后两行各保一个原 odd sigma。结合 (7) 的全部交叉极化为零，原生成函数沿 $L^t$ 的实际拉回属于
$$
\boxed{
\mathcal S_6\boxtimes\mathcal S_6
\boxtimes\mathcal S_3^{\rm odd}\boxtimes\mathcal S_3^{\rm odd}
\boxtimes\mathcal S_1^{\rm odd}\boxtimes\mathcal S_1^{\rm odd}.
}
\tag{8}
$$
这里各因子都是同一 canonical rigidification；没有随其他五个变量变化的 flat twist。

为同时支付 $h_W$，在 $I=(\xi_1,\xi_3,x,c)$ 上保原矩阵
$$
\mathcal T_I=\frac12
\begin{pmatrix}
-\omega&1&\omega^2&\omega\\
-\omega^2&-\omega&1&-\omega^2\\
-1&-\omega^2&-\omega&1\\
-\omega&1&-\omega^2&-\omega
\end{pmatrix};
\tag{9}
$$
它固定 $\xi_2,d$。由 (5)、(9) 逐行相乘，
$$
\boxed{
\mathfrak s\mathcal T=\mathfrak s,\quad
\mathfrak t\mathcal T=\omega^2\mathfrak t,\quad
C\mathcal T=\omega^2C,\quad
\mathfrak B\mathcal T=\mathfrak B,
\quad
L\mathcal TL^{-1}=\operatorname{diag}(\omega^2,1,\omega^2,1,1,1).
}
\tag{10}
$$
所以 $h_W=\omega^2\mathcal T_*e_0$ 属于同一整张量格 (8)，带全部原常数。没有从它的某条边际反推整联合。

## 3. 绝对 whole 六度核及完整深度矩形

R529 §2 与 R533 §3 已在当前射线支付
$$
g_\pi\equiv7=1+6\pmod{12},\qquad g_\pi\equiv1\pmod6.
\tag{11}
$$
前式使整个标准 even $\mathcal S_6$ 的 canonical Heisenberg 交织为 scalar。真实非零锚
$\Theta(\delta z)\in\mathcal S_6$ 继承原 $\Theta$ 的核心 $\beta$，所以其绝对 normalized 算子为 $-I$。
同理，$\sigma(\delta z)\in\mathcal S_3^{\rm odd}$ 定标整个 odd 三度核为 $-I$；原 odd 一度核也为 $\beta$。这些绝对锚与固定 p-unit 拉回相容，未留一个未知中心标量。

对任一实际行 $M$ 和非零尺度 z，记
$$
P_{M,z}=I+\frac{z-1}{N(M)}\bar M^{\,t}M.
\tag{12}
$$
它把 M 缩放为 zM，并逐点固定 $M^\perp$。清分母 $\delta$ 不改变该投影或深度条件。

由 (8)–(11)，对 $\mu=e_0,h_W,h_+$，整个六轴独立深度矩形为
$$
\boxed{
\mu\big|_{\{L_i\in p^{m_i}\ (1\le i\le6)\}}
=\beta^{m_1+\cdots+m_6}
 \left(\prod_{i=1}^6 P_{L_i,\kappa^{m_i}}\right)_*\mu,
\qquad m_i\ge0.
}
\tag{13}
$$
各因子在 (13) 中真交换，且保全部未缩放伙伴。
带 $q$ 时仍须逐个运输它；只有下一节的轴已经证明逐点固定整个 q。

## 4. 新轴逐点固定原 Y 与最终 q

把 (3) 改写为
$$
F=\mathfrak s-\mathfrak B+\omega^2\xi_2+(2+3\omega)d,\qquad
G=13\mathfrak B+26\xi_2+(3-2\omega)F .
\tag{14}
$$
因此 C、F、G 全部不含 $\mathfrak t$。原六支测试的所有指示、全部次数逆和系数都原样固定：
$$
\boxed{q\circ P_{\mathfrak t,z}=q\qquad(z\ne0).}
\tag{15}
$$
这也对 R715 的真实中性测试 $\zeta_N^{(715)}$ 成立。

另一方面，令
$$
\mathfrak A_0=A-\mathfrak r
=2\delta\xi_2-\frac{4\delta}{3}\mathfrak B .
$$
则
$$
Y=\mathfrak A_0+\mathfrak s+2d,\qquad
\langle Y,\mathfrak t\rangle=0.
\tag{16}
$$
故得到完整带权返回
$$
\boxed{
\rho_\mu|_{\mathfrak t\in p^m}
=\beta^m(P_{\mathfrak t,\kappa^m})_*\rho_\mu,
\qquad m\ge0 .
}
\tag{17}
$$
它同时保原 Y 观察和其全部单位/深度事件。

原 full Y 核在 $e_0,h_W$ 上是实际 Y 反射，R638(11) 给
$K_Y\mu=R_Y\mu$。对 $h_W$ 也可直接由 (2)、$Y\mathcal T=Y$ 及 $\mathcal T$ 的 unitary 性运输原 $e_0$ 联合核。把反射放进物理尺度，并用 $q$ 对 Y 轴不变，得到
$$
\boxed{
\rho_\mu|_{\{Y\in p^n,\ \mathfrak t\in p^m\}}
=\lambda^n\beta^m
 (P_{Y,(-\kappa)^n}P_{\mathfrak t,\kappa^m})_*\rho_\mu .
}
\tag{18}
$$
这里两个物理映射真交换，不能将 $(-\kappa)^n$ 暗中换成 $p^n$。

设
$$
f_w(v)=1_{v\ {\rm unit}}\langle v\rangle^{d_pw},\qquad
d_p=p-1,\qquad J_S(w)=\int f_w\,d\nu_S.
$$
记 $c_{e_0}=1,c_{h_W}=\omega^2,c_{h_+}=-\delta/2$。由 (4)、(18)，
$$
\boxed{
\int_{\{Y\in p^n,\mathfrak t\in p^m\}}
 f_w\!\left(Y/(-\kappa)^n\right)d\rho_\mu
=\lambda^n\beta^{m+N}c_\mu J_S(w).
}
\tag{19}
$$
若 t 恰在第 m 环带，右边再乘 $1-\beta$。这只对 (19) 的 Y 观察成立；其他会沿 t 移动的观察须使用 (17) 的完整转置。
若采用 $Y/p^n$ 的另一归一，完整 Mellin 因子
$\langle(-\kappa/p)^n\rangle^{d_pw}$ 及其质量项必须保留。

所以原 $J'_S(0)=0$ 真传入 (19) 的整个矩形/环带行。下面附 CD、E 或另一 Y 的失败条件后，不从 (19) 自动赋零。

## 5. 三个 CD 域：共同深交与浅环带互斥

置
$$
a=1+3\omega,\qquad
c_j=c\mathcal T^j=\frac{\mathfrak s-\omega^{2j}\mathfrak t}{2},
\qquad j=0,1,2 .
$$
三个原观察准确为
$$
\boxed{
W_j=W\mathcal T^j
=Y+a\mathfrak s+2d-a\omega^{2j}\mathfrak t .
}
\tag{20}
$$
特别 $W-W'=(1-4\omega)\mathfrak t$。其范数 42 只是同一实际方向的清单位表达，不另设一个来源。

原 CD 域是
$$
\mathsf{CD}_{j,N}
=\{d\in p^N,\ \mathfrak s-\omega^{2j}\mathfrak t\in p^N\}.
\tag{21}
$$
因为 $1,\omega,\omega^2$ 两两之差为 p-unit，
$$
\boxed{
\mathsf{CD}_{i,N}\cap\mathsf{CD}_{j,N}
=\{\mathfrak s,\mathfrak t,d\in p^N\}
\quad(i\ne j).
}
\tag{22}
$$
所以任意两域的交就是三个的共同交。
在 $\mathfrak t\in p^N$ 上，三个 CD 门都变为
$\{\mathfrak s,d\in p^N\}$；在精确环带
$\mathfrak t\in p^m\mathcal O^\times,\ m<N$ 上，它们两两互斥，且分别迫 $\mathfrak s$ 也恰在第 m 环带。

对任意完整有界测试 f，真正返回为
$$
\boxed{
\begin{aligned}
&\int_{\mathsf{CD}_{j,N}\cap\{\mathfrak t\in p^m\mathcal O^\times\}}
 f\,d\rho_\mu\\
&\quad=\beta^m
\int_{\substack{\mathfrak t\ {\rm unit},\ d\in p^N\\
 \mathfrak s-\omega^{2j}\kappa^m\mathfrak t\in p^N}}
 f\circ P_{\mathfrak t,\kappa^m}\,d\rho_\mu .
\end{aligned}}
\tag{23}
$$
把两边的“精确环带”改为“至少 m 深”，则只去掉右边的
$\mathfrak t$-unit 指示，其他全不变。

因此 $m<N$ 时，**至少 m 深的整个域仍含共同深交**，不能把 (23) 的互斥性推广到它。对任意有限 $M\ge N$，
$$
1_{\mathsf{CD}_{j,N}}
=1_{\mathsf{CD}_{j,N}\cap\{\mathfrak t\in p^M\}}
+\sum_{m=0}^{M-1}
 1_{\mathsf{CD}_{j,N}\cap\{\mathfrak t\in p^m\mathcal O^\times\}} .
\tag{24}
$$
(24) 保整个深尾，包括 $\mathfrak t=0$；没有使用 $\beta$ 为收缩因子，它实际是单位。

即使 $m\ge N$ 使三个 CD 门相同，(20) 的观察仍准确变为
$Y+a\mathfrak s+2d-a\omega^{2j}\kappa^m\mathfrak t$，不能把三条 W 行相认。

## 6. 原 E 浅门的完整移动

R686 的纯 Y/W 伙伴为
$$
E=(5+6\omega)A-29c-(58+87\omega)d.
$$
由 (5)、(16)，
$$
\boxed{
\begin{aligned}
E&=E_\perp+(17+3\omega)\mathfrak t,\\
E_\perp&=(5+6\omega)\mathfrak A_0
 +(-12+3\omega)\mathfrak s-(58+87\omega)d .
\end{aligned}}
\tag{25}
$$
$E_\perp\perp Y,\mathfrak t$，且 $E_\perp\mathcal T=E_\perp$。
若原门随三阶几何一起运输，则
$$
E_j=E\mathcal T^j=E_\perp+(17+3\omega)\omega^{2j}\mathfrak t.
$$
真实 t 返回分别为
$$
\boxed{
E\longmapsto E_\perp+(17+3\omega)\kappa^m\mathfrak t,\qquad
E_j\longmapsto E_\perp+(17+3\omega)\omega^{2j}\kappa^m\mathfrak t .
}
\tag{26}
$$
Y 缩放不改变这些行。对 $m\ge N$，E 深 N 的返回门准确是
$E_\perp\in p^N$，浅门是其补集；它们不是原 E 门。
对 $m<N$，必须保 (26) 的整条混合指示。所有原 reference 项按相同式运输，不删除 E 浅部分。

## 7. 原 O 外部的完整同域返回

保 R713 的原邻观察 $Y_1=Y+c-3d$。当 $n\ge N$ 时，其三个真实三阶像为
$$
\mathcal O_{j,n}
=\{Y\in p^n,\ c_j,d\in p^N,\ c_j-3d\notin p^n\}.
\tag{27}
$$
原规范 T 观察是
$$
W_j\circ P_{Y,r_n}^{-1},\qquad r_n=(-\kappa)^n .
\tag{28}
$$
这里仍使用对应的 $W_j$，不是保域却换回 $W_0$。

定义两个实际 Y 正交伙伴
$$
\widehat{\mathfrak s}=\mathfrak s-Y/17,\qquad
\widehat d=d-Y/17 .
\tag{29}
$$
因为 $\langle\mathfrak s,Y\rangle=\langle d,Y\rangle=2$、
$N(Y)=34$，二者都垂直于 Y。令
$$
H_{j,m}=\widehat{\mathfrak s}-\omega^{2j}\kappa^m\mathfrak t,\qquad
b_Y=(20+3\omega)/17 .
$$
在 $M=P_{Y,r_n}P_{\mathfrak t,\kappa^m}$ 下，准确有
$$
\begin{aligned}
d\circ M&=\widehat d+r_nY/17,\\
c_j\circ M&=H_{j,m}/2+r_nY/34,\\
(c_j-3d)\circ M&=H_{j,m}/2-3\widehat d-5r_nY/34 .
\end{aligned}
\tag{30}
$$
$n\ge N$ 使 (30) 中的 $r_nY$ 项分别属于所需深度。因此在 Mellin 单位支上，整个返回域为
$$
\boxed{
\mathcal D_{j;n,m,N}
=\{Y\ {\rm unit},\
 \widehat d\in p^N,\
 H_{j,m}\in p^N,\
 H_{j,m}/2-3\widehat d\notin p^n\}.
}
\tag{31}
$$
除 Y-unit 以外，(31) 的全部行都在 $Y^\perp$。

同一映射将完整归一观察变为
$$
\boxed{
W_j\circ P_{Y,r_n}^{-1}\circ M
=b_YY+aH_{j,m}+2\widehat d .
}
\tag{32}
$$
在 (31) 的伙伴门上，后两项属于 $p^N$，而 $b_Y$ 是原射线单位；所以 (32) 的 unit cut **准确**等价于 Y-unit。这解释 (31) 的单位指示，不是预设均匀性。

由 (18) 得到整 Mellin 恒等式
$$
\boxed{
\begin{aligned}
&\int_{\mathcal O_{j,n}\cap\{\mathfrak t\in p^m\}}
 f_w(W_j\circ P_{Y,r_n}^{-1})\,d\rho_\mu\\
&\quad=\lambda^n\beta^m
 \int_{\mathcal D_{j;n,m,N}}
 f_w(b_YY+aH_{j,m}+2\widehat d)\,d\rho_\mu .
\end{aligned}}
\tag{33}
$$
S 观察的同式是把右侧观察换成 Y，左侧换成 $Y/r_n$。
若限制 t 的精确第 m 环带，则右侧再附 $\mathfrak t$-unit；
所有 E 门按 (26) 附上。

特别，T 行减去
$\langle b_Y\rangle^{d_pw}$ 乘对应 S 行的中央导数为
$$
\boxed{
\lambda^n\beta^m d_p
 \int_{\mathcal D_{j;n,m,N}}
 \log\!\left(1+\frac{aH_{j,m}+2\widehat d}{b_YY}\right)
 \,d\rho_\mu .
}
\tag{34}
$$
这个精确相对式保质量项，未把 $\log\langle b_Y\rangle$ 单独丢掉。

三个深度范围须区分：

- 在精确 t 第 m 环带、$m<N$ 时，三个 CD 返回门互斥。
- 当 $N\le m<n$ 时，三个 CD 返回门已相同，但
  $H_{j,m}/2-3\widehat d\notin p^n$ 的失败门仍可能不同。
- 当 $m\ge n$ 时，三个完整 O 返回域都准确等于
  $$
  \boxed{
  \mathcal D^\infty_{n,N}
  =\{Y\ {\rm unit},\
     \widehat{\mathfrak s},\widehat d\in p^N,\
     \widehat{\mathfrak s}/2-3\widehat d\notin p^n\}.
  }
  \tag{35}
  $$

在最后范围，E 深/浅 N 门也都返回同一个 $E_\perp$ 门。
但三个观察仍不同，这个差正由下一节支付。

## 8. 同域三阶消去和真正条件负一首行

固定 $m\ge n\ge N$。可以在 (35) 附任何已明确运输且
$\mathcal T$-不变的伙伴门，例如 $E_\perp$ 深/浅 N，
以及 $\mathfrak t$-unit；记整个域为 $\mathcal D$。
置
$$
P=b_YY+a\widehat{\mathfrak s}+2\widehat d.
\tag{36}
$$
P 在 $\mathcal D$ 上为单位，$\mathcal TP=P$，
$P-b_YY\in p^N$。三个归一观察是
$P-a\omega^{2j}\kappa^m\mathfrak t$。

令
$$
L_\ell^\mu(\mathcal D)
=\int_{\mathcal D}\mathfrak t^\ell P^{-\ell}\,d\rho_\mu .
\tag{37}
$$
前一条完整两态身份是
$$
(\mathcal T_*)^2+\omega\mathcal T_*+\omega^2I=0
\quad\hbox{于 }\operatorname{span}\{e_0,h_W\}.
\tag{38}
$$
域、q、P 都被 $\mathcal T$ 固定，而
$\mathfrak t\mathcal T=\omega^2\mathfrak t$。
把 (38) 配对 (37)，严格得到
$$
\boxed{L_\ell^\mu(\mathcal D)=0\quad(\ell\equiv2\pmod3).}
\tag{39}
$$
这保整个原域，不是只对无条件质量作角型筛选。
同时，对 $\ell\equiv1\pmod3$，
$L_\ell^{h_W}=\omega L_\ell^{e_0}$。

在共同域比较两条 (33) 的 T 中央行，常数 $\log P$ 及质量完全消去。对所有 $j,k$，准确有
$$
\boxed{
\begin{aligned}
I_j^\mu-I_k^\mu
={}&-(\omega^{2j}-\omega^{2k})\lambda^n\beta^m d_p\\
&\cdot\sum_{r\ge0}
 \frac{a^{3r+1}\kappa^{m(3r+1)}}{3r+1}
 L_{3r+1}^\mu(\mathcal D).
\end{aligned}}
\tag{40}
$$
这里 $I_j^\mu$ 表示 (33) 中对应共同域的中央导数。
$\ell\equiv0\pmod3$ 项由 j、k 的差消去，
$\ell\equiv2\pmod3$ 项由 (39) 消去。
因 $m\ge1$ 且 q 为原有界整测试，级数一致收敛，且
$$
\boxed{
I_j^\mu-I_k^\mu
=-a(\omega^{2j}-\omega^{2k})\lambda^n\beta^m
 d_p\kappa^m L_1^\mu(\mathcal D)+p^{4m}\mathcal O .
}
\tag{41}
$$
对余项使用
$m\ell-v_p(\ell)\ge4m$ 于 $\ell=4,7,10,\ldots$，
没有把固定 p 的全部高阶项删成零。

进一步，由 (36) 在同一域给
$$
\boxed{
L_1^\mu(\mathcal D)
=b_Y^{-1}
 \int_{\mathcal D}\frac{\mathfrak t}{Y}\,d\rho_\mu
 +p^N\mathcal O .
}
\tag{42}
$$
因此 (41) 的首行是真正原 q、原失败门和原 E 条件下的 Y 负一行，不是另一个裸 sigma 或裸连接来源。

若去掉 Y-unit 后将 (42) 的其余有限伙伴门记为
$\mathcal D_\perp$，其实际条件来源为
$$
\Lambda_{\mu;n,N}
=Y_*\!\left(1_{\mathcal D_\perp}\,
            \mathfrak t\,q_N^*\,\mu\right).
\tag{43}
$$
所有门和 carry 行都在 $Y^\perp$；由原整 Y 框架及 R745 的有限伙伴收缩，(43) 属于原标准 $\mathcal S_{34}$。
各实际 q 项总次数为 $0\bmod6$，门为齐次零陪集，
乘 $\mathfrak t$ 后使其型为 5。因此它落在完整五维 type 5 空间。
这只定位真实有限来源；没有证明它等于 R735 的某条裸线、
R761 的 $D_S$，或已知非零负一值的固定倍数。
(42) 读取的是 (43) 自己的完整单位负一矩。

## 9. 与原中央和全部补域的准确范围

本篇新增的原算术零传播是 (19)：同一个最终 q 的完整 Y/t
深度矩形及其精确 t 环带回原 $J_S$。
它与 (23)、(33) 的切集返回可以同时使用，但附加 CD、另一 Y 失败或 E 浅条件后，必须保其完整补集。

对每个原 CD/O 行，(24) 给有限、互不重叠的实际环带分割；
共同深域、三个浅独占支以及域外部分都在。
当 $m\ge n$ 时，(35)–(42) 确实给同一域上的观察比较，
但该域并不是 (19) 的整个 Y/t 矩形。
所以原 $J'_S=J'_T=0$ 尚不强迫 (37)、(42) 为零；
也不能由一个条件首行非零删掉原总行的外部相反补偿。

所有 R737 的 $I/O/X$、原 $\Phi_N$ 与 q 的区别、
E 浅参考项及原 $\pi_4$ 中性方向均保留。
尤其 (15) 不表示 q 独立于其他新框架轴，(10) 也不表示
cd 返回后的 $\Phi_N$ 被 $\mathcal T$ 固定。

## 依赖与执行范围

- [R493](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)：原三阶几何与完整来源常数。
- [R529](R529-original-low-j-k-core-and-complete-st-carry.md) §2、
  [R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md) §3：
  标准 even 六度及 odd 三度的完整中心、绝对锚和全部伙伴范围。
- [R638](R638-original-yw-three-state-and-word-compensation.md)：
  含实际 Y 反射的整联合核。
- [R686](R686-original-yz-core-and-same-source-st-unit-failures.md)：
  原 $b_Y,E$ 及完整单位进入/失败支。
- [R713](R713-symmetric-frozen-sources-and-exact-paired-mixed-remainder.md)、
  [R737](R737-common-depth-elimination-and-native-primitive-strips.md)：
  原 CD/O 定义与规范观察。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：
  原最终测试、完整系数与整性。
- [R745](R745-finite-p-gates-algebraic-theta-sources-and-orthogonal-jets.md)：
  有限纯伙伴门及正矩收缩的真实代数 theta 来源。
- [最终 carry 的 T 不变性](../notes/2026-11-15-final-carry-t-invariance-and-same-weight-states.md)、
  [四单反射与保 x 边界](../notes/2026-11-15-four-input-reflections-and-x-preserving-boundary.md)：
  同一权、原两态及三个真实转置域。

本篇是所列完整来源与显示矩阵的代数推导，没有新增数值运行、
辅助素数计算或可重算输出数据。
