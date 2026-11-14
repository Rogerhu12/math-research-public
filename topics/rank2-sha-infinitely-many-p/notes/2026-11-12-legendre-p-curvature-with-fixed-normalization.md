# 固定规范的 Legendre p-curvature 与实际 Frobenius 模 p 行

日期：2026-11-12。状态：本篇矩阵公式、常数 $1$、Cartier 恒等式，
以及惰性处实际 $V\bmod p$ 的全形式盘闭式均已证明。
这些第一层信息不证明实际中央除 $p$ 行非零。

## 1. 固定家族与结论

令 $p$ 为奇素数，在 $\mathbb F_p(t)$ 上置
$$
s=1-4t^2,\qquad
A=\begin{pmatrix}0&1\\s^{-1}&8t/s\end{pmatrix},
\qquad n=(p-1)/2,\qquad H(t)=P_n(2t).
\tag{1}
$$
$P_n$ 是标准 Legendre 多项式，规范为 $P_n(1)=1$。
它的方程给
$$
sH''-8tH'-H=-p^2H=0\quad\hbox{于 }\mathbb F_p[t].
\tag{2}
$$
本篇始终使用这个 $H$；若先把 $H(0)$ 或 $H'(0)$ 归一为一，
下面矩阵的标量必须相应改变。

对 $Y'=AY$ 定义 $P_j$ 使 $Y^{(j)}=P_jY$，即
$$
P_0=I,\qquad P_{j+1}=P_j'+P_jA.
\tag{3}
$$
实际 $p$ 次迭代矩阵准确为
$$
\boxed{\quad
P_p=s^{\,1-p}
\begin{pmatrix}
HH'&-H^2\\
(H')^2&-HH'
\end{pmatrix}.
\quad}
\tag{4}
$$
因此它非零、秩一、平方为零；核与像都由
$(H,H')^t$ 张成。若把水平连接写成 $\partial_t-A$，
其 $p$-curvature 矩阵是 (4) 的负数；
以下固定使用 (3) 的 $Y^{(p)}$ 约定，避免整体符号歧义。

## 2. 多项式界先把未知常数缩到一个标量

置 $N_j=s^jP_j$。由 (3) 得整多项式递推
$$
N_{j+1}=sN_j'-j s'N_j+
N_j\begin{pmatrix}0&s\\1&8t\end{pmatrix}.
\tag{5}
$$
直接归纳得到
$$
\deg N_{j,11},\deg N_{j,22}\le j,\quad
\deg N_{j,12}\le j+1,\quad
\deg N_{j,21}\le j-1.
\tag{6}
$$
零多项式的次数取 $-\infty$，所以初始步也成立。

$H$ 的次数准确为 $n$，且 $\gcd(H,H')=1$。
证明后者时，先用 $H(\pm1/2)=(\pm1)^n$ 排除 cusp。
若其他点同时满足 $H=H'=0$，(2) 的普通点 Taylor 递推
迫使全部次数 $\le n<p$ 的系数为零，矛盾。

为在特征 $p$ 中严格使用第二解，令
$$
W=\frac1{sH^2}
$$
并在有理函数域 $\mathbb F_p(t,z)$ 上延拓导数，
**定义** $z'=W$。这里 $z$ 是新不定元；
没有假设 $W$ 在 $\mathbb F_p((t))$ 中存在形式原函数。
由 reduction of order 直接检查
$$
\mathcal Y=
\begin{pmatrix}
H&Hz\\
H'&H'z+HW
\end{pmatrix},
\qquad \mathcal Y'=A\mathcal Y,\qquad
\det\mathcal Y=H^2W=s^{-1}.
\tag{7}
$$
$\partial_t^p$ 在特征 $p$ 中是导子，并在
$\mathbb F_p(t)$ 上为零。因此
$P_p(H,H')^t=0$，而对 (7) 的行列式应用该导子得到
$$
\operatorname{tr}P_p=0.
\tag{8}
$$

写 $N_p=\begin{pmatrix}a&b\\c&-a\end{pmatrix}$。
由其核及 $\gcd(H,H')=1$，依次可得
$H\mid b$、$H^2\mid b$，继而
$$
N_p=F(t)
\begin{pmatrix}HH'&-H^2\\(H')^2&-HH'\end{pmatrix},
\qquad F\in\mathbb F_p[t].
\tag{9}
$$
由 (6) 的右上项和 $\deg H^2=p-1$，有 $\deg F\le2$。

在基域上 $\partial_t^p A=0$，所以 (7) 也给
$P_p'=[A,P_p]$。记 (9) 中的秩一矩阵为 $B_H$；
利用 (2) 逐项求导得到
$$
B_H'=[A,B_H]-\frac{s'}sB_H.
$$
又 $(s^{-p})'=0$，故 (9) 的水平性等价于
$$
sF'-s'F=0.
\tag{10}
$$
把次数至多二的 $F=\alpha t^2+\beta t+\gamma$ 代入，
得到 $\beta=0,\ \alpha=-4\gamma$，即
$F=\kappa s$。至此 (4) 只剩一个 $\kappa\in\mathbb F_p$ 待定。

## 3. 一个 cusp 的主部准确确定常数为一

仍使用 (7) 中严格定义的 $z$。由特征 $p$ 的 Leibniz 公式，
$$
\partial_t^p(Hz)=H\,\partial_t^{p-1}W.
$$
另一方面，候选 $\kappa s^{1-p}B_H$ 作用于第二列的第一坐标为
$-\kappa Hs^{-p}$。因此
$$
\partial_t^{p-1}W=-\kappa s^{-p}.
\tag{11}
$$

在 $t=1/2+x$ 附近，$H(1/2)=1$，
$s=-4x(1+x)$，所以
$$
W=-\frac1{4x}+O(1).
$$
对其求 $p-1$ 次导数，再用 $(p-1)!=-1$，得到最高极项
$1/(4x^p)$。解析部分求导不产生负幂。
而 (11) 右侧的最高极项恰为 $\kappa/(4x^p)$。
所以 $\kappa=1$，证明 (4)。
这一步在一个合法微分域中进行，不需要特征 $p$ 的
无穷形式对数解，也不需要借助有限素数数值模式。

## 4. 固定 rational Cartier 恒等式

由 (11) 及 $\kappa=1$，
$$
\partial_t^{p-1}\!\left(\frac1{sH^2}\right)=-s^{-p}.
\tag{12}
$$
采用标准 Cartier 约定
$$
\mathscr C\left(\sum_j a_jt^j\,dt\right)
=\sum_j a_{pj+p-1}^{1/p}t^j\,dt.
$$
系数在 $\mathbb F_p$ 中时，
$(\mathscr C(f\,dt)/dt)^p=-\partial_t^{p-1}f$。
故 (12) 等价于准确的有理微分恒等式
$$
\boxed{\qquad
\mathscr C\left(\frac{dt}{sH^2}\right)=\frac{dt}{s}.
\qquad}
\tag{13}
$$
这里的 $H$ 次数随 $p$ 变化，但右侧是固定有理微分。

于是存在唯一的 $R_p\in\mathbb F_p(t)$，满足
$$
R_p'=\frac1{sH^2}-\frac{t^{p-1}}{s^p},
\tag{14}
$$
并具有如下规范：

- 在 $H$ 的根处至多有简单极点；
- 在 $t=\pm1/2$ 处极点阶至多 $p-1$；
- 在无穷远点取值为零。

这是一个可构造的有理原函数。由 (13)，(14) 右侧的微分
Cartier 为零。它在 $H$ 的根处极点阶至多二，
在两个 cusp 处至多为 $p$，在无穷远处趋于零。
在分裂这些极点的有限域扩张上作部分分式：
Cartier 为零迫使每个简单极项为零，而其余极项
$(t-a)^{-j}$ 的 $2\le j\le p$ 都可除以单位 $1-j$ 积分。
选无穷远值零即得到所列极点界。该规范唯一：
两个候选之差导数为零，若有极点则其阶必须被 $p$ 整除，
与各处严格小于 $p$ 的界矛盾；余下常数由无穷远值固定。
故构造在 Galois 下不变，下降到 $\mathbb F_p(t)$。

## 5. 惰性处实际 $V$ 的全形式盘闭式

以下取 $p\equiv3\pmod4,\ p\ge7$。
使用[实际整 Frobenius](2026-11-12-integral-gm-frobenius-critical-row.md)
和[完整 Wronskian](2026-11-12-exact-gm-wronskian-and-kummer-derivative-row.md)
的同一 $a,b,U,V$。置
$$
h=H'(0)\in\mathbb F_p^\times.
$$
首先
$$
\frac ba\equiv-h^2\pmod p.
\tag{15}
$$
一个直接核对是：(4) 在 $t=0$ 的左下项为 $h^2$；
特征零周期矩阵的同一迭代项为 $(p+1)![t^{p+1}]K$。
由 $(p+1)!/p\equiv-1$ 及实际整 Frobenius 的
$p[t^{p+1}]K\equiv b/a$，得到 (15)。

把实际 Frobenius 的第二行模 $p$，水平性给
$\mathbf f'+\mathbf f A=0$。
对该式再迭代 $p$ 次，并用非零的 (4)，说明该行必须在
$P_p$ 的左核中。因此它是
$s(H',-H)$ 的一个 $\mathbb F_p[[t^p]]$ 倍数。
这里 $H'(0)$ 是单位，可直接在形式盘中除掉该坐标；
也可先在 $\mathbb F_p((t))$ 中计算后用整初值恢复。
由 $V=-F_{22}/(bs)$ 及 $V'(0)=1$，存在
$v(t)\in1+t\mathbb F_p[[t]]$ 使
$$
V=\frac Hh\,v(t^p)\pmod p.
\tag{16}
$$

令 $\zeta=U/V$。完整 Wronskian 模 $p$ 给
$$
\zeta'
=-\frac1{s^{p+1}V^2}+h^2t^{p-1}.
\tag{17}
$$
写 $C(t)=1/(s\,v(t)^2)$，把 (16) 代入即为
$$
\zeta'=-h^2C(t)^p\frac1{sH^2}+h^2t^{p-1}.
$$
对两边施 Cartier。左边是 exact 微分，Cartier 为零；
右边由 (13) 给 $-h^2C/s+h^2$。所以 $C=s$，
从而 $v^2=s^{-2}$。因为 $p$ 为奇数且 $v(0)=1$，必有
$v=s^{-1}$。因此
$$
\boxed{\qquad
V(t)\equiv\frac{H(t)}{h\,s(t)^p}\pmod p
\quad\text{在整个 }\mathbb F_p[[t]]\text{ 中成立。}
\qquad}
\tag{18}
$$
这不是只到临界次数的 Hasse 近似。

结合 (14)、(17)，得到
$$
\boxed{\qquad
\zeta=-h^2s^pR_p+c(t)^p
\quad\text{于 }\mathbb F_p((t)),
\qquad}
\tag{19}
$$
其中 $c(t)\in t\mathbb F_p[[t]]$ 为奇级数。
理由是两边差的导数为零；$R_p$ 的奇性来自 (14) 的偶性及
无穷远规范。在 $t=0$，
$R_p=-h^{-2}t^{-1}+O(t)$，所以差没有负幂。
$\zeta$ 的奇性再迫使 $c$ 为奇级数。

## 6. 对实际临界行的用途及限制

写 $Z_p=-h^2s^pR_p$，$c_1=[t]c$。
由于 $c$ 为奇级数，
$c(t)^p=c_1t^p+O(t^{3p})$。
完整 Wronskian 稿的模 $p$ 公式因而变为
$$
\boxed{
\mathcal P_p(f)\equiv
\frac12[t^{p-1}]f'Z_p^2
+(c_1+h^2)f_1\pmod p.}
\tag{20}
$$
这个公式把一般 Kummer 行中的周期商替成明确有理函数，
只留下一个来自实际 divided Frobenius 行的标量 $c_1$。
不能由 $p$-curvature 或 Hasse 多项式单独决定该标量。

同时，$c_1$ **不应被识别为中央 Sha 障碍**。
实际中央系数满足
$$
C_{p+1}=\mathcal P_p(M_eV),\qquad M_e=t^4+O(t^6).
$$
这里 $M_eV$ 从 $t^5$ 开始，故 (20) 的 $f_1$ 项本来就没有贡献。
更早的特征零完整精度比较也已经证明，
$U-K$、$V-L$ 的高阶差不影响 $C_{p+1}$。
因此分解 Kummer 共链时出现的 $c_1$ 可以在真实总比较中取消。

本篇保留了三项实际进展：标准规范的非零 $p$-curvature，
全盘公式 (18)，以及带指定 rational 原函数的 (19)–(20)。
这些均为第一层的完整计算。要判断 $C_{p+1}/p\bmod p$，
仍须保留模 $p^2$ 的真实 Kummer–GM 比较；
不能把 $C_{p+1}\equiv0$ 的已知性质升级成完整
$p$-curvature 消失，或把 (18) 直接当作中央非零性。

## 输入与可复核性

- 标准 Legendre 多项式只使用其显式系数、$P_n(1)=1$、
  $P_n(-1)=(-1)^n$ 和二阶微分方程；(2) 的换元写在正文。
- 实际整 crystalline Frobenius、行约定及首个分母比较：
  [整 GM 稿](2026-11-12-integral-gm-frobenius-critical-row.md)，
  §§1–5；其中原始整比较引文为 Stacks Project（2026 年查阅）
  Tags 07MW、07MZ、07N0。
- 实际 Wronskian 和临界泛函：
  [完整导数行](2026-11-12-exact-gm-wronskian-and-kummer-derivative-row.md)，
  式 (6)、(11)、(16)。
- (4) 的一般证明完全由 (5)–(11) 给出；
  不以有限个 $p$ 的矩阵计算作为一般恒等式的依据。
