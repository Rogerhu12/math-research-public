# R41：两个独立 CM 乘子的共同深度在全部惰性素数上可求和

日期：2026-11-12。**状态：下面的无条件加权求和定理已证明。**

本篇不再逐个 $(a,r)$ 使用不一致的 gcd 界。
一次有限的短关系乘积同时覆盖全部有关素数和全部提升深度，
然后利用惰性处的 norm/angle 阶数乘积。
这把两个固定独立 CM 乘子的**共同**惰性预算从 $O(\log k)$
加强为 $O(1)$。尚未把这种共同核实现为本题所需的固定非代数 germ。

## 1. 完全固定的两个乘子及结论

取
$$
K=\mathbb Q(i),\qquad
b_1=2+i,\quad b_2=3+2i,\qquad
A_1=5,\quad A_2=13,\qquad
u_j=b_j/\bar b_j.
$$
两个正整数 $5,13$ 乘法独立。
$u_1,u_2$ 也乘法独立：
在 Gaussian 素理想 $(b_1)$、$(b_2)$ 上取赋值，分别检测两个指数。
所有出现的数都已固定，不随 $p$ 或截断阶 $k$ 改变。

对奇的惰性素数 $p$，令
$$
\Gamma_p=\langle b_1,b_2\rangle
\subset\mathbb F_{p^2}^\times,\qquad d_p=|\Gamma_p|,
$$
$$
c_p=\min_{j=1,2}v_p(b_j^{d_p}-1),\qquad
D_p=\operatorname{lcm}(d_p,4).
\tag{1.1}
$$
各 $c_p$ 为有限正整数，赋值归一化为 $v_p(p)=1$。
定义
$$
M(k)=\sum_{D_p\le k}c_p\log p.
$$
下面将证明，对全部 $k\ge4$，
$$
\boxed{\quad
M(k)\le C\,k^{3/4},\qquad
C=2\sqrt{(4\log65)(2\log65+4\log2)}
=27.2543214115\ldots.
\quad}
\tag{1.2}
$$
特别地，
$$
\boxed{\quad
\sum_{p\ {\rm inert}}\frac{c_p\log p}{D_p-1}<\infty,
\qquad
\sum_{\substack{p\ {\rm inert}\\D_p>K}}
\frac{c_p\log p}{D_p-1}
\le8C K^{-1/4}\quad(K\ge4).
\quad}
\tag{1.3}
$$
常数没有为数值最小而优化；指数严格小于一已经给出所需收敛。

## 2. 为什么提升深度不会破坏短关系计数

以下简单事实是全部统一性的关键。
若模 $p$ 的单位子群阶为 $a$，$p\nmid a$，
且所有指定生成元的 $a$ 次幂模 $p^c$ 都为一，
则这些生成元在模 $p^c$ 的子群阶也恰为 $a$。

确实，模 $p^c$ 到模 $p$ 的单位群核是一个 $p$-群。
指定子群的指数整除 $a$，故它与这个核的交集平凡；
其约化又满射到原来的阶 $a$ 子群。
这对 $\mathbb Z_p$ 和非分歧二次局部整数环都适用。

因此可以在模 $p^c$ 中直接使用与模 $p$ 相同大小的 pigeonhole 网格。
它产生的是被 $p^c$ 整除的短关系，而不是仅模 $p$ 的短关系。

## 3. 两个有理范数的统一质量界

对 $p\nmid65$ 置
$$
a_p=|\langle5,13\rangle\bmod p|,\qquad
c_p^N=\min\{v_p(5^{a_p}-1),v_p(13^{a_p}-1)\}.
$$
令 $L=\log65$。我们证明
$$
\boxed{\quad
\sum_{a_p\le x}c_p^N\log p\le4Lx^{3/2}
\qquad(x\ge1).
\quad}
\tag{3.1}
$$

取 $M=\lfloor\sqrt x\rfloor$。
因为 $(M+1)^2>x\ge a_p$，在模 $p^{c_p^N}$ 的阶 $a_p$ 子群中，
$(M+1)^2$ 个元素
$$
5^{e_1}13^{e_2},\qquad 0\le e_1,e_2\le M,
$$
必有碰撞。差向量 $e=(e_1,e_2)$ 非零、$|e_i|\le M$，
并使 $p^{c_p^N}$ 整除非零整数
$$
N_e=
5^{e_1^+}13^{e_2^+}
-5^{e_1^-}13^{e_2^-},
\qquad e_i^\pm=\max(\pm e_i,0).
$$
这些整数非零，因为 $5,13$ 乘法独立。
向量 $e$ 与 $-e$ 给同一绝对值，可只取一半向量。
其数目为 $2M(M+1)\le4M^2$，且
$$
\log|N_e|\le ML.
$$
于是所有所需 $p^{c_p^N}$ 的乘积整除这些固定短关系整数的乘积，
在各素数处的赋值至少相应深度。取对数得到
$$
\sum_{a_p\le x}c_p^N\log p
\le2M(M+1)ML\le4Lx^{3/2}.
$$
这里没有先对每个 $p$ 取不同的常数再交换无限求和。
对给定 $x$，一个确定的有限整数乘积已经同时控制全部素数。

## 4. 两个独立角向单位的统一质量界

现在只取惰性素数。令
$$
r_p=|\langle u_1,u_2\rangle\bmod p|,\qquad
c_p^U=\min_{j=1,2}v_p(u_j^{r_p}-1).
$$
我们证明
$$
\boxed{\quad
\sum_{\substack{p\ {\rm inert}\\r_p\le x}}
c_p^U\log p
\le(2L+4\log2)x^{3/2}
\qquad(x\ge1).
\quad}
\tag{4.1}
$$

仍用 $M=\lfloor\sqrt x\rfloor$ 和第 2 节的模 $p^c$ 子群。
碰撞给出 $|e_i|\le M$ 的非零向量，使 $p^{c_p^U}$ 整除
$$
U_e=
\prod_{j=1}^2 b_j^{e_j^+}\bar b_j^{e_j^-}
-\prod_{j=1}^2\bar b_j^{e_j^+}b_j^{e_j^-}
\in\mathbb Z[i].
\tag{4.2}
$$
$U_e\ne0$ 由角向单位的乘法独立性保证。
分母只含 $5,13$，对本处惰性素数都是单位。
两项的复绝对值均至多为 $\exp(ML/2)$，所以
$$
\log|N_{K/\mathbb Q}U_e|\le2\log2+ML.
\tag{4.3}
$$
一个惰性素数在 $K$ 中剩余次数为二。
因此 $p^{c_p^U}\mid U_e$ 给
$p^{2c_p^U}\mid N_{K/\mathbb Q}U_e$。
对同一半数短关系相乘，再除以二，得到
$$
\begin{aligned}
\sum_{\substack{p\ {\rm inert}\\r_p\le x}}c_p^U\log p
&\le2M(M+1)\left(\log2+\frac{ML}{2}\right)\\
&\le4\log2\,x+2Lx^{3/2}\\
&\le(2L+4\log2)x^{3/2}.
\end{aligned}
$$
深度 $c_p^U$ 任意大都已包含在这个证明中。

## 5. 惰性 norm/angle 分解把指数降到四分之三

在 $\Gamma_p$ 上，Frobenius 是共轭。
范数映射为 $g\mapsto g^{p+1}$，
角向映射为 $g\mapsto g^{1-p}$。
它们的像分别由 $5,13$ 和 $u_1,u_2$ 生成。
因 $\Gamma_p$ 为阶 $d_p$ 的循环群，
$$
a_p=\frac{d_p}{\gcd(d_p,p+1)},\qquad
r_p=\frac{d_p}{\gcd(d_p,p-1)}.
\tag{5.1}
$$
用 $\gcd(p-1,p+1)=2$，并逐个检查二进阶，得到
$$
\boxed{a_pr_p\in\{d_p,d_p/2\}.}
\tag{5.2}
$$
这是对整个双生成元子群的公式，不是把两个单生成元公式不加检验地相乘。

另外，定义 (1.1) 给每个 $b_j^{d_p}\equiv1\pmod{p^{c_p}}$。
取范数或与共轭取商，再用 $p\nmid d_p/a_p,d_p/r_p$ 的提升指数公式，
得到
$$
c_p\le c_p^N,\qquad c_p\le c_p^U.
\tag{5.3}
$$

若 $D_p\le k$，则 $a_pr_p\le d_p\le k$。
对任意 $x>0$，这些素数被下列两类覆盖：
$$
a_p\le x
\quad\text{或}\quad
r_p\le k/x.
$$
设
$$
C_N=4L,\qquad C_U=2L+4\log2.
$$
当 $x,k/x\ge1$ 时，由 (3.1)、(4.1)、(5.3)，
$$
M(k)\le C_Nx^{3/2}+C_U(k/x)^{3/2}.
\tag{5.4}
$$
取 $x=(C_U/C_N)^{1/3}\sqrt k$。
对 $k\ge4$ 两个阈值均至少为一，得到
$$
M(k)\le2\sqrt{C_NC_U}\,k^{3/4},
$$
即 (1.2)。

这一步一次性覆盖整个双指标区域。
其指数改善来自每一侧各有两个独立生成元，而不来自一个未经统一化的
单对 gcd 小量估计。

## 6. 分部求和与实际预算接口

记 $w_p=c_p\log p$。Stieltjes 分部求和给，对 $K\ge4$，
$$
\sum_{D_p>K}\frac{w_p}{D_p-1}
=-\frac{M(K)}{K-1}
+\int_K^\infty\frac{M(t)}{(t-1)^2}\,dt.
$$
因为 $M(t)=O(t^{3/4})$，无穷端边界项为零。
再用 $(t-1)^{-2}\le(16/9)t^{-2}$，得到
$$
\sum_{D_p>K}\frac{w_p}{D_p-1}
\le\frac{64C}{9}K^{-1/4}\le8C K^{-1/4}.
$$
于是 (1.3) 成立。

若一个实际固定 germ 在全部惰性处具有大小界
$$
S_p\ge
p^{-C_0/(p^2-1)-C_1c_p/(D_p-1)}
$$
（$C_0,C_1$ 为固定常数），那么本篇直接证明其全部惰性大小损失可求和。
这比惰性部分的 $\alpha=0$ 的 jet 渐近更强。
但是本篇只证明这个条件接口及其算术和；
没有把已有单乘子逆像的深度替换成未经实现的 $\min$。

## 7. 仍然需要的固定核与 ordinary 控制

共同阶 $d_p$、共同深度 $c_p$ 同时使用 $b_1,b_2$。
此前的仿射核只要求一个有理范数和一个角向单位，
分别仍只有秩一，所以它不自动满足 (1.1)。
必须构造一个固定 $\mathbb Q$-germ，使真正的局部坏块及深度
受上述共同数据控制，同时保留复一致化、非代数性与 ordinary 目标角色接口。

在分裂素数处，没有 (5.2) 这样的 $p-1$ 与 $p+1$ 的阶数乘积。
同一个双生成元短关系法本身只给单侧质量 $O(x^{3/2})$，
不足以把其加权和压到 $O(\log k)$。
增加有限多个生成元的一般短关系指数为 $1+1/r>1$，
也不能只凭该指数解决 ordinary 问题。
中心非 Wieferich 条件及额外 tame 共振仍须另行处理。

## 8. 与已出版阶数结果的关系

这种短关系计数与经典有限生成乘法群的 order 方法同源。
Pappalardi 的已出版论文
*On the Order of Finitely Generated Subgroups of $\mathbb Q^\times$ (mod $p$) and Divisors of $p-1$*，
J. Number Theory 57 (1996)，207–222，
[DOI](https://doi.org/10.1006/jnth.1996.0044)，
研究了秩 $r$ 群的模 $p$ 阶数；其出版摘要明确区分无条件的
$p^{r/(r+1)}$ 型结果与依赖 GRH 的接近 $p$ 的结果。
这里没有调用后者。

本篇实际使用的带任意 $p^c$ 深度及明确总对数质量的形式，
在第 2–4 节已完整证明；结论 (1.2)–(1.3) 不依赖额外的文献假设，
也不依赖任何未核查的高阶非 Wieferich 命题。
