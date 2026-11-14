# 非零锚均值分支：有限柱函数已经允许形式互逆

日期：2026-11-12（UTC+8）。分工：`l2_moments`。

**状态：已证明的路线边界。** R55 零锚均值定理的证明在 $\alpha\beta\ne0$ 时只剩 $FG=\alpha\beta H^2$。本条给出两个明确的低两位柱函数，满足这个形式关系且 $\alpha=\beta=1$。所以不能仅以“有限 Walsh 次数、逐位局部有限”排除该关系。它们并不构成零矩向量对，因其零阶真实矩等于一。

## 1. 记号与例子

保持 R9/R13 的 $a_0,a_1>0$ 和 $W_n=\|A^n\|$，并置

$$
s=\sqrt{a_1/a_0}>0,\qquad
\omega=i\sqrt{a_0a_1}=i a_0s.
$$

以下函数只依赖 $y\bmod4$。按剩余类 $r=0,1,2,3$ 列出其值：

| $r$ | $f(r)$ | $g(r)$ |
|---|---:|---:|
| $0$ | $1$ | $1$ |
| $1$ | $i/s$ | $2-i/s$ |
| $2$ | $1$ | $s^2-2is$ |
| $3$ | $i/s$ | $-is$ |

这些是非零、有限范数的复柱函数，故均属于 $H_{\le2}$（实际上 $f$ 只依赖最低一位），Walsh 支撑当然逐位局部有限。当 $m\ge2$ 时，$f(2^m z)=g(2^m z)=1$，所以两个零柱均值极限均为一，且真实尾涨落都为零。

定义形式幂级数

$$
F(z)=\sum_{n\ge0}\frac{f(n)}{W_n}z^n,\qquad
G(z)=\sum_{n\ge0}\frac{g(n)}{W_n}z^n,\qquad
H(z)=\sum_{n\ge0}\frac1{W_n}z^n.
\tag{1.1}
$$

## 2. 低位生成多项式的精确分解

R13 的无进位乘法给

$$
W_{4q+r}=W_{4q}W_r\qquad(q\ge0,\ 0\le r<4).
$$

因此对任意模四柱函数 $v$，

$$
\frac{\sum_{n\ge0}v(n)z^n/W_n}{H(z)}
=\frac{\sum_{r=0}^3v(r)z^r/W_r}
{\sum_{r=0}^3z^r/W_r}.
\tag{2.1}
$$

所有操作都在形式幂级数环中进行；所消去的尾因子常数项为一。这里

$$
W_0=1,\quad W_1=a_0,\quad W_2=a_0a_1,\quad
W_3=a_0^2a_1,
$$

故分母为

$$
P_1(z)=\left(1+\frac z{a_0}\right)
\left(1+\frac{z^2}{a_0a_1}\right)
=\left(1+\frac z{a_0}\right)
\left(1-\frac z\omega\right)
\left(1+\frac z\omega\right).
\tag{2.2}
$$

对表中的 $f$，直接代入得到

$$
P_f(z)=\sum_{r=0}^3\frac{f(r)}{W_r}z^r
=\left(1-\frac z\omega\right)
\left(1+\frac{z^2}{a_0a_1}\right).
$$

所以

$$
\frac{F(z)}{H(z)}
=\frac{1-z/\omega}{1+z/a_0}.
\tag{2.3}
$$

对表中的 $g$，同样有

$$
P_g(z)=\left(1+\frac z{a_0}\right)^2
\left(1+\frac z\omega\right).
$$

例如 $z^2$ 项乘以 $W_2$ 是
$a_1/a_0+2a_1/\omega=s^2-2is$，$z^3$ 项乘以 $W_3$ 是 $a_1/\omega=-is$，与表格一致。因此

$$
\frac{G(z)}{H(z)}
=\frac{1+z/a_0}{1-z/\omega}.
\tag{2.4}
$$

结合 (2.3)–(2.4)，严格得到

$$
\boxed{F(z)G(z)=H(z)^2.}
\tag{2.5}
$$

两端都是非平凡形式单位，满足 R55 非零锚分支所留下的互逆关系。

## 3. 为什么它不是零矩反例

反射 $r\mapsto-1-r\pmod4$ 将 $r$ 送到 $3-r$。所以

$$
\begin{aligned}
B(f,g)
&=\frac14\bigl[f(0)g(3)+f(1)g(2)+f(2)g(1)+f(3)g(0)\bigr]\\
&=\frac14\bigl[-is+(i/s)(s^2-2is)+(2-i/s)+i/s\bigr]\\
&=1.
\end{aligned}
\tag{3.1}
$$

故它连零阶矩消失都不满足。并且对于 $m\ge2$，两个零柱限制都为常数一，故精确尾配对同样恒为一，不能满足 R55 证明由 $j=0$ 得到的尾配对趋零。

## 4. 剩余缺口

这个例子没有否定一般有限 chaos 矩分离；它只说明 $FG=\alpha\beta H^2$ 可以在十分有限的函数类里真实成立，不能把形式互逆关系本身当成矛盾。

要完成 R55 的 $\alpha\beta\ne0$ 分支，必须同时使用原零矩方程所要求的真实尾配对趋零，以及由非零锚值带来的协方差抵消。有限次数与逐位局部有限本身不阻止零柱上的非退化尾涨落，前一笔记已有明确二阶例子；而本条表明它们也不阻止形式互逆。尚未证明这两个必要机制在同一对向量中不相容。
