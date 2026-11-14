# R150：七条真实饱和关系与原 31h0 下一提升——单次连续执行接口

作者：normal_annihilator / 789f。2026-11-14。

本入口继续[完整七关系定理](2026-11-14-r150-seven-relation-saturation-and-smith-layers-789f.md)和 run 43626632693 已成的原 $31h_0$ 模 $31^3$ 来源。没有重复旧 198 个方向、旧四列、selected 来源或旧 T96 图。冻结时本机执行环境不可用，以下新适配源码尚未解析、编译或运行；第一次 Actions 的真实结果另记。

## 1. 直接保原十七式的七个除三次来源

固定同一七列 $b_i=A\kappa_i/p^{e_i}$，其中

$$
p=31,\qquad e=(1,1,2,2,2,2,2),\qquad P(s)=sI_7-J_7.
$$

$J_7$ 从当前已经完整重建的 10040 字节证书读取，按原列次序及原整数来源保存。整矩阵的常数项取负的 $0,\ldots,30$ 整数代表，不把未计算的 carry 省去。

先恢复七个真实原来源

$$
Az_j=\sum_i b_iP_{ij}\pmod p.
$$

其右端费用不超过 $88$，原图给临时来源费用上界 $184$。然后定义真正的原整数来源

$$
\boxed{K_{3,j}=\sum_i p^{2-e_i}\kappa_iP_{ij}-p^2z_j.}
$$

有

$$
AK_{3,j}=p^2\left(\sum_i b_iP_{ij}-Az_j\right)\equiv0\pmod {p^3}.
$$

所以新增广映射 $A^+=[A,B]$ 的七个第一 Bockstein 列，正是

$$
\left[AK_{3,j}/p^3\right]\quad\text{在 }Q/U.
$$

这样一次原十七式模 $p^4=923521$ 的完整乘回，就保住全部原整数来源及 carry，无需分别展开 $B$ 的更高精度与 $Az$。

## 2. 同时带入真正的九个当前余量

同一次原乘积另带入 run 43626632693 的实际 $Z$，计算

$$
r_{3,j}=(p h_0t_j-AZ_j)/p^3\pmod p.
$$

生成的 16 列严格分为：

- 标签 7001 至 7007：$AK_{3,j}/p^3$；
- 标签 2 至 10：$(p h_0t_j-AZ_j)/p^3$。

原乘积程序先对全部 $6188$ 原行、$4367$ 输出分量完整检查 $p^3$ 整除。前七列不扣目标，后九列扣的固定目标是原 $31h_0$。输出到 RHS 时后九列反号，得到上述真正的 $r_3$。

新的整数模型来自已落库的 65159 字节 exact-model gzip，未重新运行 parameterSystem。解压的完整原整数 JSON SHA256 为 fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3。程序重新检查原 17×77 项结构、4433 个允许系数、18 个固定缩放及原 $h_0$ 因式，并逐 token 核新模 $p^4$ 模型降到模 $p^3$ 后与已执行模型完全相同。

生成来源模数 $923521$ 超过两字节范围。因此新来源格式 R150P431 / R150O431 的系数准确用 uint32；原旧输入仍按各自真实 uint16 格式读入。新原乘积程序也能读取自己的 uint32 来源，供相容分支继续使用。没有截断成 16 位。

## 3. 整个 308 维商和完整新第一像

16 个 RHS 沿同一原常预基取正常形。全部原 3333 预基操作与旧 T96 的 forward/backward SHA 逐字相同；旧 2195 个正常形从未重算。

完整 G 商余先进入原 820 标准坐标，检查全部 505 个自由观察及完整 315 维重建。再按同一七个真类 $U$ 做商，得到 $308$ 维 torsion 作用 $J^+$；13 个自由分量仍完整保留于此前检验。

对七个新类求完整 $J^+$-Krylov 闭包。达到秩不再增长时再核闭包真正 $J^+$ 不变；任意多项式关系都已包含。七关系定理保证原全部 1834 核在这个新第一 Bockstein 中为零，所以这七列给的是新增广映射的整个第一像，而非低阶抽样。

逐个判断九个真实 $r_3$ 是否在该像里。失败目标保存同时消掉 $U$ 和整个 Krylov 闭包、对该目标取一的完整 315 坐标对偶。不得将某个目标失败写成九个目标全失败。

失败范围准确为：$A^+$ 中固定模 $p$ 初值 $(x_0,0)$ 的下一次提升。它不排除改变该初值、更高来源饱和或其他原有理来源。

当前 $Z$ 是原整数公式的模 $p^3$ 标准代表；与该公式的整数值相差 $p^3$ 倍原来源。用它计算的 $r_3$ 因而只会改变一个原 $\bar A$ 像，完整 $Q/U$ 障碍不变。没有把不同整数代表的 carry 当作零系数。

## 4. 相容时直接继续完整原式

若九个目标全部相容，程序读取其真实解

$$
r_3=\beta^+F(s)+BC\quad\text{在完整 }Q,
$$

其中 $F$ 有七行，$C$ 是七行常数；原 315 坐标逐个核过。恢复原 RHS

$$
\eta=r_3-\beta^+F-BC
$$

的全部原来源 $Aw=\eta\bmod p$，随后组成

$$
\boxed{
Z_{\mathrm{new}}
=Z+K_3F+\sum_i p^{3-e_i}\kappa_iC_i+p^3w.
}
$$

最终继续完整检查

$$
AZ_{\mathrm{new}}=p h_0T\pmod {p^4}.
$$

对 $F$ 不预设常数或一次。其次数来自完整有限 Krylov 解，至多 $307$。若初始真实原 RHS 费用为 $B\le184$，后续 RHS 费用不超过 $B+\deg F$，再由同一原图付出 96 的来源界。实际来源费用全部从原乘回回执读取。

新的 recipe writer 必须按 $923521$ 约化，不能调用旧按 $29791$ 约化的 writer；否则最后 $p^3w$ 会被错误删去。本入口已使用独立的模 $p^4$ writer。

## 5. 单一预算与恢复

精确 CLI：

    PYTHONDONTWRITEBYTECODE=1 python \
      2026-11-14-r150-seven-saturation-runner-789f.py \
      --notes-root NOTES \
      --t96-recovery T96_RECOVERY \
      --all198-recovery ALL198_RECOVERY \
      --out OUTPUT \
      --math-seconds 300 --memory-mib 512 --compile-seconds 30

只需旧 T96 与 all198 两个恢复 artifact。新的当前 $Z$、selector、小状态和完整原整数模型从已落库文件无损恢复，contract 锁定全部 26 个输入与源码依赖。

输入核对、已存整数的直接模约化和六个各不超过 30 秒的编译在数学时钟前。全部新数学阶段共用一个真实 300 秒 deadline，每进程512MiB；每阶段只获得实际剩余时间。SIGTERM 后最多 10 秒保存真数组。

可加 --resume-recovery OLD/recovery，复用完成阶段缓存、VQ 实际数组和原乘积实际数组/源前缀，不重跑已成阶段。两个 VQ 及原乘回有内部真 checkpoint；其他阶段只有完成缓存，不假称内部可续。

所有 generated binary 无损 gzip，超过4500000字节分片。新 text-recovery-manifest.json 额外保存每个 stage-cache JSON 的原相对路径和精确 SHA，避免只在 artifact 留完成缓存。失败也保全部实际原来源、部分数组及已生成余量。

## 6. 唯一成功分支与准确状态

主回执：

    OUTPUT/results/seven-saturation-pipeline-receipt.json

两种已完成分支：

1. outcome = complete-augmented-first-image-fixed-fiber-obstruction，且 newAugmentedFirstImageComplete=true、逐目标兼容性和完整对偶齐全。这只完成所述固定初值障碍，不是原有理来源总否定。
2. outcome = full-original31h0-mod923521-certificate，且 fullOriginalTarget31h0Mod923521IdentityVerified=true、finite_budget_verified=true，最后原十七式、原Macaulay全部坐标、原行单位运输和费用都通过。

只有全商相容不能成为第二种成功；程序会继续原来源和最终乘回。超时或数学错误保 failed-or-incomplete 与实际阶段。

所有分支均保持 characteristicZeroIdentityAsserted=false。即使第二种成功，也只把原 $h_0$ 的一层31分母近似提高到模 $31^3$，其与真特征零归属的距离仍由七关系定理第3节的有限秩和有限有理像条件准确描述。
