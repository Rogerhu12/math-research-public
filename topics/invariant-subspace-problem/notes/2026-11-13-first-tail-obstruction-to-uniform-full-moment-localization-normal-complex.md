# 真湮灭矩的有限块定位：一次尾禁止统一全矩算子范数方案

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065。

**状态：已证明的方法边界。** 对 R235 的实际比较算子
$T_m/h_m$，即使允许任意有限物理位集合上的任意有界算子，
其全空间算子范数定位误差乘上完整矩映射的统一成本，
仍至少为 $\sqrt{2^m}/144$。
因此不能通过“先在算子范数中截成有限块，再对所有正常密度用统一迹范数界”
来关闭真湮灭者的完整块残量。
这不限制密度专属估计，也不限制保留无限尾的实际右因子。

## 1. 准确比较对象和一次真空系数

对 $m\ge1$，
$$
q=2^m,\qquad a_j=(j+1)^{-2}\quad(j\ge m),
$$
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad
T_m=I_{<m}\otimes D_m^q,\qquad
h_m=\langle T_m1,1\rangle.
\tag{1.1}
$$
$D_m$ 的和在算子范数绝对收敛。
记 $e_k=e_k((a_j)_{j\ge m})$。
纯幂展开给
$$
T_m=q!\sum_{|A|=q}a_AE_A,\qquad
h_m=q!\,2^{-q}e_q>0.
$$
令
$$
\pi_m(A)=a_A/e_q,\qquad
p_j=\pi_m\{A:j\in A\}.
\tag{1.2}
$$
由于 $E_j\Omega_+=(\Omega_+-\chi_j)/2$，准确真空源为
$$
\frac{T_m1}{h_m}
=\sum_{|A|=q}\pi_m(A)
 \prod_{j\in A}(1-\chi_j).
\tag{1.3}
$$
其一次 Walsh 系数因此准确为
$$
\boxed{
\left\langle\frac{T_m1}{h_m},\chi_j\right\rangle=-p_j.
}
\tag{1.4}
$$
此处没有将整个无限源截断。

## 2. 对称多项式比值的两个统一界

置
$$
C_m=\frac{e_{q-1}}{e_q}.
$$
由 $p_j=a_je_{q-1}(a_{\ne j})/e_q$，
有 $p_j\le\min(1,C_ma_j)$。
又 $\sum_jp_j=q$，所以
$$
q\le\sum_{n\ge1}\min(1,C_m/n^2)
\le\int_0^\infty\min(1,C_m/x^2)\,dx
=2\sqrt{C_m}.
$$
最后的积分比较使用被积函数单调不增。
故
$$
C_m\ge q^2/4.
\tag{2.1}
$$

反向利用准确计数：
$$
q e_q
=\sum_{|G|=q-1}a_G\sum_{j\notin G}a_j.
$$
删去 $q-1$ 个最大权后，剩余总和仍至少为
$$
\sum_{j\ge m+q-1}(j+1)^{-2}
\ge\frac1{m+q}.
$$
因此
$$
C_m\le q(m+q)\le2q^2.
\tag{2.2}
$$
结合即得
$$
\boxed{q^2/4\le C_m\le2q^2.}
\tag{2.3}
$$
这里只使用 $m\le q=2^m$。

## 3. 尾部包含概率的明确下界

基本对称系数的对数凹性
$$
e_{q-1}^2\ge e_{q-2}e_q
$$
在 R235 正尾耦合稿中已经由加入一个变量的直接归纳证明。
由此
$e_{q-2}/e_{q-1}\le C_m$。
所以
$$
\begin{aligned}
e_{q-1}(a_{\ne j})
&=e_{q-1}-a_je_{q-2}(a_{\ne j})\\
&\ge e_{q-1}(1-a_jC_m).
\end{aligned}
$$
若 $j\ge2q$，(2.3) 给 $a_jC_m\le1/2$。
因此
$$
\boxed{
\frac{q^2}{8(j+1)^2}
\le p_j\le\frac{2q^2}{(j+1)^2}
\qquad(j\ge2q).
}
\tag{3.1}
$$

同时 $p_j$ 随 $j$ 单调递减。
确切地，去掉 $i,j$ 后记剩余对称系数为 $E_k$，
则
$$
p_i-p_j
=\frac{(a_i-a_j)E_{q-1}}{e_q}.
\tag{3.2}
$$
因为 $a_j$ 递减，结论成立。
这保证任意挑选 $n$ 个物理位，也不比保留前 $n$ 个尾位更能缩小遗漏的一次平方和。

## 4. 任意有限位算子的全空间误差

令 $B$ 为任意 $n$ 个物理位，可非连续，也可包含第 $m$ 位之前的位。
令 $K_B$ 为只作用于这些位的任意有界算子，
在其他位张量恒等。
不要求 $K_B$ 属于交换代数。

因为 $K_B1$ 仅有支持在 $B$ 内的 Walsh 系数，
(1.4) 和正交性给
$$
\begin{aligned}
\tau_{m,B}
&:=\left\|\frac{T_m}{h_m}-K_B\right\|\\
&\ge\left\|\frac{T_m1}{h_m}-K_B1\right\|\\
&\ge\left(\sum_{j\ge m,\ j\notin B}p_j^2\right)^{1/2}.
\end{aligned}
\tag{4.1}
$$
由单调性 (3.2)，遗漏平方和至少为从 $m+n$ 开始的尾。
令
$L=\max(m+n,2q)$，利用 (3.1) 和积分比较，
$$
\sum_{j\ge L}p_j^2
\ge\frac{q^4}{64}
 \sum_{j\ge L}(j+1)^{-4}
\ge\frac{q^4}{192(L+1)^3}.
$$
又 $L+1\le n+2q+1$，得到
$$
\boxed{
\tau_{m,B}\ge
\frac{q^2}{8\sqrt3\,(n+2q+1)^{3/2}}.
}
\tag{4.2}
$$
它同时覆盖任何有限位位置和任何有限块算子，而非某个固定的截断公式。

## 5. 完整矩的统一成本永远付不清这一误差

任意 $n$ 位块的统一纯矩映射成本为
$$
K_n=(4+2\sqrt2)^{n/2},
$$
即 $\|X_u^0\|\le K_n\|u\|$。
[块密度接口稿](2026-11-13-positive-density-block-moments-and-annihilator-dual-certificates-normal-complex.md)
中把全空间算子误差传给完整密度矩，须付 $\lambda\tau_{m,B}K_n$。

对全部整数 $n\ge0$，
$$
K_n\ge2^n\ge\frac12(n+1)^{3/2}.
$$
第二个不等式可由 $n=0,1$ 直接验证，
再用 $((n+2)/(n+1))^{3/2}<2$ 对 $n\ge1$ 归纳。
又
$n+2q+1\le(n+1)(2q+1)$，
所以 (4.2) 给
$$
\tau_{m,B}K_n
\ge\frac{q^2}{16\sqrt3(2q+1)^{3/2}}
\ge\frac{\sqrt q}{144}.
$$
因此
$$
\boxed{
\inf_{\substack{B\ {\rm finite}\\K_B\ {\rm supported\ on}\ B}}
\left\|\frac{T_m}{h_m}-K_B\right\|K_{|B|}
\ge\frac{2^{m/2}}{144}\longrightarrow\infty.
}
\tag{5.1}
$$

(5.1) 限制的是这一统一估计方法：
不能先要求相对算子范数定位，再把维数费用
$K_{|B|}$ 当成 harmless 的常数。
它不证明具体真密度的误差
$\|K_B^*m_B-r^0_{m,B}\|$ 必有相同下界；
密度专属配对可能产生更强的消去。


### 5.1 即使采用最优统一正密度常数也不能定位

此障碍并非仅由所取的 $K_n$ 上界过粗导致。
令 $C_n$ 是对全部正迹一块密度成立的最优常数，即
$$
C_n=\sup_{\sigma\ge0,\ \operatorname{Tr}\sigma=1}
 \|\mathcal L_B(\sigma)\|.
$$
取 $\sigma=\chi_B\otimes\chi_B$。
对每个 $F\subseteq B$，
$\operatorname{Tr}(\sigma D_F^*)=2^{|F|}$，故
$$
C_n\ge
\left(\sum_{F\subseteq B}4^{|F|}\right)^{1/2}
=5^{n/2}\ge2^n.
$$
第5节只用统一常数至少为 $2^n$，所以同一证明给
$$
\boxed{\tau_{m,B}C_n\ge\sqrt q/144.}
\tag{5.2}
$$
因此任何将全空间定位误差乘以一个对全部正密度统一适用的
迹范数至完整矩常数的方案，都面临这个下界。
该结论仍不限制只在真湮灭密度上证明的专属误差估计。

## 6. 真湮灭矩的剩余接口

R235 的真实全右测试向量可以不定位 $T_m$，
直接保留非正交叉约化
$\operatorname{Tr}_{B^c}(\rho T_m)/h_m$。
它的实际全矩界仍成立。
或者，需要在真湮灭方程和正性下，
以比统一迹范数更精细的密度专属范数控制块外尾。

本稿没有排除这两条路线，
也没有构造真正常湮灭者。
它只关闭了一个现在可以明确反证的全空间有限块定位方案。
普通 Hilbert ISP 未完成。

依赖：

- [R235 正尾耦合、固定基数分布和对数凹性](../results/R235-appendix-tail-couplings-almost-everywhere-continuity-and-bounded-obstruction.md)；
- [R235 真湮灭者全部实际右测试](../results/R235-appendix-annihilator-tail-coupling-energy-and-right-tests.md)；
- [块密度映射、完整残量和正性对偶](2026-11-13-positive-density-block-moments-and-annihilator-dual-certificates-normal-complex.md)。
