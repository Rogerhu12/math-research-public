# 工作补充：精细相邻 primitive Gram 上界的七位精确反例

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c。AI 辅助：GPT-6 Astra Pro。

正式记录：[R239 附录](../results/R239-appendix-seven-site-counterexample-to-refined-primitive-gram-comparison.md)。

状态：下述有限反例有完整代数证明及独立可运行的 BigInt 有理证书。它否定精细常数猜想，不否定常数 1 的一般相邻比较，也不对原边界窄源或普通 ISP 作结论。

本稿接 [原精细 Gram 猜想记录](2026-11-13-primitive-gram-finite-newton-comparison-probe-0c.md)。下文使用同一对象，保留先全逆、再压核的定义。

## 1. 保留完整逆的原对象

在七位有限布尔 Hilbert 空间中，令删除算子为
$$
D=\sum_{j=1}^7 a_jE_j,\qquad
(a_1,\ldots,a_7)=(3,3,3,3,3,1,1).
$$
其中
$$
E_je_S=
\begin{cases}
e_{S\setminus\{j\}},&j\in S,\\
0,&j\notin S.
\end{cases}
$$
记
$$
\mathcal H_s=\operatorname{span}\{e_S:|S|=s\},\qquad
K_2=\ker D\cap\mathcal H_2.
$$
定义与猜想完全相同的算子
$$
F_k=\frac{D^k(D^*)^k|_{\mathcal H_2}}{(k!)^2},
\qquad
\Gamma_k=P_{K_2}F_k^{-1}|_{K_2}.
\tag{1.1}
$$
这里先在整个二孔层上取逆，再压到删除核。所需全孔层的逆存在：$7\ge 2\cdot2+k$（$k\le3$），正权有限删除算子的满射性见 [R271 两簇稿 §6.1](../results/R271-appendix-two-cluster-minimal-inverses-and-squared-all-height-comparison-lower-bounds.md) 的等权串与正对角相似证明。

我们检验的参数为
$$
N=7,\qquad s=2,\qquad n=2.
$$
确有
$$
1\le n<N-2s=3.
$$
猜想常数是
$$
c_{7,2,2}
=\frac{4}{5}\frac{1}{2}=\frac25.
\tag{1.2}
$$

## 2. 三维对称块和唯一 primitive 方向

把前五位称为强组，后两位称为弱组。令
$$
v_0=e_{\{6,7\}},
$$
$$
v_1=\sum_{\substack{1\le i\le5\\6\le j\le7}}e_{\{i,j\}},
\qquad
v_2=\sum_{1\le i<j\le5}e_{\{i,j\}}.
$$
它们是两组分别置换下的全部二孔不变向量。这个基正交，但没有归一化：
$$
\bigl(\|v_0\|^2,\|v_1\|^2,\|v_2\|^2\bigr)=(1,10,10).
\tag{2.1}
$$
一孔层的组对称部分由
$$
w_0=e_{\{6\}}+e_{\{7\}},
\qquad
w_1=\sum_{i=1}^5e_{\{i\}}
$$
张成。直接删除给
$$
Dv_0=w_0,\qquad
Dv_1=15w_0+2w_1,\qquad
Dv_2=12w_1.
\tag{2.2}
$$
因此这个三维块中的 primitive 部分恰是一维：
$$
\boxed{f=90v_0-6v_1+v_2,\qquad Df=0.}
\tag{2.3}
$$
它的原 Hilbert 范数为
$$
\boxed{\|f\|^2=90^2+10\cdot6^2+10=8470.}
\tag{2.4}
$$

组置换与完整 D、D*、各 F_k 以及 P_K 都交换。因此它们的不变三维块是 F_k 的约化子空间，先在整个孔层取 F_k^{-1} 再作用于这个块，等于这个完整三维块的逆。不是先把 F_k 压到一维 primitive 线后再取逆。

最后，Gamma_k 保持组对称的 primitive 线，故存在正数 gamma_k 使
$$
\Gamma_k f=\gamma_k f,\qquad
\gamma_k=\frac{\langle F_k^{-1}f,f\rangle}{\|f\|^2}.
\tag{2.5}
$$
这里仅在明确的一维线使用共同特征向量；没有假设三个完整 Gamma 算子相互交换。

## 3. 三个完整 Gram 块及实际逆像

相对于依次排列的基
$$
(v_0,v_1,v_2),
$$
完整 F_1、F_2、F_3 的矩阵分别是
$$
M_1=
\begin{pmatrix}
45&30&0\\
3&74&12\\
0&12&83
\end{pmatrix},
\tag{3.1}
$$
$$
M_2=
\begin{pmatrix}
810&1080&90\\
108&1602&498\\
9&498&1621
\end{pmatrix},
\tag{3.2}
$$
$$
M_3=
\begin{pmatrix}
7290&14580&2430\\
1458&14580&6318\\
243&6318&10287
\end{pmatrix}.
\tag{3.3}
$$
它们相对于 (2.1) 的度量自伴。不能因为这些坐标矩阵不对称，就改用欧氏三维内积。

这些条目可逐对验证。对二元集合 R、T，置
$$
\delta=|R\setminus T|.
$$
则
$$
(F_k)_{R,T}
=
\left(\prod_{i\in R\triangle T}a_i\right)
e_{k-\delta}\left(a_i^2:i\notin R\cup T\right),
\tag{3.4}
$$
其中负次数的初等对称多项式取零。把列 T 按三种组类型求和，便得到 (3.1)—(3.3)。本稿证书用 BigInt 逐项执行这一步，而非将矩阵常数当作未检验输入。

令列向量
$$
b=(90,-6,1)^{\mathsf T}.
$$
准确的三个全块逆像为
$$
M_1^{-1}b=
\begin{pmatrix}514/243\\-14/81\\1/27\end{pmatrix},
\quad
M_2^{-1}b=
\begin{pmatrix}94/729\\-10/729\\1/243\end{pmatrix},
\quad
M_3^{-1}b=
\begin{pmatrix}38/2187\\-2/729\\1/729\end{pmatrix}.
\tag{3.5}
$$
每式只需乘回相应整数矩阵即可核验。

以 Gram 对角矩阵
$$
G=\operatorname{diag}(1,10,10)
$$
计算原内积，得到
$$
b^{\mathsf T}GM_1^{-1}b=\frac{1810}{9},
\quad
b^{\mathsf T}GM_2^{-1}b=\frac{1010}{81},
\quad
b^{\mathsf T}GM_3^{-1}b=\frac{1270}{729}.
\tag{3.6}
$$
除以 8470 后，
$$
\boxed{
\gamma_1=\frac{181}{7623},\qquad
\gamma_2=\frac{101}{68607},\qquad
\gamma_3=\frac{127}{617463}.
}
\tag{3.7}
$$

## 4. 精确负二次型

在 f 所在共同特征线上，猜想要求
$$
\frac{\gamma_2^2}{\gamma_3}
\le\frac25\gamma_1.
$$
实际归一化比却为
$$
\boxed{
\frac{\gamma_2^2}{\gamma_3\gamma_1}
=\frac{10201}{22987}
>\frac25,
}
\tag{4.1}
$$
因为
$$
5\cdot10201-2\cdot22987=5031>0.
$$
更直接地，
$$
\boxed{
\left\langle
\left(\frac25\Gamma_1
-\Gamma_2\Gamma_3^{-1}\Gamma_2\right)f,f
\right\rangle
=-\frac{1118}{127}<0.
}
\tag{4.2}
$$
若使用原全孔层探针输出的缩放向量 f/90，则同一个负二次型为
$$
-\frac{559}{514350}.
\tag{4.3}
$$
这也是原精确 LDL 程序在该输入的最后负主元见证值；(4.2) 已提供无需信任消元过程的独立三维证明。

## 5. 可复核证书与结论范围

[精确 JavaScript 证书](2026-11-13-finite-primitive-gram-refined-bound-counterexample-central.mjs) 无外部依赖，检查：

1. 真实删除核条件和原范数 8470；
2. 从逐集合公式 (3.4) 构造三个完整 Gram 块；
3. 非归一组基的加权自伴性；
4. 将 (3.5) 的实际逆像逐一乘回原块；
5. 三个 gamma、精确归一化比和两个负有理二次型。

本轮在 V8 中执行同一核心函数，输出
`EXACT_COUNTEREXAMPLE_PASS`。终端离线，因此不声称运行过 Node 命令行封装。终端恢复后可直接用 Node 执行归档脚本。

这个例子证明，固定 N=7、s=2、n=2 时，任何对所有正权成立的常数至少要满足
$$
c\ge\frac{10201}{22987}\approx0.4437725671.
\tag{5.1}
$$
(5.1) 是明确源给出的必要下界，未声称是这些参数下的最优常数或完整算子的最大特征值。

由于该比仍小于 1，这一见证没有否定常数 1 的较弱不等式。此前有限探针的五组正定输入仍是有效的有限证据，但不能继续支持精细常数的一般上界。原 R271 两簇稿的既有必要下界也不受影响；被否定的是将其特定两簇下界直接猜成所有正权的普遍上界。

无论较弱常数 1 是否成立，本有限反例都不识别原边界的真实 Schur 窄源，不删除原长头项或返回费用，不推出普通 ISP 的任何完成结论。
