# 实际有限偏移的原页读取：两条真左行只读取哪些 affine carry

日期：2026-11-20。**状态：完整符号推导，无数学执行。** 本补件接
《原完整来源的平方／立方有限偏移》。它不新增自由有限类，
而把该文两条实际行的值直接写回原 p／p² 方程。
特别说明一段高 tau 范围中，第一修正若存在，其非物理有限类已经
被原 p² 方程迫为非零；不能再希望同一方程把它消成自然陪集。

## 1. 同一整输入、已付 normal 行和真实三条带

保 R934/R936/R937 的所有原对象及窗口，仍有

\[
 J=s-2,\qquad T=s-15,\qquad L=\ell-2,\qquad
 s=2h+d_0+2,\quad1\le d_0\le13,\quad \tau\ge2.
\]

以原字面重记账写

\[
 P_0=P^{\rm fact},\quad R_0=R+\Delta,\quad
 P+pR=P_0+pR_0,\quad \Delta=(P-P_0)/p.                         \tag{1}
\]

以下 R_0 是同一原整来源，B=bar R_0/(qt²)；没有换一组 R。
假定它至少通过完整第一次提升

\[
 \boxed{M(P_0+pR_0)\in p^2\Gamma.}                            \tag{2}
\]

用 R928(9) 的同一个实际固定目标 F_i^{P0}，定义

\[
 \delta_i=
 [W_i^{\rm act}(R_0)]_{<s}\bmod p-\mathcal F_i^{P_0}
       \quad(i=0,1,2).                                      \tag{3}
\]

(2) 准确给 delta_i 的 <s−13 部分为零，以及第四短行误差模 w^ell 为零。
因此定义真实十三尾

\[
 C_i(w)=\sum_{v=0}^{12}[w^{s-13+v}]\delta_i\,w^v,\qquad
 \delta_i=w^{s-13}C_i\pmod{w^s}.                              \tag{4}
\]

它们不是任选的三个多项式。记同一原 affine carry 残差

\[
 \mathcal U_j(P_0,R_0)=
 \frac{\mathcal K_{j,1}(P_0)}p+
 \mathcal K_{j,1}(R_0)+\mathcal K_{j,2}(P_0)\pmod p,
 \qquad j=1,2,3.                                             \tag{5}
\]

此处真正的除 p 整性由 (2) 及 R928(8) 支付。
R928(6)、(13) 的完整实际轴合并逐项给

\[
 \boxed{\quad
 C_0=\mathcal U_1,\qquad
 C_1=a^{-1}\mathcal U_2,\qquad
 C_2=2a^{-2}\mathcal U_3.\quad}                               \tag{6}
\]

向量按 v=0,...,12 写成 w 多项式。
H_p B 的低项已包含在实际 K 中，未再次赋零。
原 S 在这些行前面带 p³，所以 (5) 不因选一个 S 改变。

## 2. 完整 q／charge 单位逆的有限尾式

仍用 R928(16) 的同一实际 U(w)，及

\[
 q_j(t)=[(E+40)^jq](t,g(t)),\qquad
 r_1=q_1/q_0,\quad r_2=q_2/q_0.
\]

q0 是实际单位，q1、q2 保全部 q 导数及四十；它们不替成自由量。
令

\[
 \begin{split}
 \alpha(t)&=U(w(t))^{-1}\left(\frac{w(t)}t\right)^{s-13},\\
 \beta(t)&=\alpha(t)/q_0(t),\qquad
 \widetilde C_i(t)=C_i(w(t)).
 \end{split}                                                \tag{7}
\]

所以 beta 是原完全确定的单位。
先乘 U^{-1}，再除已经付整除的 t²，再作同一下三角逆，
得到归一化误差

\[
 e_i=E^iB(t,g)-f_i^*\quad(i=0,1,2),\qquad
 e_3=E^3B(t,g)-f_3^* .
\]

其完整尾式为

\[
 \boxed{\begin{aligned}
 e_0&=t^T\beta\,\widetilde C_0,\\
 e_1&=t^T\beta(\widetilde C_1-r_1\widetilde C_0),\\
 e_2&=t^T\beta\{\widetilde C_2-2r_1\widetilde C_1
                    +(2r_1^2-r_2)\widetilde C_0\}
                         \pmod{t^J},\\
 e_3&=0\pmod{t^L}.
 \end{aligned}}                                             \tag{8}
\]

例如第二式来自 z1−q1(z0/q0)；第三式先减 2q1 e1 和 q2 e0，
故 C0 的系数是 2r1²−r2，不是 r1²−r2。
因 t^T=t^{s-15}，(7) 的 w/t 指数是 s−13，不能改成 T。

当前实际待实现的目标是

\[
 f_i=f_i^*-E^iB(t,g)=-e_i .                                  \tag{9}
\]

由 h+T=J+h−13>J 及 2h+L>J，R928 的完整二次逆 Taylor 立即给

\[
 \boxed{j_0=-e_0,\qquad j_1=-e_1\pmod{t^J}.}                 \tag{10}
\]

这是在 (2) 后由同一个原误差推得的精度结论；
不是对任意给定 B 删除 eta² 项。

## 3. R936：固定行恰读前两条带各至多十三位

保 R936 的低 tau 门

\[
 2\le\tau\le d_0+1,\qquad
 K=2h+\tau-2<J,\qquad K+e_+>3\kappa .
\]

lambda+ 仍是原完整 H0(N³(−Z+)) 矩阵构造出的同一真行。
该文固定值及有限类记号为

\[
 c_1=-11U_*(0)/a,\qquad
 \ell_2(B)=\lambda_+((E-3b)B|_C),\qquad
 c_1-\bar\ell_2(\beta_2).
\]

用 (9)–(10)，准确得到

\[
 \boxed{\begin{aligned}
 c_1-\bar\ell_2(\beta_2)
 &=-\lambda_+(e_1-3be_0)\\
 &=-\lambda_+\!\left(
 t^T\beta\{\widetilde C_1-(r_1+3b)\widetilde C_0\}
 \right).
 \end{aligned}}                                             \tag{11}
\]

因此这个固定原行只需要 (5) 前两条带的前

\[
 \boxed{q_{\rm low}=K-T+1=12+\tau-d_0\in[1,13]}               \tag{12}
\]

个实际系数；第三带不进入 (11)。
理由是 lambda+ 的最大次数是 K，而整个括号已带 t^T。
代入 w(t) 的线性首项非零，读取 <q_low 项也只需原 C_i 的
<q_low 项，以及同一真实 beta、r1、w/t 的对应低位。

这把“有限偏移是否抵消 −11”写成原 affine carry 的完整已指定行。
它没有证明该 carry 行非零。
全部三条带及其它原行仍须联立；单独 (11) 为零不是可提升的充分条件。

## 4. R937：固定 normal 行只读零至十二位 carry

保 R937 的高 tau 门

\[
 \begin{gathered}
 d_0+2\le\tau<\min(h+2,\ell),\qquad
 n=h+\tau-2,\quad m=n+1\le\min(2h,h+L),\\
 n+2e_+>3\kappa .
 \end{gathered}
\]

lambda2 与 Lambda2 均是该文的同一实际行，c2 仍为其单位
28 zeta0^{-s} uhat0³ e0/a。
由 e3=0 mod t^L、m<=h+L，(9) 的 eta e3 在读取范围内为零。
再用 (10)，得到

\[
 \boxed{\begin{aligned}
 c_2-\bar\ell_3(\beta_3)
 &=-\lambda_2\{e_2-(6b-1)e_1+3b(3b-1)e_0\}\\
 &=-\lambda_2\!\left[t^T\beta\left\{
      \widetilde C_2-(2r_1+6b-1)\widetilde C_1
      +A_0\widetilde C_0\right\}\right],\\
 A_0&=2r_1^2-r_2+(6b-1)r_1+3b(3b-1).
 \end{aligned}}                                             \tag{13}
\]

所有 xi、U0/P134、q 导数仍通过原 f*、C_i 和真实单位进入；
(13) 没有另选一次 high-axis lift。

所需的每条带长度准确为

\[
 \boxed{q_{\rm high}=\max(0,m-T)
      =\max(0,\tau-h-d_0+12)\le13-d_0\le12.}                  \tag{14}
\]

上界使用实际整数 tau<=h+1，不延长第四短块。
这里不是将 C_i 的其余系数设零，而是证明同一真行没有读取它们。

### 一个明确的页数结论

若

\[
 \boxed{m\le T
        \quad\Longleftrightarrow\quad
        \tau\le h+d_0-12,}                                   \tag{15}
\]

则 (13) 的整个右侧为零，无需任何下一页 carry 条件。
于是对每一个已经满足 (2) 的实际第一修正，若它存在，

\[
 \boxed{\bar\ell_3(\beta_3)=c_2\ne0,\qquad\beta_3\ne0.}       \tag{16}
\]

这里的 beta3 已在前篇由原四低门消掉物理点，只在全部
Z3^away 的真实来源像上读取。
所以在 (15) 的范围，原 p² 方程不会再迫这个 away 类为零：
它已经迫其对实际行取准确的抵消值 c2。

(16) 不证明第一修正一定存在，也不证明完整 p³ 存在。
它排除了“先用同一 p² 方程把 beta3 消为零，再利用 R937 自然单位”
这一未经支付的推断。
若能另从真实全球来源证明 beta3=0，就直接与 (2)、(16) 矛盾。

## 5. 真 beta1 与受限 S：哪些差确实不能改变该读数

对任意 Z∈K1=ker bar M，用其同一原整提升读取
K_{j,1}(Z) mod p。因为原最前十三行的 bar M 全为零，
这三个向量正是完整首 Bockstein beta1(Z) 的真实目标行；
不依赖整提升。

对这个齐次 Z，按 (7)–(8) 把 C_i 换成

\[
 C_0=K_{1,1}(Z),\quad C_1=a^{-1}K_{2,1}(Z),\quad
 C_2=2a^{-2}K_{3,1}(Z).
\]

前篇的 bar-ell2(beta2(Z))、bar-ell3(beta3(Z))
分别等于 (11)、(13) 去掉开头负号后的同一显示表达式。
因此它们在完整 K2=ker beta1 上为零。
在 (15) 的高 tau 范围，bar-ell3 甚至在整个 K1 的实际有限像上为零。

这说明 (16) 对第一修正的全部实际差保持，
不是只对 jH3、D3 或 native 尾保持。
一般范围仍只付 K2 不变性；不能把 K1 全赋为 K2。

当 R 已固定，原 S 的选择不能改变 (5)。
对两个完整 p³ 解，相减后同一 R 差属于 K2；
若 S 受限，还须同一个允许 S 差补偿全部剩余行。
以上没有给反向存在性，也没有把三个显示 Bockstein 向量
替换成完整 beta1 的全部目标。

