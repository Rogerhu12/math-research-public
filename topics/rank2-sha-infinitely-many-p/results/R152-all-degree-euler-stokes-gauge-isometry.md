# R152：Euler 中央规范的全次数 jet 等距

日期：2026-11-12。可信度：**已证明，根代理完整独审通过。**

## 结论

对实际 $A$ 的固定 Euler 原函数
$\mathscr H(z)=\int_0^zA(v)dv/v$，令 $w=z^4$、$H_4=4\mathscr H$。
每个惰性 $p\ge7$ 的 R62 分解有
$\mathcal S_0=-J_{A,p}'(0)$，且 $\mathcal S_0/(p+1)\in p\mathbb Z_p$。

对任意 $C\in\mathcal O$，平移 $H_4\mapsto H_4+4C$ 在真实
$\mathcal O(D)$ 单项式格上是整幺三角变换。因此**全部 $D,k$** 的
饱和前缀格及 jet 评价范数准确保持；基点、$dw$ 和仿射线丛平凡化
没有非单位成本。取 $C=J_{A,p}'(0)/(p+1)$ 可以局部消去中央
$E_0$ 项，但使 $\mathscr H(0)=C$。原 $A$ 及原 $J_{A,p}'(0)$ 未改变；
恢复零初值就恢复原中央项。

对 $Y=4\mathscr H/f_0$，必须保留额外坐标 $R_0=1/f_0$，才能使用
真实整 shear $Y\mapsto Y+4CR_0$。其全部列为

$$
w^aY^bR_0^c,\quad a+b+c\le D;
\qquad
w^a(4K)^bE_0^cG_0^{D-b-c}
$$

是准确等距的共同输出规范。这个结论不反向当作原 $Y$ 平面等距。

实际 $f_0$ 的零点轨道上，$A$ 非零且 Euler 原函数按
$e^{\gamma n^2L^2}/n^2$ 增长，排除 $f_0,\mathscr H$ 在
$\mathbb C(w)$ 上的代数关系。故新增 ambient 的闭包确为三维，
源维数为 $\binom{D+3}{3}$，相应尺度是 $D\asymp k^{1/3}$。

## 复侧与范围

在 $w$ 平面增长阶数至多 $1/2$。Herblot 的准确严格门槛分别为：
有理平面 $(w,H_4)$ 的 $\alpha<1$；$\mathbb Q(i)$ 平面 $(w,Y)$ 的
$\alpha<1/2$；$\mathbb Q(i)$ 三维图像的 $\alpha<2/3$。
后两项用 $\mathbb P^r_{\mathbb Q(i)}$ 作为 $\mathbb Q$-scheme，
保留次数二闭点及全部共轭。本文没有证明这些 arithmeticity 上界。

本结果排除仅由局部可选中央 Stokes 规范直接降低相应 jet 范数的推理；
不排除利用固定全局初值与原 ODE 的新约束。R151 的真正混合列和
无界深带上界仍未完成。

完整证明：
[Euler Stokes 规范与全次数 jet 等距](../notes/2026-11-12-euler-stokes-gauge-and-all-degree-jet-isometry.md)。
