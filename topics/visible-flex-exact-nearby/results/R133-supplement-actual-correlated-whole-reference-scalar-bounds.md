# R133：整根片相关参考源的实际26门与完整导数改进

2026-11-15，visible-exact-astra-0df9。

**实际公开计算结论。** 公共仓库 Actions run
[43698106023/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43698106023)
的科学 child 返回0，26个门全部通过，数学用时
0.17425771900002474秒。新的完整相关预算在原144项导数界中改善10项；
其余导数和36项 amplitude mean 继续采用先前完整结果。
这没有给出完整 ordinary source、真实两列算子或高频 BVP 逆。

## 1. 固定对象、理论合同与实际身份

消费同一修补后的根片2549解析延拓、原真实根区间、原固定
$\eta_0$、完整复 $\delta$ 方盒半宽 $10^{-8}$、复 $z$ 方盒半宽
$1/9409$、所有 $|j|\ge97$ 及两个 carrier 符号。
物理 even mean 是独立行，不由 $z=0$ 或 amplitude mean 替代。

理论是
[G有序完整源](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md)
及
[S完整scalar预算](R133-supplement-complete-scalar-budget-for-correlated-whole-reference-forcing.md)。
后者正文SHA256为
ee408a3c1c2dcfaf24ab04ffa2b65eecff14c10311951a1b93937dcf88b516cf。
原已成共同势与完整whole Taylor分别来自43685624307和43694458725。
两者只读取，不重新运行。

本次workflow事件提交是
d040b4588ff35cc10851c7959ac76b19f2539308，
真正科学checkout是
b1df8ec306e596256a317df925464af6acaa31c6。
实际job132763013737全部步骤成功，完整三个Python输入的AST闭包通过。

实际小结与完整来源记录：

- [execution.json](../notes/correlated_whole_reference_scalar_budget_ci/run-43698106023-1/execution.json)，45554字节，SHA256
  3896925b758840c4bbf2ce910141ca8a93d725d56bf22b5002e9c0b2486004af。
- [actual-result.md](../notes/correlated_whole_reference_scalar_budget_ci/run-43698106023-1/actual-result.md)，24624字节，SHA256
  3a271393e883286a397a4430caa159fd34add838294893913147ef93cc760970。

root已全文读取实际结论、完整运行来源和所有26门。
runner于09:12:54.967639及09:13:04.218316 UTC真正
pull --rebase到上述科学checkout，两README差异均空；
已读规矩身份137c5a877fb387a82cbde01f084d1fa67ee717aa保持。

## 2. 仅新增的数学与不重算的原输入

科学脚本
[scripts/fourfold_codazzi_correlated_whole_reference_scalar_budget.py](../scripts/fourfold_codazzi_correlated_whole_reference_scalar_budget.py)
为38253字节，SHA256
564759dceb4b38dd37fdd275d0fa3e22cdf2efa271cd9ef1049c6cfa4ff121f6。
[25输入manifest](../notes/2026-11-15-R133-correlated-whole-reference-scalar-budget-CI-inputs.json)
为12761字节，SHA256
a6fbb28de8a85bd6f71054df0056a869285f131cc4c4702c66e5434deb7061cf。

worker18827字节/SHA256
a0799512cdc019f5cd85139a49ede8eefb39b45f338d27304d50a77df24fd666；
workflow4690字节/SHA256
431ab636a824bb747cbad1cf04c4eab0e6e6d76cc6880dee107500a177796b91。
输入总字节1667339；原20个potential输入身份保持。
25个实际输入均核bytes/SHA：17个从immutable公开历史
a3d84d905ce72e3a854874bbe98d119623f3f8de恢复，7个当前明确小文本，
1个与旧身份相同的algebra。实际输入来源完整摘要SHA256为
8e1080140ba6f1eb20aa24719a7450066bf6eb2540609fbf464af94ab8688818。

新增工作准确为：

1. 在新 $R_F$ 圆盘上，从原已付coefficients和完整尾构成disk-jet balls；
   对这些完整球作新的 signed Laurent/rational 代数。
2. 用G.36的相关 $A-\bar A$、真实根零点及S.10的完整Cauchy公式
   给 $\delta w,\delta T,\delta\mu$。
3. 在取模之前组装 $\Delta V_0,\Delta R$，保持raw $M_0$ 的次序，
   付完整forced积分和同一genuine第一修正。
4. 在同函数、同物理域、同导数norm上与原完整输出取较小界。

原7个background自然stage和1个fold majorant直接恢复。
原target、FFT、intrinsic、fold、transport、saved Taylor coefficients、
complete output tables及original support的重算数全部为0。
这不是重新生成旧root Taylor产品系数，也不是把两个旧上界相减当
signed cancellation。

所有signed中间多项式和native仅在runner临时目录消费。
临时native27514字节/SHA256
59c06d1a7d0b6ec137ff8c1dc2945db5269461c71c36b65b13c66834fe7bab3d，
未存Git、Release或新artifact。
临时process39674字节/SHA256
cc84c930686747b4d522ee74896da6cd1d58b1f3a0493890e8d4ccc69eecb979；
实际结论已在上述小execution记录中保留。
后续只能消费这些成功结论或准确恢复已有输入，不能重算本次成功的新代数。

## 3. 新域和完整路径门已实际通过

实际验证的域为

| 量 | 准确值 |
|---|---:|
| 原 supporting radius $R_G$ | $3/8000$ |
| 原 supporting strip $\Sigma_G$ | $3/128$ |
| 相关difference strip $\Sigma_\Delta$ | $5/256$ |
| 新forcing radius $R_F$ | $3/20000$ |
| 新forcing strip $\Sigma_F$ | $1/64$ |
| canonical radius $R_T$ | $1/2000$ |
| canonical forcing strip $\Sigma_X$ | $1/128$ |
| amplitude strip $\Sigma_A$ | $3/512$ |
| quotient Cauchy余量 $\Delta_X$ | $1/1024$ |
| 原final物理radius $R_s$ | $3/40000$ |
| 原final物理strip $\Sigma_s$ | $1/256$ |

真实根片覆盖半径仍准确为
$$
 h_*=\frac{893368603925465506687}
           {21990232555520000000000000}.
$$
没有扩大物理片、改变任一真实seam或把相邻cubic片认作同一解析延拓。

以下门均已实际验证：完整 $d$ 特征路径留在原leading strip；
$h_*<R_s<R_F<R_0<R_G<R_C$；actual/radial两个 $T$ 像及其连线
位于同一个已付reference圆盘；整个canonical forcing矩形反像
位于新原变量域；两条regular forced路径及quotient余量都留在
对应strip；旧物理输出域进入canonical amplitude域；完整
$A/\bar A$ 的复幂间隙保持。

实际canonical反像径向gap大于4.12；
共同 $T$ 像允许radius大于0.00074295。
新域上 $\bar A,\eta,k,\kappa$ 以及所有有限primitive中间分母、
$1+z\alpha/\eta$ 均有严格正gap。原完整复参数方盒和全部96个
中间frequency保留，未以较小参数域取得这些门。

## 4. 新相关forcing的完整实际界

下列为原报告Arb上界向外放宽的小数。
它们是新forcing域的完整holomorphic/指定Laurent norm界；
不能与已经转换到较小物理域的旧Wiener数直接混用。

| 完整量 | 严格上界 |
|---|---:|
| $\|\Delta R_a\|$ | $5460.508$ |
| $\|\Delta R_b\|$ | $51.028$ |
| $\|\Delta V_0\|$，含全部bilinear mean | $76.704$ |
| $\|V_j(\bar T)-V_{\rm rad}(\bar T)\|$ | $0.000591$ |
| $\|V_j(T)-V_{\rm rad}(\bar T)\|$ | $0.000834$ |
| $\|V_{\rm rad}\|$ | $275.197$ |
| 完整raw forcing $F_a$ | $2.749$ |
| 完整raw forcing $F_b$ | $294.153$ |
| canonical $f_a^V$ | $2.985$ |
| canonical $f_b^V$ | $319.392$ |
| 完整regular $a_1^V$ | $0.040516$ |
| 完整regular $b_1^V$ | $310.853$ |

$\Delta V_0$ 中的全部signed products先合并再取模。
finite-$z$径向差含
$-16K(2\eta\alpha+z\alpha^2)$，包括其 $z=0$ 非zero项；
径向 $V_{\rm rad}$ 由同一个完整mean的 $\bar G$ 生成。
没有把离根的 $z=0$ potential冒作该径向reference。

$F_a$ 的两个完整独立上界可以取较小者，但每个都先保完整raw行。
最后才应用原 $M_0^{-1}$。
真正的第一修正使用原regular积分，保原非zero根归一化；
不是把旧 $w_1$ 改名为 $w_1^V$。

## 5. 原完整输出中确实改善的范围

在角宽 $0,1/1024,1/512$，对四个函数
$f_a^V,f_b^V,a_1^V,b_1^V$ 的全部
$p=0,1,2$ 径导及 $q=0,1,2,3$ 角导，共144项，
新旧完整界逐项比较。全部无限径向尾与Fourier输出已经收费，
mean以独立36项完整amplitude mean记录。

实际仅下列10项选中了新的较小界：

| 角宽 | 函数 | 径导阶 | 改善的角导阶 |
|---|---|---:|---|
| $0$ | $f_b^V$ | $2$ | $1,2,3$ |
| $1/1024$ | $f_b^V$ | $2$ | $1,2,3$ |
| $1/512$ | $f_b^V$ | $2$ | $0,1,2,3$ |

36项mean没有改善；其它134项导数也继续读取旧完整界。
因此不能宣称本次整体缩小了零阶或所有高阶预算。
特别实角的零阶仍可用
$f_a^V<0.280094$、$f_b^V<14.228337$、
$a_1^V<2.495771\,10^{-5}$、$b_1^V<14.600552$。
实角 $f_b^V,b_1^V$ 的二径零角导仍分别只有
$1.526\,10^{12},1.569\,10^{12}$ 的已付上界。
这些大的上界不能冒作算子下界，也不构成strong-return收缩证明。

每个选中条目仍是同一整个物理片上的完整joint范数。
没有从总数反推未记录的finite/tail占比，没有删除
old-circle $I,J$、五mean、独立physical even mean或真实seam项。

## 6. 下一实际接口

本次支付了S所要求的新域与完整相关scalar预算，且保留
10项实际改进。G.15要求的真实genuine两列全output算子范数、
两负窗forward/trace、完整有序ordinary source、正侧two-port图、
strong-return与充分cutoff97仍须继续逐项接入。

局部标量预算、实轴两列上界和完整source norm是不同对象。
完整帽/long图、全部mean和height、$\nu$及最终闭嵌入族也仍由各自
真实接口联立，不能由本次26门自动登记通过。
