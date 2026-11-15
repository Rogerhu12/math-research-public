# R837 — 原三长行的七倍根能量与无重数上界的统一约束

日期：2026-11-15。**状态：下列目标素数内的局部能量、实际因子截除和全来源必要界已证明。主目标仍未完成。**

本篇使用 R821 原四块矩阵中三条真正的长 Euler 行。
局部最佳常数是七：三个不同简单根等距靠近原轴时可以达到它，
不能把纯重复因子的八倍界用于全部候选。

此外，高重数因子的总实际接触由同一原次数帽控制。
把这些因子从已知三个长零中准确除去，只损失一个可估计的小量；
剩余重数有界的因子再使用 R680 的完整十九角交数。
由此无需假定实际因子重数预先有统一上界，得到
$$
p\le\frac{141}{14q}D^2+o(D^2)
$$
这一真正目标 $p$ 的必要条件。这里 $q$ 是同一候选的 charge 支持同余模数。
原四块的自然三长临界排除 $q\ge3$；若在旧两长维数临界内另有真实第三长行，
则排除 $q\ge2$。两个临界比例分开读取。

## 1. 原全部来源、物理长度和三个低段零

保 R672/R680 的完整 canonical 来源
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},\qquad
\mathcal E=Y\partial_Y,
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad
C_n=\lfloor n/2\rfloor,
$$
$$
f_D=\lfloor9D/2\rfloor+4<p,\qquad
e_{n+1}=f_n-3A_n-B_n+C_n.
\tag{1}
$$
这里只使用已经整付的这个原格；不将独立 $T^j$ 或新角来源并入。

设 $p=6s-1>211$，并使用 R821 的原
$\Gamma^{(4)}_{3s+\ell+13}$，$1\le\ell<s-13$。
对非零约化候选 $\bar P$，置
$$
\widehat P=d^{C_D}\bar P,\qquad
r=\operatorname{ord}_t\widehat P,\qquad
M_D=f_D+C_D=5D+4-(D\bmod2).
$$
完整原帽给
$$
\deg_t\widehat P\le M_D,\qquad\deg_Y\widehat P\le D<p.
\tag{2}
$$
令
$$
(\Delta,H)=
\begin{cases}
(0,s),&\bar P\in\ker\bar J_4,\\
(13,s-13),&\bar P\in\ker\bar M_4^{\rm orig}.
\end{cases}
\tag{3}
$$
R821(33)–(40) 和原单位下三角运输准确给
$$
\boxed{
\widehat P(t,g),\quad
(\mathcal E\widehat P)(t,g),\quad
(\mathcal E^2\widehat P)(t,g)\in t^Hk[[t]].
}
\tag{4}
$$
它保全部 $P_{134}/U_0$、总 charge 四十、三条十三行带；
不是把旧两长一短的第三行扩成 $H$。

在 $t=0$ 只有 $n=0,1,2$ 的原列能非零。
(4) 的三条常数行在这些列上的 $1,n,n^2$ 是单位 Vandermonde，
故
$$
1\le r\le M_D.
\tag{5}
$$
若 $r\ge H$，直接有 $p\le6(M_D+\Delta)-1$。
以下取 $r<H$，置 $S=H-r>0$。
除去真实 $t^r$ 后，三个零的长度均为 $S$。

$g$ 只使用原模 $t^s$ 低轴，满足
$g\equiv(1+8t)\Theta^{17}\pmod{t^s}$ 的已付 ODE 数据。
为记根接触可以任选它的形式延拓；所有 $\min(h_j,s)$ 均不依赖这个选择。
不在普通 $k((t))$ 中假设全 sigma 或全 Gaussian 连接存在。

若原完整 $M_4$ 的一个 primitive 模 $p^2$ 或更深右核已给出，
则其约化必须属于 $\ker\bar J_4$。
理由是原 $m_{13}$ 的 Smith 因子只有单位和一次 $p$：
$m_{13}J_4(P)\in p^2$ 强迫 $J_4(P)\in p$。
所以这类候选可用 (3) 的 $\Delta=0$，
但本篇不把该必要条件认成充分条件。

## 2. 三个 jet 的七倍加权根引理

在代数闭剩余域的共同 tame Puiseux 扩张中，令
$$
f(t,Y)=U(t,Y)\prod_{j=1}^c(Y-\psi_j(t))^{m_j},
\quad U(0,1)\ne0,\quad \psi_j(0)=1,
$$
其中 $\psi_j$ 两两不同，$m_j>0$，且 $\sum_jm_j<p$。
令 $g_0(0)=1$，并假定
$$
f(t,g_0),\quad f_Y(t,g_0),\quad f_{YY}(t,g_0)\in t^S,
\qquad0<S\le s.
\tag{6}
$$
由于 $Y$ 在原点为单位，原 $\mathcal E^0,\mathcal E^1,\mathcal E^2$
三行与 (6) 通过单位三角矩阵等价。

记
$$
h_j=\operatorname{ord}_t(\psi_j-g_0),\quad
\bar h_j=\min(h_j,s),\quad
d_{ij}=\operatorname{ord}_t(\psi_i-\psi_j).
$$
允许 $h_j=\infty$。定义与 R672/R680 相同的能量
$$
\mathscr E(f)=
\sum_jm_j^2\bar h_j+
6\sum_{i<j}m_im_jd_{ij}.
\tag{7}
$$

**引理 1。**
$$
\boxed{\mathscr E(f)\ge7S.}
\tag{8}
$$

**证明。** 先设全部 $h_j\le s$。置
$$
M(x)=\sum_{h_j\ge x}m_j,\qquad
Q(x)=\sum_{h_j\ge x}m_j^2,\qquad
H_f=\sum_jm_jh_j,\qquad w=\max h_j.
$$
由 $d_{ij}\ge\min(h_i,h_j)$，
$$
\mathscr E(f)\ge\int_0^w(3M(x)^2-2Q(x))\,dx.
\tag{9}
$$
积分只是有理分段常数的实数求和，不是正特征中的形式积分。

按达到 $w$ 的不同最近根数分类。

**只有一个最近根，重数 $m\ge2$。**
$f_{YY}/f$ 在该根的首项为
$m(m-1)/(g_0-\psi)^2$，其它项有更高赋值。
$m,m-1$ 在特征 $p$ 下均为单位，故
$H_f-2w\ge S$。
因为 $Q\le M^2$ 且
$M^2\ge7(M-2)$ 对一切实数 $M$ 成立，
(9) 至少为 $7(H_f-2w)\ge7S$。

**只有一个最近根，重数为一。**
$f_Y(t,g_0)$ 的阶准确是其余根的总接触
$H_{\rm far}=H_f-w\ge S$。
该最近根与其余根的交叉项至少为 $6H_{\rm far}$，
其余根的自项至少为 $H_{\rm far}$，已给 (8)。

**恰有两个不同最近根。**
写其首差为 $c_1t^w,c_2t^w$，$c_i\ne0$，重数为 $m_1,m_2$。
设
$$
A_1=m_1/c_1+m_2/c_2,\qquad
A_2=m_1/c_1^2+m_2/c_2^2.
$$
若 $A_1\ne0$，一阶导数给 $H_f-w\ge S$。
若 $A_1=0$，则
$$
A_2=\frac{m_1(m_1+m_2)}{m_2c_1^2}\ne0;
$$
这里 $m_1+m_2<p$，故二阶导数给更强的 $H_f-2w\ge S$。
所以总有 $H_f-w\ge S$。
每个活动集合至少含两个不同根，
$Q\le(M-1)^2+1$，从而
$$
3M^2-2Q\ge M^2+4M-4\ge7(M-1).
$$
代回 (9) 得 (8)。这也包括 $c_1=c_2$ 的情形；
此时 $A_1=(m_1+m_2)/c_1$ 已非零。

**至少三个不同最近根。**
每个活动集合至少含三个不同根，
$Q\le(M-2)^2+2$，于是
$$
3M^2-2Q\ge M^2+8M-12\ge7M\qquad(M\ge3).
$$
所以 (9) 至少为 $7H_f\ge7S$。不需要预判导数相消。

现在处理截断。
若至少两个根有 $h_j\ge s$，两个自项与它们的交叉项已经至少为
$8s\ge7S$。
若只有一个这样的根且其重数至少三，自项至少为 $9s$。
若唯一该根重数为二，将
$f=(Y-\psi)^2U_1$ 在原轴求二阶导数；
其它根接触均严格小于 $s$，故首项准确是 $2U_1(t,g_0)$，
其阶 $H_{\rm far}\ge S$。
该根与其余根的交叉项至少为 $12H_{\rm far}$。
重数为一时同理由一阶导数给 $H_{\rm far}\ge S$，
交叉项与其余自项至少为 $7H_{\rm far}$。
若 $\psi=g_0$ 为无穷接触，直接对这两个因式求导得到相同结论，
无须在零值处作对数除法。证毕。

常数七是这个能量的真实最佳常数：
在 $p>3$、$3a\le s$ 时取 $g_0=1$、
$f=(Y-1)^3-t^{3a}$。
三个不同简单根均接触 $a$，三个 jet 满足长度 $S=3a$，
而 (7) 等于 $3a+18a=7S$。
这只是局部最佳性的例子，不把该多项式当作原来源。

## 3. 原十九角全局支付

本节直接使用 R680 已逐十九角证明的原几何结论。
$\widehat P$ 是原 nef 类 $\mathcal B_D$ 的实际截面，且
$$
\mathcal B_D^2=\frac{47}{12}D^2+O(D).
\tag{10}
$$
有限参数始终使用 R680 的十九个真实取整重数定义的准确整数 $\mathcal B_D^2$。

对任一接触原单位轴的几何整非垂直因子 $F_i$，
令其严格变换为 $C_i$，$a_i=\deg_tF_i,\ b_i=\deg_YF_i$。
原同一 Euler forcing 给非零截面
$$
K_{F_i}^E|_{C_i}\in
H^0(C_i,\mathcal O_{C_i}(3C_i+L)),
\qquad L.C_i\le8b_i.
\tag{11}
$$
它在每个 $(0,\zeta)$ 支付
$$
I_{(0,\zeta)}(C_i,K_{F_i}^E)
\ge\sum_j\min(h_{ij},s)+3\Delta_{i,\zeta}.
\tag{12}
$$
完整判别式 $\Delta_{i,\zeta}$ 包括全部奇支和切向根；
额外一份 $t$ 正好补回 ODE 导数的一阶损失。
(11) 不把 forcing 免费返回原 $\mathcal W_D$，
本篇只用它的几何零极次数。

所有 $C_i$ 为 nef。若 $\mathscr C=\sum_i m_iC_i$ 是任一接触因子子和，
则原实际有效余除子给
$$
\mathcal B_D\sim\mathscr C+\Delta_{\rm eff},\qquad
\mathscr C^2\le\mathcal B_D^2.
\tag{13}
$$
两不同因子的局部根交数由 $C_iC_j$ 支付。
所以在任意若干原单位点应用引理 1 后，(11)–(13) 给
$$
\sum_\zeta\mathscr E_\zeta
\le3\mathscr C^2+\sum_i m_i^2LC_i
\le3\mathcal B_D^2+8m_{\max}\sum_i m_ib_i.
\tag{14}
$$
这里重复因子的 $m_i^2$ 始终保留。

假定原 charge 支持全落在一个模 $q$ 类，$1\le q\le D<p$。
实际恒等式
$$
\widehat P(t,\zeta Y)=\zeta^{n_*}\widehat P(t,Y)
\quad(\zeta\in\mu_q)
$$
把 (4) 的三个已有 jet 同时送到 $q$ 个互异点 $(0,\zeta)$。
因此先有不删任何因子的有限界
$$
\boxed{
7q(H-r)\le
3\mathcal B_D^2+8m_{\max}B_{\rm ct},
\qquad B_{\rm ct}=\sum_i m_ib_i\le D.
}
\tag{15}
$$
R680 的实际因子轨道还给 $m_{\max}\le\lfloor(D-n_*)/q\rfloor$。
没有新增中央零或变动几何轴的算术授权。

## 4. 高重数因子的实际接触可以统一截除

关键是消掉 (15) 中可能为二次主项的 $m_{\max}B_{\rm ct}$，
不能先假设所有重数有固定上界。

固定整数 $K\ge2$，把接触这些 $q$ 个点且重数 $m_i>K$ 的因子合为
$P_{\rm hi}=\prod_{m_i>K}F_i^{m_i}$。
原次数逐因子相加，给
$$
\sum_i m_ia_i\le M_D,\qquad
\sum_i m_ib_i\le D.
\tag{16}
$$
原 $\mathbb F_4$ 类和吹起只减自交，故
$$
C_i^2\le4b_i^2+2a_ib_i.
\tag{17}
$$
于是任一高重数因子的全部截断接触满足
$$
\sum_{\zeta,j}\min(h_{ij},s)
\le3C_i^2+8b_i
\le
B_K:=\frac{12D^2+6M_DD}{(K+1)^2}
       +\frac{8D}{K+1}.
\tag{18}
$$
以下假定
$$
\boxed{B_K<s.}
\tag{19}
$$
若没有高重数因子，则无需该门。
由 (18)–(19)，这些因子的每个实际接触都严格小于 $s$；
故没有未知高尾或无穷接触，截断可全部去掉。

令
$$
A_\zeta=\operatorname{ord}_tP_{\rm hi}(t,\zeta g),\qquad
b_\zeta=\max\{h_{ij}\text{ 属于该点的高重数因子}\},
$$
空集合时置二者为零。
每个这类根的重数至少 $K+1$，因此
$$
b_\zeta\le A_\zeta/(K+1).
\tag{20}
$$
由 (11)–(12)、(16)–(17) 的全点总和，
$$
\begin{aligned}
\sum_\zeta A_\zeta
&\le\sum_{m_i>K}m_i(12b_i^2+6a_ib_i+8b_i)\\
&\le
\mathcal A_K:=
\frac{D(12D+6M_D)}{K+1}+8D.
\end{aligned}
\tag{21}
$$
这里是全部 $q$ 个点的总量，不在右边再乘一个 $q$。

在每个点，把真实多项式
$t^{-r}\widehat P$ 除以其实际因子 $P_{\rm hi}$。
剩余多项式仍正则。对原 Euler 商法则，
$$
v\!\left(\frac{\mathcal EP_{\rm hi}}{P_{\rm hi}}\right)\ge-b_\zeta,
\qquad
v\!\left(\frac{\mathcal E^2P_{\rm hi}}{P_{\rm hi}}\right)\ge-2b_\zeta.
$$
从完整的两次商求导逐项得到，余多项式的三个 jet 均至少消到
$$
S_\zeta'=S-A_\zeta-2b_\zeta.
\tag{22}
$$
例如二阶式的四项为
$f''/Q-2f'Q'/Q^2-fQ''/Q^2+2f(Q')^2/Q^3$，
这里导数全取 $\mathcal E$；各项均满足 (22)。
因此没有把除因子视为不损 jet。

若 $S_\zeta'\le0$，只用能量非负；
若 $S_\zeta'>0$，它仍不超过 $S\le s$，引理 1 适用。
可用实数长度读取该不等式，或取上整后的整数零阶，所得下界相同。

余下所有接触因子重数不超过 $K$。
其 nef 子和仍满足 (13)，所以 (14) 的固定极成本至多为 $8KD$。
加总引理 1，再用 (20)–(22)，得到完全有限的原界
$$
\boxed{
7q(H-r)\le
3\mathcal B_D^2+8KD+
7\left(1+\frac{2}{K+1}\right)
 \left(\frac{D(12D+6M_D)}{K+1}+8D\right).
}
\tag{23}
$$
不要求余多项式本身属于 $\mathcal W_D$：
它的每一个因子仍是同一原截面的实际因子，
且 (13)、(16) 的成本均来自原 $\widehat P$。
这与免费向来源格添加商列不同。

所有 Puiseux 扩张都是 tame：
原总 $Y$ 次数低于 $p$，不可分因子不可能出现，
分裂群阶整除 $D!$，因而素于 $p$。
引理 1 所用 $m,m-1,m_1+m_2$ 的单位性也来自同一个真实次数门。

## 5. 不预设重数上界的统一主项

考虑 $D\to\infty$ 且 $p/D^2$ 有正下界的实际候选序列。
取 $K=\max(2,\lfloor\sqrt D\rfloor)$。
由 $M_D=5D+O(1)$，(18) 的 $B_K=O(D)$，
而 $s\gg D^2$，所以 (19) 最终自动成立。

(23) 因而给
$$
\boxed{
7q(H-r)\le3\mathcal B_D^2+O(D^{3/2}).
}
\tag{24}
$$
误差常数可由 (23) 直接读取，并且对 $1\le q\le D$ 一致。
结合 $r\le M_D$、$\Delta\in\{0,13\}$ 及 $p=6s-1$，
得到
$$
\boxed{
p\le\frac{18}{7q}\mathcal B_D^2+O(D^{3/2})
=\frac{141}{14q}D^2+o(D^2).
}
\tag{25}
$$
$r\ge H$ 的简单门仅为 $p=O(D)$，在当前序列本来不可能。
只有单一 charge 的来源同样只有 $O(D)$ 接触门，
所以不漏掉该情形。

相同的因子截除也可用于旧两个长零：
在 R672 四倍能量中，商求导仅损 $A_\zeta+b_\zeta$。
因此没有第三长行时，准确对应式是
$$
4q(H-r)\le3\mathcal B_D^2+8KD+
4\left(1+\frac1{K+1}\right)\mathcal A_K,
$$
并在同一二次区得到
$$
\boxed{p\le\frac{141}{8q}D^2+o(D^2).}
\tag{26}
$$
这是去掉 R680“重数有固定上界”附加条件后的统一主项。
旧 $q=3$ 在其两长临界仍恰好取主项等号；
(26) 没有排除这个边界。

## 6. 两个真实临界窗口分开读取

原来源维数是
$$
\dim\mathcal W_D=\frac{47}{24}D^2+O(D).
$$

若使用原四块的三个满块、$\ell=o(D^2)$，其自然维数临界为
$$
3s+\ell=\dim\mathcal W_D+o(D^2),
\qquad p/D^2\longrightarrow47/12.
\tag{27}
$$
对 $q\ge3$，(25) 的右侧主系数至多
$$
141/42=47/14<47/12.
$$
所以在 (27) 中，充分大时非零候选的 charge 差最大公因数只能为
$$
\boxed{1\ \text{或}\ 2.}
\tag{28}
$$

若另一方面，仍在旧两长的维数临界
$p/D^2\to47/8$ 中，另外确有 R821 的第三条真实长行，
则 $q\ge2$ 时 (25) 的主系数至多
$$
141/28<47/8.
$$
因此这个更小预算中的三长候选只能有
$$
\boxed{\gcd\{\text{非零 charge 差}\}=1.}
\tag{29}
$$
(29) 不对只有旧两长一短的来源适用。
两个结论都保 $\Delta=13$ 的完整物理窗口；
若已经给出 primitive 更深核，则可用 $\Delta=0$ 的准确较强有限门。

本篇没有排除 (28)–(29) 剩下的稠密混合来源，
也没有判定 R836 的指定仿射成员性或原同一 $R$ 的下一位。
能量、因子截除和 nef 比较均使用同一实际 $\widehat P$；
没有新增中央零、未付的因子列或辅助素数单位子式。
