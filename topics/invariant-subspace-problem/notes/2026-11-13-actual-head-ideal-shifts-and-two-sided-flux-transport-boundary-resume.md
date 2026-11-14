# 工作笔记：实际头理想生成元的段移与两侧窄通量运输

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；AI-assisted，GPT-6 Astra Pro。
状态：以下完整旗、原物理正交亏损及同一真实源的运输已逐项核对。它把已有两侧 $D_3$ 运输的最小原像方法应用到一个新的、须另核端点的头平移接口；不登记新的左费上界，不宣称 $\mathfrak K_qN\subset N$，无权 $N=M$ 仍开。

本笔记使用
[原两侧 Gram](../results/R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)、
[原联合旗与窄头跳跃](../results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)
及[原线性 lift](../results/R239-appendix-direct-linear-large-windows-and-all-q-minimal-energy.md)。
既有[窄通量平移笔记](2026-11-13-actual-narrow-head-flux-shifts-and-paid-last-source-1cf.md)
搬动的是同一最优右链的末段；这里同时搬动左最小链和右输入，并将来源匹配为同一个实际 $\xi$ 的 $N_j\xi$，不是把那个末段身份换名。

## 1. 原头、真实幂及窄矩阵的准确交织

固定原两个模型之一及
$$
m\ge5,\qquad d=2^m,\qquad
0\le j<m,\qquad r=2^j,\qquad
4d\le q,\quad q+r\le e^{d^3/4}.
\tag{1.1}
$$
记 $A=A_m,D=D_m,L=A+D$。
令 $Z=N_0^{[m]}$ 为真实有限头上的单步加权移位，
$$
Q=N_j^{[m]}=B_m^r/d_j,\qquad X=N_j.
$$
这里 $Q$ 是原头矩阵，$X$ 是整个实际边界上的理想生成元。
归一化来自原定义；两者均有范数至多一。
准确地，$Qe_i$ 在 $i<r$ 时为零，在 $i\ge r$ 时是 $e_{i-r}$ 的正实倍数。
两个实际 $A_m$ 都是 $B_m$ 的有限多项式，故
$$
[A,Q]=[D,Q]=0,\qquad [L,Q]=0.
\tag{1.2}
$$

原递归 $N_k=E_k+\eta_kE_k^*N_{k+1}$ 在第 $m$ 位截断，给
$$
X-Q=
\left(\prod_{k=j}^{m-1}\eta_k\right)
E_j^*E_{j+1}^*\cdots E_{m-1}^*N_m.
$$
此处的实际 $\eta_k=\alpha_{k+1}/\alpha_k$ 用
[R249 §1、§5.1](../results/R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)
的原权，明确有
$$
-\log\alpha_k=\frac{280}{3}16^k-90\,8^k+300\,2^k-\frac{850}{3},
\qquad
-\log\eta_k=1400\,16^k-630\,8^k+300\,2^k.
$$
因而对 $d\ge32$，
$$
\frac{-\log\eta_{m-1}}{d^4}
=\frac{175}{2}-\frac{315}{4d}+\frac{150}{d^3}
\ge\frac{175}{2}-\frac{315}{128}>85>80.
$$
这里没有用仅为 $770\,16^{m-1}$ 的粗指数替代实际相邻比。
因此
$$
\boxed{\|X-Q\|\le\eta_{m-1}\le e^{-80d^4}.}
\tag{1.3}
$$
头张量恒等因子省略，未把 $X$ 当作纯尾算子。
因为 $X=B^r/d_j$ 与原 $T$ 交换，且 $r\ge1$，
$$
XM\subset BM\subset N.
\tag{1.4}
$$

令 $W_s=\operatorname{span}\{e_0,\ldots,e_{s-1}\}$，
$s\le0$ 时取零，$s\ge d$ 时取全头。
沿原稿定义
$$
H_t=P_{W_{d-t}}A(I-P_{W_{d-t+1}}).
$$
对 $t\le1$ 或 $t\ge d$，这个矩阵为零。
单条 $r$ 步加权对角给
$$
P_{W_s}Q=QP_{W_{s+r}},\qquad
(I-P_{W_s})Q=Q(I-P_{W_{s+r}}).
$$
结合 (1.2) 得
$$
\boxed{H_tQ=QH_{t-r},\qquad QH_t=H_{t+r}Q.}
\tag{1.5}
$$
所有端点均包含在上述零矩阵约定中。

顺便保留一个真实长跳跃的消去式。若
$v=P_{V_{m,q+d}}\xi$，$f_t=H_tv_{q+t}$，则低输出方程给
$$
(Lf)_{q+t}=(AH_t-H_{t+1}A)v_{q+t}.
$$
用 (1.5) 的单步 $Z$，若 $R=A-Z$，准确有
$$
\boxed{AH_t-H_{t+1}A=RH_t-H_{t+1}R.}
\tag{1.6}
$$
原 $N_0$ 项在这里精确相消。$N$ 型 $R=\sum_{k\ge1}^{m-1}b_kN_k^{[m]}$；
$Y$ 型还保留
$Y_0^{[m]}-Z=-\eta_0N_1^{[m]}(I+Z)^{-1}$。
(1.6) 不是对完整逆能量的估计。

## 2. 两侧物理输入与记号

对 $\ell=q,q+r$，全部对象取原两侧稿的相同联合旗：
$$
V_\ell=\{v\in P_{\le\ell}H:P_{<\ell}Lv=0\},
\qquad E_\ell v=Av_\ell,
$$
$$
\mathcal U_\ell=Z_\ell\ominus\ker\mathsf F_\ell,\qquad
\mathcal Y_{0,\ell}=\ker\mathsf F_\ell\oplus\mathscr X_{H,\ell}.
$$
$\mathsf F_\ell$ 在上述公式中按两侧稿表示裸低链的首输出；
完整输入上的首输出记为 $F_\ell$。
写
$$
\mathcal J_{-,\ell}=E_\ell^\dagger\mathsf f_\ell,\qquad
\mathcal Q_\ell=\mathcal J_{-,\ell}^*\mathcal J_{-,\ell},\qquad
\mathcal D_\ell=I+\mathcal Q_\ell.
$$
两侧等距嵌入、高输出算子和 Gram 是
$$
\mathcal I_\ell(a,y)=\mathcal J_{-,\ell}a-a-y,\qquad
\mathscr E_\ell=\operatorname{Ran}\mathcal I_\ell,
$$
$$
L\mathcal I_\ell=-\iota_2\mathcal B_\ell,\qquad
H_\ell^{\rm two}=\mathcal B_\ell\mathcal B_\ell^\sharp.
\tag{2.1}
$$
输入范数是 $\mathcal D_\ell\oplus I$；$\mathcal I_\ell$ 对原物理范数等距。

记原 $t$ 段的完整输入为
$$
\mathscr C_{\ell,t}
=\bigoplus_{i=0}^{d-t}e_i
  \bigl(\ker D^{d-i}\cap\mathcal H_{\ell+t}\bigr).
\tag{2.2}
$$
高输出 $\mathscr Y_{2,\ell}$ 是原内部输出中出生至少二的闭子空间；
在第 $u$ 段，其尾核阶还满足 $h\le u-1$。
定义物理头运输
$$
Q_H:\mathscr Y_{2,q+r}\longrightarrow\mathscr Y_{2,q}
$$
为直接作用 $Q$，再按相同物理孔层读取：旧第 $u$ 段变为新第 $u+r$ 段。

这个限制合法。旧头指标 $i$ 经 $Q$ 变成 $i-r$；
若不为零，原上界 $i\le d-u-1$ 给
$i-r\le d-(u+r)-1$。
原尾核阶不变，而新允许的头旗及出生旗均扩大。
旧 $u>d-r-1$ 的输出被 $Q$ 全部杀掉。
所以
$$
\|Q_H\|\le\|Q\|\le1.
\tag{2.3}
$$

## 3. 整个两侧输入的真实运输

取任意 $x'=\mathcal I_{q+r}(a',y')$，写
$$
x'=v'-c',\qquad
v'=\mathcal J_{-,q+r}a',\qquad c'=a'+y'.
$$
它的左、右孔支撑分别为 $[0,q+r]$ 与 $[q+r+1,q+r+d]$。
因为 $Lx'$ 只有高输出，(1.2) 与 §2 给
$$
LQx'=-\iota_2Q_H\mathcal B_{q+r}(a',y').
\tag{3.1}
$$

### 3.1 末端和搬入右侧的左层均满足原旗

旧右输入第 $u>d-r$ 段只有头 $i\le d-u<r$，故被 $Q$ 杀掉。
因此 $Qx'$ 的孔支撑至多为 $q+d$。

对旧右段 $u\le d-r$，新段号 $t=u+r$，头降低 $r$，
于是 (2.2) 的头上界及尾核旗直接保留。

还须核旧左向量在 $q+1,\ldots,q+r$ 的这些层。
对任意 $v'\in V_{q+r}$，逐次用低输出递推，可得在这些层上
$$
D^k v'_p=(-A)^kv'_{p-k}.
$$
取旧头坐标 $i$ 和 $k=d-i$，右侧第 $i$ 头为零；
这里 $p\ge q+1\ge4d+1$，不越最低孔层。因此
$$
(v'_p)_i\in\ker D^{d-i}.
\tag{3.2}
$$
经过 $Q$，新头 $i-r$ 至多为 $d-r-1$。
对于新段 $1\le t\le r$，这不超过 $d-t$；
旧尾核阶 $d-i$ 也不超过新允许阶 $d-(i-r)$。
所以这些搬入的左层全部属于原 $\mathscr C_{q,t}$。
这一步没有把只有总 $D^d$ 核阶的向量免费当作逐头联合旗。

### 3.2 减去真正左最小者后只剩有限核

令
$$
v=P_{\le q}Qx',\qquad c=-P_{[q+1,q+d]}Qx'.
$$
由 (3.1)，$v\in V_q$，$c\in\mathscr C_q$，
首源相消且右侧低出生内部输出为零。
把 $c$ 按原正交分解唯一写成
$$
c=a+y,\qquad a\in\mathcal U_q,\quad y\in\mathcal Y_{0,q}.
$$
其 $a$ 由首源唯一确定：
$\mathsf f_qa=E_qv$。
定义
$$
k_-=v-\mathcal J_{-,q}a.
$$
真正左最小者的性质给
$$
k_-\in\ker E_q,\qquad k_-\perp\operatorname{Ran}\mathcal J_{-,q}.
$$
它还与全部右侧孔层正交，故
$$
\boxed{
Q\mathcal I_{q+r}(a',y')
=\mathcal I_q\mathsf T_{j,q}(a',y')+k_-,
\qquad k_-\perp\mathscr E_q,\quad Lk_-=0.
}
\tag{3.3}
$$
这里 $\mathsf T_{j,q}(a',y')=(a,y)$ 是由上述真实投影定义的线性算子。
不需要显式左头逆，也没有把构造左链当最小左链。

正交分解和原等距度量给
$$
\boxed{
\|\mathsf T_{j,q}(a',y')\|_{\mathcal D_q\oplus I}^2+\|k_-\|^2
=\|Q\mathcal I_{q+r}(a',y')\|^2
\le\|Q\|^2\|(a',y')\|_{\mathcal D_{q+r}\oplus I}^2.
}
\tag{3.4}
$$
因此该运输有界，范数至多 $\|Q\|$。没有随段数累加的 $\sqrt d$，
也没有 $e^{20d^4}$ 左塔代价。

对 (3.3) 应用 $L$，得到完整高输出交织
$$
\boxed{\mathcal B_q\mathsf T_{j,q}=Q_H\mathcal B_{q+r}.}
\tag{3.5}
$$

## 4. 两侧真实 Gram 收缩及最小原像亏损

把下一窗口的真正最小输入经 (3.4) 运输，(3.5) 给
$$
\boxed{
Q_H^*(H_q^{\rm two})^{-1}Q_H
\le\|Q\|^2(H_{q+r}^{\rm two})^{-1}.
}
\tag{4.1}
$$
这是完整两侧原物理费用，包含 $I+\mathcal Q$；不使用旧末块的普通逆压缩。

令
$$
\mathscr K_\ell f
=\mathcal I_\ell\mathcal B_\ell^\sharp(H_\ell^{\rm two})^{-1}f.
$$
它是该两侧输入空间中的真正最小物理原像，
$L\mathscr K_\ell f=-\iota_2f$。
对 $f'\in\mathscr Y_{2,q+r}$，定义
$$
k_{j,q}(f')
=Q\mathscr K_{q+r}f'-\mathscr K_qQ_Hf'.
$$
(3.3)、(3.5) 表明该差由两项组成：
一个在 $\mathcal I_q\ker\mathcal B_q$ 中，另一个是与 $\mathscr E_q$ 正交的 $k_-$。
这两项互相正交，也都与 $\mathscr K_qQ_Hf'$ 正交。因此
$$
\boxed{
\begin{aligned}
k_{j,q}(f')&\in\ker L\cap P_{\le q+d}H,\\
\|k_{j,q}(f')\|^2
&=\|Q\mathscr K_{q+r}f'\|^2
-\|Q_Hf'\|_{(H_q^{\rm two})^{-1}}^2\\
&\le\|Q\|^2\|f'\|_{(H_{q+r}^{\rm two})^{-1}}^2
-\|Q_Hf'\|_{(H_q^{\rm two})^{-1}}^2.
\end{aligned}
}
\tag{4.2}
$$
所有右侧均为真实正能量差。

(1.1) 给 $q+d\le e^{d^3/3}$。原有限核 lift 遂给
$$
\boxed{
\|P_Wk_{j,q}(f')\|
\le e^{-75d^4}\|k_{j,q}(f')\|
\le e^{-75d^4}\|Q\|\,
\|f'\|_{(H_{q+r}^{\rm two})^{-1}}.
}
\tag{4.3}
$$
这里只支付 $W$ 投影；没有把完整缺陷范数宣布为 carry。

## 5. 同一个真实来源的窄通量匹配

沿两侧稿 §9.4，对任意 $\xi\in M$，明确取
$$
f_q(\xi)_t=H_t(P_{V_{m,q+d}}\xi)_{q+t},
\qquad
\overline f_q(\xi)
=f_q(\xi)-B_{A,q}\bigl(\widehat a_q(\xi)-a_q(\xi)\bigr).
\tag{5.1}
$$
使用
$$
\delta=e^{-74d^4},\qquad \delta_r=12e^{-73d^4},\qquad
\|B_{A,q}\|\le\nu_m<1.
$$
同头的两个宽低投影 $q+d$、$q+r+d$ 都由 (1.1) 和原证明的
$\log(2+R)\le d^3$ 预算覆盖。

先将两边低投影换成对应原向量的孔截断，每边误差至多
$6\delta\|\xi\|$；再以 (1.3) 将 $X$ 换成 $Q$。
未投影的头矩阵由 (1.5) 逐段完全相同，且不同段保持物理孔层正交。
因此
$$
\|f_q(X\xi)-Q_Hf_{q+r}(\xi)\|
\le18\delta\|\xi\|.
\tag{5.2}
$$
同源修正的两项总和至多
$24\nu_m e^{-73d^4}\|\xi\|$，故
$$
\boxed{
\|\overline f_q(X\xi)-Q_H\overline f_{q+r}(\xi)\|
\le42e^{-73d^4}\|\xi\|.
}
\tag{5.3}
$$
原合法窗有 $H_q^{\rm two}\ge H_q^\circ\ge e^{-2d^4}I$，
所以进一步
$$
\boxed{
\|\overline f_q(X\xi)-Q_H\overline f_{q+r}(\xi)\|_{(H_q^{\rm two})^{-1}}
\le e^{-71d^4}\|\xi\|.
}
\tag{5.4}
$$
这个式子已经匹配为同一实际 $\xi$ 的 $N_j\xi$，没有未知的未来带主项。
它没有把 $\overline f_q(X\xi)$ 误写成 $\overline f_q(\xi)$。

## 6. 原物理最小像的运输与仍保留的边界

令
$$
\mathfrak K_\ell\xi=\mathscr K_\ell\overline f_\ell(\xi),
\qquad \xi\in M.
$$
原两侧稿已付
$$
\|\mathfrak K_\ell-P_{\mathscr G_\ell}|_M\|
\le\delta+\delta_r,\qquad
\|\mathfrak K_\ell\|\le1+\delta+\delta_r,
$$
其中 $\mathscr G_\ell$ 是两侧输入空间中完整零源核的正交补。

对 $f'=\overline f_{q+r}(\xi)$ 用 (4.2)，再用 (5.4)，得到
$$
\mathfrak K_qX\xi-Q\mathfrak K_{q+r}\xi
=-k_{j,q}(f')+
\mathscr K_q\bigl(\overline f_q(X\xi)-Q_H\overline f_{q+r}(\xi)\bigr).
$$
由 (4.3) 和上面的原物理算子范数，最后有
$$
\boxed{
\|P_W(\mathfrak K_qX|_M-Q\mathfrak K_{q+r})\|_{M\to H}
\le e^{-70d^4}.
}
\tag{6.1}
$$

本段新增的是头降低 $2^j$、源窗同时平移 $2^j$ 时的完整输入域验证，
以及同一真实窄源的 (5.4)；最小像的一般正交投影方法明确扣回旧两侧 $D_3$ 稿。
固定头不变，所有使用的窗口与 lift 均保持 (1.1)。

尽管 $X M\subset N$，(6.1) 仍不能免费删除 $\mathfrak K_qX|_M$：
目前没有证明 $\mathfrak K_qN\subset N$。
也没有把 $P_W$ 移过 $Q$、$P_M$ 或最小逆。
这些运输给同一实际来源的更多相容关系，尚未给
$\|\overline f\|_{(H^{\rm two})^{-1}}$ 的小量上界，
也未证明所需三 Gram 左费比较或无权 $N=M$。
