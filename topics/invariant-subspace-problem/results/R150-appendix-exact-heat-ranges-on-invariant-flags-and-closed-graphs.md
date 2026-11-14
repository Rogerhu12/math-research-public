# R150 附录：准确热值域在全部不变限制、有限旗子商与闭交换图上的传递

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。根代理提出利用同一组真实强单位支付逆向包含，本文给完整范数与图实现。

状态：完整证明。已核 R140 的固定 first 预解核心、R230 的强单位子商论证及 R244 的逆图核心：普遍单射稠密和强单位论证不是新结果。本稿新增的是将[准确占据权值域](R150-appendix-exact-weighted-occupation-ranges-of-positive-semigroups.md)传到实际未知限制，识别带正确加权商范数的真实子商逆域，并给一般闭交换图的准确加权核心。

## 1. 全空间输入与记号

固定非负 $a\in\ell^2$，令
$$
S(t)=e^{-tX_a},\qquad
\mathcal N_a\chi_F=\Bigl(\sum_{j\in F}a_j\Bigr)\chi_F,\qquad
W_\delta=e^{\delta\mathcal N_a}.
$$
记
$$
H_{a,\delta}=\operatorname{Dom}W_\delta,\qquad
\|f\|_{a,\delta}=\|W_\delta f\|,\quad\delta\ge0.
$$
前稿已经证明，对任意 $t>0,\delta\ge0$，
$$
\boxed{
S(t)H_{a,\delta}=H_{a,\delta+2t},\qquad
U_\delta(t)=W_{\delta+2t}S(t)W_{-\delta}\in B(H)^\times.
}
\tag{1.1}
$$
记已付的两向常数为 $M_{\delta,t}<\infty$，使
$$
M_{\delta,t}^{-1}\|f\|_{a,\delta}
\le\|S(t)f\|_{a,\delta+2t}
\le M_{\delta,t}\|f\|_{a,\delta}.
\tag{1.2}
$$

所有算子在有限放大上按对角方式作用。
对有限 $r$ 写 $H^{(r)}=H\otimes\mathbb C^r$、
$S^{(r)}(t)$ 和 $W_\delta^{(r)}$，
其范数常数仍为同一个 $M_{\delta,t}$。

这里没有假定 $W_\delta$ 保持任何未知不变空间。
下文全部逆向包含使用实际有界交换子强单位。

## 2. 固定热因子的同一组收缩强单位

固定 $t>0$，取实际有限头
$$
H_m=\sum_{j<m}a_jV_j,\qquad
D_m=e^{tH_m}\in\mathcal A.
$$
每个 $D_m$ 是全域有界单位；不要求其范数一致有界。
实际正 first 的半群分解给
$$
\boxed{
K_m:=S(t)D_m
=e^{-tX_{a\mathbf1_{j\ge m}}},\qquad
\|K_m\|\le1.
}
\tag{2.1}
$$
所有因子属于交换的 $A'$。

还需证明这个尾半群强趋于 $I$。
对有限 Walsh 柱 $f=X_f1$，实际第一阶完整域交换及
$V_j1=\chi_j$ 给
$$
\|X_{a\mathbf1_{j\ge m}}f\|
\le\|X_f\|\|a_{\ge m}\|_2.
$$
在该实际域输入上积分半群导数，得到
$$
\|(K_m-I)f\|
\le t\|X_f\|\|a_{\ge m}\|_2\longrightarrow0.
\tag{2.2}
$$
有限柱稠密且 $K_m$ 均收缩，所以
$$
\boxed{K_m\longrightarrow I\quad\mathrm{SOT}.}
\tag{2.3}
$$
这同一组 $D_m$ 将在下面每个逆、限制、子商和闭图中使用。

R88 的强多项式逼近给：
每个闭 $A^{(r)}$ 不变空间均被
$S^{(r)}(t)$、$D_m^{(r)}$ 和 $K_m^{(r)}$ 保持。
只取有限对角放大，不把整个矩阵交换子无证加入保持族。

## 3. 所有未知闭不变空间上的准确集合等式

设 $M\subseteq H^{(r)}$ 闭且 $A^{(r)}$ 不变。
置
$$
E_\delta(M)=M\cap H_{a,\delta}^{(r)}
$$
并赋予 $W_\delta^{(r)}$ 范数。
这是加权 Hilbert 空间中的闭子空间。

**定理3.1。** 对每个 $\delta\ge0,t>0$，
$$
\boxed{
S^{(r)}(t)E_\delta(M)=E_{\delta+2t}(M).
}
\tag{3.1}
$$
特别，
$$
\boxed{
S^{(r)}(t)M=M\cap H_{a,2t}^{(r)}.
}
\tag{3.2}
$$
这是实际像集合等式，不只为闭包相等。

正向包含来自 (1.1) 及 $M$ 不变。
反向取 $h\in E_{\delta+2t}(M)$。
(1.1) 给唯一 $g\in H_{a,\delta}^{(r)}$ 使
$S^{(r)}(t)g=h$。
由交换性和 (2.3)，
$$
D_m^{(r)}h
=D_m^{(r)}S^{(r)}(t)g
=K_m^{(r)}g\longrightarrow g.
$$
每个左侧属于 $M$，而 $M$ 闭，故 $g\in M$。
这就给 (3.1)。
没有在这一步作用 $W_\delta$ 于 $M$ 后要求其仍在 $M$。

(1.2) 在 $E_\delta(M)$ 上原样成立；
因此 (3.1) 是两加权 Hilbert 空间间的有界同构。
对于 $\delta>0$，(3.2) 应用于时间 $\delta/2$，
再由同一强单位，可得
$$
\overline{E_\delta(M)}^{\,H^{(r)}}=M.
\tag{3.3}
$$
$\delta=0$ 时显然。
这也重新支付限制 $S^{(r)}(t)|_M$ 的单射和稠密像，
不从全空间的这些性质直接下传。

## 4. 有限旗子商的准确热像

取闭 $A^{(r)}$ 不变旗 $N\subseteq M$，令
$$
Q=M/N,\qquad q:M\to Q
$$
为原 Hilbert 商映射。
所有有界对角交换子均保持此旗，记 $S_Q(t)$ 为诱导算子。

由 (2.1)--(2.3)，商上仍有
$$
S_Q(t)(D_m)_Q=(K_m)_Q\longrightarrow I_Q
\quad\mathrm{SOT},\qquad
\|(K_m)_Q\|\le1.
$$
若 $S_Q(t)x=0$，则交换性使所有 $(K_m)_Qx=0$，故 $x=0$；
这些强单位的像又在 $S_Q(t)Q$ 内，故该像稠密。

由 (3.2)，准确像为
$$
\boxed{
\operatorname{Ran}S_Q(t)
=q(E_{2t}(M)).
}
\tag{4.1}
$$
自然逆的准确公式为
$$
\boxed{
\operatorname{Dom}S_Q(t)^{-1}=q(E_{2t}(M)),\qquad
S_Q(t)^{-1}q(h)=q(S(t)^{-1}h).
}
\tag{4.2}
$$
右侧有意义：由 §3，$S(t)^{-1}h\in M$。
若换一个同样加权的代表元，二者之差属于 $E_{2t}(N)$，
而 (3.1) 对 $N$ 给其逆属于 $N$。
所以 (4.2) 不依赖代表元。

这个逆是闭算子，因为它就是有界单射 $S_Q(t)$ 的逆。
无需在商上先定义一个未经证明的 $\mathcal N_a$ 压缩，
也不把普通正交压缩当成乘法同态。

## 5. 正确的加权商范数与双向预算

定义真正的加权 Hilbert 商
$$
Q_\delta=E_\delta(M)/E_\delta(N),
$$
$$
\|[h]_\delta\|_{Q_\delta}
=\inf_{n\in E_\delta(N)}
\|W_\delta^{(r)}(h-n)\|.
\tag{5.1}
$$
$E_\delta(N)$ 在 $E_\delta(M)$ 中闭。
自然映射
$$
j_\delta:Q_\delta\to Q,\qquad [h]_\delta\mapsto q(h)
$$
是单射连续映射，像为 $q(E_\delta(M))$ 且稠密。
连续性来自
$\|q(h)\|_Q\le\|[h]_\delta\|_{Q_\delta}$。

定理3.1 对 $M$ 和 $N$ 同时成立，故
$$
\mathcal S_{\delta,t}:Q_\delta\to Q_{\delta+2t},
\qquad [h]_\delta\mapsto[S(t)h]_{\delta+2t}
$$
是有界双射。
对任意 $n\in E_\delta(N)$ 使用 (1.2)，再取下确界；
因 $S(t)E_\delta(N)=E_{\delta+2t}(N)$，两向都给
$$
\boxed{
M_{\delta,t}^{-1}\|[h]_\delta\|_{Q_\delta}
\le
\|\mathcal S_{\delta,t}[h]_\delta\|_{Q_{\delta+2t}}
\le
M_{\delta,t}\|[h]_\delta\|_{Q_\delta}.
}
\tag{5.2}
$$
它与原商半群满足
$$
j_{\delta+2t}\mathcal S_{\delta,t}
=S_Q(t)j_\delta.
\tag{5.3}
$$

特别 $Q_0=Q$，所以 $\mathcal S_{0,t}$ 把原商有界同构到
$Q_{2t}$。
若 $h\in E_{2t}(M)$，则
$$
\boxed{
M_{0,t}^{-1}\|[h]_{2t}\|_{Q_{2t}}
\le
\|S_Q(t)^{-1}q(h)\|_Q
\le
M_{0,t}\|[h]_{2t}\|_{Q_{2t}}.
}
\tag{5.4}
$$
这才是准确的逆图范数等价。

不能把 (5.2)--(5.4) 改成
“$q(E_{2t}(M))$ 上加权商范数与原 $Q$ 范数直接等价”。
即使 $M=H,N=0$，在不可和行上后一说法也错误。
同样，不用 $P_{M\ominus N}h$ 替换 (5.1) 的加权最小化；
该普通投影未被证明保持加权域。

## 6. 任意闭交换图的准确加权像

设 $T:\operatorname{Dom}T\subset H^{(p)}\to H^{(q)}$
为闭线性算子，假设其图
$$
\mathcal G(T)=\{(f,Tf):f\in\operatorname{Dom}T\}
\subseteq H^{(p+q)}
$$
对 $A^{(p+q)}$ 不变。
这相当于原域被 $A^{(p)}$ 保持并满足
$TA^{(p)}f=A^{(q)}Tf$。
不要求 $T$ 有通常伴随同域或 $C$ 自伴性。

R88 的对角强逼近及图闭性使每个有界
$F\in A'$ 的对角放大保持 $\mathcal G(T)$。
把定理3.1 用于这个闭不变空间，得到
$$
\boxed{
\operatorname{diag}(S^{(p)}(t),S^{(q)}(t))
\bigl[\mathcal G(T)\cap H_{a,\delta}^{(p+q)}\bigr]
=
\mathcal G(T)\cap H_{a,\delta+2t}^{(p+q)}.
}
\tag{6.1}
$$

令
$$
D_\delta(T)=
\{f\in\operatorname{Dom}T:
f\in H_{a,\delta}^{(p)},\ Tf\in H_{a,\delta}^{(q)}\}.
$$
则 (6.1) 精确等价于
$$
\boxed{
S^{(p)}(t)D_\delta(T)=D_{\delta+2t}(T),\qquad
TS^{(p)}(t)f=S^{(q)}(t)Tf.
}
\tag{6.2}
$$
其双向范数是
$$
\bigl(\|W_\delta f\|^2+\|W_\delta Tf\|^2\bigr)^{1/2}
$$
与下一权的对应图范数，仍由 (1.2) 的同一常数控制。

特别，每个固定 $\beta>0$ 的 $D_\beta(T)$ 都是 $T$ 的图核心。
证明取 $t=\beta/2$，对任意 $f\in\operatorname{Dom}T$，
$$
K_m^{(p)}f\to f,\qquad
TK_m^{(p)}f=K_m^{(q)}Tf\to Tf.
$$
由于 $D_m$ 保持图，
$K_m f=S(t)D_mf\in S(t)\operatorname{Dom}T=D_\beta(T)$。
这付出了真实图逼近，而不是仅用环境加权域稠密。

## 7. R244 的一般最小乘子也有这样的闭交换图

R244 对任意 $f\in H$ 定义最小闭乘子 $X_f$，
初始有限柱图为
$$
(u,X_uf),\qquad u\in\mathscr D.
$$
其图确被每个对角 $A'$ 元素保持，理由如下。
[R244 共同图附录](R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md) §1 已付准确核心识别：
$$
\mathcal G(X_f)=
\overline{\{(p(A)1,p(A)f):p\in\mathbb C[z]\}}.
\tag{7.1}
$$
具体地，有限 Walsh 乘子 $X_u\in\mathcal A$ 可由多项式范数逼近，
同时作用于 $1,f$；反向用有限 Walsh 乘子在 $\mathcal A$ 中的范数稠密性。
这两个图逼近给 (7.1)，没有预设某个特定 Walsh 截断列的算子范数。

对 $B\in A'$，R88 给一列多项式 $p_n(A)\to B$ 强。
对任意 $(v,X_fv)\in\mathcal G(X_f)$，(7.1) 先给
$(p_n(A)v,p_n(A)X_fv)\in\mathcal G(X_f)$；
强收敛和图闭性于是给 $(Bv,BX_fv)\in\mathcal G(X_f)$。
所以 §6 对这个最小闭图适用，未将它免费认作任意最大乘子图。

因而对每个 $f\in H$，
$$
\boxed{
S(t)\operatorname{Dom}X_f
=
\{h\in\operatorname{Dom}X_f:
h,X_fh\in H_{a,2t}\}.
}
\tag{7.2}
$$
右侧是一个实际图核心。

对任意输入 $v\in H$，这也给一个准确的逆向域检验：
$$
\boxed{
v\in\operatorname{Dom}X_f
\Longleftrightarrow
\bigl[S(t)v\in\operatorname{Dom}X_f
\ \text{且 }X_fS(t)v\in H_{a,2t}\bigr].
}
\tag{7.3}
$$
正向由图不变和 (6.2)；
反向将 $(S(t)v,X_fS(t)v)$ 放入
$\mathcal G(X_f)\cap H_{a,2t}^{(2)}$，
用 (6.1) 的准确逆像及 $S(t)$ 单射识别第一分量为 $v$。

(7.3) 仍不说明一般 $v$ 的 $S(t)v$ 属于
$\operatorname{Dom}X_f$。
它表明：若热因子使原本不在域内的输入进入配对域，
所得乘子输出必不能同时处在同一个临界热值域中。
因此这里没有把 R244 的指定配对域问题抹去。

## 8. 结论边界

本稿补上了准确热像在所有实际闭不变限制和有限旗上的逆向包含。
所以这些特定热因子的加权像识别不应继续列为完全未知。

其依据始终是同一组有界 $D_m$ 和收缩强单位
$S(t)D_m\to I$，不是一般有界拟仿射算子的免费限制结论。
对子商使用实际加权商 $Q_\delta$，不宣称占据权或共轭
$C$ 保持未知空间。

一般慢符号的限制稠密像、正常湮灭态排除和普通 Hilbert ISP
仍未由这些域等式解决。

## 9. 任意可数正占据权的共同稠密核心

本节补付同一个未知不变空间或闭交换图内的可数多锚、全部正权；不能仅从每个域分别稠密推断。根与normal已核全部逐层极限。

### 9.1. 一个锚的嵌套 Banach 空间

固定 $a\ge0$、$a\in\ell^2$，允许 $a=0$ 或 $a\in\ell^1$。
记
$$
S(t)=e^{-tX_a},\qquad
H_{a,\delta}=\operatorname{Dom}e^{\delta\mathcal N_a}.
$$
所有算子均可作有限对角放大，下面省略放大指标。

设 $M$ 是一个闭 $A$ 不变空间。
上文已以同一组实际收缩强单位证明
$$
S(t)M=M\cap H_{a,2t},
\qquad S(t)|_M\text{ 单射、像稠密}.
\tag{9.1.1}
$$
特别，这不是从全空间拟仿射性直接下传。

对整数 $n\ge0$ 定义
$$
E_n=S(n)M,\qquad
\|h\|_{E_n}=\|S(n)|_M^{-1}h\|,
\tag{9.1.2}
$$
其中 $S(0)=I$、$E_0=M$。
$S(n):M\to E_n$ 按此范数为等距同构，故每个 $E_n$ 都完备。
集合上
$$
E_n=M\cap H_{a,2n}.
\tag{9.1.3}
$$
其范数与该实际交域的占据加权范数等价，常数可以依赖 $n$；这里无需一致控制。

若 $h=S(n+1)g$，则
$$
h=S(n)S(1)g,\qquad
\|h\|_{E_n}=\|S(1)g\|\le\|g\|=\|h\|_{E_{n+1}}.
\tag{9.1.4}
$$
所以
$$
E_{n+1}\subseteq E_n
$$
且各嵌入为收缩。
在同构 $S(n):M\to E_n$ 下，$E_{n+1}$ 恰对应 $S(1)M$。
由 (9.1.1)，
$$
\overline{E_{n+1}}^{\,E_n}=E_n.
\tag{9.1.5}
$$
这付了较强范数中的稠密性，而非只在环境 $M$ 中的稠密性。

### 9.2. 完整逐层逼近与共同极限

令
$$
E_\infty=\bigcap_{n\ge0}E_n.
$$
我们证明它在每一个 $E_k$ 中稠密。

固定 $k\ge0$、$f\in E_k$ 和 $\varepsilon>0$，置 $f_k=f$。
递归利用 (9.1.5)，选
$$
f_{n+1}\in E_{n+1},
\qquad
\|f_{n+1}-f_n\|_{E_n}
<\varepsilon\,2^{-(n-k+1)}
\quad(n\ge k).
\tag{9.2.1}
$$
对任意固定 $j\ge k$，所有 $n\ge j$ 时 $f_n\in E_j$；
由嵌入的收缩性，
$$
\|f_{n+1}-f_n\|_{E_j}
\le\|f_{n+1}-f_n\|_{E_n}
<\varepsilon\,2^{-(n-k+1)}.
$$
因此 $(f_n)_{n\ge j}$ 在完备空间 $E_j$ 中收敛。
每个 $E_j$ 连续嵌入 $M$，故这些极限作为 $M$ 中向量均为同一个 $h$。
于是 $h\in E_j$ 对所有 $j\ge k$ 成立，也属于其余更大的集合 $E_j$。
所以 $h\in E_\infty$，且
$$
\|h-f\|_{E_k}
\le\sum_{n=k}^{\infty}
\|f_{n+1}-f_n\|_{E_k}
<\varepsilon.
\tag{9.2.2}
$$

由 (9.1.3)，整数权共尾于全部正实权，故得到
$$
\boxed{
\mathscr E_a(M):=
M\cap\bigcap_{\delta>0}H_{a,\delta}
=\bigcap_{n\ge0}S(n)M
\quad\text{在 }M\text{ 中稠密。}
}
\tag{9.2.3}
$$
更强地，它在每个 $M\cap H_{a,2k}$ 的实际加权范数中稠密。
对非整数 $\delta>0$，取整数 $k>\delta/2$；
也可从尺度 $E_n^{(\delta)}=S(\delta/2+n)M$ 重复同一证明，
得到它在 $M\cap H_{a,\delta}$ 的实际加权范数中稠密。

没有声称 $S(n)M$ 中的逆像范数在 $n$ 上一致；
逐层构造只使用每一层的完备性、相邻层稠密性及单调嵌入。

### 9.3. 任意可数锚的一个真实正包络

给定任意可数族
$$
a^{(\nu)}\ge0,\qquad a^{(\nu)}\in\ell^2,
\quad \nu=1,2,\ldots .
$$
不要求行之间可比、非可和或具有共同物理排序。
取
$$
c_\nu=\frac{2^{-\nu}}{1+\|a^{(\nu)}\|_2}>0,
\qquad
a=\sum_{\nu\ge1}c_\nu a^{(\nu)}.
\tag{9.3.1}
$$
级数在 $\ell^2$ 中绝对收敛，且
$$
a\ge0,\quad \|a\|_2\le1,\quad
a_j\ge c_\nu a_j^{(\nu)}
\quad\text{对全部 }j,\nu.
\tag{9.3.2}
$$

在每个有限 Walsh 占据集 $F$ 上，(9.3.2) 给
$$
\sum_{j\in F}a_j^{(\nu)}
\le c_\nu^{-1}\sum_{j\in F}a_j.
$$
因此对每个 $\sigma>0$，
$$
H_{a,\sigma/c_\nu}\subseteq H_{a^{(\nu)},\sigma},
\qquad
\|e^{\sigma\mathcal N_{a^{(\nu)}}}h\|
\le
\|e^{(\sigma/c_\nu)\mathcal N_a}h\|.
\tag{9.3.3}
$$
这只是对准确对角占据权的逐系数比较，没有对实际 $V_j$ 作正算子比较。

所以
$$
\mathscr E_a(M)\subseteq
M\cap\bigcap_{\nu\ge1}\bigcap_{\sigma>0}H_{a^{(\nu)},\sigma}.
$$
结合 (9.2.3)，得到
$$
\boxed{
\overline{
M\cap\bigcap_{\nu\ge1}\bigcap_{\sigma>0}H_{a^{(\nu)},\sigma}
}^{\,H}
=M.
}
\tag{9.3.4}
$$
同一个 $a$ 可以预先针对整个可数族选定，再适用于所有闭不变 $M$ 及其任意有限对角放大；它不依赖未知空间。

### 9.4. 所有闭交换图的共同加权核心

设
$$
T:\operatorname{Dom}T\subseteq H^{(p)}\longrightarrow H^{(q)}
$$
闭，且其图 $\mathcal G(T)\subseteq H^{(p+q)}$ 对对角 $A$ 不变。
在 §9.3 的可数族上定义
$$
\mathscr D_{\rm all}(T)=
\left\{
f\in\operatorname{Dom}T:
f\in\bigcap_{\nu,\sigma>0}H_{a^{(\nu)},\sigma}^{(p)},
\quad
Tf\in\bigcap_{\nu,\sigma>0}H_{a^{(\nu)},\sigma}^{(q)}
\right\}.
\tag{9.4.1}
$$
将 (9.3.4) 应用于闭不变空间 $\mathcal G(T)$，便得到
$$
\boxed{\mathscr D_{\rm all}(T)\text{ 是 }T\text{ 的图核心。}}
\tag{9.4.2}
$$

具体地，对每个 $(f,Tf)$ 及每个 $\varepsilon>0$，
§9.2 的逐层构造全部在同一个闭图内进行，
产生一个 $(g,Tg)$，同时满足可数族的全部正权，并使
$$
\|g-f\|^2+\|Tg-Tf\|^2<\varepsilon^2.
$$
这里既付输入也付真实算子输出的权。
若只把环境中某个高权向量序列逼近 $f$，
则其像未必收敛；(9.4.2) 避免了这个缺口。

同理，将有限个闭算子的共同完整图
$$
\{(f,T_1f,\ldots,T_\ell f):
f\in\bigcap_{i=1}^{\ell}\operatorname{Dom}T_i\}
$$
视为一个闭图，只要它对对角 $A$ 不变，就得到全部坐标同时满足可数权的共同图核心。
这里没有把若干分别稠密的定义域自动判为共同稠密；
核心是相对于原共同完整图的准确陈述。

### 9.5. 本结论不支付的范围

(9.3.4) 和 (9.4.2) 是在指定未知不变空间或指定真实闭图内的密度结论。
它们不说明某一个固定热因子把全空间送入任意第一阶域，
也不说明给定正常见证的指定原向量已经属于某一配对域。

可数正 $\ell^2$ 占据权的包络仍为 $\ell^2$ 行，其坐标趋于0。
这里不推出统一的普通 Walsh 次数指数权
$e^{\sigma|F|}$，更不推出全部乘子域平滑。
此前第一阶的精确热平滑行类、R244 的指定配对域以及真实正常态的聚合上界均保持原边界。
