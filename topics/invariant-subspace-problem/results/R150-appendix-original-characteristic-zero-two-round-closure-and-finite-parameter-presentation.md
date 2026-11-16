# 原数域至多两轮稳定与全参数有限呈示

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 原数域结论，不使用有限域换源

令
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),
\qquad B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad F=B^{10}.
$$
全部原均值和矩参数保留，$b=y\cdot w$。五个原矩方向矩阵 $N_i$、原边界来源、原六均值列和全部交换子由[完整原十生成元有限呈示](R150-appendix-complete-original-ten-generator-finite-critical-presentation.md)的精确数域算术图定义。

取未压缩的种子模
$$
L_0=B\langle Y_1,\ldots,Y_6,
[N_i,N_j]e_a\ (i<j,\ 0\le a<10),
(b-1)e_a\ (0\le a<10)\rangle
$$
并令 $L_{r+1}=L_r+\sum_iN_iL_r$。本篇证明
$$\boxed{\operatorname{Cl}_N(L_0)=L_2.}$$
从而原整个 Bell 归一临界商是一个完整有限参数模的 cokernel：保留全部 116 个字面种子时可用至多 1070 列；删除十个已经字面为零的交换子 $[N_i,N_j]e_0$ 后，可用至多 970 列。

这是原数域 $E$ 上的结论。没有使用有限域 20 条低交换子、14 条高交换子或其实际换源关系；没有将有限域 210 列呈示提升到 $E$。也没有证明该 cokernel 为零或自由。

## 2. 原 E 身份与四条固定二字路径

十个单项式为
$$m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4).$$
原完整边界来源给
$$u_im-mN_i=AS_i,$$
其中 $A$ 为全部原十八生成元，即原十七梯度加 $b-1$；前文已经把中间 $\operatorname{NF}(\partial_wR')$ 的五源校正运输回原梯度。

九条字面路径在自由 $B^{10}$ 中成立：
$$N_ie_0=e_{u_i},\qquad N_pN_qe_0=e_{u_pu_q},\qquad
\mathcal V=\{(1,4),(2,3),(2,4),(3,4)\}.$$
普通二次正规式不依赖乘法顺序，所以 $[N_i,N_j]e_0=0$。其余 90 条交换子完整保留，没有删去任何尚未在 $E$ 中证明为零的列。

原十一矩方程
$$G_g=q_g(u)+L_g(y,w)u+c_g(y,w)$$
的固定二次项有一个十一维单位，保留二次补空间正是 $\mathcal V$。原完整三次来源 $u_iq_g$ 的 $35\times55$ 映射有原常数方块单位。其精确 $E$ 非零性和来源解释见[原十一矩理想十生成元](R150-appendix-original-eleven-moment-ideal-has-ten-parameter-module-generators.md)。

这里“全部三次可降”并不只引用已经显式保存的 16 条边界目标。该完整 35 维单位在 $E$ 中可取 adjugate/原 determinant 的准确逆，因而给全部 35 个三次单项式的原来源。已实际逐原数域系数核过的 16 条来源和其全参数回填另见[完整三次边界证书](R150-appendix-complete-original-sixteen-cubic-border-source-certificates.md)。需要的固定常数逆只在 $E$ 中取，不出现任何 $y,w$ 参数分母。

## 3. 原全部二次算子关系的整列范围

对 $i\le j$，写同一原正规式
$$N_ie_{u_j}=\rho_{ij,0}e_0+\sum_k\rho_{ij,k}e_{u_k}+\sum_{(p,q)\in\mathcal V}\rho_{ij,pq}e_{u_pu_q},$$
并定义
$$
Q_{ij}=N_iN_j-\rho_{ij,0}I-\sum_k\rho_{ij,k}N_k
-\sum_{(p,q)\in\mathcal V}\rho_{ij,pq}N_pN_q.
$$
所有系数在 $B$ 中，和全部 $N_i$ 交换。字面路径给 $Q_{ij}e_0=0$。

对一次轴，展开 $[Q_{ij},N_k]e_0$。恒等式
$$[N_aN_b,N_k]=N_a[N_b,N_k]+[N_a,N_k]N_b$$
中第一项在 $e_0$ 上因内部交换子字面为零而消失；剩下只有交换子作用于一次轴。因此
$$Q_{ij}e_{u_k}\in L_0.$$

对四个二次轴，严格使用
$$Q_{ij}N_pN_qe_0=[Q_{ij},N_p]N_qe_0+N_p[Q_{ij},N_q]e_0.$$
第一项由 $N_a[N_b,N_p]e_{u_q}$ 和完整交换子作用于 $N_bN_qe_0$ 组成；第二项是一个 $N_p$ 作用于低轴交换子的组合。全部交换子列在 $L_0$ 中，故
$$Q_{ij}e_v\in L_1\quad(v\in\mathcal V).$$
于是
$$\boxed{Q_{ij}F\subset L_1.}$$
这不需要任何有限域的低交换子压缩。

将原 $G_g$ 按普通单项式有序代入 $N$，记为 $\widehat G_g$。原十一方程的二次正规式全为零，故
$$\widehat G_g=\sum_{i\le j}q_{g,ij}Q_{ij},\qquad
\boxed{\widehat G_gF\subset L_1.}$$

## 4. 三字降次与第二轮稳定

完整三次单位及原二次回填给每个 $u^\alpha$、$|\alpha|=3$ 的身份
$$
u^\alpha=\sum_g\left(\sum_i a_{gi}u_i+a_g(y,w)\right)G_g
+\sum_a r_a(y,w)m_a,
$$
其中 $a_{gi}\in E$、$a_g,r_a\in B$。这是全部原十一方程的多项式来源，来源对 $u$ 至多一次。

固定有序字代入后，全部重新排序误差只含
$$[N_i,N_j],\qquad N_k[N_i,N_j],\qquad[N_i,N_j]N_k.$$
交换子对整个 $F$ 的像在 $L_0$，所以三类误差的像分别在 $L_0,L_1,L_0$。主项 $N_k\widehat G_gF$ 在 $L_2$。因此每个长度三的算子字都可在作用于整个 $F$ 后，模 $L_2$ 降为 $I,N_i,N_pN_q$、$(p,q)\in\mathcal V$ 的组合。

现在才应用于种子。$L_2$ 按定义由长度至多二的字作用于 $L_0$ 生成；对这些列再左乘 $N_i$ 最多得到长度三。上一段将其降回 $L_2$，故
$$N_iL_2\subset L_2.$$
这个论证没有假定 $L_1$ 稳定，也没有用有限生成元数猜测迭代停止。最小性立即给 $\operatorname{Cl}_N(L_0)=L_2$。

## 5. 1070 原字面列与 970 的精确删零

对任意原种子 $z$，交换子身份先统一二字次序，$Q_{ij}F\subset L_1$ 再把全部二字降至四个保留路径。Bell 子模 $(b-1)F$ 自动稳定。因此 $L_2$ 由下列字面列生成：

- 对原六条 $Y$ 和全部 100 条交换子，分别保留 $z$、五条 $N_iz$、四条 $N_pN_qz$；
- 保留十条 $(b-1)e_a$。

总数至多 $106(1+5+4)+10=1070$。这里的“至多”允许字面零列与真实依赖。

十个 $[N_i,N_j]e_0$ 已在原 $E$ 中字面为零，其任何 $N$ 像仍为零。只删除这十个种子及其九个像，得到至多
$$\boxed{(6+90)(1+5+4)+10=970}$$
列。没有删除其它仅在有限域中观察为零的交换子，也没有使用有限域的 36 种子压缩。

## 6. 完整原商与逐列来源

每条原种子 $z$ 都有原十八来源 $mz=A\sigma(z)$。按
$$\sigma(N_iz)=u_i\sigma(z)-S_iz$$
及
$$\sigma(N_pN_qz)=u_pu_q\sigma(z)-u_pS_qz-S_pN_qz$$
给出全部新列的精确来源。全部系数是 $E[y,w,u]$ 中的真多项式，只有固定 $E$ 常数逆。原 970/1070 列因而定义可复现的精确算术表达式矩阵，不需要先展开巨大有理系数。

稳定商 $F/L_2$ 上的 $N_i$ 可交换，因为全部交换子像已在 $L_0$ 中。九条字面路径使该商由 $e_0$ 作为 $B[u]$ 模循环生成；原二次身份杀全部 $G_g$，六均值及 Bell 种子杀其它原方程。反向，由逐列来源，$e_a\mapsto m_a$ 映到原临界商。两映射逐生成元互逆。因此
$$
\boxed{\operatorname{coker}_B\bigl(B^{970}\to B^{10}\bigr)
\cong B[u]/(\partial R',b-1).}
$$
若保留全部字面零列，则同样得到 1070 列版本。

本篇是已付精确原 $E$ 身份的推论，没有新增数组运行，也没有从有限域身份推出特征零正证。该有限呈示仍可能有非平凡商；它给出了完整的有限参数来源对象，Bell 非零分支是否为空仍须由真实来源进一步决定。

## 7. 已付身份及与有限域 210 的分工

原 $E$ 边界与来源输入来自[完整十行有限呈示](R150-appendix-complete-original-ten-generator-finite-critical-presentation.md)的实际 v3：binding `11473d55e9cf229685bcbebf59fe30fea9c2b00e8fa225bac6d3d0ca71b7ef76`；完整算术图 634785 压缩字节 / SHA-256 `9d3f03d2746cfb9a1bb3f872f56822ca8136e982cfdcf0cddd666c58aa573a8a`，4405032 逻辑字节 / `9a49a0740c23bfd2dd6e3d9deec51eec7290a5b40793075c706976d4a2dc81ce`。

完整三次单位是同一固定数域系数下的原单位，不是重新选择参数点。原[16 条三次边界来源](R150-appendix-complete-original-sixteen-cubic-border-source-certificates.md)的全部原系数乘回及精确低次公式，保证了五个 $N_i$ 的同一原定义。

[有限域 210 列定理](R150-appendix-original-parameter-stable-closure-stops-at-two-and-complete210-presentation.md)另用真实完整有限域 20/14 压缩和14换源，把相应初始种子降至36。两个结论分别有各自准确的系数环与来源；原 $E$ 版不依赖该有限域交换。

## 8. 原数域的独立核查与准确边界

根与 literature_audit 分别检查了本页的数域版本：交换子全部十列在未压缩 $L_0$ 中，故二次算子对四个二字轴只需进入 $L_1$；原完整三次来源的参数系数均在中心环 $B$ 中，所有词序误差有明示的 $L_0/L_1$ 范围，最后才建立 $L_2$ 稳定。970 列只删除原数域中已经字面为零的十个种子及其像，没有使用有限域的额外删列。

$\operatorname{Cl}_N(L_0)=L_2$ 是至多两轮的停止上界，不宣称第一轮不稳定。上述精确算术表达式和原来源公式已经定义完整呈示；本页未把它们标成新展开数组、单位来源或完成的普通 Hilbert ISP 证明。
