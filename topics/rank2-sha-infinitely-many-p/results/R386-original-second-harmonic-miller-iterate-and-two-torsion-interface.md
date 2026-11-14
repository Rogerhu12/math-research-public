# R386：原第二 harmonic forcing、固定 Miller 二次迭代与二挠接口

日期：2026-11-14。**状态：以下固定参数方程、真实高轴的模 $p^2$ 展开、第二 forcing 的明确 dilogarithm 表达，以及实际 first-lift 两个补偿项对第三中央聚合的作用均已证明。** 它们使用同一个原 $S$、同一 $g,a_p$ 和全部低轴重组。没有将二次迭代对数独立赋予中央非零，也没有把有理有限 primitive 的全局附加项删除。

## 1. 固定参数族及原几何变量

保留
$$
p=6s-1>83,\qquad b=17,\qquad
t=-b/x^3,\qquad w=z^6,
$$
$$
h(t)=\sum_{n\ge0}{(1/2)_n\over n!(6n+1)}t^n,\qquad
G(t)=(1-t)^{-1/2},\qquad w=(-t/b)h(t)^6 .
$$
令
$$
E=z\partial_z=6w\partial_w,\qquad T=t\partial_t.
$$
由原参数恒等式，
$$
(1+6T)h=G,\qquad
E={6h\over G}T,\qquad
E\log h=1-h/G.
\tag{1}
$$

引入一个形式参数 $\eta$，定义完全固定的系数
$$
r_n(\eta)=
{1+\eta\over1+\eta+6n}
{(1/2+\eta/6)_n\over(1+\eta/6)_n},
$$
$$
R_\eta(t)=\sum_{n\ge0}r_n(\eta)t^n,\qquad
F_\eta(t)=\sum_{n\ge0}
{(1/2+\eta/6)_n\over(1+\eta/6)_n}t^n,
$$
以及
$$
\boxed{
Y_\eta={R_\eta\over h^{1+\eta}},\qquad
B_\eta=h^{-\eta}{F_\eta\over G}.
}
\tag{2}
$$
所有幂均取原点值一的形式支。
特别 $Y_\eta(0)=B_\eta(0)=1$。
这只是原固定级数的参数计算，不是增加另一条 theta 来源。

## 2. 两条一阶方程及完整二阶 forcing

**定理1。** 在 $\mathbb Q[\![t,\eta]\!]$ 中准确有
$$
\boxed{
(E+\eta)B_\eta=\eta h^{1-\eta},\qquad
(E+1+\eta)Y_\eta=(1+\eta)B_\eta.
}
\tag{3}
$$
因此
$$
\boxed{
(E+\eta)(E+1+\eta)Y_\eta
=\eta(1+\eta)h^{1-\eta}.
}
\tag{4}
$$

**证明。** 系数定义直接给
$$
(1+\eta+6T)R_\eta=(1+\eta)F_\eta.
$$
把 $R_\eta=h^{1+\eta}Y_\eta$ 代入，再用 (1)，得到 (3) 第二式。
若 $V_\eta=F_\eta/G$，相邻系数递推给
$$
6T V_\eta=\eta(G-V_\eta).
$$
于是
$$
E(h^{-\eta}V_\eta)
=\eta h^{1-\eta}-\eta h^{-\eta}V_\eta,
$$
即第一式。两个显示的 Euler 算子可交换，故得 (4)。
$\square$

写
$$
\boxed{Y_\eta=1+\eta U+\eta^2V+O(\eta^3).}
\tag{5}
$$
原点常数给 $U(0)=V(0)=0$。
展开 (4) 得到
$$
\boxed{E(E+1)U=h-1,}
\tag{6}
$$
$$
\boxed{
E(E+1)V=h(1-\log h)-1-(2E+1)U.
}
\tag{7}
$$
(6) 的 $U$ 正是 R342 已使用的固定 double-Euler forcing，
不是另选的同名函数。
(7) 则确定同一原高轴的第二 forcing。
其所有正常数项的逆分母是 $6n(6n+1)$，
在本篇 $n<2s$ 的原窗口均为 $p$ 单位。

例如固定首项为
$$
U={t\over588}+O(t^2),\qquad
V=-{13t\over24696}+O(t^2).
\tag{8}
$$
这只核定原符号，不是目标素数扫描。

## 3. 第二 forcing 的固定 Miller 二次迭代

定义
$$
\ell(t)=\log{1+\sqrt{1-t}\over2},\qquad
\mathcal F=\log h+\ell/3.
$$
令
$$
q={1-\sqrt{1-t}\over1+\sqrt{1-t}},
\qquad t={4q\over(1+q)^2}.
$$
将 $V_\eta=F_\eta/G$ 展开为
$1+\eta v_1+\eta^2v_2+\cdots$，第2节的递推给
$$
6T v_1=G-1,\qquad6T v_2=-v_1.
$$
原点零常数唯一确定
$$
v_1=-\ell/3,
\qquad
v_2={1\over18}\int_0^t{\ell(v)\over v}\,dv
={\operatorname{Li}_2(-q)+\ell^2\over18}.
\tag{9}
$$
这里
$\operatorname{Li}_2(u)=\sum_{n\ge1}u^n/n^2$；
(9) 的最后一式由
$dt/t=(1/q-2/(1+q))dq$ 逐项积分直接验证。

因此
$$
\boxed{
B_\eta
=1-\eta\mathcal F
+\eta^2\left\{\frac{\mathcal F^2}{2}
                 +\frac{\operatorname{Li}_2(-q)}{18}\right\}
+O(\eta^3).
}
\tag{10}
$$
将 (10) 代入 (3) 第二式，还得到准确的一阶版本
$$
\boxed{
(E+1)U=-\mathcal F,\qquad
(E+1)V=\frac{\mathcal F^2}{2}-\mathcal F-U
                      +\frac{\operatorname{Li}_2(-q)}{18}.
}
\tag{11}
$$
(7) 与 (11) 是同一个函数的两种表达。

这些对数具有原固定代数来源。
在 R334 的双覆盖
$$
\mathscr C:y^2=v^6+b,\qquad x=v^2,\qquad
v\sim z^{-1},\quad y\sim-z^{-3},
$$
令
$$
f=v^3-y,\qquad u={b\over f^2}.
$$
则准确有
$$
-q=u,\qquad 1-u={2v^3\over f},
\qquad
\ell=\log{f\over2v^3}=-\log(1-u),
$$
$$
\boxed{
\mathcal F=\frac13\log{z^3f\over2},\qquad
d\log f=-3v\,dz,\qquad
d\operatorname{Li}_2(u)=6v\ell\,dz .
}
\tag{12}
$$
所有对数括号在原物理支的原点为一；
$u$ 在该点为零。
所以 (11) 的新项是同一固定 Miller 单位的明确二次迭代，
完整保留原 $z^3$ frame。
它不是一个可任意更改的高轴 lift，
也没有因写作 dilogarithm 就获得一个新的算术非零输入。

## 4. 系数二次展开的所有分母

为了将形式参数实际取为 $\eta=p$，
定义
$$
D_n=1-\frac1{6n+1}
       +\frac{\mathsf H_{2n}-\mathsf H_n}{3}.
$$
相邻因子的对数展开给
$$
r_n(\eta)=h_n\{1+\eta D_n+\eta^2E_n+O(\eta^3)\},
$$
其中
$$
\boxed{
E_n=\frac12\left(
D_n^2-1+\frac1{(6n+1)^2}
-\frac{\mathsf H_{2n}^{(2)}}9
+\frac{\mathsf H_n^{(2)}}{18}
\right).
}
\tag{13}
$$
这里 $\mathsf H_n^{(2)}=\sum_{j=1}^n j^{-2}$。

对 $0\le n<2s$，(13) 和 $r_n(\eta)$ 的展开分母全为 $p$ 单位。
特别 $2n<p$，而 $6n+1$ 尚未遇到原首次可整除的位置 $5p$；
$(1+\eta/6)_n$ 在 $\eta=p$ 也由单位构成。
因此取 $\eta=p$ 后，截到二次的误差逐系数在 $p^3\mathcal O$，
并非只是一条形式特征零展开。

等价地，
$$
\boxed{
Y_p=1+pU+p^2V\pmod{p^3,t^{2s}}.
}
\tag{14}
$$
(13) 是 (7)、(11) 的有限有理系数版本，
可直接计算所需下一位，不需对目标素数作扫描。

## 5. 原高轴的完整第二精度

沿 R334 置
$$
\alpha_p=p\ell_s\in\mathcal O^\times,\qquad
d_p=\ell_s-\kappa(-1/b)^s\in\mathcal O,
$$
$$
Q_s(t)=\log(1+8t)+\sum_{1\le j<s}\ell_jt^j .
$$
原系数具有准确恒等式
$$
{\ell_{s+n}\over\ell_s}=r_n(p).
$$
故 (14) 给
$$
\boxed{
\log g(w)-Q_s(t(w))
=(-b)^s w^s\{d_p+\alpha_pU(w)+p\alpha_pV(w)\}
\pmod{p^2,w^{3s}}.
}
\tag{15}
$$

**证明。** 在 $t$ 坐标，左边为
$$
t^s\{\ell_sR_p(t)-\kappa(-1/b)^s h(t)^{p+1}\}.
$$
使用 $R_p=h^{p+1}Y_p$、$\ell_s=\alpha_p/p$ 和
$\kappa(-1/b)^s=\alpha_p/p-d_p$，
得到
$$
t^s h^{p+1}\{d_p+\alpha_pU+p\alpha_pV\}\pmod{p^2,t^{3s}}.
$$
最后用 $6s=p+1$ 及原精确参数式
$t^sh^{p+1}=(-b)^s w^s$，即得 (15)。
所有窗转换都是整单位变换。
$\square$

再沿 R338 记
$$
H=w^{-s}\{\log g-[\log g]_{<s}\},\qquad
\mathscr S F=w^{-s}(F-[F]_{<s}).
$$
则完整物理式为
$$
\boxed{
H=\mathscr S Q_s(t(w))
+(-b)^s\{d_p+\alpha_pU+p\alpha_pV\}
\pmod{p^2,w^{2s}}.
}
\tag{16}
$$
原低 $t$ 轴向高 $w$ 轴的重组仍在第一项中。
实际常数 $d_p$ 也仍保留；
若使用 R342 的合法同时重标使它为零，
必须同步改变整个 Gaussian 和完整插值函数。

(16) 可直接代入 R382 的第三中央式。
第二中央权需要 $H\bmod p^2$，
第三权只需 $\bar H$ 和同一个 $\bar H^2$。
所以新 $V$ 的系数、原一次 forcing 和其二次项都已明确，
不能用单独的 $V$ 值替代整个聚合。

## 6. 原 first-lift 两个补偿项的确切作用

以下在原剩余函数域中取
$$
DZ=1,\qquad D^p=0,\qquad
a=x^2/y,\qquad e=3Za,
$$
并定义已付有限 primitive
$$
I_Z(F)=\sum_{i=0}^{p-2}
 {(-1)^iZ^{i+1}D^iF\over(i+1)!}.
$$
令
$$
Z_1=I_Z(e),\qquad
f_1=Z_1/Z,\qquad
\boxed{J_c=Z^{-1}I_Z(f_1).}
\tag{17}
$$
这些都是原函数域中的真实有理函数。
$\mathcal C$ 或 finite primitive 的附加项不能全局删掉。

准确有
$$
DZ_1=e+Z^{p-1}D^{p-1}e,\qquad
D(ZJ_c)=f_1+Z^{p-1}D^{p-1}f_1.
$$
因为 $D^{p-1}f_1$ 是 $p$ 次幂，
算子 $(ZD+1)$ 作用于后一附加项时准确给因子 $p=0$。
因此得到一个完整全局式：
$$
\boxed{
(ZD+1)^2J_c=e+Z^{p-1}D^{p-1}e .
}
\tag{18}
$$
这说明第二次 primitive 的附加项已经相消，
而第一次的附加项仍确实存在。

在原点，$e$ 正规、型为零，$e(0)=-3$。
$D^{p-1}e$ 是正规 $p$ 次幂、型为二，
其首个可能项从 $z^{4p}$ 起。
所以 (18) 的附加项至少从 $z^{5p-1}$ 起。
配合原 $Z\equiv z\bmod(p,z^{5p})$，在所有本篇短窗准确有
$$
\boxed{
(E+1)^2J_c=3z\,x^2/y=-3h(t)G(t),\qquad J_c(0)=-3.
}
\tag{19}
$$
这里的等式表示所需普通系数窗；它没有取代完整的 (18)。

在一个真正非原点 $Z=0$ 测试点，
$e$ 至少一阶零，$Z_1$ 至少二阶零，
$f_1$ 至少一阶零，$J_c$ 至少一阶零。
这些固定零阶会保留到下面的 first-lift 补偿中。

## 7. Jc 是原固定二挠 Miller 对数的 double-Euler 行

置
$$
L_y=\log(-z^3y)
=3\log h+\frac12\log(1-t).
$$
原点括号为一，故这是准确正规的固定对数。
由 $Dy=3x^2$，
$$
E L_y=3+3z\,x^2/y.
$$
于是 (19) 等价于
$$
\boxed{
J_c=-3+E(E+1)^{-2}L_y
}
\tag{20}
$$
于原短窗。
右端在正常数项上的逆分母是 $(6n+1)^2$，
所用 $n<s$ 时全部为 $p$ 单位。

这正是 R371 中固定 $d\log(Z^3y)$ 的原点形式接口；
它仍含 $z^3$ frame。
真实 $S$ 在二挠点的零，不允许直接删除有限有理 theta 模型在那里具有的
$p^2$ 极或其 weighted exact 项。

对原首中央系数配对，常数部分给
$$
[w^s]J_c\widehat S=-3c_1+
[w^s]\{E(E+1)^{-2}L_y\}\widehat S .
\tag{21}
$$
因此只有在原首失败 $c_1\equiv0\bmod p$ 后，才可在这个模 $p$ 配对中去掉
显示的 $-3c_1$；其他部分没有被消去。

## 8. 唯一共振常数在首失败后的消去

R385 的强普通窗比较所用 first-lift 补偿为
$$
p\{c_pZ^{p-1}Z_1+\beta Z^p\}.
\tag{22}
$$
本节只需 (22) 这个明确输入。
下面的作用公式也对任意两个相差 (22) 的实际有理连接代表成立，
不以尚未证明的中央条件来决定 $\beta$。

R377 的 $F_1$ 因而增加
$Z^p(c_pf_1+\beta)$。
由于 $D(Z^p)=0$，有限 primitive 逐项给
$$
\boxed{
\delta H_1
=I_Z\{Z^p(c_pf_1+\beta)\}
=Z^{p+1}(c_pJ_c+\beta).
}
\tag{23}
$$
没有新的积分常数。
为保持与 R380 的同一个 $A_0$，本节明确选相容的特征零 lift：
令
$
\widetilde J_c=\widetilde Z^{-1}
 \widetilde I(\widetilde Z_1/\widetilde Z),\qquad
\delta\widetilde H_1=
\widetilde Z^{p+1}(\widetilde c_p\widetilde J_c+\widetilde\beta).
$
它在原点精确从 $w^s$ 起，且在所有真实测试点为零。
在 $x=0$，$\widetilde J_c$ 至少有三阶零；在二挠点，其极阶至多
$2p^2-p-3$，故 $\delta\widetilde H_1$ 的极阶至多 $3p^2-3$，
没有超过 R377 原 $H_1$ 的界。
这些界直接来自 $e$ 极阶 $p+1$、
$\widetilde Z_1$ 极阶至多 $p^2+p-1$，以及两次显示的有限 primitive。
因此这是原构造所允许的一个实际 lift。
如果任取其他 lift，低窗可能另改一个 $p^2$ 项，必须同步重新计算 $A_0$；
本节不将那种变化忽略。

对本节相容代表，低于 $w^s$ 的 $g$ 准确不变，故 $A_0$ 也准确不变。
原 theta 指数中是 $34pH_1$，故在所需短窗
$$
\boxed{
{g_{\rm new}^{[2]}\over g_{\rm old}^{[2]}}
=1+34p\,w^s(c_pJ_c+\beta)\pmod{p^2,w^{2s+1}} .
}
\tag{24}
$$
严格地，给 $c_2\bmod p^2$ 使用 (24) 至 $w^{2s-1}$ 已足够；
在端点保留的更高项只乘原 $S(0)=0$。
$Z^{p+1}\equiv w^s$ 的短窗比较来自原 $Z$ 的强普通窗口，
没有在全局把两个函数相等。

若 $\widehat S_{\rm new}^{[2]}$、
$\widehat S_{\rm old}^{[2]}$ 使用相同的原角因子，
则 (24) 给
$$
\delta c_1=0,\qquad
\delta c_2\equiv34p[w^s](c_pJ_c+\beta)
                         \widehat S_{\rm old}^{[2]}\pmod{p^2},
\qquad
\delta c_3\equiv0\pmod p .
\tag{25}
$$
于是 R382 的第三中央聚合变化准确为
$$
\boxed{\begin{aligned}
\delta(a_p^2c_1-pa_pc_2+2p^2c_3)
\equiv -34p^2a_p\big\{
&c_p[w^s]J_c\widehat S_{\rm old}^{[2]}\\
&+\beta\,\bar c_1
\big\}\pmod{p^3}.
\end{aligned}}
\tag{26}
$$
[R385](R385-original-zero-resonance-and-strong-whole-theta-second-lift.md)
已进一步证明当前原规范的唯一共振恰为 $\beta=0$。
上面的含 $\beta$ 公式仍保留了整规范检查：即使只先保留这个确定常数，
在已知原首失败 $\bar c_1=0$ 时，它的贡献也确实消失。
但 $c_pJ_c$ 的非恒定项仍完整存在，不能一并删去。

另一方面，(24) 在原除幂目标中的变化是 $p^2\epsilon$ 乘整低轴。
R380 证明这种变化在原 $K_1$ 上属于 $p^3$，
所以它不改变整个原 $d_2$。
这两种结论使用同一个模型，准确说明了为何
$\beta$ 不阻碍指定二阶核，却仍需在一般中央系数中先保留。

结合 R385 的强普通模 $p^2$ 比较，
R382 旧模型中的高修正还可准确识别为
$$
\boxed{
\eta\,\bar B_1=34(c_pJ_c+\beta)
\pmod{w^s},\qquad \eta=(t/w)^s ,
}
\tag{27}
$$
当前原数据 $\beta=0$，所以旧修正准确是 $34c_pJ_c$，
而升级后的 $B_1$ 模 $p$ 为零。
(27) 的整窗比较使用的是 R385；
(23)–(26) 已独立给出该补偿的全部有限作用与符号。

## 9. 当前同一原配对

(16) 以固定 $U,V$ 给高轴的全部下一精度；
(23)–(27) 则把同一个实际 first-lift 补偿放回
R377/R380/R382 的确定矩阵。
原第一失败杀掉的只是 (26) 的显示常数项。
剩余必须比较的是
$$
[w^s]J_c\widehat S_{\rm old}^{[2]}
$$
与同 $P_2,\lambda_2$ 的真正 $C_2$ 配对。
(20)、(21) 给出了该指定行的固定二挠来源，
没有将整个对数、它的局部单位值或一条 Cartier 常数单独称为中央非零。

所有物理 Gaussian、charge $n+40$、
$P_{134}/U_0$、十三行及真实 double-Euler 交换差仍按
R380/R382 保留。
全局残数仍先聚合原测试点与固定二／三挠边界，
再除以核条件支付的 $p^2$。
这里没有把有限原点窗的相等扩大成各个非原点残数分别为零。

## 依赖与同步

R334、R338、R342 的原高轴与固定 Miller 单位；
R356、R363、R371、R377 的实际 finite primitive、全局 defect 与 first-lift；
R380、R382 的原 $K_3/d_2$、完整第三中央聚合；
R385 的强普通窗及唯一共振用于 (22)、(27) 的原代表识别。

本篇为全参数证明，没有目标素数扫描。
通过已授权 GitHub API 保存；核心登记与 HANDOFF 由根代理维护。
