# 原参数模的稳定闭包至多两轮完成与完整 210 列呈示

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 结论与本次证明范围

本篇保持原合法系数剩余映射 $(p,d)=(127,100)$，全部十二参数和原十八来源。令
$$
B=\mathbb F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad F=B^{10},\qquad b=y\cdot w.
$$
原五个 $B$ 线性矩阵记为 $N_i$。接续[原十四高权来源交换与三十六种子](R150-appendix-original-high-source-exchange-and-thirtysix-seed-stable-closure.md)，令
$$
P_0=B\langle Y_1,\ldots,Y_6,C_1,\ldots,C_{20},(b-1)e_a\ (0\le a<10)\rangle,
$$
$$P_{r+1}=P_r+\sum_{i=0}^4N_iP_r.$$
前文实际完成 $P_1$ 的 106 列普通参数模呈示。本篇由原二次、三次来源恒等式证明
$$\boxed{\operatorname{Cl}_N(P_0)=P_2,\qquad N_iP_2\subset P_2\quad(0\le i<5).}$$
而且第二轮只需在原 106 列之后加入
$$
N_pN_qY_j\quad((p,q)\in\mathcal V,\ 1\le j\le6),\qquad
N_pN_qC_\ell\quad((p,q)\in\mathcal V,\ 1\le\ell\le20),
$$
其中原四条字面路径为
$$\mathcal V=\{(1,4),(2,3),(2,4),(3,4)\}.$$
这是 24 条权九及 80 条权十的准确来源定义。因此整个原 Bell 归一临界商有完整的参数模呈示
$$\boxed{B^{210}\longrightarrow B^{10}\longrightarrow B[u]/(\partial R',b-1)\longrightarrow0.}$$
这里没有把 104 条新来源当作另一次已经运行的数组生产。本篇证明其精确公式与完整性；原数值输入和来源常数均引用已完成的父证据。也没有证明该商为零、210 列独立、参数模自由或特征零单位恒等式。

## 2. 必须保留的原代数身份

十个原单项式及其字面路径是
$$
m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4),
$$
$$N_ie_0=e_{u_i},\qquad N_pN_qe_0=e_{u_pu_q}\quad((p,q)\in\mathcal V).$$
这些身份不是只在最终临界商中成立，而是在自由 $B^{10}$ 中已核的原向量身份。全部普通二次单项式使用同一个正规式，故
$$N_ie_{u_j}=N_je_{u_i},\qquad [N_i,N_j]e_0=0.$$

记有符号的完整交换子列为
$$C_{ij,a}=[N_i,N_j]e_a,\qquad C_{ji,a}=-C_{ij,a},\qquad C_{ii,a}=0.$$
[原 116 种子完整压缩](R150-appendix-original-parameter-seeds-fifty-and-complete-field-module-equivalence.md) 保留并表达了全部 100 条交换子，特别给出
$$C_{ij,a}\in L_{50}\subset P_1\quad\hbox{对全部十轴 }a,$$
以及更强的低轴身份
$$C_{ij,u_k}\in B\langle Y,C_1,\ldots,C_{20}\rangle.$$
低轴身份只使用权五均值的一次 $y$ 倍和权六保留交换子。因此
$$\boxed{N_\ell C_{ij,u_k}\in P_1.}$$
这一步不能替换成未付的 $N_\ell D$ 身份。

原十一矩方程写成
$$G_g=q_g(u)+\sum_kL_{gk}(y,w)u_k+c_g(y,w),\qquad 0\le g<11.$$
全部 $q_g$ 是固定系数域上的二次型，$L,c\in B$。原十一二次单位和完整 $35\times55$ 三次来源单位见[十生成元定理](R150-appendix-original-eleven-moment-ideal-has-ten-parameter-module-generators.md)。[原边界有限呈示](R150-appendix-complete-original-ten-generator-finite-critical-presentation.md) 保留了对应全部固定常数、低次回填与原来源。

## 3. 二次算子正规式作用于全部十轴

对 $i\le j$，原二次正规式向量为
$$\rho_{ij}=N_ie_{u_j}=\rho_{ij,0}e_0+\sum_k\rho_{ij,k}e_{u_k}+\sum_{v\in\mathcal V}\rho_{ij,v}e_v.$$
所有 $\rho$ 系数属于中心环 $B$。定义固定有序算子
$$
\mathscr Q_{ij}=N_iN_j-\rho_{ij,0}I-\sum_k\rho_{ij,k}N_k
-\sum_{(p,q)\in\mathcal V}\rho_{ij,pq}N_pN_q.
$$
原字面路径直接给 $\mathscr Q_{ij}e_0=0$。四个保留二次项对应恒等的零关系，其余十一项是原完整二次消去关系。

先对一次轴。由
$$[N_aN_b,N_k]=N_a[N_b,N_k]+[N_a,N_k]N_b$$
和所有 $[N_a,N_b]e_0=0$，得到
$$
\mathscr Q_{ij}e_{u_k}=[\mathscr Q_{ij},N_k]e_0
=C_{ik,u_j}-\sum_{(p,q)\in\mathcal V}\rho_{ij,pq}C_{pk,u_q}.
$$
故这些列属于 $L_{50}$；其中没有算子作用于未知的高轴交换子。

再对保留二次轴 $e_v=N_pN_qe_0$。严格按次序写
$$
\mathscr Q_{ij}e_v
=[\mathscr Q_{ij},N_p]N_qe_0+N_p[\mathscr Q_{ij},N_q]e_0.
$$
第一项展开后只有两类非平凡结构：
$$N_aC_{bp,u_q},\qquad [N_a,N_p](N_bN_qe_0).$$
前者属于 $P_1$，因为它是 $N$ 作用于已付低轴交换子；后者是全部十轴 $C_{ap,c}$ 的 $B$ 线性组合，属于 $L_{50}$。线性项的交换子也属于 $L_{50}$。第二项只含 $N_p$ 作用于上一段的低轴交换子，所以同样属于 $P_1$。

由完整十轴得到
$$\boxed{\mathscr Q_{ij}F\subset P_1.}$$
这里没有假定 $P_1$ 对任何 $N_i$ 稳定。使用的是上节准确的低轴门与完整交换子列门。

按普通单项式而非对称矩阵系数写
$$q_g=\sum_{i\le j}q_{g,ij}u_iu_j.$$
原二次正规式对全部 $G_g$ 为零，因而其有序算子代入满足
$$
\widehat G_g=\sum_{i\le j}q_{g,ij}N_iN_j+\sum_kL_{gk}N_k+c_gI
=\sum_{i\le j}q_{g,ij}\mathscr Q_{ij}.
$$
特别是全部原十一条方程都满足
$$\boxed{\widehat G_gF\subset P_1.}$$
不是只对某些预选二次关系或仅对 $e_0$ 的结论。

## 4. 完整三次降次及算子重排余项

完整三次单位给每个普通三次单项式 $t$ 一个精确原身份
$$
t=\sum_{g=0}^{10}\left(\sum_{\ell=0}^4a_{g\ell}u_\ell+a_g(y,w)\right)G_g
+\sum_{a=0}^9r_a(y,w)m_a.
\tag{1}
$$
其中 $a_{g\ell}$ 是固定常数，$a_g,r_a\in B$。先用原三次单位消最高次，再用原二次单位回填，正给此式；来源的 $u$ 次数至多一次。任何逆只来自固定非零系数域常数，不倒置参数。

固定把普通单项式按升序代入 $N$。该线性代入不是预先假定的代数同态。把(1)右边改写为
$$\sum_g\left(\sum_\ell a_{g\ell}N_\ell+a_gI\right)\widehat G_g+\sum_a r_a\widehat m_a$$
时，二字、三字重排误差全部是带 $B$ 系数的
$$[N_a,N_b],\qquad N_\ell[N_a,N_b],\qquad[N_a,N_b]N_\ell.$$
其作用于整个 $F$ 的像分别落在
$$P_1,\qquad N_\ell P_1\subset P_2,\qquad P_1.$$
最后一项的结论直接来自交换子对整个 $F$ 的像，绝不是假定 $P_1$ 稳定。另一方面
$$N_\ell\widehat G_gF\subset N_\ell P_1\subset P_2.$$
因此对任意有序或无序的三字 $N_iN_jN_k$，都存在只用 $I,N_\ell,N_pN_q$（$(p,q)\in\mathcal V$）的参数算子 $T_{ijk}^{\le2}$，使
$$\boxed{(N_iN_jN_k-T_{ijk}^{\le2})F\subset P_2.}$$

## 5. 第二轮停止的无循环证明

按定义，$P_2$ 是所有长度至多二的算子字作用于 $P_0$ 的 $B$ 张成。因此对任意种子 $z\in P_0$，上一节给
$$N_iN_jN_kz=T_{ijk}^{\le2}z+p,\qquad p\in P_2.$$
右边第一项本来就在 $P_2$；于是全部长度三的种子像属于 $P_2$。对 $P_2$ 的任一已定义生成列再乘任一 $N_i$，最长只产生长度三，故
$$N_iP_2\subset P_2.$$
这才建立稳定性。此前所有 $N_iP_1\subset P_2$ 都只是迭代定义，不使用待证结论。由最小稳定闭包的定义，得到 $\operatorname{Cl}_N(P_0)=P_2$。

## 6. 完整 210 列与原临界商

先用 $[N_i,N_j]F\subset L_{50}\subset P_1$ 将所有二字次序统一，再用 $\mathscr Q_{ij}F\subset P_1$ 将十五种普通二字归到四条保留路径。作用于 $Y,C$ 后，常数及一次字项已经在 $P_1$。Bell 子模 $(b-1)F$ 自动稳定，因为 $N_i$ 为 $B$ 线性。因此
$$
P_2=P_1+B\langle N_pN_qY_j,N_pN_qC_\ell:(p,q)\in\mathcal V\rangle.
$$
原 $P_1$ 的 106 列，加 $4\cdot6+4\cdot20=104$ 列，给所述 210 列完整呈示；这个数是命名列数，不是秩或最少生成元数。

完整性也可直接核两方向。每一列都有原十八来源，故 $e_a\mapsto m_a\bmod I$ 给 $F/P_2\to B[u]/I$，其中 $I=(\partial R',b-1)$。稳定性使 $N_i$ 在 $F/P_2$ 上定义作用，完整交换子使这些作用可交换。原字面路径使商由 $e_0$ 循环生成；原十一 $G_g$、六 $Y$ 和 Bell 列杀掉全部 $I$。所以 $1\mapsto e_0$ 给反向映射。两复合映射在 $1$ 与全部 $e_a=m_a(N)e_0$ 上都是恒等。

## 7. 原来源的准确递推及有界规模

设原十八生成元为行 $A$，已付 $m v=A\sigma(v)$，边界恒等式为
$$u_im-mN_i=AS_i.$$
每一次乘法的真实来源是
$$\sigma(N_iv)=u_i\sigma(v)-S_iv.$$
所以 104 条新列可逐条由已付第一层完整来源生成，或使用完全等价的二次公式
$$
\sigma(N_pN_qv)=u_pu_q\sigma(v)-u_pS_qv-S_pN_qv.
$$
这些都是全部十八坐标的原多项式身份；没有把数值零余量当来源，也没有引入参数分母。

如需以后作齐次权九矩阵，原 $P_1$ 的非 Bell 权列表为 $6$ 条权五、$20$ 条权六、$30$ 条权七、$40$ 条权八。完整权九父来源数是
$$6\cdot273+20\cdot92+30\cdot27+40\cdot6=4528.$$
新增均值只需 24 条，而非 150 条或仅按交换次序缩出的 90 条。完整输出为
$$15938+5\cdot3816+4\cdot714=37874.$$
因此一个准确后继范围是 $37874\times4552$，但本篇没有生成或消元此矩阵，也没有预填父秩。

## 8. 已付输入定位与未运行边界

全部五个 $N_i$、五个 $S_i$、原十一 $G$、九条字面路径及完整种子来源来自：

- [完整原十行参数模型](R150-appendix-actual-original-ten-generator-parameter-module-and-116-certified-seeds127.md)，源 `2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py`，SHA-256 `4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4`；
- 其完整原参数作用 phase：776254 压缩字节 / `5cbba4f798ab95fe24538f35d23d4b3a2f0d6197ee3ed33f3149b7371b0d222c`；4442756 逻辑字节 / `f07c273c934e671f5e1069954771286c14e5d10ab7c4652d998a02f71beb7d05`；
- [完整权八前沿](R150-appendix-original-complete-weight-eight-frontier-rank1312-and-twentysix-new-sources.md)与[原十四交换及完整首轮](R150-appendix-original-high-source-exchange-and-thirtysix-seed-stable-closure.md)。

本篇是这些真实原身份的代数推论，没有新增数学运行回执。104 个二次来源的实际逐列生产与再次原乘回，可另作独立有预算任务；其未运行不改变上面的构造性恒等证明，也不能被写成已经完成的新数组或新单位正证。原数域 $E$ 的未压缩版本另行证明，不能把此处有限域 20/14 换源免费上提。

## 9. 独立交叉核查与停止指标的准确含义

根与 literature_audit 独立检查了所有量词和包含方向：先证明二次算子对整个自由十轴的像进入第一轮，再以原三次恒等和全部三类词序误差进入第二轮，最后才对种子证明第二轮稳定。此过程不循环假设第一轮稳定，也不以某次矩阵秩代替参数模成员性。

结论 $\operatorname{Cl}_N(P_0)=P_2$ 表示至多两轮已足；本页没有排除 $P_1$ 已经稳定，因此不宣称最小停止指标恰为二。210 是带完整原来源公式的命名列数上界，并非独立列数。
