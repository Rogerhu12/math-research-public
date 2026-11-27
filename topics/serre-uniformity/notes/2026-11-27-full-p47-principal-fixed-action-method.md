# 原 full47 principal 家族的完整 fixed-cycle cusp 作用

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

## 新目标与原整家族

R1087 已证原角代数 $K_{23}\times K_{48}\times K_{16}$，
原 $Z_{\rm ps}=K_5-K_{25}$ 以及两处整 projector。
本次新输入是原类和的实际角系数和
$e_{\rm cusp}\mathcal F_4^*Z,e_{\rm cusp}\mathcal F_3^*Z$，
正是 R1087 (1087.21) 的两个原 CM 点的 endomorphism 系数。
不重算 R1081 Gram/Hecke 或原 $L'$。

同时用十一真 split regular 共轭类 $\mathscr K_{5^r}$，$1\le r\le11$。
其元素 order 为 $46$ 或 $23$，均不能固定原 necklace；
原整 orbital 计数及 degree $2256$ 沿 R1087 的证明逐类适用。
其 principal 值为 $47s_r$，$s_r=\zeta_{23}^r+\zeta_{23}^{-r}$；
cusp 值严格为零。
取十个原整对应
$$
Z_r=K_{5^r}-K_5,\qquad2\le r\le11.
$$
每个 degree/trace 均零。
十一项 $s_r$ 线性独立：关系给常数项零、次数至多 $22$ 的多项式，
若被 $\zeta_{23}$ 杀则须为 $\Phi_{23}$ 的倍数，常数项又迫该倍数为零。
又 $\operatorname{Tr}s_r=-1$，所以十个差准确张成 principal trace-zero 空间。
原 $Z_{\rm ps}=-Z_2$。

## 全部 projective 类与原二十三维基

PGL 矩阵用唯一代表 $(1,b;c,d)$（det 非零）及 $(0,1;c,d)$（$c\ne0$）。
共轭类由 $({\rm tr}\,g)^2/\det g=(a+1)^2/a$ 严格识别。
在原 $x_0^2=-I$ 上实际作 $gx_0g^{-1}$，按原角及每个原目标计数。
每个角全部 $d_C$ 个目标必须具有相同整数重数；
不能只把总数除以 $d_C$ 后不核目标。

仅重建本次计算需要的 R1081 composition/trace 数组，
并强制比对原两个 SHA-256；不重跑旧中间点枚举、LDL 或 Hecke。
实际关系 $I=-\sum_C R_C$ 必须保留，故真正的基乘法是
$$
R_AR_B=\sum_D(n_{AB}^D-\mathbf1_{A=B}d_A)R_D.
$$
另核全负一向量确为乘法单位。

新 $Z_{\rm ps}$ 的乘法矩阵应 rank $11$，
charpoly 为 $T^{12}m(T)$。
核实际 $m$ degree $11$、不可约及 $|m(0)|=23\cdot47^{11}$，
形成原 $e_{\rm cusp}=m(Z_{\rm ps})/m(0)$。
核其平方、rank $12$、被 $Z_{\rm ps}$ 杀及在 $4513$ 的整性。

## 完整 fixed transforms 与全部 cusp characters

设恒等角系数 $z_1=0$。原变换准确为
$$
(\mathcal F_4^*Z)_A=z_{[2A^2-1]},\qquad
(\mathcal F_3^*Z)_A=z_{[(3A^2-1)/2]}.
$$
保 $A=0$ 和映到恒等角的零项；它们不是代数同态。
先在真 QQ 角代数中求 $Z_{\rm ps}$ 的两个 cusp 投影、
十维家族两个及联合映射的 ranks；零值也如实登记。

在 $\mathbf F_{4513}$ 中从声明的有限 $t$ 候选取
$G_t=R_0+tR_2+t^2R_3$，只有完整 degree-$23$ charpoly squarefree
时才作同时 character 读取。
十二个 linear factors 是全部 cusp characters，另一个 factor degree $11$。
核原有理因子 degree $4,8,11$ 及每条 eigenline 上 cusp projector 为一。
这不把 angle root 任意认成某个尚未配对的 Hecke root。

对每个 cusp character，读十个原 $Z_r$ 的两行
$\vartheta(\mathcal F_4^*Z_r),\vartheta(\mathcal F_3^*Z_r)$，
记录实际 rank；若 rank 二，另给一个真非零二阶 minor 的索引和值。
同时给原 $Z_{\rm ps}$ 两个 scalar。
不强制预期 rank，不以整体 endomorphism 非零代替逐 character 非零。

R1087 的实际
$$
23e_{\rm cusp}d_Z
 =\tfrac12 e_{\rm cusp}(\mathcal F_4^*Z)u_{1728}
  +\tfrac23 e_{\rm cusp}(\mathcal F_3^*Z)u_0
$$
说明：若某 character 两行 rank 二，任意非零的二元剩余 CM 读数
可被家族某个整组合读为非零。
必须另付那个实际 CM 读数非零；本次不推点类、对数、全局高度或 MW 单位。

## 执行、来源与预算

一个公开 Actions job；固定已用官方 SageMath $10.6$ digest，
总数学预算 $120$ 秒、预留 $10$ 秒。
读实际 .git HEAD/refs 核 GITHUB_SHA，不依赖镜像内不存在的 git。
先核请求、全部源码和两 README SHA，再导入数学并保持 proof.all(True)。

stdout 仅新类和短系数、ranks、十二个 character 小摘要、run/source/hash
及预算回执。完整矩阵和数组不提交、不上传，不生成 artifact/Release。
失败保准确阶段；不把未完成或条件输入当成结论。
数学来源为已证 R1078、R1081、R1083、R1087 和上面原家族证明。
root 与 o1_theta 已全文逐行纸审实现及方法，核准原共轭类、真实基乘法、完整fixed变换与逐character两行秩；尚无新数学执行。
