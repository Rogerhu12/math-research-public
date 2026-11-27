# R1016 — 单一特征零平坦 trace 与原中央导数的完整 L_p 精度比较

日期：2026-11-27 UTC。**已证明。** 对整个原22维
$\mathcal V_{130}$，本篇构造一个单一、显示的特征零平坦权。
在原 $H\le L_p$ 长窗内，它把整个来源准确送到同一个
degree10 theta frame 上的亚纯来源；全部低系数先在特征零精确相等，
再用统一的完整 Hurwitz 尾得到中央导数模 $p^{H+1}$ 的比较。
因此不必把每个低项的高精度作为另一个未下推的来源保留。

下层来源的二挠极随 $N=H(p+1)$ 增长，维数与分母阶明确写在下面。
它不是固定十维 $L(10O)$ 的全纯来源，也不是新增的 canonical 算术零。
原 $\mathcal K$ 的受迫零与 $\mathcal C_{130}$ 的 old 对数非零
现在可以在这两个单一、同框架的真实 Tate 输入中检测。

## 1. 原域、长窗及特征零权

取

$$
E_1:y^2=x^3+1,\quad X=x^3,\quad
\pi=(7+\delta)/2,\quad \delta^2=-3,\quad
p=6s-1>13^3.
\tag{1}
$$

保持原 $\omega_E=dz=dx/(2y)$、sigma、$c=[z^{p+1}]\log(\sigma/z)$
及 $v_p(c)=-1$。令

$$
1\le H\le L_p,\qquad N=H(p+1)=6Hs,\qquad
a=N+1,\quad k=N/6,\quad e=a+k=\frac{7N}{6}+1.
\tag{2}
$$

R1013 已证明在此范围 $H\le(p+1)/6$。
仍取原整来源

$$
f=\sigma^{130}R_f,\qquad
R_f=x^2P_f(X),\quad \deg P_f\le21,\quad
f\in\mathcal V_{130,\mathcal O}.
\tag{3}
$$

这里允许非零质量；$\mathcal K,\mathcal C_{130}$ 及
R1012 的全部实际 principal 伴线都在所用好位的这个整格内。

采用 R1013 的同一函数和同一有限多项式

$$
v_\pi=\frac{R_\pi(X)}{(X+1)^2},\qquad
R_\pi=X^2+(2+6\delta)X+(40+24\delta)/13,
$$

$$
B_{a,k}(T)=\sum_{j=0}^{k}(-1)^j
  \binom{a+j-1}{j}(T-1)^j,\qquad
\boxed{V_{N,\pi}=v_\pi^{N+1}B_{N+1,N/6}(v_\pi).}
\tag{4}
$$

本篇(4)是在特征零定义的原有理函数，**没有取其 $p$ 次幂**。
全部系数是显示的整数二项式与原 $R_\pi$ 的系数。
因为 $T^aB_{a,k}(T)=1+O((T-1)^{k+1})$，有

$$
\boxed{\begin{aligned}
V_{N,\pi}&=1+O(z^{N+6}) &&\text{at }O,\\
\operatorname{ord}_T V_{N,\pi}&=N+1
&& (0\ne T\in E[\pi]),\\
\operatorname{pole}_T V_{N,\pi}&=4e
&& (T\in E[2]\setminus O).
\end{aligned}}
\tag{5}
$$

此外没有极。核处首系数含
$B_{a,k}(0)=\binom{a+k}{k}\ne0$，所以(5)在特征零是准确阶。
这枚二项式在某些 $p$ 处可以不是单位；本篇不假定其单位性。
约化后核零阶只会增加，所有后继极帽均用上界，故不受影响。

## 2. 单一完整 trace 和整个原 theta frame

定义未平均 trace

$$
\boxed{
A_{N,\pi}(f)=\pi^{-10}\operatorname{Tr}_{[\pi]}
       \left(V_{N,\pi}\frac{R_f}{R_\pi^{10}}\right),
\qquad
h_{N,\pi}(f)=\sigma^{10}A_{N,\pi}(f).
}
\tag{6}
$$

这是同一 $N$ 对全部原来源的线性算子。
所有13个纤维点和原 Miller 相位均保留。
由原 sigma division

$$
\sigma(\pi z)=\pi\sigma(z)^{13}R_\pi(X(z)),
\tag{7}
$$

及 R1012 的完整 Miller 平移 $T_T$，整个特征零函数满足

$$
\boxed{
h_{N,\pi}(f)(\pi z)
=\sum_{T\in E[\pi]}
 V_{N,\pi}(P(z)+T)\,T_Tf(z).
}
\tag{8}
$$

证明中每个 $R_f/R_\pi^{10}$ 等于
$\pi^{10}f/\sigma(\pi z)^{10}$；
这与(6)的 $\pi^{-10}$ 准确相消。
所以(8)没有额外13或 $\pi^{10}$，也没有将一个 Miller 提升
换成未规范的普通平移。

$T=0$ 项与 $f$ 的差由(5)从 $N+6$ 阶起；
其余12项均从 $N+1$ 阶起，因为 $T_Tf$ 是完整全纯 theta 截面。
因此

$$
\boxed{
h_{N,\pi}(f)(\pi z)-f(z)=O(z^{N+1}).
}
\tag{9}
$$

两边都是 principal，故实际还可将右边加强为 $O(z^{N+6})$。
本篇仅需(9)。它是特征零的完整系数身份，不只是一条模 $p$
同余；特别同时保留质量及所有低于 $N$ 的非 diagonal 系数。

## 3. 所有增长极、明确整基与完整分母

令

$$
\mathcal D_2=E[2]\setminus O,\qquad
\boxed{M=2e=\frac{7N}{3}+2.}
\tag{10}
$$

在上游，$V_{N,\pi}R_f/R_\pi^{10}$ 在非零 $\pi$ 核处的零阶
至少 $N-9>0$，在 $O$ 的极阶至多10，在每个二挠点的极阶至多 $4e$。
$[\pi]$ 在本篇所有剩余特征上为 étale，且置换三个二挠点。
所以

$$
\operatorname{div}_\infty A_{N,\pi}
\le10(O)+4e\mathcal D_2.
\tag{11}
$$

没有其它极，尤其没有未列出的十三核极。

原 $\mu_6$ 角色使 $A_{N,\pi}/x^2$ 是 $X$ 的有理函数，
且在 $x=0$ 没有额外极。由(11)得整个表示

$$
\boxed{
A_{N,\pi}(f)
=\frac{x^2P_{N,\pi,f}(X)}{(X+1)^M},
\qquad
\deg P_{N,\pi,f}\le M+1.
}
\tag{12}
$$

因此相应 principal 空间维数至多 $M+2$，随 $N$ 增长；
本篇没有把它称为固定十维来源。
式(12)是指定 theta frame 上的亚纯函数，不改变(6)的定义。

### 3.1 系数确在原好位整环

在(4)展开后，$V_{N,\pi}R_f/R_\pi^{10}$ 的每一项为

$$
(-1)^j\binom{N+j}{j}
\frac{R_f R_\pi^{N-9}
      (R_\pi-(X+1)^2)^j}
     {(X+1)^{2(N+1+j)}}.
\tag{13}
$$

所有分子系数在 $\mathcal O$，没有 $R_\pi$ 分母；
$\pi$ 和13在本篇均为单位。故上游函数是
$10O+4e\mathcal D_2$ 允许极之外的整正则函数，没有垂直极。

原好约化模型上的有限 étale trace 保持整性；
在每个目标局部环，它就是有限自由代数中乘法的整矩阵迹。
所以(11)也在整模型上成立。
乘 $(X+1)^M$、再除去角色强迫的 $x^2$ 后，得到整个仿射曲线上的整正则函数。
其 $\mu_6$ 不变量环是 $\mathcal O[X]$（$6$ 为单位），故

$$
\boxed{P_{N,\pi,f}\in\mathcal O[X].}
\tag{14}
$$

这逐式付了(12)的整基，没有借一个可能含 $p$ 分母的坐标求解器。
在固定数域上只需原来源分母与 $2,3,13$；
增长的二项式和 $M$ 没有增加垂直分母。
实际求值可用 R1012(42)–(44)的完整13维有理余式，
将其中的 $W^p$ 换成显示的 $V_{N,\pi}$。该 trace 身份本来对任意有理乘子成立，
原 $\mathsf A_\pi^2$ 的完整消去也保持。

### 3.2 增长成本没有被删去

$e=7N/6+1$、$M=7N/3+2$ 是本篇真实成本。
本篇只使用一个确定的 $P_{N,\pi,f}$，不把 $M+2$ 维空间的任意元素
都宣称为受迫中央零。若另作全位估计，其复范数／系数高度也须计算；
不能把这个随 $p$ 变化的输入当作原固定曲线的一条固定低高度来源。

## 4. 与 M 无关的完整 Hurwitz 界和真实 Tate 定义

沿 R602/R614 记

$$
w=z^6,\qquad W_0=z^2x,\qquad
U_\sigma=\sigma^\circ/z,\qquad
\sigma^\circ=\sigma e^{-cz^{p+1}}.
\tag{15}
$$

$W_0,U_\sigma$ 及所需单位逆均属于原整 Hurwitz 代数，
且在每个原严格内闭盘 $R<R_*=p^{-1/[6(p-1)]}$ 上范数为一。
原 $w<s(p-1)$ 窗口内的系数全整。

(12)第 $j$ 个整基的整个 degree10 Gaussian 级数准确为

$$
\boxed{
(\sigma^\circ)^{10}\frac{x^2X^j}{(X+1)^M}
=w^{M+1-j}U_\sigma^{10}
 W_0^{\,2+3j-3M}
 (1+wW_0^{-3})^{-M},
\quad0\le j\le M+1.
}
\tag{16}
$$

所有 $w$ 幂非负；$W_0$ 的指数可为负，但它是指定的单位。
$-M$ 是整数，因此最后一个负整数幂由整二项式组成；
不能把它当成一个需要除以 $M!$ 的新展开。
由整 Hurwitz 代数对乘法、单位逆及整数幂的封闭性，结合(14)，有

$$
\boxed{
G_{10,h}:=e^{-10cz^{p+1}}h_{N,\pi}(f)
\in\mathscr H_{\mathcal O},\qquad
\|G_{10,h}\|_R\le1.
}
\tag{17}
$$

这里的常数独立于 $M,N,H$。
非 Archimedean 范数取最大值，不按 $M+2$ 个项求和收费。
(16)同时给完整整系数窗，而不是只给抽象 Hurwitz 下界。

令 $d=p+1$，定义真实 Tate 函数

$$
\boxed{
J_{10,h}(v)=
\sum_{\ell\ge0}(10c)^{-\ell}
 [z^{d\ell}]G_{10,h}\,(v)_\ell.
}
\tag{18}
$$

它在与原来源相同的严格开盘上收敛，且
$J_{10,h}(0)=m_0(f)$。其每个导数项满足

$$
v_p\!\left((\ell-1)!(10c)^{-\ell}
               [z^{d\ell}]G_{10,h}\right)
\ge \ell-v_p((\ell s)!)+v_p((\ell-1)!).
\tag{19}
$$

所以这是一个完整有定义的中央导数
$j_{10,h}=J_{10,h}'(0)$。
此处只使用形式解析来源，未给这个亚纯 frame 指定新的 Hecke／Selmer 解释。

## 5. 原 frame、两个 Gaussian 和全精度中央比较

令

$$
f_N^\pi(z)=h_{N,\pi}(f)(\pi z),\qquad
q_\pi=\pi^{p+1}/13\in1+p\mathcal O,\qquad
\gamma_\pi=10c(\pi^{p+1}-13)\in\mathcal O.
\tag{20}
$$

整个 degree130 Gaussian 满足

$$
e^{-130cz^{p+1}}f_N^\pi(z)
=e^{\gamma_\pi z^{p+1}}G_{10,h}(\pi z).
\tag{21}
$$

原单位 $\pi$ 保 Hurwitz 整性及盘范数。
$\gamma_\pi w^s$ 的零常数指数仍属同一整 Hurwitz 代数，
在原严格盘上指数及逆均为范数一。
因此 $f_N^\pi$ 的原 degree130 Newton 级数同样真实收敛。

对每个整数 $n\ge0$，完整系数插值给

$$
J_{130,f_N^\pi}(n)
=n!(130c)^{-n}[z^{dn}]h_{N,\pi}(f)(\pi z)
=q_\pi^n J_{10,h}(n).
$$

两边均为同一 Tate 域内的函数，非负整数稠密，故

$$
\boxed{
J_{130,f_N^\pi}(v)=q_\pi^vJ_{10,h}(v),\qquad
j_{130,f_N^\pi}=j_{10,h}+m_0(f)\log_pq_\pi.
}
\tag{22}
$$

所有 $\pi$、13及质量项都来自真实 frame。
质量一时不得省掉最后的对数。

另一方面，(9)使
$D_N=f-f_N^\pi$ 的原 Gaussian 系数在整个 $z\le N$ 前缀中准确为零。
因此其 Newton 导数前 $H$ 项是特征零的零。
下面核其全部剩余尾，不能只把有限插值当作导数比较。

取 $h_0=(p-1)/2$。对 $H<\ell\le h_0$，
$\ell s<s(p-1)$，(16)和原来源整窗给系数全整；
(21)的指数只用 $j\le\ell<p$，所有 $j!$ 均为单位。
所以第 $\ell$ 个导数项含 $p^\ell$，至少含 $p^{H+1}$。

对全部 $\ell>h_0$，由共同 Hurwitz 界，

$$
\begin{aligned}
v_p(\text{第 }\ell\text{ 个导数项})
&\ge \ell-v_p((\ell s)!)+v_p((\ell-1)!)\\
&\ge\frac{\ell(5p-7)}{6(p-1)}
>H+1.
\end{aligned}
\tag{23}
$$

在首端点 $\ell=(p+1)/2$，最后一式由
$H\le(p+1)/6$ 归结为 $3p^2-14p+7>0$；
随后随 $\ell$ 增长。由此支付无限尾，得到本篇的全精度身份

$$
\boxed{
j_f-j_{10,h_{N,\pi}(f)}
-m_0(f)\log_pq_\pi
\in p^{H+1}\mathcal O.
}
\tag{24}
$$

若按原 $\mathfrak a/p$ 归一，则误差准确属于 $p^H\mathcal O$。
因此(24)不再只替换第 $H$ 项的模 $p$ 值：
所有低项的真实高精度已经同时进入同一个 $h_{N,\pi}(f)$。

## 6. 原 P10 和整个小边界仍有严格极帽

若继续使用 R1013 的指定有限 $P_{10}$ 及原 $Z$，
对 $0\le b<p$ 定义

$$
\eta_{N,b}=Z^{-b-1}P_{10}A_{N,\pi}(f)\omega_E.
\tag{25}
$$

R1013(22)的原 $Z^p$ 因子仍消去其它 $Z=0$ 点。
本篇的全部真实极帽为

$$
\boxed{\begin{aligned}
\operatorname{pole}_O\eta_{N,b}&\le b+1\le p,\\
\operatorname{pole}_{\mathcal D_2}\eta_{N,b}
&\le d_{N,b}
=p^3-p^2+(8-b)p+4e+1<p^3.
\end{aligned}}
\tag{26}
$$

最后一个严格不等式由
$4e\le7(p+1)^2/9+4$ 得到：
$d_{N,b}-p^3\le(-2p^2+86p+52)/9<0$。
没有因(4)不是 $p$ 次权而漏掉二挠的增长极。

所以 R1013 的六种小边界仍完整适用，包括原点质量、二挠
$\beta_1,\beta_2$ 的负号以及 $b\equiv1$ 的全纯项。
其两 exact 构造也保持。令

$$
d_1=p^2-p+9-b+\left\lfloor\frac{4e}{p}\right\rfloor,
\qquad \epsilon_b=b\bmod2\in\{0,1\}.
\tag{27}
$$

这是第一 Cartier 的形式帽；若奇偶不符，再取不超过它的实际
$b+1$ 同奇偶帽。精确的有理部分上界为

$$
\boxed{\begin{aligned}
\deg_1V_0
&\le\frac{p(p-1)}2+
 \left\lfloor
 \frac{8-b+\lfloor4e/p\rfloor+\epsilon_b}{2}
 \right\rfloor,\\
\deg_1V_1&\le\frac{p-1}{2}.
\end{aligned}}
\tag{28}
$$

原 $a_0Z,a_1Z$、完整 Cartier 截面及原点读取仍按 R1013(34)–(38)，
不以无权的两个导数替代。这里没有把下层增长空间的维数计作新增深核。

## 7. 同一实际 old 检出深度与双支质量

对 $\bar\pi$ 使用原共轭权，重复上述全部构造，得到
$h_{N,\bar\pi}(f)$。这不是将两个 target 函数认作相同。
将(24)逐支相减，得到对同一原 $f$ 的真实比较

$$
\boxed{
j_{10,h_{N,\pi}(f)}
-j_{10,h_{N,\bar\pi}(f)}
\equiv
-m_0(f)(p+1)\log_p(\pi/\bar\pi)
\pmod{p^{H+1}}.
}
\tag{29}
$$

特别同一个质量一伴线在两 target frame 上并不会给出相同导数；
其差已经由(29)准确支付。质量零时，两完整 target 导数在该精度内相同。

在原两 canonical 坏假设下，取 $H=L_p$。R1005 与 R1000 给

$$
j_{\mathcal K}=0,\qquad
j_{\mathcal C_{130}}
=-\frac{\delta(p+1)}{112}\log_p(\pi/\bar\pi),\qquad
1\le v_p\log_p(\pi/\bar\pi)\le H.
\tag{30}
$$

两来源质量均为零，故(24)得到两个**单一**真实 Tate 输入的检测

$$
\boxed{\begin{aligned}
j_{10,h_{N,\pi}(\mathcal K)}&\in p^{H+1}\mathcal O,\\
j_{10,h_{N,\pi}(\mathcal C_{130})}
&\equiv-\frac{\delta(p+1)}{112}
 \log_p(\pi/\bar\pi)\not\equiv0
 \pmod{p^{H+1}}.
\end{aligned}}
\tag{31}
$$

第二个值的赋值准确等于原对数赋值；$\bar\pi$ 支同样如此。
这用的是原实际 fixed-source 导数，不是有限扫描或假设的最低位单位性。

R1012 的两质量匹配来源
$\mathcal R_\pi=\Psi_{571220}-L_\pi$、
$\mathcal R_{\bar\pi}=\Psi_{571220}-L_{\bar\pi}$
也可直接消费(24)。它们质量均零且
$\mathcal R_\pi-\mathcal R_{\bar\pi}=3\Delta_{125}/4$，所以

$$
\boxed{
j_{10,h_{N,\pi}(\mathcal R_\pi)}
-j_{10,h_{N,\bar\pi}(\mathcal R_{\bar\pi})}
\equiv\frac34(p+1)\log_p(\pi/\bar\pi)
\not\equiv0\pmod{p^{H+1}}.
}
\tag{32}
$$

若先分别拆出共享的质量一 $\Psi_{571220}$，
必须保(29)；该项不会在不同 target frame 中免费相消。
整个有限字的投影与配对按 R1013(60)–(62)保持：
本篇 $V_{N,\pi}$ 也是 principal，故整个 trace 与几何投影交换，
但单个 Fourier 权与投影仍不交换。

## 8. 范围与继续消费

(24)把整个原 $L_p$ 精度送入一个明确的亚纯 degree10 frame，
(31)–(32)给已付 old 对数在这些实际输入中的非零检出。
它没有从 canonical 坏条件给每个字、每个
$h_{N,\pi}(L_\pi)$ 或 $h_{N,\pi}(\Psi_{571220})$ 另赋零。
后续仍须对这些同一带权输入建立真实不相容关系，
不能把增长极、$M+2$ 维空间或两 exact 当作已消去。

全部结论由显示权、原完整 isogeny／Miller frame、整 trace、
Hurwitz 代数与原 Newton 尾证明，无数学执行或素数扫描。
所用固定坏素数已包含于 $p\le13^3$；增长的整数二项式允许被 $p$ 整除，
本篇从未反演它们。
依赖：R602/R614（统一 Hurwitz 与原整窗）；
R1000（$L_p$）；R1005（原 $\mathcal K,\mathcal C_{130}$）；
R1012（全字及完整有理 trace）；R1013（全22、全部小边界与两 exact）。


## 9. 原权的两个 Frobenius gauge 与显示的窄余带

本节只约化上文同一个(4)的 $V_{N,\pi}$。
没有将它换成另一个极帽更小的 Padé 权。
记

$$
\xi=v_\pi-1,\qquad
k=Hs=qp+t,\quad0\le t<p,\qquad
q=\lfloor H/6\rfloor.
\tag{33}
$$

最后一个等式由 $H<p$ 及 $s=(p+1)/6$ 得到。
若 $H=6q+r$、$0\le r<6$，则 $t=q+rs$。
以下多项式都在 $\mathbf F_p[\xi]$ 内，所有整数二项式按原值约化。
令

$$
\begin{aligned}
Q_k(\xi)&=B_{Hp+H+1,k}(1+\xi),\\
S_q(\xi)&=\sum_{j=0}^{q}(-1)^j
             \binom{H+j-1}{j}\xi^j,\\
C_{H,q}&=\binom{H+q}{q}\in\mathbf F_p^\times.
\end{aligned}
\tag{34}
$$

$H+q<p$，所以最后一个量确为单位；并且
$S_q(-1)=C_{H,q}$。

### 9.1 唯一的实际余带及其完整系数

原 $a=Hp+H+1$ 给

$$
(1+\xi)^{H+1}Q_k(\xi)
\equiv (1+\xi)^{-Hp}
=S_\infty(\xi)^p\pmod{\xi^{k+1}},
$$

其中 $S_\infty=(1+\xi)^{-H}$。
右边到次数 $k$ 的完整截断恰是 $S_q(\xi)^p$。
所以

$$
\boxed{
E_{H,k}(\xi)=
\frac{(1+\xi)^{H+1}Q_k(\xi)-S_q(\xi)^p}
     {\xi^{k+1}}
\in\mathbf F_p[\xi],\qquad \deg E_{H,k}\le H.
}
\tag{35}
$$

这里除以 $\xi^{k+1}$ 已由整条恒等式支付，不是除以 $p$，
也没有增加未定的余系数。
它还有完全显示的闭式

$$
\boxed{
E_{H,k}(\xi)=(-1)^k C_{H,q}
 \sum_{\ell=0}^{H}\binom{k+\ell}{\ell}(1+\xi)^\ell.
}
\tag{36}
$$

证明：在 $\xi=-1$ 的参数 $r=1+\xi$ 中，
$S_q(\xi)^p=C_{H,q}+O(r^p)$；而 $H<p$。
由(35)模 $r^{H+1}$ 得
$E_{H,k}\equiv-C_{H,q}\xi^{-k-1}$。
把 $\xi=-1+r$ 代入并截到次数 $H$，就得到(36)；
两边次数至多 $H$，所以是整个多项式身份。
特别

$$
\boxed{E_{H,k}(-1)=(-1)^k C_{H,q}\ne0.}
\tag{37}
$$

因此这个余带不是可以从核处删掉的误差。

### 9.2 原 V_N 的完整两项返回

定义两个低次数的实际有理函数

$$
G_0=(1+\xi)^H S_q(\xi),\qquad
G_1=(1+\xi)^H\xi^q,\qquad
B_{H,k}=\xi^{t+1}E_{H,k}(\xi).
\tag{38}
$$

将(35)乘 $(1+\xi)^{Hp}$，得到同一个原权的完整约化

$$
\boxed{\overline{V}_{N,\pi}=G_0^p+G_1^p B_{H,k}.}
\tag{39}
$$

$G_0,G_1$ 的 $\xi$ 次数至多 $H+q$；
增长的 $N$ 没有留成一个任意高次数权。
但(39)的第二项仍是完整的原有理函数，不能只保留 $G_0^p$。

更具体地有两种准确情形。

- 若 $t+H+1<p$，则
  $\deg E_{H,k}=H$、
  $\deg B_{H,k}=t+H+1<p$。
  $B_{H,k}$ 仅有从 $\xi^{t+1}$ 到 $\xi^{t+H+1}$ 的至多 $H+1$ 个槽，
  全部系数已由(36)指定。
- 若 $t+H+1\ge p$，置 $d=p-t-1\le H$。
  Lucas 二项式恒等式逐项给
  $E_{H,k}=(-1)^{k+d}C_{H,q}\xi^d$，所以
  $B_{H,k}=(-1)^qC_{H,q}\xi^p$。
  两项可完全合成

$$
\boxed{
\overline V_{N,\pi}
=\left((1+\xi)^{H+1}
       B_{H+1,q}(1+\xi)\right)^p
\quad(t+H+1\ge p).
}
\tag{40}
$$

这恰是 R1013 的 $W_{H,+}^p$。
证明最后一步用
$(1+\xi)B_{H+1,q}(1+\xi)
=S_q(\xi)+(-1)^qC_{H,q}\xi^{q+1}$；
没有更换原权在特征零中的定义。

在第一种情形，$\xi$ 作为原曲线上的函数 degree 为12：
它的三个二挠极各为四阶，且没有约分。
因为 $p>12$，$\xi$ 不是函数域的 $p$ 次幂，
所以 $1,\xi,\ldots,\xi^{p-1}$ 是一个真实 $p$ 基。
上述窄带确在这一完整 $p$ 基内。
若使用该基，仍须保
$\omega_E=(D\xi)^{-1}d\xi$ 和原 $Z,P_{10}$；
不能把这个基的坐标直接认成原 $Z$ 的 Taylor 系数。

### 9.3 全 trace 和第一 Cartier，保原两个 frame

令 $\mathfrak f=R_f/R_\pi^{10}$。
对上文实际 $A_{N,\pi}$ 的约化，(39)直接给

$$
\boxed{
\overline A_{N,\pi}
=\pi^{-10}\operatorname{Tr}_{[\pi]}(G_0^p\mathfrak f)
+\pi^{-10}\operatorname{Tr}_{[\pi]}(G_1^pB_{H,k}\mathfrak f).
}
\tag{41}
$$

所有13项、$\pi^{-10}$、原 Miller 和全部非 principal 字仍在里面。
例如对原

$$
\eta_{\pi,b}=Z_\pi^{-b-1}\mathscr P_\pi R_f\omega_E
$$

及(25)的 $\eta_{N,b}$，整条第一 Cartier 身份为

$$
\boxed{
\pi^{b/p}\mathcal C\eta_{N,b}
=[\pi]_*\left(
G_0\mathcal C\eta_{\pi,b}
+G_1\mathcal C(B_{H,k}\eta_{\pi,b})
\right).
}
\tag{42}
$$

这是先用完整
$[\pi]_*(\overline V_{N,\pi}\eta_{\pi,b})=\pi^b\eta_{N,b}$，
再用 Cartier 的 $p$ 次幂线性；因此保全部微分 pushforward 的尺度。
它没有将 $B_{H,k}$ 越过 Cartier，也没有删除第二项的 exact 或局部留数。

### 9.4 最后一块的原核补偿准确相消

(39)的第二项在 $O$ 从 $\xi^{k+1}$ 起，
即从 $z^{N+6}$ 起；这不表示它在十三核处为零。
在每个非零 $\pi$ 核点，$1+\xi=v_\pi$ 是一个一阶零。
$G_0,G_1$ 各恰有 $H$ 阶零。
由(35)模 $(1+\xi)^{H+1}$，

$$
\boxed{
B_{H,k}\equiv-(-1)^qC_{H,q}
\pmod{(1+\xi)^{H+1}}.
}
\tag{43}
$$

这里用了 $H<p$，因而 $\xi^{-qp}$ 在这个核 jet 中只有常数
$(-1)^q$。

对整个目标前缀 $n=rp+b\le H(p+1)$，
若 $r<H$，(42)两项的核零阶已经使它们不贡献所读 $Z^{r-1}$。
若 $r=H$，则必有 $0\le b\le H$。
在这些实际低 jet 中，(43)给
$c_b(B_{H,k}T_Tf)=-(-1)^qC_{H,q}\,c_b(T_Tf)$。
同时 $G_0,G_1$ 的核首系数分别是
$C_{H,q}(Dv_\pi(T))^H$ 和
$(-1)^q(Dv_\pi(T))^H$。
因此(42)中两个完整核贡献逐个 $T$、逐个 $b\le H$ 相消。

这证明了(39)如何精确补回 R1013 的 $H$ 阶隔核权的最后一块：
原 kernel 的 $c_b(T_Tf)$ 全部保留，并因实际系数而相消，
不是因为预先给这些平移赋了 canonical 零。
它同时给后续使用 R1015 固定字来源时的两个真实 gauge
和一个确定的窄带输入。
两 exact、原 $P_{10}$、两个 Gaussian 及(24)的完整精度不由此消失。
