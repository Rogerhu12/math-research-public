# 工作笔记：实际高孔首头零返回测试、无右逆的观测式与未控横向块

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf。
状态：已完整推导的工作接口。不登记新的左费上界；不把单孔 Gram 下界、全环境联合下界或有限四头结论外推到实际高孔层。

本笔记继续
[真实左源 Gram](2026-11-13-left-source-gram-and-paid-actual-dual-source-1cf.md)、
[同返回源两侧规范](../results/R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)
及
[有限头频率滤波的全环境下界](../results/R271-appendix-finite-head-frequency-filter-and-polynomial-environment-gap.md)。

## 1. 原实际空间及同源规范

固定原模型之一、$m\ge5$、$d=2^m$ 和原合法整数窗口
$$
4d\le q\le e^{d^3/4}.
$$
令 $L=A_m+D_m$，以下简记 $A=A_m,D=D_m$。
全部头基、尾孔层及投影都用原物理 Hilbert 内积。
记
$$
E_{h,p}=\ker(D^h|_{\mathcal H_p}),\qquad
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q}.
$$

完整左空间和左最小原像是
$$
\mathscr V_q=\{v\in P_{\le q}H:P_{<q}Lv=0\},
\qquad E_qv=Av_q,\qquad \mathcal V_q=E_q^\dagger.
$$
既有左源稿已证明 $E_q$ 到 $\mathscr R_q$ 有界满射。
右侧沿用裸低链 $Z_q$、$\mathcal U_q=Z_q\ominus\ker\mathsf F_q$、
$\mathsf f_q=\mathsf F_q|_{\mathcal U_q}$。
令
$$
\mathcal Q_q=(\mathcal V_q\mathsf f_q)^*
                  \mathcal V_q\mathsf f_q,\qquad
\mathcal D_q=I+\mathcal Q_q,\qquad
\mathcal K_{0,q}=\ker B_{A,q}.
$$
取准确规范状态
$$
a^\sharp\in\mathcal U_q,\qquad
a^\sharp\perp_{\mathcal D_q}\mathcal K_{0,q},
$$
并记
$$
r^\sharp=\mathsf f_qa^\sharp,\qquad v=\mathcal V_qr^\sharp.
\tag{1.1}
$$
$v$ 属于实际左空间；没有把它认成原 $M$ 中的向量。

## 2. 高孔层仍成立的首头零返回子空间

对任意 $h\in E_{d-1,q}$，固定孔层的既有纯尾满射允许使用
$$
R_{q+1}= (D:\mathcal H_{q+1}\to\mathcal H_q)^\dagger.
$$
本节不对其范数声称单孔的统一正界。

令 $k_h$ 只有第一段非零：
$$
(k_h)_1=e_0R_{q+1}h,\qquad (k_h)_t=0\quad(t\ge2).
\tag{2.1}
$$
因为 $D^dR_{q+1}h=D^{d-1}h=0$，它满足第一段第零头的真实旗。
又 $Ae_0=0$，故所有内部输出为零，首输出恰为 $e_0h$。

任何同源裸低链的第一段第零头都要解 $Dz=h$，其范数至少为
$\|R_{q+1}h\|$；(2.1) 已达到下界。
所以同时有
$$
\boxed{
k_h=\mathsf f_q^{-1}(e_0h),\qquad
k_h\text{ 也是完整最小链},\qquad B_{A,q}k_h=0.
}
\tag{2.2}
$$
这里没有先投一个任意短链再把它叫作裸最小者。

## 3. 只用于配对的明确左原像

原实际头上三角，且第一条上对角线全部非零。
定义有限头向量 $c_{-1}=e_0$，以及
$$
c_j\in\operatorname{span}\{e_1,\ldots,e_{j+1}\},
\qquad Ac_j=c_{j-1},\qquad 0\le j\le d-2.
\tag{3.1}
$$
每步限制是上三角的可逆矩阵，因此存在唯一这样的 $c_j$。
这些系数保留实际小 carry；没有给它们头无关的范数上界。

定义 $\ell_h$ 的非零孔层为
$$
(\ell_h)_{q-j}=(-1)^j c_jD^jh,\qquad 0\le j\le d-2.
\tag{3.2}
$$
相邻层的 $A$ 项与 $D$ 项由 (3.1) 准确相消；
最下端由 $D^{d-1}h=0$ 消失。
所以
$$
\ell_h\in\mathscr V_q,\qquad E_q\ell_h=e_0h.
\tag{3.3}
$$
它只支持于 $[q-d+2,q]$。
逐头旗也正确：第 $j$ 项头指标至多为 $j+1$，
而其尾属于 $E_{d-1-j,q-j}$。

$\ell_h$ 是构造左原像，不是左最小原像。
不过
$$
\ell_h-\mathcal V_q(e_0h)\in\ker E_q,\qquad v\perp\ker E_q.
$$
因此规范正交在 (2.2) 上给准确配对
$$
\boxed{
\langle a^\sharp,k_h\rangle+\langle v,\ell_h\rangle=0
\qquad(h\in E_{d-1,q}).
}
\tag{3.4}
$$
没有将两个不同最小逆作交换。

## 4. 把右逆完全消去的实际投影观测式

对任意 $z\in E_{d,q+1}$，令 $h=Dz$。
则 $h\in E_{d-1,q}$，并且
$$
R_{q+1}Dz=P_{(\ker D)^\perp}z.
$$
另一方面，
$$
(a^\sharp_1)_0\in E_{d,q+1},\qquad
(a^\sharp_1)_0\perp\ker(D|_{\mathcal H_{q+1}}).
\tag{4.1}
$$
第一个包含来自原首段旗。第二个正交性来自：第一段第零头的任意 $\ker D$ 向量都是首输出为零的裸低链，
而 $a^\sharp\in\mathcal U_q$ 对这些向量正交。

把 $h=Dz$ 代入 (3.4)，利用 (4.1)，得到
$$
\left\langle (a^\sharp_1)_0,z\right\rangle
+\sum_{j=0}^{d-2}(-1)^j
\left\langle c_j^*v_{q-j},D^{j+1}z\right\rangle=0.
$$
所以准确的观测算子为
$$
\boxed{
\Gamma_{m,q}v
=
P_{E_{d,q+1}}
\sum_{j=0}^{d-2}(-1)^j(D^*)^{j+1}c_j^*v_{q-j},
}
\tag{4.2}
$$
并且
$$
\boxed{
\Gamma_{m,q}v=-(a^\sharp_1)_0,\qquad
\|\Gamma_{m,q}v\|\le\|a^\sharp\|.
}
\tag{4.3}
$$
这里 $c_j^*$ 只提取对应物理头线性组合，
各项都落在同一个尾孔层 $\mathcal H_{q+1}$。

(4.3) 没有乘 $R_{q+1}$ 的范数。
但是 (4.2) 的真实 $P_{E_{d,q+1}}$ 仍保留；
不能删除它，也不能把 $c_j$ 的实际头代价忽略。
更没有证明由 $\Gamma_{m,q}v$ 和 $r^\sharp$ 反向控制整个 $\|v\|$ 的温和常数。

## 5. 全环境能量看见的横向块

下面给一个准确分解，说明为什么新的环境联合下界还不能直接完成 (4.3)。

令
$$
H_-=P_{\le q}H,\qquad
S_-=P_{<q}L|_{H_-}:H_-\to P_{<q}H.
$$
则 $\mathscr V_q=\ker S_-$。
$v\in\mathscr V_q$ 的整个环境伴随只支持到 $q+1$，且
$$
\boxed{
P_{\le q}L^*v=S_-^*v_{<q}+P_qA^*v_q,\qquad
P_{q+1}L^*v=D^*v_q.
}
\tag{5.1}
$$
此处 $S_-^*$ 是上述两个实际截断空间之间的伴随。

由于 $P_{\mathscr V_q}S_-^*=0$，并且 $E_q$ 的值域包含于
$\mathscr R_q$，有
$$
\boxed{
P_{\mathscr V_q}P_{\le q}L^*v
=E_q^*P_{\mathscr R_q}v_q.
}
\tag{5.2}
$$
$P_{\mathscr R_q}$ 不能省略：$v_q$ 本身不一定是源空间向量。
而横向分量准确为
$$
\boxed{
(I-P_{\mathscr V_q})P_{\le q}L^*v
=S_-^*v_{<q}
 +(I-P_{\mathscr V_q})P_qA^*v_q.
}
\tag{5.3}
$$
三个正交分量给完整的能量恒等式
$$
\begin{aligned}
\|L^*v\|^2
={}&\|E_q^*P_{\mathscr R_q}v_q\|^2+\|D^*v_q\|^2\\
&+\left\|S_-^*v_{<q}
 +(I-P_{\mathscr V_q})P_qA^*v_q\right\|^2.
\end{aligned}
\tag{5.4}
$$
前两项至多为
$(\|A\|^2+\|D\|^2)\|v_q\|^2$。
现有零返回规范的左测试全部在 $\mathscr V_q$，
因此 (3.4) 本身没有给 (5.3) 的上界。
这不是证明该块必然很大，而是指出所需额外预算的准确位置。

具体地，令 $\gamma_m$ 为已证全环境联合下界的平方根。
因为 $Lv$ 只有顶端源 $r^\sharp$，且
$\|r^\sharp\|\le\|D\|\|a^\sharp\|$，
(5.4) 只能推出
$$
\begin{aligned}
\gamma_m^2\|v\|^2
\le{}&\|D\|^2\|a^\sharp\|^2
 +(\|A\|^2+\|D\|^2)\|v_q\|^2\\
&+\left\|S_-^*v_{<q}
 +(I-P_{\mathscr V_q})P_qA^*v_q\right\|^2.
\end{aligned}
\tag{5.5}
$$
未经控制的最后一项可能承载这个环境能量。
不能把 (5.5) 改写成已经得到
$\|L^*v\|\le C_m(\|r^\sharp\|+\|a^\sharp\|)$。

## 6. 继续保留的具体目标

实际 $a^\sharp$ 与原源之间的 $\mathcal D_q$ 费用已经支付；
(4.3) 是它满足的准确高孔观测式。
仍需用原真实来源、完整低链或窄 $\overline f$ 进一步控制 (5.3)，
或直接证明可付的三 Gram 左费比较
$$
\mu_q(r)^2
\le C_m\left(
 \|\mathsf f_q^{-1}r\|^2+\lambda_q(G_qJ_q^{-1}r)^2
 \right)
$$
在原来源上成立。
不能用单孔 $D_2D_2^*$ 的正界代替高孔限制，
也不能让 $P_M$ 与上述最小逆或环境伴随未经证明地交换。

本笔记不扩大原 lift 窗，不登记新的 $\mu$ 上界；
无权 $N=M$ 和普通复 Hilbert ISP 继续开放。

## 7. 一个不使用高孔逆的低孔系数约束

本节单独取尾孔截面 $q=0$；不把它代入前面 $q\ge4d$ 的低投影定理。
所用的只是 [R239 逐步稿 §6 式 (6.7)](2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md)：
它对任意 $m\ge5$、$1\le Q_0\le e^{(2^m)^3/3}$ 的
$\ker L_m\cap\mathcal H_{\le Q_0}^{(m)}$ 给实际提升到 $N$，
相对误差为 $e^{-75(2^m)^4}$。
这里会取 $Q_0=1$。这个初值空间允许孔位无限远，不要求有限坐标支撑。

已全文核对 [R200](../results/R200-boundary-right-shift-domains-and-forward-division-saturation.md)
及[首位小图](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)。
R200 的缺失行读 $w_{2^j-1}/\alpha_j$，并要求实际右移图域；
首位小图给压缩伴随和图度量约束。以下读原 $W$ 中的 $w_{2^j}$，
不使用右移图域；它是既有有限核提升的具体低孔推论，不登记新主定理。

### 7.1 两种真实模型共用的明确有限孔核

记
$$
b_j=(j+1)^{-2},\qquad
S_m=\sum_{j\ge m}b_j^2,\qquad
\delta_m=e^{-75\,16^m},\qquad m\ge5.
$$
在原 $\ell^2(\mathbb N_0)$ 正交基中，定义
$$
k_m=e_1-\frac1{S_m}\sum_{j\ge m}b_j e_{2^j}.
\tag{7.1}
$$
尾和在 Hilbert 范数中收敛，且
$$
\boxed{\|k_m\|^2=1+S_m^{-1}.}
\tag{7.2}
$$

对两个模型，实际有限头都满足 $A_me_1=e_0$：
$N_0$ 的首个非零矩阵元为 $1$，$Y_0=N_0(I+N_0)^{-1}$
在 $e_1$ 上有相同作用，其他项都杀去 $e_1$。
此外 $A_me_0=0$。
对 $j\ge m$，$e_{2^j}$ 恰是第零头与第 $j$ 个尾单孔的张量，所以
$$
L_me_1=e_0,\qquad L_me_{2^j}=b_j e_0.
$$
因此
$$
\boxed{L_mk_m=0,\qquad k_m\in\mathcal H_{\le1}^{(m)}.}
\tag{7.3}
$$
没有把这个纯线性核向量直接当作真实 $T$ 核；下一步才使用已付提升。

### 7.2 原缺陷的同一尾和身份

设 $w\in W=M\ominus N$，取第一变量线性的复内积，记
$$
w_n=\langle w,e_n\rangle.
$$
(7.1) 的系数均为实数，因此
$$
\langle w,k_m\rangle
=w_1-\frac1{S_m}\sum_{j\ge m}b_jw_{2^j}.
$$
这个标量级数由 Cauchy--Schwarz 绝对收敛。

对 (7.3) 使用 $Q_0=1$ 的实际提升，得到 $n_m\in N$，
$\|n_m-k_m\|\le\delta_m\|k_m\|$。
因为 $\langle w,n_m\rangle=0$，准确有
$$
\boxed{
\left|\sum_{j\ge m}b_jw_{2^j}-S_mw_1\right|
\le\delta_m\sqrt{S_m+S_m^2}\,\|w\|.
}
\tag{7.4}
$$
这是同一个 $w$ 在所有 $m\ge5$ 上的约束，不更换相邻头的来源。

### 7.3 相邻头相减的明确逐位费用

令括号内差值为
$$
\epsilon_m=\sum_{j\ge m}b_jw_{2^j}-S_mw_1.
$$
相邻 $m$ 准确相减得到
$$
b_m\bigl(w_{2^m}-b_mw_1\bigr)=\epsilon_m-\epsilon_{m+1}.
$$
故
$$
\begin{aligned}
|w_{2^m}-b_mw_1|
&\le b_m^{-1}
\left[\delta_m\sqrt{S_m+S_m^2}
+\delta_{m+1}\sqrt{S_{m+1}+S_{m+1}^2}\right]\|w\|\\
&\le
\frac{2(m+1)^2}{\sqrt{3m^3}}\,
\sqrt{1+\frac1{3m^3}}\,
\delta_m\|w\|\\
&\le 2\sqrt m\,\delta_m\|w\|
\qquad(m\ge5).
\end{aligned}
\tag{7.5}
$$
第二行使用 $S_m\le1/(3m^3)$ 及 $\delta_{m+1}\le\delta_m$。
末行由
$$
(1+1/m)^4\left(1+\frac1{3m^3}\right)
\le (6/5)^4(1+1/375)<3
$$
给出。因此
$$
\boxed{
|w_{2^m}-(m+1)^{-2}w_1|
\le2\sqrt m\,e^{-75\,16^m}\|w\|
\quad(m\ge5).
}
\tag{7.6}
$$

还可把全部远单孔坐标合成一个原 Hilbert 范数界：
$$
\boxed{
\left\|
\sum_{j\ge m}\bigl(w_{2^j}-b_jw_1\bigr)e_{2^j}
\right\|
\le3\sqrt m\,e^{-75\,16^m}\|w\|.
}
\tag{7.7}
$$
确实，$j\delta_j^2$ 的相邻比为
$$
\frac{j+1}{j}\exp[-2250\,16^j]<\frac12
\qquad(j\ge5),
$$
所以 $\sum_{j\ge m}j\delta_j^2\le2m\delta_m^2$。
对 (7.6) 平方求和即可，常数 $2\sqrt2<3$。

特别，若 $P_{\mathrm{one},\ge m}$ 表示只保留这些远单孔坐标，
则
$$
\frac{\|P_{\mathrm{one},\ge m}w\|}{\sqrt{S_m}}
\longrightarrow |w_1|.
\tag{7.8}
$$
这里只用 $S_m\ge1/[3(m+1)^3]$ 将 (7.7) 的余项除以 $\sqrt{S_m}$。

### 7.4 与原高孔问题的区别

这里的 $m$ 截的是单孔所在的物理位号，
$P_{\mathrm{one},\ge m}$ 不是原全部孔次数的高尾投影。
(7.6)--(7.8) 没有控制二孔及更高孔分量，
也没有推出 $w_1=0$、$w=0$ 或无权 $N=M$。
它们提供的是同一真实缺陷来源跨头的具体坐标约束，
不替代 §5 尚未控制的横向块，也不扩大任何实际 lift 上窗。

## 8. 更高有限孔的完整图核与同一来源坐标

本节继续 §7 的实际 $L_m=A_m+D_m$、$W=M\ominus N$，
仍只使用已付的有限核提升，不调用高孔低投影。
图核本身是 §3 左塔取 $h=D_mz$ 后与首头向量 $e_0z$ 的直接组合；
本节保存它在整个有限孔层上的实际坐标读数及明确成本，不重复登记左塔或提升定理。
记尾齐次层为 $\mathcal H_p^{(m)}$，并写
$$
w_t=P_{\mathbb C^d\otimes\mathcal H_t^{(m)}}w,\qquad
w_{0,p}=(e_0^*\otimes I)w_p.
$$
这里 $w_{0,p}$ 是第零头的尾向量；所有头读取均按原物理正交基，
复内积仍取第一变量线性。

取
$$
m\ge5,\qquad d=2^m,\qquad 1\le p\le d-1.
$$
沿 §3 的实际头链，置 $c_{-1}=e_0$，并对 $0\le j<p$ 取
$$
c_j\in\operatorname{span}\{e_1,\ldots,e_{j+1}\},\qquad
A_mc_j=c_{j-1}.
\tag{8.1}
$$
各个 $c_j$ 的真实系数全部保留。固定 $p$ 后，只要 $2^m>p$，
这些有限坐标不再随 $m$ 改变：有限头的左上角是真实同一算子的限制，
(8.1) 的三角方程及其唯一解也相同。

### 8.1 一个无需任何删除逆的全层测试族

对任意 $z\in\mathcal H_p^{(m)}$ 定义
$$
\boxed{
\mathcal K_{m,p}z
=-e_0z+\sum_{j=0}^{p-1}(-1)^j c_jD_m^{j+1}z.
}
\tag{8.2}
$$
第零项在第 $p$ 尾层，第 $j$ 个求和项在第 $p-j-1$ 尾层，
所以各项的孔支撑彼此正交。
计算 $L_m\mathcal K_{m,p}z$：
$-e_0D_mz$ 与 $A_mc_0D_mz$ 相消；
其余相邻项由 $A_mc_j=c_{j-1}$ 相消。
最末项是 $(-1)^{p-1}c_{p-1}D_m^{p+1}z=0$。
因此
$$
\boxed{
L_m\mathcal K_{m,p}=0,\qquad
\operatorname{Ran}\mathcal K_{m,p}
\subset\mathcal H_{\le p}^{(m)}.
}
\tag{8.3}
$$
这是整个 $\mathcal H_p^{(m)}$ 上的有界图映射，不涉及
$D_m^\dagger$、其范数或其与任何投影的交换。

令 $S_m=\sum_{j\ge m}b_j^2$，$b_j=(j+1)^{-2}$。
对 $u\in\mathcal H_r^{(m)}$，逐输出集合使用 Cauchy--Schwarz，
每个输入集合被计数 $r$ 次，给
$$
\|D_mu\|^2\le rS_m\|u\|^2.
$$
迭代得到
$$
\|D_m^{j+1}|_{\mathcal H_p^{(m)}}\|^2
\le\frac{p!}{(p-j-1)!}S_m^{j+1}.
\tag{8.4}
$$
由 (8.2) 的正交孔支撑，
$$
\boxed{
\|\mathcal K_{m,p}\|\le C_{m,p},\qquad
C_{m,p}^2=
1+\sum_{j=0}^{p-1}\|c_j\|^2
\frac{p!}{(p-j-1)!}S_m^{j+1}.
}
\tag{8.5}
$$
对固定 $p$，$C_{m,p}\to1$。这不是对增长的 $p$ 给头无关常数；
(8.5) 明确保留了所有 $c_j$、阶乘和 $S_m$。

### 8.2 提升后取得原缺陷的完整坐标读数

这里 $Q_0=p\le d-1<e^{d^3/3}$，所以 R239 的同一个有限核提升
直接作用于 (8.3)，且
$$
\|P_W\mathcal K_{m,p}\|\le\delta_m C_{m,p},
\qquad \delta_m=e^{-75\,16^m}.
$$
取真正伴随并作用于同一个原 $w\in W$，得到
$$
\boxed{
\left\|
w_{0,p}
-\sum_{j=0}^{p-1}(-1)^j
(D_m^*)^{j+1}c_j^*w_{p-j-1}
\right\|
\le\delta_m C_{m,p}\|w\|.
}
\tag{8.6}
$$
$c_j^*$ 只读取所标尾层的物理头线性组合。
各项均在同一个原尾层 $\mathcal H_p^{(m)}$，没有混合不同头的来源。

这条式子没有遗漏高孔情形中的核投影：
这里输入层满足 $p\le d-1$，而 $D_m^d$ 在整个 $\mathcal H_p^{(m)}$
上本来就是零。因此其测试域就是全层。
当 $p$ 超过这个范围时，不能据此删除 §4 中真实的 $P_{E_{d,\cdot}}$。

### 8.3 第一、第二孔层的明确形式

$p=1$ 时 $c_0=e_1$，$C_{m,1}=\sqrt{1+S_m}$，故 (8.6) 给
$$
\boxed{
\left\|
\sum_{j\ge m}(w_{2^j}-b_jw_1)e_{2^j}
\right\|
\le\delta_m\sqrt{1+S_m}\,\|w\|.
}
\tag{8.7}
$$
这改进 §7 的 $3\sqrt m$ 常数；§7 的相邻头减差证明及其范围仍然正确。
新增测试族同时读取了首头的全部单孔方向，而不仅是权向量 $b$ 的方向。

$p=2$ 时，记 $a=A_{m,1,2}\ne0$、$b=A_{m,0,2}$；
两种实际头都有 $A_{m,0,1}=1$，所以
$$
c_1=\frac{e_2-be_1}{a}.
$$
这些是固定的真实头系数，不把小 $a$ 吸收到未标明的常数。
(8.6) 具体成为
$$
\boxed{
\left\|
w_{0,2}-D_m^*w_{1,1}
+(D_m^*)^2\frac{w_{2,0}-\overline b\,w_{1,0}}{\overline a}
\right\|
\le\delta_m C_{m,2}\|w\|,
}
\tag{8.8}
$$
其中 $w_{i,t}$ 表示第 $i$ 个头坐标在尾层 $t$ 的向量，
$w_{i,0}$ 是其尾真空系数。实际参数为实数时共轭自然消失。
准确成本为
$$
C_{m,2}^2
=1+2S_m+2\frac{1+|b|^2}{|a|^2}S_m^2.
\tag{8.9}
$$
即使只看这一最低新例，也必须保留真实小头系数 $a$ 的费用。

本节仅给有限孔坐标之间的同一来源关系。
它没有重建全部高孔左质量，没有支付 §5 的横向块，
也没有从每个固定 $p$ 的 $C_{m,p}\to1$ 推出对全部孔层的统一控制。
无权 $N=M$ 继续开放。

## 9. 全头 primitive 顶层的完整右旗创建观测

本节由 root 提出显式右链，boundary_resume_1cf 完整核对原旗与配对。
它承接 [原连续尾低三头观测](../results/R239-appendix-actual-continuous-tail-low-three-head-primitive-source-observation.md)，
只增加全头的投影创建观测；不重复其中 $j=1$ 的首头测试，
不登记新的全源左费用上界。

仍取本笔记 §1 的原 $m\ge5,d=2^m$、合法 $q$、实际头 $A=A_m$
和原连续尾 $D=D_m$。令
$$
K_q=\ker D\cap\mathcal H_q,\qquad \nu_m=\|D\|\le m^{-1}.
$$
现在允许整个 primitive 源子空间
$$
r\in\mathscr R_q^{\rm prim}
=\operatorname{span}\{e_0,\ldots,e_{d-2}\}\otimes K_q.
\tag{9.1}
$$
全部源 Gram 和最小费用仍在原完整源空间中定义，不先压到 (9.1)。

### 9.1 真正的左最小者仅在顶层

由于实际头严格上三角、第一条上对角线非零，
存在唯一
$$
v=\sum_{j=1}^{d-1}e_jv_j,\qquad v_j\in K_q,\qquad Av=r.
\tag{9.2}
$$
把 $v$ 只放在第 $q$ 个尾孔层。
它满足低输出方程，因为 $Dv=0$。
任意左零源 $u\in\ker E_q$ 的顶层都满足 $Au_q=0$，
故 $u_q$ 只有第零头。
因此 $v$ 与整个左零源核正交，准确有
$$
v=E_q^\dagger r,\qquad
\mu(r)^2=\sum_{j=1}^{d-1}\|v_j\|^2.
\tag{9.3}
$$

写
$$
y=J_q^{-1}r,\qquad
r^\flat=G_qy,\qquad
c^\flat=F_{\rm flag}^*y.
$$
这里 $F_{\rm flag}=F|_{\ker S}$ 是原宽度 $d$ 的完整内部核上的首源映射。
原源 Gram 定义直接给
$$
Fc^\flat=r^\flat,\qquad
c^\flat\text{ 是 }r^\flat\text{ 的完整右最小链},\qquad
\|c^\flat\|=\lambda(r^\flat).
\tag{9.4}
$$
后面只用这个完整右链，不作裸低链投影。

### 9.2 所有头坐标的显式完整零内部输出链

固定 $1\le j\le d-1$。在第 $q+j$ 孔层记
$$
P_j=P_{\ker D^d\cap\mathcal H_{q+j}},\qquad
z_j=P_j(D^*)^jv_j.
\tag{9.5}
$$
更一般地，对任意 $z\in\ker D^d\cap\mathcal H_{q+j}$ 定义右链
$$
(\mathcal K_jz)_t
=\begin{cases}
(-1)^{t-1}A^te_j\,D^{j-t}z,&1\le t\le j,\\
0,&j<t\le d.
\end{cases}
\tag{9.6}
$$

先核原联合旗。第 $t$ 段的尾孔数恰为 $q+t$；
$A^te_j$ 只含头指标 $0\le i\le j-t$。
这些指标满足原头范围 $i\le d-t$。
对于每个这样的头坐标，
$$
D^{d-i}D^{j-t}z=D^{d-i+j-t}z=0,
$$
因为 $d-i+j-t\ge d$。
所以每个分量确属原输入旗 $e_iE_{d-i,q+t}$。
这一步对全部 $j\le d-1$ 成立，正是 (9.5) 中保留投影的原因。

对 $1\le t<j$，相邻两项准确相消：
$$
A(\mathcal K_jz)_t+D(\mathcal K_jz)_{t+1}=0.
$$
最右端由 $A^{j+1}e_j=0$ 消失。故
$$
\boxed{
S\mathcal K_jz=0,\qquad F\mathcal K_jz=Ae_jD^jz.
}
\tag{9.7}
$$
源旗也可直接核验：$Ae_j$ 只含 $i\le j-1$，因而
$$
D^{d-i-1}D^jz=0.
$$
于是 (9.7) 的首源属于原完整 $\mathscr R_q$。

这条链可能含高出生分量，未证明它属于裸低链，也不声称它是某个
首源的最小原像。它属于真正的 $\ker S$ 已足以用于 (9.4)。

不同 $t$ 的输入在链直和中正交，因此其原范数准确为
$$
\|\mathcal K_jz\|^2
=\sum_{t=1}^j\|A^te_j\|^2\|D^{j-t}z\|^2.
$$
定义保留全部实际头权的有限常数
$$
\boxed{
C_{m,j}^2
=\sum_{t=1}^j\|A_m^te_j\|^2\nu_m^{\,2(j-t)}.
}
\tag{9.8}
$$
则
$$
\|\mathcal K_j\|\le C_{m,j}.
$$
若只要一个粗上界，令 $M_m=\max(1,\|A_m\|)$，利用 $\nu_m\le1$ 有
$$
C_{m,j}\le\sqrt j\,M_m^j,\qquad
\sum_{j=1}^{d-1}C_{m,j}^2
\le\sum_{j=1}^{d-1}jM_m^{2j}.
\tag{9.9}
$$
这些估计没有反演任何头小 carry。

### 9.3 保完整源 Gram 的准确配对

对 (9.7) 的源记其真正左最小原像为
$$
u=E_q^\dagger(Ae_jD^jz).
$$
其顶层满足 $Au_q=Ae_jD^jz$。
由 $\ker A=\mathbb Ce_0$，
$$
u_q=e_jD^jz+e_0u_{q,0}.
\tag{9.10}
$$
$u$ 的较低孔层一般非零，不能删除；
但它们与 (9.2) 的当前 $v$ 正交。
于是，采用本笔记第一变量线性的内积，
$$
\begin{aligned}
\langle y,F\mathcal K_jz\rangle
&=\langle v,u\rangle
=\langle v_j,D^jz\rangle\\
&=\langle (D^*)^jv_j,z\rangle
=\langle z_j,z\rangle.
\end{aligned}
\tag{9.11}
$$
另一方面，$\mathcal K_jz\in\ker S$，故
$$
\langle y,F\mathcal K_jz\rangle
=\langle c^\flat,\mathcal K_jz\rangle.
$$
因此得到原 Hilbert 空间之间的准确伴随身份
$$
\boxed{
z_j=\mathcal K_j^*c^\flat.
}
\tag{9.12}
$$
这里 $\mathcal K_j^*$ 的值域是 (9.5) 所用的实际核子空间。

结合 (9.4)、(9.8)，对每个 $1\le j\le d-1$，
$$
\boxed{
\|P_{\ker D^d\cap\mathcal H_{q+j}}(D^*)^jv_j\|
\le C_{m,j}\lambda(r^\flat).
}
\tag{9.13}
$$
所有观测同时满足
$$
\boxed{
\sum_{j=1}^{d-1}
\|P_{\ker D^d\cap\mathcal H_{q+j}}(D^*)^jv_j\|^2
\le
\left(\sum_{j=1}^{d-1}C_{m,j}^2\right)\lambda(r^\flat)^2.
}
\tag{9.14}
$$
这只是一条有明确常数的正向观测；没有将左侧反向界为 $\mu(r)^2$。

### 9.4 哪些坐标可真正去掉核投影

原纯尾的逐位交换子给
$$
\operatorname{ad}_D^3(D^*)=0.
$$
对 $(D^*)^j$ 使用乘积 Leibniz 式。
每个因子至多承受两次非零交换子，所以
$$
\operatorname{ad}_D^{2j+1}((D^*)^j)=0.
$$
又 $Dv_j=0$，因此
$$
D^{2j+1}(D^*)^jv_j=0.
\tag{9.15}
$$
当 $2j+1\le d$ 时，(9.5) 的投影在当前向量上准确为恒等，
(9.13) 遂成为
$$
\boxed{
\|(D^*)^jv_j\|
\le C_{m,j}\lambda(r^\flat),
\qquad
1\le j\le\left\lfloor\frac{d-1}{2}\right\rfloor.
}
\tag{9.16}
$$
$j=1$ 时 $Ae_1=e_0$，所以 $C_{m,1}=1$；
这正好恢复已有低三头稿的首头观测，而不是另一个新结论。

对 $2j+1>d$，本节只保 (9.13)，不删除真实投影。
对 $j\ge2$，也没有由一次的纯环境下界推出高次创建下界；
它们不是同一个受限伴随问题。

### 9.5 与原真实来源之间仍保留的缺口

本节对 (9.1) 的任意源成立，使用完整 $J_q,G_q$ 和真正 $\ker S$；
无需先把显式测试链投成裸最小者。
但一般同返回源规范的正交只在 $\ker B_A$ 上，
而 (9.6) 未证明属于该子空间。
所以不能把 (9.13) 的 $\lambda(r^\flat)$ 免费换成 $\alpha(r)$。

原实际 $w$ 的残量也未被证明属于 (9.1)。
对它投 primitive 或投某段头，不会自动保持三种源费用。
因此，本节仍未重建全左质量，未给一般源或真正 $W$ 的新 $C_m$，
也没有扩大原合法 lift 窗。

## 10. 原大头上的创建观测不能单独重建左质量

本节继续 §9 的原模型、原 Hilbert 范数和原合法窗口。
它给的是 §9 所读观测的定量障碍，不是三 Gram 不等式的反例。
特别，下面不估计所构造源的 $\alpha(r)$ 或 $\lambda(r^\flat)$ 的上界，
也不把它认成真实 $w\in M\ominus N$ 的源。

### 10.1 同一个 primitive 向量的全部高次创建

令 $q\ge1$，取实际尾前缀
$$
I=[m,m+2q),\qquad J=m+2q.
$$
[原权 Vandermonde 稿](../results/R239-appendix-vandermonde-coprimitive-short-kernel-counterexamples.md)
§§2–5 给一个非零 $q$ 孔向量 $X$，满足
$$
D_I^*X=0,\qquad D_I^2X=0.
$$
令 $\mathcal C_Ie_S=e_{I\setminus S}$ 为这个有限前缀上的物理补集酉算子。
它与原权的准确关系是
$$
\mathcal C_ID_I\mathcal C_I=D_I^*.
$$
因此
$$
g_{m,q}
=\frac{\mathcal C_IX}{\|X\|}\otimes\Omega_{[J,\infty)}
$$
为同一实际尾中的单位 $q$ 孔向量，且
$$
\boxed{
D_mg_{m,q}=0,\qquad
(D_I^*)^2\mathcal C_IX=0.
}
\tag{10.1}
$$
补集只作用于这有限的 $2q$ 位；没有在整个无限真空参考空间上使用无限补集。

置
$$
a_{m,q}=\|D_I^*(\mathcal C_IX/\|X\|)\|^2\le\nu_m^2,
\qquad
S_J=\sum_{\ell\ge J}(\ell+1)^{-4}.
$$
记 $e_k^{(J)}$ 为非负数列 $((\ell+1)^{-4})_{\ell\ge J}$ 的第 $k$ 个初等对称函数，
$e_0^{(J)}=1$。
远尾真空的准确创建范数是
$$
\|(D_J^*)^k\Omega\|^2=(k!)^2e_k^{(J)}.
$$
由 (10.1)，前缀创建至多出现一次。二项展开的两项具有不同前缀孔数，
因而正交。对同一个 $g_{m,q}$ 和全部 $k\ge1$，
$$
\boxed{
\|(D_m^*)^kg_{m,q}\|^2
=(k!)^2\left(e_k^{(J)}+a_{m,q}e_{k-1}^{(J)}\right).
}
\tag{10.2}
$$
利用 $e_k^{(J)}\le S_J^k/k!$，得到
$$
\boxed{
\|(D_m^*)^kg_{m,q}\|^2
\le k!\,S_J^{k-1}(S_J+k\nu_m^2).
}
\tag{10.3}
$$

$k=1$ 的完整创建仍受原纯尾环境 gap 约束；
(10.1) 的 primitive 性并不使这个首阶范数趋零。
但是对每个固定 $m$ 和固定 $k\ge2$，
(10.3) 随 $q\to\infty$ 趋零。
所以一次 primitive 创建的环境下界不能迭代为高次创建下界。
下面不使用固定 $m$ 的无限 $q$ 极限，而选原许可的具体 $q$。

### 10.2 原真实头内的两个 dyadic 列

仍记原
$$
b_n=(n+1)^{-2},\qquad
\eta_n=\alpha_{n+1}/\alpha_n,\qquad
-\log\eta_n=1400\,16^n-630\,8^n+300\,2^n.
$$
对 $1\le n<m$，原 $N$ 头在单一 dyadic 基向量上的准确式为
$$
A_{N,m}e_{2^n}
=b_ne_0+\sum_{i<n}b_i\frac{\alpha_n}{\alpha_i}e_{2^n-2^i}.
\tag{10.4}
$$
这是原加权后移跨越 $2^n$ 时的权比：
与长度 $2^i$ 的标准归一化权积相比，只把末端的 $\alpha_i$ 换成 $\alpha_n$。
因为 $\alpha_i$ 递减，
$$
\left\|A_{N,m}e_{2^n}-b_ne_0\right\|
\le2\eta_{n-1}.
$$

$Y$ 头的第 $i<n$ 项是
$N_i^{[m]}(I+N_i^{[m]})^{-1}$。
实际归一化权积满足 $d_{i+1}/d_i^2=\eta_i$；
因此 $i+1<m$ 时有准确恒等式
$(N_i^{[m]})^2=\eta_iN_{i+1}^{[m]}$，最顶位的平方则为零。
原有限加权后移的每个归一化区间权积至多为一，故
$
\|N_i^{[m]}\|\le1,\qquad
\|(N_i^{[m]})^2\|\le\eta_i<1/3.
$
用 $(I+N_i^{[m]})^{-1}=(I-N_i^{[m]})(I-(N_i^{[m]})^2)^{-1}$，
其逆范数小于三。
它与 $N_i^{[m]}$ 交换，故作用于 $e_{2^n}$ 的范数至多
$3\alpha_n/\alpha_i$。
第 $i=n$ 项仍准确给 $e_0$，因为它在该向量上平方为零。
因此两个实际头统一满足
$$
\boxed{
A_me_{2^n}=b_ne_0+\varepsilon_{m,n},
\qquad
\|\varepsilon_{m,n}\|\le6\eta_{n-1}.
}
\tag{10.5}
$$
在 $Y$ 模型中，低位 Cayley 高次也可贡献一个极小的 $e_0$ 坐标；
它已经包括在 $\varepsilon_{m,n}$ 中，未被省略。

取
$$
n=m-2,\qquad p=2^n=d/4,\qquad
h_m=\frac{b_{n+1}e_p-b_ne_{2p}}
{\sqrt{b_n^2+b_{n+1}^2}}.
\tag{10.6}
$$
其范数为一，第一头坐标为零。两列主项恰相消，故
$$
\boxed{\|A_mh_m\|\le12\eta_{m-3}.}
\tag{10.7}
$$
对本节的 $n=m-2,m-1$，$m\ge5$ 及原显式 $\eta$ 还给
$6\eta_{n-1}\le b_n/2$。
例如在最小 $n=3$ 已有巨大余量，随后 $\eta_{n-1}$ 至少按十六次幂下降，
而 $b_n$ 只按平方下降。
所以 (10.5) 给
$$
\|A_me_{2^n}\|\ge b_n/2.
\tag{10.8}
$$
这个保守常数同时适用于 $N/Y$ 两头。

### 10.3 原合法窗口与真实左最小源

令
$$
q_m=\left\lfloor e^{d^3/4}\right\rfloor.
\tag{10.9}
$$
$m\ge5$ 时它满足 $4d\le q_m\le e^{d^3/4}$。
取 (10.1) 中同一个 $g=g_{m,q_m}$，并置
$$
v_m=h_m\otimes g,\qquad r_m=A_mv_m.
\tag{10.10}
$$
该源属于原完整 primitive 子空间 (9.1)。
由 §9.1 的完整左最小性，
$$
\boxed{
v_m=E_{q_m}^\dagger r_m,\qquad
\mu(r_m)=1,\qquad
\|r_m\|\le12\eta_{m-3}.
}
\tag{10.11}
$$
这里只给实际有限头模型的真实左源；没有认定它来自原 $W$。

令 $z_{m,j}=P_j(D_m^*)^j(v_m)_j$ 为 §9 的全部观测，
并保留其实际常数 $C_{m,j}$。
只有 $j=p,2p$ 可能非零。
从 (9.8) 的 $t=1$ 项和 (10.8)，
$$
C_{m,2^n}\ge \frac{b_n}{2}\nu_m^{\,2^n-1}
\quad(n=m-2,m-1).
\tag{10.12}
$$
而实际单孔真空测试给 $\nu_m\ge b_m=(m+1)^{-2}$。
故由 (10.3)，对 $j=p,2p$，
$$
\boxed{
\frac{\|z_{m,j}\|^2}{C_{m,j}^2}
\le
4b_{\log_2j}^{-2}\,j!
\left(\frac{S_{m+2q_m}}{\nu_m^2}\right)^{j-1}
(S_{m+2q_m}+j\nu_m^2).
}
\tag{10.13}
$$
$j=p$ 的投影由 §9.4 本来就是恒等；
$j=2p=d/2$ 的投影仍保留，(10.13) 只使用投影收缩性。

### 10.4 这个观测系统所需的费用已超过原窗口

对 $m\ge5$，
$2q_m\ge e^{d^3/4}$，因此原积分界给
$$
S_{m+2q_m}\le\frac13e^{-3d^3/4}.
$$
结合 $\nu_m^{-2}\le(m+1)^4$，有
$$
\log\left(\frac{S_{m+2q_m}}{\nu_m^2}\right)
\le-\frac34d^3+4\log(m+1)-\log3.
\tag{10.14}
$$
在 (10.13) 中用 $j!\le j^j$ 及 $j\le d/2$，
所有其余因子的对数均为 $O(d\log d+d\log(m+1))$。
最慢衰减的是 $j=p=d/4$。
所以
$$
\limsup_{m\to\infty}\frac1{d^4}
\log\left(\sum_{j=1}^{d-1}
\frac{\|z_{m,j}\|^2}{C_{m,j}^2}\right)
\le-\frac3{16}.
\tag{10.15}
$$

另一方面，(10.7) 的原 carry 不是自由参数，而是准确给
$$
2\log\eta_{m-3}
=-\frac{175}{256}d^4+\frac{315}{128}d^3-75d.
\tag{10.16}
$$
因此若定义本节仅用于辨别观测信息的量
$$
\mathfrak o_m(v)
=\|A_mv\|^2+
\sum_{j=1}^{d-1}
\frac{\|P_{\ker D_m^d}(D_m^*)^jv_j\|^2}{C_{m,j}^2},
$$
便得到实际原头、实际原连续尾、实际合法 $q_m$ 上的结论
$$
\boxed{
\mu(r_m)^2=1,\qquad
\limsup_{m\to\infty}d^{-4}\log\mathfrak o_m(v_m)
\le-\frac3{16}.
}
\tag{10.17}
$$
若有仅由这组观测重建左质量的常数
$$
\mu(Av)^2\le B_m\,\mathfrak o_m(v)
$$
对全部顶层 primitive 源成立，那么必有
$$
\boxed{
\liminf_{m\to\infty}d^{-4}\log B_m\ge\frac3{16}.
}
\tag{10.18}
$$
这里 $B_m$ 是平方不等式的常数。
若改写为范数不等式 $\mu(Av)\le b_m^{\rm obs}\sqrt{\mathfrak o_m(v)}$，
对应必要条件是
$
\liminf_{m\to\infty}d^{-4}\log b_m^{\rm obs}\ge\frac3{32}.
$
这样的观测常数不能由原同头窗口数
$O(e^{d^3/4}/d)$ 支付。

此外，$\mathfrak o_m$ 明确使用 §9 的已付上界 $C_{m,j}$。
本节没有把 $C_{m,j}$ 认成 $\mathcal K_j$ 的最优算子范数，
也没有穷尽所有可另行优化的完整右链测试。

最后明确逻辑方向：
§9 给的是每个观测由 $\lambda(r^\flat)$ 控制，
并没有给反向控制。
(10.17) 中小的是这些已读到的观测及源的普通范数；
没有证明 $\alpha(r_m)$ 或 $\lambda(r_m^\flat)$ 小。
所以本节排除的是“只依靠这些量，再作一个温和反向观测”的路线，
不是一般三 Gram 比较、实际来源比较或 $N=M$。
还须继续识别完整右最小链中没有被本节读取的能量。

## 11. 同一原模型源的完整右费用很小，而平坦源费用很大

本节继续 §10 的同一组源，不改头权、尾权、孔数或 Hilbert 范数。
root 提出用远尾相容原像支付完整右链；下面给出真空特例的明确公式、
原联合旗检查和全部费用。
结果说明 §10 小观测没有读到的能量确实存在于完整平坦源费用中。
这里仍不把所构造的源认作真实 $w\in M\ominus N$ 的残量。

### 11.1 同一远尾块上的相容真空原像

取 §10 的
$$
d=2^m,\quad m\ge5,\quad
q=\left\lfloor e^{d^3/4}\right\rfloor,\quad
J=m+2q,\quad T=d/2.
$$
原连续尾的权仍为 $b_j=(j+1)^{-2}$。
写
$$
\psi=\mathcal C_IX/\|X\|,\qquad
I=[m,J),\qquad D_I\psi=0,\qquad \|\psi\|=1,
$$
所以 §10 的 $g$ 就是 $\psi\otimes\Omega_{[J,\infty)}$。

在与 $I$ 不交的有限块
$$
B=[J,2J)
$$
上，令 $(J)_{\underline t}=J(J-1)\cdots(J-t+1)$，
并对 $0\le t\le T$ 定义
$$
\xi_t=
\frac1{(J)_{\underline t}}
\sum_{\substack{S\subset B\\ |S|=t}}
\left(\prod_{j\in S}b_j^{-1}\right)e_S,
\qquad \xi_0=\Omega_B.
\tag{11.1}
$$
这里 $B$ 恰有 $J$ 位，且 $J\ge2T$。

对任一 $(t-1)$ 元子集 $R\subset B$，
$D_B\xi_t$ 在 $e_R$ 上的系数为
$$
\frac{J-t+1}{(J)_{\underline t}}
\prod_{j\in R}b_j^{-1}.
$$
因此不是近似而是准确有
$$
D_B\xi_t=\xi_{t-1}\quad(1\le t\le T).
\tag{11.2}
$$
若写 $C_B=\sum_{j\in B}b_j^{-1}E_j^*$，
则 $\xi_t=C_B^t\Omega_B/[t!(J)_{\underline t}]$。
这是 [R254 相容多次原像](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)
§§1–3 在零孔输入上的同一有限辅助头机制；
本节直接核 (11.2)，不把原 $q$ 孔向量代入该稿的全层粗范数。

所有 $b_j^{-1}\le4J^2$，故
$$
\begin{aligned}
\|\xi_t\|^2
&=\frac1{(J)_{\underline t}^2}
\sum_{\substack{S\subset B\\|S|=t}}\prod_{j\in S}b_j^{-2}\\
&\le
\frac{16^tJ^{4t}}{t!(J)_{\underline t}}
\le\frac{32^tJ^{3t}}{t!}.
\end{aligned}
\tag{11.3}
$$
最后一步使用 $t\le T\le J/2$。
于是对同一组相容原像，
$$
\boxed{
\|\xi_t\|\le\frac{(4\sqrt2\,J^{3/2})^t}{\sqrt{t!}}.
}
\tag{11.4}
$$

把它们放回原连续尾：
$$
g_t=\psi\otimes\xi_t\otimes\Omega_{[2J,\infty)}.
$$
则
$$
g_0=g,\qquad
D_mg_t=g_{t-1},\qquad
D_m^{t+1}g_t=0,\qquad
g_t\in\mathcal H_{q+t},\qquad
\|g_t\|=\|\xi_t\|.
\tag{11.5}
$$
这里 $D_I\psi=0$ 支付了完整 $D_m$ 的前缀项；
没有把只在远尾成立的相容式当作全尾相容式。

### 11.2 原完整右旗内的零内部输出链

保持 §10 的 $h=h_m$，
其头支撑为 $\{d/4,d/2\}$，并写
$$
u=A_mh,\qquad r_m=u\otimes g,\qquad A=A_m.
$$
在原宽度 $d$ 的右链中取
$$
c_t=
\begin{cases}
(-1)^{t-1}A^{t-1}u\otimes g_t,&1\le t\le T,\\
0,&T<t\le d.
\end{cases}
\tag{11.6}
$$

核对原联合旗时，$A^{t-1}u=A^th$ 只含头指标
$$
0\le i\le T-t.
$$
这些指标满足原头范围 $i\le d-t$。
另一方面，由 (11.5)，$g_t\in\ker D^{t+1}$，而
$$
d-i\ge d-T+t=T+t\ge t+1.
$$
所以每个头坐标都在原输入旗
$e_iE_{d-i,q+t}$ 内。
源 $r_m$ 的尾向量为 primitive，头指标至多 $T-1$，
也在原源旗 $\mathscr R_q$ 内。

相容式 (11.5) 逐段给
$$
Ac_t+Dc_{t+1}=0\quad(1\le t<T).
$$
末端为
$$
Ac_T=(-1)^{T-1}A^{T+1}h\otimes g_T=0,
$$
因为实际头严格上三角且 $h$ 的最高指标为 $T$。
首源则为 $Dc_1=r_m$。因此
$$
\boxed{Sc=0,\qquad Fc=r_m.}
\tag{11.7}
$$
这是原完整内部核中的合法链。
这里不要求它等于最小链，也不投影成裸低链。
其输出孔数只到 $q+T$，仍在原宽度 $d$ 中；
并且 $q+T<e^{d^3/3}$，没有扩大已有 lift 窗。

### 11.3 原 carry 压住远尾原像的全部增长

由 §10.2，两个实际头均可使用
$$
\|A_m\|<6.
$$
具体地，$N$ 头由 $\|N_i^{[m]}\|\le1$ 和 $\sum_i b_i<2$ 得到；
$Y$ 头再用 $\|(I+N_i^{[m]})^{-1}\|<3$ 即得同一界。
各 $c_t$ 位于互相正交的链段，故
$$
\begin{aligned}
\|c\|^2
&=\sum_{t=1}^T\|A^{t-1}u\|^2\|g_t\|^2\\
&\le \|u\|^2\sum_{t=1}^T
6^{2t-2}\frac{(32J^3)^t}{t!}.
\end{aligned}
\tag{11.8}
$$
不需要最优求和。用 (10.7) 并放大每项即有
$$
\boxed{
\lambda(r_m)\le\|c\|
\le\varepsilon_m
:=12\sqrt T\,6^{T-1}
(4\sqrt2\,J^{3/2})^T\eta_{m-3}.
}
\tag{11.9}
$$

这里 $J\le3e^{d^3/4}$，而原 carry 的对数准确为
$$
\log\eta_{m-3}
=-\frac{175}{512}d^4+\frac{315}{256}d^3-\frac{75}{2}d.
$$
代入 $T=d/2$，得到
$$
\begin{aligned}
\log\varepsilon_m
\le{}&
-\frac{79}{512}d^4+\frac{315}{256}d^3-\frac{75}{2}d\\
&+\frac d2\left(\log(24\sqrt2)+\frac32\log3\right)
+\log2+\frac12\log(d/2).
\end{aligned}
\tag{11.10}
$$
第二行连同 $-75d/2$ 为负：例如 $\log(24\sqrt2)<4$、$\tfrac32\log3<2$，且 $\log2+\tfrac12\log(d/2)<d$，已给严格负上界。对全部 $m\ge5$，$d\ge32$，于是
$$
\boxed{
\lambda(r_m)
\le
\exp\!\left(-\frac{79}{512}d^4+\frac{315}{256}d^3\right)
\le e^{-d^4/9}.
}
\tag{11.11}
$$
最后一步只用
$79/512-315/(256d)\ge949/8192>1/9$。
特别，
$$
\limsup_{m\to\infty}d^{-4}\log\lambda(r_m)
\le-\frac{79}{512}.
\tag{11.12}
$$

### 11.4 同一个真实平坦源承担遗漏的能量

继续使用原完整源 Gram，而不是压缩到 primitive 子空间：
$$
y_m=J_q^{-1}r_m,\qquad
r_m^\flat=G_qy_m,\qquad
c_m^\flat=F_{\rm flag}^*y_m.
$$
由 §9.1，$\langle r_m,J_q^{-1}r_m\rangle=\mu(r_m)^2=1$；
由 §9.3，$\|c_m^\flat\|=\lambda(r_m^\flat)$。
对 (11.7) 的合法完整链，第一变量线性的内积给
$$
1=\langle r_m,y_m\rangle
=\langle c,c_m^\flat\rangle.
\tag{11.13}
$$
直接用 (11.9) 的显式链即可推出
$$
\boxed{
\lambda(r_m^\flat)\ge\varepsilon_m^{-1}\ge e^{d^4/9}.
}
\tag{11.14}
$$
若改用 $r_m$ 的完整最小链，则得到同源的准确比较
$$
\mu(r_m)^2\le\lambda(r_m)\lambda(r_m^\flat).
\tag{11.15}
$$
因此还保留较尖的渐近下界
$$
\boxed{
\liminf_{m\to\infty}d^{-4}\log\lambda(r_m^\flat)
\ge\frac{79}{512}.
}
\tag{11.16}
$$
以上是范数费用；相应平方费用的指数加倍。

所以，§10 的同一组原模型源满足：左最小费用为一，
普通源范数和该节的归一化高创建观测都很小，
完整右最小费用也很小，但完整平坦源费用很大。
§10 的小观测没有读到 (11.14) 的真实能量。
这组源因此不反驳保留 $\lambda(r^\flat)$ 的三 Gram 比较。

本节只为原完整右链给出了明确上界，
没有凭显式链免费替换裸最小者或同返回源规范。
也没有认定 $r_m$ 为实际 $W$ 向量的来源，
没有关闭原高孔横向观测或 $N=M$。

## 12. 有限前缀 primitive 子空间上的完整头矩阵观测

本节把 §11 的单个测试链作线性合并。
它给出任意原源的一项准确正能量，保留所有头坐标混合；
不把顶层观测当作整个左最小费用。

### 12.1 真实测试空间和完整右链

固定原合法 $m,d,q$，取整数
$$
1\le T\le d-1,\qquad J\ge m+2q,\qquad J\ge2T.
$$
记
$$
I=[m,J),\qquad B=[J,2J),\qquad
\mathcal K=\ker D_I\cap\mathcal H_q(I),\qquad
H_T=\operatorname{span}\{e_1,\ldots,e_T\}.
$$
$\mathcal K$ 总是用远尾真空嵌入原连续尾。
令
$$
\mathcal U=H_T\otimes\mathcal K
$$
嵌入左链的顶层 $q$，其余尾孔层为零；
$P_{\mathcal U}$ 表示这个原物理子空间上的正交投影。

取 §11.1 在同一 $B$ 上的 $\xi_t$，并置
$$
V_t\psi=\psi\otimes\xi_t\otimes\Omega_{[2J,\infty)}.
$$
则 $DV_t=V_{t-1}$、$D^{t+1}V_t=0$，且
$$
V_t^*V_t=\omega_t I_{\mathcal K},\qquad
\omega_t=\|\xi_t\|^2
=\frac{e_t(((j+1)^4)_{J\le j<2J})}{(J)_{\underline t}^2}.
\tag{12.1}
$$
这里的初等对称函数只含真实有限块 $B$ 的权。

定义 $\mathcal C_T:\mathcal U\longrightarrow\mathscr C_q$ 为
$$
(\mathcal C_Tu)_t=
\begin{cases}
(-1)^{t-1}(A^t\otimes V_t)u,&1\le t\le T,\\
0,&T<t\le d.
\end{cases}
\tag{12.2}
$$
式中 $A^t$ 作用头，$V_t$ 作用 $\mathcal K$；
允许 $u$ 是一般头尾纠缠向量，不要求是单个张量。

原联合旗的检查与 §11.2 相同，但这里允许全部 $T\le d-1$：
第 $t$ 段头指标 $i\le T-t$，尾高度至多 $t+1$，并且
$$
d-i\ge d-T+t\ge t+1.
$$
所以全部分量都在 $e_iE_{d-i,q+t}$。
逐段相容及末端 $A^{T+1}|_{H_T}=0$ 给
$$
\boxed{
S\mathcal C_T=0,\qquad F\mathcal C_Tu=Au.
}
\tag{12.3}
$$
每个 $u\in\mathcal U$ 本身都是 $Au$ 的真正左最小原像：
它只在顶层、尾向量 primitive、头没有 $e_0$；
任一左零源顶层都只有 $e_0$。
因此
$$
E_q^\dagger(Au)=u.
\tag{12.4}
$$

### 12.2 原有限头 Gram 和精确能量

各右链段正交，(12.1) 遂给准确身份
$$
\boxed{
\mathcal C_T^*\mathcal C_T=\mathsf B_T(J)\otimes I_{\mathcal K},
\qquad
\mathsf B_T(J)
=\sum_{t=1}^T
\omega_t\,(A^t|_{H_T})^*(A^t|_{H_T}).
}
\tag{12.5}
$$
这是 $T$ 维头空间上的实际正矩阵。
$\omega_1>0$，而 $A|_{H_T}$ 单射，所以 $\mathsf B_T(J)>0$。
不把不同 $t$ 的头 Gram 认作可交换，也不使用 Jordan 相似来改变范数。

现在允许 $r$ 是任意原完整源，未要求它 primitive。
写
$$
v=E_q^\dagger r,\qquad
y=J_q^{-1}r,\qquad
r^\flat=G_qy,\qquad
c^\flat=F_{\rm flag}^*y.
$$
对任一 $u\in\mathcal U$，由 (12.3)–(12.4)，
$$
\begin{aligned}
\langle c^\flat,\mathcal C_Tu\rangle
&=\langle y,Au\rangle
=\langle v,E_q^\dagger(Au)\rangle\\
&=\langle v,u\rangle
=\langle P_{\mathcal U}v_q,u\rangle.
\end{aligned}
$$
因此
$$
\boxed{\mathcal C_T^*c^\flat=P_{\mathcal U}v_q.}
\tag{12.6}
$$
此处 $v$ 的较低孔层没有被删掉；
它们只是与当前顶层测试空间 $\mathcal U$ 正交。

令
$$
\mathcal W_T=\mathcal C_T
(\mathsf B_T(J)^{-1/2}\otimes I_{\mathcal K}).
$$
由 (12.5)，$\mathcal W_T$ 是原 Hilbert 范数中的等距嵌入。
于是
$$
\boxed{
\begin{aligned}
\|P_{\operatorname{Ran}\mathcal C_T}c^\flat\|^2
&=
\left\|
(\mathsf B_T(J)^{-1/2}\otimes I_{\mathcal K})
P_{\mathcal U}v_q
\right\|^2\\
&\le\lambda(r^\flat)^2.
\end{aligned}
}
\tag{12.7}
$$
第一行是准确的正交投影能量。
它读取整个头矩阵，而不是先逐坐标用上界 $C_{m,j}$ 再求和。
$\mathcal C_T$ 仍只是一个显式完整右链族，未被认作最小链族。

### 12.3 §11 的近核头给任意源的一项小投影

取 §11 的 $q=q_m,\ J=m+2q_m,\ T=d/2$ 和单位 $h_m$。
对于任意单位 $\psi\in\mathcal K$，
§11 的同一个原范数预算给
$$
\|\mathcal C_T(h_m\otimes\psi)\|\le\varepsilon_m,
$$
其中 $\varepsilon_m$ 是 (11.9) 的明确量。
所以 (12.6) 对任意原源 $r$ 都给
$$
\boxed{
\left\|
P_{\mathcal K}(h_m^*\otimes I)v_q
\right\|
\le\varepsilon_m\,\lambda(r^\flat)
\le e^{-d^4/9}\lambda(r^\flat).
}
\tag{12.8}
$$
$P_{\mathcal K}$ 在这里包含远尾真空嵌入的正交投影。
这个结论不要求原 $r$ 为 §10 的特定源，
也不要求 $v$ 自身只占顶层。
若 $r$ 是已有 $\lambda(r^\flat)$ 预算的真实来源，
可直接代入该旧预算，没有换成另一个来源。

对整个特殊子空间 $v=h_m\otimes\mathcal K$，
(11.9) 与同源配对还同时给
$$
\lambda(Av)\le\varepsilon_m\|v\|,
\qquad
\lambda((Av)^\flat)\ge\varepsilon_m^{-1}\|v\|.
\tag{12.9}
$$
因此 §11 的正向说明并不依赖 Vandermonde 向量的额外高创建性质；
那一性质只用于 §10 证明旧观测确实很小。

### 12.4 尚未支付的部分

(12.7) 是完整平坦链内一个已识别的正交分量。
它没有支付该投影的正交补，也没有给
$\mathsf B_T(J)$ 的温和统一谱比较。
即使取 $T=d-1$，有限前缀 primitive 投影仍不能随意移过左最小逆；
$v$ 的较低孔层也可能承载左费用。

所以本节增加的是合法的矩阵观测和任意真实源上的 (12.8)，
不是全左质量重建、裸最小者识别或 $N=M$。

## 13. 跨原边界切开的有限核给出低孔整体矩阵观测

本节把 §12 的测试沿所有左孔层同时放置。
通过原边界 $q$ 切开同一个有限 $L=A+D$ 核，左、右部分的配对准确相消。
不同前缀孔数和辅助块孔数的双重正交使合并费用不随 $q$ 增长。
这次读取的是左最小者在所有低孔层上的一个实际投影，
仍不是完整左质量。

### 13.1 同一有限前缀和全部 primitive 左孔层

固定 §12 的原 $m,d,q$、
$1\le T\le d-1$ 以及 $J\ge m+2q,\ J\ge2T$。
仍取
$$
I=[m,J),\qquad B=[J,2J),\qquad
H_T=\operatorname{span}\{e_1,\ldots,e_T\}.
$$
现在令
$$
\mathcal K_{\le q}(I)
=\bigoplus_{n=0}^q\bigl(\ker D_I\cap\mathcal H_n(I)\bigr),
\qquad
\mathcal U=H_T\otimes\mathcal K_{\le q}(I)
\otimes\Omega_{[J,\infty)}.
\tag{13.1}
$$
这是原物理空间的子空间，全部位于尾孔数不超过 $q$ 的部分。
不对原源或左最小逆先作 primitive 截断。

取 §11.1 同一块 $B$ 上的相容向量 $\xi_t$，
记 $\xi_0=\Omega_B$ 和 $\omega_t=\|\xi_t\|^2$。
对于
$u_n\in H_T\otimes(\ker D_I\cap\mathcal H_n(I))$，
在物理孔层中定义
$$
\mathcal Z_nu_n
=\sum_{t=0}^T(-1)^t
(A^t\otimes V_t)u_n,
\qquad
V_t\psi=\psi\otimes\xi_t\otimes\Omega_{[2J,\infty)}.
\tag{13.2}
$$
第 $t$ 项的总尾孔数为 $n+t$。
这里 $D_I\psi=0$、$D_B\xi_t=\xi_{t-1}$，
所以相邻两项的 $A$ 与 $D$ 输出准确相消。
最左端 $D_Iu_n=0$，最右端 $A^{T+1}|_{H_T}=0$。
于是
$$
\boxed{L\mathcal Z_nu_n=0.}
\tag{13.3}
$$
该向量只占孔层 $[n,n+T]$。

令 $\mathcal Z=\sum_{n=0}^q\mathcal Z_n$，
并把 (13.1) 的自然物理嵌入写为 $\iota$。
定义
$$
\mathcal C=\mathcal Z-\iota.
\tag{13.4}
$$
$\mathcal C$ 只含 (13.2) 的 $t\ge1$ 项。
不同的 $(n,t)$ 具有不同的前缀 $I$ 孔数 $n$
或辅助块 $B$ 孔数 $t$，因而在原物理 Hilbert 空间中正交；
即使总孔数 $n+t$ 相同，也仍正交。
所以
$$
\boxed{
\mathcal C^*\mathcal C=\mathsf B_T(J)\otimes I_{\mathcal K_{\le q}(I)},
\qquad
\iota^*\mathcal C=0,
}
\tag{13.5}
$$
其中 $\mathsf B_T(J)>0$ 正是 (12.5) 的完整头矩阵。
特别没有把 $q+1$ 个孔层的范数作三角求和，
也没有产生一个链长重叠因子。

### 13.2 在原 $q$ 边界切开后的全部域

对每个 (13.2) 写
$$
z^- =P_{\le q}\mathcal Z_nu_n,\qquad
z^+ =P_{>q}\mathcal Z_nu_n.
$$
若 $n+T\le q$，则 $z^+=0$，
整个 $z^-$ 是原左零源核。

一般情形下，由 (13.3)，
$$
P_{<q}Lz^-=0.
$$
所以 $z^-\in V_q$，其原首源为 $E_qz^-=Az^-_q$。
下面核 $z^+$ 确属原完整右旗，而非只是环境高孔向量。

令 $s=q-n\ge0$。
落在右段 $k\ge1$ 的项来自 $t=s+k\le T$；
其头指标及纯尾核阶满足
$$
i\le T-t=T-s-k,\qquad
D^{t+1}(A^t\otimes V_t)u_n=0.
$$
因此
$$
i\le d-k,\qquad
d-i\ge d-T+t\ge t+1.
$$
这正好支付原第 $k$ 段的输入旗 $e_iE_{d-i,q+k}$。

左源若非零，来自 $Az^-_q$，其头指标至多 $T-s-1$，
尾高度至多 $s+1$；从而
$$
d-i-1\ge d-T+s\ge s+1.
$$
故它也在原完整源旗 $\mathscr R_q$ 中。
再用 (13.3) 在边界及全部右输出层的等式，得到
$$
\boxed{
z^+\in\ker S,\qquad
E_qz^-+Fz^+=0.
}
\tag{13.6}
$$
其最右孔层至多为 $q+T\le q+d-1$，
始终在原宽度 $d$ 之内。

这一步也说明 $\mathcal C$ 本身不必分别落在左旗或右旗；
真正被切成合法两部分的是完整 $\mathcal Z$。
后面的物理正交投影允许作用于环境有限窗，
不把 $\mathcal C$ 冒充某一边的最小原像。

### 13.3 任意原源的准确双侧正能量

取任意原源 $r\in\mathscr R_q$，仍用完整源 Gram：
$$
y=J_q^{-1}r,\qquad
v=E_q^\dagger r=E_q^*y,\qquad
r^\flat=G_qy,\qquad
c^\flat=F_{\rm flag}^*y.
$$
把左向量 $v$ 放在物理孔层 $\le q$，
把右链 $c^\flat$ 放在孔层 $q+1,\ldots,q+d$，
记其物理正交和为
$$
x=v+c^\flat.
$$
两部分按尾孔数正交，所以
$$
\|x\|^2=\mu(r)^2+\lambda(r^\flat)^2.
\tag{13.7}
$$
由 (13.6)，对每个 $u\in\mathcal U$，
$$
\begin{aligned}
\langle x,\mathcal Zu\rangle
&=\langle v,z^-\rangle+\langle c^\flat,z^+\rangle\\
&=\langle y,E_qz^-+Fz^+\rangle=0.
\end{aligned}
$$
于是，令 $p=P_{\mathcal U}v=\iota^*x$，有
$$
\boxed{\mathcal C^*x=-p.}
\tag{13.8}
$$
这是任意原源的准确关系，未把它换成相邻源或 primitive 源。

由 (13.5)，
$\mathcal C(\mathsf B_T(J)^{-1/2}\otimes I)$
是原物理空间内的等距嵌入。
其像与 $\mathcal U$ 正交。
因此 (13.8) 不仅给上界，还给准确的两项正交能量：
$$
\boxed{
\begin{aligned}
\mu(r)^2+\lambda(r^\flat)^2
={}&\|p\|^2+
\|(\mathsf B_T(J)^{-1/2}\otimes I)p\|^2\\
&+\|P_{(\mathcal U\oplus\operatorname{Ran}\mathcal C)^\perp}x\|^2.
\end{aligned}
}
\tag{13.9}
$$
特别，
$$
\boxed{
\|(\mathsf B_T(J)^{-1/2}\otimes I)P_{\mathcal U}v\|^2
\le
\mu(r)^2+\lambda(r^\flat)^2-\|P_{\mathcal U}v\|^2.
}
\tag{13.10}
$$
这里已经包含 $v$ 的全部 $0,\ldots,q$ 孔层，
但保留有限前缀 primitive 和具体头空间的实际投影。

### 13.4 原近核头在整个低孔部分上的小投影

继续取 §11 的
$$
q=q_m,\quad J=m+2q_m,\quad T=d/2,\quad h=h_m.
$$
把上面的测试空间限制为
$$
\mathcal U_h
=\mathbb Ch_m\otimes\mathcal K_{\le q_m}([m,J))
\otimes\Omega_{[J,\infty)}.
$$
限制后的 $\mathcal C_h$ 的准确 Gram 是标量
$$
\mathcal C_h^*\mathcal C_h=\beta_m I,\qquad
\beta_m=\sum_{t=1}^T\omega_t\|A_m^th_m\|^2
\le\varepsilon_m^2,
\tag{13.11}
$$
其中 $\varepsilon_m$ 是 (11.9) 已付的明确量。
$\beta_m>0$，因为实际 $A_mh_m\ne0$。

对 $p_h=P_{\mathcal U_h}v$ 重复 (13.9)，得到
$$
\left(1+\beta_m^{-1}\right)\|p_h\|^2
\le\mu(r)^2+\lambda(r^\flat)^2.
$$
从而对每一个原源 $r$，
$$
\boxed{
\|P_{\mathcal U_h}v\|^2
\le
\frac{\varepsilon_m^2}{1+\varepsilon_m^2}
\left(\mu(r)^2+\lambda(r^\flat)^2\right)
\le
e^{-2d^4/9}
\left(\mu(r)^2+\lambda(r^\flat)^2\right).
}
\tag{13.12}
$$
这不是只在第 $q$ 层的 (12.8)：
它控制同一个近核头在所有低孔层上的有限前缀 primitive 投影，
合并时没有 $q$ 或 $T$ 倍费用。

若 $r$ 是已有完整平坦源预算的真实来源，
(13.12) 可直接使用原来的 $\mu(r)$ 与 $\lambda(r^\flat)$。
本节未从普通源范数推测该预算，也未改变真实来源。

### 13.5 尚未覆盖的左质量

(13.9) 留有明确的正交补能量。
一般 $v$ 不必在 $\mathcal U_h$，甚至不必在
$H_T\otimes\mathcal K_{\le q}(I)$；
有限前缀 primitive 投影及远尾真空投影都不能免费删去。
当前只有这些具体近核头方向得到小量，
没有证明这族方向覆盖原左质量。

所以本节支付了一个实际低孔整体观测接口，
但没有给温和的全头谱比较、一般三 Gram 上界或 $N=M$。

## 14. 相容原像的 primitive 正规化与全尾低孔观测

本节保留 §13 的同一个原来源和近核头，
用原 R254 相容多次原像替换有限辅助块的真空原像。
关键是一个精确正规化：先减去各阶 primitive 输出，
得到顺次最小原像，同时仍只付线性阶数的范数。
因此下面的低孔观测不再需要有限前缀或远尾真空投影。

### 14.1 一次构造的相容多次原像

仍取原 $D=D_m=\sum_{j\ge m}(j+1)^{-2}E_j$。
给定原 $q$ 和 $1\le T\le d-1$，置
$$
P=q+T.
$$
[R254 相容多次原像](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)
§§1–3 使用一个共同辅助头，给出 $R_0=I,R_1,\ldots,R_T$，
在输入孔数 $\le P$ 上准确满足
$$
DR_t=R_{t-1}.
\tag{14.1}
$$
每个 $R_t$ 增加恰好 $t$ 个孔。
该文纯尾权写成 $(j+2)^{-2}$；
对本节只需把纯尾指标重编号为 $j_{\rm old}=j-1$、
$m_{\rm old}=m-1$。原物理头始终是 $A_m$，没有改变。

在该文取输入上界 $P=q+T$、最大原像阶 $T$，
所以其共同总孔上界为 $q+2T$。
令
$$
\boxed{
L_{m,q,T}
=512\sqrt{q+2T+1}\,
(m+q+2T+1)^{3/2}.
}
\tag{14.2}
$$
该文 (3.5) 在输入核阶 $s=1$ 时给
$$
\|R_tf\|\le L_{m,q,T}^{\,t}\|f\|,
\qquad
f\in\ker D\cap\mathcal H_{\le P}.
\tag{14.3}
$$
所有阶使用同一组 $R_t$，不是在变动辅助头上分别挑选右逆。

### 14.2 去掉 primitive 输出而不重复支付核阶

令 $P_0=P_{\ker D}$；
它与孔层正交投影交换。
在 primitive 输入上记
$$
H_t=P_0R_t.
$$
$H_t$ 的输出仍 primitive，并增加 $t$ 个孔。

定义 $Q_0=I$，并按 $t$ 递推
$$
\boxed{
Q_t=R_t-\sum_{k=1}^t Q_{t-k}H_k,
\qquad 1\le t\le T.
}
\tag{14.4}
$$
$Q_t$ 在 $\ker D\cap\mathcal H_{\le P-t}$ 上读取。
若输入孔数为 $n\le P-t$，
$H_k$ 后的孔数为 $n+k\le P-(t-k)$，
所以每个 $Q_{t-k}H_k$ 都在已定义的真实域内。
全部中间孔数不超过 $P$。
本节没有交换 $R_t$ 与 $P_0$。

归纳给
$$
\boxed{
P_0Q_t=0,\qquad DQ_t=Q_{t-1}.
}
\tag{14.5}
$$
第一式由 (14.4) 得
$P_0Q_t=H_t-H_t=0$；
其余项的 $Q_{t-k}$ 阶数为正，primitive 投影为零。
第二式中，$DQ_0H_t=DH_t=0$，其余项用归纳及 (14.1)：
$$
DQ_t
=R_{t-1}-\sum_{k=1}^{t-1}Q_{t-k-1}H_k
=Q_{t-1}.
$$

因此 $Q_tf$ 是方程 $Du=Q_{t-1}f$ 中与 $\ker D$ 正交的唯一最小原像。
在每个固定孔层上，它准确等于顺次单步 Moore--Penrose 原像。
一般不等于 $D^t$ 的最小原像，未把这两种最小化混同。
也没有宣称整个无限孔层直和上的 $D^\dagger$ 有界。

利用 $P_0Q_t=0$，(14.4) 还可写为
$$
Q_t=(I-P_0)R_t-\sum_{k=1}^{t-1}Q_{t-k}H_k.
$$
(14.3) 与 $\|H_k\|\le L^k$ 递推给
$$
\boxed{
\|Q_tf\|\le2^{t-1}L^t\|f\|\le(2L)^t\|f\|,
\qquad1\le t\le T,
}
\tag{14.6}
$$
其中 $L=L_{m,q,T}$。
具体地，$t=1$ 的系数为一；
若前面各阶已付，
$$
1+\sum_{k=1}^{t-1}2^{t-k-1}=2^{t-1}.
$$
所以这里没有出现 $L^{t(t+1)/2}$ 的重复核阶费用。

由 (14.5)，对 primitive 输入还有
$$
D^{t+1}Q_tf=0.
\tag{14.7}
$$
现在 $Q_tf$ 的位置支撑可以无限远；
(14.5)–(14.7) 是原完整尾 Hilbert 空间中的结论。

### 14.2.A 一般短核阶的顺次最小原像仍只支付一次核阶

保留 §14.1 的同一组 $R_t$ 及 §14.2 已构造的 primitive 算子 $Q_t$。
对一般 $f\in\ker D^s\cap\mathcal H_{\le P-t}$，定义
$$
\widehat Q_0f=f,\qquad
\widehat Q_tf
=R_tf-\sum_{k=1}^t Q_{t-k}(P_0R_kf).
\tag{14.18}
$$
每个 $P_0R_kf$ 都是 primitive；孔数域与 (14.4) 的检查完全相同。
这里求和中的 $Q_{t-k}$ 始终是已经定义的 primitive 算子，
没有循环使用尚待定义的 $\widehat Q$。

同样逐项计算给
$$
P_0\widehat Q_tf=0,\qquad
D\widehat Q_tf=\widehat Q_{t-1}f.
\tag{14.19}
$$
所以 $\widehat Q_t$ 是对这个输入的真正顺次单步最小原像，
并有 $D^{s+t}\widehat Q_tf=0$。
它仍不被认成 $D^t$ 的最小原像。

原 R254 (3.5) 给
$$
\|R_kf\|\le
\binom{s+k-1}{s-1}L^{s+k-1}\|f\|.
$$
把 (14.18) 的 $k=t$ 项与 $R_t$ 合成 $(I-P_0)R_t$，
再用 (14.6) 估计其余项，便得
$$
\begin{aligned}
\|\widehat Q_tf\|
&\le L^{s+t-1}
\left[
\binom{s+t-1}{s-1}
+\sum_{k=1}^{t-1}
2^{t-k-1}\binom{s+k-1}{s-1}
\right]\|f\|\\
&\le
\boxed{
2^{t-1}\binom{s+t-1}{s-1}
L^{s+t-1}\|f\|.
}
\end{aligned}
\tag{14.20}
$$
最后一步用二项系数随 $k$ 单调以及
$1+\sum_{k=1}^{t-1}2^{t-k-1}=2^{t-1}$。
因此顺次最小化也不要求把输入核阶 $s$ 支付 $t$ 次。

### 14.3 原完整 $L$ 核及跨 $q$ 切开的旗

取任意单位头 $h\in H_T$，
并令
$$
\mathcal U_h
=\mathbb Ch\otimes
(\ker D\cap\mathcal H_{\le q}).
$$
对其尾分量 $g$ 定义
$$
\mathcal Z_h(h\otimes g)
=\sum_{t=0}^T(-1)^t A^th\otimes Q_tg,
\qquad
\mathcal C_h=\mathcal Z_h-\iota_h,
\tag{14.8}
$$
其中 $\iota_h$ 是原物理嵌入。
$q\le P-t$ 对全部 $t\le T$ 成立，所以 (14.8) 全部在 (14.4) 的域内。

由 (14.5)，相邻 $A/D$ 输出相消；
由 $Dg=0$ 及 $A^{T+1}h=0$，两端也消失。
于是
$$
L\mathcal Z_h=0.
\tag{14.9}
$$
此外，(14.5) 直接给全尾正交性
$$
\boxed{
(I_{\rm head}\otimes P_0)\mathcal C_h=0,
\qquad
\mathcal U_h\perp\operatorname{Ran}\mathcal C_h.
}
\tag{14.10}
$$
这一正交性不依赖任何位置分块。

对输入的第 $n$ 孔分量，(14.8) 第 $t$ 项处在第 $n+t$ 孔层。
在边界 $q$ 切开，右段 $k$ 对应 $t=q-n+k$。
它的头指标至多 $T-t$，
尾向量由 (14.7) 属于 $\ker D^{t+1}$。
故与 §13.2 一样，
$$
i\le T-t\le d-k,\qquad d-i\ge d-T+t\ge t+1.
$$
左源旗则由 $i\le T-(q-n)-1$ 给
$d-i-1\ge q-n+1$。
因此切开的左块属于 $V_q$，
右块属于原 $\ker S$，
并且
$$
E_qz^-+Fz^+=0.
\tag{14.11}
$$
没有更换原完整 $F_{\rm flag}$，也没有增加输出宽度。

### 14.4 同一原近核头的全阶费用

对一般 $h$，即使不同输入孔层的输出相互重叠，
三角不等式和 (14.6) 仍给
$$
\|\mathcal C_h\|
\le\sum_{t=1}^T\|A^th\|(2L)^t.
\tag{14.12}
$$
这里至多合并 $T$ 个原像阶，没有 $q$ 个输入层的三角求和。

现在取 §11 的
$$
q=q_m=\lfloor e^{d^3/4}\rfloor,\qquad
T=d/2,\qquad h=h_m.
$$
用 $\|Ah_m\|\le12\eta_{m-3}$、$\|A\|<6$，
得到
$$
\boxed{
\|\mathcal C_{h_m}\|
\le\vartheta_m
:=12T\,6^{T-1}(2L_{m,q_m,T})^T\eta_{m-3}.
}
\tag{14.13}
$$

原 $q_m\ge4d$ 和 $m+1\le d$ 给
$$
L_{m,q_m,T}\le2048q_m^2.
$$
所以
$$
\begin{aligned}
\log\vartheta_m
\le{}&
-\frac{47}{512}d^4+\frac{315}{256}d^3-\frac{75}{2}d\\
&+\frac d2\log24576+\log d.
\end{aligned}
\tag{14.14}
$$
后两项连同 $-75d/2$ 为负：$\log24576<11$ 且 $\log d<d$，已经给严格负的线性上界。
又 $m\ge5$ 时 $d\ge32$，且
$47/512-315/(256d)\ge437/8192>1/20$，
故
$$
\boxed{
\vartheta_m
\le
\exp\!\left(-\frac{47}{512}d^4+\frac{315}{256}d^3\right)
\le e^{-d^4/20}.
}
\tag{14.15}
$$
相比 §11 的有限前缀真空原像，常数变弱；
本节支付的是全尾 primitive 输入及其正规化。

### 14.5 任意原源在全部 primitive 低孔层上的准确观测

仍取任意原完整源 $r$，写
$$
y=J_q^{-1}r,\qquad
v=E_q^\dagger r=E_q^*y,\qquad
c^\flat=F_{\rm flag}^*y,\qquad
x=v+c^\flat.
$$
这里 $\|x\|^2=\mu(r)^2+\lambda(r^\flat)^2$，
且两部分按原物理孔层嵌入。
由 (14.11)，$x\perp\operatorname{Ran}\mathcal Z_h$。
令
$$
p_h=P_{\mathcal U_h}v.
$$
便准确有
$$
\mathcal C_h^*x=-p_h.
\tag{14.16}
$$
再由 (14.10)，
$$
\|p_h\|
\le\|\mathcal C_h\|\,
\|(I-P_{\mathcal U_h})x\|.
$$
专取 $h=h_m$ 并用 (14.13)，得到
$$
\boxed{
\begin{aligned}
\|P_{\mathbb Ch_m\otimes
(\ker D_m\cap\mathcal H_{\le q_m})}v\|^2
&\le
\frac{\vartheta_m^2}{1+\vartheta_m^2}
\left(\mu(r)^2+\lambda(r^\flat)^2\right)\\
&\le
e^{-d^4/10}
\left(\mu(r)^2+\lambda(r^\flat)^2\right).
\end{aligned}
}
\tag{14.17}
$$
这里的投影是完整原连续尾的 $\ker D_m$ 投影，
没有有限前缀或远尾真空限制。
任意真实来源已支付的 $\lambda(r^\flat)$ 可直接代入；
来源本身没有被 primitive 截断或更换。

本节去掉的是 §13 对尾位置的限制。
(14.17) 仍只读具体的近核头方向 $h_m$，
一般头方向以及非primitive左质量仍未覆盖。
因此没有把正规化原像或 (14.17) 当作全源三 Gram 上界，
也没有宣称 $N=M$。

### 14.6 原 W 上的直接角度推论

§14 的所有 $\mathcal Z_{h_m}g$ 都属于
$\ker L_m\cap\mathcal H_{\le q_m+T}$，
而原 $q_m+T<e^{d^3/3}$。
[原线性逐头提升的完整证明](2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md)
§6 式 (6.7) 在这整个有限孔 Hilbert 空间上给
$$
\Lambda\mathcal Z_{h_m}g\in N,\qquad
\|(\Lambda-I)\mathcal Z_{h_m}g\|
\le\delta_m\|\mathcal Z_{h_m}g\|,
\qquad
\delta_m=e^{-75d^4}.
$$
该定理不要求位置支撑有限；
因此 §14 使用全尾 $P_0$ 没有损失提升域。

由 $\mathcal U_{h_m}\perp\operatorname{Ran}\mathcal C_{h_m}$，
$$
\|\mathcal Z_{h_m}\|
\le\sqrt{1+\vartheta_m^2}.
$$
于是作为从 $\mathcal U_{h_m}$ 到原物理空间的算子，
$$
\|\Lambda\mathcal Z_{h_m}-\iota_{h_m}\|
\le\vartheta_m+\delta_m\sqrt{1+\vartheta_m^2}.
\tag{14.21}
$$
对任意 $w\in W=M\ominus N$ 配对，得到
$$
\boxed{
\left\|
P_{\mathbb Ch_m\otimes
(\ker D_m\cap\mathcal H_{\le q_m})}w
\right\|
\le
\left(\vartheta_m+\delta_m\sqrt{1+\vartheta_m^2}\right)\|w\|
\le2e^{-d^4/20}\|w\|.
}
\tag{14.22}
$$
这个推论直接作用于原 $w$，不要求先用 $v\to w$，
也没有把某个投影后的向量当成另一个合法来源。
它仍只排除指定近核头方向上的这部分质量；
其余头及非primitive投影补没有因此消失。
