# R273 出生二：固定整数源与八维完整逆的多项式表示

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态。** 以下全参数身份已证明；尚未证明四维首边的相邻矩阵序。本文是[共同低阶矩规范稿](R273-appendix-shared-low-moment-normal-form-and-physical-cubic-bridge.md)的另一种完整逆表示。它不引入试探原像，不压缩后才求逆，也不把坐标变换后的普通转置冒充物理伴随。

## 1. 去权后聚合坐标及其真实 Hilbert 度量

沿用 [R273](R273-two-exceptional-weights-complete-schur-recovery.md)：两个普通组为 $(q,a)$、$(L,1)$，两个异常位为 $u,v$，
$$
z=a^2,\quad w_1=u^2,\quad w_2=v^2,\qquad q,L\ge2.
$$
相对出生固定为二，合法高度为 $0\le n\le h=q+L-2$。在任意层 $k$，合法占据写作
$$
I=(r,b,c,\ell),\quad r+b+c+\ell=k,\quad
0\le r\le q,\quad b,c\in\{0,1\},\quad0\le\ell\le L.
$$
原坐标 $f_I$ 是每个同类具体物理集合的共同振幅。记
$$
c_I=\binom qr\binom L\ell,
\qquad \rho_I=a^ru^bv^c,
\qquad p_I=c_I\rho_I^2.
$$
在每层作可逆坐标变换
$$
g_I=c_I\rho_I f_I.
\tag{1.1}
$$
则原物理范数准确为
$$
\|f\|^2=\sum_Ic_I|f_I|^2
=\sum_I\frac{|g_I|^2}{p_I}.
\tag{1.2}
$$
特别，$g$ 坐标的度量是 $P_k^{-1}=\operatorname{diag}(p_I^{-1})$，不是单位矩阵。

从第 $n+2$ 层到第二层，$D^n/n!$ 在 $g$ 坐标中的矩阵恰为
$$
(B_n)_{O,I}=\prod_{j=1}^4\binom{I_j}{O_j},
\qquad |O|=2,\quad |I|=n+2.
\tag{1.3}
$$
非法包含关系对应零值。证明只用原 incidence 公式及
$$
\binom{m}{o}\binom{m-o}{i-o}
=\binom{m}{i}\binom{i}{o}.
$$
原权因子由 $\rho_I/\rho_O$ 恰消；每个普通组的组合数也恰按此身份消去。式 (1.3) 同时等于多项式算子
$(\partial_x+\partial_y+\partial_z+\partial_t)^n/n!$ 的系数矩阵，因此归一化中的 $n!$ 已包含。

## 2. 所有高度共用的四维整数源

第二层的八个占据按如下次序排列：
$$
\mathcal O=((0,0,0,2),(0,0,1,1),(0,1,0,1),(0,1,1,0),
(1,0,0,1),(1,0,1,0),(1,1,0,0),(2,0,0,0)).
$$
令 $E$ 的四列为以下多项式在这个单项式顺序中的系数：
$$
(x-t)^2,\qquad (x-t)(y-t),\qquad
(x-t)(z-t),\qquad (y-t)(z-t).
\tag{2.1}
$$
即
$$
\boxed{
E=\begin{pmatrix}
1&1&1&1\\
0&0&-1&-1\\
0&-1&0&-1\\
0&0&0&1\\
-2&-1&-1&0\\
0&0&1&0\\
0&1&0&0\\
1&0&0&0
\end{pmatrix}.}
\tag{2.2}
$$
四列均被 $\partial_x+\partial_y+\partial_z+\partial_t$ 消去，并由 $x^2,xy,xz,yz$ 的系数直接看出独立。二层允许的八维多项式空间被这个导数满射到一层四维空间：$x^2,t^2,xy,xz$ 的导数已张成 $x,y,z,t$。因此 (2.2) 正好参数化整个相对出生二 primitive 块。

它与 $q,L,z,w_1,w_2$ 无关，也不随高度 $n$ 变化。原物理源是
$$
E_{\rm phys}=\operatorname{diag}((c_O\rho_O)^{-1})E.
\tag{2.3}
$$
这仍是一个非正交物理源；其准确 Gram 将在 (3.3) 保留。

## 3. 八维完整逆的纯多项式矩阵

对合法输入占据 $I$，记列向量
$$
(v_I)_O=\prod_{j=1}^4\binom{I_j}{O_j}.
$$
由 (1.2)–(1.3)，完整最小化为
$$
\min\left\{g^*P_{n+2}^{-1}g:B_ng=E\xi\right\}.
$$
故定义
$$
\boxed{
\mathcal F_n=B_nP_{n+2}B_n^*
=\sum_{\substack{I=(r,b,c,\ell)\text{ legal}\\|I|=n+2}}
\binom qr\binom L\ell z^r w_1^bw_2^c\,v_Iv_I^* .}
\tag{3.1}
$$
在全部合法高度，先在完整八维物理固定块取逆，得到
$$
\boxed{\mathcal H_n=E^*\mathcal F_n^{-1}E.}
\tag{3.2}
$$
$D^n$ 的满射性及组内置换平均保证 $B_n$ 满行秩，所以 $\mathcal F_n>0$。组内置换固定块同时约化实际 $D,D^*$；对固定源，先在原 Boolean 空间作完整逆再限制，得到的正是此八维块的完整逆。因此 (3.2) 没有丢失其他原像方向可能产生的能量降低。

首层准确为
$$
\mathcal F_0=P_2,
\qquad
\boxed{\mathcal H_0=E^*P_2^{-1}E.}
\tag{3.3}
$$
一般相邻比较以及本稿首边分别等价于
$$
\mathcal H_n\mathcal H_{n+1}^{-1}\mathcal H_n\prec\mathcal H_{n-1},
\qquad
\mathcal H_2-\mathcal H_1\mathcal H_0^{-1}\mathcal H_1>0.
\tag{3.4}
$$
(3.4) 是待证式，不是 (3.1) 的已证推论。

所有硬端已包含于合法占据及完整 $B_n$ 中。特别 $q=L=2$ 的 $n=2=h$ 是实际顶端；本表示仍使用其合法输入和完整逆，不从内部自由 nuisance 的式子外推该端点。

### 3.1 与 R273 原源的准确共同关系

令 R273 原四维源顺序为 $(\alpha,\beta,\gamma,\delta)$，并置
$$
T=\begin{pmatrix}
0&0&0&1/2\\
0&0&1&0\\
0&1&0&0\\
1&0&0&0
\end{pmatrix},\qquad C_q=(q!)^2z^q.
$$
将 R273 (1.2) 的源逐项作 (1.1)，由 $d=q$ 和八个合法占据直接得到
$$
E_{{\rm old},\,g}=q!a^quv\,ET.
$$
例如八个行多项式除去 $q!a^quv$ 后依次为
$$
\alpha+\beta+\gamma+\delta/2,\quad
-\alpha-\beta,\quad-\alpha-\gamma,\quad\alpha,
$$
$$
-\beta-\gamma-\delta,\quad\beta,\quad\gamma,\quad\delta/2.
$$
故所有高度准确有
$$
\boxed{H_n^{\rm R273}=C_qw_1w_2\,T^*\mathcal H_nT.}
\tag{3.5}
$$
这里 $T$ 是同一个常数可逆矩阵，前面正因子也与高度无关。这给 (3.4) 与 R273 原目标的完整同源等价，并支付新旧非正交源度量。

## 4. 精确移除每行计数权，不丢失物理度量

(3.1) 的第 $O$ 行有共同因子
$$
p_O=\binom q{O_1}\binom L{O_4}z^{O_1}w_1^{O_2}w_2^{O_3}.
$$
写
$$
\mathcal F_n=P_2G_n.
\tag{4.1}
$$
再次使用组合数身份，直接给纯多项式项
$$
(G_n)_{O,O'}=
\sum_{\substack{K\ge0,\ |K|=n\\O+K\text{ legal}}}
\left[\prod_{j=1}^4\binom{m_j-O_j}{K_j}\right]
z^{K_1}w_1^{K_2}w_2^{K_3}
\left[\prod_{j=1}^4\binom{O_j+K_j}{O'_j}\right],
\tag{4.2}
$$
其中 $(m_1,m_2,m_3,m_4)=(q,1,1,L)$。因此按 $(q,L,z,w_1,w_2)$ 的总次数，$G_n$ 至多为 $2n$，$G_0=I$。

**$G_n$ 通常不是 Hermitian 矩阵。** 实际自伴关系是
$$
G_n^*P_2=P_2G_n,
$$
而正确逆公式为
$$
\boxed{\mathcal H_n=E^*G_n^{-1}P_2^{-1}E.}
\tag{4.3}
$$
程序中的右端始终保留 $P_2^{-1}E$。它没有用 $E^*G_n^{-1}E$ 替代物理形式，也没有用普通对称消元冒充伴随。

实际可先取全部 $p_O$ 的正公共倍数 $M$，解
$$
G_nY=M P_2^{-1}E,
\qquad \mathcal H_n=M^{-1}E^*Y.
\tag{4.4}
$$
右端于是为多项式。所有前导主元非零，因为相应主子式为 $\mathcal F_n$ 的正主子式除以正的 $p_O$ 乘积。逐步 fraction-free 消元中的除法必须核余数严格为零。

## 5. 首边的精确参数域及分母正性

对未含短组边界的 $q,L\ge3$，交换普通组并整体缩放、再交换两个异常位后，可设
$$
q=3+Q,\quad L=3+R,\quad z=1+Z,
\quad w_1=U+V,\quad w_2=V,
\tag{5.1}
$$
其中 $Q,R$ 为非负整数，$Z,U\ge0,V>0$。首边只用 $n=0,1,2$；(3.1) 中全部组合数次数至多四，所以这些组合数在 (5.1) 的变量中都有非负系数。各列权也有非负系数。

因而 Cauchy–Binet 直接给 $\det\mathcal F_n$ 及它的任一非空主子式为非负系数多项式。事实上这些分母在更大的实域 $Q,R,Z,U\ge0,V>0$ 上也严格正：当 $Q=R=Z=U=0$ 时，仍是 $q=L=3$、普通权一、异常权平方 $V$ 的合法正定有限模型；增大上述非负变量只在 (3.1) 增加正半定项。

由 (4.1)，$\det G_n=\det\mathcal F_n/\det P_2>0$，公共倍数 $M$ 也正。最后若比较 $\mathcal H_2-\mathcal H_1\mathcal H_0^{-1}\mathcal H_1$，还会出现已正定的 $\mathcal H_0$ 的正行列式。因此整个相邻差的有理生成链有明确不为零的实际分母。约分后的分母仍是这些非零因子的约因子，其符号可由连通域上的一个内点确定。

这只支付证书中清分母和取逆的合法性，没有证明相邻差分子的正性。$q=2$ 或 $L=2$ 时，(3.1)–(4.4) 仍是准确完整式，但不能将 (5.1) 的非负系数域直接扩展过去。

## 6. 已执行核对及仍未完成的证书

[生成器](../notes/2026-11-14-two-exceptional-aggregate-polynomial-789f-next.py)用两条独立实现核对 $(q,L,a,u,v)=(3,4,2,3,5)$、$n=0,1,2$：一条直接用原物理 incidence 和组合数 Hilbert 度量求完整层逆；另一条用 (3.1)、(4.4) 的纯多项式核和固定整数源。全部矩阵逐项相等，且源直接被原 $D$ 消去。此核对只检查实现，不作为全参数正性证据。

消元器使用精确有理多项式，逐除法计算余数并要求为零。一次有界资源剖面中，完整 $n=1$ 的八个主元和四维形式在约九秒完成；没有据此声称 $n=2$ 或四个首主子式已算完。

主程序随后尝试生成 (3.4) 的四个前导主子式；只有每个主子式的正确符号分子均为非负系数、并保留一个在 $Q=R=Z=U=0,V>0$ 仍严格正的项，才报告该判据通过。任何负系数只记录为此判据未闭，不能当作实际反例。当前没有完成这样的全参数证书。
