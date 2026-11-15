# R150：由已成第二页连续完成饱和第三页的执行接口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。  
日期：2026-11-15。状态：§4 的完整 $S_3(B)$ 来源覆盖是已证明的条件定理；执行入口仍为草稿，仅已做 Python AST 检查，没有运行第三页。最终输入 SHA 等待第二页的实际完整回执，不以 Actions step 的 success 代替数学完成。

## 1. 只读取上一页真实来源

完整原二次饱和矩阵 $B$ 满足 $AS=p^2B$，$\operatorname{im}B=(\operatorname{im}A:p^2)$。第二页实际保存的 204 个原来源 $L_{4,j}$ 满足 $AL_{4,j}=p^4D_{4,j}$，并保 15 个整数 Taylor 系数及 10 个有形式完成保证的有效系数。

若其完整相关像维数为 $r$，已成源核文件按原 204 标签保存

$$
F(s)=[\,I-TC,\ T(sI-J_2)\,],
\qquad \#F=204+r\le229,\quad \deg F\le5.
$$

第三页逐个读取这些真实源多项式。不得以第二像的常数矩阵核代替它，也不能删去六个旧列、$te_8$ 或 $t\zeta_2$ 的高位。

本次不重建旧 $q_1,q_2,q_3$，不重算完整第二像，也不重跑旧 197 或 selector。

## 2. 精确整数 $s\to t$ 提升与第一页纠偏

令 $t=s-2$。源核文件中的每个 $f(s)=\sum f_ds^d$ 先取实际规范整数 $s$ 系数，再按

$$
f(t+2)=\sum_k\left(\sum_{d\ge k}f_d{d\choose k}2^{d-k}\right)t^k
\pmod {p^6}
$$

形成 recipe。这里先在整数中转换，再模 $p^6$，不是重新把每个 $t$ 系数约到 $0,\ldots,30$。原整数 helper 的稀疏边系数是 $t$ 系数，不能将保存的 $s$ 系数直接传入。

每个 $M_4=\sum_jL_{4,j}f_j$ 的 root2 除类准确落在 $U_9$。以真实原三次除源对应的基

$$
U_7,\quad b_8=A\kappa_8/p^3,\quad D_{3,2}=AL_{3,2}/p^3
$$

求九个常数 $d_i$，在全部 315 坐标中核其成员身份。采用本轮原 $L_{3,2}$ 的实际 20 项来源；不能用四次除源 $\kappa_9$ 免费替代它。

形成

$$
M_4^{\rm corr}
=M_4-\sum_{i\le7}p^{4-e_i}\kappa_i d_i
-p\kappa_8d_8-pL_{3,2}d_9.
\tag{2.1}
$$

原 $A\bmod p^6$ 完整十项乘回验证 $p^4$ 整除。原 3333 预基、全部 1034 输出与 H/DAG cochain 都保留。随后求解原 $Gq_4$ 的全部十项、保 13 个自由条件并完整乘回，取得原 2195 和 6188 来源。

## 3. 最后实际整除与完整第三像

令

$$
L_5=M_4^{\rm corr}-p^4\widehat q_4.
$$

原十七式全部十项实际验证 $p^5$ 整除，保

$$
D_5=AL_5/p^5\bmod p
$$

的前五项。由已付最大 Smith 指数 5，十项解有前五项一致的真正形式完成；没有再沿用未经支付的更短前缀。

完整原 root2 五项配 root1 三项零，经过原正常形得到 820 标准坐标，再用真实 143 商映射核全部 104 自由观察、39 torsion 坐标和完整 315 重建。没有把局部任意右端假设为没有自由部分。

第三商的已付空间是

$$
U_{\rm in}=U_9+\text{第二像的全部实际 Krylov 预像},
\qquad \dim U_{\rm in}=9+r.
$$

其真实基及 $J$ 作用在准备阶段逐坐标核实。完整第三像在 root2 维数 $25-r$ 的商中计算，并核 $(s-2)^5$ 湮灭身份。每个最终正组合继续记录它来自哪个 $L_5$ 及哪个幂；已付第二像的补偿也回存为原 204 个 $L_4$ 的多项式系数，不能只保一个抽象商坐标。

所有目标使用完整原 $\rho$。同时保存 $P_2\rho$、$\rho-P_2\rho$ 及真实 $U_9$ 坐标；已成身份只说外部分量已付，不说它等于零。

## 4. 为什么完整第三负可以覆盖所有原来源次数

这里给出回执负范围的来源证明，而非仅依靠矩阵维数。

对局部整数来源模记

$$
S_k(B)=\{z:Bz\in p^kV\}.
$$

任一 $S_1(B)$ 来源先减其完整 $\ker\bar B$ 初值，再除 $p$，故由实际核提升和 $pE_B$ 生成。继续一次，$S_2(B)$ 由已成完整第一页源核的真实第二提升与 $pS_1(B)$ 生成。原 1834 个核及两个关系有精确整数 $B$ 核提升；剥离它们后，恰留下全部 204 个 $L_4$ 初值。

对于 $S_3(B)$，先用完整 $F(s)$ 消去其第二像核初值；余来源属于 $pS_2(B)$。构造 (2.1) 中的 $p\kappa_8,pL_{3,2}$ 正是在源上支付第一页像，随后 $p^4q_4$ 支付原像。因此读取全部 $F$ 来源给出的第三像，再模去完整第二像及第一页像，正好是整个 $S_3(B)$ 的相关障碍。没有漏掉更低初值的进入项。

在原变量中，若存在任意次数的

$$
AX'=p^2h_0T\pmod {p^6},
$$

则 $X'\in S_2(A)$。完整来源包给 $X'=SY'$ 加一个真实原核；当前 $X$ 也有这样的 $B$ 来源。相减并除 $p^2$，得到某个 $z\in S_3(B)$ 满足

$$
Bz=p^3\rho\pmod {p^4}.
$$

故任何杀死 $U_{\rm in}$ 和全部第三多项式像、但在 $\rho$ 上非零的 root2 dual，都否定这个原目标的模 $p^6$ 来源，不受原多项式次数限制。全局来源会映入该形式局部环，所以局部必要否定已足；不需要先证明其它 primary 的全页像。

反向不成立：局部相容仍须恢复全局多项式来源、其它 primary、整数 carry，并最终核全部原式。负结论也只排本次 $p^2h_0$ 的模 $p^6$ 整数来源，不把它升级为无界 $p$ 分母的特征零否定。

这一必要否定还准确限制特征零多项式来源的 $31$ 分母：若 $AY=h_0T$ 且所有 $Y$ 的系数都属于 $p^{-2}\mathbf Z_{(31)}$，则 $p^2Y$ 约化模 $p^6$ 会给被否定的原整数来源。因此一旦取得该实际 dual，这类至多两次 $31$ 分母的来源也不存在；它不排除至少三次 $31$ 分母或任意参数分母的来源。当前仍没有第三页实际 dual，本段只是严格范围的条件推论。

## 5. 输入和 CLI

预计 26 个精确输入来自六个既有工件与主线小件。最终 contract 必须使用实际第二页回执中的 SHA 和字节数，草稿不预填来源字节。

- T96：graph、原 normal trace、forward、backward。
- all198：原 $\kappa_1,\kappa_2$ family、四个 K2 family、selected K2。
- seven：包括 $\kappa_8$ 的原整数来源 family。
- ninth：原 $A\bmod p^6$ 模型及验证回执。
- old200：仅为复用原 VQ 接口读取已绑定的原高核标签头；不重算旧高核。
- second：原 prepared/complete 两套小系统与回执、整个源核、全部 L4 与 L3 原整数源及各乘回回执、原 G/V 二十项缓存。
- notes：原 model、torsion state、143 映射及回执。

调用：

    python3 notes/2026-11-15-r150-saturated-third-page-runner-789f.py \
      --notes-root notes \
      --t96-recovery T96 --all198-recovery ALL198 \
      --seven-recovery SEVEN --ninth-recovery NINTH \
      --old200-recovery OLD200 --second-recovery SECOND \
      --out OUTPUT --math-seconds 300 \
      --memory-mib 512 --compile-seconds 30

可加 --resume-recovery OLD_THIRD_OUTPUT/recovery。second-recovery 是只读输入，不作为需要重算的本次阶段；不要把全部第二 recovery 无理由复制进新的输出。

## 6. 两种绑定与真实部分恢复

G/V 缓存仍携带上一链的实际 native data-lineage binding。新 helper 继续使用这个字段读它们，缓存字节不被改写。

本次总 continuation binding 单独绑定全部实际输入、当前数学源码和新的来源范围。每个运行阶段另有完整 source/input/recipe/spec SHA 的 stage-context 文件：部分 checkpoint 若与其上下文不同立即拒绝，不能只因为旧 native binding 相同便复用。

这些绑定不依赖恢复目录的绝对路径。原 transport 的双槽 portable 检查点、整数 helper 的完整累加器及源前缀、VQ 真数组、Schur 真单位块与完整源解，都按已有协议保存。只有实际输出哈希和 marker 全部满足，才跳过已成阶段。

## 7. 时钟、封存与完成字段

四个未改 C++ 分别编译，单次至多 30 秒、512 MiB。之后全部新数学共用 300 秒时钟；任何部分超时保真实数组，后继从准确游标继续。不能用退出 0 代替原式/源核字段。

封存使用 gzip compresslevel=1、mtime=0，保持原字节无损。超过十进制 1,000,000 字节压缩，每片不超过 4,500,000 字节；保整体与分片 SHA。逐大文件打印封存心跳，单独记 packagingElapsedSeconds，不混入数学时间。全部 stage-cache/context 也保存。

主回执为 saturated-third-page-pipeline-receipt.json。完成后：

- allTrueOriginalThirdSourcesComputed=true；
- completeRelevantSaturatedThirdImageComputed=true；
- completeOriginalS2SourceCoverageRetained=true；
- individualTargetCompatible 给完整九个局部标志；
- originalMod31SixObstructedTargetLabels 只列实际负 dual 的目标；
- solutionThirdSourcePolynomialsAscending 与 solutionSecondSourcePolynomialsAscending 保真实正来源组合。

三个 outcome：

| outcome | 准确含义 |
|---|---|
| complete-root2-third-obstruction | 九个目标均有完整第三 dual；本次原模 $p^6$ 全否定 |
| third-page-partial-local-compatible-global-continuation-required | 只有部分局部相容；相容者须继续全局原式，负目标逐个有完整否定 |
| third-page-all-local-compatible-global-continuation-required | 九个局部相容；全部仍须全局原式恢复 |

只有第一种才将 globalAllOriginalSourceMod31SixDecisionComputed 与 globalAllOriginalSourceMod31SixObstructionVerified 同时记 true。其它分支保逐目标负范围，但全九成员判定尚未闭合。

本轮始终不填 allCompatibleTargetsOriginalIdentityVerified、fullOriginalAllNineMod887503681IdentityVerified 或 characteristicZeroIdentityAsserted 为 true。正分支完整原式未完成之前，finite_budget_verified 也为 false。即使完整本次模 $p^6$ 负已闭合，原特征零 R150 与主 ISP 仍须继续。
