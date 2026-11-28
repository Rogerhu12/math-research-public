# R1204：原 PS 提升的准确返回、Cartier 核与剩余一维尖点商

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明，保持原 $p\equiv11\pmod{12}$ 行。** 本篇把 R1202 尚存的同底提升差，沿同一个原 ordinary node、full-$p$ 坐标和正规化子整对应实际读出。原高 PS 微分经过 $U_m/p$ 后回到 generic 最高 Hodge 层的向量，不再是一个未知矩阵列：它由下述二阶有理算子准确给出，而且该算子的像恰是原首中心 Cartier 泛函的核。

本篇没有将最高 packet 的单位直接认作单尖点单位。最后把剩余问题准确压到原特征零负 deck 尖点重数所决定的一个标量 $0$ 或 $1$，不以特殊纤维维数替代该重数。

## 1. 原格、原高 PS 输入及所求返回

保持 R1193、R1195、R1199、R1200、R1202 的全部来源。设
$$
p=12g-1>37,\quad m=(p-1)/2,\quad n=2g-1,\quad
m=3n+2,\quad p=6n+5,\quad e_0=m(p+1).
\tag{1204.1}
$$
原底环为 $R=W[\pi_0]$，$\pi_0^{e_0}=p$；$\Lambda$ 是同一原 compact-type 模型的整 Hodge 格。设
$$
E=E_m,\qquad U=U_m=p e_{V_m}e_N,\qquad q=U/p.
$$
原惯性和 deck 约定不变：
$\sigma(\pi_0)=\xi\pi_0$，
$\delta(b)=\zeta^2b$，
$\delta(u)=\zeta u$。

原中心为
$$
u^m=h(b)=r(b)^{n+1}A(b),\qquad
r(b)=1-b^3,\qquad A(b)=bQ(b^3),\qquad \deg Q=n.
\tag{1204.2}
$$
$A$ 的 $m-1$ 个简单根就是原 ordinary supersingular 集 $S$；在它们上 $r$ 非零。

取一个实际整 Hodge 提升
$$
\Psi\in E\Lambda,\qquad
\sigma^*\Psi=\xi^{(m+1)^2}\Psi,\qquad
\delta^*\Psi=\zeta^2\Psi.
$$
其特殊约化只在原中心的高 PS Hodge 空间，可写为
$$
\bar\Psi|_I=\frac{uT(b)}{r(b)A(b)}\,db,\qquad
T\in b^2k[b^3],\quad \deg T\le m-2.
\tag{1204.3}
$$
这是整个该角色空间，不是其中任取的一条线。局部阶分别为：在 SS 点是零，在三个 CM 点是 $2g-1$，在无穷点是 $m-2-\deg T$；负 deck 条件正给 $T\in b^2k[b^3]$。因此它有维数 $n$。

这些特殊微分均可取为上述实际提升：原 Hodge base change 为满射，惯性和 deck 的阶为 $p$ 单位，可以依原特征平均；$E$ 的像 exact。原全中心主系列模只有共同 $W_{m-1}$ 是 $N$ 可见的，故 $E$ 在 (1204.3) 的整个空间上为恒等，而非另添一个投影条件。

由于
$(m+1)^2=m^2+p$，R1202 应用于
$\pi_0^{e_0-p}\Psi$，给
$$
\boxed{\quad
q(\pi_0^{e_0-p}\Psi)=\pi_0^{-p}U\Psi\in\Lambda.
\quad}
\tag{1204.4}
$$
右边的特殊纤维只有 generic 尾的最高 Hodge 分量。记其第 $s$ 条尾上的系数为 $L_s^{\rm ret}$，基仍是原
$$
\omega_s^{\rm hi}=4V^{m-1}\eta.
$$
按 R1193、R1199 的同一插值规范，定义返回多项式 $T_{\rm ret}$：
$$
T_{\rm ret}(s)=\frac{2\tau_s A'(s)}m L_s^{\rm ret},
\qquad
T_{\rm ret}\in k[b^3],\quad \deg T_{\rm ret}<m-1.
\tag{1204.5}
$$
这里 $\tau_s=\lambda_s\rho_s$ 是原节点单位，不改基或改商。

本篇主公式是
$$
\boxed{\quad
T_{\rm ret}(b)=-3\gamma^2\mathscr D T(b),\qquad
\mathscr D T=(1-b^3)T''-4b^2T'-\frac94 bT.
\quad}
\tag{1204.6}
$$
$\gamma$ 为 R1200 的同一个 cyclotomic–Weil 首项单位，
$\gamma^{p-1}=-1$；尤其 $\gamma^2\in\mathbf F_p^\times$。不存在一个待定的同型常数。

## 2. 第 p 层的实际 full polynomial 来源

在第 $s$ 条 generic 尾，保持 R1199 (1199.14) 的真正函数
$$
z=V^{-1},\qquad W_s=\pi_0 V,\qquad zW_s=\pi_0.
\tag{1204.7}
$$
其中心约化满足 $u=\tau_sW_s+O(W_s^{m+1})$。这是原 level 参数的函数，不是在特殊纤维另选一个无关的 plumbing 坐标。

高 PS 输入在中心的首 normal 层是零。若该层有
$cW_s^j\,dW_s$，则过 node 后为
$-c\pi_0^{j+1}z^{-j-2}dz$。
因此尾的第 $a$ 层最大极阶是 $a+1$，而最高极阶只来自中心第零层。更高中心层降低此上界。原已存在 polar 项返回尾上时正则；node residue 为零。有理链按同一个 compact-type 树合同，不增加另一个极源。

惯性要求 generic 非零层为
$$
a=1+Nm.
$$
full 分支到该尾的无穷分歧指数为二，$\eta$ 在各 full 无穷点零阶为 $p-2$，所以该层完整 coefficient 的次数界为
$$
D_N=p+1+N(p-1).
\tag{1204.8}
$$
本篇只需 $N=0,1,2$，尤其临界 $a=p$ 对应 $N=2$、$D_2=3p-1$。这些 normal 均严格小于 $e_0$，故处在 R1021 的整个非约化 $R/(p)$ 常数仿射模型内。

determinant 运输由原完整 framing 权直接计算，不能只从两个次数相差一个 Dickson 幂猜出。R1021 (1021.1)、(1021.4)–(1021.5) 给同一实际
$x=\varpi\alpha,\ y=\varpi\beta$，其中
$\varpi^{p^2-1}=p$、$\pi_0=\varpi^2$。写
$\sigma(\varpi)=\epsilon\varpi$，$\epsilon$ 的阶为 $p^2-1$，
于是 $\xi=\epsilon^2$。算术 $\sigma$ 固定原 $x,y$，所以
$\sigma(\alpha,\beta)=\epsilon^{-1}(\alpha,\beta)$。
与此相对，正向 framing 同时将 $\alpha,\beta$ 乘 $\epsilon$；
在该正向作用下
$$
c=\alpha^p\beta-\alpha\beta^p,\qquad
\eta=d\alpha/\alpha^p
$$
的权分别是 $p+1$ 与 $1-p$。原 level 换基与 framing 交换；
$c$ 按 $\det$ 变换，而 $\eta$ 在全部 Weil 分支间为 invariant：
在 $dc=0$ 上，$d\beta=(\beta^p/\alpha^p)d\alpha$，
直接代任一 $\mathbf F_p$ 换基即得后一断言。

因此，权为 $w$ 的实际微分，其 $\pi_0^a$ 层的齐次代表
$c^t f_D\eta$ 必须满足完整的模 $p^2-1$ 角色等式
$$
D+1-p+(p+1)t\equiv-2(w-a)\pmod{p^2-1}.
\tag{1204.9a}
$$
这里的负号来自上述算术作用与正向 framing 的反向，
不是另换原惯性生成元。代入当前
$w=(m+1)^2$、$a=1+Nm$、$D=p+1+N(p-1)$，得到
$$
(p+1)t\equiv-2(m+1)^2\pmod{p^2-1},\qquad
t\equiv-(m+1)\equiv m-1\pmod{p-1}.
\tag{1204.9}
$$
这定出的是完整 determinant 角色，而不只是其模 $m$ 的中心标量。
同一公式代入最高输入
$w=m^2,\ a=Nm,\ D=(N+1)(p-1)-2$，准确恢复
$t\equiv1-m\pmod{p-1}$，与 R1199/R1202 一致。
实际读数始终是 $\Psi\bmod p$ 的 $a\le p$ 层；没有读取乘
$\pi_0^{e_0-p}$ 后越过 $p$ 的 normal。

原平面闭包的超平面正合列、$\mu_{p+1}$ 平均和 Dickson 齐次化遂将**完整**当前层放入
$$
\operatorname{Sym}^{D_N}(k^2)\otimes\det^{m-1}.
\tag{1204.10}
$$
它包含低极部、holomorphic 修正和其它中心层返回。所有 framing 因子在真正非零 pairing 分支解释，不在 $C=0$ 的评价点代入负次幂。

注意，第一个层的 $dV=2U_{\rm tail}\eta$ 只用于描述最高极部；它不是 (1204.10) 中整个 $E$-固定参考向量。该层的固定线可取 $V^{m+1}\eta$。本篇不沿 $\Theta$ 迭代来制造临界层。

## 3. 临界群环作用消去全部较低极部

写 Cartan 坐标为 $\mathsf A,\mathsf B$，避免与 $A(b)$ 混淆；置
$$
\mathsf c=\mathsf A^{p+1}-\mathsf B^{p+1},\quad
V=\mathsf A\mathsf B,\quad
U_{\rm tail}=(\mathsf A^{p+1}+\mathsf B^{p+1})/2,
\quad A_s=\mathsf c^2/4.
$$
在固定分支有 $U_{\rm tail}^2=V^{p+1}+A_s$，而 $A_s$ 仍是原尾模型的单位。

R1203 的实际正规化子固定基为
$$
F_0=(\mathsf A\mathsf B)^{m-1}
       \bigl(\mathsf A^{2(p+1)}+\mathsf B^{2(p+1)}\bigr),
\qquad
F_1=V^{3m+1}.
$$
准确关系及准确群环矩阵是
$$
F_0=2F_1+\mathsf c^2V^{m-1},
$$
$$
\bar U(F_0)=\frac14\mathsf c^2V^{m-1},\qquad
\bar U(F_1)=\frac18\mathsf c^2V^{m-1}.
\tag{1204.11}
$$
其中的 $-1/4$ transvectant 常数、Frobenius 交换及 Cartan determinant 因子均由 R1203 原群和固定。

因此临界层的任意固定多项式 $aF_0+bF_1$，若记最高项系数
$\ell=2a+b$，则
$$
\bar U(aF_0+bF_1)=\frac{\ell}{8}\mathsf c^2V^{m-1}.
\tag{1204.12}
$$
特别所有较低极部的固定线恰为
$k(F_0-2F_1)=k\,\mathsf c^2V^{m-1}$，并被原 $\bar U$ 真正杀掉。没有以“维数二”猜其作用，也没有丢掉低极部后才施算子。

在实际中心参数中写
$$
\frac{uT}{rA}\,db=\sum_{j\ge0}\beta_{j,s}W_s^j\,dW_s,
\qquad \beta_s=\beta_{p-1,s}.
\tag{1204.13}
$$
第 $p$ 层最高项是
$-\beta_s\pi_0^p z^{-p-1}dz$。
另一方面
$$
F_1\eta=-\frac12z^{-p-1}dz+
            \text{较低极阶项}.
$$
所以该实际输入的 $\ell$ 是 $2\beta_s$。
中心更高层、node 单位的高项及 affine normal 的低极部，都只能改变 (1204.11) 的被杀线；原 (1204.7) 已固定最高系数的坐标。结合 $\omega_s^{\rm hi}=4V^{m-1}\eta$，得到
$$
\boxed{\quad L_s^{\rm ret}=\frac{A_s}{4}\,\beta_s.\quad}
\tag{1204.14}
$$
这已是同一个原 $\Psi$ 的真实第 $p$ 层读数，而非一个只匹配惯性类型的参考微分。

## 4. 该节点系数是 exact Cartier 首系数

对任意正则一形式 $\omega=f(W)dW$，在特征 $p$ 中，
$$
[W^{p-1}]f(W)
 =\left(\frac{\mathcal C\omega}{dW}(0)\right)^p.
\tag{1204.15}
$$
这里 $\mathcal C$ 是 usual Cartier operator，按标量 $p^{-1}$ 线性。

特别若 $\widetilde W=W+O(W^2)$，所示系数不变。也可完全有限地证明：次数小于 $p-1$ 的单项式微分是一个次数小于 $p$ 的多项式的导数，换参后其 $W^{p-1}dW$ 系数仍为零；第 $p-1$ 项由一次项保留，较高项不贡献。故本处不需要已知节点坐标的整个高阶展开。

由 $u=\tau_sW_s+\cdots$，可在计算 $\beta_s$ 时换为
$\widetilde W=u/\tau_s$；这是 leading 为一的真实局部换参。保持全部 $\tau_s$，由 $u^m=h$ 得
$$
\frac{uT}{rA}\,db
   =\frac{m r^nT}{h'}\,du.
$$
令 $v=u^m$，在 $b=s$ 处用 $h$ 的局部逆函数，便有
$$
\boxed{\quad
\beta_s=\tau_s^p[v^2]\,
 \left(\frac{m r^nT}{h'}\right)(h^{-1}(v)).
\quad}
\tag{1204.16}
$$
此处 $2m=p-1$。系数 $\tau_s^p$ 来自
$du=\tau_s\,d\widetilde W$ 及 $u^{p-1}=\tau_s^{p-1}\widetilde W^{p-1}$；
不能少一个 $\tau_s$ 或把它任设为一。

## 5. 原 Gauss–Manin 方程与全部相位固定二阶式

置 $H=h'$，$R_0=r^n$。局部反演的准确二阶式是
$$
[v^2]f(h^{-1}(v))
 =\left.\frac{Hf''-H'f'}{2H^3}\right|_{b=s}.
\tag{1204.17}
$$
在原 $A$ 根上，R1198 (1198.4) 的同一个 Hasse 方程给
$$
\frac{H'}H=\frac{3b^2}{r},\qquad
\frac{H''}H=\frac{b(29+44b^3)}{4r^2}.
\tag{1204.18}
$$
第二式须由完整微分方程求出；不能将第一条只在根上成立的式子当作全局函数恒等式再微分。

因 $n=-5/6$ 于 $k$，
$R_0'/R_0=5b^2/(2r)$。把
$f=mR_0T/H$ 代入 (1204.17)，逐项相消给
$$
\boxed{\quad
\beta_s=
\frac{m\tau_s^p r_s^n}{2h'(s)^3}
 \left(T''-\frac{4s^2}{r_s}T'
                -\frac{9s}{4r_s}T\right)_{b=s}.
\quad}
\tag{1204.19}
$$
全程只除以 $2$、原 SS 的 $h'(s),r_s$ 和既定节点单位。

现在使用 R1200 的**同一实际 Cartier–Weil 标度**，记其原 off-diagonal 单位为 $\mathfrak B_s$：
$$
\mathfrak B_s=2r_s h'(s),\qquad
\tau_s=\mathfrak B_s^2,\qquad
A_s=-\frac{3\gamma^2}{\mathfrak B_s^{2p}}.
\tag{1204.20}
$$
由此
$A_s\tau_s^{p+1}=-12\gamma^2r_s^2h'(s)^2$。
将 (1204.19) 依次代入 (1204.14)、(1204.5)，并使用
$h'(s)=r_s^{n+1}A'(s)$，准确得到
$$
T_{\rm ret}(s)
=-3\gamma^2
 \left(rT''-4b^2T'-\frac94bT\right)_{b=s}.
$$
右边本来属于 $k[b^3]$，次数不超过 $m-2$：
对 $T=b^2P(b^3)$，每项都有这个角色和次数。
所以它与 (1204.5) 的插值多项式相同，而不是只给某个余类。
这证明 (1204.6)。

特别该返回仅依赖实际中心约化 $T$；任意具有同一 $T$ 的两个整提升，其较低极部之差均已经由 (1204.12) 消去。本结论不声称原最高型底向量经过 $q$ 后也 lift 独立；两种输入须区分。

## 6. 精确二对角矩阵及原 Cartier 泛函

置 $B=b^3$。若 $T=b^2P(B)$，$\deg P\le n-1$，则
$$
\mathscr D T=\mathscr L P,
$$
$$
\mathscr L=
9B^2(1-B)\frac{d^2}{dB^2}
+6B(3-5B)\frac d{dB}
+2-\frac{49}4B.
\tag{1204.21}
$$
在原 monomial 基中，
$$
\boxed{\quad
\mathscr D(b^{3j+2})
=(3j+2)(3j+1)B^j
 -\frac{(6j+7)^2}{4}B^{j+1},
\quad0\le j\le n-1.
\quad}
\tag{1204.22}
$$
两条对角系数全为 $p$ 单位。取一个非零 $P$ 的最低非零次数，(1204.22) 立即给 $\mathscr L P\ne0$。故实际返回映射
$$
\mathscr C:T\longmapsto T_{\rm ret}
$$
是 $n$ 维到 $n+1$ 维的注入。

对任意 $S(B)$、$\deg S\le n$，定义原标量
$$
\mathfrak c(S)
=[B^{2n+1}](1-B)^{2n+2}Q(B)S(B).
\tag{1204.23}
$$
它确实来自同一个原首中心 differential，而非另一个相同维数的泛函。因为 $u^p=uh^2$，
$$
\frac{S(b^3)}{uA}\,db
=u^{-p}r^{4g}A\,S(b^3)\,db.
$$
右侧 polynomial 的次数至多 $2p-3$；Cartier 仅能保留 $b^{p-1}db$ 项。准确地
$$
\boxed{\quad
\mathcal C\left(\frac{S(b^3)}{uA}\,db\right)
=\mathfrak c(S)^{1/p}\frac{db}{u}.
\quad}
\tag{1204.24}
$$
所有其它次数均被 Cartier 杀掉。这里的 $db/u$ 是原中心正 deck 全纯线。

## 7. actual PS 返回像恰为这个 Cartier 核

设
$$
\mu(B)=B^{-2n-2}(1-B)^{2n+2}Q(B).
$$
由于 $2n+2=1/3$ 于 $k$，对 (1204.21) 的 formal adjoint 直接求导得到
$$
\mathscr L^*\mu
=9B^{1-2n-2}(1-B)^{2n+2}
 \left(B(1-B)Q''+\frac43(1-2B)Q'
                         -\frac{25}{36}Q\right)=0.
\tag{1204.25}
$$
括号正是 R1201 的同一个 Jacobi 方程。
取 $B=0$ 的 formal residue；导数的 residue 为零，因此
$$
\mathfrak c(\mathscr L P)=0.
\tag{1204.26}
$$
这一步是代数的 exact residue，不引入一个可能除以 $p$ 的积分或端点项。

$\mathfrak c$ 本身不为零。使用同一 Rodrigues 公式
$$
Q(B)=\frac{1}{n!B^{2n+2}(1-B)^{2n+2}}
       \frac{d^n}{dB^n}\bigl(B^m(1-B)^m\bigr),
$$
直接抽取每个 monomial 的系数得
$$
\mathfrak c(B^j)
=(-1)^{2n+1-j}
 \binom m{2n+1-j}\binom{5n+3-j}{n},
\qquad0\le j\le n.
\tag{1204.27}
$$
各 factorial 参数均严格小于 $p$。特别
$$
\mathfrak c(1)=
-\binom m{2n+1}\binom{5n+3}{n}\in k^\times.
$$
结合 (1204.22)、(1204.26) 和维数，得到准确等号
$$
\boxed{\quad
\operatorname{im}\mathscr C
=\ker\mathfrak c
\subset k[B]_{\le n}.
\quad}
\tag{1204.28}
$$
这是原高 PS 提升经过原 $U_m$ 和除 $p$ 后的实际像，不是只由维数找到一个抽象同构。

对 R1201 的指定 CM 轮廓核 $S_*(B)=(B-1)^n$，上述 Cartier 值仍准确为
$$
\mathfrak c(S_*)=
-[B^{2n+1}](1-B)^mQ(B).
\tag{1204.29}
$$
本篇不把其已有数值探查外推成全素数非零或单位；(1204.28) 不依赖该额外非零性。

## 8. 原尖点格只余一个特征零重数输入

R1202 的最高惯性负 deck $W$-格记为 $\Gamma$。原特殊 Hodge 在此只含：

- generic 最高部分 $k[B]_{\le n}$，维数 $n+1$；
- 高 PS 中心部分 $b^2k[B]_{\le n-1}$，维数 $n$。

低 PS 的 $db/u$ 是正 deck，故不在本格中。
取两部分的实际整惯性提升作基，$\Gamma$ 的第二组基为
$\pi_0^{e_0-p}\Psi_j$。由 R1202，$q$ 在该 $W$-格上是真正整幂等元。其模 $p$ 矩阵可记为
$$
\bar q=
\begin{pmatrix}
A&\mathscr C\\
B_1&D
\end{pmatrix}.
\tag{1204.30}
$$
本篇已经把右上列 $\mathscr C$ 完整读出；$A,B_1,D$ 尚未被任设为零。

由幂等关系 $A\mathscr C+\mathscr CD=\mathscr C$ 和
$A^2+\mathscr CB_1=A$，
$A$ 保持 $\operatorname{im}\mathscr C=\ker\mathfrak c$。
在一维商
$k[B]_{\le n}/\ker\mathfrak c$ 上，它给一个标量
$\lambda\in\{0,1\}$。这个商上的标量与最高型整提升的选择无关：换提升使 $A$ 增加一个落在 $\operatorname{im}\mathscr C$ 的矩阵，不能改变商上的作用。

迹等式给
$$
\boxed{\quad \operatorname{rank}_W(q\Gamma)=n+\lambda.\quad}
\tag{1204.31}
$$
确切地，$\operatorname{tr}D=n-\operatorname{tr}(A|_{\ker\mathfrak c})$，
故模 $p$ 的迹为 $n+\lambda$。整幂等元的秩在
$0,\ldots,2n+1$ 内，而 $2n+1<p$，所以此同余准确确定整数秩。

因此原纯 cuspidal 最高 Hodge 的特殊像恰有两个可能：
$$
\overline{q\Gamma}\bigm|_{\rm generic}
=
\begin{cases}
\ker\mathfrak c,&\lambda=0,\\
k[B]_{\le n},&\lambda=1.
\end{cases}
\tag{1204.32}
$$
这里的左边指通过实际底向量映射的像，不把整个 $\Gamma/p\Gamma$ 与特殊 Hodge 空间混同。

若另从**原特征零谱**证明该负 deck 尖点重数为 $n+1$，则
$\lambda=1$，可用本篇实际 $\mathscr C$ 修正提升，把每一个原底向量，特别是 R1201 的 $S_*$，实现为纯 cuspidal 整微分。若重数为 $n$，其准确特殊像则只有 (1204.28)。

本篇没有用特殊纤维惯性计数提前选择这两种情形，也没有将 pure cuspidal 向量自动识别到 R1191 的指定 $C$。完整 MW 消去、指定 Abel 两列及 whole-disc 半径仍须继续按原来源处理。

## 来源与核准范围

- R1193、R1195、R1202：同一个 $E_m,U_m$、全部惯性／deck 格、单尖点投影的已付整性及实际 lift 返回。
- R1021、R1199 (1199.14)：整个非约化模 $p$ 的原 full affine 图及真正 $z=V^{-1},W_s=\pi_0V$。
- R1198 (1198.4)、R1200：原 Hasse／Gauss–Manin 方程和同一 Cartier–Weil 节点相位。
- R1203：原 $\bar U=-iq_2/4$ 及正规化子固定二维空间的准确矩阵；正文没有重新定标。
- R1201：同一个 Jacobi 方程、Rodrigues 公式与 SS 求值；完整最高 packet kernel 单位按 R1208 的 CM node 更正读取。

全文为纸面证明，未执行数学程序或重扫素数窗口。o2_high_coefficient 独立核过 (1204.17)–(1204.22) 的反演、正确 Hasse 方程、全部节点尺度及二对角单位；几何来源和商上的量词按正文单独支付。
