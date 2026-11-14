# R119 续篇：固定正平台的真实跨端平滑与完整有限外侧两端酉图

2026-11-14，visible-exact / tail_connector。

**状态：解析证明。** 本篇继续同一固定停止、同一标签球和同一
实际非径向背景。它补上
[三阶转折全频反射](R119-supplement-actual-cubic-turning-complete-reflection-and-strong-sources.md)
(T.34) 后明确保留的 $B$ 输出空间缺口。

完整正区的两个跨端 DN 块满足
$$
 \mathcal N_{CB}:H^1_B\longrightarrow H^1_C,\qquad
 \mathcal N_{BC}:H^{-1}_C\longrightarrow H^{-1}_B,
 \quad \|\cdot\|<2^{590}.
 \tag{S.1}
$$
所以三阶负端的 $H_C\in H^{-1/8}$ 确实产生原 $H^{-1}_B$ 总通量。
证明只使用真实长 $q=2$ 平台内部的一个固定 buffer；
不把全正区（含两个零曲率平台）假定为一致椭圆。

随后在 cut128 与原 $B$ 两端，同时保留 incoming/outgoing 波。
完整有限外侧系统给一个真正满射酉算子，定义于
$L^2_D\oplus L^2_B$；$D$ 端为原物理半阶波，
$B$ 端为 $H^1/H^{-1}$ 的原完整端口。
它不是最终开放网络 returned 方程的逆。

## 1. 同一正区与固定严格椭圆 buffer

沿用
[非负 connector 两端定理](R119-supplement-actual-nonnegative-connector-complete-two-port-and-weak-sources.md)
的原向外坐标 $t\in[0,\ell]$、角流、能量型
$$
 \mathfrak a(u,v)=\int
      (A u_t\overline{v_t}+B u_\theta\overline{v_\theta}),
 \qquad
 A>2^{-365},\quad 0\le B<24,\quad A<2 .
 \tag{S.2}
$$
内端仍是 $C$，外端仍是原 $B$；$B$ 在式 (S.2) 中也表示原
角能量系数，其含义由位置区别。

(E.3) 的原准备段给 $\omega_a<16$，而 $\Omega=2^{360}$。
因此真实 $q=2$ 平台长度
$$
 L_a>{1\over2}\log(2^{360}/16)=178\log2>89 .
 \tag{S.3}
$$
这不是新增平台或修改停止长度。选其内部一个长度6的闭区间
$I_2$，再选严格嵌套的长度4与2区间 $I_1,I_0$，
各相邻边界间距至少 $1/2$。
在这个整个 buffer 上 $-Q=3$，故
$$
 A,B\ge\varepsilon:=2^{-365}.
 \tag{S.4}
$$
取径向 $\zeta$ 支持于 $I_2$、在 $I_1$ 上为1，
以及 $\chi$ 在 $C$ 侧为0、在 $B$ 侧为1，
$\operatorname{supp}\chi'\subset I_0$，可使
$|\zeta'|,|\chi'|\le8$。

(E.8)--(E.10) 的真实角系数及其原三单位余宽给
$$
 |A_\theta|\le A,\qquad |B_\theta|\le B .
 \tag{S.5}
$$
在 $B=0$ 的平台上第二式也准确成立，因为零因子是径向 $Q$；
不是通过除以零定义的估计。所需的较高角导同样由原宽度支付，
但以下一阶平滑只需 (S.5)。

## 2. 一阶角向局部能量估计

先给光滑角数据的齐次 Poisson 解 $u$。在严格 buffer 中，
$w=\partial_\theta u$ 满足
$$
 \partial_t(Aw_t)+\partial_\theta(Bw_\theta)
 =-\partial_t(A_\theta u_t)
  -\partial_\theta(B_\theta u_\theta).
 \tag{S.6}
$$
用 $\zeta^2w$ 测试，分部积分，再以
$2ab\le a^2/2+2b^2$ 吸收含 $\zeta w_t,\zeta w_\theta$ 的项。
(S.5) 控制系数导数项，$|A|<2$、$|\zeta'|\le8$ 和
$\|u_\theta\|_{L^2(I_2)}\le\varepsilon^{-1/2}\|u\|_{\mathfrak a}$
控制 cutoff 项。于是
$$
 \int\zeta^2(A|w_t|^2+B|w_\theta|^2)
 \le2^{12}\varepsilon^{-1}\|u\|_{\mathfrak a}^2,
$$
$$
 \|\partial_\theta u\|_{H^1(I_1\times S^1)}
 <2^{374}\|u\|_{\mathfrak a}.                         \tag{S.7}
$$
这里 $H^1$ 包含径向一阶、角向一阶和零阶范数。
第二式再用一次 (S.4)，$2^{374}$ 已覆盖
$2^6\varepsilon^{-1}$ 与零阶角导项。
对一般有限能量解，先用角平移差分商作同一测试，再取弱极限；
没有要求径向解析或新增目标 jets。

## 3. 把内端数据的一阶角导搬到真实 buffer

记 $U_f$ 为两端数据 $(f,0)$ 的完整 Poisson 解。
(E.16) 给
$$
 \|U_f\|_{\mathfrak a}<16\|f\|_2 .                    \tag{S.8}
$$
对于光滑 $f$，$\partial_\theta U_f-U_{\partial_\theta f}$
有两端零迹。其准确能量方程的右侧是
$-\mathfrak a_\theta(U_f,\cdot)$；
由 (S.5) 和同一能量 Cauchy--Schwarz，
$$
 \|\partial_\theta U_f-U_{\partial_\theta f}\|_{\mathfrak a}
 \le\|U_f\|_{\mathfrak a}.                           \tag{S.9}
$$
这个差保留实际非径向系数的全部交换子。
零迹 Poincare (E.13) 和 (S.4) 给其在 $I_1$ 上的普通
$H^1$ 范数小于 $2^{192}\|U_f\|_{\mathfrak a}$。
与 (S.7)、(S.8) 合并，得到
$$
 \|U_{\partial_\theta f}\|_{H^1(I_1\times S^1)}
 <2^{379}\|f\|_2 .                                  \tag{S.10}
$$
因此真正平滑的是“跨过固定正 buffer 后的输入角导”；
并未声称 $C$ 端自块 $\mathcal N_{CC}$ 有同样增益。

令 $V_g$ 为两端数据 $(0,g)$ 的 Poisson 解，$g$ 使用原物理
$B$ 角。由 (E.15)--(E.16)、(E.26) 的零源版本和 (S.4)，
$$
 \|V_g\|_{H^1(I_1\times S^1)}<2^{204}\|g\|_{H^1_B}.
 \tag{S.11}
$$
原端点角图和通量密度已经在这些 Poisson 与 DN 中；
没有另把 $B$ 端图设为恒等。

## 4. 完整跨端 DN 的一阶平滑

因为 $(1-\chi)V_g$、$\chi U_f$ 都具有两端零迹，
齐次弱方程准确给
$$
 \mathfrak a(U_f,V_g)
 =\int A\chi'\bigl((U_f)_t\overline{V_g}
                       -U_f\overline{(V_g)_t}\bigr).
 \tag{S.12}
$$
右侧只在真实 $I_0$ 内积分。将 $f$ 换为 $\partial_\theta f$，
用 (S.10)--(S.11) 及 $A|\chi'|<16$，两项的完整范数小于
$$
 2^{588}\|f\|_2\|g\|_{H^1_B}.                        \tag{S.13}
$$
左侧就是原 $\mathcal N_{BC}$ 与原 $\mathcal N_{CB}$ 的同一个
Green 配对。结合 (E.18) 的原零阶跨块界，得到
$$
 \|\mathcal N_{CB}g\|_{H^1_C}<2^{590}\|g\|_{H^1_B}.
 \tag{S.14}
$$
光滑数据稠密，故该结论在整个原 $H^1_B$ 空间成立。

取原物理 Green 配对的对偶，得到唯一延拓
$$
 \mathcal N_{BC}:H^{-1}_C\longrightarrow H^{-1}_B,
 \qquad \|\mathcal N_{BC}\|<2^{590}.
 \tag{S.15}
$$
它与旧 $L^2_C\to H^{-1}_B$ 算子在共同域准确一致，
并保持 $\mathcal N_{BC}=\mathcal N_{CB}^*$。
因此不是给两个跨块各自选一个不相容的新表示。

这个延拓也有真实 PDE 场的意义。
对 $f\in H^{-1}$，准确分解
$f=f_0+\partial_\theta f_1$，
其中 $f_0=\Lambda^{-2}f$、
$f_1=-\partial_\theta\Lambda^{-2}f$ 均在 $L^2$，范数不超过
$\|f\|_{H^{-1}}$。用 (S.8)、(S.10) 定义其 Poisson 场在
buffer 内的 $H^1$ 极限；它与原角平移的负阶分布延拓一致。
再在更窄的 buffer 作一次 (S.7)，便有足够角导的内部真实迹，
向 $B$ 的余段是原有限能量 Poisson 问题。
所以 (S.15) 是真实 $B$ 总通量，不是仅形式边界泛函。

三阶反射原先只给 $f_C\in H^{-1/8}$。
该空间连续嵌入 $H^{-1}$，故现在准确恢复
$$
 \mathcal N_{BC}f_C\in H^{-1}_B .
 \tag{S.16}
$$
同时任意原 $f_B\in H^1_B$ 产生
$\mathcal N_{CB}f_B\in H^1_C\subset H^{1/8}_C$，
足以支付三阶证明的真实端荷空间。
这消除了其暂用 $H^2_B$ 输入以及 $H^{-9/8}_B$ 输出的限制；
没有改变三阶端点本身的负八分之一迹估计。

## 5. 同时开放 D、B 两端的真实系统

$D$ 仍是 cut128。沿三阶证明的向内坐标与实际角流，
状态 $(H,P)$ 满足该文 (T.4)。
在 $C$ 与完整正区准确接合为
$$
 \mu_*P(0)=\mathcal N_{CC}H(0)+\mathcal N_{CB}f_B,
$$
$$
 p_B=\mathcal N_{BC}H(0)+\mathcal N_{BB}f_B .
 \tag{S.17}
$$
$p_B$ 是原物理角总通量；两式中不删除任何 mean。
由 (S.14)--(S.16)，对于
$H(0)\in H^{-1/8}, f_B\in H^1$，所有跨项及其 Green 配对都定义良好。

在 $D$ 端采用单位物理波，在 $B$ 端采用原完整 $H^1/H^{-1}$ 波：
$$
 x_D=\sqrt{\mu_*}\Lambda_D^{1/2}H(\eta),\qquad
 y_D=\sqrt{\mu_*}\Lambda_D^{-1/2}P(\eta),
$$
$$
 x_B=\Lambda_B f_B,\qquad y_B=\Lambda_B^{-1}p_B,
 \qquad
 \alpha=\binom{x_D+iy_D}{x_B+iy_B},\quad
 \beta=\binom{x_D-iy_D}{x_B-iy_B}.
 \tag{S.18}
$$
$\Lambda_D$ 使用真实流角，$\Lambda_B$ 使用原物理 $B$ 角。
高度的函数 pullback、通量的密度和 $\sqrt{\mu_*}$ 同时保留，
所以两端虚 Green 通量之和准确等于波范数差的固定倍数。

对有限完整 Fourier 空间，同时压缩正区的整个 $2\times2$ DN，
不只压缩其两个对角块。它仍自伴。
加上完整有限三阶传播，给有限的两端 incoming 问题。
若 $\alpha=0$，Green 式给 $\beta=0$；
于是 $D$ 端两个 Cauchy 状态以及 $B$ 的高度、通量都为零。
三阶 ODE 唯一性和正区 Dirichlet 唯一性给零解。
因此该有限方阵可逆，$\alpha\mapsto\beta$ 酉。

## 6. 全频两端极限与不丢失跨端通量

有限酉性给
$\|\alpha_D\|^2+\|\beta_D\|^2\le2\|\alpha\|^2$。
三阶文 (T.13)--(T.19) 不需要固定 $B$ 为零；
它们只使用 $D$ 端能量。
现在
$$
 E(\eta)\le32\mu_*^{-1}\|\alpha\|_2^2,\qquad
 \|H(0)\|_{H^{-1/8}}<2^{196}\|\alpha\|_2,
$$
$$
 \|f_B\|_{H^1}\le\|\alpha\|_2 .
 \tag{S.19}
$$
这里 $\mu_*^{-1/2}<2^{182}$，常数已经包含实际物理缩放。

由 (S.14)，$\mathcal N_{CB}f_B$ 在 $H^1_C$ 一致有界。
紧嵌入 $H^1_C\Subset H^{1/8}_C$ 给这个跨项的强子列。
再用 (T.10) 的自块负阶界，得到 $P(0)$ 的所需紧性。
与三阶文完全相同的体区能量和时间紧性给真实弱解，
保持 (S.17) 的两个完整端口方程。

在 $C$ 端，$\mathcal N_{CC}$ 的自块由原 (T.20) 截断交换子
证明虚通量极限为零；剩余跨项是合法对偶配对
$\langle\mathcal N_{CB}f_B,H(0)\rangle$。
在 $B$ 端，$\mathcal N_{BB}$ 自伴，其虚配对为零。
两个跨块由 (S.15) 的准确伴随关系互相抵消。
三阶体区 (T.21) 的 strong 交换子与能量支配收敛仍适用。
因此真实极限满足
$$
 \operatorname{Im}\langle\mu_*P(\eta),H(\eta)\rangle+
 \operatorname{Im}\langle p_B,f_B\rangle=0,\qquad
 \|\beta\|_2=\|\alpha\|_2 .
 \tag{S.20}
$$
这不是把有限酉性直接带过弱极限。
由范数相等，有限输出实际强收敛。

零输入解的两个外端状态均零，再由同一 Cauchy/Dirichlet
唯一性得零解，故所有子列是一解。
反向指定任意 $\beta$，在同一有限系统上重复这些一致界和
通量极限，给任意输出的真实原像。最终得到
$$
 \boxed{\ 
 \mathscr S_{\rm ext}:L^2_D\oplus L^2_B
       \longrightarrow L^2_D\oplus L^2_B,\qquad
 \mathscr S_{\rm ext}^*\mathscr S_{\rm ext}
 =\mathscr S_{\rm ext}\mathscr S_{\rm ext}^*=I .
 \ }                                                     \tag{S.21}
$$
无“已知没有隐藏 unitary kernel”的额外假设；
该性质已由真实两个端点状态的唯一性证明。
这仍不把 $I-\mathscr R\mathscr S_{\rm ext}$ 的可逆性作为结论。

## 7. 完整源、外端 affine 列与 BV 迹

在 (S.17) 加入正区真实 affine 负荷 $\ell_C,\ell_B$，
三阶体区使用 (T.26) 的完整 $f,g_1$。
一个直接可消费的充分源空间是
$$
 \ell_C\in H^{1/8}_C,\quad \ell_B\in H^{-1}_B,\quad
 f,g_1\in\mathcal M_s(H^{1/2}).
 \tag{S.22}
$$
正区原 $g\in\mathcal M H^1$、
$F^t,F^\theta\in\mathcal M H^2$ 的强 weak 合同，
按 (T.34) 的角平移证明支付 $\ell_C$，
原 (E.25)--(E.33) 支付 $\ell_B$。
任意贴近零平台的 $L^2$ 源仍不自动获得角平滑；
(S.14) 是跨端平滑，不是这种全源增益。

对齐次两端测试解，完整 Green 式的新增负荷为
$$
 \langle\ell_C,H_Z(0)\rangle+
 \langle\ell_B,f_{B,Z}\rangle+
 \mu_*\int(\langle g_1,H_Z\rangle-\langle f,P_Z\rangle).
 \tag{S.23}
$$
(T.16)、(S.19) 和 $\mu_*<1$ 给一个共同界
$$
 \|\beta_{\rm src}\|_2
 <2^{200}\left(
 \|\ell_C\|_{H^{1/8}}+\|\ell_B\|_{H^{-1}}
 +\|f\|_{\mathcal M H^{1/2}}+\|g_1\|_{\mathcal M H^{1/2}}
 \right),
$$
$$
 \beta=\mathscr S_{\rm ext}\alpha+\beta_{\rm src}.
 \tag{S.24}
$$
原负段物理源按 (T.31)--(T.32) 的带 $\mu_*^{-1}$ Piola 映射
消费；正区用其原完整源图。连同上述所有常数，原强角源到
单位物理波的有限段预算可统一用 $2^{1024}$。
这里没有把径向测度 norm 改成其端点值。

若源含 atom，解类使用 BV/单侧迹以及真实 affine 跳；
齐次解的时间连续性不能逐字用于有跳解。
高度、总通量两种跳及两个 mean 源均保留。
bare 通量仍需原 weak 源的真实端点迹才能恢复。

真实 $\Gamma^*$ 两列、compact 参数列和原 $\nu$ 列均须按
它们的实际体源及实际外负荷进入 (S.23)。
没有因固定 connector 的系数不随某个参数变化，就删掉从内部
送入它的完整参数响应列。
本篇只证明有限外侧组件及其源算子，不替代全网参数 Schur。

## 8. 对下一接线的准确范围

原 $D=\mathrm{cut128}$ 与 $B$ 的完整外侧组件现在具有：
真实全频两端酉图、原 $B$ 的 $H^1/H^{-1}$ 端口、
全部 mean，以及完整强 ordinary/weak 源的仿射映射。
没有删去角图、密度、原 $\mu_*^{\pm1/2}$ 或任何跨端 DN 块。

开放内部网络的 $e_X$ 仍不同于 $D$。
下一步必须通过未完整 $(129,2)$ 的实际负段、当前根图与全源
映射，将 (S.21) 接到该真实 $e_X$，然后消费原开放逆的
actual returned 方程和原层权。
此处没有预先选择一个辅助外相位并把它当作原物理边界，
也没有利用正区平滑把未知 high 模截掉。
