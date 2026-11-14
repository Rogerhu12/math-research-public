# 固定 sigma 的非实 CM 除法函数与多乘子共同共振

**可信度：本文各命题已证明；没有推出初级有限的无穷性。**
日期：2026-11-12。

固定
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
\omega=\frac{dx}{2y},\quad t=-x/y,\quad
z=\log_E(t),\quad D=d/\omega.
$$
令 $\Sigma(t)$ 为先前笔记中唯一的奇级数，首项为 $t$，满足
$D^2\log\Sigma=-x$。
复一致化后记
$$
\sigma(z)=\Sigma(t(z)),\qquad
\zeta(z)=D\log\Sigma(t(z)).
$$
则 $x(z)=\wp(z)$、$y(z)=\wp'(z)/2$，
$\zeta'=-\wp$，而 $\sigma$ 是对应方格周期格的经典 sigma。
本笔记构造其非实 CM 除法关系，并准确区分它与 R41 的未扭曲共同逆像。

## 1. 准周期的 CM 变换及符号

设周期格为 $\mathcal L=\Omega\mathbb Z[i]$。
CM 对称性给
$$
\sigma(iz)=i\sigma(z),\qquad \zeta(iz)=-i\zeta(z).
\tag{1.1}
$$
对 $\lambda\in\mathcal L$ 定义
$\eta(\lambda)=\zeta(z+\lambda)-\zeta(z)$。
它与 $z$ 无关，并且是 $\mathbb Z$-线性的。
由 (1.1)，
$$
\eta(i\lambda)=-i\eta(\lambda),\qquad
\boxed{\eta(\beta\lambda)=\bar\beta\,\eta(\lambda)}
\quad(\beta\in\mathbb Z[i]).
\tag{1.2}
$$

写 $\lambda=m\Omega+ni\Omega$，经典准周期式为
$$
\sigma(z+\lambda)=\epsilon(\lambda)
\exp\!\left(\eta(\lambda)(z+\lambda/2)\right)\sigma(z),
\quad
\epsilon(\lambda)=(-1)^{m+n+mn}.
\tag{1.3}
$$
这里 $\epsilon(\lambda)=1$ 当且仅当 $\lambda\in2\mathcal L$；
其余三个模 $2\mathcal L$ 的类均给 $-1$。
公式 (1.3) 是 DLMF 23.2.17；(1.2) 是由本曲线 CM 对称性得到的计算，
没有将 $\eta$ 错当成复线性函数。

取 $\beta\ne0$，记 $d=N\beta=\beta\bar\beta$，定义
$$
R_\beta(z)=\frac{\sigma(\beta z)}{\sigma(z)^d}.
\tag{1.4}
$$
在 $z\mapsto z+\lambda$ 下，指数部分的差为
$$
\bar\beta\eta(\lambda)
\left(\beta z+\frac{\beta\lambda}{2}\right)
-d\eta(\lambda)(z+\lambda/2)=0.
$$
所以
$$
R_\beta(z+\lambda)
=\frac{\epsilon(\beta\lambda)}{\epsilon(\lambda)^d}R_\beta(z).
\tag{1.5}
$$

若 $d$ 为奇数，$\beta$ 在 $\mathbb Z[i]/2$ 中可逆，
故它置换三个非零类，(1.5) 的符号为 $1$。
若 $2\mid\beta$，两个符号同样均为 $1$。
若 $v_{1+i}(\beta)=1$，取 $\lambda=\Omega$，
则 $\beta\lambda\notin2\mathcal L$、$d$ 为偶数，
故符号为 $-1$。
因此得到完整分类：
$$
R_\beta\in\mathbb C(E)
\quad\Longleftrightarrow\quad v_{1+i}(\beta)\ne1,
\qquad R_\beta^2\in\mathbb C(E)\ \text{总成立}.
\tag{1.6}
$$

所有这些函数的除子和首项均已固定：
$$
\operatorname{div}R_\beta=[\beta]^*(O)-d(O),\qquad
R_\beta(t)=\beta\,t^{1-d}+\cdots
\tag{1.7}
$$
（在非周期情形，第一式读为相应二重覆盖上该除子的 pullback；
平方在 $E$ 上的除子为其两倍）。
当 $d$ 奇时，非零核点两两以 $T,-T$ 配对，除子 (1.7) 的
Abel 和为零，故它确实主；准周期证明还排除了未确定指数因子。
除子在 $K$ 上定义且规范首项在 $K$，由唯一性和 Galois 下降，
周期情形的函数属于 $K(E)$，平方亦属于 $K(E)$。
也可直接用 $\Sigma\in\mathbb Q[[t]]$ 和 $[\beta](t)\in K[[t]]$
检验相同的下降。

以下在奇范数时记
$$
\Psi_\beta=R_\beta\in K(E)^\times.
$$
它只有 $O$ 处一个极点，阶数为 $d-1$。
又因奇范数 $d\equiv1\pmod4$，
$$
R_\beta(iz)=i^{\,1-d}R_\beta(z)=R_\beta(z).
$$
函数域的 $[i]$-不变子域为 $K(x^2)$；
无有限极点迫使
$$
\boxed{\Psi_\beta\in K[x^2],\quad
\deg_{x^2}\Psi_\beta=(d-1)/4,\quad
\text{最高系数为 }\beta.}
\tag{1.8}
$$
范数为 $1$ 时，此式理解为常数 $\Psi_\beta=\beta$。

## 2. 两个明确的奇范数函数

**命题。**
$$
\boxed{\Psi_{2+i}=(2+i)x^2-17i,}
\tag{2.1}
$$
$$
\boxed{\begin{aligned}
\Psi_{3+2i}={}&(3+2i)x^6+(119-68i)x^4\\
&+(-3179+2890i)x^2+4913.
\end{aligned}}
\tag{2.2}
$$
共轭给出 $\Psi_{2-i}$、$\Psi_{3-2i}$ 的准确式。

**推导。** 由 $x''=6x^2-34$ 和 $x=z^{-2}+O(z^2)$，
逐项比较得到
$$
x=z^{-2}+\frac{17}{5}z^2+\frac{289}{75}z^6
+\frac{9826}{4875}z^{10}+O(z^{14}).
\tag{2.3}
$$
因此
$$
\begin{aligned}
F(z):=\log\frac{\sigma(z)}z
&=f_1z^4+f_2z^8+f_3z^{12}+O(z^{16}),\\
f_1&=-\frac{17}{60},\quad
f_2=-\frac{289}{4200},\quad
f_3=-\frac{4913}{321750},\\
x^2&=z^{-4}+u+vz^4+wz^8+O(z^{12}),\\
u&=\frac{34}{5},\quad v=\frac{289}{15},\quad
w=\frac{9826}{325}.
\end{aligned}
\tag{2.4}
$$

对 $d=5$，(1.8) 给 $\Psi_\beta=\beta x^2+C$。
另一方面
$$
R_\beta=\beta z^{-4}
\exp\!\left(f_1(\beta^4-5)z^4+O(z^8)\right).
$$
匹配常数项得到
$C=\beta(f_1(\beta^4-5)-u)=-17i$，其中 $\beta=2+i$。
这就证明 (2.1)。

对 $\beta=3+2i$、$d=13$，记
$r_j=f_j(\beta^{4j}-13)$。
将 (1.8) 写成
$\Psi_\beta=\beta (x^2)^3+B(x^2)^2+Cx^2+A$。
从
$$
R_\beta=\beta z^{-12}
\exp(r_1z^4+r_2z^8+r_3z^{12}+O(z^{16}))
$$
匹配 $z^{-8},z^{-4},z^0$，得到三角方程
$$
\begin{aligned}
B&=\beta r_1-3\beta u,\\
C&=\beta(r_2+r_1^2/2)-3\beta(u^2+v)-2Bu,\\
A&=\beta(r_3+r_1r_2+r_1^3/6)
-\beta(u^3+6uv+3w)-B(u^2+2v)-Cu.
\end{aligned}
\tag{2.5}
$$
代入 (2.4) 分别得到
$B=119-68i$、$C=-3179+2890i$、$A=4913$。
由于 (1.8) 已证明这是次数恰为三的多项式，
这四个 Laurent 系数唯一决定整个函数，证明完成。

另一个纯代数核对为
$$
x([2]R)=\frac{(x^2+17)^2}{4x(x^2-17)}.
$$
在 $(2+i)x^2-17i=0$ 上，它等于 $-x$，
而 $y([2]R)/y=2x^2/(x^2-17)=-i$，
故确有 $[2+i]R=O$。
附带小脚本还以 $[3]R=-[2i]R$ 的坐标恒等式核对 (2.2)，
与上述 Laurent 推导互相独立。

## 3. 偶范数的最小例子：不能遗漏平方

$\ker[1+i]=\{O,T\}$，其中 $T=(0,0)$。
因 $T-(O)$ 不是主除子，$R_{1+i}$ 不属于 $K(E)$。
但平方的除子为 $2(T)-2(O)=\operatorname{div}x$，
且其首项为 $(1+i)^2z^{-2}=2iz^{-2}$。
故
$$
\boxed{\left(\frac{\sigma((1+i)z)}{\sigma(z)^2}\right)^2=2ix(z).}
\tag{3.1}
$$
在形式邻域中选择首项 $(1+i)t^{-1}$ 的平方根，即得到准确的未平方关系。
这也可由 sigma 加法公式直接核对：
取 $u=z,v=iz$，使用 $\sigma(iz)=i\sigma(z)$、
$\wp(iz)=-\wp(z)$ 和
$\sigma((1-i)z)=-i\sigma((1+i)z)$，
同样得到 (3.1)。

## 4. 完整兼容关系和共同形式逆像

由 sigma 的定义直接相消，任意非零 $\alpha,\beta\in\mathbb Z[i]$ 满足
$$
R_{\alpha\beta}(z)
=R_\alpha(\beta z)R_\beta(z)^{N\alpha}
=R_\beta(\alpha z)R_\alpha(z)^{N\beta}.
\tag{4.1}
$$
当两个范数均奇时，这就是 $K(E)^\times$ 中的准确恒等式，
没有剩余根单位或常数：
$$
\boxed{\Psi_\alpha([\beta]R)\Psi_\beta(R)^{N\alpha}
=\Psi_\beta([\alpha]R)\Psi_\alpha(R)^{N\beta}.}
\tag{4.2}
$$
首项亦核对为 $\alpha\beta\,t^{1-N\alpha N\beta}$。

若要求在 $t=0$ 的真正形式单位中工作，置
$$
S(t)=\frac{\Sigma(t)}t,\qquad
U_\beta(t)=\frac{\Psi_\beta(t)t^{N\beta}}{[\beta](t)}
\in K(E)^\times\cap(1+tK[[t]]).
$$
则
$$
\boxed{\frac{S([\beta]t)}{S(t)^{N\beta}}=U_\beta(t),}
\tag{4.3}
$$
而 $U_\alpha,U_\beta$ 满足与 (4.2) 相同的兼容式。
这给出了两个固定代数右端和同一个实际形式逆像 $S$。

在对角坐标 $z$ 中，设
$$
A_\beta(z)=
\log\frac{R_\beta(z)}{\beta z^{1-N\beta}}.
$$
则
$$
\boxed{F(\beta z)-N\beta\,F(z)=A_\beta(z),\qquad
[z^k]A_\beta=(\beta^k-N\beta)[z^k]F.}
\tag{4.4}
$$
两个右端的兼容性精确为
$$
(\beta^k-N\beta)[z^k]A_\alpha
=(\alpha^k-N\alpha)[z^k]A_\beta.
\tag{4.5}
$$
对于固定非实 $\beta$、$N\beta>1$，
所有整数 $k\ge0$ 都有 $\beta^k\ne N\beta$：
取复绝对值先迫使 $k=2$，随后 $\beta^2=N\beta$
又迫使 $\beta=\bar\beta$，矛盾。
所以 (4.4) 在特征零中逐系数唯一确定 $F$；
对 $\alpha=2+i,\beta=3+2i$，(4.5) 确实给同一个共同逆像。
此处的“没有特征零零分母”不等于它在所有有限位整。

## 5. zeta 关系及其准确特征

对 (1.4) 取 $D=d/dz$ 的对数导数并除以 $\beta$，得到
$$
\boxed{\zeta(\beta z)-\bar\beta\,\zeta(z)
=Z_\beta(z),\qquad
Z_\beta=\frac1\beta D\log R_\beta\in K(E).}
\tag{5.1}
$$
即使 $v_{1+i}(\beta)=1$，也可用
$Z_\beta=(2\beta)^{-1}D\log R_\beta^2$，
所以右端仍是有理函数。
特别地
$$
Z_{2+i}=\frac{4xy}{(2+i)x^2-17i},\qquad
Z_{1+i}=\frac{y}{(1+i)x}.
\tag{5.2}
$$
对 $3+2i$，
$Z_{3+2i}=2y\Psi'_{3+2i}(x)/((3+2i)\Psi_{3+2i}(x))$，
其中导数是对 $x$ 求导。

这些右端满足准确的加法兼容式
$$
Z_\alpha(\beta z)-\bar\beta Z_\alpha(z)
=Z_\beta(\alpha z)-\bar\alpha Z_\beta(z).
\tag{5.3}
$$
若 $\zeta(z)=\sum q_kz^k$，其中 $q_{-1}=1$，
则对应系数是
$$
[z^k]Z_\beta=(\beta^k-\bar\beta)q_k.
\tag{5.4}
$$
所以这里的特征为 $\bar\beta$，不是 $1$。

## 6. 多个非实乘子共同保留每一个惰性共振

令 $p\ge7$、$p\equiv3\pmod4$，且 $p\nmid N\beta$。
在 $\mathbb Z[i]/p\simeq\mathbb F_{p^2}$ 中，
Frobenius 是复共轭。因此
$$
\beta^p\equiv\bar\beta\pmod p,\qquad
\boxed{\beta^{p+1}\equiv N\beta\pmod p.}
\tag{6.1}
$$
这对**任意预先选定的有限多个** CM 乘子同时成立，
并非某个底数偶然具有小阶。
在 (4.4) 中的共同共振权是 $k=p+1$；
在 (5.4) 中，zeta 的实际单项次数为 $k=p$。
两者相差一次微分，描述的是同一个现象。

特别地，对 $\beta_1=2+i,\beta_2=3+2i$，
若
$$
c_p=\min_{j=1,2}v_p(\beta_j^{p+1}-N\beta_j),
$$
则每个这样的惰性 $p$ 都有 $c_p\ge1$，故
$$
\sum_{p\equiv3\ (4),\,p\ge7}
\frac{c_p\log p}{p+1}=\infty.
\tag{6.2}
$$
这里仅用固定算术级数的素数定理；
$5,13$ 都分裂，不造成惰性集合的例外。

这不是只检查分母的形式现象。先前固定 sigma 笔记已证，
令 $r=(p+1)/4$、$w_r=(-1)^r\binom{2r}{r}17^r$，则
$$
v_p([t^{p+1}]\log(\Sigma/t))=-1,\qquad
p[t^{p+1}]\log(\Sigma/t)\equiv-\frac{w_r}{2}\pmod p.
$$
到所需次数 $p+2$ 为止，
$z(t)=t+\sum w_n t^{4n+1}/(4n+1)$ 的分母都素于 $p$；
其形式逆亦整，且 $\log(z/t)$ 到 $p+1$ 次也整。
因此同一首坏系数在 $F(z)$ 中仍满足
$$
\boxed{v_p([z^{p+1}]F)=-1,\qquad
p[z^{p+1}]F\equiv-\frac{w_r}{2}\pmod p.}
\tag{6.3}
$$
对应 zeta 的 $z^p$ 系数是 $(p+1)[z^{p+1}]F$，
也恰有赋值 $-1$。
在所有右端中，它被 (6.1) 的共同因子 $p$ 抵消。

所以我们已经有实际的兼容代数右端、实际的共同特征零逆像，
同时也有每个惰性素数处的真实非整系数。
这与 R38 的精确 sigma size 完全一致。

R41 控制的是 $\beta_j^k-1$ 的共同深度，利用
$\langle\beta_1,\beta_2\rangle$ 的模 $p^c$ 群阶。
本节分母是 $\beta_j^k-N\beta_j$ 或
$\beta_j^k-\bar\beta_j$；它们不能替换成 R41 的未扭曲分母。
式 (6.1)–(6.3) 给出了不允许这种替换的具体算术原因。

## 7. 非实乘子固定二次正规化，但不能靠幂次消掉 Norm 特征

全部二次补空间改变为
$\sigma_c(z)=\sigma(z)\exp(cz^2/2)$。
整数乘法不能区别它们，但非实 CM 乘法给
$$
\frac{\sigma_c(\beta z)}{\sigma_c(z)^{N\beta}}
=R_\beta(z)\,
\exp\!\left(\frac c2(\beta^2-N\beta)z^2\right).
\tag{7.1}
$$
若 $\beta$ 非实且 $c\ne0$，额外指数不可能是椭圆函数：
沿非零周期 $\lambda$ 平移后，其比值含非恒定因子
$\exp(c(\beta^2-N\beta)\lambda z)$。
甚至它也不在 $\mathbb C(E)$ 上代数：
若代数，周期平移在有限多个分支上置换，
某个非零整数倍周期必固定该亚纯函数，仍与上述指数矛盾。
因此要求一个非实乘子的比值在 $\mathbb C(E)$ 上代数，
已经唯一迫使 $c=0$。

另一方面，乘除固定整数幂 $z^m$ 只会把缩放特征改乘 $\beta^m$。
若要借此把 Norm 特征变为 $1$，需要同时满足
$\beta_j^m=N\beta_j$；上面的绝对值论证已经说明，
对任一非实 $\beta_j$ 都没有这样的整数 $m$。
有限次普通微分同样只引入整数幂的 $\beta_j$，
不能把这里的特征改成 R41 的中心 $1$。
这只排除这些具体变换，没有排除新的多变量或其他算术对象。

## 来源与复算

- [固定 sigma 笔记](2026-11-12-fixed-sigma-height-and-inert-denominator.md)：
  特征零唯一性、CM 固定性和首个惰性分母。
- [sigma 正规化笔记](2026-11-12-sigma-normalizations-and-division.md)：
  整数乘法和全部二次补空间改变。
- [R38](../results/R38-exact-inert-sigma-size-and-jet-budget.md)：
  精确惰性 size 与无限坏系数列。
- NIST DLMF，[§23.2](https://dlmf.nist.gov/23.2)，
  式 23.2.7–8、23.2.11、23.2.17；
  [§23.10](https://dlmf.nist.gov/23.10)，式 23.10.3。
- [R41](../results/R41-two-multiplier-common-depth-summability.md)：
  两个未扭曲乘子的共同深度可求和性。
- 小脚本：scripts/check-cm-sigma-division.py；
  仅作有理符号运算，不使用数值精度或数据库 rank 字段。
