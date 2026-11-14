# R56：有限个无限乘积之和与原临界算子的全部广义核分离

日期：2026-11-12（UTC）。会话：Astra-ISP-0c017065。子任务：critical_kernel。

**状态：已证明的中间结论。** 对原临界算子 $D=I-Q$，任意有限个 R16 收敛无限乘积向量（各自允许任意有限前缀）的线性张成，与每个广义核 $\ker D^r$ 都只有零交。各乘积的尾参数可以完全不同，不要求相互有序，不要求差属于 $\ell^1$，也不要求柱函数逼近具有给定速度。本条不证明这些有限和对 $A$ 全部循环，不决定一般 $H$ 向量上的 $\ker D$，不解决完整 Hilbert 不变子空间问题。

依赖：R9/R12 的有限链和高位归一化幂，R16 的收敛乘积局部分解，R24 的复对称性，R43 的原临界算子定义，R44 §2 的精确截断差。本条的真实进位误差、有限矩恢复、广义核像引理和有限维阶梯均在下文证明。

## 1. 模型、乘积类和主定理

沿用
$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Af)(y)=w(y)f(y-1),
$$
$$
w(y)=a_{v_2(y)}\quad(y\ne0),\qquad w(0)=0,
$$
$$
a_j=e^{-L_j},\qquad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
$$
写
$$
N_j=\frac{A^{2^j}}{W_{2^j}},\qquad
W_n=\|A^n\|,\qquad
\eta_j=\frac{a_{j+1}}{a_j}.
$$
令 $E_j=e_{10}$ 作用于第 $j$ 个二进位。已知
$$
\|N_j\|=1,\qquad N_j^2=\eta_jN_{j+1},\qquad
\|N_j-E_j\|=\eta_j.
\tag{1.1}
$$
$N_j$ 在所有低于 $j$ 的位上是恒等作用。

原临界参数为
$$
\delta_j=\frac2{(j+2)^2+1},\qquad r_j=1-\delta_j,
$$
$$
V_j=(I+r_jN_j)(I+N_j)^{-1},\qquad
Q=\prod_{j\ge0}V_j,\qquad D=I-Q.
\tag{1.2}
$$
$\sum_j\delta_j<\infty$，所以乘积在算子范数下收敛，全部有限子乘积的范数一致有界。$Q$ 属于 $\mathcal A=\overline{\mathbb C[I,A]}$，故与 $A$ 和各 $N_j$ 交换。

使用连续复双线性型
$$
B(f,g)=\int f(y)g(-1-y)\,d\mu(y)
=\langle f,Cg\rangle,\qquad
Cg(y)=\overline{g(-1-y)}.
\tag{1.3}
$$
$C$ 是共轭线性等距对合；$A$、$Q$ 及 $\mathcal A$ 中全部算子对 $B$ 对称：
$$
B(Tf,g)=B(f,Tg)\qquad(T\in\mathcal A).
\tag{1.4}
$$
此外 $1$ 对 $A$ 循环。

记 $\mathscr P$ 为 R16 的以下向量类：选任意有限前缀 $v\ne0$，在余下独立位上选两点函数 $h_j$，满足
$$
\frac{|h_j(0)|^2+|h_j(1)|^2}{2}=1,
$$
并且有限乘积在 $L^2$ 中收敛到非零向量。把该极限乘以 $v$，并允许非零标量倍数，即得到 $\mathscr P$。R16 §2 给出：每个 $h\in\mathscr P$ 在充分高的每一位 $j$ 都有精确张量分解
$$
h=h^{\langle j\rangle}\otimes h_j,\qquad
h_j(0)\to1,\quad h_j(1)\to1.
\tag{1.5}
$$
这里 $h^{\langle j\rangle}$ 包含除第 $j$ 位以外的全部变量；有限前缀不必是逐位乘积。因此
$$
u_{h,j}:=\frac{h_j(1)}{h_j(0)}
$$
对充分大的 $j$ 有定义，而且 $u_{h,j}\to1$。不要求这个趋近有任何指定速度。

**定理 1.1。** 若
$$
U=\operatorname{span}\{h_1,\ldots,h_s\},\qquad h_i\in\mathscr P,
$$
则对每个整数 $r\ge1$，
$$
\boxed{U\cap\ker D^r=\{0\}.}
\tag{1.6}
$$
乘积向量可以线性相关；每个乘积可以使用不同的归一化因子及不同有限前缀。

下文只需要 (1.5)，不使用每个 $h_i$ 自身的循环性。唯一使用的循环向量是固定的参考向量 $1$。

## 2. 真实 $Q^k$ 的单高位局部模型

令 $A_j$ 是删去所有赋值至少为 $j$ 的权所得有限链截断，则
$$
A_j=J_j\otimes I,\qquad
\|A-A_j\|=a_j,\qquad
\|A^n-A_j^n\|\le n a_j.
\tag{2.1}
$$
它只作用于低 $j$ 位。对 $i<j$ 置
$$
N_i^{[j]}=\frac{A_j^{2^i}}{W_{2^i}}.
$$
R44 §2 的精确路径计数给
$$
\|N_i-N_i^{[j]}\|=\frac{a_j}{a_i},\qquad
\|N_i^{[j]}\|\le1,\qquad
\|(N_i^{[j]})^2\|\le\eta_i.
\tag{2.2}
$$

### 2.1 全部低位因子的截断误差

若 $\|T\|\le1$ 且 $\|T^2\|\le\eta_0<1$，则
$$
(I+T)^{-1}=(I-T)(I-T^2)^{-1},
\qquad
\|(I+T)^{-1}\|\le\frac2{1-\eta_0}.
\tag{2.3}
$$
这给 $N_i$、$N_i^{[j]}$ 和 $E_i$ 的逆一个共同界。用
$$
V_i(T):=(I+r_iT)(I+T)^{-1}
=r_iI+\delta_i(I+T)^{-1}
$$
及逆的差恒等式，得到
$$
\|V_i(S)-V_i(T)\|\le C\delta_i\|S-T\|
\tag{2.4}
$$
（对上述算子成立）。又 $\|V_i(T)-I\|\le C\delta_i$，所以全部截断或未截断子乘积的范数都有共同界。

定义
$$
Q_{<j}=\prod_{i<j}V_i,\qquad
Q_{<j}^{[j]}=\prod_{i<j}V_i(N_i^{[j]}),\qquad
Q_{>j}=\prod_{i>j}V_i.
$$
由乘积差的望远镜展开，(2.2)—(2.4) 给
$$
\begin{aligned}
\|Q_{<j}-Q_{<j}^{[j]}\|
&\le C\sum_{i<j}\delta_i\frac{a_j}{a_i}\\
&\le C\frac{a_j}{a_{j-1}}\sum_{i<j}\delta_i
\le C'\eta_{j-1}.
\end{aligned}
\tag{2.5}
$$
这里把 $\sum\delta_i$ 吸收进常数。低位全部因子累积的自然界是 $O(\eta_{j-1})$；没有将它误写成 $O(a_j)$。

置
$$
G_j=Q_{<j}^{[j]}Q_{>j}.
\tag{2.6}
$$
第一因子只作用于低 $j$ 位；第二因子的每个 $N_i$ 都满足 $i>j$，故只作用于高于 $j$ 的位。因此 $G_j$ 在第 $j$ 位上是恒等作用，与 $E_j$ 交换，而且 $\sup_j\|G_j\|<\infty$。

由于 $E_j^2=0$，
$$
V_j(E_j)=I-\delta_jE_j.
$$
(1.1) 和 (2.4) 给
$$
\|V_j-(I-\delta_jE_j)\|\le C\delta_j\eta_j.
\tag{2.7}
$$
将 (2.5) 和 (2.7) 代入 $Q=Q_{<j}V_jQ_{>j}$，得到
$$
\boxed{
\|Q-G_j(I-\delta_jE_j)\|
\le C\eta_{j-1}.
}
\tag{2.8}
$$
使用了 $\eta_j\le\eta_{j-1}$（对本明确权列成立，且仅需充分大的 $j$）。

### 2.2 固定次幂

对每个固定整数 $k\ge0$，幂的望远镜差及 $G_jE_j=E_jG_j$ 给
$$
\boxed{
Q^k=G_j^k(I-k\delta_jE_j)
+O_{\|\cdot\|,k}(\eta_{j-1}).
}
\tag{2.9}
$$
确切地说，先把 $Q$ 替换为 $G_j(I-\delta_jE_j)$，用一致范数界控制固定次幂差；再用
$$
(I-\delta_jE_j)^k=I-k\delta_jE_j.
$$
不需要也没有声称实际的 $Q^kh_i$ 仍是乘积向量。我们仅把 $Q^k$ 转移到双线性型的第一位置，然后近似它作用于参考向量 $1$。

最后，由权的显式公式，
$$
\eta_{j-1}=o(\delta_j^q)\qquad\text{对每个固定 }q>0.
\tag{2.10}
$$
本条只需要 $q=1$。

## 3. 高位矩的标量因子公式

**引理 3.1。** 固定 $h\in\mathscr P$ 和整数 $n,k\ge0$。对充分大的 $j$，
$$
\boxed{
B(N_jA^n1,Q^kh)
=
\frac{B(A^n1,Q^kh)}
{1+u_{h,j}-k\delta_j}
+O_{n,k,h}(\eta_{j-1}).
}
\tag{3.1}
$$
若同时考虑有限多个 $n,k,h$，误差可以使用共同常数。

**证明。** 由对称性和交换性，
$$
B(N_jA^n1,Q^kh)=B(N_jA^nQ^k1,h).
\tag{3.2}
$$
依次用 (1.1)、(2.1)、(2.9) 替换右边的三个算子，得到
$$
B(N_jA^nQ^k1,h)
=
B\bigl(E_jA_j^nG_j^k(I-k\delta_jE_j)1,h\bigr)
+O_{n,k,h}(\eta_{j-1}).
\tag{3.3}
$$
这里全部算子范数对固定 $n,k$ 一致有界，且 $a_j,\eta_j\le\eta_{j-1}$ 对充分大的 $j$ 成立。另一方面，同样的估计给
$$
B(A^n1,Q^kh)
=
B\bigl(A_j^nG_j^k(I-k\delta_jE_j)1,h\bigr)
+O_{n,k,h}(\eta_{j-1}).
\tag{3.4}
$$

$A_j^nG_j^k$ 不作用于第 $j$ 位。因此 (3.3)—(3.4) 的第一位置在该位具有局部坐标
$$
(f(0),f(1))=(1,1-k\delta_j),
$$
第二位置由 (1.5) 具有局部坐标 $(h_j(0),h_j(1))$。双线性型 $B$ 在该位交换第二个向量的两坐标，故局部贡献分别为
$$
B_{\mathrm{loc}}(f,h_j)
=\frac{h_j(1)+(1-k\delta_j)h_j(0)}2,
\qquad
B_{\mathrm{loc}}(E_jf,h_j)=\frac{h_j(0)}2.
$$
余下位上的积分是同一个标量。于是两个近似矩精确相差因子
$$
\frac1{1+u_{h,j}-k\delta_j}.
$$
分母趋向 $2$，其逆最终一致有界。将 (3.3)—(3.4) 合并即得 (3.1)。证毕。

设
$$
d_{h,j}=\frac1{1+u_{h,j}}\longrightarrow\frac12.
$$
对任意固定有限个 $k$，几何展开有共同的误差界：
$$
\boxed{
\frac1{1+u_{h,j}-k\delta_j}
=d_{h,j}+k\delta_jd_{h,j}^2+O_k(\delta_j^2).
}
\tag{3.5}
$$
$d_{h,j}$ 的趋近速度与 $\delta_j$ 不必有任何比较关系。

## 4. 固定有限维空间上的有限矩恢复

**引理 4.1。** 对每个有限维子空间 $W\subset H$，存在有限集合 $F_W\subset\mathbb N_0$ 和常数 $C_W$，使
$$
\|w\|\le C_W\max_{n\in F_W}|B(A^n1,w)|
\qquad(w\in W).
\tag{4.1}
$$

**证明。** 若 $B(A^n1,w)=0$ 对全部 $n\ge0$ 成立，则 $B(x,w)=0$ 对稠密集合 $\operatorname{span}\{A^n1:n\ge0\}$ 成立。连续性及 $B$ 的非退化性给 $w=0$。

因此这些线性泛函在 $W$ 上的共同核为零。有限维性保证可以挑出有限多个泛函仍具有零共同核：若当前共同核非零，就选一个不在其上恒零的泛函，使维数严格下降。所得有限矩映射是单射；有限维空间上的逆映射有界，即得 (4.1)。证毕。

对固定 $p\ge0$，以下取
$$
W_p=\operatorname{span}\{Q^kh_i:1\le i\le s,\ 0\le k\le p+1\}.
\tag{4.2}
$$
这只是有限维空间，完全不预设列向量独立，也不预设它们各自是乘积。引理 4.1 给它一组固定有限测试；测试可以依赖 $U,p$，但不依赖高位 $j$。

## 5. 广义核像引理

定义列映射
$$
F:\mathbb C^s\longrightarrow H,\qquad
Fc=\sum_{i=1}^s c_ih_i.
$$

**引理 5.1。** 对每个整数 $p\ge0$，
$$
\boxed{
D^p\bigl(U\cap\ker D^{p+1}\bigr)\subseteq D^{p+1}U.
}
\tag{5.1}
$$

**证明。** 取 $v=Fc\in U\cap\ker D^{p+1}$，其中 $c$ 固定。由
$$
D^{p+1}=\sum_{k=0}^{p+1}(-1)^k\binom{p+1}{k}Q^k,
$$
对每个 $n,j$ 有
$$
0=B(N_jA^n1,D^{p+1}v)
=\sum_{i,k}c_i(-1)^k\binom{p+1}{k}
 B(N_jA^n1,Q^kh_i).
\tag{5.2}
$$
写
$$
d_{i,j}=\frac1{1+u_{h_i,j}},\qquad
\Delta_j=\operatorname{diag}(d_{1,j},\ldots,d_{s,j}).
$$
对 (5.2) 应用 (3.1)、(3.5)，并使用恒等式
$$
\sum_{k=0}^{p+1}k(-1)^k\binom{p+1}{k}Q^k
=-(p+1)QD^p,
\tag{5.3}
$$
得到对每个固定 $n$，
$$
\begin{aligned}
B\bigl(A^n1,\,
D^{p+1}F\Delta_jc
-(p+1)\delta_jQD^pF\Delta_j^2c
\bigr)
=O_{n,p,U,c}(\delta_j^2+\eta_{j-1}).
\end{aligned}
\tag{5.4}
$$
括号内向量属于固定的 $W_p$。现在只对 §4 为 $W_p$ 选出的有限测试使用 (5.4)，再应用 (4.1)，即可把标量矩估计转成真实 Hilbert 范数估计：
$$
\boxed{
\left\|
D^{p+1}F\Delta_jc
-(p+1)\delta_jQD^pF\Delta_j^2c
\right\|
=O_{p,U,c}(\delta_j^2+\eta_{j-1}).
}
\tag{5.5}
$$

子空间 $D^{p+1}U$ 有限维，因而闭。令
$$
\pi:H\longrightarrow H/D^{p+1}U
$$
为商映射。第一项 $D^{p+1}F\Delta_jc$ 始终在被商掉的子空间内，故它被**精确**消去；不必估计 $\Delta_j-\frac12I$ 相对于 $\delta_j$ 的大小。对 (5.5) 取商、除以 $\delta_j$，得到
$$
\left\|\pi\bigl(QD^pF\Delta_j^2c\bigr)\right\|
=O_{p,U,c}\left(\delta_j+\frac{\eta_{j-1}}{\delta_j}\right)
\longrightarrow0.
\tag{5.6}
$$
由于 $\Delta_j^2\to\frac14I$，取极限得
$$
QD^pv\in D^{p+1}U.
$$
而 $D^{p+1}v=0$，所以
$$
QD^pv=(I-D)D^pv=D^pv.
$$
这就是 (5.1)。证毕。

特别地，$p=0$ 给
$$
U\cap\ker D\subseteq DU.
\tag{5.7}
$$
只用 (5.7) 还不能直接迭代，因为其原像未必在 $\ker D$ 中；上面全部 $p$ 的统一引理恰好补上这个缺口。

## 6. 有限维广义核阶梯：主定理的证明

反设某个 $r\ge1$ 存在 $0\ne v_0\in U\cap\ker D^r$。把 $r$ 减到该向量的最小广义阶，记为 $r_0$，则
$$
w=D^{r_0-1}v_0\ne0,\qquad Dw=0.
\tag{6.1}
$$
$w$ 不必属于 $U$，后面不使用这个额外条件。

对 $v_0$ 应用引理 5.1 中 $p=r_0-1$ 的情形，得到
$$
w\in D^{r_0}U.
$$
因此可取 $v_1\in U$ 使
$$
D^{r_0}v_1=w,\qquad D^{r_0+1}v_1=0.
$$
它的最小广义阶恰为 $r_0+1$。

递归地，假设已取 $v_t\in U$ 满足
$$
D^{r_0+t-1}v_t=w\ne0,\qquad
D^{r_0+t}v_t=0.
\tag{6.2}
$$
对该向量应用 $p=r_0+t-1$ 的引理 5.1，得到 $w\in D^{r_0+t}U$，故可以取 $v_{t+1}\in U$ 满足下一步的 (6.2)。

这构造出 $U$ 内任意高的广义阶。它们线性无关：若
$$
\sum_{t=0}^{N}\alpha_tv_t=0,\qquad \alpha_N\ne0,
$$
则作用 $D^{r_0+N-1}$ 后，所有 $t<N$ 的项消失，仅剩
$$
\alpha_Nw=0,
$$
与 $w\ne0$ 矛盾。有限维 $U$ 不可能含有无限个线性无关向量。反证成立，定理 1.1 得证。

## 7. 确切覆盖范围和剩余缺口

1. 任意两个、三个乃至任意有限个不同 R16 乘积之和，只要非零，就不在原临界 $D$ 的任何有限阶广义核里。每个乘积可带独立的有限前缀，亦允许非连续的复相位乘积和任意慢的柱逼近。
2. 不需要共同的标量 Rademacher 参数，也不需要乘积之间存在逐点序或 $\ell^1$ 尾差。证明只使用每个局部比值趋近 $1$，没有将这种趋近速度与 $\delta_j$ 强行比较。
3. 本条通过参考向量 $1$ 的循环性把有限多矩恢复成有限维范数估计；没有把一般无限矩映射当作有界逆，也没有把形式除法当成有界算子。
4. 本条只针对固定临界算子 $D$。对一个一般有限乘积和 $v$，它是否对 $A$ 循环仍需排除任意 $g\in H$ 的矩消失，不能由 $D^rv\ne0$ 推出。
5. 有限乘积和包含稠密的柱函数核心，但其与各 $\ker D^r$ 交零不允许取闭包推出 $\ker D=0$。当前临界核的一般向量问题及主课题仍未解决。

同一机制可供有限维、对翻译稳定的指数多项式空间进一步使用：需要将 §3 的标量 $d_{i,j}$ 替换为趋向 $\frac12I$ 的有限矩阵，并保持一阶项为 $\delta_j$ 乘其平方。该延伸另记，不在本条中假定成立。

