# R672 — 原两长 jet 的加权根能量与 charge 同余类限制

日期：2026-11-15。**状态：以下目标素数内的必要条件已证明。**

本篇直接使用原 $P$ 与 $\mathcal EP$ 的两个长零，而不借辅助素数。
在 R467 的分支结果式中保留完整判别式，可以同时处理任意重复因子、
切向分支和不同因子间的接触。其局部加权量至少为两 jet 长度的四倍；
全局则由清角后的真实次数控制。

对整个 canonical $J=0$ 来源，得到一个新的统一平方根下界。
进一步，若同一候选的全部原 charge 落在一个模 $q$ 类，
其有效径向次数降为原次数的 $1/q$，而原两 jet 和 ODE 首共振仍保留。
在低 $\ell$ 的真实维数临界序列中，这排除所有 $q\ge8$，
特别排除只占一个模十二 canonical 块的候选。
它没有排除混合这些余类的稠密高次数首核，也没有判定其同一个 $R$ 的第二 forcing。

## 1. 同一个原来源和可用的长 jet

保持
$$
p=6s-1>101,\quad 1\le\ell<s-13,\quad
f_D=\lfloor9D/2\rfloor+4<p,
$$
以及原固定坏集排除。来源为
$$
\mathcal W_D=\bigoplus_{n=0}^{D}
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},\qquad \mathcal E=Y\partial_Y,
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},
\quad h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
e_{n+1}=f_n-3A_n-B_n+C_n.
\tag{1}
$$
只讨论这份真实 $J=0$ 子格。一般含独立 $T^j$ 的更大来源不能仅因存在这个子格便套用本篇的核排除。

剥去原完整共同目标单位后，相对 $J$ 的三块模 $p$ 仍准确读
$$
P(t,g)_{<s},\qquad
a(\mathcal EP)(t,g)_{<s},\qquad
\frac{a^2}{2}(\mathcal E^2P)(t,g)_{<\ell},
\tag{2}
$$
其中 $a$ 是原 Gaussian 单位，$g\equiv\rho\pmod{t^s}$，
$\rho=(1+8t)\Theta^{17}$。换参是已付的原整单位换参。

为同时说明完整 $M$ 的范围，令
$$
\Delta=
\begin{cases}
0,&\bar P\in\ker\bar J,\\
13,&\bar P\in\ker\bar M,
\end{cases}
\qquad H=s-\Delta.
\tag{3}
$$
这里 $M=c_*U_0m_{13}J$，先取整个 $(c_*U_0)^{-1}$，
再读取两条实际十三行 carry。两种情况均给
$$
P(t,g),\quad(\mathcal EP)(t,g)\in t^Hk[[t]].
\tag{4}
$$
它们还保留第三块的原低 $\ell$ 行。

特别，由 R449 的完整精确序列，
$$
\bar P\in K_2^{\rm red}(M)\Longrightarrow\bar P\in\ker\bar J.
\tag{5}
$$
因此原 primitive 模 $p^2$、模 $p^3$ 右核必须使用本篇较强的 $\Delta=0$，
不是 $\Delta=13$ 的较短门。

对非零约化 $\bar P$，置
$$
\widehat P=d^{C_D}\bar P\in k[t,Y],\qquad
r=\operatorname{ord}_t\widehat P.
$$
原所有角帽准确给
$$
\boxed{
\deg_t\widehat P\le
M_D:=f_D+C_D=5D+4-(D\bmod2),\qquad
\deg_Y\widehat P\le D.
}
\tag{6}
$$
确实，第 $n$ 个清分母系数的次数不超过
$3A_n+B_n+C_D-C_n+e_{n+1}=f_n+C_D$。

另外
$$
\boxed{r\ge1.}
\tag{7}
$$
在 $t=0$ 处只有 $n=0,1,2$ 的原列可非零；
(2) 的三条常数行（在原 $M$ 中位于实际乘回十三后的行）
给 $1,n,n^2$ 的单位 Vandermonde，迫这三个系数全零。
这里使用 $\ell\ge1$，没有在自由矩形中假定 (7)。

若 $r\ge H$，已经有简单必要条件
$$
\boxed{p\le6(M_D+\Delta)-1.}
\tag{8}
$$
以下处理 $r<H$，并写 $S=H-r>0$。

## 2. 局部两 jet 的加权根引理

所有代数根可先在代数闭剩余域的一个共同 tame Puiseux 扩张中读取；
赋值始终归一为 $\operatorname{ord}_t t=1$。

**引理 1。** 设 $g_0(t)\in1+t k[[t]]$，并在 $(0,1)$ 附近写
$$
f(t,Y)=U(t,Y)\prod_{j=1}^{c}(Y-\psi_j(t))^{m_j},
$$
其中 $U(0,1)\ne0$，$\psi_j$ 两两不同、$\psi_j(0)=1$，
$m_j$ 为正整数且在 $k$ 中非零。设
$$
1\le S\le s,\qquad
f(t,g_0),\ f_Y(t,g_0)\in t^Sk[[t]].
\tag{9}
$$
令
$$
h_j=\operatorname{ord}_t(\psi_j-g_0),\qquad
\bar h_j=\min(h_j,s),
\quad d_{ij}=\operatorname{ord}_t(\psi_i-\psi_j).
$$
允许 $h_j=\infty$。则
$$
\boxed{
\mathscr E:=
\sum_jm_j^2\bar h_j+
6\sum_{i<j}m_im_jd_{ij}\ \ge\ 4S.
}
\tag{10}
$$

这不是把重复因子拆成具有相同根的不同分支：
重复次数准确留在 $m_j$ 和 $m_j^2$ 中；
$d_{ij}$ 只在不同根之间取值。

**证明。** 先设 $h_{\max}\le s$，因而不需截断。
记
$$
M(x)=\sum_{h_j\ge x}m_j,\qquad
Q(x)=\sum_{h_j\ge x}m_j^2,\qquad
H_f=\sum_jm_jh_j.
$$
下面的积分只是有理分段常值函数的实数求和，不是正特征中的形式积分。
由 $d_{ij}\ge\min(h_i,h_j)$，
$$
\mathscr E\ge
\int_0^{h_{\max}}\bigl(3M(x)^2-2Q(x)\bigr)\,dx.
\tag{11}
$$

若只有一个最近根，即只有一个 $j_0$ 达到 $h_{\max}$，
对数导数的这一项
$m_{j_0}/(g_0-\psi_{j_0})$
有唯一最低赋值 $-h_{\max}$；
$m_{j_0}\ne0$ 保证它不会在正特征中消失。
$U_Y/U$ 正规，其余根的项赋值严格较高。
所以
$$
\operatorname{ord}_t f_Y(t,g_0)=H_f-h_{\max}\ge S.
$$
又 $Q\le M^2$、$M^2\ge4(M-1)$，(11) 给
$$
\mathscr E\ge4\int_0^{h_{\max}}(M-1)\,dx
=4(H_f-h_{\max})\ge4S.
$$

若至少两个不同最近根达到 $h_{\max}$，则每个
$0<x\le h_{\max}$ 的活动集合都含至少两个根。
对正整数权，有
$$
Q(x)\le(M(x)-1)^2+1.
$$
从而
$$
3M^2-2Q\ge M^2+4M-4\ge4M
\quad(M\ge2).
$$
(11) 因此至少为 $4H_f\ge4S$；
此处不需要猜测对数导数的相消程度。

现在支付 $h_{\max}\ge s$ 的截断，包括无穷阶。
若至少两个不同根有 $h_j\ge s$，
用截断后的活动集合重复上一个估计，得到
$\mathscr E\ge4\sum m_j\bar h_j\ge4s$。
若只有一个这样的根而其重数至少二，
单独的自项已给 $m_j^2s\ge4s$。

只剩唯一 $h_{j_0}\ge s$ 且 $m_{j_0}=1$ 的情况。
所有其它根的阶严格小于 $s$。
若 $h_{j_0}$ 有限，唯一最近项的同一对数导数计算给
$$
\operatorname{ord}f_Y(t,g_0)=\sum_{j\ne j_0}m_jh_j.
$$
若 $\psi_{j_0}=g_0$，则直接在乘积求导中只有对该一次因子求导的一项不为零，
仍得到同一式子。因此由 (9)，右侧至少为 $S$。
该根与所有其它根的交叉项已经给
$$
\mathscr E\ge6\sum_{j\ne j_0}m_jh_j\ge6S.
$$
全部截断情形均已覆盖，证明 (10)。证毕。

系数四不能仅凭两个局部 jet 再普遍提高：
例如一个二重根给阶 $(2h,h)$，其自项恰为 $4h$；
两个不同的对称简单根给阶 $(2h,\infty)$，其量恰为 $8h$。
这些只是局部引理的等号模型，不被声称是原 $\mathcal W_D$ 的实际核。

## 3. 原 ODE 对 charge 幂仍有同一个首共振

令 $q$ 为任意 $1\le q<p$，并暂记
$$
u_0(t)=\rho(t)^q\pmod{t^s}.
$$
对这个轴，R467 的方程仅将常数项乘 $q$：
$$
\mathscr D_q(U)=A_0(UU''-(U')^2)+B_0UU'-qC_0U^2,
$$
$$
A_0=6t(1-t)d^2,\quad
B_0=(5-8t)d^2,\quad
C_0=(154+160t+1792t^2)/3.
\tag{12}
$$
有 $\mathscr D_q(u_0)\in t^{s-1}$。

若一个 tame 单位分支 $\psi$ 精确满足 $\mathscr D_q(\psi)=0$，
对
$$
v=\psi'/\psi-8q/d
$$
取 tame 整数幂平均，仍得到正规级数并满足
$$
6t(1-t)v'+(5-8t)v=34q/3.
$$
于是
$$
v_0=34q/15,\qquad
(6n+5)v_n=(6n+2)v_{n-1}.
\tag{13}
$$
因 $p>101$、$q<p$，在 $n=s-1$ 处仍是非零首共振矛盾。
这说明后文不会因改用 $U=Y^q$ 而失去 R467 的不变因子排除。

对每个不可约
$$
F(t,U),\quad F(0,1)=0,\quad
a_F=\deg_tF,\quad1\le b_F=\deg_UF<p,
$$
其局部分裂域的 Galois 群阶整除 $b_F!$，
故全部有关分支为 tame。令 $c_F$ 为 $(0,1)$ 的完整 Hensel 因子次数，
$\Delta_F$ 为该因子的判别式赋值。
R467 的隐式微分多项式 $K_F$ 使用 (12)，仍有
$$
F\nmid K_F,\qquad
\deg_t\operatorname{Res}_U(F,K_F)
\le a_F(6b_F-1)+2b_F.
\tag{14}
$$
在每个单位根上，准确是
$K_F(t,\psi)=F_U(t,\psi)^3\mathscr D_q(\psi)$。
因此本篇保留判别式的实际值，得到
$$
\boxed{
\sum_{\psi\text{ 属于该 Hensel 因子}}
\min\{\operatorname{ord}(\psi-u_0),s\}
+3\Delta_F
\le a_F(6b_F-1)+2b_F+c_F.
}
\tag{15}
$$
R467 曾用 $\Delta_F\ge c_F-1$ 得单轴界；
这里不先作这个降低。

对不同的不可约接触因子 $F_i,F_j$，
全部对应单位根的交叉接触和满足
$$
\boxed{
I_{ij}:=\sum_{\psi\mid F_i,\ \chi\mid F_j}
\operatorname{ord}_t(\psi-\chi)
\le a_i b_j+a_j b_i.
}
\tag{16}
$$
证明是非零结果式 $\operatorname{Res}_U(F_i,F_j)$ 的次数界；
其它 Hensel 因子只贡献非负赋值。
没有删掉高阶切向交点，也没有只数几何不同点。

## 4. 任意真实重复因子的共同次数界

设非零 $F(t,U)\in k[t,U]$，并有
$$
F(t,u_0),\quad F_U(t,u_0)\in t^Hk[[t]],
\quad H\le s.
$$
令 $r=\operatorname{ord}_tF<H$。在代数闭剩余域准确分解
$$
F=t^rQ\prod_{i=1}^{m}F_i^{\mu_i},
\qquad
Q(0,1)\ne0,\quad F_i(0,1)=0,
\tag{17}
$$
其中接触因子两两不同、不可约、正 $U$ 次数。
令
$$
A_c=\sum_i\mu_i a_i,\qquad B_c=\sum_i\mu_i b_i,
\qquad c_i=\operatorname{mult}_{U=1}F_i(0,U).
$$
假设 $\deg_UF<p$，所以每个 $b_i<p$，且每个重复次数
$\mu_i$ 在 $k$ 中都是单位。

除去 $t^rQ$ 后，两 jet 仍同时消到 $S=H-r$：
第二个等式用
$$
F_U=t^rQ\left\{\partial_U\!\left(\prod_iF_i^{\mu_i}\right)
+(Q_U/Q)\prod_iF_i^{\mu_i}\right\}
$$
核定；$Q_U/Q$ 在原点正规，函数值本身已有 $S$ 阶。
故可对全部不同根统一使用引理 1。

在 (15) 乘 $\mu_i^2$，再把 (16) 乘
$6\mu_i\mu_j$。内部判别式的系数三准确等于根对的系数六。
因此引理 1 的同一个量满足
$$
\begin{aligned}
4(H-r)
&\le\sum_i\mu_i^2
 \{a_i(6b_i-1)+2b_i+c_i\}
 +6\sum_{i<j}\mu_i\mu_j(a_i b_j+a_j b_i)\\
&=\boxed{
6A_cB_c+
\sum_i\mu_i^2(-a_i+2b_i+c_i).
}
\end{aligned}
\tag{18}
$$
这保留所有实际重数及交叉因子。特别 $c_i\le b_i$ 给
$$
\sum_i\mu_i^2(2b_i+c_i)
\le3\sum_i\mu_i^2b_i\le3B_c^2.
$$
若 $\deg_tF\le A+r$、$\deg_UF\le B$，便得到
$$
\boxed{
4(H-r)\le6AB+3B^2.
}
\tag{19}
$$
$r<H$ 时必有 $B_c\ge2$，因原点的函数及其 $U$ 导数都为零，
其总局部根重数至少二。因此 $B\ge2$。

若接触部分本身无重复因子，(18) 还给较强的
$$
4(H-r)\le(6B_c-1)A_c+3B_c.
\tag{20}
$$
(18) 是优先使用的逐因子实际证书；
(19) 是不需要先识别因子的统一上界。

## 5. 原 charge 落在一个同余类时，降次仍保两 jet

设原非零 $\widehat P$ 的非零 $Y$ 次数集合至少有两个元素，
最小者为 $n_*$。
若这些次数全部同余模 $q$，其中 $q\ge1$，
则 $q\le D<p$，并且准确可写
$$
\widehat P(t,Y)=Y^{n_*}F(t,U),\qquad U=Y^q.
\tag{21}
$$
这里 $q$ 可以取所有 charge 差的最大公因数，
也可以取其任意正因子。真实次数满足
$$
\deg_tF\le M_D,\qquad
B:=\deg_UF=\frac{n_{\max}-n_*}{q}
\le\left\lfloor\frac{D-n_*}{q}\right\rfloor.
\tag{22}
$$

沿原 $Y=g(t)$，$Y^{n_*}$ 和 $U=g^q$ 都为单位。
又
$$
\mathcal E\widehat P
=Y^{n_*}\{n_*F+qUF_U\}.
$$
所以 (4) **恰给**
$$
F(t,g^q),\quad F_U(t,g^q)\in t^H.
\tag{23}
$$
没有把 $(\mathcal E-n_*)P$ 另外认作原核；
这里只使用同一个 $P$ 已有的两个为零的实际输出。

原低轴 $g^q$ 与 (12) 的 $u_0$ 模 $t^s$ 一致，
因此 (18)–(19) 可以直接应用。全部清角、次数帽由 (6)、(21)–(22) 支付，
没有加入 $U$ 的新自由列，也没有改变原 Gaussian charge。

**定理 1。** 对上述实际核，准确有下列二择：

1. $r\ge H$，从而 (8) 成立；
2. $1\le r<H$，此时 $B\ge2$，且
   $$
   \boxed{
   4(s-\Delta-r)\le6(M_D-r)B+3B^2.
   }
   \tag{24}
   $$

利用 $r\ge1$ 和 $B\ge2$，(24) 进一步给
$$
\boxed{
p\le
9M_DB+\frac92B^2-9B+5+6\Delta.
}
\tag{25}
$$
有限参数下右边可取其整数下整；优先保留更准确的 (18) 或 (24)。

若来源只含一个非零 charge，则两个长 jet 只涉及同一系数多项式乘单位。
第一长 jet 已迫其 $t$ 阶至少 $H$，因此只能落在 (8)。
同理，(22) 的 $B\le1$ 不能落入第二种情况。

本定理对整个 canonical 来源取 $q=1$ 总是可用。
对原真 $K_2^{\rm red}(M)$ 或 $K_3^{\rm red}(M)$ 的非零约化，
由 (5) 必须取 $\Delta=0$。因此它是实际提升核的必要限制，
不只是抽象环境多项式的次数估计。

## 6. 平方根预算和真实模 q 排除

首先取 $q=1$，使用 $B\le D$、$M_D=5D+O(1)$。
在 $r<H$ 的非平凡范围，(25) 给
$$
p\le\frac{99}{2}D^2+O(D).
$$
若 $r\ge H$，(8) 更强。因此任何这样的原非零首核序列都须满足
$$
\boxed{
D\ge\left(\sqrt{\frac{2}{99}}-o(1)\right)\sqrt p.
}
\tag{26}
$$
它加强 R467 只读一个长轴时的粗平方根范围，
但仍明显低于维数平衡的 $\sqrt{8/47}\sqrt p$。

若所有 charge 同余模 $q$，由 (22)、(25) 得
$$
\boxed{
p\le
\left(\frac{45}{q}+\frac{9}{2q^2}\right)D^2+O(D).
}
\tag{27}
$$
误差可对所有 $q\ge1$ 统一取 $O(D)$；
有限参数仍用 (25) 的实际 $B$，不依赖渐近式。

考虑低 $\ell$ 的真实维数临界序列
$$
2s+\ell=\dim\mathcal W_D+o(D^2),
\qquad \ell=o(D^2),\qquad
\dim\mathcal W_D=\frac{47}{24}D^2+O(D).
\tag{28}
$$
则
$$
\frac{p}{D^2}\longrightarrow\frac{47}{8}.
$$
而对所有 $q\ge8$，
$$
\frac{45}{q}+\frac{9}{2q^2}
\le\frac{45}{8}+\frac9{128}
=\frac{729}{128}
<\frac{47}{8}=\frac{752}{128}.
$$

**推论 2。** 在 (28) 的任何实际非零核序列中，充分大时，
非零原 charge 差的最大公因数不能达到八。
特别，候选不能全部位于一个模十二 canonical 块；
此时 (27) 的主系数甚至只有
$$
\frac{45}{12}+\frac{9}{288}
=\frac{121}{32}<\frac{47}{8}.
$$
该排除对原 $K_1(M)$ 使用 $\Delta=13$ 仍成立，
对真实第二、第三核则有较强的 $\Delta=0$ 精确门。

这里没有从维数平衡制造实际核，也不声称已有某个目标素数命中这种临界纤维。
推论的量词是：每个如果存在的真实非零核都必须同时满足这些限制。

## 7. 全部原提升范围和仍未解决的像

本篇没有扩充来源。全部 $q_n$、十九角和无穷帽先通过 (6) 清分母，
再在同一个原向量上读取两 jet；(21) 只利用候选本身的 charge 支持。
原 $P_{134}/U_0$、公共 charge 四十、两条十三行和第三位保持。

具体地，(25) 只是在必要约化上排除某些 $P$。
没有把真 $K_2(M)$ 的条件缩成单独 $\ker\bar J$ 的充分条件；
没有改变 R651 的同一个 $R$、完整 $Z^+$、两个十三行门和最终 $\Psi_R$；
也没有把任何新因子、幂或 Euler 输出赋予原中央零。

正特征的两个要点均由真实帽保证：

- 所有局部分裂域是 tame，因为每个接触因子的径向次数小于 $p$；
- 最近根的导数首项不消失，因为其重复次数小于 $p$。
  若允许重复次数被 $p$ 整除，局部引理的唯一最近根步骤确实会失效，
  本篇没有越过这一范围。

混合多个同余类、尤其 charge 差最大公因数为一的实际候选，
仍可能满足 (24)–(27)。它们的 regular 高尾和同一个 $R$ 的第二 forcing 仍须继续比较。
本篇不给非零原中央、跨素数有限性或主课题完成结论。

## 依赖

- [R467](R467-tame-branch-contact-and-all-factor-degree-barrier.md)：原 ODE、
  tame 整数幂共振、完整 Hensel 判别式与结果式次数。
- [R449](R449-relative-second-cokernel-and-complete-carry-exact-sequences.md)：
  原 $K_2^{\rm red}(M)\subset\ker\bar J$ 及完整 carry 分解。
- [R651](R651-original-higher-critical-branch-lift-and-complete-second-forcing.md)：
  同一原来源的完整临界基准、两 jet 像和同一修正的第三精度。
- R637：另一端的实际平方根整满射；本篇处理其下方候选的必要限制，
  两个结论均不替代原指定 forcing 的非零判定。

本篇为全参数证明，无新增目标素数扫描，也不引用未运行的证书。
