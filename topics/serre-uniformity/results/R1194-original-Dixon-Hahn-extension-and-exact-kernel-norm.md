# R1194：原 Dixon 零谱块的 Hahn 扩大与准确核范数

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126。

## 1. 结论与原对象

保持 [原 Dixon/Hesse 推导](../notes/2026-11-28-original-genus-four-Dixon-Jordan-chain.md)
(J.19)–(J.37) 的曲线、导子、谱参数及边界。令
$$
p=6N+5>37,\qquad \ell=2N+1,\qquad M=4N+2=2\ell.
\tag{1194.1}
$$
本篇给出同一个零谱核向量的显式扩大：
$$
v_j={}_3F_2\left(\begin{matrix}-\ell,\ell+1,-j\\1,-M\end{matrix};1\right),
\qquad 0\le j\le M.
\tag{1194.2}
$$
这里是有限多项式；所有实际分母均为 $p$ 单位。
它在 $0\le j<\ell$ 恰为原来的 $q_j(0)$，并且
$$
\boxed{\quad
\sum_{j=0}^{\ell-1}q_j(0)^2
=-\frac{\ell!}{2(M+1)(M!)^2}\ne0\quad\text{in }\mathbf F_p.
\quad}
\tag{1194.3}
$$
这付清一个新的准确无权范数。原短谱导数则准确读
$$
\sum_{j=0}^{N-1}\frac{q_j(0)^2}{3j+2};
\tag{1194.4}
$$
§6 保留其全部权重和归一。因此本篇不把 (1194.3) 当作原 $K_4$ 单位，
也不据全块的零根简单性关闭原两个指定障碍。

## 2. 从原矩阵逐行得到扩大算子

置 $a_j=3j+2$。原 (J.35) 在 $(\lambda,w)=(0,0)$ 的三条对角线为
$$
\mathcal Q_{j,j}=-2a_j(a_j^2+1),\quad
\mathcal Q_{j,j-1}=a_j(a_j-1)(a_j-2),\quad
\mathcal Q_{j,j+1}=a_j(a_j+1)(a_j+2).
\tag{1194.5}
$$
原范围为 $0\le j<\ell$；其中 $a_j\ne0$。
把第 $j$ 行除以 $9a_j$，并使用
$$
M\equiv-\frac43\pmod p,
$$
得到
$$
\begin{aligned}
B_j&=(j+1)(j-M)=(j+1)(j+4/3),\\
D_j&=j(j-M-1)=j(j+1/3),\\
(\mathscr L f)(j)
&=B_j\{f(j+1)-f(j)\}+D_j\{f(j-1)-f(j)\},\\
\mathscr H&=\mathscr L+2/9.
\end{aligned}
\tag{1194.6}
$$
例如 $B_j+D_j=(2a_j^2+4)/9$，所以对角线确为
$-(B_j+D_j)+2/9=-2(a_j^2+1)/9$。
上下两条对角线也正是 (1194.5) 除以 $9a_j$。

现在把 (1194.6) 定义在全部 $j=0,\ldots,M$ 上。
$D_0=B_M=0$ 给出这次扩大的真实两个端点；不需要越界值。
而
$$
B_j=D_{j+1}\qquad(0\le j<M),
\tag{1194.7}
$$
所以 $\mathscr H$ 是标准坐标内的对称矩阵。
这只是原矩阵在零谱处的逐行归一和扩大；对一般 $\lambda$，
原行归一后的谱项是 $\lambda/(9a_j)$，并不是 $\lambda I$。
尤其不能据此把原幂零谱问题换成 $\mathscr H$ 的普通谱问题。

## 3. 扩大全块的零根恰为简单根

因 $M<p$，次数至多 $M$ 的多项式在 $0,\ldots,M$ 的评价是同构。
直接展开差分可见 $\mathscr L$ 保持次数过滤，且在次数 $n$ 的最高项上
作用为 $n(n+1)$。例如 $B_j-D_j=2j-M$；
二阶差分的最高项再贡献 $n(n-1)$，合为 $n(n+1)$。
故
$$
\det(zI-\mathscr H)
=\prod_{n=0}^M\{z-n(n+1)-2/9\}.
\tag{1194.8}
$$
零特征值要求 $(3n+1)(3n+2)=0$。
两个剩余类的最小非负代表分别是
$$
n=\ell=2N+1,\qquad n=M+1=4N+3.
$$
后者不在 $0\le n\le M$，前者恰出现一次。
因此零根的代数重数与几何重数均为一。
这里不要求其他特征值互异。

还有一个不需范数公式的非零证明：若非零核向量 $v$ 满足
$v^{\mathsf t}v=0$，则由对称性
$v\in(\ker\mathscr H)^\perp=\operatorname{im}\mathscr H$。
于是有 $w$ 使 $\mathscr H w=v$，产生长度至少二的零特征 Jordan 链，
与上述代数重数一矛盾。以下进一步付清范数的准确值。

## 4. 有限多项式、反射及与原核的准确识别

对 $0\le i\le M$ 置
$$
\phi_i(j)=\frac{(-j)_i}{(-M)_i},\qquad \phi_0=1,
$$
其中 $(x)_i$ 是上升阶乘。逐项差分给
$$
\mathscr L\phi_i=i(i+1)\phi_i-i^2\phi_{i-1}
\quad(i\ge1),\qquad \mathscr L\phi_0=0.
\tag{1194.9}
$$
因此对任意整数 $0\le n\le M$，在特征零先定义
$$
V_n(j)=\sum_{i=0}^n
\frac{(-n)_i(n+1)_i}{(i!)^2}\,\phi_i(j).
\tag{1194.10}
$$
相邻系数之比为 $(i-n)(i+n+1)/(i+1)^2$；代入 (1194.9) 即得
$\mathscr L V_n=n(n+1)V_n$，并且 $V_n(0)=1$。
现在取 $n=\ell$ 并模 $p$：
$i!$、$(-M)_i$ 及 $(\ell+1)_\ell$ 所用整数均小于 $p$，
所以这一步合法，次数仍为 $\ell$，且 $v_j=V_\ell(j)$ 是 (1194.2) 的核。

反射 $j\mapsto M-j$ 交换 $B$ 与 $D$，因而与 $\mathscr H$ 交换。
核一维，$V_\ell(M-j)$ 的最高项是 $(-1)^\ell$ 倍；$\ell$ 为奇数，故
$$
v_{M-j}=-v_j,\qquad v_\ell=0.
\tag{1194.11}
$$
原 (J.20) 在 $\lambda=0$，正是
$(\mathscr Hq)(j)=0$ 的同一递推。
起点 $q_0=1=v_0$，左越界系数为零；
在 $0\le j<\ell$，用于递推到 $j+1$ 的 $B_j$ 全部非零。
因此
$$
v_j=q_j(0)\quad(0\le j\le\ell),\qquad q_\ell(0)=0.
\tag{1194.12}
$$
这同时核定了零谱识别和中点边界；没有更换原 $q_N$。

## 5. Rodrigues 与有限求和给出准确范数

为使公式自足，本节先在 $\mathbf Q$ 对整数 $0\le n\le M$ 证明。
用下降阶乘记
$$
R_n(j)=j^{\underline n}(j-M-1)^{\underline n},\qquad
\widetilde V_n(j)=\frac{\Delta^nR_n(j)}{n!(-M)_n},
\quad\Delta f(j)=f(j+1)-f(j).
\tag{1194.13}
$$
$R_n$ 在 $0,\ldots,n-1$ 和 $M+1,\ldots,M+n$ 全为零。
特别 $\Delta^nR_n(0)=R_n(n)=n!(-M)_n$，故
$\widetilde V_n(0)=1$。其次数为 $n$，最高系数为
$$
c_n=\frac{(2n)!}{(n!)^2(-M)_n}.
\tag{1194.14}
$$

展开差分并令 $k=j+i$，两端的零值精确消去全部边界，给出
$$
\sum_{j=0}^M P(j)\Delta^nR_n(j)
=(-1)^n\sum_{k=n}^M R_n(k)\nabla^nP(k),
\quad \nabla P(k)=P(k)-P(k-1).
\tag{1194.15}
$$
因此 $\widetilde V_n$ 与所有次数小于 $n$ 的多项式正交。
由 $\mathscr L$ 的对称性和次数过滤，
$(\mathscr L-n(n+1))\widetilde V_n$ 次数小于 $n$，
同时与全部该次数空间正交；在特征零的有限正定内积下它只能为零。
特征零的 $n(n+1)$ 在 $0,\ldots,M$ 中单重，
再用原点归一即得 $\widetilde V_n=V_n$。
本段的正定性仅用来证明一个特征零多项式身份，
没有对有限域中的原短范数使用正性。

在 (1194.15) 中取 $P=V_n$，有 $\nabla^nV_n=n!c_n$。
另一方面
$$
R_n(k)=(-1)^n(n!)^2
\binom{k}{n}\binom{M+n-k}{n},
$$
而 Vandermonde 求和给
$$
\sum_{k=n}^M\binom{k}{n}\binom{M+n-k}{n}
=\binom{M+n+1}{2n+1}.
$$
后一个身份也可逐个选择大小为 $2n+1$ 的子集，按其中第 $n+1$ 个元素划分，
所以包含了全部两个端点。
代回并使用 $(-M)_n=(-1)^nM!/(M-n)!$，得到
$$
\boxed{\quad
\sum_{j=0}^M V_n(j)^2
=\frac{(M+n+1)!(M-n)!}{(2n+1)(M!)^2}.
\quad}
\tag{1194.16}
$$
现在只在 $n=\ell,\ M=2\ell$ 这一安全位置约化。
因为 $M+n+1=p-1$、$M-n=\ell$，(1194.16) 的所有分母为 $p$ 单位。
Wilson 给
$$
\sum_{j=0}^M v_j^2
=-\frac{\ell!}{(M+1)(M!)^2}\ne0.
\tag{1194.17}
$$
由 (1194.11)，左右两半范数相同，中点贡献零；除以二即为 (1194.3)。
没有把 (1194.16) 在分母或分子越过 $p$ 的其他位置无条件约化。

## 6. 原短谱导数的权重不能删去

假设原第一障碍 $e=0$。由原 (J.26)，这等价于 $q_N(0)=0$。
记原 $N$ 阶左主块为 $Q_N(\lambda)$，
$$
\mathbf q(\lambda)=(q_0(\lambda),\ldots,q_{N-1}(\lambda))^{\mathsf t},
\quad A_N=\operatorname{diag}(3j+2)_{j=0}^{N-1}.
$$
其末行的真实越界项为
$u_{N-1}q_N(\lambda)$，其中
$u_{N-1}=(3N-1)(3N)(3N+1)$；所以
$$
Q_N(\lambda)\mathbf q(\lambda)
=-u_{N-1}q_N(\lambda)e_{N-1}.
\tag{1194.18}
$$
矩阵 $A_N^{-1}Q_N(0)$ 对称，
故 $\mathbf q(0)^{\mathsf t}A_N^{-1}$ 是左核向量。
对 (1194.18) 在零处求导，再乘这个左核向量，得到准确身份
$$
\boxed{\quad
\sum_{j=0}^{N-1}\frac{q_j(0)^2}{3j+2}
=-(3N)(3N+1)q_{N-1}(0)q_N'(0).
\quad}
\tag{1194.19}
$$
$q_{N-1}(0)\ne0$：否则与 $q_N(0)=0$ 一起沿非零三项系数反推，
会给 $q_0(0)=0$。其余显示因子也全是单位。
因此在 $e=0$ 下，原第二障碍的消失准确等价于 (1194.19) 左边为零。
与原符号的连接仍是 (J.27)：
$$
q_N'(0)=\frac{\delta}{6\Gamma}\nu_k,
\quad k=N+1,\quad\Gamma=(2v)^{2k},
\quad K_4=-\frac{\delta^3}{4v^2}\nu_k.
\tag{1194.20}
$$
这里 $v$ 是原 Weierstrass 常数；不与本篇带指标的 $v_j$ 混同。

(1194.3) 的无权和有 $\ell$ 项，(1194.19) 的带权和只有 $N$ 项。
原完整 Hesse 正常导数又另含 $A_N^2$，见 (J.37)。
三者各有实际来源，当前没有证明它们可相互替代。

## 7. 第一障碍下的四段与明确剩余问题

把 $V_\ell(j)$ 写成变量 $a=3j+2$ 的多项式 $P(a)$。
反射 (1194.11) 成为 $P(-a)=-P(a)$，故 $P$ 为奇多项式。
而 $j=N$ 对应 $a=(p-1)/2=-1/2$。
因此
$$
e=0\quad\Longrightarrow\quad a(a^2-1/4)\mid P(a).
\tag{1194.21}
$$
扩大核在 $j=N,\ell,3N+2$ 三处为零，余下四段各有 $N$ 个点：
$$
[0,N-1],\quad[N+1,2N],\quad[2N+2,3N+1],\quad[3N+3,4N+2].
$$
反射只把外两段、内两段分别配对；它保持平方而把 $a$ 变成 $-a$。
故不能利用该反射删掉 (1194.19) 的 $1/a$ 权重。
当前可继续的精确问题是：在同一原多项式、真实切点和完整递推下，
能否把 (1194.19) 的消失送到与 (1194.3) 冲突的等式，
或由同一实际来源给出另一项横截单位。
原 $e,K_4$ 共同非零和课题主要完成标准均仍开放。

## 8. 核定与范围

所有矩阵、分母、两端差分、范数和短谱归一均在文中证明。
o1_theta 独立纸核了逐行扩大、反射、唯一零根与 Rodrigues 范数常数；
root 按原 (J.20)、(J.35)–(J.37) 核对了对象和谱权重。
没有运行数学程序、增加素数窗口或重做已登记的 Hesse 全行列式。
本篇新增的是原零谱核的 Hahn 扩大与准确无权范数，
不是有限域上的一般正交多项式简单根论断。
