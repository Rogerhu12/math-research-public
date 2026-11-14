# R186 推论：前六个设计系数自由变化的凸充分域

**状态：已证明。** 本文是 [R186](../results/R186-delta7-only-removal-of-the-late-positive-K-island.md) 的独立推论，不改原证明、源或报告。原证明 SHA256 为 cbbab39508842f0bccaabe96fc567e04c6a3537d22796b0b0ca881655e3804ec。

本推论允许前六个 bump 系数在原 binary64 0.08 盒内自由变化，同时把第七个系数限制在 binary64 0.027 至 binary64 0.08。整个参数域有严格正半径；R186 晚段闭区间上仍有 $a_{ss}>11/10000$ 和 $K<-11/10000$。中段正 K 由所选 R182 准确 Bernstein 行另行保证。无需新增 profile 盒、F/J、BVP 或 body 计算。

## 1. 准确对象和参数域

准确 base、七个已保存支持区间和紧支撑函数均保持 R171/R175/R182 的定义。base 候选 SHA256 为 7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1。

令

$$
\psi_j(s)=1024q_j^5(1-q_j)^5,\qquad
q_j=\frac{s-L_j}{R_j-L_j}
$$

在支持内部成立，支持外取零。每个 $\psi_j$ 为 $C^4$，且 $0\le\psi_j\le1$。定义

$$
a_\delta(s)=a_{\rm base}(s)+\sum_{j=1}^{7}\delta_j\psi_j(s).
$$

[R136/R166](../results/R166-exact-round-prefix-and-complete-increment-equations.md) 的准确 base 满足全域 $a_{\rm base}\ge4/5$。取准确常数

$$
M={\rm binary64}(0.08)
=\frac{5764607523034235}{72057594037927936},\qquad
m={\rm binary64}(0.027)
=\frac{7782220156096217}{288230376151711744}.
$$

本推论首先考虑凸盒

$$
\mathcal D_{\rm box}
=\left\{\delta:\ |\delta_j|\le M\ (1\le j\le6),\
m\le\delta_7\le M\right\}.
\tag{1}
$$

这是原准确支持和原 J7 参数布局的结论，不自动扩展到新增设计列或另一 base。

## 2. 全域严格正半径

对任意 $\delta\in\mathcal D_{\rm box}$，第七项非负，而前六项各不小于 $-M$，故

$$
a_\delta(s)\ge\frac45-6M
=\frac{57646075230342347}{180143985094819840}
>\frac{319}{1000}>0
\qquad\hbox{对全部 }s.
\tag{2}
$$

这不沿用 b075 旧状态约 0.785 的下界。前六个系数自由变化后，该旧下界未被证明保持；式 (2) 是本推论明确支付的新统一下界。原 radius39 数值设计行仍可作为附加约束保留，式 (2) 的连续正半径证明本身不依赖 radius39 的采样。

## 3. 晚段负 K 结论对前六个系数完全独立

沿用 R186 的准确目标闭区间

$$
I=[A,D],\qquad
A=\frac{801077783718527}{562949953421312},\quad
D=\frac{6507701461550367}{4503599627370496}.
$$

所有前六个支持均在 $A$ 左侧结束；最右的端点满足

$$
\max_{j\le6}R_j
=\frac{6107222740134427}{4503599627370496}
<A.
\tag{3}
$$

因此在整个 $I$ 上，前六项的值及其一至四导数全部恒为零。对任何符合 (1) 的前六个系数，局部函数准确相同：

$$
a_\delta(s)=a_{\rm base}(s)+\delta_7\psi_7(s),
\qquad s\in I.
\tag{4}
$$

R186 §2–4 已对每个实数 $\delta_7\in[m,M]$ 证明该局部函数满足

$$
a_{\delta,ss}>\frac{11}{10000},
\qquad
a_\delta\le A_0+(D-A)+M<1,
\tag{5}
$$

其中 $A_0$ 是原已认证 R182 首盒在 $A$ 的准确半径上端点。式 (4) 表明这两个局部结论完全不依赖前六个新系数。再结合 (2)，得到整个凸盒上的统一结论

$$
K_\delta(s)=-\frac{a_{\delta,ss}(s)}{a_\delta(s)}
<-\frac{11}{10000}
\qquad(\delta\in\mathcal D_{\rm box},\ s\in I).
\tag{6}
$$

这一步使用的是 R186 已付的准确连续界，没有把局部采样或浮点预览提升为证书。

## 4. 与中段准确 K 域及 QP 的直接组合

中段窗口闭支撑右端为

$$
D_{\rm mid}
=\frac{4458563631096791}{4503599627370496},
$$

而第七个支持左端为

$$
L_7=\frac{4581889784524941}{4503599627370496}
>D_{\rm mid}.
\tag{7}
$$

所以 middle 窗上 $\psi_7''$ 准确恒为零，R182 middle 的全部准确 Bernstein 行第七列也准确为零。前六个系数变化可以改变 middle 上的度量与 K，不能直接复用 b075 的单状态通过结论；应对实际新 $\delta$ 核验完整所选 middle 准确行。

记这些准确有限充分行为

$$
A_i\delta\le b_i,\qquad i\in\mathcal I_{\rm mid},
$$

其每一行均绑定原 R182 连续 base 上界、准确支持和正余量。可用设计域为

$$
\mathcal D
=\mathcal D_{\rm box}
\cap\bigcap_{i\in\mathcal I_{\rm mid}}
\{\delta:A_i\delta\le b_i\}
\cap\mathcal D_{\rm radius39},
\tag{8}
$$

其中最后一项只在主求解器保留原附加设计行时加入。式 (8) 是凸域；其中每个状态同时满足 middle 的已证连续正 K 条件、式 (2) 的全域正半径，以及式 (6) 的晚段严格负 K 条件。

对已恢复的 middle-only installer，只需继续使用原 box 和 middle 行，再追加一条 QP 行

$$
(0,0,0,0,0,0,1)\,\delta\ge m.
\tag{9}
$$

该行的系数与下界都由上述明确 binary64 值准确表示，无需新的 Bernstein 舍入预算。旧 late positive-K 行必须全部排除；它们与本推论晚段负 K 设计不相容。筛选依准确四端点与 row_owner，不依窗口名称或迹符号。

恢复模块为 scripts/fd2d_gc_signed_search_domain_recovery.py，SHA256 4bd8bdd374ed4280f81f15264510f587ac2af47e2b7e401e71c9ee8c542e6c49。该模块负责 middle 准确行和原 box；它没有暗中追加式 (9)。选择本推论作为新设计域的 Context 必须同时：

1. 在 QP 的原 profile_domain 中加入式 (9)；
2. 每个实际 trial 和接受保存前，以准确 binary64 有理值核验 $\delta_7\ge m$；
3. 调用 middle-only handle.verify_delta，核所选全部准确行、原 box 与实际来源；
4. 保存明确的 R186 推论域身份及当前参数证书，并刷新实际 tail 证书。

浮点 QP 容差不替代这些准确核验；本推论也不允许只加 QP 行后将旧 candidate 证书复制给新参数。实际全参数位置由 profile_parameter_slice 决定，不写死 47:54。

## 5. 对固定区和实际曲面的作用范围

所有七个支持都不越过原受保护末窗起点；紧支撑函数的值及一至四导数在各右端为零。因此前六个自由变化及第七个变化都不修改 protected terminal 的准确度量、K 和 cut 参数定义。

第七项本身在 coast 和 middle 上恒零；但前六个系数自由变化可能改变 coast 或 middle 的度量，必须使用实际新参数。不能从本推论声称整个 coast、冻结参考解、实际位置、frame 或 seam 仍等于 b075。

这是一族明确新物理度量的凸充分域。真实等距性、完整微分 Codazzi、曲率预算、reach、闭合和幅度仍由对应新场与准确后验支付。本推论没有求得新的闭曲面或完整 BVP 解。

## 6. 准确算术记录

独立小记录为 notes/2026-11-12-fd2d-metric-R186-free-first-six-01-report.json。实际在 functions 的 V8 中用 BigInt 有理交叉乘法核定：

- 式 (2) 的准确分数及其严格大于 319/1000；
- 式 (3) 的支持分离；
- 式 (7) 的 middle / 第七支持分离。

局部 11/10000 界直接继承 R186 的已执行准确报告，不重复新 profile 包。没有 OS 子进程，未宣称 Python/Node exit code；没有新增 F/J、BVP、body、ODE 或 Arb 盒。

本 note 与小记录均为新文件。原 R186 完整证明、源及报告 SHA 保持不变。
