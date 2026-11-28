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
