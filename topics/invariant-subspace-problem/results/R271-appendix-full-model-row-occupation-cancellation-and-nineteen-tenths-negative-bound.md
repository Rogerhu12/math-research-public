# R271 附录：完整模型分析行的占据抵消与原三阶负部十分之十九次下界

日期：2026-11-15（UTC）。

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本文接[秩一 Feshbach 与抛物窗口真实三阶负部](R271-appendix-rank-one-feshbach-lower-bound-and-parabolic-third-jet-negative-obstruction.md)，使用既有[完整模型源比较](R271-appendix-full-model-source-comparison-and-original-primitive-nineteen-tenths-lower-bound.md)。新的一步是保归一模型源的全部强位坐标，并直接支付它们在原占据算子中的能量；不是把旧单源逆下界的指数直接代入 Schur。

这把前稿的 $q^{15/8}$ 三阶负部下界提高到 $q^{19/10}$，仍只排整个真实短核上的统一算子替代。实际同一 $w$ 的源流未被反证。

## 1. 原共同空间和参数

沿用前稿的原连续尾
$$
D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad
S_t=\sum_{j\ge t}(j+1)^{-4},\qquad
W=\sum_{j\ge m}(j+1)^{-4}n_j,
$$
以及 $K_q,\Gamma,H_0,C_*(q+1)$、完整顺次投影 $P_{q+1,j}$ 的定义。所有逆均先在完整固定物理孔层取 MP，再限制 primitive。

令
$$
k=\lfloor q^{4/5}/4\rfloor,\qquad J=m+2q-k,\qquad
S=S_J,\qquad z_*=(J+1)^{-4},\qquad \delta=z_*/S,
$$
$$
\theta=S(m+k)^4,\qquad
\Lambda=\frac{\theta k\delta}{1-k\delta},\qquad
R=e^{2/(m+k+1)}.
\tag{1.1}
$$
假设
$$
m\ge5,\qquad k\ge4(m+1),\qquad m+k+1\ge512.
\tag{1.2}
$$
这些条件对任意固定 $\kappa>0$、$q=\lfloor\kappa(m+1)^2\rfloor$ 在充分大 $m$ 时成立。

仍将原位分成 $k$ 个强位、$q-k$ 个相邻暗对与完整无限远尾；记原 primitive 构造为 $\widetilde f$、全层有界分析为 $\mathcal T_t$、模型 primitive 为 $\omega=\mathcal T_0\widetilde f$。模型核一维及 $\|\mathcal T_t\|\le R$ 均沿用前稿的逐项证明。强位倒数平方对称和记 $E_s$，远尾平方权对称和记 $e_r$，并置
$$
w_s=E_s\frac{e_k}{e_{k-s}},\qquad Z=\sum_{s=0}^kw_s=\|\omega\|^2.
\tag{1.3}
$$
旧完整模型源比较在这个同一原构造上准确给
$$
Z\le\|\widetilde f\|^2\le e^\Lambda Z,\qquad
\frac{\|\mathcal L^{-1}\omega\|^2}{Z}
\ge\frac{k+1-\theta}{S}.
\tag{1.4}
$$
其证明只需 $k\delta<1$、$\theta<k+1$；不另外使用 $q\ge16m^2$。下面常数账本逐项核这些条件。

## 2. 新的完整强位占据恒等式

记模型强位占据为
$$
W_{\rm hd}=\sum_{i\in[k]}a_i^2n_i.
$$
模型的强位标签 $I$、$|I|=s$ 的平方坐标为
$$
|\omega_I|^2=a_I^{-2}\frac{e_k}{e_{k-s}}.
$$
准确计数给
$$
\sum_{|I|=s}a_I^{-2}\sum_{i\in I}a_i^2
=(k-s+1)E_{s-1}.
\tag{2.1}
$$
原因是取消一个 $a_i^{-2}$ 后，每个 $(s-1)$ 元集恰有 $k-s+1$ 个补入位置。因此
$$
\begin{aligned}
\langle W_{\rm hd}\omega,\omega\rangle
&=\sum_{s=1}^{k}(k-s+1)E_{s-1}\frac{e_k}{e_{k-s}}\\
&=\sum_{r=0}^{k-1}
w_r\,(k-r)\frac{e_{k-r}}{e_{k-r-1}}\\
&\le S\sum_{r=0}^{k-1}w_r\le SZ.
\end{aligned}
\tag{2.2}
$$
最后一步是原远尾的 $(t+1)e_{t+1}\le Se_t$。故
$$
\boxed{\langle W_{\rm hd}\omega,\omega\rangle/\|\omega\|^2\le S_J.}
\tag{2.3}
$$
即使 $\theta$ 随 $q$ 增长，强位的真实加权占据能量仍由远尾平方和支付；这里没有用“强位孔数至多 $\theta$”再乘最强权。

## 3. 归一完整分析行仍具有大创建能量

定义
$$
h_\omega=\mathcal T_0^*(\omega/\sqrt Z),\qquad
\ell_\omega=P_{K_q}h_\omega.
\tag{3.1}
$$
不同强位标签在原空间中正交；每个标签的远尾分析行范数为一，中间暗对的共同行平方范数至多 $R^2$。因此
$$
\|h_\omega\|\le R,\qquad
\langle h_\omega,\widetilde f\rangle=\sqrt Z.
$$
由 (1.4) 与真正交投影，
$$
\|\ell_\omega\|^2\ge e^{-\Lambda},\qquad
\|h_\omega-\ell_\omega\|^2\le R^2-e^{-\Lambda}.
\tag{3.2}
$$

(2.3) 支付第一组强位；其余中间位与远尾的全部占据算子不超过 $S_{m+k}I$。故
$$
\langle Wh_\omega,h_\omega\rangle
\le R^2(S_J+S_{m+k})
\le2R^2S_{m+k}.
\tag{3.3}
$$
从 $0\le W\le S_mI$ 得
$$
\langle W\ell_\omega,\ell_\omega\rangle
\le4R^2S_{m+k}+2S_m(R^2-e^{-\Lambda}).
$$
因此
$$
\langle H_0\ell_\omega,\ell_\omega\rangle
\ge S_m\left[
5e^{-\Lambda}-4R^2-8R^2\frac{S_{m+k}}{S_m}
\right].
\tag{3.4}
$$

在 (1.2) 下，$m\le k\le q/4$、$J\ge7q/4$。旧模型比较的直接参数账本给
$$
k\delta<3/7,\qquad
\theta/k\le16/1029<1/64,\qquad
\Lambda\le1/343<1/64.
\tag{3.5}
$$
为免把它们当额外假设：前两式使用 $S\le1/(3J^3)$、
$\delta\le3/(J+1)$ 与 $m+k\le2k$；最后一式使用
$$
\Lambda
=\frac{k(m+k)^4z_*}{1-k\delta}
\le\frac{28k^5}{(J+1)^4}
\le\frac1{343},
$$
其中 $k^5\le q^4/4^5$。

此外前稿的同一积分比较给
$$
R^2\le65/64,\qquad S_{m+k}/S_m\le1/64.
$$
故 (3.4) 中括号至少
$$
5\frac{63}{64}-4\frac{65}{64}
-8\frac{65}{64^2}
=\frac{3000}{4096}>\frac12.
$$
准确得到
$$
\boxed{\langle H_0\ell_\omega,\ell_\omega\rangle\ge S_m/2.}
\tag{3.6}
$$

## 4. 完整秩一下界和真实三阶负部

由于模型次数 $k$ 的核恰为 $\mathbb C\omega$，对任意 $f\in K_q$，
$$
\mathcal T_0f=\langle\ell_\omega,f\rangle\,\omega/\sqrt Z.
$$
对每个完整原像 $Du=f$ 使用同一分析与模型真逆，取原最小值，得到
$$
\boxed{
\Gamma\succeq
\frac{\|\mathcal L^{-1}\omega\|^2}{R^2Z}
|\ell_\omega\rangle\langle\ell_\omega|
\succeq\frac{k+1-\theta}{R^2S_J}
|\ell_\omega\rangle\langle\ell_\omega|.
}
\tag{4.1}
$$
经 $H_0^{1/2}$ 合同，并使用前稿已完整证明的同非零谱关系与 (3.6)，
$$
\begin{aligned}
C_*(q+1)
&=\|H_0^{1/2}\Gamma H_0^{1/2}\|\\
&\ge\frac{(k+1-\theta)S_m}{2R^2S_J}\\
&\ge\frac{63}{64}
       \frac{(k+1)J^3}{4(m+1)^3}\\
&>\frac{21609}{65536}
       \frac{q^{19/5}}{(m+1)^3}
\ge\frac{q^{19/5}}{4(m+1)^3}.
\end{aligned}
\tag{4.2}
$$
全部因子的次序仍保完整 primitive Schur；没有比较 $\Gamma$ 的平方根。

令 $n=q+1$。前稿的真实 $U_{2,n}\oplus U_{3,n}$ 块给，对所有 $3\le h\le n$，
$$
\boxed{
\sup_{\substack{v\in E_{3,n}\cap K_n^\perp\\\|v\|=1}}
-\operatorname{Re}\left\langle
\sum_{j=1}^{h}P_{n,j}v,v
\right\rangle
=\frac{\sqrt{C_*(n)}-3}{2}
\ge
\frac{q^{19/10}}{4(m+1)^{3/2}}-\frac32.
}
\tag{4.3}
$$
所有向量与顺次 MP 的定义域、$P_{n,0}$ 的区别及两端 partial sums 均与前稿相同；本文没有改变任何这些空间。

若 $q\sim\kappa(m+1)^2$，该负部至少为常数乘 $(m+1)^{23/10}$。更一般，新下界相对 $q$ 的因子为 $q^{9/10}/(m+1)^{3/2}$；其强迫增长门槛是 $q\gg(m+1)^{5/3}$（另保 (1.2)）。这只限制全短核的统一算子界，不能把实际源条件拿掉。

## 5. 后继范围

本文保留的新结构是 (2.3)：完整归一模型行的强位加权占据能量不会随其强位平均孔数一起增长。它使秩一 Feshbach 方向在完整 Schur 中仍有大创建能量。

本稿没有证明 (4.3) 的近极值向量来自实际 $u_Q(w)$。实际层向量一般还有 $K_n$ 与更高 $U_{j,n}$ 分量，并满足同一个 $C$ 的递推、完整左右旗和全核正交。任何真正的同源预算仍须支付这些约束；原 $N=M$ 与普通 ISP 继续为 OPEN。
