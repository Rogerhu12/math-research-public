# 原连续尾低三头原始源的多项式三 Gram 观测

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；AI-assisted，GPT-6 Astra Pro。主会话提出用原始向量上的完整环境下界支付首头观测，并给出下面的单一显式测试；boundary_resume 完整核对真实源、最小链与全部旗。
状态：以下原连续尾、任意原实际头的指定源子类估计已给出完整证明。一般残量和无权 $N=M$ 未由本稿关闭。

本稿使用
[首头精确最小链](2026-11-13-high-hole-first-head-covector-and-restricted-adjoint-boundary-resume.md)、
[左源 Gram](2026-11-13-left-source-gram-and-paid-actual-dual-source-1cf.md)、
[两侧实际源](../results/R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)及
[有限头频率滤波稿](../results/R271-appendix-finite-head-frequency-filter-and-polynomial-environment-gap.md) §5 的原纯尾环境下界。
没有把一个有限等权池的首层逆搬到原高孔层。

## 1. 全部原空间及明确的源子类

固定原两模型之一，$m\ge5$、$d=2^m$，并取原合法窗口
$$
4d\le q\le e^{d^3/4}.
$$
令
$$
D=D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad
\nu_m=\|D_m\|\le m^{-1},\qquad
K_q=\ker D\cap\mathcal H_q.
$$
头保持原真实 $A=A_m$，不作 Jordan 相似。

完整允许源为
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_i
 \bigl(\ker D^{d-i-1}\cap\mathcal H_q\bigr).
$$
本稿处理它的闭子空间
$$
\boxed{
\mathscr S_q=
\operatorname{span}\{e_0,e_1,e_2\}\otimes K_q
\subset\mathscr R_q.
}
\tag{1.1}
$$
“原始”只表示各尾分量被一次 $D$ 杀掉。

对 $r\in\mathscr R_q$，沿用原左空间
$$
\mathscr V_q=P_{\le q}H\cap\ker(P_{<q}(A+D)),
\qquad E_qv=Av_q.
$$
记真正左最小费用为 $\mu(r)=\|E_q^\dagger r\|$，
真正裸状态为 $a=\mathsf f_q^{-1}r$、$\alpha(r)=\|a\|$，
完整右最小费用为 $\lambda(r)$。
左、完整右源 Gram 分别记为 $J_q,G_q$，并令
$$
r^\flat=G_qJ_q^{-1}r.
$$
即使 $r\in\mathscr S_q$，也不声称 $r^\flat$ 仍属于该子空间。

令
$$
\mathcal Q=(E_q^\dagger\mathsf f_q)^*
                E_q^\dagger\mathsf f_q,\qquad
\mathcal P=I+\mathscr L.
$$
原精确字典为
$$
\mu(r)^2=\langle\mathcal Qa,a\rangle,\qquad
\lambda(r^\flat)=\|\mathcal P^{-1/2}\mathcal Qa\|.
\tag{1.2}
$$
所有逆、最小化和范数都在原完整源空间及原联合旗上取得。

## 2. 两实际头的前三列，及真正左最小原像

两个原头的相关列准确为
$$
Ae_1=e_0,\qquad
Ae_2=\beta e_0+\eta_0e_1,\qquad
Ae_3=\gamma e_0+\beta e_1+e_2,
\tag{2.1}
$$
其中
$$
(\beta,\gamma)=
\left(\frac14,0\right)\ (N\text{ 型}),\qquad
\left(\frac14-\eta_0,\eta_0\right)\ (Y\text{ 型}).
$$
原 $\eta_0=e^{-1070}$，故可粗用
$$
|\beta|\ge\frac18,\qquad |\gamma|\le\frac18.
\tag{2.2}
$$
更高头列不会作用于 $\operatorname{span}\{e_1,e_2,e_3\}$。
但下面并不据此把完整右最小链限制在四头内。

给定 $r=r_0e_0+r_1e_1+r_2e_2\in\mathscr S_q$，
由正则三角头的唯一性，存在唯一
$$
v=e_1v_1+e_2v_2+e_3v_3,\qquad v_i\in K_q,
$$
使
$$
r=Av,\qquad
r_0=v_1+\beta v_2+\gamma v_3,\quad
r_1=\eta_0v_2+\beta v_3,\quad r_2=v_3.
\tag{2.3}
$$
把 $v$ 只放在第 $q$ 孔层。
由于 $Dv_i=0$，它满足所有低输出方程，故是源 $r$ 的合法左原像。

任何左零源 $z\in\ker E_q$ 的顶层都满足 $Az_q=0$。
原头 $\ker A=\mathbb Ce_0$，因此 $z_q$ 只有第零头；
而 $v$ 没有第零头，其他孔层也为零。
所以 $v\perp\ker E_q$，准确得到
$$
\boxed{v=E_q^\dagger r,\qquad \mu(r)=\|v\|.}
\tag{2.4}
$$
特别，没有把一个构造左链直接替代最小左链。

## 3. 一个真正完整最小的显式首头测试

置
$$
x=v_1\in K_q,\qquad h=DD^*x.
$$
写 $a_j=(j+1)^{-2}$，并明确记
$$
S_m=\sum_{j\ge m}a_j^2,\qquad
W_2=\sum_{j\ge m}a_j^2E_j^*E_j,\qquad
D_{3,m}=\sum_{j\ge m}a_j^3E_j.
$$
所用级数均按范数绝对收敛，故以下交换子可逐项计算。
原纯尾逐位关系给
$$
[D,D^*]=S_mI-2W_2,\qquad
[D,[D,D^*]]=-2D_{3,m},\qquad
[D,D_{3,m}]=0.
$$
于是 $\operatorname{ad}_D^3(D^*)=0$。
因为 $Dx=0$，完整 Leibniz 交换式给
$$
D^3D^*x=0,\qquad D^2h=0.
\tag{3.1}
$$
这里没有把 $D^2D^*x$ 误写为零；它一般等于 $-2D_{3,m}x$。

定义仅第一段非零的链
$$
k_1=e_0D^*x,\qquad k_t=0\quad(t\ge2).
\tag{3.2}
$$
由 (3.1) 及 $d\ge3$，第一段第零头所需的 $D^d$ 核旗完整满足。
在第一段 $t=1$，每个非零尾核高度 $b\ge1$ 的相对出生为 $2-b\le1$，所以这一段整个允许旗均属原低链域；$k$ 也确是低链。
其首源为 $e_0h$，而 $h\in\ker D^2\subset\ker D^{d-1}$，
所以该源也在原 $\mathscr R_q$ 内。

又因为 $D^*x\perp\ker D$，它是方程 $Du=h$ 的最小范数原像。
任意同首源链的第一段第零头均要解这个方程，
所以 (3.2) 同时是真正裸最小链和完整最小链。
$Ae_0=0$ 使内部方程全为零，故
$$
\boxed{
k\in\ker B_A,\qquad
\mathcal P k=k,\qquad
\|k\|=\|D^*x\|.
}
\tag{3.3}
$$
整条论证没有估计 $D^\dagger$ 的范数。

## 4. 非原始测试源仍给准确的顶层配对

令
$$
u=E_q^\dagger(e_0h).
$$
这个测试源 $h$ 一般并非原始；$u$ 可以有多个低孔层。
但顶层满足 $Au_q=e_0h$，由 $Ae_1=e_0$ 与
$\ker A=\mathbb Ce_0$，准确有
$$
u_q=e_1h+e_0u_{q,0}.
\tag{4.1}
$$
$v$ 只在第 $q$ 层、且第零头为零，
所以其与 $u$ 的配对恰为
$$
\langle v,u\rangle=\langle x,h\rangle=\|D^*x\|^2.
\tag{4.2}
$$
这一步不要求测试源属于 (1.1)，也不丢弃它真正左最小原像的低孔层；
只是那些层与当前 $v$ 正交。

由 $\mathsf f_q k=e_0h$，(1.2)、(3.3)、(4.2) 给
$$
\begin{aligned}
\|D^*x\|^2
&=\langle\mathcal Qa,k\rangle\\
&=\langle\mathcal P^{-1/2}\mathcal Qa,\mathcal P^{1/2}k\rangle\\
&\le\lambda(r^\flat)\|D^*x\|.
\end{aligned}
$$
零向量情形亦成立，故
$$
\boxed{\|D^*v_1\|\le\lambda(r^\flat).}
\tag{4.3}
$$
保留完整 $\mathcal P$ 的次序后才使用 $\mathcal P k=k$，
没有把完整逆压缩到低三头或原始子空间。

等价地，旧首头 Gram 字典会给
$\|P_{\ker D^d}D^*v_1\|\le\lambda(r^\flat)$；
本稿是由 (3.1) 真正证明投影在当前向量上为恒等。
它不是一个一般受限伴随下界。

## 5. 原纯尾环境下界在此可合法使用

已证的同一个原纯尾环境式为
$$
D^*D+DD^*\ge
\frac1{2^{14}(m+2)^{10}}I.
\tag{5.1}
$$
由于 $Dv_1=0$，这里的完整环境伴随正是 (4.3) 所控制的量。
所以
$$
\boxed{
\|v_1\|\le128(m+2)^5\lambda(r^\flat).
}
\tag{5.2}
$$
没有对未知 $M$、原联合旗或任意非原始向量的压缩伴随套用 (5.1)。

另一方面，任意裸链的首输出均为 $Dc_1=r$，因而
$$
\|r\|\le\nu_m\alpha(r).
$$
记 $X=\nu_m\alpha(r)$、$z=\|v_1\|$。
由 (2.2)--(2.3)，
$$
\|v_3\|\le X,\qquad
\|v_2\|\le8z+9X.
$$
在三头正交直和中，三角不等式给
$$
\mu(r)\le\sqrt{65}\,z+\sqrt{82}\,X
\le9z+10X.
$$
结合 (5.2)，得到本稿的原连续尾估计：
$$
\boxed{
\mu(r)\le
10\nu_m\alpha(r)+1152(m+2)^5\lambda(r^\flat),
\qquad r\in\mathscr S_q.
}
\tag{5.3}
$$
从而
$$
\boxed{
\mu(r)^2\le
\left(100\nu_m^2+1152^2(m+2)^{10}\right)
\left(\alpha(r)^2+\lambda(r^\flat)^2\right).
}
\tag{5.4}
$$
该常数对原合法 $q$ 一致，且没有任何 $e^{c d^4}$ 头相似费用。

## 6. 同源规范的对应结论与适用边界

若裸状态 $a$ 本身满足
$a\perp_{I+\mathcal Q}\ker B_A$，并且其源仍在
$\mathscr S_q$，则对同一个显式 $k$，
$$
\|D^*x\|^2
=\langle\mathcal Qa,k\rangle
=-\langle a,k\rangle
\le\alpha(r)\|D^*x\|.
$$
故可把 (4.3) 的右侧改为 $\alpha(r)$，
从而
$$
\mu(r)\le
\left(10\nu_m+1152(m+2)^5\right)\alpha(r).
\tag{6.1}
$$
此处明确要求规范态自身的源属于该子类。
一般同源规范投影不曾被证明保持 $\mathscr S_q$。

(5.3)--(5.4) 对该子类的任意原源成立，不要求它来自真实 $w$。
但原实际残量通常有非原始尾分量和更高头坐标；
把它正交投到 $\mathscr S_q$，也没有理由同时保持
$J_q,G_q,J_{\rm bare}$ 的三种费用。
因此不能把这个源子类估计直接求和为整个真实 $W$ 的预算。

本稿付清了一个原连续尾、任意原实际大头上的多项式观测：
首头测试可允许非原始源，当前左最小原像的顶层结构使配对变成
$\|D^*v_1\|^2$，并真正保留原长跳跃 $\beta$。
继续需要处理的是离开这类顶层原始源后的左层耦合及全部真实窄源。

### 6.1 固定前缀的旧直接界与本稿的定量增量

对本稿这个固定前三头源类，不能把“存在某个有限的观测常数”重计为新排核范围。
事实上，(2.3) 已直接给
$$
v_3=r_2,\qquad
v_2=(r_1-\beta r_2)/\eta_0,\qquad
v_1=r_0-\beta v_2-\gamma r_2.
$$
使用实际 $|\beta|\le1/4$、$|\gamma|\le1/8$，就有
$$
\mu(r)\le
\left(\frac{17}{8}+\frac{25}{16\eta_0}\right)\|r\|
\le
\left(\frac{17}{8}+\frac{25}{16\eta_0}\right)\nu_m\alpha(r).
\tag{6.2}
$$
原 $\eta_0=e^{-1070}$ 是固定数，故该直接界的头常数并不随 $m$ 增长。
一般固定前缀和固定尾核阶的旧左塔构造也必须扣除。

本稿新增的是 (3.2)–(4.3) 保持完整 $\mathcal P,G_q,J_q$ 的零返回测试：
它给出不含 $\eta_0^{-1}$ 的明确费用，并说明何时可真正去掉受限伴随的投影。
没有由此新增实际核排除区间；向变化的大前缀、非原始尾或全部真实窄源延伸仍须另证。
