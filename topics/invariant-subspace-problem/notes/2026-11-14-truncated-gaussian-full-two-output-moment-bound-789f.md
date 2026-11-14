# 截断 Gaussian 的完整两输出矩费用至多 4/3

本稿证明一条尺度无关、参数一致的精确矩不等式。它控制完整两维输出 Gram 的逆费用，不只控制其中一条标量投影。将它用于原平衡 star 之前，仍须由真实完整源推导出这里的 Gram 与交叉向量；这一运输不属于本引理的假设。

## 1. 分布、归一矩和待估计的完整费用

令 $U>0$ 的概率密度为

$$
\rho(u)=Z^{-1}\exp(-\lambda u-\chi u^2/2),
\qquad\lambda\in\mathbb R,\quad\chi>0.
$$

置

$$
\mu=\mathbb EU,\qquad Y=U/\mu,\qquad
q=\operatorname{Var}(U)/\mu^2,\qquad r=1+q,
$$

$$
\Delta=\mathbb EY^3-(\mathbb EY^2)^2,
\qquad s=\chi\mu^2.
$$

以下证明同时给出 $0<q<1$、$\Delta>0$。定义完整两输出矩阵及向量

$$
M=\begin{pmatrix}1&-r\\-r&r^2+\Delta\end{pmatrix},
\qquad
b=\begin{pmatrix}1-q\\\Delta/q-2\end{pmatrix}.
\tag{1.1}
$$

**结论：** 对全部上述 $\lambda,\chi$，

$$
\boxed{b^*M^{-1}b\le\frac43.}
\tag{1.2}
$$

实际所估计的完整逆费用恰为

$$
F(q,\Delta)=(1-q)^2+
 \frac{[\Delta/q-(1+q^2)]^2}{\Delta}.
\tag{1.3}
$$

因此 (1.2) 包含了两个输出方向及其真实交叉；没有先删掉非对角块后取逆。

## 2. 三条来自真实矩的界

令 $m_k=\mathbb EY^k$，$a=\lambda\mu$。对 $k\ge1$ 分部积分给

$$
k m_{k-1}=a m_k+s m_{k+1}.\tag{2.1}
$$

其中 $m_0=m_1=1$、$m_2=r$。取 $k=1,2$，准确得到

$$
a=1-sr,\qquad m_3=r^2+\Delta,
\qquad\boxed{s\Delta=2-r=1-q.}\tag{2.2}
$$

以 $Y\rho$ 为概率权（因为 $\mathbb EY=1$），严格 Cauchy–Schwarz 给 $m_3>m_2^2$，即 $\Delta>0$。又 $q>0$ 是严格正方差，(2.2) 因而直接推出 $q<1$；不需调用额外的对数凹定理。

第一条下界来自边界项。对 $(u-\mu)\rho'(u)$ 分部积分，准确有

$$
\chi\operatorname{Var}(U)=1-\mu\rho(0)<1.
$$

结合 (2.2) 得

$$
\boxed{\Delta\ge q(1-q).}\tag{2.3}
$$

其余两条界来自两个完整三阶 Gram 行列式。由 (2.1)，

$$
m_4=r m_3+\frac{3r-m_3}{s},\qquad
m_5=r m_4+\frac{4m_3-m_4}{s}.
$$

对实际向量 $(1,Y,Y^2)$，分别在概率权 $\rho$ 和 $Y\rho$ 中取 Gram，逐项展开得

$$
\det(m_{i+j})_{i,j=0}^{2}
=\frac{\Delta\,[q(1+q)-\Delta]}{1-q}\ge0,
\tag{2.4}
$$

$$
\det(m_{i+j+1})_{i,j=0}^{2}
=\frac{\Delta^2\,[(3-q)\Delta-q(1+q)^2]}{(1-q)^2}\ge0.
\tag{2.5}
$$

这些是一般符号恒等式；只使用 (2.1)–(2.2)，没有取固定参数实例。因此

$$
\boxed{
\max\left\{q(1-q),\frac{q(1+q)^2}{3-q}\right\}
\le\Delta\le q(1+q).}
\tag{2.6}
$$

两个下界在 $q=1/3$ 交叉：左区间使用 $q(1-q)$，右区间使用 $q(1+q)^2/(3-q)$。

## 3. 完整逆费用的统一上界

对固定 $q\in(0,1)$，(1.3) 关于 $\Delta$ 严格凸，因为

$$
\frac{\partial^2F}{\partial\Delta^2}
=\frac{2(1+q^2)^2}{\Delta^3}>0.
$$

所以只需估计 (2.6) 的两个端点。

在上端 $\Delta=q(1+q)$，

$$
F=\frac{(1-q)^2(1+2q)}{1+q}\le1,
$$

因为与 $1$ 的差为 $q(1+3q-2q^2)/(1+q)>0$。

当 $0<q\le1/3$ 时，下端为 $q(1-q)$，此时

$$
F=\frac{1-2q+5q^2}{1-q},\qquad
\frac43-F=\frac{(1-3q)(1+5q)}{3(1-q)}\ge0.
\tag{3.1}
$$

当 $1/3\le q<1$ 时，下端为 $q(1+q)^2/(3-q)$，此时

$$
F=\frac{(1-q)^2(-q^3+10q^2-q+4)}
 {q(3-q)(1+q)^2},
$$

$$
\frac43-F
=\frac{(3q-1)(q^4-13q^3+19q^2-3q+12)}
 {3q(3-q)(1+q)^2}\ge0.\tag{3.2}
$$

最后一个四次因子在 $0\le q\le1$ 上为正：

$$
q^4+q^2(19-13q)-3q+12\ge6q^2+9>0.
$$

上端和两个分段下端均已控制，凸性即证明 (1.2)。同一范围内还直接有

$$
0\le\frac{(1-q)^2}{1+q}\le1.\tag{3.3}
$$

## 4. 范围与用途

本引理的常数 $4/3$ 对全部实漂移 $\lambda$ 和全部正曲率 $\chi$ 一致，未声称最优。证明保留了完整 $M^{-1}$；仅控制向量 $b$ 的首分量不足以代替这个结论。

若原平衡 star 的临界三尺度计算确实产生 (1.1) 的真实两输出 Gram 和交叉向量，则本引理支付该联合费用；若另有深层通道给出 (3.3)，该通道也有统一界。它不单独证明完整源的这些识别，不替代有限 $Q$ 的误差控制，也不扩大到组数增长或比例消失的全部模型。
