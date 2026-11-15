# 原 p=11 mod12 apolar 源的 harmonic-seven 余项

日期：2026-11-15。状态：**原频率函数、低五阶多项式部分及剩余的固定原函数接口已逐式证明；其 CM 的 FG 条目非零未证明。** 本文只作路线记录，不登记新的非零定理。

接 [R812 原 apolar 源与 Gaussian 低矩](../results/R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)的全部原规范：c=0 sigma；原六截面
\(\Phi=(S,F,H,R,J,G)^t\)；同一 \(\Theta_r,\Psi_r,U,\lambda,\eta,d_0\)；
\(A(P_0)=0,\ DA(P_0)=B\ne0\)；同一 first-p 商环中的 apolar 矩阵
\[
 Q_{ab}=\mathcal B(L^2\Phi_{e,a},L^3\Phi_{o,b}),\qquad
 L=A\partial_z+6DA\,z .
\]
这里本篇的 \(R(a,b)=a^2+b^2\) 是频率二次型；原截面 \(R\) 仍是
\((x^3+Y/2)\sigma^6\)，二者不得混同。

## 1. 惰性分支的准确频率函数

设 \(p\ge41,\ p=11\pmod {12}\)，在选定剩余域中取
\(\iota^2=-1\)，则 \(\iota^p=-\iota\)。
对于 \((a,b)\not\equiv(0,0)\pmod p\)，
\[
 (a+\iota b)^{p-1}
 =\frac{a-\iota b}{a+\iota b}.
 \tag{IH1}
\]
分母非零，因为 \(-1\) 在 \(\mathbf F_p\) 中不是平方。
这不是 split 分支的一减去格点指标。

R812 的五个 first-p 端项在
\(\epsilon=\iota^{p-1}=-1\) 时，投到原 even-by-odd 行列后恰剩
\(a^4b\)。原 \(U_e\) 对 \(r\mapsto-r\) 对称，\(U_o\) 对
\(s\mapsto-s\) 反对称，故可以准确作频率的同一偶奇投影：
\[
 \frac12\left(
 \frac{a-\iota b}{a+\iota b}
 +\frac{a+\iota b}{a-\iota b}\right)
 =\frac{a^2-b^2}{a^2+b^2}.
\]
因此保留原 Wilson 负号和五端项后，实际被积函数是
\[
 \boxed{
 a^4b-a^2b^3\frac{a^2-b^2}{a^2+b^2}
 =\frac{a^2b(a^4+b^4)}{a^2+b^2}.
 }
 \tag{IH2}
\]

定义特征零的固定矩阵级数
\[
 \mathcal F_{rs}(q)=
 \sum_{\substack{a\equiv r\ (6)\\b\equiv s\ (6)}}
 \frac{a^2b(a^4+b^4)}{a^2+b^2}\,
 q^{(a^2+b^2)/12},\qquad r,s\in\mathbf Z/6.
 \tag{IH3}
\]
\((a,b)=(0,0)\) 项定义为零。

此级数在每个 \(p=3\pmod4\) 处逐系数整。
确实，若 \(p\mid a^2+b^2\)，则 \(p\mid a,b\)；写
\((a,b)=p^k(a_0,b_0)\)，其中至少一个 \(a_0,b_0\) 是 p 单位，
那么 \(a_0^2+b_0^2\) 是单位，(IH2) 的 p 赋值至少 \(5k\)。
所以它在 \((a,b)\equiv(0,0)\) 的约化自然为零，准确匹配
R812 原多项式端式；没有对一个模 p 零分母直接求逆。

令
\[
 \mathcal P=A^5\lambda^{p+4}\eta^{-2}.
\]
在原 q 函数域中，实际原矩阵因此满足
\[
 \boxed{Q=\mathcal P\,U_e\,\overline{\mathcal F}\,U_o^t.}
 \tag{IH4}
\]
横线只表示上述逐系数的合法模 p 约化。
不在 supersingular 点单独把 \(\lambda,\eta\) 当单位评价。

## 2. 准确的低五阶部分与 harmonic-seven 部分

记
\[
 \mathcal H_7(a,b)
 =7a^6b-35a^4b^3+21a^2b^5-b^7
 =\frac{(a+ib)^7-(a-ib)^7}{2i}.
 \tag{IH5}
\]
它是齐次七次谐多项式，因为两个纯幂都被
\(\partial_a^2+\partial_b^2\) 消掉。
直接乘回 \(a^2+b^2\)，得到完整有理恒等式
\[
 \boxed{
 \frac{a^2b(a^4+b^4)}{a^2+b^2}
 =\frac{25a^4b+10a^2b^3+b^5}{32}
  +\frac{\mathcal H_7(a,b)}{32(a^2+b^2)}.
 }
 \tag{IH6}
\]
它也可由 \(w=a+ib,v=a-ib\) 展开核对：分子在 \(wv=0\)
上的纯谐部分是 \((w^7-v^7)/(64i)\)。

定义同一六阶特征的固定级数
\[
 \mathcal E_{rs}(q)=
 \sum_{\substack{a\equiv r\ (6)\\b\equiv s\ (6)}}
 \frac{\mathcal H_7(a,b)}{a^2+b^2}
 q^{(a^2+b^2)/12},
 \tag{IH7}
\]
仍将零频率项定义为零。
同一赋值论证证明其在所有本分支 p 处整。
设
\[
 \mathcal T_{7,rs}(q)=
 \sum_{a\equiv r,\ b\equiv s\ (6)}
 \mathcal H_7(a,b)q^{(a^2+b^2)/12}.
\]
则
\[
 \boxed{\theta_q\mathcal E_{rs}=\mathcal T_{7,rs}/12.}
 \tag{IH8}
\]
这是一条固定 harmonic theta 级数的**一次 q 原函数**。
通常权八 cusp form 的标准 Eichler 积分要取七次原函数；
不能不作进一步转换就把任何关于标准 Eichler 积分的结论用于 (IH7)。

这条 harmonic theta 输入本身不为零：
\(\mathcal T_{7,0,1}\) 的最低 \(q^{1/12}\) 项来自 \((a,b)=(0,1)\)，
其系数为 \(-1\)。这并不证明经过原 \(U_e,U_o\) 之后的
指定 FG 值不为零。

## 3. 低五阶部分改回原 Gaussian 的全部条目

置 \(h_0=E_2\lambda^2/4=3DA/A\)，暂只在原 q 字段使用。
未乘 Gaussian 的低矩与原截面的关系为
\[
 T_0=\Phi(0),\quad T_1=\Phi'(0),\quad
 T_2=\Phi''(0)+2h_0\Phi(0),
\]
\[
 T_3=\Phi'''(0)+6h_0\Phi'(0),\quad
 T_4=\Phi''''(0)+12h_0\Phi''(0)+12h_0^2\Phi(0),
\]
\[
 T_5=\Phi'''''(0)+20h_0\Phi'''(0)+60h_0^2\Phi'(0).
 \tag{IH9}
\]
使用原 R812 的低 jets，且
\(\mathcal P/(\eta^{-2}\lambda^5)=A^6\)，(IH6) 的多项式部分
在原四乘二基中精确给
\[
 \boxed{
 Q_{\rm poly}=
 \begin{pmatrix}
 0&0\\
 0&75A^6/4\\
 -15A^6/4&135A^5DA/2\\
 -45A^5DA/2&27XA^6/4+135A^4(DA)^2
 \end{pmatrix}.
 }
 \tag{IH10}
\]
例如进入 FG 的原导数为 \(F^{(4)}(0)=24\)、
\(G'(0)=1\)，故系数为 \(25\cdot24/32=75/4\)。
进入 HJ 的原导数为 \(H''(0)=2,J'''(0)=-6\)，
故系数为 \(10\cdot2\cdot(-6)/32=-15/4\)。
其余三项由 (IH9) 的 Gaussian 交项产生，不能删去。

因而原完整等式是
\[
 \boxed{
 Q-Q_{\rm poly}
 =\frac{\mathcal P}{32}\,
 U_e\,\overline{\mathcal E}\,U_o^t.
 }
 \tag{IH11}
\]
(IH10) 是多项式，因此在 \(A(P_0)=0\) 处确实为零。
本分支的原交替卷积全部落在 (IH11) 的指定 FG 余项中：
\[
 (6B)^5\sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j
 =
 \left[
 \frac{\mathcal P}{32}U_e\overline{\mathcal E}U_o^t
 \right]_{FG}\bigg|_{P_0}.
 \tag{IH12}
\]
右边作为**整体**由 (IH11) 与原 first-p Q 定义；
没有单独令不合法的 q gauge 在 \(P_0\) 取值。

(IH10) 不被宣称是 R812 惰性源方程的完整特解。
(IH11) 的余项一般仍有源；不能照 split 分支的
\(Q-Q_{\rm part}\) 水平性将它擅自改成一个 Frobenius 常数矩阵。

## 4. 准确剩余障碍

split 分支 R812 使用 norm-p Gaussian 素理想重指标，
把原余项降到四个低五阶矩与六个固定 Heisenberg 运输值。
对于 \(p=3\pmod4\)，\(\mathbf Z[i]\) 没有 norm-p 素理想，
而 (IH1) 真正给的是商，而非指标；
不能把该六案例结论搬到这里。

现在剩下的对象已固定为 (IH7)--(IH12)，不是任意 theta 导数：

- residue classes 精确为原 \(r,s\bmod6\)；
- 原 \(U\) 与共同尺度严格沿用 R812；
- 原 Gaussian 没有改动；
- 指定输出是 FG 条目；
- 已剥离并保留了所有低五阶多项式项和 first-p 端项。

尚缺的是一个可在原 \(P_0\) 评价的独立代数/period 比较，
能确定 (IH12) 的实际条目，并证明它为单位。
harmonic theta 输入本身非零、某个转换矩阵可逆、
一般 CM 值定理或一般 Green 函数的对数代数性，都不自动提供这个比较。

即使将来证明 (IH12) 非零，它仍只给未筛临界卷积；
R770 同一个真本原 \(h\) 的 Legendre 与两条 Cartier 因子共同非零
仍须另证。本文没有新增有限素数窗口或运行新的数学计算。
