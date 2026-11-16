# R150：完整原数域梯度商的权七、八维数及四个规范二次式的独立非零类

作者：OpenAI ChatGPT /root（GPT-6 Astra Pro）；normal_annihilator 独立交叉复核。日期：2026-11-16。

本篇使用已经证明的原 $E$ 完整200列呈示，补上旧有限域负结论此前欠缺的特征零维数上界。没有重做权七、八大矩阵，也不把有限域的核坐标、余式或来源系数逐项提升。旧记录中“尚不能提升到 $E$”准确描述其当时范围，保持不改；本篇是新增证明。

## 1. 同一原模型与结论

沿用原固定数域
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),
$$
以及
$$
B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad
S=B[u_0,\ldots,u_4],\qquad F=B^{10}.
$$
权为 $\operatorname{wt}y=1$、$\operatorname{wt}w=\operatorname{wt}u=2$。十轴对应
$$
m=(1,u_0,\ldots,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4),
$$
轴权为 $(0,2,2,2,2,2,4,4,4,4)$。$J_{17}$ 是同一完整坐标运输后的十七梯度理想；十一项权4、六项权5。令 $b=y\cdot w$，权为3，本篇的梯度商暂不加 $b-1$。

[原55条 Koszul 来源与特征零200/210呈示](R150-appendix-original-koszul-fiftyfive-quotient-and-characteristic-zero-twohundredten-presentation.md)已经在这个 $E$ 上给出完整、保权的
$$
F/\Gamma_E\simeq S/J_{17},
$$
其中 $\Gamma_E$ 由200条原梯度列生成，权为
$$
5^6,\quad6^{20},\quad7^{30},\quad8^{40},\quad9^{24},\quad10^{80}.
\tag{1}
$$
四十条权八列可以由该证明选择的原 $N_iC_s$ 给出。它们不必等于旧有限域呈示的十四条高列加二十六条乘积列；以下只使用同一完整模和生成元权上界。

本篇证明：
$$
\boxed{\dim_E(\Gamma_E)_7=312,\qquad
\dim_E(\Gamma_E)_8=1312.}
\tag{2}
$$
令 $q_j(y)=y^{\mathsf T}T'_j y$ 为原固定规范化的四个二次式，令 $\delta=\delta_{14}$ 为旧指定原四阶均值子式，则
$$
\boxed{
\dim_E\operatorname{span}\{[q_jb^2]:0\le j<4\}=4
\quad\text{在 }S/J_{17}\text{ 中}.
}
\tag{3}
$$
并且
$$
\boxed{
b\delta\notin J_{17},\qquad
y_i b\delta\notin J_{17}\quad(0\le i<6).
}
\tag{4}
$$
(4)是七个分别成立的非成员结论，没有声称六个权八类联合独立。

这些是完整原梯度理想中的非成员性，不限候选来源的次数。进一步，对于原十八方程 $A_1,\ldots,A_{17},b-1$ 的加权来源：
$$
\boxed{
0\ne q\in\operatorname{span}_E\{q_0,q_1,q_2,q_3\}
\Longrightarrow q\text{ 无来源权 }\le10\text{ 的表示};
\quad
\delta_{14}\text{ 无来源权 }\le9\text{ 的表示}.
}
\tag{5}
$$
来源权的定义及完整运输在 §6。所有结论在任意扩域后保持，包括固定复嵌入后的系数域；均未证明 Bell 理想非成员性、Bell 商非零、任意更高 $b$ 倍的非成员性或普通无限维 ISP 完成。

## 2. 合法系数环和原矩阵

在合法剩余点 $(127,d-100)$ 处，取原数域的局部系数环 $\mathcal A\subset E$，其分式域为 $E$，剩余域为 $k=\mathbb F_{127}$。可从
$$
\left(\mathbb Z_{(127)}[d]/(3725d^3-43931504d^2+6080833024d+52565262336)\right)_{(127,d-100)}
$$
取得此环。首项系数在127下为42，定义式及导数在100处的模127剩余分别为0和49，故这是此前已固定的合法 place。

所有本篇使用的原 $N_i$、原 mean、原 commutator、原选中高列及其参数单项式倍，都由既付原坐标与单位常数构造，并有已核准的合法约化；不倒任何 $y,w$ 参数。完整原模型与坐标/梯度运输见[原十行模型及116来源](R150-appendix-actual-original-ten-generator-parameter-module-and-116-certified-seeds127.md)。

四个 $q_j$ 的 $E$ 定义来自[完整原规范 pencil](R150-appendix-original-rank-three-mean-incidence-and-complete-sextic-pencil.md)：四个原对称 $T_i$ 的上三角位置 $(0,0),(0,1),(0,2),(0,3)$ 给原常数方块 $U$，以 $V=U^{-1}$ 定义 $T'_j=\sum_iT_iV_{ij}$。其约化行列式为74，且完整 $UV=VU=I_4$、原参数双向运输均已付。因此这些 $q_j$ 正是旧右端计算的同四个规范目标，且属于 $\mathcal A[y]$。不能改用任意四个未校准二次式。

$\delta_{14}$ 仍采用旧原 mean 矩阵的固定四列及四个二次轴，原目标定义和全梯度运输见[七个指定原右端](../notes/2026-11-16-r150-original-rank-four-bounded-rhs127-boundary-789f.md)。本篇不把它替换为规范 pencil 的另一子式。

记 $X_7,X_8$ 为旧完整原输入矩阵在 $E$ 上的同式矩阵，行使用全部带权参数单项式及十轴，列保原来源标签：
$$
X_7\in\mathcal A^{7754\times312},\qquad
X_8\in\mathcal A^{17674\times1386}.
\tag{6}
$$
其列是原 $Y,C,D,N_iY,N_iC$ 的相应单项式倍；列选择只选原标签，不把有限域消元组合当成原 $E$ 列。每一列都有原十七来源，故
$$
\operatorname{im}_E X_t\subset(\Gamma_E)_t\quad(t=7,8).
\tag{7}
$$
这里不要求新200呈示的全部系数在 $\mathcal A$ 内；维数上界只需在 $E$ 成立。需要合法约化的对象仅是(6)的原列和指定目标。

## 3. 维数夹逼引理

**引理。** 设 $\mathcal A$ 是整环、分式域为 $E$、剩余域为 $k$。设 $V\subset E^n$、$\dim_E V\le r$，$X$ 是 $\mathcal A$ 上的矩阵且每列属于 $V$。若
$$
\operatorname{rank}_k\overline X=r,
$$
则 $\operatorname{rank}_E X=r$ 且 $\operatorname{im}_E X=V$。若另有 $s$ 个整目标列组成 $T$，满足
$$
\operatorname{rank}_k[\overline X,\overline T]\ge r+s,
$$
则这 $s$ 个目标在 $E^n/V$ 中线性独立。

**证明。** 一个约化非零的 $r$ 阶原子式在 $\mathcal A$、因而在 $E$ 中非零，所以
$$
r\le\operatorname{rank}_E X\le\dim_E V\le r.
$$
所有不等号遂为等号。增广矩阵同理在 $E$ 中秩至少 $r+s$，故目标在商中的维数至少 $s$；它只有 $s$ 个生成元，遂独立。证毕。

引理允许 $E$ 中的任意候选系数，即使这些系数自身不整或其分母在该 place 消失。它使用原非零子式和独立的 $E$ 维数上界，不需要对候选表达式约化，也不需要提升某个有限域左核或余式。

## 4. 完整权七、八维数与同原输入的张满

参数环 Hilbert 级数为
$$
\sum_{a\ge0}\dim_E B_a\,t^a=(1-t)^{-6}(1-t^2)^{-6}.
$$
因此
$$
\dim B_0=1,\quad\dim B_1=6,\quad
\dim B_2=\binom72+6=27,\quad
\dim B_3=\binom83+6\cdot6=92.
$$
从完整生成权(1)得到
$$
\begin{aligned}
\dim_E(\Gamma_E)_7
&\le6\dim B_2+20\dim B_1+30
=6\cdot27+20\cdot6+30=312,\\
\dim_E(\Gamma_E)_8
&\le6\dim B_3+20\dim B_2+30\dim B_1+40\\
&=6\cdot92+20\cdot27+30\cdot6+40=1312.
\end{aligned}
\tag{8}
$$
这是完整齐次部分的上界：取任意生成表达式的相应权分量，权9、10列均不能贡献权7、8。高权项相消不会产生额外低权分量。

旧完整原矩阵的实际秩为
$$
\operatorname{rank}_k\overline X_7=312,\qquad
\operatorname{rank}_k\overline X_8=1312.
\tag{9}
$$
后者已付原1312阶单位，行列式为4；全74关系及原核产品也已付。父结果及链接集中在[原非Bell200呈示 §5](R150-appendix-original-nonbell-two-round-twohundred-presentation-and-weight-thresholds.md)。本篇只调用这些完整矩阵上的已付原子式与秩，不再重做消元。

由(7)—(9)及引理，
$$
\operatorname{im}_E X_7=(\Gamma_E)_7,\qquad
\operatorname{im}_E X_8=(\Gamma_E)_8,
$$
并得到(2)。由于 $\dim_E F_7=7754$、$\dim_E F_8=17674$，还得到两个准确的原梯度商分次维数
$$
\dim_E(S/J_{17})_7=7442,\qquad
\dim_E(S/J_{17})_8=16362.
\tag{10}
$$
本篇没有宣称已知整个 Hilbert 级数。

## 5. 四个规范目标与七个 delta 目标

### 5.1 四个规范二次式

[四个字面规范目标及根独立审计](../notes/2026-11-16-r150-original-canonical-mean-quadrics-bounded-rhs127-boundary-789f.md)已从同一原模型重建 $U,V,T'_j,q_j$，逐全部70696个目标坐标核同，并核四个目标
$$
\overline t_j=\overline{q_jb^2e_0}
$$
在旧1312阶单位的全部行坐标上为零。四个 $q_j$ 在普通二次单项式 $y_0^2,y_0y_1,y_0y_2,y_0y_3$ 上的系数块为
$$
\operatorname{diag}(1,2,2,2),
$$
行列式为8，故四个 $\overline q_j$ 线性独立。由于 $k[y,w]$ 是整环且 $\overline b^2\ne0$，四个 $\overline t_j$ 也独立。

单位行限制在 $\operatorname{im}_k\overline X_8$ 上单射，而每个 $\overline t_j$ 在这些行上为零。因此
$$
\operatorname{span}_k\{\overline t_0,\ldots,\overline t_3\}
\cap\operatorname{im}_k\overline X_8=0,
$$
从而
$$
\operatorname{rank}_k[\overline X_8,\overline t_0,\ldots,\overline t_3]=1316.
\tag{11}
$$
把引理用于(8)的 $r=1312$ 及四目标，得到(3)。这里既不用新选40列的实际索引，也不用新权八大矩阵。

### 5.2 七个 delta 目标

[完整七右端计算及根的全原产品复核](../notes/2026-11-16-r150-original-rank-four-bounded-rhs127-boundary-789f.md)已验证完整原输入上的
$$
\overline t=\overline X\,c+r
$$
（与该文件行存储记号的转置等价），全部113798个产品坐标成立；每个余式在相应全主元行上为零，且非零坐标数为：

| 原目标 | 权 | 非零余式坐标数 |
|---|---:|---:|
| $b\delta e_0$ | 7 | 5371 |
| $y_0b\delta e_0$ | 8 | 13123 |
| $y_1b\delta e_0$ | 8 | 13103 |
| $y_2b\delta e_0$ | 8 | 13105 |
| $y_3b\delta e_0$ | 8 | 13109 |
| $y_4b\delta e_0$ | 8 | 13099 |
| $y_5b\delta e_0$ | 8 | 13092 |

若 $\overline t$ 在原列空间中，则 $r$ 也在该空间中；其全部单位行坐标为零迫使 $r=0$，与上表矛盾。所以七个增广矩阵逐个具有秩313或1313。由引理和(8)，七个原 $E$ 目标逐个不在 $(\Gamma_E)_7$ 或 $(\Gamma_E)_8$。完整商同构给(4)。

这些目标都是齐次的。齐次理想中齐次元素的成员性只取其同权分量，所以(3)、(4)不只是某个有界来源表的负结论，而是完整 $J_{17}$ 非成员性。未求六个权八 delta 类的联合增广秩，不能把逐个非零改称联合独立。

## 6. 原十八方程的过滤保持与严格来源权下界

令 $A=(A_1,\ldots,A_{17})$，$g_i=\operatorname{wt}A_i\in\{4,5\}$。原十八来源权至多 $K$ 的定义是
$$
f=\sum_{i=1}^{17}a_iA_i+(b-1)h,\qquad
\deg_w a_i+g_i\le K,\qquad\deg_w h+3\le K.
\tag{12}
$$
这控制每项来源，不能只看最终抵消后的输出权。

[原十八来源过滤等价](R150-appendix-original-eighteen-source-weight-filtration-equivalence.md)的代数证明在本篇完整原 $E$ 呈示下逐步成立。为明确本次提升所用内容，重述如下。

定义保权 $B$ 线性映射
$$
\tau:F\to S,\quad\tau(v)=mv,
\qquad
\pi(cu_0^{a_0}\cdots u_4^{a_4})
=cN_0^{a_0}\cdots N_4^{a_4}e_0.
$$
固定有序乘法，不把自由 $F$ 上的 $\pi$ 当作环同态。原字面路径给 $\pi\tau=I_F$。完整原边界恒等式 $mN_i=u_i m-AS_i$ 的单项式归纳给
$$
f-\tau\pi(f)\in J_{17},
$$
且可取来源权至多 $\deg_w f$。完整稳定商给 $\pi(J_{17})\subset\Gamma_E$。由(1)的齐次生成，
$$
\Gamma_E\cap F_{\le K}
=\sum_j B_{\le K-\nu_j}\gamma_j.
$$
每个 $\gamma_j$ 的真实原十七来源可取同权分量，且 Bell 槽为零。因此对 $f\in S_{\le K}$，
$$
\text{(12)}
\iff
\pi(f)=G+(b-1)H
$$
有参数列来源权至多 $K$ 和 $\deg_w H+3\le K$。正向施 $\pi$ 并使用其 $B$ 线性；反向施 $\tau$、回填同权原来源并加入 $f-\tau\pi(f)$。全程保持所有原 $u,y,w$ 参数和原十七来源。

对 $f\in B$，$\pi(f)=fe_0$。若 $0\ne q\in\operatorname{span}_E\{q_j\}$ 有来源权至多10，按权模3只需比较权2、5、8。$\Gamma_E$ 最低权为5，故
$$
H_2=-qe_0,\qquad
H_5=G_5-bqe_0,\qquad
b^2qe_0=G_8+bG_5\in(\Gamma_E)_8.
$$
中间 $G_5$ 完整保留。式(3)排除此事。

若 $\delta_{14}$ 有来源权至多9，则目标同余类只需权1、4、7。最低两权给
$$
H_1=0,\qquad H_4=-\delta_{14}e_0,
$$
最高权随后给 $G_7=b\delta_{14}e_0$，与(4)矛盾。遂得(5)。

任意扩域 $L/E$ 是平坦的；完整商、齐次部分及上述有限维类的独立性在张量后保持。因此相同非成员性和来源权下界也排除 $L$ 系数的候选来源，无须要求这些系数在所选127 place整。

## 7. 证据边界与继续任务

本篇新增的是特征零上界、原子式下界的夹逼，以及完整来源过滤的原 $E$ 推论。其计算证据严格复用：

- 原权七/八完整秩与1312阶原单位；没有新消元。
- 七 delta 右端的完整113798坐标及独立原输入审计。
- 四规范目标的完整70696字面坐标、原规范化和单位行零坐标。
- 原 $E$ exact-low20、原四次95核、真实 $G$-Koszul 消源及完整200呈示；不是有限域换源的系数提升。

根逐节复读相关父证明和完整原目标边界；normal_annihilator 独立复核维数、同原列合法约化、规范化及过滤权比较。没有新增大数组或本地算术执行声明。

仍须分别处理 $\delta_{14}b^2$ 的权10、$q_jb^3$ 的权11及可能更高幂，或寻找不同原 Bell 单位来源。本篇不能把(3)、(4)改写为 $q_j$、$\delta_{14}$ 在 $J_{17}+(b-1)$ 中非成员，也不决定十九图的全覆盖结果。普通复 Hilbert ISP 与当前其余 open 项继续开放。
