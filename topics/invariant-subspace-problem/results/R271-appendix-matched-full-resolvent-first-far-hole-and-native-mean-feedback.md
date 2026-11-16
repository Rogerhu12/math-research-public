# R271 附录：匹配完整 Schur 的第一远孔读数与 native 平均首反馈

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿将一个指定的原方差首源反馈，送入原来未付的完整配对
$\langle(H-B)r_w,s_f\rangle$。结论保同一个实际 $w$、完整 $h$ 段、全部左右零源、匹配切口的真正完整最小源，以及帽返回的逆伴随和外投影。它支付按 $p_i=b_i^2/S$ 合并的反馈 $\bar\alpha$；原第一源方程中的平均真空分支 $\bar g_0$ 仍明确保留。本稿不证明任意 forcing 的主交叉小，也不证明 $N=M$。

内积约定为对第一变量线性；例如 $\langle Ax,y\rangle=\langle x,A^*y\rangle$。头 bosonic Gram 记为 $\mathsf H$，完整普通右费仍记为 $H$，两者始终区别。

依据：

- [强尾联块的同一顶部源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。
- [完整返回的物理正交分解](R271-appendix-complete-return-orthogonal-decomposition-driven-system-and-unique-lift.md)。
- [joined 与 coherent forcing 的完整源 Gram](R271-appendix-joined-quotient-coherent-forcing-congruence-and-complete-source-gram.md)。
- [原方差一位完整恢复](R271-appendix-native-variance-one-bit-restoration-and-auxiliary-clearing-pairing.md)。
- [真实帽配对及相邻创建来源](R271-appendix-adjacent-creation-actual-return-pair-and-true-hat-transport.md)。

## 1. 同一原来源与固定切口

保原 N/Y 模型
$$
C=A_m+D_{[m,x)},\quad R=x-m,\quad d=2^m,\quad h=d+R,\quad C^h=0,
$$
$$
D=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad
z_i=b_i^2,\qquad S=\sum_{i\ge x}z_i.
\tag{1.1}
$$
本稿要求 $x\ge64$、$h\le2x$，并只使用已经成立的原实际母窗口。固定其中一个 $Q$ 与同一个 $w\in W$，令
$$
u=u_{w,Q}=(P_{V_Q}-P_{K_Q})w,\qquad W_0=\|w\|.
$$
原总尾孔数记为 $\mathcal N$，从 $x$ 起的远孔数记为 $\mathcal N_>$。父稿给
$$
\mathcal N_>\le\mathcal N\le\mathcal N_>+R,\qquad
\|u\|\le W_0,\qquad u\perp K_Q,
$$
$$
\|u-P_{\mathcal N\le Q}w\|\le2\eta_mW_0,\qquad
\eta_m=e^{-6d^4}.
\tag{1.2}
$$
以下不改变 $u$，也不在不同切口重选来源。写 $u_j=P_{\mathcal N_>=j}u$。在 $j+R<Q$ 时有
$$
Cu_j+Du_{j+1}=0.
\tag{1.3}
$$

对每个
$$
n\ge h,\qquad n+h+R<Q
\tag{1.4}
$$
取原左最小列 $U_n$、完整与裸右最小列 $J_{f,n},J_{b,n}$，以及
$$
r_n=Cu_n,\quad U_nr_n=u_{\le n},\quad
L_n=U_n^*U_n,\quad H_n=J_{f,n}^*J_{f,n},\quad B_n=J_{b,n}^*J_{b,n}.
$$
右栈始终保留 $h$ 段，令
$$
Y_n=(u_{n+1},\ldots,u_{n+h}),\qquad
\mathcal R_n=J_{f,n}-J_{b,n},\qquad
\mathcal R_n^*\mathcal R_n=H_n-B_n.
\tag{1.5}
$$
$\mathcal R_n$ 落在完整返回空间
$\mathscr E_{0,n}=\mathscr E_n\ominus Z_{f,n}$，其中
$\mathscr E_n=\mathscr W_n^{\rm hi}\oplus^\perp Z_{b,n}$。
真实裸最小列满足 $J_{b,n}\perp\mathscr E_n$。这些空间保全部高旗、裸零源和完整零源。

固定 $m,R,n$ 时，源空间是有限头 Jordan 相似下有限个闭尾核的直和，因而闭；原固定孔层的真右逆给 $U_n,J_{f,n},J_{b,n}$ 的有界性。这里只使用该存在性，不使用 Jordan 条件数或宣称其逆一致有界。原 $D$ 本身由 $\sum b_i<\infty$ 在全物理空间有界。

令 $i_0$ 为强头到远真空的等距嵌入。对头 forcing $g$ 定义同切口的完整最小源
$$
s_{f,n}[g]=(L_n+H_n)^{-1}U_n^*i_0g.
\tag{1.6}
$$
其真正物理核增量为
$$
\mathcal T_{f,n}s_{f,n}[g]
=(P_{\mathscr K_{n+h}^C}-P_{\mathscr K_n^C})i_0g,\qquad
\mathcal T_{f,n}s=(U_ns,-J_{f,n}s).
\tag{1.7}
$$
其中 $\mathscr K_j^C=\ker(C+D)\cap\{\mathcal N_>\le j\}$。完整投影还含共同左零源 $P_{\mathscr K_n^C}i_0g$；(1.7) 没有把它删后冒充完整投影。

## 2. 完整匹配 resolvent 与实际修正的正预算

本节暂省下标 $n$。置
$$
S_b=L+B,\quad S_f=L+H,\quad E=H-B,\quad
\mathcal P=S_f^{-1}E=I-S_f^{-1}S_b.
\tag{2.1}
$$
真正匹配配对准确为
$$
\boxed{
\langle E r,s_f[g]\rangle
=\langle U\mathcal P r,i_0g\rangle.
}
\tag{2.2}
$$
这是原算子次序的恒等式，不需要互换任何压缩与逆。

$\mathcal P$ 在 $S_b$ 内积中是自伴正收缩，因为
$$
S_b\mathcal P=S_b-S_bS_f^{-1}S_b,\qquad
0\preceq S_b\mathcal P\preceq S_b.
\tag{2.3}
$$
下面的 $S_f$ 范数界另由物理核投影证明，并非把 (2.3) 的度量任意替换。

对实际 $r=r_n$，令
$$
a_n=r_n-\mathcal P r_n=S_f^{-1}S_b r_n,\qquad
\widetilde v_n=U\mathcal P r_n=u_{\le n}-Ua_n.
$$
我们有更精确的预算
$$
\boxed{
\|a_n\|_{S_f}^2
\le\|Y_n\|^2-\alpha_n(r_n)^2
\le\|Y_n\|^2,\qquad
\alpha_n(r)^2=\langle B_nr,r\rangle.
}
\tag{2.4}
$$

证明如下。写 $\mathcal T_b r=(Ur,-J_br)$。完整短核
$\mathscr K_{n+h}^C$ 正交分解为左零源、完整右零源及
$\operatorname{Ran}\mathcal T_f$。$\mathcal T_b r$ 正交于前两者；又
$J_b^*J_f=B$，故
$$
P_{\mathscr K_{n+h}^C}\mathcal T_b r
=\mathcal T_f S_f^{-1}S_b r=\mathcal T_f a_n.
$$
由 $\mathscr K_{n+h}^C\subset K_Q$、$u\perp K_Q$ 及
$$
u_{\le n+h}=\mathcal T_b r+(0,Y_n+J_br)
$$
得到
$$
\mathcal T_f a_n
=-P_{\mathscr K_{n+h}^C}(0,Y_n+J_br).
$$
原实际裸候选为 $-P^{\rm lo}Y_n$，与 $J_br$ 同源。最小性遂给
$\langle Y_n,J_br\rangle=-\|J_br\|^2$，因而
$$
\|Y_n+J_br\|^2=\|Y_n\|^2-\alpha_n(r)^2.
$$
取投影收缩即得 (2.4)。这里 $Y_n$ 本身无需满足完整右头旗，全部高返回没有被零置。

## 3. 第一远孔读数支付完整头 Gram

定义原完整 bosonic 头 Gram
$$
\mathsf H=H_C(S)=
\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{j!S^j}.
\tag{3.1}
$$
对任意原左可行 $v\in\mathscr V_n^C$、$n\ge h$，令
$$
\beta(v)=S^{-1/2}Dv_1
$$
并将远真空输出识别为头向量。真实低行递推给
$$
\langle v,i_0C^*t\rangle
=\langle Cv_0,t\rangle
=-\sqrt S\,\langle\beta(v),t\rangle,
\tag{3.2}
$$
以及对 $0\le j<h$，
$$
C^j\beta(v)=(-1)^jS^{-1/2}D^{j+1}v_{j+1}.
\tag{3.3}
$$
$n\ge h$ 正是使用这些低行的充分门，不能仅由 $n\ge1$ 读出全部 (3.3)。

置
$$
\omega_k=(D^*)^k\Omega,\qquad
\sigma_k^2=\|\omega_k\|^2=(k!)^2e_k(b^2),\qquad
I_kt=t\otimes\omega_k/\sigma_k .
$$
这些是真实连续硬核尾的 coherent 列。$I_k$ 是等距，且在第 $k$ 远孔层上
$D^k=\sigma_k I_k^*$。由 $k!e_k(b^2)\le S^k$ 得
$$
\begin{aligned}
\|\mathsf H^{1/2}\beta(v)\|^2
&=\sum_{k=1}^{h}
 \frac{\sigma_k^2}{(k-1)!S^k}\|I_k^*v_k\|^2\\
&\le\sum_{k=1}^{h}k\|v_k\|^2.
\end{aligned}
\tag{3.4}
$$
因此这是完整 $\mathsf H$ 的实际读数预算，不是单个 coherent 方向的逆上界，也没有用 primitive Gram 代整层逆。

令
$$
A_w=\|P_{1\le\mathcal N_>\le h}u\|.
$$
将 (2.4) 代入 $\widetilde v_n$ 的低层平方和，得到
$$
\|\mathsf H^{1/2}\beta(\widetilde v_n)\|
\le\sqrt h\,[A_w+\|Y_n\|].
$$
于是 (2.2)、(3.2) 给
$$
\boxed{
|\langle E_nr_n,s_{f,n}[C^*t]\rangle|
\le\sqrt{hS}\,\|\mathsf H^{-1/2}t\|
       [A_w+\|Y_n\|].
}
\tag{3.5}
$$
这是一个保实际完整源的白化 $C^*$ 恢复界。若 forcing 为
$C^*t+g_{\rm ker}$、$Cg_{\rm ker}=0$，则
$i_0g_{\rm ker}\in\mathscr K_n^C$，而
$\widetilde v_n\in\operatorname{Ran}U_n\perp\mathscr K_n^C$，故核分量在 (2.2) 中准确消失。对任意给定 $g$，本稿不据此假设其最小 $C^*$ 原像有小范数。

## 4. 原 native 平均首反馈具有所需的白化原像

固定同一个头 forcing $g$，在选取任何切口之前，定义
$$
a=\mathsf H^{-1}g,\quad
\mathfrak F_1=\sum_{j=1}^{h-1}
 j\,\frac{\|C^ja\|^2}{S^jj!},\quad
\Delta=\|i_0g-u_{g,Q}\|.
$$
要求原低 forcing 门 $Q\ge R+h+2$。父稿的完整源结论为
$$
\mathfrak F_1\le(h-1)\Delta^2.
\tag{4.1}
$$

对每个 $i\ge x$，置
$$
s_i=S-z_i,\quad p_i=z_i/S,\quad H_i=H_C(s_i).
$$
$(a_{0,i},a_{1,i})$ 是该位并头后完整 Gram
$H_{C+b_iE_i}(s_i)$ 对 forcing $(g,0)$ 的真正最小源。其第一行准确为
$$
g=H_i a_{0,i}+\alpha_i,\qquad
\alpha_i=\frac{b_i}{s_i}C^*H_i a_{1,i}.
\tag{4.2}
$$
保 $C^*H_i$ 次序，不改作 $H_iC^*$，也不以候选源替代最小源。

完整 native Schur 已付
$$
\mathsf H\preceq H_i\preceq e^8\mathsf H,\qquad
x_i=H_i^{1/2}a_{1,i},\qquad
\sum_i\|x_i\|^2\le e^8\mathfrak F_1.
\tag{4.3}
$$
原尾积分还给
$$
S\ge\frac1{3(x+1)^3},\quad
z_{\max}=(x+1)^{-4},\quad
p_{\max}\le\frac3{x+1}<\frac12,\quad s_i\ge S/2.
\tag{4.4}
$$
取同一个概率权 $p_i$，定义
$$
\boxed{
\bar t=\sum_i p_i\frac{b_i}{s_i}H_i a_{1,i},\qquad
\bar\alpha=C^*\bar t=\sum_i p_i\alpha_i,\qquad
\bar g_0=\sum_i p_iH_i a_{0,i}=g-\bar\alpha.
}
\tag{4.5}
$$
这些源都不依赖切口 $n$。

令 $c_i=p_i b_i/s_i$。由
$\sum_i z_i^3\le z_{\max}^2 S$，
$$
\sum_i c_i^2
=\sum_i\frac{z_i^3}{S^2s_i^2}
\le\frac{4z_{\max}^2}{S^3}.
$$
又 $\|\mathsf H^{-1/2}H_i^{1/2}\|\le e^4$。在共同白化源内用 Cauchy，得到
$$
\boxed{
\|\mathsf H^{-1/2}\bar t\|
\le 2e^8\,\frac{z_{\max}}{S^{3/2}}\sqrt{\mathfrak F_1}.
}
\tag{4.6}
$$
同一估计的范数和版本证明 (4.5) 绝对收敛。固定参数时头空间有限，后接 $C^*$ 或 $\mathsf H^{1/2}$ 不改变收敛；不需要对这些环境范数作一致估计。

将 (4.6) 送入 (3.5)，再用 $z_{\max}/S\le3/(x+1)$，得到完整主交叉中的实际界
$$
\boxed{
\begin{aligned}
|\langle(H_n-B_n)r_n,s_{f,n}[\bar\alpha]\rangle|
&\le\frac{6e^8}{x+1}\sqrt{h\mathfrak F_1}
       [A_w+\|Y_n\|]\\
&\le12e^8\Delta[A_w+\|Y_n\|].
\end{aligned}}
\tag{4.7}
$$
第二行只用 $h\le2x$ 和 (4.1)。与只将反馈投到相邻 $U$ 的创建行不同，(4.7) 已包含匹配完整源的左零源及核输入反馈。

后面还需一个同源界。令
$T=\mathsf H^{1/2}C\mathsf H^{-1/2}/\sqrt S$。
原单 mode 等距核列的最高占据 $h-1$ 给
$\|T\|^2\le h-1$。因此
$$
\boxed{
\|\mathsf H^{-1/2}\bar\alpha\|
=\sqrt S\,\|T^*\mathsf H^{-1/2}\bar t\|
\le12e^8\Delta.
}
\tag{4.8}
$$

## 5. 同一源对全部切口的平均及原物理尾

取整数 $n_0\ge h$，令
$$
\mathcal I=\{n:n_0\le n\le Q-R-h-1\},\qquad
N_{\rm cut}=|\mathcal I|>0,\qquad
\beta_w=\|P_{\mathcal N_> >n_0}u\|.
$$
每一远孔层在所有未来带 $Y_n$ 中至多出现 $h$ 次，故
$$
\sum_{n\in\mathcal I}\|Y_n\|^2\le h\beta_w^2.
$$
(4.7) 遂给
$$
\boxed{
\frac1{N_{\rm cut}}\sum_{n\in\mathcal I}
|\langle(H_n-B_n)r_n,s_{f,n}[\bar\alpha]\rangle|
\le12e^8\Delta
 \left[A_w+\sqrt{\frac h{N_{\rm cut}}}\,\beta_w\right].
}
\tag{5.1}
$$
先固定 $m,R,Q,g$ 及 (4.5) 的完整源，再对全部 $n$ 使用同一来源；没有为每个切口选一个较便宜的 $g$ 或 $a_{1,i}$。

令 $P_x$ 为原 $\ell^2(\mathbb N_0)$ 的强头、远真空投影，
$\tau_x=\|(I-P_x)w\|$。原 N/Y 物理表示中 $P_x\to I$ 强收敛。
由 (1.2) 及两个孔数的包含，
$$
A_w\le\tau_x+2\eta_mW_0,\qquad
\beta_w\le
\|\mathbf1_{\{\mathcal N_{\rm all}>n_0\}}w\|+2\eta_mW_0.
\tag{5.2}
$$
因此在同一合法母窗口中，若 $m,x,n_0\to\infty$、
$h/N_{\rm cut}$ 有界，且 forcing 族 $\|g\|$ 有界，则
(5.1) 趋零。这里 $\Delta\le\|g\|$，无需给 $\tau_x$ 或原物理孔尾任何速率。可以取固定有限物理测试在足够大强头中的同一嵌入，也可以取原有界强头逼近族；二者均须先按 (4.5) 重建同一完整源。本结论不把 N/Y 的这个物理表示自动移到另一 Haar 张量积参考。

## 6. 真正帽逆伴随及全部裸端误差

本节另要求已付 Riordan 参数及其完整环境范数界
$$
\|K_{n,\rm amb}\|,\ \|K_{n,\rm amb}^{-1}\|
\le\mathcal C_0,\qquad
\mathcal C_0=\exp[32(1+e^{1070})],
$$
并把切口上界收紧为
$$
\mathcal I_{\rm hat}
=\{n:n_0\le n\le Q-R-2h-1\},\qquad
N_{\rm cut}=|\mathcal I_{\rm hat}|>0.
\tag{6.1}
$$
不把 Riordan 常数用于未满足其父稿尺度的任意 $R$。

定义实际完整返回测试及其真正运输
$$
z_{\alpha,n}=\mathcal R_ns_{f,n}[\bar\alpha]\in\mathscr E_{0,n},
\qquad
\widehat z_{\alpha,n}
=P_{\widehat{\mathscr E}_n}K_{n,\rm amb}^{-*}z_{\alpha,n}.
\tag{6.2}
$$
逆伴随后必须保外投影。它不被换成一个自由选择的帽最小源。父稿的完整混合身份给
$$
\begin{aligned}
&\langle\widehat{\mathcal R}_n(g_{\rm R}(C_{\rm s})r_n),
            \widehat z_{\alpha,n}\rangle
-\langle\mathcal R_nr_n,z_{\alpha,n}\rangle\\
&\hspace{35mm}
=\langle K_{n,\rm amb}J_{b,n}r_n,\widehat z_{\alpha,n}\rangle ,
\end{aligned}
\tag{6.3}
$$
其中 $g_{\rm R}(z)=\psi_m(z)/(d_0z)$ 是已付的归一 Riordan 源函数，不是本稿 forcing $g$。该误差绝对值不超过
$$
\mathcal C_0^2\alpha_n(r_n)
 \lambda_n(s_{f,n}[\bar\alpha]).
\tag{6.4}
$$

全部 matched 核增量仍保同一个 $i_0\bar\alpha$。由 (1.7) 及嵌套真核投影，
$$
\sum_{n\in\mathcal I_{\rm hat}}
 \lambda_n(s_{f,n}[\bar\alpha])^2
\le h\|P_{K_Q}i_0\bar\alpha\|^2.
$$
原 coherent forcing 的正确方向是
$i_0^*P_{K_Q}i_0\preceq\mathsf H^{-1}$。结合 (4.8) 得
$$
\sum_n\lambda_n(s_{f,n}[\bar\alpha])^2
\le h(12e^8\Delta)^2.
\tag{6.5}
$$
这来自真实投影增量的 Bessel 计数，不是环境完整右逆范数。另一方面
$\sum_n\alpha_n(r_n)^2\le h\beta_w^2$，故 (6.4) 的全部切口均值不超过
$12e^8\mathcal C_0^2\Delta(h/N_{\rm cut})\beta_w$。
最终
$$
\boxed{
\begin{aligned}
&\frac1{N_{\rm cut}}\sum_{n\in\mathcal I_{\rm hat}}
\left|
\langle\widehat{\mathcal R}_n(g_{\rm R}(C_{\rm s})r_n),
             \widehat z_{\alpha,n}\rangle
\right|\\
&\quad\le12e^8\Delta
\left[
 A_w+\sqrt{\frac h{N_{\rm cut}}}\,\beta_w
 +\mathcal C_0^2\frac h{N_{\rm cut}}\beta_w
\right].
\end{aligned}}
\tag{6.6}
$$
在 §5 的有界比例及原 Riordan 母窗口下，该均值亦趋零。所有完整右段、左右零源、两个部分端点和帽投影均未删去。

## 7. 真实剩余源与范围

令
$$
\mathfrak M_n(g)
=\langle(H_n-B_n)r_n,s_{f,n}[g]\rangle.
$$
第一源方程给准确分拆
$$
\boxed{
\mathfrak M_n(g)=
\mathfrak M_n(\bar g_0)+\mathfrak M_n(\bar\alpha).
}
\tag{7.1}
$$
本稿支付的是第二项及其 (6.2) 的真正帽运输。第一项
$\bar g_0=\sum_i p_iH_i a_{0,i}$ 仍含同一个完整 Schur 最小化；不能把它当原 $g$ 已付，也没有证明该映射为某个共同度量下的严格收缩。原非零锚及其 kernel-input 主反馈仍保在这一项中。

证明所用的无限位置和均先作有限和，再由 (4.3)--(4.6) 的绝对收敛或正平方和取极限。切口、头和右栈每次均有限；所有 $D^k$ 及 coherent 行属于原固定孔自然域。帽版只使用已经证明的有界环境正反映射，不把其形式交织升级为与任何 MP 逆或正交核投影的交换。新的改进限于指定原 native 平均反馈的完整 matched 返回，不宣称全普通右费、全部顺次 MP 或普通 ISP 已闭。
