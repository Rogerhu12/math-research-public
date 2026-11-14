# 六位三对独立正权的完整偶相位界

本稿证明实际六位平方权
\[
(a,a,b,b,c,c),\qquad a,b,c>0
\]
的**整个九维低 primitive 源**满足 \(\Phi\preceq I\)。真正新的部分是三组都取 spin \(1\) 时的完整三维非交换源；其中央硬源为一维，使用完整真实回归后给出一个精确整数多项式正系数证书。

这不是把 Chebyshev 根条件失效解释成相位反例，也没有以浮点样本代替正性。证书保留全部三个独立权值、所有三维交叉项、源度量及正确非交换次序。

## 1. 原模型与全部九维源的分解

令六位 lowering 与 reciprocal raising 为
\[
d_b=\sum_i b_iE_i,\qquad e_b=\sum_i b_i^{-1}E_i^*,
\quad b=(\sqrt a,\sqrt a,\sqrt b,\sqrt b,\sqrt c,\sqrt c).
\]
实际源 \(V_b=\ker d_b\cap\mathcal H_2\) 的维数是 \(15-6=9\)。目标仍为
\[
\Phi=H_0^*L_2^{-1}H_0,\qquad
H_0=G^{-1}L_2-2G-A_0A_0^*,
\]
其中 \(G,L_2\) 是完整 \(d_b,d_b^2/2\) 的 primitive MP Gram，
\(A_0=e_b^*|_{\ker d_b\cap\mathcal H_3}\)。

每个二位等权组正交分成 spin \(0\) 和 spin \(1\)。三组 Casimir 分解对全部实际算子及完整 MP 逆 reducing。全部低源为：

- 恰一组 spin \(1\)、其余 spin \(0\)：三个一维永久等号块；
- 恰两组 spin \(1\)：三个一维有效四位块，已由[任意两权全位数相位界](2026-11-14-two-weight-all-size-complete-even-phase-bound-789f-next.md)支付；
- 三组都为 spin \(1\)：一个三维源，本稿以下完整处理。

因此没有把原九维源仅限在一个任意测试方向。

## 2. 三维源与一维硬源的实际聚合坐标

每组是两位的对称模块。以聚合单项式 \(\alpha^{k_1}\beta^{k_2}\gamma^{k_3}\) 表示共同子集振幅，物理度量为
\[
\frac{1}{m(k)},\qquad
m(k)=\prod_{i=1}^3\binom2{k_i}.
\]
具体地，聚合系数除以 \(m(k)\) 后是每个子集的物理振幅。

次数二层按
\[
Y=(200,020,002,110,101,011)
\]
排序。固定源基为
\[
v_1=(\alpha-\gamma)^2,\quad
v_2=(\alpha-\gamma)(\beta-\gamma),\quad
v_3=(\beta-\gamma)^2.
\]
其列矩阵是
\[
V=
\begin{pmatrix}
1&0&0\\
0&0&1\\
1&1&1\\
0&1&0\\
-2&-1&0\\
0&-1&-2
\end{pmatrix}. \tag{2.1}
\]
这是一个非正交物理源基，以下始终保留度量。

中央次数三层按
\[
Z=(210,201,120,021,102,012,111)
\]
排序。硬源
\[
u=(\alpha-\beta)(\alpha-\gamma)(\beta-\gamma)
\]
的列向量为
\[
u=(1,-1,-1,1,1,-1,0)^T.
\]
完整 unweighted raising 在聚合坐标为
\[
e_0=\sum_{\xi=\alpha,\beta,\gamma}\xi(2-\xi\partial_\xi).
\]
故 \(E=e_0V\) 准确为
\[
E=
\begin{pmatrix}
2&1&0\\
0&-1&0\\
0&1&2\\
0&-1&0\\
0&1&2\\
2&1&0\\
-4&-2&-4
\end{pmatrix}. \tag{2.2}
\]
所有源列均被 \(d_0=\partial_\alpha+\partial_\beta+\partial_\gamma\) 杀死，源和硬源彼此的相关 raising 塔按实际物理内积正交。

写 \(z^k=a^{k_1}b^{k_2}c^{k_3}\)、\(\pi=a^2b^2c^2\)。所有以下矩阵具有整数多项式项：
\[
\begin{aligned}
H&=\sum_{k\in Y}\frac8{m(k)}\frac{\pi}{z^k}\,V_k^TV_k,&
L&=\sum_{k\in Y}\frac8{m(k)}z^k\,V_k^TV_k,\\
Q&=\sum_{k\in Z}\frac8{m(k)}z^k\,E_k^TE_k,&
C&=\sum_{k\in Z}\frac8{m(k)}z^k\,E_k^Tu_k,\\
M&=\sum_{k\in Z}\frac8{m(k)}z^k u_k^2.
\end{aligned} \tag{2.3}
\]
\(V_k,E_k\) 为对应行，\(C\) 是三列一列向量，\(M\) 是正标量。

作为显式核对，\[
M=4\bigl[(a+b+c)(ab+ac+bc)-3abc\bigr]>0,
\]
\[
C=
\begin{pmatrix}
8b(a^2-c^2)\\
4(a-b)(a+c)(b+c)\\
8a(c^2-b^2)
\end{pmatrix}. \tag{2.4}
\]

## 3. 完整第一逆和源度量的准确关系

用去权源 \(D^{-1}V\) 表示实际 \(V_b\)，其中次数二的 \(D\) 按 \(z^{k/2}\) 乘。对应真实二次型 \(h,\ell,q,g\) 为
\[
h=\frac{H}{8\pi},\qquad
\ell=\frac{L}{8\pi},\qquad
q=\frac{Q}{8\pi}. \tag{3.1}
\]
\(\ell\) 来自完整 \(d_b^2/2\) 的顶 MP 逆；该高度两端完整层维数相等，实际逆与 unweighted 顶补集公式相容。

中央补集把 \(k\) 变为 \((2,2,2)-k\)，物理计数不变。由 (2.2) 可直接见 \(E\) 在补集下不变，而 \(u\) 变号。因此中央逆权 Gram 是
\[
u^*W u=\frac{M}{8\pi},\qquad
E^*W E=\frac{Q}{8\pi},\qquad
E^*W u=-\frac{C}{8\pi}.
\]
完整真实硬源回归给
\[
4g=E^*WE-E^*Wu(u^*Wu)^{-1}u^*WE.
\]
置
\[
\boxed{G_0=M Q-CC^T>0,} \tag{3.2}
\]
则
\[
\boxed{g=\frac{G_0}{32\pi M}.} \tag{3.3}
\]
这里一维回归空间就是该整个模块的硬源，不是删掉了其他 nuisance 项。\(G_0>0\) 来自 \(W>0\)、\(E\) 三列独立且其像与硬源线独立的完整 Schur 正性。

将所有四个源二次型同乘正标量 \(8\pi\)，得到
\[
(h,\ell,q,g)\ \sim\ \left(H,L,Q,\frac{G_0}{4M}\right).
\]
这个共同缩放不改变相位。于是实际相位上界等价于
\[
\boxed{
\begin{pmatrix}H&J^T\\J&L\end{pmatrix}\succeq0,\qquad
J=4M H G_0^{-1}L-\frac{M Q+CC^T}{2M}.
} \tag{3.4}
\]
特别注意 \(H G_0^{-1}L\) 的次序；一般 \(J\) 不对称。

## 4. 去逆后的完整三维多项式缺陷

记
\[
d_H=\det H>0,\qquad A_H=\operatorname{adj}H.
\]
令
\[
R=8M^2d_H L-G_0A_H(MQ+CC^T), \tag{4.1}
\]
\[
\boxed{
D_{\rm raw}
=4M^2d_H\,G_0A_HL A_HG_0
-R A_HR^T.
} \tag{4.2}
\]
这些都是具体整数多项式矩阵。直接保序计算给
\[
\boxed{
D_{\rm raw}
=4M^2d_H^3
(G_0H^{-1})\,[L-JH^{-1}J^T]\,(G_0H^{-1})^T.
} \tag{4.3}
\]
证明只需
\[
2Md_H(G_0H^{-1})J=R.
\]
所有合同矩阵可逆，全部清分母因子严格为正。所以 (3.4) 与 \(D_{\rm raw}\succeq0\) 严格等价。

精确多项式除法给全部条目的共同正因子
\[
D_{\rm raw}=2^{35}a^8b^8c^8\,D(a,b,c). \tag{4.4}
\]
约去后的 \(D\) 是对称、每个非零条目齐次次数 \(24\) 的三乘三整数多项式矩阵。

## 5. 完整正系数证书

组置换是物理酉变换，故可先令 \(0<a\le b\le c\)。共同正权缩放后取
\[
a=1,\qquad b=1+x,\qquad c=1+x+y,\qquad x,y\ge0.
\]
\(D\) 的三个顺序主子式记为 \(m_1,m_2,m_3\)。由 (2.1)–(4.4) 精确重建后，其全部系数如下：

| 多项式 | 原齐次次数 | 有序替换后次数 | 非零项数 | 正系数数 | 负系数数 |
|---|---:|---:|---:|---:|---:|
| \(m_1\) | 24 | 24 | 310 | 310 | 0 |
| \(m_2\) | 48 | 47 | 1109 | 1109 | 0 |
| \(m_3\) | 72 | 70 | 2139 | 2139 | 0 |

这三组**全部整数系数**保存在配套 JSON，生成器从原物理坐标重新计算所有式，而不是输入待证主子式。按指数序列与十进制系数的规范 JSON 计算，SHA-256 分别为：

- \(m_1\)：af826668085135eafcec0ad983e3b9a1e9fdcd41ccee472cad41723110980a9d
- \(m_2\)：b35f74cedf69fbdfc510e98af6ac25ccfc0a59cf275581e3e9a9f6f4d4c91961
- \(m_3\)：74af50e2685f4dd03aa89af1fe5fd71a77d1cca7677115f466d875b8b755b6eb

对 \(x,y>0\)，每个非零正系数多项式严格为正，故 Sylvester 判据给 \(D\succ0\)。对允许的边界 \(x=0\) 或 \(y=0\)，通过从正间隙趋近和矩阵连续性得到 \(D\succeq0\)。齐次正缩放和三组物理置换覆盖全部 \(a,b,c>0\)。

结合 (4.3)–(4.4)，证明唯一新三维模块的完整相位满足
\[
\boxed{\Phi\preceq I,}
\]
且三种权值两两不同时，该三维块严格小于 \(I\)。

## 6. 全部九维结论与等号范围

与 §1 的所有其余物理块合并：

**定理。** 对任意独立 \(a,b,c>0\)，六位平方权 \((a,a,b,b,c,c)\) 的整个九维低源满足
\[
\boxed{\Phi\preceq I.}
\]
其完整等号核维数为：

- \(a,b,c\) 两两不同时，恰为 \(3\)，即三个“一个组 spin \(1\)、另两组 singlet”的永久等号源；
- 恰两个权值相等时，恰为 \(5\)。此时是原四位一组、二位一组的全两权模型，由完整等号公式
  \(m_1(4)m_0(2)+m_0(4)m_1(2)=3+2=5\) 得到；
- 三权全等时，整源 \(\Phi=I\)，核维数 \(9\)。

相同的物理组链同构也允许把本稿嵌入更大模型中相应的有效 spin \(1\) 三组模块；它并不支付较高组 spin 的所有三权块，更不等于任意正权的一般偶相位已经完成。

## 7. 可重建证书

配套文件为：

- 2026-11-14-three-pairs-all-weight-even-phase-certificate-789f-next.py
- 2026-11-14-three-pairs-all-weight-even-phase-certificate-789f-next.json

生成器只使用精确整数多项式运算，断言伴随矩阵恒等式、完整缺陷对称性、所有精确除法、三个有序主子式的正系数。完整系数重建并保存约 \(0.53\) 秒；JSON 为 \(143841\) 字节。该运算用于全部参数的符号证书，没有进行浮点权样本扫描。

一般多权相位常数、原 graph 费用和一般复 Hilbert 不变子空间问题仍未解决。

