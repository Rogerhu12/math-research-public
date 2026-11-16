# R271 附录：跨头有限前缀真核比较、首头可和增益与完整移动来源行

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿用原真实一位 carry 和一个有限物理池，把当前完整一远孔核投影送入下一头的有限前缀真核。由此得到固定首头的可和增益；结合已付移动 coherent 行，进一步得到任意同一物理向量的整个 moving-head 来源平方和。实际 $w\in W$ 还具有一个不需要跨头修复的直接加强，单独说明其来源。所有结论只控制准确的 primitive 首反馈，未控制核外 $r=(I-P_{\ker C})Gv$、其第二逆或普通 ISP。

内积对第一变量线性。以下空间均为原 N/Y 的同一个二进制物理 $\ell^2(\mathbb N_0)$；不更换无限张量积参考。

依据：

- [原头、权与真实列](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)，§1。
- [首二进位的真实平方界及 Cayley 逆](R271-appendix-first-binary-bit-uniform-physical-schur-and-exact-top-source.md)，§1。
- [原一步 carry 与正规修复](R271-appendix-regular-one-step-correction-and-same-neumann-canonical-forcing.md)，§2。
- [偶段可达核与第二 Green](R271-appendix-even-strong-prefix-reachable-kernel-and-first-head-second-green-schur.md)。
- [真一远孔核及物理两孔正 Schur](R271-appendix-first-head-true-one-hole-kernel-elimination-and-two-hole-positive-schur.md)，§§1–3。
- [原相对孔 Riordan 与完整来源运输](R271-appendix-relative-hole-riordan-conjugacy-full-bare-source-transport-and-uniform-budget.md)，§§5–6。
- [移动第一远孔 Bessel](R271-appendix-moving-first-far-coherent-row-bessel-and-matched-source-cost.md)，§§1–2。
- [原顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)，§2。

## 1. 适用序列与两个真实核

取 $m\ge m_0\ge10$，$D_m=2^m$。
选择偶数 $R_m$，并令
$$
x_m=m+R_m,\qquad h_m=D_m+R_m,\qquad
C_m=A_m+D_{[m,x_m)}.
$$
本稿的跨头结论要求
$$
x_m\ge D_m,\qquad
\log x_m\le13D_m^3,\qquad
y_m=(m+1)^4x_m,\qquad
y_m+6D_m\le x_{m+1}.
\tag{1.1}
$$
全部端点为整数。原强头真空投影记为 $P_{x_m}$。在共同物理空间中定义
$$
\mathscr K_{0,m}
=\ker C_m\otimes\Omega_{\ge x_m},
$$
$$
\mathscr K_{1,m}
=\ker(C_m+D_{x_m})\cap\{N_{\ge x_m}\le1\},
\qquad \Pi_{j,m}=P_{\mathscr K_{j,m}}\quad(j=0,1).
\tag{1.2}
$$
$\mathscr K_{0,m}\subset\mathscr K_{1,m}$，但本稿不假设不同 $m$ 的这些空间嵌套。

设
$$
S_m=\sum_{i\ge x_m}(i+1)^{-4},\qquad
\omega_m=\sum_{i\ge x_m}(i+1)^{-2}e_i.
$$
令 $K_m^C=\ker C_m$、$G_m^C=(C_mC_m^*)^\dagger$、
$\Gamma_m=P_{K_m^C}G_m^C|_{K_m^C}$。
偶 $R_m$ 的已付结论给
$K_m^C\perp\ker C_m^*$，所以 $K_m^C\subset\operatorname{Ran}C_m$。
本稿的 MP 只属于每个有限强头，均取完整原物理度量。
$C_m+D_{x_m}$ 是有界原算子；限制到远孔数至多一的闭空间后，
(1.2) 的核仍闭，所以 $\Pi_{j,m}$ 是真正的正交投影。
记原 coherent 读行
$$
\beta_x=\frac{D_xP_{\{N_{\ge x}=1\}}}{\sqrt{S_x}}:
\mathcal H\longrightarrow\mathcal H_{<x},
$$
其中输出远位全部是真空并与强头空间等距识别。
它不读取远孔数 $\ge2$ 的任何分量。
下文的无限行和均先对有限 $m$ 求和，再由非负单调极限取得。

## 2. 一位头 carry 的原全块界

本节写 $d=2^m$。沿新 bit $m$ 的真空／占据分块，准确有
$$
A_{m+1}=
\begin{pmatrix}A_m&b_mI+\Delta_m^{01}\\0&A_m\end{pmatrix}
=A_m+b_mE_m+\Delta_m,
\qquad b_m=(m+1)^{-2}.
\tag{2.1}
$$
这里 $\Delta_m$ 就是原物理重分组的一步 carry；
不是把 $T-L_m$ 的全尾和当成单一步。

为保留足够余量，直接从原链权推一个共同界。
原链权记为 $d_j$，与头维数 $d=2^m$ 不同。准确有
$$
W_n=\prod_{j:\operatorname{bit}_j(n)=1}d_j,\quad W_0=1,\qquad
B_m e_n=\frac{W_n}{W_{n-1}}e_{n-1},\qquad
\alpha_j=\frac{d_j}{\prod_{i<j}d_i},\qquad
N_{i,m}=B_m^{2^i}/d_i.
$$
对 $i<m$，置 $q=2^i$。按 bit $m$ 为 $0,1$ 的次序，
$$
N_{i,m+1}=
\begin{pmatrix}N_{i,m}&Z_{i,m}\\0&N_{i,m}\end{pmatrix},
\qquad
Z_{i,m}=\frac{\alpha_m}{\alpha_i}
\sum_{s=0}^{q-1}|e_{d-q+s}\rangle\langle e_s|.
\tag{2.1a}
$$
这完全由每个交叉输入 $e_{d+s}$ 的真实系数得到：
$$
\frac{W_{d+s}}{d_iW_{d+s-q}}
=\frac{d_m}{d_i^2\prod_{j=i+1}^{m-1}d_j}
=\frac{\alpha_m}{\alpha_i}
\qquad(0\le s<q).
$$
其余输入要么留在同一个对角块，要么被降成零。
因此其交叉块准确满足
$$
\|Z_{i,m}\|=\frac{\alpha_m}{\alpha_i}
\le\frac{\alpha_m}{\alpha_{m-1}}
=\kappa_{m-1}:=\frac{d_m}{d_{m-1}^2}.
\tag{2.2}
$$
各输入与输出均为相异物理坐标，所以这确是原物理算子范数。
$\alpha_{j+1}/\alpha_j=d_{j+1}/d_j^2=\kappa_j<1$，
给出 (2.2) 的单调比较。顶项则严格为
$$
N_{m,m+1}=\begin{pmatrix}0&I\\0&0\end{pmatrix}=E_m.
$$

N 型的原公式是 $A_m=\sum_{i<m}b_iN_{i,m}$；
所以 $\Delta_m^{01}=\sum_{i<m}b_iZ_{i,m}$，
直接给 $\|\Delta_m\|\le2\kappa_{m-1}$。
Y 型的原公式是 $A_m=\sum_{i<m}b_iN_{i,m}(I+N_{i,m})^{-1}$。
对 (2.1a) 的完整上三角二块，Cayley 交叉项准确为
$$
\left[N_{i,m+1}(I+N_{i,m+1})^{-1}\right]_{01}
=(I+N_{i,m})^{-1}Z_{i,m}(I+N_{i,m})^{-1}.
\tag{2.3}
$$
原 $\|N_{i,m}\|\le1$、$\|N_{i,m}^2\|\le\kappa_i<1/3$
给 $\|(I+N_{i,m})^{-1}\|\le3$。
新增顶项 $i=m$ 满足 $N_{m,m+1}=E_m$、$E_m^2=0$，
所以其 Cayley 项仍准确为 $E_m$。
因此 Y 型的 $\Delta_m^{01}$ 就是 (2.3) 乘 $b_i$ 后的完整和，
两个对角块仍是同一个原 $A_m$。
在原重分组 $L_m=A_m+\sum_{i\ge m}b_iE_i$ 下，
$L_{m+1}-L_m=\Delta_m$（张量余位恒等）；
这就是所引正规修复稿 §2 的单项 $K_m$。
用 $\sum_i b_i<2$，两型统一得到
$$
\boxed{
\|\Delta_m\|\le18\kappa_{m-1},\qquad
-\log\kappa_{m-1}
=\frac{175}{2}d^4-\frac{315}{4}d^3+150d.
}
\tag{2.4}
$$
原 $\alpha_i$ 的单调性及最后一式均来自
$-\log d_i=100\,16^i-105\,8^i+(150i+25)2^i$。
这里只是一步有限块的原范数界；没有对任何 MP 作小扰动。

## 3. 一远孔真核的有限截断是收缩

固定当前 $m$，暂写 $C=C_m$、$K=\ker C$、$S=S_m$、$x=x_m$。
对任意 $f\in\operatorname{Ran}P_x$，完整一远孔核投影有
$$
k_1=\Pi_{1,m}f=k_0+\mathcal J a,\qquad
k_0=\Pi_{0,m}f,\qquad a\in K,
$$
$$
\mathcal J a
=-\sqrt S\,C^\dagger a\otimes\Omega+
a\otimes\omega_m/\sqrt S,\qquad k_0\perp\mathcal J a.
\tag{3.1}
$$
完整核还含 $K\otimes\omega_m^\perp$ 的所有一孔 dark 来源；
它们与远真空 forcing $f$ 正交，所以在 (3.1) 的投影中准确为零。
这里
$$
\mathcal J^*\mathcal J=I+S\Gamma,\qquad
\mathcal J^*(g\otimes\Omega)
=-\sqrt S\,P_K(C^*)^\dagger g,
$$
完整 graph 的正规方程给出唯一 $a$；没有把这个投影改成候选最小源。

对 $y\ge x$，记 $S_y=\sum_{i\ge y}b_i^2$、$t=S_y/S$，
并置 $\omega_{[x,y)}=\sum_{x\le i<y}b_i e_i$。定义
$$
k^{[y]}
=k_0-\frac{S-S_y}{\sqrt S}C^\dagger a\otimes\Omega+
a\otimes\omega_{[x,y)}/\sqrt S.
\tag{3.2}
$$
由于 $CC^\dagger a=a$，有
$$
(A_m+D_{[m,y)})k^{[y]}=0.
\tag{3.3}
$$
这是真有限前缀核，而非直接截断一个核后留下残量。

原物理正交性还给
$$
\|k^{[y]}\|^2
=\|k_0\|^2+(1-t)^2S\|C^\dagger a\|^2+(1-t)\|a\|^2
\le\|k_1\|^2\le\|f\|^2,
$$
$$
\boxed{
\|k_1-k^{[y]}\|^2
=t^2S\|C^\dagger a\|^2+t\|a\|^2
\le t\,\|\mathcal Ja\|^2\le t\|f\|^2.
}
\tag{3.4}
$$
因此这一截断既是收缩，又保留准确核方程；没有使用 $C^\dagger$ 的环境范数。

取 (1.1) 的 $y=y_m$，原尾积分比较得到
$$
t_m\le\left(\frac{x_m+1}{y_m}\right)^3
\le\frac8{(m+1)^{12}},\qquad
\sqrt{t_m}\le\frac3{(m+1)^6}.
\tag{3.5}
$$

## 4. 六倍头长的新物理池修复整个 carry

把 (3.3) 改按前 $m+1$ 位分组。令
$$
A_0=A_m+b_mE_m,\qquad A_1=A_{m+1},\qquad
D_{\rm old}=D_{[m+1,y_m)}.
$$
这些定义始终使用原 N/Y 权；有
$$
(A_0+D_{\rm old})k^{[y_m]}=0,\qquad
A_0^{d+1}=0,\qquad A_1^{2d}=0.
$$
新头产生的残量是
$$
r=\Delta_m k^{[y_m]}.
$$
$D_{\rm old}$ 与全部头因子对易，所以对每个 $j\ge0$，
$$
D_{\rm old}^j r
=\Delta_m(-A_0)^j k^{[y_m]}.
\tag{4.1}
$$
特别 $D_{\rm old}^{d+1}r=0$。置 $B=A_1+D_{\rm old}$，
二项展开给
$$
\boxed{B^{3d}r=0.}
\tag{4.2}
$$
这是针对同一个真实残量的终止阶数，不是 $B$ 在整个旧前缀上的环境幂零阶数。

使用全新的原物理池
$$
\mathcal I_m=[y_m,y_m+6d),\qquad D_{\rm pool}=\sum_{i\in\mathcal I_m}b_iE_i.
$$
它与旧来源支撑不交，且由 (1.1) 完全位于新前缀 $[0,x_{m+1})$。
池长记为 $N_p=6d$，定义
$$
v_q=\frac{(N_p-q)!}{N_p!}
\sum_{\substack{I\subset\mathcal I_m\\|I|=q}}
  \left(\prod_{i\in I}b_i^{-1}\right)e_I,\qquad v_0=\Omega .
$$
直接逐位计数得
$$
D_{\rm pool}v_q=v_{q-1},\qquad
\|v_q\|^2
\le\frac{(N_p-q)!}{N_p!\,q!}\,b_{\min}^{-2q},
\quad b_{\min}\ge(y_m+6d)^{-2}.
\tag{4.3}
$$
取整个有限候选
$$
\mathcal U r=\sum_{\ell=0}^{3d-1}(-B)^\ell r\otimes v_{\ell+1}.
\tag{4.4}
$$
(4.2) 与 (4.3) 的有限望远镜严格给
$(B+D_{\rm pool})\mathcal U r=r$。
没有无穷 Neumann 级数，也没有省略末端。

原头范数 $\|A_1\|<6$、$\|A_0\|<7$，结合 (4.1) 给
$$
\|B^\ell r\|
\le14^\ell\|\Delta_m\|\,\|k^{[y_m]}\|.
$$
(4.4) 的不同池孔数正交；只放宽 (4.3) 的有利阶乘即得
$$
\|\mathcal U r\|
\le\delta_m\|k^{[y_m]}\|,
$$
$$
\delta_m=
18\kappa_{m-1}\sqrt{3d}\,14^{3d}(y_m+6d)^{6d}.
\tag{4.5}
$$
用 (1.1)、$x_m\ge d$，
$$
\log(y_m+6d)\le13d^3+4\log(m+1)+1.
$$
故
$$
\log\delta_m
\le-\frac{19}{2}d^4+\frac{315}{4}d^3
+24d\log(m+1)+6d+3d\log14
+\log18+\tfrac12\log(3d).
$$
当 $m\ge10$，后三类正项总和小于 $d^4/2$：
可分别用 $(315/4)d^3\le d^4/8$、
$24d\log(m+1)\le d^4/8$，以及其余项 $\le d^4/8$。
因此
$$
\boxed{\delta_m\le e^{-9D_m^4}.}
\tag{4.6}
$$

(4.4) 含有限个物理向量，故属于原算子的自然定义域；
它的最高新池孔数是 $3d$，(4.2) 正好消掉这个末端。
将全部未使用的新前缀位保持真空，得到
$$
\widetilde k_m=k^{[y_m]}-\mathcal U r\in\mathscr K_{0,m+1}.
$$
结合 (3.4)–(4.6)，对全部原强头 forcing 一致有
$$
\boxed{
\|\widetilde k_m-\Pi_{1,m}f\|
\le\varepsilon_m\|f\|,\qquad
\varepsilon_m=\frac3{(m+1)^6}+e^{-9D_m^4}.
}
\tag{4.7}
$$
所有修复均在同一个实际核来源上进行；整个池、所有旧孔层及 carry 词均保留。

## 5. 固定首头的投影增益与两项完整能量可和

现在固定同一个物理 $f_1=e_1$，含其余位真空，$\|f_1\|=1$。
令
$$
q_{j,m}=\|\Pi_{j,m}f_1\|^2\quad(j=0,1),\qquad
g_m=q_{1,m}-q_{0,m}\ge0.
$$
以 (4.7) 的真新核向量代入投影最优性，得到
$$
\boxed{
q_{0,m+1}\ge q_{1,m}-\rho_m,\qquad
\rho_m=2\varepsilon_m+\varepsilon_m^2.
}
\tag{5.1}
$$
证明只用
$\|f_1-\widetilde k_m\|^2
\le\|f_1-\Pi_{1,m}f_1\|^2+2\varepsilon_m+\varepsilon_m^2$。
这不声称两个整个核空间已经嵌套。

望远镜给
$$
\boxed{
\sum_{m=m_0}^{\infty}g_m
\le1-q_{0,m_0}+\sum_{m=m_0}^{\infty}\rho_m<\infty .
}
\tag{5.2}
$$
特别 $q_{0,m}$ 有极限，且 $q_{1,m}-q_{0,m}\to0$。
例如 $\rho_m\le9/(m+1)^6+3e^{-9D_m^4}$，
故右端误差和不超过
$9/(5m_0^5)+6e^{-9D_{m_0}^4}$。

把同一个首头来源代回原完整 Schur：
$$
v_m=(I+S_m\Gamma_m)^{-1}e_0.
$$
因为原两型都有 $C_me_1=e_0$、$e_0\in K_m^C$，
且 $(C_m^*)^\dagger e_1=G_m^Ce_0$，
(3.1) 的 graph 正规方程在此准确给
$a_m=-\sqrt{S_m}\Gamma_mv_m$。于是
$$
\boxed{
\begin{aligned}
g_m
&=S_m\left\langle\Gamma_me_0,
             (I+S_m\Gamma_m)^{-1}\Gamma_me_0\right\rangle\\
&=S_m\|\Gamma_mv_m\|^2
 +S_m^2\|C_m^\dagger\Gamma_mv_m\|^2.
\end{aligned}}
\tag{5.3}
$$
所以两项的整个跨 $m$ 平方和都已支付。
同时
$\sum_m\|v_m-e_0\|^2/S_m<\infty$。
这些是同一个完整最小来源的真实能量，
没有把第一逆压缩 $\Gamma_m$ 换成核外 $G_m^C$。

## 6. 任意同一物理向量的全部 moving-head 来源

令 $w$ 为任意原物理 Hilbert 向量，不要求 $w\in W$。
取
$$
f_m=P_{x_m}w,\qquad
\mathcal G_m=(\Pi_{1,m}-\Pi_{0,m})P_{x_m},\qquad
h_m^{\rm gain}=\mathcal G_mw=\mathcal J_ma_m,\qquad
\mathfrak g_m=\|h_m^{\rm gain}\|^2.
$$
这里 $h_m^{\rm gain}$ 是向量，勿与头幂零长度 $h_m$ 混同。
$\|a_m\|\le\sqrt{\mathfrak g_m}$。
用 (4.7) 近似 $k_{1,m}=\Pi_{1,m}f_m$，并以
$\|P_{\mathscr K_{0,m+1}}w\|^2
\ge2\Re\langle w,\widetilde k_m\rangle-\|\widetilde k_m\|^2$，
得到
$$
\begin{aligned}
\mathfrak g_m
\le{}&\|\Pi_{0,m+1}w\|^2-\|\Pi_{0,m}w\|^2\\
&-2\Re\langle\beta_{x_m}w,a_m\rangle
+\rho_m'\|w\|^2,\qquad
\rho_m'=4\varepsilon_m+\varepsilon_m^2.
\end{aligned}
\tag{6.1}
$$
唯一交叉项来自真正远一孔，因为
$$
2\Re\langle w,k_{1,m}\rangle-\|k_{1,m}\|^2
=\|\Pi_{0,m}w\|^2+\mathfrak g_m
 +2\Re\langle\beta_{x_m}w,a_m\rangle.
$$
此处 $f_m$ 随 $m$ 改变的差额没有丢掉；它正由这个交叉保留。

(1.1) 保证 $x_{m+1}\ge2(x_m+1)$，所以已付原全头 Bessel 给
$$
\sum_m\|\beta_{x_m}w\|^2\le B_2\|w\|^2,\qquad
B_2=\frac{1+2^{-3/2}}{1-2^{-3/2}}<3.
$$
且 $\rho_m'\le5\varepsilon_m$，从而
$\sum_{m\ge m_0}\rho_m'
\le3/m_0^5+10e^{-9D_{m_0}^4}<1$。
对 (6.1) 求有限和、望远镜，再用一次共同 Cauchy，记
$D_M=\sum_{m=m_0}^M \mathfrak g_m$，得到
$$
D_M\le2\|w\|^2+2\sqrt{3}\|w\|\sqrt{D_M}.
$$
解此二次不等式并取单调极限：
$$
\boxed{
\sum_{m=m_0}^{\infty}\|\mathcal G_mw\|^2
\le(\sqrt3+\sqrt5)^2\|w\|^2
<16\|w\|^2.
}
\tag{6.2}
$$
这是完整 moving-head 行，不是固定一个头列后的强收敛。

写 $f_m=i_{0,m}g_m^{\rm head}$，定义原同源
$$
\theta_m=P_{K_m^C}(C_m^*)^\dagger g_m^{\rm head},\qquad
t_m=(I+S_m\Gamma_m)^{-1}\theta_m.
$$
(3.1) 中 $a_m=-\sqrt{S_m}\,t_m$，因此 (6.2) 等价于
$$
\boxed{
\sum_m\left[
S_m\|t_m\|^2+
S_m^2\|C_m^\dagger t_m\|^2
\right]\le16\|w\|^2.
}
\tag{6.3}
$$
它允许原全部头维数、完整 $K_m^C$ 和全部强位 nuisance；
没有用环境 $(C_m^*)^\dagger$ 范数替换这些指定来源。

## 7. 实际 $W$ 来源的独立加强与原 cut

本节不要求 (1.1) 或 §§2–4 的跨头修复。
另取任何偶数 $R_m$ 与 $x_m=m+R_m$，
只要求同一原母窗口有 $Q_m\ge R_m+1$，并且
$x_{m+1}\ge\lambda(x_m+1)$ 对一个固定 $\lambda>1$ 成立。
其余 $C_m,K_m^C,\Pi_{j,m},f_m,\mathcal G_m$ 按 §§1、3、6 定义。
令
$$
B_\lambda=\frac{1+\lambda^{-3/2}}{1-\lambda^{-3/2}}.
$$

对于实际同一个 $w\in W$，已付原真实投影定理在全部合法
$4D_m\le Q_m\le\exp((1601/64)D_m^3)$ 上一致给
$$
u_{m,Q_m}=(P_{V_{m,Q_m}}-P_{K_{m,Q_m}})w,\qquad
\|u_{m,Q_m}-P_{\mathcal N_m\le Q_m}w\|
\le2\eta_m\|w\|,\quad \eta_m=e^{-6D_m^4}.
$$
这是对整个允许 $Q_m$ 窗的同一误差，不是固定 $Q$ 或逐列的强收敛。
$u_{m,Q_m}$ 正交于原 $K_{m,Q_m}$。
而 $h_m^{\rm gain}=\mathcal G_mw$ 是真实 $L_m$ 核，
原 $m$ 后总尾孔数至多 $R_m+1$，
故属于这个同一 $K_{m,Q_m}$。
因此
$$
\left|\mathfrak g_m+\langle\beta_{x_m}w,a_m\rangle\right|
=|\langle w,h_m^{\rm gain}\rangle|
\le2\eta_m\|w\|\sqrt{\mathfrak g_m}.
$$
若 $\mathfrak g_m>0$，除以其平方根；若为零，下式直接成立：
$$
\sqrt{\mathfrak g_m}
\le\|\beta_{x_m}w\|+2\eta_m\|w\|.
$$
由完整移动 coherent 行 Bessel，
$$
\boxed{
\sum_m \mathfrak g_m
\le2B_\lambda\|w\|^2+8\|w\|^2\sum_m\eta_m^2.
}
\tag{7.1}
$$
于是原 same-$w$ 逼近来源也满足 (6.3)，并有这里的独立常数。
这一证明仅用真核正交与整行 Bessel，不需要不同 $m$ 的核投影近单调。
例如 $R_m=D_m$ 在充分大 $m$ 可取 $\lambda=3/2$；
这个例子不携带 Riordan 帽运输。

对 §§1–6 的跨头序列，取 $Q_m=D_m^2h_m$，则
$$
4D_m\le Q_m<e^{14D_m^3}
<e^{(1601/64)D_m^3}
$$
对 $m\ge10$ 成立，且 $Q_m\ge R_m+1$。
下一个 $m+1$ 也用同一个公式。
修复后的 $\widetilde k_m$ 所有物理位都小于 $x_{m+1}$，
所以在原 $m+1$ 后孔数至多 $R_{m+1}$；
因而它还属于真正的 $K_{m+1,Q_{m+1}}$。
这同时核清了有限池支撑、$m+1$ 分组与两个母窗口。

若进一步采用下一节的原 Riordan 强位尺度，
令 $n_{0,m}=Q_m/2$，全部真帽 cut 可取
$$
n_{0,m}\le n\le Q_m-R_m-2h_m-1.
$$
其数目 $N_m=Q_m/2-R_m-2h_m$ 满足
$h_m/N_m\le3/D_m^2$。
这保留了全部 $h_m$ 段、$n+2h_m+R_m<Q_m$ 的真帽门，
以及原 matched 来源平均中 $h_m/N_m$ 的平方可和误差。
这里没有把别的较小 $R$ 自动当作已付帽参数。
(7.1) 始终只支付指定 primitive 行，不把核外返回或帽源逆置零。

## 8. 一个与原 Riordan 尺度相容的明确选择

令
$$
\tau_{14,m}
=\frac{\Lambda_{m-1}+14D_m^3+\log16}{D_m/2-1},
\qquad
R_m=2\left\lceil2e^{\tau_{14,m}}\right\rceil,
\qquad x_m=m+R_m,
$$
其中 $\Lambda_i=-\log d_i$ 使用原链权；
$D_m=2^m$ 始终只表示头维数。

直接代原 $\Lambda_{m-1}$ 可得，对 $m\ge10$，
$$
\frac{25}{2}D_m^3\le\tau_{14,m}
\le\frac{51}{4}D_m^3,\qquad
\log x_m\le13D_m^3.
$$
下一个 $\tau_{14,m+1}\ge100D_m^3$，
故 $(m+1)^4x_m+6D_m\le x_{m+1}$。
这证明 (1.1) 的全部参数条件。

该 $R_m$ 是原 $4e^{\tau_{14,m}}$ 强位尺度向上取最近偶数：
仍有 $\|D_{x_m}\|\le e^{-\tau_{14,m}}/4$、
$h_m\le6e^{\tau_{14,m}}$。
因此原 Riordan 父稿的正反环境预算所用不等式保持；
本稿不通过 $R=d$ 或另一个较小尺度免费调用帽运输。
选择上一节的 $Q_m=D_m^2h_m$ 还保其严格内部端点。

## 9. 准确未付项

固定首头的 (5.3) 和 moving 来源的 (6.3)/(7.1)
控制的都是完整 primitive 首反馈。
原两孔稿中的
$$
r_m=(I-P_{K_m^C})G_m^C(I+S_m\Gamma_m)^{-1}e_0
$$
仍含核外 Schur；本稿没有估计
$(C_m^*)^\dagger r_m$ 或其物理正饱和费用。
不能把可和的 $S_m\|\Gamma_mv_m\|^2$
替换成 $S_m\|G_m^Cv_m\|^2$。

新的跨头比较是有限物理核向量的可重建运输，
没有证明这些有限核的并在原 $M$ 中稠密。
因此也不由投影的可和增益、同 $w$ 行界或母窗口合法性，
宣称 $N=M$ 或普通 ISP 已完成。
