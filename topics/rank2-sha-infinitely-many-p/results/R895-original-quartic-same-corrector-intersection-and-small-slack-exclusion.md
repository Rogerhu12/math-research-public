# R895 原同修正 quartic 提升的严格交数与低松弛排除

日期：2026-11-16。**状态：以下原 $\tau=1$ quartic 候选的完整 $p^3$ 必要条件及其低松弛排除已证明。结论对同一个原 $P,R,S$ 成立，不假设修正的全球有限类为零；没有排除全部 quartic 候选，也没有解决完整 $K_1$ 的指定尾像。**

本篇把[全部同一首修正的严格零纤维成本](../notes/2026-11-16-r872-all-correctors-intersection-cost.md)与同一个原 quartic 截面的有效除子预算联立。这里的维数松弛沿用[原二长预算](../notes/2026-11-15-critical-mod-three-smooth-cube-exclusion.md)的准确定义，允许负值；第 5 节单独说明三个长块的转换。

## 1. 完整原来源与同修正假设

保持 [R872](R872-actual-quartic-third-carry-and-central-first-digit.md)及[同一第二页修正的整段证明](../notes/2026-11-16-r872-factored-corrector-last-row-and-residual-branches.md)(1)–(6)的原规范。具体为
$$
p=6s-1>211,\qquad r=3,\qquad \tau=1,\qquad
s=2h+2,\qquad 1<\ell\le h-1,\qquad h<s-4 .
\tag{1}
$$
于是 $h\ge17$。保同一个原 canonical 来源格 $\mathcal W_D$，
全部十九角和 $Y$ 帽；另保 $D\ge4b$、$p>D+40$ 及原 $f_D<p$ 的单位范围。

设原约化候选为
$$
\bar P=t^3F^4q,\qquad b=\deg_YF,\qquad
\deg_YF(0,Y)=3,
\tag{2}
$$
且
$$
F(0,1)=0,\qquad e_0=(EF)(0,1)\ne0,\qquad
q(0,1)\ne0,\qquad E=Y\partial_Y.
$$
$C=(F=0)$ 表示原曲面 $X$ 上的几何整、非边界严格变换。
原点记为 $P_0=(0,1)$；其单位支为 $Y=\psi(t)$。
原实际接触满足
$$
F(t(w),\bar g(w))=w^hu(w),\qquad
u_0\ne0,\qquad t(w)=t_1w+O(w^2),\quad t_1\ne0.
\tag{3}
$$
这里 $\bar g$ 是保全部实际高轴的同一个轴。

取 [R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)支付了全部 Gauss 帽的整因子提升
$$
P^{\rm fact}=t^3\widetilde F^{\,4}\widetilde q\in\mathcal W_D.
$$
$\widetilde q$ 包含原固定分母框。假设存在同一个原来源中的 $R,S$，使
$$
\boxed{
M^{\rm orig}(P^{\rm fact}+pR+p^2S)\in p^3\Gamma_4.
}
\tag{4}
$$
这里是原物理 $M$，保完整 $P_{134}$、$c_*U_0$、charge 四十、三条十三行 carry 和第四短块。不能把 (4) 换成仅相对 $J$ 的首层，或只检查某个 native 标量行。

记
$$
B=B_D,\qquad \kappa=C^2,\qquad d_D=B\cdot C,\qquad
N_D=\dim\overline{\mathcal W}_D.
\tag{5}
$$
令 $j$ 为原残截面 $\bar P/F^4$ 沿严格负水平 $H_-$ 的准确零阶。
[原 quartic 负水平全范围](../notes/2026-11-16-r872-quartic-negative-horizontal-range-and-double-vanishing.md)已证明
$$
0\le j\le2.
\tag{6}
$$
这个 $j$ 来自同一原截面，不是可另选的辅助参数。

## 2. 不要求有限类为零的全修正交数

先重述并证明本篇使用的全 $R$ 交数，明确它不依赖任何
$\mathfrak o_D(R)=0$ 假设。

由 (4) 的完整精度和前述整段证明(9)–(10)，同一个约化 $R$ 满足
$$
t\mid R,\qquad t^2\nmid R,\qquad
\operatorname{ord}_{P_0}(R|_C)\ge s,
\tag{7}
$$
以及
$$
(ER)|_C=
-\frac{11C_0u_0^4}{a}w^{s-1}+O(w^s),\qquad
C_0=t_1^3q(0,1).
\tag{8}
$$
这里 $a,C_0,u_0$ 均为原单位，$p>211$ 保 $11$ 为单位。
特别 (8) 的首项非零。

[R815](R815-complete-original-mori-nef-cones-and-s-fibration.md)的严格零纤维与原零角给
$$
f_0=f-\sum_{\nu=1}^4E_{0,\nu},\qquad
C\cdot f_0=3,\qquad \kappa\ge6b-9\ge9.
\tag{9}
$$
$R$ 的实际截面零除子 $D_R\sim B$ 含一次 $f_0$。
这是原严格纤维的来源消失，不是从 raw 除以 $t$ 推出整个总纤维已被删除。

若 $F\nmid R$，则 $D_R-f_0$ 不含 $C$。
它在 $P_0$ 与 $C$ 的交数至少为 $s-1$，因为 $t$ 是
$C$ 在 $P_0$ 的参数。其余局部交数均非负，所以
$$
d_D-3=(D_R-f_0)\cdot C\ge s-1.
\tag{10}
$$

若 $F\mid R$，(8) 迫 $F^2\nmid R$。由同一 $t$-Gauss 除法可写
$R=tFH$，且 $H|_C$ 非零。限制 $ER=t(eH+FEH)$ 得
$$
\operatorname{ord}_{P_0}(H|_C)=s-2=2h.
$$
剩余有效除子 $D_R-f_0-C$ 不含 $C$，故
$$
d_D\ge \kappa+3+2h\ge s+2.
\tag{11}
$$
(10) 也给相同结论。因此无论 $R$ 是否含 $F$，
$$
\boxed{d_D\ge s+2.}
\tag{12}
$$
这个论证使用的是 (4) 中同一个 $R$。没有把 $R$ 投影到
$F$ 因子层，没有替换其有限纤维类，也没有重新选择法向修正。

## 3. 同一个 quartic 截面的有效除子成本

原 $\bar P$ 是 $B$ 的非零截面。由 (2)、(6)，其零除子包含
$$
\operatorname{Div}(\bar P)\ge4C+3f_0+jH_-.
\tag{13}
$$
三个所列分量互不相同。尤其 $t^3$ 在严格零纤维的一般点给三，
$F(0,Y)\not\equiv0$ 保 $C$ 不是该纤维。
在 $f_0$ 与 $H_-$ 的交点，两个素除子的系数仍真实相加；
不能以单点总零阶的最大值替代 (13)。

[R680](R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)
的完整十九重数表与 nef 性给
$$
B\cdot f_0=2,\qquad B\cdot H_-=4,\qquad B\ \text{nef}.
\tag{14}
$$
因此将 (13) 与同一个 $B$ 相交，全部剩余有效分量贡献非负：
$$
B^2\ge4d_D+6+4j.
\tag{15}
$$
结合 (12)，得到本篇首个必要条件：
$$
\boxed{
M^{\rm orig}(P^{\rm fact}+pR+p^2S)\in p^3\Gamma_4
\quad\Longrightarrow\quad
B_D^2\ge4s+14+4j.
}
\tag{16}
$$
式 (16) 对假设范围内的所有原 $R,S$ 成立。
它与只在 $\mathfrak o_D(R)=0$ 时成立的更强条件不同；
此处没有先对未知有限类作归一化。

## 4. 原 canonical 维数的准确整门

原格的准确维数与自交身份是
$$
N_D=\sum_{n=0}^D(e_{n+1}+1),\qquad
\boxed{B_D^2=2N_D-2D-17.}
\tag{17}
$$
这是[原二长预算证明](../notes/2026-11-15-critical-mod-three-smooth-cube-exclusion.md)(4)
已经使用的整数身份，也见[同来源轨道证明](../notes/2026-11-15-cube-factor-orbits-and-even-critical-reduction.md)(9)。

为核对这里没有替换来源，原十九重数中三个四步负链各有总重数
$D-2$，一个三步负链有总重数 $D-1$，两个二步正链各为
$(c_D,c_D)$，其中 $c_D=\lfloor D/2\rfloor$。
置 $u_D=2c_D+4$，则
$$
\sum\nu_{i,a}=4D+4c_D-7,\qquad
-K_X\cdot B_D
=6D+2u_D-\sum\nu_{i,a}=2D+15.
\tag{18}
$$
式 (17) 与原逐 charge 的完整截面计数一致。
这里不从某个未证明的 nef 消失、物理像饱和或环境维数推导 (17)。

代入 (16) 得
$$
2(N_D-2s)\ge2D+31+4j.
$$
左边为偶整数，故准确有
$$
\boxed{N_D-2s\ge D+16+2j.}
\tag{19}
$$
取整常数为 $16$，不是 $15$。

现在沿用原二长预算的定义
$$
\boxed{\delta_D=N_D-(2s+\ell).}
\tag{20}
$$
$\delta_D$ 是有符号整数，可以为负；本篇不假设来源维数至少等于目标长度。
由 (19)，当前 quartic 的完整同修正提升必满足
$$
\boxed{\ell+\delta_D\ge D+16+2j.}
\tag{21}
$$

**低松弛排除。** 在第 1 节的全部原假设下，若
$$
\boxed{\ell+\delta_D\le D+15+2j,}
\tag{22}
$$
则不存在满足 (4) 的同源 $R,S$。
特别不预先读取 $j$ 时，统一的充分排除门是
$$
\boxed{\ell+\delta_D\le D+15.}
\tag{23}
$$

若另有准确的方阵二长预算 $\delta_D=0$，
则必要地 $\ell\ge D+16+2j$。
若一列输入满足 $\ell+\delta_D=o(D)$，
则从某项起 (23) 排除本篇的 quartic 完整 $p^3$ 提升。
这些是对额外预算条件的推论；并未断言当前所有输入都有
$\delta_D=0$、有界 $\ell$ 或次线性松弛。

## 5. 三个长块的预算不能套用 (23)

[R837](R837-original-three-long-root-energy-and-uniform-multiplicity-truncation.md)第 6 节明确区分旧二长预算和原四块的三个长块。
若为后者另定义
$$
\delta_D^{(3)}=N_D-(3s+\ell),
$$
则准确地
$$
\delta_D=\delta_D^{(3)}+s.
$$
同一个必要条件 (21) 在这套记号中只能写成
$$
\boxed{s+\ell+\delta_D^{(3)}\ge D+16+2j.}
\tag{24}
$$
不能将 (21) 中的 $\delta_D$ 直接换成 $\delta_D^{(3)}$。

例如，在 $3s+\ell=N_D+o(D^2)$、
$\ell=o(D^2)$ 的自然三长临界，$s\asymp D^2$，
(24) 不提供新的渐近排除。
在旧 $p/D^2\to47/8$ 的二长临界，
仅知道 $\ell,\delta_D=o(D^2)$ 也不足以推出 (22)：
本篇检测的是其中准确的线性松弛范围。
它没有把一个二长维数身份变成第三条未付的物理长行。

## 6. 与原待解余类的关系

(22) 直接排除本篇候选的完整 (4)，强于仅证明
$\mathfrak o_D(R)\ne0$；但排除依赖明确的低松弛门和
$r=3,\tau=1$ 的整段 normal 结论。
未满足 (22) 的候选仍须处理原全 $K_1$、$\ker\beta_1$ 的有限像，
以及同一 $R,S$ 的其余 normal、三条十三行和下一页。
一般非 quartic 首核也不在本篇范围。

证明未增加任何中央零条件，没有引入新的来源列，
没有删除十九角、连接类或原高尾。无数学数值运行。
