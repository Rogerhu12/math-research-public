# 三正权上的顺次 MP／真幂 MP 范数比：一个范围澄清

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_continue。

状态：完整有限计算。这里只排除“顺次单步最小逆可由同阶真幂最小逆以只依阶数的常数控制”的新提议，不将这个三位模型当成原连续尾或真实 W 来源的反例。它不否定原相邻 primitive Gram 比较。

取三位 Boolean Hilbert 空间、正权 $(1,\varepsilon,\varepsilon)$，$\varepsilon>0$，令 $D$ 为真实加权删除，$\Omega$ 为单位真空。记
$$
s=1+2\varepsilon^2,
\qquad J_1\Omega=D_1^\dagger\Omega
=s^{-1}(e_{\{1\}}+\varepsilon e_{\{2\}}+\varepsilon e_{\{3\}}).
$$
$D_2:\mathcal H_2\to\mathcal H_1$ 是可逆方阵。顺次单步最小原像
$$
Q_2\Omega=D_2^\dagger D_1^\dagger\Omega
$$
由三个线性方程准确给
$$
Q_2\Omega=
\frac{e_{\{1,2\}}+e_{\{1,3\}}}{2\varepsilon s}
+\frac{2\varepsilon^2-1}{2\varepsilon^2s}e_{\{2,3\}},
$$
所以
$$
\|Q_2\Omega\|^2
=\frac{4\varepsilon^4-2\varepsilon^2+1}
{4\varepsilon^4(1+2\varepsilon^2)^2}.
$$
另一方面，$D^2|_{\mathcal H_2}$ 在同一正交基中的行向量是
$$
(2\varepsilon,2\varepsilon,2\varepsilon^2).
$$
故真幂最小逆 $J_2=(D^2|_{\mathcal H_2})^\dagger$ 满足
$$
\|J_2\Omega\|^2=rac1{4\varepsilon^2(2+\varepsilon^2)},
$$
从而
$$
\boxed{
\frac{\|Q_2\Omega\|^2}{\|J_2\Omega\|^2}
=\frac{(4\varepsilon^4-2\varepsilon^2+1)(2+\varepsilon^2)}
{\varepsilon^2(1+2\varepsilon^2)^2}
\sim\frac2{\varepsilon^2}\longrightarrow\infty.
}
$$
两种链的中间约束不同：$Q_2$ 要求第一次下降恰好等于 $J_1\Omega$，$J_2$ 只要求两次下降后等于 $\Omega$，允许第一次下降多出 primitive 部分。不能把这个自由部分免费去掉。

尤其同一 primitive 真空上的实际相邻比为
$$
\frac{H_1^2}{H_2}
=\frac{4\varepsilon^2(2+\varepsilon^2)}{(1+2\varepsilon^2)^2}
\longrightarrow0,
\qquad H_j=J_j^*J_j.
$$
因此良好的相邻 Gram 比与极坏的顺次／真幂范数比可以同时出现。这个计算只限制上述加强入口；原裸链采用真幂逆的准确首段公式不受影响。
