# R150：原四次来源核秩95、全部高交换子的原来源吸收与特征零270列呈示

作者：Astra-ISP-789f / normal_annihilator，与 /root 协作。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

## 1. 新结论及系数环

在原固定三次数域
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),
\qquad B=E[y_0,\ldots,y_5,w_0,\ldots,w_5]
$$
上，令 $F=B^{10}$，保留全部十二个参数及五个原矩方向算子 $N_i$。

本次对同原四次来源矩阵的实际合法 place $(127,d-100)$ 运算得到：
$$
\operatorname{rank}\bar D=70,\qquad
\operatorname{rank}\bar T=95,\qquad
\det\bar T_{I,J}=38\ne0.
\tag{1.1}
$$
这里 $D:E^{165}\to E^{70}$ 是全部十一原二次项乘全部十五个二次单项式的完整矩阵；$T:E^{100}\to E^{165}$ 是五个 $u_i$ 乘原二十条三次来源核基。结合下面原 $E$ 多项式身份，(1.1)严格给
$$
\boxed{\operatorname{im}T=\ker D,\quad
\dim_E\ker D=95,\quad
\dim_E\ker T=5.}
\tag{1.2}
$$
实际回执的 remainingKernelDimension=0 表示 $\dim(\ker D/\operatorname{im}T)=0$，不表示 $\ker T=0$；后者恰为5维。

由(1.2)及原完整来源的低次唯一性，全部四十条高交换子满足真正普通参数模包含
$$
\boxed{
C_{\rm high}\subset
B\langle C_1,\ldots,C_{20},N_iC_s:0\le i<5,\ 1\le s\le20\rangle.
}
\tag{1.3}
$$
$C_s$ 是同原二十条低交换子。式(1.3)同时保留原十一、进而原十七来源；没有从有限域坐标提升系数。

再令
$$
P_0=B\langle Y_1,\ldots,Y_6,C_1,\ldots,C_{20},(b-1)e_a:0\le a<10\rangle,
\qquad P_{r+1}=P_r+\sum_iN_iP_r.
$$
本篇证明
$$
\boxed{\operatorname{Cl}_N(P_0)=P_2.}
\tag{1.4}
$$
因此原归一 Bell 临界商具有至多
$$
\boxed{26(1+5+4)+10=270}
\tag{1.5}
$$
条带完整原来源的 $B$ 列呈示。省去 Bell 种子时，同一证明给原十七梯度商至多260列。这里的列是完全指定的原数域算术表达式；本次没有展开新的270个参数数组，也未证明商为零或自由。

## 2. 同原二次、三次来源与准确四次对象

采用同一十个普通单项式
$$
\mathfrak m=(1,u_0,u_1,u_2,u_3,u_4,
u_1u_4,u_2u_3,u_2u_4,u_3u_4)
$$
及原十一矩方程
$$
G_g=q_g(u)+\ell_g(u)+c_g,\qquad q_g\in E[u]_2.
$$
所有 $q_g$ 系数为固定 $E$ 常数。原十一二次消元单位、35维完整三次单位和字面边界，来自：

- [原十一矩理想十生成元](R150-appendix-original-eleven-moment-ideal-has-ten-parameter-module-generators.md)；
- [完整十六条实际三次边界来源](R150-appendix-complete-original-sixteen-cubic-border-source-certificates.md)；
- [完整原十生成元有限呈示](R150-appendix-complete-original-ten-generator-finite-critical-presentation.md)；
- [低交换子原二十维来源因子化](R150-appendix-original-characteristic-zero-low-commutators-factor-through-twenty-cubic-sources.md)；
- [两个四阶单位给实际精确低20坐标](R150-appendix-actual-exact-low20-coordinates-from-two-four-dimensional-units.md)。

令 $V=E^5$，原三次矩阵为
$$
C:E^{11}\otimes V\longrightarrow\operatorname{Sym}^3V,
\qquad (z_g)\longmapsto\sum_gq_gz_g.
$$
其维数为 $35\times55$，满秩35，原单位列为0至34。取已付同原二十条核基
$$
z_s\in\ker C,\qquad s=1,\ldots,20.
$$
它们对应 $[N_0,N_j]e_{u_k}$，$j=1,\ldots,4$、$k=0,\ldots,4$；原100列字典索引是
~~~text
1,2,3,4,5,11,12,13,14,15,
21,22,23,24,25,31,32,33,34,35.
~~~

完整四次矩阵定义为
$$
D:E^{11}\otimes\operatorname{Sym}^2V
\longrightarrow\operatorname{Sym}^4V,\qquad
(d_g)\longmapsto\sum_gq_gd_g.
\tag{2.1}
$$
它保留全部165个原来源和70个输出，不作参数点消元。令
$$
T(e_\ell\otimes e_s)=u_\ell z_s.
\tag{2.2}
$$
全部100个列都保留，按 $(\ell,s)$ 原顺序编码。ordinary monomial 字典逐项核对，不混入对称张量的额外对角因子。

原 $C$ 满射直接推出 $D$ 满射：任何四次单项式可写为 $u_\ell$ 乘一个三次单项式，再将后三次按原 $C$ 来源表达。因此
$$
\dim_E\ker D=165-70=95.
\tag{2.3}
$$

## 3. 原 E 零身份与有限域单位各自支付什么

在原 $E$ 中已有 $Cz_s=0$。故逐原多项式身份，
$$
D(u_\ell z_s)=u_\ell\,Cz_s=0.
\tag{3.1}
$$
这严格给 $\operatorname{im}T\subset\ker D$，并非把模127的零乘积上提。

原三次边界线性来源 $X_{i,v}\in E^{55}$ 满足
$$
CX_{i,v}=u_i\mathfrak m_v.
$$
高交换子 $[N_i,N_j]e_v$ 的二次最高来源为
$$
d_{ij,v}=u_jX_{i,v}-u_iX_{j,v}
\in E^{11}\otimes\operatorname{Sym}^2V.
\tag{3.2}
$$
所以同样在原 $E$ 中，
$$
Dd_{ij,v}
=u_ju_i\mathfrak m_v-u_iu_j\mathfrak m_v=0.
\tag{3.3}
$$
式(3.1)、(3.3)的依据是原来源恒等式，而不是本次7000、2800个有限域零产品。

原二次/三次常数单位及所选低源具有合法 place 的同一约化。本次实际找到同原 $T$ 的95行、95列子式，其模127行列式为38。为固定同一原子式，按源码字典取 $J$ 为 $\bar T$ 约化行阶梯矩阵各非零行的首主元列，再取 $I$ 为 $(\bar T_{:,J})^T$ 的同一主元列；两组均保原升序。原 $E$ 子式始终使用这一确定的 $(I,J)$，不在特征零另换矩阵。于是该原 $E$ 子式非零，故
$$
\operatorname{rank}_E T\ge95.
$$
结合(2.3)与(3.1)的上界，得到(1.2)。对任意原 $d\in\ker D$，可用这个同原95单位的准确伴随/行列式公式求其 $E$ 系数，并由 $T$ 在所选行的单射性核实全部165坐标。有限域 beta 数组只作该域审计；原 $E$ 系数定义是原子式的精确逆，不直接提升 beta。

本次实际也验证所有40条 high 顶层来源的6600个坐标、全部100条来源的16500个 span 坐标，以及完整五维关系的825个乘积。原 $E$ 关系核维数5由秩结论给出；本篇不把五条有限域核列冒充已经逐项展开的 $E$ 核列。

## 4. 最高来源消去给全参数高交换子身份

原边界来源矩阵 $\Sigma_\ell$ 满足
$$
\mathfrak m^TN_\ell
=u_\ell\mathfrak m^T-G^T\Sigma_\ell.
\tag{4.1}
$$
对每个低基 $C_s$，记其完整原来源为 $\sigma_s$：
$$
\mathfrak m^TC_s=G^T\sigma_s,\qquad
\deg_u\sigma_s\le1,\qquad
(\sigma_s)_{u^1}=z_s.
$$
则
$$
\boxed{
\mathfrak m^T(N_\ell C_s)
=G^T\bigl(u_\ell\sigma_s-\Sigma_\ell C_s\bigr).
}
\tag{4.2}
$$
右侧来源的二次最高部分恰为 $u_\ell z_s$，因为 $\Sigma_\ell$ 的 $u$ 次数至多一。

给定高列 $H=[N_i,N_j]e_v$，其实际完整来源 $\tau_H$ 的 $u$ 次数至多二、最高部分为(3.2)。由(1.2)，存在固定 $E$ 常数 $\beta_{\ell s}$ 使
$$
d_{ij,v}=\sum_{\ell,s}\beta_{\ell s}u_\ell z_s.
$$
从原完整来源中减去(4.2)：
$$
r=\tau_H-\sum_{\ell,s}\beta_{\ell s}
\bigl(u_\ell\sigma_s-\Sigma_\ell C_s\bigr).
\tag{4.3}
$$
则 $\deg_u r\le1$，且 $G^Tr$ 的像仍只含十个保留单项式。这不是仅在某个商中相等，而是全部原来源的字面差。

写 $r=z+a$，$z$ 对 $u$ 线性、系数属于 $B$。像没有三次项，故 $z\in B\otimes_E\ker C$。被消去的十一二次系数给
$$
Ua+\operatorname{elim}\!\left(\sum_gz_g\ell_g\right)=0.
$$
由原 $U$ 单位，
$$
r=\sigma_G(z).
$$
把 $z$ 用同原二十基展开，$z=\sum_s\gamma_s(y,w)z_s$。canonical 来源的 $B$ 线性给
$$
r=\sum_s\gamma_s\sigma_s,\qquad
H=\sum_{\ell,s}\beta_{\ell s}N_\ell C_s+\sum_s\gamma_sC_s.
\tag{4.4}
$$
这证明(1.3)，并同时证明全部十一来源等式。经原固定来源变换，(4.4)保全部十七原梯度来源。没有 $y,w$ 分母。

这里得到的是 high 普通 $B$ 模包含于 $\langle C_s,N_\ell C_s\rangle$。$N_\ell C_s$ 可能是新列；因此不能把(4.4)改写成初始76列与36列的普通 $B$ 模相等。可以准确得出它们的最小 $N$ 稳定闭包相同。

## 5. 36种子至多两轮完成，未假定第一轮稳定

设 $P_0,P_1,P_2$ 如§1。全部低交换子列已在 $P_0$；全部高列由§4在 $P_1$；十个 $[N_i,N_j]e_0$ 字面为零。因此
$$
[N_i,N_j]F\subset P_1,\qquad
[N_i,N_j]e_{u_k}\in P_0.
\tag{5.1}
$$
原四条二字路径满足
$$
e_v=N_pN_qe_0,\qquad
(p,q)\in\{(1,4),(2,3),(2,4),(3,4)\}.
$$

按同原二次正规式定义算子 $Q_{ij}$：它是 $N_iN_j$ 减原常数、一次及四条保留二字路径组合。全部系数在中心环 $B$。字面路径给 $Q_{ij}e_0=0$；对一次轴，
$$
Q_{ij}e_{u_k}=[Q_{ij},N_k]e_0\in P_0,
$$
因为内部交换子作用于 $e_0$ 为零，剩下只有低轴交换子。

对二次轴必须按顺序展开
$$
Q_{ij}N_pN_qe_0
=[Q_{ij},N_p]N_qe_0+
N_p[Q_{ij},N_q]e_0.
$$
第一项只含 $N_\ell$ 作用于低交换子和完整交换子作用于 $F$；第二项是一个 $N_p$ 作用于低交换子。因此两项都在 $P_1$，从而
$$
\boxed{Q_{ij}F\subset P_1.}
\tag{5.2}
$$
全部原十一二次方程的有序算子 $\widehat G_g$ 是这些 $Q_{ij}$ 的原常系数组合，所以 $\widehat G_gF\subset P_1$。

原35维三次单位及原二次回填给全部三次单项式的身份
$$
u^\alpha=\sum_g\left(\sum_\ell a_{g\ell}u_\ell+a_g(y,w)\right)G_g
+\sum_a r_a(y,w)\mathfrak m_a,\qquad |\alpha|=3.
\tag{5.3}
$$
将(5.3)按固定有序 $N$ 字代入。重新排序误差只含
$$
[N_i,N_j]F,\quad N_\ell[N_i,N_j]F,\quad
[N_i,N_j]N_\ell F,
$$
它们由(5.1)分别位于 $P_1,P_2,P_1$；主项 $N_\ell\widehat G_gF$ 也在 $P_2$。故每个三字作用于整个 $F$ 后，模 $P_2$ 降为零、一次、四条保留二次字。

现在才将其应用于 $P_0$ 种子。$P_2$ 本来由长度至多二的字作用于 $P_0$ 生成，左乘任意 $N_\ell$ 最多变成三字。上一段把这些列全部降回 $P_2$，因此 $N_\ell P_2\subset P_2$，证明(1.4)。这没有假设 $P_1$ 稳定，也没有断言第二轮是最小停止轮数。

## 6. 完整原260/270列与来源递推

二字先用完整交换子统一顺序，再用(5.2)降至四条保留路径；误差都在 $P_1$。因此对26个非Bell种子 $z=Y_j,C_s$，只需
$$
z,\qquad N_iz,\qquad
N_pN_qz\quad ((p,q)\in\mathcal V),
$$
共至多 $26(1+5+4)=260$ 列。Bell 子模 $(b-1)F$ 本身稳定，再保原十列，得到270列。

每列都有完整原来源。若 $\mathfrak m^Tz=G^T\sigma(z)$（均值列则使用全原十七来源），原边界逐次给
$$
\sigma(N_iz)=u_i\sigma(z)-\Sigma_i z,
$$
$$
\sigma(N_pN_qz)=u_pu_q\sigma(z)
-u_p\Sigma_qz-\Sigma_pN_qz.
\tag{6.1}
$$
通过同原来源运输，全部系数是原多项式来源，只有固定 $E$ 常数逆。新列不是借用有限域210列的压缩关系。

整个稳定商上的 $N_i$ 可交换，字面路径使 $e_0$ 循环生成；原十一矩方程和六均值方程均消失。反向由逐列原来源定义映射，逐十生成元互逆。故准确有
$$
\operatorname{coker}_B(B^{260}\to B^{10})
\cong B[u]/(\partial R'),
$$
以及加入十个 Bell 列后的
$$
\boxed{
\operatorname{coker}_B(B^{270}\to B^{10})
\cong B[u]/(\partial R',b-1).
}
\tag{6.2}
$$
至多两轮与完整商论证沿用[原特征零有限呈示](R150-appendix-original-characteristic-zero-two-round-closure-and-finite-parameter-presentation.md)的原来源；本篇补上不同初始36种子的完整范围。

## 7. 真实计算与全部门

实际作业为 [run43911869940](https://github.com/Rogerhu12/math-research-public/actions/runs/43911869940)，job133455626806；步骤 original-low20-original-quartic-syzygy95-unit60，执行提交
~~~text
ef3bb5ba8b781c0a6f30db38a7a322544da2e558
~~~
实际 exit0，程序记录0.1964903289999711秒，observer0.5036411680000583秒，外层0.666658837秒；child peak RSS84604KiB。

完整原门包括：

| 对象 | 实际验证坐标数 |
|---|---:|
| 原十一二次单位双向乘回 | 242 |
| 十五二次来源完整回填 | 225 |
| 原35三次单位双向乘回 | 2450 |
| 十六原三次边界 | 560 |
| 原二十低源核 | 700 |
| 全部100条 $u_\ell z_s$ 的核产品 | 7000 |
| 全部40条高最高来源的核产品 | 2800 |
| 原95子式逆双向乘回 | 18050 |
| 全部40条高来源的完整坐标 | 6600 |
| 全100条 multiplied source 的完整 span 坐标 | 16500 |
| 五条完整关系的原乘回 | 825 |

原低投影单位模127行列式为64，原95子式为38。完整矩阵全部保留：$D$ 为70×165，$T$ 为165×100，高顶层为165×40；没有只检测选中输出子集。

raw8429字节，SHA
~~~text
7b23309fe6d5d80c52624f3f9f66b4a9ed311d62a23952cbce3a5e7e5e964f0b
~~~
binding
~~~text
9f0ee10f7e4cece784d8140d063f94c210105e7dded9f811710d6ec6f2825fa1
~~~
执行身份见 [original95-unit60.json](../notes/r150-original-exact-low20-execution-789f/43911869940-original-low20-original-quartic-syzygy95-unit60.json)。数学字段在完整 job 日志，仓库身份不保存计算数组。

两完整临时相位：

| 相位 | stored bytes / SHA256 | logical bytes / SHA256 |
|---|---|---|
| whole-original-quartic95-input | 16730 / a2d91336495f29ff2a15958ab26cf2cefcb782eb2e7acac2c88d90fb91a2de07 | 95934 / bf86bf186cd64d3ed78e0bf66b794bca62aa72e71abd3de3335e905c7cea0589 |
| complete-original-quartic95-unit | 20816 / 71d679b394ab9c58f542c576690397d8f1cbcba627d74daffd72f9bbb2e3302e | 63121 / b711688351ce47161d8e898f1322a2e4e0c355bf8d7033d7a6bb2884a95343eb |

## 8. 源码、复现与准确未完成范围

[原 high95 主源](../notes/2026-11-16-r150-original-quartic-syzygy95-small-field-gate127-789f.py)为15520字节，SHA
~~~text
b6f72e376aa403ff540a01927ea0dd4ac136099cb7be16fe201f91e95968cc4c
~~~
[inputs](../notes/2026-11-16-r150-original-quartic-syzygy95-small-field-gate-inputs-789f.json)和[interface](../notes/2026-11-16-r150-original-quartic-syzygy95-small-field-gate-interface-789f.md)锁定同原模型、ordinary monomial 字典、全部来源、运行时与预算。实际程序在新独立 output 执行；成功的 exact/model 父文件只读复用。

原 $E$ 的 $DT=0$ 与 $DH=0$ 已在§3由真实原多项式身份证明。有限域非零95子式只支付同原 $E$ 子式非零；本次实际 beta、五关系数组保持有限域范围。精确 $E$ 高吸收系数由原95单位的伴随公式及§4唯一性定义，没有把模解当作原数域解。

新结论是完整有限原参数呈示和有原来源的高列吸收。它没有把270列称为独立、没有称商自由或为零，也没有付原 Bell 非零分支判空。原有限域200/210实际数组与原数域260/270来源表达式是不同对象，各自保持准确系数环。

根独立审计：root 已全文审冻结源码、本稿和实际完成日志，并实际运行[完成日志审计](../notes/2026-11-16-r150-exact-low20-quartic95-completed-job-log-audit-789f.js)。全部六步身份及门记录核同，high95 的完整 semantic 与8429字节实际 raw 无损重建，SHA均为原值；[执行身份](../notes/2026-11-16-r150-exact-low20-quartic95-root-log-audit-execution-789f.json)保源、运行与完整身份。审计不重跑有限域算术、不把临时数组写入Git。
