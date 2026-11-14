# 一个整数序列的两类素数对角、准确固定除子及真实分母

日期：2026-11-12。状态：以下结论已证明。
沿用 R57 的统一整数
$$
A_D(z)=\sum_{r\ge1}D^{r-1}a_r\frac{z^{4r}}{(4r)!},
\qquad a_r\in\mathbb Z,\qquad a_1=24,
$$
及 R51 的实际 $A_{17}(z)=\sum b_mz^m$。
本文的首层条件均为充分证书，不声称它们对无穷多个素数命中。

## 1. 普通与惰性的同一个整数对角

取 $p\ge7$、$p\ne17$，置
$$
\epsilon_p=\left(\frac{-1}{p}\right),\quad
m_p=p-\epsilon_p,\quad r_p=\frac{m_p}{4},\quad
\nu_p=\frac{1-\epsilon_p}{2}.
\tag{1}
$$
这里 $\nu_p=0$ 是普通情形，$\nu_p=1$ 是惰性情形；
本节的 $\nu_p$ 仅为这个 $0/1$ 记号，不是旧椭圆单位深度。

R51 给普通情形的 $b_{p-1}\in p\mathbb Z_p$；
R50 的完整有符号比较给惰性情形的 $b_{p+1}\in\mathbb Z_p$。
又有
$$
v_p(m_p!)=\nu_p,\qquad
\frac{m_p!}{p^{\nu_p}}\equiv-1\pmod p.
\tag{2}
$$
普通时这是 Wilson 定理；惰性时
$(p+1)!/p=(p+1)(p-1)!\equiv-1$。
因而两类同时满足
$$
\boxed{p\mid a_{r_p},}
\tag{3}
$$
以及准确的首层同余
$$
\boxed{
p^{\nu_p-1}b_{m_p}
\equiv-17^{r_p-1}\frac{a_{r_p}}p\pmod p.
}
\tag{4}
$$
(4) 两边都整；左侧在普通时为 $b_{p-1}/p$，
惰性时为 $b_{p+1}$。

所以同一个整数条件给出两类充分证书：
$$
\boxed{
p^2\nmid a_{(p-\epsilon_p)/4}
\quad\Longrightarrow\quad
\Sha(E_{17}/\mathbb Q)[p^\infty]\text{有限}.
}
\tag{5}
$$
证明：在普通情形，(4) 给 $v_p(b_{p-1})=1$，
由 R51 得实际 $J_p'(0)$ 为单位；在惰性情形，(4) 给
$b_{p+1}$ 为单位，应用 R50/R51。

反之，$p^2\mid a_{r_p}$ **只说明这个首层证书没有命中**。
普通有限性的准确等价式仍是 $J_p'(0)\ne0$；
它允许导数非零但被 $p$ 整除。
特别地，不能把 (5) 写成有限性的充要条件。
$p=2,3,5,17$ 均不在本节断言范围内；
不能因为小素数另有数值样例就删掉这些接口例外。

## 2. 整条序列的固定除子恰为 $24$

**命题。**
$$
\boxed{\gcd(a_1,a_2,\ldots)=24.}
\tag{6}
$$

### 2.1 八的整除

R57 的乘积为
$$
A_D=\vartheta_D\vartheta_{16D}\,
\sigma_D^2\sigma_{(-7+24i)D}\sigma_{(-7-24i)D}.
\tag{7}
$$
每个 sigma 只有 $4k+1$ 次幂，且 Hurwitz 系数均为高斯整数。
在四个 sigma 因子的任一卷积项中，设指数为
$n_j=4k_j+1$，总指数为 $n=4(\sum k_j+1)$。
该项的整数 multinomial 系数满足
$$
\begin{aligned}
v_2\binom{n}{n_1,n_2,n_3,n_4}
&=\sum_{j=1}^4s_2(n_j)-s_2(n)\\
&=4+\sum_{j=1}^4s_2(k_j)-s_2\left(\sum k_j+1\right)
\ge3.
\end{aligned}
\tag{8}
$$
这里 $s_2$ 是二进制位数和，使用
$s_2(a+b)\le s_2(a)+s_2(b)$ 以及 $s_2(a+1)\le s_2(a)+1$。
再乘两个 theta 因子只增加整数二项式卷积，不会消去这个因子 $8$。
故 (7) 的每个 Hurwitz 系数都被 $8$ 除，特别 $8\mid a_r$。

### 2.2 三的整除

在 Hurwitz 环中记 $e_n=z^n/n!$，乘法为
$e_ae_b=\binom{a+b}a e_{a+b}$。
对 R57 的系统
$$
u''=-2Du^3,\qquad L'=Du^2,\qquad\vartheta_D'=L\vartheta_D
$$
模 $3$ 化简。因为
$u'''=-6Du^2u'\equiv0$，
且 Hurwitz 求导是系数移位，故
$$
u\equiv e_1,\qquad L\equiv2D e_3.
$$
若 $t_n=\vartheta_D^{(n)}(0)$，则
$$
t_n\equiv2D\binom{n-1}{3}t_{n-4}\pmod3.
$$
初值 $t_0=1$，非四倍指标为零；
$\binom{11}3=165\equiv0$ 使第十二项及其后所有四倍项消失。
因此
$$
\vartheta_D\equiv e_0+2D e_4+2D^2e_8,\qquad
\sigma_D=u\vartheta_D\equiv e_1+D e_5\pmod3.
\tag{9}
$$
而 $-7\pm24i\equiv-1\pmod3$。四个 sigma 因子的乘积于是为
$$
\begin{aligned}
\sigma_D^2\sigma_{-D}^2
&\equiv\bigl((e_1+D e_5)(e_1-D e_5)\bigr)^2\\
&=\bigl(e_1^2-D^2e_5^2\bigr)^2
=(2e_2)^2=0\pmod3.
\end{aligned}
\tag{10}
$$
此处 $e_5^2=\binom{10}5e_{10}=252e_{10}=0$，
$(2e_2)^2=24e_4=0$。
故 $3\mid a_r$ 对全部 $r$ 成立。结合 (8) 得 $24\mid a_r$；
再由 $a_1=24$ 得到准确的 (6)。

这没有给出随指标移动的素数赋值上界。
例如 $a_2=65184$ 不被 $9$ 除；
从 (3) 的素数邻项规律不能推断整个 $4r-1$ 或 $4r+1$
总是整除 $a_r$。

## 3. 整个 Euler 原函数确实有无穷多个奇分母

R56 的特殊权序列
$C_{p,n}=(m_n-1)!b_{m_n}$ 已被准确比较到普通中心导数；
R57 又证明一般
$$
C_m=(m-1)!b_m=h_m/m,\qquad h_m=m!b_m\in\mathbb Z.
$$
但不能把所有 $C_m$ 都宣称为整数。
这里有一个对**每个目标普通素数**成立的精确反证：
$$
\boxed{\text{$C_{4p}$ 的约分后分母恰为 $p$.}}
\tag{11}
$$

证明使用实际总测度，不需要假设 $J_p'(0)$ 非零。
R51 的整 Amice 变换给
$$
\Omega_p^m h_m=\int_{\mathbb Z_p}x^m\,d\nu_p(x).
$$
由于 $x^{4p}\equiv x^4\pmod p$ 对所有 $x\in\mathbb Z_p$ 成立，
且 $\Omega_p^{1-p}\equiv\mathsf H_p\pmod p$，有
$$
h_{4p}\equiv\Omega_p^{-4(p-1)}h_4
\equiv24\mathsf H_p^4\not\equiv0\pmod p.
\tag{12}
$$
普通 Hasse invariant $\mathsf H_p$ 为单位，目标 $p\ge13$。
另一方面由 (6)、$h_{4p}=17^{p-1}a_p$，$4\mid h_{4p}$。
因此 $h_{4p}/(4p)$ 约分后分母正好是 $p$，证明 (11)。

等价地，固定整函数
$$
\int_0^z\frac{A_{17}(w)}w\,dw=\sum_{m\ge1}\frac{b_m}{m}z^m
$$
的 Hurwitz 系数有这些真实奇分母。
这是非目标权 $4p\equiv4\pmod{p-1}$ 的作用；
它与 R56 的 $m_n\equiv0\pmod{p-1}$ 完全相容。
没有把这个 Hurwitz 分母结论扩张为对所有其他代数化方法的排除。

### 依赖及复核

只用已证 R50、R51、R56、R57（均为 2026-11-12）以及上面的
整数二项式与有限域恒等式。
[整数递推脚本](../scripts/check-theta-hurwitz-integers.py)
可复核任意有限前缀；(3)–(12) 的全指标结论由本文证明，
不由有限扫描推断。
