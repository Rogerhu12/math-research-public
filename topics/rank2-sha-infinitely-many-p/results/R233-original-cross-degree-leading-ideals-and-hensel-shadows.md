# R233 — 原跨齐次交集的首项理想、逐精度 shadow 与真实提升障碍

日期：2026-11-13。**状态：同一个完整前缀中的环结构、首项理想与交集长度的准确对应、全部 colon 层的二元增长、以及原 Hensel 障碍序列均已证明。** 在大素数主带，所得增长全部属于原跨齐次交集。本文没有证明双完整中央零给出这些实际理想的低次生成元，也没有把首项可除以 $p$ 当成整条原关系可除以 $p$。

本篇承接 [R224](R224-radial-image-euler-hasse-observation-and-cross-degree-relations.md) 的同一目标内跨齐次交集，并把 R223 的原乘法输入组织成逐精度、逐次数的实际理想。下文始终固定同一个 $k$ 和同一个模 $p^N$ 目标；次数增加时不更换前缀。

## 1. 原加权前缀确实是一个有限环

令素数 $p=4r-1\ge19$、$\mathcal O=\mathbf Z_p$、$v_0=-22$。使用 R224 的原严格参数
$$
u=\frac{C}{v_0A},\qquad F=\frac{v_0A^2}{C},
\qquad A=uF,\quad C=v_0u^2F.
\tag{1}
$$
原 $A,C=B-A$ 多项式源不变。原 $w$ 与 $u$ 的每个完整加权前缀由同一个整可逆代换相识别。

写 $h_n=\lfloor n/r\rfloor$，并令
$$
e_n=
\begin{cases}
0,&h_n=0,\\
h_n+\lfloor(h_n-1)/(p-1)\rfloor,&h_n\ge1.
\end{cases}
\tag{2}
$$
R215 已证明全部原行整性；R224 又给出
$$
F,F^{-1},\ A/u,\ C/(v_0u^2)\in
\mathscr B_e,\qquad
\mathscr B_e=
\left\{\sum_{n\ge0}a_nu^n:v_p(a_n)\ge-e_n\right\}.
\tag{3}
$$
所需乘法由准确的超可加性
$$
e_{i+j}\ge e_i+e_j
\tag{4}
$$
保证。它也可直接由 (2) 的两个取整函数核对。

令 $\mathfrak a_k$ 为 $\mathscr B_e$ 中前 $k$ 个系数全部为零的理想，并置
$$
L_k=\mathscr B_e/\mathfrak a_k,\qquad
T_{k,N}=L_k/p^NL_k,\qquad
\mathcal O_N=\mathcal O/p^N.
\tag{5}
$$
这里使用的是按阶截断的理想；不把它误写成具有额外权限制的 $u^k\mathscr B_e$。

$L_k$ 是以
$$
b_n=p^{-e_n}u^n,\qquad 0\le n<k
$$
为基的自由 $\mathcal O$ 模，且
$$
b_i b_j=
\begin{cases}
p^{e_{i+j}-e_i-e_j}b_{i+j},&i+j<k,\\
0,&i+j\ge k.
\end{cases}
\tag{6}
$$
(4) 使全部结构常数整。因此 $T_{k,N}$ 是一个确定的有限 $\mathcal O_N$ 代数。

原评价由此给出真正的环同态
$$
j_{k,N}:\mathcal O_N[A,C]\longrightarrow T_{k,N},
\qquad P\longmapsto P(A(u),C(u))\bmod p^N.
\tag{7}
$$
在基 $b_n$ 中，它恰为原矩阵的行
$p^{e_n}[u^n]P$。这一步是后面所有乘法递推的根据。

## 2. 齐次块与原交集

固定次数上界 $D\ge1$，并假设
$$
k>2D.
\tag{8}
$$
记
$$
H_m=\mathcal O_N[A,C]_m,\qquad
E_m=\mathcal O_N[A,C]_{\le m},
$$
$$
I_m=j_{k,N}(H_m),\qquad
S_m=\sum_{a=0}^m I_a=j_{k,N}(E_m).
\tag{9}
$$
对 $m\ge1$，定义同一目标中的实际交集长度
$$
\gamma_m(N;k)=
\operatorname{length}_{\mathcal O}
\bigl(I_m\cap S_{m-1}\bigr).
\tag{10}
$$
设
$$
B_N(m,k)=\operatorname{length}_{\mathcal O}
\ker(j_{k,N}|_{E_m}).
\tag{11}
$$

由 (1)，原齐次单项式的准确像为
$$
A^{m-c}C^c=v_0^c u^{m+c}F^m,\qquad 0\le c\le m.
\tag{12}
$$
在证明单个块的 Smith 形式时，乘 $F^{-m}$ 是整可逆目标运算，因而该块的非零 Smith 指数准确为
$$
e_m,e_{m+1},\ldots,e_{2m}.
$$
定义这部分已付的源损失
$$
\tau_m(N)=\sum_{c=0}^m\min(N,e_{m+c}).
\tag{13}
$$
不同 $m$ 的这些单块核对没有被同时当作整个 mixed 矩阵的一次目标换基。

于是
$$
\operatorname{length}I_m=(m+1)N-\tau_m(N)
$$
及有限模的和、交正合列给
$$
\boxed{\quad
B_N(m,k)-B_N(m-1,k)
=\tau_m(N)+\gamma_m(N;k).
\quad}
\tag{14}
$$
常数块单射，故 $B_N(0,k)=0$。

特别，在后文的大素数主范围
$$
r>2D
\tag{15}
$$
中，全部 $\tau_m=0$，每个 $j_{k,N}|_{H_m}$ 都单射，而且
$$
\boxed{\quad B_N(D,k)=\sum_{m=1}^D\gamma_m(N;k).\quad}
\tag{16}
$$
这里允许整个 mixed 矩阵在特征零下仍有核；不需要预设 $k$ 已超过所有真实跳跃。

## 3. 跨齐次交集就是实际 kernel 的总次数首项理想

固定 (7) 的完整多项式 kernel
$$
\mathcal K_N=\ker j_{k,N}\subset\mathcal O_N[A,C].
\tag{17}
$$
它是原环同态的理想。

对 $m\ge0$，令
$$
\mathcal R_m(N)=
\left\{H\in H_m:
\ \exists\,Q\in E_{m-1},\quad H+Q\in\mathcal K_N\right\},
\tag{18}
$$
其中 $E_{-1}=0$。这是实际关系的最高总次数部分，不要求最高部分的系数是单位。

取最高次部分给出准确正合列
$$
0\longrightarrow\mathcal K_N\cap E_{m-1}
\longrightarrow\mathcal K_N\cap E_m
\longrightarrow\mathcal R_m(N)\longrightarrow0.
\tag{19}
$$
另一方面，
$$
\mathcal R_m(N)=
(j_{k,N}|_{H_m})^{-1}(S_{m-1}),
$$
且存在准确正合列
$$
0\longrightarrow\ker(j_{k,N}|_{H_m})
\longrightarrow\mathcal R_m(N)
\longrightarrow I_m\cap S_{m-1}\longrightarrow0.
\tag{20}
$$
因此
$$
\boxed{\quad
\operatorname{length}\mathcal R_m(N)
=\tau_m(N)+\gamma_m(N;k).
\quad}
\tag{21}
$$

令
$$
\mathcal R(N)=\bigoplus_{m\ge0}\mathcal R_m(N).
\tag{22}
$$
它是 $\mathcal O_N[A,C]$ 的齐次理想，即 $\mathcal K_N$ 的总次数首项理想。确实，若 $H+Q\in\mathcal K_N$，则原环乘法给
$$
A(H+Q),\ C(H+Q)\in\mathcal K_N,
$$
所以
$$
\boxed{\quad
A\mathcal R_m(N)+C\mathcal R_m(N)
\subset\mathcal R_{m+1}(N).
\quad}
\tag{23}
$$
这个递推始终来自原 $A,C$ 的乘法，保留所有低次补偿 $Q$。

在 (15) 中，(20) 的左项为零，故每个 $\mathcal R_m(N)$ 与原交集 $I_m\cap S_{m-1}$ 准确同构。于是整个 $\gamma_m$ 序列是一个实际齐次理想的逐次长度，而不是可独立选择的数字序列。

## 4. 全部 colon 层及二元 shadow

对 $0\le t<N$，定义真正的齐次 $\mathbf F_p[A,C]$ 理想
$$
\mathcal I_{N,t}=
\frac{(\mathcal R(N):p^t)+p\mathcal O_N[A,C]}
     {p\mathcal O_N[A,C]},
\qquad
(\mathcal R(N):p^t)=\{H:p^tH\in\mathcal R(N)\}.
\tag{24}
$$
其中 $N,k$ 始终固定。记
$$
h_{N,t}(m)=\dim_{\mathbf F_p}(\mathcal I_{N,t})_m.
\tag{25}
$$
这些理想满足
$$
\mathcal I_{N,0}\subset\mathcal I_{N,1}
\subset\cdots\subset\mathcal I_{N,N-1}.
\tag{26}
$$

### 4.1. 长度的准确分层

把有限子模 $\mathcal R_m(N)\subset H_m$ 写成 Smith 形式
$$
\mathcal R_m(N)=
\bigoplus_{i=0}^m p^{a_{m,i}}\mathcal O_N e_i,
\qquad 0\le a_{m,i}\le N,
\tag{27}
$$
其中 $a_{m,i}=N$ 表示零分量。这个换基只用于计算长度。

由定义，
$$
h_{N,t}(m)=\#\{i:a_{m,i}\le t\}.
$$
所以
$$
\boxed{\quad
\tau_m(N)+\gamma_m(N;k)
=\operatorname{length}\mathcal R_m(N)
=\sum_{t=0}^{N-1}h_{N,t}(m).
\quad}
\tag{28}
$$
在 (15) 中，左侧就是纯交集 $\gamma_m$。一般范围必须保留 $\tau_m$，不再次把原齐次块的已付权算作跨块收益。

### 4.2. 一个不依赖特征的二元增长引理

若 $0\ne V\subset\mathbf F_p[A,C]_m$ 的维数为 $h$，则
$$
\dim(AV+CV)\ge h+1.
\tag{29}
$$
证明取具有不同首单项式的一组阶梯基。把这些首单项式的 $C$ 指数记为非空集合 $S\subset\{0,\ldots,m\}$。乘 $A$ 与乘 $C$ 分别保留指数 $S$ 和给出 $S+1$。可从二者选出至少
$$
|S\cup(S+1)|\ge |S|+1=h+1
$$
个具有不同首单项式的向量，因而线性独立。这个证明适用于有限域，不使用一般位置、互异节点或阶乘的可逆性。

将 (29) 用于 (24) 的真实理想，得到
$$
\boxed{\quad
h_{N,t}(m)>0
\ \Longrightarrow\
h_{N,t}(m+1)\ge h_{N,t}(m)+1.
\quad}
\tag{30}
$$

令 $a_m$ 为 $\mathcal R_m(N)$ 中非零系数向量的最小公共 $p$ 赋值；若该模为零，令 $a_m=N$。由 (27)，
$$
\#\{t:h_{N,t}(m)>0\}=N-a_m.
\tag{31}
$$
把 (30) 在全部 $t$ 上相加，准确给
$$
\boxed{\quad
\tau_{m+1}+\gamma_{m+1}
\ge \tau_m+\gamma_m+(N-a_m).
\quad}
\tag{32}
$$
因而在 (15) 的原主带，
$$
\boxed{\quad
\gamma_{m+1}(N;k)\ge
\gamma_m(N;k)+(N-a_m).
\quad}
\tag{33}
$$
原跨次数交集不减；一旦某个实际精度层出现，它在每增加一次原总次数时至少增一维。

上述含 $m+1$ 的式子用于 $m+1\le D$。同一原乘法还给 $a_{m+1}\le a_m$。因此对任意 $d\le D$，在主带有
$$
\begin{aligned}
B_N(D,k)\ge{}&
B_N(d-1,k)+(D-d+1)\gamma_d(N;k)\\
&+(N-a_d)\binom{D-d+1}{2}.
\end{aligned}
\tag{34}
$$
这不需要选择不同次数的独立目标坐标。

## 5. 实际首关系次数给出的深度—次数下界

定义
$$
d_{N,t}=
\min\{m:h_{N,t}(m)>0\},
\tag{35}
$$
不存在时记为 $+\infty$。它们是同一实际理想的首关系次数，并满足 $d_{N,t+1}\le d_{N,t}$。由于常数以及原线性块没有交集，当前 $p\ge19,k>2D$ 范围内，有效的首关系次数至少为二。

由 (30)，
$$
h_{N,t}(m)\ge (m-d_{N,t}+1)_+.
\tag{36}
$$
结合 (14)、(21)、(28)，得到全部范围内的原有限源下界
$$
\boxed{\quad
B_N(D,k)\ge
\sum_{t=0}^{N-1}
\binom{D-d_{N,t}+2}{2}_+.
\quad}
\tag{37}
$$
这里右侧一项在 $d_{N,t}\le D$ 时表示
$(D-d_{N,t}+1)(D-d_{N,t}+2)/2$，其余为零。一般 $p,D$ 下若要提取纯 $\sum\gamma_m$，应从已得下界扣除 $\sum_{m\le D}\tau_m$；在 (15) 中不需这一步。

### 5.1. 与 R223 的深 Smith 条件的实际接口

假设在主带中，存在固定 $0<\eta\le1$、$0<\theta<1$，使至少 $\eta N$ 个真实层满足
$$
d_{N,t}\le\theta D.
\tag{38}
$$
则
$$
B_N(D,k)\ge
\eta N\binom{D-\lfloor\theta D\rfloor+2}{2},
\tag{39}
$$
所以若 $M_D=(D+1)(D+2)/2$，
$$
\frac{B_N(D,k)}{NM_D}
\ge\eta(1-\theta)^2+o(1).
\tag{40}
$$
这已经是原矩阵的正比例深层输入。更准确地，若左侧至少为 $c\in(0,1)$，由于每个截断 Smith 指数至多 $N$，至少
$$
\frac{c}{2-c}M_D
$$
个 Smith 指数大于 $cN/2$，取整时只需相应调整端点。这由把其余指数都按 $cN/2$ 上界计入总和直接得到。

在 R223 所定的大素数范围，$B_N$ 与 R218 累计真实 $\iota$ 之间只有已付的 $O(D)$ 差，因此 (38) 会提供该路线所需的正比例深交集。本文没有证明 (38)，也没有把其次数和精度上界当成双完整零的自动后果。

### 5.2. colon 见证不能免费除以 $p^t$

若 $0\ne\overline H\in(\mathcal I_{N,t})_d$，它准确表示存在一个 primitive 齐次提升 $H$ 和一个原低次多项式 $Q$，使
$$
p^tH+Q\in\mathcal K_N,\qquad \deg Q<d.
\tag{41}
$$
只有最高齐次部分已写成 $p^tH$。$Q$ 未必被 $p^t$ 整除，因此不能把 (41) 直接除以 $p^t$ 后仍称为原整关系。

可以做的准确操作如下：将 (41) 提升到 $\mathcal O[A,C]$，令整个多项式 $p^tH+Q$ 的实际公共系数赋值为 $b$。由于 $H$ primitive，有 $0\le b\le t$。只除以这个实际公共内容 $p^b$，得到原 primitive 多项式 $R$，且
$$
\deg R\le d,\qquad J_{<k}(R)\in p^{N-b}L_k
\subset p^{N-t}L_k.
\tag{42}
$$
这是与 R223 单元素乘法输入的合法连接。不同 $t$ 所得见证可能相关；(37) 的累计依靠同一首项理想的长度分层，不假定这些见证彼此独立。

## 6. 同一原矩阵的真实 Hensel 障碍

为明确后续算术需要作用在哪里，仍固定 $k$，但在本节用 $T$ 表示逐次提升的精度。对原整源 $E_D(\mathcal O)$，令
$$
\Lambda_T(D)=\{P:J_{<k}(P)\in p^TL_k\},
$$
$$
\mathcal F_T(D)=
\operatorname{im}\bigl(\Lambda_T(D)\to E_D/pE_D\bigr),
$$
$$
\mathcal V_T(D)=
\left\{p^{-T}J_{<k}(P)\bmod p:
P\in\Lambda_T(D)\right\}\subset L_k/pL_k.
\tag{43}
$$
$T=0$ 时取 $\Lambda_0=E_D$。因为 $p\Lambda_{T-1}\subset\Lambda_T$，有
$$
\mathcal V_{T-1}(D)\subset\mathcal V_T(D).
$$

以下取 $T\ge1$。对 $\overline P\in\mathcal F_T(D)$，选一个实际提升 $P\in\Lambda_T(D)$，定义
$$
\beta_T(\overline P)=
p^{-T}J_{<k}(P)
\pmod{p,\ \mathcal V_{T-1}(D)}.
\tag{44}
$$
若换成另一个提升，两者之差为 $pQ$，且
$Q\in\Lambda_{T-1}(D)$，所以 (44) 良定义。直接按这个差补偿，得到准确正合列
$$
\boxed{\quad
0\longrightarrow\mathcal F_{T+1}(D)
\longrightarrow\mathcal F_T(D)
\xrightarrow{\ \beta_T\ }
\mathcal V_T(D)/\mathcal V_{T-1}(D)
\longrightarrow0.
\quad}
\tag{45}
$$
特别，$\beta_T(\overline P)=0$ 才允许同一个原模 $p$ 向量提升一层；长度不等式本身不保证逐元素提升。

原乘法使 (45) 对 $A,C$ 都相容。例如
$$
\beta_T(A\overline P)
=A\,\beta_T(\overline P)
$$
位于次数 $D+1$ 的相应商中，$C$ 同样成立。这里的右侧乘法正是 (6)–(7) 的原目标乘法。

若 $s_i$ 是原 $J_{<k}|_{E_D}$ 的 Smith 指数，则
$$
\dim\mathcal F_T(D)=\#\{i:s_i\ge T\},\qquad
\dim\bigl(\mathcal V_T/\mathcal V_{T-1}\bigr)
=\#\{i:s_i=T\},
\tag{46}
$$
特征零 kernel 按 $s_i=+\infty$ 计。由此也有
$$
B_N(D,k)=\sum_{T=1}^N\dim\mathcal F_T(D).
\tag{47}
$$
(24) 的 colon 层和 (43) 的提升层使用不同的分层；(28) 与 (47) 都是同一个原长度的准确表达，不能将两者逐项未经证明地认同。

## 7. 双完整中央零尚需给出的原输入

现在已有的正向递推是 (23)、(30)、(33)、(37)。若要把两个原完整中央导数为零用到这条路线，需要证明它们对同一个实际理想给出诸如 (38) 的首关系次数上界，或具体消去 (45) 中的原障碍分量。

R189 的条件行与 R203 的有理 $t_h$ 都保留原数据；其中仅线性的 $t_h$ 已读取原第 $rh$ 行，完整 Hasse 运输还有 R189 的额外输入和精度。在 $p\asymp D^2,\ k=O(D^2)$ 的主带内，同一个 $k$ 直接容纳的这种层数仍只有 $O(1)$。若要取得 $N$ 随 $D$ 增长的 (38)，还需要原径向方程或实际 theta 算术把这些条件作用到当前的首项理想或 Hensel 障碍上。

本篇没有选择可调的未来轴系数，也没有将齐次块各自的整 gauge 当成 mixed 源的共同目标变换。首项理想和 (45) 都由同一个原评价环同态产生。

## 依赖

- [R215：全部原行权与完整整运输](R215-full-depth-faber-transport-and-first-cross-band-carry.md)。
- [R218：真实有限像的全次数交集递归](R218-all-degree-original-image-intersection-recursion.md)。
- [R223：大素数深 Smith 门与原 primitive 产品输入](R223-large-prime-deep-smith-and-original-product-input.md)。
- [R224：同一原径向目标、齐次 Smith 与跨次数交集](R224-radial-image-euler-hasse-observation-and-cross-degree-relations.md)。
- [R189：完整中央 Hasse 族及其读取成本](R189-complete-central-hasse-families-and-weighted-core.md)。
- [R203：全部归一中央方向的原有理表达](R203-finite-central-companion-and-rational-row-lattices.md)。

这些结论是原环、原有限源和真实交集上的整代数。主目标及 (38) 的条件算术输入仍未完成。
