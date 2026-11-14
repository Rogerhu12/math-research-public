# 原有限头逆芽的 \(e^{-(25/2)d^3}\) 真实半径及保权系数

日期：2026-11-14。独占续稿：literature_audit / 789f。

**状态：完整证明。** 本稿把两个原有限真实头的逆解析芽半径从
\(e^{-(55/4)d^3}\) 改进为 \(e^{-(25/2)d^3}\)，并保留真实二进制权位置。
还给出非线性部分在该圆盘上的显式小量。
这是一条有限真实头结论；没有据此认定实际源 Schur 补、回返角度或
原边界 \(N=M\) 已得到控制。

基本模型及原链基公式见
[R239 实际头附录](../results/R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)。
与本稿可配合的实际大窗口见
[联合 carry 与二十六窗口](2026-11-14-joint-positive-carry-budget-and-twenty-six-window-actual-sources-789f-next.md)。
两篇的作用不同：后一篇给可用的真实源窗口，本稿只给头函数本身的解析尺度。

## 1. 原函数、真权与结论

取 \(m\ge10,\ d=2^m\)，在原物理头基 \(e_0,\ldots,e_{d-1}\) 中记
\[
 B_m e_n=\frac{W_n}{W_{n-1}}e_{n-1},\qquad
 W_n=\prod_{i\in\operatorname{bits}(n)}d_i,\qquad
 d_i=e^{-\Lambda_i},
\]
\[
 \Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i,\qquad
 d_0=e^{-20}.
\tag{1.1}
\]
原正外场为 \(b_i=(i+1)^{-2}\)。分别取
\[
 F_{N,m}(z)=\sum_{i<m}b_i\frac{z^{2^i}}{d_i},\qquad
 F_{Y,m}(z)=\sum_{i<m}b_i\frac{z^{2^i}}{d_i+z^{2^i}}.
\tag{1.2}
\]
有限真实头是 \(A_m=F_m(B_m)\)，其中 \(F_m\) 取上述任一个。
Cayley 式在幂零矩阵上按其有限 Taylor 多项式代入；以下则讨论其真解析函数。

置
\[
 \tau_m=\frac{25}{2}d^3,\qquad
 \rho_m=e^{-\tau_m},\qquad r_m=\frac{\rho_m}{2d_0},\qquad
 \varepsilon_m=e^{-d^3/4}.
\tag{1.3}
\]
则两个模型统一满足：

1. \(F_m\) 在 \(|z|\le\rho_m\) 的邻域内解析，且
   \[
   \left|\frac{F_m(z)}z-d_0^{-1}\right|\le\varepsilon_m.
   \tag{1.4}
   \]
   商在 \(z=0\) 取解析延拓。
2. 原逆芽 \(\psi_m=F_m^{-1}\) 在 \(|w|\le r_m\) 的邻域内解析，且
   \[
   |\psi_m(w)|\le\rho_m,\qquad
   |\psi_m(w)-d_0w|\le2d_0^2\varepsilon_m|w|.
   \tag{1.5}
   \]
3. 对全部整数 \(k,n\ge0\)，
   \[
   |[w^k]\psi_m(w)^n|
   \le(2d_0)^k\rho_m^{\,n-k}.
   \tag{1.6}
   \]
   \(k<n\) 时该系数严格为零；\(n=0\) 时仅 \(k=0\) 非零。

这里所有半径都属于有限真实函数 \(F_m\)，不对无限形式和使用
Rouché 或 Cauchy 定理。

## 2. 最高非线性位与其余位分开估计

总有 \(\Lambda_i\le100\,16^i\)。先对最高位 \(i=m-1\) 使用完整
\(\Lambda_i\)，而不是丢掉负三次项：
\[
\begin{aligned}
 \Lambda_{m-1}-\tau_m(2^{m-1}-1)
 &=-\frac58d^3+\left(75m-\frac{125}{2}\right)d\\
 &\le-\frac12d^3.
\end{aligned}
\tag{2.1}
\]
最后一步由 \(75m\le d^2/8\) 得到；它在 \(m=10\) 成立，
且左侧线性增长而 \(d^2\) 每步乘 \(4\)，故对所有 \(m\ge10\) 成立。

若 \(1\le i\le m-2\)，记 \(q=2^i\ge2\)。因为
\(8^i\le d^3/64\)，
\[
\begin{aligned}
 \Lambda_i-\tau_m(q-1)
 &\le \frac{25}{16}d^3q-\frac{25}{2}d^3(q-1)\\
 &=\left(\frac{25}{2}-\frac{175}{16}q\right)d^3
 \le-\frac{75}{8}d^3.
\end{aligned}
\tag{2.2}
\]
因此
\[
 \frac{\rho_m^{2^{m-1}-1}}{d_{m-1}}\le e^{-d^3/2},\qquad
 \frac{\rho_m^{2^i-1}}{d_i}\le e^{-75d^3/8}\quad(1\le i\le m-2).
\tag{2.3}
\]
这些界还给 \(\rho_m^{2^i}/d_i<1/2\)。
最低位有 \(\rho_m/d_0<1/2\)。所以 Cayley 的每个分母在闭圆盘上非零，
且取倒数时相对 \(d_i^{-1}\) 至多多付因子 \(2\)。

在 \(N\) 模型中，\(F_m(z)/z\) 的最低项恰为 \(d_0^{-1}\)。
在 \(Y\) 模型中，最低项是 \((d_0+z)^{-1}\)，且
\[
 |(d_0+z)^{-1}-d_0^{-1}|\le2\rho_m/d_0^2.
\]
用 \(b_i\le1\) 和 \(m-2\le d\)，两模型均有
\[
\begin{aligned}
 \left|\frac{F_m(z)}z-d_0^{-1}\right|
 &\le2e^{40-(25/2)d^3}
       +2e^{-d^3/2}+2d\,e^{-75d^3/8}\\
 &\le e^{-d^3/4}.
\end{aligned}
\tag{2.4}
\]
最后的不等式直接由 \(d\ge1024\) 得到：除以 \(e^{-d^3/4}\) 后，
三个正项分别为
\(2e^{40-(49/4)d^3}\)、\(2e^{-d^3/4}\)、
\(2d e^{-(73/8)d^3}\)，各小于 \(1/3\)。
这证明 (1.4)，也清楚指出改进来自原 \(-105\,8^i\) 项。

## 3. 唯一逆芽及非线性系数的小量

令 \(G_m(z)=F_m(z)/z\)。
对 \(|w|\le r_m\)，在 \(|z|=\rho_m\) 上，
\[
 |F_m(z)-z/d_0-w|
 \le\rho_m\varepsilon_m+\frac{\rho_m}{2d_0}
 <\frac{\rho_m}{d_0}.
\tag{3.1}
\]
Rouché 定理给 \(F_m(z)-w\) 在该圆盘内恰有一个零，按重数计。
它是单零，所以随 \(w\) 解析变化，并延拓原逆芽。
(3.1) 的严格余量及紧性还给闭 \(w\) 圆盘的一个解析邻域。
这证明 \(|\psi_m(w)|\le\rho_m\)。

由
\[
 w=d_0^{-1}\psi_m(w)+\psi_m(w)
       \bigl(G_m(\psi_m(w))-d_0^{-1}\bigr)
\]
得到
\[
 |\psi_m(w)|\le\frac{d_0|w|}{1-d_0\varepsilon_m}
 \le2d_0|w|,
\]
\[
 |\psi_m(w)-d_0w|\le d_0\varepsilon_m|\psi_m(w)|
 \le2d_0^2\varepsilon_m|w|.
\tag{3.2}
\]
在半径 \(r_m\) 的圆上对 \(\psi_m^n\) 用 Cauchy 系数公式，
即得 (1.6)。

还可以显式保留非线性小量。函数
\[
 h_m(w)=\frac{\psi_m(w)}{d_0w}-1
\]
在零点解析，满足 \(h_m(0)=0\) 和
\(|h_m|\le2d_0\varepsilon_m\)。
对 \(1\le n<d\)，
\[
 |(1+h_m)^n-1|
 \le n|h_m|e^{n|h_m|}
 \le4n d_0\varepsilon_m.
\]
最后一步使用 \(e^{2d d_0\varepsilon_m}\le2\)。
于是对 \(k>n\)，
\[
 \boxed{
 |[w^k]\psi_m(w)^n|
 \le4n d_0^{\,n+1}\varepsilon_m\,r_m^{\,n-k}.
 }
\tag{3.3}
\]
对角系数则准确是 \([w^n]\psi_m^n=d_0^n\)。
(3.3) 是对同一有限头解析芽的系数估计，不是对任意物理源的能量估计。

## 4. 真实输入列权不变

令
\[
 K_m e_k=(A_m^*)^k e_0,\qquad
 V_m=K_m^{-*}.
\]
原有限头链基满足
\[
 A_m=V_mJ_dV_m^{-1},\qquad
 K_m=D_W C_{F_m},\qquad
 (K_m^{-1})_{kn}=\frac{[w^k]\psi_m(w)^n}{W_n}.
\tag{4.1}
\]
分母仍是输入列的 \(W_n\)。

对 \(0\le n\le k<d\)，(1.6) 中的真实权组合满足
\[
\begin{aligned}
 \log\bigl(W_n^{-1}\rho_m^{\,n-k}\bigr)
 &=\tau_m k+
   \sum_{i\in\operatorname{bits}(n)}(\Lambda_i-\tau_m2^i)\\
 &\le\tau_m k.
\end{aligned}
\tag{4.2}
\]
确实，\(i<m\) 时
\(\Lambda_i\le100\,16^i\le100\,8^{m-1}2^i=\tau_m2^i\)。
结合 \(2d_0<1\)，得到
\[
 \|K_m^{-1}\|\le d\,e^{\tau_m(d-1)}.
\tag{4.3}
\]
原真实头有 \(\|A_m\|<6\)，所以
\(\|K_m\|\le\sqrt d\,6^{d-1}\)。因此也有较粗的完整相似界
\[
 \boxed{\kappa(V_m)\le e^{201\,16^{m-1}}\qquad(m\ge10).}
\tag{4.4}
\]
证明是把
\(\tau_m d=200\,16^{m-1}\) 与
\(\tfrac32\log d+(d-1)\log6<d^4/16=16^{m-1}\) 相加。
(4.4) 依然具有 \(d^4\) 指数；不能把它改称
\(e^{(25/2)d^3}\) 的源比较常数。

## 5. 同一真实首头源的接口和未付范围

这里只重申实际链基给出的源保持接口，供后续 Schur 补使用。
设 \(D\) 为原尾删除，\(f\in\ker D^d\) 为完整首头源。
真实纯尾核列的第 \(i\) 个物理头分量为
\[
 (\mathcal T_m f)_i
   =\frac{\psi_m(-D)^i f}{W_i},\qquad0\le i<d.
\tag{5.1}
\]
函数代入截断模 \(D^d\)，故有限多项式无域问题。
(5.1) 由 (4.1) 逐项得到：
\[
 \mathcal T_m f=\sum_{j<d}V_me_j(-D)^jf,\qquad
 (V_m)_{ij}=W_i^{-1}[w^j]\psi_m(w)^i.
\]
第一物理头确为 \(f\)，而不是一个另选的相似源。

若 \(S_\psi=\psi_m(-D)\)，则同一实际 Gram 是
\[
 \Gamma_m=\mathcal T_m^*\mathcal T_m
  =\sum_{i<d}\frac{(S_\psi^i)^*S_\psi^i}{W_i^2},
 \qquad B_m\mathcal T_m=\mathcal T_m S_\psi.
\tag{5.2}
\]
最后一式逐物理头检查即可；末项由 \(S_\psi^d f=0\) 消失。
所以 \(S_\psi\) 在该完整 Gram 度量中的各次幂满足
\[
 \|S_\psi^j f\|_{\Gamma_m}\le\|B_m^j\|\,\|f\|_{\Gamma_m}.
\tag{5.3}
\]
取 bare 商时必须从原商算子和原商源重新构造同式；不能借 (5.2)
把完整真核取商与环境取商后取核认作同一空间。

本稿给
\[
 \rho_m^{-2}=e^{25d^3},
\]
而实际二十六窗口是 \(Q_m=\lfloor e^{26d^3}\rfloor\)。
这说明**假如**以后能证明某条所需实际源 Schur 预算至多付固定多项式因子
乘 \(\rho_m^{-2}\)，数值尺度可以放入已付窗口。
这个假设在本稿中没有证明。尤其 (5.3) 不能替代消去低孔零核及全部
高返回源后的实际角度估计；全 \(\Gamma_m\) 的相对孔次数交换子也不由
这个小圆盘得到控制。原边界 \(N=M\) 与一般不变子空间目标仍未闭合。
