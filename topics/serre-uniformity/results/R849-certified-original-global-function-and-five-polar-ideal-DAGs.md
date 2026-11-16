# R849：原全局函数、五个极理想与 η 输入的准确表达式已完成

日期：2026-11-16。会话：serre-public-astra-20261115。

**状态：本项实际完成。** 原 p=41、f=f4 及五个 g_j=(1+T^j)f 的全局函数、
两图完整极理想、原 η 的 Picard 输入和真实三同源主函数比较，已装配成
**523节点**的有限准确表达式。全部43个非零义务绑定原证明或真实单位子式。
这里的完成对象是有完整原叶的准确表达式，不声称已展开全部系数、物化理想
HNF、求得标准 Jacobian 坐标、证明 η=0 或算出高度。

实际 run [43790410670](https://github.com/Rogerhu12/math-research-public/actions/runs/43790410670)，
compute job **133047363582**，source
**391191590dcb8bcc6f8f2d777610726fa79dc2a3**，
于 **2026-11-16T02:13:18.010890+00:00** 完成。
核心用时 **5.019478116 秒**，两个新数学阶段为原来源审计和完整表达式图；
没有重新执行旧数值算术。

## 1. 原全局函数有具体、完整的叶

本项直接消费 [U.1 原单位解](../notes/R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)
及 [GP 全局三子式证明](../notes/R839-original-global-addition-polar-ideals-and-eta-DAG.md)。

原2420阶单位图 M、右端和自由列1186确定唯一原规范解
\[
 \xi=M^{-1}r,\qquad B=Zc,\qquad
 A=\sum_{i=0}^{1233}a_iF_i^{(5)},\qquad
 B=\sum_{i=0}^{1233}b_iF_i^{(5)}.
 \tag{849.1}
\]
U.1 的完整核维数28与原单位子式证明给 A=y_fB、B≠0。
所有1234个原 real 行、原 Z、R781的130个既有 Laurent 阶段、κ、
原行列顺序、129×20×14关系及原缩放均实际在2709件来源闭包中。
本次不是把四个 CM 响应推广为全局函数。

在原272阶正规基上，完整 W 有34组全局坐标。令 χ(z,T)=det(TI−W)，
T为原 w=e2/τ，原真实循环子式保证它是特征零中的本原模型。
同一函数域中用
\[
 \partial_z F(z,T)=F_z-F_T\frac{\chi_z}{\chi_T}
 \pmod{\chi}.
 \tag{849.2}
\]
原可分性给 χ_T≠0。全部原六个 C 的12组准确坐标、完整
S5的1380×1234表示及按需Krylov单位解都作为准确有界表达式叶/运算保留，
没有以五个纤维值替代全局多项式矩阵。

因此图实际给出 A/τ5、B/τ5、u=y_f、u²−b和原全局 ∂_z u，
再由原 C_j/C0、ρ_j与真正 σ_j 生成五组同靶相对函数
y_{T^j f}、x_{T^j f}/x_f及h_{T^j f}/h_f。
非零导数和相对x差由原非零Hom及特征零函数域证明；
不取任意立方根，也不进行未知的椭圆曲线除法。

原 field 描述仍是 M+=L(tξ) 的280维描述；关系系数域 L=Q(B_fld,s)
仍为14维，每个 Laurent 系数保20个实圆分坐标。
旧初始 chart 的历史 all-branches 旗标维持原 false；
完整原关系由已绑定的 U.1/R840 后继证明承担。
两次启动格式修复见
[旧R791 ZIP](../notes/R839-global-polar-old-R791-ZIP-contract-fix.md)和
[原field/chart](../notes/R839-global-polar-original-field-and-chart-schema-fix.md)，
不把这些失败登记为数学反例。

## 2. 五个完整极理想，包含全部重数

令 E_P=(y_P)∞、I_E=O_Y(−E)，把它们作为原函数域中的分式理想保存。
R845 已有原 I_{E_f} 的八个准确生成元；σ图与τ图由原
(τ/σ)^11运输。消费者沿原完整char0单位解保这些八叶，没有把其模kernel
当作特征零系数。

对 P=f、Q=T^j f，GP.7 给
\[
 I_{E_{P+Q}}=I_{E_P}^3I_{E_Q}^3
 \bigl((x_P-x_Q)^3,\,(y_P+y_Q)^3,\,
       (x_Py_Q+x_Qy_P)^3\bigr).
 \tag{849.3}
\]
三个立方都在原 L(Y)。证明使用原始齐次坐标的反对角概形理想、
光滑曲线DVR中的理想立方、以及φ的有限平坦下降；
因此包括 O/O、二挠、分歧和所有局部重数，不是只给一张图上的支撑。
不能把 (f1,f2,f3)^3=(f1³,f2³,f3³) 外推成一般多变量环的恒等式。

本次五组输出实际给出了两图 I_{E_{g_j}}；
原群律同时附加准确 y_{g_j}。原 Hom 字、映射次数及整数规范为：

| j | 原Hom字 | deg(g_j) | p_j | q_j |
|---:|---|---:|---:|---:|
| 1 | 1+T | 2970 | 165 | 67 |
| 2 | 1+T² | 1674 | 93 | 67 |
| 3 | 1+T³ | 1800 | 100 | 67 |
| 4 | 1+T⁴ | 3024 | 168 | 67 |
| 5 | 1+T⁵ | 3339 | 371 | 134 |

这些原次数和方向直接消费 R791/R844，没有重新识别 Hom。

## 3. 原 Picard 输入和主函数的方向

令
\[
 I_{Z_j}=
  N_{L/K}(I_{E_{g_j}})^{q_j}
  N_{L/K}(I_{E_f})^{-p_j}.
 \tag{849.4}
\]
图保两图中的同一度零分式理想。原 η 输入是
−[I_{Z_j}]/q_j；负号来自 I_Z=O(−Z)。
原 h_j、极化κ和 R791/R794 的运输不变。

原α3=1−ζ²及其指定靶坐标给
\[
 I_{E_{h^R}}=(y_h^2-b)\,I_{E_h}^{\,3},
\qquad
 \mathcal R_j=
 \frac{N(y_{g_j}^2-b)^{q_j}}{N(y_f^2-b)^{p_j}},
\]
\[
 \boxed{I_{Z_j^R}=\mathcal R_j I_{Z_j}^{\,3}.}
 \tag{849.5}
\]
这是正乘原主函数的方向。真实七次σ范数同时作用原 b、ρ和全部
常数；不以固定目标上的T次幂乘积代替，也不删除非零常数。
五个非零比较函数及五个实下降极理想都已在图中明确给出。

R848原c0首项和R844/R847原c1值/一阶可消费同一主函数，
但本run本身没有计算c0帧，也没有把这些局部输入自动等同于完整
Poincaré刚性化。后续须在真实线丛中使用 (849.5)，保原纤维标量。

## 4. 实际来源、配置及留存

[执行契约](../notes/R839-original-global-polar-expression-consumer-method.md)
SHA **aeea87f4f9723774581a5290feb543bee6ae15ab1abe78307cf7583f01f5aefc**；
GP纸证 SHA **520bfbd521cadfeff2b519c864217a56258a991a07039ee33e923db7e9be4e0a**。
[公开请求](../notes/R839-global-polar-DAG-public-request.json)、
[核心](../scripts/R839_original_global_polar_DAG.py)、
[包装器](../scripts/R839_public_original_global_polar_DAG.py)按冻结原身份运行；
实际请求 SHA **39ec19929157f886f8b4bd32475bff2945611399be2988a42499923fe5524bdf**。

2709件原来源分组为 R7871241、R781134、R7866、R80645、R8091260、
R8408、R8458、R7917。完整来源身份指纹
**a2839071469186a9563e507632267c3c6f9fb1ef34e2407203596d3bcb1670ab**；
本次数学配置指纹
**87a0e26e7b0c6677905313753e4e2a36ea82e9e6a33d6f32d6d6cf7616e13183**。

| 项目 | 字节 | SHA-256 |
|---|---:|---|
| 数学核心 | 48121 | 544241acf5f3451df34c779d513ea6494616d4d4caa26cd2531749edc895aea7 |
| 包装器 | 36428 | 39bef61981f6c2193e64cd1797331a0ce9340ed468fc93dc785d8994c8d2a541 |
| 最终证书 | 7447 | b50df2dfd37a7610659fa5f9bc37b81078ba6e95508c9196f1056bef1c9c60b7 |
| 523节点准确表达式 | 202890 | 529822ba7ab26beeb06de8aeb466eedd3de63326e019e6b9a041096e554a2e79 |
| 原来源审计 | 5340 | 3df16cb4ec814bc3909c6aa2a3bd95226cb254048aa5ba7d1eb8995703264fef |
| 两阶段manifest | 2957 | d3dd9464c79be9faf4249083d49d0399ac6c03cdbd13238606e07ba17adb351f |
| 全输出manifest（12项） | 2144 | cdc06c91e9a981bf025402df732686de7415637d5e13f28552f773bb08e05cdd |
| 原source inventory | 449832 | e9a986c45970f2d16ac2ee054e22ab4ce01de7b19f5d8eb224018d66d686a9d0 |
| 2709件原来源载体 | 395061658 | 6a0a5d8cc918f1802662865dfaf254987f33086191ce01e9169ec789b5456703 |

最终文件为 p41-original-global-addition-polar-ideal-DAG-certificate.json；
主表达式为 R839-global-polar-exact-global-function-and-five-polar-expression-DAG.json.gz。

一日 artifact **14192171293**，名称
serre-global-R839-original-global-addition-polar-ideal-DAGs-43790410670-1，
ZIP **396226833B** /
**6a52068e04e91bc7b45b13de08a143ca2baef4a3bdfd1f8fac9bab1946d94083**，
到期2026-11-17T02:13:18Z。
根以11次Range读取11个小成员，共1167594B，核其全部原SHA和配置；
没有下载或声称重哈希整396MB ZIP。原大载体由本次producer按2709件
原来源封装，继续只在一日artifact中保留，不进入Git/Release。

本结果关闭“原五个全局极理想及η输入尚无完整具体表达式”的缺口。
原理想格的展开与标准化、η的准确零判、原高度/周期及全p共同根证书
仍按实际未完接口继续；不能从表达式存在推出这些后续结论。
