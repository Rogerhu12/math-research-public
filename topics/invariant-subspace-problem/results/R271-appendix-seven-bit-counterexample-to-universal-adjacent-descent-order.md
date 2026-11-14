# R271 附录：七位布尔模型否定普遍异权的相邻第一下降序

日期：2026-11-13（UTC）。作者：kernel_resume_1cf / Astra-ISP-1cf8c51d；AI-assisted，GPT-6 Astra Pro。
状态：完整的有限维反例；根代理与 boundary_resume_1cf 已独立核查真实最小逆、投影伴随及全部有理数。所有高度空间、正交投影和最小逆均取在整个真实布尔 Hilbert 空间中。本稿只否定任意正异权推广，不否定原连续尾权 $b_j=(j+1)^{-2}$ 的特定候选。

## 1. 被检查的准确候选

在有限布尔空间上，孔集向量组成正交规范基，$E_j$ 删除第 $j$ 个孔。置
$$
D=\sum_j b_jE_j,\qquad
\mathcal H_p=\text{第 }p\text{ 孔层},
$$
$$
E_{h,p}=\ker D^h\cap\mathcal H_p,\qquad
U_{h,p}=E_{h,p}\ominus E_{h-1,p}.
$$
沿用 [R271 占据交换子稿](R271-appendix-occupation-commutator-known-source-minimum-energy.md) 的实际第一下降块
$$
A_2=D|_{U_{2,2}}:U_{2,2}\to K_1,\qquad
K_1=\ker D\cap\mathcal H_1,
$$
$$
A_3=P_{U_{2,2}}D|_{U_{3,3}}:U_{3,3}\to U_{2,2}.
$$
本稿反驳
$$
A_3A_3^*\le 2A_2^*A_2.                         \tag{1.1}
$$
因此它同时反驳任意正异权下的一般式
$A_{h+1}A_{h+1}^*\le h/(h-1)\,A_h^*A_h$。

这里没有把 $A_3^*$ 换成环境 $D^*$。也没有把 primitive Gram 的“先取环境逆、再压缩”换成压缩后求逆。

## 2. 一个强位与六个相同弱位

更一般，先取一个强位 $0$ 和 $r\ge3$ 个弱位，令
$$
D=E_0+\varepsilon\sum_{j=1}^rE_j,\qquad\varepsilon>0.
$$
弱位的规范对称向量记为
$$
w_k=\binom rk^{-1/2}\sum_{\substack{I\subseteq\{1,\ldots,r\}\\|I|=k}}e_I.
$$
写 $w_k$ 时强位无孔，写 $e_0w_k$ 时强位有孔。准确有
$$
Dw_k=\varepsilon\sqrt{k(r-k+1)}\,w_{k-1},
$$
$$
D(e_0w_k)=w_k+
\varepsilon\sqrt{k(r-k+1)}\,e_0w_{k-1}.        \tag{2.1}
$$
因此
$$
g=\frac{w_1-\varepsilon\sqrt r\,e_0}{\sqrt{1+r\varepsilon^2}}
\in K_1,\qquad\|g\|=1.                       \tag{2.2}
$$

定义
$$
v_2=
\frac{-e_0w_1+
\dfrac{2}{\varepsilon\sqrt{2(r-1)}}w_2}
{\sqrt{1+r\varepsilon^2}},
\tag{2.3}
$$
$$
v_3=
\frac{-\dfrac{1}{\varepsilon\sqrt{2(r-1)}}e_0w_2+
\dfrac{3}{\varepsilon^2\sqrt{6(r-1)(r-2)}}w_3}
{\sqrt{1+r\varepsilon^2}}.
\tag{2.4}
$$
由 (2.1) 逐项计算，
$$
Dv_2=g,\qquad D^2v_3=g.
\tag{2.5}
$$
所以 $v_2\in\ker D^2$、$v_3\in\ker D^3$。

### 2.1 两个向量确为全空间最小逆

弱位置换群 $S_r$ 酉作用于整个布尔空间，并与 $D$、各实际核投影交换。
其平均是到弱位对称子空间的正交投影，记为 $P_{\rm sym}$。

第2孔层的对称空间是
$\operatorname{span}\{e_0w_1,w_2\}$。
$D$ 到第1孔层对称空间
$\operatorname{span}\{e_0,w_1\}$ 的矩阵为
$$
\begin{pmatrix}
\varepsilon\sqrt r&0\\
1&\varepsilon\sqrt{2(r-1)}
\end{pmatrix};
$$
它可逆。因此对每个 $z\in\ker D\cap\mathcal H_2$，
$P_{\rm sym}z=0$，而 $v_2$ 对称，故 $v_2\perp z$。
结合 (2.5)，
$$
v_2\in U_{2,2},
$$
并且它是整个 $\mathcal H_2$ 中 $Dv=g$ 的唯一最小范数解。

同样，第3孔层对称空间为
$\operatorname{span}\{e_0w_2,w_3\}$，
$D^2$ 到第1孔层对称空间的矩阵是
$$
\begin{pmatrix}
\varepsilon^2\sqrt{2r(r-1)}&0\\
2\varepsilon\sqrt{2(r-1)}
 &\varepsilon^2\sqrt{6(r-1)(r-2)}
\end{pmatrix}.
$$
它也可逆，所以 $v_3\perp\ker D^2\cap\mathcal H_3$。
由 (2.5)，
$$
v_3\in U_{3,3},
$$
并且是全空间 $D^2v=g$ 的唯一最小范数解。

这一步排除了“只在一个 $D$ 不变小空间求逆”的漏洞。
平均整个核后为零，才得到与完整核的正交性。

## 3. 真实第一下降及准确反例数值

记
$$
a=\|v_2\|^2
=\frac{1+2/((r-1)\varepsilon^2)}{1+r\varepsilon^2},
$$
$$
b=\|v_3\|^2
=\frac{1/(2(r-1)\varepsilon^2)
 +3/(2(r-1)(r-2)\varepsilon^4)}
 {1+r\varepsilon^2}.                         \tag{3.1}
$$
由 $D^2v_3=g$，$Dv_3$ 在 $U_{2,2}$ 上的投影是 $Dv=g$ 的最小解，故
$$
A_3v_3=v_2.                                  \tag{3.2}
$$

对称的 $U_{2,2}$ 和 $U_{3,3}$ 都是一维。
确实，前述两对称层均为二维，$D^2$ 或 $D^3$ 到真空层均为非零的一行映射，而对应前一次幂的核在该对称层为零。
所以这两个对称高度空间分别由 $v_2,v_3$ 张成。

令
$$
f_2=v_2/\sqrt a,\qquad f_3=v_3/\sqrt b.
$$
$A_3^*$ 也与弱位置换交换，因此 (3.2) 准确给
$$
A_2f_2=g/\sqrt a,\qquad
A_3^*f_2=\sqrt{a/b}\,f_3.                    \tag{3.3}
$$
于是原 Loewner 差在这个实际单位向量上的二次型为
$$
\langle(2A_2^*A_2-A_3A_3^*)f_2,f_2\rangle
=\frac2a-\frac ab.                           \tag{3.4}
$$

现在取
$$
\boxed{r=6,\qquad\varepsilon=1/10.}
$$
模型恰有七个位，所有权严格为正。
(3.1) 成为
$$
a=\frac{2050}{53},\qquad b=\frac{38000}{53}.
$$
因此
$$
\|A_3^*f_2\|^2=\frac{41}{760},\qquad
2\|A_2f_2\|^2=\frac{53}{1025},
$$
$$
\boxed{
\langle(2A_2^*A_2-A_3A_3^*)f_2,f_2\rangle
=-\frac{349}{155800}<0.
}
\tag{3.5}
$$
这已是 (1.1) 的完整准确反例，无需浮点符号判断。

相应的 primitive 最小逆比为
$$
\boxed{
\frac{a^2}{b}=\frac{8405}{4028}
=2+\frac{349}{4028}>2.
}
\tag{3.6}
$$
这里 $a,b$ 也分别是 $J_2^*J_2$、$J_3^*J_3$ 在唯一对称 primitive 直线上的真实本征值；没有假设一般 primitive Gram 彼此交换。

## 4. 反例并非孤立参数

令 $t=\varepsilon^2$，(3.1) 给
$$
\frac{a^2}{b}
=
\frac{2(r-2)((r-1)t+2)^2}
{(r-1)(1+rt)((r-2)t+3)}.
\tag{4.1}
$$
当 $t\downarrow0$ 时，该比趋于
$$
\frac{8(r-2)}{3(r-1)}.
$$
任意 $r\ge6$ 都使该极限严格大于2。
更准确，(4.1) 大于2恰等价于
$$
r-5>6(r-1)t+(r-1)(r-2)t^2.
\tag{4.2}
$$
所以相邻第一下降的普遍常数若存在，在 $h=2$ 至少须达到 $8/3$；
让 $r\to\infty$ 再取足小的 $t$ 即得这个必要下界。
本稿没有证明常数 $8/3$ 足够，也没有证明存在与异权或位数无关的有限常数。

## 5. 对原连续尾候选的范围

原边界问题固定的是连续尾 $b_j=(j+1)^{-2}$。
七位向量 $(1,1/10,\ldots,1/10)$ 并不是这个连续尾的整体截断。

若从连续尾挑选一个强位和一组相近弱位，未选的中间位仍属于完整 $D$。
它们的删除作用、正交核和最小原像不能免费删去。
因此本稿不能把 (3.5) 直接移植到原连续尾。

它准确关闭的是“先证明任意正异权布尔模型中的 (1.1)，再取连续尾极限”的路线。
原连续尾本身是否仍满足某个有用的相邻第一下降序，或者能否直接在实际 Schur 源上取较弱界，尚须独立证明。

后续的真实连续尾运输已由[相邻暗对与完整最小原像证明](R271-appendix-dark-pair-transfer-and-continuous-tail-adjacent-descent-counterexample.md)支付：保留全部未选位和无限远尾，原连续尾在所有足大头及全部指定高孔层也不满足常数2；真实比较常数的渐近必要下界为8/3。该后续步骤使用对偶下界和显式试探上界，并未直接删位移植本稿。更大常数及只针对实际窄Schur源的比较仍需另证。
