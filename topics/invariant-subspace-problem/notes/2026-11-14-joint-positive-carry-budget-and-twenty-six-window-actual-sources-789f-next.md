# 原联合 carry 的正系数预算与 \(e^{26d^3}\) 真实源窗口

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

状态：本文证明原 \(N/Y\) 两个模型的完整联合 carry 预算、母提升以及同一实际顶部的整窗两费用。没有证明原角度比较、扩大窗口上的旧量化联合旗或 \(N=M\)。

## 0. 新结论和费用位置

[二十窗口稿](2026-11-14-true-single-bit-carry-block-and-twenty-window-actual-sources-789f-next.md)
已经证明真实新位块及短残量：

\[
 A_{p+1}=\begin{pmatrix}A_p&b_pI+C_p\\0&A_p\end{pmatrix},
 \quad
 K_p=L_{p+1}-L_p=\begin{pmatrix}0&C_p\\0&0\end{pmatrix},
 \quad K_pE_p=0.
 \tag{0.1}
\]

本稿不再把
\(\|A_m^jK_pA_m^k\|\)
拆为三个独立范数。
对 \(m\le p\)，以同一原物理矩阵、真实跨块权和正系数逐项支配证明

\[
 \boxed{
 R\sum_{j,k<2^m}
 \frac{R^{j+k}}{(j+1)!\,k!}
 \|A_m^jK_pA_m^k\|
 \le e^{-2\cdot16^p}
 \quad(0<R\le\mathcal R_p),
 }
 \tag{0.2}
\]
\[
 \mathcal R_p=\exp\!\left(\frac{417}{8}\,8^p\right),
 \qquad p\ge10.
 \tag{0.3}
\]

\(A_m\) 在较大头上按恒等张量延拓。
(0.2) 已包含最高实际 carry 的费用，没有额外乘
\(\eta_{p-1}\)，因此没有把该衰减重复用于总幂。

它给出全部 \(m\ge10,d=2^m\) 下：

\[
 Q\le e^{26d^3}
 \Longrightarrow
 \exists\,\Lambda^{(26)}_{m,Q}:
 \ker L_m\cap\mathcal H_{\le Q}^{(m)}\to N,
 \qquad
 \|\Lambda^{(26)}_{m,Q}k-k\|\le e^{-d^4}\|k\|.
 \tag{0.4}
\]

进一步保全部 \(p\ge m\) 的真实误差及其 \(D_m\) 交换子，证明同范围实际低输出误差至多 \(e^{-d^4}\|w\|\)。
对 \(w\in M\ominus N\)，真正顶部最小者误差因而至多
\(2e^{-d^4}\|w\|\)，并保全窗口同一来源的裸/平坦预算。

## 1. 原矩阵权和两个模型的一个正系数支配函数

沿原物理基

\[
 B e_n=\frac{W_n}{W_{n-1}}e_{n-1},\qquad
 W_n=\prod_{i\in{\rm bits}(n)}d_i,\qquad
 d_i=e^{-\Lambda_i},
\]
\[
 \Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i,
 \qquad d_0=e^{-20}.
 \tag{1.1}
\]

固定 \(p\ge10,z=2^p\)。设 \(B_{p+1}\) 为原前 \(p+1\) 位头。
原低 \(p\) 位标量函数分别为

\[
 F_{N,p}(s)=\sum_{i<p}b_i\,\frac{s^{2^i}}{d_i},
 \qquad
 F_{Y,p}(s)=\sum_{i<p}b_i\,\frac{s^{2^i}}{d_i+s^{2^i}},
 \quad b_i=(i+1)^{-2}.
\]

取非负 Taylor 系数函数

\[
 \boxed{
 g_p(s)=\sum_{i<p}b_i\frac{s^{2^i}}{d_i-s^{2^i}}.
 }
 \tag{1.2}
\]

两个 \(F\) 的每个 Taylor 系数的绝对值都被 \(g_p\) 的同阶系数支配。
对 \(Y\)，这是先保各项完整几何级数，再用三角不等式；不同 \(i\) 的抵消没有被当作正性。

在 \(B_{p+1}\) 上所有函数均按幂零截断代入。
按新位 \(0,1\) 分块，写

\[
 g_p(B_{p+1})
 =\begin{pmatrix}\mathsf A_p&\mathsf C_p\\0&\mathsf A_p\end{pmatrix}.
 \tag{1.3}
\]

这两个块的所有物理矩阵条目非负。
(0.1) 的真正 \(C_p\) 是低函数 \(F_{N,p}\) 或 \(F_{Y,p}\) 的相同跨块，故

\[
 |C_p|\le\mathsf C_p
 \quad\hbox{逐条目}.
 \tag{1.4}
\]

这里 \(i=p\) 项是准确 \(b_pE_p\)，已经从 \(K_p\) 中减去；它没有留在支配跨块中。

同样，对任意 \(m\le p\)，将 \(A_m\) 在位 \(m,\ldots,p-1\) 上张量恒等，
有

\[
 |A_m|\le\mathsf A_p
 \quad\hbox{逐条目}.
 \tag{1.5}
\]

证明是按这些高位的固定二进制块查看对角块：
\(g_p(B_p)\) 的该对角块为 \(g_m(B_m)\)，包含原 \(A_m\) 的全部绝对系数；其余跨块均非负。没有把 \(A_m\otimes I\) 误称为整个 \(F_m(B_p)\)。

## 2. 双 factorial 和保留一个真正跨块

由 (1.4)–(1.5)，

\[
 |A_m^jC_pA_m^k|
 \le\mathsf A_p^j\mathsf C_p\mathsf A_p^k
 \le [\,g_p(B_{p+1})^{\,j+k+1}\,]_{01}.
 \tag{2.1}
\]

最后一个跨块是全部可能跨块位置的非负和，包含左边指定的那一项；不需要 \(A_m\) 与 \(C_p\) 交换。

对任意有限矩阵 \(X\)，
\(\|X\|_2\le\sum_{u,v}|X_{uv}|\)。
因此取 \(R\le\mathcal R_p\)，先放宽
\(1/(j+1)!\le1/j!\)，再将非负和延到所有 \(j,k\ge0\)，得到

\[
 \begin{aligned}
 &R\sum_{j,k<2^m}
   \frac{R^{j+k}}{(j+1)!\,k!}
       \|A_m^jC_pA_m^k\|\\
 &\quad\le
 \sum_{u,v=0}^{z-1}
 \left[
 \mathcal R_p\,g_p(B_{p+1})
       \exp\bigl(2\mathcal R_p g_p(B_{p+1})\bigr)
 \right]_{u,z+v}.
 \end{aligned}
 \tag{2.2}
\]

准确系数是
\(\sum_{j+k=n}1/(j!k!)=2^n/n!\)；
没有把双和替成一个未经证明的总幂范数。
矩阵幂零，所以右边仍是有限矩阵多项式。

## 3. 小正圆点及完整跨块权

置

\[
 \zeta_p=\frac{d_0}{4\mathcal R_p},\qquad
 t_p=\log\zeta_p^{-1}
       =\frac{417}{8}z^3+20+\log4
       \le\frac{209}{4}z^3.
 \tag{3.1}
\]

下面直接证明 \(g_p(\zeta_p)\le2\zeta_p/d_0\)。
首先 \(\zeta_p\le e^{-52z^3}\)。
对 \(1\le i<p\)，由
\(\Lambda_i\le100\,16^i\)、
\(2^i-1\ge2^{i-1}\) 和 \(8^i\le z^3/8\)，有

\[
 \log\frac{\zeta_p^{\,2^i-1}}{d_i}
 \le100\,16^i-52z^3(2^i-1)
 \le-\frac{27}{2}z^3\,2^i
 \le-27z^3.
 \tag{3.2}
\]

又 \(\zeta_p^{2^i}/d_i<1/2\)，所以其余分母的倒数至多二。
最低项为 \(1/(d_0-\zeta_p)\)；它与 \(d_0^{-1}\) 的差至多
\(2\zeta_p/d_0^2<1/4\)。
其余项总和至多 \(2p e^{-27z^3}<1/4\)。
因此

\[
 \frac{g_p(\zeta_p)}{\zeta_p}
 \le d_0^{-1}+\frac12\le2d_0^{-1},
\]
\[
 \boxed{
 \mathcal R_p g_p(\zeta_p)
       e^{2\mathcal R_p g_p(\zeta_p)}\le e/2.
 }
 \tag{3.3}
\]

标量函数
\(g_p(s)e^{2\mathcal R_p g_p(s)}\)
的 Taylor 系数非负。
故其第 \(L\) 个系数至多该函数在 \(\zeta_p\) 的值乘
\(\zeta_p^{-L}\)。

原加权后移给完整矩阵系数

\[
 [h(B_{p+1})]_{u,z+v}
 =\frac{W_{z+v}}{W_u}[s^{z+v-u}]h(s)
 =\frac{d_pW_v}{W_u}[s^{z+v-u}]h(s).
 \tag{3.4}
\]

这里 \(0\le u,v<z\)，指数 \(z+v-u\) 在 \(1,\ldots,2z-1\)；
没有删去最坏的最高次数。
(3.3)–(3.4) 将 (2.2) 中每一项控制为

\[
 \frac e2\,
     \frac{d_pW_v}{W_u}\zeta_p^{-(z+v-u)}.
 \tag{3.5}
\]

令 \(\omega_n=-\log W_n\)。
该项除常数外的对数为

\[
 -\Lambda_p+zt_p+
        (vt_p-\omega_v)-(ut_p-\omega_u).
 \tag{3.6}
\]

对每个 \(i<p\)，
\(2^it_p-\Lambda_i>0\)，因为
\(\Lambda_i/2^i\le(25/2)z^3<t_p\)。
又

\[
 nt_p-\omega_n
 =\sum_{i\in{\rm bits}(n)}(2^it_p-\Lambda_i).
\]

故在全部原 \(u,v\) 中，(3.6) 的最大值准确在
\(v=z-1,u=0\) 取得，等于

\[
 -\sum_{i=0}^{p}\Lambda_i+(2z-1)t_p.
 \tag{3.7}
\]

这一步保留了真实权分母及 \(2z-1\)，不是分别取两列范数的最大值。

原权显式求和为

\[
 \sum_{i=0}^{p}\Lambda_i
 =\frac{320}{3}z^4-120z^3
       +(300p-250)z+\frac{850}{3}.
 \tag{3.8}
\]

将全部 \(z^2\) 条目计入，用 (3.1)，(2.2) 的对数至多

\[
 2\log z+1-\frac{320}{3}z^4
                   +120z^3+\frac{209}{2}z^4
 =-\frac{13}{6}z^4+120z^3+2\log z+1
 \le-2z^4.
 \tag{3.9}
\]

最后一步对 \(z\ge1024\) 成立：
\(120/z+(2\log z+1)/z^4\le1/6\)。
这证明 (0.2)，包括 \(Y\) 的全部绝对系数、完整物理度量、矩阵条目数和最高跨块次数。

## 4. \(c=26\) 母窗口

设初值

\[
 m\ge10,\quad d=2^m,\quad
 1\le Q\le e^{26d^3},\quad
 k_0\in\ker L_m\cap\mathcal H_{\le Q}^{(m)}.
\]

第 \(n\) 步令

\[
 p=m+n,\quad z=2^p,\quad Q_n=Q+z-d.
\]

原物理相容右逆在新头的参数可取

\[
 R_0=512\sqrt{Q_n+2z+1}
          (p+1+Q_n+2z+2)^{3/2}
       \le512(Q+5z)^2.
\]

因为

\[
 \log R_0\le52d^3+7+2\log(1+5z)
         \le\frac{417}{8}z^3,
\]

有 \(R_0\le\mathcal R_p\)。
原右逆不必重新构造：其
\(R_0^t\mathcal U_{R_0}/t!\) 界随参数增大仍成立。

记当前真实残量 \(r=K_pk\)。
由 (0.1)，

\[
 D_{p+1}^\ell r=K_p(-A_p)^\ell k,\qquad
 A_{p+1}^{z}r=0.
\]

取原短修复

\[
 c=\sum_{j<z}(-A_{p+1})^jR_{j+1}'r.
\]

它满足 \(L_{p+1}c=r\)，孔数至多增加 \(z\)。
在右逆估计中将 \(A_p^j\) 先移到输入，再保同一个残量的全部导数，得到

\[
 \|c\|
 \le R_0\sum_{j,\ell<z}
 \frac{R_0^{j+\ell}}{(j+1)!\ell!}
 \|A_p^jK_pA_p^\ell\|\,\|k\|
 \le e^{-2z^4}\|k\|.
 \tag{4.1}
\]

这正是联合预算的实际使用位置。
它没有先估 \(\|K_pk\|\)，也没有另乘 \(\eta_{p-1}\)。

令 \(k'=k-c\) 并迭代，则

\[
 \|k_n\|\le2\|k_0\|,\qquad
 \|k_\infty-k_0\|\le4e^{-2d^4}\|k_0\|
                      \le e^{-d^4}\|k_0\|.
 \tag{4.2}
\]

原全部孔数的每步上界为 \(Q+3z\)，所以任意固定 \(c_0>0\) 下，

\[
 \sum_n\|e^{c_0\mathcal N}(k_{n+1}-k_n)\|
 \le2\|k_0\|\sum_n e^{c_0(Q+3z)-2z^4}<\infty.
\]

因此强极限在
\(M\cap\operatorname{Dom}e^{c_0\mathcal N}\)，
由原 \(M\cap X_3\subseteq N\) 得它属于 \(N\)。
全部步骤线性，证明 (0.4)。

## 5. 真实完整误差的联合交换子和

现在固定原头 \(m\)，令 \(A=A_m,D=D_m,d=2^m\)，并取

\[
 R=\mathcal R_m=e^{(417/8)d^3},
 \qquad \mathcal E=L_m-T=-\sum_{p\ge m}K_p.
\]

定义完整联合预算

\[
 \mathcal J_m(R)
 =R\sum_{\substack{j,k<d\\a\ge0}}
 \frac{R^{j+k+a}}{(j+1)!\,k!\,a!}
       \|A^j(\operatorname{ad}_D^a\mathcal E)A^k\|.
 \tag{5.1}
\]

下面逐个 \(p\) 支付，不把 \(\mathcal E\) 当成只在首个新位的误差。
\(A_m\) 与全部 \(E_i\)、\(i\ge m\) 交换。
对任意矩阵 \(X\)，\(E_i^2=0\) 给

\[
 \|\operatorname{ad}_{E_i}X\|\le2\|X\|,\quad
 \operatorname{ad}_{E_i}^2X=-2E_iXE_i,\quad
 \operatorname{ad}_{E_i}^3X=0.
\]

各位交换子互相交换。因此
\(A^j(\operatorname{ad}_D^aK_p)A^k\)
的全部加权导数和，至多是
\(\|A^jK_pA^k\|\) 乘

\[
 a_{m,p}(R)
 =\prod_{i=m}^{p}(1+Rb_i)^2.
 \tag{5.2}
\]

实际最后一位还可省略，但这里保留这个宽松乘积。

写 \(p=m+r,z=2^p=2^rd\)。
因 \(\log(1+R)\le(209/4)d^3\)，

\[
 \log a_{m,p}(R)
 \le\frac{209}{2}(r+1)d^3
 \le\frac18 z^4.
 \tag{5.3}
\]

最后一步等价于
\(836(r+1)\le16^r d\)，对 \(d\ge1024,r\ge0\) 成立。
又 \(R=\mathcal R_m\le\mathcal R_p\)，故可对每个 \(p\) 使用 (0.2)，得到

\[
 \boxed{
 \mathcal J_m(R)
 \le\sum_{p\ge m}e^{-(15/8)16^p}
 \le2e^{-(15/8)d^4}.
 }
 \tag{5.4}
\]

这也证明 (5.1) 中全部和绝对收敛；前面交换求和与实际
\(\mathcal E=-\sum K_p\) 一致。

## 6. 用联合预算修复实际低输出

取 \(w\in M=\ker T\)。
先保一个粗吸收预算。
原导数 carry 和以及
\(\log(2+R)\le(209/4)d^3\)
给

\[
 \epsilon_m(R)
 :=\sum_{a\ge0}\frac{R^a}{a!}
        \|\operatorname{ad}_D^a\mathcal E\|
 \le104e^{-80d^4+(209/2)d^3}
 \le e^{-79d^4}.
 \tag{6.1}
\]

原实际幂估计
\(\|A^j\|\le6^je^{-(770/256)(j-m)_+^4}\)
在有限 \(j<d\) 上给

\[
 H_m(R):=\sum_{j<d}\frac{R^j}{j!}\|A^j\|
 \le e^{50d^4}.
 \tag{6.2}
\]

例如 \(\log(6R)\le(209/4)d^3\)，有限截止的指数最大值至多
\((209/4-14/5)d^4\)，再加 \(\log d\) 仍小于 \(50d^4\)。
于是

\[
 RH_m(R)\epsilon_m(R)\le e^{-28d^4}<1/4.
\]

由实际方程 \(Dw=-Aw+\mathcal Ew\)，

\[
 \mathcal U_R(w)\le2H_m(R)\|w\|,
 \qquad
 \mathcal U_R(\mathcal Ew)
       \le\epsilon_m(R)\mathcal U_R(w).
 \tag{6.3}
\]

现在取 \(4d\le Q\le e^{26d^3}\)。
该低输出问题的原右逆参数
\(R_0\le2048Q^2\) 也小于当前 \(R\)。
设

\[
 r_0=P_{\le Q-1}\mathcal Ew,\qquad
 z=\sum_{j<d}(-A)^jR_{j+1}r_0.
\]

原右逆给 \(L_mz=r_0\)。
把头幂先移到右逆输入，并利用孔截断的收缩性，

\[
 \|z\|
 \le R\sum_{\substack{j<d\\a,b\ge0}}
 \frac{R^{j+a+b}}{(j+1)!\,a!\,b!}
       \|A^j(\operatorname{ad}_D^a\mathcal E)D^bw\|.
 \tag{6.4}
\]

这里是完整 Leibniz 展开
\(D^k\mathcal E=\sum_{a+b=k}\binom{k}{a}
(\operatorname{ad}_D^a\mathcal E)D^b\)，
全部实际交换子均保留。

再使用准确有限头展开

\[
 D^bw=(-A)^bw+
       \sum_{c=0}^{b-1}(-A)^cD^{b-1-c}\mathcal Ew.
\]

第一项在 (6.4) 中至多
\(\mathcal J_m(R)\|w\|\)。
第二项置 \(b=c+\ell+1\)，并使用
\(b!\ge c!\ell!\)，得到上界

\[
 R\,\mathcal J_m(R)\,\mathcal U_R(\mathcal Ew).
\]

于是由 (6.3)，

\[
 \|z\|
 \le\mathcal J_m(R)
       (1+2RH_m(R)\epsilon_m(R))\|w\|
 \le2\mathcal J_m(R)\|w\|
 \le4e^{-(15/8)d^4}\|w\|
 \le e^{-d^4}\|w\|.
 \tag{6.5}
\]

这一步没有重新付两个 \(H_m\)；只有粗的小吸收因子，
真正跨 carry 的主项由 (5.4) 的联合预算支付。

\(P_{\le Q}w-P_{\le Q}z\) 满足原全部低输出方程。
因此实际正交投影 \(v_Q=P_{V_Q}w\) 满足

\[
 \boxed{\|v_Q-P_{\le Q}^{(m)}w\|\le e^{-d^4}\|w\|.}
 \tag{6.6}
\]

所有右逆仍只作用于原有限孔输入。
(6.4)–(6.5) 的全空间导数只是估计该同一个有限输入，没有把右逆延拓为物理全域满射。

## 7. 实际顶部、全窗口和原固定测试

假设 \(w\in W=M\ominus N\)。
令 \(k_Q=P_{K_Q}w=P_{K_Q}v_Q\)，其中
\(K_Q=\ker L_m\cap\mathcal H_{\le Q}^{(m)}\)。
(0.4) 给

\[
 \|k_Q\|^2
 =\langle w,k_Q-\Lambda^{(26)}_{m,Q}k_Q\rangle,
 \qquad\|k_Q\|\le e^{-d^4}\|w\|.
\]

故 \(u_Q=v_Q-k_Q\) 是同一源的真正左最小者，且

\[
 \boxed{
 \|u_Q\|\le\|w\|,\qquad
 \|u_Q-P_{\le Q}^{(m)}w\|\le2e^{-d^4}\|w\|.
 }
 \tag{7.1}
\]

取

\[
 Q_m=\lfloor e^{26d^3}\rfloor,\quad
 I_m^{(26)}=\{4d,\ldots,Q_m-d\},\quad
 \varepsilon_m^{(26)}=2e^{-d^4},
 \quad u_m=u_{Q_m}.
\]

从这个同一个顶部定义
\(r_{m,p}=A_m(u_m)_p\)。
固定层截断与原完整未来带两投影给

\[
 E_{m,p}^{\dagger}r_{m,p}=P_{\le p}^{(m)}u_m,\qquad
 \Xi_{m,p}(r_{m,p})^2
 \le2\|P_{[p+1,p+d]}^{(m)}u_m\|^2.
 \tag{7.2}
\]

源在准确负流图
\(\ker[\iota_0^*(L_{m,p}+B_{m,p})]\)；
两费中仍保完整右核和原裸低旗。

置
\(\tau_m=\|\mathbf1_{\{\mathcal N_{\rm tot}>4d\}}w\|\)，
则

\[
 \boxed{
 \sum_{p\in I_m^{(26)}}\Xi_{m,p}(r_{m,p})^2
 \le2d(\tau_m+\varepsilon_m^{(26)}\|w\|)^2,
 }
 \tag{7.3}
\]
\[
 \boxed{
 \sup_{p\in I_m^{(26)}}
 \|E_{m,p}^{\dagger}r_{m,p}-w\|
 \le\tau_m+\varepsilon_m^{(26)}\|w\|\to0.
 }
 \tag{7.4}
\]

间距 \(d\) 的不交网格去掉 (7.3) 中的 \(d\)。
原固定低测试
\(t_{m,p}=E_{m,p}P_{V_{m,p}}f\)
仍满足

\[
 \langle L_{m,p}r_{m,p},t_{m,p}\rangle
       \to\langle w,f\rangle
\]

对全窗口一致。源没有在窗口间改变，顶部误差只支付一次真实带覆盖数。

## 8. 后续比较和范围

这一个实际未消量化联合旗的源族，现有充分比较目标为

\[
 \sup_{p\in I_m^{(26)}}
 \frac{\mu_{m,p}(r_{m,p})^2}
      {\Xi_{m,p}(r_{m,p})^2}
 =O(e^{26d^3}/d).
\]

若沿头子序列另证此式，则与 (7.3)–(7.4) 矛盾并排除非零缺陷。
本稿没有证明该比较。

旧深 jets/单高块联合旗的指数小 \(\delta_m\) 仍保原量词。
本稿扩大的是原未消旗、但已经在准确负流图中的实际来源窗口。
完整高输入 Schur、固定测试的源逆与角度衰减仍须保留，不能用全 Gram 的粗交换子替代。

依赖均为仓库内已有完整原证明：
[真实单新位块](2026-11-14-true-single-bit-carry-block-and-twenty-window-actual-sources-789f-next.md)、
[原实际顶部与两投影](2026-11-14-extended-sixteen-window-actual-defect-top-and-common-two-fee-sources-789f-next.md)、
[原线性导数和相容物理右逆](2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md)、
[R239 指数权核饱和](../results/R239-appendix-exponential-hole-right-inverses-and-true-tail-regularization.md)。
