# 扩展母窗内的实际缺陷顶部、同一最小左源与整窗两费用

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

状态：以下实际低输出、顶部和全窗口来源定理已证明。扩大范围保留一个原向量及其同一个顶部最小者；尚未在扩大后的全范围支付旧联合旗的参数 \(\delta_m\)，也没有证明 \(N=M\)。

## 0. 主结论

沿原两个边界模型，令

\[
 M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
\]

假设 \(0\ne w\in W\)。固定 \(m\ge10,d=2^m\)，置

\[
 Q_m=\lfloor e^{16d^3}\rfloor,\qquad
 I_m=\{4d,\ldots,Q_m-d\},\qquad
 \varepsilon_m=e^{-8d^4}+e^{-7d^4}.
 \tag{0.1}
\]

存在一个真正顶部最小左向量 \(u_m\)，使

\[
 \|u_m\|\le\|w\|,\qquad
 \boxed{\|u_m-P_{\le Q_m}^{(m)}w\|
             \le\varepsilon_m\|w\|.}
 \tag{0.2}
\]

对全部 \(p\in I_m\)，从这个同一个 \(u_m\) 定义

\[
 r_{m,p}=A_m(u_m)_p.
\]

则它们是原完整最小左源，而且准确有

\[
 \boxed{E_{m,p}^{\dagger}r_{m,p}
                     =P_{\le p}^{(m)}u_m.}
 \tag{0.3}
\]

记原裸费为 \(\alpha_{m,p}\)，原平坦费为
\(\lambda_{{\rm flat},m,p}\)，两费平方和为

\[
 \Xi_{m,p}(r)^2
  =\alpha_{m,p}(r)^2+\lambda_{{\rm flat},m,p}(r)^2.
\]

对每一个完整未来带，

\[
 \boxed{
 \Xi_{m,p}(r_{m,p})^2
       \le2\|P_{[p+1,p+d]}^{(m)}u_m\|^2.
 }
 \tag{0.4}
\]

因此，置原总孔尾

\[
 \tau_m=\|\mathbf1_{\{\mathcal N_{\rm tot}>4d\}}w\|,
\]

便有

\[
 \boxed{
 \sum_{p\in I_m}\Xi_{m,p}(r_{m,p})^2
 \le2d(\tau_m+\varepsilon_m\|w\|)^2,
 }
 \tag{0.5}
\]
\[
 \boxed{
 \sup_{p\in I_m}
 \|E_{m,p}^{\dagger}r_{m,p}-w\|
 \le\tau_m+\varepsilon_m\|w\|\longrightarrow0.
 }
 \tag{0.6}
\]

间距 \(d\) 的不交未来窗，(0.5) 右边不带因子 \(d\)。
这些都是同一实际 \(w\)、同一 \(u_m\) 的预算，未在各个切口改选向量。

依赖：
[扩展母窗](2026-11-14-extended-linear-mother-window-sixteen-and-true-stable-lift-789f-next.md)、
[原线性导数与相容右逆](2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md)、
[原最小者截断与两投影](../results/R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)。
下文重做扩大参数所需的全部指数余量；固定层的两个投影身份则保留原证明的完整源和旗。

## 1. 固定物理空间与所有有限层的域

本节固定同一个 \(m\)，省略其下标。令

\[
 A=A_m,\quad D=D_m,\quad \mathcal L=A+D,\quad
 V_p=\mathcal H_{\le p}^{(m)}
          \cap\ker(P_{\le p-1}^{(m)}\mathcal L),
 \qquad E_pv=Av_p,
\]
\[
 K_p=\ker\mathcal L\cap\mathcal H_{\le p}^{(m)}.
 \tag{1.1}
\]

\(E_p\) 的实际源空间是原

\[
 \mathscr R_p=\bigoplus_{i=0}^{d-2}
                 e_i(\ker D^{d-i-1}\cap\mathcal H_p).
\]

固定有限 \(p\) 时，完整层 MP 逆、实际受限旗及 \(E_p\) 的闭满射像均沿用原定义；其存在证明不需要 \(p\le e^{d^3/4}\)。具体的全层 MP 域见
[R279 §2.3](../results/R279-bosonic-affine-primitive-gram-transfer-and-low-occupation-bounds.md)，
原源的三角头回代与这些逆给同一有限层的满射。
没有把所有孔层的 MP 逆说成一个全局有界算子。

故可在所有本稿有限参数下写

\[
 U_p=E_p^\dagger,\quad L_p=U_p^*U_p,\quad
 \mu_p(r)^2=\langle L_pr,r\rangle,
 \qquad \ker E_p=K_p.
 \tag{1.2}
\]

零源核 \(K_p\) 随 \(p\) 嵌套。以下的 \(P_{\le p}^{(m)}\) 都是同一原尾孔投影，不改变物理位号或头内积。

## 2. 扩大参数后的真实导数 carry

先取任意整数

\[
 4d\le Q\le e^{16d^3}.
 \tag{2.1}
\]

原相容右逆可用

\[
 R=512\sqrt{Q+d+1}(m+Q+d+2)^{3/2}
       \le2048Q^2.
 \tag{2.2}
\]

记

\[
 \mathcal U_R(f)=\sum_{j\ge0}\frac{R^j}{j!}\|D^jf\|,
 \quad H_m(R)=\sum_{j<d}\frac{R^j}{j!}\|A^j\|,
 \quad \Theta=\log(6R),\quad x=\log(2+R).
\]

由 (2.1)–(2.2)，

\[
 x\le\Theta\le 32d^3+10\le\frac{65}{2}d^3.
 \tag{2.3}
\]

令 \(\mathcal E_m=L_m-T\)，并取原导数范数

\[
 \epsilon_m(R)
 =\sum_{j\ge0}\frac{R^j}{j!}
                   \|\operatorname{ad}_{D}^{j}\mathcal E_m\|.
\]

原第 \(\ell\) 个实际 carry 只与位 \(m,\ldots,\ell\) 的删除不交换；
\(\operatorname{ad}_{E_i}^{3}=0\) 和原算子范数给

\[
 \epsilon_m(R)
 \le52\sum_{r\ge0}
     \exp[-80d^4\,16^r+2(r+1)x].
\]

相邻项比小于 \(1/2\)。因为 \(d\ge1024\)，

\[
 \log104+2x\le\log104+65d^3\le d^4.
\]

所以，扩大窗口后仍有

\[
 \boxed{\epsilon_m(R)\le e^{-79d^4}.}
 \tag{2.4}
\]

这里没有沿用旧的附加假设 \(x\le d^3\)，而是把新的真实 \(x\) 直接放回全部 carry 的和。

原幂估计为

\[
 \|A^j\|\le6^j
      e^{-\gamma(j-m)_+^4},\qquad\gamma=770/256.
\]

置 \(C_\gamma=3/(4^{4/3}\gamma^{1/3})<1/3\)。
Legendre 最大值给

\[
 \log H_m(R)\le\log d+m\Theta+C_\gamma\Theta^{4/3}.
 \tag{2.5}
\]

\((65/2)^{4/3}<104\)，且对 \(m\ge10\) 有
\(m/2^m\le10/1024\) 和 \(\log d/d^4\le1/100\)，故

\[
 \frac{\log H_m(R)}{d^4}
 \le\frac1{100}+\frac{325}{1024}+\frac{104}{3}<35.
\]

即

\[
 \boxed{H_m(R)\le e^{35d^4}.}
 \tag{2.6}
\]

因此两项真正需要的吸收余量都是严格的：

\[
 RH_m(R)\epsilon_m(R)<\frac12,\qquad
 \boxed{2RH_m(R)^2\epsilon_m(R)\le e^{-8d^4}.}
 \tag{2.7}
\]

第二条的对数至多
\(\log2+(65/2)d^3+70d^4-79d^4\le-8d^4\)。

## 3. 实际 \(w\) 的低输出投影

对任何 \(w\in M\)，准确有

\[
 Dw=-Aw+\mathcal E_mw,
\]
\[
 D^kw=(-A)^kw+
       \sum_{j=0}^{k-1}(-A)^jD^{k-1-j}\mathcal E_mw.
\]

\(D\) 有界，故 \(\mathcal U_R(w)<\infty\)；原 Leibniz 范数不等式与 (2.7) 可以实际吸收，得到

\[
 \mathcal U_R(w)
 \le H_m(R)\|w\|
       +RH_m(R)\epsilon_m(R)\mathcal U_R(w)
 \le2H_m(R)\|w\|.
 \tag{3.1}
\]

令

\[
 r_0=P_{\le Q-1}L_mP_{\le Q}w
       =P_{\le Q-1}\mathcal E_mw.
\]

以原完整有限层相容逆 \(R_t\) 构造

\[
 \mathcal R=\sum_{j<d}(-A)^jR_{j+1},
 \qquad L_m\mathcal R=I
\]

于所需有限孔输入。原 factorial 估计给

\[
 \|\mathcal Rf\|\le RH_m(R)\mathcal U_R(f).
\]

设 \(z=\mathcal Rr_0\)。孔截断在 \(\mathcal U_R\) 中为收缩，故

\[
 \|z\|
 \le RH_m(R)\epsilon_m(R)\mathcal U_R(w)
 \le e^{-8d^4}\|w\|.
\]

由于 \(L_m\) 仅保持或下降一孔，

\[
 P_{\le Q}w-P_{\le Q}z\in V_Q.
\]

因此真正正交投影 \(v_Q=P_{V_Q}w\) 满足

\[
 \boxed{
 \|v_Q-P_{\le Q}w\|\le e^{-8d^4}\|w\|,
 \qquad \|v_Q\|\le\|w\|.
 }
 \tag{3.2}
\]

全部逆都在原物理有限孔输入上使用；这一步没有 bosonic 输出。

## 4. 用单位范数核投影消去左零源

现在假设 \(w\in W=M\ominus N\)。
令

\[
 k_Q=P_{K_Q}w=P_{K_Q}v_Q.
\]

扩展母窗给
\(\Lambda_{m,Q}k_Q\in N\) 及

\[
 \|\Lambda_{m,Q}k_Q-k_Q\|
        \le e^{-7d^4}\|k_Q\|.
\]

因为 \(w\perp N\)，且 \(k_Q\) 是原正交投影，

\[
 \|k_Q\|^2
 =\langle w,k_Q\rangle
 =\langle w,k_Q-\Lambda_{m,Q}k_Q\rangle.
\]

所以

\[
 \boxed{\|k_Q\|\le e^{-7d^4}\|w\|.}
 \tag{4.1}
\]

这里应用母提升的对象正是范数至多 \(\|w\|\) 的真实核投影；没有先取一个巨大非最小高返回修复再乘提升误差。

置

\[
 r_Q=E_Qv_Q,\qquad
 u_Q=v_Q-k_Q=E_Q^\dagger r_Q.
 \tag{4.2}
\]

它是 \(w\) 到 \(V_Q\ominus K_Q\) 的正交投影，因此 \(\|u_Q\|\le\|w\|\)。
结合 (3.2)、(4.1) 得

\[
 \boxed{
 \|u_Q-P_{\le Q}w\|
       \le(e^{-8d^4}+e^{-7d^4})\|w\|.
 }
 \tag{4.3}
\]

## 5. 同一个顶部的全部真实源及完整未来带

固定这个 \(u_Q\)。对 \(4d\le p\le Q\)，令

\[
 r_p=A(u_Q)_p,\qquad v_p=P_{\le p}u_Q.
\]

\(v_p\in V_p\)，且 \(u_Q\perp K_Q\supset K_p\)，所以

\[
 \boxed{v_p=U_pr_p.}
 \tag{5.1}
\]

特别

\[
 \mu_p(r_p)^2-\mu_s(r_s)^2
       =\sum_{j=s+1}^p\|(u_Q)_j\|^2.
 \tag{5.2}
\]

这些截断之间是真实向下源流。只要 \(p<Q\)，准确的固定层源流像定理还给

\[
 r_p\in\mathscr N_p
 =\ker[\iota_0^*(L_p+B_p)],
 \tag{5.3}
\]

其中 \(B_p\) 是原裸源度量。这是原负流图的代数身份；不含任何深联合旗的量化常数。

若 \(p+d\le Q\)，置 \(y_p=P_{[p+1,p+d]}u_Q\)。
记完整物理右核的首输出为 \(F_p\)、\(G_p=F_pF_p^*\)，
其最小右链空间的正交投影为 \(P_{f,p}\)。
对于任何 \(s\in\mathscr R_p\)，同源差

\[
 U_ps-F_p^\dagger s\in K_{p+d}\subseteq K_Q.
\]

它与 \(u_Q\) 正交，故

\[
 \langle L_pr_p,s\rangle
       =\langle y_p,F_p^\dagger s\rangle.
\]

再施加 \(F_p^*\)，得到原平坦链的准确式

\[
 \boxed{F_p^*L_pr_p=P_{f,p}y_p,}
 \qquad
 \lambda_{{\rm flat},p}(r_p)^2\le\|y_p\|^2.
 \tag{5.4}
\]

裸链保留原低旗 \(P_{L,p}\) 与原最小裸核投影 \(P_{b,p}\)。
完整短旗给 \((u_Q)_{p+t}\) 的第 \(i\) 头在
\(\ker D^{d-i}\)。
第 \(t\) 段的高旗在 \(\ker D^{t-1}\) 中，\(A\) 保持它，
而下一段的高旗经 \(D\) 仍落在同一高旗。
所以它们不产生低输出。首段高旗为零，首输出是
\(D(u_Q)_{p+1}=-r_p\)。
于是原裸最小链准确为

\[
 \boxed{a_p(r_p)=-P_{b,p}P_{L,p}y_p,}
 \qquad \alpha_p(r_p)^2\le\|y_p\|^2.
 \tag{5.5}
\]

两投影没有被假设正交；合计正是

\[
 \boxed{\Xi_p(r_p)^2\le2\|y_p\|^2.}
 \tag{5.6}
\]

(5.1)–(5.6) 没有上窗参数，只有固定层闭域、原物理旗、同一个最小者及 \(p+d\le Q\)。故它们在这里的扩大窗口原样成立，不需任何头相似条件数。

## 6. 整个扩大窗口、同一极限与固定测试

现在取 (0.1) 的 \(Q=Q_m\)，并写 \(u_m=u_{Q_m}\)。
令 \(t_m=\tau_m/\|w\|\)。
因尾孔数不超过原总孔数，对全部 \(p\in I_m\)，

\[
 \boxed{
 \mu_{m,p}(r_{m,p})
 \ge\bigl(\sqrt{1-t_m^2}-\varepsilon_m\bigr)\|w\|,
 }
 \tag{6.1}
\]
\[
 \|U_{m,p}r_{m,p}-w\|
 \le\tau_m+\varepsilon_m\|w\|.
 \tag{6.2}
\]

每个物理孔层最多在 \(d\) 个长度 \(d\) 的未来带中出现。
由 (5.6)，

\[
 \sum_{p\in I_m}\Xi_{m,p}(r_{m,p})^2
 \le2d\|P_{[4d+1,Q_m]}u_m\|^2
 \le2d(\tau_m+\varepsilon_m\|w\|)^2.
 \tag{6.3}
\]

任何间距 \(d\) 的子网格 \(\mathcal G_m\subset I_m\) 都有

\[
 \sum_{p\in\mathcal G_m}\Xi_{m,p}(r_{m,p})^2
 \le2(\tau_m+\varepsilon_m\|w\|)^2.
 \tag{6.4}
\]

因此若该网格有 \(K_m\) 个点，至少一个原切口满足

\[
 \Xi_{m,p}(r_{m,p})^2
 \le\frac{2(\tau_m+\varepsilon_m\|w\|)^2}{K_m},
 \qquad K_m\asymp e^{16d^3}/d.
 \tag{6.5}
\]

这里顶部误差只通过真实带覆盖数进入，没有再乘指数多个窗口。

对固定原有限物理测试 \(f\)，令

\[
 t_{m,p}=E_{m,p}P_{V_{m,p}}f.
\]

这是原固定测试的真实 Riesz 源，不是重选源。
由 (5.1)，

\[
 \langle L_{m,p}r_{m,p},t_{m,p}\rangle
       =\langle U_{m,p}r_{m,p},f\rangle
       \longrightarrow\langle w,f\rangle
 \tag{6.6}
\]

对全 \(p\in I_m\) 一致。右边误差至多
\((\tau_m+\varepsilon_m\|w\|)\|f\|\)。
因此新的窗口仍保留同一非零 \(w\) 可被固定低测试看见的实际配对。

## 7. 条件比较目标与不能迁移的部分

充分大 \(m\) 时 (6.1) 的下界为正。对本稿真正未消联合旗的源族，定义

\[
 C_{m,p}(w)=
 \frac{\mu_{m,p}(r_{m,p})^2}
      {\Xi_{m,p}(r_{m,p})^2}.
\]

若分母为零，严格正源度量迫源为零，与 (6.1) 矛盾。
(6.1)、(6.3) 给

\[
 \boxed{
 \frac1d\sum_{p\in I_m}\frac1{C_{m,p}(w)}
 \le
 \frac{2(t_m+\varepsilon_m)^2}
 {(\sqrt{1-t_m^2}-\varepsilon_m)^2}
 \longrightarrow0.
 }
 \tag{7.1}
\]

所以若在这一个实际源族上另有

\[
 \sup_{p\in I_m}C_{m,p}(w)
       =O(e^{16d^3}/d)
 \tag{7.2}
\]

沿一条头子序列成立，就会排除该非零 \(w\)。
本稿未证明 (7.2)。

原深 jets/单高块联合旗的 \(\delta_m\) 估计仍保原已证窗口。
(5.3) 的准确负图已适用新窗口，但不能据此把旧量化旗在
\(p>e^{d^3/4}\) 上也宣称已付。新的全源滤波或其幂若不依赖旧旗，可使用本稿来源；涉及旧联合余旗的版本仍须另外付新范围常数。

原完整高返回、同源左配对及有限头解析核是否能给 (7.2)，仍是实际缺口。母窗口扩大及本稿真实来源接线均未改变普通 Hilbert ISP 的完成标准。

