# R352：整个原典范来源的次数二微分算子与真实移动极

日期：2026-11-13。**状态：以下整个 canonical 来源上的固定次数二整微分算子、准确核与饱和范围、同一物理目标中的完整转置及一次行移成本均已证明。该算子保留原来源，不含按次数任意删去的 floor 项。它仍耦合同一 \(\Phi\) 与 \(\mathcal E\Phi\)；未声称后者保持原提升核，也未把真实移动极自动变为原 \(C_2(M)\) 的子商。**

## 1. 整个已付来源及其实际极界

取 R335 的系数环 \(R_0=\mathbf Z[1/(42b)]\)、\(b=17\)。为了避免与系数环混淆，以下用 \(\mathscr R\) 表示相对径向变量。
令
\[
h_7=16t^2+4t+7,\quad a=t(t-1)h_7,\quad
\chi=(t-1)(1+8t)h_7,
\]
\[
\alpha_n=\lfloor(n+1)/4\rfloor,\quad
\beta_n=\lfloor(n+1)/3\rfloor,\quad
\gamma_n=\lfloor n/2\rfloor,
\quad q_n=\frac{(t h_7)^{\alpha_n}(t-1)^{\beta_n}}{(1+8t)^{\gamma_n}}.
\tag{1}
\]
原相对来源的完整次数 \(n\) 部分准确为
\[
\mathcal V_n=\mathscr R^n q_n(t)R_0[t]_{\le e_{n+1}},
\quad e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+\lceil2m/3\rceil-2.
\tag{2}
\]
这是原权 \(n+40\) 的整个导子，乘回固定 \(G_0\) 即是 R335 的原整列。

一个便于保持所有边界的准确等式是
\[
\boxed{\deg q_n+e_{n+1}=f_n:=\lfloor9n/2\rfloor+4.}
\tag{3}
\]
所以每个 \(q_nP\) 在有限处仅可能有 \(t=-1/8\) 的至多 \(\gamma_n\) 阶极，在无穷处至多有 \(f_n\) 阶极；同时保留 (1) 显示的全部强迫零。

## 2. 一个不需逐次数修正的真实算子

定义固定齐次元素
\[
\boxed{
W=\mathscr R^2 a\chi
=\mathscr R^2 t(t-1)^2(1+8t)h_7^2,
\qquad \mathcal Q=W\,t\partial_t,
\qquad\mathcal E=\mathscr R\partial_{\mathscr R}.
}
\tag{4}
\]
\(t\partial_t\) 在这里保持 \(\mathscr R\) 不动。

**定理1。** 对每个 \(n\ge0\)，
\[
\boxed{W\mathcal V_n\subset\mathcal V_{n+2},\qquad
\mathcal Q\mathcal V_n\subset\mathcal V_{n+2}.}
\tag{5}
\]
两者都是原整数来源中的映射；\(W\mathcal E\) 也有相同结论。

先核 \(W\) 本身是原归一化 \(\mathcal N_{R_0,2}\) 的真正元素。
R335 的原次数二基本分式是
\[
\frac{A^2}{T_2}=\mathscr R^2\frac{t(t-1)h_7}{1+8t},\qquad d_2=6.
\]
(4) 与该分式之商为
\((t-1)(1+8t)^2h_7\)，次数五。因此 \(W\in\mathcal N_{R_0,2}\)，它乘整个原 canonical 模的作用已在原归一化内，没有新加入外部来源。

对微分映射，令
\[
\Delta_\alpha=\alpha_{n+2}-\alpha_n\in\{0,1\},\quad
\Delta_\beta=\beta_{n+2}-\beta_n\in\{0,1\},\quad
\gamma_{n+2}-\gamma_n=1.
\]
对原基列 \(\Phi_{n,j}=\mathscr R^nq_nt^j\)，准确有
\[
\mathcal Q\Phi_{n,j}=\mathscr R^{n+2}q_{n+2}\,B_{n,j}(t),
\tag{6}
\]
其中完整整数多项式为
\[
\begin{split}
B_{n,j}={}&t^{j+1-\Delta_\alpha}(t-1)^{1-\Delta_\beta}
 (1+8t)h_7^{1-\Delta_\alpha}\,\Bigl[
 (\alpha_n+j)(t-1)(1+8t)h_7\\
&\quad+\beta_n t(1+8t)h_7
 +\alpha_n t(t-1)(1+8t)h_7'
 -8\gamma_n t(t-1)h_7\Bigr].
\end{split}
\tag{7}
\]
所有显示的指数非负。次数准确满足
\[
\deg B_{n,j}\le j+9-3\Delta_\alpha-\Delta_\beta
\le e_{n+3}-1,
\tag{8}
\]
因为 (3) 给 \(f_{n+2}-f_n=9\)。这同时支付各有限零极与完整无穷极界，证明 (5)。

该计算解释了为什么不能只用一个 \(\chi\) 清分母后就假定所有次数闭合。
例如在 \(n=6\) 上，若改用 \(\mathscr R\chi(t\partial_t-\alpha_6)\)，则其最低列相对目标 \(q_7\) 的商是
\[
8t+10-\frac{108(t-1)}{h_7},
\tag{9}
\]
确有原七挠因子处的极。(4) 支付了这个真实问题，而不是将其作为零项删掉。

## 3. 准确核与整像的饱和范围

写 \(\mathcal V_{\le D}=\bigoplus_{n=0}^D\mathcal V_n\)，并取 \(D\ge1\)。
在特征零，\(t\partial_tf=0\) 等价于 \(f\) 为常数。
\(q_0=q_1=1\)，而 \(n\ge2\) 时 \(q_nP\) 在 \(t=1\) 有正阶零。
不同径向次数不能互相抵消。因此
\[
\boxed{\ker\mathcal Q=R_0\cdot1\oplus R_0\cdot\mathscr R.}
\tag{10}
\]

对一个原好素数，假定
\[
\boxed{f_D=\lfloor9D/2\rfloor+4<p.}
\tag{11}
\]
在模 \(p\) 的函数域中，导数为零的有理函数属于 \(k(t^p)\)，所以每个极阶都被 \(p\) 整除。
(3)、(11) 保证有限极阶 \(\gamma_n\) 和无穷极阶 \(f_n\) 都小于 \(p\)；此函数只能为常数。
原 \(t=1\) 的零又排除 \(n\ge2\) 的非零常数。
故 (10) 在模 \(p\) 后仍是准确的全部核。

原基来自 R335 的整个饱和整格，(7) 的矩阵整；其模 \(p\) 秩与特征零秩完全相同。
于是得到真正来源中的整单射
\[
\boxed{
\mathcal V_{\le D}/\langle1,\mathscr R\rangle
\ \xrightarrow{\ \mathcal Q\ }\ \mathcal V_{\le D+2}
\quad\text{的像是 }p\text{-饱和的。}}
\tag{12}
\]
这里的范围 (11) 是明确条件，不把所有 \(D\) 的 derivative 系数都当作单位。
这份饱和属于真实原来源映射，尚不直接等于评价矩阵的深关系。

## 4. 同一个物理有限目标中的完整转置

采用 R342 已付的 Gaussian 规范，或等价地采用 R338 的原规范：
\[
\mathscr R_{\rm phys}=g(w)e_2(a_p\epsilon),\qquad
w^s=p\epsilon,\quad\epsilon^3=0,\quad p=6s-1,
\]
\[
L=2s+\ell,\quad1\le\ell<s-13,\qquad
J(\Phi)=\Phi(\mathscr R_{\rm phys},t(w)),\quad M=m_{13}J.
\tag{13}
\]
若使用重标规范，(13) 的 \(g,a_p\) 同时换为 \(g_*,a_*\)，整个 \(J,M\) 不变。

令
\[
\mathsf E_w=w\partial_w,\qquad\mathsf E_w\epsilon=s\epsilon,
\quad h(t)=z\sqrt x,\quad G(t)=(1-t)^{-1/2},\quad
u(w)=G(t(w))/h(t(w)).
\]
由于 \(w=(-t/b)h(t)^6\)，准确有
\[
\mathsf E_w t=t/\nu,
\qquad\mathsf E_w\log\mathscr R_{\rm phys}
=\mathsf E_w\log g+s a_p\epsilon=:\Lambda.
\tag{14}
\]
这里 \(\mathsf E_w\log g\) 表示 \((\mathsf E_wg)/g\)，不需要选择常数的 \(p\) 进对数。
\(\mathsf E_w\) 保持全部原除幂关系及截断。

对同一个原 \(\Phi\)，链式法则给完整恒等式
\[
\boxed{
J(\mathcal Q\Phi)=W_{\rm phys}\nu
 \{\mathsf E_wJ(\Phi)-\Lambda J(\mathcal E\Phi)\},
\qquad W_{\rm phys}=\mathscr R_{\rm phys}^2a(t)\chi(t).
}
\tag{15}
\]
它含原 \(g\) 的所有高轴和真正的 \(s a_p\epsilon\)；没有分别截掉两条接触尾。
同时 \(m_{13}\mathsf E_w=(\mathsf E_w-13)m_{13}\)，故在原已付目标单位规范中
\[
\boxed{
M(\mathcal Q\Phi)=W_{\rm phys}\nu
 \{(\mathsf E_w-13)M(\Phi)-\Lambda M(\mathcal E\Phi)\}.
}
\tag{16}
\]
左边读取完整多一行目标，右边的两个原观察使用同一截断。
若将已付公共目标单位 \(U_0\) 乘回，实际算子
\(M_{\rm orig}=U_0M\) 的对应公式准确把
\(\mathsf E_w-13\) 换为
\(\mathsf E_w-13-(\mathsf E_wU_0)/U_0\)。
因此没有丢掉原 \(G_0\) 的 theta 连接。

(15)、(16) 只是原来源恒等式。
即使 \(\Phi\) 在某层提升核中，也不能无证令 \(\mathcal E\Phi\) 在同一核中；这正是 R338 两条接触尾继续耦合的原因。

## 5. 额外成本恰为一次行移

原 \(t(w)=-bw+\cdots\)、\(\mathscr R_{\rm phys}(0)=1\)、\(\nu(0)=1\)，所以
\[
\boxed{W_{\rm phys}\nu=-49b\,w\cdot V(w,\epsilon),\qquad V(0)=1,}
\tag{17}
\]
\(V\) 是同一个完整目标中的整单位。
R342 的原参数整性窗口覆盖 (13) 所有块；各单位在已付完整目标上读取，未只保留常数项。
因此 (16) 在来源上增加固定 relative charge 二，在目标上仅增加一行。

对一般 \(2s<T\le3s-1\)，原基为
\(e_r=w^r/p^{\lfloor r/s\rfloor}\)，\(0\le r<T\)。
乘 \(w\) 到完整长度 \(T+1\) 的系数为
\[
p^{\lfloor(r+1)/s\rfloor-\lfloor r/s\rfloor}.
\]
准确只有 \(r=s-1,2s-1\) 两项带一个 \(p\)，其余都是单位。
在 (16) 中 \(T=L+13\le3s-1\)，故这两条边界全部包含。
对任意原源矩阵 \(F\) 和每个提升精度 \(h\)，因此
\[
\boxed{0\le\ell(\ker(wF\bmod p^h))-ell(\ker(F\bmod p^h))\le2.}
\tag{18}
\]
这只计算新增加的一次行移；此前 charge 四十、十三行及至多二十六的原成本仍按 R328/R335 保留。

## 6. 原移动极与残数路线的具体相接

在 R342 的原惰性支上，\(y=-x^{3/2}\sqrt{1-t}\)、\(h=z\sqrt x\)，所以
\[
\nu=\frac G h=-\frac{x}{yz}.
\]
R342 的实际有理原函数
\[
Z_p=\mathscr R_p(x)/y^p,\qquad dZ_p=dz\pmod p,\qquad
z\equiv Z_p\pmod{p,u^{5p}}
\]
于是给所需完整窗口内的真实比较
\[
\boxed{\nu\equiv-\frac{x}{yZ_p}\pmod p.}
\tag{19}
\]
这里令 \(u=x^{-1/2}\)。因 \(L+14\le3s\)，比较所需的 \(z\) 阶低于 \(3(p+1)<5p\)，所以没有超出已付窗口。

R346 的全部非原点测试极恰是 \(Z_p\) 的简单零，且在那里 \(x,y\) 为单位。
因此 (19) 在这些真实极有明确的一阶主部；这就是 (16) 的原对偶关系可能读取 R346 残数的具体位置。
\(W_{\rm phys}\)、\(\Lambda\)、两条接触尾和首 Bockstein 像仍须一起参与配对；不能只把 (19) 的分母单独当作新增源或零条件。

后续准确任务是把 (16) 转置到原 \(C_2(M)^\vee\)，使用 R346 的完整有限 étale 极部，判断哪些原残数测试受这个真实来源关系约束。
本篇已经支付所需来源操作和全部固定边界，没有预付该余像结论。

## 精确证书

[check-jzero-whole-canonical-degree-two-derivation.py](../scripts/check-jzero-whole-canonical-degree-two-derivation.py)
及同名 JSON 核定十二个完整 floor 类、原闭合矩阵公式、原次数二 carrier、实际链式法则和两条一次行移边界。
核与饱和范围的全体次数证明见正文，不以有限素数实验替代。
