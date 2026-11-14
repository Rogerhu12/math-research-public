# 固定物理头逆 gauge 列：实际 source 分量的额外一阶尾强度

日期：2026-11-14。作者：Astra-ISP-789f，AI-assisted，GPT-6 Astra Pro。

状态：本稿证明固定物理测试的完整 inverse-gauge 列在真实 source
正交分量上具有 \(S_m^{a+1}\) 的平方范数预算。它只使用完整 joined
Gram 的逆块、原真实物理头及原尾。没有把此小量通过未支付的 forward
gauge 恢复为原测试列的小量。普通 ISP 与 \(N=M\) 仍为 OPEN。

依赖的定义与域见
[固定物理头 Euler、完整反馈与 inverse-gauge 联合列稿](2026-11-14-fixed-physical-head-euler-feedback-and-inverse-gauge-joint-column-budget-789f-next.md)。
下面重列所有用于新不等式的对象。

## 1. 同一个物理 joined 空间

固定原头长度 \(d=2^m\)，固定整数 \(0\le a<d\)，孔切口 \(q\ge a\)。
固定参数的全部完整层最小逆均采用原物理 Hilbert 内积。
尾删除为
\[
 D=D_m=\sum_{\nu\ge m}b_\nu E_\nu,\qquad
 b_\nu=(\nu+1)^{-2},\qquad
 S=S_m=\sum_{\nu\ge m}b_\nu^2.
\]
\(\Omega\) 为原尾真空。若 \(m\ge1\)，则
\[
0<S\le\frac1{3m^3}\le1.
\tag{1.1}
\]
原真实头满足 \(A_m=F_m(B_m)\)，\(\psi_m=F_m^{-1}\) 是零点处的
真实逆芽，\(F_m'(0)=d_0^{-1}\)、\(d_0=W_1=e^{-20}\)。
\(W_i=\prod_{\ell=1}^i\alpha_{v_2(\ell)}\) 始终为原链权，\(W_0=1\)。

使用同一 first-head 参数空间 \(\mathcal F\)、原 bare 压缩 \(\delta\)
及实际 joined 核列 \(T\)。其第 \(i\) 个物理头行是
\[
 T_i=W_i^{-1}\psi_m(-\delta)^i,\qquad 0\le i<d,
\quad T_0=I,\quad \Gamma=T^*T\succeq I.
\tag{1.2}
\]
令 \(\mathcal C=\ker\mathcal B\) 为全部真实零源，\(\mathcal U=\mathcal C^\perp\)，
其中 \(\mathcal B\) 是同稿完整 cut-source 映射。
特别全部 first-head 输入孔层 \(\le q\) 都在 \(\mathcal C\) 中。
在 \(\mathcal C\oplus\mathcal U\) 上写
\[
 \Gamma=\begin{pmatrix}\Gamma_{CC}&\Gamma_{CU}\\
                       \Gamma_{UC}&\Gamma_{UU}\end{pmatrix},
\quad
 R_U=\binom{-\Gamma_{CC}^{-1}\Gamma_{CU}}{I},
\quad
 \mathcal S=R_U^*\Gamma R_U.
\tag{1.3}
\]
\(\Gamma_{CC}\) 和 \(\mathcal S\) 有界严格正。真实正交 source 等距列是
\[
 I_U=T R_U\mathcal S^{-1/2}.
\tag{1.4}
\]
因此下面的范数是实际物理最小 joined 核的正交分量，并非仅换了源坐标的
某个欧氏范数。

## 2. 固定 inverse-gauge 列的准确 forcing

取 \(f_a=e_a\otimes\Omega\)，令 \(f_0(z)=F_m(z)/z\)，
\[
 G_a=f_0(B_m)^{-a},\qquad
 h_a=G_a^{-*}f_a
     =\frac{(A_m^*)^a(e_0\otimes\Omega)}{W_a}.
\tag{2.1}
\]
原核方程与同一真实 chain 给
\[
 T^*h_a=y_a,\qquad
 y_a=\frac{(-D^*)^a\Omega}{W_a}.
\tag{2.2}
\]
条件 \(q\ge a\) 保证这些低层中 \(\delta^*=D^*\)，没有 bare 商损失。
\(y_a\) 在输入 degree \(a\) 上；因 \(a<d\)，它属于
\(\ker D^d\)，并且 \(y_a\in\mathcal C\)。

定义 inverse-gauge 列的真实 source 分量
\[
 b'_a=I_U^*h_a.
\]
由 (1.3)–(2.2)，准确有
\[
 \boxed{
 b'_a=-\mathcal S^{-1/2}\Gamma_{UC}\Gamma_{CC}^{-1}y_a .
 }
\tag{2.3}
\]

## 3. 完整逆的 CC 块给新的正预算

整块逆公式给
\[
 (\Gamma^{-1})_{CC}
 =\Gamma_{CC}^{-1}
 +\Gamma_{CC}^{-1}\Gamma_{CU}\mathcal S^{-1}
       \Gamma_{UC}\Gamma_{CC}^{-1}.
\tag{3.1}
\]
故 (2.3) 的真实范数满足精确身份
\[
 \boxed{
 \|b'_a\|^2=
 \left\langle y_a,
 [(\Gamma^{-1})_{CC}-\Gamma_{CC}^{-1}]y_a\right\rangle .
 }
\tag{3.2}
\]
此处先取完整 \(\Gamma^{-1}\)，再取 CC 块；没有交换压缩与求逆。

由 \(\Gamma\succeq I\) 得 \(\Gamma^{-1}\preceq I\)，所以
\[
 \|b'_a\|^2
 \le\langle y_a,(I-\Gamma_{CC}^{-1})y_a\rangle
 \le\langle y_a,(\Gamma_{CC}-I)y_a\rangle.
\tag{3.3}
\]
最后一步是在 \(\Gamma_{CC}\succeq I\) 上应用
\(1-x^{-1}\le x-1\)。右端是同一低输入的完整 excess Gram，
并未另选新的 primitive source 或右链。

## 4. 完整 excess Gram 只需固定 \(a\) 个低系数

写
\[
 c_{ij}=[w^j]\psi_m(w)^i.
\]
对 \(y_a\) 作用时，所有 \(D^j y_a\) 的 \(j>a\) 项为零。
不同 \(j\) 的输出位于互相正交的物理尾 degree \(a-j\)。
再按不同物理头 \(i\) 求和，得到准确的有限正和
\[
 \boxed{
 \langle y_a,(\Gamma_{CC}-I)y_a\rangle
 =\frac1{W_a^2}
   \sum_{i=1}^{a}\frac1{W_i^2}
   \sum_{j=i}^{a}|c_{ij}|^2
       \|D^j(D^*)^a\Omega\|^2 .
 }
\tag{4.1}
\]
各项的符号不影响此平方和。这里没有使用一般 \(\Gamma\) 或 source
Schur 导数的范数；它们在原模型中可很大。

当 \(a\) 固定、\(d>a\) 时，\(c_{ij}\) 所需的所有 Taylor 系数
只取决于原有限的低位符号，因而与后来增大的 \(m,q\) 无关。
这对原 \(N\) 和 \(Y\) 两个符号分别成立。

## 5. 原尾幂的自含费用

令 \(z_\nu=b_\nu^2\)。对 \(|K|=a-j\)，真实硬核删除的系数为
\[
 [e_K]\,D^j(D^*)^a\Omega
   =a!\,j!\,b_K\, e_j(z_{\nu:\nu\notin K}).
\tag{5.1}
\]
确实，\((D^*)^a\Omega=a!\sum_{|I|=a}b_I e_I\)；
从 \(I\) 删除 \(j\) 位共有 \(j!\) 个次序，而剩余 \(K\) 固定后新增集合
与 \(K\) 不交。这在无限尾上也成立，正系数平方和由单调有限截断得到。

用 \(e_j(z_{\nu\notin K})\le S^j/j!\) 及
\(e_{a-j}(z)\le S^{a-j}/(a-j)!\)，得到
\[
 \boxed{
 \|D^j(D^*)^a\Omega\|^2
 \le\frac{(a!)^2}{(a-j)!}\,S^{a+j}.
 }
\tag{5.2}
\]
因此定义真正有限、只依赖固定物理头 \(a\) 及所选 \(N/Y\) 符号的常数
\[
 K_a=\frac{(a!)^2}{W_a^2}
       \sum_{i=1}^{a}\frac1{W_i^2}
       \sum_{j=i}^{a}\frac{|c_{ij}|^2}{(a-j)!},
 \qquad a\ge1.
\tag{5.3}
\]
由 \(S\le1\)、\(j\ge1\)，(3.3)–(5.2) 给
\[
 \boxed{
 \|b'_a\|^2\le K_a S_m^{a+1}
 \le \frac{K_a}{(3m^3)^{a+1}}
 \quad(m\ge1,\ d>a,\ q\ge a).
 }
\tag{5.4}
\]
这是同一 inverse-gauge 列的 source 分量，比已付整列的
\(a!S_m^a/W_a^2\) 平方范数预算多一阶 \(S_m\)。

### 真空与首物理头

若 \(a=0\)，则 \(y_0=\Omega\)、\(T_i\Omega=0\) 对 \(i\ge1\)，
\(\Gamma\Omega=\Omega\)。因此
\[
 b'_0=0.
\tag{5.5}
\]
此时原 \(f_0=e_0\Omega\) 本来就是真左零核，原 source 分量也为零。

若 \(a=1\)，仅 \(c_{11}=d_0=W_1\) 出现，且
\(D D^*\Omega=S_m\Omega\)。于是不必使用粗基本对称式界：
\[
 \boxed{\|b'_1\|^2\le S_m^2/d_0^2.}
\tag{5.6}
\]

## 6. 本稿明确没有支付的恢复

在同一物理 \(\mathcal C\)-核与 source 正交分解中，写
\[
 G_a|_{\mathrm{joined}}
 =\begin{pmatrix}G_C&K\\0&G_U\end{pmatrix},
\qquad
 P_{\mathrm{joined}}h_a=I_Cc'_a+I_Ub'_a .
\]
原固定测试的 source 列仍准确为
\[
 \boxed{b_a=K^*c'_a+G_U^*b'_a.}
\tag{6.1}
\]
(5.4) 不控制任意大的 \(G_U^*\) 或 \(K^*\)，更不允许分别删掉这两项。
尤其不能把 \(b'_a\to0\) 写成原 \(b_a\to0\)。
后续仍须在真实两费用或原 \(W=\ker(B|_M)^*\) 条件下支付
(6.1) 的共同恢复。本稿无需旧联合旗的孔窗假设，也没有扩大该旗的
\(\delta\) 预算。
