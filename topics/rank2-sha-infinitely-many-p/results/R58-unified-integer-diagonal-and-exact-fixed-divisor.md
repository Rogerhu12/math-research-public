# R58. 普通与惰性的统一整数对角及准确固定除子

日期：2026-11-12。**状态：全部陈述已证明；未证明首层对角无穷次非零。**

R57给同一个整数序列
$$
A_D(z)=\sum_{r\ge1}D^{r-1}a_r\frac{z^{4r}}{(4r)!},\qquad a_1=24.
$$
只在 $D=17$ 时将它解释为本课题的实际中央theta因子。

## 1. 两类素数共用一个充分条件

对任意 $p\ge7,p\ne17$，置
$$
\epsilon_p=\left(\frac{-1}{p}\right),\quad
m_p=p-\epsilon_p,\quad r_p=m_p/4,\quad e_p=(1-\epsilon_p)/2.
$$
则
$$
\boxed{p\mid a_{r_p},\qquad
p^{e_p-1}b_{m_p}\equiv-17^{r_p-1}\frac{a_{r_p}}p\pmod p.}
\tag{1}
$$
因此
$$
\boxed{
p^2\nmid a_{r_p}
\quad\Longrightarrow\quad
\Sha(E_{17}/\mathbb Q)[p^\infty]\text{有限}.
}
\tag{2}
$$
(2)是首层充分条件；$p^2\mid a_{r_p}$ 不说明初级部分无限。

**证明。** 普通情形由R51有 $b_{p-1}\in p\mathbb Z_p$；
惰性情形由R50/R51有 $b_{p+1}\in\mathbb Z_p$。
而 $v_p(m_p!)=e_p$，Wilson恒等式给
$m_p!/p^{e_p}\equiv-1\pmod p$。
把 $m_p!b_{m_p}=17^{r_p-1}a_{r_p}$ 代入即得(1)。
右端非零时，普通真实斜率是单位，或惰性 $b_{p+1}$ 为单位；
分别应用R51、R50的已证有限性判据，得(2)。
例外 $2,3,5,17$ 不在本结论范围内。

## 2. 整条序列的固定除子恰为24

有
$$
\boxed{\gcd_{r\ge1}a_r=24.}
\tag{3}
$$

**证明八的整除。** R57真实乘积的四个sigma因子只有 $4k+1$ 次幂。
每个四重Hurwitz卷积项的multinomial系数有
$$
v_2\binom{4(\sum k_j+1)}{4k_1+1,4k_2+1,4k_3+1,4k_4+1}
=4+\sum_js_2(k_j)-s_2(\sum_jk_j+1)\ge3.
$$
再乘theta因子仍是整数二项式卷积，故全部系数被8整除。

**证明三的整除。** 在模3的Hurwitz环中记 $e_n=z^n/n!$。
R57系统给 $u^{(3)}=-6Du^2u'\equiv0$，因此
$u=e_1$、$L=2De_3$。
递推 $t_n=2D\binom{n-1}3t_{n-4}$ 给
$$
\vartheta_D=e_0+2De_4+2D^2e_8,\qquad
\sigma_D=e_1+De_5\pmod3.
$$
由于 $-7\pm24i\equiv-1\pmod3$，真实乘积中的四个sigma因子满足
$$
\sigma_D^2\sigma_{-D}^2
=(e_1^2-D^2e_5^2)^2=(2e_2)^2=0\pmod3.
$$
这里 $e_5^2=252e_{10}=0$、$(2e_2)^2=24e_4=0$。
故24整除每个 $a_r$；$a_1=24$ 使gcd准确等于24。

这只计算固定除子，不是随p移动对角的赋值上界。
例如 $a_2=65184$ 不被9整除，不能把(1)推广成整个 $4r+1$ 总整除 $a_r$。

## 3. Euler原函数的实际非目标分母

记 $h_m=m!b_m\in\mathbb Z$。
对每个目标普通 $p\ge13,p\ne17$，有
$$
\boxed{h_{4p}\equiv24\mathsf H_p^4\not\equiv0\pmod p,}
\tag{4}
$$
从而 $C_{4p}=h_{4p}/(4p)$ 的约分后分母**恰为p**。

**证明。** R51的实际总测度给
$\Omega_p^mh_m=\int_{\mathbb Z_p}x^m\,d\nu_p$。
用 $x^{4p}\equiv x^4\pmod p$、
$\Omega_p^{1-p}\equiv\mathsf H_p\pmod p$ 和 $h_4=24$ 得(4)。
由(3)，$4\mid h_{4p}$；又由(4)，$p\nmid h_{4p}$，所以分母恰为p。

因此固定整个Euler原函数 $\int_0^z A_{17}(w)dw/w$ 的Hurwitz系数
有无穷多个奇分母。这里 $4p\equiv4\pmod{p-1}$，是非目标tame权，
不影响R56的特殊中央权整性或其完备有限证书。

完整证明与规范见
[统一整数对角、固定除子及真实分母](../notes/2026-11-12-universal-integer-prime-diagonal-and-fixed-divisor.md)。
所有全指标结论由上述恒等式证明，不由有限扫描推断。
