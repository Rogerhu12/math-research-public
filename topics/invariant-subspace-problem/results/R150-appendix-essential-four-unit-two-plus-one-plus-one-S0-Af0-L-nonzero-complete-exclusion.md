# R150 附录：S=Af=0、L 非零一般图的完整 QQ 排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：本附录完整关闭 $S=A_f=0,L\ne0,(I,H)\ne(0,0)$ 的原两参数图。与已登记的 $S=A_f=0$ 值碰撞排除、M6 全部有限纤维排除及整个归一化 $u=1$ 排除合并，得到整个 $S=A_f=0,L\ne0$ 范围无原临界点。$L=0$ 和 $S=0,A_f\ne0$ 仍由各自剩余任务处理；没有宣布整个非零均值层或普通 ISP 完成。

来源：[原参数覆盖](R150-appendix-essential-four-unit-two-plus-one-plus-one-U-value-S0-finite-parameter-cover.md)、[值碰撞排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-U-value-S0-collision-exclusion.md)、[M6全部例外](R150-appendix-essential-four-unit-two-plus-one-plus-one-U-value-S0-M6-exclusion.md)、[全部原首项谱](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-original-leading-spectra-exclusion.md)、[自含源码](../notes/2026-11-26-unit211-S0-minimal-QQ-original-fibers-347c.py)和[实际成功回执](../notes/2026-11-26-unit211-S0-Af0-L-nonzero-complete-execution-347c.json)。

## 1. 原图、完整覆盖与先前首项谱

共同规范 $p+q=2$，并使用已登记的原 U 值矩、原 N(V) 与原 P1 一次式。设

$$
s=2\lambda-3,\quad z=(h-1)(k-1),\quad\Delta=s^2-4z,\quad d^2=\Delta,
$$

$$
A=2\lambda^2-2\lambda+1,\quad C=-4\lambda^2+5\lambda-2,\quad
R=3-4\lambda,\quad j=2\lambda-1,
$$

$$
D=sC-Az,\quad l=D/z^2,\quad T=C/z,\quad
w=\lambda-1-T,\quad B=2T-ls.
$$

令

$$
\begin{aligned}
I_2={}&2(4\lambda-1)CD
+z[2C(1-\lambda)R-2(4\lambda^2-7\lambda+2)D]
+z^2[-2\lambda C+sjR],\\
H_3={}&D\{[4\lambda(1-\lambda)+2\lambda z]z-4jD-2sC\}\\
&-2(\lambda-1)Cz^2+2C^2z-2jRz^3+4jDz^2,\\
D_\theta={}&2zI_2+sH_3,\qquad\theta=H_3/D_\theta.
\end{aligned}
$$

完整值和权重为

$$
b=\frac l2+\frac{B}{2\Delta}d,\quad
c=\frac l2-\frac{B}{2\Delta}d,\quad
p=1+\theta d,\quad q=1-\theta d,
$$

$$
h=1+s/2+d/2,\qquad k=1+s/2-d/2.
$$

两根 d 都保留。记

$$
u=l+\theta B,\quad Q=pq=1-\theta^2\Delta,\quad V_2=2u-lQ,
$$

$$
2P_0=(2-3u)V_2-Qu+2u^3,\qquad
A_f=R-z\left(l+\frac{2u(1-u)}{Q}\right).
$$

本图允许剥除的全部单位仅为

$$
\lambda,\ z,\ \Delta,\ I_2,\ H_3,\ D_\theta,\ Q,\ bc,\ P_0,\ u,\ u-1.
\tag{1}
$$

所有分母都逐个用这些原非零量验证。$I_2=0$ 是另保的 $L=0$；$H_3=0$ 违反 $p\ne q$；$D_\theta=0$ 不属于已付共同规范。值碰撞、$I=H=0$ 及 $u=1$ 均已有完整独立排除。

从 $A_f$ 既约分子中只剥 (1)，得到固定 90 项多项式 F，次数为

$$
(\deg_\lambda F,\deg_zF)=(15,6).
$$

其身份为

```
97dd885ca63f981ae892f45e2edf7b2cf65d50f86d520e8e379ad3f4b86f7bd4
```

原 z 首项系数恰为

$$
\operatorname{lc}_zF
=\frac{(\lambda-1)(\lambda-2)J_3(\lambda)^2}{24576},
\qquad J_3=10\lambda^3-22\lambda^2+19\lambda-5.
\tag{2}
$$

已经正式登记的三首项谱附录（提交 a8213d2429c498852dde5602ccb9019251f01ff6）完整关闭 $\lambda=1,2$ 及 J3 的所有根。本次不重跑这些已闭纤维。

## 2. 四条实际 QQ 投影足以给出全部有限候选

源码从原 Frobenius 乘法、原迹、完整 K 和原 jets 重新生成全部九条条件：三条 mean、三条最高阶和三条第二梯度。原基点 $E_0=0,N_0=\lambda P_0$ 只用于有全局合法分母的 r,s 解；B/C 条件保留完整二次 d 代数，变为偶部和奇部。

全部九条原有理式的统一输入 SHA-256 为

```
0e9b97510ea6611e122210a58a51b18b266174d6813011a10237174522ccab3c
```

这与先前已实际执行的原九式及 Chow 源逐字节一致。

设原 P1 齐次一次式系数为 $\ell$，任意两条原二次条件的对称矩阵为 M,N。原有限公共点必使

$$
\begin{aligned}
a&=\ell^\mathsf T\operatorname{adj}(M)\ell,\qquad
c=\ell^\mathsf T\operatorname{adj}(N)\ell,\\
b&=\ell^\mathsf T[\operatorname{adj}(M+N)
-\operatorname{adj}(M)-\operatorname{adj}(N)]\ell,\\
\mathcal C_{M,N}&=b^2-4ac
\end{aligned}
\tag{3}
$$

为零。源码在独立 QQ 多项式环中将两个二次式及一次式的常数项用任意公共有限点表示，直接验证 (3) 恒为零。没有除原 P1 的 f 或 t 系数，故所有降次和首项零点均保留。

将 (3) 只剥 (1) 后，按以下次序计算完整 $\operatorname{Res}_z(F,\mathcal C)$：

| 实际原二次式对 | QQ lambda 结果式次数 | 当前全部已算结果式 gcd 次数 |
|---|---:|---:|
| E1、EB 偶部 | 1568 | 1568 |
| E1、N1 | 1601 | 1350 |
| E1、EB 奇部 | 1556 | 1340 |
| EB 偶部、EB 奇部 | 1511 | 1320 |

四条 Chow 的 SHA-256 依次为

```
61fc40f181e395a6181d5bd060a9280a6b0aef955eff334763667faecc8e3405
6ab877ac7aade4fd5b7f37c61b80cbcfd6e98913a21d41fb3f8893d9963f3aed
f2f6f2b4c0212b94fd5d702d63cfaff58f7306700c62026bb06ae26c22fa7f7b
3a9a4b43224163a7133fc21ec8de17887f2a04a3f59a77e832ab21438c35a04c
```

设当前四条完整结果式的 gcd 为 G。每一个原合法候选的 lambda 必是 G 的根，即使投影包含无穷远或分母退化产生的额外根，此必要性仍成立。

旧执行曾完整算过六条结果式，观察到共同次数 1320，但在最后格式化调用不支持的 zcontent 时退出 1。本次只把 1320 用作少算冗余结果式的调度目标；证明独立保留并返回当前四条实际结果式 gcd 的每一个根。因此结论不依赖未恢复的旧数组，也不把旧格式化失败改记为成功。

## 3. 全部八个原参数域

对当前真正恢复的 G，只剥已经关闭的 (2) 和原 $\lambda\ne0$ 因子，再取 squarefree。实际仅发生 J3 的 20 次剥除；其余已付 lambda 因子不在 G 中。剩余 squarefree 次数为 20，SHA-256 为

```
65ad5ab780b31d66f4768c2939762735b40333c6998e0a7926df2c65a89fc311
```

它的全部 QQ 不可约因子（允许各自乘非零有理常数）如下：

$$
\begin{gathered}
3\lambda-1,\quad 2\lambda-1,\quad 3\lambda-2,\quad
2\lambda^2-1,\quad 24\lambda^2-48\lambda+25,\quad
4\lambda^2-5\lambda+2,\\
M_5=64\lambda^5-320\lambda^4+580\lambda^3
-438\lambda^2+111\lambda-1,\\
M_6=1280\lambda^6-1344\lambda^5-8496\lambda^4
+21020\lambda^3-17150\lambda^2+5810\lambda-693.
\end{gathered}
\tag{4}
$$

源码用 QQ 一元精确因式分解得到 (4)，逐因子相乘验证恢复完整 squarefree，而非选取几个方便的低次因子。全部共轭根都保留。

对每个不可约因子 phi，在完整数域

$$
K_\phi=\mathbb Q[\lambda]/(\phi)
$$

中直接特化原 F、原 Chow 及 (1) 的多项式分子。由于 (2) 已关闭，本次每个原 F 都仍为 z 六次式。只剥原 F 与已付单位的实际共同因子，然后与原 Chow 作真实的 $K_\phi[z]$ gcd。

每次域系数求逆都计算并检查 extended-gcd 身份，并在商域回乘等于 1。所有剥因子步骤均执行精确商并检查余数为零。计算没有把不同 lambda 根混配，也没有用范数为零代替原方程。

实际完整返回如下：

| 原 lambda 因子 | 原 F 的 z 次数 | 剥除的已付共同因子 | 与第一原 Chow 的最终共同 z 次数 | 已核域逆数 |
|---|---:|---|---:|---:|
| $3\lambda-1$ | 6 | Q 的一次因子 | 0 | 67 |
| $2\lambda-1$ | 6 | Delta 的一次因子，三次反复剥除 | 0 | 60 |
| $3\lambda-2$ | 6 | Q 的二次共同因子 | 0 | 63 |
| $2\lambda^2-1$ | 6 | Delta 的一次因子，两次反复剥除 | 0 | 61 |
| $24\lambda^2-48\lambda+25$ | 6 | z 的一次因子 | 0 | 61 |
| $4\lambda^2-5\lambda+2$ | 6 | z 的一次因子，四次反复剥除 | 0 | 61 |
| M5 的全部五根 | 6 | z 的一次因子 | 0 | 61 |
| M6 的全部六根 | 6 | I2 的一次因子，两次反复剥除 | 0 | 63 |

这里 Q 非零来自 $pq\ne0$，Delta 非零来自三值互异，z 非零来自值碰撞的单独排除，I2 非零恰是当前 $L\ne0$ 范围。表中没有任何未付除数。每个因子在与 E1、EB 偶部的第一条原 Chow 返回后就得到常数 1，其余原条件不再需要用于排空。

因此 (4) 的全部二十个参数根上均无原合法点。结合 (2) 的全部已闭谱，本两参数原图为空。

## 4. 覆盖结论与实际物理范围

原两参数图使用的是原 Frobenius 迹、原 K 和原最高阶/第二梯度 jets 的必要等式。它们在这里已无任何合法解，所以当然不存在来自本课题原物理几何的临界点。此处不需要从某个抽象 Gram 解提升物理解，也没有将几何排除当作全局幂理想身份。

将本图与已登记的 $I=H=0$ 全 M6 有限纤维、$S=A_f=0$ 值碰撞及完整 $u=1$ 排除合并，当前单位 2+1+1 范围的整个 $S=A_f=0,L\ne0$ 已关闭。原 $L=0$ 仍在其独立任务中；本结论不声称消除了 $A_f\ne0$ 的图。

## 5. 可复算源码与真实成功回执

可复算源码：2026-11-26-unit211-S0-minimal-QQ-original-fibers-347c.py。

- Git blob：0b320f3b03e8bc6b60d90a424401f7e85537e350。
- 源码 21253 字节，SHA-256：4448a6795906bb39ac06858e0a8bd4b97e369f12f0b14e9b1ddac52a7d2509fb。
- 源提交：a8213d2429c498852dde5602ccb9019251f01ff6。
- 实际 Actions run 45823574259、job 139921814574，结论 success，退出码 0。
- 源执行 109.926880 秒；driver 110.026724650 秒；峰值子进程 RSS 211800 KiB。
- stdout 17780 字节，SHA-256：74369eed3d4bb27a40cb7731ed9cf5287fdb9aab2d5299a889066e5d7063e1d6。
- 实际运行中从源提交 pull 到 a39e5a6f88c9695ae43abcc6358679a422c4d5e8，根 README 和本课题 README 的 blob 分别为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、fef43bdf8690f2eec4751d85784a266eacdd0322，规则未变。
- 源记录全部四条实际 QQ 结果式、完整因式分解检查点和八个原域返回身份。环境使用 Python 3.12、python-flint 0.9.0，没有概率性的理想判空步骤。
