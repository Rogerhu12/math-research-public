# R239 附录：完整线性核链与真实低核通量的合法测试

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；主会话全文复核原逐头 lift 与 R254 相容域，central_review 独立复核拼链和头预算。
状态：本文证明同旗最小原像、完整核拼合、支持、头右移成本和真实测试误差，并由直接补核消去最终误差中的未知原像范数；只剩 Schur 后非中央合成量尚未控制，尚未得到无权最小修复的新增长界。

## 1. 原模型及需要保留的源条件

固定原线性窗口
$$
m\ge5,\qquad d=2^m,\qquad 4d\le q\le e^{d^3/4},
\qquad L=A+D,\quad A=A_m,\quad D=D_m.
$$
$A^d=0$，$\|A\|\le6$。纯尾权为 $a_j=(j+1)^{-2}$，并记
$$
D_3=\sum_{j\ge m}a_j^3E_j,\qquad
S_m=\sum_{j\ge m}a_j^2,\qquad
s_{3,m}=\sum_{j\ge m}a_j^3\le(5m^5)^{-1}.
$$
$D,D_3$ 交换，二者与所有头矩阵交换。

令
$$
E_{s,p}=\ker D^s\cap\mathcal H_p^{(m)},\qquad E_{0,p}=0,
$$
并定义准确单层联合旗
$$
\mathcal E_p=\bigoplus_{j=0}^{d-1} e_j E_{d-j,p}.
\tag{1.1}
$$
由于真实有限头是正则幂零单链，
$$
\operatorname{Ran}A^k=\operatorname{span}\{e_0,\ldots,e_{d-k-1}\}.
$$
因此对 $u\in\mathbb C^d\otimes\mathcal H_p^{(m)}$，
$$
u\in\mathcal E_p
\quad\Longleftrightarrow\quad
D^ku\in\operatorname{Ran}A^k\otimes\mathcal H_{p-k}^{(m)}
\quad(0\le k\le d).
\tag{1.2}
$$
本稿用 (1.2) 检查每一次向下补核，不把任意纯核阶有限的向量都当作合法头旗源。

[R271 联合旗及真实通量](R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md) §§4–7 的最优对偶链记为 $z_t$，$1\le t\le d-1$，其低核通量含
$$
\langle H_tw_{q+t},P_{E_{t-1,q+t}}z_t\rangle,\qquad
H_t=P_{\langle e_0,\ldots,e_{d-t-1}\rangle}
A(I-P_{\langle e_0,\ldots,e_{d-t}\rangle}).
$$
令 $\mathcal P_p$ 为 (1.1) 的正交投影，置
$$
p_t=q+t,\qquad
h_t=\mathcal P_{p_t}H_t^*P_{E_{t-1,p_t}}z_t.
\tag{1.3}
$$
则 $h_1=0$，而 $2\le t\le d-1$ 时
$$
h_t\in\mathcal F_{t,p_t},\qquad
\mathcal F_{t,p}:=
\bigoplus_{j=d-t+1}^{d-1}e_jE_{d-j,p}
\subset\mathcal E_p\cap E_{t-1,p}.
\tag{1.4}
$$
这里 $H_t^*$ 先把头指标送到 $j\ge d-t+1$；再取联合旗投影不会增加尾核阶。
R271 的真实未来投影 $\widehat v\in V_{m,q+d}$ 给
$\|\widehat v-P_{\le q+d}w\|\le e^{-74d^4}\|w\|$，
因此把原通量改用 (1.3) 的代价至多
$$
6e^{-74d^4}\|w\|\left(\sum_t\|z_t\|^2\right)^{1/2}.
\tag{1.5}
$$
结合原 $\|z\|\le e^{2d^4}\lambda$，该误差已在旧 carry 预算内。
没有将 $H_tw$ 当成 $M$ 或 $W=M\ominus N$ 中的向量。

## 2. D3 的最小原像可以保住整条短纯核旗

[全尾双行 Hodge 稿](R271-appendix-full-tail-two-row-fixed-layer-range-and-contractive-known-images.md)
已经对每个固定孔层证明完整闭源
$$
D_3F_1-DF_2=0
$$
可解为 $(Du,D_3u)=(F_1,F_2)$，并给有限的有界线性构造。

由此归纳得到：对所有固定 $s\ge1,p\ge0$，
$$
D_3:E_{s,p+1}\longrightarrow E_{s,p}
\quad\text{有界满射。}
\tag{2.1}
$$
$s=1$ 是已有结论。若已知 $s-1$，给定 $h\in E_{s,p}$，
当 $p\ge1$ 时先线性选
$$
v\in E_{s-1,p},\qquad D_3v=Dh;
$$
$p=0$ 时取 $v=0$。双行源 $(v,h)$ 闭合，故存在有界线性选取的 $u$ 使
$$
Du=v,\qquad D_3u=h.
$$
于是 $D^su=D^{s-1}v=0$。每一步只使用固定层有界算子，故给 (2.1) 的有界右逆。以 $J^4D_3$ 缩放时，实际闭源是 $(v,J^4h)$；本论证没有漏掉这个缩放。
源和目标均为 Hilbert 闭子空间，因此 (2.1) 具有有界的真正最小范数右逆。

在有限头直和 (1.4) 上逐分量应用 (2.1)，得到
$$
D_3:\mathcal F_{t,p+1}\longrightarrow\mathcal F_{t,p}
$$
有界满射。记其真正最小右逆为 $\mathcal R^{(3)}_{t,p}$，并取
$$
u_t=\mathcal R^{(3)}_{t,p_t}h_t.
\tag{2.2}
$$
准确有
$$
u_t\in\mathcal F_{t,p_t+1},\qquad
D_3u_t=h_t,\qquad D^{t-1}u_t=0.
\tag{2.3}
$$
若另已知同旗原像 $f_t\in\mathcal F_{t,p_t+1}$ 满足 $D_3f_t=h_t$，则
$$
\boxed{
u_t=P_{\mathcal F_{t,p_t+1}\ominus
(\mathcal F_{t,p_t+1}\cap\ker D_3)}f_t,
\qquad \|u_t\|\le\|f_t\|.
}
\tag{2.4}
$$
这个收缩不要求分别估计环境逆范数。但 (1.3) 本身没有自动提供一个范数已付款的 $f_t$；Schur 逆后的源仍须单独核查这一点。

## 3. 一致头右移和两侧完整核拼合

使用 [R249](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) 的实际矩阵
$$
A=S_m(\vartheta_mJ_d)S_m^{-1},\qquad
\vartheta_m=e^{20-\mathcal L_m},\qquad
\mathcal L_m=\frac{25}{2}\frac{d^4}{d-2}.
$$
这里 $\vartheta_m$ 是头 Jordan 边权，不能与最小修复量 $\lambda$ 混同。
令 $\kappa_m=\|S_m\|\|S_m^{-1}\|$，并定义一致右移
$$
\mathcal J_m=S_m(\vartheta_m^{-1}J_d^*)S_m^{-1}.
\tag{3.1}
$$
它不是 $A$ 的 Moore--Penrose 逆。准确有
$$
\mathcal J_m^d=0,\quad
A\mathcal J_mx=x\ (x\in\operatorname{Ran}A),\quad
\mathcal J_m(\operatorname{Ran}A^{k+1})\subset\operatorname{Ran}A^k,
$$
以及
$$
\boxed{\|\mathcal J_m^k\|\le\kappa_m\vartheta_m^{-k}.}
\tag{3.2}
$$
本式完整支付 $\vartheta_m^{-k}$，没有只保留条件数。

使用 [R254 相容多次原像](R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)
§§1–3 的同一辅助头族：其 (1.5) 给相容性，(3.5) 给本稿 §4 所用的受限范数界。
原稿权为 $(j+2)^{-2}$，这里作 $j'=j-1$ 的整数重标就得到原物理权 $(j+1)^{-2}$；
这一重标也见[原线性全窗口逐步稿](../notes/2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md) §2。
具体取输入孔数上界 $q+d$、最大原像阶 $d-1$，故该原稿的 $Q=q+2d-1$、起始位参数为 $m-1$。
其常数不超过本稿 (4.2) 前的 $R_*$，全部输出覆盖于 $q+2d$。
由此选定同一相容族 $R_j$，$0\le j\le d-1$，满足
$$
R_0=I,\qquad DR_j=R_{j-1}.
$$
它们只作用尾，与头矩阵交换；不假定它们与 $D_3$ 交换。

现在更一般地，设
$$
u\in\mathcal E_n\cap E_{s,n},\qquad 1\le s\le d.
$$
定义单层完整延拓
$$
\begin{aligned}
\mathcal K_n(u)_n&=u,\\
\mathcal K_n(u)_{n-k}&=(-\mathcal J_m)^kD^ku
\quad(1\le k\le s-1),\\
\mathcal K_n(u)_{n+j}&=(-A)^jR_ju
\quad(1\le j\le d-1).
\end{aligned}
\tag{3.3}
$$
若层指标小于零，对应的 $D^ku$ 已经为零。

由 (1.2)，向下每一步应用 $A\mathcal J_m=I$ 都在真实 $\operatorname{Ran}A$ 上进行。
所以相邻低层严格满足
$$
A(-\mathcal J_m)^kD^ku+D(-\mathcal J_m)^{k-1}D^{k-1}u=0.
$$
最底层由 $D^su=0$ 封口。向上则由 $DR_j=R_{j-1}$ 逐项抵消，最顶层由 $A^d=0$ 封口。因此
$$
\boxed{L\mathcal K_n(u)=0.}
\tag{3.4}
$$
整个延拓只要求已写明的同层联合旗和短纯核条件。

对 (2.2) 取 $n=p_t+1=q+t+1$、$s=t-1$，记
$$
U_t=\mathcal K_{p_t+1}(u_t).
\tag{3.5}
$$
则
$$
\boxed{
LU_t=0,\qquad
\operatorname{supp}_{\rm holes}U_t
\subset[q+3,q+t+d],\qquad
P_{p_t}D_3U_t=h_t.
}
\tag{3.6}
$$
由于 $t\le d-1$，全部 $U_t$ 支持于 $[q+3,q+2d-1]$。
下端 $q+3$ 用的是 $D^{t-1}u_t=0$，不是粗 $D^du_t=0$。
相应的 $D_3U_t$ 全部支持于 $[q+2,q+2d-2]$，不会落到原低输出区 $\le q$。

## 4. 真实范数账本：下补及上补分开支付

R249 给
$$
\log\kappa_m\le\Psi_m
=\mathcal L_m(d-1)-\omega_{d-1}+d\log12+2\log d,
$$
$$
\omega_{d-1}
=\frac{20}{3}d^4-15d^3+(150m-275)d+\frac{850}{3}.
$$
对 $m\ge5$，这些准确式直接给 $\Psi_m\le7d^4$。

纯尾短核范数引理给
$$
\|D^ku\|^2\le(s-1)_kS_m^k\|u\|^2,\qquad
(s-1)_k=\frac{(s-1)!}{(s-1-k)!}.
$$
所以向下部分的平方范数至多
$$
\kappa_m^2\sum_{k=1}^{s-1}
\vartheta_m^{-2k}(s-1)_kS_m^k\,\|u\|^2.
\tag{4.1}
$$
各项位于不同孔层，不另加非正交求和损失。

向上用同一相容族的受限界。可取
$$
R_*=512\sqrt{q+2d+1}(m+q+2d+2)^{3/2}
\le2048q^2.
$$
因为 $u\in\mathcal E_n$，
$$
D^{d-j}A^ju=A^jD^{d-j}u=0,
$$
故对 $1\le j<d$，
$$
\|A^jR_ju\|=\|R_jA^ju\|
\le(2R_*)^{d-1}\|A^ju\|
\le6^j(2R_*)^{d-1}\|u\|.
\tag{4.2}
$$
这里利用的是 $A^ju$ 的实际纯核阶 $d-j$，没有每次重付输入阶 $s$。
由 $\log q\le d^3/4$，全部上补项的平方和开方不超过 $e^{d^4}\|u\|$。

在 (3.5) 中，$s-1=t-2\le d-3$。
使用 $S_m\le1$，(4.1) 开方的对数至多
$$
\Psi_m+(d-3)(\mathcal L_m-20)
+\tfrac12d\log d+\tfrac12\log d.
$$
其中 $(d-3)\mathcal L_m\le(25/2)d^4$。
连同中心项及 (4.2)，对全部 $m\ge5$ 可统一取
$$
\boxed{\|U_t\|\le e^{20d^4}\|u_t\|.}
\tag{4.3}
$$
这个界是可付 carry 的粗统一界；没有把它称为无权增长界。

## 5. 先入实际 M，再施真实尾理想

令
$$
X_{3,m}=\sum_{j\ge m}a_j^3N_j.
$$
两种原边界都满足 $X_{3,m}M\subset N$、
$\|X_{3,m}\|\le s_{3,m}$，且
$$
\|X_{3,m}-D_3\|
\le s_{3,m}e^{-770d^4}.
\tag{5.1}
$$
使用[原线性全窗口逐步稿](../notes/2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md)
§6 的原位号逐头提升：式 (6.6) 给下述误差，式 (6.7) 明确给出目标空间 $N$。
其适用条件为 $k\in\ker L_m\cap\mathcal H_{\le Q}^{(m)}$、$Q\le e^{d^3/3}$。
原证明先由每步误差与原孔次数上界得到极限属于
$M\cap\operatorname{Dom}e^{c\mathcal N}$（每个固定 $c>0$），
再取 $c=4$ 并使用既有的 $M\cap X_3\subseteq N$；没有循环使用新权饱和结论。
[正式全整数附录](R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md) §2 也完整列出这个映射。
这里取 $Q=q+2d\le e^{d^3/3}$，故 (3.6) 的完整 $L$ 核满足全部条件：
$$
\Lambda U_t\in N\subset M,\qquad
\|\Lambda U_t-U_t\|\le e^{-75d^4}\|U_t\|.
$$
因此
$$
n_t=X_{3,m}\Lambda U_t\in N
$$
是一个合法的真实测试向量，且由 (4.3)、(5.1)
$$
\boxed{
\|n_t-D_3U_t\|
\le 2s_{3,m}e^{-55d^4}\|u_t\|
\le e^{-54d^4}\|u_t\|.
}
\tag{5.2}
$$
这一步使用完整 $U_t$ 的核归属。它没有把单层最小原像 $u_t$ 本身宣称为 $M$ 中的向量。

若 $w\in W=M\ominus N$，则
$$
|\langle w,D_3U_t\rangle|
\le e^{-54d^4}\|w\|\|u_t\|.
\tag{5.3}
$$
因此 (2.4) 的已知像收缩确实可以放进一个合法 $M$ 测试，而非只停留在环境原像上。

## 6. 非中央项的完整公式：Rt 不与 D3 交换

定义非中央各层项之和
$$
C_t(u_t)=D_3U_t-h_t
$$
（$h_t$ 放在其原孔层 $p_t$）。
由 (3.3)，它准确等于
$$
\boxed{
\begin{aligned}
C_t(u_t)={}&
\sum_{k=1}^{t-2}
(-\mathcal J_m)^kD^kh_t
\quad\text{分别放在孔层 }p_t-k\\
&+\sum_{j=1}^{d-1}
(-A)^jD_3R_ju_t
\quad\text{分别放在孔层 }p_t+j.
\end{aligned}}
\tag{6.1}
$$
低侧可用 $D_3D^k=D^kD_3$ 及头交换，把它完全写成 $h_t$。
高侧的 $D_3R_j$ 原样保留，不能换成 $R_jD_3$。
所有非中央项仍在 $[q+2,q+2d-2]$。

另可准确定位交换误差。对中心源 $h_t$ 本身使用 (3.3)，则
$$
D_3U_t-\mathcal K_{p_t}(h_t)
=\sum_{j=1}^{d-1}(-A)^j[D_3,R_j]u_t=:Z_t.
\tag{6.2}
$$
由于 $D[D_3,R_j]=[D_3,R_{j-1}]$ 且 $[D_3,R_0]=0$，
也可直接检查
$$
LZ_t=0,\qquad
\operatorname{supp}_{\rm holes}Z_t\subset[p_t+1,p_t+d-1].
\tag{6.3}
$$
所以交换误差是一个明确的完整高尾零源核，而不是零算子。
若需要在真实 $W$ 配对中消去它，仍须用 (6.3) 和其范数调用实际 lift；不能无代价声称 $R_j$ 保持 $D_3$ 已知像。
这里 $Z_t$ 可以超出原宽度 $d$ 的修复空间；不能仅由原宽度的最小性声称它与旧 $c^{\min}$ 正交。
例如由 (4.3) 对 $u_t,h_t$ 的两次应用，
$\|Z_t\|\le2s_{3,m}e^{20d^4}\|u_t\|$，其 lift 误差仍在 (5.2) 同一量级内。

## 7. 剩余量已变为真实未来层上的一个合成向量

由 (5.3)、(6.1)，
$$
\boxed{
\langle w_{p_t},h_t\rangle
=-\langle w,C_t(u_t)\rangle+\epsilon_t,\qquad
|\epsilon_t|\le e^{-54d^4}\|w\|\|u_t\|.
}
\tag{7.1}
$$
对全部 $2\le t<d$ 相加，定义
$$
C_{\rm tot}=\sum_{t=2}^{d-1}C_t(u_t),\qquad
U_{\rm src}^2=\sum_{t=2}^{d-1}\|u_t\|^2.
$$
不同 $t$ 的非中央项可能落在同一孔层；这里保留实际向量和，不先按范数相加丢掉相消。
令
$$
\beta_q=\|w_{[q+2,q+2d-2]}\|.
$$
则
$$
\boxed{
\left|\sum_t\langle w_{p_t},h_t\rangle\right|
\le \beta_q\|C_{\rm tot}\|
+e^{-53d^4}\|w\|U_{\rm src}.
}
\tag{7.2}
$$
若有同旗已知像 $f_t$，(2.4) 只对 $U_{\rm src}$ 给
$U_{\rm src}^2\le\sum_t\|f_t\|^2$。它不自动给 $\|C_{\rm tot}\|$ 的小界。

### 7.1 直接补核消去原像范数的误差项

对 $h_t$ 自身使用 (3.3)，仍取短核阶 $s=t-1$。于是
$$
K_t:=\mathcal K_{p_t}(h_t)\in\ker L,\qquad
\operatorname{supp}_{\rm holes}K_t
\subset[q+2,q+t+d-1],
$$
$$
\|K_t\|\le e^{20d^4}\|h_t\|.
\tag{7.3}
$$
这不是对 $D_3$ 原像另加假设：$h_t\in\mathcal F_{t,p_t}$ 已由 (1.3)–(1.4) 确定。
其上端不超过 $q+2d-2$，故 §5 的原逐头 lift 直接适用。
对实际 $w\in W$，得到
$$
|\langle w,K_t\rangle|
\le e^{-55d^4}\|w\|\,\|h_t\|.
\tag{7.4}
$$

定义只依赖实际 Schur 链的合成向量
$$
\widetilde C_{\rm tot}
=\sum_{t=2}^{d-1}\bigl(\mathcal K_{p_t}(h_t)-h_t\bigr).
\tag{7.5}
$$
完整公式为
$$
\boxed{
\widetilde C_{\rm tot}
=\sum_{t=2}^{d-1}\left[
\sum_{k=1}^{t-2}(-\mathcal J_m)^kD^kh_t
+\sum_{j=1}^{d-1}(-A)^jR_jh_t
\right],
}
\tag{7.6}
$$
其中第一重内项放在孔层 $p_t-k$，第二重内项放在孔层 $p_t+j$。
各项按真实孔层相加，不把可能的抵消预先丢掉。
由 (1.3) 和准确最优链预算，
$$
\left(\sum_t\|h_t\|^2\right)^{1/2}
\le6\|z\|\le6e^{2d^4}\lambda.
\tag{7.7}
$$
因此将 (7.4) 相加，$6\sqrt d\,e^{-53d^4}\le e^{-52d^4}$ 给
$$
\boxed{
\left|\sum_t\langle w_{p_t},h_t\rangle\right|
\le\beta_q\|\widetilde C_{\rm tot}\|
+e^{-52d^4}\|w\|\lambda.
}
\tag{7.8}
$$
所有未知 $D_3$ 原像范数已从这一最终误差项消去。

两种代表的准确关系是
$$
C_{\rm tot}=\widetilde C_{\rm tot}+\sum_t Z_t.
\tag{7.9}
$$
直接使用 (7.3)–(7.4) 并不需要先估计 $\sum_t Z_t$ 的范数。
(7.8) 中的 $R_jh_t$ 来自对 $h_t$ 重新做完整核拼合；
它不是把原 (6.1) 的 $D_3R_ju_t$ 无证明地交换成 $R_jD_3u_t$。

结合 R271 的真实正通量及 (1.5)，对充分大的实际非零缺陷窗口可写为
$$
\boxed{
\|v\|^2+\lambda^2
\le\beta_q\|\widetilde C_{\rm tot}\|
+e^{-51d^4}\|w\|\sqrt{\|v\|^2+\lambda^2}.
}
\tag{7.10}
$$
这里原 R271 通量误差、(1.5) 和 (7.8) 的误差均已包括。
因此当前只剩一个准确的 Schur 后合成量
$\widetilde C_{\rm tot}(h(z))$；不再另外保留可消去的 $U_{\rm src}$ carry 缺口。
若进一步取得足够小的真实预算
$\|\widetilde C_{\rm tot}\|\le K_q\lambda$，
才可从 (7.10) 得到新的最小修复增长控制。
同旗 $D_3$ 最小原像的收缩仍可用于寻找更便宜的合成代表，但不自动提供这个预算。
本稿没有取得该预算，也没有把 (4.3) 的 $e^{20d^4}$ 粗界当作 $q^{o(1)}$。

全文没有使用 $P_MR=RP_M$，没有声称单层纯核原像属于 $M$，
也没有将上补 $R_j$ 与 $D_3$ 交换。
