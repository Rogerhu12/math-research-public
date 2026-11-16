# 原十八方程与完整参数呈示的加权来源过滤等价

作者：OpenAI ChatGPT /root（GPT-6 Astra Pro）；normal_annihilator、literature_audit 独立交叉审查；2026-11-16。

本篇补齐[原非Bell完整200列呈示](R150-appendix-original-nonbell-two-round-twohundred-presentation-and-weight-thresholds.md)最后明确保留的过滤接口。系数仍严格为 $\mathbf F_{127}$、原合法剩余点 $d=100$。本篇没有新增消元或数学数组，也不向原数域 $E$ 提升。

## 1. 两种来源界的准确含义

沿用
$$
B=\mathbf F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad
S=B[u_0,\ldots,u_4],\qquad F=B^{10},
$$
以及 $\operatorname{wt}(y)=1$、$\operatorname{wt}(w)=\operatorname{wt}(u)=2$。原十轴 $e_a$ 的权为
$$
(d_a)=(0,2,2,2,2,2,4,4,4,4).
$$
令原十七生成元行是 $A=(A_1,\ldots,A_{17})$，$J_{17}=(A)$。这正是原完整坐标运输后的十七梯度，十一项的权为4，六项的权为5；记其权为 $g_i$。原第十八方程为 $b-1$，其中 $b=y\cdot w$ 的最高权为3。每个 $A_i$ 都齐次。

这些权可直接由已固定原基底逐项检查。[24条新均值来源的根独立审计](../notes/2026-11-16-r150-original-complete210-mean24-source-checkpoint-789f.md)已实际核全部十七原生成元项，顺序为十一项权4和六项权5。这里使用的是这套原 Bell 坐标加权次数，不能改称普通多项式总次数。

对任意 $f\in S$，称有**原十八来源权至多 $K$**的表示，是指
$$
f=\sum_{i=1}^{17}a_iA_i+(b-1)h,
\qquad
\deg_w a_i+g_i\le K,\quad
\deg_w h+3\le K.
$$
零系数不受次数限制。这个定义控制每项来源的权；不能先用任意高权来源，因最高项相消就称界为 $K$。

记完整200列为 $\gamma_j\in F$，其权为
$$
(\nu_j)=5^6,\ 6^{20},\ 7^{30},\ 8^{40},\ 9^{24},\ 10^{80},
\qquad
\Gamma=B\langle\gamma_1,\ldots,\gamma_{200}\rangle.
$$
对向量 $v\in F$，称有**参数呈示来源权至多 $K$**的表示，是指
$$
v=\sum_jc_j\gamma_j+(b-1)H,
\qquad
\deg_w c_j+\nu_j\le K,\quad
\deg_w H+3\le K.
$$
这里 $\deg_w H=\max_a(\deg_w H_a+d_a)$，同样不能从抵消后的输出权冒充来源界。

## 2. 两个保权线性映射

令
$$
m=(1,u_0,\ldots,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4),
\qquad
\tau:F\longrightarrow S,\quad \tau(v)=mv.
$$
$\tau$ 是保权的 $B$ 线性映射。

固定普通 $u$ 单项式的顺序，定义
$$
\pi\!\left(c\,u_0^{a_0}\cdots u_4^{a_4}\right)
=c\,N_0^{a_0}\cdots N_4^{a_4}e_0,\qquad c\in B,
$$
并 $B$ 线性延伸。原矩阵 $N_i$ 在带权十轴上齐次地增加权2，所以 $\pi$ 保权。此处不把尚未取商的 $N_i$ 当作可交换算子，也不声称自由十轴上的 $\pi$ 是环同态。

原九条字面路径给
$$
\pi(m_a)=e_a,\qquad \pi\tau=I_F.
$$
原完整边界恒等式为
$$
mN_i=u_i m-A S_i,
$$
其中这里已省去恒为零的第十八来源坐标。逐次应用该恒等式可得
$$
f-\tau\pi(f)\in J_{17}.
$$
当 $f$ 齐次权为 $t$ 时，差式也齐次权 $t$。每个边界源可取其准确齐次分量，因此差式有原十七来源权恰不超过 $t$ 的表示。对一般 $f$ 逐个齐次分量相加，得到来源权不超过 $\deg_w f$。

这一论证无需展开全部高次单项式：它是对单项式长度的有限归纳。非交换原矩阵的次序始终固定，原 $u_i$ 在 $S$ 中照常交换。

## 3. 完整200列商给出的齐次核

父证明已给完整的保权同构
$$
F/\Gamma\simeq S/J_{17}.
$$
其正向是 $\tau$，反向由 $1\mapsto e_0$ 和取商后的五个可交换 $N_i$ 给出。因此
$$
\pi(J_{17})\subset\Gamma.
$$
这一包含不能仅由某个有限首轮或有界矩阵代替；本篇确实使用了已经证明稳定的完整两轮呈示。

由于 $\Gamma$ 由齐次列生成，正权分次严格给
$$
\Gamma\cap F_{\le K}
=\sum_j B_{\le K-\nu_j}\gamma_j.
$$
证明是对任意来源表达式取每个输出权 $t\le K$ 的齐次分量。权大于 $K$ 的列或系数项无法贡献这些分量；高权相消没有例外。

每个 $\gamma_j$ 都有原十七来源
$$
\tau(\gamma_j)=A\sigma_j.
$$
左端齐次权为 $\nu_j$；取右端该权的分量，即可令第 $i$ 项来源系数齐次权为 $\nu_j-g_i$。因此所有命名列都可用同权的原十七来源回填。即使某个先前保存的来源有多余齐次块，这个取分量步骤也不会增加来源权。原第十八来源全为零是此步骤所需的已付事实。

## 4. 完整过滤等价

对任意 $f\in S_{\le K}$，有
$$
\boxed{
f\text{ 有原十八来源权 }\le K
\iff
\pi(f)\text{ 有参数200列呈示来源权 }\le K.
}
$$

**正向。** 设
$$
f=g+(b-1)h,\qquad
g=\sum_i a_iA_i,
$$
并且满足 §1 的原来源界。则 $g\in J_{17}\cap S_{\le K}$，$\deg_w h\le K-3$。因为 $\pi$ 是保权的 $B$ 线性映射且 $b\in B$，
$$
\pi(f)=\pi(g)+(b-1)\pi(h).
$$
由 §3，$\pi(g)\in\Gamma\cap F_{\le K}$，故可用200列的来源权至多 $K$ 的系数表达；而 $\deg_w\pi(h)\le K-3$。这就是所需参数来源界。

**反向。** 设
$$
\pi(f)=\sum_j c_j\gamma_j+(b-1)H
$$
满足参数来源界。施 $\tau$ 并用每列的同权原来源，得到
$$
\tau\pi(f)
=A\left(\sum_jc_j\sigma_j\right)+(b-1)\tau(H).
$$
所有来源项权至多 $K$；$\tau$ 保权，故 Bell 系数权至多 $K-3$。再加入 §2 的差式 $f-\tau\pi(f)$，其原十七来源权至多 $\deg_w f\le K$，便得到完整原十八来源界。

对本次目标 $q_j,\delta_{14}\in B$，还更直接：
$$
\pi(f)=fe_0,\qquad \tau\pi(f)=f.
$$
于是反向的补差字面为零，没有额外损失。

## 5. 原十八加权来源的严格新下界

父证明由已完成的完整权七/八计算严格得到
$$
b\delta_{14}e_0\notin\Gamma_7,
\qquad
\operatorname{span}_{\mathbf F_{127}}
\{q_jb^2e_0:0\le j<4\}\cap\Gamma_8=0.
$$
四维规范 $q$ 空间是真正的原 $T\mapsto T'$ 规范化所得，不是任意四个未校准的二次式。

对非零 $q\in\operatorname{span}_{\mathbf F_{127}}\{q_j\}$，若参数来源权至多10，则按权模3只需保留权 $2,5,8$：
$$
H_2=-qe_0,\qquad H_5=G_5-bqe_0,\qquad
b^2qe_0=G_8+bG_5\in\Gamma_8.
$$
中间 $G_5$ 不能删除。已付的整个四维交零排除了这种表示；由 §4，
$$
\boxed{
0\ne q\in\operatorname{span}\{q_0,q_1,q_2,q_3\}
\ \Longrightarrow\
q\text{ 没有原十八加权来源权 }\le10\text{ 的表示}.
}
$$

对 $\delta_{14}$，若来源权至多9，目标同余类只需比较权 $1,4,7$。最低权给 $H_1=0$、$H_4=-\delta_{14}e_0$，然后
$$
G_7=b\delta_{14}e_0,
$$
与已付权七非成员性矛盾。故
$$
\boxed{
\delta_{14}\text{ 没有原十八加权来源权 }\le9\text{ 的表示}.
}
$$

两条结论都控制任意原来源中出现的 $u$ 次数及参数系数，而不是只控制一个预先截断的乘子表；控制方式是明确的总加权来源界。它们不排除更高权来源，也不排除加 Bell 后的完整理想成员性或 $b$ 的更高幂饱和。它们仍不是 $E$ 上的非成员性、普通次数界或原无限维 ISP 的完成结论。

## 6. 审查与接续

normal_annihilator、literature_audit 已分别独立复核保权 $\pi$、完整齐次核、Bell 项的 $B$ 线性运输与反向原来源回填。根将此前仅参数呈示的界与本篇新增的原十八过滤等价严格分开，原文无需追溯改变其当时已证明的范围。

下一不同目标仍为 $\delta_{14}b^2$ 的权10及 $q_jb^3$ 的权11；本篇不重算已经排除的权7/8空间，不把新增104条的来源生产冒充更高权成员计算。
