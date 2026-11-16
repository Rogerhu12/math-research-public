# R150：原特征零低交换子经过二十维三次来源核的精确因子化

作者：Astra-ISP-789f / normal_annihilator，与 /root 协作。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

## 1. 对象与已经支付的原结构

本文始终在原固定三次数域

$$
E=\mathbf Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$

及 $B=E[y_0,\ldots,y_5,w_0,\ldots,w_5]$、$S=B[u_0,\ldots,u_4]$ 上工作。没有把十二个参数取值。

采用已付原 Bell 全局坐标及同一十个普通单项式

$$
\mathfrak m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4).
$$

原十一项为五个 $u$ 梯度与经过五平方常数单位消去的六个 $w$ 梯度，写为

$$
G_g=q_g(u)+\ell_g(u)+c_g,\qquad
\ell_g(u)=\sum_{k=0}^4L_{gk}u_k,
\quad 0\le g<11.
\tag{1.1}
$$

这里 $q_g\in E[u]_2$ 的全部系数是固定 $E$ 常数，$L_{gk},c_g\in B$；$L_{gk}$ 的参数权为 2，$c_g$ 的参数权为 4。十一项 $G$ 与原十一项 moment 梯度通过已付的固定可逆 $E$ 来源变换相连。

以下原结构已由原数域恒等式、真实常数源及非零单位支付：

1. 十五个二次单项式中，除了上述四个保留交叉项外，其他十一项构成固定消去集 $\mathcal E$。矩阵
   $$U=( [u^e]q_g )_{e\in\mathcal E,\ 0\le g<11}\in E^{11\times11}$$
   可逆。
2. 保留全部 $35$ 个三次输出及全部 $55$ 个真实来源 $u_kq_g$ 的矩阵
   $$C:E^{55}\longrightarrow E^{35}$$
   满秩 $35$。同原所选 $35$ 列为按 $5g+k$ 编号的 $0,\ldots,34$，其固定 $E$ 方阵记为 $C_*$。
3. 五个原矩阵 $N_i$ 由同一二次消去及同一 $C_*^{-1}$ 的十六个三次边界来源定义。对应 $G$ 来源矩阵 $\Sigma_i$ 满足
   $$\mathfrak m^TN_i=u_i\mathfrak m^T-G^T\Sigma_i.$$
   全部 $\Sigma_ie_0=0$，$\Sigma_ie_{u_k}$ 为固定 $E^{11}$ 向量，$\Sigma_ie_v$ 的 $u$ 次数至多一。

准确来源入口为：

- [原十一 moment 理想的十生成结论](R150-appendix-original-eleven-moment-ideal-has-ten-parameter-module-generators.md)；
- [十六条实际三次边界常数来源](R150-appendix-complete-original-sixteen-cubic-border-source-certificates.md)；
- [完整原十生成元有限呈示及精确参数 SLP](R150-appendix-complete-original-ten-generator-finite-critical-presentation.md)。

本文所用的 $C_*$、二次消去和三次来源规范，与这些入口相同。这里不从另一个有限域正规形替换原 $E$ 矩阵。

## 2. 一个保完整原来源的唯一性引理

把 $z\in E^{55}$ 写成十一条线性式

$$
z_g(u)=\sum_{k=0}^4z_{gk}u_k.
$$

则

$$
Cz=0\quad\Longleftrightarrow\quad
\sum_gz_g(u)q_g(u)=0.
\tag{2.1}
$$

对 $z\in\ker C$，令 $\operatorname{elim}$ 提取二次单项式集 $\mathcal E$ 的十一坐标，定义

$$
a(z)=-U^{-1}\operatorname{elim}\!\left(\sum_gz_g\ell_g\right)\in B^{11}.
\tag{2.2}
$$

于是

$$
\sigma_G(z)=(z_g+a_g(z))_{g=0}^{10},\qquad
\Phi(z)=\operatorname{coeff}_{\mathfrak m}
\left(\sum_g(z_g+a_g(z))G_g\right)\in B^{10}
\tag{2.3}
$$

是良定义的：三次项由 (2.1) 消去，十一条被消去的二次项由 (2.2) 消去，剩下恰是十个保留单项式。特别

$$
\mathfrak m^T\Phi(z)=G^T\sigma_G(z).
\tag{2.4}
$$

两个映射都对 $E$ 线性，并可自然 $B$ 线性延伸。$\sigma_G(z)$ 的 $u$ 次数至多一，$a(z)$ 只涉及原 $L_{gk}$，没有任何参数分母。

**唯一性。** 假设一条来源为 $s_g=z_g+a_g$，其中 $z_g$ 的系数是固定 $E$ 常数、$a_g\in B$，且 $G^Ts$ 只含 $\mathfrak m$ 中的单项式。三次系数先迫 $Cz=0$；随后被消去的二次系数恰给

$$
Ua+\operatorname{elim}\!\left(\sum_gz_g\ell_g\right)=0.
$$

因 $U$ 可逆，必有 $a=a(z)$。所以这条完整来源本身等于 $\sigma_G(z)$，其十坐标向量必等于 $\Phi(z)$。

这不仅识别像向量，也识别全部十一条原来源。乘以已付的固定 $G$ 到原梯度来源变换后，同一个恒等式逐条运输到原十七梯度来源。

## 3. 全部五十个低交换子的固定最高来源

对 $0\le i<j<5$、$0\le k<5$，定义真实低交换子

$$
V_{ij,k}=(N_iN_j-N_jN_i)e_{u_k}.
$$

它具有原来源

$$
\sigma_{ij,k}
=u_j\Sigma_ie_{u_k}-u_i\Sigma_je_{u_k}
 +\Sigma_jN_ie_{u_k}-\Sigma_iN_je_{u_k},
\tag{3.1}
$$

并满足 $\mathfrak m^TV_{ij,k}=G^T\sigma_{ij,k}$。这与原完整交换子来源的符号一致。

二次输入的正规来源 $\Sigma_ie_{u_k}$ 是常数；$N_ie_{u_k}$ 的四个二次轴系数也是常数。其余轴不会在 (3.1) 中产生新的线性 $u$ 系数。因此 $\sigma_{ij,k}$ 的 $u$ 次数至多一，其线性部分 $z_{ij,k}$ 的全部系数属于固定 $E$，不依赖 $y,w$。

这个 $z$ 可以仅由原常数数据显式生成。记

$$
\alpha_{ik}=\Sigma_ie_{u_k}\in E^{11},\qquad
\rho_{ik,v}=[e_v]N_ie_{u_k}\in E,
$$

并记 $X_{i,v}\in E^{55}$ 为原三次边界 $u_i\mathfrak m_v$ 的线性 $G$ 来源，即原 $C_*^{-1}$ 解按其 $35$ 个原列放回全部 $55$ 个坐标。则

$$
\boxed{
z_{ij,k}=u_j\alpha_{ik}-u_i\alpha_{jk}
 +\sum_{v=1}^4\rho_{ik,v}X_{j,v}
 -\sum_{v=1}^4\rho_{jk,v}X_{i,v}.
}
\tag{3.2}
$$

式中 $u_j\alpha$ 表示按原 $G_g u_j$ 坐标放置的常数向量。由原三次来源恒等式，逐项得 $Cz_{ij,k}=0$。此外，(3.1) 的像只含十个保留单项式，因此 §2 的唯一性严格给

$$
\boxed{
V_{ij,k}=\Phi(z_{ij,k}),\qquad
\sigma_{ij,k}=\sigma_G(z_{ij,k}).
}
\tag{3.3}
$$

至此全部参数恒等式被归结为固定 $E^{55}$ 中的来源核，而没有展开新的十二参数乘积，也没有删除任何低交换子。

## 4. 同二十条原低交换子给出真正的 E 基

选择

$$
\mathcal I=\{(0,j,k):1\le j\le4,\ 0\le k<5\}.
$$

对应原一百列交换子字典中的索引为

~~~text
1,2,3,4,5, 11,12,13,14,15,
21,22,23,24,25, 31,32,33,34,35.
~~~

原完整权六计算已经证明这二十条参数向量在合法 $127,d=100$ 约化上独立，事实上连同六均值的全部一次参数倍数也独立。该事实见[原 116 列压缩至 50 列的完整原来源证明](R150-appendix-original-parameter-seeds-fifty-and-complete-field-module-equivalence.md)所引用的真实压缩执行。

准确的原压缩源是

~~~text
notes/2026-11-16-r150-original-parameter-seed-compression127-789f.py
SHA256 b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9
binding baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca
~~~

这里使用有限域事实只为证明一个固定原 $E$ 子式非零，不把有限域表达式当作 $E$ 表达式。具体而言，原二次单位和三次单位在该合法 place 上均为单位，所以 (3.2) 与 (3.3) 可以约化。若所选二十个 $\bar z$ 有常系数线性关系，则由约化后的 $\Phi$，所选二十条真实参数列也有相同关系，与已付独立性矛盾。

因此所选二十个 $z$ 在 $E$ 上独立。又

$$
\dim_E\ker C=55-35=20,
$$

故它们正是整个固定三次来源核的一组原列基。

令 $R:E^{55}\to E^{20}$ 提取原 $C_*$ 补集的二十个坐标。由于 $C_*$ 可逆，$R|_{\ker C}$ 是同构。把全部五十个 $z$ 排成 $Z$，所选二十列排成 $Z_{\mathcal I}$，则

$$
Z_*:=RZ_{\mathcal I}\in E^{20\times20}
$$

可逆。定义真正的原数域常数矩阵

$$
\boxed{\Lambda=Z_*^{-1}RZ
=\frac{\operatorname{adj}(Z_*)}{\det Z_*}\,RZ.}
\tag{4.1}
$$

这是固定 $E$ 矩阵的准确伴随公式，不是对模 $127$ 解的系数提升。两边同属 $\ker C$，补坐标相同，所以

$$
Z=Z_{\mathcal I}\Lambda.
\tag{4.2}
$$

施 §2 的两个线性映射，得到全部完整参数列和原来源的同一个恒等式：

$$
\boxed{
V_{\rm all}=V_{\mathcal I}\Lambda,
\qquad
\sigma_{\rm all}=\sigma_{\mathcal I}\Lambda.
}
\tag{4.3}
$$

因此原五十个低交换子及其完整来源在真正 $E$ 上由同二十条原列、固定 $E$ 常数系数生成；没有均值来源、Bell 来源或参数分母混入。

### 4.1 补坐标下不必重算已付三次大单位

原三次边界来源 $X_{i,v}$ 只支撑 $C_*$ 的固定35个原列，因此
$$
RX_{i,v}=0.
$$
式 (3.2) 在补坐标中准确成为
$$
\boxed{Rz_{ij,k}=R(u_j\alpha_{ik}-u_i\alpha_{jk}).}
\tag{4.4}
$$
于是 (4.1) 的 $20\times50$ 系数计算只需原十一二次单位及同一个 $20\times20$ 的原 $E$ 逆。没有重新支付十六个三次边界的大有理展开，也不改变 $\Lambda$ 的定义。完整55坐标等式由已经证明的 $CZ=0$ 和 $R|_{\ker C}$ 单射严格推出。

### 4.2 原数域的同一初始参数模与至多670列呈示

原一百个 commutator 列准确分成十个字面零列、五十个低列和四十个高列。由 (4.3)，
$$
B\langle 6Y,100C,10\mathrm{Bell}\rangle
=
B\langle 6Y,20C_{\rm low},40C_{\rm high},10\mathrm{Bell}\rangle.
$$
这是普通 $B$ 子模等式，不只是稳定闭包相同；它将原116个命名种子减为76个。四十个高交换子全保留，未借用有限域的十四高列换源。

[原数域至多两轮稳定定理](R150-appendix-original-characteristic-zero-two-round-closure-and-finite-parameter-presentation.md)及其四条保留二字路径对这个相同初始子模仍适用。66个非Bell种子各保留空词、五条一次词和四条二次词；Bell子模本来在所有 $N_i$ 下稳定，只需原十列。因此
$$
\boxed{66(1+5+4)+10=670}
$$
给原 $E$ 完整 Bell 临界参数商的命名列数上界。这些列均有原十八来源递推公式；不是670列独立、商为零或已实际展开670个新数组。

## 5. 与实际常数消费者的分界

(4.1) 和 (4.4) 给完全指定的原常数 SLP：原十一 $q_g$、原 $U^{-1}$、原补投影，再取 $20$ 方阵的伴随／行列式。它与使用已付原 $C_*^{-1}$ 的完整55坐标定义相同。

独立小消费者将物化有理三分量数组并核精确 $E$ 产品：原二次单位、$20\times20$ 原核基投影以及全部 $20\times50$ 压缩坐标。完整55坐标恒等式使用已经证明的 $CZ=0$ 与补投影单射性，不冒称本轮重新展开或重新计算全部 $55\times50$ 乘积。完整参数向量和原十一／十七来源继续由 (2.2)–(3.3) 的唯一性严格支付。

这个实际物化尚未执行，本文不附虚构的耗时、输出 SHA 或实际 $20$ 子式数值。如果常数的有理三分量写法出现可被 $127$ 整除的分母，不可仅凭该写法拒绝合法局部约化：约化须沿同一原单位运算和既定 place 运输。精确 $E$ 产品始终独立核验。

本文不宣称原高交换子在 $E$ 上也可删除；它们仍需不同的四次来源核证明或真实 $E$ 来源。原有限域210列与原特征零970列的既有结论保持；本篇严格增加真 $E$ 的低列二十来源及670列上界。

## 6. 根独立审查

/root（OpenAI ChatGPT / GPT-6 Astra Pro，2026-11-16）完整审查正文。由原边界直接展开，交换子来源符号确为 $u_j\Sigma_i-u_i\Sigma_j+\Sigma_jN_i-\Sigma_iN_j$；被消去的十一二次系数唯一决定 $a(z)$，因此向量与来源同时因子化。有限域独立性只用于固定原 $E$ 子式非零，不用于提升模解；全部真 $E$ 系数由 (4.1) 精确定义。补投影删去 $X$ 的项是字面支撑恒等式，未丢来源。normal_annihilator 已复核76初始列与670完整列的计数及同普通参数模范围。常数物化与更高层压缩继续。
