# R1020 — 原全部长窗的单 primitive 返回与第二 Cartier 层的准确低窗消去

日期：2026-11-27 UTC。**已证明。** 本篇保持 R1016/R1018 的同一个
完整 target、原 $P_{10}$、$Z$、全部字权和质量。原第二 Cartier 层
在整个低窗内只贡献一个明确 scalar，而且该 scalar 只可能出现在
$b\equiv5\pmod6$。用一个显示的平坦 Cartier 截面，还可将这一项
完整吸收入同一个第一 primitive 类。

两种选择的全部极帽、原点留数、原 affine $aZ$ 和二者之间的
准确差均在下文支付。原二挠对数和第三 Cartier 的全纯项没有被
赋零；它们可以继续显式保留，也可以按同一恒等式编码进该
primitive。没有把消去第二层的低窗读取等同于消去第一层。

## 1. 同一全22 target、完整原点留数和实际极帽

沿 R1018，固定
$$
p=6s-1>13^4,\qquad
H=6\left\lfloor\frac{s-5}{6}\right\rfloor+5,\qquad
N=H(p+1),\qquad e=7N/6+1.
\tag{1}
$$
故 $H\equiv5\pmod6$、$H\le s<p$。
对 R1016 的同一个特征零来源 $h_{N,\pi}(f)$ 取其实际约化
$A=A_{N,\pi}(f)\bmod p$，其中 $f$ 可为原整个
$\mathcal V_{130,\mathcal O}$，也可为 R1018 的实际 $U_\pi$、
$U_{\bar\pi}$ 等完整 principal 来源。

对全部 $0\le b<p$ 定义
$$
\eta_b=Z^{-b-1}P_{10}A\,\omega_E,\qquad DZ=1.
\tag{2}
$$
下面始终使用同一个 target 坐标，不将 $Z$ 换成一个自由形式参数。
原 $P_{10}=-Z^p(D-10G)^{p-1}Z^9$ 保证其它 $Z=0$ 点无遗漏补极。

R1016 的全部帽是
$$
\operatorname{pole}_O\eta_b\le b+1\le p,\qquad
\operatorname{pole}_{\mathcal D_2}\eta_b\le
d_b=p^3-p^2+(8-b)p+4e+1<p^3,
\tag{3}
$$
其中 $\mathcal D_2=E[2]\setminus O$，此外没有极。
其原点留数准确为
$$
\boxed{\rho_b=\operatorname{Res}_O\eta_b
=\pi^{-b}c_b(f).}
\tag{4}
$$
这是完整低 jet 身份；不能因 $f$ 的质量为零就将所有 $\rho_b$
删除。原 principal 型只给 $c_b(f)=0$，除非 $6\mid b$。

令
$$
r_0=x^2/y,\qquad
\ell_O(\eta_b)=-\rho_b r_0\omega_E,\qquad
\eta_b^0=\eta_b-\ell_O(\eta_b).
\tag{5}
$$
$r_0\omega_E$ 在 $O$ 留数为 $-1$，且
$\mathcal C(r_0\omega_E)=r_0\omega_E$。
所以 (5) 只去掉真实的原点留数；没有去掉或预设二挠上的其它留数。

记
$$
\nu_1=\mathcal C\eta_b^0,\qquad
\nu_2=\mathcal C\nu_1=\mathcal C^2\eta_b^0.
\tag{6}
$$
因 (3) 的原点极不超过 $p$，第一次 Cartier 只能保留其留数；
该留数已在 (5) 消去。故 $\nu_1,\nu_2$ 在 $O$ 都正则，
只在原三个二挠点有极。它们不必是 Cartier 零微分。

形式帽取
$$
d_1=p^2-p+9-b+\left\lfloor\frac{4e}{p}\right\rfloor,\qquad
d_2=\left\lfloor\frac{d_1-1}{p}\right\rfloor+1.
\tag{7}
$$
奇偶不符时可取不超过它的实际同奇偶帽；本文的统一上界不依赖
这个额外节省。由 $H\le s$，
$4e\le7(p+1)^2/9+4$，所以
$$
\boxed{d_1<p^2,\qquad d_2\le p.}
\tag{8}
$$
(7) 是从 (3) 两次使用
$\operatorname{pole}\mathcal C\nu\le
\lfloor(\operatorname{pole}\nu-1)/p\rfloor+1$ 得到，
没有把形式帽少算一阶。

## 2. 一个对所有有理微分都适用的明确 Cartier 截面

保持原 Hasse 常数
$$
c_p=\binom{3s-1}{2s-1}\in\mathbf F_p^\times.
$$
R1013 的实际微分
$$
\boxed{\varphi=-\frac{3x}{c_p(X+1)}\omega_E,\qquad
\mathcal C\varphi=\omega_E}
\tag{9}
$$
只在 $\mathcal D_2$ 有二阶极，在 $O$ 从四阶起。
等式来自原
$D^{p-1}x=-c_p$ 和
$(4x(2z)-x(z))/3=-3x/(X+1)$；
这里始终是同一个微分尺度。

对任一有理微分 $\nu=u\omega_E$，定义
$$
\boxed{\mathfrak S_0(\nu)=u^p\varphi.}
\tag{10}
$$
Cartier 的 $p$ 次幂线性直接给
$$
\mathcal C\mathfrak S_0(\nu)=\nu.
\tag{11}
$$
(10) 不要求 $\nu$ 的留数为零，也不需要先删除其全纯项。
这正是本篇能保留全部二挠对数和 holomorphic 数据的原因。

由 (6)、(11)，整个微分
$$
\nu_1-\mathfrak S_0(\nu_2)
$$
被 Cartier 杀掉。因而存在唯一的 primitive 类
$$
\boxed{
[K_{0,b}]
=D^{-1}\{\nu_1-\mathfrak S_0(\nu_2)\}
\in F/F^p,\qquad F=k(E).
}
\tag{12}
$$
这里的唯一性是函数域上的准确代数事实：
用原 $p$ 基 $F=\bigoplus_{j=0}^{p-1}F^pZ^j$，
Cartier 零使 $Z^{p-1}$ 坐标为零，其余坐标逐项除以
$j+1$ 积分；$\ker D=F^p$。未引入可以另外选择的 primitive 数据。

由 (7)–(10)，
$$
\operatorname{pole}_{\mathcal D_2}
(\nu_1-\mathfrak S_0\nu_2)
\le L_0:=\max\{d_1,pd_2+2\}\le p^2+2.
\tag{13}
$$
可以取 $K_{0,b}$ 在 $O$ 正则、原二挠之外无极，写为
$$
K_{0,b}=V_{0,b}+a_{0,b}Z,\qquad
\operatorname{pole}_{\mathcal D_2}V_{0,b}\le L_0-1,
\qquad V_{0,b}(O)=0.
\tag{14}
$$
这保留原 affine 项，不能把 $aZ$ 冒称为全局正则函数。

为支付 (14) 的全局条件，在每个二挠点按原局部原函数
$du=\omega_E$ 逐项积分非 $p$ 倍负幂主部。
所得主部 $V_T$ 满足
$$
\operatorname{Res}_T(V_T\omega_E)
=-\operatorname{Res}_T\bigl(Z(\nu_1-\mathfrak S_0\nu_2)\bigr).
$$
右侧在全部点的和为零，且 $O$ 正则。
这恰是 genus1 的函数 Mittag-Leffler 障碍。
拼成 $V$ 后的全纯差为 $a\omega_E=d(aZ)$，证明 (14)。
原 $Z$ 在二挠的 $p$ 阶极已包含于上述统一帽。
若取原几何角色投影，$a_{0,b}$ 仅可能在 $b\equiv1\pmod6$ 出现。

## 3. 整个第二层在低窗只读一个实际 scalar

写
$$
\nu_2=f_{2,b}\omega_E,\qquad
c_b^\sharp=f_{2,b}(O),\qquad
\varphi=a(Z)\omega_E,\quad
a(Z)=\sum_{n\ge0}a_nZ^n.
\tag{15}
$$
$f_{2,b}$ 在 $O$ 正则，故
$$
\boxed{
\mathfrak S_0\nu_2
=(c_b^\sharp)^p\varphi+O(Z^{p+4})\omega_E.
}
\tag{16}
$$
因此所有 $Z^n$、$n<p$ 的读者都不需要第二层的其它局部系数。

原 $\mu_6$ 作用下，$\eta_b$ 的角色是 $\varepsilon^{-b}$，
两次 Cartier 后仍为 $\varepsilon^{-b}$。
所以 $f_{2,b}$ 的角色是 $\varepsilon^{-b-1}$，从而
$$
\boxed{c_b^\sharp=0\quad\hbox{除非 }b\equiv5\pmod6.}
\tag{17}
$$
这是实际字符零，不是把 $\nu_2$ 整条设为零。
在允许的角色中，该 scalar 仍是原数据的确定值，例如
$$
c_b^\sharp=
\left([Z^{p^2-1}](\eta_b^0/\omega_E)\right)^{1/p^2}.
\tag{18}
$$
本篇不将它宣称为低阶 Taylor 系数、常数单位或额外 canonical 零。

对于 $n=rp+b$、$1\le r\le H$，原有限模型读者
$t_n^{10}(A)=[Z^n](P_{10}A)$ 精确为
$$
\boxed{
t_{rp+b}^{10}(A)=
\left(
-\rho_b^{1/p}[Z^{r-1}]r_0
+r[Z^r]K_{0,b}
+(c_b^\sharp)^p a_{r-1}
\right)^p.
}
\tag{19}
$$
$r=0$ 时准确为 $t_b^{10}(A)=\rho_b$。
(19) 对所有 $b<p$ 成立，特别包括 R1018 的末四个非 diagonal
余数；这里没有再使用仅适用于 $b\le H$ 的六块估计。
$(c_b^\sharp)^p a_{r-1}$ 只可能同时有
$b\equiv r\equiv5\pmod6$。

代表 $K_{0,b}$ 的 $0<r<p$ 系数无 $F^p$ 歧义：
两个在 $O$ 正则的代表之差为正则 $p$ 次函数，
其正次数只可能是 $p$ 的倍数。
因此 (19) 中不是任选一个 primitive 的系数。

## 4. 一个明确平坦截面把该 scalar 也移入同一 primitive

(9) 的原角色是 $\varepsilon^5$，故
$$
a_n=0\quad\hbox{除非 }n\equiv4\pmod6.
$$
定义完全显示的有限多项式
$$
\boxed{
J_H(Z)=\sum_{0\le n<H}\frac{a_n}{n+1}Z^{n+1},
\qquad
\varphi_H=\varphi-dJ_H.
}
\tag{20}
$$
所有 $n+1\le H<p$ 均为单位；
$a_n$ 是原 $Z$ 下 (9) 的真实系数。
没有将原参数改成形式变量后另拟一个截面。

因为 Cartier 杀掉全导数，有
$$
\boxed{\mathcal C\varphi_H=\omega_E,\qquad
\operatorname{ord}_O(\varphi_H/\omega_E)\ge H+5.}
\tag{21}
$$
后一加强使用 $H\equiv5\pmod6$：
被截去的最后可能次数是 $H-1$，下一次是 $H+5$。
$\varphi_H$ 仍保持原角色 $\varepsilon^5$。

令
$$
\mathfrak S_H(u\omega_E)=u^p\varphi_H.
$$
则 $\mathcal C\mathfrak S_H=1$，并且
$$
\boxed{
[K_{H,b}]
=D^{-1}\{\nu_1-\mathfrak S_H\nu_2\}
=[K_{0,b}+f_{2,b}^{\,p}J_H]\quad\hbox{in }F/F^p.
}
\tag{22}
$$
这是两种实际选择的整个函数域差，不只是一条低 jet 同余。
其低窗差准确为
$$
\boxed{
[Z^r](K_{H,b}-K_{0,b})
=(c_b^\sharp)^p[Z^r]J_H
\qquad(0<r\le H).
}
\tag{23}
$$
所以没有通过更换截面丢掉 (19) 的第五角色 scalar；
它被 (22)–(23) 完整转入同一个 primitive。

### 4.1 新极帽准确支付

原 $Z$ 在每个二挠点的极阶为 $p$。
由于 $DZ=1$，不是使用粗略的“微分增加一阶”，而是准确有
$$
dJ_H=\sum_{n<H}a_n Z^n\omega_E.
$$
因此
$$
\operatorname{pole}_{\mathcal D_2}\varphi_H
\le p(H-1).
\tag{24}
$$
$H\ge5$，故该帽已包含 (9) 的二阶极。
于是
$$
\operatorname{pole}_{\mathcal D_2}
(\nu_1-\mathfrak S_H\nu_2)
\le L_H:=\max\{d_1,p(d_2+H-1)\}.
\tag{25}
$$
使用 (7) 的形式 $d_2=\lceil d_1/p\rceil$ 可取
$L_H=p(d_2+H-1)\le p(p+H-1)$。

按与 (14) 相同的全局 primitive 证明，可以取
$$
\boxed{
K_{H,b}=V_{H,b}+a_{H,b}Z,\qquad
\operatorname{pole}_{\mathcal D_2}V_{H,b}\le L_H-1,
\qquad V_{H,b}(O)=0.
}
\tag{26}
$$
(22) 的直接代表可能另含较大的 $p$ 倍主部；
(26) 是同一 $F/F^p$ 类中已付的有界代表，
不能把直接代表的较大极无证删去。

若写原角色的有理部分为
$x^u y^\epsilon P(X)/(X+1)^M$，$\epsilon=b\bmod2$，
则 (14)、(26) 分别给
$$
M_0\le\left\lfloor\frac{L_0-1+\epsilon}{2}\right\rfloor,\qquad
M_H\le\left\lfloor\frac{L_H-1+\epsilon}{2}\right\rfloor.
\tag{27}
$$
这里仅是逐点极／分母帽，不将它当成新增深核的维数。
$aZ$ 按 (14)、(26) 单独保留。

## 5. 全部 b、全部非 diagonal 的单 primitive 读者

由 (21) 及 $f_{2,b}$ 在 $O$ 正则，
$\mathfrak S_H\nu_2$ 在 $O$ 从至少 $H+5$ 阶起。
所以整个 $0\le r\le H$ 长窗口准确变成
$$
\boxed{
t_{rp+b}^{10}(A)=
\left(
-\rho_b^{1/p}[Z^{r-1}]r_0+r[Z^r]K_{H,b}
\right)^p
\quad(1\le r\le H,\ 0\le b<p).
}
\tag{28}
$$
$r=0$ 仍是 (4) 的原留数。
这保全部质量、原点低系数和非 diagonal；
没有把原第一层 primitive 的正系数也设为零。

R1013 的 $\pi^{rp+b}$、全部 sigma／$P$ 下三角矩阵、
两个 Gaussian 和原高精度低项仍按原式回代。
R1018 的 (3) 仍来自特征零的同一个 $V_{N,\pi}$。
本篇 (19)、(28) 只替换其真实模 $p$ 读者，
不将模 $p$ 单 primitive 公式冒称为一个新的全 $p^{H+1}$ 同构。

### 5.1 四阶的准确低窗兼容范围

在同一个返回点，任一至多四次的一阶连接
$D+u_j$，若每个 $u_j$ 至多有简单极，就使阶数至多下降四。
由 (21)，其作用于
$\mathfrak S_H\nu_2=f_{2,b}^p\varphi_H$ 后仍从
$H+1$ 阶起，故不进入 (28) 的窗口。
这里 $D(f_{2,b}^p)=0$，也没有漏掉其导数。

R1018 的标准 $R_{i,b}$ 在原返回点的
$G$、$D\log h$、$D\log h_i$、$1/Z$ 都至多是简单极，
所以这个局部估计可按真实位移共轭使用。
它不交换 Cartier 与 $D$，也不允许在一个未搬动返回点的
Miller 权中直接删除 (21)。
正确次序仍是先形成 R1018 的完整 first-Cartier 等式，
再对同一个目标应用下节的投影。

## 6. 对完整 first-Cartier 身份的统一线性操作

对有理微分定义
$$
\mathfrak E_H=1-\mathfrak S_H\mathcal C.
$$
它是剩余域上的线性幂等算子，准确有
$$
\boxed{
\mathcal C\mathfrak E_H=0,\qquad
\mathfrak E_H^2=\mathfrak E_H.
}
\tag{29}
$$
线性来自 $\mathcal C$ 的 $p^{-1}$ 次线性与
$\mathfrak S_H$ 的 $p$ 次线性相消。

原点留数投影
$\mathfrak R(\nu)=\nu+\operatorname{Res}_O(\nu)r_0\omega_E$
与 Cartier 交换，按同一半线性规则解释系数。
因此本篇唯一的原 primitive 读者可写成
$$
\boxed{
\mathfrak M_H(\eta)
=D^{-1}\mathfrak E_H\,\mathcal C\,\mathfrak R(\eta)
\in F/F^p.
}
\tag{30}
$$
这正是 (22) 的 $[K_{H,b}]$。
它对 $\eta$ 为 $p^{-1}$ 次线性，不是逐字新选的 primitive。

于是对 R1018 已完整证明的任一 first-Cartier 等式，
包括全部 $\chi_8$、$b_\ell$ 卷积、$13\pi^{-10}$ 的半线性尺度、
四项 concomitant 和末四个 $b$ 的二阶极补项，
先在原式中做完所有运算，再统一作用
$\mathfrak E_H\mathfrak R$，随后取 $D^{-1}$，
就得到同一 $F/F^p$ 中的真实线性身份。
右边原点留数必须按同一个 $\mathfrak R$ 处理；
不能只对某个 summand 丢掉质量或改用另一返回点。

(30) 也直接保持 R1018 的整个来源恒等式：
所有来源的常数系数经过这一步取真实 $p$ 次根，
最后 (28) 的 $p$ 次方再返回原线性系数。
不把 (30) 移过 $\nabla$、torsion translation、
非恒定乘子或原 mixed cut。

## 7. 原二挠对数和第三 Cartier 全纯项在哪里

若仍按 R1013 先保留完整小边界，写
$$
\eta_b^\circ=\eta_b-\ell_b-\alpha_b^{p^3}\chi,
$$
其中 $\ell_b$ 包含全部真实二挠留数，
$\mathcal C^3\chi=\omega_E$，则
$$
B_b=\ell_b-\ell_O(\eta_b)+\alpha_b^{p^3}\chi
$$
在 $O$ 留数为零，且
$\eta_b^0=\eta_b^\circ+B_b$。
本篇与原两 exact 写法的关系准确为
$$
\boxed{
\mathfrak M_H(\eta_b)
=\mathfrak M_H(\eta_b^\circ)
+D^{-1}\{\mathcal C B_b
-\mathfrak S_H\mathcal C^2B_b\}
\quad\hbox{in }F/F^p.
}
\tag{31}
$$
花括号被 Cartier 杀掉，故它是实际全局 primitive 类；
不是省略一个可能非零的边界。

因此可以选择保留原 $\beta_1,\beta_2$ 的负号和 $\alpha_b$
作为显式来源，再按 (31) 回代；也可以直接对完整 $\eta_b$ 用
(30)。两者严格相同。
本篇绝未声称这些原小边界、$c_b^\sharp$、
$a_{0,b}$ 或 $a_{H,b}$ 为零。

## 8. 同一 old 非零目标继续落在真实第一 primitive

R1018 的两 canonical 同时坏条件仍只给原
$j_{\Phi_*}=j_{\Phi_{260}}=0$。
R1016/R1018 的同一全精度 trace 比较和实际 old 对数非零没有改变，
特别
$$
\omega^2j_{10,h_{N,\pi}(U_\pi)}
-\omega j_{10,h_{N,\bar\pi}(U_{\bar\pi})}
\equiv-\frac{61}{18480}(p+1)\log_p(\pi/\bar\pi)
\not\equiv0\pmod{p^{H+1}}.
$$
本篇将其中原有限读者准确改写为 (28)，并付了所有需保的
原点留数及 (31) 的边界位置。
该非零值必须由这些真实项承担；
不能把 primitive 的存在、唯一类或第二层的低窗消去
解释成第一 primitive 也消失。

接 R1021 的实际 odd3 来源时，应先完成其原三处 Miller／连接
转置并形成完整 target，再对同一个目标应用 (30)。
若其真实支撑增加，须相应支付 primitive 主部，
不能套用本篇仅原 $\mathcal D_2$ 的极帽。
本篇没有从任何 $O_3$、连接或纯来源方向传播 canonical 零。

## 9. 证明和范围

所有步骤是显示有理身份、原完整 Cartier 与 $p$ 基运算，
没有新数学执行或素数扫描。
固定坏处已包含于 $p\le13^4$；
新分母只有 $c_p$ 和 $1,\ldots,H$，均已证明为单位。

准确依赖：
R887 的原 $Z/G$ 与 $p$ 基；
R1013 的完整留数、$r_0,\varphi$、角色及全局 primitive 障碍；
R1016 的同一全22 target 与完整极帽；
R1018 的线性深度和实际全字第四阶等式。
本篇没有重新定义这些对象或放宽任何中央非零完成标准。
