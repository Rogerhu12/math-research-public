# R1088：原两条 principal 对应的完整 cusp 系数矩阵可逆

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
状态：**已证明；新公开精确计算成功。**

在原 full $X=X_{\rm ns}^{+}(47)$ 上，取 R1087 定义的实际整对应
$$
Z_2=K_{25}-K_5,\qquad Z_3=K_{125}-K_5.
\tag{1088.1}
$$
它们均无 diagonal component、Rosati 自伴、degree/trace zero，
在全部 cusp 型严格为零。
令 $\mathcal T_c=e_{\rm cusp}(\mathbb T\otimes\mathbf Z_{4513})$。
本篇证明原两 CM 来源的系数矩阵
$$
\boxed{
A=\begin{pmatrix}
\tfrac12 e_{\rm cusp}\mathcal F_4^*Z_2&
\tfrac23 e_{\rm cusp}\mathcal F_3^*Z_2\\
\tfrac12 e_{\rm cusp}\mathcal F_4^*Z_3&
\tfrac23 e_{\rm cusp}\mathcal F_3^*Z_3
\end{pmatrix}
\ \in\operatorname{GL}_2(\mathcal T_c).}
\tag{1088.2}
$$
因此这两个真实 fixed-cycle 类生成的整 Hecke 模，
准确等于两个原 CM 类 $u_{1728},u_0$ 生成的模。
这消除了系数造成的共同相消；原 CM 类、首对数或高度是否为单位仍未据此解决。

## 1. 新公开回执与所消费的旧输入

- source：
  [0faac5b69a55abc98534f450c7296c910dda29b1](https://github.com/Rogerhu12/math-research-public/commit/0faac5b69a55abc98534f450c7296c910dda29b1)；
- [run45941481763](https://github.com/Rogerhu12/math-research-public/actions/runs/45941481763)，
  [job140316562143](https://github.com/Rogerhu12/math-research-public/actions/runs/45941481763/job/140316562143)，
  attempt 1，job 及全部步骤 success；
- 完整数学耗时 $3.990293168$ 秒，预算 $120$ 秒，预留 $10$ 秒；
- 固定 SageMath $10.6$ 官方 image digest；exact QQ/finite-field arithmetic；
- root/o1 提交前全文逐行纸审，root 核完整新数学回执及 success。

R1081 的原 composition、trace 来源只重建为本次计算的输入，
并比对既有两个 SHA-256。没有重跑原全中间 necklace 验证、LDL、
Hecke 分块或 $L'$。
实际 Jacobian 上的 faithfulness 和唯一关系
$I+\sum_C R_C=0$ 仍消费 R1081。

## 2. 原整共轭类与十维迹零家族

本次完整枚举原 $G=\operatorname{PGL}_2(\mathbf F_{47})$ 的
$103776$ 个 projective matrices，并识别
$\mathscr K_{5^r}$，$1\le r\le11$ 的十一类，每类恰 $2256$ 个元素。
在原 $x_0^2=-I$ 上实际求 $gx_0g^{-1}$。
每一角的所有原目标逐个计数，核其重数相同、整数且无 diagonal；
没有只把总数除以 valency 后接受。

R1087 的 proof 对这些 split regular 类逐个适用。
其 principal 分量为
$47s_r$，$s_r=\zeta_{23}^r+\zeta_{23}^{-r}$，
cusp 分量严格为零。
十一项 $s_r$ 线性独立，且域迹都为 $-1$，
故十个 $Z_r=K_{5^r}-K_5$，$2\le r\le11$，
准确张成 principal trace-zero 空间。
这里每个 $Z_r$ 是原整有理对应，不是任意抽象坐标向量。

作为一个明确原 cycle，本次的 $Z_{\rm ps}=K_5-K_{25}=-Z_2$ 为
$$
\begin{aligned}
Z_{\rm ps}={}&
2(R_2+R_3-R_7-R_8+R_9+R_{16}-R_{17}-R_{18}-R_{19}+R_{20}+R_{22})\\
&+4(R_4-R_{14}-R_{21})+R_5+R_{12}.
\end{aligned}
\tag{1088.3}
$$
其它类和的可重算系数只留脚本和回执哈希，不提交完整数组。

## 3. 真角代数中的投影与完整 fixed transforms

在原二十三个 $R_C$ 的基上，必须代入
$I=-\sum_C R_C$。
所以实际乘法常数为
$n_{AB}^{D}-\mathbf1_{A=B}d_A$。
程序核全负一向量是单位，并核新十维家族每项 degree/trace 为零。

本次 $Z_{\rm ps}$ 乘法矩阵 rank 为 $11$，
其 characteristic polynomial 为 $T^{12}m(T)$，
$m$ 不可约、degree $11$，并严格满足
$$
|m(0)|=23\cdot47^{11}.
$$
原 $e_{\rm cusp}=m(Z_{\rm ps})/m(0)$ 的平方、rank $12$、
被 $Z_{\rm ps}$ 杀以及 $4513$ 整性均核准。

完整 fixed transforms 使用 R1078/R1087 的原公式
$$
(\mathcal F_4^*Z)_A=z_{[2A^2-1]},\qquad
(\mathcal F_3^*Z)_A=z_{[(3A^2-1)/2]},
$$
其中恒等角系数设为原值零；$A=0$ 和全部 preimages 都保留。
未假定这两个线性变换是代数同态。

实际有理 ranks 为：

| 原映射 | rank |
|---|---:|
| 十维 principal trace-zero 家族 $\to e_{\rm cusp}\mathcal F_4^*$ | 10 |
| 同一家族 $\to e_{\rm cusp}\mathcal F_3^*$ | 10 |
| 两者的联合映射 | 10 |

特别 $e_{\rm cusp}\mathcal F_4^*Z_{\rm ps}$ 与
$e_{\rm cusp}\mathcal F_3^*Z_{\rm ps}$ 都非零。
这些首先是 actual endomorphism 结论；它们本身未断言某个 CM 点类非零。

## 4. 全部十二个 cusp characters 与统一二阶 minor

本次第一个候选就给 separating 元
$$
G=R_0+R_2+R_3.
$$
它在原二十三维角代数的 characteristic polynomial
模 $4513$ squarefree，完整分解为十二个 linear factors 和一个 degree-$11$ 因子。
原 QQ 因子 degree 为 $4,8,11$；
对全部十二个 eigenlines 逐个核 $e_{\rm cusp}=1$。
因此没有遗漏任何 cusp character，或把 principal line 混入其中。

对每个 cusp character $\vartheta$，
程序实际读取两行
$$
\bigl(\vartheta(\mathcal F_4^*Z_r)\bigr)_{r=2}^{11},
\qquad
\bigl(\vartheta(\mathcal F_3^*Z_r)\bigr)_{r=2}^{11}.
$$
结果不只两行 rank 都为二，而且**同一对列 $r=2,3$ 在全部十二处
都给非零 determinant**：

| 原 cusp field | 在 $\mathbf F_{4513}$ 的 characters | 两行 rank | 同一列 $2,3$ |
|---|---:|---:|---|
| $K_{16}$ | 4 | 每处均为 2 | 每处 minor 非零 |
| $K_{48}$ | 8 | 每处均为 2 | 每处 minor 非零 |

为固定读数约定，在 $G$ 的 root $1180$（$K_{16}$）处，
未乘列因子 $\tfrac12,\tfrac23$ 的 minor 为 $2327$；
在 root $221$（$K_{48}$）处为 $1771$。
全部十二行的实际数值及 minor 保留在上述公开 job log，
完整行摘要 SHA 见 §7。
这里的 $G$ roots 不是 R1081 的 $H_2$ roots，未作未经证明的逐 root 配对。

## 5. 从全部 angle characters 到真正整 Hecke 模

R1087 证明原角算子属于同一个有理 Hecke 代数，并保原好模型整格。
R1081 又认证 $\mathbb T\otimes\mathbf Z_{4513}$ 是最大无分歧整序。
其每个 cusp block 的剩余 character 在原 cusp 角代数上，
必限制为 §4 完整列出的十二个 character 之一；
这里包括一次及更高无分歧次数的实际 Hecke blocks。

由 §4，未缩放的 determinant 在这些 restrictions 上都非零，
故在实际 $\mathcal T_c$ 中为单位。
矩阵 (1088.2) 的两列另乘 $\tfrac12,\tfrac23$，
将 determinant 乘以单位 $\tfrac13$，
不改变单位性。这证明 (1088.2)。
它不需要知道某一个 $H_2$ linear root 究竟对应哪一个 $G$ root。

令 $d_i(y)=d_{Z_i}(y)$，$i=2,3$，仍使用原全部 cusp 和
$u_J=[23c_J-C_\infty]$。
R1087 的完整整 cycle 关系在 $\mathbf Z_{4513}$ 中给
$$
23\begin{pmatrix}e_{\rm cusp}d_2(y)\\ e_{\rm cusp}d_3(y)\end{pmatrix}
 =
 A\begin{pmatrix}e_{\rm cusp}u_{1728}\\ e_{\rm cusp}u_0\end{pmatrix}.
\tag{1088.4}
$$
$23$ 也是单位。因此在
$e_{\rm cusp}(J(\mathbf Q)\otimes\mathbf Z_{4513})$ 中，
$$
\boxed{
\mathcal T_c\,d_2+\mathcal T_c\,d_3
 =\mathcal T_c\,u_{1728}+\mathcal T_c\,u_0.}
\tag{1088.5}
$$
投影后的 $d_i$ 与原基点 $y$ 无关，正如 R1087 所证。

(1088.5) 是两个生成集合的模相等，不声称两个 CM 点在每个
rank-one block 上线性独立。
也不声称对对应乘任意 Hecke 元会使 fixed transform 按同样方式相乘；
本篇只使用两条已定义的原对应及其实际点类。

## 6. 对真正 CM 对数输入的用途及边界

对原整对数施于 (1088.4)，全部 endomorphisms 与对数交换。
所以在任一实际 cusp block 上，对任何 $n$，
两个 $d_i$ 的对数都落入 $4513^n$ 的整 Lie 格，
当且仅当两个原 CM 类的对数都落入该格。
由 R1089，施加 $B_{4513}$ 同样不改变这个深度。

特别，若原两 CM 首对数中至少一个非零，则原两条 $d_i$ 的首对数中
至少一个非零；无需再担心两个 fixed-cycle 系数同时把这一实际输入抵消。
R1085 给这两个 CM 首对数的真实 Serre–Tate 公式，
但其指定系数仍须在真正原 Hodge 格上计算。

本篇没有给这两个首对数任何实际非零值。
它也没有给一个指定全局高度 functional 的单位值；
将 (1088.4) 用于高度时，还必须支付原高度的整性、规范与实际读数。
原八个圆盘内部唯一性及全 $p$ Serre 目标仍 OPEN。

## 7. 可复现来源与摘要哈希

| 对象 | SHA-256 |
|---|---|
| consumer | 82cf430f104f1d8f050eea78b8332ce2c799036508362a284c9cf574e20bddee |
| method | 6b30858665126a173d4f4fdc03b063b7ad65dd7ade2a22def56f51d279387bd8 |
| request | d44f69cb55d9343754c89ac857e2e422ce8ca4ddfb101e28922b7e6759018ae3 |
| 十一原类和系数 | 9d00264cdc7fefebdd654a88a6b4950594dbf5e3459ac5423a2e763b9d66bdbd |
| principal 最小多项式 | a80ba38e398fa2b1ddc37347b62b63f54b3ddbfd86537bb053efbd1d32e46ebc |
| 真 cusp projector | 53904739eec7ca82775537a557774758739aa5cb80e16196e47cd58e06894319 |
| $Z_{\rm ps}$ 的 $\mathcal F_4^*$ cusp 投影 | 2be1e7453046ed27154c1e09bcd06ff9c606037088712e875e555a642a730ce8 |
| $Z_{\rm ps}$ 的 $\mathcal F_3^*$ cusp 投影 | a4477200da54c835c311903e94ac6cc965f8c121a697bd30e2330caf32d7046b |
| 十维家族联合投影 | acc074498ccb591c10c20b8e86ea1b9a40df2f9eb69d0c7ab9b68872f48b2930 |
| 原 separating polynomial | 7fa00ef1614d39709da229dad912cbb1332e5d27e9fce0d5066b08733c62801e |
| 全部十二个实际 character 行 | ddc1f10b86c0afaf317dd4f0471f24edcc4510f44f02d24d38b0277871b7e746 |

- [consumer](../scripts/full_p47_principal_fixed_action.py)；
- [method](../notes/2026-11-27-full-p47-principal-fixed-action-method.md)；
- [request](../notes/full-p47-principal-fixed-action-request.json)；
- [R1087 原类和与完整 fixed-cycle 证明](R1087-original-principal-Cartan-ideal-and-cusp-annihilating-correspondence.md)；
- [R1081 已认证原角代数](R1081-certified-original-level47-Cartan-trace-and-integral-Hecke-algebra.md)。

原矩阵与可重算系数数组不提交、不上传 artifact/Release。
本次确切记录已经完成，后续只消费，不重新运行同一个家族计算。
