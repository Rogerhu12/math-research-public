# 实际 Abel 坐标、独立 Čech 切向及47进对数的证明接口

日期2026-11-12；qc_global。R121进行中的完整证明笔记。实际54方向矩阵和长乘仍在计算，本文先固定证明、符号和尺度；最终数值另由证书给出，未宣布非主高度或QC共同根完成。

## 1. 固定实际局部坐标

工作于 R102 的良约化曲线 $X/\mathcal O_L$，$L/\mathbb Q_{47}$ 为未分歧二次扩张。$g=54$，$\mathcal L=K_X+D$ 次数126，$V_1=H^0(\mathcal L)$ 维73；$V_2=H^0(\mathcal L^2)$ 维199。所有以下全局截面均在原来的820点评价模型中。

令 $v_0$ 是 R102 单位评价基 $s_1,\ldots,s_{73}$ 的第一列，$C$ 是另外72个主元评价点之和。准确单位矩阵给
\[
H^0(\mathcal L(-C))=\langle v_0\rangle.
\]
实际检查 $v_0$ 在其余748个评价点全为单位。写 $(v_0)_1=C+D_*$，则 $\deg D_*=g$，$h^0(D_*)=1$。

即使 $D_*$ 非约化，序列
\[
0\longrightarrow\mathcal O_X\longrightarrow\mathcal O_X(D_*)
\longrightarrow\mathcal O_{D_*}(D_*)\longrightarrow0
\]
也给出 Abel 映射切映射
\[
H^0(\mathcal O_{D_*}(D_*))\longrightarrow H^1(\mathcal O_X).
\]
前两个 $H^0$ 都为一维，且 Riemann–Roch 给 $H^1(\mathcal O(D_*))=0$，因此该映射是同构。这证明 $\operatorname{Sym}^{54}X\to\operatorname{Pic}^{54}X$ 在 $D_*$ 附近 étale，不需要猜测残余点的分解型或重数。

对 $P=[E-D_0]$ 取唯一截面线
\[
s_E\in V_2(-E-C),\qquad(s_E)_2=E+C+D_E.
\]
则 $[D_E]=[D_0-C]-P$，所以 $D_E$ 是上面的局部 Abel 逆。它只依赖 $P$，不依赖有效代表 $E$。以
\[
U(P)=H^0(\mathcal L^2(-C-D_E))
\]
的完整73维理想并在固定73个单位行上规范化，得到 $f(P)$。

该理想线丛次数126，因而全局生成。若 $D_E$ 的一阶形变非零，选一个在相应支撑点为单位的理想截面，就能检测该形变；故完整截面理想给出的 Grassmann 映射是局部浸入。这在 $C$ 与 $D_E$ 相交时仍成立，因为固定的 Cartier 理想 $\mathcal I_C$ 可逆。

当 $E$ 避开所有评价点时，$s_E$ 仅需在删去固定 $C$ 的748行上取倒数。实际翻转的全局乘法式次数至多504，小于748，故这些评价条件仍准确地识别全局理想。$C$ 处的零行由全局系数恢复。

## 2. 真正移动点的第一种计算

选择 $P_j$ 不在 $C$ 中，使 R110 的54个典范截面的评价矩阵有54阶单位子式。选实际 $v_j\in V_1$ 满足
\[
v_j(P_j)=0,\quad v'_j(P_j)\in\mathcal O_L^\times,
\quad v_j(T)\in\mathcal O_L^\times\quad(T\neq P_j).
\]
令 $E_j=(v_j)_1$。这是一个真实零类代表，$[E_j-D_0]=0$；它在 $P_j$ 的重数恰为一。

再选 $t_j\in V_1(-P_j)$。令 $U=v_jV_2$，施加 $t_jw\in U$。若 $G=\gcd((v_j)_1,(t_j)_1)$，核为
\[
H^0(2\mathcal L-E_j+G),\qquad\dim=73+\deg G.
\]
实际125阶单位秩强制 $\deg G=1$，而已知 $G\geq P_j$，所以完整74维核恰为
\[
I_j=H^0(2\mathcal L-E_j+P_j).
\]
在这个空间施加真正圆盘 $P_j(\epsilon)$ 的值，使用 R102 同一族
\[
E_t:y^2=x^3+x+32+t,
\qquad\epsilon^2=0,
\]
的实际一阶41挠点和模形式展开，得到
\[
H^0(2\mathcal L-E_j+P_j-P_j(\epsilon)).
\]
该空间表示真实的 $[P_j(\epsilon)-P_j]$。整模型中两项支撑不相交，单位一阶值确保长度一条件，不是只取支撑并集。

将这个双数点送入 §1 的固定坐标时，因零代表 $E_j$ 含 $P_j$，额外删去该行，使用747行作无除零的翻转；747仍大于504。零阶规范矩阵必须**逐项**等于固定 $f(0)$。双数系数就是 $d f_0$ 在真正 Abel 切向上的值。

## 3. 独立 Čech 公式

这一节不用双数 PicChart 的翻转，提供独立的全部切向公式。

固定一个 $P=P_j$，局部参数为实际 $t=B-32$。由 §2 的完整74维空间可取
\[
\tau\in H^0(\mathcal L(P))
\]
在 $P$ 的主部为 $1/t$。具体取 $w\in I_j$、$w(P)$ 为单位，令
\[
\tau=\frac{v'_j(P)}{w(P)}\frac{w}{v_j}.
\]
由于 $w$ 沿 $E_j-P$ 消失，$\tau$ 在其它所有点没有极点；这不依赖知道 $E_j-P$ 的分解。

取 $s_C\in V_1$ 插值 $\tau$ 在72个点 $C$ 的值，并令其在被省略的第1个基坐标为零。于是
\[
R_P=\tau-s_C\in H^0(\mathcal L(P)(-C)),
\]
其主部仍为 $1/t$。

记 $a(\epsilon)=[P(\epsilon)-P]$。在 $P$ 的圆盘与其补集交上，$\mathcal O(P(\epsilon)-P)$ 的局部生成元是
\[
\frac{t}{t-\epsilon}=1+\frac\epsilon t.
\]
因此对 $s\in V_1$，
\[
s_\epsilon=s+\epsilon s(P)\tau
\]
给 $\mathcal L\otimes a(\epsilon)$ 的截面；相反
\[
v_\epsilon=v_0-\epsilon v_0(P)R_P
\]
给 $\mathcal L\otimes a(\epsilon)^{-1}$ 中沿 $C$ 消失的截面。这固定了正负号。
其乘积为全局 $\mathcal L^2$ 截面，且第一导数是
\[
\boxed{\delta_s=
\tau\bigl(v_0s(P)-v_0(P)s\bigr)
+v_0(P)s_Cs.}\tag{3.1}
\]
括号在 $P$ 为零，恰消掉 $\tau$ 的极点；所以
\[
\boxed{\delta_s(P)=v'_0(P)s(P)-v_0(P)s'(P)
+v_0(P)s_C(P)s(P).}\tag{3.2}
\]
所有其它评价点直接用 (3.1)。在 $C$ 上两项都消失。

令 $(v_\epsilon)_1=C+D_\epsilon$，则 $[D_\epsilon]=[D_*]-a(\epsilon)$，恰与 §1 的坐标对应。73个乘积 $v_\epsilon s_\epsilon$ 在零阶给完整基 $v_0V_1$，因此给完整 $U(a(\epsilon))$。

设 $C_0$ 为零点固定73行的逆，$U_0=(v_0W)C_0$。将 (3.1) 的73列组成 $\delta$，则规范化理想的第一导数为
\[
\boxed{\delta f=\delta C_0-U_0(\delta C_0)[S_{\rm chart}].}\tag{3.3}
\]
独立复核器还检查全部820行的 $\delta$ 满足
\[
V_2\,\delta[S_2]=\delta.
\]
因此不是只验证最终选取的54个标量；它明确检查了极点消去后确实是一条全局截面。

首个实际方向上 (3.3) 已与 §2 的双数计算在1460个候选坐标逐项相同。全54方向的相同验证由 `verify_p41_abel_tangents47.py` 执行；其矩阵算术采用 R117 已独立验证的精确整数环，但几何算法与生成器不同。

## 4. 不能省略的 Kodaira–Spencer 尺度

R102 以短 Weierstrass 模型的 $\omega=dx/(2y)$ 计算权一形式，再取二次乘积。R110 的节点Tate模型严格给
\[
x=\frac{u}{(1-u)^2}+\frac1{12},\qquad
y=\frac{u(1+u)}{2(1-u)^3},\qquad\omega=\frac{du}{u},
\]
并给权一值 $e(u)=(1+u)/(2(1-u))$、归一化常数1。因此权二值确属这个 $\omega^2$ 规范。

记 $D=4A^3+27B^2$。与Tate的 $dq/q$ 规范一致的尺度是
\[
\operatorname{KS}(\omega^2)=\frac{9B\,dA-6A\,dB}{2D}.
\]
本次 $A=1,B=32+t$，故
\[
\beta(t)=-\frac3{4+27(32+t)^2},\qquad
\boxed{\beta(0)=-\frac3{27652}\equiv38\pmod{47}.}
\]
根代理正在把该公式的独立 Gauss–Manin 约化和 Tate 首项校准整理为 R123。校准证书必须显式保存这个有理数及模 $47^4$ 值。

令 $K_1$ 是R110典范包含矩阵。对54个所选点，真正全纯微分的切向值矩阵是
\[
\boxed{\Omega=\beta(0)\,(WK_1)[P_1,\ldots,P_{54}].}\tag{4.1}
\]
不能把原始权二值 $WK_1$ 直接当作 $dt$ 系数。点的选择可用未乘 $\beta(0)$ 的单位秩，因为它是共同单位；最后的微分矩阵和变换必须乘上它。

## 5. 从局部坐标的 Lie 向量到54个真正积分

把 §2 或 §3 算出的54个 Abel 切向排成行矩阵 $D_f$。选择54个实际坐标 $I$，并验证
\[
D_I=D_f[:,I]
\]
有单位行列式。这个单位矩阵是计算输出，不能由维数计数代替。

由于 $[P_j(t)-P_j]$ 的微分对数正是 $\Omega$ 的第 $j$ 行，任意 Lie 向量 $\ell$ 在所选局部坐标中的值 $\ell_I$ 对应
\[
\boxed{\bigl(\ell(\omega_1),\ldots,\ell(\omega_{54})\bigr)
=\ell_I D_I^{-1}\Omega.}\tag{5.1}
\]
右侧就是校准证书保存的准确转换。最终输出还检查R110典范基的实际半线性矩阵 $A_K$：对 $\mathbb Q_{47}$ 有理点，行向量 $z$ 必须满足
\[
zA_K=\overline z.
\]
固定的坐标除子 $C$ 本身无需在 $\mathbb Q_{47}$ 定义；(5.1) 将结果送回真正的全纯微分基后，再核验下降。

## 6. 形式群对数公式与精度

先定义 $F(P)=f(P)-f(0)$。令 $Y\in J_1$，$\ell=\log Y\in47\operatorname{Lie}J$。在整形式坐标上，平移不变向量场 $D_\ell$ 的系数在47倍整环中，故
\[
F(\exp\ell)=\sum_{n\geq1}\frac{D_\ell^nF(0)}{n!}.
\]
第 $n$ 项的47进阶至少 $n-v_{47}(n!)$；对 $n\geq4$ 均至少4。这给严格的模 $47^4$ 余项界，而不是形式地忽略未知高阶项。

因此
\[
\boxed{dF_0(\log Y)\equiv
\frac{2F(Y)-6F(-Y)+F(-2Y)}6\pmod{47^4}.}\tag{6.1}
\]
一次、二次、三次权分别为6、0、0，6是47进单位。没有减 $f(0)$ 时常数权为 $-3$，所以必须明确用 $F$。

对本次 $Y=\epsilon hB$，R102的实际局部因子给 $h\equiv9\pmod{47}$，且长乘程序还直接验证最终模47零类。故
\[
\boxed{\log B=\epsilon h^{-1}\log Y}
\]
不损失精度。随后用 (5.1) 得到54个真实积分，不能把未校准的59860个 Grassmann 坐标叫作这54个积分。

## 7. 实际文件和待完成计算

- `p41_evaluation_jets47.py/.gp` 及其独立标准库复核器：全部实际一阶展开已通过。
- `p41_abel_tangents47.py`：双数中的实际 Abel 切向；每5方向保存可恢复work。
- `verify_p41_abel_tangents47.py`：独立的 (3.1)–(3.3) 算法，另核全部全局截面和尺度。
- `p41_formal47_multiply.py`：304位真实长乘，每5位保存。
- `p41_formal47_chart.py`：固定代表无关坐标。
- `p41_formal47_log.py`：要求长乘完成及54方向单位校准后才执行 (6.1)、(5.1)，并核最终下降。

当前完整54方向、长乘与最终对数仍待相应程序完成；非主Poincaré高度和QC共同根继续保留为真实后续问题。
