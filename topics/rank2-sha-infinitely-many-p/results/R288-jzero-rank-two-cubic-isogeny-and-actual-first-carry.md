# R288 — 新固定 j=0 秩二候选的真实三次同源、theta 对数与首进位

日期：2026-11-13。**状态：以下固定曲线的秩下界、实际三等分 theta 恒等式、未分歧三次覆盖及其 CM 同源识别、完整有理微分方程和惰性首分母带已证明。尚未构造该曲线的目标 Schwartz 截面与完整中央分支，不能把本篇的 theta frame 直接当成已付的 Sha 判据。主目标未完成。**

本篇在 O8 允许的固定有限候选中加入
$$
E^{(0)}:\quad y^2=x^3+17.
\tag{1}
$$
它不同于原 $E_{17}:y^2=x^3-17x$。原 $K=\mathbf Q(i)$ 的中央比较不被搬到新曲线；下述每一条几何和进位公式都在 (1) 的实际函数上重新证明。这里所需的三次根来自一个真正的未分歧同源覆盖，可以在固定三等分 theta 表达中实现。

## 1. 不依赖 Sha 的固定秩下界

取
$$
P=(-2,3),\qquad Q=(-1,4)\in E^{(0)}(\mathbf Q).
$$
判别式为 $-432\cdot17^2$。在两个好约化素数处直接计数得
$$
\#E^{(0)}(\mathbf F_5)=6,\qquad
\#E^{(0)}(\mathbf F_7)=13.
\tag{2}
$$
例如模五时，$x=0,1,2,3,4$ 对应的 $y$ 个数为 $0,0,1,2,2$；模七时，$x=0$ 无解，其他六个 $x$ 各有两解。加上无穷点便得 (2)。好约化处素于剩余特征的挠点约化单射；五、七初级部分可各用另一处排除，其他部分同时注入两个有限群。因此
$$
E^{(0)}(\mathbf Q)_{\rm tors}=0.
\tag{3}
$$

模十九的准确倍点表为

| $j$ | $j\bar P$ | $j\bar Q$ |
|---|---|---|
| $0$ | $O$ | $O$ |
| $1$ | $(17,3)$ | $(18,4)$ |
| $2$ | $(8,15)$ | $(6,10)$ |
| $3$ | $(0,6)$ | $(0,6)$ |
| $4$ | $(9,9)$ | $(5,3)$ |
| $5$ | $(9,10)$ | $(5,16)$ |
| $6$ | $(0,13)$ | $(0,13)$ |
| $7$ | $(8,4)$ | $(6,9)$ |
| $8$ | $(17,16)$ | $(18,15)$ |
| $9$ | $O$ | $O$ |

每项由弦切公式得到，两个九阶循环群的交恰为同一三阶群。它们生成阶二十七、指数九的非循环群，准确为 $C_9\times C_3$。
若 $P,Q$ 相关，由 (3)，其生成的有限生成无挠群只能是循环群或零；其约化像也应循环，与上表矛盾。因此
$$
\boxed{\operatorname{rank}E^{(0)}(\mathbf Q)\ge2.}
\tag{4}
$$
本篇不需要秩上界，也不以数据库的解析秩代替 (4)。

令 $\omega$ 为本原三次单位根。映射 $(x,y)\mapsto(\omega x,y)$ 给出 $\mathbf Z[\omega]$ 的复乘；相应 CM 域是 $\mathbf Q(\sqrt{-3})$。

## 2. 同一曲线上的准确三等分 theta

固定
$$
c^2=17,\qquad a^3=2c,\qquad
\delta=\sqrt{-3}=1+2\omega,
\qquad k=\mathbf Q(c,a,\omega).
\tag{5}
$$
只作这一次固定数域扩张。用 (1) 的不变微分 $dz=dx/(2y)$，取 Weierstrass 规范
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
\sigma=z+\cdots,\quad \zeta=\sigma'/\sigma,
$$
$$
x'=2y,\quad y'=3x^2,\quad \zeta'=-x.
\tag{6}
$$
$T=(0,c)$ 为非零三阶点：其切线 $y=c$ 与曲线在 $T$ 的交重数为三。选 $z_T$ 代表它，定义原点值一的 reduced translates
$$
\theta_+(z)=e^{-\zeta(z_T)z}\frac{\sigma(z+z_T)}{\sigma(z_T)},
\qquad
\theta_-(z)=e^{-\zeta(-z_T)z}\frac{\sigma(z-z_T)}{\sigma(-z_T)}.
\tag{7}
$$
这些式子先是复解析规范；以下立刻给出原点 germs 的纯代数恒等式，故同一规范可在特征零形式域中读取。

**定理 1。** 准确有
$$
\boxed{\theta_+^3=-(y+c)\sigma^3,\qquad
\theta_-^3=-(y-c)\sigma^3,\qquad
\theta_+\theta_-=x\sigma^2.}
\tag{8}
$$

**证明。** Weierstrass 加法式在 $x(T)=0$ 处给
$$
\zeta(z+z_T)-\zeta(z)-\zeta(z_T)=\frac{y-c}{x}.
$$
又由 $x^3=(y-c)(y+c)$ 得
$$
\partial_z\log(y+c)=\frac{3x^2}{y+c}=3\frac{y-c}{x}.
$$
所以第一式两边的对数导数相同。原点两边常数均为一，确定其常数因子；第二式将 $c$ 换为 $-c$。两式乘起来得到
$(\theta_+\theta_-)^3=x^3\sigma^6$，原点值仍固定三次根为一，得到第三式。$\square$

特别在原点，(8) 的右边均是常数一的 $k[[z]]$ 单位；在 $3$ 可逆处其规定三次根唯一。没有留下未指定的指数一次或二次因子。

## 3. 三次根确为未分歧的 CM 同源覆盖

定义
$$
u=\frac{a\sigma}{\theta_-},\qquad
v=\frac{\theta_+}{\theta_-}.
$$
由 (8) 准确有
$$
\boxed{u^3+v^3=1,\qquad
x=\frac{a^2v}{u^2},\qquad
y=c\left(1-\frac2{u^3}\right).}
\tag{9}
$$
原点支为 $u=az+\cdots$、$v=1+\cdots$。因此在光滑 Fermat 三次曲线
$$
\mathcal C:u^3+v^3=1
$$
上，(9) 给一个以 $O'=(0,1)$ 为原点的映射 $\varphi:\mathcal C\to E^{(0)}$。

其次数准确为三。事实上
$$
u^3=\frac{2c}{c-y},\qquad
\operatorname{div}\frac{2c}{c-y}=3(O)-3(T).
\tag{10}
$$
若右侧是 $k(E^{(0)})$ 中的三次幂，就有除子 $(O)-(T)$ 的有理函数，产生次数一的 $E^{(0)}\to\mathbf P^1$，与亏格一矛盾。因此 Kummer 扩张为三次。其所有赋值均被三整除，所以特征零下处处不分歧。第二个根没有把次数再乘三，因为 (9) 给
$$
v=\frac{x u^2}{a^2}.
$$
三个位于 $u=0$ 的点是核。直接微分 (9)，或使用 (6)，得到
$$
\boxed{u'=av^2,\qquad v'=-au^2,\qquad
\varphi^*\frac{dx}{2y}=\frac{du}{av^2}.}
\tag{11}
$$
这也核实了原点参数以及同源的可分性。

同源可以在同一个 $k$ 上精确识别。令
$$
\iota:\mathcal C\longrightarrow E^{(0)},\qquad
X=-\frac{a^2}{u+v},\quad
Y=c\delta\frac{u-v}{u+v}.
\tag{12}
$$
代入 $u^3+v^3=1$ 得 $Y^2=X^3+c^2$。该映射有有理逆：由 $X$ 恢复 $u+v=-a^2/X$，再由 $Y$ 恢复 $u-v$。故它是光滑射影曲线的同构。置
$$
T'=\iota(O')=(-a^2,-c\delta),\qquad
j=\iota-T'.
$$
$j$ 保原点，是椭圆曲线同构。由 (11)–(12) 直接算得
$$
j^*\frac{dX}{2Y}=-\frac1\delta\,\varphi^*\frac{dx}{2y}.
$$
同态 $[-\delta]\circ j$ 与 $\varphi$ 保相同原点、具有相同不变微分；特征零下差同态的微分为零便只能为零。因此
$$
\boxed{\varphi=[-\sqrt{-3}]\circ j,\qquad \deg\varphi=3.}
\tag{13}
$$
这里 $-\delta=-\omega(1-\omega)$ 为范数三的真实 CM 整数。

本篇的根与 R257 的四次根有不同的分歧情况：(10) 的除子各项均为三的倍数，而且其非平凡除子类准确给同源覆盖。并不是凭两条曲线同为 CM 就假定这层根可以通过同源实现。

## 4. 原 theta 对数的有理角参数方程

取实际角参数
$$
q=u^3=\frac{2c}{c-y},\qquad v^3=1-q.
\tag{14}
$$
它在原点为 $a^3z^3+\cdots$，不是旧 $\mathbf Q(i)$ 情形的四次参数。由 (11)，
$$
q'=3au^2v^2,\qquad
q''=6a^2uv(1-2q).
\tag{15}
$$
记 $Z_N=\log\theta_-^N$，其中 $N\ge1$ 固定。由 (8) 或前面的加法式，
$$
(\log\theta_-)'=\zeta+\frac{y+c}{x},\qquad
(\log\theta_-)''=a^2uv.
\tag{16}
$$
把 (15) 代入 (16)，便得完整有理方程
$$
\boxed{
q(1-q)Z_N''+\frac23(1-2q)Z_N'=\frac N9,
\quad Z_N(0)=0,\quad Z_N'(0)=\frac N6.
}
\tag{17}
$$
本节的撇号从 (17) 起指 $\partial_q$。微分方程在原点给唯一的 $q$ 正则解，所以 $Z_N$ 的全部系数都在 $\mathbf Q$，尽管使用过固定数域 (5)。更准确地，
$$
\boxed{
z_n:=[q^n]Z_N=\frac{N}{3n}\frac{(1/3)_n}{(2/3)_n},
\qquad
\frac{z_{n+1}}{z_n}=
\frac{n(3n+1)}{(n+1)(3n+2)}.
}
\tag{18}
$$
这由单项式公式
$$
\mathscr L_0(q^n)=n(n-1/3)q^{n-1}-n(n+1/3)q^n,
\quad
\mathscr L_0=q(1-q)\partial_q^2+\tfrac23(1-2q)\partial_q
\tag{19}
$$
逐项递推得到。

还保留负号/偶性的准确运输。由 (7) 有 $\theta_-(-z)=\theta_+(z)$；由 (9)，
$$
u(-z)=-u(z)/v(z),\quad v(-z)=1/v(z),\quad
q(-z)=q(z)/(q(z)-1).
\tag{20}
$$
所以 $\mu_6$ 的偶投影不能只在 (17) 中任意保留偶数 $q$ 次数；实际负号作用是 (20) 的 Möbius 变换，同时交换 theta 支。

## 5. 惰性首分母带及其完整三次齐次解

令
$$
p\equiv2\pmod3,\quad p\ge5,\quad p\nmid17N,
\qquad p=3r-1.
\tag{21}
$$
这些 $p$ 在新 CM 域中惰性。对 $1\le n<p$，(18) 中分母 $(2/3)_n$ 的首个 $p$ 因子在 $n=r$，分子 $(1/3)_n$ 的首个 $p$ 因子在 $n=2r$；在这个窗口各出现一次。因此
$$
v_p(z_n)=
\begin{cases}
-1,&r\le n<2r,\\
0,&1\le n<r\text{ 或 }2r\le n<p.
\end{cases}
\tag{22}
$$
这里排除了 $p\mid N$，其余显示小整数均为 $p$ 单位。式 (22) 不延伸到 $n=p$，该处还有 $1/n$ 的新分母。

令
$$
h_j=\frac{(2/3)_j}{j!(3j+1)},\qquad
h_+=\sum_{j=0}^{r-1}h_jq^j,\qquad a_0=pz_r\in\mathbf Z_p^\times.
$$
原坏带的完整首层是
$$
\boxed{p z_{r+j}\equiv a_0 h_j\pmod p
\qquad(0\le j<r).}
\tag{23}
$$
证明比较 (18) 在 $n=r+j$ 处的模 $p$ 比值与
$$
\frac{h_{j+1}}{h_j}
=\frac{(3j+2)(3j+1)}{3(j+1)(3j+4)}.
$$
两者相同，且首项已由 $a_0$ 固定。

这些 $h_j$ 来自 (11) 的同一个不变微分，不是另选的模型函数。准确地，
$$
h(q):=\frac{az}{q^{1/3}}
=\sum_{j\ge0}\frac{(2/3)_j}{j!(3j+1)}q^j,
\qquad h+3qh'=(1-q)^{-2/3}.
\tag{24}
$$
事实上 $az=\int_0^u (1-t^3)^{-2/3}dt$，展开即得 (24)。

置
$$
\mathscr L=q(1-q)\partial_q^2+(4/3-2q)\partial_q-2/9.
$$
链式法则给准确共轭
$$
\boxed{\partial_z^2(q^{1/3}V)
=9a^2u^2v\,\mathscr LV.}
\tag{25}
$$
故 $q^{-1/3}$、$h(q)$ 是其两个齐次解，且
$\mathscr L h_+\equiv0\pmod p$。后一式也可直接由各内项递推以及最高项
$-(r-2/3)(r-1/3)h_{r-1}\equiv0$ 核实。

## 6. 原余项的全部强迫与真实逆系数

定义原实际余项
$$
U_\theta=q^{-r}\{Z_N-[Z_N]_{<r}-(a_0/p)q^rh_+\}.
\tag{26}
$$
由 (22)–(23)，$U_\theta\bmod q^{2r-1}$ 全部整，且 $U_\theta(0)=0$。这里保留 $q^p$ 的窗口边界；不宣称无限余项整。

完整特征零共轭为
$$
\boxed{
q^{-r}\mathscr L_0(q^rV)=\mathscr LV+
p\left\{\tfrac23(1-q)V'+\frac r{3q}V-\frac{p+3}{9}V\right\}.
}
\tag{27}
$$
因此原 $U_\theta$ 满足 (27) 左侧算子作用后的准确非齐次方程，其右端是次数恰 $r-1$ 的整多项式 $\mathcal T_{p,r}$，所有系数为
$$
\boxed{
[q^j]\mathcal T_{p,r}=
\begin{cases}
\displaystyle
\frac{2a_0h_j(18j^2+6jp+30j+5p+11)}
{27(j+1)(3j+4)},&0\le j<r-1,\\[2mm]
\displaystyle\frac{2a_0(2r-1)h_{r-1}}3,&j=r-1.
\end{cases}}
\tag{28}
$$
特别最高系数是单位。

**证明。** 右端准确为
$$
q^{-r}\{N/9-\mathscr L_0[Z_N]_{<r}
-(a_0/p)\mathscr L_0(q^rh_+)\}.
$$
低于 $q^r$ 的项由 (18) 及 $a_0=pz_r$ 全消。对 $n=r+j$，内项是
$$
\frac{a_0}p\{n(n+1/3)h_j-(n+1)(n+2/3)h_{j+1}\},
$$
代入 $p=3r-1$ 和 $h$ 比值，得到 (28)。末项无 $h_r$，利用
$(2r-1)+1/3=2p/3$ 即得第二行。所有显示分母在给定范围均为单位。$\square$

在已付的整窗口约化，准确有
$$
\mathscr L\overline U_\theta=
\overline{\mathcal T}_{p,r}\pmod{q^{2r-2}}.
\tag{29}
$$
不能由 $\mathscr Lh_+=0$ 删除右边的最高单位强迫。

令 $A=a_0h_+$，取与原坏带一致的
$D=rA+qA'$。由 (24) 的低截断及模 $p$ 的二项式公式，
$$
\boxed{D\equiv\frac{a_0}3(1-q)^{r-1}\pmod p.}
\tag{30}
$$
在 $\mathbf F_p[[q]]$ 中，$v^3=1-q$、$v(0)=1$ 给完整恒等式
$$
(1-q)^{-(r-1)}=\frac{v(q)^2}{v(q^p)}.
$$
所以
$$
\boxed{D^{-1}\equiv\frac3{a_0}v(q)^2\pmod{(p,q^p)}.}
\tag{31}
$$
式 (31) 的根现在已经由 (9)–(13) 在固定未分歧同源上实现；不能在全局公式中删去分母 $v(q^p)$。相应的精确微分是
$$
\boxed{v^2dz=du/a.}
\tag{32}
$$

此外，根在真实 theta frame 中的清分母等式为
$$
\boxed{v^2\theta_-^N=\theta_+^2\theta_-^{N-2}
\qquad(N\ge2).}
\tag{33}
$$
它是等次数的全纯 theta 截面等式，完整保留由 $\theta_+^2\theta_-^{N-2}$ 指定的特征。没有把改变的特征丢弃，也没有把它冒称同一目标 Schwartz 线。

## 7. 可直接使用的结论与仍缺的原中央输入

(4) 已给一个新的固定合格秩候选；(8)–(13) 付清了真正的三次根、全部尺度、固定域与 CM 同源。其反对称参数不是旧四次参数，负号按 (20) 作用。
(17)–(31) 对该曲线的实际三等分 theta frame 给出了完整有理递推、首分母带和所有首余项强迫。逆系数的根可以通过 (33) 在等 theta 次数下转换，但特征也相应改变。

若下一步使用杨氏 theta 公式，必须先指定 (1) 的真实 Hecke 角色、十七处 nonsplit torus 的特征向量、二和三处的局部数据，以及完整普通或惰性中央转置。特别不能把 $\theta_-^N$ 任意选作目标截面，不能从 (28) 的单位直接推出其中央导数非零，也不能把 (33) 的不同特征全部当成原零来源。
本篇提供的是这些比较可用的真实同源和进位输入，尚未证明新曲线对无穷多个 $p$ 的 $\Sha[p^\infty]$ 有限。

## 精确证书

[脚本](../scripts/check-jzero-rank2-cubic-isogeny-and-first-carry.py) 逐项核实 (2) 和模十九群律、(9) 的两条微分、(12) 的曲线及尺度、(16)–(19) 的全部系数、(25) 的三个算子系数和 (27)–(31) 的一般参数恒等式；[输出](../scripts/check-jzero-rank2-cubic-isogeny-and-first-carry.json) 只包含有理或整系数计算。素数五、七、十九仅用于固定秩证书，没有进行 Sha 非零素数扫描。
