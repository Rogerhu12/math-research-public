# Theta 因子中心值：sigma 挠值的代数性与有限迹

日期：2026-11-12。状态：已证明有限代数迹公式与下述范围界限；尚未证明两个因子各有简单中心零点。

本文使用 [固定 sigma 平方范数笔记](2026-11-12-fixed-sigma-theta-square-factorization.md) 的固定数据

$$
 E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
 S(z)=R(x(z),y(z))\sigma_E(z)^d,
 \qquad R=P(x^2),\quad d=L^2,
$$

其中 $L$ 仅有素因子 $2,17$，$s_0=S(0)=0$。固定普通素数
$p\equiv1\pmod4$、$p\ge13$、$p\ne17$，及使
$v_p(\pi)=1$ 的嵌入 $K\hookrightarrow\mathbb Q_p$，其中
$\pi=\psi(\mathfrak p)$、$\pi\bar\pi=p$。

令

$$
 \Sigma(t)=\sigma_E(\log_E t)\in t\mathbb Z_p[[t]],
 \qquad t=-x/y.
$$

这是本曲线的固定普通 sigma 级数，不把该形式表达式在非零挠点处解释为先求 $\log_E Q=0$ 再代入复 sigma。所有挠值都由收敛的 $t$ 级数定义。

## 1. 任意奇范数 CM 乘子的精确 division 函数

设 $a\in\mathbb Z[i]\setminus\{0\}$，$N=a\bar a$ 为奇数。取与 $\sigma_E(z)=z+\cdots$ 相容的函数

$$
 \Psi_a(P)=a\prod_{T\in(E[a]\setminus\{O\})/\{\pm1\}}
                        \bigl(x(P)-x(T)\bigr)\in K(E)^\times.
                                                               \tag{1}
$$

非零 kernel 点可成对，因为 $N$ 为奇数。乘积的定义不依赖每对的代表。

**精确恒等式是**

$$
 \boxed{\displaystyle
 \sigma_E(az)=\sigma_E(z)^N\Psi_a(z),\qquad
 \Sigma([a]t)=\Sigma(t)^N\Psi_a(t).}                          \tag{2}
$$

特别地，不必额外要求 $a\equiv1\pmod{(1+i)^3}$；$a$ 可能含一个单位因子 $\pm1,\pm i$，该因子由 (1) 的首项 $a$ 保留。

### 证明

方格 $\Gamma=\Omega_E\mathbb Z[i]$ 的准周期为
$\eta(\lambda)=\pi_{\mathbb C}\bar\lambda/\Omega_E^2$。其 sigma 半特征对
$\lambda=(m+ni)\Omega_E$ 为

$$
 \epsilon(\lambda)=(-1)^{m+n+mn}.
$$

奇范数 $a$ 模 $2\mathbb Z[i]$ 为 $1$ 或 $i$。两种乘法均保持 $m+n+mn$ 的奇偶，故

$$
 \epsilon(a\lambda)=\epsilon(\lambda)
                    =\epsilon(\lambda)^N.
$$

又因为 $\eta(a\lambda)a=N\eta(\lambda)$，sigma 的指数准周期也精确相消。因此
$\sigma_E(az)/\sigma_E(z)^N$ 为椭圆函数，其零除子是全部非零 $a$-挠点，唯一极点是 $O$，阶为 $N-1$。在零处它的首项为 $az^{1-N}$。

右边 (1) 有相同除子、相同首项，故相等。CM 乘子在 $K$ 上定义，其 kernel 除子在 $K$ 上定义；或直接用 Galois 稳定的乘积可见 $\Psi_a\in K(E)$。这也完整固定了可能的根单位常数。

将 $z=\log_Et$ 作形式代入，即得 (2) 的第二式。下面使用它时会另行核实各个级数在该挠点处收敛。证毕。

## 2. 每个非零 $\pi$-挠点的 sigma 值是代数数

非零 $Q\in E[\pi]$ 都在普通正式群中，且

$$
 v_p(t(Q))=\frac1{p-1}>0.
$$

这是度一 CM/Lubin–Tate 正式群的首层性质，亦可用课题 R24 的严格 LT 参数验证。令

$$
 \vartheta_p(Q)=\Sigma(t(Q)),\qquad
 u_Q=\frac{\vartheta_p(Q)}{t(Q)}\in1+\mathfrak m.
                                                               \tag{3}
$$

因为 $\Sigma(t)/t\in1+t\mathbb Z_p[[t]]$，(3) 收敛且非零，并且
$v_p(\vartheta_p(Q))=v_p(t(Q))$。

记

$$
 e=\operatorname{ord}_{(\mathbb Z[i]/\pi)^\times}(\bar\pi),
 \qquad a=\bar\pi^e,\qquad N=p^e.
                                                               \tag{4}
$$

则 $e\mid p-1$、$a\equiv1\pmod\pi$，从而 $[a]Q=Q$。而
$E[a]\cap E[\pi]=\{O\}$，故 $\Psi_a(Q)\ne0$。

在所选普通位，$E[a]$ 是 étale 的 $\bar\pi$-primary 子群。其非零点不约化到 $O$，所以各 $x(T)$ 均整。式 (1) 说明 $\Psi_a(t)$ 是收敛于穿孔正式群圆盘的整系数 Laurent 级数，其首项为 $a t^{1-N}$。$a$ 在此处为单位，$[a]t$ 为整正式群自同构；故 (2) 的两边都可在 $t=t(Q)$ 处求值。

由 $[a]Q=Q$，得到

$$
 \boxed{\displaystyle
 \vartheta_p(Q)^{p^e-1}=\Psi_{\bar\pi^e}(Q)^{-1}.}           \tag{5}
$$

右边是非零代数数，因此 $\vartheta_p(Q)$ 本身为代数数。更精确地，

$$
 u_Q^{p^e-1}=B_Q,
 \qquad B_Q=\bigl(\Psi_{\bar\pi^e}(Q)t(Q)^{p^e-1}\bigr)^{-1}.
                                                               \tag{6}
$$

令 $F_Q$ 为包含 $K(Q)$ 的所选局部完备化。由于
$x(t)t^2\in1+t\mathcal O_{F_Q}[[t]]$、所有 $x(T)$ 整，且
$a\equiv1\pmod\pi$，乘积 (1) 直接给出 $B_Q\in1+\mathfrak m_{F_Q}$。

指数 $p^e-1$ 是 $p$ 单位，所以幂映射

$$
 1+\mathfrak m_{F_Q}\longrightarrow1+\mathfrak m_{F_Q},
 \quad u\longmapsto u^{p^e-1}
$$

为双射：对 $X^{p^e-1}-B_Q$ 在 $X=1$ 应用 Hensel 引理，其导数为单位；在任意更大局部域的 principal-unit 群中唯一性仍成立。因此 (6) 的 principal-unit 条件唯一选定根，没有另留未知根单位。

这里“代数数”表示属于 $\overline{\mathbb Q}\subset\mathbb C_p$。它并不声称属于一个与 $p$ 无关的固定数域；(4) 与 (5) 中的次数随 $p$ 变化。

## 3. 中心值的有限代数迹公式

固定 sigma 因子的 Amice 变换是

$$
 \mathcal A_p(Z)=S\bigl(\Omega_p\log(1+Z)\bigr),
$$

按整正式群同构解释后，它是有界系数的收敛幂级数。设其测度为 $\nu_p$，单位部分 Mellin 变换为 $G_p(T)$。

对任意 $\mathbb Z_p$ 上有界测度，有限 Fourier 投影给

$$
 \nu_p(p\mathbb Z_p)=\frac1p\sum_{\zeta^p=1}
                                      \mathcal A_p(\zeta-1).
                                                               \tag{7}
$$

证明只需在连续角色上使用
$p^{-1}\sum_{\zeta^p=1}\zeta^x=\mathbf1_{p\mathbb Z_p}(x)$，再积分；有限和不引入极限交换问题。

正式群同构把 $\mu_p$ 双射到 $E[\pi]$。因此 (7) 中真正收敛的求值是

$$
 \mathcal A_p(\zeta-1)
       =R(Q)\vartheta_p(Q)^d\quad(Q\ne O),
 \qquad\mathcal A_p(0)=S(0)=0.
                                                               \tag{8}
$$

**不能**把 $\log\zeta=0$ 先代入 $S$ 的加法参数 Taylor 展开，进而把 (8) 错误置零；该复合级数的延拓由普通正式群上的有界级数确定。

因测度总质量 $\nu_p(\mathbb Z_p)=S(0)=0$，得到精确公式

$$
 \boxed{\displaystyle
 G_p(0)=-\frac1p\sum_{0\ne Q\in E[\pi]}
                    R(Q)\vartheta_p(Q)^d\in\overline{\mathbb Q}.}
                                                               \tag{9}
$$

同理，第二因子为

$$
 \boxed{\displaystyle
 G_p^\dagger(0)=-\frac1p\sum_{0\ne Q\in E[\pi]}
                    \overline R(Q)\vartheta_p(Q)^d.}         \tag{10}
$$

因为两个和遍历完整的 $E[\pi]$，它们不依赖正式群同构对非零 $\pi$-挠点的编号，也不依赖 $\Omega_p$ 的生成元选择。若 $R$ 的系数在固定数域 $M$，局部 Galois 不变性还说明 (9) 属于所选 $M$ 的 $p$-进完备化；这个结论不能替换成“属于 $M$ 本身”。

固定因子分解及 R40 已证

$$
 G_p(0)G_p^\dagger(0)=0.                                    \tag{11}
$$

所以每个所列 $p$ 至少一个有限代数迹精确为零。式 (11) 尚未区分哪一个迹为零，也未给出非零一阶导数。

## 4. 固定线丛的 theta group 不能直接作用于这些平移

设 $\mathcal L=\mathcal O_E(dO)$。对 $Q\in E$，

$$
 t_Q^*\mathcal L\otimes\mathcal L^{-1}
   =\mathcal O_E\bigl(d[-Q]-d[O]\bigr)
$$

在 $\operatorname{Pic}^0(E)\simeq E$ 中对应 $-[d]Q$。所以

$$
 t_Q^*\mathcal L\simeq\mathcal L
       \iff[d]Q=O.                                         \tag{12}
$$

本处 $p\nmid d$，而非零 $Q\in E[\pi]$ 的阶为 $p$，故 (12) 不成立。第 7 节构造固定截面时用到的 $E[d]$ theta group 因而不能直接升级成 $E[\pi]$ 在同一个 $d$ 维截面空间上的作用。

若改用 $\mathcal L^{\otimes p}=\mathcal O_E(pdO)$，则这些平移确实进入 theta group，但截面空间维数变为 $pd$，且得到的是截面的 $p$ 次幂或另一个截面。特征零中
$\sum_Q S(Q)^p$ 不是 $(\sum_Q S(Q))^p$，不能据此替换 (9) 的线性迹，尤其不能忽略正是目标精度所在的交叉项。

这排除了一个具体的固定有限矩阵捷径；它不排除利用原 $R$ 来自特定 Weil 向量这一额外性质建立新的 Hecke 或 depletion 恒等式。

## 5. 复共轭与单位限制必须分别处理

式 (10) 的 $\overline R$ 与式 (9) 的 $R$ 都在**同一个** $E[\pi]$ 上求值。复共轭则把

$$
 E[\pi]\longrightarrow E[\bar\pi],\qquad
 \mathfrak p\longrightarrow\bar{\mathfrak p}.
$$

因此共轭 (9) 同时改变 connected torsion 子群及 principal-unit 根所用的局部嵌入，并不自动得到 (10)。即使 (9) 是代数数，也不能略过这一步。

此外，总质量为零只等于 $S(0)=0$；单位质量还需减去 (7)。某些 Gross CM 曲线的单因子 Euler 公式由 Rodriguez Villegas，*On the Taylor coefficients of theta functions of CM elliptic curves* (1993)，Proposition 4.6，从该文特定的**完整两变量 theta 测度分解**推出：

<https://frvillegas.github.io/pdf/frv-cm-theta.pdf>，印刷 pp.12–13。

上述论证在这一阶段使用的是固定 E17 的中央范数及整条中央分支因子分解。仅凭这些输入，尚没有同一个完整两变量 theta 测度的单因子 Frobenius 关系，所以这里不移用该 Proposition 的单 Euler 因子或中心消失结论。

该阶段留下的问题是：原有限 Schwartz 权重能否把 (9)、(10) 中的两个代数迹同时化为零，并继续识别两个因子的首个非零导数。前半项现已由下面的新输入解决；主目标仍需要后半项在无穷多个 $p$ 上的非零性。

## 6. 后续加强：两个有限代数迹现在都已证明为零

[R48](../results/R48-real-theta-structure-and-central-slope-criterion.md)
直接核对了有限 Weil 向量的反线性结构。经一次固定代数相位调整，
存在固定 $q\in\mathbb Q(i)^\times$，在所有当前 $p$ 位都是单位，使

$$
 \overline S(z)=S(q^{-1}z),\qquad
 G_p^\dagger(T)=(1+T)^{\log_p\langle q^{-1}\rangle/
                                \log_p(1+p)}G_p(T).
$$

这是同一个 $p$ 位上的实际推前关系，补上了 §5 指出的缺口；
它不把复共轭本身错误地视为该位上的连续自同构。
结合 (11)，现在对每个所列普通素数都有

$$
 \boxed{\quad G_p(0)=G_p^\dagger(0)=0.\quad}
$$

因此 (9)、(10) 两个有限代数迹分别精确为零。
随后 [主 tame 单 Euler 分布笔记](2026-11-12-theta-principal-tame-euler-distribution.md)
又由同一精确平方与测度环证明单因子的分布式。
这些新增结论保留了本篇的挠值代数性及全部根的规范，
但没有证明 $G_p'(0)\ne0$。
R48 的剩余目标正是该斜率在无穷多个 $p$ 的非零性。
