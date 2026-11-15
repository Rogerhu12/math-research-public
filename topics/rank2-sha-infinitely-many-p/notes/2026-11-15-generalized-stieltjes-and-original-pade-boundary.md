# 广义 Stieltjes 正性没有支付原 Padé 高尾

日期：2026-11-15。状态：窄文献核查与一个准确范围排除；不占新 R 编号。R637 指定非零仍未证明。

原 Beta 表达继续是
$$
\Theta(t)^{17}
=\exp\left[-\frac{17}{3}\int_0^1\log(1-tx)
\,d\operatorname{Beta}_{1/3,\,1/2}(x)\right].
$$
此次额外核了 Faraut–Fourati, *Markov–Krein transform*,
Colloquium Math. 144 (2016), 137–156，
[期刊正文](https://www.impan.pl/shop/en/publication/transaction/download/product/91463)，
§3 Proposition 3.1、Theorem 3.2。
它确实允许把每个正权
$$
F_A(t)=\exp[-A\int\log(1-tx)\,d\nu(x)]
$$
写成一个概率测度的广义 Stieltjes 变换
$$
F_A(t)=\int(1-tx)^{-A}\,d\mu_A(x).
$$
因而 $m! [t^m]F_A/(A)_m$ 是真实正矩序列。这是可以使用的呈示；不能把它误称为普通 Markov/Nikishin 完备性。

这里有一个直接障碍：取 $A=2$ 和 $d\mu(x)=dx$ 于 $[0,1]$，则
$$
\int_0^1(1-tx)^{-2}\,dx=\frac1{1-t}.
$$
测度具有整个区间上的严格正密度，但所得函数为有理函数，
高阶 Padé Hankel 子式全退化。因此，单独“有正的广义 Stieltjes 测度”
并不推出普通 Padé 表完美，更不推出原多个不同 $A=17n/3$、
全部 $q_n(t)$ 和不同多项式帽的联合 AT 性。

此外，正矩规范 $m!/(A)_m$ 依赖原 charge $n$。
在原联合矩阵上它不是同一个目标行变换：
原列 $t^kq_n(t)\Theta^{17n}$ 同时混合移位 $k$ 和不同 $A$。
即使某个固定权的实数 Hankel 行列式非零，也没有由此证明它在相应素数下是整单位。

所以本次核查没有把先前普通 Stieltjes 的缺口补成原实际 Schur 的非零。
继续使用 R651 的同一个 $R$、完整两十三行和原像；不以广义正性替代旧 Padé 高尾。
