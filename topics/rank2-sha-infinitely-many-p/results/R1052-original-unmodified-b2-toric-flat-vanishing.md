# R1052 — 原未剔除 theta 来源的真实 b=2 toric flat 分支恒零

日期：2026-11-27 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

**状态：以下结论只针对同一原未作通常 $p$ 剔除的固定 weight3 来源，经实际 $g_2$ 好点来源和 $g_1$ 拉回所给的 $b=2$ flat 读者。它证明这个读者在指定完整 toric 分支恒零，所以不能借它检测原 canonical $J'_S(0)$。它没有证明 $J'_S(0)=0$，没有把通常剔除、原 outward 图或任一 signed 类一并置零。**

## 1. 固定来源、实际基和所取分支

保[原 psi4 来源](../notes/2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)的三个完整来源
$$
 D_k(z)=\sum_{n\ge0}d_{k,n}z^n,\qquad
 S_k(z)=\sum_{n\ge0}s_{k,n}z^n,\qquad k=1,3,5.
 \tag{1}
$$
$D_k$ 是同一真实两条三挠 Weyl 词给出的 degree102 截面，首四阶归一为1；$S_1=S$，$S_3=H_{3,1}$，$S_5=H_{5,1}$ 是原 degree34 截面。所有多项式、raw 幅度、实际 $z=\Omega_0h_\infty T/\delta$ 缩放、三处相位、十八个17核、sign、Artin 和 corestriction 权保持原定义。

取好惰性 $p>211$，排除原固定模型、系数、非零 Artin 幅度和下文固定代数数的有限坏集。记
$$
 \tau=\frac p{p^2-1},\qquad d=p+1,\qquad
 g_1=\operatorname{diag}(p,1),\quad
 g_2=\operatorname{diag}(1,p).
 \tag{2}
$$
在各实际 CM 点使用同一个源基及其 prime-to-$p$ 运输。书版 CM period 的约定是
$$
 \omega_{\rm can}\,\Omega_p=\omega_0,\qquad
 v_p(\Omega_p)=-\tau.
 \tag{3}
$$
第一式由 AMS212 (1.12)、印第242页脚注2和(8.17)确定，第二式是 Proposition7.7 (7.8)。不能把 2018 版 (129) 的反向记号接到书版估值。若原代数微分与整微分相差固定代数数，将其保入固定坏集和下面的基比较；没有把 $\Omega_p$ 当作单位。

令 $F_0$ 为实际未剔除形式相对于 $\omega_{\rm can}^3$ 的函数。其好点来源取 $g_2^*F_0$，沿 $g_1$ 拉回。本文使用[实际 good 拉回来源证明](../notes/2026-11-27-original-good-pullback-and-bad-source-return.md)中的同源返回，准确有
$$
 g_1^*\{(p\delta_3)^n(g_2^*F_0)\}
   =(p^2\delta_3)^n\{(pI)^*F_0\}
   =-p^{2n}\delta_3^nF_0 .
 \tag{4}
$$
末负号来自完整 full2/full9 的实际中心作用；中心 $pI$ 自身保持 $z_{\rm dR}$，不另添 $p^{2n}$。这里的好点 $Q_1$ 展开及拉回的坏点 $Q_2$ 展开确为有界来源。本文不使用 Proposition7.20 的 usual/flat 比较。

把(4)施于原完整 toric 和，记其未取 flat 的非负整数值为 $\mathcal R_{k,p}(n)$。各有限外权是原固定 characters 与实际微分运输的权，不是新的任意矩。选一个素于 $p$ 的正整数 $D_p$，同时固定所有这些外权的 Teichmuller 部分、原六步 finite phase，并满足 $p-1\mid D_p$、$6\mid D_p$。原 CM 单位权在 $K_p^\times$ 时可直接取 $D_p=p^2-1$；若在一个较大固定系数域记录额外单位权，取有限个 Teichmuller 阶的公倍数即可。以下证明不依赖这个无害选择。

实际局部参数为
$$
 n(u)=-2+D_pu,\qquad u\in\mathbf Z_p.
 \tag{5}
$$
$D_p$ 是 $p$ 进单位；正整数 $u$ 给原合法 $n\equiv4\bmod6$。每个有限单位外权沿(5)由其固定 Teichmuller 部分及 $1+\mathfrak m$ 部分的幂连续延拓，导数仍是该实际外权的导数。

## 2. 原全部 sigma 系数的统一估值

本节只消费已经证明的 [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md) §4 和 [R588](R588-actual-wild-kummer-disc-and-nonlinear-primitive-radius.md) §1(3)–(4)、§2(8)，不重新执行系数计算。

置
$$
 r_\sigma=p^{-\tau},\quad \rho=p^{-1/(2p)},\quad
 c=[z^{p+1}]\log(\sigma/z),\quad
 H_\sigma=\frac{\sigma}{z\exp(cz^{p+1})},\quad W=z^2x .
 \tag{6}
$$
$v_p(c)=-1$，$r_\sigma<\rho$；$H_\sigma$、其逆和 $W$ 在 $\rho$ 盘的 Gauss 范数为1。对于每个整数 $N\ge0$，全部 Gaussian 系数满足
$$
 v_p((Nc)^h/h!)+\tau(p+1)h
 \ \ge\ \frac{s_p(h)}{p-1}\ \ge0.
 \tag{7}
$$
因此 $\exp(Ncz^{p+1})$ 在 $r_\sigma$ 的逐系数加权上确界不超过1。它在闭边界未必属于 Tate 代数；本证明没有作此加强。

对任一实际完整 holomorphic theta 截面
$$
 F(z)=\sigma^N\sum_a q_ax^a,\qquad N-2a\ge0,
$$
逐项恒等式
$$
 F=\sum_aq_a z^{N-2a}H_\sigma^N W^a
                  \exp(Ncz^{p+1})
$$
给
$$
 v_p([z^m]F)+\tau m
 \ge m_F:=\min_{q_a\ne0}
       \{v_p(q_a)+\tau(N-2a)\}.
 \tag{8}
$$
这是完整有限和及全部 Cauchy 乘积的界，常数与 $m$ 无关。

原 $D_k$ 的多项式形式为 $\sigma^{102}xP_{16}(x^3)$ 乘各自已指定的常数，所以 $a\le49$、$102-2a\ge4$。原 $S_k$ 是 $\sigma^{34}$ 乘次数至17的实际多项式，故 $34-2a\ge0$。每条归一分母仍保在(8)的有限最小值中；例如 canonical 的原 $301056=2^{11}\cdot3\cdot7^2$ 在这里为单位。于是存在与 $n$ 无关的实际常数 $m_{D,k},m_{S,k}$，使
$$
 v_p(d_{k,n})+v_p(s_{k,n+2})
 \ge -\tau(2n+2)+m_{D,k}+m_{S,k}.
 \tag{9}
$$
零系数按赋值 $+\infty$ 理解。没有把原高尾删掉或把原各来源改为自由系数。

## 3. 全阶乘、周期和基倍率合并后的正斜率

[完整正权来源](../notes/2026-11-27-original-psi4-full-graphs-artin-and-geometric-newton-cross.md) §3及[固定张量审计](../notes/2026-11-27-original-psi4-common-factor-digit-and-continuity-audit.md) §7.3给，所有合法非负整数 $n$ 都有
$$
 \mathcal T_k(n)
 = B_k\,\frac{n!(n+2)!}{4!\,6!}\,
       \xi^{\,n-4}\delta^{-n}d_{k,n}s_{k,n+2},
 \qquad n\equiv4\pmod6.
 \tag{10}
$$
$B_k\ne0$ 是原 $n=4$ 锚固定的 Artin 幅度，$\xi\ne0$ 是同一代数张量比较固定的代数数。其代数性已经由原两个非零代数槽证明；这里没有把复周期任意嵌入 $\mathbf C_p$。删去 $\xi$ 的有限坏位后 $v_p(\xi)=0$。

必须在同一完整张量
$\omega^3\otimes(\Omega^1)^n$ 上比较。书版(3)和实际 KS 给周期幂 $\Omega_p^{3+2n}$；源 determinant 线及其整杯积基保持原约定。先作 weight3 的原有限17字、再 raising，与 $\mathcal T_k(n)$ 的次序相差 $17^{-n}$；它是 $p$ 单位。所有其余固定 tame 余切基比、$\delta^{-n}$ 以及有限单位运输仍是 $p$ 单位的固定幂。由(4)，实际完整未取 flat 的 toric 和因此是
$$
 \mathcal R_{k,p}(n)
 =K_{k,p}\,p^{2n}\Omega_p^{\,3+2n}
      u_{k,p}^{\,n}\,n!(n+2)!
          d_{k,n}s_{k,n+2},
 \qquad v_p(u_{k,p})=0 .
 \tag{11}
$$
$K_{k,p}$ 保原中心负号、$B_k$、$4!6!$、固定首权基比及全部固定权；它不依赖 $n$。式(11)只是已完成的同一代数张量换基和原完整未平方 theta 身份，没有将函数移过连接后重新微分。各 CM 微分用同一 prime-to-$p$ isogeny 运输，period 相同；若用各自原整微分，实际固定单位倍率在 $u_{k,p}^n$ 和原有限权中逐项抵消后得到同一式。

由(3)、(9)、(11)，
$$
 \boxed{\quad
 v_p(\mathcal R_{k,p}(n))
 \ge (2-4\tau)n+v_p(n!)+v_p((n+2)!)+C_{k,p},
 \quad}
 \tag{12}
$$
其中 $C_{k,p}$ 是与 $n$ 无关的有限常数。比如把(11)中的 $\Omega_p^3$ 留在显示式时，可取
$C_{k,p}=v_p(K_{k,p})+m_{D,k}+m_{S,k}-5\tau$。

$p>211$ 时 $2-4\tau>0$。所以沿任何合法整数 $n\to+\infty$，完整和 $\mathcal R_{k,p}(n)\to0$。这一估值没有使用 canonical 坏假设，也不使用参考 $K_-$ 的单位性或 $J'_S(0)$ 的值。

## 4. 真正 unflat 极限，而非正整数插值假设

为避免引用未付接合，直接证明本次所需的极限。对一个实际 bounded source
$$
 A(Q)=\int_{\mathbf Z_p}Q^x\,d\mu(x),\quad
 \inf_rv_p\!\left(\int\binom xr\,d\mu\right)>-\infty
$$
和实际 $C$，非负整数 Maass 值为
$$
 R_N=\sum_{i=0}^N c_i(N)C^i
               \int_{\mathbf Z_p}x^{N-i}\,d\mu,
 \quad c_i(X)=\binom{X+2}{i}\binom Xi\,i!.
$$
取一个固定合法整数 $j$，以及
$$
 N_r=j+D_pp^r\longrightarrow j
 \quad\hbox{在权空间，且 }N_r\longrightarrow+\infty
 \quad\hbox{在通常整数意义下}.
$$
对每个固定 $i$，$c_i(N_r)\to c_i(j)$。单位上 $x^{N_r-i}$ 一致趋于指定 tame 分支的 $x^{j-i}$；非单位上则一致趋零。因此该项趋于真实单位测度项。另一方面，全部整数 $N$、$i\le N$ 都有统一尾界
$$
 v_p\!\left(c_i(N)C^i\int x^{N-i}d\mu\right)
 \ge m_A+v_p(i!)+i\,v_p(C)\longrightarrow+\infty .
$$
这里用的是实际 $v_p(C)=2$，更一般 $v_p(C)>-1/(p-1)$ 即可。先截有限 $i$，再取极限，最后去尾，严格给
$$
 \lim_{r\to\infty}R_{j+D_pp^r}
 =\sum_{i\ge0}c_i(j)C^i
       \int_{\mathbf Z_p^\times}x^{j-i}d\mu
 =\mathcal M_A(j).
 \tag{13}
$$
这是同一个 source 的 unflat-to-flat 极限，绝不是
$R_j=\mathcal M_A(j)$ 的逐正权等式。

原 toric 和只有有限个实际来源。所选 $D_p$ 固定每个外权的 tame 部分；其单位幂沿 $N_r$ 连续趋于在 $j$ 的真实外权。故(13)逐项求和仍成立，保全部 sign/Artin/Cor 和外权。

## 5. 指定原 toric flat 分支与完整斜率为零

取(5)中任一正整数 $u_0$，令 $j=-2+D_pu_0$。由(12)，左边的完整 toric 极限为零；由(13)，它正是本次实际 flat 读者在 $u_0$ 的值。因此所有正整数 $u_0$ 都是其零点。

同源 flat 笔记已证明局部解析性及一致差商尾；全部有限外权连续，并在每个足够小的权邻域内为实际解析单位幂。在未分歧单位域可直接用全盘解析，较大分歧系数域则先限制到足够小的权圆盘。正整数在 $\mathbf Z_p$ 稠密，所以
$$
 \boxed{\quad
 \mathcal L^{\flat,\mathrm{unmodified},b=2}_{k,p}(u)
       \equiv0\quad(u\in\mathbf Z_p),\qquad k=1,3,5.
 \quad}
 \tag{14}
$$
特别在 $u=0$ 的值和完整导数均为零，导数包括每一个外权的导数。$D_p$ 为单位，改回任何已经固定同一 tame 分支的合法局部参数也保持这个结论。

这是整个指定有限 toric 和的结论；本文没有由和为零推出各个点的测度支撑均在 $p\mathbf Z_p$。也没有声称任意 $p$-level 改源都满足(10)或(12)。

## 6. 对下一入口的确切限制

(14)封住的是“只把原未剔除 $F_0$ 送入实际 $g_2/g_1$、再靠真实 $b=2$ flat 获得 canonical 检测”的入口。此前直接 finite Newton 读者和 Bol primitive 仍成立，但对这个来源及完整 toric 分支读到的是零。

下一来源必须实际保住一个非平凡部分，例如真正 $p$-level 改源的全部局部向量、其原 finite trace，或直接的指定 proper 图读数；其整数权式和负端点必须重新比较。不能把(14)反译为原 $J'_S(0)$ 为零，也不能因此取消原固定有限曲线族的通常全 $\Sha$ 桥。主目标及联合无穷 canonical 非零仍未完成。

本篇只有纸证；没有运行数学程序，没有保存可重算输出。
