# R369：原有限 theta frame、真实六十八阶移位与共同 forcing 的高尾原始性

日期：2026-11-13。**状态：以下原 regularized theta 的完整低窗有理代表、其与正规局部单位连接之间的显式全局差，以及两个真次数二乘子的六十八阶物理移位和共同高尾 forcing 的整原始性均已证明。前十一列是实际消失列；余下列使用同一个 forcing 和 R366 的固定整 Bézout 证书。没有以局部单位变换删除 $Z_p^{68}$，也没有把有限原点 jet 相同自动解释为所有非原点留数为零。**

## 1. 对真实 $\zeta$ 原函数再作有限 primitive

沿 R356、R363 取
$
p=6s-1,\quad s>13,\quad b=17,\quad
E_b:y^2=x^3+b,\quad D=D_z,\quad DZ=1,\quad D^p=0.
$
$Z=Z_p=\overline{\mathscr R_p/y^p}$ 是原有理参数。
采用 sigma 规范
$
\zeta_\sigma=\zeta-\frac{(p+1)\kappa_\sigma}{34}z^p,
\qquad
G_\sigma=\sum_{i=0}^{p-2}
\frac{(-1)^iZ^{i+1}D^i(-x)}{(i+1)!}.
$
R356 已付
$
G_\sigma\equiv\zeta_\sigma\pmod{p,z^{5p-2}},
\quad DG_\sigma=-x+c_pZ^{p-1},
\quad G_\sigma(P)=0
$
于全部原非原点测试点 $P$。

定义一个新的、完全指定的有理函数
$
\boxed{
H_\sigma=
\sum_{i=0}^{p-2}
\frac{(-1)^iZ^{i+1}D^iG_\sigma}{(i+1)!}.
}
\tag{1}
$
其阶乘仍全为单位。有限求导恒等式给
$
DH_\sigma=G_\sigma+Z^{p-1}D^{p-1}G_\sigma.
$

置
$
\boxed{
\chi_p=\frac1Z+Z^{p-1}D^{p-1}G_\sigma.
}
\tag{2}
$
则完整的全局等式是
$
\boxed{DH_\sigma=G_\sigma-\frac1Z+\chi_p.}
\tag{3}
$
不能先删除 (2)，再将 (1) 当成 $G_\sigma$ 的全局对数原函数。

## 2. 原点归一、真实低窗和全局非零 frame 差

**定理1。** $H_\sigma$ 在 $O$ 正规，常数为零；且
$
\boxed{
H_\sigma\equiv
\log(\sigma/z)-\frac{\kappa_\sigma}{34}w^s
\pmod{p,w^{5s-1}},\qquad w=z^6.
}
\tag{4}
$
与此同时，
$
\boxed{
\chi_p\,dz=O(Z^{6p-1})\,dZ\quad\text{于 }O,\qquad
\operatorname{Res}_{P}(\chi_p\,dz)=1
}
\tag{5}
$
于每个真正的非原点测试点 $Z(P)=0$。

**证明。** 在 $O$ 用实际局部参数 $Z$。
$G_\sigma=Z^{-1}+\cdots$，其型为 $-1$。
(1) 的每一项在 $O$ 至多为常数，常数和准确为
$
\sum_{j=1}^{p-1}\frac1j=0\quad\text{于 }k.
$
故 $H_\sigma$ 正规且常数为零，型为零，至少从 $Z^6$ 起。

由型 $-1$，$G_\sigma$ 的幂指数都同余于 $-1\pmod6$。
$D^{p-1}$ 只保留指数同余于 $p-1\pmod p$ 的项。
除主部 $Z^{-1}$ 外，第一个可能同时满足两条件的指数是 $6p-1$。
因此
$
D^{p-1}G_\sigma=-Z^{-p}+O(Z^{5p}),
$
代入 (2) 给 (5) 的原点阶。
在非原点测试点，$G_\sigma$ 及其导数都正规，
故 (2) 的第一项是唯一简单极，且 $DZ=1$，其残数准确为一。

R342 的 $Z\equiv z\pmod{p,u^{5p}}$ 给
$1/Z-1/z=O(z^{5p-2})$。
配合 R356 的 $G_\sigma$ 比较和 (3)，两边在 (4) 中的导数之差
至少为 $z^{5p-2}$。
原点常数都为零；型为零的导数零项必须是 $z^{mp}$ 且 $6\mid m$，
第一个是 $z^{6p}$，不在窗口中。
故 (4) 成立。相关对数在这一窗口整：
$\zeta_\sigma$ 的唯一首 $p$ 分母已在 R356 支付，
再积分的指数在 $6p$ 之前不产生新的 $p$ 分母。$\square$

(5) 给出一个实际的全局差：它在整个原三块窗口及其有限对偶中不可见，
而在指定测试极的残数非零。
这说明后续全局配对必须使用完整的 (3)，不能仅凭原点 jet 匹配删除它。

若 $\kappa=\kappa_\sigma+\Delta$，R356 的准确修正为
$
G_\kappa=G_\sigma-\bar\delta_\kappa Z^p,\qquad
\delta_\kappa=(p+1)\Delta/34.
$
相应
$
\boxed{
H_\kappa=H_\sigma-\bar\delta_\kappa Z^{p+1},\qquad
DH_\kappa=G_\kappa-\frac1Z+\chi_p.
}
\tag{6}
$
这里 $\chi_p$ 完全不变；
(4) 只按同一 Gaussian 重分解改为
$\log(\sigma/z)-\kappa w^s/34$。
所有小于 $p$ 的非原点局部 jets 也不变。

## 3. 原 regularized theta 的明确有理代表

令
$
E_{p-1}(u)=\sum_{j=0}^{p-1}u^j/j!,
\quad
\mathcal T_\kappa=
(Z^2x)\,E_{p-1}(2H_\kappa).
$
这是 $k(E_b)$ 中的真实有理函数。
对每个非负整数 $N$，置 $m=34N$，定义
$
\boxed{
\mathcal G_{N,\kappa,p}
=Z^{m}x^{m/2}(1+8t)^N E_{p-1}(mH_\kappa).
}
\tag{7}
$
它在 $O$ 为一。
由 (4)、$Z^2x\equiv z^2x\pmod{p,w^{5s-1}}$，准确得到
$
\boxed{
\mathcal G_{N,\kappa,p}
\equiv g_\kappa(w)^N
\pmod{p,w^{5s-1}},
\qquad
g_\kappa=e^{-\kappa w^s}\Theta^{17}(1+8t).
}
\tag{8}
$
这里指数截尾确已支付：
$H_\kappa$ 从 $w$ 起，而 $5s-1<p$，
所以所需所有指数系数的阶乘小于 $p$；
从第 $p$ 项起的截尾只在 $w^p$ 之后参与。
同样，有限指数的乘积与 $E_{p-1}(mH_\kappa)$ 在该窗口相同。

原物理来源并非只有 (7)：
在完整三块目标中还必须乘回
$
\boxed{e_2(Na_\kappa\epsilon),\qquad w^s=p\epsilon,\qquad\epsilon^3=0.}
\tag{9}
$
式 (8) 识别的是 ordinary regularized 系数。
没有把 $\epsilon$ 当作全局曲线上一个可以除以 $p$ 求值的函数。

完整全局连接差也可直接写出。模 $p$ 时
$E_{p-1}'(u)=E_{p-1}(u)+u^{p-1}$，所以
$
\boxed{
D\log\mathcal G_{N,\kappa,p}
=mG_\kappa+\frac m2\,D\log x+N D\log(1+8t)
+m\chi_p+
m(DH_\kappa)\frac{(mH_\kappa)^{p-1}}{E_{p-1}(mH_\kappa)}.
}
\tag{10}
$
最后一项在 $O$ 至少从 $Z^{6p-1}$ 起；
在每个测试点因 $H_\kappa=O(Z^2)$，至少从 $Z^{2p-1}$ 起。
它在其他全局零点的分母仍须保留。
(10) 的 $m\chi_p$ 在测试点有残数 $m$，
恰记录 (7) 的 $Z^m$ 零阶。
因此 (7) 与正规单位局部解的关系不是行单位变换。

## 4. 两个真次数二乘子的完整 $Z^{68}$ 因子

采用 R366 的两个真实归一化乘子
$
Q_0=\rho^2\frac{t(t-1)h_7}{1+8t}
=\Theta^{34}F_0(t),\qquad
Q_1=tQ_0=\Theta^{34}F_1(t),
$
$
F_0=t(t-1)(1+8t)h_7,\qquad F_1=t^2(t-1)(1+8t)h_7.
\tag{11}
$
其 regularized 原低窗代表准确是
$
\boxed{
\mathcal Q_{i,\kappa,p}
=Z^{68}x^{34}F_i(t)E_{p-1}(68H_\kappa),\qquad i=0,1.
}
\tag{12}
$
它们分别匹配 $g_\kappa^2t(t-1)h_7/(1+8t)$
和其乘 $t$ 的实际原低窗。
完整物理乘法仍保留共同的 $e_2(2a_\kappa\epsilon)$。

在一个真正测试点 $P$，取
$
h_{68,P}
=\exp\!\left(68\int_0^Z G_\kappa\,dZ\right)
$
的小于 $p$ 的正规 jets。
由 (6)，$H_\kappa(P)=DH_\kappa(P)=0$，
并且 (6) 中多出的 $Z^{p-1}D^{p-1}G_\kappa$
只在局部第 $p$ 阶积分共振参与。
所以
$
E_{p-1}(68H_\kappa)\equiv h_{68,P}\pmod{Z^p}.
\tag{13}
$
(12) 因而是
$Z^{68}$ 乘 R366 的正规单位局部权及全部角因子；
这个非单位因子不能删去。

对同一个 forcing
$
\omega_{\boldsymbol q}=
\sum_{n=1}^Kq_nZ^{-6n}\,d\log r,\qquad d\log r=-6v\,dz,\quad x=v^2,
$
实际模型的留数阶变成
$
\boxed{N_n=6n-69.}
\tag{14}
$
故 $n\le11$ 的全部列准确为零；
$n=12$ 从第3阶导数开始。
这一消失是在原有限模型中真实发生的，不是删去低行的记号选择。

## 5. 真移位后的完整多项式矩阵

以下取 $12\le K\le s-2$，并记
$
K'=K-11,\qquad j=n-11,\qquad N_j=6j-3,\qquad
\xi=b/v^6=-t,\qquad Y/b=y/v^3.
$
所有 $N_j$ 都小于 $p$，所需局部阶乘均为单位。

为完整定义系数，沿 R366 令 $g$ 为形式变量，且 $Dg=0$；
用 $D-x\partial_g+mg$ 计算实际 $DG_\kappa=-x$ 的小于 $p$ jets。
对任意奇整数 $N<p$，定义
$
\boxed{
A_N^{m,A}(\xi)
=\frac{v^{-A}}{N!\,y v^{N-2}}
 \left.(D-x\partial_g+mg)^N v^{A+1}\right|_{g=0}.
}
\tag{15}
$
它是 $\xi$ 的多项式，且
$
\deg A_N^{m,A}\le(N-1)/2,\qquad
A_N^{m,A}(0)=[u^N](1-u)^{m-A-1}e^{mu}.
\tag{16}
$
这个界也适用于显示的负 $A$。
一个直接的全参数证明是置
$\theta=y/v^3,\ \gamma=g/v$，则
$
Dv=v^2\theta,\quad D\xi=-6v\xi\theta,\quad
D\theta=-3v\xi,\quad D\gamma=v(-1-\gamma\theta),
\quad\theta^2=1+\xi .
$
给 $\xi,\theta,\gamma$ 分别赋 filtration weight $2,1,1$；
每次显示算子最多增加一，
在 $\gamma=0$ 的奇阶结果中提取 $\theta$ 后就得到 (16) 的次数界。
退化到 $\xi=0$ 时，准确局部解给第二式。

写 $e_0=1,e_1=2$ 及
$F_i=\sum_{d=e_i}^{e_i+4}c_{i,d}t^d$；
两个最低系数都为 $-7$。
定义真实移位多项式
$
\widehat A_{i,j}(\xi)
=\sum_{d=e_i}^{e_i+4}c_{i,d}(-1)^d
 \xi^{d-e_i}A_{N_j}^{68,68-6d}(\xi).
$
则
$
\boxed{\deg\widehat A_{i,j}\le3j+2.}
\tag{17}
$

在每个测试点除去共同的有限 étale 行单位 $v(P)^{68}$，
实际模型的两个残数准确为
$
\boxed{
\frac{\operatorname{Res}_P(\mathcal Q_{i,\kappa,p}\omega_{\boldsymbol q})}
     {v(P)^{68}}
=-6(Y/b)v(P)^{-2}\xi^{e_i-K'}\,
 \mathcal P_{i,\boldsymbol q}(\xi),
}
$
$
\boxed{
\mathcal P_{i,\boldsymbol q}
=\sum_{j=1}^{K'}q_{j+11}b^j\xi^{K'-j}\widehat A_{i,j}(\xi),
\qquad
\deg\mathcal P_{i,\boldsymbol q}\le3K'+2.
}
\tag{18}
$
这里的 $v(P)^{-2}=1/x(P)$ 是实际单位，所有角因子仍在
$\widehat A_{i,j}$ 中。
没有删掉 $F_i(P)=0$ 的测试分量。

为核定幂次，单项 $v^{69-6d}$ 的第 $N_j=6j-3$ 阶导数
带因子
$
(y/v^3)v^{69-6d+N_j};
$
除 $v(P)^{68}$，再乘 $(-b)^d$，
恰变为
$(Y/b)v(P)^{-2}(-1)^db^j\xi^{d-j}$。
这支付了从 $q_{j+11}$ 到 (18) 的真实负幂，没有沿用未移位的 $q_j$。

## 6. 同一 forcing 高尾的原始整单射

沿 R366 用其整数 Charlier 多项式
$
P_r(N)=68^r\sum_{a=0}^{r}
 (-1)^a\binom ra\frac{(N)_a}{68^a}.
$
现在代入的是 $N_j=6j-3$，而非未移位的 $6j-1$。
仍准确有
$
\widehat A_{0,j}(0)
=7\frac{68^{N_j-5}}{N_j!}P_5(N_j),\qquad
\widehat A_{1,j}(0)
=-7\frac{68^{N_j-11}}{N_j!}P_{11}(N_j).
\tag{19}
$
因为指数 $68-(69-6e_i)=6e_i-1$ 未被物理移位改变，
故仍是同一对 $P_5,P_{11}$。

R366 已给完整整数恒等式
$
U(N)P_5(N)+V(N)P_{11}(N)=C,
$
$
C=57898118088659915362886263937901527040\ne0.
\tag{20}
$
完整数组及有限 BigInt 证书已在该结果中发表。

**定理2。** 假设原好位条件、$p>83$ 以及 $p\nmid bC$。
两个真正移位的联合局部留数矩阵，对同一 forcing 的
$
\boxed{(q_{12},q_{13},\ldots,q_K)}
$
有一个 $K-11$ 阶单位子式。
其整像是 $p$-饱和的；完整 $K$ 列的核准确是前十一列的张成空间。

**证明。** 原测试代数是 R346 的
$\mathcal O[\xi]/\mathscr B_p(\xi)$，其约化平方自由、次数 $3s-1$，
且 $\xi,1+\xi,Y,v$ 在全部显示测试点为单位。
(18) 的公因子因此都是已付整行单位。

因为 $K'\le s-13$，
$
3K'+2\le3s-37<3s-1.
$
所以 (18) 不在模 $B_p$ 后回绕到低系数行。
对第 $j$ 列，其最低可能行是 $K'-j$，
两个候选对角是 $b^j\widehat A_{i,j}(0)$。
(20) 保证至少一项为单位。
对每个 $j$ 选取该块的对应行，得到一个单位三角子式。

特征零提升使用同一真实有限 étale 测试格和正规单位局部 jets。
所有留数阶 $6n-68$ 小于 $p$，故全部局部导数分母为单位。
任何与 (12)、(13) 相容的整提升都具有这个同一模 $p$ 子式，
于是该高尾图有整左逆。
前十一列由于 $Z^{68}$ 的真实零阶，在整局部模型中也精确为零。
因此核和原始性均如所述。$\square$

原 R342 的 $K=s-14$ 落在显示范围；
当高尾非空时，它保留全部 $K-11$ 个高 forcing 方向。
这里只付一个固定十一维损失，不把它视作完整原目标中可以删除的来源行。

## 7. 与原 $K_2/C_2$ 配对的准确接口

R366 已付两个真正乘法图、所有 $K_r,\beta_1,d_2$ 的自然性，
以及同一个混合次数 $P$ 上的
$
(\mathcal E+40)(PQ_i)=Q_i(\mathcal E+42)P.
$
R338/R366 的实际接触恒等式仍为
$
\mathcal D(PQ_i)=Q_{i,\rm phys}\,\mathcal D(P)\pmod p .
$
共同 Gaussian 的 $e_2(2a_\kappa\epsilon)$ 包含在
$Q_{i,\rm phys}$ 中，不能在传到 (18) 之前删去。
式 (18) 的两个局部矩阵使用指定的同一个 $\boldsymbol q$；
没有为两个乘子重新选择两个独立向量。
这尚不是两个原 double-Euler 转置已经保持此权的证明。
准确地，令 $\mathsf E=6w\partial_w$、
$\mathcal L=\mathsf E(\mathsf E-1)$、$d_n=6n(6n+1)$，
对原接触乘子 $v_i(w)$，真实拉回是
$
q_i=\mathcal L^{-1}\operatorname{pp}(v_i\mathcal Lq),
\qquad
(q_i)_n=d_n^{-1}\sum_k(v_i)_k d_{n+k}q_{n+k}.
$
所以必须保留 $\mathcal L$ 与 $v_i$ 的交换差及所有末行，
不能从 $\mathcal D(PQ_i)=Q_{i,\rm phys}\mathcal D(P)$
直接将 $q_i$ 认作 $v_iq$。完整固定边界和此转置见 R372。

本篇补上的，是原 finite theta 模型确实带 $Z^{68}$，
以及保留这一因子后 (18)–(20) 仍给完整高尾的原始单射。
R363 的完整二阶有理连接系数和 R365 的总 charge 算子继续使用；
公共 $G_0/U_0$、$P_{134}$、$Z^{-78}$ 和十三行仍须按原定义保留。

(3)、(5)、(10) 则精确记录从原点 finite jet 到全局测试极时的 frame 差。
尤其 $\chi_p dz$ 在原窗口不可见却在每个测试极残数为一，
所以仅有 finite-jet 代表相等，不足以证明两个完整
off-pole residual 都为零。
后续必须把这个已明确的差与同一 $P,\mathcal E+42$、
真实可提升左核及完整 Gaussian 块一起代入。
本篇没有假定这个剩余全局零传播已经成立。

原中央失败仍是完整聚合，未增加逐权或逐次数的新零条件。
本篇全为参数证明；没有扫描目标素数。

## 依赖

- R342：原有限 Mellin/残数与全部 Gaussian 重标。
- R346：真正有限 étale 测试代数及整留数坐标。
- R351、R356、R363：原整左核、规范 primitive 及二阶有理连接。
- R365：整个原 carrier 和总 charge 转置。
- [R366](R366-original-two-degree-two-multipliers-and-joint-local-residue-primitivity.md)：
  两个真正乘子、同一 forcing 的整自然性及整数 Bézout 证书。

文件通过已授权的 GitHub API 保存；核心同步记录由根代理维护。
