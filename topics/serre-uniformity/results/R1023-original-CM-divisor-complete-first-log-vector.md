# R1023：原 CM 点差在整个 Jacobian 上的准确首层对数

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明：对 \(p>37,\ p\equiv11\pmod{12}\)，原
\(P=(p-1)D_0\) 的完整形式对数仍属于第 \(m=(p-1)/2\) 层；
其首层是下面明确给出的全部 \(e=1\) 尾向量。**
证明保留真实 quotient-isogeny、非约化模 \(p\) 的 Frobenius、
原 Igusa 中心、三个原支持尾及对数的全部可能同阶项。
本篇先给准确公式；该向量非零的独立代数证明另行登记。
实际非 CM 简单商的整投影、原 CM 圆盘排点与 Serre 全局覆盖仍 OPEN。

## 1. 原对象、参数与结论

完全沿用 R1014、R1018、R1021 的原 \(X_1,J_1,D_0\)，不更换曲线、
点差、六标记、Cartan 或 ordinary quotient。设
\[
p=12g-1>37,\quad m=(p-1)/2,\quad e_0=(p^2-1)/2,
\quad R=W(k)[\pi_0],\quad \pi_0^{e_0}=p,
\]
\[
\varepsilon=\pi_0^m,\qquad \varepsilon^{p+1}=p,\qquad
P=(p-1)D_0\in\mathcal J(R).
\tag{1023.1}
\]
这里 \(k=\overline{\mathbf F}_p\)，\(\mathcal J/R\) 是原 compact-type
模型的好约化 Jacobian。\(P\) 定义于未分歧底域。

中心的同一个标准 Igusa 参数仍为 \(b\)，令
\[
r=1-b^3,\quad G(b)=\frac{(b-1)^2}{b^2+b+1},\qquad
\lambda(b)=2G'(b)/G(b)=-\frac{6(b+1)}r.
\tag{1023.2}
\]
三个 \(r=0\) 点为原 \(D_0\) 的支持，都是 \(e=3\) 尾。
原 fine 辅助椭圆曲线为
\[
E_b:\ y^2=x^3+3brx+r(1-2b^3).
\]
定义实际 Hasse 多项式
\[
h_p(b)=[x^{p-1}]
 \bigl(x^3+3brx+r(1-2b^3)\bigr)^{(p-1)/2}
       =r^{2g}A_p(b),
\]
\[
A_p(b)=bQ_p(b^3),\qquad
\deg A_p=6g-2,\quad \deg Q_p=2g-1,
\tag{1023.3}
\]
其中 \(A_p,Q_p\) 均为 monic。其简单根集
\(S=\{A_p=0\}\) 恰为全部 \(e=1\) supersingular 辅助点；
\(S\cap\{r=0\}=\varnothing\)。

在每个 \(s\in S\)，始终取 R1018 的同一个 trace-zero
\(Q=\sqrt{-3}P_{\rm level}\) 方向。记
\[
\psi_s=\beta_Q^{p-1},\qquad
f_s=[\psi_s]=[z_s^{-m}]
       \in H^1(D_s,O_{D_s}).
\]
此为原底 gap，并非整个 quotient tail 上的全局 regular 函数。
由真实 quotient-isogeny 定义常数 \(\theta_s\in k^\times\)：
\[
b_{\rm lift}-s=\varepsilon\theta_s\psi_s+\text{高阶项}.
\tag{1023.4}
\]
不把这些单位任意改成一。

置
\[
\mathscr F_p(b)=
 \frac{6(b^p+1)}{r^{4g+1}A_p(b)^2},\qquad
d_s=\frac{6(s^p+1)}{r_s^{4g+1}A_p'(s)^2}.
\]
它在 \(S\) 至多有二阶极点，且一阶极系数为零。唯一部分分式为
\[
\mathscr F_p(b)=
 \sum_{s\in S}\frac{d_s}{(b-s)^2}+R_p(b),
\tag{1023.5}
\]
其中 \(R_p\) 仅在三个 \(r=0\) 点有极点，且于无穷远消失。

**定理 1023.1。** 在整个实际 Lie 格中
\[
\log_{\mathcal J}(P)\in\pi_0^m\operatorname{Lie}(\mathcal J/R),
\]
并且
\[
\boxed{\quad
\log_{\mathcal J}(P)\equiv
 \varepsilon\sum_{s\in S}
       \theta_s\bigl(\lambda(s)+R_p(s)\bigr)f_s
 \pmod{\pi_0^{m+1}\operatorname{Lie}(\mathcal J/R)}.
\quad}
\tag{1023.6}
\]
右侧以特殊纤维 \(H^1(O)\) 识别首层；其余尾、中心及高 gap
在此层的分量全为零。这里已包含它们在原形式点中的输入，
不是把它们预先删除。

## 2. 全部惯性权与唯一可能的对数项

R1018 已计算全部余切权。用 \(\xi=\sigma(\pi_0)/\pi_0\) 表示
阶 \(e_0\) 的完整 tame 惯性生成元，\(e=1\) 尾的权为
\[
w=m(2j+1),\quad 0\le j<(p+1)/4;
\]
三个 \(e=3\) 尾的权为
\[
w=3m(2j+1),\quad 0\le j<g.
\]
中心 \(I\) 的权为 \(p+1\) 的倍数，而且没有零权：
其 tame quotient 为 \(\mathbf P^1_b\)，故
\[
H^1(I,O_I)^{\mathbf F_p^\times/\{\pm1\}}
 =H^1(\mathbf P^1,O)=0.
\]
树上的有理链不贡献 \(H^1(O)\)。因此全部实际权满足
\[
m\le w_i<pm=e_0-m.
\tag{1023.7}
\]
整 character 平均给形式参数 \(Z_i\)，使
\(\sigma Z_i=\xi^{w_i}Z_i\) 在整个形式环上成立。
原点 \(P\) 未分歧且约化为零，故
\(v_{\pi_0}(Z_i(P))\ge w_i\)。
R1018 已准确计算唯一底权输入：
\[
Z_s(P)=\varepsilon v_s+O(\pi_0^{m+1}),\qquad
v_s=\theta_s\lambda(s).
\tag{1023.8}
\]
原三个支持尾从 \(3m\) 开始；中心从至少 \(p+1\) 开始。

先处理 formal log 的全部分母，避免把 (1023.8) 当作对数。
在任一整 formal 坐标中，其不变微分是整的。若次数 \(n\)
单项式系数为 \(a_\alpha\)，则每个
\(\alpha_j a_\alpha\) 都整；因为
\(\min_jv_p(\alpha_j)\le v_p(n)\)，其分母至多
\(p^{v_p(n)}\)。用 strict integral 坐标变换消去 log 的
次数 \(2,\ldots,p-1\)；这些次数只有 \(p\)-单位分母，且变换的
线性部为恒等、与 character 相容，故 (1023.8) 不变。

写新 log 的次数 \(p\) 部分为 \(B_p\)，新 \([p]\) 的相应部分为
\(M_p\)。比较 \(L([p]Z)=pL(Z)\) 的次数 \(p\)，得到底环 \(R\)
内的准确恒等式
\[
M_p=(p-p^p)B_p,\qquad
pB_p=M_p/(1-p^{p-1}).
\tag{1023.9}
\]
在整个非约化底 \(R/(p)\) 上，Picard 的乘 \(p\) 是相对 Frobenius
再接曲线 Frobenius 的拉回；从 line-bundle transition 的 \(p\)
次幂可直接核准。因此 \(M_p\) 模 \(p\) 只有纯 \(Z_j^p\)，其矩阵
正是实际 \(H^1(O)\) 半线性 Frobenius 矩阵 \(H\)：
\[
pB_p(Z)\equiv HZ^{(p)}\pmod p.
\tag{1023.10}
\]
这是整个 \(R/(p)\) 上的式子，不只是约化至 \(k\) 的 Hasse–Witt。
上述 strict 坐标变换线性部为恒等，而模 \(p\) 的 \([p]\) 从
次数 \(p\) 开始，故不改变此矩阵。

次数 \(n>p\) 的项在原点至少有估值
\(nm-e_0v_p(n)>m\)。若 \(v_p(n)=1\)，用 \(n\ge2p\)；
若 \(v_p(n)=k\ge2\)，用
\(p^k-k(p+1)>1\)；无 \(p\) 分母时直接成立。
这些项全不能进入首层。

次数 \(p\) 的输出 \(i\)、输入 \(j\) 系数之 character 为
\(w_i-pw_j\bmod e_0\)。由于 \(pw_j>w_i\)，其除 \(p\)
后在 \(P\) 上至少有估值 \(w_i\)。所以整个 log 仍在第 \(m\) 层。
若输出 \(w_i=m\) 而输入 \(w_j>m\)，则
\(pw_j>e_0+m\)，估值至少为 \(e_0+m\)。
故首层只需底权到自身的 Frobenius 块，且须准确算到
\[
H_{\rm bottom}=\varepsilon^2K+O(\pi_0^{2m+1}).
\tag{1023.11}
\]
因为 \(\varepsilon^{p+1}=p\)，这个块正会与线性项同阶。

## 3. 真实节点、完整 Frobenius 消去与跨尾矩阵

### 3.1 节点的整提升

fine \(X_0(p)\) 的 SS 变形环正则，令 \(v,w\) 为实际同源及
其 dual 的微分乘子，则 \(vw=p\)。它们确实构成参数：
模 \(v\) 时底为特征 \(p\)，微分为零的 degree-\(p\) 同源
通过 relative Frobenius 分解，剩余 degree-one 映射为同构。
故该商环是源椭圆曲线的特征 \(p\) 变形环 \(k[[u]]\)；
\(w\) 在其中是实际 Hasse 的单位倍，有简单零。因此
\((v,w)\) 生成极大理想，完整局部环就是
\(W[[v,w]]/(vw-p)\)。这从实际微分构造参数，不预设任意
node 坐标恰等于同源微分。

用 Morava framing 平均 \(v\)，保持其主理想；
令 \(w=p/v\)，可使二者的 character 互逆。
原 target eigenparameter \(t_s=u'\) 与 \(v\) 同权，其准确形状为
\[
u'=vA(p,v^{p+1})+w^pB(p,w^{p+1}),\qquad A(0,0)\in W^\times.
\tag{1023.12}
\]
这是 character 条件：约去 \(vw=p\) 后，只有
\(v^{1+j(p+1)}\) 或 \(w^{p+j(p+1)}\) 可出现。
\(A(0,0)\) 为单位来自实际 target Hasse 的简单零。

在原 \(e=1\) 正则节点
\(R[[z,w_I]]/(zw_I-\pi_0)\) 上，\(v\) 没有水平零，因为
特征零中的同源微分处处非零。它在 \(I\) 上为单位，在尾上估值
为 \(m\)，后者正是 R1018 的原 norm derivative。
正则局部环为 UFD，故
\[
v=w_I^mU,\quad U\text{ 为单位}.
\]
只对这个单位取 Hensel \(m\) 次根，置
\[
W=w_IU^{1/m},\quad Z=zU^{-1/m};
\qquad v=W^m,\quad ZW=\pi_0.
\tag{1023.13}
\]
所以原 gap 有 \(v/\varepsilon=Z^{-m}\) 的真实节点提升。
这里没有从模 \(p\) 的等式中开一个可能丢精度的 \(m\) 次根。

R1021 在真实 affine full-\(p\) 尾上给
\[
u'=\varepsilon(c_s\psi_s+p\mathcal R_s),\qquad c_s\in W^\times.
\]
\(\mathcal R_s\) 仅在 affine 尾正则，不能预设其在节点无极点。
式 (1023.12)–(1023.13) 补足节点：在其 Laurent 重叠上，
\(v^{p+2}/\varepsilon\) 含 \(p\)，而
\(w^p/\varepsilon=p^{p-1}Z^{mp}\)。
因此在所需模 \(p\) 精度中，可以保同一 \(\psi_s\) 的常数规范取
\[
t_s=c_s\varepsilon f_s.
\tag{1023.14}
\]
此处 \(f_s\) 也表示该原类的指定整 cocycle 提升。

### 3.2 消去函数与整个中心

R1021 的真实 affine 模型在整个非约化 \(R/(p)\) 上为常数。
其 Dickson 函数
\[
\mathcal D_s=
 \frac{\alpha^{p^2}\beta-\alpha\beta^{p^2}}
      {\alpha^p\beta-\alpha\beta^p}
\]
是对实际 level 群不变的多项式，故下降为 quotient affine 尾的
全局 regular 函数。记 \(C_s=\alpha^p\beta-\alpha\beta^p\) 的
选定非零常数，有
\[
\psi_s^p=\mathcal D_s-\frac{C_s^{p-1}}{\psi_s}.
\tag{1023.15}
\]
先减 \(\mathcal D_s\)，剩下的节点项是
\(-C_s^{p-1}/f_s\)。该式保留真实 quotient，不把局部
\(\psi_s\) 冒称全局函数。

写实际参数变换
\[
b=B_s(t_s)=s+a_st_s+b_{2s}t_s^2+b_{3s}t_s^3+\cdots,
\qquad \theta_s=c_sa_s.
\]
常数项这里在模 \(p\) 后为 \(s\)；整的 \(B_s(0)\) 不必是
Teichmüller lift。中心的首主部由
\(-\varepsilon C_s^{p-1}c_s/t_s(b)\) 给出，用拉回
\(\mathbf P^1_b\) 的同一个 rational principal part
\[
R_s^*(b)=\frac{C_s^{p-1}\theta_s}{b-s}
\tag{1023.16}
\]
消去。其它尾去掉常数之后，对 \(t\ne s\) 得
\[
K_{ts}=-\frac{C_s^{p-1}\theta_s\theta_t}{(t-s)^2}.
\tag{1023.17}
\]
在自身尾，
\[
\frac{a_s}{b-s}-\frac1{t_s}
 =-\frac{b_{2s}}{a_s}
  +\left(\frac{b_{2s}^2}{a_s^2}-\frac{b_{3s}}{a_s}\right)t_s+\cdots.
\]
令 \(\mathcal S_s=\operatorname{Schwarzian}(t_s;b)(s)\)，括号内
为 \(a_s^2\mathcal S_s/6\)，故准确对角为
\[
K_{ss}=\frac{C_s^{p-1}\theta_s^2\mathcal S_s}{6}.
\tag{1023.18}
\]
这固定了交叉项和自身项的相对符号。

正 genus 的 \(I\) 没被假设为零。原底 gap 的 Frobenius
character 为 \(+m\)；在精度 \(n\le2m\) 中，中心唯一可能出现的
cohomology 角色要求 \(n=m\) 及中心权零，而该不变量已在 §2
证明不存在。其它尾则只有 \(n=2m\) 的底权能出现。故没有隐藏的
Igusa homogeneous 类、原支持尾或有理链修正。

若整 cocycle 提升相差 \(\pi_0g\)，其 Frobenius 差含
\(\pi_0^p=\pi_0^{2m+1}\)。输出 basis 改成保持同一特殊基的
整 character basis，也只把已至少为 \(\pi_0^{2m}\) 的整列改变到
\(\pi_0^{2m+1}\)。因此 (1023.17)–(1023.18) 正是
(1023.10) 所需的整矩阵，不能以“只在特殊纤维”排除此修正。

## 4. 原 Gauss–Manin、Hasse 和三阶 projective connection

取 \(\omega=dx/(2y),\eta=x\omega\)。用
\(d(x^j/y)\) 作代数 de Rham reduction，直接得到
\[
\nabla\omega=\frac{b^2}{2r}\omega+\frac1{2r}\eta,\qquad
\nabla\eta=\frac b2\omega-\frac{b^2}{2r}\eta.
\tag{1023.19}
\]
矩阵的 trace 为零，杯积配对为常数。
Frobenius 水平性模 \(p\)，或对 (1023.3) 直接微分，给
\[
h_p''-\frac{3b^2}{r}h_p'
       -\frac{b(5-4b^3)}{4r^2}h_p=0.
\tag{1023.20}
\]
写 \(P_0=r'/r=-3b^2/r\)、
\(Q_0=-b(5-4b^3)/(4r^2)\)，则相应 projective connection 为
\[
\mathcal S(b)=2Q_0-P_0'-P_0^2/2
            =\frac{b(b^3+7)}{2r^2}.
\tag{1023.21}
\]

这里只需水平晶体平凡化到三阶；递推的除数 \(1,2,3\) 皆为
\(p\)-单位。framing 的 \(\mu_{p^2-1}\) 在特殊晶体上有两条
特征线，period ratio 在其固定 Hodge 线附近的 tangent
character 与原 target \(u'\) 一致，阶为 \(p+1>3\)。
有限平均可保此平凡化的 equivariance，因此该 ratio 与 \(u'\)
的比较没有二、三次项；Kodaira–Spencer 系数 \(1/(2r_s)\)
为单位，线性项亦为单位。Schwarzian 的三阶比较遂给
\[
\mathcal S_s=\mathcal S(s).
\tag{1023.22}
\]
这里没有借用一个未说明的全局 period map；只使用实际
Serre–Tate/crystalline 比较的三个整 jet。

核准 (1023.3) 的准确归一：展开 Hasse 时，若
\(x^3,3brx,r(1-2b^3)\) 的次数分别为 \(i,j,k\)，则
\[
3g\le i\le4g-1,\quad j=12g-2-3i,\quad k=2i-6g+1.
\]
每项皆含 \(br^{2g}\)，余因子只依 \(b^3\)。
在 \(r=0\) 的最低 \(r\) 次项由
\((i,j,k)=(4g-1,1,2g-1)\) 唯一给出且非零，所以 \(A_p\)
在这三点非零。其最高次项由 nodal 多项式
\((X-1)^2(X+2)\) 给出，系数为 \(3^{(p-1)/2}=1\)，
故 \(A_p,Q_p\) 如上准确 monic。

代入 (1023.20) 得
\[
A_p''-\frac{4b^2}{r}A_p'-\frac{9b}{4r}A_p=0.
\tag{1023.23}
\]
因为 \(\deg A_p<p\)，在 \(r\ne0\) 处的合法 Taylor 递推排除
共同根 \(A_p=A_p'=0\)。这些根即原 fine Hasse 的全部简单 SS 零。
在 \(x=b^3\) 中，
\[
x(1-x)Q_p''+\frac43(1-2x)Q_p'-\frac{25}{36}Q_p=0.
\tag{1023.24}
\]
尤其 \(Q_p(0)Q_p(1)\ne0\)，并且
\(Q_p(1-x)=-Q_p(x)\)：方程对反射不变，次数
\(2g-1\) 为奇数；低次递推在该次数内的分母均非零，故同次数
多项式解一维，比较 monic 最高项即可。

## 5. 真实尺度 \(q_s\)：不删 crystalline 或 norm 单位

置
\[
q_s=C_s^{p-1}\theta_s^{p+1}.
\]
先说明全部 \(s\in S\) 属于 \(\mathbf F_{p^2}\)。
可取 Frobenius 平方为 \(-p\) 的 SS 模型，而
\(-p\equiv1\pmod6\)，所以其 full tame-six 标记定义于
\(\mathbf F_{p^2}\)；原 \(\sqrt[3]4\) 扭曲因 \(p\equiv2\pmod3\)
已在 \(\mathbf F_p\) 解开。实际 family 的模型还可能相差自同构，
下面保留它。

在实际 \(E_s\) 的 crystalline 基中写
\[
F\omega=p(a_F\omega+c_F\eta),\qquad
F\eta=b_F\omega+h\eta.
\]
\(F\) 对系数为 \(p\)-半线性，且 determinant 为 \(p\)。
在 SS 点，(1023.19) 的水平性和 determinant 给
\[
h_p'(s)=-c_{\rm GM}(s)b_F,\qquad
c_F=-1/b_F,\qquad c_{\rm GM}=1/(2r).
\]
\(F^2/p\) 在 \(\eta\) 商上的系数为
\(-b_F^{p-1}\)。确切地，另一个项
\(\sigma(h)h/p\) 模 \(p\) 为零，因为 \(h\in pW\)；
没有把 \(\sigma\) 误作特征零的字面 \(p\) 次幂。

若实际 Frobenius 平方为 \([p]\nu\)，则该 \(\eta\) 系数为
\(\nu_{\rm lin}^{-1}\)，也就是实际形式 \([p]\) 的
\(T^{p^2}\) 系数 \(U_{\rm target}\)。所以
\[
U_{\rm target}
 =-\left(h_p'(s)/c_{\rm GM}(s)\right)^{p-1}.
\tag{1023.25}
\]
这保留可能的非平凡 \(\nu\)。

令原 \(\phi,\phi^\vee\) 在特殊形式群的首项分别为
\(k_sT^p,g_sT^p\)。原 Drinfeld 根乘积、norm derivative
以及 \(\phi\phi^\vee=[p]\) 准确给
\[
C_s^{p-1}=\frac1{g_sk_s^p},\quad
U_{\rm target}=k_sg_s^p,\quad
\theta_s=-\frac{k_sg_s}{h_p'(s)}.
\]
因此所有实际形式参数尺度同时消去：
\[
\boxed{\quad
q_s=\frac{U_{\rm target}}{h_p'(s)^{p+1}}
   =-\frac{c_{\rm GM}(s)^{1-p}}{h_p'(s)^2}
   =-\frac{r_s^{8g-2}}{A_p'(s)^2}.
\quad}
\tag{1023.26}
\]
由 (1023.2)，恰有
\[
q_s\lambda(s)^p=d_s.
\tag{1023.27}
\]
没有把任何未知 \(p\)-adic unit 设为一。

## 6. 全部项合并为同一个 rational remainder

因为 \(\mathscr F_p=6(b^p+1)/(r h_p^2)\)，在
\(h_p(s)=0\) 处，其分子的正阶导数直到 \(p-1\) 都为零。
写 \(t=b-s\)，(1023.20) 给
\[
\frac{h_p(b)}{h_p'(s)}
 =t-\frac{P_0(s)}2t^2
   +\frac{P_0(s)^2-P_0'(s)-Q_0(s)}6t^3+\cdots.
\]
而 \(r^{-1}\) 的对数导数为 \(-P_0\)。
代入即可得到：\(\mathscr F_p\) 的双极系数为 \(d_s\)，
简单极系数为零，regular constant 为
\[
d_s\,\mathcal S(s)/6.
\tag{1023.28}
\]
这也证明 (1023.5) 的全部 partial-fraction 断言。

结合 (1023.8)、(1023.10)–(1023.11)，实际 log 首向量为
\[
\varepsilon\bigl(v+Kv^{(p)}\bigr).
\]
第 \(t\) 分量除以 \(\theta_t\) 后为
\[
\lambda(t)+\frac{d_t\mathcal S(t)}6
                -\sum_{s\ne t}\frac{d_s}{(t-s)^2}.
\]
由 (1023.5)、(1023.28)，它恰为
\(\lambda(t)+R_p(t)\)，证明 (1023.6)。

误差精度也准确闭合：
\(H_{\rm bottom}\) 的误差 \(\pi_0^{2m+1}\) 乘
\(\varepsilon^p/p=\varepsilon^{-1}\) 后为
\(\pi_0^{m+1}\)；模 \(p\) lift 的误差更高。
不能将该二次 Frobenius 返回项删去，也不能从原形式首层非零
直接跳过它。

## 7. 与原 Hasse 多项式完全一致的有限代数判据

令
\[
\ell=4g,\quad y=1-b^3,\quad q(y)=Q_p(y),
\]
\[
P_1(y)=T_{\le\ell}\frac1{(1-y)q(y)^2},\qquad
P_2(y)=T_{\le\ell}\frac{(1-y)^{\ell-1}}{q(y)^2}.
\tag{1023.29}
\]
这里是有限 Taylor 截断，\(q(0)\ne0\)。

利用 \(q(1-y)=-q(y)\)、\(p=3\ell-1\) 及 \(A_p=bq(b^3)\)，
同一个 rational 函数准确写成
\[
\mathscr F_p(b)=\frac6{y^{\ell+1}}
 \left\{\frac{b}{(1-y)q(y)^2}
              +\frac{(1-y)^{\ell-1}}{q(y)^2}\right\}.
\]
将两个括号截断到 \(\ell\) 次恰给全部 \(y=0\) 极部；
所得函数无其它有限极点且于无穷远消失。
故与 (1023.5) 的唯一 \(R_p\) 相同，并得到
\[
\boxed{\quad
\lambda(b)+R_p(b)
 =\frac6{y^{\ell+1}}
 \left\{b\bigl(P_1(y)-y^\ell\bigr)
                +\bigl(P_2(y)-y^\ell\bigr)\right\}.
\quad}
\tag{1023.30}
\]

对 \(q\) 的每个根 \(y\)，原 \(A_p\) 有三个不同的非零
\(b\) 根，满足 \(b^3=1-y\)。这三个根上的全零要求括号中
两个系数分别为零。原 \(b=0\) 根则给 \(y=1\) 的额外条件。
所以首向量全零**当且仅当**
\[
\boxed{\quad
q\mid P_1-y^\ell,\qquad
q\mid P_2-y^\ell,\qquad P_2(1)=1.
\quad}
\tag{1023.31}
\]
没有删掉中心 \(b=0\) 条件，没有改换 Hasse 多项式或原输入。
后继可直接在这个有限恒等式上证明全称非零。

## 8. 范围、来源与核准

本篇完整处理原 \(P=(p-1)D_0\) 的 entire-Jacobian 首 log。
R1019 的实际 \(T_5^2\) 或 \((T_{31}-32)T_5^2\) 可作用于此
真实 Lie 向量，但不能未经核准把 (1023.2) 任意替换成别的
\(d\log H\)：新支撑可能落在 \(e=1\) 尾，必须同时计算这些
实际支持项。即使本向量非零，也不自动证明 R1011 所选非 CM
简单商的整投影为单位。

- [R1014](R1014-original-CM-divisor-reduction-and-Igusa-Frobenius-principalization.md)、[R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)：原模型、全部惯性权、同一 \(G,b,\phi\)、真实 gap、原形式首层。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)：真实 affine 尾在整个非约化模 \(p\) 底上的常数化、实际 level 作用和完整 Dickson 消去函数。
- Edixhoven–Parent, [实际 stable model](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)，§§2–3；Strauch, [full-level deformation](https://arxiv.org/pdf/math/0611121)，§2.1、Theorem 2.2、Theorem 4.4。
- Conrad, [\(p\)-isogeny deformation handout](https://math.stanford.edu/~conrad/248BPage/handouts/km.pdf)：fine \(p\)-isogeny deformation 的正则局部模型；本篇保持实际两微分参数和 \(vw=p\)，再作所列单位正规化。
- [执行路径偏差及纠正](../notes/2026-11-26-execution-path-deviation-and-correction.md)：相关助手曾作不合规 V8 探索，已停止，其数值不作为本篇证明或完成窗口。

global_route 给出原几何推导，root 独立纸面核准全部权界、整 formal-log
分母及非约化精度、实际节点单位根、两类 Čech 符号、GM 矩阵、
三阶 Schwarzian、Hasse 归一、半线性 crystalline 尺度、
rational partial fraction 与 (1023.31) 的全部条件。
本篇的证明不依赖有限素数探索、矩阵秩程序或 BigInt 系数输出。
Serre 主目标仍 OPEN。
