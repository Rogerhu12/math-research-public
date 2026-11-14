# 平衡 star 的真实后验分数：互逆权完整列预算

本稿继续同一完整物理源的 Beta–binomial 表达。它给两个真实后验分数列的统一互逆权预算，保留两个端点的互补；不对各自未加权的回归残差声称统一界，也不把下面的混合列替代最终相位交叉。

## 1. 同一概率、物理源和端点

取整数 \(q_i\ge1\)、正数 \(z_i>0\)，令 \(Q=\sum_iq_i\ge1\)。采用[完整平衡 star 源稿](2026-11-14-balanced-star-full-source-beta-binomial-phase-transport-789f-next.md)中的同一联合概率：
\[
\rho(t)=\frac{\prod_i(1-t+z_it)^{q_i}}{\int_0^1\prod_i(1-u+z_iu)^{q_i}\,du},\qquad
K_i\mid T=t\sim\operatorname{Binomial}\!\left(q_i,\frac{z_it}{1-t+z_it}\right),
\]
条件下各 \(K_i\) 独立。记
\[
X_i=K_i/q_i,\qquad S=\sum_iK_i,\qquad
G=\operatorname{Cov}\(X\),
\]
\[
H=\mathbb E\!\left[\frac{1-T}{T}XX^*\right],\qquad
L=\mathbb E\!\left[\frac{T}{1-T}(\mathbf1-X)(\mathbf1-X)^*\right]. \tag{1.1}
\]
完整源稿已经识别真实物理源度量、中间 MP Gram 和顶部 MP Gram 分别为 \(cH,cG,cL\)，其中同一 \(c>0\) 可在所有二次型中约去。这里保持整个组数维源，不限制到某一个对称向量。

后验恰为 \(T\mid K\sim\operatorname{Beta}(S+1,Q-S+1)\)。因此定义
\[
a_s=\frac{Q-s+1}{s}\quad(s\ge1),\qquad
b_s=\frac{s+1}{Q-s}\quad(s\le Q-1),
\]
及真正有限的列
\[
\overline F=a_SX,\qquad \overline B=b_S(\mathbf1-X). \tag{1.2}
\]
在 \(S=0\) 时把整个 \(\overline F\) 列定义为零；在 \(S=Q\) 时把整个 \(\overline B\) 列定义为零。这与对应原后验条件期望一致，因为这些事件上分别 \(X=0\) 或 \(\mathbf1-X=0\)。不单独对无意义的端点分母赋值。

于是
\[
H=\mathbb E[a_SXX^*],\qquad
L=\mathbb E[b_S(\mathbf1-X)(\mathbf1-X)^*], \tag{1.3}
\]
端点仍按整个被乘列为零理解。

## 2. 互逆权的全源统一预算

定义在全部 \(0\le s\le Q\) 上均有限且严格正的
\[
\tau_s=\frac{s+1}{Q-s+1}. \tag{2.1}
\]
则对任意组数、全部独立正权及全部组长，
\[
\boxed{\mathbb E[\tau_S\overline F\overline F^*]\preceq2H,
\qquad
\mathbb E[\tau_S^{-1}\overline B\overline B^*]\preceq2L.} \tag{2.2}
\]

证明是完整矩阵的逐样本比较。在 \(S\ge1\) 的非零第一列上，
\[
\tau_S a_S=\frac{S+1}{S}\le2,
\]
故 \(\tau_Sa_S^2XX^*\preceq2a_SXX^*\)。在 \(S=0\) 两边该列均为零。另一列同理由
\[
\tau_S^{-1}b_S=\frac{Q-S+1}{Q-S}\le2\qquad(S\le Q-1)
\]
得到，\(S=Q\) 时该列为零。取期望即得 (2.2)。这里每一不等式均保留非对角项和所有共同源方向。

令
\[
M=\mathbb E[\overline F\overline B^*].
\]
同一个概率空间中的两个列 \(\tau_S^{1/2}\overline F\)、\(\tau_S^{-1/2}\overline B\) 的 Gram 为正，结合 (2.2) 得
\[
\boxed{\begin{pmatrix}2H&M\\M^*&2L\end{pmatrix}\succeq0.} \tag{2.3}
\]
等价地，对全部源向量 \(u,v\)，
\[
|u^*Mv|\le2\sqrt{u^*Hu}\sqrt{v^*Lv},\qquad
\|H^{-1/2}ML^{-1/2}\|\le2. \tag{2.4}
\]
同乘 \(c\) 后，(2.3) 也是原物理源的完整正块。

两个单侧预算中的常数 \(2\) 已在本类的 \(Q=1\) 情形取到，因而在允许全部 \(Q\ge1\) 时不能减小。

## 3. 仅混合列的稍强常数

当 \(Q\ge2\) 时，还可单独对 \(M\) 保留准确的内点乘积。对于 \(1\le s\le Q-1\)，
\[
a_sb_s=1+\frac{Q+1}{s(Q-s)}\le\frac{2Q}{Q-1}. \tag{3.1}
\]
令 \(\eta_Q=\sqrt{2Q/(Q-1)}\le2\)。在每个内点样本上，
\[
\begin{pmatrix}
\eta_Q a_sXX^*&a_sb_sX(\mathbf1-X)^*\\
a_sb_s(\mathbf1-X)X^*&\eta_Qb_s(\mathbf1-X)(\mathbf1-X)^*
\end{pmatrix}\succeq0, \tag{3.2}
\]
因为该矩阵是标量正块
\(\left(\begin{smallmatrix}\eta_Qa_s&a_sb_s\\a_sb_s&\eta_Qb_s\end{smallmatrix}\right)\)
沿两列的合同，行列式非负恰由 \(a_sb_s\le\eta_Q^2\) 保证。两个端点混合列为零，剩余对角项仍为正。

取期望得
\[
\boxed{\begin{pmatrix}\eta_QH&M\\M^*&\eta_QL\end{pmatrix}\succeq0.} \tag{3.3}
\]
这只加强混合列预算，并不加强 (2.2) 中已最优的统一单侧常数。

## 4. 准确范围

实际相位仍为
\[
J=HG^{-1}L-2G-(2\mathbb EX-\mathbf1)(2\mathbb EX-\mathbf1)^*,
\]
目标仍是 \(J^*L^{-1}J\preceq\kappa H\)，不能把 \(J\) 换为 (M^*) 或 \(M\)。

(2.2) 保留互逆权的两端互补。它既不声称未加权 \(\overline F,\overline B\) 的残差范数分别有统一界，也不声称真实投影到全部常数和线性 \(X\) 的回归在这两个互逆加权空间中自动有界。后者必须与原来的均值和总数方向共同处理；直接拆成三个独立范数会失去这里的预算。

本稿的新结论是 (2.2)–(2.4) 及 (3.3)。全部概率和物理源识别沿用已证明的完整平衡 star 稿；一般相位费用尚未由本稿支付。
