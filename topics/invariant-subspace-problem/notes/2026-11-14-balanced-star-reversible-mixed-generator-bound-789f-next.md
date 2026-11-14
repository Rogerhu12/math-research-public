# 平衡 star：两个真实可逆增删生成元的统一混合预算

本稿在完整 Beta–binomial 物理源上构造两个可逆增删生成元。它们的混合二次型可准确消为单位阵减一个固定大小子集的交换矩阵。由完整 Boolean 创建、删除的同一 Cauchy–Schwarz 估计，得到不依赖全部独立正权和组数的范数界。最后保留真实线性回归的完整混合残差；不把全生成元乘积的界免费转给压缩后的乘积或最终相位。

## 1. 同一有限概率与记号

取 \(q_i\ge1\)、\(z_i>0\)，总长 \(Q=\sum_iq_i\ge1\)。采用[完整平衡 star 稿](2026-11-14-balanced-star-full-source-beta-binomial-phase-transport-789f-next.md)的实际联合概率。其计数边缘是
\[
\pi(k)=\frac{\prod_i\binom{q_i}{k_i}z_i^{k_i}}
{(Q+1)Z_F\binom Qs},\qquad s=\sum_i k_i,
\quad
Z_F=\int_0^1\prod_i(1-t+z_it)^{q_i}\,dt. \tag{1.1}
\]
记
\[
X_i=K_i/q_i,\quad S=\sum_iK_i,\quad
m=\mathbb EX,\quad n=\mathbf1-m,\quad
G=\operatorname{Cov}(X),
\]
\[
Z=\operatorname{diag}(z_i),\quad
D=\operatorname{diag}(q_i^{-1}),\quad
D_m=\operatorname{diag}(m_i/q_i),\quad
D_n=\operatorname{diag}(n_i/q_i),
\quad D_m+D_n=D. \tag{1.2}
\]
所有原物理源、MP Gram 和顶部 Gram 仍是同一源中的 \(cH,cG,cL\)，其中
\[
H=\mathbb E[a_SXX^*],\quad
L=\mathbb E[b_S(\mathbf1-X)(\mathbf1-X)^*],
\]
\[
a_s=(Q-s+1)/s\quad(s\ge1),\qquad
b_s=(s+1)/(Q-s)\quad(s\le Q-1). \tag{1.3}
\]
定义有限列 \(\overline F=a_SX\)、\(\overline B=b_S(\mathbf1-X)\)。在 \(S=0\) 把整个第一列取零，在 \(S=Q\) 把整个第二列取零；不分别解释零端点的分母。这里两个列与[互逆权预算稿](2026-11-14-balanced-star-reciprocal-weight-score-budget-789f-next.md)完全相同。

另记真实两个端点参数
\[
\alpha=Z_F^{-1},\qquad
\beta=Z_F^{-1}\prod_i z_i^{q_i}.
\]
由 (1.1)，
\[
\mathbb P\(S=0\)=\frac\alpha{Q+1},\qquad
\mathbb P\(S=Q\)=\frac\beta{Q+1}. \tag{1.4}
\]

## 2. 两个可逆生成元与完整 Dirichlet 压缩

在全部计数状态上定义
\[
\begin{aligned}
\mathcal L_+f(k)
={}&\sum_i k_i\,[f(k-e_i)-f(k)]\\
&+\sum_i z_i(q_i-k_i)b_s\,[f(k+e_i)-f(k)],
\end{aligned} \tag{2.1}
\]
\[
\begin{aligned}
\mathcal L_-f(k)
={}&\sum_i(q_i-k_i)\,[f(k+e_i)-f(k)]\\
&+\sum_i z_i^{-1}k_i a_s\,[f(k-e_i)-f(k)].
\end{aligned} \tag{2.2}
\]
边界上没有相应边的项直接省略。令 \(\mathcal A_\pm=-\mathcal L_\pm\)。

相邻状态的真实概率比为
\[
\frac{\pi(k+e_i)}{\pi(k)}
=z_i\frac{q_i-k_i}{k_i+1}\,b_s. \tag{2.3}
\]
因为 \(a_{s+1}=b_s^{-1}\)，(2.3) 分别验证两个链的详细平衡。因此 \(\mathcal A_\pm\) 都是有限维 \(L^2(\pi)\) 上非负、自伴且消去常数的真实算子。

在整个线性观察向量上，逐坐标准确有
\[
\boxed{\mathcal A_+X=X-Z\overline B,\qquad
\mathcal A_-X=Z^{-1}\overline F-(\mathbf1-X).} \tag{2.4}
\]
每条边只有相应坐标的 \(X_i\) 改变 \(1/q_i\)。用下行边写第一条 Dirichlet 形式、上行边写第二条，得到完整矩阵身份
\[
\boxed{
\mathbb E[(\mathcal A_+X)(X-m)^*]=D_m,\qquad
\mathbb E[(\mathcal A_-X)(X-m)^*]=D_n.
} \tag{2.5}
\]
这是所有原线性源的同一压缩，非仅逐个对角估计。

## 3. 混合生成元的准确消去

定义
\[
\Delta=(Q+1)\mathbb E\!\left[
\frac{X(\mathbf1-X)^*}{S(Q-S)}\,\mathbf1_{\{1\le S\le Q-1\}}
\right]. \tag{3.1}
\]
当 \(Q=1\) 时 \(\Delta=0\)。内点上
\[
a_sb_s=1+\frac{Q+1}{s(Q-s)},
\]
而两个端点的 \(X(\mathbf1-X)^*\) 都为零，所以
\[
\mathbb E[\overline F\overline B^*]
=mn^*-G+\Delta. \tag{3.2}
\]

条件于 (T=t)，不同组的均值满足
\[
p_i(t)(1-p_j(t))
=\frac{z_i t(1-t)}{(1-t+z_it)(1-t+z_jt)}.
\]
因此（对角项自动相同）
\[
Z^{-1}(mn^*-G)Z=nm^*-G. \tag{3.3}
\]
也可直接由固定大小子集的交换详细平衡得到同式。

由 (2.4)–(2.5)，
\[
Z^{-1}H=D_n+nm^*-G,\qquad
LZ=D_m+nm^*-G. \tag{3.4}
\]
现在完整展开同一个混合乘积，并仅使用 (3.2)–(3.4)：
\[
\begin{aligned}
\mathbb E[(\mathcal A_-X)(\mathcal A_+X)^*]
&=Z^{-1}H+LZ-(nm^*-G)
  -Z^{-1}\mathbb E[\overline F\overline B^*]Z\\
&=\boxed{D-Z^{-1}\Delta Z}. 
\end{aligned} \tag{3.5}
\]
全部均值、对角 binomial 噪声和内点后验修正都已保留。

## 4. 完整 Boolean 层的一条无权谱估计

先证明一个独立的完整物理估计。令 \(\psi\) 是 \(Q\) 位 Boolean 空间第 \(s\) 层的单位向量，\(1\le s\le Q-1\)。定义无对角一粒子矩阵
\[
O_{ij}=\langle\psi,E_i^*E_j\psi\rangle\quad(i\ne j),
\qquad O_{ii}=0.
\]
则
\[
\boxed{O\preceq\frac{s(Q-s)}Q I.} \tag{4.1}
\]

证明：对单位系数向量 \(v\in\mathbb C^Q\)，令
\[
B_v=\sum_i v_iE_i,\qquad
a=\sum_i|v_i|^2\langle\psi,n_i\psi\rangle.
\]
在每个 \(\(s-1\)\)-子集的删除行上用 Cauchy–Schwarz，然后把同一个原 \(s\)-子集的贡献合并，得
\[
\|B_v\psi\|^2\le s-\(s-1\)a.
\]
所以 \(v^*Ov\le s(1-a)\)。对补集中的创建行做完全相同的估计，得
\[
\|B_v^*\psi\|^2\le1+(Q-s-1)a,
\]
所以同一无对角二次型还满足 \(v^*Ov\le(Q-s)a\)。合并为
\[
v^*Ov\le\min\{s(1-a),(Q-s)a\}\le\frac{s(Q-s)}Q.
\]
这证明 (4.1)。估计没有压缩 primitive，也不涉及 MP 逆。

## 5. 实际交换矩阵的统一范数界

先把各组拆成 \(Q\) 个真实独立位，重复相同的组权。条件于 (S=s)，子集概率为
\[
\mu_s\\(I\)=\frac{z_I}{e_s(z)},\qquad |I|=s.
\]
取完整第 \(s\) 层单位纯态
\[
\psi_s=\sum_{|I|=s}\sqrt{\mu_s\\(I\)}\,e_I.
\]
不同位 \(i,j\) 满足
\[
\mathbb E[X_i(1-X_j)\mid S=s]
=\frac{z_i e_{s-1}(z_{\widehat {ij}})}{e_s(z)},
\]
\[
(O_s)_{ij}
=\frac{\sqrt{z_iz_j}\,e_{s-1}(z_{\widehat {ij}})}{e_s(z)}.
\]
故完整单个位版本的对称化交换矩阵准确是
\[
Z^{-1/2}\Delta Z^{1/2}
=(Q+1)\sum_{s=1}^{Q-1}\frac{\mathbb P(S=s)}{s(Q-s)}O_s. \tag{5.1}
\]
所有矩阵元均非负。由 (4.1)，
\[
Z^{-1/2}\Delta Z^{1/2}\preceq c_Q I,\qquad
c_Q=\frac{Q+1}{Q}\mathbb P(1\le S\le Q-1)
=1+\frac{1-\alpha-\beta}{Q}. \tag{5.2}
\]
对称非负矩阵的谱半径等于其最大特征值，所以 (5.2) 同时给完整算子范数界。

回到组源。令 \(V:\mathbb C^{\#\mathrm{groups}}\to\mathbb C^Q\) 在第 \(i\) 组的每一位取系数 \(1/\sqrt{q_i}\)；这是固定等距嵌入。组内计数定义 \(X_i=K_i/q_i\) 表明
\[
N:=D^{-1/2}Z^{-1/2}\Delta Z^{1/2}D^{-1/2}
\]
恰为 (5.1) 的 \(V^*(\cdot)V\) 压缩。尤其组对角 \(X_i(1-X_i)\) 对应组内不同物理位的全部交叉，并没有丢掉这些项。因此
\[
\boxed{N=N^*,\quad N\text{ 逐项非负},\quad
\|N\|\le c_Q\le1+\frac1Q.} \tag{5.3}
\]
当 \(Q=1\) 时直接为 \(N=0,c_Q=0\)，与同式一致。

把 (3.5) 在两个真实列上分别乘 (D^{-1/2}Z^{1/2})、(D^{-1/2}Z^{-1/2})，得到
\[
\boxed{
\mathbb E\!\left[
(D^{-1/2}Z^{1/2}\mathcal A_-X)
(D^{-1/2}Z^{-1/2}\mathcal A_+X)^*
\right]=I-N.
} \tag{5.4}
\]
于是准确有
\[
\boxed{
\frac{\alpha+\beta-1}{Q}I
\preceq I-N
\preceq\left(2+\frac{1-\alpha-\beta}{Q}\right)I,
\qquad
\|I-N\|\le2+\frac1Q.
} \tag{5.5}
\]
这是真实全部源的统一混合生成元预算；在 \(Q=1\) 时 (5.4) 直接等于 \(I\)。

## 6. 保留共同回归后的准确余项

令 \(C=X-m\)，\(P_C\) 是 \(L^2(\pi)\) 中到全部线性中心源的正交投影。由 (2.5)，
\[
P_C(\mathcal A_-X)=D_nG^{-1}C,\qquad
P_C(\mathcal A_+X)=D_mG^{-1}C.
\]
因此真实共同残差的混合 Gram 恰为
\[
\boxed{
\mathbb E\!\left[
(I-P_C)\mathcal A_-X\,
((I-P_C)\mathcal A_+X)^*
\right]
=D-Z^{-1}\Delta Z-D_nG^{-1}D_m.
} \tag{6.1}
\]
(6.1) 是混合 Gram，不是一个向量与自身的平方，不能免费宣称它非负，也不能将 (5.5) 的界转移到 \(D_nG^{-1}D_m\)。其均值及端点项仍须与完整相位
\[
J=HG^{-1}L-2G-(2m-\mathbf1)(2m-\mathbf1)^*,\qquad
J^*L^{-1}J\preceq\kappa H
\]
共同处理。本文没有支付该最终不等式。

本稿新增的是两个真实可逆链、精确消去 (3.5)，及由完整物理层 (4.1) 得出的全源统一预算 (5.3)–(5.5)；(6.1) 记录继续研究时必须保留的实际余项。
