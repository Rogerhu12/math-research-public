# R782：原两个六次 sigma 截面的完整双线性加法恒等式

日期：2026-11-14。状态：**全部六倍阶 Hirota 常数、显式平方生成函数和原临界系数矩阵已证明。** 同一真本原标签的三个模 $p$ 因子同时非零仍未证明。

本文始终用 R697/R760/R770 的原 $c=0$ sigma、同一曲线和同一两个截面。所得恒等式不是高斯变换后的近似，也不把三同源的 degree $18$ 拉回当作 degree $6$ 空间的自作用。

## 1. 原函数与双线性导数

固定
$$
E_0:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad
x'=2y,\quad y'=3x^2,
$$
$$
\sigma(z)=z+O(z^7),\qquad
(\log\sigma)''=-x.
\tag{782.1}
$$
令
$$
F=x\sigma^6,\qquad
G=-xy\sigma^6,\qquad
\mathscr W=(x^3-4)\sigma^6.
\tag{782.2}
$$
三者均为原 degree $6$ theta 截面，局部规范为
$$
F=z^4\left(1+\frac4{35}z^6+\cdots\right),\qquad
G=z\left(1-\frac6{35}z^6+\cdots\right),
$$
$$
\mathscr W=1-\frac{18}{5}z^6+\cdots.
\tag{782.3}
$$
这里 $\mathscr W$ 不表示 R698 中用于 Weierstrass zeta 的另一个同名字母。

对整数 $r\ge0$ 定义普通 Hirota 双线性导数
$$
\mathcal D^rF\cdot G
=
\sum_{i=0}^r(-1)^{r-i}\binom ri F^{(i)}G^{(r-i)}
=
\left.
(\partial_{z_1}-\partial_{z_2})^rF(z_1)G(z_2)
\right|_{z_1=z_2=z}.
\tag{782.4}
$$
因此
$$
F(z+t)G(z-t)
=
\sum_{r\ge0}\frac{t^r}{r!}\mathcal D^rF\cdot G(z).
\tag{782.5}
$$

**主恒等式。** 对所有 $m\ge0$，存在原规范下的有理数 $c_m$，使
$$
\boxed{\mathcal D^{6m}F\cdot G=c_mFG,}
\tag{782.6}
$$
并且所有常数由同一个显式平方给出：
$$
\boxed{
\sum_{m\ge0}\frac{c_m}{(6m)!}t^{6m}
=\mathscr W(t)^2
=(x(t)^3-4)^2\sigma(t)^{12}.
}
\tag{782.7}
$$
等价地，
$$
\boxed{
\frac16\sum_{\epsilon\in\mu_6}
 F(z+\epsilon t)G(z-\epsilon t)
=F(z)G(z)\mathscr W(t)^2.
}
\tag{782.8}
$$
特别地
$$
c_0=1,\qquad c_1=-5184,\qquad
\mathcal D^6F\cdot G=-5184FG.
\tag{782.9}
$$
此外有原第五阶平方恒等式
$$
\boxed{\mathcal D^5F\cdot G=-120\mathscr W^2.}
\tag{782.10}
$$

这些首先是特征零中的完整解析或形式恒等式；不是只到某个素数阶的观察。

## 2. 每个六倍阶商为何必为常数

原 sigma 的准周期公式为
$$
\sigma(z+\omega)
=\varepsilon(\omega)
 \exp\!\left(\eta_\omega(z+\omega/2)\right)\sigma(z).
$$
因为取第六次幂，$F$ 和 $G$ 有相同的 theta 乘子
$$
F(z+\omega)
=e^{6\eta_\omega(z+\omega/2)}F(z),\qquad
G(z+\omega)
=e^{6\eta_\omega(z+\omega/2)}G(z).
\tag{782.11}
$$
同时平移 $z_1,z_2$ 时，二者乘子的乘积只依赖 $z_1+z_2$；差导数
$\partial_{z_1}-\partial_{z_2}$ 将这个因子视为常数。因此
$$
H_r=\frac{\mathcal D^rF\cdot G}{FG}
\tag{782.12}
$$
是原 $E_0$ 上的椭圆函数。分子是完整 degree $12$ 截面，故其商的可能极点只在 $FG$ 的零点，极点阶至多为相应的零阶。导数阶增大不会增大这项极点上界。

用 sigma 的零除子及 $x,y$ 的除子，准确得到
$$
\operatorname{div}_0(FG)
=
5[O]+2[Q_+]+2[Q_-]+\sum_{T\in E_0[2]\setminus\{O\}}[T],
\tag{782.13}
$$
其中 $Q_\pm=(0,\pm\sqrt{-1})$。总次数为 $5+2+2+3=12$。

对 $\epsilon\in\mu_6$，原 CM 规范给
$$
\sigma(\epsilon z)=\epsilon\sigma(z),\quad
x(\epsilon z)=\epsilon^{-2}x(z),\quad
y(\epsilon z)=\epsilon^{-3}y(z).
$$
所以
$$
F(\epsilon z)=\epsilon^4F(z),\qquad
G(\epsilon z)=\epsilon G(z),
\qquad
H_r(\epsilon z)=\epsilon^{-r}H_r(z).
\tag{782.14}
$$
当 $r=6m$ 时，$H_r$ 为 $\mu_6$ 不变函数。

现在逐点处理 (782.13) 的全部可能极点：

- $O$ 的稳定子为 $\mu_6$，不变函数在该点的阶是 $6$ 的倍数；可能极点阶至多 $5$，故无极点。
- $Q_+,Q_-$ 各自被 $\mu_3$ 固定。不变函数的阶是 $3$ 的倍数，而可能极点阶至多 $2$，故无极点。
- 每个非零二挠点被 $[-1]$ 固定。不变函数的阶为偶数，而可能极点阶至多 $1$，故无极点。

这里用的是局部商映射的分歧指数，不能只凭全局权重宣称无极点。所有点已覆盖，故 $H_{6m}$ 是光滑完备曲线上的无极点函数，只能为常数。这证明 (782.6)。由于原 $F,G$ 的 Taylor 系数为有理数，取任意非零 Taylor 系数比较，也得到 $c_m\in\mathbb Q$。

## 3. 从原点第五阶项确定全部常数的生成函数

将 (782.5) 对 $t$ 的六个单位根平均，再用 (782.6)，有
$$
\frac16\sum_{\epsilon\in\mu_6}F(z+\epsilon t)G(z-\epsilon t)
=
FG(z)\,K(t),\qquad
K(t)=\sum_{m\ge0}\frac{c_m}{(6m)!}t^{6m}.
\tag{782.15}
$$
由 (782.3)，$FG(z)=z^5+O(z^{11})$，所以右侧的 $z^5$ 系数恰为 $K(t)$。

$F$ 为偶函数，$G$ 为奇函数。于是
$$
[z^5]\bigl(F(z+t)G(z-t)\bigr)
=
-\frac1{5!}\mathcal D^5F\cdot G(t).
\tag{782.16}
$$
按 (782.14)，$\mathcal D^5F\cdot G$ 本身已为 $\mu_6$ 不变截面：
两个原截面的总特征为 $5$，五阶差导数恰将它消去。因此 (782.16) 在六次平均中不再改变，得到
$$
K(t)=-\frac1{120}\mathcal D^5F\cdot G(t).
\tag{782.17}
$$
负号来自 $G(z-t)=-G(t-z)$，不是任选平方根的符号。原点第五阶前的系数全由 (782.15) 自动消失，故取该系数没有除以一个未知的前导项。

## 4. 完整计算第五阶双导数

记 $a=x,b=-xy$，仍在原曲线上用 $D_z$。只需以下三个有限代数恒等式：
$$
\begin{aligned}
\mathcal D a\cdot b&=3x^4,\\
\mathcal D^3a\cdot b&=96x^5+48x^2,\\
\mathcal D^5a\cdot b&=6000x^6+6720x^3-1920.
\end{aligned}
\tag{782.18}
$$
它们分别由 (782.4) 及 $x'=2y,y'=3x^2,y^2=x^3-1$ 直接展开；没有除以 $x$、$y$ 或 sigma 值。

另一方面，设 $\ell=\log\sigma$。由 $\ell''=-x$ 与 $x''=6x^2$，
$$
\begin{aligned}
\frac{\sigma(t+z)^6\sigma(t-z)^6}{\sigma(t)^{12}}
&=\exp\left(6\ell''(t)z^2+\frac12\ell^{(4)}(t)z^4+O(z^6)\right)\\
&=1-6x(t)z^2+15x(t)^2z^4+O(z^6).
\end{aligned}
\tag{782.19}
$$
将它与 $a(t+z)b(t-z)$ 相乘，准确取第五阶系数，可得
$$
-\frac{\mathcal D^5F\cdot G}{120}
=
\sigma^{12}\left(
-\frac{\mathcal D^5a\cdot b}{120}
+x\,\mathcal D^3a\cdot b
-15x^2\mathcal D a\cdot b\right).
\tag{782.20}
$$
代入 (782.18)，括号化简为
$$
\begin{aligned}
&-50x^6-56x^3+16+96x^6+48x^3-45x^6\\
&\hspace{30mm}=x^6-8x^3+16=(x^3-4)^2.
\end{aligned}
$$
这同时证明 (782.7)、(782.8)、(782.10)。由 $\mathscr W^2=1-\frac{36}{5}t^6+\cdots$，
$$
c_1=6!\left(-\frac{36}{5}\right)=-5184,
$$
与单独取 (782.3) 的六阶双导数一致。

也可把原第十二阶常数完全写出。由原 Weierstrass 方程及两次积分，
$$
x=z^{-2}+\frac17z^4+\frac1{637}z^{10}+\cdots,
$$
$$
\sigma^6=z^6\left(
1-\frac1{35}z^6+
\left(\frac1{2450}-\frac1{14014}\right)z^{12}+\cdots\right).
$$
于是
$$
\mathscr W=1-\frac{18}{5}z^6+\frac{324}{1925}z^{12}+\cdots,
\qquad
\mathscr W^2
=1-\frac{36}{5}z^6+\frac{25596}{1925}z^{12}+\cdots.
$$
故
$$
\boxed{
c_2=\frac{12!\,25596}{1925}
=2^{12}3^9\cdot79=6369103872,\qquad
\mathcal D^{12}F\cdot G=c_2FG.
}
\tag{782.20a}
$$
两个常数 $c_1,c_2$ 在所有 $p\ge41$、$p\equiv5\pmod6$ 均为单位：唯一新增的素因子 $79\equiv1\pmod6$ 不在范围内。这只是两个已明确计算的常数的统一单位结论，不是全体 $c_m$ 的单位断言。

## 5. 与原三同源、三倍公式的相容性

这里只用于核对同一 sigma 规范，不用来代替前四节的证明。原除法公式给
$$
\sigma(sz)=s\,x(z)\sigma(z)^3,\qquad
\sigma(3z)=3x(z)(x(z)^3-4)\sigma(z)^9,
\qquad s^2=-3.
\tag{782.21}
$$
故
$$
\mathscr W(z)=\frac{s}{3}\frac{\sigma(3z)}{\sigma(sz)},\qquad
\mathscr W(z)^2=-\frac13
 \left(\frac{\sigma(3z)}{\sigma(sz)}\right)^2.
\tag{782.22}
$$
比值在原点的常数是 $1$，与 (782.3) 相符。这里保留 $s/3$，不选择新的复共轭方向。两个公式中的可能二次指数因子均由原 $\sigma=z+O(z^7)$ 规范固定为零；不能在计算中再自由换 $\sigma$ 的 Gaussian。

特别注意，$[s]^*\mathcal O(6[O])$ 的次数是 $18$，不是 $6$。本篇真正返回原两个截面的算子是 (782.8) 的完整双变量恒等式；它不是将 $[s]^*$ 错认成原 degree $6$ 空间上的正定自算子。

## 6. 原临界总阶上的有限精确矩阵

现在令 $p=6N+5\ge41$。保留 R770 的平坦参数及低阶约化
$$
F=z^4f(z^6),\qquad
G=z\,g(z^6),\qquad
f(v)=\sum_{i=0}^{N-1}f_i v^i,\quad
g(v)=\sum_{i=0}^{N-1}g_i v^i
\pmod{v^N}.
\tag{782.23}
$$
同样写
$$
\mathscr W(z)^2=k(z^6),\qquad k(v)=\sum_{\ell\ge0}k_\ell v^\ell,\quad k_0=1.
\tag{782.24}
$$
这里所需的 $f_i,g_i,k_\ell$，$0\le i,\ell\le N-1$，全在合法整范围内。对 $k_\ell$ 也可直接使用 R698：
$$
\mathscr W=(1-4w)T(w),\qquad z=uZ(w),\quad w=u^6.
\tag{782.25}
$$
$r\le N-1$ 的换参、乘方及逆换参仅用原 $T,Z$ 至该阶；分母 $r,6r+1,6r-1$ 及 $6$ 均为 $p$ 单位。因而本节的约化没有跨越原 $T_{N+1}$ 的首个 $p$ 分母。

令
$$
d=p-6=6N-1,\qquad
a_i=f_i g_{N-1-i}\quad(0\le i<N),
\tag{782.26}
$$
并定义完全显式的整数矩阵
$$
\boxed{
K_{\ell i}
=[X^{6\ell}](1+X)^{6i+4}
                     (1-X)^{6(N-1-i)+1},
\quad 0\le\ell,i<N.
}
\tag{782.27}
$$
这里的 $X$ 是独立多项式变量。

从 (782.8) 取齐次总阶 $d$，再取 $z^{d-6\ell}t^{6\ell}$，逐项得到
$$
\boxed{
\sum_{i=0}^{N-1}K_{\ell i}f_i g_{N-1-i}
=
k_\ell\sum_{\substack{r+s=N-1-\ell\\r,s\ge0}}f_r g_s.
}
\tag{782.28}
$$
这是特征零中的精确有限式，在上述合法范围内也可约化模 $p$。

证明时左侧的六次平均只筛掉 $t$ 指数不被 $6$ 整除的项；保留下来的指数 $6\ell$ 的平均值恰为 $1$。右侧 $FG=z^5(fg)(z^6)$，故
$$
d-6\ell=5+6(N-1-\ell),
$$
给出 (782.28) 的准确指标。特别地没有将 $w=u^6$ 与 $v=z^6$ 混用。

第一行恒为
$$
K_{0i}=1,
\tag{782.29}
$$
于是 $\ell=0$ 是通常卷积恒等式；其余行是原两个截面的新增双线性约束。本文不假定矩阵 $K$ 可逆，也不从有限小素数矩阵的秩猜测其全素数秩。

## 7. 同标签、Legendre 因子与本原筛选仍须逐项保留

R770 的实际非端点标签为
$$
h=6a+1=6i+7,\qquad a=i+1,\quad
0\le i<N,\quad (h,p+1)=1,
$$
并且
$$
U_hV_h=f_i g_{N-1-i}=a_i.
\tag{782.30}
$$
在原 $p$-进嵌入中保留 $s^2=-3$、$\alpha^3=4$、原 $\zeta$，以及
$$
B=(-1)^{N+1}\binom{3N+2}{2N+1}\in\mathbf F_p^\times.
$$
原有限范数因子是 $P_{6i+6}(1/s)$，故 R770 的原配对仍为
$$
\mathcal B_p
=
\sum_{i=0}^{N-1}
 \mathbf1_{(6i+7,p+1)=1}\,
 P_{6i+6}(1/s)\,a_i.
\tag{782.31}
$$
所有原平方常数仍完整保持 R770(770.17)，即
$$
\left(\frac{p^2M_{2,h}}{\zeta}\right)^2
=
\left(
1296\alpha s B^5P_{6i+6}(1/s)a_i
\right)^2
\pmod p.
\tag{782.32}
$$
本文没有从这个平方等式选择符号。

(782.28) 作用于完整向量 $(a_i)$；其右侧是低阶普通卷积与 $k_\ell$ 的乘积。它并不自动保留 (782.31) 的本原对角筛选或 Legendre 对角权。事实上矩阵第一行 (782.29) 已同时混合全部标签。若人为将任意对角权 $\operatorname{diag}(d_i)$ 放在两侧，则交换子的第一行是
$$
[\operatorname{diag}(d_i),K]_{0i}=d_0-d_i.
\tag{782.33}
$$
因此不能在未核交换关系时，把“先施行完整加法恒等式”与“先筛实际标签”互换。即使某个特殊 $p$ 的本原筛选恰为恒等，原 Legendre 权和同标签条件也仍须检查。

## 8. 新桥的准确范围

本篇得到的是原两个截面的完整加法恒等式，故比单独的六阶方程更强。所有六倍阶双导数由一个原 degree $6$ 截面的平方统一控制；原临界 $i+j=N-1$ 上也已有准确矩阵 (782.28)，没有只留下一个不匹配的形式权重。

但以下步骤仍未得到证明：

1. 不能由 $c_1=-5184$ 为单位，推任意高阶 $c_m$ 或指定 $k_\ell$ 为单位。
2. R765 的非零截断残差位于总指标 $N+1$；(782.28) 的目标位于 $N-1$。新的完整恒等式可以用于研究其间关系，但尚未证明一个保留 (782.31) 的可逆下降。
3. (782.28) 本身没有证明存在同一个真本原 $h$ 使 $P_{h-1}(1/s)U_hV_h\ne0$，也未证明 $\mathcal B_p\ne0$。
4. 即使以后证明三因子单位，所得仍首先是原标量 Abel 分量的赋值与零点结论，不能直接替代原二次高度条件。

本篇没有新素数窗口或新数值证书；(782.18) 的有限多项式运算和全部恒等式均由显示的微分关系逐项证明。

## 依赖

- R697：原 sigma 六次截面、普通导数与固定规范。
- R698：$u=x^{-1/2}$ 中的原 $T,Z$ 以及完整整性截断。
- R760、R770：原同标签两系数、真实 Legendre 范数与全部平方常数。
- R765：截断非零残差的实际指标及其合法约化边界。
