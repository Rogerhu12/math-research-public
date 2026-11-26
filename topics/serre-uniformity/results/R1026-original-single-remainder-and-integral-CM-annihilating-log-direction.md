# R1026：原单一余式全称非零与杀 CM 的真实整 Lie 方向

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；
o2_high_coefficient / global_route / root。

**已证明：对一个定义明确的绝对界以上的全部允许素数，
R1023 的原第一余式不被 \(Q_p\) 整除。**
在已证明原 compact-type 公式的 \(p\equiv11\bmod12\) 行，
这给原 \(P=(p-1)D_0\) 在真实整 \(\delta\)-投影下的首 log 单位；
该投影杀掉全部 CM 新部分。
进一步，它在原 Jacobian Lie 格定义的饱和 CM 商中保持第 \(m\)
层本原性。这里不把这个格商冒称 R1011 任意具体简单商模型的
Néron 格，也不删掉原 CM jet 的后续比较。

## 1. 原多项式与绝对结论

先给可独立使用的纯代数结论。令 \(p\ge41,\ p\equiv5\bmod6\)，
\[
d=(p-5)/6,\qquad \ell=2d+2=(p+1)/3.
\]
取唯一 monic degree-\(d\) 多项式 \(q=Q_p\)，使
\[
y(1-y)q''+\frac43(1-2y)q'-\frac{25}{36}q=0.
\tag{1026.1}
\]
等价地，\(q/q(0)\) 是
\({}_2F_1(5/6,5/6;4/3;y)\) 在特征 \(p\) 的终止多项式；
其 \(d+1\) 次递推分子为零，而此前分母非零。
更明确地，常数项为一的终止解是
\(\sum_{j=0}^d(-d)_j^2y^j/((4/3)_j j!)\)，最高系数
\(d!/(4/3)_d\ne0\)。有限 Vandermonde 恒等式给其在一的值
\((4/3+d)_d/(4/3)_d\ne0\)：分母的整数因子是
\(4+3j\)，分子的整数因子是 \(3d+4+3j\)，\(0\le j<d\)，
全部在一与 \(p=6d+5\) 之间。故 \(q(0)q(1)\ne0\)。
在其它点，(1026.1) 的 Taylor 递推与 \(\deg q<p\)
排除重根。

保同一个原截断
\[
P_1(y)=T_{\le\ell}\frac1{(1-y)q(y)^2}.
\tag{1026.2}
\]
**定理 1026.1。** 存在 §5 明确定义、与 \(p\) 无关的正整数
\(C_*\)，使
\[
\boxed{\qquad
p>C_*,\quad p\equiv5\bmod6
\ \Longrightarrow\ q\nmid P_1-y^\ell.
\qquad}
\tag{1026.3}
\]
本纯引理不需要 \(d\) 为奇数。
其实际首 log 应用仍只取 R1023 已覆盖的
\(p\equiv11\bmod12\)，不外推另一个行的中心或图同调。

## 2. 单一整除强迫一个次数至多三的多项式

反设 \(q\mid P_1-y^\ell\)，写
\[
P_1=y^\ell+qU,\qquad \deg U\le d+2.
\]
R1024 §2 的第一条一阶计算完全不使用第二余式或中心条件，
故对某个 \(A\in\mathbf F_p\)，准确有
\[
(1-y)qU'+[3(1-y)q'-q]U
 =y^{\ell-1}(Ay-\ell).
\tag{1026.4}
\]
这里 \(A\) 是未知常数，不是 Hasse 多项式。

在 \(q\) 的任意根 \(\alpha\)，本式及其导数给
\[
3(1-\alpha)q'(\alpha)U(\alpha)
 =\alpha^{\ell-1}(A\alpha-\ell),
\]
\[
4(1-\alpha)q'(\alpha)U'(\alpha)
+[3(1-\alpha)q''(\alpha)-4q'(\alpha)]U(\alpha)
 =\ell\alpha^{\ell-2}(A\alpha-\ell+1).
\]
从 (1026.1)，
\[
q''(\alpha)/q'(\alpha)
 =-\frac{4(1-2\alpha)}{3\alpha(1-\alpha)}.
\]
把第二式乘 \(\alpha(A\alpha-\ell)\)，再以第一式消去右侧，
得到
\[
4\alpha(A\alpha-\ell)U'(\alpha)
 =[(3\ell+4)A\alpha-(3\ell+1)\ell]U(\alpha).
\]
因为 \(3\ell=p+1\)，这就是
\[
4\alpha(A\alpha-\ell)U'(\alpha)
 =(5A\alpha-2\ell)U(\alpha).
\]
过程中没有除以 \(A\alpha-\ell\)，所以其为零的根也已包含。
因此
\[
\boxed{\quad
W=\frac{4y(Ay-\ell)U'-(5Ay-2\ell)U}{q}
  \in\mathbf F_p[y],\qquad \deg W\le3.
\quad}
\tag{1026.5}
\]

## 3. 与两个固定有理幂级数的准确比较

令 \(h_p=q/q(0)\)、
\(F_p=(1-y)^{-1}h_p^{-4}\)。
从原截断 (1026.2)，
\[
U\equiv(1-y)^{-1}q^{-3}\pmod{y^\ell}.
\]
微分的误差为 \(O(y^{\ell-1})\)，而 (1026.5) 中的导数项带
一个 \(y\)，故仍准确比较到模 \(y^\ell\)。
直接用对数导数整理，得到
\[
q(0)^4W\equiv
3y(Ay-\ell)F_p'
+\left[2\ell-5Ay+\frac{y(Ay-\ell)}{1-y}\right]F_p
\pmod{y^\ell}.
\tag{1026.6}
\]

现在在 \(\mathbf Q[[y]]\) 固定
\[
h(y)={}_2F_1(5/6,5/6;4/3;y),\qquad
F(y)=(1-y)^{-1}h(y)^{-4},
\]
\[
\mathcal A(y)=3y^2F'(y)
       +\left(-5y+\frac{y^2}{1-y}\right)F(y),
\]
\[
\mathcal B(y)=-3yF'(y)
       +\left(2-\frac{y}{1-y}\right)F(y).
\tag{1026.7}
\]
这些级数完全固定，与 \(p\) 无关。
对任何固定有限次数，\(p\) 足够大时，原 (1026.1) 的低 jet
就是这些有理级数的合法模 \(p\) 约化。
于是 (1026.5)–(1026.6) 强迫
\[
A\,\mathcal A_n+\ell\,\mathcal B_n=0
\quad(4\le n<\ell)
\tag{1026.8}
\]
于所有合法的固定低次范围。
只需证明 \(\mathcal A,\mathcal B\) 的四次及以上系数列具有秩二。

## 4. 两个正 Euler 积分证明尾系数秩二

以下在实区间 \(0<y<1\) 取正分支。
置 \(t=1-y\)，并令
\[
j(t)={}_2F_1(1/2,1/2;2/3;t).
\]
直接代入 (1026.1) 的特征零方程可核：
在 \(y=1\) 的两个独立局部解是
\(h(t)\) 与 \(t^{-1/3}j(t)\)。
所以存在常数 \(C,D\)，使
\[
h(y)=C\,t^{-1/3}j(t)+D\,h(t).
\tag{1026.9}
\]

这里必须证明两项都真正出现。
按常数项为一归一后，两个 Euler 积分的核分别为
\[
u^{-1/6}(1-u)^{-1/2}(1-yu)^{-5/6},
\]
\[
u^{-1/2}(1-u)^{-5/6}(1-yu)^{-1/2}.
\]
各自乘一个固定正归一常数，再从 \(0\) 积到 \(1\)，就分别为
\(h(y)\)、\(j(y)\)。展开最后一因子并逐项作 Beta 积分即证明
这些公式；它们也与 DLMF 15.6.1 的普通 Gauss 归一一致。
当 \(y\uparrow1\) 时，两个正核在 \(u=1\) 都趋于
\((1-u)^{-4/3}\) 的非零单位倍，单调收敛给
\[
h(y)\longrightarrow+\infty,\qquad
j(y)\longrightarrow+\infty.
\]
所以 (1026.9) 中 \(C\ne0\)。
若 \(D=0\)，把该恒等式沿 \((0,1)\) 继续到 \(y\downarrow0\)，
右侧的 \(j(1-y)\) 发散而 \(h(0)=1\)，矛盾。
故
\[
C D\ne0.
\tag{1026.10}
\]
这也表明 \(h\) 在整个实区间为正，无需跨过一个未处理的零点来
继续 \(F\)。

记 \(\rho=D/C\ne0\)。从 \(h(t)=j(t)=1+O(t)\)，准确得
\[
F(y)=C^{-4}
 \left(t^{1/3}-4\rho t^{2/3}+10\rho^2t+O(t^{4/3})\right),
\]
\[
3F'(y)+F(y)/t
 =C^{-4}\left(4\rho t^{-1/3}-20\rho^2+O(t^{1/3})\right).
\tag{1026.11}
\]
这里 \(F'\) 对 \(y\) 微分，因 \(t=1-y\) 必须保其负号。

对任意复常数 \(a,b\)，由 (1026.7)
\[
a\mathcal A+b\mathcal B
 =y(ay-b)\bigl(3F'+F/t\bigr)+(2b-5ay)F.
\]
若 \(a\ne b\)，首项为
\(4C^{-4}\rho(a-b)t^{-1/3}\)，不可能是多项式。
若 \(a=b\ne0\)，第一项只有 \(O(t^{2/3})\)，第二项的首项为
\(-3aC^{-4}t^{1/3}\)，仍不可能是多项式。
故
\[
a\mathcal A+b\mathcal B\in\mathbf C[y]
 \ \Longrightarrow\ a=b=0.
\tag{1026.12}
\]
特别地，四次及以上的有理系数列线性无关。
这是固定特征零函数的严格分数幂论证，不是从有限模 \(p\)
观察推断一个全称断言。

## 5. 一个定义明确、与 \(p\) 无关的绝对界

由 (1026.12)，存在 \(4\le i<j\)，使
\[
\Delta=\mathcal A_i\mathcal B_j-\mathcal A_j\mathcal B_i\ne0.
\]
为固定规范，先选满足此条件的最小 \(j\)，再选最小 \(i\)。
记 \(M=j\)，令 \(D_{\rm rat}>0\) 是这四个有理系数的最小共同分母，
并置
\[
N_{\rm rat}=D_{\rm rat}^2\Delta\in\mathbf Z\setminus\{0\},\qquad
\boxed{\quad
C_*=\max\{41,\ 12(M+1),\ D_{\rm rat},\ |N_{\rm rat}|\}.
\quad}
\tag{1026.13}
\]
这些整数由固定有理级数唯一决定；它们的存在与非零已由
(1026.12) 证明，不随研究的素数改变。

若 \(p>C_*\)，则 \(\ell>M\)，原终止 \(h_p\) 与 \(h\) 到
所需次数的递推分母均为 \(p\)-单位，并且
\(p\nmid D_{\rm rat}N_{\rm rat}\)。
取 (1026.8) 的第 \(i,j\) 条，非零 determinant 迫
\(A=\ell=0\) 于 \(\mathbf F_p\)。
但 \(\ell=(p+1)/3\ne0\)，矛盾。定理 1026.1 成立。

本篇没有把 \(C_*\) 写成一个已计算的十进制数；
(1026.13) 是固定、有限、可按有理递推求出的精确定义。
此处的全称结论是“所有 \(p>C_*\)”，不冒称已排掉其下全部素数，
也不制造新的有限扫描完成窗口。

## 6. 原 Lie 格的真实 \(\delta\)-投影

现在只取 \(p\equiv11\bmod12\)、\(p>C_*\)，回到
R1023 的同一个 \(X_1,J_1,P\)。原甲板自同构
\(\delta:a\mapsto\zeta a\) 定义于 \(K=\mathbf Q(\zeta)\)；
\(K_p/\mathbf Q_p\) 未分歧，且该自同构真实延拓到好模型。
写 \(\delta_*\) 为它在原 Jacobian 与 Lie 格上的实际作用。

在整个
\(\mathcal L=\operatorname{Lie}(\mathcal J/R)\) 上，准确整 projector 是
\[
e_-=\frac{1+\zeta\delta_*+\zeta^2\delta_*^2}{3}.
\tag{1026.14}
\]
由于 \(3\) 为单位，它的像为整 direct summand。
原 \(N=1+\delta_*+\delta_*^2\) 满足 \(NP=0\)，故在
\(\log P\) 上才可使用
\[
e_-\log P=\frac{\log(\delta_*P)-\zeta\log P}{\zeta^2-\zeta}.
\tag{1026.15}
\]
这个线性简式不是整个 \(\mathcal L\) 上的 projector；
旧部 \(\delta=1\) 已由真正的 (1026.14) 消去。

为了读取真实作用，不猜各尾 \(\theta_s\) 的置换规范。
由原 \(a=b^p\)，\(\delta\) 在 Igusa 上为
\(b\mapsto\zeta^2b\)。原 \(\delta_*P\) 的主函数因此为
\(G(\zeta b)^2\)，全部支持仍在同样三个 \(e=3\) 尾，
\[
\lambda_\delta(b)
 =-\frac{6(\zeta^2b+\zeta)}{1-b^3}.
\]
对这个实际点重复 R1023 的同一完整推导；
因为 \(\zeta^p=\zeta^2\)，其 rational 函数为
\[
\mathscr F_\delta(b)
 =\frac{6(\zeta b^p+\zeta^2)}
        {(1-b^3)^{\ell+1}A_p(b)^2},
\]
其三个支持极部为
\[
R_\delta(b)
 =\frac{6\{\zeta^2bP_1(y)+\zeta P_2(y)\}}{y^{\ell+1}},
\qquad y=1-b^3.
\]
结合 (1026.15)，得到真实整投影的准确首向量
\[
\boxed{\quad
e_-\log P\equiv
6\varepsilon\sum_{s\in S}
 \theta_s\,
 \frac{b_s(P_1(y_s)-y_s^\ell)}{y_s^{\ell+1}}f_s
\pmod{\pi_0^{m+1}\mathcal L}.
\quad}
\tag{1026.16}
\]
原 \(b=0\) 分量在此投影中自动为零。
其余 \(S\) 的三个一组根正由 \(q(y)=0\) 参数化，且
\(b_s,y_s,\theta_s\) 都非零。
故 (1026.3) 准确给
\[
\boxed{\quad
e_-\log P\in\pi_0^m e_-\mathcal L
 \setminus\pi_0^{m+1}e_-\mathcal L.
\quad}
\tag{1026.17}
\]

## 7. 为什么该方向杀全部 CM 新部

此步消费既有实际 CM 分类与 R575 的正确甲板方向，不重做其
根号或恢复已撤回的 CM 秩零说法。

R1010 §3 的局部型分析覆盖全部 canonical 新 CM 成分：
在当前 \(p\equiv11\bmod12\) 行，它们的 CM 域全是
\(K=\mathbf Q(\sqrt{-3})\)，在二处未分歧，三处导子为二。
在惰性的 \(p\) 处，CM 诱导导子只能为零或二。
若为零，则无穷型一的 Hecke 角色在三处只有 conductor-one
的有限角色，杀 \(\zeta_3\)；其它有限处也杀这个全局单位，
与全局单位条件矛盾。因此实际 CM 新形式全来自 \(9p^2\) 层。

对这些全部 CM 形式及每个系数嵌入，Fourier 系数都满足
\[
a_n=0\quad\text{除非 }n\equiv1\bmod3,\qquad a_2=0,\quad a_4=-2.
\]
原因是素于三的 \(K\)-理想范数总为 \(1\bmod3\)，而三处已在
导子中；二处未分歧及平凡中央角色另给 \(a_4=a_2^2-2=-2\)。于是 R575 §§2–4 的实际六层 tame 标准平面计算对
它们全部适用：每条 holomorphic \(H_6\) 不变线满足
\[
\delta^*\omega=\zeta\omega.
\tag{1026.18}
\]
这不是只对一个选定 \(\theta\) 或一个系数嵌入的结论。
原 \(\kappa_4\) 下降的同构与 \(\delta\) 交换，不改变该方向。
对 Jacobian 推前 \(\delta_*\) 的 Lie 作用，与其在微分上的拉回
有相同 eigenvalue。因此全部实际 CM 新 Lie 子空间在
\(\delta_*=\zeta\) 的方向，(1026.14) 将它们杀掉。
整个旧部也被 (1026.14) 杀掉，不需要声称旧 CM 也满足
(1026.18)。

## 8. 原饱和 CM Lie 商中的本原性及仍需支付的比较

令
\[
\mathcal L^{\rm new}=\ker(N:\mathcal L\to\mathcal L),
\]
它因 \(3\) 可逆而是整 direct summand。
令 \(V_{\rm CM}\) 为 R1010 固定的实际全部 CM 新子簇的
generic-fibre Lie 子空间，并定义
\[
\mathcal L_{\rm CM}^{\rm sat}
 =\mathcal L^{\rm new}\cap V_{\rm CM}.
\]
这个子模饱和，因此
\(\mathcal Q=\mathcal L^{\rm new}/\mathcal L_{\rm CM}^{\rm sat}\)
为自由 \(R\)-模。§7 给
\(e_-\mathcal L_{\rm CM}^{\rm sat}=0\)。
由 R1023 的下界与 (1026.17)，原 \(\log P\) 在这个**由原
Jacobian 格定义**的商中准确属于
\[
\boxed{\quad
\pi_0^m\mathcal Q\setminus\pi_0^{m+1}\mathcal Q.
\quad}
\tag{1026.19}
\]
否则其像被 \(\pi_0^{m+1}\) 整除，再作用 \(e_-\) 就会违反
(1026.17)。

这个结论没有挑选一个未给出的整 Hecke 幂等元，也不要求某个
具体 quotient differential 自动饱和。
要用于 R1011 的指定 \(Q\)-simple 半秩模型，仍须比较其实际
Néron Lie 格、同源分母和原 \(c_1\) 的 Abel jet。
上述整格本原性不能自动保证该模型的某个首项为单位，
更不能据此宣布原 CM 圆盘或 O0 全部异常分支已被排除。

## 9. 来源、核准与继续范围

- [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)：原完整 first-log、实际 \(Q_p,P_1,P_2\) 及全部支持项。
- [R1024](R1024-original-complete-first-log-uniform-nonvanishing.md)：同一个 \(P_1\) 的一阶方程；本篇不使用其第二整除或中心条件。
- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)：实际正 CM 甲板方向、全部系数嵌入和原三次下降；沿用其撤回边界。
- [R1010](R1010-original-CM-divisor-nontorsion-in-nonCM-part.md) §3：全部 CM 新部的真实局部型与 CM 域覆盖；这里使用分类本身，不把其非挠范围改写。
- [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)：实际简单商及仍需核准的整尺度。
- DLMF [15.6.1](https://dlmf.nist.gov/15.6.E1)、[15.10.4](https://dlmf.nist.gov/15.10.E4)：Euler 积分和 \(y=1\) 的局部基。本文另以逐项 Beta 积分、正性及两个分数幂首项支付所需非零性，不依赖数值连接系数。

o2、global_route 与 root 独立纸核根处微分消元、未除的可能零因子、
有限 jet 精度、两个正积分、Puiseux 非多项式、固定 determinant
界及实际 \(\delta_*P\) 的全部相位。
root 另核 R575 全文与 R1010 §3 的覆盖和整 projector 范围。
本证明不使用数学程序或有限数值结果作为依据。
Serre 主目标仍 OPEN。
