# R537 — 原切向返回的全部核、不可分排除与来源饱和

日期：2026-11-14。**状态：已证明。** 本篇继续 R517 的真实
\(\mathcal H_2\) 切向返回。在一个覆盖 R495 满主阶二次临界窗的明确范围内，
确定它在实际多项式来源中的全部核，而不只知道 \(F^2\) 给一条关系。

关键是：若两个独立多项式的 Jacobian 为零，其函数域扩张的不可分次数至少为 \(p\)；
本题原 \(\mathbb F_4\) 上的交数却给出一个严格小于 \(p\) 的上界。
随后在**未局部化的** \(k[t,Y]\) 中用不可约纤维和正规中间曲线证明
\(k(F)\) 在 \(k(t,Y)\) 中相对代数闭，并确定其与多项式环的交。全部十九个实际角条件决定最终核是一维还是三维。
保持角阶与次数的整提升再给来源返回像的 \(p\) 饱和与准确秩。

这是来源返回的结果。评价到原 \(\Gamma\) 后还可以产生新的关系，
物理像的饱和、原首 Bockstein、\(d_2/G_2\) 和完整中央非零均未由本篇推出。

## 1. 同一实际因子、曲面和三个返回

保持 R491、R495、R498、R517 的原对象。特别，
$$
d^{C_D}\bar P=t^rF^3Q,\qquad
\bar P\in\overline{\mathcal W}_D,\qquad
F(0,1)=0,\qquad F_Y(0,1)Q(0,1)\ne0,
$$
其中 \(F\in k[t,Y]\) 不可约、\(Y=\mathscr R\)、\(d=1+8t\)。
令
$$
b=\deg_YF\ge1,\qquad
F=\sum_{i=0}^b f_i(t)Y^i,\qquad
u=\max_i(\deg f_i-4i)\ge0.
\tag{1}
$$
这里已清除原固定 \(d\) 分母，\(F\) 本身处于未局部化的多项式环。
因 \(F\ne Y\)，有 \(f_0\ne0\)；各 \(f_i\) 没有共同有限角因子。

在 R495 的同一 \(\mathbb F_4\) 上，
$$
C_0\sim bS_0+(u+4b)F_0,\qquad
C_0^2=4b^2+2bu.
$$
\(X\) 仍是原十九个普通吹起，\(C\) 是严格变换。记
$$
\kappa=C^2,\qquad \chi=-K_XC,\qquad
\mathcal H_2=H^0(X,\mathcal O_X(2C)).
$$
R495 给
$$
\boxed{\dim_k\mathcal H_2=1+2\kappa+\chi.}
\tag{2}
$$
全部空间可先扩到代数闭剩余域；矩阵秩和以下核基随后下降。
R495 已由不可约 \(F\) 及 \(k\) 有理光滑点 \(P=(0,1)\) 支付几何整性。

继续使用真实导子
$$
\delta=t\partial_t,\qquad \mathcal E=Y\partial_Y,\qquad
\boxed{\mathcal V_F=(\mathcal EF)\delta-(\delta F)\mathcal E.}
\tag{3}
$$
R517、R521 的已付返回包括
$$
\mathfrak m_2=Y^2t(t-1)^2h_7^2,\qquad
H\longmapsto d^{-C_D}t^rQ\,\mathfrak m_2\mathcal V_FH,
\tag{4}
$$
$$
\mathfrak m_3=Y^3t(t-1)^2h_7^3d^2,\qquad
H\longmapsto d^{-C_D}t^rQ\,\mathfrak m_3\mathcal V_FH,
\tag{5}
$$
以及 R517 的缓冲返回
$$
H\longmapsto d^{-C_D}t^{r-4}Q\,(t-1)h_7d\,\mathcal V_FH.
\tag{6}
$$
(4)、(5) 分别保原两个、三个 charge 成本；只有已付相应余量时才仍在同一
\(\mathcal W_D\)。式 (6) 保
$$
r\ge4,\qquad v_0(P^{\rm fact})\ge14,
\tag{7}
$$
其仅用原参数的充分门仍是 \(4r-D\ge14\)。
本篇不放宽这些成员性条件，也不删 (6) 的真实低行。

以下的新增素数范围为
$$
\boxed{p>83,\qquad p>2C_0^2=8b^2+4bu.}
\tag{8}
$$

## 2. 原交数严格排除独立的 Jacobian 零对

**引理 1。** 设 \(H\in\mathcal H_2\)。在 (8) 下，
$$
\mathcal V_FH=0\quad\Longrightarrow\quad
F,H\text{ 在 }k(t,Y)\text{ 中代数相关}.
\tag{9}
$$

**证明。** 由原导子的定义，
$$
\mathcal V_FH=tY(F_YH_t-F_tH_Y).
$$
未局部化多项式环是整环，所以其为零准确等价于 Jacobian 为零。

若 \(F,H\) 代数独立，记
$$
L=k(t,Y),\qquad K=k(F,H).
$$
扩张 \(L/K\) 有限。\(k\) 完美，且 \(dF,dH\) 在
\(\Omega^1_{L/k}\) 中相关，因此这个有限扩张不可分。
于是
$$
p\mid[L:K],\qquad [L:K]\ge p.
\tag{10}
$$

另一方面，原 \(\mathcal H_2\) 的每个多项式满足
$$
\deg_YH\le2b,\qquad \deg_tH_i\le2u+4i.
\tag{11}
$$
所以对两个独立通用常数 \(c_1,c_2\)，
\(F-c_1\)、\(H-c_2\) 在 \(\mathbb F_4\) 上分别是
类 \(C_0\)、\(2C_0\) 的截面。
它们在仿射平面的通用纤维长度准确为 \([L:K]\)，包含不可分重数。
曲面上的完整交数还包括可能的边界交点，不能小于这个长度，故
$$
[L:K]\le C_0(2C_0)=2C_0^2.
\tag{12}
$$
这里无需把吹起后的 \(\kappa\) 代入一个未付的移动纤维次数：
使用的是明确的原 ambient 类 \(C_0\)。
通用 \(F-c_1\) 没有整个边界曲线作为分量；
两条通用纤维在仿射部分也无共同曲线，因为 \(F,H\) 代数独立。
因此 (12) 是有效的零维交数上界。
(8)、(10)、(12) 矛盾。证毕。

这个步骤不能只以 \(b<p\) 代替 (8)。
正特征中两个独立低次数多项式的 Jacobian 仍可能为零；
必须支付整个不可分次数的交数界。

## 3. 未局部化多项式环中的全部第一积分

**引理 2。** 在代数闭域 \(k\) 上，若
\(F\in k[t,Y]\) 不可约、非常数，则 \(k(F)\) 在 \(k(t,Y)\) 中相对代数闭，且 \(k(F)\cap k[t,Y]=k[F]\)。
因而任一多项式 \(H\in k[t,Y]\) 若代数于 \(k(F)\)，必属于 \(k[F]\)。

**证明。** 令 \(K'\) 为 \(k(F)\) 在 \(k(t,Y)\) 中的相对代数闭包。
它是 \(k(F)\) 的有限扩张。
令 \(B\) 为 \(k[F]\) 在 \(K'\) 中的整闭包，则 \(B\) 有限于 \(k[F]\)，
并且
$$
B\subset k[t,Y].
\tag{13}
$$
确实，\(B\) 的元素整于 \(k[F]\)，所以也整于正规环 \(k[t,Y]\)；
其元素又在 \(k(t,Y)\) 中，因而属于该多项式环。

置 \(Z=\operatorname{Spec}B\)。
包含 (13) 给支配态射 \(\mathbb A^2\to Z\)。
选一条使某个非常数 \(B\) 元素的限制仍非常数的仿射直线，
得到 \(\mathbb A^1\to Z\) 的支配态射。
所以 \(k(Z)\) 嵌入 \(k(z)\)；由 Lüroth 定理，
\(Z\) 的光滑射影完备化是 \(\mathbb P^1\)。

同时
$$
B^\times\subset k[t,Y]^\times=k^\times.
$$
故这个仿射有理曲线的完备化只能删去一个点：
若删去至少两个点，它们的比值函数会给一个非常数单位；
若一个点也不删，则不是维数一的仿射曲线。
于是 \(B=k[G]\)，且 (13) 保 \(G\in k[t,Y]\)。

现在 \(F=P(G)\)，其中 \(P\in k[Z]\)。
若 \(\deg P>1\)，在代数闭域分解 \(P\)，
每个 \(G-\alpha\) 都是非常数多项式。
这使 \(F\) 分解为至少两个非单位因子，计入重数后同样如此，
与 \(F\) 不可约且约化矛盾。
故 \(\deg P=1\)，得到 \(K'=k(F)\)。

最后若 \(H=A(F)/B_0(F)\in k[t,Y]\)，可令 \(A,B_0\) 互素。
它们在 \(k[F]\) 中的 Bézout 恒等式说明 \(B_0(F)\) 必为
\(k[t,Y]\) 的单位，故 \(B_0\) 为常数。于是 \(H\in k[F]\)。证毕。

本引理的单位论证只用于 \(k[t,Y]\)；
不用于 \(k[t,Y,d^{-1}]\)，更不用于加入任意角单位逆的环。
这也是第1节先清原固定分母的原因。

由两个引理及 \(\deg_YH\le2b\)，立即得到
$$
\boxed{\ker(\mathcal V_F:\mathcal H_2\to k[t,Y])
=\mathcal H_2\cap\langle1,F,F^2\rangle_k.}
\tag{14}
$$
下一节准确计算这个交，不能预先把 \(1,F\) 当成真实来源。

## 4. 全部十九角将核准确分成两种

记 \(a_d=-1/8\)。定义
$$
\varepsilon_F=
\begin{cases}
1,&F(a_d,0)=f_0(a_d)=0,\\
3,&F(a_d,0)\ne0.
\end{cases}
\tag{15}
$$

**定理 1。** 在 (8) 中，准确有
$$
\boxed{
\ker\mathcal V_F|_{\mathcal H_2}=
\begin{cases}
kF^2,&F(-1/8,0)=0,\\
k\cdot1\oplus k\cdot F\oplus k\cdot F^2,&F(-1/8,0)\ne0.
\end{cases}}
\tag{16}
$$
特别，第二种情形的 \(1,F\) 确实满足原 \(\mathcal H_2\) 的全部条件，
并非只在环境多项式环中存在。

**证明。** 使用 R495 全部中间链，而非只检查最后一个 Gauss 值。

对 \(a=0\) 和两个 \(h_7\) 根、\(1\le j\le4\)，以及
\(a=1\)、\(1\le j\le3\)，置
$$
v_{a,j}(F)=\min_i\{j\operatorname{ord}_a f_i-i\}.
$$
因为各 \(f_i\) 无共同角因子，某个 \(f_i\) 在 \(a\) 为单位，所以
$$
v_{a,j}(F)\le0.
\tag{17}
$$
对无穷远两步链，
$$
v_{\infty,j}(F)=\min_i\{-j\deg f_i+(4j+1)i\}\le-j\deg f_0\le0,
\qquad j=1,2.
\tag{18}
$$
(17)、(18) 中任一赋值 \(v\) 都满足
$$
v(c_0+c_1F+c_2F^2)\ge2v(F)
$$
对全部 \(c_i\in k\) 成立；抵消只能提高赋值。
加入原 \(2b\)、\(2ju\) 平凡化因子后，
这正是 \(\mathcal O_X(2C)\) 在相应中间例外除子上的条件。

剩余的是 \(d=0,Y=0\) 的两步链：
$$
v_{d,j}(F)=\min_i\{j\operatorname{ord}_{a_d}f_i+i\},\qquad j=1,2.
\tag{19}
$$
这些值非负。
若 \(f_0(a_d)\ne0\)，它们都为零，
所以 \(1,F,F^2\) 在这两步也全部满足要求。

若 \(f_0(a_d)=0\)，则两个值都严格为正。
在其中任一赋值下，\(1,F,F^2\) 的值分别为
\(0,v,2v\)，三者严格不同。
因此要使 \(c_0+c_1F+c_2F^2\) 达到所需的 \(2v\)，
必须先有 \(c_0=0\)，再有 \(c_1=0\)。
\(F^2\) 则在全部链准确达到原因子的两倍条件。

最后，ambient 帽也全部保留：
\(u\ge0\) 使 \(1,F,F^2\) 都满足 (11)。
结合 (14) 得 (16)。对非代数闭 \(k\)，三份多项式均在原域定义且线性独立，
故核基和维数下降。证毕。

由 (2)、(16)，多项式切向像的准确秩为
$$
\boxed{
\operatorname{rank}\mathcal V_F|_{\mathcal H_2}
=1+2\kappa+\chi-\varepsilon_F
=
\begin{cases}
2\kappa+\chi,&f_0(-1/8)=0,\\
2\kappa+\chi-2,&f_0(-1/8)\ne0.
\end{cases}}
\tag{20}
$$
乘 (4)、(5)、(6) 中任一已付的非零前缀不改变这个核与秩。

## 5. 真实整提升与来源返回像的 p 饱和

取 R491/R498 的角保持整提升，进一步按每个系数的原次数提升：
每个非零 \(f_i\) 保各固定有限角的准确阶、准确次数和最高项单位。
具体可先提出已知的有限角因子，再提升剩余多项式；
固定角两两不碰撞，所有分母在当前好位均为单位。
这同时保持 R495 的全部十九个中间重数。
尤其
$$
\deg\widetilde F=\deg\bar F
$$
对总次数成立，
且 \(f_0(-1/8)=0\) 时提升仍在该点准确为零；
非零时提升值是整单位。

这样的 \(\widetilde F\) 在分式域上仍几何不可约。
若在某有限系数扩张中分解，利用 Gauss 赋值将两因子正规化为
整且约化非零。约化的几何不可约性使其中一个因子约化为常数。
若该因子有正总次数，乘积总次数将严格大于其约化的总次数，
与上面的次数保持矛盾。故没有非平凡分解。

令 \(\widetilde{\mathcal H}_2\) 为 R498 的有限自由整系数格；
其约化准确是 \(\mathcal H_2\)。
令 \(\mathcal T\) 是 (4)、(5) 或 (6) 中一个确实返回所用
\(\mathcal W\) 的整多项式矩阵。
保持对应的成本、原 \(Q\)、全部角条件和整前缀。

**定理 2。** 在上述提升与 (8) 下，
\(\ker\mathcal T\) 是 (16) 的同一整核基：
或 \(\mathcal O\widetilde F^2\)，
或 \(\mathcal O\cdot1\oplus\mathcal O\cdot\widetilde F
\oplus\mathcal O\cdot\widetilde F^2\)。
而且
$$
\boxed{\operatorname{im}\mathcal T\subset\mathcal W
\text{ 是 }p\text{ 饱和的有限自由子格}.}
\tag{21}
$$
其秩准确为 (20)。

**证明。** 特征零中 Jacobian 零的独立对不可能存在；
第3节的正规中间曲线论证和第4节的同一整角条件，
给分式域上的上述核。
这些显示核向量的约化线性独立：
\(1,\bar F,\bar F^2\) 的不同 \(Y\) 次数直接保证这一点。
因此它们在整多项式格中生成饱和子格，分式域核与原整格的交
正是所写的整核。

模 \(p\) 后，由定理1，核的维数仍准确为 \(\varepsilon_F\)。
返回前缀的约化是非零有理函数；
在原 \(k[t,Y]\) 清共同 \(d\) 分母后乘法仍单射，
所以它不增加任何模 \(p\) 的来源关系。
故整矩阵 \(\mathcal T\) 与其约化具有相同秩
\(1+2\kappa+\chi-\varepsilon_F\)。
Smith 形式的每个非零因子因而都是单位，证明 (21)。证毕。

同一结论也适用于先把像放在 R517/R521 的完整
\(\mathcal H_{3,2}\)、\(\mathcal H_{3,3}\) 比较格中。
称为原 \(\mathcal W_D\) 的子格时，则仍须实际满足第1节的同 \(D\) 返回门。

## 6. 明确覆盖哪一段实际临界预算

(8) 是逐个实际因子的准确条件，不以“通常足够大”替代它。
它确实覆盖此前保留的满主阶二次窗口。

例如保 R495 第8节的实际候选条件
$$
D=3b,\qquad u=b+O(1),\qquad
2s+\ell=\dim\mathcal W_{3b}+o(b^2),\qquad
\ell/s\longrightarrow\lambda\in[0,1),
$$
以及原
$$
\dim\mathcal W_{3b}=\frac{141}{8}b^2+O(b).
$$
则
$$
p=\left(\frac{423}{4(2+\lambda)}+o(1)\right)b^2,\qquad
2C_0^2=12b^2+O(b).
\tag{22}
$$
右侧主常数严格小于左侧，故 (8) 最终成立。
特别低 \(\ell\) 时 \(\lambda=0\)，左侧常数为 \(423/8\)。

这个覆盖只用于**已经存在**且满足这些原预算的真实候选。
R495 的人工形状族不因此获得原 theta 的深接触；
本篇也没有由角帽制造一个首核。

## 7. 到原物理矩阵时可以使用什么

置
$$
\mathcal U_{\mathcal T}=\operatorname{im}\mathcal T\subset\mathcal W.
$$
由定理2，
$$
\widetilde{\mathcal H}_2/\ker\mathcal T
\xrightarrow{\ \sim\ }\mathcal U_{\mathcal T}
$$
是整格同构，并且 \(\mathcal U_{\mathcal T}\) 在来源 \(\mathcal W\) 中饱和。
所以对原完整 \(J\) 或 \(M\)，使用
\(J\mathcal T\)、\(M\mathcal T\) 这个自由呈示，
只多出准确的 \(\varepsilon_F\) 个零列；
其余 Smith 因子准确就是限制矩阵
\(J|_{\mathcal U_{\mathcal T}}\)、\(M|_{\mathcal U_{\mathcal T}}\) 的因子。
不会因来源返回本身再引入一个未计的 \(p\) 因子。

不过，
$$
\ker(\bar J\,\bar{\mathcal T})/\ker\bar{\mathcal T}
\quad\text{及}\quad
\ker(\bar M\,\bar{\mathcal T})/\ker\bar{\mathcal T}
$$
仍可能非零。这些是原评价产生的新关系，
不是第4节的多项式第一积分。
因此 (20)、(21) **不是**物理切向像的满秩或饱和声明。

R517 的全 \(\Gamma\) 恒等式与完整转置继续按原矩阵使用：
\(\epsilon\) 的导数、\(w^s=p\epsilon\) carry、三 normal 系数及低行高尾全保。
原
$$
M=c_*U_0m_{13}J
$$
的 \(P_{134}/U_0\)、十三自由行、两条十三行 carry 和同一修正
\(d_2/G_2\) 也均不改变。

本篇支付了此前切向呈示中的全部来源冗余和不可分风险。
下一实际比较仍是其物理像与 R524 两连接所产生的边界核：
R521 的显示 forcing 残数须杀那个真实核及其余原列，才会给原余核的非零类。
三条完整中央没有被赋给这些切向列。
