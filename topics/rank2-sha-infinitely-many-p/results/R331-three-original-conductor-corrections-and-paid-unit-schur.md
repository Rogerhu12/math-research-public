# R331：三条原导子修正、两条常数障碍的真实消去与完整单位 Schur 块

日期：2026-11-13。**状态：以下 primitive 原来源扩张、完整物理目标中的运输、三条修正的准确系数及所有精度的单位 Schur 化均已证明。原单乘子归一化像的两条常数障碍，可以由已有的三条原导子列实际支付；修正后其余高行仍完整保留。没有给这些导子或乘积另加中央零条件，尚未证明余下深关系足以完成主目标。**

## 1. 原来源、完整目标与三个已付乘子

沿 R322、R326、R328，取
$$
b=17,\quad p=6s-1>7,\quad p\ne17,\quad
s>13,\quad 1\le\ell<s-13,\quad L=2s+\ell.
$$
所有系数在该惰性位的整数环 $\mathcal O$ 中，剩余域记为 $k$。
保留原权 $(1,3,4)$ 的 $A=7bS$、$B=7bS(\delta z)$、$C=7bS(2z)$，
原环 $\mathcal T$、归一化 $\mathcal N$ 及 $w=z^6$。

置
$$
h_7=16t^2+4t+7,\quad a=t(t-1)h_7,\quad t=-b/x^3,
$$
$$
g=e^{-\kappa w^s}\rho,\quad a_p=p\kappa\in\mathcal O^\times,
\quad e_2(v)=1+v+v^2/2,
$$
并使用同一个完整目标
$$
\Gamma_L=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2).
\tag{1}
$$
$g,t$ 的原高轴整性已经支付；以下所有整 Schur 矩阵均使用它们的实际系数。

R326 的 $G_0$ 是原40次导子，R328 已证明
$$
\mathcal J(G_0)=c_*w^{13}\mathcal U,\qquad
c_*\in\mathcal O^\times,\quad \mathcal U\in\Gamma_{L+13}^{\times}.
\tag{2}
$$
固定整数3159421仅在分裂类中，故 (2) 不新增惰性坏素数。
R328 的三条原导子为
$$
v_0=(t-1)(1+8t)h_7,\quad V=A/t=-7x^3S,
$$
$$
\boxed{K_0=v_0G_0,\quad K_1=v_0VG_0,\quad K_2=v_0V^2G_0,}
\tag{3}
$$
其原权为40、41、42，物理首阶都为十三。
$V$ 全纯且 $V(0)=-7$，但 $V\notin\mathcal N_1$；不能免费加入其所有幂。
本文只使用 (3) 中三条已经属于原 $\mathcal T$ 的实际元素。

## 2. 三条修正给 primitive 原来源扩张

对 $D\ge3$，定义真正的原子格
$$
\boxed{\mathcal F_D=G_0\mathcal N_{\le D}
                 +\mathcal O K_0+\mathcal O K_1+\mathcal O K_2
                 \ \subset\mathcal T_{\le D+40}.}
\tag{4}
$$
右边没有额外的次数42开销：$D\ge3$ 时三条权都已在 $D+40$ 预算内。

**定理1。** (4) 的和是直和，且其向原 $\mathcal T_{\le D+40}$ 的嵌入 primitive。
因此它的秩为 $\operatorname{rank}\mathcal N_{\le D}+3$，并在每个模 $p^N$ 来源中保持单射。

**证明。** R322 给 $\mathcal T/p\hookrightarrow\mathcal N/p$，后者是域；
$G_0\bmod p\ne0$。分次后，只需在相对次数0、1、2检查
$v_0,v_0V,v_0V^2$ 是否分别在 $\mathcal N_0,\mathcal N_1,\mathcal N_2$ 中。
次数零只有常数，而 $v_0$ 的四次首系数128为单位。
次数一只有 $\mathcal O A$，但 $(v_0V)/A=v_0/t$ 在 $t=0$ 有一个真极。
次数二的 $A^{-2}\mathcal N_2$ 在 $t=0$ 至多有一个极，而
$v_0V^2/A^2=v_0/t^2$ 有两个；这里 $v_0(0)=-7$ 为单位。
所以三个分次关系在剩余域中都只有零解，全部其余次数由 $G_0$ 在域中可消去得到。
这证明整个来源映射模 $p$ 单射，也就证明其余核没有 $p$ 挠。
同一论证在特征零给直和。$\square$

这个扩张确实比单独的 $G_0\mathcal N$ 大。它的合法性来自原导子成员性，
不是把 $V$ 或一个原点单位另作中央零来源。

## 3. 完整运输与三条虚拟列的准确意义

令
$$
Z=g(t-1)h_7e_2(a_p\epsilon),\qquad
W_i=v_0(t)Z^i\in\Gamma_L\quad(i=0,1,2).
\tag{5}
$$
这些仅是已付原列 $K_i$ 除去共同 $G_0$ 后，在目标中读取的有限级数。
并未声称 $v_0V^i$ 是归一化来源。
定义
$$
\mathcal J_D^+:(P,c_0,c_1,c_2)\longmapsto
             \mathcal J(P)+\sum_{i=0}^2c_iW_i,
\qquad P\in\mathcal N_{\le D}.
\tag{6}
$$
R328 的完整十三行运输 $m_{13}$ 给
$$
\boxed{\mathcal J_{L+13}\left(G_0P+\sum c_iK_i\right)
       =c_*\mathcal U\,m_{13}\left(\mathcal J_D^+(P,c_0,c_1,c_2)\right).}
\tag{7}
$$
所有四类来源的物理首阶至少十三，所以较短目标 $w^L$ 之后的未读系数在乘回时
都落到 $w^{L+13}$ 之后。此处与 R328 一样，先乘后截断，并非把截断环当作较长环的子环。

$m_{13}$ 的两个各十三行跨界带仍完整存在，总格指数仍为26。
对 R328 的核长度 $K_N$，因此有所有精度的准确比较
$$
\boxed{0\le K_N(\mathcal J_{L+13}|_{\mathcal F_D})
                   -K_N(\mathcal J_D^+)\le26.}
\tag{8}
$$
定理1又使这些实际原核嵌入整个 $\mathcal T_{\le D+40}$ 的核。
增加三条修正不重复收取40次，也不免费取消26条边界。

## 4. 单乘子中两条常数障碍，现在可以实际消去

R322 的归一化整基记为
$$
E_{n,j}=A^nt^j/T_n,\quad 0\le j\le d_n,
$$
$$
u_n=\lfloor3n/4\rfloor,\quad v_n=\lfloor n/2\rfloor,
\quad c_n=\lfloor2n/3\rfloor,
\quad d_n=3u_n+2v_n+c_n,
$$
$$T_n=t^{u_n}(t-1)^{c_n}(1+8t)^{v_n}h_7^{u_n}.$$
每个正次列在物理 $w$ 轴上至少一阶。因此 $\overline{\mathcal J}(\mathcal N)$
在三个径向常数坐标上的像只有 $(1,0,0)$。
R328 的边界空间 $\mathcal B_{13}$ 也不接触这些常数坐标。
故单乘子余核总有向 $k\epsilon\oplus k\epsilon^2$ 的满射，不能宣称它本身为零。

但 (5) 在同样三个坐标上的矩阵模 $p$ 是
$$
\boxed{\mathsf R=
\begin{pmatrix}
-7&49&-343\\
0&49a_p&-686a_p\\
0&49a_p^2/2&-686a_p^2
\end{pmatrix},\qquad
\det\mathsf R=7^6a_p^3\in k^\times.}
\tag{9}
$$
证明是 $g(0)=1,v_0(0)=V(0)=-7$，而相对 charge 是0、1、2。
高普通系数对常数坐标的进位都有一个 $p$，所以 (9) 是完整实际矩阵的模 $p$，
而非遗漏进位后的特征零等式。
特别，三条真实修正同时控制全部径向常数。

给定常数向量 $x=(x_0,x_1,x_2)$，置
$$
\begin{aligned}
q_0&=x_0-\frac{3x_1}{2a_p}+\frac{x_2}{a_p^2},\\
q_1&=\frac{2x_1}{a_p}-\frac{2x_2}{a_p^2},\\
q_2&=\frac{x_2}{a_p^2}-\frac{x_1}{2a_p},\qquad
\boxed{c_i=q_i/(-7)^{i+1}.}
\end{aligned}\tag{10}
$$
这些是 $\mathsf R^{-1}x$ 的准确系数；仅除以已知单位2、7、$a_p$。

更明确地，若 $P\in\mathcal N_{\le D}$ primitive，
$\mathcal J(P)\in p^r\Gamma_L$，记
$$o_r(P)=p^{-r}\mathcal J(P)\bmod p.$$
则存在 $Q\in\mathcal N_{\le D}$ 及 $c_i\in\mathcal O$，使原来源
$$
G_0P-p^r\left(G_0Q+\sum c_iK_i\right)
\tag{11}
$$
在完整长度 $L+13$ 的目标中被 $p^{r+1}$ 整除，当且仅当
$$
\boxed{[o_r(P)]=0\quad\text{于}\quad
\frac{\Gamma_L/p}{I_{N,D}+\mathcal B_{13}
                              +\operatorname{span}_k(\bar W_0,\bar W_1,\bar W_2)}.}
\tag{12}
$$
证明将 (7) 除以 $p^r$ 再模 $p$，使用
$\ker\bar m_{13}=\mathcal B_{13}$ 即可；(11) 模 $p$ 仍是非零的 $\bar G_0\bar P$。
所以这是 primitive 原关系的真实提升判据。

设 $\lambda$ 读取三个径向常数，定义剩余向量
$$
\boxed{o_r^\flat=o_r-\sum_{i=0}^2
                 (\mathsf R^{-1}\lambda(o_r))_i\bar W_i.}
\tag{13}
$$
它的三个常数坐标都为零；其余高行是 (13) 的完整值，不能继续删去。
相对于 R328 的单乘子商，(12) 的像增加至少二维、至多三维。
下界由 (9) 中原像没有的两条径向常数给出；上界由新列数给出。
这是一项固定但实际支付的改进，不是无界深度收益。

## 5. 归一化实际低行的统一单位主元

以下给 (6) 一个不依赖素数样本的有限消元，进一步缩小 (12) 的矩阵。
置
$$
r_n=n-u_n=\lceil n/4\rceil,\qquad
m_n=r_n+d_n=n+2u_n+2v_n+c_n.
\tag{14}
$$
真实轴
$$H_{n,j}=g^na(t)^nt^j/T_n$$
首阶为 $r_n+j$。若首阶是 $k$，首系数恰为单位
$$
\boxed{\lambda_{n,k}=(-b)^k(-1)^{n-c_n}7^{r_n}.}
\tag{15}
$$
这由 $t=-bw+\cdots$、$g(0)=1$ 直接得到。
因此每个 $n$ 可自由提供的首阶区间是 $r_n\le k\le m_n$。

对 $D\ge3$、$k\ge1$，这些区间中可用 charge 的数目，截到三后恰为
$$
\boxed{\min(3,\#\{n\le D:r_n\le k\le m_n\})
     =\sum_{j=0}^2\mathbf1_{k\le m_{D-j}}.}
\tag{16}
$$
证明 $m_n$ 严格递增、$m_n\ge n$。
若右边至少为 $q\in\{1,2,3\}$，取连续的
$$n=\min(k,D-q+1),\ n+1,\ldots,n+q-1.$$
当 $k\le D-q+1$ 时，$n=k$，最大 charge 至多 $k+2\le4k$，
故其最小阶不超过 $k$，而最大阶至少 $k$。
当 $k>D-q+1$ 时，取最后 $q$ 个 charge；
$r_D\le D-2\le k$，并且 $k\le m_{D-q+1}$。
反向由 $m_n$ 严格递增立即得到。

在第 $k$ 行，取仍存在的径向块数与 (16) 的最小值为 $q$，
选择上述连续 charge 的 $E_{n,k-r_n}$，并读取径向0至 $q-1$ 的坐标。
模 $p$ 的准确方块是
$$
\left(\frac{(a_p n)^i}{i!}\lambda_{n,k}\right)
      _{0\le i<q,\ n=n_0,\ldots,n_0+q-1}.
$$
连续整数的 Vandermonde 行列式约掉 $\prod i!$，给
$$
\boxed{\det=a_p^{q(q-1)/2}\prod_{n=n_0}^{n_0+q-1}\lambda_{n,k}
                 \in\mathcal O^\times.}
\tag{17}
$$
不同 $k$ 的列都是不同的原基列。按 $k$ 排列时，整个模 $p$ 子矩阵块下三角，
因为每列在低于自身首阶的所有径向行都为零。
所以不只逐个小块，合在一起仍是一个实际单位 minor。

## 6. 完整 Schur 化及其原格成本

在完整三块目标 (1) 中，归一化来源具有至少
$$
\boxed{B_D=1+\min(s-1,m_D)+\min(s-1,m_{D-1})
                         +\min(\ell-1,m_{D-2})}
\tag{18}
$$
个明确的单位主元。这里 $\ell\ge1$，所以各项非负。
第一项由常数来源1提供；三项分别计数三个径向块的正次首阶。

对扩张 (6)，用 $W_0,W_1,W_2$ 替换常数来源1，再保留 (18) 中全部正次主元。
正次列的径向常数模 $p$ 为零；(9)、(17) 因此组成一个完整的
$$\boxed{B_D+2\text{ 阶单位 minor}.}\tag{19}$$
这个结论不要求 $D<p$：连续 charge 的差是1和2，(17) 中没有随 $D$ 新增的分母。

现在用**完整整数矩阵**在这些行列上组成 $\mathsf U$，包括全部高轴和进位。
它由 (19) 在 $\mathcal O$ 上可逆。若原矩阵按相同行列排列成
$$\begin{pmatrix}\mathsf U&\mathsf B\\\mathsf C&\mathsf D\end{pmatrix},$$
则真正整 Schur 余块是
$$
\boxed{\mathsf M_D^+=\mathsf D-\mathsf C\mathsf U^{-1}\mathsf B.}
\tag{20}
$$
整行列变换给 $I_{B_D+2}\oplus\mathsf M_D^+$，所以所有 $N\ge1$ 都有
$$
\boxed{K_N(\mathcal J_D^+)=K_N(\mathsf M_D^+).}
\tag{21}
$$
这里的余来源是实际列减去 $\mathsf U^{-1}\mathsf B$ 的修正，仍为 primitive 整格。
不能把仅模 $p$ 的 Vandermonde 逆代替 (20) 的完整整数逆。

与 (8) 合并，$\mathsf M_D^+$ 中所有精度的关系，以一次 charge40 返回原来源，
完整目标的总边界差至多26。若仅处理 R328 的模 $p$ 剩余商，则将 (18) 中的
$s-1$ 换成 $s-14$，得到删除那二十六条已付边界后的相同单位消元。
这个后者只是指定模 $p$ 商；不据此删除完整整数目标的行。

当 $s,\ell$ 都超过相应 $m_n$ 时，$B_D=(25/2)D+O(1)$；
$\operatorname{rank}\mathcal N_{\le D}=47D^2/24+O(D)$。
所以 (20) 确实消掉明确的低行，并保留真正的大余块；没有将它计成所需的
$D^4\log D$ 主阶改善。

## 7. 原中央条件在这个消元中的准确位置

对任意正次来源 $P$，记实际 $W_j(P)$ 为 R322 的径向 Euler 值。
其径向常数行在完整三块中是
$$
J_{1,0}(P)=p[w^s]W_0(P),\qquad
J_{2,0}(P)=pa_p[w^s]W_1(P)+p^2[w^{2s}]W_0(P).
\tag{22}
$$
所以首 Bockstein 的这两行是
$$\bigl([w^s]W_0(P),\ a_p[w^s]W_1(P)\bigr)\bmod p.$$
R301、R314、R319 的原完整中央失败，确实使 (22) 对原三条 $A,B,C$ 的
首 Bockstein 值为零；其共同首权是同一个 $s_{p+1}$ 的单位倍数。
这只使用已经证明的准确缩放零条件。

式 (10)–(13) 处理任意实际提升类时，采用的是 (3) 的原来源修正。
并不需要 $K_i$ 的中央导数为零，亦没有宣称这一点。
同样，做 (20) 后不能把原三列的零条件直接赋给它们的余列：
若原列 $P$ 被改成 $P-\sum x_jP_j$，任何实际 Bockstein 行也必须减去
$\sum\bar x_j\,\beta(P_j)$，保留完整进位产生的值。

本篇的正向结果是：单一 $G_0\mathcal N$ 留下的两条常数障碍，已由原导子的
连续 charge 真正消去；余下问题现在是 (12)、(13)、(20) 中完整保留的高行及其深度。
这些余项是否受原完整中央失败约束，仍须继续证明。

依赖：[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R322](R322-three-true-zero-weighted-saturation-and-original-q2-kernel.md)、
[R326](R326-original-weighted-conductor-integral-generators-and-uniform-return.md)、
[R328](R328-original-conductor-thirteen-shift-and-normal-image-obstruction.md)、
[R329](R329-fourteen-generator-normalization-and-full-conductor-matrix.md)。
