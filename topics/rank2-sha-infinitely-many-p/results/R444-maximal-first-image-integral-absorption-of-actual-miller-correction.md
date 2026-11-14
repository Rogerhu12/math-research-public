# R444：原首像最大时实际 Miller 修正的整来源吸收

日期：2026-11-14。**状态：已证明。** 本篇确定 R390/R403 的实际低轴修正在什么真正来源范围内能够作用于第二障碍。若原模 \(p\) 像已等于完整 \(w^{13}\) 理想，则整个 \(p^2A_0\) 修正可由同一有限自由来源的整基变换吸收；所有真实 \(P_2,\lambda_2\) 上的 Miller 修正配对严格为零。这个结论不要求相对 \(J\) 整满射，也不要求真正 \(P_2\) 为空。特别，R428 的唯一 carry 掉秩线虽可有一维真第二核和十四维 \(C_2\)，仍属于本篇的零修正范围。一般情况下，全部低轴修正的像通过一个明确的首像缺口，维数有准确上界。两条完整中央的基准项及最高两行均保持，没有据此断言原中央非零。

## 1. 同一原来源与完整目标理想

固定

\[
p=6s-1>83,\quad 1\le\ell<s-13,\quad L=2s+\ell,
\quad T_0=L+13<3s,
\]

以及 R403/R406 的同一有限自由原来源

\[
\mathcal W_{D,J}=\bigoplus_{n=0}^D\bigoplus_{j=0}^J
\mathscr R^nq_n(t)\mathcal O[t]_{\le e_{n+1}}T^j,
\qquad 0\le J\le16.
\tag{1}
\]

总 Euler 在显示列上的值是 \(n+40+\alpha j\)，其中 \(\alpha=36/17\)。保持原完整物理矩阵

\[
\mathsf M=c_*U_0m_{13}J:\mathcal W_{D,J}\longrightarrow
Y=\Gamma_{T_0}.
\tag{2}
\]

\(U_0\) 含全部 \(P_{134}\)、公共 theta 和 Gaussian；没有把它替换为常数。在剩余目标

\[
\bar Y=k[w,\epsilon]/
(w^s,\epsilon^3,w^{\ell+13}\epsilon^2)
\]

中定义实际理想

\[
I_{13}=w^{13}\bar Y.
\tag{3}
\]

它在三块中的基分别是

\[
\{w^r:13\le r<s\},\quad
\{\epsilon w^r:13\le r<s\},\quad
\{\epsilon^2w^r:13\le r<\ell+13\}.
\]

因此

\[
\dim_k I_{13}=L-26,
\qquad I:=\operatorname{im}\bar{\mathsf M}\subset I_{13}.
\tag{4}
\]

两个十三行 carry 带在 (4) 中均被保留：它们在整 \(m_{13}\) 上乘 \(p\)，而在这里的模 \(p\) 像中消失。原最初十三行也仍在 \(\bar Y/I_{13}\) 中。因为 \(c_*U_0\) 是整个目标中的乘法单位，它保持理想 \(I_{13}\)，故 (4) 是原物理矩阵的断言，不只属于剥去载体的辅助矩阵。

定义首像缺口

\[
G=I_{13}/I,\qquad
\gamma=\dim_kG=L-26-\operatorname{rank}_k\bar{\mathsf M}.
\tag{5}
\]

这里 \(G\) 只是明确的向量空间商；一般 \(I\) 不保持目标乘法，不能预先把它称为商环或模理想。

## 2. 修正通过真正的首像缺口

固定 R385/R388 的同一个实际提升、原第三坐标及低轴

\[
A(t)=\bar A_0^\sharp(t)\in tk[t]_{<s}.
\]

R403.(24) 对整个 (1) 给出的完整比较是

\[
\boxed{
\mathsf M-\mathsf M^\sharp
=p^2A(t(w))\,\bar{\mathsf M}\mathcal E_{\rm tot}
\pmod{p^3}.
}
\tag{6}
\]

右边以任意整提升读取模 \(p^3\)，结果与提升无关。两个矩阵模 \(p^2\) 相同，因此使用同一个真实 \(P_2\in K_2\)、同一个可提升左核 \(\lambda_2\)，以及同一个首 Bockstein \(\beta_1\)。记

\[
C_1=\bar Y/I,\qquad C_2=C_1/\beta_1(K_1).
\]

\(G\) 自然嵌入 \(C_1\)。令

\[
G_2=\operatorname{im}(G\longrightarrow C_2).
\tag{7}
\]

**定理 1。** 对 (6) 的实际 \(A\)，以及同一目标中的任意指定乘子 \(A\)，修正

\[
\delta_A(\bar P)=
\bigl[A\,\bar{\mathsf M}(\mathcal E_{\rm tot}\bar P)\bigr]
\in C_2
\tag{8}
\]

的像都包含于 \(G_2\)。全部这种修正的线性张成维数至多 \(\dim G_2\le\gamma\)。特别

\[
\boxed{\gamma=0\ \Longrightarrow\ \delta_A=0
\text{ 对所有真正第二核输入和所有 }A.}
\tag{9}
\]

**证明。** \(\mathcal E_{\rm tot}\bar P\) 仍是同一来源的向量，虽然未必是核向量；所以 \(\bar{\mathsf M}(\mathcal E_{\rm tot}\bar P)\in I\subset I_{13}\)。\(I_{13}\) 是目标理想，故其乘 \(A\) 后仍在 \(I_{13}\)。在真实 \(C_1\) 再商掉完整 \(\beta_1(K_1)\) 后，其像正通过 (7)。不需要假设 Euler 保持核，也没有把 \(\beta_1\) 的像删去。\(\square\)

## 3. 最大首像时，整个修正可由原来源基变换吸收

**定理 2。** 若

\[
\operatorname{rank}\bar{\mathsf M}=L-26,
\tag{10}
\]

则存在同一个有限自由来源上的整自同构

\[
V_A=1+p^2C_A\pmod{p^3},
\qquad V_A^{-1}=1-p^2C_A\pmod{p^3},
\]

使

\[
\boxed{\mathsf M=\mathsf M^\sharp V_A\pmod{p^3}.}
\tag{11}
\]

它在模 \(p^2\) 来源上是恒等，因此所有第一次提升、真正第二核及左核都按原规范识别。对这些同一个提升，准确有

\[
\boxed{
\langle\lambda_0,d_2^{\rm orig}(\bar P)\rangle
=d^\sharp(P_2,\lambda_2).
}
\tag{12}
\]

**证明。** 由 (4)、(10)，\(I=I_{13}\)。选择满射
\(\bar{\mathsf M}:\mathcal W_{D,J}/p\to I_{13}\)
的任一线性右逆 \(R\)。因为目标中
\(A\bar{\mathsf M}\mathcal E_{\rm tot}\) 的像在 \(I_{13}\)，可取

\[
\bar C_A=R\,A\bar{\mathsf M}\mathcal E_{\rm tot}.
\tag{13}
\]

于是 \(\bar{\mathsf M}\bar C_A=A\bar{\mathsf M}\mathcal E_{\rm tot}\)。把 (13) 任意整提升后代入 (6)，得到 (11)。这只是原有限自由来源内部的可逆列变换；没有增加角列、负幂或新的算术来源。

对真实 \(P_2\)，两个矩阵模 \(p^2\) 相同；(11) 在除以 \(p^2\) 后给出的差是 \(\bar{\mathsf M}(\bar C_A\bar P)\)，属于实际首像，故在整个 \(C_2\) 中为零。这证明 (12)，也证明该结论与允许的首次提升选择相容。\(\square\)

这项来源吸收不等于另选 theta 模型将 \(A_0\) 规范掉：\(\mathsf M^\sharp\) 和两条中央基准仍固定为原来的选择。它只证明在 (10) 下，这个确定的低轴修正对原有限矩阵的第三精度不再提供独立障碍。

## 4. 原双线性转置逐项为零，而不只对实际 forcing 为零

在剥去完整 \(c_*U_0\) 后的同一个规范中，真实 \(\bar P\) 有

\[
[W_0]_{<s}=[W_1]_{<s}=0,\quad [W_2]_{<\ell}=0,
\quad W_i=(\mathcal E_{\rm rel}^i\bar P)_{\rm reg}.
\]

原 \(t=0\) 只容 \(j=0,n=0,1,2\) 三个常数部分，故其三条 Euler 值为零又给全部 \(W_i(0)=0\)。R390 的公式因而原样推广到 (1)：

\[
\begin{aligned}
\mathfrak B_{P,\lambda}(A)={}&
a\sum_{r=0}^{s-14}\lambda_{1,r+13}[w^r](A W_2)\\
&+\frac{a^2}{2}\sum_{r=0}^{\ell-1}
\lambda_{2,r+13}[w^r](A W_3).
\end{aligned}
\tag{14}
\]

在 (10) 下，\(\lambda_0\) 杀掉整个 \(I_{13}\)。完整 \(U_0\) 的逆仍保持该理想，故 (14) 的每一个 \(\lambda_{1,r+13}\)、\(\lambda_{2,r+13}\) 都为零。因此

\[
\boxed{\eta_k(P,\lambda)=\mathfrak B_{P,\lambda}(t^k)=0
\quad(1\le k<s).}
\tag{15}
\]

R390 的倒序伴随递推 \(d_kc_k-u_{k+1}c_{k+1}=\eta_k\)、\(c_s=0\) 随之给 \(c_k=0\) 全部成立。故其实际 Miller forcing 残数测试本身为零；这个结论不是从某个 Cartier 单位或某个偶然 forcing 值推出的。

一般 \(\gamma>0\) 时，仍保留 R390 的真实支持界
\(\eta_k=0\) 于

\[
k>\max\{0,s-14-\ell,\ell-2\}\le s-15,
\]

以及定理 1 的实际像上界。不能将这两个界解释为剩余权可以自由选择。

## 5. 首像缺口的准确计算矩阵

令 \(\Phi_{n,k,j}\) 为 (1) 的原列，\(q=n+\alpha j\)，并用其真实 regularized 普通部分。\(m_{13}\) 模 \(p\) 只删除相对第一、第二块各自最后十三行。因此

\[
\boxed{
\gamma=L-26-
\operatorname{rank}
\begin{pmatrix}
([w^r]\Phi_{\rm reg})_{0\le r<s-13}\\
(q[w^r]\Phi_{\rm reg})_{0\le r<s-13}\\
(q^2[w^r]\Phi_{\rm reg})_{0\le r<\ell}
\end{pmatrix}.
}
\tag{16}
\]

省去的 \(a,a^2/2\) 是已经明确的行单位。换到原 \(t\) 坐标只在各个前缀中作单位三角变换；因所读次数均小于 \(s\)，也可直接使用固定原 \(\Theta^{17n+36j}d^nq_n(fV)^jt^k\) 的系数。式 (16) 是真正较短的来源评价，不需计算任意环境左核。

一个统一充分范围也可直接给出。沿 R412 记

\[
b_n=\lfloor(n+1)/4\rfloor+e_{n+1},\qquad
\rho(r)=\min\{n:b_n\ge r\}.
\]

若

\[
\boxed{
D\ge\max\{1+\rho(s-14),\ 2+\rho(\ell-1)\},
}
\tag{17}
\]

则 (16) 满行秩。证明仍选每个普通首阶的两个、或存在第三层时的三个相邻真实 \(j=0\) 列；R412 的首项 Vandermonde 子式完全相同，这里的前两层仅缩短到 \(s-13\)。所有高项按首阶过滤三角消去，所选列均是原 canonical 基列。于是 (17) 足以保证整个 (11)，而无需先得到较大 \(J\) 的整满射。

## 6. 唯一 carry 掉秩线仍没有低轴修正

在 R428/R434 的 \(\ell=1,N=L\) 方阵中，假设原参考 \(J_\circ\) 为单位方阵。该文已证明，全部高轴参数的原 \(\bar{\mathsf M}_{u,v}\) 相同，且其秩准确为 \(L-26\)。所以本篇 (10) 对整个这个实际有限参数模型成立，包括

\[
1+\tau_pu=0.
\tag{18}
\]

在 (18) 上，真正 \(C_2\) 的维数为十四、\(\ker\beta_1\) 有一维；仍由 (11)–(15) 得到全部 \(A_0\) 修正为零。这里没有以“右核不存在”为理由。那个唯一方向上的 \(d_2\) 必须由完整基准项读取；R428 的 \(\eta_p\) 和原两中央 Hensel 解的第二位仍须准确计算。

特别，要在 (18) 这一方向上获得新的数论限制，单独继续展开 R388 的实际 Miller forcing 不会提供新的第二障碍值。更一般地，若想让这一低轴机制产生非零配对，必须先有 (16) 的真正首像缺口 \(\gamma>0\)，而不只是有 carry 造成的非平凡 \(C_2\)。

两条完整中央条件并未消失。R403 的

\[
B_S+[w^s](A\widehat S^\sharp)=0,\qquad
B_T-B_S+[w^s]\{A\widehat S^\sharp(\widehat H^\sharp-1)\}=0
\]

仍保留其实际基准；两条转置的最高系数分别为
\((-1)^{s-1}/5\)、\(\beta_H(-1)^{s-2}/22\)。定理 2 不赋予这些中央观察以来源基变换下的额外零传播，也不把其基准设为零。它确定的是同一原有限矩阵中低轴修正的准确可见范围。

## 依赖与验证范围

- R338/R351：完整首像、整左右核提升、真实第二 Bockstein 与两个十三行 carry 带。
- R390：实际低轴的双线性测试、有限伴随及固定二挠 Miller 残数。
- R403/R406/R408：共同 \(A_0\)、不同 Gaussian charge、原两来源有限自由格及完整第三精度比较。
- R412：相邻真实 charge 的原单位子式。
- R425/R428/R434：完整两中央 Hensel 基准、唯一 carry 线及固定实际高轴。

证明是同一个原矩阵上的整线性代数及其实际理想结构；没有目标素数扫描。R444 的先行 Padé 工作记录另存于 `notes/2026-11-14-r444-actual-pade-remainder-and-unpaid-angular-boundary.md`，其尚未付清的相邻子式非零不被本篇冒称已经解决。主课题仍未完成。
