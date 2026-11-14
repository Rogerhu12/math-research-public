# 奇硬池加入弱位后的完整偶相位极限与同常数硬端传输

日期：2026-11-14（UTC）。代理：literature_audit / 789f。

**状态：本文的真实源极限、有限反例传输及全称条件蕴含已证明；一般偶临界相位的统一有限上界尚未证明。** 新内容是：若偶临界池的指定相位费用具有统一常数，单是这条费用就足以控制全部奇数硬端，进而控制全部加强高度。这个推论不借助有限弱位 SOS 的其它尚未支付条件，也不作循环的按位数归纳。

## 1. 固定奇数池与所要加入的弱位

固定任意正权 \(b_1,\ldots,b_{2r+1}\)，\(r\ge1\)。在正交子集基的物理层 \(H_j\) 上定义
\[
d=\sum_i b_iE_i,\qquad
e=\sum_i b_i^{-1}E_i^*,\qquad A_{\rm all}=e^*,
\qquad C=\sum_i b_i^3E_i.
\]
令
\[
U=\ker d\cap H_r,\qquad W=\ker d\cap H_{r-1},
\]
\[
G=\Gamma_{1,r},\qquad L_j=\Gamma_{j,r-1}\quad(1\le j\le3),
\qquad A=A_{\rm all}|_U:U\to W,\qquad B=C|_U:U\to W.
\tag{1.1}
\]
这里 \(\Gamma_{j,s}\) 始终表示完整层 \(d^j/j!\) 的最小范数逆 \(\mathcal J_{j,s}\) 的 Gram。所有伴随按继承的物理内积取。\(U\) 的高度是一，\(W\) 的高度是三；没有定义不存在的 \(\Gamma_{2,r}\)。

简写实际最小逆
\[
E=\mathcal J_{1,r}:U\to H_{r+1},\qquad
R=\mathcal J_{1,r-1}:W\to H_r,\qquad
J_j=\mathcal J_{j,r-1}.
\]
故 \(E^*E=G\)、\(R^*R=L_1\)、\(J_j^*J_j=L_j\)。定义
\[
Q=B^*L_2:W\to U,
\qquad
\delta=\tfrac12(G^{-1}B^*L_3-B^*L_2),
\qquad \Xi=Q+\delta.
\tag{1.2}
\]

加入权 \(a>0\) 的新位，得到 \(2r+2\) 位偶池，删除为
\[
D=d\otimes I+aI\otimes E_{\rm bit},\qquad t=a^2.
\]
该偶池的临界低源是 \(V_a=\ker D\cap H_r^{\rm new}\)，高度二；最高 primitive 源是 \(U_a=\ker D\cap H_{r+1}^{\rm new}\)，高度零。

## 2. 旧奇数池的一条完整两塔关系

除已付的硬端消逆
\[
\delta^*G=-L_1A,
\tag{2.1}
\]
外，本稿需要如下实际恒等式：
\[
\boxed{G^{-1}A^*L_1=A^*+2Q.}
\tag{2.2}
\]

下面在真实物理层证明 (2.2)。中央删除 \(d:H_{r+1}\to H_r\) 可逆，且由 \([d,e]|_{H_r}=I\) 得 \(e|_U=E\)。又有
\[
e|_W=3R+A^*,\qquad
A_{\rm all}E=\iota_U G+RA.
\tag{2.3}
\]
第一式由 \(de|_W=3I_W\) 与 \(H_r=U\oplus\operatorname{Ran}d^*\) 的正交分解得到。第二式中，删除给 \(dA_{\rm all}E=A\)，而 \(U\) 分量由 \(e|_U=E\) 取伴随确定为 \(G\)。

真实两带式为
\[
d^*|_U=EG^{-1}-J_2B,
\qquad dJ_2=2R-Q.
\tag{2.4}
\]
这里第一式也可直接由 \(d^2d^*|_U=-2B\)、\(d^3d^*|_U=0\) 及两个真 MP 塔正交推出；投到 \(E(U)\) 的系数是 \(G^{-1}\)。第二式的低塔系数由 \(d^2J_2=2I_W\) 确定，上塔系数由第一式取伴随得到。

在 \(R(W)\subset H_r\) 上用 \([d,e]=I\)，有
\[
deR=e|_W+R=4R+A^*.
\]
另一方面，由 (2.4)，
\[
d\{2J_2+E(A^*+2Q)\}=4R+A^*.
\]
中央删除可逆，所以
\[
\boxed{eR=2J_2+E(A^*+2Q).}
\tag{2.5}
\]
左乘 \(E^*\)，真塔正交给右侧 \(G(A^*+2Q)\)；左侧由 (2.3) 给
\[
E^*eR=(A_{\rm all}E)^*R=A^*L_1.
\]
这证明 (2.2)。

式 (2.1) 是 [R297 硬端创新消逆](../results/R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md) 的真实恒等式。其等价形式是
\(L_3B=L_2BG-2L_1A\)，来自把 \([A_{\rm all},d^*]=-I\) 作用于 \(E(U)\)，再投到 \(J_2(W)\)；保留完整逆后投影，没有交换压缩次序。结合 (2.1)–(2.2)，得到
\[
\boxed{\delta=-A^*-2Q,\qquad \Xi=-A^*-Q.}
\tag{2.6}
\]

## 3. 两个新源的物理坐标及全部度量

新低源的同一个图坐标为
\[
\mathcal E_a:U\oplus W\longrightarrow V_a,
\qquad \mathcal E_a(x,y)=(x-aRy,y).
\tag{3.1}
\]
它是双射，并且
\[
\mathcal E_a^*\mathcal E_a
=\mathsf H_a=\operatorname{diag}(I_U,I_W+tL_1).
\tag{3.2}
\]
新最高源的图坐标是
\[
\mathcal F_a:U\longrightarrow U_a,
\qquad \mathcal F_a u=(-aEu,u),
\qquad \mathcal F_a^*\mathcal F_a=I_U+tG.
\tag{3.3}
\]
所以这些坐标一般不正交，不能把它们的坐标伴随当作物理伴随。

令 \(A_{0,a}:U_a\to V_a\) 是新池的真实倒数删除。由 (2.3)，它在上述两个坐标中的矩阵为
\[
\mathcal E_a^{-1}A_{0,a}\mathcal F_a
=\mathcal A_a
=\begin{pmatrix}a^{-1}I_U-aG\\ A\end{pmatrix}.
\tag{3.4}
\]
因此其实际平方 \(A_{0,a}A_{0,a}^*\) 的算子坐标准确是
\[
\boxed{\mathsf R_a=
\mathcal A_a(I_U+tG)^{-1}\mathcal A_a^*\mathsf H_a.}
\tag{3.5}
\]
最右边的 \(\mathsf H_a\) 与中间的 \((I+tG)^{-1}\) 都不可省去。

令 \(G_a=\Gamma_{1,r}(D)\)、\(L_a=\Gamma_{2,r}(D)\)。它们的形式坐标记为
\[
\widehat G_a=\mathcal E_a^*G_a\mathcal E_a,
\qquad \widehat L_a=\mathcal E_a^*L_a\mathcal E_a.
\]
由 [R275 完整一位递推](../results/R275-one-bit-full-primitive-schur-recursion-and-innovation.md) 的真实最高高度公式，有
\[
P=(G^{-1}+tI)^{-1},\quad V_1=L_1+tL_2,\quad V_2=L_2+tL_3,
\]
\[
S_C=\begin{pmatrix}I_U&-aC\\0&I_W\end{pmatrix},
\]
\[
\boxed{
\widehat G_a=S_Q^*\operatorname{diag}(P,V_1)S_Q,
\qquad
\widehat L_a=S_\Xi^*\operatorname{diag}(t^{-1}G,V_2)S_\Xi.
}
\tag{3.6}
\]
首式用 \(Q_1=B^*L_2\)；第二式用真正顶硬约束 \(P_2=t^{-1}G\) 和 \(Q_2=Q_1+\delta\)。这没有把旧 \(G_2\) 设成某个有限正矩阵。

算子坐标则是
\[
\mathsf G_a=\mathsf H_a^{-1}\widehat G_a,
\qquad \mathsf L_a=\mathsf H_a^{-1}\widehat L_a.
\tag{3.7}
\]

## 4. 真相位的完整块极限

定义新偶池的实际相位
\[
H_{0,a}=G_a^{-1}L_a-2G_a-A_{0,a}A_{0,a}^*,
\qquad
\Phi_a=H_{0,a}^*L_a^{-1}H_{0,a}.
\tag{4.1}
\]
其算子坐标为
\[
\mathsf H_{0,a}
=\widehat G_a^{-1}\widehat L_a
-2\mathsf H_a^{-1}\widehat G_a-\mathsf R_a.
\tag{4.2}
\]

所有下面的 \(O(a^j)\) 都是固定旧有限池下的算子范数估计；常数允许依赖 \(b\)，没有声称对全部旧权一致。

直接相乘 (3.6) 给
\[
\widehat G_a^{-1}\widehat L_a
=\begin{pmatrix}
t^{-1}I+G-QV_1^{-1}\delta^*G&
-a^{-1}\Xi+a\{-G\Xi+QV_1^{-1}V_2+QV_1^{-1}\delta^*G\Xi\}\\
-a^{-1}V_1^{-1}\delta^*G&
V_1^{-1}(V_2+\delta^*G\Xi)
\end{pmatrix}.
\tag{4.3}
\]
另一方面，(3.5) 的四块分别为
\[
\begin{aligned}
\mathsf R_{a,11}&=t^{-1}I-3G+O(t),\\
\mathsf R_{a,12}&=a^{-1}A^*+a(A^*L_1-2GA^*)+O(a^3),\\
\mathsf R_{a,21}&=a^{-1}A-2aAG+O(a^3),\\
\mathsf R_{a,22}&=AA^*+O(t).
\end{aligned}
\tag{4.4}
\]
用 \(\delta^*G=-L_1A\) 以及 (2.6) 抵消 (4.2) 中的奇异项，得到
\[
\boxed{
\mathsf H_{0,a}=
\begin{pmatrix}
2G+QA+O(a^2)&a^{-1}Q+O(a)\\
O(a)&J+O(a^2)
\end{pmatrix},
\quad J=L_1^{-1}L_2-2L_1+AQ.
}
\tag{4.5}
\]
这里的上右 \(a^{-1}Q\) 不能单独估范数；必须同下一个顶度量一起计算。

由 (3.6) 真正求逆，恰有
\[
\boxed{
\widehat L_a^{-1}=
\begin{pmatrix}
tG^{-1}+t\Xi V_2^{-1}\Xi^*&a\Xi V_2^{-1}\\
aV_2^{-1}\Xi^*&V_2^{-1}
\end{pmatrix}.
}
\tag{4.6}
\]
于是 \(\Phi_a\) 的形式坐标是
\[
\mathcal E_a^*\Phi_a\mathcal E_a
=\mathsf H_{0,a}^*\mathsf H_a\widehat L_a^{-1}
\mathsf H_a\mathsf H_{0,a}.
\tag{4.7}
\]
特别 \(\mathsf H_a\) 出现两次，来源都是物理度量转换。

令
\[
\boxed{Z=L_1^{-1}L_2-2L_1-Q^*Q.}
\tag{4.8}
\]
由 (2.6)，有 \(\Xi^*Q+J=Z\)。将 (4.5)–(4.6) 代入 (4.7)，其下右块趋于
\[
Q^*G^{-1}Q+(\Xi^*Q+J)^*L_2^{-1}(\Xi^*Q+J)
=Q^*G^{-1}Q+Z^*L_2^{-1}Z.
\tag{4.9}
\]
上左块为 \(O(a^2)\)，两个交叉块为 \(O(a)\)。所有矩阵维数固定，且 \(\mathsf H_a\to I\)。因此得到完整源上的结论。

**定理 4.1（真实同源相位极限）。** 令
\[
\mathcal U_a=\mathcal E_a\mathsf H_a^{-1/2}:U\oplus W\to V_a.
\]
这是一个物理酉同构，并且在算子范数下
\[
\boxed{
\mathcal U_a^*\Phi_a\mathcal U_a
\longrightarrow
\operatorname{diag}\left(0_U,\ Q^*G^{-1}Q+Z^*L_2^{-1}Z\right)
\quad(a\downarrow0).
}
\tag{4.10}
\]
一般 \(Z\) 不必自伴，故式中保持 \(Z^*L_2^{-1}Z\) 的原次序。

## 5. 偶相位统一界单独足以支付所有奇硬端

**推论 5.1。** 固定 \(\kappa>0\)。如果任意有限正权偶临界池的相位均满足
\[
H_0^*L^{-1}H_0\preceq\kappa I,
\tag{5.1}
\]
那么任意奇数硬池的加强硬端费用都不超过同一个 \(\kappa\)。因此由 R297 的普适硬端归约，全部有限正权、全部出生和合法高度的加强相邻费用也不超过同一个 \(\kappa\)。

**证明。** 对任意固定旧奇数池应用 (5.1) 于每个 \(a>0\) 的新增偶池，再用 (4.10)，得
\[
Q^*G^{-1}Q+Z^*L_2^{-1}Z\preceq\kappa I_W.
\]
删除第二个已知正项，得到 \(Q^*G^{-1}Q\preceq\kappa I_W\)。矩形算子 \(G^{-1/2}Q\) 的两个平方具有相同非零谱，故该式等价于
\[
QQ^*=B^*L_2^2B\preceq\kappa G.
\tag{5.2}
\]
由 [R297 倒数权桥平方等价](../results/R297-appendix-reciprocal-bridge-square-and-physical-projection-target.md)，(5.2) 正是互易权池 \((b_i^{-1})\) 的实际硬端费用上界。倒数变换遍历全部正权，因此得到所有奇数硬端。出生零的单个位硬端费用为零，不留下例外。最后应用已付的[同常数硬端普适归约](../results/R297-appendix-weak-bit-hard-top-universal-strengthened-equivalence.md) 即得全部加强高度。\(\square\)

该证明只使用偶相位的全称假设与一个真实弱位极限。它不需要另假旧首费用或本稿之前的 SOS 联合剩余块，也不把那些尚未证明的量作为归纳已知项。

**推论 5.2（有限真实反例的传输）。** 若某个奇数硬池违反常数 \(\kappa\)，则取它的互易权后，加入一个充分小但严格正的位权，就得到违反同一 \(\kappa\) 的实际偶临界相位。

**证明。** 由 (5.2) 的反向等价，互易权池的 \(Q^*G^{-1}Q\) 存在大于 \(\kappa\) 的 Rayleigh 商；(4.10) 的极限仍大于 \(\kappa\)。算子范数收敛保证固定旧池存在 \(a_0>0\)，使所有 \(0<a<a_0\) 均违反相位界。这个阈值允许依赖旧池与严格违例余量，不是对全部权的一致边界估计。\(\square\)

本稿没有证明反向全称蕴含；尤其极限还保留 \(Z^*L_2^{-1}Z\)，不能把它无理由丢掉后称偶相位与硬端完全等价。

## 6. 一次完整层精确校准及尚缺的界

只为核归一化，取旧三权 \(b=(1,2,3)\)，以
\[
\begin{pmatrix}1&0\\0&1\\-1/3&-2/3\end{pmatrix}
\]
为 \(U=b^\perp\) 的非正交物理基，\(W=\mathbb C\)。从新四位完整子集包含矩阵独立计算两个完整逆、实际最高 primitive 核与倒数删除，符号求得 (4.7) 的全源极限恰为
\[
\operatorname{diag}(0,0,199/343),
\]
与 (4.9) 完全相同。这个一次精确核对不参与一般证明，也不作为任意权相位上界的证据。

一般的 (5.1) 仍未证明，连某个权与出生均无关的有限 \(\kappa\) 也尚未得到。等权偶池相位费用恰为 \(I\)，所以若要给出普适相位常数，必须 \(\kappa\ge1\)。当前真正待付的是同一个物理压缩的相位费用；共同谱、正 Schur 残差或未投影提升范数不能自动代替它。

即使将来证明 (5.1)，上述有限 Boolean primitive 结论仍不自动支付原首物理头 graph 接合的全部费用。本稿不宣称 Hilbert 不变子空间问题已经完成。
