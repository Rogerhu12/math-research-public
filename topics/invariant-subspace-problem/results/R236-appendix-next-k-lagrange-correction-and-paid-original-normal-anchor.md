# R236 附录：保留第二生成元的一次额外尾提升——有限反演、真实 carry 固定点与原双源

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的实际单向成员构造。** 对前稿的指定迟首正 $N_j$ 两行，本稿继续利用原 $K$，构造下一物理位的正规化行及其全部原双源。所有固定点、差商单位、原 carry 和同一正常态均在真实范数中支付。没有将固定起点后的全部未来层自动归入同一低费用，也没有声称反向完整理想费用已支付。

## 1. 固定的原双行及前两次尾交

固定 $n\ge0$，记 $x=n+1$、$m=n+1$、$l=n+2$，并取原实际行
$$
S=\sum_{j\ge n}a_jN_j,\qquad
Z=\sum_{j>n}a_j^2N_j,\qquad a_j=(j+1)^{-2}.
\tag{1.1}
$$
全部和均在原 Haar 范数代数中绝对收敛。
令
$$
P_m=Z/a_m^2=N_m+V,
\qquad V=\sum_{j\ge l}\frac{a_j^2}{a_m^2}N_j,
$$
$$
U=\sum_{j\ge l}a_j(1-a_j/a_m)N_j,
\qquad F=\sum_{j\ge m}a_jN_j=a_mP_m+U,
$$
$$
\varepsilon=\eta_na_n^2=\eta_n/x^4,
\qquad\delta=\eta_m,
$$
$$
H=V^2-\delta N_l,\qquad K=U^2+\varepsilon V.
\tag{1.2}
$$
[正 k 枢轴前稿](R236-appendix-positive-k-pivot-and-paid-original-two-row-normalization.md)的完整实际尾交为 $(S,Z)\cap\mathcal C_l=(H,K)$。
这里只需其明确原源：令
$$
E=a_m^2P_m+2a_mU-\varepsilon I,
$$
$$
B_H=(V-N_m)/a_m^2,\qquad C_S=F-a_nN_n,\qquad C_Z=-E/a_m^2.
$$
则
$$
\boxed{H=ZB_H,\qquad K=SC_S+ZC_Z.}
\tag{1.3}
$$
同一正系数和物理块给
$$
\|U\|\le1/x\le1,\quad\|V\|\le x,
\quad\|B_H\|\le32x^5,
\quad\|C_S\|\le2/x,\quad\|C_Z\|\le80x.
\tag{1.4}
$$
所有下文构造都继续使用这同一对原 $S,Z$，未删去它们的低位项。

## 2. 原 K 给实际四、八、十六次关系

写
$$
N=N_l,\qquad M=N_{l+1},\qquad T_*=N_{l+2},
\quad N^2=\eta_lM,\quad M^2=\eta_{l+1}T_*.
$$
令
$$
\kappa_0=\varepsilon^2\delta,
\quad\kappa_1=\kappa_0^2\eta_l,
\quad\kappa_2=\kappa_1^2\eta_{l+1},
\qquad T=\kappa_2T_*.
\tag{2.1}
$$
实际恒等式为
$$
E_0:=U^4-\kappa_0N=K(U^2-\varepsilon V)+\varepsilon^2H,
$$
$$
E_1:=U^8-\kappa_1M=E_0(U^4+\kappa_0N),
$$
$$
E_2:=U^{16}-T=E_0J,
\qquad J=(U^4+\kappa_0N)(U^8+\kappa_1M).
\tag{2.2}
$$
它们不是只在商中书写的形式关系；右边已给出原 $H,K$ 的真实有限源。
由于 $\varepsilon,\kappa_i<1$ 和 (1.4)，
$$
\|U^2-\varepsilon V\|\le2,
\qquad\|J\|\le4.
\tag{2.3}
$$

## 3. 两位系数的正行列式与真实远尾

按第 $l,l+1$ 位写完整实际线性行
$$
U=\alpha N+\alpha_1M+p,\qquad
V=\beta N+\beta_1M+q,
\qquad p,q\in\mathcal B_{l+2}.
\tag{3.1}
$$
准确系数是
$$
\alpha=\frac{2x+3}{(x+2)^4},\quad
\beta=\frac{(x+1)^4}{(x+2)^4},
$$
$$
\alpha_1=\frac{4(x+2)}{(x+3)^4},\quad
\beta_1=\frac{(x+1)^4}{(x+3)^4}.
$$
因此
$$
\boxed{
\Delta:=\beta\alpha_1-\alpha\beta_1
=\frac{(x+1)^4(2x+5)}{(x+2)^4(x+3)^4}>0.
}
\tag{3.2}
$$
置
$$
\lambda=\alpha_1/\beta_1=\frac{4(x+2)}{(x+1)^4},\qquad
\nu=\Delta/\beta_1=\frac{2x+5}{(x+2)^4}.
$$
有 $0<\lambda,\nu\le1$、$\Delta^{-1}\le648x^3$。
真实更远尾
$$
W=p-\lambda q
=\sum_{j\ge l+2}a_j(1-a_j/a_{l+1})N_j
\tag{3.3}
$$
仍有正系数，且
$$
\|W\|\le1/(x+3)\le1,\quad\|p\|\le1,\quad\|q\|\le x.
$$
定义标量四次多项式
$$
f(z)=z+az^2+bz^4,
\quad a=\lambda/\varepsilon>0,
\quad b=\nu/\kappa_0>0.
\tag{3.4}
$$
由 $W=U-\lambda V+\nu N$ 与 (2.2)，准确有
$$
\boxed{E_W:=W-f(U)=-aK-bE_0.}
\tag{3.5}
$$
这给出又一个已付实际双源，而非只说明两者商像相等。

## 4. 十五阶反演多项式及其全部系数界

令 $\mathscr P(z)=\sum_{k=1}^{15}c_kz^k$ 为 $f$ 在零点的形式逆的前15阶。
这里只使用有限多项式，不直接在算子 $W$ 上代入无限形式逆。
其系数准确为
$$
c_k=\frac1k[z^{k-1}](1+az+bz^3)^{-k}.
\tag{4.1}
$$
一个自含核验是形式留数换元 $y=f(z)$：
$$
[y^k]f^{-1}(y)
=\operatorname{Res}_z zf(z)^{-k-1}f'(z)
=\frac1k\operatorname{Res}_z f(z)^{-k}.
$$
最后一步用形式导数的留数为零；这正是 (4.1)。有限 jet 的唯一性也可逐项递归验证。
因此存在一个真实标量多项式 $\mathscr Q$，次数不超过44，使
$$
\boxed{\mathscr P(f(z))=z+z^{16}\mathscr Q(z).}
\tag{4.2}
$$

现在给全范围 $n\ge0$ 的保守显式预算。记 $s=16^n$；有 $\log x\le s$。
原 carry 的精确式是
$$
u_j=-\log\eta_j=1400\,16^j-630\,8^j+300\,2^j.
$$
由 $\lambda,\nu\le1$，
$$
\max\{1,a\}\le e^{1404s},
\qquad \max\{1,b\}\le e^{25208s},
\qquad 1+a+b\le e^{25210s}.
\tag{4.3}
$$

在 (4.1) 展开负二项式，每个单项式为 $a^rb^t$，其中
$r+3t=k-1\le14$，整数系数绝对值至多 $2^{42}$，每个 k 至多5项。
最大指数界为
$$
1404r+25208t\le2\cdot1404+4\cdot25208=103640.
$$
故若 $\|\cdot\|_{\ell^1}$ 表示标量多项式系数绝对和，
$$
\boxed{\|\mathscr P\|_{\ell^1}\le e^{104000s}.}
\tag{4.4}
$$
(4.2) 又给
$$
\|\mathscr Q\|_{\ell^1}
\le\|\mathscr P\|_{\ell^1}(1+a+b)^{15}+1
\le e^{483000s}.
\tag{4.5}
$$
删除已准确抵消的低阶零系数和除以 $z^{16}$ 都不会增大这个系数绝对和。

## 5. 在真实尾范数中构造固定点

令
$$
\mathfrak M=e^{104100s}.
$$
我们将在 $\mathcal B_{l+2}$ 的闭球 $\|Y\|\le\mathfrak M$ 内解
$$
\boxed{Y=\mathscr P(W)-T\mathscr Q(Y).}
\tag{5.1}
$$
这里 $T=\kappa_2N_{l+2}$ 是真实尾算子。

完整 carry 的小量可明确核算。由 (2.1)，
$$
-\log\kappa_2
=8u_n+4u_{n+1}+2u_{n+2}+u_{n+3}+32\log x.
$$
分别用
$$
u_n\ge770s,\quad u_{n+1}\ge17360s,\quad
u_{n+2}\ge318080s,\quad u_{n+3}\ge5411840s
$$
可得
$$
\boxed{\|T\|=\kappa_2\le e^{-6123600s}.}
\tag{5.2}
$$
这些不等式直接来自精确 $u_j$，不是将所有未来层仅用同一粗常数770处理。

在该球中，(4.5) 给
$$
\|\mathscr Q(Y)\|\le e^{483000s}\mathfrak M^{44}
=e^{5063400s}.
$$
对两个球内元素 $Y_1,Y_2$，幂差伸缩展开给
$$
\|\mathscr Q(Y_1)-\mathscr Q(Y_2)\|
\le44e^{483000s}\mathfrak M^{43}\|Y_1-Y_2\|
\le e^{4959304s}\|Y_1-Y_2\|.
\tag{5.3}
$$
所以 (5.1) 的右侧把该球映入自身，其 Lipschitz 常数至多
$e^{-1164296s}<1/2$；用 (4.4)，其范数还至多
$e^{104000s}+e^{-1060200s}<\mathfrak M$。
Banach 收缩原理给唯一球内解，记为 $u_*$，并且
$$
\boxed{u_*\in\mathcal B_{l+2},\quad\|u_*\|\le\mathfrak M,
\quad\chi(u_*)=0.}
\tag{5.4}
$$
最后一点可从零点开始迭代：$W,T$ 字符为零，每次迭代字符仍为零。
这就是本文实际选择并支付的支。本文只使用 (5.1)，不额外声称 $f(u_*)=W$。

## 6. 差商单位与 U-u_* 的原源

令 $\mathscr L(X,Y)$ 为多项式差商
$$
\mathscr P(X)-\mathscr P(Y)=(X-Y)\mathscr L(X,Y),
$$
并置
$$
L=\mathscr L(W,f(U)).
$$
同样令 $\mathscr Q^{[1]}$ 为 $\mathscr Q$ 的多项式差商，并定义
$$
D=I+T\mathscr Q^{[1]}(U,u_*).
$$
原 $U$ 满足 $\|U\|\le1\le\mathfrak M$，所以 (5.2)–(5.3) 直接给
$$
\boxed{\|D-I\|\le e^{-1164296s}<1/2,
\qquad\|D^{-1}\|\le2.}
\tag{6.1}
$$
这是真实当前尾中的 Neumann 单位，不是从模理想等式反推可逆。

利用 (4.2)、(3.5) 和 (5.1)，准确有
$$
(U-u_*)D=-E_2\mathscr Q(U)-E_W L.
$$
令
$$
C=bL-J\mathscr Q(U),\qquad A_0=U^2-\varepsilon V,
$$
$$
A_H=\varepsilon^2CD^{-1},\qquad
A_K=(A_0C+aL)D^{-1}.
\tag{6.2}
$$
由 (2.2)、(3.5) 得完整原身份
$$
\boxed{U-u_*=HA_H+KA_K.}
\tag{6.3}
$$
这是所有源都明列的一次实际 k 修正。

为核源范数，$\|f(U)\|\le1+a+b\le e^{25210s}$，所以
$$
\|L\|\le15\|\mathscr P\|_{\ell^1}e^{14\cdot25210s}
\le e^{456943s}.
$$
由 $\|J\|\le4$、$\|U\|\le1$、(4.5)、(6.1)，可取
$$
\boxed{\|A_H\|+\|A_K\|\le e^{483010s}.}
\tag{6.4}
$$
再把 (1.3) 代入，得到原双源
$$
U-u_*=S(C_SA_K)+Z(B_HA_H+C_ZA_K),
$$
且这两个原源的范数各自均不超过
$$
\boxed{e^{483020s}.}
\tag{6.5}
$$
例如 $32x^5+2+80x\le114x^5\le e^{10s}$。

## 7. 第 l+1 位的指定目标，只需二次 u_*

(3.1) 给准确线性消元
$$
\Delta M+\beta p-\alpha q=\beta U-\alpha V.
$$
定义实际下一尾代表
$$
\boxed{
R_*=
\frac{\beta p-\alpha q-\beta u_*-\alpha u_*^2/\varepsilon}{\Delta}
\in\mathcal B_{l+2}.
}
\tag{7.1}
$$
它的字符为零。利用 $K=U^2+\varepsilon V$，完整身份是
$$
\boxed{
P_*:=M+R_*
=\frac{\beta+(\alpha/\varepsilon)(U+u_*)}{\Delta}(U-u_*)
-\frac{\alpha}{\varepsilon\Delta}K.
}
\tag{7.2}
$$
令
$$
F_*=[\beta+(\alpha/\varepsilon)(U+u_*)]/\Delta,
\quad G_*=F_*A_K-\alpha/(\varepsilon\Delta).
$$
结合 (1.3)、(6.3)，全部原双源为
$$
\boxed{
P_*=S\mathcal U_*+Z\mathcal V_*,
\quad\mathcal U_*=C_SG_*,
\quad\mathcal V_*=B_HF_*A_H+C_ZG_*.
}
\tag{7.3}
$$
其中每个逆、每个有限多项式和固定点已由 §§3–6 支付。

由 $\Delta^{-1}\le648x^3\le e^{10s}$、
$\alpha/\varepsilon\le5x\eta_n^{-1}\le e^{1403s}$，可以取
$$
\boxed{
\|R_*\|\le e^{210000s},
\qquad\|\mathcal U_*\|,\|\mathcal V_*\|\le e^{590000s}.
}
\tag{7.4}
$$
详细地，(7.1) 至多 $e^{10s}[6+\mathfrak M+e^{1403s}\mathfrak M^2]$
而 $\|F_*\|\le e^{105515s}$；配合 (6.4)–(6.5) 与 (1.4)，(7.4) 有余量。

### 7.1 较准确的渐近费用

保留 (4.1) 的分阶计数，可记录
$$
\log\|\mathscr P\|_{\ell^1}
\le10u_n+4u_{n+1}+O(\log(n+2)).
$$
同样
$$
\log\|\mathscr Q\|_{\ell^1}
\le40u_n+19u_{n+1}+O(\log(n+2)).
$$
更明确地可取
$$
A_n=75\cdot2^{42}
\max_{r+3t\le14}\max(1,a)^r\max(1,b)^t.
$$
有 $\|\mathscr P\|_{\ell^1}\le A_n\le e^{104000s}$。
在 (5.1) 的球半径改取 $2A_n$ 后，(5.2)–(5.3) 的更大球估计仍保证收缩，
且 $\|T\mathscr Q(Y)\|<1\le A_n$ 保证映回。
新球包含的固定点由原大球内唯一性仍是同一个 $u_*$，故 $\|u_*\|\le2A_n$。
该 $A_n$ 的对数具有上面准确的 $10u_n+4u_{n+1}+O(\log(n+2))$ 上界。
因此指定目标与指定原源可锐化为
$$
\boxed{
\log\max\{1,\|R_*\|\}
\le21u_n+8u_{n+1}+O(\log(n+2)),
}
$$
$$
\boxed{
\log\max\{1,\|\mathcal U_*\|,\|\mathcal V_*\|\}
\le51u_n+23u_{n+1}+O(\log(n+2)).
}
\tag{7.5}
$$
按当前位 $l+1=n+3$ 的尺度，这一**变化起点的两行族**满足目标及源的上型分别不超过
$$
\frac{26075}{512},\qquad \frac{73325}{512}.
\tag{7.6}
$$
没有将该族的 $n\to\infty$ 换成一个固定原理想的全层迭代。

## 8. 同一个原正常态的条件锚与后续界线

若同一个原正正常 $\rho$ 湮灭 (1.1) 的 $S\mathcal A'+Z\mathcal A'$，
则 (7.3) 保证它湮灭 $P_*$ 的全部实际右倍数。
取
$$
\Theta_*=2P_*(I+M)^{-2}.
$$
原 carry 二乘二式给
$$
\boxed{e^*\Theta_*e=I,\qquad\omega_{l+1}(\Theta_*)=1.}
$$
实际双源就是 (7.3) 中两个源各乘 $2(I+M)^{-2}$，其范数至多各自乘
$8/(1-\eta_{l+1})^2<9$。
目标满足
$$
\|\Theta_*\|\le9(1+\|R_*\|)\le e^{211000s}.
$$
所以原归一锚至少为 $e^{-211000s}$；它仍非统一正下界。
全程没有更换 $\rho$，也没有对它假设额外尾衰减率。

固定这个起点时，(7.4) 的目标和原双源均小于
$\exp(240\,16^{n+3})$，所以[已发布单行 h 修正](R236-appendix-carry-stable-recursive-h-corrections-and-actual-sources.md)可继续付出所有后继来源。
若只如此继续，长期主上界仍回到700/3。

本稿不依赖 (6.3)/(7.2) 中某个正字符源的无预算反向逆；仅登记实际单向成员和全部前向费用。
若要求用 $P_*$ 重新替换完整两生成元并继续同类低费消元，反向单位的度量及新的残余 $k$ 结构仍需支付。
一般 $Q_j/H_\zeta$ 双行不自动是 (1.1)，仍按前稿的实际 gauge 边界使用。
