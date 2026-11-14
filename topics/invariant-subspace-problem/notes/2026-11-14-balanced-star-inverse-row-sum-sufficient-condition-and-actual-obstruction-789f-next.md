# 平衡 star 的逆协方差行和：一个准确充分条件及真实两权障碍

日期：2026-11-14；工作标识：789f。

本附录只处理均值混合量的一条充分路线。它不把逆协方差的逐项符号当作原相位目标，也不把以下反例当作相位反例。宏观渐近输入来自已经完整证明的[任意多个宏观小组内峰全源相位稿](2026-11-14-balanced-star-macroscopic-interior-full-phase-projection-limit-789f-next.md)的式 (4.5)–(4.6)；本附录不重复登记该渐近定理。

## 1. 一个对二值源成立的条件引理

令 \(X=(X_1,\ldots,X_Q)\in\{0,1\}^Q\)，记
\[
 m=\mathbb EX,\qquad n=\mathbf1-m,\qquad
 G=\operatorname{Cov}(X)>0.
\]
假设 \(G\) 逐项非负，并且
\[
                    c=G^{-1}\mathbf1\geq0
                    \quad\hbox{逐项}.                    \tag{1.1}
\]
则
\[
                         m^*G^{-1}n\leq Q.                \tag{1.2}
\]
因此在使用 \(\eta=m^*G^{-1}n-1\) 的记号时，(1.1) 足以推出 \(\eta\leq Q-1\)。

**证明。** 置 \(A=G^{-1}\)、\(D_c=\operatorname{diag}(c)\)。先证明
\[
                A-D_c\succeq0,\qquad (A-D_c)\mathbf1=0.  \tag{1.3}
\]
矩阵 \(B=D_c^{1/2}GD_c^{1/2}\) 对称、半正定且逐项非负。在 \(c_i>0\) 的指标集上，\(\sqrt c\) 是严格正的向量，且由 \(Gc=\mathbf1\) 得
\[
                         B\sqrt c=\sqrt c.
\]
其余行列为零。故在非零指标集上，\(B\) 与一个行随机的非负矩阵相似；其谱半径为 \(1\)。于是 \(0\preceq B\preceq I\)。\(G^{1/2}D_cG^{1/2}\) 与 \(B\) 有相同的非零特征值，因此也不超过 \(I\)；合同即得 (1.3) 的正性。零向量身份直接来自 \(A\mathbf1=c=D_c\mathbf1\)。这一论证允许 \(c\) 有零分量，不需要偷换为严格正的情形。

定义真实二值距离矩阵
\[
 W_{ij}=\frac12\mathbb E(X_i-X_j)^2
       =\frac{m_i+m_j}{2}-\mathbb E(X_iX_j).               \tag{1.4}
\]
它满足 \(W_{ii}=0\)，且对 \(v\perp\mathbf1\)，
\[
                    v^*Wv=-\mathbb E|v^*X|^2\leq0.        \tag{1.5}
\]
由 (1.3)，\(A-D_c\) 是支撑在 \(\mathbf1^\perp\) 上的半正定矩阵；故 (1.5) 给
\[
 \operatorname{tr}(AW)
 =\operatorname{tr}((A-D_c)W)\leq0,                       \tag{1.6}
\]
其中使用了 \(W_{ii}=0\)。另一方面，\(\mathbb E(XX^*)=G+mm^*\)，所以
\[
 \begin{aligned}
 \operatorname{tr}(AW)
 &=m^*A\mathbf1-\operatorname{tr}(AG)-m^*Am\\
 &=m^*An-Q.
 \end{aligned}                                           \tag{1.7}
\]
(1.6)–(1.7) 就是 (1.2)。\(\square\)

这是一个只涉及真实向量 \(c\) 的充分条件。证明只用了 \(G^{-1}\mathbf1\)、由它产生的 (1.3)，以及二值距离的共同二次型；没有从一般正相关或 MTP2 免费推出 (1.1)，也没有断言它与逆协方差的非对角元符号条件之间存在蕴含关系。

## 2. 实际平衡 star 的逆行和仍可为负

取 \(Q\to\infty\) 沿 \(8\) 的正整数倍，两个小组为
\[
 q_1=\frac{3Q}{8},\qquad q_2=\frac{5Q}{8},\qquad
 z_1=3,\qquad z_2=\frac13.                                \tag{2.1}
\]
主组仍为长度 \(Q\)、权平方 \(1\) 的原平衡 star 主组。全部小位展开后，是 \(Q\) 个真实二值坐标：前 \(q_1\) 位权平方为 \(3\)，后 \(q_2\) 位权平方为 \(1/3\)。

其真实潜变量密度为
\[
 \rho_Q(t)=Z_{F,Q}^{-1}
       (1+2t)^{3Q/8}(1-2t/3)^{5Q/8},\qquad 0<t<1,         \tag{2.2}
\]
给定 \(T=t\) 后，各位独立，成功率分别为
\[
 p_1(t)=\frac{3t}{1+2t},\qquad
 p_2(t)=\frac{t/3}{1-2t/3}.
\]
这不是任意替换的混合密度。

记
\[
 \omega=(3/8,5/8)^*,\qquad
 \ell(t)=\tfrac38\log(1+2t)+\tfrac58\log(1-2t/3).
\]
有唯一严格内峰
\[
 t_0=\frac14,\qquad
 p(t_0)=\left(\frac12,\frac1{10}\right)^*,\qquad
 a=t_0(1-t_0)=\frac3{16},\qquad
 -\ell''(t_0)=\frac{16}{15}>0.                            \tag{2.3}
\]
例如 \(\ell'(t_0)=\frac38\frac43+\frac58(-\frac45)=0\)。端点条件也严格成立：\(\sum_i\omega_i z_i=4/3>1\)、\(\sum_i\omega_i z_i^{-1}=2>1\)。

令 \(X_i=K_i/q_i\) 为两组的真实平均，\(G_{\rm grp,Q}=\operatorname{Cov}(X_1,X_2)\)。既有完整内峰定理给
\[
 G_{\rm grp,Q}^{-1}
 =Q\left[\operatorname{diag}\!\left(
            \frac{\omega_i}{p_i(1-p_i)}\right)
                     -\frac{\omega\omega^*}{a}\right]+O(1)
 =Q\begin{pmatrix}
        3/4&-5/4\\[-1mm]
        -5/4&175/36
    \end{pmatrix}+O(1).                                  \tag{2.4}
\]
因而
\[
          G_{\rm grp,Q}^{-1}\mathbf1
            =Q\left(-\frac12,\frac{65}{18}\right)^*+O(1).
                                                                  \tag{2.5}
\]
首分量在所有充分大的合法 \(Q\) 上严格为负。

## 3. 展开全部真实二值源；不是先压缩再求逆

令 \(G_{\rm full,Q}\) 是上述全部 \(Q\) 个二值坐标的完整协方差。它因全支撑而严格正定。令
\(S:\mathbb R^2\to\mathbb R^Q\) 将一个两分量向量分别重复到两个组，\(D_q=\operatorname{diag}(q_1,q_2)\)。组内置换不变性给准确身份
\[
 G_{\rm full,Q}S=S G_{\rm grp,Q}D_q.                      \tag{3.1}
\]
并且 \(G_{\rm full,Q}^{-1}\mathbf1\) 本身组内恒定，因为完整协方差及 \(\mathbf1\) 都保每个组的置换。故完整逆严格满足
\[
 G_{\rm full,Q}^{-1}\mathbf1
       =S D_q^{-1}G_{\rm grp,Q}^{-1}\mathbf1.              \tag{3.2}
\]
这里用的是完整协方差的一个真正 reducing 模块；没有把不变源之外的 nuisance 先删掉后冒称完整逆。

将 (2.5) 代入，前组每一位和后组每一位分别满足
\[
 \boxed{
 (G_{\rm full,Q}^{-1}\mathbf1)_j
   =\begin{cases}
       -4/3+O(Q^{-1}),&j\text{ 在第一组},\\[1mm]
       52/9+O(Q^{-1}),&j\text{ 在第二组}.
     \end{cases}}                                        \tag{3.3}
\]
因此 (1.1) 在实际完整二值源上也不普适。没有使用浮点近零或病态矩阵来判定负号。

## 4. 已排与未排的范围

本附录排除了以 \(G^{-1}\mathbf1\geq0\) 作为所有权的共同入口。它没有否定 \(m^*G^{-1}n\leq Q\) 本身，更没有否定
\[
 J^*L^{-1}J\preceq\kappa H,\qquad
 J=HG^{-1}L-2G-(2m-\mathbf1)(2m-\mathbf1)^*.
\]
(2.1) 是已经证明相位常数 \(1\) 的两权类中的实际模型；这里的逆行和失败与该相位界相容。后续仍需保留原 \(q\) 方向、均值项和全部共同 Schur，不能再用逐项逆符号代替这一联合预算。
