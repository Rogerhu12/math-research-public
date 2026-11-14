# 实际低测试的两种未来最小化、同源角度差与已付 flat 预算

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

**状态：以下投影识别、非交换恒等式与同窗预算已证明。** 本稿保留原完整左源、真实完整物理右旗和实际低物理测试。它把测试源准确拆成一个已付左小量、一个真核增量及剩余角度源；剩余角度源的 flat 费也有同窗上界，但其裸费和左存活量尚未支付。没有由这些恒等式推出 \(N=M\)。

依赖：
[完整左像与部分零模 Gram](2026-11-14-actual-left-partial-zero-mode-gram-and-source-resolvent-budget-789f-next.md)；
[实际低测试的完整像逆后未来预算](2026-11-14-actual-low-test-full-image-inverse-bosonic-future-budget-789f-next.md)；
[bosonic 未来的真实 bare／完整双投影](2026-11-14-bosonic-future-actual-bare-full-projections-and-ordered-source-contractions-789f-next.md)；
[实际固定测试源流与同一 good-top](../results/R271-appendix-fixed-test-adjoint-source-flow-and-joint-good-top-budget.md)。

## 1. 全部空间和同一个物理源

固定原 \(m,d=2^m,A=A_m,D=D_m\)、尾平方和 \(S\)，以及切口 \(q\)。写
\[
V_q=\mathcal H_{\le q}\cap
  \ker P_{\le q-1}(A+D),\qquad E_qv=Av_q,
\]
\[
\mathscr R_q=\operatorname{Ran}E_q,\qquad
U_q=E_q^\dagger,\qquad L=U_q^*U_q=(E_qE_q^*)^{-1}.
\tag{1.1}
\]
所有源均属于这个原物理 Hilbert 空间 \(\mathscr R_q\)。固定参数下的逆和最小者按原完整层 MP 定理有界；这里不把全部 Fock 层的 \(D^\dagger\) 当作一个有界算子。

记
\[
\mathcal K_j=\ker(A+D)\cap\mathcal H_{\le j}.
\]
固定同一个物理测试 \(f\in\mathcal H_{\le s}\)，以下 \(q\ge s\)，并置
\[
q_f=P_{V_q}f,\qquad k_j=P_{\mathcal K_j}f,\qquad
t=E_qq_f .
\]
则
\[
q_f=k_q+U_qt,\qquad
\langle U_qr,f\rangle=\langle Lr,t\rangle.
\tag{1.2}
\]

完整 bosonic 删除为 \(\mathcal B=\sqrt S\,a_0\)，真实核为
\(\mathcal K_{\rm B}=\ker(A+\mathcal B)\)。定义
\[
\mathcal L_q
=\{z\in\mathcal K_{\rm B}:P_{\le q}z\in\mathcal H_{\rm hc}\},
\qquad \bar z_q=P_{\mathcal L_q}f .
\tag{1.3}
\]
它使用原平方自由前缀条件，绝不是任意横向源空间。

令 \(c_{\rm B}(r)\) 是原源 \(r\) 的完整 bosonic 最小右链，其源 Gram 记为
\[
M=M_{{\rm B},q},\qquad
\|c_{\rm B}(r)\|^2=\langle Mr,r\rangle.
\tag{1.4}
\]
其准确公式是
\[
c_{{\rm B},j}(r)=(-A)^{j-1}
 \frac{(a_0^*)^j}{S^{j/2}}
 (N_0+1)_{\overline j}^{-1}r,\qquad 1\le j\le d.
\]
它先在完整 bosonic 空间取最小逆，再限制到原 \(\mathscr R_q\)。

令 \(\mathcal C_{\rm f}\) 为完整物理右旗可行核，保全部原头旗、尾短核旗、内部方程和末端封口；\(F_{\rm f}\) 读取其第一段的 \(Dc_1\)。写
\[
G=F_{\rm f}F_{\rm f}^*,\qquad
c_{\rm f}(r)=F_{\rm f}^*G^{-1}r,\qquad
\lambda(r)^2=\langle G^{-1}r,r\rangle.
\tag{1.5}
\]
在同一未来 bosonic 直和中，\(P_{\rm f}\) 为到 \(\mathcal C_{\rm f}\) 的物理正交投影。双投影稿已经证明
\[
P_{\rm f}c_{\rm B}(r)=F_{\rm f}^*Mr,\qquad
M\preceq G^{-1}.
\tag{1.6}
\]
原 flat 费仍定义为
\[
\lambda_{\rm flat}(r)^2=\|F_{\rm f}^*Lr\|^2
=\langle LGLr,r\rangle.
\tag{1.7}
\]
这里没有将 flat 费改成同源的普通右费 \(\lambda(r)\)。

## 2. 两个完整投影的准确源

### 2.1 物理左前缀加 bosonic 未来

任意给定左前缀 \(k+U_qr\)，其中 \(k\in\mathcal K_q\)，其横向次数不超过 \(q\) 的完整 bosonic 延拓准确为
\[
k+U_qr-c_{\rm B}(r).
\tag{2.1}
\]
左部分与未来部分按物理总次数正交。其余 bosonic 延拓之差是零左前缀的真核，只含横向次数至少 \(q+1\)，因而与 (2.1) 正交。这就是完整最小性，而非逐层任选右逆。

由于 \(f\) 支持在 \(\le q\)，其与零左前缀的自由核配对为零；在 \(\mathcal K_q\) 上的投影为 \(k_q\)。对剩余源最小化准确得到
\[
\boxed{
\bar r=(L+M)^{-1}Lt,\qquad
\bar z_q=k_q+U_q\bar r-c_{\rm B}(\bar r).
}
\tag{2.2}
\]
因此
\[
\bar r=E_qP_{\le q}\bar z_q .
\tag{2.3}
\]
公式 (2.2) 同时给出了完整像压缩逆的物理解释：它与前稿
\(\overline{\mathfrak H}_q^{-1}P_{\mathcal Z_q^{\rm left}}y_f\)
是同一个最小化问题，没有把实际像换成完整横向空间。

### 2.2 真正有限孔物理核

每个 \(\mathcal K_{q+d}\) 向量可由其左前缀分为：
一个 \(\mathcal K_q\) 分量、一个
\[
U_qr-c_{\rm f}(r),
\]
以及零左前缀的完整物理零源右旗。最后一项与 \(f\) 正交；最小右链与该零源空间也正交。故
\[
\boxed{
u=(L+G^{-1})^{-1}Lt,\qquad
k_{q+d}=k_q+U_qu-c_{\rm f}(u).
}
\tag{2.4}
\]
特别，
\[
u=E_qP_{\le q}k_{q+d},
\]
而全部 \(q\) 到 \(q+d\) 的真核增量恰为
\[
\boxed{
\|k_{q+d}-k_q\|^2
=\mu(u)^2+\lambda(u)^2,\qquad
\mu(r)^2=\langle Lr,r\rangle .
}
\tag{2.5}
\]
这条式子不能只保 \(\mu(u)\) 而丢掉完整右费。

## 3. 精确源差：先支付第一项，再保留角度项

定义
\[
\delta=t-\bar r,\qquad e=\bar r-u,\qquad t-u=\delta+e.
\tag{3.1}
\]
由 (2.2)、(2.4) 按原顺序相乘，
\[
(L+M)\bar r=Lt,\qquad
(I+GL)u=GLt=(GL+GM)\bar r.
\]
所以准确恒等式为
\[
\boxed{(I+GL)e=(I-GM)\bar r.}
\tag{3.2}
\]
左边必须是 \(e=\bar r-u\)。若换成 \(t-u\)，其左边实际等于 \(t\)，并不等于 (3.2) 的右边。

第一项 \(\delta\) 已有与未知角度无关的界。令
\[
C=L^{-1/2}ML^{-1/2}\succeq0,\qquad x=L^{1/2}t .
\]
则
\[
L^{1/2}\bar r=(I+C)^{-1}x,\qquad
L^{1/2}\delta=C(I+C)^{-1}x .
\]
对标量 \(c\ge0\)，
\(c^2/(1+c)^2\le c/4\)，故谱演算给
\[
\boxed{
\mu(t-\bar r)^2\le\frac14\langle Mt,t\rangle .
}
\tag{3.3}
\]
同时
\[
\boxed{
\langle M\bar r,\bar r\rangle
=\langle x,C(I+C)^{-2}x\rangle
\le\langle Mt,t\rangle .
}
\tag{3.4}
\]
这些证明保完整非交换因子次序，只在共同合同后的同一个正算子 \(C\) 上作标量演算。

## 4. 真正的正交角度投影及精确三项能量

有 \(\mathcal K_{q+d}\subseteq\mathcal L_q\)。因此
\[
\Pi_{{\rm gap},q}
=P_{\mathcal L_q}-P_{\mathcal K_{q+d}}
\]
是正交投影，而
\[
\boxed{
\Pi_{{\rm gap},q}f
=\bar z_q-k_{q+d}
=U_qe-\bigl(c_{\rm B}(\bar r)-c_{\rm f}(u)\bigr).
}
\tag{4.1}
\]
它的左前缀是 \(U_qe\)。完整范数准确为
\[
\boxed{
\|\Pi_{{\rm gap},q}f\|^2
=\left\langle Lt,
 \bigl[(L+M)^{-1}-(L+G^{-1})^{-1}\bigr]Lt
 \right\rangle .
}
\tag{4.2}
\]
两逆仍作用在同一个原 \(\mathscr R_q\) 上。

(2.2)、(2.4) 相减还给
\[
G^{-1}u-M\bar r=Le.
\]
结合 (1.6)，得到一个完全物理的完整右旗恒等式
\[
\boxed{
F_{\rm f}^*Le
=c_{\rm f}(u)-P_{\rm f}c_{\rm B}(\bar r).
}
\tag{4.3}
\]
所以剩余角度源的 flat 链已经被两个真实同源投影列准确表示，并有
\[
\boxed{
\lambda_{\rm flat}(e)^2
\le2\lambda(u)^2+2\langle M\bar r,\bar r\rangle .
}
\tag{4.4}
\]

再把 \(c_{\rm B}(\bar r)\) 按 \(P_{\rm f}\) 正交分解，(4.1) 给精确 Pythagoras：
\[
\boxed{
\begin{aligned}
\|\Pi_{{\rm gap},q}f\|^2
={}&\mu(e)^2+\lambda_{\rm flat}(e)^2\\
&+\langle M\bar r,\bar r\rangle
 -\langle M\bar r,GM\bar r\rangle .
\end{aligned}
}
\tag{4.5}
\]
最后一行是 \(\|(I-P_{\rm f})c_{\rm B}(\bar r)\|^2\ge0\)。
因此即使两个未来项都小，仍不能从 (4.5) 删除 \(\mu(e)^2\)。

## 5. 同一个固定测试和原 good-top 中的锐化预算

以下 \(q\ge s+1\)。原真实固定测试流给
\[
t_q=-A v_q,\qquad
\sum_{q\ge s+1}\|v_q\|^2\le\|f\|^2.
\tag{5.1}
\]
完整头 Gram 为
\[
H_A=\sum_{j<d}\frac{(A^j)^*A^j}{S^j j!}
\preceq C_mI .
\]
使用 (1.4) 的完整 bosonic 幂最小逆，头尾交换以及
\((N_0+1)_{\overline j}\ge j!\)，准确有
\[
\begin{aligned}
\langle M_{{\rm B},q}t_q,t_q\rangle
&=\sum_{j=1}^{d}\|\mathcal I_{j,q}A^jv_q\|^2\\
&\le\langle(H_A-I)v_q,v_q\rangle\\
&\le(C_m-1)\|v_q\|^2 .
\end{aligned}
\tag{5.2}
\]
其中 \(A^d=0\) 杀掉最后一项，不需要在整个 Fock 空间使用一个无界的幂逆。

设 \(\mathcal J\subseteq\{s+1,s+2,\ldots\}\) 是步长至少 \(d\) 的切口网格。由真核递增及固定同一 \(f\)，
\[
\sum_{q\in\mathcal J}
 \bigl(\mu(u_q)^2+\lambda(u_q)^2\bigr)
=\sum_{q\in\mathcal J}\|k_{q+d}-k_q\|^2
\le\|f\|^2.
\tag{5.3}
\]
因此 (3.3)、(3.4)、(4.4) 直接给
\[
\boxed{
\sum_{q\in\mathcal J}\mu(t_q-\bar r_q)^2
\le\frac{C_m-1}{4}\|f\|^2,
}
\tag{5.4}
\]
\[
\boxed{
\sum_{q\in\mathcal J}\lambda_{\rm flat}(e_q)^2
\le2C_m\|f\|^2.
}
\tag{5.5}
\]
并且 \(t_q-e_q=(t_q-\bar r_q)+u_q\)，从而
\[
\boxed{
\sum_{q\in\mathcal J}\mu(t_q-e_q)^2
\le\left(\frac{C_m-1}{2}+2\right)\|f\|^2.
}
\tag{5.6}
\]
所以 \(e_q\) 在原左范数中接近原实际测试源，且它的原 flat 费也已支付；没有改变源上的 \(L\) 或 \(G\)。

这些结论也逐个输入给固定测试空间上的正算子序。更具体地，沿原稿的 \(\Psi_p\succeq0\)，
\[
\|v_q(f)\|^2\le\langle\Psi_qf,f\rangle,\qquad
\mu(u_q(f))^2+\lambda(u_q(f))^2
\le\left\langle\sum_{p=q+1}^{q+d}\Psi_pf,f\right\rangle .
\]
故
\[
\mu(t_q-e_q)^2
\le\frac{C_m-1}{2}\langle\Psi_qf,f\rangle
 +2\left\langle\sum_{p=q+1}^{q+d}\Psi_pf,f\right\rangle ,
\tag{5.7}
\]
\[
\lambda_{\rm flat}(e_q)^2
\le2(C_m-1)\langle\Psi_qf,f\rangle
 +2\left\langle\sum_{p=q+1}^{q+d}\Psi_pf,f\right\rangle .
\tag{5.8}
\]
所以原来已经选定、同时保完整两费和
\(\sum_{p=q}^{q+d}\Psi_p\) 的 good-top 可直接使用这些界，无需另选一个不相同的切口。

## 6. 剩余范围

对任何同切口原来源 \(r\)，原固定物理功能准确拆成
\[
\langle Lr,t_q\rangle
=\langle Lr,t_q-e_q\rangle+\langle Lr,e_q\rangle .
\tag{6.1}
\]
第一项可用原 \(\mu(r)\) 与 (5.7) 支付。第二项保留同一个实际角度源 \(e_q\)。

虽然 (5.8) 已支付 \(e_q\) 的 flat 费，它并不支付其裸费
\(\langle Be_q,e_q\rangle\)，也不自动控制
\(\langle Lr,e_q\rangle\)。两个源的 flat 费都小，仍不能以此比较它们的左内积。

当固定 \(m\) 而令 \(q\to\infty\) 时，\(\mathcal L_q\) 递减到完整平方自由真核，而 \(\bigcup_q\mathcal K_q\) 在该核中稠密。后一点可用原第一物理头参数化 \(P(D)g\)、\(g\in\ker D^d\) 后按孔层截断证明；这只使用固定头的有限有界同构。因此 \(\Pi_{{\rm gap},q}\to0\) 强成立。它未给 \(m,q\) 同时变化时的速率，不能套入原移动窗口。

本稿没有支付 \(\mu(e_q)\) 的同阶平方和、\(e_q\) 的裸费或完整两费局部逆，也没有把固定 \(m\) 的强收敛冒称原 \(N=M\) 的证明。
