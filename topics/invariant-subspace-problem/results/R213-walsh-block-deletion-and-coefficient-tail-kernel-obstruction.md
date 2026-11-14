# R213：危险分支核的逐坐标与整块 Walsh 删除下界

日期：2026-11-13（Asia/Taipei）。作者：kernel / Astra-ISP-1cf8c51d。

状态：完整证明。结合 R208 的实际删除交换子与 R161 的通常伴随图界，得到逐坐标压缩投影下界；有限块秩一删除进一步把普通 Hilbert 尾下界加强到整个系数 ℓ² 尾，规范慢行为 m^(1/2−σ)，并排除临界最高指标加权域。仍未排除任意慢尾，不宣称主问题解决。

## 1. 同一实际闭分支上的两个接口

固定本题 Haar 表示中的闭第一阶
$$
X=a_*I+\sum_{j\ge0}a_jV_j,\qquad a\in\ell^2,
$$
令
$$
\mathcal B_2=\sum_{j\ge0}a_j^2(I-V_j^2),\qquad
Y=\varphi(\mathcal B_2),\qquad T=X-Y,
\qquad M=\ker T,
$$
其中 $\varphi$ 在零点邻域全纯。$Y\in\mathcal A$ 有界，$\operatorname{Dom}T=\operatorname{Dom}X$。置 $g=\|a\|_2$。

对 Walsh 基定义
$$
b_j\chi_F=\begin{cases}\chi_{F\setminus\{j\}},&j\in F,\\0,&j\notin F,\end{cases}
\qquad n_j=b_j^*b_j.
$$
$n_j$ 是 Walsh 展开中含第 $j$ 位的正交投影，不是物理位乘法投影。

R208 §§2–5 给出完整域上的实际等式
$$
b_j\operatorname{Dom}T\subseteq\operatorname{Dom}T,
\qquad
[b_j,T]=a_j(I-2n_j+2b_j)+R_j,
\tag{1.1}
$$
并且对 $j\ge1$ 可取
$$
\begin{split}
\|R_j\|\le r_j:={}&
\frac{36g\eta_{j-1}}{\sqrt{1-\eta_*^2}}
+16|a_j|\eta_j\\
&+C_\varphi\bigl(432g^2\eta_{j-1}+72|a_j|^2\bigr).
\end{split}
\tag{1.2}
$$
这里 $\eta_*<1/4$，$C_\varphi$ 是固定全纯演算圆周上的 resolvent 常数。具体而言，R208 (3.6) 控制 $[b_j,X]-a_j(I-2n_j+2b_j)$，R208 (5.2) 控制 $[b_j,Y]$；两者相减即为 (1.2)。完整域保持来自 R208 §4 的图核心延拓，未把核心等式直接当成最大域等式。

另一方面 R161 给
$$
\operatorname{Dom}X=\operatorname{Dom}X^*,\qquad
\|Xf\|^2-\|X^*f\|^2=\langle C_af,f\rangle,
\qquad
\|C_a\|\le(4+\varepsilon_{\rm carry})g^2.
\tag{1.3}
$$
因此同一核 $M$ 上的通常伴随有界：定义
$$
L=\sqrt{\|Y\|^2+\|C_a\|}+\|Y\|,
\tag{1.4}
$$
则
$$
\boxed{M\subseteq\operatorname{Dom}T^*,\qquad
\|T^*f\|\le L\|f\|\quad(f\in M).}
\tag{1.5}
$$
证明是 $Xf=Yf$ 与 (1.3) 给 $\|X^*f\|^2\le(\|Y\|^2+\|C_a\|)\|f\|^2$，再使用有界扰动的完整伴随公式 $T^*=X^*-Y^*$。不假定 $T^*M\subseteq M$。

## 2. 每个活跃坐标上的核内删除下界

**定理 2.1。** 令
$$
\beta_j=\frac{(|a_j|-r_j)_+}{L+4|a_j|},
\tag{2.1}
$$
若分子分母同为零则规定 $\beta_j=0$。则
$$
\boxed{\|b_jf\|\ge\beta_j\|f\|\qquad(f\in M),}
\tag{2.2}
$$
等价地，作为全空间上的正算子不等式，
$$
\boxed{P_Mn_jP_M\ge\beta_j^2P_M.}
\tag{2.3}
$$

**证明。** $f\in M$ 时，(1.1) 保证 $b_jf\in\operatorname{Dom}T$，所以内积对第一变量线性的约定给
$$
\langle[b_j,T]f,f\rangle
=-\langle Tb_jf,f\rangle
=-\langle b_jf,T^*f\rangle.
\tag{2.4}
$$
将 (1.1) 代入，使用 $\langle n_jf,f\rangle=\|b_jf\|^2$ 和 (1.5)，得到
$$
(|a_j|-r_j)\|f\|^2
\le2|a_j|\|b_jf\|^2
+(2|a_j|+L)\|b_jf\|\,\|f\|.
\tag{2.5}
$$
由 $\|b_jf\|\le\|f\|$，右侧至多 $(L+4|a_j|)\|b_jf\|\|f\|$。若分子非正结论平凡；否则除以正数得到 (2.2)。平方并用 $n_j=b_j^*b_j$ 即得 (2.3)。证毕。

保留 (2.5) 的二次项，还可得到稍强的根式界。对 $s=|a_j|>r_j$，
$$
\frac{\|b_jf\|}{\|f\|}\ge
\frac{\sqrt{(L+2s)^2+8s(s-r_j)}-(L+2s)}{4s}.
\tag{2.6}
$$
后文只需简洁的 (2.1)。

## 3. 普通有限头尾及缺失单坐标

令 $Q_m$ 为只依赖低 $m$ 位的有限柱空间的正交投影。若 $j\ge m$，则 $b_jQ_m=0$，所以
$$
\|b_jf\|=\|b_j(I-Q_m)f\|\le\|(I-Q_m)f\|.
$$
于是
$$
\boxed{\|(I-Q_m)f\|\ge
\left(\sup_{j\ge\max(m,1)}\beta_j\right)\|f\|
\quad(f\in M).}
\tag{3.1}
$$
这是普通 Hilbert 范数下界，不要求控制 $X^*(I-Q_m)f$ 或任何次数算子图范数。

若 $\beta_j>0$，还有
$$
M\cap\ker b_j=\{0\}.
\tag{3.2}
$$
$b_j|_M$ 单射、值域闭，且其像上的逆范数不超过 $\beta_j^{-1}$。该像不被声称仍在 $M$；删除算子也不被当成保持核的交换子。

## 4. 规范慢行的多项式下界

若沿一组活跃坐标满足
$$
a_j\ne0,\qquad \eta_{j-1}/|a_j|\longrightarrow0,
\tag{4.1}
$$
则 $a_j\to0$ 与 (1.2) 给 $r_j/|a_j|\to0$。所以在这些坐标的充分大部分，
$$
\boxed{\beta_j\ge\frac{|a_j|}{2(L+4g)}.}
\tag{4.2}
$$
活跃坐标存在时 $g>0$，故分母非零。

特别对
$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad\frac12<\sigma\le1,
\tag{4.3}
$$
本题超快 $\eta_j$ 使 (4.1) 对全部充分大坐标成立。取 $j=m$ 得
$$
\boxed{\|(I-Q_m)f\|\ge c(m+1)^{-\sigma}\|f\|
\quad(m\ge m_0,\ f\in M),}
\tag{4.4}
$$
其中 $c>0,m_0$ 只依赖固定行、固定分支和实际模型，不依赖 $f$。

在 R208 §7 的无常数项 $a_*=0$ 设置下，对危险平方，令最低非零系数为 $a=a_{j_0}$，取
$$
Y=(a^2I-\mathcal B_2)^{1/2},\qquad\chi(Y)=a.
$$
R208 §7 已在真实自然域中证明
$$
\ker X_{u^2-a^2}=\ker(X-Y)=M.
$$
因此 (4.4) 适用于这个实际 Bell 平方核，而不只是一个形式分支。

**推论 4.1。** 对 (4.3) 的行，若非零 $f\in H$ 满足
$$
\|(I-Q_m)f\|=o(m^{-\sigma}),
\tag{4.5}
$$
则 $f\notin\ker(X-\varphi(\mathcal B_2))$，特别不属于危险平方核。

这允许无界 Walsh 次数和仅多项式头部逼近。例如
$$
f_p=\sum_{n\ge1}(n+1)^{-p}\chi_{\{0,\ldots,n-1\}},
\qquad p>\sigma+\tfrac12,
$$
属于 $H$，有无界次数，且
$$
\|(I-Q_m)f_p\|^2=\sum_{n>m}(n+1)^{-2p}
=O(m^{1-2p})=o(m^{-2\sigma}).
$$
这些非零向量被相应核排除，但本稿不由此宣称其完整 $A$ 循环性。

## 5. 正算子叠加与保留的缺口

因为 (2.3) 是同一核上的正算子不等式，对任意有限非负权 $t_j$，
$$
P_M\left(\sum_jt_jn_j\right)P_M
\ge\left(\sum_jt_j\beta_j^2\right)P_M.
\tag{5.1}
$$
不能把 $\sum_{j\ge m}n_j$ 误当成有界投影。一般 $H$ 向量的次数期望可以无穷，未知核也没有已证有限次数期望。

因此 (5.1) 本身不证明更强的块质量界
$$
\|(I-Q_m)f\|^2\ge c\sum_{j\ge m}|a_j|^2\|f\|^2.
$$
也不能把 (2.2) 的 $f$ 替换为 $b_kf$ 后迭代，因为一般 $b_kf\notin M$。

相邻双反射中 $B^{-1}E$ 在未知核上的域和有界性不由本稿自动确定。本稿加强了该核必须满足的粗糙性，仍允许所有更慢的普通尾。普通 ISP 与危险平方单核问题仍未解决。

依赖：R125；R161 (1.4)–(1.6) 及 §6；R208 (3.6)、§4、(5.2) 与 §7。

## 6. 有限块秩一删除：改进为整个系数平方尾

本节加强 §4。下面的有限块删除只作用于零次和一次 Walsh 层，其交换子范数因而只依赖块中系数的 $\ell^2$ 质量，没有增长块的 $\ell^1$ 代价。

固定整数 $1\le m<n$，令 $I=[m,n)$，并置
$$
q=q_{m,n}=\left(\sum_{j=m}^{n-1}|a_j|^2\right)^{1/2}>0.
$$
在这块的 Walsh 张量空间中，令 $\Omega_I=1$，
$$
h_I=q^{-1}\sum_{j\in I}a_j\chi_j,
\qquad
D_I z=\langle z,h_I\rangle\Omega_I.
\tag{6.1}
$$
在块外张量恒等。$D_I$ 是范数 $1$ 的实际有界算子，且 $D_IQ_m=0$。内积仍对第一变量线性。

令 $S_j=I-2E_j$ 为纯单比特模型，并写
$$
X_I^0=\sum_{j\in I}a_jS_j.
$$
单比特 Walsh 矩阵为
$$
S_j=\begin{pmatrix}0&-1\\1&2\end{pmatrix}.
$$
直接计算给
$$
X_I^0\Omega_I=qh_I,
$$
$$
(X_I^0)^*h_I
=q\Omega_I+\frac2q\sum_{j\in I}|a_j|^2\chi_j
-\frac1q\sum_{j<k\in I}
(\overline a_ja_k+\overline a_ka_j)\chi_j\chi_k.
\tag{6.2}
$$
三个不同次数层正交。用
$|\overline a_ja_k+\overline a_ka_j|^2\le4|a_j|^2|a_k|^2$，得到
$$
\|(X_I^0)^*h_I\|^2
\le3q^2+\frac{2\sum_{j\in I}|a_j|^4}{q^2}
\le5q^2.
$$
秩一算子相乘的准确公式遂给
$$
\boxed{\|[D_I,X_I^0]\|\le(1+\sqrt5)q.}
\tag{6.3}
$$
同时，对每个 $v\in\operatorname{Ran}Q_m$，
$$
\boxed{[D_I,X_I^0]v=qv.}
\tag{6.4}
$$
没有用整个 $X_I^0$ 的范数代替 (6.3)；后者确实没有块长损失。

### 6.1 真实进位、完整域与全纯项的统一预算

对 $k<m$ 用实际低头截断 $V_k^{[m]}$，它只作用于低 $m$ 位。R208 的进位估计给
$$
\|V_k-V_k^{[m]}\|\le18\alpha_m/\alpha_k,
\qquad\|V_j-S_j\|\le8\eta_j.
$$
因此，把 $X$ 中 $k<m$ 的项换成 $V_k^{[m]}$，并把 $j\in I$ 的项换成 $S_j$，总差是有界算子 $E_{m,n}$，且统一于 $n$ 有
$$
\|E_{m,n}\|\le e_m:={26g\eta_{m-1}\over\sqrt{1-\eta_*^2}}.
\tag{6.5}
$$
这里低头部分使用 Cauchy–Schwarz 与几何比值和；块内部分使用
$\sum_{j\ge m}|a_j|\eta_j\le g\eta_m/\sqrt{1-\eta_*^2}$。保留的 $k\ge n$ 尾项只作用于块之后，和 $D_I$ 精确交换。常数项也交换。

有限局部算子 $D_I$ 保持有限柱核心。在核心上，$[D_I,X]$ 只涉及有限个 $k<n$ 的有界项。像 R208 §4 一样以 $X$ 图核心逼近，得到
$$
D_I\operatorname{Dom}X\subseteq\operatorname{Dom}X,
\qquad
[D_I,X]=[D_I,X_I^0]+[D_I,E_{m,n}]
\tag{6.6}
$$
作为真实完整域上的有界交换子。于是
$$
\|[D_I,X]\|\le(1+\sqrt5)q+2e_m,
\tag{6.7}
$$
以及
$$
\|([D_I,X]-qI)v\|\le2e_m\|v\|
\quad(v\in\operatorname{Ran}Q_m).
\tag{6.8}
$$

对 Bell 项，低于 $m$ 的实际截断平方差至多
$216\alpha_m/\alpha_k$；块内逐项用 $\|I-V_j^2\|\le37$；块之后与 $D_I$ 交换。因为 $\|D_I\|=1$，
$$
\|[D_I,\mathcal B_2]\|
\le432g^2\eta_{m-1}+74q^2.
\tag{6.9}
$$
固定全纯演算圆周的有界 resolvent 公式给
$$
\boxed{\|[D_I,Y]\|\le
y_m(q):=C_\varphi(432g^2\eta_{m-1}+74q^2).}
\tag{6.10}
$$
此处同一个 $C_\varphi$ 可取为
$\operatorname{length}(\Gamma)\max_\Gamma|\varphi(z)|\max_\Gamma\|(z-\mathcal B_2)^{-1}\|^2/(2\pi)$，与 $m,n$ 无关。无须要求 Taylor 半径大于算子范数。

### 6.2 普通尾的块下界

**定理 6.1。** 对每个 $f\in M$，
$$
\boxed{
{\|(I-Q_m)f\|\over\|f\|}
\ge
{(q-2e_m-y_m(q))_+\over
L+(2+\sqrt5)q+2e_m}
\quad(f\ne0).
}
\tag{6.11}
$$

**证明。** 归一化 $\|f\|=1$，写 $v=Q_mf$、$u=f-v$、$\epsilon=\|u\|$。因为 $D_Iv=0$，$\|D_If\|\le\epsilon$。由 $Tf=0$、完整域保持及 (1.5)，
$$
|\langle[D_I,T]f,f\rangle|
=|\langle D_If,T^*f\rangle|\le L\epsilon.
\tag{6.12}
$$
另一方面，(6.7)–(6.8) 给
$$
\|([D_I,X]-qI)f\|
\le2e_m+((2+\sqrt5)q+2e_m)\epsilon.
$$
用 (6.10) 控制 $[D_I,Y]$，并把上式与 (6.12) 合并，得到
$$
q\le2e_m+y_m(q)
+[L+(2+\sqrt5)q+2e_m]\epsilon.
$$
这正是 (6.11)。证毕。

### 6.3 整个平方尾及规范幂尾

令
$$
s_m=\left(\sum_{j\ge m}|a_j|^2\right)^{1/2}.
$$
对固定 $m$ 令有限块终点 $n\to\infty$。不需要 $D_I$ 有任何算子极限：直接对 (6.11) 右侧的标量连续函数取极限即可。得到
$$
\boxed{
{\|(I-Q_m)f\|\over\|f\|}
\ge
{(s_m-2e_m-y_m(s_m))_+\over
L+(2+\sqrt5)s_m+2e_m}.
}
\tag{6.13}
$$

如果 $s_m>0$ 且 $\eta_{m-1}/s_m\to0$，则 $s_m\to0$，所以 (6.13) 的分子最终至少为 $s_m/2$，分母有固定上界。因此存在 $c>0,m_0$，使
$$
\boxed{\|(I-Q_m)f\|\ge c\,s_m\|f\|
\quad(m\ge m_0,\ f\in M).}
\tag{6.14}
$$
对规范慢行 (4.3)，积分比较给 $s_m\asymp(m+1)^{1/2-\sigma}$，从而
$$
\boxed{\|(I-Q_m)f\|\ge c(m+1)^{1/2-\sigma}\|f\|.}
\tag{6.15}
$$
这严格加强 §4 的逐坐标界。现在普通尾为 $o(m^{1/2-\sigma})$ 的所有非零向量均被相应闭分支核排除。前述链状 Walsh 例只需 $p>\sigma$，而非 $p>\sigma+1/2$，就满足这一更强排除条件。

### 6.4 最大 Walsh 指标的临界加权二次型必须发散

对非空有限集 $F$ 置 $\nu(F)=1+\max F$，空集置 $\nu(\varnothing)=0$。写 $f=\sum_F\widehat f_F\chi_F$。由 (6.15)，非零 $f\in M$ 对所有充分大 $m$ 满足
$$
\sum_{\nu(F)>m}|\widehat f_F|^2
\ge c^2(m+1)^{-(2\sigma-1)}\|f\|^2.
\tag{6.16}
$$
令 $p=2\sigma-1>0$。非负级数的分部求和（或 Tonelli）给
$$
\sum_F\nu(F)^p|\widehat f_F|^2
=\sum_{m\ge0}((m+1)^p-m^p)
\sum_{\nu(F)>m}|\widehat f_F|^2.
$$
由 $((m+1)^p-m^p)\asymp m^{p-1}$ 和 (6.16)，右侧支配一个正常数倍的调和级数。故
$$
\boxed{\sum_F(1+\max F)^{2\sigma-1}|\widehat f_F|^2=\infty
\quad(0\ne f\in M),}
\tag{6.17}
$$
其中空集项按零处理。本结论排除一个明确的临界最大指标加权 Hilbert 域，不要求有限 Walsh 次数。

所有结论仍允许慢于 (6.15) 的尾。有限块测试的范数界并没有把 $M$ 的单位球变成有限头一致可逼近集，也没有构造一个非零紧交换子。不能据此取消相邻反射中未知限制上的第二次除法。
