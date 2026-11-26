# 原伴随的负前缀完成域与一个实际除法图核心扇区

日期：2026-11-27（Asia/Taipei）；2026-11-26（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：本稿实际有界延拓、图核心扇区、无条件多项式阶阈值和更大的输出条件核心均已证明；整个除法核心及 $N=M$ 仍未完成。**
接原 [闭关系与两个不同范围核心](../results/R271-appendix-actual-formal-division-closed-relation-and-two-range-cores.md)。本稿给第一道核心中一个明确、严格超出普通 Hilbert 来源的已付款域，保留每个首零位后的全部 primitive 和尾向量。并不声称真正 $W$ 的规范形式原像已落在此域。

## 1. 原算子和负前缀空间

仍取
$$
Be_n=\alpha_{v_2(n)}e_{n-1},\quad Be_0=0,\qquad
\mathsf N_i=B^{2^i}/d_i,\quad
\mathsf Y_i=\mathsf N_i(I+\mathsf N_i)^{-1},
$$
$$
T_N=\sum_{i\ge0}a_i\mathsf N_i,
\qquad T_Y=\sum_{i\ge0}a_i\mathsf Y_i,
\qquad a_i=(i+1)^{-2}.
$$
记 $S=B^*$，以及
$$
\eta_i=\alpha_{i+1}/\alpha_i\le e^{-770\,16^i},
\qquad \varepsilon=e^{-770}.
$$
由 $770(16^i-1)\ge i\log2$，可统一使用
$$
\eta_i\le\varepsilon2^{-i}.
\tag{1.1}
$$

对整数 $n\ge0$ 令 $q(n)=v_2(n+1)$。$P_q$ 是首个零位恰在 $q$ 的投影：低 $q$ 位全占据，第 $q$ 位空，其余位完全任意。于是
$$
I=\sum_{q\ge0}P_q
$$
按强算子拓扑成立，且各项正交。对 $\beta\ge0$ 定义完成空间
$$
\mathcal Y_{-\beta}
=\left\{x:\sum_{q\ge0}(q+1)^{-2\beta}\|P_qx\|^2<\infty\right\},
$$
$$
\|x\|_{-\beta}^2
=\sum_{q\ge0}(q+1)^{-2\beta}\|P_qx\|^2.
\tag{1.2}
$$
它是相应正权序列 Hilbert 空间，允许普通范数无穷的形式向量；每个坐标泛函连续，有限支撑向量稠密。每个 $P_qx$ 自身仍属于原 Hilbert 空间。

**定理 1.1。** 两个原伴随均有唯一有界延拓
$$
\boxed{
\widetilde T_\bullet^*:\mathcal Y_{-1}\longrightarrow\mathcal H,
\qquad \|\widetilde T_\bullet^*\|<3,
\quad \bullet\in\{N,Y\}.
}
\tag{1.3}
$$
原 $S$ 也有延拓
$$
\boxed{\widetilde S:\mathcal Y_{-1}\longrightarrow\mathcal H,
\qquad \|\widetilde S\|\le\alpha_0.}
\tag{1.4}
$$
这些延拓在每个有限输出坐标上就是原形式级数；没有另造算子符号。

## 2. 纯创建的全尾分解

先在有限支撑 $x$ 上写 $x_q=P_qx$，以及
$$
D^*=\sum_{i\ge0}a_iE_i^*.
$$
若 $i<q$，则 $E_i^*x_q=0$；若 $i>q$，创建保留首零位 $q$；若 $i=q$，创建把首零位移到更高处。因此准确分成
$$
D^*x
=\sum_{q\ge0}D_{>q}^*x_q
 +\sum_{q\ge0}a_qE_q^*x_q,
\qquad D_{>q}^*=\sum_{i>q}a_iE_i^*.
\tag{2.1}
$$
第一和的各项属于相互正交的 $P_q\mathcal H$。积分比较给
$$
\|D_{>q}^*\|\le\sum_{i>q}a_i\le(q+1)^{-1},
$$
从而
$$
\left\|\sum_qD_{>q}^*x_q\right\|\le\|x\|_{-1}.
\tag{2.2}
$$
第二和不被称为正交和。实际使用三角不等式和标量 Cauchy--Schwarz：
$$
\begin{aligned}
\left\|\sum_qa_qE_q^*x_q\right\|
&\le\sum_qa_q\|x_q\|\\
&\le\left[\sum_q a_q^2(q+1)^2\right]^{1/2}
       \|x\|_{-1}
<\sqrt2\,\|x\|_{-1}.
\end{aligned}
\tag{2.3}
$$
所以
$$
\boxed{\|D^*x\|\le(1+\sqrt2)\|x\|_{-1}.}
\tag{2.4}
$$
尤其 (2.1) 保留首零位以后的整个物理空间，不只作用于真空、固定孔层或一个对称列。

## 3. 原 carry 与 Y 型全部逆

原加法进位给：当 $q=i$ 时
$(\mathsf N_i^*-E_i^*)P_q=0$；当 $q>i$ 时
$$
\|\mathsf N_i^*P_qx\|
=\frac{\alpha_q}{\alpha_i}\|P_qx\|,
\qquad E_i^*P_q=0.
\tag{3.1}
$$
当 $q<i$ 时，进位可能非零，但它保留首零位 $q$，其普通范数至多 $\eta_i$。
因此在 $\bigoplus_{q<i}P_q\mathcal H$ 上，差算子从 $\mathcal Y_{-1}$ 到 $\mathcal H$ 的范数至多 $i\eta_i$，且输出仍在同一正交直和中。
在 $q>i$ 的部分，$\mathsf N_i^*$ 是单个加权前移，不同 $q$ 的输入仍有不相交输出坐标，并且全部输出的首零位为 $i$，与前一部分正交。
由于 $(q+1)\alpha_q$ 递减，两部分取最大值即给
$$
\boxed{
\|\mathsf N_i^*-E_i^*\|_{\mathcal Y_{-1}\to\mathcal H}
\le(i+2)\eta_i.
}
\tag{3.2}
$$
这里 $(q+2)\alpha_{q+1}\le(q+1)\alpha_q$ 直接由 $\eta_q<1/2$ 得到。
因 $a_i(i+2)\le2$，(1.1) 给
$$
\|T_N^*-D^*\|_{\mathcal Y_{-1}\to\mathcal H}
\le\sum_i a_i(i+2)\eta_i\le4\varepsilon.
\tag{3.3}
$$

另有
$$
\|E_i^*\|_{\mathcal Y_{-1}\to\mathcal H}\le i+1,
$$
因为它在 $\bigoplus_{q>i}P_q\mathcal H$ 上为零。结合 (3.2)，
$$
\|\mathsf N_{i+1}^*\|_{\mathcal Y_{-1}\to\mathcal H}
\le(i+2)+(i+3)\eta_{i+1}\le2(i+3).
\tag{3.4}
$$
真实身份 $\mathsf N_i^2=\eta_i\mathsf N_{i+1}$ 和原逆范数 $\|(I+\mathsf N_i^*)^{-1}\|\le3$ 给
$$
\mathsf Y_i^*-\mathsf N_i^*
=-\eta_i(I+\mathsf N_i^*)^{-1}\mathsf N_{i+1}^*.
$$
最后一个因子先从 $\mathcal Y_{-1}$ 进到 $\mathcal H$，再作用原有界逆，故不要求该逆在未知的加权空间中有界。于是
$$
\begin{aligned}
\|T_Y^*-T_N^*\|_{\mathcal Y_{-1}\to\mathcal H}
&\le6\sum_i a_i(i+3)\eta_i\\
&\le36\varepsilon,
\end{aligned}
\tag{3.5}
$$
其中用了 $a_i(i+3)\le3$。
(2.4)、(3.3)、(3.5) 给统一界
$$
\|T_\bullet^*x\|\le
(1+\sqrt2+40\varepsilon)\|x\|_{-1}<3\|x\|_{-1},
$$
证明 (1.3)。所有误差和级数在所声明的算子范数中收敛。

最后 $S$ 在 $P_q\mathcal H$ 上正好乘权 $\alpha_q$ 并等距前移，故
$$
\|Sx\|^2=\sum_q\alpha_q^2\|x_q\|^2
\le\alpha_0^2\|x\|_{-1}^2.
$$
这证明 (1.4)。

## 4. 已支付的真实图核心扇区

沿用前稿 $G_0=TJ_B$、$G_0^*$ 的最大域
$$
\mathcal D(G_0^*)=\{y:T^*y\in\operatorname{Ran}S\},
\qquad SG_0^*y=T^*y.
$$
对 $x\in\mathcal Y_{-1}$，取有限支撑 $x_n\to x$ 于 $\mathcal Y_{-1}$。令
$$
y=\widetilde Sx,\qquad z=\widetilde T^*x.
$$
定理 1.1 给 $Sx_n\to y$、$T^*x_n\to z$ 于原 Hilbert 范数。
又 $T^*Sx_n=ST^*x_n$，由原 $S,T^*$ 的有界性，
$$
T^*y=Sz.
$$
所以
$$
\boxed{
y\in\mathcal D(G_0^*),\qquad G_0^*y=z,
\qquad (Sx_n,G_0^*Sx_n)\longrightarrow(y,G_0^*y).
}
\tag{4.1}
$$
这是真正两分量的图范数逼近，非仅形式逐坐标逼近。

因此已付扇区可写为
$$
\mathcal D_{\rm pref}=\widetilde S\mathcal Y_{-1}
$$
$$
\boxed{
\mathcal D_{\rm pref}
=\left\{y:y_0=0,
\sum_{n\ge1}
\frac{|y_n|^2}
{(v_2(n)+1)^2\alpha_{v_2(n)}^2}<\infty\right\}.
}
\tag{4.2}
$$
所列和有限已保证 $y\in\mathcal H$。此扇区严格大于 $S\mathcal H$：取
$$
x=\sum_{q\ge0}e_{2^q-1}\in\mathcal Y_{-1}\setminus\mathcal H,
\qquad
y=\sum_{q\ge0}\alpha_qe_{2^q},
$$
则 $y\in\mathcal D_{\rm pref}$，而单射前移的唯一形式原像 $x$ 不在 $\mathcal H$，故 $y\notin S\mathcal H$。

更直接地，有限逼近还给
$$
\boxed{
\widetilde T^*(\mathcal Y_{-1})
\subset\overline{\operatorname{Ran}T^*}=\mathcal I.
}
\tag{4.3}
$$
没有把左侧或右侧称作未闭的 $\operatorname{Ran}T^*$ 本身。

## 5. 真正 W 来源上的明确充分成本

设 $w\in W=M\ominus N$。[既有稳定范围真空结论](R271-appendix-anisotropic-high-bit-averaging-modulo-stable-range-and-formal-readout.md)给 $e_0\in N$，所以 $w_0=0$。
由于 $T^*=M_F$ 的形式阶数为 1、首项非零，存在唯一形式向量 $h(w)$ 满足
$$
T^*h(w)=w.
\tag{5.1}
$$
这里先按系数递推定义 $h(w)$，不假定它属于任何 Hilbert 域。

若同一来源支付了
$$
\boxed{
\sum_{n\ge0}
\frac{|h(w)_n|^2}{(v_2(n+1)+1)^2}<\infty,
}
\tag{5.2}
$$
则 $h(w)\in\mathcal Y_{-1}$；(1.3) 的输出与 (5.1) 在每个有限坐标一致，因此 $w=\widetilde T^*h(w)\in\mathcal I$。又 $w\in M=\mathcal I^\perp$，故
$$
\boxed{(5.2)\Longrightarrow w=0.}
\tag{5.3}
$$
相比要求 $h(w)\in\mathcal H$，(5.2) 真正允许沿坏前缀有一阶多项式范数损失；其余所有尾和 primitive 仍使用原普通范数。尚未证明一般真正 $w\in W$ 自动满足 (5.2)。

## 6. 无附加来源条件的多项式阶 1 是准确阈值

对任何 $\beta>1$，原 $T_N^*$ 或 $T_Y^*$ 都不能有一个对全部 $\mathcal Y_{-\beta}$ 有界到 $\mathcal H$ 的延拓。

证明：对 $q\ge1$ 取单位乘积向量 $x^{(q)}$，令低 $q$ 位全占，第 $q$ 位空，第 $q+1,\ldots,2q$ 位均取 $(|0\rangle+|1\rangle)/\sqrt2$，更高位取真空。它准确属于 $P_q\mathcal H$，故
$$
\|x^{(q)}\|_{-\beta}=(q+1)^{-\beta}.
$$
纯尾在这一块的输出给
$$
\begin{aligned}
\|P_qD^*x^{(q)}\|
&=\|D_{>q}^*x^{(q)}\|\\
&\ge\langle D_{>q}^*x^{(q)},x^{(q)}\rangle
=\frac12\sum_{i=q+1}^{2q}a_i
\ge\frac1{18q}.
\end{aligned}
\tag{6.1}
$$
低 $i<q$ 的实际 $\mathsf N_i^*$ carry 范数为 $\alpha_q/\alpha_i$；Y 型最多再付逆范数 3。高 $i\ge q$ 的纯创建差满足
$\|\mathsf N_i^*-E_i^*\|\le\eta_i$、
$\|\mathsf Y_i^*-E_i^*\|\le4\eta_i$。
故两型统一有
$$
\|P_q(T_\bullet^*-D^*)x^{(q)}\|
\le6e^{-770\,16^{q-1}}+8e^{-770\,16^q}
\le14e^{-770\,16^{q-1}}
<\frac1{36q}.
\tag{6.2}
$$
低纯创建为零，第 $q$ 个纯创建离开 $P_q$，因此这里保留的主项就是 (6.1)，无多算的低位项。于是
$$
\frac{\|T_\bullet^*x^{(q)}\|}
 {\|x^{(q)}\|_{-\beta}}
\ge\frac{(q+1)^\beta}{36q}\longrightarrow\infty.
\tag{6.3}
$$
这证明所述阈值。它不排除在额外支付来源关系或对角尾能量后扩大域；只排除免费把 (1.3) 的整个全 primitive 域改成更大的多项式阶。

## 7. 对偶输出域

(1.3) 还给整个原 $T$ 的连续正前缀输出估计
$$
\boxed{
\sum_{q\ge0}(q+1)^2\|P_qTf\|^2\le9\|f\|^2
\qquad(f\in\mathcal H).
}
\tag{7.1}
$$
这是 (1.2) 配对下的直接伴随，不是对核向量重新假定加权正则性。

下一节继续使用准确输出已经在 $\mathcal H$ 中这一来源条件，得到严格更大的图核心；它不要求在整个更大加权空间上有 (1.3) 那样的无条件有界延拓。

## 8. 已知准确输出时的更大核心：接近负三半阶

定义完整块范数
$$
\mathfrak b(h)=\sum_{q\ge0}a_q\|P_qh\|,
\qquad
\mathcal B_{\rm pref}=\{h:\mathfrak b(h)<\infty\}.
\tag{8.1}
$$
各块仍在原 Hilbert 空间，块后全部 primitive 不截断。
在此空间上，(2.1) 的改首零位部分
$$
Rh=\sum_qa_qE_q^*P_qh
$$
按原范数绝对收敛，$\|Rh\|\le\mathfrak b(h)$。

记实际余项 $K_\bullet=T_\bullet^*-D^*$。对 $q\ge1$，同 (6.2) 的低、高位分割给
$$
\|K_\bullet P_q\|
\le6e^{-770\,16^{q-1}}+8e^{-770\,16^q}
\le14e^{-770\,16^{q-1}};
$$
当 $q=0$ 时可用 $8\varepsilon$。因为
$$
\sup_{q\ge1}(q+1)^2\,2^{-(q-1)}=9/2,
$$
(1.1) 蕴含统一界
$$
\boxed{\|K_\bullet P_q\|\le64\varepsilon a_q\quad(q\ge0).}
\tag{8.2}
$$
因此 $K_\bullet h=\sum_qK_\bullet P_qh$ 也绝对收敛，且
$$
\|K_\bullet h\|\le64\varepsilon\,\mathfrak b(h).
\tag{8.3}
$$
又 $(q+1)^2\alpha_q\le\alpha_0$，故
$$
\|\widetilde Sh\|\le\alpha_0\mathfrak b(h).
\tag{8.4}
$$

**定理 8.1（准确输出条件核心）。** 设 $h\in\mathcal B_{\rm pref}$，并且原形式伴随的准确输出
$$
f=T_\bullet^*h
\tag{8.5}
$$
属于 $\mathcal H$。则 $f\in\mathcal I$，而 $y=\widetilde Sh$ 属于 $G_0^*$ 的真实图核心：存在 $h_n\in\mathcal H$，使
$$
Sh_n\to y,\qquad T_\bullet^*h_n\to f,
\qquad G_0^*y=f.
\tag{8.6}
$$
$h_n$ 还可以选为有限支撑。

证明。先令 $h^{[Q]}=\sum_{q=0}^QP_qh\in\mathcal H$。纯创建的保首零位部分为块对角算子
$$
Ah=\bigoplus_{q\ge0}D_{>q}^*P_qh.
$$
每一个块均定义良好；此时尚不假定整个直和在 $\mathcal H$ 中。
由于原前移型形式级数每个有限输出行只含有限个输入坐标，(2.1) 及实际 carry 的逐行身份仍给
$$
Ah=f-Rh-K_\bullet h.
\tag{8.7}
$$
右侧由 (8.3)、(8.5) 属于 $\mathcal H$，所以整个块对角输出实际平方可和。正交块截断因而满足
$$
Ah^{[Q]}\longrightarrow Ah.
$$
另由 (8.1)--(8.4)，$Rh^{[Q]}\to Rh$、$K_\bullet h^{[Q]}\to K_\bullet h$ 和 $Sh^{[Q]}\to y$。
因此
$$
T_\bullet^*h^{[Q]}
=Ah^{[Q]}+Rh^{[Q]}+K_\bullet h^{[Q]}
\longrightarrow f.
$$
这同时证明 $f\in\mathcal I$。对 $T^*Sh^{[Q]}=ST^*h^{[Q]}$ 取极限，得到 $T^*y=Sf$，故 (4.1) 的真实域判据给 $G_0^*y=f$。
最后，对每个普通 Hilbert 向量 $h^{[Q]}$ 作有限支撑逼近，并用原 $S,T^*$ 有界性取对角序列，即得有限支撑版本。证毕。

对任意 $\beta<3/2$，Cauchy--Schwarz 给
$$
\mathfrak b(h)
\le\left[\sum_{q\ge0}(q+1)^{2\beta-4}\right]^{1/2}
\|h\|_{-\beta}.
\tag{8.8}
$$
所以，**对已经知道 $T^*h\in\mathcal H$ 的来源**，整个 $\mathcal Y_{-\beta}$、$\beta<3/2$ 都满足上述核心判据。
端点还可取任意 $\delta>0$ 的范数条件
$$
\sum_{q\ge0}
\frac{(\log(q+2))^{1+\delta}}{(q+1)^3}\|P_qh\|^2<\infty,
\tag{8.9}
$$
因为相应 Cauchy--Schwarz 的另一因子是收敛的
$\sum_{q\ge0}[(q+1)(\log(q+2))^{1+\delta}]^{-1}$。
这里不声称 $\beta=3/2$ 的无对数端点失败或成立。

这个输出条件核心严格超过第 4 节扇区。例如
$$
h=\sum_{q\ge0}\sqrt{q+1}\,e_{2^q-1}
$$
满足 $\mathfrak b(h)<\infty$，但 $h\notin\mathcal Y_{-1}$。
对它，块对角项的准确正交创建范数满足
$$
\sum_q\|D_{>q}^*P_qh\|^2
=\sum_q(q+1)\sum_{i>q}(i+1)^{-4}
\le\frac13\sum_q(q+1)^{-2}<\infty.
$$
故 $T^*h=Ah+Rh+K_\bullet h\in\mathcal H$，确实适用定理 8.1，而不是只给一个未核输出域的形式例子。

## 9. 同一真正 W 的当前充分费用

对第 5 节的唯一规范形式原像 $h(w)$，准确输出本来就是 $w\in\mathcal H$。
因此定理 8.1 将 (5.2) 放宽为
$$
\boxed{
\sum_{q\ge0}\frac{\|P_qh(w)\|}{(q+1)^2}<\infty
\quad\Longrightarrow\quad w=0.
}
\tag{9.1}
$$
各块必须属于原 Hilbert 空间。任一 (8.8) 或 (8.9) 的费用是 (9.1) 的明确充分输入。
本稿没有证明一般真正 $w\in W$ 自动支付这些费用，也没有将总孔数截断的已有形式原像界换成首零位块的整个普通范数。
整个最大乘法域的图核心、第二道精确可除值域的稠密性及 $N=M$ 仍需继续。实际 $\alpha_q^{-1}$ 权和母支持窗口没有被这些前缀费用替换。
