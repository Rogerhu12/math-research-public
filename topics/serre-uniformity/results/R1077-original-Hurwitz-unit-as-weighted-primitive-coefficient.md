# R1077：新 Hurwitz 单位在同一原 primitive 上的加权高系数

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient / o1_theta / root。

**已证明以下同源单位身份。** 本文把 R1075 的新单位准确搬到 R1076 的同一个原多项式，而不更换椭圆曲线、微分或原函数。它没有证明原短两个障碍不能同时为零。

## 1. 原模型和准确结论

保持 [R1061](R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md) 与 [R1076](R1076-original-primitive-cubic-and-sixth-power-obstructions.md) 的规范：
$$
p=6k-1\ge41,\quad E:V^2=U^3+v^2,\quad
v=-6s,\quad v^2=-108,\quad v^p=-v,\quad
\omega=\frac{dU}{2V},\quad \mathscr D=d/\omega,
$$
$$
z=\frac{1-V/v}{2},\qquad
\mathscr D\Psi=\delta\in\mathbf F_p^\times,\qquad
\mathscr T(z)=z(1-z)\mathscr H(z)^3=-\frac{2v}{\delta^3}\Psi^3.
$$
$\mathscr H$ 是 R1076 的明确有限多项式；最高的 $z^p$ 盲项也保其原值。
取唯一的 $C\in\mathbf F_p^\times$ 满足 $C^3=4v^2$。
唯一性用 $p\equiv2\bmod3$，不是任意丢弃立方相位。

令
$$
\mathcal E_k=[z^{2k}](1-z)^{-1/3}\mathscr T(z)^2.
\tag{1077.1}
$$
此处只读取次数 $2k<p$，全部二项式分母均可逆。
则准确有
$$
\boxed{\quad
G_{p-5}=\frac{C}{24v^2}\mathcal E_k,\qquad
\mathcal E_k=\frac{576v^4}{7C\delta^5}\in\mathbf F_p^\times.
\quad}
\tag{1077.2}
$$
$G_{p-5}$ 是同一 $\omega$ 的原 Hurwitz 系数
$$
U(t)=t^{-2}+\sum_{d\ge4,\ d\ {\rm even}}(d-1)G_d\,t^{d-2},
\qquad dt=\omega.
$$
此外 $2k=1/3$ 在 $\mathbf F_p$ 中，故同一有限读数也可写成
$$
\mathcal E_k=[z^{2k}](1-z)^{-2k}\mathscr T(z)^2.
\tag{1077.3}
$$

## 2. 原 O 处参数与微分

在原无穷点 $O$ 取形式参数 $w=z^{-1/3}$，并选其分支使
$$
V=v(1-2w^{-3}),\qquad
U=Cw^{-2}(1-w^3)^{1/3}.
$$
由 $U^3=-4v^2z(1-z)$ 可直接核这两个式子。
其单位三次根取首项一，故所有当前所需系数唯一。

直接对 $U$ 微分，得到
$$
\omega=c(1-w^3)^{-2/3}\,dw,\qquad
c=\frac{C}{2v}=\frac{2v}{C^2},\qquad
Cc^2=1,\qquad c^3=\frac1{2v},\qquad c^p=-c.
\tag{1077.4}
$$
特别原 additive 参数为
$$
t=cwA(w^3),\qquad
A(Z)=\sum_{j\ge0}\frac{(2/3)_j}{j!(3j+1)}Z^j
={}_2F_1(1/3,2/3;4/3;Z).
\tag{1077.5}
$$
本文实际只需要 $j\le2k-2$。
在此范围 $3j+1\le p-4$，分母全部为 $p$-单位；
没有越过共振后对特征零无限级数强行约化。
$Cc^2=1$ 保证 $U(t)$ 的首项准确为 $t^{-2}$，
所以此 $t$ 与原 Hurwitz 规范完全相同。

## 3. 同一个 residue 及完整系数转换

用原 Laurent coefficient 的 residue 读取，
$$
(p-6)G_{p-5}
=\operatorname{Res}_{O}U\,t^{-p+6}\omega.
$$
代入 (1077.4)–(1077.5) 后，$w$ 的显式次数是 $4-p$，故
$$
(p-6)G_{p-5}
=Cc^{\,7-p}
 [Z^{2k-2}](1-Z)^{-1/3}A(Z)^{6-p}.
\tag{1077.6}
$$
这里 $p-5=3(2k-2)$，没有遗漏 residue 的一次偏移。
由 $c^p=-c$，准确有
$$
Cc^{7-p}=-Cc^6=-\frac{C}{4v^2}.
\tag{1077.7}
$$

因所读次数 $2k-2<p$，在全部已经支付整性的前缀内
$A(Z)^{-p}\equiv1\bmod (p,Z^{2k-1})$。
Euler 的同一有限变换为
$$
A(Z)=(1-Z)^{1/3}\mathscr H(Z)
       \pmod{Z^{2k-1}}.
$$
它也可直接由两边的系数递推在这个安全范围验证。
于是
$$
\begin{aligned}
[Z^{2k-2}](1-Z)^{-1/3}A^{6-p}
&=[Z^{2k-2}](1-Z)^{5/3}\mathscr H^6\\
&=[Z^{2k}](1-Z)^{-1/3}\mathscr T^2\\
&=\mathcal E_k.
\end{aligned}
\tag{1077.8}
$$
将 $p-6=-6$ 与 (1077.7) 代入 (1077.6)，得到
$G_{p-5}=C\mathcal E_k/(24v^2)$。

R1061 §21.3 已在此同一模型和同一相对 Cartier 标架证明
$$
C_{\rm rel}(U\omega)/\omega'=-\delta.
$$
故 [R1075](R1075-original-Hurwitz-unit-and-first-cuspidal-slope.md) 的原闭式在这里准确给
$$
G_{p-5}=-\frac{24v^2}{7(-\delta)^5}
       =\frac{24v^2}{7\delta^5}.
$$
这支付 (1077.2) 的全部常数和非零性。
所有外因子在 $p\ge41$ 都是单位，没有未知 period 比。

另一种保留幂式的等价写法是
$$
\mathcal E_k=-6(2v)^{-2k+2}G_{p-5}.
$$
因为 $(2v)^{2k}=-C$，它与 (1077.2) 完全相同：
两边都在 $\mathbf F_p$，其立方由 $6k=p+1$ 给 $-4v^2$，再用立方映射双射。
这也保留两个独立 residue 推导中的原分支。

## 4. 与真正短障碍的关系及剩余问题

R1076 已证明原短障碍准确为
$$
\eta_k=k[z^k]\mathscr T,\qquad
\nu_k=\frac{k}{40}[z^k]\mathscr T^2,
$$
以及
$$
e=K_4=0\ \Longleftrightarrow\
[z^k]\mathscr T=[z^k]\mathscr T^2=0.
$$
本文证明单位的是同一 $\mathscr T^2$ 的**加权 $2k$ 次**系数。
它与上述未加权 $k$ 次系数不同。
现在有真实的原来源桥，但尚无已证明的
$$
\eta_k=\nu_k=0\ \Longrightarrow\ \mathcal E_k=0.
$$
因此本文没有用高加权单位代替指定短系数，
也没有据此关闭原 $f_N/e$、$K_4$ 或全局 Serre 问题。
下一步继续同一原三挠平移及短配对的准确恒等式。

本篇均为纸面证明。o2 给出实际 $O$ 参数和 residue 桥；
o1 独立给 $C/(24v^2)$ 归一；root 独核两种常数的相等、全部指数和安全前缀。
无数学程序执行或旧窗口重算。
