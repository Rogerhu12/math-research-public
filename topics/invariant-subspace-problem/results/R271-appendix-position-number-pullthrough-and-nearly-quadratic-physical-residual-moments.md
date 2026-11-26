# R271 附录：真实位置数算子的拉通与同源残量的近二阶物理孔矩

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下真实位置加权数算子、全部严格低于二阶的孔矩及近二阶对数权结论已证明。**
本稿继续[原数算子缺陷与同一残量](R271-appendix-actual-number-defect-and-uniform-first-moment-of-the-same-residual.md)的准确来源
$$
a_s=(I+T^*T/s)^{-1}f_1,\qquad h_s=Ta_s,\qquad f_1=e_1,\quad s>0.
$$
不改变 forcing，不改原未加权 inverse。新输入是原位权 $(i+1)^{-2}$ 的可和性。

## 1. 一般真实位置数算子及可核条件

记 $n_i=E_i^*E_i$，$\mathcal N=\sum_i n_i$ 为总物理孔数。
取真实位置权
$$
\omega_0=1,\qquad 1\le\omega_i\le A(i+1),\qquad A\ge1,\qquad
L_\omega:=\sum_{i\ge0}\frac{|\omega_i-1|}{(i+1)^2}<\infty.
\tag{1.1}
$$
在原孔基 $e_S$ 上定义正自伴对角算子
$$
\mathcal N_\omega e_S=\left(\sum_{i\in S}\omega_i\right)e_S.
$$
其自然域由上述特征值平方可和定义；有限物理向量构成核心，且
每个权都放在原物理位上，且
$
\mathcal N_\omega f_1=f_1.
\tag{1.2}
$

两个原模型的真实缺陷 $\mathcal B_\omega=T+[\mathcal N_\omega,T]$ 有有界延拓，并可统一取
$$
\boxed{\|\mathcal B_\omega\|\le D_\omega:=9L_\omega+200A\eta,\qquad \eta=e^{-1070}.}
\tag{1.3}
$

## 2. 原完整 N/Y carry 的位置费用

令
$$
X_{i,\ell}=E_i^*\cdots E_{i+\ell-1}^*E_{i+\ell},\qquad
p_{i,\ell}=\prod_{j=i}^{i+\ell-1}\eta_j,\qquad
\mathsf N_i=\sum_{\ell\ge0}p_{i,\ell}X_{i,\ell}.
$$
空积按恒等理解。第 $\ell$ 项使 $\mathcal N_\omega$ 改变
$\sum_{j=i}^{i+\ell-1}\omega_j-\omega_{i+\ell}$，故
$$
\mathsf N_i+[\mathcal N_\omega,\mathsf N_i]=(1-\omega_i)E_i+\mathcal C_{i,\omega},
\tag{2.1}
$$
$$
\mathcal C_{i,\omega}
=\sum_{\ell\ge1}\left(1+\sum_{j=i}^{i+\ell-1}\omega_j-\omega_{i+\ell}\right)
p_{i,\ell}X_{i,\ell}.
$$
由 (1.1)，括号绝对值至多 $A(\ell+2)(i+\ell+1)$。
原精确 $\eta_i$ 公式给 $\eta_i\le\eta^{16^i}\le\eta^{i+1}$，所以
$$
\sum_{i\ge0}(i+1)\frac{\eta_i}{(i+1)^2}
\le\sum_{i\ge0}\eta^{i+1}<2\eta.
\tag{2.2}
$$
又有 $p_{i,\ell}\le\eta_i\eta^{\ell-1}$、$i+\ell+1\le(\ell+1)(i+1)$，故
$$
\sum_i\frac{\|\mathcal C_{i,\omega}\|}{(i+1)^2}
\le2A\eta\sum_{\ell\ge1}(\ell+1)(\ell+2)\eta^{\ell-1}
\le16A\eta.
\tag{2.3}
$$
末和在 $0\le\eta\le1/16$ 时小于 $8$，其准确表达式为
$(6-6\eta+2\eta^2)/(1-\eta)^3$。N 型完整缺陷至多 $L_\omega+16A\eta$。

Y 型令 $R_i=(I+\mathsf N_i)^{-1}$，$\|R_i\|<3$。准确有
$$
\mathsf Y_i+[\mathcal N_\omega,\mathsf Y_i]
=\mathsf N_i^2R_i^2+
R_i\bigl(\mathsf N_i+[\mathcal N_\omega,\mathsf N_i]\bigr)R_i.
\tag{2.4}
$$
第一项给至多 $18\eta$，第二项至多 $9L_\omega+144A\eta$，证明 (1.3)。全部 Cayley 逆均保留。

这些级数同时在交换子范数中收敛。按核心、闭性与逆的单位群差商，
$T,T^*$ 保 $\operatorname{Dom}\mathcal N_\omega$，并且
$$
[\mathcal N_\omega,T]=-T+\mathcal B_\omega,\qquad
[\mathcal N_\omega,T^*]=T^*-\mathcal B_\omega^*.
\tag{2.5}
$$
原总孔数稿第3节的 resolvent 域证明因而适用，依据是 (2.5) 的真实有界交换子。

## 3. 同一残量的完整位置拉通及图范数收敛

令 $R_s=(T^*T+s)^{-1}$、$Q_s=(TT^*+s)^{-1}$。
由 (1.2)、(2.5)，同一原源满足
$$
\boxed{\mathcal N_\omega h_s=sQ_s\mathcal B_\omega a_s+TR_s\mathcal B_\omega^*h_s.}
\tag{3.1}
$$
因为 $\|a_s\|\le1$、$\|h_s\|\le\sqrt s/2$、$\|sQ_s\|\le1$、
$\|TR_s\|\le1/(2\sqrt s)$，
$$
\boxed{\|\mathcal N_\omega h_s\|\le\frac54D_\omega.}
\tag{3.2}
$$
常数不含任何强前缀长度、有限母 cut 或辅助高度。

原 $T$ 的有限三角首超对角非零，故 $\operatorname{Ran}T$ 稠密。
于是 $sQ_s\to0$ 强，$a_s\to P_Mf_1$，其中 $M=\ker T$；
谱测度有界收敛还给 $h_s/\sqrt s\to0$。代回 (3.1)，
$$
\boxed{\|h_s\|+\|\mathcal N_\omega h_s\|\longrightarrow0.}
\tag{3.3}
$$
还保持原正能量身份
$$
s\langle(\mathcal N_\omega-I)a_s,a_s\rangle+
\langle\mathcal N_\omega h_s,h_s\rangle
=\operatorname{Re}\langle h_s,\mathcal B_\omega a_s\rangle.
\tag{3.4}
$$
它由 $(T^*T+s)a_s=sf_1$ 与 $(\mathcal N_\omega-I)a_s$ 配对，
再用 $T(\mathcal N_\omega-I)a_s=\mathcal N_\omega h_s-\mathcal B_\omega a_s$ 得到。
因为 $a_s\perp\Omega$ 且所有 $\omega_i\ge1$，左边两项非负；
右边至多 $D_\omega\sqrt s/2$。此式不宣称 $a_s$ 自身的位置矩一致有界。

## 4. 全部严格低于二阶的总物理孔矩

取 $0<\alpha<1$、$\omega_i=(i+1)^\alpha$。可取 $A=1$，且
$$
L_\omega=\sum_{i\ge0}\bigl((i+1)^{\alpha-2}-(i+1)^{-2}\bigr)
\le\frac1{1-\alpha},\qquad
D_\alpha\le\frac{10}{1-\alpha}.
\tag{4.1}
$$
任意实际 $q$ 孔子集的递增位号至少为 $0,\ldots,q-1$，所以
$$
\mathcal N_\alpha|_{\mathcal H_q}\ge\sum_{i=1}^q i^\alpha
\ge\frac{q^{1+\alpha}}{1+\alpha}.
\tag{4.2}
$$
这些算子全在原同一孔基中对角。令 $p=1+\alpha\in(1,2)$，由 (3.2)–(3.3)，
$$
\boxed{\|\mathcal N^p h_s\|\le C_p:=\frac{25p}{2(2-p)},\qquad
\|\mathcal N^p h_s\|\longrightarrow0.}
\tag{4.3}
$$
低于或等于一阶的结论由前稿给出，不扩大这里 $C_p$ 的定义范围。
任何旧强前缀的物理孔数 $N_{[m,y)}$ 都受 $\mathcal N$ 控制，
所以同一 $C_p$ 同时适用于全部 $y$，包括指数增长的原窗口。

对 $1<p<2$、$0\le\theta<p$，谱测度 Hölder 给显式速率
$$
\boxed{\|\mathcal N^\theta h_s\|
\le\left(\frac{\sqrt s}{2}\right)^{1-\theta/p}C_p^{\theta/p}.}
\tag{4.4}
$$
固定 $p$ 的端点 (4.3) 没有另给速率。

## 5. 一个近二阶的真实对数权

固定 $\epsilon>0$，取
$$
c=\left\lceil e^{2(1+\epsilon)}\right\rceil,\qquad
\omega_i=\frac{i+c}{c}
\left(\frac{\log c}{\log(i+c)}\right)^{1+\epsilon}.
\tag{5.1}
$$
函数 $x/(\log x)^{1+\epsilon}$ 在 $x\ge c$ 递增，所以
$\omega_0=1$、$1\le\omega_i\le i+1$。对 $i<c$ 用后一界，
对 $i\ge c$ 用 $i+c\le2(i+1)$ 与积分比较，得
$$
L_\omega\le L_\epsilon:=1+\log c+\frac{2\log c}{c\epsilon}<\infty.
\tag{5.2}
$$
可取 $D_\epsilon=9L_\epsilon+200\eta$。在第 $q$ 孔层，
$$
\mathcal N_\omega\ge\sum_{i=0}^{q-1}\omega_i
\ge\frac{(\log c)^{1+\epsilon}}{c[\log(q+c)]^{1+\epsilon}}
\sum_{i=0}^{q-1}(i+1)
\ge\frac{(\log c)^{1+\epsilon}}{2c}
\frac{q^2}{[\log(q+c)]^{1+\epsilon}}.
\tag{5.3}
$$
故真正总孔数权 $W_\epsilon(\mathcal N)=
\mathcal N^2/[\log(\mathcal N+c)]^{1+\epsilon}$ 满足
$$
\boxed{\|W_\epsilon(\mathcal N)h_s\|
\le\frac{5cD_\epsilon}{2(\log c)^{1+\epsilon}},\qquad
\|W_\epsilon(\mathcal N)h_s\|\longrightarrow0.}
\tag{5.4}
$$
没有针对 $\epsilon$ 或窗口重选 forcing。不能直接代 $\epsilon=0$，
因为相应位置费用的调和对数级数不再可和。

## 6. 相对形式扩张与完整 log 方差积分

更强的条件只要求
$$
\omega_0=1,\qquad1\le\omega_i\le A(i+1)^3,\qquad A\ge1,\qquad
\sigma_\omega^2:=\sum_{i\ge0}a_i^2\frac{(\omega_i-1)^2}{\omega_i}<\infty,
\quad a_i=(i+1)^{-2}.
\tag{6.1}
$$
本节不假设 $T+[\mathcal N_\omega,T]$ 全空间有界，也不假设其伴随已能作用于 $h_s$。

对每个 $M_0\ge1$ 取 $\omega_i^{[M_0]}=\min(\omega_i,M_0)$，
令 $\mathcal N_{\omega,M_0}$ 为对应真实位置数算子。
截断位权满足第1节条件（可取 $A=M_0$），故每个 $M_0$ 的 (3.4) 严格成立。
准确分出主删除行与全部真实余项：
$$
\mathcal B_{\omega,M_0}=D_{M_0}+K_{M_0},\qquad
D_{M_0}=\sum_i a_i(1-\omega_i^{[M_0]})E_i.
\tag{6.2}
$$
对形式域中的 $v$，加权 Cauchy–Schwarz 给
$$
\begin{aligned}
\|D_{M_0}v\|
&\le
\left(\sum_i a_i^2\frac{(\omega_i^{[M_0]}-1)^2}{\omega_i^{[M_0]}}\right)^{1/2}
\left(\sum_i\omega_i^{[M_0]}\|E_iv\|^2\right)^{1/2}\\
&\le\sigma_\omega\|\mathcal N_{\omega,M_0}^{1/2}v\|.
\end{aligned}
\tag{6.3}
$$
函数 $(x-1)^2/x=x-2+x^{-1}$ 在 $x\ge1$ 单调，
第二平方和准确等于原位置占据形式。

全部 carry 系数仍有
$$
\left|1+\sum_{j=i}^{i+\ell-1}\omega_j^{[M_0]}-\omega_{i+\ell}^{[M_0]}\right|
\le A(\ell+2)(i+\ell+1)^3.
$$
使用
$\sum_i a_i(i+1)^3\eta_i=\sum_i(i+1)\eta_i\le2\eta$、
$(\ell+2)(\ell+1)^3\le24\ell^4$ 和
$\sum_{\ell\ge1}\ell^4\eta^{\ell-1}<2$（$\eta<1/1024$），
N 型所有 carry 之和至多 $96A\eta$，与 $M_0$ 无关。

为核完整 Y 型，置 $R_i^0=I-E_i$。原恒等式和
$\|\mathsf N_i-E_i\|\le\eta_i$ 给
$$
\|R_i-R_i^0\|\le6\eta_i,\qquad
R_i^0E_iR_i^0=E_i,\qquad
\|R_iE_iR_i-E_i\|\le30\eta_i.
$$
从 (2.4) 减去 $(1-\omega_i^{[M_0]})E_i$ 后，真实余项是
$$
\mathsf N_i^2R_i^2+
R_i\mathcal C_{i,\omega^{[M_0]}}R_i+
(1-\omega_i^{[M_0]})(R_iE_iR_i-E_i).
$$
三项乘 $a_i$ 全部求和分别至多 $18\eta$、$864A\eta$、$120A\eta$；
末项使用 $\sum_i a_i|1-\omega_i^{[M_0]}|\eta_i\le4A\eta$。
因此两个模型统一有
$$
\boxed{\|K_{M_0}\|\le2048A\eta.}
\tag{6.4}
$$
因为 $a_s\perp\Omega$ 且 $\mathcal N_{\omega,M_0}\ge I$ 于 $\Omega^\perp$，
$$
\|\mathcal B_{\omega,M_0}a_s\|
\le C_\omega\|\mathcal N_{\omega,M_0}^{1/2}a_s\|,
\qquad C_\omega:=\sigma_\omega+2048A\eta.
\tag{6.5}
$$
记
$X_{M_0}^2=\langle(\mathcal N_{\omega,M_0}-I)a_s,a_s\rangle$、
$Y_{M_0}^2=\langle\mathcal N_{\omega,M_0}h_s,h_s\rangle$。
同一正身份给
$$
sX_{M_0}^2+Y_{M_0}^2
\le C_\omega\|h_s\|\sqrt{X_{M_0}^2+\|a_s\|^2}
\le C_\omega\|h_s\|(X_{M_0}+\|a_s\|).
$$
对 $X_{M_0}$ 完成平方，再仅对非负对角形式取单调极限 $M_0\to\infty$，得
$$
\boxed{
h_s\in\operatorname{Dom}\mathcal N_\omega^{1/2},\qquad
\|\mathcal N_\omega^{1/2}h_s\|^2
\le\frac{C_\omega^2}{4s}\|h_s\|^2+C_\omega\|h_s\|\,\|a_s\|.
}
\tag{6.6}
$$
没有在极限中施加未知 $\mathcal B_\omega^*$。
由于 $h_s/\sqrt s\to0$，
$$
\boxed{\|\mathcal N_\omega^{1/2}h_s\|\longrightarrow0.}
\tag{6.7}
$$
在 $0<s\le1$ 上，统一平方上界可取 $C_\omega^2/16+C_\omega/2$。

完整 log 方差积分也已支付。原谱测度给
$$
\int_0^\infty\frac{\|h_s\|^2}{s^2}\,ds
=\|(I-P_M)f_1\|^2\le1,\qquad M=\ker T,
\tag{6.8}
$$
因为每个 $\lambda>0$ 的标量积分为
$\int_0^\infty\lambda(\lambda+s)^{-2}ds=1$，$\lambda=0$ 的贡献为零。
将 (6.6) 除以 $s$ 并在 $(0,1)$ 积分，再用
$\|h_s\|\le\sqrt s/2$、$\|a_s\|\le1$，得
$$
\boxed{\int_0^1\|\mathcal N_\omega^{1/2}h_s\|^2\frac{ds}{s}
\le\frac{C_\omega^2}{4}+C_\omega.}
\tag{6.9}
$$
所有被积量来自同一原来源。也可先截权再用非负单调收敛积分。

## 7. 任意对数指数大于二分之一的近二阶权

固定 $\epsilon>0$，取 $c=\lceil e^{2(1+\epsilon)}\rceil$，现在改用
$$
\omega_i=\left(\frac{i+c}{c}\right)^3
\left(\frac{\log c}{\log(i+c)}\right)^{1+\epsilon}.
\tag{7.1}
$$
仍有 $\omega_0=1$、单调递增、$1\le\omega_i\le(i+1)^3$，故可取 $A=1$。
头尾分别求和给
$$
\sigma_\omega^2\le\sum_i a_i^2\omega_i
\le1+\log c+\frac{8\log c}{c^3\epsilon}<\infty.
\tag{7.2}
$$
前 $c$ 项至多 $\sum_{n\le c}1/n$；后项使用
$\sum_{n>c}[n(\log n)^{1+\epsilon}]^{-1}
\le(\log c)^{-\epsilon}/\epsilon$。

对真实 $q$ 孔层，单调性给
$$
\begin{aligned}
\mathcal N_\omega|_{\mathcal H_q}
&\ge\sum_{i=0}^{q-1}\omega_i\\
&\ge\frac{(\log c)^{1+\epsilon}}{c^3[\log(q+c)]^{1+\epsilon}}
\sum_{i=0}^{q-1}(i+1)^3\\
&\ge\frac{(\log c)^{1+\epsilon}}{4c^3}
\frac{q^4}{[\log(q+c)]^{1+\epsilon}}.
\end{aligned}
\tag{7.3}
$$
取平方根，再用 (6.6)–(6.7)，得到
$$
\boxed{\left\|\frac{\mathcal N^2}
{[\log(\mathcal N+c)]^{(1+\epsilon)/2}}h_s\right\|\longrightarrow0.}
\tag{7.4}
$$
其 $0<s\le1$ 显式统一上界为
$$
\frac{2c^{3/2}}{(\log c)^{(1+\epsilon)/2}}
\left(\frac{C_\omega^2}{16}+\frac{C_\omega}{2}\right)^{1/2}.
$$
任意 $\theta>1/2$ 取 $\epsilon=2\theta-1$ 即可。
端点 $\theta=1/2$ 未由本稿证明。

同一总孔权保 (6.9) 的 log 方差平方积分，常数只乘
$4c^3/(\log c)^{1+\epsilon}$。
因此在任意 $e^{-2L}\le s\le e^{-L}$、$L>0$，一次共同方差选择使
该加权残量平方不超过此积分常数除以 $L$。
选择不需为每个后续前缀 $y$ 重做。

## 8. 对原清除接口的范围

所有估计使用同一个 $a_s$、$h_s$、原 $J=1$ inverse 及全部物理位。
对每个 $w\in\ker T$ 仍有
$\langle w,a_s\rangle=\langle w,f_1\rangle$。
本稿去除了残量旧前缀多项式孔矩中的粗 $y$ 因子。

这些矩仍不控制完整指数范数
$\sum_qe^{\kappa q}\|P_qh_s\|$，
也不自动给清除后核向量的正则性。
原同源物理 MP 返回、真 $F_0/S_x$ 的绝对 $\mathcal Z_\gamma$、
全 $J$ 接口及普通 Hilbert ISP 继续开放。
