# R639 — 原完整中央规范与整个形式群内盘的同一 Stokes 缺陷

日期：2026-11-15。**状态：已证明。**

本篇在原 sigma 上一次支付全部非中央规范因子，并将 R622 的同一
中央连接推进到每个严格小于 \(R_E=p^{-1/(p^2-1)}\) 的原 \(z\) 盘。
所需原点值仍是原完整 Newton 导数 \(j_m\)，没有新增第二个中央零。

核心输入是原 CM 乘法公式的整性。对范数一的
\(\zeta\in\mu_{p+1}\)，原比值 \(h(\zeta z)/h(z)\) 在 \(u=x^{-1/2}\)
中是常数一的整级数。它由原 prime-to-\(p\) CM 除法多项式极限得到，
而不是用形式指数的逐项小分母去猜整性。
由此得到完整规范、真实中央连接的严格常数主导，以及整个内盘上
同一个 \(j_m\) 的解析逆。

## 1. 原对象、准确中央投影和声明

固定同一个原 \(b=17\) 模型与惯性素数
\[
p=6s-1>71,\quad d=p+1=6s,\quad w=z^6,\quad X=z^d=w^s,
\quad L=(p^2-1)/6.
\]
保持 \(dx/(2y)=dz\)、\(\sigma=z+O(z^7)\)、
\((\log\sigma)''=-x\)，并记
\[
h=\sigma/z,\quad F=\log h=\sum_{n\ge1}F_nw^n,\quad c=F_s,
\quad v_p(c)=-1.
\]
原零初值 Euler 函数、两算术来源和投影始终为
\[
\mathscr U_m(z)=\int_0^z A_m(t)\frac{dt}{t},\qquad
A_{34}=S,\quad A_{72}=T,
\]
\[
\Pi_0 f=\frac1d\sum_{\zeta^d=1}f(\zeta z).
\]
定义**完整正式中央因子**
\[
F_{\rm c}(X)=\Pi_0 F(z)=\sum_{h\ge1}F_{hs}X^h,\qquad
E_{\rm c}(X)=\exp F_{\rm c}(X),\qquad q_{\rm c}=F_{\rm c}'.
\tag{1}
\]
\(E_{\rm c}\) 在这里先是常数一形式级数；本篇不假定它在大盘 Tate。

令
\[
S_z=p^{-p/(p^2-1)},\qquad
R_E=p^{-1/(p^2-1)},\qquad r_E=R_E^d=p^{-1/(p-1)}.
\]
本篇将证明：

1. \(h/E_{\rm c}\) 及其逆在每个闭 \(z\) 盘 \(R<R_E\) 都是
   范数一 Tate 单位，而且在原 \(u\) 参数中有整系数。
2. 若 \(p^{-1}<r=R^d<r_E\)，则
   \[
   q_{\rm c}\in\mathcal T_r,\qquad
   \|q_{\rm c}/c-1\|_r<1.
   \tag{2}
   \]
3. 对同一完整
   \[
   G_{m,{\rm c}}=E_{\rm c}^{-m}A_m,\qquad
   G_{m,{\rm c},0}=\Pi_0G_{m,{\rm c}},
   \]
   方程
   \[
   (\partial_X+m q_{\rm c})\mathcal R_{m,{\rm c}}
   =G_{m,{\rm c},0}/X
   \tag{3}
   \]
   在上述每个闭 \(r\) 盘有相容的唯一 Tate 解，且
   \[
   \mathcal R_{m,{\rm c}}(0)=j_m.
   \tag{4}
   \]
   因而原零初值解满足
   \[
   dE_{\rm c}^{-m}\Pi_0\mathscr U_m
   =\mathcal R_{m,{\rm c}}-j_m E_{\rm c}^{-m}.
   \tag{5}
   \]

全部环和范数可延到 \(\mathbf C_p\)。实际有限非分歧系数域记为
\(K_p=\mathbf Q_p(\omega)\)，\(\omega^2+\omega+1=0\)，整数环为
\(\mathcal O\)。\(p\) 惯性，所以其非平凡自同构在剩余域为
\(a\mapsto a^p\)，并且每个 \(\zeta\in\mu_{p+1}\) 的范数为一。

## 2. 原 prime-to-p CM 乘法式的整性

取非零 \(\alpha\in\mathbf Z[\omega]\)，
\(\alpha\equiv1\pmod2\)、\(p\nmid N\)，其中 \(N=\alpha\bar\alpha\)。
所以 \(N\) 为正奇数，原 CM 同态 \([\alpha]\) 的核阶为 \(N\)。

先支付原 sigma 规范的乘法式。原 \(j=0\) sigma 满足
\(\sigma(\omega z)=\omega\sigma(z)\)，故其准周期映射满足
\(\eta(\omega\lambda)=\bar\omega\,\eta(\lambda)\)。
在原周期格上线性延长给
\[
\eta(\alpha\lambda)=\bar\alpha\,\eta(\lambda).
\]
于是 \(\sigma(\alpha z)/\sigma(z)^N\) 的指数准周期完全相消。
\(\alpha\equiv1\pmod2\) 及 \(N\) 奇还支付同一个半特征号，
所以这个比值是真正原椭圆函数，不需额外二次 Gaussian。

其除子在非零核点有单零点，在原点有 \(N-1\) 阶极点。
核的非零点按 \(T,-T\) 成对（奇阶核无非零二挠点），
原首项固定其常数，准确得到
\[
\boxed{
\frac{\sigma(\alpha z)}{\sigma(z)^N}
=\alpha\prod_{T\in(\ker[\alpha]\setminus\{0\})/\{\pm1\}}
     (x(z)-x(T)).
}
\tag{6}
\]
\(N=1\) 时使用空积，同式仍成立。
这是原完整 CM 除法身份，后文不将 \(\alpha\) 改成任意形式参数。

因为 \(p\nmid N\) 且曲线在 \(p\) 处好约化，
每个非零核点都不会约化为原点。
确实若它落在原形式群，则 \([N]\) 的单位线性项使其在形式群上
可逆，不可能杀掉一个非零点。因此这些点的 \(x(T)\) 都整。
置原 \(u=x^{-1/2}=z+\cdots\)，有
\[
P_\alpha(u)=
\prod_{T\in(\ker[\alpha]\setminus\{0\})/\{\pm1\}}
       (1-x(T)u^2)\in1+u^2\mathcal O[u].
\tag{7}
\]
积分性可在包含全部核点的有限扩张上逐因子读出；
Galois 不变性再将系数降回 \(K_p\)。
没有随 \(\alpha\) 增长的 \(p\) 分母。

保持 R632 的原形式对数
\[
\tau=bu^6,\quad
C(\tau)=(1+\tau)^{-1/2},\quad
H(\tau)=\sum_{n\ge0}\frac{C_n}{6n+1}\tau^n,\quad
z=uH(\tau).
\]
由 (6) 严格得到
\[
\boxed{
h(\alpha z)=h(z)^N H(bu^6)^{N-1}P_\alpha(u).
}
\tag{8}
\]
这里的 \(H^{N-1}\) 必须保留；将 \(u\) 和 \(z\) 直接相认会使 (8) 错误。

## 3. 范数一 CM 极限给完整整单位

固定 \(\zeta\in\mu_d\subset\mathcal O^\times\)。
由中国剩余定理和 \(\mathbf Z[\omega]\) 在 \(\mathcal O\) 中的稠密性，
可取 \(\alpha_n\equiv1\pmod2\)、\(\alpha_n\to\zeta\)。
各 \(\alpha_n\) 在 \(p\) 处为单位，且
\[
N_n=\alpha_n\bar\alpha_n\longrightarrow
\zeta\bar\zeta=1.
\]
对任何固定的形式级数系数，(8) 右侧除 \(P_{\alpha_n}\) 外的各项
都对 \(\alpha_n,N_n\) 连续。
这只用整数幂的有限二项式系数，不假设 \(h\) 在目标大盘收敛。
因此 \(P_{\alpha_n}\) 逐系数收敛，给出
\[
\boxed{
P_\zeta(u)=
\frac{h(\zeta z(u))}{h(z(u))}
\in1+u^2\mathcal O[[u]].
}
\tag{9}
\]
左边是完整整多项式序列的系数极限，右边先按原正式身份理解。
整系数的统一界使该极限在每个严格单位内 \(u\) 闭盘一致收敛；
其与逆均为范数一单位。这里无须限制 \(N_n\) 的大小。

令
\[
T(u)=\left(\prod_{\zeta^d=1}P_\zeta(u)\right)^{1/d}.
\tag{10}
\]
因 \(d\) 为 \(p\) 单位，常数一的 \(1/d\) 次根可由整二项式级数定义，
故 \(T,T^{-1}\in1+u^2\mathcal O[[u]]\)。
对 (9) 作有限乘积并取正式 log，得到
\[
\log T(u(z))=\Pi_0F-F=F_{\rm c}-F,
\]
所以
\[
\boxed{
E_{\rm c}=h\,T(u(z)),\qquad h/E_{\rm c}=T(u(z))^{-1}.
}
\tag{11}
\]
这确定了完整规范，全部高阶中央项都在 (1) 中，没有截断。

R632 已付对每个闭 \(R<R_E\)，原 \(u(z)\) 是实际 Tate 逆，
\[
\|u\|_R=R,\qquad
\|u/z-1\|_R<1,\qquad \|H(bu^6)-1\|_R<1.
\tag{12}
\]
于是 (11) 的比值及其逆确为该原 \(z\) 盘上的范数一 Tate 单位，
并且
\[
\|T(u(z))-1\|_R\le R^2<1.
\tag{13}
\]
本篇没有把 \(E_{\rm c}\) 本身称为大盘 Tate 元。
\(\sigma/E_{\rm c}=z/T(u(z))=uH/T\)，其 \(H\) 仍在；
\(u\) 参数中直接整的是 \(h/E_{\rm c}\)。

## 4. 原 zeta 系数的全部进位界

要支付整个中央连接，不能只知道第一个 Gaussian。
记同一个原
\[
J(\tau)=\sum_{n\ge0}J_n\tau^n,\qquad
J_n=\frac{C_n}{1-6n},\qquad
\zeta_{\rm W}(z(u))=u^{-1}J(\tau),
\tag{14}
\]
其中 \(\zeta_{\rm W}=\sigma'/\sigma\) 是原 Weierstrass zeta，
不与有限群元素 \(\zeta\) 混同。
(14) 可由 \(\zeta_{\rm W}'=-x\)、\(dz=C\,du\) 及原首项直接积分。

若 \(a=v_p(6n-1)\)，条件 \(6n\equiv1\pmod{p^a}\) 确定其最低
\(a\) 个 \(p\) 进位，依次为
\[
s,\ 5s-1,\ s-1,\ 5s-1,\ s-1,\ldots .
\]
在 \(n+n\) 中，第一个 \(s\) 位不进位，随后每个 \(5s-1\) 位必进位，
其后的 \(s-1\) 位即使接入该进位仍不进位。
所以中央二项式至少有 \(\lfloor a/2\rfloor\) 个 \(p\) 因子。
保留 (14) 的整个分母后，
\[
\boxed{v_p(J_n)\ge-\lceil a/2\rceil.}
\tag{15}
\]
\(a=0\) 时同样成立。

令 \(R=p^{-\tau}\) 满足
\[
p^{-1/d}<R<R_E,\qquad
\frac1{p^2-1}<\tau<\frac1d.
\tag{16}
\]
在 \(u\) 半径 \(R\) 上，\(J_s b^s u^d\) 的权估值为
\[
-1+d\tau<0.
\tag{17}
\]
其余所有项严格大于它：

- \(a=0\) 的项整，权估值非负，常数项也为零赋值；
- \(a=1\) 时最早可能的指标是 \(s\)，其余指标 \(n>s\)
  满足 \(v_p(J_n)+6n\tau\ge-1+6n\tau>-1+d\tau\)；
- \(a\ge2\) 时，\(6n-1\ge p^a\)，由 (15)
  \[
  v_p(J_n)+6n\tau
  \ge-\lceil a/2\rceil+\frac{p^a+1}{p^2-1}>0.
  \tag{18}
  \]
  最后一式在 \(a=2\) 为 \(2/(p^2-1)>0\)，
  此后相邻差至少为 \(p^a/(p+1)-1>0\)。

(15) 的对数增长还保证整个高尾权估值趋于无穷。
因而这些严格不等式真给 Gauss 范数的统一严格差：
\[
\boxed{
\|J(bu^6)-J_s b^s u^d\|_R<pR^d,\qquad
v_p(J_s)=-1.
}
\tag{19}
\]
没有遗漏高阶 \(p\) 分母或高于 \(p^2\) 的指标。

## 5. 完整中央连接在全内盘的常数主导

原 \(h\) 的 log 导数在 \(u\) 坐标为
\[
q_\sigma(z(u))=\frac{h'}h(z(u))
=u^{-1}\left(J(bu^6)-H(bu^6)^{-1}\right).
\tag{20}
\]
两项常数相消，所以 (20) 在原点正则。
由 (12)，\(\|H^{-1}\|_R=1<pR^d\)。
将 (19) 除以 \(u\)，再用真实逆 (12)，
\(u^p-z^p\) 的范数严格小于 \(R^p\)，得到
\[
\boxed{
q_\sigma(z)=J_s b^s z^p+\mathcal E(z),\qquad
\|\mathcal E\|_R<pR^p.
}
\tag{21}
\]
实际代换 \(u\leftrightarrow z\) 在这里是同一闭盘的 Tate 同构，
并保持 Gauss 范数；没有把两个参数的形式可逆当作边界逆。

对 (11) 作正式 log 微分，右边各项已由前述估计确为 Tate，故
\[
d z^p q_{\rm c}(X)
=q_\sigma(z)+\frac{D_zT(u(z))}{T(u(z))}.
\tag{22}
\]
第二项的范数不超过 \(R^{-1}\|T(u(z))-1\|_R\)，
特别严格小于 \(R^{-1}<pR^p\)，最后一式正用 \(pR^d>1\)。
(21)–(22) 因此给
\[
\left\|q_{\rm c}-\frac{J_s b^s}{d}\right\|_r<p,
\qquad r=R^d.
\tag{23}
\]
(22) 左边的正式级数只含 \(z^{dh-1}\)；
由已证 Tate 性，除以 \(d z^p\) 并改读 \(X=z^d\) 是合法的
Tate 级数，而不引入负幂或遗漏角。

\(q_{\rm c}(0)=F_s=c\) 是原来同一个 \(c\)。
(23) 在常数项上也严格，故移去实际常数后仍有
\[
\boxed{
|c|=p,\qquad
q_{\rm c}\in\mathcal T_r,\qquad
\|q_{\rm c}-c\|_r<p,\qquad
\|q_{\rm c}/c-1\|_r<1
}
\tag{24}
\]
对全部 \(p^{-1}<r<r_E\) 成立。
这就是所需完整主导式；它同时处理所有更高中央项，
不只处理 \(cX+a_2X^p\)。

## 6. 原完整来源及唯一 Banach 逆

原 \(S,T\) 在 R632 的同一数据中写成
\[
A_m(z)=z^6 h(z)^m P_m(z),\qquad m=34,72,
\tag{25}
\]
其中 \(P_m=H(bu(z)^6)^{m-6}Q_m(bu(z)^6)\) 是完整原固定因子。
每个 \(Q_m\) 常数一且整，所以对任意 \(R<R_E\)，
\(P_m,P_m^{-1}\) 都是范数一 Tate 单位。
没有删去原椭圆多项式。

由 (11)，完整规范化来源确为
\[
G_{m,{\rm c}}(z)=z^6 T(u(z))^{-m}P_m(z)\in\mathcal T_R,\qquad
\|G_{m,{\rm c}}\|_R=R^6.
\tag{26}
\]
原 \(\Pi_0\) 的阶 \(d\) 为单位，故它不增加 Gauss 范数。
因此
\[
G_{m,{\rm c},0}(X)=\Pi_0G_{m,{\rm c}}
\in X\mathcal T_r,\qquad
\|G_{m,{\rm c},0}/X\|_r\le R^6/r.
\tag{27}
\]
它只是无常数项，不必是单位或非零首行。

对原
\[
H_{m,{\rm c}}=dE_{\rm c}^{-m}\Pi_0\mathscr U_m
\]
直接微分，并用 \(z\partial_z=dX\partial_X\)，得到
\[
H_{m,{\rm c}}'+m q_{\rm c}H_{m,{\rm c}}
=G_{m,{\rm c},0}/X,\qquad H_{m,{\rm c}}(0)=0.
\tag{28}
\]
\(d\) 因子和零初值在这里都没有改变。

令
\[
\mathcal B_{m,r}=(mc)^{-1}\partial_X+(q_{\rm c}-c)/c.
\]
因为 \(m\) 为 \(p\) 单位，由 (24)
\[
\boxed{
\|\mathcal B_{m,r}\|
\le\max\{p^{-1}r^{-1},\,\|q_{\rm c}/c-1\|_r\}<1 .
}
\tag{29}
\]
完整 Neumann 级数给
\[
\boxed{
\mathcal R_{m,{\rm c}}=
(mc)^{-1}\sum_{n\ge0}(-\mathcal B_{m,r})^n
       (G_{m,{\rm c},0}/X),
\qquad
\|\mathcal R_{m,{\rm c}}\|_r\le p^{-1}R^6/r .
}
\tag{30}
\]
这支付全部算子尾与唯一性。
任意两个允许半径上的解在共同内盘都唯一，所以它们相容；
于是得到整个 \(p^{-1}<r<r_E\) 的同一个解，
并可向更小盘限制。无需声称在所有小盘上算子也可逆。

## 7. 原点值准确等于原完整 j

这里必须比较实际原规范，不能把新方程的原点值重新命名为算术中央。

在 R618 的原范围内，令
\[
\mathcal U(z)=e^{F-cX},\qquad
R_2=p^{-(2p-1)/(p(p^2-1))},\qquad r_2=R_2^d.
\]
R618 已付 \(\mathcal U,\mathcal U^{-1}\) 在每个 \(R<R_2\) 为 Tate 单位，
且 \(p^{-1}<r_2<r_E\)。
由 (11)，
\[
D_{\rm c}(X):=E_{\rm c}/e^{cX}
=\mathcal U(z)\,T(u(z))
\tag{31}
\]
在这些盘也是常数一的 Tate 单位；其正式级数只含 \(X\)。
所以对任意 \(p^{-1}<r<r_2\)，
原第一连接与 (28) 由同一个真实单位 \(D_{\rm c}^m\) 互相变换。

具体地，R598/R618 的原第一层唯一 Tate 解
\[
\mathcal R_{m,1}' +mc\,\mathcal R_{m,1}
=G_{m,1,0}/X,\qquad
\mathcal R_{m,1}(0)=
\sum_{h\ge1}(-1)^{h-1}(h-1)!(mc)^{-h}g_{m,h}=j_m
\]
保全部原 Newton 尾。
因 \(G_{m,{\rm c},0}=D_{\rm c}^{-m}G_{m,1,0}\)，
准确有
\[
\mathcal R_{m,{\rm c}}=D_{\rm c}^{-m}\mathcal R_{m,1}
\quad(p^{-1}<r<r_2).
\tag{32}
\]
两边都在该盘 Tate，唯一性而非形式猜测保证等式。
\(D_{\rm c}(0)=1\)，故
\[
\boxed{\mathcal R_{m,{\rm c}}(0)=j_m.}
\tag{33}
\]
相容性将同一个值保到全部 \(r<r_E\)，没有引入新的参数。

(28) 的两形式解之差为常数乘 \(E_{\rm c}^{-m}\)。
原 \(H_{m,{\rm c}}(0)=0\) 遂确定唯一常数，得到
\[
\boxed{
H_{m,{\rm c}}=\mathcal R_{m,{\rm c}}-j_mE_{\rm c}^{-m},\qquad
d\Pi_0\mathscr U_m=E_{\rm c}^{m}\mathcal R_{m,{\rm c}}-j_m.
}
\tag{34}
\]
这些是原形式与小盘身份；右边的 Tate 因子由 §§3–6 在更大盘支付。
不宣称其中每个野指数在大盘单独解析。

## 8. 同一个中央零在整个形式群内盘的准确等价

由 (31)，\(E_{\rm c}^{-m}=e^{-mcX}D_{\rm c}^{-m}\)。
\(D_{\rm c}^{-m}\) 在大于 \(r_1=S_z^d=p^{-p/(p-1)}\) 的盘 Tate，
而 \(|mc|=p\)。
Legendre 数字和公式给 \(e^{-mcX}\) 准确半径 \(r_1\)，
在闭 \(r_1\) 非 Tate。因此 \(E_{\rm c}^{-m}\) 也有同一边界。

另一方面 \(\mathcal R_{m,{\rm c}}\) 在所有 \(r<r_E\) 解析。
由 (34) 严格得到
\[
\boxed{
j_m=0
\iff H_{m,{\rm c}}\in\mathcal T_{r_1}
\iff H_{m,{\rm c}}\text{ 在每个闭 }r<r_E\text{ 为 Tate 元}.
}
\tag{35}
\]
若 \(j_m\ne0\)，它的准确 \(X\) 半径仍为 \(r_1\)，闭边界非 Tate。
乘一个非零常数 \(j_m\)，无论其赋值多高，都不能使那条固定
非趋零系数子列变为 Tate 尾。

这完成原中央连接的整个 \(R<R_E\) 范围。
闭 \(R_E\) 不在 (35) 的结论中；R635 的原形式对数边界零点继续存在，
此处没有调用不存在的闭盘逆。

## 9. 整个首 Kummer 范围中的原中央域身份

R632 已付对 \(S_z\le R<R_E\)，
\[
F_R=\operatorname{Frac}(\mathbf C_p\langle z/R\rangle),\qquad
[F_R(h):F_R]=p.
\]
由 (11)、(30)、(34)，准确有
\[
\boxed{
d\Pi_0\mathscr U_m=
h^m\,T(u(z))^m\,\mathcal R_{m,{\rm c}}-j_m
\in F_R(h)\qquad(S_z\le R<R_E).
}
\tag{36}
\]
若某个 \(R\) 小于 (16) 的下限，只需从更大的允许盘限制
\(\mathcal R_{m,{\rm c}}\)，仍得到 (36)。

所以 R623 在较小外盘上的原对角域身份也扩展到了整个首 Kummer
范围。它对 \(j_m=0\) 与 \(j_m\ne0\) 同样成立，
**域成员身份本身仍不检测中央零**。
这不延伸 R623 两个独立 Gaussian 所生成的整个 \(p^2\) 域的呈示，
也不将两个中央投影当成两个新的独立局部积分变量。

## 10. 完整系数界与原临界两行

写
\[
G_{m,{\rm c},0}(X)=\sum_{k\ge1}g^{\rm c}_{m,k}X^k.
\]
由 (26)–(27) 对所有 \(R<R_E\) 的范数界，令半径趋向 \(R_E\)，
得到完整系数估计
\[
\boxed{
v_p(g^{\rm c}_{m,k})
\ge
\left\lceil\frac1L-\frac{k}{p-1}\right\rceil
=-\left\lfloor\frac{ks-1}{L}\right\rfloor .
}
\tag{37}
\]
原系数在非分歧环中，故这里可取整数 ceiling/floor。
类似地，若
\(\mathcal R_{m,{\rm c}}=\sum_{n\ge0}r_{m,n}X^n\)，(30) 给
\[
\boxed{
v_p(r_{m,n})\ge
\left\lceil1+\frac1L-\frac{n+1}{p-1}\right\rceil .
}
\tag{38}
\]
尤其 \(j_m=r_{m,0}\in p\mathcal O\)，与原完整 Newton 规范一致；
(38) 不宣称首行是单位。

R624 的原 \(f_4,f_1\) 都有 sigma degree 六。
因
\[
F_{\rm c}-cX\in X^2K_p[[X]],
\]
其共同两种规范的比值
\[
\exp(-6(F_{\rm c}-cX))\in1+w^{2s}K_p[[w]]
\]
不改变归一来源的 \(w^{s-1}\)、\(w^{2s-1}\) 两行。
故原首 Gaussian 的指定 \(c_\ell,d_{\ell,2}\) 与完整中央规范的
对应两行**逐项相同**。
若另外使用 R606 的 canonical 整移 \(c^\dagger-c\)，
仍须同时保留原来共同三角剪切；其 determinant 不变。

(11) 可以将这些低行放回同一真实 \(u\) 参数，且
\(h/E_{\rm c}\) 在其中整。
然而 \(\sigma/E_{\rm c}=uH/T\) 的 \(H\) 不可删：
它在低于 \(L\) 的有限窗口整，随后有 R635 的实际边界零点。
\(T(u)\) 是由原 CM 极限给出的整形式函数；
本篇未证明它是原全局函数域 \(k(E)\) 中的有理函数。
因此不能仅凭 (37) 或形式 Cartier 操作就宣称原指定两行非退化。

## 11. 来源成本与未完成的算术输入

完整规范已经支付每个严格形式群内盘的实际解析性、
整个中央连接的唯一逆及同一个 \(j_m\)。
但 \(E_{\rm c}\)、\(\Pi_0\) 和 CM 极限都依赖当前 \(p\)；
它们不是原固定全局多项式来源格中新增的免费列。

多 charge 来源不能任意共用一个标量规范。
把某条原来源除以其完整 \(E_{\rm c}^m\)，还不证明任意次数帽、
十九角、同一个 \(R\)、全部 carry 或连续饱和前缀在此操作下保持。
原九格的普通成本、惰性成本及每个 \(D/k\) 的真实旗标门继续保留。

(35) 也没有证明 \(j_m\ne0\)。
下一算术输入仍须在同一个原临界块、真实补偿或已付全来源中产生，
不能由全部解析盘内的可逆性自动替代。
本篇因此是完整中央接口的推进；固定曲线无穷素数的主目标尚未完成。

## 依赖

- [R598](R598-original-full-newton-derivatives-and-central-euler-stokes.md)、
  [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：
  同一原 \(j_m\)、首连接与完整 Newton 尾、重叠盘上的唯一解。
- [R622](R622-original-two-gaussian-central-connection-and-identical-newton-defect.md)：
  同一原零初值、第二规范和不增加中央零的接口。
- [R632](R632-original-pth-power-formal-group-boundary-and-full-kummer-range.md)、
  [R635](R635-all-original-powers-and-formal-logarithm-boundary.md)：
  原 \(u/z\) 真实内盘逆、完整首 Kummer 范围与闭边界限制。
- [R624](R624-original-paired-forcing-determinant-and-four-digit-division-return.md)、
  [R606](R606-original-gaussian-unit-gauge-and-canonical-second-central-row.md)：
  原两条临界观察、共同规范与 determinant 的实际剪切。

原 CM 乘法式、其整性极限和全部新范数界已在正文给出完整证明。
本篇没有新增有限素数扫描，也没有以 ordinary sigma 的整性替代惯性论证。
