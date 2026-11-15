# R148：固定曲率轴上最高第四 action 的 sharp 一维符号门

日期：2026-11-15。**已证明。** 只作纸面推导；没有新原式评价或研究计算。依据 [R137](R137-real-fast-pulse-positivity-and-acceleration-PSD.md)、[R140](R140-full-action-multiplier-equivalence-for-real-cost-positivity.md) 和 [R141](R141-affine-character-acceleration-covariance-and-J-positivity.md)。

本稿给出一个既必要又充分的**一维最高导数 action** 判据。它对真实第四成本正性只是必要门；不把这个受限路径类的非负性当作所有水平路径、完整低阶 action 或实际成本半群的正性。

## 1. 真实固定曲率路径与完整最高层

令 $\ell$ 为满足 R141 仿射字符条件的实泛函，权为 $\sigma\in\mathbb Z$，并杀掉 $\mathcal R_8$。完整正规最高层为

$$
L_4^\ell=
A_{hh}^\ell a^2+A_{hk}^\ell ab+A_{kk}^\ell b^2
+(H_1^\ell u+H_2^\ell w)(ub-wa)
+\widehat Q_4^\ell(S;u,w),
$$

其中 $u=h_s,w=k_s,a=h_{ss},b=k_{ss}$，$S=(h,k,\omega)$。这里 $\widehat Q_4$ 必须是完整式

$$
\widehat Q_4=Q_4^v-D_0P_{3v}-\mathcal B_{m_2}(N_2).
\tag{1}
$$

不能用原 $v_4$ 的速度四次部分代替 (1)，也不能仅因已有 pure 投影关系而删掉 $N_2$。

R141 已证明 A/H 的协变。同一论证也给完整速度四次式的协变：先由真实开放路径纤维论证吸收矩阵端项，再按时长分离最高权；A/H 差已为零后，剩下一个对所有水平平端路径积分为零的速度四次式。在任意状态用小幅共线脉冲，除以幅度四次，任意速度方向迫该多项式逐点为零。因此

$$
\widehat Q_4^\ell(S_{H,d};Hu,w)
=H^\sigma\widehat Q_4^\ell(S;u,w),
\qquad S_{H,d}=(Hh,k,(\omega+d)/H).
\tag{2}
$$

现在固定任意实数 $k_0,\omega_0$，只令 $h(s)>0$ 变化。这个路径是真实水平路径，因为 $k_s=0$ 恰给 $\omega_s=0$。frame 和中心线仍按真实 ODE 积分；不要求其自身先闭合，R137 已为这种开放路径支付真实补偿。

令

$$
a(k_0)=A_{hh}^\ell(1,k_0,0),\qquad
 d(k_0)=[u^4]\widehat Q_4^\ell((1,k_0,0);u,0).
$$

由 R141 与 (2)，不依赖 $\omega_0$，且

$$
\boxed{
L_4^\ell|_{k=k_0}
=a(k_0)h^{\sigma-2}(h'')^2
+d(k_0)h^{\sigma-4}(h')^4.
}
\tag{3}
$$

面积项在 $w=b=0$ 时严格为零。下文只研究 (3)。

## 2. 准确平方分解

设 $h\in C^\infty([0,L])$ 为正函数，在两端开邻域分别为常数。两端常数可以不同；所有构造也可与真倒行拼成同 scalar germ 的路径。

定义

$$
A_\sigma[h]=\int_0^L h^{\sigma-2}(h'')^2\,ds,
\qquad
B_\sigma[h]=\int_0^L h^{\sigma-4}(h')^4\,ds.
$$

由真实端部 $h'=0$，

$$
0=\int_0^L\bigl(h^{\sigma-3}(h')^3\bigr)'ds
=(\sigma-3)B_\sigma
+3\int_0^L h^{\sigma-3}(h')^2h''\,ds.
$$

置

$$c_\sigma=\frac{3-\sigma}{3}.$$

逐项展开即得准确身份

$$
\boxed{
A_\sigma-c_\sigma^2B_\sigma
=\int_0^L h^{\sigma-2}
\left(h''-c_\sigma\frac{(h')^2}{h}\right)^2ds
\ge0.
}
\tag{4}
$$

这不是丢掉未控边界项的估计。端点项由平端条件准确为零。

## 3. σ 不为零时的 sharpness

若 $\sigma\ne0$，置

$$w=h^{\sigma/3}>0.$$

准确链式法则给

$$
A_\sigma-c_\sigma^2B_\sigma
=\frac9{\sigma^2}\int_0^L w(w'')^2ds,
\qquad
B_\sigma=\frac{81}{\sigma^4}
\int_0^L\frac{(w')^4}{w}\,ds.
\tag{5}
$$

下面构造实际平端 $w_\varepsilon$，并分别控制两端过渡的积分，而不从“没有等号解”推测 sharpness。

固定一条 $C^\infty$ 正函数 $a:[0,2]\to(0,\infty)$，使 $a(t)=1$ 在 0 的邻域，$a(t)=t$ 在 2 的邻域。例如在中间用一个平坦 cutoff 将 1 与 t 光滑相接，可保持正性。再固定正函数 $b:[1,3]\to(0,\infty)$，使 $b(s)=s$ 在 1 的邻域，$b(s)=2$ 在 3 的邻域。

对 $0<\varepsilon<1/4$ 定义

$$
w_\varepsilon(s)=
\begin{cases}
\varepsilon a(s/\varepsilon),&0\le s\le2\varepsilon,\\
s,&2\varepsilon\le s\le1,\\
b(s),&1\le s\le3.
\end{cases}
\tag{6}
$$

各接缝在开邻域准确等于同一线性函数，所以 (6) 为 $C^\infty$；左右端分别在开邻域等于 $\varepsilon,2$。

左过渡有准确变量换元

$$
\int_0^{2\varepsilon}w_\varepsilon(w_\varepsilon'')^2ds
=\int_0^2a(t)(a''(t))^2dt,
$$

$$
\int_0^{2\varepsilon}\frac{(w_\varepsilon')^4}{w_\varepsilon}ds
=\int_0^2\frac{(a'(t))^4}{a(t)}dt.
\tag{7}
$$

这两个量都有限且与 $\varepsilon$ 无关；其中 $a$ 的正下界已经固定。右过渡由固定 b 给两个固定有限量。中间线性段对第一个积分贡献为零，而对第二个贡献

$$
\int_{2\varepsilon}^1\frac{ds}{s}
=\log\frac1{2\varepsilon}.
\tag{8}
$$

所以若 $h_\varepsilon=w_\varepsilon^{3/\sigma}$，每个 $\varepsilon$ 都给真实光滑正平端 h，且

$$
\frac{A_\sigma[h_\varepsilon]}{B_\sigma[h_\varepsilon]}
=c_\sigma^2+
\frac{\sigma^2}{9}
\frac{O(1)}{\log(1/(2\varepsilon))+O(1)}
\longrightarrow c_\sigma^2.
\tag{9}
$$

这里 h 的上界或下界可以随 $\varepsilon$ 变化；本稿不声称在任意事先固定的紧 h 盒内有同样的 sharp 常数。对每一个有限 $\varepsilon>0$，路径仍严格正且有限。

## 4. σ 等于零时的独立构造

当 $\sigma=0$ 时令 $v=\log h$。不能把 (5) 含 $\sigma^{-1}$ 的式子直接代入零。直接计算与端部 $v'=0$ 给

$$
A_0-B_0=\int_0^L(v'')^2ds,
\qquad B_0=\int_0^L(v')^4ds.
\tag{10}
$$

取 $v_L'$ 在左右各一条固定长度过渡内由 0 平坦升至 1、再由 1 平坦降至 0；中间长度 L 的区间准确等于 1。置 $v_L(0)=0$，$h_L=e^{v_L}$。每个 $h_L$ 在两端开邻域为正的常数。

两条固定过渡给

$$
\int(v_L'')^2=O(1),\qquad
\int(v_L')^4=L+O(1),
$$

因此

$$\frac{A_0[h_L]}{B_0[h_L]}\longrightarrow1=c_0^2.$$

右端 h 值随 L 增长，但每条路径长度和状态值都有限。没有把 L 无穷的极限路径当作实际几何。

结合 (4)、(9)、(10)，对全部正平端非恒常 h，有

$$
\boxed{
\inf\frac{A_\sigma[h]}{B_\sigma[h]}
=\frac{(3-\sigma)^2}{9}.
}
\tag{11}
$$

非恒常 h 的 B 严格正。平方余项等于零时，$\sigma\ne0$ 的 w 为线性函数，或 $\sigma=0$ 的 v 为线性函数；平端迫其恒常。因此 (11) 的最优常数一般不由非恒常平端路径取得。这个未取得性与前面的显式逼近构造共同构成完整 sharp 结论。

## 5. 一维 action 的必要充分符号条件

固定两个实数 a,d。对所有正平端 h，

$$aA_\sigma[h]+dB_\sigma[h]\ge0$$

当且仅当

$$
\boxed{
a\ge0,\qquad d+\frac{(3-\sigma)^2}{9}a\ge0.
}
\tag{12}
$$

**充分性。** 由 (4)，

$$
aA_\sigma+dB_\sigma
=a(A_\sigma-c_\sigma^2B_\sigma)
+(d+c_\sigma^2a)B_\sigma\ge0.
$$

**必要性。** 先在一条固定区间取 $h=h_*+\varepsilon f$，其中 $h_*>0$ 且 $f$ 为非零光滑紧支撑函数。$A_\sigma$ 的首项为严格正的 $\varepsilon^2$ 量，B 为 $O(\varepsilon^4)$；若 a<0，小幅时 action 为负。因此 a 必须非负。

随后用 (9) 或 (10) 的准确平端序列。如果 $d+c_\sigma^2a<0$，则对某条充分靠近最优比值、仍有限且真实的 h，action 严格负。这证明第二个条件，而不要求 inf 被取到。

对固定曲率 $k_0$ 的真实最高层 (3)，条件 (12) 因而准确成为

$$
\boxed{
a(k_0)\ge0,\qquad
 d(k_0)+\frac{(3-\sigma)^2}{9}a(k_0)\ge0.
}
\tag{13}
$$

它对这个固定 $k_0$、仅 h 可变的最高层全部路径既必要又充分。若 $\ell$ 是完整真实成本闭锥的正泛函，R137 已保证所有这类开放路径的最高层积分非负，所以 (13) 必须对每个 $k_0\in\mathbb R$ 成立。

## 6. 权负二的新 J 门及最小后继原式目标

R141 在权 $\sigma=-2$ 给

$$a(k)=a_0+a_2k^2,\qquad a_0=\ell(J).$$

在 $k_0=0$ 定义完整原系数

$$
\mathcal D_0=[h^{-6}]\,[u^4]
\widehat Q_4((h,0,0);u,0).
$$

这里的状态系数按完整真权 $-2$ 理解；其实际表达式必须由 (1) 保留 $N_2$、三阶 IBP 势和原 $Q_4^v$ 共同提取。本稿没有计算这个新原系数。

于是

$$
\boxed{
\ell(J)\ge0,\qquad
\ell\left(\mathcal D_0+\frac{25}{9}J\right)\ge0.
}
\tag{14}
$$

这给一个具体后继问题：消费既有原因子，只形成完整 $\mathcal D_0$，研究其与 J 及已付 lineality 的原式关系。不能先用不完整速度项、纯幂尾投影或模 p 符号代替它。

即使以后得到一个迫权负二正字符在 J 上为零的关系，也必须说明其范围：一般正泛函不一定本身是这个单权字符，其他偶权正字符及完整 action 仍要分别处理。本稿不据 (14) 宣布 J 已可双向支付。

## 7. 物理与逻辑边界

所有构造保持 $k=k_0,\omega=\omega_0$，所以 $\omega_s=k_s/(2h)$ 准确成立。其直接 profile 物理间隙可在固定 $\xi+\omega_0>0$ 的区间保留；真实框架、矩阵及第三成本补偿仍由 R137 对每条有限路径处理，不要求本一维段自身就是闭面或零矩环。

Sharpness 允许 h 范围或长度沿序列扩大，没有证明给定宏观长度、reach、厚度或指定紧控制盒内的同一可达性。

(13) 仅是完整最高导数 action 在真实一维子类上的精确符号判据。它不支付其余速度方向、面积项、R140 的低阶耦合、同一个八矩乘子、完整 ruling、第四成本半群或有限等距族。

