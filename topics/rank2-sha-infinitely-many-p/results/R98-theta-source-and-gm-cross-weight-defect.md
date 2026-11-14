# R98. 原 theta 源的完整中央投影及真实 GM 跨权差

## 原 theta 的同权源准确保留未知中央数据

令 \(a=-p,q=p^2,W_P=w\Theta_P=1+X_P\)。在原加法坐标中，
\[
W_{aP}(az,aw)=W_P^q E_{p,P},\qquad
E_{p,P}=\frac{aw^{1-q}}{\Psi_a(w)}
 \frac{\Psi_a(P+z+w)}{\Psi_a(P+z)}.
\]
这里已乘回完整 \(w/Z(w)\) 公共因子；不声称加法坐标的全部系数整。
真实非线性源直接由实际除法函数和逐标签有限多项式定义：
\[
\mathcal N_p=\sum_P\left\{
(E_{p,P}-1)(1+qX_P)+
E_{p,P}\sum_{k=2}^q\binom qkX_P^k\right\}.
\]
其总次数 \(D\) 部分只用全部较低总次数的混合 \(X_P\) jets，
并保留原 \(256\) 标签、参考与交叉项。

准确中央投影为
\[
[z^mw^{m+1}]\mathcal N_p=-p^2(1+p^{2m-1})d_m.
\]
取已核定的 Borel 尺度 \(\kappa_md_m=C_m\)，全部中央生成式为
\[
\mathscr H(\mathcal N_p)(u)
=-p^2\mathcal B_1(u)-p\mathcal B_1(p^2u).
\]
这不是 Bol exact：实际 \(m=4,C_4=1\) 已给非零留数。
对完整深度 \(m_n=(p+1)p^n\)、\(S_{p,n}=p^{p^n}C_{m_n}\)，
归一化源准确为
\[
T_{p,n}=-(1+p^{2m_n-1})S_{p,n}.
\]
它与原 \(S_{p,n}\) 有完全相同的赋值和模 \(p^{4n+4}\) 非零判据。
所以直接投影该源，没有产生独立的中央非零输入。

## 真实 GM 箭头及不能删除的跨权差

设
\[
A_q=K(t^q)L'-L(t^q)K',\quad
B_q=L(t^q)K-K(t^q)L,\quad
g_f=st^{q-1}f(t^q).
\]
完整二步 Frobenius 在一形式上是
\[
-p^3g_f(A_q\omega+B_q\eta)\,dt.
\]
消去 \(\eta\) 给准确标量算子
\[
\operatorname{Fr}_2(f)=-p^3\bigl(g_fA_q-(g_fB_q)'\bigr);
\]
两者相差明确的 exact 项
\(\nabla(-p^3g_fB_q\omega)\)。

实际主部 \(f_m\) 的极点阶是 \(m-3\)，而
\(\operatorname{Fr}_2^-(f_m)\) 的极点阶为 \(q(m-4)+1\)，
首系数为 \(-p^3(1-q(m-4))\)。
因此它与 \(f_{mq}\) 的极点阶相差 \(4q-4\)，不能直接等同。
准确主部差的留数为
\[
\operatorname{Res}\bigl((f_{mq}-\operatorname{Fr}_2^-(f_m))\omega\,dt\bigr)
=(C_{mq}+p^3C_m,0).
\]
先分别按完整中央规范整化后，差的留数改为
\[
(S_{p,n+2}+p^3S_{p,n},0).
\]
如果统一乘下一层尺度，第二项还须乘
\(p^{(p^2-1)p^n}\)；两个比较不得混淆。

实际首层 \(\Gamma_{i,p}=C_{p+1}/p\) 为单位时，
全部 \(n\ge0\) 都有
\[
v_pS_{p,n}=2n+2,\qquad
v_p(S_{p,n+2}+p^3S_{p,n})=2n+5.
\]
原曲线 \(p=7\) 已满足此假设。
因此“下一层是固定秩二留数 Frobenius 的单位倍数”在真实对象上已被排除。
原纤维同源产生 \(u\mapsto p^2u\)，底参数 Frobenius 产生
\(u\mapsto u(t(u)^{p^2})\)；局部分歧次数不同，不能直接换坐标识别。

## 证明与剩余问题

[完整 theta 源证明](../notes/2026-11-12-theta-carry-central-residue-source.md)
及[GM cochain 与完整归一化](../notes/2026-11-12-gm-frobenius-principal-part-and-central-defect.md)
均经根端全文审计，作者另相互核对实际源与尺度。

新的路线须约束这个具体跨权差，或真正构造保留公共 Poincaré
参考的其他中央上同调对象。仅因半因子平方及张量斜率相容，
不能自行换成一个尚未构造的张量类。
主目标的无穷素数非零性仍未证明。
