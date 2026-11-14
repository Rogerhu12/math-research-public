# 尾部正耦合：几乎处处连续见证排除、无界径向类与有界反例

日期：2026-11-13（UTC）。作者：normal_next / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：以下结论完整证明，属于中间进展。** 本稿将连续核的相对迹结论扩到有界且几乎处处连续的 Hilbert 值特征映射，并在两个真实比较边缘的一致可积性下允许无界映射。给出无界的明确径向类及精确边缘尾估计。另一方面，一个有界、模恒为一的正秩一例使同一归一化矩趋向负数，说明一般正常性甚至有界分量都不够。坏例不湮灭慢主理想。一般正正常见证、见证专属配对与普通 ISP 仍未解决。

## 1. 实际对象和正特征映射

沿用原 Haar 空间 $H=L^2(\mathbb Z_2,\mu)$、实际代数
$\mathcal A=\overline{\mathbb C[I,A]}$ 及
$$
S_N=\sum_{j\ge0}a_jN_j,\qquad
S_Y=\sum_{j\ge0}a_jY_j,\qquad a_j=(j+1)^{-2}.
$$
对 $S=S_N$ 或 $S_Y$，令
$$
q=2^m,\qquad
P_m=\prod_{\zeta^q=1}\gamma_\zeta(S)
=I_{<m}\otimes Q_m\in S\mathcal A,
$$
并置
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad E_j=e_{10}^{(j)},\qquad
T_m=I_{<m}\otimes D_m^q,\qquad
h_m=\langle T_m1,1\rangle.
\tag{1.1}
$$
R253 第三附录已经证明
$$
h_m>0,\qquad
\|P_m-T_m\|\le e_m,\qquad
\frac{e_m}{h_m}\longrightarrow0,
\tag{1.2}
$$
其中可取
$$
e_m=13a_\Sigma q(3a_\Sigma)^{q-1}e^{-770\,16^{m-1}},
\qquad h_m\ge(8eq)^{-q}.
$$
这些是两个实际慢符号共有的真 carry 估计，不是假定纯模型等于实际代数。

设 $\mathcal K$ 为可分 Hilbert 空间，
$$
F:\mathbb Z_2\to\mathcal K,\qquad
\int\|F(y)\|_{\mathcal K}^2\,d\mu(y)=\lambda<\infty
\tag{1.3}
$$
为强可测映射。取 $\mathcal K$ 的正交基并写 $F=(f_i)_i$，则
$$
\rho_F=\sum_i f_i\otimes f_i\ge0,\qquad
\operatorname{Tr}\rho_F=\lambda.
\tag{1.4}
$$
级数在迹范数下收敛。定义
$\phi_F(B)=\operatorname{Tr}(\rho_FB)$。内积线性于第一个变量，故对有界算子 $B$，
$$
\phi_F(B)=\sum_i\langle Bf_i,f_i\rangle.
$$

## 2. 正尾幂给出的准确近对角耦合

设 $w_j=a_j/2$，$j\ge m$，并记 $e_q(w)$ 为基本对称多项式。对每个 $q$ 元有限子集
$A\subset[m,\infty)$，定义
$$
\pi_m(A)=\frac{w_A}{e_q(w)}.
\tag{2.1}
$$
因为所有集合大小同为 $q$，也有
$\pi_m(A)=a_A/e_q(a)$。

定义 $\nu_m$ 为 $\mathbb Z_2\times\mathbb Z_2$ 上的概率测度：
先按 (2.1) 选择 $A$；在 $A$ 外取同一组独立公平二进位；把第一坐标 $x$ 的 $A$ 位全设为 $0$，把第二坐标 $y$ 的 $A$ 位全设为 $1$。因此第一坐标是算子的输入，第二坐标是输出。记两个边缘为
$$
\nu_m^-,\qquad \nu_m^+.
$$
其相对于 Haar 测度的密度准确为
$$
r_m^-(x)=2^q\sum_A\pi_m(A)\mathbf1_{\{x_j=0:j\in A\}},
\qquad
r_m^+(y)=2^q\sum_A\pi_m(A)\mathbf1_{\{y_j=1:j\in A\}}.
\tag{2.2}
$$
特别
$$
0\le r_m^\pm\le2^q.
\tag{2.3}
$$
两端的前 $m$ 位相同，并具有完全相同的 Haar 头分布。

对有限 $A$，令 $n_A=\sum_{j\in A}2^j$。物理位矩阵的准确作用是
$$
(E_Af)(y)=\mathbf1_{\{y_j=1:j\in A\}}\,f(y-n_A).
$$
在该示性集上，减去 $n_A$ 恰好把这些位改成 $0$，其余位不变。因此，保留输入、输出和共轭方向后，
$$
\boxed{
\frac{\phi_F(T_m)}{h_m}
=\int\langle F(x),F(y)\rangle_{\mathcal K}\,d\nu_m(x,y).
}
\tag{2.4}
$$
右端核是 $K_F(x,y)=\sum_i f_i(x)\overline{f_i(y)}$；不是把两坐标交换后的共轭。

严格地，先对有限个 $f_i$ 和有限和 $D_m^q=q!\sum_Aa_AE_A$ 验证等式，再取极限。该展开在算子范数绝对收敛。由 (2.3)，
$$
\int\|F(x)\|^2d\nu_m,\ 
\int\|F(y)\|^2d\nu_m\le2^q\lambda.
$$
两端 Cauchy--Schwarz 保证 (2.4) 的绝对可积性及可数坐标求和的合法性。

还准确有
$$
\nu_m\Longrightarrow\Delta_*\mu,
\qquad \Delta(y)=(y,y).
\tag{2.5}
$$
证明很直接：任何只依赖两坐标前 $n$ 位的函数，在 $m\ge n$ 时沿 $\nu_m$ 的积分恰等于其沿 Haar 对角的积分。连续函数由这些有限柱函数一致逼近，故 (2.5) 成立。此弱收敛不表示边缘密度一致可积；第 7 节将明确显示其强烈集中。

## 3. 加权头逼近条件与几乎处处连续情形

令 $G_m=\mathbb E_\mu(F\mid\text{前 }m\text{ 位})$ 为 Bochner 条件期望，并定义
$$
u_m^2=\int\|F-G_m\|^2\,d\nu_m^-,
\qquad
v_m^2=\int\|F-G_m\|^2\,d\nu_m^+.
\tag{3.1}
$$
由于前 $m$ 位相同，$\nu_m$ 几乎处处有 $G_m(x)=G_m(y)$。两边缘的头分布为 Haar，所以
$$
\int\|G_m(x)\|^2d\nu_m
=\int\|G_m(y)\|^2d\nu_m=\|G_m\|_{L^2(\mu;\mathcal K)}^2.
$$
展开两边的误差并分别用 Cauchy--Schwarz，得到
$$
\boxed{
\left|\frac{\phi_F(T_m)}{h_m}-\|G_m\|_2^2\right|
\le u_mv_m+\|G_m\|_2(u_m+v_m).
}
\tag{3.2}
$$

**判据 3.1。** 若 $u_m,v_m\to0$，则
$$
\frac{\phi_F(P_m)}{h_m}\longrightarrow\lambda.
\tag{3.3}
$$
事实上 $G_m\to F$ 于普通 $L^2$，(3.2) 先给纯比较极限，再由 (1.2) 给
$$
\left|\frac{\phi_F(P_m)-\phi_F(T_m)}{h_m}\right|
\le\lambda\frac{e_m}{h_m}\longrightarrow0.
\tag{3.4}
$$
因此，$\lambda>0$ 时 $\rho_F$ 不可能湮灭 $S\mathcal A$。

**定理 3.2。** 若 $F$ 有一个有界、在 $\mu$ 几乎处处按 $\mathcal K$ 范数连续的代表，则 (3.3) 成立。特别适用于任意有限组有界、几乎处处连续的复函数。

证明。在每个前 $m$ 位柱集 $C$ 上，令
$$
\operatorname{osc}_m(F)|_C
=\sup_{x,y\in C}\|F(x)-F(y)\|.
$$
它是有界的有限柱函数。在 $F$ 连续的点，
$\operatorname{osc}_m(F)\to0$；因而
$$
\int\operatorname{osc}_m(F)^2\,d\mu\longrightarrow0.
\tag{3.5}
$$
对该代表的任意点，条件期望平均给
$$
\|F-G_m\|\le\operatorname{osc}_m(F).
$$
两个边缘在前 $m$ 位上都是 Haar，故
$$
u_m^2,v_m^2
\le\int\operatorname{osc}_m(F)^2\,d\mu\longrightarrow0.
$$
由判据 3.1 即得。这里没有从普通 $L^2$ 逼近直接推导加权逼近，也没有不加控制地套用 Lusin 定理。

该条件严格弱于存在连续代表；例如第 6 节的 $\alpha=0$ 例只在一个零测点不连续，却不存在连续代表。

## 4. 无界映射的两边缘一致可积性

**定理 4.1。** 假设 $F$ 按 $\mathcal K$ 范数在 $\mu$ 几乎处处连续，并满足
$$
\lim_{R\to\infty}\limsup_{m\to\infty}
\int_{\{\|F\|>R\}}\|F\|^2\,d\nu_m^-=0,
\qquad
\lim_{R\to\infty}\limsup_{m\to\infty}
\int_{\{\|F\|>R\}}\|F\|^2\,d\nu_m^+=0.
\tag{4.1}
$$
则仍有 (3.3)，从而非零 $\rho_F$ 不能湮灭 $S\mathcal A$。

证明。各固定 $m$ 的积分有限，由 (2.3) 和 $F\in L^2(\mu;\mathcal K)$ 得知。因此 (4.1) 等价于将两个 $\limsup_m$ 换成 $\sup_m$：先控制足够大的 $m$，再用有限个绝对连续边缘的尾可积性处理剩余项。记
$$
\eta_R^\pm=\sup_m\int_{\{\|F\|>R\}}\|F\|^2\,d\nu_m^\pm\to0,
\quad
B^\pm=\sup_m\int\|F\|^2\,d\nu_m^\pm<\infty.
$$
后一个统一有限性由取一个使 $\eta_R^\pm$ 有限的固定 $R$ 即得。

作径向截断
$$
F_R(y)=
\begin{cases}
F(y),&\|F(y)\|\le R,\\
R\,F(y)/\|F(y)\|,&\|F(y)\|>R.
\end{cases}
$$
$F_R$ 有界，并在 $F$ 连续的点连续。定理 3.2 给其归一化纯迹极限
$\int\|F_R\|^2d\mu$。另一方面，真正作用于两个不同边缘的估计为
$$
\begin{aligned}
&\left|\int\big(
\langle F(x),F(y)\rangle
-\langle F_R(x),F_R(y)\rangle\big)d\nu_m\right|\\
&\qquad\le
\sqrt{\eta_R^-}\sqrt{B^+}
+\sqrt{B^-}\sqrt{\eta_R^+}.
\end{aligned}
\tag{4.2}
$$
这来自将差拆成
$\langle F-F_R,F\rangle+\langle F_R,F-F_R\rangle$，随后双边 Cauchy--Schwarz；没有把两个边缘换成原 $\mu$。

先令 $m\to\infty$，再令 $R\to\infty$，并用
$\|F_R-F\|_{L^2(\mu;\mathcal K)}\to0$，得到纯迹极限 $\lambda$。最后使用 (3.4) 支付实际 carry。证毕。

## 5. 加权固定基数子集的相关性与遗漏下界

本节给第 6 节所需的新定量输入。仍按 (2.1) 选择 $q$ 元集合 $A$，令
$$
p_j=\mathbb P(j\in A),\qquad j\ge m.
$$

### 5.1 负柱相关的直接证明

对任意正可和权序列，其基本对称多项式满足
$$
e_k^2\ge e_{k-1}e_{k+1}.
\tag{5.1}
$$
为避免隐藏相关性定理，给出证明。有限个变量时从序列 $(1)$ 开始，每加入权 $t>0$，新系数为 $b_k=a_k+ta_{k-1}$。直接展开
$$
b_k^2-b_{k-1}b_{k+1}
=(a_k^2-a_{k-1}a_{k+1})
+t(a_ka_{k-1}-a_{k-2}a_{k+1})
+t^2(a_{k-1}^2-a_{k-2}a_k).
$$
若 $a$ 非负、无内部零且对数凹，则首尾非负；相邻比值递减还给中项非负。端点按越界系数为零处理。因此归纳成立。对无限可和权取有限变量极限即得 (5.1)。

剔除两个不同指标 $i,j$，把剩余权的对称多项式记为 $E_k$。固定基数分布的分母为
$$
Z=E_q+(w_i+w_j)E_{q-1}+w_iw_jE_{q-2}.
$$
直接计算
$$
p_ip_j-\mathbb P(i,j\in A)
=\frac{w_iw_j}{Z^2}(E_{q-1}^2-E_qE_{q-2})\ge0.
\tag{5.2}
$$
条件于某些指标已经选中后，剩余分布仍是同类的固定基数加权子集分布，所以逐次使用 (5.2) 给任意有限 $J$
$$
\boxed{
\mathbb P(J\subset A)\le\prod_{j\in J}p_j.
}
\tag{5.3}
$$
当 $|J|>q$ 时左端为零。展开正乘积，进一步得到
$$
\boxed{
\mathbb E\,2^{|A\cap J|}
=\sum_{B\subset J}\mathbb P(B\subset A)
\le\prod_{j\in J}(1+p_j).
}
\tag{5.4}
$$

### 5.2 每个指标的遗漏概率下界

在去掉 $j$ 的权序列上，计数恒等式为
$$
q\,e_q(w_{\ne j})
=\sum_{\substack{|G|=q-1\\j\notin G}}
w_G\sum_{i\notin G\cup\{j\}}w_i.
$$
至多删去 $q$ 个权，因 $w_i=1/[2(i+1)^2]$ 递减，
$$
\sum_{i\notin G\cup\{j\}}w_i
\ge\sum_{i\ge m+q}w_i
\ge\frac1{2(m+q+1)}
\ge\frac1{5q}
$$
（$m\ge1$，$q=2^m\ge2$，$m\le q$）。因此
$$
\frac{e_q(w_{\ne j})}{e_{q-1}(w_{\ne j})}\ge\frac1{5q^2}.
$$
利用准确的比值
$$
\frac{p_j}{1-p_j}
=w_j\,\frac{e_{q-1}(w_{\ne j})}{e_q(w_{\ne j})},
$$
得到
$$
\boxed{
1-p_j\ge\frac{2(j+1)^2}{5q^2+2(j+1)^2}.
}
\tag{5.5}
$$
这与 R253 第三附录的反向估计
$1-p_j\le4(j+1)^2/q^2$ 相容；两者用途不同。

## 6. 无界径向类：$o(n^{3/4})$ 的实际见证排除

令
$$
V(y)=v_2(y)=\min\{j:y_j=1\},
$$
并将 $V(0)=\infty$。单点 $0$ 对所有边缘均为零测集。

**定理 6.1。** 若
$$
g:\mathbb N_0\to\mathcal K,\qquad
\|g(n)\|=o((1+n)^{3/4}),
\tag{6.1}
$$
取
$$
F(y)=g(V(y))\quad(y\ne0)
$$
并在 $0$ 任意赋一个有限值，则
$$
\frac{\phi_F(P_m)}{h_m}\longrightarrow
\lambda=\sum_{n\ge0}2^{-n-1}\|g(n)\|^2.
\tag{6.2}
$$
因此任意非零该类正态都不能湮灭两个实际慢主理想。允许任意复相位或任意 $\mathcal K$ 方向；没有单调性假设。

证明分为边缘尾和一致可积性两步。

对 $J=\{m,\ldots,m+L-1\}$，输入边缘在前 $m$ 位全零的概率为 $2^{-m}$。条件于所选 $A$，$J$ 中被选的位强制为零，其余公平，所以
$$
\nu_m^-\{V\ge m+L\}
=2^{-m}\mathbb E\,2^{-|J\setminus A|}.
\tag{6.3}
$$
由 (5.4)，
$$
\mathbb E\,2^{-|J\setminus A|}
\le\prod_{j\in J}\frac{1+p_j}{2}
\le\exp\left(-\frac12\sum_{j\in J}(1-p_j)\right).
\tag{6.4}
$$
当 $1\le L\le q$，$j+1\le m+q\le2q$，故 (5.5) 给
$$
\frac12\sum_{j=m}^{m+L-1}(1-p_j)
\ge\frac1{13q^2}\sum_{s=1}^Ls^2
\ge\frac{L^3}{39q^2}.
$$
当 $L\ge q$，前 $q$ 项给 $q/39$，随后各项至少给 $1/7$，故总和至少 $L/39$。因此
$$
\boxed{
\nu_m^-\{V\ge m+L\}
\le2^{-m}\exp\left[
-\frac1{39}\min\left(\frac{L^3}{q^2},L\right)
\right].
}
\tag{6.5}
$$
$L=0$ 的概率恰为 $2^{-m}$。

对任意固定 $p>0$，对 (6.5) 作分层求和，或把离散尾以常数调整后积分，得到常数 $C_p<\infty$，使
$$
\boxed{
\int_{\{V\ge m\}}(1+V)^p\,d\nu_m^-
\le C_p q^{-1}\big((1+m)^p+q^{2p/3}\big).
}
\tag{6.6}
$$
为付清指数：在 $0\le L\le q$ 上代换 $L=q^{2/3}u$，其 $p$ 次矩积分至多为
$C_pq^{2p/3}\int_0^\infty u^{p-1}e^{-u^3/39}du$；在 $L\ge q$ 上用 $e^{-L/39}$，该尾有界于同一量。再用
$(1+m+L)^p\le C_p((1+m)^p+(1+L)^p)$，并乘前 $m$ 位全零的概率 $q^{-1}$，即得 (6.6)。

当 $V=n<m$ 时，输入边缘的概率准确等于 Haar 值 $2^{-n-1}$。在 $V\ge m$ 上，令
$$
c_m=\sup_{n\ge m}\frac{\|g(n)\|^2}{(1+n)^{3/2}}\longrightarrow0.
$$
(6.6) 的 $p=3/2$ 情形给
$$
\int_{\{V\ge m\}}\|g(V)\|^2d\nu_m^-\le Cc_m\longrightarrow0.
\tag{6.7}
$$
故
$$
\limsup_{m\to\infty}
\int_{\{\|g(V)\|>R\}}\|g(V)\|^2d\nu_m^-
\le\sum_{\{\|g(n)\|>R\}}2^{-n-1}\|g(n)\|^2.
\tag{6.8}
$$
右端随 $R\to\infty$ 趋零。

输出边缘更简单。给定 $A$，设 $k=\min A$。则 $V(y)$ 在 $n<k$ 的概率是 $2^{-n-1}$，在 $n=k$ 的概率是 $2^{-k}$，在 $n>k$ 的概率为零。因此对每个 $n$，
$$
\nu_m^+\{V=n\}\le2\mu\{V=n\}=2^{-n}.
\tag{6.9}
$$
这直接给输出边缘的相应一致可积性，不要求 $g(n)$ 的大小单调。

函数 $F$ 在每个 clopen 环带 $\{V=n\}$ 上常值，只可能在 $0$ 不连续；它属于 $L^2(\mu;\mathcal K)$。于是 (6.8)—(6.9) 验证定理 4.1 的全部条件，得到 (6.2)，并由 (3.4) 支付实际 carry。证毕。

### 6.1 明确超出连续核与端点次数矩的例子

取标量
$$
g(n)=(-1)^n(1+n)^\alpha,\qquad 0\le\alpha<3/4.
\tag{6.10}
$$
$\alpha=0$ 时分量有界而只在 $0$ 不连续；$\alpha>0$ 时分量无界。它在每个正测度环带上交替变号，因此秩一密度不保持函数非负锥。

设非空 Walsh 集 $B$ 的最大指标为 $j$。其 Fourier 系数只依赖 $j$，准确为
$$
c_j=-2^{-j-1}g(j)+\sum_{n\ge j+1}2^{-n-1}g(n)
=2^{-j-1}\left[-g(j)+\sum_{r\ge1}2^{-r}g(j+r)\right].
\tag{6.11}
$$
取出 $(-1)^j$ 后，后面的交替级数从负项开始，且
$2^{-r}(j+r+1)^\alpha$ 严格递减（$\alpha<1$）。故该交替和非正，得到
$$
|c_j|\ge2^{-j-1}(j+1)^\alpha.
\tag{6.12}
$$
最大指标为 $j$ 的 Walsh 集共有 $2^j$ 个，故
$\sum_B|\widehat f(B)|=\infty$。此外在 $r=\sqrt3$ 时，
$$
\sum_B3^{|B|}|\widehat f(B)|^2
\ge\sum_{j\ge0}3\cdot4^j|c_j|^2
\ge\frac34\sum_{j\ge0}(j+1)^{2\alpha}
=\infty.
\tag{6.13}
$$
因此这些例子不满足 R255 的锐端点次数矩条件；$\alpha>0$ 时也没有连续核。定理 6.1 仍排除它们为慢理想见证。没有声称这一径向增长阈值最优，也没有把 (6.1) 换成无条件的 $O(n^{3/4})$。

## 7. 一般有界正态的反例与边缘集中

本节说明定理 3.2 的几乎处处连续性不能直接删除，即使保持正秩一和恒定的点态对角密度。

令
$$
L_m=\lfloor q^{1/2}\rfloor,\qquad
J_m=\{m,\ldots,m+L_m-1\},\qquad
E_m^+=\{y:y_j=1\text{ 对所有 }j\in J_m\}.
$$
R253 第三附录 §3 已证
$$
1-p_j\le\frac{4(j+1)^2}{q^2}.
$$
当 $m\le L_m$ 时，并集界给
$$
\mathbb P(J_m\nsubseteq A)
\le\frac4{q^2}\sum_{j\in J_m}(j+1)^2
\le16q^{-1/2}\longrightarrow0.
\tag{7.1}
$$
只要 $J_m\subseteq A$，输出 $y$ 就属于 $E_m^+$。因此
$$
\nu_m^+(E_m^+)\longrightarrow1,
\qquad
\mu(E_m^+)=2^{-L_m}\longrightarrow0.
\tag{7.2}
$$
这显示边缘密度不一致可积；其弱 Haar 极限不能控制任意有界可测函数。

选择 $m_0$ 充分大，使
$$
U=\bigcup_{m\ge m_0}E_m^+,\qquad
0<\theta:=\mu(U)<1/4.
\tag{7.3}
$$
这是可行的，因为 $\sum_m2^{-L_m}<\infty$，其尾和趋零。$U$ 是递增的开集：把任意物理位由 $0$ 改成 $1$ 都不会使点离开 $U$。它还是稠密集，因为任意有限头柱集都与足够高的 $E_m^+$ 相交。

由 (7.1)，
$$
\nu_m^+(U)\longrightarrow1.
\tag{7.4}
$$
输入边缘可由先取一个 Haar 点、再把所选 $A$ 位强制为零得到。因 $U$ 递增，
$$
\nu_m^-(U)\le\mu(U)=\theta.
\tag{7.5}
$$
反向极限不需要任何抽象支配收敛：令
$U_N=\bigcup_{m_0\le n\le N}E_n^+$。这是只依赖有限头的集合。对所有充分大的 $m$，输入边缘在这个固定头上恰为 Haar，所以
$$
\nu_m^-(U)\ge\nu_m^-(U_N)=\mu(U_N).
$$
先令 $m\to\infty$，再令 $N\to\infty$，得到
$$
\boxed{\nu_m^-(U)\longrightarrow\theta.}
\tag{7.6}
$$

现在取
$$
f=1-2\mathbf1_U,\qquad \rho=f\otimes f.
\tag{7.7}
$$
$f$ 实值、$|f|=1$，故 $\rho\ge0$、秩为一且 $\operatorname{Tr}\rho=1$。尽管其核的点态对角恒等于 $1$，由 (2.4)，
$$
\begin{aligned}
\frac{\operatorname{Tr}(\rho T_m)}{h_m}
&=\int f(x)f(y)\,d\nu_m\\
&=-\int f(x)\,d\nu_m+
 2\int f(x)\mathbf1_{\{y\notin U\}}\,d\nu_m.
\end{aligned}
$$
第二项的绝对值不超过 $2\nu_m^+(U^c)\to0$。用 (7.6)，得到
$$
\boxed{
\frac{\operatorname{Tr}(\rho P_m)}{h_m}
\longrightarrow-1+2\theta<-1/2.
}
\tag{7.8}
$$
从 $T_m$ 到真实 $P_m$ 的误差仍由 (3.4) 趋零。

$U$ 稠密开而 $U^c$ 有正测度，故 $f$ 在 $U^c$ 的每一点都不连续。它不满足几乎处处连续性假设；修改一个零测集也不能使它几乎处处连续：在 $\mu$ 几乎处处的 $U^c$ 点，每个邻域都含正测度的 $U^c$，而稠密开集 $U$ 在每个邻域也有正测度；两侧值均不能被零测修改消去。这个例子说明一般 $L^\infty$、恒模、正有限秩、正常性或连续的点态对角密度，都不足以推出相对迹极限为迹。

还可以保留 $C$ 实化。原反射共轭为
$Cf(y)=\overline{f(-1-y)}$，且每个 $P\in\mathcal A$ 都满足 $CP^*C=P$。于是准确有
$$
\langle P(Cf),Cf\rangle
=\langle Pf,f\rangle.
$$
因此
$$
\rho_{\mathbb R}
=\tfrac12(f\otimes f+Cf\otimes Cf)
$$
仍为迹 $1$ 的正、$C$ 不变、秩至多二密度，并有同一个负极限 (7.8)。这不构造正常湮灭者；相反，(7.8) 本身使它在充分大的 $P_m\in S\mathcal A$ 上非零。

若只想看相对测试消失的例子，取
$f_0=\mathbf1_{U^c}$。则 $\|f_0\|_2^2=1-\theta>0$，而
$$
0\le\frac{\langle T_mf_0,f_0\rangle}{h_m}
\le\nu_m^+(U^c)\longrightarrow0,
$$
故真实 $P_m$ 的相同比值也趋零。这个 $f_0$ 非负，已由 R235 的保锥定理排除为慢湮灭见证；它只是说明此指定归一化测试可能失去正迹。

## 8. 对剩余正常问题的准确意义

本稿新增三个适用层次：有界几乎处处连续的特征映射；无界但在两个边缘下满足 (4.1) 的映射；以及已明确验证 (4.1) 的径向 $o(n^{3/4})$ 类。每一层的排除都通过同一个真实 $P_m$，并支付 $e_m/h_m$。

另一方面，(7.8) 和非负 $f_0$ 例给出不能免费扩大范围的直接证据。普通 Haar $L^2$ 逼近与此处边缘下的加权逼近是不同条件；Lusin 大集合可能恰好被集中边缘避开。没有证明假想正常湮灭者自动满足 (3.1) 或 (4.1)，也没有给 R253 的完整理想范数 $q_m$ 找到非消失统一下界。

因此 R244 的见证专属配对、一般正常正湮灭者排除及普通 Hilbert ISP 仍开放。

## 已证依赖与去重

- [R253](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)：实际相位消元及 $P_m\in S\mathcal A$。
- [R253第三附录](../results/R253-appendix-identity-multiplier-vacuum-ratio-decay.md) §§2--5：真实 $e_m/h_m$、正纯尾幂展开及 (7.1) 所用遗漏概率上界。
- [连续核相对迹附录](../results/R235-appendix-continuous-kernel-relative-tail-traces.md)：本稿沿用其问题设置，但第 3--7 节是更弱正则类和明确反例；并未重复登记连续核主结论。
- R235：仅用于说明第 7 节非负 $f_0$ 不是新的湮灭者。
- R255：仅用于比较 (6.13) 的端点正则性，不在新耦合证明中作为假设。
