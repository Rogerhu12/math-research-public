# 新输入：h=k、Delta=0 的正确 RWO 原 Q 投影

日期：2026-11-28（Asia/Taipei）。Astra-ISP-8542378f-20261127；GPT-6 Astra Pro（AI-assisted）。

**尚未执行。** 固定180秒/4GiB，共用最外层绝对截止。这里只续旧错误第二曲线撤回后的真正原输入，不重放原 Delta/Tnum 投影或已冻的两个 Loww-z 投影。

## 1. 准确作用域与必要来源

限于对称原 $h=k$、$\Delta=0$ 图，保留
$$
ABQ(1-Q)P_f\,bcP_{02}\ne0.
$$
这是[正确五原行](../results/R150-appendix-unit211-h-equals-k-corrected-five-original-rows-and-three-physical-cofactor-conditions.md)已证明的准确图。没有假定 $P_f$ 在整个碰撞支自动为单位；其零支仍独立保留。

沿该页原公式取 $\Delta=\Phi N_F-S\xi P_f$、$T_n=P_fN_C-P_cN_F$。同一原 $NV$ 给
$$
P_fNV=T_n-bc\Delta z,\qquad z=Qt.
$$
故本图每个原点满足 $\Delta=T_n=0$。

本次仅取正确 f33 源的5121 B原 R/W/O 定义前缀；SHA256
325c32cb81f37b3f31affd4e98f01c39fcee75b2cc0eae1d9cbb079edaf6d078。
不会进入原 N1、五行输出、三组 cofactor 证书或因式门。

已证真 $F_{61,17,9}$ 作为新投影的必要输入，只按原 RWO 三行和已刊因式商定义再生：
$$
C_1=\frac{(2\lambda-1)^2 Z^3}{56668397794435742564352}\,F_{61,17,9},
$$
$$
Z=B^4u^2-2A^3B^2u+A^6Q=-4B^4bc(1-Q).
$$
其5855项规范 SHA256 必须恰为
69babd37fc45ade649b12b4b849151574080a2bf92c7c2266141d17be1a9d999。
这仅定义输入，不重做已登记的三组原 cofactor 结论。没有采用旧 $R_{\mathrm{bad}}$ 或旧第二曲线 $M$。

## 2. 一个真正新的固定 Q 目标

清 $\Delta$ 的已付分母并只剥当前图已有因子，得 $D_2$。新目标仅为
$$
M_{\mathrm{raw}}^{\mathrm{true}}(\lambda,u)
=\operatorname{Res}_Q(D_2,F_{61,17,9}).
$$
两条的固定 Q 次数为2与9，即11阶 Sylvester 行列式。精确 QQ resultant 的共同有限根必要性包括所有 Q 首项为零的专化，不以任何 Q 首项作为除数。

先完整报告这个新原结式，再剥与 Q 无关且已有原证明的支持：
$$
A,\ B,\ \lambda,\ u,\ u-1,\ S.
$$
其中 $u\ne0$ 由347c的真 dual 零基点 mean 全排除及非零共同缩放支付，静核见[本次来源说明](2026-11-28-unit211-original-u-zero-scaling-static-audit-8542.md)；
对称 $u-1$ 只能引用[新的6516整纤维证明](../results/R150-appendix-unit211-h-equals-k-entire-symmetric-u-one-original-exclusion.md)，不引用旧 $p=1$ 的 $u_{\mathrm{old}}=1$。
$S$ 来自已单独全文核对的三份真实原源。没有支付一般 $m,\Phi$ 或新的几何范数。

若新结式为零，保留它并不作有限或排空结论；若非零，所有未付因子完整保留。

## 3. 复用独立旧 P，不重算已登记投影

旧独立的 $\Delta,T_n$ 相容曲线
$$
P(\lambda,u),\qquad \deg_{\lambda,u}P=(28,3)
$$
不涉及错误 Rbad，规范 SHA 为
8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c。
其第一次真实计算为run46025096446/job140594347573。

为不重算这项已登记的4阶投影，工作流只按根规矩15用终端 git 从历史提交
ac40c96b0cfb3758fbf8bd380d18ca288a23601f
取当时的原回执到 runner 临时目录。程序仅在内存中读取指定 SHA 的独立 P，检查完整规范 SHA 与双次数；不解码或使用旧错误 M，不打印、传输、保存或重新提交任何系数载荷。当前主线已经清理的数据回执保持不变。

新的 QQ 运算是 $g=\gcd(P,M^{\mathrm{true}})$，且两次整除全部乘回：
$$
\{P=M^{\mathrm{true}}=0\}
=\{g=0\}\cup\{P/g=M^{\mathrm{true}}/g=0\}.
$$
非恒定共享曲线及全部交点都保留。若 $g$ 是非零常数，只给有限不同 $(\lambda,u)$ 基点界
$$
(\deg_\lambda P)(\deg_uM^{\mathrm{true}})
+(\deg_\lambda M^{\mathrm{true}})(\deg_uP).
$$
理由是固定 u-Sylvester 行列式的次数界；每个固定 $\lambda$ 上不同共同有限 u 根给独立评价列，迫相应阶数的行列式零。两多项式没有公共曲线才允许此有限性，不把多变量 gcd 为一误作无解。

本次不展开该更大的 u 结式。完整 Q 纤维、自由 Gram 及个别谱条件全部仍须原处理；有限投影基点绝不等于排空碰撞支或完成 ISP。

## 4. 执行与边界

新源 SHA256：3fcc2e90677b7bbd0247d72c1922fc6ed0b60da4ced715a7cecbeae656aade33；9871 B。

唯一代码依赖是正确 f33 源，完整 SHA256
2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2。
历史数据只作上述已登记独立 P 的临时输入。所有输出仅含定义、次数、项数、字节数、SHA和实际状态。

若新目标、历史 P 读取或新 gcd 任一阶段未完成，只保已经真正返回的部分，不提高预算或重启资源门。原错误848/578界仍撤回；新输入未实际返回前不预记新的有限界。
