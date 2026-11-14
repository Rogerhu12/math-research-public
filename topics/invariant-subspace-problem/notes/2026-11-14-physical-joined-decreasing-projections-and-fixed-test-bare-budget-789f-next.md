# 原物理 left+bare 的递减闭空间、同测试 Riesz 源与全切口 bare 预算

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明的中间结论。** 本稿把原 joined left+bare 核放入同一个物理 Hilbert 空间中的递减闭空间族。对固定物理测试的真正 joined Riesz 源，得到
\[
\sum_{q\ge s}\alpha_q(u_q^{\rm b})^2
\le d(2+\log d)^2\|f\|^2.
\]
这不经过 bosonic 硬核修复，不含原 Jordan 相似条件数，也不使用增长孔层的 MP 统一界。
与真实完整核投影作差后，两费也有全切口预算。
该差的主左能量仍可能大；本文不宣称原 \(N=M\)。

依赖：
[完整首头商及原 \(L+B\)](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)；
[原同源 full／bare 与高返回](2026-11-14-one-bit-complete-right-bare-source-and-actual-return-schur-789f-next.md)。
固定层 MP 和原源的闭满射仅用于引用的原费用定义；以下闭空间及投影流证明不把全孔 \(D^\dagger\) 视为有界。

**后续加强：** [物理投影夹逼](2026-11-14-physical-joined-sandwich-and-same-increment-three-fee-fixed-test-budget-789f-next.md)已支付本文此前留下的 \(\mu(t-u^{\rm b})\)，并把全部预算锐化为原同一投影增量，去掉 Fourier 对数及头常数；本文较弱不等式仍正确。主左角度配对仍未闭合。

## 1. 在整个原物理空间定义高旗

固定原 \(m\ge5,d=2^m,A=A_m,D=D_m\)，并置
\[
\mathcal H=\mathbb C^d\otimes\bigoplus_{p\ge0}\mathcal H_p,\qquad
C=A+D,\qquad \mathcal K=\ker C.
\]
由于 \(b\in\ell^1\)，\(D\) 及 \(C\) 在这个全孔 Hilbert 空间上有界。
保留实际规范
\[
A=VJ_dV^{-1},\qquad V=1\oplus V_+.
\]

记 \(E_h^{(p)}=\ker D^h\cap\mathcal H_p\)、\(E_0^{(p)}=0\)。
对每个整数切口 \(q\ge0\)，定义全孔高旗
\[
\boxed{
\mathcal H_{{\rm hi},q}
=\mathbb C^d\otimes
 \bigoplus_{p\ge q+2} E_{p-q-1}^{(p)}.
}
\tag{1.1}
\]
各孔层正交，故它闭；并且
\[
\mathcal H_{{\rm hi},q+1}\subseteq
\mathcal H_{{\rm hi},q}.
\]
此处先张量全部物理头，未把原右输入旗扩大为一个额外的可行核。
原头旗将在真正商核中自动恢复。

\(D E_h\subseteq E_{h-1}\)，所以高旗在 \(D,A,C\) 下不变。
记 \(Q_q=P_{\mathcal H_{{\rm hi},q}^{\perp}}\)，
\(\delta_q=Q_qD|_{\mathcal H_{{\rm hi},q}^{\perp}}\)；
尾算子默认与头单位张量。商的不变性给
\[
\delta_q^j=Q_qD^j|_{\mathcal H_{{\rm hi},q}^{\perp}}.
\tag{1.2}
\]
在这个全孔商中，\(\delta_q\) 本身不必幂零；
下文只使用其真正的 \(\ker\delta_q^d\)。

## 2. 闭和、完整提升及有限孔支撑

定义
\[
\boxed{\mathcal M_q=\mathcal K+\mathcal H_{{\rm hi},q}.}
\tag{2.1}
\]
这里的加号先表示代数和。以下证明它已经闭，不能只因两个加数闭而宣告。

商核 \(A+\delta_q\) 的首头公式准确为
\[
T_qf=\sum_{j=0}^{d-1}(Ve_j)(-\delta_q)^jf,
\qquad f\in\ker\delta_q^d.
\tag{2.2}
\]
反向由 \(V^{-1}\) 的逐头方程得到全部商核，且首头为唯一参数。

按孔层计算 \(\ker\delta_q^d\)。
若 \(p\le q+d\)，其商最小代表 \(f_p\) 满足
\(D^df_p=0\)，因为输出层 \(p-d\le q\) 没有高旗。
若 \(p>q+d\)，令 \(h=p-q-1\ge d\)。
由 (1.2)，
\[
\delta_q^df_p=0
\ \Longrightarrow\
D^df_p\in E_{h-d}^{(p-d)}
\ \Longrightarrow\ D^hf_p=0.
\]
但最小代表 \(f_p\perp E_h^{(p)}\)，所以 \(f_p=0\)。
这也涵盖 \(h=d\) 时的 \(E_0=0\)。

因此
\[
\boxed{
\ker\delta_q^d=
\bigoplus_{p\le q}E_d^{(p)}
\ \oplus\
\bigoplus_{j=1}^{d}
\left(E_d^{(q+j)}\ominus E_{j-1}^{(q+j)}\right).
}
\tag{2.3}
\]
每个这样的 \(f\) 本身属于完整 \(\ker D^d\)，所以
\[
v=\sum_{j<d}(Ve_j)(-D)^jf\in\mathcal K,\qquad
Q_qv=T_qf.
\tag{2.4}
\]
这证明完整核到商核的满射，不需要一个受限逆的条件数。

对任意物理 \(u\)，由高旗不变性，
\(Q_qCu=0\) 当且仅当 \(Q_qu\) 属于上述商核。
再用 (2.4)，得到
\[
\boxed{
\mathcal M_q=\ker(Q_qC).
}
\tag{2.5}
\]
右端是有界算子的核，故 (2.1) 的代数和闭。
它们构成同一个原物理 Hilbert 空间中的递减闭族。

商核 (2.2) 的物理最小代表只支持到孔层 \(q+d\)；
第 \(j\) 个未来层的非零头满足 \(i\le d-j\)，
第 \(i\) 头仍在 \(E_{d-i}\)。
因此它准确是引用稿的原 joined left+bare 核，全部头旗、短核旗、内部零输出和两端封口都保留。

## 3. 固定测试的真实 joined 投影与源

固定 \(f\in\mathcal H_{\le s}\)，对 \(q\ge s\) 置
\[
z_q=P_{\mathcal M_q}f.
\tag{3.1}
\]
因为 \(f\perp\mathcal H_{{\rm hi},q}\) 且后者包含于 \(\mathcal M_q\)，
\[
z_q\perp\mathcal H_{{\rm hi},q}.
\]
所以 \(z_q\) 就在 (2.2) 的物理最小代表商核中，特别
\[
\boxed{\operatorname{supp}z_q\subseteq[0,q+d].}
\tag{3.2}
\]

保留原左测试和有限核投影
\[
q_q=P_{V_q}f,\qquad t_q=E_qq_q,\qquad
k_q=P_{\mathcal K_q}f,\quad
\mathcal K_q=\mathcal K\cap\mathcal H_{\le q}.
\]
仍以 \(L_q,B_q,G_q\) 表示同一个实际源空间的原三形式，
\(\mathcal A_q\) 表示源到 bare 最小链的映射。
则存在唯一源 \(u_q^{\rm b}\)，使
\[
\boxed{
z_q=(\,k_q+E_q^\dagger u_q^{\rm b},\
          -\mathcal A_q u_q^{\rm b}\,),
\qquad
u_q^{\rm b}=(L_q+B_q)^{-1}L_qt_q .
}
\tag{3.3}
\]
证明是完整 joined 核中对同一个固定功能
\(\langle f,v\rangle\) 作 Riesz 表示：
左零源部分独立给 \(k_q\)，其余源的准确度量是 \(L_q+B_q\)。
这不是把 \(t_q\) 直接当成 joined 最优源。

特别
\[
\boxed{
\|P_{>q}z_q\|^2=\alpha_q(u_q^{\rm b})^2.
}
\tag{3.4}
\]

## 4. 全切口 bare 能量：只用原物理正交增量

递减投影的差
\[
\Pi_j=P_{\mathcal M_{j-1}}-P_{\mathcal M_j}
\]
为两两正交投影。
对当前固定测试令
\[
a_j=\Pi_jf=z_{j-1}-z_j,\qquad j\ge s+1.
\]
由 (3.2)，
\[
\operatorname{supp}a_j\subseteq[0,j+d],\qquad
\sum_{j\ge s+1}\|a_j\|^2\le\|f\|^2.
\tag{4.1}
\]
于是
\[
P_{>q}z_q=P_{>q}z_s-
 \sum_{\substack{s<j\le q\\0\le q-j<d}}P_{>q}a_j.
\tag{4.2}
\]

下面明确保留这组随切口变化的向量，不能对每个 \(z_q\) 独立估计后相加。
物理滑动带分析算子
\[
W_d:v\longmapsto
   (P_{(q,q+d]}v)_{q\ge s}
\]
满足 \(\|W_d\|\le\sqrt d\)，因为每个物理孔层恰至多被计数 \(d\) 次。
限制输入到两两正交的
\(\bigoplus_j\operatorname{span}\{a_j\}\)，仍有同一范数。

区间 Schur 乘子 \(0\le q-j<d\) 的算子范数至多
\[
\frac1{2\pi}\int_{-\pi}^{\pi}
 \left|\sum_{\ell=0}^{d-1}e^{i\ell t}\right|dt
\le1+\log d.
\tag{4.3}
\]
这是对输入第 \(j\) 块和输出第 \(q\) 行分别施加相位酉后的 Fourier 平均；
只用 \(|D_d(t)|\le\min(d,\pi/|t|)\) 即得显示常数。

当 \(q\ge j\) 时，由 \(a_j\) 的支撑上界，
\(P_{>q}a_j=P_{(q,q+d]}a_j\)；
而 \(q-j\ge d\) 时该项为零。
所以 (4.2) 的第二项准确是这个区间乘子作用于 \(W_d\)，
其输出直和范数至多
\(\sqrt d(1+\log d)\|f\|\)。

第一项由 \(z_s\) 支撑至多 \(s+d\)，有
\[
\sum_{q\ge s}\|P_{>q}z_s\|^2
\le d\|z_s\|^2\le d\|f\|^2.
\]
在输出 Hilbert 直和中作一次三角不等式，得到
\[
\boxed{
\sum_{q\ge s}\alpha_q(u_q^{\rm b})^2
\le d(2+\log d)^2\|f\|^2.
}
\tag{4.4}
\]
这条全切口估计不使用 \(\|V\|\|V^{-1}\|\)，也不假设商最小代表保持某个 bosonic 占据上界。

## 5. 与真实完整核投影作差：同一个源的两费

令 \(u_q^{\rm f}\) 为 \(k_{q+d}=P_{\mathcal K_{q+d}}f\)
在切口 \(q\) 的实际源。零源和右核最小性给
\[
k_{q+d}=
(\,k_q+E_q^\dagger u_q^{\rm f},\
       -\mathcal C_q^{\min}u_q^{\rm f}\,),
\]
\[
\boxed{
u_q^{\rm f}=(L_q+G_q^{-1})^{-1}L_qt_q .
}
\tag{5.1}
\]
其中 \(\mathcal C_q^{\min}\) 是原普通完整右最小链。

\(\mathcal K_q\) 递增，所以
\[
\|k_{q+d}-k_q\|^2
=\mu_q(u_q^{\rm f})^2+\lambda_q(u_q^{\rm f})^2.
\]
将两两正交的单步核增量计数，每个至多出现 \(d\) 次，得到
\[
\boxed{
\sum_{q\ge s}
\{\mu_q(u_q^{\rm f})^2+\lambda_q(u_q^{\rm f})^2\}
\le d\|f\|^2.
}
\tag{5.2}
\]
在步长 \(d\) 的不交网格上，右边可换成 \(\|f\|^2\)。

定义实际差源
\[
e_q^{\rm bf}=u_q^{\rm b}-u_q^{\rm f}.
\tag{5.3}
\]
两条真实源正规方程给
\[
L_qe_q^{\rm bf}
=G_q^{-1}u_q^{\rm f}-B_qu_q^{\rm b}.
\]
完整投影关系 \(P_{\rm f}F_{\rm b}^*=F_{\rm f}^*\)
因此准确给
\[
\boxed{
F_{\rm f}^*L_qe_q^{\rm bf}
=\mathcal C_q^{\min}u_q^{\rm f}
 -P_{\rm f}\mathcal A_qu_q^{\rm b}.
}
\tag{5.4}
\]
这已是原 flat 链，不将普通右费替换成 flat。

同时
\[
\alpha_q(e_q^{\rm bf})
\le\alpha_q(u_q^{\rm b})+\lambda_q(u_q^{\rm f}).
\]
结合 (4.4)、(5.2)、(5.4)，
\[
\boxed{
\sum_{q\ge s}\Xi_q(e_q^{\rm bf})^2
\le4d\{(2+\log d)^2+1\}\|f\|^2.
}
\tag{5.5}
\]
两个费用确实属于同一个原差源 \(e_q^{\rm bf}\)。

对任意同切口原源 \(r\)，另有准确测试误差
\[
\langle L_qr,t_q-e_q^{\rm bf}\rangle
=\langle B_qr,u_q^{\rm b}\rangle
 +\langle L_qr,u_q^{\rm f}\rangle,
\]
从而
\[
\boxed{
|\langle L_qr,t_q-e_q^{\rm bf}\rangle|
\le
\Xi_q(r)
\{\alpha_q(u_q^{\rm b})^2+\lambda_q(u_q^{\rm f})^2\}^{1/2}.
}
\tag{5.6}
\]
这用原 bare 配对和原 flat／ordinary 配对。
它不需要一个尚未证明的 \(\mu_q(t_q-u_q^{\rm b})\) 上界。

(5.5)--(5.6) 可对固定有限个测试共同求和，
并与原 \(\Xi_q(r)\) 窗口预算同时选点。
它构造的是保原泛函的一个真实小两费差源，
不是给左费用一个两费上界。

## 6. 仍可存活的左角度与固定参数极限

因为 \(\mathcal K_{q+d}\subseteq\mathcal M_q\)，
\[
\mathcal G_q=
P_{\mathcal M_q}-P_{\mathcal K_{q+d}}
\]
是正交投影，且随 \(q\) 递减。
其在固定测试上的向量为
\[
\mathcal G_qf=z_q-k_{q+d},
\]
左部分正是 \(E_q^\dagger e_q^{\rm bf}\)，
未来部分为
\(-\mathcal A_qu_q^{\rm b}
 +\mathcal C_q^{\min}u_q^{\rm f}\)。
因此 (5.5) 仍未给
\[
\mu_q(e_q^{\rm bf})^2
=\|P_{\le q}\mathcal G_qf\|^2
\]
一个随原 \(m,q\) 联合增长而趋零的上界。

固定 \(m\) 时确有 \(\mathcal G_q\to0\) 强收敛。
一方面 \(\cap_q\mathcal M_q=\mathcal K\)，由 (2.5)
和 \(\cap_q\mathcal H_{{\rm hi},q}=0\) 直接得到。
另一方面完整核的首头表示
\[
v=\sum_{j<d}(Ve_j)(-D)^jf,\qquad f\in\ker D^d
\]
允许按首头孔层截断 \(f\)，从而
\(\overline{\cup_q\mathcal K_q}=\mathcal K\)。
这里固定 \(m\) 的首头映射有界已足够。

但该强收敛没有给原 \(m\to\infty\)、
\(q\le\exp(d^3/4)\) 窗口的统一速率。
尤其不能从 (5.5) 的两费小推出主左配对小。
本稿保留这一个真实角度缺口，不把递减投影终点当作
原 \(N=M\) 的完成证明。
