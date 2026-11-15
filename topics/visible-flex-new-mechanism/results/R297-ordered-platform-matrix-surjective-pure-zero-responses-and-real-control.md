# R297：有序平台三矩矩阵的九个 pure-zero 响应与真实有限支付

日期：2026-11-15。**完整纸面证明；未执行新的原式展开程序、profile 求积、秩计算、人工检查或科学运行。** 本文只读取已发表的完整原式，手写微分及同右锚分部积分。

采用 [R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md) 的真实有序平台矩阵。本文证明：它的全部九个坐标在完整 pure-zero 响应上已经满射，并由 R222 的一般有限观测定理取得真正的有限路径控制。因而可在同一个真实闭 hook 上同时要求整 universal pure 为零以及整个三矩矩阵为任意指定实矩阵，特别可以全零。

这不是把九个几何 history 参数当作独立变量，也不是从有符号线性 span 直接宣布存在负成本。真实结论保留 prototype、整 pure 校正的 mixed 基准、有限重复、frame/scalar 端口和 Klein 位移闭合。它不自动保持某个预先指定的 Gaussian 共振 germ、Morse 性、单包自项、其他已选观测或完整 period/ruling。

## 1. 三矩矩阵及本稿结论的准确对象

令 U 为原 canonical 完整第四成本空间，$\mathcal R$ 为真实响应空间，$\pi$ 为 universal pure 投影，记

$$
U_{\mathrm p0}=U\cap\ker\pi,\qquad
\mathcal R_{\mathrm p0}=\mathcal R\cap\ker\pi.
\tag{1}
$$

第三 period 另记为 $\mathbf T_B$，以免与本稿的三矩型 $\mathcal T_B$ 混淆。

对于一个真实周期几何 B，保 R73 的实际第二 history

$$
m(s)=\int_{s_0}^s M(t)\,dt,\qquad
m(s_0)=m(L)=0.
\tag{2}
$$

对 $\mu=(\mu_0,\mu_1,\mu_2)^{\mathsf T}$，R292§3 定义原二阶左尾量

$$
p_\mu=\frac{(1+d^2)\mu_0+2hd\mu_1+h^2\mu_2}{8h},
\qquad d=h\omega-k,
$$

$$
W_\mu=\mathfrak a_\mu x^2+\mathfrak b_\mu x+\mathfrak c_\mu,
\qquad
t_\mu=\frac{\mathfrak b_\mu}{2}-\omega\mathfrak a_\mu
-\frac{(p_\mu)_s}{2h},
$$

$$
\eta_\mu=-ht_\mu-k\mathfrak a_\mu-(p_\mu)_s,\qquad
q_\mu=-kt_\mu-h(\mathfrak c_\mu-\omega\mathfrak b_\mu+\omega^2\mathfrak a_\mu),
$$

$$
\tau_\mu=(t_\mu)_s-\frac{h_s}{h}t_\mu.
\tag{3}
$$

其中 $W_\mu$ 由同一个实际 m 决定，不能另设其系数或初值。本文采用的有序型是

$$
\boxed{
\mathcal T_B(\mu,\nu)
=-\frac14\int_B
\left[
t_\mu t_\nu+\tau_\mu\tau_\nu+
\frac{k}{h}(\mathfrak a_\mu t_\nu+\eta_\mu q_\nu)
\right]ds.
}
\tag{4}
$$

以列向量约定写成 $\mathcal T_B(\mu,\nu)=\mu^{\mathsf T}\mathsf T_B\nu$。

当 B 满足 R292 的实际 $M_B=0$、$\mathbf T_B=\kappa\mathfrak H$、整 pure 零条件时，(4) 正是两个不同紧微包 $u_i$ 在 $u_j$ 左方时，其真实第四交叉 period 的左二次系数。它与各单包的真实自 history $q_i$ 不是同一数据。

本文的核心是构造九条完整真实响应 $\mathcal K_{ij}\in\mathcal R_{\mathrm p0}$，$0\le i,j\le2$，使

$$
\boxed{
\mathsf T(\mathcal K_{ij})=\mathsf e_{ij},
}
\tag{5}
$$

其中 $\mathsf e_{ij}$ 是普通 $3\times3$ 矩阵单位。第 2 节给 $\mathsf T$ 在整个 U 上的准确原函数查询定义；第 6 节再由既有真实控制定理支付指定的矩阵值。

## 2. 从真正跨包原函数定义线性观测，不另赋 history

### 2.1 原相位两参数的交叉系数

在共同合法 profile 区间 I 中取两个紧 profiles u、v，且 u 的整个支撑严格位于 v 左方。所有输入在同一个右 collar 为零；左尾保留。暂把两个实幅度记为 a、b，考虑原 universal 成本

$$
V(a^2u^2,bv).
$$

这里第一槽是原种子平方 F，第二槽是原 $\phi$。这是原函数的合法代数查询，不把这两个测试包自身宣称为已经满足全圆三矩/ruling 的一个新第一圆。

记 $\mathscr P$ 为原周期恢复。由原完整第四式，

$$
V=-\mathscr P H(Z_D,Z_D)
+4\mathscr P H(Y_\phi,C(\phi;D)),
\qquad D=F-\phi^2.
\tag{6}
$$

因为 v 在 u 右方，而 $Z_{u^2}$ 在 u 右方整个为零，所以

$$
C(v;u^2)=0
\tag{7}
$$

是原场的完整身份，不仅是一个 period 值。于是 (6) 的准确幅度系数为

$$
\boxed{
[a^2b^2]\,V(a^2u^2,bv)
=2\mathscr P H(Z_{u^2},Z_{v^2}).
}
\tag{8}
$$

没有删去 $Z_{v^2}$ 在 u 包内的真实仿射左尾，也没有重锚任何积分。

在共同左 collar，右边是次数至多二的多项式。R292(30)–(31) 对同一有序两包给

$$
[x^2]\mathscr P H(Z_{u^2},Z_{v^2})
=\frac12\int
\left[
\frac{\nabla_sU_u\cdot\nabla_sU_v}{h^2}
+\frac{k}{h}U_u\cdot(V_v-\omega U_v)
\right]ds.
$$

使用其原 $\nabla_sU_\mu=(0,-ht_\mu,h\tau_\mu)$，立即有

$$
\boxed{
-\frac14[x^2]_{\rm left}[a^2b^2]\,
V(a^2u^2,bv)
=\mathcal T_B(\mu(u),\mu(v)),
}
\tag{9}
$$

其中

$$
\mu(u)=\left(
\int(u'')^2,\ 
\int x(u'')^2,\ 
\int[x^2(u'')^2+2(u')^2]
\right)^{\mathsf T}.
\tag{10}
$$

推 (8)–(9) 不需要先用 pure 零身份。R292 的 whole-pure 身份用于再把该量认成有序 $Q_{ij}$ 的系数及推平台递推；此处直接保留了真实 $Z$–$Z$ 项。

### 2.2 全 U 的九个原查询

U 由实际 $M=\mathbf T=0$ 成本线性张成。对每个这样的生成元，(9) 都成立；所有输入、输出右锚及其原函数定义相同。因此按成本线性延拓，得到唯一线性映射

$$
\boxed{\mathsf T:U\longrightarrow\operatorname{Mat}_3(\mathbb R).}
\tag{11}
$$

下面也给一个有限原查询的明确承载，避免把“有限维”当成任意独立赋值。

在一个小左包络内，选同宽、三个不同中心的同一非零偶 bump；它们的三矩列向量为正因子乘

$$
(1,c_i,c_i^2+\nu_*w^2)^{\mathsf T}.
$$

三列行列式是非零 Vandermonde 因子。右侧另一个不交包络也如此选三条 v。把 (9) 在这九对真实测试输入上评价，再左右乘这两个已固定三矩矩阵的逆，就准确恢复 (11) 的九坐标。

幅度系数是有限次原函数评价的线性组合；共同左二次尾的 $x^2$ 系数也是三个固定 collar 查询值的线性组合。故 (11) 由有限个真实 profile/输出评价承载。没有把某个 Volterra 尾值或 $\mu$ 分量当成自由几何参数，没有新的采样或求秩。

如果一个 U 元素有两种真实成本分解，其原函数差为零，则九个查询差为零，矩阵也为零。因此 (11) 不依赖所选成本分解。对原 R292 实际闭 hook，(11) 的值正好是 (4)，并非另造的形式矩阵。

## 3. 三个已发表局部系数的完整矩身份

[R254](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md) 已给完整第三对角核

$$
Z=\ker\Delta,\qquad \Delta\tau(q)=\tau(q;q,q)
$$

以及原 $\chi_{32},\chi_{37},\chi_{40}\in Z$。其索引按原 W 的完整 retained 序列，不是新形式标签。

对 $\tau\in Z$，记

$$
K_f^\tau(w)=\tau(w;f,f),\qquad
D^3K_f^\tau(w)=\mathscr A_{\tau,f}w,
$$

$$
\mathscr A_{\tau,f}=D^2(a_{\tau,f}D^2)+D(b_{\tau,f}D)+c_{\tau,f}.
\tag{12}
$$

R261 已证明完整局部自伴性、$\mathscr A_{\tau,f}f=0$ 和真实右三常数。本文不重新生成这些算子或重算旧对角差。

令 $p=u'$、$r=u''$。直接把 R261§3 的三个原 $c$ 多项式按乘法求导重组，得到以下可逐项手核的局部身份：

$$
\boxed{
256c_{32,u}
=2D^2(r^2)-D^3(2pr+3xr^2),
}
\tag{13}
$$

$$
\boxed{
256c_{37,u}
=-4D^2(xr^2)
+D^3(4p^2-16xpr+18x^2r^2),
}
\tag{14}
$$

$$
\boxed{
256c_{40,u}
=2D^2(x^2r^2+2p^2)
+D^3(-4xp^2+8x^2pr-6x^3r^2).
}
\tag{15}
$$

例如 $D^3(pr)=3(r')^2+4rr''+pr'''$、
$D^3(xr^2)=6(r')^2+6rr''+x(6r'r''+2rr''')$；
将其代入 (13)，正好恢复
$-2pr'''-22rr''-20(r')^2-6xrr'''-18xr'r''$。
(14)、(15) 同样只用乘法法则，保全部显式 x 与 profile jets。

u 是真实双端紧包，故 (13)–(15) 的原局部抗导及相关端 jets 在包端全零。对任意二次多项式 P，三次导数部分经过三次分部积分准确为零，二次导数部分给 $P''$ 乘原密度积分。因此

$$
\begin{array}{c|ccc}
 &\displaystyle\int c_{\tau,u}
 &\displaystyle\int x c_{\tau,u}
 &\displaystyle\int x^2c_{\tau,u}\\ \hline
\chi_{32}&0&0&\mu_0(u)/64\\
\chi_{37}&0&0&-\mu_1(u)/32\\
\chi_{40}&0&0&\mu_2(u)/64
\end{array}.
\tag{16}
$$

这里第三个矩完整包含 $2(u')^2$。若将它删掉，(15) 及下文的第三行都会错误。

规范化三个真实第三方向：

$$
\sigma_0=64\chi_{32},\qquad
\sigma_1=-32\chi_{37},\qquad
\sigma_2=64\chi_{40}.
\tag{17}
$$

则三式统一为

$$
\boxed{
\int c_{\sigma_i,u}(x)P(x)\,dx
=[x^2]P\ \mu_i(u),
\qquad 0\le i\le2,\quad \deg P\le2.
}
\tag{18}
$$

这是原函数的准确矩身份，不是对若干选定 profile 的有限数值拟合。

## 4. 完整响应给全部九个矩阵单位

### 4.1 两条真实右积分与第三 history

对任意 $\tau\in Z$，R255(31) 的完整响应为

$$
\boxed{
\mathcal B_A(\tau)(f^2,\phi)
=2K_f^\tau\!\left(\Phi_A(f^2-\phi^2)\right)
+4\Phi_A\!\left(\phi,K_f^\tau(\phi)\right).
}
\tag{19}
$$

第二项是真实第三 history，通常不能删去。

但对第 2 节的左 u、右 v，R261 的局部系数都支撑于 u，且关于 u 的 jets 为二次，所以 $\mathscr A_{\tau,u}v=0$。同一个原右 collar 的三个零常数给

$$
K_u^\tau(v)=0.
\tag{20}
$$

这支付了 (19) 的第二项，而不是从外槽支撑不交直接假定一个带尾算子为零。于是

$$
[a^2b^2]\mathcal B_A(\tau)(a^2u^2,bv)
=-2K_u^\tau\!\left(\Phi_A(v^2)\right).
\tag{21}
$$

令 $Jz(x)=\int_x^{r_*}z(\xi)\,d\xi$。原符号是

$$
K_u^\tau(w)=-J^3(\mathscr A_{\tau,u}w),\qquad
K_u^\tau(w)''=-J(\mathscr A_{\tau,u}w).
$$

在共同左 collar，保真实二次尾，因而

$$
[x^2]K_u^\tau(w)
=-\frac12\int\mathscr A_{\tau,u}w
=-\frac12\int c_{\tau,u}w.
\tag{22}
$$

最后一个等号只积分掉两个真实全导数；其系数支撑于 u，故即使 w 有非零左多项式尾也没有边项漏失。

将 (21)–(22) 代入原查询 (9)，准确得到

$$
\boxed{
\mathsf T(\mathcal B_A(\tau))(\mu(u),\mu(v))
=-\frac14\int c_{\tau,u}(x)
\,\Phi_A(v^2)(x)\,dx.
}
\tag{23}
$$

(23) 中的二次算子始终保原右积分；只是由于积分系数支撑于 u，才可在该支撑上使用它对右包 v 的真实左多项式。

### 4.2 八矩的真实左多项式

R73 的八坐标约定给

$$
A=\begin{pmatrix}
p_0&2r_1&-4r_0\\
p_1&2s_1&-4s_0\\
p_2&2t_1&-4t_0
\end{pmatrix},
\qquad t_0=p_0/4+s_1/2.
$$

对右包 v，令 $\nu=\mu(v)$。在它左方，

$$
\boxed{
\Phi_A(v^2)(x)
=-\frac14\nu^{\mathsf T}A
\begin{pmatrix}x^2\\-2x\\1\end{pmatrix}.
}
\tag{24}
$$

这是完整原尾，不是另选的积分常数。特别对原单位方向 $E_{p_j}$，$j=0,1,2$，

$$
[x^2]\Phi_{E_{p_j}}(v^2)=-\nu_j/4.
\tag{25}
$$

$E_{p_0}$ 的迹补偿也保留；它改变真实常数尾而不改变 (25)。

以 (17)、(18)、(23) 得

$$
\mathsf T(\mathcal B_{E_{p_j}}(\sigma_i))(\mu,\nu)
=\frac1{16}\mu_i\nu_j.
$$

故定义

$$
\boxed{
\mathcal K_{ij}
=16\mathcal B_{E_{p_j}}(\sigma_i),
\qquad 0\le i,j\le2,
}
\tag{26}
$$

便得到 (5)。这些是完整 W 中已付原 $\chi$ 与 E8 构成的真实响应方向。R247/R255 的 $\Delta\sigma_i=0$ 保证每条 $\mathcal K_{ij}$ 的 universal pure 准确为零。

于是

$$
\boxed{
\mathsf T(\mathcal R_{\mathrm p0})
=\operatorname{Mat}_3(\mathbb R).
}
\tag{27}
$$

九行九列的独立性由 (5) 直接给出，没有进行新的矩阵求秩，更没有据此增加整个 $\mathcal R$ 或 U 的已知维数。

## 5. 对称性、反对称性及正字符的准确后果

### 5.1 两种几何项都不能单独定号

直接将 (4) 与两槽互换式相加、相减，得到对称与反对称部分

$$
\begin{aligned}
\operatorname{Sym}\mathcal T_B(\mu,\nu)
=-\frac14\int\Big[
&t_\mu t_\nu+\tau_\mu\tau_\nu\\
&+\frac{k}{2h}
(\mathfrak a_\mu t_\nu+\mathfrak a_\nu t_\mu
+\eta_\mu q_\nu+\eta_\nu q_\mu)
\Big]ds,
\end{aligned}
\tag{28}
$$

$$
\boxed{
\operatorname{Alt}\mathcal T_B(\mu,\nu)
=-\frac18\int\frac{k}{h}
(\mathfrak a_\mu t_\nu-\mathfrak a_\nu t_\mu
+\eta_\mu q_\nu-\eta_\nu q_\mu)\,ds.
}
\tag{29}
$$

式 (27) 给全部六维对称矩阵与全部三维反对称矩阵的真实响应原像。它表明不能只靠第一行的平方型就删掉 (28) 的真实 history 交叉项，也不能将 (29) 未经证明地设零。第 6 节将进一步给实际成本的任意矩阵值，故这不只是形式响应域的计数。

### 5.2 真倒行本身仍不提供负值

在同 scalar germ 的真实 M0 倒行上，R73 的 M 只含速度的偶次组合，因此

$$
M^{\rm rev}(s)=M(L-s),\qquad
m^{\rm rev}(s)=-m(L-s).
$$

从 (3) 原式逐项有：$p$ 按倒行复合，$\mathfrak a,t,\eta,q$ 变号，$\tau$ 不变。故

$$
\boxed{\mathsf T_{B^{\rm rev}}=\mathsf T_B.}
\tag{30}
$$

同端 M0 块拼接时第二 history 在每块末回到零，所以 (4) 按块准确相加。式 (30) 说明真实负矩阵的取得仍需第 6 节的有限控制论证，不能把反走路径当作成本取负。

### 5.3 该矩阵不能承载 $\lambda_+$

R196 的真实正字符杀整个 $\mathcal R$。若存在矩阵空间上的实线性泛函 $\ell$ 使

$$
\lambda_+|_{U_{\mathrm p0}}=\ell\circ\mathsf T,
$$

则由 (5) 与 $\lambda_+(\mathcal K_{ij})=0$，$\ell$ 必杀所有矩阵单位，即 $\ell=0$。但 R201 给 $H\in U_{\mathrm p0}$、$\lambda_+(H)=1$，矛盾。

更具体，令

$$
H_{\mathsf T}
=H-\sum_{i,j}\mathsf T(H)_{ij}\mathcal K_{ij}.
$$

则

$$
\boxed{
\pi H_{\mathsf T}=0,\qquad
\mathsf T(H_{\mathsf T})=0,\qquad
\lambda_+(H_{\mathsf T})=1.
}
\tag{31}
$$

(31) 先是完整真实函数空间的线性身份，不把该表达式本身当成一个零基准 signed 成本字。

## 6. 保全部基准的真实整 pure 与九矩联调

### 6.1 准确调用一般有限观测定理

取 (11) 的九坐标作
$F:U\to\mathbb R^9$，取 (26) 的九条响应。它们满足 [R222](R222-simultaneous-real-pure-and-eight-flux-control.md)§1–5 的一般 $m=9$ 假设，且其观测矩阵恰为单位阵。

因此对任意

$$
p\in P=\pi U,\qquad A\in\operatorname{Mat}_3(\mathbb R),
$$

存在一个有限真实同 scalar germ、frame $I\to I$ 的块 D，使

$$
\boxed{
M_D=\mathbf T_D=0,\qquad
\pi V_D=p,\qquad
\mathsf T(V_D)=A.
}
\tag{32}
$$

在固定紧目标集上，还可取得固定有限词的 $C^1$ 目标截面。原总长、位移、费用及可能改变的基础度量并不固定。

这里不能用“九个 signed 响应满秩”直接跳到 (32)。所用 R222 机制为：

1. 每条 (26) 拆成有限个原 $\mathcal B_E(\tau)$，选真实第三 prototypes；全部完整 mixed 成本保留。
2. 在每组 prototype 后追加 R212 的实际整 pure 校正，使该组基准 pure 为零，但不删其 mixed 基准。
3. 真响应词给成本
   $E_0(t)+n(2\sum\widehat v_j+\sum t_j\mathcal K_j)$；
   其中 $E_0$ 与复制数 n 无关。
4. 同一个整 pure $C^1$ 截面准确支付
   $p-\pi E_0(t)$。这条校正带来的全部九矩值保留在有界 $C^1$ 函数 $\mathcal E(t,p)$ 中。
5. 在真实九矩基准决定的 t 盒固定之后，最后选有限 n，用
   $t=t^0+n^{-1}(A-\mathcal E(t,p))$
   的 Brouwer/统一收缩解同时付九坐标。

负系数只进入允许的小参数族及有限组合，不表示负路径；未知原基准没有被舍弃。所有有限生成库与 scalar 包络先选定，随后固定共同 I、右锚和查询 profiles；再增加有限重复不会扩原包络。

R222 的这个一般控制部分允许完整 W prototypes，不限 R71 交换子。R225§10.3 已明确：若另要保 Morse 或特定第三结构的自由扰动族，须有额外实现证明；本文不省去这一条件。

### 6.2 真实闭 hook 的整个矩阵也可指定

先把一个真实闭 hook 背景 $X_0$ 纳入共同有限库，其

$$
M_{X_0}=0,\qquad
\mathbf T_{X_0}=\kappa\mathfrak H,\qquad \kappa\ne0.
$$

其成本属于 U，来源是同端真倒行使
$X_0X_0^{\rm rev}$ 的 $M=\mathbf T=0$、成本为 $2V_{X_0}$；取半只用于线性空间归属。

给定目标矩阵 A，在 (32) 指定

$$
p=-\frac14\pi V_{X_0},\qquad
F(V_D)=\frac14\{A-\mathsf T(V_{X_0})\}.
\tag{33}
$$

按 R222§7 把同一个 D 插入真实 Klein prototype，其四个正确 ambient 副本保 frame、第三算子及改后真实位移闭合，且

$$
V_X=V_{X_0}+4V_D.
$$

故得到一个真正的有限闭 hook，满足

$$
\boxed{
M_X=0,\qquad
\mathbf T_X=\kappa\mathfrak H,\qquad
\pi V_X=0,\qquad
\mathsf T_X=A.
}
\tag{34}
$$

特别可取 $A=0$。R196 的完整身份仍给

$$
\lambda_+(V_X)=\int k^2\,ds
=L+\int(h_s/h)^2\,ds>0.
\tag{35}
$$

所以新矩阵全零并不强迫正字符为零。这是实际几何见证，不仅是 (31) 的空间反例。

由于 A 可为任意实矩阵，M0、完整第三 hook 和 whole-pure 零本身既不强迫 $\mathsf T_X$ 对称，也不强迫其对称部分具有一个固定非零定号组合。任一非零线性矩阵泛函都可在这些真实闭 hook 上取正、负、零；取得它们的几何与基准一般不同。

(34) 不保持一个先验指定的 Gaussian 共振几何族，也没有自动保全域 Morse、某一固定偶 germ 或其他已付观测。若这些额外条件是后继模板的前提，必须在同一约束族中另行联调；不能把 R222 的一般闭 hook 偷换成该更窄族。

## 7. 新九矩支付仍不等于全部平台或完整 period

当前 R292/R295 的模板可以严格要求 $\mathsf T_B=0$。本文证明该矩阵条件本身可真实支付，并非一个独立于所有 pure-zero 响应的 $\lambda_+$ 障碍。以下欠账仍保留。

### 7.1 单包自 history 不由九矩自动消失

对同一个响应、单包 u，取 $f=u,\phi=0$。由 (19)、(22)，其真实 self 系数为

$$
\boxed{
q_{\mathcal B_A(\tau)}(u)
=-\frac14\int c_{\tau,u}(x)\,\Phi_A(u^2)(x)\,dx.
}
\tag{36}
$$

此时 $\Phi_A(u^2)$ 在 u 包内是完整原函数，不能替换为 (24) 的左多项式。因此 (18) 不足以判 (36)，不能从 $\mathsf T=0$ 推全部 $q_i=0$，也不能推 self 的最高 profile jet 主部为零。

### 7.2 不把不同有限观测的满射合并

本文没有证明九矩与已付八个修正通量、所有平台常数/一次系数、每个活动通量或全部 $q_i$ 联合满射。若加入新观测，必须检查同一响应组的联合矩阵或给新的核方向；不能将两个各自满射的结论相加成联合满射。

R225 的全部平台、内部 Laurent、两端 germ、真实右锚常数必须由同一个元素同时支付。之后同一个合法二阶 gauge 还须通过 R221 的完整 ruling 条件。本文不宣布这些门完成，也不把改变几何期间的控制路径当作固定度量的等距族。

### 7.3 三矩开集仅用于观测忠实性

(10) 的真实三矩包含开集，只用于证明 (11) 的矩阵坐标被原查询唯一决定以及 (5) 的矩阵身份。它不表示三个 $\mu$ 是可独立指定的几何控制，不表示九个 history 项可逐项改动，也不重新证明任何圆的三矩或完整第三 ruling 合法性。

本文的新增完成项是：三个原 c 系数的准确二次矩身份 (13)–(18)，九个完整 pure-zero 响应原像 (26)，真实全矩阵观测满射 (27)，以及保全部基准的实际联调与闭 hook (32)–(35)。它们可直接供后继处理 self 与剩余完整平台条件，无需重跑已付八个 hook、旧 pure 分类或原第四 forcing。
