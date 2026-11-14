# R258：固定纯自伴方向的整指数域、完整核运输与真实尾 Möbius 乘法

日期：2026-11-13（UTC）。作者：kernel。

状态：已证明的实际中间结论。本文将 R257 的局部解析思想用于一个明确的纯自伴方向，支付该方向上所有有限实参数的指数定义域，并给出真正的点乘解释。这是一般实系数的闭域工具，不把一个固定方向的指数矩扩为全部 Walsh 次数矩。规范特殊核已由最新 R236 对称高位平均附录另证为零。

## 1. 设置与结论

在原 Haar 空间取实系数 $a=(a_j)\in\ell^2$、任意常数 $a_*\in\mathbb C$，并置
$$
u=\sum_{j\ge0}a_j\chi_j,\qquad
X=a_*I+\sum_{j\ge0}a_jV_j,\qquad
B_2=\sum_{j\ge0}a_j^2(I-V_j^2).
$$
$X$ 使用 R125/R161 的实际闭实现，$Y=\phi(B_2)$，其中 $\phi$ 是零点邻域的任意解析芽。置
$$
T=X-Y,\qquad M=\ker T.
\tag{1.1}
$$
规范危险支是
$$
a_j=(-1)^j/(j+1),\quad a_*=0,\quad \phi(w)=\sqrt{1-w},\quad\phi(0)=1.
$$

在每个 Walsh 两维因子 $\{1,\chi_j\}$ 上定义
$$
n_j=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
K_j=\begin{pmatrix}0&i\\-i&0\end{pmatrix},\qquad
S_j=I-2E_j=2n_j+iK_j.
\tag{1.2}
$$
令 $U$ 为全空间酉算子
$$
U\chi_F=i^{|F|}\chi_F.
$$
定义自伴算子
$$
K_0=U^*M_uU,\qquad
H_0\chi_F=2\Big(\sum_{j\in F}a_j\Big)\chi_F
\tag{1.3}
$$
及其各自的最大自然域。这里 $M_u$ 是实际点乘算子。

**定理。** 存在全平面整的有界算子族 $A(z),B_2(z),Y(z),Q(z)$，满足
$$
A(0)=A,\quad B_2(0)=B_2,\quad Y(0)=Y,
$$
$$
T_z=H_0+iK_0+Q(z),\qquad
\operatorname{Dom}T_z=\mathcal D_0
:=\operatorname{Dom}H_0\cap\operatorname{Dom}K_0,
\qquad T_0=T.
\tag{1.4}
$$
每个 $A(z),B_2(z)$ 均准幂零，$Y(z)=\phi(B_2(z))$ 保留原解析芽。并且：

1. 对每个 $z\in\mathbb C$、$s>0$，
   $$
   \ker T_z\subseteq\operatorname{Dom}e^{s|K_0|},
   \qquad
   e^{s|K_0|}|_{\ker T_z}\in B(\ker T_z,H).
   \tag{1.5}
   $$
   范数界在有界 $z,s$ 集合上一致。

2. 每个 $w\in\mathbb C$ 的实际自伴谱指数给有界双射
   $$
   \boxed{
   e^{wK_0}:\ker T_z\longrightarrow\ker T_{z+w},
   \qquad
   (e^{wK_0})^{-1}=e^{-wK_0}.
   }
   \tag{1.6}
   $$
   两侧指数都只在已经支付的核向量域上使用，不宣称在全 $H$ 有界。

3. 令 $\widetilde M=UM$。则对所有 $s>0$，
   $$
   \boxed{
   \int e^{2s|u(y)|}|Uf(y)|^2\,d\mu(y)
   \le C_s^2\|f\|^2\qquad(f\in M)
   }
   \tag{1.7}
   $$
   对某个有限 $C_s$ 成立。实际点乘 $e^{wu}$ 将 $\widetilde M$ 有界双射到
   $\ker(UT_wU^*)$。

4. 若 $J$ 充分大，使 $\sup_{j\ge J}|a_j|<1$，定义实际正乘法符号
   $$
   q_J(y)=\prod_{j\ge J}(1+a_j\chi_j(y)).
   \tag{1.8}
   $$
   则 $q_J$、$q_J^{-1}$ 都在 $\widetilde M$ 上给全域有界映射到 $H$。
   $q_J\widetilde M$ 是闭子空间；其逆在该像上有界，并且该像是一个下文明确写出的闭算子的完整核。

这里点乘正则性的空间是 $UM$，不是未经变换的 $M$。完整核等式 (1.6) 来自本稿特定自伴指数族的全参数逆域证明；不是把 R257 的一般核包含无条件升级。

## 2. 纯分量的完整域及图范数

记 $g=\|a\|_2$。有限 Walsh 柱是 $M_u$ 的图核心：它们在
$$
L^2((1+|u|^2)\,d\mu)
$$
中稠密，因为这个有限测度的可测结构由有限柱生成。$U$ 保持有限柱，故有限柱也是 $K_0$ 的图核心。由 (1.2)，在有限柱上
$$
K_0=\lim_{m\to\infty}\sum_{j<m}a_jK_j.
$$
$H_0$ 是实对角自伴算子。

令 $P_m$ 为投影到前 $m$ 位有限柱。它与 $H_0$ 交换。对 $K_0$，将尾空间的真空记为 $\Omega$，有
$$
\|K_{\ge m}\Omega\|^2=\sum_{j\ge m}a_j^2,\qquad
\langle K_{\ge m}\Omega,\Omega\rangle=0.
$$
因此 $[K_0,P_m]$ 有界，并满足
$$
\|[K_0,P_m]\|\le\left(\sum_{j\ge m}a_j^2\right)^{1/2}\longrightarrow0.
\tag{2.1}
$$
具体地，尾交换子是
$|K_{\ge m}\Omega\rangle\langle\Omega|
-|\Omega\rangle\langle K_{\ge m}\Omega|$，其范数就是上式右端。
先在核心验证，再由 $K_0$ 闭性延到完整域。因此对 $f\in\mathcal D_0$，
$$
P_mf\to f,\quad H_0P_mf\to H_0f,\quad K_0P_mf\to K_0f.
\tag{2.2}
$$

在有限柱上，纯自交换子计算给
$$
\| (H_0+iK_0)f\|^2-\|(H_0-iK_0)f\|^2
=4\left\langle M_{\sum a_j^2\chi_j}f,f\right\rangle.
$$
与两范数之和恒等式结合，
$$
\boxed{
\|H_0f\|^2+\|K_0f\|^2
\le\|(H_0+iK_0)f\|^2+2g^2\|f\|^2.
}
\tag{2.3}
$$
由 (2.2) 延到 $\mathcal D_0$。这个估计使 $H_0+iK_0$ 在该交域上闭，并使有限柱成为其图核心。

真实进位差
$$
L=\sum_j a_j(V_j-S_j)
\tag{2.4}
$$
按算子范数绝对收敛，因为 R130/R161 给
$\|V_j-S_j\|\le8\eta_j$。
在共同有限柱核心上，
$$
X=a_*I+H_0+iK_0+L.
$$
两侧都是闭算子且具有这个共同图核心，所以
$$
\boxed{
\operatorname{Dom}X=\mathcal D_0,\qquad
X=a_*I+H_0+iK_0+L.
}
\tag{2.5}
$$
这里不是只从两个形式实虚部分推断最大域。

由 (2.3)，任意 $Q\in B(H)$ 及
$T_Q=H_0+iK_0+Q$ 均满足
$$
\boxed{
\|K_0f\|
\le\|T_Qf\|+(\|Q\|+\sqrt2\,g)\|f\|,
\qquad f\in\mathcal D_0.
}
\tag{2.6}
$$

## 3. 实际局部壳层给全平面整的 A(z)

实际链为
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
A=\alpha_0N_0,\qquad
\alpha_{j+1}/\alpha_j=\eta_j,
$$
$$
\eta_j\le e^{-770\,16^j}.
\tag{3.1}
$$
逐次展开得到算子范数收敛的精确式
$$
A=\sum_{\ell\ge0}\alpha_\ell C_\ell,\qquad
C_\ell=E_0^*\cdots E_{\ell-1}^*E_\ell.
\tag{3.2}
$$
$C_\ell$ 只作用于前 $\ell+1$ 位，$\|C_\ell\|=1$。令
$$
A^{[m]}=\sum_{\ell<m}\alpha_\ell C_\ell.
$$
按物理二进制有限头顺序，这是严格前移矩阵，故
$$
(A^{[m]})^{2^m}=0,\qquad
\|A-A^{[m]}\|\le\alpha_m.
\tag{3.3}
$$

记
$$
K_{0,m}=\sum_{j<m}a_jK_j,\qquad
s_m=\sum_{j\le m}|a_j|.
$$
定义
$$
A(z)=\sum_{\ell\ge0}\alpha_\ell
 e^{zK_{0,\ell+1}}C_\ell e^{-zK_{0,\ell+1}}.
\tag{3.4}
$$
对 $|z|\le R$，第 $\ell$ 项范数至多
$$
\alpha_\ell e^{2Rs_\ell}
\le\alpha_\ell e^{2Rg\sqrt{\ell+1}},
$$
故该级数在每个紧盘上一致绝对收敛，定义整的 $B(H)$ 值函数。
它在虚轴上就是实际酉共轭：
$$
A(it)=e^{itK_0}Ae^{-itK_0}.
\tag{3.5}
$$
此式对全空间成立，因为 $e^{itK_0}$ 是全空间酉算子，而每个局部壳只与相应有限头发生作用。

相容的有限截断是
$$
A^{[m]}(z)=e^{zK_{0,m}}A^{[m]}e^{-zK_{0,m}}.
$$
设 $\eta_*=\sup_j\eta_j<1$。由
$s_\ell\le g\sqrt m+g\sqrt{\ell-m+1}$ 和
$\alpha_\ell/\alpha_m\le\eta_*^{\ell-m}$，得到
$$
\boxed{
\sup_{|z|\le R}\|A(z)-A^{[m]}(z)\|
\le C_R\alpha_m e^{2Rg\sqrt m},
}
\tag{3.6}
$$
其中可取
$$
C_R=\sum_{q\ge0}\eta_*^q e^{2Rg\sqrt{q+1}}<\infty.
$$

### 3.1 每个 A(z) 都确实准幂零

令 $d=2^m$，在 $|z|\le R$ 上统一取
$$
M_R\ge1+\sup_m\sup_{|z|\le R}
\big(\|A(z)\|+\|A^{[m]}(z)\|\big).
$$
因 $(A^{[m]}(z))^d=0$，真实幂差恒等式给
$$
\|A(z)^d\|
\le dM_R^{d-1}C_R\alpha_m e^{2Rg\sqrt m}.
\tag{3.7}
$$
另一方面
$$
\alpha_m\le\alpha_0
 \exp\left[-\frac{770}{15}(16^m-1)\right].
$$
所以 (3.7) 的 $d$ 次根趋零，且在紧 $z$ 盘上一致。谱半径公式遂给
$$
\boxed{\sigma(A(z))=\{0\}\quad(z\in\mathbb C).}
\tag{3.8}
$$
这一步使用了准确的局部有限头幂零阶及超快尾。单纯“范数极限是幂零矩阵的极限”不能代替它。

## 4. Cayley 与 Bell 分支的整运输

令 $d_j$ 为原归一化常数，定义
$$
N_j(z)=A(z)^{2^j}/d_j.
$$
也可以按真实局部链写成
$$
N_j(z)=\sum_{\ell\ge j}\frac{\alpha_\ell}{\alpha_j}
 e^{z\sum_{k=j}^{\ell}a_kK_k}
 (E_j^*\cdots E_{\ell-1}^*E_\ell)
 e^{-z\sum_{k=j}^{\ell}a_kK_k}.
\tag{4.1}
$$
这两个整函数在虚轴相等，因而全平面相等。
置
$$
E_j(z)=e^{za_jK_j}E_je^{-za_jK_j}.
$$
同样的局部串估计给
$$
\boxed{
\sup_j\sup_{|z|\le R}\|N_j(z)\|<\infty,\qquad
\|N_j(z)-E_j(z)\|\le C'_R\eta_j.
}
\tag{4.2}
$$
例如尾串长度 $q+1$ 的指数成本至多
$e^{2Rg\sqrt{q+1}}$，而第一个进位提取出 $\eta_j$，其后由 $\eta_*^{q-1}$ 求和。
$E_j(z)^2=0$。

每个 $N_j(z)$ 由 (3.8) 准幂零，故
$$
V_j(z)=(I-N_j(z))(I+N_j(z))^{-1}
$$
在全平面有定义并为整函数。其逆预算必须对 $j$ 一致：

- 对充分大 $j$，(4.2) 使 $N_j(z)$ 一致接近 $E_j(z)$，
  而 $(I+E_j(z))^{-1}=I-E_j(z)$ 在紧盘上一致有界，Neumann 公式给一致逆界。
- 余下有限多个 $j$，由各自准幂零性和紧盘连续性取最大逆界。

因此
$$
\sup_j\sup_{|z|\le R}\|V_j(z)\|<\infty.
\tag{4.3}
$$
实际逆差式还给，置 $S_j(z)=I-2E_j(z)$ 后，
$$
\boxed{
\|V_j(z)-S_j(z)\|\le C''_R\eta_j
\qquad(|z|\le R).
}
\tag{4.4}
$$
于是
$$
L(z)=\sum_j a_j(V_j(z)-S_j(z)),\qquad
B_2(z)=\sum_j a_j^2(I-V_j(z)^2)
\tag{4.5}
$$
都在紧盘上一致范数收敛，故为整函数。

### 4.1 Bell 的零字符不能省略

固定 $z$，令 $\mathcal A_z$ 为 $A(z)$ 生成的闭幺交换算子代数。
由 (3.7)，其任意 character $\xi$ 满足
$$
|\xi(A(z))|^{2^m}\le\|A(z)^{2^m}\|,
$$
所以 $\xi(A(z))=0$。
$I+N_j(z)$ 的逆属于该闭代数（可由准幂零 Neumann 幂级数得到），于是
$\xi(V_j(z))=1$，继而由 (4.5)
$$
\xi(B_2(z))=0.
$$
交换 Banach 代数的谱刻画给
$$
\boxed{\sigma(B_2(z))=\{0\}.}
\tag{4.6}
$$

取 $\phi$ 的任意固定小圆解析轮廓，围住零点且位于其解析域内。
该轮廓在每个 $z$ 都避开 $\sigma(B_2(z))$；在每个紧 $z$ 盘上预解式一致有界。
因此
$$
\boxed{Y(z)=\phi(B_2(z))}
\tag{4.7}
$$
是全平面整的有界算子族，且
$$
Y(it)=e^{itK_0}Ye^{-itK_0}.
$$
这里保留的是同一个解析芽及字符 $\phi(0)$；没有沿参数更换平方根符号。

## 5. 完整闭算子族及虚轴上的实际域共轭

定义
$$
Z(z)=2\sum_j a_j
 \big(e^{za_jK_j}n_je^{-za_jK_j}-n_j\big).
\tag{5.1}
$$
第 $j$ 项在 $|z|\le R$ 上范数至多
$4R a_j^2e^{2Rg}$，所以 $Z$ 是整的有界族。
令
$$
Q(z)=a_*I+Z(z)+L(z)-Y(z),\qquad
T_z=H_0+iK_0+Q(z),\quad \operatorname{Dom}T_z=\mathcal D_0.
\tag{5.2}
$$
由 §2，每个 $T_z$ 都闭，有限柱是共同图核心。

还必须证明实际酉共轭保持这个域。对有限 $K_{0,m}$，
$$
e^{itK_{0,m}}H_0e^{-itK_{0,m}}
=H_0+
2\sum_{j<m}a_j(e^{ita_jK_j}n_je^{-ita_jK_j}-n_j).
$$
右侧有界差按算子范数收敛，左侧酉因子强收敛到 $e^{itK_0}$。
对任意 $f\in\operatorname{Dom}H_0$，用 $H_0$ 闭性取极限；
再把 $t$ 换成 $-t$，得到双向域保持及
$$
e^{itK_0}H_0e^{-itK_0}=H_0+Z(it).
\tag{5.3}
$$
$e^{itK_0}$ 自然双向保持 $\operatorname{Dom}K_0$。
故它也双向保持 $\mathcal D_0$。

所有局部族满足参数平移的协变式；特别
$$
Z(z+it)=Z(it)+e^{itK_0}Z(z)e^{-itK_0},
$$
且 $L,B_2,Y$ 满足不带加项的同类式。
因此在完整共同域上
$$
\boxed{
e^{itK_0}T_ze^{-itK_0}=T_{z+it}
\qquad(t\in\mathbb R,\ z\in\mathbb C).
}
\tag{5.4}
$$
此外对 $r\ge1$，
$$
e^{itK_0}Q^{(r)}(z)e^{-itK_0}=Q^{(r)}(z+it).
\tag{5.5}
$$
实际单位群差商和 $K_0$ 闭性给
$$
Q^{(r)}(z)\operatorname{Dom}K_0\subseteq\operatorname{Dom}K_0,
\qquad
[K_0,Q^{(r)}(z)]=Q^{(r+1)}(z).
\tag{5.6}
$$
逐阶使用即得所有有限 $K_0$ 幂域的保持。这里的导数域式来自 (5.5)，不是由 $B(H)$ 整性本身猜测。

## 6. 核向量的实际自然幂与统一局部解析界

先给一个域差商。若 $f\in\mathcal D_0$ 且 $T_zf\in\operatorname{Dom}K_0$，则由 (5.4)
$$
T_z\frac{e^{itK_0}-I}{it}f
=
\frac{e^{itK_0}-I}{it}T_zf+
e^{itK_0}\frac{Q(z-it)-Q(z)}{it}f.
$$
$t\to0$ 时，两边的输入和右侧都在 $H$ 收敛。
$T_z$ 闭性给
$$
\boxed{
K_0f\in\mathcal D_0,\qquad
T_zK_0f=K_0T_zf-Q'(z)f.
}
\tag{6.1}
$$

对 $f\in\ker T_z$，(6.1) 与 (5.6) 逐阶给
$$
K_0^nf\in\mathcal D_0\quad(n\ge0),
$$
以及真实域公式
$$
\boxed{
T_zK_0^nf
=-\sum_{r=0}^{n-1}\binom n{r+1}
 Q^{(r+1)}(z)K_0^{n-1-r}f
\quad(n\ge1).
}
\tag{6.2}
$$
域归纳如下：已知 $K_0^nf\in\mathcal D_0$，先得到下一次 $K_0$ 作用有定义；
(6.2) 右侧各项因 (5.6) 落入 $\operatorname{Dom}K_0$，
故可对 $K_0^nf$ 再用 (6.1)，同时得到下一阶域和公式。

固定 $R>0$，定义有限常数
$$
L_R=\sup_{|z|\le R}\|Q(z)\|+\sqrt2\,g,\qquad
C_R=\max\left(1,\sup_{|\zeta|\le R+1}\|Q'(\zeta)\|\right).
$$
Cauchy 估计给
$$
\|Q^{(r+1)}(z)\|\le C_Rr!\qquad(|z|\le R).
\tag{6.3}
$$
取
$$
K_R=\max(2,\,2L_R,\,2\sqrt{C_R}).
\tag{6.4}
$$
则
$$
\boxed{
\|K_0^nf\|\le K_R^n n!\|f\|,
\qquad f\in\ker T_z,\ |z|\le R.
}
\tag{6.5}
$$

证明：$n=0$ 显然，$n=1$ 由 (2.6)。
若已知较低阶界，(6.2) 给
$$
\begin{aligned}
\|T_zK_0^nf\|
&\le C_R n!K_R^{n-1}
 \sum_{r=0}^{n-1}\frac{K_R^{-r}}{r+1}\|f\|\\
&\le2C_R n!K_R^{n-1}\|f\|.
\end{aligned}
$$
再对 $K_0^nf$ 使用 (2.6)，
$$
\|K_0^{n+1}f\|
\le n!K_R^{n+1}
 \left(\frac{2C_R}{K_R^2}+\frac{L_R}{K_R}\right)\|f\|
\le n!K_R^{n+1}\|f\|.
$$
这比所需下一阶界还强。归纳完成。

自伴谱演算和绝对收敛的指数级数由此给，对 $|h|<K_R^{-1}$，
$$
f\in\operatorname{Dom}e^{|h||K_0|},\qquad
e^{hK_0}f=\sum_{n\ge0}\frac{h^n}{n!}K_0^nf,
$$
$$
\|e^{hK_0}f\|\le(1-K_R|h|)^{-1}\|f\|.
\tag{6.6}
$$

### 6.1 局部核运输确实处于完整闭域

在小盘内置 $g(h)=e^{hK_0}f$。它是 $H$ 值全纯函数。
对虚参数 $h=it$，(5.4) 给
$$
T_zg(it)=-[Q(z+it)-Q(z)]g(it).
$$
考虑 $H\oplus H$ 值全纯函数
$$
h\longmapsto
\big(g(h),-[Q(z+h)-Q(z)]g(h)\big).
$$
它在虚轴小区间落入闭线性空间 $\operatorname{Graph}T_z$。
任意消灭该闭图的连续线性泛函与之复合后都是全纯函数，
且在有聚点的集合为零，所以在整个小盘为零。
闭图的双重消灭刻画遂给
$$
g(h)\in\mathcal D_0,\qquad
T_zg(h)=-[Q(z+h)-Q(z)]g(h).
$$
因此
$$
\boxed{e^{hK_0}\ker T_z\subseteq\ker T_{z+h}}
\tag{6.7}
$$
在这个实际小盘内成立。
这个论证没有假定一般闭算子的高次幂自动闭，也没有把未定义的复指数共轭作用在全空间。

## 7. 用紧参数一致半径走到任意实参数，并得到完整核等式

固定初始 $z$ 与任意有限实数 $t$。
取一个包含线段 $z+[0,t]$ 的有界盘，并使用 §6 的同一个 $K_R$。
把该线段分成有限多段，每段长度小于 $1/(2K_R)$。
由 (6.7) 逐段应用实际谱指数，每步都有定义且范数至多扩大两倍。

自伴谱演算的乘积规则在这些已经付清的域上给
$$
e^{h_2K_0}e^{h_1K_0}f=e^{(h_1+h_2)K_0}f.
$$
所以对每个实 $t$，
$$
e^{tK_0}:\ker T_z\longrightarrow\ker T_{z+t}
$$
全域有界。对纯虚参数用 (5.4) 的全空间酉算子，便得到全部复 $w$ 的有界核映射。

现在从终点核 $\ker T_{z+w}$ 出发，沿反向参数重复同一个构造，
得到有界的实际 $e^{-wK_0}$。两个谱指数的乘积在这些域上为恒等，
所以
$$
\boxed{e^{wK_0}\ker T_z=\ker T_{z+w}}
$$
并且是有界双射。这就证明 (1.6)，特别像闭且有下界。

还可给直接的实参数预算。置
$$
L(\zeta)=\|Q(\zeta)\|+\sqrt2\,g.
$$
已构成的轨道 $f_t=e^{tK_0}f$ 局部解析，
$f_t\in\ker T_{z+t}$，且由 (2.6)
$$
\|f_t'\|=\|K_0f_t\|\le L(z+t)\|f_t\|.
$$
于是对 $t\ge0$，
$$
\boxed{
\|e^{tK_0}f\|
\le\exp\left(\int_0^t L(z+s)\,ds\right)\|f\|.
}
\tag{7.1}
$$
负参数沿反向线段用相同预算。
对 $s>0$，谱演算给
$$
\|e^{s|K_0|}f\|
\le\|e^{sK_0}f\|+\|e^{-sK_0}f\|,
\tag{7.2}
$$
从而得到 (1.5) 及紧参数一致界。

### 7.1 A(z) 的真实域保持与不变性

不能只由 $A(z)$ 整且有界推断它保持 $\mathcal D_0$。
固定 $f\in\mathcal D_0$，考虑整函数对
$$
\left(
 A(z)f,\ 
 A(z)T_zf-[Q(z)-Q(0)]A(z)f
\right).
$$
在虚轴上，R125 的原 $A$ 完整域交换与 (5.4) 给该对属于
$\operatorname{Graph}T_0$。用 §6.1 同一闭图全纯判据，得到全部 $z$ 上
$$
\boxed{
A(z)\mathcal D_0\subseteq\mathcal D_0,\qquad
T_zA(z)f=A(z)T_zf.
}
\tag{7.3}
$$
所以每个 $\ker T_z$ 对相应的 $A(z)$ 不变。这里不把 $A(z)$ 换回原来的 $A$。

## 8. 明确的实际点乘模型

由 (1.2) 逐位计算，
$$
UK_jU^*=M_{\chi_j},\qquad UH_0U^*=H_0.
$$
于是 $UK_0U^*=M_u$ 是最大自伴域上的等式，(1.5)—(1.7) 都是真正的点乘结论。
置
$$
\widetilde T_z=UT_zU^*,\qquad
\widetilde A(z)=UA(z)U^*.
$$
则
$$
\boxed{
M_{e^{wu}}:\ker\widetilde T_z
  \longrightarrow\ker\widetilde T_{z+w}
}
\tag{8.1}
$$
是实际全域有界双射，并有实际逆 $M_{e^{-wu}}$。

令 $R_j$ 是物理点的第 $j$ 位翻转，则在 Walsh 基底 $n_j=(I-R_j)/2$。
因此 $H_0$ 的准确闭实现是有限柱上
$\sum_j a_j(I-R_j)$ 的闭包，不使用发散的常数和。
点乘部分的变形可直接写成
$$
UZ(z)U^*
=\sum_j a_j\big(I-M_{e^{2za_j\chi_j}}\big)R_j.
\tag{8.2}
$$
此级数按算子范数绝对收敛，因为其第 $j$ 项不超过
$2|z|a_j^2e^{2|z|g}$。
式 (8.2) 正是
$$
M_{e^{zu}}R_jM_{e^{-zu}}
=M_{e^{2za_j\chi_j}}R_j
$$
的有限位比值。无界乘法只在 (8.1) 已付清的核域上使用。

## 9. 真实尾 Möbius 乘法域及闭核

取 $J$ 使 $\theta=\sup_{j\ge J}|a_j|<1$。令
$$
w_j=\operatorname{arctanh}(a_j)\quad(j\ge J),
$$
并定义绝对可和行
$$
d_j=
\begin{cases}
-a_j,&j<J,\\
w_j-a_j,&j\ge J.
\end{cases}
\tag{9.1}
$$
后半部满足 $|w_j-a_j|\le C_\theta|a_j|^3$，故 $d\in\ell^1$。
因此
$$
b(y)=\exp\left(\sum_jd_j\chi_j(y)\right)
\tag{9.2}
$$
是有界、正、处处有界逆的乘法符号。
同时
$$
c_J=\prod_{j\ge J}(1-a_j^2)^{1/2}
$$
收敛到严格正数。由
$e^{w_j\chi_j}=(1-a_j^2)^{-1/2}(1+a_j\chi_j)$，
实际几乎处处收敛的乘积为
$$
\boxed{
q_J=c_J\,b\,e^u,\qquad
q_J^{-1}=c_J^{-1}b^{-1}e^{-u}.
}
\tag{9.3}
$$
几乎处处收敛可由中心化 $\ell^2$ Rademacher 级数及绝对可和的余项直接得到。

式 (8.1) 与 $b^{\pm1}\in L^\infty$ 立即给
$$
q_J\widetilde M\subset H,\qquad
q_J^{-1}\widetilde M\subset H
$$
且两映射在 $\widetilde M$ 上有统一范数界。更准确地，
$$
\boxed{
q_J\widetilde M=c_J\,M_b\ker\widetilde T_1.
}
\tag{9.4}
$$
右侧闭；从该像返回 $\widetilde M$ 的实际逆是
$c_J^{-1}M_{e^{-u}}M_{b^{-1}}$，由 (8.1) 在准确的终点核上有界。
所以这里不只是逐向量可乘，而是闭像及有界逆。

### 9.1 有界修正 b 也支付完整闭域

$M_b$ 与 $M_u$ 交换。对 $H_0$，
$$
[H_0,M_b]
=\sum_j a_j M_{b-b\circ R_j}R_j
\tag{9.5}
$$
按算子范数绝对收敛，因为
$$
\|b-b\circ R_j\|_\infty
\le2\|b\|_\infty e^{2\|d\|_\infty}|d_j|,
\qquad
\sum_j|a_jd_j|<\infty.
$$
先仅取有限 Walsh 柱 $f,g$。此时 $H_{0,m}f,H_{0,m}g$ 均最终等于 $H_0f,H_0g$。对有限算子的交换子恒等式取弱极限，得到
$$
\langle bf,H_0g\rangle=\langle bH_0f+K_bf,g\rangle,
$$
其中 $K_b$ 为 (9.5) 的算子范数和。有限柱是 $H_0$ 的自伴图核心，故 $bf\in\operatorname{Dom}H_0$ 且 $H_0bf=bH_0f+K_bf$。再对任意 $f\in\operatorname{Dom}H_0$ 用 $P_mf$ 的 $H_0$ 图逼近和 $H_0$ 闭性延拓。对 $b^{-1}$ 相同。没有假定有符号行的 $H_{0,m}$ 在任意最大域输入上逐项收敛。因此两者双向保持
$$
\widetilde{\mathcal D}_0=U\mathcal D_0
=\operatorname{Dom}H_0\cap\operatorname{Dom}M_u.
$$

定义真正的闭算子
$$
\widetilde T^{\,q}
=M_b\,\widetilde T_1\,M_{b^{-1}},
\qquad
\operatorname{Dom}\widetilde T^{\,q}
=\widetilde{\mathcal D}_0.
\tag{9.6}
$$
常数 $c_J$ 不影响核，所以 (9.4) 给
$$
\boxed{\ker\widetilde T^{\,q}=q_J\widetilde M.}
\tag{9.7}
$$
它仍是 $H_0+iM_u$ 加一个明确的有界算子。
对应的有界
$$
\widetilde A^{\,q}=M_b\,\widetilde A(1)\,M_{b^{-1}}
$$
准幂零，并完整保持该域且与 $\widetilde T^{\,q}$ 交换。
Bell 分支也由同一个有界相似传递，字符不变。

对规范交替行可直接取 $J=1$，与最新 R236 已排除该 $M$ 的结论一致。上述尾乘法和逆域定理在一般实系数的可能非零核上仍有内容；没有把逐项 Möbius 系数公式当作原 $A$ 上的不变核恒等式。

## 10. 对当前主缺口的准确含义

本稿的正向输入是：原实际进位快到足以承受局部非酉指数共轭；
这种共轭仍产生准幂零的有界 $A(z)$ 和同一 Bell 解析分支。
核方程的纯分量图估计随后支付所有有限实参数的真正指数域，
最后给 $UM$ 上真实的指数及尾 Möbius 点乘。

尚未得到：

- 原空间 $M$ 本身的 $e^{su}$ 或 $q_J$ 点乘域；
- $U$、$e^{tK_0}$ 或 $q_J$ 保持原 $A$ 的不变子空间；
- 所有 $\ell^2$ first 方向同时的矩界，或全部 Walsh 次数指数矩；
- 新核与原核的参数改变能移动 R246 的活动碰撞根；
- 一般实系数闭分支的排核，以及把这些点乘运输与原 $A$ 的不变格对齐。

特别，$A(z)$ 及 $\widetilde A^{\,q}$ 是准确写出的新有界算子；
它们没有因谱都为 $\{0\}$ 就被当作原 $A$。
最新 R236 的对称高位平均已进一步证明规范交替行的全部 $\ker(X-\phi(B_2))=\{0\}$，并得到所有非零二次及以下 $q(u)$ 循环；此前 $N_r=M$ 与 $D_H=\{0\}$ 的接口亦已关闭。本稿的一般实系数域结论不以该规范排核为前提，也未将其自动扩到其他系数行。

## 已使用的仓库接口

- R125/R161：原 first 的共同有限柱图核心、实际闭实现和通常伴随。
- R130/R161：$\|V_j-(I-2E_j)\|\le8\eta_j$ 与真实链。
- R236 最新高位反射附录：当前中央闭像和逆域接口；本稿不依赖其结论来支付指数域。
- R257：局部解析思想的背景；本稿的自伴全参数运输在 §§2–9 独立支付。

壳层、准幂零和 Bell 整运输的核心已由 boundary 独立核对；
本稿完整核域证明另外写出，不以该局部核对代替其域论证。
