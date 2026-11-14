# R167：整 Hecke 收缩、准确 CM 对数与同框架形式终点

日期：2026-11-13（Asia/Taipei）；负责：root。**状态：以下整映射、完整有限矩阵和八个形式除子代表已证明并计算。**

令 $X=X_{\rm ns}^+(41)$，$J=\operatorname{Jac}(X)$，$R=\mathbb Z_{47}$，
$R_2=R[i]$、$i^2=-1$，工作精度 $q=47^4=4879681$。
记 $m=\#J(\mathbb F_{47})$ 为 R121 已使用的准确304位整数；
$m\bmod q=459340$，$m\bmod47=9$。

本结果实现两条已授权 CM Miller 链的独立形式终点输入。
另给出实际 $N=48-T_{47}$，并严格区分“把点送入形式群”与“已经搬运一个 Poincaré 纤维”。
它没有计算这两条新链的主函数，也不把 $N$ 当作可直接除去的标量高度倍率。

## 1. $48-T_{47}$ 把全部有理局部点送入形式群

在47处 $X$、$J$ 都有好约化。其 Hecke 算子满足特殊纤维上的准确关系
$$
\overline T_{47}=F+V,\qquad FV=VF=[47].
\tag{167.1}
$$
这里使用本曲线的真实 Hecke 对应，不是只用与另一个 Jacobian 的有理同源。

说明 (167.1) 中没有遗漏 diamond 算子。一般素于水平的细模问题上，两个普通分支分别来自 Frobenius 核和 Verschiebung 核；后者在水平结构上留下标量 $47I$，因而一般式为 $F+\langle47\rangle V$。
本题的非分裂 Cartan 正规化子包含全部标量，$47I\bmod41$ 在该商上作用平凡。
于是这里的 diamond 确为恒等。

这一计算可先在额外素于47的细水平上作，随后按原水平群下降。
普通轨迹的两个对应分支给上述拉推；把除子移动离开有限多个超奇异点与尖点，就能代表每个 Jacobian 类，所以得到整个 $J_{\mathbb F_{47}}$ 上的等式。
这也是通常 Eichler–Shimura 对应证明在本题 Cartan 商上的应用。

对 $P\in J(\mathbb F_{47})$，$FP=P$，故 $VP=47P$；因此
$$
\boxed{NP=0,\quad N:=48-T_{47}.}
\tag{167.2}
$$
由约化与 endomorphism 相容，
$$
N J(\mathbb Q_{47})\subset J_1(R),
\tag{167.3}
$$
其中 $J_1(R)=\ker(J(R)\to J(\mathbb F_{47}))$。

## 2. $N$ 在形式群上整可逆

八个实际 Hecke 域次数仍为 $2,3,3,4,4,8,12,18$。
各块的 Frobenius 多项式为 $X^2-a_{47}X+47$，所以
$$
\det(dN)=\prod_f N_{K_f/\mathbb Q}(48-a_{47}(f))
=\#J(\mathbb F_{47})=m.
\tag{167.4}
$$
特别地 $dN\in\mathrm{GL}_{54}(R)$。
因线性项为单位，形式逆函数定理给 $N$ 的整形式逆；所以 $N$ 限制为 $J_1(R)$ 的自同构。在形式对数与指数的收敛域上，它也写成：
$$N|_{J_1}=\exp\circ dN\circ\log.$$
没有除47或选择非整本征向量。

作为一个精确推论，$\ker N(\mathbb Q_{47})$ 约化到 $J(\mathbb F_{47})$ 是同构。
单射来自形式群上可逆；对任意提升 $C$，令
$$C_1=(N|_{J_1})^{-1}(NC),\qquad T=C-C_1,$$
则 $NT=0$ 且 $T$ 与 $C$ 同约化，给满射。
所以这个局部核是阶 $m$ 的有限群，给出有理局部点的形式部分与素于47的挠部分。
这不是关于 $J(\mathbb Q)_{\rm tors}$ 阶为 $m$ 的声明；后者仍只用 R162 的16消去界。

### 准确矩阵

R140 已证明 $\mathbb Z_{47}[T_3]$ 是完整的整 étale 代数。
生成器在 R89 的八个 $H=T_2+2T_3$ 幂基中列出
$$1,T_3,\ldots,T_3^{53}$$
的54行，所得矩阵行列式模47为 **20**，并保存模 $q$ 的双侧逆。
据此把 $T_2,T_{47},r_3,r_7$ 和 R162 的两个 CM 差类算子都准确转换成 $T_3$ 的次数至多53多项式。

将 $T_2$ 的多项式代入 R131 的真实典范矩阵，所得全部 $54^2$ 条目与原 $T_2$ 矩阵相同。
这检查了八域坐标与实际微分基的方向及识别，而非仅比较特征多项式。
同法得到真实 $T_{47}$、$N$ 及 $N^{-1}$，双侧乘积均为单位矩阵，且
$$\det N=459340+0i\pmod q.$$

另把 $N=A+iB$ 写成108阶整数实块矩阵
$$\begin{pmatrix}A&-B\\B&A\end{pmatrix}.$$
独立 FLINT 复核先取其**准确整数行列式**再模 $q$，结果为
$$708841=459340^2\pmod q.$$
此处独立检查的是 $R_2/R$ 范数，与主程序的 $R_2$ 行列式计算分开。

## 3. 两个实际 CM 差类的对数

令 $b=P_{-3}$、$u=P_{-12}$、$c=P_{-7}$，
$$C_u=[u-b],\qquad C_c=[c-b].$$
R89、R144、R162 给真实点的有理坐标
$$
C_u=R_uB_{-4},\quad R_u=(T_2r_3/3-r_3)/20,
\qquad
C_c=R_cB_{-4},\quad R_c=(r_7-r_3)/20
\tag{167.5}
$$
于 $J(\mathbb Q)\otimes\mathbb Q$。
全部相关分母均为47单位。对数杀挠点，故这些式子在对数上是准确等式。
用 R121 的实际 $\log B_{-4}$ 与上述真实 $T_3$ 矩阵作 Horner 运算，得到完整的两个54维 $R_2$ 行向量。

实际微分算子采用列坐标，因此对数采用**右乘同一矩阵**；若改为列对数才取转置。
程序同时核验
$$
20\log C_u=\tfrac13(\log(r_3B))T_2-\log(r_3B),
$$
$$20\log C_c=\log(r_7B)-\log(r_3B).$$
两个结果与 R162 的54个小 Hecke 坐标表达逐项相同，并满足原半线性 Frobenius 下降。
全部坐标在 $47R_2$ 中。

计算并保存四个目标
$$m\log C_u,\quad m\log C_c,\quad
(\log C_u)N,\quad(\log C_c)N.
\tag{167.6}
$$
前两个对应 $mC_u,mC_c$，因为 $m$ 杀整个约化群；后两个对应 $NC_u,NC_c$，由 (167.3) 同样位于形式群。
形式对数在该群上单射，所以无需用额外长乘来定义这些目标。
对仍在运行的两条 $m$-Miller 链，最终必须再与它们作完整实际类比较；本结果不预写该比较为已完成。

## 4. 同一双 Abel 框架的八个完整除子理想

沿用 R141/R145 的两组固定54点、残余72次除子和截面 $v_j$，所有原 SHA 保留。
在每一组中，实际微分的积分写成
$$
L_j(t)=\sum_{a=1}^{54}\left(
\Omega_{a,0}t_a+\frac12\Omega_{a,1}t_a^2+
\frac13\Omega_{a,2}t_a^3\right)\pmod{47^4}.
\tag{167.7}
$$
常数 Jacobian 是单位矩阵意义下可逆的实际微分评价矩阵。
对每个 (167.6) 目标 $z\in47R_2^{54}$，三次整 Newton 更新解出 $t\in47R_2^{54}$，并逐项检查 $L_j(t)=z$。
R136/R140 的整系数全尾界适用：对 $n\ge4$，$n-v_{47}(n)\ge4$，所以被省略的积分项均为零模 $47^4$。

把已保存的真实73个截面三阶展开代入这些 $t_a$，求移动54点对199维二次截面空间的限制。
再与实际残余72次除子的127维整理想相交，得到秩73的单位核。
这给实际次数126有效除子
$$E_j(z)=R_j+Z_j(t)$$
的完整 Makdisi 理想；Riemann–Roch 的维数和单位子式保证是完整整格。
每个结果均核验原 Frobenius 下降与其平方为一。

注意 $E_j(0)=\operatorname{div}(v_j)$。
其点类等于 $[Z_j(t)-Z_j]$，但更换到这个差除子时仍有实际函数 $v_j/f_0$；纤维计算不能把它删掉。
本次保存两个 CM 类、两个乘子、两套框架，共八个完整73维理想。
第一套框架的点 SHA 为：

| 类 | 乘子 | 点与 Frobenius SHA256 |
|---|---|---|
| $C_u$ | $m$ | ac94861a1b6168a8e6d85a9e7b89240e679015739f5910317788cc75bf35a21b |
| $C_c$ | $m$ | f2d3b0fcc786b29200486b57f757de40cbf29131fa25b79ac34431a907ebe0f5 |
| $C_u$ | $N$ | 7e5427bee504193b47ced3b293f0a40d37f813b0787d11b7769228ef44d1eaf6 |
| $C_c$ | $N$ | 663dd815b53a1100aa24f9e5d346665fb84d45b6e32d66e5e62a27213fe5329b |

第二套框架、全部参数与 Lie 坐标均在完整证书中，不以表中哈希代替数据。

## 5. 为什么不能把 $N$ 当作标量高度倍率

固定主极化的 Poincaré 双扩张 $\mathcal P$。
若要像整数 $m$ 那样，把任一纤维元素沿 $(N,N)$ 直接送到新纤维，并在 $\mathbb G_m$ 上取统一整数 $k$ 次幂，则必须有
$$(N,N)^*\mathcal P\simeq\mathcal P^{\otimes k}.$$
双扩张的分类将左边对应到 $N^\dagger N$，右边对应到 $[k]$。
故这种统一操作要求
$$N^\dagger N=[k].\tag{167.8}$$
这里 Hecke 自伴随，故左边为 $N^2$。实际矩阵已经否定它为标量：
在本文同一微分基中，$N^2$ 的第1行第2列模47为
$$39+46i\ne0.$$
独立整数复核器直接验证这个非对角条目。
因此不能从 $dN$ 可逆就把一个纤维的数值“除以 $N$”或“除以 $N^2$”。

若使用整 Hecke 多纤维向量，可以考虑矩阵反演，但仍须构造每条真实对应的范数和不同除子框架之间的主函数。
仅在 Jacobian 或 Lie 代数上验证 Hecke 关系，并不计算这些规范标量。
另一个实际成本是47同源的靶除子可能在特殊纤维高重数合并；此时必须用有限平坦代数或准确整盘因子，不能假定48个靶点均能在未分歧二次环内分开。

所以当前两条标量 $m$ 链继续运行；$N$ 的点、矩阵和端点提供另一个准确接口，尚未构成已实现的纤维捷径。

## 6. 文件、复算与来源

- [准确 CM 对数和八个 Abel 端点生成器](../scripts/p41_cm_formal_endpoints47.py)。
- [完整端点和矩阵证书](../scripts/data/p41_cm_formal_endpoints47_checkpoint.json.gz)：1182267字节，SHA256 `05a194c9d7e4dc0e8a28266b18aa351a635f70be0d8d311556cff3b2e9eea0b9`。
- [独立整数行列式及非标量平方复核](../scripts/verify_p41_cm_formal_endpoints47.py)和[复核结果](../scripts/data/p41_cm_formal_endpoints47_independent.json)。

主源码 SHA256：`e9f06af1109cf0ab1c27db0991999857fd8f77f180cb67e495e05cdd90778ca9`。
恢复原 R141 双 Abel bases 和 source cubic jets 到已记录的同名 `/tmp` 输入后，从仓库根运行：

~~~bash
python -B topics/serre-uniformity/scripts/p41_cm_formal_endpoints47.py \
  --script-dir topics/serre-uniformity/scripts
python -B topics/serre-uniformity/scripts/verify_p41_cm_formal_endpoints47.py
~~~

第一条默认写新的 `/tmp` 结果；第二条检查仓库保存的完整证书。

(167.1) 的标准一般式可参见 Diamond–Im, *Modular forms and modular curves*, §10.2，(10.2.3)（印刷页87），含 diamond 算子；本节已解释它在当前 Cartan 商上为何为一。
可直接阅读的模对应证明见 A. Snowden, [Lecture 17: Eichler–Shimura](https://websites.umich.edu/asnowden/teaching/2013/679/L17.html)，其中说明有限平坦对应与约化相容及从普通轨迹移除有限点后的 Jacobian 结论。

其余实际输入是 R89/R94 的 Hecke 坐标、R121 的真实对数和约化群阶、R131 的真实算子、R136/R141/R145 的同框架指数及全尾界、R160 的两个实际 CM 初始点、R162 的小 Hecke 坐标。
本结果不把形式终点、局部收缩或有限矩阵等同于完整高度、QC 共同根或 Serre 统一性。
