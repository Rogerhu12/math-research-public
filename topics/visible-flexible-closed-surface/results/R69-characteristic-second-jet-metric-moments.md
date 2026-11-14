# R69：闭合渐近接口的二阶障碍、共同四矩修正与真实参考条带

作者：Astra-visible-flex-78718bd0 / geometric_closure，2026-11-10。
状态：**已证明，已由未参与者全文独审；仅为中间结果。**
root 独立展开核过二阶 Gauss–Codazzi 系数及四矩条件；独审另由
independent_audit 完成，全文身份及核读回执见第 7 节。原冻结稿保持不变。

本文一方面证明：即使有符号曲率解除首个周期门，原直纹度量仍禁止
非零边界 $L_0$ 延伸到本文要求的正则性。另一方面给一个对整个参数族
固定的度量修正，解除这个二阶条件，并把该修正实现为一个真实解析
参考条带的诱导度量。**其余参数的二维等距浸入尚未构造。**

## 1. 固定几何与明确的正则性

设 $u\in\mathbb R/\ell\mathbb Z$，有解析闭嵌入曲线 $\gamma$ 及
周期正定向正交标架 $(d,T,N)$，满足

$$
\gamma'=T,\qquad d'=\alpha T-N,\qquad
T'=-\alpha d,\qquad N'=d.
\tag{1}
$$

$\alpha$ 为解析周期函数，且

$$
\int_0^\ell\alpha\,du=0,\qquad \alpha\not\equiv0.
\tag{2}
$$

显式满足这些假设的实际闭嵌入曲线及严格区间证书已完整写于
[R68](R68-signed-curvature-closed-seed.md)；其完整独审与区间独跑已完成，
本文各阶兼容和实际参考条带仍另作完整证明。

固定共同度量取测地法坐标

$$
g=dr^2+a(r,u)^2du^2,\qquad Q=aa_{rr},
\tag{3}
$$

并规定接口上的低阶数据

$$
a=1,\quad a_r=\alpha,\quad Q=1,\quad Q_r=-2\alpha
\qquad(r=0).
\tag{4}
$$

若某个延伸保持接口的位置与标架 (1)，其第二形式
$II=L\,dr^2+2M\,dr\,du+C\,du^2$ 在接口必有
$M=-1,C=0$。以下求二次径向 Gauss 导数时，明确假设 $L,M,C$ 为
$C^2$；例如 $C^4$ 浸入足够。**此假设不能擅自加到本题全部 $C^2$
候选上，以下障碍也不是所有 $C^2$ 曲面的刚性命题。**

令

$$
l(u)=L(0,u),\qquad h(u)=L_r(0,u),\qquad
Q_{rr}(0,u)=6\alpha^2-2+\Delta(u).
\tag{5}
$$

这里 $\Delta$ 属于固定的共同度量，不允许随族参数改变。

## 2. 完整二次径向兼容计算

记 $\mu=a_r/a$、$\nu=a_u/a$、$B=aa_r$。Gauss–Codazzi 为

$$
LC-M^2=-Q,\qquad M_r=L_u-\mu M,\qquad
C_r=M_u+\mu C+BL-\nu M.
\tag{6}
$$

在接口，(4) 给

$$
\mu=\alpha,\quad \mu_r=1-\alpha^2,\quad
\nu=0,\quad \nu_r=\alpha',\quad
B=\alpha,\quad B_r=\alpha^2+1.
\tag{7}
$$

因此逐项微分 (6) 得

$$
\begin{aligned}
M_r&=l'+\alpha,& C_r&=\alpha l,\\
M_{rr}&=h'+1-2\alpha^2-\alpha l',&
C_{rr}&=l''+2\alpha'+(2\alpha^2+1)l+\alpha h.
\end{aligned}
\tag{8}
$$

所有等式 (7)–(8) 均指 $r=0$。Gauss 的一次径向导数给

$$
\boxed{2l'+\alpha l^2=0.}
\tag{9}
$$

二次导数给

$$
2hC_r+lC_{rr}-2(M_r^2+M M_{rr})=-Q_{rr}.
$$

把 (8) 代入，其左边为

$$
2h'+3\alpha lh+l l''-2(l')^2-6\alpha l'
 +2\alpha'l+(2\alpha^2+1)l^2-6\alpha^2+2.
$$

由 (9)，$l'=-\alpha l^2/2$，
$l''=-\alpha'l^2/2+\alpha^2l^3/2$。故完整二阶条件是

$$
\boxed{
2h'+3\alpha lh+\alpha'l\left(2-\frac{l^2}{2}\right)
 +(5\alpha^2+1)l^2=-\Delta.}
\tag{10}
$$

这里只消掉已明确满足的首阶关系，没有丢掉 $\alpha'$ 或周期端项。

## 3. 原直纹度量的确定障碍

原直纹参考图 $F(r,u)=\gamma(u)+rd(u)$ 的诱导度量为

$$
a_0^2=(1+r\alpha)^2+r^2,
\qquad Q_0=\frac1{a_0^2}.
\tag{11}
$$

直接微分得 $(Q_0)_{rr}(0,u)=6\alpha^2-2$，故此时 $\Delta=0$。
若周期解 $l$ 非零，则由 (9) 的 ODE 唯一性，全圈 $l$ 从不为零且
保持同号。(10) 的积分因子恰为 $l^{-3}$，具体为

$$
\left(\frac h{l^3}\right)'
=-\frac{\Delta}{2l^3}-\frac{\alpha'}{l^2}
 +\frac{\alpha'}4-\frac{5\alpha^2+1}{2l}.
\tag{12}
$$

周期分部积分和 (9) 给

$$
0=\int_0^\ell\left(\frac\alpha{l^2}\right)'du
=\int_0^\ell\left(\frac{\alpha'}{l^2}
                         +\frac{\alpha^2}{l}\right)du.
$$

因而 (12) 有周期 $h$ 的充要条件为

$$
\boxed{\int_0^\ell
\left(\frac{\Delta}{l^3}+\frac{3\alpha^2+1}{l}\right)du=0.}
\tag{13}
$$

充分性也包含在积分因子公式中：右端零平均时，积分得到周期
$h/l^3$，再乘周期非零的 $l^3$ 即可。

当 $\Delta=0$，(13) 的被积函数严格同号，因此不可能。
所以对于 (11)，保持同一位置及标架的 $C^2$ 第二形式延伸只能有
$L(0,u)=0$。即使 (2) 令首 jet 存在一族非零周期解，该族也不能
原样延伸为此共同度量的 $C^4$ 浸入。

该结论不排除 $L(0,u)=0$ 而更高阶不同的延伸，不排除全部 jets 平端
的扰动，更不证明原闭曲面研究问题不可能。

## 4. 对整个参数族固定的一次度量修正

令

$$
A(u)=\frac12\int_0^u\alpha(s)\,ds,\qquad b(u)=3\alpha(u)^2+1.
\tag{14}
$$

$A$ 是解析、周期且非恒常的函数。首 jet 的整个小参数族为

$$
l_\lambda(u)=\frac{\lambda}{1+\lambda A(u)}.
\tag{15}
$$

选 $\lambda_*>0$ 使 $|\lambda A(u)|<1/2$ 对全部
$|\lambda|\le\lambda_*$ 与 $u$ 成立。对 $\lambda\ne0$，
$1/l_\lambda=z+A$，其中 $z=1/\lambda$。
所以同一个 $\Delta(u)$ 对所有这些 $\lambda$ 都满足 (13)，当且仅当
下列关于 $z$ 的三次多项式恒为零：

$$
\int_0^\ell\bigl[\Delta(z+A)^3+b(z+A)\bigr]du.
$$

展开并逐系数比较，得到恰好四个线性矩条件

$$
\boxed{
\begin{aligned}
\int\Delta&=0,&\quad \int A\Delta&=0,\\
\int A^2\Delta&=-\frac13\int b,&
\int A^3\Delta&=-\int Ab.
\end{aligned}}
\tag{16}
$$

本节及以下无端点的积分都在 $[0,\ell]$ 上。
这不是为每个 $l_\lambda$ 单独选择度量，而是一次选择同一个 $\Delta$。

定义实对称 $4\times4$ 矩阵

$$
G_{ij}=\int_0^\ell A(u)^{i+j}\,du\qquad(0\le i,j\le3).
\tag{17}
$$

它正定：若 $c^TGc=0$，连续非负函数
$\bigl(\sum_{j=0}^3c_j A(u)^j\bigr)^2$ 恒为零。
非恒常连续 $A$ 的像含非退化区间，多项式在该区间恒零迫使所有
$c_j=0$。故 $G$ 可逆。

令

$$
q=\left(0,\ 0,\ -\frac13\int b,\ -\int Ab\right)^T,
\qquad c=G^{-1}q,\qquad
\boxed{\Delta(u)=\sum_{j=0}^3c_jA(u)^j.}
\tag{18}
$$

此一个解析周期函数精确满足 (16)。未使用数值近似矩或近似零点。

对每个小参数 $\lambda$，以 $h_\lambda(0)=0$ 解 (10)。其系数和
右端解析地依赖 $(u,\lambda)$，且没有 $1/\lambda$ 的真实奇点。
当 $\lambda\ne0$，(13)–(16) 保证 $h_\lambda$ 周期；当
$\lambda=0$，方程是 $2h_0'=-\Delta$，也由 $\int\Delta=0$ 保证周期。
为明确零参数也无奇点，记 $D_\lambda=1+\lambda A$，则 (10) 除以 2
后的积分因子为 $D_\lambda^3$。令

$$
R_\lambda=-\frac{\Delta}{2}-\alpha'l_\lambda
 +\frac{\alpha'l_\lambda^3}{4}
 -\frac{(5\alpha^2+1)l_\lambda^2}{2}.
$$

满足初值的完整解为

$$
h_\lambda(u)=D_\lambda(u)^{-3}
 \int_0^uD_\lambda(s)^3R_\lambda(s)\,ds.
$$

积分中的函数恰为
$-\Delta D_\lambda^3/2-\alpha'\lambda D_\lambda^2
+\alpha'\lambda^3/4-(5\alpha^2+1)\lambda^2D_\lambda/2$，
是关于 $\lambda$ 的三次多项式，故此式直接给包含零参数的联合解析性。
端值相等及周期系数还保证所有 $u$ 导数在接口匹配。

于是共同度量 (4)–(5) 有一族满足 Gauss 两次径向兼容以及 Codazzi
一次径向兼容的周期数据 $(l_\lambda,h_\lambda)$。
该断言的准确范围到此为止，尚不是完整二维方程的解。

## 5. 该共同度量 jet 确实可由真实参考嵌入产生

不必把 (18) 仅保留为一个抽象度量 jet。令

$$
h_0(u)=-\frac12\int_0^u\Delta(s)\,ds,
\qquad
\overline F(s,u)=\gamma(u)+s d(u)+\frac{s^3}{6}h_0(u)N(u).
\tag{19}
$$

它在某个统一的 $|s|<\varepsilon$ 上给实际解析嵌入条带。
证明如下：$\overline F_s(0,u)=d$、$\overline F_u(0,u)=T$，所以
在每个边界点附近秩为二，并可选某个平面投影使其为局部图。
紧致性给统一的浸入宽度。若不存在统一嵌入宽度，可取趋向零宽度的
两列不同材料点具有同一像；极限在嵌入曲线 $\gamma$ 上必须有相同
$u$。这与该点附近的局部图单射性矛盾，故宽度还可统一保证嵌入。

其度量在 $(s,u)$ 坐标中的三个系数为

$$
\begin{aligned}
\overline E&=1+\frac{s^4h_0^2}{4},\\
\overline F_{\rm met}&=-\frac{s^3h_0}{3}
                        +\frac{s^5h_0h_0'}{12},\\
\overline G&=(1+s\alpha)^2+s^2-
              \frac{s^4h_0'}3+\frac{s^6[(h_0')^2+h_0^2]}{36}.
\end{aligned}
\tag{20}
$$

对这个实际解析诱导度量，以同一条 $s=0$ 边界及初始单位法向
$\partial_s$ 作测地法坐标 $(r,u)$。测地 ODE 的解析局部存在与参数
依赖、紧致性以及 $r=0$ 的非退化微分给统一的解析坐标变换；
初始位置和标架仍为 (1)。周期系数与测地 ODE 唯一性保证
$s(r,u+\ell)=s(r,u)$、旧角坐标 $\eta(r,u+\ell)=\eta(r,u)+\ell$，
故坐标真实下降到材料圈。在此坐标中记同一嵌入为 $F_*$。
r 是单位速测地参数；混合项的径向导数为
$\partial_r\langle\partial_r,\partial_u\rangle
=\tfrac12\partial_u|\partial_r|^2=0$，初值为零，
故度量确实为 $dr^2+a_*^2du^2$。

由 (20)，在 $s=0$，$\overline E_s=\overline E_u=
(\overline F_{\rm met})_s=0$。所以测地初值的坐标加速度为零，
$(s_r,u_r)=(1,0)$、$(s_{rr},u_{rr})=(0,0)$。
又 $\overline F_{ss}=s h_0N$，其第二形式满足
$\overline L(0,u)=0$、$\overline L_s(0,u)=h_0$。
按二次型的坐标变换公式，得到

$$
L_*(0,u)=0,\quad (L_*)_r(0,u)=h_0,
\quad M_*(0,u)=-1,\quad C_*(0,u)=0.
\tag{21}
$$

例如计算 $(L_*)_r$ 时，附加项为
$2\overline L s_{rr}+2\overline M u_{rr}$，在边界都消失。
另外 $a_*(0,u)=1$，且
$\tfrac12\partial_r|F_{*,u}|^2(0,u)=T\cdot d'=\alpha$，
故 $(a_*)_r=\alpha$。

现在对这个**实际嵌入**使用 (6)。由 (21) 得

$$
Q_*(0,u)=1,\quad (Q_*)_r(0,u)=-2\alpha,
\quad (Q_*)_{rr}(0,u)=6\alpha^2-2-2h_0'
                     =6\alpha^2-2+\Delta.
\tag{22}
$$

最后一个等式也可直接由
$(M_*)_r=\alpha$、$(M_*)_{rr}=h_0'+1-2\alpha^2$
及两次微分 $Q_*=M_*^2-L_*C_*$ 得到。
所以 (18) 修正后的整个共同度量 jet 是某个真实解析参考条带
$F_*$ 的诱导度量 jet，而且 $\lambda=0$ 的 $(l_0,h_0)$ 正是其实际数据。

## 6. 尚须解决的完整问题

(19) 只构造了 $\lambda=0$ 的一个实际参考条带；
对 $\lambda\ne0$，本文仅给该同一度量的有限阶兼容数据。
没有证明完整二维周期 Gauss–Codazzi 可解、形式级数收敛或位置/标架
monodromy 消失，不能把它当作精确等距族或 README 的 G5。

还须注意：若接口另一侧保持参考图完全固定，$C^2$ 接合要求其
$L(0,u)$ 也匹配为零。故非零 (15) 即便能够二维延伸，也不能直接
与固定参考半片接合。允许两侧共同变化的非分离接口或其它整体构造
仍需独立解决；本稿不付帽、固定开握持区、有效幅度或全闭面 reach。

后续应研究完整周期特征问题的可解结构与收敛机制，而不是把增加
有限形式阶数本身当作完成进度。


## 7. 全文独立审查、正式采纳与范围

原作者冻结稿为
[characteristic-second-jet-v1](../notes/2026-11-10-78718-geometry-characteristic-second-jet-v1.md)，
10203 B，SHA256
`91901f5ff48055831e216ed5b837ccee2526161b43f33b8489d641b2bc134b8f`。
root 已全文读取该稿（工具 `72317b`，后再读 `7c0cf9`），并独立展开
二阶系数和四矩条件；root 的参与核查不作为未参与者独审。

未参与者 independent_audit 的
[全文独立审稿](../notes/2026-11-10-78718-audit-characteristic-second-jet.md)，
16244 B，SHA256
`da053cf2f688da82510753e1be89f2746babfa85c110aceb9c4e2fd8b0d16e88`。
root 已全文核读（工具 `e91dda`）。审稿无数学订正，独立核查全部
Gauss–Codazzi 展开、周期充分性、Gram 正定性与真实参考嵌入；本正式稿
纳入了审稿已补证的无参数奇点积分因子和周期测地坐标说明。

本结果没有运行二维 ODE/PDE、数值候选优化或闭面网格，
也没有新增程序回执。R68 的既有整数区间执行只证明其输入曲线。
只有 $\lambda=0$ 给实际二维参考条带；其它参数给有限阶兼容数据，
不支付共同度量族、封帽、固定握持区、有效幅度或本题完成标准。
