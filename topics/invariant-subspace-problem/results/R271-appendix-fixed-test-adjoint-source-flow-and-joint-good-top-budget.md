# R271 附录：固定物理测试的真实伴随源流、正耗散与共同 good-top

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d；AI-assisted，GPT-6 Astra Pro。

状态：**以下原算子恒等式、全段正预算及共同切口选择已证明。**
固定同一个物理测试后，其真实 Riesz 源沿原左源流的伴随递推。
本文给该递推的受限正逆公式、每一步的两项投影耗散，以及全孔层
的平方和预算。将其与实际固定缺陷的原两费预算一起平均，可以在
同一个 good top 同时保留两费小量与一个固定有限测试空间的真实
测试源小量。

尚未证明这些测试源的完整右费小，也未给
[固定测试局部 Gram](R271-appendix-fixed-physical-tests-and-minimum-two-chain-local-gram.md)
的 $O(K_{\rm win})$ 上界。右修复中的真实误差仍完整保留。

依赖：

- [原左最小截断及 source Riccati](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)。
- [原源流准确负图及纤维](R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md)。
- [同源首头右度量](R239-appendix-first-source-head-metric-splitting-and-middle-band-schur-amplification.md)。
- [固定物理测试与最小双链局部 Gram](R271-appendix-fixed-physical-tests-and-minimum-two-chain-local-gram.md)。
- [同时保完整顶费的尾自适应联合余商](R271-appendix-tail-adaptive-joint-quotient-with-complete-top-cost-transport.md)。

## 1. 一个固定头与两种不同的源流

固定原 $m,d=2^m,A=A_m,D=D_m$，所有孔层保持这个 $m$。
取合法整数 $s<p\le Q$。记
$$
V_p=\mathcal H_{\le p}^{(m)}
 \cap\ker P_{\le p-1}^{(m)}(A+D),\qquad
E_pv=Av_p,
$$
$$
\mathscr R_p=\bigoplus_{i=0}^{d-2}e_i
 (\ker D^{d-i-1}\cap\mathcal H_p),\qquad
J_p=E_pE_p^*,\quad L_p=J_p^{-1},\quad U_p=E_p^\dagger.
\tag{1.1}
$$
这里 $U_p$ 是从原源到真正左最小者的映射。另记原零源核
$$
\mathcal K_p=\ker E_p=\ker(A+D)\cap\mathcal H_{\le p}^{(m)}.
\tag{1.2}
$$

相邻顶输入及真正受限算子为
$$
\mathscr X_p=\bigoplus_{i=0}^{d-1}e_i
 (\ker D^{d-i}\cap\mathcal H_p),\qquad
A_p=A|_{\mathscr X_p},\qquad
\mathcal D_p=D|_{\mathscr X_p}:\mathscr X_p\to\mathscr R_{p-1}.
\tag{1.3}
$$
其中 $\mathcal D_p$ 满射，且每个伴随均是这个实际受限映射的伴随。
置
$$
W_p=I+\mathcal D_p^*L_{p-1}\mathcal D_p,\qquad
X_p=W_p^{-1}A_p^*L_p,\qquad
T_p=-\mathcal D_pX_p.
\tag{1.4}
$$
原 source Riccati 给
$$
J_p=A_pW_p^{-1}A_p^*,\qquad
P_{\le p-1}U_p=U_{p-1}T_p.
\tag{1.5}
$$
$T_p$ 是原最小左向量的向下源流。

现在另固定一个物理测试 $f\in\mathcal H_{\le s}^{(m)}$。对所有
$p\ge s$，定义
$$
q_p=P_{V_p}f,\qquad k_p=P_{\mathcal K_p}f,
$$
$$
\boxed{g_p=U_p^*f,\qquad
t_p=J_pg_p=E_pP_{V_p}f.}
\tag{1.6}
$$
$t_p$ 恰是固定测试稿中的真正 Riesz 测试源。由于
$\mathcal K_p\subseteq V_p$，
$$
\boxed{U_pt_p=q_p-k_p,\qquad
\mu_p(t_p)^2=\|q_p\|^2-\|k_p\|^2\le\|f\|^2.}
\tag{1.7}
$$
这个向上的测试源族不是一个原顶部左最小者的物理截断源族。

由 (1.5) 取伴随，并用 $f$ 支持在 $\le s\le p-1$，准确有
$$
\boxed{g_p=T_p^*g_{p-1}.}
\tag{1.8}
$$
所以始终只测试同一个 $f$，没有在不同切口独立挑选较小的测试向量。

## 2. 真正测试源的受限正逆递推

在原 $\mathscr R_{p-1}$ 上置
$$
Z_p=J_{p-1}+\mathcal D_p\mathcal D_p^*\succ0,
$$
$$
\boxed{
v_p=\mathcal D_p^*Z_p^{-1}t_{p-1}\in\mathscr X_p,\qquad
e_p=J_{p-1}Z_p^{-1}t_{p-1}\in\mathscr R_{p-1}.}
\tag{2.1}
$$
所有逆在固定原参数下有界；没有把 $\mathcal D_p\mathcal D_p^*$
改成不带短核旗的环境压缩。

直接乘回得
$$
\boxed{t_{p-1}=\mathcal D_pv_p+e_p,\qquad t_p=-A_pv_p.}
\tag{2.2}
$$
第二式可以由 (1.4)、(1.8) 及准确恒等式
$$
W_p^{-1}\mathcal D_p^*L_{p-1}
=\mathcal D_p^*(J_{p-1}+\mathcal D_p\mathcal D_p^*)^{-1}
\tag{2.3}
$$
得到。为核对 (2.3)，将其右侧左乘
$I+\mathcal D_p^*J_{p-1}^{-1}\mathcal D_p$，所得为
$\mathcal D_p^*J_{p-1}^{-1}$；全部乘法顺序保留。

更具体地，真正正交投影满足
$$
\boxed{
(q_p)_p=-v_p,\qquad
P_{\le p-1}q_p=q_{p-1}-U_{p-1}e_p.}
\tag{2.4}
$$
证明：任意 $V_p$ 向量唯一按其顶层 $x\in\mathscr X_p$ 写成
$$
\bigl(k-U_{p-1}\mathcal D_px,\ x\bigr),
\qquad k\in\mathcal K_{p-1}.
$$
投影固定 $f$ 时，先对 $k$ 极小化得到 $k=k_{p-1}$；
其余准确目标为
$$
\|x\|^2+\mu_{p-1}(t_{p-1}+\mathcal D_px)^2
$$
加上一个与 $x$ 无关的常数。正规方程给 $x=-v_p$。
再用 $t_{p-1}-\mathcal D_pv_p=e_p$，即得 (2.4)。

这里 $e_p$ 是必须保留的原源误差。特别，后续的 $v_p$ 不能因
范数小就被视为 $t_{p-1}$ 的完整右链。

## 3. 两种正投影耗散

### 3.1 左可行投影的损失

由 (2.4)，旧投影在新顶层补零后与新投影之差为
$$
q_{p-1}-q_p=(U_{p-1}e_p,\ v_p).
$$
原 $V_p$ 包含于
$V_{p-1}\oplus(\mathbb C^d\otimes\mathcal H_p)$，而 $f$ 的新顶层为零。
故 $q_p=P_{V_p}q_{p-1}$，从而有准确 Pythagoras：
$$
\boxed{
\|q_{p-1}\|^2-\|q_p\|^2
=\mu_{p-1}(e_p)^2+\|v_p\|^2
=\langle Z_p^{-1}t_{p-1},t_{p-1}\rangle.}
\tag{3.1}
$$
最后的等号也可用 $Z_p=J_{p-1}+\mathcal D_p\mathcal D_p^*$ 逐项相乘。
这是沿同一测试的正损失，不把 $V_p$ 在整个环境中误称为嵌套空间。

### 3.2 零源核的准确首头增量

令
$$
E_{h,r}=\ker D^h\cap\mathcal H_r,\qquad
R_{p-1}=(D:\mathcal H_p\to\mathcal H_{p-1})^\dagger,
$$
$$
K_{p-1}^{\rm tail}
=(R_{p-1}|_{E_{d-1,p-1}})^*R_{p-1}|_{E_{d-1,p-1}},
$$
并令 $\iota_0:E_{d-1,p-1}\to\mathscr R_{p-1}$ 嵌入第零源头。
定义真实首头桥
$$
\mathcal H_pz=U_{p-1}\iota_0z-e_0R_{p-1}z,
$$
其中两项分别支持在 $\le p-1$ 与第 $p$ 孔。它是原完整零源向量，
且
$$
\mathcal H_p^*\mathcal H_p
=N_{0,p}:=K_{p-1}^{\rm tail}+\iota_0^*L_{p-1}\iota_0.
\tag{3.2}
$$

准确的正交分解为
$$
\boxed{
\mathcal K_p=\mathcal K_{p-1}
 \oplus e_0(\ker D\cap\mathcal H_p)
 \oplus\operatorname{Ran}\mathcal H_p.}
\tag{3.3}
$$
核对完整性：若 $z\in\mathcal K_p$，顶层满足 $Az_p=0$，
所以 $z_p=e_0h$。原短核旗给 $h\in E_{d,p}$。
唯一分解 $h=R_{p-1}a+h_{\rm prim}$ 中
$a=Dh\in E_{d-1,p-1}$，$h_{\rm prim}\in\ker D$。
低部分的源是 $-e_0a$，扣除其真正最小左原像后只剩
$\mathcal K_{p-1}$；因此得到 (3.3)。三个部分正交分别来自
真正左最小性、孔层正交及 $R_{p-1}a\perp\ker D$。
(3.2) 严格正，所以桥的像闭。

由于固定 $f$ 支持在 $\le p-1$，新 primitive 首头与 $f$ 正交。
桥的测试行则准确是
$$
\mathcal H_p^*f=\iota_0^*g_{p-1}.
$$
因此
$$
\boxed{
\|k_p\|^2-\|k_{p-1}\|^2
=\|N_{0,p}^{-1/2}\iota_0^*g_{p-1}\|^2.}
\tag{3.4}
$$
本节与原负源图使用完全相同的 $K_{p-1}^{\rm tail}+L_{00}$。
它没有把两费 $M_2$ 的头压缩代入这一位置。

## 4. 固定测试的准确伴随 Riccati 能量及全段预算

结合 (1.7)、(3.1)、(3.4)，得到
$$
\boxed{
\begin{aligned}
\mu_{p-1}(t_{p-1})^2-\mu_p(t_p)^2
={}&\|v_p\|^2+\mu_{p-1}(e_p)^2\\
&+\|N_{0,p}^{-1/2}\iota_0^*g_{p-1}\|^2.
\end{aligned}}
\tag{4.1}
$$
每一项都是同一个固定 $f$ 的原物理能量。相加即有
$$
\boxed{
\sum_{p=s+1}^{Q}
\left[
 \|v_p\|^2+\mu_{p-1}(e_p)^2+
 \|N_{0,p}^{-1/2}\iota_0^*g_{p-1}\|^2
\right]
=\mu_s(t_s)^2-\mu_Q(t_Q)^2
\le\|f\|^2.}
\tag{4.2}
$$
因此，用原 $\|A_m\|\le6$ 和 (2.2)，得到新的真实测试源预算
$$
\boxed{\sum_{p=s+1}^{Q}\|t_p\|^2\le36\|f\|^2.}
\tag{4.3}
$$
它对窗口总长度 $Q$ 无增长，也不含整个头逆的条件数。

(4.1) 还等价于原源空间上的准确正算子身份
$$
\boxed{
\begin{aligned}
J_{p-1}-T_pJ_pT_p^*
={}&J_{p-1}Z_p^{-1}J_{p-1}\\
&+\iota_0N_{0,p}^{-1}\iota_0^*.
\end{aligned}}
\tag{4.4}
$$
可直接验证它，而不只对已选 $f$ 推断：加权最小化给
$$
W_p^{-1}A_p^*L_pA_pW_p^{-1}
=W_p^{-1}
-\iota_{\ker A_p}
 (\iota_{\ker A_p}^*W_p\iota_{\ker A_p})^{-1}
 \iota_{\ker A_p}^* .
$$
左右乘 $\mathcal D_p,\mathcal D_p^*$，再用
$$
J_{p-1}-\mathcal D_pW_p^{-1}\mathcal D_p^*
=J_{p-1}Z_p^{-1}J_{p-1},
$$
以及 $\ker A_p=e_0E_{d,p}$ 上
$$
D_0(I+D_0^*L_{00}D_0)^{-1}D_0^*
=(K_{p-1}^{\rm tail}+L_{00})^{-1},
$$
即可得到 (4.4)。最后一式使用
$(D_0D_0^*)^{-1}=K_{p-1}^{\rm tail}$，没有交换非交换正块。

## 5. 固定有限物理测试空间的矩阵预算

现在固定
$$
\mathscr T_n=\operatorname{span}(e_0,\ldots,e_{n-1}),
$$
并取 $d\ge n$。这些整数坐标在当前分解中都位于尾真空，
故可同时作为以上所有 $f$ 的输入。

将 (2.1) 中的 $v_p,e_p$ 和 (3.4) 中的归一化首头行视为
从 $\mathscr T_n$ 出发的线性映射，定义正的 $n\times n$ 矩阵
$$
\Psi_p
=V_p^*V_p+\mathcal E_p^*L_{p-1}\mathcal E_p
 +G_p^*\iota_0N_{0,p}^{-1}\iota_0^*G_p.
\tag{5.1}
$$
此处 $V_pf=v_p$、$\mathcal E_pf=e_p$、
$G_pf=g_{p-1}$。$\mathcal E_p$ 只是本节的误差映射，
不是 primitive 坐标化；$G_p$ 不是原完整右源 Gram。

由 (4.2) 对所有 $f$ 同时成立，
$$
\boxed{\sum_{p=s+1}^{Q}\Psi_p\preceq I_{\mathscr T_n}.}
\tag{5.2}
$$
若 $\mathcal T_pf=t_p$，则还有
$$
\boxed{\mathcal T_p^*\mathcal T_p\preceq36\Psi_p,\qquad
 \sum_{p=s+1}^{Q}\mathcal T_p^*\mathcal T_p
 \preceq36I_{\mathscr T_n}.}
\tag{5.3}
$$
这里没有用点态向量界冒称一个伴随行界；(5.2) 是逐输入相加所得的
真正算子序。

## 6. 与原实际源在同一个切口同时变小

取原实际固定 $w$ 的同一顶部最小者 $u_Q$，以及它在每个切口诱导
的原源 $r_p$。沿原 good-top 构造，使用步长 $d$ 的终端半段网格
$J$，记
$$
K_{\rm win}=|J|,\qquad b\in J
 \ \Longrightarrow\ b\ge Q/2,\quad b+d\le Q.
$$
取 $s<\min J$，例如原 $s=4d$。原两费预算为
$$
\sum_{b\in J}\Xi_b(r_b)^2\le2\varepsilon_m^2.
\tag{6.1}
$$
所有 $\Psi_p$ 则使用同一原 $m$ 以及同一个固定测试空间
$\mathscr T_n$ 构造，不依赖选择哪个实际源。

令
$$
D_b^{(n)}=\sum_{p=b}^{b+d}\Psi_p.
\tag{6.2}
$$
因为网格步长为 $d$，每个孔层最多在两个这样的闭整数区间中出现。
由 (5.2)，
$$
\sum_{b\in J}D_b^{(n)}\preceq2I_{\mathscr T_n},\qquad
\sum_{b\in J}\operatorname{tr}D_b^{(n)}\le2n.
\tag{6.3}
$$
若 $\varepsilon_m>0$，对
$$
\frac{\Xi_b(r_b)^2}{2\varepsilon_m^2}
+\frac{\operatorname{tr}D_b^{(n)}}{2n}
$$
在同一个网格平均，其和至多为 $2$。因此存在一个共同 $b$，使
$$
\boxed{
\Xi_b(r_b)^2\le\frac{4\varepsilon_m^2}{K_{\rm win}},
\qquad
D_b^{(n)}\preceq\frac{4n}{K_{\rm win}}I_{\mathscr T_n}.}
\tag{6.4}
$$
结合 (5.3)，同一切口的真正 Riesz 测试源映射满足
$$
\boxed{
\|\,f\mapsto E_bP_{V_b}f\,\|^2
=\|\mathcal T_b\|^2\le\frac{144n}{K_{\rm win}}.}
\tag{6.5}
$$
同时，对每个 $f\in\mathscr T_n$，其整个 $[b,b+d]$ 的
$v/e/$首头创新能量之和至多
$4n\|f\|^2/K_{\rm win}$。这不是在另一切口获得的独立估计。

若 $\varepsilon_m=0$，(6.1) 的每个原源均为零，选择只需考虑
(6.3)；实际非零缺陷的后续论证不需要在零尾量上作除法。

共同选定切口后，可以继续作已经支付的原头旗及联合谱删除。
相对于原 sharp top 常数 $2$，(6.4) 只将原
$\Xi_b(r_b)^2$ 上界乘 $2$。这些正齐次投影证明中的平方费用界
随之乘 $2$，范数界乘 $\sqrt2$；原真实约束、精确头测试和
所有相容源流不变。测试映射 $\mathcal T_b$ 仅由
$(A_m,D_m,b,f)$ 决定，源删除不会改变 (6.5)。

因此在同一个保留固定 $w$ 的余源 $\widehat r_b$ 上，仍可准确写
$$
\langle E_b^\dagger\widehat r_b,f\rangle
=\langle L_b\widehat r_b,t_b(f)\rangle
$$
并同时使用原两费小量与 (6.5)。

## 7. 这些新小量尚不能免费变成完整右链

从 (2.2) 看，连续测试顶向量满足
$$
Dv_{p+1}=t_p-e_{p+1},\qquad Av_p=-t_p,
$$
所以
$$
\boxed{Av_p+Dv_{p+1}=-e_{p+1}.}
\tag{7.1}
$$
原始的 $v$ 族有明确内部误差，且尚未被证明满足一个完整右旗
在第 $j$ 段的全部缩短头旗。它不能直接作为 $t_b$ 的右修复。

(4.2)、(6.4) 支付的是 $\mu(e_p)$，并没有支付
$\lambda(e_p)$，更没有删除误差。
同样，$\|t_b\|=O_n(K_{\rm win}^{-1/2})$ 与
$\mu_b(t_b)\le\|f\|$ 不推出 $\lambda_b(t_b)$ 小；
完整右逆可能在这个真实测试方向上放大。

新的可用输入是完整的受限递推 (2.1)、误差身份 (7.1) 和同一
切口的矩阵预算 (6.4)，而不是一个未经证明的右链。
将这些误差及跨头部分接到原裸／平坦双测试，或据此证明固定测试
局部 Gram 的窗口计数阶上界，仍是当前未完成项。普通无权
$N=M$ 与复 Hilbert ISP 保持开放。


## 8. 后续结论：整段正交组装与同一未来带支付的弱误差

本节补充原伴随流的两个可直接使用的结构，不将它们提升成
完整右链或终端小量。

### 8.1 增广可行空间与真正嵌套的测试余空间

在整个原头／尾 Hilbert 空间中定义
$$
\mathcal S_p=V_p\oplus\mathcal H_{>p}^{(m)}
=\ker P_{\le p-1}^{(m)}(A+D).
\tag{8.1}
$$
等号使用 $A+D$ 只保持或降低一孔。因此
$\mathcal S_{p+1}\subseteq\mathcal S_p$。
又 $\mathcal K_p\subseteq\ker(A+D)\subseteq\mathcal S_q$ 对所有 $p,q$
成立。令
$$
\boxed{\mathcal W_p=\mathcal S_p\ominus\mathcal K_p.}
\tag{8.2}
$$
由于 $\mathcal S_p$ 递减、$\mathcal K_p$ 递增，
$\mathcal W_p$ 也递减。

对原固定低测试 $f$，高孔自由直和分量的投影为零，所以
$$
q_p=P_{\mathcal S_p}f,\qquad
\boxed{U_pt_p=P_{\mathcal W_p}f.}
\tag{8.3}
$$
于是 (4.1) 不只是范数单调，还来自一个真正嵌套的物理投影族。

记
$$
h_p=q_{p-1}-q_p=(U_{p-1}e_p,v_p),\qquad
j_p=k_p-k_{p-1}.
$$
不同 $p$ 的 $h_p$ 彼此正交，因为 $\mathcal S_p$ 嵌套；
不同 $p$ 的 $j_p$ 也彼此正交，因为 $\mathcal K_p$ 嵌套。
此外 $h_p\perp\ker(A+D)$，而每个 $j_q$ 属于该核，所以这两组
对全部 $p,q$ 相互正交。

因此对 $s<a\le c\le Q$，
$$
\boxed{
\|q_{a-1}-q_c\|^2
=\sum_{p=a}^{c}\bigl(\mu_{p-1}(e_p)^2+\|v_p\|^2\bigr),}
\tag{8.4}
$$
$$
\boxed{
\|U_{a-1}t_{a-1}-U_ct_c\|^2
=\sum_{p=a}^{c}
 \bigl(\mu_{p-1}(e_p)^2+\|v_p\|^2+
       \|N_{0,p}^{-1/2}\iota_0^*g_{p-1}\|^2\bigr).}
\tag{8.5}
$$
这两个窗口身份均不产生 $\sqrt{c-a+1}$ 的额外因子。
其矩阵形式特别给
$$
\boxed{
\Psi_p=P_{\mathscr T_n}
 (P_{\mathcal W_{p-1}}-P_{\mathcal W_p})|_{\mathscr T_n},\quad
D_b^{(n)}=P_{\mathscr T_n}
 (P_{\mathcal W_{b-1}}-P_{\mathcal W_{b+d}})|_{\mathscr T_n}.}
\tag{8.6}
$$

### 8.2 原左误差可以整段组装，仍无窗口长度损失

把各 $U_{p-1}e_p$ 按零延拓放到同一个物理空间。由 (2.4)，
$$
\sum_{p=a}^cU_{p-1}e_p
=q_{a-1}-q_c-\sum_{p=a}^cv_p.
$$
$v_p$ 位于互异孔层，故彼此正交。利用 (8.4)，
$$
\boxed{
\left\|\sum_{p=a}^cU_{p-1}e_p\right\|
\le
2\left[
 \sum_{p=a}^c
 \bigl(\mu_{p-1}(e_p)^2+\|v_p\|^2\bigr)
\right]^{1/2}.}
\tag{8.7}
$$
此处没有声称 $U_{p-1}e_p$ 彼此正交；正交的是完整的 $h_p$。
对固定测试空间，(6.4) 因而给
$$
\left\|f\longmapsto
 \sum_{p=b+1}^{b+d}U_{p-1}e_p(f)\right\|
\le4\sqrt{n/K_{\rm win}}.
\tag{8.8}
$$

### 8.3 同一个实际左流上的弱误差恰是物理未来内积

令 $u=U_Qr_Q$ 是一个真正原顶部最小者，
$r_p=Au_p$ 是同一个向量诱导的相容源。对 $p\le Q$，
$r_{p-1}=-\mathcal D_pu_p$。
置 $a_p=Z_p^{-1}t_{p-1}$，则 (2.1) 给
$e_p=J_{p-1}a_p$、$v_p=\mathcal D_p^*a_p$。因此准确有
$$
\boxed{
\langle L_{p-1}r_{p-1},e_p\rangle
=\langle r_{p-1},a_p\rangle
=-\langle u_p,v_p\rangle.}
\tag{8.9}
$$
其中两个左向量均为同一源定义的真正最小者，所以也有
$$
\langle U_{p-1}r_{p-1},U_{p-1}e_p\rangle
=-\langle u_p,v_p\rangle.
$$
对任何连续或不交选定孔集合 $\mathcal I$，Cauchy 给
$$
\boxed{
\sum_{p\in\mathcal I}
 |\langle L_{p-1}r_{p-1},e_p\rangle|
\le
\left(\sum_{p\in\mathcal I}\|u_p\|^2\right)^{1/2}
\left(\sum_{p\in\mathcal I}\|v_p\|^2\right)^{1/2}.}
\tag{8.10}
$$
右边只使用同一实际物理未来带与同一固定测试的已付能量。
这是弱配对的支付，不要求或断言 $\lambda(e_p)$ 小。

### 8.4 共同切口还可保真正未来带小量

原 good-top 的更早物理预算是
$$
y_b=P_{[b+1,b+d]}u,\qquad
\sum_{b\in J}\|y_b\|^2\le\varepsilon_m^2,\qquad
\Xi_b(r_b)^2\le2\|y_b\|^2.
$$
因此在第6节选择共同切口时，可以平均
$$
\frac{\|y_b\|^2}{\varepsilon_m^2}
+\frac{\operatorname{tr}D_b^{(n)}}{2n}
$$
代替原显示的两个项。其和仍至多 $2$。由此得到同一个 $b$ 的
加强版本：
$$
\boxed{
\|y_b\|^2\le\frac{2\varepsilon_m^2}{K_{\rm win}},\quad
\Xi_b(r_b)^2\le\frac{4\varepsilon_m^2}{K_{\rm win}},\quad
D_b^{(n)}\preceq\frac{4n}{K_{\rm win}}I.}
\tag{8.11}
$$
全部第6节的结论保持。对每个固定 $f\in\mathscr T_n$，(8.10)
在这个真正未来窗中进一步给
$$
\boxed{
\sum_{p=b+1}^{b+d}
|\langle L_{p-1}r_{p-1},e_p(f)\rangle|
\le
\frac{2\sqrt{2n}\,\varepsilon_m}{K_{\rm win}}\|f\|.}
\tag{8.12}
$$

### 8.5 剩余的真正端点不能删除

由原相容流与 (1.8)，对任何 $s\le p-1<p\le Q$，
$$
\boxed{
\langle L_pr_p,t_p\rangle
=\langle r_p,g_p\rangle
=\langle r_{p-1},g_{p-1}\rangle
=\langle L_{p-1}r_{p-1},t_{p-1}\rangle.}
\tag{8.13}
$$
这个守恒配对就是 $\langle u,f\rangle$。
因此 (8.9) 中的已付误差恰与物理 $u_p,v_p$ 配对抵消，
并没有消灭右端点 $t_{b+d}$。

(8.4)–(8.12) 允许把真实误差整段组装或与实际来源配对时避免
一个虚假的窗口长度损失。若要由此得到固定测试局部 Gram 上界，
仍须控制终端源、真实缩头旗，或给一个保原两费的端点消元。
小的正交增量不意味着端点 $U_{b+d}t_{b+d}$ 本身小。
