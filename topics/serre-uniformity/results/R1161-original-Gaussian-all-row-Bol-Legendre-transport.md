# R1161：原 Gaussian 全实际标签的 Bol–Legendre 运输

日期：2026-11-28（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；root / o2_high_coefficient。

**已证明，纯纸面。** 本篇把
[R1116 §9](R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)
的每一条原 actual-good Gaussian profile，准确运输到
[R1154](R1154-original-Gaussian-first-profile-and-joint-finite-Gauss-moments.md)
中同一个固定次数的 Legendre 对 $P_\nu,V_\nu$。
Bol 模块性、固定权的整 $q$ 展开、Wilson 阶乘、
原热流时间、Hasse 符号和实际 source 单位均保留。
所得公式不除以 Bernoulli 数，不添加缺席角色，也不将不同的
原 coarse components 合并。

这个结论区别于只对权 $6,8,10$ 作一次反射：
那三个特例最终回到 R1135 已登记的 Wronskian。
这里支付的是全部实际行与同一固定 $P_\nu,V_\nu$ 的完整对应，
包括每条行的真实 Eisenstein 多项式权重。
尚未证明所得全部实际行能分离两个不同的 coarse 参数。

## 1. 原标记、角色范围与有限热流

设 $p\equiv3\bmod4$、$p\ge41$，原 Gaussian 曲线为
$$
E_{\rm G}:y^2=x^3+a_{\rm G}x,\qquad a_{\rm G}\in\mathbf F_p^\times .
$$
保持 R1116 的原 $\delta\in\mathbf F_p^\times$、
torsion-root $\beta_0$、source 参数 $\lambda_{\rm src}$、
以及 good 角色的圆单位规范 $b_{\omega^R}$。
为避免与后面的 Legendre 变量 $w$ 混淆，把原 gauge 写成
$$
\eta=\delta\lambda_{\rm src}\beta_0^{\,1-p}t_*,
\qquad
\eta'=\delta\lambda_{\rm src}\beta_0^{\,1-p}t_*',
$$
$$
N_R=
\frac{(\beta_0^{p+1})^R\delta^{R-1}}
     {2b_{\omega^R}R!}.
\tag{1161.1}
$$
不假设 $\beta_0,\lambda_{\rm src}\in\mathbf F_p$，
也不把 $(\beta_0^{p+1})^R$ 改成一。
只有在原角色为 good 时才使用这个 $b_{\omega^R}^{-1}$。

每个实际偶角色 $R$ 对应唯一的整数 $s$：
$$
s=
\begin{cases}
R,&R<(p-1)/2,\\
p-R,&R>(p+1)/2,
\end{cases}
\qquad
v=p+1-2s,\qquad 2\le s\le(p-3)/2 .
\tag{1161.2}
$$
等价地，$s$ 偶时 $R=s$，$s$ 奇时 $R=p-s$。
这里 $4\le v,2s\le p-3$。
中间角色 $R=(p+1)/2$ 的真实缺席已由 R1070/R1116 支付；
本篇不把它作为一个新观测补回。

原 Ramanujan 场为
$$
\Theta=(4wa+6b)\partial_a
 +(6wb-4a^2/3)\partial_b+(w^2+a/3)\partial_w .
$$
仅在这一行中 $w$ 表示通用 gauge。
令 $(a_0(u),b_0(u),w_0(u))$ 是从 $(a_{\rm G},0,0)$ 出发的
模 $u^p$ Taylor 解。它只用 $1!,\ldots,(p-1)!$，
不是一个被假定存在的无限 characteristic-$p$ 加法群流。
记
$$
\mathcal G_j(u)=G_j(a_0(u),b_0(u)).
$$
R1116 (1116.48) 的原完整差为
$$
\boxed{
\begin{aligned}
\Pi_R(t_*^2)-\Pi_R(t_*'^2)
={}&-\frac{N_R}{(v)_s}
 \sum_{\substack{2\le i\le s\\ i\ {\rm even}}}
 (-1)^i\binom{s+i-1}{i}
 (\eta^i-\eta'^i)[u^{s-i}]\mathcal G_v(u).
\end{aligned}}
\tag{1161.3}
$$
其最高原输入权为 $p-3$。下面从这条已付原身份出发，
不先对一个共纤维点对作横向微分。

## 2. 整 Eisenstein 多项式与固定权的展开原则

用标准变量 $H=E_2,E=E_4,F=E_6$，并令
$$
g_j=-\frac{B_j}{2j}+\sum_{n\ge1}\sigma_{j-1}(n)q^n,
\qquad G_j=\frac{2g_j}{(j-1)!}.
\tag{1161.4}
$$
右边 $G_j$ 在原模型中的解释是
$E=-48a,F=864b$，与 R1154 (1154.7) 的规范相同。

对偶数 $4\le j\le p-3$，$g_j$ 是
$\mathbf Z_{(p)}[E,F]$ 中的真正权 $j$ 模形式。
这里不要求 $B_j$ 为单位：
von Staudt–Clausen 的分母判据只需 $p-1\nmid j$，
就给 $B_j\in\mathbf Z_{(p)}$，而 $2j$ 也是单位。
全部正次 Fourier 系数本来是整数。

说明本篇所用的整展开原则。
沿用
[R992 §1、§4](R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md)
的 full-level 整权环与实际 Serre 导子，
置 $\Delta=(E^3-F^2)/1728$。
在任意固定偶权 $W$，取
$$
\Delta^h E^{a_h}F^{b_h},\qquad
4a_h+6b_h=W-12h,\quad b_h\in\{0,1\},
\tag{1161.5}
$$
其中只取 $a_h\ge0$ 的可行指标。
这些元素构成该固定权的基；
把 $F^2=E^3-1728\Delta$ 反复代入就得到这一基变换。
各基元素的 Fourier 首项恰为 $q^h$，系数一，
而不同基元素的 $h$ 不同。
所以若一个有理模形式的 Fourier 系数全部 $p$ 整，
从最小 $h$ 逐项消去，得到它在此基中的系数全部 $p$ 整。
同样，约化后一个固定权元素的 $q$ 展开若为零，
其最小非零基系数也必须为零，矛盾。
因此固定权的模 $p$ 展开原则在本篇全部权上成立。

这没有把混合权环的 $q$ 展开误当成单射：
Hasse 多项式 $A$ 的展开为一，确会给混合权关系。
本篇只比较已核相同整数权的两个模形式。

写
$$
\mathfrak d=-\frac F3\partial_E-\frac{E^2}{2}\partial_F,
\qquad A=E_{p-1}\bmod p,\quad B=E_{p+1}\bmod p .
$$
实际规范为
$$
\mathfrak dA=B/12,\qquad
\mathfrak dB=-EA/12,\qquad A(q)=1,\quad B(q)=H(q).
\tag{1161.6}
$$
这些恒等式的同权 Fourier 证明已在 R992 (992.18)、
R1135 及 R1154 §17 给出。

## 3. 全部安全权的 Bol 身份

在标准变量中，原 $\Theta$ 正是
$$
\Theta=
\frac{H^2-E}{12}\partial_H
+\frac{HE-F}{3}\partial_E
+\frac{HF-E^2}{2}\partial_F .
$$
若 $\mathcal Z=2H\partial_H+4E\partial_E+6F\partial_F$，
则
$$
[\partial_H,\Theta]=\mathcal Z/12,\qquad
[\mathcal Z,\Theta]=2\Theta .
$$
对不含 $H$、权为 $j$ 的模形式 $M$，归纳交换给
$$
\partial_H(\Theta^nM)
=\frac{n(j+n-1)}{12}\Theta^{n-1}M.
\tag{1161.7}
$$

现在取偶数 $4\le j\le p-3$，令 $m=p+1-j$。
$m$ 也在同一安全范围内。
(1161.7) 的系数为 $mp/12=0$。
此外 $\Theta^m g_j$ 的整数权为
$$
j+2m=2p+2-j\le2p-2.
$$
因 $H$ 权二，其 $H$ 次数严格小于 $p$。
所以 $\partial_H(\Theta^m g_j)=0$ 确实迫它不含 $H$；
这里不会留下一个未经排除的 $H^p$ 项。
它因而是一个真实模形式，而不只是 quasimodular 展开。

逐个 Fourier 系数有
$$
n^m\sigma_{j-1}(n)=n\sigma_{m-1}(n)\pmod p.
$$
当 $p\mid n$，两边都为零；
否则在因子和中作 $d\mapsto n/d$ 并用
$m=p+1-j$ 即得。
另一方面，
$A\mathfrak d g_m+(m/12)Bg_m$ 的展开准确为
$q\,dg_m/dq$，包括零常数项。
两者权都是 $p+1+m$，于是 §2 的固定权展开原则证明
$$
\boxed{\qquad
\Theta^{\,m}g_j
=A\,\mathfrak d g_m+\frac m{12}B\,g_m,
\qquad m=p+1-j.
\qquad}
\tag{1161.8}
$$
全过程没有除以 $B_j,B_m$ 或任何 Eisenstein 常数项。

## 4. 同一 Gaussian 流上的 Wilson 反射

沿 §1 的原有限流，令
$$
C=B/12-wA .
$$
R1116 (1116.49) 给 $\Theta A=C,\Theta C=0$。
在原 Gaussian 点，
$$
A(0)=0,\qquad C(0)=-\delta,
$$
故在模 $u^p$ 的实际有限流中
$$
A=-\delta u,\qquad C=-\delta .
\tag{1161.9}
$$
对于权 $m$ 的模形式，
$\mathfrak d g_m=\Theta g_m-mwg_m$。
因此 (1161.8) 沿流的右边为
$-\delta(u\,d/du+m)g_m$。

当 $0\le h\le j-2$，有 $m+h\le p-1$。
读取 $u^h$、再用 (1161.4)，得到
$$
\boxed{\qquad
[u^{m+h}]\mathcal G_j(u)
=-\delta\,(-1)^h
 \frac{h!(j-h-1)!}{((j-1)!)^2}
 [u^h]\mathcal G_m(u).
\qquad}
\tag{1161.10}
$$
为核全部阶乘，读取前的系数是
$$
-\delta\,\frac{h!(m-1)!}
 {(j-1)!(m+h-1)!}.
$$
Wilson 给
$(m-1)!=1/(j-1)!$、
$(m+h-1)!=(-1)^h/(j-h-1)!$，
正是显示公式。
所有阶乘的指标都严格小于 $p$。

对 (1161.3)，取 $j=2s,m=v,h=s-i$。
同时
$$
(v)_s=(-1)^s\frac{(2s-1)!}{(s-1)!}.
$$
将 (1161.10) 倒代入 (1161.3)，每项的系数准确化为
$$
N_R\,\frac{(2s-1)!}{\delta\,i!(s-i)!}.
$$
于是原完整行差成为
$$
\boxed{
\begin{aligned}
\Pi_R(t_*^2)-\Pi_R(t_*'^2)
={}&N_R\frac{(2s-1)!}{\delta\,s!}
 [u^{p+1-s}]
 \bigl\{(1+\eta u)^s-(1+\eta'u)^s\bigr\}
 \mathcal G_{2s}(u).
\end{aligned}}
\tag{1161.11}
$$
奇数 $i$ 项由原 Gaussian parity 自动为零，$i=0$ 项在差中抵消。
最高实际读取为 $p-s-1<p$，最低不小于 $v\ge4$。
这既没有触及原 Kronecker 的未付 principal 行，
也没有借 Bol 身份取消 actual-good mask。

## 5. 同一个固定 Legendre 对及全部时间尺度

令
$$
\nu=\lfloor p/6\rfloor,\qquad
P=P_\nu(w),\quad a_\nu=P_\nu'(0),\quad
V=\mathsf W_{\nu-1}-P\mathcal L_p,\quad f=a_\nu V .
$$
$\nu$ 是奇数，
$a_\nu=(-1)^{(\nu-1)/2}(3/2)_{(\nu-1)/2}/((\nu-1)/2)!$
为单位。以下都在
$\mathcal A=\mathbf F_p[w]/(w^p)$ 中计算。
R1154 §§15、17 的实际坐标与标准流为
$$
\xi=\frac{P}{a_\nu f},\qquad
\mathscr R(H)=[w^{p-1}]\frac{H}{1-w^2}
            =[\xi^{p-1}]Hf^2,
$$
$$
\mathcal E_4=f^4,\quad
\mathcal E_6=-wf^6,\quad
A(\mathcal E_4,\mathcal E_6)=-a_\nu\xi,\quad
B(1,0)=-6a_\nu.
\tag{1161.12}
$$
这不是另选一个齐次 companion；$V$ 的首 $p$ 强制项仍由原式保留。

暂取 $\vartheta$ 满足
$\vartheta^4=-48a_{\rm G}$。
标准三变量场 $X=2\Theta$ 的初值为 $(0,1,0)$。
齐次性与有限 Taylor 唯一性准确给
$$
\boxed{
\begin{gathered}
\xi=\vartheta^2u/2,\\
-48a_0(u)=\vartheta^4\mathcal E_4(\xi),\qquad
864b_0(u)=\vartheta^6\mathcal E_6(\xi),\\
12w_0(u)=\vartheta^2\mathcal E_2(\xi),\\
\delta=\frac{a_\nu\vartheta^{p+1}}2 .
\end{gathered}}
\tag{1161.13}
$$
最后一式来自原 $B/12=-\delta$ 和标准
$B(1,0)=-6a_\nu$。
由于 $4\mid p+1$，$\vartheta^{p+1}$ 属于 $\mathbf F_p$，
而且不依赖四次根的选择。

定义每个真正的低权 Eisenstein 多项式
$$
Q_s(w)=G_{2s}\!\left(-\frac1{48},-\frac w{864}\right),
\qquad
\kappa=\frac{2}{a_\nu^2\vartheta^2},
\qquad
\kappa^2=-\frac1{12a_\nu^4a_{\rm G}}.
\tag{1161.14}
$$
其次数至多 $\lfloor s/3\rfloor$，奇偶性与 $s$ 相同。
这里的 $Q_s$ 不是 Legendre 第二解。
同权性给
$\mathcal G_{2s}(u)=\vartheta^{2s}f^{2s}Q_s(w)$。

设 $L=p+1-s$。
由 $\xi=\vartheta^2u/2$，左侧换系数的因子是
$\vartheta^{2p+2}2^{s-2}$。
再用 (1161.12) 及 $\xi=P/(a_\nu f)$，有
$$
\begin{aligned}
&[\xi^{p+1-s}]
 (1+2\eta\xi/\vartheta^2)^s f^{2s}Q_s\\
&\qquad
=\mathscr R\!\left[
 \xi^{s-2}f^{2s-2}
 (1+2\eta\xi/\vartheta^2)^sQ_s
 \right]\\
&\qquad
=a_\nu^2\,
 \mathscr R\!\left[P^{s-2}Q_s(V+\kappa\eta P)^s\right].
\end{aligned}
$$
因为 $\delta^2=a_\nu^2\vartheta^{2p+2}/4$，
最终完整的取系数身份是
$$
\boxed{\quad
[u^{p+1-s}](1+\eta u)^s\mathcal G_{2s}(u)
=2^s\delta^2\,
 \mathscr R\!\left[P^{s-2}Q_s(w)(V+\kappa\eta P)^s\right].
\quad}
\tag{1161.15}
$$
每个乘积只在 $\mathcal A$ 中读取：
次数至少 $p$ 的项先按同一个有限代数约去，
不把完整多项式在 $w=1$ 的值代替这个截断读数。

## 6. 全部原实际行的统一加权 moment

合并 (1161.11)、(1161.15)，得到主要公式
$$
\boxed{
\begin{aligned}
\Pi_R(t_*^2)-\Pi_R(t_*'^2)
={}&N_R\,\frac{2^s\delta(2s-1)!}{s!}\,
 \mathscr R\!\left[
 P^{s-2}Q_s(w)
 \bigl\{(V+\kappa\eta P)^s-(V+\kappa\eta'P)^s\bigr\}
 \right].
\end{aligned}}
\tag{1161.16}
$$
$N_R$ 与所有显示的外部阶乘、$\delta$ 都是该 good 行的单位。
两个槽仍来自同一个原 $P,V$；
不同 $s$ 只改变明确的权重 $P^{s-2}Q_s$ 与幂次数。

四次根的消去是逐项的。
$P^{s-2}Q_s$ 是偶函数，$V$ 偶、$P$ 奇；
所以括号中的奇数 $i$ 对 $\mathscr R$ 的贡献为零。
把 $Z=\eta^2$，定义一个完全在原系数域中的多项式
$$
\boxed{
\mathcal T_s(Z)=
\sum_{h=1}^{\lfloor s/2\rfloor}
 \binom{s}{2h}(\kappa^2 Z)^h\,
 \mathscr R\!\left[P^{s+2h-2}Q_s(w)V^{s-2h}\right].
}
\tag{1161.17}
$$
于是 (1161.16) 的最后一个读数就是
$\mathcal T_s(\eta^2)-\mathcal T_s(\eta'^2)$。
$\vartheta\mapsto i\vartheta$ 只将 $\kappa$ 改为 $-\kappa$，
而 $\kappa^2$ 已在 (1161.14) 明确下降；
因此没有遗留一个任意第四根或新的标记选择。

令 $\mathcal S_{\rm good}$ 是 (1161.2) 从原
$\mathcal G_p$ 得到的实际指标集。
在同一个已经固定的原 coarse component 内，
两个原点具有相同全部 good 标签，准确等价于
$$
\boxed{\qquad
\mathcal T_s(\eta^2)=\mathcal T_s(\eta'^2)
\quad\hbox{对全部 }s\in\mathcal S_{\rm good}.
\qquad}
\tag{1161.18}
$$
两条 Gaussian twist 的统一仍消费 R1135 §10 的完整标记运输；
本式没有只留下单一 fine line 的平方像，
也没有将另外的 Weil/coarse components 合并。

## 7. 原低行的尺度校验与保留的真正缺口

原规范给
$$
Q_2=\frac1{720},\qquad Q_3=\frac w{30240}.
$$
$P^2$ 为次数小于 $p$ 的偶多项式，且 $P(1)^2=1$，
所以
$$
\mathcal T_2(Z)=\frac{\kappa^2}{720}Z .
$$
这只在原 $R=2$ 实际出现且为 good 时提供 affine 单位行；
它没有把 R1127 的 Bernoulli 出现条件删除。

对 $s=3$，R1154 的原记号满足
$\mathscr R(wP^3V)=a_\nu^2\mathsf h$。
(1161.16) 因而给
$$
\Pi_{p-3}(t_*^2)-\Pi_{p-3}(t_*'^2)
=N_{p-3}\frac{\delta\kappa^2a_\nu^2}{63}\,
  \mathsf h\,(\eta^2-\eta'^2).
\tag{1161.19}
$$
核对这正是旧 $N_{p-3}\mathcal H_p/4$ 的斜率。
写
$$
r=-\frac43a_{\rm G},\qquad
\varepsilon_r=r^{(p-1)/2},\qquad \beta_{\rm G}=-\delta .
$$
由于 $(-48a_{\rm G})/r=36$ 是平方，(1161.13) 给
$$
\boxed{\qquad
\delta\beta_{\rm G}
=12\varepsilon_r a_\nu^2a_{\rm G}.
\qquad}
\tag{1161.20}
$$
代 (1161.14) 后，
$\delta\kappa^2a_\nu^2/63=-\varepsilon_r/(63\beta_{\rm G})$，
正好配 R1154 (1154.33)
$\mathcal H_p=-4\varepsilon_r\mathsf h/(63\beta_{\rm G})$。
特别 $a_{\rm G}=-1/48$ 时，
$r=1/36$、$\varepsilon_r=1$，准确有
$\beta_{\rm G}=-a_\nu/2$。
所以这里没有丢失 $\Theta$ 与 $2\Theta$ 之间的二，
也没有把固定判别式参数的 $\beta_{\rm G}$ 误当 torsion-root。

(1161.17) 给全部实际行一个固定的有限源；
其系数是指定的
$\mathscr R(P^{s+2h-2}Q_sV^{s-2h})$。
不能用未加权 moment、单个端点或另一个 horizontal 权空间替换它们。
同样，(1161.18) 没有推出这组真实指标在某个 Jacobi/Serre 算子下封闭。
原 Bernoulli mask、$S=0,P=0$ 的点对边界、
missing-principal 的完整低卷积和首 $p$ carry 都继续存在。

后继目标是对这同一个实际子集证明
$\eta^2\ne\eta'^2$ 时至少一个 (1161.17) 的差非零，
或证明一个能分离该点对的操作真实保留这些原行。
本篇没有宣称这一目标已完成；全部推导为纸面证明，无数学程序执行。


## 8. 同一 Legendre 导子的完整 Cartier 规范

本节将 §6 的实际 weighted moment 送入一个确定的 Cartier 投影。
仍用 $q=1-w^2$、$D=q\,d/dw$、$P=\mathsf P_\nu$、
$a=a_\nu$，并置
$$
\delta_P=P^2D,\qquad \alpha=\frac{dw}{qP^2}.
$$
以下 $\alpha'$ 表示相对 Frobenius 目标上的同一微分，
不是对 $\alpha$ 求导。所有 pullback 都只作用于显示的
**函数系数**；不把微分的 Frobenius pullback 当作非零微分。

### 8.1. 原有理微分给出的精确 restricted power

原 Legendre 第二多项式 $W=\mathsf W_{\nu-1}$ 满足
$$
q(PW'-WP')=P^2-1.
$$
这个有理多项式恒等式可由同一 Legendre 方程和
$P'(0)=a,\ W(0)=a^{-1}$ 定准；也由 R1154 的原
$P,W$ 递推直接得到。因此
$$
\boxed{\qquad
\alpha=\frac{dw}{q}-d\!\left(\frac WP\right),
\qquad
C_{\rm rel}(\alpha)=\frac{dw'}{q'}.
\qquad}
\tag{1161.21}
$$
第二式使用 exact 微分的 Cartier 为零，以及
$C_{\rm rel}(dw/(1-w^2))=dw'/(1-w'^2)$。
在 $w=\pm1$，$\alpha$ 的留数仍分别为 $-1/2,1/2$，
没有将这两个实际极点删除。

为同时核准导子公式，给一个一般的函数域证明。
设 $\delta=v(w)\,d/dw$、$\alpha_\delta=dw/v$，
且 $\delta^p=c\delta$。
交换 $\delta$ 与 $\delta^p$ 得 $\delta c=0$。
在相对常数域上，$\delta$ 的像维数为 $p-1$。
两个算子
$$
\delta^{p-1}-c,\qquad
v^p\left(\frac d{dw}\right)^{p-1}\circ v^{-1}
$$
都杀掉这个像，且最高阶系数同为 $v^{p-1}$；
所以它们相等。
再用 $(p-1)!=-1$ 的标准 Cartier 取系数式，得到
$$
\boxed{\qquad
F_{\rm rel}^*\!
 \left(\frac{C_{\rm rel}(h\alpha_\delta)}
                  {\alpha_\delta'}\right)
   =ch-\delta^{p-1}h .
\qquad}
\tag{1161.22}
$$
这里只对右边的相对 Frobenius 常数作系数下降，
不要求底域的任意参数有 literal $p$ 次根。

将 $h=1$ 与 (1161.21) 代入 (1161.22)，准确得到
$$
\boxed{\qquad
\delta_P^{\,p}=P^{2p}\delta_P,\qquad
F_{\rm rel}^*\!
 \left(\frac{C_{\rm rel}(h\alpha)}{\alpha'}\right)
 =P^{2p}h-\delta_P^{\,p-1}h .
\qquad}
\tag{1161.23}
$$
这将 R1154 §16 中仅需非零的 restricted-power 系数
完全定为 $P^{2p}$。它不是说 $\delta_P$ 对原 actual-good
行空间已经给出了一个闭合的操作。

### 8.2. 每个真实 Eisenstein 权重的 Cartier 身份

在权为 $k$ 的模形式上，记原 Katz 导子为
$$
\mathscr T M=A\mathfrak d M+\frac{k}{12}BM .
$$
它的权为 $k+p+1$，其 $q$ 展开是 $q\,dM/dq$。
将 $M$ 限制到 $E_4=1,E_6=-w$，写为 $Q(w)$。
Euler 同权式以及
$A=-P,\ B=-6DP+wP$ 给
$$
\mathfrak dM\big|_{(1,-w)}
 =\frac12DQ+\frac{k}{12}wQ,\qquad
\mathscr TM\big|_{(1,-w)}
 =-\frac12\bigl(PDQ+k(DP)Q\bigr).
$$
于是对原 $Q_s$，逐次保留变化后的权
$2s+n(p+1)\equiv2s+n\bmod p$，得到
$$
\boxed{\qquad
\delta_P^n(P^{2s}Q_s)
 =(-2)^nP^{2s+n}
       \bigl(\mathscr T^nG_{2s}\bigr)\big|_{(1,-w)} .
\qquad}
\tag{1161.24}
$$
没有在每次作用后继续误用初始权 $2s$。

原 Eisenstein 系数满足
$\sigma_{2s-1}(pm)\equiv\sigma_{2s-1}(m)\bmod p$。
因此 $\mathscr T^{p-1}G_{2s}$ 的展开恰是
$G_{2s}(q)-G_{2s}(q^p)$，包括零常数项。
以下两项和左边的整数权都为 $p^2-1+2s$，
所以 §2 的固定权展开原则给
$$
\mathscr T^{p-1}G_{2s}
 =A^{p+1}G_{2s}
   -A^{p+1-2s}G_{2s}^{\,p}.
$$
实际范围 $2\le s\le(p-3)/2$ 保证
$p+1-2s\ge4$；两次 $A$ 的幂均为偶数。
合并 (1161.23)、(1161.24)，得完整有理微分身份
$$
\boxed{\qquad
C_{\rm rel}\!\left(
 P^{2s-2}Q_s(w)\frac{dw}{q}\right)
       =Q_s(w')\frac{dw'}{q'}.
\qquad}
\tag{1161.25}
$$
具体地，若 $h=P^{2s}Q_s$，则
$$
\delta_P^{p-1}h=P^{2p}(h-Q_s^p),
$$
所以 (1161.23) 的右边正是
$P^{2p}Q_s^p$，没有另一个常数或 holomorphic 补项。

在 $w=0$ 读取 (1161.25) 给
$$
\mathscr R(P^{2s-2}Q_s)=Q_s(0).
\tag{1161.26}
$$
例如实际偶 $s$ 的最高 coarse 系数准确为
$\kappa^sQ_s(0)$。这只是原系数的值，
并未证明每个 $Q_s(0)$ 都是单位。
对于奇 $s$，(1161.26) 的两边由奇偶性均为零，
不能把它替换成原带 $V$ 的最高奇行读数。

## 9. 每条原行的单一 Cartier 读取及安全误差界

为书写全局有理式，暂取原有限对象的指定多项式代表
$$
V=W-P\mathcal L_p,\qquad
\mathcal L_p=\sum_{j=0}^{(p-3)/2}\frac{w^{2j+1}}{2j+1}.
$$
不在中途把它换成 characteristic-zero 的无限对数。
定义
$$
Y_\eta=V+\kappa\eta P,\qquad
Z_\eta=\frac{Y_\eta}{P},\qquad
\mathcal M_s(\eta)=
 \mathscr R(P^{s-2}Q_sY_\eta^s).
$$
原行差 (1161.16) 正是同一单位因子乘
$\mathcal M_s(\eta)-\mathcal M_s(\eta')$。
由 (1161.21) 及
$\mathcal L_p'=(1-w^{p-1})/q$，有精确的有理函数式
$$
\boxed{\qquad
\delta_P Z_\eta=-1+P^2w^{p-1}.
\qquad}
\tag{1161.27}
$$
显示的最后一项没有在函数域中消失。

### 9.1. 原 weighted moment 的 $2p$ 次系数

令
$$
h_s=P^{2s}Q_sZ_\eta^s=P^sQ_sY_\eta^s.
$$
则 $h_s\alpha=P^{s-2}Q_sY_\eta^s\,dw/q$，
所以其相对 Cartier 在 $w'=0$ 的常数系数就是
$\mathcal M_s(\eta)$。
由于 $\operatorname{ord}_0h_s\ge s\ge2$，
(1161.23) 中 $P^{2p}h_s$ 不贡献 $w^{2p}$。
另一方面，$P=aw+O(w^3)$；
在 $C_{\rm rel}(h_s\alpha)/\alpha'$ 中
$w'^2$ 的系数准确为 $a^2\mathcal M_s(\eta)$。
因此
$$
\boxed{\qquad
\mathcal M_s(\eta)
 =-\frac1{a^2}[w^{2p}]
       \delta_P^{p-1}(P^{2s}Q_sZ_\eta^s).
\qquad}
\tag{1161.28}
$$
这可以在把 $\eta$ 看作独立底参数的相对 Cartier 中证明；
不对 $\eta$ 擅自取 Frobenius 逆。
原标记中的 $\kappa$、$N_R$ 仍由 §§5–6 保留。

### 9.2. 仅在这一指定读取中排除首个有限对数误差

把 $Z$ 先看作独立变量，在
$\mathbf F_p((w))[Z]$ 上赋予
$\operatorname{ord}w=1,\operatorname{ord}Z=-1$。
设
$$
\mathcal D_0=\delta_P-\partial_Z,\qquad
\mathcal E=P^2w^{p-1}\partial_Z .
$$
代入 $Z=Z_\eta$ 后，真正的 $\delta_P$ 作用是
$\mathcal D_0+\mathcal E$。
$\mathcal D_0$ 将赋值提高至少一，
$\mathcal E$ 将赋值提高至少 $p+2$。
而输入 $P^{2s}Q_sZ^s$ 的赋值至少为 $s$。
在 $p-1$ 次作用的展开中，只要一个词含 $\mathcal E$，
其最终赋值至少为
$$
s+(p+2)+(p-2)=2p+s>2p.
$$
这也包括 $\delta_P$ 随后微分误差系数的情形；
不需要假设两个误差算子可交换。

只有 $\delta_P$ 与 $\partial_Z$ 在 $\mathcal D_0$ 内可交换。
用
$\binom{p-1}{j}(-1)^j=1$，得到真实读取
$$
\boxed{
\begin{aligned}
\mathcal M_s(\eta)
 =-\frac1{a^2}[w^{2p}]
 \sum_{j=0}^{s}
   s(s-1)\cdots(s-j+1)\,
   \delta_P^{p-1-j}(P^{2s}Q_s)\,
   Z_\eta^{\,s-j}.
\end{aligned}}
\tag{1161.29}
$$
$j=0$ 的下降阶乘为一。
所有阶乘指标均小于 $p$；
本式不除 Bernoulli 数，也不添加任何缺席行。

(1161.29) 是 (1161.28) 的准确有限计算规则，
不是把 (1161.27) 的误差从所有恒等式中删掉。
若改变 $V$ 的代表一个 $w^p$ 倍数，
(1161.28) 的被微分输入变化的赋值至少为 $p+s$，
作用后至少为 $2p+s-1>2p$；
所以结果仍是原 $\mathbf F_p[w]/(w^p)$ 中的同一读数。
这里出现的 $2p$ 次系数来自已定义的有理 Legendre 函数，
不是延伸一个尚未证明整性的原 $\sigma$ 或 torsion logarithm jet。

### 9.3. 原多项式余项的低 jet 不含未知 Frobenius 修正

同一精确导子还给 R1154 §16 的四个实际多项式逆
一个无需解未知 Frobenius 常数的读取。
对 $r=1,2,3$，若该节的实际有界解满足
$\mathcal S_rH=T$，定义
$$
\mathcal I_r(T)=
 P^{r-2p}\delta_P^{p-r-2}(P^{r+2}T).
$$
由 (1154.92)，
$P^{r+2}T=\delta_P^{r+1}(H/P^r)$ 在 $\delta_P$ 的像中。
(1161.23) 因而证明
$\mathcal S_r\mathcal I_r(T)=T$，所以
$$
H-\mathcal I_r(T)=P^r u(w)^p
\quad\text{对某个 }u(w)\in\mathbf F_p(w).
$$
这里没有将 $u$ 任意设为零。

在 $P$ 的每个简单根处，
$\delta_P^{p-r-2}(P^{r+2}T)$ 的零阶至少为 $p$。
故 $\mathcal I_r$ 的极阶至多 $p-r$，
从而 $u$ 的极阶至多一。
在原 Gaussian 点 $w=0$，写
$u=c/w+u_{\rm reg}$。
因 $r\nu<p$，$w^{-p}P^r$ 的全部项均为负次；
而 $P^r u_{\rm reg}^p$ 的零阶至少为 $r$。
所以全部 $0\le j<r$ 的所需低 jet 都不受该修正影响：
$$
\boxed{\qquad
[w^j]H
 =\frac1{a^2}[w^{2p+j}]
       P^r\delta_P^{p-r-2}(P^{r+2}T),
\qquad 0\le j<r.
\qquad}
\tag{1161.30}
$$
最后一步使用
$P^{-2p}=a^{-2}w^{-2p}+O(1)$；
其余项乘分子后的零阶至少为 $p+r$，不进入读取。

因此 (1161.30) 同时适用于原
$H_1(0),H_7(0)$、$H_2'(0)$、
$H_3(0),[w^2]H_3$。
其中 $H_7$ 的源仍是
$[wP^7]_{\deg<p}-[wP^7]_{\deg<p}(1)$，
不能改成完整 $wP^7-1$。
将这些值代入 (1154.95)、(1154.99)，就是同一原
$\mathsf h,\mathbf B_\nu,\mathbf U_\nu,\mathbf V_\nu$
和 Bernoulli 系数 $3/8$，没有换一个未加权的检测。

以上新身份固定了原 Eisenstein 权重、相对 Cartier 系数、
低 jet 的 Frobenius 修正范围和有限对数误差的确切起阶。
它们尚未证明不同的 $\eta^2,\eta'^2$ 必被
(1161.18) 的 actual-good 子集分离；
特别不由 $\delta_P$ 的 restricted power 推出该子集封闭。
后继仍须处理原两点差以及同一 $Q_s$，
不能把 (1161.25) 的单个最高系数或 (1161.30) 的存在性
替代指定 weighted minor 的非零。全部为纸面推导，无数学程序执行。


## 10. 全部实际行的唯一有限对称幂逆与完整首 $p$ forcing

本节继续固定 §§5–9 的同一个 $P,V,Q_s$，而不换取未加权源。
它把 (1161.17) 的每条真实行写成一个唯一有限逆的低 jet。
低偶行的一维障碍完整保留；对角单位只说明这些读数之间的
三角等价，不说明实际 good 行共同分离两点。

### 10.1. 原有限 Legendre connection 的核

置
$$
\mathcal A=\mathbf F_p[w]/(w^p),\quad
D=(1-w^2)\frac d{dw},\quad
\phi=\lambda(1-w^2),\quad \lambda=-\frac5{36}.
$$
以下 $V$ 取 (1161.27) 的原多项式代表后约到 $\mathcal A$。
原式准确给
$$
(D^2+\phi)P=0,\qquad
(D^2+\phi)V=a\,w^{p-1},\qquad
P\,DV-V\,DP=-1.
\tag{1161.31}
$$
最后一式在 $\mathcal A$ 中成立；
在函数域中的差仍是 (1161.27) 的 $P^2w^{p-1}$。

对 $1\le s<p$，记 $\mathcal S_s$ 为
$D^2+\phi$ 的第 $s$ 个 scalar symmetric-power operator，
首项为 $D^{s+1}$。
它可直接由秩二方程在 $\operatorname{Sym}^s$ 上的
$s+1$ 个方程消元定义：相邻系数 $1,\ldots,s$
均为单位，故系数在 $\mathbf F_p[w]$ 中。
在有理函数域中同一消元给
$$
\boxed{\qquad
\mathcal S_s
 =P^{-s-2}\delta_P^{\,s+1}\circ P^{-s},
\qquad \delta_P=P^2D .
\qquad}
\tag{1161.32}
$$
例如可在一个 differential extension 中令
$\delta_P z=1$，则 $P^sz^j$, $0\le j\le s$，
同时给出两边的 $s+1$ 个解并锁定首项。
约到 $\mathcal A$ 时使用已消去分母的多项式算子；
不在 $\mathcal A$ 中反除 $P$。

给出该有限算子的完整核证明。
在实际基
$$
\begin{pmatrix}P&V\\DP&DV\end{pmatrix}
$$
中，原秩二 connection 为
$$
\nabla_D=D+w^{p-1}N,\qquad
N(e_2)=e_1,\quad N(e_1)=0.
$$
确实，将 (1161.31) 的误差列 $(0,aw^{p-1})^t$
乘以此矩阵的逆，只得 $(w^{p-1},0)^t$；
这里使用 $V(0)=a^{-1}$、$P(0)=0$。

在 $\mathcal A$ 中 $D^p=D$。
也可直接令 $x=(1+w)/(1-w)$，得到 $D=2x\,d/dx$。
由 $D^p=D$ 和原点常数项 $(p-1)!=-1$，
$$
D^{p-1}(w^{p-1})=w^{p-1}-1.
$$
因此
$\nabla_D^p-\nabla_D=-N$。
张量求导的 Leibniz 公式在模 $p$ 后消去中间二项式项，
所以在 $\operatorname{Sym}^s$ 上的 $p$-curvature
准确为 $-N_s$。
因 $s<p$，$N_s$ 是一个 Jordan block，
核仅由 $e_1^s$ 生成。
任一 horizontal vector 因而是 $c(w)e_1^s$，
再由 $Dc=0$ 得 $c\in\mathbf F_p$。
scalar cyclic elimination 与此一一对应，故
$$
\boxed{\qquad
\ker(\mathcal S_s:\mathcal A\to\mathcal A)
     =\mathbf F_p P^s .
\qquad}
\tag{1161.33}
$$
这里的有限 Jordan 结论来自显示的实际 connection，
并非从一般不可约三对角矩阵推得。

配对
$$
\langle f,g\rangle=\mathscr R(fg)
 =[w^{p-1}]\frac{fg}{1-w^2}
$$
在 $\mathcal A$ 上非退化，且 $D^*=-D$。
由 (1161.32)，先在有理函数域计算
$\delta_P^*=-P^{-2}\delta_PP^2$，再消去分母，得到
$$
\boxed{\qquad
\mathcal S_s^*=(-1)^{s+1}\mathcal S_s,\qquad
\operatorname{im}\mathcal S_s
 =\{T\in\mathcal A:\mathscr R(P^sT)=0\}.
\qquad}
\tag{1161.34}
$$
后一式由前式和 (1161.33) 的准确秩 $p-1$ 得到。

### 10.2. 原低偶行的 cokernel 不能删除

回到全部实际范围 $2\le s\le(p-3)/2$，置
$$
T_s=P^{s-2}Q_s,\qquad
J_s=a^{-s}w^{p-1-s}.
$$
(1161.25) 的原 Cartier 身份，以及 $P=aw+O(w^3)$，
分别给
$$
\mathscr R(P^sT_s)=Q_s(0),\qquad
\mathscr R(P^sJ_s)=1 .
\tag{1161.35}
$$
因此有唯一的有限多项式 $\mathscr H_s\in\mathcal A$，满足
$$
\boxed{
\mathcal S_s\mathscr H_s=T_s-Q_s(0)J_s,\qquad
\mathscr H_s(-w)=(-1)^{s+1}\mathscr H_s(w).
}
\tag{1161.36}
$$
这是同一 $Q_s$ 的实际逆，不是任意选择的一个 primitive。

证明唯一性还须保奇偶性。
$T_s$ 为偶，$\mathcal S_s$ 改变奇偶性的因子为
$(-1)^{s+1}$，而其唯一核 $P^s$ 的奇偶性为
$(-1)^s$。
若 $s$ 奇，$Q_s$ 奇而 $Q_s(0)=0$；
$\mathcal S_s$ 在偶子空间上为双射。
若 $s$ 偶，目标为偶，(1161.35) 正好扣除其一维 cokernel；
将任一解取奇部分即给 (1161.36)，且没有奇核。
特别，低偶行未经修正的方程
$\mathcal S_sH=T_s$ 可解当且仅当 $Q_s(0)=0$。
没有为得到“全行逆”擅自抹去这个条件。

为保全部标记，暂以 $c$ 代替 $\kappa\eta$，定义
$$
\mathfrak M_s(c)=\mathscr R\bigl(T_s(V+cP)^s\bigr),\qquad
\mathfrak B_s(c)=a^{-s}[w^s]\frac{(V+cP)^s}{1-w^2}.
$$
则 $\mathcal M_s(\eta)=\mathfrak M_s(\kappa\eta)$。
由 (1161.34)–(1161.36)，得到完整读式
$$
\boxed{
\mathfrak M_s(c)=
 (-1)^{s+1}\mathscr R\!\left(
       \mathscr H_s\,\mathcal S_s(V+cP)^s\right)
       +Q_s(0)\mathfrak B_s(c).
}
\tag{1161.37}
$$
这里 $\mathfrak B_s$ 的 $c^s$ 系数准确为一。
若 $s$ 偶，它为偶多项式；若 $s$ 奇，其系数在
(1161.37) 前已为零。低偶行的最高项因此仍为
$Q_s(0)c^s$，没有用 Bernoulli 非零假设反除它。

### 10.3. 只保一次误差的完整 symmetric-power forcing

以下从函数域中的真等式 (1161.27) 出发。
令
$$
Y_c=V+cP,\qquad Z_c=Y_c/P,\qquad
E=P^2w^{p-1}.
$$
则 $\delta_PZ_c=-1+E$。
把 $Z$ 暂看成独立变量，给
$\operatorname{ord}w=1,\operatorname{ord}Z=-1$。
算子
$\delta_P-\partial_Z$ 升赋值至少一，
$E\partial_Z$ 升赋值至少 $p+2$。
在 $(s+1)$ 次作用于 $Z^s$ 后，
含至少两次 $E\partial_Z$ 的词，再乘 $P^{-s-2}$，
赋值至少为 $2p+1-s>p$，不进入 $\mathcal A$。

零次误差项为零。
对恰一次误差按其位置展开，且保留其后对 $E$ 的全部导数，
二项式求和给
$$
\boxed{
\mathcal S_s(Y_c^s)=
s!P^{-s-2}
\sum_{r=1}^{s}
 (-1)^{s-r}\binom{s+1}{r+1}
 \frac{\delta_P^rE}{(r-1)!}\,Z_c^{r-1}
 \pmod{w^p}.
}
\tag{1161.38}
$$
这里使用
$\sum_{\ell=0}^{s-r}\binom{s-\ell}{r}
 =\binom{s+1}{r+1}$。
右侧虽以 Laurent 表达式显示，
各项最低次数均非负，且左侧是已定义的多项式算子。
所有阶乘指标小于 $p$。

特别，对 $0\le i<s$，
$$
\boxed{
[c^i]\mathcal S_s(Y_c^s)
 =(-1)^{s+i+1}(i+1)s!\,a^{\,2i+2-s}
       w^{p-s+i}+O(w^{p-s+i+2}).
}
\tag{1161.39}
$$
要核完整常数，用
$\delta_P^rE=a^{2r+2}r!\,w^{p+r+1}+\cdots$
和 $V/P=a^{-2}w^{-1}+O(w)$。
剩余有限和是
$$
\sum_{r=i+1}^{s}
 (-1)^{s-r}r\binom{s+1}{r+1}\binom{r-1}{i}
 =(-1)^{s+i+1}(i+1).
$$
例如其生成式在次数小于 $s$ 的部分恰为
$(-1)^{s+1}(1+x)^{-2}$，逐项即得此式。
$c^s$ 项为零，因为 $\mathcal S_sP^s=0$。

### 10.4. 原 centered 系数与低 jet 的单位三角关系

将 (1161.39) 代入完整 (1161.37)。
对偶数 $i$ 满足 $2\le i<s$，有
$$
\boxed{
\begin{aligned}
[c^i]\bigl(\mathfrak M_s-Q_s(0)\mathfrak B_s\bigr)
={}&(i+1)s!\,a^{\,2i+2-s}
       [w^{s-i-1}]\mathscr H_s\\
&+\text{只含同奇偶性且次数小于 $s-i-1$
的 $\mathscr H_s$ 系数的线性组合}.
\end{aligned}}
\tag{1161.40}
$$
adjoint 的 $(-1)^{s+1}$ 与 forcing 首项符号
在偶 $i$ 时恰相消，故对角统一是显示的正号。
$1/(1-w^2)$ 与 forcing 的较高项只读更低的 jet，
不会改动对角。

对奇 $s$，原轮廓的 centered coefficients 因而与
$$
[w^0]\mathscr H_s,\ [w^2]\mathscr H_s,\ldots,
       [w^{s-3}]\mathscr H_s
$$
作单位三角变换。
对偶 $s$，先完整保留 $Q_s(0)\mathfrak B_s$，
剩余 centered coefficients 与
$$
[w^1]\mathscr H_s,\ [w^3]\mathscr H_s,\ldots,
       [w^{s-3}]\mathscr H_s
$$
作单位三角变换；另有最高系数 $Q_s(0)$。
所有对角因子均为单位，因 $i+1\le s<p$、$a\ne0$。
未被 centered profile 读取的 $s-1$ 次 jet 不被设为零。

例如 $s=2$ 只剩原 $Q_2(0)c^2=c^2/720$，
仍须其实际出现条件。
$s=3$ 给
$$
[c^2]\mathfrak M_3=18a^3\mathscr H_3(0)
 =\frac{a^2\mathsf h}{10080}.
\tag{1161.41}
$$
所以新 $\mathscr H_3$ 指的是源 $wP/30240$ 的有限逆；
它不是 R1154 §16 中源 $wP^5-1$ 的另一个 $H_3$。
这里的尺度仍正好回到 (1161.19)，不新增一条角色。

### 10.5. 相邻 symmetric powers 的真实 source 变换

为明确何种跨行操作已付、何种尚未付，
从 (1161.32) 还得到一个完全显示的 operator identity：
$$
\boxed{
\mathcal S_{s+2}\circ P^2=\mathscr L_s\circ\mathcal S_s,
}
$$
$$
\mathscr L_s(T)=P^2D^2T+2(s+3)P(DP)DT
 +(s+2)\bigl((s+3)(DP)^2-\phi P^2\bigr)T.
\tag{1161.42}
$$
证明是直接展开
$\mathscr L_s=P^{-s-4}\delta_P^2\circ P^{s+2}$，
再用 $D^2P=-\phi P$。
取 adjoint 同时给
$P^2\mathcal S_{s+2}=\mathcal S_s\mathscr L_s^*$。
这对其实际范围内的 $s,s+2$ 都成立。

但 (1161.42) 运输的是完整
$\mathscr L_s(P^{s-2}Q_s-Q_s(0)J_s)$；
没有证明它等于下一条
$P^sQ_{s+2}-Q_{s+2}(0)J_{s+2}$。
因此不能把这个真实 symmetric-power 关系自动当作
(1161.18) 的 good-mask 闭性。
本节完成的是全部原 weighted rows 的有限唯一逆、
低偶行的准确一维障碍和 centered 系数的完整单位三角读取。
后继仍须处理这些指定逆之间的真正关系，或直接证明原两点差非零。
全部为纸面推导，无数学程序执行。


## 11. 保原点值的一阶运输、同权 Hecke 源与共同二阶分母

本节把 §10 的相邻对称幂关系细化成保持同一个 $c=\kappa\eta$
的点值身份。全部实际行由此进入一个确定的同权模形式空间，
其 Hecke 特征值正是原角色的特征值除以 $\ell$。
最后的两点条件保留完整 mask；没有把 Gaussian 单点 jet 理想
预先宣称为 Hecke 稳定。

### 11.1. 跨奇偶行的实际一阶关系

仍在 $\mathcal A=\mathbf F_p[w]/(w^p)$ 中，定义
$$
\mathscr J_j=-P D-(j+2)DP,\qquad
\mathscr J_j^*=P D-(j+1)DP .
$$
这里 $DP$ 表示乘以该函数，adjoint 使用原 $\mathscr R$。
由 (1161.31)，对 $Y_c=V+cP$ 和 $j+1<p$ 准确有
$$
\boxed{\qquad
\mathscr J_j^*(Y_c^{j+1})
 =(j+1)Y_c^j(PDY_c-Y_cDP)
 =-(j+1)Y_c^j .
\qquad}
\tag{1161.43}
$$
函数域中的额外项含 $P^2w^{p-1}$，在这里的实际
$\mathcal A$ 中确为零；没有将它从更高 jet 的恒等式中删除。
因此对任意实际源 $T\in\mathcal A$，
$$
\mathscr R((\mathscr J_jT)Y_c^{j+1})
 =-(j+1)\mathscr R(TY_c^j).
$$
并且 $\mathscr J_{j+1}\mathscr J_j=\mathscr L_j$，
故 (1161.42) 的点值版本为
$$
\mathscr R((\mathscr L_jT)Y_c^{j+2})
 =(j+1)(j+2)\mathscr R(TY_c^j).
\tag{1161.44}
$$
这些是对原 $c$ 的多项式身份，不是对两个相等点值横向微分。

对原 $T_s=P^{s-2}Q_s$，(1161.24) 的同一 Katz 导子给
$$
\mathscr J_sT_s=2P^{s-2}
      (\mathscr TG_{2s})\big|_{(1,-w)}.
$$
继续到第 $j=s+n$ 行时，实际模形式权模 $p$ 为
$2s+n=s+j$，恰好是微分 $P^{s-2}$ 后的完整 $DP$ 系数。
所以可逐项迭代为
$$
\boxed{
\mathscr J_{S-1}\cdots\mathscr J_sT_s
 =2^{S-s}P^{s-2}
        (\mathscr T^{S-s}G_{2s})\big|_{(1,-w)}
\quad(s\le S\le p-1),
}
\tag{1161.45}
$$
其 moment 为
$(-1)^{S-s}S!/s!$ 乘原 $\mathfrak M_s(c)$。
本式没有在迭代中把权误写成 $2j$。

### 11.2. 全部原角色进入同一个真实 Hecke 源

用标准 $E_4,E_6$ 多项式记原 $G_{2s}$，
并定义全局模形式
$$
\boxed{\qquad
\mathcal F_s=A^{s-2}\mathscr T^{p-1-s}G_{2s},
\qquad \operatorname{wt}(\mathcal F_s)=(p-1)^2 .
\qquad}
\tag{1161.46}
$$
这里 $A=E_{p-1}$ 是同一个 Hasse 多项式；
权的计算是
$$
(s-2)(p-1)+2s+(p-1-s)(p+1)=(p-1)^2.
$$
所有 $2\le s\le(p-3)/2$ 均用这一权，不是混权 $q$ 展开比较。

在 Tate 参数 $q_{\rm T}$ 上，$\mathcal F_s$ 的常数项为零，
而对 $n\ge1$，
$$
[q_{\rm T}^n]\mathcal F_s=
 \frac{2}{(2s-1)!}\,
 n^{p-1-s}\sigma_{2s-1}(n).
\tag{1161.47}
$$
当 $p\mid n$ 时右边为零；
当 $p\nmid n$ 时，幂可准确写成 $n^{-s}$。
因此它是一个非零的 mod-$p$ cusp form，
其 $q_{\rm T}^1$ 系数为单位。
这里没有反除 $B_{2s}$。

对每个素数 $\ell\ne p$，使用权 $(p-1)^2$
的标准 Hecke 系数式，
$\ell^{(p-1)^2-1}\equiv\ell^{-1}\bmod p$，
以及原 Eisenstein divisor-sum 恒等式，得到
$$
\boxed{\qquad
T_\ell\mathcal F_s
 =(\ell^{-s}+\ell^{s-1})\mathcal F_s
 =\ell^{-1}(\ell^R+\ell^{1-R})\mathcal F_s .
\qquad}
\tag{1161.48}
$$
最后一式对 (1161.2) 的两种实际 $R$ 都成立：
低偶行 $R=s$，高偶行 $R=p-s\equiv1-s\pmod{p-1}$。
证明也可逐 Fourier 系数写成
$T_\ell\mathscr T^nG_{2s}
 =\ell^n(1+\ell^{2s-1})\mathscr T^nG_{2s}$；
整数权以 (1161.46) 统一后，§2 的固定权展开原则支付
模形式等式，而不只支付一份形式级数。

所以
$\mathscr U_{\rm good}=\operatorname{span}_{\mathbf F_p}
 \{\mathcal F_s:s\in\mathcal S_{\rm good}\}$
是真实、同权、away-$p$ Hecke 稳定的源空间。
此处的指标仍严格是原实际出现且 good 的集合；
(1161.46) 对其他 $s$ 的存在不把它们添加为观测。
(1161.48) 只锁定显示的标准特征值，
不额外识别一个尚未给出的整 Jacobian 格或局部 Hecke 算子。

### 11.3. 同一个 Cauchy 核准确读回全部原行

在 (1161.45) 取 $S=p-1$。
由于 $A(1,-w)=-P$、$(p-1)!=-1$、
$2^{p-1-s}=2^{-s}$ 和 $Y_c^p=a^{-1}$ 于 $\mathcal A[c]$，
所有符号和阶乘合并后给
$$
\boxed{\qquad
\mathfrak M_s(c)
 =-\frac{s!}{2^s a}\,
      \mathscr R\!\left(
        \frac{\mathcal F_s(1,-w)}{V+cP}\right).
\qquad}
\tag{1161.49}
$$
$V+cP$ 在原点常数为 $a^{-1}$，所以这里是真正的单位逆。
没有对 $c$ 假设 $c^p=c$；$P^p=0$ 已使其贡献消失。

再用原 $f=aV$、$\xi=P/(af)$。
本坐标满足 $\xi=w+O(w^3)$、
$dw/(1-w^2)=f^2d\xi$，且 $f^p=1$ 于 $\mathcal A$。
同权性以及 $(p-1)^2\equiv1\pmod p$ 准确给
$$
f\,\mathcal F_s(1,-w)
 =\mathcal F_s(f^4,-wf^6)
 =:\widehat{\mathcal F}_s(\xi)\pmod{\xi^p}.
$$
所以 (1161.49) 变成
$$
\boxed{\qquad
\mathfrak M_s(c)
 =-\frac{s!}{2^s}
     [\xi^{p-1}]
      \frac{\widehat{\mathcal F}_s(\xi)}
           {1+a^2c\xi}.
\qquad}
\tag{1161.50}
$$
这里的 $f^4,-wf^6$ 正是 R1154 §§15、17 的原有限
$E_4,E_6$，不延伸未付的无限 flow。

权 $(p-1)^2$ 为四的倍数，故
$\mathcal F_s(1,-w)$ 为偶多项式；
$f$ 偶、$\xi$ 奇使 $\widehat{\mathcal F}_s$ 也为偶。
令
$$
m=(p-1)/2,\qquad \tau=\xi^2,\qquad
\widehat{\mathcal F}_s(\xi)=\mathcal C_s(\tau)
 \quad\bmod \xi^p,\qquad \deg\mathcal C_s\le m .
$$
将 $c=\kappa\eta$ 代回，并用 (1161.14)，定义原 coarse
坐标的一个明确单位缩放
$$
Z=a^4c^2=a^4\kappa^2\eta^2
   =-\frac{\eta^2}{12a_{\rm G}} .
$$
因此新的显示尺度中 $a_\nu$ 和临时第四根均消去。
由偶性，(1161.50) 准确等价于
$$
\boxed{\qquad
\mathcal M_s(\eta)
 =-\frac{s!}{2^s}
       [\tau^m]\frac{\mathcal C_s(\tau)}{1-Z\tau}.
\qquad}
\tag{1161.51}
$$
所有 $\mathcal C_s$ 都来自 (1161.46) 的同一权空间；
并非为每条行重新选择任意的反序多项式。

### 11.4. 保全部 mask 的两点余核

对同一原 coarse component 中的两个允许点，
记相应缩放为 $Z,Z'$，并令
$$
S=Z+Z',\qquad P_{\rm pair}=ZZ'.
$$
若 $Z\ne Z'$，则
$$
\frac1{1-Z\tau}-\frac1{1-Z'\tau}
 =\frac{(Z-Z')\tau}
        {1-S\tau+P_{\rm pair}\tau^2}.
$$
代入 (1161.16) 与 (1161.51) 后，
原完整归一的行差为
$$
\boxed{
\Pi_R(t_*^2)-\Pi_R(t_*'^2)
 =-N_R\delta(2s-1)!(Z-Z')\,
 [\tau^{m-1}]
 \frac{\mathcal C_s(\tau)}
      {1-S\tau+P_{\rm pair}\tau^2}.
}
\tag{1161.52}
$$
因所示外部因子均为单位，原共同纤维准确等价于
$$
\boxed{\qquad
[\tau^{m-1}]
 \frac{\mathcal C_s(\tau)}
      {1-S\tau+P_{\rm pair}\tau^2}=0
 \quad\hbox{对全部 }s\in\mathcal S_{\rm good}.
\qquad}
\tag{1161.53}
$$
本式保 $S=0$、$P_{\rm pair}=0$，也保 R1135 §10 的两个
twists；没有将其他原 coarse components 合并。
$\mathcal C_s$ 的 $\tau^m$ 项是本次差值未读取的真正常数层，
不能据此将它设为零。

例如原 $s=2$ 的 centered slope 是 $c^2/720$，
故这里准确有
$[\tau^{m-1}]\mathcal C_2=-1/(360a^4)$，
更低项为零。
这只在原 $s=2$ 实际出现时给 affine 单位行，
不绕过 R1127 的 Bernoulli 条件。

(1161.48) 支付的是全局同权源的真实 Hecke 稳定。
它并未证明映射
$\mathcal F_s\mapsto\mathcal C_s$ 的 Gaussian 单点 jet 核
为 Hecke 稳定，也未证明 Hecke 对应仅移动这两个 coarse 点。
因此不能由该全局稳定性直接推出原节点代数的 Euler 稳定。
本节的新共同源和二阶分母保留了这条准确边界；
后继仍须证明 (1161.53) 对不同允许点不可能同时成立，
或付清一个真正作用于此余核的操作。
全部为纸面推导，无数学程序执行。


## 12. 同一源的超奇异极部、原 Hecke trace 与指定对数留数

本节把 §11 的同权源除以同一个 Hasse 幂，得到实际的
weight-zero 有理模函数。其极部阶数、Hecke 规范和原两点差的
留数读取都可完整支付。这没有把全局对应局部化到 Gaussian 点；
最后列明其它超奇异点在全局留数式中的准确位置。

### 12.1. 全部原行的同权 companion 身份

保留原 $2\le s\le(p-3)/2$，置
$$
m_s=p+1-2s,\qquad 4\le m_s\le p-3.
$$
仍用 $g_j$、$G_j=2g_j/(j-1)!$ 和 §2 的
$\mathscr T=A\mathfrak d+\operatorname{wt}(\,\cdot\,)B/12$。
有准确同权身份
$$
\boxed{\qquad
\mathscr T^{m_s}g_{2s}
 =A^{m_s}\mathscr Tg_{m_s}.
\qquad}
\tag{1161.54}
$$
两边的整数权都为 $m_sp+p+1$。
当 $p\nmid n$ 时，其 Fourier 系数相等是
$$
n^{p+1-2s}\sigma_{2s-1}(n)
 =n\,\sigma_{p-2s}(n)\pmod p;
$$
这是将 divisor $d$ 换成 $n/d$，再用
$n^{p-1}=1$ 的直接结果。
当 $p\mid n$ 时，两边均为零，常数项也均为零。
所有 $g$ 的权均在 $4,\ldots,p-3$，故系数 $p$ 整。
§2 的固定整数权、首 $q$ 系数为单位的三角基因而给 (1161.54)；
没有用混权 $q$ 展开作单射，也没有反除任何 Bernoulli 数。

由 $\mathfrak dA=B/12$ 和 $\operatorname{wt}A=p-1$，
准确有 $\mathscr TA=0$。
对 (1161.54) 再施 $\mathscr T^{s-2}$，
并乘 (1161.46) 中的 $2A^{s-2}/(2s-1)!$，得到
$$
\boxed{\qquad
\mathcal F_s
 =\frac{2}{(2s-1)!}\,
 A^{p-1-s}\mathscr T^{s-1}g_{m_s}.
\qquad}
\tag{1161.55}
$$
这里 $m_s+s-2=p-1-s$。
最后的 $\mathscr T^{s-1}g_{m_s}$ 权为 $s(p-1)$，
所以它和 (1161.46) 的权完全吻合。
(1161.55) 是同一原源的整幂整除式，不是为各行重选 companion。

### 12.2. 真正的 weight-zero 函数与完整首极系数

定义
$$
\boxed{\qquad
\mathfrak r_s
 :=\frac{\mathcal F_s}{A^{p-1}}
 =\frac{2}{(2s-1)!}\,
   \frac{\mathscr T^{s-1}g_{m_s}}{A^s}.
\qquad}
\tag{1161.56}
$$
分子、分母权相等，故 $\mathfrak r_s$ 是原 level-one
模曲线上的有理函数，不依 Hodge frame。
它只可能在 Hasse 零点有极，每个几何超奇异点的
stack 局部极阶至多为 $s$。
这里 Hasse 零点的简单性可沿用 R1135 §14.2 的自足证明：
在固定非零判别式曲线上，$\partial$ 无零，
$\partial^2A=(a/3)A$，而 $\operatorname{pole}_O A=(p-1)/2<p$；
若零阶 $j\ge2$，左边的首项单位 $j(j-1)$ 与右边零阶矛盾。
这个论证只用 Hasse 身份，不用 R1135 其它函数上的 Bernoulli 分支。

在 cusp，$A(q)=1$，故 $\mathfrak r_s$ 的 $q$ 展开就是
(1161.47)。特别其零阶恰为一，
首项为 $2q/(2s-1)!$。
这给每条 $\mathfrak r_s$ 的非零性，但不支付其某个 Gaussian jet 的非零性。

还可保留每个超奇异点的准确最高极系数。
模 $A$，第 $j$ 次 $\mathscr T$ 的乘权因子是 $m_s+j$；
因此
$$
\boxed{
A^s\mathfrak r_s
 \equiv
 \frac{2(-1)^{s-1}}{s!}
 \left(\frac B{12}\right)^{s-1}g_{m_s}
 \pmod A.
}
\tag{1161.57}
$$
计算中用的是
$(m_s)_{s-1}=(-1)^{s-1}(2s-1)!/s!$。
所有显示阶乘都是单位。
在 Gaussian 点，奇 $s$ 给 $m_s\equiv2\bmod4$，
所以 $g_{m_s}(E_4,0)=0$，极阶至少再降一阶。
偶 $s$ 的最高系数仍须保留原 $g_{m_s}$ 的实际值；
它不等于该模形式在 cusp 的 Bernoulli 常数。

在 $w$ chart，
$$
\mathfrak r_s(w)
 =\frac{\mathcal F_s(1,-w)}{P(w)^{p-1}}.
$$
它为偶函数。其在 Gaussian 局部 $w=0$ 的极阶至多为 $s$，
奇 $s$ 时至多为 $s-1$。
对真正 coarse 参数 $w^2$，这给极阶至多 $\lfloor s/2\rfloor$。
这些界全由同一原源而来。

### 12.3. 无额外 $\ell$ 相位的原 Hecke trace

对素数 $\ell\ne p$，令 $\operatorname{Tr}_\ell$ 表示
全部 cyclic order-$\ell$ 子群的未归一 trace：
$$
(\operatorname{Tr}_\ell r)(E)
 =\sum_{\substack{C\subset E\\|C|=\ell}}r(E/C),
$$
按该对应的实际 multiplicities 求和。
由于 $r$ 权为零，这里不再选择目标 Hodge frame。

若为比较取 $\phi^*\omega'=\omega$，
relative Cartier 与 prime-to-$p$ isogeny 的相容性给
$A(E/C,\omega')=A(E,\omega)$。
权 $W=(p-1)^2$ 的标准算子是
$\ell^{-1}$ 乘这个带 differential 的子群和。
因此 (1161.48) 准确变成
$$
\boxed{\qquad
\operatorname{Tr}_\ell\mathfrak r_s
 =(\ell^s+\ell^{1-s})\mathfrak r_s
 =(\ell^R+\ell^{1-R})\mathfrak r_s .
\qquad}
\tag{1161.58}
$$
最后一式仍同时覆盖原低偶 $R=s$ 与高偶 $R=p-s$。
也可直接在 Tate curve 核规范：
未归一 trace 的系数为
$\ell a_{\ell n}+a_{n/\ell}$，
而 $\ell^W=1\bmod p$，恰是 $\ell T_W$。
所以这次除以 Hasse 幂后得到的是真正原角色的 Hecke trace，
没有另留 $\ell^{-1}$ 或人为缩放。

只取原 $\mathcal S_{\rm good}$ 时，
$\operatorname{span}\{\mathfrak r_s:s\in\mathcal S_{\rm good}\}$
仍是这个全局 trace 的稳定空间。
未出现或非 good 的其它 $s$ 不因此成为观测。

### 12.4. 原两点差的指定 logarithmic residue

以下仍用原 $Y_c=V+cP$，其中 $c=\kappa\eta$；
$V=W_{\nu-1}-PL_p$ 是已固定的完整有限多项式。
记 $\operatorname{Res}_0$ 为原 $w=0$ 处函数域微分的留数。
由
$$
\mathscr R(H)=\operatorname{Res}_0\frac{H\,dw}{q\,w^p},
\qquad
\frac{P^p}{w^p}=a+O(w^p),
$$
以及 $\operatorname{pole}_0\mathfrak r_s\le s<p$，
(1161.49) 准确给
$$
\boxed{\qquad
\mathfrak M_s(c)
 =-\frac{s!}{2^s}\,
   \operatorname{Res}_0
      \frac{\mathfrak r_s\,dw}{qP Y_c}.
\qquad}
\tag{1161.59}
$$
误差的零阶至少为 $p$，其余因子的极阶至多 $s+1$，
所以该误差不能贡献留数。
$Y_c(0)=a^{-1}$ 保证这里对任意 $c$ 都是同一合法局部读取。

必须保完整有限-log Wronskian。
在有理函数域中，实际身份是
$$
P DV-V DP=-1+P^2w^{p-1},
$$
从而
$$
\boxed{
d\log\frac{Y_c}{Y_{c'}}
 =\frac{(c-c')(1-P^2w^{p-1})}{qY_cY_{c'}}\,dw .
}
\tag{1161.60}
$$
其中 $P^2w^{p-1}$ 在原点的阶至少为 $p+1$。
乘 $\mathfrak r_s$ 后，它仍不生留数。
将 (1161.59) 的两个值相减，于是得到
$$
\boxed{
\begin{aligned}
\mathfrak M_s(c)-\mathfrak M_s(c')
 &=\frac{s!}{2^s}
   \operatorname{Res}_0
     \left(\mathfrak r_s\,d\log\frac{Y_c}{Y_{c'}}\right),\\
\Pi_R(t_*^2)-\Pi_R(t_*'^2)
 &=N_R\delta(2s-1)!
   \operatorname{Res}_0
     \left(\mathfrak r_s\,d\log\frac{Y_{\kappa\eta}}
                                      {Y_{\kappa\eta'}}\right).
\end{aligned}}
\tag{1161.61}
$$
第一式的号为正；它由
$Y_{c'}-Y_c=(c'-c)P$ 和 (1161.59) 的负号共同给出。
第二式保留原 $N_R,\delta$ 全尺度。
这两式在所需系数扩域上成立，并由原偶性下降到
$Z=-\eta^2/(12a_{\rm G})$。
不假设 $c^p=c$，也不删 $Z+Z'=0$ 或 $ZZ'=0$。

和 (1161.52) 对照，(1161.61) 的留数准确等于
$$
-(Z-Z')\,[\tau^{m-1}]
 \frac{\mathcal C_s(\tau)}
 {1-(Z+Z')\tau+ZZ'\tau^2}.
$$
因此是同一个原两点余核的函数域读取，不是另一份任意局部泛函。

### 12.5. 全局留数的其余项不能删除

这个读取还给一份有限、完整的全局关系。
$P$ 的有限零点都是简单零，且不在 $w=\pm1$；
由 (1161.60) 前的 Wronskian，在 $P(\alpha)=0$ 处
$$
V(\alpha)DP(\alpha)=1.
$$
所以全部 $Y_c$ 都不在这些点为零，
$Y_c/Y_{c'}$ 在那里取值一。
其 logarithmic differential 虽然正则，
乘有极的 $\mathfrak r_s$ 后仍可能有非零留数。

对 $c\ne c'$，在代数闭包中按重数记
$$
\mathcal T_s(c)=
 \sum_{Y_c(\zeta)=0}\operatorname{mult}_\zeta(Y_c)\,
                         \mathfrak r_s(\zeta).
$$
每项都有定义，因为 $P$ 与 $Y_c$ 无共同零点。
这也可按 closed points 写成 residue-field traces；
不要求 $Y_c$ 的根全部简单。

在无穷远，
$\deg V=p+\nu-2$、$\deg P=\nu$，
故 $Y_c/Y_{c'}=1+O(w^{-(p-2)})$。
另一方面 (1161.56) 的 numerator 权为 $s(p-1)$，
所以
$$
\operatorname{pole}_{\infty}\mathfrak r_s
 \le \max\!\left\{0,\left\lfloor\frac{s(p-1)}6\right\rfloor-s\nu\right\}
 \le\left\lfloor\frac{2s}{3}\right\rfloor.
$$
于是 $\mathfrak r_s\,d\log(Y_c/Y_{c'})$ 在无穷远不生留数。
在 $w=\pm1$，$\mathfrak r_s$ 为零，故即使 $Y_c$ 在那里为零，
所得项也为零。
有理曲线上的全局留数定理现在准确给
$$
\boxed{
\sum_{P(\alpha)=0}
 \operatorname{Res}_{w=\alpha}
    \left(\mathfrak r_s\,d\log\frac{Y_c}{Y_{c'}}\right)
 =\mathcal T_s(c')-\mathcal T_s(c).
}
\tag{1161.62}
$$
若在非代数闭底域写本式，各留数亦取相应 field trace。

因此 (1161.61) 的 Gaussian 项只是 (1161.62) 的指定
$\alpha=0$ 项。其余 Hasse 根处的留数和
$\mathcal T_s(c')-\mathcal T_s(c)$ 都是实际来源的一部分，
不能因 (1161.58) 而设为零。
本节支付 companion 的完整 Hasse 整除、真实 pole/cusp 范围、
原未归一 Hecke 特征值和指定 logarithmic residue；
后继仍须在原 good mask 上控制 (1161.61)，
或付清真正保持该指定余核的操作。
全部为纸面推导，无数学程序执行。
