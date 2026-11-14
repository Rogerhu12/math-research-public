# R180：固定支撑的唯一 flat 提升、规范化单位矩阵与晶体迹

**状态：已证明。**

R176 保留完整的 $p$ 处局部型，所得后阶阻碍一般不为零。
本文把该条件放宽为固定行列式的有限平坦条件，并完整比较这两个问题。

在单素数支撑、$\gamma_q=0$、$\lambda_q\ne0$、
$v_p(q+1)=1$ 时，原首差类确实有**唯一的完整全局有限平坦提升**；
每一级都存在，不必另选素数。
这不构造椭圆曲线。该提升的晶体 Frobenius 迹是一个确定的
$t_q^\epsilon\in p^2\mathbf Z_p$，实际椭圆曲线要求它恰为零，
还须满足全局的有理整数迹与原始整数方程。

更一般地，本文用 $p$ 处 flat 切线规范化 R168 的 $q$-单位，
得到不受旧单位基变换影响的矩阵
$$
\widetilde C=C-\beta\gamma.
\tag{180.1}
$$
其非退化性给固定全部支撑的唯一完整 flat 提升判据。
本文不证明变化支撑上该矩阵总非退化，也不证明任何新 $t_q^\epsilon=0$。

## 1. 模、局部坐标与 flat 配对

沿用 R176：
$$
A:y^2=x^3-x,\qquad p>37,\quad p\equiv3\pmod4,
$$
$$
M=\operatorname{ad}^0A[p]=\mathbf F_p(\eta)J\oplus W,\qquad
\eta=\chi_{-4},
$$
$$
R=\{q_1,\ldots,q_r\},\qquad q_i\equiv-1\pmod{4p},\qquad
S=\{2,p,\infty\}\cup R.
\tag{180.2}
$$
这里 $R$ 是**整个允许的新增分歧支撑**，不是遗漏较深素数后的最小支撑。
所有 $q_i$ 的 Tate 惯性在 $p$ 深度开始，并固定其符号
$\epsilon_i\in\{1,-1\}$。令 $D_\epsilon=\operatorname{diag}(\epsilon_i)$。

在 $q_i$ 处使用 R168 的完整规范：
$$
F_i^2=1,\qquad J^2=-1,\qquad K_i=JF_i,
$$
primal $W$ 的有限、奇异坐标分别为 $a_iF_i,b_iK_i$；
dual $W(1)$ 的有限、奇异坐标分别为 $c_iK_i,d_iF_i$。
局部配对为
$$
\langle(a_i,b_i),(c_i,d_i)\rangle_{q_i}
=2(a_id_i-b_ic_i).
\tag{180.3}
$$
在 $p$ 处记固定 cyclotomic 行列式的 flat 切线为
$$
L_{\rm fl}\subset H^1(\mathbf Q_p,W),\qquad \dim L_{\rm fl}=1.
$$
第 2 节以真正的晶体迹坐标定义其生成元 $f$。

取 R163 的原始 Robert 生成元
$0\ne d_0\in\mathcal D_p$，以及 R168 的
$d_j\in\mathcal D_{p,R}$，其奇异坐标在 $q_j$ 为 $1$，
在其余 $q_i$ 为零。记
$$
\gamma_i=c_i(d_0),\qquad C_{ji}=c_i(d_j).
\tag{180.4}
$$
R161 最小 flat Selmer 及其对偶都为零。因此
$$
k=\langle f,\operatorname{loc}_p(d_0)\rangle_p\ne0.
\tag{180.5}
$$
确实，若该配对为零，则 $d_0$ 在 $p$ 落入 $L_{\rm fl}^{\perp}$，
在其余素数满足最小对偶条件，成为已知为零的最小 dual Selmer 类。

定义
$$
\beta_j=\frac{\langle f,\operatorname{loc}_p(d_j)\rangle_p}{k},
\qquad
\widetilde d_j=d_j-\beta_jd_0.
\tag{180.6}
$$
于是 $\widetilde d_j$ 的奇异坐标仍为第 $j$ 个标准向量，
而其 $p$ 定位与整个 $L_{\rm fl}$ 正交。
其有限坐标矩阵恰为 (180.1)。

若 $d_j$ 改为 $d_j+u_jd_0$，
则 $C$ 改为 $C+u\gamma$，$\beta$ 改为 $\beta+u$，
所以 $\widetilde C$ 不变。
若 $d_0$ 改乘非零标量，$\gamma,k$ 同时缩放，
$\beta$ 反向缩放，$\widetilde C$ 仍不变。
因此它在已固定的局部规范下是确定的；
没有将 R168 中可改变的原矩阵冒称规范数值。

## 2. 全有限层的 flat 函子与晶体迹坐标

R161 亲核的 Conrad Theorem 4.1.2(ii) 给出整个无框架变形函子的环
$$
R_p^{\rm fl,\det=\chi_p}\simeq\mathbf Z_p[[T]].
\tag{180.7}
$$
这里残余表示局部绝对不可约、底域为 $\mathbf Q_p$、
分歧指数 $1<p-1$；残余群及其 Cartier 对偶均连通。
定理适用于所有有限 Artin 系数环，不只适用于特征零点。

以下把抽象的 $T$ 换成有固定数学意义的参数。
对局部 Artin $\mathbf Z_p$-代数 $B$ 及 $t\in\mathfrak m_B$，
取 Fontaine–Laffaille 模
$$
\begin{aligned}
\mathscr M_t&=Be_1\oplus Be_2,\qquad
\operatorname{Fil}^1\mathscr M_t=Be_1,\\
\varphi_1(e_1)&=e_2,\qquad
\varphi_0(e_1)=p e_2,\qquad
\varphi_0(e_2)=-e_1+t e_2.
\end{aligned}
\tag{180.8}
$$
系数作用与所有映射交换。
$\varphi_0|_{\operatorname{Fil}^1}=p\varphi_1$，
两个 Frobenius 像生成全模，过滤为直接和因子。
这里须处理有限 Artin 系数的反变问题。
记 Fontaine–Laffaille 原文的反变函子为 $U$，采用的实现明确取为
$$
\mathbb T(\mathscr M_t)
=\operatorname{Hom}_{\mathbf Z_p}
  \bigl(U(\mathscr M_t),\mathbf Q_p/\mathbf Z_p\bigr)(1).
\tag{180.8a}
$$
即先取有限平坦群的 Cartier 对偶，再取泛纤维。
这是**协变、精确、$B$-线性**的函子，且像仍有限平坦。
不能直接把反变 $U(\mathscr M_t)$ 的自然 $B$ 作用当作自由 $B^2$：
对非 Gorenstein 的 $B$，那一步一般不成立。

协变实现的自由性可完整核算。对任一理想 $I\subset B$，
用 $I$ 的有限生成元写出乘法映射
$\mathscr M_t^{\oplus s}\to\mathscr M_t$；
其余核为 $\mathscr M_t/I\mathscr M_t$，过滤逐项直接取商。
精确性给
$$
\mathbb T(\mathscr M_t)/I\mathbb T(\mathscr M_t)
\simeq\mathbb T(\mathscr M_t/I\mathscr M_t).
$$
同样用有限表示处理任意 Artin 系数基变换。
取 $I=\mathfrak m_B$，右端为 $A[p]$，故剩余维数为 $2$。
Fontaine–Laffaille Theorem 3.3 的长度公式及 Pontryagin 对偶保持长度给
$$
\operatorname{length}_{\mathbf Z_p}\mathbb T(\mathscr M_t)
=\operatorname{length}_{\mathbf Z_p}\mathscr M_t
=2\operatorname{length}_{\mathbf Z_p}B.
$$
Nakayama 引理给 $B^2\twoheadrightarrow\mathbb T(\mathscr M_t)$；
两边长度相同，遂为同构。
因此得到的确是自由秩 $2$ 的 $B$-表示，
而不是仅同阶的有限 $\mathbf Z_p$-模。

行列式的规范也可以不借用未经证明的任意系数外积断言。
先对任意 $t\in p\mathbf Z_p$ 取整族。
对原反变实现，过滤外积满足
$$
\varphi_1(e_1)\wedge\varphi_0(e_2)=e_1\wedge e_2.
\tag{180.9}
$$
原刊 §6.13(b)（正文页 589）的张量兼容性适用于此处：
两个权 $0,1$ 对象的张量权不超过 $2<p-1$；
$p$ 奇，反对称投影 $\frac12(1-\mathrm{swap})$ 给外积。
整格的版本由 Proposition 7.15 及有限层取极限得到。
所以反变实现的行列式与 $t=0$ 时相同，即 $\chi_p$。
协变实现取对偶并扭曲一次，秩为 $2$，其行列式为
$\chi_p^{-1}\chi_p^2=\chi_p$。

基变换先给一条 $\mathbf Z_p[[t]]$ 上的 full flat 族。
对每个 Galois 元素，其行列式减去 $\chi_p$ 是整系数形式幂级数，
在全部 $t\in p\mathbf Z_p$ 为零，因此恒为零。
例如若存在首个非零系数，代入充分高的 $p$ 次幂，
其项的赋值严格小于所有后项，便不能为零。
这证明整个形式族、因而任意 Artin 系数特化的行列式准确固定，
没有假设非 Gorenstein 系数上的反变外积可直接交换。

$A$ 的原整 Fontaine–Laffaille 对象在上述基中的 Frobenius 矩阵为
$$
\begin{pmatrix}0&-1\\p&0\end{pmatrix};
$$
R157 的反变晶体规范和稳定格唯一性已将该对象与 $T_p(A)$ 对齐。
协变实现的 $t=0$ 点为 $T_p(A)^\vee(1)$，
通过 $A$ 的 Weil 配对与同一个 $T_p(A)$ 对齐。

取 $B=\mathbf F_p[\varepsilon]/(\varepsilon^2)$、
$t=\varepsilon$ 时，(180.8) 非平凡：
同构保持 $\operatorname{Fil}^1$，故 $e_1$ 只可改乘单位，
$\varphi_1(e_1)=e_2$ 随即迫 $e_2$ 改乘同一个单位；
$\varphi_0(e_2)$ 的系数 $t$ 因而不能消去。
协变实现仍完全忠实，故此切方向仍非零；其切类定义为
$$
f=\left.\frac{\partial\mathscr M_t}{\partial t}\right|_{t=0}
\in L_{\rm fl}.
\tag{180.10}
$$

这还证明 (180.8) 是整个通用 flat 族。
将 (180.7) 的坐标平移，使 $A$ 点为 $T=0$。
族 (180.8) 给环映射
$\mathbf Z_p[[T]]\to\mathbf Z_p[[t]]$；
$T$ 的像常数项为零，线性系数为单位，
因为 (180.10) 是非零切方向。
形式幂级数的逆函数因此给出环同构。
这个论证排除了“只构造了一条非零一阶方向”与“已经获得全部高层点”
之间的缺口。

对 $\mathbf Z_p$ 点，采用 R157 的反变晶体规范，
原对象的矩阵为 $\Phi_t$；Cartier 对偶实现的矩阵为
$p\Phi_t^{-\mathsf t}$。具体为
$$
\Phi_t=\begin{pmatrix}0&-1\\p&t\end{pmatrix},\qquad
p\Phi_t^{-\mathsf t}=\begin{pmatrix}t&-p\\1&0\end{pmatrix},\qquad
\det(X-\Phi_t)=\det(X-p\Phi_t^{-\mathsf t})=X^2-tX+p.
\tag{180.11}
$$
两矩阵由固定交替矩阵整共轭，迹均为 $t$。
对真实椭圆曲线的 Tate 模，这个 $t$ 就是 $a_p(E)$。
在自由秩 $2$、固定行列式的点上，
$\chi_p\rho^{-\mathsf t}=J_0\rho J_0^{-1}$，
$J_0=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$；
以 $t=0$ 的 Weil 对齐归一化后，这也说明切线 (180.10)
与 R161 使用的是同一个方向，不产生额外反号。

现在给定任意模 $p^m$ flat 表示。
它对应唯一的 $t_m\in p(\mathbf Z/p^m)$，
其下一层 flat 提升恰由
$$
t_{m+1}=\widetilde t_m+p^m u,\qquad u\in\mathbf F_p
\tag{180.12}
$$
给出。任意两次提升之差，均为同一残余方向 $u f$。
这一结论对每个 $m$ 成立，不能仅由特殊点的切空间维数推断，
而是使用了完整的通用环。

局部残余绝对不可约使
$\operatorname{End}_{G_{\mathbf Q_p}}(\rho_m)=\mathbf Z/p^m$：
逐级减标量、除以 $p$ 即可。
所以没有另一个非标量局部自同构商改变 (180.12)。

## 3. 首层所有 flat 类的准确参数化

令 $H_R^{\rm fl}(W)$ 为在 $p$ 取 $L_{\rm fl}$、
在 $2$ 取零、在 $R$ 取整个局部 $H^1$、
在其余素数取不分歧条件的全局空间。
R161 最小 primal 与 dual flat Selmer 都为零。
把 $R$ 的条件从不分歧放宽为整个 $H^1$，
Poitou–Tate 比较遂给同构
$$
H_R^{\rm fl}(W)\xrightarrow{\sim}
\bigoplus_{i=1}^r H^1_{\rm sing}(\mathbf Q_{q_i},W)
=\mathbf F_p^r.
\tag{180.13}
$$
因此每个奇异向量 $b$ 有唯一一个全局 flat 类 $w_b$。

写
$$
\operatorname{loc}_p(w_b)=s f,\qquad
a=(a_i).
$$
与 $d_0$ 的全局互反及 (180.3) 给
$$
k s-2\gamma b=0.
\tag{180.14}
$$
与 $\widetilde d_j$ 的全局互反中，$p$ 项为零，
$q_i$ 项之和为
$2(a_j-\sum_i\widetilde C_{ji}b_i)$。所以
$$
\boxed{\quad
a=\widetilde C b,\qquad
s=\frac{2}{k}\gamma b.
\quad}
\tag{180.15}
$$
因子 $2$ 来自 R168 的迹配对，未被并入 $\gamma$ 或 $k$。

$\eta J$ 分量在 $p$ 的 flat 条件为零。
其全局类由 $R$ 奇异向量 $x\in\mathbf F_p^r$ 唯一确定：
$\mathbf Q(i)$ 类数为 $1$，每个惰性射线素数给一个独立的
反循环 $p$ 角色，单位的阶与 $p$ 互素。
$p$ 处不分歧类为零，因为 $\eta(\operatorname{Frob}_p)=-1$。
$2$ 处整个伴随 $H^1$ 为零。

合并两项，固定 $p$ flat、其余非 $R$ 局部型的首差类由 $(x,b)$ 唯一确定。
它在 $p$ 的晶体迹满足
$$
\frac{t}{p}\equiv s=\frac{2}{k}\gamma b\pmod p,
\tag{180.16}
$$
其中 $t$ 是局部模 $p^2$ 参数。

## 4. 完整 Tate 首类的可解判据

令
$$
z_i=\frac{q_i+1}{2p}\pmod p,\qquad z=(z_i).
\tag{180.17}
$$
R176 的完整局部 Tate 模型说明，惯性深度 $1$、符号 $\epsilon_i$
在首差处准确要求
$$
b_i=\epsilon_i x_i,\qquad a_i=\epsilon_i z_i,\qquad x_i\ne0.
\tag{180.18}
$$
这包括 Frobenius 的有限坐标，不只要求非零幂零惯性。
反过来，(180.18) 由 R176 的整局部模型实现，
所以它对给定模 $p^2$ 首类也是充分的。

若 $\widetilde C$ 可逆，唯一可能的解为
$$
\boxed{\quad
b=\widetilde C^{-1}D_\epsilon z,\qquad
x=D_\epsilon\widetilde C^{-1}D_\epsilon z.
\quad}
\tag{180.19}
$$
若其中每个 $x_i\ne0$，(180.13) 及 $\eta$ 角色构造
给唯一全局首类 $c\in H^1(G_{\mathbf Q,S},M)$。
表示
$$
\rho_2(g)=(1+p c(g))\rho_A(g)\pmod{p^2}
\tag{180.20}
$$
具有固定 cyclotomic 行列式、$p$ 处 flat、$2$ 处指定型，
并与每个指定整 Tate 型的模 $p^2$ 约化同构。
改变 cocycle 代表只改变严格共轭类。

因此此时首层不是一个待检验的存在性假设。
它确由规范化单位矩阵构造。
但实际椭圆曲线还要求 $p$ 的首局部型已经与 $A$ 相同，即
$$
\gamma\widetilde C^{-1}D_\epsilon z=0.
\tag{180.21}
$$
若某个 $x_i=0$，则该构造不在全部支撑深度 $1$ 的分支；
不能直接用后面的全阶定理。

## 5. 每一级 fixed-Tate + flat 问题的核与余核

设 $m\ge2$，$\rho_m$ 已满足全部指定 Tate 型、$2$ 处指定型及 $p$ flat。
R176 的全局计算仍适用：
$$
H^2(G_{\mathbf Q,S},M)\xrightarrow{\sim}
\bigoplus_{q\in R}H^2(\mathbf Q_q,M),\qquad
\dim H^1(G_{\mathbf Q,S},M)=2r+2.
\tag{180.22}
$$
$p$ flat 函子由 (180.12) 形式光滑，各 $q$ 来自固定整 Tate 模型，
$2$ 来自 $A$，故普通全局提升障碍的全部局部定位为零。
所以普通固定行列式的下一层总存在。

恢复全部局部条件时：
$p$ 的比较子空间为 $L_{\rm fl}$；
每个 $q_i$ 的比较子空间为
$$
L_{q_i}=\mathbf F_p(J+\epsilon_iK_i)
$$
的纯奇异线。
后者对所有 $m\ge2$ 成立，因为完整 Tate Frobenius 的两根之差为单位，
模 $p^m$ 自同构必须对角；
与深度为 $1$ 的惯性交换再迫两对角项之差被 $p^{m-1}$ 整除。
除标量后正是 $1+p^{m-1}uF_i$，
下一层仅改变上述奇异线。

令
$$
\mathcal V_{\rm fl}
=H^1(\mathbf Q_p,M)/L_{\rm fl}\ \oplus\
\bigoplus_iH^1(\mathbf Q_{q_i},M)/L_{q_i}.
\tag{180.23}
$$
其维数为 $2+2r$。
普通全局提升的局部偏差给
$$
\operatorname{Obs}^{\rm fl}_m(\rho_m)\in
\operatorname{coker}
\bigl(H^1(G_{\mathbf Q,S},M)\to\mathcal V_{\rm fl}\bigr).
\tag{180.24}
$$

精确求此余核。
R176 的 $H^1(G_{\mathbf Q,S},\eta(1))=0$ 仍成立，
所以全局对偶类只在
$\mathcal D_{p,R}=\langle d_0,d_1,\ldots,d_r\rangle$ 中。
写成 $t_0d_0+\sum_jv_jd_j$。
在 $p$ 与 flat 线正交，准确等价于
$$
t_0+\beta^{\mathsf t}v=0.
$$
在每个 $q_i$ 与 $L_{q_i}$ 正交，准确等价于有限 $W(1)$ 坐标为零。
消去 $t_0$，得到
$$
\gamma^{\mathsf t}t_0+C^{\mathsf t}v
=\widetilde C^{\mathsf t}v=0.
$$
所以
$$
\boxed{\quad
\operatorname{coker}(\operatorname{res}_{\rm fl})^\vee
\simeq\ker(\widetilde C^{\mathsf t}).
\quad}
\tag{180.25}
$$
两个相同维数 $2r+2$ 的空间之间的线性映射，
其核与余核等维。因此
$$
\boxed{\quad
\dim\ker(\operatorname{res}_{\rm fl})
=\dim\operatorname{coker}(\operatorname{res}_{\rm fl})
=\dim\ker\widetilde C.
\quad}
\tag{180.26}
$$
也可直接用 (180.15)：差异类落在全部 $L_{q_i}$，
要求 $b=D_\epsilon x$、$\widetilde Cb=0$，
同样得到核的维数。

这是真正针对已给 $\rho_m$ 的小扩张比较。
$p$ 处全函子及 $q$ 处模 $p^m$ 中心化子都已逐项核对，
故没有把残余特殊点的切空间机械地当成所有高层比较空间。

## 6. 唯一的完整全局 flat 表示

**定理 180.1。**
假设 (180.2) 且 $\widetilde C$ 可逆。
对每个满足 (180.19) 各 $x_i$ 非零条件的指定符号向量 $\epsilon$，
存在唯一严格共轭类的连续表示
$$
\rho_{R,\epsilon}:G_{\mathbf Q,S}\longrightarrow
\operatorname{GL}_2(\mathbf Z_p)
\tag{180.27}
$$
满足：

- 残余为 $A[p]$，行列式为 $\chi_p$；
- 在 $p$ 有限平坦，在 $2$ 与 $T_p(A)$ 同构；
- 每个 $q_i$ 与指定符号、深度为 $1$ 的整 Tate 模型同构；
- 首类为 (180.19)–(180.20)。

**证明。**
第 4 节构造唯一 $\rho_2$。
$\widetilde C$ 可逆使 (180.25) 的余核为零，
故每一级普通全局提升都能调整为所需局部型。
(180.26) 的核也为零，故下一层严格共轭类唯一。
逐级选择相容的矩阵代表并取逆极限。
局部同构的集合为非空紧致集合，逐级限制给嵌套条件，
紧致性保证极限仍有指定局部型。
$p$ 的局部参数也相容，由 (180.7) 给真正的整 flat 表示。
全局残余绝对不可约，故各层全局自同构只有标量，
没有遗漏另一个非标量稳定子。证毕。

不同 Tate 参数的单位 $\mu$ 没有给定理增加参数：
深度同为 $1$ 时，整对角单位基变换可以缩放非零幂零矩阵，
把任意两个 $p\mu$ 模型互相识别。
Weil 配对乘数仍对实际曲线给必要条件，
但这里分类的是 $\operatorname{GL}_2$ 表示，不是指定乘数的辛表示。

定理中的 “flat” 不能换成“来自一条椭圆曲线”。
它保证局部有限平坦群及完整全局表示，并不保证所有好素数迹为有理整数，
也没有给出实际曲线的全局 Weierstrass 模型。

## 7. 一个确定的晶体迹与 R176 的全部后阶阻碍

令 $t_{R,\epsilon}\in p\mathbf Z_p$ 为
$\rho_{R,\epsilon}|_{G_{\mathbf Q_p}}$ 的参数 (180.11)。
它由完整表示唯一确定，并满足
$$
\boxed{\quad
\frac{t_{R,\epsilon}}p
\equiv\frac2k\gamma\widetilde C^{-1}D_\epsilon z\pmod p.
\quad}
\tag{180.28}
$$

假设 (180.21) 成立，则 $t_{R,\epsilon}\in p^2\mathbf Z_p$。
对每个 $m\ge2$，
唯一 flat 塔在第 $m$ 层满足 R176 的完整 $p$ 型，当且仅当
$$
t_{R,\epsilon}\equiv0\pmod{p^m}.
\tag{180.29}
$$
这是通用参数的等价，不是仅比较两个特征零 Frobenius 多项式。

特别地，当 $r=1,\gamma_q=0,\lambda_q\ne0$、
$v_p(q+1)=1$ 时，
$\widetilde C=C=(\lambda_q)$，(180.19) 给
$$
x_q=\frac{q+1}{2p\lambda_q}\ne0,\qquad
b_q=\epsilon x_q,\qquad
t_q^\epsilon\in p^2\mathbf Z_p.
\tag{180.30}
$$
完整 flat 塔总存在。
若前面已满足 $t_q^\epsilon\equiv0\bmod p^m$，
取该唯一 flat 下一层作 R176 的普通全局提升，
其在 $p$ 与固定 $A$ 型的偏差是
$$
z_{p,m}=
\left(\frac{t_q^\epsilon}{p^m}\bmod p\right)f.
$$
因此在与 R176 相同的“提升减去固定型”规范下，
$$
\boxed{\quad
\Omega_m=
k\left(\frac{t_q^\epsilon}{p^m}\bmod p\right).
\quad}
\tag{180.31}
$$
$k\ne0$。若反向定义偏差，等式两侧同时反号，零性不变。

所以这些后阶标量不是分别可选的一串独立参数：
它们是同一个确定晶体迹的逐位检测。
若 $v_p(t_q^\epsilon)=\nu<\infty$，
固定 $A$ 型的塔准确存在到模 $p^\nu$，
并在下一层被 $\Omega_\nu\ne0$ 阻断。
若 $t_q^\epsilon=0$，全部这些固定局部型阻碍消失。
本文未计算这个完整 $p$ 进数，也未证明其为零或非零。

对任意符号向量，二次自扭曲给一个进一步相容性。
$J$ 实现 $A\otimes\eta\simeq A$，
故
$$
\rho\longmapsto \eta\,J\rho J^{-1}
$$
仍残余于同一个 $A[p]$。
它把所有惰性 $q_i$ 的符号同时反转；
在首差上保持 $\eta J$ 分量，把 $W$ 分量反号。
在 $p$，$\eta$ 是未分歧二次角色，
将 (180.8) 的 Frobenius 同时反号后改基 $e_2'=-e_2$，
得到参数 $-t$。
由全局唯一性，
$$
\boxed{\quad t_{R,-\epsilon}=-t_{R,\epsilon}.\quad}
\tag{180.32}
$$
因此两种整体符号并不给独立的零性条件。

## 8. R171 实例的真正整表示与椭圆曲线边界

R171 的已证素数 $q$ 和 $p=43$ 满足
$$
\gamma_q=0,\qquad \lambda_q=16,\qquad
v_{43}(q+1)=1,\qquad (q+1)/43\equiv11\pmod{43}.
$$
所以 (180.30) 给 $x_q=-1$。
定理 180.1 在这个**同一个**素数上，
对两种符号各构造一个真正完整的 $\mathbf Z_{43}$ 表示。
这不再只是模 $43^2$ 或任意固定有限层的存在性。

但它们都不是椭圆曲线的 Tate 模。
以下只重用 R171 已验证的 Gaussian $5$ 符号，
不进行任何新的素数搜索。

取 primary $\beta_5=-1+2i$，$N\beta_5=5$。
R171 的
$\beta_5^{(q^2-1)/43}\ne1$
说明该素理想在唯一非零的反循环射线 $43$ 角色 $\kappa$ 上非零。
这里 $\kappa$ 的 tame 系数为 $x_q=-1$，
故不是可重新选成零的角色。
Frobenius 的 CM 矩阵是 $-1+2J$；
$W$ 与 Cartan 在迹配对下正交，因而
$$
\operatorname{tr}\rho_{q,\epsilon}(\operatorname{Frob}_5)
\equiv-2-4\cdot43\,\kappa(\operatorname{Frob}_{\beta_5})
\not\equiv-2\pmod{43^2}.
\tag{180.33}
$$
另一方面其模 $43$ 的迹为 $-2$。

若来自椭圆曲线，由 $5$ 处表示不分歧及 Néron–Ogg–Shafarevich，
曲线在 $5$ 好约化。
其有理整数迹满足 $|a_5|\le2\sqrt5<5$；
该区间中模 $43$ 同余于 $-2$ 的唯一整数为 $-2$，
与 (180.33) 矛盾。

这里没有调用模性提升定理。
若另外将此表示识别为某个权 $2$、平凡特征的新形式表示，
还可得一个精确的条件性系数域结论：
令 $a_5$ 为其特征值，$d=[\mathbf Q(a_5):\mathbf Q]$。
$a_5+2$ 是非零代数整数，
指定的 $43$ 进嵌入使 $43$ 整除其范数。
各复共轭满足权 $2$ 的 Weil 界，故
$$
43\le\left|N_{\mathbf Q(a_5)/\mathbf Q}(a_5+2)\right|
\le(2+2\sqrt5)^d.
$$
由于 $(2+2\sqrt5)^2=24+8\sqrt5<42<43$，必有 $d\ge3$。
这是“若有该模形式识别”的推论，
本文不靠未核对的模性提升假设宣布已经取得新形式。

## 9. 与主目标的准确关系

本结果把一个实际未解决的后阶问题收缩为更具体的量：

- $q$-单位基的任意性被 $p$ 的 flat 线消去，形成 $\widetilde C$；
- 在其可逆、全部惯性深度为 $1$ 的分支，
  同一个支撑上真正的完整 flat 表示总存在且唯一；
- 实际曲线要求该表示的晶体迹为零，
  并满足所有有理整数迹、全局 Weil 乘数及 R19 原始整数族。

最后一项不能从 flat 提升的存在性推出。
R171 已给出一个完整 flat 表示存在、但有理整数迹条件失败的明确实例。
即使某个新的 $t_{R,\epsilon}=0$，仍不能省略实际椭圆曲线的全局实现条件。

变化支撑上，$\widetilde C$ 的非退化性尚未统一证明；
若较深惯性素数后面才出现，必须扩大支撑、重算矩阵及比较问题。
本文不把固定支撑定理变成对所有分母的统一排除。

## 10. 来源定位

- R114 §2.2：$2$ 处完整局部型；R157 §2：反变晶体规范、
  整格唯一性及实际有限层的对齐。
- R161 §§2–3：准确的 fixed-determinant flat 函子、
  其 $W$ 切线、最小 primal/dual Selmer 均为零。
- R163：原始 Robert 生成元；R168：完整局部配对、
  单位行、$q$-单位矩阵及 Tate 非齐次式；
  R171：本篇 §8 的全部有限证书；R176：普通 $H^2$、
  全 $m$ Tate 中心化子与固定局部型比较。
- B. Conrad，Ramified deformation problems，
  Duke Math. J. 97 (1999), 439–513，
  Theorem 4.1.2(ii)；
  [作者全文](https://math.stanford.edu/~conrad/papers/ramdef.pdf)，
  作者页 30（PDF 页 30）。
  本文使用完整环 $\mathcal O[[T]]$，
  而不是只引用一维切空间。
- J.-M. Fontaine、G. Laffaille，Construction de représentations $p$-adiques，
  Ann. Sci. ÉNS (4) 15 (1982), 547–608，
  Theorem 3.3、Theorem 6.1、§6.13(b)（正文页 589）、
  Proposition 7.15、§9.11、Proposition 9.12；
  [原刊全文](https://www.numdam.org/item/ASENS_1982_4_15_4_547_0.pdf)。
  权 $0,1$ 的完全忠实性、有限平坦对应、长度公式和所述张量兼容
  负责 (180.8)–(180.9) 的实际表示解释。
  一般 Artin 系数明确采用协变 Cartier 对偶实现并逐项证明自由性；
  通用性另由 (180.7)
  和已证明的非零切映射推出。

