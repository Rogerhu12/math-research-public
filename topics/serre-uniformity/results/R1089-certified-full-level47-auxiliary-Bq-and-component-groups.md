# R1089：原 full47 的两个辅助 (B) 证书及完整分量群条件

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
状态：**已证明；两个新 $T_q$ 精确计算均成功。**

对原 $J=\operatorname{Jac}(X_{\rm ns}^{+}(47))$，
$$
\boxed{\#J(\mathbf F_{283})\equiv70\pmod{283},\qquad
       \#J(\mathbf F_{4513})\equiv551\pmod{4513}.}
\tag{1089.1}
$$
故这两个辅助素数均满足 $(B)_q:q\nmid\#J(\mathbf F_q)$。
原坏 $47$ 几何分量群的指数为 $46$，所以二者也都满足
所有分量群阶与 $q$ 互素的条件。
本篇不推原 MW 饱和、具体 CM 首对数或高度单位。

## 1. 新执行回执

- source：
  [1f0e3604a87d4b574c708ddcc0ab1b17852f09f1](https://github.com/Rogerhu12/math-research-public/commit/1f0e3604a87d4b574c708ddcc0ab1b17852f09f1)；
- [run45941243499](https://github.com/Rogerhu12/math-research-public/actions/runs/45941243499)，
  [job140315814260](https://github.com/Rogerhu12/math-research-public/actions/runs/45941243499/job/140315814260)，
  attempt 1，所有步骤及 job success；
- 完整数学耗时 $21.248974477$ 秒，预算 $600$ 秒，预留 $30$ 秒；
- SageMath $10.6$，已固定同一个官方 image digest，全部 exact rational/integer 运算；
- root 与 global_route 提交前全文逐行纸审；root 核完整数学日志和最终 success。

旧 R1080 原 full new Fricke-positive 空间只作为新 $T_q$ 的输入重建：
ambient/cuspidal/new 维数 $189,165,157$，
逐实际因子核 Fricke 矩阵 $\pm I$，
正号完整因子维数为 $16,24,33$，负号总维数 $84$。
未重新计算 $L'$、旧 $H_t$ 分块、角 Gram 或任何旧点筛选。

## 2. 从完整 Hecke 多项式到原有限域点数

原 Chen–de Smit–Edixhoven 有理同源
$$
J\sim_{\mathbf Q}J_0^+(47^2)^{\rm new}
$$
已由 R1080 固定。它给每个良素数相同的 Frobenius 多项式和点数；
不要求同源的次数与该良素数互素。

对每个 $q=283,4513$，在原三个完整因子上计算
$$
P_{q,i}(X)=\det(X-T_q\mid V_i)\in\mathbf Z[X],\qquad
P_q=\prod_iP_{q,i}.
$$
特征多项式先在 QQ 精确形成，再严格转为 ZZ 多项式，所有分母必须为一。
逐因子首一、degree $16,24,33$，完整乘积首一、degree $73$。

Eichler–Shimura 给每个特征嵌入的 Frobenius 多项式
$T^2-a_qT+q$。在 $T=1$ 评价并对全 $73$ 个嵌入相乘，得到
$$
\#J(\mathbf F_q)=P_q(q+1)\equiv P_q(1)\pmod q.
\tag{1089.2}
$$
$P_q$ 是 $73$ 次 Hecke 多项式，不是 $146$ 次 Frobenius 多项式。
程序同时用完整多项式和三个因子的正整数值核
$P_q(q+1)$，并逐项核模 $q$ 等式。

实际余数为：

| 原因子维数 | $P_{283,i}(1)\bmod283$ | $P_{4513,i}(1)\bmod4513$ |
|---:|---:|---:|
| 16 | 265 | 1679 |
| 24 | 196 | 3031 |
| 33 | 201 | 4141 |
| 完整乘积，维数 73 | **70** | **551** |

各因子与完整乘积都非零。
没有只计算一个简单因子，也没有省略某些 Galois 嵌入。

## 3. 实际 $B_q$ 的整可逆性及原 CM 对数深度

令 $B_q=q+1-T_q$ 是原 $J$ 的实际整 Hecke endomorphism。
它在原 Hodge 空间的 determinant 正是 $P_q(q+1)$。
由 (1089.1)，这个 determinant 是 $\mathbf Z_q$ 的单位。

$B_q$ 延伸到原好约化阿贝尔模型。
其对实际 Hodge/Lie 格的矩阵整且 determinant 为单位，
因此对两格均为 automorphism。
也可直接对 $P_q(q+1-X)$ 用 Cayley–Hamilton：
常数项是单位，给 $B_q^{-1}$ 为实际整 Hecke 算子的
$\mathbf Z_q$-线性组合。
所以没有经一个未经检验的同源运输整格。

因 $\#J(\mathbf F_q)$ 与 $q$ 互素，
$J(\mathbf Q_q)$ 的 pro-$q$ completion 就由其形式核 $J_1(\mathbf Q_q)$ 读取。
对 $q>2$ 的好约化形式群，
$$
\log_J:J_1(\mathbf Q_q)\ \simeq\ q\,\operatorname{Lie}(\mathcal J)(\mathbf Z_q).
$$
将任意点乘以与 $q$ 互素的群阶即可进入形式核，故原全局对数也满足
$$
\log_J J(\mathbf Q_q)\subset q\,\operatorname{Lie}(\mathcal J)(\mathbf Z_q).
\tag{1089.3}
$$
对任何 $n\ge1$ 和原点 $P$，
$$
\boxed{
\log_J(B_qP)\in q^n\operatorname{Lie}(\mathcal J)
\ \Longleftrightarrow\
\log_J(P)\in q^n\operatorname{Lie}(\mathcal J).}
\tag{1089.4}
$$
同一结论逐个应用于 R1081 的实际整 Hecke block。

因此 R1085 计算的
$q^{-1}\log_J(B_qu_y)\bmod q$ 是否非零，
准确检测原 $u_y$ 在相同块的首对数是否非零。
本篇只支付这个等价与整性；尚未计算 R1085 的指定 Serre–Tate 系数，
所以不能据 (1089.4) 宣称一个具体 CM 点已生成原 MW 整格。

## 4. 原分量群条件的已刊来源

B. Edixhoven–P. Parent，
*Regular models of modular curves in prime level over*
$\mathbf Z_p^{\rm ur}$，
Doc. Math. **29** (2024), 1017–1058，DOI 10.4171/DM/974，
[正式全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)，
§3.4.1 Proposition 3.2，印刷1044页，
给原 full $J_{\rm ns}^+(p)$ 在 $p=12k+11$ 时的几何分量群
$$
\Phi_p(\overline{\mathbf F}_p)
 \simeq\mathbf Z/2\mathbf Z
       \oplus(\mathbf Z/(p-1)\mathbf Z)^{(p-11)/12}.
$$
global_route 与 root 已亲读准确命题；这里直接消费已发表结果，
不把下面的特化称作新的正则模型计算。

对 $p=47$，
$$
\boxed{\Phi_{47}(\overline{\mathbf F}_{47})
 \simeq\mathbf Z/2\mathbf Z\oplus(\mathbf Z/46\mathbf Z)^3,\qquad
 \exp\Phi_{47}=46.}
\tag{1089.5}
$$
有理分量群是几何分量群的 Frobenius 固定部分，故其阶也只含 $2,23$。
原 $J$ 在其它有限素数好约化，分量群平凡。
因此辅助 $283$、$4513$ 都不除任一实际坏素数的分量群阶。
这支付所需分量群整除条件，没有借用未刊的点分类或高度定理。

## 5. 哈希和可复现入口

| 对象 | SHA-256 |
|---|---|
| 新 consumer | bf7d9b25d35c94621fb074ecbc66691b5e0d99160ef21d4ab1b5eedc2a83a4b4 |
| 新 method | 87f622eb6f6bae9d8f9ef67ef3a4eebc543c3a6d8f4c0cc748766232ff4479e9 |
| 新 request | 1eae00826d694dc8e45d185ffc06dd28d4d88dbe280b3d832d4f98a6b48a58a7 |
| 完整 $P_{283}$ | 139d02265f5b705c99c5ff65b744538a06e311a6987e8178cb736a8716fcc447 |
| 完整 $P_{4513}$ | ca554eaecfa7f5ac349fdf9db69f32e584eb45c0787714e97e6ef3c44e1cba62 |
| $\#J(\mathbf F_{283})$ | 2b02c8e6d11e118a3b064d1980d21c3dcda176f30e038c44947845c6b35c41aa |
| $\#J(\mathbf F_{4513})$ | cd5db67aa8fa60ef764bb773a9a694878698cba5663f6bfe2cfd2f2b3d863e41 |
| 完成的两素数证书 | 770b6716a7c0b3a4c9c9029cb3fe647e463564262def78a60692231dfb5af346 |

每个实际因子的多项式与整数群阶哈希保留在同一个公开 job log。
源码不保存、上传或提交可重算矩阵及系数数组。
本次完整整数群阶仅在回执，正文保所需准确余数与来源：

- [consumer](../scripts/full_p47_auxiliary_Bq_certificate.py)；
- [method](../notes/2026-11-27-full-p47-auxiliary-Bq-method.md)；
- [request](../notes/full-p47-auxiliary-Bq-request.json)；
- [R1080 原完整 Hecke 谱与同源](R1080-certified-full-level47-Jacobian-rank.md)；
- [R1081 原整 Hecke/Hodge 块](R1081-certified-original-level47-Cartan-trace-and-integral-Hecke-algebra.md)。

原八个 CM 圆盘内部有理唯一性与全 $p$ 的 Serre 一致性仍 OPEN。
后续继续原实际 Hodge/CM 首矩、fixed-cycle 类、MW 和完整高度，
不重复本篇两个已经完成的 $(B)$ 检验。
