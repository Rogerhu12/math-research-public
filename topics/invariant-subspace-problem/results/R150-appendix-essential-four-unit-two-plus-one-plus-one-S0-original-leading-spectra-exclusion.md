# R150 附录：S=Af=0 两参数图的全部原 z 首项零谱排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本附录完整排除 $S=A_f=0,L\ne0,(I,H)\ne(0,0)$ 两参数图中原参数曲线 z 首项系数为零的全部谱，即 $\lambda=1$、$\lambda=2$ 及 $10\lambda^3-22\lambda^2+19\lambda-5=0$。结论不覆盖一般 lambda 参数，不宣布整个 S 层或非零均值层为空。

关联：[原 U 值图](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)、[S0 有限参数覆盖](R150-appendix-essential-four-unit-two-plus-one-plus-one-U-value-S0-finite-parameter-cover.md)、[本定理自含原源码](../notes/2026-11-26-unit211-S0-original-leading-spectra-QQ-347c.py)和[实际执行回执](../notes/2026-11-26-unit211-S0-original-leading-spectra-execution-347c.json)。

## 1. 同一个原图及已付单位

使用已经登记的 U 值图、原 P1 一次式和 $S=A_f=0$ 覆盖。共同规范 $p+q=2$；整个 $u=1$ 分支已另行排除。三值互异图写成

$$
s=2\lambda-3,\quad z=(h-1)(k-1),\quad
\Delta=s^2-4z,\quad d^2=\Delta,
$$

$$
A=2\lambda^2-2\lambda+1,\quad
C=-4\lambda^2+5\lambda-2,\quad
R=3-4\lambda,\quad j=2\lambda-1,
$$

$$
D=sC-Az,\quad l=D/z^2,\quad T=C/z,\quad
w=\lambda-1-T,\quad B=2T-ls.
$$

设

$$
\begin{aligned}
I_2={}&2(4\lambda-1)CD\\
&+z\{2C(1-\lambda)R-2(4\lambda^2-7\lambda+2)D\}\\
&+z^2\{-2\lambda C+sjR\},
\\
H_3={}&D\{[4\lambda(1-\lambda)+2\lambda z]z-4jD-2sC\}\\
&-2(\lambda-1)Cz^2+2C^2z-2jRz^3+4jDz^2,
\\
D_\theta={}&2zI_2+sH_3,\qquad
\theta=H_3/D_\theta .
\end{aligned}
$$

原量由同一二次代数给出：

$$
\begin{aligned}
b&=\frac l2+\frac{B}{2\Delta}d,&
c&=\frac l2-\frac{B}{2\Delta}d,\\
p&=1+\theta d,&q&=1-\theta d,\\
h&=1+\frac s2+\frac d2,&
k&=1+\frac s2-\frac d2.
\end{aligned}
$$

记

$$
u=l+\theta B,\quad Q=1-\theta^2\Delta,\quad
V_2=2u-lQ,
$$

$$
2P_0=(2-3u)V_2-Qu+2u^3,\qquad
A_f=R-z\left(l+\frac{2u(1-u)}{Q}\right).
$$

源码保留 $d^2=\Delta$ 的两个根，直接核验全部三个原 U 矩及 $bcpq,u,P_0$ 的定义。没有把一个抽象 Gram 解当作物理解。

本图全部使用的非零量只有

$$
\lambda,\ z,\ \Delta,\ I_2,\ H_3,\ D_\theta,\ Q,\ bc,\ P_0,\ u,\ u-1.
\tag{1}
$$

这里 $I_2\ne0$ 等价于当前图的 $L\ne0$；$H_3\ne0$ 来自 $p\ne q$；$D_\theta\ne0$ 来自共同规范 $p+q=2$ 的有效性。$I=H=0$、值碰撞及 $u=1$ 均已有单独结论。所有有理式分母逐个只用 (1) 的多项式分子作 gcd 剥除，余下非零有理常数；没有额外首项除法。

从 $A_f$ 的既约分子中只剥 (1) 的因子，得到固定归一化的

$$
F(\lambda,z)=0,\qquad
(\deg_\lambda F,\deg_z F)=(15,6).
$$

它有 90 项。实际序列化 SHA-256 为

```
97dd885ca63f981ae892f45e2edf7b2cf65d50f86d520e8e379ad3f4b86f7bd4
```

可复算源码给出上述公式及确定性的归一化程序，因而不以省略的数值样本定义 F。

## 2. 原 mean、最高阶和第二梯度仍完整保留

源码先按原 Frobenius 乘法、原迹和同一个 K 生成全部九条剩余条件：三条 mean、三条最高阶条件、三条第二梯度条件。B/C 两式依共轭变成偶部与奇部。原 $E_0=N_0-\lambda P_0=0$ 在唯一合法的线性图中用于解原 r,s；完整 K、原 jets 和同一 Frobenius 迹均未替换。

全部九条有理系数先保留并得到与已执行 Chow 源一致的输入身份

```
0e9b97510ea6611e122210a58a51b18b266174d6813011a10237174522ccab3c
```

本证明只需原 P1 一次式与两个原 mean 二次式；未使用的条件仍是原系统的一部分。用必要子系统证明无解足以排除完整原系统，并没有宣称必要条件是充分条件。

令原 P1 的齐次一次式为 $\ell=(a,b,c)$，两个 mean 二次式的对称矩阵为 M,N。定义

$$
\mathcal A=\ell^\mathsf T\operatorname{adj}(M)\ell,\qquad
\mathcal C=\ell^\mathsf T\operatorname{adj}(N)\ell,
$$

$$
\mathcal B
=\ell^\mathsf T[\operatorname{adj}(M+N)-\operatorname{adj}(M)
-\operatorname{adj}(N)]\ell,
\qquad
\mathcal C_{M,N}=\mathcal B^2-4\mathcal A\mathcal C.
\tag{2}
$$

每个原有限公共点必使 (2) 为零。源码在一个独立 QQ 多项式环中，令两个二次式及一次式的常数项分别由任意公共有限点 $(f_0,t_0)$ 决定，直接展开并核验 (2) 恒为零。故 (2) 的必要性不依赖 P1 的 f 或 t 系数非零，也不丢失一次式首项为零的点。

三条原 Chow 多项式全部重建并与原成功执行逐个核对身份：

| 原二次式对 | SHA-256 |
|---|---|
| E1、EB 偶部 | 61fc40f181e395a6181d5bd060a9280a6b0aef955eff334763667faecc8e3405 |
| E1、EB 奇部 | f2f6f2b4c0212b94fd5d702d63cfaff58f7306700c62026bb06ae26c22fa7f7b |
| EB 偶部、EB 奇部 | 3a9a4b43224163a7133fc21ec8de17887f2a04a3f59a77e832ab21438c35a04c |

所有清分母与共同因子剥除仍只使用 (1)。

## 3. 精确首项谱及全部原纤维返回

对第 1 节固定归一化 F，实际 QQ 因式分解给出

$$
\operatorname{lc}_zF
=\frac{1}{24576}(\lambda-1)(\lambda-2)
\left(10\lambda^3-22\lambda^2+19\lambda-5\right)^2.
\tag{3}
$$

源码先用实际 F 的 z 六次系数构造一元多项式，再验证除以 (3) 所示非恒定因子后恰为非零 QQ 常数，最后独立分解该实际系数。完整不可约因子次数为 $1,1,3$；没有略去任何原首项谱。

对每个不可约因子 $\phi$，在

$$
K_\phi=\mathbb Q[\lambda]/(\phi)
$$

中将原 F、三条原 Chow 和全部 (1) 的单位多项式直接代入。所有运算都在 $K_\phi[z]$ 中完成。一次域系数求逆均计算实际 extended gcd，验证

$$
a(\lambda)s(\lambda)+\phi(\lambda)t(\lambda)=g\in\mathbb Q^\times
$$

及商域内 $a(s/g)=1$。因此没有把零系数当作可逆，也没有假设二次 d 代数不可约。

令 g 为原 F 的特化。只有当它与一个已付单位多项式有非平凡 gcd 时，才从 g 中反复剥去该 gcd。随后逐条与原 Chow 作真实域上一元 gcd。任何原合法点必须是最后 g 的根。实际结果如下：

| lambda 谱 | 原 F 的 z 次数 | 剥去的已付因子 | 第一原 Chow 返回后的共同 z 次数 | 真正域逆身份数 |
|---|---:|---|---:|---:|
| $\lambda=2$ | 5 | 无 | 0 | 58 |
| $\lambda=1$ | 5 | H3 的一次共同因子 | 0 | 60 |
| $10\lambda^3-22\lambda^2+19\lambda-5=0$ 的全部三个根 | 5 | 无 | 0 | 57 |

三种谱在第一对 E1、EB 偶部的原 Chow 返回后已各得单位多项式 1。lambda=1 被剥的 H3 因子违反原 $p\ne q$；没有剥任何新因子。三次谱是在整个三次商域内处理，包含所有共轭根，未选实根或数值近似。

于是这三个原首项谱没有满足原系统的点。注意结论来自原 F 与原必要 Chow 的共同 gcd 为 1；单独比较两条平面曲线没有公共分量，并不足以给出本结论。

## 4. 实际执行身份与范围

冻结源码 Git blob：

```
e46f3d212336d4944e613174f1f11112875b580a
```

源码 17725 字节，SHA-256：

```
6f8aeb452357198e255ddfa110b1cb8df44cd2620103f27374d8156e83e84992
```

真实公开执行：

- 源提交：85f8c05de49cde33e3cf78fe29c0657cc38a36c3。
- Actions run 45821311603，job 139913974571，工作流结论 success。
- 源执行 20.080736 秒；driver 20.160298919 秒；峰值子进程 RSS 187400 KiB；退出码 0。
- stdout 6209 字节，SHA-256 d843d5234742694f6087683c01dff8f853e287a8c3c461b673cc1b8bc8b398d8。
- Python 3.12、python-flint 0.9.0；源码自身记录全部输入身份、因子、原纤维返回和真实域逆次数。
- 执行前实际 pull 后，根 README 与课题 README blob 分别为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、fef43bdf8690f2eec4751d85784a266eacdd0322；规则未变。

本结论与此前全六条 QQ lambda 结果式的末格式化失败是两次不同执行。旧执行已完成的六条结果式不被重新标为成功，也不以本次局部谱排除替代一般 lambda 候选的原纤维返回。下一项仍是 $S=A_f=0,L\ne0,(I,H)\ne(0,0)$ 图上其余全部 lambda 候选。
