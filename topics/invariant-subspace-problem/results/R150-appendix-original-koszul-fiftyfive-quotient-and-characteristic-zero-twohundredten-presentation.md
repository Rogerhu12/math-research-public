# R150：原五十五条二次 Koszul 来源与特征零200/210列完整呈示

作者：Astra-ISP-789f / normal_annihilator，与 /root 协作。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

## 1. 结论与本次范围

继续采用原固定数域
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),
\quad
B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\quad
F=B^{10}.
$$
[原四次来源核95与270列定理](R150-appendix-original-quartic-syzygies-rank95-and-characteristic-zero-twohundredseventy-presentation.md)已证明：

- 原二十条低交换子的线性最高来源 $z_s$ 是完整三次核基；
- 全部100条 $u_i z_s$ 张满95维四次来源核；
- 全部高交换子有真原来源，落在 $B\langle C_s,N_iC_s\rangle$；
- 26个非Bell低种子加10个 Bell 种子的最小 $N$ 稳定闭包至多两轮完成。

本篇由原二次方程自身的55条 Koszul 来源，进一步证明存在40条字面的 $N_iC_s$，使
$$
\boxed{
B\langle C_s,N_iC_s:1\le s\le20,\ 0\le i<5\rangle
=
B\langle C_s,W_1,\ldots,W_{40}\rangle.
}
\tag{1.1}
$$
这是真正普通 $B$ 子模等式，且保留全部原来源；不需要均值或 Bell 来源。

因此第一轮可用106列，第二轮可用210列；省去 Bell 列后分别为96、200。准确得到
$$
\boxed{
\operatorname{coker}_B(B^{200}\to B^{10})
\cong B[u]/(\partial R'),\qquad
\operatorname{coker}_B(B^{210}\to B^{10})
\cong B[u]/(\partial R',b-1).
}
\tag{1.2}
$$
这是纯原 $E$ 结论。它不使用有限域200/210参数换源关系，不从有限域解提升系数。本篇给存在性、确定贪心选择规则与原伴随公式；新的40个实际索引和混合95子式数值尚未运行，不能称为本次已物化的数组。

## 2. 完整四次来源核中的55条独立 Koszul 列

原十一矩方程为
$$
G_g=q_g+\ell_g+c_g,\qquad q_g\in E[u]_2,\quad0\le g<11.
$$
原十一消元单项式上的系数单位 $U$ 可逆，所以 $q_0,\ldots,q_{10}$ 在 $\operatorname{Sym}^2E^5$ 中线性独立。

令
$$
D:E^{11}\otimes\operatorname{Sym}^2E^5\longrightarrow
\operatorname{Sym}^4E^5,\qquad
(d_g)\longmapsto\sum_gq_gd_g,
$$
并在其165个完整原来源坐标中定义
$$
k_{ab}=q_a e_b-q_b e_a,\qquad0\le a<b<11.
\tag{2.1}
$$
共有55列。由于多项式交换，
$$
Dk_{ab}=q_bq_a-q_aq_b=0.
$$
若 $\sum_{a<b}\lambda_{ab}k_{ab}=0$，逐每个 $E^{11}$ 分量比较，得到某些 $q_a$ 的常系数线性关系。它们线性独立，故全部 $\lambda_{ab}=0$。因此
$$
K=\operatorname{span}_E\{k_{ab}\}\subset\ker D,\qquad
\dim_EK=55.
\tag{2.2}
$$
这是原 $E$ 的直接证明，不依赖55个有限域向量的事后秩猜测。

已付完整四次核结论给
$$
\dim_E\ker D=95,\qquad
\ker D=\operatorname{span}_E\{u_i z_s:0\le i<5,\ 1\le s\le20\}.
$$
于是
$$
\dim_E(\ker D/K)=40.
\tag{2.3}
$$
从这100个字面来源中可以选40条补齐 $K$。记所选对为
$$
\mathcal J=\{(i_\nu,s_\nu):1\le\nu\le40\},\qquad
W_\nu=N_{i_\nu}C_{s_\nu}.
$$
这给完整核基
$$
\{k_{ab}\}_{a<b}\ \cup\
\{u_{i_\nu}z_{s_\nu}\}_{\nu=1}^{40}.
\tag{2.4}
$$

## 3. 完全指定的原列选择与精确系数公式

可沿已付原95单位的行集合 $I$ 固定坐标投影
$$
R_{95}:E^{165}\to E^{95}.
$$
由于该原95单位的列张满 $\ker D$，$R_{95}|_{\ker D}$ 为同构。

在同合法 place $(127,d-100)$，原 $q_g$ 仍由原11单位线性独立，因此55条 $\bar k_{ab}$ 独立。已付全部100条 $\overline{u_i z_s}$ 张满同95维核，故下列确定规则必会在40步完成：

1. 保留全部55条 $R_{95}\bar k_{ab}$；
2. 按原 $(i,s)$ 字典顺序扫描100条 $R_{95}\overline{u_i z_s}$；
3. 每次只保留使已有列秩增加的原列，直到补齐95列。

这个规则没有十二参数取值。它选中同原40条来源，使
$$
M=[R_{95}K,\ R_{95}T_{\mathcal J}]\in E^{95\times95}
$$
在该 place 上为单位，因而在 $E$ 中可逆。对任何原 $d\in\ker D$，其准确系数定义为
$$
\binom{\kappa(d)}{\beta(d)}
=M^{-1}R_{95}d
=\frac{\operatorname{adj}M}{\det M}R_{95}d.
\tag{3.1}
$$
这是真正固定 $E$ 常数矩阵的伴随公式。有限域只选择和认证同原非零子式，不将有限域解当成(3.1)的原系数。

本篇证明该规则必结束及其来源意义；新的实际40索引、混合单位行列式和全坐标乘回由独立小常数消费者另行支付。既有 actual95 没有被重复计为已算过该新混合单位。

## 4. 用真正 G Koszul 来源消掉二次最高部分

对原100条 $v_{is}=N_iC_s$，采用已付完整来源
$$
\tau_{is}=u_i\sigma_s-\Sigma_iC_s,\qquad
\mathfrak m^Tv_{is}=G^T\tau_{is}.
\tag{4.1}
$$
这里 $\deg_u\tau_{is}\le2$，其二次最高部分为 $u_i z_s$。

由(2.4)，对每条原 $v_{is}$ 有固定 $E$ 系数
$$
u_i z_s=
\sum_\nu\beta_\nu u_{i_\nu}z_{s_\nu}
+\sum_{a<b}\kappa_{ab}(q_a e_b-q_b e_a).
\tag{4.2}
$$
定义完整来源差
$$
r_{is}
=\tau_{is}-\sum_\nu\beta_\nu\tau_{i_\nu s_\nu}
-\sum_{a<b}\kappa_{ab}(G_a e_b-G_b e_a).
\tag{4.3}
$$
最后一项是真正的原 $G$ Koszul 来源，其原乘回严格为零：
$$
G^T(G_a e_b-G_b e_a)=0.
$$
因其二次最高部分是(2.1)，式(4.2)使(4.3)的全部 $u^2$ 来源消失。因此
$$
\deg_u r_{is}\le1,\qquad
G^Tr_{is}
=\mathfrak m^T\left(v_{is}-\sum_\nu\beta_\nu W_\nu\right).
\tag{4.4}
$$
右边仍是十个保留单项式中的正常形。

现在使用原低来源唯一性。写 $r=z+a$，其三次像为零迫 $z\in B\otimes_E\ker C$；原11单位唯一决定
$$
a=-U^{-1}\operatorname{elim}\left(\sum_gz_g\ell_g\right).
$$
将 $z$ 在原20基上展开，得到 $\gamma_s(y,w)\in B$，并同时得到完整向量和来源恒等式
$$
v_{is}=\sum_\nu\beta_\nu W_\nu+\sum_s\gamma_s C_s,
\tag{4.5}
$$
$$
\tau_{is}
=\sum_\nu\beta_\nu\tau_{i_\nu s_\nu}
+\sum_s\gamma_s\sigma_s
+\sum_{a<b}\kappa_{ab}(G_a e_b-G_b e_a).
\tag{4.6}
$$
这证明(1.1)的非平凡包含，反向包含因40列本来就是100列中的原子集而成立。

特别，(4.6)保留了那些乘回为零的真正 Koszul 来源；它没有把“像相等”冒充来源向量字面相等。通过原固定来源运输，仍得到全部原十七方程的合法来源，无参数分母。

## 5. 第一轮106与完整第二轮210

令
$$
P_0=B\langle6Y,20C,10\mathrm{Bell}\rangle.
$$
Bell 子模在所有 $N_i$ 下稳定。由(1.1)，
$$
P_1=P_0+\sum_iN_iP_0
=B\langle6Y,20C,30N_iY,40W,10\mathrm{Bell}\rangle.
\tag{5.1}
$$
所以第一轮至多106列，非Bell部分至多96列。这里不声称这些列独立，也没有推出 $P_1$ 稳定。

原270定理已证明
$$
\operatorname{Cl}_N(P_0)=P_2,
$$
且全部二字对整个 $F$ 可模 $P_1$ 归到四条保留路径
$$
\mathcal V=\{(1,4),(2,3),(2,4),(3,4)\}.
$$
因此在(5.1)之外，只需增加
$$
N_pN_qY_j\quad((p,q)\in\mathcal V,\ 1\le j\le6)
$$
的24列，以及
$$
N_pN_qC_s\quad((p,q)\in\mathcal V,\ 1\le s\le20)
$$
的80列。总计
$$
106+24+80=210,\qquad96+24+80=200.
\tag{5.2}
$$
所有新列继续使用原来源递推
$$
\sigma(N_iz)=u_i\sigma(z)-\Sigma_i z,\qquad
\sigma(N_pN_qz)=u_pu_q\sigma(z)-u_p\Sigma_qz-\Sigma_pN_qz.
$$
通过已付原十生成元循环性、完整交换子与全部原方程，得到(1.2)。

## 6. 同原权过滤与没有宣称的事项

参数权为 $\operatorname{wt}y=1$、$\operatorname{wt}w=2$，$\operatorname{wt}u=2$。200个非Bell命名列按来源总权分成
$$
6\text{ 列权5},\
20\text{ 列权6},\
30\text{ 列权7},\
40\text{ 列权8},\
24\text{ 列权9},\
80\text{ 列权10}.
$$
(4.2)的系数属于固定 $E$；(4.5)中低列补偿是参数权2的系数，故换源保原齐次权与原来源。Bell10仍是原 $(b-1)e_a$，按既有原十八来源过滤解释。

这给原 $E$ 中200/210完整呈示的存在与可重现原系数定义。它不把此前有限域200呈示中的40条权8换源列自动认作本篇新的原 $E$ 选择，没有声称新的40坐标已经计算，也没有支付单位理想或 Bell 非零分支为空。现有有限域实际200数组继续保持自己的已付身份；本篇原 $E$ 结论有独立的 Koszul 与来源证明。

根与 literature_audit 已分别纯代数交叉核：55独立性、减真正 $G$ Koszul 后的完整来源次数、canonical 唯一性、106加104的计数均成立；两者均未把这一理论核对记作新的数值门。
