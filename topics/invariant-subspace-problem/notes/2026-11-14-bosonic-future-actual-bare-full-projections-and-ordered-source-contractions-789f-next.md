# 同一 bosonic 未来的真实 bare／完整右双投影与有序源收缩

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core / root；AI-assisted，GPT-6 Astra Pro。

**状态：下列投影、源读出及能量身份已证明。** 本稿把
[实际固定测试的 bosonic 未来预算](2026-11-14-actual-low-test-full-image-inverse-bosonic-future-budget-789f-next.md)
接到真正 bare 核和完整右核。正交投影自动给合法链，不需要先逐层投回硬核再调用未付的修复逆。
它们的源准确变为 \(B^{-1}M_{\rm B}t\) 和 \(GM_{\rm B}t\)；
本稿没有将这两个源认成原来的 \(t\)，也没有支付源差的原左费用。

依赖：
[原首头及全部右链](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)；
[同源完整右／bare 高返回 Schur](2026-11-14-one-bit-complete-right-bare-source-and-actual-return-schur-789f-next.md)；
[真核零模头预算](2026-11-14-full-boolean-kernel-bosonic-zero-occupation-and-head-only-budget-789f-next.md)。

## 1. 保完整原源的 bosonic 真最小右链

固定原 \(m,d=2^m,A=A_m,D=D_m\)、切口 \(q\) 和
\[
S=\sum_i b_i^2,\qquad \mathcal B=\sqrt S\,a_0,\qquad
N_0=a_0^*a_0.
\]
平方自由空间按原物理范数等距嵌入完整 bosonic 空间。
原实际源仍为
\[
\mathscr R_q
=\bigoplus_{i=0}^{d-2}
e_i\bigl(\ker D^{d-i-1}\cap\mathcal H_q\bigr).
\]
本稿每次运算只涉及固定的 \(q,\ldots,q+d\) 层；
不在全部 Fock 空间上把 \(\mathcal B\) 当成有界算子。

令 \((N_0+1)_{\overline j}=(N_0+1)\cdots(N_0+j)\)，定义完整 bosonic 幂的最小右逆
\[
\mathcal I_{j,q}
=\frac{(a_0^*)^j}{S^{j/2}}
 (N_0+1)_{\overline j}^{-1}.
\tag{1.1}
\]
分母作用于输入层，置于 creation 的右侧。
在集体占据 \(k\) 上，它的范数系数为
\[
[S^j(k+1)\cdots(k+j)]^{-1/2}.
\]
所以
\(\mathcal B^j\mathcal I_{j,q}=I\)，且
\[
\mathcal I_{j,q}^*\mathcal I_{j,q}
=S^{-j}(N_0+1)_{\overline j}^{-1}.
\tag{1.2}
\]

对 \(t\in\mathscr R_q\)，置
\[
\boxed{
c_{{\rm B},j}(t)=(-A)^{j-1}\mathcal I_{j,q}t,\qquad
1\le j\le d.
}
\tag{1.3}
\]
头尾算子交换，故
\[
\mathcal Bc_{{\rm B},1}=t,\qquad
Ac_{{\rm B},j}+\mathcal Bc_{{\rm B},j+1}=0,\qquad
Ac_{{\rm B},d}=0.
\tag{1.4}
\]
在原源上 \(A^{d-1}t=0\)，所以最后一段本身为零。

这条链严格保持原 bosonic 头／短核旗。
源第 \(i\) 头满足 \(N_0\le d-i-2\)；
第 \(j\) 次提升后集体占据至多 \(d-i+j-2\)，
而 \(A^{j-1}\) 只能输出到头 \(\ell\le i-j+1\)。
因此输出头 \(\ell\le d-j\)，且
\(N_0\le d-\ell-1\)，恰为所需完整短核条件。
它仍未必平方自由。

### 1.1 最小性的准确理由

(1.3) 的全部横向次数不超过 \(q\)。
任意首源为零的完整 bosonic 右链，只含横向次数至少 \(q+1\)：
其第一段由 \(\mathcal Bc_1=0\) 得到这一点；
对任意固定横向次数 \(b\le q\)，以后各段的集体占据均正，
\(\mathcal B\) 在该分量上单射，逐段递推遂迫这些分量全部为零。

因此 (1.3) 正交于完整 bosonic 零源核，是同一个实际源 \(t\)
在完整 bosonic 右链空间中的真最小者。
这里先在完整空间取最小逆，再限制源到 \(\mathscr R_q\)。

记 \(\iota_q:\mathscr R_q\hookrightarrow
\mathbb C^d\otimes\mathscr F_q\) 为实际包含，
定义它的原源 Gram
\[
\boxed{
M_{{\rm B},q}
=\iota_q^*
 \left[
 \sum_{j=1}^{d}
 \frac{(A^{j-1})^*A^{j-1}}
 {S^j(N_0+1)_{\overline j}}
 \right]\iota_q .
}
\tag{1.5}
\]
头因子与 \(N_0\) 交换，但 \(N_0\) 不必保持平方自由原源；
(1.5) 的压缩次序不可省。
准确有
\[
\|c_{\rm B}(t)\|^2=\langle M_{{\rm B},q}t,t\rangle.
\tag{1.6}
\]

由原源的 \(N_0\le d-2\) 和已证头 Gram
\(H_A=\sum_{\ell<d}(A^\ell)^*A^\ell/(S^\ell\ell!)\preceq C_mI\)，
\[
\boxed{
\frac1{S(d-1)}I\preceq M_{{\rm B},q}
\preceq\frac{C_m}{S}I .
}
\tag{1.7}
\]
上界只用 \((k+1)_{\overline j}\ge j!\)。
故 \(M_{{\rm B},q}\) 在同一原源上有界、正可逆，
且该比较不依赖孔切口 \(q\)。

## 2. 两个真正物理核及其源

将各段最小代表等距放入同一个 bosonic 未来直和。
记 \(\mathcal C_{\rm b}\) 为原 bare 可行核，
\(\mathcal C_{\rm f}\) 为原完整物理右核，
\(P_{\rm b},P_{\rm f}\) 为它们在该共同环境中的正交投影。
两个空间都保全部原头旗、尾短核旗、内部方程和末端封口。

源映射为
\[
F_{\rm b}:\mathcal C_{\rm b}\to\mathscr R_q,\qquad
F_{\rm f}:\mathcal C_{\rm f}\to\mathscr R_q,
\]
均读取第一段 \(Dc_1\)。沿用原记号
\[
B^{-1}=F_{\rm b}F_{\rm b}^*,\qquad
G=F_{\rm f}F_{\rm f}^*.
\tag{2.1}
\]
所有伴随均取这两个真实核的诱导物理内积。

原完整右到 bare 的商映射满射。
具体说，对每个 \(a\in\mathcal C_{\rm b}\) 有同源的
\(c\in\mathcal C_{\rm f}\)，满足
\[
c-a\in\mathcal H_{\rm hi}.
\tag{2.2}
\]
同一高返回空间在 bosonic 中准确满足
\[
\mathcal H_{\rm hi}
\subseteq
\mathcal H_{\rm hc}\cap\{N_\perp\ge q+2\};
\tag{2.3}
\]
原头旗仍保留在左侧，不将它替换成全部横向 Fock 空间。
这些事实由引用的完整首头参数化及真实高返回商证明。

## 3. 不修复逐行残量的准确双投影

以下暂写 \(M=M_{{\rm B},q}\)。

取任意 \(t\in\mathscr R_q\) 和
\(a\in\mathcal C_{\rm b}\)，令 \(r=F_{\rm b}a\)。
选择 (2.2) 的同源完整提升 \(c\)。
由横向次数正交及 bosonic 最小性，
\[
\begin{aligned}
\langle c_{\rm B}(t),a\rangle
&=\langle c_{\rm B}(t),c\rangle\\
&=\langle c_{\rm B}(t),c_{\rm B}(r)\rangle\\
&=\langle Mt,r\rangle.
\end{aligned}
\tag{3.1}
\]
第一步用 (2.3)，第二步只删除同源 bosonic 零源链。
因而
\[
\boxed{
P_{\rm b}c_{\rm B}(t)=F_{\rm b}^*Mt,\qquad
P_{\rm f}c_{\rm B}(t)=F_{\rm f}^*Mt.
}
\tag{3.2}
\]
第二式直接由完整物理链作为 bosonic 可行链得到。

这两个投影本身已是合法链。
不需要把 \(Q_{\rm hc}c_{\rm B}(t)\) 当成可行链，
也不调用一个费用未知的内部行逆。

它们的真实源分别是
\[
\boxed{
t_{\rm b}=B^{-1}Mt,\qquad t_{\rm f}=GMt.
}
\tag{3.3}
\]
因此“投影费用不增加”并不等于“同一个源 \(t\) 已被修复”。

由投影收缩，
\[
M B^{-1}M\preceq M,\qquad MGM\preceq M.
\]
结合原 bare／完整最小费用关系，准确得到
\[
\boxed{
M\preceq B\preceq G^{-1},
\qquad
0\prec G\preceq B^{-1}\preceq M^{-1}.
}
\tag{3.4}
\]

## 4. 同一个度量下的源收缩、及高返回差的正能量

定义
\[
\beta=B^{-1}M,\qquad \gamma=GM.
\tag{4.1}
\]
它们通常不在原物理内积中自伴。
在同一个 \(M\) 内积中却是有序的正收缩，因为
\[
\boxed{
0\prec M^{1/2}GM^{1/2}
\preceq M^{1/2}B^{-1}M^{1/2}\preceq I.
}
\tag{4.2}
\]
这保留全部非交换因子次序。

再记
\[
a_t=F_{\rm b}^*Mt,\qquad c_t=F_{\rm f}^*Mt.
\]
对任何 \(c\in\mathcal C_{\rm f}\)，其 bare 最小代表
\(Q_{\rm lo}c\) 属于 \(\mathcal C_{\rm b}\)，且源不变。
故
\[
\langle F_{\rm b}^*Mt,c\rangle
=\langle Mt,F_{\rm f}c\rangle,
\]
从而
\[
\boxed{P_{\rm f}a_t=c_t.}
\tag{4.3}
\]
于是有严格 Pythagoras：
\[
\boxed{
\|a_t-c_t\|^2
=\langle Mt,(B^{-1}-G)Mt\rangle,
\qquad
F(a_t-c_t)=(\beta-\gamma)t.
}
\tag{4.4}
\]
这里 \(F\) 只表示读取共同物理第一段的 \(D\)；
没有把 \(a_t-c_t\) 称为完整右可行链。

若沿同源 first-head 坐标记
\(C_{\rm b}\) 为 bare 边界源映射、
\(H_{\rm b}\) 为 bare 首源 Gram、
\(E_{\rm ret}\succeq0\) 为完整稿的真实高返回 Schur，
则
\[
\boxed{
B^{-1}-G
=C_{\rm b}
\left[
H_{\rm b}^{-1}-(H_{\rm b}+E_{\rm ret})^{-1}
\right]C_{\rm b}^*.
}
\tag{4.5}
\]
因此 (4.4) 的正差恰读取原完整返回块，
不是删去该块后制造的假相等。

## 5. 原正耗散直接支付更锐的同窗预算

同一个固定物理测试 \(f\in\mathcal H_{\le s}\) 产生
\[
q_p=P_{V_p}f,\qquad t_p=E_pq_p.
\]
[原真实伴随流](../results/R271-appendix-fixed-test-adjoint-source-flow-and-joint-good-top-budget.md)
§§2--5 已证明，对 \(p\ge s+1\)，
\[
t_p=-A v_p,\qquad v_p=-(q_p)_p,\qquad
\sum_{p\ge s+1}\|v_p\|^2\le\|f\|^2.
\tag{5.1}
\]
所有 \(v_p\) 来自同一个物理测试的实际受限正逆，未另择源。

### 5.1 逐切口的原头正预算

由 (1.1)--(1.6)，头尾交换及
\((N_0+1)_{\overline j}\succeq j!I\)，准确有
\[
\begin{aligned}
\langle M_{{\rm B},p}t_p,t_p\rangle
&=\sum_{j=1}^{d}\|\mathcal I_{j,p}A^jv_p\|^2\\
&\le\sum_{j=1}^{d}\frac{\|A^jv_p\|^2}{S^j j!}\\
&=\langle(H_A-I)v_p,v_p\rangle\\
&\le(C_m-1)\|v_p\|^2.
\end{aligned}
\tag{5.2}
\]
最后一项的 \(j=d\) 因 \(A^d=0\) 严格为零。
这保持了原实际源和全部短旗；没有将源换成任意低出生方向。

将 (5.2) 对全部 \(p\ge s+1\) 求和，得
\[
\boxed{
\sum_{p\ge s+1}\|c_{\rm B}(t_p)\|^2
=\sum_{p\ge s+1}\langle M_{{\rm B},p}t_p,t_p\rangle
\le(C_m-1)\|f\|^2.
}
\tag{5.3}
\]
这锐化了完整像逆稿的 \(C_m^2k_0(2+\log d)^2\) 上界。
那个证明仍正确，且保留了准确零模像与实际投影的识别；
此处用后来得到的真 bosonic 最小逆，直接接原正耗散。

若要连初始 \(p=s\) 一并相加，
\(t_s=A(q_s)_s\) 给该单项至多 \((C_m-1)\|f\|^2\)，
因而总界可取 \(2(C_m-1)\|f\|^2\)。
原合法 good-top 窗全部在 \(p>s\)，无需这个额外因子。

(3.2)--(4.4) 给三条同源物理预算：
\[
\boxed{
\sum_{p\ge s+1}\|a_{t_p}\|^2,\quad
\sum_{p\ge s+1}\|c_{t_p}\|^2,\quad
\sum_{p\ge s+1}\|a_{t_p}-c_{t_p}\|^2
\ \le\ (C_m-1)\|f\|^2.
}
\tag{5.4}
\]
每条都是实际可行投影或准确正差，不能将其源再认成 \(t_p\)。

### 5.2 已选的同一个 good-top 不用重挑

在原固定 \(n\) 维物理测试空间 \(\mathscr T_n\) 上，
令 \(\mathcal T_p f=t_p\)，\(\mathcal V_p f=v_p\)，
\(\Psi_p\) 为上述原真实伴随流 §5 的正耗散矩阵。
原式给 \(\mathcal V_p^*\mathcal V_p\preceq\Psi_p\)，
所以 (5.2) 对所有输入同时成立，即
\[
\boxed{
\mathcal T_p^*M_{{\rm B},p}\mathcal T_p
\preceq(C_m-1)\mathcal V_p^*\mathcal V_p
\preceq(C_m-1)\Psi_p.
}
\tag{5.5}
\]
由 (3.2)--(4.4)，三个物理投影／差映射的Gram也各被 (5.5) 控制。

原同一切口选择已付
\[
D_b^{(n)}=\sum_{p=b}^{b+d}\Psi_p
\preceq\frac{4n}{K_{\rm win}}I.
\]
因此在这个已经选好的 \(b\)，
\[
\boxed{
\|f\mapsto a_{t_b(f)}\|^2,\quad
\|f\mapsto c_{t_b(f)}\|^2,\quad
\|f\mapsto a_{t_b(f)}-c_{t_b(f)}\|^2
\le\frac{4n(C_m-1)}{K_{\rm win}}.
}
\tag{5.6}
\]
原实际源的两费同时仍为
\(\Xi_b(r_b)^2\le4\varepsilon_m^2/K_{\rm win}\)。
所以本文没有通过改选另一切口来拼接这些小量，
也没有引入额外平均损失。
常数沿 \(m=O(\log\log q)\) 仍为 \(q^{o(1)}\)。

## 6. 必须保留的源差与未付左配对

原目标功能是
\[
\langle Lr,t_p\rangle=\langle E_p^\dagger r,f\rangle.
\]
(5.4)--(5.6) 控制的两个实际源是
\[
\beta_pt_p=B_p^{-1}M_{{\rm B},p}t_p,\qquad
\gamma_pt_p=G_pM_{{\rm B},p}t_p.
\]
没有证明
\[
\mu_p((I-\beta_p)t_p)
\quad\text{或}\quad
\mu_p((I-\gamma_p)t_p)
\]
具有同阶上界。
\(M\)-正收缩不能被当成 \(L\)-收缩；
也不能把这些源差未经识别就命名为原流的 \(e_{p+1}\)。

例如，用已付完整投影测试链可以准确写
\[
\begin{aligned}
\langle Lr,t_p\rangle
&=\langle F_{\rm f}^*Lr,c_{t_p}\rangle
 +\langle Lr,(I-\gamma_p)t_p\rangle,
\end{aligned}
\tag{6.1}
\]
第一项由原 flat 费与 (5.6) 支付。在上述同一未改源的原good-top上，其绝对值至多 \(4\varepsilon_m\sqrt{n(C_m-1)}\|f\|/K_{\rm win}\)。
第二项仍是同一个原源的真实左配对，不能删除。

本稿完成的是：将已付 bosonic 未来预算转成真正可行的两种物理右测试、
给出它们的准确源及共同正收缩结构。
它把剩余问题集中到 (6.1) 的源差，而未证明该差消失、原
\(E_{\rm ret}\) 有所需统一界、\(N=M\) 或普通 ISP。
