# R271 附录：完整最小修复链的降孔交换缺陷与真实源的 W 投影预算

日期：2026-11-13 UTC。作者：boundary_resume_1cf / Astra-ISP-1cf8c51d；根逐项复核同头窗口、端点支撑、Pythagoras、完整Gram、逆压缩Schur及实际M源。状态：本稿付清整个最小修复算子在真实缺陷投影后的降孔交换、完整源能量与低核真 Schur 度量的降孔收缩，以及真实降孔源的投影预算；它不证明无权完整修复能量增长界，不推出 $N=M$。

使用 [R271 联合旗与右逆](../results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md) 和 [R239 原线性全整数窗口](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md) 的同一实际模型。以下始终固定**同一个**头 $m$，不在相邻两个源层之间偷换 $m$。

## 1. 两个相邻源层与共同提升预算

令 $m\ge5$、$d=2^m$、$L=A_m+D_m$，其中
$$
D_m=\sum_{j\ge m}b_jE_j,\qquad b_j=(j+1)^{-2}.
$$
对 $T=T_N$ 或 $T_Y$，仍记
$$
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
$$
取整数 $q$ 满足
$$
\boxed{4d\le q,\qquad q+1\le e^{d^3/4}.}
\tag{1.1}
$$
所以 $q$ 与 $q+1$ 都在同一个 $m$ 的原窗口内。

记 $E_{h,p}=\ker(D_m^h|_{\mathcal H_p^{(m)}})$，非正核阶约定为空间 $\{0\}$；以下都采用实际物理头的正交基。
记真实源空间为
$$
\mathscr R_j
=\bigoplus_{i=0}^{d-2}e_i\otimes
\ker(D_m^{d-i-1}|_{\mathcal H_j^{(m)}}).
$$
令
$$
\mathcal R_j=F_j^*G_j^{-1}:\mathscr R_j\longrightarrow\mathcal H_-,
\qquad G_j=F_jF_j^*,
\tag{1.2}
$$
为原 Hilbert 范数中的真正最小修复算子。这里 $F_j$ 是完整联合旗链上的首输出，$G_j$ 是已经付清的准确源范围 Gram。于是
$$
L\mathcal R_jr=r,\qquad
\operatorname{supp}_{\rm hole}(\mathcal R_jr)
\subset[j+1,j+d],
$$
$$
\|\mathcal R_j\|\le\Gamma_j\le e^{d^4}
\qquad(j=q,q+1).
\tag{1.3}
$$
这些是整个算子界，不仅适用于一个给定残量。

本稿所需有限核向量的孔数至多 $q+d+1$。由 (1.1)，
$$
q+d+1\le e^{d^3/4}+d
\le2e^{d^3/4}\le e^{d^3/3},
\tag{1.4}
$$
最后一步只用 $\log2\le d^3/12$。故全部使用同一个已证提升
$$
\Lambda:\ker L\cap\mathcal H_{\le q+d+1}^{(m)}\longrightarrow N,
\qquad
\|\Lambda f-f\|\le\delta_m\|f\|,\quad
\delta_m=e^{-75d^4}.
$$
特别，
$$
\boxed{\|P_Wf\|\le\delta_m\|f\|
\quad(f\in\ker L,\ \operatorname{supp}_{\rm hole}f\subset[0,q+d+1]).}
\tag{1.5}
$$
不把 (1.5) 扩张到无限孔核。

## 2. 一次纯尾降孔与真实尾理想

可先取任意 $c=(c_j)_{j\ge m}\in\ell^1$，置
$$
C=\sum_{j\ge m}c_jE_j,\qquad
X=\sum_{j\ge m}c_jN_j,\qquad
s=\sum_{j\ge m}|c_j|,\qquad
\varepsilon=\sum_{j\ge m}|c_j|\eta_j.
\tag{2.1}
$$
$C$ 准确降低一个尾孔，并与 $A_m,D_m,L$ 交换。因为它与 $D_m$ 交换，
$$
C\mathscr R_{q+1}\subset\mathscr R_q.
\tag{2.2}
$$
以下 $C_{\mathscr R,q}$ 表示 (2.2) 的这个有界限制，范数至多 $s$。

两种边界共用 $N_j=d_j^{-1}B^{2^j}$，且 $B$ 保持 $M$，所以
$N_jM\subset BM$。由范数级数及 $N$ 闭，准确有 $XM\subset N$。
原矩阵界 $\|N_j-E_j\|\le\eta_j$ 还给
$$
\|C\|,\|X\|\le s,\qquad
\|C-X\|\le\varepsilon,\qquad
\boxed{\|P_WCP_M\|\le\varepsilon.}
\tag{2.3}
$$
这一步对正在研究 $T_Y$ 的情形同样使用 $N_j$，不是把辅助尾误换为 $Y_j$。定义与范数界见 [R202 §1–2](../results/R202-slow-boundary-finite-hole-degree-rigidity.md)、[R205 §1](../results/R205-cayley-boundary-degree-two-tail-sum-rigidity.md) 和 [R234 §2](../results/R234-slow-boundary-right-inverses-on-cubic-hole-degree-space.md)。

实际三次尾取
$$
C=D_{3,m},\qquad c_j=b_j^3,\qquad
s=s_{3,m}=\sum_{j\ge m}(j+1)^{-6}\le\frac1{5m^5}.
$$
这时
$$
\varepsilon\le s_{3,m}e^{-770d^4}.
\tag{2.4}
$$

## 3. 完整链交换缺陷准确是一个有限 L 核向量

定义
$$
\mathcal J_q
=C\mathcal R_{q+1}-\mathcal R_q C_{\mathscr R,q}
:\mathscr R_{q+1}\longrightarrow\mathcal H_-.
\tag{3.1}
$$
对任何 $r\in\mathscr R_{q+1}$，
$$
L(C\mathcal R_{q+1}r)=Cr
=L(\mathcal R_qCr),
$$
所以
$$
\boxed{L\mathcal J_qr=0.}
\tag{3.2}
$$
孔支撑两端也一致：
$$
\mathcal R_{q+1}r:\ [q+2,q+d+1]
\ \xrightarrow{\ C\ }\ [q+1,q+d],
$$
而 $\mathcal R_qCr$ 本来就在 $[q+1,q+d]$。因此
$$
\boxed{\operatorname{supp}_{\rm hole}(\mathcal J_qr)
\subset[q+1,q+d].}
\tag{3.3}
$$
没有留下第 $q$ 层或第 $q+d+1$ 层的额外端项。并且
$$
\|\mathcal J_q\|
\le s(\Gamma_q+\Gamma_{q+1}).
$$
用 (1.5) 得到
$$
\boxed{
\|P_W\mathcal J_q\|
\le\delta_m s(\Gamma_q+\Gamma_{q+1})
\le2s e^{-74d^4}.
}
\tag{3.4}
$$
这控制的是**整个** $F_j^*G_j^{-1}$ 的交换缺陷投影；它没有断言 $C$ 单独与 $G_j^{-1}$、某个 Schur 逆或某个低核投影交换。

准确的伴随版本为
$$
\boxed{
\|\mathcal R_{q+1}^*C^*P_W
-C_{\mathscr R,q}^*\mathcal R_q^*P_W\|
\le2s e^{-74d^4},
}
\tag{3.5}
$$
其中
$$
C_{\mathscr R,q}^*
=P_{\mathscr R_{q+1}}C^*|_{\mathscr R_q}.
\tag{3.6}
$$
必须保留 (3.6) 的真实源旗投影；不能把它直接写成环境 $C^*$。

### 3.1 同时保留真正的源能量收缩

$C\mathcal R_{q+1}r$ 是 $Cr$ 的同一个 $d$ 段可行修复；$\mathcal R_qCr$ 是这个闭仿射集的最小范数元。因此
$$
\mathcal R_qCr\perp\mathcal J_qr,
$$
并有准确的原 Hilbert 能量等式
$$
\boxed{
\|\mathcal J_qr\|^2
=\|C\mathcal R_{q+1}r\|^2-\|\mathcal R_qCr\|^2.
}
\tag{3.7}
$$
特别，
$$
\|\mathcal R_qCr\|\le s\|\mathcal R_{q+1}r\|,
\qquad
\|P_W\mathcal J_qr\|\le\delta_m\|\mathcal J_qr\|.
\tag{3.8}
$$
所以已知源还可以使用 (3.7)，不必一律换成全源 $\Gamma_j$ 上界。

将 $\|\mathcal R_jr\|^2=\langle G_j^{-1}r,r\rangle$ 代入，得到
$$
\boxed{
C_{\mathscr R,q}^*G_q^{-1}C_{\mathscr R,q}
\le s^2G_{q+1}^{-1}.
}
\tag{3.9}
$$
等价地，
$$
\boxed{
C_{\mathscr R,q}G_{q+1}C_{\mathscr R,q}^*
\le s^2G_q.
}
\tag{3.10}
$$
等价性只需对有界算子
$G_q^{-1/2}C_{\mathscr R,q}G_{q+1}^{1/2}$ 及其伴随取范数；不要求 $C_{\mathscr R,q}$ 可逆。这是一条准确 Gram 度量收缩，不是 Gram 与降孔可交换的断言。

### 3.2 内部完整 Gram 与低核通量的正确 Schur 度量

为明确允许通过的投影，复写同一内部链空间
$$
\mathscr C_{q,t}
=\bigoplus_{i=0}^{d-t}e_iE_{d-i,q+t},
\qquad
\mathscr Y_{q,t}
=\bigoplus_{i=0}^{d-t-1}e_iE_{d-i-1,q+t}.
$$
令 $\mathscr C_q=\bigoplus_{t=1}^d\mathscr C_{q,t}$、
$\mathscr Y_q=\bigoplus_{t=1}^{d-1}\mathscr Y_{q,t}$，并取
$$
S_qc=(Ac_t+Dc_{t+1})_{t=1}^{d-1},
\qquad \mathcal G_q=S_qS_q^*.
$$
所有算子仍在原物理正交基中。旧同时右逆保证 $\mathcal G_q$ 有界且严格正。

$C$ 的逐段限制 $C_{\mathscr C,q}:\mathscr C_{q+1}\to\mathscr C_q$、
$C_{\mathscr Y,q}:\mathscr Y_{q+1}\to\mathscr Y_q$ 都有范数至多 $s$。因 $C$ 与 $A,D$ 交换，
$$
S_qC_{\mathscr C,q}
=C_{\mathscr Y,q}S_{q+1}.
$$
故直接在实际链中计算
$$
\boxed{
C_{\mathscr Y,q}\mathcal G_{q+1}C_{\mathscr Y,q}^*
=S_qC_{\mathscr C,q}C_{\mathscr C,q}^*S_q^*
\le s^2\mathcal G_q.
}
\tag{3.11}
$$
与 (3.9)–(3.10) 同样取范数，等价得到
$$
C_{\mathscr Y,q}^*\mathcal G_q^{-1}C_{\mathscr Y,q}
\le s^2\mathcal G_{q+1}^{-1}.
\tag{3.12}
$$
内部最小右逆的交换差只自动属于 $\ker S_q$，不一定属于 $\ker L$；不能把 (3.4) 的真实 $W$ 投影预算直接套给这个内部交换差。

现在取 $a=1,2$，定义相对出生层不小于 $a$ 的闭子空间
$$
\mathscr Y_{a,q}
=
\bigoplus_{t=1}^{d-1}
\bigoplus_{i=0}^{d-t-1}
e_iE_{\min\{d-i-1,t-a+1\},q+t},
\tag{3.13}
$$
其中非正核阶约定为空间 $\{0\}$。按出生层 $s=p-h+1$、$p=q+t$，条件恰是 $s-q\ge a$。特别 $a=2$ 正是主通量所需的逐段 $\ker D^{t-1}$ 与原联合旗的交。

由 $CD=DC$，每个 $E_h$ 在降孔后保持相同核阶，所以
$$
C_{\mathscr Y,q}\mathscr Y_{a,q+1}\subset\mathscr Y_{a,q}.
$$
将此限制记为 $C_{a,q}$；并令 $P_{a,q}$ 为对应正交投影。定义
$$
\boxed{
\mathcal H_{a,q}
=
\left(P_{a,q}\mathcal G_q^{-1}|_{\mathscr Y_{a,q}}\right)^{-1}.
}
\tag{3.14}
$$
这个正算子是**消去整个低出生补空间**的 Schur 补：
若按 $\mathscr Y_{a,q}\oplus\mathscr Y_{a,q}^{\perp}$ 写
$\mathcal G_q=(G_{\mu\nu})$，则
$$
\mathcal H_{a,q}=G_{11}-G_{12}G_{22}^{-1}G_{21}.
$$
不把它换成 $G_{11}$ 的普通压缩。

将 (3.12) 的二次型准确限制到
$h\in\mathscr Y_{a,q+1}$；因 $Ch\in\mathscr Y_{a,q}$，左右的逆二次型分别就是 (3.14)。于是
$$
\boxed{
C_{a,q}^*\mathcal H_{a,q}^{-1}C_{a,q}
\le s^2\mathcal H_{a,q+1}^{-1},
\qquad
C_{a,q}\mathcal H_{a,q+1}C_{a,q}^*
\le s^2\mathcal H_{a,q}.
}
\tag{3.15}
$$
这是降孔通过真实低核 Schur 度量的已付范围。它没有交换 $P_{a,q}$ 与 $C$，而是使用 $C$ 对该子空间的准确不变性，再限制完整逆能量。

由于 $\mathscr Y_{2,q}\subset\mathscr Y_{1,q}$，Schur 结合律还给
$$
\mathcal H_{2,q}^{-1}
=
P_{2,q}\mathcal H_{1,q}^{-1}|_{\mathscr Y_{2,q}}.
\tag{3.16}
$$
所以先消去出生层 $\le q$、再消去出生层 $q+1$，与一次消去全部 $\le q+1$ 完全一致；(3.15) 不额外累乘 $\Gamma_q$。

旧两桥表达式先消去高出生块，用到的是高块的普通压缩及不同顺序的 Schur 补。不能据 (3.15) 把那个高块压缩免费换为 $\mathcal H_{2,q}$。若改用这里的消元顺序，仍须核对消元后的真实有效源是否是 (3.15) 可用的 $C$ 像；本节尚未证明这一点。


## 4. 来自真实 M 向量的降孔源预算

取任意 $u\in M$。令 $v=v_{m,q+1}(u)$ 为旧低输出正交投影，置
$$
r=r_{m,q+1}(u)=Lv=A_mv_{q+1}.
$$
则
$$
v\in\mathscr V_{m,q+1},\quad
r\in\mathscr R_{q+1},\quad
\|v\|\le\|u\|,\quad \|r\|\le6\|u\|,
$$
$$
\|v-P_{\le q+1}^{(m)}u\|\le e^{-74d^4}\|u\|.
\tag{4.1}
$$
因为 $C$ 降一孔并与 $L$ 交换，
$$
Cv\in\mathscr V_{m,q},\qquad L(Cv)=Cr.
\tag{4.2}
$$
所以 $h=Cr$ 是一个有明确低输出来源的真实源；不是任意环境源。

直接比较同源向量
$$
k=Cv-\mathcal R_qCr.
$$
由 (4.2)，$Lk=0$，孔支撑至多 $q+d$，且
$$
\|k\|\le s(1+6\Gamma_q)\|u\|.
\tag{4.3}
$$
定义原尾孔尾范数
$$
\tau_{q+1}^{(m)}(u)=\|P_{>q+1}^{(m)}u\|.
$$
由 (2.3)、(4.1)，
$$
\|P_WCv\|
\le s\tau_{q+1}^{(m)}(u)
+\bigl(\varepsilon+s e^{-74d^4}\bigr)\|u\|.
$$
再对 $k$ 用 (1.5)，得到完整预算
$$
\boxed{
\begin{aligned}
\|P_W\mathcal R_q C r_{m,q+1}(u)\|
&\le s\tau_{q+1}^{(m)}(u)\\
&\quad+
\left[\varepsilon+s e^{-74d^4}
+\delta_m s(1+6\Gamma_q)\right]\|u\|\\
&\le s\tau_{q+1}^{(m)}(u)
+\left[\varepsilon+8s e^{-74d^4}\right]\|u\|.
\end{aligned}
}
\tag{4.4}
$$
对实际三次尾尤其有
$$
\boxed{
\|P_W\mathcal R_q D_{3,m}r_{m,q+1}(u)\|
\le s_{3,m}\tau_{q+1}^{(m)}(u)
+9s_{3,m}e^{-74d^4}\|u\|.
}
\tag{4.5}
$$
尾孔数不超过原全部孔数，所以也可用原全部孔尾
$\tau_{q+1}(u)$ 替换右端。整个证明没有把某个最小逆与 $P_M$ 交换，也没有要求任一中间对偶链属于 $M$。

### 4.1 与实际 N 源的明确对应

由 $Xu\in N\subset M$，还可形成 $v_{m,q}(Xu)$。纯降孔恒等式
$CP_{\le q+1}^{(m)}=P_{\le q}^{(m)}C$ 给
$$
\|Cv_{m,q+1}(u)-v_{m,q}(Xu)\|
\le(2s e^{-74d^4}+\varepsilon)\|u\|.
$$
两者均在 $\mathscr V_{m,q}$，故顶部残量之差满足
$$
\boxed{
\|Cr_{m,q+1}(u)-r_{m,q}(Xu)\|
\le6(2s e^{-74d^4}+\varepsilon)\|u\|.
}
\tag{4.6}
$$
乘上真正最小修复 $\mathcal R_q$ 仍只付 $\Gamma_q\le e^{d^4}$：
$$
\|\mathcal R_qCr_{m,q+1}(u)-\mathcal R_qr_{m,q}(Xu)\|
\le6\Gamma_q(2s e^{-74d^4}+\varepsilon)\|u\|.
\tag{4.7}
$$
这识别了一个实际 $N$ 源的修复链，但没有假定所有 $N$ 源都已有小的完整修复能量。

## 5. 两次降孔的同头版本

若将 (1.1) 加强为 $q+2\le e^{d^3/4}$，则 $q+2$ 的同一右逆界仍有 $\Gamma_{q+2}\le e^{d^4}$，而
$q+d+2\le e^{d^3/4}+d\le e^{d^3/3}$ 重新付清全部提升域。全部论证可对
$C^2:\mathscr R_{q+2}\to\mathscr R_q$ 直接应用。两项的孔支撑仍同时为
$[q+1,q+d]$，因为
$$
[q+3,q+d+2]\xrightarrow{\ C^2\ }[q+1,q+d].
$$
其真实比较算子是 $X^2$，且
$$
X^2M\subset N,\quad
\|C^2\|,\|X^2\|\le s^2,\quad
\|C^2-X^2\|\le2s\varepsilon.
$$
因此
$$
\|P_W(C^2\mathcal R_{q+2}-\mathcal R_qC^2)\|
\le2s^2e^{-74d^4},
\tag{5.1}
$$
以及
$$
\boxed{
\|P_W\mathcal R_q C^2r_{m,q+2}(u)\|
\le s^2\tau_{q+2}^{(m)}(u)
+(2s\varepsilon+8s^2e^{-74d^4})\|u\|.
}
\tag{5.2}
$$
这里 $\mathcal R_qC^2$ 中的 $C^2$ 始终限制在 $\mathscr R_{q+2}$。

若需沿全部整数 $q\ge128$ 选头，可以统一选
$$
m=\max\!\left(5,\left\lceil
\frac{\log(4\log(q+4))}{3\log2}
\right\rceil\right)
$$
并对 $q,q+1,q+2$ 全部使用它。其 $d^3\ge4\log(q+4)$ 给上界；
$d\le\max\{32,2(4\log(q+4))^{1/3}\}$ 与
$2048\log(q+4)\le q^3$ 给 $4d\le q$。
最后这个标量不等式在 $q=128$ 成立，且 $q^3/\log(q+4)$ 在该范围递增。
因此没有因原自适应头在相邻整数处跳变而越界。

## 6. 仍需与真实两出生层桥逐项匹配

(4.5)、(5.2) 只控制修复向量的 $W$ 投影：
$$
\|P_W\mathcal R_q C^\ell r\|.
$$
它们没有给 $\|\mathcal R_q C^\ell r\|$ 的相同界，因而还不是无权最小能量增长定理。

旧出生层上升桥实际含受限 $D_{3,m}^*$；两桥之间还有真实 Schur 逆及低核投影。不能仅因出现两次 $D_3$ 就把该复合算子改成这里的 $(D_3^*)^2$，也不能只将 (3.5) 中整个最小修复算子拆出一部分来使用。下一缺口是证明那条完整复合链在真实源上能化为本稿可付的整体交换项，或另行控制其余项。无权 $N=M$ 与普通 ISP 继续开放。

## 7. 新消元顺序的准确有效源及 Schur 能量定位

本节继续固定同一个 $m,q$，采用本稿 §3.2 的内部完整 Gram
$\mathcal G=SS^*$ 以及 $a=2$ 的正确 Schur 补 $\mathcal H_{2,q}$。
本节逐项匹配[原出生层两带与两桥稿](../notes/2026-11-13-low-kernel-birth-layer-double-schur-bridge-1cf.md)的真实源；新增的是低出生层先消元的明确源公式与末块能量定位。它没有给有效源一个已付成本的 $D_3$ 原像，也不把旧能量恒等式的代数推论重新计为独立进展。

### A. 先消去低出生层的准确源

按相对出生层分成
$$
\mathscr Y=\mathscr Y_0\oplus\mathscr Y_1\oplus\mathscr Y_2,
$$
其中三块依次为 $s-q\le0$、$s-q=1$、$s-q\ge2$。
末块正是本稿的 $\mathscr Y_{2,q}$。

旧出生层两带关系使内部 Gram 准确三对角：
$$
\mathcal G=
\begin{pmatrix}
B_0&V_1^*&0\\
V_1&B_1&V_2^*\\
0&V_2&B_2
\end{pmatrix}.
\tag{A.1}
$$
对真正最小修复，置
$$
y=G_q^{-1}r,\qquad b=P_{\mathscr C_q}D_0^*y,\qquad
g=Sb,\qquad z=\mathcal G^{-1}g.
$$
纯 $D^*$ 把每个正交高度 $U_h$ 送入 $U_{h+1}\oplus U_{h+2}$。源 $y$ 的高度至少为1，所以 $D^*y$ 的高度至少为2；联合旗投影保留正交高度，$b$ 也只有第一段。故 $g=Sb=(Ab_1,0,\ldots,0)$；头 $A$ 保持尾高度，第一段的相对出生层是 $2-h\le0$。因此 $g=(g_0,0,0)$，不是任意假定的特殊右端。

定义
$$
Q_1=B_1-V_1B_0^{-1}V_1^*,\qquad
\zeta=V_1B_0^{-1}g_0,
$$
$$
\boxed{
\mathcal H_{2,q}=B_2-V_2Q_1^{-1}V_2^*,\qquad
\sigma=V_2Q_1^{-1}\zeta.
}
\tag{A.2}
$$
所有逆都存在，来自 $\mathcal G$ 的严格正下界和 Schur 正性。
先消去第零块，再消去第一块，准确给
$$
\boxed{z_2=\mathcal H_{2,q}^{-1}\sigma.}
\tag{A.3}
$$
特别，(A.2) 的 $\mathcal H_{2,q}$ 确实等于
$[P_{2,q}\mathcal G^{-1}|_{\mathscr Y_{2,q}}]^{-1}$，
不是旧先消高块顺序中的普通高块压缩 $B_2$。

同一块消元给原 Hilbert 正能量的准确分解
$$
\begin{aligned}
\langle\mathcal G^{-1}g,g\rangle
&=\langle B_0^{-1}g_0,g_0\rangle
+\langle Q_1^{-1}\zeta,\zeta\rangle\\
&\quad+\langle\mathcal H_{2,q}^{-1}\sigma,\sigma\rangle.
\end{aligned}
\tag{A.4}
$$
又因 $b=c^{\min}+S^*z$ 是正交分解，
$$
\langle\mathcal G^{-1}g,g\rangle=\|b\|^2-\lambda^2,
\qquad \lambda=\|c^{\min}\|.
$$
记
$$
\mathcal E_2=\langle\mathcal H_{2,q}^{-1}\sigma,\sigma\rangle.
$$
则
$$
\boxed{0\le\mathcal E_2\le\|b\|^2-\lambda^2.}
\tag{A.5}
$$

### B. 真通量在同一个 Schur 度量中有低成本测试

现在取 $w\in W$。使用 R271 联合旗稿 §5 已证的稍宽低投影
$$
\widehat v=P_{\mathscr V_{m,q+d}}w,\qquad
\|\widehat v-P_{\le q+d}^{(m)}w\|
\le e^{-74d^4}\|w\|.
\tag{B.1}
$$
该旧证明重新支付了放大后的 $R$，并没有要求把 $q+d$ 当成另一个满足 $q+d\le e^{d^3/4}$ 的原窗口。

令
$$
u_t=P_{W_{d-t+1}}\widehat v_{q+t},\quad 1\le t\le d,
\qquad
F_t=H_t\widehat v_{q+t},\quad1\le t\le d-1,
$$
其中 $H_t=P_{W_{d-t}}A(I-P_{W_{d-t+1}})$。
逐头关系 $D^{d-i}\widehat v_i=0$ 保证 $u\in\mathscr C_q$；
$H_t$ 只读取 $j\ge d-t+1$ 的坐标，故
$$
F_t\in\ker D^{t-1}\cap\mathscr Y_{q,t},
\qquad F\in\mathscr Y_{2,q}.
$$
对内部第 $t$ 段，$q+t\le q+d-1$，低输出方程准确为零。
投到输出头 $W_{d-t}$ 后得到
$$
\boxed{Su=-F.}
\tag{B.2}
$$
没有末段未知尾，也没有新增低核投影误差。

记
$$
\beta=\|P_{[q+1,q+d]}^{(m)}w\|,\qquad
\beta_+=\beta+e^{-74d^4}\|w\|.
$$
则 $\|u\|\le\beta_+$。因为 $u$ 是 $-F$ 的一个真实内部原像，
$$
\boxed{
\langle\mathcal H_{2,q}^{-1}F,F\rangle
=\langle\mathcal G^{-1}F,F\rangle\le\beta_+^2.
}
\tag{B.3}
$$
这一步使用的恰是逆压缩定义的真 Schur 度量，不是普通高块逆。

写
$$
v=v_{m,q}(w),\qquad E=\|v\|^2+\lambda^2.
$$
旧正通量估计给
$$
\left|\sum_t\langle H_tw_{q+t},z_t\rangle-E\right|
\le2e^{-70d^4}\|w\|\sqrt E.
$$
将 $w$ 带替成 (B.1) 中的 $\widehat v$，额外误差至多
$$
6e^{-74d^4}\|w\|\,\|z\|
\le6e^{-72d^4}\|w\|\lambda
\le e^{-70d^4}\|w\|\sqrt E.
$$
这里用的是已证 $\|z\|\le e^{2d^4}\lambda$，并有 $d\ge32$。
因 $F\in\mathscr Y_{2,q}$，最后得到
$$
\left|\langle F,\mathcal H_{2,q}^{-1}\sigma\rangle-E\right|
\le3e^{-70d^4}\|w\|\sqrt E.
$$
在 (B.3) 的同一个正度量中用 Cauchy--Schwarz，
$$
\boxed{
E-3e^{-70d^4}\|w\|\sqrt E
\le\beta_+\sqrt{\mathcal E_2}.
}
\tag{B.4}
$$
这是对真正 $w$、真正最优 $y,z$ 及 (A.2) 的实际有效源 $\sigma$ 的估计，不是环境任意源下界。

### C. 将真实强制能量定位到末块

对固定 $0\ne w\in W$，沿合法全整数头有 $v\to w$、$\beta_+\to0$。
充分大的窗口上 $\lambda>0$，并可置
$$
\epsilon_q=\frac{3e^{-70d^4}\|w\|}{\sqrt E}\longrightarrow0.
$$
由 $E/\lambda=\lambda+\|v\|^2/\lambda\ge2\|v\|$，
(B.4) 给
$$
\boxed{
\frac{\mathcal E_2}{\lambda^2}
\ge
\frac{4(1-\epsilon_q)^2\|v\|^2}{\beta_+^2}.
}
\tag{C.1}
$$
再用 (A.5) 还可重得旧能量身份的比例推论（此项不计新增结论）：
$
\boxed{
\frac{\lambda^2}{\|b\|^2}
\le
\frac{\beta_+^2}{\beta_+^2+4(1-\epsilon_q)^2\|v\|^2}
\longrightarrow0.
}
\tag{C.2}
$$
比例 (C.2) 也能从旧首段方程与缺陷正交直接推出，不能单独当作新进展。本节保留下来的新定位是 (A.2)–(A.4) 与 (C.1)：真实通量所强制的能量必须出现在明确的末块源 $\sigma$ 中，而不能只用全部 $\operatorname{Ran}S^*$ 投影损失替代。

若进一步能把实际 $\sigma$ 写成
$C_{2,q}h$，本稿的正确 Schur 收缩给
$$
\mathcal E_2
\le s^2\langle\mathcal H_{2,q+1}^{-1}h,h\rangle.
$$
结合 (B.4) 便是对任何这类原像能量的明确必要下界。
目前没有得到所需的反向上界：$V_1,V_2$ 的上升方向带受限 $D_3^*$，其间的 $Q_1^{-1}$ 也没有被交换掉。
固定层一般满射只付存在性，不能因此把 (A.2) 认成一个已知低成本的 $C$ 像。以上必要约束仍不证明 $N=M$。


[完整线性核链及合法 M 测试](R239-appendix-full-l-kernel-completion-and-legal-m-tests.md)已另外付清逐段源的同旗最小原像、两侧完整核及实际 lift；其最终未控量是精确合成向量 $\widetilde C_{\rm tot}(h(z))$。本节的 $z_2=\mathcal H_{2,q}^{-1}\sigma$ 识别它所使用的同一个低核部分，未给该合成量或 $\mathcal E_2$ 增加上界。
