# R242 — 原第一次提升的修正仍保留一个共同因子

日期：2026-11-13。**状态：已证明。** 本篇在实际 $q=2$ 带上，把 R238 的首次提升方程中的修正空间由整个原 $E_d$ 缩小为 $F E_{d-e}$，其中 $F$ 是同一原核的共同高接触因子、$e=\deg F$。这个缩小不损失任何模 $p^2$ 提升。没有证明缩小后的障碍为零，没有由双中央消失推出新的深关系。

## 1. 同一原窗口与共同因子

固定
$$
p=4r-1\ge19,\qquad k=2r+s,\qquad 0\le s<r,
$$
$$
d<p,\qquad r-2>d(d-1),
\qquad V_d=\ker(j_{k,1}|_{\mathbf F_p[A,C]_{\le d}}).
\tag{1}
$$
原源为 $E_d=\mathbf Z_p[A,C]_{\le d}$，$C=B-A$；$L_k$ 与 $j_{k,1}$ 仍为 R233 的原加权前缀环和评价。假设 $V_d\ne0$。

R238 给唯一的低次高接触因子 $F$，并且
$$
e=\deg F\le d/2,\qquad F^2\mid P\quad(0\ne P\in V_d).
$$
记原图接触为
$$
h=v_\phi(F),\qquad \mu=v_\phi(F_C),
\qquad \phi(A)=-22A^2+O(A^3).
$$
对任意 $0\ne P_0\in V_d$，写
$$
P_0=F^mG,
\quad m\ge2,\quad F\nmid G,
\quad g=d-me\ge\deg G,
\quad z=v_\phi(G).
\tag{2}
$$
R238 的已付准确界是
$$
h>e(d-1),\quad \mu\le e(e-1),\quad z\le eg,
$$
$$
(m-1)h+\mu+z\ge r-2.
\tag{3}
$$
其中 $h$ 允许为无穷；$\mu,z$ 有限。式 (3) 的最后一项是同一个完整原第一带的 $j=1$ 条件。

## 2. 原 j=1 条件将接触进一步提高到 ed 之上

**引理 1。** 在 (1) 中，原共同因子满足
$$
\boxed{h>ed.}
\tag{4}
$$

**证明。** 若 $h\le ed$，由 (2)—(3)
$$
(m-1)h+\mu+z
\le(m-1)ed+e(e-1)+e(d-me).
$$
右侧不超过 $d(d-1)$，因为其与 $d(d-1)$ 的差准确为
$$
d(d-1)-\bigl[(m-1)ed+e(e-1)+e(d-me)\bigr]
=(m-1)e(e-1)+g(d-1)\ge0.
$$
这与 (3) 及 $r-2>d(d-1)$ 矛盾。$\square$

这里没有把 $F_C$ 或 $G$ 在原点的值当成单位；其实际接触阶已保留在 (3) 中。

## 3. 真实第一块上的除 p 余项

令 $J=J_{d,<k}:E_d\to L_k$ 为同一原完整归一矩阵。取任意整多项式提升 $\widetilde F,\widetilde G$，并记
$$
\widetilde P_0=\widetilde F^m\widetilde G.
\tag{5}
$$
由 $P_0\in V_d$，$J(\widetilde P_0)\in pL_k$。

在原第一块 $0\le n<r$，权 $e_n=0$，所以这些行就是实际未加权系数。原 $A(w),C(w)$ 在这个窗口全部整，$A(w)=w+O(w^2)$ 是严格整参数。其模 $p$ 图在 $A^r$ 之前准确为原 $\phi$。

因此在这个共同截断内，可以写
$$
\widetilde F(A(w),C(w))=f_0(w)+p f_1(w),
$$
$$
\widetilde G(A(w),C(w))=g_0(w)+p g_1(w),
\tag{6}
$$
其中选取的整系数代表满足
$$
\operatorname{ord}_w f_0\ge\min(h,r),\qquad
\operatorname{ord}_w g_0\ge\min(z,r).
$$
这只是给前 $r$ 个实际系数选模 $p$ 代表，不为原函数添加可调整的高阶系数。

因 $mh+z\ge r$，$f_0^mg_0$ 在第一块内准确为零。模 $p^2$ 的展开给
$$
\widetilde P_0/p
\equiv m f_0^{m-1}f_1g_0+f_0^mg_1\pmod p
\quad\text{在前 }r\text{ 个系数中}.
\tag{7}
$$
由 $z<h$，这份实际第一块余项的接触至少为
$$
\boxed{\quad
\min\{r,(m-1)h+z\}.
\quad}
\tag{8}
$$
若 $h\ge r$，则 $m\ge2$ 使 (7) 的整个第一块为零；(8) 仍成立。

这里只处理原 $n<r$ 的行，所以不存在删去一个非单位权、遗漏下一块或把原轴在 $A^r$ 以后继续当作实际图的问题。后两块仍由完整 $J$ 保留，不在 (7) 中替代。

## 4. 任何模 p² 提升的修正必须保留 F

**定理 1。** 设某个原次数至多 $d$ 的多项式
$$
P=\widetilde F^m\widetilde G+pR
$$
满足
$$
J(P)\in p^2L_k.
\tag{9}
$$
则
$$
\boxed{F\mid\overline R\quad\text{在 }\mathbf F_p[A,C]\text{ 中}.}
\tag{10}
$$

**证明。** (7)—(9) 说明 $\overline R$ 在原图上的接触至少为 (8)。由 (4)、$m\ge2$、$z\ge0$，以及
$r>d(d-1)+2\ge ed$，该接触严格大于 $ed$：
$$
v_\phi(\overline R)>ed.
\tag{11}
$$
若 $\overline R=0$，结论直接成立。否则若 $F\nmid\overline R$，则关于 $C$ 的 resultant 非零，且总次数界给
$$
\deg_A\operatorname{Res}_C(F,\overline R)
\le e\deg\overline R\le ed.
$$
无分母的 Bézout 恒等式代入原图，又由 (4)、(11) 给其消失阶严格大于 $ed$，矛盾。故 (10) 成立。$\square$

式 $r>d(d-1)+2\ge ed$ 使用 $d\ge2e$；在最小 $d=2,e=1$ 时右侧仍为严格界。定理并不依赖 R241 的 ODE 排除范围。

### 4.1. 不依赖特定的因子化提升

若只写 $P_0=F^2Q$ 并为 $Q$ 选择任意整提升，另一种按 (2) 因子化的提升与它之差是
$p\widetilde F^2Q_1$ 模 $p^2$。相应修正 $\overline R$ 的变化本身被 $F^2$ 整除。因此定理 1 对表示
$$
P=\widetilde F^2\widetilde Q+pR
\tag{12}
$$
仍然成立。改变 $\widetilde F$ 的整提升也只改变一个被 $F$ 整除的首次修正。

所以，**每个** 模 $p^2$ 原提升，都可在不损失次数的情况下写成
$$
\boxed{\quad
P\equiv\widetilde F^2\widetilde Q
       +p\widetilde F\widetilde H\pmod{p^2E_d},
\qquad \deg H\le d-e.
\quad}
\tag{13}
$$
这是同一原源中的因子保持结论，而不是只在目标环中除以一个可能为零因子的像。

## 5. 缩小后仍准确的首次障碍

定义实际较小源
$$
W=\{Q\in\mathbf F_p[A,C]_{\le d-2e}:F^2Q\in V_d\},
$$
以及同一目标中的原像
$$
S_F=j_{k,1}\bigl(F\,\mathbf F_p[A,C]_{\le d-e}\bigr)
\subset L_k/pL_k.
\tag{14}
$$
因 $j_{k,1}$ 为原环同态，$S_F$ 也等于
$j_{k,1}(F)\,j_{k,1}(E_{d-e}\bmod p)$。不能把后一因子换成整个目标环。

对 $Q\in W$，定义
$$
\boxed{\quad
\omega_F^{\mathrm{nor}}(Q)=
\overline{\frac{J(\widetilde F^2\widetilde Q)}p}
\pmod{S_F}
\quad\in(L_k/pL_k)/S_F.
\quad}
\tag{15}
$$
横线指先在整个原输出中除以 $p$，再模 $p$。除法合法来自 $Q\in W$，不逐项删除未付公共因子。

**定理 2。** (15) 与提升选择无关，是线性映射，且
$$
\boxed{\quad
\mathcal F_2(d)=F^2\ker\omega_F^{\mathrm{nor}}.
\quad}
\tag{16}
$$

**证明。** 改变 $F,Q$ 的整提升，乘积除以 $p$ 后的变化模 $p$ 为原多项式
$$
2FF_1Q+F^2Q_1\in F E_{d-e},
$$
所以 (15) 良定义；同一论证给线性。

若 (15) 为零，选 $H\in E_{d-e}\bmod p$ 使
$$
j_{k,1}(FH)=-\overline{J(\widetilde F^2\widetilde Q)/p}.
$$
(13) 的右侧即给原模 $p^2$ 提升。

反过来，任何提升都具有 (12) 的形式，定理 1 迫使 $\overline R\in F E_{d-e}$。因而它使 (15) 为零。这证明 (16)。$\square$

原 R238 的首次障碍商去整个 $j_{k,1}(E_d)$；这里改为严格指定的 $S_F$，同时保留完全相同的提升核。所有后两块行和原 carry 都仍在 (15) 的完整输出中。

## 6. 最小次数平方候选的具体后果

若 $d=2e$ 且 $V_d\ne0$，则 $F^2\mid V_d$ 立即给
$$
V_d=\mathbf F_p F^2.
$$
在这个情况下，全部首次问题是单个实际类
$\omega_F^{\mathrm{nor}}(1)$ 是否为零，修正只需在原 $E_e$ 中找。

若它为零，(13) 给
$$
\widetilde F^2+p\widetilde F\widetilde H
\equiv\left(\widetilde F+\frac p2\widetilde H\right)^2
\pmod{p^2E_{2e}}.
\tag{17}
$$
因此每个首次平方关系都有一个仍在原次数 $e$ 内的平方根提升。这里的结论是该根的**平方输出**属于 $p^2L_k$；不声称根的输出属于 $pL_k$。原有限目标含幂零元，最后这个推断一般不合法。

对于更大的 $d$，(13) 保证一个 $F$，没有证明保留第二个。能否强制第二个因子，或能否由双完整中央条件使 (15) 的实际核非零，仍需新的输入。

### 6.1. 第二个因子应作为变形后的因子读取

要求 (12) 中的固定修正 $\overline R$ 被 $F^2$ 整除，不是与提升选择无关的条件。把 $\widetilde F$ 换成 $\widetilde F+pU$，同一个多项式的 $H=\overline R/F$ 会改变为
$$
H-2UQ\pmod F.
$$
所以正确问题是：给定首次提升
$$
\widetilde F^2\widetilde Q+p\widetilde F\widetilde H,
$$
它是否可以写成一个仍保留重数二的原次数变形
$$
(\widetilde F+p\widetilde U)^2
 (\widetilde Q+p\widetilde V)\pmod{p^2E_d}.
$$

设 $F,Q$ 互素，$\deg Q=n$，并使用准确次数预算 $d=2e+n$。展开后得到充要条件
$$
\boxed{\quad
H=2QU+FV,
\qquad U\in\mathbf F_p[A,C]_{\le e},\quad
V\in\mathbf F_p[A,C]_{\le n}.
\quad}
\tag{18}
$$
这里 $H\in E_{e+n}\bmod p$。这个条件的有限次数障碍空间准确为
$$
\mathcal N_{F,Q}=
\frac{\mathbf F_p[A,C]_{\le e+n}}
 {2Q\,\mathbf F_p[A,C]_{\le e}
       +F\,\mathbf F_p[A,C]_{\le n}},
\qquad
\boxed{\dim\mathcal N_{F,Q}=en.}
\tag{19}
$$
证明考虑 (18) 的线性映射。若 $2QU+FV=0$，互素性给
$U=cF,V=-2cQ$，因为 $\deg U\le e$，故 $c$ 只能为常数；反之这些向量都在核内。所以映射核一维，余核维数为
$$
\binom{e+n+2}{2}-\binom{e+2}{2}-\binom{n+2}{2}+1=en.
$$
它也可以视为同次数齐次化后两个原平面曲线的完整交点障碍；计算保留可能在无穷远处的交点，不只取原点的局部商。

因此一般首次提升与保留一个变形后平方因子是两级条件。$n=0$ 时 (19) 为零，恢复 (17)；$n>0$ 时尚需支付这个实际的 $en$ 维类。若 $Q$ 也被 $F$ 整除，不能套互素性的维数式，应保留 (18) 的真实带次数像。

## 7. 双完整中央条件在这个 q=2 核上的实际作用

本节再加入原 $A,C$ 两个完整中央导数均为零的假设。仍是同一个 $q=2,k,d$，不引用 R201 中只在高 $q$ 范围证明的权理想结论。

令 $a=17pu_0\in\mathcal O^\times$，并记原整轴的中央向量
$$
v_1=([y^r]f,[y^r]c),\qquad
v_2=([y^{2r}]f,[y^{2r}]c).
$$
R203 的原中央递推给实际整向量 $t_1,t_2$，满足
$$
v_1=pt_1,\qquad v_2=at_1+2pt_2.
\tag{20}
$$
删去这两个实际中央轴项得到 $(f^\circ,c^\circ)$，并用原 $a$ 和 R199 的同一准确第一带公式定义 $J^\circ$。这个比较只用于定位原中央条件的有限精度作用，不把比较轴当成另一条全局 theta 曲线。

### 7.1. 第一提升障碍准确不变

对原 $P\in E_d$，R199 的前三块公式直接给
$$
J-J^\circ\in p^2\operatorname{Hom}(E_d,L_k).
\tag{21}
$$
更准确地，记 $D=D_{t_1}$，模 $p^3$ 的差为
$$
\begin{aligned}
(J-J^\circ)_l(P)&=0 &&(0\le l<r),\\
\frac{(J-J^\circ)_{r+l}(P)}{p^2}
&\equiv[y^l]DP(f,c)\pmod p &&(0\le l<r),\\
\frac{(J-J^\circ)_{2r+l}(P)}{p^2}
&\equiv a[y^l]D(\mathcal E+1)P(f,c)\pmod p
&&(0\le l<s).
\end{aligned}
\tag{22}
$$
这些式子可直接核对：第一块完全不读中央项；第二块只读 $pD_{v_1}P$；第三块模 $p^3$ 只保留
$p^2D_{v_2}P+paD_{v_1}\mathcal EP$。代入 (20) 得 (22)。所有二次轴扰动至少含四个 $p$ 因子，下一角向进位在此也至少属于 $p^3$。因此这里没有使用高 $q$ 假设。

由 (21)，$J,J^\circ$ 的原模 $p$、模 $p^2$ 核相同，$S_F$ 相同，且 (15) 中除以 $p$ 后的差仍被 $p$ 整除。因此
$$
\boxed{\omega_F^{\mathrm{nor}}(J)
=\omega_F^{\mathrm{nor}}(J^\circ).}
\tag{23}
$$
这是两个实际有限映射的相等；它没有把任一映射的值证明为零。

### 7.2. 新因子保持结论支付真实 pair 的前两行

取共有的原模 $p^2$ 核向量 $P$。由定理 1，可以选择表示
$$
P=G+p\widetilde F\widetilde H+p^2S,
\qquad G=\widetilde F^2\widetilde Q.
\tag{24}
$$
因 $h>ed\ge2$，$F$ 没有常数项和原 $A$ 项。选择同样没有这两项的整提升后，$\widetilde F$ 的原最低角权至少为二，$G$ 的至少为四，$\widetilde F\widetilde H$ 的至少为二。原 Euler 算子 $\mathcal E=A\partial_A+C\partial_C$ 保持这些角权。

记
$$
g_j(y)=(\mathcal E^j\overline G)(f(y),c(y))\in\mathbf F_p[[y]].
$$
原模 $p$ 核条件已经给 $g_0,g_1\in y^r\mathbf F_p[[y]]$、$g_2\in y^s\mathbf F_p[[y]]$。
现在把 (24) 的 $P/p$ 代入同一原第一带公式，在第一个完整块的角 $l=0,1$ 处读取。所有直接来自 $\mathcal E^jG$ 的低角项准确为零；所有来自 $\mathcal E^j(FH)$ 的这些项模 $p$ 也为零。因此这两条真实行进一步给
$[y^r]g_0=[y^{r+1}]g_0=0$。

对部分块同样读取已包含的 $l=0,1$ 行，得到 $g_1$ 的前 $\min(s,2)$ 个新系数为零。准确地，
$$
\boxed{\quad
g_0\in y^{r+2}\mathbf F_p[[y]],\qquad
g_1\in y^{r+\min(s,2)}\mathbf F_p[[y]],\qquad
g_2\in y^s\mathbf F_p[[y]].
\quad}
\tag{25}
$$
这里用的是 (24) 中**已由原模 $p^2$ 条件付出的因子保持**，不是给不同 summand 分别假设完整前缀。

### 7.3. 第三层差至多支撑在最后两行

写
$$
W=f c'-c f'=v_0y^2+\cdots,\qquad
K_t=\frac{(t_1)_A c'-(t_1)_C f'}{W},\qquad
L_t=\frac{(t_1)_C f-(t_1)_A c}{W}.
$$
则 $\operatorname{ord}K_t\ge-2$、$\operatorname{ord}L_t\ge-1$。原链式法则给
$$
(D\mathcal E^j\overline G)(f,c)=K_tg_{j+1}+L_tg_j'.
\tag{26}
$$
由 (25)，第一完整块的 (22) 余差具有角阶至少
$r-2+\min(s,2)$。部分块的余差具有角阶至少 $s-2$；另一方面，原 $D(\mathcal E+1)G$ 的角权至少为二，所以它实际具有角阶至少 $\max(2,s-2)$。

因此，对每个共有的 $P\in K_2(k)$，准确有
$$
\boxed{\quad
\frac{(J-J^\circ)P}{p^2}\bmod p
\text{ 只支撑于原行 }\{k-2,k-1\}.
\quad}
\tag{27}
$$
更细地，可能保留的行数至多为
$$
b_s=\begin{cases}
2,&s=0,\\
1,&s=1,\\
0,&s=2,\\
1,&s=3,\\
2,&s\ge4.
\end{cases}
\tag{28}
$$
例如 $s=1$ 时只可能是 $k-2$，$s=3$ 时只可能是 $k-1$。这些是支撑上界，不声称相应行必非零。

R233 的提升层现在给直接的列核后果。$\mathcal F_1,\mathcal F_2$ 对两矩阵相同；一次除幂像 $\mathcal V_1$ 也相同，因为 (21) 除以一次 $p$ 后仍模 $p$ 为零。把两份第二 Bockstein 都看成从同一个 $\mathcal F_2$ 到共同环境商 $(L_k/pL_k)/\mathcal V_1$ 的映射；不要求它们在该环境商中的像相同。由 (27)，它们相差一个秩至多 $b_s$ 的映射，所以
$$
\boxed{\quad
|\dim\mathcal F_3(J)-\dim\mathcal F_3(J^\circ)|\le b_s,
\qquad
|B_3(J)-B_3(J^\circ)|\le b_s.
\quad}
\tag{29}
$$
$s=2$ 时第三层的核本身相同。这一结论只比较原 $q=2$ 同一窗口中的有限源核，没有把第三层的控制无证迭代到更高精度。

## 8. 当前连接到主目标的准确位置

本篇给出的是第一次提升的实际缩小方程 (15)，不只是对可能次数的排除。它可以直接用 R224 的原径向系数、R233 的加权乘法，在同一个 $k$ 上计算。

原中央双行消失目前尚未证明使这个类为零。§7 已把现有传播式对这个核的实际作用付出：首次障碍不变，第三层只留下至多两条尾行。尤其 $S_F$ 是原有限次数像；把它放大为 $j(F)\cdot(L_k/pL_k)$，或仅在形式局部环里解修正，都可能遗漏原次数障碍，不能支付 R223 的深关系输入。

依赖：R196 的原第一带图；R199 的原准确指数式；R203 的原中央整递推；R233 的原环和提升层；R238 的共同高接触因子及准确 Hasse 接触公式。本篇没有新增目标素数扫描，也没有用数值结果替代 (16)。
