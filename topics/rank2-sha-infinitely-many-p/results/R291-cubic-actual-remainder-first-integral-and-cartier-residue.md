# R291：三次实际余项的准确首积分与不能删去的 Cartier 项

**已证明，2026-11-13。** 继续 R288 的同一固定曲线、同一三次同源及原余项。下面把次数随 $p$ 增长的完整强迫压成显式多项式微分，积分出准确的 $-2\log v$ 项；没有把任意 theta 截面或一个 Cartier 计算当作原 $\Sha$ 的中央输入。

## 1. 固定来源和结论

沿用 R288：
$$
E:y^2=x^3+17,\quad c^2=17,\quad a^3=2c,\quad
u^3+v^3=1,\quad u'=av^2,\quad v'=-au^2,\quad q=u^3.
\tag{1}
$$
撇号在 (1) 及涉及 $z$ 的公式中指 $\partial_z$。这是 R288 已构造的真实 $[-\sqrt{-3}]$ 同源覆盖，原点 $u=0,v=1$。其 theta 对数 $Z_N=\log\theta_-^N$、原坏带 $A=a_0h_+$ 和原余项为
$$
z_n=[q^n]Z_N=\frac N{3n}\frac{(1/3)_n}{(2/3)_n},\qquad
h_j=\frac{(2/3)_j}{j!(3j+1)},\qquad
h_+=\sum_{j=0}^{r-1}h_jq^j,
$$
$$
p=3r-1\ge5,\quad p\nmid17N,\quad
a_0=pz_r\in\mathbf Z_p^\times,
$$
$$
U=q^{-r}\bigl(Z_N-[Z_N]_{<r}-(a_0/p)q^rh_+\bigr).
\tag{2}
$$
这里 $U\bmod q^{2r-1}$ 整，且 $U(0)=0$。下文的 $A,U,a_0$ 均约化到特征 $p$，只在已付的窗口使用 $U$。固定好数域在 $p$ 上的一个剩余域 $k$；$a,c\in k^\times$。

定义真正的有限多项式
$$
B_p(V)=\sum_{j=0}^{r-2}
 \frac{(-1)^j\binom{r-1}{j}-1}{3j+2}\,V^{3j+2}\in\mathbf F_p[V].
\tag{3}
$$
所有分母均非零。结论是
$$
\boxed{
v^2\bigl(U+3q\partial_qU+A\bigr)
=a_0\bigl(1+B_p(v)-2\log v\bigr)
\pmod{q^{2r-1}}.}
\tag{4}
$$
其中 $v=(1-q)^{1/3}$ 取 $v(0)=1$，
$$
\log v=\frac13\log(1-q)
=-\sum_{n=1}^{2r-2}\frac{q^n}{3n}\pmod{q^{2r-1}}.
$$
它在此窗口整，故 (4) 没有在特征 $p$ 的无穷级数中无条件使用对数。

更准确的几何载体是多项式微分
$$
\beta_p=\frac{1-u^{p+1}-v^{p+1}}{uv}\,du
       =dB_p(v)-2v^{p-1}dv.
\tag{5}
$$
因此其 Cartier 像准确为
$$
\boxed{C\beta_p=-2\,dv\ne0,\qquad C^2\beta_p=0.}
\tag{6}
特别不能把 (5) 的末项从全局微分中删去，也不能把 $C^2\beta_p=0$ 说成 $\beta_p$ 已有有理原函数。

## 2. 全部强迫的压缩，含最高项

R288 的算子及方程是
$$
\mathscr L=q(1-q)\partial_q^2+(4/3-2q)\partial_q-2/9,
\qquad
\mathscr L U=\mathcal T\pmod{q^{2r-2}},
$$
$$
[q^j]\mathcal T=
\begin{cases}
\displaystyle\frac{2a_0h_j(18j^2+30j+11)}{27(j+1)(3j+4)},&0\le j<r-1,\\[1mm]
\displaystyle\frac{2a_0(2r-1)h_{r-1}}3,&j=r-1.
\end{cases}
\tag{7}
$$
注意 (7) 的顶项不能从无限齐次解的系数递推直接补上。

先由 R288 的准确多项式恒等式
$$
A+3qA'=a_0(1-q)^{r-1}
\tag{8}
$$
比较最高项。因 $p$ 为奇数，$r$ 为偶数；又 $3r-2=p-1$，故
$$
-h_{r-1}=(-1)^{r-1}=-1,\qquad h_{r-1}=1.
\tag{9}
$$
对 (7) 的内项代入 $h_{j+1}/h_j$ 的准确比值，连同顶项 (9)，得到完整式
$$
\mathcal T=-\frac23(1-q)A'
 +\left(\frac13-\frac1{9q}\right)A
 +\frac{a_0}{9q}-\frac{a_0}9q^{r-1}.
\tag{10}
$$
这里 $q^{-1}$ 的两项在原点相消。(10) 的最后一项正是补足真实顶项的项。再以 (8) 消去 $A'$，得到
$$
\boxed{9q\mathcal T=(1+q)A+
 a_0\bigl(1-2(1-q)^r-q^r\bigr).}
\tag{11}
$$
这是完整多项式恒等式，未丢掉任何顶端系数。

## 3. 在同一三次曲线上的一次消元

置
$$
Y=uU,\qquad H=uA,\qquad U_p=u^p,\qquad V_p=v^p.
$$
由 (8)，在函数域中准确有
$$
H'=aa_0V_p,\qquad H''=0.
\tag{12}
$$
R288 的真实 Darboux 等式是
$$
Y''=9a^2u^2v\mathscr L U.
$$
把 (11) 代入右边，注意 $q^r=uU_p$、$(1-q)^r=vV_p$，其实际强迫可写为
$$
a^2\frac{v(1+u^3)}{u^2}H
 +a^2a_0\left(\frac vu-2V_p\frac{v^2}u-U_pv\right).
\tag{13}
$$
这里 $U_p,V_p$ 是实际 Frobenius 函数，微分为零；它们不是可以在全局函数域里任意置一的常数。

直接由 (1) 得
$$
\left(\frac{v^2}u\right)'=-a\frac{v(1+u^3)}{u^2}.
\tag{14}
$$
于是令 $J=Y'+a(v^2/u)H$，由 (12)–(14) 得
$$
J'=a^2a_0\left(\frac vu-V_p\frac{v^2}u-U_pv\right).
\tag{15}
$$
乘 $dz=du/(av^2)$ 后，(15) 的右端正是 $aa_0\beta_p$。对原截断余项，除去 $\partial_z=3au^2v^2\partial_q$ 的公共因子，式 (15) 在 $q$ 微分中准确到 $q^{2r-2}$。所以积分可恢复到模 $q^{2r-1}$；本步积分的分母小于 $p$，没有丢失额外常数方向。

## 4. 显式积分和非零 Cartier 项

利用 $u^{p+1}=u^{3r}=(1-v^3)^r$、$v^{p+1}=v^{3r}$ 以及 $du=-v^2dv/u^2$，直接化简得到
$$
\begin{aligned}
\beta_p
 &=-v\frac{1-(1-v^3)^r-v^{3r}}{1-v^3}\,dv\\
 &=v\left((1-v^3)^{r-1}-\sum_{j=0}^{r-1}v^{3j}\right)dv.
\end{aligned}
\tag{16}
$$
所以整个微分其实属于子域 $k(v)$。其最高项为
$$
\bigl((-1)^{r-1}-1\bigr)v^{3r-2}dv=-2v^{p-1}dv;
$$
其余项的积分分母 $3j+2$ 均不被 $p$ 整除，逐项积分恰好给出 (3)、(5)。

Cartier 在光滑曲线函数域上的公式
$C(dF)=0$、$C(f^p\eta)=fC(\eta)$ 及 $C(v^{p-1}dv)=dv$
于是给 (6)。也可直接在局部参数 $v$ 中按指数 $p-1$ 取项。$dv\ne0$ 是因为 $v$ 为分离参数；由 (1)，$v'=-au^2$ 非零。以上计算在函数域上成立，没有把形式窗口冒充全局有理原函数。

在 $q=0$ 附近，$v(0)=1$，故 $d\log v=dv/v$。将 (5) 积分并暂保完整 Frobenius 因子，可写
$$
J=aa_0\bigl(B_p(v)-2v^p\log v\bigr)+C_0
\pmod{q^{2r-1}}.
\tag{17}
$$
该式只使用 $q$ 次数小于 $p$ 的对数，$\partial_q(v^p)=0$。又 $v^p=1+O(q^p)$，在已付窗口中可将 $v^p\log v$ 替换为 $\log v$；这个替换不适用于全局 (5)。

## 5. 原点归一：$B_p(1)=0$ 的完整证明

除 (3) 直接给出的 $B_p(0)=0$ 外，还有
$$
\boxed{B_p(1)=0.}
\tag{18}
$$
下面证明此式，避免留一个数值归一常数。

在 $\mathbf Q$ 中使用部分分式恒等式
$$
\sum_{j=0}^{r-1}\frac{(-1)^j\binom{r-1}{j}}{3j+2}
=\frac{3^{r-1}(r-1)!}{\prod_{j=0}^{r-1}(3j+2)}.
\tag{19}
$$
它由 $\sum_{j=0}^{m}(-1)^j\binom mj/(x+j)=m!/[x(x+1)\cdots(x+m)]$
在 $m=r-1,x=2/3$ 得到；后式的两边有相同简单极及留数且在无穷远趋零。

取出 (19) 的顶项 $-1/p$，并设
$$
K=\frac{3^{r-1}(r-1)!}{\prod_{j=0}^{r-2}(3j+2)}
 =-\prod_{k=1}^{r-1}\left(1-\frac p{3k}\right)^{-1}.
$$
第二个等号由反向排列 $3j+2=p-3k$ 及 $r-1$ 为奇数得到。因此
$$
K\equiv-1-\frac p3\sum_{k=1}^{r-1}\frac1k\pmod{p^2},
$$
$$
\sum_{j=0}^{r-2}\frac{(-1)^j\binom{r-1}{j}}{3j+2}
=\frac{K+1}{p}
\equiv-\frac13\sum_{k=1}^{r-1}\frac1k\pmod p.
$$
而同样的反向排列给
$\sum_{j=0}^{r-2}(3j+2)^{-1}\equiv-\frac13\sum_{k=1}^{r-1}k^{-1}\pmod p$。
两式相减正是 (18)。

由 $Y'(0)=0$、$H/u=A$ 和 $v(0)=1$，有 $J(0)=aa_0$。于是 (17) 的常数为 $C_0=aa_0$。最后
$$
J=a v^2\bigl(U+3q\partial_qU+A\bigr),
$$
约去 $a$ 就得到 (4)。

## 6. 尖锐窗口与后继接口

式 (4) 逐系数准确给出原 $U$ 的全部已整窗口。事实上 $1+3q\partial_q$ 在 $q^n$ 上的特征值为 $1+3n$，对 $0\le n<2r-1$ 都非零；第一个共振恰在
$$
n=2r-1,\qquad 1+3n=2p.
\tag{20}
$$
这与原 $Z_N$ 的 $q^p$ 项一致，因为 $r+(2r-1)=p$。所以不能凭 (4) 越过 (20)，也不能把下一带的分母算成已消去。

对 $p>5$，$B_p$ 次数准确为 $p-3$，最高系数为 $5/9$；$p=5$ 时 $B_p=0$。又 (18) 及指数模三的形式给
$$
B_p(v)=v^5(v^3-1)C_p(v^3),\qquad
\deg C_p=r-4\quad(p>5).
\tag{21}
$$
这给出真实多项式载体在 $v=0$ 和三个 $v^3=1$ 点的消失，没有引入额外根覆盖。高次项仍是实际有限多项式 (3)，不得把它称为固定低次 theta 截面。

当前可继续的输入是：原余项的全部首积分已压成 (3) 与一个准确系数 $-2$ 的三挠对数比 $\log v=\log(\theta_+/\theta_-)$，并且其 Cartier 余项明确非零。要用于主目标，仍须在原曲线实际 Hecke 特征的 Schwartz 模型中支付此对数比的全部权、质量、Euler 因子和中央比较。本篇不预设这一比较，也不以 (6) 直接推出任何素数的 $\Sha[p^\infty]$ 有限。

## 7. 精确证书

`scripts/check-cubic-remainder-first-integral.py` 以有理数计算 (2) 的真实余项，再在 $p=5,11,23$ 的完整允许窗口核对 (4)。这三项覆盖 $B_5=0$ 的边界及非零多项式情形；证明对全部 (2) 的素数由上面统一恒等式给出，未依赖素数样本。同时脚本核对最高项、$B_p(1)$、微分分解及第一个共振位置。
