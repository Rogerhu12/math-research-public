# R262 — 非 beta 拉回的 norm-two 常数来源与原八次伴随整基

日期：2026-11-13。**状态：一族真正非 $[\beta]^*$ 的全纯代数来源、完整 norm-two primitive 常数式、真实共轭十七迹、到原四八次伴随的可逆矩阵，以及原两条完整中央行的准确重写均已证明。没有由对数常数非零或矩阵可逆推出原中央非零。**

本篇接续 [R260](R260-positive-normtwo-clearing-weighted-traces-and-terminal-cm17-image.md)
实际算出的纯拉回秩一终像。新来源保留 $z$ 变量中的 $1/x(z)$ 与
$(x(z)^2-1)^{-h}$，因而不属于那个纯 $\beta$ 变量的输入。

## 1. 一个确实消去非恒定对数的原 norm-two 行

沿用
$$
E_0:y^2=x^3-x,\quad dz=dx/(2y),\quad
\alpha=1+i,\quad\beta=4-i,\quad\bar\beta=4+i,
$$
$$
S_8=-y\vartheta\sigma^3,\qquad F=S_8^{17},\qquad
B_0(z)=\frac1{x(z)^2-1}.
$$
令 $\Phi_k=\Psi_k-C_k$ 为 R253 的四个原八次中心化对数，
$k=1,3,5,7$。原准确 norm-two 式为
$$
\Phi_k(z+T_0)=-\Phi_k(z)-2C_k,\qquad
T_0=(1+i)\Omega_0/2,
\tag{1}
$$
且 $C_k\ne0$。本篇不把 $C_k$ 当作 $p$ 进单位。

关键的实际有理函数恒等式是
$$
\boxed{x(z)B_0(z)=\frac1{2i x(\alpha z)}.}
\tag{2}
$$
因此左侧在原 norm-two deck 变换 $z\mapsto z+T_0$ 下不变。
对 $0\le h\le8$，定义
$$
q_h(z)=x(z)B_0(z)B_0(\alpha z)^h,
\qquad H_\beta(z)=F(\alpha\beta z),
$$
$$
\mathcal P_{k,h}(z)=H_\beta(z)q_h(z)\Phi_k(z),\qquad
G_h(w)=\frac{F(\beta w)}{x(w)(x(w)^2-1)^h}.
\tag{3}
$$
$H_\beta=[\alpha]^*(F(\beta w))$ 的 degree 为 $2312$。
其标准 $T_0$ Mumford lift 的符号是负，因为
$\alpha\beta T_0=(1+4i)\Omega_0$、$F$ 的原半特征为 $(-1)^{m+n}$。
故正有限平坦迹仍使用 R259/R260 的 canonical lift
$-\mathcal T_{T_0}^{2312}$。
将 (1)、(2) 放入整个两点纤维，得到
$$
\boxed{[\alpha]_*\mathcal P_{k,h}(w)=iC_kG_h(w).}
\tag{4}
$$
这是全部原 germ 的恒等式。非恒定对数确已消去，相位准确为 $i$。
未中心化来源 $H_\beta q_h\Psi_k$ 的同一迹是零；
(4) 正是原点中心化留下的水平常数，不是另加的任意非零量。

## 2. 真正的全纯来源与逐点零重

每个 $G_h$ 都是 degree-$1156$ 的全纯代数 theta 截面，
具有原 $T_0$ twist 和全局 $i=-1$ 特征。
逐点检查如下。

在 $T_\pm=(\pm1,0)$，$F(\beta w)$ 的零阶为十七，
$(x^2-1)^{-h}$ 的极阶为 $2h$，故余下至少 $17-2h\ge1$ 阶零。
在 $T_0=(0,0)$，$F(\beta w)$ 有三十四阶零，$1/x$ 有二阶极，
余下三十二阶零。在原点，准确有
$$
G_h(w)=w^{2+4h}+O(w^{6+4h}).
\tag{5}
$$
其他点不产生新极点。这不是仅按多项式次数推断全纯性。

$H_\beta q_h$ 也是实际全纯代数截面：$xB_0$ 在 $T_\pm$ 的二阶极
由 $H_\beta$ 的三十四阶零支付；$B_0(\alpha z)^h$ 在
$\alpha^{-1}T_\pm$ 的 $2h$ 阶极由十七阶零支付。
在 $T_0$ 和原点则分别有至少二阶零。
乘 $\Phi_k$ 后是原对数来源，仍须保其 multivalued 部分；
这里没有把含对数的 germ 称为单值全纯 theta 截面。
其原点阶至少 $6+4h$，并在原对数除子处保留相应高阶 theta 零。

$G_h$ 的分母使用原 $x(w)$，不是 $x(\beta w)$。
所以不能把它写成 R260 所排除的纯 $[\beta]^*$ frame 修正，
也不能套用那个秩一结论删除其 primitive 分量。

## 3. 整个共轭 CM17 迹及实际相邻权 frame

置 $U=x(z)^2$，并沿用 R248 的
$$
\mathcal W=-y\vartheta\sigma^{67},\qquad D(U)=U^8(U-1)^8,
\qquad F=\mathcal W D.
$$
取 R248 同一线丛同构与正有限平坦迹，得到
$$
[\bar\beta]_*G_h=\frac{\mathcal W}{x}P_h(U),\qquad\deg P_h\le16.
\tag{6}
$$
每条都是整个十七点纤维的迹。
写 $P_\beta,P_{\bar\beta},Q_{\bar\beta},K_{\bar\beta}$ 为 R248 已固定的
实际 CM 多项式，其精确计算公式是
$$
\boxed{
P_h(t)=D(t)\operatorname{Tr}_{UQ_{\bar\beta}^4-tK_{\bar\beta}^4=0}
\left[
\left(\frac{P_\beta}{P_{\bar\beta}}\right)^{17}
\frac{Q_{\bar\beta}^2}{K_{\bar\beta}^2}\,
\frac1{(U-1)^h}
\right].}
\tag{7}
$$
这里的 frame 因子是
$x(\bar\beta z)/x(z)=Q_{\bar\beta}^2/K_{\bar\beta}^2$。
它与 R254 的 $x(z)x(\bar\beta z)$ 不同，不能误添一个 $U$。

全纯性和 $i$ 特征已经先给出十六次界。
证书在十七个准确纤维上恢复全部九条 $P_h$，再逐条核对一个
未用于插值的完整纤维；没有按有限数值样本猜测次数。

## 4. 原四八次坐标及前四条来源的可逆性

令 $\mathcal V$ 是 R246 的原双向 dyadic 反向算子，定义
$$
Z_h=\mathcal V\bigl(([\bar\beta]_*G_h)(2z)\bigr).
$$
R254 已完全支付相邻 CM5 八次投影及四个 $\delta_j$。
在同一原 R235 基 $H_1,H_3,H_5,H_7$ 中，本篇得到
$$
\boxed{Z_h=\sum_{j=1,3,5,7}M^{\rm n}_{j,h}H_j(2z),
\qquad 0\le h\le8.}
\tag{8}
$$
全部三十六个系数均在证书中明确给出。
特别，对最初要求的 $G_0=F(\beta z)/x(z)$，写 $r=\sqrt2$，
其四个准确系数为
$$
\begin{aligned}
M^{\rm n}_{1,0}
 &=-\frac{35109363+26933343r+i(147514549+100285190r)}{2^{25}},\\
M^{\rm n}_{3,0}
 &=\frac{-127137551-81471538r+i(24345715+47012661r)}{2^{25}},\\
M^{\rm n}_{5,0}&=\sigma M^{\rm n}_{1,0},\qquad
M^{\rm n}_{7,0}=\sigma M^{\rm n}_{3,0},
\qquad \sigma(r)=-r,\quad\sigma(i)=i.
\end{aligned}
\tag{9}
$$
四个原八次分量全部非零。

更强地，取 $h=0,1,2,3$ 的前四列 $M_4^{\rm n}$，准确有
$$
\boxed{
\det M_4^{\rm n}
=-\frac{8166189052086266994027356593}{2^{88}}
-\frac{741021328781080805667662475123}{2^{94}}i\ne0.}
\tag{10}
$$
因此前四个实际非拉回来源已经覆盖整个原四维八次伴随，
不必使用剩余五条才能恢复原两列。
原相邻十七维空间中的其余分量保存在证书中；它们由
$\mathcal V=\mathcal V\Pi_v$ 的真实八次投影去除。

令 R235 的原系数列为 $\mathbf a=(a_j)_j$、$\mathbf b=(b_j)_j$，定义
$$
\eta_A=(M_4^{\rm n})^{-1}\mathbf a,\qquad
\eta_B=(M_4^{\rm n})^{-1}\mathbf b.
\tag{11}
$$
证书列出全部八个系数，并回乘核定
$$
\boxed{C_A(2z)=\sum_{h=0}^3\eta_{A,h}Z_h,\qquad
C_B^+(2z)=\sum_{h=0}^3\eta_{B,h}\kappa^{-1}Q_{+,0}Z_h,}
\tag{12}
$$
其中 $\kappa=2^{-1/4}$。
这恢复的是原两条实际 companion，不把九个新来源命名为新的椭圆曲线。

## 5. 非零常数已经送入原 companion，且 CM 补偿全部保持

定义完整原 norm-two 观察
$$
\mathscr R_{k,h}
=\mathcal V\left(
\bigl([\bar\beta]_*[\alpha]_*\mathcal P_{k,h}\bigr)(2z)
\right).
$$
由 (4)、(8) 得到全部实际源的等式
$$
\boxed{\mathscr R_{k,h}=iC_kZ_h.}
\tag{13}
$$
于是
$$
\mathscr C_{A,k}:=\sum_{h=0}^3\eta_{A,h}\mathscr R_{k,h}
=iC_k C_A(2z).
\tag{14}
$$
对 $B$ 使用 R235 的原次数恢复算子
$\operatorname{Reg}:K_j\mapsto\widetilde K_j$，以及其三个固定
$a_\ell L_\ell$ 补偿，定义
$$
\begin{aligned}
\mathscr C_{B,k}:={}&
\sum_{h=0}^3\eta_{B,h}\operatorname{Reg}
           (\kappa^{-1}Q_{+,0}\mathscr R_{k,h})\\
&+iC_k\sum_{\ell=1}^3a_\ell L_\ell(2z).
\end{aligned}
$$
则准确有
$$
\boxed{\mathscr C_{B,k}=iC_k C_B(2z).}
\tag{15}
$$
这里的 CM 系数仍由 R235 的两个最高阶条件唯一决定。
没有把 (15) 中显式加入的已知常数补偿当成一条原来不存在的零观察。

质量与原对象一致：
$$
\mathscr C_{A,k}/z^2\big|_{z=0}
=-iC_k\frac{272}{1155},\qquad
\mathscr C_{B,k}/z^2\big|_{z=0}
=-iC_k\frac{2261}{10240}.
\tag{16}
$$

## 6. 完整中央行、全部连接及缩放单位

固定惰性 $p>19$，排除 (10)、(11) 及其余固定代数分母的有限坏素位。
置 $d=p+1,c=272c_0,q_2=2^{p-1}$，
$$
\Theta_2=\vartheta(4z)^{17},\qquad
\nabla_0=\partial_z-\Theta_2'/\Theta_2,\quad
W=z\Theta_2'/\Theta_2,\quad W_0=W-dcz^d.
$$
对任一伴随 $U$，置
$$
f_U=J_c(U/z^2),\quad g_U=J_c(W_0U/z^2),\quad
h_U=J_c((W_0^2+EW_0-W_0)U/z^2),\qquad E=z\partial_z.
$$
完整二阶表达保持为
$$
\begin{aligned}
J_c(\nabla_0^2U;u)={}&(du+1)(du+2)f_U(u)
 +du(d-3-2du)f_U(u-1)\\
&+d^2u(u-1)f_U(u-2)-2(du+1)g_U(u)
 +2dug_U(u-1)+h_U(u).
\end{aligned}
\tag{17}
$$
特别其质量项 $2f_U(0)$ 由 (16) 全部保留。

令 $A=A_{17}(2z)/16$、$B=A_{34}(z)$，定义两个完整源
$$
\mathscr A_k=\frac1{16}\nabla_0^2\mathscr C_{A,k}
                 +iC_k\beta_A\Theta_2,
$$
$$
\mathscr B_k=\frac1{16}\nabla_0^2\mathscr C_{B,k}
                 +iC_k\beta_B(\Theta\rho)(2z),
$$
其中 $\beta_A=34/1155,\ \beta_B=2261/81920$ 是原值。
由 (14)、(15) 及 R229 的原二阶关系，得
$$
\boxed{
J_c(\mathscr A_k;u)=iC_k q_2^uJ_{68c_0}(A;u),\qquad
J_c(\mathscr B_k;u)=iC_k q_2^uJ_{68c_0}(B;u).}
\tag{18}
$$
所有原点质量相消，$\mathscr A_k(0)=\mathscr B_k(0)=0$。
所以中央导数准确为
$$
\boxed{
J_c'(\mathscr A_k;0)=iC_kJ_{68c_0}'(A;0),\qquad
J_c'(\mathscr B_k;0)=iC_kJ_{68c_0}'(B;0).}
\tag{19}
$$
(18) 先保留全 $q_2^u$，再用原零质量得到 (19)。

若要把 (17) 转回最初对数输入，取共同 $[2]$ 源
$f=F(2\alpha\beta z)$，degree 为 $9248$。
所有实际分支斜率都是 $r=(\alpha\bar\beta)^{-1}$。
对包含原 Mumford 乘子的分支 $T_\nu$，设
$a_\nu=\partial_z\log(T_\nu f/\Theta_2)$。链式法则准确给
$$
\boxed{
\nabla_0^2T_\nu Q
=r^2T_\nu\nabla_f^2Q+2r a_\nu T_\nu\nabla_fQ
 +(a_\nu^2+a_\nu')T_\nu Q.}
\tag{20}
$$
此处 $Q=f\,q_h(2z)\Phi_k(2z)$，所以
$\nabla_f^jQ=f\partial_z^j(q_h(2z)\Phi_k(2z))$。
式 (20) 保留 $q_h$ 的全部导数，以及 $\Phi_k''$、$\Phi_k'$、
$\Phi_k$ 三块，不能只保留原代数 $\Phi_k''$ 行。

若移出各分支的缩放，还须带上
$$
\left(U_{\alpha,p}U_{\bar\beta,p}\right)^{-u},\qquad
U_{\alpha,p}=\alpha^{p+1}/2,\quad
U_{\bar\beta,p}=\bar\beta^{p+1}/17.
\tag{21}
$$
(17)–(20) 都先在实际目标 germ 内运算，故未省略该单位。
原 R54/R254 盘 $p^{-1/(2p)}$ 上，有限次有理乘子、连接和除去固定
零阶保持完整 Newton 收敛。单个平移后的对数仍使用 $p^{1/2}$ 型界，
不把它误换成未平移角色和的 $R^4$ 界。

## 7. 已完成的兼容关系与尚未得到的非零性

(4)、(13) 已把非零 $C_k$ 通过真正非拉回载体送入原四八次图，
并由 (10)–(18) 完整恢复两条原中央行。
所以这次没有停在一个被共轭十七迹杀掉的纯拉回来源。

但 (19) 是准确的乘法关系，不是额外的非零定理。
已知 $C_k\ne0$ 只能给
$$
J_c'(\mathscr A_k;0)=0\iff J_{68c_0}'(A;0)=0,
\qquad
J_c'(\mathscr B_k;0)=0\iff J_{68c_0}'(B;0)=0.
$$
它没有独立证明左端非零。四个 $C_k$ 的代数系数线性独立，
也不能应用于系数仍为未知 $p$ 进 Mellin 残差的关系。

更具体地，原 $\Phi_k''$ 不随 primitive 加常数而改变，而 (4)
使用了原点中心化与 norm-two 负类型之间的准确差值。
要从原三条曲线中央零推出与 (4) 冲突，还须独立约束这个完整
primitive 观察，包括 (20) 的全部三块。
不能把四个 (18) 再计成四条独立于原两曲线的零条件。

## 精确证书

- [脚本](../scripts/check-nonbeta-normtwo-constants-original-octic.py)
  与 [完整输出](../scripts/check-nonbeta-normtwo-constants-original-octic.json)
  给出九条全纤维 trace 多项式、实际 $4\times9$ 矩阵、前四列行列式、
  两条原 companion 的全部反解，以及原质量与 norm-two 常数符号核对。
- R253 固定四个非零对数常数和完整 norm-two 归一；R246 固定原 dyadic
  相位；R251/R254 固定相邻 CM5、四条原八次线和全部中央连接；
  R260 固定 canonical norm-two lift，并说明本篇避开的纯拉回秩一界。
- 计算只在固定数域中进行；未使用目标素数样本，也未把有限源可逆性
  当作中央非零结论。
