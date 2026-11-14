# R564 恢复：两个实际有理核的完整 Cartier 交换

日期：2026-11-14。状态：**已证明。**

恢复说明：本稿只恢复后续 R601 所需的原 R564 短恒等式，并给自包含证明；不声称原文件字节或旧高权 \(C_p\) 讨论已恢复。它是固定曲线上的代数微分恒等式，不自行产生真实模曲线商的全局非消失或秩结论。

## 1. 规范与精确公式

设 \(p\ge5\)、\(p\equiv5\pmod6\)。在 \(k=\overline{\mathbb F}_p\) 上取

\[
 E_0:y^2=x^3-1,\qquad \omega=dx/(2y),
\]
\[
 \Delta(x)=x^9-228x^6+48x^3-64,
\]
\[
 R_-(x)=\frac{x^2(x^6+34x^3-8)}{\Delta(x)},\qquad
 R_+(x)=\frac{x^2(x^6-20x^3-8)}{\Delta(x)}.
\tag{564R.1}
\]

令 \(\alpha\in\mathbb F_p\) 是 \(\alpha^3=4\) 的唯一解，取 \(\beta^2=3\)，并置

\[
 \varepsilon=\left(\frac3p\right),\qquad
 c=\frac{\varepsilon\alpha^2}{2},\qquad
 \gamma=\frac{\varepsilon\alpha}{2}.
\tag{564R.2}
\]

特别 \(c,\gamma\in\mathbb F_p^\times\) 且 \(c\gamma=1\)。对绝对 Cartier 算子 \(\mathcal C\)，

\[
 \boxed{\mathcal C(R_-\omega)=cR_+\omega},\qquad
 \boxed{\mathcal C(R_+\omega)=\gamma R_-\omega}.
\tag{564R.3}
\]

这里选择 \(\alpha\) 为 \(\mathbb F_p\) 中的根是规范的一部分。若在特征零先取 \(\sqrt[3]4\)，约化时须选使该根落入 \(\mathbb F_p\) 的对应素位；不能对另一个共轭根仍不加说明地使用 (564R.2)。

## 2. 混合六挠点的显式参数

取 \(\zeta\in\mathbb F_{p^2}\) 为三次单位根。置

\[
 Q_3=(\alpha,\beta),\qquad T_2=(1,0).
\]

\(Q_3\) 是准确三阶点，\(T_2\) 是准确二阶点。考虑十八个点

\[
 P_{\delta,i,j}=[\delta]\,[\zeta^i]Q_3+[\zeta^j]T_2,
 \qquad\delta=\pm1,\quad i,j\in\mathbb Z/3\mathbb Z.
\tag{564R.4}
\]

记 \(r=\alpha\zeta^{i-j}\)，则 \(r^3=4\)。椭圆曲线加法直接给

\[
 x(P_{\delta,i,j})=\zeta^j\frac{r+2}{r-1},\qquad
 y(P_{\delta,i,j})=-\frac{3\delta\beta}{(r-1)^2}.
\tag{564R.5}
\]

\(r\ne1\)，因为 \(p\ne3\)。对 \(j=0\)，\(x=(r+2)/(r-1)\) 满足 \(x^3-6x^2-4=0\)。因此九个不同的 \(x\) 坐标恰为

\[
 \prod_{j=0}^2(x^3-6\zeta^j x^2-4)
 =(x^3-4)^3-216x^6=\Delta(x)
\tag{564R.6}
\]

的根。十八个点的二、三主分量唯一，故彼此不同；它们都不是二挠点，九个 \(x\) 坐标也不同。于是 \(\Delta\) 在所有所述 \(p\) 上均无重根。

## 3. 两个微分的全部留数

在上述十八个点之外，\(R_\pm\omega\) 均无极点；在无穷点，它们形如 \(z^2dz+\cdots\)，也正则。

直接代入 (564R.5) 可得

\[
 \operatorname{Res}_{P_{\delta,i,j}}(R_-\omega)
       =-\frac{\delta r}{72\beta},\qquad
 \operatorname{Res}_{P_{\delta,i,j}}(R_+\omega)
       =-\frac{\delta r^2}{144\beta}.
\tag{564R.7}
\]

说明这一有限代数化简的全部输入：若 \(X=x^3\)，\(D(X)=X^3-228X^2+48X-64\)，则在一个简单极点

\[
 \operatorname{Res}(R_\pm\omega)
 =\frac{X^2+(34\text{ 或 }-20)X-8}{6yD'(X)}.
\tag{564R.8}
\]

对 \(j=0,\delta=1\)，将 \(x=(r+2)/(r-1)\)、\(y=-3\beta/(r-1)^2\) 代入并用 \(r^3=4\)，即分别得到

\[
 \beta\operatorname{Res}(R_-\omega)=-r/72,
 \qquad \beta\operatorname{Res}(R_+\omega)=-r^2/144.
\]

一般 \(\delta\) 给符号 \(\delta\)。\(j\) 的改变是 \((x,y)\mapsto(\zeta^jx,y)\)，而 \(R_\pm\omega\) 在这个 \(\mu_3\) 作用下不变，所以留数不另乘单位根。该计算可在 \(\mathbb Q[r]/(r^3-4)\) 中精确核对，配套脚本只保存这两个有理恒等式的零余数证书。

## 4. Frobenius 对留数的作用

由 \(p\equiv2\pmod3\)、\(\alpha\in\mathbb F_p\)，

\[
 \zeta^p=\zeta^{-1},\qquad
 r^p=\alpha\zeta^{j-i}=\frac{\alpha^2}{r},\qquad
 \beta^p=\varepsilon\beta.
\tag{564R.9}
\]

这些点及留数都定义在 \(\mathbb F_{p^2}\)，因此取 \(1/p\) 次幂与取 \(p\) 次幂相同。由 (564R.7)–(564R.9)，

\[
 \operatorname{Res}_{P}(R_-\omega)^{1/p}
 =\frac{\varepsilon\alpha^2}{2}
       \operatorname{Res}_{P}(R_+\omega),
\]
\[
 \operatorname{Res}_{P}(R_+\omega)^{1/p}
 =\frac{\varepsilon\alpha}{2}
       \operatorname{Res}_{P}(R_-\omega).
\tag{564R.10}
\]

例如第一式左边是 \(-\delta\varepsilon\alpha^2/(72\beta r)\)，右边用 \(r^3=4\) 正好相同。

## 5. 消掉完整微分中的正则差

局部 Laurent 公式

\[
 \mathcal C\left(\sum_n a_nz^n dz\right)
 =\sum_m a_{pm+p-1}^{1/p}z^m dz
\tag{564R.11}
\]

说明 Cartier 不产生新的极点，且简单极点的留数变为原留数的 \(1/p\) 次幂。因此由 (564R.10)，两个差

\[
 \mathcal C(R_-\omega)-cR_+\omega,\qquad
 \mathcal C(R_+\omega)-\gamma R_-\omega
\]

在整条曲线上均正则。

\(R_\pm\omega\) 在 \(\sigma:(x,y)\mapsto(\zeta x,y)\) 下不变；Cartier 的自然性给其像也不变。正则微分空间是 \(k\omega\)，但 \(\sigma^*\omega=\zeta\omega\)，所以其中没有非零 \(\sigma\)-不变向量。两个正则差都只能为零，证明 (564R.3)。\(\square\)

这个步骤不能仅从“留数相同”直接跳到完整微分相等；最后的 \(\mu_3\) 权重确实消除了可能的全纯差。

## 6. 下游的准确使用范围

R601 可以使用第二式 \(\mathcal C(R_+\omega)=\gamma R_-\omega\)，其中 \(\gamma\ne0\)，配合恢复 R574 的 \(q=-B^{-1}D^{p-2}x\)、\(Dq=1\)、\(q(Q)=-B^{-1}e_Q^p\)。

本稿不包含任何阶乘消分母、模曲线 Hodge 尺度或全局 CM 商的识别。因此它不单独证明某个实际中心值非零，不给实际 \(M_0\) 或 \(M_2\) 的单位性，也不把旧固定高权 \(C_p\) 与它们等同。
