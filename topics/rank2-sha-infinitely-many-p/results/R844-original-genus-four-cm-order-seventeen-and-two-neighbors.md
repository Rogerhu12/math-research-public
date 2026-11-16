# R844 — 原最低属四曲线的 CM 阶17、实际定义域与三个阶34邻点

日期：2026-11-16。**状态：下述条件性几何与定义域结论已证明。**

本篇处理 R841 附录 B 的同一个原有限 Hom 展开。对其中生成
$E_0^3$、像正规化亏格恰为4的项，R843 已给两个真实三同源
椭圆商 $E_+,E_-$。本篇证明它们的整数 CM order 均为
$\mathcal O_{17}=\mathbf Z+17\mathcal O_K$，并确定其共同
$j$-域为 $H_{17}=K(17^{1/6})$。它们的三个 degree2 邻点
才具有 order34，且其 $j$-域准确等于原有限角色域 $H_\eta$。

结论的量词始终是“若原实际项的正规化达到亏格四”。
本篇不证明这种项存在或非零，也不把邻点相认成原
$q_0/q_2$ 对应或 R814 的 canonical cycle。

## 1. 保留原完整角色、Hom 与实际曲线项

固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
E_0:y^2=x^3+1,\quad
X=X_0(10404),\quad C=X_0(2601).
$$
沿 R806/R826，取 $\eta=\eta_{10}$，并保原三个角色
$$
\eta_4=\eta^{13},\qquad \eta_{10}=\eta,\qquad
\eta_{16}=\eta^7,\qquad
\eta_j^3=\psi_{17}/\psi_0.
\tag{1}
$$
这里 $\psi_0$、$\psi_{17}$ 分别是原 $E_0$ 和
$y^2=x^3+17$ 的 CM 角色。原两个权一来源是
$$
f=\theta(\eta^3\psi_0),\qquad
\mathcal G=\{g_j=\theta(\eta_j^{-2}\psi_0):j=4,10,16\}.
\tag{2}
$$
$\mathcal G$ 是整个原有理三维 Hecke 因子，不是任择一条
非有理 eigline。记相应阿贝尔簇为 $A_f,A_{\mathcal G}$，
维数分别为1和3。

R841 B 已将原完整端点写成固定有限和
$$
\widetilde Z=\sum_i c_i\,
 \Pi\,\Phi_{F_i,a_i,*}[X],\qquad
\Phi_{F,a}=(F,a q_0,a q_2).
\tag{3}
$$
其中 $F$ 经整个原 $e_f$，$a$ 经整个原 $e_{\mathcal G}$；
它们是清除有理分母后的真实曲线态射，均以 cusp
$\infty$ 为零点。原 $R_N:z\mapsto z+1/3$ 和
$S:z\mapsto z+1/2$ 满足
$$
\Phi R_N=[\omega]^{\times3}\Phi,\qquad
\Phi S=L\Phi,\qquad
L=\begin{pmatrix}
-1&0&0\\
0&-1&-1\\
0&0&1
\end{pmatrix}.
\tag{4}
$$
这些是完整态射恒等式，含原 $q_0:z\mapsto z$、
$q_2:z\mapsto4z$。本篇只处理 (3) 中一个生成 $E_0^3$ 的
实际像；令 $D$ 是其正规化，并假设 $g(D)=4$。

R841 A、B 已给其三阶自同构 $v$、二阶自同构 $s$，
以及
$$
J(D)\sim_{\overline K}E_0^4,\qquad
\dim H^0(D,\Omega^1)_\omega=3,\quad
\dim H^0(D,\Omega^1)_{\omega^2}=1.
\tag{5}
$$
以下先下降**这份实际映射**，再确定模型参数的域。

## 2. 原有限角色域准确是 ring class field $H_{34}$

对 $f\ge1$，写
$$
\mathcal O_f=\mathbf Z+f\mathcal O_K,\qquad
H_f/K=\text{其 ring class field}.
$$
令 $\mathcal H/K$ 是 $\eta$ 切出的扩张。R806 的完整定义为
$$
\eta_j((a))=
\left[
 \operatorname{Teich}_{\mu_3}(a\bmod2)^{-1}
 (a\bmod17)^{16(j-9)}
\right]^{-1}.
\tag{6}
$$
它在全局单位和有理 idèle 上平凡，导子是 $(34)$，
阶为18；原完整局部数据还给
$$
e_2(\mathcal H/K)=3,\qquad
e_{17}(\mathcal H/K)=18,\qquad
e_3(\mathcal H/K)=1.
\tag{7}
$$

这里可以直接核 ring-class 条件。对 $\ell=2,17$，
$$
(\mathcal O_{34}\otimes\mathbf Z_\ell)^\times
=\mathbf Z_\ell^\times(1+\ell\mathcal O_{K,\ell}).
$$
(6) 在第一因子上平凡，在第二因子上由真实导子一次而平凡；
其它有限位是原最大整环单位。因此 $\eta$ 在
$\widehat{\mathcal O}_{34}^{\,\times}$ 上平凡，确实因子化经过
$\operatorname{Pic}(\mathcal O_{34})$，不是只凭其阶数认 ring class。

由于 $h_K=1$，整环类群的精确列给
$$
\operatorname{Pic}(\mathcal O_f)
\simeq
(\mathcal O_K/f\mathcal O_K)^\times
\big/\bigl((\mathbf Z/f\mathbf Z)^\times\mathcal O_K^\times\bigr).
\tag{8}
$$
对 $f=34$，2和17均在 $K$ 惰性，且
$\mathcal O_{34}^\times=\{\pm1\}$，所以
$$
h_{34}
=\frac{(4-1)(17^2-1)}{(17-1)\cdot3}
=18.
\tag{9}
$$
$\eta$ 已有准确阶18，故 (8) 的角色忠实，严格得到
$$
\boxed{\mathcal H=H_{34},\qquad
\operatorname{Gal}(\mathcal H/K)\simeq C_{18}.}
\tag{10}
$$
同理 $h_{17}=6$。自然的 order 包含给
$H_{17}\subset H_{34}$；它是 (7) 中二处惯性群的固定域。
由 (1)，$\eta^3$ 切出 $E_{17}$ 相对于 $E_0$ 的 sextic
twist 域。真实坐标变换
$(x,y)\mapsto(x/17^{1/3},y/17^{1/2})$
表明该域为 $K(17^{1/6})$。于是
$$
\boxed{
H_{17}=K(17^{1/6}),\qquad
K_3:=K(17^{1/3})\subset H_{17}.}
\tag{11}
$$
$K_3/K$ 是 $\mathcal H/K$ 的唯一三次子扩张。

固定 $\sigma\in\operatorname{Gal}(\mathcal H/K)$，
使 $\eta(\sigma)=\zeta_{18}$，并取
$\zeta_{18}^6=\omega$。令
$$
\tau=\sigma^3,\qquad
\operatorname{Gal}(\mathcal H/K_3)=\langle\tau\rangle\simeq C_6 .
\tag{12}
$$
由 (7)，此六次扩张在17处完全分歧。
这些域和角色在研究素数 $p$ 之前已经固定。

## 3. 原全部实际 Hom 的定义域与同一个六阶作用

须证明 (3) 的实际映射可以取 $\mathcal H$ 定义，
而不只证明带系数的某个抽象 motive 在该域分裂。

取一个辅助 Tate 素数，分开原两个 $K$-CM 分量。
由 (2)，在所选 CM 分量上，
$$
\begin{array}{c|c}
\text{实际 Hom 空间}&
\text{相对于 }\operatorname{Hom}(E_0,E_0)\text{ 的有限角色}\\ \hline
\operatorname{Hom}(A_f,E_0)\otimes K &\eta^{-3}\\
\operatorname{Hom}(A_{\mathcal G},E_0)\otimes_K\overline K
&\eta_4^{\,2}\oplus\eta_{10}^{\,2}\oplus\eta_{16}^{\,2}.
\end{array}
\tag{13}
$$
另一 CM 分量是其共轭。这里的逆号来自
$\operatorname{Hom}(V_{\rm source},V_{E_0})$，不是任取的
twist 规范。

在 $G_{\mathcal H}$ 上所有有限角色都平凡。
Faltings 的权一同态定理遂给
$$
A_f\sim_{\mathcal H}E_0,\qquad
A_{\mathcal G}\sim_{\mathcal H}E_0^3.
\tag{14}
$$
$E_0$ 的全部几何 endomorphism 已在 $K$ 定义。
将 (14) 的同源及其有理逆复合，说明两份 Hom 的全部几何
有理同态都在 $\mathcal H$ 定义；清分母后得到真实整同态。
因此 (3) 的全部实际 $F,a$ 可在同一 $\mathcal H$ 上选择。

(13) 还支付实际的 $\tau$ 作用，而不仅给维数：
$$
\eta^{-3}(\tau)=-1,\qquad
\eta_j^2(\tau)=\zeta_{18}^{6k_j}=\omega,
\quad (k_4,k_{10},k_{16})=(13,1,7).
$$
由于三份 $k_j$ 均为 $1\bmod3$，
整个有理 Hecke packet 的 Hom 同时得到同一个 $[\omega]$，
没有剩余的三份相容性选择。
Tate 实现对实际 Hom 忠实，故
$$
\boxed{F^\tau=-F,\qquad a^\tau=[\omega]a.}
\tag{15}
$$
R841 的 $R$-等变平均由 $K$-定义的对应构成，保持 (15)。
对整数和 $a+b$ 的 polarization 同样保持 (15)。
这里不让系数域 $\mathcal E$ 的嵌入随 Galois 动作移动；
(15) 是每个实际 Hom 本体的等式。

## 4. 原曲线、基点和可能的三次扭曲下降到 $K_3$

置
$$
M=\operatorname{diag}(-1,[\omega],[\omega])\in
\operatorname{Aut}_K(E_0^3).
$$
由 (15)，
$$
\Phi^\tau=M\Phi,\qquad M^6=1.
\tag{16}
$$
因而 $D^\tau=MD$。用 $M^{-1}:D^\tau\to D$ 作下降同构，
其六个共轭复合严格为恒等，给真正的 cyclic-six descent datum。
它也使 $X\to D$ 的正规化映射满足下降条件：
其与目标 $E_0^3$ 中嵌入的复合由 (16) 一致，
正规化的泛型唯一性遂给整条态射一致。

由此得到 $K_3$ 上的 $D_0$、原映射
$X_{K_3}\to D_0$ 以及目标扭曲 $B$。
$M$ 与 (4) 的 $[\omega]^{\times3}$、$L$ 交换，
故原 $v,s$ 一并下降；它们仍保持
$X\to D_0$。原 $\infty$ 的像是一个 $K_3$-有理点，
同时被 $v,s$ 固定。

目标下降实际分裂为
$$
B=B_f\times B_g^2.
\tag{17}
$$
相对于 $E_0$ 的有限 Tate 角色分别为
$\eta^3|_{G_{K_3}}$ 和 $\eta^{-2}|_{G_{K_3}}$：
在 $\tau$ 上分别取 $-1,\omega^2$。
这也可直接由 (16) 的逆下降矩阵读取。
不要将 Hom 的 (15) 与目标的逆角色混同。

R841 的分支计算给 $D_0/\langle v\rangle$ 亏格0。
它有原 $\infty$ 所给的有理点，故确为 $\mathbf P^1_{K_3}$，
并非只在二次扩域上分裂的 conic。
$s$ 诱导的非平凡 involution 有一个有理固定分支点，
故另一个固定点也有理。六分支中已有一个固定点，
而其它轨道为二元，故两个固定点都在分支中。
将它们置于 $0,\infty$，另外四点成两对相反数。

因此可在 $K_3$ 上写成
$$
\boxed{
D_0:\quad y^3=d\,x(x^4+A x^2+B),\qquad
d,A,B\in K_3,\quad dB(A^2-4B)\ne0,
}
\tag{18}
$$
$$
v(x,y)=(x,\omega y),\qquad s(x,y)=(-x,-y).
\tag{19}
$$
$d$ 是可能的真实三次扭曲，未在 $K_3$ 内免费开立方根。
(18) 用到的只是 $\mu_3\subset K_3$ 的 Kummer 描述及实际
六个同 monodromy 分支。由于 $s^2=1$，
其对 $y$ 的 lift 必为 $-y$，不是另一个未定的六次根。

## 5. 实际 Prym 的完整 Galois endomorphism 表

记
$$
P=\operatorname{im}(1-s_J)\subset J(D_0).
$$
在 (18) 的全纯微分基
$$
dx/y^2,\quad x\,dx/y^2,\quad x^2\,dx/y^2,\quad dx/y
$$
上，$s^*$ 的特征依次为 $(-1,+1,-1,+1)$。
所以 $P$ 维数2，其两条全纯线的 $v$ 特征都为 $\omega$。
原满同态 $J(D_0)\to B$ 的核是 (5) 的
$\omega^2$ 一维部分，处于 $s=+1$。
因此在 $s=-1$ 部分上，原实际同态给同源
$$
\boxed{P\sim_{K_3}B_f\times B_g.}
\tag{20}
$$

两个 elliptic twists 的比为
$$
\vartheta=\eta^5|_{G_{K_3}}.
\tag{21}
$$
它在 $\langle\tau\rangle$ 上精确为六阶，
在17惯性上也精确为六阶。
所有几何 endomorphism 作为一个 $K$-向量空间，真实的
Galois 特征为
$$
\boxed{
\operatorname{End}^0_{\overline K}(P):
\quad 1,\ 1,\ \vartheta,\ \vartheta^{-1}.
}
\tag{22}
$$
这是 (20) 中两个 diagonal Hom 和两条 off-diagonal Hom；
所选 CM 类型在两份上相同。
尤其 (22) **没有非平凡 quadratic 特征**。
这里使用的是整个实际 endomorphism 空间，
不是某个 $h^1$ 维数推断的任意高余维 cycle 空间。

## 6. $\sqrt B$ 已在 $K_3$，并产生两个真实 $j=0$ 因子

先在代数闭包中取 $\beta^2=B$，令
$$
\delta_D(x,y)=(\beta/x,\beta y/x^2).
\tag{23}
$$
R843 A 的逐式证明在保留 $d$ 时原样成立：
$\delta_D^2=1$，它与 $s,v$ 交换。
若 $\gamma\in G_{K_3}$ 使 $\beta^\gamma=-\beta$，
则准确有
$$
\delta_D^\gamma=s\delta_D.
$$
在 $P$ 上 $s=[-1]$，故
$$
(\delta_D|_P)^\gamma=-\delta_D|_P.
\tag{24}
$$
$\delta_D|_P$ 是非零的可逆 endomorphism。
这里也须排除 $\beta$ 根本不在 $\mathcal H$ 的可能：
由 (20) 的实际 $K_3$ 同源及 $E_0$ 的全部 endomorphism 在 $K$ 定义，
$\operatorname{End}^0(P)$ 的 Galois 作用已经因子化经过
$\operatorname{Gal}(\mathcal H/K_3)$。
故对每个 $\gamma\in G_{\mathcal H}$，左侧等于 $\delta_D|_P$；
由 (24) 的同一符号公式及其非零性，$\gamma$ 必须固定 $\beta$。
先得到 $\beta\in\mathcal H$。
若仍 $\beta\notin K_3$，其符号字符便是 $C_6$ 的唯一非平凡
quadratic character，在 $\tau$ 上取 $-1$，
而 (22) 的特征仅为 $1,1,\zeta_6,\zeta_6^{-1}$，不含 $-1$，
再次矛盾。因此
$$
\boxed{\beta=\sqrt B\in K_3.}
\tag{25}
$$
这个步骤是原 Hom 角色的实质使用；仅凭 $J(D)\sim E_0^4$
不能推出 (25)。

置 $z=y/x$、$U_\pm=x\pm\beta/x$，保持全部系数：
$$
U_\pm^2=z^3/d-A\pm2\beta.
$$
取 $X_\pm=dz,\ Y_\pm=d^2U_\pm$，得到 $K_3$ 上两条实际商
$$
\boxed{
\mathcal E_\pm:\quad
Y_\pm^2=X_\pm^3+c_\pm,\qquad
c_\pm=d^4(-A\pm2\beta).
}
\tag{26}
$$
它们分别是 $D_0/\langle\delta_D\rangle$、
$D_0/\langle s\delta_D\rangle$，都非奇异，$j=0$。
其 degree2 norm maps 给
$$
P\sim_{K_3}\mathcal E_+\times\mathcal E_-.
\tag{27}
$$
两份 $v$ 都在 $dX_\pm/Y_\pm$ 上作用为 $\omega$，
所以这是与 (20) 相同的 CM 方向。

(20)、(22)、(27) 的两个不同权一 simple characters
迫使 $\{\mathcal E_+,\mathcal E_-\}$ 与
$\{B_f,B_g\}$ 在 $K_3$ 上逐一同源（允许交换）。
于是比值
$$
r=\frac{c_+}{c_-}=\frac{-A+2\beta}{-A-2\beta}\in K_3^\times
\tag{28}
$$
的 sextic Kummer character 在17惯性上有精确阶6，
由 (21) 给出，允许整体取逆。共同 $d^4$ 已准确相消；
未删去它在各自椭圆曲线中的实际 twist。
更精确地，全局 sextic Kummer character 是 $\vartheta$ 或其逆；
由 (21) 的忠实性，得到
$
K_3(\sqrt[6]{r})=\mathcal H .
\tag{28a}
$
两个真实 twist 角色的乘积则是 $\eta|_{G_{K_3}}$。
因 $c_+c_-=d^8(A^2-4B)$，
令 $c^6=d^2(A^2-4B)$，有 $c_+c_-=(dc)^6$；
其同样忠实的 Kummer character 给
$
K_3(c)=\mathcal H.
\tag{28b}
$
这说明下节归一化整个 $H_\mu$ 所需的根也已经在原域内，
而不只是两个 $j$-值在某个较小域。

## 7. 精确六阶惯性给非整数 $j$-赋值

$K_3/K$ 在17处完全分歧三次。用两个不同的规范：
$$
v_3(K_3^\times)=\mathbf Z,\quad v_3(17)=3,
\qquad v_{17}(17)=1,\quad v_{17}=v_3/3.
\tag{29}
$$
将它们延拓到所需代数闭包，置
$$
n=v_3(r)\in\mathbf Z.
$$
剩余特征17与6互素，且 $\mu_6\subset K_3$。
在最大未分歧扩张中，全部单位均可开六次根；
因此 $r$ 的 sextic Kummer character 的惯性阶准确是
$6/\gcd(6,n)$。由 (28) 的真实惯性阶6，
$$
\boxed{\gcd(n,6)=1,\qquad n\ne0.}
\tag{30}
$$

保留 $d$ 后，$D_0/s$ 的原不变量可取
$$
z=y/x,\qquad W=d(x^2-B/x^2),
$$
并满足
$$
W^2=z^6-2dAz^3+d^2(A^2-4B).
\tag{31}
$$
选择 $c^6=d^2(A^2-4B)$ 后，R843 的归一参数为
$$
\mu=-2dA/c^3,\qquad
\boxed{\mu^2=\frac{4A^2}{A^2-4B}=r+r^{-1}+2.}
\tag{32}
$$
因此 $\mu^2\in K_3$，不依赖 (18) 的三次 twist。
$A=0$ 将给 $r=-1$，与 (30) 矛盾，故 $A\ne0$。

由 $n\ne0$，(32) 右侧恰有一个严格最负赋值的项。
所以
$$
v_3(\mu)=-|n|/2,\qquad
v_{17}(\mu)=-|n|/6.
\tag{33}
$$
同一个 R843 三同源的两个实际 elliptic quotients 的
$j$ 为
$$
j_+=-\frac{6912(2\mu+5)^3}{(\mu-2)^3(\mu+2)},\qquad
j_-=-\frac{6912(5-2\mu)^3}{(\mu+2)^3(\mu-2)}.
\tag{34}
$$
6912、2、5都是17单位，且 (33) 严格为负，故每一括号的
最高 $\mu$ 项严格主导。准确得到
$$
\boxed{
v_3(j_+)=v_3(j_-)=|n|/2,\qquad
v_{17}(j_+)=v_{17}(j_-)=|n|/6\notin\mathbf Z.
}
\tag{35}
$$
特别不能把左侧 $v_3$ 的值误写成 $|n|/6$。

## 8. CM 主定理唯一确定 order17 和参数域

R843 已证明原两个实际 $E_\pm$ 的几何 endomorphism
algebra 是 $K$。设其整数 endomorphism ring 为
$\mathcal O_{f_\pm}$。CM 主定理对任意虚二次 order 给
$$
K(j_\pm)=H_{f_\pm},\qquad
[K(j_\pm):K]=h_{f_\pm}.
\tag{36}
$$
由 (32)、(34)，
$$
K(j_\pm)\subset K_3(\mu),\qquad
[K_3(\mu):K]\le6.
\tag{37}
$$

若 $17\nmid f_\pm$，ring class field $H_{f_\pm}/K$
在17处不分歧。$K/\mathbf Q$ 在17也不分歧，
所以其元素的 $v_{17}$ 只能为整数，与 (35) 矛盾。
故
$$
17\mid f_\pm,\qquad h_{f_\pm}\le6.
\tag{38}
$$
由 (8) 的一般素幂版本（单位指数在 $f>1$ 时为3），
$$
h_f=\frac f3
 \prod_{\ell\mid f}\left(1-\frac{(-3/\ell)}{\ell}\right).
\tag{39}
$$
对 $f=17$ 其值为6。将 $f=17t$ 代入，
每次提高17的幂数贡献因子17；
对另一个 $\ell^a\Vert t$，贡献
$\ell^{a-1}(\ell-(-3/\ell))$。
$\ell=2,3$ 的最小贡献都是3，其余素数贡献更大。
因此 $f$ 是17的任何真倍数时 $h_f>6$。
(38) 唯一容许
$$
\boxed{
\operatorname{End}_{\overline K}(E_+)
=\operatorname{End}_{\overline K}(E_-)=\mathcal O_{17}.
}
\tag{40}
$$

现在 (36)、(37) 两端次数都为6，故
$$
\boxed{
K(j_+)=K(j_-)=K_3(\mu)=H_{17}=K(17^{1/6}).
}
\tag{41}
$$
此外 $j_+$ 是 $\mu$ 的 $K$-有理函数，所以
$H_{17}=K(j_+)\subset K(\mu)\subset K_3(\mu)=H_{17}$；
即 $K(\mu)=H_{17}$，没有额外的常数域缺口。
由 $A\ne0$ 和 (32)，
$K_3(\sqrt{A^2-4B})=K_3(\mu)$；
而 $H_{17}=K_3(\sqrt{17})$。
因此模型参数还满足准确平方类限制
$$
\boxed{
B\in K_3^{\times2},\qquad
A^2-4B\in17\,K_3^{\times2}.
}
\tag{42}
$$
(25)、(42) 是原实际 Hom 对最低 genus-four 模型的必要条件，
不是一般 $\mu$-家族的恒等式。

原 degree3 isogeny 现在也有确定的 CM 性质。
3在 $K$ 分歧而不除17，$\mathcal O_{17}$ 只有一个
norm3 的 proper prime ideal $\mathfrak d$。
两端 order 相同，所以 R843 的指定核是此唯一 horizontal
核。$\mathfrak d^2=(3)$，而 $\mathfrak d$ 不主：
$\mathcal O_{17}$ 没有 norm3 的元素（$\mathcal O_K$ 的这些
元素是单位乘 $\sqrt{-3}$，均不在该非最大 order）。
所以其类准确为阶2，Artin 作用交换 $j_+$、$j_-$。
这恰是 (41) 中 $H_{17}/K_3$ 的非平凡元素；
在参数上为 $\mu\mapsto-\mu$，与 (34) 完全一致。

## 9. 三个真实二同源邻点的 order34 与原 $H_\eta$

固定上述任一几何椭圆商 $E$，其 endomorphism ring 为
$\mathcal O_{17}$。2在 $K$ 惰性，且不除17，
$$
\mathcal O_{17}/2\mathcal O_{17}\simeq\mathbf F_4 .
$$
$E[2]$ 的三个 order2 子群是这个二维 $\mathbf F_2$
空间的三条直线，没有一条由整个 $\mathbf F_4$ 保持。
所以没有 horizontal degree2 同源。

这也可直接从真实格读出，避免仅据同源图名称断言。
写 $E=\mathbf C/\Lambda$，$\Lambda$ 是 proper
$\mathcal O_{17}$-格。每个 subgroup 给唯一超格
$\Lambda\subset\Lambda'$，$[\Lambda':\Lambda]=2$。
在所有非2位，$\Lambda,\Lambda'$ 的整化相同；
在2处其 multiplier ring 至少包含
$\mathbf Z_2+2\mathcal O_{K,2}$，而若等于最大 order，
原那条 $\mathbf F_2$ 直线就必须 $\mathbf F_4$-稳定，矛盾。
因此三个实际 quotient 均准确有
$$
\boxed{\operatorname{End}_{\overline K}(E/C)=\mathcal O_{34}
\quad(C\subset E[2],\ |C|=2).}
\tag{43}
$$

它们的三个 $j$ 互不相同。若两条 degree2 映射有同一
目标至同构，则用一条的极化对偶复合另一条，得到
$\mathcal O_{17}$ 中 norm4 的 endomorphism。
这个 order 的 norm4 元素只有 $\pm2$；
故两条映射仅差符号，核相同，矛盾。
其中“只有 $\pm2$”同样可在 $\mathcal O_K$ 的 norm4 元素中
逐项核：其它单位乘2均不在 $\mathcal O_{17}$。

对 (43) 再用 (36)，每个邻点都满足
$$
\boxed{K(j(E/C))=H_{34}=\mathcal H.}
\tag{44}
$$
由于 $[H_{34}:H_{17}]=3$，三个邻点在
$\operatorname{Gal}(H_{34}/H_{17})$ 下构成一个完整轨道。
对 $H_{17}$ 上任意同 $j(E)$ 的模型，
$C\mapsto j(E/C)$ 是上述 Galois 等变单射；
它确定全部三个 kernel 的置换作用。
不同这样的模型仅差 quadratic twist，$-1$ 在 $E[2]$
上恒等，所以不改变这个三点作用。
若实际 quotient 被写在更大的固定域上，则对这些模点作
同一 base change，结论 (43)、(44) 保持。

由此原 order18 角色域在这个具体最低几何中有了准确位置：
它是两个 order17 商的三点 degree2 邻域的共同域。
这仍不是把某一个邻点指定为原 $q_0/q_2$，也没有把邻点的
CM ideal 与 R814 的 cycle correspondence 免费相认。

## 10. 原来源的所有系数、次数与剩余比较

本篇没有改动 (3) 的实际 Hom，只证明可以在原
$\mathcal H$ 上选择它们并完成 (16) 的下降。
因此每一项仍带 R841 的实际
$\deg(X\to D)$、polarization 系数、三个等变平均系数及
原 Artin/Hecke 系数。下降和 (26)、(34) 的坐标变化
没有被当成向原 Chow 类额外乘一个同源次数。

R843 的内部 norm isogeny 次数16、genus-two 到两个
elliptic quotients 的次数4，以及指定 degree3 isogeny，
均保持原样。原共同 $X_0$ 目标没有新增6；
返回 old 副本仍用 $6^{-2}$，原 $X_1$ 的
$1632/816$ 与 $12^{-2}$ 全部不变。

(40)–(44) 解决的是最低属四项的整数 order 和域。
尚未支付的是这类项是否实际出现、原有限线性组合是否非零，
以及该指定类到 R814 canonical 类的非零对应。
本篇没有从 CM field、同一个 Artin 轨道或单个 $j$-值
推断这些缺口，也未推出任何新的跨 $p$ AJ 非零或全
$\Sha[p^\infty]$ 结论。

全文为符号几何与类域论证明，无新增数值运行、
目标素数扫描或可重算数据。

## 11. 依赖与文献

- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)
  §2，(6)–(12)：原完整有限 $\eta$、各坏位及其共同域。
- [R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)：
  原 $\eta_j^{-2}\psi_0$ 三份 Galois packet、$\eta^3\psi_0$、
  同一个 $q/q^4$ 低权来源。
- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)、
  [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)：
  原共同目标、实际 Hom 展开及完整 $X_0/X_1$ 次数。
- [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)
  附录 A、B：完整对应等变平均、对称 polarization、
  实际 $R,S$、最低亏格及属四模型。
- [R843](R843-actual-genus-four-quotient-and-cm-three-isogeny.md)
  正文及附录 A：同一 genus-two 商、真实 degree3 isogeny、
  全常数 $j_\pm$ 和两个 $j=0$ Prym 因子。
- G. Faltings, *Endlichkeitssätze für abelsche Varietäten über
  Zahlkörpern*, Invent. Math. 73 (1983), 349–366：
  权一 Tate 同态与同源定理；本文只用于真实 abelian varieties
  的 Hom、定义域和 (14)、(20)，未用高余维 Chow 忠实性。
- J. S. Milne, *Modular Functions and Modular Forms*，
  §12 “The main theorem for orders”，印刷页123：
  <https://www.jmilne.org/math/CourseNotes/MF110.pdf>。
- A. V. Sutherland, *18.783 Elliptic Curves, Lecture 21:
  Ring class fields and the CM method*, 2023，
  Theorem21.1、Corollaries21.2、21.6、21.10：
  <https://math.mit.edu/classes/18.783/2023/LectureNotes21.pdf>。
  用于任意 order 的 $K(j)=H_f$、degree $h_f$、
  order 包含与分歧范围；(8)、(9)、(39) 的本题计数及
  (43) 的真实格计算已在正文自含写出。
