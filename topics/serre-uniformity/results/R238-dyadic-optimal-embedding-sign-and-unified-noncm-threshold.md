# R238：二进最优嵌入的准确符号与全部实际类型的统一非 CM 门槛

日期：2026-11-13。状态：**已证明。** 本篇补齐 R236 的
$p\equiv3\pmod8$ 分支。参考极大序上的共同 CM 符号是 $-1$；
它由两种二进最优嵌入的准确数目给出。于是同一个修正二次扭曲投影
适用于全部阶四类型，无须二进 Hecke 支集扩张。全部实际类型和旧
Steinberg 参数可共用一个明确有效常数。

## 1. 精确陈述

保持 R213/R214 的实际小惯性分支。设 $\theta$ 的阶为四，
$\Xi=(\theta\vartheta^{\pm1})\circ\lambda$，$\Omega=\Xi^{-1}$。
令 $a$ 是 $\Omega$ 的 prime-to-$p$ 准确环类导子，记

$$D=|D_K|,\qquad M=Da^2,\qquad h=h(\mathcal O_a),
\qquad a_D=\prod_{q\mid D}q^{v_q(a)},\qquad a_0=a/a_D,$$

$$\mathcal L_a=\prod_{q\mid a}(1-\chi_K(q)/q)^{-1},
\qquad\mathcal T(M)=\max_{1\le m<M}\tau(m).$$

**定理 238.1。** 对两个实际三次符号及全部阶四同余分支，都有

$$\boxed{p>
\frac{2a_D^2\,4^{\omega(D)}16^{\omega(a_0)}
\mathcal T(M)^2M}{h\mathcal L_a^2}
\quad\Longrightarrow\quad
\exists f\in\mathcal F_\theta(p^2)\text{ 非 CM}:
L(\tfrac12,\pi_{f,K}\otimes\Xi)\ne0.}                    \tag{238.1}$$

R236 已处理 $p\equiv7\pmod8$、$a=c$。
本文的新部分为 $p\equiv3\pmod8$，其实际准确导子是 $a=bc$。
本篇不要求 $2\nmid Da$。

令 $M^*=D(bc)^2$。沿用 R213 §6 的有效有限积，则

$$\boxed{C_\epsilon^{\rm all}=
5184X_{\epsilon/4}T_{\epsilon/8}^{\,2}\beta_{\epsilon/2}^{-2}} \tag{238.2}$$

满足以下完整有效整性判据：

$$\boxed{
p\ge C_\epsilon^{\rm all}\frac{(M^*)^{1+\epsilon}}
{h(\mathcal O_{bc})}
\quad\Longrightarrow\quad j(E)\in\mathbb Z.
}                                                        \tag{238.3}$$

其量词涵盖全部需要的实际深度零类型、两个三次方向、全部商域 $K$
和共同导子 $bc$。这里不把 $M^*$ 当成已被 $p$ 控制的量。

## 2. 参考空间和唯一被删除的类

以下假设 $p\equiv3\pmod8$。令

$$F=\mathbb Q(\sqrt{-p}),\quad h_F=h(-p),\quad
S_1=\mathcal O_F,\quad S_2=\mathbb Z[\sqrt{-p}],
\quad\chi=\chi_F.$$

取 $B=B_{p,\infty}$ 中的全局 $j_0^2=-p$，并选包含 $S_1$ 的
极大序 $R_0$。参考空间 $H_0$ 在 $p$ 具有右 $\theta$ 特征，
在所有 $q\ne p$ 被 $(R_0)_q^\times$ 固定。
定义与 R236 相同的

$$S_0=R(j_{0,p})\mathcal M_\chi,
\qquad(\mathcal M_\chi\phi)(g)
=\chi(\operatorname{Nrd}g)\phi(g).                      \tag{238.4}$$

其中 $j_{0,p}$ 是只在 $p$ 非平凡的 adele。
$S_0$ 保持 $H_0$，为酉 involution。

在极大序单位中，$\theta$ 杀死中心及所有三阶部分，但在阶四元上
等于 $(-1)^{(p+1)/4}=-1$。由 Deuring 理想类对应与特征 $p>3$ 的
椭圆曲线自同构分类，唯一含阶四单位的理想类是 $j=1728$ 的类；
因 $p\equiv3\pmod4$，该类确实超奇异。
所以 $H_0$ 按全部极大序理想类给出一维纤维，**唯独 $1728$ 类的
纤维为零**。其他类的全部单位都被 $\theta$ 杀死。

特别，不得把全部 $2h_F$ 个 Frobenius 固定类直接当成
$\operatorname{tr}S_0$；还必须删除这一类并计算其他类的符号。

## 3. 固定点的符号恰由二进交序决定

对参考极大序理想类 $[g]$，若 Frobenius 置换固定它，则如
R236 §3.1 可写

$$g j_{0,p}=\gamma g u,
\qquad\operatorname{Nrd}\gamma=p,\qquad\gamma^2=-p,
\qquad u\in\widehat R_0^\times.                         \tag{238.5}$$

用全局 Skolem–Noether 把 $\gamma$ 共轭到 $j_0$ 后，R236 的
同一计算表明：所有 $q\ne2,p$ 的范数字符为一，$p$ 处的相位
$\theta(u_p)$ 与 $\chi_p(\operatorname{Nrd}g_p)$ 精确抵消。
因此固定点权只剩下

$$\boxed{w([g])=\chi_2(\operatorname{Nrd}g_2).}           \tag{238.6}$$

现在 $F_2/\mathbb Q_2$ 未分歧二次，$\chi_2$ 未分歧且
$\chi_2(2)=-1$。参考极大序在 $2$ 对应一个 $\mathcal O_{F,2}$
稳定格。设 $\Lambda=g_2\mathbb Z_2^2$；由 (238.5)，它被
$S_{2,2}=\mathbb Z_2+2\mathcal O_{F,2}$ 保持。

这里所需的格分类可直接证明。用一个 $F_2^\times$ 元缩放格，使
$1\in\Lambda\subseteq\mathcal O_{F,2}$。写
$\mathcal O_{F,2}=\mathbb Z_2+\mathbb Z_2\alpha$。
$\Lambda/\mathbb Z_2$ 是秩一格，所以再调整基后

$$\Lambda=\mathbb Z_2+2^n\mathbb Z_2\alpha.$$

由 $2\alpha\cdot1\in\Lambda$ 得 $n\le1$。
$F_2$ 中缩放元的范数有偶赋值，所以不改变 (238.6)。
上述两种格的行列式赋值分别为零和一。
因此

$$\boxed{
w([g])=\begin{cases}
 +1,&F\cap R([g])=S_1\text{ 对所选嵌入而言},\\
 -1,&F\cap R([g])=S_2\text{ 对所选嵌入而言}.
\end{cases}}                                           \tag{238.7}$$

在 $q\ne2$ 交序已经极大，故这是全局交序的两种全部可能。
对非 $1728$ 类，全部单位的 $\theta$ 值为一，固定点权不依赖
(238.5) 中选取的范数 $p$ 元，因而该类的所有这些嵌入都具有
同一种交序。

记其数目分别为 $N_1,N_2$。下一节准确计算它们。

## 4. 最优嵌入数与 $1728$ 类的半数修正

### 4.1 全局嵌入数，没有遗失权或取向

对 $S=S_1,S_2$，令 $m_i(S)$ 是 $S$ 到第 $i$ 个左极大序
$R_i$ 的最优嵌入数，按 $R_i^\times$ 共轭取商。
Eichler 的双陪集计数公式给

$$\sum_i m_i(S)=h(S)\prod_q m_q(S,R_0).                 \tag{238.8}$$

所用的是 Voight (2021), Theorem 30.4.7 的理想类求和公式；
不把求和范围误换成极大序同构类型。
所有局部因子在此都是一：$q\ne p$ 为分裂矩阵代数中的极大序，
每个二次整序的最优嵌入有一个 $\mathrm{GL}_2(\mathbb Z_q)$
共轭类；在 $p$，$F_p$ 分歧且 $S_p$ 极大，而
$B_p^\times=F_p^\times\mathcal O_{B_p}^{\times}$。
因此

$$\sum_i m_i(S_1)=h_F,
\qquad\sum_i m_i(S_2)=h(S_2)=3h_F.                     \tag{238.9}$$

最后一个等式来自环类数公式：$[\mathcal O_F^\times:S_2^\times]=1$，
$\chi_F(2)=-1$，故 $h(S_2)/h_F=2(1+1/2)=3$。

为把 (238.9) 连到固定类，设 $R_i$ 的 Frobenius 类固定。
范数 $p$ 的唯一双边素理想此时主化，取一个生成元 $\gamma$。
所有范数 $p$ 元恰为 $\gamma R_i^\times$，所以其数目是
$|R_i^\times|$。它们全部具有迹零，证明仍是 R236 的
“迹被 $p$ 整除且绝对值小于 $2\sqrt p$”。
反之，任一个这样的元都使该理想类固定。

每个嵌入的共轭稳定子是 $F^\times\cap R_i^\times=\{\pm1\}$，
因为 $F\ne\mathbb Q(i),\mathbb Q(\sqrt{-3})$。
因此共轭轨道长度为 $|R_i^\times|/2$。
对非 $1728$ 固定类，§3 说明全部范数 $p$ 元为同一种交序，
故该类对相应 $m_i(S)$ 的贡献准确为二，对另一个为零。

### 4.2 $1728$ 类恰好对两种序各贡献一

在这一类的极大序中取 $i^2=-1$，单位群是
$\{\pm1,\pm i\}$。若 $\gamma$ 为一个范数 $p$ 元，全部四个为

$$\gamma,\ -\gamma,\ \gamma i,\ -\gamma i.$$

$\gamma$ 和 $\gamma i$ 的迹都为零，故 $\gamma i=-i\gamma$。
在 $R_{i,2}\simeq M_2(\mathbb Z_2)$ 中，$i$ 的模二像是非平凡
unipotent 元：若 $i\equiv1\pmod2$，则 $(1+i)/2$ 为整元，
但其范数为 $1/2$，矛盾。

模二约化后 $\gamma$ 与 $i$ 交换；非平凡 unipotent 元在
$\mathrm{GL}_2(\mathbb F_2)$ 中的中心化子正好是 $\{1,i\}$。
所以 $\gamma$ 与 $\gamma i$ 的模二像中恰有一个为单位元。
而 $\mathbb Z[\gamma]$ 延伸到 $\mathcal O_F$ 的准确条件是
$(1+\gamma)/2$ 为整元，即 $\gamma\equiv1\pmod2$。
于是这四个范数 $p$ 元中，恰好两个给 $S_1$，另两个给 $S_2$。

每个共轭轨道长度为 $4/2=2$，故

$$\boxed{m_{1728}(S_1)=m_{1728}(S_2)=1.}                \tag{238.10}$$

这个半数修正同时解释了为什么不能用不带权的 Deuring 固定点数
直接算出 $S_0$ 的迹。

### 4.3 准确符号计数

代入 (238.9)–(238.10) 得

$$2N_1+1=h_F,\qquad2N_2+1=3h_F,$$

即

$$\boxed{N_1=(h_F-1)/2,\qquad N_2=(3h_F-1)/2.}           \tag{238.11}$$

由 §2，$1728$ 类不在 $H_0$ 中；其他非固定类对置换迹贡献零。
由 (238.7)，

$$\boxed{\operatorname{tr}(S_0|H_0)=N_1-N_2=-h_F.}       \tag{238.12}$$

这也独立复现总固定类数 $N_1+N_2+1=2h_F$，但证明使用了比
总数更精细的最优嵌入区分。

## 5. 全部 CM 线的共同负号

R181 精确计数的 CM 空间在 $H_0$ 中有 $h_F$ 条线。
与 R236 一样，$S_0$ 将非 CM 的 $\pi,\pi\otimes\chi_F$ 配对互换，
这些配对的迹为零；在每条 CM 线上，$S_0$ 的特征值为 $\pm1$。
(238.12) 迫使这 $h_F$ 个符号全为 $-1$。

回到实际 Gross–Prasad 共轭极大序，并将 $j_0$ 换成规范化原
$K_p$ 的 $j$，仍只使全部 CM 符号同乘一个共同 $\pm1$。
因此存在实际共同符号 $\varepsilon$，使

$$S|H_{\rm CM}=\varepsilon,\qquad
A=R(f)\frac{1-\varepsilon S}{2}\text{ 为杀死 CM 的正算子}. \tag{238.13}$$

本篇未借用“二次自扭曲的经典 Fourier 归一化自动通过 JL”这样的
未说明兼容；共同负号来自 (238.8)–(238.12) 的准确有限计数。

## 6. 同一个混合迹立即给统一精确阈值

R236 §4–6 中以下事实只要求 $\theta$ 阶四、$\Omega$ 阶十二及
$\Omega^6=\chi_F\circ N_{K/\mathbb Q}$，并未要求 $p\equiv7\pmod8$：

- $R(f)S$ 的核是原核在 $p$ 平移后，再乘右变量的
  $\chi_F\circ\operatorname{Nrd}$；
- 两个 singular 稳定子角色非平凡，所以混合迹没有主项；
- $p$ 处混合局部积分绝对值至多一，支集为 $v_p(\xi)<0$；
- 全局参数为 $\xi=y/(y-M)$、$0<y<M$、$p\mid M-y$；
- 换 $z=M-y$ 后，$q\mid a_0$ 的截断赋值权逐项不变，且进程
  通过零，因此全部误差仍为 R213 的 $E$。

这里使用当前实际 $a=bc$，并保留 $a_D\mid36$。特别包括
$2\mid D$ 或 $2\mid a$ 的情形，未替换二进测试函数。
于是

$$J(A)\ge\frac12\left(
\frac{4h\mathcal L_a^2}{M}-2E\right),
\qquad
E=\frac{4a_D^2\,4^{\omega(D)}16^{\omega(a_0)}\mathcal T(M)^2}{p}.$$

(238.1) 使 $J(A)>0$，所以得到所需同一实际角色上的非 CM
中心值非消失。这证明定理 238.1。

## 7. 一个明确常数涵盖全部实际整性接口

由 R213 §6 的逐素数有效界及 $a_D^2\le1296$，(238.1) 的右侧
不超过

$$2592X_{\epsilon/4}T_{\epsilon/8}^{\,2}
\beta_{\epsilon/2}^{-2}\frac{M^{1+\epsilon}}h.$$

再乘二保证非严格充分条件推出严格正性，得到 (238.2)。
该常数同时大于 R213 在全部 $r>4$ 上的 $2592$ 系数和
R87 旧三次 Steinberg 参数的 $162$ 系数。
在 $a\mid bc$ 时，R213 已证明
$M^{1+\epsilon}/h(\mathcal O_a)$ 随导子整除单调不减。
所以 (238.3) 的数值条件同时给全部实际类型的非 CM 非消失，
并给旧 Steinberg 三次参数的非消失。

R172 给这些实际有理投影像有限，R177 的全部类型单位理想与
R181 的整行充分判据排除每个实际分母素数，得 $j(E)\in\mathbb Z$。
这证明 (238.3)，没有额外乘上类型数目。

统一 Siegel 下界仍可把它写成
$p\ge C_\nu(M^*)^{1/2+\nu}\Rightarrow j(E)\in\mathbb Z$，
但这一幂次版本的常数一般无效；新明确有效结论是 (238.2)–(238.3)。
变化共同导子上界和整 $j$ 异常分支依然开放，本文没有将一个必要
导子下界当成最终不存在证明。

## 8. 来源、依赖与交付清单

- John Voight, *Quaternion Algebras*, GTM **288**, Springer (2021)，
  [Chapter 30: Optimal embeddings](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_30)，
  pp.541–567，Theorem 30.4.7/式 (30.4.8) 是理想类上的完整求和；
  Proposition 30.5.3(a),(b) 给所用局部嵌入数。二进格的奇偶权、
  每个固定类的贡献及 $1728$ 的半数修正均在本文独立证明。
- 同书 [Chapter 42](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)，
  Corollary 42.3.7 给理想类、自同构群与超奇异曲线的对应。
- R181：准确 CM 维数；R236：正投影、混合核、两个 singular 项、
  $p$ 处完整相位及不引入 $D$ 依赖的 regular 求和。
- R213/R214/R226：实际准确导子、导子在 $D$ 上的统一界和有效
  有限乘积；R87/R172/R177/R181：旧谱、有限投影与整性接口。

**Manifest：纯证明。** 新交付只有本 Markdown；没有数据、脚本、
未经展示的有限枚举或需要重跑的数值结果。
