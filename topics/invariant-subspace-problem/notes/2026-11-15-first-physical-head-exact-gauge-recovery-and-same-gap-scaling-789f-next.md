# 首物理头的完整 gauge 恢复：零源、source 与同一 gap 的准确缩放

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

状态：本稿把固定物理头 \(a=1\) 的正向恢复完全消去，准确恢复系数为
\(W_1/S_m\)。同时证明原 source、完整左最小源、真实物理 gap 及其
下降增量都按同一系数缩放。因此已有 inverse-gauge 小量及同 gap
耗散没有自动产生额外的 \(o(S_m)\)；本稿不声明原测试衰减或 \(N=M\)。

依赖：
[完整 Euler、零源反馈与 inverse-gauge](2026-11-14-fixed-physical-head-euler-feedback-and-inverse-gauge-joint-column-budget-789f-next.md)、
[source 分量额外一阶尾强度](2026-11-14-fixed-inverse-gauge-source-column-extra-tail-order-789f-next.md)、
[同一物理 gap 的内在切口耗散](2026-11-14-same-physical-gap-intrinsic-cut-dissipation-and-fixed-test-pairing-789f-next.md)。

旧[高孔首头观测](2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)
§7 已用同一个低孔核向量取得原 \(W\) 的单孔系数约束。
本稿不重复登记那个核向量或其提升；这里保存它对后来完整 gauge
双块和同一个物理 gap 的准确作用。

## 1. 原物理对象与低孔核向量

固定原 \(N\) 或 \(Y\) 模型的真实头 \(A=A_m=F_m(B_m)\)，
\(d=2^m\ge2\)，以及
\[
 D=D_m=\sum_{\nu\ge m}b_\nu E_\nu,\qquad
 b_\nu=(\nu+1)^{-2},\qquad
 S=S_m=\sum_{\nu\ge m}b_\nu^2>0.
\]
\(\Omega\) 是尾真空，\(W_1=d_0=e^{-20}\) 是原加权链权。
原真实归一给
\[
 A e_0=0,\qquad A e_1=e_0.
 \tag{1.1}
\]
设
\[
 f_0=e_0\otimes\Omega,\quad f_1=e_1\otimes\Omega,\quad
 h_1=\frac{A^*f_0}{W_1},\quad
 y=-\frac{D^*\Omega}{W_1}.
 \tag{1.2}
\]
\(h_1\) 正是 \(a=1\) 的 inverse-gauge 原物理测试；
\(y\) 是 first-head 输入向量，位于尾 degree 一。

定义物理向量
\[
 v=-\frac{e_0\otimes D^*\Omega}{W_1}
                        +\frac S{W_1}f_1 .
 \tag{1.3}
\]
因为 \(DD^*\Omega=S\Omega\)，(1.1) 给
\[
 (A+D)v=0.
 \tag{1.4}
\]
\(v\) 只占尾层 \(0,1\)，所以在任何 \(q\ge1\) 的真实左零源核中。
并有一个不涉及任何最小逆的环境身份
\[
 \boxed{
 h_1+\frac S{W_1}f_1-v
             =\frac{(A+D)^*f_0}{W_1}.
 }
 \tag{1.5}
\]

## 2. 完整 joined Gram 的同一 forcing

取上述依赖稿的同一原 first-head 商、全部零源 \(\mathcal C\)、
欧氏正交补 \(\mathcal U\) 和真实列 \(T\)，切口 \(q\ge1\)。
逐物理头写
\[
 T_i=W_i^{-1}\psi_m(-\delta)^i,\qquad
 T_0=I,\qquad \Gamma=T^*T\succeq I.
\]
degree 一上 \(\delta=D\)，且
\(\psi_m'(0)=W_1\)。因此准确有
\[
 T_0y=y,\qquad T_1y=\frac S{W_1}\Omega,\qquad
 T_i y=0\quad(i\ge2),
\]
\[
 Ty=v,\qquad T^*h_1=y.
 \tag{2.1}
\]
特别 \(y\in\mathcal C\)。置 \(t_1=T^*f_1\)，立即得到
\[
 \boxed{\Gamma y-y=\frac S{W_1}t_1.}
 \tag{2.2}
\]
(2.2) 中 \(\Gamma\) 是完整原 Gram；未先删除任何高返回或零源块。

在 \(\mathcal C\oplus\mathcal U\) 上写
\[
 \Gamma=\begin{pmatrix}\Gamma_{CC}&\Gamma_{CU}\\
                       \Gamma_{UC}&\Gamma_{UU}\end{pmatrix},
 \quad
 R_U=\binom{-\Gamma_{CC}^{-1}\Gamma_{CU}}{I},
 \quad \mathcal S=R_U^*\Gamma R_U.
\]
这里用 \(\mathcal S\) 区别于尾强度 \(S\)。定义真实物理等距
\[
 I_C=T_C\Gamma_{CC}^{-1/2},\qquad
 I_U=TR_U\mathcal S^{-1/2}.
\]
原列及变换后列分别是
\[
 c_1=I_C^*f_1,\quad b_1=I_U^*f_1,\qquad
 c'_1=I_C^*h_1,\quad b'_1=I_U^*h_1.
\]

## 3. 零源和 source 两块的完整恢复

由 (2.1) 和完整逆块，
\[
 c'_1=\Gamma_{CC}^{-1/2}y,\qquad
 b'_1=-\mathcal S^{-1/2}
                      \Gamma_{UC}\Gamma_{CC}^{-1}y .
 \tag{3.1}
\]
将 (2.2) 分成 \(C/U\) 两块，不丢 \(UC\) 项：
\[
 (t_1)_C=\frac{W_1}S(\Gamma_{CC}-I)y,\qquad
 (t_1)_U=\frac{W_1}S\Gamma_{UC}y.
\]
所以
\[
 \boxed{
 c_1=\frac{W_1}S
          (\Gamma_{CC}^{1/2}-\Gamma_{CC}^{-1/2})y,
 \qquad
 b_1=-\frac{W_1}S b'_1 .
 }
 \tag{3.2}
\]
source 式也可由
\(R_U^*\Gamma y=0\) 直接推出；这个正交关系使用全部零源的真正 Schur。

两块合起来是
\[
 \boxed{
 c'_1+\frac S{W_1}c_1=\Gamma_{CC}^{1/2}y,\qquad
 b'_1+\frac S{W_1}b_1=0.
 }
 \tag{3.3}
\]
等价的物理投影身份为
\[
 \boxed{
 P_{\rm jo}h_1+\frac S{W_1}P_{\rm jo}f_1=v.
 }
 \tag{3.4}
\]
因此一般恢复式
\(b_1=K^*c'_1+G_U^*b'_1\)
的两项在此确实共同合成 (3.2)，恢复成本只有 \(W_1/S\)。
没有分别估计两个大交叉块。

原尾满足
\[
 \frac1{3(m+1)^3}\le S_m\le\frac1{3m^3},
\]
故这个恢复系数至多 \(3W_1(m+1)^3\)。

已付的 \(\|b'_1\|^2\le S^2/W_1^2\) 通过 (3.2) 只给
\(\|b_1\|\le1\)。甚至直接用 \(b_1\) 与 (1.3) 正交，可得
\[
 \|b_1\|^2\le\frac1{1+S},\qquad
 \|b'_1\|^2\le\frac{S^2}{W_1^2(1+S)}.
 \tag{3.5}
\]
证明：\(v=(S/W_1)(f_1-e_0D^*\Omega/S)\)，后一个向量的平方范数为
\(1+S^{-1}\)，与 \(f_1\) 的内积为一；source 是其正交补中的一个
真正正交分量。式 (3.5) 仍不趋零。

## 4. 原左最小源也严格按同一系数缩放

令 \(\mathcal U_q r\) 是同一原完整源 \(r\) 的真正左最小原像。
它与全部左零源核正交，且
\[
 (A+D)\mathcal U_q r
\]
只在尾层 \(q\) 有顶输出。当 \(q\ge1\) 时，
它与尾真空 \(f_0\) 正交。因此 (1.5) 给
\[
 \left\langle\mathcal U_q r,h_1+\frac S{W_1}f_1\right\rangle
 =
 \langle\mathcal U_q r,v\rangle
 +\frac1{W_1}\langle(A+D)\mathcal U_q r,f_0\rangle=0.
\]
所以作为完整物理源泛函，
\[
 \boxed{
 \mathcal U_q^*h_1=-\frac S{W_1}\mathcal U_q^*f_1.
 }
 \tag{4.1}
\]
若使用 \(L_q=\mathcal U_q^*\mathcal U_q\) 的原 Riesz 源
\(L_qt_q(f)=\mathcal U_q^*f\)，则
\[
 \boxed{t_q(h_1)=-\frac S{W_1}t_q(f_1).}
 \tag{4.2}
\]
这是同一个 source、同一个左 Gram 和同一个切口；没有换源或投掉反馈。

## 5. 同一个物理 gap 与下降增量

沿内在耗散稿，令
\[
 \mathcal M_q=\ker[Q_q(A+D)],\qquad
 \mathcal K_{q+d}=\ker(A+D)\cap P_{\le q+d}\mathcal H,
 \qquad
 \mathsf G_q=P_{\mathcal M_q}-P_{\mathcal K_{q+d}}.
\]
\(Q_q\) 是该稿原物理低输出商投影，保持尾真空输出 \(f_0\)。
\(\mathsf G_q\) 是实际正交 gap 投影，并随 \(q\) 递减。

(1.3) 的 \(v\) 属于两个空间。
另一方面，
\[
 \langle z,(A+D)^*f_0\rangle
   =\langle Q_q(A+D)z,f_0\rangle=0
 \quad(z\in\mathcal M_q).
\]
所以分别投影 (1.5) 再相减，得到
\[
 \boxed{\mathsf G_qh_1=-\frac S{W_1}\mathsf G_qf_1
        \qquad(q\ge1).}
 \tag{5.1}
\]
定义该稿同一个能量与下降量
\[
 g_q(f)=\langle f,\mathsf G_qf\rangle,\qquad
 d_q(f)=\langle f,(\mathsf G_{q-d}-\mathsf G_q)f\rangle .
\]
当 \(q\ge d+1\) 时，两个切口均可用 (5.1)，于是
\[
 \boxed{
 g_q(h_1)=\frac{S^2}{W_1^2}g_q(f_1),\qquad
 d_q(h_1)=\frac{S^2}{W_1^2}d_q(f_1).
 }
 \tag{5.2}
\]
两者的比值（分母非零时）完全相同。

## 6. 还需要的额外量

(3.2) 真正消去了首头恢复中的大 gauge 块，但它不把已有阶数变成
原固定测试的衰减。对完整 source，所需加强准确是
\[
 \|b'_1\|=o(S_m)
 \quad\Longleftrightarrow\quad
 \|b_1\|\longrightarrow0.
\]
对同一个物理 gap，
\[
 \|\mathsf G_qh_1\|=o(S_m)
 \quad\Longleftrightarrow\quad
 \|\mathsf G_qf_1\|\longrightarrow0.
\]
已有同 gap 耗散的所有齐次能量项同时乘上 (5.2) 的因子，
故仅把同一估计用于 \(h_1\) 再除 \(S_m\)，不会额外赚得一个小量。

后续必须支付这个固定低 forcing 的远孔传播，或用原实际两费用得到
额外衰减。原 \(a>1\) 的共同恢复、移动切口速率及 \(N=M\) 均未由本稿关闭。
