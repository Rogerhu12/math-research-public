# 原 theta 幂的 Beta 表达与直接 Nikishin 识别的范围

日期：2026-11-14。**状态：下述割线变号计算已证明；没有由此证明实际 Hermite–Padé 系统不正规，也没有得到原第二余类非零。** 本笔记不占结果编号。

## 1. 原函数的正 Beta 表达

R434 (2) 给同一个原函数
$$
L(t)=\Theta(t)^{17},\qquad
\log L(t)=\frac{17}{3}\sum_{n\ge1}
 \frac{(1/3)_n}{(5/6)_n}\frac{t^n}{n}.
$$
设 $\mu$ 为 $[0,1]$ 上的 Beta$(1/3,1/2)$ 概率测度，即
$$
d\mu(x)=\frac{x^{-2/3}(1-x)^{-1/2}}{B(1/3,1/2)}\,dx.
$$
逐项积分 $\int x^n\,d\mu=(1/3)_n/(5/6)_n$，得到原点归一的准确解析延拓
$$
\boxed{
L(t)=\exp\!\left(-\frac{17}{3}\int_0^1
 \log(1-tx)\,d\mu(x)\right)}
\tag{1}
$$
于 $\mathbf C\setminus[1,\infty)$，其中对数采用从 $t=0$ 延拓的分支。
这是 Markov–Krein 型的对数积分表达；它本身不是
$L(t)=\int (x-t)^{-1}d\sigma(x)$ 的定号 Cauchy 表达。

## 2. 原幂的完整割线有反复变号

对每个实数 $u>1$，令
$$
M(u)=\mu((1/u,1)),\qquad
A(u)=\exp\!\left(-\frac{17}{3}\int_0^1
                    \log|1-ux|\,d\mu(x)\right)>0 .
$$
内部的对数奇点可积。上半平面趋近割线时，
$1-(u+i0)x$ 在 $x>1/u$ 上的辐角为 $-\pi$，故
$$
\boxed{
L(u+i0)^n=A(u)^n
          \exp\!\left(\frac{17n\pi i}{3}M(u)\right).}
\tag{2}
$$
$M$ 连续严格增加，由 $0$ 趋于 $1$。于是
$$
\operatorname{Im}L(u+i0)^n
=A(u)^n\sin\!\left(\frac{17n\pi}{3}M(u)\right)
\tag{3}
$$
在每个 $M(u)=3j/(17n)$、$0<j<17n/3$ 处严格变号。
变号次数为 $\lceil17n/3\rceil-1$；特别 $n=1$ 已有五次。

原有限格使用
$$
\mathscr R=(1+8t)L(t),\qquad
q_n(t)=
\frac{\{t(7+4t+16t^2)\}^{A_n}(t-1)^{B_n}}
 {(1+8t)^{C_n}} .
$$
对 $u>1$，$q_n(u)(1+8u)^n u^k$ 严格为正。因此每个
$n\ge1$ 的原基函数 $t^kq_n(t)\mathscr R(t)^n$
在整条割线上保留 (3) 的所有变号。
添加在该实段取实值的有理函数或多项式，也不会改变该虚部。

任一有限定号实测度的普通 Cauchy 变换，在上半平面的虚部恒有一个符号
（取决于分母采用 $x-z$ 还是 $z-x$）。故这些原幂函数不能直接
等同于这类定号测度的 Cauchy 变换，甚至加一个实有理项也不能完成这种识别。

## 3. 正规性定理的准确适用边界

Fidalgo Prieto 与 López Lagomasino 的 Nikishin 完美性结果使用
定号生成测度、其实际支撑区间以及递归 Cauchy 乘积构造。
其中 AT 条件同时量化所有规定次数帽的实多项式乘子。
这不是仅由 $L$ 在一个实区间上单调、或由 (1) 的 $\mu\ge0$
就得到的性质。

本次核对的主源：

- U. Fidalgo Prieto, G. López Lagomasino,
  *Nikishin systems are perfect. The case of unbounded and touching supports*,
  Journal of Approximation Theory 163 (2011), 779–811,
  [DOI 与定义、定理页面](https://doi.org/10.1016/j.jat.2011.03.004)。
  核对了该页的 Nikishin 生成测度及 AT 定义；没有把旧文献中关于一般多指标的开放陈述沿用为现状。
- J. Faraut, F. Fourati, *Markov–Krein transform*,
  Colloquium Mathematicum 144 (2016), 137–156,
  [期刊页及摘要](https://www.impan.pl/en/publishing-house/journals-and-series/colloquium-mathematicum/all/144/11/91463/markov-krein-transform)，
  DOI 10.4064/cm6235-10-2015。
  该变换的正性不等于本题原幂族及其全部多项式乘子的 AT 正规性。

(2)–(3) 排除的是最直接的“每个原幂就是定号 Markov 函数”识别。
它们**没有排除**某个更复杂的分段支撑、基变换或不同定理能够证明实际系统正规。
但那一步必须重新支付整个原 $\mathcal W_D$、全部 $q_n$ 和不等多项式次数帽；
现有证明没有提供它。因此不能借这一正 Beta 表达宣称连续 Padé 子式非零、
真饱和旗标成本改善，或 R597 的同一 $R$ 第二余类非零。
