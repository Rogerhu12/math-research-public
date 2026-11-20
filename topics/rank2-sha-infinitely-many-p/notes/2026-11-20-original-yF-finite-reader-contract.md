# 原 e/z 有限读数的实现契约

状态：实现与静态证明；尚未实际运行本 helper，不填 e、z、dF 数字。本地只做 AST/来源阅读，数学交给公开 Actions。

## 入口与输入

文件 `original_yF_finite_pole_degree.py` 的唯一主入口为

```python
context, receipt = build_original_first_pole_degree(
    cube_context, ds_context, cusp_context,
    progress=progress, cube_receipt=cube_receipt)
```

`cube_context,cube_receipt` 必须是同次 `build_original_cube_section_fractions(29,first,packet)` 的两个原返回值。`ds_context` 是 `build_original_ds_section_algebra(prime=29,q_precision=817,max_unit_trials=64,batch_size=128,with_frobenius=True)` 的第一个返回值。`cusp_context` 是 `build_original_y_cusp_fibers(prime=29,q_precision=2453,batch_size=64)` 的第一个返回值，包含全原正规化、Fp 上的666截面 core、全部六个真实 cusp 纤维及厚度289局部代数。不得用单独挑选的点或只约化的 cusp 代替它。

helper 不重造大前端，不新选有限域、omega、RF 根或曲线模型。只接受 r=29。cube 的旧 RF 完整 R6 核900必须保留；compact R2 分式不能替代它。

## 实际来源与引用理论的区别

degree180 的输入不是硬填的历史运行数字：必填 `cube_receipt` 内的 `same_authenticated_F_and_P_source.F` 是同次完整混合方程的秩/零度回执，实际检查 nullity144、rank1116、窗口0..1428、同选中原 F 坐标和原 S³。按 R927 已证明的分母投影识别与 RR，得 `2*204+1-85-144=180`。

RF 的完整900×2280矩阵、全部原1140个 R6 recipes、完整2313项核回执和6941项原立方恒等式都来自同一个 cube；其完整核哈希与原回执绑定。R927 的同一 RR 论证给 `6*204+1-85-900=240`。这不声称已经求出整个 RF 极理想。

DS 的原120格与 cube 逐项比较 QQ 的205项来源、实际饱和变换、全部共同模形式/RR/S 系数；Y 的原底格使用已公开同源核对函数。哈希只记录已做过的完整比较，不能替代比较。

## e 的完整有限门

先取原 DS Frobenius F 的 F²，实际验证其为秩102的约化投影。对51个已有原二次残域，以真实幂基 `(e_i,alpha_i)` 和真实乘法关系建立204→102矩阵 C 及102→204矩阵 R。逐分量核完整回代，并核 `R*C=I102`、`C*R=F²`。每个二次乘法使用该原 alpha 的实际最小多项式；不新选二次域。

每个需要的原 M2 成对乘积以409项完整归属门送入 `R2/SR1`，得到 `(f_i f_j)/h`。原 R6 recipe 分成三对，在已经与原代数全回代的直积中相乘，准确得到 `R6/h³` 的约化值。全部900分母同时作用，得到900×102矩阵。

R927 的加强论证给 `deg(M_R(-Z_ell))=882>168`，所以完整限制像就是 RF 正则支集的理想。实现还逐个检验51个因子的像秩为0或2，并直接比较整个像的标准行基与相应完整直积理想的标准行基。故实际 e 是该整个像的维数，同时等于全部活跃二次点次数之和。这里没有把所选单条分母或不完整限制矩阵的秩当作支集度。

本门只需要 R6 的约化值，回执明确标示没有构造全部 R6 的非约化值；输入的 DS 仍是完整204维非约化代数，且每个投影有完整204坐标回代。

## z 的完整有限门

原全部六 cusp 中，选择 xi=infinity 纤维唯一的 `(ambient_dimension,residue_degree)=(289,1)` 分量。原全289幂基的每一步都以实际乘法矩阵核 `nu^j*nu=nu^(j+1)`，最后一行乘为零，并核 rank289。它因此是该原分量的全部局部商，不是一个猜测的截断环。

从 Fp 截面 core 直接 specialize 所有666个 `F_i/J0`，与已保存的原纤维值逐项相等；实际核 J0 坐标组合等于完整纤维单位。用原120×666的 pi2 拉回矩阵，重新核1225项忠实窗口 `2*f_i(u²)`，再送入289幂基。这保留每个六元 recipe 的完整2⁶因子。

全部900条分母的剩余值均检查。若全零，R927 的全局生成性准确给 RF 在底 cusp 有极，故 z=0。否则按原核行顺序选第一条剩余值非零的分母，并使用同一行的配对分子。在原 nu 模289代数中逐次 Newton 求单位逆，每步核完整残差。最后把逆与 RF 值都送回原306维坐标，核 `D*Dinv=e_Q` 和 `D*RF=N`。

真正读出的首个非零指数 j 必须满足 `0<=j<=192` 且 `j%4==0`，取 z=j/2。若289项全零则拒绝，不能猜未知尾或允许更大零阶。原参数的选取只改变首项系数，不改变该零阶。

## 返回值与范围

两个返回值都含整数 `e,z,dF`。context 还保全部实际输入、e_context（原残域编码、完整R6约化值、900限制值、完整正则理想）及 z_context（原厚点、120局部坐标、1140个R6局部值、900分母残值、所选配对分式和完整RF局部值）。大矩阵只留内存。

receipt 含全部来源/维数/点身份/框架/矩阵哈希与具体接受门。结论采用 R927 的严格公式 `dF=2160+9*(e-z)`，并核 dF 为18倍数、1296<=dF<=3078、dF不等2256；原循环分支记录为 `F_first` 或 `P_first`。

本门不计算完整全局 pole ideals、四大交除子或 shadow，也不声称 ordinary 非零或无穷多个素数。所有这些状态分开列出。

## 源文件依赖

helper 的直接依赖为自己、`original_section_ring_embedding.py`、`section_quotient_algebra.py`，`source_dependencies()` 返回实际 Path，`SOURCE_DEPENDENCIES` 给文件名。完整 pipeline 还需沿 cube、DS、Y正规化与六 cusp 原前端保留全部传递依赖；root 的 host/producer 已列同一25项 manifest。没有调用旧 eta48 函数域前端。
