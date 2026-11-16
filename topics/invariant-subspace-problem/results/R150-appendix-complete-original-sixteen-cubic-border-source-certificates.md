# 原十生成元模型的十六条完整三次来源证书

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。日期：2026-11-16。

## 1. 结论与原模型

本文接续[完整十一矩方向与十生成元定理](R150-appendix-original-eleven-moment-ideal-has-ten-parameter-module-generators.md)及[完整十二梯度低次正规式](R150-appendix-complete-original-twelve-gradient-low-normal-forms-over-all-parameters.md)。系数域始终为原匹配三次域
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336).
$$
全部原参数 $y_0,\ldots,y_5,w_0,\ldots,w_5$ 保留；本文没有参数特化或参数分母。

设原十一矩方向按已付常数可逆来源运输写成
$$
G=(F_0,\ldots,F_4,\operatorname{NF}(\partial_{w_0}R'),\ldots,
\operatorname{NF}(\partial_{w_5}R')).
$$
其中 $F_i=\partial_{u_i}R'$，而六条 $\operatorname{NF}(\partial_wR')$ 与原六条 $\partial_wR'$ 相差固定 $E$ 常数乘以五条 $F_i$。记 $q_g$ 为 $G_g$ 的 $u$ 次数二齐次项。前文给出原35个三次来源 $u_kq_g$ 的常数方块非零；本次实际求得并逐原系数验证以下16个目标的完整 $E$ 来源：
$$
t_j=\sum_{\ell=0}^{34}X_{\ell j}\,u_{k(\ell)}q_{g(\ell)}.
\tag{1}
$$
这里 $g(\ell)=\lfloor\ell/5\rfloor$、$k(\ell)=\ell\bmod5$，即五条 $F$ 与前两条 $\operatorname{NF}(\partial_wR')$ 各乘全部五个 $u_k$。没有使用未记录的来源替换。

按顺序，16个目标是
$$
\begin{gathered}
u_0u_1u_4,\ u_0u_2u_3,\ u_0u_2u_4,\ u_0u_3u_4,\\
u_1^2u_4,\ u_1u_2u_3,\ u_1u_2u_4,\ u_1u_3u_4,\ u_1u_4^2,\\
u_2^2u_3,\ u_2^2u_4,\ u_2u_3^2,\ u_2u_3u_4,\ u_2u_4^2,\
u_3^2u_4,\ u_3u_4^2.
\end{gathered}
$$
它们恰为十生成元中四个二次单项式
$$
v=(u_1u_4,u_2u_3,u_2u_4,u_3u_4)
$$
乘五个 $u_i$ 后出现的全部不同三次单项式。五次十列乘法因此只需这16条新的三次来源。

这次实际结论是完整常数来源证书。全参数低次回填在§4给出精确公式，但本次回执没有宣称已展开或保存这些参数正规式，也没有宣称十生成元自由。

## 2. 原35列与完整乘回

程序从已付完整十一二次模型的原字典重新构造
$$
A:E^{35}\longrightarrow E[u]_3.
$$
输出保全部35个三次单项式。原选列是完整55来源字典中的 $0,\ldots,34$；逐项核对其原梯度标签及 $u_k$ 乘子。

用固定基 $(1,d,d^2)$ 表示每个 $E$ 元素，得到同一映射的有理正规表示
$$
Q:\mathbb Q^{105}\longrightarrow\mathbb Q^{105}.
$$
程序逐个构造所有11025个有理矩阵坐标；没有用有限域矩阵代替 $Q$。右端 $R$ 为16个原三次目标的单位向量。实际 Dixon 解给出 $X_{\mathbb Q}$ 的全部105×16坐标，随后把每列35个 $E$ 三元组先完整保存。

续验重新读取全部候选文件及各自完整压缩、逻辑 SHA，并从原 $q_g$ 再构造同一 $Q$。为避免大有理分母重复约分，取每行正公分母 $a_i$、每个来源列正公分母 $b_j$，精确形成
$$
U_{ik}=a_iQ_{ik},\qquad N_{kj}=b_j(X_{\mathbb Q})_{kj}.
$$
所有11025个行缩放恒等式和1680个列缩放恒等式均先核验。随后实际核
$$
(UN)_{ij}=a_iR_{ij}b_j
$$
全部1680坐标。因为每个 $a_i,b_j$ 是非零整数，这与 $QX_{\mathbb Q}=R$ 完全等价，也即(1)的全部560个原 $E$ 系数恒等式。列公分母最大72436位，行公分母最大28546位；这些是固定数域常数，均不是 $y,w$ 参数分母。

## 3. 实际执行范围

首次求解使用180秒数学预算。精确 Dixon 部分163.63335927799926秒；全部16完整候选在167.51840329799597秒前保存。随后在最终乘回处触发预算，实际183.7710828449999秒、exit75。旧回执和其未验证范围保留，未修改为成功。

第二次是独立只读续验，没有再求解或选单位。实际24.702726178999秒、exit0，最大常驻内存132364 KiB。全部16候选 SHA、全部原输出、全部原来源和全部原乘回均通过。

| 对象 | 字节数 | SHA256 |
|---|---:|---|
| 首次预算回执 | 7450 | 58c7b7686a7334aa966e0b0efcf4b62e2bbc3814f75d1da8624f278313971cc4 |
| 完整16列候选索引 | 5041 | c477bbb0acc38c651a011f76cd0433273825cf14e51883de51f857a933714dfb |
| 独立乘回回执 | 1490 | 6b6bb6a7a4901558ebb0ffc583c6e8dd78927611442ea1f936228bdda6cf23c0 |
| 完整验证模型 gzip | 2679 | e5277e55afd111ce7038aead9989d1d1a236adae38edd7962cbd3548f8fe569e |
| 完整验证模型逻辑内容 | 6994 | 9d492e238da77ee3610bad61987bc8442f9caac3e39c91226c7c83a2b4c7168c |

首次 binding 为
~~~text
883430390f24f79cf127df1df44645f091b345372ef2b36915c212c1787ae35e
~~~
续验 binding 为
~~~text
bb79e9288b5fe0c033b2a3c51c62938b3cb9ae50c482ff30ab3c7e72af90930f
~~~

源码、参数及执行身份分别为：

- [原常数16右端求解器](../notes/2026-11-16-r150-original-sixteen-cubic-border-constant-source-solve-789f.py)；
- [完整原乘回续验器](../notes/2026-11-16-r150-original-sixteen-cubic-border-integer-product-verification-789f.py)；
- [输入及实际临时绑定](../notes/2026-11-16-r150-original-sixteen-cubic-border-source-inputs-789f.json)；
- [执行接口](../notes/2026-11-16-r150-original-sixteen-cubic-border-source-interface-789f.md)；
- [两阶段执行身份与输出 SHA](../notes/r150-nonrankone-execution-789f/20261116-local-original-sixteen-cubic-border-sources.json)。

仓库只保存这些小文件及证明，16个大有理列与临时模型不入库。

## 4. 全参数回填的准确公式

令 $B=E[y,w]$，并写
$$
G_g=q_g+\sum_{a=0}^4L_{ga}(y,w)u_a+c_g(y,w).
$$
这些 $L,c$ 来自已付原十二梯度包，不重新选择数值。在全部15个二次单项式中，记 $z$ 为五个平方与前六个被消去混合项，$v$ 为上列四个保留项。固定常数矩阵满足
$$
G=Uz+Vv+Lu+c,\qquad
U=\begin{pmatrix}Q_5&P_E\\0&C_6\end{pmatrix}.
$$
已付 $Q_5,C_6$ 均为 $E$ 单位，所以
$$
z=-U^{-1}(Vv+Lu+c)+U^{-1}G.
\tag{2}
$$
这条式子直接给全部二次单项式 $m$ 的十坐标表达
$$
m=\rho_m+\sigma_mG.
$$
对(1)的任一已验证三次目标，把 $q_g=G_g-L_gu-c_g$ 代回，再应用(2)，得到
$$
t_j=
-\sum_{g,k,a}X_{(g,k),j}L_{ga}\rho_{u_ku_a}
-\sum_{g,k}X_{(g,k),j}c_gu_k
+\left(
\sum_{g,k}X_{(g,k),j}u_k e_g^{\mathsf T}
-\sum_{g,k,a}X_{(g,k),j}L_{ga}\sigma_{u_ku_a}
\right)G.
\tag{3}
$$
所有符号和原来源均保留。(3)只涉及固定 $E$ 常数及已付原参数多项式的加法、乘法；因此可用精确算术表达式表示，无须先把巨大常分母与全部参数系数展开。来源的 $u$ 次数至多1。

(2)与(3)给十生成元下的五个乘法代表，但这些代表在自由 $B^{10}$ 上不必可交换。其交换子及所有参数关系必须保留，六条原均值梯度和 Bell 归一关系也仍须加入。本文没有据常数顶次满秩宣布全临界商非零、自由、无解或 Bell 属根式。
