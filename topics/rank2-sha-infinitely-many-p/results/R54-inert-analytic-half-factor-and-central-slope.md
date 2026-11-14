# R54. 惰性中央权的实际解析半因子与完整导数证书

日期：2026-11-12。**状态：构造、阶数比较、首层及严格尾界均已证明。**
**主问题未完成：尚未证明导数在无穷多个素数上非零。**

## 1. 从同一固定截面构造解析函数

在 $E_1:y^2=x^3-x$ 上，令
$$
A=\frac15\vartheta\sigma^{16}(x^2+1)(5x^4-2x^2+1)
     =\sum\beta_mz^m,\qquad
S=(x^2+1)\sigma^4=\sum s_mz^m.
$$
$A$ 是 R51 目标截面的单位缩放，$\beta_4=1$；
$S$ 才是这条秩零参考曲线的实际 theta 因子，$s_0=1$。
固定惰性 $p\ge7$，置 $d=p+1$、$r=d/4$、$t=-x/y$，并取
$$
c=[t^d]\log\bigl(\sigma(\log_Et)/t\bigr)\in\mathbb Q,\qquad v_p(c)=-1.
$$
R38 的固定有理递推准确给出这个数。

存在实际解析余项
$$
A(z)=e^{17cz^d}G(z),\qquad S(z)=e^{4cz^d}G_0(z),
\tag{1}
$$
它们在 $R=p^{-1/(2p)}$ 的闭圆盘上满足
$$
\|G\|_R\le R^4,\qquad \|G_0\|_R\le1.
\tag{2}
$$
(1) 是形式恒等式；没有要求单独的指数在整个较大圆盘上收敛。

写 $g_n=[z^n]G$、$g_n^0=[z^n]G_0$，定义下降阶乘
$(u)_h=u(u-1)\cdots(u-h+1)$，并置
$$
\boxed{\quad
J_p(u)=\sum_{h\ge0}a_h(u)_h,\quad a_h=g_{dh}(17c)^{-h},\qquad
J_{0,p}(u)=\sum_{h\ge0}a_h^0(u)_h,\quad a_h^0=g_{dh}^0(4c)^{-h}.
\quad}
\tag{3}
$$
准确系数界为
$$
v_p(a_h)\ge\left\lceil\frac{h(p-1)+4}{2p}\right\rceil,\qquad
v_p(a_h^0)\ge\left\lceil\frac{h(p-1)}{2p}\right\rceil
\quad(h\ge1).
\tag{4}
$$
所以两级数在 $|u|_p<p^{(p-1)/(2p)}$ 上解析，并且
$$
J_p\in pu\mathbb Z_p\langle u\rangle,\qquad
J_{0,p}\in1+p\mathbb Z_p\langle u\rangle.
\tag{5}
$$
对每个整数 $k\ge0$，有准确插值
$$
\boxed{\quad
J_p(k)=k!(17c)^{-k}\beta_{dk},\qquad
J_{0,p}(k)=k!(4c)^{-k}s_{dk}.
\quad}
\tag{6}
$$

## 2. 收敛证明保留了高度二与实际坐标

完整证明分见
[解析半因子全文](../notes/2026-11-12-inert-central-mahler-half-factor.md)
及[更大余项圆盘](../notes/2026-11-12-inert-half-factor-first-layer.md)。
这里给出关键估计，说明过收敛不是一个额外假设。

固定形式对数为
$$
\log_Et=t+\sum_{n\ge1}
 \frac{(-1)^n\binom{2n}{n}}{4n+1}t^{4n+1}.
$$
若 $p^a\mid4n+1$，$n$ 的前 $a$ 个 $p$ 进位数交替为
$3r-1,r-1,\ldots$。相加 $n+n$ 至少有 $\lceil a/2\rceil$ 次进位，
故该对数系数赋值至少 $-\lfloor a/2\rfloor$。
于是形式对数在每个半径小于 $p^{-1/(p^2-1)}$ 的圆盘上有等距解析逆。
令 $W=z^2x(z)=1+\sum A_nz^{4n}$，得到
$$
v_p(A_n)\ge-\frac{4n}{p^2-1}.
\tag{7}
$$

在加法坐标中
$$
F_\sigma(z):=\log(\sigma(z)/z)
       =-\sum_{n\ge1}\frac{A_nz^{4n}}{4n(4n-1)}.
$$
它的 $z^d$ 系数与上述 $c$ 相差一个 $p$ 整数。
在次数小于 $p^2-1$ 时，(7) 使 $A_n$ 整。
除去 $d=p+1$ 后，分母首次可能再含 $p$ 的次数至少为 $4p$；
因此在 $R=p^{-1/(2p)}$ 上所有这些非临界项的加权赋值严格超过
$1/(p-1)$。
对次数 $q\ge p^2$，令 $b=\lfloor\log_pq\rfloor$，统一下界是
$$
q\left(\frac1{2p}-\frac1{p^2-1}\right)-b>\frac1{p-1};
$$
在 $b=2,p=7$ 已严格成立，之后增加。边界 $q=p^2-1$ 单独满足同一严格界。
故
$$
\|F_\sigma-cz^d\|_R<p^{-1/(p-1)}.
$$
这个余项的 $4$、$17$ 倍均可实际取指数。把 $x=z^{-2}W$ 代入 $A,S$，
其余前因子分别从 $z^4$、$1$ 开始且整，立即得到 (1)–(2)。
(4) 是 Gauss 界逐系数求得；下降阶乘的系数为整数，证明 (3)–(5)。
在整数 $k$ 处，$(k)_h=0$ 对 $h>k$ 成立，(1) 的有限系数卷积遂给 (6)。

## 3. 与同一个 Rubin 整函数的中央阶数完全比较

令 $\mathcal A_p(T)\in\mathbb Z_{p^2}[[T]]$ 为 R50 的实际 signed
Rubin 系数，$x_m=q^m-1$、$v_p(q-1)=1$。
参考实际全权平方为
$$
d_m^{(0)}/f_0^{2m+1}=\tfrac14\,32^{-m}s_m^2\qquad(4\mid m).
$$
因为 $J_{0,p}(k)$ 始终为单位，(6) 给出全部同支权的准确参考赋值
$$
v_ps_{dk}=-k-v_p(k!),\qquad
v_pd_{dk}^{(0)}=-2k-2v_p(k!).
\tag{8}
$$
因此 R50 的全权比较可用于每个正整数 $k$，R51 的平方公式又给
$$
\boxed{\quad v_p\mathcal A_p(x_{dk})=2v_pJ_p(k).\quad}
\tag{9}
$$
两个 $k!$ 和两个赋值为 $-1$ 的指数常数准确抵消；
这里没有假定未知高权周期的单位比值随权解析。

$\mathcal A_p\ne0$ 来自 BKO 2021 的 torsion 与特征理想定理。
由 (9) 及 $x_{dp^a}\to0$，$J_p$ 也不恒为零。
设 $e=\operatorname{ord}_0J_p$、$j_e=[u^e]J_p\ne0$。沿 $k=p^a$，
比较 (9) 关于 $a$ 的斜率和常数，得到
$$
\boxed{\quad
\operatorname{ord}_0\mathcal A_p=2e,\qquad
v_p([T^{2e}]\mathcal A_p)=2v_p(j_e)-2e.
\quad}
\tag{10}
$$
特别是 $v_p(j_e)\ge e$，且 Rubin 中央首项赋值为偶数。
R50 的控制是
$$
2\le\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}
 \le\operatorname{ord}_0\mathcal A_p=2e.
$$
所以
$$
\boxed{\quad J_p'(0)\ne0\ \Longrightarrow\
\Sha(E_{17}/\mathbb Q)[p^\infty]\text{ 有限}.\quad}
\tag{11}
$$
本处没有证明反向等价；不能把普通 R40 的完整主项结论未经比较移入惰性情形。

## 4. 首层准确等于原首权，高精度由严格尾界检测

(4) 对每个 $h\ge2$ 都至少为二，因此有整个 Tate 代数的同余
$$
\boxed{\quad
J_p(u)\equiv\frac{\beta_{p+1}}{17c}u\pmod{p^2},\qquad
\frac{J_p'(0)}p\equiv\frac{\beta_{p+1}}{17pc}\pmod p.
\quad}
\tag{12}
$$
$pc$ 是单位，$b_{p+1}=17^{r-1}\beta_{p+1}$，故
$$
b_{p+1}\in\mathbb Z_p^\times
\quad\Longleftrightarrow\quad J_p'(0)/p\in\mathbb Z_p^\times.
$$
这次删除高 $h$ 的依据是已经证明的更大余项圆盘。

对一般精度，逐项求导给
$$
J_p'(0)=\sum_{h\ge1}(-1)^{h-1}(h-1)!a_h.
$$
若 $L_{p,H}$ 为前 $H$ 项，则
$$
\boxed{\quad
v_p(J_p'(0)-L_{p,H})\ge
M_{p,H}:=\left\lceil\frac{(H+1)(p-1)+4}{2p}\right\rceil+v_p(H!).
\quad}
\tag{13}
$$
所以 $J_p'(0)\ne0$ 当且仅当某个有限 $H$ 满足
$v_pL_{p,H}<M_{p,H}$。结合 (11) 是实际的有限初级有限性证书，
容许导数有更高但有限的赋值；尚未给出这样的证书对无穷多个 $p$ 存在。

较弱圆盘曾给“首权非单位迫使整个首层下降阶乘截断消失”的结论。
(12) 进一步说明其中所有 $h\ge2$ 项本来就被 $p^2$ 整除；
这并没有产生一组新的独立非消失条件。

## 5. 一个实际消去参考周期的固定覆盖

原函数确有代数恒等式
$$
\frac{G^4}{G_0^{17}}=\frac{A^4}{S^{17}}
 =\frac{x^2(5x^4-2x^2+1)^4}{5^4(x^2+1)^{13}}.
$$
因此实际固定对象可以取为
$$
\widetilde C:\quad y^2=x^3-x,\qquad v^4=x^2/(x^2+1),
$$
及其函数
$$
B=\frac{5x^4-2x^2+1}{5(x^2+1)^3}v,\qquad
A/S^{17/4}=G/G_0^{17/4}=B.
$$
在 $O$ 上方取 $v\to1$ 的支和常数项一的 $17/4$ 次幂。
分支除子是 $4(T)-\sum_{[2]Q=T}(Q)$，四个后者各完全分歧，
Riemann–Hurwitz 给 $g(\widetilde C)=7$。

这是实际消期得到的覆盖；下降阶乘变换 (3) 却不是乘法同态。
尚须构造它与这个覆盖的具体 cohomology/Frobenius 的比较，
不能把任意 Cartier 矩阵项或覆盖普通性直接等同于 (11) 的导数。
