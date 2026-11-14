# 任意多种正权的主 spin 边界：完整真实相位常数 1

本稿证明一个不限制位数、不限制独立权值个数的新物理族。把 Boolean 空间按等权组的实际正交 spin 模块分解后，若一个组的有效 spin 恰比其余组的 spin 总和大 \(1\)，则该完整模块的临界低源相位满足
\[
\boxed{\Phi\preceq I.}
\]
非零源在每个这样的有效模块中为一维；所有组内 primitive 多重性均保留为正交副本。结论来自完整 MP 逆的精确积分表达和一条自足的对数凹矩不等式，不是有限权例子的数值归纳。

本文不声称解决含非零中央硬源的任意多组模块，也不把本族外推为一般偶相位或原无限 graph 结论。

## 1. 模型、真实源及目标

取任意整数 \(m\ge0\)、\(q_i\ge0\)，置
\[
Q=\sum_{i=1}^m q_i,\qquad s=Q+1,\qquad M=2Q+2.
\]
第 \(i\) 个小组有 \(q_i\) 位、共同平方权 \(z_i>0\)；主组有 \(Q+2\) 位、共同平方权 \(1\)。零长度组可以删去。任意主组正权可先共同缩放成 \(1\)：若全部 \(b_i\) 乘 \(\lambda\)，则 \(G,L_2,H_0\) 分别乘 \(\lambda^{-2},\lambda^{-4},\lambda^{-2}\)，相位不变。

在实际 Boolean Hilbert 空间中，标准子集向量正交归一，\(E_i\) 删除第 \(i\) 位，\(E_i^*\) 添加第 \(i\) 位。记
\[
d_b=\sum_i b_iE_i,\qquad e_b=\sum_i b_i^{-1}E_i^*,
\]
并限制到各组内完全对称的正交 reducing 模块 \(\mathcal S\)。实际低源和中央硬源为
\[
V_b=\ker d_b\cap\mathcal S_{s-1},\qquad
U_b=\ker d_b\cap\mathcal S_s.
\]
设 \(\mathcal J_1,\mathcal J_2\) 分别为完整 \(d_b\) 和 \(d_b^2/2\) 的 MP 逆，再限制到 \(V_b\)，
\[
G=\mathcal J_1^*\mathcal J_1,\qquad
L_2=\mathcal J_2^*\mathcal J_2,\qquad A_0=e_b^*|_{U_b}.
\]
目标为
\[
H_0=G^{-1}L_2-2G-A_0A_0^*,\qquad
\boxed{\Phi=H_0^*L_2^{-1}H_0\preceq I_{V_b}.} \tag{1.1}
\]

这里 \(\mathcal S\) 对 \(d_b,e_b\) 及其伴随都 reducing。因此在 \(\mathcal S\) 中计算得到的是完整物理 MP 逆在该模块上的限制：不先把层压成 primitive 再取逆，也不从另外的模块借入虚假的小范数原像。

## 2. 唯一低源与空硬源

用聚合多项式坐标
\[
f(\alpha_1,\ldots,\alpha_m,\gamma)
=\sum_{\boldsymbol k,\ell} f_{\boldsymbol k,\ell}
 \alpha_1^{k_1}\cdots\alpha_m^{k_m}\gamma^\ell.
\]
系数 \(f_{\boldsymbol k,\ell}\) 除以对应子集数
\(\prod_i\binom{q_i}{k_i}\binom{Q+2}{\ell}\)，就是每个物理子集的共同振幅。故实际范数为
\[
\|f\|^2
=\sum_{\boldsymbol k,\ell}
\frac{|f_{\boldsymbol k,\ell}|^2}
{\prod_i\binom{q_i}{k_i}\binom{Q+2}{\ell}}. \tag{2.1}
\]
不带权的 lowering 和 raising 为
\[
d_0=\sum_i\partial_{\alpha_i}+\partial_\gamma,
\]
\[
e_0=\sum_i\alpha_i(q_i-\alpha_i\partial_{\alpha_i})
+\gamma(Q+2-\gamma\partial_\gamma). \tag{2.2}
\]

若 \(d_0f=0\)，则 \(f\) 是差变量
\(\alpha_i-\gamma\) 的多项式。每个差变量的次数至多 \(q_i\)：若更大，其最高 \(\alpha_i\) 系数不可能由平移消掉。于是：

* 在总次数 \(Q\) 上，primitive 恰为
  \[
  v=\prod_{i=1}^m(\alpha_i-\gamma)^{q_i} \tag{2.3}
  \]
  的标量倍数。
* 在总次数 \(Q+1\) 上，没有 primitive。

令 \(D_j=\operatorname{diag}(b_I)\) 作用于真实 \(j\) 层，则
\[
d_b=D_{j-1}^{-1}d_0D_j.
\]
因此
\[
\boxed{V_b=\mathbb C D_{s-1}^{-1}v,\qquad U_b=0.} \tag{2.4}
\]
直接把 (2.3) 代入 (2.2)，还得到
\[
\boxed{e_0v=2\gamma v.} \tag{2.5}
\]
这里主组容量 \(Q+2\) 的差 \(2\) 正是该系数的来源。

## 3. 完整第一逆、顶逆及共同源度量

以 \(v/\sqrt{N_v}\) 为固定源单位向量，\(N_v=\|v\|^2\)。定义真实拉回二次型
\[
h=\frac{\|D_{s-1}^{-1}v\|^2}{N_v},\quad
g=\frac{\|\mathcal J_1D_{s-1}^{-1}v\|^2}{N_v},\quad
\ell=\frac{\|\mathcal J_2D_{s-1}^{-1}v\|^2}{N_v}. \tag{3.1}
\]
实际标量算子为 \(G=g/h\)、\(L_2=\ell/h\)。

由于
\[
[d_b,e_b]|_{\mathcal H_{s-1}}=2I,\qquad U_b=0,
\]
对源 \(D_{s-1}^{-1}v\) 有
\[
\mathcal J_1D_{s-1}^{-1}v
=\frac12e_bD_{s-1}^{-1}v
=D_s^{-1}\gamma v. \tag{3.2}
\]
这是真正的最小范数原像：它在 reducing 模块内是唯一原像，而其余模块只能增加正交的范数。故
\[
g=\frac{\|D_s^{-1}\gamma v\|^2}{N_v}. \tag{3.3}
\]

为完整说明顶逆，令 \(C\) 为物理补集酉，置
\[
\pi=\prod_i z_i^{q_i}.
\]
不带权的 \((d_0^2/2)C\) 在 \(\ker d_0\cap\mathcal H_{s-1}\) 上等于
\((-1)^{s-1}I\)。确实，对固定 \((s-1)\)-子集 \(I\)，
\[
\sum_{J\cap I=\varnothing}v_J
=\sum_{R\subseteq I}(-1)^{|R|}\sum_{J\supseteq R}v_J
=(-1)^{s-1}v_I.
\]
当 \(|R|<s-1\) 时，内和由 \(d_0v=0\) 为零；只剩 \(R=I\)。

完整 \(d_0^2:\mathcal H_{s+1}\to\mathcal H_{s-1}\) 可逆。一个直接证明是由原 commutator 算得
\[
d_0^2e_0^2=e_0^2d_0^2+8e_0d_0+4I
\quad\hbox{于 }\mathcal H_{s-1}.
\]
其右边至少为 \(4I\)，而两层维数相同。带权 \(d_b^2\) 是其两侧正对角变换，同样可逆。因此上述原像就是完整顶 MP 逆，且
\[
\mathcal J_2D_{s-1}^{-1}v
=(-1)^{s-1}D_{s+1}^{-1}Cv
=(-1)^{s-1}\pi^{-1/2}CD_{s-1}v.
\]
从而
\[
\boxed{\ell=\pi^{-1}\frac{\|D_{s-1}v\|^2}{N_v}.} \tag{3.4}
\]
上述论证也适用于 \(Q=0\)：此时是两个等权有效位的真一维源。

因 \(A_0=0\)，由 (1.1) 得实际标量传输
\[
\boxed{
\mathcal T
=\frac{h\ell/g-2g}{\sqrt{h\ell}}
=\frac{r-2}{\sqrt r},\qquad
r=\frac{h\ell}{g^2},\qquad
\Phi=\frac{(r-2)^2}{r}.
} \tag{3.5}
\]
因此需要证明 \(1\le r\le4\)。

## 4. 任意多权的精确 Beta 积分

置
\[
F_{\boldsymbol z}(t)=\prod_{i=1}^m(1-t+z_it)^{q_i},\qquad 0\le t\le1,
\]
\[
A=\int_0^1t^2F_{\boldsymbol z}(t)\,dt,\quad
B=\int_0^1(1-t)^2F_{\boldsymbol z}(t)\,dt,\quad
C_1=\int_0^1t(1-t)F_{\boldsymbol z}(t)\,dt. \tag{4.1}
\]
这里 \(C_1\) 是一个正标量积分，不表示任何 primitive 精度矩阵。

由 (2.1)、(2.3)，
\[
N(\boldsymbol z):=\|D_{s-1}v\|^2
=\sum_{0\le k_i\le q_i}
\frac{\prod_i\binom{q_i}{k_i}z_i^{k_i}}
{\binom{Q+2}{Q-\sum_i k_i}}. \tag{4.2}
\]
使用
\[
\binom n r^{-1}=(n+1)\int_0^1t^r(1-t)^{n-r}\,dt
\]
并把 \(t\) 换成 \(1-t\)，得到
\[
\boxed{N(\boldsymbol z)=(Q+3)A,\qquad N_v=(Q+3)/3.} \tag{4.3}
\]
同样，
\[
\|D_s\gamma v\|^2=(Q+3)C_1. \tag{4.4}
\]
又
\[
F_{\boldsymbol z^{-1}}(t)=\pi^{-1}F_{\boldsymbol z}(1-t).
\]
把 (4.3)–(4.4) 代入 (3.1)、(3.3)、(3.4)，得到全部真实量的共同规范：
\[
\boxed{
h=3\pi^{-1}B,\qquad
g=3\pi^{-1}C_1,\qquad
\ell=3\pi^{-1}A.
} \tag{4.5}
\]
故
\[
\boxed{r=AB/C_1^2.} \tag{4.6}
\]
这些相同前因子来自完整物理源，不是分别缩放三个 Gram。

\(F_{\boldsymbol z}\) 严格正且对数凹，因为
\[
(\log F_{\boldsymbol z})''(t)
=-\sum_i\frac{q_i(z_i-1)^2}{(1-t+z_it)^2}\le0. \tag{4.7}
\]

## 5. 自足的对数凹反向 Cauchy 不等式

**引理。** 若 \(F\) 是 \([0,1]\) 上严格正、连续、对数凹的函数，则
\[
\boxed{
\left(\int_0^1t^2F\right)
\left(\int_0^1(1-t)^2F\right)
\le4\left(\int_0^1t(1-t)F\right)^2.
} \tag{5.1}
\]
等号当且仅当 \(F\) 为常数。

**第一步：在固定均值下由截断指数支配方差。**
归一化为概率密度 \(f=F/\int F\)，记
\[
\mu=\mathbb E_fT,\qquad u=\mu(1-\mu),\qquad v=\operatorname{Var}_fT.
\]
严格正密度给 \(0<\mu<1\)、\(0<v<u\)。唯一的截断指数密度
\[
g_\lambda(t)=\frac{e^{\lambda t}}{\int_0^1e^{\lambda r}\,dr}
\]
具有同一均值 \(\mu\)：其均值对 \(\lambda\) 的导数是严格正方差，并在
\(\lambda\to-\infty,+\infty\) 时分别趋向 \(0,1\)。

\(\log(f/g_\lambda)\) 凹，故 \(f-g_\lambda\) 的正集合是一个区间。如果二者不相同，同质量、同均值排除只有一次变号：若变号点为 \(a\)，则
\((t-a)(f-g_\lambda)\) 将同号且不恒零，其积分却必须为零。因此存在两端点 \(a<b\)，使差具有
\[
-,\quad +,\quad -
\]
的符号次序；允许中间或边界有零区间。于是
\[
\int_0^1(t-a)(t-b)(f-g_\lambda)\,dt<0.
\]
常数和一次项因同质量、同均值消掉，所以
\[
\boxed{\operatorname{Var}_fT\le\operatorname{Var}_{g_\lambda}T,} \tag{5.2}
\]
除非 \(f=g_\lambda\)，否则严格。这个论证直接证明所需二阶矩支配，不调用外部凸序定理。

**第二步：固定均值时目标随方差严格递减。**
对于任意具有均值 \(\mu\)、方差 \(v\) 的概率密度，
\[
\begin{aligned}
\mathbb ET^2&=\mu^2+v,\\
\mathbb E(1-T)^2&=(1-\mu)^2+v,\\
\mathbb ET(1-T)&=u-v.
\end{aligned}
\]
因此
\[
4[\mathbb ET(1-T)]^2-\mathbb ET^2\,\mathbb E(1-T)^2
=3u^2-(1+6u)v+3v^2. \tag{5.3}
\]
它对 \(v\in[0,u]\) 的导数为
\[
-1-6u+6v\le-1<0.
\]
由 (5.2)，只需证明截断指数密度的 (5.1)。

**第三步：指数族的完整正幂级数。**
直接使用未归一函数 \(e^{\lambda t}\)，记对应积分为
\(A_\lambda,B_\lambda,C_\lambda\)。当 \(\lambda\ne0\) 时，置 \(E=e^\lambda\)，有
\[
\lambda^3A_\lambda=E(\lambda^2-2\lambda+2)-2,
\]
\[
\lambda^3B_\lambda=2E-(\lambda^2+2\lambda+2),
\]
\[
\lambda^3C_\lambda=E(\lambda-2)+\lambda+2.
\]
直接展开并配对 \(e^\lambda,e^{-\lambda}\)，得到
\[
\begin{aligned}
\lambda^6e^{-\lambda}
(4C_\lambda^2-A_\lambda B_\lambda)
={}&4(\lambda^2+6)\cosh\lambda
-24\lambda\sinh\lambda\\
&+\lambda^4+8\lambda^2-24\\
={}&\sum_{j\ge4}
\frac{8(2j-1)(j-3)}{(2j)!}\lambda^{2j}>0.
\end{aligned} \tag{5.4}
\]
所有级数系数均非负，且 \(j=4\) 项对 \(\lambda\ne0\) 严格正。
\(\lambda=0\) 时为均匀密度，
\(A_0=B_0=1/3,C_0=1/6\)，恰取等。

若 \(f\ne g_\lambda\)，(5.2) 和 (5.3) 已给严格不等式；若
\(f=g_\lambda\) 且 \(\lambda\ne0\)，(5.4) 给严格不等式。因此只有常数密度取等，引理证毕。

该自足证明的指数族恒等式由并行 boundary 核查提供；正文已把全部代数和符号机制写出，无需引用尚未证明的新文献。

## 6. 相位结论、严格性及实际组模块

Cauchy–Schwarz 对函数 \(t\sqrt F\)、\((1-t)\sqrt F\) 给
\[
AB>C_1^2,
\]
因为严格正密度上两个函数不成比例。结合引理，
\[
\boxed{1<r\le4.} \tag{6.1}
\]
于是
\[
1-\Phi
=\frac{(r-1)(4-r)}r\ge0,
\]
证明 (1.1)。

若至少一个非空小组满足 \(z_i\ne1\)，由 (4.7) \(F_{\boldsymbol z}\) 非常数，故
\(1<r<4\)，实际相位严格小于 \(1\)。若所有非空小组权都与主组相同，则
\(F=1\)、\(r=4\)、\(\mathcal T=1\)、\(\Phi=1\)。这也包含 \(Q=0\) 的永久两有效位等号模块。

更一般地，原等权组 \(g\) 的大小为 \(n_g\)，选定一个组内 unweighted primitive 次数 \(a_g\)，其有效长度为
\[
q_g=n_g-2a_g,\qquad j_g=q_g/2.
\]
该原组的每个正交 ladder 均等距于 \(q_g\) 个相同权位的对称模块；\(d_b,e_b\)、伴随及完整 MP 逆均保持此分解。因此，若某组 \(g_0\) 满足
\[
\boxed{j_{g_0}=1+\sum_{g\ne g_0}j_g,} \tag{6.2}
\]
则整个对应 tensor 模块（包括其全部组内 primitive 多重性）已由本稿证明
\(\Phi\preceq I\)。除去实际有效权全相同的情形，每个非零低源副本都严格。

这里其余组数、有效长度和正权均任意。含中央硬源的 spin 三角区不满足
(6.2)，仍须保留其完整回归 Schur；本稿不取消那部分困难。

