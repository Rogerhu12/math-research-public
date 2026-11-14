# 固定物理测试经实际左像压缩逆后的全未来 bosonic 能量预算

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

**状态：已证明的中间结论。** 本稿继续[实际左域部分零模 Gram](2026-11-14-actual-left-partial-zero-mode-gram-and-source-resolvent-budget-789f-next.md)，对同一个固定物理测试 \(f\) 和真正 \(q_p=P_{V_p}f\)，支付完整像投影、完整压缩逆之后的未来能量。准确结论是
\[
\sum_{p\ge s}\|P_{>p}\mathcal R_AP_0q_p\|^2
\le C_m^2 k_0(2+\log d)^2\|f\|^2,
\qquad f\in\mathcal H_{\le s}.
\]
常数为 \(\exp(O(m\log(m+1)))\)，独立所有切口和出生。随后减去真实零源投影 \(k_p\) 不改变该未来部分，所以这也是原实际 Riesz 源 \(t_p\) 的同源 bosonic 完整右链费用。

这条链尚未必平方自由；本稿没有把它认作原普通右链或 bare 可行链。新的预算确实针对原低测试，而非假设固定低出生旗在压缩逆下不变。

## 1. 固定对象与完整 bosonic 核

固定原 \(m\ge5,d=2^m,A=A_m,D=D_m\)、尾平方和 \(S\)。
保留完整 bosonic 集体模式 \(\mathcal B=\sqrt S a_0\)，以及
\[
\mathcal K_{\rm B}=\ker(A+\mathcal B).
\]
零模重构给
\[
\mathcal R_Ah
=\sum_{j<d}\frac{(-A)^j(a_0^*)^jh}{S^{j/2}j!},
\quad
\|\mathcal R_Ah\|^2
=\langle H_Ah,h\rangle,
\]
\[
H_A=\sum_{j<d}\frac{(A^j)^*A^j}{S^j j!},
\qquad I\preceq H_A\preceq C_mI.
\tag{1.1}
\]
\(H_A\) 只作用头，并保持每个横向次数。原 carry 预算给
\(\log C_m=O(m\log(m+1))\)。

前稿集体占据矩的证明只用 (1.1) 和原 \(A\) 的幂界，实际上对
**整个** \(\mathcal K_{\rm B}\) 都成立，无需其向量平方自由。因此
\[
\boxed{
\langle N_0z,z\rangle\le k_0\|z\|^2
\quad(z\in\mathcal K_{\rm B}),\qquad
k_0=\max(2m,16).
}
\tag{1.2}
\]
所有此类向量的集体占据还准确至多 \(d-1\)。

以下 \(P_p=1_{\{N_{\rm tot}\le p\}}\)，
\(R_p=1_{\{N_\perp\le p\}}\)，\(Q_{\rm hc}\) 为硬核投影。
记 \(F_p=R_p-P_p\)。由两种次数的交换和层计数，
\[
\boxed{
\mathscr F:z\longmapsto(F_pz)_{p\ge0}
\text{ 在 }\mathcal K_{\rm B}\text{ 上有范数至多 }\sqrt{k_0}.
}
\tag{1.3}
\]

## 2. 一个真正递减的共同 Hilbert 空间族

定义
\[
\boxed{
\mathcal L_p
=\{z\in\mathcal K_{\rm B}:P_pz\in\mathcal H_{\rm hc}\}.
}
\tag{2.1}
\]
它们是完整 Fock 范数中的闭子空间，并满足
\(\mathcal L_{p+1}\subseteq\mathcal L_p\)。
这里没有声称原 \(V_p\) 本身递减。

固定同一个物理测试 \(f\in\mathcal H_{\le s}\)。对 \(p\ge s\)，置
\[
\bar z_p=P_{\mathcal L_p}f.
\tag{2.2}
\]
高横向次数子空间
\(\mathcal R_A\Gamma_{\rm s}^{>p}(u^\perp)\) 完全包含于 \(\mathcal L_p\)，
且在 (1.1) 的物理范数中与低横向次数正交。
因为 \(f\) 的总次数至多 \(s\le p\)，其在该高子空间上的配对为零。所以
\[
\boxed{
R_p\bar z_p=\bar z_p,\qquad
\operatorname{supp}\bar z_p\subseteq[0,p+d-1].
}
\tag{2.3}
\]
特别
\[
F_p\bar z_p=P_{>p}\bar z_p.
\tag{2.4}
\]

令
\[
\Pi_j=P_{\mathcal L_{j-1}}-P_{\mathcal L_j}
\qquad(j\ge s+1).
\]
因 \(\mathcal L_j\) 递减，\(\Pi_j\) 是两两正交的投影。其像属于
\(\mathcal K_{\rm B}\)。同时，高横向 \(>j\) 子空间包含于
\(\mathcal L_j\)，故 \(\operatorname{Ran}\Pi_j\) 的横向次数至多 \(j\)，总次数至多 \(j+d-1\)。于是
\[
\boxed{F_p\Pi_j=0\qquad(p\ge j+d-1).}
\tag{2.5}
\]
这是每个投影像的算子性质，不仅是某个选定向量的支撑观察。

## 3. 同一递减投影流的未来能量总和

由嵌套投影的恒等式，
\[
\bar z_p=\bar z_s-\sum_{j=s+1}^p\Pi_jf.
\]
结合 (2.5)，
\[
F_p\bar z_p
=F_p\bar z_s-\sum_{\substack{s<j\le p\\p-j<d-1}}F_p\Pi_jf.
\tag{3.1}
\]
第二项是 (1.3) 的分析算子在正交输入分解
\(\bigoplus_j\operatorname{Ran}\Pi_j\) 上，截取宽度不超过 \(d\) 的对角带。

为明示完整常数，区间乘子
\[
D_d(t)=\sum_{r=0}^{d-1}e^{irt}
\]
满足
\[
\frac1{2\pi}\int_{-\pi}^{\pi}|D_d(t)|\,dt
\le1+\log d.
\tag{3.2}
\]
这是由
\(|D_d(t)|\le\min(d,\pi/|t|)\)
在 \(0<|t|\le\pi\) 上积分所得。
对输入第 \(j\) 块、输出第 \(p\) 行分别施加相位酉，用 (3.2) 作 Fourier 平均，便准确保留 \(0\le p-j<d\) 的块。因此第二项的总分析范数至多
\[
(1+\log d)\sqrt{k_0}\|f\|.
\]
第一项由 (1.3) 及 \(\|\bar z_s\|\le\|f\|\) 至多为
\(\sqrt{k_0}\|f\|\)。
在输出 Hilbert 直和中用一次三角不等式，再用 (2.4)，得到
\[
\boxed{
\sum_{p\ge s}\|P_{>p}\bar z_p\|^2
\le k_0(2+\log d)^2\|f\|^2.
}
\tag{3.3}
\]
这个证明完整处理了随 \(p\) 变化的 \(\bar z_p\)，没有错误地将固定向量的 (1.3) 逐次套给它们后求和。

## 4. 两个逆仍在同一个原硬核像上

保留原实际左空间
\[
V_p=\mathcal H_{\le p}\cap
   \ker P_{\le p-1}(A+D),\qquad q_p=P_{V_p}f.
\]
令
\(\mathcal Z_p^{\rm left}=P_0V_p\)，并记其投影为 \(P_{\mathcal Z_p}\)。
前稿的部分头 Gram 在横向次数 \(b\le p\) 上为
\[
H_{p,b}
=\sum_{j\le\min(d-1,p-b)}
     \frac{(A^j)^*A^j}{S^j j!}.
\]
将其准确压缩到 \(\mathcal Z_p^{\rm left}\)，记为
\(\mathfrak H_p\)。另将完整 \(H_A\) 压缩到**同一个像**，记为
\[
\overline{\mathfrak H}_p
=P_{\mathcal Z_p}H_A|_{\mathcal Z_p^{\rm left}},
\qquad
\mathfrak T_p=\overline{\mathfrak H}_p-\mathfrak H_p\succeq0.
\tag{4.1}
\]
有
\[
I\preceq\mathfrak H_p\preceq
\overline{\mathfrak H}_p\preceq C_mI,
\qquad
0\preceq\mathfrak T_p\preceq(C_m-1)\mathfrak H_p.
\tag{4.2}
\]

固定功能为 \(y_f=\mathcal R_A^*f\)，支撑横向次数至多 \(s\)。
置 \(y_p=P_{\mathcal Z_p}y_f\)。
由两个真实最小二乘问题，
\[
\boxed{
h_p=P_0q_p=\mathfrak H_p^{-1}y_p,\qquad
\bar h_p=P_0\bar z_p
   =\overline{\mathfrak H}_p^{-1}y_p.
}
\tag{4.3}
\]
第二式成立，是因为 (2.1) 的低横向部分恰为同一个
\(\mathcal Z_p^{\rm left}\)，而高横向部分与固定功能正交。
所以比较中没有交换压缩和求逆，也没有假设
\(\mathcal Z_p^{\rm left}\) 被 \(R_q\) 保持。

对任意 \(h\in\mathcal Z_p^{\rm left}\)，
\[
\langle\mathfrak T_ph,h\rangle
=\|P_{>p}\mathcal R_Ah\|^2.
\tag{4.4}
\]
由 (4.3)，
\[
h_p=\bar h_p+\mathfrak H_p^{-1}\mathfrak T_p\bar h_p.
\]
令 \(C=\mathfrak T_p^{1/2}\mathfrak H_p^{-1}
                  \mathfrak T_p^{1/2}\)；
(4.2) 给 \(0\preceq C\preceq(C_m-1)I\)。因此
\[
\mathfrak T_p^{1/2}h_p
=(I+C)\mathfrak T_p^{1/2}\bar h_p,
\]
从而
\[
\boxed{
\|P_{>p}\mathcal R_Ah_p\|^2
\le C_m^2\|P_{>p}\bar z_p\|^2.
}
\tag{4.5}
\]
同时原左前缀差还有
\[
\boxed{
\|q_p-P_p\bar z_p\|^2
\le(C_m-1)\|P_{>p}\bar z_p\|^2.
}
\tag{4.6}
\]
这是保完整非交换次序的正算子估计。

## 5. 原实际左投影的未来预算

把 (4.5) 对同一固定测试的全部切口求和，再用 (3.3)，得到
\[
\boxed{
\sum_{p\ge s}
 \|P_{>p}\mathcal R_AP_0q_p\|^2
\le C_m^2 k_0(2+\log d)^2\|f\|^2.
}
\tag{5.1}
\]
(4.6) 也给
\[
\boxed{
\sum_{p\ge s}\|q_p-P_p\bar z_p\|^2
\le(C_m-1)k_0(2+\log d)^2\|f\|^2.
}
\tag{5.2}
\]

在零模坐标中，(5.1) 的被积项准确为
\[
\sum_{b\le p}\sum_{\substack{p-b<j<d}}
  \frac{\|A^jh_{p,b}\|^2}{S^j j!}.
\tag{5.3}
\]
所以这是一条完整像压缩逆之后的**加权高出生反馈**预算。
它没有声称未加权 \(\|h_{p,b}\|\) 在所有高出生方向上小；例如被 \(A\) 杀掉的方向不被 (5.3) 收费。

## 6. 同一个实际 Riesz 源的 bosonic 右链

令
\[
\mathcal K_p=\ker(A+D)\cap\mathcal H_{\le p},\qquad
k_p=P_{\mathcal K_p}f,
\]
并保持原真实测试源
\[
t_p=E_pq_p,\qquad U_pt_p=q_p-k_p.
\]
对真核 \(k_p\)，重构准确给
\(\mathcal R_AP_0k_p=k_p\)，故没有未来部分。
于是
\[
\widehat u_p=\mathcal R_AP_0(q_p-k_p)
\]
满足
\[
(A+\mathcal B)\widehat u_p=0,\qquad
P_p\widehat u_p=U_pt_p,\qquad
P_{>p}\widehat u_p=P_{>p}\mathcal R_AP_0q_p.
\tag{6.1}
\]
定义
\[
c_{p,j}=-(\widehat u_p)_{p+j}\quad(1\le j\le d-1),
\qquad c_{p,d}=0.
\]
它们是同一个真实源 \(t_p\) 的完整 bosonic 右链：
\[
\boxed{
\mathcal Bc_{p,1}=t_p,\qquad
Ac_{p,j}+\mathcal Bc_{p,j+1}=0,\qquad Ac_{p,d}=0.
}
\tag{6.2}
\]
全部头坐标和强度仍是原 \(A_m,S_m\)。由 (5.1)，
\[
\boxed{
\sum_{p\ge s}\sum_{j=1}^d\|c_{p,j}\|^2
\le C_m^2k_0(2+\log d)^2\|f\|^2.
}
\tag{6.3}
\]
不同切口的源仍是原同一个固定测试生成的 \(t_p\)，未在每个切口重新择源。

这些未来列的横向次数至多 \(p\)，因此与原 future 高返回空间
\[
\mathcal H_{\rm hc}\cap\{N_\perp\ge p+2\}
\]
正交。它们自身未必平方自由；该正交性不把它们变成 bare 可行链。

## 7. 投回硬核后的误差及同窗使用范围

令 \(\widetilde u_p=Q_{\rm hc}\widehat u_p\)。
它保留原左最小者 \(U_pt_p\) 的整个左前缀。
因为那个左前缀已平方自由，
\[
\|(I-Q_{\rm hc})\widehat u_p\|
\le\|P_{>p}\widehat u_p\|.
\]
利用前一切口稿逐纤维证明的
\(\|Q_{\rm hc}\mathcal B(I-Q_{\rm hc})\|\le\sqrt{2S}\)，有准确残量
\[
(A+D)\widetilde u_p
=-Q_{\rm hc}\mathcal B(I-Q_{\rm hc})\widehat u_p.
\]
因此
\[
\boxed{
\sum_{p\ge s}\|(A+D)\widetilde u_p\|^2
\le2S C_m^2k_0(2+\log d)^2\|f\|^2.
}
\tag{7.1}
\]

对固定 \(n\) 个正交单位物理测试，将 (6.3)–(7.1) 求和后，可与原两费预算在同一个 \(K_{\rm win}\) 切口窗口平均；未来 bosonic 费的共同上界为
\[
\frac{n C_m^2k_0(2+\log d)^2}{K_{\rm win}}.
\]
其分子为 \(\exp(O(m\log(m+1)))\)，沿原
\(m=O(\log\log q)\) 为 \(q^{o(1)}\)。

仍须支付的内容准确是：投回原平方自由／短核旗后，内部方程的残量怎样在同一个实际源和原 mixed flat 度量中处理。不能只因 (7.1) 的物理残量小就调用一个没有统一费用的逆，也不能删除 boundary 已保留的 \(E^{\rm ret}\)。本稿没有完成该硬核高返回修复或 \(N=M\)。
