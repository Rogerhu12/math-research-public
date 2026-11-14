# R239 附录：真实原始块的无权消去、高秩扩展与完整投影障碍

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。主会话全文复核：原低方程确为正交投影；无限相容原像收敛、全部合法链约束、投影平方范数损失和完整投影矩阵元均已独立核对。

这里完整保留三份证明。对任意真实核，范数受控的中间原始分量可无权小修复，且可选几乎完整维数主指数的块；同一固定前缀的完整原始投影却有指数范数下界。普通 ISP 与完整无权 N=M 均未解决。

## A. 渐近正交的局部坏方向

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：已证明的范围校准；不构造真实缺陷。

本补充使用[局部最小能量下界与真实投影约束](../results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)的全部原参数和配对向量 $h_{m,q},g_{m,q}$。取
$$
m=m(q),\quad d=2^m,\quad
t=\left\lfloor(3\log q/800)^{1/3}\right\rfloor,
\quad J=m+2q,
$$
并简写
$$
S_J=\sum_{j\ge J}(j+1)^{-4},\qquad
B_t=\sqrt{t!}\,S_J^{t/2},\qquad
\rho=\langle h_{m,q},g_{m,q}\rangle.
$$
以下只需充分大的整数 $q$。

### 1. 改选实际头方向仍保留最小修复下界

原有限头路径已证
$$
A_m^t e_t=\kappa_t e_0,\qquad \kappa_t\ge e^{-100t^4}.
$$
故
$$
n_t:=\|(A_m^*)^t e_0\|\ge\kappa_t>0.
$$
取
$$
x_q=\frac{(A_m^*)^t e_0}{n_t},\qquad
v_q=x_q\otimes h_{m,q},\qquad
u_q=x_q\otimes g_{m,q}.
$$
三个向量均为单位向量，$v_q$ 属于原低输出精确核。
此外
$$
\|A_m^t x_q\|
\ge|\langle A_m^t x_q,e_0\rangle|=n_t.
$$
因此对任意有限加宽窗口，乃至整个无限高尾，原配对下界给
$$
\lambda^{[\infty]}_{m(q),q}(v_q)
\ge\frac{\rho n_t}{B_t}
\ge\frac{\rho\kappa_t}{B_t}.
$$
特别
$$
\boxed{
\liminf_{q\to\infty}
\frac{\log\lambda^{[\infty]}_{m(q),q}(v_q)}
 {(\log q)^{4/3}}
\ge c_0,\qquad
c_0=\frac{3(3/2)^{4/3}}{4^{4/3}100^{1/3}}>0.
}
\tag{1.1}
$$
改选头方向没有把坏能量换成指定右逆的范数。

### 2. 对偶方向与整个真实核几乎正交

令 $P_M$ 为原真实 $M=\ker T$ 的正交投影。对任意单位 $w\in M$，原稿的真实全局相容恒等式给
$$
\left\|
A_m^t(I\otimes\langle g_{m,q},\cdot\rangle)
P_q^{(m)}w
\right\|
\le B_t+26t\,6^{t-1}\eta_{m-1}.
$$
取其 $e_0$ 坐标，得到
$$
|\langle w,u_q\rangle|
\le\frac{B_t+26t\,6^{t-1}\eta_{m-1}}{n_t}.
$$
所以
$$
\|P_Mu_q\|
\le \frac{B_t}{\kappa_t}
+\frac{26t\,6^{t-1}\eta_{m-1}}{\kappa_t}.
\tag{2.1}
$$

第一项由原优化直接满足
$$
\frac{B_t}{\kappa_t}
\le\exp[-(c_0-o(1))(\log q)^{4/3}].
$$
第二项必须保留这里的实际 $t$，不能粗换成 $d$。
事实上
$$
100t^4=(c_0/3+o(1))(\log q)^{4/3},
\qquad
d^4\ge (4\log(q+2))^{4/3}.
$$
因此由 $\eta_{m-1}\le e^{-80d^4}$，
$$
\begin{aligned}
\log\frac{26t6^{t-1}\eta_{m-1}}{\kappa_t}
&\le -80d^4+100t^4+O(t+\log t)\\
&\le[-80\cdot4^{4/3}+c_0/3+o(1)](\log q)^{4/3},
\end{aligned}
$$
其指数远小于第一项。最终
$$
\boxed{
\|P_Mu_q\|
\le\exp[-(c_0-o(1))(\log q)^{4/3}].
}
\tag{2.2}
$$

### 3. 真正低输出坏向量本身也渐近离开 M

配对构造满足 $\rho\ge e^{-2/(m+1)}$，从而
$$
\|h_{m,q}-g_{m,q}\|^2=2(1-\rho)
\le\frac4{m+1}.
$$
利用正交投影的收缩性，
$$
\boxed{
\|P_Mv_q\|
\le \frac2{\sqrt{m(q)+1}}
+\exp[-(c_0-o(1))(\log q)^{4/3}]
\longrightarrow0.
}
\tag{3.1}
$$
于是这组单位低输出向量同时满足：

- 任意宽度的真正最小高尾修复至少有 $\exp(c(\log q)^{4/3})$ 规模；
- 到真实核的正交投影范数趋于零，故其到真实核的距离趋于1。

这定位了该局部坏族，没有把它误作真实核内坏向量。若
$C_{m,q}:M\to\mathscr V_{m,q}$ 是真实低方程投影的限制，则对
$v_q\in\mathscr V_{m,q}$ 有
$C_{m,q}^*v_q=P_Mv_q$，所以 (3.1) 同时是实际投影范围的一个准确对偶约束。

它不排除真实范围上的其他坏方向，也没有控制完整 Gram 逆能量。下一步仍须利用真实核相容性处理那些不能被 (3.1) 消掉的部分。

## B. 相容真空原像与真实原始块小修复

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：以下真空原像和原始块小修复已证明；完整补空间的最小能量及原无权 $N=M$ 仍开放。

本稿使用[局部最小能量与真实投影约束](../results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)中的相邻配对纯核/共纯核。新的结论是：那一块在全低输出空间会产生真正的 $\log^{4/3}$ 坏能量，但对任意真实 $w\in M$，其实际残量分量可用范数趋零的合法高尾修复消去；不需要对 $w$ 的 Hilbert 尾另加正则性。

### 1. 后尾真空的渐近最优相容原像

设
$$
D_J=\sum_{j\ge J}a_jE_j,\qquad
a_j=(j+1)^{-2},\qquad S_J=\sum_{j\ge J}a_j^2.
$$
给定整数 $d\ge1$，假设 $J^{3/4}\ge2d$。令
$$
\varepsilon=J^{-1/4},\qquad n_0=J,\quad
L_i=\lceil\varepsilon n_i\rceil,\quad n_{i+1}=n_i+L_i,
\quad I_i=[n_i,n_{i+1}-1].
$$
这些有限块分割整个后尾，且 $L_i\ge J^{3/4}$。

在第 $i$ 块上写
$$
D_i=\sum_{j\in I_i}a_jE_j,\quad
C_i=\sum_{j\in I_i}a_j^{-1}E_j^*,\quad
U_i=\sum_{j\in I_i}a_j^{-2},\quad
\sigma_i=\frac{L_i^2}{U_i}.
$$
记下降阶乘 $(L)_t=L(L-1)\cdots(L-t+1)$。定义
$$
b_{i,0}=\Omega_i,\qquad
b_{i,t}=\frac{C_i^t\Omega_i}{t!(L_i)_t}
\quad(1\le t\le d).
\tag{1.1}
$$
有限块的准确关系
$[D_i,C_i]=L_i-2\mathcal N_i$ 给
$$
D_iC_i^t\Omega_i
=t(L_i-t+1)C_i^{t-1}\Omega_i,
$$
故
$$
\boxed{D_ib_{i,t}=b_{i,t-1}.}
\tag{1.2}
$$

同时
$$
\|b_{i,t}\|^2
=\frac{e_t((a_j^{-2})_{j\in I_i})}{(L_i)_t^2}
\le
\frac1{t!\sigma_i^t}
\left(\frac{L_i^t}{(L_i)_t}\right)^2.
$$
因 $t\le d\le L_i/2$，
$$
2\log\frac{L_i^t}{(L_i)_t}
=2\sum_{k<t}-\log(1-k/L_i)
\le\frac{2t(t-1)}{L_i}.
$$
所以
$$
\|b_{i,t}\|^2
\le\frac{\exp(2t(t-1)/L_i)}{t!\sigma_i^t}.
\tag{1.3}
$$

块内系数比满足
$a_{\max}/a_{\min}\le(1+\varepsilon)^2$。若
$S_i=\sum_{j\in I_i}a_j^2$，Cauchy--Schwarz 与最大/最小值比较分别给
$$
(1+\varepsilon)^{-4}S_i\le\sigma_i\le S_i.
$$
置
$$
\sigma=\sum_i\sigma_i,\qquad p_i=\sigma_i/\sigma.
$$
则 $\sum_ip_i=1$，并有
$$
(1+\varepsilon)^{-4}S_J\le\sigma\le S_J.
\tag{1.4}
$$

对 $0\le t\le d$，在无限张量尾空间定义
$$
b_t=
\sum_{\substack{(t_i)\ {\rm 有限支撑}\\t_i\ge0,\ \sum_i t_i=t}}
 \bigotimes_i p_i^{t_i}b_{i,t_i}.
\tag{1.5}
$$
不同多重指标的各块孔次数不同，因此求和项互相正交。
由 (1.3)，总指数损失至多
$2\sum_it_i(t_i-1)/L_i\le2d^2/J^{3/4}$。
多项式展开给准确标量求和
$$
\sum_{\sum t_i=t}
 \prod_i\frac{p_i^{2t_i}}{t_i!\sigma_i^{t_i}}
=
\frac1{t!}\left(\sum_i\frac{p_i^2}{\sigma_i}\right)^t
=\frac1{t!\sigma^t}.
$$
这既证明 (1.5) 在 Hilbert 范数下收敛，也给
$$
\boxed{
\|b_t\|^2\le
\frac{K_{J,d}}{t!\,S_J^t},
\quad
K_{J,d}:=
\exp\!\left(\frac{2d^2}{J^{3/4}}+
             \frac{8d}{J^{1/4}}\right).
}
\tag{1.6}
$$
这里用了 (1.4) 及 $4d\log(1+\varepsilon)\le8d\varepsilon$。

每项严格有 $t$ 个后尾孔。由 (1.2)，对固定目标多重指标，删除一孔的全部来源系数相加恰为 $\sum_ip_i=1$。先截有限块，再用上述范数收敛及 $D_J$ 有界取极限，得到
$$
\boxed{
b_0=\Omega,\qquad D_Jb_t=b_{t-1}\quad(1\le t\le d).
}
\tag{1.7}
$$
特别 $D_J^tb_t=\Omega$。反过来，任何满足这个等式的 $t$ 孔原像都由 Cauchy--Schwarz 满足
$$
\|b_t\|^2\ge
\|(D_J^*)^t\Omega\|^{-2}
\ge\frac1{t!S_J^t}.
\tag{1.8}
$$
所以 (1.6) 不仅保留阶乘，而且整个同一相容族在
$d^2/J^{3/4}+d/J^{1/4}\to0$ 时同时渐近达到这个真空能量下界。

### 2. 配对原始块的准确斜投影

回到原全整数选择 $m=m(q)$、$d=2^m$、$J=m+2q$。
在前缀 $I=[m,J-1]$ 上取原稿的单位向量 $h=h_{m,q}$、$g=g_{m,q}$；
这里先不附加后尾真空。它们严格有 $q$ 孔，且
$$
D_Ih=0,\qquad D_I^*g=0,\qquad
\rho=\langle h,g\rangle\ge e^{-2/(m+1)}.
$$
定义前缀斜投影并在原头与后尾张量恒等：
$$
\boxed{\Pi=\rho^{-1}|h\rangle\langle g|.}
\tag{2.1}
$$
有
$$
\Pi^2=\Pi,\qquad \|\Pi\|=\rho^{-1}\longrightarrow1,
$$
$$
D_I\Pi=\Pi D_I=0,\qquad
[D_m,\Pi]=[A_m,\Pi]=[L_m,\Pi]=0.
\tag{2.2}
$$
注意完整 $D_m\Pi$ 一般并非零；(2.2) 的零等式只对前缀
$D_I$ 成立。完整后尾删除仍作用于 $\Pi$ 的像。

$\Pi$ 保持尾孔次数。若 $v\in\mathscr V_{m,q}$，它在 $q$ 以下各层均被 $\Pi$ 杀掉，并且
$$
\Pi v=\frac{x_g(v)}{\rho}\otimes h\otimes\Omega_J,
\quad
x_g(v)=(I_{\rm head}\otimes
 \langle g\otimes\Omega_J,\cdot\rangle)v_q.
\tag{2.3}
$$
因此 $\Pi v$ 仍在同一低输出精确核，且对 $r=A_mv_q$，
$$
r^\Pi:=\Pi r
=A_mx_g(v)/\rho\otimes h\otimes\Omega_J.
\tag{2.4}
$$

### 3. 这一块的真正有限和无限最小能量

先对任意原头向量 $x$ 取 $v=x\otimes h\otimes\Omega_J$，
并记
$$
Q_{A,J}(x)=
\sum_{t=1}^{d}
 \frac{\|A_m^t x\|^2}{t!S_J^t}.
$$
原配对观测对任意有限宽度或无限高尾可行修复给
$$
\lambda^{[\infty]}(v)^2\ge\rho^2Q_{A,J}(x).
\tag{3.1}
$$

用 §1 的同一相容族定义
$$
c_t=(-1)^{t-1}A_m^t x\otimes h\otimes b_t,
\qquad c=\sum_{t=1}^{d}c_t.
\tag{3.2}
$$
由 $D_Ih=0$、(1.7) 及 $A_m^d=0$，
$$
D_mc_1=A_mx\otimes h,\qquad
D_mc_{t+1}=-A_mc_t,\qquad A_mc_d=0.
$$
所以 $L_mc=A_mv$。它严格支持尾孔 $q+1,\ldots,q+d$；
$D_m^dc=0$ 也准确成立，因为 $b_t$ 只有 $t$ 孔，且 $t=d$ 项本来为零。
各 $c_t$ 互相正交，故 (1.6) 给
$$
\|c\|^2\le K_{J,d}Q_{A,J}(x).
$$
于是
$$
\boxed{
\rho^2Q_{A,J}(x)
\le\lambda^{[\infty]}(v)^2
\le\lambda^{[d]}(v)^2
\le K_{J,d}Q_{A,J}(x).
}
\tag{3.3}
$$
对于原自适应 $d=O((\log q)^{1/3})$、$J=m+2q$，
有 $K_{J,d}\to1$ 且 $\rho\to1$。
因此 (3.3) 是对全部头向量 $x$ 统一的渐近精确二次型，而非某个候选右逆的单侧粗界。零二次型时两边都准确为零。

### 4. 任意真实核的这一块有无权小修复

现取任意 $w\in M=\ker T$，$v=v_{m,q}(w)$。
原真实相容性已付清
$$
Z_t(v):=\frac{\|A_m^t x_g(v)\|}{\sqrt{t!}S_J^{t/2}}
\le\|P_{q+t}^{(m)}w\|
 +e^{-72d^4}\|w\|
\qquad(1\le t\le d).
\tag{4.1}
$$
其中归一化小分母已经支付，未把 $\eta$ 小直接当作小原像。

对 (2.4) 取 (3.2) 中 $x=x_g(v)/\rho$，记所得合法修复为
$c^\Pi$。由 (1.6) 和有限序列 Minkowski 不等式，
$$
\boxed{
\begin{aligned}
\|c^\Pi\|
&\le \frac{\sqrt{K_{J,d}}}{\rho}
 \left(\sum_{t=1}^d Z_t(v)^2\right)^{1/2}\\
&\le\frac{\sqrt{K_{J,d}}}{\rho}
 \left[
 \|P_{[q+1,q+d]}^{(m)}w\|
 +\sqrt d\,e^{-72d^4}\|w\|
 \right].
\end{aligned}
}
\tag{4.2}
$$
尾孔超过 $q$ 必使原总孔超过 $q$，故该上界至多为
$$
(1+o(1))
 \left[\tau_q(w)+\sqrt d\,e^{-72d^4}\|w\|\right]
\longrightarrow0.
\tag{4.3}
$$
这一结论对每个真实 Hilbert 核向量成立，不要求任何指定尾衰减速度。

这里没有声称 $\Pi$ 保持真实 $\ker T$。它与混合 $L_m$ 交换；
真实 $T$ 的误差全部通过 (4.1) 进入 (4.2)。

### 5. 可以从原最小能量中删去这个分量

令 $\lambda_q^\Pi(w)$ 为同一合法窗口内源 $r^\Pi$ 的最小修复范数，
令 $\lambda_q^{\rm rem}(w)$ 为源 $(I-\Pi)r$ 的最小修复范数。
由于 $\Pi v$ 和 $(I-\Pi)v$ 都是同一低方程核向量，二者的
$D^d$ 约束均由已证链身份自动满足。

原 Gram 表示的最小解算子是线性的：
$F^*\mathsf G^{-1}r$。因此
$$
\boxed{
|\lambda_q(w)-\lambda_q^{\rm rem}(w)|
\le\lambda_q^\Pi(w)
\le\|c^\Pi\|\longrightarrow0.
}
\tag{5.1}
$$
这使用一个明确可行的小修复及最小解线性性，不是把某个
Gram 非对角块直接删除，也没有遗漏 Schur 补。

对 $\Pi$ 源本身，(3.3) 更准确给
$$
\sum_{t=1}^d Z_t(v)^2
\le(\lambda_q^\Pi(w))^2
\le\frac{K_{J,d}}{\rho^2}\sum_{t=1}^d Z_t(v)^2.
\tag{5.2}
$$
因此这部分真正最小能量已被实际未来尾控制，任何慢 Hilbert 尾都不构成障碍。

### 6. 推广到任意受控的中间原始投影

上述机制不要求前缀像只有一维。设 $P$ 是前缀
$I=[m,m+2q-1]$ 上的有界投影，满足
$$
\operatorname{Ran}P\subseteq\mathcal H_q(I),\qquad
P=P\,P_q(I),\qquad D_IP=P D_I=0.
\tag{6.1}
$$
在原头和后尾张量恒等。则 $P$ 与 $L_m$ 交换，而 $Pv$ 的后尾仍是真空。
§3 的同一 $b_t$ 可作用于向量值的 $Pv$，得到 $Pr$ 的合法修复。

对原真实恒等式
$A^t-(-D)^t=\sum_{j<t}A^{t-1-j}(-D)^jL$
作用于 $w$ 后再施加 $P$。由于 $P D_I=0$，删除幂只剩
$P D_J^t$；在所选总层上其后尾源恰有 $t$ 孔，范数至多
$\|P\|\sqrt{t!}S_J^{t/2}$。按 (4.1) 相同预算，得到
$$
\boxed{
\lambda_q^{P}(w)
\le
\sqrt{K_{J,d}}\,\|P\|
 \left[
 \|P_{[q+1,q+d]}^{(m)}w\|
 +\sqrt d\,e^{-72d^4}\|w\|
 \right].
}
\tag{6.2}
$$
故任何范数一致有界的这类前缀原始投影族，都可对任意真实核消去其残量分量，而不增加尾正则假设。

当前仍未证明这些受控原始块组成覆盖全部实际 $D^d$ 残量的稳定分解。匹配块、一般原始向量之间的框架常数，以及其余纯删除链，都必须另付；不能从单块或 (6.2) 直接跳到完整 $\lambda_q(w)$ 的控制。

## C. 高秩受控块与完整固定前缀障碍

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：以下扩块构造和完整投影下界已证明；未闭合全部实际残量的稳定分解。

本稿应用[相容真空 jets 与无权原始块消去](../notes/2026-11-13-compatible-vacuum-jets-and-unweighted-primitive-block-removal-boundary-resume.md)的通用投影结论：在前缀 $I=[m,m+2q-1]$ 上，只要
$$
\operatorname{Ran}P\subseteq H_q(I),\quad P=P P_q(I),
\quad D_IP=P D_I=0,
\tag{0.1}
$$
且 $\|P\|$ 一致受控，任意真实 $w\in M$ 的 $Pr_{m,q}(w)$ 都有合法小修复
$$
\lambda_q^P(w)\le
\sqrt{K_{m+2q,d}}\,\|P\|
\left[\|P_{[q+1,q+d]}^{(m)}w\|
+\sqrt d\,e^{-72d^4}\|w\|\right].
\tag{0.2}
$$
这里的 $P$ 可以有很大的秩。本稿先构造这样的指数秩投影，再证明同一固定前缀的完整原始投影不能具有这种统一范数。

### 1. 均权中间原始空间

在一个有 $2r$ 位的有限块上，令
$$
D_0=\sum_{j=1}^{2r}E_j.
$$
在 $r$ 孔层 $H_r$，
$[D_0,D_0^*]=2r-2\mathcal N=0$，所以
$$
\ker(D_0|_{H_r})=\ker(D_0^*|_{H_r}).
$$
令 $P_0^{(r)}$ 为这个公共核的正交投影，在其他孔层取零。则
$$
D_0P_0^{(r)}=P_0^{(r)}D_0=0.
\tag{1.1}
$$
在第 $r-1$ 层，$D_0D_0^*\ge2I$，故
$D_0:H_r\to H_{r-1}$ 满射。于是
$$
\boxed{
\operatorname{rank}P_0^{(r)}
=\binom{2r}{r}-\binom{2r}{r-1}
=\operatorname{Cat}(r):=\frac1{r+1}\binom{2r}{r}.
}
\tag{1.2}
$$
记 $\operatorname{Cat}(0)=1$。

### 2. 一个近均权块的原始投影范数只损失平方量

现在块为 $[n,n+2r-1]$，原权仍为 $a_j=(j+1)^{-2}$。
令 $a_0=a_n$，定义正对角矩阵
$$
S e_F=\left(\prod_{j\in F}\frac{a_0}{a_j}\right)e_F.
$$
直接按一个删除矩阵元核对，
$$
D_{\rm block}=S(a_0D_0)S^{-1}.
$$
因此
$$
P_{\rm block}=S P_0^{(r)}S^{-1}
\tag{2.1}
$$
是满足原权版本 (1.1) 的投影，其像严格在中间 $r$ 孔层。

对任意 $F$，
$$
0\le\log S_{FF}
\le4r\log\left(1+\frac{2r-1}{n+1}\right)
\le\frac{8r^2}{n+1}.
$$
乘 $S$ 以一个正标量不改变 (2.1)。取居中的标量后，可使
$$
\delta:=\|S-I\|\le\frac{8r^2}{n+1}\le\frac12
\qquad(n+1\ge16r^2).
$$
于是
$$
\|P_{\rm block}-P_0^{(r)}\|
\le\frac{2\delta}{1-\delta}\le4\delta.
\tag{2.2}
$$

这里不能直接把 (2.2) 的线性误差逐块相乘；投影范数有平方改善。
对任何非零有界幂等 $P$，相对于其像的正交分解有
$P=\begin{pmatrix}I&B\\0&0\end{pmatrix}$，故
$$
\boxed{\|P\|^2=1+\|P-P^*\|^2.}
\tag{2.3}
$$
由 (2.2)，$\|P_{\rm block}-P_{\rm block}^*\|\le8\delta$，所以
$$
\boxed{
\log\|P_{\rm block}\|
\le32\delta^2
\le\frac{2048r^4}{(n+1)^2}.
}
\tag{2.4}
$$
所有矩阵都在实际原权下；没有丢掉相似的条件数。

### 3. 前 2q 位上范数趋于1的指数秩投影

写 $q=ar+s$，$0\le s<r$。把前缀 $I=[m,m+2q-1]$ 分成
$a$ 个相邻 $2r$ 位块，最后若 $s>0$ 再加一个 $2s$ 位块。
在每块取 §2 的实际投影，并令
$$
P_q^{(r)}=\bigotimes_{\rm blocks}P_{\rm block}.
$$
它满足 (0.1)，且
$$
\boxed{
\operatorname{rank}P_q^{(r)}
=\operatorname{Cat}(r)^a\operatorname{Cat}(s).
}
\tag{3.1}
$$
因为各块恰有半数孔，全部像恰有 $q$ 孔；每个块的删除从左右都被杀掉，所以整个 $D_I$ 也从左右被杀掉。

若 $m+1\ge16r^2$，把最终小块也用 $r$ 的上界支付，
$$
\begin{aligned}
\log\|P_q^{(r)}\|
&\le2048r^4\sum_{k\ge0}(m+2rk+1)^{-2}\\
&\le2048r^4
 \left[\frac1{(m+1)^2}+\frac1{2r(m+1)}\right]\\
&\le\frac{2048r^3}{m+1}.
\end{aligned}
$$
因此
$$
\boxed{
\|P_q^{(r)}\|\le
\exp\!\left(\frac{2048r^3}{m+1}\right).
}
\tag{3.2}
$$

取原 $m=m(q)$，再令 $r=\lfloor m^{1/4}\rfloor$。
对充分大的 $q$，上述条件满足，$r\to\infty$，且
$r^3/m\to0$，故
$$
\|P_q^{(r)}\|\longrightarrow1.
\tag{3.3}
$$
由
$$
\frac{4^r}{(r+1)(2r+1)}
\le\operatorname{Cat}(r)\le4^r
$$
以及 (3.1)，得到
$$
\boxed{
\log\operatorname{rank}P_q^{(r)}
=(2\log2-o(1))q.
}
\tag{3.4}
$$
这只描述维数主指数，不表示该像等于完整中间原始空间。

对任意真实 $w\in M$，(0.2)、(3.3) 给
$$
\boxed{
\lambda_q^{P_q^{(r)}}(w)
\le(1+o(1))
 \left[\tau_q(w)+\sqrt d\,e^{-72d^4}\|w\|\right]
\longrightarrow0.
}
\tag{3.5}
$$
最小解线性性还给
$$
|\lambda_q(w)-\lambda_q^{I-P_q^{(r)}}(w)|
\le\lambda_q^{P_q^{(r)}}(w)\longrightarrow0.
\tag{3.6}
$$
因此已消去的块不仅是一条配对原始线；它可以具有 (3.4) 的指数秩，而且不要求原核向量的尾正则性。

### 4. 同一固定前缀的完整原始投影唯一

令 $I$ 恰有 $2q$ 位，原权为 $a_j$。
设
$$
K=\ker(D_I|_{H_q(I)}),\qquad
R=D_I H_{q+1}(I).
$$
在均权下，$K_0=R_0^\perp$；按同一个正对角 $S$ 相似后仍有
$$
H_q(I)=K\mathbin{\dot+}R.
\tag{4.1}
$$
因此，在第 $q$ 层上，任何像为全部 $K$ 且杀掉 $R$ 的投影只能是
$$
\boxed{P_{\rm full}=S P_0^{(q)}S^{-1}.}
\tag{4.2}
$$
其余层取零后，它也满足 $D_IP_{\rm full}=P_{\rm full}D_I=0$。
这个投影是唯一的，不能通过另选完整基来改变其算子范数。

### 5. 均权完整投影的互补子集矩阵元

固定一个 $q$ 元子集 $G$。均权 $P_0^{(q)}$ 与所有位排列交换，
因此其列
$$
f(F)=\langle P_0^{(q)}e_G,e_F\rangle
$$
只依赖 $k=|F\cap G|$，记为 $u_k$。
因 $D_0f=0$，对任意 $(q-1)$ 元集合 $H$、$k=|H\cap G|$，
$$
(q-k)u_{k+1}+(k+1)u_k=0.
$$
从 $k=0$ 递推到 $k=q-1$，得到 $u_q=(-1)^qu_0$。
另一方面，置换对称使所有对角元相等；由 (1.2) 的秩，
$$
u_q=\frac{\operatorname{Cat}(q)}{\binom{2q}{q}}
=\frac1{q+1}.
$$
所以对互补 $q$ 元子集 $F=I\setminus G$，
$$
\boxed{
\left|\langle P_0^{(q)}e_G,e_F\rangle\right|
=\frac1{q+1}.
}
\tag{5.1}
$$
这是一段有限维完整证明，没有借用未核的 Specht 张成结论。

### 6. 原固定前缀的完整投影范数指数大

取 $G$ 为前缀的最前 $q$ 位，$F$ 为最后 $q$ 位。
由于 $S_{FF}/S_{GG}=\prod_{j\in G}a_j/\prod_{j\in F}a_j$，
(4.2)、(5.1) 给
$$
\boxed{
\|P_{\rm full}\|
\ge
\frac1{q+1}
\left[
\frac{(m+2q)!\,m!}{((m+q)!)^2}
\right]^2.
}
\tag{6.1}
$$
对原 $m(q)=O(\log\log q)$，
中心二项系数与有限额外乘积的比较给
$$
\log\frac{(m+2q)!\,m!}{((m+q)!)^2}
=2q\log2+o(q).
$$
故
$$
\boxed{
\log\|P_{\rm full}\|
\ge(4\log2-o(1))q.
}
\tag{6.2}
$$
这是原 $(j+1)^{-2}$ 权的实际下界，不是任意不均匀权的抽象例。

特别，若某个分析算子 $\mathcal A$ 和重构算子 $\mathcal R$
在同一固定前缀内满足
$\mathcal R\mathcal A=P_{\rm full}$，则
$$
\|\mathcal R\|\,\|\mathcal A\|
\ge\|P_{\rm full}\|
\ge\exp[(4\log2-o(1))q].
\tag{6.3}
$$
把许多局部原始块相加，并要求在全部 $K$ 上为恒等、在 $R$ 上为零，
也必然合成为同一个 $P_{\rm full}$，因此同样受 (6.2) 限制。

### 7. 已推进的部分与剩余问题

(3.5)–(3.6) 对一个范数趋于1、维数具有几乎完整主指数的实际原始块，给出了真正的无权小修复。这使用真实全局核相容性；局部单位球中同样的方向仍能有很大的最小能量。

(6.2) 同时排除在这个固定前缀上，靠一个统一有界的完整原始投影或稳定分析/重构来直接覆盖全部剩余向量。其余原始方向、跨块删除链、移动前缀或利用真实范围的进一步分解仍需处理。不能从高秩或局部投影范数好直接宣布覆盖所有 $D^d$ 残量。

