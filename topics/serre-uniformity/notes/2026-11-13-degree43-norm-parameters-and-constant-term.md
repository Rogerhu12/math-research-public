# 次数 43 Norm 的参数化、交域及指定 q 剩余值

这是 R191、R201、R202 的计算接口。它给出完整的次数 $43$ 参数空间和无需扩剩余域的局部读取法；**没有取得 Norm 见证，也没有求出 $L$**。所有投影仍为 R201 的同一 $C/\tau$、同一完整 Kummer 根。

## 1. 不能漏掉的二次交域

令 $p=43$，$K=\mathbf Q(i)$，$T=K(A[p])$，

$$
F=T^{\mathbf F_p^\times},\qquad B=K(\mu_p).
$$

$\operatorname{Gal}(T/K)=\mathbf F_{p^2}^\times$，而 $B$ 由 determinant，即有限域 Norm 截出。因此

$$
F\cap B=K(\sqrt{-43}),\qquad
FB=T^{\{\pm1\}},\qquad [FB:F]=21. \tag{43.1}
$$

证明是直接的群计算：标量群与 Norm-one 群的交为 $\{\pm1\}$，两者生成群的指数为 $2$。所以不能把 $FB/F$ 当成次数 $42$ 的域扩张；抽象张量 $F\otimes_KB$ 有两个分量，必须选与同一个 Weil 根相容的分量。

## 2. 不先求最小多项式也有完整的 43 维坐标

R191 给 $a\in B^\times$、$\alpha^{43}=a$，以及 $\sigma$ 在 $B/K$ 的阶 $42$ 作用和提升

$$
\widetilde\sigma\alpha=w\alpha^3,
\qquad \widetilde\sigma^{42}=1.
$$

$3$ 生成 $\mathbf F_{43}^\times$，提升与 $\Gamma=C_{43}$ 交换；$L_q=(B(\alpha))^{\langle\widetilde\sigma\rangle}$。在 $F$ 上，真正的固定子群是 $H=\langle\widetilde\sigma^2\rangle$，阶为 $21$。

每个 $X\in FL_q$ 唯一写成

$$
X=x_0+\operatorname{Tr}_H(c_1\alpha)
       +\operatorname{Tr}_H(c_2\alpha^3),
\quad x_0\in F,\quad c_1,c_2\in FB. \tag{43.2}
$$

其中 $\operatorname{Tr}_H(c\alpha^s)=\sum_{j=0}^{20}\widetilde\sigma^{2j}(c\alpha^s)$。两个和分别使用模 $43$ 的平方指数轨道与非平方指数轨道。每个和内的 $21$ 个 $\alpha$ 指数互异，故 trace 在 $FB\alpha$ 及 $FB\alpha^3$ 上各自单射；两个像及常数项支撑互不相交。维数为 $1+21+21=43$，所以 (43.2) 是满参数化。

把它写成 $X(Y)$，并用 $Y^{43}=a$ 约化，则

$$
N_{FL_q/F}X=\operatorname{Res}_Y(Y^{43}-a,X(Y))\in F. \tag{43.3}
$$

这一等式可以在 $FB$ 上计算；固定性保证最终结果回到 $F$。它避免先构造绝对次数数千的最小多项式，但不自动解 (43.3) 的 Norm 方程。

## 3. 实际整 theta 模型更适于执行

R207 已以 R191 的同一个 Kummer 数据，将中心指数换成 $1,\ldots,42$ 的正代表，构造整的 $\alpha_+$ 和

$$
\theta=\sum_{j=0}^{41}\widetilde\sigma^j\alpha_+.
$$

该点为实数，属于 $L_q^+$。在指定 $q$ 素点上，$42$ 个和项的赋值恰为 $1/43,\ldots,42/43$；最小值唯一，所以 $v_q(\theta)=1/43$。这给次数 $43$ 的 $q$-Eisenstein 多项式 $P_q\in\mathbf Z[Y]$。其逐系数重建、严格高度界和完整执行证书见 R207；本文不替代该证书。

于是可直接在

$$
FL_q=F[Y]/(P_q(Y))
$$

中求解，未知量恰是

$$
X=x_0+x_1\theta+\cdots+x_{42}\theta^{42},\qquad x_j\in F,
$$

Norm 是 $\operatorname{Res}(P_q,X)$。这个表示没有枚举 $q$-挠点，也没有把 $q$-ray 的乘法轨道 Norm 错换成加法同源 Norm。

## 4. Norm 为 q 单位时，剩余值恰是常数项

在 R171 的指定 $q$ 素点，$F_\lambda=\mathbf Q_{q^2}$ 是未分歧二次域。$\theta$ 的赋值为 $1/43$，所以各项的赋值

$$
v_q(x_j\theta^j)=v_q(x_j)+j/43
$$

具有两两不同的小数部分。它们之间不能发生最小赋值抵消。

若 $N_{FL_q/F}X=U$ 且 $U$ 在 $q$ 为单位，则 $v_q(X)=0$。上式立即迫使

$$
v_q(x_0)=0,\qquad v_q(x_j)\ge0\quad(1\le j\le42),
$$

并且

$$
\boxed{\overline X=\overline{x_0}\in\mathbf F_{q^2}^\times.} \tag{43.4}
$$

因此一旦有实际 Norm 见证，读取 R201 所需的剩余值不需要 $\mathbf F_{q^{43}}$ 或更大的有限域。对每个所需 $C$ 共轭都可用相同论证，再施加同一角色和 $\tau$ 投影。

若普通 $X_U,X_V$ 尚未作完整等变投影，必须按原权对所有需要的共轭常数项合成；不能把一个未投影 $x_0$ 的 logarithm 直接命名为 $L$。若已在规范向量 Norm 线上求解，则 (43.4) 可直接与 R201 的根 $(\beta_U,\beta_V\zeta^6)$ 比较。

## 5. 一个确切的缺口，而非局部精度问题

式 (43.4) 只给必要同余 $x_0^{43}\equiv U\pmod q$。这个同余有 $43$ 个根。局部 tame Norm 理论允许相应的局部选择；只有全局 $S$-支撑和同一角色的 Norm 见证才选出 R200 的规范剩余量。提高 $q$ 进精度或从这些根任选一个都不能补上该全局条件。

CM 新短目标 $u=(z-i)/(z+i)$、$\Pi_\chi u_0=15\Pi_\chi u$ 可以降低目标表达式的高度，但也不能被一条对未定元 $z$ 普遍成立的 Norm 恒等式解决：在常数扩张 $L_q(z)/K(z)$ 中，素除子 $z=i$ 的剩余度为 $43$，而 $u$ 的赋值为 $1$，所以 $u$ 不是这个函数域扩张的 Norm。任何成功的特殊恒等式必须使用真实的次数 $44$ CM 关系、完整角色投影或 R191 的特殊 $g$。

当前已完成的是：完整参数空间、准确交域、可认证的 Norm 等式以及指定剩余值的低成本读取。实际 $X$、其外支撑修正与最后 $L$ 仍是待求对象。
