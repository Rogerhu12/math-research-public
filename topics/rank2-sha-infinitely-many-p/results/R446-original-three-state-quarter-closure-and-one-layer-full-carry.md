# R446 — 原残余三态四挠闭包与同一层完整 carry 消元

日期：2026-11-14。**状态：已证明。**

R443 的反射态不仅在总输出核心下闭合，也属于同一个残余
$Q$ 核心的三维实际来源空间。本篇支付其完整四挠恒等式、全部中心
符号和第三残余来源的整性。两个真实核心在该空间生成一个
$D_8$ 作用；同一层三个真实单位 carry 的一个单位线性组合
准确返回原 $\mathcal K_0$。等式保留任意完整 $W$ 测试，
不必先作第一 principal 投影，也没有遗留奇奇部分。

这仍不把任意 $W$ 深子域的中央赋零；原算术零只控制下文明确写出的
完整中央行。主目标未完成。

## 1. 固定原来源、真实平移与三个状态

全篇使用 R431、R439 的同一固定普通 ray、原周期和
$$
\lambda=-\bar\pi_0^{-1},\qquad
\lambda_\sigma=-\lambda,\qquad
\kappa=p/\bar\pi_0^2,\qquad
\eta=\eta_{5,p}\in\{1,-1\}.
\tag{1}
$$
没有重新选择 $\pi_0$ 或重置 sigma 的物理尺度。
曲线参数始终是原 $b=17$。

沿用 R424、R443 的
$$
\Sigma(y,v)=\sigma(y-v)\sigma(y+v),\qquad
A_0(y,v)=G_{16}(y)R_{16,16}(y,v)
             \in\mathcal S_{32}\otimes\mathcal S_{16}.
$$
于是
$$
\mathcal K_0=\Sigma A_0,\qquad
\mathcal L_0=\sigma(y+v)A_0.
\tag{2}
$$
对 $t\in E[4]$，以下均为 R443 的完整 canonical Heisenberg lift；
不是仅对函数参数作平移。定义
$$
D_-=\frac18\sum_{t\in E[4]}
             T_t^{(32)}\otimes T_{-t}^{(16)},\qquad
D_+=\frac18\sum_{t\in E[4]}
             T_t^{(32)}\otimes T_t^{(16)}.
\tag{3}
$$
记 $R=R_Y$ 为第一轴的普通反射。由于两个 level 都是偶数，
$$
R D_- R=D_+,\qquad R A_0=A_0,\qquad R\Sigma=\Sigma.
\tag{4}
$$
R443 已支付
$$
A_1=D_-A_0,\qquad \mathcal K_1=\Sigma A_1,\qquad
\mathcal L_1=\sigma(y+v)A_1.
$$
本篇加入实际第三态
$$
\boxed{
A_R=R A_1=D_+A_0,\quad
\mathcal K_R=\Sigma A_R=R_Y\mathcal K_1,\quad
\mathcal L_R=\sigma(y+v)A_R.}
\tag{5}
$$
注意 $\mathcal L_R$ 的定义并不是对 $\mathcal L_1$ 直接反射：
外部待消的因子仍固定为 $\sigma(y-v)$。

## 2. 完整四挠恒等式

本篇的关键完整身份是
$$
\boxed{
D_-A_1=A_0,\qquad
D_-A_R=A_1+A_R-A_0.}
\tag{6}
$$
第二式也可写为
$$
\boxed{D_-D_+A_0=D_-A_0+D_+A_0-A_0.}
\tag{7}
$$
这里没有作任何输出边际、角投影或有限点取值。

### 2.1 含奇项的 canonical 商环核算

为给 (6) 一份可独立重放的有限证书，先在 $b=1$ 计算。
取
$$
q=1+\sqrt3,\quad q^2=2q+2,\quad
F=-6q-3,\quad \tau=f\,y,\quad f^2=F,\quad
\tau^2=F(x^3+1),
$$
$$
k_t=\frac{1-q}{12F}.
$$
R443 的真实四挠 lift 满足
$$
R_t:=\frac{\sigma_t^4}{\sigma^4}
 =x^2-q^2x-2q+\frac23(1-q)\tau,
$$
$$
x_t=\frac{B(x)-2\tau}{d(x)},\qquad
B(x)=-qx^2+q^2x+2,\quad d(x)=(x+q)^2,
$$
$$
R_tR_{-t}=(x+q)^4.
\tag{8}
$$
在 level $N=32,16$，偶基向量的完整 lift 为
$$
T_t^{(N)}(\sigma^Nx^i)/\sigma^N
   =k_t^{N/8}R_t^{N/4}x_t^i.
\tag{9}
$$

第二次变换必须保留 R443 的奇奇部分。由 $x'=2y$、
$y'=3x^2$，直接微分 (8) 得
$$
\boxed{
fR_ty_t=
\frac{R_t}{d^2}
 \left(2\tau^2d'-3Fx^2d
       +\tau(B'd-Bd')\right).}
\tag{10}
$$
右侧在所示商环中是多项式；两个系数的余式均为零。
因此全部奇基向量
$\sigma^Nx^iy$ 的 lift 也由 (8)、(10) 的有限乘法给出。
第一轴的奇 lift 若写作 $(a+\tau b)/f$，
第二轴在 $-t$ 的奇 lift 就是
$(-a+\tau b)/f$。这个负号是中心与反射规范的一部分，
不能把它改成偶基向量的符号。

对 R443 已列出的完整 $A_1$ 偶偶、奇奇多项式分别使用
(9)、(10)，乘共同系数 $k_t^6$，得到：

1. 两个单奇部分逐项为零。
2. $\sqrt3$ 的所有非有理系数逐项为零。
3. 三个半周期的 $\mu_3$ 转移只保留多项式指数
   $i+j\equiv1\pmod3$，并乘 $3$。
4. 加回四个二挠项后，完整 $D_-A_1$ 的偶偶部分是 $A_0$，
   奇奇部分是零。
5. 完整 $D_-A_R$ 的奇奇部分是零，偶偶部分准确为
   $2(A_1)_{\rm even}-A_0=A_1+A_R-A_0$。

这些都是整个多项式环中的等式。可重放脚本为
[check-r446-three-state-quarter-and-carry.py](../scripts/check-r446-three-state-quarter-and-carry.py)，
其完整有理系数与关系证书为
[check-r446-three-state-quarter-and-carry.json](../scripts/check-r446-three-state-quarter-and-carry.json)。
脚本读取 R443 的完整系数证书，但不执行或改写 R443 脚本。
这里既没有插值，也没有目标素数扫描。

若 $u^6=b$，曲线缩放给
$A_{0,b}(y,v)=u^{-4}A_{0,1}(uy,uv)$。
canonical lift 与同一缩放交换，三个状态都带同一因子
$u^{-4}$。故上述完整身份下降到原 $b=17$。
本篇没有用 $b=1$ 的周期替代原周期。

## 3. 第三态的完整 theta 格、整性与核心

由 (5)，
$$
\mathcal K_R\in\mathcal S_{34}\otimes\mathcal S_{18}.
$$
所有实际四挠点、平移 lift 和 $1/8$ 在当前 $p>19$ 都整。
R424 的 $G_{16}R_{16,16}$ 已是整来源，因此
$A_R$、$\mathcal L_R$ 和 $\mathcal K_R$ 都给整有界测度。
这个整性证明不需要在 Amice 环中除以一个非单位。

在 R437 的真实正交坐标
$$
y=w+9q,\qquad v=w-17q,
$$
$A_R$ 的两个 level 是 $32,16$；
与外因子 $\sigma(y+v)=\sigma(2w-8q)$ 合起来，
$$
\begin{aligned}
N_W&=32+16+4=52,\\
N_Q&=32\cdot9^2+16\cdot17^2+8^2=7280,\\
\text{交叉项}&=32\cdot9-16\cdot17-2\cdot8=0.
\end{aligned}
$$
所以完整第三残余态准确属于
$$
\boxed{\mathcal L_R(w,q)\in
       \mathcal S_{52}\otimes\mathcal S_{7280},\qquad
       \sigma(26q)\mathcal L_R(w,q)=\mathcal K_R(w,q).}
\tag{11}
$$

R443 已证明完整 $\mathcal K_1$、$\mathcal K_R$ 的 $W$ 核心均为
$-\lambda$。由于 $\sigma(26q)$ 只依赖伴随输出，
$W$ trace 与乘此因子交换；在整 Amice 幂级数环中消去同一非零因子，
得三个残余态的完整 $W$ 核心都为 $-\lambda$。

对 $Q$ 二挠平移，$A_0$、$A_1$、$A_R$ 的反对角二挠作用均固定。
这里第一轴反射与二挠平移交换，而 (3) 也与该作用交换。
外部 $\sigma(y+v)$ 的 $Q$ 位移是 $-8t$，为偶整周期，
其完整 lift 固定。因此三态均属于 R439 已付的二挠固定格。

R439 的 whole level $1820$ 核心身份适用于这个完整固定格，
含同一个绝对符号 $\eta$。拉回 level $7280$ 后，其归一化
$Q$ 核心就是 $\eta D_-$。由 (6)，完整残余核心为
$$
\boxed{
\begin{array}{c|ccc}
 &\mathcal L_0&\mathcal L_1&\mathcal L_R\\ \hline
K_W&-\mathcal L_0&-\mathcal L_1&-\mathcal L_R\\
K_Q/\eta&\mathcal L_1&\mathcal L_0&
                 -\mathcal L_0+\mathcal L_1+\mathcal L_R .
\end{array}}
\tag{12}
$$
表中尚未乘公共测度标量 $\lambda$；
实际限制一层深度再除以 $\kappa$ 时才带该标量。

另令总伴随输出仍为 R431、R442 的 $A$。
R443 的完整总核心已给
$$
\boxed{
K_A\mathcal K_0=\mathcal K_0,\quad
K_A\mathcal K_1=\mathcal K_R,\quad
K_A\mathcal K_R=\mathcal K_1.}
\tag{13}
$$
这不是把残余 $Q$ 与总 $A$ 视为同一个输出。

## 4. 实际三维闭包与两个核心的 $D_8$ 作用

在三态来源空间上记 $D$ 为 (12) 的第二行除去 $\eta$，
记 $R$ 为 (13) 的总核心。按列记录各基向量的像，
$$
D=
\begin{pmatrix}0&1&-1\\1&0&1\\0&0&1\end{pmatrix},
\qquad
R=
\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\tag{14}
$$
三个来源线性独立：R443 的非零奇奇部分区别
$\mathcal K_1,\mathcal K_R$，其第一 principal 四列与原 $S$
的增广秩区别 $\mathcal K_0$ 和两者的偶部。

直接有
$$
D^2=R^2=I,\qquad (DR)^4=I,\qquad (DR)^2\ne I.
\tag{15}
$$
更透明的实际来源基是
$$
E=\frac{\mathcal K_1+\mathcal K_R}{2},\qquad
V=\mathcal K_0-E,\qquad
O=\frac{\mathcal K_1-\mathcal K_R}{2}.
\tag{16}
$$
对应残余来源同样使用 $\mathcal L_i$ 的这三个线性组合。
两个核心准确作用为
$$
\boxed{
D:E\mapsto E,\ V\leftrightarrow O;\qquad
R:E\mapsto E,\ V\mapsto V,\ O\mapsto-O.}
\tag{17}
$$
因此这是真实的一维共同特征加二维标准块。
没有为 $E$ 或 $V$ 引入新的算术中央零。

## 5. 同一个三输入测度上的完整限制

在原物理残余测度中使用 R439 的 $(W,Q)$，并令
$$
C=26c,\qquad A=Q+C.
$$
对 $i=0,1,R$，取实际三输入来源
$$
\rho_i=\nu_{\mathcal L_i}(W,Q)\otimes[26]_*\nu_\sigma(C),
\qquad \mathfrak k_i=(W,A)_*\rho_i.
\tag{18}
$$
其物理两个输出准确为
$$
Y=(17W+A)/26,\qquad X=(9W-A)/26.
\tag{19}
$$

线性延拓记 $\rho(v)$、$\mathfrak k(v)$。
由三个独立输入的完整核心，任意 $a,b,c\ge0$ 有
$$
\boxed{
\rho(v)|_{\{W\in p^a,\ Q\in p^b,\ C\in p^c\}}
 =(-\lambda)^{a+c}(\eta\lambda)^b
 [\kappa^a,\kappa^b,\kappa^c]_*\rho(D^bv).}
\tag{20}
$$
全部另外输入都保留；$D$ 改的是显示的实际残余来源。
另一方面，完整总输出核心给
$$
\boxed{
\mathfrak k(v)|_{A\in p}
  =\lambda[1,\kappa]_*\mathfrak k(Rv).}
\tag{21}
$$

## 6. 同一层三个真实单位 carry 的单位消元

对每个状态定义真实单位相消域
$$
\mathscr B=\{Q,C\in\mathbf Z_p^\times,\ A=Q+C\in p\},
$$
并使用同一个规范总输出
$$
\mathfrak b_i=(W,A/\kappa)_*
                    (\mathbf1_{\mathscr B}\rho_i).
\tag{22}
$$
在 $A\in p$ 上，除 $\mathscr B$ 之外的分支正是 $Q,C$ 同时深一层。
该分支由 (20) 带系数 $-\eta\lambda^2$ 和状态 $D$。
从 (21) 减去它，得到完整来源身份
$$
\boxed{\mathfrak b(v)
   =\lambda\mathfrak k(Rv)+\eta\lambda^2\mathfrak k(Dv).}
\tag{23}
$$
特别令 $t=\eta\lambda$，
$$
\begin{aligned}
\mathfrak b_0&=\lambda\mathfrak k_0+\eta\lambda^2\mathfrak k_1,\\
\mathfrak b_1&=\lambda\mathfrak k_R+\eta\lambda^2\mathfrak k_0,\\
\mathfrak b_R&=\lambda\mathfrak k_1+
           \eta\lambda^2(-\mathfrak k_0+\mathfrak k_1+\mathfrak k_R).
\end{aligned}
\tag{24}
$$
这是同一层三条真实 carry，没有混合一层和两层的不同规范化。

在 (16) 的基下，$\lambda^{-1}\mathfrak b$ 的算子为
$$
\begin{pmatrix}
1+t&0&0\\
0&1&t\\
0&t&-1
\end{pmatrix}.
\tag{25}
$$
第二块的平方是 $(1+t^2)I$。其完整行列式是
$-(1+t)(1+t^2)$。

R410 已在同一原 ray 支付 $1-\lambda$、$1+\lambda$、
$1+\lambda^2$ 均为单位；这里没有追加素数细分。
也可直接核对最后一个因子：原 ray 给 $p\equiv7\pmod{64}$，
故 $p\equiv3\pmod4$。若 $1+\lambda^2$ 非单位，则在选定的
普通剩余域中 $\pi_0\equiv0$、$\bar\pi_0\equiv a_p$，得到
$a_p^2\equiv-1\pmod p$，与 $p\equiv3\pmod4$ 矛盾。
因此 $1+t=1+\eta\lambda$ 和 $1+t^2$ 都是已付单位。

从 (24) 作精确消元，得到
$$
\boxed{
(1+t)\mathfrak b_0+t^2\mathfrak b_1-t\mathfrak b_R
 =\lambda(1+t)(1+t^2)\mathfrak k_0.}
\tag{26}
$$
整个比例是单位。这是完整两个输出的测度等式，不需要
第一 principal 角投影来杀掉余项。
所以可乘任意连续 $f(W,A/\kappa)$，特别可保任意 $W$ 深条件。

必须同时保其精确范围：(26) 已向 $(W,A/\kappa)$ 推前。
若还要保留原 $C$ 或另一个独立伴随变量，须使用相应三变量核心；
这里没有把该额外隐藏输入无代价附回。

## 7. 原完整中央的准确返回及仍有的补域

对任意连续 $h$，在规范输出 $(W,A')$ 上定义
$$
F_{u,h}(W,A')
=\mathbf1_{Y'\ {\rm unit}}\langle Y'\rangle^{du}h(X'),
\quad
Y'=(17W+A')/26,\quad X'=(9W-A')/26.
$$
记 $B_i(u,h)=\int F_{u,h}\,d\mathfrak b_i$。
由 (26) 和 R430，完整地有
$$
\boxed{
(1+t)B_0(u,h)+t^2B_1(u,h)-tB_R(u,h)
 =-\frac23\lambda(1+t)(1+t^2)J_S(u)
                         \int h\,d\nu_{G_{18}}.}
\tag{27}
$$
没有把新来源的中央先设为零。取 R441 的同一真实测试 $h(X)=X^6$，
$$
\boxed{
(1+t)B'_0(0,X^6)+t^2B'_1(0,X^6)-tB'_R(0,X^6)
 =14976b\Omega^6\lambda(1+t)(1+t^2)J'_S(0).}
\tag{28}
$$
显示比例仍为单位。三条左侧的物理输出都由同一个
$A'=A/\kappa$ 读取。

若在 (26) 两边再加 $W\in p^n$，等式仍完整成立，
但右侧变成原 $\mathcal K_0$ 的该深管中央。
R430 的 $J'_S(0)=0$ 本身不把这个子域中央赋零。
因此本篇保留 R441 的非零深管及其所有外部补域。

还可看出三维闭包没有暗中创造一条新算术零。
第一 principal 完整测试杀掉 $O$，但一般不杀掉 $E$ 或 $V$。
写其完整中央行为 $\Gamma_E,\Gamma_V,\Gamma_O$，则
$$
\Gamma_O(u,h)=0,\qquad
\Gamma_V(u,h)=\Gamma_0(u,h)-\Gamma_E(u,h).
\tag{29}
$$
假设原 $J'_S(0)=0$，只能推出
$\Gamma'_V(0,h)=-\Gamma'_E(0,h)$；
不能把两边各自设为零。

第三态也确实含新的隐藏域信息。例如在原物理残余坐标 $(y,v)$，
完整多项式的五阶首项给
$$
[\deg5](\mathcal L_1-\mathcal L_R)
 =\frac2{21}yv(y+v)(5y^2+v^2)\ne0,
\tag{30}
$$
而外部还原后的 $\mathcal K_1-\mathcal K_R$ 对全部第一 principal
完整测试为零。非零隐藏域与完整中央零可以同时存在；
后续必须用本篇实际核心追踪它们的补域，不能直接相认。

## 8. 本条支付的接口

本篇付清了 R442 原先没有的第三真实残余状态及其完整 $Q$ 核心，
把残余核心、总核心和反射放进同一个精确三态空间。
同一层完整 carry 的 (26) 比仅在第一 principal 行杀余项更强，
并可直接配合保独立伴随输入的三变量核心继续追踪。
原两个算术中央和 R441 非零隐藏域之间的最终全域闭合仍待完成。
