# R791 — 同一 q 的 J 深浅负一行、两个有限算术分量与真实 E 双块

日期：2026-11-15。**状态：已证明。**

本篇完成 R786 的原 J-only 条件负一行。使用同一个 $q_N^*$、同一个 R773 正矩生成器和已经算出的第一返回项；新公开读取只增加其完整 CM13 投影。两条原算术幅度在旧普通射线的相对密度一子族上，均对全部 $N\in4\mathbf Z_{>0}$ 为单位。整个 primitive 三维块保留。

所得结论不只是一条局部非零。原 $J$ 深、浅两个 $t/Y$ 单位行在 $\overline{\mathbf Q}$ 上线性独立；R785 把它们准确送回同一个原三维深域内的物理 $E$ 深、浅双块。对原混合 T 中央，两个完整外部仍须承担这些首系数及全对数尾，本文没有删除补偿。

## 1. 原条件来源与正确共同系数

记
$$
\lambda=-\bar\pi_0^{-1},\qquad\beta=-\lambda,\qquad
\kappa=p\lambda^2,\qquad u=\kappa^N,\qquad
b=17,\qquad N\in4\mathbf Z_{>0}.
\tag{1}
$$
原 $q=q_N^*$、$B_0$、$Y,P,t,J$、$E$ 和所有整格均为 R786 的原定义。
其实际 J 条件来源是
$$
\boxed{
\Omega^{-1}Y_*(t\,1_{J\in p^N}qB_0)
=\lambda^N\beta^N\mathcal L_N^J,\qquad
\mathcal L_N^J=Y_*(\widetilde\Phi_N(u)\mathcal M_5).
}
\tag{2}
$$
$\widetilde\Phi_N(u)$ 是 R786(17) 保全部六支、原 E 次数逆及 M-unit 第二项的完整多项式。
本篇没有加帽的 $Z_0$ 深事件，也没有作 R773 的 $U^{300}$ 失败扣除。
因此共同系数是 $\lambda^N\beta^N$，不是该旧帽来源的
$\lambda^{2N}\beta^N$。

以 R767 的五基
$$
\Xi_j=-b^j\sigma_b^{34}x_b^{13-3j}y_b,\qquad 0\le j\le4,
\tag{3}
$$
和原单位三角 reader $\mathbb T$，完整坐标为
$$
c_N=\mathbb T^{-1}
 \left(
 \frac{\int Y^{5+6i}\widetilde\Phi_N(u)\,d\mathcal M_5}
 {b^i(5+6i)!\Omega^{5+6i}}
 \right)_{i=0}^{4}.
\tag{4}
$$
原六输入总正次数不超过60。
所有 E 次数逆、quarter、原50行及最后两条核修正均未改动。
$P_{d,N}$ 的 $\lambda,\kappa,u,\eta$ 依赖也未冻结为辅助数。

R732 的原整个 CM13 分解给
$$
\boxed{
\mathcal L_N^J
=A_{\omega,\eta}(\lambda,\kappa,u)D_{\omega,b}
 +A_{-,\eta}(\lambda,\kappa,u)D_{-,b}
 +\mathcal L_{{\rm prim},N}.}
\tag{5}
$$
两条线按 R735 的原首 $z^5$ 系数1规范；
完整 primitive 块的特征多项式为 $T^3+\omega$。
没有因辅助数值中某个投影为零而从(5)删去它。

## 2. 真实公开执行与准确两幅度

本次仅兼容包装原 R773 producer，在其已算出的 raw0、raw1 后读取
oddSource(raw0)、oddSource(raw1)。原 source generator、reader、适配逆与全部门均未重定义。

- producer：[check-r791-j-only-arithmetic-amplitudes.js](../scripts/check-r791-j-only-arithmetic-amplitudes.js)；
- 参数：--max-block=4 --taus=2,3 --with-b --b-g-blocks=3 --neutral-degree=12；
- source commit：747bd324bdac56a9025f9c5f92c71f5974390145；
- [公开 run 43735795943](https://github.com/Rogerhu12/math-research-public/actions/runs/43735795943)，job132878022152；
- producer SHA256：0b61ceb2c2f4aadd97eee6719f2471273f99c3d4ee4c4402fd9676646b60a43b；
- 被调用 R773 producer SHA256：a8d5b436e383831f418b04f546d6d18d7c1b13cde3f5a9d81694f692a7aec5b7；
- 原 R719 producer SHA256：29bd414c63ac4fdca93ae4b56ccdf2ccaa2114395bf96a52d2e8fd1ea809fdb2；
- stdout9370字节，SHA256：1b72924f31179c7d8ee13689297ebf0293cfc801feb1a7d2270ed90a710639a6；
- exit code 0，全部实际旧行通过；无本地数值执行，无生成输出入库或Release。

规范为 $\mathbf F_{1009}$、$\omega=374$、$b=\Omega=1$、
$\lambda=(1-\tau)/\tau$、$\kappa=u=0$。
读取的是 first_return_spectrum，两个幅度准确为：

| $\tau$ | $\eta$ | $A_{\omega,\eta}(\lambda,0,0)$ | $A_{-,\eta}(\lambda,0,0)$ |
|---:|---:|---:|---:|
| 2 | $+1$ | 10 | 373 |
| 2 | $-1$ | 363 | 253 |
| 3 | $+1$ | 790 | 947 |
| 3 | $-1$ | 493 | 678 |

CM13 的相应特征值分别是 $-\omega^2$ 与 $-1$。
输出同时保完整五坐标及第二返回项，未将 R773 的条件两幅度代入这里。
原 a=629、第二测试系数240、真实规范 $\mathfrak j_2=319$，
以及原50行、quarter行和两核列均与旧运行一致。

四个辅助点的 primitive 块确为零，但本文没有把这些有限零值升为特征零恒等式。
以下只用显示非零值来证明四个固定有理分子不是零多项式。

## 3. 实际 CM 参数上的单位幅度，包含全部 N

由(4)和原 P 的生成算法，每个 $A_{\omega,\eta}$、$A_{-,\eta}$
是 $K(\lambda,\kappa,u)$ 中的明确有理式，$\eta=\pm1$ 分别处理。
分母来自原 R734 两级整逆、原 E 次数逆、固定五阶 reader、
完整 CM13 投影及原整数几何。
所有 $\Omega$ 幂在(4)中消去；恢复 $b=17$ 使用(3)的同一齐次规范。

清分母后，表中非零值证明
$$
A_{\omega,\eta}(L,0,0),\qquad A_{-,\eta}(L,0,0)
\tag{6}
$$
的四个固定 $K[L]$ 分子均非零。
这里的辅助 $\tau$ 不必来自原普通射线；
它只证明这个固定代数函数不是零函数。

将四个分子和全部固定分母的 Norm 多项式加入
[固定 CM 单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)
的有限乘积，代入 $L=-1/\bar\pi_0$。
删去固定有限分母素数及 $O(\sqrt X\log X)$ 的坏 CM 素数后，
原完整射线仍有相对密度一子族。
没有重定义 R558 的固定大模数，也不新增射线。

实际 $\kappa=p\lambda^2$、$u=\kappa^N$ 均在 $p\mathcal O$。
原分母在 $\kappa=u=0$ 为单位，故在上述同一子族上，
**两种 $\eta$、全部 $N\in4\mathbf Z_{>0}$ 同时**有
$$
\boxed{
A_{\omega,\eta}(\lambda,\kappa,\kappa^N)\in\mathcal O^\times,\qquad
A_{-,\eta}(\lambda,\kappa,\kappa^N)\in\mathcal O^\times.}
\tag{7}
$$
同一结论也在 $u=0$ 成立。
有限辅助点没有被直接当作实际 p；(7)是密度引理与真实整逆给出的提升。

## 4. 原 J 深负一非零：保所有 primitive 点因子

为统一周期，写
$$
\mathbb I_\omega=\Omega\int_{Y\ {\rm unit}}Y^{-1}d\nu_{D_{\omega,b}},
\qquad
\mathbb I_-=\Omega\int_{Y\ {\rm unit}}Y^{-1}d\nu_{D_{-,b}},
$$
$$
\mathcal I_p^J(u)
=\Omega\int_{Y\ {\rm unit}}Y^{-1}d\mathcal L_N^J .
\tag{8}
$$
式(8)右端中的 $N$ 只通过原有理式的 $u=\kappa^N$ 进入。

R735 支付两条原 rank-one 曲线的完整 Schwartz、period/Euler 与
同一个 $\Omega$ 下的点对数公式；$\mathbb I_\omega,\mathbb I_-$
非零，并在 $\overline{\mathbf Q}$ 上线性独立。
R761 支付整个 primitive 三维块的负一值及其准确 cyclic9 点域，
包括其中可能为零的值。
原两条 cubic 点与 primitive exact-order9 点由真正 point-factor 惯性投影分开；
等价地，先在固定 cyclic9 点域作2惯性平均，再分两条 cubic 标签。

因此将同一个一变量 unit 泛函作用于(5)合法给
$$
\mathcal I_p^J(u)
=A_{\omega,\eta}(\lambda,\kappa,u)\mathbb I_\omega
 +A_{-,\eta}(\lambda,\kappa,u)\mathbb I_-
 +\mathbb I_{{\rm prim},N}.
\tag{9}
$$
所有系数均在 K，绝非任意 $\mathbf C_p$ 系数。
原 $\lambda=-\bar\pi_0^{-1}$、$\kappa=p\lambda^2$、$u=\kappa^N$
全是固定嵌入下的代数数；它们可以随 p、N 变化而不影响有限点对数单射。

(7)和完整点分离推出
$$
\boxed{
\mathcal I_p^J(\kappa^N)\ne0,\qquad
M_N^+:=\int_{\substack{Y\ {\rm unit}\\J\in p^N}}
          \frac{t}{Y}q_N^*\,dB_0
=\lambda^N\beta^N\mathcal I_p^J(\kappa^N)\ne0 .}
\tag{10}
$$
这是同一个 q、原 J 条件、原 Y-unit 域的结论。
它不是把裸 $D_\omega$ 代入另一个条件域，也不依赖原 $I_{f_1,-5}$。

## 5. 原 J 浅行也非零，且两行代数线性独立

定义其实际全补域
$$
M_N^-:=\int_{\substack{Y\ {\rm unit}\\J\notin p^N}}
          \frac{t}{Y}q_N^*\,dB_0,\qquad c=-22/21 .
$$
R767 的整个原首 t 来源给出准确总和
$$
\boxed{
M_N^++M_N^-=c\,\beta^N\mathbb I_\omega .}
\tag{11}
$$
因此
$$
\boxed{
\begin{aligned}
\beta^{-N}M_N^+&=\lambda^N\mathcal I_p^J(\kappa^N),\\
\beta^{-N}M_N^-&=c\mathbb I_\omega-\lambda^N\mathcal I_p^J(\kappa^N).
\end{aligned}}
\tag{12}
$$
浅支的 $D_-$ 系数准确为 $-\lambda^NA_{-,\eta}$，由(7)非零；
它不能被 $D_\omega$ 或 primitive 项抵消。故 $M_N^-\ne0$。

更强，若 $\alpha M_N^++\gamma M_N^-=0$，其中
$\alpha,\gamma\in\overline{\mathbf Q}$，在同一个有限 point-log 空间先投 $D_-$，
得到
$(\alpha-\gamma)\lambda^NA_{-,\eta}\mathbb I_-=0$，所以 $\alpha=\gamma$。
再用(11)，得到 $\alpha c\mathbb I_\omega=0$，因而 $\alpha=\gamma=0$。
于是
$$
\boxed{M_N^+,M_N^-\ \text{在 }\overline{\mathbf Q}\text{ 上线性独立}.}
\tag{13}
$$

其两个已知算术分量的实际系数矩阵是
$$
\begin{pmatrix}
\lambda^NA_{\omega,\eta}&\lambda^NA_{-,\eta}\\
c-\lambda^NA_{\omega,\eta}&-\lambda^NA_{-,\eta}
\end{pmatrix},
\qquad
\boxed{\det=\frac{22}{21}\lambda^NA_{-,\eta}\in\mathcal O^\times .}
\tag{14}
$$
矩阵以 $\mathbb I_\omega,\mathbb I_-$ 为列；未称这两个值或点对数归一常数本身为单位。
未展示的 primitive 列在两行中准确相反，证明并未删除它们。
(13)只陈述这两条有限负一值，不把后续完整对数积分也宣称为代数线性独立。

可另附同一个 t-unit 条件。因原 $B_0$ 的 t 核为 $\beta$，
且 q、J、Y 均被 t 缩放固定，
$$
\boxed{
\int_{\substack{Y,t\ {\rm unit}\\J^{\pm}}}\frac tYq\,dB_0
=(1-\beta\kappa)M_N^\pm .}
\tag{15}
$$
这里 $J^+$ 表示深 N，$J^-$ 表示其完整浅补集；
$1-\beta\kappa$ 是单位。两条 t-unit 行仍保持(13)。

## 6. 返回原三维深域的两个真实 E 块

置
$$
\mathscr V_r=\{Y,P,t\in p^r\},\qquad r\ge N,\quad r\in2\mathbf Z.
$$
物理 E 的原固定截距为
$$
E=-\frac{17(25+48\omega)}{144}Z_0+(17+3\omega)t-\frac{1841}{72}J.
$$
R785/R786 已支付全三态与同 q 的返回：
在 $\mathscr V_r$ 上归一三个观察后，E 深 N准确对应 J 深 N，
E 浅 N准确对应 J 浅 N。故
$$
\boxed{
\begin{aligned}
\mathcal M_{r,N}^\pm
 &:=
 \int_{\substack{\mathscr V_r,\ E^\pm\\Y/\kappa^r\ {\rm unit}}}
 \frac{t/\kappa^r}{Y/\kappa^r}\,q\,dB_0\\
 &=\lambda^{3r}M_N^\pm .
\end{aligned}}
\tag{16}
$$
式(16)是原物理 E 的两条不交域，没有将 $E_\perp$ 改称 E，
也没有增加 P-unit、W-unit 或一个不存在的 CD 条件。
它们均非零，且在 $\overline{\mathbf Q}$ 上线性独立。
若附 $t/\kappa^r$-unit，则两行同乘(15)的单位。

所以(13)确已回到原完整来源上的两块，不是只存在于一个辅助 marginal。
但这两块仍只是原中央总行的真实部分。

## 7. 有限 carrier 的深度极限与严格赋值

现在固定满足(7)的一个实际 p，并固定该 p 的原分支 $\eta=\eta(p)\in\{\pm1\}$；以下 N 极限中不改变这个分支。
先去掉显示的 $\lambda^N\beta^N$ 单位相位。
R786 的固定五维有理坐标在 $u=0$ 正则且整，因此
$$
\mathcal I_p^J(\kappa^N)=\mathcal I_p^J(0)+p^N\mathcal O .
\tag{17}
$$
(7)也在 $u=0$ 成立，故同一有限点分离给
$\mathcal I_p^J(0)\ne0$。
置
$$
v_p^+=v_p(\mathcal I_p^J(0))<\infty .
$$
对全部足够大的原 $N\in4\mathbf Z$，
$$
\boxed{v_p(M_N^+)=v_p^+.}
\tag{18}
$$
这里只在同一个五维来源中按代数有理系数取极限，没有把 point-only 投影当作
$\mathbf C_p$ 连续算子。

浅支的(12)还含 $\lambda^N$，它一般不在所有 N 上收敛。
本文不将它免费设成1。可以选明确合法的共尾子列
$$
N_j=4(p-1)p^j,\qquad j\ge0 .
\tag{19}
$$
由于 $\lambda\in\mathbf Z_p^\times$，有
$\lambda^{N_j}=1+p^{j+1}\mathcal O$。
又 $\kappa^{N_j}\in p^{N_j}\mathcal O$。从而
$$
\beta^{-N_j}M_{N_j}^-
=c\mathbb I_\omega-\mathcal I_p^J(0)+p^{j+1}\mathcal O .
\tag{20}
$$
极限的 $D_-$ 系数为 $-A_{-,\eta}(\lambda,\kappa,0)$，仍为单位，
所以极限非零。令
$$
v_p^-=v_p(c\mathbb I_\omega-\mathcal I_p^J(0))<\infty .
$$
对足够大的 j，
$$
\boxed{
v_p(M_{N_j}^-)=v_p^-,\qquad
v_p(M_{N_j}^+)=v_p^+.}
\tag{21}
$$
所有极限系数在固定有限 carrier 中趋向明确的代数系数；
没有以无限 p-character 点池替代此论证。
(13)对全部 N 成立，只有浅支的统一赋值(21)使用该子列。

## 8. 同 E 门的完整 T 外部：非零首项与原中央补偿

保 R786 的原完整观察
$$
W^{[-r]}=b_Y\kappa^{-r}Y+Z_0-at .
$$
定义实际共同深块返回
$$
\mathcal D_N^\pm(z,w)
=\int f_w(b_YY+z(Z_0-at))\,d\mathfrak F_{B_0,N}^{\pm},
$$
及完整外部
$$
\mathscr R_N^\pm(r,w)=
\int_{\substack{Y\in p^r,\ E^\pm\\\mathscr V_r^c}}
 f_w(W^{[-r]})\,q\,dB_0 .
$$
q、所有 unit 条件、物理 E 和伙伴都与 R786 相同。
准确恒等式是
$$
\boxed{
\mathscr R_N^\pm(r,w)
=\lambda^r C_N^\pm(w)
 -\lambda^{3r}\mathcal D_N^\pm(\kappa^r,w),}
\tag{22}
$$
其中
$$
C_N^+(w)=\frac{\lambda^{2N}6\delta}{c_B}J_T(w),\qquad
C_N^-(w)=\frac{(\beta^N-\lambda^{2N})6\delta}{c_B}J_T(w).
\tag{23}
$$
不是给两个外部另加一个独立零。

在 $z\in p\mathcal O$，移动观察 unit 准确等价于 Y-unit。
原 T 特征使不含 t 的整条来源为零，故质量为零，
而完整导数保 R786(37) 的全部负幂级数。
其首项是
$$
\boxed{
\partial_w\mathcal D_N^\pm(\kappa^r,0)
=-\frac{d_pa}{b_Y}\kappa^r M_N^\pm+p^{2r}\mathcal O .}
\tag{24}
$$
没有将(24)当作整个 Mellin 函数，也没有向全对数尾施加点惯性投影。

当 $r>v_p(M_N^\pm)$ 时，(24)非零且赋值恰为
$r+v_p(M_N^\pm)$。
特别，对(19)中足够大的 j及每个偶 $r\ge N_j$，
$$
\boxed{
v_p(\partial_w\mathcal D_{N_j}^{\pm}(\kappa^r,0))
=r+v_p^\pm .}
\tag{25}
$$
如果原 $J_T'(0)=0$，(22)给
$$
\boxed{
(\mathscr R_{N_j}^\pm)'(r,0)
=-\lambda^{3r}\partial_w\mathcal D_{N_j}^{\pm}(\kappa^r,0),\qquad
v_p((\mathscr R_{N_j}^\pm)'(r,0))=r+v_p^\pm .}
\tag{26}
$$
因此原两完整外部都必须承担非零补偿；它们没有因同一个 T 中央为零而各自归零。

(13)—(16)给出的是原第一法向有限行的非退化二行系统。
从它到整个对数外部的另一个独立关系仍需支付实际同域词或原第三来源。
原 R780/R784 的随 CM 分支逆 Y、E 浅参考项、R783 的全部 CD 失败和
帽/U 补域继续保留。本文不声称已由(26)完成主目标。

## 依赖

- [R732](R732-original-type-five-full-cm13-and-two-eigenlines.md)：原全五维 CM13 算子、两算术线与 primitive 块。
- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)：原两条负一值、全 period/Schwartz 和同一微分下的点对数。
- [R761](R761-primitive-type-five-ninth-order-characters-and-point-fields.md)：整个 primitive 三维块的点域与有限 point-factor 分离。
- [R767](R767-native-t-moment-and-complete-five-partner-boundary.md)：原整 t 首矩及 $-22D_\omega/21$。
- [R773](R773-native-common-hat-domain-and-five-conditional-moment-return.md)：同一正矩 producer、原全部返回项。
- [R785](R785-original-three-state-even-frames-and-exact-e-gate.md)：物理 E 截距、全三维偶深核。
- [R786](R786-original-j-depth-three-output-and-native-e-exteriors.md)：本篇两个真实 J 来源、全部门、finite carrier与完整外部式。
