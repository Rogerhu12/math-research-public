# R170. 全 CM 闭合平面与准确稀疏共振

**状态：已证明。** 日期：2026-11-12。

完整证明：
[全 CM theta–sigma 平面、稀疏共同共振与准确一次除 p](../notes/2026-11-12-full-cm-theta-plane-and-sparse-resonance.md)。

## 固定平面上的真实算子

在 $E_0:y^2=x^3-x$ 上取
$a=\vartheta^4$、$b=\sigma^4$、$w=z^4$。
对每个非零 $\beta\in\mathbb Z[i]$，存在

$$
F_\beta\in\mathbb Z[i,1/2][a,b]^2,\qquad
\deg F_\beta=N\beta,\qquad
F_\beta(a(w),b(w))=(a(\beta^4w),b(\beta^4w)).
$$

它们满足 $F_\alpha F_\beta=F_{\alpha\beta}$，基点 Jacobian 为

$$
\begin{pmatrix}
N\beta&(\beta^4-N\beta)/3\\
0&\beta^4
\end{pmatrix}.
$$

奇范数的准周期与半特征逐项相消，故没有遗漏二次指数。
整性用实际 $\mathbb P^1$ 同源商及无穷远处单位规范支付，
包括除 $N\beta$ 的奇素数。
最小偶范数算子明确为

$$
F_{1+i}(a,b)=((a-b)^2,-4ab),\qquad F_{1+i}^{\circ2}=F_2.
$$

## 准确共振与一次除 p

实际图形 $a=f(b)=1+\sum c_kb^k$ 满足

$$
(\beta^{4k}-N\beta)c_k
=\mathcal R_{\beta,k}(c_1,\ldots,c_{k-1}),
\qquad \mathcal R_{\beta,k}\in\mathbb Z[i,1/2][c_1,\ldots,c_{k-1}].
$$

若 $p\equiv3\pmod4$、$p\ge7$，置
$r=(p+1)/4$、$R_p=(p^2-1)/4$，则

$$
\min_{p\nmid N\beta}v_p(\beta^{4k}-N\beta)
=
\begin{cases}
0,&k\not\equiv r\pmod{R_p},\\
1,&k\equiv r\pmod{R_p}.
\end{cases}
$$

共同共振由整数倍乘的 $p$ 级间距缩到 $p^2$ 级间距。
在共振位置，$\beta=1+2p$ 与 $1+2ip$ 中至少一个给准确估值一，
故没有整数 LTE 中额外的 $v_p(4k-2)$ 损失。
第一个共振为 $r$，第二个为 $pr$。

全部非共振系数是先前真实共振系数的整多项式。
特别在 $k<pr$，

$$
c_k\in\mathcal O_{\mathbb Q_p(i)}[c_r],\qquad
\deg_{c_r}\le\lfloor k/r\rfloor,\qquad
v_p(c_k)\ge-\lfloor k/r\rfloor,
$$

其中 $v_p(c_r)=-1$ 已由 R167 支付。

## 对主问题的准确作用

这是同一固定二维多项式源上的全阶递推；实际拉回次数仍从 $D$
增加到 $(N\beta)D$。在 $p\nmid N\beta$ 时，该拉回是等距饱和
嵌入，沿真实曲线的全部前缀与首个非零 jet 也完全等距
（输出仅乘单位 $\beta^{4k}$）。局部完成中的整逆若按一般
极大理想截断保持第 $k$ 阶，需要次数 $k$ 的代表，不能免费
代替原 $D\asymp\sqrt{k}$ 源。旧分母会通过非线性分子传播。
尚须对全部混合列的共同饱和前缀核给出 R159 的严格预算，
不能用单个系数或单个最佳分母替代该任务。
这里的共振来自 $\beta^{4k}-N\beta$，不在 R41 未扭曲
$\beta^k-1$ 的共同深度定理范围内。
