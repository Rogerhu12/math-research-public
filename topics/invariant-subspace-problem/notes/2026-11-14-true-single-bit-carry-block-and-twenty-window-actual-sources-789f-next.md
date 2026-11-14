# 原单新位 carry 的准确块形与 \(e^{20d^3}\) 实际源窗口

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

状态：本文的真实块形、母提升及同一个实际顶部的整窗两费用均已证明。原深联合旗的量化参数不随窗口自动扩大；角度/负图比较及 \(N=M\) 仍未证明。

## 0. 严格增量

[十六窗口母提升](2026-11-14-extended-linear-mother-window-sixteen-and-true-stable-lift-789f-next.md)
用完整 \(2z\) 头和一般新残量导数，付
\(52\eta R(1+bR)H_p(R)H_{p+1}(R)\)。
本稿利用原 \(N/Y\) 模型新位的实际块，证明对于真正逐头残量：

\[
 K_pE_p=0,\qquad
 A_{p+1}^jK_p=A_p^jK_p,\qquad
 A_{p+1}^{\,z}K_p=0,\quad z=2^p.
 \tag{0.1}
\]

因此只对这个残量，修复和可截到 \(j<z\)，导数中的 \(1+bR\) 也严格消失。一步成本变为

\[
 \boxed{52\eta_{p-1}R\,H_p(R)^2.}
 \tag{0.2}
\]

保有限 \(j<z\) 而不用无穷区间 Legendre 上界后，得到：

* \(m\ge10,d=2^m,Q\le e^{20d^3}\) 时，原有限物理核线性提升到 \(N\)，相对误差至多 \(e^{-3d^4}\)；
* 同范围的实际 \(w\in M\) 低输出投影误差至多 \(e^{-3d^4}\)；
* 对 \(w\in M\ominus N\)，同一个顶部最小者误差至多 \(2e^{-3d^4}\)；它的全部较低完整未来窗保原 bare/flat 两投影及累计费用。

所有空间和输入仍为原物理空间，位置可无限。没有将一个一般右逆在全域截短，也没有从 \(A_p^jK_pA_p^k\) 中重复扣除 carry。

## 1. 原 \(N/Y\) 真实有限头的逐位块形

令旧头含位 \(0,\ldots,p-1\)，\(z=2^p\)。
把新第 \(p\) 位按占据 \(0,1\) 排成两块，每块保原旧头内积。
物理新位删除记为

\[
 E_p=\begin{pmatrix}0&I\\0&0\end{pmatrix}.
\]

实际加权后移满足

\[
 B e_n=\alpha_{v_2(n)}e_{n-1},\qquad
 W_n=\prod_{i\in{\rm bits}(n)}d_i.
\]

对每个 \(i<p\)，原 \(N_i=B^{2^i}/d_i\) 的新有限头有准确块形

\[
 N_i^{[p+1]}
   =\begin{pmatrix}
       N_i^{[p]}&C_{i,p}^{N}\\
       0&N_i^{[p]}
     \end{pmatrix}.
 \tag{1.1}
\]

这是原加权减法的直接分块：不跨第 \(p\) 位时，两对角块是相同旧头；跨位借一时只产生右上块。
第 \(p\) 项则为

\[
 N_p^{[p+1]}=E_p.
 \tag{1.2}
\]

确实 \(W_{z+r}=d_pW_r\) 对 \(0\le r<z\) 成立，所以 \(B^z/d_p\) 把 \((r,1)\) 准确送到 \((r,0)\)，系数为一。

对 \(Y_i=N_i(I+N_i)^{-1}=I-(I+N_i)^{-1}\)，令
\(R_i=(I+N_i^{[p]})^{-1}\)。块逆直接给

\[
 Y_i^{[p+1]}
  =\begin{pmatrix}
      Y_i^{[p]}&R_iC_{i,p}^{N}R_i\\
      0&Y_i^{[p]}
    \end{pmatrix}
   \quad(i<p).
 \tag{1.3}
\]

原有限头幂零，所以这里的逆是完整有限多项式逆。
又因 \(E_p^2=0\)，\(Y_p^{[p+1]}=E_p\)。

令 \(b_p=(p+1)^{-2}\)，并把各个 \(i<p\) 的真实非对角块按原 \(b_i\) 求和，记为 \(C_p\)。对两个模型均准确有

\[
 \boxed{
 A_{p+1}
   =\begin{pmatrix}
       A_p&b_p I+C_p\\
       0&A_p
     \end{pmatrix},\qquad
 K_p:=A_{p+1}-(A_p+b_pE_p)
   =\begin{pmatrix}0&C_p\\0&0\end{pmatrix}.
 }
 \tag{1.4}
\]

这里 \(A_p\) 在两块上对角作用。
没有假设 \([A_p,C_p]=0\)。
因为任意两个严格右上块的乘积为零，直接得到

\[
 K_pE_p=E_pK_p=0,\qquad
 A_{p+1}^jK_p=A_p^jK_p\quad(j\ge0),
 \qquad A_{p+1}^{z}K_p=0.
 \tag{1.5}
\]

全物理纯尾模型 \(L_p=A_p+D_p\) 满足
\(L_{p+1}-L_p=K_p\)，其中
\(D_p=b_pE_p+D_{p+1}\)。
因此原真实估计原样给

\[
 \|K_p\|\le52\eta_{p-1},\qquad
 \eta_{p-1}\le e^{-80z^4}\quad(p\ge5),
 \qquad [K_p,D_{p+1}]=0.
 \tag{1.6}
\]

最后的交换来自不交物理位；它不是把 \(K_p\) 和旧头自由交换。

## 2. 只对真实残量的短修复

设

\[
 k\in\ker(A_p+D_p)\cap\mathcal H_{\le Q'}^{(p)}.
\]

旧核关系给 \(D_p^\ell k=(-A_p)^\ell k\)。
新尾 \(D_{p+1}=D_p-b_pE_p\) 满足

\[
 D_{p+1}^{\ell}k
 =(-A_p)^\ell k
    -\ell b_pE_p(-A_p)^{\ell-1}k\quad(\ell\ge1).
\]

对真实新残量 \(r=K_pk\)，使用 (1.5)–(1.6) 得

\[
 \boxed{
 D_{p+1}^{\ell}r=K_p(-A_p)^\ell k
       \quad(\ell\ge0).
 }
 \tag{2.1}
\]

因此对

\[
 \mathcal U_R(f)=\sum_{\ell\ge0}\frac{R^\ell}{\ell!}
                       \|D_{p+1}^{\ell}f\|,
 \qquad
 H_p(R)=\sum_{\ell<z}\frac{R^\ell}{\ell!}\|A_p^\ell\|,
\]

准确有

\[
 \boxed{\mathcal U_R(r)
      \le52\eta_{p-1}H_p(R)\|k\|.}
 \tag{2.2}
\]

这里没有 \(1+b_pR\)；它对应的整个项已被 \(K_pE_p=0\) 杀掉。

取原物理相容右逆 \(R_t'\)，其输入孔上界为 \(Q'\)；
可仍用原 \(2z\) 最大阶的宽松参数

\[
 R=512\sqrt{Q'+2z+1}
      (p+1+Q'+2z+2)^{3/2}.
 \tag{2.3}
\]

它满足

\[
 D_{p+1}R_t'=R_{t-1}',\quad R_0'=I,\qquad
 \|R_t'f\|\le\frac{R^t}{t!}\mathcal U_R(f),
 \tag{2.4}
\]

并与所有新头算子交换。
定义仅用于当前残量的修复

\[
 c=\sum_{j=0}^{z-1}(-A_{p+1})^jR_{j+1}'r.
 \tag{2.5}
\]

相消后的终端项是
\(-(-A_{p+1})^{z}R_z'r=0\)，由 (1.5) 得

\[
 (A_{p+1}+D_{p+1})c=r.
 \tag{2.6}
\]

此外 \(R_{j+1}'r\) 仍在新位 \(0\) 块中，
所以 \(A_{p+1}^jR_{j+1}'r=A_p^jR_{j+1}'r\)。
(2.2)、(2.4) 给

\[
 \boxed{
 \|c\|\le R H_p(R)\mathcal U_R(r)
       \le52\eta_{p-1}R H_p(R)^2\|k\|.
 }
 \tag{2.7}
\]

令 \(k'=k-c\)，则 \(L_{p+1}k'=0\)，新尾孔数至多 \(Q'+z\)。

(2.5) 不是任意新输入的全域右逆。只因当前 \(r=K_pk\) 落在 (1.5) 的真实短核中，才可把通常 \(2z\) 项截为 \(z\) 项。

## 3. 有限截止给出的 \(c=20\) 余量

仍用原实际头幂

\[
 \|A_p^j\|\le6^j
       e^{-\gamma(j-p)_+^4},
 \qquad \gamma=770/256>3.
 \tag{3.1}
\]

设 \(p\ge10,z=2^p\)，并且

\[
 \Theta=\log(6R)\le\frac{81}{2}z^3.
 \tag{3.2}
\]

对 \(j<z\)，

\[
 \frac{R^j}{j!}\|A_p^j\|
 \le e^{j\Theta-\gamma(j-p)_+^4}
 \le e^{j(81/2)z^3-\gamma(j-p)_+^4}.
\]

最后一个指数作为 \(j\in[0,z]\) 的函数严格递增：
其导数不小于
\((81/2-4\gamma)z^3>0\)。
因此

\[
 \log H_p(R)
 \le\log z+\frac{81}{2}z^4-\gamma(z-p)^4.
\]

\(p/z\le10/1024<1/100\)，所以

\[
 \gamma(1-p/z)^4
 \ge3(99/100)^4>14/5.
\]

又 \(\log z\le z^4/100\)，故

\[
 \boxed{
 \log H_p(R)
 \le\frac{3771}{100}z^4
 <\frac{151}{4}z^4.
 }
 \tag{3.3}
\]

与无穷 Legendre 极值不同，这里明确保留了真正的 \(j<z\) 截止。

现在固定

\[
 m\ge10,\quad d=2^m,\quad
 1\le Q\le e^{20d^3}.
\]

第 \(n\) 步置

\[
 p=m+n,\quad z=2^p,\quad Q_n=Q+z-d.
 \tag{3.4}
\]

由 (2.3)，

\[
 R\le512(Q+5z)^2,
\]
\[
 \Theta\le9+40d^3+2\log(1+5z)
       \le\frac{81}{2}z^3.
\]

所以 (3.3) 对全部步骤都适用。
(1.6)、(2.7) 的修复系数对数至多

\[
 \log52-80z^4+\frac{81}{2}z^3+\frac{151}{2}z^4
 \le-4z^4.
\]

最后一步用 \(z\ge1024\)。因此

\[
 \boxed{\|k_{n+1}-k_n\|\le e^{-4z^4}\|k_n\|.}
 \tag{3.5}
\]

## 4. \(e^{20d^3}\) 母窗口的原稳定像提升

迭代 (2.5) 得 \(k_n\in\ker L_{m+n}\)，新尾孔数至多 \(Q_n\)。
由 (3.5)，

\[
 \|k_n\|\le2\|k_0\|,\qquad
 \|k_\infty-k_0\|
 \le4e^{-4d^4}\|k_0\|
 \le e^{-3d^4}\|k_0\|.
 \tag{4.1}
\]

原 \(L_{m+n}\to T\) 算子范数收敛，故 \(Tk_\infty=0\)。
每步差的原总孔数至多 \(Q+3z\)；因而对任意固定 \(c>0\)，

\[
 \sum_n\|e^{c\mathcal N}(k_{n+1}-k_n)\|
 \le2\|k_0\|\sum_n e^{c(Q+3z)-4z^4}<\infty.
\]

初值亦为有限孔，所以
\(k_\infty\in M\cap\operatorname{Dom}e^{c\mathcal N}\)
对每个 \(c>0\) 成立。
用原已经证明的 \(M\cap X_3\subseteq N\)，得到 \(k_\infty\in N\)。
全部步骤线性，故

\[
 \boxed{
 \Lambda^{(20)}_{m,Q}:
 \ker L_m\cap\mathcal H_{\le Q}^{(m)}\longrightarrow N,\quad
 \|\Lambda^{(20)}_{m,Q}k-k\|\le e^{-3d^4}\|k\|,
 \quad Q\le e^{20d^3}.
 }
 \tag{4.2}
\]

这里重新支付了原 Hilbert 极限和全部孔指数域，没有只证明极限落在 \(M\)。

## 5. 同一 \(c=20\) 范围的实际低输出

本节独立检查扩大后的实际低输出，不沿用旧常数。
取

\[
 4d\le Q\le e^{20d^3},\qquad
 R=512\sqrt{Q+d+1}(m+Q+d+2)^{3/2}\le2048Q^2.
\]

令 \(x=\log(2+R)\)、\(\Theta=\log(6R)\)，则

\[
 x\le\Theta\le40d^3+10\le(81/2)d^3.
\]

原完整 carry 导数和仍为

\[
 \epsilon_m(R)
 \le52\sum_{r\ge0}
       e^{-80d^4\,16^r+2(r+1)x}.
\]

相邻项比小于 \(1/2\)，且
\(\log104+2x\le\log104+81d^3\le d^4\)，故

\[
 \epsilon_m(R)\le e^{-79d^4}.
 \tag{5.1}
\]

(3.3) 适用于此旧头 \(m\)。因此

\[
 RH_m(R)\epsilon_m(R)<1/2,\qquad
 2RH_m(R)^2\epsilon_m(R)
 \le e^{-3d^4}.
 \tag{5.2}
\]

第二项的对数至多
\(\log2+(81/2)d^3+(151/2)d^4-79d^4\le-3d^4\)。

对原 \(w\in M\)，
\(Dw=-A_mw+(L_m-T)w\) 的实际导数吸收给
\(\mathcal U_R(w)\le2H_m(R)\|w\|\)。
用原物理相容右逆修复
\(P_{\le Q-1}(L_m-T)w\)，其范数由 (5.2) 支付。
因此准确正交投影

\[
 v_Q=P_{V_Q}w,\qquad
 V_Q=\mathcal H_{\le Q}^{(m)}
        \cap\ker(P_{\le Q-1}^{(m)}L_m)
\]

满足

\[
 \boxed{\|v_Q-P_{\le Q}^{(m)}w\|
                  \le e^{-3d^4}\|w\|.}
 \tag{5.3}
\]

该修复使用完整物理有限层相容逆；没有借用完整 bosonic 满射。

## 6. 真正顶部与全窗口同一个来源

设 \(w\in W=M\ominus N\)。
令 \(K_Q=\ker L_m\cap\mathcal H_{\le Q}^{(m)}\)、
\(k_Q=P_{K_Q}w=P_{K_Q}v_Q\)。
(4.2) 和 \(w\perp N\) 直接给

\[
 \|k_Q\|^2
 =\langle w,k_Q-\Lambda^{(20)}_{m,Q}k_Q\rangle,
 \qquad \|k_Q\|\le e^{-3d^4}\|w\|.
\]

取原顶部源 \(r_Q=E_Qv_Q\)，其最小左向量

\[
 u_Q=v_Q-k_Q=E_Q^\dagger r_Q
\]

满足

\[
 \boxed{
 \|u_Q\|\le\|w\|,\qquad
 \|u_Q-P_{\le Q}^{(m)}w\|
                  \le2e^{-3d^4}\|w\|.
 }
 \tag{6.1}
\]

这一步用的是单位范数核投影，不乘任何显式巨大高返回范数。

令

\[
 Q_m=\lfloor e^{20d^3}\rfloor,\qquad
 I_m^{(20)}=\{4d,\ldots,Q_m-d\},\qquad
 \varepsilon_m^{(20)}=2e^{-3d^4}.
\]

固定 \(u_m=u_{Q_m}\)。
对全部 \(p\in I_m^{(20)}\)，定义
\(r_{m,p}=A_m(u_m)_p\)。
[实际顶部与整窗稿](2026-11-14-extended-sixteen-window-actual-defect-top-and-common-two-fee-sources-789f-next.md)
§§1、5 的固定层证明没有上窗假设，因此这里仍准确有

\[
 E_{m,p}^\dagger r_{m,p}=P_{\le p}^{(m)}u_m,\qquad
 r_{m,p}\in\ker[\iota_0^*(L_{m,p}+B_{m,p})],
 \tag{6.2}
\]
\[
 F_{m,p}^*L_{m,p}r_{m,p}
   =P_{f,m,p}P_{[p+1,p+d]}^{(m)}u_m,
\]
\[
 a_{m,p}(r_{m,p})
   =-P_{b,m,p}P_{L,m,p}P_{[p+1,p+d]}^{(m)}u_m.
 \tag{6.3}
\]

前者保完整右核，后者保原低旗及裸零源最小投影。
两投影不假设正交，故

\[
 \boxed{\Xi_{m,p}(r_{m,p})^2
   \le2\|P_{[p+1,p+d]}^{(m)}u_m\|^2.}
 \tag{6.4}
\]

置
\(\tau_m=\|\mathbf1_{\{\mathcal N_{\rm tot}>4d\}}w\|\)。
同一个顶部的一次误差与真实带覆盖数给

\[
 \boxed{
 \sum_{p\in I_m^{(20)}}\Xi_{m,p}(r_{m,p})^2
 \le2d(\tau_m+\varepsilon_m^{(20)}\|w\|)^2,
 }
 \tag{6.5}
\]
\[
 \boxed{
 \sup_{p\in I_m^{(20)}}
 \|E_{m,p}^\dagger r_{m,p}-w\|
 \le\tau_m+\varepsilon_m^{(20)}\|w\|\longrightarrow0.
 }
 \tag{6.6}
\]

间距 \(d\) 的不交网格把 (6.5) 中的 \(d\) 去掉。
同一原固定低测试 \(f\) 的 Riesz 源
\(t_{m,p}=E_{m,p}P_{V_{m,p}}f\)
亦满足

\[
 \langle L_{m,p}r_{m,p},t_{m,p}\rangle
       \longrightarrow\langle w,f\rangle
\]

对整个窗口一致。
没有重选源，也没有用头相似条件数。

## 7. 当前量词及未付部分

对这一个实际、尚未消联合旗的负流图源族，新同窗比较阈值成为

\[
 \sup_{p\in I_m^{(20)}}
 \frac{\mu_{m,p}(r_{m,p})^2}
      {\Xi_{m,p}(r_{m,p})^2}
 =O(e^{20d^3}/d).
 \tag{7.1}
\]

若沿头子序列能另证 (7.1)，则与 (6.5)–(6.6) 矛盾并排除该非零缺陷 \(w\)。本稿没有证明 (7.1)。

精确源流负图 (6.2) 已在新范围成立；旧深 jets/单高块联合旗的指数小 \(\delta_m\) 仍保原已证窗口。依赖那条量化旗的正化滤波，不因本稿扩大母窗便自动在新范围取得同一个 \(\delta_m\)。

本稿只用一次真实 carry 范数，再分别支付两个旧头幂；没有宣称
\(\|A_p^jK_pA_p^k\|\) 可以免费替换为含 \(j+k\) 的一个幂界。
这样的联合改进必须另核原路径上的权，不能把已付的最高 carry 重复计入四次衰减。普通 Hilbert ISP 的完成标准保持原样。
