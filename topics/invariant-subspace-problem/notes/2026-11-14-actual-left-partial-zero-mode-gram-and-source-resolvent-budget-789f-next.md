# 实际左可行空间的部分零模 Gram 与同源 \(Z_q^{-1}\) 预算

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

**状态：已证明的中间结论。** [全真核零占据稿](2026-11-14-full-boolean-kernel-bosonic-zero-occupation-and-head-only-budget-789f-next.md)的正预算可扩到原真实左可行空间，而不要求顶部源为零。本文给它的准确部分零模 Gram、保持整个左前缀的 bosonic 核延伸，以及原 source Riccati 正逆 \(Z_q^{-1}\) 在同一个实际源上的比较。常数仍是 \(\log C_m=O(m\log(m+1))\)，独立孔截止。

比较后的零模像仍是原硬核约束的准确闭像；它没有被替换为任意横向向量。因而此结果不宣称 \(Z_q^{-1}\) 保固定出生，也未免费支付未来 bare 或普通右费。

## 1. 实际左空间与横向分解

固定原 \(m,d=2^m,A=A_m,D=D_m\)，记尾平方和为 \(S\)。沿用完整 bosonic 嵌入
\[
\mathcal B=\sqrt S\,a_0,\qquad
\mathcal F=\Gamma_{\rm s}(\mathbb Cu)\otimes\Gamma_{\rm s}(u^\perp),
\]
及零占据投影 \(P_0\)。原平方自由层记为 \(\mathcal H_p\)，头恒等默认保留。

对 \(p\ge0\)，原左可行空间及源映射是
\[
V_p=\mathcal H_{\le p}\cap
 \ker P_{\le p-1}(A+D),\qquad E_pv=Av_p.
\tag{1.1}
\]
\(V_p\) 闭。源空间取原闭值域
\(\mathscr R_p=\operatorname{Ran}E_p\)，并用原完整左最小费
\[
\mu_p(r)^2=\min\{\|v\|^2:v\in V_p,\ E_pv=r\}.
\tag{1.2}
\]

将一个 \(v\in V_p\) 按横向次数 \(b\) 和集体占据 \(j\) 展开：
\[
v=\sum_{b+j\le p}|j\rangle_0\otimes v_{b,j},
\qquad
v_{b,j}\in\mathcal E\otimes\Gamma_{\rm s}^b(u^\perp).
\]
由于 \(A\) 不改尾次数，\(\mathcal B\) 只降低集体占据，全部真正低输出行给
\[
Av_{b,j}+\sqrt{S(j+1)}\,v_{b,j+1}=0
\qquad(b+j\le p-1).
\tag{1.3}
\]
所以置 \(h_b=v_{b,0}\)，有
\[
\boxed{
v_{b,j}=\frac{(-A)^jh_b}{\sqrt{S^j j!}}
\quad(0\le j\le p-b).
}
\tag{1.4}
\]
当 \(j\ge d\) 时该项为零。由此
\[
\boxed{
v=P_{\le p}\mathcal R_Ah,\qquad h=P_0v,\quad
h=\bigoplus_{b=0}^{p}h_b.
}
\tag{1.5}
\]
这里 \(\mathcal R_A\) 是前稿的有限集体创建重构算子。

## 2. 完整部分 Gram 与准确闭像

在横向次数 \(b\) 上定义头矩阵
\[
H_{p,b}
=\sum_{j=0}^{\min(d-1,p-b)}
   \frac{(A^j)^*A^j}{S^j j!},
\]
并令
\[
\mathbf H_p=\bigoplus_{b=0}^{p}
 \left(H_{p,b}\otimes I_{\Gamma_{\rm s}^b(u^\perp)}\right).
\tag{2.1}
\]
不同 \(b,j\) 在完整 Fock 内积中正交，因此
\[
\boxed{\|v\|^2=\langle\mathbf H_ph,h\rangle.}
\tag{2.2}
\]
前稿的原头预算给
\[
\boxed{I\preceq\mathbf H_p\preceq C_mI,\qquad
\log C_m=O(m\log(m+1)).}
\tag{2.3}
\]

必须保留的源像为
\[
\boxed{
\mathcal Z_p^{\rm left}
=\{h\in\mathcal E\otimes\Gamma_{\rm s}^{\le p}(u^\perp):
      P_{\le p}\mathcal R_Ah
         \in\mathcal E\otimes\mathcal H_{\rm hc}\}.
}
\tag{2.4}
\]
因为 \(\mathcal R_A\) 有界、硬核空间闭，\(\mathcal Z_p^{\rm left}\) 闭。
任意 (2.4) 的 \(h\) 经 \(P_{\le p}\mathcal R_A\) 都满足原低行；反向由 (1.5) 成立。所以
\[
P_0V_p=\mathcal Z_p^{\rm left},\qquad
\mathcal T_p:=P_{\le p}\mathcal R_A|_{\mathcal Z_p^{\rm left}}
: \mathcal Z_p^{\rm left}\longrightarrow V_p
\tag{2.5}
\]
是有界双射，其逆是 \(P_0|_{V_p}\)。

记 \(P_{\mathcal Z_p}\) 为准确像上的正交投影。真正左域 Gram 是
\[
\boxed{
\mathfrak H_p
=P_{\mathcal Z_p}\mathbf H_p|_{\mathcal Z_p^{\rm left}},
\qquad I\preceq\mathfrak H_p\preceq C_mI.
}
\tag{2.6}
\]
后文所有逆均在此完整闭像上。没有用
\(P_{\mathcal Z_p}\mathbf H_p^{-1}P_{\mathcal Z_p}\)
替代 \(\mathfrak H_p^{-1}\)。

## 3. 保全部左前缀的有限 bosonic 延伸

对 \(v\in V_p\)，置
\[
\widehat v=\mathcal R_AP_0v.
\]
由构造，
\[
(A+\mathcal B)\widehat v=0,\qquad
P_{\le p}\widehat v=v,\qquad
\operatorname{supp}\widehat v\subseteq[0,p+d-1].
\tag{3.1}
\]
其总能量准确为
\[
\|\widehat v\|^2
=\sum_{b\le p}\sum_{j<d}
       \frac{\|A^jh_b\|^2}{S^j j!}
\le C_m\|h\|^2\le C_m\|v\|^2.
\tag{3.2}
\]
所以每个实际左可行向量都有保整个左前缀、费用至多 \(C_m\) 的真 **bosonic** 核延伸。

未来部分可能含重复占据。即使先投回硬核，它也通常带真实方程残量。因此 (3.2) 不是原普通右链费用界，更不是 \(\lambda\le\sqrt{C_m}\mu\)；已有相应真实有限反例排除了这种无条件外推。

## 4. 同一个实际边界源的零模变分式

定义准确边界读取
\[
\mathscr E_p:\mathcal Z_p^{\rm left}\to\mathscr R_p,\qquad
\mathscr E_ph=A(\mathcal T_ph)_p.
\tag{4.1}
\]
它与 (1.1) 的 \(E_p\) 使用同一个物理源。由 (1.4)，可写成
\[
\mathscr E_ph
=\sum_{j=0}^{\min(p,d-1)}
  \frac{(-1)^jA^{j+1}(a_0^*)^j h_{p-j}}
       {S^{j/2}j!},
\tag{4.2}
\]
其中和的物理平方自由性由 \(h\in\mathcal Z_p^{\rm left}\) 保证，而非逐项假定。

原左最小费因此是
\[
\boxed{
\mu_p(r)^2
=\inf_{\substack{h\in\mathcal Z_p^{\rm left}\\
                 \mathscr E_ph=r}}
       \langle\mathfrak H_ph,h\rangle.
}
\tag{4.3}
\]
另定义同一可行集上的零模费
\[
\mu_{0,p}(r)^2
=\inf_{\substack{h\in\mathcal Z_p^{\rm left}\\
                 \mathscr E_ph=r}}\|h\|^2.
\]
由 (2.6)，
\[
\boxed{\mu_{0,p}(r)^2\le\mu_p(r)^2
                  \le C_m\mu_{0,p}(r)^2.}
\tag{4.4}
\]

在原源内积中置
\[
J_p=E_pE_p^*,\qquad
J_{0,p}=\mathscr E_p\mathscr E_p^*.
\]
由于 \(\mathcal T_p^*\mathcal T_p=\mathfrak H_p\)，使用其真正有界逆给
\[
\boxed{
J_p=\mathscr E_p\mathfrak H_p^{-1}\mathscr E_p^*,
\qquad C_m^{-1}J_{0,p}\preceq J_p\preceq J_{0,p}.
}
\tag{4.5}
\]
这里的 \(J_p\) 正是原 source Riccati 中的完整左源 Gram，不是另一个缩小源的矩阵。

## 5. 真正 \(Z_p^{-1}\) 的同源比较：完整尾列保留

沿 [R271 实际测试流](../results/R271-appendix-fixed-test-adjoint-source-flow-and-joint-good-top-budget.md)，记
\[
\mathscr X_p
=\bigoplus_{i=0}^{d-1}e_i
  (\ker D^{d-i}\cap\mathcal H_p),\qquad
\mathcal D_p=D|_{\mathscr X_p}:\mathscr X_p\to\mathscr R_{p-1}.
\]
每个伴随都仍是这个原受限映射的伴随。原正逆为
\[
Z_p=J_{p-1}+\mathcal D_p\mathcal D_p^*.
\]
仅把左 Gram 换成 §4 的同源零模 Gram，定义
\[
Z_{0,p}=J_{0,p-1}+\mathcal D_p\mathcal D_p^*.
\tag{5.1}
\]
没有扩大 \(\mathscr X_p\)，也没有先把尾列压到某个 primitive 出生。

由 (4.5) 及 \(C_m\ge1\)，
\[
C_m^{-1}Z_{0,p}\preceq Z_p\preceq Z_{0,p},
\]
所以在同一个 \(\mathscr R_{p-1}\) 上
\[
\boxed{
Z_{0,p}^{-1}\preceq Z_p^{-1}
                  \preceq C_m Z_{0,p}^{-1}.
}
\tag{5.2}
\]
全部源和参数均保持原值。

更直接的原可行集解释是
\[
\boxed{
\langle Z_p^{-1}t,t\rangle
=
\inf_{\substack{x\in\mathscr X_p,\ h\in\mathcal Z_{p-1}^{\rm left}\\
       \mathcal D_px+\mathscr E_{p-1}h=t}}
  \left(\|x\|^2+\langle\mathfrak H_{p-1}h,h\rangle\right).
}
\tag{5.3}
\]
将后一个二次型换成 \(\|h\|^2\) 得到
\(\langle Z_{0,p}^{-1}t,t\rangle\)。这证明 (5.2) 的比较是在完整同一 source splitting 上完成；不是把两个互不相同的 nuisance 先删去再比较。

(5.2) 只比较二次能量。不能从它推出向量
\(Z_p^{-1}t\)、\(Z_{0,p}^{-1}t\) 属于同一个固定出生旗，或把其中一个实际源替换成另一个源。

## 6. 固定物理测试在零模中仍由固定低次数功能读取

若 \(f\) 支持在原物理尾次数 \(\le s\)，则对全部 \(p\ge s\)，
\[
\langle f,v\rangle
=\langle y_f,h\rangle,\qquad
v=\mathcal T_ph,\qquad
y_f=\mathcal R_A^*f.
\tag{6.1}
\]
\(\mathcal R_A\) 只增加尾次数，所以 \(y_f\) 的横向次数至多 \(s\)，且不随 \(p\) 改变。若 \(f\) 的尾为真空——原固定有限物理头测试即属此类——则
\[
\boxed{y_f=f.}
\tag{6.2}
\]
因此原左投影 \(q_p=P_{V_p}f\) 的零模坐标准确为
\[
\boxed{
P_0q_p=\mathfrak H_p^{-1}P_{\mathcal Z_p}y_f.
}
\tag{6.3}
\]
这保留同一个固定测试。实际零模像投影
\(P_{\mathcal Z_p}\) 及完整压缩逆仍可能把其反馈散到高横向次数；
(6.3) 不等于“测试源保持固定出生”。

原固定测试的 \(t_p=E_pq_p\)、以及随后
\(Z_p^{-1}t_{p-1}\) 的全部定义因此都可在上述同源闭像中读取。
新的已付量是原左域和同源 \(Z_p^{-1}\) 的头费用 \(C_m\)；
硬核像的跨次数 Schur、未来高返回和 mixed flat 度量继续保留。
