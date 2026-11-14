# 固定留数线的真实 GM Frobenius、中央主部差与 theta 源项

日期：2026-11-12。状态：实际二步 GM Frobenius 的标量主部公式、
不同中央权之间的完整留数差、原 theta carry 的同权比较及已知
非零素数的全层校准均已证明。
尚未构造跨中央权的闭合有限维 Frobenius 递推。

本文接续
[中央主部与 Bol 留数](2026-11-12-central-principal-parts-pf-bol-residue.md)，
使用同一个实际 \(M_e,K,L,s,\omega,\eta\)。
特别不把任意给定的 \(C_m\) 当成一个已知的 Frobenius 轨道。
所有素数均为惰性 \(p\ge7\)，置 \(q=p^2\)。

## 1. 实际二步 crystalline 箭头

R68 的行约定是
\[
\Phi(e^\phi)=\mathcal F(t)e,\qquad
e=\binom{\omega}{\eta},\quad \phi(t)=t^p,\quad
\mathcal F=Y(t^p)F_0Y(t)^{-1},
\]
\[
Y=\begin{pmatrix}K&L\\K'&L'\end{pmatrix},\quad
F_0=\begin{pmatrix}0&pa_p\\b_p&0\end{pmatrix},\quad
a_pb_p=-1,\quad \det Y=s^{-1}.
\tag{1}
\]
这些级数、基及 \(F_0\) 都在 \(\mathbb Q_p\) 上，故二步系数
Frobenius 在这里固定它们。由 \(F_0^2=-pI\)，准确有
\[
\boxed{\quad
\Phi^{[2]}(e^{\phi^2})
=-pY(t^q)Y(t)^{-1}e.
\quad}
\tag{2}
\]
矩阵 (2) 是实际整 crystalline 矩阵，不是任意选择的
形式水平解。

为缩短公式，记
\[
K_q=K(t^q),\quad L_q=L(t^q),\qquad
A_q=K_qL'-L_qK',\quad B_q=L_qK-K_qL.
\tag{3}
\]
于是 (2) 的第一行为 \(-ps(A_q,B_q)\)。

对一个有有限极部的标量形式 \(f(t)\omega\,dt\)，还必须拉回
基底微分 \(dt\)，即 \(d(t^q)=qt^{q-1}dt\)。
令
\[
g_f=s\,t^{q-1}f(t^q).
\]
则完整一形式箭头为
\[
\boxed{\quad
\Phi_{\rm dR}^{[2]}(f\omega\,dt)
=-p^3g_f(A_q\omega+B_q\eta)\,dt.
\quad}
\tag{4}
\]
此处的第三个 \(p\) 因子包含基底留数的 Tate twist；
只作用纤维而漏掉 \(dt\) 会得到错误的斜率。

## 2. 消去 \(\eta\) 后的准确标量算子

由 \(\nabla(b\omega)=(b'\omega+b\eta)dt\)，(4) 与下面的
标量一形式相差一个明确 exact 项：
\[
\boxed{\quad
\operatorname{Fr}_2(f)
  =-p^3\left(g_fA_q-(g_fB_q)'\right),\qquad
\Phi_{\rm dR}^{[2]}(f\omega\,dt)
-\operatorname{Fr}_2(f)\omega\,dt
=\nabla(-p^3g_fB_q\omega).
\quad}
\tag{5}
\]
这给一形式级的比较，不只是先指定一个留数后命名其系数。
对 Laurent 级数取严格负次幂部分，记
\(\operatorname{Fr}_2^-(f)=[\operatorname{Fr}_2(f)]_{<0}\)。
它是一个有限 Laurent 多项式。
丢掉的正则部分对两个水平留数都无贡献。

在水平基 \(h=Y^{-1}e\) 中，(2) 是常数箭头 \(-pI\)；
再用形式留数的换元公式
\[
\operatorname{res}_{t=0}qt^{q-1}H(t^q)\,dt
      =q\,\operatorname{res}_{t=0}H(t)\,dt,
\]
得到对任意这种 \(f\)
\[
\operatorname{Res}_0
 \bigl(\operatorname{Fr}_2^-(f)\omega\,dt\bigr)
      =-p^3\operatorname{Res}_0(f\omega\,dt).
\tag{6}
\]
这与 R94 的几何留数基上 \(\Phi^2=-p^3\) 完全一致。

## 3. 实际中央主部不能直接当作这个 Frobenius 轨道

对 \(m\equiv0\pmod4\)、\(m\ge4\)，实际中央主部为
\[
f_m=t^{-m-1}
 \left[\frac{M_eK^{m-1}}{sJ^{m+1}}\right]_{\le m}.
\tag{7}
\]
其最高极点阶为 \(m-3\)，首系数为一；
水平留数为 \((C_m,0)\)。
当 \(m=4\) 时 \(f_4=1/t\)；以下极点比较对所有 \(m\ge4\) 成立。

令
\[
h=q(m-4)+1.
\]
由 \(A_q=1+O(t^2)\)、\(B_q=-t+O(t^3)\)，
\(g_{f_m}=t^{-h}+\cdots\)，可逐项核定
\[
\boxed{\quad
\operatorname{Fr}_2^-(f_m)
=-p^3\bigl(1-q(m-4)\bigr)t^{-h}
       +\text{较低极点阶的项}.
\quad}
\tag{8}
\]
确实 \(gB\) 的首项是 \(-t^{-h+1}\)，
所以 \(gA-(gB)'\) 的首系数为 \(1-(h-1)=2-h\)。
该首系数 \(1-q(m-4)\) 是 \(p\) 单位。

而 \(f_{mq}\) 的最高极点阶是 \(mq-3\)；
二者的极点阶相差
\[
(mq-3)-\bigl(q(m-4)+1\bigr)=4q-4.
\tag{9}
\]
这是实际 \(M_e\) 的四阶零点在 \(t\mapsto t^q\) 下变成
四 \(q\) 阶零点所造成的具体差别。
并非一个共同单位规范可以删去的误差。

定义实际主部差
\[
\mathcal E_m=f_{mq}-\operatorname{Fr}_2^-(f_m).
\tag{10}
\]
由 (5)、(7) 可以直接有限计算它的每个负次系数；
它不是只由右侧留数反向定义的对象。
其最高极点项仍为 \(t^{-mq+3}\)，且 (6) 给
\[
\boxed{\quad
\operatorname{Res}_0(\mathcal E_m\omega\,dt)
       =(C_{mq}+p^3C_m,0).
\quad}
\tag{11}
\]
应用 R94 的特征零 PF 消元，准确有某个负奇 Laurent 多项式
\(\widetilde R_m\) 使
\[
\mathcal E_m=\mathscr D\widetilde R_m
                 +(C_{mq}+p^3C_m)/t.
\tag{12}
\]
这里没有声称 \(\widetilde R_m\) 整；
R94 的高极点分母及实际输入格成本仍必须保留。

## 4. 完整深度的正确归一化

令
\[
m_n=(p+1)p^n,\qquad \tau_n=p^{p^n},\qquad
S_{p,n}=\tau_n C_{m_n}.
\tag{13}
\]
R77 及[完整惰性 jet](2026-11-12-iterated-gm-frobenius-and-complete-inert-jets.md)
使用的正是 \(S_{p,n}\)；准确有
\[
v_p(S_{p,n})=2v_p(J_{A,p}(p^n)).
\tag{14}
\]
完整中心导数为零时，相应全层深度条件为
\(v_p(S_{p,n})\ge4n+4\)，对所有 \(n\) 成立。

若比较**已经归一化**的实际类，则应取
\[
\mathcal E^{\rm norm}_n
   =\tau_{n+2}f_{m_{n+2}}
      -\operatorname{Fr}_2^-(\tau_nf_{m_n}).
\]
其准确留数是
\[
\boxed{\quad
\operatorname{Res}_0
  (\mathcal E^{\rm norm}_n\omega\,dt)
=(S_{p,n+2}+p^3S_{p,n},0).
\quad}
\tag{15}
\]
如果先对未归一化的 (10) 统一乘 \(\tau_{n+2}\)，
第二项则变成
\[
S_{p,n+2}
 +p^{\,3+(p^2-1)p^n}S_{p,n}.
\tag{16}
\]
(15)、(16) 是不同的比较，不能将巨大的相对尺度漏掉。

### 4.1 一个对实际对象成立的全层校准

若 \(\Gamma_{i,p}=C_{p+1}/p\) 是单位，则 R54 的准确一阶式给
\[
J_{A,p}'(0)\in p\mathbb Z_p^\times,\qquad
J_{A,p}(u)-J_{A,p}'(0)u\in p^2u^2\mathbb Z_p\langle u\rangle .
\tag{17}
\]
因此对所有 \(n\ge0\)，一次项和余项赋值不同，准确有
\[
v_p(J_{A,p}(p^n))=n+1,\qquad
\boxed{v_p(S_{p,n})=2n+2.}
\tag{18}
\]
这不是对大 \(n\) 的渐近估计。
由 (15)，两项的赋值分别为 \(2n+6\) 与 \(2n+5\)，故
\[
\boxed{\quad
v_p(S_{p,n+2}+p^3S_{p,n})=2n+5.
\quad}
\tag{19}
\]
例如原实际截面在 \(p=7\) 的精确数值为
\[
C_8=\frac{65863}{1252815},\qquad C_8/7\equiv2\pmod7,
\]
由 R94 的独立整数流脚本认证。
于是 (18)、(19) 对这个真实素数的**全部** \(n\) 成立。

这排除了在本篇规范下
“\(S_{p,n+2}\mathfrak c_0\) 是
\(\Phi^2(S_{p,n}\mathfrak c_0)\) 的单位倍数”的朴素递推：
两边赋值准确相差一。
因此不能用固定留数 Frobenius 的斜率 \(3/2\)，
直接反证完整中心导数为零；实际非齐次项 (15) 必须先处理。
本结论没有排除含不同参考连接、其他真实张量类或高阶扩张的比较。

## 5. 原 theta 的 carry 给的是同一权，而非 (15) 的跨权递推

[原 theta 平方 Frobenius](2026-11-12-original-theta-square-frobenius-and-witt-trace.md)
与[完整一步同源](2026-11-12-geometric-p-step-theta-and-ramified-witt-carry.md)
使用的是原固定椭圆曲线上的真实 \([-p]\)，在加法参数中为
\((z,w)\mapsto(-pz,-pw)\)。
它与本篇模参数的 \(t\mapsto t^{p^2}\) 是不同空间上的箭头。

把公共 \(w/Z(w)\) 因子补回后，
[实际 carry 中央源](2026-11-12-theta-carry-central-residue-source.md)
定义 \(W_P=w\Theta_P=1+X_P\)，并给出明确的正式 correction
\[
E_{a,P}
=\frac{a w^{1-q}}{\Psi_a(w)}
  \frac{\Psi_a(P+z+w)}{\Psi_a(P+z)},\qquad a=-p.
\]
这里 \(w\) 是加法参数；只有此前整参数中的 \(D_{a,P}\)
被证明为曲面上的有理函数，不能因此称这个 \(E_{a,P}\)
为全局有理函数或全整单位。
对应的完整非线性项为
\[
\mathcal N_P
=(E_{a,P}-1)(1+qX_P)
 +E_{a,P}\sum_{k=2}^q\binom qk X_P^k .
\tag{20}
\]
令 \(\Pi_m=[z^mw^{m+1}]\)，并取原来已经核定的
\(\kappa_m d_m=C_m\)。该笔记准确证明
\[
\boxed{\quad
\kappa_m\Pi_m\sum_{P\in\mathcal S}\mathcal N_P
=\bigl((-p)^{2m+1}-p^2\bigr)C_m
=-p^2(1+p^{2m-1})C_m.
\quad}
\tag{21}
\]
左侧保留公共参考、所有 \(256\) 标签及 Bell/Witt 交叉项。
其总次数 \(2m+1\) 的计算只用 correction 到该次数，
以及各 \(X_P\) 的严格较低总次数混合 jet。
这里没有把它误写成一个已知为零的 exact 源。

投到 R94 的固定留数线后，(21) 仍是
\[
-p^2(1+p^{2m-1})C_m\,\mathfrak c_0 .
\tag{22}
\]
它把原未知中央量以一个明确非零标量完整保留了下来。
例如 \(m=4\) 时 \(C_4=1\)，所以该源的留数已非零。
然而 (21) 保持 \(m\)，没有产生 \(C_{mp^2}\) 与 \(C_m\)
之间的闭合关系。

若把 (21) 的全部中央对角 Borel 化，其实际生成式为
\[
-p^2\mathcal B_1(u)-p\mathcal B_1(p^2u).
\tag{23}
\]
这里出现的是 \(u\mapsto p^2u\)，原点分歧次数为一；
本篇的基底 Frobenius 在水平坐标中则是
\(u\mapsto u(t(u)^{p^2})\)，原点分歧次数为 \(p^2\)。
二者不能经可逆局部参数变换直接识别。
完整系数比较仍须通过真正的 heat/Gauss–Manin 交换式，
包括 (20) 的参考与非齐次项，而不能只把两个公式都称为
“Frobenius”便相互替换。

## 6. 当前留下的具体问题

已经构造并核定的是 (5)、(10)、(15)、(20) 的真实对象及其留数。
新的非零输入若要从这里产生，必须约束
\[
S_{p,n+2}+p^3S_{p,n}
\]
这个实际跨权差，或者构造另一个真实、保留原公共参考的
上同调对象，其 Frobenius 箭头确实与完整中央规范相容。

仅因 \(S_{p,n}\) 是半因子值的平方，不能把 R94 的
\(H^1(E)(-1)\) 自行换成 \(H^1(E)\otimes H^1(E)(-1)\)。
后者的二步斜率在数值上与 (18) 相容，但本篇没有构造其
实际中央类。必须保留原 Poincaré/theta 参考，才能判断这种
张量比较是否存在；不能从斜率相等计入一个新结果。
